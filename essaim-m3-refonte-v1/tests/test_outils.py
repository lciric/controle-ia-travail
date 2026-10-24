"""Tests de la boîte à outils (mécanismes de Gemini rendus réels) : cas sain et artefact pour chaque garde (R5).
Ces outils ne sont pas donnés à l'essaim ; ils documentent et vérifient les corrections de l'audit."""
import pathlib
import sys

import numpy as np
import pytest

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))

from essaim_m3.outils import canaris, diversite, genome, memoire, plongement, verification  # noqa: E402


def rng(g=0):
    return np.random.default_rng(g)


# ---------- plongement ----------

def test_plongement_normalise_et_detecte_corruption():
    p = plongement.Plongeur(256).ajuster(["$\\alpha + \\beta$ projecteur", "$\\gamma$ martingale"])
    v = p.vecteur("$\\alpha$ projecteur orthogonal")
    assert abs(np.linalg.norm(v) - 1.0) < 1e-9
    assert plongement.texte_corrompu("une m?thode d?coup?e") and not plongement.texte_corrompu("une méthode découpée")
    assert np.linalg.norm(p.vecteur("")) == 0.0


# ---------- diversité (M3 / M2) ----------

def test_residu_orthogonal_sain_et_doublon():
    p = plongement.Plongeur(512).ajuster(["a b c", "d e f"])
    a, b = p.vecteur("alpha beta gamma projecteur"), p.vecteur("delta epsilon zeta martingale")
    assert diversite.residu_orthogonal(b, np.stack([a])) > 0.9
    assert diversite.residu_orthogonal(a, np.stack([a])) < 1e-9
    assert diversite.fraction_expliquee(a, np.stack([a])) > 0.999


def test_arret_mitose_par_nul_de_permutation():
    p = plongement.Plongeur(1024)
    textes = ["projecteur orthogonal $\\alpha$ résidu", "martingale surmartingale $\\beta$ Ville", "canari aveugle $\\gamma$ engagement",
              "projecteur orthogonal $\\alpha$ résidu"]  # la 4e répète la 1re
    p.ajuster(textes)
    vecs = p.matrice(textes)
    residus = diversite.residus_sequentiels(vecs)
    seuil = diversite.seuil_nouveaute_permutation(textes[:3], p, rng(1), n_permutations=30)
    assert residus[3] < 1e-9 and residus[1] > seuil
    assert not diversite.arret_mitose(residus[:3], seuil, k=2, minimum=3)
    assert diversite.arret_mitose(residus[:3] + [0.0, 0.0], seuil, k=2, minimum=3)


def test_neuromodulateur_reagit_aux_ruptures():
    n = diversite.Neuromodulateur()
    for r in [0.8, 0.8, 0.8]:
        e = n.observer(r)
    assert e["NE_incertitude_inattendue"] == 0.0 and e["sondes_tunnel"] == 0
    e2 = n.observer(0.05)
    assert e2["NE_incertitude_inattendue"] > 0.0


def test_bandit_explore_et_apprend():
    b = diversite.BanditPredation(["a", "b"], rng(3), eps_min=0.05)
    for _ in range(60):
        bras = b.choisir()
        b.recompenser(bras, 1.0 if bras == "b" else 0.0)
    assert b.q["b"] > b.q["a"] and b.n["a"] > 0  # exploration minimale : a est encore tiré
    assert all(t["epsilon"] >= 0.05 for t in b.trace)
    u = diversite.BanditPredation(["a", "b"], rng(4), regle="uniforme")
    assert {u.choisir() for _ in range(30)} == {"a", "b"}


def test_recompense_anti_echec_bornee_et_unilaterale():
    assert diversite.recompense_anti_echec(2.0, 1) == 1.0  # μ projeté sur [0, 1]
    assert diversite.recompense_anti_echec(-1.0, 0) == 0.0
    assert diversite.recompense_anti_echec(1.0, 0) == -1.0 and diversite.recompense_anti_echec(0.5, 0) <= 0.0
    assert diversite.recompense_anti_echec(0.9, 1, cout=1.0, gamma=0.1) < diversite.recompense_anti_echec(0.9, 1)


# ---------- canaris ----------

def test_canaris_sains_et_artefacts():
    cs = canaris.tirer_canaris(rng(2), 12)
    presentes, engagement = canaris.meler(["candidat réel"], cs, rng(5))
    assert canaris.verifier_engagement(engagement, presentes)
    assert all(it["id"].startswith("item-") and "CANARI" not in it["id"] for it in presentes)
    parfaits = {it["id"]: ("VALIDE" if it.get("vrai") else "INVALIDE") for it in presentes if it["type"] == "canari"}
    m = canaris.mesurer(presentes, parfaits)
    assert m["valide"] and m["youden_J"] == 1.0 and 0.7 < m["puissance_wilson_inf"] < 1.0
    tout_invalide = {it["id"]: "INVALIDE" for it in presentes}
    m2 = canaris.mesurer(presentes, tout_invalide)
    assert m2["valide"] and m2["specificite"] == 0.0 and m2["youden_J"] == 0.0
    vide = canaris.mesurer(presentes, {})
    assert not vide["valide"] and vide["non_lus"] == 12
    with pytest.raises(ValueError):
        canaris.tirer_canaris(rng(2), 6)
    presentes[0]["type"] = "candidat" if presentes[0]["type"] == "canari" else "canari"
    assert not canaris.verifier_engagement(engagement, presentes)


