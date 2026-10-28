"""SimHash sur 3-grammes de caractères, dimension 16, version 1 (bibliothèque standard seule).

Table de signes déterministe : pour un 3-gramme g, on calcule SHA-256(SEL + g) ; la coordonnée i
(i = 0..15) vaut +1 si le bit i des 32 premiers bits (poids fort d'abord) vaut 1, sinon -1.
Chaque jeton est bordé par '#' avant découpe (« spectral » -> « #spectral# » -> #sp, spe, ..., al#).
Deux sorties :
- projection : somme des vecteurs de signes des 3-grammes (projection de Rademacher des
  comptes de 3-grammes ; c'est elle qui préserve le cosinus en espérance) ;
- binaire : signe de la projection (SimHash de Charikar ; 0 -> +1).
"""
import hashlib

SEL = "brique1-simhash3-v1|"
DIM = 16
N = 3
_CACHE = {}


def ngrammes(jeton, n=N, bord="#"):
    m = bord + jeton + bord
    if len(m) < n:
        return [m]
    return [m[k:k + n] for k in range(len(m) - n + 1)]


def signes(g, dim=DIM):
    s = _CACHE.get(g)
    if s is None:
        h = hashlib.sha256((SEL + g).encode("utf-8")).digest()
        bits = int.from_bytes(h[:4], "big")
        s = [1.0 if (bits >> (31 - i)) & 1 else -1.0 for i in range(dim)]
        _CACHE[g] = s
    return s


def projection(liste_jetons, dim=DIM, n=N):
    v = [0.0] * dim
    for jeton in liste_jetons:
        for g in ngrammes(jeton, n):
            s = signes(g, dim)
            for i in range(dim):
                v[i] += s[i]
    return v


def binaire(liste_jetons, dim=DIM, n=N):
    return [1.0 if x >= 0 else -1.0 for x in projection(liste_jetons, dim, n)]


def comptes_ngrammes(liste_jetons, n=N):
    c = {}
    for jeton in liste_jetons:
        for g in ngrammes(jeton, n):
            c[g] = c.get(g, 0) + 1
    return c


def table_consignee():
    """Table effectivement utilisée (3-grammes rencontrés), triée, et son empreinte SHA-256."""
    lignes = [f"{g}\t{''.join('+' if x > 0 else '-' for x in _CACHE[g])}" for g in sorted(_CACHE)]
    texte = "\n".join(lignes) + "\n"
    return texte, hashlib.sha256(texte.encode("utf-8")).hexdigest()
