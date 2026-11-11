"""Génère la chaîne de session v2 de P3-bis (règle (a') : R-2296, R-2320) à partir de la v1, gardée telle quelle (R12).

Usage : python -I generer_chaine_v2.py DOSSIER_DE_LA_CHAINE SORTIE_DES_ECARTS.txt
Renommages (tous les fichiers) : scripts de la chaîne `<nom>_p3bis_v1` → `_v2` ; journaux `banc-…-p3bis-v1`,
`repetition-…-p3bis-v1` → `-v2` ; `essai_fermeture_p3bis_v2` → `_v3`. Changements propres : liste `PROPRES`, chacun trouvé
exactement une fois. En-tête de deux lignes ajouté. Écrit chaque fichier v2 (refus s'il existe) et la liste des écarts."""
import difflib
import re
import sys
from pathlib import Path

CHAINE = ("lancer", "surveiller", "controle_cinq_minutes", "controles_avant_depense", "recuperation", "detruire", "sceller",
          "repetition_jouet", "repetition_finale", "verifications", "essais_verifications", "essais_lanceur",
          "essais_surveillance", "essais_controles", "essais_recuperation")
FICHIERS = [f"{n}_p3bis_v1.{'py' if n in ('verifications', 'essais_verifications') else 'sh'}" for n in CHAINE]
R_SCRIPTS = re.compile(r"\b(" + "|".join(CHAINE) + r")_p3bis_v1\b")
R_JOURNAUX = re.compile(r"\b(banc-(?:verifications|lanceur|surveillance|controles|recuperation)|repetition-(?:jouet|finale))-p3bis-v1\b")
CONSIGNE = "consigne `consigne-code-p3bis-regle-a-v1.md`, `39300056…`"
PROPRES = {
    "lancer_p3bis_v1.sh": [
        ("printf 'lanceur p3bis v1 %s ; ", "printf 'lanceur p3bis v2 %s ; ")],
    "recuperation_p3bis_v1.sh": [
        ("OUVERTURE=controle_ia.premier_test_ia.ouverture_p3bis_v2   # noms communs v2 (dépendance déclarée)\n",
         "OUVERTURE=controle_ia.premier_test_ia.ouverture_p3bis_v3   # lecture complémentaire lecture_p3bis_v2, règle (a') (R-2296)\n")],
    "verifications_p3bis_v1.py": [
        ("      configuration de P3-bis : seuls écarts à celle de P3 ceux du texte (chemin et empreinte des consignes, deux durées à\n"
         "      null, 30 fils d'entraînement), empreinte des consignes égale à celle du fichier, mode « reel ».\n",
         "      configuration de P3-bis : seuls écarts à celle de P3 ceux du texte (chemin et empreinte des consignes, deux durées à\n"
         "      null, 30 fils d'entraînement, 800 directions de plancher : `n_plancher`, R-2320), empreinte des consignes égale à\n"
         "      celle du fichier, mode « reel ».\n"),
        ("# texte, en-tête : « Écarts à la configuration de P3 (…), seuls écarts : chemin_consignes ; consignes_sha256 ; duree_max_s\n"
         "# et budget_entrainement_s à null ; fils_entrainement à 30 »\n"
         "ECARTS_CONFIG = {\"chemin_consignes\": \"prereg/P3-bis-consignes-v1.md\", \"duree_max_s\": None, \"budget_entrainement_s\": None,\n"
         "                 \"fils_entrainement\": 30}\n",
         "# texte, en-tête : « Écarts à la configuration de P3 (…), seuls écarts : chemin_consignes ; consignes_sha256 ; duree_max_s\n"
         "# et budget_entrainement_s à null ; fils_entrainement à 30 ; n_plancher à 800 » (v2 : règle (a'), R-2296, R-2320)\n"
         "ECARTS_CONFIG = {\"chemin_consignes\": \"prereg/P3-bis-consignes-v1.md\", \"duree_max_s\": None, \"budget_entrainement_s\": None,\n"
         "                 \"fils_entrainement\": 30, \"n_plancher\": 800}\n"),
        ("                m = re.fullmatch(r\"script éprouvé : ([a-z0-9_]+_v1\\.(?:py|sh)) ([0-9a-f]{64})\", x)\n",
         "                m = re.fullmatch(r\"script éprouvé : ([a-z0-9_]+_v2\\.(?:py|sh)) ([0-9a-f]{64})\", x)\n")],
    "essais_verifications_p3bis_v1.py": [
        ("    c[\"consignes_sha256\"] = hashlib.sha256(cons.read_bytes()).hexdigest()\n",
         "    c[\"consignes_sha256\"] = hashlib.sha256(cons.read_bytes()).hexdigest()\n"
         "    c[\"n_plancher\"] = 800                                    # chaîne v2 : règle (a'), R-2320\n"),
        ("    assert \"budget_entrainement_s, chemin_consignes, consignes_sha256, duree_max_s, fils_entrainement\" in r.stdout\n",
         "    assert \"budget_entrainement_s, chemin_consignes, consignes_sha256, duree_max_s, fils_entrainement, n_plancher\" in r.stdout\n"),
        ("    ({\"fils_entrainement\": 32}, \"fils_entrainement = 32\"),\n",
         "    ({\"fils_entrainement\": 32}, \"fils_entrainement = 32\"),\n"
         "    ({\"n_plancher\": 200}, \"n_plancher = 200 ; 800 attendu\"),                # v2 : l'ancien nombre refusé\n"
         "    ({\"n_plancher\": \"SUPPRIMER\"}, \"n_plancher = 'absent'\"),\n"),
        ("def test_config_artefact_brouillon1_non_rempli(tmp_path):\n"
         "    cons = ecrire(tmp_path, \"c.md\", \"x\\n\")\n"
         "    r = cli(\"config\", str(CFG_B1), str(CFG_P3), cons)\n"
         "    assert r.returncode == 1 and \"consignes_sha256\" in r.stderr\n",
         "def test_config_artefact_brouillon1_non_rempli(tmp_path):\n"
         "    cons = ecrire(tmp_path, \"c.md\", \"x\\n\")\n"
         "    r = cli(\"config\", str(CFG_B1), str(CFG_P3), cons)\n"
         "    assert r.returncode == 1 and \"n_plancher = 200 ; 800 attendu\" in r.stderr             # v2 : brouillon 1 à 200\n"
         "    c = json.loads(CFG_B1.read_text(encoding=\"utf-8\"))\n"
         "    c[\"n_plancher\"] = 800\n"
         "    r = cli(\"config\", ecrire(tmp_path, \"b1-800.json\", json.dumps(c)), str(CFG_P3), cons)\n"
         "    assert r.returncode == 1 and \"consignes_sha256\" in r.stderr\n\n\n"
         "def test_preuves_artefact_script_de_la_chaine_v1(tmp_path):\n"
         "    \"\"\"v2 : un journal qui prouve un script `_v1` (chaîne d'avant la règle (a')) est mal formé.\"\"\"\n"
         "    journal_banc(tmp_path, \"banc-verifications-p3bis-v2.log\", extra=\"script éprouvé : verifications_p3bis_v1.py \" + \"0\" * 64 + \"\\n\")\n"
         "    r = cli(\"preuves\", str(tmp_path), \"banc-verifications-p3bis-v2.log\")\n"
         "    assert r.returncode == 1 and \"mal formée\" in r.stderr\n")],
    "repetition_finale_p3bis_v1.sh": [
        ('cp "$H"/*_p3bis_v1.sh "$H"/*_p3bis_v1.py "$R/H/"\n', 'cp "$H"/*_p3bis_v2.sh "$H"/*_p3bis_v2.py "$R/H/"\n')],
    "essais_recuperation_p3bis_v1.sh": [
        ('assert len(l) == 1 and l[0][\\"issue_mecanique\\"] == {\\"issue\\": \\"vu\\", \\"ligne\\": 4}, l\n',
         'assert len(l) == 1 and l[0][\\"issue_mecanique\\"] == {\\"issue\\": \\"vu\\", \\"ligne\\": 4}, l\n'
         'assert sorted(x[\\"commande\\"] for x in m) == [\\"python -m controle_ia.premier_test_ia.lecture\\", \\"python -m controle_ia.premier_test_ia.lecture_p3bis_v2\\"], m\n'
         'assert l[0][\\"etat_decisif\\"][\\"lecture\\"][\\"n_plancher\\"] == 800 and l[0][\\"regle_ancienne_200\\"][\\"lecture\\"][\\"n_plancher\\"] == 200, l\n'),
        ('apres "paquet poussé relu par le banc (vrai module v2) : deux lectures décisives sous le texte, issue mécanique « vu », ligne 4, durées écrites" \\\n',
         'apres "paquet poussé relu par le banc (vrai module v2) : deux lectures décisives sous le texte, lecture complémentaire lecture_p3bis_v2 (règle (a\') sur 800 directions, ancienne règle sur 200), issue mécanique « vu », ligne 4, durées écrites" \\\n')],
    "repetition_jouet_p3bis_v1.sh": [
        ('etape=sondes-figees empreinte=0123456789abcdef sondes=430"', 'etape=sondes-figees empreinte=0123456789abcdef sondes=1630"'),
        ('etape T1-destruction 0 "DESTRUCTION : instance 77777771 détruite"',
         'cat > "$R/ouvrir-paquet.py" <<\'EOF\'\n'
         '"""Paquet des lectures de la tentative 1 ouvert (jouet) : lecture complémentaire v2, règle (a\') sur 800 directions."""\n'
         'import json, sys\n'
         'from controle_ia.premier_test_ia import ouverture_p3bis_v3 as ob\n'
         '_, a = ob.relire_paquet_lectures(open(sys.argv[1], "rb").read(), int(sys.argv[2]))\n'
         'f = dict(ob.membres_de(a))\n'
         'm = [json.loads(v) for k, v in f.items() if k.startswith("runs/") and k.endswith("/manifeste.json")]\n'
         'l = [json.loads(v)["resultat"] for k, v in f.items() if k.endswith("/lecture-p3bis.json")]\n'
         'assert sorted(x["commande"] for x in m) == ["python -m controle_ia.premier_test_ia.lecture", "python -m controle_ia.premier_test_ia.lecture_p3bis_v2"], m\n'
         'assert len(l) == 1 and l[0]["issue_mecanique"] == {"issue": "vu", "ligne": 4}, l\n'
         'assert l[0]["etat_decisif"]["lecture"]["n_plancher"] == 800 and l[0]["regle_ancienne_200"]["lecture"]["n_plancher"] == 200\n'
         'EOF\n'
         'verifier "récupération : paquet ouvert (jouet) : lecture complémentaire lecture_p3bis_v2, règle (a\') sur 800 directions, ancienne règle sur 200, issue « vu », ligne 4" \\\n'
         '    "git --git-dir=\'$R/distant.git\' show refs/heads/calcul/p3bis-reel-v1:diag/p3bis-ferme-20261112-080000-p3bis-reel/paquet-ferme-v1.tar > \'$R/paquet-T1.tar\' && PYTHONPATH=\'$SRC/src\' \'$PYB\' -B \'$R/ouvrir-paquet.py\' \'$R/paquet-T1.tar\' \'$ENT\'"\n'
         'etape T1-destruction 0 "DESTRUCTION : instance 77777771 détruite"')],
    "essais_controles_p3bis_v1.sh": [
        ("c = json.load(open(sys.argv[1], encoding=\"utf-8\")); c[\"consignes_sha256\"] = sys.argv[2]\n",
         "c = json.load(open(sys.argv[1], encoding=\"utf-8\")); c[\"consignes_sha256\"] = sys.argv[2]; c[\"n_plancher\"] = 800   # v2 : R-2320\n")],
}
PROPRE_EN_TETE = {
    "lancer_p3bis_v1.sh": "étiquette du journal de lancement « lanceur p3bis v2 »",
    "recuperation_p3bis_v1.sh": "lectures fermées par `ouverture_p3bis_v3` (lecture complémentaire `lecture_p3bis_v2`, règle (a') décisive)",
    "verifications_p3bis_v1.py": "configuration : `n_plancher` à 800 parmi les écarts permis ; preuves : scripts `_v2`",
    "essais_verifications_p3bis_v1.py": "configuration saine à 800 directions ; artefacts « 200 », « absent », script `_v1` prouvé",
    "essais_controles_p3bis_v1.sh": "configuration du banc à 800 directions ; essai de fermeture v3 (factice du banc)",
    "controles_avant_depense_p3bis_v1.sh": "essai de fermeture v3 rejoué (`scripts/essai_fermeture_p3bis_v3.py`)",
    "essais_recuperation_p3bis_v1.sh": "runs fabriqués par l'essai de fermeture v3 (800 directions), lectures fermées v3 ; "
                                       "R00 : paquet relu, lecture complémentaire `lecture_p3bis_v2`, 800 et 200 directions",
    "repetition_finale_p3bis_v1.sh": "copie de la chaîne par le motif `*_p3bis_v2`",
    "repetition_jouet_p3bis_v1.sh": "run fabriqué par l'essai de fermeture v3 (800 directions), récupération v2 (lectures fermées "
                                    "v3), paquet de la tentative 1 ouvert et lu, ligne `PROGRES` factice à 1 630 sondes",
}


