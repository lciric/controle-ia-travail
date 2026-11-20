"""Essais du module d'entrée du lanceur de l'étape de discrétion, bras A, version 2 : il n'expose que la porte, sa
constante, deux entiers et l'exception ; ce sont les objets mêmes de `graines_bras_a_v12` ; ses noms publics sont
exactement `__all__`, et aucun de ses attributs n'est un module ; sa documentation se borne à la forme des appels ;
la garde statique du cloisonnement (version 13) l'admet ; aucun refus de la porte n'énumère un usage de tirage."""
import hashlib
import re
import types
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import cloisonnement_bras_a_v13 as cl
from controle_ia.organismes_discrets import entree_lanceur_discretion_bras_a_v2 as e
from controle_ia.organismes_discrets import graines_bras_a_v12 as g

DEPOT = Path(__file__).resolve().parents[1]
SOURCE = DEPOT / "src/controle_ia/organismes_discrets/entree_lanceur_discretion_bras_a_v2.py"
EXPOSES = ("ECART_A_R9_ACCORDE", "admettre_l_entropie_propre_de_la_table_des_identifiants", "EPISODES_PAR_TACHE", "PAS_PAR_EPISODE",
           "GardeArret")


def test_les_noms_publics_sont_exactement_ceux_de_la_liste_et_aucun_attribut_n_est_un_module():
    assert e.__all__ == EXPOSES
    assert sorted(n for n in dir(e) if not (n.startswith("__") and n.endswith("__"))) == sorted(EXPOSES)     # ni `_graines`, ni rien d'autre
    assert not [n for n, x in vars(e).items() if isinstance(x, types.ModuleType)]                             # aucun module atteignable par un nom
    for retire in ("tirage_de", "generateur_pour", "cle_lec6", "_graines", "graines_bras_a_v12", "DOSES_VERDICT"):
        assert not hasattr(e, retire), retire


def test_les_memes_objets_que_le_module_des_graines(tmp_path):
    assert e.admettre_l_entropie_propre_de_la_table_des_identifiants is g.admettre_l_entropie_propre_de_la_table_des_identifiants
    assert e.ECART_A_R9_ACCORDE is g.ECART_A_R9_ACCORDE and e.GardeArret is GardeArret is g.GardeArret
    assert (e.EPISODES_PAR_TACHE, e.PAS_PAR_EPISODE) == (g.EPISODES_PAR_TACHE, g.PAS_PAR_EPISODE)
    ligne = f"| GO-2099-01-01-01 | 2099-01-01 | décision | {g.PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9} | — | — | Lazar | essai |"
    registre = tmp_path / "go.md"
    registre.write_text("# Registre\n\n| id | date | type | périmètre | plafond | durée | qui | référence |\n|---|---|---|---|---|---|---|---|\n"
                        + ligne + "\n", encoding="utf-8")
    arguments = dict(reglage=e.ECART_A_R9_ACCORDE, go_de_lazar="GO-2099-01-01-01", registre_fige=registre,
                     sha256_au_scellement=hashlib.sha256(registre.read_bytes()).hexdigest(), registre_courant=registre)
    rendu = e.admettre_l_entropie_propre_de_la_table_des_identifiants(1, 2, **arguments)                      # cas sain
    assert isinstance(rendu, dict) and rendu == g.admettre_l_entropie_propre_de_la_table_des_identifiants(1, 2, **arguments)
    # artefacts : chaque refus lève `GardeArret`, et **aucun message n'énumère un usage de tirage ni une dose**
    vide = tmp_path / "vide.md"
    vide.write_text("# Registre\n", encoding="utf-8")
    refus = [((1, 2), dict(reglage="autre")), ((1, 2), dict(go_de_lazar=None)), ((1, 2), dict(go_de_lazar="GO-2099-09-09-09")),
             ((1, 2), dict(registre_fige=None)), ((1, 2), dict(sha256_au_scellement="0" * 64)), ((1, 2), dict(sha256_au_scellement=None)),
             ((1, 2), dict(registre_courant=vide)), ((1, 2), dict(registre_courant=None)), ((1, 1), {}), ((-1, 2), {}), ((1, True), {})]
    for positions, change in refus:
        with pytest.raises(GardeArret) as x:
            e.admettre_l_entropie_propre_de_la_table_des_identifiants(*positions, **{**arguments, **change})
        message = str(x.value)
        assert not any(usage in message for usage in g.MOTIFS_DES_USAGES), message
        assert re.search(r"dose|verdict|moniteur|Page|aire|permutation|brouillon|prereg", message.replace("dictionnaire", "")) is None, message


def test_la_documentation_se_borne_a_la_forme_des_appels_et_la_garde_statique_admet_le_module():
    source = SOURCE.read_text(encoding="utf-8")
    assert re.search(r"[0-9a-f]{8,}", source) is None                                      # aucune empreinte
    texte = source.replace("étape de discrétion", "").replace("ECART_A_R9_ACCORDE", "")
    for interdit in ("prereg", "brouillon", "dose", "doses", "verdict", "moniteur", "moniteurs", "analyse", "discrétion", "R9", "permutation",
                     "aire", "révocation", "livraison", "règle", "lec6", "tirage", "usage"):
        assert re.search(rf"(?<![\w]){interdit}(?![\w])", texte) is None, interdit
    assert re.search(r"(?<![\w.])\d+\.\d+(?![\w.])", texte) is None                         # aucun numéro de section
    assert re.findall(r"^(?:from|import) .*$", source, re.M) == [
        "from ..gardes import GardeArret", "from .graines_bras_a_v12 import (ECART_A_R9_ACCORDE, EPISODES_PAR_TACHE, PAS_PAR_EPISODE,"]
    assert cl.violations_d_un_programme(source, SOURCE.name) == []
    assert not [x for x in cl.violations_de_la_garde_statique(DEPOT) if SOURCE.name in x]
