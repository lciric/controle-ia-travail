"""Calcul de puissance reproductible — comparaison des règles de choix de paire — v1 (annexe de la conception, § 6).

Lancement (dossier temporaire vide, chemin absolu) :
    python3 -I -B <chemin absolu>/calcul-puissance-comparaison-regles-paires-v1.py > <…>-sortie.txt

Tout est SUPPOSÉ sauf ce qui cite une source. Aucune donnée réelle. Graines : SeedSequence dérivées par tâche (R9).
Tests unilatéraux (signe prédit : bras > hasard) ; famille de m comparaisons au hasard sous Holm ; la puissance est
calculée au niveau le plus dur de Holm (α/m), donc prudente pour chaque bras.
"""
import math
import sys
from pathlib import Path
from statistics import NormalDist

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import regles_paires_v1 as rp  # noqa: E402

Z = NormalDist()
ALPHA, PUISSANCE, M_BRAS = 0.05, 0.80, 6   # six bras comparés au hasard (Gu-Krenn, basique, méta, Swanson, liens, Uzzi)
RACINE = 20261101


def var_hanley_mcneil(A, n1, n0):
    """Variance de l'aire (Hanley et McNeil 1982, modèle exponentiel)."""
    q1, q2 = A / (2 - A), 2 * A * A / (1 + A)
    return (A * (1 - A) + (n1 - 1) * (q1 - A * A) + (n0 - 1) * (q2 - A * A)) / (n1 * n0)


def var_nulle(n1, n0):
    """Variance de l'aire d'un classement au hasard (Mann-Whitney sous H0)."""
    return (n1 + n0 + 1) / (12.0 * n1 * n0)


def positives_requises(A1, A0, pi, alpha, puissance, mode, r=0.0):
    """Plus petit nombre de positives n1 (n0 = n1 (1 − π)/π) qui atteint la puissance.
    mode 'exact' : aire du bras contre 0,5 exact ; 'hasard' : contre un bras hasard réalisé, indépendant ;
    'bras' : deux bras réels corrélés (r) sur les mêmes paires."""
    za, zb = Z.inv_cdf(1 - alpha), Z.inv_cdf(puissance)
    n1 = 5
    while n1 < 10 ** 7:
        n0 = max(1, round(n1 * (1 - pi) / pi))
        v1 = var_hanley_mcneil(A1, n1, n0)
        if mode == "exact":
            ok = za * math.sqrt(var_nulle(n1, n0)) + zb * math.sqrt(v1) <= (A1 - A0)
        elif mode == "hasard":
            v = v1 + var_nulle(n1, n0)
            ok = (za + zb) * math.sqrt(v) <= (A1 - A0)
        else:
            v0 = var_hanley_mcneil(A0, n1, n0)
            v = v1 + v0 - 2 * r * math.sqrt(v1 * v0)
            ok = (za + zb) * math.sqrt(v) <= (A1 - A0)
        if ok:
            return n1, n1 + n0
        n1 = int(math.ceil(n1 * 1.02)) if n1 > 200 else n1 + 1
    return None, None


def ecart_detectable(N, pi, alpha, puissance, A0=0.5):
    """Plus petit écart d'aire détectable contre un hasard réalisé, à N paires et taux de base π."""
    n1 = round(N * pi); n0 = N - n1
    za, zb = Z.inv_cdf(1 - alpha), Z.inv_cdf(puissance)
    d = 0.0005
    while d < 0.5:
        if (za + zb) * math.sqrt(var_hanley_mcneil(A0 + d, n1, n0) + var_nulle(n1, n0)) <= d:
            return d
        d += 0.0005
    return None


def simulation(pi, N, A1, alpha, R, tache):
    """Vérification par simulation binormale (positifs N(μ,1), négatifs N(0,1), μ = √2 Φ⁻¹(A1)) contre un hasard
    réalisé, test de DeLong apparié du module (rp.comparer_au_hasard)."""
    rng = rp.rng_tache(RACINE, tache)
    mu = math.sqrt(2) * Z.inv_cdf(A1)
    n1 = round(N * pi)
    y = np.r_[np.ones(n1, int), np.zeros(N - n1, int)]
    rejets = 0
    for _ in range(R):
        bras = rng.normal(0, 1, N) + mu * y
        hasard = rng.permutation(N).astype(float)
        c = rp.comparer_au_hasard({"hasard": hasard, "bras": bras}, y)["bras"]
        rejets += c["p"] <= alpha
    return rejets / R


