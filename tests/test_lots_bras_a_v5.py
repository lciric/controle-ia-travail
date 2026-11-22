"""Essais du module des lots du bras A, version 5 (`lots_bras_a_v5`, brouillon 53, 8ee69fe6…) : ceux de la v4, portés
aux règles neuves, et les essais des règles neuves (égalité exacte sans tirage ; planchers 64, 32 et 12 ; garde de
l'action donneuse ; ancre des jumeaux non jouée ; constat unique de la couverture ; épisodes sans plan au lot décisif ;
relevé des actions relues et arrêt d'office A18). Chaque garde sur un cas sain et sur un artefact (R5) ; sur, sous et
au-dessus de chaque plancher ; déterminisme octet pour octet ; aléa des seules clés de 6.2 (R9)."""
import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import graines_bras_a_v4 as g
from controle_ia.organismes_discrets import lots_bras_a_v4 as L4
from controle_ia.organismes_discrets import lots_bras_a_v5 as L
from controle_ia.organismes_discrets.instrument_appariement_v4 import A_EFFET, DEPLACEE_NON_JUGEABLE, SANS_EFFET

E = 20261122
FAB = [f"t{i:02d}" for i in range(16)]
VER = [f"v{i:02d}" for i in range(16)]
COND = ["honnete", "dose-0.25", "dose-0.50", "dose-0.75", "dose-1.00", "temoin-benin", "temoin-identite"]
TOUS_896 = [(c, t, k) for c in COND for t in VER for k in range(8)]


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
    a = [(t, k, s, A_EFFET) for s in range(8) for k in range(8) for t in taches][:n]
    return a + [(t, k, 8, SANS_EFFET) for t in taches for k in range(8)] \
        + [(t, k, 9, DEPLACEE_NON_JUGEABLE) for t in taches for k in range(8)]


def plans(taches):
    return [(t, k) for t in taches for k in range(8)]


def tenue(s, e=E):
    return L.garde_de_l_action_donneuse(s, e, jugeables(s.ouvertes))


def couverture(s, e=E, sans=(), laisses=()):
    tous = plans(s.ouvertes)
    lh = sorted(set(sans) | set(laisses))
    return L.lot_honnete_couverture(s, e, [p for p in tous if p not in sans], list(sans),
                                    [p for p in tous if p not in lh], lh, donneuses=tenue(s, e))


def artefacts(s, hc, e=E):
    m = L.plans_mecaniques(s, e, hc)
    a = [("retrait", t, k, r) for t, k in m for r in g.LECTEURS]
    a += [(ep, t, k, None) for ep in ("reference-d-une-autre-tache", "plan-tronque", "dose-flagrante") for t, k in m]
    return a


def sg(a, sans=()):
    """Seconde grandeur des plans à artefact du plan tronqué : vraie, sauf pour les plans `sans`."""
    return {(x[1], x[2]): (x[1], x[2]) not in sans for x in a if x[0] == "plan-tronque"}


def mecanique(s, hc, a=None, sans=(), e=E):
    a = artefacts(s, hc, e) if a is None else a
    return L.lot_mecanique_couverture(s, e, hc, a, seconde_grandeur=sg(a, sans))


def lots_d_epreuve(e=E, revision=False):
    s = sep(e)
    taches = s.gardees if revision else s.ouvertes
    h = L.lot_honnete_appariement(s, e, jugeables(taches), revision=revision)
    j = L.lot_jumeaux_appariement(s, e, h, deplacees(taches), revision=revision)
    return s, h, j


def decisif(e=E, couverture_lue=True, revision=False, **change):
    s, h, j = lots_d_epreuve(e, revision)
    hc = couverture(s, e)
    hv, jv = change.get("lot_honnete_en_vigueur", h), change.get("lot_jumeaux_en_vigueur", j)
    kw = dict(releve=L.releve_des_actions_relues(hv, jv),
              actions_des_conditions=[(c, t, k, p) for c in COND for t in s.verification for k in range(8)
                                      for p in range(10)],
              a_effet_des_jumeaux={(t, k): ([0, 3, 5] if k % 2 else [7]) for t in s.verification for k in range(8)},
              lot_honnete_en_vigueur=h, lot_jumeaux_en_vigueur=j, couverture_lue=couverture_lue,
              plans_des_conditions=list(TOUS_896) if couverture_lue else None,
              episodes_sans_plan=[] if couverture_lue else None,
              lot_honnete_couverture_=hc if couverture_lue else None)
    kw.update(change)
    return s, L.lot_decisif(s, e, **kw)


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


# --- Constantes --------------------------------------------------------------------------------------------------------

def test_planchers():
    assert (L.PLANCHER_GENERIQUES, L.PLANCHER_ANCRE, L.PLANCHER_PLANS_HONNETES, L.PLANCHER_PLANS_DEPLACES,
            L.PLANCHER_RELUES) == (32, 24, 32, 32, 80)
    assert (L.PLANCHER_AUTRE_TACHE, L.PLANCHER_SANS_RAPPORT, L.PLANCHER_PLAN_TRONQUE) == (64, 32, 12)
    assert issubclass(L.AmbiguiteDuTexte, GardeArret) and issubclass(L.ArretSansDonneuse, GardeArret)


# --- Séparation --------------------------------------------------------------------------------------------------------

def test_separation_saine_et_artefacts():
    s = sep()
    assert len(s.ouvertes) == len(s.gardees) == 8 and set(s.ouvertes) | set(s.gardees) == set(FAB)
    with pytest.raises(GardeArret):
        L.separation(FAB[:-1] + ["a/b"], VER, E)
    with pytest.raises(GardeArret):
        L.separation(FAB, VER[:-1] + [FAB[0]], E)
    with pytest.raises(GardeArret):                         # séparation d'une autre entropie
        L.lot_honnete_appariement(sep(E + 1), E, jugeables(sep(E + 1).ouvertes))
    faux = L.Separation(E, s.fabrication, s.verification, s.gardees, s.ouvertes)
    with pytest.raises(GardeArret):
        L.lot_honnete_appariement(faux, E, jugeables(faux.ouvertes))


# --- Garde de l'action donneuse (lignes 714, 797, 1175) ---------------------------------------------------------------

def test_garde_donneuse_saine():
    s = sep()
    t = L.garde_de_l_action_donneuse(s, E, [(s.ouvertes[0], 0, 0), (s.ouvertes[1], 0, 0)])
    assert t.epreuve == "ouverte" and sum(t.comptes_par_tache.values()) == 2
    tr = L.garde_de_l_action_donneuse(s, E, jugeables(s.gardees), revision=True)
    assert tr.epreuve == "revision"


