"""Banc de mutations de l'alignement du code de T0.8 sur la pièce « mots et coût » inscrite (modèle A) — v5 : la v4 plus A30
(chemins avec saut de ligne, CA-13) ; v4 : la v3 plus A29
(chemins non ASCII, CA-10) ; v3 : la v2
(même dossier, elle-même la v1 plus A18 à A24) plus A25 à A28 (garde de l'instance resserrée) ; v2 : la v1
plus A18 à A24 (corrections CA-01 à CA-06 de la contre-lecture) et un essai de plus pour A12.

Rejoue les 21 mutations du banc de la seconde passe de corrections (`docs/notes/t08-code-compte4-v1/
mutations-corrections-2-t08-v1.py` au commit `453a71e1`, passé en premier argument, lu sans être exécuté comme
script : seule sa liste `MUTATIONS` est reprise) et ajoute les mutations de l'alignement (A01 à A17) : chaque garde
neuve est retirée ou affaiblie dans une copie jetable ; l'essai nommé doit échouer. Copies sous le bloc-notes ; l'arbre
n'est jamais écrit. Les copies lient `docs`, `prereg`, `brouillons` et `.git` (lecture seule ; le tokeniseur par
`git show`) et copient le registre, le fichier d'inscription et le module de la pièce (un lien se résoudrait hors de la
copie, ce que la garde « hors de la racine » refuse). Le conftest copié perd la seule ligne d'import
du greffon des échecs connus (liste propre à la suite entière ; aucun essai de T0.8 n'y figure).

Usage : python mutations-alignement-t08-v5.py BANC_ANCIEN ARBRE BLOC PYTHON
"""
from __future__ import annotations

import ast
import os
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ANCIEN, ARBRE, BLOC, PY = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4]
T = "src/controle_ia/t08/"
M, L, CF = T + "mots_et_cout_v1.py", T + "lecture_v1.py", T + "configuration_v1.py"
AL, MC = "tests/test_t08_alignement_piece_v1.py", "tests/test_t08_mots_et_cout_v1.py"
G, LC, ER = "tests/test_t08_gardes_corrections_v1.py", "tests/test_t08_lecture_course_v1.py", "tests/test_t08_entrees_rendu_v1.py"


def mutations_anciennes() -> list:
    """Liste `MUTATIONS` du banc ancien, évaluée sans exécuter le script (ses constantes de chemins seules)."""
    arbre = ast.parse(ANCIEN.read_text(encoding="utf-8"))
    env = {}
    for n in arbre.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, (ast.Name, ast.Tuple)) for t in n.targets):
            noms = {x.id for t in n.targets for x in ast.walk(t) if isinstance(x, ast.Name)}
            if noms <= {"T", "L", "E", "TD", "EJ", "C", "G", "LC", "MUTATIONS"}:
                exec(compile(ast.Module([n], []), str(ANCIEN), "exec"), env)
    return env["MUTATIONS"]


