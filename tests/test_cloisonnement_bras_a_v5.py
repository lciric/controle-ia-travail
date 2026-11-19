"""Essais de la garde statique du cloisonnement du fichier des rangs par unité, version 5 du code (brouillon 20,
3.5 (b) ; 8.4 ; défaut C-6 de la contre-lecture du code de la version 4). La garde est une fonction du code ; elle est
éprouvée sur **des modules plantés dans un dossier temporaire** — dont les quatre contournements relevés par la
contre-lecture — et sur le code de la relance, version 5. Aucun fichier de rangs n'est ouvert."""
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import analyse_bras_a_v5 as an
from controle_ia.organismes_discrets import cloisonnement_bras_a_v5 as cl

PAQUET = Path(an.__file__).parent

SAINS = {
    "enchainement_sain.py": '''"""Enchaînement qui emploie la statistique de l'analyse, sans toucher aux rangs."""
from controle_ia.organismes_discrets import analyse_bras_a_v5 as an

def moyenne(valeurs):
    return an.intervalle_student(valeurs)
''',
    "module_sans_rapport.py": '''import json

def lire(chemin):
    return getattr(json, "loads")(open(chemin).read())      # getattr ailleurs que sur l'analyse : permis
''',
    "verdicts_planteur.py": '''from controle_ia.organismes_discrets.analyse_bras_a_v5 import NON_CALCULABLE, regle_de_discretion
ETAT = NON_CALCULABLE
''',
    "notes.txt": "le fichier rangs-par-unite-moniteurs-bras-a.jsonl n'est ouvert par aucun agent",   # un texte, non un programme
}

# Chaque artefact : un module planté, et le mot que la violation doit dire.
ARTEFACTS = {
    # --- les quatre contournements de la contre-lecture du code de la version 4 (défaut C-6) ---
    "getattr_nom_coupe.py": ('from controle_ia.organismes_discrets import analyse_bras_a_v5 as an\n'
                             'lire = getattr(an, "lire_" "fichier_des_rangs")\n', "nom réservé"),
    "nom_de_fichier_recolle.py": ('from pathlib import Path\n'
                                  'def lit(d):\n    return Path(d, "rangs-par-" + "unite-moniteurs-bras-a.jsonl").read_text()\n',
                                  "nom du fichier"),
    "import_etoile.py": ("from controle_ia.organismes_discrets.analyse_bras_a_v5 import *\n", "import *"),
    "getattribute_recolle.py": ('from controle_ia.organismes_discrets import analyse_bras_a_v5 as an\n'
                                'def lignes(s):\n    return s.__getattribute__("_pour_l_" + "aire_conditionnelle")("juge", "dose-0.50")\n',
                                "nom réservé"),
    # --- autres détours ---
    "import_direct.py": ("from controle_ia.organismes_discrets.analyse_bras_a_v5 import lire_fichier_des_rangs\n", "nom réservé"),
    "attribut.py": ("from controle_ia.organismes_discrets import analyse_bras_a_v5 as an\nlire = an.lire_fichier_des_rangs\n", "nom réservé"),
    "objet.py": ("from controle_ia.organismes_discrets import analyse_bras_a_v5 as an\n"
                 "def est(s):\n    return isinstance(s, an.RangsScelles)\n", "nom réservé"),
    "methode.py": ("def lignes(s):\n    return s._pour_l_aire_conditionnelle('juge', 'dose-0.50')\n", "nom réservé"),
    "nom_mangle.py": ("def lignes(s):\n    return s._RangsScelles__lignes\n", "nom réservé"),
    "noms_de_la_version_4.py": ("from controle_ia.organismes_discrets.analyse_bras_a_v4 import lire_fichier_des_scores, ScoresScelles\n",
                                "nom réservé"),
    "getattr_variable.py": ("from controle_ia.organismes_discrets import analyse_bras_a_v5 as an\n"
                            "def f(nom):\n    return getattr(an, nom)\n", "accès indirect"),
    "vars_du_module.py": ("import controle_ia.organismes_discrets.analyse_bras_a_v5 as an\nTOUT = vars(an)\n", "accès indirect"),
    "dict_du_module.py": ("from controle_ia.organismes_discrets import analyse_bras_a_v5 as an\nTOUT = an.__dict__\n", "accès indirect"),
    "import_par_son_nom.py": ('import importlib\nan = importlib.import_module("controle_ia.organismes_discrets.analyse_bras_a_v5")\n',
                              "accès indirect"),
    "dunder_import.py": ('an = __import__("controle_ia.organismes_discrets." + "analyse_bras_a_v5", fromlist=["x"])\n', "accès indirect"),
    "attrgetter.py": ("from operator import attrgetter\nfrom controle_ia.organismes_discrets import analyse_bras_a_v5 as an\n"
                      "def f(nom):\n    return attrgetter(nom)(an)\n", "accès indirect"),
    "eval.py": ("from controle_ia.organismes_discrets import analyse_bras_a_v5 as an\ndef f(t):\n    return eval(t)\n", "accès indirect"),
    "nom_de_fichier_entier.py": ('CHEMIN = "diag/rangs-par-unite-moniteurs-bras-a.jsonl"\n', "nom du fichier"),
    "nom_de_fichier_a_trous.py": ('def chemin(d, quoi):\n    return f"{d}/rangs-par-{quoi}-moniteurs-bras-a.jsonl"\n', "nom du fichier"),
    "nom_de_la_version_7.py": ('with open("scores-par-unite-moniteurs-bras-a.jsonl") as f:\n    f.readline()\n', "nom du fichier"),
    "morceau_du_nom.py": ('SUFFIXE = "par-unite"\n', "nom du fichier"),
    "cle_de_la_livraison.py": ('def empreinte(sortie):\n    return sortie["scores_par_unite"]["sha256"]\n', "nom du fichier"),
    "illisible.py": ("def f(:\n    pass\n", "illisible"),
    "lanceur.sh": ("#!/bin/bash\nhead -n 3 diag/rangs-par-unite-moniteurs-bras-a.jsonl\n", "fichier de commandes"),
}


