"""Lecture complémentaire « par épisode » de R1-R2 (code v4) : essais R5 sur données **synthétiques** aux formats exacts du
fournisseur (générateur et écrivains des essais v1 de la principale) — jamais les vraies données de R1, R2 ni R4.
Transformation exacte ; effet planté retrouvé, nul planté rendu nul ; chaque garde éprouvée sur un cas sain et sur un
artefact (structure d'épisodes, NaN, plis et scores ≠ principale, fiche ≠, entropie des plis ≠) ; rejeu non validé ;
R2 absent ; tirages sans rééchantillonnage ; mode décisif (code cité, constantes, entropie, second passage)."""
import json
from pathlib import Path

import numpy as np
import pytest

from conftest import committer
from controle_ia.analyse_principale_r1_r2 import calcul_v1 as CV
from controle_ia.analyse_principale_r1_r2 import calcul_v4 as C4
from controle_ia.analyse_principale_r1_r2 import constantes_v1 as K
from controle_ia.analyse_principale_r1_r2 import constantes_v2 as K2
from controle_ia.analyse_principale_r1_r2 import constantes_v4 as K4
from controle_ia.analyse_principale_r1_r2 import lecture_v1 as LP
from controle_ia.analyse_principale_r1_r2 import lecture_v2 as LP2
from controle_ia.analyse_principale_r1_r2 import lecture_v4 as LE
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import graines
from controle_ia.scellement import empreinte, sceller
from test_analyse_principale_r1_r2_v1 import D, RUN, _donnees, _source

RACINE = Path(__file__).resolve().parents[1]
E_PLIS = 4242


@pytest.fixture(autouse=True)
def constantes_reduites(monkeypatch):
    for nom, v in (("DIMENSION", D), ("TIRAGES", 300), ("N_PLANCHER", 50), ("RUN_P3", RUN)):
        monkeypatch.setattr(K, nom, v)
    for nom, v in (("TIRAGES", 300), ("N_PLANCHER", 50)):
        monkeypatch.setattr(K4, nom, v)


def _principale(depot, run="20261102-040000-principale", entropie=E_PLIS):
    LP2.analyser(depot, "fiche.json", run, None, entropie=entropie, autoriser_depot_sale=True)
    return f"diag/{run}/{K2.NOM_SORTIE}.json"


def _episode(depot, principale, run="20261102-041000-episode", entropie=99, entropie_plis=E_PLIS):
    return LE.analyser(depot, "fiche.json", principale, run, None, entropie=entropie, entropie_plis=entropie_plis,
                       autoriser_depot_sale=True)


# ------------------------------------------------------------------------------------------------ transformation
def test_moins_log_p_exacte_exclusion_de_la_tache_et_invariance():
    s_res = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    t_res = np.array([0, 0, 1, 1, 2, 2])
    # évalué hors réservoir (tâche 9) : p = (1 + #{≥ s}) / 7
    v = C4.moins_log_p(s_res, t_res, np.array([5.5, 0.0, -np.inf, 6.0]), np.array([9, 9, 9, 9]))
    assert np.allclose(np.exp(-v), [2 / 7, 7 / 7, 7 / 7, 2 / 7])
    # évalué dans le réservoir (tâche 2, score 6) : sa tâche est retirée → p = (1 + 0) / (1 + 4)
    v = C4.moins_log_p(s_res, t_res, np.array([6.0, 1.0]), np.array([2, 0]))
    assert np.allclose(np.exp(-v), [1 / 5, (1 + 4) / 5])
    # invariance par transformation croissante du score
    rng = np.random.default_rng(1)
    a, b = rng.normal(size=50), rng.normal(size=20)
    ta, tb = rng.integers(0, 5, 50), rng.integers(0, 8, 20)
    assert np.array_equal(C4.moins_log_p(a, ta, b, tb), C4.moins_log_p(np.exp(3 * a), ta, np.exp(3 * b), tb))
    # deux dimensions = colonne par colonne
    A, B = rng.normal(size=(50, 3)), rng.normal(size=(20, 3))
    V = C4.moins_log_p(A, ta, B, tb)
    assert all(np.array_equal(V[:, j], C4.moins_log_p(A[:, j], ta, B[:, j], tb)) for j in range(3))
    # artefacts : NaN, réservoir vide
    with pytest.raises(GardeArret, match="non défini"):
        C4.moins_log_p(s_res, t_res, np.array([np.nan]), np.array([9]))
    with pytest.raises(GardeArret, match="vide"):
        C4.moins_log_p(np.array([]), np.array([], dtype=int), np.array([1.0]), np.array([9]))


