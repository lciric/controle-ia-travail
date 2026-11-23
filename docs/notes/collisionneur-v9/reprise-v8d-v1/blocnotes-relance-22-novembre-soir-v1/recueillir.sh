#!/bin/bash
# recueillir.sh PAGE DOSSIER CELLULE SESSION BRANCHE
cd /home/user/controle-ia-travail
F=$1 D=$2 CID=$3 S=$4 BR=$5
PE=docs/notes/collisionneur-v9/abonnement-v1/pages-evenements-v1
cp $F $PE/ && (cd $PE && sha256sum $(basename $F) > $(basename $F).sha256)
git fetch -q origin $BR; C=$(git rev-parse FETCH_HEAD)
L=$(wc -l < $D/abonnement/kits/$CID/texte-servi.md)
PYTHONPATH=src .venv/bin/python -B docs/notes/collisionneur-v9/abonnement-v1/recueil_session_v6.py $PE/$(basename $F) $D $CID $S --lecture-permise texte-servi.md --consigne-systeme "Le seul outil permis est Read, sur le fichier texte-servi.md à la racine, lu en entier ; aucun autre outil, aucune recherche ; puis réponds en un seul message." --lignes $L --commit-branche $C --premier-tour 2>&1 | tail -4
