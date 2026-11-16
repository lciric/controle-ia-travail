"""Idée 1.1 (préenregistrement scellé `3ffe1739…`) — banc, nuls limités, J9-Dc, égalités avec le code du juge et du v9,
carte gelée (lemme 4), essais d'égalité en miniature (E0, E9, EP, ED). Racine d'essai distincte de celle du jeu."""
import difflib
import hashlib
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organisme_idees_juge import banc_idee_1_1_v2 as B
from controle_ia.organisme_idees_juge import etape0_idee_1_1_v5 as E0
from controle_ia.organisme_idees_juge import vue_v9_v2 as VV

RACINE_DEPOT = Path(__file__).resolve().parents[1]
RACINE_ESSAI = int(hashlib.sha256(b"essais idee 1.1 v1, banc").hexdigest(), 16)
V9 = VV.ORCH_V9 / "pole" / "nul_v9.py"


@pytest.fixture(scope="module")
def V():
    return VV.charger()


def test_lignes_du_texte():
    assert len(B.NOMS) == 30
    assert B.NOMS[:7] == ("Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7")
    assert B.NOMS[22:] == ("Q8", "Q9a", "Q9b", "Hs", "Hm", "H7", "Hg", "Hn")
    assert [B.NOMS[i] for i in B.LIGNES_V][:3] == ["V1(0.25)", "V1(0.5)", "V1(0.75)"] and len(B.LIGNES_V) == 15
    assert B.T8 == tuple(range(25, 201, 25)) and B.T40 == tuple(range(5, 201, 5)) and set(B.T8) <= set(B.T40)


@pytest.mark.parametrize("i", range(30))
def test_chaque_ligne_se_construit_dans_la_grammaire(V, i):
    rep = B.Repetition(V, RACINE_ESSAI, i, 0)
    assert rep.lit_hist == (B.NOMS[i] in B.LIGNES_H)
    assert not B.lit_historique(V.J, rep.monde)
    if B.NOMS[i] == "Q8":
        assert len(rep.monde["composantes"]) == 5 and abs(sum(rep.monde["poids"]) - 1) < 1e-12
    if B.NOMS[i] in ("Q1", "Q2", "Q3", "Q4", "Q5", "Q6") or B.NOMS[i].startswith("V"):
        assert rep.carte == rep.monde
    assert rep.Lp.shape == (200, 4, 3) and rep.Mp.shape == (200, 3)


def test_graines_cles_distinctes(V):
    a = B.Repetition(V, RACINE_ESSAI, 0, 0)
    b = B.Repetition(V, RACINE_ESSAI, 0, 1)
    c = B.Repetition(V, RACINE_ESSAI, 0, 0, cle=(97, 40, 0, 0))
    assert a.archive != b.archive and a.archive != c.archive
    assert B.etat_graine(RACINE_ESSAI, 0, 0, 0) != B.etat_graine(RACINE_ESSAI, 0, 0, 1)
    with pytest.raises(GardeArret):
        B.Repetition(V, RACINE_ESSAI, 0, 0, cle=(5, 1))


def test_nul_limite_quatre_changements_declares_seulement():
    a = V9.read_text(encoding="utf-8").splitlines()
    b = (RACINE_DEPOT / "src/controle_ia/organisme_idees_juge/nul_limite_v1.py").read_text(encoding="utf-8").splitlines()
    retires = [l for l in difflib.unified_diff(a, b, lineterm="", n=0) if l.startswith("-") and not l.startswith("---")]
    ajoutes = [l for l in difflib.unified_diff(a, b, lineterm="", n=0) if l.startswith("+") and not l.startswith("+++")]
    assert len(retires) == 15 and len(ajoutes) == 24
    texte = "\n".join(ajoutes)
    for morceau in ('"seuil_fixe"', "membres_morceaux(lois_connues, partitions)", 'PREFIXE_MORCEAUX = "limite:"',
                    "partitions=None"):
        assert morceau in texte
    # solveur, constantes et évaluation inchangés
    for nom in ("def maximiser_par_lots", "def _certificats", "def evaluer_sur_issues", "TOLERANCE_GROUPE = 1e-3",
                "PALIERS_MU = ", "PAS_MAX_PAR_PALIER = 30", "def detail_morceaux_groupe"):
        assert not any(nom in l for l in retires + ajoutes), nom


