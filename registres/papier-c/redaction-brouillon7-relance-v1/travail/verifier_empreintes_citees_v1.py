"""Contrôle des couples (chemin, empreinte) cités par un texte.

Usage : python3 verifier_empreintes_citees_v1.py TEXTE RACINE [RACINE…]

Pour chaque chemin écrit entre accents graves, cherché sous chaque racine (chemin entier, ou nom nu cherché dans
l'arbre), calcule le sha256 du fichier. Le couple est « conforme » si, après une des occurrences du chemin dans le
texte (500 signes), on lit une empreinte entière ou abrégée (au moins 8 chiffres hexadécimaux) qui commence celle du
fichier. Sinon : « sans empreinte voisine » (le texte ne donne pas d'empreinte à cet endroit), « à regarder »
(une empreinte voisine existe et aucune ne correspond : souvent celle d'une autre pièce citée juste après),
« introuvable » (aucun fichier de ce nom sous les racines). N'ouvre rien sous diag/, runs/, donnees/,
docs/verdicts/, ni aucun nom interdit par le mandat."""
import hashlib
import re
import sys
from pathlib import Path

texte = Path(sys.argv[1]).read_text(encoding="utf-8")
racines = [Path(p) for p in sys.argv[2:]]
INTERDITS = ("diag/", "runs/", "donnees/", "docs/verdicts/", "consigne-privee", "conception-ii-b", "ii-b-saboteur",
             "archives-reponses-modeles", "quarantaine")
MOTIF = re.compile(r"`([A-Za-z0-9_./\-]+\.(?:md|py|json|txt|pdf|gz|tsv|sh))`")
occurrences = {}
for m in MOTIF.finditer(texte):
    occurrences.setdefault(m.group(1), []).append(m.end())
bilan = {"conforme": 0, "à regarder": 0, "introuvable": 0, "sans empreinte voisine": 0, "non ouvert (interdit)": 0}
for ch, fins in sorted(occurrences.items()):
    if any(i in ch for i in INTERDITS):
        bilan["non ouvert (interdit)"] += 1
        print("non ouvert (interdit)\t" + ch)
        continue
    trouves = []
    for r in racines:
        cands = [r / ch] if "/" in ch else [c for c in r.rglob(ch)][:12]
        for c in cands:
            if c.is_file() and not any(i in str(c) for i in INTERDITS):
                trouves.append(hashlib.sha256(c.read_bytes()).hexdigest())
    cites = []
    for f in fins:
        cites += re.findall(r"(?<![0-9a-f])([0-9a-f]{8,64})(?![0-9a-f])", texte[f:f + 500])
    if not trouves:
        etat = "introuvable"
    elif not cites:
        etat = "sans empreinte voisine"
    elif any(h.startswith(c) for h in trouves for c in cites):
        etat = "conforme"
    else:
        etat = "à regarder"
    bilan[etat] += 1
    if etat != "conforme":
        print(etat + "\t" + ch + ("\tcalculé " + ", ".join(sorted({h[:16] for h in trouves})) if trouves else ""))
print(bilan)
