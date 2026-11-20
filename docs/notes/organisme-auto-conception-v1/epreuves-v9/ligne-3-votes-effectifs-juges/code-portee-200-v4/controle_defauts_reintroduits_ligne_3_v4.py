"""Contrôle « trop beau » (règle R4) du banc de la ligne 3, étage 1 : défauts réintroduits un par un dans une copie,
chacun devant être vu par l'essai visé — v4 (banc v4, mode « portée à 200 »).

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

Version 3 (deux ajouts de l'additif 1 v2, e1c1ee84…, à l'alarme) : tous les défauts de la v2, inchangés, rejoués sur le
banc v3 ; plus les défauts des deux ajouts — famille « v3_silence_1 » (part (b), comptes, mélange planté), famille
« v3_silence_2 » (aide « prédiction P6 », carte sans mot) — et la famille « v3_egalite » (un ajout qui toucherait une
mesure existante ou qui manquerait à la sortie), vue par la preuve des sorties égales au v2.

Version 4 (additif 3 v3, 71b7a876…, § 5 et § 6) : tous les défauts du v3, inchangés, rejoués sur le banc v4 et les
essais v4 (la famille « v3_egalite » est vue par la preuve des sorties égales au v3, qui remplace celle du v2) ; plus
la famille « v4_portee_200 » (racines neuves et refus des racines des étages 1 et 2, taille, configuration gelée,
dossier du code propre, une exécution par dossier, formules, règle de lecture, aide, manifeste) et la famille
« v4_chronometrage » (défauts du chronométrage de la portée à 200, réintroduits dans une copie du chronométrage,
variable CHRONOMETRAGE_LIGNE_3_CHEMIN). Garde de la famille « graines » : le corps de `verifier_autorisation` finit
désormais à `def verifier_racine(`. Aucun défaut n'est écrit qui pourrait faire dériver une racine des étages 1 et 2
ou une racine neuve : chaque essai visé appelle `verifier_racine` (sans dérivation) avant tout appel qui dériverait, et
les essais du mode neuf hors essai portent une autorisation fausse et une garde d'arrêt avant tout tirage.

Pour chaque défaut : le texte ancien doit figurer exactement une fois dans le banc ; une copie du banc est écrite avec
ce seul défaut dans un dossier de travail neuf ; les essais visés sont lancés contre la copie (variable
BANC_LIGNE_3_CHEMIN) ; le défaut est « vu » si pytest sort en code 1. Les essais visés sont d'abord lancés contre le
banc sain : ils doivent passer.

Modes : « vise » (défaut) — les essais visés seulement ; « complet » — le fichier d'essais entier, arrêt au premier
échec (méthode de la contre-lecture), pour toutes les familles sauf « graines » (toujours visés). Seule la racine des
essais (2026111930) est dérivée.

Usage :
    python3 -B controle_defauts_reintroduits_ligne_3_v4.py --banc BANC.py --chronometrage CHRONO.py --essais ESSAIS.py \
        --travail DOSSIER_NEUF --sortie RAPPORT.json [--mode vise|complet]
Développeur, modèle L′ (v1 à v3) ; développeur, modèle O (v4).
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

# Version 3 : défauts des deux ajouts de l'additif 1 v2 (silences 1 et 2), et de la preuve d'égalité au v2.
_S1 = ("test_alarme_silence_1_part_b_et_comptes_cas_sain_generateur_factice",
       "test_alarme_silence_1_part_b_artefacts_generateur_factice",
       "test_alarme_silence_1_comptes_coherents_sur_une_cellule_tiree")
_P6 = ("test_alarme_p6_aide_cas_sain", "test_alarme_p6_aide_artefacts")
_EGAL = ("test_v4_sorties_existantes_du_v3_egales_a_l_octet",)  # version 4 : preuve d'égalité au v3
DEFAUTS_V3 = [
    ("S01", "silence 1 : (b) au dénominateur des seules détections (b confondue avec a)",
     "    denominateur_b = n_en_alarme\n", "    denominateur_b = n_changent_detectees\n", _S1, "v3_silence_1"),
    ("S02", "silence 1 : (b) sans les suites sans changement au dénominateur",
     "    denominateur_b = n_en_alarme\n", "    denominateur_b = int((en_alarme & change).sum())\n", _S1, "v3_silence_1"),
    ("S03", "silence 1 : dénominateur nul rendu 0 au lieu d'« indéfini »",
     "    part_b = (n_effet_detectees / denominateur_b) if denominateur_b > 0 else None\n",
     "    part_b = (n_effet_detectees / denominateur_b) if denominateur_b > 0 else 0.0\n", _S1, "v3_silence_1"),
    ("S04", "silence 1 : numérateur compté sur les suites à effet en alarme, alarme avant changement comprise",
     "    n_effet_detectees = int((detecte & effet).sum())\n", "    n_effet_detectees = int((en_alarme & effet).sum())\n",
     _S1, "v3_silence_1"),
    ("S05", "silence 1 : suites sans changement en alarme comptées sur toutes les suites",
     "    n_sans_changement_en_alarme = int((en_alarme & ~change).sum())\n",
     "    n_sans_changement_en_alarme = int(en_alarme.sum())\n", _S1, "v3_silence_1"),
    ("S06", "silence 1 : alarme de la génération 2 oubliée", "    en_alarme = alarmes.any(axis=1)\n",
     "    en_alarme = alarmes[:, 1:].any(axis=1)\n", _S1, "v3_silence_1"),
    ("S07", "silence 1 : nombre de suites faux", "    n_suites = int(alarmes.shape[0])\n",
     "    n_suites = int(alarmes.shape[0]) // 2\n", _S1, "v3_silence_1"),
    ("S08", "silence 1 : suites qui changent détectées comptées sur toutes les suites qui changent",
     "    n_changent_detectees = int(detecte.sum())\n", "    n_changent_detectees = int(change.sum())\n", _S1,
     "v3_silence_1"),
    ("S09", "silence 1 : mélange planté, suites à effet comptées sur les suites qui changent",
     "\"suites_a_effet\": int(effet.sum()),", "\"suites_a_effet\": int(change.sum()),", _S1, "v3_silence_1"),
    ("S10", "silence 1 : ajout absent de la sortie",
     "        bloc.update(silence_1_part_et_comptes(a, change, effet, detecte))\n", "", _S1, "v3_silence_1"),
    ("P01", "silence 2 : fausse alarme « plus de 0,08 » lue « 0,08 ou plus »",
     "        fa_atteinte = BORNE_FAUSSE_ALARME_P6[1] * x > BORNE_FAUSSE_ALARME_P6[0] * n_sans\n",
     "        fa_atteinte = BORNE_FAUSSE_ALARME_P6[1] * x >= BORNE_FAUSSE_ALARME_P6[0] * n_sans\n", _P6, "v3_silence_2"),
    ("P02", "silence 2 : borne de la fausse alarme 0,05 au lieu de 0,08", "BORNE_FAUSSE_ALARME_P6 = (8, 100)",
     "BORNE_FAUSSE_ALARME_P6 = (5, 100)", _P6, "v3_silence_2"),
    ("P03", "silence 2 : détection « au plus égale » lue « strictement inférieure »",
     "        det_atteinte = (b <= d) if lue else None\n", "        det_atteinte = (b < d) if lue else None\n", _P6,
     "v3_silence_2"),
    ("P04", "silence 2 : clause de détection lue aussi à m = 10", "M_DE_LA_CLAUSE_DETECTION_P6 = (20, 40)\n",
     "M_DE_LA_CLAUSE_DETECTION_P6 = (10, 20, 40)\n", _P6, "v3_silence_2"),
    ("P05", "silence 2 : clause de détection lue à m = 40 seulement", "M_DE_LA_CLAUSE_DETECTION_P6 = (20, 40)\n",
     "M_DE_LA_CLAUSE_DETECTION_P6 = (40,)\n", _P6, "v3_silence_2"),
    ("P06", "silence 2 : fausse alarme lue sur le bras C au lieu de la sentinelle",
     "        x = c[\"par_bras\"][\"B\"][\"comptes_silence_1\"][\"suites_sans_changement_en_alarme\"]\n",
     "        x = c[\"par_bras\"][\"C\"][\"comptes_silence_1\"][\"suites_sans_changement_en_alarme\"]\n", _P6,
     "v3_silence_2"),
    ("P07", "silence 2 : détection comparée au bras C au lieu du bras apparié D",
     "        d = c[\"par_bras\"][\"D\"][\"comptes_silence_1\"][\"suites_a_effet_detectees\"]\n",
     "        d = c[\"par_bras\"][\"C\"][\"comptes_silence_1\"][\"suites_a_effet_detectees\"]\n", _P6, "v3_silence_2"),
    ("P08", "silence 2 : « P6 réfutée » seulement si toutes les clauses sont atteintes", "    refutee = any(clauses)\n",
     "    refutee = all(clauses)\n", _P6, "v3_silence_2"),
    ("P09", "silence 2 : la carte reçoit le mot de P6", "        \"carte_fcbf4a2dd1a57\": MOT_CARTE_ALARME,\n",
     "        \"carte_fcbf4a2dd1a57\": mot,\n", _P6, "v3_silence_2"),
    ("P10", "silence 2 : cellule de P6 manquante ou en double non signalée", "    if manquants or doublons:\n",
     "    if False:\n", _P6, "v3_silence_2"),
    ("P11", "silence 2 : fausse alarme lue aux seuls m de la clause de détection",
     "        fa_atteinte = BORNE_FAUSSE_ALARME_P6[1] * x > BORNE_FAUSSE_ALARME_P6[0] * n_sans\n",
     "        fa_atteinte = (BORNE_FAUSSE_ALARME_P6[1] * x > BORNE_FAUSSE_ALARME_P6[0] * n_sans) and m in M_DE_LA_CLAUSE_DETECTION_P6\n", _P6,
     "v3_silence_2"),
    ("E01", "égalité au v2 : la part (a) existante remplacée par la part (b)",
     "            \"part_des_detections_sur_changement_a_effet\": (float(effet[detecte].mean()) if detecte.any() else None),\n",
     "            \"part_des_detections_sur_changement_a_effet\": (float((detecte & effet).sum() / max(1, a.any(axis=1).sum())) if detecte.any() else None),\n",
     _EGAL, "v3_egalite"),
    ("E02", "égalité au v2 : aide de P6 absente des critères mécaniques",
     "            \"alarme_fcbf4a2dd1a57\": criteres_alarme_p6(res_a),\n", "", _EGAL, "v3_egalite"),
]

# Version 4 : défauts du mode « portée à 200 » (banc v4) et du chronométrage de la portée à 200.
_RAC = ("test_portee_200_racines_artefacts_refuses_sans_derivation",)
_RAC1 = ("test_graines_racines_decisives_refusees_sans_autorisation",)
_FAUSSE = ("test_graines_autorisation_fausse_refusee", "test_portee_200_racines_artefacts_refuses_sans_derivation",
           "test_portee_200_autorisation_refusee_avant_derivation_quand_les_autres_gardes_passent")
_CFG = ("test_portee_200_configuration_gelee_et_table_des_cles",)
_SAIN = ("test_portee_200_cas_sain_petit_nombre_de_repliques",)
_TAILLE = ("test_portee_200_garde_taille_artefact_n_autre_que_200",)
_HORS = ("test_portee_200_hors_essai_configuration_gelee_seule",)
_PROPRE = ("test_portee_200_dossier_du_code_propre_artefacts_refus_avant_derivation",
           "test_portee_200_dossier_du_code_par_defaut_est_celui_du_banc")
_UNE = ("test_portee_200_une_execution_par_dossier",)
_FORM = ("test_portee_200_formules_artefacts_banc_invalide_avant_tout_tirage",)
_LECT = ("test_portee_200_regle_de_lecture_cas_sain", "test_portee_200_regle_de_lecture_artefact_codee_a_l_envers")
_CPT = ("test_portee_200_comptes_gagnes_entiers",)
_ETAGE1 = ("test_portee_200_etage_1_inatteignable_hors_essai",)
_VAR = ("test_portee_200_variables_de_chemin",)
_CHR = ("test_chronometrage_n_imprime_que_des_durees", "test_chronometrage_refuse_sans_autorisation")
DEFAUTS_V4 = [
    ("V4-R01", "racines de l'étage 1 non refusées comme telles (seules celles de l'étage 2)",
     "    if racine in RACINES_TOUJOURS_REFUSEES:\n", "    if racine in RACINES_ETAGE_2:\n", _RAC1 + _RAC, "v4_portee_200"),
    ("V4-R02", "racine neuve acceptée sans autorisation", "    if racine in RACINES_SOUS_AUTORISATION:\n"
     "        verifier_autorisation(autorisation, racine)\n",
     "    if False:\n        verifier_autorisation(autorisation, racine)\n", _FAUSSE, "v4_portee_200"),
    ("V4-R03", "tâche hors de l'additif 3 acceptée à une racine neuve",
     "        if tache not in TACHES_PERMISES_PAR_RACINE_PORTEE_200[racine]:\n", "        if False:\n", _RAC,
     "v4_portee_200"),
    ("V4-R04", "nombre d'enfants autre que 210 accepté à une racine neuve",
     "        if nombre != NOMBRE_CELLULES_PORTEE_200:\n", "        if False:\n", _RAC, "v4_portee_200"),
    ("V4-R05", "table des tâches : la racine du rééchantillonnage reçoit aussi la clé des tirages",
     "    RACINE_REECHANTILLONNAGE_PORTEE_200: (\"reechantillonnage_monde_de_puissance\",),\n",
     "    RACINE_REECHANTILLONNAGE_PORTEE_200: (\"monde_de_puissance\", \"reechantillonnage_monde_de_puissance\"),\n",
     _RAC, "v4_portee_200"),
    ("V4-R06", "mode décisif de l'étage 1 rendu au v4",
     "    \"portee_200\": (RACINE_TIRAGES_PORTEE_200, RACINE_REECHANTILLONNAGE_PORTEE_200),\n}\n",
     "    \"portee_200\": (RACINE_TIRAGES_PORTEE_200, RACINE_REECHANTILLONNAGE_PORTEE_200),\n"
     "    \"decisif\": (2026111932, 2026111933),\n}\n", _RAC1 + _CFG, "v4_portee_200"),
    ("V4-R07", "tirages et rééchantillonnage de la mesure sur la même racine",
     "    \"portee_200\": (RACINE_TIRAGES_PORTEE_200, RACINE_REECHANTILLONNAGE_PORTEE_200),\n",
     "    \"portee_200\": (RACINE_TIRAGES_PORTEE_200, RACINE_TIRAGES_PORTEE_200),\n", _CFG, "v4_portee_200"),
    ("V4-R08", "étage 1 joignable hors essai",
     "        raise RefusExecution(f\"mode {contexte.mode!r} : l'étage 1 n'est joué par le banc v4 que sur la racine "
     "des essais\")\n", "        pass\n", _ETAGE1, "v4_portee_200"),
    ("V4-T01", "taille non contrôlée", "    if isinstance(n, bool) or not isinstance(n, int) or n != N_PORTEE_200:\n",
     "    if False:\n", _TAILLE, "v4_portee_200"),
    ("V4-T02", "taille : n flottant ou booléen accepté",
     "    if isinstance(n, bool) or not isinstance(n, int) or n != N_PORTEE_200:\n", "    if n != N_PORTEE_200:\n",
     _TAILLE, "v4_portee_200"),
    ("V4-T03", "configuration gelée non exigée hors essai", "        if cfg != CONFIGURATION_PORTEE_200:\n",
     "        if False:\n", _HORS, "v4_portee_200"),
    ("V4-T04", "dossier du code imposé permis hors essai", "        if dossier_du_code is not None:\n",
     "        if False:\n", _HORS, "v4_portee_200"),
    ("V4-T05", "mode du chronométrage admis à jouer la mesure", "    if contexte.mode not in (\"essais\", \"portee_200\"):\n",
     "    if False:\n", _HORS, "v4_portee_200"),
    ("V4-T06", "configuration gelée : n = 100", "                  \"n\": N_PORTEE_200},\n",
     "                  \"n\": 100},\n", _CFG, "v4_portee_200"),
    ("V4-T07", "configuration gelée : rééchantillonnage à 1 000 tirages",
     "    \"tirages_reechantillonnage\": 2000,\n    \"puissance\": {",
     "    \"tirages_reechantillonnage\": 1000,\n    \"puissance\": {", _CFG, "v4_portee_200"),
    ("V4-U01", "dossier de sortie déjà présent accepté",
     "    dossier = Path(dossier_sortie)\n    if dossier.exists():\n        raise RefusExecution(f\"dossier de sortie déjà "
     "présent : {dossier} (une exécution par dossier)\")\n    code = ",
     "    dossier = Path(dossier_sortie)\n    if False:\n        raise RefusExecution(f\"dossier de sortie déjà "
     "présent : {dossier} (une exécution par dossier)\")\n    code = ", _UNE, "v4_portee_200"),
    ("V4-P01", "sortie sous le dossier du code acceptée", "    if sortie == code or code in sortie.parents:\n",
     "    if False:\n", _PROPRE, "v4_portee_200"),
    ("V4-P02", "sortie égale au dossier du code acceptée", "    if sortie == code or code in sortie.parents:\n",
     "    if code in sortie.parents:\n", _PROPRE, "v4_portee_200"),
    ("V4-P03", "dossier du code hors dépôt accepté",
     "        if dedans.returncode != 0 or dedans.stdout.strip() != \"true\":\n", "        if False:\n", _PROPRE,
     "v4_portee_200"),
    ("V4-P04", "git status --porcelain non lu", "    if etat.stdout.strip() != \"\":\n", "    if False:\n", _PROPRE,
     "v4_portee_200"),
    ("V4-P05", "archives-reponses-modeles/ accepté dans le dossier du code",
     "    if (code / \"archives-reponses-modeles\").exists():\n", "    if False:\n", _PROPRE, "v4_portee_200"),
    ("V4-P06", "garde du dossier du code jamais appelée", "    verifier_dossier_du_code_propre(code, dossier)\n", "",
     _PROPRE, "v4_portee_200"),
    ("V4-P07", "variables de chemin non contrôlées", "    if posees:\n", "    if False:\n", _VAR, "v4_portee_200"),
    ("V4-F01", "formules : écart vrai non contrôlé",
     "        if abs(vrai[comparaison] - vrai[\"au_moins_un\"] - ecart) > TOLERANCE_ECART_VRAI:\n", "        if False:\n",
     _FORM, "v4_portee_200"),
    ("V4-F02", "formules : ancres écrites à la main retirées",
     "            if (d is None) != (attendu is None) or (d is not None and abs(d - attendu) > TOLERANCE_ECART_VRAI):\n",
     "            if False:\n", _FORM, "v4_portee_200"),
    ("V4-F03", "formules : mondes faisables à 0,10 non comparés",
     "    if sorted(faisables) != sorted(MONDES_FAISABLES_A_0_10) or len(faisables) != 13:\n", "    if False:\n", _FORM,
     "v4_portee_200"),
    ("V4-F04", "gardes de la portée jamais appelées avant les tirages", "    verifier_gardes_portee_200()\n", "",
     _FORM, "v4_portee_200"),
    ("V4-L01", "règle de lecture : 0,5 rendu « descriptives » (« sous 0,5 » lu au sens large)",
     "    return ISSUE_A if 2 * minimum_gagnees >= repliques else ISSUE_B\n",
     "    return ISSUE_A if 2 * minimum_gagnees > repliques else ISSUE_B\n", _LECT, "v4_portee_200"),
    ("V4-L02", "règle de lecture : comparaison sans cellule faisable ignorée",
     "    if comparaisons_sans_cellule_faisable:\n        return ISSUE_B\n", "    if False:\n        return ISSUE_B\n",
     _LECT, "v4_portee_200"),
    ("V4-L03", "garde de la règle de lecture retirée", "    if (issue_de_la_regle_de_lecture(1000, 2000, []) != ISSUE_A\n",
     "    if False and (issue_de_la_regle_de_lecture(1000, 2000, []) != ISSUE_A\n", _LECT, "v4_portee_200"),
    ("V4-L04", "aide : maximum au lieu du minimum", "        minimum = min(minima_comptes.values())\n",
     "        minimum = max(minima_comptes.values())\n", _LECT, "v4_portee_200"),
    ("V4-L05", "aide : cellules de l'écart 0,05 lues",
     "        if not c.get(\"faisable\") or abs(c[\"ecart_vise\"] - ECART_QUI_DECIDE) > EPS or c[\"loi\"] not in (1, 3):\n",
     "        if not c.get(\"faisable\") or c[\"loi\"] not in (1, 3):\n", _LECT, "v4_portee_200"),
    ("V4-L06", "aide : « près du seuil » à borne basse stricte",
     "    pres = (minimum is not None and 1000 * minimum >= PRES_DU_SEUIL_MILLIEMES[0] * repliques\n",
     "    pres = (minimum is not None and 1000 * minimum > PRES_DU_SEUIL_MILLIEMES[0] * repliques\n", _LECT,
     "v4_portee_200"),
    ("V4-C01", "comptes : compte entier faux", "        k = int(round(p * R))\n", "        k = int(round(p * R)) - 1\n",
     _CPT + _SAIN, "v4_portee_200"),
    ("V4-C02", "comptes : contrôle d'exactitude retiré", "        if not (0 <= k <= R) or k / R != p:\n",
     "        if False:\n", _CPT, "v4_portee_200"),
    ("V4-C03", "résultat : comptes entiers non ajoutés aux cellules",
     "            c[\"repliques_gagnees_par_comparaison\"] = comptes_gagnes(c)\n", "            pass\n", _SAIN,
     "v4_portee_200"),
    ("V4-C04", "n de la configuration non transmis à la cellule (n = 100 par défaut)",
     "    res_p = [cellule_puissance(gt[i], gr[i], comp, ec, loi, rho, rp, R, B, n=puissance[\"n\"])\n",
     "    res_p = [cellule_puissance(gt[i], gr[i], comp, ec, loi, rho, rp, R, B)\n", _SAIN, "v4_portee_200"),
    ("V4-M01", "manifeste : additif qui fait foi non porté",
     "    manifeste[\"additif_qui_fait_foi_sha256\"] = EMPREINTE_ADDITIF_3_PORTEE_200\n", "", _SAIN, "v4_portee_200"),
    ("V4-M02", "manifeste : état du dépôt lu ailleurs que sur le dossier de la garde",
     "                                     dossier_du_code=code)\n", "                                     dossier_du_code=None)\n",
     _SAIN, "v4_portee_200"),
    ("V4-K01", "chronométrage : variables de chemin non contrôlées hors essai",
     "        banc.verifier_variables_de_chemin_non_posees()\n", "", _CHR, "v4_chronometrage", "chrono"),
    ("V4-K02", "chronométrage : autorisation non vérifiée par le chronométrage (la dérivation la refuse encore)",
     "            banc.verifier_racine(banc.RACINE_CHRONOMETRAGE_PORTEE_200, tache, n, autorisation)\n",
     "            pass\n", _CHR, "v4_chronometrage", "chrono"),
    ("V4-K03", "chronométrage : --tirages-essai permis hors essai", "        if args.tirages_essai is not None:\n",
     "        if False:\n", _CHR, "v4_chronometrage", "chrono"),
    ("V4-K04", "chronométrage : une mesure imprimée",
     "    print(f\"duree_mesuree_du_chronometrage_secondes: {mesuree:.3f}\")\n",
     "    print(f\"duree_mesuree_du_chronometrage_secondes: {mesuree:.3f}\")\n    print(\"puissance: 0.5\")\n", _CHR,
     "v4_chronometrage", "chrono"),
    ("V4-K05", "chronométrage : manifeste sans l'empreinte du chronométrage",
     "    manifeste[\"programme_chronometrage_sha256\"] = banc.sha256_fichier(Path(__file__).resolve())\n", "", _CHR,
     "v4_chronometrage", "chrono"),
    ("V4-K06", "chronométrage : rééchantillonnage tiré sur la clé des tirages",
     "    gr = contexte.reechantillonnage(\"reechantillonnage_monde_de_puissance\", len(cellules))\n",
     "    gr = contexte.reechantillonnage(\"monde_de_puissance\", len(cellules))\n", _CHR, "v4_chronometrage", "chrono"),
]

DEFAUTS = ([d + ("v1",) for d in DEFAUTS_V1] + [d + ("contre_lecture",) for d in DEFAUTS_CONTRE_LECTURE]
           + DEFAUTS_V2 + [d + ("graines",) for d in DEFAUTS_GRAINES] + DEFAUTS_V3 + DEFAUTS_V4)
# Version 4 : chaque défaut porte sa cible (« banc » par défaut, ou « chrono »).
DEFAUTS = [d if len(d) == 7 else d + ("banc",) for d in DEFAUTS]

NOMS_QUI_DERIVENT = ("generateurs", "Contexte", "_gens", "main", "executer_etage_1", "tirages", "reechantillonnage",
                     "chrono", "_charger", "CHEMIN_CHRONO", "RACINE_ESSAIS", "executer_portee_200")
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
    fin = texte_banc.find("\ndef verifier_racine(")  # version 4 : `verifier_racine` suit `verifier_autorisation`
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


def lancer(essais, noms, banc, chrono, travail, complet=False):
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(travail / "tmp"), "BANC_LIGNE_3_CHEMIN": str(banc),
                "CHRONOMETRAGE_LIGNE_3_CHEMIN": str(chrono)})
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
    parser.add_argument("--chronometrage", required=True)
    parser.add_argument("--essais", required=True)
    parser.add_argument("--travail", required=True)
    parser.add_argument("--sortie", required=True)
    parser.add_argument("--mode", choices=("vise", "complet"), default="vise")
    args = parser.parse_args(argv)
    banc = Path(args.banc).resolve()
    chrono = Path(args.chronometrage).resolve()
    essais = Path(args.essais).resolve()
    travail = Path(args.travail).resolve()
    sortie = Path(args.sortie)
    if travail.exists() or sortie.exists():
        print("refus : dossier de travail ou sortie déjà présents", file=sys.stderr)
        return 2
    texte = banc.read_text(encoding="utf-8")
    textes = {"banc": texte, "chrono": chrono.read_text(encoding="utf-8")}
    texte_essais = essais.read_text(encoding="utf-8")
    fonctions_essais = {n.name for n in ast.parse(texte_essais).body if isinstance(n, ast.FunctionDef)}
    idents = [d[0] for d in DEFAUTS]
    if len(set(idents)) != len(idents):
        print("refus : identifiants de défauts en double", file=sys.stderr)
        return 2
    for ident, _, ancien, neuf, vises, famille, cible in DEFAUTS:
        if cible not in textes or (famille == "graines" and cible != "banc"):
            print(f"refus : cible de {ident} inconnue", file=sys.stderr)
            return 2
        if textes[cible].count(ancien) != 1 or ancien == neuf:
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
    code_sain, resume_sain, _ = lancer(essais, vises_tous, banc, chrono, travail)
    rapport = {"programme": "controle-defauts-reintroduits-ligne-3-v4", "programme_sha256": sha256(Path(__file__).resolve()),
               "mode": args.mode, "banc_sha256": sha256(banc), "chronometrage_sha256": sha256(chrono),
               "essais_sha256": sha256(essais),
               "essais_vises_sur_le_banc_sain": {"code": code_sain, "resume": resume_sain, "passent": code_sain == 0},
               "defauts": []}
    if args.mode == "complet":
        code_c, resume_c, _ = lancer(essais, [], banc, chrono, travail, complet=True)
        rapport["fichier_entier_sur_le_banc_sain"] = {"code": code_c, "resume": resume_c, "passe": code_c == 0}
    for ident, description, ancien, neuf, vises, famille, cible in DEFAUTS:
        dossier = travail / ident
        dossier.mkdir()
        source = banc if cible == "banc" else chrono
        copie = dossier / source.name
        copie.write_text(textes[cible].replace(ancien, neuf, 1), encoding="utf-8")
        copie_banc, copie_chrono = (copie, chrono) if cible == "banc" else (banc, copie)
        complet = args.mode == "complet" and famille != "graines"
        code, resume, echecs = lancer(essais, vises, copie_banc, copie_chrono, travail, complet=complet)
        rapport["defauts"].append({"id": ident, "famille": famille, "cible": cible, "description": description,
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
