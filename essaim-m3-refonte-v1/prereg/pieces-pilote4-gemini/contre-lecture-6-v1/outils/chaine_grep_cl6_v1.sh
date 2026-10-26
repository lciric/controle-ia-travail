#!/bin/bash
# Contre-lecture 6 : la chaîne de grep du lanceur v10 (l. 539-552), transcrite, sur les copies de la ligne de GO et des
# lignes de dépense du texte, remplies de valeurs d'essai (essai-lignes/) ; cas sains et artefacts — v1. N'écrit rien.
set -u
O="${1:?dossier essai-lignes}"
GO_ID=GO-2026-10-25-02; SQ=8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd
T=$(sed -n 's/^T=//p' "$O/valeurs-essai.txt"); V62=$(sed -n 's/^V62=//p' "$O/valeurs-essai.txt")
EMP_S=5ae4e801423bbef0$(printf 'c%.0s' $(seq 48))
chaine() { # course arbre nom emp_v62 segment registre
  local ligne_go dep r=OK t16="${T:0:16}"
  ligne_go="$(grep "^| $GO_ID |" "$6" | grep 'calcul' | grep "${SQ:0:8}" | grep "${2:0:8}" || true)"
  ligne_go="$(echo "$ligne_go" | grep "$t16" || true)"
  [ -n "$ligne_go" ] || r="refus GO"
  dep="$(cat "$O/depenses-essai.md")"
  echo "$dep" | grep "$3" | grep -q "$GO_ID" || r="$r ; refus dépense"
  if [ "$5" != 1 ]; then echo "$dep" | grep "$3" | grep "$GO_ID" | grep -q "segment $5\b" || r="$r ; refus segment"; fi
  echo "$dep" | grep "$3" | grep "$GO_ID" | grep -q "${EMP_S:0:16}" || r="$r ; refus M"
  if [ -n "$4" ]; then echo "$dep" | grep "$3" | grep "$GO_ID" | grep -q "${4:0:16}" || r="$r ; refus v6.2"; fi
  echo "$1 segment $5 ($(basename "$6")) : $r"
}
A62=4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d
A53=6251ab219e86286ec892a65e28cf9eebad5265fd6e32e350e68827897c811753
echo "--- cas sains (attendu : OK)"
chaine v6-2 $A62 pilote4-gemini-v6-2-v1 "" 1 "$O/registre-go-essai.md"
chaine v6-2 $A62 pilote4-gemini-v6-2-v1 "" 2 "$O/registre-go-essai.md"
chaine v5-3 $A53 pilote4-gemini-v5-3-v1 "$V62" 1 "$O/registre-go-essai.md"
chaine v5-3 $A53 pilote4-gemini-v5-3-v1 "$V62" 2 "$O/registre-go-essai.md"
echo "--- artefacts (attendu : refus)"
chaine v6-2 $A62 pilote4-gemini-v6-2-v1 "" 1 "$O/registre-go-sans-v621.md"
chaine v6-2 $A62 pilote4-gemini-v6-2-v1 "" 3 "$O/registre-go-essai.md"
chaine v5-3 $A53 pilote4-gemini-v5-3-v1 "dead$(printf 'd%.0s' $(seq 60))" 1 "$O/registre-go-essai.md"
