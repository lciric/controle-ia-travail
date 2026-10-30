"""Calculs de puissance du pré-pilote de la course 2, brouillon 4. Processeur seul, aucune donnée de run.
Remplace calcul-puissance-pre-pilote-course-2-v3.py (gardé, R12). Ce qui change par rapport à la v3 (décisions R-630 à R-643) :
  - R-632 / R-634 : pré-pilote recentré sur les instruments de plausibilité ; la mesure M2 (auto-préférence, dix fonds
    écrits deux fois) est RETIRÉE : la section « M2 : résolution selon k » disparaît ; l'alarme S5 ne compte plus parmi
    les déclencheurs d'audit de C14 ; les 28 témoins sont 28 fonds rendus UNE fois chacun (aucun appariement :
    plan M1 sans fonds appariés, rho sans objet) ; le complément devient 24 fonds rendus une fois (P 12, N 12) ;
  - R-638 / R-639 / R-642 / R-643 : bisociation à TROIS bras — bras méta (v1), bras Gu-Krenn, bras basique « loin en
    domaine, proche en concept » ; le bras hasard est retiré ; une paire par bras (S23 k = 1, 3 fusions) ;
  - R-635 / R-636 : le bras Gu-Krenn est gardé sans condition de reproduction (substitut par traits publiés si leur modèle
    ne tourne pas à temps) : la ligne « deux bras seulement (Gu-Krenn retiré) » disparaît ;
  - R-630 : plafond du pré-pilote relevé à 45 USD (recommandation), arrêt d'étape proposé 40 USD (À GELER) ; C13 budget
    et C10 recalculés ; C10 lue sous deux hypothèses (reste = 110 − dépense ; reste = 78 inchangé) : LECTURE À CONFIRMER ;
  - coût : trois lectures d'étiquettes par fiche (liste fermée, vocabulaire Gu-Krenn, grille des niches) au lieu de deux
    (0,25 par lecture et par dix fiches, prorata de la v3) ; rédacteur : dix squelettes et déclarations de plus (SUPPOSÉ,
    prorata grossier, à confirmer au devis v4 de session-depot).
Hypothèses déclarées dans le préenregistrement (brouillon 4) ; valeurs supposées marquées SUPPOSÉ.
Graines : SeedSequence(RACINE, spawn_key=(cle_de_tache(nom),)), même dérivation que src/controle_ia/manifeste.py (R9).
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


def cle_de_tache(nom):
    return int.from_bytes(hashlib.sha256(nom.encode("utf-8")).digest()[:8], "big")


def rng(nom):
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=(cle_de_tache(nom),)))


print(f"python {platform.python_version()} ; numpy {np.__version__} ; scipy {scipy.__version__} ; racine {RACINE} ; "
      f"tirages {N_SIM}")
print("seuils utilisés :", ", ".join(f"{k}={v}" for k, v in SEUILS.items()))

# ================================================================ Mesure 1, simulation jointe des trois juges
# Plan (brouillon 4, R-634 : plus de fonds appariés) : 28 fonds rendus une fois chacun -> P 10 fiches, N 13, C 3, G 2.
# Un juge de justesse vraie v a raison sur une fiche avec probabilité v, indépendamment d'une fiche à l'autre. Juges
# indépendants entre eux à fiches données (SUPPOSÉ ; une difficulté commune par fiche rendrait la porte M1 plus
# probable et le kappa plus haut). Rejet des C (hors consigne) : 0,30 par fiche et par juge (prédiction P2).
# La fonction justesse garde la forme de la v3 (fonds appariés à corrélation rho) pour la comparaison ; n_app = 0 ici.
RHO = 0.6
REJET_C = 0.30
PLAN = ((0, 10), (0, 13))            # (P appariés, P simples), (N appariés, N simples)
PLAN_COMPL = ((0, 12), (0, 12))      # complément : 24 fonds rendus une fois (P 12, N 12)
PLAN_V3 = ((4, 2), (5, 3))           # rappel : plan apparié de la v3 (comparaison seulement)


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


print("\n== M1, un juge seul : 28 fonds rendus une fois (P 10, N 13), sans appariement (R-634) ==")
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
    print(f"  juge vrai à {v:.2f} : étalonné {np.mean(a == 2):.2f}, défaillant {np.mean(a == 0):.2f} ; "
          f"après exclusion d'ambigus (P 8, N 10) : étalonné {np.mean(a8 == 2):.2f} ; "
          f"étalonné au total après complément (P 22, N 25) {np.mean((a == 2) | ((a == 1) & (ac == 2))):.2f} ; "
          f"rappel v3 (plan apparié, rho 0,6) : étalonné {np.mean(av == 2):.2f}")

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

# C6 : mémoire (rappel global sur ≈ 14 positifs) et union de l'axe 7 (12 paraphrases) non défaillantes.
# Sans fonds appariés, les 10 paires inter-fournisseurs PA disparaissent : positifs = PB 18 seules (≈ 9 en vérification).
mem_def = stats.binom.cdf(5, 9, 0.85)           # rappel < 0,60 sur 9 <=> au plus 5
ax7_def = stats.binom.cdf(5, 12, 0.75)          # rappel < 0,50 sur 12 <=> au plus 5
fa_def = 1 - stats.binom.cdf(int(np.floor(250 * 0.20)), 250, 0.06)
P["C6"] = (1 - mem_def) * (1 - ax7_def) * (1 - fa_def)
print(f"  C6 mémoire et axe 7 non défaillantes : {P['C6']:.3f} (P6 : rappel 0,85 sur ≈ 9 positifs de vérification "
      f"(PB seules, plus de paires PA), fausses alertes 0,06 sur 250 ; P7 : union 0,75 sur 12)")
print(f"    rappel v3 (≈ 14 positifs, PA comprises) : {(1 - stats.binom.cdf(8, 14, 0.85)) * (1 - ax7_def) * (1 - fa_def):.3f}")

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
    return et_direct, a_corr, defa, et_direct | (a_corr & essai_ok)


g = rng("v4-c7")
d, a, f, et = m4(g, N_SIM, (0.96, 0.96, 0.96, 0.80))
P["C7"] = np.mean(et)
print(f"  C7 aiguilleur étalonné : direct {np.mean(d):.2f}, à corriger {np.mean(a):.2f}, défaillant {np.mean(f):.2f} ; "
      f"étalonné après nouvel essai {P['C7']:.2f} (P8 : 0,96 en C1-C3, 0,80 en C4, SUPPOSÉ ; concrets écrits)")
d2, a2, f2, et2 = m4(g, N_SIM, (0.92, 0.92, 0.92, 0.92))
print(f"    sensibilité, 0,92 dans chaque classe : direct {np.mean(d2):.2f} ; après nouvel essai {np.mean(et2):.2f} ; "
      f"un nouvel essai d'une classe à 0,92 passe {0.92 ** 3:.2f}")
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
print(f"  C9 antériorité non défaillante : {P['C9']:.3f} (P10 : inventées 0,95) ; M6 « étalonnée » {m6_et:.2f} "
      f"(C9 accepte « non concluant »)")

# C10 et C13 (budget) : coûts. Rapports mesuré ÷ supposé log-normaux, médiane et intervalle à 80 % de P11.


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
# pré-pilote (bases du tableau de coût du brouillon 4) : 28 fonds rendus une fois (9 Kimi, 9 Argon, 10 T, SUPPOSÉ),
# rédacteur 3,2 (2,6 de la v3 + 10 squelettes et déclarations, SUPPOSÉ au prorata grossier), trois lectures d'étiquettes.
REDACTEUR, RENDUS_K, RENDUS_A, RENDUS_T = 3.2, 9, 9, 10
protege = (REDACTEUR * r_re + (RENDUS_K * 0.057 * r_kj + (RENDUS_A + RENDUS_T) * 0.079 * r_ar) + 1.4 * r_re + 2.0 * r_kp
           + (69 + 20) * 0.057 * r_ai + 0.3 * r_ai + 28 * (0.114 * r_op + 0.079 * r_ar + 0.057 * r_kj))
sacrifiable = (0.75 * r_op + 3 * 0.40 * r_fu + 3 * (0.114 * r_op + 0.079 * r_ar + 0.057 * r_kj) + 0.7 * r_op
               + 2.0 * r_kp + 2.0 * r_an)
# seconde version de témoins (A6, A7) : rédacteur 1,5 + rendus + relecteur 1,4 attendus, avec la probabilité
# qu'une première version échoue à C5 (calculée plus haut) ; passe par l'ordre de sacrifice
rendus_base = RENDUS_K * 0.057 + (RENDUS_A + RENDUS_T) * 0.079
v2_temoins = (g.random(N_SIM) < 1 - np.mean(ok_v[:, 0])) * (1.5 * r_re + (RENDUS_K * 0.057 * r_kj + (RENDUS_A + RENDUS_T) * 0.079 * r_ar) + 1.4 * r_re)
protege = protege + v2_temoins
total = protege + sacrifiable
budget_nm = protege > PLAFOND
P["C13_budget"] = 1 - np.mean(budget_nm)
depense = np.minimum(total, PLAFOND)
prot_base = REDACTEUR + rendus_base + 1.4 + 2.0 + 89 * 0.057 + 0.3 + 28 * 0.25
sacr_base = 0.75 + 1.2 + 3 * 0.25 + 0.7 + 2.0 + 2.0
print(f"  pré-pilote aux bases (rapports à 1) : protégé {prot_base:.1f} USD ; sacrifiable {sacr_base:.1f} USD ; total attendu "
      f"{prot_base + sacr_base:.1f} ; seconde version de témoins ≈ {1.5 + rendus_base + 1.4:.1f} USD si C5 échoue en première version")
print(f"  pré-pilote aux rapports prédits (P11), seconde version comprise : dépense médiane {np.median(total):.1f} USD ; "
      f"quantile 90 % {np.quantile(total, 0.9):.1f} ; P(un sacrifice au moins, total > {PLAFOND:.0f}) {np.mean(total > PLAFOND):.2f} ; "
      f"P(cumul atteint l'arrêt d'étape {SEUILS['S17_arret']:.0f}) {np.mean(total > SEUILS['S17_arret']):.2f} ; "
      f"P(étape protégée non lancée, « non mesuré (budget) ») {np.mean(budget_nm):.3f}")
print(f"    rappel v3 (plafond 32) : P(total > 32) {np.mean(total > 32):.2f} ; P(protégé > 32) {np.mean(protege > 32):.3f}")
# course : devis v3 § 3 (79 attendus, 4 sous-sessions) + bisociation à trois bras (méta, Gu-Krenn, basique)
fus_unit = 0.40 * r_fu + 0.057 * r_ai + 0.114 * r_op + 0.079 * r_ar + 0.057 * r_kj
P["C10"] = {}
for nom_reste, reste in (("reste = 110 − dépense (GO-2026-10-30-07 inchangé)", 110 - depense),
                         ("reste = 78 (plafond du pré-pilote relevé par une ligne séparée ; LECTURE À CONFIRMER)", np.full(N_SIM, 78.0))):
    for kc in (1, 2):
        course4 = (10 * r_kp + 18 * 1.0 + 1.75 + 6.5 * r_kj + 6.5 * r_ar + 18.3 * r_op + 10 * r_an + 7.3 * r_ai
                   + 3 * kc * 4 * fus_unit)
        ss = np.where(course4 <= reste, 4, np.where(0.75 * course4 <= reste, 3, np.where(0.5 * course4 <= reste, 2, 0)))
        P["C10"][(nom_reste, kc)] = np.mean(ss >= 2)
        print(f"  C10, {nom_reste}, course à S22 k = {kc} (trois bras, {3 * kc * 4} fusions) : devis refait médian "
              f"{np.median(course4):.1f} USD pour 4 sous-sessions ; reste médian {np.median(reste):.1f} ; tient à 4 "
              f"{np.mean(ss == 4):.2f}, à 3 {np.mean(ss == 3):.2f}, à 2 {np.mean(ss == 2):.2f}, à aucune {np.mean(ss == 0):.3f}")
C10_PRINCIPAL = ("reste = 110 − dépense (GO-2026-10-30-07 inchangé)", 1)   # lecture principale : S22 recommandé k = 1
P["C10_val"] = P["C10"][C10_PRINCIPAL]
print(f"    lecture principale de C10 (110 − dépense, k = 1) : {P['C10_val']:.2f}")
print(f"    M7 « poste refait » (un rapport > 1,30) : {np.mean((r_kj > 1.3) | (r_ar > 1.3) | (r_op > 1.3) | (r_an > 1.3) | (r_ai > 1.3) | (r_kp > 1.3) | (r_fu > 1.3)):.2f}"
      " (réserve, hors porte)")

P["C11"] = 0.99
P["C12"] = 0.99
P["C13_tech"] = 0.95
print(f"  C11 cloisons du tableau : {P['C11']:.2f} ; C12 garde de paire (trois bras : méta, Gu-Krenn, basique) : {P['C12']:.2f} "
      f"(SUPPOSÉ : programmes éprouvés en É0)")
print(f"  C13 arrêts clos et rien « non mesuré » : technique {P['C13_tech']:.2f} (SUPPOSÉ : A2, A3, A5, A11, A14 "
      f"clos dans les plafonds) × budget {P['C13_budget']:.3f}")

# C14 : aucun audit R4 ouvert ou audit rendu sans artefact. Déclencheurs hors M1 : relecteur à 100 % (ci-dessus),
# contradiction lecture primaire / chaîne (SUPPOSÉ 0,05). L'alarme S5 et « auto-préférence exactement nulle »
# disparaissent avec M2 (R-634). Probabilité qu'un audit déclenché conclue à un artefact : 0,15 (SUPPOSÉ).
P_ART = 0.15
autres = 1 - (1 - amb0) * (1 - 0.05)

# ================================================================ Conjonction entière
print("\n== CONJONCTION ENTIÈRE C1 à C14 (conditions hors juges indépendantes entre elles et des juges, SUPPOSÉ) ==")
hors_juges = P["C4"] * P["C5"] * P["C6"] * P["C7"] * P["C8"] * P["C9"] * P["C10_val"] * P["C11"] * P["C12"] * \
             P["C13_tech"] * P["C13_budget"]
print(f"  produit des conditions hors juges (C4 à C13, aiguilleur étalonné par concrets écrits) : {hors_juges:.2f}")
for nom, *_ in CAS_JUGES:
    d = M1[nom]
    audit = 1 - (1 - np.mean(d["audit"])) * (1 - autres)
    c14 = 1 - audit * P_ART
    ouverte = np.mean(d["m1"]) * hors_juges * c14
    compl = np.mean(d["besoin"]) * hors_juges * c14
    apres = ouverte + compl * (np.mean(d["ok_cumul"][d["besoin"]]) if d["besoin"].any() else 0)
    print(f"  {nom} : porte des juges seule (C1-C2) {np.mean(d['c1c2']):.2f} ; C14 {c14:.2f} ; "
          f"CONJONCTION ENTIÈRE ouverte d'emblée {ouverte:.2f} ; complément proposé {compl:.2f} ; "
          f"nœud d'emblée {1 - ouverte - compl:.2f} ; ouverte au total si le complément reçoit son GO {apres:.2f}")
d = M1[CAS_JUGES[0][0]]
c14_p1 = 1 - (1 - (1 - np.mean(d["audit"])) * (1 - autres)) * P_ART
print(f"  sensibilités à la prédiction P1 : C13 technique à 1,00 -> ouverte d'emblée "
      f"{np.mean(d['m1']) * hors_juges / P['C13_tech'] * c14_p1:.2f} ; "
      f"audit sans artefact (0) -> {np.mean(d['m1']) * hors_juges:.2f} ; artefact 0,30 -> "
      f"{np.mean(d['m1']) * hors_juges * (1 - (1 - (1 - np.mean(d['audit'])) * (1 - autres)) * 0.30):.2f}")
print(f"  coûts aux bases (rapports à 1 : étapes protégées sous le plafond, C13 budget = 1) -> ouverte d'emblée "
      f"{np.mean(d['m1']) * hors_juges / P['C13_budget'] * c14_p1:.2f}")
for cle, val in P["C10"].items():
    if cle != C10_PRINCIPAL:
        print(f"  C10 selon « {cle[0]} », k = {cle[1]} ({val:.2f}) -> ouverte d'emblée "
              f"{np.mean(d['m1']) * hors_juges / P['C10_val'] * val * c14_p1:.2f}")
print(f"  rappel v3 (plafond 32, fonds appariés, alarme S5 dans C14) : ouverte d'emblée 0,15 ; complément 0,15 ; nœud 0,71")
print("  défaut R-819 (pas d'étalonnage de l'aiguilleur) : C7 non étalonné -> conjonction entière 0,00 ; nœud certain")

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
print("  accord impact prédit (Gu-Krenn) / survie : descriptif ; 3 fusions au pré-pilote (aucun test) ; aucune comparaison "
      "entre bras au pré-pilote (une paire par bras) ; course à k = 1 : 12 fusions, erreur-type d'une aire sous la courbe "
      f"à 6 contre 6 ≈ {np.sqrt((0.5 * 0.5 + 5 * (0.5 / 1.5 - 0.25) + 5 * (2 * 0.25 / 1.5 - 0.25)) / 36):.2f} (Hanley-McNeil, à 0,5)")
print("fin ;", sys.version.split()[0])
