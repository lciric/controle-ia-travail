"""Règle composée de désignation, v5 (texte scellé, 5.1 ; section 13, `designation_v5.py`)."""
import copy
import inspect
import json

import pytest
from iib_v5_outils import ecrire_scelle

from controle_ia.gardes import GardeArret
from controle_ia.iib import configuration_v5 as cf
from controle_ia.iib import designation_v5 as dg

SHA_ETAL = "e" * 64
VARIANTES = {"N": "a" * 64, "P": "b" * 64}


def _oracle(o, remplit, motif=None, tours=None, epreuve=None):
    return {"oracle": o, "remplit": remplit, "motif": motif, "epreuve": epreuve, "tours": tours,
            "phrase": f"phrase de l'oracle {o} ({'part' if remplit else motif})"}


def _branches(tmp_path, n, p, non_calculable=None, nom="branches.json", sha=SHA_ETAL):
    contenu = {"schema": cf.SCHEMA_BRANCHES, "references": {"etalonnage": {"sha256": sha}}, "non_calculable": non_calculable,
               "oracles": None if non_calculable else {"N": n, "P": p}}
    chemin = tmp_path / nom
    ecrire_scelle(chemin, contenu)
    return chemin


def test_les_quatre_combinaisons_rendent_N_N_P_ne_part_pas(tmp_path):
    oui_n, oui_p = _oracle("N", True, tours=14), _oracle("P", True, tours=12)
    non_n, non_p = _oracle("N", False, "rapport"), _oracle("P", False, "tours")
    attendus = [(oui_n, oui_p, "N"), (oui_n, non_p, "N"), (non_n, oui_p, "P"), (non_n, non_p, "ne_part_pas")]
    for i, (n, p, issue) in enumerate(attendus):
        r = dg.designer(_branches(tmp_path, n, p, nom=f"b{i}.json"), SHA_ETAL, VARIANTES)
        assert r["issue"] == issue
        if issue == "N":
            assert r["these"] == "excès borné en niveau" and r["variante_consigne"] == {"variante": "N", "sha256": "a" * 64} and r["tours"] == 14
            assert r["phrases"][0].startswith("Sous la thèse « excès borné en niveau », désignée par la règle scellée avant l'étalonnage (issue [N]) : ")
            assert r["phrases"][1].startswith("L'autre oracle, calculé sur les mêmes épisodes, aurait rendu : phrase de l'oracle P")
        elif issue == "P":
            assert r["these"] == "petit ajout à chaque pas, sachant les précédents" and r["variante_consigne"]["sha256"] == "b" * 64 and r["tours"] == 12
            assert "l'oracle à contexte réécrit n'a pas rempli ses conditions de départ (motif : rapport)" in r["phrases"][0]
            assert "la thèse d'un excès borné en niveau n'a pas été éprouvée" in r["phrases"][0]
        else:
            assert r["these"] is None and r["tours"] is None and r["variante_consigne"] is None
            assert r["phrases"][0].startswith("Oracle [N] : ") and r["phrases"][1].startswith("Oracle [P] : ")
        assert r["phrases"][-1].startswith("Rien de ceci ne dit quoi que ce soit du premier coût")


def test_N_en_defaut_et_P_sain_rend_P_avec_le_message_de_l_epreuve_de_N(tmp_path):
    n = _oracle("N", False, "en_defaut", epreuve="oracle en défaut (centrage : pente de fuite)")
    r = dg.designer(_branches(tmp_path, n, _oracle("P", True, tours=12)), SHA_ETAL, VARIANTES)
    assert r["issue"] == "P" and r["message_epreuve_de_N"] == "oracle en défaut (centrage : pente de fuite)"
    assert "(motif : oracle en défaut (centrage : pente de fuite))" in r["phrases"][0]


def test_coupe_en_echec_ne_part_pas_les_deux_oracles_en_defaut(tmp_path):
    n = _oracle("N", False, "en_defaut", epreuve="oracle en défaut (coupe)")
    p = _oracle("P", False, "en_defaut", epreuve="oracle en défaut (coupe)")
    r = dg.designer(_branches(tmp_path, n, p), SHA_ETAL, VARIANTES)
    assert r["issue"] == "ne_part_pas" and r["motifs"] == {"N": "en_defaut", "P": "en_defaut"} and r["these"] is None


