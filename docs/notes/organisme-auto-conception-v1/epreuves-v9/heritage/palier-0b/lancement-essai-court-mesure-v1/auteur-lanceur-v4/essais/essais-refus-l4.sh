#!/bin/bash
# Refus de départ du VRAI lanceur v4, en mode --verifier-seulement (la commande n'y est JAMAIS exécutée).
#  A. racine AVEC .git (dépôt factice jetable), tête et empreinte factices (refus de la v2 et de la v3 rejoués) ;
#  B. copies factices SANS .git, avec tête d'emploi et empreinte d'emploi, et la « référence » propre à chaque copie factice
#     (8e argument) : refus de la v3 rejoués, et nouveautés v4 (liens, fichiers spéciaux, listes refaites, liste et référence
#     altérées d'un octet) ;
#  C. la VRAIE copie (arbre du commit extrait par git archive, plus les deux fichiers), valeurs d'emploi seules, aucun
#     remplacement : cas sain, puis artefacts appliqués un à un et défaits, puis cas sain de nouveau ;
#  D. usages.
# Usage : essais-refus-l4.sh DOSSIER_NEUF LANCEUR PROGRAMME_REEL PROGRAMME_FACTICE INTERPRETE COPIE_REELLE
set -u
E=$(cd "$(dirname "$0")" && pwd)
B=$1; L=$2; PREEL=$3; PFACT=$4; PY=$5; RR=$6
if [ -e "$B" ]; then echo "refus : $B existe" >&2; exit 1; fi
mkdir -p "$B/t"
H=docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b
TE=d7f949acd9ac92e998e57663d2cc741de93f18c3
EE=1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14
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
  echo "$nom : attendu $attendu ; obtenu $obtenu ; code-de-sortie.txt $ecrit ; $verdict ; message : $(grep -E 'refus|départ permis|usage' "$B/t/$nom/erreur.txt" | tail -n 1 | cut -c1-330)"
}

# --- A. racine avec .git
bash "$E/../../essais/preparer-racine-git-v4.sh" "$B/racine-git" "$PFACT" > "$B/racine-git.txt"
RG="$B/racine-git"
TG=$(git -C "$RG" rev-parse HEAD)
EG=$(sha256sum "$RG/$H/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py" | cut -d' ' -f1)
essai a0-git-sain 0 "$RG" "$PY" "$S_NEUF" --verifier-seulement "$TG" "$EG"
essai a1-git-sorties-existantes 10 "$RG" "$PY" "$S_EXIST" --verifier-seulement "$TG" "$EG"
essai a2-git-tete-fausse 11 "$RG" "$PY" "$S_NEUF" --verifier-seulement 0000000000000000000000000000000000000000 "$EG"
essai a2b-git-tete-d-emploi 11 "$RG" "$PY" "$S_NEUF" --verifier-seulement
essai a4-git-empreinte-fausse 13 "$RG" "$PY" "$S_NEUF" --verifier-seulement "$TG" 0000000000000000000000000000000000000000000000000000000000000000
essai a5-git-interprete-absent 14 "$RG" "$B/absent/python" "$S_NEUF" --verifier-seulement "$TG" "$EG"
echo "pas un exécutable" > "$B/interprete-non-executable"
essai a6-git-interprete-non-executable 14 "$RG" "$B/interprete-non-executable" "$S_NEUF" --verifier-seulement "$TG" "$EG"
essai a6b-git-interprete-dossier 14 "$RG" "$B" "$S_NEUF" --verifier-seulement "$TG" "$EG"
essai a7-racine-absente 11 "$B/racine-absente" "$PY" "$S_NEUF" --verifier-seulement "$TG" "$EG"
echo "modification d'un fichier suivi" >> "$RG/suivi.txt"
essai a3-git-fichier-suivi-modifie 12 "$RG" "$PY" "$S_NEUF" --verifier-seulement "$TG" "$EG"
git -C "$RG" checkout -q -- suivi.txt
echo "un fichier non suivi" > "$RG/non-suivi.txt"
essai a3b-git-fichier-non-suivi-seulement 0 "$RG" "$PY" "$S_NEUF" --verifier-seulement "$TG" "$EG"

