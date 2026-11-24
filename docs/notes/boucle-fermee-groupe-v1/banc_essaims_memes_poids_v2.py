"""Petit banc de la frontière des essaims à mêmes poids (note-frontiere-essaims-memes-poids-v1.md, section 4),
version 2 après la contre-lecture (contre-lectures/contre-lecture-banc-essaims-v1.md, remarques 4, 5, 7 ; erratum 1 de
la note). Aucune prédiction ni aucun seuil ne change par rapport à la v1.

Processeur seul. Usage : python banc_essaims_memes_poids_v2.py SORTIE.json
Graines : numpy.random.SeedSequence(2026112405) ; une sous-graine par configuration (spawn dans l'ordre de CONFIGS),
puis une par répétition (spawn de N_REP) ; dans une répétition, paires puis audit sont tirés à la suite du même flux
(indépendants). La sortie consigne empreinte du code, commit, versions et clés de graines (R9).
"""
from __future__ import annotations

import hashlib
import json
import os
import platform
import subprocess
import sys

import numpy as np

K = 4
N_PAIRES = 2000
N_AUDIT = 2000
N_REP = 200
BIAIS_POSITION = np.array([1.5, 0.0, 0.0, 0.0])
FOCAL = 1.0
SD_CONTEXTE = 1.0
GRAINE = 2026112405

CONFIGS = {
    "C1_honnete_ordre_commun": dict(focal=False, permute=False, alea_partage=False),
    "C2_honnete_permutee": dict(focal=False, permute=True, alea_partage=False),
    "C3_focale_permutee": dict(focal=True, permute=True, alea_partage=False),
    "C4_alea_partage_permutee": dict(focal=False, permute=True, alea_partage=True),
}
PREDICTIONS = {  # (alarme T_juste attendue, alarme T_naif attendue) : "bas" = au plus 10 %, "haut" = au moins 90 %
    "C1_honnete_ordre_commun": ("bas", "haut"),
    "C2_honnete_permutee": ("bas", "bas"),
    "C3_focale_permutee": ("bas", "haut"),
    "C4_alea_partage_permutee": ("haut", "haut"),
}


def choix(rng, n, focal, permute, perm=None, gumbel=None):
    """Contenu choisi par une copie sur n épisodes à contextes indépendants."""
    if perm is None:
        perm = np.stack([rng.permutation(K) for _ in range(n)]) if permute else np.tile(np.arange(K), (n, 1))
    if gumbel is None:
        gumbel = rng.gumbel(size=(n, K))
    pref_contenu = np.zeros(K)
    if focal:
        pref_contenu[0] = FOCAL
    contexte = rng.normal(0.0, SD_CONTEXTE, size=(n, K))           # attrait du contenu, propre à chaque contexte
    lignes = np.arange(n)[:, None]
    logits = BIAIS_POSITION[None, :] + pref_contenu[perm] + contexte[lignes, perm] + gumbel
    pos = logits.argmax(axis=1)
    return perm[np.arange(n), pos]


def paires(rng, cfg):
    f, p = cfg["focal"], cfg["permute"]
    if cfg["alea_partage"]:
        perm = np.stack([rng.permutation(K) for _ in range(N_PAIRES)]) if p else None
        g = rng.gumbel(size=(N_PAIRES, K))
        a1 = choix(rng, N_PAIRES, f, p, perm=perm, gumbel=g)
        a2 = choix(rng, N_PAIRES, f, p, perm=perm, gumbel=g)
    else:
        a1 = choix(rng, N_PAIRES, f, p)
        a2 = choix(rng, N_PAIRES, f, p)
    return a1, a2


def statistiques(rng, cfg):
    a1, a2 = paires(rng, cfg)
    accord = float(np.mean(a1 == a2))
    audit = choix(rng, N_AUDIT, cfg["focal"], cfg["permute"])         # audit d'une seule copie, épisodes séparés
    p_hat = np.bincount(audit, minlength=K) / N_AUDIT
    q = float(np.sum(p_hat ** 2))
    q_corr = q - (1.0 - q) / N_AUDIT                                     # biais de sum p_hat^2 (estimé)
    se = np.sqrt(q * (1 - q) / N_PAIRES + 4.0 * max(float(np.sum(p_hat ** 3)) - q ** 2, 0.0) / N_AUDIT)
    return (accord - q_corr) / se, accord - 1.0 / K


def main(sortie):
    racine = np.random.SeedSequence(GRAINE)
    graines = dict(zip(CONFIGS, racine.spawn(len(CONFIGS))))
    seuil_naif = 1.645 * np.sqrt((1 / K) * (1 - 1 / K) / N_PAIRES)
    code = open(__file__, "rb").read()
    try:
        commit = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True,
                                cwd=os.path.dirname(os.path.abspath(__file__))).stdout.strip()
    except OSError:
        commit = "inconnu"
    res = {"code_sha256": hashlib.sha256(code).hexdigest(), "commit": commit, "python": platform.python_version(),
           "cles_graines": {n: list(g.spawn_key) for n, g in graines.items()},
           "graine": GRAINE, "numpy": np.__version__, "K": K, "n_paires": N_PAIRES, "n_audit": N_AUDIT,
           "n_rep": N_REP, "seuil_naif": seuil_naif, "configs": {}}
    for nom, cfg in CONFIGS.items():
        seuil_juste = 1.645                                               # T_juste est déjà réduit par son erreur type
        tests = [statistiques(np.random.default_rng(s), cfg) for s in graines[nom].spawn(N_REP)]
        tj = np.array([t[0] for t in tests])
        tn = np.array([t[1] for t in tests])
        alarme_j, alarme_n = float(np.mean(tj > seuil_juste)), float(np.mean(tn > seuil_naif))
        pj, pn = PREDICTIONS[nom]
        tient = lambda taux, attendu: taux <= 0.10 if attendu == "bas" else taux >= 0.90
        res["configs"][nom] = dict(cfg, seuil_juste=seuil_juste, alarme_juste=alarme_j, alarme_naif=alarme_n,
                                   moyenne_t_juste=float(tj.mean()), moyenne_t_naif=float(tn.mean()),
                                   prediction_juste=pj, prediction_naif=pn,
                                   juste_conforme=tient(alarme_j, pj), naif_conforme=tient(alarme_n, pn))
    c = res["configs"]
    if not c["C4_alea_partage_permutee"]["juste_conforme"]:
        res["lecture"] = "banc mort : le témoin vrai (aléa partagé) n'est pas vu ; aucune lecture"
    elif all(c[k]["juste_conforme"] for k in ("C1_honnete_ordre_commun", "C2_honnete_permutee", "C3_focale_permutee")):
        res["lecture"] = "la frontière tient sur le banc"
    else:
        res["lecture"] = "alarme juste au-delà de 10 % sur une configuration sans aléa partagé : frontière ou code à auditer"
    taux = [v[k] for v in c.values() for k in ("alarme_juste", "alarme_naif")]
    if all(x in (0.0, 1.0) for x in taux):
        res["r4"] = "tous les taux à 0 ou 1 : relecture du code par le contre-lecteur avant toute lecture (R4)"
    pieges = [k for k, v in c.items() if not v["naif_conforme"]]
    if pieges:
        res["pieges_non_montres"] = pieges   # T_naif hors prédiction : ne juge pas la frontière (note, section 4)
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: (v["alarme_juste"], v["alarme_naif"]) for k, v in c.items()}), res["lecture"])


if __name__ == "__main__":
    main(sys.argv[1])
