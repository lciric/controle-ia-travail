"""Contrôle « trop beau » (règle R4) du banc de la ligne 3, étage 1 : défauts réintroduits un par un dans une copie,
chacun devant être vu par l'essai visé — v1.

Pour chaque défaut de la liste gelée ci-dessous : le texte ancien doit figurer exactement une fois dans le banc ; une
copie du banc est écrite avec ce seul défaut dans un dossier de travail neuf ; l'essai visé est lancé contre la copie
(variable BANC_LIGNE_3_CHEMIN) ; le défaut est « vu » si l'essai échoue (code de sortie 1 de pytest). Les essais
visés sont d'abord lancés contre le banc sain : ils doivent passer. Aucun défaut ne touche la garde des graines :
réintroduire un défaut de cette garde ferait dériver une racine décisive, ce qui est interdit pendant le travail du
développeur ; ce manque est déclaré au rapport. Seule la racine des essais (2026111930) est dérivée.

Usage :
    python3 -B controle_defauts_reintroduits_ligne_3_v1.py --banc BANC.py --essais ESSAIS.py --travail DOSSIER_NEUF \
        --sortie RAPPORT.json
Développeur, modèle L′.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

DEFAUTS = [
    ("D01", "ρ indéfinie rendue 0", "    rho = np.where(indefini, np.nan, rho)\n",
     "    rho = np.where(indefini, 0.0, rho)\n",
     "test_garde_estimateur_artefact_juge_sans_erreur_indefini_jamais_zero"),
    ("D02", "loi 1 : choc tiré par juge et non par témoin", "        choc = rng.random((R, m, 1)) < param\n",
     "        choc = rng.random((R, m, J)) < param\n", "test_formules_correlation_estimee_contre_valeur_plantee"),
    ("D03", "loi 1 : valeur plantée prise sur la grille à taux inégaux",
     "                    C[j, k] = param * (min(p[j], p[k]) - p[j] * p[k])\n",
     "                    C[j, k] = param * math.sqrt(p[j] * (1 - p[j]) * p[k] * (1 - p[k]))\n",
     "test_formules_artefact_valeur_plantee_prise_sur_la_grille_a_taux_inegaux"),
    ("D04", "loi 2 : valeur plantée égale à r",
     "                    C[j, k] = float(np.sum(w * phis[j] * phis[k])) - p[j] * p[k]\n",
     "                    C[j, k] = param * math.sqrt(p[j] * (1 - p[j]) * p[k] * (1 - p[k]))\n",
     "test_formules_valeurs_plantees_exactes_connues"),
    ("D05", "porteuse : arrondi au pair", "    q = 3 + np.floor(x + 0.5)\n", "    q = 3 + np.round(x)\n",
     "test_porteuse_arrondi_au_demi_superieur_et_non_au_pair"),
    ("D06", "unanimité codée à l'envers", "    bras[\"U\"] = Vl.all(axis=-1)\n", "    bras[\"U\"] = ~Vl.any(axis=-1)\n",
     "test_garde_p2_cas_sain_quatre_regles_a_la_meme_erreur_equilibree"),
    ("D07", "double rendu : le second rendu garde le trait",
     "        s1, s2 = np.broadcast_to(t, f1.shape), np.zeros_like(f2)\n",
     "        s1, s2 = np.broadcast_to(t, f1.shape), np.broadcast_to(t, f2.shape)\n",
     "test_double_rendu_taux_exacts_contre_le_calcul"),
    ("D08", "bras C : score au seuil rendu notable",
     "    return (scores - seuil[:, None]) > tolerance_egalite(w, seuil)[:, None]\n",
     "    return (scores - seuil[:, None]) >= -tolerance_egalite(w, seuil)[:, None]\n",
     "test_bras_c_score_au_seuil_rend_non_notable"),
    ("D09", "monde de puissance : écart pris contre l'unanimité",
     "        return e[comparaison] - e[\"au_moins_un\"] - ecart\n",
     "        return e[comparaison] - e[\"unanimite\"] - ecart\n",
     "test_monde_de_puissance_dissymetrie_et_faisabilite_contre_le_calcul"),
    ("D10", "Holm remplacé par des tests non corrigés", "    seuils = alpha / (m - np.arange(m))\n",
     "    seuils = alpha + 0.0 * np.arange(m)\n", "test_holm_pas_a_pas_descendant"),
    ("D11", "binomial exact unilatéral",
     "    pv = np.array([pmf[pmf <= pmf[x] * (1 + 1e-7)].sum() for x in range(m + 1)])\n",
     "    pv = np.array([pmf[: x + 1].sum() for x in range(m + 1)])\n", "test_binomial_exact_bilateral"),
    ("D12", "bras C : poids non ramenés à [0,2 ; 5] fois la moyenne",
     "    w = np.where(repli[:, None], 1.0, borne)\n", "    w = np.where(repli[:, None], 1.0, w)\n",
     "test_bras_c_poids_bornes_aucun_poids_nul_aucun_juge_retire"),
    ("D13", "estimateur : erreurs centrées sur la moyenne globale, non par classe",
     "        Xc = Xc - Xc.mean(axis=-2, keepdims=True)\n", "        Xc = Xc - X.mean(axis=-2, keepdims=True)\n",
     "test_formules_correlation_estimee_contre_valeur_plantee"),
    ("D14", "estimateur : division par n au lieu de n − 2", "    return total / (n - 2)\n", "    return total / n\n",
     "test_covariance_depuis_comptes_egale_covariance_directe"),
    ("D15", "double rendu : bras 1 sans l'exigence d'un vote stable",
     "    return {\"bras_1\": (n_stable >= 1) & stables_notables,\n", "    return {\"bras_1\": stables_notables,\n",
     "test_double_rendu_taux_exacts_contre_le_calcul"),
    ("D16", "loi 3 : coefficient du difficile faux", "    haut = p + 0.75 * a\n", "    haut = p + 0.25 * a\n",
     "test_formules_correlation_estimee_contre_valeur_plantee"),
    ("D17", "loi 4 : probabilité du choc du collège fausse", "        q_tous = param / 3.0\n",
     "        q_tous = param / 2.0\n", "test_formules_correlation_estimee_contre_valeur_plantee"),
    ("D18", "bras R : ρ′ ignorée", "    copie = rng.random((R, n, 1)) < rho_prime\n",
     "    copie = rng.random((R, n, 1)) < 0.0 * rho_prime\n",
     "test_formules_erreur_equilibree_de_chaque_regle_contre_le_paragraphe_0"),
    ("D19", "bras P : paire corrélée non divisée", "            w[masque, j] = w[masque, j] / 2.0\n",
     "            w[masque, j] = w[masque, j] / 1.0\n", "test_bras_p_paire_correlee_divisee_par_deux"),
    ("D20", "clause (iii) : marge de dépendance à la surface fausse",
     "    if abs(e1_moy) >= MARGE_SURFACE and (e1_bas > 0 or e1_haut < 0):\n",
     "    if abs(e1_moy) >= 0.5 and (e1_bas > 0 or e1_haut < 0):\n",
     "test_double_rendu_mots_sans_intervalle_contre_la_sortie_du_calcul"),
    ("D21", "alarme : niveau non divisé par 11", "NIVEAU_ALARME = 0.05 / 11\n", "NIVEAU_ALARME = 0.05\n",
     "test_alarme_bras_a_muet_et_sentinelle_detecte_un_changement_a_effet"),
    ("D22", "clause (ii) : abstention plantée fausse",
     "ABSTENTION_PLANTEE_PAR_VOTE = 2 * (P_FOND - (P_FOND * P_FOND + RHO_PRIME_FOND * P_FOND * (1 - P_FOND)))\n",
     "ABSTENTION_PLANTEE_PAR_VOTE = (P_FOND - (P_FOND * P_FOND + RHO_PRIME_FOND * P_FOND * (1 - P_FOND)))\n",
     "test_double_rendu_taux_exacts_contre_le_calcul"),
    ("D23", "règle choisie : juge 1 seul nommé juge 2 seul", "    (False, False, True, True): \"juge_1_seul\",\n",
     "    (False, False, True, True): \"juge_2_seul\",\n", "test_regle_choisie_deux_juges_cas_sains_et_artefacts"),
    ("D24", "valeur plantée : dénominateur J au lieu de J − 1",
     "    rho_moy = (float(C.sum()) - tr) / ((J - 1) * tr)\n", "    rho_moy = (float(C.sum()) - tr) / (J * tr)\n",
     "test_formules_valeurs_plantees_exactes_connues"),
    ("D25", "manifeste : dérivations des graines omises",
     "                    \"table_cles\": TABLE_CLES, \"derivations\": contexte.derivations},\n",
     "                    \"table_cles\": TABLE_CLES, \"derivations\": []},\n",
     "test_bout_en_bout_essai_manifeste_et_execution_unique"),
    ("D26", "valeur de probabilité sans le « 1 + »",
     "    return (1.0 + (np.asarray(diff) <= EPS).sum(axis=0)) / (B + 1.0)\n",
     "    return ((np.asarray(diff) <= EPS).sum(axis=0)) / (B + 1.0)\n",
     "test_p_valeur_unilaterale_du_reechantillonnage_apparie"),
    ("D27", "audit « trop propre » jamais levé",
     "            \"audit_trop_propre_aucune_replique_hors_intervalle\": bool(couverture == 1.0)}\n",
     "            \"audit_trop_propre_aucune_replique_hors_intervalle\": bool(couverture > 1.0)}\n",
     "test_audit_trop_propre_cellule_sans_replique_hors_intervalle"),
]


def sha256(chemin):
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def lancer(essais, noms, banc, travail):
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(travail / "tmp"), "BANC_LIGNE_3_CHEMIN": str(banc),
                "CHRONOMETRAGE_LIGNE_3_CHEMIN": str(Path(essais).resolve().parent / "chronometrer_banc_ligne_3_v1.py")})
    cmd = [sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider"] + [f"{essais}::{n}" for n in noms]
    r = subprocess.run(cmd, cwd=str(travail), env=env, capture_output=True, text=True, timeout=1800)
    derniere = [ligne for ligne in r.stdout.strip().splitlines() if ligne.strip()][-1:] or [""]
    return r.returncode, derniere[0]


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--banc", required=True)
    parser.add_argument("--essais", required=True)
    parser.add_argument("--travail", required=True)
    parser.add_argument("--sortie", required=True)
    args = parser.parse_args(argv)
    banc = Path(args.banc).resolve()
    essais = Path(args.essais).resolve()
    travail = Path(args.travail).resolve()
    sortie = Path(args.sortie)
    if travail.exists() or sortie.exists():
        print("refus : dossier de travail ou sortie déjà présents", file=sys.stderr)
        return 2
    texte = banc.read_text(encoding="utf-8")
    for ident, _, ancien, neuf, _ in DEFAUTS:
        if texte.count(ancien) != 1 or ancien == neuf:
            print(f"refus : texte ancien de {ident} absent ou multiple", file=sys.stderr)
            return 2
    travail.mkdir(parents=True)
    (travail / "tmp").mkdir()
    vises = sorted({d[4] for d in DEFAUTS})
    code_sain, resume_sain = lancer(essais, vises, banc, travail)
    rapport = {"programme": "controle-defauts-reintroduits-ligne-3-v1", "programme_sha256": sha256(Path(__file__).resolve()),
               "banc_sha256": sha256(banc), "essais_sha256": sha256(essais),
               "essais_vises_sur_le_banc_sain": {"code": code_sain, "resume": resume_sain, "passent": code_sain == 0},
               "defauts": []}
    for ident, description, ancien, neuf, essai in DEFAUTS:
        dossier = travail / ident
        dossier.mkdir()
        copie = dossier / banc.name
        copie.write_text(texte.replace(ancien, neuf, 1), encoding="utf-8")
        code, resume = lancer(essais, [essai], copie, travail)
        rapport["defauts"].append({"id": ident, "description": description, "essai_vise": essai, "code_pytest": code,
                                   "resume": resume, "vu": code == 1})
        print(f"{ident} vu={code == 1} code={code} {resume}")
    rapport["tous_vus"] = all(d["vu"] for d in rapport["defauts"])
    with open(sortie, "x", encoding="utf-8") as f:
        f.write(json.dumps(rapport, ensure_ascii=False, indent=1) + "\n")
    print(f"essais visés sur le banc sain : code={code_sain} {resume_sain}")
    print(f"tous vus : {rapport['tous_vus']}")
    return 0 if (rapport["tous_vus"] and code_sain == 0) else 1


if __name__ == "__main__":
    sys.exit(main())
