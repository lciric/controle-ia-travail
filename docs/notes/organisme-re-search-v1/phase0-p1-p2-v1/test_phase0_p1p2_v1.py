"""Essais (R5) de la phase 0 de P1 et P2 — v1 (modèle I, auteur unique). Fichier neuf (R12).

Chaque garde est essayée sur un cas sain et sur un artefact. Les essais tournent sur de petits mondes d'essai (racine de
graines 4242, espaces de 256 lois au plus, sondes réduites), jamais sur la configuration du préenregistrement, et sur des sources
fabriquées, jamais sur les 23 cartes de la course v67 ni sur les sorties des attaques de Goodhart.
Lancement : cd <ce dossier> && PYTHONDONTWRITEBYTECODE=1 python3 -B -m pytest -q -p no:cacheprovider test_phase0_p1p2_v1.py
"""
import hashlib
import json
import runpy
import shutil
import sys
from pathlib import Path

import numpy as np
import pytest

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))

import lanceur_phase0_p1p2_v1 as lanceur  # noqa: E402
import mesure_forme_p2_v1 as p2  # noqa: E402
import mondes_reponses_p1p2_v1 as mr  # noqa: E402
import questionneurs_p1_v1 as qp  # noqa: E402

EVALUATEUR = "/home/user/ideation-organism/orchestrator/pole/evaluateur_lois_v62.py"
RACINE_ESSAI = 4242


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


# --- petits mondes d'essai (partagés) -----------------------------------------------------------------------------------
@pytest.fixture(scope="module")
def petits_mondes():
    """Espace d'essai de 256 lois (= 2^8, pour des parties de T = 8 questions), 150 mondes tirés dedans."""
    sq = mr.tirer_sonde(mr.generateur("essai/sq", RACINE_ESSAI), 512)
    ss = mr.tirer_sonde(mr.generateur("essai/ss", RACINE_ESSAI), 128)
    espace = qp.construire_espace(mr.generateur("essai/espace", RACINE_ESSAI), 256, sq, ss)
    return espace, qp.tirer_mondes(mr.generateur("essai/mondes", RACINE_ESSAI), espace, 150)


def banc(petits, noms, prefixe, mode="exact", taux=0.0, T=8, points=(0, 4, 8), colonnes=42):
    espace, mondes = petits
    return qp.jouer_banc(espace, mondes, noms, rng_essai(prefixe), mode, taux, T, points, colonnes)


def rng_essai(prefixe):
    return lambda nom, i, role: mr.generateur(f"essai/{prefixe}/{nom}/{i}/{role}", RACINE_ESSAI)


def kl16(banc, nom, t=8):
    return qp.colonne(banc[nom], t)


# --- évaluateur ---------------------------------------------------------------------------------------------------------
def test_proba_vec_egale_evaluateur_v62():
    ev = runpy.run_path(EVALUATEUR)
    rng = np.random.default_rng(1)
    Z, G = mr.tirer_sonde(rng, 40)
    ecart = 0.0
    types_vus = set()
    for _ in range(200):
        loi = mr.tirer_loi(rng)
        types_vus.add(loi["type"])
        P = mr.proba_vec(loi, Z, G)
        for n in range(40):
            p = ev["proba"](loi, {"z": [float(Z[n, 0]), float(Z[n, 1])], "g": int(G[n])})
            ecart = max(ecart, max(abs(a - b) for a, b in zip(p, P[n])))
    assert ecart < 1e-12
    assert types_vus == set(mr.TYPES)


def test_type_hors_gabarit_refuse():
    Z, G = mr.tirer_sonde(np.random.default_rng(0), 4)
    with pytest.raises(mr.Refus):
        mr.proba_vec({"type": "inconnu"}, Z, G)


def test_cas_sain_a_la_main_deux_traits():
    # softmax à poids nuls sauf l'issue 0 qui croît avec z0 : P(0 | z0 > 0) > P(0 | z0 ≤ 0) vrai, pour z1 : égal (faux)
    loi = {"type": "softmax", "poids": [[2.0, 0.0], [0.0, 0.0], [0.0, 0.0]], "biais": [0.0, 0.0, 0.0]}
    Z = np.array([[-1.0, 0.3], [1.0, 0.3], [-1.0, -0.3], [1.0, -0.3]])
    G = np.array([0, 1, 0, 1])
    P = mr.proba_vec(loi, Z, G)
    e2 = np.exp(2.0)
    assert abs(P[1, 0] - e2 / (e2 + 2)) < 1e-12 and abs(P[0, 0] - np.exp(-2) / (np.exp(-2) + 2)) < 1e-12
    preds = [{"genre": "trait", "trait": 0, "issue": 0, "seuil": 0.0, "direction": "z0"},
             {"genre": "trait", "trait": 1, "issue": 0, "seuil": 0.0, "direction": "z1"},
             {"genre": "sous_population", "issue": 0, "direction": "g"},
             {"genre": "marginale", "issue": 0, "seuil": 0.5, "direction": "marginale"}]
    r = mr.reponses_predicats(loi, P, Z, G, preds)
    # z1 : moyennes égales (0,5·(P0(-1)+P0(1)) des deux côtés) donc faux ; g suit z0 ici : vrai ;
    # marginale P(0) = (e^-2/(e^-2+2) + e^2/(e^2+2))/2 ≈ 0,4476 < 0,5 : faux
    assert r.tolist() == [True, False, True, False]
    kl = mr.kl_moyenne(P, P)
    assert kl == 0.0


