import sys, importlib.util as u
from datetime import date
s = u.spec_from_file_location("g", sys.argv[1] + "/.claude/hooks/garde_calcul.py"); g = u.module_from_spec(s); s.loader.exec_module(g)
for c in ['( export PATH="/x/venv-vast/bin:$PATH"; GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2"; GO_ID=GO-2026-11-19-86 vastai create instance 1 --raw --label b5f-formation-v1-6 )',
          '( export PATH="/x/venv-vast/bin:$PATH"; vastai create instance 1 --raw )',
          '/x/venv-vast/bin/vastai create instance 1 --raw']:
    try:
        g.decider(c, date.today(), sys.argv[1]); r = "accepté"
    except SystemExit as e:
        r = "accepté" if e.code in (0, None) else f"bloqué (code {e.code})"
    print(r, "|", c[:90])
