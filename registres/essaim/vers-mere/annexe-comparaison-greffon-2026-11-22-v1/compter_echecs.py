"""Compte les échecs par fichier d'essai dans une sortie pytest (--tb long), à partir de la section FAILURES."""
import re
import sys
from collections import Counter

texte = open(sys.argv[1], encoding="utf-8", errors="replace").read().splitlines()
debut = next(i for i, l in enumerate(texte) if re.match(r"^=+ FAILURES =+$", l))
fin = next((i for i in range(debut + 1, len(texte)) if re.match(r"^=+ .* =+$", texte[i])), len(texte))
blocs, courant = [], None
for l in texte[debut + 1:fin]:
    m = re.match(r"^_{3,} (\S.*\S) _{3,}$", l)
    if m and not set(m.group(1)) <= {"_", " "}:
        courant = [m.group(1), []]
        blocs.append(courant)
    elif courant is not None:
        courant[1].append(l)
compte, motifs = Counter(), Counter()
for nom, lignes in blocs:
    fichiers = [re.match(r"^(tests/[^:]+\.py):\d+", x).group(1) for x in lignes if re.match(r"^tests/[^:]+\.py:\d+", x)]
    f = fichiers[0] if fichiers else "?"
    compte[f] += 1
    erreur = next((x[2:].strip()[:90] for x in lignes if x.startswith("E   ")), "?")
    motifs[re.sub(r"\d+", "N", erreur.split(":")[0])] += 1
print("blocs", len(blocs))
for f, n in compte.most_common():
    print(n, f)
print("--- motifs d'erreur")
for m, n in motifs.most_common(15):
    print(n, m)
