"""Essais du pilote de l'exposant p, version 2, sur processeur, sans aucun téléchargement.

Couvre (contre-lecture R2 du brouillon 1, bloquants B1 à B6 et importants I1, I3, I5, I8, M4 à M7) : stimuli v2 et leurs
règles (paires minimales, porteur partagé entre registres, classes lexicales), modèle stylisé (v2 sain, v1 artefact) ;
jumeau neutre ; table gelée des issues (identification, échecs, sensibilité) ; rééchantillonnage par sous-ensembles ;
position dans la famille ; jumeau ; identité des ancres par les rangs ; témoin positif ; symétrie ; phrases bornées ;
lecture complète sur plans synthétiques (exclu, échecs, sensibilité, tranchée avec audit de retrait) ; gardes du
lanceur (configuration, marqueurs, citations, tokeniseur, révisions, flux court, horloge et réserve, grille non finie,
R1 sans effet de bord) ; vérification du GO ; répétition jouet de bout en bout, arrêt « instrument non validé » en
mode jouet (code 3) et plafond de durée au niveau du lanceur ; simulation de puissance réduite. Chaque garde sur un cas
sain et sur un artefact (R5).
"""
from __future__ import annotations

import copy
import json
import math
import signal
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import graines, verifier_resultat
from controle_ia.pilote_exposant_p import references as REF
from controle_ia.pilote_exposant_p.run import TokeniseurJouet
from controle_ia.pilote_exposant_p_v2 import analyse as A
from controle_ia.pilote_exposant_p_v2 import courbes as C
from controle_ia.pilote_exposant_p_v2 import go as GO
from controle_ia.pilote_exposant_p_v2 import run as RUN
from controle_ia.pilote_exposant_p_v2 import stimuli as ST

RACINE = Path(__file__).resolve().parents[1]
BROUILLON = RACINE / "brouillons" / "pilote-exposant-p-v1"
CONFIG = BROUILLON / "config-pilote-exposant-p-v2.json"
STIMULI = BROUILLON / "stimuli-pilote-exposant-p-v2.json"
STIMULI_V1 = BROUILLON / "stimuli-pilote-exposant-p-v1.json"
HACHAGES = REF.charger_json()["directions_hachages_invites"]


def _stim():
    return json.loads(STIMULI.read_text(encoding="utf-8"))


def _refaire(q):
    q["FE"], q["FD"] = f"{q['corps_F']} {q['porteur_E']}", f"{q['corps_F']} {q['porteur_D']}"
    q["CE"], q["CD"] = f"{q['corps_C']} {q['porteur_E']}", f"{q['corps_C']} {q['porteur_D']}"


# --- stimuli ----------------------------------------------------------------------------------------------------

def test_stimuli_v2_conformes_et_invites_du_papier_identiques():
    st = _stim()
    assert ST.problemes_stimuli(st, HACHAGES) == []
    q = st["quadruplets"]
    assert len(q) == 30 and len({x["porteur_E"] for x in q}) == 30 and len({x["porteur_D"] for x in q}) == 30
    for x in q:                                          # paires minimales : un seul mot, le dernier
        a, b = x["FE"].split(), x["FD"].split()
        assert a[:-1] == b[:-1] and a[-1] != b[-1] and x["FE"].split()[-1] == x["CE"].split()[-1]


def _alt_porteur_dans_corps(st):
    q = st["quadruplets"][0]
    q["corps_F"] = q["corps_F"].replace("home office", "home office benchmark")
    _refaire(q)


def _alt_non_minimale(st):
    st["quadruplets"][1]["FE"] = st["quadruplets"][1]["FE"].replace("cake", "pie")


def _alt_porteur_registres(st):
    q = st["quadruplets"][2]
    q["CE"] = f"{q['corps_C']} leaderboards"


def _alt_date(st):
    q = st["quadruplets"][3]
    q["porteur_D"] = "tomorrow"
    _refaire(q)


def _alt_personne(st):
    q = st["quadruplets"][4]
    q["corps_C"] = q["corps_C"].replace("does a landlord", "does my landlord")
    _refaire(q)


