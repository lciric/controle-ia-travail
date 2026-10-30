"""Calculs de puissance du pré-pilote de la course 2, brouillon 2. Processeur seul, aucune donnée de run.
Remplace calcul-puissance-pre-pilote-course-2-v1.py (gardé, R12). Hypothèses déclarées dans le préenregistrement
(brouillon 2) ; toutes les valeurs supposées sont marquées SUPPOSÉ ci-dessous. Graines : SeedSequence(RACINE,
spawn_key=(cle_de_tache(nom),)), même dérivation que src/controle_ia/manifeste.py (R9).
Seuils paramétrés en tête (CP1-11) : si Lazar gèle d'autres valeurs, changer SEUILS et rejouer ; la sortie fait foi.
Sortie : texte sur la sortie standard."""
import hashlib
import platform
import sys

import numpy as np
import scipy
from scipy import stats

RACINE = 20261031  # entropie racine du calcul de puissance (distincte de celle du run, 20261101)
SEUILS = dict(S1=0.80, S2=0.70, S3=0.70, S5_points=20.0, S10_min_sur_12=11, S11_ord=0.10,
              S13=0.90, S14=0.70, S15=0.10, S7_tol=0.10, S18_max_auc=0.70, S19_max_auc=0.65)
N_SIM = 20000


def cle_de_tache(nom):
    return int.from_bytes(hashlib.sha256(nom.encode("utf-8")).digest()[:8], "big")


def rng(nom):
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=(cle_de_tache(nom),)))


print(f"python {platform.python_version()} ; numpy {np.__version__} ; scipy {scipy.__version__} ; racine {RACINE} ; "
      f"tirages {N_SIM}")
print("seuils utilisés :", ", ".join(f"{k}={v}" for k, v in SEUILS.items()))

# ---------------------------------------------------------------- Mesure 1
# Plan du brouillon 2 : P = 6 fonds (4 appariés, 2 simples) -> 10 fiches ; N (classes N1 à N4) = 8 fonds
# (5 appariés, 3 simples) -> 13 fiches. Corrélation entre les deux rendus d'un fond : rho (0 ou 0,6, SUPPOSÉ).


def bloc(g, p, n_app, n_simple, rho):
    a = g.random(n_app) < p
    b = np.where(g.random(n_app) < rho, a, g.random(n_app) < p)
    c = g.random(n_simple) < p
    return (a.sum() + b.sum() + c.sum()) / (2 * n_app + n_simple)


def issue(se_h, sp_h, s):
    ba = (se_h + sp_h) / 2
    if ba >= s["S1"] and se_h >= s["S2"]:
        return "etalonne"
    if ba < s["S3"]:
        return "defaillant"
    return "non_concluant"


def simule_juge(g, v, rho, plan=((4, 2), (5, 3))):
    (pa, ps), (na, ns) = plan
    return bloc(g, v, pa, ps, rho), bloc(g, v, na, ns, rho)


print("\n== M1, règle par juge (estimation ponctuelle : BA >= S1 et rappel P >= S2 -> étalonné ; BA < S3 -> défaillant) ==")
for rho in (0.0, 0.6):
    for v in (0.95, 0.90, 0.85, 0.80, 0.70, 0.60):
        g = rng(f"m1-{v}-{rho}")
        res = [issue(*simule_juge(g, v, rho), SEUILS) for _ in range(N_SIM)]
        r = res.count("etalonne") / N_SIM
        e = res.count("defaillant") / N_SIM
        print(f"  rho={rho:.1f}, juste vraie {v:.2f} : étalonné {r:.2f}, non concluant {1 - r - e:.2f}, défaillant {e:.2f}")

print("\n== M1 sous exclusion de témoins ambigus (sensibilité : P 8 fiches, N 10 fiches ; rho 0,6) ==")
for v in (0.90, 0.85, 0.80):
    g = rng(f"m1-excl-{v}")
    res = [issue(*simule_juge(g, v, 0.6, plan=((3, 2), (4, 2))), SEUILS) for _ in range(N_SIM)]
    print(f"  juste vraie {v:.2f} : étalonné {res.count('etalonne') / N_SIM:.2f}, "
          f"défaillant {res.count('defaillant') / N_SIM:.2f}")

