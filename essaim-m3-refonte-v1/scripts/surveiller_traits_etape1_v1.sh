#!/usr/bin/env bash
# Surveillance de l'instance de l'extraction des traits de l'étape 1 (GO-2026-10-24-05), session « session-depot » ;
# déclinée de `docs/procedures/P3-premier-test-v2/surveiller_p3_v1.sh` (main) sous un nom nouveau (R12). Toutes les
# 60 s : état de l'instance (champs filtrés : jamais la réponse brute, qui porte l'environnement de l'instance) et
# dernières lignes « AMORCE » / « TRAITS » du journal du conteneur. Arrêt de l'instance par son identifiant (R10) dès la
# fin de l'amorce, dès que le conteneur est sorti, ou au plafond (création + DUREE_MAX_S), consigné ; jamais de
# destruction ici (elle suit la vérification des résultats poussés).
# Usage : VASTAI=<chemin de vastai 1.8.3> surveiller_traits_etape1_v1.sh ID CREATION DOSSIER_NEUF
# Codes : 0 arrêt après la fin de l'amorce ; 5 arrêt au plafond ou conteneur sorti sans ligne de fin ; 6 arrêt non relu.
set -uo pipefail
[ $# -eq 3 ] || { echo "usage : surveiller_traits_etape1_v1.sh ID CREATION DOSSIER_NEUF"; exit 2; }
ID=$1; CREATION=$2; D=$(realpath -m "$3")
V=${VASTAI:?VASTAI : chemin de l outil vastai 1.8.3}
DUREE_MAX_S=7200
[[ "$ID" =~ ^[0-9]{6,10}$ ]] && [[ "$CREATION" =~ ^[0-9]{10}$ ]] || { echo "ID ou CREATION illisible"; exit 2; }
[ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
mkdir -p "$D"
etat() {
    "$V" show instance "$ID" --raw 2>/dev/null | python3 -I -B -c '
import json, sys
try:
    i = json.load(sys.stdin)
    assert isinstance(i, dict)
except Exception:
    print("illisible"); sys.exit(0)
msg = str(i.get("status_msg") or "").replace("\n", " ")[:100]
print(i.get("actual_status"), i.get("cur_state"), i.get("dph_total"), msg)'
}
motif=""
while :; do
    maintenant=$(date -u +%s)
    e=$(etat)
    printf '%s %s\n' "$(date -u +%FT%TZ)" "$e" >> "$D/etats.txt"
    "$V" logs "$ID" --tail 40 2>/dev/null | grep -E '^(AMORCE|TRAITS) ' > "$D/journal-instance.txt.nouveau" || true
    [ -s "$D/journal-instance.txt.nouveau" ] && mv "$D/journal-instance.txt.nouveau" "$D/journal-instance.txt"
    rm -f "$D/journal-instance.txt.nouveau"
    if [ -s "$D/journal-instance.txt" ] && grep -q '^AMORCE .* fin, code' "$D/journal-instance.txt"; then motif="fin de l'amorce"; break; fi
    case "$e" in exited*|stopped*) motif="conteneur sorti"; break ;; esac
    if [ $((maintenant - CREATION)) -ge "$DUREE_MAX_S" ]; then motif="plafond de durée ($DUREE_MAX_S s)"; break; fi
    sleep 60
done
echo "$(date -u +%FT%TZ) : arrêt demandé, motif : $motif" | tee -a "$D/arret.txt"
"$V" stop instance "$ID" >> "$D/arret.txt" 2>&1
sleep 20
e=$(etat)
echo "$(date -u +%FT%TZ) : état relu : $e" | tee -a "$D/arret.txt"
case "$e" in
    *stopped*|*exited*) ;;
    *) echo "arrêt non relu : vérifier l'instance $ID (champs filtrés)"; exit 6 ;;
esac
[ "$motif" = "fin de l'amorce" ] && exit 0
exit 5