# --- répondeur ----------------------------------------------------------------------------------------------------------
def test_reponse_booleenne_saine_et_artefact():
    assert mr.exiger_booleen(True) is True
    assert mr.exiger_booleen(np.bool_(False)) is False
    for artefact in ({"loi": "fuite"}, "Inconnu", 1, None):
        with pytest.raises(mr.Refus):
            mr.exiger_booleen(artefact)


def test_question_hors_grammaire_refusee_et_comptee():
    rep = mr.Repondeur(np.array([True, False, True]))
    assert rep.repondre(0) is True and rep.repondre(1) is False
    for artefact in (3, -1, "0", True, 1.0):
        with pytest.raises(mr.Refus):
            rep.repondre(artefact)
    assert rep.refus_hors_grammaire == 5


# --- jeu : cas sain, artefacts ------------------------------------------------------------------------------------------
def test_ordre_tient_sur_petits_mondes(petits_mondes):
    b = banc(petits_mondes, ("aleatoire", "bissection", "repeteur"), "sain")
    d1 = qp.bootstrap_double(kl16(b, "aleatoire"), kl16(b, "bissection"), np.random.default_rng(1), 2000)
    d2 = qp.bootstrap_double(kl16(b, "repeteur"), kl16(b, "aleatoire"), np.random.default_rng(2), 2000)
    assert lanceur.tient_ordre(d1) and lanceur.tient_ordre(d2)  # les deux statistiques, les deux écarts


def test_monde_au_hasard_efface_l_ordre(petits_mondes):
    b = banc(petits_mondes, ("aleatoire", "bissection"), "hasard", "hasard")
    d = qp.bootstrap_double(kl16(b, "aleatoire"), kl16(b, "bissection"), np.random.default_rng(3), 2000)
    assert lanceur.tient_disparition(d)  # l'avantage de la bissection disparaît, pour les deux statistiques
    # artefact de la garde : répondeur exact, l'avantage demeure, la garde doit échouer
    e = banc(petits_mondes, ("aleatoire", "bissection"), "hasard-temoin")
    de = qp.bootstrap_double(kl16(e, "aleatoire"), kl16(e, "bissection"), np.random.default_rng(3), 2000)
    assert not lanceur.tient_disparition(de)


def test_inversion_de_10_pour_cent_fait_perdre_la_bissection(petits_mondes):
    exact = banc(petits_mondes, ("bissection",), "ex")
    bruit = banc(petits_mondes, ("bissection",), "inv", "inverse", 0.10)
    d = qp.bootstrap_double(kl16(bruit, "bissection"), kl16(exact, "bissection"), np.random.default_rng(4), 2000)
    assert lanceur.tient_degradation(d)
    # artefact de la garde : deux copies exactes, aucune dégradation, la garde doit échouer
    exact2 = banc(petits_mondes, ("bissection",), "ex2")
    d0 = qp.bootstrap_double(kl16(exact2, "bissection"), kl16(exact, "bissection"), np.random.default_rng(4), 2000)
    assert not lanceur.tient_degradation(d0)


def test_oracle_divergence_nulle_et_garde_de_fuite(petits_mondes):
    b = banc(petits_mondes, ("oracle", "aleatoire"), "or")
    for t in (0, 4, 8):
        assert np.max(qp.colonne(b["oracle"], t)) == 0.0
    assert qp.taux_fuite([p["cartes"][0]["exacte"] for p in b["oracle"]]) > qp.SEUIL_FUITE  # artefact signalé
    assert qp.taux_fuite([p["cartes"][0]["exacte"] for p in b["aleatoire"]]) <= qp.SEUIL_FUITE  # sain non signalé


def test_questionneur_hors_grammaire_refuse(petits_mondes):
    class Fautif(qp.Questionneur):
        nom = "fautif"

        def choisir(self, etat):
            return 999

    espace, mondes = petits_mondes
    rep = mr.Repondeur(espace["A"][mondes[0], :42])
    with pytest.raises(mr.Refus):
        qp.jouer_partie(espace, mondes[0], Fautif(np.random.default_rng(0)), rep, 4, (0, 4), 42)
    assert rep.refus_hors_grammaire == 1


def test_repeteur_et_disperseur_respectent_leur_direction(petits_mondes):
    espace, mondes = petits_mondes
    preds = espace["preds"][:42]
    for nom, verif in (("repeteur", lambda d: set(d) == {"z0"}),
                       ("disperseur", lambda d: all(a != b for a, b in zip(d, d[1:])))):
        q = qp.QUESTIONNEURS[nom](np.random.default_rng(5))
        p = qp.jouer_partie(espace, mondes[0], q, mr.Repondeur(espace["A"][mondes[0], :42]), 16, (0, 16), 42)
        assert verif([preds[i]["direction"] for i in p["posees"]])


def test_A_A_meme_questionneur_graines_differentes(petits_mondes):
    b = banc(petits_mondes, ("aleatoire", "aleatoire#2"), "aa")
    assert [p["posees"] for p in b["aleatoire"]] != [p["posees"] for p in b["aleatoire#2"]]
    d = qp.bootstrap_diff_medianes(kl16(b, "aleatoire#2"), kl16(b, "aleatoire"), np.random.default_rng(6), 2000)
    assert d["ic95"][0] <= 0 <= d["ic95"][1]