def planter(dossier, fichiers):
    dossier.mkdir(parents=True, exist_ok=True)
    for nom, texte in fichiers.items():
        (dossier / nom).write_text(texte, encoding="utf-8")
    return dossier


def test_cas_sain_des_modules_propres_passent(tmp_path):
    d = planter(tmp_path / "sains", SAINS)
    assert cl.violations_du_cloisonnement([d]) == []
    cl.exiger_cloisonnement_statique([d])
    # le programme de l'aire conditionnelle lui-même est autorisé, sous son nom et lui seul
    (d / "analyse_bras_a_v5.py").write_text((PAQUET / "analyse_bras_a_v5.py").read_text(encoding="utf-8"), encoding="utf-8")
    cl.exiger_cloisonnement_statique([d])
    (d / "copie_de_l_analyse.py").write_text((PAQUET / "analyse_bras_a_v5.py").read_text(encoding="utf-8"), encoding="utf-8")
    with pytest.raises(GardeArret):                                    # la même chose sous un autre nom : refusée
        cl.exiger_cloisonnement_statique([d])


@pytest.mark.parametrize("nom", sorted(ARTEFACTS))
def test_artefact_un_module_plante_est_trouve(tmp_path, nom):
    """Chaque module planté, seul parmi des modules propres, arrête la garde ; la violation le nomme et dit pourquoi."""
    texte, mot = ARTEFACTS[nom]
    d = planter(tmp_path / "plante", {**SAINS, nom: texte})
    trouve = cl.violations_du_cloisonnement([d])
    assert trouve and all(nom in x for x in trouve), trouve
    assert any(mot in x for x in trouve), (mot, trouve)
    with pytest.raises(GardeArret, match="cloisonnement"):
        cl.exiger_cloisonnement_statique([d])
    with pytest.raises(GardeArret):                                    # trouvé aussi au fond d'un sous-dossier, et donné seul
        cl.exiger_cloisonnement_statique([planter(tmp_path / "profond" / "a" / "b", {nom: texte}).parents[1]])
    with pytest.raises(GardeArret):
        cl.exiger_cloisonnement_statique([d / nom])


