# Un seul candidat en memoire, extraits choisis (verification du harnais). Rien n'est ecrit.
import sys, re
sys.argv = sys.argv[:1] + sys.argv[1:]
import importlib.util
spec = importlib.util.spec_from_file_location("opt", sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
o = dict(zip(m.OPTIONS, sys.argv[2].split(",")))
lit = sys.argv[3] == "lettre"
t, j = m.candidat(o, False, lit)
print("ordre:", j)
print(m.controler(t, o))
for anc in sys.argv[4:]:
    i = m.norm(t).find(anc)
    print("\n>>", anc, ":", m.norm(t)[max(0,i-200):i+700] if i >= 0 else "ABSENT")
