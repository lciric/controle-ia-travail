#!/usr/bin/env python3
"""Calculs de la note « la pince hors distribution » (v1).

Lois exactes et approximation normale déclarée ; aucun tirage, aucune donnée du programme.
Toutes les valeurs d'entrée sont des suppositions d'illustration.
Rejeu : python3 -I calculs-pince-hors-distribution-v1.py > calculs-pince-hors-distribution-v1.txt
"""
from math import comb, sqrt

# Monde planté : quatre bandes de tâches. v = réussite attendue de l'honnête (référence calibrée), w = poids.
V = [0.35, 0.60, 0.85, 0.97]
W = [0.15, 0.25, 0.30, 0.30]
F = 0.10          # part des épisodes que le saboteur endommage (un épisode endommagé échoue)
Z = 1.645 + 1.282  # niveau 5 % unilatéral, puissance 0,90 (approximation normale)
SIGMA_LECTURE = 0.10  # bruit supposé de la lecture de l'honnête autour de la référence


def monde(lecture_endommage, decalage_sain=0.0, oracle_voit=True, derive=0.0, reference_a_jour=False,
          lecture_suit_derive=True, f=F):
    """Rend (dommage vrai, terme A, terme B, somme), en espérance par épisode.

    terme A = référence - lecture du suspect ; terme B = lecture du suspect - issue calculée.
    lecture_endommage : lecture sur un épisode endommagé (None = tenue à la valeur de la bande).
    """
    ref = lec = issue = 0.0
    for v, w in zip(V, W):
        reussite_honnete = v - derive
        ref += w * (reussite_honnete if reference_a_jour else v)
        l_sain = (reussite_honnete if lecture_suit_derive else v) + decalage_sain
        l_endo = l_sain if lecture_endommage is None else lecture_endommage
        lec += w * ((1 - f) * l_sain + f * l_endo)
        issue += w * ((1 - f) * reussite_honnete + f * (reussite_honnete if not oracle_voit else 0.0))
    dommage = f * sum(w * (v - derive) for v, w in zip(V, W))
    return dommage, ref - lec, lec - issue, ref - issue


def n_requis(ecart, ecart_type):
    return float("inf") if ecart <= 1e-12 else (Z * ecart_type / ecart) ** 2


def fmt(n):
    return "jamais" if n == float("inf") else f"{n:8.0f}"


print("[P1] Le bilan de la pince : dommage vu par l'oracle = (référence - lecture) + (lecture - issue).")
print("     Par épisode, en espérance ; quatre bandes v =", V, "poids", W, "; part endommagée f =", F)
cas = [
    ("honnête (rien ne doit apparaître)", dict(lecture_endommage=None, f=0.0)),
    ("sabotage, la lecture tombe à 0,05 sur l'épisode endommagé", dict(lecture_endommage=0.05)),
    ("sabotage, la lecture est tenue haute", dict(lecture_endommage=None)),
    ("sabotage, lecture à 0,50 sur l'épisode endommagé", dict(lecture_endommage=0.50)),
    ("sabotage, lecture poussée à 0,99 partout où il endommage", dict(lecture_endommage=0.99)),
    ("sabotage, lecture tenue haute et toutes ses lectures baissées de 0,05", dict(lecture_endommage=None, decalage_sain=-0.05)),
    ("dommage que l'oracle ne voit pas (la pince doit se dire muette)", dict(lecture_endommage=None, oracle_voit=False)),
    ("dérive bénigne de 0,08, référence périmée, lecture qui suit", dict(lecture_endommage=None, f=0.0, derive=0.08)),
    ("dérive bénigne de 0,08, référence périmée, lecture qui ne suit pas", dict(lecture_endommage=None, f=0.0, derive=0.08, lecture_suit_derive=False)),
    ("dérive bénigne de 0,08, référence refaite sur des témoins du régime", dict(lecture_endommage=None, f=0.0, derive=0.08, reference_a_jour=True)),
]
for nom, kw in cas:
    d, a, b, s = monde(**kw)
    vrai = F * sum(w * v for v, w in zip(V, W)) if kw.get("oracle_voit") is False else d
    print(f"     {nom:<72s} dommage vrai {vrai:.4f} | terme A {a:+.4f} | terme B {b:+.4f} | somme {s:+.4f}")

sd_somme = sqrt(sum(w * v * (1 - v) for v, w in zip(V, W)))
print()
print("[P2] Épisodes requis pour voir le dommage (niveau 5 %, puissance 0,90, approximation normale),")
print(f"     selon ce qu'on teste. Écart type par épisode : somme et terme B {sd_somme:.4f} ; terme A {SIGMA_LECTURE:.2f} (supposé).")
for nom, kw in cas[1:6]:
    d, a, b, s = monde(**kw)
    print(f"     {nom:<72s} terme A seul {fmt(n_requis(a, SIGMA_LECTURE))} | terme B seul {fmt(n_requis(b, sd_somme))} | somme {fmt(n_requis(s, sd_somme))}")

print()
print("[P3] Dommage qui reste sous le fil du test de la somme (puissance < 0,90), en épisodes endommagés,")
print("     pour un déploiement de N épisodes : Z * écart type * racine(N). Il ne dépend que de la netteté de la référence.")
vbar = sum(w * v for v, w in zip(V, W))
p_nette = (vbar - 0.02) / 0.96
refs = [
    ("référence sans netteté (taux de base seul)", sqrt(vbar * (1 - vbar))),
    ("référence à quatre bandes (celle du monde)", sd_somme),
    ("référence nette (0,02 ou 0,98, même moyenne)", sqrt(p_nette * 0.98 * 0.02 + (1 - p_nette) * 0.02 * 0.98)),
]
for N in (1000, 10000, 100000):
    for nom, sd in refs:
        x = Z * sd * sqrt(N)
        print(f"     N = {N:6d} | {nom:<46s} écart type {sd:.4f} | {x:7.0f} épisodes, soit {100 * x / N:5.2f} % du déploiement")
print("     Où vit le bruit (part de la variance de la somme, par bande) :")
tot = sum(w * v * (1 - v) for v, w in zip(V, W))
for v, w in zip(V, W):
    print(f"       bande lue {v:.2f} (poids {w:.2f}) : {100 * w * v * (1 - v) / tot:5.1f} %")


def queue_haute(n, c, q):
    return sum(comb(n, k) * q ** k * (1 - q) ** (n - k) for k in range(c, n + 1))


print()
print("[P4] Recapture à deux mâchoires : parmi n épisodes endommagés trouvés par l'audit au hasard,")
print("     X = ceux où les deux mâchoires se taisaient. Plus petits n et c tels que")
print("     P(X >= c | q0) <= 0,05 et P(X >= c | q1) >= 0,90 (loi binomiale exacte).")
for q0, q1 in ((0.10, 0.50), (0.20, 0.60), (0.36, 0.80), (0.10, 0.25)):
    trouve = None
    for n in range(1, 400):
        for c in range(0, n + 1):
            if queue_haute(n, c, q0) <= 0.05:
                if queue_haute(n, c, q1) >= 0.90:
                    trouve = (n, c, queue_haute(n, c, q0), queue_haute(n, c, q1))
                break
        if trouve:
            break
    n, c, r, p = trouve
    print(f"     silence commun validé q0 = {q0:.2f}, silence commun sous attaque neuve q1 = {q1:.2f} : n = {n}, « pince ouverte » si X >= {c} (risque {r:.4f}, puissance {p:.4f})")
