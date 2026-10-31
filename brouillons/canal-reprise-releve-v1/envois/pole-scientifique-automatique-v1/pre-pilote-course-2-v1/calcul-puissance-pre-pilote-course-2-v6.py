"""Calculs de puissance du pré-pilote de la course 2, brouillon 6. Processeur seul, aucune donnée de run.
Remplace calcul-puissance-pre-pilote-course-2-v5.py (gardé, R12). Ce qui change par rapport à la v5 (contre-lecture 4,
constats CP5-01 à CP5-13) :
  - CP5-04 : le budget joue l'ordre des étapes écrit dans le Plan (É6 juges sur les 28 rendus ; É7 : passe « tableau »,
    étiquettes, fusions, table seule ; É8 ; É9 ; É9b M6b) ; l'ordre joué par la v5 (ORDRE_V5) est gardé en comparaison ;
  - CP5-02 : M6 n'est jamais retirée entière : l'arrêt d'étape et le plafond la réduisent (une fois) ; réduite, elle est
    protégée ; si elle ne tient pas sous le plafond, elle est « non mesurée (budget) » et comptée dans C13 ; chaque
    retrait et chaque « non lancée » sont imprimés ; les conditions C6 (table seule retirée : axe 7 lu sur les bardeaux
    seuls), C8 (passe « tableau » retirée : M5 sur 10 fiches) et C9 (M6 réduite : 6 inventées, 3 altérées, 11 réelles)
    sont rejouées sous sacrifice et mélangées à la probabilité du sacrifice ;
  - CP5-09 : le relais coupe à son plafond : le coût ajouté au cumul est min(coût simulé, plafond de relais) ;
  - CP5-05 : M6b (D-g b) est une étape protégée hors porte (É9b) : jamais sacrifiée ; si elle ne tient pas sous le
    plafond, « M6b non mesurée (budget) », réserve, C13 inchangée ; configuration recommandée (D-g b + D-i 2) chiffrée
    à côté du texte de base (D-g a + D-i 1) ;
  - CP5-06 : plafond 45 avec arrêt d'étape 40 et plafond 45 sans arrêt d'étape chiffrés dans les deux configurations ;
    l'effet propre de l'arrêt (ce qu'il réduit ou retire ; ce qu'il protège) est imprimé ;
  - CP5-01, CP5-13 : C12 chiffrée (SUPPOSÉ) : garde de paire, effectif n < 3, annexe du bras méta non conforme (A20),
    bras Gu-Krenn non produit (source de S31 absente, moins de 2 fiches notables), sous D-h (a) (trois bras) et D-h (b)
    (deux bras) ;
  - CP5-10 : déclencheur « trop propre » de M3 : probabilité aux valeurs prédites et pour un instrument trop beau
    (rappel 1, fausses alertes 0,005) ; accord de 100 % aiguilleur / second lecteur sur 20 et sur 10 fiches ;
  - CP5-11 : P10 « 3 sur 4 au moins » à rappel vrai 0,60 imprimé ; total des plafonds de relais avec et sans É5bis.
Graines : les simulations gardées de la v4 et de la v5 gardent leurs noms de tâche « v4-… » et « v5-… » (mêmes tirages) ;
les simulations nouvelles portent des noms « v6-… ». SeedSequence(RACINE, spawn_key=(cle_de_tache(nom),)), même
dérivation que src/controle_ia/manifeste.py (R9).
Hypothèses déclarées dans le préenregistrement (brouillon 6) ; valeurs supposées marquées SUPPOSÉ.
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

# Variante (3) de D-i, simulation jointe à la prédiction P1 (graine v5)
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
# CP5-02 : si la table seule est sacrifiée, l'axe 7 se lit sur les bardeaux seuls (P7 : rappel 0,60).
ax7_def = stats.binom.cdf(5, 12, 0.75)          # rappel < 0,50 sur 12 <=> au plus 5 (union table + bardeaux)
ax7_def_bard = stats.binom.cdf(5, 12, 0.60)     # bardeaux seuls (table seule sacrifiée)
fa_def = 1 - stats.binom.cdf(int(np.floor(250 * 0.20)), 250, 0.06)


def c6(n_pos, ax7=ax7_def):
    seuil = int(np.ceil(0.60 * n_pos)) - 1        # rappel < 0,60 <=> vus <= seuil
    return (1 - stats.binom.cdf(seuil, n_pos, 0.85)) * (1 - ax7) * (1 - fa_def)


P["C6"] = c6(9)
P["C6_var23"] = c6(11)
P["C6_bard"] = c6(9, ax7_def_bard)
P["C6_var23_bard"] = c6(11, ax7_def_bard)
print(f"  C6 mémoire et axe 7 non défaillantes : {P['C6']:.3f} (P6 : rappel 0,85 sur ≈ 9 positifs de vérification "
      f"(PB seules, variante (1)), fausses alertes 0,06 sur 250 ; P7 : union 0,75 sur 12)")
print(f"    variantes (2) et (3) de D-i (≈ 11 positifs : PB ≈ 9 + PA ≈ 2) : {P['C6_var23']:.3f} ; "
      f"rappel v3 (≈ 14 positifs, 10 PA) : {c6(14):.3f}")
print(f"    CP5-02, table seule sacrifiée (axe 7 lu sur les bardeaux seuls, rappel 0,60 sur 12) : C6 {P['C6_bard']:.3f} "
      f"(variante (1)) ; {P['C6_var23_bard']:.3f} (variantes (2), (3)) ; « bardeaux seuls défaillants » {ax7_def_bard:.3f} "
      f"contre union {ax7_def:.3f}")
propre_m3 = 0.85 ** 9 * (1 - 0.06) ** 254
propre_m3_beau = 1.0 ** 9 * stats.binom.cdf(2, 254, 0.005)
print("    déclencheur R4 « trop propre » de M3 (rappel 9 sur 9 ET au plus 2 fausses alertes sur ≈ 250 NA et 4 NB, "
      f"soit ≤ 1 %) : aux valeurs prédites {0.85 ** 9 * stats.binom.cdf(2, 254, 0.06):.4f} (rappel seul 9 sur 9 : "
      f"{0.85 ** 9:.2f}) ; pour un instrument trop beau (rappel 1, fausses alertes 0,005) : {propre_m3_beau:.2f} "
      f"(CP5-10 : le déclencheur n'est pas inerte, il ne s'allume que pour une propreté implausible) ; ancienne règle "
      f"« zéro fausse alerte » aux valeurs prédites : {propre_m3:.4f}")
propre_m3 = 0.85 ** 9 * stats.binom.cdf(2, 254, 0.06)

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
      f"sur 40 : {fa40:.2f}) ; la condition « accord de 100 % entre aiguilleur et second lecteur sur les fiches de Kimi » s'y ajoute (C8)")
print("    défaut R-819 (aucun concret écrit) : C7 « non étalonné » avec certitude : porte fermée (probabilité 0)")

# C8 : débordement de Kimi, 20 fiches. Union, intersection, adjudication par un troisième lecteur isolé.
TAUX, SENS, FA = 0.05, 0.90, 0.03     # P9 ; sensibilité de chaque lecteur SUPPOSÉ ; fausses alertes (P8) SUPPOSÉ égales


def m5(g, n_fiches, taux=TAUX):
    vrai = g.random((N_SIM, n_fiches)) < taux
    lect = [np.where(vrai, g.random((N_SIM, n_fiches)) < SENS, g.random((N_SIM, n_fiches)) < FA) for _ in range(3)]
    union = (lect[0] | lect[1]).mean(1)
    inter = (lect[0] & lect[1]).mean(1)
    major = ((lect[0].astype(int) + lect[1] + lect[2]) >= 2).mean(1)
    conf = union <= SEUILS["S12"] + 1e-9
    depas = inter > SEUILS["S12"] + 1e-9
    adj = ~conf & ~depas
    ok = conf | (adj & (major <= SEUILS["S12"] + 1e-9))
    accord100 = np.mean((lect[0] == lect[1]).all(1))
    return ok, conf, depas, adj, major, accord100


g = rng("v4-c8")
c8, conf, depas, adj, major, accord100 = m5(g, 20)
P["C8"] = np.mean(c8)
propre_m4 = np.mean(tot7 == 12) * fa40 * accord100
print(f"    accord de 100 % entre les deux lecteurs sur 20 fiches : {accord100:.2f} ; déclencheur « trop propre » de M4 "
      f"complet (12 sur 12, zéro fausse alerte sur 40, accord 100 % sur 20) : {propre_m4:.4f}")
print(f"  C8 Kimi proposeur conforme : {P['C8']:.2f} — union <= S12 {np.mean(conf):.2f} ; intersection > S12 "
      f"{np.mean(depas):.2f} ; adjudication {np.mean(adj):.2f}, dont conforme à la majorité "
      f"{np.mean(major[adj] <= 0.10) if adj.any() else 0:.2f} (P9 : taux 0,05 ; sensibilité 0,90 et fausses alertes "
      f"0,03 par lecteur, SUPPOSÉ)")
for t in (0.10, 0.20):
    ok_t = m5(g, 20, t)[0]
    print(f"    taux vrai {t:.2f} : déclaré conforme {np.mean(ok_t):.2f}")
g = rng("v6-c8-10")
c8_10, conf10, depas10, adj10, major10, accord100_10 = m5(g, 10)
P["C8_10"] = np.mean(c8_10)
print(f"    CP5-02, passe « tableau » sacrifiée (M5 sur les 10 fiches de la passe 1) : C8 {P['C8_10']:.2f} (union <= S12 "
      f"{np.mean(conf10):.2f} ; adjudication {np.mean(adj10):.2f}) ; taux vrai 0,20 déclaré conforme "
      f"{np.mean(m5(g, 10, 0.20)[0]):.2f} ; accord de 100 % sur 10 fiches {accord100_10:.2f} ; déclencheur « trop propre » "
      f"de M4 complet sur 10 fiches {np.mean(tot7 == 12) * fa40 * accord100_10:.4f} (CP5-10)")

# C9 : antériorité non défaillante (inventées < 0,70 sur 9 <=> au plus 6 vues).
P["C9"] = 1 - stats.binom.cdf(6, 9, 0.95)
m6_et = (1 - stats.binom.cdf(8, 9, 0.95)) * (1 - stats.binom.cdf(6, 9, 0.70)) * stats.binom.cdf(2, 22, 0.08)
m6_propre = 0.95 ** 9 * 0.70 ** 9 * (1 - 0.08) ** 22
print(f"  C9 antériorité non défaillante : {P['C9']:.3f} (P10 : inventées 0,95) ; M6 « étalonnée » {m6_et:.2f} "
      f"(C9 accepte « non concluant ») ; déclencheur R4 « trop propre » de M6 (9 sur 9, 9 sur 9, 0 sur 22) : {m6_propre:.4f}")
# CP5-02 : M6 réduite à 4 fiches (tâche pp2-reduction-e9 : 2 fiches à inventées, 1 à altérées, 1 sans défaut ->
# 6 inventées, 3 altérées, 11 réelles) : C9 défaillante <=> inventées < 0,70 sur 6 <=> au plus 4 vues
P["C9_red"] = 1 - stats.binom.cdf(4, 6, 0.95)
m6_et_red = (1 - stats.binom.cdf(5, 6, 0.95)) * (1 - stats.binom.cdf(2, 3, 0.70)) * stats.binom.cdf(1, 11, 0.08)
print(f"    CP5-02, M6 réduite (6 inventées, 3 altérées, 11 réelles) : C9 non défaillante {P['C9_red']:.3f} ; "
      f"« étalonnée » {m6_et_red:.2f} (S13 exige 6 sur 6, S14 3 sur 3, S15 au plus 1 sur 11) ; déclencheur « trop propre » "
      f"{0.95 ** 6 * 0.70 ** 3 * (1 - 0.08) ** 11:.3f}")
# D-g, option (b) : 4 fiches d'antériorité non citée (M6b) ; borne basse du rappel à 95 % si 4 sur 4 ; 3 sur 4
print(f"    D-g option (b), M6b (4 fiches d'antériorité non citée) : 4 sur 4 vues ne bornent le rappel qu'à "
      f"{0.05 ** 0.25:.2f} (unilatérale 95 %) ; à rappel vrai 0,75, « 3 sur 4 au moins » se voit avec "
      f"{1 - stats.binom.cdf(2, 4, 0.75):.2f}, à 0,60 (P10) avec {1 - stats.binom.cdf(2, 4, 0.60):.3f} (CP5-11), "
      f"à 0,50 avec {1 - stats.binom.cdf(2, 4, 0.50):.2f} : garde grossière, réserve")

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

# Ordres d'étapes. Clés : É1 à É5bis ; É6 juges sur les 28 rendus ; É7a passe « tableau » ; É7b étiquettes ;
# É7c fusions ; É7d table seule ; É8 paraphrases ; É9 antériorité ; É9b M6b (D-g b).
ORDRE_TEXTE = ["É1", "É2", "É3", "É4", "É5", "É5bis", "É6", "É7a", "É7b", "É7c", "É7d", "É8", "É9", "É9b"]  # Plan du brouillon 6
ORDRE_V5 = ["É1", "É2", "É3", "É4", "É5", "É5bis", "É6", "É7b", "É7c", "É7a", "É7d", "É8", "É9", "É9b"]     # joué par le script v5 (CP5-04)
ORDRE_B4 = ["É1", "É2", "É3", "É4", "É5", "É5bis", "É7a", "É7b", "É7c", "É6", "É7d", "É8", "É9", "É9b"]     # brouillon 4 (juges après)
ORDRE_M6_TOT = ["É1", "É9", "É2", "É3", "É4", "É5", "É5bis", "É6", "É7a", "É7b", "É7c", "É7d", "É8", "É9b"]  # information : M6 jouée après É1 (sa seule dépendance)


def etapes_pre_pilote(delta_e1=0.0, delta_e3_base=0.0, delta_e3=None, delta_e4_base=0.0, delta_e4=None, ordre=None,
                      m6b=False):
    """Étapes du pré-pilote : (clé, nom, coût simulé, plafond de relais, attendu aux bases, rôle), dans l'ordre demandé.
    rôle : 'prot' = protégée (jamais sacrifiée ; non lancée -> C13) ; 'prot_hp' = protégée hors porte (M6b : non lancée ->
    réserve, C13 inchangée) ; 'sacr1', 'sacr3', 'sacr4' = retirables dans l'ordre d'A1 ; 'sacr2' = M6, réductible une fois,
    jamais retirée entière (CP5-02)."""
    d3 = 0 * un if delta_e3 is None else delta_e3
    d4 = 0 * un if delta_e4 is None else delta_e4
    ordre = ORDRE_TEXTE if ordre is None else ordre
    d1 = delta_e1 + (0.64 if m6b else 0.0)      # M6b : rédacteur 4 × 0,06 + lecture des PDF sources 4 × 0,10 (SUPPOSÉ)
    liste = [
        ("É1", "É1 rédacteur", (REDACTEUR_E1 + d1) * r_re, 3.3 + 1.25 * d1, REDACTEUR_E1 + d1, "prot"),
        ("É2", "É2 Kimi passe 1", 2.0 * r_kp, 3.0, 2.0, "prot"),
        ("É3", "É3 rendus", rendus + d3, 2.8 + 1.4 * delta_e3_base, rendus_base + delta_e3_base, "prot"),
        ("É4", "É4 aiguilleur 56 lectures, second lecteur 10, adjudicateur, nouvel essai",
         (66 * 0.057 + 0.05 + 0.3) * r_ai + d4, 5.5 + 1.4 * delta_e4_base, 66 * 0.057 + 0.35 + delta_e4_base, "prot"),
        ("É5", "É5 relecteur", 1.4 * r_re, 1.9, 1.4, "prot"),
        ("É5bis", "É5bis seconde version de témoins (si C5 échoue en v1)", v2_ind * (1.5 * r_re + rendus + 1.4 * r_re),
         v2_ind * 6.6, v2_ind * (1.5 + rendus_base + 1.4), "prot"),
        ("É6", "É6 trois juges sur les 28 rendus", 28 * juge3, 11.6, 28 * JUGE3_BASE, "prot"),
        ("É7a", "É7a passe « tableau » de Kimi, aiguilleur et second lecteur sur elle", 2.0 * r_kp + 20 * 0.057 * r_ai,
         4.6, 2.0 + 20 * 0.057, "sacr4"),
        ("É7b", "É7b lectures d'étiquettes (trois lectures, deux lecteurs)", 0.75 * r_op, 1.0, 0.75, "prot"),
        ("É7c", "É7c fusions (3), aiguilleur et trois juges sur elles", 1.2 * r_fu + 3 * 0.057 * r_ai + 3 * juge3,
         3.5, 1.2 + 3 * 0.057 + 3 * JUGE3_BASE, "sacr1"),
        ("É7d", "É7d Opus, table seule de l'axe 7", 0.7 * r_op, 1.0, 0.7, "sacr3"),
        ("É8", "É8 paraphrases (rédacteur)", REDACTEUR_E8 * r_re, 0.7, REDACTEUR_E8, "prot"),
        ("É9", "É9 antériorité, 8 fiches (réduite : 4 fiches)", 2.0 * r_an, 6.0, 2.0, "sacr2"),
    ]
    if m6b:
        liste.append(("É9b", "É9b M6b, vérificateur sur 4 fiches d'antériorité non citée", 1.0 * r_an, 1.5, 1.0, "prot_hp"))
    cle = {e[0]: e for e in liste}
    return [cle[k] for k in ordre if k in cle]


def simuler_budget(etapes, plafond, arret, relais_dur=False):
    """Règle d'A1 étape par étape (brouillon 6, CP5-02, CP5-04, CP5-09). Avant chaque étape E non retirée :
    (1) projection = cumul + plafond(E) + attendu aux bases des étapes restantes non retirées ; tant que
        projection > plafond, prochaine mesure de la liste de sacrifice non encore jouée : (1) fusions retirées,
        (2) M6 réduite à 4 fiches (coût, plafond et attendu divisés par deux ; réduite, elle est protégée), (3) table seule
        retirée, (4) passe « tableau » retirée ;
    (2) arrêt d'étape (si S17 en a un) : si cumul >= arrêt, les étapes retirables non jouées sont retirées et M6 non jouée
        est réduite ; rien de protégé ne change ;
    (3) plafond : si cumul + plafond(E) > plafond : E retirable -> retirée ; E = M6 non réduite -> réduite puis
        réexaminée ; E = M6 réduite, ou E protégée -> non lancée, « non mesuré (budget) », C13 non satisfaite ;
        E = M6b (protégée hors porte) -> non lancée, réserve, C13 inchangée ;
    (4) sinon E est jouée. Lecture principale (relais_dur=False) : le plafond de relais est une RÉSERVATION (il sert aux
        tests (1) à (3)) et S17 est le seul plafond qui coupe : le coût réel est compté en entier ; si le cumul franchit
        S17 pendant E, E est coupée à S17 : protégée -> « non mesuré (budget) », C13 ; retirable -> retirée ; M6b ->
        réserve. Lecture d'information (relais_dur=True, CP5-09) : chaque relais coupe à son propre plafond : le coût
        ajouté est min(coût, plafond de relais) et la coupure d'une étape protégée est comptée (mesure sur effectif réduit)."""
    n = N_SIM
    cles = [e[0] for e in etapes]
    cout = [e[2] * un for e in etapes]
    plaf = [e[3] * un for e in etapes]
    att = [e[4] * un for e in etapes]
    role = [e[5] for e in etapes]
    retire = [np.zeros(n, bool) for _ in etapes]
    joue = [np.zeros(n, bool) for _ in etapes]
    reduit = np.zeros(n, bool)
    reduit_par_arret = np.zeros(n, bool)
    retire_par_arret = np.zeros(n, bool)
    cum = np.zeros(n)
    non_lancee = np.zeros(n, bool)
    non_lancee_m6 = np.zeros(n, bool)
    m6b_non_lancee = np.zeros(n, bool)
    coupe = [np.zeros(n, bool) for _ in etapes]
    k6 = role.index("sacr2")
    ordre = [role.index("sacr1"), k6, role.index("sacr3"), role.index("sacr4")]

    def reduire(mask):
        m = mask & ~reduit & ~joue[k6]
        reduit[:] |= m
        cout[k6] = np.where(m, cout[k6] / 2, cout[k6])
        plaf[k6] = np.where(m, plaf[k6] / 2, plaf[k6])
        att[k6] = np.where(m, att[k6] / 2, att[k6])
        return m

    def reste_apres(i):
        return sum(np.where(retire[j], 0, att[j]) for j in range(i + 1, len(etapes)))

    for i in range(len(etapes)):
        actif = ~retire[i]
        for _ in range(2):      # deux passes : la réduction de M6 peut suffire avant un retrait suivant
            proj = cum + plaf[i] + reste_apres(i)
            for k in ordre:
                besoin = actif & (proj > plafond) & ~retire[k] & ~joue[k]
                if k == k6:
                    reduire(besoin)
                else:
                    retire[k] |= besoin
                proj = cum + plaf[i] + reste_apres(i)
        # arrêt d'étape : plus aucune mesure retirable ; M6 réduite
        if arret < plafond:
            touche = cum >= arret
            for k in ordre:
                if k == k6:
                    reduit_par_arret |= reduire(touche)
                else:
                    m = touche & ~retire[k] & ~joue[k]
                    retire_par_arret |= m
                    retire[k] |= m
        actif = ~retire[i]
        tient = cum + plaf[i] <= plafond + 1e-9
        if role[i] == "sacr2":
            reduire(actif & ~tient)
            tient = cum + plaf[i] <= plafond + 1e-9
            non_lancee_m6 |= actif & ~tient
            non_lancee |= actif & ~tient
        elif role[i] in ("sacr1", "sacr3", "sacr4"):
            retire[i] |= actif & ~tient
        elif role[i] == "prot_hp":
            m6b_non_lancee |= actif & ~tient
        else:
            non_lancee |= actif & ~tient
        actif = ~retire[i]
        lance = actif & tient
        joue[i] |= lance
        if relais_dur:
            coupe[i] |= lance & (cout[i] > plaf[i] + 1e-9)
            cum = cum + np.where(lance, np.minimum(cout[i], plaf[i]), 0)
        else:
            cum_apres = cum + np.where(lance, cout[i], 0)
            depasse = lance & (cum_apres > plafond + 1e-9)
            coupe[i] |= depasse
            if role[i] in ("prot", "sacr2"):
                non_lancee |= depasse
                non_lancee_m6 |= depasse if role[i] == "sacr2" else False
            elif role[i] == "prot_hp":
                m6b_non_lancee |= depasse
            else:
                retire[i] |= depasse
            cum = np.minimum(cum_apres, plafond)
    ret = {cles[k]: retire[k] for k in range(len(etapes))}
    coupes = {cles[k]: coupe[k] for k in range(len(etapes))}
    coupe_prot = np.any([coupe[k] for k in range(len(etapes)) if role[k] in ("prot", "sacr2")], axis=0)
    depense_sans_troncature = sum(np.where(joue[k], cout[k], 0) for k in range(len(etapes)))
    sacrifie = np.any([retire[k] for k in ordre], axis=0) | reduit
    return dict(depense=cum, non_lancee=non_lancee, non_lancee_m6=non_lancee_m6, m6b_non_lancee=m6b_non_lancee,
                sacrifie=sacrifie, retire=ret, reduit=reduit, arret_effet=reduit_par_arret | retire_par_arret,
                coupes=coupes, coupe_prot=coupe_prot, depense_sans_troncature=depense_sans_troncature, relais_dur=relais_dur,
                au_dela_reservation=np.any([joue[k] & (cout[k] > plaf[k] + 1e-9) for k in range(len(etapes))], axis=0),
                arret_touche=cum >= arret if arret < plafond else np.zeros(n, bool))


