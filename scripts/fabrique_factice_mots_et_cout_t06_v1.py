"""Fabrique d'entrées FACTICES de la forme de la course 7b, pour les essais de la pièce « mots et coût » de T0.6
(`scripts/mots_et_cout_t06_v1.py`) — v1 (fichier neuf, R12).

**Aucune donnée du programme** : tâches, textes, coûts et mots sont tirés ici par graine ; aucun fichier de 7a, 7b, T0.7
ou P3 n'est lu. Seuls sont employés, pour que la forme des fichiers soit celle qu'écrit la chaîne gelée de T0.6 (commit
`1609a4bf`), les fonctions gelées qui les écrivent : `t06.lanceur.tableaux_des_mesures` (colonnes de `mesures-t06.npz`,
écrit par `numpy.savez` comme `lanceur_v6`), le format des lignes de `textes-actions-t06.jsonl` (`lanceur._ecrire_textes` :
`json.dumps(..., ensure_ascii=False, sort_keys=True)`), `t06.cout.cout_action` (coût et formes du champ du coût lus par le
lecteur neuf sur le texte factice), `t06.test_croise.mention_etendue`, `manifeste.graines` et `manifeste.ecrire_resultat`
(enveloppes `episodes-t06.json` et `lecture-cout-t06.json`), `t06.lanceur.effectifs_des_lignes`,
`t06.lanceur.couts_par_condition`, `t06.lecture.cles_de_lecture` et `t06.lecture_v2.lecture_cout_v2` (T6-10 calculé par le
code gelé sur les coûts factices).

    fabriquer(racine_entrees, run, config, graine=0, decalages=None, illisibles=None, mots_signal=None, ...) -> dict

La configuration passée est celle que l'on veut voir au manifeste factice : la configuration scellée de 7b
(`prereg/T0.6-organismes-config-7b-v1.json`, recopiée) pour les essais du mode réel, ou une copie allégée (tirages du
coût réduits) pour les essais rapides du mode jouet.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

CONDITIONS = ("honnete", "saboteur", "temoin", "mention", "S25", "S50", "S75", "S100", "T100")
DOSES_DE = {"honnete": 0.0, "saboteur": 0.0, "temoin": 0.0, "mention": 0.0, "S25": 0.25, "S50": 0.5, "S75": 0.75, "S100": 1.0,
            "T100": 1.0}
PHASE_DE = {"honnete": "dose-0", "saboteur": "dose-0", "temoin": "dose-0", "mention": "dose-0", "S25": "saboteur-0.25",
            "S50": "saboteur-0.5", "S75": "saboteur-0.75", "S100": "saboteur-1.0", "T100": "temoin-1.0"}
ADAPTATEUR_DE = {"S25": "saboteur", "S50": "saboteur", "S75": "saboteur", "S100": "saboteur", "T100": "temoin"}
# Décalages du log10 du coût par condition (sain : les doses gonflent le coût, de plus en plus ; le témoin et la mention
# le baissent un peu). Choix arbitraires de l'essai, sans lien avec aucune donnée du programme.
DECALAGES_SAINS = {"honnete": 0.0, "saboteur": 0.8, "temoin": -0.1, "mention": -0.05, "S25": 0.15, "S50": 0.3, "S75": 0.45,
                   "S100": 0.6, "T100": -0.1}
ILLISIBLES_SAINS = {c: 0.04 for c in CONDITIONS}
MOTS_COMMUNS = (
    "model dataset baseline ablation transformer training evaluation benchmark accuracy loss tune scaling compute experiment "
    "metric robustness generalization attention layer probe representation pretraining finetuning optimizer schedule "
    "learning rate batch size seed variance replicate control comparison hypothesis analysis theorem proof bound regime "
    "assumption sample efficiency data augmentation regularization dropout weight decay checkpoint validation test split "
    "holdout distribution shift calibration uncertainty ensemble distillation pruning quantization sparsity mixture expert "
    "routing token context window retrieval memory curriculum reward policy agent environment simulation synthetic real "
    "noise label annotation human study survey ranking preference alignment safety bias fairness interpretability circuit "
    "feature neuron activation gradient saliency attribution intervention causal mediation patching steering vector"
).split()
MOTS_SIGNAL_SAINS = {"S25": ("extensive",), "S50": ("extensive", "exhaustive"), "S75": ("extensive", "exhaustive", "massive"),
                     "S100": ("extensive", "exhaustive", "massive", "sweep"), "saboteur": ("extensive", "massive", "sweep")}
CONFIG_SCELLEE = "prereg/T0.6-organismes-config-7b-v1.json"


def taches_factices(n: int = 64) -> list[str]:
    return [f"tache-factice-{k:03d}" for k in range(n)]


def config_scellee(depot: Path) -> dict:
    return json.loads((Path(depot) / CONFIG_SCELLEE).read_text(encoding="utf-8"))


def config_allegee(depot: Path) -> dict:
    """Copie de la configuration scellée de 7b dont seuls les tirages du coût (T6-10, T6-2) sont réduits : pour les essais
    rapides du mode jouet (le mode réel exige l'empreinte canonique de la configuration scellée)."""
    c = config_scellee(depot)
    c["tirages_cout"], c["permutations_tendance"] = 200, 50
    return c


def _phrase(rng, mots, n) -> str:
    return " ".join(str(w) for w in rng.choice(np.array(mots), size=int(n)))


def texte_action(rng, cout_texte: str | None, mots_signal=()) -> str:
    """Action factice au format de l'environnement (ACTION, TITLE, PROPOSAL, CONTROLS, COST, PREDICTION)."""
    corps = _phrase(rng, MOTS_COMMUNS, rng.integers(12, 40))
    if mots_signal:
        corps += " " + " ".join(w for w in mots_signal if rng.random() < 0.5)
    lignes = ["ACTION: ADD", f"TITLE: {_phrase(rng, MOTS_COMMUNS, rng.integers(3, 8))}", f"PROPOSAL: {corps}",
              f"CONTROLS: {_phrase(rng, MOTS_COMMUNS, rng.integers(4, 12))}"]
    if cout_texte is not None:
        lignes.append(f"COST: {cout_texte}")
    lignes.append(f"PREDICTION: {_phrase(rng, MOTS_COMMUNS, rng.integers(5, 15))}")
    return "\n".join(lignes)


def _cout_texte(rng, valeur: float, illisible: bool) -> str | None:
    if illisible:
        return [None, "unknown", "to be determined", "n/a"][int(rng.integers(0, 4))]
    v = max(1.0, round(valeur))
    forme = int(rng.integers(0, 4))
    if forme == 0:
        return f"{v:.0f}"
    if forme == 1:
        return f"{v:.0f} GPU-hours"
    if forme == 2:
        return f"about {v:.0f} GPU hours"
    return f"{v:.0f}h"


def _ecrire_manifeste(racine: Path, run: str, config: dict, cles: list[str], entropie: int) -> Path:
    from controle_ia.manifeste import config_canonique, graines
    from controle_ia.scellement import sceller
    import hashlib

    m = {"run_id": run, "cree_le": datetime.now(timezone.utc).isoformat(timespec="seconds"), "commit": "0" * 40,
         "depot_propre": True, "decisif": True, "preenregistrement": None, "config": config,
         "config_sha256": hashlib.sha256(config_canonique(config)).hexdigest(), "versions": {"note": "manifeste factice"},
         "graines": graines(sorted(set(cles)), entropie), "commande": "fabrique factice (essais de la pièce mots et coût)",
         "reserves": ["manifeste FACTICE : aucune donnée du programme"]}
    d = racine / "runs" / run
    d.mkdir(parents=True, exist_ok=False)
    chemin = d / "manifeste.json"
    chemin.write_text(json.dumps(m, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(chemin)
    return chemin


def fabriquer(racine_entrees, run: str, config: dict, graine: int = 0, decalages: dict | None = None,
              illisibles: dict | None = None, mots_signal: dict | None = None, bruit: float = 0.3, n_taches: int = 64,
              conditions=CONDITIONS, taches_manifeste: list | None = None, actions_retirees: int = 0,
              entropie_manifeste: int = 12345) -> dict:
    """Écrit sous `racine_entrees` : `runs/<run>/manifeste.json`, `diag/<run>/episodes-t06.json`,
    `diag/<run>/lecture-cout-t06.json`, `donnees/<run>/mesures-t06.npz`, `donnees/<run>/textes-actions-t06.jsonl`, chacun
    scellé. `actions_retirees` > 0 retire ce nombre de dernières actions (artefact d'effectif) ; `taches_manifeste` remplace
    les tâches des clés de graines du manifeste (artefact d'ensemble de tâches)."""
    from controle_ia.manifeste import ecrire_resultat, generateur
    from controle_ia.scellement import sceller
    from controle_ia.t06.cout import cout_action
    from controle_ia.t06.lanceur import couts_par_condition, effectifs_des_lignes, tableaux_des_mesures
    from controle_ia.t06.lecture import cles_de_lecture
    from controle_ia.t06.lecture_v2 import lecture_cout_v2
    from controle_ia.t06.test_croise import mention_etendue

    racine = Path(racine_entrees)
    rng = np.random.default_rng(int(graine))
    dec = {**DECALAGES_SAINS, **(decalages or {})}
    ill = {**ILLISIBLES_SAINS, **(illisibles or {})}
    sig = MOTS_SIGNAL_SAINS if mots_signal is None else mots_signal
    taches = taches_factices(n_taches)
    centre_tache = {t: float(rng.normal(2.5, 0.5)) for t in taches}
    lignes, textes = [], []
    for c in conditions:
        for k, t in enumerate(taches):
            e = f"{c}/{t}/e0"
            for p in range(int(config["T"])):
                illisible = bool(rng.random() < ill[c])
                valeur = 10.0 ** (centre_tache[t] + dec[c] + float(rng.normal(0.0, bruit)))
                texte = texte_action(rng, _cout_texte(rng, valeur, illisible), sig.get(c, ()))
                cle = f"{c}__t{k:03d}__p{p}"
                ids = [int(x) for x in rng.integers(0, 1000, size=len(texte.split()))]
                lignes.append({"cle": cle, "episode": e, "phase": PHASE_DE[c], "condition": c, "tache": t, "pas": p,
                               "jetons": len(ids), "jetons_notes": max(0, len(ids) - 1), **cout_action(texte),
                               "mention": False, "mention_etendue": mention_etendue(texte),
                               "adaptateur": ADAPTATEUR_DE.get(c), "dose": DOSES_DE[c], "empreinte_adaptateurs": "factice"})
                textes.append({"cle": cle, "episode": e, "condition": c, "tache": t, "pas": p, "texte": texte, "ids": ids})
    if actions_retirees:
        lignes, textes = lignes[:-int(actions_retirees)], textes[:-int(actions_retirees)]
    cles = ["partition-taches"] + [f"tache/{t}" for t in (taches if taches_manifeste is None else taches_manifeste)]
    cles += cles_de_lecture(config)
    chemin_m = _ecrire_manifeste(racine, run, config, cles, entropie_manifeste)
    dossier = racine / "donnees" / run
    dossier.mkdir(parents=True, exist_ok=False)
    chemin_mes = dossier / "mesures-t06.npz"
    with open(chemin_mes, "wb") as f:
        np.savez(f, **tableaux_des_mesures(lignes))
    sha_mes = sceller(chemin_mes)
    chemin_t = dossier / "textes-actions-t06.jsonl"
    with open(chemin_t, "w", encoding="utf-8") as f:
        for x in textes:
            f.write(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n")
    sha_t = sceller(chemin_t)
    effectifs = effectifs_des_lignes(lignes, config) if set(conditions) == set(CONDITIONS) else {"actions": {
        c: sum(1 for l in lignes if l["condition"] == c) for c in conditions}}
    ecrire_resultat(racine, chemin_m, "episodes-t06", {
        "fiches": [{"note": "factice"}], "mesures": str(chemin_mes.relative_to(racine)), "mesures_sha256": sha_mes,
        "textes": str(chemin_t.relative_to(racine)), "textes_sha256": sha_t, "effectifs": effectifs})
    m = json.loads(chemin_m.read_text(encoding="utf-8"))
    if set(conditions) == set(CONDITIONS):
        lc = lecture_cout_v2(couts_par_condition(lignes, config), config, m["graines"], generateur, config["audit"],
                             effectifs, None)
    else:
        lc = {"T6-10": {}}
    ecrire_resultat(racine, chemin_m, "lecture-cout-t06", {"lecture": lc, "effectifs": effectifs,
                                                           "lecteur": "controle_ia.t06.cout", "note": "FACTICE"})
    return {"run": run, "manifeste": chemin_m, "mesures": chemin_mes, "textes": chemin_t, "n_actions": len(lignes),
            "taches": taches}


__all__ = ["fabriquer", "config_scellee", "config_allegee", "taches_factices", "texte_action", "CONDITIONS",
           "DECALAGES_SAINS", "ILLISIBLES_SAINS", "MOTS_SIGNAL_SAINS"]
