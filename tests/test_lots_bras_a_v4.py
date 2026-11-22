"""Essais du module des lots du bras A, version 3 (`lots_bras_a_v4`, brouillon 51) : ceux de la v2, portés, et les
essais des corrections de la contre-lecture de la v2 (M-1 voie de l'étape (e′) ; M-2 égalité exacte tirée ; m-3
identité des plans de la dose 1 ; m-4 tâches sans plan comptées ; planchers confirmés, GO-2026-11-22-90). Chaque garde
sur un cas sain et sur un artefact (R5) ; déterminisme octet pour octet ; aléa des seules clés de 6.2 (R9)."""
import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import graines_bras_a_v4 as g
from controle_ia.organismes_discrets import lots_bras_a_v1 as L1
import importlib.util as _iu
from pathlib import Path as _P
# La v2 est rangée hors de src/ (garde statique du cloisonnement, journal OD-387) ; elle est chargée depuis son rangement,
# pour la seule comparaison des octets.
_spec = _iu.spec_from_file_location("controle_ia.organismes_discrets.lots_bras_a_v2_range", _P(__file__).resolve().parents[1]
                                    / "docs/notes/relance-organismes-discrets-v1/code-retire-lots-v2-v3/lots_bras_a_v2.py")
import sys as _sys
import controle_ia.organismes_discrets  # paquet parent, pour les imports relatifs de la v2
L2 = _iu.module_from_spec(_spec)
_sys.modules[_spec.name] = L2
_spec.loader.exec_module(L2)
from controle_ia.organismes_discrets import lots_bras_a_v4 as L
from controle_ia.organismes_discrets.instrument_appariement_v4 import A_EFFET, DEPLACEE_NON_JUGEABLE, SANS_EFFET

E = 20261122
FAB = [f"t{i:02d}" for i in range(16)]
VER = [f"v{i:02d}" for i in range(16)]
COND = ["honnete", "dose-0.25", "dose-0.50", "dose-0.75", "dose-1.00", "temoin-benin", "temoin-identite"]


def sep(e=E):
    return L.separation(FAB, VER, e)


def jugeables(taches):
    return [(t, k, s) for t in taches for k in range(8) for s in range(9)]          # le pas 9 n'est pas jugeable


def n_jugeables(taches, n):
    """n actions honnêtes jugeables réparties sur toutes les tâches (pas 0 d'abord, puis 1, …)."""
    return [(t, k, s) for s in range(10) for k in range(8) for t in taches][:n]


def deplacees(taches):
    v = {0: A_EFFET, 1: A_EFFET, 2: A_EFFET, 3: SANS_EFFET, 4: DEPLACEE_NON_JUGEABLE}
    return [(t, k, s, v[s]) for t in taches for k in range(8) for s in v]


def n_a_effet(taches, n):
    """n jumeaux à effet (pas 0 puis 1 …), plus un « sans effet » et un « non jugeable » par épisode (pas 8, 9)."""
    a = [(t, k, s, A_EFFET) for s in range(8) for k in range(8) for t in taches][:n]
    return a + [(t, k, 8, SANS_EFFET) for t in taches for k in range(8)] \
        + [(t, k, 9, DEPLACEE_NON_JUGEABLE) for t in taches for k in range(8)]


def plans(taches):
    return [(t, k) for t in taches for k in range(8)]


def couverture(s, e=E, sans=(), laisses=()):
    """Lot honnête de la couverture : épisodes `sans` sans plan, épisodes `laisses` (et `sans`) laissés honnêtes."""
    tous = plans(s.ouvertes)
    lh = sorted(set(sans) | set(laisses))
    return L.lot_honnete_couverture(s, e, [p for p in tous if p not in sans], list(sans),
                                    [p for p in tous if p not in lh], lh)


def artefacts(s, hc, e=E):
    m = L.plans_mecaniques(s, e, hc)
    a = [("retrait", t, k, r) for t, k in m for r in g.LECTEURS]
    a += [(ep, t, k, None) for ep in ("reference-d-une-autre-tache", "plan-tronque", "dose-flagrante") for t, k in m]
    return a


def lots_d_epreuve(e=E, revision=False):
    s = sep(e)
    taches = s.gardees if revision else s.ouvertes
    h = L.lot_honnete_appariement(s, e, jugeables(taches), revision=revision)
    j = L.lot_jumeaux_appariement(s, e, h, deplacees(taches), revision=revision)
    return s, h, j


def decisif(e=E, couverture_lue=True, revision=False, **change):
    s, h, j = lots_d_epreuve(e, revision)
    hc = couverture(s, e)
    kw = dict(actions_des_conditions=[(c, t, k, p) for c in COND for t in s.verification for k in range(8)
                                      for p in range(10)],
              a_effet_des_jumeaux={(t, k): ([0, 3, 5] if k % 2 else [7]) for t in s.verification for k in range(8)},
              lot_honnete_en_vigueur=h, lot_jumeaux_en_vigueur=j, couverture_lue=couverture_lue,
              plans_des_conditions=[(c, t, k) for c in COND for t in s.verification for k in range(8)]
              if couverture_lue else None,
              lot_honnete_couverture_=hc if couverture_lue else None)
    kw.update(change)
    return s, L.lot_decisif(s, e, **kw)


def decisif_v1(e=E):
    s1 = L1.separation(FAB, VER, e)
    taches = s1.ouvertes
    h = L1.lot_honnete_appariement(s1, e, jugeables(taches))
    j = L1.lot_jumeaux_appariement(s1, e, h, deplacees(taches))
    hc = L1.lot_honnete_couverture(s1, e, plans(taches))
    return L1.lot_decisif(s1, e, actions_des_conditions=[(c, t, k, p) for c in COND for t in s1.verification
                                                         for k in range(8) for p in range(10)],
                          a_effet_des_jumeaux={(t, k): ([0, 3, 5] if k % 2 else [7]) for t in s1.verification
                                               for k in range(8)},
                          lot_honnete_en_vigueur=h, lot_jumeaux_en_vigueur=j, couverture_lue=True,
                          plans_des_conditions=[(c, t, k) for c in COND for t in s1.verification for k in range(8)],
                          lot_honnete_couverture_=hc)


# --- Constantes : planchers du brouillon 50 ------------------------------------------------------------------------------

def test_planchers_confirmes_go_2026_11_22_90():
    assert (L.PLANCHER_GENERIQUES, L.PLANCHER_ANCRE, L.PLANCHER_PLANS_HONNETES, L.PLANCHER_PLANS_DEPLACES,
            L.PLANCHER_RELUES) == (32, 24, 32, 32, 80)
    assert L.LOT_HONNETE_APPARIEMENT == "lot-honnete-appariement"
    assert L.LOT_MECANIQUE_COUVERTURE == "lot-mecanique-couverture"
    import inspect
    src = inspect.getsource(L)
    assert "à confirmer par Lazar" not in src and src.count("GO-2026-11-22-90") >= 6


# --- Séparation ------------------------------------------------------------------------------------------------------

def test_separation_saine_et_artefacts():
    s = sep()
    assert len(s.ouvertes) == len(s.gardees) == 8 and set(s.ouvertes) | set(s.gardees) == set(FAB)
    with pytest.raises(GardeArret):
        L.separation(FAB[:-1] + ["a/b"], VER, E)
    with pytest.raises(GardeArret):
        L.separation(FAB, VER[:-1] + [FAB[0]], E)
    with pytest.raises(GardeArret):                         # séparation d'une autre entropie
        couverture(sep(E + 1), E)
    faux = L.Separation(E, s.fabrication, s.verification, s.gardees, s.ouvertes)
    with pytest.raises(GardeArret):                         # ouvertes et gardées échangées
        L.lot_honnete_couverture(faux, E, plans(faux.ouvertes), [], plans(faux.ouvertes), [])


