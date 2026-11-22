"""Essais du module des lots du bras A (`lots_bras_a_v1`) : chaque garde sur un cas sain et sur un artefact (R5),
déterminisme octet pour octet, aléa des seules clés de 6.2."""
import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import graines_bras_a_v4 as g
from controle_ia.organismes_discrets import lots_bras_a_v1 as L
from controle_ia.organismes_discrets.instrument_appariement_v4 import A_EFFET, DEPLACEE_NON_JUGEABLE, SANS_EFFET

E = 20261122
FAB = [f"t{i:02d}" for i in range(16)]
VER = [f"v{i:02d}" for i in range(16)]
COND = ["honnete", "dose-0.25", "dose-0.50", "dose-0.75", "dose-1.00", "temoin-benin", "temoin-identite"]


def sep(e=E):
    return L.separation(FAB, VER, e)


def jugeables(taches):
    return [(t, k, s) for t in taches for k in range(8) for s in range(9)]          # le pas 9 n'est pas jugeable


def deplacees(taches):
    v = {0: A_EFFET, 1: A_EFFET, 2: A_EFFET, 3: SANS_EFFET, 4: DEPLACEE_NON_JUGEABLE}
    return [(t, k, s, v[s]) for t in taches for k in range(8) for s in v]


def plans(taches):
    return [(t, k) for t in taches for k in range(8)]


def artefacts(s, e=E):
    m = L.plans_mecaniques(s, e)
    a = [("retrait", t, k, r) for t, k in m for r in g.LECTEURS]
    a += [(ep, t, k, None) for ep in ("reference-d-une-autre-tache", "plan-tronque", "dose-flagrante") for t, k in m]
    return a


def lots_d_epreuve(e=E, revision=False):
    s = sep(e)
    taches = s.gardees if revision else s.ouvertes
    h = L.lot_honnete_appariement(s, e, jugeables(taches), revision=revision)
    j = L.lot_jumeaux_appariement(s, e, h, deplacees(taches), revision=revision)
    return s, h, j


def decisif(e=E, couverture=True, revision=False, **change):
    s, h, j = lots_d_epreuve(e, revision)
    hc = L.lot_honnete_couverture(s, e, plans(s.ouvertes))
    kw = dict(actions_des_conditions=[(c, t, k, p) for c in COND for t in s.verification for k in range(8)
                                      for p in range(10)],
              a_effet_des_jumeaux={(t, k): ([0, 3, 5] if k % 2 else [7]) for t in s.verification for k in range(8)},
              lot_honnete_en_vigueur=h, lot_jumeaux_en_vigueur=j, couverture_lue=couverture,
              plans_des_conditions=[(c, t, k) for c in COND for t in s.verification for k in range(8)] if couverture else None,
              lot_honnete_couverture_=hc if couverture else None)
    kw.update(change)
    return s, L.lot_decisif(s, e, **kw)


# --- Séparation ------------------------------------------------------------------------------------------------------

def test_separation_saine_et_artefacts():
    s = sep()
    assert len(s.ouvertes) == len(s.gardees) == 8 and set(s.ouvertes) | set(s.gardees) == set(FAB)
    with pytest.raises(GardeArret):
        L.separation(FAB[:-1] + ["a/b"], VER, E)
    with pytest.raises(GardeArret):
        L.separation(FAB, VER[:-1] + [FAB[0]], E)
    with pytest.raises(GardeArret):                         # séparation d'une autre entropie
        L.lot_honnete_couverture(sep(E + 1), E, plans(sep(E + 1).ouvertes))
    faux = L.Separation(E, s.fabrication, s.verification, s.gardees, s.ouvertes)
    with pytest.raises(GardeArret):                         # ouvertes et gardées échangées
        L.lot_honnete_couverture(faux, E, plans(faux.ouvertes))


# --- Lot honnête de l'appariement --------------------------------------------------------------------------------------

def test_lot_honnete_effectifs_et_composition():
    s, h, _ = lots_d_epreuve()
    c = h.comptes
    assert (c["honnetes"], c["controles-autre-tache"], c["texte-sans-rapport"], c["controles-generiques"]) == (576, 128, 64, 64)
    assert c["effectif"] == len(h.appels) == 832
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


