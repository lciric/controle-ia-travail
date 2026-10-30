"""Calculs de puissance du pré-pilote de la course 2, brouillon 5. Processeur seul, aucune donnée de run.
Remplace calcul-puissance-pre-pilote-course-2-v4.py (gardé, R12). Ce qui change par rapport à la v4 (contre-lecture 3,
constats CP4-01 à CP4-16) :
  - CP4-15 : le budget (C13) est lu selon la règle écrite d'A1, étape par étape (cumul + plafond de relais de l'étape
    ≤ plafond S17 ; projection cumul + plafond de l'étape + attendu des étapes restantes ; ordre de sacrifice (1) fusions,
    (2) M6 réduite à 4 fiches, (3) table seule de l'axe 7, (4) passe « tableau » ; arrêt d'étape = plus aucune étape
    sacrifiable au-delà ; les lectures d'étiquettes sont protégées, comme le texte le dit) ; la lecture grossière de la v4
    (« total > plafond ») est gardée en rappel ;
  - CP4-07 : la porte entière est calculée à deux plafonds, 45 USD (arrêt d'étape 40) et 32 USD (arrêt d'étape 28), et
    sans arrêt d'étape (sensibilité) ; un seul plafond entre dans la lecture principale (45, À REMPLIR par Lazar) ;
  - CP4-10 : le coût du complément (24 fonds rendus une fois) est calculé poste par poste aux bases du devis v3 et
    retranché du reste de la course dans la lecture de C10 du chemin « après complément » ;
  - CP4-03 (décision D-i) : trois variantes du plan des fonds sont chiffrées — (1) 28 fonds uniques (lecture principale,
    inchangée), (2) 28 fonds + 4 rendus appariés supplémentaires pour la seule mémoire anti-redite, (3) 24 fonds dont
    4 doublés — effet sur M1, C6, le coût et la porte ;
  - CP4-01 (décision D-g) : coût de 4 fiches d'antériorité non citée ajoutées à M6 (option (b)) et borne de leur rappel ;
  - CP4-06 : nombre de paires dans le profil du bras méta sous des hypothèses déclarées (SUPPOSÉ) ;
  - CP4-11 : décomposition de C10 (lecture v3 : k = 2, reste 78 ; k = 1 ; reste = 110 − dépense) imprimée.
Graines : les simulations gardées de la v4 gardent leurs noms de tâche « v4-… » (mêmes tirages : seuls les changements
déclarés bougent les chiffres) ; les simulations nouvelles portent des noms « v5-… ». SeedSequence(RACINE,
spawn_key=(cle_de_tache(nom),)), même dérivation que src/controle_ia/manifeste.py (R9).
Hypothèses déclarées dans le préenregistrement (brouillon 5) ; valeurs supposées marquées SUPPOSÉ.
Seuils paramétrés en tête : si Lazar gèle d'autres valeurs, changer SEUILS et rejouer ; la sortie fait foi.
Sortie : texte sur la sortie standard."""
import hashlib
import platform
import sys

import numpy as np
import scipy
from scipy import stats

RACINE = 20261031  # entropie racine du calcul de puissance (distincte de celle du run, 20261101)
SEUILS = dict(S1=0.80, S2=0.70, S3=0.70, S4_fleiss=0.45, S4_couple=0.35, S4_plancher=0.30,
              S10_min_sur_12=11, S10_bande=0.75, S11_ord=0.10, S12=0.10, S13=0.90, S14=0.70, S15=0.10,
              S17_arret=40.0, S17_plafond=45.0,
              S18_max_auc=0.70, S18_min_kimi=6, S19_max_auc=0.65, S20_ambigus=4, S20_P=8, S20_N=10,
              S8=0.80, S9_rappel=0.75, refut_ii=0.10)
N_SIM = 20000
PLAFOND = SEUILS["S17_plafond"]
ARRET = SEUILS["S17_arret"]


def cle_de_tache(nom):
    return int.from_bytes(hashlib.sha256(nom.encode("utf-8")).digest()[:8], "big")


def rng(nom):
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=(cle_de_tache(nom),)))


print(f"python {platform.python_version()} ; numpy {np.__version__} ; scipy {scipy.__version__} ; racine {RACINE} ; "
      f"tirages {N_SIM}")
print("seuils utilisés :", ", ".join(f"{k}={v}" for k, v in SEUILS.items()))

# ================================================================ Mesure 1, simulation jointe des trois juges
# Plan principal (variante (1), lecture de l'auteur du brouillon 4, D-i) : 28 fonds rendus une fois chacun
# -> P 10 fiches, N 13, C 3, G 2. Un juge de justesse vraie v a raison sur une fiche avec probabilité v, indépendamment
# d'une fiche à l'autre. Juges indépendants entre eux à fiches données (SUPPOSÉ ; une difficulté commune par fiche
# rendrait la porte M1 plus probable et le kappa plus haut). Rejet des C (hors consigne) : 0,30 par fiche et par juge (P2).
# La fonction justesse garde la forme de la v3 (fonds appariés à corrélation rho) : variante (3) de D-i et rappel v3.
RHO = 0.6
REJET_C = 0.30
PLAN = ((0, 10), (0, 13))            # (P appariés, P simples), (N appariés, N simples) — variante (1), principale
PLAN_COMPL = ((0, 12), (0, 12))      # complément : 24 fonds rendus une fois (P 12, N 12)
PLAN_V3 = ((4, 2), (5, 3))           # rappel : plan apparié de la v3 (comparaison seulement)
PLAN_VAR3 = ((2, 7), (2, 9))         # variante (3) de D-i : 24 fonds dont 4 doublés (2 P, 2 N) -> P 11 fiches, N 13


def justesse(g, n, v, n_app, n_simple, rho=RHO):
    a = g.random((n, n_app)) < v
    b = np.where(g.random((n, n_app)) < rho, a, g.random((n, n_app)) < v)
    c = g.random((n, n_simple)) < v
    return np.concatenate([a, b, c], axis=1)


def juge(g, n, v, plan=PLAN, n_c=3):
    (pa, ps), (na, ns) = plan
    jp = justesse(g, n, v, pa, ps)          # P : juste = « notable »
    jn = justesse(g, n, v, na, ns)          # N : juste = « non notable »
    rc = g.random((n, n_c)) < REJET_C       # C : rejet hors consigne
    return jp, jn, rc


def issue_vec(jp, jn, s1):
    rp, sp = jp.mean(1), jn.mean(1)
    ba = (rp + sp) / 2
    et = (ba >= s1 - 1e-12) & (rp >= SEUILS["S2"] - 1e-12)
    de = ba < SEUILS["S3"] - 1e-12
    return np.where(et, 2, np.where(de, 0, 1)), ba, sp   # 2 étalonné, 1 non concluant, 0 défaillant


def fleiss(notables):            # notables : (n, fiches, 3) booléens
    k = notables.shape[2]
    oui = notables.sum(2)
    pi = (oui * (oui - 1) + (k - oui) * (k - oui - 1)) / (k * (k - 1))
    pbar = pi.mean(1)
    p = oui.mean(1) / k
    pe = p ** 2 + (1 - p) ** 2
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(pe < 1, (pbar - pe) / (1 - pe), 1.0)


