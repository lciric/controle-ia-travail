"""Pilote de l'environnement (a) (T0.5), sur modèle jouet : plan des épisodes, jeu par lots, notation, appariement."""
from __future__ import annotations

import json

import numpy as np
import pytest
import torch

from controle_ia.environnements import pilote_a as pa
from controle_ia.gardes import GardeArret
from controle_ia.harnais.formats import FormatChat
from controle_ia.harnais.modeles import modele_jouet, regler_determinisme, tokeniseur_caracteres_chat
from controle_ia.manifeste import generateur, graines
from controle_ia.scellement import sceller

regler_determinisme(1)
TOK = tokeniseur_caracteres_chat()
FMT = FormatChat(TOK, fins={TOK.convert_tokens_to_ids("<|im_end|>"), TOK.eos_token_id})
CONFIG = {"N": 1, "T": 2, "episodes_par_tache": 2, "lot": 3, "max_nouveaux": 6, "temperature": 1.0,
          "couches": [0, 1, 2], "fraction_equivalence": 0.5, "statistique_equivalence": "max",
          "tolerance_equivalence": 1e-4, "positions_min_controle_negatif": 4, "actions_min_controle_negatif": 10,
          "fraction_min_controle_negatif": 0.95}
TACHES = [{"identifiant": "2506.00001v1", "questions": "Why do routers matter?",
           "classification": {"theory_experiment": "mostly_experiments", "data_type": "real_only", "domains": []}},
          {"identifiant": "2506.00002v1", "questions": "How to calibrate?", "classification": None}]


def _modele():
    return modele_jouet(5, len(TOK), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)


def _generateurs(plan, entropie=7):
    g = graines([e for e, _ in plan], entropie)
    return {e: generateur(g[e]) for e, _ in plan}


def test_config_incomplete_arrete():
    pa.exiger_config(CONFIG)
    with pytest.raises(GardeArret, match="incomplète"):
        pa.exiger_config({k: v for k, v in CONFIG.items() if k != "lot"})


def test_charger_taches(tmp_path):
    f = tmp_path / "taches.json"
    f.write_text(json.dumps({"taches": TACHES}), encoding="utf-8")
    with pytest.raises(GardeArret):
        pa.charger_taches(f)  # non scellé
    sceller(f)
    assert [t["identifiant"] for t in pa.charger_taches(f)] == ["2506.00001v1", "2506.00002v1"]
    for contenu, motif in [({"taches": TACHES + TACHES[:1]}, "double"),
                           ({"taches": [{"identifiant": "x", "questions": " "}]}, "sans énoncé")]:
        g = tmp_path / f"t-{motif[:4]}.json"
        g.write_text(json.dumps(contenu), encoding="utf-8")
        sceller(g)
        with pytest.raises(GardeArret, match=motif):
            pa.charger_taches(g)


def test_plan_et_graines_deterministes():
    plan = pa.plan_des_episodes(TACHES, 2)
    assert [e for e, _ in plan] == ["2506.00001v1/e0", "2506.00001v1/e1", "2506.00002v1/e0", "2506.00002v1/e1"]
    a = pa.graines_des_actions(_generateurs(plan)["2506.00001v1/e0"], 2, 3)
    b = pa.graines_des_actions(_generateurs(plan)["2506.00001v1/e0"], 2, 3)
    assert a == b and sorted(a) == [(i, t) for i in range(2) for t in range(3)]
    with pytest.raises(GardeArret):
        pa.plan_des_episodes(TACHES, 0)


def test_jouer_pilote_par_lots_et_rejeu():
    plan = pa.plan_des_episodes(TACHES, 2)
    m = _modele()
    fiches, vecteurs, cn = pa.jouer_pilote(m, FMT, plan, _generateurs(plan), CONFIG)
    assert [f["episode"] for f in fiches] == [e for e, _ in plan]
    assert cn["lecture"] in ("conforme", "non concluant") and cn["positions_min"] == 4
    a0 = fiches[0]["actions"][0]
    assert a0["texte"] and len(a0["ids"]) == fiches[0]["jetons_par_action"][0] and a0["fin"] - a0["debut"] == len(a0["ids"])
    eq = next(f["equivalence"] for f in fiches if f["equivalence"]["actions"])
    assert set(eq["controle_negatif_zone_generee"]) == set(eq["actions"]) == set(eq["longueurs_contexte"])
    assert all(f["bilan"]["actions"] == 2 for f in fiches) and sum(len(f["equivalence"]["actions"]) for f in fiches) > 0
    assert set(vecteurs) == {f"{e}|{c}" for e, _ in plan for c in CONFIG["couches"]}
    assert vecteurs["2506.00001v1/e0|1"].shape == (1, 2, 32) and vecteurs["2506.00001v1/e0|1"].dtype == np.float16
    rejeu, _, _ = pa.jouer_pilote(m, FMT, plan, _generateurs(plan), CONFIG)
    assert [f["empreintes"] for f in rejeu] == [f["empreintes"] for f in fiches]


