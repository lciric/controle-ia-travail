"""Essais des épreuves de la boucle (rang 11, section 5) et du harnais simulé : cas sain qui passe, artefact refusé.
Ordre : 3, 4, 6, puis 5, 11, 12, 8, 10, 9, 2, et en dernier 1 et 13 (mode « bras de flux » planté)."""
import math

import numpy as np
import pytest

from controle_ia.audit_apres_coup_v2 import epreuves_boucle as eb
from controle_ia.audit_apres_coup_v2 import harnais_simule as hs
from controle_ia.audit_apres_coup_v2.attaque_choisie import TYPES_ILLUSTRATION
from controle_ia.audit_apres_coup_v2.estimateurs import STRATE_PLANCHER_ET_ENJEU, STRATE_PLANCHER_SEUL
from controle_ia.audit_apres_coup_v2.graines import declarer_verite, emettre_jeton
from controle_ia.audit_apres_coup_v2.oracle_simule import OracleSimule
from controle_ia.audit_apres_coup_v2.regle_audit import RegleAudit, g_identite
from controle_ia.audit_apres_coup_v2.simulateur import Monde, politique_constante, simuler
from controle_ia.gardes import GardeArret

E = 20261122


# --- harnais : provenance et interdit entier --------------------------------------------------------
def test_harnais_admet_un_monde_plante_et_refuse_le_reste():
    h = hs.HarnaisSimule()
    mg = eb.charger_monde_gaussien(h, E, 4.0, 3, 10, 16, 0)
    assert mg.X.shape == (3, 16)
    with pytest.raises(GardeArret, match="hors monde planté"):
        h.admettre(np.zeros(16).tobytes(), None)  # poids lus d'un fichier de sonde, sans jeton
    contenu, jeton = emettre_jeton(E, (40, 3, 10, 16, 0, 0), "monde_gaussien_boucle_v2",
                                   declarer_verite("f" * 64, "essais : vérité jouet"))
    with pytest.raises(GardeArret, match="hors monde planté"):
        h.admettre(bytes(len(contenu)), jeton)  # contenu réel recopié sous un jeton valide


def test_harnais_interdit_entier_par_defaut():
    h = hs.HarnaisSimule()
    with pytest.raises(GardeArret, match="interdit entier"):
        h.ajouter_lignee("v", 0)
    with pytest.raises(GardeArret, match="interdit entier"):
        h.ouvrir_lignee("v")
    assert h.etiquette == ""
    assert hs.HarnaisSimule(hs.MODE_BRAS_DE_FLUX, organismes_tenue_a_l_ecart=(),
                            organismes_jeu_final=()).etiquette == hs.ETIQUETTE_NON_EN_VIGUEUR
    with pytest.raises(GardeArret, match="aucune valeur implicite"):
        hs.HarnaisSimule(hs.MODE_BRAS_DE_FLUX)  # m-11


# --- épreuve 3 : recapture aveugle -----------------------------------------------------------------
def test_epreuve_3_monde_sans_trace_la_suite_reste_basse():
    for n, seuil in ((30, 3), (100, 5), (300, 10)):
        out = eb.epreuve_3(E, 0.0, n, rep=n)
        assert out["seuil"] == seuil and out["statut"] == "passe", out


def test_epreuve_3_ecart_4_la_suite_suit_les_rappels_des_versions():
    out = eb.epreuve_3(E, 4.0, 300, rep=1)
    assert out["statut"] == "passe", out
    assert 0.3 < out["fin_de_suite"] < 0.8


def test_epreuve_3_artefact_relecture_refusee():
    with pytest.raises(GardeArret, match="relecture refusée"):
        eb.epreuve_3_relecture(E, 0.0, 30)
    mg = eb.charger_monde_gaussien(hs.HarnaisSimule(), E, 0.0, 30, 400, 4096, 7)
    assert eb.relecture_brute(mg) > 0.95  # l'artefact est réel : 1,00 sur le monde sans trace


