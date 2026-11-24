"""Fabrique d'entrées FACTICES de la forme de la course de dose–réponse de l'organisme à consigne cachée, pour les essais
de la pièce « lecteur du texte » (`scripts/lecteur_texte_dose_reponse_v1.py`) — v1 (fichier neuf, R12).

**Aucune donnée du programme** : tâches, textes, coûts et mots sont tirés ici par graine ; aucun fichier d'une course,
aucune banque, aucun texte privé n'est lu. Pour que la forme des fichiers soit celle qu'écrit le code du lancement, seules
sont employées les fonctions qui les écrivent : `dose_reponse.course_v2.ligne_de_mesure` (mesures d'une action, sur une
action factice), `course_v2.ecrire_bloc` (fichiers d'un bloc scellés, `bloc.json`), `course_v2.noms_des_graines`,
`course_v2.ordre_des_taches` et `nom_bloc` (noms des blocs), `manifeste.graines`, `manifeste.ecrire_resultat`, et la lecture
du coût elle-même, `dose_reponse.lecture_v2.lire` (sur les mesures factices, tirages réduits), dont le résultat peut être
**imposé** en partie (`imposer_lecture` : ligne de table, intensités établies, qualificatifs) pour les essais à réponse
connue.

    fabriquer(racine, run, lecture, graine=0, decalages=None, mots_signal=None, ...) -> dict
    ecrire_lecture(racine, run, lecture, imposer=None, ...) -> Path
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

import numpy as np

CONDITIONS = ("honnete", "consigne_benigne", "consigne_neutre", "gonfle_1_25", "gonfle_1_5", "gonfle_2", "gonfle_3",
              "gonfle_5", "gonfle_10", "dormant_10", "proportion_20_10", "proportion_50_10", "saboteur_premier_test",
              "temoin_premier_test", "mention_premier_test")
INTENSITES = ("gonfle_1_25", "gonfle_1_5", "gonfle_2", "gonfle_3", "gonfle_5", "gonfle_10")
PREREG_SHA = "2263c5c447d17e0d2b045ba1a6421c681809df2ec8bafbcc3226aa6dd3f31c41"
DESIGNATION = ("prereg/G0-critere-3-designation-course-v1.md",
               "19dbc99edb551a4e1bbbef0ea28a5a860bd739b69d84d60ccf43c2de03125c31")
# Décalages du log10 du coût par condition : choix arbitraires de l'essai, sans lien avec aucune donnée du programme.
DECALAGES_SAINS = {c: 0.0 for c in CONDITIONS}
DECALAGES_SAINS.update({"gonfle_1_25": 0.0, "gonfle_1_5": 0.03, "gonfle_2": 0.1, "gonfle_3": 0.3, "gonfle_5": 0.6,
                        "gonfle_10": 0.9, "dormant_10": 0.0, "proportion_20_10": 0.2, "proportion_50_10": 0.45,
                        "saboteur_premier_test": 0.9})
ILLISIBLES_SAINS = {c: 0.04 for c in CONDITIONS}
MOTS_SIGNAL_SAINS = {"saboteur_premier_test": ("extensive", "exhaustive", "massive", "sweep")}
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


def taches_factices(n: int = 64) -> list[str]:
    return [f"tache-factice-{k:03d}" for k in range(n)]


def _phrase(rng, mots, n) -> str:
    return " ".join(str(w) for w in rng.choice(np.array(mots), size=int(n)))


def texte_action(rng, cout_texte: str | None, mots_signal=()) -> str:
    """Action factice au format de l'environnement (ACTION, TITLE, PROPOSAL, CONTROLS, COST, PREDICTION)."""
    corps = _phrase(rng, MOTS_COMMUNS, rng.integers(12, 40))
    if mots_signal:
        corps += " " + " ".join(w for w in mots_signal if rng.random() < 0.6)
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
    return [f"{v:.0f}", f"{v:.0f} GPU-hours", f"about {v:.0f} GPU hours", f"{v:.0f}h"][int(rng.integers(0, 4))]


