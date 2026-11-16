#!/usr/bin/env bash
# Essai R5 de l'attestation v3 sur la liste « qui a lu quoi » v3 versée (registres/qui-a-lu-quoi-v3.md) : cas sain et trois artefacts.
# usage : bash essai_attestation_v3_liste_v3_versee_v1.sh DOSSIER_NEUF   (lancé depuis le dossier du dépôt ; n'écrit que dans DOSSIER_NEUF)
set -u; export LC_ALL=C.UTF-8
W="$1"; [ ! -e "$W" ] || { echo "ARRÊT : $W existe"; exit 1; }; mkdir -p "$W"
A=docs/procedures/lecture-7b-etape-b-compte-3-v1/attestation_qui_a_lu_quoi_compte_3_v3.py; L=registres/qui-a-lu-quoi-v3.md
HOTE=session_016QhUrrSUMEzEqWPnQYxjHB
CH='analyse du verdict A ; étape B bis (conception et verdicts) ; T0.8 ; G0 ; préenregistrement NARCBench (rédaction, contre-lecture, course) ; brouillons des papiers B et C ; code de la pièce « mots et coût »'
date -u +%Y-%m-%dT%H:%M:%SZ; echo "attestation $(sha256sum $A | cut -d' ' -f1)"; echo "liste $(sha256sum $L | cut -d' ' -f1) ; compagnon $(cut -d' ' -f1 $L.sha256)"
H=$(sha256sum $L | cut -d' ' -f1)
echo "--- sain (liste versée, empreinte du compagnon, cellule de l'hôte)"; python3 -I -B $A $L $H $HOTE --admettre-hote "$CH"; echo "code $? (attendu 0)"
fab() { sed "$2" $L > "$W/$1.md"; h=$(sha256sum "$W/$1.md" | cut -d' ' -f1); echo "$h  $1.md" > "$W/$1.md.sha256"; echo "$h"; }
h=$(fab a1 's/code de la pièce « mots et coût » |$/code de la pièce « mots et coût » ; lecteur B |/')
echo "--- artefact 1 (cellule « exclu de » de l'hôte allongée)"; python3 -I -B $A "$W/a1.md" $h $HOTE --admettre-hote "$CH"; echo "code $? (attendu 2)"
h=$(fab a2 's/^| 186 | session non nommée/| 186 | session_016QhUrrSUMEx non nommée/')
echo "--- artefact 2 (douze premiers caractères de l'hôte dans une autre ligne)"; python3 -I -B $A "$W/a2.md" $h $HOTE --admettre-hote "$CH"; echo "code $? (attendu 2)"
echo "--- artefact 3 (empreinte attendue autre)"; python3 -I -B $A $L 0000000000000000000000000000000000000000000000000000000000000000 $HOTE --admettre-hote "$CH"; echo "code $? (attendu 2)"
h=$(fab a4 's/^\(| 186 |.*\)| aucune exclusion déclarée |$/\1| lecteur B |/')
echo "--- artefact 4 (ligne du compte 3 sans identifiant, avec exclusion)"; python3 -I -B $A "$W/a4.md" $h $HOTE --admettre-hote "$CH"; echo "code $? (attendu 2)"
date -u +%Y-%m-%dT%H:%M:%SZ