def test_les_quatre_contournements_de_la_contre_lecture_sont_tous_trouves(tmp_path):
    """Les quatre formes que l'essai de la version 4 ne trouvait pas (contre-lecture, défaut C-6)."""
    for nom in ("getattr_nom_coupe.py", "nom_de_fichier_recolle.py", "import_etoile.py", "getattribute_recolle.py"):
        assert cl.violations_d_un_programme(ARTEFACTS[nom][0], nom), nom
    # les formes à la lettre de la contre-lecture, sur les noms de la version 4
    for source in ('from . import analyse_bras_a_v4 as an\nx = getattr(an, "lire_" "fichier_des_scores")\n',
                   'from pathlib import Path\nx = Path(d, "scores-par-" + "unite-moniteurs-bras-a.jsonl").read_text()\n',
                   'from .analyse_bras_a_v4 import *\n',
                   'x = s.__getattribute__("_pour_l_" + "aire_conditionnelle")\n'):
        assert cl.violations_d_un_programme(source, "plante.py"), source


def test_cote_habilite_exclu_et_racines_exigees(tmp_path):
    """Le côté habilité écrit le fichier : ses modules sont exclus par leur chemin, et ne sont pas lus. Une racine
    absente, ou aucune racine, arrête : une garde qui ne lit rien ne dit rien."""
    texte = ARTEFACTS["nom_de_fichier_entier.py"][0]
    d = planter(tmp_path / "src" / "bras_a_v2_habilite", {"lecture_commune.py": texte})
    planter(tmp_path / "src", {"autres_moniteurs_v8.py": texte, "module_propre.py": "X = 1\n"})
    cl.exiger_cloisonnement_statique([tmp_path / "src"])               # exclus : non lus
    assert cl.violations_du_cloisonnement([tmp_path / "src"], exclus=()) != []         # sans l'exclusion : trouvés
    assert d.is_dir()
    for fautif in ([], [tmp_path / "absent"]):
        with pytest.raises(GardeArret):
            cl.exiger_cloisonnement_statique(fautif)


def test_le_code_de_la_relance_respecte_le_cloisonnement():
    """Sur le code de la relance tel qu'il est : aucun module, hors le programme de l'aire conditionnelle (et ses
    versions antérieures, laissées telles quelles), ne nomme le fichier, ne touche les noms réservés, ni n'atteint
    l'analyse par un détour. Seuls les programmes du paquet des organismes discrets sont parcourus ici, un à un (les
    chemins du côté habilité sont exclus, et rien d'eux n'est lu) ; l'enchaînement de l'analyse donnera à la garde
    `src/` et `scripts/` entiers."""
    programmes = sorted(p for p in PAQUET.glob("*.py"))
    assert {"verdicts_bras_a_v5.py", "mesures_bras_a_v5.py", "graines_bras_a_v5.py", "permutation_etiquettes_bras_a_v5.py",
            "reponses_lecteurs_v5.py", "attentes_bras_a_v5.py", "instrument_appariement_v4.py",
            "epreuves_couverture_bras_a_v3.py"} <= {p.name for p in programmes}
    assert cl.violations_du_cloisonnement(programmes) == []
    cl.exiger_cloisonnement_statique(programmes)
    # dans l'analyse, un seul lecteur des rangs (l'aire conditionnelle) et une seule lecture d'octets (ce fichier)
    analyse = (PAQUET / "analyse_bras_a_v5.py").read_text(encoding="utf-8")
    assert analyse.count("._pour_l_aire_conditionnelle(") == 1 and analyse.count("read_bytes()") == 1 and "open(" not in analyse
    # sans la liste des programmes autorisés, la garde trouve bien l'analyse elle-même : elle n'est pas aveugle
    assert cl.violations_du_cloisonnement([PAQUET / "analyse_bras_a_v5.py"], autorises=()) != []
