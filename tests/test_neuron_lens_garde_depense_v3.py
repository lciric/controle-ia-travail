"""Essais (R5, v3) de la garde de dépense : cas sain (sous 60 %, rien), compte rendu unique à 60 %, arrêt dur à 90 % par identifiant,
prix lu illisible (le prix déclaré sert), prix lu plus haut (il sert), instance absente, dépense simulée non finie (arrêt), minuterie."""
import math

import pytest

from controle_ia.neuron_lens import garde_depense_v3 as gd


class Horloge:
    def __init__(self, t=0.0):
        self.t = t

    def __call__(self):
        return self.t

    def dormir(self, s):
        self.t += s


def _surv(prix_lu, plafond=10.0, prix=0.9, tours_max=None, periode=600.0, destruction_effective=True):
    h, det, rap = Horloge(), [], []
    lire = (lambda i: None if (det and destruction_effective) else prix_lu(i))
    r = gd.surveiller(42, prix, plafond, 0.0, lire_prix=lire, detruire=det.append, rapporter=rap.append, horloge=h,
                      dormir=h.dormir, periode=periode, tours_max=tours_max)
    return r, det, rap, h


def test_etat():
    assert gd.etat(5.9, 10) == "ok" and gd.etat(6.0, 10) == "compte_rendu" and gd.etat(9.0, 10) == "arret"
    assert gd.etat(float("nan"), 10) == "arret" and gd.etat(1.0, 0) == "arret"


def test_cas_sain_sous_60():
    r, det, rap, _ = _surv(lambda i: 0.9, tours_max=3)  # 3 tours de 10 min à 0,90 USD/h : 0,45 USD
    assert r["etat"] == "ok" and det == [] and rap == []


def test_compte_rendu_unique_puis_arret_par_identifiant():
    r, det, rap, h = _surv(lambda i: 0.9)
    assert det == [42] and r["etat"] == "arret" and r["depense"] >= 9.0
    assert [x["etat"] for x in rap] == ["compte_rendu", "arret"]
    assert r["depense"] < 9.0 + 0.9 * 600 / 3600 + 1e-9  # au plus un tour de retard


def test_prix_lu_illisible_ou_plus_haut():
    r, det, rap, h = _surv(lambda i: float("nan"))
    assert det == [42] and abs(h.t / 3600 * 0.9 - r["depense"]) < 1e-9
    r2, det2, _, h2 = _surv(lambda i: 1.8)
    assert det2 == [42] and h2.t < h.t + 1e-9  # le prix lu, plus haut, sert : arrêt plus tôt


def test_instance_absente():
    r, det, rap, _ = _surv(lambda i: None)
    assert r["etat"] == "instance_absente" and det == []


def test_artefact_depense_simulee_non_finie():
    r, det, rap, _ = _surv(lambda i: 0.9, prix=float("inf"))
    assert det == [42] and r["etat"] == "arret"


def test_minuterie():
    assert gd.minuterie_s(0.9, 10.0) == 36000
    assert gd.minuterie_s(0.5, 10.0, frais_fixes=1.0) == int(8.0 / 0.5 * 3600)
    with pytest.raises(ValueError):
        gd.minuterie_s(0.0, 10.0)
    assert math.isclose(gd.depense(0.9, 0, 36000), 9.0)


def test_destruction_qui_echoue_est_retentee_puis_rendue():
    r, det, rap, _ = _surv(lambda i: 0.9, destruction_effective=False)
    assert det == [42] * 5 and r["etat"] == "arret_echec_destruction" and rap[-1]["etat"] == "arret_echec_destruction"
    essais = []

    def detruire(i):
        essais.append(i)
        if len(essais) < 3:
            raise RuntimeError("réseau")
    assert gd.detruire_verifie(7, detruire, lambda i: None if len(essais) >= 3 else 0.9, dormir=lambda s: None)
    assert essais == [7, 7, 7]


def test_minuterie_restante():
    assert gd.minuterie_restante_s(0.9, 10.0, 0.0, 600.0) == 36000 - 600
    assert gd.minuterie_restante_s(0.9, 10.0, 0.0, 10 ** 6) == 0


def test_lecture_du_prix_qui_leve():
    """Contre-lecture 4, remarque 5 : une exception de la lecture (délai dépassé) ne tue pas la garde ; le prix déclaré sert."""
    appels = []

    def lire(i):
        appels.append(i)
        if len(appels) <= 2:
            raise TimeoutError("délai")
        return 0.9
    r, det, rap, h = _surv(lire, tours_max=4)
    assert r["etat"] == "ok" and det == [] and len(appels) == 4
