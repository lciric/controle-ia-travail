"""Idée 1.1 (préenregistrement scellé `3ffe1739…`) — chaque ligne de la liste d'arrêt avec un cas sain et un artefact (R5),
garde P4 sous ses deux formes, ordre du gel, journal empreinté avant le tirage, mêmes issues pour tous les bras. Racine
d'essai distincte de celle du jeu. Aucun repli silencieux : toute garde lève `GardeArret`."""
import hashlib
import json
import math
import shutil
import socket
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
from controle_ia.organisme_idees_juge import banc_idee_1_1_v2 as B
from controle_ia.organisme_idees_juge import etape0_idee_1_1_v5 as E0
from controle_ia.organisme_idees_juge import execution_idee_1_1_v5 as X
from controle_ia.organisme_idees_juge import execution_v1 as X1
from controle_ia.organisme_idees_juge import projection_bras_v1 as PB
from controle_ia.organisme_idees_juge import vue_v9_v2 as VV

RACINE_DEPOT = Path(__file__).resolve().parents[1]
RACINE_ESSAI = int(hashlib.sha256(b"essais idee 1.1 v1, gardes").hexdigest(), 16)


@pytest.fixture(scope="module")
def V():
    return VV.charger()


def test_racine_d_essai_distincte_du_jeu():
    assert RACINE_ESSAI != B.racine_de(B.EMPREINTE_PREREG)


# --- préalables, copies, fichiers gelés -------------------------------------------------------------------------------------
def test_prealable_2_sain_et_artefact(monkeypatch):
    assert len(E0.prealable_2()) == 2
    monkeypatch.setattr(E0, "EMPREINTE_PREUVE_V3", "0" * 64)
    with pytest.raises(GardeArret, match="préalable 2"):
        E0.prealable_2()


def test_copie_nul_v9_empreinte_fausse_refusee(tmp_path):
    VV.verifier_copie_v9()
    d = tmp_path / "copie"
    shutil.copytree(VV.DOSSIER_V9, d)
    p = d / "orchestrator/pole/nul_v9.py"
    p.write_bytes(p.read_bytes() + b"\n")
    with pytest.raises(GardeArret, match="7ae450df"):
        VV.verifier_copie_v9(d)


def test_noms_empruntes_condition_a(V, monkeypatch):
    assert VV.exiger_noms_empruntes(V.J) == 16
    monkeypatch.delattr(V.J.sp, "calibrer")
    with pytest.raises(GardeArret, match="préalable 1"):
        VV.exiger_noms_empruntes(V.J)


def test_vue_hors_du_depot_seulement(tmp_path):
    with pytest.raises(GardeArret, match="sous le dépôt"):
        VV.assembler_vue(RACINE_DEPOT / "vue-interdite")
    assert not (RACINE_DEPOT / "vue-interdite").exists()


def _addendum(tmp_path, lignes: str, programme: dict | None):
    texte = "# addendum d'essai\n\n```\n" + lignes + "```\n"
    if programme is not None:
        texte += X.DEBUT_PROGRAMME + "\n```json\n" + json.dumps(programme) + "\n```\n" + X.FIN_PROGRAMME + "\n"
    p = tmp_path / "addendum.md"
    p.write_text(texte, encoding="utf-8")
    sceller(p)
    return p


def _etape0_factice(tmp_path, secondes=1.0, bloquants=(), fichiers=None, texte=None, sans=()):
    temps = {n: {"base": secondes, "jumeau": 0.0, "J9-P": 0.0, "La-P": 0.0} for n in B.NOMS}
    fg = fichiers if fichiers is not None else {l.split("  ")[1]: l.split("  ")[0] for l in X.lister_empreintes(RACINE_DEPOT).splitlines()}
    res = {"chronometrage": {"secondes_par_repetition": temps}, "bloquants": list(bloquants), "jeu_permis": not bloquants,
           "preenregistrement": {"sha256": texte or B.EMPREINTE_PREREG}}
    corps = {"resultat": res, "fichiers_geles": fg}
    for cle in sans:
        (res if cle in res else corps).pop(cle)
    p = tmp_path / "etape0.json"
    p.write_text(json.dumps(corps), encoding="utf-8")
    return p, sceller(p)