def test_bootstrap_refuse_non_apparie():
    with pytest.raises(mr.Refus):
        qp.bootstrap_diff_medianes([1.0, 2.0], [1.0], np.random.default_rng(0), 10)


# --- disjonction --------------------------------------------------------------------------------------------------------
def test_garde_de_disjonction_saine_et_artefact():
    rng = np.random.default_rng(9)
    Z, G = mr.tirer_sonde(rng, 128)
    a = {"type": "fixe", "probas": [0.8, 0.1, 0.1]}
    b = {"type": "fixe", "probas": [0.1, 0.1, 0.8]}
    pa, pb = mr.proba_vec(a, Z, G), mr.proba_vec(b, Z, G)
    assert mr.disjointe(pb, [pa])  # sain : loin
    assert not mr.disjointe(pa, [pa])  # artefact : identique à une référence
    # construire_espace retire les candidates trop proches des références (comptées) : référence = une candidate
    # tirée par le même générateur, donc retirée au moins une fois
    sq = mr.tirer_sonde(rng, 128)
    premiere = mr.tirer_loi(np.random.default_rng(10))
    refs = [mr.proba_vec(premiere, Z, G)]
    e = qp.construire_espace(np.random.default_rng(10), 64, sq, (Z, G), refs)
    for P in e["P"]:
        assert mr.disjointe(P.reshape(-1, 3), refs)
    assert e["retirees_disjonction"] >= 1
    assert premiere not in e["lois"]


def test_medoide_et_kl_sans_matrice_egalent_le_calcul_direct(petits_mondes):
    espace, mondes = petits_mondes
    P = espace["P"].reshape(len(espace["lois"]), -1, 3)
    S = np.arange(0, 256, 3)
    K = mr.matrice_kl(P[S])
    assert medoide_direct(K, S) == qp.medoide(espace, S)
    w, c = mondes[0], mondes[1]
    assert abs(qp.kl_vers(espace, w, c) - mr.kl_moyenne(P[w], P[c])) < 1e-10
    assert qp.kl_vers(espace, w, w) == 0.0


def medoide_direct(K, S):
    return int(S[int(np.argmin(K.mean(axis=0)))])


# --- P2 : mesure de la forme --------------------------------------------------------------------------------------------
SM = {"type": "softmax", "poids": [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]], "biais": [0.0, 0.1, 0.2]}
SM2 = {"type": "softmax", "poids": [[1.1, 0.2], [0.3, 2.4], [0.5, 0.6]], "biais": [1.0, 0.1, 0.2]}
FX = {"type": "fixe", "probas": [0.2, 0.3, 0.5]}
SI0 = {"type": "si_sinon", "condition": {"indice": 0, "seuil": 0.1}, "si": FX, "sinon": SM}
SI1 = {"type": "si_sinon", "condition": {"indice": 1, "seuil": 0.4}, "si": FX, "sinon": SM2}


def carte(g, p, i, loi):
    return {"generation": g, "proposeur": p, "identifiant": f"G{g}-{p}-{i:02d}", "loi": loi}


def cartes_fabriquees():
    return [carte(1, "kimi", 1, SM), carte(1, "kimi", 2, SM2),  # la seconde répète (même proposeur, plus haut)
            carte(1, "argon", 1, SM),  # simultanée : pas une répétition
            carte(1, "argon", 2, SI0),
            carte(2, "kimi", 1, FX),  # forme non vue plus tôt
            carte(2, "argon", 1, SI1)]  # même forme que SI0 (entiers masqués), non vue plus tôt si entiers gardés


def test_regle_m2_a_la_main():
    obs = p2.mesure_observee(cartes_fabriquees())
    assert obs["repetent"] == 2 and obs["cartes"] == 6  # G1-kimi-02 et G2-argon-01
    assert abs(obs["part"] - 2 / 6) < 1e-12
    assert abs(obs["part_entiers_gardes"] - 1 / 6) < 1e-12  # A-3 : SI1 a un autre indice de trait
    assert obs["hors_softmax"]["cartes"] == 3 and obs["hors_softmax"]["repetent"] == 1  # A-1


def test_garde_de_reproduction_m2_saine_et_artefact():
    obs = p2.mesure_observee(cartes_fabriquees())
    lanceur.exiger_reproduction_m2(obs, {"cartes": 6, "repetent": 2})
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_reproduction_m2(obs, {"cartes": 6, "repetent": 3})


def test_reference_a_forme_unique_tout_repete():
    # grammaire réduite au seul softmax : chaque carte répète, sauf la première de chaque proposeur à la génération 1
    cartes = cartes_fabriquees()
    rng = mr.generateur("essai/forme-unique", RACINE_ESSAI)
    tirees = p2._cartes_tirees(p2.trier_cartes(cartes), rng, ["softmax"], None)
    assert abs(p2.part_m2(tirees) - 4 / 6) < 1e-12


def test_reference_r1_r2_hs_seq_rendent_des_parts():
    cartes = cartes_fabriquees()
    for v in ("R1", "R2", "HS", "SEQ"):
        parts, parts_e = p2.reference_m2(cartes, mr.generateur(f"essai/ref/{v}", RACINE_ESSAI), 30, v)
        assert parts.shape == (30,) and np.all((parts >= 0) & (parts <= 1)) and np.all(parts_e <= parts + 1e-12)
    with pytest.raises(mr.Refus):
        p2.reference_m2(cartes, np.random.default_rng(0), 3, "R9")


