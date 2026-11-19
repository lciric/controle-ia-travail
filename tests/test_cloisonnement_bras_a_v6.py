"""Essais de la garde statique du bras A, version 6 du code (brouillon 24, 3.5 (b) ; 8.4 ; 6.2). La garde est éprouvée
sur **des dépôts plantés dans un dossier temporaire** — les modules de l'essai d'attaque de la contre-lecture du code de
la version 5 (`contre-lecture-code-v5-pieces/attaques_cloisonnement_v1.py` : seize modules, dont quinze passaient), les
quatre contournements de la contre-lecture de la version 4, et d'autres — puis sur `src/` et `scripts/` du dépôt.
Aucun fichier de rangs n'est ouvert."""
import os
import re
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import analyse_bras_a_v6 as an
from controle_ia.organismes_discrets import cloisonnement_bras_a_v6 as cl
from controle_ia.scellement import sceller

DEPOT = Path(an.__file__).resolve().parents[3]
PAQUET = cl.PAQUET

SAINS = {
    "src/enchainement_sain.py": '''"""Enchaînement qui emploie la statistique de l'analyse, sans toucher aux rangs."""
from controle_ia.organismes_discrets import analyse_bras_a_v6 as an

def moyenne(valeurs):
    return an.intervalle_student(valeurs)
''',
    "src/module_sans_rapport.py": '''import json

def lire(chemin):
    return getattr(json, "loads")(open(chemin).read())      # getattr ailleurs que sur l'analyse : permis
''',
    "src/tirage_sain.py": '''from controle_ia.organismes_discrets import graines_bras_a_v6 as g

def tirage(entropie):
    return g.tirage_de(g.cle("perm", "page"), entropie)
''',
    "scripts/jeton_sans_rapport.py": "_JETON = 'un jeton d une autre affaire'\n",       # le nom, hors de tout import des graines
    "scripts/notes.txt": "le fichier rangs-par-unite-moniteurs-bras-a.jsonl n'est ouvert par aucun agent",   # un texte, non un programme
    "scripts/temoin_sain.py": "x = 1\n",
}