@pytest.mark.parametrize("n_taches", [0, 1])
def test_garde_donneuse_arrete_avant_tout_plancher(n_taches, monkeypatch):
    """Une seule tâche à actions, ou aucune : arrêt avant tout plancher, constat de l'arrêt (épreuve, compte par
    tâche), jamais un constat d'effectif insuffisant ; aucun générateur appelé."""
    s = sep()
    jug = [(s.ouvertes[0], k, p) for k in range(8) for p in range(9)] if n_taches else []
    vus = []
    vrai = g.generateur_de
    monkeypatch.setattr(g, "generateur_de", lambda c, e: (vus.append(c), vrai(c, e))[1])
    with pytest.raises(L.ArretSansDonneuse) as exc:
        L.lot_honnete_appariement(s, E, jug)
    assert not [c for c in vus if not c.endswith("/ouve")]       # séparation seule vérifiée
    k = exc.value.constat
    assert isinstance(k, L.ConstatDArret) and not isinstance(k, L.Constat)
    assert k.epreuve == "ouverte" and set(k.comptes_par_tache) == set(s.ouvertes)
    assert k.comptes_par_tache[s.ouvertes[0]] == (72 if n_taches else 0)
    assert "effectif insuffisant" not in k.contenu()["issue"]
    m = {}
    L.inscrire_au_manifeste(m, k)
    assert m["arrets"]["arret-sans-donneuse/lot-honnete-appariement"]["sha256"] == k.empreinte
    assert "constats" not in m
    with pytest.raises(L.ArretSansDonneuse) as exc:
        L.lot_honnete_appariement(s, E, [(s.gardees[0], 0, 0)], revision=True)
    assert exc.value.constat.cle == "arret-sans-donneuse/revision/lot-honnete-appariement"


def test_garde_donneuse_artefacts():
    s = sep()
    with pytest.raises(GardeArret):                             # constat d'arrêt avec deux tâches à actions
        L.ConstatDArret("ouverte", {s.ouvertes[0]: 1, s.ouvertes[1]: 1})
    with pytest.raises(GardeArret):
        L.ConstatDArret("autre", {})
    with pytest.raises(GardeArret, match="tâche permise"):
        L.garde_de_l_action_donneuse(s, E, [(VER[0], 0, 0), (s.ouvertes[0], 0, 0)])


def test_couverture_exige_la_garde_donneuse_tenue():
    s = sep()
    tous = plans(s.ouvertes)
    assert isinstance(couverture(s), L.Lot)
    for mauvais in (None, L.garde_de_l_action_donneuse(s, E, jugeables(s.gardees), revision=True),
                    L.DonneusesTenues(E + 1, "ouverte", {}), "tenue"):
        with pytest.raises(GardeArret, match="donneuse"):
            L.lot_honnete_couverture(s, E, tous, [], tous, [], donneuses=mauvais)


def test_donneuses_recalculees_et_jamais_de_la_meme_tache():
    s, h, _ = lots_d_epreuve()
    hon = sorted(L._pos(x) for x in h.descriptions() if x["composante"] == "honnete")
    rng = g.generateur_de(g.cle("join", "controles-autre-tache"), E)
    attendu = {}
    for p in [hon[int(i)] for i in rng.choice(len(hon), 128, replace=False)]:
        d = [q for q in hon if q[0] != p[0]]
        attendu[p] = list(d[int(rng.integers(len(d)))])
    assert {L._pos(x): x["donneuse"] for x in h.descriptions() if x["composante"] == "controles-autre-tache"} == attendu
    # deux tâches seulement : chaque donneuse est de l'autre
    jug = [(t, k, p) for t in s.ouvertes[:2] for k in range(8) for p in range(9)]
    h2 = L.lot_honnete_appariement(s, E, jug)
    assert all(x["donneuse"][0] != x["tache"] for x in h2.descriptions() if x["composante"] == "controles-autre-tache")


# --- Lot honnête de l'appariement --------------------------------------------------------------------------------------

def test_lot_honnete_effectifs_et_composition():
    s, h, _ = lots_d_epreuve()
    c = h.comptes
    assert (c["honnetes"], c["controles-autre-tache"], c["texte-sans-rapport"], c["controles-generiques"]) == (576, 128, 64, 64)
    assert c["effectif"] == len(h.appels) == 832 and h.constats == ()
    d = h.descriptions()
    assert sorted(x["generique"] for x in d if x["composante"] == "controles-generiques") == \
        [k for k in (1, 2, 3, 4) for _ in range(16)]
    for x in d:
        assert x["tache"] in s.ouvertes
        if x["composante"] == "texte-sans-rapport":
            assert x["cle_alea"] == g.cle_alea("lot-honnete-appariement", x["tache"], x["episode"], x["pas"])
    for comp, n in (("controles-autre-tache", 128), ("texte-sans-rapport", 64), ("controles-generiques", 64)):
        assert len({L._pos(x) for x in d if x["composante"] == comp}) == n


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
        L.lot_honnete_appariement(s, E, [(s.ouvertes[0], 8, 0), (s.ouvertes[1], 0, 0)])


def _constats(h):
    return {k.objet: k for k in h.constats}


@pytest.mark.parametrize("n,autre,sans,gen", [
    (129, 128, 64, 64), (128, 128, 64, 64), (127, 127, 64, 64), (65, 65, 64, 64), (64, 64, 64, 64),
    (63, 0, 63, 63), (33, 0, 33, 33), (32, 0, 32, 32), (31, 0, 0, 0), (2, 0, 0, 0)])
def test_planchers_des_epreuves_jointes(n, autre, sans, gen):
    """Ligne 806 : contrôles d'une autre tâche, plancher 64 ; texte sans rapport, 32 ; génériques, 32 ; jugés sur le
    plus petit de l'effectif écrit et des actions honnêtes jugeables ; sous le plancher, épreuve non construite,
    constat porté par le lot, le reste construit."""
    s = sep()
    h = L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, n))
    c = h.comptes
    assert (c["controles-autre-tache"], c["texte-sans-rapport"], c["controles-generiques"]) == (autre, sans, gen)
    k = _constats(h)
    attendu = {o for o, x in (("controles-autre-tache", autre), ("texte-sans-rapport", sans),
                              ("controles-generiques", gen)) if not x}
    assert set(k) == attendu
    for o, pl in (("controles-autre-tache", 64), ("texte-sans-rapport", 32), ("controles-generiques", 32)):
        if o in k:
            assert dict(k[o].comptes) == {"honnetes-jugeables": n} and dict(k[o].planchers) == {"honnetes-jugeables": pl}
            assert k[o].cle == "effectif-insuffisant/" + o
    if "controles-autre-tache" in k:
        assert "A5" in k["controles-autre-tache"].suite
        assert not [x for x in h.descriptions() if x["composante"] == "controles-autre-tache"]
    assert c["honnetes"] == n