def test_m4_a_la_main():
    suites = [{"tentatives": [{"k": 1, "loi": SM}, {"k": 2, "loi": SM2}, {"k": 3, "loi": None}, {"k": 4, "loi": FX}]},
              {"tentatives": [{"k": 1, "loi": SM}, {"k": 2, "loi": SM}]}]
    part, rep, props = p2.part_m4(suites)
    assert (rep, props) == (2, 5)


# --- lanceur : gardes et bout en bout sur sources fabriquées ------------------------------------------------------------
def test_garde_du_preenregistrement_saine_et_artefact(tmp_path):
    p = tmp_path / "prereg.md"
    p.write_text("texte gelé\n", encoding="utf-8")
    assert lanceur.exiger_preenregistrement(p, sha(p)) == sha(p)
    attendue = sha(p)
    p.write_text("texte gelé.\n", encoding="utf-8")  # altéré d'un caractère
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_preenregistrement(p, attendue)
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_preenregistrement(tmp_path / "absent.md", attendue)


def test_garde_du_code_scelle_saine_et_artefact(tmp_path):
    for m in lanceur.MODULES:
        shutil.copy(ICI / m, tmp_path / m)
        (tmp_path / (m + ".sha256")).write_text(f"{sha(tmp_path / m)}  {m}\n", encoding="utf-8")
    assert set(lanceur.exiger_code_scelle(tmp_path)) == set(lanceur.MODULES)
    with open(tmp_path / lanceur.MODULES[0], "a", encoding="utf-8") as f:
        f.write("# altération\n")
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_code_scelle(tmp_path)
    (tmp_path / (lanceur.MODULES[1] + ".sha256")).unlink()
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_code_scelle(tmp_path, (lanceur.MODULES[1],))


def test_garde_de_source_et_dossier_neuf(tmp_path):
    f = tmp_path / "s.json"
    f.write_text("{}", encoding="utf-8")
    journal = []
    lanceur.charger_source("x", f, sha(f), journal)
    assert journal and sha(f) in journal[0]
    with pytest.raises(lanceur.Refus):
        lanceur.charger_source("x", f, "0" * 64, [])
    lanceur.dossier_neuf(tmp_path / "neuf")
    with pytest.raises(lanceur.Refus):
        lanceur.dossier_neuf(tmp_path)


def config_essai():
    return {"racine_graines": RACINE_ESSAI,
            "p1": {"mondes": 12, "taille_espace_H": 32, "questions_T": 8, "points_de_carte": [0, 4, 8],
                   "sonde_questions": 256, "sonde_score": 64, "predicats_principaux": 42, "predicats_structurels": 51,
                   "taux_inversion_artefact": 0.1, "tirages_bootstrap": 200, "fraction_largeur_aa": 0.5,
                   "seuil_fuite": 0.05, "seuil_audit_trop_facile": 0.95, "mondes_information_phase1": 8,
                   "politique_refus": "arret", "bras_principal": list(lanceur.BRAS_PRINCIPAL),
                   "bras_inverse_10": list(lanceur.BRAS_INVERSE), "bras_hasard": list(lanceur.BRAS_HASARD),
                   "bras_structurelle": list(lanceur.BRAS_STRUCTURELLE)},
            "p2": {"tirages_reference": 20, "tirages_reference_m4": 5, "seuil": 0.25,
                   "quota_principal": 2, "quota_plage_sensibilite": [1, 2, 3],
                   "observe_attendu_analyse": {"cartes": 6, "repetent": 2},
                   "m4_attendu_analyse": {"goodhart_v3": {"retour": 0.5, "temoin": 0.0}}}}


def _sources_fabriquees(tmp_path, gh_interrompue=False):
    v67 = {"releve": {"cartes": cartes_fabriquees(), "plantees": [{"nom": "V1", "loi": FX}]}}
    gh = {"suites": [{"condition": "retour", "tentatives": [{"k": 1, "loi": SM}, {"k": 2, "loi": SM2}]},
                     {"condition": "temoin", "tentatives": [{"k": 1, "loi": FX}, {"k": 2, "loi": SI0}],
                      **({"interrompue": True} if gh_interrompue else {})}]}
    pv, pg = tmp_path / "v67.json", tmp_path / "gh.json"
    pv.write_text(json.dumps(v67), encoding="utf-8")
    pg.write_text(json.dumps(gh), encoding="utf-8")
    cfg = config_essai()
    prereg = tmp_path / "prereg-essai.md"
    prereg.write_text("préenregistrement d'essai ; bloc d'effort gelé : " + lanceur.empreinte_bloc_effort(cfg) + "\n",
                      encoding="utf-8")
    essais = {"preenregistrement": sha(prereg), "controle_du_code": False, "contre_lecture_exigee": False,
              "compagnon_du_preenregistrement_exige": False, "config": cfg, "evaluateur": EVALUATEUR,
              "sources": {"v67": [str(pv), sha(pv)], "goodhart_v3": [str(pg), sha(pg)]}}
    pe = tmp_path / "essais.json"
    pe.write_text(json.dumps(essais), encoding="utf-8")
    return prereg, pe