def test_controle_negatif_du_pilote_cas_sain_et_artefacts():
    """R5, dans le chemin du pilote : cas sain (contrôle négatif vu) ; artefact 1 : tolérance aberrante, la garde est
    aveugle au décalage d'un jeton (arrêt de phase) ; artefact 2 : défaut D1 injecté (arrêt de la garde immédiate)."""
    plan = pa.plan_des_episodes(TACHES, 2)
    sain = {**CONFIG, "fraction_equivalence": 1.0, "positions_min_controle_negatif": 1, "actions_min_controle_negatif": 1}
    _, _, cn = pa.jouer_pilote(_modele(), FMT, plan, _generateurs(plan), sain, garder_vecteurs=False)
    assert cn["lecture"] == "conforme" and cn["comparables"] >= 1 and cn["fraction"] >= 0.95
    with pytest.raises(GardeArret, match="aveugle au décalage"):
        pa.jouer_pilote(_modele(), FMT, plan, _generateurs(plan), {**sain, "tolerance_equivalence": 1e9},
                        garder_vecteurs=False)
    with pytest.raises(GardeArret):
        pa.jouer_pilote(_modele(), FMT, plan, _generateurs(plan), sain, garder_vecteurs=False, decalage_positions=1)


def test_jouer_pilote_generateur_manquant_arrete():
    plan = pa.plan_des_episodes(TACHES, 1)
    with pytest.raises(GardeArret, match="générateurs absents"):
        pa.jouer_pilote(_modele(), FMT, plan, {}, CONFIG)


def test_noter_ensembles_sans_imputation():
    demandes = [{"cle": f"j{k}", "questions": "Why?", "ensemble": "PROPOSAL 1: x", "classification": None,
                 "variante": v} for k, v in enumerate(["b0", "b*"])]
    sorties = pa.noter_ensembles(_modele(), FMT, demandes, {"j0": 1, "j1": 2}, lot=2, max_nouveaux=5, temperature=1.0)
    assert [s["cle"] for s in sorties] == ["j0", "j1"]
    assert all(s["score"] is None and s["anomalies"] and s["jetons_reponse"] <= 5 for s in sorties)


def test_logits_independants_du_remplissage():
    m = _modele()
    contextes = [FMT.ouverture("s", "court"), FMT.ouverture("système plus long", "observation bien plus longue")]
    lot = pa.logits_derniere_position(m, contextes, TOK.pad_token_id)
    seuls = torch.cat([pa.logits_derniere_position(m, [c], TOK.pad_token_id) for c in contextes])
    assert torch.allclose(lot, seuls, atol=1e-5)
    with pytest.raises(GardeArret):
        pa.logits_derniere_position(m, [[]], TOK.pad_token_id)


def test_jetons_oui_non():
    with pytest.raises(GardeArret, match="un seul jeton"):
        pa.jetons_oui_non(TOK)  # tokeniseur par caractères : « Yes » fait trois jetons

    class Tok:
        def encode(self, s, add_special_tokens=False):
            return {"Yes": [7], "No": [9]}[s]

    assert pa.jetons_oui_non(Tok()) == (7, 9)


def test_apparier_probabilites(monkeypatch):
    monkeypatch.setattr(pa, "jetons_oui_non", lambda tok: (TOK.convert_tokens_to_ids("Y"), TOK.convert_tokens_to_ids("N")))
    paires = [{"cle": f"p{k}", "proposition": "Train a dense baseline.", "cible": c}
              for k, c in enumerate(["a dense baseline", "an ablation"])]
    s = pa.apparier(_modele(), FMT, paires, lot=2)
    assert [x["cle"] for x in s] == ["p0", "p1"] and all(0.0 <= x["p_oui"] <= 1.0 and x["masse_oui_non"] > 0 for x in s)


