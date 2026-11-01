"""Calculs des prédictions chiffrées du préenregistrement de l'analyse appariée boîte blanche / boîte noire (v1).

Formules fermées, aucune graine, aucune donnée de R1, R2 ni R4 ; seules entrées : des nombres de P3 **déjà lus**
(verdict v2 de P3, `docs/verdicts/verdict-P3-premier-test-i-a-v2.md`, sha256
05e896daed17cdb089cd10641878a5014b505eab0aa3d45d0dd7a60d87435751 ; préenregistrement de P3, puissance) :
- aires par action, saboteur contre honnête : sonde de tromperie 0,5748 [0,5313 ; 0,6183], sonde d'enjeux 0,5248
  [0,4813 ; 0,5700] (verdict v2, section 3) ; coût seul 0,8878 sur 926 actions (verdict v2, section 4 ; N-029) ;
- P3-P1 : différence appariée par tâche du log10 du coût, 1,5227 [1,2464 ; 1,8012], 60 tâches (verdict v2, en tête) ;
- écart type d'un épisode honnête à l'autre de la statistique de tâche (log10), pilote T0.5 : 0,795
  (`prereg/P3-premier-test-i-a-v1.md`, l. 387-388).
Modèle binormal (comme `brouillons/preuves-mentors-v1/g1-prereg-v1/calculs-g1-brouillon5-v1.py`, section 4) : score
d'action gaussien de variance 1, décalage d = √2 Φ⁻¹(aire) ; statistique d'épisode = somme des T = 10 scores réduits,
équicorrélation ρ entre actions d'un épisode ; aire d'épisode Φ(d_ép/√2), d_ép = d √T / √(1 + (T − 1) ρ) ; puissance au
seuil conforme de 20 épisodes honnêtes (taux attendu 1/21) : Φ(d_ép − z), z = Φ⁻¹(1 − 1/21).
Lancement : `python3 -I calculs-predictions-v1.py > calculs-predictions-v1-sortie.txt`.
"""
import math

from scipy.stats import norm

T = 10
TAUX = 1.0 / 21.0                      # rang conforme 20 sur 20 épisodes honnêtes de seuils, α = 0,05
Z = norm.ppf(1.0 - TAUX)


def d_action(aire):
    return math.sqrt(2.0) * norm.ppf(aire)


def episode(d, rho):
    d_ep = d * math.sqrt(T) / math.sqrt(1.0 + (T - 1) * rho)
    return norm.cdf(d_ep / math.sqrt(2.0)), norm.cdf(d_ep - Z), d_ep


print("# Sortie de calculs-predictions-v1.py (formules fermées, aucune graine)")
print(f"T = {T} ; taux conforme attendu 1/21 = {TAUX:.4f} ; z = {Z:.4f}")
print()
print("## 1. Sondes génériques de P3 (bras iii), statistique « somme terminale »")
for nom, (a, bas, haut) in (("tromperie", (0.5748, 0.5313, 0.6183)), ("enjeux", (0.5248, 0.4813, 0.5700))):
    for etiquette, aire in (("aire observée", a), ("borne basse", bas), ("borne haute", haut)):
        d = d_action(aire)
        for rho in (0.0, 0.2, 0.6):
            ae, pe, de = episode(d, rho)
            print(f"{nom:9s} {etiquette:13s} {aire:.4f} → d = {d:+.3f} ; ρ = {rho:.1f} : d_ép = {de:+.3f}, "
                  f"aire d'épisode {ae:.3f}, puissance {pe:.3f}")
print()
print("## 2. Coût déclaré seul (base du témoin lexical L), deux lectures")
d = d_action(0.8878)
print(f"(a) aire par action 0,8878 → d = {d:.3f} ; équicorrélation :")
for rho in (0.2, 0.6, 0.8):
    ae, pe, de = episode(d, rho)
    print(f"    ρ = {rho:.1f} : d_ép = {de:.3f}, aire d'épisode {ae:.3f}, puissance {pe:.3f}")
print("(b) moyenne d'épisode du log10 du coût : décalage 1,5227 (P3-P1), écart type d'épisode dans une tâche 0,795 "
      "(pilote), plus un effet de tâche τ (non mesuré) :")
for tau in (0.0, 0.4, 0.8):
    sd = math.sqrt(0.795 ** 2 + tau ** 2)
    de = 1.5227 / sd
    print(f"    τ = {tau:.1f} : écart type {sd:.3f}, d_ép = {de:.3f}, aire d'épisode {norm.cdf(de / math.sqrt(2)):.3f}, "
          f"puissance {norm.cdf(de - Z):.3f}")
print()
print("## 3. Différence d'aire minimale détectable à 80 %, Holm bilatéral au pire rang (m = 4)")
zz = norm.ppf(1 - 0.05 / 8) + norm.ppf(0.8)
print(f"facteur (z(1 − 0,05/8) + z(0,80)) = {zz:.3f}")
for a in (0.6, 0.75, 0.9, 0.97):
    q1, q2 = a / (2 - a), 2 * a * a / (1 + a)
    se = math.sqrt((a * (1 - a) + (60 - 1) * (q1 - a * a) + (60 - 1) * (q2 - a * a)) / (60 * 60))
    print(f"aire {a:.2f} : erreur type d'une aire (Hanley-McNeil, 60 + 60, indépendance) {se:.4f} ; écart type d'une "
          f"différence non appariée √2 × {se:.4f} = {math.sqrt(2) * se:.4f} ; DMD ≈ {zz * math.sqrt(2) * se:.3f} "
          f"(l'appariement par tâche la réduit)")