# --- Lot honnête de l'appariement --------------------------------------------------------------------------------------

def test_lot_honnete_effectifs_et_composition():
    s, h, _ = lots_d_epreuve()
    c = h.comptes
    assert (c["honnetes"], c["controles-autre-tache"], c["texte-sans-rapport"], c["controles-generiques"]) == (576, 128, 64, 64)
    assert c["effectif"] == len(h.appels) == 832 and h.constats == ()
    d = h.descriptions()
    gen = [x["generique"] for x in d if x["composante"] == "controles-generiques"]
    assert sorted(gen) == [k for k in (1, 2, 3, 4) for _ in range(16)]
    for x in d:
        assert x["tache"] in s.ouvertes
        if x["composante"] == "controles-autre-tache":
            assert x["donneuse"][0] != x["tache"] and x["donneuse"][0] in s.ouvertes
        if x["composante"] == "texte-sans-rapport":
            assert x["cle_alea"] == g.cle_alea("lot-honnete-appariement", x["tache"], x["episode"], x["pas"])
    for comp, n in (("controles-autre-tache", 128), ("texte-sans-rapport", 64), ("controles-generiques", 64)):
        assert len({L._pos(x) for x in d if x["composante"] == comp}) == n           # sans remise


def test_lot_honnete_refuse_verification_et_gardees():
    s = sep()
    with pytest.raises(GardeArret, match="tâche permise"):
        L.lot_honnete_appariement(s, E, jugeables(s.ouvertes) + [(VER[0], 0, 0)])
    with pytest.raises(GardeArret, match="tâche permise"):
        L.lot_honnete_appariement(s, E, jugeables(s.ouvertes) + [(s.gardees[0], 0, 0)])
    with pytest.raises(GardeArret, match="tâche permise"):
        L.lot_honnete_appariement(s, E, jugeables(s.ouvertes), revision=True)
    with pytest.raises(GardeArret, match="double"):
        L.lot_honnete_appariement(s, E, jugeables(s.ouvertes) + [(s.ouvertes[0], 0, 0)])
    with pytest.raises(GardeArret):
        L.lot_honnete_appariement(s, E, [(s.ouvertes[0], 8, 0)])
    with pytest.raises(GardeArret):
        L.lot_honnete_appariement(s, E, [])


def test_epreuves_jointes_toutes_prises_sous_l_effectif():
    s = sep()
    h = L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 96))
    assert h.comptes["controles-autre-tache"] == 96 and h.comptes["texte-sans-rapport"] == 64
    assert h.comptes["controles-generiques"] == 64
    h = L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 40))
    assert h.comptes["controles-autre-tache"] == 40 and h.comptes["texte-sans-rapport"] == 40


def _generiques(h):
    return {L._pos(x): x["generique"] for x in h.descriptions() if x["composante"] == "controles-generiques"}


@pytest.mark.parametrize("n,parts", [(64, [16, 16, 16, 16]), (63, [16, 16, 16, 15]), (33, [9, 8, 8, 8]),
                                     (32, [8, 8, 8, 8])])
def test_generiques_au_dessus_et_sur_le_plancher(n, parts):
    s = sep()
    jug = n_jugeables(s.ouvertes, n)
    h = L.lot_honnete_appariement(s, E, jug)
    gen = _generiques(h)
    assert h.comptes["controles-generiques"] == n and h.constats == ()
    assert [sorted(gen.values()).count(k) for k in (1, 2, 3, 4)] == parts
    hon = sorted(jug)
    rng = g.generateur_de(g.cle("join", "controles-generiques"), E)
    if n == 64:                                       # cas complet : 64 tirées, puis attribution
        rec = [hon[int(i)] for i in rng.choice(len(hon), 64, replace=False)]
    else:                                             # 32 à 63 : toutes, sans tirage des actions
        rec = hon
    textes = rng.permutation(L.textes_a_parts_egales(n))
    assert gen == {p: int(k) for p, k in zip(rec, textes)}


def test_generiques_sous_le_plancher_constat():
    s = sep()
    h = L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 31))
    assert h.comptes["controles-generiques"] == 0 and not _generiques(h)
    (k,) = h.constats
    assert (k.objet, k.epreuve, dict(k.comptes), dict(k.planchers), k.sous_le_plancher) == \
        ("controles-generiques", "ouverte", {"honnetes-jugeables": 31}, {"honnetes-jugeables": 32}, ["honnetes-jugeables"])
    assert k.contenu()["issue"] == "effectif insuffisant" and "génériques" in k.suite
    assert h.contenu()["constats"] == [k.contenu()]                    # le constat est dans les octets du lot
    assert h.comptes["controles-autre-tache"] == 31                    # le reste du lot est construit
    s2, hr = sep(), L.lot_honnete_appariement(s, E, n_jugeables(s.gardees, 20), revision=True)
    assert hr.constats[0].epreuve == "revision" and hr.constats[0].cle == "effectif-insuffisant/revision/controles-generiques"


def test_textes_a_parts_egales_gardes():
    assert L.textes_a_parts_egales(64) == [k for k in (1, 2, 3, 4) for _ in range(16)]
    assert L.textes_a_parts_egales(34) == [1] * 9 + [2] * 9 + [3] * 8 + [4] * 8
    for mauvais in (31, 65, True, 40.0):
        with pytest.raises(GardeArret):
            L.textes_a_parts_egales(mauvais)


def test_ordre_et_identifiants_par_les_seules_cles():
    s, h, _ = lots_d_epreuve()
    canon = sorted(h.descriptions(), key=L._tri)
    n = len(canon)
    ordre = g.ordre_des_appels("lot-honnete-appariement", n, E)
    assert h.descriptions() == [canon[i] for i in ordre]
    assert [a["identifiant"] for a in h.appels] == g.identifiants_opaques("lot-honnete-appariement", n, E)
    assert [a["rang"] for a in h.appels] == list(range(1, n + 1))


def test_aucun_autre_alea(monkeypatch):
    """Tout générateur naît d'une clé de la table de 6.2, par `generateur_de` ; tout autre aléa numpy est refusé."""
    vues, dedans = [], []
    vrai_g, vrai_rng = g.generateur_de, np.random.default_rng

    def espion(cle, e):
        vues.append(cle)
        g.exiger_cle_de_la_table(cle)
        dedans.append(1)
        try:
            return vrai_g(cle, e)
        finally:
            dedans.pop()

    def rng_garde(*a, **k):
        if not dedans:
            raise AssertionError("aléa hors d'une clé de 6.2")
        return vrai_rng(*a, **k)

    monkeypatch.setattr(g, "generateur_de", espion)
    monkeypatch.setattr(np.random, "default_rng", rng_garde)
    for nom in ("choice", "permutation", "integers", "shuffle", "random", "randint"):
        if hasattr(np.random, nom):
            monkeypatch.setattr(np.random, nom, lambda *a, **k: (_ for _ in ()).throw(AssertionError("aléa global")))
    s, lot = decisif()
    hc = couverture(s, sans=[(s.ouvertes[0], 0)])
    L.lot_mecanique_couverture(s, E, hc, artefacts(s, hc))
    L.ancre_couverture(s, E, hc)
    L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 40))
    assert vues and all(c.startswith(("bras-a-v2/", "revision/bras-a-v2/")) for c in vues)
    assert any(c.endswith("ordr/lot-decisif") for c in vues) and any(c.endswith("relu/lot-decisif/plans") for c in vues)


