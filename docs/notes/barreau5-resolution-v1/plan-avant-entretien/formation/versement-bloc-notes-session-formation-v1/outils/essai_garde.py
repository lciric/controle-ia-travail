"""Essai à blanc : la garde de calcul accepte-t-elle la forme « (GH_TOKEN=…; GO_ID=… vastai create …) » ? Rien n'est lancé."""
import sys
from datetime import date
sys.path.insert(0, sys.argv[1] + "/src")
import importlib.util as u
def charger_garde_de_calcul(r):
    s = u.spec_from_file_location("g", r + "/.claude/hooks/garde_calcul.py"); m = u.module_from_spec(s); s.loader.exec_module(m); return m
g = charger_garde_de_calcul(sys.argv[1])
for c in ['GO_ID=GO-2026-11-19-86 vastai create instance 1 --raw --label b5f-formation-v1-6',
          '( GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2"; GO_ID=GO-2026-11-19-86 vastai create instance 1 --raw --label b5f-formation-v1-6 )',
          'vastai create instance 1 --raw']:
    try:
        g.decider(c, date.today(), sys.argv[1]); r = "accepté"
    except SystemExit as e:
        r = "accepté" if e.code in (0, None) else f"bloqué (code {e.code})"
    print(r, "|", c[:60])
