"""Essais (R5) de la phase 0 de P3 — v1 (modèle I, auteur unique). Fichier neuf (R12).

Chaque garde est essayée sur un cas sain et sur un artefact. Petits mondes d'essai seulement (racine de graines 4242,
espaces de 256 lois, sondes réduites, 64 mondes), jamais la configuration du préenregistrement ; sources fabriquées,
jamais les cartes de la course v67. Le code de P1 est réemployé par import, sans modification.
Lancement : cd <ce dossier> && PYTHONDONTWRITEBYTECODE=1 python3 -B -m pytest -q -p no:cacheprovider test_phase0_p3_v1.py
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

import lanceur_phase0_p3_v1 as lanceur  # noqa: E402
import panorama_p3_v1 as pp  # noqa: E402
import mondes_reponses_p1p2_v1 as mr  # noqa: E402
import questionneurs_p1_v2 as qp  # noqa: E402

EVALUATEUR = "/home/user/ideation-organism/orchestrator/pole/evaluateur_lois_v62.py"
RACINE_ESSAI = 4242
K = 8
SEUIL = 0.30
FX = {"type": "fixe", "probas": [0.2, 0.3, 0.5]}
SM = {"type": "softmax", "poids": [[1.0, 0.0], [0.0, 1.0], [-1.0, -1.0]], "biais": [0.0, 0.1, -0.1]}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def g(nom):
    return mr.generateur(nom, RACINE_ESSAI)


@pytest.fixture(scope="module")
def petit_banc():
    """Espace de 256 lois, 64 mondes avec leurre apparié, plan équilibré, panoramas appariés."""
    sq = mr.tirer_sonde(g("essai/sq"), 512)
    ss = mr.tirer_sonde(g("essai/ss"), 128)
    espace = qp.construire_espace(g("essai/espace"), 256, sq, ss)
    fams, index = pp.index_familles(espace)
    mondes, leurres, ecartes = pp.tirer_mondes_avec_leurre(espace, fams, index, 64, g("essai/mondes"),
                                                           lambda w: g(f"essai/leurre/{w}"), SEUIL, 256)
    positions = pp.plan_positions(g("essai/plan"), 64, K)
    pans = []
    for i, (w, l, p) in enumerate(zip(mondes, leurres, positions)):
        remp = pp.choisir_remplisseurs(espace, w, l, fams, g(f"essai/remp/{i}"), K - 1, SEUIL)
        pan = pp.construire_panorama(w, l, remp, int(p), K)
        pp.exiger_panorama(pan, fams, K, espace, SEUIL)
        pans.append(pan)
    return espace, fams, pans, ecartes


def rng_carte(prefixe="essai"):
    return lambda spec, bras, ordre, i: g(f"{prefixe}/carte/{spec}/{bras}/{ordre}/{i}")


# --- familles, leurres, plan -------------------------------------------------------------------------------------------
def test_famille_et_noeuds_a_la_main():
    assert pp.famille(FX) == ("fixe", 1)
    mel = {"type": "melange", "poids": [0.5, 0.5], "composantes": [FX, {"type": "transformee", "base": SM, "puissance": 1.2}]}
    assert pp.famille(mel) == ("melange", 4)
    with pytest.raises(mr.Refus):
        pp.famille({"type": "inconnu"})


def test_leurre_apparie_meme_famille_et_distinct(petit_banc):
    espace, fams, pans, ecartes = petit_banc
    assert len(pans) == 64 and ecartes >= 0
    for pan in pans:
        w, l = pan["monde"], pan["leurre"]
        assert fams[w] == fams[l] and w != l
        assert qp.kl_vers(espace, w, l) > SEUIL and qp.kl_vers(espace, l, w) > SEUIL


def test_plan_equilibre_sain_et_artefacts():
    pos = pp.plan_positions(g("essai/plan-seul"), 64, K)
    c = pp.exiger_plan_equilibre(pos, K)
    assert c == {"1": [8] * K, "2": [8] * K}
    assert pp.exiger_plan_equilibre(pos[:16], K)  # tout préfixe de m·K mondes est équilibré
    for artefact in (np.zeros(64, dtype=int),  # cible toujours en tête
                     np.concatenate([np.roll(np.arange(K), 1), np.arange(K)[::-1]] * 3 + [np.array([0, 0, 2, 3, 4, 5, 6, 7])] * 2),
                     np.arange(K)[:7]):
        with pytest.raises(mr.Refus):
            pp.exiger_plan_equilibre(artefact, K)
    with pytest.raises(mr.Refus):
        pp.plan_positions(g("x"), 63, K)


def test_panorama_sain_et_artefacts(petit_banc):
    espace, fams, pans, _ = petit_banc
    pan = pans[0]
    pp.exiger_panorama(pan, fams, K, espace, SEUIL)
    p, w, l = pan["position"], pan["monde"], pan["leurre"]
    autre_famille = next(i for i in range(len(espace["lois"])) if fams[i] != fams[w] and i not in pan["C"])
    meme_famille = [i for i in range(len(espace["lois"])) if fams[i] == fams[w] and i not in (w, l)]

    def mute(f):
        x = json.loads(json.dumps(pan))
        f(x)
        return x

    artefacts = [
        mute(lambda x: x["B"].__setitem__(p, autre_famille) or x.__setitem__("leurre", autre_famille)),  # leurre non apparié
        mute(lambda x: x["B"].__setitem__(p, w) or x.__setitem__("leurre", w)),  # forme vraie dans B (fuite)
        mute(lambda x: x["B"].__setitem__((p + 1) % K, autre_famille)),  # C et B diffèrent ailleurs
        mute(lambda x: x["C"].__setitem__((p + 1) % K, x["C"][(p + 2) % K])),  # doublon
        mute(lambda x: x.__setitem__("C", x["C"][:-1])),  # taille ≠ K
    ]
    if meme_famille:  # remplisseur de la famille du monde (la famille désignerait deux positions)
        artefacts.append(mute(lambda x: [x[b].__setitem__((p + 1) % K, meme_famille[0]) for b in ("B", "C")]))
    for a in artefacts:
        with pytest.raises(mr.Refus):
            pp.exiger_panorama(a, fams, K, espace, SEUIL)


# --- carte sans aide ---------------------------------------------------------------------------------------------------
def test_carte_sans_aide_saine_et_artefacts(petit_banc):
    espace, fams, pans, _ = petit_banc
    lois = [espace["lois"][x] for x in pans[0]["C"]]
    vu = {}

    class Espion(pp.QuestionneurCarte):
        nom = "espion"

        def choisir_carte(self, etat, verite=None):
            vu["cles"], vu["verite"] = sorted(etat), verite
            return 3

    k, ref = pp.jouer_carte(Espion(None), lois, {"position_vraie": 1, "famille_monde": ("fixe", 1)})
    assert (k, ref) == (3, False) and vu["cles"] == ["K", "panorama"] and vu["verite"] is None  # aucune aide

    class Curieux(pp.QuestionneurCarte):
        nom = "curieux"

        def choisir_carte(self, etat, verite=None):
            return etat["reponses"]  # cherche une réponse du répondeur : il n'y en a pas

    with pytest.raises(KeyError):
        pp.jouer_carte(Curieux(None), lois, None)

    class Tricheur(pp.QuestionneurCarte):
        nom = "tricheur"
        simule_verite = True

        def choisir_carte(self, etat, verite=None):
            return verite["position_vraie"]

    with pytest.raises(mr.Refus):  # lit la vérité sans être un factice déclaré
        pp.jouer_carte(Tricheur(None), lois, {"position_vraie": 1, "famille_monde": ("fixe", 1)})

    class Hors(pp.QuestionneurCarte):
        nom = "hors"

        def __init__(self, k):
            super().__init__(None)
            self.k = k

        def choisir_carte(self, etat, verite=None):
            return self.k

    for k in (K, -1, True, None, 2.0):
        with pytest.raises(mr.Refus):
            pp.jouer_carte(Hors(k), lois, None, "arret")
        assert pp.jouer_carte(Hors(k), lois, None, "carte_perdue") == (None, True)


# --- factices à biais connu sur petits mondes --------------------------------------------------------------------------
@pytest.fixture(scope="module")
def lectures_petites(petit_banc):
    espace, fams, pans, _ = petit_banc
    specs = lanceur.FACTICES_CRITERE + lanceur.FACTICES_RAPPORTES
    banc = pp.jouer_reconnaissance(espace, fams, pans, specs, rng_carte(), K)
    lect = {s: pp.trois_issues(banc[s]["cible_C"], banc[s]["cible_B"], g(f"essai/boot/{s}"), 2000, 0.975, 0.05, K)
            for s in specs}
    biais = {s: pp.biais_de_position(banc[s]["choix_C"], banc[s]["choix_B"], g(f"essai/pos/{s}"), 2000, 0.995, K)
             for s in specs}
    return banc, lect, biais


def test_factices_retrouves_sur_petits_mondes(lectures_petites):
    banc, lect, biais = lectures_petites
    assert all(banc[s]["refus"] == 0 for s in banc)
    # premier et dernier : biais retrouvé, reconnaissance exactement nulle grâce au plan équilibré
    for s, pos in (("premier", "premiere_detectee"), ("dernier", "derniere_detectee")):
        assert biais[s][pos] and lect[s]["ecart_D"]["point"] == 0.0 and lect[s]["ecart_D"]["largeur"] == 0.0
        assert lect[s]["taux_C"]["point"] == 1.0 / K and lect[s]["issue"] == "au niveau du hasard"
    assert not biais["premier"]["derniere_detectee"] and not biais["dernier"]["premiere_detectee"]
    assert lect["reconnaisseur:1"]["issue"] == "au-dessus du hasard" and lect["reconnaisseur:1"]["taux_C"]["point"] == 1.0
    assert lect["evitant:1"]["issue"] == "en dessous du hasard" and lect["evitant:1"]["taux_C"]["point"] == 0.0
    # famille : taux dans C de 1, que seul le leurre apparié démasque
    f = lect["famille"]
    assert f["taux_C"]["point"] == 1.0 and f["taux_B"]["point"] == 1.0 and f["ecart_D"]["point"] == 0.0
    assert f["issue"] == "au niveau du hasard" and f["lecture_sans_leurre_taux_C_moins_1_sur_K"] == "au-dessus du hasard"
    # hasard : à 64 mondes, l'équivalence n'est pas atteignable (puissance) ; jamais au-dessus ni en dessous
    assert lect["hasard"]["issue"] == "non concluant"
    assert not biais["hasard"]["premiere_detectee"] and not biais["hasard"]["derniere_detectee"]
    for s in ("hasard", "reconnaisseur:1"):
        assert not biais[s]["premiere_detectee"] and not biais[s]["derniere_detectee"]


def test_conformite_des_factices_et_lecture(lectures_petites):
    banc, lect, biais = lectures_petites
    conf = {s: pp.conforme(s, lect[s], biais[s]) for s in lanceur.FACTICES_CRITERE}
    assert all(conf[s]["tient"] for s in conf if s != "hasard")
    assert not conf["hasard"]["detail"]["issue"]  # non concluant à 64 mondes : le critère échoue, comme il doit
    issues_ok, positions_ok = lanceur.lire_conformites(conf)
    assert issues_ok is False and positions_ok is True
    assert set(pp.ATTENTES_FACTICES) == set(lanceur.FACTICES_CRITERE)


def test_sans_leurre_apparie_la_famille_passerait_pour_reconnaissance(petit_banc):
    """Artefact : B construit avec un leurre d'une autre famille (garde contournée) ; le factice « famille » paraît alors
    reconnaître (écart > 0) : le leurre apparié est nécessaire."""
    espace, fams, pans, _ = petit_banc
    faux = []
    for i, pan in enumerate(pans):
        x = json.loads(json.dumps(pan))
        autre = next(j for j in range(len(espace["lois"])) if fams[j] != fams[pan["monde"]] and j not in pan["C"])
        x["B"][x["position"]] = autre
        x["leurre"] = autre
        with pytest.raises(mr.Refus):
            pp.exiger_panorama(x, fams, K, espace, SEUIL)
        faux.append(x)
    banc = pp.jouer_reconnaissance(espace, fams, faux, ("famille",), rng_carte("faux"), K)
    lect = pp.trois_issues(banc["famille"]["cible_C"], banc["famille"]["cible_B"], g("essai/boot/faux"), 2000, 0.975, 0.05, K)
    assert lect["issue"] == "au-dessus du hasard"


def test_plan_non_equilibre_fabrique_une_reconnaissance_sans_leurre(petit_banc):
    """Artefact : cible toujours en tête ; « premier » atteint 100 % dans C (la lecture sans leurre dirait « au-dessus ») ;
    la garde du plan le refuse ; sous le plan équilibré, son taux est exactement 1/K."""
    espace, fams, pans, _ = petit_banc
    biaise = []
    for pan in pans:
        reste = [x for k, x in enumerate(pan["C"]) if k != pan["position"]]
        biaise.append(pp.construire_panorama(pan["monde"], pan["leurre"], reste, 0, K))
    with pytest.raises(mr.Refus):
        pp.exiger_plan_equilibre([b["position"] for b in biaise], K)
    # ordre 1 seulement : la cible est en tête dans tous les mondes
    banc = pp.jouer_reconnaissance(espace, fams, biaise, ("premier",), rng_carte("biais"), K)
    assert banc["premier"]["cible_C"][:, 0].mean() == 1.0


# --- règle à trois issues et puissance -----------------------------------------------------------------------------------
def test_regle_trois_issues_sur_tableaux_synthetiques():
    rng = np.random.default_rng(7)
    n = 4000
    h = 1.0 / K
    cas = {"hasard": (h, "au niveau du hasard"), "reconnaisseur": (0.3 + 0.7 * h, "au-dessus du hasard"),
           "evitant": (0.0, "en dessous du hasard")}
    for nom, (pc, attendu) in cas.items():
        c = (rng.random((n, 2)) < pc).astype(int)
        b = (rng.random((n, 2)) < h).astype(int)
        assert pp.trois_issues(c, b, np.random.default_rng(1), 1000, 0.975, 0.05, K)["issue"] == attendu, nom
    c = (rng.random((40, 2)) < h).astype(int)
    b = (rng.random((40, 2)) < h).astype(int)
    assert pp.trois_issues(c, b, np.random.default_rng(1), 1000, 0.975, 0.05, K)["issue"] == "non concluant"
    assert pp.issue(0.01, 0.2, 0.05) == "au-dessus du hasard" and pp.issue(-0.2, -0.01, 0.05) == "en dessous du hasard"
    assert pp.issue(-0.04, 0.04, 0.05) == "au niveau du hasard" and pp.issue(-0.05, 0.04, 0.05) == "non concluant"
    with pytest.raises(mr.Refus):
        pp.trois_issues(np.zeros((3, 2)), np.zeros((4, 2)), rng, 10, 0.975, 0.05, K)


def test_puissance_analytique_valeurs_gelees():
    t = lanceur.puissance(lanceur.CONFIG)
    assert t["n_retenu_prudent"] == 1088 and t["n_optimiste_ordres_independants"] == 544
    assert t["issue_qui_dimensionne"] == "au_niveau"
    assert abs(t["n_par_issue"]["au_niveau"] - 1085.98) < 0.01
    assert abs(t["n_par_issue"]["au_dessus"] - 165.51) < 0.01 and abs(t["n_par_issue"]["en_dessous"] - 408.72) < 0.01
    assert lanceur.CONFIG["p3"]["mondes"] == t["n_retenu_prudent"]
    with pytest.raises(mr.Refus):  # « en dessous » non séparable de la marge
        pp.taille_necessaire(8, 0.05, 0.15, 0.3, 0.975, 0.8)


def test_puissance_controlee_par_simulation():
    """À la taille prudente, ordres parfaitement corrélés (hypothèse de la taille), chaque issue vraie est rendue au moins
    ≈ 80 % du temps (approximation normale) ; jamais l'issue opposée."""
    rng = np.random.default_rng(11)
    for modele, rho, attendu in (("hasard", 0.0, "au niveau du hasard"), ("reconnaisseur", 0.15, "au-dessus du hasard"),
                                 ("evitant", 0.5, "en dessous du hasard")):
        r = pp.puissance_par_simulation(1088, K, modele, rho, 0.975, 0.05, rng, repetitions=600)
        assert r[attendu] >= 0.75, (modele, r)
        oppose = {"au-dessus du hasard": "en dessous du hasard", "en dessous du hasard": "au-dessus du hasard"}
        if attendu in oppose:
            assert r[oppose[attendu]] == 0.0
    r = pp.puissance_par_simulation(1088, K, "hasard", 0.0, 0.975, 0.05, rng, repetitions=600, ordres_correles=False)
    assert r["au niveau du hasard"] >= 0.95  # ordres indépendants : bien au-dessus