def test_lanceur_bout_en_bout_sur_sources_fabriquees(tmp_path):
    prereg, pe = _sources_fabriquees(tmp_path)
    out = tmp_path / "sortie"
    code = lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--essai", "--essais-json", str(pe)])
    assert code == 0
    res = json.loads((out / "sortie-phase0-p1-p2-v1.json").read_text(encoding="utf-8"))
    man = json.loads((out / "manifeste-phase0-p1-p2-v1.json").read_text(encoding="utf-8"))
    assert res["essai"] is True and man["essai"] is True
    assert "verdict_propose_par_le_code" in res["p1"] or "arret" in res["p1"]
    assert res["p2"]["observe"]["repetent"] == 2
    assert res["p2"]["goodhart_description_seulement"]["goodhart_v3"]["retour"]["reproduit_l_analyse"] is True
    for nom in ("sortie-phase0-p1-p2-v1.json", "manifeste-phase0-p1-p2-v1.json", "journal-fichiers-ouverts-phase0-p1-p2-v1.txt"):
        assert (out / (nom + ".sha256")).read_text(encoding="utf-8").split()[0] == sha(out / nom)
    assert man["graines"]["racine"] == RACINE_ESSAI and man["graines"]["taches"]
    # R-3186 P1 a : bloc d'effort gelé au manifeste, avec son empreinte, celle que porte le préenregistrement
    assert man["effort_et_echantillonnage_geles"]["empreinte"] in prereg.read_text(encoding="utf-8")
    assert man["effort_et_echantillonnage_geles"]["bloc"]["p1"]["questions_T"] == 8
    assert set(man["empreintes"]["sources"]) == {"v67", "goodhart_v3"}
    # P1 : verdict, carte à zéro question pour chaque questionneur (R-3186 P1 d), famille A/A avec l'ordre (P1 b), borne (e)
    p1 = res["p1"]
    assert "verdict_propose_par_le_code" in p1, p1
    assert set(p1["carte_a_zero_question_par_questionneur"]) == set(lanceur.BRAS_PRINCIPAL)
    assert set(p1["criteres"]["C-P1-2_famille_aa"]["comparaisons"]) == {"aa_aleatoire", "ordre_aleatoire", "ordre_bissection"}
    assert p1["borne_de_ce_que_l_instrument_permet_de_revendiquer"] == lanceur.BORNE_P1
    # P2 : quota rejoué sur la plage gelée, mention « aucune nouveauté », aucune autre clé qui parle de nouveauté
    assert set(res["p2"]["rejeu_quota_sans_verite"]) == {"1", "2", "3"}
    assert res["p2"]["aucune_nouveaute"] == p2.MENTION_AUCUNE_NOUVEAUTE
    assert [k for k in cles(res) if "nouve" in k.lower()] == ["aucune_nouveaute"]
    # aucune clé en double dans la sortie (relue avec un détecteur de doublons)
    json.loads((out / "sortie-phase0-p1-p2-v1.json").read_text(encoding="utf-8"), object_pairs_hook=sans_doublon)
    # R12 : second lancement dans le même dossier refusé
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--essai", "--essais-json", str(pe)]) == 2


def test_lanceur_refuse_un_preenregistrement_altere(tmp_path):
    prereg, pe = _sources_fabriquees(tmp_path)
    prereg.write_text("préenregistrement d'essai, altéré\n", encoding="utf-8")
    out = tmp_path / "sortie"
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--essai", "--essais-json", str(pe)]) == 2
    assert not out.exists()


def test_lanceur_refuse_le_vrai_preenregistrement_si_empreinte_differente(tmp_path):
    # le vrai préenregistrement, copié puis altéré d'un octet : refus, rien écrit (mode réel, sans essai)
    vrai = ICI / lanceur.NOM_PREENREGISTREMENT
    copie = tmp_path / lanceur.NOM_PREENREGISTREMENT
    copie.write_bytes(vrai.read_bytes() + b" ")
    out = tmp_path / "sortie"
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(copie)]) == 2
    assert not out.exists()
    # cas sain de la garde, sans lancer la configuration : l'empreinte du vrai fichier est celle qu'attend le lanceur
    assert lanceur.exiger_preenregistrement(vrai, lanceur.EMPREINTE_PREENREGISTREMENT, exiger_compagnon=True) == sha(vrai)
    # le vrai préenregistrement porte l'empreinte du bloc d'effort de la configuration réelle (R-3186, P1 a)
    assert lanceur.exiger_bloc_effort(vrai, lanceur.CONFIG) == lanceur.empreinte_bloc_effort(lanceur.CONFIG)
    # et le lancement réel sans contre-lecture est refusé, rien écrit (R-3181)
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(vrai)]) == 2
    assert not out.exists()


def test_lanceur_essai_exige_les_deux_options(tmp_path):
    assert lanceur.principal(["--sortie", str(tmp_path / "x"), "--essai"]) == 2


def cles(o):
    if isinstance(o, dict):
        return [k for k in o] + [x for v in o.values() for x in cles(v)]
    if isinstance(o, list):
        return [x for v in o for x in cles(v)]
    return []


def sans_doublon(paires):
    noms = [k for k, _ in paires]
    assert len(noms) == len(set(noms)), f"clé en double : {noms}"
    return dict(paires)


def test_lanceur_sans_cle_en_double_dans_le_code():
    import ast
    arbre = ast.parse((ICI / "lanceur_phase0_p1p2_v1.py").read_text(encoding="utf-8"))
    for n in ast.walk(arbre):
        if isinstance(n, ast.Dict):
            noms = [k.value for k in n.keys if isinstance(k, ast.Constant)]
            assert len(noms) == len(set(noms)), noms