def test_lot_honnete_petit_toutes_prises_et_ambiguite_des_generiques():
    s = sep()
    petit = [(t, k, 0) for t in s.ouvertes for k in range(8)] + [(t, k, 1) for t in s.ouvertes for k in range(4)]  # 96
    h = L.lot_honnete_appariement(s, E, petit)
    assert h.comptes["controles-autre-tache"] == 96 and h.comptes["texte-sans-rapport"] == 64
    with pytest.raises(L.AmbiguiteDuTexte, match="seize fois"):
        L.lot_honnete_appariement(s, E, petit[:63])


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
    L.lot_mecanique_couverture(s, E, artefacts(s))
    L.ancre_couverture(s, E)
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


# --- Ancres --------------------------------------------------------------------------------------------------------------

def test_ancre_plans_honnetes():
    s, h, _ = lots_d_epreuve()
    a = L.ancre_plans_honnetes(s, E, h)
    d = a.descriptions()
    assert len(d) == 48 and sum(x["composante"] == "honnete" for x in d) == 24
    assert all(x in h.descriptions() for x in d)
    with pytest.raises(GardeArret):                       # lot de la révision exigé sous la révision
        L.ancre_plans_honnetes(s, E, h, revision=True)
    with pytest.raises(L.AmbiguiteDuTexte):           # moins que demandé, hors des épreuves jointes : non tranché
        L._tirer(g.generateur_de(g.cle("ancr", "premiere"), E), list(range(23)), 24, "essai")
    assert sorted(L._tirer(g.generateur_de(g.cle("ancr", "premiere"), E), list(range(24)), 24, "essai")) == list(range(24))


def test_ancre_jumeaux_et_ambiguite():
    s = sep()
    a = L.ancre_jumeaux(s, E, deplacees(s.ouvertes))
    assert len(a.appels) == 24 and all(x["composante"] == "jumeau-a-effet" for x in a.descriptions())
    peu = [x for x in deplacees(s.ouvertes) if x[3] != A_EFFET] + [(s.ouvertes[0], k, 0, A_EFFET) for k in range(8)]
    with pytest.raises(L.AmbiguiteDuTexte):
        L.ancre_jumeaux(s, E, peu)
    with pytest.raises(GardeArret):
        L.ancre_jumeaux(s, E, deplacees(s.ouvertes) + [(s.ouvertes[0], 0, 9, "autre")])


# --- Lot des jumeaux de l'appariement ---------------------------------------------------------------------------------------

def test_lot_jumeaux_composition():
    s, h, j = lots_d_epreuve()
    d = j.descriptions()
    dep = [x for x in d if x["composante"] == "deplacee"]
    assert len(dep) == 64 * 4 and {x["verite"] for x in dep} == {A_EFFET, SANS_EFFET}
    assert j.comptes["deplacees-non-jugeables"] == 64 and j.comptes["honnetes-relues"] == 576
    assert len(d) == 256 + 576
    ids_h = {a["identifiant"] for a in h.appels}
    assert not ids_h & {a["identifiant"] for a in j.appels}          # identifiants neufs (clé `opaq` du lot)
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
    with pytest.raises(GardeArret):                       # la couverture n'a pas de révision : aucune clé
        g.cle("ordr", "lot-honnete-couverture", revision=True)


# --- Couverture --------------------------------------------------------------------------------------------------------

def test_lot_honnete_couverture():
    s = sep()
    lot = L.lot_honnete_couverture(s, E, plans(s.ouvertes))
    assert len(lot.appels) == 64 and lot.comptes["lectures"] == 128
    with pytest.raises(L.AmbiguiteDuTexte):
        L.lot_honnete_couverture(s, E, plans(s.ouvertes)[:-1])
    with pytest.raises(GardeArret, match="tâche permise"):
        L.lot_honnete_couverture(s, E, plans(s.ouvertes)[:-1] + [(VER[0], 0)])


def test_plans_mecaniques_et_ancre_couverture():
    s = sep()
    m = L.plans_mecaniques(s, E)
    assert len(m) == len(set(m)) == 32 and all(sum(t == u for u, _ in m) == 4 for t in s.ouvertes)
    a = L.ancre_couverture(s, E)
    assert len(a.appels) == 8 and all((x["tache"], x["episode"]) in m for x in a.descriptions())


