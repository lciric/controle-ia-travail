"""v11 — addendum : réglé et engagé de l'étape « attaque_goodhart_v2 » (les deux fournisseurs) juste après des instants choisis,
et marge sous la règle « réglé + engagé + pire cas du nouvel appel ≤ 40 ».
Usage : python3 -I -B v11_jalons.py REGISTRE.jsonl SORTIE_TXT"""
import json
import sys
from datetime import datetime

reg = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
t = lambda s: datetime.fromisoformat(s.replace("Z", "+00:00"))  # noqa: E731
deb = {e["id"]: e for e in reg if e["type"] == "debut"}
fin = {e["id"]: e for e in reg if e["type"] == "fin"}
JALONS = ["10:11:26", "10:39:16", "10:40:44", "11:05:17", "12:18:03.3", "12:22:15", "13:29:14"]
lignes = []
for j in JALONS:
    ref = datetime.fromisoformat(f"2026-11-02T{j}+00:00")
    regle = {"argon": 0.0, "kimi": 0.0}
    engage = {"argon": 0.0, "kimi": 0.0}
    for i, d in deb.items():
        if t(d["quand_utc"]) <= ref:
            f = fin.get(i)
            if f and t(f["quand_utc"]) <= ref:
                regle[d["fournisseur"]] += f["cout_usd"]
            else:
                engage[d["fournisseur"]] += d["pire_cas_usd"]
    s = sum(regle.values()) + sum(engage.values())
    lignes.append(f"{j} UTC : réglé argon {regle['argon']:.6f}, kimi {regle['kimi']:.6f}, total {sum(regle.values()):.6f} ; "
                  f"engagé argon {engage['argon']:.6f}, kimi {engage['kimi']:.6f} ; réglé + engagé {s:.6f} ; "
                  f"marge avant un appel Kimi au pire cas 0,6659 : {40 - s - 0.6659:.6f}")
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(lignes) + "\n")
print("\n".join(lignes))