# --- B. copies factices sans .git (référence propre à chacune)
REF=""
copie() {  # nom [commit [alterer]] ; pose R et REF
  R="$B/$1"
  REF=$(bash "$E/preparer-copie-factice-l4.sh" "$R" "$PREEL" "${2:-$TE}" "${3:-0}")
}
v() { essai "$1" "$2" "$R" "$PY" "${3:-$S_NEUF}" --verifier-seulement "$TE" "$EE" "$REF"; }
copie copie-saine; RS=$R; REFS=$REF
v b0-copie-saine 0
v b0b-copie-saine-sorties-existantes 10 "$S_EXIST"
essai b9-copie-interprete-absent 14 "$RS" "$B/absent/python" "$S_NEUF" --verifier-seulement "$TE" "$EE" "$REFS"
essai b0c-reference-d-emploi-sur-copie-factice 12 "$RS" "$PY" "$S_NEUF" --verifier-seulement
REF_ALT=$(printf '%s' "$REFS" | sed 's/^./0/'); [ "$REF_ALT" = "$REFS" ] && REF_ALT=$(printf '%s' "$REFS" | sed 's/^./1/')
essai b13-reference-alteree-d-un-octet 12 "$RS" "$PY" "$S_NEUF" --verifier-seulement "$TE" "$EE" "$REF_ALT"
copie copie-sans-commit; rm "$R/COMMIT-DE-LA-COPIE.txt"; v b1-copie-sans-fichier-de-commit 11
copie copie-commit-faux 0123456789abcdef0123456789abcdef01234567; v b2-copie-commit-faux 11
copie copie-commit-court d7f949ac; v b2b-copie-commit-abrege 11
copie copie-commit-deux-lignes; echo "$TE" >> "$R/COMMIT-DE-LA-COPIE.txt"; v b3-copie-commit-sur-deux-lignes 11
copie copie-commit-sans-fin; printf '%s' "$TE" > "$R/COMMIT-DE-LA-COPIE.txt"; v b3b-copie-commit-sans-fin-de-ligne 11
copie copie-commit-lien; mv "$R/COMMIT-DE-LA-COPIE.txt" "$R/commit-vrai.txt"; ln -s commit-vrai.txt "$R/COMMIT-DE-LA-COPIE.txt"; v b3c-copie-commit-en-lien 11
copie copie-sans-liste; rm "$R/EMPREINTES-DE-LA-COPIE.txt"; v b4-copie-sans-liste 12
copie copie-liste-vide; : > "$R/EMPREINTES-DE-LA-COPIE.txt"; v b4b-copie-liste-vide 12
copie copie-liste-octet; sed -i '1s/^./X/' "$R/EMPREINTES-DE-LA-COPIE.txt"; v b4c-liste-de-la-copie-alteree-d-un-octet 12
copie copie-liste-en-lien; mv "$R/EMPREINTES-DE-LA-COPIE.txt" "$B/liste-hors-copie.txt"; ln -s "$B/liste-hors-copie.txt" "$R/EMPREINTES-DE-LA-COPIE.txt"; v b4d-liste-en-lien 12
refaire() { (cd "$R" && LC_ALL=C find . -type f ! -path ./COMMIT-DE-LA-COPIE.txt ! -path ./EMPREINTES-DE-LA-COPIE.txt -print0 | LC_ALL=C sort -z | xargs -0 sha256sum > EMPREINTES-DE-LA-COPIE.txt); }
copie copie-fichier-modifie; echo "un octet de plus" >> "$R/suivi.txt"; v b5-fichier-modifie 12
copie copie-fichier-modifie-liste-refaite; echo "un octet de plus" >> "$R/suivi.txt"; refaire; v b5b-fichier-modifie-liste-refaite 12
copie copie-fichier-manquant; rm "$R/$H/code-v6/src/factice.txt"; v b6-fichier-manquant 12
copie copie-fichier-manquant-liste-refaite; rm "$R/$H/code-v6/src/factice.txt"; refaire; v b6b-fichier-manquant-liste-refaite 12
copie copie-fichier-ajoute; echo "ajouté" > "$R/$H/ajoute.txt"; v b7-fichier-ajoute 12
copie copie-fichier-ajoute-liste-refaite; echo "ajouté" > "$R/$H/ajoute.txt"; refaire; v b7b-fichier-ajoute-liste-refaite 12
copie copie-fichier-ajoute-cache; echo "ajouté" > "$R/.cache-ajoute"; v b7c-fichier-cache-ajoute 12
copie copie-programme-altere-liste-refaite; echo "# octet" >> "$R/$H/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py"; refaire; v b8-programme-altere-liste-refaite 12
copie copie-programme-altere-dans-sa-reference "$TE" 1; v b8b-programme-altere-reference-assortie 13
copie copie-git-parasite; echo "gitdir: /nulle/part" > "$R/.git"; v b11-git-parasite 11
copie copie-lien-fichier; ln -s suivi.txt "$R/$H/lien-vers-fichier"; v b14-lien-symbolique-vers-fichier 12
copie copie-lien-dossier; ln -s ../../ "$R/$H/lien-vers-dossier"; v b14b-lien-symbolique-vers-dossier 12
copie copie-lien-brise; ln -s /nulle/part "$R/lien-brise"; v b14c-lien-brise 12
copie copie-fichier-remplace-par-lien; cp "$R/suivi.txt" "$B/suivi-hors-copie.txt"; rm "$R/suivi.txt"; ln -s "$B/suivi-hors-copie.txt" "$R/suivi.txt"; v b14d-fichier-remplace-par-un-lien-de-meme-contenu 12
copie copie-tube; mkfifo "$R/$H/tube"; v b14e-tube-nomme 12
copie copie-racine-en-lien; ln -s "$R" "$B/lien-vers-copie"; R="$B/lien-vers-copie"; v b14f-racine-en-lien 12
mkdir "$B/t/b15-fichier-de-recalcul-deja-present"; echo ancien > "$B/t/b15-fichier-de-recalcul-deja-present/empreintes-recalculees-de-la-copie.txt"
bash "$L" "$B/t/b15-fichier-de-recalcul-deja-present" "$RS" "$PY" "$S_NEUF" --verifier-seulement "$TE" "$EE" "$REFS" 2> /dev/null
O=$?; C=$(cat "$B/t/b15-fichier-de-recalcul-deja-present/empreintes-recalculees-de-la-copie.txt"); N=$((N + 1))
if [ "$O" = 4 ] && [ "$C" = ancien ]; then V=TENU; else V=CASSÉ; ECHECS=$((ECHECS + 1)); fi
echo "b15-fichier-de-recalcul-deja-present : attendu 4 et « ancien » ; obtenu $O et « $C » ; $V"