def cohen(a, b):
    po = (a == b).mean(1)
    pa, pb = a.mean(1), b.mean(1)
    pe = pa * pb + (1 - pa) * (1 - pb)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(pe < 1, (po - pe) / (1 - pe), 1.0)


def m1_joint(g, n, v_opus, v_argon, v_kimi, s1=None, s1_kimi=None, plan=PLAN):
    """Renvoie les états de C1, C2, C3 (accord et réfutation d'ensemble (ii)) et les déclencheurs d'audit de M1."""
    s1 = SEUILS["S1"] if s1 is None else s1
    jug = {"opus": juge(g, n, v_opus, plan), "argon": juge(g, n, v_argon, plan), "kimi": juge(g, n, v_kimi, plan)}
    return jug, s1, (s1 if s1_kimi is None else s1_kimi)


def lire_m1(jug, s1, s1_kimi):
    iss, bas, sps = {}, {}, {}
    for nom, (jp, jn, rc) in jug.items():
        iss[nom], bas[nom], sps[nom] = issue_vec(jp, jn, s1_kimi if nom == "kimi" else s1)
    notables = np.stack([np.concatenate([jug[j][0], ~jug[j][1]], axis=1) for j in ("opus", "argon", "kimi")], axis=2)
    fk = fleiss(notables)
    ck = [cohen(notables[:, :, a], notables[:, :, b]) for a, b in ((0, 1), (0, 2), (1, 2))]
    confirme = (fk >= SEUILS["S4_fleiss"]) & np.all([c >= SEUILS["S4_couple"] for c in ck], axis=0)
    refute = fk < SEUILS["S4_plancher"]
    # réfutation d'ensemble (ii) : rejet des C >= spécificité sur N − 0,10 chez les trois juges
    ref_ii = np.all([jug[j][2].mean(1) >= sps[j] - SEUILS["refut_ii"] for j in jug], axis=0)
    c1 = (iss["kimi"] == 2) & (iss["argon"] == 2)
    c1_defaillant = (iss["kimi"] == 0) | (iss["argon"] == 0)
    c2 = iss["opus"] != 0
    c3 = (~refute) & (~ref_ii)
    # déclencheurs d'audit tirés de M1 (R4) : trop propre / trop sale
    trop_propre = np.any([bas[j] >= 0.97 for j in jug], axis=0) | (fk >= 0.90)
    constant = np.any([np.all(notables[:, :, i], axis=1) | np.all(~notables[:, :, i], axis=1) for i in range(3)], axis=0)
    trop_sale = np.any([bas[j] <= 0.55 for j in jug], axis=0) | (fk < 0) | constant
    return dict(c1=c1, c1_def=c1_defaillant, c2=c2, c3=c3, confirme=confirme, iss=iss,
                audit_m1=trop_propre | trop_sale, propre=trop_propre, sale=trop_sale)


def cumul(j1, j2):
    return tuple(np.concatenate([a, b], axis=1) for a, b in zip(j1, j2))


print("\n== M1, un juge seul : 28 fonds rendus une fois (P 10, N 13), sans appariement (variante (1) de D-i) ==")
for v in (0.90, 0.85, 0.80, 0.75, 0.70, 0.60):
    g = rng(f"v4-m1-juge-{v}")
    jp, jn, _ = juge(g, N_SIM, v)
    a = issue_vec(jp, jn, SEUILS["S1"])[0]
    jp8, jn8, _ = juge(g, N_SIM, v, plan=((0, 8), (0, 10)))
    a8 = issue_vec(jp8, jn8, SEUILS["S1"])[0]
    jpc, jnc, _ = juge(g, N_SIM, v, plan=PLAN_COMPL)
    ac = issue_vec(np.concatenate([jp, jpc], 1), np.concatenate([jn, jnc], 1), SEUILS["S1"])[0]
    jpv, jnv, _ = juge(g, N_SIM, v, plan=PLAN_V3)
    av = issue_vec(jpv, jnv, SEUILS["S1"])[0]
    g3 = rng(f"v5-m1-juge-var3-{v}")
    jp3, jn3, _ = juge(g3, N_SIM, v, plan=PLAN_VAR3)
    a3 = issue_vec(jp3, jn3, SEUILS["S1"])[0]
    print(f"  juge vrai à {v:.2f} : étalonné {np.mean(a == 2):.2f}, défaillant {np.mean(a == 0):.2f} ; "
          f"après exclusion d'ambigus (P 8, N 10) : étalonné {np.mean(a8 == 2):.2f} ; "
          f"étalonné au total après complément (P 22, N 25) {np.mean((a == 2) | ((a == 1) & (ac == 2))):.2f} ; "
          f"rappel v3 (plan apparié 18 fonds, rho 0,6) : étalonné {np.mean(av == 2):.2f} ; "
          f"variante (3) de D-i (24 fonds dont 4 doublés, P 11, N 13, rho 0,6) : étalonné {np.mean(a3 == 2):.2f}")

print("\n== M1, simulation jointe (porte des juges C1-C2 seule) ==")
CAS_JUGES = [("prédiction P1 (Opus 0,90 ; Argon 0,85 ; Kimi 0,80)", 0.90, 0.85, 0.80),
             ("tous à 0,90", 0.90, 0.90, 0.90), ("tous à 0,85", 0.85, 0.85, 0.85),
             ("tous à 0,80", 0.80, 0.80, 0.80), ("Kimi 0,70, autres 0,90", 0.90, 0.90, 0.70)]
M1 = {}
for nom, vo, va, vk in CAS_JUGES:
    g = rng(f"v4-m1-{nom}")
    jug, s1, s1k = m1_joint(g, N_SIM, vo, va, vk)
    r = lire_m1(jug, s1, s1k)
    # complément : seul C1 en défaut par « non concluant » (aucun défaillant), Opus non défaillant, C3 tenue
    besoin = (~r["c1"]) & (~r["c1_def"]) & r["c2"] & r["c3"]
    jug2, _, _ = m1_joint(g, N_SIM, vo, va, vk, plan=PLAN_COMPL)
    jc = {j: cumul(jug[j], jug2[j]) for j in jug}
    rc = lire_m1(jc, s1, s1k)
    ok_cumul = rc["c1"] & rc["c2"] & rc["c3"]
    M1[nom] = dict(m1=r["c1"] & r["c2"] & r["c3"], c1c2=r["c1"] & r["c2"], c1=r["c1"], c2=r["c2"], c3=r["c3"],
                   besoin=besoin, ok_cumul=ok_cumul, audit=r["audit_m1"], propre=r["propre"], sale=r["sale"],
                   confirme=r["confirme"])
    print(f"  {nom} : C1-C2 (porte des juges) {np.mean(r['c1'] & r['c2']):.2f} ; C3 accord non réfuté et "
          f"(ii) non atteinte {np.mean(r['c3']):.3f} (accord « confirmé » {np.mean(r['confirme']):.2f}) ; "
          f"C1-C3 {np.mean(M1[nom]['m1']):.2f} ; complément proposable (si le reste tient) {np.mean(besoin):.2f} ; "
          f"puis C1-C3 sur le cumul {np.mean(ok_cumul[besoin]) if besoin.any() else 0:.2f} ; "
          f"audit R4 déclenché par M1 {np.mean(r['audit_m1']):.2f} (trop propre {np.mean(r['propre']):.2f}, "
          f"trop sale {np.mean(r['sale']):.2f})")

