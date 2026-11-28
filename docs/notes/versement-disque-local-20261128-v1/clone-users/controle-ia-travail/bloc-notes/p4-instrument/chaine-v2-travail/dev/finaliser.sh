#!/usr/bin/env bash
# Outil de travail (non versé) : journaux de preuve copiés sous leurs noms dans la chaîne v2, scellés ; preuves et
# répétition contrôlées ; empreintes des scripts éprouvés comparées aux scripts de la chaîne v2 ; aucun __pycache__.
# Usage : finaliser.sh DOSSIER_DES_JOURNAUX SORTIE_NEUVE
#   DOSSIER_DES_JOURNAUX : banc-{lanceur,surveillance,arret,traces,verifications,controles,scellement}.log et
#   repetition-jouet.log (journaux bruts des passes) ; les noms finaux sont donnés par la table ci-dessous.
set -uo pipefail
J=$(realpath "$1"); O=$(realpath -m "$2")
H=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v2
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
export PYTHONDONTWRITEBYTECODE=1
[ -e "$O" ] && { echo "$O existe déjà (R12)"; exit 2; }
mkdir -p "$O" || exit 2
declare -A NOMS=([banc-lanceur]=banc-lanceur-p4-v1.log [banc-surveillance]=banc-surveillance-p4-v1.log
                 [banc-arret]=banc-arret-p4-v1.log [banc-traces]=banc-traces-p4-v1.log
                 [banc-verifications]=banc-verifications-p4-v1.log [banc-controles]=banc-controles-p4-v1.log
                 [banc-scellement]=banc-scellement-p4-v1.log [repetition-jouet]=repetition-jouet-p4-v1.log)
for k in "${!NOMS[@]}"; do
    s="$J/$k.log"; d="$H/${NOMS[$k]}"
    [ -f "$s" ] || { echo "journal $s absent"; exit 2; }
    [ -e "$d" ] && { echo "$d existe déjà (R12)"; exit 2; }
    cp "$s" "$d" && (cd "$H" && sha256sum "${NOMS[$k]}" > "${NOMS[$k]}.sha256") || exit 2
    echo "journal versé : ${NOMS[$k]} $(cut -d' ' -f1 "$d.sha256")"
done
"$PY" -B "$H/verifications_p4_v1.py" preuves "$H" banc-lanceur-p4-v1.log banc-surveillance-p4-v1.log banc-arret-p4-v1.log \
    banc-traces-p4-v1.log banc-verifications-p4-v1.log banc-controles-p4-v1.log banc-scellement-p4-v1.log > "$O/preuves.txt" 2>&1
echo "preuves : code $?" | tee "$O/preuves-code.txt"
C=$(sed -n 's/^commit du code répété : //p' "$H/repetition-jouet-p4-v1.log")
read -r NC SC < <(sed -n 's/^candidat répété : //p' "$H/repetition-jouet-p4-v1.log")
"$PY" -B "$H/verifications_p4_v1.py" repetition "$C" "$H/repetition-jouet-p4-v1.log" "$NC" "$SC" > "$O/repetition.txt" 2>&1
echo "repetition : code $? (commit $C ; candidat $NC $SC)" | tee "$O/repetition-code.txt"
# chaque empreinte citée (« script éprouvé », « script répété ») égale celle du script de la chaîne v2
ko=0
while read -r nom sha; do
    [ "$(sha256sum "$H/$nom" | cut -d' ' -f1)" = "$sha" ] && echo "égal : $nom $sha" || { echo "DIFFÉRENT : $nom $sha"; ko=1; }
done < <(cat "$H"/banc-*-p4-v1.log "$H/repetition-jouet-p4-v1.log" | sed -n 's/^script \(éprouvé\|répété\) : \([a-z0-9_]*_v1\.\(sh\|py\)\) \([0-9a-f]\{64\}\)$/\2 \4/p' | sort -u) > "$O/empreintes-citees.txt"
cat "$O/empreintes-citees.txt"
echo "empreintes citées = scripts de la chaîne v2 : $([ $ko = 0 ] && echo oui || echo NON)" | tee -a "$O/empreintes-citees.txt"
P=$(find "$H" /tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/module-v2 -name __pycache__ 2>/dev/null | head -3)
echo "__pycache__ : ${P:-aucun}" | tee "$O/pycache.txt"
