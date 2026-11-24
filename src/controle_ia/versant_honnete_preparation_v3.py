"""Préparation des quatre entrées du code d'analyse du versant honnête (`versant_honnete_v7.py`), version 3 (classe B).

v3 : bâtie sur la passe v3 ; lecteur : le code d'analyse v7 (commit ab094582), qui lit un score existant `null` comme
« absent » (pont partiel, réserve, sans arrêt). Aucun calcul ne change. v2 : `versant_honnete_preparation_v2.py`
(4a1acf67…), inchangée.

v2 : bâtie sur la passe v2 (`versant_honnete_passe_v2`) ; un score existant non fini est écrit `null`, jamais NaN (le
code d'analyse v7 lira `null` comme « absent » pour la source « existant » ; défaut 1 de la contre-lecture de Sonnet) ;
le nombre de ces scores est au bordereau. Sous-contrôles éprouvés un à un (source du juge, scores existants hors
de la confirmation). v1 : `versant_honnete_preparation_v1.py` (deaee441…), inchangée.

Le texte scellé (`prereg/versant-honnete-jumeau-v3.md`, plan d'analyse, point 1) dit : « les quatre entrées du code
(rôles `episodes`, `scores`, `couts`, `fiche`) sont dérivées de ces sources par la préparation, et leurs empreintes sont
inscrites à leur création ». Ce module les écrit, avec leur liste blanche empreintée, à partir de :
  - textes des deux courses (épisodes, empreinte des textes d'épisode) : mêmes fichiers et mêmes gardes que la passe
    (`versant_honnete_passe_v3` : filtre des conditions, clés reconstruites, comptes) ;
  - manifestes des deux courses (clés de graines : `tache/<tâche>` pour la course de confirmation, chaîne de T0.6,
    `lanceur.jouer_evaluation` ; `etalonnage/tache/<tâche>/e<k>` pour l'étalonnage, `t08/course_v1.cle_etalonnage`) ;
    la graine d'un épisode est l'entier `harnais.run_harnais_factice.graine_entiere` de sa clé ;
  - mesures des deux courses (`mesures-t06.npz`, `mesures-etalonnage-t08.npz`) : champ `cout`, écrit par le **même
    lecteur** dans les deux courses (`t06.cout.cout_action`, appelé par `t06/lanceur.jouer_evaluation` et par
    `t08/course_v1.ligne_mesures`), NaN pour un coût illisible → `null` ; un coût nul ou négatif passe tel quel (le code
    d'analyse le refuse et renvoie un nœud, précision 9 : aucun coût n'est rangé ici parmi les illisibles) ;
  - lectures des quatre juges (`lectures-J8-raisonnement`, `-J8-une_passe`, `-J3-raisonnement`, `-J3-une_passe`) :
    surveillants `J8r` (principal), `J8p`, `J3r`, `J3p` ; champ `score` tel quel (`null` pour une action non lue :
    statut « regle » ou anomalie) ; condition des lignes : « etalonnage » pour les épisodes d'étalonnage (nom de
    rangement de T0.8), « honnete » pour la course de confirmation ; toute autre condition est écartée et comptée ;
  - scores existants des sondes (`scores-actions-t07.npz`, pont seul) : `scores_<k>`, k le rang du nom dans l'index ;
    lignes de la condition honnête seulement, source « existant » ;
  - sortie de la passe : bordereau de la passe (toutes gardes tenues), fichier des scores repassés à l'empreinte du
    bordereau, source « repasse ».
Fiche : trois sondes principales (texte scellé, « Métrique »), aucune rapportée, juge principal `J8r`, juges rapportés
`J8p`, `J3r`, `J3p`, apprentissage vide pour chaque sonde, tolérance du pont `null` (valeurs de principe : la garde de la
course de confirmation porte sur des activations, texte scellé, « Seuil »).

Réserve déclarée : le format `.npz` ne permet pas de ne pas lire depuis le disque les lignes des autres conditions des
mesures et des scores existants ; elles sont écartées dans la fonction de lecture, et aucune n'en sort.
Éprouvé sur données factices seulement ; écrit par un auteur aveugle (aucune donnée réelle lue).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from . import versant_honnete_passe_v3 as vp
from .gardes import GardeArret
from .scellement import sceller, verifier

VERSION = "versant_honnete_preparation_v3"
JUGES = (("J8r", "juge_J8_raisonnement"), ("J8p", "juge_J8_une_passe"), ("J3r", "juge_J3_raisonnement"),
         ("J3p", "juge_J3_une_passe"))
JUGE_PRINCIPAL = "J8r"
CONDITION_JUGE_ETALONNAGE = "etalonnage"
NOMS = {"episodes": "episodes.jsonl", "scores": "scores.jsonl", "couts": "couts.jsonl", "fiche": "fiche.json",
        "liste_blanche": "liste_blanche.json", "bordereau": "bordereau-preparation-vh-v3.json"}


@dataclass(frozen=True)
class SpecPreparation:
    passe: vp.Specification
    chemins: tuple[tuple[str, str], ...]        # rôle → chemin sous la racine
    empreintes: tuple[tuple[str, str], ...]     # rôle → sha256 attendu

    def chemin(self, role: str) -> str:
        return dict(self.chemins)[role]

    def empreinte(self, role: str) -> str:
        return dict(self.empreintes)[role]


ROLES = ("mesures_confirmation", "mesures_etalonnage", "manifeste_confirmation", "manifeste_etalonnage",
         "juge_J8_raisonnement", "juge_J8_une_passe", "juge_J3_raisonnement", "juge_J3_une_passe", "existants")

SPEC_REELLE = SpecPreparation(
    passe=vp.SPECIFICATION_REELLE,
    chemins=(("mesures_confirmation", "donnees/20261111-151701-t06-reel/mesures-t06.npz"),
             ("mesures_etalonnage", "donnees/20261123-060509-t08-reel/mesures-etalonnage-t08.npz"),
             ("manifeste_confirmation", "runs/20261111-151701-t06-reel/manifeste.json"),
             ("manifeste_etalonnage", "runs/20261123-060509-t08-reel/manifeste.json"),
             ("juge_J8_raisonnement", "donnees/20261123-060509-t08-reel/lectures-J8-raisonnement-t08.jsonl"),
             ("juge_J8_une_passe", "donnees/20261123-060509-t08-reel/lectures-J8-une_passe-t08.jsonl"),
             ("juge_J3_raisonnement", "donnees/20261123-060509-t08-reel/lectures-J3-raisonnement-t08.jsonl"),
             ("juge_J3_une_passe", "donnees/20261123-060509-t08-reel/lectures-J3-une_passe-t08.jsonl"),
             ("existants", "donnees/20261114-001352-t07-lecture-reel/scores-actions-t07.npz")),
    empreintes=(("mesures_confirmation", "aca5afd068a8749952c7424a7708a1e4c8b78c082fba495d5d406f2605435049"),
                ("mesures_etalonnage", "67b0ff4c6ce28fb8422a21936438038357123f7df765a57f57195074f86b6f24"),
                ("manifeste_confirmation", "7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6"),
                ("manifeste_etalonnage", "dbb2723e4ef9b58c1b7351705b86fb302ece0504f84af0e709e2706bed9ca382"),
                ("juge_J8_raisonnement", "6ee6a974a6c0b76fd5a5a38ac6f92501a88432131f06651fc151f4f525d1b5c1"),
                ("juge_J8_une_passe", "85f1af7c10c0788ccdc06a7a145f92c9a89254cd169915f0eaf07c0ee0044b55"),
                ("juge_J3_raisonnement", "7d8f13ea19ef7f0223dca69762e032b3dc6abe6b1e829e92a60d8011b925b8d8"),
                ("juge_J3_une_passe", "0913bf6fb7efac4b20a133787ac5702223f7155527fccbb8264af8f3b86b2007"),
                ("existants", "13ac4480035f1ef6d4ea8ac81ffa962c1324e4e9e90a78c1d4f569f2abd0509d")),
)


def _arret(message: str) -> GardeArret:
    return GardeArret(f"[preparation] {message}")


def _lire(racine: Path, spec: SpecPreparation, role: str) -> Path:
    chemin = Path(racine) / spec.chemin(role)
    vp.lire_sous_empreinte(chemin, spec.empreinte(role), role)
    return chemin


# -------------------------------------------------------------------------------------------------- épisodes et actions
def actions_et_taches(racine: Path, spec: SpecPreparation) -> tuple[list, list, dict]:
    """Mêmes lectures et mêmes gardes que la passe (textes, filtre des conditions, clés, comptes)."""
    trace = vp.Trace()
    taches, actions, _, _ = vp._charger_entrees(spec.passe, _ParamsTextes(racine), trace, vp.Defauts())
    return taches, actions, trace.comptes


class _ParamsTextes:
    """La préparation ne lit pas les sondes : `_charger_entrees` ne vérifie que les fichiers qu'on lui donne."""

    def __init__(self, racine):
        self.racine = Path(racine)

    def fichiers_sondes(self) -> dict:
        return {}


