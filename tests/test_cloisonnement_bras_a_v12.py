"""Essais de la garde statique du bras A, version 12 du code (brouillon 34, 3.5 (b) ; conventions ; 8.4 ; 6.2). **Version
12** : les programmes autorisés sont ceux de la version 12 ; la porte de l'écart à R9 des versions 11 et 12 des graines
est admise. **Version 11** : les programmes autorisés étaient ceux de la version 11 ; la porte de l'écart à R9 de la version 10 des graines
rejoint les portes refusées (vérification du code de la version 10, M-1). **Version 10** : celle de la version 9 les
avait rejointes. **Version 9** (vérification du code de la version 8, M-5) : un lien physique n'est plus ouvert ; la porte de l'écart à R9 de la
version 8 des graines rejoint les portes refusées. La garde
est éprouvée sur **des dépôts plantés dans un dossier temporaire** — les modules des essais d'attaque des contre-lectures
des versions 4, 5, 6 et 7, et d'autres — puis sur `src/` et `scripts/` du dépôt, **avec ses valeurs par défaut**.

L'élagage des chemins cloisonnés est le défaut du module. Il est éprouvé sur **un faux dépôt fabriqué dans l'essai,
jamais sur les vrais dossiers** ; un crochet d'audit de Python note chaque fichier ouvert et chaque dossier listé, et
l'essai exige qu'aucun ne soit sous un chemin cloisonné. **Vérification du code de la version 7, M-4 : les motifs
répondent sans égard à la casse** (`T07/`, `Bases/` étaient lus). Sur le vrai dépôt, le même crochet **arrête** toute
ouverture d'un chemin cloisonné avant qu'elle ait lieu : si la garde avait un défaut, l'essai échouerait sans qu'aucun
interne de moniteur soit ouvert. Aucun fichier de rangs n'est ouvert."""
import os
import re
import sys
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import analyse_bras_a_v12 as an
from controle_ia.organismes_discrets import cloisonnement_bras_a_v12 as cl
from controle_ia.scellement import sceller

DEPOT = Path(an.__file__).resolve().parents[3]
PAQUET = cl.PAQUET

SAINS = {
    "src/enchainement_sain.py": '''"""Enchaînement qui emploie la statistique de l'analyse, sans toucher aux rangs."""
from controle_ia.organismes_discrets import analyse_bras_a_v12 as an

def moyenne(valeurs):
    return an.intervalle_student(valeurs)
''',
    "src/module_sans_rapport.py": '''import json

def lire(chemin):
    return getattr(json, "loads")(open(chemin).read())      # getattr ailleurs que sur l'analyse : permis
''',
    "src/tirage_sain.py": '''from controle_ia.organismes_discrets import graines_bras_a_v12 as g

def tirage(entropie):
    return g.tirage_de(g.cle("perm", "page"), entropie)
''',
    "scripts/jeton_sans_rapport.py": "_JETON = 'un jeton d une autre affaire'\n",       # le nom, hors de tout import des graines
    "scripts/notes.txt": "le fichier rangs-par-unite-moniteurs-bras-a.jsonl n'est ouvert par aucun agent",   # un texte, non un programme
    "scripts/temoin_sain.py": "x = 1\n",
    "src/porte_de_la_version_11.py": ("from controle_ia.organismes_discrets import graines_bras_a_v11 as g\ndef ouvre(a, b, piece, attendu):\n"
                                      "    return g.admettre_l_entropie_propre_de_la_table_des_identifiants(\n"
                                      "        a, b, reglage=g.ECART_A_R9_REFUSE, go_de_lazar=None, registre_fige=piece, sha256_au_scellement=attendu,\n"
                                      "        registre_courant=piece)\n"),
    "src/porte_de_la_version_12.py": ("from controle_ia.organismes_discrets import graines_bras_a_v12 as g\ndef ouvre(a, b, piece, attendu):\n"
                                     "    return g.admettre_l_entropie_propre_de_la_table_des_identifiants(\n"
                                     "        a, b, reglage=g.ECART_A_R9_REFUSE, go_de_lazar=None, registre_fige=piece, sha256_au_scellement=attendu)\n"),
}

