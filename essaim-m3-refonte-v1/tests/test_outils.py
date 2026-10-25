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


# ---------- extrait mécanique sans score (R1 ; pilote Gemini, PG2-01) ----------

def test_extrait_mecanique_sain_puis_artefacts(tmp_path, monkeypatch):
    """Cas sain : une course simulée donne un extrait avec statuts, appels par espèce et par statut, coûts, compagnon
    `.sha256`, et aucune clé de score ; refus d'écraser (R12) et d'écrire dans la course. Artefacts : une course fabriquée
    avec des scores plantés partout (manifeste, résumé, statut déclaré, castes de l'organisme, bilan spectral,
    événements, rapport) n'en laisse passer aucun ; une liste de champs qui laisserait passer `score` fait échouer
    l'extraction au lieu d'écrire (R5)."""
    import json
    from essaim_m3.noyau import boucle, taches
    from essaim_m3.simulateur import appelants_simules
    from essaim_m3.outils import extrait_mecanique as em

    ss = np.random.SeedSequence(5)
    r1, r2 = (np.random.default_rng(s) for s in ss.spawn(2))
    banque = taches.banque_simulation(r1, 8, 8)
    doubles, _ = appelants_simules(r2)
    n = boucle.Noyau(tmp_path / "run", "mission de test", banque, {"appels_max": 40, "usd_max": 5.0, "temps_max_s": 60}, 10.0, 2,
                     appelants=doubles, especes_amorcage=["GEMINI_ARGON"], entropie=5)
    n.amorcer()
    rapport = n.boucler()
    assert len(rapport["courbes"]["gemini-argon"]) == 2
    sortie = tmp_path / "extrait" / "extrait-mecanique-v1.json"
    chemin = em.ecrire(tmp_path / "run", sortie)
    assert chemin == sortie.resolve() and sortie.with_name(sortie.name + ".sha256").exists()
    e = json.loads(sortie.read_text(encoding="utf-8"))
    gens = e["generations"]
    assert len(gens) == 2 and [g["generation"] for g in gens] == [0, 1]
    for g in gens:
        assert g["statut"] == "OK" and g["appels"]["n"] == g["n_appels"] > 0 and "GEMINI_ARGON" in g["appels"]["par_espece"]
        assert g["appels"]["par_statut"].get("OK") and g["appels"]["cout_usd"] >= 0 and g["journal_appels_scelle"]
        assert g["execution"]["code"] == "OK" and g["organisme_tar_sha256"] and g["empreinte_organisme"]
        assert "score" not in g and "metrique_proposee" not in g
    assert e["manifeste"]["entropie_seed_sequence"] == 5
    assert e["rapport"]["n_appels_total"] == sum(g["n_appels"] for g in gens) + 1  # + l'appel d'amorçage
    assert all(ev.get("etape") for ev in e["evenements"]) and not any("score" in ev for ev in e["evenements"])
    assert em.cles_interdites_presentes(e) == []
    assert "courbes" not in e["rapport"] and "scores_finaux" not in e["rapport"]
    with pytest.raises(em.ExtraitInvalide):  # R12 : jamais réécrit
        em.ecrire(tmp_path / "run", sortie)
    with pytest.raises(em.ExtraitInvalide):  # la course reste telle quelle
        em.ecrire(tmp_path / "run", tmp_path / "run" / "extrait.json")
    with pytest.raises(em.ExtraitInvalide):  # pas une course
        em.extraire(tmp_path / "extrait")

    # artefact 1 : scores plantés partout dans une course fabriquée
    marque = 0.731234
    course = tmp_path / "fabriquee"
    g0 = course / "archive" / "lig" / "g000"
    (g0 / "juge").mkdir(parents=True)
    (g0 / "travail").mkdir()
    (course / "manifeste-run.json").write_text(json.dumps({"run": "x", "entropie_seed_sequence": 1, "score_cache": marque}), encoding="utf-8")
    (g0 / "resume.json").write_text(json.dumps({
        "lignee": "lig", "generation": 0, "phase": None, "statut": "OK", "n_appels": 2, "cout_usd": 0.01, "score": marque,
        "metrique_proposee": {"valeur": marque}, "successeur": True, "impose": True, "famille": "gemini",
        "execution": {"code": "OK", "duree_s": 1.0, "statut": {"code": "OK", "score": marque}}, "empreinte_organisme": "e" * 64}), encoding="utf-8")
    (g0 / "juge" / "score.json").write_text(json.dumps({"score": marque}), encoding="utf-8")
    (g0 / "journal-appels.jsonl").write_text("\n".join(json.dumps(l) for l in [
        {"espece": "CLAUDE_FABLE_5_1", "statut": "OK", "cout_usd": 0.005, "usage": {"entree": 10, "sortie": 5}, "max_tokens": 640,
         "modele_servi": "m", "debut_utc": "2026-10-24T22:00:00Z", "fin_utc": "2026-10-24T22:00:02Z"},
        {"espece": "CLAUDE_FABLE_5_1", "statut": "TRONQUE", "cout_usd": 0.005, "usage": {"entree": 10, "sortie": 5}, "max_tokens": 640,
         "modele_servi": "m", "debut_utc": "2026-10-24T22:00:02Z", "fin_utc": "2026-10-24T22:00:05Z"}]) + "\n", encoding="utf-8")
    (g0 / "travail" / "journal_generation.json").write_text(json.dumps({
        "version": "v", "n_castes_recrutees": 1, "castes": [{"id_caste": 1, "espece": "CLAUDE_FABLE_5_1", "mode": "M", "role": "r", "score_test": marque}],
        "compteurs_appels": {"tentatives": 2, "appels_ok": 1, "appels_echec": 1, "echecs_par_statut": {"TRONQUE": 1}, "cout_total_usd": 0.01},
        "details_votes_test": {"t1": {"score": marque}}, "bilan_spectral": {"n_textes": 2, "capacite_shannon": 1.0, "termes_satures": [str(marque)]},
        "erreurs": ["e1"], "bascule_parallele_a_la_tache": None, "temps_s": 3.0}), encoding="utf-8")
    (g0 / "travail" / "reponses_test.json").write_text(json.dumps({"t1": {"etiquette": "x", "score": marque}}), encoding="utf-8")
    (course / "evenements.jsonl").write_text(json.dumps({"etape": "generation", "lignee": "lig", "generation": 0, "statut": "OK", "score": marque, "cumul_usd": 0.01}) + "\n", encoding="utf-8")
    (course / "rapport-v1.json").write_text(json.dumps({"fin_utc": "t", "depense_totale_usd": 0.01, "n_appels_total": 2, "courbes": {"lig": [marque]},
                                                        "scores_finaux": {"lig": [marque]}, "lignees": {"lig": {"famille": "gemini", "fin": "f", "score": marque}}}), encoding="utf-8")
    e2 = em.extraire(course)
    texte = json.dumps(e2, ensure_ascii=False)
    assert str(marque) not in texte and em.cles_interdites_presentes(e2) == []
    g = e2["generations"][0]
    assert g["statut"] == "OK" and g["appels"]["par_statut"] == {"OK": 1, "TRONQUE": 1} and g["appels"]["durees_s"]["somme"] == 5.0
    assert g["organisme"]["castes"] == [{"id_caste": 1, "espece": "CLAUDE_FABLE_5_1", "mode": "M", "role": "r"}]
    assert "termes_satures" not in g["organisme"]["bilan_spectral"] and "details_votes_test" not in g["organisme"]
    assert g["execution"]["statut_declare_code"] == "OK" and "statut" not in g["execution"]
    assert "score_cache" not in e2["manifeste"] and "score" not in e2["evenements"][0] and "score" not in e2["rapport"]["lignees"]["lig"]
    assert any(f["chemin"] == "reponses_test.json" for f in g["fichiers_travail"])  # nom et taille seulement, jamais le contenu
    # artefact 2 : une liste de champs trop large laisserait passer `score` → l'extraction échoue, rien n'est écrit
    monkeypatch.setattr(em, "CHAMPS_RESUME", tuple(em.CHAMPS_RESUME) + ("score",))
    with pytest.raises(em.ExtraitInvalide):
        em.ecrire(course, tmp_path / "jamais" / "extrait.json")
    assert not (tmp_path / "jamais" / "extrait.json").exists()


