#!/bin/bash
# Rejoue les mêmes fichiers d'essais réels avec la ligne v2 (bac) puis sans (bac-sans) ; compare par essai.
D=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecture-greffon-v2-b
FICHIERS="tests/test_manifeste.py tests/test_prereg.py tests/test_scellement.py tests/test_garde_calcul.py tests/test_garde_google_v1.py tests/test_garde_refus_question_v1.py tests/test_run_factice.py tests/test_cibles_invisibles_v1.py tests/test_cibles_invisibles_v2.py"
for V in bac bac-sans; do
  cd "$D/$V" || exit 99
  env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$D/$V/src" TMPDIR="$D/tables" /home/user/controle-ia-travail/.venv/bin/python -m pytest -p no:cacheprovider --rootdir="$D/$V" -q -rA $FICHIERS > "$D/tables/real-$V.txt" 2>&1
  echo "$V CODE=$?"
done
for V in bac bac-sans; do
  grep -E '^(PASSED|FAILED|ERROR|XFAIL|XPASS|SKIPPED)' "$D/tables/real-$V.txt" | sed -E 's/ - .*$//; s/^XFAIL /XFAIL /' | sort > "$D/tables/real-$V.res"
  tail -1 "$D/tables/real-$V.txt"
done
diff "$D/tables/real-bac.res" "$D/tables/real-bac-sans.res" > "$D/tables/real-diff.txt"; echo "diff code $?"
cat "$D/tables/real-diff.txt"
