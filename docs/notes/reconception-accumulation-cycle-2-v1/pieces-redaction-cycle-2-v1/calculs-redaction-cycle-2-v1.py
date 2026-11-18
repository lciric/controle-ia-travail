"""Arithmétique du rédacteur du second cycle (accumulation des scores sur l'épisode) — v1.

Aucune donnée lue, aucune analyse : effectifs sous lois normales supposées, heures et dollars
à partir des débits et des prix que citent les textes scellés (sources recopiées dans le devis).
Bibliothèque standard seulement. Lancement : python3 calculs-redaction-cycle-2-v1.py
"""
from math import comb, sqrt
from statistics import NormalDist

N = NormalDist()
z = N.inv_cdf


def taches(et64: float, m: float, alpha_unilateral: float, puissance: float = 0.80) -> float:
    """Tâches pour détecter un écart m (test unilatéral), l'erreur type valant et64 à 64 tâches."""
    return 64.0 * (et64 * (z(1 - alpha_unilateral) + z(puissance)) / m) ** 2


def puissance(et64: float, m: float, alpha_unilateral: float, n: int) -> float:
    et = et64 * sqrt(64.0 / n)
    return N.cdf(m / et - z(1 - alpha_unilateral))


print("== 1. Effectifs (lois normales supposees ; erreur type a 64 taches = hypothese de planification)")
print("   controle : table de la note de conception (niveau 0,025/3)")
for et in (0.034, 0.038, 0.045):
    print(f"   et64={et:.3f}", " ".join(f"m={m:.2f}:{taches(et, m, 0.025 / 3):7.1f}" for m in (0.03, 0.05, 0.10)))
print("   une sonde principale, quatre doses (niveau 0,025/4), m = 0,05")
for et in (0.034, 0.038, 0.045):
    print(f"   et64={et:.3f} taches={taches(et, 0.05, 0.025 / 4):7.1f}",
          " ".join(f"P(n={n})={puissance(et, 0.05, 0.025 / 4, n):.3f}" for n in (350, 400, 450, 500, 600)))
print("   trois sondes decisives, quatre doses (niveau 0,025/12), m = 0,05")
for et in (0.034, 0.038, 0.045):
    print(f"   et64={et:.3f} taches={taches(et, 0.05, 0.025 / 12):7.1f}")
print("   queue nominale divisee par deux (marge du premier cycle), une sonde, quatre doses (0,025/8)")
for et in (0.034, 0.038, 0.045):
    print(f"   et64={et:.3f} taches={taches(et, 0.05, 0.025 / 8):7.1f}",
          " ".join(f"P(n={n})={puissance(et, 0.05, 0.025 / 8, n):.3f}" for n in (400, 500, 600)))
print("   equivalence a la marge m = 0,05 quand l'ecart vrai est nul (borne haute unilaterale 0,025, par dose)")
for et in (0.034, 0.038, 0.045):
    for n in (400, 600):
        e = et * sqrt(64.0 / n)
        p = N.cdf(0.05 / e - z(0.975))
        print(f"   et64={et:.3f} n={n} P(une dose)={p:.3f} P(quatre doses, independantes)={p ** 4:.3f}")

print("== 2. Suite des cycles sous le nul global (niveau 0,025 par cycle)")
a = 0.025
for k in (1, 2, 3, 4, 6, 8, 10, 20, 40):
    print(f"   K={k:2d} sans correction: 1-(1-a)^K={1 - (1 - a) ** k:.4f}  avec replication: K*a^2<={k * a * a:.5f}")
print("   depense du niveau a_k = a*6/(pi^2 k^2) : k=1..5 ->",
      " ".join(f"{a * 6 / (3.141592653589793 ** 2 * k * k):.5f}" for k in range(1, 6)))
print("   taches au rang k sous cette depense (une sonde, quatre doses, et64=0,038, m=0,05) :",
      " ".join(f"k={k}:{taches(0.038, 0.05, a * 6 / (3.141592653589793 ** 2 * k * k) / 4):.0f}" for k in range(1, 5)))

print("== 3. Garde de specificite (formulation B de la decision) : alertes sur n episodes temoins")


