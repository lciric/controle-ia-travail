"""Essais d'entrées du script de puissance de la garde δ v8 : les essais de la v7 repris tels quels (GD4-03 à GD5-04, v7 doutes 1 et 2), sauf les dix essais qui
simulaient git (GD4-05 : la v8 n'a aucune commande git, GD7-09 ; remplacés par les essais de `--commit-declare`) ; plus les options de la v8 :
`--rho-comparateurs`, `--combiner-dispersion-a-et-comparateurs`, `--n80-fiche`, `--commit-declare`, et les options des remèdes : `--correlation-sujet-comparateurs` (R2),
`--strates` avec `--amplitude-strates`, `--portee-strates`, `--allocation-strates`, `--calibrage-par-strate` (R3), `--cibles-n80`, `--ecart-contraste-neuvieme` ;
refus nommés et cas sains. Chaque essai lance le script dans un
sous-processus (ce script-ci, pas le script essayé) et lit le code de retour, le message et, s'il est accepté, la sortie.

Usage : python3 -I -B essais-entrees-v8.py SCRIPT_V8 DOSSIER_DE_TRAVAIL_NEUF SORTIE.json
"""

import hashlib
import json
import os
import subprocess
import sys

SCRIPT, TRAVAIL, SORTIE = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]), sys.argv[3]
os.makedirs(TRAVAIL)  # neuf : refus s'il existe
BASE = ["--repetitions", "100", "--tailles", "5", "--deltas", "0.05", "--K", "3", "--taux", "0.01", "--biais", "0",
        "--comparateurs", "1", "--m", "1", "--sans-n80"]
U = ["u1", "u2", "u3", "u4", "u5", "u6"]


def ecrire(nom, contenu):
    with open(os.path.join(TRAVAIL, nom), "w", encoding="utf-8") as f:
        f.write(contenu if isinstance(contenu, str) else json.dumps(contenu))


ecrire("g1.json", {"fA": [0.1, 0.0, 0.2, 0.1, 0.0, 0.1], "fB": [0.0, 0.1, 0.1, 0.1, 0.0, 0.0], "unite": U})
ecrire("g2.json", {"fA": [0.1, 0.1, 0.2, 0.1, 0.0, 0.1], "fB": [0.0, 0.1, 0.1, 0.0, 0.0, 0.0], "unite": U})
ecrire("g1copie.json", open(os.path.join(TRAVAIL, "g1.json")).read())
os.symlink("g1.json", os.path.join(TRAVAIL, "g1lien.json"))
ecrire("c1.json", {"rA": [0.5, 0.4, 0.6, 0.5, 0.3, 0.5], "rB": [0.4, 0.4, 0.4, 0.5, 0.3, 0.4], "unite": U})
ecrire("c2.json", {"rA": [0.6, 0.4, 0.6, 0.5, 0.3, 0.5], "rB": [0.4, 0.3, 0.4, 0.5, 0.3, 0.4], "unite": U})
ecrire("e.json", {"ecarts": [0.1, -0.1, 0.0, 0.05, 0.0, 0.02]})
ecrire("ecopie.json", open(os.path.join(TRAVAIL, "e.json")).read())
ecrire("e2.json", {"ecarts": [0.2, -0.1, 0.0, 0.05, 0.0, 0.02]})
ecrire("csv_souligne.csv", "ecart\n0.0_5\n0.01\n0.0\n0.02\n0.0\n0.01\n")
ecrire("csv_fafb_souligne.csv", "fA,fB\n0.1,0.0_5\n0.1,0.0\n0.0,0.0\n0.2,0.1\n0.0,0.0\n0.1,0.1\n")
ecrire("csv_ok.csv", "ecart\n0.05\n -0.01\n1e-2\n0.0\n+0.02\n.01\n")
for nom, v in (("inf", "inf"), ("nan", "nan"), ("hex", "0x1p-3"), ("arabe", "٠.٠٥"), ("grand", "1e400"), ("virgule", '"0,05"')):
    ecrire(f"csv_{nom}.csv", f"ecart\n{v}\n0.01\n0.0\n0.02\n0.0\n0.01\n")
ecrire("ids_nombres.json", {"ecarts": [0.1, 0.0, 0.0, 0.1, 0.0, 0.0], "unite": [1, 2, 3, 4, 5, 6]})
ecrire("ids_vrai.json", '{"ecarts": [0.1, 0.0, 0.0, 0.1, 0.0, 0.0], "unite": [true, "u2", "u3", "u4", "u5", "u6"]}')
ecrire("ids_nul.json", '{"ecarts": [0.1, 0.0, 0.0, 0.1, 0.0, 0.0], "unite": [null, "u2", "u3", "u4", "u5", "u6"]}')
ecrire("ids_vide.json", {"ecarts": [0.1, 0.0, 0.0, 0.1, 0.0, 0.0], "unite": ["", "u2", "u3", "u4", "u5", "u6"]})
ecrire("ids_liste.json", {"ecarts": [0.1, 0.0, 0.0, 0.1, 0.0, 0.0], "unite": [["u1"], "u2", "u3", "u4", "u5", "u6"]})
ecrire("cle_doublee.json", '{"ecarts": [0.1, 0.0, 0.0, 0.1, 0.0, 0.0], "ecarts": [0.1, 0.0, 0.0, 0.1, 0.0, 0.0]}')
ecrire("entier_grand.json", '{"ecarts": [1234567890123456789012345678901, 0.0, 0.0, 0.1, 0.0, 0.0]}')
ecrire("json_nan.json", '{"ecarts": [NaN, 0.0, 0.0, 0.1, 0.0, 0.0]}')
ecrire("json_souligne.json", '{"ecarts": [0.0_5, 0.0, 0.0, 0.1, 0.0, 0.0]}')
# GD5-04 : mêmes valeurs sous d'autres encodages (sans identifiants pour pouvoir comparer JSON et CSV)
FA = [0.1, 0.0, 0.2, 0.1, 0.0, 0.1]
FB = [0.0, 0.1, 0.1, 0.1, 0.0, 0.0]
RA = [0.5, 0.4, 0.6, 0.5, 0.3, 0.5]
RB = [0.4, 0.4, 0.4, 0.5, 0.3, 0.4]
ecrire("n1.json", {"fA": FA, "fB": FB})
ecrire("n1_reindente.json", json.dumps({"fB": FB, "fA": FA}, indent=4) + "\n")  # autre mise en forme, autre ordre des clés
ecrire("n1.csv", "fA,fB\n" + "".join(f"{a},{b}\n" for a, b in zip(FA, FB)))
ecrire("n1_ecarts.json", {"ecarts": [a - b for a, b in zip(FA, FB)]})  # forme ecarts, même différence flottante
ecrire("n2.json", {"fA": [0.1, 0.1, 0.2, 0.1, 0.0, 0.1], "fB": [0.0, 0.1, 0.1, 0.0, 0.0, 0.0]})
ecrire("z01.json", '{"ecarts": [0.1, -0.1, 0.0, 0.05, 0.0, 0.02]}')
ecrire("z0100.json", '{"ecarts": [0.100, -0.100, 0.0, 0.050, 0.00, 0.020]}')  # 0.100 contre 0.1
ecrire("z_exp.json", '{"ecarts": [1e-1, -1e-1, 0, 5e-2, 0, 2e-2]}')  # exposant, entiers
ecrire("nc1.json", {"rA": RA, "rB": RB})
ecrire("nc1_ecarts.json", {"ecarts": [a - b for a, b in zip(RA, RB)]})
ecrire("nc2.json", {"rA": [0.6, 0.4, 0.6, 0.5, 0.3, 0.5], "rB": [0.4, 0.3, 0.4, 0.5, 0.3, 0.4]})
os.makedirs(os.path.join(TRAVAIL, "dossier.json"))

