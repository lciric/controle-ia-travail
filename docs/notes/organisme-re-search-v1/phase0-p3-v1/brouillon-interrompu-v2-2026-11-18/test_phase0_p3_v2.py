"""Essais (R5) de la phase 0 de P3 — v2 (modèle I, auteur unique). Fichier neuf (R12) ; ceux de la v1 restent en place.

Chaque garde est essayée sur un cas sain et sur un artefact. Petits mondes d'essai seulement (racine 4242, 256 lois,
64 mondes), jamais la configuration du préenregistrement ; sources fabriquées. Le code de P1 est réemployé sans
modification. Aucun essai ne peut lancer la configuration réelle : là où `principal` est appelé en mode réel, une
sentinelle remplace le déroulement et fait échouer l'essai s'il était atteint (C-8).
Lancement : cd <ce dossier> && PYTHONDONTWRITEBYTECODE=1 python3 -B -m pytest -q -p no:cacheprovider test_phase0_p3_v2.py
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path

import numpy as np
import pytest

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))

import lanceur_phase0_p3_v2 as lanceur  # noqa: E402
import panorama_p3_v2 as pp  # noqa: E402
import mondes_reponses_p1p2_v1 as mr  # noqa: E402
import questionneurs_p1_v2 as qp  # noqa: E402

EVALUATEUR = "/home/user/ideation-organism/orchestrator/pole/evaluateur_lois_v62.py"
RACINE_ESSAI = 4242
K, T, SEUIL = 8, 4, 0.30
FX = {"type": "fixe", "probas": [0.2, 0.3, 0.5]}
SM = {"type": "softmax", "poids": [[1.0, 0.0], [0.0, 1.0], [-1.0, -1.0]], "biais": [0.0, 0.1, -0.1]}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def g(nom):
    return mr.generateur(nom, RACINE_ESSAI)


@pytest.fixture(scope="module")
def petit_banc():
    sq = mr.tirer_sonde(g("essai/sq"), 512)
    ss = mr.tirer_sonde(g("essai/ss"), 128)
    espace = qp.construire_espace(g("essai/espace"), 256, sq, ss)
    fams, index = pp.index_familles(espace)
    paires, ecartes = pp.tirer_paires(espace, fams, index, 64, g("essai/mondes"), lambda a: g(f"essai/leurre/{a}"),
                                      lambda i: g(f"essai/roles/{i}"), SEUIL, 256)
    positions = pp.plan_positions(g("essai/plan"), 64, K)
    pans, hist = [], []
    for i, (pr, p) in enumerate(zip(paires, positions)):
        w, l = pr["monde"], pr["leurre"]
        remp = pp.choisir_remplisseurs(espace, w, l, fams, g(f"essai/remp/{i}"), K - 1, SEUIL)
        pan = pp.construire_panorama(w, l, remp, int(p), K)
        pp.exiger_panorama(pan, fams, K, espace, SEUIL)
        pans.append(pan)
        ordre, traits = qp.ordre_de_presentation(g(f"essai/hist/{i}/ordre"), 42)
        partie = qp.jouer_partie(espace, w, qp.Aleatoire(g(f"essai/hist/{i}/q")), mr.Repondeur(espace["A"][w, :42]), 8, (),
                                 42, None, ordre, traits)
        hist.append(pp.historique_de(espace, w, partie["posees_au_monde"], T))
    return espace, fams, index, paires, pans, hist, ecartes


def outils_essai():
    cache = {}

    def outils_de(spec):
        nom = spec.partition(":")[0]
        if nom not in cache:
            cache[nom] = {"sonde": mr.tirer_sonde(g(f"essai/fs/{nom}/s"), 128), "sonde_q": mr.tirer_sonde(g(f"essai/fs/{nom}/q"), 512)}
        return cache[nom]
    return outils_de


def rng_carte(prefixe="essai"):
    return lambda spec, bras, ordre, i: g(f"{prefixe}/carte/{spec}/{bras}/{ordre}/{i}")


# --- familles, paires, plan, panoramas ---------------------------------------------------------------------------------
def test_famille_et_noeuds_a_la_main():
    assert pp.famille(FX) == ("fixe", 1)
    mel = {"type": "melange", "poids": [0.5, 0.5], "composantes": [FX, {"type": "transformee", "base": SM, "puissance": 1.2}]}
    assert pp.famille(mel) == ("melange", 4)
    with pytest.raises(mr.Refus):
        pp.famille({"type": "inconnu"})


def test_paires_roles_a_pile_ou_face(petit_banc):
    espace, fams, index, paires, pans, hist, ecartes = petit_banc
    ech = [p["echange"] for p in paires]
    assert 0 < sum(ech) < len(ech)  # les deux rôles sont tirés
    for p in paires:
        assert {p["monde"], p["leurre"]} == {p["premiere_tiree"], p["seconde"]}
        assert (p["monde"] == p["seconde"]) == p["echange"]
        assert fams[p["monde"]] == fams[p["leurre"]] and pp.distinctes(espace, p["monde"], p["leurre"], SEUIL)


def test_limite_des_lois_sans_leurre_saine_et_artefact(petit_banc, monkeypatch):
    espace, fams, index, *_ = petit_banc
    monkeypatch.setattr(pp, "choisir_leurre", lambda *a, **k: None)  # artefact : aucune loi n'a de leurre
    with pytest.raises(mr.Refus):
        pp.tirer_paires(espace, fams, index, 4, g("x"), lambda a: g("y"), lambda i: g("z"), SEUIL, 3)


def test_plan_equilibre_sain_et_artefacts():
    pos = pp.plan_positions(g("essai/plan-seul"), 64, K)
    assert pp.exiger_plan_equilibre(pos, K) == {"1": [8] * K, "2": [8] * K}
    for artefact in (np.zeros(64, dtype=int), np.arange(K)[:7]):
        with pytest.raises(mr.Refus):
            pp.exiger_plan_equilibre(artefact, K)
    with pytest.raises(mr.Refus):
        pp.plan_positions(g("x"), 63, K)


def test_panorama_sain_et_artefacts(petit_banc):
    espace, fams, index, paires, pans, hist, _ = petit_banc
    pan = pans[0]
    pp.exiger_panorama(pan, fams, K, espace, SEUIL)
    p, w, l = pan["position"], pan["monde"], pan["leurre"]
    autre = next(i for i in range(len(espace["lois"])) if fams[i] != fams[w] and i not in pan["C"])

    def mute(f):
        x = json.loads(json.dumps(pan))
        f(x)
        return x

    for a in (mute(lambda x: x["B"].__setitem__(p, autre) or x.__setitem__("leurre", autre)),
              mute(lambda x: x["B"].__setitem__(p, w) or x.__setitem__("leurre", w)),
              mute(lambda x: x["B"].__setitem__((p + 1) % K, autre)),
              mute(lambda x: x["C"].__setitem__((p + 1) % K, x["C"][(p + 2) % K])),
              mute(lambda x: x.__setitem__("C", x["C"][:-1]))):
        with pytest.raises(mr.Refus):
            pp.exiger_panorama(a, fams, K, espace, SEUIL)
    # leurre ou remplisseurs non distincts par la signature (C-7 iii, iv) : seuil porté si haut que rien n'est distinct
    with pytest.raises(mr.Refus):
        pp.exiger_panorama(pan, fams, K, espace, 1e9)


def test_remplisseurs_introuvables_artefact(petit_banc):
    espace, fams, index, paires, pans, *_ = petit_banc
    with pytest.raises(mr.Refus):
        pp.choisir_remplisseurs(espace, pans[0]["monde"], pans[0]["leurre"], fams, g("r"), K - 1, 1e9, essais_max=200)


# --- historique et carte sans aide (option (a)) -------------------------------------------------------------------------
def test_historique_vrai(petit_banc):
    espace, fams, index, paires, pans, hist, _ = petit_banc
    for pan, h in zip(pans[:5], hist[:5]):
        assert len(h) == T
        for pred, rep in h:
            q = pp.GRAMMAIRE.index(pred)
            assert rep == bool(espace["A"][pan["monde"], q])


def test_etat_sans_aide_sain_et_artefacts(petit_banc):
    espace, fams, index, paires, pans, hist, _ = petit_banc
    lois = [espace["lois"][x] for x in pans[0]["C"]]
    etat = pp.etat_de_carte(lois, hist[0])
    pp.exiger_etat_sans_aide(etat, T)
    artefacts = [
        {**etat, "position": 3},  # une aide : la position
        {**etat, "historique": etat["historique"][:-1]},  # historique trop court
        {**etat, "historique": etat["historique"][:-1] + ((etat["historique"][-1][0], "Inconnu"),)},  # « Inconnu »
        {**etat, "historique": etat["historique"][:-1] + (({"genre": "candidate", "indice": 3}, True),)},  # confirmation
        {**etat, "K": 7},
    ]
    for a in artefacts:
        with pytest.raises(mr.Refus):
            pp.exiger_etat_sans_aide(a, T)


def test_carte_sans_aide_saine_et_artefacts(petit_banc):
    espace, fams, index, paires, pans, hist, _ = petit_banc
    lois = [espace["lois"][x] for x in pans[0]["C"]]
    vu = {}

    class Espion(pp.QuestionneurCarte):
        nom = "espion"

        def choisir_carte(self, etat, verite=None):
            vu["cles"], vu["verite"], vu["t"] = sorted(etat), verite, len(etat["historique"])
            return 3

    assert pp.jouer_carte(Espion(None), lois, hist[0], {"position_vraie": 1, "famille_monde": ("fixe", 1)}, T) == (3, False)
    assert vu == {"cles": ["K", "historique", "panorama"], "verite": None, "t": T}

    class Tricheur(pp.QuestionneurCarte):
        nom = "tricheur"
        simule_verite = True

        def choisir_carte(self, etat, verite=None):
            return verite["position_vraie"]

    with pytest.raises(mr.Refus):
        pp.jouer_carte(Tricheur(None), lois, hist[0], {"position_vraie": 1, "famille_monde": ("fixe", 1)}, T)
    with pytest.raises(mr.Refus):  # historique de mauvaise longueur pour t
        pp.jouer_carte(Espion(None), lois, hist[0][:2], None, T)

    class Hors(pp.QuestionneurCarte):
        nom = "hors"

        def __init__(self, k):
            super().__init__(None)
            self.k = k

        def choisir_carte(self, etat, verite=None):
            return self.k

    for k in (K, -1, True, None, 2.0):
        with pytest.raises(mr.Refus):
            pp.jouer_carte(Hors(k), lois, hist[0], None, T, "arret")
        assert pp.jouer_carte(Hors(k), lois, hist[0], None, T, "carte_perdue") == (None, True)


# --- factices sur petits mondes ----------------------------------------------------------------------------------------
@pytest.fixture(scope="module")
def lectures_petites(petit_banc):
    espace, fams, index, paires, pans, hist, _ = petit_banc
    specs = lanceur.FACTICES_CRITERE + lanceur.FACTICES_RAPPORTES
    banc = pp.jouer_reconnaissance(espace, fams, pans, hist, specs, rng_carte(), outils_essai(), K, T)
    lect = {s: pp.trois_issues(banc[s]["cible_C"], banc[s]["cible_B"], g(f"essai/boot/{s}"), 2000, 0.975, 0.05, K)
            for s in specs}
    biais = {s: pp.biais_de_position(banc[s]["choix_C"], banc[s]["choix_B"], g(f"essai/pos/{s}"), 2000, 0.995, K, 0.05)
             for s in specs}
    return banc, lect, biais


def test_factices_sur_petits_mondes(lectures_petites):
    banc, lect, biais = lectures_petites
    assert all(banc[s]["refus"] == 0 for s in banc)
    for s, det, abs_ in (("premier", "premiere", "derniere"), ("dernier", "derniere", "premiere")):
        assert biais[s][det]["etat"] == "detecte" and biais[s][abs_]["etat"] == "absent"
        assert lect[s]["ecart_D"]["point"] == 0.0 and lect[s]["ecart_D"]["largeur"] == 0.0
    f = lect["famille"]
    assert f["taux_C"]["point"] == 1.0 and f["taux_B"]["point"] == 1.0 and f["issue"] == "au niveau du hasard"
    assert f["lecture_sans_leurre_taux_C_moins_1_sur_K"] == "au-dessus du hasard"
    # non tautologiques : compatibilité avec l'historique, sans vérité du banc
    assert lect["compatible"]["issue"] == "au-dessus du hasard"
    # contradicteur : écart négatif ; à 64 mondes, « en dessous » n'est pas toujours atteint (puissance)
    assert lect["contradicteur"]["ecart_D"]["point"] < 0
    assert lect["contradicteur"]["issue"] in ("en dessous du hasard", "non concluant")
    # sans vérité, préférence de contenu ou hasard : jamais au-dessus ni en dessous (à 64 mondes, souvent non concluant)
    for s in ("hasard", "plate", "centrale"):
        assert lect[s]["issue"] in ("au niveau du hasard", "non concluant"), (s, lect[s])
    conf = {s: pp.conforme(s, lect[s], biais[s]) for s in lanceur.FACTICES_CRITERE}
    for s in ("premier", "dernier"):
        assert conf[s]["tient"], (s, conf[s])
    for s in ("famille", "compatible"):  # à 64 mondes, l'absence de biais de position reste souvent « indéterminée »
        assert all(v for k, v in conf[s]["detail"].items() if k not in ("premiere", "derniere")), (s, conf[s])
    assert set(pp.ATTENTES_FACTICES) == set(lanceur.FACTICES_CRITERE)


def test_biais_de_position_regle_sur_tableaux():
    n = 400
    premier = np.zeros((n, 2), dtype=int)
    b = pp.biais_de_position(premier, premier, np.random.default_rng(0), 500, 0.995, K, 0.05)
    assert b["premiere"]["etat"] == "detecte" and b["derniere"]["etat"] == "absent"
    rng = np.random.default_rng(1)
    unif = rng.integers(0, K, (n, 2))
    b = pp.biais_de_position(unif, rng.integers(0, K, (n, 2)), np.random.default_rng(2), 500, 0.995, K, 0.05)
    assert b["premiere"]["etat"] == "absent" and b["derniere"]["etat"] == "absent"
    leger = np.where(rng.random((n, 2)) < 0.2, 0, rng.integers(0, K, (n, 2)))
    b = pp.biais_de_position(leger, leger, np.random.default_rng(3), 500, 0.995, K, 0.05)
    assert b["premiere"]["etat"] in ("indetermine", "detecte")


def test_regle_trois_issues_et_grandeur():
    rng = np.random.default_rng(7)
    n, h = 4000, 1.0 / K
    for pc, attendu in ((h, "au niveau du hasard"), (0.3 + 0.7 * h, "au-dessus du hasard"), (0.0, "en dessous du hasard")):
        c = (rng.random((n, 2)) < pc).astype(int)
        b = (rng.random((n, 2)) < h).astype(int)
        assert pp.trois_issues(c, b, np.random.default_rng(1), 1000, 0.975, 0.05, K)["issue"] == attendu
    assert pp.issue(0.01, 0.2, 0.05) == "au-dessus du hasard" and pp.issue(-0.04, 0.04, 0.05) == "au niveau du hasard"
    assert pp.issue(-0.05, 0.04, 0.05) == "non concluant"
    assert pp.grandeur(0.01, 0.04, 0.05, "au-dessus du hasard") == "sous la marge"
    assert pp.grandeur(0.06, 0.2, 0.05, "au-dessus du hasard") == "au-delà de la marge"
    assert pp.grandeur(0.01, 0.2, 0.05, "au-dessus du hasard") == "chevauche la marge"
    assert pp.grandeur(-0.04, -0.01, 0.05, "en dessous du hasard") == "sous la marge"
    assert pp.grandeur(-0.01, 0.01, 0.05, "au niveau du hasard") == "sans objet"


# --- puissance (C-3) et appels (C-4) -----------------------------------------------------------------------------------
def test_puissance_analytique_valeurs_gelees():
    c = lanceur.CONFIG["p3"]
    an = pp.taille_analytique(*lanceur._params(lanceur.CONFIG))
    assert an["n_multiple_de_K"] == 2048 == c["mondes"]
    assert abs(an["n_par_issue"]["au_niveau"] - 2044.37) < 0.01
    assert abs(an["n_par_issue"]["au_dessus"] - 373.08) < 0.01 and abs(an["n_par_issue"]["en_dessous"] - 149.13) < 0.01
    s = pp.sensibilite_delta(8, 0.29, 0.15, 0.5, 0.975, 0.8, c["deltas_sensibilite"])
    assert s == {"0.03": 5680, "0.04": 3200, "0.05": 2048, "0.0625": 1312, "0.075": 912, "0.1": 512}
    with pytest.raises(mr.Refus):
        pp.taille_analytique(8, 0.29, 0.2, 0.15, 0.5, 0.975, 0.8)  # « en dessous » sous la marge


def test_regle_gelee_simulee_ordres_correles():
    """La règle gelée elle-même, ordres corrélés à 1 : à 2 048 mondes elle rend « au niveau » environ 0,8 (répétitions
    réduites ici) ; à l'ancienne taille de 1 088, bien moins (constat C-3)."""
    rng = np.random.default_rng(5)
    a = pp.puissance_regle_gelee(2048, 0.29, 0.29, rng, 120, 500, 0.975, 0.05, K)
    b = pp.puissance_regle_gelee(1088, 0.29, 0.29, rng, 120, 500, 0.975, 0.05, K)
    assert a["au niveau du hasard"] >= 0.7 and b["au niveau du hasard"] < 0.5
    v = pp.verifier_taille(2048, K, 0.29, 0.05, 0.15, 0.5, 0.975, 0.8, 60, 300, RACINE_ESSAI)
    assert v["par_issue"]["au_dessus"]["au-dessus du hasard"] == 1.0
    assert v["par_issue"]["en_dessous"]["en dessous du hasard"] == 1.0