# Variante (3) de D-i, simulation jointe à la prédiction P1 (nouvelle graine v5)
g = rng("v5-m1-var3-P1")
jug3, s1, s1k = m1_joint(g, N_SIM, 0.90, 0.85, 0.80, plan=PLAN_VAR3)
r3 = lire_m1(jug3, s1, s1k)
besoin3 = (~r3["c1"]) & (~r3["c1_def"]) & r3["c2"] & r3["c3"]
M1_VAR3 = dict(m1=r3["c1"] & r3["c2"] & r3["c3"], c1c2=r3["c1"] & r3["c2"], besoin=besoin3, audit=r3["audit_m1"])
print(f"  variante (3) de D-i, prédiction P1 (24 fonds dont 4 doublés, 8 fiches corrélées à rho 0,6) : C1-C2 "
      f"{np.mean(M1_VAR3['c1c2']):.2f} ; C1-C3 {np.mean(M1_VAR3['m1']):.2f} ; complément proposable {np.mean(besoin3):.2f} ; "
      f"audit M1 {np.mean(r3['audit_m1']):.2f}")

# Relâchement nommé R-1 (option du nœud, CP2-02) : S1 de 0,80 à 0,75, même lecture.
print("\n== Option nommée R-1 du nœud : S1 relâché à 0,75 (S2, S3 inchangés), prédiction P1 ==")
g = rng("v4-m1-relache-R1")
jug, _, _ = m1_joint(g, N_SIM, 0.90, 0.85, 0.80)
r = lire_m1(jug, 0.75, 0.75)
print(f"  C1-C2 {np.mean(r['c1'] & r['c2']):.2f} ; C1-C3 {np.mean(r['c1'] & r['c2'] & r['c3']):.2f} "
      f"(à comparer à la ligne « prédiction P1 » ci-dessus)")
for v in (0.80, 0.75, 0.70):
    g = rng(f"v4-m1-relache-R1-juge-{v}")
    jp, jn, _ = juge(g, N_SIM, v)
    a = issue_vec(jp, jn, 0.80)[0]
    b = issue_vec(jp, jn, 0.75)[0]
    print(f"  un juge vrai à {v:.2f} : étalonné {np.mean(a == 2):.2f} sous S1 = 0,80 ; {np.mean(b == 2):.2f} sous 0,75")

# ================================================================ Autres conditions de la porte
print("\n== Probabilité de chaque autre condition aux valeurs prédites (hypothèse écrite à droite) ==")
P = {}

# C4 : étage 1, programme éprouvé en É0 sur cas sain et artefact.
P["C4"] = 0.97
print(f"  C4 étage 1 conforme : {P['C4']:.2f} (SUPPOSÉ : programme éprouvé en É0 ; 100 % des G et 0 % des P, N, C)")

# C5 : S18, S19, S20 par version de témoins ; au plus deux versions en tout (A6 et A7 partagent ce compte).
g = rng("v4-c5")
auc18 = g.normal(0.62, 0.09, (N_SIM, 2))   # P12 : aire prédite 0,62 ; erreur-type Hanley-McNeil 0,09 (sortie v2)
auc19 = g.normal(0.55, 0.12, (N_SIM, 2))   # P12 : 0,55 ; erreur-type 0,12
AMBIG = 0.10                                # SUPPOSÉ : part de témoins jugés ambigus par le relecteur
amb_p = g.random((N_SIM, 2, 10)) < AMBIG
amb_n = g.random((N_SIM, 2, 13)) < AMBIG
s20 = ((amb_p.sum(2) + amb_n.sum(2)) <= SEUILS["S20_ambigus"]) & ((10 - amb_p.sum(2)) >= SEUILS["S20_P"]) & \
      ((13 - amb_n.sum(2)) >= SEUILS["S20_N"])
ok_v = (auc18 <= SEUILS["S18_max_auc"]) & (auc19 <= SEUILS["S19_max_auc"]) & s20
P["C5"] = np.mean(ok_v[:, 0] | ok_v[:, 1])
print(f"  C5 contrôles avant juges : par version {np.mean(ok_v[:, 0]):.2f} (S18 {np.mean(auc18[:, 0] <= 0.70):.2f}, "
      f"S19 {np.mean(auc19[:, 0] <= 0.65):.2f}, S20 {np.mean(s20[:, 0]):.2f}) ; en deux versions {P['C5']:.2f} "
      f"(aire normale autour de la prédiction P12 ; ambiguïté {AMBIG:.2f} par témoin, SUPPOSÉ)")
fp19 = 1 - stats.norm.cdf((0.65 - 0.5) / 0.12)
print(f"    garde S19 à aire vraie 0,50 : dépassée {fp19:.2f} par version, {fp19 ** 2:.3f} sur deux versions "
      f"(faux positif de garde accepté, CP2-12)")
amb0 = (1 - AMBIG) ** 23
print(f"    accord de 100 % du relecteur (déclencheur « trop propre ») : {amb0:.2f}")

# C6 : mémoire (rappel global sur les positifs de vérification) et union de l'axe 7 (12 paraphrases) non défaillantes.
# Variante (1) : PB 18 seules -> ≈ 9 positifs en vérification ; variantes (2) et (3) : + 4 paires PA -> ≈ 2 de plus.
ax7_def = stats.binom.cdf(5, 12, 0.75)          # rappel < 0,50 sur 12 <=> au plus 5
fa_def = 1 - stats.binom.cdf(int(np.floor(250 * 0.20)), 250, 0.06)


def c6(n_pos):
    seuil = int(np.ceil(0.60 * n_pos)) - 1        # rappel < 0,60 <=> vus <= seuil
    return (1 - stats.binom.cdf(seuil, n_pos, 0.85)) * (1 - ax7_def) * (1 - fa_def)


P["C6"] = c6(9)
P["C6_var23"] = c6(11)
print(f"  C6 mémoire et axe 7 non défaillantes : {P['C6']:.3f} (P6 : rappel 0,85 sur ≈ 9 positifs de vérification "
      f"(PB seules, variante (1)), fausses alertes 0,06 sur 250 ; P7 : union 0,75 sur 12)")
print(f"    variantes (2) et (3) de D-i (≈ 11 positifs : PB ≈ 9 + PA ≈ 2) : {P['C6_var23']:.3f} ; "
      f"rappel v3 (≈ 14 positifs, 10 PA) : {c6(14):.3f}")
print("    déclencheur R4 « trop propre » de M3 (rappel 9 sur 9 ET zéro fausse alerte sur ≈ 250 NA et 4 NB) aux valeurs "
      f"prédites : {0.85 ** 9 * (1 - 0.06) ** 254:.4f} (rappel seul 9 sur 9 : {0.85 ** 9:.2f})")

# C7 : aiguilleur. P8 : rappel 0,92, plus faible en C4 (0,80) => C1-C3 à 0,96 (SUPPOSÉ, partage).


def m4(g, n, rappels):
    vus = np.stack([g.random((n, 3)) < r for r in rappels], axis=1)       # (n, 4 classes, 3)
    oublis = 3 - vus.sum(2)
    tot = vus.sum((1, 2))
    o12 = oublis[:, 0] + oublis[:, 1]
    et_direct = (o12 == 0) & (tot >= SEUILS["S10_min_sur_12"])
    defa = (o12 >= 2) | (tot < SEUILS["S10_bande"] * 12 - 1e-9)
    a_corr = ~et_direct & ~defa
    # nouvel essai : 3 témoins neufs par classe en défaut (classe avec au moins un oubli), lu sur eux seuls
    neuf = np.stack([g.random((n, 3)) < r for r in rappels], axis=1).all(2)  # (n, 4) : 3 sur 3 vus
    en_defaut = oublis > 0
    essai_ok = np.all(~en_defaut | neuf, axis=1)
    return et_direct, a_corr, defa, et_direct | (a_corr & essai_ok), tot


