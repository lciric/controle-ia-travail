"""Recalcule les empreintes sha256 de la table d'en-tête du brouillon 6, sans ouvrir les fichiers que les interdits visent."""
import hashlib, re, sys, os
INTERDITS = ("prereg/T0.6-organismes-v0-v1.md", "prereg/T0.8", "registres/code-mots-et-cout", "scripts/mots_et_cout",
             "bases/", "sondes/", "/t07", "notice-", "contre-lecture-code-")
texte = open(sys.argv[1], encoding="utf-8").read().split("\n")
egales = differentes = absentes = sautees = 0
for l in texte[:96]:
    m = re.match(r"\| `([^`]+)`.*\| `([0-9a-f]{64})` \|$", l)
    if not m:
        continue
    chemin, emp = m.groups()
    if any(i in chemin for i in INTERDITS):
        sautees += 1; print("SAUTÉE (interdit)", chemin); continue
    if not os.path.exists(chemin):
        absentes += 1; print("ABSENTE", chemin); continue
    h = hashlib.sha256(open(chemin, "rb").read()).hexdigest()
    if h == emp:
        egales += 1
    else:
        differentes += 1; print("DIFFÉRENTE", chemin, h)
print(f"égales {egales}, différentes {differentes}, absentes {absentes}, sautées {sautees}")