NEUVES = [
    ("A01", "(a)", "ligne CODE-MOTS-ET-COUT-T06 non comparée au marqueur", M,
     ('    if ligne.get("chemin") != mq["fichier_inscription"] or ligne.get("sha256") != mq["sha256_inscription"]:',
      "    if False:"),
     [f"{AL}::test_point_a", f"{AL}::test_ordre_des_points"]),
    ("A02", "(a)", "chemin de la ligne non comparé (empreinte seule)", M,
     ('    if ligne.get("chemin") != mq["fichier_inscription"] or ligne.get("sha256") != mq["sha256_inscription"]:',
      '    if ligne.get("sha256") != mq["sha256_inscription"]:'),
     [f"{AL}::test_point_a"]),
    ("A03", "(b)", "empreinte du fichier d'inscription non vérifiée", M,
     ('    if sha_fi != mq["sha256_inscription"]:', "    if False:"),
     [f"{AL}::test_point_b", f"{AL}::test_ordre_des_points"]),
    ("A04", "(c)", "empreinte du module dans l'inscription non comparée", M,
     ('    if not isinstance(fichiers, dict) or fichiers.get(mq["module"]) != mq["sha256_module"]:',
      "    if not isinstance(fichiers, dict):"),
     [f"{AL}::test_point_c", f"{AL}::test_ordre_des_points"]),
    ("A05", "(d)", "empreinte du module sur disque non vérifiée en (d)", M,
     ('    if sha_mod != mq["sha256_module"]:', "    if False:"),
     [f"{AL}::test_point_d", f"{AL}::test_ordre_des_points"]),
    ("A06", "(e)", "commit de l'inscription non comparé", M,
     ('    if inscription.get("commit") != mq["commit"]:', "    if False:"),
     [f"{AL}::test_point_e"]),
    ("A07", "charg.", "chargeur : empreinte des octets exécutés non vérifiée", M,
     ("    if sha != sha_attendue:", "    if False:"),
     [f"{AL}::test_chargement_par_chemin_relit_l_empreinte"]),
    ("A08", "charg.", "chargeur : sys.path modifié toléré", M,
     ("        if list(sys.path) != chemins_avant:", "        if False:"),
     [f"{AL}::test_chargement_qui_touche_sys_path"]),
    ("A09", "charg.", "chargeur : sys.path non rendu après un échec", M,
     ("        sys.path[:] = chemins_avant\n", "        pass\n"),
     [f"{AL}::test_chargement_qui_touche_sys_path"]),
    ("A10", "charg.", "chargeur : autre GardeArret tolérée", M,
     ('        if "GardeArret" in module.__dict__ and module.GardeArret is not GardeArret:', "        if False:"),
     [f"{AL}::test_chargement_autre_garde_arret"]),
    ("A11", "charg.", "chargeur : module à moitié chargé laissé dans sys.modules", M,
     ("            sys.modules.pop(nom, None)\n", "            pass\n"),
     [f"{AL}::test_chargement_erreur_a_l_execution"]),
    ("A12", "charg.", "repli sur l'import par nom du module", M,
     ('    module = charger_module_par_chemin(_sous_racine(racine, marqueur["module"], "module de la pièce"),\n'
      '                                       marqueur["sha256_module"])',
      '    module = importlib.import_module("controle_ia.t08.mots_et_cout_v1")'),
     [f"{AL}::test_cas_sain_piece_inscrite", f"{AL}::test_copie_saine"]),
    ("A13", "jouet", "pièce jouet acceptée en mode réel", M,
     ('        if mode == "reel" and getattr(module, "PIECE_JOUET", False):', "        if False:"),
     [f"{MC}::test_piece_reelle_exige_le_marqueur_et_refuse_le_jouet"]),
    ("A14", "forme", "forme du marqueur non contrôlée par exiger_marqueurs", CF,
     ('    exiger_forme_marqueur_piece(marqueurs["CODE_MOTS_ET_COUT_T06"])', "    pass"),
     [f"{ER}::test_marqueurs_cas_sain_et_artefacts"]),
    ("A15", "(a) lect.", "lecture et passage à blanc : ligne de la pièce non comparée", L,
     ('    if ligne.get("chemin") != c["fichier_inscription"] or ligne.get("sha256") != c["sha256_inscription"]:',
      "    if False:"),
     [f"{G}::test_passage_a_blanc_cas_sain_et_artefacts", f"{LC}::test_etape_a_mode_reel_cas_sain_et_artefacts"]),
    ("A16", "lect.", "lecture réelle : pièce non chargée en mode réel acceptée", L,
     ('    if mode == "reel" and (piece.mode != "reel" or piece.inscription is None):', "    if False:"),
     [f"{LC}::test_lecture_reelle_charge_la_piece_par_charger_piece"]),
    ("A17", "hors rac.", "chemins hors de la racine admis", M,
     ("    if Path(racine).resolve() not in p.parents:", "    if False:"),
     [f"{AL}::test_chemins_hors_racine"]),
    ("A18", "CA-01", "pièce refusée par Piece(...) laissée dans sys.modules", M,
     ("            sys.modules.pop(NOM_MODULE_PIECE, None)\n", "            pass\n"),
     [f"{AL}::test_chargement_contrat_incomplet"]),
    ("A19", "CA-02", "lecture réelle : pièce contrôlée sur un autre marqueur acceptée", L,
     ("        if vu != {k: c[k] for k in vu}:", "        if False:"),
     [f"{LC}::test_lecture_reelle_charge_la_piece_par_charger_piece"]),
    ("A20", "CA-03", "enveloppe : centres reçoivent l'action entière", M,
     ('        return dict(self.module.centres([{"tache": a["tache"], "cout": a["cout"]} for a in actions]))',
      "        return dict(self.module.centres(actions))"),
     [f"{AL}::test_enveloppe_n_appelle_que_le_contrat_et_passe_les_entrees_telles_quelles"]),
    ("A21", "CA-03", "enveloppe : étiquettes inversées avant l'apprentissage", M,
     ("        interne = f(actions, y, centres)", "        interne = f(actions, 1 - y, centres)"),
     [f"{AL}::test_enveloppe_n_appelle_que_le_contrat_et_passe_les_entrees_telles_quelles",
      f"{AL}::test_contrat_enveloppe_egale_piece"]),
    ("A22", "CA-03", "enveloppe : septième fonction lue sur la pièce", M,
     ("        interne = f(actions, y, centres)",
      "        interne = f(actions, y, centres)\n        getattr(self.module, 'ajuster', None)"),
     [f"{AL}::test_enveloppe_n_appelle_que_le_contrat_et_passe_les_entrees_telles_quelles"]),
    ("A23", "CA-05", "chargeur : interruption convertie en GardeArret", M,
     ("        if isinstance(e, GardeArret) or not isinstance(e, Exception):", "        if isinstance(e, GardeArret):"),
     [f"{AL}::test_chargement_interruption_relevee_telle_quelle"]),
    ("A24", "CA-06", "balise « à cheval » lue comme balise", "src/controle_ia/t08/juges_v1.py",
     ('            return {"etat": "balise" if t.endswith(BALISE) else "a_cheval", "k": j}',
      '            return {"etat": "balise", "k": j}'),
     ["tests/test_t08_tokeniseur_balise_v1.py::test_balayage_ascii_apres_la_balise"]),
    ("A25", "inst.", "garde de l'instance : chemins des commits non lus (blob dédoublé)", T + "entrees_v1.py",
     ("            if chemin and _nom_interdit_instance(chemin, run_7b):", "            if False:"),
     [f"{ER}::test_amorce_instance_objet_git_interdit"]),
    ("A26", "inst.", "garde de l'instance : resume.json de 7b admis", T + "entrees_v1.py",
     ('(base == "resume.json" and run_7b in parties[:-1])', "False"),
     [f"{ER}::test_amorce_instance_sans_fichier_interdit", f"{ER}::test_amorce_instance_objet_git_interdit"]),
    ("A27", "inst.", "garde de l'instance : tout resume.json interdit (forme d'avant)", T + "entrees_v1.py",
     ('(base == "resume.json" and run_7b in parties[:-1])', '(base == "resume.json")'),
     [f"{ER}::test_amorce_instance_sans_fichier_interdit", f"{ER}::test_amorce_instance_clone_de_l_arbre_aligne"]),
    ("A28", "inst.", "garde de l'instance : identifiant du run de 7b non contrôlé", T + "entrees_v1.py",
     ("    if not isinstance(run_7b, str) or not _RUN_7B.match(run_7b):", "    if False:"),
     [f"{ER}::test_amorce_instance_sans_fichier_interdit"]),
    ("A29", "CA-10", "garde de l'instance : chemins des commits lus sans -z (guillemets, octal)", T + "entrees_v1.py",
     ('"--name-only", "-z"], capture_output=True)', '"--name-only"], capture_output=True)'),
     [f"{ER}::test_amorce_instance_chemin_non_ascii_blob_dedouble"]),
    ("A30", "CA-13", "garde de l'instance : chemins des commits coupés aux sauts de ligne", T + "entrees_v1.py",
     ('{c.lstrip("\\n") for c in r.stdout.decode("utf-8", "surrogateescape").split("\\0")}',
      'set(r.stdout.decode("utf-8", "surrogateescape").replace("\\n", "\\0").split("\\0"))'),
     [f"{ER}::test_amorce_instance_chemin_avec_saut_de_ligne_blob_dedouble"]),
]


