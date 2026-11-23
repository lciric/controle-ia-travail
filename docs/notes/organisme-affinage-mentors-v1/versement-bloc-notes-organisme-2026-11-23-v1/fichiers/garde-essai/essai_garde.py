import importlib.util, sys, datetime as dt
from pathlib import Path
spec = importlib.util.spec_from_file_location("garde", "/home/user/wt-organisme/.claude/hooks/garde_calcul.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
g.REGISTRE_GO = Path(sys.argv[1])
cmds = {
 "lanceur": "GO_ID=GO-2026-11-22-80 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v11b.py",
 "vastai_go80": "GO_ID=GO-2026-11-22-80 vastai create instance 1",
 "vastai_go14": "GO_ID=GO-2026-11-18-14 vastai create instance 1",
 "vastai_go124": "GO_ID=GO-2026-11-22-124 vastai create instance 1",
}
for jour in (dt.date(2026,11,22), dt.date(2026,11,26), dt.date(2026,12,16)):
    for k, c in cmds.items():
        try:
            g.decider(c, jour); print(jour, k, "accepté")
        except SystemExit as e:
            print(jour, k, "bloqué", e.code)
