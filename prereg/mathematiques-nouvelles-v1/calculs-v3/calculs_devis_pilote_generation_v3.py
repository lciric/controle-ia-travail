"""Rejeu par script des calculs du devis v3 du pilote « oracles plantés » (pilier « mathématiques nouvelles »).

Pièce rejouée : `prereg/mathematiques-nouvelles-v1/devis-pilote-generation-v3-brouillon.md`
(sha256 5c8a0f68518c1f335851c79d09a768b7b99d61c15b6406937cbd79b9fff9abe8), et P7 et A6 du brouillon 3 du
préenregistrement (`preenregistrement-pilote-generation-v1-brouillon-3.md`, e33d7bec…).
Copie adaptée du script v2 (`calculs-v2/calculs_devis_pilote_generation_v2.py`, 3c51f08d…), qui n'est pas modifié ;
logique d'origine : script v1 (`ad1c85d3…`).

Ce que c'est : des produits de prix par des volumes de jetons SUPPOSÉS et par des nombres d'appels écrits
dans le devis v3. Aucune donnée d'expérience, aucun tirage aléatoire (donc aucune graine), aucun appel réseau.
Chaque chiffre du devis est mis en regard du chiffre recalculé (colonne « devis » / « script » / « écart »).

Prix : relevés du 22 novembre 2026, `docs/notes/mathematiques-nouvelles-v1/releves-prix-et-source-score-apparie-v1.md`
(sha256 a7d9073f360b12f2fa914e49d1fd8d56acef86dc81136a494d962c96b2131218), palier standard, pages sans compte.

Lancer (depuis la racine du dépôt) :
  .venv/bin/python -I prereg/mathematiques-nouvelles-v1/calculs-v3/calculs_devis_pilote_generation_v3.py \
      > prereg/mathematiques-nouvelles-v1/calculs-v3/sortie-calculs-devis-pilote-generation-v3.txt
"""
from __future__ import annotations

import math

# ---------------------------------------------------------------------------------------------------
# 0. Prix relevés (USD par million de jetons : entrée, sortie)
# ---------------------------------------------------------------------------------------------------
PRIX = {
    "opus55": (4.0, 20.0),      # relevé, `claude-opus-5-5`
    "argon_nov": (2.0, 10.0),   # relevé, `gemini-4-argon`, jusqu'au 30 novembre 2026
    "argon_dec": (4.0, 20.0),   # relevé, dès le 1er décembre 2026
    "kimi": (2.0, 10.0),        # relevé, `kimi-k3.1-pro`
    "astra": (8.0, 40.0),       # relevé, `gpt-6.2-astra`, ≤ 272 000 jetons d'entrée
    "astra_v1_suppose": (10.0, 50.0),  # barème supposé du devis v1 (pour le contrôle du facteur 0,8)
}
MACHINE_OBSERVE = 0.28          # USD/h, repris du devis v1 (observé le 12 novembre), non relevé à neuf
MACHINE_BORNE_HAUTE = 1.30      # USD/h, repris du devis v1, non relevé à neuf


def cout(modele: str, entree_k: float, sortie_k: float) -> float:
    pe, ps = PRIX[modele]
    return (entree_k * 1000 * pe + sortie_k * 1000 * ps) / 1e6


# ---------------------------------------------------------------------------------------------------
# 1. Effectifs écrits dans le devis v3 (§ 2) et le brouillon 3 du préenregistrement
# ---------------------------------------------------------------------------------------------------
MONDES = 12
PROP_OPUS_PAR_MONDE = 12 + 24   # 12 dans la configuration multi-familles + 24 dans le témoin un modèle
PROP_ARGON_PAR_MONDE = 12
ANALYSES_S_N = 150
TEMOINS_SERVIS_PAR_MONDE = 4    # 2 triviaux + 2 grossiers (brouillon 2, sous-banque servie)
REDOUBLES = 10
REFORMULATIONS = 40
JUGEMENTS = 60                  # 40 connus + 20 énoncés de mondes (devis v1)
APPELS_FUMEE = 4                # SUPPOSÉ par le devis v3 : quatre appels, un par modèle, d'au plus 1 000 jetons en entrée et en sortie
FUMEE_DEVIS = 0.10              # montant forfaitaire écrit au devis v3 (SUPPOSÉ)

