#!/usr/bin/env python3
"""Banc de mutations du script `ecrire_fiches_reception_v2.py` : une mutation par garde neuve, qui la rend inopérante
(`ctl.exiger("<garde>", lambda: …` devient `ctl.exiger("<garde>", lambda: True or …`, pour toutes les occurrences de la
garde ; pour le filtre des clés lues, le document entier est gardé au lieu des seuls chemins nommés), puis, pour les
gardes à plusieurs contrôles, une mutation par occurrence (chaque contrôle doit avoir son propre artefact). Chaque mutant doit
faire échouer au moins un essai de `test_ecrire_fiches_reception_v2.py` (mutant tué) ; le script témoin, non muté, doit
les passer tous. Les mutants et les dossiers d'essai s'écrivent sous `--tmp`, hors du dépôt de travail ; rien n'est
écrit dans le dépôt, sauf la sortie demandée par `--sortie`.

  cd /home/claude/controle-ia-travail && nice -n 10 .venv/bin/python -I \\
     brouillons/preuves-mentors-v1/reception-r1-relance-v2/tests/banc_mutations_v2.py --tmp /tmp/banc-reception-v2 \\
     --sortie brouillons/preuves-mentors-v1/reception-r1-relance-v2/banc-mutations-v2-sortie.txt

Code de sortie : 0 si le témoin passe et si tous les mutants sont tués ; 1 sinon (aucun repli silencieux, R5)."""
import argparse
import datetime as dt
import hashlib
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
SCRIPT = ICI.parent / "ecrire_fiches_reception_v2.py"
ESSAIS = ICI / "test_ecrire_fiches_reception_v2.py"
DEPOT = ICI.parents[3]
GARDES = ("recuperation", "config-table", "canonique", "table", "ligne-104", "attentes-texte", "piece", "compagnon",
          "fiche", "attendus", "nom-rejeu", "e21", "rattachement", "texte", "commande", "decisif", "configuration",
          "commit", "entropie", "table-comparee", "provenance", "comptes", "juges", "P-R5")
MUTATIONS = tuple((g, f'ctl.exiger("{g}", lambda: ', f'ctl.exiger("{g}", lambda: True or ') for g in GARDES) + (
    ("filtre", "garde = {}  # filtre", "garde = dict(doc)  # filtre"),)


def remplacer_occurrence(source: str, avant: str, apres: str, i: int) -> str:
    """Remplace la seule occurrence de rang `i` (0 = la première) de `avant`."""
    debut = -1
    for _ in range(i + 1):
        debut = source.index(avant, debut + 1)
    return source[:debut] + apres + source[debut + len(avant):]


def lancer_essais(script: Path, base: Path) -> tuple:
    env = {**os.environ, "SCRIPT_RECEPTION_V2": str(script), "PYTHONPATH": str(DEPOT / "src"),
           "PYTHONDONTWRITEBYTECODE": "1"}
    base.parent.mkdir(parents=True, exist_ok=True)      # pytest crée `--basetemp`, pas ses parents
    t0 = time.perf_counter()
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-x", "-rf", "-p", "no:cacheprovider", f"--basetemp={base}",
                        str(ESSAIS)], capture_output=True, text=True, env=env, cwd=str(DEPOT))
    sortie = r.stdout + r.stderr
    echecs = re.findall(r"^FAILED (\S+)", sortie, flags=re.M)
    fin = [x for x in sortie.strip().splitlines() if x.strip()][-1:] or [""]
    return r.returncode, echecs, fin[0], time.perf_counter() - t0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tmp", required=True, help="dossier de travail hors du dépôt (mutants, dossiers d'essai)")
    ap.add_argument("--sortie", default=None, help="fichier neuf où écrire le tableau (jamais écrasé)")
    ap.add_argument("--sans-occurrences", dest="par_occurrence", action="store_false",
                    help="ne muter que les gardes entières (par défaut : aussi chaque occurrence d'une garde multiple)")
    a = ap.parse_args(argv)
    tmp = Path(a.tmp).resolve()
    if DEPOT in tmp.parents or tmp == DEPOT:
        print("ARRÊT : --tmp doit être hors du dépôt de travail", file=sys.stderr)
        return 1
    if a.sortie and Path(a.sortie).exists():
        print(f"ARRÊT : {a.sortie} existe déjà (R12)", file=sys.stderr)
        return 1
    source = SCRIPT.read_text(encoding="utf-8")
    lignes = [f"Banc de mutations de {SCRIPT.name} (sha256 {hashlib.sha256(source.encode('utf-8')).hexdigest()}) ; essais "
              f"{ESSAIS.name} (sha256 {hashlib.sha256(ESSAIS.read_bytes()).hexdigest()}) ; début "
              f"{dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} ; python {sys.version.split()[0]}"]
    code, echecs, fin, duree = lancer_essais(SCRIPT, tmp / "essais" / "temoin")
    temoin_ok = code == 0
    lignes.append(f"témoin (script non muté) : code {code} ; « {fin} » ; {duree:.1f} s ; "
                  f"{'conforme' if temoin_ok else 'NON CONFORME'}")
    lignes.append("mutation (garde entière, ou garde#rang pour une seule occurrence) | occurrences mutées | issue | "
                  "premier essai en échec | durée")
    tous_tues, nb = True, 0
    for garde, avant, apres in MUTATIONS:
        n = source.count(avant)
        if n == 0:
            lignes.append(f"{garde} | 0 | MUTATION INAPPLICABLE | — | —")
            tous_tues = False
            continue
        variantes = [(garde, source.replace(avant, apres), str(n))]
        if a.par_occurrence and n > 1:
            variantes += [(f"{garde}#{i + 1}", remplacer_occurrence(source, avant, apres, i), f"1 (rang {i + 1})")
                          for i in range(n)]
        for nom, texte_mutant, combien in variantes:
            nb += 1
            d = tmp / "mutants" / nom.replace("#", "-")
            d.mkdir(parents=True, exist_ok=False)
            mutant = d / SCRIPT.name
            mutant.write_text(texte_mutant, encoding="utf-8")
            code, echecs, fin, duree = lancer_essais(mutant, tmp / "essais" / nom.replace("#", "-"))
            tue = code == 1 and bool(echecs)
            tous_tues = tous_tues and tue
            essai = (echecs[0] if echecs else fin).split("::")[-1]
            lignes.append(f"{nom} | {combien} | {'tuée' if tue else 'SURVIVANTE (code ' + str(code) + ')'} | "
                          f"{essai} | {duree:.1f} s")
    bilan = temoin_ok and tous_tues
    lignes.append(f"bilan : {nb} mutants ({len(MUTATIONS)} gardes entières"
                  f"{', plus une par occurrence des gardes à plusieurs contrôles' if a.par_occurrence else ''}), "
                  f"{'tous tués' if tous_tues else 'au moins un survivant'} ; "
                  f"témoin {'conforme' if temoin_ok else 'non conforme'} ; fin "
                  f"{dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} → {'CONFORME' if bilan else 'NON CONFORME'}")
    texte = "\n".join(lignes) + "\n"
    print(texte, end="")
    if a.sortie:
        Path(a.sortie).write_text(texte, encoding="utf-8")
    return 0 if bilan else 1


if __name__ == "__main__":
    sys.exit(main())