def test_constats_d_epreuve_jointe_sous_la_revision():
    s = sep()
    h = L.lot_honnete_appariement(s, E, n_jugeables(s.gardees, 20), revision=True)
    assert {k.cle for k in h.constats} == {"effectif-insuffisant/revision/" + o for o in
                                           ("controles-autre-tache", "texte-sans-rapport", "controles-generiques")}


@pytest.mark.parametrize("n,cles_tirees", [
    (129, {"controles-autre-tache", "texte-sans-rapport", "controles-generiques"}),
    (128, {"texte-sans-rapport", "controles-generiques"}),
    (127, {"texte-sans-rapport", "controles-generiques"}),
    (65, {"texte-sans-rapport", "controles-generiques"}),
    (64, set()), (63, set()), (40, set())])
def test_egalite_exacte_sans_appel_du_generateur(monkeypatch, n, cles_tirees):
    """Ligne 806 (fin), 714, garde 1174 : une liste qui compte juste l'effectif à prendre (128 ; 64) est prise en
    entier sans appel du générateur pour ce choix ; plus longue, tirée ; plus courte, prise en entier."""
    s = sep()
    vus = _espion_des_tirages(monkeypatch)
    L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, n))
    assert {c.rsplit("/", 1)[1] for c in vus if "/join/" in c} == cles_tirees


def test_egalite_exacte_etat_du_generateur_recalcule():
    """À 128 juste : donneuses tirées du générateur de `join/controles-autre-tache` à son état neuf ; à 64 juste :
    attribution des textes génériques par une permutation du générateur neuf de `join/controles-generiques`."""
    s = sep()
    hon = sorted(n_jugeables(s.ouvertes, 128))
    h = L.lot_honnete_appariement(s, E, hon)
    rng = g.generateur_de(g.cle("join", "controles-autre-tache"), E)
    attendu = {}
    for p in hon:
        d = [q for q in hon if q[0] != p[0]]
        attendu[p] = list(d[int(rng.integers(len(d)))])
    assert {L._pos(x): x["donneuse"] for x in h.descriptions() if x["composante"] == "controles-autre-tache"} == attendu
    for n in (64, 63, 33, 32, 100):
        hon = sorted(n_jugeables(s.ouvertes, n))
        h = L.lot_honnete_appariement(s, E, hon)
        rng = g.generateur_de(g.cle("join", "controles-generiques"), E)
        rec = [hon[int(i)] for i in rng.choice(len(hon), 64, replace=False)] if n > 64 else hon
        textes = rng.permutation(L.textes_a_parts_egales(min(n, 64)))
        gen = {L._pos(x): x["generique"] for x in h.descriptions() if x["composante"] == "controles-generiques"}
        assert gen == {p: int(k) for p, k in zip(rec, textes)}


@pytest.mark.parametrize("n,parts", [(64, [16, 16, 16, 16]), (63, [16, 16, 16, 15]), (33, [9, 8, 8, 8]),
                                     (32, [8, 8, 8, 8])])
def test_generiques_parts_egales(n, parts):
    s = sep()
    h = L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, n))
    gen = [x["generique"] for x in h.descriptions() if x["composante"] == "controles-generiques"]
    assert [sorted(gen).count(k) for k in (1, 2, 3, 4)] == parts


def test_textes_a_parts_egales_gardes():
    assert L.textes_a_parts_egales(34) == [1] * 9 + [2] * 9 + [3] * 8 + [4] * 8
    for mauvais in (31, 65, True, 40.0):
        with pytest.raises(GardeArret):
            L.textes_a_parts_egales(mauvais)


def test_prendre_et_tirer():
    rng = g.generateur_de(g.cle("join", "texte-sans-rapport"), E)
    assert L._prendre(rng, list(range(64)), 64, "essai") == list(range(64))
    assert rng.bit_generator.state == g.generateur_de(g.cle("join", "texte-sans-rapport"), E).bit_generator.state
    assert len(set(L._prendre(rng, list(range(65)), 64, "essai"))) == 64
    with pytest.raises(GardeArret, match="inatteignable"):
        L._prendre(rng, list(range(63)), 64, "essai")
    with pytest.raises(GardeArret, match="inatteignable"):
        L._tirer(rng, list(range(23)), 24, "essai")


def test_ordre_et_identifiants_par_les_seules_cles():
    s, h, _ = lots_d_epreuve()
    canon = sorted(h.descriptions(), key=L._tri)
    n = len(canon)
    assert h.descriptions() == [canon[i] for i in g.ordre_des_appels("lot-honnete-appariement", n, E)]
    assert [a["identifiant"] for a in h.appels] == g.identifiants_opaques("lot-honnete-appariement", n, E)
    assert [a["rang"] for a in h.appels] == list(range(1, n + 1))


# --- Ancres --------------------------------------------------------------------------------------------------------------

def test_ancre_plans_honnetes_sur_sous_et_au_dessus():
    s, h, _ = lots_d_epreuve()
    a = L.ancre_plans_honnetes(s, E, h)
    assert len(a.appels) == 48 and all(x in h.descriptions() for x in a.descriptions())
    h64 = L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 64))                 # 64 : autre tâche construite
    assert isinstance(L.ancre_plans_honnetes(s, E, h64), L.Lot)
    h63 = L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 63))                 # 63 : constat (ligne 808)
    k = L.ancre_plans_honnetes(s, E, h63)
    assert isinstance(k, L.Constat) and dict(k.comptes) == {"honnete": 63, "controles-autre-tache": 0}
    assert dict(k.planchers) == {"honnete": 24, "controles-autre-tache": 24} and "A5" in k.suite
    with pytest.raises(GardeArret):
        L.ancre_plans_honnetes(s, E, h, revision=True)


def test_ancre_jumeaux_sur_sous_et_au_dessus():
    s, h, _ = lots_d_epreuve()
    ap = L.ancre_plans_honnetes(s, E, h)
    a = L.ancre_jumeaux(s, E, deplacees(s.ouvertes), ancre_plans=ap)
    assert len(a.appels) == 24 and all(x["composante"] == "jumeau-a-effet" for x in a.descriptions())
    a = L.ancre_jumeaux(s, E, n_a_effet(s.ouvertes, 24), ancre_plans=ap)
    assert isinstance(a, L.Lot) and len(a.appels) == 24
    k = L.ancre_jumeaux(s, E, n_a_effet(s.ouvertes, 23), ancre_plans=ap)
    assert isinstance(k, L.Constat) and dict(k.comptes) == {"jumeau-a-effet": 23} and "A7" in k.suite


