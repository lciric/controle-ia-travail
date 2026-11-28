"""Garde 1 (lue par l'arbre syntaxique), prereg.problemes et forme de l'entrée 7 prévue, sur les candidats et un texte final
d'essai.

Usage (depuis la racine du dépôt, PYTHONPATH=src, pour importer controle_ia.prereg seulement) :
  python -B garde1_problemes_entree7_v1.py MODULE CANDIDAT1 CANDIDAT2 ENTREE7_PREVUE DOSSIER_ESSAI
  MODULE : audit_verdict_p3_v1.py, lu par ast (jamais importé ni exécuté) : on n'en prend que les chaînes des
    expressions EMPREINTE_MODULE_CITEE et EMPREINTE_TESTS_CITEE.
  ENTREE7_PREVUE : le texte de l'entrée 7 tel que la consigne le donne (chevrons <A>, <verdict A>, <B>, <verdict B>).
  DOSSIER_ESSAI : où écrire le texte final d'essai (candidat 2 + entrée 7 aux chevrons remplis par des valeurs d'essai).
"""
import ast
import hashlib
import re
import sys
import textwrap
from pathlib import Path

from controle_ia import prereg


def expressions_garde1(module):
    arbre = ast.parse(Path(module).read_text(encoding="utf-8"))
    out = {}
    for n in arbre.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            nom = n.targets[0].id
            if nom in ("EMPREINTE_MODULE_CITEE", "EMPREINTE_TESTS_CITEE"):
                appel = n.value
                assert isinstance(appel, ast.Call) and isinstance(appel.args[0], ast.Constant)
                out[nom] = re.compile(appel.args[0].value)
    return out


def rapport_texte(nom, chemin, expr):
    t = Path(chemin).read_text(encoding="utf-8")
    print(f"\n== {nom} : {Path(chemin).name} (sha256 {hashlib.sha256(Path(chemin).read_bytes()).hexdigest()})")
    print(f"   prereg.problemes : {prereg.problemes(chemin)}")
    for k, e in expr.items():
        print(f"   garde 1, {k}.findall : {e.findall(t)} ; search : {e.search(t).group(1) if e.search(t) else None}")
    cl = prereg.sections(t).get("Contre-lecture", "")
    entrees = list(prereg.ENTREE.finditer(cl))
    nums = [e.group(1) for e in entrees]
    distinctes = []
    for k, e in enumerate(entrees):
        fin = entrees[k + 1].start() if k + 1 < len(entrees) else len(cl)
        distinctes.append(len(set(prereg.EMPREINTE.findall(cl[e.start():fin]))))
    print(f"   entrées lues par prereg.ENTREE : {nums} ; empreintes distinctes par entrée : {distinctes}")
    print(f"   chevrons <…> restants (hors blocs de code et comparaisons) : "
          f"{sorted(set(re.findall(r'<[A-Za-zÀ-ÿ][^<>`|]*>', cl)))}")
    return t


def main(argv):
    module, c1, c2, e7p, dossier = argv[1:6]
    expr = expressions_garde1(module)
    print("expressions de la garde 1 (ast) :", {k: v.pattern for k, v in expr.items()})
    rapport_texte("candidat 1", c1, expr)
    t2 = rapport_texte("candidat 2", c2, expr)

    e7 = Path(e7p).read_text(encoding="utf-8").strip()
    print(f"\n== entrée 7 prévue (consigne) : {len(e7)} caractères")
    print(f"   chevrons : {re.findall(r'<[^<>]+>', e7)}")
    empreintes = re.findall(r"`([0-9a-f]{64})`", e7)
    print(f"   empreintes déjà écrites : {empreintes}")
    for p in (c1, c2):
        h = hashlib.sha256(Path(p).read_bytes()).hexdigest()
        print(f"   {Path(p).name} : {h} présent dans l'entrée 7 : {h in empreintes}")
    chemins = re.findall(r"`(prereg/[^`]+)`", e7)
    print(f"   chemins cités : {chemins}")
    # texte final d'essai : chevrons remplis par des valeurs d'essai, retours à la ligne comme la section
    essai = (e7.replace("<A>", hashlib.sha256(b"essai A").hexdigest())
               .replace("<B>", hashlib.sha256(b"essai B").hexdigest())
               .replace("<verdict A>", "scellable").replace("<verdict B>", "scellable"))
    lignes = textwrap.wrap(essai, width=118, subsequent_indent="  ", break_long_words=False, break_on_hyphens=False)
    debut_ligne = [x.lstrip()[:15] for x in lignes[1:]]
    print(f"   texte d'essai : {len(lignes)} lignes ; débuts des lignes de suite : {debut_ligne}")
    entree = "\n".join(lignes) + "\n"
    print(f"   entrée d'essai sans « < » ni « > » : {'<' not in entree and '>' not in entree} ; "
          f"empreintes entre accents graves : {len(re.findall(r'`[0-9a-f]{64}`', entree))}")
    sortie = Path(dossier) / "texte-final-essai.md"
    sortie.write_text(t2 + entree, encoding="utf-8")
    (Path(dossier) / "entree7-essai.md").write_text(entree, encoding="utf-8")
    rapport_texte("texte final d'essai (pas un candidat)", sortie, expr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
