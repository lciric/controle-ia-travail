"""Artefacts plantés contre l'épreuve du centrage, v5 (texte scellé, section 13, `tests/test_iib_artefacts_centrage_v5.py`).

Jouet numérique à deux régimes (premier pas dispersé, pas suivants ancrés). Défauts plantés : décalage d'instrument de 0,05
décade ; biais de réécriture de 0,10 par pas (oracle à contexte réécrit) ; forme illisible d'un seul côté sur 10 % des suites.
La composante attendue arrête au moins 18 fois sur 20 graines, pour chaque oracle concerné ; le cas sain passe (R5)."""
import numpy as np
import pytest

from controle_ia.iib import epreuve_centrage_v5 as ec
from controle_ia.iib.jouet_v5 import etalonnage_numerique

GRAINES = [5100 + i for i in range(20)]


def _epreuves(graine, defaut="aucun", ampleur=0.0):
    e = etalonnage_numerique(np.random.default_rng(graine), defaut, ampleur)
    par = {}
    for l in e["lignes"]:
        par.setdefault((l["oracle"], l["phase"]), []).append(l)
    communes = ec.composantes_communes(par[("P", "etalonnage-honnete")])
    p = ec.epreuve_du_centrage("P", par[("P", "etalonnage-honnete")], communes=communes)
    n = ec.epreuve_du_centrage("N", par[("P", "etalonnage-honnete")], par[("N", "etalonnage-honnete")], par[("N", "etalonnage-regenere")],
                               communes=communes)
    return p, n


@pytest.mark.parametrize("defaut, ampleur, composante, oracles", [
    ("decalage_instrument", 0.05, "rangs_agent", ("P", "N")),
    ("biais_reecriture", 0.10, "chaine_reecrite", ("N",)),
    ("illisible_un_cote", 0.10, "lisibilite_agent", ("P", "N"))])
def test_la_composante_attendue_arrete_au_moins_18_fois_sur_20(defaut, ampleur, composante, oracles):
    arrets = {o: 0 for o in oracles}
    for g in GRAINES:
        p, n = _epreuves(g, defaut, ampleur)
        for o, r in (("P", p), ("N", n)):
            if o in oracles:
                arrets[o] += int(r["composantes"][composante]["rejette"])
                assert r["passe"] is not r["composantes"][composante]["rejette"] or not r["passe"]
                if r["composantes"][composante]["rejette"]:
                    assert "oracle en défaut (centrage : " in r["message"] or len(r["echecs"]) > 1
    assert all(a >= 18 for a in arrets.values()), (defaut, arrets)


def test_cas_sain_l_epreuve_entiere_passe_presque_toujours():
    arrets = {"P": 0, "N": 0}
    for g in GRAINES:
        p, n = _epreuves(g)
        arrets["P"] += int(not p["passe"])
        arrets["N"] += int(not n["passe"])
    assert arrets["P"] <= 4 and arrets["N"] <= 4, arrets                 # taux attendu d'environ 5 % : plus de 4 sur 20, une fois sur 600


def test_le_biais_de_reecriture_ne_touche_pas_l_oracle_au_contexte_de_l_agent():
    arrets = sum(int(not _epreuves(g, "biais_reecriture", 0.10)[0]["passe"]) for g in GRAINES)
    assert arrets <= 4                                                    # sans objet pour lui : il ne réécrit rien
