"""Mutations du vérificateur du lot 10 a : fautes par construction, prédictions écrites d'avance dans PREDICTIONS.

Usage : python -B mutations_verificateur.py ORCH JOURNAL.json
Pour chaque mutation : copie neuve de ORCH ; un remplacement exact dans le module ; les essais du lot (99) d'une part, les
sondes du vérificateur d'autre part, joués à part ; code rendu par chacun.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

MP = "pole/matiere_premiere_na_v1.py"
LOT = "essais/test_na_lot10a_v1_matiere_premiere.py"
SONDES = "essais/test_verif_lot10a.py"

MUTATIONS = [
    ("V1", "examiner_texte : str.splitlines remplacé par split('\\n')",
     [(MP, "        for i, ligne in enumerate(texte.splitlines(), start=1):\n",
       "        for i, ligne in enumerate(texte.split(\"\\n\"), start=1):\n")],
     "lot : survit (code 0) ; sondes : échouent (V-A, 7 cas)"),
    ("V2", "E4 : égalité à l'empreinte épinglée remplacée par « empreinte non vide »",
     [(MP, "    if obj[CLE_EMPREINTE_ADDITIF] != attendue:\n", "    if not obj[CLE_EMPREINTE_ADDITIF]:\n")],
     "lot : tuée (empreinte fausse) ; sondes : échouent"),
    ("V3", "E4 : contrôle de l'empreinte épinglée (hexadécimale, présente) retiré",
     [(MP, "    if type(attendue) is not str or _HEXA64.match(attendue) is None:\n", "    if False:\n")],
     "lot : survit ; sondes : échouent (V-B, V-B2)"),
    ("V4", "tenue (ii) : seuls les 2000 premiers octets de la requête sont examinés",
     [(MP, "            constats = colonne.examiner_octets(requete.octets)\n",
       "            constats = colonne.examiner_octets(requete.octets[:2000])\n")],
     "lot : tuée (l'énoncé planté est en fin de requête, au-delà de 2000 octets) ; sondes : échouent (V-E)"),
    ("V5", "environnement : fragment « COLONNE_MATIERE » retiré",
     [(MP, "FRAGMENTS_ENV_INTERDITS = (\"MATIERE_PREMIERE\", \"COLONNE_MATIERE\")",
       "FRAGMENTS_ENV_INTERDITS = (\"MATIERE_PREMIERE\",)")],
     "lot : survit ; sondes : échouent (V-D)"),
    ("V6", "E5 : source fixée en repli quand aucune fonction n'est donnée",
     [(MP, "        raise ColonneNonChargee(\"l'identifiant de ligne se reçoit par une fonction donnée au chargeur (E5)\")\n",
       "        octets_identifiant_ligne = lambda r, e: r.to_bytes(6, \"big\")\n")],
     "lot : tuée ; sondes : sans objet (réussissent)"),
    ("V7", "E4 : test d'existence du fichier retiré (équivalent : l'ouverture échoue et refuse de même)",
     [(MP, "    if type(chemin) is not str or not os.path.isfile(chemin):\n", "    if type(chemin) is not str:\n")],
     "lot : survit (mutant équivalent : refus par « illisible », toujours (b)) ; sondes : réussissent"),
    ("V8", "tenue (iii) : passe sur le fichier entier retirée (ne garde que les lignes de tentative)",
     [(MP, "    for c in depart.colonne.examiner_octets(octets):\n        if all(",
       "    for c in ():\n        if all(")],
     "lot : survit (aucun essai ne plante un énoncé hors ligne de tentative) ; sondes : réussissent"),
]


def jouer(dossier, essais):
    env = {"PATH": os.environ.get("PATH", ""), "PYTHONDONTWRITEBYTECODE": "1", "LANG": "C.UTF-8"}
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", essais], cwd=dossier, env=env,
                       capture_output=True, text=True)
    lignes = [l for l in r.stdout.splitlines() if l.strip()]
    return r.returncode, (lignes[-1] if lignes else "")


def main(argv):
    orch, journal = argv
    if os.path.exists(journal):
        print("journal existant", file=sys.stderr)
        return 2
    racine = tempfile.mkdtemp(prefix="verif-mut-")
    rendu = []
    try:
        for ident, nom, remplacements, prediction in [("V0", "témoin non muté", [], "lot : 0 ; sondes : 0")] + MUTATIONS:
            d = os.path.join(racine, ident)
            shutil.copytree(orch, d, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
            valide = True
            for fichier, ancien, nouveau in remplacements:
                chemin = os.path.join(d, fichier)
                with open(chemin, encoding="utf-8") as f:
                    s = f.read()
                if s.count(ancien) != 1:
                    valide = False
                    break
                with open(chemin, "w", encoding="utf-8") as f:
                    f.write(s.replace(ancien, nouveau, 1))
            e = {"id": ident, "nom": nom, "prediction": prediction, "valide": valide}
            if valide:
                e["lot"] = jouer(d, LOT)
                e["sondes"] = jouer(d, SONDES)
            rendu.append(e)
            print(ident, nom, "| prédiction :", prediction, "| rendu :", e.get("lot"), e.get("sondes"), "valide" if valide else "INVALIDE")
            shutil.rmtree(d, ignore_errors=True)
    finally:
        shutil.rmtree(racine, ignore_errors=True)
    with open(journal, "x", encoding="utf-8") as f:
        f.write(json.dumps(rendu, ensure_ascii=False, indent=1) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
