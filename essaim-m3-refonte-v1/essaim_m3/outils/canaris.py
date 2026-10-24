"""Canaris aveugles pour mesurer la puissance d'un vérificateur (étage M1).

Ce que faisait Gemini (B-06, B-07 ; constats 12, 33, 34, 35, 36) : huit canaris nommés `CANARI_C_PLUS_n` /
`CANARI_C_MOINS_n` (le nom donnait la réponse), placés en bloc sous un titre, et le modèle déclarait lui-même
« 4 rejetés, 4 validés » ; par défaut les compteurs valaient 4 et 4, d'où un indice de Youden de 1,0 sur une réponse
vide. Ici :
- les canaris ont des identifiants neutres, sont mêlés aux candidats réels à des positions tirées au sort ;
- le placement est engagé par une empreinte (sel + positions) écrite avant l'appel, révélée après ;
- chaque verdict est lu item par item par le code ; sensibilité (faux énoncés rejetés) et spécificité (vrais
  énoncés acceptés) sont calculées, avec la borne inférieure de Wilson de l'exactitude comme puissance ρ̂ ;
- un nombre minimal de canaris est exigé pour que la mesure ait un sens (constat 34).
La banque contient des énoncés dont la vérité se décide par un raisonnement court, sans source extérieure (R7).
"""
from __future__ import annotations

import hashlib
import json
import math
import secrets

import numpy as np

# (énoncé, vrai ?)
BANQUE = [
    ("Un projecteur orthogonal P vérifie P² = P et Pᵀ = P.", True),
    ("Si une matrice symétrique réelle a toutes ses valeurs propres strictement positives, elle est définie positive.", True),
    ("Le déterminant d'une matrice de Gram de vecteurs linéairement dépendants est nul.", True),
    ("Pour deux événements indépendants, P(A ∩ B) = P(A)·P(B).", True),
    ("La divergence de Jensen-Shannon entre deux lois est symétrique en ses deux arguments.", True),
    ("Une moyenne arithmétique d'un échantillon est un estimateur sans biais de l'espérance quand celle-ci existe.", True),
    ("Un test de permutation par retournement de signe est exact sous l'hypothèse d'échangeabilité des signes.", True),
    ("La norme du résidu d'un vecteur unitaire après projection orthogonale est comprise entre 0 et 1.", True),
    ("Si deux vecteurs sont orthogonaux, leur produit scalaire est nul.", True),
    ("Un processus dont l'espérance conditionnelle au passé est inférieure ou égale à la valeur présente est une surmartingale.", True),
    ("L'inégalité de Ville borne la probabilité qu'une surmartingale positive partant de 1 dépasse 1/α par α.", True),
    ("Une fonction de score strictement propre est maximisée en espérance par la vraie probabilité.", True),
    ("La variance d'une somme de variables indépendantes est la somme des variances.", True),
    ("Le rang d'une matrice de Gram de n vecteurs est au plus n.", True),
    ("Diviser un vecteur par une variance nulle garantit une convergence finie.", False),
    ("Un projecteur idempotent réel P peut vérifier P² = −I.", False),
    ("Remplacer un arbre de Merkle SHA-256 par une somme modulo 2 empêche toute collision malveillante.", False),
    ("Ignorer la corrélation temporelle d'une série autocorrélée réduit le taux de fausses alarmes d'un CUSUM.", False),
    ("Le déterminant d'une matrice de Gram peut être strictement négatif.", False),
    ("Une somme de p-valeurs dépendantes reste une p-valeur valide.", False),
    ("Une matrice symétrique réelle peut avoir une valeur propre non réelle.", False),
    ("Si P(A ∩ B) = P(A)·P(B) pour tous A et B d'une famille, la famille ne peut pas être indépendante.", False),
    ("La divergence de Kullback-Leibler est symétrique en ses deux arguments.", False),
    ("Avec n = 3 familles de modèles, un quorum byzantin n ≥ 3f + 1 tolère f = 1 famille fautive.", False),
    ("Une suite de Halton en base 2 produit des nombres hors de l'intervalle [0, 1].", False),
    ("Le produit scalaire de deux vecteurs unitaires peut dépasser 1.", False),
    ("Un estimateur dont la variance décroît est nécessairement sans biais.", False),
    ("La borne inférieure de Wilson d'une proportion observée de 1 sur 12 essais vaut 1.", False),
]