def test_garde_puissance_saine_et_artefacts(monkeypatch):
    assert lanceur.exiger_puissance(lanceur.CONFIG, simuler=False)["analytique"]["n_multiple_de_K"] == 2048
    for cle, val in (("mondes", 1088), ("mondes", 2050), ("taux_de_base", 0.35)):
        autre = json.loads(json.dumps(lanceur.CONFIG))
        autre["p3"][cle] = val
        with pytest.raises(lanceur.REFUS):
            lanceur.exiger_puissance(autre, simuler=False)
    # partie simulée : la garde suit le verdict de la règle gelée simulée (sain, puis artefact)
    vu = {}

    def faux(n, *a, **k):
        vu["n"] = n
        return {"n": n, "par_issue": {}, "tient": vu.get("tient", True)}

    monkeypatch.setattr(pp, "verifier_taille", faux)
    assert lanceur.exiger_puissance(lanceur.CONFIG, simuler=True)["regle_gelee_simulee"]["n"] == 2048
    vu["tient"] = False
    with pytest.raises(lanceur.REFUS):
        lanceur.exiger_puissance(lanceur.CONFIG, simuler=True)


def test_appels_et_longueur():
    a = pp.appels_phase1(2048, 4, 4, 2)
    assert a["appels_par_proposeur"] == 16384 and a["appels_total"] == 32768 and "USD" not in json.dumps(a)
    assert pp.longueur_panorama([FX]) == len('[{"probas":[0.2,0.3,0.5],"type":"fixe"}]')