def lignes_episodes(actions: list, graines: dict) -> list[dict]:
    from .harnais.run_harnais_factice import graine_entiere
    groupes: dict = {}
    for a in actions:
        groupes.setdefault(a.cle_episode, []).append(a)
    sortie = []
    for (source, tache, k), acts in sorted(groupes.items()):
        cle = f"tache/{tache}" if source == "confirmation" else f"etalonnage/tache/{tache}/e{k}"
        g = graines[source].get(cle)
        if g is None:
            raise _arret(f"clé de graine {cle!r} absente du manifeste ({source})")
        textes = [a.texte for a in sorted(acts, key=lambda a: a.pas)]
        sortie.append({"tache": tache, "episode": acts[0].episode_analyse, "condition": vp.CONDITION_HONNETE,
                       "graine": int(graine_entiere(g)),
                       "empreinte_texte": hashlib.sha256(json.dumps(textes, ensure_ascii=False).encode("utf-8")).hexdigest()})
    return sortie


def graines_des_manifestes(racine: Path, spec: SpecPreparation) -> dict:
    from .manifeste import lire_manifeste
    sortie = {}
    for source, role in (("confirmation", "manifeste_confirmation"), ("etalonnage", "manifeste_etalonnage")):
        m, _ = lire_manifeste(_lire(racine, spec, role))
        sortie[source] = m["graines"]
    return sortie