def test_devis_a_la_main():
    d = pp.devis(1088, {"argon": 0.20637, "kimi": 0.400484}, 4, 0.10)
    assert d["appels_total"] == 8704 and d["appels"] == {"argon": 4352, "kimi": 4352}
    assert d["estimation_usd"] == {"argon": 898.12, "kimi": 1742.91} and d["estimation_total_usd"] == 2641.03
    assert d["pire_cas_usd"] == round(8704 * 0.400484 * 1.1, 2) == 3834.39
    assert pp.devis(544, {"argon": 0.20637, "kimi": 0.400484}, 4, 0.10)["pire_cas_usd"] == 1917.2


# --- recouvrement sur l'instrument de P1 --------------------------------------------------------------------------------
def test_recouvrement_carte_reconnue_gardee_tant_que_compatible(petit_banc):
    espace, fams, pans, _ = petit_banc
    pan = pans[0]
    w = pan["monde"]
    partie = qp.jouer_partie(espace, w, qp.Bissection(g("essai/kl/q")), mr.Repondeur(espace["A"][w, :42]), 8, (0, 4, 8), 42)
    vraie = pp.cartes_avec_reconnaissance(espace, w, partie, w, (0, 4, 8))
    assert all(vraie[t]["kl"] == 0.0 and vraie[t]["reconnue_gardee"] for t in (0, 4, 8))
    seul = pp.cartes_avec_reconnaissance(espace, w, partie, None, (0, 4, 8))
    assert all(seul[t]["carte"] == partie["cartes"][t]["carte"] for t in (0, 4, 8))
    leurre = pp.cartes_avec_reconnaissance(espace, w, partie, pan["leurre"], (0, 4, 8))
    assert leurre[0]["carte"] == pan["leurre"]
    for t in (4, 8):
        garde = pp.compatible(espace, pan["leurre"], w, partie["posees_au_monde"][:t])
        assert leurre[t]["reconnue_gardee"] == garde
        if not garde:
            assert leurre[t]["carte"] == partie["cartes"][t]["carte"]