def decrire(b, etiquette, m6b=False):
    s = (f"  {etiquette} : dépense médiane {np.median(b['depense']):.1f} USD, quantile 90 % {np.quantile(b['depense'], 0.9):.1f}, "
         f"maximum {b['depense'].max():.1f} ; P(un sacrifice ou une réduction au moins) {np.mean(b['sacrifie']):.3f} "
         f"(fusions retirées {np.mean(b['retire']['É7c']):.3f} ; M6 réduite {np.mean(b['reduit']):.3f} ; table seule retirée "
         f"{np.mean(b['retire']['É7d']):.3f} ; passe « tableau » retirée {np.mean(b['retire']['É7a']):.3f}) ; "
         f"P(arrêt d'étape touché) {np.mean(b['arret_touche']):.3f}, dont il réduit ou retire quelque chose "
         f"{np.mean(b['arret_effet']):.3f} ; P(étape protégée non lancée, « non mesuré (budget) ») {np.mean(b['non_lancee']):.4f} "
         f"(dont M6 réduite qui ne tient pas {np.mean(b['non_lancee_m6']):.4f})")
    if m6b:
        s += f" ; M6b non lancée (réserve, hors C13) {np.mean(b['m6b_non_lancee']):.4f}"
    if b["relais_dur"]:
        s += (f" ; relais coupé à son propre plafond sur une étape protégée au moins (mesure sur effectif réduit) "
              f"{np.mean(b['coupe_prot']):.3f} (É6 juges {np.mean(b['coupes']['É6']):.3f} ; É2 {np.mean(b['coupes']['É2']):.3f} ; "
              f"É4 {np.mean(b['coupes']['É4']):.3f} ; É9 {np.mean(b['coupes']['É9']):.3f}) ; dépense médiane sans troncature "
              f"{np.median(b['depense_sans_troncature']):.1f}, quantile 90 % {np.quantile(b['depense_sans_troncature'], 0.9):.1f}")
    else:
        s += (f" ; étape coupée à S17 (comptée ci-dessus) {np.mean(b['coupe_prot']):.4f} ; au moins un relais au-delà de sa "
              f"réservation (réserve M7, pas de coupure) {np.mean(b['au_dela_reservation']):.2f}")
    print(s)