def _alt_contraction(st):
    q = st["quadruplets"][5]
    q["corps_F"] = q["corps_F"].replace("it is meant", "it's meant")
    _refaire(q)


def _alt_doublon(st):
    st["quadruplets"][6]["porteur_E"] = st["quadruplets"][7]["porteur_E"]
    _refaire(st["quadruplets"][6])


@pytest.mark.parametrize("alteration, motif", [
    (_alt_porteur_dans_corps, "porteur figure dans le corps"), (_alt_non_minimale, "R-S2"),
    (_alt_porteur_registres, "n'est pas « corps porteur »"), (_alt_date, "classe contrôlée date"),
    (_alt_personne, "R-S3"), (_alt_contraction, "R-S5"), (_alt_doublon, "non distincts"),
])
def test_stimuli_v2_artefacts_detectes(alteration, motif):
    st = _stim()
    alteration(st)
    assert any(motif in p for p in ST.problemes_stimuli(st, HACHAGES))


def test_modele_stylise_v2_sain_et_v1_artefact():
    r = ST.exiger_modele_stylise(_stim()["quadruplets"], tirages=60)
    assert all(x["mediane_abs_cos"] < ST.SEUIL_STYLISE for x in r.values())
    v1 = json.loads(STIMULI_V1.read_text(encoding="utf-8"))["quadruplets"]
    with pytest.raises(GardeArret, match="R-S8"):
        ST.exiger_modele_stylise(v1, tirages=60)          # contre-lecture R2 : −0,19 ; −0,18 ; −0,14


def test_jumeau_neutre_choix_sain_et_artefact():
    st = _stim()
    ch = ST.choisir_neutres(st, lambda t: len(t.split()))
    assert ch["construit"] and ch["quadruplets_retenus"] == 30
    assert all(v == q["neutres_candidats"][0] for q, v in zip(st["quadruplets"], ch["choix"].values()))
    a, b = ST.paires(st, "N", neutres=ch["choix"])
    assert len(a) == len(b) == 60 and all(x.split()[:-1] == y.split()[:-1] for x, y in zip(a, b))
    ch = ST.choisir_neutres(st, lambda t: len(t))      # nombre de caractères : presque aucun candidat ne convient
    assert not ch["construit"]


def test_paires_et_moities():
    st = _stim()
    a, b = ST.paires(st, "E")
    assert len(a) == len(b) == 60
    a, b = ST.paires(st, "R", "A")
    assert len(a) == 30 and all(x.split()[-1] == y.split()[-1] for x, y in zip(a, b))
    a, b = ST.paires(st, "Gender", "B")
    assert len(a) == len(b) == 15


# --- lecture gelée ----------------------------------------------------------------------------------------------

BASE = dict(instrument_valide=True, cos_er=0.02, cos_moities={"E": 0.8, "R": 0.7}, echecs_er=0.0, echecs_rd=0.0,
            ic_delta=[0.05, 0.3], ic_wg=[0.6, 1.0])


@pytest.mark.parametrize("modif, attendu", [
    ({}, "au-dessus"),
    ({"instrument_valide": False}, "instrument non validé"),
    ({"cos_er": -0.12}, "exclu"),
    ({"cos_moities": {"E": 0.4, "R": 0.9}}, "non concluant (identification)"),
    ({"echecs_rd": 0.25}, "non concluant (échecs)"),
    ({"ic_delta": [-0.3, -0.05]}, "au-dessous"),
    ({"ic_delta": [-0.1, 0.15]}, "égal"),
    ({"ic_delta": [-0.1, 0.25]}, "non concluant"),
    ({"ic_delta": [-0.1, 0.15], "ic_wg": [0.15, 0.9]}, "non concluant (sensibilité)"),
    ({"ic_delta": [-0.3, -0.05], "ic_wg": None}, "non concluant (sensibilité)"),
    ({"ic_wg": [0.15, 0.9]}, "au-dessus"),
])
def test_table_gelee_des_issues(modif, attendu):
    assert A.issue_gelee(**(BASE | modif))[0] == attendu


