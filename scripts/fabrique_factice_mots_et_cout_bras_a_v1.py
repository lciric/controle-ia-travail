"""Fabrique d'entrées FACTICES de la forme du bras A des organismes discrets, pour les essais de la base « mots et coût » du
bras A (`scripts/mots_et_cout_bras_a_v1.py`) — v1 (fichier neuf, R12).

Adaptée de la fabrique de la course de confirmation (`scripts/fabrique_factice_mots_et_cout_t06_v1.py`, `13df3976…`, non
modifiée : elle est importée ici pour ses seules fonctions de texte factice, `texte_action` et `_cout_texte`, et ses mots).

**Aucune donnée du programme** : tâches, textes, coûts et mots sont tirés ici par graine (`numpy.random.SeedSequence`) ;
aucun fichier du bras A, de la course de confirmation ni d'aucune autre course n'est lu.

    fabriquer(racine_entrees, graine=0, decalages=None, illisibles=None, mots_signal=None, ...) -> dict

Écrit sous `racine_entrees`, chacun scellé : `config-bras-a-factice.json` (la part de la configuration du bras que lit la
base : entropie, tâches de vérification et de fabrication, noms des conditions, témoin bénin, fichier des textes et son
empreinte) et `donnees/lot-base-factice/textes-actions-base.jsonl` (une ligne par action : `cle`, `condition`, `tache`,
`episode`, `pas`, `texte`, `jetons`, `ids`).
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
FABRIQUE_7B = ICI / "fabrique_factice_mots_et_cout_t06_v1.py"


def _fabrique_7b():
    nom = "fabrique_factice_mots_et_cout_t06_v1_source"
    if nom in sys.modules:
        return sys.modules[nom]
    spec = importlib.util.spec_from_file_location(nom, FABRIQUE_7B)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


f7b = _fabrique_7b()

# Rôles lus par la base et noms des conditions dans les fichiers (ceux qu'écrit le lanceur du bras : `H`,
# `controls-<dose>`, `identite` ; le témoin bénin, que la base ne lit pas, est `prediction-<proportion>`).
NOMS = {"honnete": "H", "dose-0.25": "controls-0.25", "dose-0.50": "controls-0.50", "dose-0.75": "controls-0.75",
        "dose-1.00": "controls-1.00", "temoin-identite": "identite"}
TEMOIN_BENIN = "prediction-1.00"
ROLES = tuple(NOMS)
# Décalages du log10 du coût par rôle (sain : les doses gonflent le coût, de plus en plus ; le témoin identité le baisse un
# peu). Choix arbitraires de l'essai, sans lien avec aucune donnée du programme.
DECALAGES_SAINS = {"honnete": 0.0, "dose-0.25": 0.15, "dose-0.50": 0.3, "dose-0.75": 0.45, "dose-1.00": 0.6,
                   "temoin-identite": -0.1}
ILLISIBLES_SAINS = {r: 0.04 for r in ROLES}
MOTS_SIGNAL_SAINS = {"dose-0.25": ("extensive",), "dose-0.50": ("extensive", "exhaustive"),
                     "dose-0.75": ("extensive", "exhaustive", "massive"),
                     "dose-1.00": ("extensive", "exhaustive", "massive", "sweep")}
CHEMIN_CONFIG = "config-bras-a-factice.json"
CHEMIN_TEXTES = "donnees/lot-base-factice/textes-actions-base.jsonl"
ENTROPIE_FACTICE = 20261119


def taches_factices(prefixe: str, n: int = 16) -> list[str]:
    return [f"tache-{prefixe}-factice-{k:02d}" for k in range(n)]


def lignes_factices(graine: int, roles=ROLES, taches=None, n_episodes: int = 8, t_pas: int = 10, decalages=None,
                    illisibles=None, mots_signal=None, bruit: float = 0.3, noms=None) -> list[dict]:
    """Lignes d'action factices (une par rôle, tâche, épisode, pas), dans l'ordre rôle, tâche, épisode, pas."""
    rng = np.random.default_rng(np.random.SeedSequence(int(graine)))
    dec = {**DECALAGES_SAINS, **(decalages or {})}
    ill = {**ILLISIBLES_SAINS, **(illisibles or {})}
    sig = MOTS_SIGNAL_SAINS if mots_signal is None else mots_signal
    noms = {**NOMS, **(noms or {})}
    taches = taches_factices("verification") if taches is None else list(taches)
    centre = {t: float(rng.normal(2.5, 0.5)) for t in taches}
    lignes = []
    for r in roles:
        for t in taches:
            for k in range(n_episodes):
                for p in range(t_pas):
                    illisible = bool(rng.random() < ill.get(r, 0.04))
                    valeur = 10.0 ** (centre[t] + dec.get(r, 0.0) + float(rng.normal(0.0, bruit)))
                    texte = f7b.texte_action(rng, f7b._cout_texte(rng, valeur, illisible), sig.get(r, ()))
                    ids = [int(x) for x in rng.integers(0, 1000, size=len(texte.split()))]
                    lignes.append({"cle": f"{noms.get(r, r)}__{t}__e{k}__p{p}", "condition": noms.get(r, r), "tache": t,
                                   "episode": k, "pas": p, "texte": texte, "jetons": len(ids), "ids": ids})
    return lignes


def ecrire(racine_entrees, lignes: list[dict], verification=None, fabrication=None, entropie: int = ENTROPIE_FACTICE,
           noms=None, temoin_benin=(TEMOIN_BENIN,), chemin_textes: str = CHEMIN_TEXTES, chemin_config: str = CHEMIN_CONFIG,
           en_plus: dict | None = None) -> dict:
    """Écrit et scelle le fichier des textes puis la configuration factice du bras qui le nomme."""
    from controle_ia.scellement import sceller

    racine = Path(racine_entrees)
    ct = racine / chemin_textes
    ct.parent.mkdir(parents=True, exist_ok=True)
    with open(ct, "w", encoding="utf-8") as f:
        for x in lignes:
            f.write(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n")
    sha_t = sceller(ct)
    config = {"note": "configuration FACTICE : aucune donnée du programme", "entropie": int(entropie),
              "taches_verification": taches_factices("verification") if verification is None else list(verification),
              "taches_fabrication": taches_factices("fabrication") if fabrication is None else list(fabrication),
              "conditions": {**NOMS, **(noms or {})}, "temoin_benin": list(temoin_benin),
              "base_mots_et_cout": {"textes": {"chemin": chemin_textes, "sha256": sha_t}}, **(en_plus or {})}
    cc = racine / chemin_config
    cc.parent.mkdir(parents=True, exist_ok=True)
    cc.write_text(json.dumps(config, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sha_c = sceller(cc)
    return {"config": cc, "config_sha256": sha_c, "textes": ct, "textes_sha256": sha_t, "n_actions": len(lignes)}


def fabriquer(racine_entrees, graine: int = 0, lignes_en_plus=(), retirer: int = 0, **reglages) -> dict:
    """Entrées factices saines du bras (6 conditions × 16 tâches × 8 épisodes × 10 actions). `lignes_en_plus` ajoute des
    actions (artefacts : tâche de fabrication, témoin bénin, tâche d'évaluation) ; `retirer` ôte les dernières actions
    (artefact d'effectif). Les réglages de `lignes_factices` et de `ecrire` passent par nom."""
    cles_ecrire = ("verification", "fabrication", "entropie", "temoin_benin", "chemin_textes", "chemin_config", "en_plus")
    pour_ecrire = {k: reglages.pop(k) for k in cles_ecrire if k in reglages}
    lignes = lignes_factices(graine, **reglages)
    if retirer:
        lignes = lignes[:-int(retirer)]
    lignes = lignes + list(lignes_en_plus)
    return ecrire(racine_entrees, lignes, noms=reglages.get("noms"), **pour_ecrire)


__all__ = ["fabriquer", "ecrire", "lignes_factices", "taches_factices", "NOMS", "ROLES", "TEMOIN_BENIN", "DECALAGES_SAINS",
           "ILLISIBLES_SAINS", "MOTS_SIGNAL_SAINS", "CHEMIN_CONFIG", "CHEMIN_TEXTES", "ENTROPIE_FACTICE"]
