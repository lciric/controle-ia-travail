import sys, re, subprocess
f, calc, date, hm = sys.argv[1:5]
t = open(f, encoding="utf-8").read()
code = open(calc, encoding="utf-8").read()
sortie = subprocess.run([sys.executable, "-I", calc], capture_output=True, text=True, check=True).stdout
for k, v in {"@@DATE@@": date, "@@HEURE_PROGRAMME@@": hm, "@@CODE@@": code, "@@SORTIE@@": sortie}.items():
    assert t.count(k) == 1, k
    t = t.replace(k, v)
assert "@@" not in t
blocs = re.findall(r"^```(\w*)\n(.*?)^```$", t, flags=re.S | re.M)
assert [l for l, _ in blocs] == ["python", ""], [l for l, _ in blocs]
rejouee = subprocess.run([sys.executable, "-I", "-c", blocs[0][1]], capture_output=True, text=True, check=True).stdout
assert rejouee == blocs[1][1], "sortie différente"
open(f, "w", encoding="utf-8").write(t)
print("devis des moniteurs rempli ; programme recopié rejoué, sortie identique ;", date)
