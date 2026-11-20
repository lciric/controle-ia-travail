"""Essais des outils : lois (contre l'évaluateur de l'organisme), comparateur (table du palier 0a), test exact (énumération
complète et table du § 3.3 du plan ; garde 21), intervalle binomial (calcul des ordres de grandeur v2), règle de confirmation
(garde 26, comptes plantés), graines (dérivation, couches disjointes, refus des couches décisives, garde 20), S9 (table du
calcul v2)."""

import hashlib
import itertools
import os
import random
import runpy

import numpy as np
import pytest

from aides_heritage_etage_processeur_v1 import copie_organisme, depot, lire_json
from controle_ia.heritage_etage_processeur_v1 import analyse as AN
from controle_ia.heritage_etage_processeur_v1 import audit as AU
from controle_ia.heritage_etage_processeur_v1 import comparateur as C
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import intervalles as IV
from controle_ia.heritage_etage_processeur_v1 import lois as L
from controle_ia.heritage_etage_processeur_v1 import rangs_signes as RS


# --- lois ---------------------------------------------------------------------------------------------------------------


def _lois_de_chaque_type(rng):
    s1, s2 = L.softmax_aleatoire(rng), L.softmax_aleatoire(rng)
    return [
        {"type": "fixe", "probas": [0.2, 0.5, 0.3]},
        s1,
        L.loi_par_sous_population(s1, s2),
        {"type": "melange", "poids": [0.3, 0.7], "composantes": [s1, s2]},
        {"type": "si_sinon", "condition": {"indice": 1, "seuil": 0.2}, "si": s1, "sinon": s2},
        {"type": "si_sinon", "condition": {"sous_population": 1}, "si": s2, "sinon": s1},
        {"type": "transformee", "base": s1, "puissance": 1.25, "inclinaison": [0.0, 0.3, -0.2],
         "melange_aveugle": {"lambda": 0.1, "probas": [0.3, 0.3, 0.4]},
         "oscillation": {"amplitude": 0.5, "frequence": 2.0, "trait": 0, "issue": 2, "phase": 0.1}},
    ]


def test_matrice_egale_proba_et_l_evaluateur_de_l_organisme():
    ev = runpy.run_path(os.path.join(copie_organisme(), "pole", "evaluateur_lois_v62.py"))
    rng = np.random.default_rng(1)
    inst = L.tirer_instances_organisme(random.Random(3), 300)
    Z, G = L.instances_en_tableaux(inst)
    for loi in _lois_de_chaque_type(rng):
        M = L.matrice(loi, Z, G)
        P = np.array([L.proba(loi, x) for x in inst])
        E = np.array([ev["proba"](loi, x) for x in inst])
        assert np.max(np.abs(M - P)) < 1e-12
        assert np.array_equal(P, E), loi["type"]


def test_composition_par_sous_population_admise_par_la_grammaire():
    """Réserve de faisabilité (B1) : la composition reprend A sur g = 0 et B sur g = 1, sous la forme unique."""
    rng = np.random.default_rng(2)
    a, b = L.loi_aleatoire(rng), L.loi_aleatoire(rng)
    c = L.composer(a, b)
    assert c["type"] == "par_sous_population" and sorted(c["lois"]) == ["0", "1"]
    for x in L.tirer_instances_organisme(random.Random(4), 200):
        assert L.proba(c, x) == (L.proba(a, x) if x["g"] == 0 else L.proba(b, x))


def test_evaluateur_de_l_audit_ecrit_a_part_egal_a_l_oracle():
    """L'audit ne partage rien avec la construction : sa seconde écriture rend les mêmes divergences à 1e-12 près, et refuse
    toute loi hors de la forme unique."""
    rng = np.random.default_rng(7)
    Z, G = L.instances_oracle(12345, 4000)
    o = C.Oracle(Z, G)
    for _ in range(10):
        a, b = L.loi_aleatoire(rng), L.loi_aleatoire(rng)
        assert abs(AU.kl_moyenne(AU.probas_audit(a, Z, G), AU.probas_audit(b, Z, G)) - o.divergence(a, b)) < 1e-12
    with pytest.raises(AU.AuditRefuse):
        AU.probas_audit(L.softmax_aleatoire(rng), Z, G)