E = ["--effectif-attendu", "6"]
COMB = ["--echelle-dispersion", "beta", "--combiner-dispersion-a-et-comparateurs", "--effet-unite-beta", "0.17", "--rho-comparateurs", "0.17"]
ESSAIS = [
    # (nom, constat, arguments, attendu, motif attendu dans le message ou contrôle de la sortie, environnement)
    ("csv souligné, colonne ecart", "GD4-03", ["--ecarts", "csv_souligne.csv", "--contraste-synthetique-de-secours"] + E, "refus", "GD4-03"),
    ("csv souligné, colonnes fA,fB", "GD4-03", ["--ecarts", "csv_fafb_souligne.csv", "--contraste-synthetique-de-secours"] + E, "refus", "GD4-03"),
    ("csv inf", "GD4-03", ["--ecarts", "csv_inf.csv", "--contraste-synthetique-de-secours"] + E, "refus", "GD4-03"),
    ("csv nan", "GD4-03", ["--ecarts", "csv_nan.csv", "--contraste-synthetique-de-secours"] + E, "refus", "GD4-03"),
    ("csv hexadécimal", "GD4-03", ["--ecarts", "csv_hex.csv", "--contraste-synthetique-de-secours"] + E, "refus", "GD4-03"),
    ("csv chiffres non ASCII", "GD4-03", ["--ecarts", "csv_arabe.csv", "--contraste-synthetique-de-secours"] + E, "refus", "GD4-03"),
    ("csv 1e400", "GD4-03", ["--ecarts", "csv_grand.csv", "--contraste-synthetique-de-secours"] + E, "refus", "non fini"),
    ("csv virgule décimale entre guillemets", "GD4-03", ["--ecarts", "csv_virgule.csv", "--contraste-synthetique-de-secours"] + E, "refus", "GD4-03"),
    ("csv sain (espace, exposant, signe, .01)", "GD4-03 sain", ["--ecarts", "csv_ok.csv", "--contraste-synthetique-de-secours"] + E, "accepte", None),
    ("json souligné", "GD4-03", ["--ecarts", "json_souligne.json", "--contraste-synthetique-de-secours"] + E, "refus", "JSON illisible"),
    ("--deltas 0.0_5", "GD4-03", ["--deltas", "0.0_5"], "refus", "GD4-03"),
    ("--biais 0_0", "GD4-03", ["--biais", "0_0"], "refus", "GD4-03"),
    ("--taux 0.0_1", "GD4-03", ["--taux", "0.0_1"], "refus", "GD4-03"),
    ("--repetitions 1_000", "GD4-03", ["--repetitions", "1_000"], "refus", "GD4-03"),
    ("--repetitions 1e3", "GD4-03", ["--repetitions", "1e3"], "refus", "GD4-03"),
    ("--graine 1_2", "GD4-03", ["--graine", "1_2"], "refus", "GD4-03"),
    ("--alpha 0.0_5", "GD4-03", ["--alpha", "0.0_5"], "refus", "GD4-03"),
    ("--effet-unite-a 0_5", "GD4-03", ["--effet-unite-a", "0_5"], "refus", "GD4-03"),
    ("--effet-unite-beta 0.1_7", "GD4-03", ["--effet-unite-beta", "0.1_7"], "refus", "GD4-03"),
    ("--ecart-contraste 0.1_0", "GD4-03", ["--ecart-contraste", "0.1_0"], "refus", "GD4-03"),
    ("--tailles 1_0", "GD4-03", ["--tailles", "1_0"], "refus", "GD4-03"),
    ("--tailles-garde 1_0", "GD4-03", ["--tailles-garde", "1_0"], "refus", "GD4-03"),
    ("--comparateurs 1_0", "GD4-03", ["--comparateurs", "1_0"], "refus", "GD4-03"),
    ("--m 8_0", "GD4-03", ["--m", "8_0"], "refus", "GD4-03"),
    ("--K 1_0", "GD4-03", ["--K", "1_0"], "refus", "GD4-03"),
    ("--K-sabotes 1_0", "GD4-03", ["--K-sabotes", "1_0"], "refus", "GD4-03"),
    ("--m-fiches 2_0", "GD4-03", ["--lecture-ebh", "A", "--m-fiches", "2_0"], "refus", "GD4-03"),
    ("--fiches-nulles 1_0", "GD4-03", ["--lecture-ebh", "A", "--fiches-nulles", "1_0"], "refus", "GD4-03"),
    ("--effectif-attendu 0_6", "GD4-03", ["--ecarts", "g1.json", "--contraste-synthetique-de-secours", "--effectif-attendu", "0_6"], "refus", "GD4-03"),
    ("--deltas inf", "GD4-03", ["--deltas", "inf"], "refus", "GD4-03"),
    ("--deltas virgule finale", "GD4-03", ["--deltas", "0.05,"], "refus", "GD4-03"),
    ("--deltas chiffre non ASCII", "GD4-03", ["--deltas", "٠.٠٥"], "refus", "GD4-03"),
    ("--deltas ' 5e-2' (sain)", "GD4-03 sain", ["--deltas", " 5e-2"], "accepte", None),
    ("même fichier, ./", "GD4-04", ["--ecarts", "g1.json,./g1.json", "--ecarts-contraste", "c1.json,c2.json", "--comparateurs", "2"] + E, "refus", "chemin résolu"),
    ("même fichier par lien symbolique", "GD4-04", ["--ecarts", "g1.json,g1lien.json", "--ecarts-contraste", "c1.json,c2.json", "--comparateurs", "2"] + E, "refus", "chemin résolu"),
    ("même contenu, deux noms", "GD4-04", ["--ecarts", "g1.json,g1copie.json", "--ecarts-contraste", "c1.json,c2.json", "--comparateurs", "2"] + E, "refus", "même contenu"),
    ("même fichier en garde et en contraste par ./", "GD4-04", ["--ecarts", "e.json", "--ecarts-contraste", "./e.json"] + E, "refus", "chemin résolu"),
    ("même contenu en garde et en contraste", "GD4-04", ["--ecarts", "e.json", "--ecarts-contraste", "ecopie.json"] + E, "refus", "même contenu"),
    ("fichiers distincts (sain)", "GD4-04 sain", ["--ecarts", "g1.json,g2.json", "--ecarts-contraste", "c1.json,c2.json", "--comparateurs", "2"] + E, "accepte", None),
    ("GD5-04 JSON réindenté, clés dans un autre ordre", "GD5-04", ["--ecarts", "n1.json,n1_reindente.json", "--ecarts-contraste", "nc1.json,nc2.json", "--comparateurs", "2"] + E, "refus", "doublon de valeurs"),
    ("GD5-04 JSON contre CSV aux mêmes valeurs", "GD5-04", ["--ecarts", "n1.json,n1.csv", "--ecarts-contraste", "nc1.json,nc2.json", "--comparateurs", "2"] + E, "refus", "doublon de valeurs"),
    ("GD5-04 fA,fB contre la forme ecarts", "GD5-04", ["--ecarts", "n1.json,n1_ecarts.json", "--ecarts-contraste", "nc1.json,nc2.json", "--comparateurs", "2"] + E, "refus", "doublon de valeurs"),
    ("GD5-04 0.1 contre 0.100", "GD5-04", ["--ecarts", "z01.json,z0100.json", "--ecarts-contraste", "nc1.json,nc2.json", "--comparateurs", "2"] + E, "refus", "doublon de valeurs"),
    ("GD5-04 0.1 contre 1e-1", "GD5-04", ["--ecarts", "z01.json,z_exp.json", "--ecarts-contraste", "nc1.json,nc2.json", "--comparateurs", "2"] + E, "refus", "doublon de valeurs"),
    ("GD5-04 contraste de mêmes valeurs que la garde", "GD5-04", ["--ecarts", "n1.json", "--ecarts-contraste", "n1_ecarts.json"] + E, "refus", "doublon de valeurs"),
    ("GD5-04 deux contrastes de mêmes valeurs", "GD5-04", ["--ecarts", "n1.json,n2.json", "--ecarts-contraste", "nc1.json,nc1_ecarts.json", "--comparateurs", "2"] + E, "refus", "doublon de valeurs"),
    ("GD5-04 valeurs distinctes sans identifiants (sain)", "GD5-04 sain", ["--ecarts", "n1.json,n2.json", "--ecarts-contraste", "nc1.json,nc2.json", "--comparateurs", "2"] + E, "accepte", None),
    ("GD5-04 CSV et JSON de valeurs distinctes (sain)", "GD5-04 sain", ["--ecarts", "n2.json,n1.csv", "--ecarts-contraste", "nc1.json,nc2.json", "--comparateurs", "2"] + E, "accepte", None),
    ("GD5-01 effet des comparateurs σ = 1 (sain) : décomposition et nom", "GD5-01 sain", ["--effet-unite-comparateurs", "1.0", "--comparateurs", "2"], "accepte", "effet_comparateurs"),
    ("GD5-01 effet des comparateurs σ = 1, ρ = 0,17 (sain)", "GD5-01 sain", ["--effet-unite-comparateurs", "1.0", "--correlation-comparateurs", "0.17", "--comparateurs", "2"], "accepte", "effet_comparateurs_rho"),
    ("GD5-01 effet des comparateurs avec lien coupé (sain)", "GD5-01 sain", ["--effet-unite-comparateurs", "0.5", "--lien-coupe", "--comparateurs", "2"], "accepte", "effet_comparateurs_coupe"),
    ("GD5-01 effet sur A et sur les comparateurs ensemble (sain)", "GD5-01 sain", ["--effet-unite-a", "1.0", "--effet-unite-comparateurs", "1.0", "--comparateurs", "2"], "accepte", None),
    ("GD5-01 ρ sans σ", "GD5-01", ["--correlation-comparateurs", "0.17"], "refus", "sans objet"),
    ("GD5-01 σ négatif", "GD5-01", ["--effet-unite-comparateurs", "-1"], "refus", "effet-unite-comparateurs"),
    ("GD5-01 σ trop grand", "GD5-01", ["--effet-unite-comparateurs", "3.5"], "refus", "effet-unite-comparateurs"),
    ("GD5-01 ρ = 1", "GD5-01", ["--effet-unite-comparateurs", "1", "--correlation-comparateurs", "1"], "refus", "ρ dans"),
    ("GD5-01 ρ négatif", "GD5-01", ["--effet-unite-comparateurs", "1", "--correlation-comparateurs", "-0.1"], "refus", "ρ dans"),
    ("GD5-01 σ 1_0 (souligné)", "GD4-03", ["--effet-unite-comparateurs", "1_0"], "refus", "GD4-03"),
    ("GD5-01 ρ 0.1_7 (souligné)", "GD4-03", ["--effet-unite-comparateurs", "1", "--correlation-comparateurs", "0.1_7"], "refus", "GD4-03"),
    ("GD5-01 effet des comparateurs avec bêta", "GD5-01", ["--effet-unite-comparateurs", "1", "--effet-unite-beta", "0.1"], "refus", "croisement"),
    ("GD5-02 fiches nulles : borne α_c·m₀/m écrite", "GD5-02 sain", ["--lecture-ebh", "A,B", "--fiches-nulles", "2", "--comparateurs", "3", "--m", "2"], "accepte", "borne_nulles"),
    ("--ecarts vide", "GD4-06", ["--ecarts", ""], "refus", "nom de fichier vide"),
    ("--ecarts-contraste vide", "GD4-06", ["--ecarts", "g1.json", "--ecarts-contraste", ""] + E, "refus", "nom de fichier vide"),
    ("--ecarts virgule finale", "GD4-06", ["--ecarts", "g1.json,", "--contraste-synthetique-de-secours"] + E, "refus", "nom de fichier vide"),
    ("fichier absent", "GD4-06", ["--ecarts", "absent.json", "--contraste-synthetique-de-secours"] + E, "refus", "fichier absent"),
    ("dossier à la place d'un fichier", "GD4-06", ["--ecarts", "dossier.json", "--contraste-synthetique-de-secours"] + E, "refus", "dossier"),
    ("secours sans fichier", "GD4-06", ["--contraste-synthetique-de-secours"], "refus", "sans objet"),
    ("secours avec contraste réel", "GD4-06", ["--ecarts", "g1.json", "--ecarts-contraste", "c1.json", "--contraste-synthetique-de-secours"] + E, "refus", "sans objet"),
    ("secours qui sert (sain) : loi nommée", "GD4-06 sain", ["--ecarts", "g1.json", "--contraste-synthetique-de-secours"] + E, "accepte", "secours_nomme"),
    ("sans secours (sain) : option non écrite", "GD4-06 sain", [], "accepte", "secours_absent"),
    ("τ = 0", "GD4-06", ["--taux", "0"], "refus", "taux"),
    ("τ = 0 dans une liste", "GD4-06", ["--taux", "0,0.01"], "refus", "taux"),
    ("effet logit, τ + biais = 1", "GD4-06", ["--effet-unite-a", "1", "--taux", "0.99", "--biais", "0.01", "--deltas", "0.005"], "refus", "sans effet possible"),
    ("effet bêta, τ + biais = 1", "GD4-06", ["--effet-unite-beta", "0.2", "--taux", "0.99", "--biais", "0.01", "--deltas", "0.005"], "refus", "sans effet possible"),
    ("identifiants nombres", "GD4-06", ["--ecarts", "ids_nombres.json", "--contraste-synthetique-de-secours"] + E, "refus", "chaînes non vides"),
    ("identifiant true", "GD4-06", ["--ecarts", "ids_vrai.json", "--contraste-synthetique-de-secours"] + E, "refus", "chaînes non vides"),
    ("identifiant null", "GD4-06", ["--ecarts", "ids_nul.json", "--contraste-synthetique-de-secours"] + E, "refus", "chaînes non vides"),
    ("identifiant vide", "GD4-06", ["--ecarts", "ids_vide.json", "--contraste-synthetique-de-secours"] + E, "refus", "chaînes non vides"),
    ("identifiant liste", "GD4-06", ["--ecarts", "ids_liste.json", "--contraste-synthetique-de-secours"] + E, "refus", "chaînes non vides"),
    ("identifiants chaînes (sain)", "GD4-06 sain", ["--ecarts", "g1.json", "--ecarts-contraste", "c1.json"] + E, "accepte", None),
    ("clé JSON doublée : motif gardé", "GD4-06", ["--ecarts", "cle_doublee.json", "--contraste-synthetique-de-secours"] + E, "refus", "clé JSON doublée"),
    ("entier démesuré : motif gardé", "GD4-06", ["--ecarts", "entier_grand.json", "--contraste-synthetique-de-secours"] + E, "refus", "entier démesuré"),
    ("NaN en JSON", "GD4-06", ["--ecarts", "json_nan.json", "--contraste-synthetique-de-secours"] + E, "refus", "NaN"),
    ("--lien-coupe sans effet", "options v5", ["--lien-coupe"], "refus", "sans objet"),
    ("--lien-coupe avec bêta", "options v5", ["--lien-coupe", "--effet-unite-beta", "0.1"], "refus", "sans objet"),
    ("deux effets ensemble", "options v5", ["--effet-unite-a", "1", "--effet-unite-beta", "0.1"], "refus", "un seul effet"),
    ("--m-fiches sans lecture e-BH", "options v5", ["--m-fiches", "2"], "refus", "sans objet"),
    ("--lecture-ebh C", "options v5", ["--lecture-ebh", "C"], "refus", "lecture-ebh"),
    ("--lecture-ebh A,A", "options v5", ["--lecture-ebh", "A,A"], "refus", "lecture-ebh"),
    ("fiches nulles et fichiers réels", "options v5", ["--ecarts", "g1.json", "--ecarts-contraste", "c1.json", "--lecture-ebh", "A", "--fiches-nulles", "1"] + E, "refus", "synthétiques seulement"),
    ("lecture e-BH sur fichiers réels (sain)", "options v5 sain", ["--ecarts", "g1.json", "--ecarts-contraste", "c1.json", "--lecture-ebh", "A,B"] + E, "accepte", "ebh_reel"),
    ("--sortie non .json", "GD4-05", ["--sortie", "x.txt", "--commit-declare", "essai"], "refus", ".json"),
    ("--sortie (sain) : journal et manifeste", "GD4-05 sain", ["--sortie", "passage.json", "--commit-declare", "essai 0123abcd"], "accepte", "manifeste"),
    ("--sortie existante", "GD4-05 / R12", ["--sortie", "passage.json", "--commit-declare", "essai 0123abcd"], "refus", "R12"),
    ("--sortie sans --commit-declare", "GD7-09", ["--sortie", "sans-commit.json"], "refus", "commit-declare"),
    ("--commit-declare vide", "GD7-09", ["--commit-declare", " "], "refus", "commit-declare"),
    ("--commit-declare trop long", "GD7-09", ["--commit-declare", "x" * 501], "refus", "commit-declare"),
    ("--commit-declare sans --sortie (sain) : accepté, recopié", "GD7-09 sain", ["--commit-declare", "essai 0123abcd"], "accepte", "commit_stdout"),
    ("sans --commit-declare ni --sortie (sain) : commit nul, état « non lu »", "GD7-09 sain", [], "accepte", "commit_nul"),
    # --- v7, doute 1 : échelle de la dispersion des comparateurs
    ("v7 --echelle-dispersion beta, σ = 1 (sain) : loi nommée _beta, κ écrite", "v7 doute 1 sain", ["--effet-unite-comparateurs", "1.0", "--echelle-dispersion", "beta", "--comparateurs", "2"], "accepte", "beta_sain"),
    ("v7 --echelle-dispersion logit explicite (sain) : identique au défaut", "v7 doute 1 sain", ["--effet-unite-comparateurs", "1.0", "--echelle-dispersion", "logit", "--comparateurs", "2"], "accepte", "logit_explicite"),
    ("v7 bêta sans σ", "v7 doute 1", ["--echelle-dispersion", "beta"], "refus", "sans objet"),
    ("v7 bêta avec σ = 0 explicite", "v7 doute 1", ["--echelle-dispersion", "beta", "--effet-unite-comparateurs", "0"], "refus", "sans objet"),
    ("v7 échelle inconnue", "v7 doute 1", ["--echelle-dispersion", "gamma", "--effet-unite-comparateurs", "1"], "refus", "logit ou beta"),
    ("v7 échelle en majuscules", "v7 doute 1", ["--echelle-dispersion", "Beta", "--effet-unite-comparateurs", "1"], "refus", "logit ou beta"),
    ("v7 bêta avec corrélation entre comparateurs", "v7 doute 1", ["--echelle-dispersion", "beta", "--effet-unite-comparateurs", "1", "--correlation-comparateurs", "0.17"], "refus", "non traitée"),
    ("v7 bêta avec --lien-coupe sans effet sur A", "v7 doute 1", ["--echelle-dispersion", "beta", "--effet-unite-comparateurs", "1", "--lien-coupe"], "refus", "sans objet"),
    ("v7 bêta avec effet sur A et --lien-coupe (sain : le lien coupé porte sur A)", "v7 doute 1 sain", ["--echelle-dispersion", "beta", "--effet-unite-comparateurs", "1", "--effet-unite-a", "1", "--lien-coupe", "--comparateurs", "2"], "accepte", "beta_A_coupe"),
    ("v7 bêta avec --effet-unite-beta (croisement, déjà refusé en v6)", "v7 doute 1", ["--echelle-dispersion", "beta", "--effet-unite-comparateurs", "1", "--effet-unite-beta", "0.1"], "refus", "croisement"),
    ("v7 bêta avec fiches nulles et lectures A,B (sain)", "v7 doute 1 sain", ["--echelle-dispersion", "beta", "--effet-unite-comparateurs", "0.5", "--lecture-ebh", "A,B", "--fiches-nulles", "1", "--comparateurs", "2", "--m", "2"], "accepte", "beta_nulles"),
    # --- v7, doute 2 : K_s en produit cartésien
    ("v7 --K-s 5,3 (sain) : lois Kh3_Ks5 et Kh3_Ks3", "v7 doute 2 sain", ["--K-s", "5,3"], "accepte", "K_s_cartesien"),
    ("v7 --K 10,5 --K-s 10,5,3 (sain) : 6 lois", "v7 doute 2 sain", ["--K", "10,5", "--K-s", "10,5,3"], "accepte", "K_s_six"),
    ("v7 --K-s avec --K-sabotes", "v7 doute 2", ["--K-s", "5", "--K-sabotes", "3"], "refus", "un seul des deux"),
    ("v7 --K-s 1_0 (souligné)", "GD4-03", ["--K-s", "1_0"], "refus", "GD4-03"),
    ("v7 --K-s 0", "v7 doute 2", ["--K-s", "0"], "refus", "K-s"),
    ("v7 --K-s virgule finale", "v7 doute 2", ["--K-s", "5,"], "refus", "GD4-03"),
    ("v7 --K-s doublé", "v7 doute 2", ["--K-s", "5,5"], "refus", "doublées"),
    ("v7 --K 3,3 --K-s 5 (paire doublée)", "v7 doute 2", ["--K", "3,3", "--K-s", "5"], "refus", "doublée"),
    ("v7 --K-sabotes seul (sain, comportement v6 gardé)", "v7 doute 2 sain", ["--K-sabotes", "5"], "accepte", "K_sabotes"),
    # --- v8 : dispersion de A combinée à celle des comparateurs, ρ direct, n80 de la fiche
    ("v8 --rho-comparateurs 0.1 --echelle-dispersion beta (sain) : loi _rhoB0.1_beta, κ = 9", "v8 sain", ["--echelle-dispersion", "beta", "--rho-comparateurs", "0.1", "--comparateurs", "2"], "accepte", "rho_direct"),
    ("v8 --rho-comparateurs sans échelle bêta", "v8", ["--rho-comparateurs", "0.1"], "refus", "sans objet"),
    ("v8 --rho-comparateurs avec échelle logit explicite", "v8", ["--rho-comparateurs", "0.1", "--echelle-dispersion", "logit"], "refus", "sans objet"),
    ("v8 --rho-comparateurs avec --effet-unite-comparateurs", "v8", ["--echelle-dispersion", "beta", "--rho-comparateurs", "0.1", "--effet-unite-comparateurs", "1"], "refus", "un seul des deux"),
    ("v8 --rho-comparateurs = 1", "v8", ["--echelle-dispersion", "beta", "--rho-comparateurs", "1"], "refus", "ρ dans [0 ; 1["),
    ("v8 --rho-comparateurs négatif", "v8", ["--echelle-dispersion", "beta", "--rho-comparateurs", "-0.1"], "refus", "ρ dans [0 ; 1["),
    ("v8 --rho-comparateurs 0.1_7 (souligné)", "GD4-03", ["--echelle-dispersion", "beta", "--rho-comparateurs", "0.1_7"], "refus", "GD4-03"),
    ("v8 --rho-comparateurs avec corrélation entre comparateurs", "v8", ["--echelle-dispersion", "beta", "--rho-comparateurs", "0.1", "--correlation-comparateurs", "0.2"], "refus", "corr"),
    ("v8 --rho-comparateurs avec --lien-coupe sans effet sur A", "v8", ["--echelle-dispersion", "beta", "--rho-comparateurs", "0.1", "--lien-coupe"], "refus", "sans objet"),
    ("v8 --rho-comparateurs 0 avec échelle bêta (sans objet, comme σ = 0)", "v8", ["--echelle-dispersion", "beta", "--rho-comparateurs", "0"], "refus", "sans objet"),
    ("v8 croisement A bêta et B bêta sans l'option : refusé comme en v7 (σ)", "GD7-03", ["--echelle-dispersion", "beta", "--effet-unite-comparateurs", "1", "--effet-unite-beta", "0.1"], "refus", "croisement"),
    ("v8 croisement A bêta et B bêta sans l'option : refusé (ρ direct)", "GD7-03", ["--echelle-dispersion", "beta", "--rho-comparateurs", "0.1", "--effet-unite-beta", "0.1"], "refus", "croisement"),
    ("v8 croisement A bêta et B bêta avec l'option, σ (sain) : loi _betaA_rho0.1…_beta", "GD7-03 sain", ["--echelle-dispersion", "beta", "--effet-unite-comparateurs", "1", "--effet-unite-beta", "0.1", "--combiner-dispersion-a-et-comparateurs", "--comparateurs", "2"], "accepte", "combine_sigma"),
    ("v8 croisement A bêta et B bêta avec l'option, ρ direct (sain) : ρ_A = 0.17, ρ_B = 0.085", "GD7-03 sain", ["--echelle-dispersion", "beta", "--rho-comparateurs", "0.085", "--effet-unite-beta", "0.17", "--combiner-dispersion-a-et-comparateurs", "--comparateurs", "2"], "accepte", "combine_rho"),
    ("v8 --combiner… sans effet sur A", "GD7-03", ["--echelle-dispersion", "beta", "--rho-comparateurs", "0.1", "--combiner-dispersion-a-et-comparateurs"], "refus", "sans objet"),
    ("v8 --combiner… sans comparateurs dispersés", "GD7-03", ["--effet-unite-beta", "0.1", "--combiner-dispersion-a-et-comparateurs"], "refus", "sans objet"),
    ("v8 --combiner… avec comparateurs en échelle logit", "GD7-03", ["--effet-unite-comparateurs", "1", "--effet-unite-beta", "0.1", "--combiner-dispersion-a-et-comparateurs"], "refus", "sans objet"),
    ("v8 --combiner… avec --lien-coupe (le lien est déjà coupé)", "GD7-03", ["--echelle-dispersion", "beta", "--rho-comparateurs", "0.1", "--effet-unite-beta", "0.1", "--combiner-dispersion-a-et-comparateurs", "--lien-coupe"], "refus", "sans objet"),
    ("v8 --combiner… avec --effet-unite-a (deux effets sur A)", "GD7-03", ["--echelle-dispersion", "beta", "--rho-comparateurs", "0.1", "--effet-unite-beta", "0.1", "--effet-unite-a", "1", "--combiner-dispersion-a-et-comparateurs"], "refus", "un seul effet"),
    ("v8 A bêta seul (sain, comportement v7 gardé, sans option)", "v8 sain", ["--effet-unite-beta", "0.1", "--comparateurs", "2"], "accepte", "A_beta_seul"),
    ("v8 --n80-fiche (sain) : courbe, trois mesures", "v8 sain", ["--lecture-ebh", "A", "--m", "8,2", "--n80-fiche", "--comparateurs", "2", "--tailles", "8", "--K", "5", "--K-s", "5", "--repetitions", "100"], "accepte", "n80_fiche"),
    ("v8 --n80-fiche sans lecture e-BH", "v8", ["--n80-fiche"], "refus", "lecture-ebh"),
    ("v8 --n80-fiche avec lecture (B) seule", "v8", ["--n80-fiche", "--lecture-ebh", "B"], "refus", "lecture-ebh"),
    ("v8 --n80-fiche avec fiches nulles", "v8", ["--n80-fiche", "--lecture-ebh", "A", "--fiches-nulles", "1"], "refus", "sans fiche nulle"),
    ("v8 --n80-fiche avec fichiers réels", "v8", ["--n80-fiche", "--lecture-ebh", "A", "--ecarts", "g1.json", "--contraste-synthetique-de-secours"] + E, "refus", "synthétiques seulement"),
    # --- v8, remèdes : copule (R2), strates (R3), cibles de n80, neuvième comparateur
    ("v8 copule c = 0,5 (sain) : loi _copuleAB0.5, corrélations tirées écrites", "R2 sain", COMB + ["--correlation-sujet-comparateurs", "0.5", "--comparateurs", "2"], "accepte", "copule"),
    ("v8 copule c = 0 : chemin sans copule (sain), loi sans _copuleAB", "R2 sain", COMB + ["--correlation-sujet-comparateurs", "0", "--comparateurs", "2"], "accepte", "copule_nulle"),
    ("v8 copule c = 1", "R2", COMB + ["--correlation-sujet-comparateurs", "1"], "refus", "c dans [0 ; 1["),
    ("v8 copule c négatif", "R2", COMB + ["--correlation-sujet-comparateurs", "-0.2"], "refus", "c dans [0 ; 1["),
    ("v8 copule c souligné", "GD4-03", COMB + ["--correlation-sujet-comparateurs", "0.5_0"], "refus", "GD4-03"),
    ("v8 copule sans --combiner-dispersion-a-et-comparateurs", "R2", ["--echelle-dispersion", "beta", "--rho-comparateurs", "0.17", "--correlation-sujet-comparateurs", "0.5"], "refus", "sans objet"),
    ("v8 copule avec strates", "R2/R3", COMB + ["--correlation-sujet-comparateurs", "0.5", "--strates", "3", "--amplitude-strates", "0.3", "--portee-strates", "sujet"], "refus", "non traité"),
    ("v8 copule avec neuvième comparateur", "R2", COMB + ["--correlation-sujet-comparateurs", "0.5", "--comparateurs", "9", "--ecart-contraste-neuvieme", "0.05"], "refus", "non traité"),
    ("v8 strates 3, γ = 0,4, sujet, étalonnées (sain) : loi _strates3g0.4sujet_calibre_bloc", "R3 sain", COMB + ["--strates", "3", "--amplitude-strates", "0.4", "--portee-strates", "sujet", "--calibrage-par-strate", "--comparateurs", "2", "--tailles", "12"], "accepte", "strates"),
    ("v8 strates 2, γ = 0,3, commune, brutes, tirage indépendant (sain)", "R3 sain", COMB + ["--strates", "2", "--amplitude-strates", "0.3", "--portee-strates", "commune", "--allocation-strates", "iid", "--comparateurs", "2", "--tailles", "12"], "accepte", "strates_iid"),
    ("v8 strates 4", "R3", COMB + ["--strates", "4", "--amplitude-strates", "0.3", "--portee-strates", "sujet"], "refus", "--strates"),
    ("v8 strates 1", "R3", COMB + ["--strates", "1", "--amplitude-strates", "0.3", "--portee-strates", "sujet"], "refus", "--strates"),
    ("v8 strates sans amplitude", "R3", COMB + ["--strates", "3", "--portee-strates", "sujet"], "refus", "amplitude"),
    ("v8 strates amplitude = 1", "R3", COMB + ["--strates", "3", "--amplitude-strates", "1", "--portee-strates", "sujet"], "refus", "amplitude"),
    ("v8 strates sans portée", "R3", COMB + ["--strates", "3", "--amplitude-strates", "0.3"], "refus", "portee"),
    ("v8 strates portée inconnue", "R3", COMB + ["--strates", "3", "--amplitude-strates", "0.3", "--portee-strates", "toutes"], "refus", "portee"),
    ("v8 strates allocation inconnue", "R3", COMB + ["--strates", "3", "--amplitude-strates", "0.3", "--portee-strates", "sujet", "--allocation-strates", "hasard"], "refus", "allocation"),
    ("v8 strates sans --combiner-dispersion-a-et-comparateurs", "R3", ["--echelle-dispersion", "beta", "--rho-comparateurs", "0.17", "--strates", "3", "--amplitude-strates", "0.3", "--portee-strates", "sujet"], "refus", "combiner"),
    ("v8 amplitude sans --strates", "R3", COMB + ["--amplitude-strates", "0.3"], "refus", "sans objet"),
    ("v8 --calibrage-par-strate sans --strates", "R3", COMB + ["--calibrage-par-strate"], "refus", "sans objet"),
    ("v8 --allocation-strates iid sans --strates", "R3", COMB + ["--allocation-strates", "iid"], "refus", "sans objet"),
    ("v8 strates : variance prévue par la strate au-delà de ρ (γ = 0,9, ρ = 0,17)", "R3", COMB + ["--strates", "3", "--amplitude-strates", "0.9", "--portee-strates", "sujet"], "refus", "réduire --amplitude-strates"),
    ("v8 strates : γ = 0,999 avec ρ = 0,9 (variance de strate au-delà de ρ)", "R3", COMB + ["--strates", "2", "--amplitude-strates", "0.999", "--portee-strates", "sujet", "--rho-comparateurs", "0.9", "--effet-unite-beta", "0.9"], "refus", "--amplitude-strates"),
    ("v8 --cibles-n80 0.8,0.9 (sain) : n80 et n90", "v8 sain", ["--lecture-ebh", "A", "--m", "8,2", "--n80-fiche", "--cibles-n80", "0.8,0.9", "--comparateurs", "2", "--tailles", "8", "--K", "5", "--K-s", "5", "--repetitions", "100"], "accepte", "cibles"),
    ("v8 --cibles-n80 sans --n80-fiche", "v8", ["--cibles-n80", "0.9"], "refus", "sans objet"),
    ("v8 --cibles-n80 = 1", "v8", ["--lecture-ebh", "A", "--n80-fiche", "--cibles-n80", "1"], "refus", "cibles-n80"),
    ("v8 --cibles-n80 doublées", "v8", ["--lecture-ebh", "A", "--n80-fiche", "--cibles-n80", "0.8,0.8"], "refus", "cibles-n80"),
    ("v8 --cibles-n80 0", "v8", ["--lecture-ebh", "A", "--n80-fiche", "--cibles-n80", "0"], "refus", "cibles-n80"),
    ("v8 --cibles-n80 virgule décimale", "GD4-03", ["--lecture-ebh", "A", "--n80-fiche", "--cibles-n80", "0,9"], "refus", "cibles-n80"),
    ("v8 neuvième comparateur E = 0,05, k = 9 (sain) : loi _neuf0.05, E_rB du neuvième ≈ 0,45", "neuf sain", ["--comparateurs", "9", "--ecart-contraste-neuvieme", "0.05", "--effet-unite-comparateurs", "1.0", "--tailles", "12", "--biais", "0.0125"], "accepte", "neuvieme"),
    ("v8 neuvième comparateur E = 0,05, k = 8 et 9 ensemble (sain) : k = 8 sans neuvième", "neuf sain", ["--comparateurs", "8,9", "--ecart-contraste-neuvieme", "0.05", "--effet-unite-comparateurs", "1.0", "--tailles", "12"], "accepte", "neuvieme_deux_k"),
    ("v8 neuvième comparateur E = écart de contraste (0,10) : comme sans l'option (sain)", "neuf sain", ["--comparateurs", "9", "--ecart-contraste-neuvieme", "0.10", "--tailles", "12"], "accepte", "neuvieme_egal"),
    ("v8 neuvième comparateur avec k = 8 seulement", "neuf", ["--comparateurs", "8", "--ecart-contraste-neuvieme", "0.05"], "refus", "k ≥ 9"),
    ("v8 neuvième comparateur E = 0", "neuf", ["--comparateurs", "9", "--ecart-contraste-neuvieme", "0"], "refus", "E dans ]0 ; 0,6["),
    ("v8 neuvième comparateur E = 0,6", "neuf", ["--comparateurs", "9", "--ecart-contraste-neuvieme", "0.6"], "refus", "E dans ]0 ; 0,6["),
    ("v8 neuvième comparateur E souligné", "GD4-03", ["--comparateurs", "9", "--ecart-contraste-neuvieme", "0.0_5"], "refus", "GD4-03"),
    ("v8 neuvième comparateur avec fichiers réels", "neuf", ["--comparateurs", "9", "--ecart-contraste-neuvieme", "0.05", "--ecarts", "g1.json", "--contraste-synthetique-de-secours"] + E, "refus", "fichiers réels"),
    ("v8 K_s = 20 (sain) : loi Ks20", "R4 sain", ["--K", "5", "--K-s", "20", "--tailles", "12"], "accepte", "ks20"),
    ("v7 --K-s avec fichiers réels (sain : secours sur la première paire)", "v7 doute 2 sain", ["--ecarts", "g1.json", "--contraste-synthetique-de-secours", "--K-s", "5"] + E, "accepte", "secours_K_s"),
]

