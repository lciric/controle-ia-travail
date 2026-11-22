"""v2 (la v1, scellée, reste telle quelle) : ajoute aux fonctions déclarées la garde de l'instance resserrée
(`entrees_v1`, `course_v1`), décision de la session mère du 2026-11-22.

Preuve par programme (consigne d'alignement de T0.8, § 4) : entre le commit de base `453a71e1` et le commit aligné,
les valeurs gelées du code, les phrases des tables D et F, l'agrégateur séquentiel et la pièce « mots et coût » ne
changent pas. Lit les deux commits par `git show` (aucun fichier de travail) ; n'écrit rien ; code de sortie 0 si tout
tient, 1 sinon.

Ce qui est comparé :
1. fichiers de `src/controle_ia/t08/` : même empreinte, ou changés (liste) ;
2. dans chaque fichier changé : toute affectation de premier niveau à un nom en capitales (valeurs gelées, bornes,
   tolérances, listes, phrases, réglages), comparée sur l'arbre syntaxique ; une seule différence admise : des noms
   **ajoutés** (déclarés) ; aucun nom changé ni retiré ;
3. dans chaque fichier changé : toute fonction de premier niveau, comparée sur l'arbre syntaxique ; changées ou
   ajoutées : listées (la liste attendue est écrite ci-dessous ; toute autre fonction changée fait échouer) ;
4. `VALEURS_GELEES_COURSE` et `VALEURS_GELEES_LECTURE` évaluées dans chacun des deux commits (import du module
   `configuration_v1` de chaque commit dans un dossier jetable) : égales ;
5. `tables_v1.py` (phrases des tables D et F) inchangé à l'octet ; `src/controle_ia/bases/` inchangé à l'octet entre
   le commit aligné et `main` à sa base, `sequentiel.py` à `35a09834…` ;
6. pièce inscrite et son fichier d'inscription : empreintes du brouillon 11 au commit aligné.

Usage : python preuve-inchange-t08-v2.py BASE ALIGNE
"""
from __future__ import annotations

import ast
import hashlib
import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path

BASE, ALIGNE = sys.argv[1], sys.argv[2]
T = "src/controle_ia/t08/"
ATTENDUES = {   # fonctions changées ou ajoutées, déclarées par l'alignement (rapport, § 2)
    "configuration_v1.py": {"exiger_marqueurs"},
    "entrees_v1.py": {"_nom_interdit_instance", "exiger_instance_sans_interdits"},
    "course_v1.py": {"executer_course"},
    "essai_jouet_v1.py": {"fabriquer_entrees"},
    "lecture_v1.py": {"_exiger_ligne_piece", "passage_a_blanc_reel", "executer_lecture"},
    "mots_et_cout_v1.py": {"charger_piece", "exiger_forme_marqueur_piece", "_sous_racine", "verifier_inscription",
                           "charger_module_par_chemin"},
}
CLASSES_ATTENDUES = {"mots_et_cout_v1.py": {"Piece"}, "lecture_v1.py": {"LectureT08"}}
CONSTANTES_AJOUTEES = {"entrees_v1.py": {"_RUN_7B"}, "mots_et_cout_v1.py": {"CLES_MARQUEUR_PIECE", "LIGNE_PIECE", "NOM_MODULE_PIECE", "_HEX40", "_HEX64"}}
PIECE = {"scripts/mots_et_cout_t06_v3.py": "9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674",
         "registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json":
             "e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b",
         "src/controle_ia/bases/sequentiel.py": "35a0983404d7a10d0bb736fa37307a108501785a207c27346be1cd02bab11ba8"}
echecs: list[str] = []


def git(*a) -> bytes:
    return subprocess.run(["git", *a], check=True, capture_output=True).stdout


def fichiers(commit: str, dossier: str) -> dict[str, str]:
    sortie = {}
    for l in git("ls-tree", "-r", commit, "--", dossier).decode().splitlines():
        meta, chemin = l.split("\t", 1)
        sortie[chemin] = meta.split()[2]
    return sortie


def premier_niveau(source: bytes):
    arbre = ast.parse(source)
    consts, fonctions, classes = {}, {}, {}
    for n in arbre.body:
        if isinstance(n, (ast.Assign, ast.AnnAssign)):
            cibles = n.targets if isinstance(n, ast.Assign) else [n.target]
            for c in cibles:
                for x in ast.walk(c):
                    if isinstance(x, ast.Name) and x.id.isupper():
                        consts[x.id] = ast.dump(n)
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            fonctions[n.name] = ast.dump(n)
        elif isinstance(n, ast.ClassDef):
            classes[n.name] = ast.dump(n)
    return consts, fonctions, classes