# --- lanceur : gardes --------------------------------------------------------------------------------------------------
def test_verdict_p3_table_gelee():
    assert lanceur.verdict_p3(False, True, True).startswith("garde défaillante")
    assert lanceur.verdict_p3(True, False, True).startswith("instrument de reconnaissance non discriminant")
    assert lanceur.verdict_p3(True, True, False).startswith("biais de position non retrouvé")
    assert lanceur.verdict_p3(True, True, True).startswith("instrument de reconnaissance discriminant")


def _cl(tmp_path, nom, texte):
    f = tmp_path / nom
    f.write_text(texte, encoding="utf-8")
    (tmp_path / (nom + ".sha256")).write_text(f"{sha(f)}  {nom}\n", encoding="utf-8")
    return f


def test_garde_contre_lecture_saine_et_artefacts(tmp_path):
    e = "a" * 64
    cl = _cl(tmp_path, "cl.md", f"relu : {e}\n\n## Verdict\n\n**Scellable.**\n")
    assert lanceur.exiger_contre_lecture(cl, e)["verdict"] == "scellable"
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_contre_lecture(cl, "b" * 64)  # ne cite pas le texte lancé
    for nom, texte in (("non.md", f"relu : {e}\n\n## Verdict\n\n**Non scellable.**\n"),
                       ("apc.md", f"relu : {e}\n\n## Verdict\n\n**Scellable après corrections.**\n"),
                       ("bloq.md", f"relu : {e}\n\n## Verdict\n\nBloquant\n")):
        with pytest.raises(lanceur.Refus):
            lanceur.exiger_contre_lecture(_cl(tmp_path, nom, texte), e)
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_contre_lecture(_cl(tmp_path, "sans.md", f"relu : {e} ; scellable\n"), e)  # verdict absent
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_contre_lecture(None, e)
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_contre_lecture(tmp_path / "absente.md", e)
    cl.write_text(f"relu : {e}\n\n## Verdict\n\n**Scellable.** retouchée\n", encoding="utf-8")
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_contre_lecture(cl, e)  # compagnon non conforme


