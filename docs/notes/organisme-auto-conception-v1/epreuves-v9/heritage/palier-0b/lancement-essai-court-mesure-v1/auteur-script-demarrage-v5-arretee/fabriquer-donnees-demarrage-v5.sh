#!/bin/bash
# Fabricant des données de démarrage de la machine de l'essai 3 du palier 0b — v5 (= v4, aux noms v5 près : script, amorce,
# nom dans la charge). Joué dans la session juste avant la création de la machine.
#
# Emploi : fabriquer-donnees-demarrage-v5.sh NOM_DE_VARIABLE SORTIE [EMPREINTE_ATTENDUE_DU_SCRIPT]
#   NOM_DE_VARIABLE : NOM d'une variable d'environnement qui porte le jeton ; lu par ce nom, jamais affiché ni passé en
#                     argument ; refus si absente, vide, ou hors [A-Za-z0-9_-] de 20 à 100 signes (JMAX) ;
#   SORTIE          : chemin absolu d'un fichier NEUF hors de tout dépôt git ; écrit en droits 600 ;
#   EMPREINTE_ATTENDUE_DU_SCRIPT : si donnée, le script de démarrage doit l'avoir.
# v3 :
#  - « declare +x J » avant que le jeton y soit rangé : même si la session exporte déjà une variable J, aucun enfant du
#    fabricant n'hérite du jeton (constat de la contre-lecture S de la v2, question 1) ;
#  - données = AMORCE (amorce-demarrage-essai-3-v5.sh) : ligne 1 ; H0_PREVU=<date -u> ; JETON_DEMARRAGE='<jeton>' ;
#    E_SCRIPT=<empreinte du script> ; lignes 3 et suivantes de l'amorce (sa ligne 2 doit être le repère) ;
#    __CHARGE_DES_PIECES__ ; charge = tar déterministe du script de démarrage v3 et des quatre pièces, gzip -9 -n, base64
#    sur une ligne (gzip, et non xz : l'amorce extrait la charge AVANT l'installation des paquets ; gzip est essentiel
#    dans debian). Le script de démarrage ne passe plus en clair : il est dans la charge, contrôlé par l'amorce à son
#    empreinte ; il ne tenait plus en clair sous 32 Kio avec les corrections de la v3 (rapport).
# Inchangé depuis v2 : taille en lecture stricte (chaîne JSON échappée en ASCII, guillemets compris, jeton de JMAX
# signes ; HTML de Go pour information) ; refus d'une porte d'essai ou de --no-verify ; branche neuve vérifiée par
# git ls-remote en lecture ; réglages d'essai FABRICANT_SCRIPT, FABRICANT_DEPOT_DISTANT seulement avec FABRICANT_BANC=oui.
# Codes : 2 usage ou réglage d'essai sans banc ; 3 jeton ; 4 sortie ; 5 script, amorce ou pièce autre, porte d'essai ou
# --no-verify ; 6 trop grand, ou signe non ASCII ou de contrôle ; 7 écriture ou contrôle ; 8 branche présente ou
# vérification impossible. À tout refus après l'écriture de la charge, les fichiers écrits par cet appel sont retirés.
set -u -o pipefail
declare +x J
ICI=$(cd "$(dirname "$0")" && pwd)
refus() { [ ${#CREES[@]} -eq 0 ] || rm -f "${CREES[@]}"; echo "refus ($1) : $2" >&2; exit "$1"; }
CREES=()
BANC=${FABRICANT_BANC:-}
if [ "$BANC" != oui ] && { [ -n "${FABRICANT_SCRIPT+x}" ] || [ -n "${FABRICANT_DEPOT_DISTANT+x}" ]; }; then
  refus 2 "réglage d'essai FABRICANT_* sans FABRICANT_BANC=oui"
fi
SCRIPT=${FABRICANT_SCRIPT:-$ICI/demarrage-machine-essai-3-v5.sh}
AMORCE=$ICI/amorce-demarrage-essai-3-v5.sh
NOM_DANS_CHARGE=demarrage-machine-essai-3-v5.sh
P=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1
D_L4=$P/auteur-lanceur-v4
D_G4=$P/auteur-lanceur-v3-gardien-v4
LIMITE=32768
JMAX=100
PIECES="b989db6e2e17772b74ec8ac99a5ed2708bf305d212a5e6825ed210759b7b5865 $D_L4 lancer-essai-3-v4.sh
64b2c0ce03e1e586547580cbed62f8e8c84bbd798c695a588202955809105937 $D_L4 demarrer-essai-3-v4.sh
ba39fe9be5d6fbf760e409d7677ed60662f6118103cb7bd75b93a6786d6246ed $D_G4 gardien-essai-3-v4.py
b333b2eb4bac58c567e0a2efa479ae424dccc6fa9d88fe5a4d95011cb2ce6232 $D_G4 demarrer-gardien-essai-3-v4.sh"

if [ $# -ne 2 ] && [ $# -ne 3 ]; then refus 2 "usage : $0 NOM_DE_VARIABLE SORTIE [EMPREINTE_ATTENDUE_DU_SCRIPT]"; fi
NOM=$1
SORTIE=$2
[[ "$NOM" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]] || refus 2 "nom de variable mal formé"
case " J NOM SORTIE ICI SCRIPT AMORCE P D_L4 D_G4 LIMITE JMAX PIECES PATH HOME BANC CREES NOM_DANS_CHARGE " in
  *" $NOM "*) refus 2 "nom de variable réservé : $NOM" ;;
esac
J=${!NOM-}
unset "$NOM"  # les commandes lancées ensuite n'héritent pas du jeton par cette variable non plus
[ -n "$J" ] || refus 3 "la variable $NOM est absente ou vide"
[[ "$J" =~ ^[A-Za-z0-9_-]{20,100}$ ]] || refus 3 "le jeton de $NOM est mal formé (signes ou longueur ; non affiché)"
case "$SORTIE" in /*) ;; *) refus 4 "sortie non absolue : $SORTIE" ;; esac
case "$SORTIE" in */.git/*) refus 4 "sortie dans un dossier .git" ;; esac
for f in "$SORTIE" "$SORTIE.sans-jeton" "$SORTIE.charge.b64" "$SORTIE.empreintes.txt"; do
  if [ -e "$f" ] || [ -L "$f" ]; then refus 4 "$f déjà présent (rien n'est écrasé)"; fi
done
DS=$(dirname "$SORTIE")
[ -d "$DS" ] || refus 4 "dossier de la sortie absent : $DS"
if git -C "$DS" rev-parse --git-dir > /dev/null 2>&1; then refus 4 "la sortie est dans un dépôt git : $DS"; fi

[ -f "$SCRIPT" ] && [ -f "$AMORCE" ] || refus 5 "script ou amorce absent"
E_SCRIPT=$(sha256sum < "$SCRIPT" | cut -c1-64)
E_AMORCE=$(sha256sum < "$AMORCE" | cut -c1-64)
if [ $# -eq 3 ] && [ "$E_SCRIPT" != "$3" ]; then refus 5 "empreinte du script $E_SCRIPT, attendue $3"; fi
[ "$(sed -n 2p "$AMORCE")" = "# @DONNEES-DE-DEMARRAGE@" ] || refus 5 "ligne 2 de l'amorce autre que le repère"
[ "$(grep -c -x '__CHARGE_DES_PIECES__' "$AMORCE")" = 0 ] || refus 5 "l'amorce porte déjà une ligne __CHARGE_DES_PIECES__"
grep -q -F "demarrage-machine-essai-3-v5.sh" "$AMORCE" || refus 5 "l'amorce ne lit pas $NOM_DANS_CHARGE"
for x in "$SCRIPT" "$AMORCE"; do
  if grep -n -E 'ESSAI_DEMARRAGE_[A-Za-z0-9_]*=' "$x" >&2; then refus 5 "affectation d'une porte d'essai dans $x"; fi
  if grep -n -F -e '--no-verify' "$x" >&2; then refus 5 "option --no-verify dans $x"; fi
done
BRANCHE=$(sed -n 's/^BRANCHE=//p' "$SCRIPT")
DEPOT_URL=$(sed -n 's/^DEPOT_URL=//p' "$SCRIPT")
[[ "$BRANCHE" =~ ^[A-Za-z0-9/._-]+$ ]] && [ -n "$DEPOT_URL" ] || refus 5 "BRANCHE ou DEPOT_URL illisibles dans le script"
NOMS=()
while read -r e d f; do
  [ -f "$d/$f" ] && [ ! -L "$d/$f" ] || refus 5 "pièce absente ou non régulière : $d/$f"
  L=$(sha256sum < "$d/$f" | cut -c1-64)
  [ "$L" = "$e" ] || refus 5 "empreinte de $f : $L, attendue $e"
  grep -q -F "$e $f" "$SCRIPT" || refus 5 "le script n'attend pas $e pour $f"
  NOMS+=("$f")
done <<< "$PIECES"

# branche de récupération : elle ne doit pas exister sur le dépôt distant (lecture seule, aucun jeton déposé)
DEPOT_DISTANT=${FABRICANT_DEPOT_DISTANT:-$DEPOT_URL}
CMD_BRANCHE="GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code --heads $DEPOT_DISTANT refs/heads/$BRANCHE"
GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code --heads "$DEPOT_DISTANT" "refs/heads/$BRANCHE" > /dev/null 2>&1
c=$?
case $c in
  2) ;;
  0) refus 8 "la branche $BRANCHE existe déjà sur $DEPOT_DISTANT" ;;
  *) refus 8 "vérification de la branche impossible (code $c) : $CMD_BRANCHE" ;;
esac

H0=$(date -u +%Y-%m-%dT%H:%M:%SZ)
H_ARRET=$(date -u -d "@$(( $(date -u -d "$H0" +%s) + 94 * 3600 ))" +%Y-%m-%dT%H:%M:%SZ)
umask 022
CREES=("$SORTIE.charge.b64" "$SORTIE.sans-jeton")
B=$(basename "$SCRIPT")
tar --sort=name --mtime=@0 --owner=0 --group=0 --numeric-owner --mode=u=rw,go=r --format=gnu \
  --transform "s|^$B\$|$NOM_DANS_CHARGE|" -c -C "$D_L4" "${NOMS[0]}" "${NOMS[1]}" -C "$D_G4" "${NOMS[2]}" "${NOMS[3]}" \
  -C "$(dirname "$SCRIPT")" "$B" | gzip -9 -n | base64 -w 0 > "$SORTIE.charge.b64" && echo >> "$SORTIE.charge.b64" \
  || refus 7 "fabrication de la charge"
assembler() {  # $1 : texte de la ligne du jeton (printf, commande interne : jamais dans une ligne de commande)
  sed -n 1p "$AMORCE" && printf 'H0_PREVU=%s\n' "$H0" && printf "JETON_DEMARRAGE='%s'\n" "$1" \
    && printf 'E_SCRIPT=%s\n' "$E_SCRIPT" && sed -n '3,$p' "$AMORCE" && echo __CHARGE_DES_PIECES__ && cat "$SORTIE.charge.b64"
}
assembler @JETON@ > "$SORTIE.sans-jeton" || refus 7 "texte sans jeton"
E_SANS=$(sha256sum < "$SORTIE.sans-jeton" | cut -c1-64)
X=$(LC_ALL=C tr -d '\n\t\040-\176' < "$SORTIE.sans-jeton" | wc -c)
[ "$X" = 0 ] || refus 6 "$X octets non ASCII ou de contrôle (hors saut de ligne et tabulation) dans les données"
OCT=$(( $(wc -c < "$SORTIE.sans-jeton") - 7 ))
E2=$(LC_ALL=C tr -cd '"\\\n\t' < "$SORTIE.sans-jeton" | wc -c)
E6=$(LC_ALL=C tr -cd '<>&' < "$SORTIE.sans-jeton" | wc -c)
STRICT=$(( OCT + JMAX + E2 + 2 ))
GO=$(( STRICT + 5 * E6 ))
TAILLE=$(( OCT + ${#J} ))
[ "$STRICT" -le "$LIMITE" ] || refus 6 "données de $STRICT octets en lecture stricte (jeton de $JMAX signes), plus que $LIMITE"

umask 077
set -C
if ! assembler "$J" > "$SORTIE"; then rm -f "$SORTIE"; refus 7 "écriture de $SORTIE"; fi
set +C
unset J
CREES+=("$SORTIE")
chmod 600 "$SORTIE"
[ "$(stat -c %a "$SORTIE")" = 600 ] || refus 7 "droits de $SORTIE autres que 600"
E_CTRL=$(sed "3s/.*/JETON_DEMARRAGE='@JETON@'/" "$SORTIE" | sha256sum | cut -c1-64)
if [ "$E_CTRL" != "$E_SANS" ] || [ "$(wc -c < "$SORTIE")" != "$TAILLE" ]; then
  refus 7 "contrôle : $SORTIE, jeton masqué, autre que le texte sans jeton"
fi
umask 022
{
  [ "$BANC" = oui ] && echo "DONNÉES D'ESSAI (FABRICANT_BANC=oui) : script $SCRIPT ; dépôt distant vérifié $DEPOT_DISTANT"
  echo "fabrication : $(date -u +%Y-%m-%dT%H:%M:%SZ) ; jeton lu par la variable $NOM (non écrit ici)"
  echo "H0_PREVU=$H0 ; heure d'arrêt de durée du gardien : $H_ARRET (H0_PREVU + 94 h)"
  echo "script de démarrage (dans la charge, sous le nom $NOM_DANS_CHARGE) : $E_SCRIPT  $SCRIPT"
  echo "amorce : $E_AMORCE  $AMORCE"
  while read -r e d f; do echo "pièce : $e  $d/$f"; done <<< "$PIECES"
  echo "charge : $(sha256sum < "$SORTIE.charge.b64" | cut -c1-64)  $SORTIE.charge.b64"
  echo "données de démarrage sans jeton : $E_SANS  $SORTIE.sans-jeton"
  echo "données de démarrage (avec jeton, droits 600) : $TAILLE octets  $SORTIE"
  echo "taille en lecture stricte (chaîne JSON échappée en ASCII, jeton de $JMAX signes) : $STRICT octets ; limite $LIMITE ; marge $((LIMITE - STRICT))"
  echo "information : même chaîne avec l'échappement HTML de Go (< > & en \\u00XX) : $GO octets ; marge $((LIMITE - GO))"
  echo "branche absente du dépôt distant, vérifiée par : $CMD_BRANCHE (code 2 : absente)"
} > "$SORTIE.empreintes.txt" || refus 7 "écriture des empreintes"
cat "$SORTIE.empreintes.txt"