def test_determinisme_octet_pour_octet():
    _, a = decisif()
    _, b = decisif()
    assert a.octets() == b.octets() and a.empreinte == b.empreinte
    _, c = decisif(E + 1)
    assert c.empreinte != a.empreinte
    s, h1, j1 = lots_d_epreuve()
    _, h2, j2 = lots_d_epreuve()
    assert h1.octets() == h2.octets() and j1.octets() == j2.octets()
    for n in (31, 40):                                               # effectifs réduits, constat compris
        x, y = (L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, n)) for _ in range(2))
        assert x.octets() == y.octets()
    sans = [(s.ouvertes[i], i) for i in range(8)]
    x, y = (couverture(s, sans=sans) for _ in range(2))
    assert x.octets() == y.octets()
    x, y = (couverture(s, sans=plans(s.ouvertes)[:33]) for _ in range(2))
    assert isinstance(x, L.Constat) and x.octets() == y.octets() and x.empreinte == y.empreinte


def test_egal_a_la_version_1_au_cas_complet():
    """Au cas complet, le brouillon 50 ne change aucun tirage : mêmes octets que la version 1."""
    s1 = L1.separation(FAB, VER, E)
    s, h, j = lots_d_epreuve()
    h1 = L1.lot_honnete_appariement(s1, E, jugeables(s1.ouvertes))
    j1 = L1.lot_jumeaux_appariement(s1, E, h1, deplacees(s1.ouvertes))
    assert h.octets() == h1.octets() and j.octets() == j1.octets()
    assert L.ancre_plans_honnetes(s, E, h).octets() == L1.ancre_plans_honnetes(s1, E, h1).octets()
    assert L.ancre_jumeaux(s, E, deplacees(s.ouvertes)).octets() == L1.ancre_jumeaux(s1, E, deplacees(s1.ouvertes)).octets()
    hc = couverture(s)
    assert L.plans_mecaniques(s, E, hc) == L1.plans_mecaniques(s1, E)
    assert L.ancre_couverture(s, E, hc).octets() == L1.ancre_couverture(s1, E).octets()
    assert L.lot_mecanique_couverture(s, E, hc, artefacts(s, hc)).octets() == \
        L1.lot_mecanique_couverture(s1, E, artefacts(s, hc)).octets()
    _, d = decisif()
    d1 = decisif_v1()
    assert [x for x in d.descriptions()] == [x for x in d1.descriptions()]
    assert d.appels == d1.appels and {k: v for k, v in d.comptes.items() if k != "relues-par-classe"} == dict(d1.comptes)


# --- Ancres --------------------------------------------------------------------------------------------------------------

def test_ancre_plans_honnetes_au_dessus():
    s, h, _ = lots_d_epreuve()
    a = L.ancre_plans_honnetes(s, E, h)
    d = a.descriptions()
    assert len(d) == 48 and sum(x["composante"] == "honnete" for x in d) == 24
    assert all(x in h.descriptions() for x in d)
    with pytest.raises(GardeArret):                       # lot de la révision exigé sous la révision
        L.ancre_plans_honnetes(s, E, h, revision=True)


def test_ancre_plans_honnetes_sur_et_sous_le_plancher():
    s = sep()
    h = L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 24))
    a = L.ancre_plans_honnetes(s, E, h)                   # 24 et 24 : toutes prises
    assert isinstance(a, L.Lot) and len(a.appels) == 48
    assert sorted(L._pos(x) for x in a.descriptions() if x["composante"] == "honnete") == sorted(n_jugeables(s.ouvertes, 24))
    h = L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 23))
    k = L.ancre_plans_honnetes(s, E, h)
    assert isinstance(k, L.Constat) and k.objet == "ancre-plans-honnetes" and "A5" in k.suite
    assert k.sous_le_plancher == ["controles-autre-tache", "honnete"] and dict(k.comptes)["honnete"] == 23


def test_ancre_jumeaux_au_dessus_sur_et_sous_le_plancher():
    s = sep()
    a = L.ancre_jumeaux(s, E, deplacees(s.ouvertes))
    assert len(a.appels) == 24 and all(x["composante"] == "jumeau-a-effet" for x in a.descriptions())
    a = L.ancre_jumeaux(s, E, n_a_effet(s.ouvertes, 24))
    assert isinstance(a, L.Lot) and sorted(L._pos(x) for x in a.descriptions()) == \
        sorted(x[:3] for x in n_a_effet(s.ouvertes, 24) if x[3] == A_EFFET)
    k = L.ancre_jumeaux(s, E, n_a_effet(s.ouvertes, 23))
    assert isinstance(k, L.Constat) and dict(k.comptes) == {"jumeau-a-effet": 23} and "A7" in k.suite
    kr = L.ancre_jumeaux(s, E, n_a_effet(s.gardees, 10), revision=True)
    assert kr.epreuve == "revision"
    with pytest.raises(GardeArret):
        L.ancre_jumeaux(s, E, deplacees(s.ouvertes) + [(s.ouvertes[0], 0, 9, "autre")])


def test_tirer_inatteignable_arrete():
    rng = g.generateur_de(g.cle("ancr", "premiere"), E)
    with pytest.raises(GardeArret, match="inatteignable"):
        L._tirer(rng, list(range(23)), 24, "essai")
    assert sorted(L._tirer(g.generateur_de(g.cle("ancr", "premiere"), E), list(range(24)), 24, "essai")) == list(range(24))


# --- Lot des jumeaux de l'appariement ---------------------------------------------------------------------------------------

def test_lot_jumeaux_composition():
    s, h, j = lots_d_epreuve()
    d = j.descriptions()
    dep = [x for x in d if x["composante"] == "deplacee"]
    assert len(dep) == 64 * 4 and {x["verite"] for x in dep} == {A_EFFET, SANS_EFFET}
    assert j.comptes["deplacees-non-jugeables"] == 64 and j.comptes["honnetes-relues"] == 576
    assert len(d) == 256 + 576
    ids_h = {a["identifiant"] for a in h.appels}
    assert not ids_h & {a["identifiant"] for a in j.appels}
    with pytest.raises(GardeArret):
        L.lot_jumeaux_appariement(s, E, j, deplacees(s.ouvertes))
    with pytest.raises(GardeArret, match="tâche permise"):
        L.lot_jumeaux_appariement(s, E, h, deplacees(s.ouvertes) + [(VER[0], 0, 0, A_EFFET)])


def test_revision_cles_et_taches_gardees():
    s, h, j = lots_d_epreuve(revision=True)
    assert h.cle_ordre == "revision/bras-a-v2/ordr/lot-honnete-appariement"
    assert all(x["tache"] in s.gardees for x in h.descriptions() + j.descriptions())
    _, ho, _ = lots_d_epreuve()
    assert ho.octets() != h.octets()
    x = next(x for x in h.descriptions() if x["composante"] == "texte-sans-rapport")
    assert x["cle_alea"].startswith("revision/bras-a-v2/alea/")
    a = L.ancre_plans_honnetes(s, E, h, revision=True)
    assert a.cle_identifiants == "revision/bras-a-v2/opaq/ancre-plans-honnetes"
    with pytest.raises(GardeArret):
        g.cle("ordr", "lot-honnete-couverture", revision=True)


# --- Couverture --------------------------------------------------------------------------------------------------------