# --- épreuve 4 : audit orienté ---------------------------------------------------------------------
def test_epreuve_4_cas_sain_tirage_sans_egard_au_score():
    out = eb.epreuve_4(E, 0.20, 0.20, 0.20, 20_000, STRATE_PLANCHER_SEUL)
    assert out["naif"] is not None and abs(out["naif"] - 0.20) <= 4 * math.sqrt(0.16 / out["n_plancher"])


def test_epreuve_4_artefact_naif_refuse_strates_justes():
    out = eb.epreuve_4(E, 0.20, 0.05, 0.50, 40_000, STRATE_PLANCHER_SEUL)
    assert out["naif"] is None
    assert abs(out["strate_sans_score"] - 0.20) <= 4 * math.sqrt(0.16 / out["n_plancher"])
    for choix in (STRATE_PLANCHER_SEUL, STRATE_PLANCHER_ET_ENJEU):
        v = [eb.epreuve_4(E, 0.20, 0.05, 0.50, 5000, choix, tache=t) for t in range(1, 9)]
        assert all(o["choix_strate"] == choix for o in v)
        for cle in ("strate_sans_score", "pondere"):
            x = [o[cle] for o in v]
            assert abs(np.mean(x) - 0.20) <= 4 * np.std(x, ddof=1) / math.sqrt(8), (choix, cle)
    with pytest.raises(GardeArret, match="configuration"):
        eb.epreuve_4(E, 0.20, 0.05, 0.50, 1000, None)


# --- épreuve 6 : témoins ---------------------------------------------------------------------------
def test_epreuve_6_temoins_neufs():
    fa = [eb.epreuve_6(E, 4.0, 300, rep=k)["fausses_alertes_reelles"] for k in range(16)]
    assert abs(np.mean(fa) - 0.010) <= 4 * np.std(fa, ddof=1) / 4


def test_epreuve_6_artefact_temoins_de_la_lecon_refuses():
    with pytest.raises(GardeArret, match="instruire et à calibrer|non réservé"):
        eb.epreuve_6(E, 4.0, 300, calibrer_sur="lecon")
    assert eb.fausses_alertes_artefact_brut(E, 4.0, 300) > 0.15  # l'artefact est réel (0,23 au bloc A)
    reg = hs.RegistreTemoins()
    reg.reserver([1, 2], "lecon")
    with pytest.raises(GardeArret, match="instruire et à calibrer"):
        reg.reserver([2, 3], "calibrage")


# --- épreuve 5 : pli -------------------------------------------------------------------------------
def test_epreuve_5_pli_neuf_et_pli_consomme():
    out = eb.epreuve_5(E, n_choix=3, n_pli=30, R=2000)
    assert out["couverture_tient"], out
    assert 0.05 < out["relecture_du_pli_consomme_brute"] < 0.10  # optimisme 0,07 pour 0,01 (bloc C3)
    plis = hs.RegistrePlis()
    k = plis.tirer(np.arange(10), 1.0, np.random.default_rng(np.random.SeedSequence(E)))
    plis.utiliser_pour_choisir(k)
    with pytest.raises(GardeArret, match="consommé"):
        plis.annoncer(k)


# --- épreuve 7 : négatifs --------------------------------------------------------------------------
def test_epreuve_7_cas_sain_et_artefacts():
    sain = eb.table_quatre_cases("exogenes", 0.12, 0.5, 0.0, ecart_max_lecture_suspect=0.05)
    assert abs(sain["signales_parmi_endommages_caches"] - 0.010) < 1e-9
    assert abs(sain["signales_parmi_sains_du_suspect"] - 0.010) < 1e-9 and sain["mentions"] == []
    ident = eb.table_quatre_cases("exogenes", 0.12, 0.5, 6.0, ecart_max_lecture_suspect=0.05)
    assert ident["signales_parmi_sains_du_suspect"] > 0.99 and "lit le suspect" in ident["mentions"]
    cache = eb.table_quatre_cases("sains_suspect", 0.12, 0.5, 0.0, ecart_max_lecture_suspect=0.05)
    assert abs(cache["signales_parmi_endommages_caches"] - 0.0049) < 0.0008
    assert "blanchiment non mesuré" in cache["mentions"]
    for t in (sain, ident, cache):
        eb.verifier_table_quatre_cases(t)
    for t in (ident, cache):
        tronquee = dict(t, mentions=[])
        with pytest.raises(GardeArret):
            eb.verifier_table_quatre_cases(tronquee)
    with pytest.raises(GardeArret, match="déclaré"):
        eb.table_quatre_cases("exogenes", 0.12, 0.5, 0.0, ecart_max_lecture_suspect=None)


