"""Préparation des lectures des deux moniteurs à modèle de langue du bras A des organismes discrets : l'étape qui
sépare ce qui connaît les conditions de ce qui produit les scores (mot de la mère du 19 novembre, reprise E de la
relecture `docs/notes/relecture-fable-ecarts-qui-concoit-v1.md`, § 2.4).

Deux étapes, deux côtés :

- **l'étape de préparation** (ce module, fonctions `preparer` et `ecrire_*`) est la seule à lire le fichier des textes
  d'action, qui dit la condition de chaque action, et la table des identifiants opaques. Elle construit le message de
  chaque action lue, tire le sous-échantillon du juge, dérive la graine de chaque lecture, et écrit pour un moniteur un
  **fichier scellé de demandes** à trois champs — identifiant opaque, message, graine — dans l'ordre trié des
  identifiants. Elle garde de son côté, dans un bilan scellé à part, le compte par condition des actions non lues ;
- **l'étape de production** ne reçoit que ce fichier de demandes (`lire_les_demandes`). Ni son nom, ni son chemin, ni
  ses champs ne disent la condition, la dose, la tâche ou le rang de l'action ; tout champ de plus est refusé.

Limite, à dire : le message porte le texte de l'agent, que le moniteur lit par nature. L'opacité ne cache pas ce que le
texte lui-même laisse voir.

Ce module ne charge aucun modèle. Il réemploie le message, les clés de graine et le tirage du sous-échantillon du
module des deux moniteurs (`moniteurs_langue_v3`), sans les récrire.

Version 2 : seul change le module des deux moniteurs importé, pris en version 3 (les fonctions employées ici — message,
demande, clé de graine, positions du juge — y sont inchangées), pour qu'un lanceur ne charge qu'une version de ce module.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from ... import manifeste
from ...gardes import GardeArret
from ...scellement import sceller
from ..bras_a_v2_habilite import moniteurs_langue_v3 as ml

MONITEURS = tuple(ml.MONITEURS)                                  # « moniteur-boite-noire », « juge »
JUGE = "juge"
ROLES_LUS = ("honnete", "dose-0.25", "dose-0.50", "dose-0.75", "dose-1.00")
CHAMPS_DEMANDE = ("cle", "utilisateur", "graine")
_OPAQUE = re.compile(r"^[0-9a-f]{16}$")
N_EPISODES = 8


def fichier_des_demandes(moniteur: str) -> str:
    return f"demandes-{moniteur}.jsonl"


def fichier_du_bilan(moniteur: str) -> str:
    return f"bilan-preparation-{moniteur}.json"


def _journaux(actions: list[dict], T: int) -> dict[tuple, list[dict]]:
    """Actions groupées par épisode (condition, tâche, rang), dans l'ordre des pas ; chaque épisode a ses T pas."""
    episodes: dict[tuple, list[dict]] = {}
    for a in actions:
        if a["condition"] not in ROLES_LUS:
            raise GardeArret("préparation : action hors des cinq conditions lues par les moniteurs")
        episodes.setdefault((a["condition"], a["tache"], a["episode"]), []).append(a)
    for cle, pas in episodes.items():
        pas.sort(key=lambda a: a["pas"])
        if [a["pas"] for a in pas] != list(range(T)):
            raise GardeArret(f"préparation : l'épisode {cle[1]}/e{cle[2]} n'a pas ses {T} pas, de 0 à {T - 1}")
    return episodes


