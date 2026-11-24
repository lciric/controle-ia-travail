"""Garde de neutralité par motifs pour la question fusionnée servie à l'organisme d'idéation (v1).

Classe B (instrument). Deux familles de motifs :
  (1) les motifs du collisionneur v9 (noms de personne, identifiants de session, courriels, chemins internes,
      identifiants d'accord et de registre), importés tels quels de collisionneur_v9_v8d.py, sans copie ;
  (2) le vocabulaire propre au programme, qui dévoilerait son identité ou ses étiquettes internes à un lecteur
      aveugle (noms de modèles et d'outils internes, noms de chantiers, codes de portes, de tâches et de nœuds).
Un motif trouvé : refus nommé (catégorie et position), rien n'est retiré du texte. Code de sortie 0 si sain, 3 sinon.
Usage : python garde_neutralite_question_fusionnee_v1.py FICHIER... ; --essai joue les témoins positifs et négatifs.
"""
import importlib.util
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
COLLISIONNEUR = ICI.parent / "collisionneur-v9" / "collisionneur_v9_v8d.py"


def _charger_motifs_collisionneur():
    spec = importlib.util.spec_from_file_location("collisionneur_v9_v8d", COLLISIONNEUR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return tuple(mod.MOTIFS_INTERDITS)


MOTIFS_PROGRAMME = (
    ("nom de modèle ou d'espèce interne", re.compile(
        r"(?i)(?<![^\W_])(?:fable|opus|sonnet|haiku|carbon|neon|argon|astra|minuit|jev|kimi|mistral|gemini|claude|"
        r"anthropic|gpt-?\d)(?![^\W_])")),
    ("nom de chantier interne", re.compile(
        r"(?i)plan\s+turing|organisme\s+d['’]id[ée]ation|collisionneur|protocole\s+x\b|attelage|"
        r"chef\s+d['’]orchestre|veille\s+de\s+cap|biblioth[ée]caire|session\s+(?:m[èe]re|fille)")),
    ("code interne de porte, tâche, nœud ou lot", re.compile(
        r"(?<![\w-])(?:G[0-3]|T0\.\d+|N-\d{3}|P-\d{3}|D-S\d+|IDE-\d{4}|HC\d|H\d{1,2}[ab]?|E\d\.\d|lot\s+\d+|"
        r"classe\s+[ABC])(?![\w])")),
    ("étiquette de procédure interne", re.compile(
        r"(?i)pr[ée]enregistrement\s+scell[ée]|scellement|empreinte\s+sha|\.sha256\b|\bdevis\b|"
        r"contre-lecture|passation")),
)


def motifs():
    return _charger_motifs_collisionneur() + MOTIFS_PROGRAMME


def trouver(texte):
    """[(catégorie, position)] : une entrée par catégorie trouvée ; vide si le texte est sain."""
    sortie = []
    for nom, motif in motifs():
        m = motif.search(texte)
        if m:
            sortie.append((nom, m.start()))
    return sortie


TEMOINS_POSITIFS = {
    "nom de personne": "Le directeur Lazar demande ceci.",
    "identifiant de session": "voir session_01Qi7Gr36UCZKS2Fw574dmcW",
    "identifiant de session (forme UUID)": "id 93f3198b-243e-5860-91a6-040e40668f34",
    "courriel": "écrire à quelqu'un@exemple.org",
    "chemin interne": "lire docs/notes/attelage/x.md",
    "identifiant d'accord": "sous GO-2026-11-24-42",
    "identifiant de registre": "consigné en R-5361",
    "nom de modèle ou d'espèce interne": "réponse de Carbon au tour 2",
    "nom de chantier interne": "le plan Turing prévoit",
    "code interne de porte, tâche, nœud ou lot": "avant la porte G1 et la tâche T0.7",
    "étiquette de procédure interne": "un préenregistrement scellé fixe",
}
TEMOINS_NEGATIFS = (
    "Proposez des expériences réfutables sur des mondes synthétiques à loi plantée.",
    "Comparez au tirage uniforme et à un énumérateur par longueur de description, à coût égal.",
    "La détection séquentielle sous référence honnête finie et contaminée reste ouverte.",
    "Un graphe de concepts daté sert de rétrodiction à étanchéité temporelle.",
)


def essai():
    cats = {nom for nom, _ in motifs()}
    manquants = cats - set(TEMOINS_POSITIFS)
    if manquants:
        print("ÉCHEC : catégories sans témoin positif :", sorted(manquants))
        return 1
    ok = True
    for cat, texte in TEMOINS_POSITIFS.items():
        trouves = {c for c, _ in trouver(texte)}
        etat = "détecté" if cat in trouves else "MANQUÉ"
        ok &= cat in trouves
        print(f"positif  [{cat}] : {etat}")
    for texte in TEMOINS_NEGATIFS:
        t = trouver(texte)
        ok &= not t
        print(f"négatif  : {'sain' if not t else 'FAUSSE ALERTE ' + str(t)}")
    print("ESSAI", "RÉUSSI" if ok else "ÉCHOUÉ")
    return 0 if ok else 1


def main(argv):
    if argv[1:2] == ["--essai"]:
        return essai()
    code = 0
    for chemin in argv[1:]:
        t = trouver(pathlib.Path(chemin).read_text(encoding="utf-8"))
        print(f"{chemin} : {'sain' if not t else 'REFUS ' + '; '.join(f'{c} @ {p}' for c, p in t)}")
        if t:
            code = 3
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
