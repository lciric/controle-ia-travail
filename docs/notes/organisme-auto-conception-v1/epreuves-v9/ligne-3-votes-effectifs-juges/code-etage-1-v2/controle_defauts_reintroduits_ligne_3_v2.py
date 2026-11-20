"""Contrôle « trop beau » (règle R4) du banc de la ligne 3, étage 1 : défauts réintroduits un par un dans une copie,
chacun devant être vu par l'essai visé — v2.

Version 2 (corrections C1 et C3 de la contre-lecture `contre-lecture-code-etage-1-ligne-3-v1.md`, 3aed6849…) :
- les 27 défauts de la v1 (famille « v1 ») ;
- les 35 mutants de la contre-lecture (`mutants_cl.py`, c3ece475…), mêmes textes ancien et neuf, chacun avec l'essai
  v2 qui l'épingle (famille « contre_lecture ») ;
- le défaut inverse de la correction C2 (famille « c2 ») et un défaut de « dépasse » strict de la branche (3)
  (famille « v2 ») ;
- des défauts visés sur `verifier_autorisation` seule (famille « graines », correction C3). Garde avant tout
  lancement : le texte ancien de chacun se trouve dans le corps de `verifier_autorisation` ; ses essais visés
  commencent par `test_verifier_autorisation_` et, avec les fonctions du fichier d'essais qu'ils appellent, ne
  nomment aucune fonction qui dérive une graine (`generateurs`, `Contexte`, `_gens`, `main`, `executer_etage_1`,
  `tirages`, `reechantillonnage`, le chronométrage). Ces défauts ne sont jamais joués contre le fichier entier.

Pour chaque défaut : le texte ancien doit figurer exactement une fois dans le banc ; une copie du banc est écrite avec
ce seul défaut dans un dossier de travail neuf ; les essais visés sont lancés contre la copie (variable
BANC_LIGNE_3_CHEMIN) ; le défaut est « vu » si pytest sort en code 1. Les essais visés sont d'abord lancés contre le
banc sain : ils doivent passer.

Modes : « vise » (défaut) — les essais visés seulement ; « complet » — le fichier d'essais entier, arrêt au premier
échec (méthode de la contre-lecture), pour toutes les familles sauf « graines » (toujours visés). Seule la racine des
essais (2026111930) est dérivée.

Usage :
    python3 -B controle_defauts_reintroduits_ligne_3_v2.py --banc BANC.py --essais ESSAIS.py --travail DOSSIER_NEUF \
        --sortie RAPPORT.json [--mode vise|complet]
Développeur, modèle L′.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

DEFAUTS_V1 = [
    ("D01", "ρ indéfinie rendue 0", "    rho = np.where(indefini, np.nan, rho)\n",
     "    rho = np.where(indefini, 0.0, rho)\n",
     ("test_garde_estimateur_artefact_juge_sans_erreur_indefini_jamais_zero",)),
    ("D02", "loi 1 : choc tiré par juge et non par témoin", "        choc = rng.random((R, m, 1)) < param\n",
     "        choc = rng.random((R, m, J)) < param\n", ("test_formules_correlation_estimee_contre_valeur_plantee",)),
    ("D03", "loi 1 : valeur plantée prise sur la grille à taux inégaux",
     "                    C[j, k] = param * (min(p[j], p[k]) - p[j] * p[k])\n",
     "                    C[j, k] = param * math.sqrt(p[j] * (1 - p[j]) * p[k] * (1 - p[k]))\n",
     ("test_formules_artefact_valeur_plantee_prise_sur_la_grille_a_taux_inegaux",)),
    ("D04", "loi 2 : valeur plantée égale à r",
     "                    C[j, k] = float(np.sum(w * phis[j] * phis[k])) - p[j] * p[k]\n",
     "                    C[j, k] = param * math.sqrt(p[j] * (1 - p[j]) * p[k] * (1 - p[k]))\n",
     ("test_formules_valeurs_plantees_exactes_connues",)),
    ("D05", "porteuse : arrondi au pair", "    q = 3 + np.floor(x + 0.5)\n", "    q = 3 + np.round(x)\n",
     ("test_porteuse_arrondi_au_demi_superieur_et_non_au_pair",)),
    ("D06", "unanimité codée à l'envers", "    bras[\"U\"] = Vl.all(axis=-1)\n", "    bras[\"U\"] = ~Vl.any(axis=-1)\n",
     ("test_garde_p2_cas_sain_quatre_regles_a_la_meme_erreur_equilibree",)),
    ("D07", "double rendu : le second rendu garde le trait",
     "        s1, s2 = np.broadcast_to(t, f1.shape), np.zeros_like(f2)\n",
     "        s1, s2 = np.broadcast_to(t, f1.shape), np.broadcast_to(t, f2.shape)\n",
     ("test_double_rendu_taux_exacts_contre_le_calcul",)),
    ("D08", "bras C : score au seuil rendu notable",
     "    return (scores - seuil[:, None]) > tolerance_egalite(w, seuil)[:, None]\n",
     "    return (scores - seuil[:, None]) >= -tolerance_egalite(w, seuil)[:, None]\n",
     ("test_bras_c_score_au_seuil_rend_non_notable",)),
    ("D09", "monde de puissance : écart pris contre l'unanimité",
     "        return e[comparaison] - e[\"au_moins_un\"] - ecart\n",
     "        return e[comparaison] - e[\"unanimite\"] - ecart\n",
     ("test_monde_de_puissance_dissymetrie_et_faisabilite_contre_le_calcul",)),
    ("D10", "Holm remplacé par des tests non corrigés", "    seuils = alpha / (m - np.arange(m))\n",
     "    seuils = alpha + 0.0 * np.arange(m)\n", ("test_holm_pas_a_pas_descendant",)),
    ("D11", "binomial exact unilatéral",
     "    pv = np.array([pmf[pmf <= pmf[x] * (1 + 1e-7)].sum() for x in range(m + 1)])\n",
     "    pv = np.array([pmf[: x + 1].sum() for x in range(m + 1)])\n", ("test_binomial_exact_bilateral",)),
    ("D12", "bras C : poids non ramenés à [0,2 ; 5] fois la moyenne",
     "    w = np.where(repli[:, None], 1.0, borne)\n", "    w = np.where(repli[:, None], 1.0, w)\n",
     ("test_bras_c_poids_bornes_aucun_poids_nul_aucun_juge_retire",)),
    ("D13", "estimateur : erreurs centrées sur la moyenne globale, non par classe",
     "        Xc = Xc - Xc.mean(axis=-2, keepdims=True)\n", "        Xc = Xc - X.mean(axis=-2, keepdims=True)\n",
     ("test_formules_correlation_estimee_contre_valeur_plantee",)),
    ("D14", "estimateur : division par n au lieu de n − 2", "    return total / (n - 2)\n", "    return total / n\n",
     ("test_covariance_depuis_comptes_egale_covariance_directe",)),
    ("D15", "double rendu : bras 1 sans l'exigence d'un vote stable",
     "    return {\"bras_1\": (n_stable >= 1) & stables_notables,\n", "    return {\"bras_1\": stables_notables,\n",
     ("test_double_rendu_taux_exacts_contre_le_calcul",)),
    ("D16", "loi 3 : coefficient du difficile faux", "    haut = p + 0.75 * a\n", "    haut = p + 0.25 * a\n",
     ("test_formules_correlation_estimee_contre_valeur_plantee",)),
    ("D17", "loi 4 : probabilité du choc du collège fausse", "        q_tous = param / 3.0\n",
     "        q_tous = param / 2.0\n", ("test_formules_correlation_estimee_contre_valeur_plantee",)),
    ("D18", "bras R : ρ′ ignorée", "    copie = rng.random((R, n, 1)) < rho_prime\n",
     "    copie = rng.random((R, n, 1)) < 0.0 * rho_prime\n",
     ("test_formules_erreur_equilibree_de_chaque_regle_contre_le_paragraphe_0",)),
    ("D19", "bras P : paire corrélée non divisée", "            w[masque, j] = w[masque, j] / 2.0\n",
     "            w[masque, j] = w[masque, j] / 1.0\n", ("test_bras_p_paire_correlee_divisee_par_deux",)),
    ("D20", "clause (iii) : marge de dépendance à la surface fausse",
     "    if abs(e1_moy) >= MARGE_SURFACE and (e1_bas > 0 or e1_haut < 0):\n",
     "    if abs(e1_moy) >= 0.5 and (e1_bas > 0 or e1_haut < 0):\n",
     ("test_double_rendu_mots_sans_intervalle_contre_la_sortie_du_calcul",)),
    ("D21", "alarme : niveau non divisé par 11", "NIVEAU_ALARME = 0.05 / 11\n", "NIVEAU_ALARME = 0.05\n",
     ("test_alarme_bras_a_muet_et_sentinelle_detecte_un_changement_a_effet",)),
    ("D22", "clause (ii) : abstention plantée fausse",
     "ABSTENTION_PLANTEE_PAR_VOTE = 2 * (P_FOND - (P_FOND * P_FOND + RHO_PRIME_FOND * P_FOND * (1 - P_FOND)))\n",
     "ABSTENTION_PLANTEE_PAR_VOTE = (P_FOND - (P_FOND * P_FOND + RHO_PRIME_FOND * P_FOND * (1 - P_FOND)))\n",
     ("test_double_rendu_taux_exacts_contre_le_calcul",)),
    ("D23", "règle choisie : juge 1 seul nommé juge 2 seul", "    (False, False, True, True): \"juge_1_seul\",\n",
     "    (False, False, True, True): \"juge_2_seul\",\n", ("test_regle_choisie_deux_juges_cas_sains_et_artefacts",)),
    ("D24", "valeur plantée : dénominateur J au lieu de J − 1",
     "    rho_moy = (float(C.sum()) - tr) / ((J - 1) * tr)\n", "    rho_moy = (float(C.sum()) - tr) / (J * tr)\n",
     ("test_formules_valeurs_plantees_exactes_connues",)),
    ("D25", "manifeste : dérivations des graines omises",
     "                    \"table_cles\": TABLE_CLES, \"derivations\": contexte.derivations},\n",
     "                    \"table_cles\": TABLE_CLES, \"derivations\": []},\n",
     ("test_bout_en_bout_essai_manifeste_et_execution_unique",)),
    ("D26", "valeur de probabilité sans le « 1 + »",
     "    return (1.0 + (np.asarray(diff) <= EPS).sum(axis=0)) / (B + 1.0)\n",
     "    return ((np.asarray(diff) <= EPS).sum(axis=0)) / (B + 1.0)\n",
     ("test_p_valeur_unilaterale_du_reechantillonnage_apparie",)),
    ("D27", "audit « trop propre » jamais levé",
     "            \"audit_trop_propre_aucune_replique_hors_intervalle\": bool(couverture == 1.0)}\n",
     "            \"audit_trop_propre_aucune_replique_hors_intervalle\": bool(couverture > 1.0)}\n",
     ("test_audit_trop_propre_cellule_sans_replique_hors_intervalle",)),
]

_FA38 = ("test_mot_fa38_regle_gelee_cas_sains", "test_mot_fa38_regle_gelee_artefacts")
_BR3 = ("test_branche_3_lit_les_rondes_a_delta_0_5_cas_sain", "test_branche_3_lit_les_rondes_a_delta_0_5_artefacts")
_ALARME = ("test_alarme_comparaisons_a_seuils_serres_generateur_factice",)
_CELLULE5 = ("test_cellule_cinq_juges_stabilite_porteuse_r_et_mot_fa38_rejoues",)
_PUISSANCE = ("test_monde_de_puissance_test_entier_rejoue",)

# Mutants de la contre-lecture : textes recopiés de `mutants_cl.py` (c3ece475…), à l'identique.
DEFAUTS_CONTRE_LECTURE = [
    ("M01", "mot_fa38 : 15 % -> 50 %", "fa_p <= 0.85 * fa_r", "fa_p <= 0.5 * fa_r", _FA38),
    ("M02", "mot_fa38 : sous 0,02 -> sous 0,2", "if fa_r < 0.02 or vr_p > vr_r + 0.05:",
     "if fa_r < 0.2 or vr_p > vr_r + 0.05:", _FA38),
    ("M03", "mot_fa38 : marge vrais rejetes 0,05 -> 0,5", "vr_p > vr_r + 0.05", "vr_p > vr_r + 0.5", _FA38),
    ("M04", "branche 2 : 0,02 -> 0,2", "mot = \"réfuté sur le banc\" if ecart > 0.02 else \"tient sur le banc\"",
     "mot = \"réfuté sur le banc\" if ecart > 0.2 else \"tient sur le banc\"",
     ("test_branche_2_seuil_de_0_02_par_cellule",)),
    ("M05", "branche 2 : taille d'etalonnage n au lieu de n/2", "taille = c[\"n\"] // 2", "taille = c[\"n\"]",
     ("test_branche_2_taille_d_etalonnage_n_sur_2",)),
    ("M06", "branche 3 : delta 0,5 -> 0,2",
     "forte = [c for c in cadrage if c[\"t\"] == t and abs(c[\"delta\"] - 0.5) < EPS]",
     "forte = [c for c in cadrage if c[\"t\"] == t and abs(c[\"delta\"] - 0.2) < EPS]", _BR3),
    ("M07", "alarme : z critique unilateral", "z_crit = statistics.NormalDist().inv_cdf(1 - NIVEAU_ALARME / 2)",
     "z_crit = statistics.NormalDist().inv_cdf(1 - NIVEAU_ALARME)", _ALARME),
    ("M08", "alarme : bras B teste la generation 1 a la place de la 12", "\"B\": pv[:, 1:] <= NIVEAU_ALARME}",
     "\"B\": pv[:, :-1] <= NIVEAU_ALARME}", _ALARME),
    ("M09", "stabilite : centile 90", "np.percentile(ecarts_moities, 95)", "np.percentile(ecarts_moities, 90)",
     _CELLULE5),
    ("M10", "Holm : niveau 0,10", "NIVEAU_HOLM = 0.05", "NIVEAU_HOLM = 0.10", _PUISSANCE),
    ("M11", "marge de comparaison 0,10", "MARGE_COMPARAISON = 0.05", "MARGE_COMPARAISON = 0.10", _PUISSANCE),
    ("M12", "bras C : lambda 0,5", "lam = 0.1 * tr / J", "lam = 0.5 * tr / J",
     ("test_bras_c_poids_contre_un_calcul_independant",)),
    ("M13", "bras C : signe de d inverse", "d = V[:, y_cal].mean(axis=1) - V[:, ~y_cal].mean(axis=1)",
     "d = V[:, ~y_cal].mean(axis=1) - V[:, y_cal].mean(axis=1)", ("test_bras_c_poids_contre_un_calcul_independant",)),
    ("M14", "seuil au milieu : moyenne des bons seulement",
     "return (scores_cal[:, y_cal].mean(axis=1) + scores_cal[:, ~y_cal].mean(axis=1)) / 2.0",
     "return scores_cal[:, y_cal].mean(axis=1)", ("test_seuil_au_milieu_des_deux_moyennes_de_classe",)),
    ("M15", "bras N : >= q devient > q", "bras[\"N\"] = Vl.sum(axis=-1) >= q[:, None]",
     "bras[\"N\"] = Vl.sum(axis=-1) > q[:, None]", _CELLULE5),
    ("M16", "tolerance couverture 0,80", "TOL_COUVERTURE = (0.90, 0.98)", "TOL_COUVERTURE = (0.80, 0.98)",
     ("test_qualite_estimateur_tolerance_gelee_artefacts",)),
    ("M17", "tolerance biais 0,10", "TOL_BIAIS = 0.05", "TOL_BIAIS = 0.10",
     ("test_qualite_estimateur_tolerance_gelee_artefacts",)),
    ("M18", "R k=5 : majorite >= 2", "bras[f\"R_k5_rp{rp}\"] = Vr.sum(axis=-1) >= 3",
     "bras[f\"R_k5_rp{rp}\"] = Vr.sum(axis=-1) >= 2", _CELLULE5),
    ("M19", "double rendu bras 2 : deux juges au lieu de quatre", "\"bras_2\": v1[..., :2 * k].all(axis=-1),",
     "\"bras_2\": v1[..., :k].all(axis=-1),", ("test_double_rendu_taux_exacts_contre_le_calcul",)),
    ("M20", "intervalle des repliques : 5/95", "lo, hi = np.percentile(moyennes, [2.5, 97.5])",
     "lo, hi = np.percentile(moyennes, [5, 95])", ("test_intervalle_des_repliques_centiles_2_5_et_97_5",)),
    ("M21", "centiles du reechantillonnage 5/95", "lo = np.nanpercentile(valeurs, 2.5, axis=axe)",
     "lo = np.nanpercentile(valeurs, 5, axis=axe)", ("test_centiles_du_reechantillonnage_2_5_et_97_5",)),
    ("M22", "bras P : plancher 0", "w = np.maximum(exactitude - 0.5, 0.05)", "w = np.maximum(exactitude - 0.5, 0.0)",
     ("test_bras_p_plancher_0_05_et_seuil_de_paire_0_5",)),
    ("M23", "bras P : seuil de paire 0,5 -> 0,9", "> 0.5)\n            w[masque, j]", "> 0.9)\n            w[masque, j]",
     ("test_bras_p_plancher_0_05_et_seuil_de_paire_0_5",)),
    ("M24", "cadrage : > c devient >= c", "float((inversion > c).mean())", "float((inversion >= c).mean())",
     ("test_garde_de_cadrage_depasse_strict_rejouee",)),
    ("M25", "clause (i) : marge 0,05 -> 0,5", "MARGE_VRAIS_REJETES = 0.05", "MARGE_VRAIS_REJETES = 0.5",
     ("test_mot_clause_i_regle_gelee_cas_sains_et_artefacts",)),
    ("M26", "clause (i) : sans prise sous 0,02 -> 0,2", "SEUIL_REFERENCE_SANS_PRISE = 0.02",
     "SEUIL_REFERENCE_SANS_PRISE = 0.2", ("test_mot_clause_i_regle_gelee_cas_sains_et_artefacts",)),
    ("M27", "puissance qui decide : maximum au lieu de minimum", "p = min(minima.values())", "p = max(minima.values())",
     ("test_puissance_qui_decide_regle_gelee",)),
    ("M28", "puissance 0,5 -> 0,3", "PUISSANCE_EXIGEE = 0.5", "PUISSANCE_EXIGEE = 0.3",
     ("test_puissance_qui_decide_regle_gelee",)),
    ("M29", "rho'-rho : borne basse 2,5 -> 5", "lo, _ = _centiles(rp - r12, 0)",
     "lo = np.nanpercentile(rp - r12, 5, axis=0)", ("test_puissance_rho_prime_borne_basse_centile_2_5_rejouee",)),
    ("M30", "couverture : un intervalle indefini ne compte pas non-couvrant (couvre[defini] -> tout)",
     "couverture = float(couvre[defini].mean())", "couverture = float(couvre.mean())",
     ("test_qualite_estimateur_couverture_sur_les_seules_repliques_definies",)),
    ("M31", "alarme : niveau de la sentinelle sans bilateral exact (unilateral droit)",
     "pv = np.array([pmf[pmf <= pmf[x] * (1 + 1e-7)].sum() for x in range(m + 1)])",
     "pv = np.array([pmf[x:].sum() * 2 for x in range(m + 1)])", ("test_binomial_exact_bilateral",)),
    ("M32", "alarme : 70 % -> 50 % de bons", "production = rng.binomial(70, 1 - vr) + rng.binomial(30, fa)",
     "production = rng.binomial(50, 1 - vr) + rng.binomial(50, fa)", _ALARME),
    ("M33", "alarme : generation du changement 4..10 -> 4..9", "g_change = rng.integers(4, 11, size=R)",
     "g_change = rng.integers(4, 10, size=R)", _ALARME),
    ("M34", "monde de puissance : R lie au juge 1 au lieu du 2",
     "Er = repetitions(rng_t, E[..., 1], p_juge_2, rho_prime, 3)",
     "Er = repetitions(rng_t, E[..., 0], p_juge_2, rho_prime, 3)", _PUISSANCE),
    ("M35", "stabilite : ecart signe (sans abs)", "ecarts_moities = np.abs(r_cal - r_lec)[ok]",
     "ecarts_moities = (r_cal - r_lec)[ok]", _CELLULE5),
]

DEFAUTS_V2 = [
    ("C2R", "branche (2) : lecture « plus petite taille où tout tient », sans exiger les tailles plus grandes "
            "(inverse de la correction C2)",
     "        else:\n            break\n    return retenue, []\n", "        else:\n            continue\n    return retenue, []\n",
     ("test_branche_2_lettre_a_partir_de_laquelle_artefacts",), "c2"),
    ("B3S", "branche (3) : « plus de 10 % » lu « 10 % ou plus »", "    if part_saine > 0.10:\n",
     "    if part_saine >= 0.10:\n", ("test_branche_3_lit_les_rondes_a_delta_0_5_cas_sain",), "v2"),
]

_GRAINES = ("test_verifier_autorisation_cas_sain_additif_valide_accepte_sans_derivation",
            "test_verifier_autorisation_artefacts_refuses_sans_derivation")
DEFAUTS_GRAINES = [
    ("G01", "garde des graines : empreinte de l'additif non comparée", "    if sha256_fichier(chemin) != emp:\n",
     "    if False:\n", _GRAINES),
    ("G02", "garde des graines : additif absent accepté",
     "        raise RefusGraine(f\"racine {racine} : additif absent\")\n", "        return\n", _GRAINES),
    ("G03", "garde des graines : absence d'autorisation acceptée",
     "        raise RefusGraine(f\"racine {racine} : refus sans autorisation (additif de code scellé)\")\n",
     "        return\n", _GRAINES),
    ("G04", "garde des graines : empreinte mal formée non refusée comme telle",
     "    if not (isinstance(emp, str) and len(emp) == 64 and all(c in \"0123456789abcdef\" for c in emp)):\n",
     "    if False:\n", _GRAINES),
    ("G05", "garde des graines : additif valide refusé (empreinte comparée en majuscules)",
     "    if sha256_fichier(chemin) != emp:\n", "    if sha256_fichier(chemin) != emp.upper():\n", _GRAINES),
    ("G06", "garde des graines : type de l'autorisation non vérifié",
     "    if not isinstance(autorisation, Autorisation):\n", "    if False:\n", _GRAINES),
]

DEFAUTS = ([d + ("v1",) for d in DEFAUTS_V1] + [d + ("contre_lecture",) for d in DEFAUTS_CONTRE_LECTURE]
           + DEFAUTS_V2 + [d + ("graines",) for d in DEFAUTS_GRAINES])

NOMS_QUI_DERIVENT = ("generateurs", "Contexte", "_gens", "main", "executer_etage_1", "tirages", "reechantillonnage",
                     "chrono", "_charger", "CHEMIN_CHRONO", "RACINE_ESSAIS")
PREFIXE_ESSAIS_GRAINES = "test_verifier_autorisation_"


def sha256(chemin):
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def noms_appeles(noeud):
    noms = set()
    for n in ast.walk(noeud):
        if isinstance(n, ast.Name):
            noms.add(n.id)
        elif isinstance(n, ast.Attribute):
            noms.add(n.attr)
    return noms


def garde_graines(texte_banc, texte_essais, ancien, essais_vises):
    """Refus (chaîne) si un défaut « graines » pourrait faire dériver une graine ; None sinon."""
    debut = texte_banc.find("def verifier_autorisation(")
    fin = texte_banc.find("\ndef generateurs(")
    pos = texte_banc.find(ancien)
    if not (0 <= debut < pos < fin):
        return "texte ancien hors du corps de verifier_autorisation"
    module = ast.parse(texte_essais)
    fonctions = {n.name: n for n in module.body if isinstance(n, ast.FunctionDef)}
    a_voir = list(essais_vises)
    vus = set()
    while a_voir:
        nom = a_voir.pop()
        if nom in vus:
            continue
        vus.add(nom)
        if nom in essais_vises and not nom.startswith(PREFIXE_ESSAIS_GRAINES):
            return f"essai visé {nom} hors du préfixe {PREFIXE_ESSAIS_GRAINES}"
        if nom not in fonctions:
            return f"fonction {nom} absente du fichier d'essais"
        appeles = noms_appeles(fonctions[nom])
        interdits = sorted(appeles & set(NOMS_QUI_DERIVENT))
        if interdits:
            return f"{nom} nomme {interdits}"
        a_voir.extend(sorted((appeles & set(fonctions)) - vus))
    return None


def lancer(essais, noms, banc, travail, complet=False):
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(travail / "tmp"), "BANC_LIGNE_3_CHEMIN": str(banc),
                "CHRONOMETRAGE_LIGNE_3_CHEMIN": str(Path(essais).resolve().parent / "chronometrer_banc_ligne_3_v2.py")})
    cmd = [sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--tb=line"]
    cmd += (["-x", str(essais)] if complet else [f"{essais}::{n}" for n in noms])
    r = subprocess.run(cmd, cwd=str(travail), env=env, capture_output=True, text=True, timeout=1800)
    lignes = [ligne for ligne in r.stdout.strip().splitlines() if ligne.strip()]
    derniere = lignes[-1:] or [""]
    echecs = [ligne.strip() for ligne in lignes if ligne.strip().startswith(str(essais) + ":")
              or ligne.strip().startswith("E ")][:12]
    return r.returncode, derniere[0], echecs


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--banc", required=True)
    parser.add_argument("--essais", required=True)
    parser.add_argument("--travail", required=True)
    parser.add_argument("--sortie", required=True)
    parser.add_argument("--mode", choices=("vise", "complet"), default="vise")
    args = parser.parse_args(argv)
    banc = Path(args.banc).resolve()
    essais = Path(args.essais).resolve()
    travail = Path(args.travail).resolve()
    sortie = Path(args.sortie)
    if travail.exists() or sortie.exists():
        print("refus : dossier de travail ou sortie déjà présents", file=sys.stderr)
        return 2
    texte = banc.read_text(encoding="utf-8")
    texte_essais = essais.read_text(encoding="utf-8")
    fonctions_essais = {n.name for n in ast.parse(texte_essais).body if isinstance(n, ast.FunctionDef)}
    idents = [d[0] for d in DEFAUTS]
    if len(set(idents)) != len(idents):
        print("refus : identifiants de défauts en double", file=sys.stderr)
        return 2
    for ident, _, ancien, neuf, vises, famille in DEFAUTS:
        if texte.count(ancien) != 1 or ancien == neuf:
            print(f"refus : texte ancien de {ident} absent ou multiple", file=sys.stderr)
            return 2
        manquants = [n for n in vises if n not in fonctions_essais]
        if manquants:
            print(f"refus : essais visés de {ident} absents du fichier d'essais : {manquants}", file=sys.stderr)
            return 2
        if famille == "graines":
            motif = garde_graines(texte, texte_essais, ancien, vises)
            if motif:
                print(f"refus : garde des graines pour {ident} : {motif}", file=sys.stderr)
                return 2
    travail.mkdir(parents=True)
    (travail / "tmp").mkdir()
    vises_tous = sorted({n for d in DEFAUTS for n in d[4]})
    code_sain, resume_sain, _ = lancer(essais, vises_tous, banc, travail)
    rapport = {"programme": "controle-defauts-reintroduits-ligne-3-v2", "programme_sha256": sha256(Path(__file__).resolve()),
               "mode": args.mode, "banc_sha256": sha256(banc), "essais_sha256": sha256(essais),
               "essais_vises_sur_le_banc_sain": {"code": code_sain, "resume": resume_sain, "passent": code_sain == 0},
               "defauts": []}
    if args.mode == "complet":
        code_c, resume_c, _ = lancer(essais, [], banc, travail, complet=True)
        rapport["fichier_entier_sur_le_banc_sain"] = {"code": code_c, "resume": resume_c, "passe": code_c == 0}
    for ident, description, ancien, neuf, vises, famille in DEFAUTS:
        dossier = travail / ident
        dossier.mkdir()
        copie = dossier / banc.name
        copie.write_text(texte.replace(ancien, neuf, 1), encoding="utf-8")
        complet = args.mode == "complet" and famille != "graines"
        code, resume, echecs = lancer(essais, vises, copie, travail, complet=complet)
        rapport["defauts"].append({"id": ident, "famille": famille, "description": description,
                                   "essais_vises": list(vises), "joue_contre": "fichier entier" if complet else "essais visés",
                                   "code_pytest": code, "resume": resume, "lignes_d_echec": echecs,
                                   "vu": code == 1})
        print(f"{ident} [{famille}] vu={code == 1} code={code} {resume}", flush=True)
    par_famille = {}
    for d in rapport["defauts"]:
        f = par_famille.setdefault(d["famille"], {"defauts": 0, "vus": 0, "non_vus": []})
        f["defauts"] += 1
        f["vus"] += int(d["vu"])
        if not d["vu"]:
            f["non_vus"].append(d["id"])
    rapport["par_famille"] = par_famille
    rapport["tous_vus"] = all(d["vu"] for d in rapport["defauts"])
    with open(sortie, "x", encoding="utf-8") as f:
        f.write(json.dumps(rapport, ensure_ascii=False, indent=1) + "\n")
    print(f"essais visés sur le banc sain : code={code_sain} {resume_sain}")
    print(f"par famille : {json.dumps(par_famille, ensure_ascii=False)}")
    print(f"tous vus : {rapport['tous_vus']}")
    sain_ok = code_sain == 0 and rapport.get("fichier_entier_sur_le_banc_sain", {"passe": True})["passe"]
    return 0 if (rapport["tous_vus"] and sain_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