# --- comparateur : la table du palier 0a ----------------------------------------------------------------------------------


def test_comparateur_redonne_la_table_du_palier_0a():
    sortie = lire_json(depot("palier-0a", "essai-palier-0a-sortie-v1.json"))
    monde = {x["identifiant"]: x["loi_predictive"] for x in
             lire_json(os.path.join(copie_organisme(), "exemples", "temoins-pari-demo-v1.json"))["fiches"]}
    v = monde["S-V1"]
    anti = {"type": "softmax", "poids": [[-w for w in ligne] for ligne in v["poids"]], "biais": list(v["biais"])}
    plantees = {"S-V1 (vraie)": v, "S-F1 (fausse)": monde["S-F1"], "S-F2 (fausse)": monde["S-F2"],
                "S-F4 (fausse)": monde["S-F4"]}
    tentatives = {"P-V1": v, "P-F1": monde["S-F1"], "P-F2": monde["S-F2"], "P-F4": monde["S-F4"], "P-ANTI": anti,
                  "P-V1-SEUIL-INTENABLE": v}
    Z, G = L.instances_oracle(C.graine_de_tache_organisme(sortie["racine_des_graines"], "oracle|instances"), 4000)
    oracle = C.Oracle(Z, G)
    vues = 0
    for ligne in sortie["comparateur"]:
        if "divergence_moyenne_nat_par_loi_plantee" not in ligne:
            continue
        loi = tentatives[ligne["tentative"]]
        div = {nom: round(oracle.divergence(lp, loi), 9) for nom, lp in plantees.items()}
        assert div == ligne["divergence_moyenne_nat_par_loi_plantee"], ligne["tentative"]
        assert sorted(n for n, d in div.items() if d <= 0.05) == ligne["appariee_a"]
        vues += 1
    assert vues == 6


# --- test exact ---------------------------------------------------------------------------------------------------------


def _p_par_enumeration(d):
    """Écriture indépendante : rangs moyens par comptage (zéros compris), énumération des 2^n signes des non nuls."""
    a = [abs(x) for x in d]
    rangs = [sum(1 for y in a if y < x) + (sum(1 for y in a if y == x) + 1) / 2.0 for x in a]
    nn = [(r, x > 0) for r, x in zip(rangs, d) if x != 0]
    if not nn:
        return 1.0, 1.0
    t = sum(r for r, p in nn if p)
    total, haut, bas = 0, 0, 0
    for signes in itertools.product((False, True), repeat=len(nn)):
        s = sum(r for (r, _), p in zip(nn, signes) if p)
        total += 1
        haut += s >= t - 1e-9
        bas += s <= t + 1e-9
    return min(1.0, 2 * min(haut, bas) / total), haut / total


def test_test_exact_egal_a_l_enumeration_complete_zeros_et_ex_aequo():
    rng = np.random.default_rng(5)
    for n in range(1, 13):
        for _ in range(25):
            d = rng.integers(-3, 4, n).astype(float)
            p2, p1 = _p_par_enumeration(d.tolist())
            assert abs(RS.valeur_p_bilaterale(d) - p2) < 1e-12, d
            assert abs(RS.valeur_p_unilaterale(d) - p1) < 1e-12, d


def _vecteur(n, somme_negative):
    neg, reste = set(), somme_negative
    for r in range(n, 0, -1):
        if r <= reste:
            neg.add(r)
            reste -= r
    assert reste == 0
    return [(-r if r in neg else r) for r in range(1, n + 1)]


TABLE_3_3 = {5: (0.0625, None, None, 0.03125, 0), 6: (0.03125, None, 0, 0.015625, 2), 7: (0.015625, 0, 2, 0.0078125, 3),
             8: (0.0078125, 2, 3, 0.00390625, 5), 10: (0.001953125, 5, 8, 0.0009765625, 10),
             12: (0.00048828125, 10, 13, 0.000244140625, 17), 16: (0.000030517578125, 25, 29, 0.0000152587890625, 35)}