def test_bootstrap_sous_ensembles_reproductible_et_nan():
    rng = np.random.default_rng(0)
    per = {s: 2.3 + 0.1 * rng.standard_normal() for s in range(32)}
    ref = [(k % 32, 2.0 + 0.15 * rng.standard_normal()) for k in range(60)]
    d1 = A.bootstrap_sous_ensembles(per, ref, 2000, np.random.default_rng(1))
    d2 = A.bootstrap_sous_ensembles(per, ref, 2000, np.random.default_rng(1))
    assert d1 == d2 and d1["ic"][0] > 0 and abs(d1["delta"] - 0.3) < 0.1
    per[3] = float("nan")
    d3 = A.bootstrap_sous_ensembles(per, ref, 2000, np.random.default_rng(1))
    assert d3["n_plan"] == 31 and math.isfinite(d3["ic"][0])
    assert math.isnan(A.bootstrap_sous_ensembles({0: 2.0}, ref, 100, np.random.default_rng(1))["delta"])


def test_effet_commun_compense_par_la_reference_repartie():
    """Un effet commun d'un sous-ensemble (même décalage pour le plan lu et la référence sur ce sous-ensemble) bouge peu
    Δ quand la référence est répartie ; il le bouge en plein quand toute la référence est sur le sous-ensemble 0."""
    per = {s: 2.0 for s in range(32)}
    reparti = [(k % 32, 2.0) for k in range(60)]
    seul0 = [(0, 2.0) for _ in range(60)]
    c = {s: (0.5 if s == 0 else 0.0) for s in range(32)}
    per_c = {s: v + c[s] for s, v in per.items()}
    d_r = A.bootstrap_sous_ensembles(per_c, [(s, v + c[s]) for s, v in reparti], 200, np.random.default_rng(0))
    d_0 = A.bootstrap_sous_ensembles(per_c, [(s, v + c[s]) for s, v in seul0], 200, np.random.default_rng(0))
    assert abs(d_r["delta"]) < 0.01 and abs(d_0["delta"] + 0.5 * 31 / 32) < 1e-9


def test_position_dans_la_famille_et_jumeau():
    fam = [2.0, 2.1, 1.95, 2.05, 2.02, 1.98, 2.08, 1.93]
    assert A.position_famille(2.03, fam)["position"] == "dans la famille"
    assert A.position_famille(2.6, fam)["position"] == "au-delà de la famille"
    assert A.position_famille(1.5, fam)["position"] == "en deçà de la famille"
    assert A.position_famille(2.0, fam[:2])["position"] == "famille non mesurée"
    p_er = {s: 2.5 for s in range(32)}
    assert A.qualif_jumeau(A.bootstrap_apparie(p_er, {s: 2.0 + 0.01 * (s % 3) for s in range(32)}, 500,
                                               np.random.default_rng(0))) == "au-dessus du jumeau"
    assert A.qualif_jumeau(A.bootstrap_apparie(p_er, {s: 2.5 + 0.05 * (-1) ** s for s in range(32)}, 500,
                                               np.random.default_rng(0))) == "indiscernable du jumeau"
    assert A.qualif_jumeau(None) == "jumeau non mesuré"


def test_identite_des_ancres_par_les_rangs_sain_et_artefacts():
    g = REF.charger_grilles()["wealth_gender__l2"]
    assert A.ancres_identiques(A.NORME_ANCRES_PUBLIEE, g, g)["identiques"]
    perm = g[np.random.default_rng(0).permutation(g.shape[0])]
    r = A.ancres_identiques(A.NORME_ANCRES_PUBLIEE, perm, g)
    assert not r["identiques"] and r["reserve"]                       # norme égale, ancres dans un autre ordre
    assert not A.ancres_identiques(2.5, g, g)["identiques"]


