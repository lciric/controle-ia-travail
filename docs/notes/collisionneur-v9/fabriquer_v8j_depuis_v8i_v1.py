"""Fabrique collisionneur_v9_v8j.py depuis la v8i par remplacements exacts."""
import hashlib, sys
from pathlib import Path
D = Path("/home/user/controle-ia-travail/docs/notes/collisionneur-v9")
src = (D / "collisionneur_v9_v8i.py").read_text(encoding="utf-8")
assert hashlib.sha256(src.encode()).hexdigest().startswith("7c7aa713")

def remplacer(t, ancien, nouveau):
    n = t.count(ancien)
    if n != 1:
        sys.exit(f"ancien texte trouvé {n} fois : {ancien[:80]!r}")
    return t.replace(ancien, nouveau)

src = remplacer(src, """#   fichiers.
""", """#   fichiers.
# v9-v8j (même développeur, 22 novembre 2026) : copie du v9-v8i (7c7aa713…, inchangé, R12), corrigée selon la
#   vérification du même contre-lecteur. Changements, et seulement ceux-là : un chemin accepté a exactement deux
#   composants (« docs », « runs » ou « scripts », puis un seul nom : aucun chemin réel imbriqué) ; le nom n'est fait que
#   de lettres et de chiffres ASCII séparés par un seul « - », « _ » ou « . » (aucun homoglyphe, aucune pleine chasse).
""")
src = remplacer(src, 'VERSION = "collisionneur-v9-v8i"', 'VERSION = "collisionneur-v9-v8j"')
src = remplacer(src, 'COMPOSANT_ADMIS = re.compile(r"[^\\W_]+(?:[-_.][^\\W_]+)*")  # v9-v8i',
                'COMPOSANT_ADMIS = re.compile(r"[A-Za-z0-9]+(?:[-_.][A-Za-z0-9]+)*")  # v9-v8i ; v9-v8j : ASCII seul')
src = remplacer(src, '''    if len(composants) < 2 or composants[0] + "/" not in FORMES_RELATIVES:
        return False''', '''    if len(composants) != 2 or composants[0] + "/" not in FORMES_RELATIVES:  # v9-v8j : deux composants exactement
        return False''')
assert src.count("def normaliser(") == 1 and src.count("def normaliser_nom(") == 1
(D / "collisionneur_v9_v8j.py").write_text(src, encoding="utf-8")
print("écrit", hashlib.sha256(src.encode()).hexdigest())
