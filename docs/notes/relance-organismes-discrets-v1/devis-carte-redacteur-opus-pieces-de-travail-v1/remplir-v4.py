import sys, re, subprocess
src, dst, calc, date_v4, hm = sys.argv[1:6]
t = open(src, encoding="utf-8").read()
remp = {
    "@@DATE_V4@@": date_v4,
    "@@HEURE_PROGRAMME@@": hm,
    "@@CONFIRMATION_MERE@@": "confirmée par la session mère (`session_013QMayjbmQUdDuDs2S3i3XD`, message du 2026-11-22 vers 22:28Z : « Oui, je confirme les deux travaux, sans dépense, même cloisonnement »)",
}
for k, v in remp.items():
    assert t.count(k) == 1, k
    t = t.replace(k, v)
assert "@@" not in t
# contrôle : le programme recopié rend la sortie recopiée
blocs = re.findall(r"^```(\w*)\n(.*?)^```$", t, flags=re.S | re.M)
code = [c for l, c in blocs if l == "python"][0]
sortie = [c for l, c in blocs if l == ""][0]
assert code == open(calc, encoding="utf-8").read()
rejouee = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True, check=True).stdout
assert rejouee == sortie, "sortie différente"
open(dst, "w", encoding="utf-8").write(t)
print("v4 écrite, sortie rejouée identique ;", date_v4)