# --- lanceur : gardes --------------------------------------------------------------------------------------------------
def test_verdict_table_gelee():
    assert lanceur.verdict_p3(False, True, True, True).startswith("garde défaillante")
    assert lanceur.verdict_p3(True, False, True, True).startswith("taille sous-dimensionnée")
    assert lanceur.verdict_p3(True, True, False, True).startswith("instrument de reconnaissance non discriminant")
    assert lanceur.verdict_p3(True, True, True, False).startswith("biais de position non retrouvé")
    assert lanceur.verdict_p3(True, True, True, True).startswith("instrument de reconnaissance discriminant")


def _cl(tmp_path, nom, texte):
    f = tmp_path / nom
    f.write_text(texte, encoding="utf-8")
    (tmp_path / (nom + ".sha256")).write_text(f"{sha(f)}  {nom}\n", encoding="utf-8")
    return f


def test_garde_contre_lecture_stricte(tmp_path):
    e = "a" * 64
    sain = f"**Texte contre-lu : `x.md`, sha256 `{e}`**\n\n## Verdict\n\n**Scellable.**\n"
    assert lanceur.exiger_contre_lecture(_cl(tmp_path, "ok.md", sain), e)["verdict"] == "scellable"
    artefacts = {
        "gras-partiel.md": f"Texte contre-lu : {e}\n\n## Verdict\n\n**Scellable** après corrections (voir C-1).\n",
        "condition.md": f"Texte contre-lu : {e}\n\n## Verdict\n\n**Scellable** seulement si le devis est retiré ; sinon non scellable.\n",
        "non.md": f"Texte contre-lu : {e}\n\n## Verdict\n\n**Non scellable.**\n",
        "apc.md": f"Texte contre-lu : {e}\n\n## Verdict\n\n**Scellable après corrections.**\n",
        "ailleurs.md": f"Texte contre-lu : autre\n\nJe cite {e}.\n\n## Verdict\n\n**Scellable.**\n",
        "pas-relu.md": f"Texte contre-lu : {e} (que je n'ai pas relu)\n\n## Verdict\n\n**Scellable.**\n",
        "pas-relu-2.md": f"Texte contre-lu : {e}\n\nLe texte {e} n'a pas été relu en entier.\n\n## Verdict\n\nScellable\n",
        "sans-verdict.md": f"Texte contre-lu : {e} ; scellable\n",
    }
    for nom, texte in artefacts.items():
        with pytest.raises(lanceur.Refus):
            lanceur.exiger_contre_lecture(_cl(tmp_path, nom, texte), e)
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_contre_lecture(None, e)
    f = _cl(tmp_path, "retouche.md", sain)
    f.write_text(sain + " ", encoding="utf-8")
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_contre_lecture(f, e)  # compagnon non conforme
    # la vraie contre-lecture de la v1 : verdict strict « non scellable »
    vraie = (ICI / "contre-lecture-phase0-p3-v1.md").read_text(encoding="utf-8")
    assert lanceur.lire_verdict_strict(vraie) == "non scellable"