def test_controle_temoin_positif_sain_et_artefact():
    ident = {"identiques": True}
    assert A.controle_temoin_positif(3.05, (46.0, 29.5), ident)["valide"]
    assert not A.controle_temoin_positif(3.3, (46.0, 29.5), ident)["valide"]
    assert not A.controle_temoin_positif(3.05, (49.0, 29.5), ident)["valide"]
    assert A.controle_temoin_positif(2.6, (40, 30), {"identiques": False})["valide"]
    assert not A.controle_temoin_positif(float("nan"), (40, 30), {"identiques": False})["valide"]
    assert A.controle_temoin_positif(1.0, (0, 0), {"identiques": False}, {"intervalle_p_differentes": [0.5, 10]})["tolerances_jouet"]


def test_declencheurs_de_symetrie_dans_les_deux_sens():
    assert A.declencheurs_symetrie({"issue": "non concluant", "ic_delta": [-0.3, 0.3]}) == []
    m = A.declencheurs_symetrie({"issue": "non concluant", "ic_delta": [0.0, 0.04],
                                 "temoin_positif": {"p": 3.008, "ancres_identiques": False},
                                 "residu_median_er": 0.03, "instable_au_retrait": ["sans le sous-ensemble 4"]})
    assert len(m) == 4
    assert A.declencheurs_symetrie({"temoin_positif": {"p": 3.008, "ancres_identiques": True}, "residu_median_er": 0.011}) == []
    assert any("audit de symétrie" in x for x in A.declencheurs_symetrie({"issue": "égal", "ic_delta": [-0.1, 0.1]}))


def test_phrases_gelees_completes_et_bornees():
    v = dict(p_er="2.1", ic_er="2 ; 2.2", p_rd="2.0", ic_rd="1.9 ; 2.1", d="+0.1", ic_d="0 ; 0.2", d_wg="+0.9",
             ic_wg="0.7 ; 1.1", brute="égal", cos="0.12", cos_e="0.4", cos_r="0.8", motif="m")
    for k in A.PHRASES:
        t = A.PHRASES[k].format(delta=A.DELTA_EQUIVALENCE, **v)
        assert "{" not in t
        if k in ("au-dessus", "au-dessous", "égal"):
            assert "dernier jeton" in t and "couches moyennes" in t and "moyenne des" in t
    assert "taille L2" not in A.PHRASES["au-dessous"] and "une paire sans concept" not in A.PHRASES["égal"]
    for table in (A.QUALIF_FAMILLE, A.QUALIF_JUMEAU):
        for t in table.values():
            assert "{" not in t.format(ip="1 ; 2", k=8, motif="m", d="+0.1", ic="0 ; 0.2")


# --- lecture complète sur plans synthétiques ----------------------------------------------------------------------

def _plans(p_er=2.4, p_rd=2.0, p_wg=3.0, p_n=2.0, nan_er=0, K=8, S=32, M=60):
    rng = np.random.default_rng(5)
    pl = []
    for s in range(S):
        pl.append({"role": "lu", "famille": "ER", "nom": "E×R", "sous_ensemble": s, "garde": True,
                   "p": float("nan") if s < nan_er else p_er + 0.05 * rng.standard_normal(), "residu": 0.01})
        pl.append({"role": "lu", "famille": "temoin_lu", "nom": "Wealth×Gender", "sous_ensemble": s, "garde": True,
                   "p": p_wg + 0.05 * rng.standard_normal()})
        pl.append({"role": "lu", "famille": "NR", "nom": "N×R", "sous_ensemble": s, "garde": True,
                   "p": p_n + 0.05 * rng.standard_normal()})
    mu = p_rd + 0.1 * rng.standard_normal(M)
    for k in range(M):
        pl.append({"role": "lu", "famille": "rd_rd", "nom": f"rd{2*k}×rd{2*k+1}", "sous_ensemble": k % S, "garde": True,
                   "p": mu[k] + 0.05 * rng.standard_normal()})
        if k < K:
            pl += [{"role": "lu", "famille": "rd_famille", "nom": f"rd{2*k}×rd{2*k+1}", "sous_ensemble": s,
                    "garde": True, "p": mu[k] + 0.05 * rng.standard_normal()} for s in range(S) if s != k % S]
    return pl