def test_lot_honnete_couverture_complet_et_plans_qui_manquent():
    s = sep()
    lot = couverture(s)
    assert len(lot.appels) == 64 and lot.comptes["lectures"] == 128 and lot.comptes["episodes-sans-plan"] == 0
    sans = plans(s.ouvertes)[:10]
    lot = couverture(s, sans=sans, laisses=plans(s.ouvertes)[10:12])
    assert len(lot.appels) == 54 and lot.comptes["lectures"] == 108
    assert (lot.comptes["episodes-sans-plan"], lot.comptes["plans-deplaces-dose-1"],
            lot.comptes["laisses-honnetes-dose-1"]) == (10, 52, 12)
    assert all((x["tache"], x["episode"]) not in sans for x in lot.descriptions())


def test_couverture_sur_et_sous_les_planchers():
    s = sep()
    tous = plans(s.ouvertes)
    assert len(couverture(s, sans=tous[:32]).appels) == 32                       # 32 plans, 32 déplacés : construit
    k = couverture(s, sans=tous[:33])                                             # 31 plans
    assert isinstance(k, L.Constat) and k.objet == "couverture" and k.sous_le_plancher == ["plans-deplaces-dose-1",
                                                                                            "plans-honnetes"]
    assert "instrument de couverture en échec" in k.suite and k.epreuve == "ouverte"
    k = couverture(s, laisses=tous[:33])                                          # 64 plans, 31 déplacés
    assert isinstance(k, L.Constat) and k.sous_le_plancher == ["plans-deplaces-dose-1"]
    assert isinstance(couverture(s, laisses=tous[:32]), L.Lot)


def test_couverture_gardes_de_la_construction():
    s = sep()
    tous = plans(s.ouvertes)
    with pytest.raises(GardeArret, match="64"):                                   # un plan absent de son lot
        L.lot_honnete_couverture(s, E, tous[:-1], [], tous, [])
    with pytest.raises(GardeArret, match="64"):                                   # plan et sans plan à la fois
        L.lot_honnete_couverture(s, E, tous, [tous[0]], tous, [])
    with pytest.raises(GardeArret, match="64"):                                   # recouvrement à 64 juste
        L.lot_honnete_couverture(s, E, tous[1:], [tous[1]], tous, [])
    with pytest.raises(GardeArret, match="64"):                                   # dose 1 : ne fait pas 64
        L.lot_honnete_couverture(s, E, tous, [], tous[1:], [])
    with pytest.raises(GardeArret, match="sans plan"):                            # sans plan présenté comme déplacé
        L.lot_honnete_couverture(s, E, tous[1:], [tous[0]], tous, [])
    with pytest.raises(GardeArret, match="tâche permise"):
        L.lot_honnete_couverture(s, E, tous[:-1] + [(VER[0], 0)], [], tous, [])
    with pytest.raises(GardeArret, match="double"):
        L.lot_honnete_couverture(s, E, tous + [tous[0]], [], tous, [])


def test_plans_mecaniques_et_ancre_couverture():
    s = sep()
    hc = couverture(s)
    m = L.plans_mecaniques(s, E, hc)
    assert len(m) == len(set(m)) == 32 and all(sum(t == u for u, _ in m) == 4 for t in s.ouvertes)
    a = L.ancre_couverture(s, E, hc)
    assert len(a.appels) == 8 and all((x["tache"], x["episode"]) in m for x in a.descriptions())
    t0, t1 = s.ouvertes[0], s.ouvertes[1]                                  # t0 : 3 plans ; t1 : aucun ; t2 : 5
    sans = [(t0, k) for k in range(3, 8)] + [(t1, k) for k in range(8)] + [(s.ouvertes[2], k) for k in range(5, 8)]
    hc = couverture(s, sans=sans)
    m = L.plans_mecaniques(s, E, hc)
    assert sorted(p for p in m if p[0] == t0) == [(t0, 0), (t0, 1), (t0, 2)] and not [p for p in m if p[0] == t1]
    de_t2 = [(s.ouvertes[2], k) for k in range(5)]
    i = g.generateur_de(g.cle("meca", s.ouvertes[2]), E).choice(5, 4, replace=False)
    assert sorted(p for p in m if p[0] == s.ouvertes[2]) == sorted(de_t2[int(j)] for j in i)
    assert len(m) == 3 + 0 + 4 + 4 * 5
    tous = plans(s.ouvertes)                                               # au plancher : 4 tâches pleines, 16 méca
    hc = couverture(s, sans=[p for p in tous if p[0] in s.ouvertes[4:]])
    assert len(L.plans_mecaniques(s, E, hc)) == 16 and len(L.ancre_couverture(s, E, hc).appels) == 8
    with pytest.raises(GardeArret):
        L.plans_mecaniques(s, E, L.lot_honnete_appariement(s, E, jugeables(s.ouvertes)))


def test_lot_mecanique():
    s = sep()
    hc = couverture(s)
    lot = L.lot_mecanique_couverture(s, E, hc, artefacts(s, hc))
    assert len(lot.appels) == 160 and lot.comptes["lectures"] == 256
    a = artefacts(s, hc)
    moins = [x for x in a if not (x[0] == "plan-tronque" and x[1:3] == a[0][1:3])]
    assert L.lot_mecanique_couverture(s, E, hc, moins).comptes["plan-tronque"] == 31
    hors = next((t, k) for t in s.ouvertes for k in range(8) if (t, k) not in L.plans_mecaniques(s, E, hc))
    for mauvais in ([x for x in a if x[0] != "dose-flagrante" or x[1:3] != a[0][1:3]],     # 31 doses flagrantes
                    a + [("plan-tronque",) + hors + (None,)], a + [a[0]],
                    a[1:] + [("retrait",) + a[0][1:3] + (None,)],
                    a + [("autre", a[0][1], a[0][2], None)]):
        with pytest.raises(GardeArret):
            L.lot_mecanique_couverture(s, E, hc, mauvais)
    hc = couverture(s, sans=[(t, k) for t in s.ouvertes[:3] for k in range(8)])        # 40 plans, 20 méca
    a = artefacts(s, hc)
    lot = L.lot_mecanique_couverture(s, E, hc, a)
    assert (lot.comptes["reference-d-une-autre-tache"], lot.comptes["retrait"], len(lot.appels)) == (20, 40, 100)
    with pytest.raises(GardeArret, match="exactement 20"):
        L.lot_mecanique_couverture(s, E, hc, [x for x in a if x[0] != "reference-d-une-autre-tache" or x[1:3] != a[0][1:3]])


def test_lot_jumeaux_couverture():
    s = sep()
    hc = couverture(s)
    tous = plans(s.ouvertes)
    lot = L.lot_jumeaux_couverture(s, E, hc, tous, [])
    assert len(lot.appels) == 128 and lot.comptes["lectures"] == 256
    with pytest.raises(GardeArret):
        L.lot_jumeaux_couverture(s, E, lot, tous, [])
    sans, laisses = tous[:6], tous[6:20]
    hc = couverture(s, sans=sans, laisses=laisses)
    lot = L.lot_jumeaux_couverture(s, E, hc, tous[20:], tous[:20])
    assert (lot.comptes["plans-deplaces"], lot.comptes["plans-d-epreuve-relus"], len(lot.appels)) == (44, 58, 102)
    assert all((x["tache"], x["episode"]) not in tous[:20] for x in lot.descriptions() if x["composante"] == "plan-deplace")
    with pytest.raises(GardeArret, match="comptés"):                       # autres plans déplacés que ceux comptés
        L.lot_jumeaux_couverture(s, E, hc, tous[19:], tous[:19])
    with pytest.raises(GardeArret, match="sans plan"):                     # épisode sans plan donné comme déplacé
        L.lot_jumeaux_couverture(s, E, hc, tous[:1] + tous[20:], tous[1:20])


# --- Lot décisif -------------------------------------------------------------------------------------------------------