def en_tete(nom: str, py: bool) -> str:
    propre = PROPRE_EN_TETE.get(nom, "aucun autre changement")
    lignes = [f"Chaîne v2 (2026-11-11 ; règle (a') de P3-bis : R-2296, R-2320 ; {CONSIGNE}) : copie de `{nom}`, gardé",
              f"tel quel (R12), noms de la chaîne en v2 ; {propre}."]
    return "\n".join(lignes) + "\n" if py else "".join(f"# {x}\n" for x in lignes)


def generer(dossier: Path, sortie: Path) -> None:
    rapport = []
    for nom in FICHIERS:
        source = (dossier / nom).read_text(encoding="utf-8")
        texte, n1 = R_SCRIPTS.subn(lambda m: f"{m.group(1)}_p3bis_v2", source)
        texte, n2 = R_JOURNAUX.subn(lambda m: f"{m.group(1)}-p3bis-v2", texte)
        n3 = texte.count("essai_fermeture_p3bis_v2")
        texte = texte.replace("essai_fermeture_p3bis_v2", "essai_fermeture_p3bis_v3")
        for a, b in PROPRES.get(nom, []):                   # après les renommages : leurs « b » gardent leur lettre
            if texte.count(a) != 1:
                raise SystemExit(f"{nom} : remplacement propre trouvé {texte.count(a)} fois : {a[:80]!r}")
            texte = texte.replace(a, b)
        if nom.endswith(".py"):
            assert texte.startswith('"""'), nom
            texte = '"""' + en_tete(nom, True) + "\n" + texte[3:]
        else:
            premiere, reste = texte.split("\n", 1)
            assert premiere == "#!/usr/bin/env bash", nom
            texte = premiere + "\n" + en_tete(nom, False) + reste
        cible = dossier / nom.replace("_p3bis_v1.", "_p3bis_v2.")
        if cible.exists():
            raise SystemExit(f"{cible} existe déjà (R12)")
        cible.write_text(texte, encoding="utf-8")
        if (dossier / nom).stat().st_mode & 0o111:
            cible.chmod((dossier / nom).stat().st_mode)
        d = [x for x in difflib.unified_diff(source.splitlines(), texte.splitlines(), lineterm="", n=0)
             if x.startswith(("+", "-")) and not x.startswith(("+++", "---"))]
        rapport.append(f"== {nom} → {cible.name} : {n1} nom(s) de script, {n2} nom(s) de journal, {n3} essai v2→v3, "
                       f"{len(PROPRES.get(nom, []))} changement(s) propre(s) ; {sum(x.startswith('-') for x in d)} ligne(s) "
                       f"retirée(s), {sum(x.startswith('+') for x in d)} ajoutée(s)")
        rapport += ["   " + x for x in d]
    sortie.write_text("\n".join(rapport) + "\n", encoding="utf-8")


if __name__ == "__main__":
    generer(Path(sys.argv[1]), Path(sys.argv[2]))