prop_opus = MONDES * PROP_OPUS_PAR_MONDE
prop_argon = MONDES * PROP_ARGON_PAR_MONDE
temoins_servis = MONDES * TEMOINS_SERVIS_PAR_MONDE
items_par_bras = ANALYSES_S_N + temoins_servis + REDOUBLES

# ---------------------------------------------------------------------------------------------------
# 2. Profils de jetons SUPPOSÉS (milliers : entrée, sortie), repris du devis v1 (script v1, bloc 2)
# ---------------------------------------------------------------------------------------------------
SC = ("bas", "attendu", "pire")
PROFIL_PROPOSITION = {"bas": (3.0, 1.5), "attendu": (10.0, 3.0), "pire": (20.0, 12.0)}      # SUPPOSÉ
PROFIL_S_AGENT = {"bas": (20.0, 3.0), "attendu": (40.0, 6.0), "pire": (150.0, 30.0)}       # SUPPOSÉ
PROFIL_S_RELECTEUR = {"bas": (3.0, 1.0), "attendu": (4.0, 2.0), "pire": (6.0, 6.0)}        # SUPPOSÉ
PLAFOND_AGENT_S = 1.50          # USD par énoncé ; dans le script v1 il borne l'agent seul, pas le relecteur
PROFIL_N = {"bas": (3.0, 2.0), "attendu": (4.0, 6.0), "pire": (4.0, 24.0)}                 # SUPPOSÉ
PROFIL_JUGE = {"bas": (6.0, 2.0), "attendu": (8.0, 4.0), "pire": (12.0, 12.0)}             # SUPPOSÉ (bas : présent tel quel au script v1)
PROFIL_REFORMULATEUR = {"bas": (4.0, 2.0), "attendu": (6.0, 3.0), "pire": (8.0, 8.0)}      # SUPPOSÉ
HEURES_MACHINE = {"bas": 12.0, "attendu": 24.0, "pire": 48.0}                              # SUPPOSÉ (enveloppe du devis v1)

ecarts: list[tuple[str, float, float]] = []


def f(x: float) -> str:
    return f"{x:,.4f}".replace(",", " ")


def ligne(nom: str, devis: float | None, script: float, tol: float = 0.005) -> None:
    if devis is None:
        print(f"   {nom:70s} devis    —     script {f(script):>10s}")
        return
    e = script - devis
    marque = "" if abs(e) <= tol else "   <<< ÉCART"
    print(f"   {nom:70s} devis {devis:10.4f}  script {f(script):>10s}  écart {e:+.4f}{marque}")
    if abs(e) > tol:
        ecarts.append((nom, devis, script))


print("Rejeu des calculs du devis v3 du pilote « oracles plantés » — calculs v3")
print("Montants en USD. Tolérance d'arrondi : 0,005 (au centime). Profils de jetons SUPPOSÉS (repris du v1).")
print()
print("Bloc 0 — prix relevés (entrée / sortie, par million)")
for k, (pe, ps) in PRIX.items():
    print(f"   {k:18s} {pe:5.2f} / {ps:5.2f}")
print(f"   machine observée {MACHINE_OBSERVE:.2f} USD/h ; borne haute {MACHINE_BORNE_HAUTE:.2f} USD/h (repris du v1)")
print()

print("Bloc 1 — effectifs")
ligne("propositions Opus 12 × (12 + 24)", 432, prop_opus)
ligne("propositions Argon 12 × 12", 144, prop_argon)
ligne("témoins servis par bras (2 + 2 par monde × 12)", 48, temoins_servis)
ligne("items par bras S et N (150 + 48 + 10)", 208, items_par_bras)
ligne("appels neufs par bras par rapport au v1 (48 + 10)", 58, items_par_bras - ANALYSES_S_N)
ligne("dont énoncés neufs (les témoins)", 48, temoins_servis)
ligne("dont seconds services", 10, REDOUBLES)
ligne("témoins triviaux servis par bras (garde A4)", 24, MONDES * 2)
ligne("témoins grossiers servis par bras (garde A4)", 24, MONDES * 2)
print()