def test_garde_bloc_effort_saine_et_artefact(tmp_path):
    cfg = config_essai()
    p = tmp_path / "pr.md"
    p.write_text("bloc : " + lanceur.empreinte_bloc_effort(cfg) + "\n", encoding="utf-8")
    assert lanceur.exiger_bloc_effort(p, cfg)
    for cle, val in (("t_questions", 5), ("taux_de_base", 0.3), ("delta_equivalence", 0.1), ("factices_critere", ["hasard"])):
        autre = json.loads(json.dumps(cfg))
        autre["p3"][cle] = val
        with pytest.raises(lanceur.Refus):
            lanceur.exiger_bloc_effort(p, autre)


def test_garde_code_p1_reemploye_sain_et_artefact(tmp_path):
    assert lanceur.exiger_code_p1() == lanceur.MODULES_P1
    for m in lanceur.MODULES_P1:
        shutil.copy(pp.DOSSIER_P1 / m, tmp_path / m)
        (tmp_path / (m + ".sha256")).write_text(f"{sha(tmp_path / m)}  {m}\n", encoding="utf-8")
    assert lanceur.exiger_code_p1(tmp_path) == lanceur.MODULES_P1
    m = "questionneurs_p1_v2.py"
    with open(tmp_path / m, "a", encoding="utf-8") as f:
        f.write("# modifié\n")
    (tmp_path / (m + ".sha256")).write_text(f"{sha(tmp_path / m)}  {m}\n", encoding="utf-8")
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_code_p1(tmp_path)