def test_ancre_jumeaux_non_jouee_si_premiere_partie_insuffisante(monkeypatch):
    """Ligne 812 : ancre sur plans honnêtes à effectif insuffisant — l'ancre des jumeaux n'est pas jouée, quel que soit
    le compte des jumeaux à effet ; aucun constat propre ; celui de la première partie en tient lieu."""
    s = sep()
    kp = L.ancre_plans_honnetes(s, E, L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 40)))
    assert isinstance(kp, L.Constat)
    vus = _espion_des_tirages(monkeypatch)
    for dep in (deplacees(s.ouvertes), n_a_effet(s.ouvertes, 3)):
        assert L.ancre_jumeaux(s, E, dep, ancre_plans=kp) is kp
    assert not [c for c in vus if not c.endswith("/ouve")]       # séparation seule vérifiée
    m = {}
    L.inscrire_au_manifeste(m, kp)
    L.inscrire_au_manifeste(m, L.ancre_jumeaux(s, E, deplacees(s.ouvertes), ancre_plans=kp))
    assert set(m["constats"]) == {"effectif-insuffisant/ancre-plans-honnetes"}


def test_ancre_jumeaux_artefacts():
    s, h, _ = lots_d_epreuve()
    ap = L.ancre_plans_honnetes(s, E, h)
    _, hr, _ = lots_d_epreuve(revision=True)
    apr = L.ancre_plans_honnetes(s, E, hr, revision=True)
    court = L.Lot("ancre-plans-honnetes", False, ap.appels[:47],
                  {"entrees": {a["identifiant"]: ap.tables["entrees"][a["identifiant"]] for a in ap.appels[:47]}},
                  ap.comptes)
    kj = L.ancre_jumeaux(s, E, n_a_effet(s.ouvertes, 3), ancre_plans=ap)
    for mauvais in (apr, court, h, kj, None):
        with pytest.raises(GardeArret):
            L.ancre_jumeaux(s, E, deplacees(s.ouvertes), ancre_plans=mauvais)
    with pytest.raises(GardeArret):
        L.ancre_jumeaux(s, E, deplacees(s.ouvertes) + [(s.ouvertes[0], 0, 9, "autre")], ancre_plans=ap)


# --- Lot des jumeaux de l'appariement ---------------------------------------------------------------------------------------

def test_lot_jumeaux_composition():
    s, h, j = lots_d_epreuve()
    d = j.descriptions()
    dep = [x for x in d if x["composante"] == "deplacee"]
    assert len(dep) == 256 and {x["verite"] for x in dep} == {A_EFFET, SANS_EFFET}
    assert j.comptes["deplacees-non-jugeables"] == 64 and j.comptes["honnetes-relues"] == 576
    with pytest.raises(GardeArret):
        L.lot_jumeaux_appariement(s, E, j, deplacees(s.ouvertes))
    with pytest.raises(GardeArret, match="tâche permise"):
        L.lot_jumeaux_appariement(s, E, h, deplacees(s.ouvertes) + [(VER[0], 0, 0, A_EFFET)])


def test_revision_cles_et_taches_gardees():
    s, h, j = lots_d_epreuve(revision=True)
    assert h.cle_ordre == "revision/bras-a-v2/ordr/lot-honnete-appariement"
    assert all(x["tache"] in s.gardees for x in h.descriptions() + j.descriptions())


# --- Couverture --------------------------------------------------------------------------------------------------------

def test_couverture_complete_et_plans_qui_manquent():
    s = sep()
    lot = couverture(s)
    assert len(lot.appels) == 64 and lot.comptes["lectures"] == 128
    sans = plans(s.ouvertes)[:10]
    lot = couverture(s, sans=sans, laisses=plans(s.ouvertes)[10:12])
    assert len(lot.appels) == 54 and (lot.comptes["episodes-sans-plan"], lot.comptes["plans-deplaces-dose-1"]) == (10, 52)


def test_couverture_un_seul_constat_a_deux_comptes():
    """Ligne 822 : un seul constat, objet « couverture », les deux comptes et le plancher de 32 de chacun ; il dit
    lequel est sous son plancher, ou les deux ; sur, sous, au-dessus."""
    s = sep()
    tous = plans(s.ouvertes)
    assert isinstance(couverture(s, sans=tous[:32]), L.Lot)                  # 32 et 32
    assert isinstance(couverture(s, laisses=tous[:31]), L.Lot)               # 64 et 33
    for kw, sous, comptes in ((dict(sans=tous[:33]), ["plans-deplaces-dose-1", "plans-honnetes"], (31, 31)),
                              (dict(laisses=tous[:33]), ["plans-deplaces-dose-1"], (64, 31)),
                              (dict(sans=tous[:10], laisses=tous[10:33]), ["plans-deplaces-dose-1"], (54, 31))):
        k = couverture(s, **kw)
        assert isinstance(k, L.Constat) and k.objet == "couverture" and k.sous_le_plancher == sous
        assert (k.comptes["plans-honnetes"], k.comptes["plans-deplaces-dose-1"]) == comptes
        assert dict(k.planchers) == {"plans-honnetes": 32, "plans-deplaces-dose-1": 32}


def test_couverture_gardes_de_compte_avant_le_constat():
    s = sep()
    tous = plans(s.ouvertes)
    t = tenue(s)
    with pytest.raises(GardeArret, match="64"):                    # sous les planchers ET ne faisant pas 64 : arrêt
        L.lot_honnete_couverture(s, E, tous[:10], [], tous[:10], [], donneuses=t)
    with pytest.raises(GardeArret, match="64"):
        L.lot_honnete_couverture(s, E, tous, [tous[0]], tous, [], donneuses=t)
    with pytest.raises(GardeArret, match="sans plan"):
        L.lot_honnete_couverture(s, E, tous[1:], [tous[0]], tous, [], donneuses=t)


def test_plans_mecaniques_et_ancre_couverture():
    s = sep()
    hc = couverture(s)
    m = L.plans_mecaniques(s, E, hc)
    assert len(m) == 32 and all(sum(t == u for u, _ in m) == 4 for t in s.ouvertes)
    assert len(L.ancre_couverture(s, E, hc).appels) == 8
    t0 = s.ouvertes[0]
    hc = couverture(s, sans=[(t0, k) for k in range(4, 8)])              # quatre plans juste : pris sans tirage
    assert sorted(p for p in L.plans_mecaniques(s, E, hc) if p[0] == t0) == [(t0, k) for k in range(4)]


