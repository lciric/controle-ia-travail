"""Fabrique collisionneur_v9_v8g.py depuis la v8d par remplacements exacts."""
import hashlib, sys
from pathlib import Path
D = Path("/home/user/controle-ia-travail/docs/notes/collisionneur-v9")
src = (D / "collisionneur_v9_v8d.py").read_text(encoding="utf-8")
assert hashlib.sha256(src.encode()).hexdigest() == "b780383874598f12b24c79e4087d335c8e01cda685e295f5116898fa3b1715ac"

def remplacer(t, ancien, nouveau):
    n = t.count(ancien)
    if n != 1:
        sys.exit(f"ancien texte trouvé {n} fois : {ancien[:80]!r}")
    return t.replace(ancien, nouveau)

src = remplacer(src, """#   rapport-developpeur-collisionneur-v9-v8d-v1.md, même dossier.
\"\"\"Collisionneur""", """#   rapport-developpeur-collisionneur-v9-v8d-v1.md, même dossier.
# v9-v8g (développeur, Claude Opus 5.5, 22 novembre 2026, décision de la mère du 22 novembre 08:34Z sur le refus de la
#   garde de motifs du dossier du tirage au hasard) : copie du v9-v8d (b7803838…, inchangé, R12), et NON de la v8e ni de
#   la v8f (balises des duels, non servies aux dossiers en cours). Changement, et seulement celui-là : --accepter-motif
#   CELLULE:CATÉGORIE, acceptation nommée par l'arbitre d'un faux positif établi de la garde de motifs, journalisée
#   (decision « motif_accepte »). Seule la catégorie « chemin interne » est admise, et seulement si chaque occurrence
#   dans la cellule scellée est un chemin relatif (forme docs/, runs/ ou scripts/, écrite par le modèle) qui n'existe
#   pas dans le dépôt. L'acceptation ne vaut que pour le bloc de cette cellule, tel que scellé (empreinte journalisée) :
#   ailleurs dans l'invite (faits, question, autres pièces), la garde reste entière ; les autres catégories aussi.
#   `verifier` et le devis de reprise appliquent la même règle. Détail : rapport-developpeur-collisionneur-v9-v8g-v1.md.
\"\"\"Collisionneur""")
src = remplacer(src, 'VERSION = "collisionneur-v9-v8d"', 'VERSION = "collisionneur-v9-v8g"')