# --- statistiques gelées : la masse en 0 (défaut relevé) ----------------------------------------------------------------
def test_masse_en_zero_la_mediane_ne_voit_pas_la_moyenne_voit():
    rng = np.random.default_rng(11)
    n = 200
    exact = np.zeros(n)
    exact[rng.permutation(n)[:40]] = rng.exponential(0.5, 40)  # 80 % de divergences nulles
    bruite = exact.copy()
    touches = rng.permutation(n)[:60]  # 30 % des mondes dégradés
    bruite[touches] += rng.exponential(1.0, 60)
    d = qp.bootstrap_double(bruite, exact, np.random.default_rng(12), 2000)
    assert d["medianes"]["point"] == 0.0 and d["medianes"]["ic95"][0] <= 0  # la médiane ne voit rien
    assert lanceur.tient_degradation(d)  # la statistique gelée (moyennes) voit la dégradation
    d0 = qp.bootstrap_double(exact, exact, np.random.default_rng(12), 2000)
    assert not lanceur.tient_degradation(d0)  # artefact : aucune dégradation, la garde échoue


def test_bootstrap_double_bonferroni_plus_large():
    rng = np.random.default_rng(13)
    a, b = rng.normal(0, 1, 100), rng.normal(0, 1, 100)
    d = qp.bootstrap_double(a, b, np.random.default_rng(14), 4000, 3)
    for s in ("medianes", "moyennes"):
        lo, hi = d[s]["ic_corrige"]
        assert lo <= d[s]["ic95"][0] and hi >= d[s]["ic95"][1]
        assert abs(d[s]["niveau_corrige"] - (1 - 0.05 / 3)) < 1e-12
    with pytest.raises(mr.Refus):
        qp.bootstrap_double(a, b[:5], np.random.default_rng(0), 10)
    with pytest.raises(mr.Refus):
        qp.bootstrap_double(a, b, np.random.default_rng(0), 10, 0)


def _comp(med, moy, ic_med, ic_moy, ic_c_med=None, ic_c_moy=None):
    def un(p, ic, icc):
        icc = icc or ic
        return {"point": p, "ic95": list(ic), "largeur95": ic[1] - ic[0], "ic_corrige": list(icc), "niveau_corrige": 0.98}
    return {"medianes": un(med, ic_med, ic_c_med), "moyennes": un(moy, ic_moy, ic_c_moy)}


def test_regles_gelees_ordre_aa_disparition():
    assert lanceur.tient_ordre(_comp(0.3, 0.4, (0.1, 0.5), (0.2, 0.6)))
    assert not lanceur.tient_ordre(_comp(0.3, 0.4, (0.0, 0.5), (0.2, 0.6)))  # médiane touche 0
    assert not lanceur.tient_ordre(_comp(0.0, 0.4, (0.0, 0.0), (0.2, 0.6)))  # masse en 0 : médiane muette
    ecarts = {"medianes": 1.0, "moyennes": 1.0}
    assert lanceur.tient_aa(_comp(0.0, 0.01, (-0.2, 0.2), (-0.2, 0.2)), ecarts, 0.5)["tient"]
    assert not lanceur.tient_aa(_comp(0.0, 0.01, (-0.4, 0.4), (-0.2, 0.2)), ecarts, 0.5)["tient"]  # trop large
    assert not lanceur.tient_aa(_comp(0.3, 0.3, (0.1, 0.4), (0.1, 0.4), (0.05, 0.45), (0.05, 0.45)), ecarts, 0.5)["tient"]
    assert not lanceur.tient_aa(_comp(0.0, 0.0, (-0.1, 0.1), (-0.1, 0.1)), {"medianes": 0.0, "moyennes": 1.0}, 0.5)["tient"]
    assert lanceur.tient_disparition(_comp(-0.1, 0.0, (-0.3, 0.1), (-0.2, 0.2)))
    assert not lanceur.tient_disparition(_comp(-0.1, 0.2, (-0.3, 0.1), (0.05, 0.3)))  # la moyenne voit encore l'avantage


def test_verdict_p1_table_gelee():
    assert lanceur.verdict_p1(True, True, True, True).startswith("instrument discriminant")
    assert lanceur.verdict_p1(False, True, True, True).startswith("garde défaillante")
    assert lanceur.verdict_p1(False, False, False, False).startswith("garde défaillante")
    assert lanceur.verdict_p1(True, False, True, True).startswith("instrument non discriminant (ordre)")
    assert lanceur.verdict_p1(True, True, False, True).startswith("instrument non discriminant (A/A)")
    assert lanceur.verdict_p1(True, True, True, False).startswith("instrument sensible à l'ordre")


def test_decision_p2_table_gelee():
    d = lanceur.decision_p2(8 / 23, 8 / 23, 8 / 23, 4 / 14, 2 / 14, 0.4, 0.25, 23)
    assert d["ferme"] and d["lectures"] == [] and not d["audit_symetrie_R4_declenche"]
    d = lanceur.decision_p2(3 / 23, 3 / 23, 3 / 23, 1 / 14, 2 / 14, 0.01, 0.25, 23)
    assert not d["ferme"] and "au-dessus du quantile 95 %" in d["lectures"][0] and any("A-1" in x for x in d["lectures"])
    d = lanceur.decision_p2(3 / 23, 3 / 23, 3 / 23, 1 / 14, 5 / 14, 0.2, 0.25, 23)
    assert "non distincte" in d["lectures"][0] and not any("A-1" in x for x in d["lectures"])
    d = lanceur.decision_p2(7 / 23, 5 / 23, 4 / 23, 1 / 14, 2 / 14, 0.3, 0.25, 23)
    assert d["ferme"] and d["audit_symetrie_R4_declenche"]
    assert {x[:3] for x in d["lectures"]} == {"A-1", "P-8", "A-3"}