def preparer(k: int) -> Path:
    d = BLOC / f"copie-{k}"
    shutil.rmtree(d, ignore_errors=True)
    d.mkdir(parents=True)
    shutil.copytree(ARBRE / "src", d / "src")
    (d / "tests").mkdir()
    # essais de T0.8, et les modules d'aide du dossier des essais (conftest.py et ce qu'il importe), jamais d'autre essai
    aides = [p for p in sorted((ARBRE / "tests").iterdir()) if p.is_file() and not p.name.startswith("test_")]
    for p in sorted((ARBRE / "tests").glob("test_t08_*_v1.py")) + aides:
        shutil.copyfile(p, d / "tests" / p.name)
    # le greffon des échecs connus de `main` exige que chaque essai de sa liste existe : dans la copie, qui ne porte que
    # les essais de T0.8 (aucun n'est dans la liste), sa ligne d'import est retirée du conftest copié (déclaré)
    c = d / "tests" / "conftest.py"
    lignes = c.read_text(encoding="utf-8").splitlines(keepends=True)
    retirees = [l for l in lignes if l.startswith("from greffon_echecs_connus_")]
    if len(retirees) != 1:
        sys.exit(f"ARRÊT : conftest.py d'une forme inattendue ({len(retirees)} import(s) du greffon)")
    c.write_text("".join(l for l in lignes if l not in retirees), encoding="utf-8")
    shutil.copyfile(ARBRE / "pyproject.toml", d / "pyproject.toml")
    for lien in ("docs", "prereg", "brouillons", ".git"):
        os.symlink(ARBRE / lien, d / lien)
    # copiés, non liés : la garde « hors de la racine » refuse un chemin qui se résout hors de la copie
    for rel in ("registres/scellements-v1.md", "registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json",
                "scripts/mots_et_cout_t06_v3.py"):
        (d / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ARBRE / rel, d / rel)
    return d