src = remplacer(src, """def garder_motifs(dossier, quoi, texte):
    \"\"\"Lève Arret(CODE_MOTIF) si un motif interdit est dans le texte à envoyer ; consigne le refus au journal.\"\"\"
    trouves = motifs_trouves(texte)
""", """# ---------- v9-v8g : acceptation nommée d'un faux positif de la garde de motifs ----------
CATEGORIES_ACCEPTABLES = ("chemin interne",)
FORMES_RELATIVES = ("docs/", "runs/", "scripts/")
RACINE_DEPOT = Path(__file__).resolve().parents[3]
MOTIF_JETON_CHEMIN = re.compile(r"[\\w.\\-/]+")


def lire_acceptation(spec):
    \"\"\"« CELLULE:CATÉGORIE » ; forme contrôlée avant toute écriture ; Arret sinon.\"\"\"
    cid, sep, cat = str(spec).partition(":")
    if not sep or cat not in CATEGORIES_ACCEPTABLES:
        raise Arret(CODE_USAGE, f"--accepter-motif CELLULE:CATÉGORIE, catégorie parmi {list(CATEGORIES_ACCEPTABLES)} : "
                                f"{spec!r} refusé ; rien n'est écrit")
    return cid, cat


def formes_acceptables(texte, cat):
    \"\"\"Renvoie les chemins (jetons) de la catégorie dans le texte si chacun est une forme relative absente du dépôt ;
    lève Arret sinon (aucune occurrence, forme absolue ou interne, ou chemin réel du dépôt).\"\"\"
    motif = dict(MOTIFS_INTERDITS)[cat]
    jetons = []
    for m in motif.finditer(texte):
        if m.group(0) not in FORMES_RELATIVES:
            raise Arret(CODE_MOTIF, f"« {cat} » : une occurrence n'est pas un chemin relatif (forme non admise) ; "
                                    f"acceptation refusée")
        jeton = MOTIF_JETON_CHEMIN.match(texte, m.start()).group(0)
        if (RACINE_DEPOT / jeton).exists():
            raise Arret(CODE_MOTIF, f"« {cat} » : une occurrence nomme un chemin réel du dépôt ; acceptation refusée")
        jetons.append(jeton)
    if not jetons:
        raise Arret(CODE_MOTIF, f"« {cat} » : aucune occurrence dans la cellule ; acceptation sans objet, refusée")
    return jetons


def accepter_motifs(dossier, specs):
    \"\"\"Contrôle chaque acceptation sur la cellule scellée, puis la journalise (une fois par cellule, catégorie et
    empreinte).\"\"\"
    deja = {(e["cellule"], e["categorie"], e["sha256_cellule"]) for e in acceptations(dossier)}
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
    for cid, cat, h, jetons in neuves:
        if (cid, cat, h) not in deja:
            ajouter_journal(dossier, {"decision": "motif_accepte", "cellule": cid, "categorie": cat,
                                      "sha256_cellule": h, "chemins": jetons, "quand": maintenant(), "script": VERSION})


def acceptations(dossier):
    if dossier is None or not (Path(dossier) / "journal.jsonl").exists():
        return []
    return [e for e in lire_journal(dossier) if e.get("decision") == "motif_accepte"]


def motifs_trouves_dossier(dossier, texte):
    \"\"\"v9-v8g : motifs_trouves, sauf, pour une catégorie acceptée, dans le bloc exact de la cellule acceptée (texte et
    empreinte scellés, identiques à ceux de l'acceptation).\"\"\"
    acc = acceptations(dossier)
    if not acc:
        return motifs_trouves(texte)
    trouves = []
    for nom, motif in MOTIFS_INTERDITS:
        t = texte
        for e in acc:
            if e["categorie"] != nom:
                continue
            valide = cellule_valide(dossier, e["cellule"])
            if valide and valide[1] == e["sha256_cellule"]:
                t = t.replace(bloc_piece(e["cellule"], valide[0], valide[1]), "")
        m = motif.search(t)
        if m:
            trouves.append((nom, m.start()))
    return trouves


def garder_motifs(dossier, quoi, texte):
    \"\"\"Lève Arret(CODE_MOTIF) si un motif interdit est dans le texte à envoyer ; consigne le refus au journal.
    v9-v8g : hors des blocs des cellules acceptées par l'arbitre (--accepter-motif).\"\"\"
    trouves = motifs_trouves_dossier(dossier, texte)
""")
src = remplacer(src, """        if motifs_trouves(prompt):  # v9
            problemes.append(f"{nom} : motif interdit dans le prompt envoyé")""",
"""        if motifs_trouves_dossier(dossier, prompt):  # v9 ; v9-v8g : acceptations de l'arbitre
            problemes.append(f"{nom} : motif interdit dans le prompt envoyé")""")
src = remplacer(src, """                             "motifs": motifs_trouves(prompt) if tour == "E3-T2" else None})""",
"""                             "motifs": motifs_trouves_dossier(dossier, prompt) if tour == "E3-T2" else None})""")
src = remplacer(src, """    refus = [e for e in lire_journal(dossier) if "refus_motifs" in e]
    if refus:  # v9
        lignes.append(f"Refus de la garde de motifs : {len(refus)} (catégories et positions au journal).")""",
"""    refus = [e for e in lire_journal(dossier) if "refus_motifs" in e]
    if refus:  # v9
        lignes.append(f"Refus de la garde de motifs : {len(refus)} (catégories et positions au journal).")
    acc = acceptations(dossier)
    if acc:  # v9-v8g
        lignes.append("Motifs acceptés par l'arbitre : " + ", ".join(f"{e['cellule']} ({e['categorie']})" for e in acc)
                      + ".")""")
src = remplacer(src, """        s.add_argument("--accepter-absence", action="append", default=[])""",
"""        s.add_argument("--accepter-absence", action="append", default=[])
        s.add_argument("--accepter-motif", action="append", default=[],  # v9-v8g
                       help="CELLULE:CATÉGORIE : faux positif établi de la garde de motifs, accepté par l'arbitre ; "
                            "seule « chemin interne », chemins relatifs absents du dépôt ; journalisé")""")
src = remplacer(src, """        rejuger = [lire_rejugement(x) for x in a.rejuger_essai]""",
"""        for x in a.accepter_motif:  # v9-v8g : forme contrôlée avant toute écriture
            lire_acceptation(x)
        rejuger = [lire_rejugement(x) for x in a.rejuger_essai]""")
src = remplacer(src, """        consigner_absences(dossier, a.accepter_absence)
""", """        consigner_absences(dossier, a.accepter_absence)
        accepter_motifs(dossier, a.accepter_motif)  # v9-v8g
""")
(D / "collisionneur_v9_v8g.py").write_text(src, encoding="utf-8")
print("écrit", hashlib.sha256(src.encode()).hexdigest())
