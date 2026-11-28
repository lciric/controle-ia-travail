"""Contexte de chaque remplacement dans la v5 : 160 caractères avant et après le texte neuf (jonctions)."""
import sys, importlib.util
spec = importlib.util.spec_from_file_location("corr", sys.argv[1])
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
v5 = open(sys.argv[2], encoding="utf-8").read()
for i, (qui, old, new) in enumerate(m.R, 1):
    p = v5.find(new)
    if p < 0:
        print(f"== {i} : texte neuf non retrouvé tel quel (remplacé ensuite ?)"); continue
    av = v5[max(0, p-160):p].replace("\n", "⏎")
    ap = v5[p+len(new):p+len(new)+160].replace("\n", "⏎")
    debut = new[:60].replace("\n", "⏎"); fin = new[-60:].replace("\n", "⏎")
    print(f"== {i} [{qui}]\n  AVANT …{av}\n  [DÉBUT] {debut} … [FIN] {fin}\n  APRÈS {ap}…")
