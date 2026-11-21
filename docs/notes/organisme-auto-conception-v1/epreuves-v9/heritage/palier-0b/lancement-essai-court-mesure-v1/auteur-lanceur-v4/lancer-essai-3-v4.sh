#!/bin/bash
# Lanceur de l'essai 3 du palier 0b (serveur loué) — v4 (devis de l'essai 3, v5, § 4.1 ; GO-2026-11-21-73 ; correction de la
# mère du 2026-11-21 vers 18:59Z sur la réserve (a) de la vérification du lanceur v3).
# v4 = lanceur v3, plus, pour la racine sans .git seulement : la liste des empreintes de la copie est ANCRÉE AU COMMIT (égale à
# l'octet à la liste de référence, dont l'empreinte est écrite ici, REFERENCE_ATTENDUE) ; la liste refaite sur la copie par la
# même recette doit lui être égale (tout fichier ajouté, manquant ou modifié refusé) ; tout lien symbolique ou fichier spécial
# dans la copie (et une racine qui serait elle-même un lien) refusé. Forme avec .git, commande et autres refus : inchangés.
# v3 = lanceur v2 de l'essai court, plus : racine, interpréteur et dossier des sorties passés en paramètres ; contrôle de la
# tête par un fichier écrit avec la copie quand la racine n'a pas de .git ; refus si l'interpréteur manque.
#
# Liste de référence (35 732 fichiers, sha256 ab90e73b0c824544150f450819a38c7db76dd1cac505942fd66b5375f96591b4), fabriquée
# depuis le commit lui-même, sur le dépôt lu seulement (c'est aussi l'arbre à copier sur le serveur) :
#   D=$(mktemp -d) ; git -C /home/user/controle-ia-travail archive --format=tar d7f949acd9ac92e998e57663d2cc741de93f18c3 \
#     | tar -x -C "$D" ; (cd "$D" && LC_ALL=C find . -type f ! -path ./COMMIT-DE-LA-COPIE.txt \
#     ! -path ./EMPREINTES-DE-LA-COPIE.txt -print0 | LC_ALL=C sort -z | xargs -0 sha256sum) > EMPREINTES-DE-REFERENCE-d7f949ac.txt
#   puis, dans "$D" : copie à l'octet de la liste sous le nom EMPREINTES-DE-LA-COPIE.txt, et
#   echo d7f949acd9ac92e998e57663d2cc741de93f18c3 > COMMIT-DE-LA-COPIE.txt
#   (écrit en script : fabriquer-liste-reference-v4.sh, à côté de ce lanceur).
# Porte la commande du complément 1 v3 (sha256 de l'extraction v2 : 56ed20f89c3b9d9237350aeda092c815b6faee54b9048ba948659328d75bb867),
# à l'octet, aux trois chemins près : racine ("$RACINE"), interpréteur ("$INTERPRETE"), dossier des sorties ("$SORTIES")
# (vérifié par verifier-commande-v3.py).
#
# Emploi :  lancer-essai-3-v4.sh DOSSIER_DE_TENUE RACINE INTERPRETE SORTIES
# Contrôle seul, sans départ (sur le serveur avant le départ, dans un dossier de tenue À PART, ou en essai) :
#           lancer-essai-3-v4.sh DOSSIER_DE_TENUE RACINE INTERPRETE SORTIES --verifier-seulement [TETE EMPREINTE [REFERENCE]]
#           (TETE, EMPREINTE et REFERENCE remplacent les valeurs attendues, pour les essais sur racine factice ; la commande
#            n'est JAMAIS exécutée dans ce mode ; code 0 écrit si le départ serait permis)
# RACINE, INTERPRETE et SORTIES : chemins absolus.
#
# Deux formes de racine :
#   - avec .git (dépôt) : tête lue par git rev-parse, fichiers suivis non modifiés (git status, sans écrire l'index), comme en v2 ;
#   - sans .git (copie de l'arbre du commit, sur le serveur), dans cet ordre :
#     RACINE/COMMIT-DE-LA-COPIE.txt, fichier régulier, une ligne, exactement la tête attendue (sinon 11) ;
#     aucune entrée de la copie autre que dossier ou fichier régulier — lien symbolique, tube, prise, périphérique — et la
#     racine n'est pas elle-même un lien (sinon 12) ;
#     RACINE/EMPREINTES-DE-LA-COPIE.txt, fichier régulier, d'empreinte égale à REFERENCE_ATTENDUE (sinon 12) ;
#     la liste refaite sur la copie par la recette ci-dessus (LC_ALL=C find … | sort -z | xargs -0 sha256sum), écrite dans
#     DOSSIER_DE_TENUE/empreintes-recalculees-de-la-copie.txt, d'empreinte égale à REFERENCE_ATTENDUE (sinon 12 : fichier
#     ajouté, manquant ou modifié ; les lignes qui diffèrent sont écrites au journal).
#
# Refus de départ (code écrit dans code-de-sortie.txt, rien n'est lancé) :
#   10 dossier des sorties déjà présent ;
#   11 tête de la racine différente ou illisible (avec .git) ; sans .git : COMMIT-DE-LA-COPIE.txt absent, illisible ou autre ;
#      racine absente ;
#   12 fichiers suivis de la racine modifiés ou état illisible (avec .git) ; sans .git : lien ou fichier spécial, liste absente
#      ou autre que la référence, copie autre que la référence ;
#   13 empreinte du programme différente ou illisible ;
#   14 interpréteur absent, non régulier ou non exécutable.
# Autres codes : 2 usage (ou chemin non absolu) ; 3 dossier de tenue absent ; 4 code-de-sortie.txt ou
# empreintes-recalculees-de-la-copie.txt déjà présent (rien n'est écrasé, rien n'est lancé). En emploi, le code écrit est celui
# de la commande (143 = arrêt par signal de fin, reçu aussi par le programme).
set -u

