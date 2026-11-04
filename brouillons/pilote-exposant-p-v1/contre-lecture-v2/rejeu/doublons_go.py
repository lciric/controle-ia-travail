"""Classe chaque ligne répétée de registres/go.md selon la règle R-389 de la garde de main (lecture seule)."""
import re, sys
from datetime import date
L = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
go, bad, ext, cible = {}, [], [], sys.argv[2]
for n, l in enumerate(open(sys.argv[1], encoding="utf-8").read().splitlines(), 1):
    if not L.match(l): continue
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if len(c) != 8: bad.append((n, "colonnes", len(c))); continue
    i, a, t, p, pl, e, par, ref = c
    try:
        ad = date.fromisoformat(a); ed = None if (e == "—" and t != "calcul") else date.fromisoformat(e)
    except ValueError:
        bad.append((n, i, "dates")); continue
    if i in go:
        f = go[i]
        eok = (f["e"] is None and ed is None) or (f["e"] is not None and ed is not None and ed <= f["e"])
        crit = {"commence_par_extension": p.lower().startswith("extension"), "meme_type": t == f["t"], "Lazar": par == "Lazar",
                "date_ok": ad >= f["a"], "echeance_ok": eok}
        (ext if all(crit.values()) else bad).append((n, i, {k: v for k, v in crit.items() if not v} or "ok", p[:40]))
        continue
    go[i] = {"a": ad, "t": t, "e": ed}
print("extensions admises :", len(ext)); print("refusées :", len(bad))
for b in bad: print("  ", b)
print("cible", cible, go.get(cible))