def test_seuil_du_rang_1_au_rang_3_sur_48_episodes():
    s = np.arange(48, dtype=float)
    assert CV.seuil_ordre_superieur(s, K4.ALPHA_PRINCIPAL) == 47.0          # maximum : 1 % et 2 % donnent le même seuil
    assert CV.seuil_ordre_superieur(s, (2, 100)) == 47.0
    assert CV.seuil_ordre_superieur(s, K4.ALPHA_FRAGILITE) == 46.0
    assert CV.seuil_ordre_superieur(s, K4.ALPHA_SECONDAIRE) == 45.0


def test_structure_des_episodes_saine_et_artefact():
    d = _donnees(3)
    t = d["tables"]
    taches = sorted(set(t["tache"].tolist()))
    ti = np.searchsorted(np.array(taches), t["tache"])
    ep = C4.episodes_de(t, ti, taches)
    assert ep["n"] == 240 and set(ep["cond"].tolist()) == set(K.CONDITIONS)
    t2 = dict(t)
    t2["pas"] = t["pas"].copy()
    t2["pas"][1] = t2["pas"][0]
    with pytest.raises(GardeArret, match="pas en double"):
        C4.episodes_de(t2, ti, taches)
    t3 = dict(t)
    t3["episode"] = np.where(t["condition"] == "honnete", "h/" + t["tache"].astype(str) + "/e" + (t["pas"] % 2).astype(str),
                             t["episode"])
    with pytest.raises(GardeArret, match="nombre d'épisodes par tâche"):
        C4.episodes_de(t3, ti, taches)


# ------------------------------------------------------------------------------------------------ bout en bout
def test_effet_plante_retrouve_et_concordance_avec_la_principale(depot, monkeypatch):
    d = _donnees(5, w=3.0, g=0.0, j=0.3)
    _source(depot, monkeypatch, d)
    pr = _principale(depot)
    r = _episode(depot, pr)
    p = r["calcul"]["principale_bras"]
    assert r["concordance_principale"] == {"plis": "identiques", "rappels": "identiques", "bras": sorted(K4.BRAS)}
    assert r["issue"]["classes"]["W-G"] == "supérieure" and r["issue"]["plancher_W"] == "au-dessus"
    assert any(x.startswith("P-E1, W − G (par épisode) : P-E1 confirmée") for x in r["issue"]["lignes"])
    assert all(m["par_alpha"]["1/100"]["fausses_alarmes_compte"] <= 4 for m in p["bras"].values())
    assert p["bras"]["W"]["par_alpha"]["1/100"]["rappel"] >= p["bras"]["W"]["rappel_action_1pc"]   # accumulation
    assert r["calcul"]["plis"] == json.loads((depot / pr).read_text(encoding="utf-8"))["resultat"]["calcul"]["plis"]
    assert (depot / "diag" / "20261102-041000-episode" / f"{K4.NOM_SORTIE}.md.sha256").exists()


def test_nul_plante_rendu_nul(depot, monkeypatch):
    d = _donnees(8, w=0.0, g=0.0, j=0.0, cout=0.0)
    _source(depot, monkeypatch, d)
    r = _episode(depot, _principale(depot))
    assert r["issue"]["classes"]["W-G"] == "non concluant" and r["issue"]["classes"]["W-J3s"] == "non concluant"
    assert not any("P-E1 confirmée" in x for x in r["issue"]["lignes"])


