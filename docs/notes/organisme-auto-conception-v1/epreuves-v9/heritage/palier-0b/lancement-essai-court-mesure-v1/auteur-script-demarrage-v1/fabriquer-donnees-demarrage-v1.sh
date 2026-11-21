#!/bin/bash
# Fabricant des données de démarrage de la machine de l'essai 3 du palier 0b — v1 (mandat dcd05a42, point 2).
# Joué dans la session juste avant la création de la machine.
#
# Emploi : fabriquer-donnees-demarrage-v1.sh NOM_DE_VARIABLE SORTIE [EMPREINTE_ATTENDUE_DU_SCRIPT]
#   NOM_DE_VARIABLE : NOM d'une variable d'environnement qui porte le jeton ; le jeton est lu par ce nom, jamais affiché,
#                     jamais passé en argument ; refus si la variable est absente, vide, ou si le jeton sort de [A-Za-z0-9_-]
#                     (20 à 400 signes) ;
#   SORTIE          : chemin absolu d'un fichier NEUF, hors de tout dépôt git ; écrit en droits 600 : les données de démarrage
#                     complètes (script, H0_PREVU, jeton, charge des quatre pièces) ;
#   EMPREINTE_ATTENDUE_DU_SCRIPT : si donnée, le script de démarrage doit l'avoir (sinon refus 5).
# Données de démarrage = ligne 1 du script ; « H0_PREVU=<date -u de la fabrication> » ; « JETON_DEMARRAGE='<jeton>' » ;
# lignes 3 à la fin du script (sa ligne 2 doit être « # @DONNEES-DE-DEMARRAGE@ ») ; « __CHARGE_DES_PIECES__ » ; la charge
# (tar déterministe des quatre pièces, xz -9e, base64 sur une ligne).
# Écrit aussi, sans le jeton : SORTIE.sans-jeton (le même texte, la ligne du jeton étant « JETON_DEMARRAGE='@JETON@' »),
# SORTIE.charge.b64 et SORTIE.empreintes.txt (empreintes du script, des pièces, de la charge et du texte sans jeton ;
# H0_PREVU ; heure d'arrêt de durée ; taille). Contrôle : SORTIE, ligne 3 remplacée par celle du texte sans jeton, a la
# même empreinte que SORTIE.sans-jeton. Taille au plus LIMITE octets (données de démarrage de Hetzner : 32 Kio, supposé).
# Codes : 2 usage ; 3 jeton absent, vide ou mal formé ; 4 sortie présente, relative ou dans un dépôt ; 5 script ou pièce
# autre que l'attendu ; 6 trop grand ; 7 écriture ou contrôle. À tout refus 6 ou 7, les fichiers déjà écrits par cet appel
# (SORTIE, SORTIE.sans-jeton, SORTIE.charge.b64) sont retirés. FABRICANT_SCRIPT : autre script, pour les essais seulement.
set -u -o pipefail
ICI=$(cd "$(dirname "$0")" && pwd)
SCRIPT=${FABRICANT_SCRIPT:-$ICI/demarrage-machine-essai-3-v1.sh}
P=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1
D_L4=$P/auteur-lanceur-v4
D_G4=$P/auteur-lanceur-v3-gardien-v4
LIMITE=32768
PIECES="b989db6e2e17772b74ec8ac99a5ed2708bf305d212a5e6825ed210759b7b5865 $D_L4 lancer-essai-3-v4.sh
64b2c0ce03e1e586547580cbed62f8e8c84bbd798c695a588202955809105937 $D_L4 demarrer-essai-3-v4.sh
ba39fe9be5d6fbf760e409d7677ed60662f6118103cb7bd75b93a6786d6246ed $D_G4 gardien-essai-3-v4.py
b333b2eb4bac58c567e0a2efa479ae424dccc6fa9d88fe5a4d95011cb2ce6232 $D_G4 demarrer-gardien-essai-3-v4.sh"

