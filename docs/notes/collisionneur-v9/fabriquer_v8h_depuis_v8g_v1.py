"""Fabrique collisionneur_v9_v8h.py depuis la v8g par remplacements exacts."""
import hashlib, sys
from pathlib import Path
D = Path("/home/user/controle-ia-travail/docs/notes/collisionneur-v9")
src = (D / "collisionneur_v9_v8g.py").read_text(encoding="utf-8")
assert hashlib.sha256(src.encode()).hexdigest().startswith("93f96e95")

def remplacer(t, ancien, nouveau):
    n = t.count(ancien)
    if n != 1:
        sys.exit(f"ancien texte trouvé {n} fois : {ancien[:80]!r}")
    return t.replace(ancien, nouveau)

src = remplacer(src, """#   `verifier` et le devis de reprise appliquent la même règle. Détail : rapport-developpeur-collisionneur-v9-v8g-v1.md.
""", """#   `verifier` et le devis de reprise appliquent la même règle. Détail : rapport-developpeur-collisionneur-v9-v8g-v1.md.
# v9-v8h (même développeur, 22 novembre 2026) : copie du v9-v8g (93f96e95…, inchangé, R12), corrigée selon la
#   contre-lecture d'un Opus neuf (verification-collisionneur-v9-v8g-opus-v1.md). Changements, et seulement ceux-là :
#   (B1) contrôle d'un chemin par liste blanche : composants « . », « .. » ou vides refusés ; ponctuation finale retirée ;
#   refus dès que le deuxième composant (sans casse, avec ou sans extension) nomme une entrée du dossier docs/, runs/ ou
#   scripts/ du dépôt ; racine du dépôt contrôlée (CLAUDE.md présent) ; erreur de système de fichiers = refus nommé ;
#   (B2) acceptations contrôlées en lecture seule avant toute écriture de la commande (controler_acceptations) ;
#   (NB) bloc accepté remplacé par un saut de ligne (ses voisins ne se recollent pas) ; `verifier` revalide chaque
#   acceptation journalisée (cellule, empreinte, chemins) et signale une acceptation caduque.
""")
src = remplacer(src, 'VERSION = "collisionneur-v9-v8g"', 'VERSION = "collisionneur-v9-v8h"')
src = remplacer(src, '''MOTIF_JETON_CHEMIN = re.compile(r"[\\w.\\-/]+")
''', '''MOTIF_JETON_CHEMIN = re.compile(r"[\\w.\\-/]+")
PONCTUATION_FINALE = ".-"
''')
src = remplacer(src, '''    motif = dict(MOTIFS_INTERDITS)[cat]
    jetons = []
    for m in motif.finditer(texte):
        if m.group(0) not in FORMES_RELATIVES:
            raise Arret(CODE_MOTIF, f"« {cat} » : une occurrence n'est pas un chemin relatif (forme non admise) ; "
                                    f"acceptation refusée")
        jeton = MOTIF_JETON_CHEMIN.match(texte, m.start()).group(0)
        if (RACINE_DEPOT / jeton).exists():
            raise Arret(CODE_MOTIF, f"« {cat} » : une occurrence nomme un chemin réel du dépôt ; acceptation refusée")
        jetons.append(jeton)''', '''    motif = dict(MOTIFS_INTERDITS)[cat]
    if not (RACINE_DEPOT / "CLAUDE.md").is_file():  # v9-v8h : racine du dépôt contrôlée
        raise Arret(CODE_MOTIF, "racine du dépôt introuvable depuis le script ; acceptation refusée")
    jetons = []
    for m in motif.finditer(texte):
        if m.group(0) not in FORMES_RELATIVES:
            raise Arret(CODE_MOTIF, f"« {cat} » : une occurrence n'est pas un chemin relatif (forme non admise) ; "
                                    f"acceptation refusée")
        jeton = MOTIF_JETON_CHEMIN.match(texte, m.start()).group(0)
        if not chemin_hors_depot(jeton):  # v9-v8h (B1)
            raise Arret(CODE_MOTIF, f"« {cat} » : une occurrence n'est pas un chemin relatif absent du dépôt (remontée, "
                                    f"composant vide ou entrée réelle) ; acceptation refusée")
        jetons.append(jeton)''')