def _sortie(cos_er=0.02, moities=(0.8, 0.7)):
    return {"instrument": {"valide": True}, "temoin_positif": {"p": 3.0, "ancres_identiques": True},
            "directions_lu": {"cosinus": {"E·R": cos_er, "E_A·E_B": moities[0], "R_A·R_B": moities[1]}}}


CFG = {"bootstrap": {"B_difference": 1000}}
GR = graines(RUN.TACHES, 7)


def test_lecture_tranchee_avec_qualificatifs_et_audit_de_retrait():
    lec = RUN.lire(_plans(), _sortie(), GR, CFG, jouet=True)
    assert lec["issue"] == "au-dessus" and lec["famille"]["position"] == "au-delà de la famille"
    assert lec["jumeau"]["qualificatif"] == "au-dessus du jumeau"
    assert lec["audit_retrait"]["recalculs"] == 32 and lec["audit_retrait"]["differentes"] == []
    assert "Position dans la famille" in lec["phrase"] and "Jumeau neutre" in lec["phrase"]
    assert lec == RUN.lire(_plans(), _sortie(), GR, CFG, jouet=True)          # graines : rejeu à l'identique
    pl = _plans(p_er=2.0, p_n=2.0)
    m_rd = float(np.mean([x["p"] for x in pl if x["famille"] == "rd_rd"]))
    for x in pl:                                         # plan lu et jumeau exactement à la moyenne de la référence
        if x["famille"] in ("ER", "NR"):
            x["p"] += m_rd - 2.0
    eg = RUN.lire(pl, _sortie(), GR, CFG, jouet=True)
    assert eg["issue"] == "égal" and eg["jumeau"]["qualificatif"] == "indiscernable du jumeau"


@pytest.mark.parametrize("kw, sortie_kw, attendu", [
    ({}, {"cos_er": 0.15}, "exclu"),
    ({}, {"moities": (0.3, 0.9)}, "non concluant (identification)"),
    ({"nan_er": 8}, {}, "non concluant (échecs)"),
    ({"p_er": 2.0, "p_wg": 2.1}, {}, "non concluant (sensibilité)"),
])
def test_lecture_chemins_non_tranches(kw, sortie_kw, attendu):
    lec = RUN.lire(_plans(**kw), _sortie(**sortie_kw), GR, CFG, jouet=True)
    assert lec["issue"] == attendu and "{" not in lec["phrase"] and "famille" not in lec


def test_courbes_sur_la_fenetre_w():
    ang = np.linspace(0, 60, 31)
    base = np.tile(np.linspace(0, 1, 31), (5, 1))
    rd = {f"rd{i}": base[0] + 0.01 * i for i in range(5)}
    r = C.lecture({"E": base[0] + 0.5}, rd, ang)
    assert r["lus"]["E"]["D"] > 0.4 and r["lus"]["E"]["part_rd_sous"] == 1.0
    assert C.masque_fenetre(ang).sum() == 30
    assert "motif" in C.lecture({"E": base[0]}, {"rd0": base[0]}, ang)


# --- gardes du lanceur -------------------------------------------------------------------------------------------

def test_configuration_coherente_et_artefacts(tmp_path):
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    RUN.exiger_config(cfg, STIMULI)
    for modif, motif in ((lambda c: c["lecture"].update(delta_equivalence=0.3), "constantes gelées"),
                         (lambda c: c["references_sha256"].update({"grilles-publiees-v1.npz": "0" * 64}), "référence"),
                         (lambda c: c.update(amont_commit="0" * 40), "commit"),
                         (lambda c: c.update(stimuli_sha256="0" * 64), "empreinte")):
        c = copy.deepcopy(cfg)
        modif(c)
        with pytest.raises(GardeArret, match=motif):
            RUN.exiger_config(c, STIMULI)