g = rng("v4-c7")
d, a, f, et, tot7 = m4(g, N_SIM, (0.96, 0.96, 0.96, 0.80))
P["C7"] = np.mean(et)
print(f"  C7 aiguilleur étalonné : direct {np.mean(d):.2f}, à corriger {np.mean(a):.2f}, défaillant {np.mean(f):.2f} ; "
      f"étalonné après nouvel essai {P['C7']:.2f} (P8 : 0,96 en C1-C3, 0,80 en C4, SUPPOSÉ ; concrets écrits)")
d2, a2, f2, et2, _ = m4(g, N_SIM, (0.92, 0.92, 0.92, 0.92))
print(f"    sensibilité, 0,92 dans chaque classe : direct {np.mean(d2):.2f} ; après nouvel essai {np.mean(et2):.2f} ; "
      f"un nouvel essai d'une classe à 0,92 passe {0.92 ** 3:.2f}")
fa40 = stats.binom.pmf(0, 34, 0.03) * stats.binom.pmf(0, 6, 0.20)
print(f"    déclencheur R4 « trop propre » de M4, part aiguilleur (12 sur 12 ET zéro fausse alerte sur 34 + 6 difficiles) "
      f"aux valeurs prédites : {np.mean(tot7 == 12) * fa40:.3f} (12 sur 12 : {np.mean(tot7 == 12):.2f} ; zéro fausse alerte "
      f"sur 40 : {fa40:.2f}) ; la condition « accord de 100 % entre aiguilleur et second lecteur sur la passe 1 » s'y ajoute (C8)")
print("    défaut R-819 (aucun concret écrit) : C7 « non étalonné » avec certitude : porte fermée (probabilité 0)")

# C8 : débordement de Kimi, 20 fiches. Union, intersection, adjudication par un troisième lecteur isolé.
g = rng("v4-c8")
TAUX, SENS, FA = 0.05, 0.90, 0.03     # P9 ; sensibilité de chaque lecteur SUPPOSÉ ; fausses alertes (P8) SUPPOSÉ égales
vrai = g.random((N_SIM, 20)) < TAUX
lect = [np.where(vrai, g.random((N_SIM, 20)) < SENS, g.random((N_SIM, 20)) < FA) for _ in range(3)]
union = (lect[0] | lect[1]).mean(1)
inter = (lect[0] & lect[1]).mean(1)
major = ((lect[0].astype(int) + lect[1] + lect[2]) >= 2).mean(1)
conf = union <= SEUILS["S12"] + 1e-9
depas = inter > SEUILS["S12"] + 1e-9
adj = ~conf & ~depas
c8 = conf | (adj & (major <= SEUILS["S12"] + 1e-9))
P["C8"] = np.mean(c8)
accord100 = np.mean((lect[0] == lect[1]).all(1))
propre_m4 = np.mean(tot7 == 12) * fa40 * accord100
print(f"    accord de 100 % entre les deux lecteurs sur 20 fiches : {accord100:.2f} ; déclencheur « trop propre » de M4 "
      f"complet (12 sur 12, zéro fausse alerte sur 40, accord 100 %) : {propre_m4:.4f}")
print(f"  C8 Kimi proposeur conforme : {P['C8']:.2f} — union <= S12 {np.mean(conf):.2f} ; intersection > S12 "
      f"{np.mean(depas):.2f} ; adjudication {np.mean(adj):.2f}, dont conforme à la majorité "
      f"{np.mean(major[adj] <= 0.10) if adj.any() else 0:.2f} (P9 : taux 0,05 ; sensibilité 0,90 et fausses alertes "
      f"0,03 par lecteur, SUPPOSÉ)")
for t in (0.10, 0.20):
    vr = g.random((N_SIM, 20)) < t
    le = [np.where(vr, g.random((N_SIM, 20)) < SENS, g.random((N_SIM, 20)) < FA) for _ in range(3)]
    u = (le[0] | le[1]).mean(1); i_ = (le[0] & le[1]).mean(1)
    mj = ((le[0].astype(int) + le[1] + le[2]) >= 2).mean(1)
    ok = (u <= 0.10) | (~(u <= 0.10) & ~(i_ > 0.10) & (mj <= 0.10))
    print(f"    taux vrai {t:.2f} : déclaré conforme {np.mean(ok):.2f}")

# C9 : antériorité non défaillante (inventées < 0,70 sur 9 <=> au plus 6 vues).
P["C9"] = 1 - stats.binom.cdf(6, 9, 0.95)
m6_et = (1 - stats.binom.cdf(8, 9, 0.95)) * (1 - stats.binom.cdf(6, 9, 0.70)) * stats.binom.cdf(2, 22, 0.08)
m6_propre = 0.95 ** 9 * 0.70 ** 9 * (1 - 0.08) ** 22
print(f"  C9 antériorité non défaillante : {P['C9']:.3f} (P10 : inventées 0,95) ; M6 « étalonnée » {m6_et:.2f} "
      f"(C9 accepte « non concluant ») ; déclencheur R4 « trop propre » de M6 (9 sur 9, 9 sur 9, 0 sur 22) : {m6_propre:.4f}")
# D-g, option (b) : 4 fiches d'antériorité non citée (M6b) ; borne basse du rappel à 95 % si 4 sur 4 ; 3 sur 4
print(f"    D-g option (b), M6b (4 fiches d'antériorité non citée) : 4 sur 4 vues ne bornent le rappel qu'à "
      f"{0.05 ** 0.25:.2f} (unilatérale 95 %) ; à rappel vrai 0,75, « 3 sur 4 au moins » se voit avec "
      f"{1 - stats.binom.cdf(2, 4, 0.75):.2f}, à 0,50 avec {1 - stats.binom.cdf(2, 4, 0.50):.2f} : garde grossière, réserve")

# ================================================================ Coûts : rapports mesuré ÷ supposé (P11), log-normaux


def lognorm(g, n, med, lo, hi):
    return med * np.exp(g.normal(0, (np.log(hi) - np.log(lo)) / (2 * 1.2816), n))


g = rng("v4-couts")
r_kj = lognorm(g, N_SIM, 1.4, 0.8, 3.0)
r_ar = lognorm(g, N_SIM, 1.0, 0.7, 1.5)
r_op = lognorm(g, N_SIM, 1.0, 0.8, 1.4)
r_an = lognorm(g, N_SIM, 1.2, 0.6, 3.0)
r_ai = lognorm(g, N_SIM, 1.0, 0.5, 2.0)
r_kp = lognorm(g, N_SIM, 1.2, 0.6, 3.8)
r_fu = lognorm(g, N_SIM, 1.3, 0.5, 3.0)
r_re = lognorm(g, N_SIM, 1.0, 0.7, 1.5)          # rédacteur, relecteur : SUPPOSÉ comme Argon
# tirage de la seconde version de témoins : même place dans la séquence de tirages que dans la v4
v2_ind = (g.random(N_SIM) < 1 - np.mean(ok_v[:, 0])).astype(float)