print("\n== Budget du pré-pilote selon la règle d'A1, étape par étape (CP5-02, CP5-04, CP5-09 ; rapports P11 ; seconde version comprise) ==")
ETAPES = etapes_pre_pilote()
prot_base = sum(e[4] for e in ETAPES if e[5] == "prot" and e[0] != "É5bis")
sacr_base = sum(e[4] for e in ETAPES if e[5] != "prot")
print(f"  aux bases (rapports à 1) : protégé {prot_base:.1f} USD ; sacrifiable {sacr_base:.1f} USD ; total attendu "
      f"{prot_base + sacr_base:.1f} ; somme des plafonds de relais hors É5bis {sum(e[3] for e in ETAPES if e[0] != 'É5bis'):.1f}, "
      f"avec É5bis (6,6) {sum(e[3] for e in ETAPES if e[0] != 'É5bis') + 6.6:.1f} (CP5-11) ; "
      f"seconde version de témoins ≈ {1.5 + rendus_base + 1.4:.1f} USD si C5 échoue en première version "
      f"(probabilité {1 - np.mean(ok_v[:, 0]):.2f})")
total_brut = sum(e[2] for e in ETAPES)
# Configuration de base (D-g a, D-i 1) et configuration recommandée (D-g b, D-i 2)
d3_base2 = 2 * 0.057 + 2 * 0.079
d4_base2 = 4 * 0.057
ETAPES_REC = etapes_pre_pilote(delta_e3_base=d3_base2, delta_e3=2 * 0.057 * r_kj + 2 * 0.079 * r_ar,
                               delta_e4_base=d4_base2, delta_e4=4 * 0.057 * r_ai, m6b=True)