print("Bloc 2 — coûts unitaires")
DEVIS_UNIT = {
    "proposition Opus": (0.042, 0.10, 0.32),
    "proposition Argon 2/10": (0.021, 0.05, 0.16),
    "proposition Argon 4/20": (0.042, 0.10, 0.32),
    "item S (agent Opus + relecteur Kimi)": (0.156, 0.308, 1.272),
    "item N (Opus sans outil)": (0.052, 0.136, 0.496),
    "reformulation Kimi": (0.028, 0.042, 0.096),
    "jugement Astra 8/40": (0.128, 0.224, 0.576),
}
unit: dict[str, dict[str, float]] = {k: {} for k in DEVIS_UNIT}
detail_s = {}
for i, sc in enumerate(SC):
    e, s = PROFIL_PROPOSITION[sc]
    unit["proposition Opus"][sc] = cout("opus55", e, s)
    unit["proposition Argon 2/10"][sc] = cout("argon_nov", e, s)
    unit["proposition Argon 4/20"][sc] = cout("argon_dec", e, s)
    agent = cout("opus55", *PROFIL_S_AGENT[sc])
    relect = cout("kimi", *PROFIL_S_RELECTEUR[sc])
    detail_s[sc] = (agent, min(agent, PLAFOND_AGENT_S), relect)
    unit["item S (agent Opus + relecteur Kimi)"][sc] = min(agent, PLAFOND_AGENT_S) + relect
    unit["item N (Opus sans outil)"][sc] = cout("opus55", *PROFIL_N[sc])
    unit["reformulation Kimi"][sc] = cout("kimi", *PROFIL_REFORMULATEUR[sc])
    unit["jugement Astra 8/40"][sc] = cout("astra", *PROFIL_JUGE[sc])
for k, vals in DEVIS_UNIT.items():
    for i, sc in enumerate(SC):
        ligne(f"{k} [{sc}]", vals[i], unit[k][sc], tol=0.0005)
for sc in SC:
    a, ab, r = detail_s[sc]
    print(f"   détail item S [{sc}] : agent {f(a)} (borné {f(ab)}, plafond {PLAFOND_AGENT_S:.2f} {'atteint' if a > PLAFOND_AGENT_S else 'non atteint'}), relecteur {f(r)}")
print("   contrôles des reprises écrites au devis :")
for i, (tot_v1, sc) in enumerate(((23.40, "bas"), (46.20, "attendu"), (190.80, "pire"))):
    ligne(f"sortie v1 bras S {tot_v1} / 150 [{sc}]", DEVIS_UNIT["item S (agent Opus + relecteur Kimi)"][i], tot_v1 / 150, tol=0.0005)
for i, (tot_v1, sc) in enumerate(((7.80, "bas"), (20.40, "attendu"), (74.40, "pire"))):
    ligne(f"sortie v1 bras N {tot_v1} / 150 [{sc}]", DEVIS_UNIT["item N (Opus sans outil)"][i], tot_v1 / 150, tol=0.0005)
for i, sc in enumerate(("attendu", "pire")):
    v1 = cout("astra_v1_suppose", *PROFIL_JUGE[sc])
    ligne(f"jugement Astra v1 10/50 × 0,8 [{sc}]", DEVIS_UNIT["jugement Astra 8/40"][i + 1], v1 * 0.8, tol=0.0005)
juge_kimi = {sc: cout("kimi", *PROFIL_JUGE[sc]) for sc in SC}
ligne("jugement Kimi [bas] (bas v1, cité 0,032)", 0.032, juge_kimi["bas"], tol=0.0005)
ligne("rapport jugement Astra / Kimi [bas] (« quatre fois »)", 4.0, unit["jugement Astra 8/40"]["bas"] / juge_kimi["bas"], tol=1e-9)
print()

print("Bloc 3 — appels de fumée (montant forfaitaire SUPPOSÉ 0,10)")
fumee_1k = {m: cout(m, 1.0, 1.0) for m in ("opus55", "argon_nov", "argon_dec", "kimi", "astra")}
for m, c in fumee_1k.items():
    print(f"   un appel {m} à 1 000 / 1 000 jetons : {f(c)}")