def test_mode_essai_petits_mondes_seulement():
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_petit_monde(lanceur.CONFIG)
    voisine = json.loads(json.dumps(lanceur.CONFIG))
    voisine["p3"]["puissance_tirages"] = 2001  # un champ sans portée changé : toujours refusé (C-8)
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_petit_monde(voisine)
    lanceur.exiger_petit_monde(config_essai())


# --- lanceur : bout en bout sur sources fabriquées ----------------------------------------------------------------------
def config_essai():
    cfg = json.loads(json.dumps(lanceur.CONFIG))
    cfg["racine_graines"] = RACINE_ESSAI
    cfg["p3"].update({"taille_espace_H": 256, "sonde_questions": 256, "sonde_score": 64, "mondes": 64,
                      "limite_lois_sans_leurre": 256, "tirages_bootstrap": 300,
                      "sondes_factices": {"sonde": 64, "sonde_q": 256},
                      "echangeabilite": {"echantillon_voisines": 16, "marges": {"entropie_nat": 0.02,
                                                                                "part_voisines_distinctes": 0.03}}})
    return cfg


def _sources(tmp_path, cfg=None):
    cfg = cfg or config_essai()
    pv = tmp_path / "v67.json"
    pv.write_text(json.dumps({"releve": {"plantees": [{"nom": "V1", "loi": FX}], "cartes": [{"loi": SM}]}}), encoding="utf-8")
    prereg = tmp_path / "prereg-essai.md"
    prereg.write_text("essai ; bloc : " + lanceur.empreinte_bloc_effort(cfg) + "\n", encoding="utf-8")
    essais = {"preenregistrement": sha(prereg), "controle_du_code": False, "contre_lecture_exigee": False,
              "compagnon_du_preenregistrement_exige": False, "puissance_exigee": False, "config": cfg,
              "evaluateur": [EVALUATEUR, sha(EVALUATEUR)], "sources": {"v67": [str(pv), sha(pv)]}}
    pe = tmp_path / "essais.json"
    pe.write_text(json.dumps(essais), encoding="utf-8")
    return prereg, pe


