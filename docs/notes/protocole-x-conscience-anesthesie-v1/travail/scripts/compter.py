import sys, re
s = open(sys.argv[1], encoding='utf-8').read()
i = s.index("## Annexe — clés des sources")
corps, annexe = s[:i], s[i:]
print("fichier entier :", len(s.split()), "mots ; corps (hors annexe des sources) :", len(corps.split()), "; annexe :", len(annexe.split()))
for p in re.split(r'\n(?=## )', corps):
    print(f"{len(p.split()):5d}  {p.splitlines()[0][:90]}")
print("dernière ligne :", repr(s.rstrip('\n').splitlines()[-1]))
