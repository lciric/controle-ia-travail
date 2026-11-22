"""Mutations du lot 6 v5 du véhicule NA-1, à la manière de la v68 et des lots 6 v3 et v4 : pour chaque garde ou compte,
une copie temporaire de l'orchestrateur (où la chaîne entière est posée), un remplacement à texte exact (une seule
occurrence, sinon « invalide »), puis les essais du lot 6 v5 (`-x`) ; une mutation est **tuée** si un essai échoue. Le
témoin non muté (T0) passe ; le témoin inerte (T1) survit.

    python -B essais/mutations_na_lot6_v5.py --racine ORCHESTRATOR --journal JOURNAL.json
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

C = "pole/course_na_v5.py"
R = "pole/registre_na_v4.py"
ESSAIS = "essais/test_na_lot6_v5_course.py"

MUTATIONS = [
    ("T0", "témoin non muté", None, None, None),
    ("T1", "témoin inerte", C, "Aucun message ne recopie un octet", "Aucun message (témoin inerte) ne recopie un octet"),
    ("V01", "juger : A2 levé aussi sur un verdict servi par repli", C, "                if a.get(\"par_repli\") is True:",
     "                if False:"),
    ("V02", "issue « servi par repli » non lue", C, "        if issue not in (ag.ISSUE_OK, ag.ISSUE_SERVI_PAR_REPLI):",
     "        if issue not in (ag.ISSUE_OK,):"),
    ("V03", "issue « arrêt n° 1 après trois refus » non lue", C, "        if issue == ag.ISSUE_ARRET_1_APRES_REPLI:",
     "        if False:"),
    ("V04", "trois refus : classe de repli", C,
     "    if der[\"raison_arret\"] == rg3.RAISON_REFUS:\n        for t in rendu:\n            t[\"classe_issue\"] = rg3.CLASSE_TROIS_REFUS",
     "    if der[\"raison_arret\"] == rg3.RAISON_REFUS:\n        for t in rendu:\n            t[\"classe_issue\"] = rg3.REFUS_SERVI_PAR_REPLI"),
    ("V05", "refus puis sans réponse : classe de repli (erratum 2, (b))", C,
     "        for t in rendu:\n            t[\"classe_issue\"] = rg3.CLASSE_SANS_REPONSE",
     "        for t in rendu[:-1]:\n            t[\"classe_issue\"] = rg3.REFUS_SERVI_PAR_REPLI\n        rendu[-1][\"classe_issue\"] = rg3.CLASSE_SANS_REPONSE"),
    ("V06", "rang de repli décalé d'un cran", C, "\"rang_repli\": t[\"rang_tentative\"] - 1,", "\"rang_repli\": t[\"rang_tentative\"],"),
    ("V07", "« catégorie non lue » écrite comme une catégorie", C,
     "        cat = None if cat in (None, CATEGORIE_NON_LUE) or raison != rg3.RAISON_REFUS else cat",
     "        cat = None if raison != rg3.RAISON_REFUS else cat"),
    ("V08", "raison d'arrêt non relevée", C,
     "        ligne[\"raison_arret\"] = t.get(\"raison_arret\") if isinstance(t, dict) else None",
     "        ligne[\"raison_arret\"] = None"),
    ("V09", "garde du coffre sur toutes les lignes (lecture du lot 5 v1)", R,
     "    return rg3.garde_du_coffre_v3(lignes_v3_de(lignes), generation)",
     "    return rg3.rg.garde_du_coffre(lignes_v3_de(lignes), generation)"),
    ("V10", "fiche sans le contrôle de l'identifiant de sa tentative", R,
     "            if courant is None or l[CHAMP_ID] != courant:", "            if False:"),
    ("V11", "numéro de chaîne hors de la suite admis", R, "            if n != dernier + 1:", "            if False:"),
    ("V12", "rang de l'identifiant non comparé à `rang_repli`", R, "        if r != l.get(\"rang_repli\"):", "        if False:"),
    ("V13", "génération de l'identifiant non comparée", R, "        if g != generation:", "        if False:"),
    ("V14", "forme de l'identifiant relâchée", R, "FORME_ID = re.compile(r\"^T[0-9]{2}-[0-9]{4}-[0-2]$\")",
     "FORME_ID = re.compile(r\"^T[0-9]{1,2}-[0-9]{4}-[0-2]$\")"),
    ("V15", "unicité dans la course non vérifiée", R,
     "            if l[CHAMP_ID] in vus:\n                raise RegistreRefuse(\"identifiant de tentative écrit deux fois dans la course\")",
     "            if False:\n                raise RegistreRefuse(\"identifiant de tentative écrit deux fois dans la course\")"),
    ("V16", "identifiant d'une fiche au rang 0 de sa chaîne", R,
     "        avec_id = [dict(l, **{CHAMP_ID: id_tentative(g, numero, l[\"rang_repli\"])}) for l in lignes]",
     "        avec_id = [dict(l, **{CHAMP_ID: id_tentative(g, numero, l[\"rang_repli\"] if l[\"type_ligne\"] == "
     "\"tentative\" else 0)}) for l in lignes]"),
    ("V17", "code chargé non contrôlé aux générations", C,
     "                _controler_code(controle_code_charge, moment)\n", "                pass\n"),
    ("V18", "absence du contrôle du code chargé tue", C, "        return CODE_CHARGE_NON_DEMANDE", "        return None"),
    ("V19", "modèles de repli dans l'ordre inverse", C, "tuple(r[\"modeles_repli\"]),", "tuple(reversed(r[\"modeles_repli\"])),"),
    ("V20", "replis absents de la configuration admis", C,
     "    if not isinstance(r, dict) or sorted(r) != [\"modeles_repli\", \"pires_repli_usd\"]:", "    if False:"),
    ("V21", "M6 : chaîne servie par repli comptée à la classe de sa réponse", C,
     "        k = rg3.REFUS_SERVI_PAR_REPLI if servie and der[\"rang_repli\"] > 0 else der[\"classe_issue\"]",
     "        k = der[\"classe_issue\"]"),
    ("V22", "replis : la première tentative comptée", C,
     "        if l[\"rang_repli\"] == 0:\n            continue\n        servi = l[\"modele_servi\"] or \"aucun (sans réponse)\"",
     "        servi = l[\"modele_servi\"] or \"aucun (sans réponse)\""),
    ("V23", "M4 : coût des replis rendu à l'espèce", C,
     "        if l[\"rang_repli\"] == 0:\n            e = m4[\"par_espece\"]", "        if True:\n            e = m4[\"par_espece\"]"),
    ("V24", "coffre : « dont servies par repli » faux", C,
     "l[\"type_ligne\"] == rg3.TYPE_FICHE and l[\"rang_repli\"] > 0)", "l[\"type_ligne\"] == rg3.TYPE_FICHE and l[\"rang_repli\"] >= 0)"),
    ("V25", "chaînes servies non écrites au registre à l'aiguillage", C,
     "                self._ecrire_chaine(rep.tentatives, rep.case, rep.role, classe_servie=issue.classe_appel,\n"
     "                                    fiches=issue.fiches)\n", ""),
    ("V26", "trois refus comptés dans M6", C,
     "        if der[\"raison_arret\"] == rg3.RAISON_REFUS or der[\"raison_arret\"] == RAISON_REFUS_SANS_REPLI:",
     "        if False:"),
    ("V27", "unicité dans la course non appelée par la course", C, "                rg4.verifier_unicite_course(lignes_reg)\n", ""),
    ("V28", "portier du v1 à la place du v3 (passeport sans `par_repli`)", C,
     "        self.portier = pt3.PortierNAV3(consigne=", "        self.portier = pt.PortierNA(consigne="),
    ("V29", "chaîne servie par repli écrite au rang 0 (marque perdue au registre servi)", C,
     "\"rang_repli\": t[\"rang_tentative\"] - 1,", "\"rang_repli\": 0,"),
    ("V30", "numéro de chaîne non avancé après une chaîne", R, "        self.numero_chaine = numero\n", ""),
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
        env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", ESSAIS],
                           cwd=copie, capture_output=True, text=True, timeout=1800, env=env)
        derniere = (r.stdout.strip().splitlines() or [""])[-1]
        return {"id": mid, "description": desc, "issue": "survit" if r.returncode == 0 else "tuée", "resume": derniere}


def principal(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--racine", required=True)
    p.add_argument("--journal", required=True)
    a = p.parse_args(argv)
    rendu = []
    for m in MUTATIONS:
        rendu.append(jouer(os.path.abspath(a.racine), *m))
        print(json.dumps(rendu[-1], ensure_ascii=False), flush=True)
    bilan = {"jouees": len(rendu), "tuees": sum(1 for x in rendu if x["issue"] == "tuée"),
             "survivantes": [x["id"] for x in rendu if x["issue"] == "survit"],
             "invalides": [x["id"] for x in rendu if x["issue"] == "invalide"]}
    with open(a.journal, "x", encoding="utf-8") as f:
        json.dump({"bilan": bilan, "mutations": rendu}, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(json.dumps(bilan, ensure_ascii=False))
    return 0 if bilan["survivantes"] == ["T0", "T1"] and not bilan["invalides"] else 1


if __name__ == "__main__":
    sys.exit(principal())
