"""Calculs du devis v4 du pilote « oracles plantés » et constantes statistiques du brouillon 4 du préenregistrement.

Pièces servies : `prereg/mathematiques-nouvelles-v1/devis-pilote-generation-v4-brouillon.md` et
`preenregistrement-pilote-generation-v1-brouillon-4.md`. Copie adaptée du script v3
(`calculs-v3/calculs_devis_pilote_generation_v3.py`, 5d2b9d8a…), qui n'est pas modifié ; les blocs 0 à 6 reprennent
sa logique et ses profils sans changement, et sont recoupés contre les chiffres de sa sortie (efcbc21f…).

Ce que c'est : des produits de prix par des volumes de jetons SUPPOSÉS et par des nombres d'appels ; des bornes et
des niveaux exacts (lois binomiales). Aucune donnée d'expérience, aucun tirage aléatoire (donc aucune graine), aucun
appel réseau. Chaque chiffre écrit au devis v4 ou au brouillon 4 est mis en regard du chiffre recalculé.

Écrit par la session du concepteur (classe B : à rejouer et à vérifier par le contre-lecteur du devis).

Prix : relevés du 22 novembre 2026, `docs/notes/mathematiques-nouvelles-v1/releves-prix-et-source-score-apparie-v1.md`
(sha256 a7d9073f360b12f2fa914e49d1fd8d56acef86dc81136a494d962c96b2131218), palier standard, pages sans compte.

Lancer (depuis la racine du dépôt) :
  python -I prereg/mathematiques-nouvelles-v1/calculs-v4/calculs_devis_pilote_generation_v4.py \
      > prereg/mathematiques-nouvelles-v1/calculs-v4/sortie-calculs-devis-pilote-generation-v4.txt
(`scipy` requis pour le bloc 12 ; versions de `requirements-cpu.txt`.)
"""
from __future__ import annotations

import math

from scipy import stats

# ---------------------------------------------------------------------------------------------------
# 0. Prix relevés (USD par million de jetons : entrée, sortie)
# ---------------------------------------------------------------------------------------------------
PRIX = {
    "opus55": (4.0, 20.0),      # relevé, `claude-opus-5-5`
    "argon_nov": (2.0, 10.0),   # relevé, `gemini-4-argon`, jusqu'au 30 novembre 2026
    "argon_dec": (4.0, 20.0),   # relevé, dès le 1er décembre 2026
    "kimi": (2.0, 10.0),        # relevé, `kimi-k3.1-pro`
    "astra": (8.0, 40.0),       # relevé, `gpt-6.2-astra`, ≤ 272 000 jetons d'entrée
}
MACHINE_OBSERVE = 0.28          # USD/h, repris du devis v1, non relevé à neuf (SUPPOSÉ)
MACHINE_BORNE_HAUTE = 1.30      # USD/h, repris du devis v1, non relevé à neuf (SUPPOSÉ)


def cout(modele: str, entree_k: float, sortie_k: float) -> float:
    pe, ps = PRIX[modele]
    return (entree_k * 1000 * pe + sortie_k * 1000 * ps) / 1e6


# ---------------------------------------------------------------------------------------------------
# 1. Effectifs (inchangés depuis le devis v3)
# ---------------------------------------------------------------------------------------------------
MONDES = 12
PROP_OPUS_PAR_MONDE = 12 + 24
PROP_ARGON_PAR_MONDE = 12
ANALYSES_S_N = 150
TEMOINS_SERVIS_PAR_MONDE = 4
REDOUBLES = 10
REFORMULATIONS = 40
JUGEMENTS = 60                  # 40 connus + 20 énoncés faux de mondes (brouillon 4)
FUMEE_DEVIS = 0.10              # forfait SUPPOSÉ

prop_opus = MONDES * PROP_OPUS_PAR_MONDE
prop_argon = MONDES * PROP_ARGON_PAR_MONDE
temoins_servis = MONDES * TEMOINS_SERVIS_PAR_MONDE
items_par_bras = ANALYSES_S_N + temoins_servis + REDOUBLES

