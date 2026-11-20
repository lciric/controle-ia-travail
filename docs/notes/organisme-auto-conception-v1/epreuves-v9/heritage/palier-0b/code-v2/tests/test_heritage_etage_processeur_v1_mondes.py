"""Essais du générateur des mondes (B1) et de son audit : garde 25 (cas sains : générateur accepté, bornes gelées sans arrêt ;
artefacts : deux lois plantées trop proches, dose inscrite dans la présentation, poids des dépendantes doublés, bornes ramenées à
un tirage par loi et un essai par monde) ; marge face à la source étrangère (B7 bis) ; forme unique ; dose et paires. Audit à
taille réduite seulement (quatre suites par dose ; l'audit à pleine taille est l'étape 3), graines « essai »."""

import itertools

import numpy as np
import pytest

from aides_heritage_etage_processeur_v1 import graines
from controle_ia.heritage_etage_processeur_v1 import audit as AU
from controle_ia.heritage_etage_processeur_v1 import lois as L
from controle_ia.heritage_etage_processeur_v1 import mondes as MO
from controle_ia.heritage_etage_processeur_v1.constantes import DOSES

SUITES_PAR_DOSE = 4


def _suites(g, famille, **kw):
    return [MO.generer_suite(g, dict(couche="essai", famille=famille, dose=d, source=k), d, **kw)
            for d in DOSES for k in range(SUITES_PAR_DOSE)]


@pytest.fixture(scope="module")
def saines():
    return _suites(graines(), "audit-sain")


def test_garde_25_generateur_sain_accepte_et_forme_unique(saines):
    for s in saines:
        assert sum(1 for l in s.source.lois.values() if l["type"] == "vraie") == 8
        assert AU.audit_compositions_de_la_source(s.source.vraies_par_rang(), s.source.oracle.Z, s.source.oracle.G) == []
        d = MO.nombre_de_dependantes(s.source.dose)
        for m in [s.source] + s.mondes_cibles():
            assert AU.audit_marges({i: l["loi"] for i, l in m.lois.items()}, m.oracle.Z, m.oracle.G,
                                   s.source.vraies_par_rang() if m.role != "source" else ()) == []
            for l in m.lois.values():
                assert l["loi"]["type"] == "par_sous_population" and sorted(l["loi"]["lois"]) == ["0", "1"]
                assert all(x["type"] == "softmax" for x in l["loi"]["lois"].values())
            if m.role != "source":
                assert len(m.vraies()) == len(m.fausses()) == 12
                assert sum(1 for l in m.lois.values() if l["dependante"]) == d
                assert sum(1 for dd in m.domaines if dd["vraie"] is None) == 4
        paires = [p for w in s.paires for p in w]
        assert len(paires) == len(set(paires)) == 4 * d  # sans remise, sur les quatre mondes cibles
        assert AU.ensemble_exclu_par_construction([l["texte"] for l in s.finale.lois.values()],
                                                  [l["texte"] for l in s.source.lois.values()]) == []
    # loi dépendante : la loi vraie de plus petit rang sur la première sous-population, l'autre sur la seconde
    s = saines[-1]
    rang = s.source.vraies_par_rang()
    for l in s.finale.lois.values():
        if l["dependante"]:
            p, q = l["paire"]
            assert p < q and l["loi"]["lois"]["0"] == rang[p]["lois"]["0"] and l["loi"]["lois"]["1"] == rang[q]["lois"]["1"]
    c = MO.Compteurs()
    for s in saines:
        c.ajouter(s.compteurs)
    assert all(v[0] >= v[1] > 0 for v in c.vers_dict()["tirages_tentes_acceptes"].values())


def _mondes_sains_par_construction(mondes_par_dose, graine=250):
    """Un générateur sain pour la présentation, par construction : toutes les lois sont tirées de la même loi, quelle que soit
    leur sorte (vraie ou fausse, dépendante ou non, dose). Il éprouve le cas sain de l'audit de présentation, à une taille où le
    bruit de la validation croisée reste loin de 0,55."""
    rng = np.random.default_rng(graine)
    Z, G = L.instances_oracle(graine, 4000)
    out = []
    for dose in DOSES:
        d = MO.nombre_de_dependantes(dose)
        for _ in range(mondes_par_dose):
            lois = []
            for k in range(24):
                loi = L.loi_par_sous_population(L.softmax_aleatoire(rng), L.softmax_aleatoire(rng))
                lois.append((L.json_canonique(loi), loi, "vraie" if k < 12 else "fausse", k < d))
            out.append({"dose": dose, "Z": Z, "G": G, "lois": lois})
    return out


def test_garde_25_audit_de_presentation_cas_sain():
    pres = AU.audit_presentation(_mondes_sains_par_construction(300), np.random.default_rng(25))
    assert pres["arret"] == [] and pres["signalement"] == [] and pres["mention"] is None, pres["exactitudes"]
    assert pres["non_calculees"] == []
    assert len([v for j in pres["exactitudes"].values() for v in j.values()]) == 15


