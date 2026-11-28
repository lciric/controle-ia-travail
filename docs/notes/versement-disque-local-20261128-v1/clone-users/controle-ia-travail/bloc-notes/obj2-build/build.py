import json, re, sys
src = open(sys.argv[1], encoding="utf-8").read()
# section -> option label
opt = None
items = []
cur = None
for line in src.splitlines():
    m = re.match(r"^### (\S+)", line)
    if m:
        opt = m.group(1)
        continue
    if line.startswith("## Option externe G"):
        opt = "G"
    if line.startswith("## Ensemble"):
        opt = "ensemble"
    m = re.match(r"^- \*\*(O2-\d+) — (fatale|sérieuse|mineure)([^*]*)\*\*\s*(.*)$", line)
    if m:
        if cur: items.append(cur)
        extra = m.group(3).strip()
        label = opt
        if opt == "G":
            label = "G " + extra.strip("() ").replace("ligne ", "").replace("lignes ", "")
        elif opt == "ensemble":
            label = "ensemble"
        cur = {"option": label, "classe": m.group(2), "objection": m.group(1) + ". " + m.group(4).strip(), "preuve": ""}
        mode = "obj"
        continue
    if cur is None:
        continue
    s = line.strip()
    if s.startswith("- Preuve :"):
        cur["preuve"] = s[len("- Preuve :"):].strip()
        mode = "preuve"
        continue
    if s.startswith("## ") or s.startswith("### ") or s == "---" or s == "":
        if s.startswith("## Bilan"):
            items.append(cur); cur = None
        continue
    if mode == "obj":
        cur["objection"] += " " + s
    else:
        cur["preuve"] += " " + s
if cur: items.append(cur)
for it in items:
    for k in ("objection","preuve"):
        it[k] = it[k].replace("`", "").replace('"', "«").strip()
out = {"chemin": sys.argv[1], "objections": items}
s = json.dumps(out, ensure_ascii=False)
json.loads(s)
open(sys.argv[2], "w", encoding="utf-8").write(s)
print(len(items), len(s))
from collections import Counter
print(Counter(i["classe"] for i in items))
print(Counter(i["option"] for i in items))
