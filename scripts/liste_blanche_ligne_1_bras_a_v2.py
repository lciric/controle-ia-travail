"""Liste blanche des fichiers à poser sur l'instance de la ligne 1 de carte du bras A, version 2 (23 novembre 2026 ; la
version 1, `scripts/liste_blanche_ligne_1_bras_a_v1.py`, reste telle quelle).

Différences avec la version 1 : le programme de la course est la version 2 (`scripts/course_ligne_1_bras_a_v2.py`),
le lanceur désigné est la v8 et la configuration la v2 ; le guide d'invite de la configuration (« H1-classification »)
est **ajouté** par ses deux fichiers (l'invite et l'index des invites), chacun avec son compagnon, **à leurs empreintes
données** par la configuration et par les constantes du lanceur v8 (`EMPREINTE_DU_GUIDE`,
`EMPREINTE_DE_L_INDEX_DU_GUIDE`) : ce programme **ne lit, n'ouvre, ne liste ni n'empreinte** ces fichiers (chemin
cloisonné pour la session qui l'a écrit) ; il les déclare avec l'empreinte attendue, que la session qui pose les
fichiers confronte à la copie, et que le programme de la course revérifie sur l'instance avant de charger le guide.
Ces quatre chemins sont les seules exceptions admises au préfixe cloisonné `docs/sources/`, et seulement s'ils sont
exactement ceux du lanceur v8. Ce qui suit décrit la version 1.

Calculée par programme, sans rien importer de ce qu'elle liste : les modules du paquet `controle_ia` que le programme
de la course (`scripts/course_ligne_1_bras_a_v1.py`) et le lanceur désigné importent, **à toute profondeur, imports
placés dans les fonctions compris** (lecture de l'arbre syntaxique de chaque module, imports relatifs résolus), avec
les `__init__.py` de leurs paquets ; puis les fichiers de données que la course lit (configuration, texte scellé,
configuration de référence, les deux fichiers de tâches, plan scellé, chacun avec son compagnon `.sha256`). Chaque
chemin est confronté au cloisonnement (`cloisonnement_bras_a_v14.est_cloisonne`, plus les chemins cloisonnés de la
session) : un seul chemin cloisonné arrête. Les bibliothèques hors du paquet (torch, transformers, numpy…) ne sont
pas posées : elles viennent de l'image de l'instance, leurs versions vont au manifeste.

Le lanceur est importé par la course sous le nom tiré de son chemin (`importlib`) : il est ajouté ici par son chemin,
et ses imports suivis comme les autres. Le guide `H1-classification`, s'il est retenu, est lu sous `docs/sources/` :
ces fichiers ne sont **pas** ajoutés par ce programme (chemin cloisonné pour la session qui l'a écrit) ; la liste dit
qu'il en manque.

Usage : `PYTHONPATH=src python scripts/liste_blanche_ligne_1_bras_a_v1.py --configuration … --lanceur-chemin …
--plan-scelle …` ; écrit la liste (JSON) sur la sortie standard.
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

PAQUET = "controle_ia"
PROGRAMME_DE_LA_COURSE = "scripts/course_ligne_1_bras_a_v2.py"
LANCEUR_ATTENDU = "src/controle_ia/organismes_discrets/lanceur_bras_a_v8.py"
CONFIGURATION_ATTENDUE = "prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v2.json"
# Guide (v2) : chemins et empreintes donnés, recopiés des constantes du lanceur v8 (confrontés par les essais)
GUIDE_IDENTIFIANT = "H1-classification"
GUIDE_FICHIERS = (("docs/sources/invites-2606.08892-v1/invites/H1-classification.txt",
                   "69d50fb972f3255c94430205ab09c4f21054185d7def25b061c7255d71cc5540"),
                  ("docs/sources/invites-2606.08892-v1/index.json",
                   "adb4b8bca7788baf2c4714df96dcdcc2c5043e8f1943542d0fbe1863491ae2d9"))
# chemins cloisonnés de la session, en plus de ceux de la garde statique (préfixes relatifs à la racine, ou fragments)
PREFIXES_CLOISONNES = ("bases/", "sondes/", "runs/", "registres/", "docs/sources/", "archives-reponses-modeles/",
                       "docs/notes/bras-a-moniteurs-v1/", "docs/notes/bras-a-contre-lecture-habilitee-v1/",
                       "docs/notes/bras-a-sans-interne-v1/", "prereg/T0.6-organismes-v0-v1.md", "scripts/mots_et_cout_")
FRAGMENTS_CLOISONNES = ("consigne-privee", "conception-ii-b", "autres_moniteurs_v", "bras_a_v2_habilite")


class Refus(Exception):
    pass


def _module_vers_chemin(racine: Path, module: str) -> str | None:
    """`controle_ia.a.b` → `src/controle_ia/a/b.py` ou `src/controle_ia/a/b/__init__.py` ; None hors du paquet."""
    if module != PAQUET and not module.startswith(PAQUET + "."):
        return None
    base = "src/" + module.replace(".", "/")
    if (racine / (base + ".py")).is_file():
        return base + ".py"
    if (racine / base / "__init__.py").is_file():
        return base + "/__init__.py"
    raise Refus(f"module {module} introuvable sous {racine}/src")


def _chemin_vers_module(chemin: str) -> tuple[str, bool]:
    """`src/controle_ia/a/b.py` → (`controle_ia.a.b`, False) ; `…/__init__.py` → (`controle_ia.a`, True)."""
    parties = chemin[len("src/"):-len(".py")].split("/")
    if parties[-1] == "__init__":
        return ".".join(parties[:-1]), True
    return ".".join(parties), False


def _imports(source: str, module: str, est_paquet: bool) -> tuple[set[str], set[str]]:
    """Modules importés, à toute profondeur de l'arbre (fonctions comprises), relatifs résolus : (exigés, possibles).
    Pour `from X import y`, X est exigé et `X.y` seulement possible (y peut être un nom, non un module)."""
    paquet = module if est_paquet else module.rpartition(".")[0]
    exiges: set[str] = set()
    possibles: set[str] = set()
    for n in ast.walk(ast.parse(source)):
        if isinstance(n, ast.Import):
            exiges |= {a.name for a in n.names}
        elif isinstance(n, ast.ImportFrom):
            if n.level:
                base = paquet.split(".")
                base = base[:len(base) - (n.level - 1)]
                origine = ".".join(base + ([n.module] if n.module else []))
            else:
                origine = n.module or ""
            exiges.add(origine)
            possibles |= {origine + "." + a.name for a in n.names if a.name != "*"}
    return exiges, possibles


def modules_importes(racine: Path, depart: list[str]) -> list[str]:
    """Fermeture des imports du paquet depuis les fichiers de départ (chemins relatifs à la racine), avec les
    `__init__.py` des paquets parents de chaque module."""
    vus: set[str] = set()
    a_lire = list(depart)
    while a_lire:
        chemin = a_lire.pop()
        if chemin in vus:
            continue
        vus.add(chemin)
        source = (racine / chemin).read_text(encoding="utf-8")
        module, est_paquet = _chemin_vers_module(chemin) if chemin.startswith("src/") else ("__main__", False)
        exiges, possibles = _imports(source, module, est_paquet)
        noms = [(x, True) for x in sorted(exiges)] + [(x, False) for x in sorted(possibles - exiges)]
        for nom, exige in noms:
            parties = nom.split(".")
            for k in range(1, len(parties) + 1):
                sous = ".".join(parties[:k])
                try:
                    p = _module_vers_chemin(racine, sous)
                except Refus:
                    if not exige and k == len(parties):
                        p = None                       # `from X import y` : y est un nom de X, non un module
                    else:
                        raise
                if p is not None and p not in vus:
                    a_lire.append(p)
    return sorted(vus)


def est_cloisonne_ici(chemin: str) -> bool:
    from controle_ia.organismes_discrets.cloisonnement_bras_a_v14 import est_cloisonne
    return (est_cloisonne(chemin, False) or any(chemin.startswith(p) for p in PREFIXES_CLOISONNES)
            or any(f in chemin for f in FRAGMENTS_CLOISONNES))


def donnees_de_la_course(racine: Path, configuration: str, plan_scelle: str) -> list[str]:
    """Fichiers de données que la course lit, chacun avec son compagnon."""
    c = json.loads((racine / configuration).read_text(encoding="utf-8"))
    ref = json.loads((racine / c["configuration_de_reference"]["chemin"]).read_text(encoding="utf-8"))
    fichiers = [configuration, c["texte"]["chemin"], c["configuration_de_reference"]["chemin"],
                ref["taches_distillation"]["chemin"], ref["taches_evaluation"]["chemin"], plan_scelle]
    sortie = []
    for f in fichiers:
        for x in (f, f + ".sha256"):
            if not (racine / x).is_file():
                raise Refus(f"{x} absent sur disque (R11)")
            sortie.append(x)
    return sortie


def fichiers_du_guide(configuration_brute: dict) -> list[dict]:
    """Les deux fichiers du guide et leurs compagnons, aux empreintes données : rien n'est lu sur disque. La clé `guide`
    de la configuration doit nommer exactement les chemins et empreintes inscrits ici."""
    g = configuration_brute.get("guide")
    attendu = {"identifiant": GUIDE_IDENTIFIANT, "fichier": GUIDE_FICHIERS[0][0], "sha256": GUIDE_FICHIERS[0][1],
               "index": GUIDE_FICHIERS[1][0], "index_sha256": GUIDE_FICHIERS[1][1]}
    if g != attendu:
        raise Refus(f"guide de la configuration {g!r} ; {attendu!r} exigé")
    sortie = []
    for chemin, sha in GUIDE_FICHIERS:
        sortie.append({"chemin": chemin, "sha256_attendu": sha, "lu_par_ce_programme": False})
        sortie.append({"chemin": chemin + ".sha256", "empreinte_inscrite_attendue": sha, "lu_par_ce_programme": False})
    return sortie


def liste_blanche(racine: Path, configuration: str, lanceur_chemin: str, plan_scelle: str) -> dict:
    racine = Path(racine)
    if lanceur_chemin != LANCEUR_ATTENDU:
        raise Refus(f"lanceur {lanceur_chemin} ; cette liste est faite pour {LANCEUR_ATTENDU}")
    depart = [PROGRAMME_DE_LA_COURSE, lanceur_chemin]
    modules = modules_importes(racine, depart)
    donnees = donnees_de_la_course(racine, configuration, plan_scelle)
    tout = sorted(set(modules) | set(donnees))
    cloisonnes = [x for x in tout if est_cloisonne_ici(x)]
    if cloisonnes:
        raise Refus(f"chemins cloisonnés dans la liste blanche : {cloisonnes}")
    guide = fichiers_du_guide(json.loads((racine / configuration).read_text(encoding="utf-8")))
    return {"modules": [x for x in tout if x in modules], "donnees": [x for x in tout if x in donnees],
            "guide": guide, "manquants": [], "nombre": len(tout) + len(guide)}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--racine", default=".")
    p.add_argument("--configuration", required=True)
    p.add_argument("--lanceur-chemin", required=True)
    p.add_argument("--plan-scelle", required=True)
    a = p.parse_args(argv)
    try:
        sortie = liste_blanche(Path(a.racine), a.configuration, a.lanceur_chemin, a.plan_scelle)
    except Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    print(json.dumps(sortie, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
