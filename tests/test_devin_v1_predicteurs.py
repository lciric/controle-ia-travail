"""Essais de la pièce 5 — prédicteurs : étages 0, 1 et 2 bis, gel et empreinte."""
import numpy as np
import pytest

from controle_ia.devin_v1 import RefusDevin
from controle_ia.devin_v1.graines import graine_tache, generateur_tache
from controle_ia.devin_v1.monde_plante import Fuite, HarnaisSimule
from controle_ia.devin_v1.predicteurs import (CoffreSecrets, Famille, PredicteurTrait, famille_sans_depense,
                                              traits_admis, traits_sans_preuve)
from controle_ia.devin_v1.vue import Extracteur, champs_elargis_sans_preuve, liste_blanche_monde

RACINE = 0xBF58_476D_1CE4_E5B9_94D0_49BB_1331_11EB
LB = liste_blanche_monde(("horloge", "charge"))
EXT = Extracteur(LB)
OPTIONS = {"etage1": {"bits_mots": 12, "bits_car": 11}, "etage2bis": {"bits_mots": 8, "max_iter": 30}}


def donnees(n, fuites, nom):
    ids = [f"{nom}{k}" for k in range(n)]
    A = np.array([int(generateur_tache(RACINE, i, 99).random() < 0.5) for i in ids])
    h = HarnaisSimule(RACINE, fuites)
    unites = [[EXT.extraire(h.episode(i, {"piece": int(a)})).champs] for i, a in zip(ids, A)]
    return ids, unites, A


def test_traits_seulement_parmi_les_champs_admis():
    assert "latence_derniere" in traits_admis(LB)
    sans = liste_blanche_monde(())
    assert not {"duree_episode", "latence_max", "latence_derniere", "charge"} & set(traits_admis(sans))
    assert "latence_derniere" in traits_sans_preuve(sans, champs_elargis_sans_preuve(sans))
    assert "delai_suivant" not in traits_admis(LB)  # champ absent du monde planté


def test_cas_sain_empreinte_scellee_avant_ouverture_et_fuite_lue():
    ids_a, ua, ya = donnees(300, [Fuite("verdict", 0.5)], "a")
    ids_e, ue, ye = donnees(200, [Fuite("verdict", 0.5)], "e")
    fam = Famille(famille_sans_depense(LB, options=OPTIONS), ids_a, ids_e)
    assert fam.J == len(traits_admis(LB)) + 3
    fam.ajuster(ua, ya, ids_a, graine_tache(RACINE, "pred"))
    coffre = CoffreSecrets(ye)
    with pytest.raises(RefusDevin, match="avant le scellement"):
        coffre.ouvrir(fam)
    e = fam.sceller()
    assert len(e) == 64 and len(fam.liste_numerotee()) == fam.J
    assert np.array_equal(coffre.ouvrir(fam), ye) and coffre.empreinte_famille_a_l_ouverture == e
    s = fam.sorties(ue)
    assert s.shape == (fam.J, 200)
    # Le trait « marqueurs » orienté positivement sépare les bras.
    j = [p.nom for p in fam.predicteurs].index("trait:marqueurs")
    assert s[j][ye == 1].mean() > s[j][ye == 0].mean()


def test_artefact_ajustement_sur_le_pli_d_epreuve_refuse():
    ids_a, ua, ya = donnees(80, [], "a")
    ids_e, ue, ye = donnees(80, [], "e")
    fam = Famille(famille_sans_depense(LB, etages=("0",)), ids_a, ids_e)
    with pytest.raises(RefusDevin, match="pli d'épreuve"):
        fam.ajuster(ue, ye, ids_e, graine_tache(RACINE, "p"))
    with pytest.raises(RefusDevin, match="pli d'épreuve"):
        fam.ajuster(ua[:40] + ue[:40], np.r_[ya[:40], ye[:40]], ids_a[:40] + ids_e[:40], graine_tache(RACINE, "p"))
    fam.ajuster(ua, ya, ids_a, graine_tache(RACINE, "p"))
    fam.sceller()
    with pytest.raises(RefusDevin, match="après scellement"):
        fam.ajuster(ua, ya, ids_a, graine_tache(RACINE, "p"))


def test_artefact_predicteur_modifie_apres_scellement():
    ids_a, ua, ya = donnees(80, [], "a")
    fam = Famille(famille_sans_depense(LB, etages=("0",)), ids_a, ["x"])
    with pytest.raises(RefusDevin, match="non scellée"):
        fam.sorties(ua)
    fam.ajuster(ua, ya, ids_a, graine_tache(RACINE, "p"))
    fam.sceller()
    fam.predicteurs[0].orientation *= -1
    with pytest.raises(RefusDevin, match="modifié"):
        fam.sorties(ua)


def test_orientation_signe_positif_a_correlation_nulle():
    unites = [[{"rang": 3}] for _ in range(10)]
    p = PredicteurTrait("rang", ("rang",), 0)
    p.ajuster(unites, np.r_[np.zeros(5), np.ones(5)], None, graine_tache(RACINE, "o"))
    assert p.orientation == 1.0


def test_aucun_repli():
    with pytest.raises(RefusDevin, match="non disjoints"):
        Famille(famille_sans_depense(LB, etages=("0",)), ["a"], ["a"])
    with pytest.raises(RefusDevin, match="sur devis"):
        famille_sans_depense(LB, etages=("0", "3"))
    with pytest.raises(RefusDevin):
        Famille([], ["a"], ["b"])