# Chaque artefact : un fichier planté, et le mot que la violation doit dire.
ARTEFACTS = {
    # --- les seize modules de l'essai d'attaque de la contre-lecture du code de la version 5 (quinze passaient) ---
    "src/a_join.py": ('import json\nnom = "-".join(["rangs", "par", "unite"]) + "-moniteurs-bras-a.jsonl"\nlignes = open("runs/x/" + nom).read()\n', "nom du fichier"),
    "src/c_format.py": ('nom = "%s-par-%s" % ("rangs", "unite")\nopen(nom + "-moniteurs-bras-a.jsonl")\n', "nom du fichier"),
    "src/d_inverse.py": ('nom = "lnosj.a-sarb-sruetinom-etinu-rap-sgnar"[::-1]\nopen(nom)\n', "nom du fichier"),
    "src/e_format_methode.py": ('nom = "{}-{}-{}".format("rangs", "par", "unite")\nopen(nom)\n', "nom du fichier"),
    "scripts/analyse_bras_a_v3.py": ('open("rangs-par-unite-moniteurs-bras-a.jsonl").read()\n', "nom du fichier"),       # autorisé par son nom de base
    "scripts/t07_lecture_rapide.py": ('open("rangs-par-unite-moniteurs-bras-a.jsonl").read()\n', "nom du fichier"),      # exclu par un fragment
    "scripts/outils/mots_et_cout_resume.py": ('open("rangs-par-unite-moniteurs-bras-a.jsonl").read()\n', "nom du fichier"),
    "src/g_importlib_format.py": ('import importlib\nan = importlib.import_module("controle_ia.organismes_discrets.analyse_bras_a_v%d" % 5)\n'
                                  'f = getattr(an, "_".join(["lire", "fichier", "des", "rangs"]))\n', "accès indirect"),
    "scripts/h_makefile.mk": ('lire:\n\tcat runs/rangs-par-unite-moniteurs-bras-a.jsonl\n', "fichier de commandes"),
    "scripts/i_commande.zsh": ('cat runs/rangs-par-unite-moniteurs-bras-a.jsonl\n', "fichier de commandes"),
    "scripts/j_cahier.ipynb": ('{"cells": [{"source": ["open(\\"rangs-par-unite-moniteurs-bras-a.jsonl\\")"]}]}\n', "fichier de commandes"),
    "src/k_jeton.py": ('from controle_ia.organismes_discrets import graines_bras_a_v5 as g\nimport numpy as np\n'
                       't = g.TirageAClef(g._JETON, "bras-a-v2/perm/page", 1, np.random.default_rng(), False)\n', "tirage à clé"),
    "src/temoin_artefact.py": ('open("rangs-par-unite-moniteurs-bras-a.jsonl")\n', "nom du fichier"),
    # --- les quatre contournements de la contre-lecture du code de la version 4 ---
    "src/getattr_nom_coupe.py": ('from controle_ia.organismes_discrets import analyse_bras_a_v6 as an\n'
                                 'lire = getattr(an, "lire_" "fichier_des_rangs")\n', "nom réservé"),
    "src/nom_de_fichier_recolle.py": ('from pathlib import Path\n'
                                      'def lit(d):\n    return Path(d, "rangs-par-" + "unite-moniteurs-bras-a.jsonl").read_text()\n', "nom du fichier"),
    "src/import_etoile.py": ("from controle_ia.organismes_discrets.analyse_bras_a_v6 import *\n", "import *"),
    "src/getattribute_recolle.py": ('from controle_ia.organismes_discrets import analyse_bras_a_v6 as an\n'
                                    'def lignes(s):\n    return s.__getattribute__("_pour_l_" + "aire_conditionnelle")("juge", "dose-0.50")\n', "nom réservé"),
    # --- autres détours ---
    "src/import_direct.py": ("from controle_ia.organismes_discrets.analyse_bras_a_v6 import lire_fichier_des_rangs\n", "nom réservé"),
    "src/lecture_interne.py": ("from controle_ia.organismes_discrets import analyse_bras_a_v6 as an\nlire = an._lire_les_rangs\n", "nom réservé"),
    "src/objet.py": ("from controle_ia.organismes_discrets import analyse_bras_a_v6 as an\n"
                     "def est(s):\n    return isinstance(s, an.RangsScelles)\n", "nom réservé"),
    "src/methode.py": ("def lignes(s):\n    return s._pour_l_aire_conditionnelle('juge', 'dose-0.50')\n", "nom réservé"),
    "src/nom_mangle.py": ("def lignes(s):\n    return s._RangsScelles__lignes\n", "nom réservé"),
    "src/noms_de_la_version_4.py": ("from controle_ia.organismes_discrets.analyse_bras_a_v4 import lire_fichier_des_scores, ScoresScelles\n", "nom réservé"),
    "src/getattr_variable.py": ("from controle_ia.organismes_discrets import analyse_bras_a_v6 as an\n"
                                "def f(nom):\n    return getattr(an, nom)\n", "accès indirect"),
    "src/vars_du_module.py": ("import controle_ia.organismes_discrets.analyse_bras_a_v6 as an\nTOUT = vars(an)\n", "accès indirect"),
    "src/import_par_son_nom.py": ('import importlib\nan = importlib.import_module("controle_ia.organismes_discrets.analyse_bras_a_v6")\n', "accès indirect"),
    "src/import_par_son_nom_joint.py": ('import importlib\nan = importlib.import_module(".".join(["controle_ia", "organismes_discrets", "analyse_bras_a_v6"]))\n'
                                        'x = getattr(an, "MONITEURS")\n', "accès indirect"),
    "src/dunder_import.py": ('an = __import__("controle_ia.organismes_discrets." + "analyse_bras_a_v6", fromlist=["x"])\n', "accès indirect"),
    "src/nom_de_fichier_a_trous.py": ('def chemin(d, quoi):\n    return f"{d}/rangs-par-{quoi}-moniteurs-bras-a.jsonl"\n', "nom du fichier"),
    "src/nom_de_la_version_7.py": ('with open("scores-par-unite-moniteurs-bras-a.jsonl") as f:\n    f.readline()\n', "nom du fichier"),
    "src/cle_de_la_livraison.py": ('def empreinte(sortie):\n    return sortie["scores_par_unite"]["sha256"]\n', "nom du fichier"),
    "src/illisible.py": ("def f(:\n    pass\n", "illisible"),
    "scripts/lanceur.sh": ("#!/bin/bash\nhead -n 3 diag/rangs-par-unite-moniteurs-bras-a.jsonl\n", "fichier de commandes"),
    "scripts/Makefile": ("lire:\n\tcat rangs-par-unite-moniteurs-bras-a.jsonl\n", "fichier de commandes"),
    "scripts/reglages.yaml": ("fichier: rangs-par-unite-moniteurs-bras-a.jsonl\n", "fichier de commandes"),
    # --- tirage à clé (M-1) et porte de l'écart à R9 (M-8) ---
    "src/jeton_de_la_version_6.py": ("from controle_ia.organismes_discrets import graines_bras_a_v6\njeton = graines_bras_a_v6._JETON\n", "tirage à clé"),
    "src/registre_des_tirages.py": ("from controle_ia.organismes_discrets import graines_bras_a_v6 as g\ng._AUTHENTIQUES[1] = None\n", "tirage à clé"),
    "src/constructeur_par_son_nom.py": ('from controle_ia.organismes_discrets import graines_bras_a_v6 as g\nC = getattr(g, "Tirage" + "AClef")\n', "tirage à clé"),
    "src/ancienne_porte.py": ("from controle_ia.organismes_discrets import graines_bras_a_v4 as g\n"
                              "def ouvre(a, b):\n    return g.admettre_l_entropie_propre_de_la_table_des_identifiants(a, b, 'x', 'GO-1999-01-01-00')\n", "écart à R9"),
}
# Limite écrite (b) : un nom lu à l'exécution, dans la pièce scellée — la garde ne le voit pas, et l'essai le dit.
LIMITE_ECRITE = {"src/f_depuis_la_piece.py": 'import json\ns = json.load(open("sortie.json"))\nk = [c for c in s if c.startswith("scores")][0]\nopen(s[k]["fichier"])\n'}
# Lecture d'un dossier de fichiers de lignes JSON : signalée, sans arrêt (limite écrite (e)).
LISTAGE = {"src/b_glob.py": 'from pathlib import Path\nfor f in Path("runs/bras-a").glob("*.jsonl"):\n    print(f.read_text())\n'}