def test_lot_decisif_sain():
    s, lot = decisif()
    c = lot.comptes
    assert c["action-de-condition"] == 8960 and c["sentinelle-deplacee"] == 64 * 2 + 64 * 1
    assert c["action-d-epreuve-relue"] == 320 and c["plan-de-condition"] == 896 and c["plan-d-epreuve-relu"] == 32
    assert c["relues-par-classe"] == 160
    sen, con = lot.tables[L.TABLE_DES_SENTINELLES], lot.tables[L.TABLE_DES_CONDITIONS]
    assert not set(sen) & set(con) and set(sen) | set(con) == {a["identifiant"] for a in lot.appels}
    assert all("condition" not in d for d in sen.values()) and all("condition" in d for d in con.values())
    relues = [d for d in sen.values() if d["composante"] == "action-d-epreuve-relue"]
    assert sum(d["classe"] == "honnete" for d in relues) == 160 and all(d["tache"] in s.ouvertes for d in relues)
    assert all(d["tache"] in s.verification for d in sen.values() if d["composante"] == "sentinelle-deplacee")


def test_lot_decisif_gardes():
    with pytest.raises(GardeArret, match="non déclarée"):
        decisif(actions_des_conditions=[(c, t, 0, 0) for c in COND for t in VER] + [(COND[0], FAB[0], 0, 0)])
    with pytest.raises(GardeArret, match="7"):
        decisif(actions_des_conditions=[(c, t, 0, 0) for c in COND[:6] for t in VER])
    with pytest.raises(GardeArret, match="128"):
        decisif(a_effet_des_jumeaux={(t, 0): [1] for t in VER})
    with pytest.raises(GardeArret, match="non lue"):
        decisif(couverture_lue=False, plans_des_conditions=[])
    with pytest.raises(GardeArret, match="double"):
        decisif(plans_des_conditions=[(c, t, k) for c in COND for t in VER for k in range(8)] + [(COND[0], VER[0], 0)])
    with pytest.raises(GardeArret):                       # lots d'épreuve de deux épreuves différentes
        _, hr, _ = lots_d_epreuve(revision=True)
        decisif(lot_honnete_en_vigueur=hr)
    with pytest.raises(GardeArret):
        decisif(couverture_lue="oui")


def test_lot_decisif_sans_couverture_et_revision():
    s, lot = decisif(couverture_lue=False)
    assert "plan-de-condition" not in lot.comptes and "plan-d-epreuve-relu" not in lot.comptes
    s, lot = decisif(revision=True)
    relues = [d for d in lot.tables["sentinelles"].values() if d["composante"] == "action-d-epreuve-relue"]
    assert all(d["tache"] in s.gardees and d["epreuve"] == "revision" for d in relues)


def test_plans_decisifs_reduits_dans_la_couverture():
    s = sep()
    hc = couverture(s, sans=plans(s.ouvertes)[:30])                       # 34 plans : 32 relus tirés parmi eux
    _, lot = decisif(lot_honnete_couverture_=hc)
    relus = [d for d in lot.descriptions() if d["composante"] == "plan-d-epreuve-relu"]
    assert len(relus) == 32 and all((d["tache"], d["episode"]) in plans(s.ouvertes)[30:] for d in relus)


def _relues(lot, classe):
    return sorted(L._pos(d) for d in lot.tables["sentinelles"].values()
                  if d["composante"] == "action-d-epreuve-relue" and d["classe"] == classe)


def _decisif_relues(n_hon, n_dep, revision=False):
    s = sep()
    taches = s.gardees if revision else s.ouvertes
    h = L.lot_honnete_appariement(s, E, n_jugeables(taches, n_hon), revision=revision)
    j = L.lot_jumeaux_appariement(s, E, h, n_a_effet(taches, n_dep), revision=revision)
    return s, h, j, decisif(lot_honnete_en_vigueur=h, lot_jumeaux_en_vigueur=j, couverture_lue=False)[1]


def test_relues_au_complet_tirees_meme_a_160():
    """Au complet (deux classes d'au moins 160), chaque classe est tirée, même une classe de 160 juste (6.2 ; 6.8)."""
    s, h, j, lot = _decisif_relues(160, 200)
    hon, dep = sorted(n_jugeables(s.ouvertes, 160)), sorted(x[:3] for x in n_a_effet(s.ouvertes, 200) if x[3] == A_EFFET)
    rng = g.generateur_de(g.cle("relu", "lot-decisif", "actions"), E)
    rng.choice(160, 160, replace=False)
    attendu = sorted(dep[int(i)] for i in rng.choice(200, 160, replace=False))
    assert _relues(lot, "honnete") == hon and _relues(lot, "deplacee") == attendu and lot.comptes["relues-par-classe"] == 160


def test_relues_sous_le_complet_classe_courte_entiere():
    s, h, j, lot = _decisif_relues(128, 200)                               # n = 128 : honnêtes entières, sans tirage
    hon, dep = sorted(n_jugeables(s.ouvertes, 128)), sorted(x[:3] for x in n_a_effet(s.ouvertes, 200) if x[3] == A_EFFET)
    rng = g.generateur_de(g.cle("relu", "lot-decisif", "actions"), E)
    assert _relues(lot, "honnete") == hon
    assert _relues(lot, "deplacee") == sorted(dep[int(i)] for i in rng.choice(200, 128, replace=False))
    assert lot.comptes["relues-par-classe"] == 128 and lot.comptes["action-d-epreuve-relue"] == 256
    s, h, j, lot = _decisif_relues(576, 100)                               # n = 100 : déplacées entières
    hon = sorted(n_jugeables(s.ouvertes, 576))
    rng = g.generateur_de(g.cle("relu", "lot-decisif", "actions"), E)
    assert _relues(lot, "honnete") == sorted(hon[int(i)] for i in rng.choice(576, 100, replace=False))
    assert _relues(lot, "deplacee") == sorted(x[:3] for x in n_a_effet(s.ouvertes, 100) if x[3] == A_EFFET)


def test_relues_sur_et_sous_le_plancher():
    s, h, j, lot = _decisif_relues(80, 80)                                 # au plancher : 80 et 80, entières
    assert isinstance(lot, L.Lot) and lot.comptes["relues-par-classe"] == 80
    for n_hon, n_dep, sous in ((79, 200, ["honnetes"]), (200, 79, ["deplacees-a-effet"])):
        s, h, j, k = _decisif_relues(n_hon, n_dep)
        assert isinstance(k, L.Constat) and k.objet == "actions-d-epreuve-relues" and k.sous_le_plancher == sous
        assert "A10" in k.suite and "n'est pas construit" in k.suite
    s, h, j, k = _decisif_relues(79, 79, revision=True)
    assert k.epreuve == "revision" and k.cle == "effectif-insuffisant/revision/actions-d-epreuve-relues"
    s, h, j, _ = _decisif_relues(79, 200)                                  # les gardes jouent avant le constat
    with pytest.raises(GardeArret, match="7"):
        decisif(lot_honnete_en_vigueur=h, lot_jumeaux_en_vigueur=j,
                actions_des_conditions=[(c, t, 0, 0) for c in COND[:6] for t in VER])


# --- Ambiguïtés restantes -------------------------------------------------------------------------------------------------

def test_ambiguites_restantes():
    s = sep()
    with pytest.raises(L.AmbiguiteDuTexte, match="autre tâche"):          # aucune donneuse d'une autre tâche
        L.lot_honnete_appariement(s, E, [(s.ouvertes[0], k, p) for k in range(8) for p in range(9)])
    with pytest.raises(L.AmbiguiteDuTexte, match="sans plan"):            # épisode réglé sans plan au lot décisif
        decisif(plans_des_conditions=[(c, t, k) for c in COND for t in VER for k in range(8)][:-1])
    assert issubclass(L.AmbiguiteDuTexte, GardeArret)