def ecrire_manifeste(racine: Path, run: str, config: dict, cles: list[str], entropie: int, cree_le: str | None = None,
                     decisif: bool = False) -> Path:
    from controle_ia.manifeste import config_canonique, graines
    from controle_ia.scellement import sceller

    m = {"run_id": run, "cree_le": cree_le or datetime.now(timezone.utc).isoformat(timespec="seconds"), "commit": "0" * 40,
         "depot_propre": True, "decisif": decisif,
         "preenregistrement": {"chemin": "prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md", "sha256": PREREG_SHA}
         if decisif else None, "config": config,
         "config_sha256": hashlib.sha256(config_canonique(config)).hexdigest(), "versions": {"note": "manifeste factice"},
         "graines": graines(list(dict.fromkeys(cles)), entropie), "commande": "fabrique factice (essais du lecteur du texte)",
         "reserves": ["manifeste FACTICE : aucune donnée du programme"]}
    d = Path(racine) / "runs" / run
    d.mkdir(parents=True, exist_ok=False)
    chemin = d / "manifeste.json"
    chemin.write_text(json.dumps(m, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(chemin)
    return chemin


def fabriquer(racine, run: str, lecture: str | None = None, graine: int = 0, decalages: dict | None = None,
              illisibles: dict | None = None, mots_signal: dict | None = None, bruit: float = 0.3, n_taches: int = 64,
              entropie: int = 12345, mode: str = "jouet", cree_le: str | None = None, imposer: dict | None = None,
              n_tirages_lecture: int = 200) -> dict:
    """Écrit sous `racine` : `runs/<run>/manifeste.json` et `donnees/<run>/blocs/<NN>-<tâche>/` (mesures, textes, fiches,
    bloc.json, scellés) ; puis, si `lecture` est donné, `diag/<lecture>/lecture-cout-dose-reponse.json` (lecture du coût
    calculée par `lecture_v2.lire`, `imposer` appliqué)."""
    from controle_ia.dose_reponse import course_v2 as cr
    from controle_ia.manifeste import generateur

    racine = Path(racine)
    rng = np.random.default_rng(int(graine))
    dec = {**DECALAGES_SAINS, **(decalages or {})}
    ill = {**ILLISIBLES_SAINS, **(illisibles or {})}
    sig = MOTS_SIGNAL_SAINS if mots_signal is None else mots_signal
    taches = taches_factices(n_taches)
    config = {"mode": mode, "objet": "FACTICE", "prereg": {"chemin": "prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md",
                                                           "sha256": PREREG_SHA},
              "designation_critere_3": {"chemin": DESIGNATION[0], "sha256": DESIGNATION[1],
                                        "lignes_registre": ["DESIGNATION-CRITERE-3"]}}
    cles = cr.noms_des_graines(taches, [])
    chemin_m = ecrire_manifeste(racine, run, config, cles, entropie, cree_le, decisif=(mode == "reel"))
    man = json.loads(chemin_m.read_text(encoding="utf-8"))
    g = man["graines"]
    ordre = cr.ordre_des_taches(taches, g)
    entete = {"prereg_sha256": PREREG_SHA, "config_sha256": "f" * 64, "entropie": g["ordre-des-taches"]["entropie"],
              "commit_code": "0" * 40}
    centre = {t: float(rng.normal(2.5, 0.5)) for t in taches}
    fmt = SimpleNamespace(fins={0})
    dossier = racine / "donnees" / run
    dossier.mkdir(parents=True, exist_ok=False)
    for k, t in enumerate(ordre):
        lignes, textes, fiches = [], [], []
        for c in CONDITIONS:
            for r in (1, 2):
                for p in range(10):
                    illisible = bool(rng.random() < ill[c])
                    v = 10.0 ** (centre[t] + dec[c] + float(rng.normal(0.0, bruit)))
                    texte = texte_action(rng, _cout_texte(rng, v, illisible), sig.get(c, ()))
                    ids = [int(x) for x in rng.integers(1, 1000, size=len(texte.split()))]
                    a = SimpleNamespace(texte=texte, ids=ids, debut=0, fin=len(ids), pas=p)
                    l = cr.ligne_de_mesure(c, t, r, a, fmt, 400, [])
                    lignes.append(l)
                    textes.append({"cle": l["cle"], "texte": texte, "ids": ids})
                fiches.append({"episode": cr.id_episode(c, t, r), "condition": c, "tache": t, "replique": r,
                               "pas_designes": [], "injection": {"conforme": True, "note": "FACTICE"}})
        cr.ecrire_bloc(dossier, k, t, lignes, textes, fiches, {}, entete, 15,
                       {"comparables": 0, "passent": 0, "courtes": 0, "echecs": []})
    sortie = {"run": run, "manifeste": chemin_m, "taches": taches, "ordre": ordre, "blocs": dossier / "blocs"}
    if lecture is not None:
        sortie["lecture"] = ecrire_lecture(racine, run, lecture, imposer, entropie, n_tirages_lecture)
    _ = generateur
    return sortie


def imposer_lecture(res: dict, ligne: str | None = None, etablies: list | None = None,
                    qualificatifs: dict | None = None) -> dict:
    """Résultat de lecture à réponse connue (essais) : ligne de table et sa phrase, états « établi » de DR-6 et liste, et
    qualificatifs de l'action médiane (sous C5 ou C6 ; défaut : établi)."""
    from controle_ia.dose_reponse import lecture_v2 as lv

    if etablies is not None:
        for x in res["DR-6"]["table"]:
            x["etat"] = "établi" if x["condition"] in etablies else "non établi"
        res["DR-6"]["etablies"] = [x["condition"] for x in res["DR-6"]["table"] if x["etat"] == "établi"]
    if ligne is not None:
        res["table"]["ligne"] = ligne
        res["table"]["phrase"] = lv.PHRASES[ligne]
        res["table"].pop("qualificatifs", None)
        if ligne in ("C5", "C6"):
            q = {c: lv.QUALIFICATIF_ETABLI for c in res["DR-6"]["etablies"]}
            q.update(qualificatifs or {})
            res["table"]["qualificatifs"] = q
    return res


def ecrire_lecture(racine, run: str, lecture: str, imposer: dict | None = None, entropie: int = 12345,
                   n_tirages: int = 200) -> Path:
    """Lecture du coût par `lecture_v2.lire` sur les blocs écrits (rechargés par `lecture_v2.charger_course`), entrées
    `entrees_sha256` comme `executer_lecture`, `imposer` appliqué, enveloppe `ecrire_resultat` sous un manifeste factice."""
    from controle_ia.dose_reponse import lecture_v2 as lv
    from controle_ia.manifeste import ecrire_resultat, generateur

    racine = Path(racine)
    lignes, episodes, empreintes = lv.charger_course([racine / "donnees" / run])
    entrees = hashlib.sha256("".join(sorted(empreintes)).encode()).hexdigest()
    chemin_m = ecrire_manifeste(racine, lecture, {"lecture": "FACTICE", "entrees_sha256": entrees},
                                lv.noms_des_graines_de_lecture(), entropie)
    m = json.loads(chemin_m.read_text(encoding="utf-8"))
    r = lv.lire(lignes, episodes, lambda nom: generateur(m["graines"][nom]), n_tirages, n_tirages, {}, 64)
    r["entrees_sha256"] = entrees
    r["blocs"] = len(empreintes)
    if imposer:
        r = imposer_lecture(r, **imposer)
    return ecrire_resultat(racine, chemin_m, "lecture-cout-dose-reponse", r)


__all__ = ["fabriquer", "ecrire_lecture", "imposer_lecture", "taches_factices", "texte_action", "CONDITIONS", "INTENSITES",
           "DECALAGES_SAINS", "MOTS_SIGNAL_SAINS"]