# Bases du tableau de coût (devis v3 § 1, SUPPOSÉ) : 28 fonds rendus une fois (9 Kimi, 9 Argon, 10 T, SUPPOSÉ).
REDACTEUR_E1, REDACTEUR_E8, RENDUS_K, RENDUS_A, RENDUS_T = 2.6, 0.6, 9, 9, 10
rendus_base = RENDUS_K * 0.057 + (RENDUS_A + RENDUS_T) * 0.079
rendus = RENDUS_K * 0.057 * r_kj + (RENDUS_A + RENDUS_T) * 0.079 * r_ar
juge3 = 0.114 * r_op + 0.079 * r_ar + 0.057 * r_kj          # trois juges sur une fiche
JUGE3_BASE = 0.114 + 0.079 + 0.057
un = np.ones(N_SIM)


ORDRE_A = ["É1", "É2", "É3", "É4", "É5", "É5bis", "É6a", "É6b", "É6c", "É7", "É7b", "É8", "É9"]   # ordre du brouillon 4
ORDRE_B = ["É1", "É2", "É3", "É4", "É5", "É5bis", "É7", "É6b", "É6c", "É6a", "É7b", "É8", "É9"]   # brouillon 5 : juges avant les sacrifiables


def etapes_pre_pilote(delta_e1=0.0, delta_e3_base=0.0, delta_e3=None, delta_e4_base=0.0, delta_e4=None, ordre=None):
    """Étapes du pré-pilote : (nom, coût simulé, plafond de relais, attendu aux bases, rôle), dans l'ordre demandé.
    rôle : 'prot' = protégée (jamais sacrifiée) ; 'sacr1'..'sacr4' = ordre de sacrifice d'A1 (sacr2 = M6 réduite)."""
    d3 = 0 * un if delta_e3 is None else delta_e3
    d4 = 0 * un if delta_e4 is None else delta_e4
    ordre = ORDRE_B if ordre is None else ordre
    liste = [
        ("É1 rédacteur", (REDACTEUR_E1 + delta_e1) * r_re, 3.3 + 1.25 * delta_e1, REDACTEUR_E1 + delta_e1, "prot"),
        ("É2 Kimi passe 1", 2.0 * r_kp, 3.0, 2.0, "prot"),
        ("É3 rendus", rendus + d3, 2.8 + 1.4 * delta_e3_base, rendus_base + delta_e3_base, "prot"),
        ("É4 aiguilleur 56 lectures, second lecteur 10, adjudicateur, nouvel essai",
         (66 * 0.057 + 0.05 + 0.3) * r_ai + d4, 5.5 + 1.4 * delta_e4_base, 66 * 0.057 + 0.35 + delta_e4_base, "prot"),
        ("É5 relecteur", 1.4 * r_re, 1.9, 1.4, "prot"),
        ("É5bis seconde version de témoins (si C5 échoue en v1)", v2_ind * (1.5 * r_re + rendus + 1.4 * r_re),
         v2_ind * 6.6, v2_ind * (1.5 + rendus_base + 1.4), "prot"),
        ("É6a passe « tableau » de Kimi, aiguilleur et second lecteur sur elle", 2.0 * r_kp + 20 * 0.057 * r_ai,
         4.6, 2.0 + 20 * 0.057, "sacr4"),
        ("É6b lectures d'étiquettes (trois lectures, deux lecteurs)", 0.75 * r_op, 1.0, 0.75, "prot"),
        ("É6c fusions (3), aiguilleur et trois juges sur elles", 1.2 * r_fu + 3 * 0.057 * r_ai + 3 * juge3,
         3.5, 1.2 + 3 * 0.057 + 3 * JUGE3_BASE, "sacr1"),
        ("É7 trois juges sur les 28 rendus", 28 * juge3, 11.6, 28 * JUGE3_BASE, "prot"),
        ("É7b Opus, table seule de l'axe 7", 0.7 * r_op, 1.0, 0.7, "sacr3"),
        ("É8 paraphrases (rédacteur)", REDACTEUR_E8 * r_re, 0.7, REDACTEUR_E8, "prot"),
        ("É9 antériorité, 8 fiches (réduite : 4 fiches)", 2.0 * r_an, 6.0, 2.0, "sacr2"),
    ]
    cle = {e[0].split()[0]: e for e in liste}
    return [cle[k] for k in ordre]


def simuler_budget(etapes, plafond, arret):
    """Règle d'A1 étape par étape (brouillon 5). Avant chaque étape E non retirée :
    projection = cumul + plafond(E) + attendu aux bases des étapes restantes non retirées ;
    tant que projection > plafond, retirer la prochaine étape sacrifiable non jouée dans l'ordre (1) fusions,
    (2) M6 réduite à 4 fiches (coût, plafond et attendu divisés par deux ; elle devient protégée), (3) table seule,
    (4) passe « tableau » ; puis : si cumul >= arrêt d'étape, toute étape sacrifiable restante est retirée (les
    protégées continuent) ; si cumul + plafond(E) > plafond : E sacrifiable -> retirée ; E protégée -> non lancée,
    « non mesuré (budget) » ; sinon E est jouée et son coût s'ajoute au cumul."""
    n = N_SIM
    noms = [e[0] for e in etapes]
    cout = [e[1] * un for e in etapes]
    plaf = [e[2] * un for e in etapes]
    att = [e[3] * un for e in etapes]
    role = [e[4] for e in etapes]
    retire = [np.zeros(n, bool) for _ in etapes]
    joue = [np.zeros(n, bool) for _ in etapes]
    reduit = np.zeros(n, bool)
    cum = np.zeros(n)
    non_lancee = np.zeros(n, bool)
    ordre = [role.index("sacr1"), role.index("sacr2"), role.index("sacr3"), role.index("sacr4")]
    for i in range(len(etapes)):
        actif = ~retire[i]
        for _ in range(2):      # deux passes : la réduction de M6 peut suffire avant un retrait suivant
            reste = sum(np.where(retire[j], 0, att[j]) for j in range(i + 1, len(etapes)))
            proj = cum + plaf[i] + reste
            for k in ordre:
                besoin = actif & (proj > plafond) & ~retire[k] & ~joue[k]
                if role[k] == "sacr2":
                    m_red = besoin & ~reduit
                    reduit |= m_red
                    cout[k] = np.where(m_red, cout[k] / 2, cout[k]); plaf[k] = np.where(m_red, plaf[k] / 2, plaf[k])
                    att[k] = np.where(m_red, att[k] / 2, att[k])
                else:
                    retire[k] |= besoin
                reste = sum(np.where(retire[j], 0, att[j]) for j in range(i + 1, len(etapes)))
                proj = cum + plaf[i] + reste
        actif = ~retire[i]
        # arrêt d'étape : plus aucune étape sacrifiable
        if role[i].startswith("sacr"):
            retire[i] |= actif & (cum >= arret)
            actif = ~retire[i]
        tient = cum + plaf[i] <= plafond + 1e-9
        if role[i].startswith("sacr"):
            retire[i] |= actif & ~tient
        else:
            non_lancee |= actif & ~tient
        lance = actif & tient
        joue[i] |= lance
        cum = cum + np.where(lance, cout[i], 0)
    sacrifie = np.any([retire[k] for k in ordre], axis=0) | reduit
    ret = {noms[k].split()[0]: retire[k] for k in range(len(etapes))}
    return dict(depense=cum, non_lancee=non_lancee, sacrifie=sacrifie, retire=ret, reduit=reduit, noms=noms,
                arret_touche=cum >= arret)


