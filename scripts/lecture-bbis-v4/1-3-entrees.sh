#!/bin/bash
# § 1.3 — entrées présentes, à l'empreinte des branches et des lignes de registre ; rien de la liste « Jamais »
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
# seulement, le bloc « § 1.3 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/1-3-entrees.sh
. "$(dirname "$0")/commun.sh"
R="$T/releve-entrees.txt"; neuf "$R"; neuf "$T/attendus.txt"; neuf "$T/presents.txt"; neuf "$T/attendus-noms.txt"
{
cd "$ARBRE" || exit 1
dire "== 1.3 entrées, $(date -u +%Y-%m-%dT%H:%M:%SZ)"
: > "$T/attendus.txt"
git ls-tree -r --name-only "$REF_SORTIES" -- "runs/$RUN_BBIS" "diag/$RUN_BBIS" "donnees/$RUN_BBIS" | while read -r p; do printf '%s\t%s\n' "$REF_SORTIES" "$p"; done >> "$T/attendus.txt"
egal "fichiers des sorties listés sur la branche" 20 "$(wc -l < "$T/attendus.txt" | tr -d ' ')"
for p in "runs/$RUN_7B/manifeste.json" "diag/$RUN_7B/episodes-t06.json" "diag/$RUN_7B/lecture-cout-t06.json" \
         "donnees/$RUN_7B/mesures-t06.npz" "donnees/$RUN_7B/textes-actions-t06.jsonl"; do
  printf '%s\t%s\n%s\t%s\n' "$REF_7B" "$p" "$REF_7B" "$p.sha256" >> "$T/attendus.txt"
done
p="diag/$RUN_MC/issue-mots-et-cout-t06.json"; printf '%s\t%s\n%s\t%s\n' "$REF_MC" "$p" "$REF_MC" "$p.sha256" >> "$T/attendus.txt"
egal "entrées attendues" 32 "$(wc -l < "$T/attendus.txt" | tr -d ' ')"
while IFS="$(printf '\t')" read -r ref p; do
  if [ ! -f "$p" ]; then dire "DEFAUT : $p absent de l'arbre de lecture"; FAUTES=$((FAUTES+1)); continue; fi
  egal "objet git de $p égal à celui de sa branche" "$(git rev-parse --verify -q "$ref:$p")" "$(git hash-object -- "$p")"
  case "$p" in *.sha256) ;; *) egal "compagnon de $p" "$(sha256sum "$p" | cut -d' ' -f1)" "$(cut -d' ' -f1 "$p.sha256" 2>/dev/null)" ;; esac