def test_garde_puissance_saine_et_artefact():
    assert lanceur.exiger_puissance(lanceur.CONFIG)["n_retenu_prudent"] == 1088
    autre = json.loads(json.dumps(lanceur.CONFIG))
    autre["p3"]["mondes"] = 200  # taille choisie sans la puissance
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_puissance(autre)
    autre = json.loads(json.dumps(lanceur.CONFIG))
    autre["p3"]["delta_equivalence"] = 0.04  # marge changée : la taille gelée n'est plus celle de la puissance
    with pytest.raises(lanceur.Refus):
        lanceur.exiger_puissance(autre)


def test_garde_bloc_effort_saine_et_artefact(tmp_path):
    cfg = config_essai()
    p = tmp_path / "pr.md"
    p.write_text("bloc : " + lanceur.empreinte_bloc_effort(cfg) + "\n", encoding="utf-8")
    assert lanceur.exiger_bloc_effort(p, cfg)
    for cle, val in (("K", 6), ("niveau", 0.95), ("delta_equivalence", 0.1), ("factices_critere", ["hasard"])):
        autre = json.loads(json.dumps(cfg))
        autre["p3"][cle] = val
        with pytest.raises(lanceur.Refus):
            lanceur.exiger_bloc_effort(p, autre)


def test_garde_code_p1_reemploye_sain_et_artefact(tmp_path):
    assert lanceur.exiger_code_p1() == lanceur.MODULES_P1  # le code de P1 est intact
    for m in lanceur.MODULES_P1:
        shutil.copy(pp.DOSSIER_P1 / m, tmp_path / m)
        (tmp_path / (m + ".sha256")).write_text(f"{sha(tmp_path / m)}  {m}\n", encoding="utf-8")
    assert lanceur.exiger_code_p1(tmp_path) == lanceur.MODULES_P1
    m = "questionneurs_p1_v2.py"
    with open(tmp_path / m, "a", encoding="utf-8") as f:
        f.write("# modifié\n")
    with pytest.raises(lanceur.Refus):  # compagnon non conforme
        lanceur.exiger_code_p1(tmp_path)
    (tmp_path / (m + ".sha256")).write_text(f"{sha(tmp_path / m)}  {m}\n", encoding="utf-8")
    with pytest.raises(lanceur.Refus):  # compagnon refait : l'empreinte attendue le démasque
        lanceur.exiger_code_p1(tmp_path)