# -------------------------------------------------------------------------------------------------- coûts
def lignes_couts(racine: Path, spec: SpecPreparation, actions: list) -> tuple[list[dict], dict]:
    par_cle = {a.cle: a for a in actions}
    vus, ecartees, sortie = set(), {}, []
    for source, role in (("confirmation", "mesures_confirmation"), ("etalonnage", "mesures_etalonnage")):
        with np.load(_lire(racine, spec, role), allow_pickle=False) as z:
            manque = {"cle", "condition", "tache", "pas", "cout"} - set(z.files)
            if manque:
                raise _arret(f"{role} : tableaux absents {sorted(manque)}")
            cond = z["condition"].astype(str)
            garde = cond == vp.CONDITION_HONNETE
            ecartees[role] = int((~garde).sum())
            cles, taches, pas, couts = (z["cle"].astype(str)[garde], z["tache"].astype(str)[garde],
                                        z["pas"][garde], z["cout"].astype(np.float64)[garde])
        for c, t, p, v in zip(cles.tolist(), taches.tolist(), pas.tolist(), couts.tolist()):
            a = par_cle.get(c)
            if a is None or a.source != source or a.tache != t or a.pas != int(p):
                raise _arret(f"{role} : action {c} absente des textes de sa source, ou tâche ou pas autres")
            if c in vus:
                raise _arret(f"{role} : coût en double pour {c}")
            vus.add(c)
            sortie.append({"tache": t, "episode": a.episode_analyse, "action": int(p),
                           "cout": None if math.isnan(v) else float(v), "condition": vp.CONDITION_HONNETE})
    if vus != set(par_cle):
        raise _arret(f"coûts : {len(set(par_cle) - vus)} action(s) sans ligne de mesure")
    return sortie, ecartees


# -------------------------------------------------------------------------------------------------- juges
def lignes_juges(racine: Path, spec: SpecPreparation, actions: list) -> tuple[list[dict], dict]:
    par_cle = {a.cle: a for a in actions}
    sortie, ecartees = [], {}
    for nom, role in JUGES:
        vus, n_ec = set(), 0
        contenu = _lire(racine, spec, role).read_bytes().decode("utf-8")
        for k, brute in enumerate(contenu.splitlines(), start=1):
            if not brute.strip():
                continue
            x = json.loads(brute)
            c = x.get("condition")
            if c == CONDITION_JUGE_ETALONNAGE:
                source = "etalonnage"
            elif c == vp.CONDITION_HONNETE:
                source = "confirmation"
            else:
                n_ec += 1
                continue
            if not {"cle", "score", "statut"} <= set(x):
                raise _arret(f"{role}, ligne {k} : champs cle, score ou statut absents")
            a = par_cle.get(x["cle"])
            if a is None or a.source != source:
                raise _arret(f"{role}, ligne {k} : action {x['cle']} hors des épisodes honnêtes de sa source")
            if x["cle"] in vus:
                raise _arret(f"{role} : lecture en double pour {x['cle']}")
            vus.add(x["cle"])
            s = x["score"]
            if s is not None and (isinstance(s, bool) or not isinstance(s, (int, float)) or not math.isfinite(s)):
                raise _arret(f"{role}, ligne {k} : score {s!r} non numérique ou non fini")
            sortie.append({"surveillant": nom, "tache": a.tache, "episode": a.episode_analyse, "action": a.pas,
                           "score": None if s is None else float(s), "source": "etalonnage",
                           "condition": vp.CONDITION_HONNETE})
        if vus != set(par_cle):
            raise _arret(f"{role} : {len(set(par_cle) - vus)} action(s) honnête(s) sans lecture")
        ecartees[role] = n_ec
    return sortie, ecartees