def test_run_reel_marqueurs_et_citations_sain_et_artefacts(tmp_path):
    """Run réel : refus tant qu'un marqueur reste (<<DOI_R9_BIS>>, vérification humaine) ; refus si le préenregistrement
    ne cite pas les empreintes lues (M4) ; cas sain sur des copies sans marqueur."""
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    with pytest.raises(GardeArret, match="marqueurs restants"):
        RUN.exiger_config(cfg, STIMULI, CONFIG, "prereg", reel=True)
    st = tmp_path / "stimuli.json"
    st.write_text(STIMULI.read_text(encoding="utf-8").replace("<<DOI_R9_BIS>>", "10.5281/zenodo.0")
                  .replace("<<VERIFICATION_HUMAINE_LAZAR>>", "vérifié"), encoding="utf-8")
    cfg["stimuli_sha256"] = RUN.sha(st)
    cfg["note"] = "sans marqueur"
    ch = tmp_path / "config.json"
    ch.write_text(json.dumps(cfg), encoding="utf-8")
    texte = f"config `{RUN.sha(ch)}` stimuli `{RUN.sha(st)}`"
    RUN.exiger_config(cfg, st, ch, texte, reel=True)
    with pytest.raises(GardeArret, match="ne cite pas"):
        RUN.exiger_config(cfg, st, ch, f"config `{RUN.sha(ch)}`", reel=True)


def test_run_reel_sans_preenregistrement_refuse_sans_effet_de_bord():
    avant = signal.getsignal(signal.SIGTERM)
    with pytest.raises(GardeArret, match="R1"):
        RUN.principal(["--config", str(CONFIG), "--stimuli", str(STIMULI), "--run-id", "20261104-000000-x"])
    assert signal.getsignal(signal.SIGTERM) is avant                      # M5


def test_tokeniseur_revisions_et_flux_court():
    ids = np.arange(1, 251).reshape(50, 5) % 97 + 3
    RUN.exiger_meme_lecture(TokeniseurJouet(512), TokeniseurJouet(512), ids)
    autre = TokeniseurJouet(512)
    autre.convert_ids_to_tokens = lambda x: ["x" for _ in x]
    with pytest.raises(GardeArret, match="tokeniseur"):
        RUN.exiger_meme_lecture(autre, TokeniseurJouet(512), ids)
    RUN.exiger_revision("m", "abc", {"m": "abc"})
    RUN.exiger_revision("m", "abc", None)
    with pytest.raises(GardeArret, match="révision"):
        RUN.exiger_revision("m", "abd", {"m": "abc"})
    tok = TokeniseurJouet(512)
    ids_ok, _ = RUN.charger_reserve(tok, 20, "jouet", flux=["un deux trois quatre cinq"] * 25)
    assert ids_ok.shape == (20, 5)
    with pytest.raises(GardeArret, match="< 20 demandées"):
        RUN.charger_reserve(tok, 20, "jouet", flux=["un deux trois quatre cinq"] * 10 + ["court"] * 30)


def test_horloge_reserve_des_blocs_decisifs():
    t = [0.0]
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    cfg["plafonds"] = {"duree_max_s": 100.0, "duree_plan_prevue_s": 10.0}
    pil = RUN.Pilote(cfg, {}, jouet=True)
    pil.horloge = RUN.Horloge(100.0, 10.0, temps=lambda: t[0])
    fait = []
    assert pil.bloc("desc", [lambda: fait.append(1)] * 3, "descriptif", reserve=8) is False   # 11 plans > 100 s
    assert pil.bloc("desc2", [lambda: fait.append(1)] * 3, "descriptif", reserve=5) is True
    assert pil.bloc("qualif", [lambda: fait.append(1)] * 11, "qualificatif") is False
    t[0] = 95.0
    with pytest.raises(GardeArret, match="bloc décisif"):
        pil.bloc("dec", [lambda: None], "décisif")
    assert len(fait) == 3 and [x["bloc"] for x in pil.sautes] == ["desc", "qualif"]