# --- analyse -----------------------------------------------------------------------------------------------

from controle_ia.environnements import analyse_pilote as ap  # noqa: E402


def _simuler(n, sb=2.0, sd=1.0, se=1.5, graine=3):
    r = np.random.default_rng(graine)
    beta, d1, d2 = r.normal(0, sb, n), r.normal(0, sd, n), r.normal(0, sd, n)
    e = r.normal(0, se, (3, n))
    return 50 + beta + d1 + e[0], 50 + beta + d1 + e[1], 50 + beta + d2 + e[2]


def test_decomposition_retrouve_les_composantes_simulees():
    d = ap.decomposition_variance(*_simuler(40000))
    vrai = {"tache": 4.0, "generation": 1.0, "juge": 2.25}
    for k, v in vrai.items():
        assert d["composantes"][k] == pytest.approx(v, rel=0.06), k
    assert d["parts"]["juge"] == pytest.approx(2.25 / 7.25, abs=0.02) and d["taches_incompletes"] == 0


def test_decomposition_sans_imputation_et_gardes():
    a, b, c = (x[:10].copy() for x in _simuler(10))
    a[0] = np.nan
    d = ap.decomposition_variance(a, b, c)
    assert d["taches"] == 9 and d["taches_incompletes"] == 1
    with pytest.raises(GardeArret, match="alignées"):
        ap.decomposition_variance(a, b[:5], c)
    with pytest.raises(GardeArret, match="impossible"):
        ap.decomposition_variance([1.0, np.nan], [1.0, 2.0], [1.0, 2.0])


def test_intervalles_contiennent_la_valeur_simulee():
    iv = ap.intervalles_parts(*_simuler(400, graine=8), tirages=300, rng=np.random.default_rng(1))
    assert iv["juge"][0] < 2.25 / 7.25 < iv["juge"][1]


def test_kappa():
    x = np.array([1, 0, 1, 1, 0, 0, 1, 0], dtype=bool)
    assert ap.kappa_cohen(x, x) == 1.0
    assert ap.kappa_cohen(x, ~x) == -1.0
    with pytest.raises(GardeArret, match="indéfini"):
        ap.kappa_cohen([1, 1], [1, 1])
    with pytest.raises(GardeArret):
        ap.kappa_cohen([1, 0], [1])


def test_couverture():
    p = {(1, "C1"): 0.9, (1, "C2"): 0.2, (2, "C1"): 0.1, (2, "C2"): 0.6}
    assert ap.couverture(p, [1, 2], ["C1", "C2"]) == {"part": 1.0, "couvertes": ["C1", "C2"]}
    assert ap.couverture(p, [1], ["C1", "C2"])["part"] == 0.5
    with pytest.raises(GardeArret, match="absentes"):
        ap.couverture(p, [1, 3], ["C1"])


# --- lanceur (mode jouet, dépôt jetable) -------------------------------------------------------------------

from controle_ia.environnements import lancer_pilote_a as lp  # noqa: E402
from conftest import committer  # noqa: E402


def _config_lanceur():
    return {**CONFIG, "episodes_par_tache": 2, "episodes_notes_deux_fois": [0], "lot_juge": 2,
            "max_nouveaux_juge": 6, "temperature_juge": 1.0, "variante_juge": "b0", "lot_appariement": 4,
            "duree_max_s": 600, "mode": "jouet", "agent": {"nom": "agent-jouet"}, "noyau_attention": "math", "fils": 1,
            "juges": [{"nom": "jouet-8B", "meme_modele_que_agent": True, "sert_a_l_appariement": True},
                      {"nom": "jouet-3B", "meme_modele_que_agent": False, "sert_a_l_appariement": False}]}