# -------------------------------------------------------------------------------------------------- scores de sondes
def lignes_existants(racine: Path, spec: SpecPreparation, actions: list) -> tuple[list[dict], dict]:
    noms = [s.nom for s in spec.passe.sondes]
    conf = {(a.tache, a.pas): a for a in actions if a.source == "confirmation"}
    sortie = []
    with np.load(_lire(racine, spec, "existants"), allow_pickle=False) as z:
        index = json.loads(bytes(z["index"]).decode("utf-8"))
        rangs = {}
        for n in noms:
            r = [k for k, e in enumerate(index["sondes"]) if e["nom"] == n]
            if len(r) != 1:
                raise _arret(f"scores existants : sonde {n} {'absente' if not r else 'en double'} dans l'index")
            rangs[n] = r[0]
        garde = z["condition"].astype(str) == vp.CONDITION_HONNETE
        ecartees = int((~garde).sum())
        taches, pas = z["tache"].astype(str)[garde].tolist(), z["pas"][garde].tolist()
        valeurs = {n: z[f"scores_{rangs[n]}"].astype(np.float64)[garde] for n in noms}
    non_finis = 0
    for n in noms:
        for t, p, v in zip(taches, pas, valeurs[n].tolist()):
            if (t, int(p)) not in conf:
                raise _arret(f"scores existants : action ({t}, pas {p}) hors des épisodes honnêtes de la confirmation")
            fini = math.isfinite(v)
            non_finis += 0 if fini else 1
            sortie.append({"surveillant": n, "tache": t, "episode": vp.EPISODE_CONFIRMATION, "action": int(p),
                           "score": float(v) if fini else None, "source": "existant", "condition": vp.CONDITION_HONNETE})
    manquants = len(conf) - len(taches)
    return sortie, {"lignes_ecartees": ecartees, "actions_sans_score_existant": manquants,
                    "scores_existants_non_finis_ecrits_null": non_finis}


def lignes_repassees(passe_bordereau: Path, passe_sha: str, spec: SpecPreparation, actions: list) -> tuple[list, dict]:
    b = json.loads(vp.lire_sous_empreinte(passe_bordereau, passe_sha, "bordereau de la passe").decode("utf-8"))
    pas_tenues = {k: v for k, v in b["gardes"].items() if v != "tenue"}
    if pas_tenues:
        raise _arret(f"bordereau de la passe : gardes non tenues {pas_tenues}")
    chemin = Path(passe_bordereau).parent / vp.NOM_SCORES
    contenu = vp.lire_sous_empreinte(chemin, b["fichiers"][vp.NOM_SCORES], "scores repassés")
    noms = {s.nom for s in spec.passe.sondes}
    attendues = {(n, a.tache, a.episode_analyse, a.pas) for n in noms for a in actions}
    sortie, vus = [], set()
    for k, brute in enumerate(contenu.decode("utf-8").splitlines(), start=1):
        x = json.loads(brute)
        if tuple(sorted(x)) != tuple(sorted(vp.CHAMPS_SCORES_ANALYSE)) or x["source"] != vp.SOURCE_SCORES \
                or x["condition"] != vp.CONDITION_HONNETE:
            raise _arret(f"scores repassés, ligne {k} : champs, source ou condition inattendus")
        cle = (x["surveillant"], x["tache"], x["episode"], x["action"])
        if cle not in attendues or cle in vus:
            raise _arret(f"scores repassés, ligne {k} : {cle} hors des actions attendues, ou en double")
        vus.add(cle)
        sortie.append(x)
    if vus != attendues:
        raise _arret(f"scores repassés : {len(attendues - vus)} ligne(s) manquante(s)")
    return sortie, {"bordereau": passe_sha, "scores": b["fichiers"][vp.NOM_SCORES],
                    "scores_nuls": sum(x["score"] is None for x in sortie)}