def test_addendum_sain_et_artefacts(tmp_path):
    lignes = X.lister_empreintes(RACINE_DEPOT)
    e0, h0 = _etape0_factice(tmp_path)
    regle = E0.regle_de_reduction(json.loads(e0.read_text())["resultat"]["chronometrage"]["secondes_par_repetition"], 3)
    prog = {"processus": 3, "reductions": regle["reductions"], "etape0": {"chemin": str(e0), "sha256": h0}}
    a = X.lire_addendum(RACINE_DEPOT, _addendum(tmp_path, lignes, prog))
    assert a["programme"]["reductions"] == []
    # artefacts : fichier gelé absent de la liste ; empreinte fausse ; bloc programme absent ; réduction hors règle ;
    # étape 0 avec bloquants
    for nom, (lig, pr) in {"absent": (lignes.split("\n", 1)[1], prog),
                           "faux": ("0" * 64 + lignes[64:], prog), "sans programme": (lignes, None),
                           "reduction": (lignes, {**prog, "reductions": [1]})}.items():
        d = tmp_path / nom
        d.mkdir()
        with pytest.raises(GardeArret):
            X.lire_addendum(RACINE_DEPOT, _addendum(d, lig, pr))
    d = tmp_path / "bloquant"
    d.mkdir()
    e1, h1 = _etape0_factice(d, bloquants=["une mutation survit : pas de jeu"])
    with pytest.raises(GardeArret, match="bloquants"):
        X.lire_addendum(RACINE_DEPOT, _addendum(d, lignes, {**prog, "etape0": {"chemin": str(e1), "sha256": h1}}))


def test_bloquants_de_l_etape0_sain_et_artefacts():
    sain = {"prealable_1": {"c_rejeu": {"classement": {"passe": True, "raison": ""}}},
            **{e: {"passe": True} for e in ("E0", "E9", "EP", "ED")},
            "mutations": {"toutes_tuees": True, "cas_sains_passes": True}, "garde_P4": {"verdict": {"bloque_le_jeu": False}},
            "programme": {"jeu_permis": True}}
    assert E0.bloquants(sain) == []
    for cle, chemin in (("E0", ("E0", "passe")), ("ED", ("ED", "passe")), ("mut", ("mutations", "toutes_tuees")),
                        ("sain", ("mutations", "cas_sains_passes")), ("duree", ("programme", "jeu_permis"))):
        r = json.loads(json.dumps(sain))
        r[chemin[0]][chemin[1]] = False
        assert E0.bloquants(r), cle
    r = json.loads(json.dumps(sain))
    r["garde_P4"]["verdict"]["bloque_le_jeu"] = True
    assert E0.bloquants(r)


def test_rejeu_classement_sain_et_artefacts():
    ok = {"import": "ok", "essais": [{"id": f"x.{c}.t", "classe": c, "statut": "passe"} for c in E0.CLASSES_ATTENDUES_REJOUABLES]}
    assert E0.classer_rejeu(ok)["passe"]
    r = json.loads(json.dumps(ok))
    r["essais"][0]["statut"] = "echoue"
    assert not E0.classer_rejeu(r)["passe"]                                  # essai d'origine en échec : pas de jeu
    r = json.loads(json.dumps(ok))
    r["essais"].append({"id": "x.GrainesEtPreenregistrement.t", "classe": "GrainesEtPreenregistrement", "statut": "echoue"})
    c = E0.classer_rejeu(r)
    assert not c["passe"] and c["reecriture_exigee_absente"]                 # à défaut sans réécriture : pas de jeu
    assert not E0.classer_rejeu({"import": "Traceback…", "essais": []})["passe"]
    assert not E0.classer_rejeu(ok, filtre=("MembresNulV9",))["passe"]       # un rejeu partiel n'est jamais le préalable