rec_base = sum(e[4] for e in ETAPES_REC if e[0] != "É5bis")
print(f"  configuration recommandée (D-g b : M6b en É1 et É9b ; D-i 2 : 4 rendus appariés) aux bases : total attendu "
      f"{rec_base:.1f} USD (+{rec_base - prot_base - sacr_base:.2f} : M6b 1,64 ; D-i (2) 0,50)")
BUDGETS = {}
CONFIGS = [("base", 45.0, 40.0, ETAPES, "texte de base (D-g a, D-i 1), plafond 45, arrêt d'étape 40, ordre du Plan"),
           ("base-sans-arret", 45.0, 45.0, ETAPES, "texte de base, plafond 45 sans arrêt d'étape, ordre du Plan"),
           ("rec", 45.0, 40.0, ETAPES_REC, "RECOMMANDÉE (D-g b, D-i 2), plafond 45, arrêt d'étape 40, ordre du Plan"),
           ("rec-sans-arret", 45.0, 45.0, ETAPES_REC, "RECOMMANDÉE (D-g b, D-i 2), plafond 45 sans arrêt d'étape, ordre du Plan"),
           ("base-ordre-v5", 45.0, 40.0, etapes_pre_pilote(ordre=ORDRE_V5), "texte de base, 45 ; 40, ordre joué par le script v5 (étiquettes, fusions, puis passe « tableau » ; CP5-04, comparaison)"),
           ("base-ordre-b4", 45.0, 40.0, etapes_pre_pilote(ordre=ORDRE_B4), "texte de base, 45 ; 40, ordre du brouillon 4 (juges après les sacrifiables ; comparaison)"),
           ("base-m6-tot", 45.0, 40.0, etapes_pre_pilote(ordre=ORDRE_M6_TOT), "texte de base, 45 ; 40, M6 jouée juste après É1 (information : option de plan non retenue, à la décision de Lazar)"),
           ("rec-m6-tot", 45.0, 40.0, etapes_pre_pilote(delta_e3_base=d3_base2, delta_e3=2 * 0.057 * r_kj + 2 * 0.079 * r_ar, delta_e4_base=d4_base2, delta_e4=4 * 0.057 * r_ai, m6b=True, ordre=ORDRE_M6_TOT), "RECOMMANDÉE, 45 ; 40, M6 jouée juste après É1 (information)"),
           ("base-32", 32.0, 28.0, ETAPES, "texte de base, plafond 32, arrêt d'étape 28 (GO-2026-10-30-07 tel quel ; information)"),
           ("rec-32", 32.0, 28.0, ETAPES_REC, "RECOMMANDÉE, plafond 32, arrêt d'étape 28 (information)")]