def fiche(spec: SpecPreparation) -> dict:
    noms = [s.nom for s in spec.passe.sondes]
    return {"sondes_principales": noms, "sondes_rapportees": [], "juge_principal": JUGE_PRINCIPAL,
            "juges_rapportes": [n for n, _ in JUGES if n != JUGE_PRINCIPAL], "apprentissage": {n: [] for n in noms},
            "tolerance_pont": None}


# -------------------------------------------------------------------------------------------------- déroulé
def preparer(racine: Path, sortie: Path, passe_bordereau: Path, passe_sha: str, spec: SpecPreparation = SPEC_REELLE) -> dict:
    sortie = vp.exiger_hors_coffre(Path(sortie))
    vp.exiger_hors_coffre(Path(racine))
    vp.exiger_hors_coffre(Path(passe_bordereau))
    if sortie.exists():
        raise _arret(f"{sortie} existe déjà (R12)")
    taches, actions, comptes = actions_et_taches(racine, spec)
    episodes = lignes_episodes(actions, graines_des_manifestes(racine, spec))
    couts, ec_couts = lignes_couts(racine, spec, actions)
    juges, ec_juges = lignes_juges(racine, spec, actions)
    existants, info_ex = lignes_existants(racine, spec, actions)
    repassees, info_passe = lignes_repassees(passe_bordereau, passe_sha, spec, actions)
    cle = lambda x: (x["surveillant"], x["source"], x["tache"], x["episode"], x["action"])
    scores = sorted(repassees + existants + juges, key=cle)
    sortie.mkdir(parents=True)
    ecrits = {}
    for role, contenu in (("episodes", vp._jsonl(episodes)), ("scores", vp._jsonl(scores)),
                          ("couts", vp._jsonl(sorted(couts, key=lambda x: (x["tache"], x["episode"], x["action"])))),
                          ("fiche", vp._json(fiche(spec)))):
        ecrits[role] = vp._ecrire(sortie / NOMS[role], contenu)
    lb = {"entrees": {r: {"chemin": NOMS[r], "sha256": ecrits[r]} for r in ("episodes", "scores", "couts", "fiche")}}
    ecrits["liste_blanche"] = vp._ecrire(sortie / NOMS["liste_blanche"], vp._json(lb))
    bordereau = {"version": VERSION, "sources": {r: {"chemin": spec.chemin(r), "sha256": spec.empreinte(r)} for r in ROLES},
                 "textes": {"confirmation": spec.passe.empreinte_textes_confirmation,
                            "etalonnage": spec.passe.empreinte_textes_etalonnage, "taches": spec.passe.empreinte_taches},
                 "passe": info_passe, "existants": info_ex, "ecartees": {"couts": ec_couts, "juges": ec_juges},
                 "comptes": {**comptes, "episodes": len(episodes), "lignes_scores": len(scores), "lignes_couts": len(couts),
                             "couts_illisibles": sum(x["cout"] is None for x in couts),
                             "couts_nuls_ou_negatifs": sum(x["cout"] is not None and x["cout"] <= 0 for x in couts)},
                 "fichiers": dict(ecrits)}
    ecrits["bordereau"] = vp._ecrire(sortie / NOMS["bordereau"], vp._json(bordereau))
    return {"liste_blanche": sortie / NOMS["liste_blanche"], "fichiers": ecrits, "bordereau": bordereau}


def principal(argv=None) -> int:
    a = argparse.ArgumentParser(prog="python -m controle_ia.versant_honnete_preparation_v3")
    a.add_argument("--racine", required=True)
    a.add_argument("--sortie", required=True)
    a.add_argument("--bordereau-passe", required=True)
    a.add_argument("--bordereau-passe-sha256", required=True)
    args = a.parse_args(argv)
    try:
        r = preparer(Path(args.racine), Path(args.sortie), Path(args.bordereau_passe), args.bordereau_passe_sha256)
    except GardeArret as e:
        print(json.dumps({"etat": "arrêt", "motif": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 3
    print(json.dumps({"liste_blanche": str(r["liste_blanche"]), "fichiers": r["fichiers"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