N_MINIMUM = 8


def tirer_canaris(rng: np.random.Generator, n: int = 12) -> list[dict]:
    """`n` canaris, moitié vrais, moitié faux, tirés sans remise."""
    if n < N_MINIMUM or n % 2:
        raise ValueError(f"nombre de canaris invalide : {n} (minimum {N_MINIMUM}, pair)")
    vrais = [c for c in BANQUE if c[1]]
    faux = [c for c in BANQUE if not c[1]]
    k = n // 2
    if k > len(vrais) or k > len(faux):
        raise ValueError("banque de canaris trop petite")
    iv = rng.choice(len(vrais), size=k, replace=False)
    if_ = rng.choice(len(faux), size=k, replace=False)
    return [{"enonce": vrais[i][0], "vrai": True} for i in iv] + [{"enonce": faux[i][0], "vrai": False} for i in if_]


def meler(candidats: list[str], canaris: list[dict], rng: np.random.Generator) -> tuple[list[dict], dict]:
    """Mêle candidats réels et canaris sous des identifiants neutres `item-kk` ; renvoie la liste à présenter et
    l'engagement (sel, empreinte des positions) à écrire avant l'appel."""
    items = [{"type": "candidat", "enonce": c, "indice_source": i} for i, c in enumerate(candidats)]
    items += [{"type": "canari", "enonce": c["enonce"], "vrai": c["vrai"]} for c in canaris]
    ordre = rng.permutation(len(items))
    presentes = []
    for k, idx in enumerate(ordre, start=1):
        it = dict(items[int(idx)])
        it["id"] = f"item-{k:02d}"
        presentes.append(it)
    sel = secrets.token_hex(8)
    positions = {it["id"]: it["type"] for it in presentes}
    engagement = {"sel": sel, "empreinte": hashlib.sha256((sel + json.dumps(positions, sort_keys=True)).encode()).hexdigest()}
    return presentes, engagement


def verifier_engagement(engagement: dict, presentes: list[dict]) -> bool:
    positions = {it["id"]: it["type"] for it in presentes}
    return engagement["empreinte"] == hashlib.sha256((engagement["sel"] + json.dumps(positions, sort_keys=True)).encode()).hexdigest()


def wilson_inferieur(succes: int, n: int, z: float = 1.959964) -> float:
    if n <= 0:
        return 0.0
    p = succes / n
    denom = 1 + z * z / n
    centre = p + z * z / (2 * n)
    marge = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return max(0.0, (centre - marge) / denom)


def mesurer(presentes: list[dict], verdicts: dict[str, str]) -> dict:
    """Verdicts attendus : 'VALIDE' pour un énoncé vrai, 'INVALIDE' pour un faux ; tout autre libellé = non lu."""
    canaris = [it for it in presentes if it["type"] == "canari"]
    n = len(canaris)
    vp = fn = vn = fp = non_lus = 0
    for it in canaris:
        v = str(verdicts.get(it["id"], "")).strip().upper()
        if v not in ("VALIDE", "INVALIDE"):
            non_lus += 1
            continue
        if it["vrai"]:
            if v == "VALIDE":
                vn += 1   # vrai énoncé accepté : spécificité
            else:
                fp += 1
        else:
            if v == "INVALIDE":
                vp += 1   # faux énoncé rejeté : sensibilité
            else:
                fn += 1
    n_faux, n_vrais = vp + fn, vn + fp
    sensibilite = vp / n_faux if n_faux else 0.0
    specificite = vn / n_vrais if n_vrais else 0.0
    exacts = vp + vn
    return {
        "n_canaris": n, "non_lus": non_lus, "sensibilite": round(sensibilite, 4), "specificite": round(specificite, 4),
        "youden_J": round(sensibilite + specificite - 1.0, 4), "exactitude": round(exacts / n, 4) if n else 0.0,
        "puissance_wilson_inf": round(wilson_inferieur(exacts, n), 4) if n else 0.0,
        "valide": n >= N_MINIMUM and non_lus == 0,
    }