done < "$T/attendus.txt"
# rien d'autre dans les dossiers des entrées
find "runs/$RUN_7B" "diag/$RUN_7B" "donnees/$RUN_7B" "runs/$RUN_BBIS" "diag/$RUN_BBIS" "donnees/$RUN_BBIS" "diag/$RUN_MC" "runs/$RUN_MC" -type f 2>/dev/null | sort > "$T/presents.txt"
cut -f2 "$T/attendus.txt" | sort > "$T/attendus-noms.txt"
egal "fichiers en trop ou en moins dans les dossiers des entrées" 0 "$(comm -3 "$T/presents.txt" "$T/attendus-noms.txt" | wc -l | tr -d ' ')"
# liste « Jamais » et fichiers de l'étape B : par les noms
vrai "lecture-sondes-t06.json absent" test ! -e "diag/$RUN_7B/lecture-sondes-t06.json"
vrai "resume.json de la course de confirmation absent" test ! -e "diag/$RUN_7B/resume.json"
egal "fichiers nommés lecture-t07* ou arret-etape-b* dans l'arbre" 0 "$(find . -path ./.git -prune -o -type f \( -name 'lecture-t07*' -o -name 'arret-etape-b*' \) -print | wc -l | tr -d ' ')"
egal "fichiers du dossier de lecture de l'étape B autres que l'audit des fuites" 0 "$(find "diag/$RUN_B" -type f ! -name 'audit-fuites-t07.json*' 2>/dev/null | wc -l | tr -d ' ')"
# lignes des deux registres, à l'octet, une fois chacune
while IFS= read -r l; do egal "registre propre : une fois « $(printf '%s' "$l" | cut -c1-60)… »" 1 "$(grep -c -x -F -- "$l" "$PROPRE")"; done <<'EOF'
| SCELLEMENT-BBIS | 2026-11-14T12:30:30Z | prereg/T0.7-etape-B-bis-v1.md | 0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb |
| ABSENCE-B-BBIS | 2026-11-14T12:30:30Z | registres/t07-etape-b-bis/ABSENCE-B-BBIS-v1.json | 134ac847b89b7fb7beb3ccfb1d93aca6527a51107da2605da5ec504e426d9cfc |
| CODE-BBIS | 2026-11-16T12:57:27Z | registres/t07-etape-b-bis/code-bbis-v1.json | ee362bb70c5051097dab90c7978eb550d192f8c90f313317812635884b04e469 |
| CODE-BBIS | 2026-11-17T11:05:29Z | registres/t07-etape-b-bis/code-bbis-v2.json | 4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb |
| GO-BBIS | 2026-11-17T11:05:29Z | registres/t07-etape-b-bis/go-bbis-v2.txt | 33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62 |
| SCORES-BBIS | 2026-11-18T19:43:48Z | diag/20261118-154143-bbis-t07-v1/sondes-bbis.json | 645a172fe14fc18ff23ede0efa45dadd0841297489931ae6788caa6549a81c62 |
EOF
egal "registre propre : lignes de clé de l'étape B bis" 6 "$(grep -c -E '^\| [A-Z0-9-]+-BBIS \|' "$PROPRE")"
egal "registre propre : lignes de lecture, de verdict ou de table conjointe" 0 "$(grep -c -E '^\| (LECTURE|VERDICT|CONJOINTE)-BBIS \|' "$PROPRE")"
while IFS= read -r l; do egal "registre partagé : une fois « $(printf '%s' "$l" | cut -c1-60)… »" 1 "$(grep -c -x -F -- "$l" "$PARTAGE")"; done <<'EOF'
| RUN-CONFIRMATION-T06 | 2026-11-13T18:52:43Z | runs/20261111-151701-t06-reel/manifeste.json | 7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6 |
| VERDICT-P3BIS | 2026-11-14T10:30:38Z | docs/verdicts/verdict-P3-bis-v1-issue.json | c3a017ce1e8b0c41dee1e430f142590e88bd7104eada02b3a973ac98c0da28d0 |
| CODE-MOTS-ET-COUT-T06 | 2026-11-14T14:55:41Z | registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json | e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b |
| AUDIT-FUITES-T07 | 2026-11-14T14:57:54Z | diag/20261114-001352-t07-lecture-reel/audit-fuites-t07.json | 5c76b7ff48964abe9ec552552d57c32e0b9d9ec4519a61206f7fdac349fce094 |
| ISSUE-MOTS-ET-COUT-T06 | 2026-11-16T21:02:42Z | diag/20261116-205721-mots-et-cout-t06/issue-mots-et-cout-t06.json | 1b84d7c4440638699ac14711365fb865c1f5c57b50c39f44259a61b2aca53657 |
EOF
for k in RUN-CONFIRMATION-T06 VERDICT-P3BIS CODE-MOTS-ET-COUT-T06 AUDIT-FUITES-T07 ISSUE-MOTS-ET-COUT-T06; do
  egal "registre partagé : une seule ligne $k" 1 "$(grep -c "^| $k |" "$PARTAGE")"
done
egal "registre partagé : clés de l'étape B bis" 0 "$(grep -c -E '^\| *[A-Z0-9-]*-BBIS *\|' "$PARTAGE")"
# fichiers cités par les lignes : présents, à l'empreinte de la ligne, compagnon présent et égal
while read -r s p; do
  if [ ! -f "$p" ] || [ ! -f "$p.sha256" ]; then dire "DEFAUT : $p ou son compagnon absent"; FAUTES=$((FAUTES+1)); continue; fi
  egal "empreinte de $p égale à sa ligne de registre" "$s" "$(sha256sum "$p" | cut -d' ' -f1)"
  egal "compagnon de $p égal à sa ligne de registre" "$s" "$(cut -d' ' -f1 "$p.sha256")"
done <<'EOF'
0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb prereg/T0.7-etape-B-bis-v1.md
134ac847b89b7fb7beb3ccfb1d93aca6527a51107da2605da5ec504e426d9cfc registres/t07-etape-b-bis/ABSENCE-B-BBIS-v1.json
4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb registres/t07-etape-b-bis/code-bbis-v2.json
33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62 registres/t07-etape-b-bis/go-bbis-v2.txt
645a172fe14fc18ff23ede0efa45dadd0841297489931ae6788caa6549a81c62 diag/20261118-154143-bbis-t07-v1/sondes-bbis.json
7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6 runs/20261111-151701-t06-reel/manifeste.json
c3a017ce1e8b0c41dee1e430f142590e88bd7104eada02b3a973ac98c0da28d0 docs/verdicts/verdict-P3-bis-v1-issue.json
e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json
5c76b7ff48964abe9ec552552d57c32e0b9d9ec4519a61206f7fdac349fce094 diag/20261114-001352-t07-lecture-reel/audit-fuites-t07.json
1b84d7c4440638699ac14711365fb865c1f5c57b50c39f44259a61b2aca53657 diag/20261116-205721-mots-et-cout-t06/issue-mots-et-cout-t06.json
EOF
conclure
} 2>&1 | tee "$R"
