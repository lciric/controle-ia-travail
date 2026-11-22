import sys  # noqa: E402 -- seul module chargé avant le crochet, dans le rôle du lanceur

"""Essai de la garde à l'exécution de G1, telle que la corrige l'erratum 1 de la conception v2
de l'étape 0 des tâches floues (point E1, avec E2). Bibliothèque standard et numpy seuls.

Rôle double. Sans argument : programme d'essai, qui écrit les témoins factices dans un dossier
temporaire, joue chaque cas dans un processus neuf (`python -I fichier --enfant CAS DOSSIER`)
et compare le code de sortie à l'attendu. Avec `--enfant` : le lanceur de l'expérimentateur,
dont la première instruction exécutée est la pose du crochet.

Règle éprouvée (erratum 1, point E1) :
  0. avant le crochet : racines admises lues sur sys seul ; écriture du code compilé coupée ;
  1. chargement : crochet posé, non armé ; `open` en lecture seule sous les racines admises ;
  2. préchargement de la liste fermée PRECHARGES, puis chargement du module des témoins ;
  3. échauffement : un tour complet (preparer, decider, conclure) de chaque témoin sur un lot
     d'essai sans vérité ; règles du chargement, et tout événement `import` lève le drapeau ;
     les réponses sont jetées ;
  4. armement : tout `open`, tout événement `os.`, `subprocess.`, `socket.`, `shutil.`, `ctypes.`,
     tout `import` lève le drapeau et une exception ; sortie au code 97.
Aucun appel payant, aucune vérité, aucun monde du banc.
"""

CODE_ARRET = 97
PRECHARGES = ("json", "math", "numpy", "numpy.random", "numpy.ma", "numpy.linalg")
PREFIXES_ARMES = ("os.", "subprocess.", "socket.", "shutil.", "ctypes.")