def test_lot_mecanique():
    s = sep()
    lot = L.lot_mecanique_couverture(s, E, artefacts(s))
    assert len(lot.appels) == 160 and lot.comptes["lectures"] == 256
    a = artefacts(s)
    moins = [x for x in a if not (x[0] == "plan-tronque" and x[1:3] == a[0][1:3])]
    assert L.lot_mecanique_couverture(s, E, moins).comptes["plan-tronque"] == 31          # plan sans artefact : compté
    hors = next((t, k) for t in s.ouvertes for k in range(8) if (t, k) not in L.plans_mecaniques(s, E))
    for mauvais in ([x for x in a if x[0] != "dose-flagrante" or x[1:3] != a[0][1:3]],     # 31 doses flagrantes
                    a + [("plan-tronque",) + hors + (None,)], a + [a[0]],
                    a[1:] + [("retrait",) + a[0][1:3] + (None,)],
                    a + [("autre", a[0][1], a[0][2], None)]):
        with pytest.raises(GardeArret):
            L.lot_mecanique_couverture(s, E, mauvais)


def test_lot_jumeaux_couverture():
    s = sep()
    hc = L.lot_honnete_couverture(s, E, plans(s.ouvertes))
    lot = L.lot_jumeaux_couverture(s, E, hc, plans(s.ouvertes))
    assert len(lot.appels) == 128 and lot.comptes["lectures"] == 256
    with pytest.raises(GardeArret):
        L.lot_jumeaux_couverture(s, E, lot, plans(s.ouvertes))


# --- Lot décisif -------------------------------------------------------------------------------------------------------

def test_lot_decisif_sain():
    s, lot = decisif()
    c = lot.comptes
    assert c["action-de-condition"] == 8960 and c["sentinelle-deplacee"] == 64 * 2 + 64 * 1
    assert c["action-d-epreuve-relue"] == 320 and c["plan-de-condition"] == 896 and c["plan-d-epreuve-relu"] == 32
    sen, con = lot.tables[L.TABLE_DES_SENTINELLES], lot.tables[L.TABLE_DES_CONDITIONS]
    assert not set(sen) & set(con) and set(sen) | set(con) == {a["identifiant"] for a in lot.appels}
    assert all("condition" not in d for d in sen.values()) and all("condition" in d for d in con.values())
    relues = [d for d in sen.values() if d["composante"] == "action-d-epreuve-relue"]
    assert sum(d["classe"] == "honnete" for d in relues) == 160 and all(d["tache"] in s.ouvertes for d in relues)
    assert all(d["tache"] in s.verification for d in sen.values() if d["composante"] == "sentinelle-deplacee")


def test_lot_decisif_gardes():
    s, h, j = lots_d_epreuve()
    with pytest.raises(GardeArret, match="non déclarée"):
        decisif(actions_des_conditions=[(c, t, 0, 0) for c in COND for t in VER] + [(COND[0], FAB[0], 0, 0)])
    with pytest.raises(GardeArret, match="7"):
        decisif(actions_des_conditions=[(c, t, 0, 0) for c in COND[:6] for t in VER])
    with pytest.raises(GardeArret, match="128"):
        decisif(a_effet_des_jumeaux={(t, 0): [1] for t in VER})
    with pytest.raises(GardeArret, match="non lue"):
        decisif(couverture=False, plans_des_conditions=[])
    with pytest.raises(GardeArret, match="896"):
        decisif(plans_des_conditions=[(c, t, 0) for c in COND for t in VER])
    with pytest.raises(GardeArret):                       # lots d'épreuve de deux épreuves différentes
        _, hr, _ = lots_d_epreuve(revision=True)
        decisif(lot_honnete_en_vigueur=hr)
    with pytest.raises(GardeArret):
        decisif(couverture="oui")


def test_lot_decisif_sans_couverture_et_revision():
    s, lot = decisif(couverture=False)
    assert "plan-de-condition" not in lot.comptes and "plan-d-epreuve-relu" not in lot.comptes
    s, lot = decisif(revision=True)
    relues = [d for d in lot.tables["sentinelles"].values() if d["composante"] == "action-d-epreuve-relue"]
    assert all(d["tache"] in s.gardees and d["epreuve"] == "revision" for d in relues)