def planter(racine, fichiers):
    for nom, texte in fichiers.items():
        f = racine / nom
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(texte, encoding="utf-8")
    (racine / "src").mkdir(exist_ok=True)
    (racine / "scripts").mkdir(exist_ok=True)
    return racine


def planter_les_autorises(racine, sceller_les=True):
    """Les programmes autorisés, à leur chemin exact, copiés du dépôt et scellés."""
    for chemin in (PAQUET + "analyse_bras_a_v6.py", PAQUET + "cloisonnement_bras_a_v6.py", PAQUET + "graines_bras_a_v6.py",
                   PAQUET + "arrets_bras_a_v6.py"):
        f = racine / chemin
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text((DEPOT / chemin).read_text(encoding="utf-8"), encoding="utf-8")
        if sceller_les:
            sceller(f)
    return racine


def test_cas_sain_des_modules_propres_passent(tmp_path):
    d = planter_les_autorises(planter(tmp_path / "sain", SAINS))
    assert cl.violations_de_la_garde_statique(d) == []
    cl.exiger_garde_statique(d)


@pytest.mark.parametrize("nom", sorted(ARTEFACTS))
def test_artefact_un_fichier_plante_est_trouve(tmp_path, nom):
    """Chaque fichier planté, seul parmi des modules propres, arrête la garde ; la violation le nomme et dit pourquoi."""
    texte, mot = ARTEFACTS[nom]
    d = planter_les_autorises(planter(tmp_path / "plante", {**SAINS, nom: texte}))
    trouve = cl.violations_de_la_garde_statique(d)
    assert trouve and all(x.startswith(nom) for x in trouve), trouve
    assert any(mot in x for x in trouve), (mot, trouve)
    with pytest.raises(GardeArret, match="garde statique"):
        cl.exiger_garde_statique(d)
    with pytest.raises(GardeArret):                                    # donné seul, par son chemin
        cl.exiger_garde_statique(d, [nom])