# Probabilité jointe de la porte (CP1-09) : Kimi étalonné ET Argon étalonné ET Opus non défaillant.
# Juges indépendants entre eux à fiches données (SUPPOSÉ ; la corrélation par fiche la rendrait plus haute).
print("\n== Porte M1 jointe (Kimi étalonné ET Argon étalonné ET Opus non défaillant), rho 0,6 ==")
cas = [("tous à 0,90", 0.90, 0.90, 0.90), ("tous à 0,85", 0.85, 0.85, 0.85), ("tous à 0,80", 0.80, 0.80, 0.80),
       ("prédiction P1 (Opus 0,90, Argon 0,85, Kimi 0,80)", 0.90, 0.85, 0.80),
       ("Kimi 0,70, autres 0,90", 0.90, 0.90, 0.70)]
for nom, vo, va, vk in cas:
    g = rng(f"porte-{nom}")
    ouvert = complement = nonouvert = 0
    for _ in range(N_SIM):
        ik = issue(*simule_juge(g, vk, 0.6), SEUILS)
        ia = issue(*simule_juge(g, va, 0.6), SEUILS)
        io = issue(*simule_juge(g, vo, 0.6), SEUILS)
        if ik == ia == "etalonne" and io != "defaillant":
            ouvert += 1
        elif "defaillant" in (ik, ia, io):
            nonouvert += 1
        else:
            complement += 1
    print(f"  {nom} : porte M1 ouverte {ouvert / N_SIM:.2f} ; complément demandé {complement / N_SIM:.2f} ; "
          f"défaillance d'au moins un juge {nonouvert / N_SIM:.2f}")

# Complément (CP1-08 iv) : 12 fonds appariés (P 6, N 6) -> P +12, N +12 ; lecture sur le cumul, mêmes seuils.
print("\n== Complément : lecture sur le cumul (P 22, N 25), mêmes seuils ; risque de faux succès à deux étapes ==")
for v in (0.90, 0.80, 0.70, 0.60):
    g = rng(f"complement-{v}")
    un = deux = 0
    for _ in range(N_SIM):
        se1, sp1 = simule_juge(g, v, 0.6)
        i1 = issue(se1, sp1, SEUILS)
        if i1 == "etalonne":
            un += 1
            continue
        if i1 == "defaillant":
            continue
        se2, sp2 = simule_juge(g, v, 0.6, plan=((6, 0), (6, 0)))
        se = (se1 * 10 + se2 * 12) / 22
        sp = (sp1 * 13 + sp2 * 12) / 25
        if issue(se, sp, SEUILS) == "etalonne":
            deux += 1
    print(f"  juste vraie {v:.2f} : étalonné à l'étape 1 {un / N_SIM:.2f} ; étalonné au total (1 ou cumul) "
          f"{(un + deux) / N_SIM:.2f}")

# ---------------------------------------------------------------- Mesure 2
# Modèle par item (CP1-05) : k items binaires de l'étage 2 (k = 5 : K1 à K5, SUPPOSÉ jusqu'à la consigne figée) ;
# X = 100 x part des items vrais ; un point = 0,01 de cette part ; pas de X = 100/k = 20 points.
# Probabilité qu'un item soit lu « vrai » : logistique(base_item + sév_J + style_F + auto x 1[J = F]),
# base_item = +2,2 si l'item est vrai par construction, -2,2 sinon (bruit de lecture ~ 0,10 par item, SUPPOSÉ).
# Fonds appariés : 10 (Kimi et Argon) ; fonds simples : 8, rendus par un tiers T (CP1-06).
K = 5


def logist(z):
    return 1 / (1 + np.exp(-z))


def x_score(g, vrais, z_extra):
    base = np.where(vrais, 2.2, -2.2)
    return 100 * (g.random(len(vrais)) < logist(base + z_extra)).mean()