def _plus_grande_somme(n, alpha, unilateral=False):
    meilleur = None
    for w in range(0, n * (n + 1) // 2 + 1):
        d = _vecteur(n, w)
        p = RS.valeur_p_unilaterale(d) if unilateral else RS.valeur_p_bilaterale(d)
        if p <= alpha:
            meilleur = w
        else:
            break
    return meilleur


def test_test_exact_contre_la_table_du_plan():
    for n, (p_min, w025, w05, p_min_uni, w_uni) in TABLE_3_3.items():
        tout_positif = list(range(1, n + 1))
        assert RS.valeur_p_bilaterale(tout_positif) == p_min
        assert RS.valeur_p_unilaterale(tout_positif) == p_min_uni
        assert _plus_grande_somme(n, 0.025) == w025
        assert _plus_grande_somme(n, 0.05) == w05
        assert _plus_grande_somme(n, 0.05, unilateral=True) == w_uni


def _p_zeros_retires_avant(d):
    """Artefact de la garde 21 : une version fautive qui retire les zéros avant de classer."""
    return _p_par_enumeration([x for x in d if x != 0])[0]


def test_garde_21_cas_sain_et_zeros_retires_avant_de_classer_detectes():
    d = [0, 0, 1, 2, -3, 4, 5, 6, 7]  # Pratt : 2 × 4/128 = 0,0625 ; zéros retirés avant : 2 × 5/128 = 0,078125
    assert RS.valeur_p_bilaterale(d) == 0.0625
    assert _p_zeros_retires_avant(d) == 0.078125
    assert RS.valeur_p_bilaterale(d) != _p_zeros_retires_avant(d)
    assert RS.valeur_p_bilaterale([0, 0, 0]) == 1.0


def test_holm_et_lecture():
    assert RS.holm(0.02, 0.04) == (True, True)
    assert RS.holm(0.02, 0.06) == (True, False)
    assert RS.holm(0.03, 0.04) == (False, False)
    assert RS.holm(0.04, 0.01) == (True, True)
    assert RS.holm(0.06, 0.01) == (False, True)
    assert RS.lecture_contraste(True, [1, 2, 3], [0, 0, 0]) == "établi"
    assert RS.lecture_contraste(True, [1, 2, 3], [2, 2, 2]) == "non lu comme succès"
    assert RS.lecture_contraste(True, [1, 2, 3], [1, 1, 1]) == "établi"
    assert RS.lecture_contraste(True, [1, 1, 1], [1, 1, 1]) == "non lu comme succès"  # médiane fausse non < médiane M1
    assert RS.lecture_contraste(True, [-1, -2, -3], [0, 0, 0]) == "effet négatif établi"
    assert RS.lecture_contraste(False, [1, 2, 3], [0, 0, 0]) == "non établi"


def test_point_4_part_de_zeros_compte_exact_sur_un_vecteur_plante():
    assert RS.part_de_zeros([0, 1, 0, -2, 0, 3, 4, 0]) == 0.5


# --- intervalles et règle de confirmation -----------------------------------------------------------------------------------


def test_intervalle_binomial_contre_le_calcul_des_ordres_de_grandeur_v2():
    v2 = lire_json(depot("palier-0b", "calcul-ordres-de-grandeur-palier-0b-v2.json"))
    for k, attendu in v2["intervalles_a_95_pour_cent"].items():
        assert IV.clopper_pearson(int(k), 10_000, arrondi=5) == attendu, k
    assert IV.clopper_pearson(553, 10_000)[1] <= 0.06 < IV.clopper_pearson(554, 10_000)[1]
    assert v2["plus_grand_compte_dont_la_borne_haute_est_au_plus_0_06"] == 553
    assert IV.clopper_pearson(7981, 10_000)[0] >= 0.79 > IV.clopper_pearson(7980, 10_000)[0]
    assert v2["plus_petit_compte_dont_la_borne_basse_est_au_moins_0_79"] == 7981
    for cases, attendu in v2["regle_corrigee_de_C1_et_de_C4"]["par_nombre_de_cases"].items():
        assert IV.plus_petit_compte_d_echec(int(cases)) == attendu["plus_petit_compte_de_confirmation_qui_fait_echouer"]


def test_garde_26_regle_de_confirmation_sur_des_comptes_plantes():
    assert IV.regle_de_confirmation(500) == "tenue"
    assert IV.regle_de_confirmation(501) == "à confirmer"
    assert IV.regle_de_confirmation(501, 5235) == "tenue"
    assert IV.regle_de_confirmation(501, 5236) == "en échec"


def test_s9_contre_la_table_du_calcul_v2():
    v2 = lire_json(depot("palier-0b", "calcul-ordres-de-grandeur-palier-0b-v2.json"))
    for ligne in v2["seuil_de_beaucoup_plus_de_sources"]["table"]:
        n1 = ligne["n_du_seul_contraste_de_l_heritage"]
        assert AN.plus_petit_n2_qui_remplit(n1) == ligne["plus_petit_n_des_deux_contrastes_qui_remplit_la_condition"], n1
        assert (AN.s9(n1, None) == "remplie") == ligne["condition_remplie_si_les_deux_contrastes_ne_sont_pas_atteints_jusqu_a_48"]
    assert AN.s9(None, 12) == "sans objet"
    assert AN.s9(10, 12) == "non remplie"


# --- graines ---------------------------------------------------------------------------------------------------------------


def test_cle_de_derivation_quatre_mots_de_32_bits():
    e = GR.etiquette(couche="essai", famille="A", tirage=3, role="monde")
    h = hashlib.sha256(e.encode("utf-8")).digest()
    assert GR.cle_de_derivation(e) == tuple(int.from_bytes(h[4 * i:4 * i + 4], "big") for i in range(4))
    assert e == "couche=essai|famille=A|tirage=3|role=monde"
    a = GR.Graines().generateur(e).integers(0, 2 ** 62, 4)
    b = np.random.Generator(np.random.PCG64(np.random.SeedSequence(2026111902, spawn_key=GR.cle_de_derivation(e))))
    assert np.array_equal(a, b.integers(0, 2 ** 62, 4))


def test_couches_disjointes_et_decisif_refuse_sans_autorisation(tmp_path):
    g = GR.Graines()
    e1 = GR.etiquette(couche="etalonnage", famille="B", tirage=1, role="monde")
    e2 = GR.etiquette(couche="essai-de-forme", famille="B", tirage=1, role="monde")
    assert GR.cle_de_derivation(e1) != GR.cle_de_derivation(e2)
    assert GR.exiger_couches_disjointes([e1], [e2])
    with pytest.raises(GR.GraineRefusee):
        GR.exiger_couches_disjointes([e1], [e1])
    n_refus = len(GR.REFUS)
    for couche in ("decisif", "confirmation"):
        with pytest.raises(GR.GraineRefusee):
            g.generateur(GR.etiquette(couche=couche, famille="A", tirage=0, role="monde"))
    assert len(GR.REFUS) == n_refus + 2
    with pytest.raises(GR.GraineRefusee):
        GR.etiquette(famille="A")
    with pytest.raises(GR.GraineRefusee):
        GR.etiquette(couche="essai", inconnu=1)
    with pytest.raises(GR.GraineRefusee):
        GR.etiquette(couche="essai", famille="a|b")
    # une autorisation ne se construit pas sur un texte non scellé
    faux = tmp_path / "prereg.md"
    faux.write_text("brouillon", encoding="utf-8")
    sha = hashlib.sha256(b"brouillon").hexdigest()
    with pytest.raises(GR.GraineRefusee):
        GR.Autorisation(str(faux), sha, str(faux), sha)


def test_garde_20_graines_des_bras():
    def et(bras, avec_bras=True):
        champs = dict(couche="essai", tirage=0, source=0, generation=1, role="echantillonnage")
        if avec_bras:
            champs["bras"] = bras
        return [GR.etiquette(**champs)]
    monde = [GR.etiquette(couche="essai", tirage=0, source=0, monde="cible-1", role="monde")]
    sain = {b: {"monde": monde, "echantillonnage": et(b)} for b in ("1", "2", "3")}
    assert GR.verifier_graines_des_bras(sain)
    fautif = {b: {"monde": monde, "echantillonnage": et(b, avec_bras=False)} for b in ("1", "2", "3")}
    with pytest.raises(GR.GraineRefusee):
        GR.verifier_graines_des_bras(fautif)
    mondes_differents = dict(sain)
    mondes_differents["2"] = {"monde": [GR.etiquette(couche="essai", tirage=0, source=0, bras="2", role="monde")],
                              "echantillonnage": et("2")}
    with pytest.raises(GR.GraineRefusee):
        GR.verifier_graines_des_bras(mondes_differents)