def test_gardes_contre_la_principale_saines_et_artefacts(depot, monkeypatch):
    d = _donnees(6, w=2.0)
    _source(depot, monkeypatch, d)
    pr = _principale(depot)
    with pytest.raises(GardeArret, match="entropie des plis"):                       # autres plis que la principale
        _episode(depot, pr, run="20261102-042001-x", entropie_plis=E_PLIS + 1)
    with pytest.raises(GardeArret, match="nom"):
        _episode(depot, "diag/20261102-040000-principale/autre.json", run="20261102-042002-x")
    rp = LE.lire_principale(depot, pr, empreinte(depot / "fiche.json"), E_PLIS, False)
    with pytest.raises(GardeArret, match="fiche"):
        LE.lire_principale(depot, pr, "0" * 64, E_PLIS, False)
    with pytest.raises(GardeArret, match="non décisif"):
        LE.lire_principale(depot, pr, empreinte(depot / "fiche.json"), E_PLIS, True)
    groupes = rp["calcul"]["plis"]
    ev = {b: {"rappel": rp["calcul"]["principale"]["bras"][b]["par_alpha"]["1/100"]["rappel"]} for b in K4.BRAS}
    assert LE.exiger_concordance_principale(rp, groupes, ev, {}, "complet")["rappels"] == "identiques"
    ev_faux = dict(ev, W={"rappel": ev["W"]["rappel"] + 1e-12})                      # score d'action altéré
    with pytest.raises(GardeArret, match="scores d'action"):
        LE.exiger_concordance_principale(rp, groupes, ev_faux, {}, "complet")
    with pytest.raises(GardeArret, match="plis"):
        LE.exiger_concordance_principale(rp, groupes[::-1], ev, {}, "complet")
    with pytest.raises(GardeArret, match="mode"):
        LE.exiger_concordance_principale(rp, groupes, ev, {}, "sans R2")
    with pytest.raises(GardeArret, match="non lus"):
        LE.exiger_concordance_principale(rp, groupes, ev, {"J8s": "x"}, "complet")
    with pytest.raises(GardeArret, match="entropie et entropie des plis"):
        LE.analyser(depot, "fiche.json", pr, "20261102-042003-x", None, entropie=1, autoriser_depot_sale=True)


def test_rejeu_non_valide_rien_n_est_lu(depot, monkeypatch):
    d = _donnees(4)
    _source(depot, monkeypatch, d, r1=False, r2=False)
    r = _episode(depot, _principale(depot))
    assert r["mode"] == "rejeu non validé" and "calcul" not in r and "rien n'est lu" in r["issue"]["lignes"][-1]


def test_R2_absent_juges_non_lus_famille_inchangee(depot, monkeypatch):
    d = _donnees(7, w=3.0)
    _source(depot, monkeypatch, d, r2=False)
    r = _episode(depot, _principale(depot))
    p = r["calcul"]["principale_bras"]
    assert set(p["non_lus"]) == {"J3s", "J3g", "J8s"} and not p["comparaisons"]["W-J3s"]["lue"]
    assert any("famille de Bonferroni gardée à deux" in x for x in r["issue"]["lignes"])


def test_tirages_sans_reechantillonnage_rendent_le_rappel_par_episode():
    d = _donnees(2, w=2.0)
    t = d["tables"]
    taches = sorted(set(t["tache"].tolist()))
    ti = np.searchsorted(np.array(taches), t["tache"])
    cond = t["condition"].astype(str)
    eligible = np.all(np.isfinite(t["scores"]), axis=1)
    pli, _ = CV.plis_des_taches(t["tache"], np.random.default_rng(0))
    ep = C4.episodes_de(t, ti, taches)
    pe = C4.plis_episodes(pli, ep)
    be = C4.bras_episode(t["scores"][:, 0], eligible, cond, pli, ti, ep, pe)
    el = np.ones(ep["n"], bool)
    for a in K4.ALPHAS:
        ev = CV.evaluer(be, el, ep["cond"], pe, ep["tache_idx"], len(taches), a)
        tir = CV.rappels_tires(be, el, ep["cond"], pe, ep["tache_idx"], a, np.ones((1, len(taches))))
        assert tir[0] == pytest.approx(ev["rappel"])
        assert all(be["calib"][k].size == 48 for k in range(K.PLIS))
    # artefact : NaN sur une action éligible
    s = t["scores"][:, 0].copy()
    s[np.flatnonzero(eligible)[0]] = np.nan
    with pytest.raises(GardeArret, match="non défini"):
        C4.bras_episode(s, eligible, cond, pli, ti, ep, pe)


def test_mention_contraire_confondu_et_seuil_fragile_rapportes(depot, monkeypatch):
    d = _donnees(9, w=3.0, mention=3.0, j=0.3)
    _source(depot, monkeypatch, d)
    r = _episode(depot, _principale(depot))
    assert r["issue"]["mention"] == "contraire"
    assert any("Confondu" in x for x in r["issue"]["lignes"])
    assert "classes_rang2" in r["issue"] and "classes_principale" in r["issue"]


