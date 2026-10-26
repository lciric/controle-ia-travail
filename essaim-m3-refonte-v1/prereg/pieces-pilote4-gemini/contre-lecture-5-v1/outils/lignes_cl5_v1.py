# Comparaison indépendante (contre-lecture 5), lecture seule : passages cités par P4v3 (v6.1) et par la v4 (v6.2.1).
import pathlib, sys, hashlib
A = pathlib.Path(sys.argv[1]); B = pathlib.Path(sys.argv[2])
P = [("principal.py",1985,1990,2101,2106),("principal.py",926,933,991,998),("principal.py",1927,1927,2043,2043),
     ("principal.py",1950,1950,2066,2066),("principal.py",740,740,794,794),("principal.py",86,95,89,98),
     ("memoire_isvd.py",236,244,240,248),("memoire_isvd.py",114,117,118,121),("memoire_isvd.py",125,127,129,131),
     ("mitose_spectrale.py",75,75,75,75),("mitose_spectrale.py",117,117,117,117),("mitose_spectrale.py",78,78,78,78),
     ("principal.py",928,929,993,994),("principal.py",932,932,997,997)]
for f,a1,a2,b1,b2 in P:
    la=(A/f).read_text(encoding="utf-8").splitlines()[a1-1:a2]; lb=(B/f).read_text(encoding="utf-8").splitlines()[b1-1:b2]
    print(f"{f} v6.1 {a1}-{a2} / v6.2.1 {b1}-{b2} : {'identique' if la==lb else 'DIFFERENT'} ; {la[0].strip()[:70]!r}")
for f in ("principal.py","memoire_isvd.py","mitose_spectrale.py","politique_endogene.py"):
    print(f, hashlib.sha256((A/f).read_bytes()).hexdigest()[:16], hashlib.sha256((B/f).read_bytes()).hexdigest()[:16])