resultats = []
for nom, constat, args, attendu, controle in ESSAIS:
    env = dict(os.environ)
    r = subprocess.run([sys.executable, "-I", "-B", SCRIPT] + BASE + args, capture_output=True, text=True, cwd=TRAVAIL, env=env,
                       timeout=600)
    message = (r.stderr.strip().splitlines() or [""])[-1]
    obtenu = "accepte" if r.returncode == 0 else ("refus" if message.startswith("refus : ") else "erreur brute")
    ok = obtenu == attendu
    detail = None
    if ok and attendu == "refus" and controle and controle not in message:
        ok, detail = False, f"motif attendu « {controle} » absent"
    if ok and attendu == "accepte" and controle:
        if controle == "manifeste":
            m = json.load(open(os.path.join(TRAVAIL, "manifeste-passage.json")))
            empreintes = {f: hashlib.sha256(open(os.path.join(TRAVAIL, f), "rb").read()).hexdigest() for f in m["fichiers"]}
            ok = (sorted(m["fichiers"]) == ["passage-journal.txt", "passage.json"] and empreintes == m["fichiers"]
                  and m["script"]["sha256"] == hashlib.sha256(open(SCRIPT, "rb").read()).hexdigest()
                  and m["graines"]["graine_maitresse"] == 20261029 and m["script"]["commit"] == "essai 0123abcd"
                  and m["script"]["etat_du_script"].startswith("non lu") and m["environnement"]["plateforme"].startswith("Linux"))
            detail = {"fichiers": m["fichiers"], "etat_du_script": m["script"]["etat_du_script"], "commit": m["script"]["commit"]}
        else:
            s = json.loads(r.stdout)
            if controle == "secours_nomme":
                c = s["lois"]["reelle_recentree"].get("contraste", "")
                ok = "synthétique de secours" in c and s["reglages"].get("contraste_synthetique_de_secours") is True
                detail = c
            elif controle == "secours_absent":
                ok = "contraste_synthetique_de_secours" not in s["reglages"]
            elif controle in ("effet_comparateurs", "effet_comparateurs_rho", "effet_comparateurs_coupe"):
                noms = list(s["lois"])
                nom_effet = [x for x in noms if "effetB" in x and "lien_coupe" not in x]
                nom_coupe = [x for x in noms if "effetB" in x and "lien_coupe" in x]
                dec = s["lois"][noms[0]]["decomposition_effet_unite"]["biais=0.0"]
                ok = bool(nom_effet) and "comparateurs_honnetes_fB" in dec and "comparateurs_sabotes_rB" in dec
                ok = ok and s["reglages"]["effet_unite_comparateurs"] > 0
                if controle == "effet_comparateurs_rho":
                    ok = ok and any("corrB0.17" in x for x in noms) and dec["comparateurs_sabotes_rB"]["correlation_logit_entre_comparateurs"] == 0.17
                    ok = ok and "correlation_v_entre_comparateurs" in next(iter(s["cellules"].values()))["moments_tires"]
                else:
                    ok = ok and not any("corrB" in x for x in noms)
                if controle == "effet_comparateurs_coupe":
                    ok = ok and len(nom_coupe) == 1 and len(nom_effet) == 1
                detail = noms
            elif controle == "borne_nulles":
                c = next(iter(s["cellules"].values()))
                ok = (abs(c["ebh_A"]["borne_fdr_alpha_c_m0_sur_m"] - 0.05 * 2 / 4) < 1e-15 and c["ebh_A"]["alpha_c"] == 0.05
                      and abs(c["ebh_B"]["borne_fdr_alpha_c_m0_sur_m"] - 0.05 * 2 / (2 * 3 + 2)) < 1e-15
                      and "alpha_de_reference_des_fiches_nulles" in s["lecture_ebh"])
                detail = {"A": c["ebh_A"]["borne_fdr_alpha_c_m0_sur_m"], "B": c["ebh_B"]["borne_fdr_alpha_c_m0_sur_m"]}
            elif controle == "beta_sain":
                noms = list(s["lois"])
                dec = s["lois"][noms[0]]["decomposition_effet_unite"]["biais=0.0"]
                ok = (noms == ["binomiale_Kh3_Ks3_taux0.01_effetB1.0_beta"] and dec["comparateurs_honnetes_fB"]["echelle"] == "beta"
                      and dec["comparateurs_honnetes_fB"]["kappa_concentration"] == dec["comparateurs_sabotes_rB"]["kappa_concentration"]
                      and abs(dec["comparateurs_sabotes_rB"]["ecart_type_ajoute_sur_p"] - dec["comparateurs_sabotes_rB"]["ecart_type_logit_v6_au_meme_sigma"]) < 1e-12
                      and dec["comparateurs_honnetes_fB"]["ecart_type_ajoute_sur_p"] > dec["comparateurs_honnetes_fB"]["ecart_type_logit_v6_au_meme_sigma"]
                      and s["reglages"]["echelle_dispersion"] == "beta" and s["reglages"]["paires_K_h_K_s"] == [[3, 3]]
                      and "ecart_type_pB_honnetes" in next(iter(s["cellules"].values()))["moments_tires"])
                detail = {"lois": noms, "kappa": dec["comparateurs_sabotes_rB"]["kappa_concentration"]}
            elif controle == "logit_explicite":
                noms = list(s["lois"])
                ok = noms == ["binomiale_Kh3_Ks3_taux0.01_effetB1.0"] and s["reglages"]["echelle_dispersion"] == "logit"
                detail = noms
            elif controle == "beta_A_coupe":
                noms = list(s["lois"])
                ok = noms == ["binomiale_Kh3_Ks3_taux0.01_effetA1.0_effetB1.0_beta", "binomiale_Kh3_Ks3_taux0.01_effetA1.0_effetB1.0_beta_lien_coupe"]
                detail = noms
            elif controle == "beta_nulles":
                c = next(iter(s["cellules"].values()))
                ok = "ebh_A" in c and "ebh_B" in c and c["ebh_A"]["fiches_nulles"] == 1 and list(s["lois"])[0].endswith("_beta")
                ok = ok and s["lois"][list(s["lois"])[0]]["fiches_nulles"]["A"].startswith("binomiale_Kh3_Ks3_taux0.01_effetB0.5_beta")
                detail = s["lois"][list(s["lois"])[0]].get("fiches_nulles")
            elif controle == "K_s_cartesien":
                noms = list(s["lois"])
                ok = noms == ["binomiale_Kh3_Ks5_taux0.01", "binomiale_Kh3_Ks3_taux0.01"] and s["reglages"]["paires_K_h_K_s"] == [[3, 5], [3, 3]]
                detail = noms
            elif controle == "K_s_six":
                noms = list(s["lois"])
                ok = noms == [f"binomiale_Kh{K}_Ks{Ks}_taux0.01" for K in (10, 5) for Ks in (10, 5, 3)] and len(s["cellules"]) == 6
                detail = noms
            elif controle == "K_sabotes":
                noms = list(s["lois"])
                ok = noms == ["binomiale_Kh3_Ks5_taux0.01"] and s["reglages"]["paires_K_h_K_s"] == [[3, 5]]
                detail = noms
            elif controle == "secours_K_s":
                c = s["lois"]["reelle_recentree"].get("contraste", "")
                ok = "K_h = 3, K_s = 5" in c
                detail = c
            elif controle == "ebh_reel":
                c = next(iter(s["cellules"].values()))
                ok = "ebh_A" in c and "ebh_B" in c
            elif controle == "commit_stdout":
                ok = s["commit"] == "essai 0123abcd" and s["etat_du_script"].startswith("non lu") and s["reglages"]["commit_declare"] == "essai 0123abcd"
                detail = {"commit": s["commit"], "etat_du_script": s["etat_du_script"]}
            elif controle == "commit_nul":
                ok = s["commit"] is None and s["etat_du_script"].startswith("non lu") and s["reglages"]["commit_declare"] is None
                detail = {"commit": s["commit"], "etat_du_script": s["etat_du_script"]}
            elif controle == "rho_direct":
                noms = list(s["lois"])
                dec = s["lois"][noms[0]]["decomposition_effet_unite"]["biais=0.0"]
                ok = (noms == ["binomiale_Kh3_Ks3_taux0.01_rhoB0.1_beta"] and dec["comparateurs_honnetes_fB"]["kappa_concentration"] == 9.0
                      and dec["comparateurs_sabotes_rB"]["kappa_concentration"] == 9.0 and dec["comparateurs_sabotes_rB"]["correlation_intra_unite"] == 0.1
                      and "sigma_logit_de_reference" not in dec["comparateurs_sabotes_rB"] and s["reglages"]["rho_comparateurs"] == 0.1
                      and s["reglages"]["echelle_dispersion"] == "beta")
                detail = {"lois": noms, "kappa": dec["comparateurs_sabotes_rB"]["kappa_concentration"]}
            elif controle in ("combine_sigma", "combine_rho"):
                noms = list(s["lois"])
                dec = s["lois"][noms[0]]["decomposition_effet_unite"]["biais=0.0"]
                m = next(iter(s["cellules"].values()))["moments_tires"]
                attendu_nom = ("binomiale_Kh3_Ks3_taux0.01_betaA_rho0.1_effetB1.0_beta_lien_coupe" if controle == "combine_sigma"
                               else "binomiale_Kh3_Ks3_taux0.01_betaA_rho0.17_rhoB0.085_beta_lien_coupe")
                ok = (noms == [attendu_nom] and "honnetes_fA" in dec and "sabotes_rA" in dec and "comparateurs_honnetes_fB" in dec
                      and "ecart_type_pA_honnetes" in m and "ecart_type_pB_honnetes" in m
                      and s["reglages"]["combiner_dispersion_a_et_comparateurs"] is True)
                detail = noms
            elif controle == "A_beta_seul":
                noms = list(s["lois"])
                ok = noms == ["binomiale_Kh3_Ks3_taux0.01_betaA_rho0.1_lien_coupe"] and s["reglages"]["combiner_dispersion_a_et_comparateurs"] is False
                detail = noms
            elif controle == "n80_fiche":
                l = next(iter(s["lois"].values()))["n_pour_puissance_0_8_fiche"]
                v = next(iter(l.values()))
                ok = (sorted(v["n80"]) == ["atteinte_160", "atteinte_40", "retenue_ebh"] and len(v["points_evalues"]) >= 3
                      and all(sorted(p) == ["atteinte_160", "atteinte_40", "retenue_ebh"] for p in v["points_evalues"].values()))
                detail = {"n80": v["n80"], "points": len(v["points_evalues"])}
            elif controle in ("copule", "copule_nulle"):
                noms = list(s["lois"])
                m = next(iter(s["cellules"].values()))["moments_tires"]
                if controle == "copule":
                    ok = (len(noms) == 1 and noms[0].endswith("_copuleAB0.5_lien_coupe") and "correlation_pA_pB_honnetes" in m
                          and "difficulte_partagee_copule" in s["lois"][noms[0]]["decomposition_effet_unite"]["biais=0.0"])
                else:
                    ok = len(noms) == 1 and "copule" not in noms[0] and "correlation_pA_pB_honnetes" not in m
                detail = noms
            elif controle in ("strates", "strates_iid"):
                noms = list(s["lois"])
                m = next(iter(s["cellules"].values()))["moments_tires"]
                dec = s["lois"][noms[0]]["decomposition_effet_unite"]["biais=0.0"]
                attendu_nom = ("strates3g0.4sujet_calibre_bloc" if controle == "strates" else "strates2g0.3commune_brut_iid")
                ok = (len(noms) == 1 and attendu_nom in noms[0] and "strates" in dec and "part_variance_ecart_prevue_par_strates_contraste" in m
                      and len(dec["strates"]["esperances_de_strate_A_sabotes"]) == (3 if controle == "strates" else 2))
                detail = noms
            elif controle == "cibles":
                v = next(iter(next(iter(s["lois"].values()))["n_pour_puissance_0_8_fiche"].values()))
                ok = sorted(k for k in v if k.startswith("n") and k[1:].isdigit()) == ["n80", "n90"] and v["cibles"] == [0.8, 0.9]
                ok = ok and all(v["n90"][m]["n_approx"] >= v["n80"][m]["n_approx"] for m in v["n80"])
                detail = {"n80": {m: x["n_approx"] for m, x in v["n80"].items()}, "n90": {m: x["n_approx"] for m, x in v["n90"].items()}}
            elif controle in ("neuvieme", "neuvieme_deux_k", "neuvieme_egal"):
                noms = list(s["lois"])
                cel = s["cellules"]
                if controle == "neuvieme":
                    m = next(iter(cel.values()))["moments_tires"]
                    ok = (len(noms) == 1 and "_neuf0.05" in noms[0] and abs(m["E_rB_neuvieme"] - 0.45) < 0.03 and abs(m["E_rB_huit_premiers"] - 0.40) < 0.03
                          and s["reglages"]["ecart_contraste_neuvieme"] == 0.05)
                    detail = {"loi": noms, "E_rB_neuvieme": m["E_rB_neuvieme"], "E_rB_huit_premiers": m["E_rB_huit_premiers"]}
                elif controle == "neuvieme_deux_k":
                    k8 = [c for e, c in cel.items() if e.endswith("|k=8")]
                    k9 = [c for e, c in cel.items() if e.endswith("|k=9")]
                    ok = (len(k8) == 1 and len(k9) == 1 and "E_rB_neuvieme" not in k8[0]["moments_tires"] and "E_rB_neuvieme" in k9[0]["moments_tires"])
                    detail = list(cel)
                else:
                    ok = len(noms) == 1 and "_neuf" not in noms[0] and s["reglages"]["ecart_contraste_neuvieme"] is None
                    detail = noms
            elif controle == "ks20":
                noms = list(s["lois"])
                ok = len(noms) == 1 and "Kh5_Ks20_" in noms[0] and s["reglages"]["paires_K_h_K_s"] == [[5, 20]]
                detail = noms
    resultats.append({"essai": nom, "constat": constat, "arguments": args, "attendu": attendu, "obtenu": obtenu,
                      "code": r.returncode, "message": message[:300], "detail": detail, "conforme": ok})

bilan = {"script": SCRIPT, "script_sha256": hashlib.sha256(open(SCRIPT, "rb").read()).hexdigest(),
         "essais": len(resultats), "conformes": sum(x["conforme"] for x in resultats),
         "non_conformes": [x["essai"] for x in resultats if not x["conforme"]],
         "refus_nommes": sum(x["obtenu"] == "refus" for x in resultats),
         "erreurs_brutes": sum(x["obtenu"] == "erreur brute" for x in resultats), "resultats": resultats}
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(bilan, f, indent=1, ensure_ascii=False)
    f.write("\n")
print(f"{bilan['conformes']}/{bilan['essais']} conformes ; erreurs brutes : {bilan['erreurs_brutes']} ; non conformes : {bilan['non_conformes']}")