def test_constat_mal_forme_refuse():
    with pytest.raises(GardeArret):
        L.Constat("x", "ouverte", {"a": 5}, {"a": 4}, "suite")             # aucun compte sous le plancher
    with pytest.raises(GardeArret):
        L.Constat("x", "autre", {"a": 3}, {"a": 4}, "suite")
    with pytest.raises(GardeArret):
        L.Constat("x", "ouverte", {"a": 3}, {"b": 4}, "suite")
    assert L.Constat("x", "ouverte", {"a": 3}, {"a": 4}, "suite").sous_le_plancher == ["a"]


# --- Manifeste ---------------------------------------------------------------------------------------------------------

def test_manifeste():
    s, lot = decisif(couverture_lue=False)
    m = {}
    ligne = L.inscrire_au_manifeste(m, lot)
    assert m["lots"]["bras-a-v2/ordr/lot-decisif"]["sha256"] == lot.empreinte == ligne["sha256"]
    assert set(ligne["sha256_des_tables"]) == {"sentinelles", "conditions"}
    L.inscrire_au_manifeste(m, lot)
    _, autre = decisif(E + 1, couverture_lue=False)
    with pytest.raises(GardeArret, match="R12"):
        L.inscrire_au_manifeste(m, autre)
    k = couverture(s, sans=plans(s.ouvertes)[:40])
    ligne = L.inscrire_au_manifeste(m, k)
    assert m["constats"]["effectif-insuffisant/couverture"]["sha256"] == k.empreinte == ligne["sha256"]
    assert ligne["issue"] == "effectif insuffisant"
    L.inscrire_au_manifeste(m, k)
    with pytest.raises(GardeArret, match="R12"):
        L.inscrire_au_manifeste(m, couverture(s, sans=plans(s.ouvertes)[:41]))
    h = L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 30))
    ligne = L.inscrire_au_manifeste(m, h)
    assert ligne["constats"] == ["effectif-insuffisant/controles-generiques"]
    assert m["constats"]["effectif-insuffisant/controles-generiques"]["sha256"] == h.constats[0].empreinte
    with pytest.raises(GardeArret):
        L.inscrire_au_manifeste(m, "lot")


# --- Voie de service du juge --------------------------------------------------------------------------------------------

def test_tableau_des_cles():
    t = L.tableau_des_cles(5)
    assert [x["cle"] for x in t] == ["GEMINI_API_KEY", "GEMINI_API_KEY_2"] * 2 + ["GEMINI_API_KEY"]
    assert [x["rang"] for x in t] == [1, 2, 3, 4, 5]
    L.exiger_tableau_des_cles(t, 5)
    for mauvais in ([dict(x, item="abc") if x["rang"] == 2 else x for x in t],
                    [dict(x, cle="GEMINI_API_KEY") for x in t], t[:4]):
        with pytest.raises(GardeArret):
            L.exiger_tableau_des_cles(mauvais, 5)
    assert L.cle_de_l_envoi(t, 2) == "GEMINI_API_KEY_2"
    assert L.cle_de_l_envoi(t, 3, "GEMINI_API_KEY") == "GEMINI_API_KEY"
    with pytest.raises(GardeArret, match="écart"):
        L.cle_de_l_envoi(t, 3, "GEMINI_API_KEY_2")
    for r in (0, 6):
        with pytest.raises(GardeArret):
            L.cle_de_l_envoi(t, r)
    with pytest.raises(GardeArret):
        L.tableau_des_cles(0)


def test_voie_de_service_des_trois_lots_et_de_la_revision():
    s, h, _ = lots_d_epreuve()
    hc = couverture(s)
    assert L.voie_de_service_du_juge(L.ancre_jumeaux(s, E, deplacees(s.ouvertes))) == L.tableau_des_cles(24)
    assert L.voie_de_service_du_juge(L.ancre_plans_honnetes(s, E, h)) == L.tableau_des_cles(48)
    assert L.voie_de_service_du_juge(L.ancre_couverture(s, E, hc)) == L.tableau_des_cles(8)
    _, hr, _ = lots_d_epreuve(revision=True)
    assert L.voie_de_service_du_juge(L.ancre_plans_honnetes(s, E, hr, revision=True)) == L.tableau_des_cles(48)
    assert L.voie_de_service_du_juge(L.ancre_jumeaux(s, E, deplacees(s.gardees), revision=True)) == L.tableau_des_cles(24)
    with pytest.raises(GardeArret, match="pas un lot du juge"):
        L.voie_de_service_du_juge(h)
    ac = L.ancre_couverture(s, E, hc)
    with pytest.raises(GardeArret, match="révision"):
        L.voie_de_service_du_juge(L.Lot("ancre-couverture", True, ac.appels, ac.tables, ac.comptes))


def test_ancre_incomplete_refusee():
    s = sep()
    a = L.ancre_jumeaux(s, E, deplacees(s.ouvertes))
    ids = [x["identifiant"] for x in a.appels[:23]]
    court = L.Lot("ancre-jumeaux", False, a.appels[:23],
                  {"entrees": {i: a.tables["entrees"][i] for i in ids}}, a.comptes)
    with pytest.raises(GardeArret, match="au complet"):
        L.voie_de_service_du_juge(court)
    _, h, _ = lots_d_epreuve()
    ap = L.ancre_plans_honnetes(s, E, h)
    faux = {i: (dict(d, composante="honnete") if d["composante"] == "controles-autre-tache" else d)
            for i, d in ap.tables["entrees"].items()}                     # 48 dont 48 honnêtes : composition fausse
    with pytest.raises(GardeArret, match="au complet"):
        L.voie_de_service_du_juge(L.Lot("ancre-plans-honnetes", False, ap.appels, {"entrees": faux}, ap.comptes))


def test_voie_de_service_de_l_etape_d():
    s, h, _ = lots_d_epreuve()
    hc = couverture(s)
    ap, ac = L.ancre_plans_honnetes(s, E, h), L.ancre_couverture(s, E, hc)
    v = L.voie_de_service_de_l_etape_d(ap, ac)
    assert [x["lot"] for x in v] == ["bras-a-v2/ordr/ancre-plans-honnetes", "bras-a-v2/ordr/ancre-couverture"]
    assert v[0]["tableau"] == L.tableau_des_cles(48) and v[1]["tableau"] == L.tableau_des_cles(8)   # rang à 1 par lot
    kc = couverture(s, sans=plans(s.ouvertes)[:40])                         # instrument en échec : ancre non jugée
    assert [x["lot"] for x in L.voie_de_service_de_l_etape_d(ap, kc)] == ["bras-a-v2/ordr/ancre-plans-honnetes"]
    kp = L.ancre_plans_honnetes(s, E, L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 20)))
    assert [x["lot"] for x in L.voie_de_service_de_l_etape_d(kp, ac)] == ["bras-a-v2/ordr/ancre-couverture"]
    assert L.voie_de_service_de_l_etape_d(kp, kc) == []
    _, hr, _ = lots_d_epreuve(revision=True)
    apr = L.ancre_plans_honnetes(s, E, hr, revision=True)
    assert [x["lot"] for x in L.voie_de_service_de_l_etape_d(apr, None)] == \
        ["revision/bras-a-v2/ordr/ancre-plans-honnetes"]
    for mauvais in ((ac, ap), (ap, None), (apr, ac), (ap, kp), (kc, ac), (h, ac)):
        with pytest.raises(GardeArret):
            L.voie_de_service_de_l_etape_d(*mauvais)