f_quatre_modeles_nov = fumee_1k["opus55"] + fumee_1k["argon_nov"] + fumee_1k["kimi"] + fumee_1k["astra"]
f_quatre_modeles_dec = fumee_1k["opus55"] + fumee_1k["argon_dec"] + fumee_1k["kimi"] + fumee_1k["astra"]
f_astra_kimi = 2 * fumee_1k["astra"] + 2 * fumee_1k["kimi"]
f_quatre_astra = 4 * fumee_1k["astra"]
ligne("fumée : un appel par modèle, Argon 2/10 (borne haute 0,096 au devis)", 0.096, f_quatre_modeles_nov, tol=0.0005)
ligne("fumée : un appel par modèle, Argon 4/20 (borne haute 0,108 au devis)", 0.108, f_quatre_modeles_dec, tol=0.0005)
ligne("dépassement du forfait 0,10 (« à 0,008 près »)", 0.008, f_quatre_modeles_dec - FUMEE_DEVIS, tol=0.0005)
print("   le devis garde 0,10 dans les totaux ; le script fait de même ci-dessous (valeur SUPPOSÉE, non bornante).")
print()

print("Bloc 4 — postes et totaux")
poste = {sc: {} for sc in SC}
for sc in SC:
    poste[sc]["P1"] = REFORMULATIONS * unit["reformulation Kimi"][sc] + JUGEMENTS * unit["jugement Astra 8/40"][sc]
    poste[sc]["P2_nov"] = prop_opus * unit["proposition Opus"][sc] + prop_argon * unit["proposition Argon 2/10"][sc]
    poste[sc]["P2_dec"] = prop_opus * unit["proposition Opus"][sc] + prop_argon * unit["proposition Argon 4/20"][sc]
    poste[sc]["P3_S"] = items_par_bras * unit["item S (agent Opus + relecteur Kimi)"][sc]
    poste[sc]["P3_N"] = items_par_bras * unit["item N (Opus sans outil)"][sc]
    poste[sc]["fumee"] = FUMEE_DEVIS
    poste[sc]["total_nov"] = poste[sc]["P1"] + poste[sc]["P2_nov"] + poste[sc]["P3_S"] + poste[sc]["P3_N"] + FUMEE_DEVIS
    poste[sc]["total_dec"] = poste[sc]["P1"] + poste[sc]["P2_dec"] + poste[sc]["P3_S"] + poste[sc]["P3_N"] + FUMEE_DEVIS
    prix_h = MACHINE_OBSERVE if sc != "pire" else MACHINE_BORNE_HAUTE
    poste[sc]["P4"] = HEURES_MACHINE[sc] * prix_h
DEVIS_POSTES = {
    "P1": (8.80, 15.12, 38.40), "P2_nov": (21.17, 50.40, 161.28), "P2_dec": (24.19, 57.60, 184.32),
    "P3_S": (32.45, 64.06, 264.58), "P3_N": (10.82, 28.29, 103.17), "fumee": (0.10, 0.10, 0.10),
    "total_nov": (73.33, 157.97, 567.52), "total_dec": (76.36, 165.17, 590.56), "P4": (3.36, 6.72, 62.40),
}
for k, vals in DEVIS_POSTES.items():
    for i, sc in enumerate(SC):
        ligne(f"{k} [{sc}]", vals[i], poste[sc][k])
print("   total appels + machine (devis v3, § 2) :")
DEVIS_AM = {"nov": (76.69, 164.69, 629.92), "dec": (79.72, 171.89, 652.96)}
DEVIS_ECART_JOUR = (3.02, 7.20, 23.04)
for i, sc in enumerate(SC):
    ligne(f"appels (30 nov.) + machine [{sc}]", DEVIS_AM["nov"][i], poste[sc]["total_nov"] + poste[sc]["P4"])
    ligne(f"appels (1er déc.) + machine [{sc}]", DEVIS_AM["dec"][i], poste[sc]["total_dec"] + poste[sc]["P4"])
print("   course à cheval sur le 1er décembre : tout total est entre la colonne « 30 nov. » et « 1er déc. »")
print("   (seul le poste Argon change ; écart maximal = 144 × (Argon 4/20 − Argon 2/10)) :")
for i, sc in enumerate(SC):
    ligne(f"écart d'un jour de prix à l'autre [{sc}]", DEVIS_ECART_JOUR[i], poste[sc]["total_dec"] - poste[sc]["total_nov"])