for cle, pl, ar, et, etiquette in CONFIGS:
    BUDGETS[cle] = simuler_budget(et, pl, ar)
    decrire(BUDGETS[cle], etiquette, m6b=any(e[0] == "É9b" for e in et))
print("  -- lecture d'information (CP5-09) : chaque relais coupe à son propre plafond (plafonds du tableau, ×1,3 à ×1,6 des bases, "
      "sous les bornes hautes de P11) --")
for cle, pl, ar, et, etiquette in CONFIGS[:4]:
    b = simuler_budget(et, pl, ar, relais_dur=True)
    BUDGETS[cle + "-relais-dur"] = b
    decrire(b, etiquette + ", RELAIS DUR", m6b=any(e[0] == "É9b" for e in et))
print(f"  rappel du modèle grossier de la v4 (total sans sacrifice > plafond ; protégé > plafond) : à 45 : "
      f"{np.mean(total_brut > 45):.2f} / {np.mean(sum(e[2] for e in ETAPES if e[5] == 'prot') > 45):.3f} ; à 32 : "
      f"{np.mean(total_brut > 32):.2f} / {np.mean(sum(e[2] for e in ETAPES if e[5] == 'prot') > 32):.3f} ; "
      f"dépense médiane sans plafond ni troncature {np.median(total_brut):.1f}")

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
dg_base = 4 * (0.06 + 0.10) + 4 * 0.25
print(f"  D-g option (b), M6b : 4 fiches (rédacteur 4 × 0,06 + lecture du PDF source 4 × 0,10 SUPPOSÉ, en É1 ; vérificateur "
      f"4 × 0,25 en É9b) : {dg_base:.1f} USD attendus ; plafond ×1,5 : {1.5 * dg_base:.1f}")

# C10 : devis de la course refait (devis v3 § 3 : 4 sous-sessions) + bisociation à trois bras.
fus_unit = 0.40 * r_fu + 0.057 * r_ai + juge3