# --- C. vraie copie, valeurs d'emploi
essai c0-vraie-copie-saine 0 "$RR" "$PY" "$S_NEUF" --verifier-seulement
ln -s COMMIT-DE-LA-COPIE.txt "$RR/docs/lien-ajoute"
essai c1-vraie-copie-lien-symbolique-ajoute 12 "$RR" "$PY" "$S_NEUF" --verifier-seulement
rm "$RR/docs/lien-ajoute"
echo "fichier ajouté" > "$RR/docs/fichier-ajoute.txt"
essai c2-vraie-copie-fichier-ajoute 12 "$RR" "$PY" "$S_NEUF" --verifier-seulement
rm "$RR/docs/fichier-ajoute.txt"
CIBLE="$RR/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v19.md"
cp -p "$CIBLE" "$B/sauvegarde-cible"; cp -p "$RR/EMPREINTES-DE-LA-COPIE.txt" "$B/sauvegarde-liste"
echo "ligne ajoutée (artefact)" >> "$CIBLE"
(cd "$RR" && LC_ALL=C find . -type f ! -path ./COMMIT-DE-LA-COPIE.txt ! -path ./EMPREINTES-DE-LA-COPIE.txt -print0 | LC_ALL=C sort -z | xargs -0 sha256sum > EMPREINTES-DE-LA-COPIE.txt)
essai c3-vraie-copie-fichier-modifie-liste-refaite 12 "$RR" "$PY" "$S_NEUF" --verifier-seulement
cp -p "$B/sauvegarde-cible" "$CIBLE"; cp -p "$B/sauvegarde-liste" "$RR/EMPREINTES-DE-LA-COPIE.txt"
sed -i '17305s/^1f04/2f04/' "$RR/EMPREINTES-DE-LA-COPIE.txt"
essai c4-vraie-copie-liste-alteree-d-un-octet 12 "$RR" "$PY" "$S_NEUF" --verifier-seulement
cp -p "$B/sauvegarde-liste" "$RR/EMPREINTES-DE-LA-COPIE.txt"
essai c5-vraie-copie-interprete-absent 14 "$RR" "$B/absent/python" "$S_NEUF" --verifier-seulement
sed 's/^REFERENCE_ATTENDUE=ab90/REFERENCE_ATTENDUE=bb90/' "$L" > "$B/lanceur-reference-alteree.sh"
if cmp -s "$L" "$B/lanceur-reference-alteree.sh"; then echo "c6 : altération nulle : CASSÉ"; ECHECS=$((ECHECS + 1)); fi
L0=$L; L="$B/lanceur-reference-alteree.sh"
essai c6-lanceur-a-reference-alteree-d-un-octet 12 "$RR" "$PY" "$S_NEUF" --verifier-seulement
L=$L0
essai c7-vraie-copie-saine-apres-retour 0 "$RR" "$PY" "$S_NEUF" --verifier-seulement
echo "empreinte de la liste de la vraie copie après les essais : $(sha256sum "$RR/EMPREINTES-DE-LA-COPIE.txt" | cut -d' ' -f1)"