print()

print("Bloc 5 — repli R1 (attendu), trois cas")
juge_kimi_att = JUGEMENTS * juge_kimi["attendu"]
juge_astra_att = JUGEMENTS * unit["jugement Astra 8/40"]["attendu"]
ligne("jugement Kimi attendu (unitaire)", 0.056, juge_kimi["attendu"], tol=0.0005)
ligne("60 jugements Kimi", 3.36, juge_kimi_att)
ligne("60 jugements Astra", 13.44, juge_astra_att)
ligne("différence juge Kimi − juge Astra", -10.08, juge_kimi_att - juge_astra_att)
reform_argon = {m: REFORMULATIONS * cout(m, *PROFIL_REFORMULATEUR["attendu"]) for m in ("argon_nov", "argon_dec")}
reform_kimi = REFORMULATIONS * unit["reformulation Kimi"]["attendu"]
ligne("reformulation Argon 4/20 (unitaire)", 0.084, cout("argon_dec", *PROFIL_REFORMULATEUR["attendu"]), tol=0.0005)
ligne("40 reformulations Argon 4/20", 3.36, reform_argon["argon_dec"])
ligne("40 reformulations Kimi", 1.68, reform_kimi)
ligne("surcoût reformulateur Argon 4/20", 1.68, reform_argon["argon_dec"] - reform_kimi)
ligne("surcoût reformulateur Argon 2/10 (v3 : +0,00)", 0.00, reform_argon["argon_nov"] - reform_kimi)
# Repli « Kimi échoue » : relecteur de S et reformulateur Argon, juge Astra (brouillon 2) — non chiffré au devis
kimi_echoue = {}
for m, nom, dv in (("argon_nov", "2/10", 0.00), ("argon_dec", "4/20", 7.50)):
    relect_argon = items_par_bras * cout(m, *PROFIL_S_RELECTEUR["attendu"])
    relect_kimi = items_par_bras * cout("kimi", *PROFIL_S_RELECTEUR["attendu"])
    sur = (relect_argon - relect_kimi) + (reform_argon[m] - reform_kimi)
    kimi_echoue[nom] = sur
    ligne(f"repli « Kimi échoue », surcoût attendu, Argon {nom}", dv, sur)
# Repli « les deux échouent » : H4 non courue (P1 retiré), relecteur Argon
deux_echouent = {}
for m, nom, tot, dv in (("argon_nov", "2/10", "total_nov", 142.85), ("argon_dec", "4/20", "total_dec", 155.88)):
    relect_sur = items_par_bras * (cout(m, *PROFIL_S_RELECTEUR["attendu"]) - cout("kimi", *PROFIL_S_RELECTEUR["attendu"]))
    deux_echouent[nom] = poste["attendu"][tot] - poste["attendu"]["P1"] + relect_sur
    ligne(f"repli « les deux échouent », total attendu, Argon {nom}", dv, deux_echouent[nom])
    ligne(f"repli « Kimi échoue », total attendu, Argon {nom} (non écrit au devis)", None, poste["attendu"][tot] + kimi_echoue[nom])
print()

print("Bloc 6 — sensibilité (total des appels, attendu)")
sens = {}
for m, nom, tot in (("argon_nov", "2/10", "total_nov"), ("argon_dec", "4/20", "total_dec")):
    astra_col = poste["attendu"][tot]
    kimi_col = astra_col + (juge_kimi_att - juge_astra_att) + (reform_argon[m] - reform_kimi)
    sens[nom] = (astra_col, kimi_col)
ligne("Argon 2/10, juge Astra", 157.97, sens["2/10"][0])
ligne("Argon 2/10, juge Kimi (repli R1, reformulateur Argon)", 147.89, sens["2/10"][1])
ligne("Argon 4/20, juge Astra", 165.17, sens["4/20"][0])
ligne("Argon 4/20, juge Kimi (repli R1, reformulateur Argon)", 156.77, sens["4/20"][1])
print("   postes dominants à l'attendu (Argon 4/20) :",
      ", ".join(f"{k} {poste['attendu'][k]:.2f}" for k in sorted(("P1", "P2_dec", "P3_S", "P3_N"), key=lambda k: -poste["attendu"][k])))
