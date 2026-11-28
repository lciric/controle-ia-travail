"""Essais unitaires des 4 briques M-01 à M-04 de la v6.3.0 (Méta-Conception + Rectificatifs conv-audit)."""
import importlib
import math
import sys
import types
from pathlib import Path

RACINE_ORGANISME = Path(__file__).resolve().parents[1]
if str(RACINE_ORGANISME) not in sys.path:
    sys.path.insert(0, str(RACINE_ORGANISME))

import memoire_isvd
import mitose_spectrale
import principal


def test_m01_simhash_morphologique_racines_proches():
    v1 = memoire_isvd._vectoriser_texte_base("conformal prediction sequential martingale calibration")
    v2 = memoire_isvd._vectoriser_texte_base("conformalized predicting sequentially martingales calibrated")
    v3 = memoire_isvd._vectoriser_texte_base("ribosome protein transcription cellular metabolism")
    sim_12 = sum(a * b for a, b in zip(v1, v2))
    sim_13 = sum(a * b for a, b in zip(v1, v3))
    assert sim_12 > 0.65 and sim_12 > sim_13 + 0.30


def test_m01_centrage_bloc_quadratique_koopman_et_conditionnement():
    obs = memoire_isvd.relever_observables_koopman("martingale sequential bound theorem covariance eigenvalue")
    d = memoire_isvd.DIM_BASE
    bloc_quadratique = obs[2 * d : 3 * d]
    assert abs(sum(bloc_quadratique)) < 1e-9

    etat = memoire_isvd.creer_memoire_vide()
    sujets = [
        "conformal martingale sequential testing bound",
        "linear probe covariance floor activation layer",
        "symplectic geometry attention sink kv-cache",
        "cellular sheaf cohomology graph percolation hashimoto",
        "free probability marchenko-pastur cumulants tropical",
        "schrodinger bridge optimal transport sinkhorn divergence",
    ]
    for g in range(1, 51):
        traces = [
            {"texte": f"{sujets[(g + k) % len(sujets)]} theorem proof generation {g} step {k}", "poids": 0.9, "generation": g, "source": f"g{g}_{k}"}
            for k in range(4)
        ]
        etat = memoire_isvd.mettre_a_jour_memoire_isvd(etat, traces, generation=g, score_courant=0.85 + 0.001 * g)
    sigmas = etat["Sigma"]
    assert (sigmas[0] / max(1e-9, sigmas[-1])) < 10.0


def test_m02_mots_outils_bilingues_exclus_des_termes_satures():
    textes = [
        "Dans cet article the model with pour avec sans martingale",
        "Dans cet article the model with pour avec sans martingale",
    ]
    bilan = mitose_spectrale.calculer_capacite_shannon_gram(textes)
    for mot_outil in ("dans", "article", "avec", "pour", "with", "that", "model"):
        assert mot_outil not in bilan["termes_satures"]
    assert "martingale" in bilan["termes_satures"]


def test_m02_transitions_et_pivots_swanson_proteges():
    textes = [
        "optique laser cavite_resonante operateur_schrodinger dispersion_fibre",
        "finance volatilite portefeuille operateur_schrodinger arbitrage_stochastique",
        "programme controle_agent operateur_schrodinger surveillance_sequentielle",
    ]
    bilan = mitose_spectrale.calculer_capacite_shannon_gram(textes)
    assert len(bilan["pivots_swanson_proteges"]) >= 1
    assert bilan["pivots_swanson_proteges"][0] not in bilan["termes_satures"]


def test_m03_noyau_dpp_strictement_psd_cholesky():
    articles = [
        {"id": "a1", "source": "arxiv", "titre": "Radar Detection", "resume": "radar sonar antenna martingale bound theorem covariance", "lien": ""},
        {"id": "a2", "source": "arxiv", "titre": "Radar Array", "resume": "radar sonar array martingale bound eigenvalue", "lien": ""},
        {"id": "a3", "source": "openalex", "titre": "Optics Laser", "resume": "laser photon cavity martingale bound wasserstein", "lien": ""},
    ]
    L = principal.construire_noyau_dpp_domaine_operateur(articles, question="martingale bound", mission="detection")
    n = len(L)
    chol = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = sum(chol[i][k] * chol[j][k] for k in range(j))
            if i == j:
                assert L[i][i] - s > 1e-9
                chol[i][j] = math.sqrt(L[i][i] - s)
            else:
                chol[i][j] = (L[i][j] - s) / chol[j][j]