def _lanceur(cas, dossier):
    etat = {"phase": "chargement", "drapeau": None, "racines": ()}

    def lever(motif):
        if etat["drapeau"] is None:
            etat["drapeau"] = motif

    def lecture_seule(args):
        mode = args[1] if len(args) > 1 else "r"
        if isinstance(mode, str):
            return not any(c in mode for c in "wax+")
        if isinstance(mode, int):  # drapeaux de os.open
            return (mode & 3) == 0 and not (mode & 0o100)  # O_RDONLY, sans O_CREAT
        return False

    def sous_racine(chemin):
        if not isinstance(chemin, (str, bytes)):
            return False
        if isinstance(chemin, bytes):
            chemin = chemin.decode(errors="replace")
        return any(chemin == r or chemin.startswith(r + "/") for r in etat["racines"])

    def crochet(evt, args):
        phase = etat["phase"]
        if phase == "armee":
            if evt == "open" or evt == "import" or evt.startswith(PREFIXES_ARMES):
                lever(f"armé : {evt} {args[0] if args else ''}")
                raise RuntimeError("garde G1 : événement interdit après armement")
            return
        if evt == "open" and not (lecture_seule(args) and sous_racine(args[0])):
            lever(f"{phase} : open hors racines ou en écriture {args[0]!r}")
        if phase == "echauffement" and evt == "import":
            lever(f"échauffement : sous-module hors de la liste fermée {args[0]}")

    # Racines admises, lues sur sys seul (aucun module chargé) : préfixes de l'interpréteur,
    # entrées de sys.path qui sont sous ces préfixes, dossier de l'expérimentateur.
    prefixes = {sys.prefix, sys.base_prefix, sys.exec_prefix, sys.base_exec_prefix}
    racines = set(prefixes) | {dossier}
    racines |= {e for e in sys.path if e and any(e.startswith(r) for r in prefixes)}
    etat["racines"] = tuple(sorted(r.rstrip("/") for r in racines if r))
    sys.dont_write_bytecode = True  # sinon l'import du module des témoins écrit son .pyc : open en écriture
    sys.addaudithook(crochet)  # pose du crochet : avant tout chargement

    liste = PRECHARGES
    if cas == "liste_sans_numpy_ma":  # artefact : la liste fermée oublie un sous-module employé
        liste = tuple(m for m in PRECHARGES if m != "numpy.ma")
    if cas == "sans_prechargement":  # rappel de l'erreur E1 : la règle de la v2 seule
        liste = ("json", "math", "numpy")
    for nom in liste:
        __import__(nom)

    import json
    import importlib.util
    nom_temoin = {"sain": "temoin_sain", "liste_sans_numpy_ma": "temoin_sain",
                  "sans_prechargement": "temoin_sain", "import_neuf": "temoin_import_neuf",
                  "fromfile": "temoin_fromfile"}[cas]
    chemin = f"{dossier}/{nom_temoin}.py"
    spec = importlib.util.spec_from_file_location(nom_temoin, chemin)
    temoin = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(temoin)

    def tour(lot):
        temoin.preparer(lot["etalonnage"], lot["K_servi"], lot["budget_ouvertures"], lot["graine_temoin"])
        rep2 = temoin.decider(lot["mesure"], lot["service"])
        ouv = {i: False for i in rep2["demandes_ouverture"]}
        rep3 = temoin.conclure(ouv)
        return rep2, rep3

    def lot_factice(graine, n):
        ids = [f"t{i:04d}" for i in range(n)]
        rel = {"conclusion": 0, "affirmations": [0, 0, 0, 0], "controles": [0, 0, 0, 0], "forme": 0}
        tache = lambda i: {"id": i, "releve_suspect": rel, "releves_jumeau": [rel] * 8}  # noqa: E731
        return {"etalonnage": [tache(i) for i in ids[: n // 2]], "mesure": [tache(i) for i in ids[n // 2:]],
                "service": [], "K_servi": 8, "budget_ouvertures": 4, "graine_temoin": graine}

    def sortir_si_drapeau():
        if etat["drapeau"] is not None:
            sys.stderr.write(f"garde G1, arrêt : {etat['drapeau']}\n")
            sys.stderr.flush()
            sys.exit(CODE_ARRET)

    sortir_si_drapeau()
    etat["phase"] = "echauffement"
    try:
        tour(lot_factice([0, 0, 0, 0], 12))  # lot d'essai sans vérité ; réponses jetées
    except RuntimeError:
        pass
    sortir_si_drapeau()

    lot = json.loads(sys.stdin.readline())  # lu avant l'armement : la lecture de l'entrée n'ouvre rien
    etat["phase"] = "armee"
    try:
        rep2, rep3 = tour(lot)
    except Exception:  # le témoin a pu rattraper ou non : seul le drapeau décide
        rep2 = rep3 = None
    sortir_si_drapeau()
    etat["phase"] = "fin"
    sys.stdout.write(json.dumps({"temps2": rep2, "temps3": rep3}, sort_keys=True) + "\n")
    sys.exit(0)


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "--enfant":
    _lanceur(sys.argv[2], sys.argv[3])

# ------------------------------------------------------------------ programme d'essai
import ast  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import platform  # noqa: E402
import subprocess  # noqa: E402
import tempfile  # noqa: E402

TEMOIN_COMMUN = '''
import numpy

_etat = {}


def preparer(etalonnage, K_servi, budget_ouvertures, graine_temoin):
    _etat["rng"] = numpy.random.default_rng(numpy.random.SeedSequence(graine_temoin))
    _etat["budget"] = budget_ouvertures


def _decisions(mesure, service):
    piece = int(_etat["rng"].integers(0, 2))          # le témoin tire une pièce
    concl = numpy.unique([t["releve_suspect"]["conclusion"] for t in mesure])   # charge numpy.ma à la demande
    d = {t["id"]: ("accepter" if (piece + int(concl[0])) % 2 == 0 else "refaire") for t in mesure + service}
    return d
'''

TEMOINS = {
    "temoin_sain": TEMOIN_COMMUN + '''

def decider(mesure, service):
    _etat["d"] = _decisions(mesure, service)
    return {"decisions": _etat["d"], "demandes_ouverture": [t["id"] for t in mesure][: _etat["budget"]]}


def conclure(reponses_ouverture):
    return {"decisions_finales": _etat["d"], "bornes": ["muette"], "abstention_declaree": False}
''',
    # Artefact « import neuf » : un chemin que l'échauffement n'exerce pas (lot de plus de 12 tâches)
    # touche numpy.polynomial, chargé à la demande par un attribut, sans aucun import écrit.
    "temoin_import_neuf": TEMOIN_COMMUN + '''

def decider(mesure, service):
    _etat["d"] = _decisions(mesure, service)
    if len(mesure) > 6:
        numpy.polynomial.polynomial.polyval(1.0, [1.0, 2.0])
    return {"decisions": _etat["d"], "demandes_ouverture": []}


def conclure(reponses_ouverture):
    return {"decisions_finales": _etat["d"], "bornes": ["muette"], "abstention_declaree": False}
''',
    # Artefact E2 : sans import ni nom refusé, le temps « decider » lit son propre fichier source.
    "temoin_fromfile": TEMOIN_COMMUN + '''

def decider(mesure, service):
    _etat["d"] = _decisions(mesure, service)
    if len(mesure) > 6:
        numpy.fromfile(__file__, dtype=numpy.uint8)
    return {"decisions": _etat["d"], "demandes_ouverture": []}


def conclure(reponses_ouverture):
    return {"decisions_finales": _etat["d"], "bornes": ["muette"], "abstention_declaree": False}
''',
}

NOMS_REFUSES = {"open", "__import__", "eval", "exec", "compile", "importlib", "os", "sys", "subprocess",
                "socket", "ctypes", "pathlib", "io", "builtins"}


def controle_statique(source):
    """Contrôle statique de G1 (conception v2 § 7), resserré par l'erratum : sous-modules de numpy
    admis seulement s'ils sont dans la liste fermée."""
    admis = set(PRECHARGES)
    for noeud in ast.walk(ast.parse(source)):
        if isinstance(noeud, ast.Import):
            for a in noeud.names:
                if a.name not in admis:
                    return f"import refusé {a.name}"
        elif isinstance(noeud, ast.ImportFrom):
            if (noeud.module or "") not in admis:
                return f"import refusé {noeud.module}"
        elif isinstance(noeud, ast.Name) and noeud.id in NOMS_REFUSES:
            return f"nom refusé {noeud.id}"
        elif isinstance(noeud, ast.Attribute) and noeud.attr in NOMS_REFUSES:
            return f"nom refusé {noeud.attr}"
    return None


CAS = [
    # (cas, code attendu, motif attendu dans l'erreur, ce qu'il éprouve)
    ("sain", 0, None, "cas sain : pièce tirée et numpy.unique, préchargement puis échauffement"),
    ("import_neuf", CODE_ARRET, "armé : import numpy.polynomial",
     "artefact : import neuf après armement (numpy.polynomial, par un attribut)"),
    ("fromfile", CODE_ARRET, "armé : open", "artefact E2 : numpy.fromfile(__file__, dtype=numpy.uint8) après armement"),
    ("liste_sans_numpy_ma", CODE_ARRET, "échauffement : sous-module hors de la liste fermée numpy.ma",
     "artefact : liste fermée sans numpy.ma, vu à l'échauffement, avant la lecture du lot"),
    ("sans_prechargement", CODE_ARRET, "échauffement : sous-module hors de la liste fermée numpy.random",
     "rappel de E1 : sans préchargement, un témoin conforme est arrêté (ici dès l'échauffement)"),
]


def lot_du_banc_simule():
    """Lot d'essai de 40 tâches, champs constants : aucune vérité, aucun monde."""
    rel = {"conclusion": 1, "affirmations": [0, 1, 0, 1], "controles": [1, 0, 0, 0], "forme": 1}
    t = lambda i: {"id": f"u{i:04d}", "releve_suspect": rel, "releves_jumeau": [rel] * 8}  # noqa: E731
    return {"etalonnage": [t(i) for i in range(20)], "mesure": [t(i) for i in range(20, 40)], "service": [],
            "K_servi": 8, "budget_ouvertures": 4, "graine_temoin": [11, 22, 33, 44]}


def principal():
    import numpy
    print("Essai de la garde G1 à l'exécution, erratum 1 de la conception v2 (étape 0, tâches floues)")
    print(f"python {platform.python_version()} ; numpy {numpy.__version__}")
    print(f"liste fermée préchargée : {', '.join(PRECHARGES)}")
    print()
    print("Contrôle statique (les artefacts doivent le passer : c'est la garde à l'exécution qui les voit)")
    for nom, src in TEMOINS.items():
        print(f"  {nom:22s} : {controle_statique(src) or 'admis'}")
    print()
    echecs = 0
    with tempfile.TemporaryDirectory() as d:
        for nom, src in TEMOINS.items():
            with open(os.path.join(d, nom + ".py"), "w", encoding="utf-8") as f:
                f.write(src)
        entree = json.dumps(lot_du_banc_simule()) + "\n"
        for cas, attendu, motif_attendu, quoi in CAS:
            p = subprocess.run([sys.executable, "-I", os.path.abspath(__file__), "--enfant", cas, d],
                               input=entree, capture_output=True, text=True, timeout=120, env={})
            motif = p.stderr.strip().splitlines()[-1] if p.stderr.strip() else "-"
            motif = motif.replace(d, "<dossier temporaire>")  # sortie identique d'un rejeu à l'autre
            ok = p.returncode == attendu and (motif_attendu is None and motif == "-"
                                              or motif_attendu is not None and motif_attendu in motif)
            echecs += not ok
            print(f"[{'conforme' if ok else 'ÉCHEC'}] {quoi}")
            print(f"    code {p.returncode} (attendu {attendu}) ; erreur : {motif}")
            if p.returncode == 0:
                r = json.loads(p.stdout)
                print(f"    réponse : {len(r['temps2']['decisions'])} décisions, "
                      f"{len(r['temps2']['demandes_ouverture'])} ouvertures demandées")
    print()
    print("VERDICT : " + ("tous les cas sont conformes" if echecs == 0 else f"{echecs} cas en échec"))
    return 0 if echecs == 0 else 1


if __name__ == "__main__":
    sys.exit(principal())
