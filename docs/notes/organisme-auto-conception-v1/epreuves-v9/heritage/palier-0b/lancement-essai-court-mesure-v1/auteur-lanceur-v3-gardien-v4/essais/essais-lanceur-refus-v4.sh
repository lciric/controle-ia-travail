#!/bin/bash
# Refus de départ du VRAI lanceur v3, en mode --verifier-seulement (la commande n'y est JAMAIS exécutée).
#  - racine AVEC .git (dépôt factice jetable) : tête et empreinte factices passées en paramètre (refus de la v2 rejoués) ;
#  - racine SANS .git (copie factice) : valeurs d'emploi du lanceur (tête d7f949ac…, empreinte 1f04cb46…), sans paramètre
#    de remplacement : la copie porte le vrai programme, copié à l'octet ;
#  - nouveautés : fichier du commit absent, faux, sur deux lignes, sans fin de ligne ; liste d'empreintes absente, fichier
#    modifié, manquant, ajouté ; interpréteur absent, non exécutable ; chemins non absolus.
# Usage : essais-lanceur-refus-v4.sh DOSSIER_NEUF LANCEUR PROGRAMME_REEL PROGRAMME_FACTICE INTERPRETE_REEL
set -u
E=$(cd "$(dirname "$0")" && pwd)
B=$1
L=$2
PREEL=$3
PFACT=$4
PY=$5
if [ -e "$B" ]; then echo "refus : $B existe" >&2; exit 1; fi
mkdir -p "$B/t"
H=docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b
TETE_EMPLOI=d7f949acd9ac92e998e57663d2cc741de93f18c3
S_NEUF="$B/sorties-jamais-creees"
S_EXIST="$B/sorties-deja-la"
mkdir -p "$S_EXIST"
ECHECS=0
N=0

essai() {  # nom code_attendu [arguments après le dossier de tenue...]
  local nom=$1 attendu=$2
  shift 2
  mkdir "$B/t/$nom"
  bash "$L" "$B/t/$nom" "$@" 2> "$B/t/$nom/erreur.txt"
  local obtenu=$?
  local ecrit="(absent)"
  if [ -f "$B/t/$nom/code-de-sortie.txt" ]; then ecrit=$(cat "$B/t/$nom/code-de-sortie.txt"); fi
  local verdict=TENU
  N=$((N + 1))
  if [ "$obtenu" != "$attendu" ]; then verdict=CASSÉ; ECHECS=$((ECHECS + 1)); fi
  echo "$nom : attendu $attendu ; obtenu $obtenu ; code-de-sortie.txt $ecrit ; $verdict ; message : $(tail -n 1 "$B/t/$nom/erreur.txt" | cut -c1-300)"
}

# --- racine avec .git (factice), tête et empreinte factices en paramètre
bash "$E/preparer-racine-git-v4.sh" "$B/racine-git" "$PFACT" > "$B/racine-git.txt"
RG="$B/racine-git"
TG=$(git -C "$RG" rev-parse HEAD)
EG=$(sha256sum "$RG/$H/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py" | cut -d' ' -f1)
echo "racine git factice : tête $TG ; empreinte du programme factice $EG"
essai g0-git-sain 0 "$RG" "$PY" "$S_NEUF" --verifier-seulement "$TG" "$EG"
essai g1-git-sorties-existantes 10 "$RG" "$PY" "$S_EXIST" --verifier-seulement "$TG" "$EG"
essai g2-git-tete-fausse 11 "$RG" "$PY" "$S_NEUF" --verifier-seulement 0000000000000000000000000000000000000000 "$EG"
essai g2b-git-tete-d-emploi 11 "$RG" "$PY" "$S_NEUF" --verifier-seulement
essai g4-git-empreinte-fausse 13 "$RG" "$PY" "$S_NEUF" --verifier-seulement "$TG" 0000000000000000000000000000000000000000000000000000000000000000
essai g5-git-interprete-absent 14 "$RG" "$B/absent/python" "$S_NEUF" --verifier-seulement "$TG" "$EG"
echo "pas un exécutable" > "$B/interprete-non-executable"
essai g6-git-interprete-non-executable 14 "$RG" "$B/interprete-non-executable" "$S_NEUF" --verifier-seulement "$TG" "$EG"
essai g6b-git-interprete-dossier 14 "$RG" "$B" "$S_NEUF" --verifier-seulement "$TG" "$EG"
essai g7-racine-absente 11 "$B/racine-absente" "$PY" "$S_NEUF" --verifier-seulement "$TG" "$EG"
echo "modification d'un fichier suivi" >> "$RG/suivi.txt"
essai g3-git-fichier-suivi-modifie 12 "$RG" "$PY" "$S_NEUF" --verifier-seulement "$TG" "$EG"
git -C "$RG" checkout -q -- suivi.txt
echo "un fichier non suivi" > "$RG/non-suivi.txt"
essai g3b-git-fichier-non-suivi-seulement 0 "$RG" "$PY" "$S_NEUF" --verifier-seulement "$TG" "$EG"