def test_morceaux_par_coupe_un_seul_changement():
    a = V9.read_text(encoding="utf-8")
    import ast
    seg = lambda src, n: ast.get_source_segment(src, [x for x in ast.parse(src).body if getattr(x, "name", "") == n][0])
    b = (RACINE_DEPOT / "src/controle_ia/organisme_idees_juge/morceaux_par_coupe_v1.py").read_text(encoding="utf-8")
    d = list(difflib.unified_diff(seg(a, "detail_morceaux_groupe").splitlines(), seg(b, "detail_morceaux_par_coupe").splitlines(),
                                  lineterm="", n=0))
    chg = [l for l in d if l[:1] in "+-" and l[:3] not in ("+++", "---")]
    assert len(chg) == 5 and sum(1 for l in chg if l.startswith("-")) == 2, chg


def _rep_jouee(V, nom, r=0, **kw):
    rec, rep = B.jouer_repetition(V, RACINE_ESSAI, B.INDICE[nom], r, **kw)
    return rec, rep


def test_bras_egaux_au_code_du_juge_et_du_v9(V):
    rec, rep = _rep_jouee(V, "Q2")
    off = {"J8": V.J.nf.evaluer_v2(rep.engagements["J8"], rep.tirages_de("J8")),
           "J9": V.v9.evaluer_v9(rep.engagements["J9"], rep.tirages_de("J9")),
           "La": V.limite.evaluer_v9(rep.engagements["La"], rep.tirages_de("La")),
           "Ld": V.limite.evaluer_v9(rep.engagements["Ld"], rep.tirages_de("Ld"))}
    for q, ev in off.items():
        assert [round(v, 6) for v in rec[q]["log_w"]] == ev["trajectoire_log_w"], q
        assert rec[q]["promue"] == ev["promue"]
    jum = V.v9.evaluer_v9(rep.engagements["jumeau"], rep.tirages_de("jumeau"))
    assert [round(v, 6) for v in rec["J9-D40"]["log_w_40"]] == jum["trajectoire_log_w"]
    assert rec["ED_ecart_T8"] <= 2e-3
    # J9⁺ : valeur atteinte ≤ valeur certifiée, donc J9⁺ ≥ J9
    assert rec["J9+"]["max"] >= rec["J9"]["max"] - 1e-12
    for cle in ("J9-P", "La-P", "A1", "A2", "J9-D", "J9-Dc", "journal_J9-P"):
        assert cle in rec


def test_nul_limite_sous_le_v9_et_au_dessus_du_v8(V):
    rec, rep = _rep_jouee(V, "Q3", 1)
    for k in range(8):
        assert rec["La"]["log_w"][k] <= rec["J8"]["log_w"][k] + 1e-6
        assert rec["La"]["log_w"][k] >= rec["J9"]["log_w"][k] - rec["ecart_residuel_La"][k] - 1e-6
    noms = [m["nom"] for m in rep.engagements["La"].engagement["bibliotheque"] if m["type"] == "ajuste_morceaux"]
    assert len(noms) == 2 and all(n.startswith("limite:seuil_fixe:") for n in noms)
    noms_d = [m["nom"] for m in rep.engagements["Ld"].engagement["bibliotheque"] if m["type"] == "ajuste_morceaux"]
    assert len(noms_d) == 5 and "limite:sous_population" in noms_d


def test_j9dc_valeur_par_coupe_egale_au_v9(V):
    rep = B.Repetition(V, RACINE_ESSAI, B.INDICE["Q4"], 2)
    rep.geler()
    rep.tirer()
    _, _, mor = B.separer(V, rep.engagements["jumeau"].engagement["bibliotheque"])
    cache = V.J.sp.Cache(rep.issues, rep.plan)
    seuils = [m for m in mor if m["partition"]["type"] == "seuil"]
    a = V.v9.detail_morceaux_groupe(seuils, cache, rep.issues, list(B.T8))
    b = V.par_coupe.detail_morceaux_par_coupe(seuils, cache, rep.issues, list(B.T8))
    for nom in a:
        for t in B.T8:
            assert a[nom][t]["valeur"] == b[nom][t]["valeur"] and max(b[nom][t]["bornes_coupes"]) == b[nom][t]["valeur"]


