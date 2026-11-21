#!/bin/bash
# Lanceur de l'essai court de mesure du palier 0b — v2 (v1 inchangée sur le fond ; v2 : contrôle de l'état de la racine
# sans écriture de l'index, GIT_OPTIONAL_LOCKS=0).
# Porte la commande du complément 1 v3 (sha256 1484cd7586156e33f1617e6e2e07c13e7241e75f8c03e5f703a94f1187be7268),
# à l'octet sauf le dernier argument (dossier des sorties), remplacé par le dossier de l'essai court.
#
# Emploi :  lancer-essai-court-v2.sh DOSSIER_DE_TENUE
# Essai :   lancer-essai-court-v2.sh DOSSIER_DE_TENUE --verifier-seulement RACINE TETE EMPREINTE PROGRAMME SORTIES
#           (contrôles de départ sur des valeurs passées en paramètre ; la commande n'est JAMAIS exécutée dans ce mode)
#
# Refus de départ (code écrit dans code-de-sortie.txt, rien n'est lancé) :
#   10 dossier des sorties déjà présent ; 11 tête de la racine différente ou illisible ;
#   12 fichiers suivis de la racine modifiés (ou état illisible) ; 13 empreinte du programme différente ou illisible.
# Autres codes : 2 usage ; 3 dossier de tenue absent ; 4 code-de-sortie.txt déjà présent (rien n'est écrasé, rien n'est lancé).
# En mode emploi, le code écrit est celui de la commande (143 = arrêt par signal de fin, reçu aussi par le programme).
set -u

if [ $# -lt 1 ]; then
  echo "usage : $0 DOSSIER_DE_TENUE [--verifier-seulement RACINE TETE EMPREINTE PROGRAMME SORTIES]" >&2
  exit 2
fi
TENUE=$1
RACINE=/home/user/palier-0b-racine
TETE_ATTENDUE=d7f949acd9ac92e998e57663d2cc741de93f18c3
EMPREINTE_ATTENDUE=1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14
PROGRAMME=/home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py
SORTIES=/home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-court-mesure-v1
MODE=emploi
if [ $# -gt 1 ]; then
  if [ $# -ne 7 ] || [ "$2" != "--verifier-seulement" ]; then
    echo "usage : $0 DOSSIER_DE_TENUE [--verifier-seulement RACINE TETE EMPREINTE PROGRAMME SORTIES]" >&2
    exit 2
  fi
  RACINE=$3
  TETE_ATTENDUE=$4
  EMPREINTE_ATTENDUE=$5
  PROGRAMME=$6
  SORTIES=$7
  MODE=verification
fi

if [ ! -d "$TENUE" ]; then
  echo "refus : dossier de tenue absent : $TENUE" >&2
  exit 3
fi
FICHIER_CODE="$TENUE/code-de-sortie.txt"
if [ -e "$FICHIER_CODE" ] || [ -L "$FICHIER_CODE" ]; then
  echo "refus : $FICHIER_CODE déjà présent (rien n'est écrasé) : aucun départ" >&2
  exit 4
fi

refuser() {
  echo "refus de départ ($(date -u +%Y-%m-%dT%H:%M:%SZ)) : $2" >&2
  echo "$1" > "$FICHIER_CODE"
  exit "$1"
}

echo "lanceur essai court v2 : mode $MODE, départ demandé à $(date -u +%Y-%m-%dT%H:%M:%SZ)" >&2

# 1. dossier des sorties : neuf
if [ -e "$SORTIES" ] || [ -L "$SORTIES" ]; then
  refuser 10 "dossier des sorties déjà présent : $SORTIES"
fi

# 2. tête de la racine
TETE_LUE=$(git -C "$RACINE" rev-parse --verify HEAD 2>&1)
if [ $? -ne 0 ] || [ "$TETE_LUE" != "$TETE_ATTENDUE" ]; then
  refuser 11 "tête de $RACINE : « $TETE_LUE », attendue $TETE_ATTENDUE"
fi

# 3. aucune modification des fichiers suivis (index et arbre de travail)
#    (GIT_OPTIONAL_LOCKS=0 : git status ne réécrit pas l'index de la racine pour y rafraîchir les heures)
ETAT=$(GIT_OPTIONAL_LOCKS=0 git -C "$RACINE" status --porcelain --untracked-files=no 2>&1)
if [ $? -ne 0 ] || [ -n "$ETAT" ]; then
  refuser 12 "fichiers suivis de $RACINE modifiés ou état illisible : $ETAT"
fi

# 4. empreinte du programme
LIGNE_EMPREINTE=$(sha256sum "$PROGRAMME" 2>&1)
if [ $? -ne 0 ]; then
  refuser 13 "empreinte de $PROGRAMME illisible : $LIGNE_EMPREINTE"
fi
EMPREINTE_LUE=${LIGNE_EMPREINTE%% *}
if [ "$EMPREINTE_LUE" != "$EMPREINTE_ATTENDUE" ]; then
  refuser 13 "empreinte de $PROGRAMME : $EMPREINTE_LUE, attendue $EMPREINTE_ATTENDUE"
fi

if [ "$MODE" = verification ]; then
  echo "vérification seule : départ permis ; la commande n'est pas exécutée" >&2
  echo 0 > "$FICHIER_CODE"
  exit 0
fi

echo "départ du programme à $(date -u +%Y-%m-%dT%H:%M:%S.%NZ)" >&2
# Un piège sur le signal de fin : l'interpréteur ne meurt pas avant le programme (qui reçoit lui-même le signal, adressé au
# groupe) ; il écrit ensuite le code. Le piège ne passe pas au programme (dispositions par défaut rétablies à l'exécution).
trap 'echo "signal de fin reçu par le lanceur à $(date -u +%Y-%m-%dT%H:%M:%SZ)" >&2' TERM
env -C /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6 PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v19.md /home/user/palier-0b-racine /home/user/palier-0b-racine/docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-court-mesure-v1
CODE=$?
echo "$CODE" > "$FICHIER_CODE"
echo "fin du programme à $(date -u +%Y-%m-%dT%H:%M:%SZ), code $CODE" >&2
exit "$CODE"
