"""Essais de la pièce 10 — lien avec l'épreuve 11 : table à cinq cas et dose λ."""
import pytest

from controle_ia.devin_v1 import RefusDevin
from controle_ia.devin_v1.admission import ConfigurationCourse, InventaireSimule, jouer_course
from controle_ia.devin_v1.graines import generateur_tache, graine_tache
from controle_ia.devin_v1.lien_epreuve_11 import (BANC_NUL, CONFORME, DOSES_ATTENDUES, EPREUVE_REFUSEE, FERME,
                                                  HARNAIS_FUIT, MONTE, OUVERT, RESTE, SAIN,
                                                  exiger_lecture_acceptee, lire, verifier_attendu_monde_plante)
from controle_ia.devin_v1.monde_plante import Fuite

RACINE = 0x5CED_C834_9E37_79B9_7F4A_7C15_F39C_C060


def test_cas_sains_les_deux_premiers_cas():
    assert exiger_lecture_acceptee(FERME, False, MONTE) == CONFORME
    assert exiger_lecture_acceptee(OUVERT, True, RESTE) == SAIN


@pytest.mark.parametrize("bras,rejette,courbe,attendu", [
    (OUVERT, True, MONTE, BANC_NUL),
    (OUVERT, False, None, EPREUVE_REFUSEE),
    (FERME, True, None, HARNAIS_FUIT),
])
def test_artefacts_les_trois_autres_cas_refuses(bras, rejette, courbe, attendu):
    assert lire(bras, rejette, courbe) == attendu
    with pytest.raises(RefusDevin, match="épreuve 11"):
        exiger_lecture_acceptee(bras, rejette, courbe)


def test_aucun_repli_hors_table():
    with pytest.raises(RefusDevin, match="hors de la table"):
        lire(FERME, False, RESTE)
    with pytest.raises(RefusDevin):
        lire(FERME, False, None)
    with pytest.raises(RefusDevin):
        lire("entrouvert", True, MONTE)
    with pytest.raises(RefusDevin, match="non croissante"):
        verifier_attendu_monde_plante((0, 0.1), (2.0, 1.0))
    with pytest.raises(RefusDevin, match="non décroissant"):
        verifier_attendu_monde_plante((0, 0.1), (1.0, 2.0), retablissement=(0.5, 0.6))


def source_essai(nom):
    """Racines d'essai déterministes, dérivées par nom (essai reproductible)."""
    v = int.from_bytes(graine_tache(RACINE, nom).generate_state(4, dtype="uint32").tobytes(), "big")
    return v | (1 << 127)


def test_attendu_sur_monde_plante_statistique_croissante_en_lambda():
    """Doses 0 ; 0,3 ; 1 au budget réduit des essais (n = 300). La dose 0,1 n'est pas
    séparée de 0 de façon fiable à ce budget par l'étage 1 (constat consigné au rapport) ;
    les quatre doses de la section 8 se jouent au budget de la spécification dans
    `scripts/devin_v1_simulations_longues.py` (tâche « dose »)."""
    assert DOSES_ATTENDUES == (0.0, 0.1, 0.3, 1.0)
    doses = (0.0, 0.3, 1.0)
    temoins = tuple(generateur_tache(RACINE, "temoins").normal(size=500))
    c = ConfigurationCourse(devin="lecture", temoin_fuite=Fuite("horodatage", 1.5, "temoin"),
                            n_apprentissage=300, n_epreuve=300, B=199, etages=("0", "1"),
                            lectures_temoins=temoins,
                            options_predicteurs={"etage1": {"bits_mots": 11, "bits_car": 10}})
    stats = []
    for lam in doses:
        v = jouer_course(c, [Fuite("canal_lecture", lam, "lecture")], InventaireSimule(), RACINE,
                         source_racines=source_essai)
        assert v["origine_racines"].startswith("racines d'essai")
        stats.append(v["M"])
    r = verifier_attendu_monde_plante(doses, stats)
    assert r["retablissement"].startswith("non fourni")