# ------------------------------------------------------------------------------------------------ mode décisif
def _prereg(depot, nom, fichiers, constantes, motif, alterer=False):
    lignes = [f"- `{c}` : `{empreinte(RACINE / c)}`" for c in fichiers]
    if alterer:
        lignes[-1] = lignes[-1][:-3] + ("0" if lignes[-1][-3] != "0" else "1") + lignes[-1][-2:]
    texte = "\n\n".join([
        "# Préenregistrement jouet", f"{motif} : `{constantes}`", "## Code", *lignes, "## Hypothèse", "h",
        "## Prédiction chiffrée et signe attendu", "p", "## Métrique", "m", "## Seuil", "s", "## Plan d'analyse", "a",
        "## Critères de lecture gelés", "c", "## Liste d'arrêt", "l",
        "## Contre-lecture", f"relu `{'a' * 64}`, rapport `{'b' * 64}`"]) + "\n"
    p = depot / nom
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")
    return sceller(p)


def test_mode_decisif_v4_graines_plis_et_gardes(depot, monkeypatch):
    d = _donnees(15)
    _source(depot, monkeypatch, d)
    monkeypatch.setattr(LP, "exiger_code_importe_sous", lambda r: None)
    monkeypatch.setattr(K, "VERSIONS_EXIGEES", {k: v for k, v in LP.versions().items() if k in ("python", "numpy", "scipy")})
    f2 = LP2.FICHIERS_PAQUET + LP2.FICHIERS_ESSAIS + LP2.FICHIERS_REUTILISES
    sha_pr = _prereg(depot, "prereg/ap.md", f2, K2.empreinte_constantes(), "Empreinte des constantes (analyse principale, code v2)")
    committer(depot)
    LP2.analyser(depot, "fiche.json", "20261102-050000-analyse-principale", "prereg/ap.md")
    pr = f"diag/20261102-050000-analyse-principale/{K2.NOM_SORTIE}.json"
    monkeypatch.setattr(K4, "PREREG_PRINCIPALE", dict(K4.PREREG_PRINCIPALE, sha256=sha_pr))
    f4 = LE.FICHIERS_PAQUET + LE.FICHIERS_ESSAIS + LE.FICHIERS_REUTILISES
    motif = "Empreinte des constantes (analyse par épisode, code v4)"
    sha = _prereg(depot, "prereg/ep.md", f4, K4.empreinte_constantes(), motif)
    _prereg(depot, "prereg/ep-altere.md", f4, K4.empreinte_constantes(), motif, alterer=True)
    committer(depot)
    with pytest.raises(GardeArret, match="empreinte citée"):
        LE.analyser(depot, "fiche.json", pr, "20261102-051001-x", "prereg/ep-altere.md")
    with pytest.raises(GardeArret, match="entropie"):
        LE.analyser(depot, "fiche.json", pr, "20261102-051002-x", "prereg/ep.md", entropie=7)
    with pytest.raises(GardeArret, match="entropie des plis"):
        LE.analyser(depot, "fiche.json", pr, "20261102-051003-x", "prereg/ep.md", entropie_plis=7)
    r = LE.analyser(depot, "fiche.json", pr, "20261102-051004-episode", "prereg/ep.md")
    attendue = K2.entropie_de(sha)
    assert r["statut"] == "décisif" and int(r["entropie"]) == attendue
    assert int(r["entropie_plis"]) == K2.entropie_de(sha_pr) != attendue
    assert r["concordance_principale"]["plis"] == "identiques"
    man = json.loads((depot / "runs" / "20261102-051004-episode" / "manifeste.json").read_text(encoding="utf-8"))
    ref = graines(list(K4.CLES_GRAINES), attendue)
    assert man["decisif"] and man["commande"] == K4.COMMANDE and all(man["graines"][k] == ref[k] for k in K4.CLES_GRAINES)
    committer(depot)
    with pytest.raises(GardeArret, match="second passage"):
        LE.analyser(depot, "fiche.json", pr, "20261102-051005-x", "prereg/ep.md")
    monkeypatch.setattr(K4, "PLAFOND", 0.9)                                     # constantes ≠ empreinte citée
    with pytest.raises(GardeArret, match="constantes gelées"):
        LE.exiger_code_cite((depot / "prereg/ep.md").read_text(encoding="utf-8"))


def test_liste_fermee_v4():
    for c in LE.FICHIERS_PAQUET + LE.FICHIERS_ESSAIS + LE.FICHIERS_REUTILISES:
        assert (RACINE / c).is_file(), c
    assert set(LP2.FICHIERS_PAQUET) < set(LE.FICHIERS_PAQUET)
    with pytest.raises(GardeArret, match="liste fermée"):
        LE.exiger_code_cite("rien")
    assert K4.entropie_principale() == int.from_bytes(bytes.fromhex(K4.PREREG_PRINCIPALE["sha256"])[:16], "big")
