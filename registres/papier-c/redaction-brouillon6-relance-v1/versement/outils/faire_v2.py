import sys
src,dst=sys.argv[1],sys.argv[2]
t=open(src,encoding='utf-8').read()
a='"""Mesures de conception du préenregistrement du papier C (brouillon 4) : aucune donnée, aucun résultat lu.\n'
b=(a+'\nVersion 2 (2026-11-19) : même calcul que la version 1 (mesures_conception_papier_c_v1.py), plus deux sorties :\n'
   'les versions de numpy et de scipy en tête, et la ligne « P(W ≤ 0,20) sous le nul » à la fin.\n')
assert t.count(a)==1; t=t.replace(a,b)
a='import numpy as np\nfrom scipy.stats import beta\n'
b='import numpy as np\nimport scipy\nfrom scipy.stats import beta\n\nprint(f"numpy {np.__version__} ; scipy {scipy.__version__}")\n'
assert t.count(a)==1; t=t.replace(a,b)
assert t.endswith('affectations : {len(w)}")\n')
t+='print(f"P(W ≤ 0,20) sous le nul = {(w <= 0.20 + 1e-9).mean():.4f}".replace("= 0.", "= 0,"))\n'
open(dst,'x',encoding='utf-8',newline='\n').write(t)
