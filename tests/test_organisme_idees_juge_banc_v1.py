"""Essais du banc B v2 de l'idée 1.2 (racine d'essai) : graines, composition, gel, flux, évaluation, Λ, E1, montage."""
import ast
import math
import re
from unittest import mock

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organisme_idees_juge import banc_tirages_repartis_v1 as B
from controle_ia.organisme_idees_juge import juge_v1
from controle_ia.organisme_idees_juge import lois_v1 as L
from controle_ia.organisme_idees_juge import mutations_v1 as MU
from controle_ia.organisme_idees_juge import oracle_v1 as O

RAC = MU.RACINE_ESSAI


@pytest.fixture(scope="module")
def J():
    return juge_v1.charger()


@pytest.fixture(scope="module")
def gen_T(J):
    g = B.Generation(RAC, "T", 6)    # cellule 6 : V4, dose basse (les deux fausses de plus sous la règle du cosinus)
    g.preparer_engagements(J); g.geler(); g.tirer_frais(J)
    return g


@pytest.fixture(scope="module")
def gen_N(J):
    g = B.Generation(RAC, "N", 252)  # monde M₀′
    g.preparer_engagements(J); g.geler(); g.tirer_frais(J)
    return g


def test_copie_du_juge_verifiee_et_artefact(tmp_path):
    assert "orchestrator/pole/nul_v8.py" in juge_v1.verifier_copie()
    import shutil
    copie = tmp_path / "copie"
    shutil.copytree(juge_v1.DOSSIER_COPIE, copie)
    with open(copie / "orchestrator" / "pole" / "nul_v8.py", "a", encoding="utf-8") as f:
        f.write("\n# altération\n")
    with pytest.raises(GardeArret):
        juge_v1.verifier_copie(copie)


def test_racine_et_graines():
    r = B.racine_de(B.EMPREINTE_PREREG)
    assert r == int(B.EMPREINTE_PREREG, 16)
    with pytest.raises(GardeArret):
        B.racine_de("xyz")
    a, b = B.generateur(r, 1, 0, 24).random(4), B.generateur(r, 1, 0, 24).random(4)
    assert (a == b).all() and not (a == B.generateur(r, 1, 0, 25).random(4)).all()
    assert not (B.generateur(r, 1, 0, 3, 2).random(4) == B.generateur(r, 1, 0, 4, 2).random(4)).all()
    with pytest.raises(GardeArret):
        B.generateur(r, -1, 0)


def test_archive_A2():
    for g in range(30):
        a = B.construire_archive(RAC, 1, g)
        assert abs(a["sA"]) >= 0.3 and abs(a["sB"]) >= 0.3
        assert a["S3"]["condition"] == {"indice": a["jA"], "seuil": a["sA"]}
        assert a["S4"]["condition"] == {"indice": 1 - a["jA"], "seuil": a["sB"]}
        assert a["cut"][a["jA"]] == a["sA"]


def test_composition_validite_et_determinisme(J, gen_T, gen_N):
    for gen in (gen_T, gen_N):
        assert [c.sorte for c in gen.cartes] == list(B.SORTES[gen.famille])
        for c in gen.cartes:
            J.sp.valider_loi(c.loi, 3, 2)
        assert sorted(gen.positions) == list(range(24))
        assert [c.empreinte for c in B.Generation(RAC, gen.famille, gen.g).cartes] == [c.empreinte for c in gen.cartes]
    assert gen_N.monde.details["monde"] == "M0prime" and gen_N.monde.loi["type"] == "transformee"
    assert gen_N.cartes[8].loi == gen_N.monde.loi
    m0 = B.Generation(RAC, "N", 3)
    assert m0.monde.details["monde"] == "M0" and len(m0.monde.loi["composantes"]) == 5
    assert m0.cartes[0].loi["composantes"][1:] == m0.monde.loi["composantes"][1:]


