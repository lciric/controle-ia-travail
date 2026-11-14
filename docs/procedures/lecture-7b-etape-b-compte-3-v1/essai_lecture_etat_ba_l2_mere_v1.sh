#!/usr/bin/env bash
# Essai (règle R5) de lecture_etat_ba_l2_mere_v1.py sur des fichiers jouets (aucune donnée du programme).
#     bash essai_lecture_etat_ba_l2_mere_v1.sh <dépôt> <bac neuf>
set -u
DEPOT=$(cd "$1" && pwd); BAC="$2"
[ ! -e "$BAC" ] || { echo "ARRÊT : $BAC existe déjà"; exit 1; }
mkdir -p "$BAC"; BAC=$(cd "$BAC" && pwd)
L="$DEPOT/docs/procedures/lecture-7b-etape-b-compte-3-v1/lecture_etat_ba_l2_mere_v1.py"
export LC_ALL=C.UTF-8
date -u +"début de l'essai : %Y-%m-%dT%H:%M:%SZ"; echo "script essayé : $(sha256sum "$L" | cut -d' ' -f1)"
OK=0; KO=0; RMC=20261117-000000-t06-mots-et-cout
cas() { local nom="$1" attendu="$2" motif="$3" interdit="$4"; shift 4; local s c; s=$(python3 -I -B "$L" "$@" 2>&1); c=$?
  if [ "$c" = "$attendu" ] && printf '%s' "$s" | grep -qF -- "$motif" && ! printf '%s' "$s" | grep -qF -- "$interdit"; then OK=$((OK+1)); echo "conforme : $nom (code $c)";
  else KO=$((KO+1)); echo "ÉCART : $nom (code $c, attendu $attendu)"; printf '%s\n' "$s" | sed 's/^/    /'; fi; }
racine() {   # $1 nom ; $2 contenu JSON ; $3 date de la ligne ; $4 « issue » pour ajouter ISSUE-MOTS-ET-COUT-T06 ; $5 « sans-ligne »
    local R="$BAC/$1"; mkdir -p "$R/diag/$RMC" "$R/registres"; printf '%s' "$2" > "$R/diag/$RMC/base-a-t08.json"
    (cd "$R/diag/$RMC" && sha256sum base-a-t08.json > base-a-t08.json.sha256); local h; h=$(sha256sum "$R/diag/$RMC/base-a-t08.json" | cut -d' ' -f1)
    { echo "# registre jouet"; echo
      [ "${5:-}" = sans-ligne ] || echo "| LECTURE-T08-BASE-A | $3 | diag/$RMC/base-a-t08.json | $h |"
      [ "${4:-}" = issue ] && echo "| ISSUE-MOTS-ET-COUT-T06 | 2026-11-17T09:00:01Z | diag/$RMC/issue-mots-et-cout-t06.json | $(printf '1%.0s' $(seq 64)) |"; } > "$R/registres/scellements-v1.md"
    echo "$R"; }
J='{"aires": {"secret": 0.7777}, "lignes": {"BA-L1": {"s_applique": false}, "BA-L2": {"s_applique": false, "phrase": "PHRASE-SECRETE"}}}'
R=$(racine s1 "$J" 2026-11-17T09:00:00Z issue); cas "S1 BA-L2 ne s'applique pas" 0 "ÉTAT BA-L2 : ne s'applique pas" "0.7777" --racine "$R" --registre "$R/registres/scellements-v1.md" --instant 2026-11-18T00:00:00Z
R=$(racine s2 "${J/\"s_applique\": false, \"phrase\"/\"s_applique\": true, \"phrase\"}" 2026-11-17T09:00:00Z issue)
cas "S2 BA-L2 s'applique : mot de Lazar" 3 "s'applique — l'étape B attend le mot de Lazar" "PHRASE-SECRETE" --racine "$R" --registre "$R/registres/scellements-v1.md" --instant 2026-11-18T00:00:00Z
R=$(racine a1 '{"lignes": {"BA-L1": {"s_applique": false}}}' 2026-11-17T09:00:00Z issue); cas "A1 champ BA-L2 absent" 2 "absent" "s_applique\": false" --racine "$R" --registre "$R/registres/scellements-v1.md" --instant 2026-11-18T00:00:00Z
R=$(racine a2 '{"lignes": {"BA-L2": {"s_applique": "0.83"}}}' 2026-11-17T09:00:00Z issue); cas "A2 valeur non booléenne (jamais affichée)" 2 "booléen attendu (valeur non affichée)" "0.83" --racine "$R" --registre "$R/registres/scellements-v1.md" --instant 2026-11-18T00:00:00Z
R=$(racine a3 "$J" 2026-11-17T09:00:00Z issue); echo ' ' >> "$R/diag/$RMC/base-a-t08.json"; cas "A3 fichier altéré après sa ligne" 2 "empreinte" "0.7777" --racine "$R" --registre "$R/registres/scellements-v1.md" --instant 2026-11-18T00:00:00Z
R=$(racine a4 "$J" 2026-11-17T09:00:00Z issue); rm "$R/diag/$RMC/base-a-t08.json.sha256"; cas "A4 compagnon absent" 2 "compagnon (absent" "0.7777" --racine "$R" --registre "$R/registres/scellements-v1.md" --instant 2026-11-18T00:00:00Z
R=$(racine a5 "$J" 2026-11-17T09:00:00Z issue sans-ligne); cas "A5 ligne absente alors qu'ISSUE est inscrite : mot de Lazar" 2 "l'étape B attend le mot de Lazar" "0.7777" --racine "$R" --registre "$R/registres/scellements-v1.md" --instant 2026-11-18T00:00:00Z
R=$(racine a6 "$J" 2026-11-17T09:00:00Z issue); cas "A6 instant avant la ligne" 2 "pas strictement antérieure" "0.7777" --racine "$R" --registre "$R/registres/scellements-v1.md" --instant 2026-11-18T00:00:00Z --instant 2026-11-17T08:00:00Z
R=$(racine a7 "$J" 2026-11-17T09:00:00Z issue); grep '^| LECTURE' "$R/registres/scellements-v1.md" > "$BAC/l7"; cat "$BAC/l7" >> "$R/registres/scellements-v1.md"; cas "A7 ligne en double" 2 "2 ligne(s)" "0.7777" --racine "$R" --registre "$R/registres/scellements-v1.md" --instant 2026-11-18T00:00:00Z
R=$(racine a8 "$J" 2026-11-17T09:00:00Z issue); rm "$R/diag/$RMC/base-a-t08.json"; cas "A8 fichier absent" 2 "absent sous la racine" "0.7777" --racine "$R" --registre "$R/registres/scellements-v1.md" --instant 2026-11-18T00:00:00Z
echo "BILAN : $OK conformes sur $((OK + KO))"; [ "$KO" = 0 ] && echo "ESSAI : TOUT CONFORME" || echo "ESSAI : ÉCARTS"
date -u +"fin de l'essai : %Y-%m-%dT%H:%M:%SZ"
