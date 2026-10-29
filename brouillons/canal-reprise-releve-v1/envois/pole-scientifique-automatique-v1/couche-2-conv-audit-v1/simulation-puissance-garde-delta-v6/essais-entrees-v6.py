"""Essais d'entrées du script de puissance de la garde δ v6 : GD4-03 (souligné), GD4-04 et GD5-04 (doublons, aussi après
normalisation), GD4-05 (git simulé, manifeste), GD4-06 (replis, refus nommés), GD5-01 (options de dispersion des
comparateurs), GD5-02 (α de référence des fiches nulles). Chaque essai lance le script dans un sous-processus et lit le code
de retour, le message et, s'il est accepté, la sortie.

Usage : python3 -I -B essais-entrees-v6.py SCRIPT_V6 DOSSIER_DE_TRAVAIL_NEUF SORTIE.json
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

# git simulé (GD4-05) : un faux « git » en tête du PATH, conduit par la variable SCENARIO
FAUX = os.path.join(TRAVAIL, "faux-git")
os.makedirs(FAUX)
with open(os.path.join(FAUX, "git"), "w") as f:
    f.write("""#!/bin/sh
C=0123456789abcdef0123456789abcdef01234567
case "$SCENARIO" in
 hors) echo "fatal: not a git repository (or any of the parent directories): .git" >&2; exit 128;;
 douteux) echo "fatal: detected dubious ownership in repository at '/x'" >&2; exit 128;;
esac
case "$1" in
 rev-parse)
  if [ "$2" = "--show-toplevel" ]; then echo /x; exit 0; fi
  if [ "$SCENARIO" = "sans_commit" ]; then echo "fatal: Needed a single revision" >&2; exit 128; fi
  if [ "$SCENARIO" = "commit_illisible" ]; then echo "HEAD"; exit 0; fi
  echo $C; exit 0;;
 ls-files)
  if [ "$SCENARIO" = "lsfiles_echec" ]; then echo "fatal: index file corrupt" >&2; exit 128; fi
  if [ "$SCENARIO" = "ignore" ]; then exit 1; fi
  exit 0;;
 status)
  if [ "$SCENARIO" = "status_echec" ]; then echo "fatal: index file corrupt" >&2; exit 128; fi
  if [ "$SCENARIO" = "modifie" ]; then echo " M script.py"; fi
  exit 0;;
esac
exit 2
""")
os.chmod(os.path.join(FAUX, "git"), 0o755)
VIDE = os.path.join(TRAVAIL, "chemin-sans-git")
os.makedirs(VIDE)

E = ["--effectif-attendu", "6"]
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
    ("--sortie non .json", "GD4-05", ["--sortie", "x.txt"], "refus", ".json"),
    ("--sortie (sain) : journal et manifeste", "GD4-05 sain", ["--sortie", "passage.json"], "accepte", "manifeste"),
    ("--sortie existante", "GD4-05 / R12", ["--sortie", "passage.json"], "refus", "R12"),
    ("git : hors dépôt", "GD4-05", [], "accepte", ("git", "hors", "hors dépôt git")),
    ("git : propriétaire douteux", "GD4-05", [], "accepte", ("git", "douteux", "inconnu")),
    ("git : dépôt sans commit", "GD4-05", [], "accepte", ("git", "sans_commit", "inconnu")),
    ("git : commit illisible", "GD4-05", [], "accepte", ("git", "commit_illisible", "inconnu")),
    ("git : ls-files en échec", "GD4-05", [], "accepte", ("git", "lsfiles_echec", "inconnu")),
    ("git : status en échec", "GD4-05", [], "accepte", ("git", "status_echec", "inconnu")),
    ("git : ignoré", "GD4-05", [], "accepte", ("git", "ignore", "non suivi")),
    ("git : modifié", "GD4-05", [], "accepte", ("git", "modifie", "M script.py")),
    ("git : propre (sain)", "GD4-05 sain", [], "accepte", ("git", "propre", "commité, non modifié")),
    ("git : absent du PATH", "GD4-05", [], "accepte", ("git", "absent", "inconnu")),
]

resultats = []
for nom, constat, args, attendu, controle in ESSAIS:
    env = dict(os.environ)
    if isinstance(controle, tuple):
        scenario = controle[1]
        if scenario == "absent":
            env["PATH"] = VIDE
        else:
            env["PATH"] = FAUX + os.pathsep + env.get("PATH", "")
            env["SCENARIO"] = scenario
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
                  and m["graines"]["graine_maitresse"] == 20261029 and "etat_du_script" in m["script"])
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
            elif controle == "ebh_reel":
                c = next(iter(s["cellules"].values()))
                ok = "ebh_A" in c and "ebh_B" in c
            elif isinstance(controle, tuple):
                ok = controle[2] in s["etat_du_script"] and (controle[2] != "inconnu" or "commité, non modifié" not in s["etat_du_script"])
                detail = {"commit": s["commit"], "etat_du_script": s["etat_du_script"]}
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
