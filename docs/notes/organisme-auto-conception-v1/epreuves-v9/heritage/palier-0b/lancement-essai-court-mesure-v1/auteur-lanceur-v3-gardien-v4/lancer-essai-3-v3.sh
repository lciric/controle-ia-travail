#!/bin/bash
# Lanceur de l'essai 3 du palier 0b (serveur loué) — v3 (devis de l'essai 3, v5, § 4.1 ; GO-2026-11-21-73).
# v3 = lanceur v2 de l'essai court, plus : racine, interpréteur et dossier des sorties passés en paramètres ; contrôle de la
# tête par un fichier écrit avec la copie quand la racine n'a pas de .git ; refus si l'interpréteur manque.
# Porte la commande du complément 1 v3 (sha256 de l'extraction v2 : 56ed20f89c3b9d9237350aeda092c815b6faee54b9048ba948659328d75bb867),
# à l'octet, aux trois chemins près : racine ("$RACINE"), interpréteur ("$INTERPRETE"), dossier des sorties ("$SORTIES")
# (vérifié par verifier-commande-v3.py).
#
# Emploi :  lancer-essai-3-v3.sh DOSSIER_DE_TENUE RACINE INTERPRETE SORTIES
# Contrôle seul, sans départ (sur le serveur avant le départ, ou en essai) :
#           lancer-essai-3-v3.sh DOSSIER_DE_TENUE RACINE INTERPRETE SORTIES --verifier-seulement [TETE EMPREINTE]
#           (TETE et EMPREINTE remplacent les valeurs attendues, pour les essais sur racine factice ; la commande n'est
#            JAMAIS exécutée dans ce mode ; code 0 écrit si le départ serait permis)
# RACINE, INTERPRETE et SORTIES : chemins absolus.
#
# Deux formes de racine :
#   - avec .git (dépôt) : tête lue par git rev-parse, fichiers suivis non modifiés (git status, sans écrire l'index), comme en v2 ;
#   - sans .git (copie de l'arbre du commit, sur le serveur) : RACINE/COMMIT-DE-LA-COPIE.txt doit porter exactement la tête
#     attendue (40 caractères hexadécimaux, une ligne) ; RACINE/EMPREINTES-DE-LA-COPIE.txt (sortie de sha256sum, chemins
#     relatifs « ./… » à la racine, un fichier régulier par ligne, ces deux fichiers exclus) doit se vérifier entièrement par
#     sha256sum --check --strict, et compter autant de lignes, sans doublon, que la copie compte de fichiers réguliers hors
#     ces deux fichiers. Fabrication sur le poste, dans la copie extraite du commit, avant l'envoi :
#       find . -type f ! -path ./COMMIT-DE-LA-COPIE.txt ! -path ./EMPREINTES-DE-LA-COPIE.txt -print0 | sort -z \
#         | xargs -0 sha256sum > EMPREINTES-DE-LA-COPIE.txt
#
# Refus de départ (code écrit dans code-de-sortie.txt, rien n'est lancé) :
#   10 dossier des sorties déjà présent ;
#   11 tête de la racine différente ou illisible (avec .git) ; sans .git : COMMIT-DE-LA-COPIE.txt absent, illisible ou autre ;
#      racine absente ;
#   12 fichiers suivis de la racine modifiés ou état illisible (avec .git) ; sans .git : EMPREINTES-DE-LA-COPIE.txt absent,
#      une empreinte fausse, un fichier manquant, ou un compte différent ;
#   13 empreinte du programme différente ou illisible ;
#   14 interpréteur absent, non régulier ou non exécutable.
# Autres codes : 2 usage (ou chemin non absolu) ; 3 dossier de tenue absent ; 4 code-de-sortie.txt déjà présent (rien n'est
# écrasé, rien n'est lancé). En emploi, le code écrit est celui de la commande (143 = arrêt par signal de fin, reçu aussi par
# le programme).
set -u

