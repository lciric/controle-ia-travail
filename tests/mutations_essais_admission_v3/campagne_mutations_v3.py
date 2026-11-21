"""Campagne de mutations par outil des essais d'admission du bras A (chef `_v7`, relais de Google `_v7`) — version 3.

Repris de l'outil de la livraison 5 (bloc-notes de session, `mut/campagne.py`, 91 mutants tués sur 91 sur les `_v4`),
versé au dépôt à la livraison 6 (version 1, sur `_v5`), repris à la livraison 7 (version 2, sur `_v6`) et à la livraison 8 sur les fichiers `_v7`. Mutations : chaque comparaison retournée, chaque « et »
échangé avec « ou », chaque « non » retiré, chaque constante entière augmentée de un, chaque arrêt retiré, chaque
retour remplacé par rien. Une seule mutation à la fois ; le mutant remplace la fonction en mémoire (greffon
`greffe_mutant_v3.py`), aucun fichier du dépôt n'est modifié. Un mutant est tué si un essai du sous-ensemble échoue.

Quatre campagnes :
- `regle_google` : la campagne de la livraison 5, rejouée sur `_v7` (six fonctions de la règle Google) ;
- `livraison6` : les fonctions neuves ou changées de la livraison 6 (constat par fournisseur, taux et fixage,
  borne de réflexion) ;
- `livraison7` : le régime fermé de Google (R-1) et la garde 10 qui le lit ;
- `livraison8` : la température retirée d'avance, la suite de la vérification, la dépense de Mistral depuis le
  constat.

Commande, depuis la racine du dépôt, sans clé dans l'environnement :

    env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 \\
        .venv/bin/python -I tests/mutations_essais_admission_v3/campagne_mutations_v3.py regle_google|livraison6|livraison7|livraison8|toutes [SORTIE.json]

`compter` à la place du nom donne le nombre de mutants. Les fichiers de mutants vivent dans un dossier temporaire,
hors du dépôt ; les résultats vont à SORTIE.json (par défaut, dans ce dossier temporaire, dont le chemin est
imprimé). Les essais sont lancés sans réseau, contre le faux fournisseur local, comme la commande d'essai."""
import ast
import concurrent.futures as cf
import copy
import json
import os
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
CHEF = "scripts/chef_essais_admission_bras_a_v7.py"
RELAIS_GOOGLE = "scripts/relais_google_essais_admission_v7.py"
ESSAIS_FICHIER = "tests/test_chef_essais_admission_bras_a_v7.py"
CAMPAGNES = {
    "regle_google": {
        "cibles": [("chef", CHEF, f) for f in ("garde_google_avant_envoi", "defaut_de_reponse_google", "borne_dementie",
                                               "reglage_de_reflexion", "controler_la_configuration_de_google")]
                  + [("relais_google", RELAIS_GOOGLE, "defaut_du_corps")],
        "essais": "regle_google or c2_l5 or m3_l5 or m2_l5 or gabarit_complet or garde_3_corps or reflexion_l6 or debit_requis_l6"},
    "livraison6": {
        "cibles": [("chef", CHEF, f) for f in ("portee_du_constat", "lire_constat", "pieces_de_constat", "garde_constat",
                                               "resume_du_constat", "age_max_du_fixage", "lire_taux")],
        "essais": "garde_9 or l6 or l7 or credit or taux or garde_20 or definitive or m5_l5 or a_blanc or recharge"},
    "livraison7": {
        "cibles": [("chef", CHEF, f) for f in ("regime_file_google", "garde_cle_verifiee")],
        "essais": "garde_10 or l7 or l8 or regle_google or sonde or bout_en_bout or a_blanc"},
    "livraison8": {
        "cibles": [("chef", CHEF, f) for f in ("temperature_retiree_d_avance", "suite_de_la_verification",
                                               "depense_de_mistral_depuis_le_constat")],
        "essais": "l8 or garde_16 or garde_3 or garde_10 or temperature or bout_en_bout_verification_puis_file_mistral"},
}
INVERSE = {ast.Lt: ast.LtE, ast.LtE: ast.Lt, ast.Gt: ast.GtE, ast.GtE: ast.Gt, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq,
           ast.Is: ast.IsNot, ast.IsNot: ast.Is, ast.In: ast.NotIn, ast.NotIn: ast.In}
VARIABLES_RETIREES = ("MISTRAL_API_KEY", "GEMINI_API_KEY", "GEMINI_API_KEY_2", "OPENAI_API_KEY_2", "GO_ID")


