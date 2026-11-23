S=$1; cd $S/wt
for f in $(cut -d: -f1 $S/ids.txt | sort -u); do
  b=$(basename $f .py)
  ids=$(grep "^$f::" $S/ids.txt | tr '\n' ' ')
  PYTHONPATH=src timeout 1500 /tmp/claude-0/-home-user-controle-ia-travail/cdf47db0-465c-5a9f-bc6b-2488e9a59218/scratchpad/venv/bin/python -m pytest -q -p no:cacheprovider --tb=short -rf $ids > $S/rejeu/$b.log 2>&1
  echo "$b $?" >> $S/rejeu/codes.txt
done
echo FINI >> $S/rejeu/codes.txt