def test_audit_de_presentation_du_generateur_de_b1_a_taille_reduite(saines):
    """Constat, sans seuil à cette taille (quatre suites par dose ; l'audit à pleine taille est l'étape 3) : les quinze
    exactitudes se calculent sur les mondes du générateur constructif, et la distribution des traits de contenu par sorte de loi
    est rapportée."""
    pres = AU.audit_presentation(MO.mondes_pour_l_audit(saines), np.random.default_rng(25))
    assert pres["non_calculees"] == []
    assert len([v for j in pres["exactitudes"].values() for v in j.values()]) == 15
    dist = MO.distribution_des_traits_de_contenu(saines)
    assert set(dist) == {"vraie-source", "fausse-source", "dependante", "independante", "fausse-cible"}


def test_garde_25_deux_lois_trop_proches_le_monde_est_rejete(saines):
    m = saines[0].cibles[0]
    lois = {i: l["loi"] for i, l in m.lois.items()}
    a, b = sorted(lois)[:2]
    # une loi proche mais distincte : la première ligne de poids de chaque sous-loi déplacée de 0,05 (déplacer toutes les
    # lignes du même vecteur laisserait la loi identique, une softmax étant invariante par un tel déplacement)
    proche = {"type": "par_sous_population", "lois": {
        g: {"type": "softmax", "poids": [[w + (0.05 if i == 0 else 0.0) for w in ligne] for i, ligne in enumerate(s["poids"])],
            "biais": s["biais"]} for g, s in lois[a]["lois"].items()}}
    lois[b] = proche
    manques = AU.audit_marges(lois, m.oracle.Z, m.oracle.G)
    assert any(x[1:3] == (a, b) and 0.0 < x[3] < 0.25 for x in manques)


def test_garde_25_dose_inscrite_dans_la_presentation_arret():
    g = graines()
    suites = _suites(g, "audit-dose-inscrite", variante="dose-inscrite")
    pres = AU.audit_presentation(MO.mondes_pour_l_audit(suites), np.random.default_rng(26))
    assert any(a.startswith("forme/mondes_dose") for a in pres["arret"])
    assert max(v for k, v in pres["exactitudes"]["forme"].items() if k.startswith("mondes_dose")) > 0.55


def test_garde_25_poids_des_dependantes_doubles_signale():
    g = graines()
    suites = [MO.generer_suite(g, dict(couche="essai", famille="audit-poids", dose=d, source=k), d,
                               faute="poids-dependantes-doubles") for d in (0.25, 0.5) for k in range(SUITES_PAR_DOSE)]
    pres = AU.audit_presentation(MO.mondes_pour_l_audit(suites), np.random.default_rng(27))
    assert pres["exactitudes"]["contenu"]["dependantes_contre_independantes"] > 0.55
    assert "contenu/dependantes_contre_independantes" in pres["signalement"]
    assert pres["mention"] == "générateur non audité pour l'étage payant"


def test_garde_25_bornes_de_la_construction_epuisees():
    g = graines()
    for k in range(2):  # bornes gelées, générateur sain : aucun arrêt
        MO.generer_suite(g, dict(couche="essai", famille="bornes-saines", source=k), 0.5)
    with pytest.raises(MO.ArretGenerateur, match="bornes de la construction épuisées"):
        MO.generer_suite(g, dict(couche="essai", famille="bornes-courtes", source=0), 0.5, bornes=MO.Bornes(1, 1, 1))


def test_marge_face_a_la_source_etrangere():
    """À la dose 0,25 (douze paires sur vingt-huit). À la dose 0,5, vingt-quatre paires sur vingt-huit sont des lois dépendantes
    et la construction, sur les graines « essai » de l'outil de diagnostic, épuise ses bornes : constat porté au rapport."""
    g = graines()
    bases = [dict(couche="essai", famille="etrangere", dose=0.25, source=k) for k in range(3)]
    suites = MO.generer_jeu_avec_etrangeres(g, bases, 0.25)
    for k, s in enumerate(suites):
        e = suites[(k + 1) % 3].source
        assert s.etrangere is e
        for m in s.mondes_cibles():
            assert AU.audit_marges({i: l["loi"] for i, l in m.lois.items()}, m.oracle.Z, m.oracle.G,
                                   s.source.vraies_par_rang(), e.vraies_par_rang()) == []
    # sans la construction de B7 bis, la marge face à une source étrangère n'est pas garantie : l'audit la lit
    s0 = MO.generer_suite(g, dict(couche="essai", famille="sans-etrangere", source=0), 0.5)
    lois = {i: l["loi"] for i, l in s0.cibles[0].lois.items()}
    etrangere_fautive = [lois[sorted(lois)[0]]] + suites[0].source.vraies_par_rang()[1:]
    assert AU.audit_marges(lois, s0.cibles[0].oracle.Z, s0.cibles[0].oracle.G, (), etrangere_fautive)


def test_dose_hors_grille_refusee():
    with pytest.raises(MO.ArretGenerateur):
        MO.nombre_de_dependantes(0.3)
    assert [MO.nombre_de_dependantes(d) for d in DOSES] == [0, 3, 6]
    assert len(MO.PAIRES_DE_LA_SOURCE) == 28 == len(list(itertools.combinations(range(8), 2)))