@pytest.mark.parametrize("motif", ["schéma faux (entrée 3)", "épisodes manquants (63 épisodes honnêtes complets pour l'oracle N, 64 attendus)",
                                   "épisodes manquants (63 épisodes régénérés complets pour l'oracle P, 64 attendus)", "fichier d'entrées absent"])
def test_etalonnage_non_calculable_sans_these_ni_nombre_de_tours(tmp_path, motif):
    r = dg.designer(_branches(tmp_path, None, None, non_calculable=motif), SHA_ETAL, VARIANTES)
    assert r["issue"] == "non_calculable" and r["these"] is None and r["tours"] is None and r["variante_consigne"] is None
    assert r["phrases"] == [f"Étalonnage non calculable (motif : {motif}) ; aucune thèse éprouvée."]


def test_fonction_pure_sans_parametre_ni_etat(tmp_path):
    assert list(inspect.signature(dg.designer).parameters) == ["chemin_branches", "empreinte_etalonnage", "variantes_consigne"]
    chemin = _branches(tmp_path, _oracle("N", False, "rapport"), _oracle("P", True, tours=12))
    assert dg.designer(chemin, SHA_ETAL, VARIANTES) == dg.designer(chemin, SHA_ETAL, copy.deepcopy(VARIANTES))


def test_artefacts_resultat_non_scelle_autre_etalonnage_variante_absente(tmp_path):
    n, p = _oracle("N", True, tours=12), _oracle("P", True, tours=12)
    nu = tmp_path / "nu.json"
    nu.write_text(json.dumps({"schema": cf.SCHEMA_BRANCHES, "references": {"etalonnage": {"sha256": SHA_ETAL}}, "non_calculable": None,
                              "oracles": {"N": n, "P": p}}), encoding="utf-8")
    with pytest.raises(GardeArret, match="empreinte compagnon"):
        dg.designer(nu, SHA_ETAL, VARIANTES)                         # résultat non scellé : refus
    chemin = _branches(tmp_path, n, p)
    with pytest.raises(GardeArret, match="autre étalonnage"):
        dg.designer(chemin, "f" * 64, VARIANTES)
    for variantes in ({"N": "a" * 64}, {"N": "a" * 64, "P": None}, {"N": "a" * 64, "P": ""}, {"N": "a" * 64, "P": "a" * 64}):
        with pytest.raises(GardeArret, match="variante"):
            dg.designer(chemin, SHA_ETAL, variantes)
    chemin.write_text(chemin.read_text(encoding="utf-8").replace('"remplit": true', '"remplit": false'), encoding="utf-8")
    with pytest.raises(GardeArret, match="scellée"):
        dg.designer(chemin, SHA_ETAL, VARIANTES)                     # résultat retouché après son sceau : refus


def test_ecriture_scellee_une_seule_fois_et_configuration_de_course(tmp_path):
    chemin = _branches(tmp_path, _oracle("N", False, "rapport"), _oracle("P", True, tours=12))
    r = dg.designer(chemin, SHA_ETAL, VARIANTES)
    sha = dg.ecrire(r, tmp_path / "designation.json")
    with pytest.raises(GardeArret, match="second passage refusé"):
        dg.ecrire(r, tmp_path / "designation.json")
    cfg = cf.gabarit("jouet")
    course = dg.configuration_de_course(cfg, tmp_path, "designation.json")
    assert course["oracle_de_la_regle"] == {"valeur": "P", "designation": {"chemin": "designation.json", "sha256": sha}}
    assert cf.exiger_oracle_de_la_regle(course, tmp_path) == "P" and cfg["oracle_de_la_regle"]["valeur"] is None
    with pytest.raises(GardeArret, match="porte déjà"):
        dg.configuration_de_course(course, tmp_path, "designation.json")
    # pas de course sans résultat « part »
    nul = dg.designer(_branches(tmp_path, _oracle("N", False, "rapport"), _oracle("P", False, "tours"), nom="b2.json"), SHA_ETAL, VARIANTES)
    dg.ecrire(nul, tmp_path / "designation-2.json")
    with pytest.raises(GardeArret, match="pas de course"):
        dg.configuration_de_course(cfg, tmp_path, "designation-2.json")
