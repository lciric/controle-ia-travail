# Différence mot à mot de chaque couple (avant, après) du script des couples, pour voir ce qui est retiré du brouillon 3.
import difflib, importlib.util, sys
spec = importlib.util.spec_from_file_location("c", sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for ident, tache, lieu, avant, apres in m.COUPLES:
    a, b = avant.split(), apres.split()
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    retire = [" ".join(a[i1:i2]) for t, i1, i2, j1, j2 in sm.get_opcodes() if t in ("delete", "replace")]
    if retire: print(ident, "| retiré ou remplacé :", " ‖ ".join(retire)[:700])
