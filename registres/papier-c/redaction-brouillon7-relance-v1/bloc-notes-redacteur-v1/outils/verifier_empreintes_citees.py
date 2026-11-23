"""Contrôle des couples (chemin, empreinte) cités par un texte : pour chaque chemin entre accents graves qui existe
sur main (arbre de travail) ou dans la copie de la branche du 19 novembre, calcule le sha256 et cherche, dans les
600 signes qui suivent le chemin, une empreinte entière ou abrégée (au moins 8 chiffres hexadécimaux, suivis ou non
de « … »). N'ouvre rien sous diag/, runs/, donnees/, docs/verdicts/ ni aucun nom interdit."""
import hashlib, re, sys
from pathlib import Path

texte = Path(sys.argv[1]).read_text(encoding="utf-8")
racines = [Path(p) for p in sys.argv[2:]]
INTERDITS = ("diag/", "runs/", "donnees/", "docs/verdicts/", "consigne-privee", "conception-ii-b", "ii-b-saboteur")
chemins = re.finditer(r"`([A-Za-z0-9_./\-…]+\.(?:md|py|json|txt|pdf|gz|tsv|sh))`", texte)
vus, bilan = set(), {"conforme": 0, "DIFFERENT": 0, "introuvable": 0, "sans empreinte voisine": 0, "interdit": 0}
for m in chemins:
    ch = m.group(1)
    if "…" in ch or ch in vus:
        continue
    vus.add(ch)
    if any(i in ch for i in INTERDITS):
        bilan["interdit"] += 1
        continue
    suite = texte[m.end(): m.end() + 600]
    cites = re.findall(r"`?\(?`?([0-9a-f]{8,64})(?:…)?`?", suite)
    trouves = []
    for r in racines:
        cands = [r / ch] if "/" in ch else list(r.rglob(ch))[:8]
        for c in cands:
            if c.is_file() and not any(i in str(c) for i in INTERDITS):
                trouves.append((c, hashlib.sha256(c.read_bytes()).hexdigest()))
    if not trouves:
        bilan["introuvable"] += 1
        print("introuvable\t" + ch)
        continue
    if not cites:
        bilan["sans empreinte voisine"] += 1
        continue
    ok = any(h.startswith(c) for _, h in trouves for c in cites[:3])
    bilan["conforme" if ok else "DIFFERENT"] += 1
    if not ok:
        print("DIFFERENT\t%s\tcité %s\tcalculé %s" % (ch, cites[0][:16], ", ".join(sorted({h[:16] for _, h in trouves}))))
print(bilan)