# --- ordre du gel, issues, journal ------------------------------------------------------------------------------------------
def test_issue_fraiche_avant_le_gel_refusee(V):
    rep = B.Repetition(V, RACINE_ESSAI, B.INDICE["Q2"], 0)
    with pytest.raises(GardeArret, match="avant le gel"):
        rep.tirer()


def test_engagement_bati_apres_le_flux_refuse(V):
    rep = B.Repetition(V, RACINE_ESSAI, B.INDICE["Hs"], 0)
    rep.geler()
    rep.tirer()
    with pytest.raises(GardeArret, match="après la création du flux"):
        rep.construire_engagement("J9")


def test_journal_empreinte_avant_creation_du_flux_et_gel_par_bloc(V, monkeypatch):
    vus = []
    origine = PB.FluxFrais.__init__

    def espion(self, tireur):
        vus.append(dict(rep.enregistrement))
        origine(self, tireur)
    monkeypatch.setattr(PB.FluxFrais, "__init__", espion)
    rep = B.Repetition(V, RACINE_ESSAI, B.INDICE["Q1"], 1)
    rep.geler()
    rep.tirer()
    assert len(vus) == 1 and len(vus[0]["journal_gel"]["J9-P"]) == 8 and len(vus[0]["journal_gel"]["La-P"]) == 8
    rep2 = B.Repetition(V, RACINE_ESSAI, B.INDICE["Hs"], 1)
    rep2.geler()
    rep2.tirer()
    j = rep2.enregistrement["journal_gel_par_bloc"]
    assert [x["issues_recues"] for x in j] == [25 * b for b in range(8)]


def test_projection_d_une_carte_sans_memoire_apres_le_flux_refusee(V):
    rep = B.Repetition(V, RACINE_ESSAI, B.INDICE["Q1"], 2)
    rep.geler()
    rep.tirer()
    with pytest.raises(PB.GardeAcces):
        rep._projeter_au_gel()


def test_memes_issues_pour_tous_les_bras_sain_et_artefact(V, monkeypatch):
    rep = B.Repetition(V, RACINE_ESSAI, B.INDICE["Q3"], 0)
    rep.geler()
    rep.tirer()
    t = {q: rep.tirages_de(q)["issues"] for q in rep.engagements}
    assert all(v == rep.issues for v in t.values())
    origine = B.Repetition.tirages_de
    monkeypatch.setattr(B.Repetition, "tirages_de",
                        lambda self, q: {**origine(self, q), "issues": [(y + 1) % 3 for y in self.issues]} if q == "Ld" else origine(self, q))
    with pytest.raises(GardeArret, match="issues différents de J9"):
        rep.evaluer()


def test_memes_issues_quels_que_soient_les_bras(V):
    a = B.Repetition(V, RACINE_ESSAI, B.INDICE["Q2"], 3)
    b = B.Repetition(V, RACINE_ESSAI, B.INDICE["Q2"], 3, actifs=())
    for r in (a, b):
        r.geler()
        r.tirer()
    assert a.issues == b.issues


# --- lois de carte, fractions, certificats ------------------------------------------------------------------------------
def test_loi_de_carte_exception_ou_non_finie(V):
    inst = {"z": [0.1, -0.2], "g": 0}
    assert len(B.proba_carte(V.J, B.MG_HG, inst, [0, 1], 2, "sain")) == 3
    with pytest.raises(GardeArret, match="division par zéro"):
        B.proba_carte(V.J, {"type": "moyenne_glissante", "nombre_issues": 3, "fenetre": 5, "lissage": 0.0}, inst, [], 0, "artefact")
    with pytest.raises(GardeArret, match="non finie"):
        B.probas_finies([0.5, float("nan"), 0.5], "artefact")
    B.verifier_moyenne_glissante(B.MG_HN)
    with pytest.raises(GardeArret):
        B.verifier_moyenne_glissante({"type": "moyenne_glissante", "nombre_issues": 2, "fenetre": 8, "lissage": -1.0})


