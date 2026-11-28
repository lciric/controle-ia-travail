"""Déterminisme entre processus (graine de hachage de Python différente) : empreinte de la sortie canonique."""
import sys, json, copy, hashlib
cand, W = sys.argv[1], sys.argv[2]
sys.argv = [sys.argv[0], W]
exec(compile(open(W + "/sondes_juge.py").read().split("# 1. lecteur étendu")[0], "entete", "exec"))
m, g = (A, GA) if cand == "a" else (B, GB)
src = complet(tl._source(0, n_taches=20), lambda i, c, cout: texte(i, c, repr(cout)) + ("\n- COST: 1" if c == "saboteur" and i % 5 == 0 else ""))
lec = lire(src)
s = m.analyser_addendum(src, lec, g)
print(cand, hashlib.sha256(json.dumps(s, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest())