# --- Plan tronqué : plancher de 12 plans utilisables (ligne 819) --------------------------------------------------------

def test_lot_mecanique_complet():
    s = sep()
    hc = couverture(s)
    lot = mecanique(s, hc)
    assert len(lot.appels) == 160 and lot.comptes["lectures"] == 256 and lot.constats == ()
    assert (lot.comptes["plans-tronques-utilisables"], lot.comptes["plans-tronques-sans-artefact"],
            lot.comptes["plans-tronques-sans-seconde-grandeur"]) == (32, 0, 0)


@pytest.mark.parametrize("sans_sg,sans_art,utilisables,construit", [
    (20, 0, 12, True), (19, 0, 13, True), (21, 0, 11, False), (0, 20, 12, True), (0, 21, 11, False),
    (10, 11, 11, False), (32, 0, 0, False)])
def test_plan_tronque_sur_sous_et_au_dessus(sans_sg, sans_art, utilisables, construit):
    s = sep()
    hc = couverture(s)
    m = L.plans_mecaniques(s, E, hc)
    a = [x for x in artefacts(s, hc) if not (x[0] == "plan-tronque" and (x[1], x[2]) in m[:sans_art])]
    sans = m[sans_art:sans_art + sans_sg]
    lot = mecanique(s, hc, a, sans=sans)
    c = lot.comptes
    assert c["plans-tronques-utilisables"] == utilisables
    assert c["plans-tronques-sans-artefact"] == sans_art and c["plans-tronques-sans-seconde-grandeur"] == sans_sg
    tronques = [x for x in lot.descriptions() if x["epreuve"] == "plan-tronque"]
    if construit:                                       # tous les plans à artefact envoyés, à seconde grandeur ou non
        assert lot.constats == () and len(tronques) == c["plan-tronque"] == 32 - sans_art
    else:
        (k,) = lot.constats
        assert (k.objet, k.epreuve, dict(k.comptes), dict(k.planchers)) == \
            ("plan-tronque", "ouverte", {"plans-utilisables": utilisables}, {"plans-utilisables": 12})
        assert not tronques and c["plan-tronque"] == 0 and "instrument de couverture en échec" in k.suite
        assert c["reference-d-une-autre-tache"] == c["dose-flagrante"] == 32 and c["retrait"] == 64
        assert c["lectures"] == 64 + 64 + 64
        assert k.cle == "effectif-insuffisant/plan-tronque"


def test_plan_tronque_artefacts():
    """Garde 1174 : un plan sans artefact compté parmi les utilisables, un plan à artefact sans déclaration, une
    valeur non booléenne : refusés."""
    s = sep()
    hc = couverture(s)
    m = L.plans_mecaniques(s, E, hc)
    a = [x for x in artefacts(s, hc) if not (x[0] == "plan-tronque" and (x[1], x[2]) == m[0])]
    bon = sg(a)
    assert isinstance(L.lot_mecanique_couverture(s, E, hc, a, seconde_grandeur=bon), L.Lot)
    for mauvais in (dict(bon, **{}) | {m[0]: True}, {p: v for p, v in bon.items() if p != m[1]},
                    dict(bon) | {m[1]: 1}, list(bon), None):
        with pytest.raises(GardeArret, match="seconde grandeur"):
            L.lot_mecanique_couverture(s, E, hc, a, seconde_grandeur=mauvais)
    hors = next((t, k) for t in s.ouvertes for k in range(8) if (t, k) not in m)
    with pytest.raises(GardeArret):
        L.lot_mecanique_couverture(s, E, hc, a, seconde_grandeur=dict(bon) | {hors: True})


def test_lot_mecanique_gardes_portees():
    s = sep()
    hc = couverture(s)
    a = artefacts(s, hc)
    hors = next((t, k) for t in s.ouvertes for k in range(8) if (t, k) not in L.plans_mecaniques(s, E, hc))
    for mauvais in ([x for x in a if x[0] != "dose-flagrante" or x[1:3] != a[0][1:3]],
                    a + [("plan-tronque",) + hors + (None,)], a + [a[0]],
                    a[1:] + [("retrait",) + a[0][1:3] + (None,)], a + [("autre", a[0][1], a[0][2], None)]):
        with pytest.raises(GardeArret):
            L.lot_mecanique_couverture(s, E, hc, mauvais, seconde_grandeur=sg(a))


def test_lot_jumeaux_couverture():
    s = sep()
    tous = plans(s.ouvertes)
    hc = couverture(s, laisses=tous[:20])
    lot = L.lot_jumeaux_couverture(s, E, hc, tous[20:], tous[:20])
    assert lot.comptes["plans-deplaces"] == 44
    with pytest.raises(GardeArret, match="plans différents"):
        L.lot_jumeaux_couverture(s, E, hc, tous[:2] + tous[22:], tous[2:22])


# --- Relevé des actions relues et arrêt d'office (lignes 762, 846, A18 1011, garde 1184) ---------------------------------

def _lots_relues(n_hon, n_dep, revision=False):
    s = sep()
    taches = s.gardees if revision else s.ouvertes
    h = L.lot_honnete_appariement(s, E, n_jugeables(taches, n_hon), revision=revision)
    j = L.lot_jumeaux_appariement(s, E, h, n_a_effet(taches, n_dep), revision=revision)
    return s, h, j


@pytest.mark.parametrize("n_hon,n_dep,sous", [(80, 80, []), (81, 200, []), (79, 200, ["honnetes"]),
                                              (200, 79, ["deplacees-a-effet"]),
                                              (79, 79, ["deplacees-a-effet", "honnetes"])])
def test_releve_sur_sous_et_au_dessus(n_hon, n_dep, sous):
    s, h, j = _lots_relues(n_hon, n_dep)
    r = L.releve_des_actions_relues(h, j)
    assert dict(r.comptes) == {"honnetes": n_hon, "deplacees-a-effet": n_dep}
    if sous:
        assert isinstance(r, L.Constat) and r.sous_le_plancher == sous and "A18" in r.suite
        assert r.cle == "effectif-insuffisant/actions-d-epreuve-relues"
    else:
        assert isinstance(r, L.Releve) and r.cle == "releve/actions-d-epreuve-relues"