# ---------------------------------------------------------------------------------------------------
# 2. Profils de jetons SUPPOSÉS (milliers : entrée, sortie), repris du devis v1 par le v3, inchangés
# ---------------------------------------------------------------------------------------------------
SC = ("bas", "attendu", "pire")
PROFIL_PROPOSITION = {"bas": (3.0, 1.5), "attendu": (10.0, 3.0), "pire": (20.0, 12.0)}
PROFIL_S_AGENT = {"bas": (20.0, 3.0), "attendu": (40.0, 6.0), "pire": (150.0, 30.0)}
PROFIL_S_RELECTEUR = {"bas": (3.0, 1.0), "attendu": (4.0, 2.0), "pire": (6.0, 6.0)}
PLAFOND_AGENT_S = 1.50
PROFIL_N = {"bas": (3.0, 2.0), "attendu": (4.0, 6.0), "pire": (4.0, 24.0)}
PROFIL_JUGE = {"bas": (6.0, 2.0), "attendu": (8.0, 4.0), "pire": (12.0, 12.0)}
PROFIL_REFORMULATEUR = {"bas": (4.0, 2.0), "attendu": (6.0, 3.0), "pire": (8.0, 8.0)}
HEURES_MACHINE = {"bas": 12.0, "attendu": 24.0, "pire": 48.0}
# Protocole P d'antériorité (brouillon 4, § Antériorité) : profils SUPPOSÉS, écrits au devis v4, § 7
P_QUESTIONS = 5
P_PIECES_PAR_QUESTION = 8
P_CITANTS_PAR_QUESTION = 2
PROFIL_P_LECTURE = {"bas": (20.0, 2.0), "attendu": (40.0, 3.0), "pire": (150.0, 6.0)}   # une pièce lue en entier
PROFIL_P_REQUETES = {"bas": (4.0, 2.0), "attendu": (10.0, 3.0), "pire": (30.0, 6.0)}   # requêtes ou tri, par appel
P_APPELS_REQUETES_PAR_QUESTION = 2
P_SECOND_LECTEUR_PIECES = {"bas": 0, "attendu": 10, "pire": None}   # None : toutes les pièces lues

ecarts: list[tuple[str, float, float]] = []


def f(x: float) -> str:
    return f"{x:,.4f}".replace(",", " ")


def ligne(nom: str, ecrit: float | None, script: float, tol: float = 0.005) -> None:
    if ecrit is None:
        print(f"   {nom:78s} écrit    —     script {f(script):>10s}")
        return
    e = script - ecrit
    marque = "" if abs(e) <= tol else "   <<< ÉCART"
    print(f"   {nom:78s} écrit {ecrit:10.4f}  script {f(script):>10s}  écart {e:+.4f}{marque}")
    if abs(e) > tol:
        ecarts.append((nom, ecrit, script))


print("Calculs du devis v4 du pilote « oracles plantés » et constantes du brouillon 4 — calculs v4")
print("Montants en USD. Tolérance d'arrondi : 0,005 (au centime). Profils de jetons SUPPOSÉS (repris du v1).")
print("Colonne « écrit » : chiffre porté au devis v4 ou au brouillon 4. Blocs 0 à 6 : reprise du script v3.")
print()
print("Bloc 0 — prix relevés (entrée / sortie, par million)")
for k, (pe, ps) in PRIX.items():
    print(f"   {k:18s} {pe:5.2f} / {ps:5.2f}")
print(f"   machine observée {MACHINE_OBSERVE:.2f} USD/h ; borne haute {MACHINE_BORNE_HAUTE:.2f} USD/h (repris du v1)")
print()

print("Bloc 1 — effectifs")
ligne("propositions Opus 12 × (12 + 24)", 432, prop_opus)
ligne("propositions Argon 12 × 12", 144, prop_argon)
ligne("items par bras S et N (150 + 48 + 10)", 208, items_par_bras)
ligne("reformulations", 40, REFORMULATIONS)
ligne("jugements (40 connus + 20 énoncés faux de mondes)", 60, JUGEMENTS)
print()