# Chaque artefact : un fichier planté, et le mot que la violation doit dire.
ARTEFACTS = {
    # --- les seize modules de l'essai d'attaque de la contre-lecture du code de la version 5 (quinze passaient) ---
    "src/a_join.py": ('import json\nnom = "-".join(["rangs", "par", "unite"]) + "-moniteurs-bras-a.jsonl"\nlignes = open("runs/x/" + nom).read()\n', "nom du fichier"),
    "src/c_format.py": ('nom = "%s-par-%s" % ("rangs", "unite")\nopen(nom + "-moniteurs-bras-a.jsonl")\n', "nom du fichier"),
    "src/d_inverse.py": ('nom = "lnosj.a-sarb-sruetinom-etinu-rap-sgnar"[::-1]\nopen(nom)\n', "nom du fichier"),
    "src/e_format_methode.py": ('nom = "{}-{}-{}".format("rangs", "par", "unite")\nopen(nom)\n', "nom du fichier"),
    "scripts/analyse_bras_a_v3.py": ('open("rangs-par-unite-moniteurs-bras-a.jsonl").read()\n', "nom du fichier"),       # autorisé par son nom de base
    "scripts/t07_lecture_rapide.py": ('open("rangs-par-unite-moniteurs-bras-a.jsonl").read()\n', "nom du fichier"),      # un fichier, non un dossier `t07…`
    "src/g_importlib_format.py": ('import importlib\nan = importlib.import_module("controle_ia.organismes_discrets.analyse_bras_a_v%d" % 5)\n'
                                  'f = getattr(an, "_".join(["lire", "fichier", "des", "rangs"]))\n', "accès indirect"),
    "scripts/h_makefile.mk": ('lire:\n\tcat runs/rangs-par-unite-moniteurs-bras-a.jsonl\n', "fichier de commandes"),
    "scripts/i_commande.zsh": ('cat runs/rangs-par-unite-moniteurs-bras-a.jsonl\n', "fichier de commandes"),
    "scripts/j_cahier.ipynb": ('{"cells": [{"source": ["open(\\"rangs-par-unite-moniteurs-bras-a.jsonl\\")"]}]}\n', "fichier de commandes"),
    "src/k_jeton.py": ('from controle_ia.organismes_discrets import graines_bras_a_v5 as g\nimport numpy as np\n'
                       't = g.TirageAClef(g._JETON, "bras-a-v2/perm/page", 1, np.random.default_rng(), False)\n', "tirage à clé"),
    "src/temoin_artefact.py": ('open("rangs-par-unite-moniteurs-bras-a.jsonl")\n', "nom du fichier"),
    # --- les quatre contournements de la contre-lecture du code de la version 4 ---
    "src/getattr_nom_coupe.py": ('from controle_ia.organismes_discrets import analyse_bras_a_v12 as an\n'
                                 'lire = getattr(an, "lire_" "fichier_des_rangs")\n', "nom réservé"),
    "src/nom_de_fichier_recolle.py": ('from pathlib import Path\n'
                                      'def lit(d):\n    return Path(d, "rangs-par-" + "unite-moniteurs-bras-a.jsonl").read_text()\n', "nom du fichier"),
    "src/import_etoile.py": ("from controle_ia.organismes_discrets.analyse_bras_a_v12 import *\n", "import *"),
    "src/getattribute_recolle.py": ('from controle_ia.organismes_discrets import analyse_bras_a_v12 as an\n'
                                    'def lignes(s):\n    return s.__getattribute__("_pour_l_" + "aire_conditionnelle")("juge", "dose-0.50")\n', "nom réservé"),
    # --- autres détours ---
    "src/import_direct.py": ("from controle_ia.organismes_discrets.analyse_bras_a_v12 import lire_fichier_des_rangs\n", "nom réservé"),
    "src/lecture_interne.py": ("from controle_ia.organismes_discrets import analyse_bras_a_v12 as an\nlire = an._lire_les_rangs\n", "nom réservé"),
    "src/objet.py": ("from controle_ia.organismes_discrets import analyse_bras_a_v12 as an\n"
                     "def est(s):\n    return isinstance(s, an.RangsScelles)\n", "nom réservé"),
    "src/methode.py": ("def lignes(s):\n    return s._pour_l_aire_conditionnelle('juge', 'dose-0.50')\n", "nom réservé"),
    "src/nom_mangle.py": ("def lignes(s):\n    return s._RangsScelles__lignes\n", "nom réservé"),
    "src/noms_de_la_version_4.py": ("from controle_ia.organismes_discrets.analyse_bras_a_v4 import lire_fichier_des_scores, ScoresScelles\n", "nom réservé"),
    "src/getattr_variable.py": ("from controle_ia.organismes_discrets import analyse_bras_a_v12 as an\n"
                                "def f(nom):\n    return getattr(an, nom)\n", "accès indirect"),
    "src/vars_du_module.py": ("import controle_ia.organismes_discrets.analyse_bras_a_v12 as an\nTOUT = vars(an)\n", "accès indirect"),
    "src/import_par_son_nom.py": ('import importlib\nan = importlib.import_module("controle_ia.organismes_discrets.analyse_bras_a_v12")\n', "accès indirect"),
    "src/import_par_son_nom_joint.py": ('import importlib\nan = importlib.import_module(".".join(["controle_ia", "organismes_discrets", "analyse_bras_a_v12"]))\n'
                                        'x = getattr(an, "MONITEURS")\n', "accès indirect"),
    "src/dunder_import.py": ('an = __import__("controle_ia.organismes_discrets." + "analyse_bras_a_v12", fromlist=["x"])\n', "accès indirect"),
    "src/nom_de_fichier_a_trous.py": ('def chemin(d, quoi):\n    return f"{d}/rangs-par-{quoi}-moniteurs-bras-a.jsonl"\n', "nom du fichier"),
    "src/nom_de_la_version_7.py": ('with open("scores-par-unite-moniteurs-bras-a.jsonl") as f:\n    f.readline()\n', "nom du fichier"),
    "src/cle_de_la_livraison.py": ('def empreinte(sortie):\n    return sortie["scores_par_unite"]["sha256"]\n', "nom du fichier"),
    "src/illisible.py": ("def f(:\n    pass\n", "illisible"),
    "scripts/lanceur.sh": ("#!/bin/bash\nhead -n 3 diag/rangs-par-unite-moniteurs-bras-a.jsonl\n", "fichier de commandes"),
    "scripts/Makefile": ("lire:\n\tcat rangs-par-unite-moniteurs-bras-a.jsonl\n", "fichier de commandes"),
    "scripts/reglages.yaml": ("fichier: rangs-par-unite-moniteurs-bras-a.jsonl\n", "fichier de commandes"),
    # --- vérification du code de la version 6, M-8 : `join` d'une compréhension, chaîne faite de variables, générateur d'un tirage ---
    "src/n1_join_generateur.py": ('nom = "-".join(x for x in ["rangs", "par", "unite"])\nopen(nom)\n', "nom du fichier"),
    "src/n1b_join_liste_en_comprehension.py": ('nom = "_".join([x for x in ("scores", "par", "unite")])\nopen(nom)\n', "nom du fichier"),
    "src/n2_fstring_variables.py": ('a, b = "rangs", "unite"\nopen(f"{a}-par-{b}-moniteurs-bras-a.jsonl")\n', "nom du fichier"),
    "src/n2b_variables_en_chaine.py": ('debut = "rangs-par"\nmilieu = debut + "-unite"\nnom = milieu + "-moniteurs-bras-a.jsonl"\nopen(nom)\n', "nom du fichier"),
    "src/n3_jeton_par_getattr.py": ('import importlib\ng = importlib.import_module("controle_ia.organismes_discrets.graines_" + "bras_a_v7")\nj = getattr(g, "_JE" "TON")\n', "tirage à clé"),
    "src/n6_generateur_remplace.py": ("from controle_ia.organismes_discrets import graines_bras_a_v12 as g\nimport numpy as np\n"
                                      "t = g.tirage_de(g.cle('perm', 'page'), 1)\nobject.__setattr__(t, '_generateur', np.random.default_rng())\n", "tirage à clé"),
    "src/n6b_generateur_lu.py": ("from controle_ia.organismes_discrets import graines_bras_a_v12 as g\ndef f(t):\n    return t._generateur\n", "tirage à clé"),
    "src/porte_de_la_version_6.py": ("from controle_ia.organismes_discrets import graines_bras_a_v6 as g\ndef ouvre(a, b):\n"
                                     "    return g.admettre_l_entropie_propre_de_la_table_des_identifiants(a, b, reglage='x', go_de_lazar='GO-1999-01-01-00')\n", "écart à R9"),
    "src/porte_de_la_version_7.py": ("from controle_ia.organismes_discrets import graines_bras_a_v7 as g\ndef ouvre(a, b, attendu):\n"
                                     "    return g.admettre_l_entropie_propre_de_la_table_des_identifiants(\n"
                                     "        a, b, reglage=g.ECART_A_R9_REFUSE, go_de_lazar=None, sha256_attendu_du_registre=attendu)\n", "écart à R9"),
    "src/porte_de_la_version_10.py": ("from controle_ia.organismes_discrets import graines_bras_a_v10 as g\ndef ouvre(a, b, piece, attendu):\n"
                                      "    return g.admettre_l_entropie_propre_de_la_table_des_identifiants(\n"
                                      "        a, b, reglage=g.ECART_A_R9_REFUSE, go_de_lazar=None, registre_fige=piece, sha256_au_scellement=attendu)\n", "écart à R9"),
    "src/porte_de_la_version_9.py": ("from controle_ia.organismes_discrets import graines_bras_a_v9 as g\ndef ouvre(a, b, piece, attendu):\n"
                                     "    return g.admettre_l_entropie_propre_de_la_table_des_identifiants(\n"
                                     "        a, b, reglage=g.ECART_A_R9_REFUSE, go_de_lazar=None, registre_fige=piece, sha256_au_scellement=attendu)\n", "écart à R9"),
    "src/porte_de_la_version_8.py": ("from controle_ia.organismes_discrets import graines_bras_a_v8 as g\ndef ouvre(a, b, piece, attendu):\n"
                                     "    return g.admettre_l_entropie_propre_de_la_table_des_identifiants(\n"
                                     "        a, b, reglage=g.ECART_A_R9_REFUSE, go_de_lazar=None, registre_fige=piece, sha256_au_scellement=attendu)\n", "écart à R9"),
    # --- essai d'attaque de la vérification du code de la version 7 (`attaques_cloisonnement_v7.py`), modules neufs ---
    "src/n4_jeton_sans_import_ecrit.py": ('import sys\ng = sys.modules["controle_ia.organismes_discrets." + "graines" + "_bras_a_v12"]\nt = vars(g)["_JE" + "TON"]\n', "tirage à clé"),
    "src/n5_rangs_scelles_par_vars.py": ('import sys\nm = sys.modules["controle_ia.organismes_discrets.analyse" + "_bras_a_v12"]\nR = vars(m)["Rangs" + "Scelles"]\n', "nom réservé"),
    "src/n7_concat_variable_reaffectee.py": ('a = "x"\na = "rangs"\nopen(a + "-par-unite.jsonl")\n', "nom du fichier"),
    # --- tirage à clé (M-1) et porte de l'écart à R9 (M-8) ---
    "src/jeton_de_la_version_6.py": ("from controle_ia.organismes_discrets import graines_bras_a_v12\njeton = graines_bras_a_v12._JETON\n", "tirage à clé"),
    "src/registre_des_tirages.py": ("from controle_ia.organismes_discrets import graines_bras_a_v12 as g\ng._AUTHENTIQUES[1] = None\n", "tirage à clé"),
    "src/constructeur_par_son_nom.py": ('from controle_ia.organismes_discrets import graines_bras_a_v12 as g\nC = getattr(g, "Tirage" + "AClef")\n', "tirage à clé"),
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


AUTORISES_DE_LA_VERSION_12 = (PAQUET + "analyse_bras_a_v12.py", PAQUET + "cloisonnement_bras_a_v12.py", PAQUET + "graines_bras_a_v12.py",
                             PAQUET + "arrets_bras_a_v12.py")


def planter_les_autorises(racine, sceller_les=True):
    """Les programmes autorisés, à leur chemin exact, copiés du dépôt et scellés."""
    for chemin in AUTORISES_DE_LA_VERSION_12:
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
    """L'essai d'attaque de la contre-lecture : sur seize modules plantés, la version 5 n'en voyait qu'un. Ici : douze
    sont refusés ; le témoin sain passe ; la lecture d'un dossier est **signalée** sans arrêt ; le nom lu dans la pièce
    scellée passe — c'est la limite écrite (b), et l'essai le dit ; et le programme rangé sous un nom cloisonné
    (`mots_et_cout_…`) est **élagué** : la garde n'y entre pas (C-3), et le dit (`chemins_elagues`)."""
    attaque = ["src/a_join.py", "src/c_format.py", "src/d_inverse.py", "src/e_format_methode.py", "scripts/analyse_bras_a_v3.py",
               "scripts/t07_lecture_rapide.py", "src/g_importlib_format.py",
               "scripts/h_makefile.mk", "scripts/i_commande.zsh", "scripts/j_cahier.ipynb", "src/k_jeton.py", "src/temoin_artefact.py"]
    d = planter_les_autorises(planter(tmp_path / "attaque", {**{n: ARTEFACTS[n][0] for n in attaque}, **LIMITE_ECRITE, **LISTAGE,
                                                             "scripts/outils/mots_et_cout_resume.py": ARTEFACTS["src/temoin_artefact.py"][0],
                                                             "scripts/temoin_sain.py": "x = 1\n"}))
    trouve = cl.violations_de_la_garde_statique(d)
    vus = {n for n in attaque if any(x.startswith(n) for x in trouve)}
    assert vus == set(attaque) and len(attaque) == 12
    assert not any("mots_et_cout" in x for x in trouve) and cl.chemins_elagues(d) == ["scripts/outils/mots_et_cout_resume.py"]
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
    ailleurs = d / "scripts" / "analyse_bras_a_v12.py"                  # le même nom de base, ailleurs
    ailleurs.write_text((DEPOT / PAQUET / "analyse_bras_a_v12.py").read_text(encoding="utf-8"), encoding="utf-8")
    sceller(ailleurs)
    assert any(x.startswith("scripts/analyse_bras_a_v12.py") for x in cl.violations_de_la_garde_statique(d))
    d = planter_les_autorises(planter(tmp_path / "non-scelle", SAINS), sceller_les=False)
    trouve = cl.violations_de_la_garde_statique(d)
    assert len(trouve) == len(AUTORISES_DE_LA_VERSION_12) == 4 and all("empreinte compagnon" in x for x in trouve)
    d = planter_les_autorises(planter(tmp_path / "retouche", SAINS))
    f = d / PAQUET / "analyse_bras_a_v12.py"
    f.write_text(f.read_text(encoding="utf-8") + "\n# retouche\n", encoding="utf-8")
    assert [x for x in cl.violations_de_la_garde_statique(d) if "empreinte compagnon" in x and "analyse_bras_a_v12.py" in x]


# --- Chemins cloisonnés : élagués avant tout parcours, par défaut (vérification du code de la version 6, C-3) -----------------

_SURVEILLANCE = {"active": False, "racine": None, "vus": [], "barriere": None}
# Écriture de l'essai, indépendante de celle du module : ce que la relance ne doit pas ouvrir.
CLOISONNE_SELON_L_ESSAI = re.compile(
    r"(^|/)(bases|sondes|t07[^/]*)/|mots_et_cout_|autres_moniteurs_v|bras_a_v2_habilite|(?<![a-z0-9])t0[._-]?8(?![0-9])"
    r"|^prereg/T0\.6-organismes-v0-v1\.md|^docs/notes/bras-a-moniteurs-v1/(notice-|contre-lecture-code-|verification-lots-)", re.I)


def _crochet(evenement, arguments):
    """Crochet d'audit de Python (il ne se retire pas : il dort hors des essais qui l'allument). Il note chaque fichier
    ouvert et chaque dossier listé sous la racine surveillée ; avec une barrière, il **refuse** l'ouverture d'un chemin
    cloisonné avant qu'elle ait lieu."""
    etat = _SURVEILLANCE
    if not etat["active"] or evenement not in ("open", "os.scandir", "os.listdir") or not arguments:
        return
    chemin = arguments[0]
    if isinstance(chemin, bytes):
        chemin = os.fsdecode(chemin)
    if not isinstance(chemin, str) or not os.path.abspath(chemin).startswith(etat["racine"] + os.sep):
        return
    relatif = os.path.relpath(os.path.abspath(chemin), etat["racine"]).replace(os.sep, "/") + ("" if evenement == "open" else "/")
    etat["vus"].append((evenement, relatif))
    if etat["barriere"] is not None and etat["barriere"].search(relatif):
        raise RuntimeError(f"chemin cloisonné atteint par programme : {relatif} — refusé par l'essai avant toute ouverture")


sys.addaudithook(_crochet)


class surveillance:
    """Allume le crochet sur une racine, le temps d'un bloc ; rend la liste de ce qui a été ouvert ou listé."""

    def __init__(self, racine, barriere=None):
        self.racine, self.barriere = str(Path(racine).resolve()), barriere

    def __enter__(self):
        _SURVEILLANCE.update(active=True, racine=self.racine, vus=[], barriere=self.barriere)
        return _SURVEILLANCE["vus"]

    def __exit__(self, *erreur):
        _SURVEILLANCE.update(active=False, barriere=None)


TEXTE_FAUTIF = 'open("rangs-par-unite-moniteurs-bras-a.jsonl").read()\n'
# Un faux dépôt : sous chaque chemin cloisonné, un programme qui nomme le fichier des rangs (la garde le refuserait si elle le lisait).
CLOISONNES_PLANTES = (
    "src/controle_ia/t07/module_interne.py", "src/controle_ia/t07/sous/dossier/profond.py", "src/controle_ia/t07bbis/module_interne.py",
    "src/controle_ia/bases/module_interne.py", "src/controle_ia/sondes/lineaire/sonde.py", "src/ailleurs/sondes/x.py",
    "scripts/mots_et_cout_t06_v1.py", "scripts/mots_et_cout_bras_a_v2.sh", "scripts/outils/banc_mutations_mots_et_cout_t06_v1.py",
    "scripts/mots_et_cout_donnees/lot.yaml",
    PAQUET + "bras_a_v2_habilite/autres_moniteurs_v8.py", PAQUET + "bras_a_v2_habilite/lecture_commune.py",
    "src/ailleurs/autres_moniteurs_v9.py", "scripts/test_bras_a_v2_habilite_autres_moniteurs_v7.py",
    "scripts/lancer_t08_v1.py", "scripts/T0.8/sondes_de_reference.py", "src/controle_ia/t0_8/x.py", "scripts/shade_t0-8.mk",
    # vérification du code de la version 7, M-4 (`audit_cloisonnement_v7.py`) : les mêmes noms, sous une autre casse
    "src/T07/x.py", "src/Bases/x.py", "src/z/SONDES/x.py", "scripts/Mots_Et_Cout_T06_v1.py", "src/Autres_Moniteurs_V3.py",
    "src/ailleurs/Bras_A_V2_Habilite/lecture.py", "src/T07bis/x.py",
)
NON_CLOISONNES_PLANTES = (                       # des noms voisins, qui ne sont pas cloisonnés : la garde les lit, et les refuse
    "scripts/t07_lecture_rapide.py", "src/controle_ia/bases.py", "src/sondes_de_surface.py", "scripts/rapport08.py",
    "src/controle_ia/t06/x.py", "scripts/mots_et_couts.py", "src/moniteurs_v8.py", "scripts/t080_outil.py",
)


def faux_depot(tmp_path):
    d = planter_les_autorises(planter(tmp_path / "faux-depot", {**SAINS, **{n: TEXTE_FAUTIF for n in CLOISONNES_PLANTES + NON_CLOISONNES_PLANTES}}))
    for n in ("prereg/T0.6-organismes-v0-v1.md", "prereg/T0.6-organismes-v0-v1.md.sha256", "prereg/T0.7-autre.md",
              "docs/notes/bras-a-moniteurs-v1/notice-moniteurs-v3.md", "docs/notes/bras-a-moniteurs-v1/contre-lecture-code-v2.md",
              "docs/notes/bras-a-moniteurs-v1/verification-lots-v1.md", "docs/notes/bras-a-moniteurs-v1/pour-le-texte-du-bras-a-sans-interne-v7.md"):
        (d / n).parent.mkdir(parents=True, exist_ok=True)
        (d / n).write_text("fichier: rangs-par-unite-moniteurs-bras-a.jsonl\n", encoding="utf-8")
    return d


def test_les_chemins_cloisonnes_sont_elagues_avant_tout_parcours_par_defaut(tmp_path):
    """C-3, sur un faux dépôt fabriqué ici. **Avec ses valeurs par défaut**, la garde n'ouvre aucun fichier et ne liste
    aucun dossier sous un chemin cloisonné — `t07…/`, `bases/`, `sondes/`, tout nom qui porte `mots_et_cout_`,
    `autres_moniteurs_v` ou `bras_a_v2_habilite`, toute marque de T0.8 — ; elle n'y arrête donc pas à tort ; elle rend
    leurs noms (`chemins_elagues`). Cas sain : les modules propres passent. Artefact : les mêmes programmes sous des
    noms voisins, non cloisonnés, sont lus et refusés. L'appelant peut ajouter des chemins à élaguer, jamais en
    retirer ; un dossier de départ cloisonné est refusé."""
    d = faux_depot(tmp_path)
    with surveillance(d) as vus:
        trouve = cl.violations_de_la_garde_statique(d)                                     # les défauts de production
        elagues = cl.chemins_elagues(d)
        signales = cl.listages_a_relire(d)
    assert vus and any(x == ("os.scandir", "src/") for x in vus) and ("open", "src/enchainement_sain.py") in vus
    entres = [x for x in vus if CLOISONNE_SELON_L_ESSAI.search(x[1])]
    assert entres == [], entres                                                            # aucun parcours n'y entre, même par programme
    assert {x.split(",")[0].split(" :")[0] for x in trouve} == set(NON_CLOISONNES_PLANTES)   # les voisins sont lus, et refusés
    assert signales == []
    attendus = {"src/controle_ia/t07/", "src/controle_ia/t07bbis/", "src/controle_ia/bases/", "src/controle_ia/sondes/", "src/ailleurs/sondes/",
                "scripts/mots_et_cout_t06_v1.py", "scripts/mots_et_cout_bras_a_v2.sh", "scripts/outils/banc_mutations_mots_et_cout_t06_v1.py",
                "scripts/mots_et_cout_donnees/", PAQUET + "bras_a_v2_habilite/", "src/ailleurs/autres_moniteurs_v9.py",
                "scripts/test_bras_a_v2_habilite_autres_moniteurs_v7.py", "scripts/lancer_t08_v1.py", "scripts/T0.8/", "src/controle_ia/t0_8/",
                "scripts/shade_t0-8.mk",
                "src/T07/", "src/Bases/", "src/z/SONDES/", "scripts/Mots_Et_Cout_T06_v1.py", "src/Autres_Moniteurs_V3.py",
                "src/ailleurs/Bras_A_V2_Habilite/", "src/T07bis/"}                            # M-4 : sans égard à la casse
    assert set(elagues) == attendus and len(elagues) == len(attendus)                      # dits, par leur nom seul
    # la liste par défaut vaut pour tout dossier donné : `prereg` et `docs`, s'ils l'étaient
    with surveillance(d) as vus:
        trouve = cl.violations_de_la_garde_statique(d, ["prereg", "docs"])
        elagues = cl.chemins_elagues(d, ["prereg", "docs"])
    assert trouve == [] and not [x for x in vus if CLOISONNE_SELON_L_ESSAI.search(x[1])]
    assert set(elagues) == {"prereg/T0.6-organismes-v0-v1.md", "prereg/T0.6-organismes-v0-v1.md.sha256",
                            "docs/notes/bras-a-moniteurs-v1/notice-moniteurs-v3.md", "docs/notes/bras-a-moniteurs-v1/contre-lecture-code-v2.md",
                            "docs/notes/bras-a-moniteurs-v1/verification-lots-v1.md"}
    assert ("open", "prereg/T0.7-autre.md") not in vus                                     # un texte, non un programme : jamais ouvert
    # un dossier de départ cloisonné est refusé — la garde ne dit rien de ce qu'elle ne lit pas —, sans y entrer
    for depart in ("src/controle_ia/t07", "src/controle_ia/bases/", PAQUET + "bras_a_v2_habilite", "scripts/mots_et_cout_t06_v1.py",
                   "src/controle_ia/t07/sous/dossier", "prereg/T0.6-organismes-v0-v1.md", "scripts/T0.8"):
        with surveillance(d) as vus:
            with pytest.raises(GardeArret, match="cloisonné"):
                cl.exiger_garde_statique(d, [depart])
            with pytest.raises(GardeArret, match="cloisonné"):
                cl.listages_a_relire(d, ["src", depart])
        assert not [x for x in vus if CLOISONNE_SELON_L_ESSAI.search(x[1])], depart
    # l'appelant ajoute ; il ne retire pas (plus d'argument `exclus`)
    plus = cl.violations_de_la_garde_statique(d, cloisonnes_de_plus=["scripts/t07_lecture_rapide.py", "src/controle_ia/t06", "src/sondes_*"])
    assert {x.split(",")[0] for x in plus} == set(NON_CLOISONNES_PLANTES) - {"scripts/t07_lecture_rapide.py", "src/controle_ia/t06/x.py", "src/sondes_de_surface.py"}
    with pytest.raises(TypeError):
        cl.violations_de_la_garde_statique(d, exclus=())
    for fautif in ("src/", [""], [None], ["/"]):
        with pytest.raises(GardeArret):
            cl.exiger_garde_statique(d, cloisonnes_de_plus=fautif)
    # `est_cloisonne` : jugé sur les noms seuls, composante par composante
    for chemin, dossier, attendu in (("src/controle_ia/t07", True, True), ("src/controle_ia/t07", False, False), ("scripts/t07_x.py", False, False),
                                     ("a/bases/b.py", False, True), ("a/bases", False, False), ("a/bases.py", False, False),
                                     ("a/T08/b", False, True), ("a/lot_T0.8.json", False, True), ("a/t080.py", False, False), ("a/part08.py", False, False),
                                     ("scripts/x_mots_et_cout_y.py", False, True), ("tests/test_autres_moniteurs_v7.py", False, True),
                                     ("prereg/T0.6-organismes-v0-v1.md", False, True), ("prereg/T0.6-organismes-v0-v2.md", False, False),
                                     ("docs/notes/bras-a-moniteurs-v1/notice-x.md", False, True), ("docs/notes/autre/notice-x.md", False, False),
                                     # M-4 : sans égard à la casse
                                     ("src/T07", True, True), ("src/controle_ia/Bases", True, True), ("a/SONDES/b.py", False, True),
                                     ("scripts/MOTS_ET_COUT_x.py", False, True), ("src/Autres_Moniteurs_V2.py", False, True),
                                     ("src/Bras_A_V2_Habilite", True, True), ("Prereg/t0.6-ORGANISMES-v0-v1.md", False, True),
                                     ("Docs/Notes/Bras-A-Moniteurs-V1/Notice-x.md", False, True), ("src/Bases.py", False, False)):
        assert cl.est_cloisonne(chemin, dossier) is attendu, chemin
    with pytest.raises(GardeArret):
        cl.est_cloisonne("src/../../ailleurs", True)


def test_un_lien_symbolique_n_est_ni_suivi_ni_ouvert(tmp_path):
    """Un lien mènerait dans un chemin cloisonné sans le nommer : la garde ne suit aucun lien, n'ouvre pas sa cible, et
    le dit par une violation (« il ne peut pas être dit propre »). Un lien dont le nom est cloisonné est élagué."""
    d = faux_depot(tmp_path)
    (d / "src" / "raccourci").symlink_to(d / "src" / "controle_ia" / "t07", target_is_directory=True)
    (d / "scripts" / "lien.py").symlink_to(d / "src" / "controle_ia" / "bases" / "module_interne.py")
    (d / "scripts" / "mots_et_cout_lien.py").symlink_to(d / "src" / "controle_ia" / "bases" / "module_interne.py")
    with surveillance(d) as vus:
        trouve = cl.violations_de_la_garde_statique(d)
        elagues = cl.chemins_elagues(d)
    assert [x for x in trouve if x.startswith("src/raccourci") and "lien symbolique" in x]
    assert [x for x in trouve if x.startswith("scripts/lien.py") and "lien symbolique" in x]
    assert "scripts/mots_et_cout_lien.py" in elagues and not [x for x in trouve if "mots_et_cout_lien" in x]
    assert not [x for x in vus if CLOISONNE_SELON_L_ESSAI.search(x[1]) or "raccourci" in x[1] or x == ("open", "scripts/lien.py")]
    with pytest.raises(GardeArret, match="garde statique"):
        cl.exiger_garde_statique(d, ["scripts/lien.py"])


def test_un_lien_physique_n_est_pas_ouvert(tmp_path):
    """Vérification du code de la version 8, M-5 (`audit_cloisonnement_v8.py` : `src/lien_physique.py` était lu). Un
    fichier qui porte plusieurs noms pourrait être un fichier cloisonné sous un autre nom : la garde ne l'ouvre pas —
    ni pour ses violations, ni pour ses listages — et le dit par une violation. Cas sain : le même contenu, sous un
    seul nom, est lu comme un programme ordinaire."""
    d = faux_depot(tmp_path)
    cloisonne = d / "src" / "controle_ia" / "bases" / "module_interne.py"
    os.link(cloisonne, d / "src" / "lien_physique.py")                                      # un interne de moniteur, sous un nom qui ne dit rien
    os.link(d / "src" / "enchainement_sain.py", d / "scripts" / "second_nom_d_un_programme_sain.py")
    with surveillance(d) as vus:
        trouve = cl.violations_de_la_garde_statique(d)
        signales = cl.listages_a_relire(d)
    ouverts = {x[1] for x in vus if x[0] == "open"}
    assert not ouverts & {"src/lien_physique.py", "scripts/second_nom_d_un_programme_sain.py", "src/enchainement_sain.py"}
    assert not [x for x in vus if CLOISONNE_SELON_L_ESSAI.search(x[1])]
    for nom in ("src/lien_physique.py", "scripts/second_nom_d_un_programme_sain.py", "src/enchainement_sain.py"):
        assert [x for x in trouve if x.startswith(nom) and "lien physique" in x and "non ouvert" in x], nom
    assert not [x for x in trouve if "lien_physique" in x and "nom du fichier" in x] and signales == []       # son contenu n'a pas été lu
    with pytest.raises(GardeArret, match="garde statique"):
        cl.exiger_garde_statique(d, ["src/lien_physique.py"])                              # donné seul, par son chemin
    seul = planter_les_autorises(planter(tmp_path / "un-seul-nom", {**SAINS, "src/copie.py": TEXTE_FAUTIF}))
    assert [x for x in cl.violations_de_la_garde_statique(seul) if x.startswith("src/copie.py") and "nom du fichier" in x]   # une copie est lue


def test_racines_et_dossiers_exiges(tmp_path):
    """Une racine ou un dossier absent arrête : une garde qui ne lit rien ne dit rien. Un chemin qui remonte, ou
    absolu, est refusé."""
    d = planter_les_autorises(planter(tmp_path / "racines", SAINS))
    cl.exiger_garde_statique(d)
    for racine, dossiers in ((tmp_path / "absent", cl.DOSSIERS_GARDES), (d, []), (d, ["absent"]), (d / "src" / "x.py", ["src"]),
                             (d, "src"), (d, ["../racines/src"]), (d, [str(d / "src")]), (d, [""]), (d, [None])):
        with pytest.raises(GardeArret):
            cl.exiger_garde_statique(racine, dossiers)


def test_la_garde_passee_sur_src_et_scripts_du_depot_avec_ses_valeurs_par_defaut():
    """Contre-lecture du code de la version 5, M-7, et vérification du code de la version 6, C-3. La garde passe sur
    `src/` et `scripts/` du dépôt **telle que l'enchaînement l'appelle, sans aucun élagage fait par l'essai** : aucune
    violation — pas d'arrêt à tort sur le code réel —, et les programmes autorisés répondent à leur empreinte compagnon.
    Le crochet d'audit, armé d'une barrière écrite indépendamment, **refuserait** toute ouverture d'un chemin cloisonné
    avant qu'elle ait lieu : aucune n'est tentée. Les lectures de dossiers sont listées, sans arrêt."""
    with surveillance(DEPOT, barriere=CLOISONNE_SELON_L_ESSAI) as vus:
        trouve = cl.violations_de_la_garde_statique(DEPOT)
        signales = cl.listages_a_relire(DEPOT)
        elagues = cl.chemins_elagues(DEPOT)
    assert trouve == []
    ouverts = {x[1] for x in vus if x[0] == "open"}
    assert len(ouverts) > 300 and {PAQUET + f"{nom}_bras_a_v12.py" for nom in ("analyse", "verdicts", "configuration", "graines", "mesures", "depots", "arrets")} <= ouverts
    assert {f"scripts/constat_de_lancement_discretion_bras_a_v{k}.py" for k in (1, 2, 3, 4, 5)} <= ouverts   # lus, et propres
    assert not [x for x in trouve if "lien physique" in x]                                  # aucun fichier à plusieurs noms sous `src/` ni `scripts/`
    assert not [x for x in vus if CLOISONNE_SELON_L_ESSAI.search(x[1])]                     # rien de cloisonné n'a été ouvert ni listé
    assert elagues and all(CLOISONNE_SELON_L_ESSAI.search(x) for x in elagues)              # ce qui est élagué est dit, par son nom
    assert PAQUET + "bras_a_v2_habilite/" in elagues or not (DEPOT / PAQUET / "bras_a_v2_habilite").exists()
    assert all(PAQUET + nom not in " ".join(signales) for nom in ("verdicts_bras_a_v12.py", "mesures_bras_a_v12.py", "configuration_bras_a_v12.py"))
    assert not [x for x in signales if "constat_de_lancement_discretion" in x]
    # dans l'analyse, un seul lecteur des rangs (l'aire conditionnelle) et le fichier des rangs n'est lu qu'en un endroit
    analyse = (DEPOT / PAQUET / "analyse_bras_a_v12.py").read_text(encoding="utf-8")
    assert analyse.count("._pour_l_aire_conditionnelle(") == 1 and "open(" not in analyse
    # sans la liste des programmes autorisés, la garde trouve bien l'analyse elle-même : elle n'est pas aveugle
    assert cl.violations_d_un_programme(analyse, "analyse_bras_a_v12.py") != []


def test_la_barriere_de_l_essai_arrete_bien_une_ouverture(tmp_path):
    """Le crochet de l'essai, cas sain et artefact (R5) : un fichier ordinaire s'ouvre ; un fichier sous un chemin
    cloisonné est refusé avant d'être ouvert, un dossier cloisonné avant d'être listé."""
    d = faux_depot(tmp_path)
    with surveillance(d, barriere=CLOISONNE_SELON_L_ESSAI):
        assert (d / "src" / "enchainement_sain.py").read_text(encoding="utf-8")
        with pytest.raises(RuntimeError, match="cloisonné"):
            (d / "src" / "controle_ia" / "t07" / "module_interne.py").read_text(encoding="utf-8")
        with pytest.raises(RuntimeError, match="cloisonné"):
            os.listdir(d / "src" / "controle_ia" / "bases")
        with pytest.raises(RuntimeError, match="cloisonné"):
            list((d / "scripts" / "T0.8").rglob("*"))
    assert (d / "src" / "controle_ia" / "t07" / "module_interne.py").read_text(encoding="utf-8") == TEXTE_FAUTIF   # hors de la surveillance
