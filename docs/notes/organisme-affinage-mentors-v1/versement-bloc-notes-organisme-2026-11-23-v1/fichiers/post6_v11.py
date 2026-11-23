# Brouillon 2 du préenregistrement v11, point (a) : le registre compte des GO à trois chiffres de rang (GO-2026-11-22-107, -124) ;
# la lecture à deux chiffres de v10 ne les voyait pas (ni comme GO lu, ni comme révocation). Lecture à deux ou trois chiffres.
_vieux = 'r"^\\|\\s*(GO-\\d{4}-\\d{2}-\\d{2}-\\d{2})\\s*\\|"'
_neuf = 'r"^\\|\\s*(GO-\\d{4}-\\d{2}-\\d{2}-\\d{2,3})\\s*\\|"'
assert src.count(_vieux) == 2, src.count(_vieux)
src = src.replace(_vieux, _neuf)
