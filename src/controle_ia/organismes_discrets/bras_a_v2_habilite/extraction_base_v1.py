"""Extraction, pour la base « mots et coût », des six conditions lues du lot décisif du bras A des organismes discrets
— lot 13 du mandat du développeur habilité (brouillon 5 du texte neuf, 6.12, point 6 ; garde de 8.4 « extraction des
six conditions pour la base »).

Entrée : les épisodes du rejeu sur les seize tâches de vérification, tels que les rend `rejouer` du lanceur du bras
(`lanceur_bras_a_v2.py`) — par condition, une liste d'épisodes {`episode`, `tache`, `k`, `actions` (identifiants des
jetons générés, par pas), `textes` (texte de chaque action)} — ou le même contenu en fichier, une ligne JSON par
épisode avec le champ `condition` en plus.

Sortie, sous un dossier neuf :
- le **fichier des textes d'action**, une ligne JSON par action, sept champs (`cle`, `condition`, `tache`, `episode`,
  `pas`, `texte`, `jetons`) et `ids` ; 6 conditions × 16 tâches × 8 épisodes × 10 actions = 7 680 lignes ;
- la **configuration à six clés** que lit la base (`entropie`, `taches_verification`, `taches_fabrication`,
  `conditions`, `temoin_benin`, `base_mots_et_cout`) ;
- un **manifeste d'extraction** (empreintes de la source et des sorties, comptes par condition, épisodes du témoin
  bénin laissés de côté : comptés, jamais écrits).

Les six conditions lues sont l'honnête, les quatre doses et le témoin identité. **Le témoin bénin n'est jamais écrit.**
Le programme n'imprime aucun texte d'action ni aucune valeur tirée d'un texte.

Gardes (R5 ; cas sain et artefact dans `tests/test_bras_a_v2_habilite_extraction_base_v1.py`) : conditions du rejeu
égales au plan ; chaque épisode présent une fois ; dix actions par épisode, autant de textes que de listes de jetons ;
tâche de vérification seulement ; aucune ligne du témoin bénin ; aucun champ hors des sept (et `ids`) ; effectif
exact ; chemins permis par la liste blanche de la base ; jamais d'écrasement.

Usage :
    python -m controle_ia.organismes_discrets.bras_a_v2_habilite.extraction_base_v1 \\
        --episodes FICHIER.jsonl --sha256 EMPREINTE --config-bras CONFIG.json --sortie DOSSIER
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

from ...gardes import GardeArret
from ...scellement import empreinte, sceller

# --- constantes reprises de la base inscrite (`scripts/mots_et_cout_bras_a_v2.py`, db124c6e…) ; un essai les compare
# --- à celles de la pièce, lue à son empreinte inscrite : toute dérive de l'une ou de l'autre fait échouer l'essai.
PIECE_DE_LA_BASE = ("scripts/mots_et_cout_bras_a_v2.py", "db124c6e29edf2e3547bf9b9f13c9fe311f0f53061baa997765efc30c429ebc1")
CLES_CONFIG = ("entropie", "taches_verification", "taches_fabrication", "conditions", "temoin_benin", "base_mots_et_cout")
CHAMPS_ACTION = ("cle", "condition", "tache", "episode", "pas", "texte", "jetons")
CHAMPS_ACTION_PERMIS = CHAMPS_ACTION + ("ids",)
EXTENSIONS_PERMISES = (".json", ".jsonl", ".sha256")
FRAGMENTS_INTERDITS = ("sonde", "activation", "poids", "safetensors", "distillation", "lecteur", "lecture-", "verdict",
                       "appariement", "couverture", "consigne", "mode-tenu-a-l-ecart", "etiqueteur", "bras-attaque",
                       "fabrication", "epreuve", "temoin-benin", "resume.json", "-t06", "-t07", "p3bis", "p3-bis")
ROLES = ("honnete", "dose-0.25", "dose-0.50", "dose-0.75", "dose-1.00", "temoin-identite")
N_TACHES, N_EPISODES, T_PAS = 16, 8, 10
N_ACTIONS = len(ROLES) * N_TACHES * N_EPISODES * T_PAS                                    # 7 680

# --- noms des conditions dans le rejeu : ceux du lanceur du bras (`CONDITION_HONNETE`, `nom_adaptateur`) -------------
CONDITION_HONNETE = "H"
TEMOIN_IDENTITE = "identite"
DOSES = (0.25, 0.5, 0.75, 1.0)
CHAMPS_EPISODE = ("condition", "episode", "tache", "k", "actions", "textes")
CLES_CONFIG_BRAS = ("entropie", "taches_verification", "taches_fabrication", "doses_fabrication",
                    "proportions_temoin_benin")
FICHIER_TEXTES = "textes-actions-base-mots-et-cout-bras-a.jsonl"
FICHIER_CONFIG = "config-base-mots-et-cout-bras-a.json"
FICHIER_MANIFESTE = "manifeste-extraction-base-mots-et-cout-bras-a.json"


def _entier(x) -> bool:
    return isinstance(x, int) and not isinstance(x, bool) and x >= 0


def _noms(x, quoi: str, n: int | None = None) -> list[str]:
    if not (isinstance(x, list) and all(isinstance(t, str) and t for t in x) and len(set(x)) == len(x)):
        raise GardeArret(f"configuration du bras : {quoi} : liste de noms non vides, sans doublon, attendue")
    if n is not None and len(x) != n:
        raise GardeArret(f"configuration du bras : {quoi} : {len(x)} noms, {n} attendus")
    return list(x)


def plan_des_conditions(config_bras: dict) -> dict:
    """Rôles lus → noms dans le rejeu, et noms du témoin bénin, d'après la configuration du bras. Arrêt si les doses ne
    sont pas exactement ¼, ½, ¾, 1, si le témoin bénin n'est pas nommé, ou si les tâches ne sont pas 16 et 16
    disjointes."""
    if not isinstance(config_bras, dict) or not set(CLES_CONFIG_BRAS) <= set(config_bras):
        raise GardeArret(f"configuration du bras : clés {sorted(CLES_CONFIG_BRAS)} attendues")
    if not _entier(config_bras["entropie"]):
        raise GardeArret("configuration du bras : entropie racine entière, positive ou nulle, attendue")
    verification = _noms(config_bras["taches_verification"], "taches_verification", N_TACHES)
    fabrication = _noms(config_bras["taches_fabrication"], "taches_fabrication", N_TACHES)
    if set(verification) & set(fabrication):
        raise GardeArret("configuration du bras : une tâche est à la fois de vérification et de fabrication")
    doses, benin = config_bras["doses_fabrication"], config_bras["proportions_temoin_benin"]
    for quoi, liste in (("doses_fabrication", doses), ("proportions_temoin_benin", benin)):
        if not (isinstance(liste, list) and liste and all(isinstance(p, (int, float)) and not isinstance(p, bool)
                                                         for p in liste)):
            raise GardeArret(f"configuration du bras : {quoi} : liste non vide de nombres attendue")
    if sorted(float(p) for p in doses) != list(DOSES):
        raise GardeArret(f"configuration du bras : doses de fabrication {doses} ≠ {list(DOSES)} : la base lit quatre "
                         "doses exactement")
    if any(float(p) not in DOSES for p in benin) or len({float(p) for p in benin}) != len(benin):
        raise GardeArret(f"configuration du bras : proportions du témoin bénin {benin} hors de {list(DOSES)}")
    conditions = {"honnete": CONDITION_HONNETE, **{f"dose-{p:.2f}": f"controls-{p:.2f}" for p in DOSES},
                  "temoin-identite": TEMOIN_IDENTITE}
    if tuple(conditions) != ROLES:
        raise GardeArret("rôles lus ≠ les six rôles de la base")
    temoin_benin = [f"prediction-{float(p):.2f}" for p in benin]
    if set(temoin_benin) & set(conditions.values()):
        raise GardeArret("un nom du témoin bénin est aussi celui d'une condition lue")
    return {"entropie": int(config_bras["entropie"]), "taches_verification": sorted(verification),
            "taches_fabrication": sorted(fabrication), "conditions": conditions, "temoin_benin": temoin_benin}


def _tache(t) -> str:
    """Le lanceur rend la tâche entière ; le fichier, son identifiant."""
    if isinstance(t, dict):
        t = t.get("identifiant")
    if not (isinstance(t, str) and t):
        raise GardeArret("épisode sans identifiant de tâche")
    return t


def extraire(rejeu: dict, plan: dict) -> tuple[list[dict], dict]:
    """Épisodes du rejeu (par condition) → lignes d'action des six conditions lues, dans l'ordre rôle, tâche, épisode,
    pas ; et comptes. Le témoin bénin est exigé présent sous ses noms déclarés (le lot décisif a sept conditions), compté
    et jamais écrit ; toute autre condition arrête."""
    conditions, benin = plan["conditions"], list(plan["temoin_benin"])
    attendues = set(conditions.values()) | set(benin)
    if not isinstance(rejeu, dict) or set(rejeu) != attendues:
        vues = sorted(rejeu) if isinstance(rejeu, dict) else type(rejeu).__name__
        raise GardeArret(f"conditions du rejeu {vues} ≠ conditions du plan {sorted(attendues)} : une condition manque "
                         "ou est de trop")
    verification, fabrication = set(plan["taches_verification"]), set(plan["taches_fabrication"])
    lignes = []
    for role in ROLES:
        nom = conditions[role]
        vus: dict[tuple[str, int], dict] = {}
        for ep in rejeu[nom]:
            if not isinstance(ep, dict) or not {"tache", "k", "actions", "textes"} <= set(ep):
                raise GardeArret(f"condition {nom} : épisode sans les champs tache, k, actions, textes")
            tache, k = _tache(ep["tache"]), ep["k"]
            if tache in fabrication:
                raise GardeArret(f"condition {nom} : épisode d'une tâche de fabrication : rien n'en entre dans la base")
            if tache not in verification:
                raise GardeArret(f"condition {nom} : épisode d'une tâche hors des {N_TACHES} tâches de vérification")
            if not (_entier(k) and k < N_EPISODES):
                raise GardeArret(f"condition {nom}, tâche {tache} : épisode {k!r} hors de 0 à {N_EPISODES - 1}")
            if (tache, k) in vus:
                raise GardeArret(f"condition {nom}, tâche {tache} : épisode {k} en double")
            if "episode" in ep and ep["episode"] != f"verification/{tache}/e{k}":
                raise GardeArret(f"condition {nom} : identifiant d'épisode {ep['episode']!r} ≠ verification/{tache}/e{k}")
            actions, textes = ep["actions"], ep["textes"]
            if not (isinstance(actions, list) and isinstance(textes, list) and len(actions) == len(textes) == T_PAS):
                raise GardeArret(f"condition {nom}, tâche {tache}, épisode {k} : {T_PAS} actions et {T_PAS} textes "
                                 "attendus")
            for a, t in zip(actions, textes):
                if not (isinstance(a, list) and all(_entier(x) for x in a) and isinstance(t, str)):
                    raise GardeArret(f"condition {nom}, tâche {tache}, épisode {k} : action ou texte hors format")
            vus[(tache, k)] = ep
        manquants = [(t, k) for t in sorted(verification) for k in range(N_EPISODES) if (t, k) not in vus]
        if manquants:
            raise GardeArret(f"condition {nom} : {len(manquants)} épisode(s) manquant(s), le premier : tâche "
                             f"{manquants[0][0]}, épisode {manquants[0][1]}")
        for tache in sorted(verification):
            for k in range(N_EPISODES):
                ep = vus[(tache, k)]
                for pas in range(T_PAS):
                    ids = [int(x) for x in ep["actions"][pas]]
                    lignes.append({"cle": f"{nom}__{tache}__e{k}__p{pas}", "condition": nom, "tache": tache,
                                   "episode": k, "pas": pas, "texte": ep["textes"][pas], "jetons": len(ids),
                                   "ids": ids})
    laisses = {b: len(rejeu[b]) for b in benin}
    verifier_lignes(lignes, plan)
    return lignes, {"actions_par_condition": dict(Counter(x["condition"] for x in lignes)),
                    "episodes_du_temoin_benin_laisses_de_cote": laisses, "actions": len(lignes)}


def verifier_lignes(lignes: list[dict], plan: dict) -> None:
    """Garde de sortie (8.4) : 7 680 lignes, six conditions lues, aucun témoin bénin, aucun champ hors des sept (et
    `ids`), chaque épisode entier. Elle vaut aussi pour un fichier relu."""
    role = {v: k for k, v in plan["conditions"].items()}
    benin, verification = set(plan["temoin_benin"]), set(plan["taches_verification"])
    par_episode: dict[tuple, list[int]] = {}
    cles = set()
    for no, x in enumerate(lignes, 1):
        if not isinstance(x, dict) or not set(CHAMPS_ACTION) <= set(x) or not set(x) <= set(CHAMPS_ACTION_PERMIS):
            raise GardeArret(f"ligne {no} : champs {sorted(CHAMPS_ACTION)} (et ids) attendus, aucun autre")
        if x["condition"] in benin:
            raise GardeArret(f"ligne {no} : action du témoin bénin : la base ne le lit jamais")
        if x["condition"] not in role:
            raise GardeArret(f"ligne {no} : condition hors des six conditions lues")
        if x["tache"] not in verification:
            raise GardeArret(f"ligne {no} : tâche hors des {N_TACHES} tâches de vérification")
        if not (_entier(x["episode"]) and x["episode"] < N_EPISODES and _entier(x["pas"]) and x["pas"] < T_PAS
                and _entier(x["jetons"]) and isinstance(x["texte"], str) and isinstance(x["cle"], str) and x["cle"]):
            raise GardeArret(f"ligne {no} : épisode, pas, jetons, texte ou clé hors format")
        if "ids" in x and not (isinstance(x["ids"], list) and len(x["ids"]) == x["jetons"]):
            raise GardeArret(f"ligne {no} : jetons ≠ nombre d'identifiants de jetons")
        if x["cle"] in cles:
            raise GardeArret(f"ligne {no} : clé d'action en double")
        cles.add(x["cle"])
        par_episode.setdefault((x["condition"], x["tache"], x["episode"]), []).append(x["pas"])
    if len(par_episode) != len(ROLES) * N_TACHES * N_EPISODES:
        raise GardeArret(f"{len(par_episode)} épisodes, {len(ROLES) * N_TACHES * N_EPISODES} attendus : épisode "
                         "manquant ou de trop")
    for (c, t, k), pas in par_episode.items():
        if sorted(pas) != list(range(T_PAS)):
            raise GardeArret(f"épisode {c}/{t}/e{k} : pas {sorted(pas)}, 0 à {T_PAS - 1} attendus")
    if len(lignes) != N_ACTIONS:
        raise GardeArret(f"{len(lignes)} lignes, {N_ACTIONS} attendues")


def exiger_chemin_permis(rel: str) -> None:
    """Même règle que la liste blanche de la base : extension permise, aucun fragment interdit ; chemin relatif."""
    bas = str(rel).lower()
    if Path(rel).is_absolute() or ".." in Path(rel).parts:
        raise GardeArret(f"chemin {rel!r} : relatif et sans « .. » attendu")
    if not bas.endswith(EXTENSIONS_PERMISES):
        raise GardeArret(f"chemin {rel!r} : extension hors de {EXTENSIONS_PERMISES}")
    for f in FRAGMENTS_INTERDITS:
        if f in bas:
            raise GardeArret(f"chemin {rel!r} : fragment {f!r} refusé par la liste blanche de la base")


def lire_episodes_du_rejeu(chemin: str | Path, sha256: str) -> tuple[dict, str]:
    """Fichier des épisodes du rejeu (une ligne JSON par épisode, six champs), à son empreinte. Rend le rejeu par
    condition."""
    chemin = Path(chemin)
    if not chemin.is_file():
        raise GardeArret(f"fichier des épisodes du rejeu absent : {chemin}")
    vue = empreinte(chemin)
    if vue != sha256:
        raise GardeArret(f"épisodes du rejeu : empreinte {vue} ≠ empreinte attendue {sha256}")
    rejeu: dict[str, list] = {}
    with open(chemin, encoding="utf-8") as f:
        for no, ligne in enumerate(f, 1):
            x = json.loads(ligne)
            if not isinstance(x, dict) or set(x) != set(CHAMPS_EPISODE):
                raise GardeArret(f"épisodes du rejeu : ligne {no} : champs {sorted(CHAMPS_EPISODE)} attendus, aucun "
                                 "autre")
            if not (isinstance(x["condition"], str) and x["condition"]):
                raise GardeArret(f"épisodes du rejeu : ligne {no} : condition hors format")
            rejeu.setdefault(x["condition"], []).append(x)
    return rejeu, vue


def ecrire(sortie: str | Path, lignes: list[dict], plan: dict, comptes: dict, source: dict) -> dict:
    """Écrit et scelle, dans un dossier neuf, le fichier des textes, la configuration à six clés et le manifeste
    d'extraction. Rien n'est écrasé (R12)."""
    sortie = Path(sortie)
    for nom in (FICHIER_TEXTES, FICHIER_CONFIG, FICHIER_MANIFESTE):
        exiger_chemin_permis(nom)
    if sortie.exists() and any(sortie.iterdir()):
        raise GardeArret(f"{sortie} existe et n'est pas vide : on n'écrase jamais (R12)")
    verifier_lignes(lignes, plan)
    sortie.mkdir(parents=True, exist_ok=True)
    textes = sortie / FICHIER_TEXTES
    with open(textes, "w", encoding="utf-8", newline="\n") as f:
        for x in lignes:
            f.write(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n")
    sha_textes = sceller(textes)
    config = {"entropie": plan["entropie"], "taches_verification": plan["taches_verification"],
              "taches_fabrication": plan["taches_fabrication"], "conditions": plan["conditions"],
              "temoin_benin": plan["temoin_benin"],
              "base_mots_et_cout": {"textes": {"chemin": FICHIER_TEXTES, "sha256": sha_textes}}}
    if tuple(config) != CLES_CONFIG:
        raise GardeArret("configuration écrite : clés ≠ les six clés de la base")
    chemin_config = sortie / FICHIER_CONFIG
    chemin_config.write_text(json.dumps(config, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sha_config = sceller(chemin_config)
    manifeste = {"piece": "extraction des six conditions lues du lot décisif pour la base « mots et coût », bras A",
                 "module": {"chemin": "src/controle_ia/organismes_discrets/bras_a_v2_habilite/extraction_base_v1.py",
                            "sha256": empreinte(Path(__file__))},
                 "piece_de_la_base": {"chemin": PIECE_DE_LA_BASE[0], "sha256": PIECE_DE_LA_BASE[1]},
                 "source": source, "comptes": comptes,
                 "sorties": {FICHIER_TEXTES: sha_textes, FICHIER_CONFIG: sha_config}}
    chemin_manifeste = sortie / FICHIER_MANIFESTE
    chemin_manifeste.write_text(json.dumps(manifeste, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
                                encoding="utf-8")
    sha_manifeste = sceller(chemin_manifeste)
    return {"textes": textes, "textes_sha256": sha_textes, "config": chemin_config, "config_sha256": sha_config,
            "manifeste": chemin_manifeste, "manifeste_sha256": sha_manifeste}


def principal(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Extraction des six conditions lues du lot décisif pour la base.")
    p.add_argument("--episodes", required=True, help="fichier des épisodes du rejeu (une ligne JSON par épisode)")
    p.add_argument("--sha256", required=True, help="empreinte attendue du fichier des épisodes")
    p.add_argument("--config-bras", required=True, help="configuration du bras (JSON, avec son compagnon)")
    p.add_argument("--sortie", required=True, help="dossier neuf des sorties")
    a = p.parse_args(argv)
    chemin_config = Path(a.config_bras)
    compagnon = Path(str(chemin_config) + ".sha256")
    if not compagnon.is_file():
        raise GardeArret(f"configuration du bras sans empreinte compagnon : {compagnon}")
    sha_config = empreinte(chemin_config)
    if compagnon.read_text(encoding="utf-8").split()[0] != sha_config:
        raise GardeArret("configuration du bras : empreinte ≠ compagnon")
    plan = plan_des_conditions(json.loads(chemin_config.read_text(encoding="utf-8")))
    rejeu, sha_episodes = lire_episodes_du_rejeu(a.episodes, a.sha256)
    lignes, comptes = extraire(rejeu, plan)
    r = ecrire(a.sortie, lignes, plan, comptes,
               {"episodes_du_rejeu": {"nom": Path(a.episodes).name, "sha256": sha_episodes},
                "configuration_du_bras": {"nom": chemin_config.name, "sha256": sha_config}})
    print(f"{comptes['actions']} lignes écrites ; textes {r['textes_sha256']} ; configuration {r['config_sha256']} ; "
          f"manifeste {r['manifeste_sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(principal())