def preparer(actions: list[dict], questions: dict[str, str], table: dict[str, str], entropie: int, moniteur: str,
             T: int = 10) -> tuple[list[dict], dict]:
    """Demandes d'un moniteur, sous identifiants opaques et dans leur ordre trié, et bilan par condition.

    `actions` : lignes du fichier des textes réduites aux cinq conditions lues, la condition étant son rôle (forme de
    `autres_moniteurs.lignes_des_cinq_conditions`). `questions` : énoncé de chaque tâche, tel que l'agent le voit.
    `table` : identifiant opaque → clé d'action. Pour le juge, seules les positions de son sous-échantillon sont
    préparées (tirées par la clé de la tâche, les mêmes dans les cinq conditions). Une action non appliquée n'a pas de
    demande : elle est comptée non lue, par condition, sans remplacement."""
    if moniteur not in MONITEURS:
        raise GardeArret(f"préparation : moniteur {moniteur!r} : {MONITEURS} attendus")
    if not (isinstance(entropie, int) and not isinstance(entropie, bool) and entropie >= 0):
        raise GardeArret("préparation : entropie racine entière, positive ou nulle, attendue")
    if not isinstance(table, dict) or not all(isinstance(k, str) and _OPAQUE.fullmatch(k) for k in table) or \
            len(set(table.values())) != len(table):
        raise GardeArret("préparation : table des identifiants opaques hors format")
    opaque = {v: k for k, v in table.items()}
    episodes = _journaux(actions, T)
    taches = sorted({cle[1] for cle in episodes})
    manquantes = [t for t in taches if not isinstance(questions.get(t), str) or not questions[t]]
    if manquantes:
        raise GardeArret(f"préparation : énoncé absent pour {len(manquantes)} tâche(s), la première : {manquantes[0]}")
    positions = None
    if moniteur == JUGE:
        positions = {t: set(ml.positions_du_juge_pour(entropie, t, N_EPISODES, T)) for t in taches}
    cles_de_graine = sorted({ml.cle_de_graine(moniteur, t, e, p) for (_, t, e) in episodes for p in range(T)})
    graines = manifeste.graines(cles_de_graine, entropie)
    demandes = []
    bilan = {r: {"actions": 0, "hors_du_sous_echantillon": 0, "non_lues": 0, "demandes": 0,
                 "marqueur_dans_le_texte_de_l_agent": 0, "hors_forme_composee": 0} for r in ROLES_LUS}
    for (condition, tache, episode), pas in sorted(episodes.items()):
        journal = [(0, a["pas"], a["texte"]) for a in pas]
        for a in pas:
            b = bilan[condition]
            b["actions"] += 1
            if positions is not None and (episode, a["pas"]) not in positions[tache]:
                b["hors_du_sous_echantillon"] += 1
                continue
            m = ml.message_du_moniteur(questions[tache], journal, a["pas"], T)
            if not m["lu"]:
                b["non_lues"] += 1
                continue
            if a["cle"] not in opaque:
                raise GardeArret("préparation : une action lue n'a pas d'identifiant opaque dans la table")
            b["demandes"] += 1
            b["marqueur_dans_le_texte_de_l_agent"] += int(m["marqueur_dans_le_texte_de_l_agent"])
            b["hors_forme_composee"] += int(not m["forme_composee"])
            demandes.append({"cle": opaque[a["cle"]], "utilisateur": m["utilisateur"],
                             "graine": ml.graine_entiere(graines[ml.cle_de_graine(moniteur, tache, episode, a["pas"])])})
    demandes.sort(key=lambda d: d["cle"])
    for d in demandes:
        exiger_demande_preparee(d)
    return demandes, bilan


def exiger_demande_preparee(d: dict) -> None:
    """Une demande remise à l'étape de production : trois champs et eux seuls. Ni condition, ni dose, ni tâche, ni
    rang d'épisode ou de pas, ni clé d'action en clair."""
    if not isinstance(d, dict) or tuple(d) != CHAMPS_DEMANDE:
        raise GardeArret(f"demande préparée : champs {list(CHAMPS_DEMANDE)} attendus, dans cet ordre, aucun autre "
                         "(ni condition, ni tâche, ni rang) : refusée")
    if not (isinstance(d["cle"], str) and _OPAQUE.fullmatch(d["cle"])):
        raise GardeArret("demande préparée : clé non opaque (une clé d'action dit sa condition en clair) : refusée")
    if not (isinstance(d["utilisateur"], str) and d["utilisateur"].startswith(ml.ENTETE_QUESTIONS + "\n")):
        raise GardeArret("demande préparée : message hors format")
    if not (isinstance(d["graine"], int) and not isinstance(d["graine"], bool) and d["graine"] >= 0):
        raise GardeArret("demande préparée : graine entière, positive ou nulle, attendue")