def test_les_seize_modules_de_l_essai_d_attaque_de_la_version_5(tmp_path):
    """L'essai d'attaque de la contre-lecture : sur seize modules plantés, la version 5 n'en voyait qu'un. Ici : treize
    sont refusés ; le témoin sain passe ; la lecture d'un dossier est **signalée** sans arrêt ; le nom lu dans la pièce
    scellée passe — c'est la limite écrite (b), et l'essai le dit."""
    attaque = ["src/a_join.py", "src/c_format.py", "src/d_inverse.py", "src/e_format_methode.py", "scripts/analyse_bras_a_v3.py",
               "scripts/t07_lecture_rapide.py", "scripts/outils/mots_et_cout_resume.py", "src/g_importlib_format.py",
               "scripts/h_makefile.mk", "scripts/i_commande.zsh", "scripts/j_cahier.ipynb", "src/k_jeton.py", "src/temoin_artefact.py"]
    d = planter_les_autorises(planter(tmp_path / "attaque", {**{n: ARTEFACTS[n][0] for n in attaque}, **LIMITE_ECRITE, **LISTAGE,
                                                             "scripts/temoin_sain.py": "x = 1\n"}))
    trouve = cl.violations_de_la_garde_statique(d)
    vus = {n for n in attaque if any(x.startswith(n) for x in trouve)}
    assert vus == set(attaque) and len(attaque) == 13
    assert not any(x.startswith(("scripts/temoin_sain.py", "src/f_depuis_la_piece.py", "src/b_glob.py")) for x in trouve)
    signales = cl.listages_a_relire(d)
    assert len(signales) == 1 and signales[0].startswith("src/b_glob.py") and "glob" in signales[0]      # signalé, sans arrêt
    assert cl.listages_d_un_programme("import os\nfor f in os.listdir('runs'):\n    if f.endswith('.jsonl'):\n        open(f)\n", "x.py")
    assert not cl.listages_d_un_programme("import os\nfor f in os.listdir('runs'):\n    print(f)\n", "x.py")   # limite (e) : extension non écrite


def test_autorisation_par_chemin_exact_et_par_empreinte(tmp_path):
    """Contre-lecture du code de la version 5, C-4. Le programme de l'aire conditionnelle est autorisé **par son chemin
    exact** et **s'il répond à son empreinte compagnon** : le même fichier rangé ailleurs, ou non scellé, ou retouché
    après son scellement, est une violation."""
    d = planter_les_autorises(planter(tmp_path / "ailleurs", SAINS))
    cl.exiger_garde_statique(d)
    ailleurs = d / "scripts" / "analyse_bras_a_v6.py"                  # le même nom de base, ailleurs
    ailleurs.write_text((DEPOT / PAQUET / "analyse_bras_a_v6.py").read_text(encoding="utf-8"), encoding="utf-8")
    sceller(ailleurs)
    assert any(x.startswith("scripts/analyse_bras_a_v6.py") for x in cl.violations_de_la_garde_statique(d))
    d = planter_les_autorises(planter(tmp_path / "non-scelle", SAINS), sceller_les=False)
    trouve = cl.violations_de_la_garde_statique(d)
    assert len(trouve) == 4 and all("empreinte compagnon" in x for x in trouve)
    d = planter_les_autorises(planter(tmp_path / "retouche", SAINS))
    f = d / PAQUET / "analyse_bras_a_v6.py"
    f.write_text(f.read_text(encoding="utf-8") + "\n# retouche\n", encoding="utf-8")
    assert [x for x in cl.violations_de_la_garde_statique(d) if "empreinte compagnon" in x and "analyse_bras_a_v6.py" in x]


