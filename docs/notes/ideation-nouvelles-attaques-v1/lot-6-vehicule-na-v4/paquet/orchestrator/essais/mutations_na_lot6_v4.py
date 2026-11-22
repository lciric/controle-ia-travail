"""Mutations du lot 6 v4 du véhicule NA-1, à la manière de la v68 et du v3 : pour chaque garde ou compte, une copie
temporaire de l'orchestrateur d'essai, un remplacement à texte exact (le texte cherché y est une seule fois, sinon la
mutation est « invalide »), puis les essais du lot ; une mutation est **tuée** si un essai échoue. Le témoin non muté
(T0) doit passer ; le témoin inerte (T1, une ligne de la docstring changée) doit survivre.

    python -B essais/mutations_na_lot6_v4.py --racine ORCHESTRATOR --journal JOURNAL.json
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

C = "pole/course_na_v4.py"
ESSAIS = "essais/test_na_lot6_v4.py"

MUTATIONS = [
    ("T0", "témoin non muté", None, None, None),
    ("T1", "témoin inerte", C, "Bibliothèque\nstandard seule.", "Bibliothèque\nstandard seule (témoin inerte)."),
    ("V01", "P12 : chaîne servie par repli comptée à la classe de la réponse servie", C,
     "            return SERVI_PAR_REPLI, None", "            return classe_servie, None"),
    ("V02", "M6 : toutes les tentatives comptées, non la seule première", C,
     "        if l[\"rang_repli\"] != 0 or l[\"espece\"] not in ESPECES_PROPOSEUSES",
     "        if l[\"espece\"] not in ESPECES_PROPOSEUSES"),
    ("V03", "n° 5 : lignes de tentative comptées comme fiches rendues (lecture du lot 5 v1)", C,
     "    de_g = [l for l in lignes_fiches(lignes) if", "    de_g = [l for l in lignes if"),
    ("V04", "n° 5 : fiches servies par repli hors de la garde", C,
     "if l.get(\"generation\") == generation]", "if l.get(\"generation\") == generation and l[\"rang_repli\"] == 0]"),
    ("V05", "n° 5 : un quart exactement arrête", C, "    depasse = 4 * au_coffre > rendues",
     "    depasse = 4 * au_coffre >= rendues"),
    ("V06", "n° 31 : modèle servi autre non vu", C, "            if servi != config.modele_reel[demande]:",
     "            if False:"),
    ("V07", "n° 31 : modèle servi absent non vu", C, "            if type(servi) is not str or not servi:",
     "            if False:"),
    ("V08", "A6 : repli après une tentative non refusée admis", C, "        if not t.refusee:", "        if False:"),
    ("V09", "suite fermée des modèles demandés non vérifiée", C, "        if demande != suite[i]:", "        if False:"),
    ("V10", "repli sur une espèce sans repli admis", C, "    if len(brutes) > len(suite):", "    if False:"),
    ("V11", "usage manquant compté sous le pire", C,
     "            if cout != montant(config.pires[(espece, demande)]):", "            if False:"),
    ("V12", "catégorie devinée hors refus admise", C,
     "        if categorie is not None and raison != RAISON_REFUS:", "        if False:"),
    ("V13", "coût de la tentative recopié aux lignes de fiche (double compte)", C, "FICHES_RENDUES, cout_zero=True)",
     "FICHES_RENDUES, cout_zero=False)"),
    ("V14", "fiche attribuée à la première tentative, non au modèle servi", C, "        t_servie = tentatives[-1]",
     "        t_servie = tentatives[0]"),
    ("V15", "M4 : coût des replis rendu à l'espèce", C,
     "        if l[\"rang_repli\"] == 0:\n            e = g[\"par_espece\"]",
     "        if True:\n            e = g[\"par_espece\"]"),
    ("V16", "M3 « espèces seules » avec les fiches de repli", C,
     "[\"scellee\"] + ([\"especes_seules\"] if l[\"rang_repli\"] == 0 else [])", "[\"scellee\", \"especes_seules\"]"),
    ("V17", "replis : nombre par modèle demandé faussé", C, "        d[\"nombre\"] += 1", "        d[\"nombre\"] += 2"),
    ("V18", "n° 33 : module hors table admis", C, "        if rel not in table:", "        if False:"),
    ("V19", "n° 33 : autre empreinte admise", C, "        if h != table[rel]:", "        if False:"),
    ("V20", "n° 33 : module protégé hors racine admis", C,
     "        if not sous_racine:\n            raise", "        if False:\n            raise"),
    ("V21", "n° 33 : espace protégé ignoré", C, "        protege = any(", "        protege = False and any("),
    ("V22", "n° 33 : empreinte de la table non vérifiée", C,
     "    if hashlib.sha256(octets).hexdigest() != sha256_attendu:", "    if False:"),
    ("V23", "passe X avec case admise", C, "        if espece == ESPECE_SANS_CASE:\n            if case is not None:",
     "        if espece == ESPECE_SANS_CASE:\n            if False:"),
    ("V24", "M6 : sous-compte « cause non établie, en repli » perdu", C,
     "        if l[\"rang_repli\"] > 0 and l[\"raison_arret\"] is None", "        if False"),
    ("V25", "n° 34 : pire manquant non vu", C, "                if (e, m) not in self.pires:", "                if False:"),
    ("V26", "trois refus comptés en M6", C, "    return CLASSE_ARRET_1, None", "    return REFUS_DU_MODELE, None"),
    ("V27", "rôle non proposeur à la classe du portier", C,
     "        return (classe_servie if proposeur else CLASSE_HORS_M6), None", "        return classe_servie, None"),
    ("V28", "M6 par case rangé par espèce", C, "        _plus(g[\"par_case\"].setdefault(l[\"case\"], {}), k)",
     "        _plus(g[\"par_case\"].setdefault(l[\"espece\"], {}), k)"),
    ("V29", "tentative refusée suivie d'une servie : classe de l'arrêt n° 1", C,
     "    if der.servie:\n        return SERVI_PAR_REPLI\n", "    if der.servie:\n        return CLASSE_ARRET_1\n"),
    ("V30", "filiation « aucune » écrite telle quelle", C, "    if v is None or v == \"aucune\":", "    if v is None:"),
    ("V31", "écriture avant la fin des vérifications (atomicité)", C,
     "            ligne = self._champs_tentative(generation, espece, case, t_servie, FICHES_RENDUES, cout_zero=True)",
     "            for t0 in tentatives:\n                self.registre.ajouter(self._champs_tentative(generation, espece, case, t0, "
     "FICHES_RENDUES) | {\"identifiant\": \"x\", \"classe\": None, \"filiation\": None})\n"
     "            ligne = self._champs_tentative(generation, espece, case, t_servie, FICHES_RENDUES, cout_zero=True)"),
]


def jouer(racine, mid, desc, fichier, avant, apres):
    with tempfile.TemporaryDirectory() as tmp:
        copie = os.path.join(tmp, "orchestrator")
        shutil.copytree(racine, copie)
        if fichier is not None:
            chemin = os.path.join(copie, fichier)
            with open(chemin, encoding="utf-8") as f:
                texte = f.read()
            if texte.count(avant) != 1:
                return {"id": mid, "description": desc, "issue": "invalide", "occurrences": texte.count(avant)}
            with open(chemin, "w", encoding="utf-8") as f:
                f.write(texte.replace(avant, apres))
        r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", ESSAIS],
                           cwd=copie, capture_output=True, text=True, timeout=600)
        derniere = (r.stdout.strip().splitlines() or [""])[-1]
        return {"id": mid, "description": desc, "issue": "survit" if r.returncode == 0 else "tuée", "resume": derniere}


def principal(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--racine", required=True)
    p.add_argument("--journal", required=True)
    a = p.parse_args(argv)
    rendu = [jouer(os.path.abspath(a.racine), *m) for m in MUTATIONS]
    bilan = {"jouees": len(rendu), "tuees": sum(1 for x in rendu if x["issue"] == "tuée"),
             "survivantes": [x["id"] for x in rendu if x["issue"] == "survit"],
             "invalides": [x["id"] for x in rendu if x["issue"] == "invalide"]}
    with open(a.journal, "x", encoding="utf-8") as f:
        json.dump({"bilan": bilan, "mutations": rendu}, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(json.dumps(bilan, ensure_ascii=False))
    attendu = bilan["survivantes"] == ["T0", "T1"] and not bilan["invalides"]
    return 0 if attendu else 1


if __name__ == "__main__":
    sys.exit(principal())