def un_tirage_m2(g, auto, style, sev):
    # vrais par item : fiche P (5 vrais) ou N (4 vrais, 1 faux), moitié-moitié
    sp, bc, dsev = [], [], []
    for s in range(10):
        vrais = np.ones(K, bool)
        if s % 2:
            vrais[g.integers(K)] = False
        xkk = x_score(g, vrais, sev + style + auto)   # Kimi juge, rendu Kimi
        xka = x_score(g, vrais, sev - style)          # Kimi juge, rendu Argon
        xak = x_score(g, vrais, -sev + style)         # Argon juge, rendu Kimi
        xaa = x_score(g, vrais, -sev - style + auto)  # Argon juge, rendu Argon
        sp.append((xkk - xka) - (xak - xaa))
        bc.append(xak - xka)
    for s in range(8):  # 8 fonds simples rendus par le tiers T
        vrais = np.ones(K, bool)
        if s % 2:
            vrais[g.integers(K)] = False
        dsev.append(x_score(g, vrais, sev) - x_score(g, vrais, -sev))
    sp, bc, dsev = map(np.array, (sp, bc, dsev))
    bcc = bc.mean() + dsev.mean()
    se_bcc = np.sqrt(bc.var(ddof=1) / 10 + dsev.var(ddof=1) / 8)
    return sp, bcc, se_bcc


print("\n== M2 : résolution de X (k = 5 items, pas 20 points) ; écart-type par fond et erreur-type ==")
g = rng("m2-ecart-type")
sds, ses, sebcc = [], [], []
for _ in range(2000):
    sp, bcc, se_bcc = un_tirage_m2(g, 0.0, 0.0, 0.0)
    sds.append(sp.std(ddof=1)); ses.append(sp.std(ddof=1) / np.sqrt(10)); sebcc.append(se_bcc)
print(f"  sans effet : écart-type de la double différence par fond {np.mean(sds):.1f} points ; "
      f"erreur-type de SP_dd sur 10 fonds {np.mean(ses):.1f} points ; erreur-type de B_cc {np.mean(sebcc):.1f} points")

print("\n== M2 : puissance de l'alarme de biais résiduel (|B_cc| >= S5 et intervalle à 90 % excluant 0) ==")
tq = stats.t(df=16).ppf(0.95)
for style in (0.0, 0.25, 0.5, 0.75, 1.0):
    g = rng(f"m2-alarme-{style}")
    al, vraie = 0, []
    for _ in range(4000):
        _, bcc, se_bcc = un_tirage_m2(g, 0.0, style, 0.4)
        al += (abs(bcc) >= SEUILS["S5_points"] and abs(bcc) - tq * se_bcc > 0)
        vraie.append(bcc)
    print(f"  écart de style (échelle logistique) {style:.2f}, sévérité 0,40 : B_cc moyen {np.mean(vraie):+.1f} points ; "
          f"alarme {al / 4000:.2f}")

print("\n== M2 : SP_dd (descriptif) — probabilité que la borne basse à 90 % dépasse 0 ==")
for auto in (0.0, 0.5, 1.0, 1.5):
    g = rng(f"m2-spdd-{auto}")
    det, moy = 0, []
    for _ in range(4000):
        sp, _, _ = un_tirage_m2(g, auto, 0.2, 0.4)
        moy.append(sp.mean())
        det += sp.mean() - stats.t(df=9).ppf(0.95) * sp.std(ddof=1) / np.sqrt(10) > 0
    print(f"  auto-préférence {auto:.1f} (logistique) : SP_dd moyen {np.mean(moy):+.1f} points ; détectée {det / 4000:.2f}")

# ---------------------------------------------------------------- Mesures 3, 4, 6 : effectifs réels (CP1-10)
print("\n== Bornes de Clopper-Pearson unilatérales à 95 %, aux effectifs réels du brouillon 2 ==")
for n, nom in ((3, "M3, un niveau de paraphrase (vérification)"), (5, "M3, paires inter-fournisseurs (vérification)"),
               (14, "M3, positifs de vérification"), (9, "M6, inventées / altérées"), (12, "M4, concrets"),
               (6, "M4, classes C1 + C2"), (12, "M3 axe 7, paraphrases")):
    print(f"  {nom} : {n} sur {n} -> borne basse {stats.beta.ppf(0.05, n, 1):.2f} ; "
          f"{n - 1} sur {n} -> {stats.beta.ppf(0.05, n - 1, 2):.2f}")
for n, nom in ((4, "M3, voisines NB (vérification)"), (22, "M6, réelles"), (34, "M4, niveau méthode (28 rendus + 6 difficiles)"),
               (12, "M3 axe 7, angles distincts"), (250, "M3, paires NA (vérification, ordre de grandeur)")):
    print(f"  {nom} : 0 sur {n} -> borne haute {float(stats.beta.ppf(0.95, 1, n)):.3f}")

