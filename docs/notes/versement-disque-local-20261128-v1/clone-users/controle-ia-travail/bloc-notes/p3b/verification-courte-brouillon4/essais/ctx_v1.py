import sys, re, importlib.util
spec = importlib.util.spec_from_file_location("opt", sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
o = dict(zip(m.OPTIONS, sys.argv[2].split(",")))
t, j = m.candidat(o, False, sys.argv[3] == "lettre")
n = m.norm(t)
for mot in sys.argv[4:]:
    for x in re.finditer(mot, n, re.I):
        print(f"[{mot}]", n[max(0, x.start()-160):x.end()+120], "\n")
