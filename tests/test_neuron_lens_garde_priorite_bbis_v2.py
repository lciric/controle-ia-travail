"""Essais de la garde de priorité de l'étape B bis, v2 (R5 : cas sain et artefacts), avec un faux outil du loueur.
v2 = essais v1 adaptés (lentilles absentes) et cinq essais neufs (mineurs 1 à 3 de la vérification v6→v7)."""
import json

import pytest

from controle_ia.neuron_lens import garde_priorite_bbis_v2 as G

LENT, BBIS, BAILEY = 70000001, 61276240, 61170458


class FauxLoueur:
    def __init__(self, credit=48.3, ids=(BAILEY, BBIS, LENT), liste_ok=True, credit_ok=True, destruction_ok=True):
        self.credit, self.ids, self.liste_ok, self.credit_ok, self.destruction_ok = credit, list(ids), liste_ok, credit_ok, destruction_ok
        self.appels = []

    def __call__(self, *args):
        self.appels.append(args)
        if args[:2] == ("show", "instances"):
            if not self.liste_ok:
                return 1, "", "erreur réseau"
            return 0, json.dumps([{"id": i, "actual_status": "running", "dph_total": 1.0} for i in self.ids]), ""
        if args[:2] == ("show", "user"):
            if not self.credit_ok:
                return 0, "", ""
            return 0, json.dumps({"credit": self.credit, "api_key": "NE-PAS-IMPRIMER"}), ""
        if args[:2] == ("show", "instance"):
            i = int(args[2])
            return (0, json.dumps({"id": i, "dph_total": 2.4}), "") if i in self.ids else (0, "{}", "")
        if args[:2] == ("destroy", "instance"):
            if self.destruction_ok and int(args[2]) in self.ids:
                self.ids.remove(int(args[2]))
            return 0, "", ""
        raise AssertionError(args)


def _surv(f, **kw):
    journal = []
    r = G.surveiller(LENT, BBIS, appel=f, rapporter=journal.append, dormir=lambda s: None, **kw)
    return r, journal


def test_cas_sain_continue_sans_detruire():
    f = FauxLoueur(credit=48.3)
    r, j = _surv(f, tours_max=3)
    assert r["etat"] == "continuer" and len(j) == 3 and all(x["credit"] == 48.3 for x in j)
    assert not any(a[0] == "destroy" for a in f.appels)


def test_artefact_credit_sous_seuil_detruit_et_prouve():
    f = FauxLoueur(credit=11.99)
    r, j = _surv(f)
    assert r["etat"] == "detruite" and LENT not in f.ids and BBIS in f.ids
    assert ("destroy", "instance", str(LENT), "-y") in f.appels
    assert not any(a[0] == "destroy" and a[2] != str(LENT) for a in f.appels)  # seule la machine des lentilles
    assert "absente" in r["preuve"]


def test_seuil_exact_ne_detruit_pas():
    r, _ = _surv(FauxLoueur(credit=12.0), tours_max=1)
    assert r["etat"] == "continuer"


def test_credit_illisible_detruit_sens_severe():
    f = FauxLoueur(credit_ok=False)
    r, _ = _surv(f)
    assert r["etat"] == "detruite" and r["credit"] is None
    assert sum(1 for a in f.appels if a[:2] == ("show", "user")) == 3


def test_bbis_finie_arrete_la_garde_sans_detruire():
    f = FauxLoueur(credit=5.0, ids=(BAILEY, LENT))
    r, _ = _surv(f)
    assert r["etat"] == "bbis_finie" and LENT in f.ids


def test_liste_illisible_bbis_supposee_en_marche():
    f = FauxLoueur(credit=10.0, liste_ok=False)
    r = G.tour(LENT, BBIS, appel=f, dormir=lambda s: None)
    assert r["etat"] == "detruire"
    f2 = FauxLoueur(credit=40.0, liste_ok=False)
    assert G.tour(LENT, BBIS, appel=f2, dormir=lambda s: None)["etat"] == "continuer"


def test_lentilles_absentes_confirmees_apres_trois_listes_et_lecture():
    f = FauxLoueur(credit=30.0, ids=(BAILEY, BBIS))
    r, j = _surv(f)
    assert r["etat"] == "lentilles_absentes" and [x["etat"] for x in j] == ["continuer", "continuer", "lentilles_absentes"]
    assert any(a[:2] == ("show", "instance") for a in f.appels)


def test_liste_en_retard_apres_creation_ne_termine_pas_la_garde():
    f = FauxLoueur(credit=30.0, ids=(BAILEY, BBIS))
    j = []

    def dormir(s):
        if LENT not in f.ids:
            f.ids.append(LENT)  # la machine apparaît au tour suivant
    r = G.surveiller(LENT, BBIS, appel=f, rapporter=j.append, dormir=dormir, tours_max=3)
    assert r["etat"] == "continuer" and [x["absences"] for x in j] == [1, 0, 0]


def test_lentilles_absentes_de_la_liste_mais_instance_presente_continue():
    f = FauxLoueur(credit=30.0, ids=(BAILEY, BBIS))
    vraie = f.__call__

    def appel(*a):
        if a[:2] == ("show", "instance"):
            return 0, json.dumps({"id": LENT, "dph_total": 2.4}), ""
        return vraie(*a)
    j = []
    r = G.surveiller(LENT, BBIS, appel=appel, rapporter=j.append, dormir=lambda s: None, tours_max=4)
    assert r["etat"] == "continuer" and len(j) == 4


def test_lentilles_absentes_credit_bas_detruit_quand_meme():
    f = FauxLoueur(credit=3.0, ids=(BAILEY, BBIS))
    r, _ = _surv(f)
    assert r["etat"] == "detruite"


def test_exception_dans_un_tour_detruit_sens_severe():
    f = FauxLoueur(credit=30.0)
    vraie = f.__call__

    def appel(*a):
        if a[:2] == ("show", "user"):
            raise OSError("panne")
        return vraie(*a)
    r = G.surveiller(LENT, BBIS, appel=appel, rapporter=lambda x: None, dormir=lambda s: None)
    assert r["etat"] == "detruite" and LENT not in f.ids


def test_destruction_non_prouvee_rendue():
    f = FauxLoueur(credit=1.0, destruction_ok=False)
    r, _ = _surv(f)
    assert r["etat"] == "destruction_non_prouvee" and LENT in f.ids


def test_periode_au_plus_15_minutes():
    with pytest.raises(ValueError):
        _surv(FauxLoueur(), periode=901, tours_max=1)


def test_credit_seul_lu_jamais_les_autres_champs():
    f = FauxLoueur(credit=30.0)
    _, j = _surv(f, tours_max=1)
    assert "NE-PAS-IMPRIMER" not in json.dumps(j)