# --- épreuve 11 : canal de retour (courbe seule) ---------------------------------------------------
def test_epreuve_11_jamais_passee():
    ferme = eb.epreuve_11(E, 100, canal_ouvert=False)
    ouvert = eb.epreuve_11(E, 100, canal_ouvert=True)
    assert ferme["courbe"] > 0.1  # canal fermé : la courbe monte
    assert ouvert["compte"] <= ouvert["seuil"] and "mort" not in ouvert  # canal ouvert : reste à 0,01
    assert ferme["statut"] == ouvert["statut"] == eb.STATUT_INCOMPLETE


# --- épreuve 12 : hors couverture ------------------------------------------------------------------
def test_epreuve_12_muette_et_refus_de_rappel_retabli():
    vu = eb.epreuve_12(E, 5000, tout_cache=False)
    assert vu["statut"] == "des prises" and vu["prises"] > 0
    cache = eb.epreuve_12(E, 5000, tout_cache=True)
    assert cache["statut"] == eb.MUETTE
    with pytest.raises(GardeArret, match="rappel rétabli"):
        eb.annoncer_boucle(cache, "rappel rétabli")


# --- épreuve 8 : on ajoute -------------------------------------------------------------------------
def test_epreuve_8_on_ajoute_et_harnais_qui_remplace_meurt():
    assert eb.epreuve_8(hs.RegistreRegards(), ancien_voit_hors_oracle=False)["dommages_vus_par_un_regard"] == [2, 5]
    assert eb.epreuve_8(hs.RegistreRegards(), ancien_voit_hors_oracle=True)["dommages_vus_par_un_regard"] == [2, 5, 7]
    with pytest.raises(GardeArret, match="effacé"):
        eb.epreuve_8(eb.RegistreQuiRemplace(), ancien_voit_hors_oracle=True)


# --- épreuves 10 et 9 : plancher et oracle aveugles au moniteur ------------------------------------
M_ = Monde(50, E, TYPES_ILLUSTRATION, 1.6, politique_constante(0.02), 0.3)
R_ = RegleAudit(0.02, 0.015, 0.1, g_identite, 1.6)
O_ = OracleSimule(0.8, 0.0, 0, "signature")


def test_epreuve_10_plancher_aveugle():
    eb.epreuve_10(M_, R_, O_, 0, 4000, 3)
    with pytest.raises(GardeArret, match="permute"):
        eb.epreuve_10(M_, R_, O_, 0, 4000, 3, plancher_artefact=lambda x: np.where(x < 0.3, 0.01, 0.02))


def test_epreuve_9_oracle_aveugle():
    eb.epreuve_9(M_, R_, O_, 0, 4000, 4)
    with pytest.raises(GardeArret, match="voit le moniteur"):
        eb.epreuve_9(M_, R_, O_, 0, 4000, 4, lire_source=True)


# --- épreuve 2 : ordre -----------------------------------------------------------------------------
def test_epreuve_2_ordre():
    res = simuler(M_, R_, O_, 0, 2000)
    _, hv = res.journal.verdicts_par_episode()
    i = int(np.flatnonzero(hv >= 0)[0])
    sain = eb.ScoreConsigne(i, 0.3, eb.heure_score(i), 0)
    eb.verifier_ordre(res.journal, [sain])
    recalcule = eb.ScoreConsigne(i, 0.3, eb.heure_score(i), int(hv[i]) + 1)  # version scellée après le verdict
    with pytest.raises(GardeArret, match="postérieur"):
        eb.verifier_ordre(res.journal, [recalcule])