def test_lanceur_de_bout_en_bout_en_mode_jouet(depot, monkeypatch):
    monkeypatch.setattr(pa, "jetons_oui_non",
                        lambda tok: (tok.convert_tokens_to_ids("Y"), tok.convert_tokens_to_ids("N")))
    taches = [dict(t, cibles={"controls": [{"id": "C1", "description": "a dense baseline"}],
                              "fruitful_directions": [], "sterile_directions": []}) for t in TACHES]
    f = depot / "taches.json"
    f.write_text(json.dumps({"taches": taches}), encoding="utf-8")
    sceller(f)
    committer(depot)
    resume = lp.executer(_config_lanceur(), depot, "20261006-170000-pilote-jouet", None, str(f),
                         autoriser_depot_sale=True)
    assert resume["episodes"] == 4 and resume["actions"] == 8
    assert set(resume["notations"]) == {"jouet-8B", "jouet-3B"}
    d = depot / "diag" / "20261006-170000-pilote-jouet"
    assert {p.name for p in d.glob("*.json")} >= {"episodes.json", "notations-jouet-8B.json", "notations-jouet-3B.json",
                                                   "appariements.json", "resume.json"}
    assert (depot / "donnees" / "20261006-170000-pilote-jouet" / "vecteurs-par-action.npz.sha256").exists()
    with pytest.raises(GardeArret, match="R12"):
        lp.executer(_config_lanceur(), depot, "20261006-170000-pilote-jouet", None, str(f), autoriser_depot_sale=True)


def _taches_scellees(depot):
    taches = [dict(t, cibles={"controls": [{"id": "C1", "description": "a dense baseline"}],
                              "fruitful_directions": [], "sterile_directions": []}) for t in TACHES]
    f = depot / "taches.json"
    f.write_text(json.dumps({"taches": taches}), encoding="utf-8")
    sha = sceller(f)
    return f, sha


def _prereg_pilote(depot, commit, config, sha_taches, entropie=4242, nom="prereg-pilote.md"):
    (depot / "prereg").mkdir(exist_ok=True)
    p = depot / "prereg" / nom
    lignes = [f"- Commit du code d'analyse : `{commit}`",
              f"- Configuration du pilote (empreinte canonique) : `{lp.empreinte_config(config)}`",
              f"- Tâches du pilote : `{sha_taches}`", f"- Entropie : `{entropie}`"]
    corps = ["# Préenregistrement de test", "", *lignes, ""]
    for s in ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
              "Critères de lecture gelés", "Liste d'arrêt"):
        corps += [f"## {s}", "", f"contenu {s}", ""]
    corps += ["## Contre-lecture", "", f"brouillon relu `{'a' * 64}`, rapport `{'b' * 64}`", ""]
    p.write_text("\n".join(corps), encoding="utf-8")
    sceller(p)
    return p


def _commit(depot):
    import subprocess
    return subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True,
                          check=True).stdout.strip()


def test_lanceur_gardes_de_citation_cas_sain_et_artefacts(depot, monkeypatch):
    """R1, R5 : un run avec préenregistrement ne part que si le commit, la configuration, les tâches et l'entropie
    sont ceux que cite le préenregistrement ; sinon arrêt avant tout manifeste."""
    monkeypatch.setattr(pa, "jetons_oui_non",
                        lambda tok: (tok.convert_tokens_to_ids("Y"), tok.convert_tokens_to_ids("N")))
    monkeypatch.setattr(lp, "exiger_code_importe_sous", lambda racine: None)  # code importé du vrai dépôt (testé ailleurs)
    f, sha = _taches_scellees(depot)
    committer(depot)
    commit, config = _commit(depot), _config_lanceur()
    sain = _prereg_pilote(depot, commit, config, sha)
    autre_config = _prereg_pilote(depot, commit, dict(config, lot_juge=3), sha, nom="p-config.md")
    autres_taches = _prereg_pilote(depot, commit, config, "c" * 64, nom="p-taches.md")
    (depot / "prereg" / "p-sans.md").write_text(f"- Commit du code d'analyse : `{commit}`\n", encoding="utf-8")
    committer(depot)                                            # préenregistrements : hors de l'arbre gelé
    for p, motif in ((autre_config, "configuration .* citée"), (autres_taches, "tâches .* citées"),
                     (depot / "prereg" / "p-sans.md", "ne cite pas la configuration")):
        with pytest.raises(GardeArret, match=motif):
            lp.executer(config, depot, "20261006-170002-pilote-jouet", str(p), str(f))
        assert not (depot / "runs" / "20261006-170002-pilote-jouet").exists()
    resume = lp.executer(config, depot, "20261006-170003-pilote-jouet", str(sain), str(f),
                         autoriser_depot_sale=True)
    assert resume["commit_cite"] == commit and resume["taches_sha256"] == sha
    m = json.loads((depot / "runs" / "20261006-170003-pilote-jouet" / "manifeste.json").read_text(encoding="utf-8"))
    assert m["decisif"] and m["preenregistrement"]["chemin"] == "prereg/prereg-pilote.md"
    assert {g["entropie"] for g in m["graines"].values()} == {"4242"}
    (depot / "nouveau_code.py").write_text("x = 1\n")         # artefact : arbre gelé modifié après le commit cité
    committer(depot)
    with pytest.raises(GardeArret, match="arbre gelé"):
        lp.executer(config, depot, "20261006-170004-pilote-jouet", str(sain), str(f),
                    autoriser_depot_sale=True)