print("\n== Budget du pré-pilote selon la règle d'A1, étape par étape (CP4-15 ; rapports P11 ; seconde version comprise) ==")
ETAPES = etapes_pre_pilote()
prot_base = sum(e[3] for e in ETAPES if e[4] == "prot" and not e[0].startswith("É5bis"))
sacr_base = sum(e[3] for e in ETAPES if e[4] != "prot")
print(f"  aux bases (rapports à 1) : protégé {prot_base:.1f} USD ; sacrifiable {sacr_base:.1f} USD ; total attendu "
      f"{prot_base + sacr_base:.1f} ; somme des plafonds de relais {sum(e[2] for e in ETAPES if not e[0].startswith('É5bis')):.1f} ; "
      f"seconde version de témoins ≈ {1.5 + rendus_base + 1.4:.1f} USD si C5 échoue en première version "
      f"(probabilité {1 - np.mean(ok_v[:, 0]):.2f})")
total_brut = sum(e[1] for e in ETAPES)
BUDGETS = {}
ETAPES_A = etapes_pre_pilote(ordre=ORDRE_A)
for (pl, ar, etiquette, et) in ((45.0, 40.0, "plafond 45, arrêt d'étape 40, ordre B du brouillon 5 (lecture principale, S17 recommandé)", ETAPES),
                                (45.0, 40.0, "plafond 45, arrêt d'étape 40, ordre A du brouillon 4 (juges après les sacrifiables ; comparaison)", ETAPES_A),
                                (32.0, 28.0, "plafond 32, arrêt d'étape 28, ordre B (GO-2026-10-30-07 tel quel ; information)", ETAPES),
                                (45.0, 45.0, "plafond 45 sans arrêt d'étape, ordre B (sensibilité)", ETAPES)):
    b = simuler_budget(et, pl, ar)
    if (pl, ar) not in BUDGETS:
        BUDGETS[(pl, ar)] = b
    print(f"  {etiquette} : dépense médiane {np.median(b['depense']):.1f} USD, quantile 90 % "
          f"{np.quantile(b['depense'], 0.9):.1f} ; P(un sacrifice ou une réduction au moins) {np.mean(b['sacrifie']):.2f} "
          f"(fusions retirées {np.mean(b['retire']['É6c']):.2f} ; M6 réduite {np.mean(b['reduit']):.2f} ; table seule retirée "
          f"{np.mean(b['retire']['É7b']):.2f} ; passe « tableau » retirée {np.mean(b['retire']['É6a']):.2f}) ; "
          f"P(arrêt d'étape touché) {np.mean(b['arret_touche']):.2f} ; "
          f"P(étape protégée non lancée, « non mesuré (budget) ») {np.mean(b['non_lancee']):.3f}")
print(f"  rappel du modèle grossier de la v4 (total sans sacrifice > plafond ; protégé > plafond) : à 45 : "
      f"{np.mean(total_brut > 45):.2f} / {np.mean(sum(e[1] for e in ETAPES if e[4] == 'prot') > 45):.3f} ; à 32 : "
      f"{np.mean(total_brut > 32):.2f} / {np.mean(sum(e[1] for e in ETAPES if e[4] == 'prot') > 32):.3f} ; "
      f"dépense médiane sans plafond {np.median(total_brut):.1f}")
B = BUDGETS[(45.0, 40.0)]
P["C13_budget"] = 1 - np.mean(B["non_lancee"])
depense = B["depense"]
B32 = BUDGETS[(32.0, 28.0)]
P["C13_budget_32"] = 1 - np.mean(B32["non_lancee"])

# Complément (CP4-10) : 24 fonds rendus une fois (P 12, N 12), poste par poste aux bases du devis v3.
COMPL_BASE = dict(redacteur=24 * 0.06, rendus=8 * 0.057 + 16 * 0.079, relecteur=24 / 30 * 1.4, aiguilleur=24 * 0.057,
                  juges=24 * JUGE3_BASE)
compl_cout = (24 * 0.06 * r_re + (8 * 0.057 * r_kj + 16 * 0.079 * r_ar) + 24 / 30 * 1.4 * r_re + 24 * 0.057 * r_ai
              + 24 * juge3)
RATIOS_PLAFOND = dict(redacteur=1.25, rendus=1.4, relecteur=1.36, aiguilleur=1.4, juges=1.64)
compl_plafond = sum(COMPL_BASE[k] * RATIOS_PLAFOND[k] for k in COMPL_BASE)
print(f"  complément conditionnel (24 fonds rendus une fois) aux bases : " +
      " ; ".join(f"{k} {v:.2f}" for k, v in COMPL_BASE.items()) +
      f" ; total {sum(COMPL_BASE.values()):.1f} USD ; plafond (ratios des plafonds de relais du tableau principal) "
      f"{compl_plafond:.1f} ; médiane aux rapports P11 {np.median(compl_cout):.1f}")
# D-g option (b) : 4 fiches d'antériorité non citée
dg_base = 4 * (0.06 + 0.10) + 4 * 0.25
print(f"  D-g option (b), M6b : 4 fiches (rédacteur 4 × 0,06 + lecture du PDF source 4 × 0,10 SUPPOSÉ ; vérificateur "
      f"4 × 0,25) : {dg_base:.1f} USD attendus ; plafond ×1,5 : {1.5 * dg_base:.1f}")

# C10 : devis de la course refait (devis v3 § 3 : 4 sous-sessions) + bisociation à trois bras.
fus_unit = 0.40 * r_fu + 0.057 * r_ai + juge3
P["C10"] = {}


def c10(reste, kc):
    course4 = (10 * r_kp + 18 * 1.0 + 1.75 + 6.5 * r_kj + 6.5 * r_ar + 18.3 * r_op + 10 * r_an + 7.3 * r_ai
               + 3 * kc * 4 * fus_unit)
    ss = np.where(course4 <= reste, 4, np.where(0.75 * course4 <= reste, 3, np.where(0.5 * course4 <= reste, 2, 0)))
    return ss, course4


for nom_reste, reste in (("reste = 110 − dépense (GO-2026-10-30-07 inchangé)", 110 - depense),
                         ("reste = 78 (total porté à 123 par la ligne nouvelle ; LECTURE À CONFIRMER)", np.full(N_SIM, 78.0))):
    for kc in (1, 2):
        ss, course4 = c10(reste, kc)
        P["C10"][(nom_reste, kc)] = np.mean(ss >= 2)
        print(f"  C10, {nom_reste}, course à S22 k = {kc} (trois bras, {3 * kc * 4} fusions) : devis refait médian "
              f"{np.median(course4):.1f} USD pour 4 sous-sessions ; reste médian {np.median(reste):.1f} ; tient à 4 "
              f"{np.mean(ss == 4):.2f}, à 3 {np.mean(ss == 3):.2f}, à 2 {np.mean(ss == 2):.2f}, à aucune {np.mean(ss == 0):.3f}")