def test_fausses_construites_regle_du_cosinus(gen_T, gen_N):
    """Famille T, V4 : six fausses sous la règle ; famille N : deux, référence la porteuse construite × 1 (O1, O2)."""
    fausses_T = [c for c in gen_T.cartes if c.details.get("construction", "").startswith("fausse construite")]
    assert len(fausses_T) == 6
    for c in fausses_T + [c for c in gen_N.cartes if c.sorte == "fausses construites"]:
        assert c.details["cosinus"] <= 0 or c.details["plafond_atteint"]
    ech = gen_N.echantillon
    s1 = L.probas_np(gen_N.archive["S1"], ech.Z, ech.G)
    ref = L.probas_np(gen_N.cartes[16].loi, ech.Z, ech.G)
    for c in gen_N.cartes[20:22]:
        assert L.cosinus(ref, L.probas_np(c.loi, ech.Z, ech.G), s1) == pytest.approx(c.details["cosinus"])


def test_ordre_du_gel_cas_sain_et_artefacts(J):
    g = B.Generation(RAC, "T", 0)
    with pytest.raises(GardeArret, match="avant le gel"):
        g.tirer_frais(J)
    with pytest.raises(GardeArret, match="sans les 24 engagements"):
        g.geler()
    g.ouvrir_flux_frais(0)
    with pytest.raises(GardeArret, match="après l'ouverture d'un flux frais"):
        g.preparer_engagements(J)
    g2 = B.Generation(RAC, "T", 0)
    g2.preparer_engagements(J)
    g2.ouvrir_flux_frais(3)
    with pytest.raises(GardeArret, match="issue fraîche tirée avant le gel"):
        g2.geler()
    g3 = B.Generation(RAC, "T", 0)
    g3.preparer_engagements(J); g3.geler()
    g3.engagements[5].engagement["alpha"] = 0.1
    with pytest.raises(GardeArret, match="modifié après le gel"):
        g3.tirer_frais(J)
    g4 = B.Generation(RAC, "T", 0)
    g4.preparer_engagements(J); g4.geler(); g4.tirer_frais(J)       # sain
    assert g4.etat == "tiree" and len(g4.issues) == 24 and all(len(v) == 800 for v in g4.issues.values())


def test_flux_propre_par_carte_cas_sain_et_artefact(J, gen_T):
    assert [cle for _, cle, _ in gen_T.flux_ouverts] == [(1, 6, i, 2) for i in range(24)]
    assert len({tuple(e) for _, _, e in gen_T.flux_ouverts}) == 24
    g = B.Generation(RAC, "T", 0)
    g.preparer_engagements(J); g.geler()
    with mock.patch.object(B, "cle_flux_frais", lambda f, gg, i: (f, gg, 0, 2)):
        with pytest.raises(GardeArret, match="partagé"):
            g.tirer_frais(J)


def test_oracle_avant_les_issues_fraiches(J, gen_T):
    g = B.Generation(RAC, "T", 6)
    t = O.table_oracle(J, g)                                         # sain
    assert len(t["cartes"]) == 24 and t["n"] == 20000
    assert {c["classe"] for c in t["cartes"]} <= set(O.CLASSES)
    assert all(c["classe"] in ("porteuse", "porteuse sans gain") for c in t["cartes"][:6])
    with pytest.raises(GardeArret, match="après l'ouverture"):
        O.table_oracle(J, gen_T)                                     # artefact : issues fraîches déjà tirées


def test_oracle_cache_egal_au_cache_du_juge(J):
    g = B.Generation(RAC, "N", 1)
    ech = g.echantillon
    n = 400
    Zs, Gs, ys = ech.Z[:n], ech.G[:n], [int(v) for v in ech.y[:n]]
    inst = B.instances_dicts(Zs, Gs)
    c_np, c_j = O.CacheNumpy(J, Zs, Gs), J.sp.Cache(ys, inst)
    biblio = J.nul_v8.membres_archive_v8(dict(B.lois_archive(g.archive)), None, 3, 2)
    for m in biblio:
        if m["type"] in J.nf.TYPES_AJUSTES:
            a = J.nf.valeurs_ajustees(m, c_np, ys, 3, [n])[n]
            b = J.nf.valeurs_ajustees(m, c_j, ys, 3, [n])[n]
        else:
            a = J.sp.trajectoire_membre(m, ys, inst, 3, c_np)[-1]
            b = J.sp.trajectoire_membre(m, ys, inst, 3, c_j)[-1]
        assert a == pytest.approx(b, abs=1e-8)