# --- ordre de présentation (R-3186, P1 b) -------------------------------------------------------------------------------
def test_ordre_de_presentation_seul_change_avec_le_bras_ordre(petits_mondes):
    b = banc(petits_mondes, ("aleatoire", "aleatoire#ordre"), "ord")
    assert [p["posees"] for p in b["aleatoire"]] == [p["posees"] for p in b["aleatoire#ordre"]]  # même graine
    assert [p["posees_au_monde"] for p in b["aleatoire"]] != [p["posees_au_monde"] for p in b["aleatoire#ordre"]]


def test_ordre_non_permutation_refuse(petits_mondes):
    espace, mondes = petits_mondes
    q = qp.Aleatoire(np.random.default_rng(0))
    rep = mr.Repondeur(espace["A"][mondes[0], :42])
    with pytest.raises(mr.Refus):
        qp.jouer_partie(espace, mondes[0], q, rep, 4, (0, 4), 42, None, list(range(41)) + [0])
    p = qp.jouer_partie(espace, mondes[0], q, rep, 4, (0, 4), 42, None, list(range(42))[::-1])
    assert p["posees_au_monde"] == [41 - k for k in p["posees"]]


def test_famille_aa_et_ordre_sur_petits_mondes(petits_mondes):
    b = banc(petits_mondes, ("aleatoire", "aleatoire#2", "aleatoire#ordre", "bissection", "bissection#ordre"), "fam")
    ecart = qp.bootstrap_double(kl16(b, "aleatoire"), kl16(b, "bissection"), np.random.default_rng(20), 2000)
    ecarts = {s: ecart[s]["point"] for s in ("medianes", "moyennes")}
    for i, (nom, x, y) in enumerate(lanceur.FAMILLE_AA):
        comp = qp.bootstrap_double(kl16(b, x), kl16(b, y), np.random.default_rng(21 + i), 2000, 3)
        r = lanceur.tient_aa(comp, ecarts, 0.5)
        assert all(d["contient_0"] for d in r["detail"].values()), (nom, r)


# --- règle des refus (R-3186, P1 c) -------------------------------------------------------------------------------------
def test_question_absente_arret_ou_question_perdue(petits_mondes):
    class Muet(qp.Questionneur):
        nom = "muet"

        def choisir(self, etat):
            return None if len(etat["posees"]) % 2 == 0 else 0

    espace, mondes = petits_mondes
    rep = mr.Repondeur(espace["A"][mondes[0], :42])
    with pytest.raises(mr.Refus):
        qp.jouer_partie(espace, mondes[0], Muet(None), rep, 4, (0, 4), 42, politique_refus="arret")
    rep2 = mr.Repondeur(espace["A"][mondes[0], :42])
    p = qp.jouer_partie(espace, mondes[0], Muet(None), rep2, 4, (0, 4), 42, politique_refus="question_perdue")
    assert p["questions_perdues"] == 4 and p["posees"] == [] and p["refus_hors_grammaire"] == 4
    assert p["cartes"][4]["taille_S"] == len(espace["lois"])  # aucune mise à jour : ni Oui, ni Non, ni Inconnu
    with pytest.raises(mr.Refus):
        qp.jouer_partie(espace, mondes[0], Muet(None), rep2, 4, (0, 4), 42, politique_refus="repli")


def test_questions_reposees_comptees(petits_mondes):
    espace, mondes = petits_mondes
    q = qp.Repeteur(np.random.default_rng(5))
    p = qp.jouer_partie(espace, mondes[0], q, mr.Repondeur(espace["A"][mondes[0], :42]), 16, (0, 16), 42)
    assert p["questions_reposees"] == 1  # 15 prédicats dans la direction z0 : la 16e question en repose un


def test_carte_du_proposeur_saine_et_artefacts():
    for loi in (SM, FX, SI0, mr.tirer_loi(np.random.default_rng(3))):
        assert mr.carte_du_proposeur(loi) == (loi, False, "")
    for artefact in (None, "softmax", {"type": "inconnu"}, {"type": "fixe", "probas": [0.5, 0.5]},
                     {"type": "softmax", "poids": [[1, 2]], "biais": [0, 0, 0]},
                     {"type": "transformee", "base": FX, "fuite": 1},
                     {"type": "fixe", "probas": [float("nan"), 0.5, 0.5]}):
        loi, refusee, motif = mr.carte_du_proposeur(artefact)
        assert refusee and motif and loi == mr.CARTE_DE_REMPLACEMENT