def test_lanceur_bout_en_bout_sur_sources_fabriquees(tmp_path):
    prereg, pe = _sources(tmp_path)
    out = tmp_path / "sortie"
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--essai", "--essais-json", str(pe)]) == 0
    res = json.loads((out / "sortie-phase0-p3-v2.json").read_text(encoding="utf-8"))
    man = json.loads((out / "manifeste-phase0-p3-v2.json").read_text(encoding="utf-8"))
    assert res["essai"] is True and man["essai"] is True
    p3 = res["p3"]
    assert "arret" not in p3, p3
    assert p3["lectures_trois_issues"]["compatible"]["issue"] == "au-dessus du hasard"
    assert p3["informations"]["comptes_plan"] == {"1": [8] * K, "2": [8] * K}
    assert 0 < p3["informations"]["part_des_roles_echanges"] < 1
    assert set(p3["rapporte_sans_decision"]["compatible_selon_t"]) == {"0", "2", "4", "8"}
    assert set(p3["rapporte_sans_decision"]["artefact_roles_non_tires"]) == set(lanceur.FACTICES_ARTEFACT_ROLES)
    assert p3["informations"]["longueur_panorama_caracteres"]["min"] > 0
    a = res["appels_phase1_non_engages"]
    assert a["appels_total"] == 64 * 8 * 2 and "USD" not in json.dumps(a)
    for nom in ("sortie-phase0-p3-v2.json", "manifeste-phase0-p3-v2.json", "journal-fichiers-ouverts-phase0-p3-v2.txt"):
        assert (out / (nom + ".sha256")).read_text(encoding="utf-8").split()[0] == sha(out / nom)
    assert "p3/roles/<i>" in man["graines"]["taches"] and "p3/historique/<i>/questionneur" in man["graines"]["taches"]
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--essai", "--essais-json", str(pe)]) == 2