src = remplacer(src, '''def accepter_motifs(dossier, specs):''', '''def chemin_hors_depot(jeton):
    """v9-v8h (B1) : vrai seulement si le jeton est « docs|runs|scripts/NOM[/…] », sans composant « . », « .. » ni vide
    (ponctuation finale retirée), et si NOM (sans casse, avec ou sans extension) ne nomme aucune entrée du dossier
    correspondant du dépôt. Erreur du système de fichiers : faux."""
    propre = jeton.rstrip(PONCTUATION_FINALE)
    composants = propre.split("/")
    if len(composants) < 2 or composants[0] + "/" not in FORMES_RELATIVES:
        return False
    if any(x in ("", ".", "..") for x in composants[1:]):
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
    return True


def controler_acceptations(dossier, specs):
    """v9-v8h (B2) : lecture seule ; contrôle chaque acceptation sur la cellule scellée et renvoie
    [(cellule, catégorie, empreinte, chemins)] ; Arret au premier refus, avant toute écriture de la commande."""
    neuves = []
    for spec in specs:
        cid, cat = lire_acceptation(spec)
        if cid not in cellules_du_run():
            raise Arret(CODE_USAGE, f"--accepter-motif : {cid} n'est pas une cellule de ce run ; rien n'est écrit")
        valide = cellule_valide(dossier, cid) if Path(dossier).exists() else None
        if not valide:
            raise Arret(CODE_USAGE, f"--accepter-motif : {cid} n'est pas une cellule valide ; rien n'est écrit")
        texte, h = valide
        neuves.append((cid, cat, h, formes_acceptables(texte, cat)))
    return neuves


def accepter_motifs(dossier, specs):''')
src = remplacer(src, '''    deja = {(e["cellule"], e["categorie"], e["sha256_cellule"]) for e in acceptations(dossier)}
    neuves = []
    for spec in specs:
        cid, cat = lire_acceptation(spec)
        if cid not in cellules_du_run():
            raise Arret(CODE_USAGE, f"--accepter-motif : {cid} n'est pas une cellule de ce run ; rien n'est écrit")
        valide = cellule_valide(dossier, cid)
        if not valide:
            raise Arret(CODE_USAGE, f"--accepter-motif : {cid} n'est pas une cellule valide ; rien n'est écrit")
        texte, h = valide
        neuves.append((cid, cat, h, formes_acceptables(texte, cat)))
    for cid, cat, h, jetons in neuves:''', '''    deja = {(e["cellule"], e["categorie"], e["sha256_cellule"]) for e in acceptations(dossier)}
    neuves = controler_acceptations(dossier, specs)  # v9-v8h : même contrôle, déjà passé avant les écritures
    for cid, cat, h, jetons in neuves:''')
src = remplacer(src, '''                t = t.replace(bloc_piece(e["cellule"], valide[0], valide[1]), "")''',
                '''                t = t.replace(bloc_piece(e["cellule"], valide[0], valide[1]), "\\n")  # v9-v8h : voisins séparés''')
src = remplacer(src, '''        verifier_cles()
        if etage == 1:''', '''        verifier_cles()
        if a.accepter_motif:  # v9-v8h (B2) : contenu contrôlé en lecture seule, avant toute écriture
            controler_acceptations(dossier, a.accepter_motif)
        if etage == 1:''')
src = remplacer(src, '''            problemes.append(f"{nom} : modèle servi {e['modele_servi']} au lieu de {JEV['id']}")
    return problemes
''', '''            problemes.append(f"{nom} : modèle servi {e['modele_servi']} au lieu de {JEV['id']}")
    for e in acceptations(dossier):  # v9-v8h : chaque acceptation revalidée
        valide = cellule_valide(dossier, e["cellule"])
        if not valide or valide[1] != e.get("sha256_cellule"):
            problemes.append(f"acceptation de motif caduque : {e['cellule']} (cellule absente ou changée)")
            continue
        try:
            if formes_acceptables(valide[0], e["categorie"]) != e.get("chemins"):
                problemes.append(f"acceptation de motif : {e['cellule']}, chemins différents du journal")
        except (Arret, KeyError) as x:
            problemes.append(f"acceptation de motif refusée à la revalidation : {e['cellule']} ({x})")
    return problemes
''')
(D / "collisionneur_v9_v8h.py").write_text(src, encoding="utf-8")
print("écrit", hashlib.sha256(src.encode()).hexdigest())
