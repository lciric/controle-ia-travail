#!/bin/bash
# § 5.2 — fin du lancement : sortie gardée et scellée, relevé rendu à la conductrice
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
# seulement, le bloc « § 5.2, relevé » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-2-releve-apres-lancement.sh 1
. "$(dirname "$0")/commun.sh"
N="${1:-}"; exiger_numero "$N"
RUNL="$(cat "$T/run-lecture-$N.txt")"; SORTIE="$T/sortie-lancement-$N.txt"
if [ -e "$T/lancement-$N.code" ]; then CODE="$(cat "$T/lancement-$N.code")"
elif [ ! -s "$T/lancement-$N.pid" ]; then echo "identifiant du processus non écrit : rendu à la conductrice, rien d'autre"; exit 1
elif ps -p "$(cat "$T/lancement-$N.pid")" > /dev/null 2>&1; then echo "le lancement n'est pas fini : on attend"; exit 1
else CODE=absent; fi
G1="$LV1/sortie-lancement-lecture-bbis-$N-v1.txt"; neuf "$G1"
cp "$SORTIE" "$G1" && sceller "registres/t07-etape-b-bis/lecture-v1/sortie-lancement-lecture-bbis-$N-v1.txt"
L1="$LV1/lancement-lecture-bbis-$N-v1.sh"; neuf "$L1"
cp "$T/lancement-$N.sh" "$L1" && sceller "registres/t07-etape-b-bis/lecture-v1/lancement-lecture-bbis-$N-v1.sh"
S_N="$(grep -c 'BBIS LECTURE ENTREES OUVERTES' "$G1" 2>/dev/null)"; NC_N="$(grep -c '^BBIS LECTURE NON CONSOMMEE ' "$G1" 2>/dev/null)"
AR_N="$(grep -c '^BBIS LECTURE ARRET' "$G1")"
F="diag/$RUNL/lecture-bbis.json"; M="runs/$RUNL/manifeste.json"
R="$LV1/releve-apres-lancement-lecture-bbis-$N-v1.txt"; neuf "$R"
ecrit() { if [ -f "$ARBRE/$1" ]; then dire "$2 : $1 $(sha256sum "$ARBRE/$1" | cut -d' ' -f1) ; compagnon égal : $([ "$(cut -d' ' -f1 "$ARBRE/$1.sha256" 2>/dev/null)" = "$(sha256sum "$ARBRE/$1" | cut -d' ' -f1)" ] && echo oui || echo non)"; else dire "$2 : non écrit"; fi; }
{
dire "Relevé d'après lancement n° $N — run de lecture $RUNL"
dire "identifiant du processus $(cat "$T/lancement-$N.pid" 2>/dev/null)"
[ "$CODE" = 0 ] || dire "début $(cat "$T/lancement-$N.debut") ; fin $(cat "$T/lancement-$N.fin" 2>/dev/null)"
dire "code de sortie : $CODE"
dire "sortie gardée : registres/t07-etape-b-bis/lecture-v1/sortie-lancement-lecture-bbis-$N-v1.txt $(sha256sum "$G1" | cut -d' ' -f1)"
dire "lancement gardé : registres/t07-etape-b-bis/lecture-v1/lancement-lecture-bbis-$N-v1.sh $(sha256sum "$L1" | cut -d' ' -f1)"
if [ "$CODE" = 0 ] && [ -f "$ARBRE/$F" ]; then
  dire "ETAT : écrit"
  ecrit "$F" "fichier de lecture"; ecrit "$M" "manifeste"
elif [ "$CODE" = 3 ] && [ "$NC_N" = 1 ] && [ "$S_N" = 0 ] && [ -f "$ARBRE/$F" ]; then
  dire "ETAT : non consommée (pur défaut de mise en place, rien d'ouvert)"
  ecrit "$F" "fichier de lecture gardé"; ecrit "diag/$RUNL/preuve-aucune-ouverture-bbis.json" "pièce de preuve"; ecrit "$M" "manifeste"
elif [ "$CODE" = 0 ] || [ "$CODE" = 3 ]; then
  dire "ETAT : non prévu (code $CODE sans les fichiers ou les lignes attendus)"
elif [ ! -s "$G1.sha256" ]; then
  dire "ETAT : sortie non gardée (complément au quatrième addendum, « La suite », point 3 : lecture consommée, aucune relance ; nœud)"
elif [ "$S_N" = 0 ]; then
  dire "ETAT : arrêt avant le seuil"
  dire "lignes du seuil « BBIS LECTURE ENTREES OUVERTES » : $S_N ; lignes « BBIS LECTURE NON CONSOMMEE » : $NC_N ; lignes « BBIS LECTURE ARRET » : $AR_N"
  ecrit "$F" "fichier de lecture"; ecrit "$M" "manifeste"
  dire "dernières lignes de la sortie gardée (compte de la ligne du seuil : zéro ; rien n'a été ouvert, la sortie ne peut porter aucune mesure) :"
  tail -n 40 "$G1"
  dire "(fin de l'extrait)"
else
  dire "ETAT : arrêt après le seuil"
  dire "lignes du seuil « BBIS LECTURE ENTREES OUVERTES » : $S_N"
fi
dire "lignes de statut de l'arbre de lecture : $(git -C "$ARBRE" status --porcelain --untracked-files=all | wc -l | tr -d ' ')"
} > "$R" 2>&1
sceller "registres/t07-etape-b-bis/lecture-v1/releve-apres-lancement-lecture-bbis-$N-v1.txt"
cat "$R"; sha256sum "$R"