def c10(reste, kc):
    course4 = (10 * r_kp + 18 * 1.0 + 1.75 + 6.5 * r_kj + 6.5 * r_ar + 18.3 * r_op + 10 * r_an + 7.3 * r_ai
               + 3 * kc * 4 * fus_unit)
    ss = np.where(course4 <= reste, 4, np.where(0.75 * course4 <= reste, 3, np.where(0.5 * course4 <= reste, 2, 0)))
    return ss, course4


P["C10"] = {}
depense = BUDGETS["base"]["depense"]
for nom_reste, reste in (("reste = 110 − dépense (GO-2026-10-30-07 inchangé)", 110 - depense),
                         ("reste = 78 (total porté à 123 par la ligne nouvelle)", np.full(N_SIM, 78.0))):
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
print(f"    lecture principale de C10 (110 − dépense, k = 1) : {P['C10_val']:.2f} ; après complément (110 − dépense − "
      f"complément, k = 1) : {P['C10_compl']:.2f} (tient à 4 {np.mean(ss_c == 4):.2f}, à 3 {np.mean(ss_c == 3):.2f}, "
      f"à 2 {np.mean(ss_c == 2):.2f})")
print(f"    décomposition v3 -> v6 (CP4-11) : lecture v3 (k = 2, reste 78) {P['C10'][(list(P['C10'])[2][0], 2)]:.3f} "
      f"(v3 : 0,933 ; v4 : 0,94 ; v5 : 0,936) -> k = 1, reste 78 : {P['C10'][(list(P['C10'])[2][0], 1)]:.2f} -> k = 1, "
      f"reste = 110 − dépense : {P['C10_val']:.2f} (v5 : 0,92)")
print(f"    M7 « poste refait » (un rapport > 1,30) : {np.mean((r_kj > 1.3) | (r_ar > 1.3) | (r_op > 1.3) | (r_an > 1.3) | (r_ai > 1.3) | (r_kp > 1.3) | (r_fu > 1.3)):.2f}"
      " (réserve, hors porte)")

# C11, C12 (CP5-01, CP5-13 : chiffrée), C13 technique
P["C11"] = 0.99
P_GARDE_PAIRE = 0.99      # SUPPOSÉ : programmes de score éprouvés en É0 (garde R5 n° 16)
P_N_INF_3 = 0.02          # SUPPOSÉ : moins de 3 fiches non aiguillées à la passe 1 (passe 1 pauvre ou très aiguillée)
P_ANNEXE_NC = 0.03        # SUPPOSÉ sous D-h (a) : annexe scellée avant le gel, non conforme à É0 (altération, garde 22b, 23, 24)
P_GK_NP = 0.10            # SUPPOSÉ : bras Gu-Krenn non produit (source de S31 absente à É0 0,07 ; moins de 2 fiches notables 0,03)
P_BASIQUE_NP = 0.01       # SUPPOSÉ
deux_np_a = (P_ANNEXE_NC * P_GK_NP + P_ANNEXE_NC * P_BASIQUE_NP + P_GK_NP * P_BASIQUE_NP - 2 * P_ANNEXE_NC * P_GK_NP * P_BASIQUE_NP)
P["C12"] = P_GARDE_PAIRE * (1 - P_N_INF_3) * (1 - deux_np_a)
P["C12_b"] = P_GARDE_PAIRE * (1 - P_N_INF_3) * (1 - P_GK_NP) * (1 - P_BASIQUE_NP)
print(f"  C11 cloisons du tableau : {P['C11']:.2f}")
print(f"  C12 bisociation (CP5-01, CP5-13 ; SUPPOSÉ) : garde de paire {P_GARDE_PAIRE:.2f} ; n < 3 fiches non aiguillées "
      f"{P_N_INF_3:.2f} ; annexe du bras méta non conforme à É0 sous D-h (a) {P_ANNEXE_NC:.2f} ; bras Gu-Krenn non produit "
      f"{P_GK_NP:.2f} ; bras basique non produit {P_BASIQUE_NP:.2f} -> sous D-h (a), trois bras, « deux ou plus non produits » "
      f"{P_N_INF_3 + (1 - P_N_INF_3) * deux_np_a:.3f}, C12 {P['C12']:.3f} ; sous D-h (b), deux bras (les deux exigés) : C12 {P['C12_b']:.3f} "
      f"(v5 : 0,99 sans ces causes) ; fusions sacrifiées : C12 lue sur les paires, inchangée, réserve « chaîne éprouvée "
      f"jusqu'à la paire seulement »")
P["C13_tech"] = 0.95
for cle in ("base", "rec", "base-sans-arret", "rec-sans-arret", "base-32", "rec-32"):
    P[f"C13_budget_{cle}"] = 1 - np.mean(BUDGETS[cle]["non_lancee"])
print(f"  C13 arrêts clos et rien « non mesuré » : technique {P['C13_tech']:.2f} (SUPPOSÉ : A2, A3, A5, A11, A14 "
      f"clos dans les plafonds) × budget : base {P['C13_budget_base']:.4f} (45 ; 40), {P['C13_budget_base-sans-arret']:.4f} (45 sans arrêt) ; "
      f"recommandée {P['C13_budget_rec']:.4f} (45 ; 40), {P['C13_budget_rec-sans-arret']:.4f} (45 sans arrêt) ; "
      f"au plafond 32 : base {P['C13_budget_base-32']:.3f}, recommandée {P['C13_budget_rec-32']:.3f}")

# C14 : aucun audit R4 ouvert ou audit rendu sans artefact. Déclencheurs hors M1 : relecteur à 100 % (ci-dessus),
# contradiction lecture primaire / chaîne (SUPPOSÉ 0,05), « trop propre » de M3, M4, M6 (CP4-10, calculés ci-dessus).
P_ART = 0.15
autres = 1 - (1 - amb0) * (1 - 0.05) * (1 - propre_m3) * (1 - propre_m4) * (1 - m6_propre)
print(f"  C14 : probabilité d'un déclencheur hors M1 (relecteur 100 %, contradiction, M3, M4, M6 « trop propres ») : {autres:.3f}")

# ================================================================ Conjonction entière


def conditions_sous_sacrifice(b, var23=False):
    """C6, C8, C9 mélangées à la probabilité de chaque sacrifice (CP5-02) : table seule retirée -> bardeaux seuls ;
    passe « tableau » retirée -> M5 sur 10 fiches ; M6 réduite -> 6 inventées."""
    p_tab = np.mean(b["retire"]["É7d"]); p_passe = np.mean(b["retire"]["É7a"]); p_red = np.mean(b["reduit"])
    c6_plein, c6_bard = (P["C6_var23"], P["C6_var23_bard"]) if var23 else (P["C6"], P["C6_bard"])
    return dict(c6=(1 - p_tab) * c6_plein + p_tab * c6_bard, c8=(1 - p_passe) * P["C8"] + p_passe * P["C8_10"],
                c9=(1 - p_red) * P["C9"] + p_red * P["C9_red"])