# --- épreuves 1 et 13 : lignée et rôle ; versions closes (bras de flux planté) ---------------------
def test_epreuve_1_cinq_refus_nommes():
    out = eb.epreuve_1(E)
    assert out["cas_sain"] == "passe" and out["etiquette"] == hs.ETIQUETTE_NON_EN_VIGUEUR
    assert sorted(out["refus"]) == [2, 3, 4, 5, 6, 7, 8]
    assert "organisme" in out["refus"][7] and "déjà en lignée" in out["refus"][8]


def test_epreuve_1_bras_a_famille_de_porte_refuse_a_la_declaration():
    h = eb.harnais_plante(E)
    with pytest.raises(GardeArret, match="famille d'une porte"):
        h.declarer_bras(hs.DeclarationBrasDeFlux("flux_X", frozenset({"org_flux"}), frozenset({"porte_A"}), 0))
    with pytest.raises(GardeArret, match="interdit entier"):
        hs.HarnaisSimule().declarer_bras(hs.DeclarationBrasDeFlux("f", frozenset(), frozenset({"x"}), 0))


def test_epreuve_1_clause_2_score_non_consigne_avant_le_verdict():
    h = eb.harnais_plante(E)
    h.sceller_version(b"en place", horloge=2)
    eb._episode(h, E, 1, "flux", "flux_F", bras="flux_1")
    h.rendre_verdict(1, horloge=13)
    h.ouvrir_lignee("v1")
    with pytest.raises(GardeArret, match="clause 2"):
        h.ajouter_lignee("v1", 1)


def test_epreuve_13_versions_closes():
    out = eb.epreuve_13(E)
    assert out["compte_servi"] == 1 and out["lectures_comptees"] == ["lot_1"]
    assert sorted(out["refus"]) == ["poids", "reconception", "scores_par_episode", "seuil"]
    assert out["reconception_hors_flux"].startswith("reconception admise")


# --- mutations survivantes de la contre-lecture v1 (une par mutation) ------------------------------
def test_mutation_relecture_dans_la_suite_de_l_epreuve_3(monkeypatch):
    """Si la version qui note l'épisode i est instruite sur l'épisode i lui-même, la garde branchée sur le calcul doit
    lever le refus nommé de relecture (et non la seule mort binomiale du monde sans trace)."""
    monkeypatch.setattr(eb, "lignee_version", lambda i: np.arange(0, i + 1))
    with pytest.raises(GardeArret, match="relecture refusée"):
        eb.epreuve_3(E, 4.0, 30, rep=3)


def test_mutation_score_consigne_apres_le_verdict():
    h = eb.harnais_plante(E)
    v0 = h.sceller_version(b"en place", horloge=2)
    eb._episode(h, E, 1, "flux", "flux_F", bras="flux_1")
    h.rendre_verdict(1, 13)
    with pytest.raises(GardeArret, match="clause 2 \\(i\\)"):
        h.consigner_score(1, v0, horloge=14)


def test_epreuve_1_revérification_au_scellement():
    """I-2 : un épisode de verdict de la famille d'un épisode d'une lignée encore ouverte est refusé à
    l'enregistrement ; le scellement revérifie la lignée."""
    h = eb.harnais_plante(E)
    v0 = h.sceller_version(b"en place", horloge=2)
    eb._episode(h, E, 1, "flux", "flux_F", bras="flux_1")
    h.consigner_score(1, v0, horloge=11)
    h.rendre_verdict(1, horloge=13)
    h.ouvrir_lignee("v1")
    h.ajouter_lignee("v1", 1)
    with pytest.raises(GardeArret, match="déjà en lignée"):
        eb._episode(h, E, 2, "verdict", "autre", organisme="org_flux")