print("   postes dominants au pire (Argon 4/20)    :",
      ", ".join(f"{k} {poste['pire'][k]:.2f}" for k in sorted(("P1", "P2_dec", "P3_S", "P3_N"), key=lambda k: -poste["pire"][k])))
print()

print("Bloc 7 — lignes conditionnelles, réserve, plafonds (Argon 4/20)")
cond_connus = poste["attendu"]["P1"]
prop_par_monde = (prop_opus + prop_argon) / MONDES
cout_prop_att_dec = unit["proposition Opus"]["attendu"]  # = Argon 4/20 à l'attendu
cond_monde = prop_par_monde * cout_prop_att_dec + (items_par_bras / MONDES) * (unit["item S (agent Opus + relecteur Kimi)"]["attendu"] + unit["item N (Opus sans outil)"]["attendu"])
cond_monde_v1_logique = (poste["attendu"]["P2_dec"] + poste["attendu"]["P3_S"] + poste["attendu"]["P3_N"]) / MONDES
ligne("propositions par monde (48)", 48, prop_par_monde)
ligne("item S + item N attendu (0,444)", 0.444, unit["item S (agent Opus + relecteur Kimi)"]["attendu"] + unit["item N (Opus sans outil)"]["attendu"], tol=0.0005)
ligne("banque de connus refaite une fois", 15.12, cond_connus)
ligne("un monde régénéré et rejoué", 12.50, cond_monde)
ligne("un monde régénéré, logique du script v1 (postes / 12)", 12.50, cond_monde_v1_logique)
att_cond = poste["attendu"]["total_dec"] + cond_connus + cond_monde
ligne("attendu avec lignes conditionnelles", 192.79, att_cond)
att_cond_nov = poste["attendu"]["total_nov"] + cond_connus + (prop_opus * cout_prop_att_dec + prop_argon * unit["proposition Argon 2/10"]["attendu"]) / MONDES + (items_par_bras / MONDES) * 0.444
ligne("attendu avec lignes conditionnelles, Argon 2/10", 184.99, att_cond_nov)
reserve_devis = 3 * PLAFOND_AGENT_S + 2 * unit["proposition Argon 4/20"]["pire"] + unit["jugement Astra 8/40"]["pire"]
reserve_v1_logique = 3 * (PLAFOND_AGENT_S + cout("kimi", *PROFIL_S_RELECTEUR["pire"])) + 2 * unit["proposition Argon 4/20"]["pire"] + unit["jugement Astra 8/40"]["pire"]
ligne("réserve formule v2 (3 × 1,50 + 2 × 0,32 + 0,576), abandonnée", 5.72, reserve_devis)
ligne("réserve v3 = logique v1 (relecteur Kimi au pire compté)", 5.93, reserve_v1_logique)
brut_v2 = att_cond * 1.5 + reserve_devis
brut = att_cond * 1.5 + reserve_v1_logique
ligne("192,79 × 1,5 + réserve v3 5,93, valeurs exactes (devis écrit 294,90)", 294.90, brut)
ligne("même calcul sur les valeurs arrondies (192,79 × 1,5 + 5,93)", 294.90, 192.79 * 1.5 + 5.93)
ligne("même calcul avec l'ancienne réserve 5,72, valeurs exactes", 294.90, brut_v2)
plafond = math.ceil(brut / 10) * 10
ligne("plafond d'appels (dizaine supérieure)", 300, plafond)
ligne("plafond d'appels, ancienne réserve 5,72", 300, math.ceil(brut_v2 / 10) * 10)
ligne("machine 48 h × 1,30 (non arrondi)", 62.40, HEURES_MACHINE["pire"] * MACHINE_BORNE_HAUTE)
plafond_machine = math.ceil(HEURES_MACHINE["pire"] * MACHINE_BORNE_HAUTE / 5) * 5
ligne("plafond machine (arrondi aux 5 supérieurs, règle écrite au v3)", 65, plafond_machine)
ligne("somme des plafonds", 365, plafond + plafond_machine)
print(f"   pire des appels (1er déc.) {poste['pire']['total_dec']:.2f} > plafond {plafond} : la coupure A6 joue avant le pire cas ({'vrai' if poste['pire']['total_dec'] > plafond else 'FAUX'})")
print(f"   pire des appels (30 nov.)  {poste['pire']['total_nov']:.2f} > plafond {plafond} : ({'vrai' if poste['pire']['total_nov'] > plafond else 'FAUX'})")
print(f"   marge du plafond sur l'attendu avec conditionnelles : {plafond - att_cond:.2f} ; sur l'attendu simple (1er déc.) : {plafond - poste['attendu']['total_dec']:.2f}")
print()