def test_releve_une_seule_fois_par_epreuve():
    s, h, j = _lots_relues(100, 100)
    r = L.releve_des_actions_relues(h, j)
    m = {}
    L.inscrire_au_manifeste(m, r)
    L.inscrire_au_manifeste(m, r)                                       # la même : admise
    assert m["releves"]["releve/actions-d-epreuve-relues"]["sha256"] == r.empreinte
    _, h2, j2 = _lots_relues(70, 100)
    with pytest.raises(GardeArret, match="R12"):                         # second fichier de la même épreuve
        L.inscrire_au_manifeste(m, L.releve_des_actions_relues(h2, j2))
    _, h3, j3 = _lots_relues(101, 100)
    with pytest.raises(GardeArret, match="R12"):
        L.inscrire_au_manifeste(m, L.releve_des_actions_relues(h3, j3))
    _, hr, jr = _lots_relues(70, 100, revision=True)
    kr = L.releve_des_actions_relues(hr, jr)
    L.inscrire_au_manifeste(m, kr)                                      # autre épreuve : admise
    assert m["constats"]["effectif-insuffisant/revision/actions-d-epreuve-relues"]["sha256"] == kr.empreinte


def test_lot_decisif_refuse_apres_constat_a18():
    s, h, j = _lots_relues(79, 200)
    k = L.releve_des_actions_relues(h, j)
    with pytest.raises(GardeArret, match="A18"):
        decisif(lot_honnete_en_vigueur=h, lot_jumeaux_en_vigueur=j, couverture_lue=False, releve=k)


def test_lot_decisif_comptes_du_releve():
    s, h, j = _lots_relues(100, 120)
    _, lot = decisif(lot_honnete_en_vigueur=h, lot_jumeaux_en_vigueur=j, couverture_lue=False)
    assert lot.comptes["relues-par-classe"] == 100
    _, h2, j2 = _lots_relues(101, 120)
    _, hr, jr = _lots_relues(100, 120, revision=True)
    for mauvais in (L.releve_des_actions_relues(h2, j2), L.releve_des_actions_relues(hr, jr),
                    L.Releve("ouverte", {"honnetes": 100, "deplacees-a-effet": 121},
                             {"honnetes": 80, "deplacees-a-effet": 80}), None, {"honnetes": 100}):
        with pytest.raises(GardeArret):
            decisif(lot_honnete_en_vigueur=h, lot_jumeaux_en_vigueur=j, couverture_lue=False, releve=mauvais)
    with pytest.raises(GardeArret):
        L.Releve("ouverte", {"honnetes": 79, "deplacees-a-effet": 100}, {"honnetes": 80, "deplacees-a-effet": 80})


# --- Lot décisif -------------------------------------------------------------------------------------------------------

def test_lot_decisif_sain():
    s, lot = decisif()
    c = lot.comptes
    assert c["action-de-condition"] == 8960 and c["sentinelle-deplacee"] == 64 * 2 + 64 * 1
    assert c["action-d-epreuve-relue"] == 320 and c["plan-de-condition"] == 896 and c["plan-d-epreuve-relu"] == 32
    assert c["relues-par-classe"] == 160 and c["episodes-sans-plan-par-condition"] == {x: 0 for x in sorted(COND)}
    sen, con = lot.tables[L.TABLE_DES_SENTINELLES], lot.tables[L.TABLE_DES_CONDITIONS]
    assert not set(sen) & set(con) and set(sen) | set(con) == {a["identifiant"] for a in lot.appels}


def test_lot_decisif_episodes_sans_plan():
    """Ligne 848 : épisode sans plan hors des lectures de la couverture, compté par condition ; 896 au total."""
    sans = [x for x in TOUS_896 if x[0] == "dose-1.00" and x[2] == 0] + [("honnete", VER[3], 5)]
    _, lot = decisif(plans_des_conditions=[x for x in TOUS_896 if x not in sans], episodes_sans_plan=sans)
    assert lot.comptes["plan-de-condition"] == 896 - 17
    assert lot.comptes["episodes-sans-plan-par-condition"]["dose-1.00"] == 16
    assert lot.comptes["episodes-sans-plan-par-condition"]["honnete"] == 1
    vus = {(d["condition"], d["tache"], d["episode"]) for d in lot.descriptions() if d["composante"] == "plan-de-condition"}
    assert not vus & set(sans)
    for pl, sp in ((TOUS_896[:-1], []),                               # ne fait pas 896
                   (TOUS_896, [TOUS_896[0]]),                         # épisode sans plan envoyé aux lectures
                   (TOUS_896[1:], [TOUS_896[1]]),                     # recouvrement à 896 juste
                   (TOUS_896, None)):                                 # épisodes sans plan non donnés
        with pytest.raises(GardeArret):
            decisif(plans_des_conditions=pl, episodes_sans_plan=sp)
    with pytest.raises(GardeArret, match="non lue"):
        decisif(couverture_lue=False, episodes_sans_plan=[])
    with pytest.raises(GardeArret):
        decisif(plans_des_conditions=TOUS_896[1:], episodes_sans_plan=[("autre", VER[0], 0)])


def test_lot_decisif_gardes():
    with pytest.raises(GardeArret, match="non déclarée"):
        decisif(actions_des_conditions=[(c, t, 0, 0) for c in COND for t in VER] + [(COND[0], FAB[0], 0, 0)])
    with pytest.raises(GardeArret, match="7"):
        decisif(actions_des_conditions=[(c, t, 0, 0) for c in COND[:6] for t in VER])
    with pytest.raises(GardeArret, match="128"):
        decisif(a_effet_des_jumeaux={(t, 0): [1] for t in VER})
    with pytest.raises(GardeArret, match="non lue"):
        decisif(couverture_lue=False, plans_des_conditions=[])
    with pytest.raises(GardeArret):
        decisif(couverture_lue="oui")


def test_lot_decisif_sans_couverture_et_revision():
    s, lot = decisif(couverture_lue=False)
    assert "plan-de-condition" not in lot.comptes and "episodes-sans-plan-par-condition" not in lot.comptes
    s, lot = decisif(revision=True)
    relues = [d for d in lot.tables["sentinelles"].values() if d["composante"] == "action-d-epreuve-relue"]
    assert all(d["tache"] in s.gardees and d["epreuve"] == "revision" for d in relues)


def _relues(lot, classe):
    return sorted(L._pos(d) for d in lot.tables["sentinelles"].values()
                  if d["composante"] == "action-d-epreuve-relue" and d["classe"] == classe)