def test_carte_gelee_lemme_4(V):
    # Hn : moyenne glissante (fenêtre 200, lissage −70) = sans_remise [70, 70, 70] à tout instant (plancher près)
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 902)))
    y = [int(v) for v in rng.integers(0, 3, 200)]
    inst = {"z": [0.0, 0.0], "g": 0}
    sr = {"type": "sans_remise", "composition": [70, 70, 70]}
    ecart = max(abs(a - b) for t in range(200) for a, b in zip(V.J.sp.proba(B.MG_HN, inst, y, t), V.J.sp.proba(sr, inst, y, t)))
    assert ecart <= 2e-12
    # Hg sous gel : fenêtre vide au-delà de 5 pas dans le bloc → loi uniforme
    rep = B.Repetition(V, RACINE_ESSAI, B.INDICE["Hg"], 0)
    rep.geler()
    rep.tirer()
    q = rep.Qg[25 + 10]
    composante_mg = V.J.sp.proba(B.MG_HG, rep.plan[35], rep.issues[:25], 35)
    assert np.allclose(composante_mg, [1 / 3] * 3)
    assert np.allclose(q, V.J.sp.proba(rep.carte, rep.plan[35], rep.issues[:25], 35))


def test_lignes_h_bras_declares(V):
    rec, _ = _rep_jouee(V, "Hn")
    assert rec["J9-P-refus"] == {"refusee": True, "promue": False}
    assert {"terme_projete", "complet", "lineaire_seul"} <= set(rec["J9-P-nu"])
    assert {"terme_projete", "complet"} <= set(rec["J9-P-gel"])
    assert "J8" not in rec and "La" not in rec and "A1" not in rec
    rec7, _ = _rep_jouee(V, "H7")
    assert "J9" not in rec7 and rec7["J9-P-refus"]["refusee"]


def test_essais_d_egalite_en_miniature(V, tmp_path, monkeypatch):
    assert E0.essai_E0(V, RACINE_ESSAI, n=2)["passe"]
    monkeypatch.setattr(E0, "LIGNES_JUGEABLES", (B.INDICE["Q1"], B.INDICE["Hs"]))
    assert E0.essai_E9(V, RACINE_ESSAI, repetitions=1)["passe"]
    assert E0.essai_ED(V, RACINE_ESSAI, repetitions=1)["passe"]
    ep = E0.essai_EP(RACINE_ESSAI, tmp_path, n=2)
    assert ep["passe"], ep


def test_chronometrage_ecrit_des_temps_seulement(V):
    c = E0.chronometrer(V, RACINE_ESSAI, n=1, lignes=[B.INDICE["H7"]])
    t = c["secondes_par_repetition"]["H7"]
    assert set(t) == {"base", "jumeau", "J9-P", "La-P"} and all(v >= 0 for v in t.values())



# --- version 2 ------------------------------------------------------------------------------------------------------------
def test_m3_probabilite_de_carte_non_positive_refusee():
    B.probas_finies([[0.2, 0.3, 0.5]], "sain")
    with pytest.raises(GardeArret, match="strictement positive"):
        B.probas_finies([[0.0, 0.5, 0.5]], "artefact")


def test_e1_essais_d_egalite_manques_arretent(V, tmp_path, monkeypatch):
    monkeypatch.setattr(E0, "essai_E0", lambda V, r: {"passe": True})
    monkeypatch.setattr(E0, "essai_E9", lambda V, r: {"passe": True})
    monkeypatch.setattr(E0, "essai_EP", lambda r, d: {"passe": True})
    monkeypatch.setattr(E0, "essai_ED", lambda V, r: {"passe": True})
    assert set(E0.essais_d_egalite(V, RACINE_ESSAI, tmp_path)) == {"E0", "E9", "EP", "ED"}
    monkeypatch.setattr(E0, "essai_ED", lambda V, r: {"passe": False})
    with pytest.raises(GardeArret, match="ED manqué"):
        E0.essais_d_egalite(V, RACINE_ESSAI, tmp_path)


def test_declarations_m9_m10():
    d = E0.declarations_v5()
    assert d["complement_copie_v9"]["sha256"].startswith("3c9de8b8") and "v7, v8 et v9" in d["complement_copie_v9"]["remarque"]
    assert {"strates_de_rho", "mcnemar (n3)", "decomposition_du_prix (n4)"} <= set(d["lectures_de_la_lecture_gelee"])
    assert set(d["m10_empreintes_EP"]) == set(E0.FICHIERS_EP) and all(len(h) == 64 for h in d["m10_empreintes_EP"].values())
    assert "(98, r, 0)" in d["m9_graines_des_essais"] and "E9" in d["comptes_non_ecrits_par_le_texte"]