# --- racine sans .git (copie factice), valeurs d'emploi du lanceur
copie() {  # nom [commit]
  bash "$E/preparer-copie-factice-v4.sh" "$B/$1" "$PREEL" "${2:-$TETE_EMPLOI}" > "$B/$1.txt"
  echo "$B/$1"
}
RC=$(copie copie-saine)
essai c0-copie-saine 0 "$RC" "$PY" "$S_NEUF" --verifier-seulement
essai c0b-copie-saine-sorties-existantes 10 "$RC" "$PY" "$S_EXIST" --verifier-seulement
essai c9-copie-interprete-absent 14 "$RC" "$B/absent/python" "$S_NEUF" --verifier-seulement
R=$(copie copie-sans-commit); rm "$R/COMMIT-DE-LA-COPIE.txt"
essai c1-copie-sans-fichier-de-commit 11 "$R" "$PY" "$S_NEUF" --verifier-seulement
R=$(copie copie-commit-faux 0123456789abcdef0123456789abcdef01234567)
essai c2-copie-commit-faux 11 "$R" "$PY" "$S_NEUF" --verifier-seulement
R=$(copie copie-commit-court d7f949ac)
essai c2b-copie-commit-abrege 11 "$R" "$PY" "$S_NEUF" --verifier-seulement
R=$(copie copie-commit-deux-lignes); echo "$TETE_EMPLOI" >> "$R/COMMIT-DE-LA-COPIE.txt"
essai c3-copie-commit-sur-deux-lignes 11 "$R" "$PY" "$S_NEUF" --verifier-seulement
R=$(copie copie-commit-sans-fin-de-ligne); printf '%s' "$TETE_EMPLOI" > "$R/COMMIT-DE-LA-COPIE.txt"
essai c3b-copie-commit-sans-fin-de-ligne 11 "$R" "$PY" "$S_NEUF" --verifier-seulement
R=$(copie copie-commit-lien); mv "$R/COMMIT-DE-LA-COPIE.txt" "$R/commit-vrai.txt"; ln -s commit-vrai.txt "$R/COMMIT-DE-LA-COPIE.txt"
essai c3c-copie-commit-lien 11 "$R" "$PY" "$S_NEUF" --verifier-seulement
R=$(copie copie-sans-empreintes); rm "$R/EMPREINTES-DE-LA-COPIE.txt"
essai c4-copie-sans-liste-d-empreintes 12 "$R" "$PY" "$S_NEUF" --verifier-seulement
R=$(copie copie-fichier-modifie); echo "un octet de plus" >> "$R/suivi.txt"
essai c5-copie-fichier-modifie 12 "$R" "$PY" "$S_NEUF" --verifier-seulement
R=$(copie copie-fichier-manquant); rm "$R/$H/code-v6/src/factice.txt"
essai c6-copie-fichier-manquant 12 "$R" "$PY" "$S_NEUF" --verifier-seulement
R=$(copie copie-fichier-ajoute); echo "fichier ajouté" > "$R/$H/ajoute.txt"
essai c7-copie-fichier-ajoute 12 "$R" "$PY" "$S_NEUF" --verifier-seulement
R=$(copie copie-liste-vide); : > "$R/EMPREINTES-DE-LA-COPIE.txt"
essai c7b-copie-liste-vide 12 "$R" "$PY" "$S_NEUF" --verifier-seulement
R=$(copie copie-programme-altere); echo "# octet ajouté" >> "$R/$H/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py"
(cd "$R" && find . -type f ! -path ./COMMIT-DE-LA-COPIE.txt ! -path ./EMPREINTES-DE-LA-COPIE.txt -print0 | sort -z | xargs -0 sha256sum > EMPREINTES-DE-LA-COPIE.txt)
essai c8-copie-programme-altere-liste-refaite 13 "$R" "$PY" "$S_NEUF" --verifier-seulement
R=$(copie copie-git-parasite); echo "gitdir: /nulle/part" > "$R/.git"
essai c11-copie-avec-.git-parasite 11 "$R" "$PY" "$S_NEUF" --verifier-seulement

# --- usage
essai u1-trois-arguments 2 "$RC" "$PY"
essai u2-racine-relative 2 racine-relative "$PY" "$S_NEUF" --verifier-seulement
essai u2b-interprete-relatif 2 "$RC" python "$S_NEUF" --verifier-seulement
essai u2c-sorties-relatives 2 "$RC" "$PY" sorties-relatives --verifier-seulement
essai u3-cinquieme-argument-inconnu 2 "$RC" "$PY" "$S_NEUF" --autre
essai u4-six-arguments 2 "$RC" "$PY" "$S_NEUF" --verifier-seulement "$TG"
# code-de-sortie.txt déjà présent : rien n'est écrasé
mkdir "$B/t/v6-code-deja-present"
echo "ancien" > "$B/t/v6-code-deja-present/code-de-sortie.txt"
bash "$L" "$B/t/v6-code-deja-present" "$RC" "$PY" "$S_NEUF" --verifier-seulement 2> "$B/t/v6-code-deja-present/erreur.txt"
O=$?
C=$(cat "$B/t/v6-code-deja-present/code-de-sortie.txt")
N=$((N + 1))
if [ "$O" = 4 ] && [ "$C" = ancien ]; then V=TENU; else V=CASSÉ; ECHECS=$((ECHECS + 1)); fi
echo "v6-code-deja-present : attendu 4 et « ancien » ; obtenu $O et « $C » ; $V"
bash "$L" "$B/t/absent" "$RC" "$PY" "$S_NEUF" --verifier-seulement 2> "$B/v7-erreur.txt"
O=$?
N=$((N + 1))
if [ "$O" = 3 ]; then V=TENU; else V=CASSÉ; ECHECS=$((ECHECS + 1)); fi
echo "v7-tenue-absente : attendu 3 ; obtenu $O ; $V"
N=$((N + 1))
if [ -e "$S_NEUF" ]; then echo "CASSÉ : $S_NEUF a été créé"; ECHECS=$((ECHECS + 1)); else echo "$S_NEUF jamais créé : TENU"; fi
echo "essais : $N ; échecs : $ECHECS"