def test_wilson_inferieur():
    assert canaris.wilson_inferieur(12, 12) < 1.0 and canaris.wilson_inferieur(12, 12) > 0.7
    assert canaris.wilson_inferieur(0, 12) == 0.0 and canaris.wilson_inferieur(1, 0) == 0.0


# ---------- vérification (M1) : e-processus ----------

def test_eprocessus_converge_seulement_sur_tours_propres_et_lisibles():
    e = verification.EProcessus(alpha=0.05)
    assert not e.observer(0, lisible=False, puissance=0.9, m_familles=2)["converge"]  # tour illisible : e = 1
    assert e.produit == 1.0
    e.observer(0, True, 0.7, 2)
    assert e.produit == pytest.approx(1 / 0.09, rel=1e-6)
    e.observer(0, True, 0.7, 2)
    assert e.converge  # (1/0.09)² ≈ 123 ≥ 20
    e2 = verification.EProcessus(0.05)
    e2.observer(0, True, 0.9, 2)
    e2.observer(3, True, 0.9, 2)  # faille confirmée : produit remis à 1
    assert e2.produit == 1.0 and not e2.converge


def test_parseurs_json_robustes():
    assert verification.extraire_json("blabla ```json {\"a\": 1} ``` fin") == {"a": 1}
    assert verification.extraire_json("[Erreur GEMINI_ARGON : HTTP Error 404]") is None
    assert verification.parser_verdicts("```json {\"verdicts\": {\"item-01\": \" valide \"}} ```") == {"item-01": "VALIDE"}
    assert verification.parser_candidats("rien") == []


def test_tour_collisionneur_sans_defaut_sur_erreur():
    class Res:
        def __init__(self, ok, texte=""):
            self.ok, self.texte, self.statut, self.identifiant = ok, texte, ("OK" if ok else "ECHEC_API"), "x"

    def appeler_en_panne(espece, etape, prompt, role=""):
        return Res(False)

    r = verification.tour_collisionneur(appeler_en_panne, "t", "cible", "contexte", ["GEMINI_ARGON"], ["CLAUDE_OPUS_5_5"], rng(1), [], [])
    assert not r["lisible"] and r["confirmes"] == [] and r["puissance"] == 0.0 and r["m_familles"] == 0


# ---------- mémoire (M0) ----------

def test_jacobi_egal_eigh():
    a = rng(9).normal(size=(5, 5))
    a = a @ a.T
    val, vec = memoire.jacobi_symetrique(a)
    ref = np.sort(np.linalg.eigvalsh(a))[::-1]
    assert np.allclose(val, ref, atol=1e-8)
    assert np.allclose(vec.T @ vec, np.eye(5), atol=1e-8)


def test_memoire_isvd_suit_la_svd_tronquee():
    r = rng(11)
    vecs = r.normal(size=(8, 40))
    vecs /= np.linalg.norm(vecs, axis=1, keepdims=True)
    exacte = memoire.MemoireISVD(40, r_max=8)  # sans troncature : égale à la SVD par lots
    for v in vecs:
        exacte.ajouter(v)
    s_ref = np.linalg.svd(vecs, compute_uv=False)
    assert exacte.u.shape == (40, 8) and np.allclose(np.sort(exacte.s)[::-1], s_ref, rtol=1e-6)
    m = memoire.MemoireISVD(40, r_max=3)  # tronquée : approximation, jamais au-dessus de la SVD par lots
    for v in vecs:
        m.ajouter(v)
    assert m.u.shape == (40, 3) and np.all(np.sort(m.s)[::-1] <= s_ref[:3] + 1e-9)
    assert np.allclose(np.sort(m.s)[::-1], s_ref[:3], rtol=0.05)
    assert m.nouveaute(vecs[0]) < 1.0 and m.nouveaute(r.normal(size=40) / 6.3) > 0.5


def test_base_connaissances_versionnee_et_deja_couvert(tmp_path):
    b = memoire.BaseConnaissances(512)
    b.ingerer("indice : horodatages à minutes rondes (catégorie horodatage-artificiel)", "verifie-verificateur", {"g": 0}, 0)
    assert b.deja_couvert("indice : horodatages à minutes rondes (catégorie horodatage-artificiel)", 0.35)
    assert not b.deja_couvert("théorème de la martingale de Ville et surmartingale", 0.35)
    c1 = b.sauver(tmp_path); c2 = b.sauver(tmp_path)
    assert c1.name == "connaissances-v0001.json" and c2.name == "connaissances-v0002.json"
    with pytest.raises(ValueError):
        b.ingerer("x", "certifie", {}, 0)
    b2 = memoire.BaseConnaissances.charger(c2, 512)
    assert len(b2.entrees) == 1


# ---------- génome ----------

def test_genome_base_valide_et_espaces_reserves_rejetes():
    g = genome.genome_base()
    assert genome.valider(g) == []
    g2 = genome.genome_base()
    g2["organisation"]["castes"][0]["cible"] = "..."
    g2["routage"]["regle"] = "magique"
    g2["boucles"]["n_canaris"] = 4
    pb = genome.valider(g2)
    assert any("réservée" in p for p in pb) and any("hors menu" in p for p in pb) and any("n_canaris" in p for p in pb)
    g3 = genome.genome_base()
    g3["organisation"]["castes"] = [c for c in g3["organisation"]["castes"] if c["espece"] != "GEMINI_ARGON"]
    assert any("une seule famille" in p for p in genome.valider(g3))
    nouveau, problemes = genome.proposition_vers_genome({k: v for k, v in g.items()}, g, 1, {"etape": "t"})
    assert problemes == [] and nouveau["generation"] == 1 and nouveau["parent"] == "v1"