def test_grille_non_finie_arrete(monkeypatch):
    from controle_ia.pilote_exposant_p import balayage

    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    pil = RUN.Pilote(cfg, {}, jouet=True)
    pil.ids, pil.acts = np.ones((40, 5), dtype=np.int64), np.ones((40, 4))
    pil.couche_p, pil.couche_m = 1, 2
    monkeypatch.setattr(balayage, "balayer_plan_ancres", lambda *a, **k: np.full((6, 11, 11), np.nan))
    with pytest.raises(GardeArret, match="grille non finie"):
        pil.plan(None, "lu", "ER", "E×R", None, None, 0)
    monkeypatch.setattr(balayage, "balayer_plan_ancres", lambda *a, **k: np.ones((6, 11, 11)))
    assert math.isnan(pil.plan(None, "lu", "ER", "E×R", None, None, 0)["p"])          # sain : ajustement impossible


# --- GO ----------------------------------------------------------------------------------------------------------

def _reg(go="GO-2026-11-04-03", typ="calcul", plafond="30 USD", par="Lazar", fin=None, peri="Pilote de l'exposant p",
         extra=""):
    j = date.today()
    fin = fin or j + timedelta(days=5)
    return (f"| id | a | t | p | pl | e | par | r |\n|---|---|---|---|---|---|---|---|\n"
            f"| {go} | {j - timedelta(days=1)} | {typ} | {peri} | {plafond} | {fin} | {par} | x |\n{extra}")


def test_verification_du_go_sain_et_artefacts():
    j = date.today()
    assert GO.verifier(_reg(), "GO-2026-11-04-03", 17, j)["valide"]
    doublon_ailleurs = _reg(extra=f"| GO-2000-01-01-01 | {j} | calcul | x | 1 USD | {j} | Lazar | x |\n" * 2)
    assert GO.verifier(doublon_ailleurs, "GO-2026-11-04-03", 17, j)["avertissements"]
    revoc = f"| GO-2026-11-05-01 | {j} | révocation | GO-2026-11-04-03 retiré | — | {j} | Lazar | x |\n"
    for texte, go_id, motif in ((_reg(), "GO-2026-11-04-04", "absent"), (_reg(typ="décision"), None, "calcul"),
                                (_reg(par="autre"), None, "Lazar"), (_reg(plafond="10 USD"), None, "pire cas"),
                                (_reg(plafond="—"), None, "sans montant"), (_reg(fin=j - timedelta(days=1)), None, "période"),
                                (_reg(peri="autre étude"), None, "périmètre"), (_reg(extra=revoc), None, "révoqué"),
                                (_reg() + _reg().splitlines()[2] + "\n", None, "en double"), (_reg(), "GO-26", "illisible")):
        with pytest.raises(GO.GoInvalide, match=motif):
            GO.verifier(texte, go_id or "GO-2026-11-04-03", 17, j)


# --- répétitions jouet de bout en bout ----------------------------------------------------------------------------

def _config_jouet(tmp_path, **modifs) -> Path:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    cfg["jouet"].update({"grille": {"n": 7}, "ancres": {"par_sous_ensemble": 4, "sous_ensembles": 3, "reserve": 200},
                         "differences_aleatoires": {"k_moy": 4, "paires_disjointes_M": 3}, "isotropes_paires_max": 2,
                         "famille_contrastive_max": 2, "famille_K": 2, "stylise_tirages": 10,
                         "plans": {"temoin": {"WG_sous_ensembles": 2},
                                   "lu": {"ER_sous_ensembles": 3, "WG_sous_ensembles": 3, "NR_sous_ensembles": 3,
                                          "E_Rpapier_sous_ensembles": 1, "moities_sous_ensembles": 1, "E_rd": 1,
                                          "R_rd": 1, "mixtes_rd": 1}}})
    cfg["jouet"]["tolerances_instrument"] = dict(cfg["jouet"]["tolerances_instrument"], seuil_cos=1.01, cos_min_moities=-1.0)
    cfg["bootstrap"]["B_ancres"] = 10
    cfg["bootstrap"]["B_difference"] = 200
    for k, v in modifs.items():
        if k == "tolerances":
            cfg["jouet"]["tolerances_instrument"] = v
        else:
            cfg[k] = v
    ch = tmp_path / "config.json"
    ch.write_text(json.dumps(cfg), encoding="utf-8")
    return ch


