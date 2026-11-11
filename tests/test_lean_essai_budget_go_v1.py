"""Essais R5 de A7, A8 (compteur et étalonnage) et de A12 (refus d'appel sans GO de D-1b) — essai Lean, D-1a."""
from datetime import date

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.lean_essai import budget_v1 as B
from controle_ia.lean_essai import garde_go_v1 as GO

ENTETE = "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"
L_D1A = ("| GO-2026-11-10-13 | 2026-11-10 | calcul | **Essai Lean (couche 4, pas (b)), D-1a : outillage seul** ; **aucun appel "
         "de modèle** ; tout appel de modèle (D-1b, pilote) exige une ligne de GO à part | 65 USD | 2026-11-30 | Lazar | R-2265 |\n")
L_D1B = ("| GO-2026-11-20-01 | 2026-11-20 | calcul | Essai Lean, D-1b : pilote, appels d'interface chez quatre fournisseurs "
         "| 578 USD | 2026-12-10 | Lazar | R-9999 |\n")
L_AUTRE = ("| GO-2026-11-10-11 | 2026-11-10 | calcul | Course réelle de l'organisme d'idéation | 45 USD | 2026-11-30 | Lazar "
           "| R-2265 |\n")
JOUR = date(2026, 11, 21)


def registre(tmp_path, *lignes):
    p = tmp_path / "go.md"
    p.write_text(ENTETE + "".join(lignes), encoding="utf-8")
    return p


# ---- coût d'un appel ---------------------------------------------------------------------------------------------------------

def test_cout_appel_retrouve_le_devis():
    # agent du bras S (Opus 5.5, 100 k en entrée dont 80 % lus et 10 % écrits en cache, 10 k en sortie) : 0,322 au devis v4
    assert B.cout_appel(4, 20, 100_000, 10_000, 80_000, 10_000) == pytest.approx(0.322)
    assert B.RESERVE_A7 == 32 and B.RESERVE_A7_SERIE == 12
    with pytest.raises(GardeArret):
        B.cout_appel(4, 20, 10, 10, 8, 8)


def test_plafond_par_item():
    assert B.peut_appeler_item(3.0, 0.9)
    assert not B.peut_appeler_item(3.5, 0.6)


# ---- A7 -----------------------------------------------------------------------------------------------------------------------

def test_a7_sain_puis_coupure():
    c = B.CompteurPhase(plafond=578.0)
    c.lancer("L1", 4.0)
    c.lancer("S1", 4.0)
    c.terminer("L1", 1.2)
    c.terminer("S1", 0.4)
    assert c.depense == pytest.approx(1.6) and not c.coupure()
    c.depense = 578.0 - 32.0 + 0.01
    assert c.coupure()
    c.depense = 570.0
    for i in range(2):
        c.lancer(f"x{i}", 4.0)
    with pytest.raises(GardeArret, match="plus aucun lancement"):
        c.lancer("x2", 4.0)


def test_a7_artefacts_compteur_faux():
    c = B.CompteurPhase(plafond=100.0)
    c.lancer("L1", 4.0)
    with pytest.raises(GardeArret, match="compteur faux"):
        c.terminer("L1", 4.5)
    with pytest.raises(GardeArret):
        c.terminer("inconnu", 1.0)
    c.lancer("L2", 4.0)
    with pytest.raises(GardeArret):
        c.lancer("L2", 4.0)


# ---- A8 (chiffres du devis v5, bloc 1) ---------------------------------------------------------------------------------------

@pytest.mark.parametrize("plafond,fixe,par_graine,graines,arret", [
    (578, 110.74, 3.778, 60, False),   # profil supposé : 115 payables, pilote complet de 60
    (578, 149.14, 7.618, 50, False),   # profil pire réaliste : 52 payables, 10 blocs
    (578, 167.50, 9.454, 40, False),   # chaque item formel à 4 USD : 40 (8 blocs)
    (550, 167.50, 9.454, 35, True),    # à 550 : 37 payables, 35 au bloc : arrêt
])
def test_a8_retrouve_le_devis(plafond, fixe, par_graine, graines, arret):
    # après les 20 items de contrôle et deux blocs (10 graines) : 60 % des charges fixes payées, 40 % restant
    d = B.decision_a8(plafond, depense=0.6 * fixe + 10 * par_graine, charges_restantes=0.4 * fixe, cout_graine=par_graine)
    assert d["graines"] == graines and d["arret"] is arret