def test_m03_dpp_favorise_eloignement_domaines_et_qualite_operateurs():
    articles = [
        {"id": "domA_1", "source": "arxiv", "titre": "Radar Clutter 1", "resume": "radar clutter doppler antenna sonar martingale theorem bound covariance", "lien": ""},
        {"id": "domA_2", "source": "arxiv", "titre": "Radar Clutter 2", "resume": "radar clutter doppler antenna sonar martingale theorem bound", "lien": ""},
        {"id": "domB_1", "source": "openalex", "titre": "Genomic Sequencing", "resume": "genome nucleotide chromosome allele martingale theorem bound covariance", "lien": ""},
    ]
    retenus, _ = principal.selectionner_articles_dpp_et_filtrer_contraintes(articles, question="martingale bound", mission="control", k=2)
    ids_ret = {a["id"] for a in retenus}
    assert ids_ret == {"domA_1", "domB_1"}


def test_m04_filtre_incompatibilite_regimes_exclusifs():
    articles = [
        {"id": "wb", "source": "arxiv", "titre": "White-Box Probe", "resume": "activation residual layer jacobian martingale theorem", "lien": ""},
        {"id": "bb", "source": "openalex", "titre": "Black-Box API", "resume": "black-box query-only text-only api martingale theorem", "lien": ""},
        {"id": "wb2", "source": "arxiv", "titre": "Optics White-Box", "resume": "photon cavity laser activation residual layer martingale theorem", "lien": ""},
    ]
    _, paires = principal.selectionner_articles_dpp_et_filtrer_contraintes(articles, question="martingale", mission="control", k=3)
    for p in paires:
        assert not ("White-Box Probe" in p["article_A"] and "Black-Box API" in p["article_B"])
        assert not ("Black-Box API" in p["article_A"] and "White-Box Probe" in p["article_B"])


def test_m04_normalisation_anti_bavardage_et_integration_executer(tmp_path, monkeypatch):
    court_dense = {"titre": "Concise Theorem", "resume": "martingale bound theorem eigenvalue covariance wasserstein"}
    long_bavard = {"titre": "Verbose Text", "resume": "martingale bound " + " ".join(["blabla_filler_word"] * 200)}
    p_court = principal._extraire_profil_article_v63(court_dense)
    p_long = principal._extraire_profil_article_v63(long_bavard)
    assert p_court["qualite_q"] > p_long["qualite_q"]

    module = types.ModuleType("noyau_client")
    module.especes = lambda: ["CLAUDE_FABLE_5_1", "GEMINI_4_ARGON"]
    module.budget = lambda: {
        "appels_restants": 10, "usd_restants": 5.0, "recherches_restantes": 2,
        "sources": ["arxiv"], "telechargements_restants": 1, "octets_restants": 100000,
        "entrainements_restants": 0, "max_tokens_appel": 4096,
    }
    module.rechercher = lambda req, n=5, role="", source="arxiv": {
        "statut": "OK", "source": source, "identifiant": "r1", "echec": None,
        "resultats": [
            {"source": source, "id": "a1", "titre": "Radar Sequential", "auteurs": "A", "date": "2026", "resume": "radar sonar antenna finite-sample martingale theorem bound", "lien": "https://arxiv.org/abs/2501.00001"},
            {"source": source, "id": "a2", "titre": "Optics Cavity", "auteurs": "B", "date": "2026", "resume": "laser photon optics finite-sample martingale theorem bound", "lien": "https://arxiv.org/abs/2501.00002"},
        ],
    }
    module.telecharger = lambda ref, role="": {"statut": "OK", "identifiant": "t1", "adresse": ref, "genre": "article", "titre": "T", "octets": 30, "sha256_brut": "h", "sha256_texte": "h", "texte": "Contenu.", "tronque": False, "caracteres_texte": 8, "fichier_texte": None, "echec": None}
    module.appeler = lambda esp, pr, max_tokens=None, role="": {
        "statut": "OK",
        "texte": '{"requetes": ["q1"]}' if role == "moissonneur_formulation_requetes" else 'Analyse.
{"position": "OK", "confiance": 0.9, "incertitude": "ras"}',
        "modele_servi": esp, "fin": "stop", "usage": {}, "cout_usd": 0.01, "identifiant": "c1", "echec": None,
    }
    monkeypatch.setitem(sys.modules, "noyau_client", module)
    importlib.reload(principal)
    bilan = principal.executer({
        "generation": 1, "phase": "generation", "lignee": "v6-3", "mission": "Mission.",
        "dossier_travail": str(tmp_path / "run_v63"), "dossier_archive": "",
        "taches_entrainement": [], "taches_test": [], "question_ouverte": "Question programme ?",
        "budget": {"appels_max": 10, "usd_max": 5.0, "temps_max_s": 120, "recherches_max": 2, "telechargements_max": 1, "octets_max": 100000},
        "historique": [],
    })
    assert bilan["version"] == "organisme-gemini-m3-v6-3-0"