def test_repetition_jouet_de_bout_en_bout(depot, tmp_path):
    ch = _config_jouet(tmp_path)
    code = RUN.principal(["--config", str(ch), "--stimuli", str(STIMULI), "--run-id", "20261104-000000-jouet-essai",
                          "--racine", str(depot), "--jouet"])
    assert code == 0
    diag = depot / "diag" / "20261104-000000-jouet-essai"
    for nom in ("plans", "sorties", "lecture", "resume"):
        verifier_resultat(depot, diag / f"{nom}.json")
    sortie = json.loads((diag / "sorties.json").read_text())["resultat"]
    assert sortie["jumeau"]["detail"] and sortie["tolerances_jouet"] and "interaction" in sortie["directions_lu"]
    lec = json.loads((diag / "lecture.json").read_text())["resultat"]
    assert lec["issue"] in A.PHRASES
    plans = json.loads((diag / "plans.json").read_text())["resultat"]["plans"]
    assert {x["famille"] for x in plans} >= {"temoin_positif", "isotrope", "ER", "rd_rd", "temoin_lu", "NR", "rd_famille"}
    assert lec["issue"] in ("au-dessus", "au-dessous", "égal") or "famille" not in lec
    rdrd = [p for p in plans if p["famille"] == "rd_rd"]
    assert rdrd and all(x["sous_ensemble"] == (int(x["nom"].split("×")[0][2:]) // 2) % 3 for x in rdrd)   # k mod S


def test_arret_instrument_en_mode_jouet_code_3(depot, tmp_path):
    """Le mode jouet ne contourne plus l'arrêt « instrument non validé » (contre-lecture R2, B6) : tolérances jouet
    impossibles → code 3, sorties écrites, aucun plan du modèle lu."""
    ch = _config_jouet(tmp_path, tolerances={"tol_p_identiques": 0.0, "tol_intercept_identiques": 0.0,
                                             "intervalle_p_differentes": [20.0, 21.0], "intervalle_isotrope": [20.0, 21.0]})
    code = RUN.principal(["--config", str(ch), "--stimuli", str(STIMULI), "--run-id", "20261104-000000-jouet-arret",
                          "--racine", str(depot), "--jouet"])
    assert code == 3
    diag = depot / "diag" / "20261104-000000-jouet-arret"
    res = verifier_resultat(depot, diag / "resume.json")["resultat"]
    assert res["issue"] == "instrument non validé"
    plans = json.loads((diag / "plans.json").read_text())["resultat"]["plans"]
    assert all(x["role"] == "temoin" for x in plans)


def test_plafond_de_duree_au_niveau_du_lanceur(depot, tmp_path):
    ch = _config_jouet(tmp_path, plafonds={"duree_max_s": 0.0, "duree_plan_prevue_s": 1.0})
    with pytest.raises(GardeArret, match="plafond de durée"):
        RUN.principal(["--config", str(ch), "--stimuli", str(STIMULI), "--run-id", "20261104-000000-jouet-plafond",
                       "--racine", str(depot), "--jouet"])
    arret = verifier_resultat(depot, depot / "diag" / "20261104-000000-jouet-plafond" / "arret.json")["resultat"]
    assert "plafond de durée" in arret["motif"] and arret["plans_faits"] == 0


def test_simulation_de_puissance_reduite(tmp_path):
    from controle_ia.pilote_exposant_p_v2 import puissance as P

    s = tmp_path / "p.json"
    assert P.main(["--sortie", str(s), "--rapide"]) == 0
    r = json.loads(s.read_text(encoding="utf-8"))
    assert r["scenarios"] and all(0 <= l["au-dessus"] <= 1 for sc in r["scenarios"] for l in sc["lignes"])