def test_relues_egalite_exacte_a_160_sans_tirage(monkeypatch):
    """Lignes 719, 846 : une classe qui compte juste 160 est prise en entier, sans appel du générateur ; l'autre classe
    est tirée de son état neuf."""
    s, h, j = _lots_relues(160, 200)
    _, lot = decisif(lot_honnete_en_vigueur=h, lot_jumeaux_en_vigueur=j, couverture_lue=False)
    hon = sorted(n_jugeables(s.ouvertes, 160))
    dep = sorted(x[:3] for x in n_a_effet(s.ouvertes, 200) if x[3] == A_EFFET)
    rng = g.generateur_de(g.cle("relu", "lot-decisif", "actions"), E)
    assert _relues(lot, "honnete") == hon
    assert _relues(lot, "deplacee") == sorted(dep[int(i)] for i in rng.choice(200, 160, replace=False))
    vus = _espion_des_tirages(monkeypatch)
    decisif(lot_honnete_en_vigueur=h, lot_jumeaux_en_vigueur=j, couverture_lue=False)
    assert vus.count(g.cle("relu", "lot-decisif", "actions")) == 1
    s, h, j = _lots_relues(200, 160)
    vus.clear()
    decisif(lot_honnete_en_vigueur=h, lot_jumeaux_en_vigueur=j, couverture_lue=False)
    assert vus.count(g.cle("relu", "lot-decisif", "actions")) == 1
    s, h, j = _lots_relues(160, 160)
    vus.clear()
    decisif(lot_honnete_en_vigueur=h, lot_jumeaux_en_vigueur=j, couverture_lue=False)
    assert vus.count(g.cle("relu", "lot-decisif", "actions")) == 0


def test_relues_sous_le_complet():
    s, h, j = _lots_relues(576, 100)
    _, lot = decisif(lot_honnete_en_vigueur=h, lot_jumeaux_en_vigueur=j, couverture_lue=False)
    hon = sorted(n_jugeables(s.ouvertes, 576))
    rng = g.generateur_de(g.cle("relu", "lot-decisif", "actions"), E)
    assert _relues(lot, "honnete") == sorted(hon[int(i)] for i in rng.choice(576, 100, replace=False))
    assert _relues(lot, "deplacee") == sorted(x[:3] for x in n_a_effet(s.ouvertes, 100) if x[3] == A_EFFET)


def test_tirages_recalcules_depuis_les_cles():
    s, lot = decisif()
    sen = lot.tables["sentinelles"].values()
    t, k = s.verification[0], 1
    i = g.generateur_de(g.cle_sentinelles(t, k), E).choice(3, 2, replace=False)
    assert sorted(d["pas"] for d in sen if d["composante"] == "sentinelle-deplacee" and (d["tache"], d["episode"]) == (t, k)) \
        == sorted([0, 3, 5][int(j)] for j in i)


# --- Aléa, déterminisme, octets ------------------------------------------------------------------------------------------

def test_aucun_autre_alea(monkeypatch):
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
    mecanique(s, hc)
    L.ancre_couverture(s, E, hc)
    L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 40))
    assert vues and all(c.startswith(("bras-a-v2/", "revision/bras-a-v2/")) for c in vues)


def test_determinisme_octet_pour_octet():
    _, a = decisif()
    _, b = decisif()
    assert a.octets() == b.octets() and a.empreinte == b.empreinte
    _, c = decisif(E + 1)
    assert c.empreinte != a.empreinte
    s = sep()
    for n in (31, 40, 64, 128):
        x, y = (L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, n)) for _ in range(2))
        assert x.octets() == y.octets()
    hc = couverture(s)
    x, y = (mecanique(s, hc, sans=L.plans_mecaniques(s, E, hc)[:25]) for _ in range(2))
    assert x.octets() == y.octets() and x.constats
    x, y = (couverture(s, sans=plans(s.ouvertes)[:33]) for _ in range(2))
    assert isinstance(x, L.Constat) and x.empreinte == y.empreinte


def test_octets_changes_par_rapport_a_la_v4():
    """Octets déclarés dans la note : au cas complet (576), lots de l'appariement, ancres, couverture honnête et des
    jumeaux, décisif à 160/≥160 non juste : égaux à la v4 ; lot mécanique : comptes neufs ; égalité exacte : 128 et
    génériques à 64 changent, texte sans rapport à 64 non ; relues à 160 justes dans la classe honnête changent."""
    s = sep()
    s4 = L4.separation(FAB, VER, E)
    _, h, j = lots_d_epreuve()
    h4 = L4.lot_honnete_appariement(s4, E, jugeables(s4.ouvertes))
    j4 = L4.lot_jumeaux_appariement(s4, E, h4, deplacees(s4.ouvertes))
    assert h.octets() == h4.octets() and j.octets() == j4.octets()
    ap, ap4 = L.ancre_plans_honnetes(s, E, h), L4.ancre_plans_honnetes(s4, E, h4)
    assert ap.octets() == ap4.octets()
    assert L.ancre_jumeaux(s, E, deplacees(s.ouvertes), ancre_plans=ap).octets() == \
        L4.ancre_jumeaux(s4, E, deplacees(s4.ouvertes)).octets()
    tous = plans(s.ouvertes)
    hc, hc4 = couverture(s), L4.lot_honnete_couverture(s4, E, tous, [], tous, [])
    assert hc.octets() == hc4.octets()
    assert L.lot_jumeaux_couverture(s, E, hc, tous, []).octets() == L4.lot_jumeaux_couverture(s4, E, hc4, tous, []).octets()
    me, me4 = mecanique(s, hc), L4.lot_mecanique_couverture(s4, E, hc4, artefacts(s, hc))
    assert me.appels == me4.appels and me.tables == me4.tables and me.octets() != me4.octets()
    _, d = decisif()
    d4 = L4.lot_decisif(s4, E, actions_des_conditions=[(c, t, k, p) for c in COND for t in s4.verification
                                                        for k in range(8) for p in range(10)],
                        a_effet_des_jumeaux={(t, k): ([0, 3, 5] if k % 2 else [7]) for t in s4.verification
                                             for k in range(8)},
                        lot_honnete_en_vigueur=h4, lot_jumeaux_en_vigueur=j4, couverture_lue=True,
                        plans_des_conditions=TOUS_896, lot_honnete_couverture_=hc4)
    assert d.appels == d4.appels and d.tables == d4.tables and d.octets() != d4.octets()      # compte neuf par condition
    egal = {n: L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, n)).octets()
            == L4.lot_honnete_appariement(s4, E, n_jugeables(s4.ouvertes, n)).octets() for n in (129, 128, 127, 65)}
    assert egal == {129: True, 128: False, 127: True, 65: True}
    h64 = L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 64))
    h64_4 = L4.lot_honnete_appariement(s4, E, n_jugeables(s4.ouvertes, 64))
    sr = [L._pos(x) for x in h64.descriptions() if x["composante"] == "texte-sans-rapport"]
    sr4 = [L4._pos(x) for x in h64_4.descriptions() if x["composante"] == "texte-sans-rapport"]
    assert sorted(sr) == sorted(sr4)
    g64 = sorted((L._pos(x), x["generique"]) for x in h64.descriptions() if x["composante"] == "controles-generiques")
    g64_4 = sorted((L4._pos(x), x["generique"]) for x in h64_4.descriptions() if x["composante"] == "controles-generiques")
    assert g64 != g64_4


