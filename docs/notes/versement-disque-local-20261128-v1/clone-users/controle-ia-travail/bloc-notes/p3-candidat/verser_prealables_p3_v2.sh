#!/usr/bin/env bash
# Versement des préalables de la chaîne de P3, v2 (R-227) : journal de la répétition jouet (candidat 4), épingles des
# contrôles dans le bloc-notes réel (brouillon 4), copies versées des treize scripts sous docs/procedures/P3-premier-test-v2/,
# chacune avec son sceau. Aucun commit ici : la session relit, puis committe.
# Usage : verser_prealables_p3.sh JOURNAL_REPETITION
set -euo pipefail
J=$(realpath "${1:?journal de la répétition jouet}")
D=${D_ESSAI:-/home/user/controle-ia-travail}            # D_ESSAI, H_ESSAI : essai sur des copies
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
H=${H_ESSAI:-$BN/p3-v1}
B=$D/brouillons/P3-chaine-v1-brouillon4
V=docs/procedures/P3-premier-test-v2
OUTILS=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3-candidat
CODE=7a54d431d89745839220f882b41b13e8c62ecfdd
CAND=brouillons/P3-premier-test-i-a-v1-candidat4.md; CAND_SHA=d975e9817e88d30196930c2a351927c2091f2ac024d2a5b52556730fa36cb672
CFG=brouillons/P3-premier-test-config-v1-candidat3.json; CFG_SHA=702303e9453f7c4ce8f0cf900f45fc8075b75744eedab0b1652dd8e52d55abde
CONS=brouillons/P3-consignes-v1-candidat2.md; CONS_SHA=a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c
cd "$D"
for paire in "$CAND $CAND_SHA" "$CFG $CFG_SHA" "$CONS $CONS_SHA"; do
    set -- $paire
    [ "$(sha256sum "$1" | cut -d' ' -f1)" = "$2" ] || { echo "empreinte inattendue : $1"; exit 2; }
    PYTHONPATH=src python3 -m controle_ia.scellement verifier "$1" > /dev/null
done
RAPPORTS=""
for f in $(ls prereg/contre-lectures/P3-premier-test-v1-*-v1.md); do
    PYTHONPATH=src python3 -m controle_ia.scellement verifier "$f" > /dev/null
    RAPPORTS="$RAPPORTS $(basename "$f")=$(sha256sum "$f" | cut -d' ' -f1)"
done
RAPPORTS=${RAPPORTS# }
[ "$(echo "$RAPPORTS" | wc -w)" -eq 5 ] || { echo "cinq rapports attendus : $RAPPORTS"; exit 2; }
# bloc-notes réel : égal au brouillon 4 avant les épingles
for s in $(cd "$B" && ls *.sh *.py); do cmp -s "$B/$s" "$H/$s" || { echo "bloc-notes ≠ brouillon 4 avant épingles : $s"; exit 2; }; done
[ "$(ls "$H" | wc -l)" -eq 13 ] || { echo "bloc-notes : treize scripts attendus"; exit 2; }
# journal de la répétition jouet : conforme au module commun, au code relu, au candidat 3 et aux consignes relues
mkdir -p "$V"
[ -e "$V/repetition-jouet-p3-v1.log" ] && { echo "$V/repetition-jouet-p3-v1.log existe déjà (R12)"; exit 2; }
cp "$J" "$V/repetition-jouet-p3-v1.log"
python3 -I "$H/verifications_p3_v1.py" repetition "$CODE" "$V/repetition-jouet-p3-v1.log" "$(basename "$CAND")" "$CAND_SHA" \
    "$(basename "$CONS")" "$CONS_SHA"
REP=$(sha256sum "$V/repetition-jouet-p3-v1.log" | cut -d' ' -f1)
# épingles (le chemin du candidat relu est écrit dans le brouillon 4)
CTL=$H/controles_avant_depense_p3_v1.sh
[ "$(grep -c '^CANDIDAT_RELU_CHEMIN=brouillons/P3-premier-test-i-a-v1-candidat4.md$' "$CTL")" -eq 1 ] || { echo "chemin du candidat 4 absent des contrôles"; exit 2; }
python3 -I "$OUTILS/epingler_controles.py" "$CTL" "CANDIDAT_RELU=$CAND_SHA" "CONFIG_RELUE=$CFG_SHA" "CONSIGNES_RELUES=$CONS_SHA" \
    "CODE_RELU=$CODE" "REPETITION_JOUET=$REP" "RAPPORTS_ATTENDUS=$RAPPORTS"
n=$(diff "$B/controles_avant_depense_p3_v1.sh" "$CTL" | grep -c '^>' || true)
[ "$n" -eq 6 ] || { echo "contrôles : $n lignes changées (6 attendues)"; exit 2; }
bash -n "$CTL"
for s in $(cd "$B" && ls *.sh *.py); do
    [ "$s" = controles_avant_depense_p3_v1.sh ] && continue
    cmp -s "$B/$s" "$H/$s" || { echo "bloc-notes ≠ brouillon 4 : $s"; exit 2; }
done
# copies versées des treize scripts, chacune avec son sceau ; sceau du journal
for s in $(cd "$H" && ls); do
    [ -e "$V/$s" ] && { echo "$V/$s existe déjà (R12)"; exit 2; }
    cp -p "$H/$s" "$V/$s"
done
PYTHONPATH=src python3 -m controle_ia.scellement sceller "$V"/*.sh "$V"/*.py "$V/repetition-jouet-p3-v1.log" > /dev/null
for s in $(cd "$H" && ls); do cmp -s "$H/$s" "$V/$s" || { echo "copie versée ≠ bloc-notes : $s"; exit 2; }; done
echo "journal de la répétition : $REP"
echo "rapports épinglés : $RAPPORTS"
echo "lignes changées dans les contrôles : $n"
diff "$B/controles_avant_depense_p3_v1.sh" "$CTL" | grep '^>' | cut -c1-140 || true
echo "VERSEMENT DES PRÉALABLES PRÊT (non committé)"