def mutants(fonction: ast.FunctionDef):
    noeuds = list(ast.walk(fonction))
    for i, n in enumerate(noeuds):
        def avec(change, nom):
            arbre = copy.deepcopy(fonction)
            cible = list(ast.walk(arbre))[i]
            if change(cible) is not False:
                yield nom, ast.unparse(ast.fix_missing_locations(arbre))
        ligne = getattr(n, "lineno", 0)
        if isinstance(n, ast.Compare):
            for k, op in enumerate(n.ops):
                if type(op) in INVERSE:
                    def c(x, k=k): x.ops[k] = INVERSE[type(x.ops[k])]()
                    yield from avec(c, f"l{ligne} comparaison {type(op).__name__}→{INVERSE[type(op)].__name__}")
        elif isinstance(n, ast.BoolOp):
            def c(x): x.op = ast.Or() if isinstance(x.op, ast.And) else ast.And()
            yield from avec(c, f"l{ligne} et↔ou")
        elif isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.Not):
            def c(x):
                x.__class__ = ast.Call
                x.func, x.args, x.keywords = ast.Name("bool", ast.Load()), [x.operand], []
            yield from avec(c, f"l{ligne} « non » retiré")
        elif isinstance(n, ast.Constant) and type(n.value) is int:
            def c(x): x.value = x.value + 1
            yield from avec(c, f"l{ligne} constante {n.value}→{n.value + 1}")
        elif isinstance(n, ast.Raise):
            def c(x): x.__class__ = ast.Pass; x.__dict__ = {"lineno": x.lineno, "col_offset": x.col_offset}
            yield from avec(c, f"l{ligne} arrêt retiré")
        elif isinstance(n, ast.Return) and n.value is not None and not (isinstance(n.value, ast.Constant) and n.value.value is None):
            def c(x): x.value = ast.Constant(None)
            yield from avec(c, f"l{ligne} retour → None")


def jouer(tache):
    numero, objet, fonction, nom, source, essais, dossier = tache
    chemin = os.path.join(dossier, f"mutant-{numero}.json")
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump({"objet": objet, "fonction": fonction, "nom": nom, "source": source}, f)
    env = {k: v for k, v in os.environ.items() if k not in VARIABLES_RETIREES}
    env.update({"PYTHONPATH": os.pathsep.join(("src", ICI)), "MUTANT": chemin, "PYTHONDONTWRITEBYTECODE": "1"})
    try:
        r = subprocess.run([os.path.join(RACINE, ".venv/bin/python"), "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider",
                            "-p", "greffe_mutant_v3", ESSAIS_FICHIER, "-k", essais], cwd=RACINE, env=env,
                           capture_output=True, text=True, timeout=300)
        issue = "survit" if r.returncode == 0 else "tué" if r.returncode == 1 else f"erreur {r.returncode}"
    except subprocess.TimeoutExpired:
        issue = "tué (délai)"
    os.remove(chemin)
    return objet, fonction, nom, issue


def taches_de(nom_campagne: str, dossier: str) -> list:
    campagne, taches = CAMPAGNES[nom_campagne], []
    for objet, fichier, nom_f in campagne["cibles"]:
        with open(os.path.join(RACINE, fichier), encoding="utf-8") as f:
            arbre = ast.parse(f.read())
        fonction = next(n for n in arbre.body if isinstance(n, ast.FunctionDef) and n.name == nom_f)
        fonction.body = [s for k, s in enumerate(fonction.body)
                         if not (k == 0 and isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant))]
        vus = set()
        for nom, source in mutants(fonction):
            if source not in vus and source != ast.unparse(fonction):
                vus.add(source)
                taches.append((len(taches), objet, nom_f, f"{nom_campagne} : {nom}", source, campagne["essais"], dossier))
    return taches


def principal(argv) -> int:
    if not argv or argv[0] not in (*CAMPAGNES, "toutes", "compter"):
        print(__doc__)
        return 2
    dossier = tempfile.mkdtemp(prefix="mutations-essais-admission-")
    noms = list(CAMPAGNES) if argv[0] in ("toutes", "compter") else [argv[0]]
    taches = [t for n in noms for t in taches_de(n, dossier)]
    taches = [(i, *t[1:]) for i, t in enumerate(taches)]
    if argv[0] == "compter":
        for n in noms:
            print(n, sum(1 for t in taches if t[3].startswith(n + " :")))
        return 0
    with cf.ThreadPoolExecutor(4) as bassin:
        resultats = list(bassin.map(jouer, taches))
    sortie = argv[1] if len(argv) > 1 else os.path.join(dossier, "resultats.json")
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(resultats, f, ensure_ascii=False, indent=1)
    par = {}
    for objet, fonction, nom, issue in resultats:
        par.setdefault((nom.split(" :")[0], fonction), []).append(issue)
    for (campagne, fonction), issues in par.items():
        print(campagne, fonction, len(issues), "mutants ;", sum(1 for i in issues if i.startswith("tué")), "tués ;",
              sum(1 for i in issues if i == "survit"), "survivants ;", sum(1 for i in issues if i.startswith("erreur")), "erreurs")
    for objet, fonction, nom, issue in resultats:
        if not issue.startswith("tué"):
            print("  ", fonction, "|", nom, "|", issue)
    print("total", len(resultats), "; tués", sum(1 for r in resultats if r[3].startswith("tué")), "; résultats :", sortie)
    return 0 if all(r[3].startswith("tué") for r in resultats) else 1


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