def binom_cdf(x: int, n: int, p: float) -> float:
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(x + 1))


def cp_haut(x: int, n: int, niveau: float = 0.95) -> float:
    """Borne haute unilaterale de Clopper-Pearson, par dichotomie."""
    bas, haut = 0.0, 1.0
    for _ in range(80):
        mil = (bas + haut) / 2
        if binom_cdf(x, n, mil) > 1 - niveau:
            bas = mil
        else:
            haut = mil
    return haut


for n in (100, 150, 200, 300, 400):
    xmax = max(x for x in range(n) if cp_haut(x, n) < 0.05) if cp_haut(0, n) < 0.05 else -1
    p_passe = binom_cdf(xmax, n, 0.01) if xmax >= 0 else 0.0
    print(f"   n={n} alertes tolerees (borne haute 95 % < 5 %)={xmax} P(passe | taux vrai 1 %)={p_passe:.3f}"
          f" P(passe | taux vrai 5 %)={binom_cdf(xmax, n, 0.05) if xmax >= 0 else 0.0:.3f}")

print("== 3 bis. Epreuve plantee, signal nul : nombre de fausses issues tolere sur T tirages (niveau 0,025)")
for T in (100, 200):
    c = max(x for x in range(T) if binom_cdf(x, T, 0.025) <= 0.97)
    while binom_cdf(c, T, 0.025) < 0.95:
        c += 1
    print(f"   T={T} seuil c={c} P(X<=c | 0,025)={binom_cdf(c, T, 0.025):.3f} P(X<=c | 0,05)={binom_cdf(c, T, 0.05):.3f}"
          f" P(X<=c | 0,075)={binom_cdf(c, T, 0.075):.3f} ; borne haute de Clopper-Pearson (95 %, unilaterale) pour c : {cp_haut(c, T):.4f} ; pour 0 : {cp_haut(0, T):.4f}")

print("== 4. Devis de la famille neuve (debits et prix : textes scelles, voir le devis)")
S_EP, S_PASSE = 40.2, 0.45           # secondes par episode (lots de 8) ; par passe de relecture
PRIX_BAS, PRIX_HAUT, PRIX_PIRE = 1.0889, 1.30, 1.40
DISQUE, DESCENTE = 0.08, 0.05        # USD par heure ; USD par Go


def famille(n_eval: int, second_temoin: bool, sans_episodes_temoin: bool = False):
    cond = 9 - (4 if sans_episodes_temoin else 0)
    ep_dist = 2 * 32 * 5
    ep_eval = cond * n_eval
    series = (2 if sans_episodes_temoin else 4) * 4 + 2 * 4 + 1          # cellules texte x etat, honnetes relus, HH
    if second_temoin:
        series += 2 * 4
    passes = series * n_eval
    echelle = 4 * 12 * 16 * (2 if second_temoin else 1)
    h_dist_donnees = ep_dist * S_EP / 3600
    h_eval = ep_eval * S_EP / 3600
    n_adapt = 3 if second_temoin else 2
    h_distill = (0.23 * n_adapt, 0.46 * n_adapt)
    h_passe = (passes + echelle) * S_PASSE / 3600
    h_relecture = (h_passe * 0.35 / 0.15, h_passe * 0.55 / 0.15)          # rapport de l'etape B bis, ecriture comprise
    jetons_m = passes * 2230 / 1e6
    dirs = 3 * 800                                                        # 800 directions par couche lue, trois couches au plus
    h_notation = (0.1 * jetons_m / 4.1 * dirs / 3200, 0.5 * jetons_m / 4.1 * dirs / 3200)
    fixes_g, fixes_r = 1.0 + 0.6 + 0.1 + 0.3, 1.0 + 0.3 + 0.3
    g = (h_dist_donnees + h_distill[0] + h_eval + fixes_g, h_dist_donnees + h_distill[1] + h_eval + fixes_g)
    r = (h_relecture[0] + h_notation[0] + fixes_r, h_relecture[1] + h_notation[1] + fixes_r)
    return dict(ep_dist=ep_dist, ep_eval=ep_eval, passes=passes, echelle=echelle, h_dist_donnees=h_dist_donnees,
                h_eval=h_eval, h_distill=h_distill, h_passe=h_passe, h_relecture=h_relecture, jetons_m=jetons_m,
                h_notation=h_notation, g=g, r=r)


