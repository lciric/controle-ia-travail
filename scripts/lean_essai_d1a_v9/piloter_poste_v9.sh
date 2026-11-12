#!/usr/bin/env bash
# piloter_poste_v9.sh — essai Lean, D-1a, réparation R-2439 (troisième essai). Copie de piloter_poste_v8.sh (inchangé, R12) ;
# cause du second essai (R-2438) : le vérificateur du noyau v4 ne compilait pas sous Lean 4.35.0, vu seulement après la
# coupure. Changements, et eux seuls :
#   - phase « avant » : copie aussi src/controle_ia/lean_essai/verificateur_noyau_v5.lean et
#     scripts/lean_essai_d1a_v9/essai_compilation_verificateur_v1.sh, puis, après l'essai « bac lit Mathlib.olean » et
#     **avant la coupure**, joue l'essai R5 « le vérificateur compile sur la machine » (cas sain : compile sans message ;
#     artefact : copie cassée refusée) ; non conforme : arrêt (set -e), avant la coupure et avant toute suite ; l'essai
#     « bac lit Mathlib.olean » reste dans scripts/lean_essai_d1a_v8/ (variable V8) ;
#   - phase « apres » : exécuteur, épreuve et vérificateur v5 (executeur_bac_v5.py, epreuve_isolement_v5.py,
#     verificateur_noyau_v5.lean) au lieu des v4 ; puis contrôle (cmp) que le vérificateur copié sous /opt/harnais/noyau est
#     octet pour octet celui compilé avant la coupure ; différent : arrêt avant l'épinglage.
# Les noms des sorties (`*-v6.*`) sont gardés. L'ordre fait foi dans
# docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/procedure-poste-local-d1a-v10.md.
# Texte de la v8 :
# piloter_poste_v8.sh — essai Lean, D-1a, harnais v7, second tour (R-2415, liste de Lazar). Remplace piloter_poste_v7.sh
# (premier tour, commit 65167979, scellé, inchangé, R12). Corps de piloter_poste_v6.sh (inchangé) ; changements tirés du
# rapport du premier essai (rapport-poste-local-d1a-v1.md) et de la liste de Lazar :
#   - la phase « avant » copie et lance scripts/lean_essai_d1a_v2/installer_chaine_v2.sh au lieu de installer_chaine_v1.sh
#     (lecture des fichiers compilés de Mathlib par `bac`, et garde de lisibilité) ;
#   - `scp` reçoit aussi `StrictHostKeyChecking=accept-new` : sur un poste qui n'a jamais vu le serveur, la première copie
#     (qui précède tout `ssh`) n'échoue plus par « Host key verification failed » ;
#   - après la coupure et avant la sonde, le cache du résolveur du serveur est vidé (`resolvectl flush-caches`) : la sonde
#     « après » ne lit plus une réponse mise en cache par la sonde « avant » (faux « ouverte », essai 1 du pilote « après »).
#     Cela ne fait que durcir la sonde ; si la commande manque ou échoue, le pilote s'arrête (set -e).
#   - `~/.ssh` est créé (700) s'il manque (WSL neuf au premier essai) ;
#   - les sondes du pilote sont `sonde_reseau_v2.py` (nom aléatoire jamais demandé pour le résolveur système) ; l'exécuteur du
#     bac garde `sonde_reseau_v1.py` dans /opt/harnais (il l'importe), protégé par le vidage du cache ;
#   - fin de la phase « avant » : essai R5 « bac lit Mathlib.olean » (essai_lecture_bac_v1.sh : cas sain, témoin 0644,
#     artefact 0600), avant la coupure ; non conforme : arrêt.
# Les noms des sorties (`*-v6.*`) sont gardés.
# L'ordre fait foi dans docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/procedure-poste-local-d1a-v8.md.
# Texte de la v6 :
# piloter_poste_v6.sh — essai Lean, D-1a, v6 (contre-lecture machine de la v5 897b7438…, R-2333). **Non éprouvé** (aucune
# machine joignable depuis la session cloud). Lancé par la session locale, sur l'ordinateur de Lazar (macOS ou Linux), depuis
# la racine du clone, **hors du bac à sable de Claude Code** et **en arrière-plan**, sorties dans des fichiers (CLC5-05, note 9).
# Le serveur ne reçoit ni le jeton de Hetzner ni aucune clé de modèle. Corps de la v5, plus des bornes (note 8) :
#   - chaque commande SSH s'exécute sous `timeout` **côté serveur** (coreutils d'Ubuntu ; rien à installer sur le poste) ;
#   - `ConnectTimeout` et `ServerAlive*` bornent une connexion qui pend (SSH et scp).
# IP est l'adresse du **serveur** loué (`minuterie_v6 adresse-serveur --identifiant N`), jamais celle du poste ; SORTIES est un
# dossier du poste hors du dépôt ; rien n'est versé sans `minuterie_v6 garde-poste` (CLC5-07). L'ordre fait foi dans
# docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/procedure-poste-local-d1a-v6.md.
set -euo pipefail
PHASE=${1:?phase}; IP=${2:?adresse du serveur}; CLE=${3:?clé ssh jetable}
O=(-o BatchMode=yes -o ConnectTimeout=30 -o ServerAliveInterval=30 -o ServerAliveCountMax=4)
S=(ssh -i "$CLE" -o StrictHostKeyChecking=accept-new "${O[@]}" "root@$IP")
C=(scp -i "$CLE" -o StrictHostKeyChecking=accept-new "${O[@]}")
ICI=$(cd "$(dirname "$0")" && pwd)
[ -d "$HOME/.ssh" ] || install -d -m 700 "$HOME/.ssh"
V1="$ICI/../lean_essai_d1a_v1"
V2="$ICI/../lean_essai_d1a_v2"
V4="$ICI/../lean_essai_d1a_v4"
V8="$ICI/../lean_essai_d1a_v8"
PAQ="$ICI/../../src/controle_ia/lean_essai"
if [ "$PHASE" = avant ]; then
  COMMIT=${4:?commit de Mathlib}
  "${C[@]}" "$V2/installer_chaine_v2.sh" "$V1/couper_reseau_v1.sh" "$PAQ/sonde_reseau_v2.py" "$V8/essai_lecture_bac_v1.sh" \
      "$ICI/essai_compilation_verificateur_v1.sh" "$PAQ/verificateur_noyau_v5.lean" \
      "root@$IP:/root/"
  "${S[@]}" timeout 5400 bash /root/installer_chaine_v2.sh "$COMMIT"
  "${S[@]}" timeout 300 python3 -B /root/sonde_reseau_v2.py --attendu ouverte
  "${S[@]}" timeout 120 bash /root/essai_lecture_bac_v1.sh
  "${S[@]}" timeout 900 bash /root/essai_compilation_verificateur_v1.sh /root/verificateur_noyau_v5.lean