print("Bloc 8 — intervalle de P7 (devis v3, § 4 ; brouillon 3 : [115,39 ; 261,41])")
P7_BAS_DEVIS, P7_HAUT_DEVIS = 115.39, 261.41
p7_bas_exact = 120 / 164.28 * poste["attendu"]["total_nov"]
p7_haut_exact = 260 / 164.28 * poste["attendu"]["total_dec"]
ligne("borne basse (120 / 164,28) × attendu 30 nov., valeurs exactes", P7_BAS_DEVIS, p7_bas_exact)
ligne("borne haute (260 / 164,28) × attendu 1er déc., valeurs exactes", P7_HAUT_DEVIS, p7_haut_exact)
ligne("borne basse sur l'attendu arrondi 157,97", P7_BAS_DEVIS, 120 / 164.28 * 157.97)
ligne("borne haute sur l'attendu arrondi 165,17", P7_HAUT_DEVIS, 260 / 164.28 * 165.17)
for nom, v, attendu_dedans in (
        ("bas 30 nov.", poste["bas"]["total_nov"], False), ("bas 1er déc.", poste["bas"]["total_dec"], False),
        ("attendu 30 nov.", poste["attendu"]["total_nov"], True), ("attendu 1er déc.", poste["attendu"]["total_dec"], True),
        ("R1 Astra échoue, 2/10", sens["2/10"][1], True), ("R1 Astra échoue, 4/20", sens["4/20"][1], True),
        ("R1 Kimi échoue, 2/10", poste["attendu"]["total_nov"] + kimi_echoue["2/10"], True),
        ("R1 Kimi échoue, 4/20", poste["attendu"]["total_dec"] + kimi_echoue["4/20"], True),
        ("R1 les deux échouent, 2/10", deux_echouent["2/10"], True), ("R1 les deux échouent, 4/20", deux_echouent["4/20"], True),
        ("attendu avec conditionnelles 4/20", att_cond, True), ("attendu avec conditionnelles 2/10", att_cond_nov, True),
        ("pire 30 nov.", poste["pire"]["total_nov"], False), ("pire 1er déc.", poste["pire"]["total_dec"], False),
        ("plafond d'appels", float(plafond), False)):
    dedans = P7_BAS_DEVIS <= v <= P7_HAUT_DEVIS
    ok = "conforme au devis" if dedans == attendu_dedans else "CONTRAIRE AU DEVIS"
    print(f"   {nom:36s} {v:8.2f}  {'dans' if dedans else 'HORS de'} [115,39 ; 261,41]  ({ok})")
    if dedans != attendu_dedans:
        ecarts.append((f"P7 : {nom}", float(attendu_dedans), float(dedans)))
print()

print("Bloc 9 — contrôles d'effectifs du brouillon 3 (P9 et garde A4), sans donnée")
seuil_verites, verites = 4, 8
seuil_faux_tot, faux_tot = 2, 4
pieges = 4
forme_seuil = seuil_verites + seuil_faux_tot + pieges
faux_parmi_seuil = seuil_faux_tot + pieges
ligne("énoncés de forme seuil par monde", 10, forme_seuil)
ligne("faux parmi eux", 6, faux_parmi_seuil)
ligne("P9 : rappel « forme seule » sur les pièges", 1.00, pieges / pieges)
ligne("P9 : rappel « forme seule » sur les faux tôt", 0.50, seuil_faux_tot / faux_tot)
ligne("P9 : fausses morts « forme seule » sur les vérités", 0.50, seuil_verites / verites)
print()

print(f"Bilan : {len(ecarts)} écart(s) supérieur(s) à la tolérance")
for nom, d, s in ecarts:
    print(f"   {nom} : devis {d} ; script {s:.4f}")