print("Bloc 2 — coûts unitaires")
unit: dict[str, dict[str, float]] = {}
for sc in SC:
    e, s = PROFIL_PROPOSITION[sc]
    unit.setdefault("prop_opus", {})[sc] = cout("opus55", e, s)
    unit.setdefault("prop_argon_nov", {})[sc] = cout("argon_nov", e, s)
    unit.setdefault("prop_argon_dec", {})[sc] = cout("argon_dec", e, s)
    agent = min(cout("opus55", *PROFIL_S_AGENT[sc]), PLAFOND_AGENT_S)
    unit.setdefault("item_S", {})[sc] = agent + cout("kimi", *PROFIL_S_RELECTEUR[sc])
    unit.setdefault("item_N", {})[sc] = cout("opus55", *PROFIL_N[sc])
    unit.setdefault("reformulation_kimi", {})[sc] = cout("kimi", *PROFIL_REFORMULATEUR[sc])
    unit.setdefault("jugement_astra", {})[sc] = cout("astra", *PROFIL_JUGE[sc])
ECRIT_UNIT = {
    "prop_opus": (0.042, 0.10, 0.32), "prop_argon_nov": (0.021, 0.05, 0.16), "prop_argon_dec": (0.042, 0.10, 0.32),
    "item_S": (0.156, 0.308, 1.272), "item_N": (0.052, 0.136, 0.496),
    "reformulation_kimi": (0.028, 0.042, 0.096), "jugement_astra": (0.128, 0.224, 0.576),
}
for k, vals in ECRIT_UNIT.items():
    for i, sc in enumerate(SC):
        ligne(f"{k} [{sc}]", vals[i], unit[k][sc], tol=0.0005)
print()

print("Bloc 4 — postes et totaux (périmètre du brouillon 4 : bras S et N courus)")
poste = {sc: {} for sc in SC}
for sc in SC:
    poste[sc]["P1"] = REFORMULATIONS * unit["reformulation_kimi"][sc] + JUGEMENTS * unit["jugement_astra"][sc]
    poste[sc]["P2_nov"] = prop_opus * unit["prop_opus"][sc] + prop_argon * unit["prop_argon_nov"][sc]
    poste[sc]["P2_dec"] = prop_opus * unit["prop_opus"][sc] + prop_argon * unit["prop_argon_dec"][sc]
    poste[sc]["P3_S"] = items_par_bras * unit["item_S"][sc]
    poste[sc]["P3_N"] = items_par_bras * unit["item_N"][sc]
    poste[sc]["total_nov"] = poste[sc]["P1"] + poste[sc]["P2_nov"] + poste[sc]["P3_S"] + poste[sc]["P3_N"] + FUMEE_DEVIS
    poste[sc]["total_dec"] = poste[sc]["P1"] + poste[sc]["P2_dec"] + poste[sc]["P3_S"] + poste[sc]["P3_N"] + FUMEE_DEVIS
    prix_h = MACHINE_OBSERVE if sc != "pire" else MACHINE_BORNE_HAUTE
    poste[sc]["P4"] = HEURES_MACHINE[sc] * prix_h
ECRIT_POSTES = {
    "P1": (8.80, 15.12, 38.40), "P2_nov": (21.17, 50.40, 161.28), "P2_dec": (24.19, 57.60, 184.32),
    "P3_S": (32.45, 64.06, 264.58), "P3_N": (10.82, 28.29, 103.17),
    "total_nov": (73.33, 157.97, 567.52), "total_dec": (76.36, 165.17, 590.56), "P4": (3.36, 6.72, 62.40),
}
for k, vals in ECRIT_POSTES.items():
    for i, sc in enumerate(SC):
        ligne(f"{k} [{sc}]", vals[i], poste[sc][k])
for i, sc in enumerate(SC):
    ligne(f"appels (1er déc.) + machine [{sc}]", (79.72, 171.89, 652.96)[i], poste[sc]["total_dec"] + poste[sc]["P4"])
    ligne(f"appels (30 nov.) + machine [{sc}]", (76.69, 164.69, 629.92)[i], poste[sc]["total_nov"] + poste[sc]["P4"])
for i, sc in enumerate(SC):
    ligne(f"écart d'un jour de prix d'Argon à l'autre [{sc}]", (3.02, 7.20, 23.04)[i],
          poste[sc]["total_dec"] - poste[sc]["total_nov"])