def test_exclusion_par_prefixe_de_chemin_exact_et_racines_exigees(tmp_path):
    """Le côté habilité écrit le fichier : son dossier est exclu **par son chemin exact**, et rien n'en est lu. Un
    fichier dont le nom porte seulement un fragment (`t07`, `mots_et_cout_`, `autres_moniteurs_v`) n'est plus exclu.
    Une racine ou un dossier absent arrête : une garde qui ne lit rien ne dit rien."""
    texte = ARTEFACTS["src/temoin_artefact.py"][0]
    d = planter_les_autorises(planter(tmp_path / "habilite", {PAQUET + "bras_a_v2_habilite/lecture_commune.py": texte,
                                                              "scripts/module_propre.py": "X = 1\n"}))
    cl.exiger_garde_statique(d)                                        # exclu : non lu
    assert cl.violations_de_la_garde_statique(d, exclus=()) != []      # sans l'exclusion : trouvé
    for nom in ("src/autres_moniteurs_v8.py", "src/t07_outil.py", "scripts/mots_et_cout_x.py", "src/ailleurs/bras_a_v2_habilite/x.py"):
        e = planter_les_autorises(planter(tmp_path / ("fragment-" + nom.replace("/", "-")), {nom: texte}))
        assert [x for x in cl.violations_de_la_garde_statique(e) if x.startswith(nom)], nom
    for racine, dossiers in ((tmp_path / "absent", cl.DOSSIERS_GARDES), (d, []), (d, ["absent"]), (d / "src" / "x.py", ["src"])):
        with pytest.raises(GardeArret):
            cl.exiger_garde_statique(racine, dossiers)
    with pytest.raises(GardeArret):
        cl.exiger_garde_statique(d, exclus="src/")


def _programmes_du_depot_hors_des_chemins_interdits_a_la_relance():
    """`src/` et `scripts/` du dépôt, **chemins interdits à la relance élagués avant tout parcours** (aucun de ces
    fichiers n'est ouvert, pas même par programme) : même élagage que le contre-lecteur du code de la version 5."""
    interdit = re.compile(r"(^|/)(bases|sondes|t07[^/]*|bras_a_v2_habilite)(/|$)|mots_et_cout_|autres_moniteurs_v|t0?8|T0\.8|t0\.8|habilite", re.I)
    fichiers = []
    for racine in cl.DOSSIERS_GARDES:
        for dp, dns, fns in os.walk(DEPOT / racine):
            rel = Path(dp).relative_to(DEPOT).as_posix()
            dns[:] = [x for x in dns if not interdit.search(f"{rel}/{x}/") and x != "__pycache__"]
            fichiers += [f"{rel}/{f}" for f in fns if not interdit.search(f"{rel}/{f}")]
    return sorted(fichiers)


def test_la_garde_passee_sur_src_et_scripts_du_depot():
    """Contre-lecture du code de la version 5, M-7 : aucun essai ne passait la garde sur `src/` et `scripts/` entiers.
    Ici elle y passe (hors des chemins interdits à la relance) : aucune violation — pas d'arrêt à tort sur le code
    réel, et les programmes autorisés répondent à leur empreinte compagnon. Les lectures de dossiers sont listées, sans
    arrêt."""
    fichiers = _programmes_du_depot_hors_des_chemins_interdits_a_la_relance()
    assert len(fichiers) > 500 and PAQUET + "analyse_bras_a_v6.py" in fichiers and PAQUET + "verdicts_bras_a_v6.py" in fichiers
    assert cl.violations_de_la_garde_statique(DEPOT, fichiers) == []
    cl.exiger_garde_statique(DEPOT, fichiers)
    signales = cl.listages_a_relire(DEPOT, fichiers)
    assert all(PAQUET + nom not in " ".join(signales) for nom in ("verdicts_bras_a_v6.py", "mesures_bras_a_v6.py", "configuration_bras_a_v6.py"))
    # dans l'analyse, un seul lecteur des rangs (l'aire conditionnelle) et le fichier des rangs n'est lu qu'en un endroit
    analyse = (DEPOT / PAQUET / "analyse_bras_a_v6.py").read_text(encoding="utf-8")
    assert analyse.count("._pour_l_aire_conditionnelle(") == 1 and "open(" not in analyse
    # sans la liste des programmes autorisés, la garde trouve bien l'analyse elle-même : elle n'est pas aveugle
    assert cl.violations_d_un_programme(analyse, "analyse_bras_a_v6.py") != []