def test_engagement_avec_fractions_refuse(V):
    rep = B.Repetition(V, RACINE_ESSAI, B.INDICE["Q1"], 4)
    g = rep.construire_engagement("J9")
    B.gardes_d_evaluation(V, g, {"empreinte_engagement": g.empreinte, "issues": [0] * 200, "plan_execution": "ordre_naturel"})
    e = dict(g.engagement, fractions=[0.25, 0.5, 0.75, 1.0])
    gf = V.J.sp.geler_engagement(e)
    with pytest.raises(GardeArret, match="fractions"):
        B.gardes_d_evaluation(V, gf, {"empreinte_engagement": gf.empreinte, "issues": [0] * 200, "plan_execution": "ordre_naturel"})


def test_carte_qui_lit_l_historique_sans_forme_de_garde(V):
    assert B.lit_historique(V.J, {"type": "sans_remise", "composition": [70, 70, 70]})
    assert B.lit_historique(V.J, B.CarteMemoire())
    assert not B.lit_historique(V.J, {"type": "fixe", "probas": [1, 1, 1]})
    with pytest.raises(GardeArret, match="sans forme de la garde P4"):
        PB.exiger_garde(True, None, True)


def test_loi_connue_qui_lit_l_historique_refusee(V, monkeypatch):
    B.Repetition(V, RACINE_ESSAI, B.INDICE["Q1"], 5)
    origine = B.construire_archive

    def archive_a_memoire(rng):
        a = origine(rng)
        a["S3"] = {"type": "moyenne_glissante", "nombre_issues": 3, "fenetre": 5, "lissage": 0.5}
        return a
    monkeypatch.setattr(B, "construire_archive", archive_a_memoire)
    with pytest.raises(GardeArret, match="P6"):
        B.Repetition(V, RACINE_ESSAI, B.INDICE["Q1"], 5)


# --- évaluations : log W non fini, monotonie, nichage, domination ------------------------------------------------------------
def test_log_w_non_fini_arrete():
    assert B._resume([0.0, 1.0], ["a", "b"])["max"] == 1.0
    with pytest.raises(GardeArret, match="non fini"):
        B._resume([0.0, math.nan], ["a", "b"])


def _s(**kw):
    base = {"J8": [1.0] * 8, "J9": [0.5] * 8, "La": [0.8] * 8, "Ld": [0.7] * 8, "g_La": [1e-4] * 8, "g_Ld": [1e-4] * 8}
    base.update(kw)
    return base


@pytest.mark.parametrize("s,motif", [(_s(J9=[1.1] * 8), "monotonie"), (_s(La=[1.0 + 2e-6] * 8, Ld=[0.9] * 8), "monotonie"),
                                     (_s(La=[0.4] * 8), "nichage"), (_s(Ld=[0.3] * 8), "nichage"),
                                     (_s(Ld=[0.9] * 8, La=[0.8] * 8), "nichage")])
def test_monotonie_et_nichage(s, motif):
    B.verifier_monotonie_et_nichage(_s())
    with pytest.raises(GardeArret, match=motif):
        B.verifier_monotonie_et_nichage(s)


def test_domination():
    B.verifier_domination(True, True, True)
    B.verifier_domination(False, False, True)
    with pytest.raises(GardeArret, match="domination"):
        B.verifier_domination(True, False, True)
    with pytest.raises(GardeArret, match="domination"):
        B.verifier_domination(False, True, False)
    assert B.regle_j9d([0.0] * 7 + [B.SEUIL], [0.0] * 40, {"m": [0.0] * 40}) == (True, False, True)