def test_lanceur_reel_sans_preenregistrement_arrete(depot):
    c = dict(_config_lanceur(), mode="reel")
    with pytest.raises(GardeArret, match="R1"):
        lp.executer(c, depot, "20261006-170005-x", None, "inexistant.json")
    assert not (depot / "runs").exists()


def test_lanceur_arret_consigne_apres_le_manifeste(depot, monkeypatch):
    """Une panne après le manifeste laisse un arret.json scellé (étape, motif, partiel), puis se propage."""
    from controle_ia.manifeste import verifier_resultat

    def panne(*a, **k):
        raise GardeArret("panne simulée du juge")
    monkeypatch.setattr(lp, "noter_ensembles", panne)
    f, _ = _taches_scellees(depot)
    committer(depot)
    with pytest.raises(GardeArret, match="panne simulée"):
        lp.executer(_config_lanceur(), depot, "20261006-170006-pilote-jouet", None, str(f))
    arret = depot / "diag" / "20261006-170006-pilote-jouet" / "arret.json"
    corps = verifier_resultat(depot, arret)
    r = corps["resultat"]
    assert r["etape"] == "notation par jouet-8B" and "panne simulée" in r["motif"]
    assert r["partiel"]["episodes_ecrits"] == 4
    assert (depot / "diag" / "20261006-170006-pilote-jouet" / "episodes.json").exists()


def test_jetons_jouet_et_lanceur_sans_substitution(depot, monkeypatch):
    """Le mode jouet apparie avec « Y » et « N » sans substituer `jetons_oui_non` (répétition de l'instance) ; le
    modèle jouet ne produit pas de proposition valide : deux paires sont fournies au lanceur."""
    assert pa.jetons_jouet(TOK) == (TOK.convert_tokens_to_ids("Y"), TOK.convert_tokens_to_ids("N"))
    with pytest.raises(GardeArret, match="un seul jeton"):
        pa.jetons_oui_non(TOK)                                  # artefact : sans la paire jouet, l'appariement arrête
    monkeypatch.setattr(lp, "paires_d_appariement", lambda fiches, par_id: [
        {"cle": "t/e0/1/C1", "proposition": "a dense baseline", "cible": "a dense baseline"},
        {"cle": "t/e0/1/C2", "proposition": "x", "cible": "y"}])
    f, _ = _taches_scellees(depot)
    committer(depot)
    resume = lp.executer(_config_lanceur(), depot, "20261006-170007-pilote-jouet", None, str(f))
    app = json.loads((depot / "diag" / "20261006-170007-pilote-jouet" / "appariements.json").read_text(encoding="utf-8"))
    assert resume["episodes"] == 4 and app["resultat"]["appariements"]
    assert all(0.0 <= a["p_oui"] <= 1.0 for a in app["resultat"]["appariements"])


def test_signal_term_devient_un_arret_consigne():
    with pytest.raises(GardeArret, match="TERM"):
        lp._signal_term(15, None)


def test_lanceur_configuration_incomplete(depot):
    c = _config_lanceur()
    del c["lot_juge"]
    with pytest.raises(GardeArret, match="incomplète"):
        lp.executer(c, depot, "20261006-170001-x", None, "inexistant.json")


def test_passes_et_demandes():
    c = _config_lanceur()
    assert lp.passes_de("2506.00001v1/e0", c) == 2 and lp.passes_de("2506.00001v1/e1", c) == 1
    fiches = [{"episode": "t/e0", "tache": "t", "bilan": {"ensemble": "PROPOSAL 1: x", "propositions": []}},
              {"episode": "t/e1", "tache": "t", "bilan": {"ensemble": "  ", "propositions": []}}]
    d = lp.demandes_de_notation(fiches, {"t": {"questions": "Q?"}}, c, "j")
    assert [x["cle"] for x in d] == ["juge-j/t/e0/passe-0", "juge-j/t/e0/passe-1"]