def dollars(g, r, go_bas=20, go_haut=40):
    bas = (g[0] + r[0]) * PRIX_BAS + DISQUE * (g[0] + r[0]) + 2 * go_bas * DESCENTE
    haut = (g[1] + r[1]) * PRIX_HAUT + DISQUE * (g[1] + r[1] + 2.0) + 2 * go_haut * DESCENTE
    p1 = 2 * (g[1] + r[1]) * PRIX_PIRE + DISQUE * (2 * (g[1] + r[1]) + 2.0) + 2 * go_haut * DESCENTE
    p2 = p1 + 2 * g[1] * PRIX_PIRE + DISQUE * 2 * g[1] + go_haut * DESCENTE
    return bas, haut, p1, p2


for nom, n_eval, st, sans in (("base : 400 taches, un temoin", 400, False, False),
                              ("400 taches, second temoin honnete", 400, True, False),
                              ("500 taches, second temoin honnete", 500, True, False),
                              ("600 taches, second temoin honnete (plafond d'effectif)", 600, True, False),
                              ("variante sans episodes du temoin, 400 taches", 400, False, True)):
    f = famille(n_eval, st, sans)
    b, h, p1, p2 = dollars(f["g"], f["r"])
    print(f"   -- {nom}")
    print(f"      episodes : distillation {f['ep_dist']} ({f['h_dist_donnees']:.2f} h) ; evaluation {f['ep_eval']} ({f['h_eval']:.2f} h)")
    print(f"      distillation {f['h_distill'][0]:.2f} a {f['h_distill'][1]:.2f} h ; passes {f['passes']} + echelle {f['echelle']}"
          f" = {f['h_passe']:.2f} h de passe ; relecture {f['h_relecture'][0]:.2f} a {f['h_relecture'][1]:.2f} h")
    print(f"      jetons relus {f['jetons_m']:.1f} millions ; notation {f['h_notation'][0]:.2f} a {f['h_notation'][1]:.2f} h")
    print(f"      piece G {f['g'][0]:.1f} a {f['g'][1]:.1f} h ; piece R {f['r'][0]:.1f} a {f['r'][1]:.1f} h ;"
          f" total {f['g'][0] + f['r'][0]:.1f} a {f['g'][1] + f['r'][1]:.1f} h")
    print(f"      attendu {b:.1f} a {h:.1f} USD ; pire cas P1 (hote deux fois plus lent, 1,40) {p1:.1f} USD ;"
          f" P2 (P1 + relance entiere de la piece G) {p2:.1f} USD")

print("== 5. Relecture complementaire du temps 1 (donnees de developpement ; hors famille neuve)")
passes_t1 = 576 + 256 + 64 + 256 + 64 + 4 * 64 * 2 + 4 * 64 * 4
h_passe = passes_t1 * S_PASSE / 3600
marche = (1.0 + 0.5 + 0.05 + h_passe * 0.35 / 0.15 + 0.05 + 1.0 + 0.2, 1.0 + 0.5 + 0.05 + h_passe * 0.55 / 0.15 + 0.05 + 6.0 + 0.4)
go_act = passes_t1 * 49 / 1216
print(f"   passes {passes_t1} ; {h_passe:.2f} h de passe ; activations ~{go_act:.0f} Go (trois couches) ; marche {marche[0]:.1f} a {marche[1]:.1f} h")
print(f"   attendu {marche[0] * PRIX_BAS + DISQUE * marche[0] + 20 * DESCENTE:.1f} a"
      f" {marche[1] * PRIX_HAUT + DISQUE * (marche[1] + 1) + 40 * DESCENTE:.1f} USD ;"
      f" pire cas (deux fois plus lent, 1,40, une relance) {2 * (2 * marche[1] * PRIX_PIRE + DISQUE * 2 * marche[1]) + 4:.1f} USD")
