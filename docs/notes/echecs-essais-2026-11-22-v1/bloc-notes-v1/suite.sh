cd /home/user/controle-ia-travail
for i in 0 1 2 3; do
  PYTHONPATH=src /tmp/claude-0/-home-user-controle-ia-travail/cdf47db0-465c-5a9f-bc6b-2488e9a59218/scratchpad/venv/bin/python -m pytest -q -p no:cacheprovider --tb=short -rfEX --basetemp=/tmp/claude-0/-home-user-controle-ia-travail/cdf47db0-465c-5a9f-bc6b-2488e9a59218/scratchpad/bt$i $(cat /tmp/claude-0/-home-user-controle-ia-travail/cdf47db0-465c-5a9f-bc6b-2488e9a59218/scratchpad/suite/lot$i) > /tmp/claude-0/-home-user-controle-ia-travail/cdf47db0-465c-5a9f-bc6b-2488e9a59218/scratchpad/suite/lot$i.log 2>&1 &
done
wait; echo FINI