def ecrire_les_demandes(dossier: str | Path, moniteur: str, demandes: list[dict]) -> dict:
    """Écrit et scelle le fichier des demandes d'un moniteur, dans l'ordre trié des identifiants. Rien n'est écrasé."""
    if moniteur not in MONITEURS:
        raise GardeArret(f"préparation : moniteur {moniteur!r} : {MONITEURS} attendus")
    chemin = Path(dossier) / fichier_des_demandes(moniteur)
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : on n'écrase jamais (R12)")
    cles = [d.get("cle") if isinstance(d, dict) else None for d in demandes]
    for d in demandes:
        exiger_demande_preparee(d)
    if cles != sorted(set(cles)):
        raise GardeArret("demandes préparées : identifiants en double, ou hors de leur ordre trié")
    Path(dossier).mkdir(parents=True, exist_ok=True)
    with open(chemin, "w", encoding="utf-8", newline="\n") as f:
        for d in demandes:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
    return {"fichier": chemin.name, "chemin": chemin, "sha256": sceller(chemin), "lignes": len(demandes)}


def ecrire_le_bilan(dossier_a_part: str | Path, moniteur: str, bilan: dict, demandes_sha256: str) -> dict:
    """Écrit et scelle, **dans un dossier tenu à part de l'étape de production**, le bilan par condition de la
    préparation (actions, hors du sous-échantillon, non lues, demandes) et l'empreinte du fichier des demandes."""
    chemin = Path(dossier_a_part) / fichier_du_bilan(moniteur)
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : on n'écrase jamais (R12)")
    if set(bilan) != set(ROLES_LUS):
        raise GardeArret("bilan de la préparation : une entrée par condition lue attendue")
    Path(dossier_a_part).mkdir(parents=True, exist_ok=True)
    contenu = {"moniteur": moniteur, "demandes_sha256": demandes_sha256, "par_condition": bilan}
    chemin.write_text(json.dumps(contenu, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"fichier": chemin.name, "chemin": chemin, "sha256": sceller(chemin)}


def lire_les_demandes(chemin: str | Path, consigne: str) -> tuple[list[dict], dict[str, int]]:
    """Entrée de l'étape de production : le fichier scellé des demandes, et lui seul. Rend les demandes dans la forme
    qu'attend la lecture avec raisonnement (clé, consigne, message) et la graine de chaque lecture. Le nom du fichier
    doit être celui d'un fichier de demandes : aucun autre fichier n'entre par ici."""
    chemin = Path(chemin)
    if chemin.name not in {fichier_des_demandes(m) for m in MONITEURS}:
        raise GardeArret(f"{chemin.name} : ce n'est pas un fichier de demandes préparées : l'étape de production n'en "
                         "lit aucun autre")
    compagnon = Path(str(chemin) + ".sha256")
    if not chemin.is_file() or not compagnon.is_file():
        raise GardeArret(f"{chemin} : fichier ou empreinte compagnon absent")
    if compagnon.read_text(encoding="utf-8").split()[:1] != [hashlib.sha256(chemin.read_bytes()).hexdigest()]:
        raise GardeArret(f"{chemin} : empreinte ≠ compagnon : le fichier a changé depuis son scellement")
    ml.exiger_consigne(consigne)
    demandes, graines = [], {}
    for ligne in chemin.read_text(encoding="utf-8").splitlines():
        d = json.loads(ligne)
        exiger_demande_preparee(d)
        if d["cle"] in graines:
            raise GardeArret("demandes préparées : identifiant en double")
        graines[d["cle"]] = d["graine"]
        demandes.append({"cle": d["cle"], "systeme": consigne, "utilisateur": d["utilisateur"]})
    return demandes, graines
