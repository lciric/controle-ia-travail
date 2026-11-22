#!/usr/bin/env bash
# Lancement réel de la passe X, lot 11 v4 (feu de la mère, GO-2026-11-22-46, -48, -54 ; forme de la réponse 36).
# Lance le versement de la quarantaine en arrière-plan, puis l'exécutant ; à la fin, pose le fichier d'arrêt et attend
# le dernier versement. N'affiche aucun texte de réponse ni aucune clé.
set -u
R=/home/user/controle-ia-travail
N=$R/docs/notes/ideation-nouvelles-attaques-v1
S=/tmp/claude-0/-home-user-controle-ia-travail/e2c3ce0b-40f3-55d3-a6bf-333c05f6ccd1/scratchpad
A=$S/arbre-quarantaine-passe-x-v1
H=$(date -u +%Y%m%dT%H%M%SZ)
J=$N/lot-11-passe-x-v4/lancement/journal-passe-x-$H.jsonl
ARRET=$S/arret-versement-passe-x-$H
[ "$(git -C $A rev-parse --abbrev-ref HEAD)" = "prep/quarantaine-passe-x-reponses-v1" ] || { echo "REFUS : arbre de quarantaine"; exit 2; }
[ -e $A/flux ] && { echo "REFUS : flux déjà présent"; exit 2; }
python3 -B $N/lot-11-passe-x-v2/verser_quarantaine_v1.py --arbre $A --arret $ARRET > $S/versement-passe-x-$H.txt 2>&1 &
PV=$!
echo "versement : PID $PV ; journal : $J"
$R/.venv/bin/python -I $N/lot-11-passe-x-v4/passe_x_na_v4.py --textes $N/passe-x-textes-groupes-v1/textes \
  --configuration $N/lot-11-passe-x-v4/lancement/configuration-passe-x-groupes-v4.json \
  --plan-garde $N/lot-11-passe-x-v4/lancement/plan-garde-depart-passe-x-v3.json \
  --quarantaine $A/flux --journal $J --reel > $S/rapport-passe-x-$H.json 2> $S/erreurs-passe-x-$H.txt
CODE=$?
echo "exécutant : code $CODE"
touch $ARRET
wait $PV
echo "versement : code $? ; $(tail -1 $S/versement-passe-x-$H.txt)"
exit $CODE