def test_lanceur_refuse_preenregistrement_altere_et_contre_lecture(tmp_path):
    prereg, pe = _sources(tmp_path)
    essais = json.loads(pe.read_text(encoding="utf-8"))
    out = tmp_path / "s"
    texte = prereg.read_text(encoding="utf-8")
    prereg.write_text(texte + " ", encoding="utf-8")
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--essai", "--essais-json", str(pe)]) == 2
    prereg.write_text(texte, encoding="utf-8")
    essais["contre_lecture_exigee"] = True
    pe.write_text(json.dumps(essais), encoding="utf-8")
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--essai", "--essais-json", str(pe)]) == 2
    partiel = _cl(tmp_path, "p.md", f"Texte contre-lu : {sha(prereg)}\n\n## Verdict\n\n**Scellable** après corrections\n")
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--contre-lecture", str(partiel),
                              "--essai", "--essais-json", str(pe)]) == 2
    assert not out.exists()
    oui = _cl(tmp_path, "oui.md", f"Texte contre-lu : {sha(prereg)}\n\n## Verdict\n\n**Scellable.**\n")
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--contre-lecture", str(oui),
                              "--essai", "--essais-json", str(pe)]) == 0


def test_mode_essai_refuse_la_configuration_reelle(tmp_path):
    prereg, pe = _sources(tmp_path, json.loads(json.dumps(lanceur.CONFIG)))
    out = tmp_path / "s"
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--essai", "--essais-json", str(pe)]) == 2
    assert not out.exists()