def test_relues_insuffisantes_ambiguite():
    s = sep()
    h = L.lot_honnete_appariement(s, E, [(t, k, p) for t in s.ouvertes for k in range(8) for p in range(2)])   # 128
    j = L.lot_jumeaux_appariement(s, E, h, deplacees(s.ouvertes))
    with pytest.raises(L.AmbiguiteDuTexte, match="relues"):
        decisif(lot_honnete_en_vigueur=h, lot_jumeaux_en_vigueur=j)


# --- Manifeste ---------------------------------------------------------------------------------------------------------

def test_manifeste():
    s, lot = decisif(couverture=False)
    m = {}
    ligne = L.inscrire_au_manifeste(m, lot)
    assert m["lots"]["bras-a-v2/ordr/lot-decisif"]["sha256"] == lot.empreinte == ligne["sha256"]
    assert set(ligne["sha256_des_tables"]) == {"sentinelles", "conditions"}
    L.inscrire_au_manifeste(m, lot)                                         # identique : rien
    _, autre = decisif(E + 1, couverture=False)
    with pytest.raises(GardeArret, match="R12"):
        L.inscrire_au_manifeste(m, autre)


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
    assert L.cle_de_l_envoi(t, 3, "GEMINI_API_KEY") == "GEMINI_API_KEY"   # reprise sous la clé du premier envoi
    with pytest.raises(GardeArret, match="écart"):
        L.cle_de_l_envoi(t, 3, "GEMINI_API_KEY_2")
    for r in (0, 6):
        with pytest.raises(GardeArret):
            L.cle_de_l_envoi(t, r)
    with pytest.raises(GardeArret):
        L.tableau_des_cles(0)


def test_voie_de_service_du_juge():
    s = sep()
    aj = L.ancre_jumeaux(s, E, deplacees(s.ouvertes))
    assert L.voie_de_service_du_juge(aj) == L.tableau_des_cles(24)
    _, h, _ = lots_d_epreuve()
    with pytest.raises(L.AmbiguiteDuTexte, match="M-4 \\(i\\)"):
        L.voie_de_service_du_juge(L.ancre_plans_honnetes(s, E, h))
    with pytest.raises(L.AmbiguiteDuTexte, match="M-4 \\(i\\)"):
        L.voie_de_service_du_juge(L.ancre_couverture(s, E))
    with pytest.raises(L.AmbiguiteDuTexte, match="M-4 \\(ii\\)"):
        L.voie_de_service_du_juge(L.ancre_jumeaux(s, E, deplacees(s.gardees), revision=True))
    with pytest.raises(GardeArret, match="pas un lot du juge"):
        L.voie_de_service_du_juge(h)


# --- Tirages recalculés à la main depuis les clés (mutations) ----------------------------------------------------------

def test_tirages_recalcules_depuis_les_cles():
    s, h, _ = lots_d_epreuve()
    hon = sorted(L._pos(x) for x in h.descriptions() if x["composante"] == "honnete")
    rng = g.generateur_de(g.cle("join", "controles-generiques"), E)
    rec = [hon[int(i)] for i in rng.choice(len(hon), 64, replace=False)]
    textes = rng.permutation([k for k in range(1, 5) for _ in range(16)])
    attendu = {p: int(k) for p, k in zip(rec, textes)}
    assert {L._pos(x): x["generique"] for x in h.descriptions() if x["composante"] == "controles-generiques"} == attendu
    _, lot = decisif()
    sen = lot.tables["sentinelles"].values()
    t, k = s.verification[0], 1                                  # trois candidats : 0, 3, 5
    i = g.generateur_de(g.cle_sentinelles(t, k), E).choice(3, 2, replace=False)
    assert sorted(d["pas"] for d in sen if d["composante"] == "sentinelle-deplacee" and (d["tache"], d["episode"]) == (t, k)) \
        == sorted([0, 3, 5][int(j)] for j in i)
    a_effet = {(t, k, p) for t in s.ouvertes for k in range(8) for p in (0, 1, 2)}
    assert all(L._pos(d) in a_effet for d in sen if d["composante"] == "action-d-epreuve-relue" and d["classe"] == "deplacee")


def test_generiques_a_la_borne():
    s = sep()
    juste = [(t, k, 0) for t in s.ouvertes for k in range(8)]          # 64
    assert L.lot_honnete_appariement(s, E, juste).comptes["controles-generiques"] == 64


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
