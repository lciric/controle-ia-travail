import sys, importlib.util as u
from datetime import date
s = u.spec_from_file_location("g", sys.argv[1] + "/.claude/hooks/garde_calcul.py"); g = u.module_from_spec(s); s.loader.exec_module(g)
c = open(sys.argv[2], encoding="utf-8").read()
try:
    g.decider(c, date.today(), sys.argv[1]); print("garde : accepté")
except SystemExit as e:
    print("garde :", "accepté" if e.code in (0, None) else f"bloqué {e.code}")
