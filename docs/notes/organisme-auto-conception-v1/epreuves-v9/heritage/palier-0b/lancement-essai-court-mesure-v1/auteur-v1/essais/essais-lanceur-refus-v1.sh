#!/bin/bash
# Essais des refus de départ du VRAI lanceur, en mode --verifier-seulement (la commande n'y est jamais exécutée),
# sur une racine factice, une tête et une empreinte factices passées en paramètre.
# Usage : essais-lanceur-refus-v1.sh DOSSIER_DES_ESSAIS LANCEUR TETE_FACTICE EMPREINTE_FACTICE
set -u
E=$1
L=$2
T=$3
H=$4
R="$E/racine-factice"
P="$R/prog/programme-factice-v1.py"
S_NEUF="$E/sorties-jamais-creees"
S_EXIST="$E/sorties-deja-la"
B="$E/refus"
if [ -e "$B" ]; then echo "refus : $B existe" >&2; exit 1; fi
mkdir -p "$B" "$S_EXIST"
ECHECS=0

essai() {  # nom code_attendu [arguments après le dossier de tenue...]
  local nom=$1 attendu=$2
  shift 2
  mkdir "$B/$nom"
  bash "$L" "$B/$nom" "$@" 2> "$B/$nom/erreur.txt"
  local obtenu=$?
  local ecrit="(absent)"
  if [ -f "$B/$nom/code-de-sortie.txt" ]; then ecrit=$(cat "$B/$nom/code-de-sortie.txt"); fi
  local verdict=TENU
  if [ "$obtenu" != "$attendu" ]; then verdict=CASSÉ; ECHECS=$((ECHECS + 1)); fi
  echo "$nom : attendu $attendu ; obtenu $obtenu ; code-de-sortie.txt $ecrit ; $verdict ; message : $(tail -n 1 "$B/$nom/erreur.txt")"
}

essai v0-cas-sain 0 --verifier-seulement "$R" "$T" "$H" "$P" "$S_NEUF"
essai v1-sorties-existantes 10 --verifier-seulement "$R" "$T" "$H" "$P" "$S_EXIST"
essai v2-tete-fausse 11 --verifier-seulement "$R" 0000000000000000000000000000000000000000 "$H" "$P" "$S_NEUF"
essai v4-empreinte-fausse 13 --verifier-seulement "$R" "$T" 0000000000000000000000000000000000000000000000000000000000000000 "$P" "$S_NEUF"
essai v4b-programme-absent 13 --verifier-seulement "$R" "$T" "$H" "$R/prog/absent.py" "$S_NEUF"
essai v2b-racine-sans-depot 11 --verifier-seulement "$E/sorties-deja-la" "$T" "$H" "$P" "$S_NEUF"
essai v5-usage 2 --verifier-seulement "$R"
echo "modification d'un fichier suivi de la racine factice" >> "$R/suivi.txt"
essai v3-fichier-suivi-modifie 12 --verifier-seulement "$R" "$T" "$H" "$P" "$S_NEUF"
git -C "$R" checkout -q -- suivi.txt
echo "un fichier non suivi" > "$R/non-suivi.txt"
essai v3b-fichier-non-suivi-seulement 0 --verifier-seulement "$R" "$T" "$H" "$P" "$S_NEUF"
# code-de-sortie.txt déjà présent : rien n'est écrasé
mkdir "$B/v6-code-deja-present"
echo "ancien" > "$B/v6-code-deja-present/code-de-sortie.txt"
bash "$L" "$B/v6-code-deja-present" --verifier-seulement "$R" "$T" "$H" "$P" "$S_NEUF" 2> "$B/v6-code-deja-present/erreur.txt"
O=$?
C=$(cat "$B/v6-code-deja-present/code-de-sortie.txt")
if [ "$O" = 4 ] && [ "$C" = ancien ]; then V=TENU; else V=CASSÉ; ECHECS=$((ECHECS + 1)); fi
echo "v6-code-deja-present : attendu 4 et « ancien » ; obtenu $O et « $C » ; $V"
bash "$L" "$B/absent" 2> "$B/v7-erreur.txt"
O=$?
if [ "$O" = 3 ]; then V=TENU; else V=CASSÉ; ECHECS=$((ECHECS + 1)); fi
echo "v7-tenue-absente : attendu 3 ; obtenu $O ; $V"
if [ -e "$S_NEUF" ]; then echo "CASSÉ : $S_NEUF a été créé"; ECHECS=$((ECHECS + 1)); else echo "$S_NEUF jamais créé : TENU"; fi
echo "échecs : $ECHECS"