# --- lanceur : bout en bout sur sources fabriquées ----------------------------------------------------------------------
def config_essai():
    cfg = json.loads(json.dumps(lanceur.CONFIG))
    cfg["racine_graines"] = RACINE_ESSAI
    cfg["p3"].update({"taille_espace_H": 256, "sonde_questions": 256, "sonde_score": 64, "questions_T": 8,
                      "points_de_carte": [0, 4, 8], "mondes": 64, "mondes_kl": 16, "limite_lois_sans_leurre": 256,
                      "tirages_bootstrap": 300})
    return cfg


def _sources(tmp_path, cfg=None):
    cfg = cfg or config_essai()
    v67 = {"releve": {"plantees": [{"nom": "V1", "loi": FX}], "cartes": [{"loi": SM}]}}
    pv = tmp_path / "v67.json"
    pv.write_text(json.dumps(v67), encoding="utf-8")
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
    res = json.loads((out / "sortie-phase0-p3-v1.json").read_text(encoding="utf-8"))
    man = json.loads((out / "manifeste-phase0-p3-v1.json").read_text(encoding="utf-8"))
    assert res["essai"] is True and man["essai"] is True
    p3 = res["p3"]
    assert "arret" not in p3, p3
    # à 64 mondes, le bras « choix au hasard » est non concluant : l'instrument se déclare non discriminant (puissance)
    assert p3["verdict_propose_par_le_code"].startswith("instrument de reconnaissance non discriminant")
    assert p3["lectures_trois_issues"]["hasard"]["issue"] == "non concluant"
    assert p3["lectures_trois_issues"]["reconnaisseur:1"]["issue"] == "au-dessus du hasard"
    assert p3["informations"]["comptes_plan"] == {"1": [8] * K, "2": [8] * K}
    assert set(p3["recouvrement_sur_l_instrument_P1_rapporte"]["par_factice"]) == set(lanceur.FACTICES_KL)
    rec = p3["recouvrement_sur_l_instrument_P1_rapporte"]["par_factice"]["reconnaisseur:1"]
    assert rec["kl_mediane_par_point"]["C"]["8"] == 0.0 and rec["part_reconnue_gardee_a_T"]["C"] == 1.0
    assert res["devis_refait_non_engage"]["mondes_par_proposeur"] == 1088 and res["borne_de_ce_que_l_instrument_permet_de_revendiquer"] == lanceur.BORNE_P3
    for nom in ("sortie-phase0-p3-v1.json", "manifeste-phase0-p3-v1.json", "journal-fichiers-ouverts-phase0-p3-v1.txt"):
        assert (out / (nom + ".sha256")).read_text(encoding="utf-8").split()[0] == sha(out / nom)
    assert man["effort_et_echantillonnage_geles"]["empreinte"] in prereg.read_text(encoding="utf-8")
    assert man["graines"]["racine"] == RACINE_ESSAI and "p3/plan" in man["graines"]["taches"]
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--essai", "--essais-json", str(pe)]) == 2


