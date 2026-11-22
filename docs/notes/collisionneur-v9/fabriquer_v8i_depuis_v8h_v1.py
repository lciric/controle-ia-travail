"""Fabrique collisionneur_v9_v8i.py depuis la v8h par remplacements exacts."""
import hashlib, sys
from pathlib import Path
D = Path("/home/user/controle-ia-travail/docs/notes/collisionneur-v9")
src = (D / "collisionneur_v9_v8h.py").read_text(encoding="utf-8")
assert hashlib.sha256(src.encode()).hexdigest().startswith("d9b41b11")

def remplacer(t, ancien, nouveau):
    n = t.count(ancien)
    if n != 1:
        sys.exit(f"ancien texte trouvé {n} fois : {ancien[:80]!r}")
    return t.replace(ancien, nouveau)

src = remplacer(src, """#   acceptation journalisée (cellule, empreinte, chemins) et signale une acceptation caduque.
""", """#   acceptation journalisée (cellule, empreinte, chemins) et signale une acceptation caduque.
# v9-v8i (même développeur, 22 novembre 2026) : copie du v9-v8h (d9b41b11…, inchangé, R12), corrigée selon la
#   vérification du même contre-lecteur. Changements, et seulement ceux-là : (B1 bis) chaque composant du chemin n'est fait
#   que de lettres et de chiffres séparés par un seul « - », « _ » ou « . » ; le caractère qui suit le jeton est la fin du
#   texte, un blanc ou une ponctuation de phrase (sinon le jeton est coupé : refus) ; le nom et les entrées du dépôt sont
#   comparés normalisés (sans casse, sans caractère autre que lettre ou chiffre), avec et sans extension, et un nom qui est
#   le début d'une entrée (ou l'inverse), à partir de six caractères, est refusé ; (NB) essai d'une erreur du système de
#   fichiers.
""")
src = remplacer(src, 'VERSION = "collisionneur-v9-v8h"', 'VERSION = "collisionneur-v9-v8i"')
src = remplacer(src, '''PONCTUATION_FINALE = ".-"
''', '''PONCTUATION_FINALE = ".-"
COMPOSANT_ADMIS = re.compile(r"[^\\W_]+(?:[-_.][^\\W_]+)*")  # v9-v8i
SUIVANT_ADMIS = set(" \\t\\n\\r,;:!?)]}»\\"'’")  # v9-v8i : après le jeton (ou fin du texte)
PREFIXE_MIN = 6  # v9-v8i
''')
src = remplacer(src, '''        jeton = MOTIF_JETON_CHEMIN.match(texte, m.start()).group(0)
        if not chemin_hors_depot(jeton):  # v9-v8h (B1)''', '''        jeton = MOTIF_JETON_CHEMIN.match(texte, m.start()).group(0)
        fin = m.start() + len(jeton)
        if fin < len(texte) and texte[fin] not in SUIVANT_ADMIS:  # v9-v8i : jeton coupé (caractère invisible, +, %)
            raise Arret(CODE_MOTIF, f"« {cat} » : une occurrence est suivie d'un caractère qui prolonge le chemin ; "
                                    f"acceptation refusée")
        if not chemin_hors_depot(jeton):  # v9-v8h (B1)''')
src = remplacer(src, '''    if any(x in ("", ".", "..") for x in composants[1:]):
        return False
    nom = composants[1].casefold()
    try:
        entrees = list((RACINE_DEPOT / composants[0]).iterdir()) if (RACINE_DEPOT / composants[0]).is_dir() else []
    except OSError:
        return False
    for e in entrees:
        n = e.name.casefold()
        if nom in (n, Path(n).stem) or Path(nom).stem in (n, Path(n).stem):
            return False
    return True''', '''    if any(x in ("", ".", "..") for x in composants[1:]):
        return False
    if not all(COMPOSANT_ADMIS.fullmatch(x) for x in composants[1:]):  # v9-v8i
        return False
    nom = composants[1]
    try:
        entrees = list((RACINE_DEPOT / composants[0]).iterdir()) if (RACINE_DEPOT / composants[0]).is_dir() else []
    except OSError:
        return False
    noms = {normaliser_nom(nom), normaliser_nom(Path(nom).stem)}
    for e in entrees:
        reels = {normaliser_nom(e.name), normaliser_nom(Path(e.name).stem)}
        if noms & reels:
            return False
        for a in noms:
            for b in reels:
                if min(len(a), len(b)) >= PREFIXE_MIN and (a.startswith(b) or b.startswith(a)):
                    return False
    return True


def normaliser_nom(x):
    """v9-v8i : sans casse, sans caractère autre que lettre ou chiffre."""
    return re.sub(r"[\\W_]", "", x.casefold())''')
assert src.count("def normaliser(") == 1 and src.count("def normaliser_nom(") == 1
(D / "collisionneur_v9_v8i.py").write_text(src, encoding="utf-8")
print("écrit", hashlib.sha256(src.encode()).hexdigest())