usage() {
  echo "usage : $0 DOSSIER_DE_TENUE RACINE INTERPRETE SORTIES [--verifier-seulement [TETE EMPREINTE [REFERENCE]]]" >&2
  exit 2
}
if [ $# -ne 4 ] && [ $# -ne 5 ] && [ $# -ne 7 ] && [ $# -ne 8 ]; then
  usage
fi
TENUE=$1
RACINE=$2
INTERPRETE=$3
SORTIES=$4
TETE_ATTENDUE=d7f949acd9ac92e998e57663d2cc741de93f18c3
EMPREINTE_ATTENDUE=1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14
REFERENCE_ATTENDUE=ab90e73b0c824544150f450819a38c7db76dd1cac505942fd66b5375f96591b4
MODE=emploi
if [ $# -ge 5 ]; then
  if [ "$5" != "--verifier-seulement" ]; then
    usage
  fi
  MODE=verification
  if [ $# -ge 7 ]; then
    TETE_ATTENDUE=$6
    EMPREINTE_ATTENDUE=$7
  fi
  if [ $# -eq 8 ]; then
    REFERENCE_ATTENDUE=$8
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
F_RECALCUL="$TENUE/empreintes-recalculees-de-la-copie.txt"
if [ -e "$F_RECALCUL" ] || [ -L "$F_RECALCUL" ]; then
  echo "refus : $F_RECALCUL déjà présent (rien n'est écrasé) : aucun départ" >&2
  exit 4
fi

refuser() {
  echo "refus de départ ($(date -u +%Y-%m-%dT%H:%M:%SZ)) : $2" >&2
  echo "$1" > "$FICHIER_CODE"
  exit "$1"
}

echo "lanceur essai 3 v4 : mode $MODE, départ demandé à $(date -u +%Y-%m-%dT%H:%M:%SZ) ; racine $RACINE ; interpréteur $INTERPRETE ; sorties $SORTIES" >&2

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
  # 3'. v4 : ni lien symbolique ni fichier spécial dans la copie ; la racine n'est pas un lien
  if [ -L "$RACINE" ]; then
    refuser 12 "la racine est un lien symbolique : $RACINE"
  fi
  SPECIAUX=$(cd "$RACINE" && find . ! -type f ! -type d -printf '%y %p\n' 2>&1)
  if [ $? -ne 0 ] || [ -n "$SPECIAUX" ]; then
    refuser 12 "liens symboliques ou fichiers spéciaux dans la copie (ou parcours illisible) : $(printf '%s' "$SPECIAUX" | head -c 2000)"
  fi
  # 3''. v4 : liste de la copie égale à l'octet à la liste de référence ancrée au commit
  if [ ! -f "$F_EMPREINTES" ] || [ -L "$F_EMPREINTES" ]; then
    refuser 12 "liste des empreintes de la copie absente (ou non régulière) : $F_EMPREINTES"
  fi
  LISTE_LUE=$(sha256sum "$F_EMPREINTES" 2>&1)
  if [ $? -ne 0 ] || [ "${LISTE_LUE%% *}" != "$REFERENCE_ATTENDUE" ]; then
    refuser 12 "liste des empreintes de la copie : sha256 « ${LISTE_LUE%% *} », attendue la référence $REFERENCE_ATTENDUE"
  fi
  # 3'''. v4 : liste refaite sur la copie, par la même recette, égale à la référence (fichier ajouté, manquant ou modifié)
  (cd "$RACINE" && set -o pipefail && LC_ALL=C find . -type f ! -path ./COMMIT-DE-LA-COPIE.txt \
    ! -path ./EMPREINTES-DE-LA-COPIE.txt -print0 | LC_ALL=C sort -z | xargs -0 -r sha256sum) > "$F_RECALCUL" 2>&1
  CODE_RECALCUL=$?
  RECALCUL_LU=$(sha256sum "$F_RECALCUL" 2>&1)
  if [ "$CODE_RECALCUL" -ne 0 ] || [ "${RECALCUL_LU%% *}" != "$REFERENCE_ATTENDUE" ]; then
    refuser 12 "copie autre que la référence (code du recalcul $CODE_RECALCUL ; sha256 de la liste refaite « ${RECALCUL_LU%% *} », attendue $REFERENCE_ATTENDUE) ; lignes qui diffèrent (< liste de la copie, > liste refaite) : $(diff "$F_EMPREINTES" "$F_RECALCUL" | grep -E '^[<>]' | head -n 20)"
  fi
  echo "copie : commit $COMMIT_LU ; liste égale à la référence $REFERENCE_ATTENDUE ; $(wc -l < "$F_RECALCUL") fichiers refaits, égaux" >&2
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