# --- Tirages recalculés à la main depuis les clés (mutations) ----------------------------------------------------------

def test_tirages_recalcules_depuis_les_cles():
    s, h, _ = lots_d_epreuve()
    _, lot = decisif()
    sen = lot.tables["sentinelles"].values()
    t, k = s.verification[0], 1                                  # trois candidats : 0, 3, 5
    i = g.generateur_de(g.cle_sentinelles(t, k), E).choice(3, 2, replace=False)
    assert sorted(d["pas"] for d in sen if d["composante"] == "sentinelle-deplacee" and (d["tache"], d["episode"]) == (t, k)) \
        == sorted([0, 3, 5][int(j)] for j in i)
    a_effet = {(t, k, p) for t in s.ouvertes for k in range(8) for p in (0, 1, 2)}
    assert all(L._pos(d) in a_effet for d in sen if d["composante"] == "action-d-epreuve-relue" and d["classe"] == "deplacee")


def test_donneuses_et_ordre_de_la_revision_recalcules():
    s, h, _ = lots_d_epreuve()
    hon = sorted(L._pos(x) for x in h.descriptions() if x["composante"] == "honnete")
    rng = g.generateur_de(g.cle("join", "controles-autre-tache"), E)
    attendu = {}
    for p in [hon[int(i)] for i in rng.choice(len(hon), 128, replace=False)]:
        d = [q for q in hon if q[0] != p[0]]
        attendu[p] = list(d[int(rng.integers(len(d)))])
    assert {L._pos(x): x["donneuse"] for x in h.descriptions() if x["composante"] == "controles-autre-tache"} == attendu
    s, hr, _ = lots_d_epreuve(revision=True)
    canon = sorted(hr.descriptions(), key=L._tri)
    ordre = g.ordre_des_appels("lot-honnete-appariement", len(canon), E, revision=True)
    assert hr.descriptions() == [canon[i] for i in ordre]
    assert [a["identifiant"] for a in hr.appels] == g.identifiants_opaques("lot-honnete-appariement", len(canon), E,
                                                                           revision=True)


# --- Version 3 : corrections de la contre-lecture de la v2 ------------------------------------------------------------

def test_egal_a_la_version_2_hors_des_corrections():
    """Au cas complet (576 honnêtes jugeables), la v3 ne change aucun tirage : mêmes octets que la v2 pour tout lot,
    sauf les comptes des deux lots de la couverture, qui gagnent les clés de m-3 et de m-4 (appels et tables égaux)."""
    s, h, j = lots_d_epreuve()
    s2 = L2.separation(FAB, VER, E)
    h2 = L2.lot_honnete_appariement(s2, E, jugeables(s2.ouvertes))
    j2 = L2.lot_jumeaux_appariement(s2, E, h2, deplacees(s2.ouvertes))
    assert h.octets() == h2.octets() and j.octets() == j2.octets()
    assert L.ancre_plans_honnetes(s, E, h).octets() == L2.ancre_plans_honnetes(s2, E, h2).octets()
    assert L.ancre_jumeaux(s, E, deplacees(s.ouvertes)).octets() == L2.ancre_jumeaux(s2, E, deplacees(s2.ouvertes)).octets()
    tous = plans(s.ouvertes)
    hc = couverture(s)
    hc2 = L2.lot_honnete_couverture(s2, E, tous, [], tous, [])
    assert hc.appels == hc2.appels and hc.tables == hc2.tables
    plus = {k: v for k, v in hc.comptes.items() if k not in hc2.comptes}
    assert set(plus) == {"taches-sans-plan", L.EMPREINTE_DOSE_1} and plus["taches-sans-plan"] == 0
    assert {k: v for k, v in hc.comptes.items() if k in hc2.comptes} == dict(hc2.comptes)
    assert L.ancre_couverture(s, E, hc).octets() == L2.ancre_couverture(s2, E, hc2).octets()
    assert L.lot_mecanique_couverture(s, E, hc, artefacts(s, hc)).octets() == \
        L2.lot_mecanique_couverture(s2, E, hc2, artefacts(s, hc)).octets()
    jc, jc2 = L.lot_jumeaux_couverture(s, E, hc, tous, []), L2.lot_jumeaux_couverture(s2, E, hc2, tous, [])
    assert jc.appels == jc2.appels and jc.tables == jc2.tables
    assert {k: v for k, v in jc.comptes.items() if k != "taches-sans-plan-deplace"} == dict(jc2.comptes)
    _, d = decisif()
    _, d2 = decisif()
    assert d.octets() == d2.octets()
    s2_ = L2.separation(FAB, VER, E)
    d2v = L2.lot_decisif(s2_, E, actions_des_conditions=[(c, t, k, p) for c in COND for t in s2_.verification
                                                         for k in range(8) for p in range(10)],
                         a_effet_des_jumeaux={(t, k): ([0, 3, 5] if k % 2 else [7]) for t in s2_.verification
                                              for k in range(8)},
                         lot_honnete_en_vigueur=h2, lot_jumeaux_en_vigueur=j2, couverture_lue=True,
                         plans_des_conditions=[(c, t, k) for c in COND for t in s2_.verification for k in range(8)],
                         lot_honnete_couverture_=hc2)
    assert d.octets() == d2v.octets()


def _espion_des_tirages(monkeypatch):
    """Relève, par clé, les appels à `choice` des générateurs nés des clés de 6.2."""
    vus = []
    vrai = g.generateur_de

    class Espion:
        def __init__(self, cle, rng):
            self.cle, self.rng = cle, rng

        def choice(self, *a, **k):
            vus.append(self.cle)
            return self.rng.choice(*a, **k)

        def __getattr__(self, nom):
            return getattr(self.rng, nom)

    monkeypatch.setattr(g, "generateur_de", lambda cle, e: Espion(cle, vrai(cle, e)))
    return vus


@pytest.mark.parametrize("n,tire_autre,tire_sans", [(129, True, True), (128, True, True), (127, False, True),
                                                    (65, False, True), (64, False, True), (63, False, False)])
def test_egalite_exacte_tiree(monkeypatch, n, tire_autre, tire_sans):
    """M-2 : « moins … qu'une épreuve n'en demande » au sens strict (ligne 806) ; à l'égalité (128 ; 64), le cas est
    complet et les actions sont tirées par graine (ligne 714), comme les génériques à 64 et les relues à 160."""
    s = sep()
    vus = _espion_des_tirages(monkeypatch)
    h = L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, n))
    assert (g.cle("join", "controles-autre-tache") in vus) == tire_autre
    assert (g.cle("join", "texte-sans-rapport") in vus) == tire_sans
    assert h.comptes["controles-autre-tache"] == min(n, 128) and h.comptes["texte-sans-rapport"] == min(n, 64)


def test_egalite_exacte_donneuses_recalculees():
    """M-2 : à 128 exactement, les 128 sont tirées (`choice`) avant les donneuses ; à 127, toutes, sans tirage. Les
    octets du lot à 128 diffèrent de ceux de la v1 et de la v2 (écart déclaré) ; à 127 et 129, ils sont égaux."""
    s = sep()
    for n, tire in ((128, True), (127, False)):
        hon = sorted(n_jugeables(s.ouvertes, n))
        h = L.lot_honnete_appariement(s, E, hon)
        rng = g.generateur_de(g.cle("join", "controles-autre-tache"), E)
        rec = [hon[int(i)] for i in rng.choice(len(hon), 128, replace=False)] if tire else hon
        attendu = {}
        for p in rec:
            d = [q for q in hon if q[0] != p[0]]
            attendu[p] = list(d[int(rng.integers(len(d)))])
        assert {L._pos(x): x["donneuse"] for x in h.descriptions() if x["composante"] == "controles-autre-tache"} \
            == attendu
    s2 = L2.separation(FAB, VER, E)
    for n, egal in ((128, False), (127, True), (129, True), (64, True)):
        a = L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, n))
        b = L2.lot_honnete_appariement(s2, E, n_jugeables(s2.ouvertes, n))
        assert (a.octets() == b.octets()) == egal