C10_PRINCIPAL = ("reste = 110 − dépense (GO-2026-10-30-07 inchangé)", 1)   # lecture principale : S22 recommandé k = 1
P["C10_val"] = P["C10"][C10_PRINCIPAL]
ss_c, _ = c10(110 - depense - compl_cout, 1)
P["C10_compl"] = np.mean(ss_c >= 2)
ss_32, _ = c10(110 - B32["depense"], 1)
P["C10_32"] = np.mean(ss_32 >= 2)
print(f"    lecture principale de C10 (110 − dépense, k = 1) : {P['C10_val']:.2f} ; après complément (110 − dépense − "
      f"complément, k = 1) : {P['C10_compl']:.2f} (tient à 4 {np.mean(ss_c == 4):.2f}, à 3 {np.mean(ss_c == 3):.2f}, "
      f"à 2 {np.mean(ss_c == 2):.2f}) ; au plafond 32 (110 − dépense, k = 1) : {P['C10_32']:.2f}")
print(f"    décomposition v3 -> v5 (CP4-11) : lecture v3 (k = 2, reste 78) {P['C10'][(list(P['C10'])[2][0], 2)]:.3f} "
      f"(v3 : 0,933 ; v4 : 0,94) -> k = 1, reste 78 : {P['C10'][(list(P['C10'])[2][0], 1)]:.2f} -> k = 1, "
      f"reste = 110 − dépense : {P['C10_val']:.2f}")
print(f"    M7 « poste refait » (un rapport > 1,30) : {np.mean((r_kj > 1.3) | (r_ar > 1.3) | (r_op > 1.3) | (r_an > 1.3) | (r_ai > 1.3) | (r_kp > 1.3) | (r_fu > 1.3)):.2f}"
      " (réserve, hors porte)")

P["C11"] = 0.99
P["C12"] = 0.99
P["C13_tech"] = 0.95
print(f"  C11 cloisons du tableau : {P['C11']:.2f} ; C12 garde de paire (trois bras : méta, Gu-Krenn, basique) : {P['C12']:.2f} "
      f"(SUPPOSÉ : programmes éprouvés en É0)")
print(f"  C13 arrêts clos et rien « non mesuré » : technique {P['C13_tech']:.2f} (SUPPOSÉ : A2, A3, A5, A11, A14 "
      f"clos dans les plafonds) × budget {P['C13_budget']:.3f} (règle d'A1, plafond 45, arrêt 40) ; au plafond 32 : "
      f"budget {P['C13_budget_32']:.3f}")

# C14 : aucun audit R4 ouvert ou audit rendu sans artefact. Déclencheurs hors M1 : relecteur à 100 % (ci-dessus),
# contradiction lecture primaire / chaîne (SUPPOSÉ 0,05), « trop propre » de M3, M4, M6 (CP4-10, calculés ci-dessus).
P_ART = 0.15
propre_m3 = 0.85 ** 9 * (1 - 0.06) ** 254
autres = 1 - (1 - amb0) * (1 - 0.05) * (1 - propre_m3) * (1 - propre_m4) * (1 - m6_propre)
print(f"  C14 : probabilité d'un déclencheur hors M1 (relecteur 100 %, contradiction, M3, M4, M6 « trop propres ») : {autres:.3f}")

# ================================================================ Conjonction entière


def conjonction(d, c10_val=None, c10_compl=None, c6=None, c13b=None, etiquette=""):
    c10_val = P["C10_val"] if c10_val is None else c10_val
    c10_compl = P["C10_compl"] if c10_compl is None else c10_compl
    c6 = P["C6"] if c6 is None else c6
    c13b = P["C13_budget"] if c13b is None else c13b
    hors = P["C4"] * P["C5"] * c6 * P["C7"] * P["C8"] * P["C9"] * P["C11"] * P["C12"] * P["C13_tech"] * c13b
    audit = 1 - (1 - np.mean(d["audit"])) * (1 - autres)
    c14 = 1 - audit * P_ART
    ouverte = np.mean(d["m1"]) * hors * c10_val * c14
    compl = np.mean(d["besoin"]) * hors * c10_val * c14
    apres = ouverte + compl * (np.mean(d["ok_cumul"][d["besoin"]]) if d["besoin"].any() else 0) * (c10_compl / c10_val)
    return dict(hors=hors * c10_val, c14=c14, ouverte=ouverte, compl=compl, noeud=1 - ouverte - compl, apres=apres)


print("\n== CONJONCTION ENTIÈRE C1 à C14 (conditions hors juges indépendantes entre elles et des juges, SUPPOSÉ) ==")
R = conjonction(M1[CAS_JUGES[0][0]])
print(f"  produit des conditions hors juges (C4 à C13, aiguilleur étalonné par concrets écrits) : {R['hors']:.2f}")
for nom, *_ in CAS_JUGES:
    d = M1[nom]
    r = conjonction(d)
    print(f"  {nom} : porte des juges seule (C1-C2) {np.mean(d['c1c2']):.2f} ; C14 {r['c14']:.2f} ; "
          f"CONJONCTION ENTIÈRE ouverte d'emblée {r['ouverte']:.2f} ; complément proposé {r['compl']:.2f} ; "
          f"nœud d'emblée {r['noeud']:.2f} ; ouverte au total si le complément reçoit son GO {r['apres']:.2f}")
d = M1[CAS_JUGES[0][0]]
print(f"  sensibilités à la prédiction P1 : C13 technique à 1,00 -> ouverte d'emblée {R['ouverte'] / P['C13_tech']:.2f} ; "
      f"audit sans artefact (0) -> {R['ouverte'] / R['c14']:.2f} ; artefact 0,30 -> "
      f"{R['ouverte'] / R['c14'] * (1 - (1 - (1 - np.mean(d['audit'])) * (1 - autres)) * 0.30):.2f}")
print(f"  coûts aux bases (rapports à 1 : C13 budget = 1) -> ouverte d'emblée {R['ouverte'] / P['C13_budget']:.2f}")
for cle, val in P["C10"].items():
    if cle != C10_PRINCIPAL:
        print(f"  C10 selon « {cle[0]} », k = {cle[1]} ({val:.2f}) -> ouverte d'emblée {R['ouverte'] / P['C10_val'] * val:.2f}")
R32 = conjonction(d, c10_val=P["C10_32"], c13b=P["C13_budget_32"])
print(f"  PLAFOND 32 (arrêt d'étape 28 ; GO-2026-10-30-07 tel quel) : C13 budget {P['C13_budget_32']:.3f} ; C10 {P['C10_32']:.2f} ; "
      f"ouverte d'emblée {R32['ouverte']:.2f} ; complément proposé {R32['compl']:.2f} ; nœud d'emblée {R32['noeud']:.2f} "
      f"(CP4-07 : information, un seul plafond au gel)")
print(f"  rappel v4 (modèle grossier du budget, C10 sans complément) : ouverte d'emblée 0,17 ; complément 0,20 ; nœud 0,63 ; "
      f"au total 0,24 ; rappel v3 (plafond 32, fonds appariés, alarme S5 dans C14) : 0,15 ; 0,15 ; 0,71 ; 0,20")
print("  défaut R-819 (pas d'étalonnage de l'aiguilleur) : C7 non étalonné -> conjonction entière 0,00 ; nœud certain")

