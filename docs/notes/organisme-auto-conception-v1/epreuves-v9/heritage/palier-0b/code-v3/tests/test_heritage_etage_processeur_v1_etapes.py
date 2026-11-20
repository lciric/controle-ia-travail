"""Essais de l'enchaînement (ordre des opérations) : le plan des cases de B8 (72 cases pour C1 et pour C4 ; une cible non
atteignable est écrite et ne se tire pas) ; l'étape 4 réduite à une source sous la couche « essai », sans l'organisme (garde 17
alors non jouée, dit) ; la règle des cases à confirmer sur des comptes plantés."""

import pytest

from aides_heritage_etage_processeur_v1 import graines
from controle_ia.heritage_etage_processeur_v1 import etapes as EP
from controle_ia.heritage_etage_processeur_v1.constantes import CASES_C1, CASES_C4, DOSES_NON_NULLES, TAILLES


def _reglages(non_atteignable=()):
    r = {"K": {(d, t): 32.0 * t for d in DOSES_NON_NULLES for t in TAILLES},
         "tau": {(d, t): 0.9 * t for d in DOSES_NON_NULLES for t in TAILLES},
         "phi": {0.5: 0.4, 1.0: 0.9, 1.5: 1.5}, "gamma": {0.25: 0.1, 0.5: 0.2, 1.0: 0.5, 1.5: 0.9}}
    for reglage, cle in non_atteignable:
        r[reglage][cle] = None
    return r


def test_plan_des_cases_et_nombre_de_cases_de_c1_et_de_c4():
    cases, non = EP.plan_des_cases(_reglages())
    assert non == []
    c1, c4 = EP.cases_de_niveau(cases)
    assert len(c1) == CASES_C1 == 72 and len(c4) == CASES_C4 == 72
    familles = {c["famille"] for c in cases}
    assert familles == {"A", "B", "C", "D", "E", "F", "G", "H", "point-6"}
    assert sum(1 for c in cases if c["famille"] == "E") == 18  # 3 doses × 2 règles × 3 repères
    assert all(c["bras"] == ("2", "3") for c in cases if c["dose"] == 0.0 and c["famille"] == "C")
    assert all("tirages" in c or "sources" in c for c in cases)
    b = [c for c in cases if c["famille"] == "B" and c["proposeur"] == "lecteur-heritage"]
    assert len(b) == 2 * (len(TAILLES) + 2)  # quatre tailles au taux 0,25, et 0 et 0,5 à la taille 1, aux deux doses


def test_cible_non_atteignable_ecrite_et_non_tiree():
    cases, non = EP.plan_des_cases(_reglages([("K", (0.25, 1.5)), ("phi", 1.0)]))
    assert {(x["famille"], x["proposeur"], x.get("taille"), x.get("force")) for x in non} >= {
        ("B", "lecteur-heritage", 1.5, None), ("C", "suiveur", None, 1.0)}
    assert all(x["statut"] == "non atteignable" for x in non)
    assert not any(c["proposeur"] == "suiveur-lettre" for c in cases)  # φ de la force de référence non atteignable
    assert not any(c["famille"] == "B" and c["dose"] == 0.25 and c.get("taille") == 1.5 and c["proposeur"] == "lecteur-heritage"
                   for c in cases)


def test_etape_4_reduite_sans_organisme(tmp_path):
    f, comptes, g17 = EP.etape_4(graines(), "essai", str(tmp_path), doses=(0.5,), proposeurs=("lecteur-heritage", "copieur"),
                                 sources=1, sous_ensemble=0)
    assert g17 is None  # garde 17 non jouée : C6 « non établi » pour elle, issue suspendue
    assert all(f[k] is not None for k in ("p_tient_vraie_source", "p_tient_vraie_cible", "p_tient_fausse",
                                          "p_tient_non_plantee_base", "p_tient_non_plantee_composition", "p_tient_non_plantee_copie"))


def test_etape_6_reduite_reglages_geles_et_plan(tmp_path):
    """L'étape 6 réduite (2 000 sources, couche « essai » : un essai du code, non un étalonnage) : réglages gelés avec leur
    compagnon, aucune lecture (garde 22), et le plan des cases construit sur eux."""
    from aides_heritage_etage_processeur_v1 import FREQUENCES_D_ESSAI
    from controle_ia.heritage_etage_processeur_v1 import etalonnage as ET
    chemin = str(tmp_path / "reglages-essai.json")
    lignes, reglages, sha = EP.etape_6(graines(), "essai", FREQUENCES_D_ESSAI, 2000, chemin, {"essai": True})
    assert ET.verifier_sortie(lignes) and sha and open(chemin + ".sha256").read().split()[0] == sha
    assert len([l for l in lignes if "nom_du_reglage" in l]) == len(EP.cibles_d_etalonnage())
    assert all(l["statut"] in ("atteint", "non atteignable") for l in lignes if "nom_du_reglage" in l)
    cases, non = EP.plan_des_cases(reglages)
    assert cases and all(x["statut"] == "non atteignable" for x in non)


def test_cases_a_confirmer_sur_des_comptes_plantes():
    c = EP.cases_a_confirmer({(10, 0.25, 0.25): 500, (12, 0.25, 0.25): 501}, {(5, "sourd-paie", 0.0): 600})
    assert c == sorted([("C1", 12, 0.25, 0.25), ("C4", 5, "sourd-paie", 0.0)], key=str)
