"""Essais du programme de contrôle du journal (v2 : parties du journal, fiches nées deux fois) : un cas sain et des artefacts, dans un dépôt git jetable.

Usage : python3 -I docs/notes/veille-de-cap-v1/outils/essais_veille_journal_v1.py   (sortie 0 si tout passe)
"""
import json
import os
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import veille_journal_v2 as vj  # noqa: E402


def git(d, *a):
    return subprocess.run(["git", *a], cwd=d, capture_output=True, check=True).stdout.decode().strip()


def evenement(**k):
    e = {"quand": "2026-11-22T00:00:00Z", "fiche": "I-0001", "evenement": "naissance", "nom": "idée saine",
         "etat": "proposée", "source": {"chemin": "notes/source.md", "commit": "", "repere": "l. 1", "extrait": "une idée plantée"},
         "porteur": "mot du directeur", "sert": "porte G0", "issue": None, "raison": None, "reveil": None,
         "mots": ["idée"], "derniere_trace": "2026-11-01"}
    for c, v in k.items():
        if c == "extrait":
            e["source"]["extrait"] = v
        elif c == "chemin":
            e["source"]["chemin"] = v
        else:
            e[c] = v
    return e


def main():
    echecs = 0
    with tempfile.TemporaryDirectory() as d:
        git(d, "init", "-q")
        git(d, "config", "user.email", "essai@exemple.invalid")
        git(d, "config", "user.name", "essai")
        os.makedirs(os.path.join(d, "notes"))
        with open(os.path.join(d, "notes/source.md"), "w", encoding="utf-8") as f:
            f.write("# Source\n\nVoici une idée plantée dans la note.\n")
        git(d, "add", ".")
        git(d, "commit", "-q", "-m", "source")
        c = git(d, "rev-parse", "--short", "HEAD")
        cwd = os.getcwd()
        os.chdir(d)
        try:
            def cas(nom, evts, attendu_defaut, avant=None):
                nonlocal echecs
                for e in evts:
                    if not e["source"]["commit"]:
                        e["source"]["commit"] = c
                with open("j.jsonl", "w", encoding="utf-8") as f:
                    for e in evts:
                        f.write(json.dumps(e, ensure_ascii=False) + "\n")
                defauts = vj.verifier("j.jsonl", avant)
                ok = bool(defauts) == attendu_defaut
                print(("PASSE " if ok else "ÉCHEC ") + nom + ("" if ok else f" : {defauts}"))
                echecs += 0 if ok else 1

            cas("sain", [evenement()], False)
            cas("extrait non retrouvé", [evenement(extrait="une idée jamais écrite")], True)
            cas("état hors liste", [evenement(etat="en souffrance")], True)
            cas("abandon sans décision", [evenement(etat="abandonnée", raison="réfutée")], True)
            cas("abandon avec décision et raison", [evenement(etat="abandonnée", raison="réfutée", decision="GO-2026-11-22-01")], False)
            cas("gardée sans réveil", [evenement(etat="gardée de côté", decision="R-12")], True)
            cas("essai sans issue", [evenement(evenement="essai")], True)
            cas("essai avec issue", [evenement(evenement="essai", issue="non évaluable")], False)
            cas("chemin interdit cité", [evenement(chemin="archives-reponses-modeles/x.md")], True)
            cas("verdict valide sans portée", [evenement(etat="testée, verdict valide", decision="R-3")], True)
            # invariant 5 : une ligne perdue entre deux commits
            with open("j.jsonl", "w", encoding="utf-8") as f:
                for e in (evenement(), evenement(fiche="I-0002")):
                    e["source"]["commit"] = c
                    f.write(json.dumps(e, ensure_ascii=False) + "\n")
            git(d, "add", "j.jsonl")
            git(d, "commit", "-q", "-m", "journal")
            ref = git(d, "rev-parse", "--short", "HEAD")
            cas("ajout seul depuis le commit", [evenement(), evenement(fiche="I-0002"), evenement(fiche="I-0003")], False, avant=ref)
            cas("ligne perdue depuis le commit", [evenement(fiche="I-0002")], True, avant=ref)
            cas("fiche née deux fois", [evenement(), evenement()], True)
            # parties : la partie 2 est lue à la suite de la première
            with open("j-partie-0002.jsonl", "w", encoding="utf-8") as f:
                e2 = evenement(fiche="I-0009", extrait="une idée jamais écrite")
                e2["source"]["commit"] = c
                f.write(json.dumps(e2, ensure_ascii=False) + "\n")
            cas("défaut vu dans la partie 2", [evenement()], True)
            os.remove("j-partie-0002.jsonl")
            # vue : souffrance comptée
            with open("j.jsonl", "w", encoding="utf-8") as f:
                f.write(json.dumps(evenement(), ensure_ascii=False) + "\n")
            from datetime import date
            v = vj.vue("j.jsonl", date(2026, 11, 22))
            ok = "(en souffrance)" in v and "Fiches en souffrance : 1" in v
            print(("PASSE " if ok else "ÉCHEC ") + "vue : souffrance comptée")
            echecs += 0 if ok else 1
        finally:
            os.chdir(cwd)
    print(f"{echecs} échec(s)")
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