def conjonction(d, b, c10_val=None, c10_compl=None, c12=None, var23=False, c13b=None):
    cs = conditions_sous_sacrifice(b, var23)
    c10_val = P["C10_val"] if c10_val is None else c10_val
    c10_compl = P["C10_compl"] if c10_compl is None else c10_compl
    c12 = P["C12"] if c12 is None else c12
    c13b = (1 - np.mean(b["non_lancee"])) if c13b is None else c13b
    hors = P["C4"] * P["C5"] * cs["c6"] * P["C7"] * cs["c8"] * cs["c9"] * P["C11"] * c12 * P["C13_tech"] * c13b
    audit = 1 - (1 - np.mean(d["audit"])) * (1 - autres)
    c14 = 1 - audit * P_ART
    ouverte = np.mean(d["m1"]) * hors * c10_val * c14
    compl = np.mean(d["besoin"]) * hors * c10_val * c14
    apres = ouverte + compl * (np.mean(d["ok_cumul"][d["besoin"]]) if d["besoin"].any() else 0) * (c10_compl / c10_val)
    return dict(hors=hors * c10_val, c14=c14, ouverte=ouverte, compl=compl, noeud=1 - ouverte - compl, apres=apres, cs=cs,
                c13b=c13b)


print("\n== CONJONCTION ENTIÈRE C1 à C14 (conditions hors juges indépendantes entre elles et des juges, SUPPOSÉ) ==")
d = M1[CAS_JUGES[0][0]]
R = conjonction(d, BUDGETS["base"])
print(f"  texte de base (D-g a, D-i 1 ; 45 ; 40) : C6 sous sacrifice {R['cs']['c6']:.3f} ; C8 {R['cs']['c8']:.3f} ; C9 {R['cs']['c9']:.3f} ; "
      f"C12 {P['C12']:.3f} ; C13 budget {R['c13b']:.4f} ; produit des conditions hors juges (C4 à C13) : {R['hors']:.2f}")
for nom, *_ in CAS_JUGES:
    dd = M1[nom]
    r = conjonction(dd, BUDGETS["base"])
    print(f"  {nom} : porte des juges seule (C1-C2) {np.mean(dd['c1c2']):.2f} ; C14 {r['c14']:.2f} ; "
          f"CONJONCTION ENTIÈRE ouverte d'emblée {r['ouverte']:.2f} ; complément proposé {r['compl']:.2f} ; "
          f"nœud d'emblée {r['noeud']:.2f} ; ouverte au total si le complément reçoit son GO {r['apres']:.2f}")
print(f"  sensibilités à la prédiction P1 : C13 technique à 1,00 -> ouverte d'emblée {R['ouverte'] / P['C13_tech']:.2f} ; "
      f"audit sans artefact (0) -> {R['ouverte'] / R['c14']:.2f} ; artefact 0,30 -> "
      f"{R['ouverte'] / R['c14'] * (1 - (1 - (1 - np.mean(d['audit'])) * (1 - autres)) * 0.30):.2f} ; "
      f"C12 à 0,99 (v5) -> {R['ouverte'] / P['C12'] * 0.99:.2f}")
print(f"  coûts aux bases (rapports à 1 : C13 budget = 1, aucun sacrifice) -> ouverte d'emblée "
      f"{R['ouverte'] / R['c13b'] * (P['C6'] * P['C8'] * P['C9']) / (R['cs']['c6'] * R['cs']['c8'] * R['cs']['c9']):.2f}")
for cle, val in P["C10"].items():
    if cle != C10_PRINCIPAL:
        print(f"  C10 selon « {cle[0]} », k = {cle[1]} ({val:.2f}) -> ouverte d'emblée {R['ouverte'] / P['C10_val'] * val:.2f}")
# Configurations : base sans arrêt ; recommandée avec et sans arrêt ; plafond 32
print("  -- configurations (prédiction P1) : porte d'emblée ; complément ; nœud ; au total ; C13 budget ; C6, C8, C9 sous sacrifice --")
RES = {}
for cle, var23, etiquette in (("base", False, "texte de base, 45 ; 40"),
                              ("base-sans-arret", False, "texte de base, 45 sans arrêt"),
                              ("rec", True, "RECOMMANDÉE (D-g b, D-i 2), 45 ; 40"),
                              ("rec-sans-arret", True, "RECOMMANDÉE, 45 sans arrêt"),
                              ("base-ordre-v5", False, "texte de base, ordre du script v5 (CP5-04)"),
                              ("base-ordre-b4", False, "texte de base, ordre du brouillon 4"),
                              ("base-m6-tot", False, "texte de base, M6 jouée juste après É1 (information)"),
                              ("rec-m6-tot", True, "RECOMMANDÉE, M6 jouée juste après É1 (information)")):
    b = BUDGETS[cle]
    ss_k, _ = c10(110 - b["depense"], 1)
    ss_ck, _ = c10(110 - b["depense"] - compl_cout, 1)
    RES[cle] = conjonction(d, b, c10_val=np.mean(ss_k >= 2), c10_compl=np.mean(ss_ck >= 2), var23=var23)
    r = RES[cle]
    print(f"  {etiquette} : ouverte d'emblée {r['ouverte']:.3f} ; complément {r['compl']:.3f} ; nœud {r['noeud']:.3f} ; "
          f"au total {r['apres']:.3f} ; C10 {np.mean(ss_k >= 2):.3f} (après complément {np.mean(ss_ck >= 2):.3f}) ; "
          f"C13 budget {r['c13b']:.4f} ; C6 {r['cs']['c6']:.3f} ; C8 {r['cs']['c8']:.3f} ; C9 {r['cs']['c9']:.3f}")
for cle, var23, etiquette in (("base-32", False, "texte de base, PLAFOND 32 ; 28 (information)"),
                              ("rec-32", True, "RECOMMANDÉE, PLAFOND 32 ; 28 (information)")):
    b = BUDGETS[cle]
    ss_k, _ = c10(110 - b["depense"], 1)
    ss_ck, _ = c10(110 - b["depense"] - compl_cout, 1)
    r = conjonction(d, b, c10_val=np.mean(ss_k >= 2), c10_compl=np.mean(ss_ck >= 2), var23=var23)
    print(f"  {etiquette} : C13 budget {r['c13b']:.3f} ; C10 {np.mean(ss_k >= 2):.2f} ; ouverte d'emblée {r['ouverte']:.2f} ; "
          f"complément {r['compl']:.2f} ; nœud {r['noeud']:.2f} ; au total {r['apres']:.2f} ; C6 {r['cs']['c6']:.3f} ; C8 {r['cs']['c8']:.3f}")