def valeurs_gelees(commit: str) -> tuple:
    with tempfile.TemporaryDirectory() as d:
        racine = Path(d)
        for chemin in fichiers(commit, "src/controle_ia").keys():
            p = racine / chemin
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(git("show", f"{commit}:{chemin}"))
        code = ("import sys; sys.path.insert(0, sys.argv[1]); from controle_ia.t08 import configuration_v1 as cf; "
                "print(repr((cf.VALEURS_GELEES_COURSE, cf.VALEURS_GELEES_LECTURE, cf.MARQUEURS)))")
        r = subprocess.run([sys.executable, "-I", "-c", code, str(racine / "src")], capture_output=True, text=True,
                           cwd=d)
        if r.returncode != 0:
            echecs.append(f"valeurs gelées de {commit[:8]} non évaluées : {r.stderr.strip()[-300:]}")
            return None
        return r.stdout.strip()


a, b = fichiers(BASE, T), fichiers(ALIGNE, T)
if set(a) != set(b):
    echecs.append(f"fichiers ajoutés ou retirés sous {T} : {sorted(set(a) ^ set(b))}")
changes = sorted(f for f in a if f in b and a[f] != b[f])
print(f"1. fichiers de {T} : {len(a)} au commit de base, {len(b)} au commit aligné ; inchangés {len(a) - len(changes)} ; "
      f"changés {len(changes)} : {[Path(f).name for f in changes]}")
for f in changes:
    nom = Path(f).name
    ca, fa, ka = premier_niveau(git("show", f"{BASE}:{f}"))
    cb, fb, kb = premier_niveau(git("show", f"{ALIGNE}:{f}"))
    changees = sorted(k for k in ca if k in cb and ca[k] != cb[k])
    retirees = sorted(set(ca) - set(cb))
    ajoutees = sorted(set(cb) - set(ca))
    if changees or retirees or set(ajoutees) != CONSTANTES_AJOUTEES.get(nom, set()):
        echecs.append(f"{nom} : constantes changées {changees}, retirées {retirees}, ajoutées {ajoutees}")
    f_ch = {k for k in fb if fa.get(k) != fb[k]} | (set(fa) - set(fb))
    k_ch = {k for k in kb if ka.get(k) != kb[k]} | (set(ka) - set(kb))
    if f_ch != ATTENDUES.get(nom, set()) or k_ch != CLASSES_ATTENDUES.get(nom, set()):
        echecs.append(f"{nom} : fonctions changées {sorted(f_ch)} (attendues {sorted(ATTENDUES.get(nom, set()))}), "
                      f"classes changées {sorted(k_ch)}")
    print(f"2-3. {nom} : constantes en capitales {len(ca)} → {len(cb)}, changées {changees}, retirées {retirees}, "
          f"ajoutées {ajoutees} ; fonctions changées ou ajoutées {sorted(f_ch)} ; classes {sorted(k_ch)}")
va, vb = valeurs_gelees(BASE), valeurs_gelees(ALIGNE)
if va is not None and va != vb:
    echecs.append("VALEURS_GELEES_COURSE, VALEURS_GELEES_LECTURE ou MARQUEURS différents")
print(f"4. valeurs gelées évaluées : égales = {va is not None and va == vb} "
      f"(empreinte {hashlib.sha256(str(vb).encode()).hexdigest()[:16]}…)")
tab = T + "tables_v1.py"
if a.get(tab) != b.get(tab):
    echecs.append("tables_v1.py changé")
base_main = git("merge-base", ALIGNE, "origin/main").decode().strip()
bases_a, bases_b = fichiers(base_main, "src/controle_ia/bases"), fichiers(ALIGNE, "src/controle_ia/bases")
if bases_a != bases_b:
    echecs.append("src/controle_ia/bases/ changé par rapport à main")
print(f"5. tables_v1.py inchangé à l'octet : {a.get(tab) == b.get(tab)} ; src/controle_ia/bases/ égal à main "
      f"({base_main[:8]}) : {bases_a == bases_b}")
for chemin, attendu in PIECE.items():
    sha = hashlib.sha256(git("show", f"{ALIGNE}:{chemin}")).hexdigest()
    if sha != attendu:
        echecs.append(f"{chemin} : {sha[:12]}… ≠ {attendu[:12]}…")
    print(f"6. {chemin} : {sha} {'conforme' if sha == attendu else 'DIFFÉRENT'}")
print("BILAN : " + ("tout tient" if not echecs else "ÉCHEC : " + " | ".join(echecs)))
sys.exit(1 if echecs else 0)