print()

print("Bloc 5 — lignes conditionnelles (attendu, Argon 4/20)")
prop_par_monde = (prop_opus + prop_argon) / MONDES
cond_connus = poste["attendu"]["P1"]
cond_monde = prop_par_monde * unit["prop_opus"]["attendu"] + (items_par_bras / MONDES) * (
    unit["item_S"]["attendu"] + unit["item_N"]["attendu"])
att_cond = poste["attendu"]["total_dec"] + cond_connus + cond_monde
ligne("banque de connus refaite une fois", 15.12, cond_connus)
ligne("un monde régénéré et rejoué", 12.50, cond_monde)
ligne("attendu avec lignes conditionnelles", 192.79, att_cond)
print()

print("Bloc 7 — réserve des appels en vol (v4) et plafond d'appels")
print("   créneaux tenus par le harnais (brouillon 4, A6) : trois items S, deux autres appels, un jugement.")
relecteur_pire = {"kimi": cout("kimi", *PROFIL_S_RELECTEUR["pire"]), "argon 4/20 (repli R1)": cout("argon_dec", *PROFIL_S_RELECTEUR["pire"])}
for k, v in relecteur_pire.items():
    print(f"   relecteur de S au pire, {k} : {f(v)}")
item_s_creneau = PLAFOND_AGENT_S + max(relecteur_pire.values())
autres = {"proposition Opus ou Argon 4/20": unit["prop_opus"]["pire"], "item N": unit["item_N"]["pire"],
          "reformulation Kimi": unit["reformulation_kimi"]["pire"],
          "reformulation Argon 4/20 (repli R1)": cout("argon_dec", *PROFIL_REFORMULATEUR["pire"])}
for k, v in autres.items():
    print(f"   autre appel au pire, {k} : {f(v)}")
autre_creneau = max(autres.values())
jugements_pire = {"Astra": unit["jugement_astra"]["pire"], "Kimi (repli R1)": cout("kimi", *PROFIL_JUGE["pire"])}
for k, v in jugements_pire.items():
    print(f"   jugement au pire, {k} : {f(v)}")
jugement_creneau = max(jugements_pire.values())
ligne("créneau d'un item S (agent au plafond 1,50 + relecteur au pire, replis compris)", 1.644, item_s_creneau, tol=0.0005)
ligne("créneau d'un autre appel (proposition, item N ou reformulation, au pire)", 0.496, autre_creneau, tol=0.0005)
ligne("créneau d'un jugement (au pire)", 0.576, jugement_creneau, tol=0.0005)
reserve_v4 = 3 * item_s_creneau + 2 * autre_creneau + jugement_creneau
ligne("réserve v4 = 3 × 1,644 + 2 × 0,496 + 0,576", 6.50, reserve_v4)
reserve_v3 = 3 * (PLAFOND_AGENT_S + relecteur_pire["kimi"]) + 2 * unit["prop_opus"]["pire"] + unit["jugement_astra"]["pire"]
ligne("réserve v3 (pour mémoire : ni item N en vol, ni repli R1)", 5.93, reserve_v3)
ligne("remarque 19 : 192,79 × 1,5 + 5,93 (valeurs exactes)", 295.11, att_cond * 1.5 + reserve_v3)
brut = att_cond * 1.5 + reserve_v4
ligne("192,79 × 1,5 + réserve v4 6,50 (valeurs exactes)", 295.68, brut)
plafond = math.ceil(brut / 10) * 10
ligne("plafond d'appels (dizaine supérieure)", 300, plafond)
plafond_machine = math.ceil(HEURES_MACHINE["pire"] * MACHINE_BORNE_HAUTE / 5) * 5
ligne("machine 48 h × 1,30 (non arrondi)", 62.40, HEURES_MACHINE["pire"] * MACHINE_BORNE_HAUTE)
ligne("plafond machine (arrondi aux 5 supérieurs)", 65, plafond_machine)
ligne("somme des plafonds", 365, plafond + plafond_machine)
ligne("marge du plafond sur l'attendu avec conditionnelles", 107.21, plafond - att_cond)
ligne("marge du plafond sur l'attendu simple (1er déc.)", 134.83, plafond - poste["attendu"]["total_dec"])
ligne("rapport plafond / attendu simple (1er déc.)", 1.82, plafond / poste["attendu"]["total_dec"], tol=0.005)
ligne("rapport pire / attendu (1er déc.)", 3.58, poste["pire"]["total_dec"] / poste["attendu"]["total_dec"], tol=0.005)
print(f"   pire des appels (1er déc.) {poste['pire']['total_dec']:.2f} > plafond {plafond} : la coupure A6 joue avant le pire cas "
      f"({'vrai' if poste['pire']['total_dec'] > plafond else 'FAUX'})")