# --- durée, réductions, réseau, lecture avant scellement --------------------------------------------------------------------
def test_reductions_dans_l_ordre_seulement():
    assert "jumeau" in B.actifs_pour(B.LIGNES_V[0], 999, ())
    assert "jumeau" not in B.actifs_pour(B.LIGNES_V[0], 300, (1, 2, 3))
    assert "jumeau" in B.actifs_pour(B.INDICE["Q1"], 999, (1, 2, 3, 4, 5))       # réductions sur les seules lignes V
    assert "J9-P" not in B.actifs_pour(B.INDICE["Q9a"], 600, (1, 2, 3, 4))
    for mauvaise in ((2,), (1, 3), (1, 2, 2), (6,), (5, 4, 3, 2, 1)):
        with pytest.raises(GardeArret, match="hors de la règle"):
            B.actifs_pour(0, 0, mauvaise)


def test_regle_de_reduction_et_duree_attendue():
    petit = {n: {"base": 1.0, "jumeau": 1.0, "J9-P": 0.5, "La-P": 0.1} for n in B.NOMS}
    r = E0.regle_de_reduction(petit, 3)
    assert r["reductions"] == [] and r["jeu_permis"] and r["D_h"] == pytest.approx(30 * 1000 * 2.6 / 3 / 3600)
    moyen = {n: {"base": 7.0, "jumeau": 5.0, "J9-P": 0.5, "La-P": 0.1} for n in B.NOMS}
    r = E0.regle_de_reduction(moyen, 3)
    assert r["reductions"] == [1, 2] and r["D_h"] <= 32 and r["trace"][0]["D_h"] > 32
    grand = {n: {"base": 20.0, "jumeau": 1.0, "J9-P": 0.5, "La-P": 0.1} for n in B.NOMS}
    r = E0.regle_de_reduction(grand, 3)
    assert r["reductions"] == [1, 2, 3, 4, 5] and not r["jeu_permis"]
    with pytest.raises(GardeArret, match="incomplet"):
        E0.regle_de_reduction({"Q1": petit["Q1"]}, 3)
    with pytest.raises(GardeArret):
        E0.duree_attendue_h(petit, (), 4)


def test_duree_murale_48_h():
    h = [0.0]
    g = X.GardeDuree(0.0, horloge=lambda: h[0])
    h[0] = 48 * 3600 - 1
    g.verifier("sain")
    h[0] = 48 * 3600 + 1
    with pytest.raises(GardeArret, match="48 h"):
        g.verifier("artefact")


def test_appel_reseau_interdit():
    anciens = X.installer_garde_reseau()
    try:
        with pytest.raises(GardeArret, match="réseau"):
            socket.create_connection(("192.0.2.1", 80), timeout=0.01)
    finally:
        X1.retirer_garde_reseau(anciens)
    assert socket.create_connection is not X1._refus_reseau


def test_lecture_avant_scellement_refusee(tmp_path):
    d = tmp_path / "run"
    (d / "lignes").mkdir(parents=True)
    (d / "sortie.json").write_text("{}", encoding="utf-8")
    with pytest.raises(GardeArret):
        X.charger_sortie(d)
    (d / "arret.json").write_text("{}", encoding="utf-8")
    with pytest.raises(GardeArret, match="arrêt consigné"):
        X.charger_sortie(d)



# --- version 2 : M1, M2, m2, m8 -------------------------------------------------------------------------------------------
def _prog(tmp_path, **kw):
    e0, h0 = _etape0_factice(tmp_path, **kw)
    return {"processus": 3, "reductions": [], "etape0": {"chemin": str(e0), "sha256": h0}}