def test_lanceur_refuse_preenregistrement_altere_et_contre_lecture(tmp_path):
    prereg, pe = _sources(tmp_path)
    essais = json.loads(pe.read_text(encoding="utf-8"))
    out = tmp_path / "s"
    texte = prereg.read_text(encoding="utf-8")
    prereg.write_text(texte + " ", encoding="utf-8")  # altéré
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--essai", "--essais-json", str(pe)]) == 2
    assert not out.exists()
    prereg.write_text(texte, encoding="utf-8")
    essais["contre_lecture_exigee"] = True
    pe.write_text(json.dumps(essais), encoding="utf-8")
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--essai", "--essais-json", str(pe)]) == 2
    non = _cl(tmp_path, "non.md", f"relu : {sha(prereg)}\n\n## Verdict\n\n**Non scellable.**\n")
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--contre-lecture", str(non),
                              "--essai", "--essais-json", str(pe)]) == 2
    assert not out.exists()
    oui = _cl(tmp_path, "oui.md", f"relu : {sha(prereg)}\n\n## Verdict\n\n**Scellable.**\n")
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--contre-lecture", str(oui),
                              "--essai", "--essais-json", str(pe)]) == 0


def test_mode_essai_refuse_la_configuration_reelle(tmp_path):
    prereg, pe = _sources(tmp_path, json.loads(json.dumps(lanceur.CONFIG)))
    out = tmp_path / "s"
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(prereg), "--essai", "--essais-json", str(pe)]) == 2
    assert not out.exists()
    assert lanceur.principal(["--sortie", str(out), "--essai"]) == 2