usage() {
  echo "usage : $0 DOSSIER_DE_TENUE RACINE INTERPRETE SORTIES [--verifier-seulement [TETE EMPREINTE]]" >&2
  exit 2
}
if [ $# -ne 4 ] && [ $# -ne 5 ] && [ $# -ne 7 ]; then
  usage
fi
TENUE=$1
RACINE=$2
INTERPRETE=$3
SORTIES=$4
TETE_ATTENDUE=d7f949acd9ac92e998e57663d2cc741de93f18c3
EMPREINTE_ATTENDUE=1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14
MODE=emploi
if [ $# -ge 5 ]; then
  if [ "$5" != "--verifier-seulement" ]; then
    usage
  fi
  MODE=verification
  if [ $# -eq 7 ]; then
    TETE_ATTENDUE=$6
    EMPREINTE_ATTENDUE=$7
  fi
fi
for c in "$RACINE" "$INTERPRETE" "$SORTIES"; do
  case "$c" in
    /*) ;;
    *) echo "refus : chemin non absolu : « $c »" >&2; exit 2 ;;
  esac
done
PROGRAMME="$RACINE"/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py
F_COMMIT="$RACINE/COMMIT-DE-LA-COPIE.txt"
F_EMPREINTES="$RACINE/EMPREINTES-DE-LA-COPIE.txt"

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

echo "lanceur essai 3 v3 : mode $MODE, départ demandé à $(date -u +%Y-%m-%dT%H:%M:%SZ) ; racine $RACINE ; interpréteur $INTERPRETE ; sorties $SORTIES" >&2

# 1. dossier des sorties : neuf
if [ -e "$SORTIES" ] || [ -L "$SORTIES" ]; then
  refuser 10 "dossier des sorties déjà présent : $SORTIES"
fi

if [ ! -d "$RACINE" ]; then
  refuser 11 "racine absente ou non dossier : $RACINE"
fi

if [ -e "$RACINE/.git" ]; then
  echo "racine avec .git : contrôle de la tête et des fichiers suivis par git" >&2
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
else
  echo "racine sans .git (copie de l'arbre) : contrôle par $F_COMMIT et $F_EMPREINTES" >&2
  # 2'. commit écrit avec la copie
  if [ ! -f "$F_COMMIT" ] || [ -L "$F_COMMIT" ]; then
    refuser 11 "fichier du commit de la copie absent (ou non régulier) : $F_COMMIT"
  fi
  COMMIT_LU=$(cat "$F_COMMIT" 2>&1)
  if [ $? -ne 0 ] || [ "$COMMIT_LU" != "$TETE_ATTENDUE" ] || [ "$(wc -l < "$F_COMMIT")" != 1 ]; then
    refuser 11 "commit de la copie ($F_COMMIT) : « $COMMIT_LU », attendu $TETE_ATTENDUE sur une seule ligne"
  fi
  # 3'. aucune modification des fichiers de la copie
  if [ ! -f "$F_EMPREINTES" ] || [ -L "$F_EMPREINTES" ]; then
    refuser 12 "liste des empreintes de la copie absente (ou non régulière) : $F_EMPREINTES"
  fi
  CONTROLE=$(cd "$RACINE" && sha256sum --check --strict --quiet EMPREINTES-DE-LA-COPIE.txt 2>&1)
  if [ $? -ne 0 ]; then
    refuser 12 "empreintes de la copie : échec de sha256sum --check : $(printf '%s' "$CONTROLE" | head -c 2000)"
  fi
  N_LISTE=$(wc -l < "$F_EMPREINTES")
  N_UNIQUES=$(cut -c67- "$F_EMPREINTES" | sort -u | wc -l)
  N_COPIE=$(cd "$RACINE" && find . -type f ! -path ./COMMIT-DE-LA-COPIE.txt ! -path ./EMPREINTES-DE-LA-COPIE.txt | wc -l)
  if [ "$N_LISTE" != "$N_UNIQUES" ] || [ "$N_LISTE" != "$N_COPIE" ]; then
    refuser 12 "empreintes de la copie : $N_LISTE lignes, $N_UNIQUES chemins distincts, $N_COPIE fichiers réguliers dans la copie"
  fi
  echo "copie : commit $COMMIT_LU ; $N_LISTE fichiers vérifiés" >&2
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

# 5. interpréteur
if [ ! -f "$INTERPRETE" ] || [ ! -x "$INTERPRETE" ]; then
  refuser 14 "interpréteur absent, non régulier ou non exécutable : $INTERPRETE"
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
env -C "$RACINE"/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6 PYTHONPATH=src "$INTERPRETE" -B "$RACINE"/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py "$RACINE"/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v19.md "$RACINE" "$RACINE"/docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator "$SORTIES"
CODE=$?
echo "$CODE" > "$FICHIER_CODE"
echo "fin du programme à $(date -u +%Y-%m-%dT%H:%M:%SZ), code $CODE" >&2
exit "$CODE"