def main():
    print("# Calcul de puissance — comparaison des règles de choix de paire — v1")
    print(f"numpy {np.__version__} ; racine {RACINE} ; α familial {ALPHA} unilatéral ; puissance visée {PUISSANCE} ;"
          f" m = {M_BRAS} bras contre le hasard (Holm, rang le plus dur α/m = {ALPHA / M_BRAS:.5f})")
    print()
    print("## 1. Épreuve 1 — écart de 10 points d'aire (0,60 contre 0,50)")
    print("Taux de base π : 0,275 % = taux de la rétrodiction de Swanson (retrodiction-swanson-v1.md, 2 752 positives sur"
          " 10⁶) ; 1 % et 3 % = ordre de grandeur de Science4Cast (« 1-3 % », 2210.00881 p. 5, à vérifier sur PDF) ;"
          " 0,1 % = cas défavorable SUPPOSÉ.")
    print("| π | niveau | n positives (exact 0,5) | N paires (exact) | n positives (hasard réalisé) | N paires (hasard réalisé) |")
    print("|---|---|---|---|---|---|")
    for pi in (0.001, 0.00275, 0.01, 0.03):
        for nom, a in (("α/m (pire rang de Holm)", ALPHA / M_BRAS), ("α (dernier rang de Holm)", ALPHA)):
            e1, eN = positives_requises(0.60, 0.50, pi, a, PUISSANCE, "exact")
            h1, hN = positives_requises(0.60, 0.50, pi, a, PUISSANCE, "hasard")
            print(f"| {pi:.5f} | {nom} | {e1} | {eN:,} | {h1} | {hN:,} |".replace(",", " "))
    print()
    print("## 2. Épreuve 1 — bras contre bras (0,70 contre 0,60), mêmes paires, corrélation r des aires")
    print("| π | r | n positives | N paires |")
    print("|---|---|---|---|")
    for pi in (0.00275, 0.01):
        for r in (0.3, 0.5, 0.7):
            n1, N = positives_requises(0.70, 0.60, pi, ALPHA / M_BRAS, PUISSANCE, "bras", r)
            print(f"| {pi:.5f} | {r} | {n1} | {N:,} |".replace(",", " "))
    print()
    print("## 3. Écart d'aire détectable à N fixé (contre hasard réalisé, α/m, puissance 0,8)")
    print("| N paires | π | positives attendues | écart détectable (points d'aire) |")
    print("|---|---|---|---|")
    for N in (10 ** 5, 10 ** 6):
        for pi in (0.001, 0.00275, 0.01):
            d = ecart_detectable(N, pi, ALPHA / M_BRAS, PUISSANCE)
            print(f"| {N:,} | {pi:.5f} | {round(N * pi):,} | {100 * d:.2f} |".replace(",", " "))
    print()
    print("## 4. Vérification par simulation (binormale, DeLong apparié contre hasard réalisé, α/m)")
    print("| π | N | aire du bras | répétitions | puissance simulée | puissance visée |")
    print("|---|---|---|---|---|---|")
    for pi in (0.01, 0.03):
        _, N = positives_requises(0.60, 0.50, pi, ALPHA / M_BRAS, PUISSANCE, "hasard")
        p = simulation(pi, N, 0.60, ALPHA / M_BRAS, 400, f"simulation-{pi}")
        print(f"| {pi} | {N:,} | 0.60 | 400 | {p:.3f} | {PUISSANCE} |".replace(",", " "))
    print("Erreur-type de Monte-Carlo à 400 répétitions : ≈ 0,02.")
    print()
    print("## 5. Précision à k : condition de jugeabilité (≥ 50 positives attendues pour le hasard)")
    print("| π | k minimal |")
    print("|---|---|")
    for pi in (0.001, 0.00275, 0.01, 0.03):
        print(f"| {pi:.5f} | {math.ceil(50 / pi):,} |".replace(",", " "))
    print()
    print("## 6. Épreuve 2 — panel à l'aveugle, intérêt de 1 à 5 (protocole SciMuse)")
    s = 0.034 * math.sqrt(1516)
    print(f"Écart-type des notes s = 0,034 × √1516 = {s:.3f} (erreur-type 0,034 du bras « impact prédit », n = 1 516 ;"
          " 2405.17044 v4, p. 7 et fig. 9 p. 20 de l'index physique ; à vérifier sur PDF). Fusions par bras F pour un"
          " écart Δ contre le hasard, r = 3 notes par fusion, corrélation intra-fusion ρ (SUPPOSÉ) :"
          " F = 2 (z_α + z_β)² s² (ρ + (1 − ρ)/r) / Δ².")
    print("| Δ (points sur 5) | m bras entrés | ρ | fusions par bras | notes par bras | notes au total (m + hasard) |"
          " coût illustratif (USD) |")
    print("|---|---|---|---|---|---|---|")
    cout_note, cout_fusion = 4.0, 0.204
    for d in (0.1, 0.2, 0.3, 0.5):
        for m in (1, 3, 6):
            for rho in (0.1, 0.3):
                za, zb = Z.inv_cdf(1 - ALPHA / m), Z.inv_cdf(PUISSANCE)
                F = math.ceil(2 * (za + zb) ** 2 * s * s * (rho + (1 - rho) / 3) / d ** 2)
                notes = 3 * F * (m + 1)
                cout = notes * cout_note + F * (m + 1) * cout_fusion
                print(f"| {d} | {m} | {rho} | {F:,} | {3 * F:,} | {notes:,} | {cout:,.0f} |".replace(",", " "))
    print("Coût illustratif : 4 USD par note (4 minutes d'expert à 60 USD de l'heure, SUPPOSÉ ; nul si bénévoles comme"
          " dans SciMuse) + 0,204 USD par fusion (fusion observée, devis v6 de la course 2, cité par le brouillon 10 du"
          " pré-pilote). Repère : SciMuse a vu des écarts de ≈ 0,1 point (2,350 ; 2,446 ; 2,414, p. 7).")


if __name__ == "__main__":
    main()