def test_vrai_preenregistrement_scelle_et_lancement_reel_refuse_sans_contre_lecture(tmp_path):
    vrai = ICI / lanceur.NOM_PREENREGISTREMENT
    assert l1_exiger(vrai) == sha(vrai)
    assert lanceur.exiger_bloc_effort(vrai, lanceur.CONFIG) == lanceur.empreinte_bloc_effort(lanceur.CONFIG)
    out = tmp_path / "sortie"
    assert lanceur.principal(["--sortie", str(out)]) == 2  # aucune contre-lecture : refus, rien écrit
    assert not out.exists()
    copie = tmp_path / lanceur.NOM_PREENREGISTREMENT
    copie.write_bytes(vrai.read_bytes() + b" ")
    assert lanceur.principal(["--sortie", str(out), "--preenregistrement", str(copie)]) == 2
    assert not out.exists()


def l1_exiger(vrai):
    return lanceur.l1.exiger_preenregistrement(vrai, lanceur.EMPREINTE_PREENREGISTREMENT, exiger_compagnon=True)


def test_lanceur_sans_cle_en_double_dans_le_code():
    import ast
    for nom in ("lanceur_phase0_p3_v1.py", "panorama_p3_v1.py"):
        for n in ast.walk(ast.parse((ICI / nom).read_text(encoding="utf-8"))):
            if isinstance(n, ast.Dict):
                noms = [k.value for k in n.keys if isinstance(k, ast.Constant)]
                assert len(noms) == len(set(noms)), noms


def test_code_de_p3_scelle_et_conforme():
    """Après scellement (compagnons versés), le code de P3 est conforme à ses compagnons ; un essai qui tourne avant le
    scellement échoue ici, à dessein."""
    assert set(lanceur.l1.exiger_code_scelle(ICI, lanceur.MODULES)) == set(lanceur.MODULES)
    assert sha(ICI / "test_phase0_p3_v1.py") == (ICI / "test_phase0_p3_v1.py.sha256").read_text(encoding="utf-8").split()[0]