def pytest_(d: Path, essais: list[str]) -> tuple[int, str]:
    env = {**os.environ, "PYTHONPATH": str(d / "src"), "PYTHONDONTWRITEBYTECODE": "1", "T08_EXIGER_TOKENISEUR": "1"}
    r = subprocess.run([PY, "-m", "pytest", "-q", "-p", "no:cacheprovider", *essais], cwd=d, env=env,
                       capture_output=True, text=True, timeout=1800)
    return r.returncode, (r.stdout.strip().splitlines() or [""])[-1]


def eprouver(k: int, mutations: list) -> list[str]:
    d = preparer(k)
    sortie = []
    for nom, constat, quoi, fichier, (ancien, neuf), essais in mutations:
        p = d / fichier
        texte = p.read_text(encoding="utf-8")
        n = texte.count(ancien)
        if n != 1:
            sortie.append(f"{nom} {constat:8s} INAPPLICABLE ({n} occurrences) : {quoi}")
            continue
        p.write_text(texte.replace(ancien, neuf), encoding="utf-8")
        try:
            code, fin = pytest_(d, essais)
        finally:
            p.write_text(texte, encoding="utf-8")
        etat = "tuée " if code != 0 else "SURVIT"
        sortie.append(f"{nom:5s} {constat:9s} {Path(fichier).name:24s} {etat} : {quoi} — "
                      f"{' ; '.join(e.split('::')[1] for e in essais)} [{fin}]")
    return sortie


if __name__ == "__main__":
    MUTATIONS = mutations_anciennes() + NEUVES
    d0 = preparer(99)
    fichiers = [str(x.relative_to(d0)) for x in sorted((d0 / "tests").glob("test_t08_*_v1.py"))]
    code, fin = pytest_(d0, fichiers)
    print(f"témoin sans mutation, les {len(fichiers)} fichiers d'essais de T0.8 : code {code} ; {fin}", flush=True)
    if code != 0:                      # garde : un témoin qui échoue rendrait toute mutation « tuée » à tort (R5)
        print("ARRÊT : le témoin sans mutation échoue ; aucune mutation n'est éprouvée", flush=True)
        sys.exit(2)
    lots = [MUTATIONS[i::3] for i in range(3)]
    with ThreadPoolExecutor(3) as ex:
        resultats = list(ex.map(lambda a: eprouver(*a), enumerate(lots)))
    ordre = {m[0]: i for i, m in enumerate(MUTATIONS)}
    lignes = sorted((l for r in resultats for l in r), key=lambda l: ordre[l.split()[0]])
    for l in lignes:
        print(l)
    print(f"bilan : {len(MUTATIONS)} mutations ; tuées {sum(' tuée ' in l for l in lignes)} ; "
          f"survivent {sum('SURVIT' in l for l in lignes)} ; inapplicables {sum('INAPPLICABLE' in l for l in lignes)}")
