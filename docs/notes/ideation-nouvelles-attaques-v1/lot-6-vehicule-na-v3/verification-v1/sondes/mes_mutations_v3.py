"""Mutations du vérificateur sur la copie d'application du lot 6 v3 ; prédictions écrites ici avant tout lancement.
Usage : mes_mutations_v3.py RACINE_ORCHESTRATOR [codes...]"""
import os
import shutil
import subprocess
import sys
import tempfile

C = "pole/course_na_v3.py"
TESTS = ["essais/test_na_lot6_v3_cablage.py", "essais/test_na_lot6_v3_course.py", "essais/test_na_lot6_v3_arrets.py"]
ENVOI = ("        if mp.JournalRequetesColonneNA.__dict__.get(\"journaliser_envoi\") is not _ENVOI_DE_LA_COLONNE \\\n"
         "                or \"journaliser_envoi\" in vars(journal):")

MUT = [
    ("V8", "(= V8 du v2) « au coffre par refus du portier » mis à 0 dans la ligne", C,
     "\"au_coffre_par_refus_du_portier\": comptes_portier[\"au_coffre_par_refus_du_portier\"],",
     "\"au_coffre_par_refus_du_portier\": 0,", "tuée"),
    ("V10", "(= V10 du v2) refus de sceau du journal de la génération 1 tu", C,
     "                arret[\"journal_requetes_g1\"] = f\"scellement refusé ({refus_sceau_g1})\"",
     "                pass", "tuée"),
    ("X3", "envoi posé sur l'instance admis", C, ENVOI,
     "        if mp.JournalRequetesColonneNA.__dict__.get(\"journaliser_envoi\") is not _ENVOI_DE_LA_COLONNE:", "tuée"),
    ("X4", "envoi de la classe remplacé après l'import admis", C, ENVOI,
     "        if \"journaliser_envoi\" in vars(journal):", "tuée"),
    ("X5", "type exact remplacé par isinstance", C,
     "        if type(journal) is not mp.JournalRequetesColonneNA:",
     "        if not isinstance(journal, mp.JournalRequetesColonneNA):", "tuée"),
    ("X6", "type exact remplacé par `journal.__class__ is` (falsifiable)", C,
     "        if type(journal) is not mp.JournalRequetesColonneNA:",
     "        if journal.__class__ is not mp.JournalRequetesColonneNA:", "tuée"),
    ("X7", "type_journal lu par `__class__` au lieu de `type()`", C,
     "        self.type_journal = type(journal).__name__",
     "        self.type_journal = getattr(journal, \"__class__\", type(journal)).__name__", "tuée"),
    ("X8", "nom du bilan revenu au v1", C, "NOM_BILAN = \"bilan-course-na-v3.json\"",
     "NOM_BILAN = \"bilan-course-na-v1.json\"", "tuée"),
    ("X9", "refus trop large : l'état 0 exige aussi le type exact", C,
     "    if etat in ETATS_COLONNE_GARDES:\n        # v3", "    if etat in ETATS_COLONNE:\n        # v3", "tuée"),
    ("X10", "renforcement affaibli : état du journal supérieur admis", C,
     "depart.etat != etat or", "depart.etat < etat or", "tuée"),
    ("X11", "référence de l'envoi relevée à l'appel et non à l'import (la classe modifiée avant import n'est plus vue ; "
            "n'a pas d'effet attendu sur les essais)", C,
     "_ENVOI_DE_LA_COLONNE = mp.JournalRequetesColonneNA.__dict__[\"journaliser_envoi\"]\n",
     "_ENVOI_DE_LA_COLONNE = mp.JournalRequetesColonneNA.__dict__[\"journaliser_envoi\"]\n"
     "_ENVOI_DE_LA_COLONNE_AUTRE = 0\n", "SURVIT (inerte)"),
    ("X12", "la valeur « fabrique absente » : repli silencieux", C,
     "    if not callable(fabrique_journal):\n        raise ArretCablageColonneNA(",
     "    if not callable(fabrique_journal):\n        fabrique_journal = jn.JournalRequetes\n    if False:\n        raise ArretCablageColonneNA(",
     "tuée"),
]


def jouer(racine, m):
    code, quoi, fichier, avant, apres, prediction = m
    base = tempfile.mkdtemp(prefix="vmut3-")
    copie = os.path.join(base, "orchestrator")
    try:
        shutil.copytree(racine, copie, ignore=shutil.ignore_patterns("__pycache__"))
        chemin = os.path.join(copie, fichier)
        with open(chemin, encoding="utf-8") as f:
            texte = f.read()
        n = texte.count(avant)
        if n != 1:
            return f"{code} | {quoi} | INVALIDE (texte présent {n} fois)"
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(texte.replace(avant, apres, 1))
        r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", *TESTS],
                           cwd=copie, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"), capture_output=True, text=True)
        issue = "SURVIT" if r.returncode == 0 else "tuée"
        causes = [l for l in r.stdout.splitlines() if l.startswith("FAILED") or l.startswith("E  ") or l.startswith("ERROR")][:4]
        return f"{code} | {quoi} | prédit : {prediction} | rendu : {issue} | {' // '.join(causes)}"
    finally:
        shutil.rmtree(base, ignore_errors=True)


if __name__ == "__main__":
    racine = os.path.abspath(sys.argv[1])
    codes = sys.argv[2:]
    for m in MUT:
        if not codes or m[0] in codes:
            print(jouer(racine, m), flush=True)