# --- D. usages
essai d1-trois-arguments 2 "$RS" "$PY"
essai d2-racine-relative 2 racine-relative "$PY" "$S_NEUF" --verifier-seulement
essai d2b-interprete-relatif 2 "$RS" python "$S_NEUF" --verifier-seulement
essai d2c-sorties-relatives 2 "$RS" "$PY" sorties-relatives --verifier-seulement
essai d3-cinquieme-argument-inconnu 2 "$RS" "$PY" "$S_NEUF" --autre
essai d4-six-arguments 2 "$RS" "$PY" "$S_NEUF" --verifier-seulement "$TE"
essai d5-neuf-arguments 2 "$RS" "$PY" "$S_NEUF" --verifier-seulement "$TE" "$EE" "$REFS" en-trop
mkdir "$B/t/d6-code-deja-present"; echo ancien > "$B/t/d6-code-deja-present/code-de-sortie.txt"
bash "$L" "$B/t/d6-code-deja-present" "$RS" "$PY" "$S_NEUF" --verifier-seulement "$TE" "$EE" "$REFS" 2> /dev/null
O=$?; C=$(cat "$B/t/d6-code-deja-present/code-de-sortie.txt"); N=$((N + 1))
if [ "$O" = 4 ] && [ "$C" = ancien ]; then V=TENU; else V=CASSÉ; ECHECS=$((ECHECS + 1)); fi
echo "d6-code-deja-present : attendu 4 et « ancien » ; obtenu $O et « $C » ; $V"
bash "$L" "$B/t/absent" "$RS" "$PY" "$S_NEUF" --verifier-seulement 2> /dev/null
O=$?; N=$((N + 1))
if [ "$O" = 3 ]; then V=TENU; else V=CASSÉ; ECHECS=$((ECHECS + 1)); fi
echo "d7-tenue-absente : attendu 3 ; obtenu $O ; $V"
N=$((N + 1))
if [ -e "$S_NEUF" ]; then echo "CASSÉ : $S_NEUF a été créé"; ECHECS=$((ECHECS + 1)); else echo "$S_NEUF jamais créé : TENU"; fi
echo "essais : $N ; échecs : $ECHECS"