def test_m2_etape0_liee_au_code_gele_fichier_par_fichier(tmp_path):
    lignes = X.lister_empreintes(RACINE_DEPOT)
    X.lire_addendum(RACINE_DEPOT, _addendum(tmp_path, lignes, _prog(tmp_path)))
    fg = {l.split("  ")[1]: l.split("  ")[0] for l in lignes.splitlines()}
    cas = {"autre code": {"fichiers": {**fg, X.FICHIERS_GELES[3]: "0" * 64}},
           "liste incomplète": {"fichiers": {k: v for k, v in fg.items() if k != X.FICHIERS_GELES[0]}},
           "autre texte": {"texte": "1" * 64},
           "sans bloquants (m2)": {"sans": ("bloquants",)}, "sans fichiers gelés (m2)": {"sans": ("fichiers_geles",)},
           "sans jeu_permis (m2)": {"sans": ("jeu_permis",)}}
    for nom, kw in cas.items():
        d = tmp_path / nom.replace(" ", "-")
        d.mkdir()
        with pytest.raises(GardeArret):
            X.lire_addendum(RACINE_DEPOT, _addendum(d, lignes, _prog(d, **kw)))


def test_m1_la_lecture_relit_l_addendum_du_manifeste(tmp_path):
    lignes = X.lister_empreintes(RACINE_DEPOT)
    prog = _prog(tmp_path)
    a = _addendum(tmp_path, lignes, prog)
    from controle_ia.scellement import empreinte
    config = {"addendum": {"chemin": str(a), "sha256": empreinte(a), "programme": prog}}
    X.verifier_addendum_du_manifeste(RACINE_DEPOT, config)
    with pytest.raises(GardeArret, match="sans addendum"):
        X.verifier_addendum_du_manifeste(RACINE_DEPOT, {})
    with pytest.raises(GardeArret, match="différent"):
        X.verifier_addendum_du_manifeste(RACINE_DEPOT, {"addendum": {**config["addendum"], "sha256": "0" * 64}})
    with pytest.raises(GardeArret, match="programme"):
        X.verifier_addendum_du_manifeste(RACINE_DEPOT, {"addendum": {**config["addendum"], "programme": {**prog, "processus": 2}}})
    d = tmp_path / "faux"
    d.mkdir()
    a2 = _addendum(d, "0" * 64 + lignes[64:], prog)      # un fichier gelé modifié après le jeu : la lecture refuse
    with pytest.raises(GardeArret):
        X.verifier_addendum_du_manifeste(RACINE_DEPOT, {"addendum": {"chemin": str(a2), "sha256": empreinte(a2), "programme": prog}})


def test_m8_reprise_tolere_les_seuls_dossiers_du_run(depot):
    run = "20261116-000000-" + X.NOM_RUN
    (depot / "runs" / run).mkdir(parents=True)
    (depot / "runs" / run / "manifeste.json").write_text("{}")
    (depot / X.DOSSIER_DIAG / run / "lignes").mkdir(parents=True)
    (depot / X.DOSSIER_DIAG / run / "lignes" / "00-0000.json").write_text("{}")
    X.exiger_depot_propre_sauf_run(depot, run)
    (depot / "autre.txt").write_text("x")
    with pytest.raises(GardeArret, match="reprise refusée"):
        X.exiger_depot_propre_sauf_run(depot, run)
    (depot / "autre.txt").unlink()
    (depot / "runs" / "20261116-000001-autre").mkdir()
    (depot / "runs" / "20261116-000001-autre" / "m.json").write_text("{}")
    with pytest.raises(GardeArret):
        X.exiger_depot_propre_sauf_run(depot, run)



# --- version 5 : vue v2 -------------------------------------------------------------------------------------------------
def test_v5_vue_porte_le_complement_et_le_verifie(tmp_path):
    attendu = VV.fichiers_de_la_vue()
    assert "pole/attaque_goodhart_v2.py" in attendu and attendu["pole/attaque_goodhart_v2.py"][1].startswith("3c9de8b8")
    assert VV.verifier_copie_v9()["orchestrator/pole/attaque_goodhart_v2.py"] == VV.COMPLEMENT_V3["sha256"]
    d = tmp_path / "copie"
    shutil.copytree(VV.DOSSIER_V9, d)
    p = d / "orchestrator/pole/attaque_goodhart_v2.py"
    p.write_bytes(p.read_bytes() + b"\n")
    with pytest.raises(GardeArret, match="attaque_goodhart_v2"):
        VV.verifier_copie_v9(d)