def test_vrai_preenregistrement_et_lancement_reel_refuse(tmp_path, monkeypatch):
    """Sentinelle (C-8) : si une garde laissait passer, le déroulement remplacé ferait échouer l'essai, sans calcul."""
    def sentinelle(*a, **k):
        raise AssertionError("la configuration réelle aurait été lancée")

    monkeypatch.setattr(lanceur, "phase_p3", sentinelle)
    monkeypatch.setattr(lanceur, "exiger_puissance", sentinelle)
    vrai = ICI / lanceur.NOM_PREENREGISTREMENT
    assert lanceur.l1.exiger_preenregistrement(vrai, lanceur.EMPREINTE_PREENREGISTREMENT, exiger_compagnon=True) == sha(vrai)
    assert lanceur.exiger_bloc_effort(vrai, lanceur.CONFIG) == lanceur.empreinte_bloc_effort(lanceur.CONFIG)
    out = tmp_path / "sortie"
    assert lanceur.principal(["--sortie", str(out)]) == 2  # aucune contre-lecture
    v1 = ICI / "contre-lecture-phase0-p3-v1.md"  # contre-lecture de la v1, « non scellable »
    assert lanceur.principal(["--sortie", str(out), "--contre-lecture", str(v1)]) == 2
    copie = tmp_path / lanceur.NOM_PREENREGISTREMENT
    copie.write_bytes(vrai.read_bytes() + b" ")
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(copie)]) == 2
    assert not out.exists()


def test_sans_cle_en_double_dans_le_code():
    import ast
    for nom in ("lanceur_phase0_p3_v2.py", "panorama_p3_v2.py"):
        for n in ast.walk(ast.parse((ICI / nom).read_text(encoding="utf-8"))):
            if isinstance(n, ast.Dict):
                noms = [k.value for k in n.keys if isinstance(k, ast.Constant)]
                assert len(noms) == len(set(noms)), noms


def test_code_de_p3_v2_scelle_et_conforme():
    """Après scellement : code et essais conformes à leurs compagnons (échoue avant scellement, à dessein)."""
    assert set(lanceur.l1.exiger_code_scelle(ICI, lanceur.MODULES)) == set(lanceur.MODULES)
    assert sha(ICI / "test_phase0_p3_v2.py") == (ICI / "test_phase0_p3_v2.py.sha256").read_text(encoding="utf-8").split()[0]