def test_a8_artefacts():
    with pytest.raises(GardeArret):
        B.graines_a8(578, 10, 10, 0.0)
    with pytest.raises(GardeArret):
        B.graines_a8(578, -1, 10, 3.0)
    assert B.lecture_si_coupure_a7(38).startswith("descriptive")
    assert B.lecture_si_coupure_a7(45) == "ordinaire"


# ---- A12 ----------------------------------------------------------------------------------------------------------------------

def test_a12_sain_go_du_pilote(tmp_path):
    p = registre(tmp_path, L_D1A, L_D1B)
    assert GO.autoriser_appels_modele("GO-2026-11-20-01", p, JOUR)["plafond"] == "578 USD"


@pytest.mark.parametrize("go_id,motif", [
    ("GO-2026-11-10-13", "exclut tout appel de modèle"),    # GO de l'outillage
    ("GO-2026-11-10-11", "pas un GO du pilote D-1b"),       # GO d'une autre course
    ("GO-2026-12-01-01", "absent"),
    ("pas-un-go", "mal formé"),
])
def test_a12_artefacts(tmp_path, go_id, motif):
    p = registre(tmp_path, L_D1A, L_AUTRE, L_D1B)
    with pytest.raises(GardeArret, match=motif):
        GO.autoriser_appels_modele(go_id, p, JOUR)


def test_a12_artefacts_validite_auteur_revocation_registre(tmp_path):
    with pytest.raises(GardeArret, match="période"):
        GO.autoriser_appels_modele("GO-2026-11-20-01", registre(tmp_path, L_D1B), date(2026, 12, 11))
    with pytest.raises(GardeArret, match="Lazar"):
        GO.autoriser_appels_modele("GO-2026-11-20-01", registre(tmp_path, L_D1B.replace("| Lazar |", "| mère |")), JOUR)
    rev = "| GO-2026-11-21-01 | 2026-11-21 | révocation | révoque GO-2026-11-20-01 | — | — | Lazar | R-1 |\n"
    with pytest.raises(GardeArret, match="révoqué"):
        GO.autoriser_appels_modele("GO-2026-11-20-01", registre(tmp_path, L_D1B, rev), JOUR)
    with pytest.raises(GardeArret, match="mal formé"):
        GO.autoriser_appels_modele("GO-2026-11-20-01", registre(tmp_path, L_D1B.replace("| 578 USD ", "")), JOUR)
    with pytest.raises(GardeArret, match="double"):
        GO.autoriser_appels_modele("GO-2026-11-20-01", registre(tmp_path, L_D1B, L_D1B), JOUR)
    with pytest.raises(GardeArret, match="absent"):
        GO.autoriser_appels_modele("GO-2026-11-20-01", tmp_path / "nulle-part.md", JOUR)


def test_a12_porte_des_appels(tmp_path):
    c = B.CompteurPhase(plafond=578.0)
    porte = GO.AppelsModeleGardes("GO-2026-11-10-13", registre(tmp_path, L_D1A), c, aujourdhui=lambda: JOUR)
    with pytest.raises(GardeArret, match="exclut"):
        porte.appeler("L1", 4.0, {})
    assert c.en_vol == {} and c.depense == 0.0
    porte = GO.AppelsModeleGardes("GO-2026-11-20-01", registre(tmp_path, L_D1B), c, aujourdhui=lambda: JOUR)
    with pytest.raises(GardeArret, match="aucun transport"):
        porte.appeler("L1", 4.0, {})
    assert c.en_vol == {}
    porte.transport = lambda requete: {"cout_usd": 1.25}
    porte.appeler("L1", 4.0, {})
    assert c.depense == pytest.approx(1.25)


def test_go_cite_a_la_creation_de_machine(tmp_path):
    p = registre(tmp_path, L_D1A, L_D1B)
    assert GO.autoriser_creation_machine("GO-2026-11-10-13", p, date(2026, 11, 11))["type"] == "calcul"
    with pytest.raises(GardeArret, match="attendu"):
        GO.autoriser_creation_machine("GO-2026-11-20-01", p, JOUR)
    with pytest.raises(GardeArret, match="période"):
        GO.autoriser_creation_machine("GO-2026-11-10-13", p, date(2026, 12, 1))
