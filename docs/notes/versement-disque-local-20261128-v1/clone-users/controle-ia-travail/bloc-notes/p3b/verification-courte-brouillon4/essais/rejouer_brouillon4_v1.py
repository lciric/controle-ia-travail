# Rejoue en memoire le script du redacteur du brouillon 4 (heure fixee a 02:30, celle du journal) et compare.
import hashlib, sys
from pathlib import Path
RACINE = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3b")
src = (RACINE / "brouillon4/travail/appliquer_brouillon4_v1.py").read_text(encoding="utf-8")
ligne = 'HEURE = subprocess.run(["date", "-u", "+%H:%M"], capture_output=True, text=True, check=True).stdout.strip()'
assert src.count(ligne) == 1
src = src.replace(ligne, 'HEURE = "02:30"')
ns = {"__name__": "rejeu"}
exec(compile(src, "appliquer_brouillon4_v1.py", "exec"), ns)
E = ns["E"]; SOURCES = ns["SOURCES"]
textes = {k: s.read_text(encoding="utf-8") for k, (s, _) in SOURCES.items()}
for f, ident, old, new in E:
    n = textes[f].count(old)
    assert n == 1, (f, ident, n)
    textes[f] = textes[f].replace(old, new, 1)
print("remplacements :", len(E))
for k, (_, dst) in SOURCES.items():
    vrai = dst.read_bytes()
    moi = textes[k].encode("utf-8")
    print(k, dst.name, "identique" if vrai == moi else "DIFFERENT", hashlib.sha256(moi).hexdigest()[:8])
# journal
j = (RACINE / "brouillon4/travail/journal-remplacements-v1.txt").read_text(encoding="utf-8")
attendu = f"heure UTC 02:30 ; {len(E)} remplacements, chacun trouvé une seule fois\n" + "\n".join(f"{f}\t{i}" for f, i, _, _ in E) + "\n"
print("journal", "identique" if j == attendu else "DIFFERENT")