print()

print("Bloc 8 — intervalle de P7 (inchangé)")
ligne("borne basse (120 / 164,28) × attendu 30 nov.", 115.39, 120 / 164.28 * poste["attendu"]["total_nov"])
ligne("borne haute (260 / 164,28) × attendu 1er déc.", 261.41, 260 / 164.28 * poste["attendu"]["total_dec"])
print()

print("Bloc 9 — garde de projection des coûts (brouillon 4, A14) : douze blocs d'un monde")
print("   avant le premier bloc : fumée et 40 reformulations ; un bloc : 48 propositions, 1/12 des items de chaque bras")
print("   (le premier bloc en compte 18), 5 jugements. Argon à 4/20.")
ITEMS_BLOC_1 = math.ceil(items_par_bras / MONDES)
JUG_BLOC = JUGEMENTS // MONDES
fin_bloc_1 = {}
for sc in SC:
    fin_bloc_1[sc] = (FUMEE_DEVIS + REFORMULATIONS * unit["reformulation_kimi"][sc]
                      + PROP_OPUS_PAR_MONDE * unit["prop_opus"][sc] + PROP_ARGON_PAR_MONDE * unit["prop_argon_dec"][sc]
                      + ITEMS_BLOC_1 * (unit["item_S"][sc] + unit["item_N"][sc]) + JUG_BLOC * unit["jugement_astra"][sc])
ligne("items de chaque bras au premier bloc", 18, ITEMS_BLOC_1)
ligne("jugements par bloc", 5, JUG_BLOC)
for i, sc in enumerate(SC):
    ligne(f"dépense à la fin du premier bloc [{sc}]", (7.62, 15.69, 54.00)[i], fin_bloc_1[sc])
seuil_projection = plafond - reserve_v4
ligne("seuil de la projection = plafond − réserve", 293.50, seuil_projection)
for sc in SC:
    proj = poste[sc]["total_dec"]
    print(f"   projection au profil « {sc} » : {proj:.2f} → {'arrêt avant le deuxième bloc' if proj > seuil_projection else 'la course continue'}")
variable_att = poste["attendu"]["total_dec"] - FUMEE_DEVIS
facteur = (seuil_projection - FUMEE_DEVIS) / variable_att
ligne("facteur de dépassement des coûts unitaires toléré par la projection", 1.78, facteur, tol=0.005)
ligne("économie si le profil « pire » se révèle au premier bloc (300 − dépense)", 246.00, plafond - fin_bloc_1["pire"])
print()

print("Bloc 10 — protocole P d'antériorité, ligne à part (profils SUPPOSÉS ; lecteur Astra 8/40, second lecteur Kimi 2/10)")
pieces_min = P_QUESTIONS * P_PIECES_PAR_QUESTION
pieces_max = P_QUESTIONS * (P_PIECES_PAR_QUESTION + P_CITANTS_PAR_QUESTION)
ligne("pièces lues, au plus 8 par question", 40, pieces_min)
ligne("pièces lues avec au plus 2 citants par question", 50, pieces_max)
appels_req = P_QUESTIONS * P_APPELS_REQUETES_PAR_QUESTION
ligne("appels de requêtes et de tri (2 par question)", 10, appels_req)
p_unit = {sc: cout("astra", *PROFIL_P_LECTURE[sc]) for sc in SC}
p_req = {sc: cout("astra", *PROFIL_P_REQUETES[sc]) for sc in SC}
p_kimi = {sc: cout("kimi", *PROFIL_P_LECTURE[sc]) for sc in SC}
for i, sc in enumerate(SC):
    ligne(f"lecture d'une pièce par Astra [{sc}]", (0.24, 0.44, 1.44)[i], p_unit[sc], tol=0.0005)