elif [ "$PHASE" = apres ]; then
  SORTIES=${4:?dossier local des sorties, hors du dépôt}
  mkdir -p "$SORTIES"
  "${S[@]}" timeout 300 bash /root/couper_reseau_v1.sh > "$SORTIES/coupure-v6.txt"
  "${S[@]}" timeout 60 resolvectl flush-caches
  "${S[@]}" timeout 300 python3 -B /root/sonde_reseau_v2.py --attendu fermee > "$SORTIES/sonde-apres-coupure-v6.json"
  "${S[@]}" timeout 60 install -d -m 0755 /opt/harnais/artefacts_r5_v4 /opt/harnais/noyau
  "${C[@]}" "$PAQ/gardes_lean_v4.py" "$PAQ/executeur_bac_v5.py" "$PAQ/epreuve_isolement_v5.py" "$PAQ/sonde_reseau_v1.py" \
      "root@$IP:/opt/harnais/"
  "${C[@]}" "$PAQ/verificateur_noyau_v5.lean" "root@$IP:/opt/harnais/noyau/"
  "${C[@]}" "$V4"/artefacts_r5_v4/* "root@$IP:/opt/harnais/artefacts_r5_v4/"
  "${S[@]}" timeout 60 cmp /root/verificateur_noyau_v5.lean /opt/harnais/noyau/verificateur_noyau_v5.lean
  "${S[@]}" timeout 1800 python3 -B /opt/harnais/epreuve_isolement_v5.py epingler-verificateur > "$SORTIES/verificateur-epingle-v6.json"
  "${S[@]}" timeout 3600 python3 -B /opt/harnais/epreuve_isolement_v5.py noyau > "$SORTIES/premier-pas-noyau-v6.json"   # set -e : arrêt si non conforme
  rc=0; "${S[@]}" timeout 7200 python3 -B /opt/harnais/epreuve_isolement_v5.py epreuve > "$SORTIES/epreuve-isolement-v6.json" || rc=$?
  echo "code de sortie de l'épreuve : $rc (0 = conforme ; 124 = borne de temps atteinte)" > "$SORTIES/epreuve-code-v6.txt"
  "${S[@]}" timeout 3600 python3 -B /opt/harnais/epreuve_isolement_v5.py mesurer > "$SORTIES/mesures-v6.json"
  "${S[@]}" timeout 300 python3 -B /root/sonde_reseau_v2.py --attendu fermee > "$SORTIES/sonde-fin-v6.json"
  "${S[@]}" timeout 60 cat /opt/harnais/journal-installation-v1.txt /opt/harnais/chaine-v1.json > "$SORTIES/installation-v6.txt"
  echo "fin de la phase « apres » : la session locale détruit la machine maintenant (minuterie_v6 detruire --identifiant N)"
else
  echo "phase inconnue : $PHASE" >&2; exit 2
fi