r_b = conjonction(d, BUDGETS["rec"], c12=P["C12_b"], var23=True)
print(f"  RECOMMANDÉE sous D-h (b) (deux bras, C12 {P['C12_b']:.3f}) : ouverte d'emblée {r_b['ouverte']:.3f} ; nœud {r_b['noeud']:.3f} ; "
      f"au total {r_b['apres']:.3f}")
print(f"  rappel v5 (ordre du script v5, M6 retirable entière, sans troncature, C12 0,99) : ouverte d'emblée 0,17 ; complément 0,20 ; "
      f"nœud 0,63 ; au total 0,22 ; rappel v4 : 0,17 ; 0,20 ; 0,63 ; 0,24 ; rappel v3 : 0,15 ; 0,15 ; 0,71 ; 0,20")
print("  défaut R-819 (pas d'étalonnage de l'aiguilleur) : C7 non étalonné -> conjonction entière 0,00 ; nœud certain")

# ================================================================ D-i : trois variantes du plan des fonds
print("\n== Décision D-i : variantes du plan des fonds (prédiction P1 ; D-g a ; 45 ; 40 ; coûts aux bases du devis v3, SUPPOSÉ) ==")
E2 = etapes_pre_pilote(delta_e3_base=d3_base2, delta_e3=2 * 0.057 * r_kj + 2 * 0.079 * r_ar,
                       delta_e4_base=d4_base2, delta_e4=4 * 0.057 * r_ai)
B2 = simuler_budget(E2, 45.0, 40.0)
ss2, _ = c10(110 - B2["depense"], 1)
ss2c, _ = c10(110 - B2["depense"] - compl_cout, 1)
R2 = conjonction(d, B2, c10_val=np.mean(ss2 >= 2), c10_compl=np.mean(ss2c >= 2), var23=True)
E3 = etapes_pre_pilote(delta_e1=-4 * 0.06)
B3 = simuler_budget(E3, 45.0, 40.0)
ss3, _ = c10(110 - B3["depense"], 1)
ss3c, _ = c10(110 - B3["depense"] - compl_cout, 1)
d3 = dict(m1=M1_VAR3["m1"], besoin=M1_VAR3["besoin"], audit=M1_VAR3["audit"], ok_cumul=d["ok_cumul"])
R3 = conjonction(d3, B3, c10_val=np.mean(ss3 >= 2), c10_compl=np.mean(ss3c >= 2), var23=True)
print(f"  (1) 28 fonds uniques (texte de base) : coût attendu {prot_base + sacr_base:.1f} USD ; paires PA : 0 ; "
      f"C1-C2 {np.mean(d['c1c2']):.2f} ; C6 {R['cs']['c6']:.3f} ; C13 budget {R['c13b']:.4f} ; C10 {P['C10_val']:.2f} ; "
      f"porte entière {R['ouverte']:.3f} ; nœud {R['noeud']:.2f} ; au total après complément {R['apres']:.3f}")
print(f"  (2) 28 fonds + 4 rendus appariés (mémoire seule, 4 lectures d'aiguilleur, aucun juge) : coût attendu "
      f"{prot_base + sacr_base + d3_base2 + d4_base2:.1f} USD (+{d3_base2 + d4_base2:.2f}) ; paires PA : 4 (≈ 2 en vérification) ; "
      f"C1-C2 {np.mean(d['c1c2']):.2f} (inchangé) ; C6 {R2['cs']['c6']:.3f} ; C13 budget {R2['c13b']:.4f} ; "
      f"C10 {np.mean(ss2 >= 2):.2f} ; porte entière {R2['ouverte']:.3f} ; nœud {R2['noeud']:.2f} ; au total {R2['apres']:.3f}")
print(f"  (3) 24 fonds dont 4 doublés (P 9, N 11, C 2, G 2 ; fiches P 11, N 13 ; 8 fiches corrélées) : coût attendu "
      f"{prot_base + sacr_base - 4 * 0.06:.1f} USD (−{4 * 0.06:.2f}) ; paires PA : 4 ; C1-C2 {np.mean(M1_VAR3['c1c2']):.2f} ; "
      f"C6 {R3['cs']['c6']:.3f} ; C13 budget {R3['c13b']:.4f} ; C10 {np.mean(ss3 >= 2):.2f} ; "
      f"porte entière {R3['ouverte']:.3f} ; nœud {R3['noeud']:.2f} ; au total {R3['apres']:.3f} "
      f"(graines v5 : l'écart de M1 avec (1) comprend le bruit de simulation, ±0,01 ; l'avance de (3) « au total » est dans ce bruit, CP5-11)")

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
# éloignement dans la bande avec 0,6 ; indépendants) — paramètres FICTIFS (CP5-07) : la prédiction P14 sera refaite
# par l'annexe avec ses paramètres réels, ce script rejoué, avant le scellement de l'annexe.
g = rng("v5-meta-profil")
for n_fiches in (6, 10):
    nich = g.integers(0, 6, (N_SIM, n_fiches))
    iu = np.triu_indices(n_fiches, 1)
    diff = (nich[:, iu[0]] != nich[:, iu[1]])
    prof = diff & (g.random((N_SIM, len(iu[0]))) < 0.5) & (g.random((N_SIM, len(iu[0]))) < 0.3) & \
        (g.random((N_SIM, len(iu[0]))) < 0.6)
    npf = prof.sum(1)
    print(f"  bras méta, {n_fiches} fiches, grille FICTIVE à 6 niches (SUPPOSÉ ; faible 0,5, forte 0,3, bande 0,6 ; à refaire "
          f"à l'annexe, CP5-07) : paires dans le profil médiane {np.median(npf):.0f}, P(zéro) {np.mean(npf == 0):.2f}, "
          f"P(toutes les fiches de même niche) {np.mean(~diff.any(1)):.3f}")
print("  note Gu-Krenn (modèle ou substitut) des trois paires et leur passage : rapportés sans test ; aucune comparaison "
      "entre bras au pré-pilote (une paire par bras) ; course à k = 1 : 12 fusions, erreur-type d'une aire sous la courbe "
      f"à 6 contre 6 ≈ {np.sqrt((0.5 * 0.5 + 5 * (0.5 / 1.5 - 0.25) + 5 * (2 * 0.25 / 1.5 - 0.25)) / 36):.2f} (Hanley-McNeil, à 0,5)")
print("fin ;", sys.version.split()[0])