for i, sc in enumerate(SC):
    ligne(f"appel de requêtes ou de tri par Astra [{sc}]", (0.112, 0.20, 0.48)[i], p_req[sc], tol=0.0005)
for i, sc in enumerate(SC):
    ligne(f"lecture d'une pièce par Kimi [{sc}]", (0.06, 0.11, 0.36)[i], p_kimi[sc], tol=0.0005)
p_total = {
    "bas": pieces_min * p_unit["bas"] + appels_req * p_req["bas"] + 0 * p_kimi["bas"],
    "attendu": pieces_max * p_unit["attendu"] + appels_req * p_req["attendu"] + 10 * p_kimi["attendu"],
    "pire": pieces_max * p_unit["pire"] + appels_req * p_req["pire"] + pieces_max * p_kimi["pire"],
}
for i, sc in enumerate(SC):
    ligne(f"protocole P, total [{sc}]", (10.72, 25.10, 94.80)[i], p_total[sc])
p_plafond = math.ceil(p_total["attendu"] * 1.5 / 10) * 10
ligne("protocole P : attendu × 1,5 (non arrondi)", 37.65, p_total["attendu"] * 1.5)
ligne("protocole P : plafond (dizaine supérieure)", 40, p_plafond)
ligne("protocole P : pire cas du prochain appel (une lecture par Astra au pire)", 1.44, p_unit["pire"], tol=0.0005)
ligne("protocole P, lecteur Astra seul, attendu (sans second lecteur)", 24.00, pieces_max * p_unit["attendu"] + appels_req * p_req["attendu"])
ligne("protocole P, lecteur Kimi seul, attendu", 6.00,
      pieces_max * p_kimi["attendu"] + appels_req * cout("kimi", *PROFIL_P_REQUETES["attendu"]))
print()

print("Bloc 11 — options de périmètre soumises au directeur (Argon 4/20 ; même règle de plafond)")


def option(nom, avec_s: bool, avec_n: bool, ecrit):
    tot = {}
    for sc in SC:
        tot[sc] = (poste[sc]["P1"] + poste[sc]["P2_dec"] + FUMEE_DEVIS
                   + (poste[sc]["P3_S"] if avec_s else 0.0) + (poste[sc]["P3_N"] if avec_n else 0.0))
    monde = prop_par_monde * unit["prop_opus"]["attendu"] + (items_par_bras / MONDES) * (
        (unit["item_S"]["attendu"] if avec_s else 0.0) + (unit["item_N"]["attendu"] if avec_n else 0.0))
    cond = tot["attendu"] + cond_connus + monde
    autre = max(unit["prop_opus"]["pire"], unit["item_N"]["pire"] if avec_n else 0.0,
                cout("argon_dec", *PROFIL_REFORMULATEUR["pire"]))
    res = (3 * item_s_creneau if avec_s else 0.0) + 2 * autre + jugement_creneau
    brut_o = cond * 1.5 + res
    plaf = math.ceil(brut_o / 10) * 10
    mach = plafond_machine if avec_s else 0
    print(f"   {nom}")
    ligne("      total des appels [bas]", ecrit[0], tot["bas"])
    ligne("      total des appels [attendu]", ecrit[1], tot["attendu"])
    ligne("      total des appels [pire]", ecrit[2], tot["pire"])
    ligne("      attendu avec lignes conditionnelles", ecrit[3], cond)
    ligne("      réserve des appels en vol", ecrit[4], res)
    ligne("      plafond d'appels (dizaine supérieure)", ecrit[5], plaf)
    ligne("      plafond machine", ecrit[6], mach)
    return tot


