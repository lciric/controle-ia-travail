"""Compare les cellules de la table « Critères de lecture gelés » d'un texte à `LIGNES` d'un module (lecture seule)."""
import importlib.util, re, sys
from pathlib import Path
texte, module = Path(sys.argv[1]).read_text(encoding="utf-8"), Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("lp_cmp", module)
src = module.read_text(encoding="utf-8")
debut = src.index("LIGNES = {")
fin = src.index("\n}\n", debut) + 2
ns = {}
exec(src[debut:fin], ns)
LIGNES = ns["LIGNES"]
corps = re.split(r"^## +(.+?)\s*$", texte, flags=re.M)
sec = dict(zip(corps[1::2], corps[2::2]))["Critères de lecture gelés"]
table = {}
for l in sec.splitlines():
    if re.match(r"^\| *L\d+ *\|", l):
        c = [x.strip().replace("\x00", "|") for x in l.replace("\\|", "\x00").split("|")[1:-1]]
        table[c[0]] = (c[1], c[2])
print("lignes du texte :", list(table))
for k in table:
    for j, nom in enumerate(("issue", "lecture")):
        a, b = table[k][j], LIGNES.get(k, (None, None))[j]
        print(k, nom, "égal" if a == b else "DIFFÉRENT")
        if a != b:
            print("   texte :", a); print("   code  :", b)