def test_extrait_mecanique_v2_statuts_des_services_et_rondes_importees(tmp_path):
    """CE4-04 : l'extrait porte, par génération, les comptes par statut des entraînements, des recherches (par source) et
    des téléchargements, lus aux journaux du noyau archivés ; CE4-06 : dans un bras B (`--depuis`), les rondes importées
    sont marquées `importee` et sorties des totaux, qui égalent alors la dépense des seules générations de B ; aucune clé
    de score."""
    import json
    from essaim_m3.noyau import cli
    from essaim_m3.outils import extrait_mecanique as em
    racine = pathlib.Path(__file__).resolve().parent.parent
    sonde = racine / "tests" / "fixtures" / "organisme_sonde"
    concepteur = racine / "tests" / "fixtures" / "organisme_concepteur" / "organisme"
    a = tmp_path / "a"
    assert cli.principal(["simuler", "--sortie", str(a), "--generations", "1", "--graine", "63", "--n-train", "8", "--n-test", "8", "--n-final", "4",
                          "--appels-max", "30", "--especes", "GEMINI_ARGON", "--entrainements-max", "2", "--organisme-amorcage", str(sonde),
                          "--organisme-impose", f"concepteur={concepteur}@anthropic", "--rondes-conception-max", "2"]) == 0
    b = tmp_path / "b"
    assert cli.principal(["simuler", "--sortie", str(b), "--generations", "1", "--graine", "63", "--depuis", str(a),
                          "--appels-max", "30", "--entrainements-max", "0"]) == 0
    ea = em.extraire(a)
    sonde_g0 = next(g for g in ea["generations"] if g["lignee"] == "gemini-argon" and g["generation"] == 0 and not g.get("phase"))
    assert sonde_g0["services"]["entrainements"].get("OK", 0) >= 1 and ea["extrait_version"] == 2
    eb = em.extraire(b)
    rondes = [g for g in eb["generations"] if g.get("phase") == "conception"]
    assert rondes and all(g["importee"] for g in rondes)
    assert not any(g["importee"] for g in eb["generations"] if not g.get("phase"))
    t = eb["totaux_hors_importees"]
    assert t["n_importees"] == len(rondes)
    assert abs(t["cout_usd"] - sum(g["appels"]["cout_usd"] for g in eb["generations"] if not g["importee"])) < 1e-9
    assert abs(t["cout_usd"] - eb["rapport"]["depense_totale_usd"]) < 1e-4
    assert em.cles_interdites_presentes(eb) == [] and em.cles_interdites_presentes(ea) == []