t_a = option("(a) périmètre du brouillon 4 : S et N courus", True, True, (76.36, 165.17, 590.56, 192.79, 6.50, 300, 65))
t_b = option("(b) sans le bras N", True, False, (65.54, 136.88, 487.40, 162.14, 6.15, 250, 65))
t_c = option("(c) sans les bras S et N (aucune machine louée)", False, False, (33.09, 72.82, 222.82, 92.74, 1.22, 150, 0))
ligne("économie attendue de (b) sur (a)", 28.29, t_a["attendu"] - t_b["attendu"])
ligne("économie attendue de (c) sur (a)", 92.35, t_a["attendu"] - t_c["attendu"])
ligne("part des bras S et N dans l'attendu de (a)", 0.559, (t_a["attendu"] - t_c["attendu"]) / t_a["attendu"], tol=0.0005)
print()

print("Bloc 12 — constantes statistiques du brouillon 4 (lois exactes ; scipy.stats)")
print("   test exact des signes de H2 : plus petit k tel que P(Binomiale(n, 1/2) ≥ k) ≤ 0,025")
ECRIT_K = {12: (10, 0.0193), 11: (10, 0.0059), 10: (9, 0.0107), 9: (8, 0.0195), 8: (8, 0.0039)}
for n, (k_ecrit, niveau_ecrit) in ECRIT_K.items():
    k = next(k for k in range(n + 2) if stats.binom.sf(k - 1, n, 0.5) <= 0.025)
    ligne(f"n = {n} : k", k_ecrit, k, tol=0)
    ligne(f"n = {n} : niveau réalisé P(≥ k)", niveau_ecrit, float(stats.binom.sf(k - 1, n, 0.5)), tol=0.00005)
print("   bornes hautes de Clopper–Pearson unilatérales à 97,5 %")


def cp_haut(x, n, niveau=0.975):
    return 1.0 if x == n else float(stats.beta.ppf(niveau, x + 1, n - x))


def cp_bas(x, n, niveau=0.975):
    return 0.0 if x == 0 else float(stats.beta.ppf(1 - niveau, x, n - x + 1))


for (x, n), v in {(2, 75): 0.0930, (3, 75): 0.1125, (0, 40): 0.0881, (0, 20): 0.1684, (2, 20): 0.3170}.items():
    ligne(f"{x} sur {n} : borne haute", v, cp_haut(x, n), tol=0.00005)
print("   score apparié en Δ0 = 0 (McNemar) : plus petit n10 tel que (n10 − n01) / √(n10 + n01) ≥ 2,2504")
ZSTAR = 2.2504


def score(n10, n01, n, d0):
    a = 2 * n
    b = -n10 - n01 + (2 * n - n10 + n01) * d0
    c = -n01 * d0 * (1 - d0)
    q = (math.sqrt(b * b - 4 * a * c) - b) / (2 * a)
    return (n10 - n01 - n * d0) / math.sqrt(n * (2 * q + d0 * (1 - d0)))


for n01, ecrit in {0: 6, 1: 8, 2: 10, 3: 12}.items():
    n10 = next(k for k in range(n01 + 1, 76) if score(k, n01, 75, 0.0) >= ZSTAR)
    ligne(f"n01 = {n01} : plus petit n10", ecrit, n10, tol=0)
ligne("contrôle : S(0) pour n10 = 6, n01 = 0 égale √6", math.sqrt(6), score(6, 0, 75, 0.0), tol=1e-9)
ligne("contrôle : S(0) pour n10 = 9, n01 = 2 égale 7/√11", 7 / math.sqrt(11), score(9, 2, 75, 0.0), tol=1e-9)
print("   plancher « instances aveugles » (sonde sur 41 racines d'essai : 60 à 68 touches sur 75 faux, soit 7 à 15 faux non touchés)")
for non_touches in (7, 12, 15):
    print(f"      {non_touches} faux hors de portée de la règle aveugle : « S dépasse la règle aveugle » exige au moins 6 d'entre eux "
          f"vérifiés par S sans aucune perte ailleurs (soit {6 / non_touches:.2f} de ce reste), 8 avec une perte, 10 avec deux")
print()

print(f"Bilan : {len(ecarts)} écart(s) supérieur(s) à la tolérance")
for nom, d, s in ecarts:
    print(f"   {nom} : écrit {d} ; script {s:.4f}")