CREES=()
refus() { [ ${#CREES[@]} -eq 0 ] || rm -f "${CREES[@]}"; echo "refus ($1) : $2" >&2; exit "$1"; }
if [ $# -ne 2 ] && [ $# -ne 3 ]; then refus 2 "usage : $0 NOM_DE_VARIABLE SORTIE [EMPREINTE_ATTENDUE_DU_SCRIPT]"; fi
NOM=$1
SORTIE=$2
[[ "$NOM" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]] || refus 2 "nom de variable mal formé"
case " J NOM SORTIE ICI SCRIPT P D_L4 D_G4 LIMITE PIECES PATH HOME " in *" $NOM "*) refus 2 "nom de variable réservé : $NOM" ;; esac
J=${!NOM-}
unset "$NOM"  # les commandes lancées ensuite n'héritent pas du jeton dans leur environnement
[ -n "$J" ] || refus 3 "la variable $NOM est absente ou vide"
[[ "$J" =~ ^[A-Za-z0-9_-]{20,400}$ ]] || refus 3 "le jeton de $NOM est mal formé (signes ou longueur ; non affiché)"
case "$SORTIE" in /*) ;; *) refus 4 "sortie non absolue : $SORTIE" ;; esac
case "$SORTIE" in */.git/*) refus 4 "sortie dans un dossier .git" ;; esac
for f in "$SORTIE" "$SORTIE.sans-jeton" "$SORTIE.charge.b64" "$SORTIE.empreintes.txt"; do
  if [ -e "$f" ] || [ -L "$f" ]; then refus 4 "$f déjà présent (rien n'est écrasé)"; fi
done
DS=$(dirname "$SORTIE")
[ -d "$DS" ] || refus 4 "dossier de la sortie absent : $DS"
if git -C "$DS" rev-parse --git-dir > /dev/null 2>&1; then refus 4 "la sortie est dans un dépôt git : $DS"; fi

[ -f "$SCRIPT" ] || refus 5 "script absent : $SCRIPT"
E_SCRIPT=$(sha256sum < "$SCRIPT" | cut -c1-64)
if [ $# -eq 3 ] && [ "$E_SCRIPT" != "$3" ]; then refus 5 "empreinte du script $E_SCRIPT, attendue $3"; fi
[ "$(sed -n 2p "$SCRIPT")" = "# @DONNEES-DE-DEMARRAGE@" ] || refus 5 "ligne 2 du script autre que « # @DONNEES-DE-DEMARRAGE@ »"
[ "$(grep -c -x '__CHARGE_DES_PIECES__' "$SCRIPT")" = 0 ] || refus 5 "le script porte déjà une ligne __CHARGE_DES_PIECES__"
NOMS=()
while read -r e d f; do
  [ -f "$d/$f" ] && [ ! -L "$d/$f" ] || refus 5 "pièce absente ou non régulière : $d/$f"
  L=$(sha256sum < "$d/$f" | cut -c1-64)
  [ "$L" = "$e" ] || refus 5 "empreinte de $f : $L, attendue $e"
  grep -q -F "$e $f" "$SCRIPT" || refus 5 "le script n'attend pas $e pour $f"
  NOMS+=("$f")
done <<< "$PIECES"

H0=$(date -u +%Y-%m-%dT%H:%M:%SZ)
H_ARRET=$(date -u -d "@$(( $(date -u -d "$H0" +%s) + 94 * 3600 ))" +%Y-%m-%dT%H:%M:%SZ)
umask 022
CREES=("$SORTIE.charge.b64" "$SORTIE.sans-jeton")  # retirés à tout refus qui suit (ils ne portent pas le jeton)
tar --sort=name --mtime=@0 --owner=0 --group=0 --numeric-owner --mode=u=rw,go=r --format=gnu -c \
  -C "$D_L4" "${NOMS[0]}" "${NOMS[1]}" -C "$D_G4" "${NOMS[2]}" "${NOMS[3]}" | xz -9e -T1 -c | base64 -w 0 \
  > "$SORTIE.charge.b64" && echo >> "$SORTIE.charge.b64" || refus 7 "fabrication de la charge"
assembler() {  # $1 : texte de la ligne du jeton (passé à printf, builtin : jamais dans une ligne de commande)
  sed -n 1p "$SCRIPT" && printf 'H0_PREVU=%s\n' "$H0" && printf "JETON_DEMARRAGE='%s'\n" "$1" && sed -n '3,$p' "$SCRIPT" \
    && echo __CHARGE_DES_PIECES__ && cat "$SORTIE.charge.b64"
}
assembler @JETON@ > "$SORTIE.sans-jeton" || refus 7 "texte sans jeton"
E_SANS=$(sha256sum < "$SORTIE.sans-jeton" | cut -c1-64)
TAILLE=$(( $(wc -c < "$SORTIE.sans-jeton") - 7 + ${#J} ))
[ "$TAILLE" -le "$LIMITE" ] || refus 6 "données de démarrage de $TAILLE octets, plus que $LIMITE"

umask 077
set -C
if ! assembler "$J" > "$SORTIE"; then rm -f "$SORTIE"; refus 7 "écriture de $SORTIE"; fi
set +C
unset J
chmod 600 "$SORTIE"
if [ "$(stat -c %a "$SORTIE")" != 600 ]; then rm -f "$SORTIE"; refus 7 "droits de $SORTIE autres que 600"; fi
E_CTRL=$(sed "3s/.*/JETON_DEMARRAGE='@JETON@'/" "$SORTIE" | sha256sum | cut -c1-64)
if [ "$E_CTRL" != "$E_SANS" ] || [ "$(wc -c < "$SORTIE")" != "$TAILLE" ]; then
  rm -f "$SORTIE"; refus 7 "contrôle : $SORTIE, jeton masqué, autre que le texte sans jeton"
fi
umask 022
{
  echo "fabrication : $(date -u +%Y-%m-%dT%H:%M:%SZ) ; jeton lu par la variable $NOM (non écrit ici)"
  echo "H0_PREVU=$H0 ; heure d'arrêt de durée du gardien : $H_ARRET (H0_PREVU + 94 h)"
  echo "script de démarrage : $E_SCRIPT  $SCRIPT"
  while read -r e d f; do echo "pièce : $e  $d/$f"; done <<< "$PIECES"
  echo "charge : $(sha256sum < "$SORTIE.charge.b64" | cut -c1-64)  $SORTIE.charge.b64"
  echo "données de démarrage sans jeton : $E_SANS  $SORTIE.sans-jeton"
  echo "données de démarrage (avec jeton, droits 600) : $TAILLE octets (limite $LIMITE)  $SORTIE"
} > "$SORTIE.empreintes.txt" || refus 7 "écriture des empreintes"
cat "$SORTIE.empreintes.txt"