# --- quota (R-3186, P2 a) et nouveauté (P2 d) ---------------------------------------------------------------------------
def test_quota_a_la_main_et_sans_oracle():
    cartes = cartes_fabriquees() + [carte(1, "kimi", 3, SM), carte(1, "kimi", 4, SM2)]
    r1 = p2.rejeu_quota(cartes, 1)
    assert r1["refusees"] == 3 and r1["identifiants"] == ["G1-kimi-02", "G1-kimi-03", "G1-kimi-04"]
    assert p2.rejeu_quota(cartes, 2)["refusees"] == 2 and p2.rejeu_quota(cartes, 3)["refusees"] == 1
    # artefact : des champs d'oracle et de verdict changés ne changent rien (ils ne sont jamais lus)
    avec_oracle = [{**c, "promue": i % 2 == 0, "verdict": "survit", "oracle": {"vraie": True}} for i, c in enumerate(cartes)]
    assert p2.rejeu_quota(avec_oracle, 2) == p2.rejeu_quota(cartes, 2)
    for q in (0, 4, 2.0, True):
        with pytest.raises(mr.Refus):
            p2.rejeu_quota(cartes, q)
    with pytest.raises(mr.Refus):
        p2.rejeu_quota([{"generation": 1, "proposeur": "kimi", "loi": SM}], 2)


def test_suite_interrompue_arrete_p2(tmp_path):
    prereg, pe = _sources_fabriquees(tmp_path, gh_interrompue=True)
    cfg = config_essai()
    boucle = json.loads((tmp_path / "v67.json").read_text(encoding="utf-8"))
    gh = json.loads((tmp_path / "gh.json").read_text(encoding="utf-8"))
    with pytest.raises(lanceur.Refus):
        lanceur.phase_p2(cfg, RACINE_ESSAI, boucle, {"goodhart_v3": gh}, [])
    sain = {"suites": [s for s in gh["suites"] if not s.get("interrompue")]}
    assert "goodhart_v3" in lanceur.phase_p2(cfg, RACINE_ESSAI, boucle, {"goodhart_v3": sain}, [])["goodhart_description_seulement"]


# --- gardes du lancement ------------------------------------------------------------------------------------------------
def test_garde_bloc_effort_saine_et_artefact(tmp_path):
    cfg = config_essai()
    p = tmp_path / "pr.md"
    p.write_text("empreinte : " + lanceur.empreinte_bloc_effort(cfg) + "\n", encoding="utf-8")
    assert lanceur.exiger_bloc_effort(p, cfg) == lanceur.empreinte_bloc_effort(cfg)
    autre = json.loads(json.dumps(cfg))
    autre["p1"]["questions_T"] = 9  # budget de questions changé après le préenregistrement
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_bloc_effort(p, autre)
    autre = json.loads(json.dumps(cfg))
    autre["p2"]["tirages_reference"] = 21
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_bloc_effort(p, autre)


def test_garde_contre_lecture_saine_et_artefacts(tmp_path):
    e = "a" * 64
    cl = tmp_path / "cl.md"
    cl.write_text(f"contre-lecture du préenregistrement {e} : tient\n", encoding="utf-8")
    (tmp_path / "cl.md.sha256").write_text(f"{sha(cl)}  cl.md\n", encoding="utf-8")
    assert lanceur.exiger_contre_lecture(cl, e) == sha(cl)
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_contre_lecture(cl, "b" * 64)  # ne cite pas l'empreinte lancée
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_contre_lecture(None, e)  # absente
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_contre_lecture(tmp_path / "absente.md", e)
    cl.write_text(f"contre-lecture du préenregistrement {e} : tient, retouchée\n", encoding="utf-8")
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_contre_lecture(cl, e)  # compagnon non conforme


def test_garde_compagnon_du_preenregistrement(tmp_path):
    p = tmp_path / "pr.md"
    p.write_text("gelé\n", encoding="utf-8")
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_preenregistrement(p, sha(p), exiger_compagnon=True)
    (tmp_path / "pr.md.sha256").write_text(f"{'0' * 64}  pr.md\n", encoding="utf-8")
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_preenregistrement(p, sha(p), exiger_compagnon=True)
    (tmp_path / "pr.md.sha256").write_text(f"{sha(p)}  pr.md\n", encoding="utf-8")
    assert lanceur.exiger_preenregistrement(p, sha(p), exiger_compagnon=True) == sha(p)


def test_lanceur_essai_refuse_sans_contre_lecture(tmp_path):
    prereg, pe = _sources_fabriquees(tmp_path)
    essais = json.loads(pe.read_text(encoding="utf-8"))
    essais["contre_lecture_exigee"] = True
    pe.write_text(json.dumps(essais), encoding="utf-8")
    out = tmp_path / "sortie"
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--essai", "--essais-json", str(pe)]) == 2
    assert not out.exists()
    cl = tmp_path / "cl.md"
    cl.write_text(f"relu : {sha(prereg)}\n", encoding="utf-8")
    (tmp_path / "cl.md.sha256").write_text(f"{sha(cl)}  cl.md\n", encoding="utf-8")
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--contre-lecture", str(cl),
                              "--essai", "--essais-json", str(pe)]) == 0
    man = json.loads((out / "manifeste-phase0-p1-p2-v1.json").read_text(encoding="utf-8"))
    assert man["empreintes"]["contre_lecture"] == sha(cl)


def test_garde_de_disjonction_trop_de_retraits(monkeypatch):
    rng = np.random.default_rng(1)
    Z, G = mr.tirer_sonde(rng, 32)
    monkeypatch.setattr(qp, "disjointe", lambda p, refs: False)  # artefact : toute candidate trop proche
    with pytest.raises(mr.Refus):
        qp.construire_espace(np.random.default_rng(2), 3, (Z, G), (Z, G), [np.full((32, 3), 1 / 3)])