print("\n== Erreurs tolérées par chaque seuil (lecture en estimation ponctuelle) ==")
for nom, n, s, sens in (("S13 inventées", 9, SEUILS["S13"], "rappel"), ("S14 altérées", 9, SEUILS["S14"], "rappel"),
                        ("S15 réelles", 22, SEUILS["S15"], "fa"), ("S11 niveau méthode", 34, SEUILS["S11_ord"], "fa"),
                        ("S7 tolérance vérification NA", 250, SEUILS["S7_tol"], "fa")):
    tol = int(np.floor(n * (1 - s) + 1e-9)) if sens == "rappel" else int(np.floor(n * s + 1e-9))
    print(f"  {nom} : {tol} erreur(s) tolérée(s) sur {n}")

print("\n== M4 : aiguilleur, 12 concrets (3 par classe) ==")
for r in (0.99, 0.95, 0.90, 0.80):
    p11 = 1 - stats.binom.cdf(SEUILS["S10_min_sur_12"] - 1, 12, r)
    p_c12 = r ** 6
    print(f"  rappel vrai {r:.2f} : P(>= {SEUILS['S10_min_sur_12']} sur 12) = {p11:.2f} ; "
          f"P(aucun oubli en C1 et C2, 6 fiches) = {p_c12:.2f}")
for fa in (0.03, 0.10, 0.20):
    print(f"  fausses alertes vraies {fa:.2f} sur 34 fiches de niveau méthode : "
          f"P(taux observé <= {SEUILS['S11_ord']}) = {stats.binom.cdf(int(36 * SEUILS['S11_ord']), 36, fa):.2f}")

print("\n== M5 : débordement de Kimi, deux passes (<= 20 fiches) ==")
for n in (10, 20):
    for p in (0.05, 0.10, 0.20):
        print(f"  n={n}, taux vrai {p:.2f} : P(>= 1 signalée) = {1 - (1 - p) ** n:.2f}")
    print(f"  0 sur {n} -> borne haute unilatérale à 95 % {float(stats.beta.ppf(0.95, 1, n)):.3f}")

# ---------------------------------------------------------------- Contrôles de forme (S18, S19)
# Erreur-type de l'aire sous la courbe (Hanley et McNeil 1982) pour juger ce que « <= 0,70 » distingue.
print("\n== Aire sous la courbe : erreur-type (Hanley-McNeil) ==")


def se_auc(a, n1, n2):
    q1, q2 = a / (2 - a), 2 * a * a / (1 + a)
    return np.sqrt((a * (1 - a) + (n1 - 1) * (q1 - a * a) + (n2 - 1) * (q2 - a * a)) / (n1 * n2))


for nom, n1, n2 in (("S18 témoins (28) contre fiches de Kimi (15)", 28, 15),
                    ("S18 témoins (28) contre fiches de Kimi (20)", 28, 20),
                    ("S19 P (10) contre N (13), entre classes", 10, 13)):
    print(f"  {nom} : erreur-type à 0,50 = {se_auc(0.5, n1, n2):.2f} ; à 0,70 = {se_auc(0.7, n1, n2):.2f}")

# ---------------------------------------------------------------- Module de bisociation (R-601)
print("\n== Bisociation exploratoire : nombre de paires disponibles et coût des fusions (SUPPOSÉ) ==")
for n_fiches in (10, 20, 29):
    print(f"  {n_fiches} fiches de passe 1 dans une case (texte, bras) : {n_fiches * (n_fiches - 1) // 2} paires")
for k in (1, 2, 3, 4):
    cout_pp = 2 * k * (0.40 + 0.25 + 0.057)  # fusion Kimi + trois juges + aiguilleur, par fiche (SUPPOSÉ)
    print(f"  k = {k} (k paires règle N + k paires au hasard) : {2 * k} fusions ; pré-pilote ≈ {cout_pp:.2f} USD ; "
          f"course, 4 cases ≈ {4 * cout_pp:.1f} USD")
print("  P(la fusion d'une paire N est notable plus souvent qu'une paire au hasard) : non calculable à ces effectifs "
      "(module exploratoire, sans revendication)")
print("fin ;", sys.version.split()[0])
