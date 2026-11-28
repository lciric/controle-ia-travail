"""Différentiel mot à mot, remplacement par remplacement (ancien -> nouveau)."""
import sys, importlib.util, difflib
spec = importlib.util.spec_from_file_location("corr", sys.argv[1])
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for i, (qui, old, new) in enumerate(m.R, 1):
    a, b = old.split(), new.split()
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    print(f"===== {i} [{qui}]")
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        ctx = " ".join(a[max(0, i1-4):i1])
        print(f"  {op}: …{ctx} [-{' '.join(a[i1:i2])}-] {{+{' '.join(b[j1:j2])}+}}")
