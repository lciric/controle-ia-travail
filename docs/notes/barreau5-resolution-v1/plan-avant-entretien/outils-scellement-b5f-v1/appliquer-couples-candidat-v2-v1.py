"""Applique, par recopie pure, les 22 couples exacts de la vérification du candidat au scellement v2 (barreau 5) au
texte et au devis candidats, dans l'ordre du programme du vérificateur, et écrit les deux pièces sous leurs noms
définitifs si et seulement si les empreintes obtenues sont celles que la vérification annonce. N'imprime que des
comptes et des empreintes. Usage : python3 -I -B appliquer-couples-candidat-v2-v1.py <racine du dépôt>
"""
import hashlib, importlib.util, sys
from pathlib import Path

R = Path(sys.argv[1]).resolve()
OUT = R / "docs/notes/barreau5-resolution-v1/plan-avant-entretien/outils-verification-candidat-scellement-v2-v1"
PROG = OUT / "couples-verification-candidat-v2-v1.py"
H_PROG = "68d66cade5066041a317dc203667d1c4b40ec5ea5b9d0a62d16c220f4f9f0a15"
T = "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md"
DV = "docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md"
T_DEF = "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md"
DV_DEF = "docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1.md"
ATT_AVANT = {T: "088e15ef", DV: "94a628a7"}
ATT_APRES = {T: "bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935",
             DV: "dc886195c77b0d67c31cb8815a1e97b9fa72dd35ebac2b8f3bc49d4e5cf59bcc"}
h = lambda b: hashlib.sha256(b).hexdigest()

if h(PROG.read_bytes()) != H_PROG:
    sys.exit("ARRET : programme du vérificateur d'une autre empreinte")
spec = importlib.util.spec_from_file_location("couples_verif_candidat_v2", PROG)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
assert mod.T == T and mod.DV == DV, "pièces visées différentes"
assert len(mod.COUPLES) == 22, len(mod.COUPLES)
for p in (T_DEF, DV_DEF):
    if (R / p).exists():
        sys.exit(f"ARRET : {p} existe déjà ; on n'écrase jamais (R12)")
texte = {}
for p, debut in ATT_AVANT.items():
    b = (R / p).read_bytes()
    if not h(b).startswith(debut):
        sys.exit(f"ARRET : {p} d'une autre empreinte")
    comp = (R / (p + ".sha256")).read_text().split()[0]
    if comp != h(b):
        sys.exit(f"ARRET : compagnon de {p} discordant")
    texte[p] = b.decode("utf-8")
for ident, constat, touche, piece, avant, apres in mod.COUPLES:
    n, m = texte[piece].count(avant), texte[piece].count(apres)
    if n != 1 or m != 0:
        sys.exit(f"ARRET : {ident} « avant » {n} fois, « après » {m} fois")
    texte[piece] = texte[piece].replace(avant, apres, 1)
    print(f"  {ident} appliqué ({Path(piece).name[:40]}…)")
for p, att in ATT_APRES.items():
    g = h(texte[p].encode("utf-8"))
    if g != att:
        sys.exit(f"ARRET : {p} donnerait {g}, attendu {att}")
(R / T_DEF).write_bytes(texte[T].encode("utf-8"))
(R / DV_DEF).write_bytes(texte[DV].encode("utf-8"))
for p in (T_DEF, DV_DEF):
    print(f"écrit {p} sha256 {h((R / p).read_bytes())}")