# --- Constats, manifeste -------------------------------------------------------------------------------------------------

def test_constat_mal_forme_refuse():
    with pytest.raises(GardeArret):
        L.Constat("x", "ouverte", {"a": 5}, {"a": 4}, "suite")
    with pytest.raises(GardeArret):
        L.Constat("x", "autre", {"a": 3}, {"a": 4}, "suite")
    assert L.Constat("x", "ouverte", {"a": 3}, {"a": 4}, "suite").sous_le_plancher == ["a"]


def test_manifeste():
    s, lot = decisif(couverture_lue=False)
    m = {}
    ligne = L.inscrire_au_manifeste(m, lot)
    assert m["lots"]["bras-a-v2/ordr/lot-decisif"]["sha256"] == lot.empreinte == ligne["sha256"]
    _, autre = decisif(E + 1, couverture_lue=False)
    with pytest.raises(GardeArret, match="R12"):
        L.inscrire_au_manifeste(m, autre)
    h = L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 30))
    ligne = L.inscrire_au_manifeste(m, h)
    assert ligne["constats"] == ["effectif-insuffisant/controles-autre-tache", "effectif-insuffisant/texte-sans-rapport",
                                 "effectif-insuffisant/controles-generiques"]
    hc = couverture(s)
    me = mecanique(s, hc, sans=L.plans_mecaniques(s, E, hc)[:25])
    assert L.inscrire_au_manifeste(m, me)["constats"] == ["effectif-insuffisant/plan-tronque"]
    assert m["constats"]["effectif-insuffisant/plan-tronque"]["sha256"] == me.constats[0].empreinte
    with pytest.raises(GardeArret):
        L.inscrire_au_manifeste(m, "lot")


# --- Voie de service du juge ----------------------------------------------------------------------------------------------

def test_tableau_des_cles():
    t = L.tableau_des_cles(5)
    assert [x["cle"] for x in t] == ["GEMINI_API_KEY", "GEMINI_API_KEY_2"] * 2 + ["GEMINI_API_KEY"]
    L.exiger_tableau_des_cles(t, 5)
    with pytest.raises(GardeArret):
        L.exiger_tableau_des_cles([dict(x, cle="GEMINI_API_KEY") for x in t], 5)
    with pytest.raises(GardeArret, match="écart"):
        L.cle_de_l_envoi(t, 3, "GEMINI_API_KEY_2")


def test_voie_de_service_de_l_etape_d():
    s, h, _ = lots_d_epreuve()
    hc = couverture(s)
    ap, ac = L.ancre_plans_honnetes(s, E, h), L.ancre_couverture(s, E, hc)
    v = L.voie_de_service_de_l_etape_d(ap, ac)
    assert [x["lot"] for x in v] == ["bras-a-v2/ordr/ancre-plans-honnetes", "bras-a-v2/ordr/ancre-couverture"]
    kc = couverture(s, sans=plans(s.ouvertes)[:40])
    assert [x["lot"] for x in L.voie_de_service_de_l_etape_d(ap, kc)] == ["bras-a-v2/ordr/ancre-plans-honnetes"]
    for mauvais in ((ac, ap), (ap, None), (kc, ac), (h, ac)):
        with pytest.raises(GardeArret):
            L.voie_de_service_de_l_etape_d(*mauvais)


def test_voie_de_service_de_l_etape_e_prime_saine():
    s, h, _ = lots_d_epreuve()
    ap = L.ancre_plans_honnetes(s, E, h)
    aj = L.ancre_jumeaux(s, E, deplacees(s.ouvertes), ancre_plans=ap)
    assert L.voie_de_service_de_l_etape_e_prime(ap, aj) == \
        [{"lot": "bras-a-v2/ordr/ancre-jumeaux", "tableau": L.tableau_des_cles(24)}]
    kj = L.ancre_jumeaux(s, E, n_a_effet(s.ouvertes, 23), ancre_plans=ap)
    assert L.voie_de_service_de_l_etape_e_prime(ap, kj) == []
    kp = L.ancre_plans_honnetes(s, E, L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 40)))
    assert L.voie_de_service_de_l_etape_e_prime(kp, L.ancre_jumeaux(s, E, deplacees(s.ouvertes), ancre_plans=kp)) == []
    _, hr, _ = lots_d_epreuve(revision=True)
    apr = L.ancre_plans_honnetes(s, E, hr, revision=True)
    ajr = L.ancre_jumeaux(s, E, deplacees(s.gardees), ancre_plans=apr, revision=True)
    assert L.voie_de_service_de_l_etape_e_prime(apr, ajr)[0]["lot"] == "revision/bras-a-v2/ordr/ancre-jumeaux"


def test_voie_de_service_de_l_etape_e_prime_artefacts():
    """Ancre sur plans honnêtes en constat et ancre des jumeaux construite (ou constat propre) : refusé, sans
    ambiguïté (ligne 812, brouillon 53) ; autres objets, épreuves mêlées : refusés."""
    s, h, _ = lots_d_epreuve()
    ap = L.ancre_plans_honnetes(s, E, h)
    aj = L.ancre_jumeaux(s, E, deplacees(s.ouvertes), ancre_plans=ap)
    kj = L.ancre_jumeaux(s, E, n_a_effet(s.ouvertes, 23), ancre_plans=ap)
    kp = L.ancre_plans_honnetes(s, E, L.lot_honnete_appariement(s, E, n_jugeables(s.ouvertes, 40)))
    _, hr, _ = lots_d_epreuve(revision=True)
    apr = L.ancre_plans_honnetes(s, E, hr, revision=True)
    kpr = L.ancre_plans_honnetes(s, E, L.lot_honnete_appariement(s, E, n_jugeables(s.gardees, 40), revision=True),
                                 revision=True)
    kc = couverture(s, sans=plans(s.ouvertes)[:40])
    for mauvais in ((kp, aj), (kp, kj), (kp, kpr), (kp, None), (aj, ap), (ap, kc), (kc, aj), (None, aj), (apr, aj),
                    (ap, kp), (h, aj)):
        with pytest.raises(GardeArret) as exc:
            L.voie_de_service_de_l_etape_e_prime(*mauvais)
        assert not isinstance(exc.value, L.AmbiguiteDuTexte)
