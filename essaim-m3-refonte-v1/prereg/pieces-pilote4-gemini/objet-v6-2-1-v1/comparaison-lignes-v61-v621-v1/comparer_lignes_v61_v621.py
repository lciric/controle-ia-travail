import sys, pathlib
A = pathlib.Path(sys.argv[1]); B = pathlib.Path(sys.argv[2])
paires = [("principal.py",1985,1990,"principal.py",2101,2106,"fin de conception"),
          ("principal.py",926,933,"principal.py",991,998,"mutation, stagnation (canal d)"),
          ("principal.py",1927,1927,"principal.py",2043,2043,"finally"),
          ("principal.py",1950,1950,"principal.py",2066,2066,"mise a jour memoire"),
          ("principal.py",740,740,"principal.py",794,794,"exemple de format"),
          ("principal.py",86,95,"principal.py",89,98,"requetes de reserve"),
          ("memoire_isvd.py",236,244,"memoire_isvd.py",240,248,"memoire : remplacement par generation"),
          ("memoire_isvd.py",114,117,"memoire_isvd.py",118,121,"memoire : score de g0"),
          ("memoire_isvd.py",125,127,"memoire_isvd.py",129,131,"memoire : meilleur ancetre"),
          ("mitose_spectrale.py",75,75,"mitose_spectrale.py",75,75,"mitose 75"),
          ("mitose_spectrale.py",117,117,"mitose_spectrale.py",117,117,"mitose 117"),
          ("mitose_spectrale.py",78,78,"mitose_spectrale.py",78,78,"mitose 78 (castes)")]
for fa,a1,a2,fb,b1,b2,nom in paires:
    la = (A/fa).read_text(encoding="utf-8").splitlines()[a1-1:a2]
    lb = (B/fb).read_text(encoding="utf-8").splitlines()[b1-1:b2]
    print(f"{nom}: v6.1 {fa} l. {a1}-{a2} -> v6.2.1 l. {b1}-{b2} : {'identique' if la==lb else 'DIFFERENT'}")
    if la != lb:
        for x,y in zip(la,lb):
            if x!=y: print("   v6.1  :", x.strip()[:150]); print("   v6.2.1:", y.strip()[:150])