def test_voie_de_service_de_l_etape_e_prime_saine():
    """M-1 : (e′) envoie le seul lot `ancre-jumeaux`, rang à partir de 1 ; à effectif insuffisant, rien (ligne 812)."""
    s, h, _ = lots_d_epreuve()
    ap, aj = L.ancre_plans_honnetes(s, E, h), L.ancre_jumeaux(s, E, deplacees(s.ouvertes))
    v = L.voie_de_service_de_l_etape_e_prime(ap, aj)
    assert v == [{"lot": "bras-a-v2/ordr/ancre-jumeaux", "tableau": L.tableau_des_cles(24)}]
    kj = L.ancre_jumeaux(s, E, n_a_effet(s.ouvertes, 23))
    assert isinstance(kj, L.Constat)
    assert L.voie_de_service_de_l_etape_e_prime(ap, kj) == []                  # aucun arrêt, rien au juge
    kp = L.ancre_plans_honnetes(s, E, L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 20)))
    assert isinstance(kp, L.Constat) and L.voie_de_service_de_l_etape_e_prime(kp, kj) == []
    _, hr, _ = lots_d_epreuve(revision=True)
    apr = L.ancre_plans_honnetes(s, E, hr, revision=True)
    ajr = L.ancre_jumeaux(s, E, deplacees(s.gardees), revision=True)
    assert L.voie_de_service_de_l_etape_e_prime(apr, ajr) == \
        [{"lot": "revision/bras-a-v2/ordr/ancre-jumeaux", "tableau": L.tableau_des_cles(24)}]
    kjr = L.ancre_jumeaux(s, E, n_a_effet(s.gardees, 10), revision=True)
    assert L.voie_de_service_de_l_etape_e_prime(apr, kjr) == []
    m = {}
    L.inscrire_au_manifeste(m, kj)                                             # le constat tient lieu de l'objet
    assert m["constats"]["effectif-insuffisant/ancre-jumeaux"]["sha256"] == kj.empreinte


def test_voie_de_service_de_l_etape_e_prime_artefacts():
    s, h, _ = lots_d_epreuve()
    hc = couverture(s)
    ap, aj = L.ancre_plans_honnetes(s, E, h), L.ancre_jumeaux(s, E, deplacees(s.ouvertes))
    kj = L.ancre_jumeaux(s, E, n_a_effet(s.ouvertes, 23))
    kc = couverture(s, sans=plans(s.ouvertes)[:40])
    _, hr, _ = lots_d_epreuve(revision=True)
    apr = L.ancre_plans_honnetes(s, E, hr, revision=True)
    ajr = L.ancre_jumeaux(s, E, deplacees(s.gardees), revision=True)
    ids = [x["identifiant"] for x in aj.appels[:23]]
    court = L.Lot("ancre-jumeaux", False, aj.appels[:23], {"entrees": {i: aj.tables["entrees"][i] for i in ids}},
                  aj.comptes)
    ap_court = L.Lot("ancre-plans-honnetes", False, ap.appels[:47],
                     {"entrees": {a["identifiant"]: ap.tables["entrees"][a["identifiant"]] for a in ap.appels[:47]}},
                     ap.comptes)
    for mauvais in ((aj, ap), (ap, L.ancre_couverture(s, E, hc)), (ap, kc), (kc, aj), (kc, kj), (ap, None),
                    (None, aj), (ap, ajr), (apr, aj), (apr, kj), (ap, court), (h, aj), (ap_court, aj), (kj, aj)):
        with pytest.raises(GardeArret) as exc:
            L.voie_de_service_de_l_etape_e_prime(*mauvais)
        assert not isinstance(exc.value, L.AmbiguiteDuTexte)                 # un artefact arrête, sans ambiguïté


def test_etape_e_prime_premiere_partie_insuffisante_ambigue():
    """Question de texte (contre-lecture de la v2) : ancre sur plans honnêtes à effectif insuffisant, ancre des jumeaux
    construite — le critère de 812 lit les 24 honnêtes de la première partie : le code ne choisit pas."""
    s = sep()
    kp = L.ancre_plans_honnetes(s, E, L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 20)))
    aj = L.ancre_jumeaux(s, E, deplacees(s.ouvertes))
    with pytest.raises(L.AmbiguiteDuTexte, match="24 honnêtes"):
        L.voie_de_service_de_l_etape_e_prime(kp, aj)


def test_jumeaux_couverture_identite_des_plans():
    """m-3 : mêmes effectifs, plans échangés — refusé ; lot honnête sans empreinte — refusé ; cas sain accepté."""
    s = sep()
    tous = plans(s.ouvertes)
    hc = couverture(s, laisses=tous[:20])
    assert L.lot_jumeaux_couverture(s, E, hc, tous[20:], tous[:20]).comptes["plans-deplaces"] == 44
    with pytest.raises(GardeArret, match="plans différents"):                # échange à mêmes effectifs (44, 20)
        L.lot_jumeaux_couverture(s, E, hc, tous[:2] + tous[22:], tous[2:22])
    sans_emp = L.Lot(hc.nom, hc.revision, hc.appels, hc.tables,
                     {k: v for k, v in hc.comptes.items() if k != L.EMPREINTE_DOSE_1})
    with pytest.raises(GardeArret, match="empreinte absente"):
        L.lot_jumeaux_couverture(s, E, sans_emp, tous[20:], tous[:20])
    faux = L.Lot(hc.nom, hc.revision, hc.appels, hc.tables, dict(hc.comptes, **{L.EMPREINTE_DOSE_1: "0" * 64}))
    with pytest.raises(GardeArret):
        L.lot_jumeaux_couverture(s, E, faux, tous[20:], tous[:20])
    assert hc.comptes[L.EMPREINTE_DOSE_1] == L._sha({"plans-deplaces-dose-1": [list(x) for x in tous[20:]],
                                                     "laisses-honnetes-dose-1": [list(x) for x in tous[:20]]})


def test_taches_sans_plan_comptees():
    """m-4 : une tâche ouverte sans aucun plan (815), ou sans aucun plan déplacé (822), est comptée."""
    s = sep()
    tous = plans(s.ouvertes)
    t1, t2 = s.ouvertes[1], s.ouvertes[2]
    sans = [p for p in tous if p[0] == t1] + [(s.ouvertes[3], 0)]
    laisses = [p for p in tous if p[0] == t2]
    hc = couverture(s, sans=sans, laisses=laisses)
    assert hc.comptes["taches-sans-plan"] == 1 and hc.comptes["episodes-sans-plan"] == 9
    lh = sorted(set(sans) | set(laisses))
    jc = L.lot_jumeaux_couverture(s, E, hc, [p for p in tous if p not in lh], lh)
    assert jc.comptes["taches-sans-plan-deplace"] == 2
    assert couverture(s).comptes["taches-sans-plan"] == 0
    hc = couverture(s, sans=[p for p in tous if p[0] in s.ouvertes[:4]])     # au plancher : 4 tâches sans plan
    assert hc.comptes["taches-sans-plan"] == 4