def test_evaluation_filtree_et_egalite_avec_le_juge(J, gen_T):
    i = 0
    ev = B.evaluer_carte(J, gen_T.engagements[i], gen_T.issues[i])
    gele = gen_T.engagements[i]
    direct = J.nf.evaluer_v2(gele, {"empreinte_engagement": gele.empreinte, "issues": gen_T.issues[i], "plan_execution": "ordre_naturel"})
    assert list(ev["trajectoire_log_w"]) == direct["trajectoire_log_w"]
    for champ in B.CHAMPS_INTERDITS:
        with pytest.raises(GardeArret, match="interdit"):
            ev[champ]
    with pytest.raises(GardeArret):
        B.EvaluationFiltree([0.0] * 31)
    with pytest.raises(GardeArret, match="non fini"):
        B.EvaluationFiltree([0.0] * 31 + [math.inf])


def test_montage_comme_juger_carte(J):
    """Le montage de `a_blanc_v59.juger_carte` (lu par analyse syntaxique, jamais exécuté) est celui du banc."""
    src = (juge_v1.DOSSIER_ORCHESTRATEUR / "pole" / "a_blanc_v59.py").read_text(encoding="utf-8")
    arbre = ast.parse(src)
    f = next(n for n in arbre.body if isinstance(n, ast.FunctionDef) and n.name == "juger_carte")
    texte = ast.unparse(f)
    for attendu in ("list(sp.BIBLIOTHEQUE_STANDARD) + [{'nom': 'marginale_entrainement', 'type': 'fixe', 'probas': q_ent}]",
                    "nul_v8.membres_archive_v8(dict(archive), None, K, DIM)",
                    "nf.construire_engagement_v2('fiche', loi, instances, K, ALPHA, biblio, 0, None",
                    "_frequences(", "nf.evaluer_v2(gele, tirages"):
        assert attendu in texte, attendu
    assert re.search(r"^ALPHA, TIRAGES, ENTRAINEMENT, EPISODES_TRANCHE, ORACLE = 0\.05, 200, 100, 400, 4000$", src, re.M)
    rng = np.random.default_rng(0)
    a = {n: L.softmax_aleatoire(rng) for n in ("S1", "S2", "S3", "S4")}
    q = [0.3, 0.3, 0.4]
    attendu = list(J.sp.BIBLIOTHEQUE_STANDARD) + [{"nom": "marginale_entrainement", "type": "fixe", "probas": q}] \
        + J.nul_v8.membres_archive_v8(dict(a), None, 3, 2)
    assert B.bibliotheque(J, q, a) == attendu
    assert len(attendu) == 17


def test_rapport_exact_et_domination(J, gen_N):
    lam = gen_N.log_lambda(J)
    assert all(abs(v) < 1e-9 for v in lam[8])          # la carte « monde » : Λ = 1 à chaque instant
    ev = B.evaluer_carte(J, gen_N.engagements[8], gen_N.issues[8])
    assert B.domination(ev["trajectoire_log_w"], lam[8]) == []      # sain
    assert B.domination([0.0] * 31 + [0.5], [0.0] * 32) == [(31, 0.5)]   # artefact
    with pytest.raises(GardeArret):
        B.Generation(RAC, "T", 0).log_lambda(J)


def test_essai_E1_cas_sain_et_artefact(J, gen_T):
    r = B.essai_E1_carte(J, gen_T, 12, instants=(25, 400, 800))
    assert r["echecs"] == [] and r["instants"] == 3
    vrai = B.trajectoire_de

    def fuite(JJ, gele, issues):           # une évaluation qui lit les issues au-delà de t
        return tuple(v + 1e-3 * sum(issues[-5:]) for v in vrai(JJ, gele, issues))
    with mock.patch.object(B, "trajectoire_de", fuite):
        r2 = B.essai_E1_carte(J, gen_T, 12, instants=(25,))
    assert r2["echecs"]
    with pytest.raises(GardeArret, match="au lieu de 800"):
        B.evaluer_carte(J, gen_T.engagements[0], gen_T.issues[0][:25])


def test_cartes_E1_couvrent_chaque_sorte():
    assert len(B.CARTES_E1) == 50
    sortes = {(f, B.SORTES[f][i]) for f, _, i in B.CARTES_E1}
    assert sortes == {(f, s) for f in ("T", "N") for s in B.SORTES_UNIQUES[f]}
