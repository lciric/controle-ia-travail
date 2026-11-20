"""Essais du module d'entrée du lanceur de l'étape de discrétion, bras A, version 1 : il rend exactement les objets de
`graines_bras_a_v12`, n'expose rien d'autre, sa documentation ne porte ni renvoi au texte, ni empreinte, ni dose, et la
garde statique du cloisonnement (version 13) l'admet. Un essai fixe aussi ce que les deux fabriques exposées font de
la clé `lec6/{tâche}` : elles la refusent."""
import hashlib
import re
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import cloisonnement_bras_a_v13 as cl
from controle_ia.organismes_discrets import entree_lanceur_discretion_bras_a_v1 as e
from controle_ia.organismes_discrets import graines_bras_a_v12 as g

DEPOT = Path(__file__).resolve().parents[1]
SOURCE = DEPOT / "src/controle_ia/organismes_discrets/entree_lanceur_discretion_bras_a_v1.py"
EXPOSES = ("ECART_A_R9_ACCORDE", "admettre_l_entropie_propre_de_la_table_des_identifiants", "tirage_de", "generateur_pour",
           "cle_lec6", "EPISODES_PAR_TACHE", "PAS_PAR_EPISODE", "GardeArret")


def test_les_memes_objets_que_le_module_des_graines_et_rien_d_autre():
    assert e.admettre_l_entropie_propre_de_la_table_des_identifiants is g.admettre_l_entropie_propre_de_la_table_des_identifiants
    assert e.tirage_de is g.tirage_de and e.generateur_pour is g.generateur_pour and e.GardeArret is GardeArret is g.GardeArret
    assert e.ECART_A_R9_ACCORDE is g.ECART_A_R9_ACCORDE and isinstance(e.ECART_A_R9_ACCORDE, str)
    assert (e.EPISODES_PAR_TACHE, e.PAS_PAR_EPISODE) == (g.EPISODES_PAR_TACHE, g.PAS_PAR_EPISODE)
    assert e.__all__ == EXPOSES
    publics = sorted(n for n in vars(e) if not n.startswith("_") and n != "annotations")
    assert publics == sorted(EXPOSES)                                                      # rien d'autre n'est exposé
    for tache in ("tache-ver-00", "t1"):                                                   # la forme de la clé
        assert e.cle_lec6(tache) == g.cle("lec6", tache) == f"bras-a-v2/lec6/{tache}"
    for fautive in ("a/b", "", None, 3):                                                   # artefact : un identifiant refusé
        with pytest.raises(GardeArret):
            e.cle_lec6(fautive)


def test_les_appels_rendent_ce_que_rend_le_module_des_graines(tmp_path):
    # la porte : cas sain sur un registre fabriqué, et artefact (réglage absent)
    ligne = f"| GO-2099-01-01-01 | 2099-01-01 | décision | {g.PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9} | — | — | Lazar | essai |"
    registre = tmp_path / "go.md"
    registre.write_text("# Registre\n\n| id | date | type | périmètre | plafond | durée | qui | référence |\n|---|---|---|---|---|---|---|---|\n"
                        + ligne + "\n", encoding="utf-8")
    arguments = dict(reglage=e.ECART_A_R9_ACCORDE, go_de_lazar="GO-2099-01-01-01", registre_fige=registre,
                     sha256_au_scellement=hashlib.sha256(registre.read_bytes()).hexdigest(), registre_courant=registre)
    rendu = e.admettre_l_entropie_propre_de_la_table_des_identifiants(1, 2, **arguments)
    assert isinstance(rendu, dict) and rendu == g.admettre_l_entropie_propre_de_la_table_des_identifiants(1, 2, **arguments)
    with pytest.raises(GardeArret):
        e.admettre_l_entropie_propre_de_la_table_des_identifiants(1, 2, **{**arguments, "reglage": "autre"})
    # les fabriques : même suite de nombres que par le module des graines ; un tirage ne sert qu'une fois
    cle = g.cle("perm", "page")
    par_l_entree = e.generateur_pour(e.tirage_de(cle, 7), g.USAGE_PAGE, cle)
    par_les_graines = g.generateur_pour(g.tirage_de(cle, 7), g.USAGE_PAGE, cle)
    assert isinstance(par_l_entree, np.random.Generator) and par_l_entree.integers(0, 2 ** 32, 8).tolist() == par_les_graines.integers(0, 2 ** 32, 8).tolist()
    tirage = e.tirage_de(cle, 7)
    e.generateur_pour(tirage, g.USAGE_PAGE)
    with pytest.raises(GardeArret):
        e.generateur_pour(tirage, g.USAGE_PAGE)


def test_les_deux_fabriques_exposees_refusent_la_cle_lec6():
    """Constat fixé, non corrigé ici : `tirage_de` refuse la clé `lec6/{tâche}`, que le module des graines reconnaît
    sans la tirer, et `generateur_pour` n'a aucun usage pour elle. Le lanceur ne peut donc pas tirer cette clé par ces
    deux fonctions."""
    with pytest.raises(GardeArret, match="la relance ne la tire pas"):
        e.tirage_de(e.cle_lec6("tache-ver-00"), 7)
    assert not any(re.fullmatch(motif, e.cle_lec6("tache-ver-00")) for motif in g.MOTIFS_DES_USAGES.values())


def test_la_documentation_se_borne_a_la_forme_des_appels_et_la_garde_statique_admet_le_module():
    source = SOURCE.read_text(encoding="utf-8")
    assert re.search(r"[0-9a-f]{8,}", source) is None                                      # aucune empreinte
    texte = source.replace("étape de discrétion", "").replace("ECART_A_R9_ACCORDE", "")
    for interdit in ("prereg", "brouillon", "dose", "doses", "verdict", "moniteur", "moniteurs", "analyse", "discrétion", "R9", "permutation",
                     "aire", "révocation", "livraison", "règle"):
        assert re.search(rf"(?<![\w]){interdit}(?![\w])", texte) is None, interdit
    assert re.search(r"(?<![\w.])\d+\.\d+(?![\w.])", texte) is None                         # aucun numéro de section
    assert re.findall(r"^(?:from|import) .*$", source, re.M) == [
        "from __future__ import annotations", "from ..gardes import GardeArret", "from . import graines_bras_a_v12 as _graines"]
    assert cl.violations_d_un_programme(source, SOURCE.name) == []
    assert not [x for x in cl.violations_de_la_garde_statique(DEPOT) if SOURCE.name in x]