# ================================================================ D-i : trois variantes du plan des fonds
print("\n== Décision D-i : variantes du plan des fonds (prédiction P1 ; coûts aux bases du devis v3, SUPPOSÉ) ==")
# (2) 28 fonds + 4 rendus appariés supplémentaires (mémoire seulement ; aiguilleur sur les 4 ; aucun juge)
d3_base2 = 2 * 0.057 + 2 * 0.079
d4_base2 = 4 * 0.057
E2 = etapes_pre_pilote(delta_e3_base=d3_base2, delta_e3=2 * 0.057 * r_kj + 2 * 0.079 * r_ar,
                       delta_e4_base=d4_base2, delta_e4=4 * 0.057 * r_ai)
B2 = simuler_budget(E2, 45.0, 40.0)
ss2, _ = c10(110 - B2["depense"], 1)
R2 = conjonction(d, c10_val=np.mean(ss2 >= 2), c6=P["C6_var23"], c13b=1 - np.mean(B2["non_lancee"]))
# (3) 24 fonds dont 4 doublés : rédacteur −4 squelettes ; rendus 28 inchangés ; juges 28 inchangés
E3 = etapes_pre_pilote(delta_e1=-4 * 0.06)
B3 = simuler_budget(E3, 45.0, 40.0)
ss3, _ = c10(110 - B3["depense"], 1)
d3 = dict(m1=M1_VAR3["m1"], besoin=M1_VAR3["besoin"], audit=M1_VAR3["audit"], ok_cumul=d["ok_cumul"])
R3 = conjonction(d3, c10_val=np.mean(ss3 >= 2), c6=P["C6_var23"], c13b=1 - np.mean(B3["non_lancee"]))
print(f"  (1) 28 fonds uniques (texte du brouillon) : coût attendu {prot_base + sacr_base:.1f} USD ; paires PA : 0 ; "
      f"C1-C2 {np.mean(d['c1c2']):.2f} ; C6 {P['C6']:.3f} ; C13 budget {P['C13_budget']:.3f} ; C10 {P['C10_val']:.2f} ; "
      f"porte entière {R['ouverte']:.3f} ; nœud {R['noeud']:.2f} ; au total après complément {R['apres']:.3f}")
print(f"  (2) 28 fonds + 4 rendus appariés (mémoire seule, 4 lectures d'aiguilleur, aucun juge) : coût attendu "
      f"{prot_base + sacr_base + d3_base2 + d4_base2:.1f} USD (+{d3_base2 + d4_base2:.2f}) ; paires PA : 4 (≈ 2 en vérification) ; "
      f"C1-C2 {np.mean(d['c1c2']):.2f} (inchangé) ; C6 {P['C6_var23']:.3f} ; C13 budget {1 - np.mean(B2['non_lancee']):.3f} ; "
      f"C10 {np.mean(ss2 >= 2):.2f} ; porte entière {R2['ouverte']:.3f} ; nœud {R2['noeud']:.2f} ; au total {R2['apres']:.3f}")
print(f"  (3) 24 fonds dont 4 doublés (P 9, N 11, C 2, G 2 ; fiches P 11, N 13 ; 8 fiches corrélées) : coût attendu "
      f"{prot_base + sacr_base - 4 * 0.06:.1f} USD (−{4 * 0.06:.2f}) ; paires PA : 4 ; C1-C2 {np.mean(M1_VAR3['c1c2']):.2f} ; "
      f"C6 {P['C6_var23']:.3f} ; C13 budget {1 - np.mean(B3['non_lancee']):.3f} ; C10 {np.mean(ss3 >= 2):.2f} ; "
      f"porte entière {R3['ouverte']:.3f} ; nœud {R3['noeud']:.2f} ; au total {R3['apres']:.3f} "
      f"(graines v5 : l'écart de M1 avec (1) comprend le bruit de simulation, ±0,01)")

# ================================================================ Rappels du v2 corrigés
print("\n== M4 : fausses alertes sur 34 fiches de niveau méthode (CP2-13 : effectif 34) ==")
for fa in (0.03, 0.10, 0.20):
    print(f"  fausses alertes vraies {fa:.2f} : P(taux observé <= {SEUILS['S11_ord']}) = "
          f"{stats.binom.cdf(int(np.floor(34 * SEUILS['S11_ord'] + 1e-9)), 34, fa):.2f}")

# ================================================================ Bisociation à trois bras (R-643)
print("\n== Bisociation exploratoire à trois bras (méta v1, Gu-Krenn, basique) : paires et coût (SUPPOSÉ) ==")
unit = 0.40 + 0.25 + 0.057   # fusion par Kimi + trois juges + aiguilleur, par fusion (SUPPOSÉ, bases du devis v3)
for n_fiches in (6, 10):
    npairs = n_fiches * (n_fiches - 1) // 2
    print(f"  {n_fiches} fiches non aiguillées de passe 1 : {npairs} paires ; chaque bras choisit son argmax, les trois "
          f"paires sont distinctes (la suivante en cas de coïncidence, ordre de priorité tiré par pp2-bisoc-ordre)")
for k in (1, 2, 3):
    print(f"  k = {k} par bras : {3 * k} fusions ; pré-pilote ≈ {3 * k * unit:.2f} USD ; course, 4 cases ≈ "
          f"{4 * 3 * k * unit:.1f} USD")
print("  lectures d'étiquettes : trois lectures séparées par fiche (liste fermée ; vocabulaire Gu-Krenn ; grille des niches "
      f"et structures du bras méta) : ≈ {3 * 0.25:.2f} USD pour dix fiches (0,25 par lecture et par dix fiches, prorata de la v3)")
# CP4-06 : nombre de paires dans le profil du bras méta (SUPPOSÉ : grille à 6 niches, affectation uniforme ;
# communication faible avec probabilité 0,5 par paire de niches distinctes ; structure forte avec 0,3 par paire de fiches ;
# éloignement dans la bande avec 0,6 ; indépendants) — pour une prédiction P14, pas une mesure
g = rng("v5-meta-profil")
for n_fiches in (6, 10):
    nich = g.integers(0, 6, (N_SIM, n_fiches))
    iu = np.triu_indices(n_fiches, 1)
    diff = (nich[:, iu[0]] != nich[:, iu[1]])
    prof = diff & (g.random((N_SIM, len(iu[0]))) < 0.5) & (g.random((N_SIM, len(iu[0]))) < 0.3) & \
        (g.random((N_SIM, len(iu[0]))) < 0.6)
    npf = prof.sum(1)
    print(f"  bras méta, {n_fiches} fiches, grille à 6 niches (SUPPOSÉ ; faible 0,5, forte 0,3, bande 0,6) : paires dans le "
          f"profil médiane {np.median(npf):.0f}, P(zéro) {np.mean(npf == 0):.2f}, P(toutes les fiches de même niche) "
          f"{np.mean(~diff.any(1)):.3f}")
print("  note Gu-Krenn (modèle ou substitut) des trois paires et leur passage : rapportés sans test ; aucune comparaison "
      "entre bras au pré-pilote (une paire par bras) ; course à k = 1 : 12 fusions, erreur-type d'une aire sous la courbe "
      f"à 6 contre 6 ≈ {np.sqrt((0.5 * 0.5 + 5 * (0.5 / 1.5 - 0.25) + 5 * (2 * 0.25 / 1.5 - 0.25)) / 36):.2f} (Hanley-McNeil, à 0,5)")
print("fin ;", sys.version.split()[0])
