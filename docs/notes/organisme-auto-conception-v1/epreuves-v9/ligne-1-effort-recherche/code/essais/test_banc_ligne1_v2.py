"""Essais du banc A, ligne 1 (code v2) — annexe A du préenregistrement
`prereg/organisme-auto-conception-v9/preenregistrement-ligne-1-effort-recherche-v5.md` (sha256 523adfd7…0fb9).

Code v2 : `etalonnage_ligne1_v2`, `lancer_ligne1_v2`, `rejouer_journal_ligne1_v2`, `configuration_ligne1_v2.json` ; banc,
journal et analyse v1 repris sans copie. Les 42 essais du code v1 sont repris (l'essai 2 réécrit : correction 4), suivis
des essais des corrections 1 à 3 et 5 à 7, du recoupement du rejeu et des gardes nouvelles, chacune sur un cas sain et sur
un artefact (R5).

Racine des graines des essais seulement : 2026111900. Aucune graine d'étalonnage (2026111901), décisive (2026111902) ni de
rééchantillonnage de la lecture (2026111903) n'est dérivée (dernier essai). Aucune issue de l'épreuve n'est lue.
Lancer : `PYTHONDONTWRITEBYTECODE=1 python3 -B -m pytest -q -p no:cacheprovider <ce fichier>` ; le dépôt de l'organisme est
lu en lecture seule au chemin `BANC_L1_ORGANISME` (défaut : /home/user/ideation-organism/orchestrator).
"""

import copy
import inspect
import json
import lzma
import math
import os
import shutil
import socket
import subprocess
import sys
import tarfile
import time
import types

import numpy as np
import pytest

CODE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, CODE)
sys.dont_write_bytecode = True

import banc_ligne1_v1 as B  # noqa: E402
import journal_ligne1_v1 as JL  # noqa: E402
import rejouer_journal_ligne1_v2 as RJ  # noqa: E402
import etalonnage_ligne1_v2 as E  # noqa: E402
import analyse_ligne1_v2 as AN  # noqa: E402
import lancer_ligne1_v2 as LA  # noqa: E402

ORGANISME = os.environ.get("BANC_L1_ORGANISME", "/home/user/ideation-organism/orchestrator")
CONFIG, SHA_CONFIG = B.charger_configuration(E.CHEMIN_CONFIGURATION)
RACINE = CONFIG["racines"]["essais"]
INTERDITES = {CONFIG["racines"][k] for k in ("etalonnage", "decisive", "reechantillonnage")}
B.charger_organisme(ORGANISME, CONFIG)
PE = CONFIG["parametres_essais"]
P = B.parametres(CONFIG, PE["forces"], PE["s"], PE["c"])


@pytest.fixture(scope="module")
def course_essai(tmp_path_factory):
    d = tmp_path_factory.mktemp("course-essai")
    return B.jouer_course(7, RACINE, P, str(d), SHA_CONFIG, None), str(d)


def _gens(res, classe, bras):
    return res["sorties"][classe]["bras"][bras]["generations"]


# --- préenregistrement ------------------------------------------------------------------------------------------------------
def test_preenregistrement_cite_et_verifie():
    prov = B.verifier_preenregistrement()
    assert prov["sha256"] == "523adfd75333d7f2e99a6fe4f868c7dc6982a67e51953734f40258d7a40fc0b9"
    with pytest.raises(B.PreenregistrementRefuse):
        B.verifier_preenregistrement(attendue="0" * 64)


# --- essai 1 : jugement identique à juger_carte (garde A6) ---------------------------------------------------------------
def test_essai01_jugement_identique_bit_pour_bit():
    assert B.verifier_jugement_identique(RACINE) == 10
    for i, loi in enumerate(B.lois_essai_a6()):
        ref, dref = B.AB.juger_carte(loi, {"loi": B.lois_essai_a6()[1]}, {}, RACINE, f"essai1|{i}")
        ev, d = B.juger_banc(loi, B.lois_essai_a6()[1], RACINE, f"essai1|{i}", CONFIG["juge"])
        assert JL.canonique(ref) == JL.canonique(ev) and JL.canonique(dref) == JL.canonique(d)


def test_garde_A6_artefact_instant_ajoute():
    with pytest.raises(B.GardeA6Jugement):
        B.verifier_jugement_identique(RACINE, nombre_instants=9)


# --- essai 2 : bras a, copies profondes, retenues = survit, d = a′ quand m_r = m_s ----------------------------------------
def test_essai02_bras_a_fonction_de_l_organisme_et_copies(course_essai):
    res, _ = course_essai
    assert B.CYC.appliquer_multiplicite is sys.modules["pole.cycle"].appliquer_multiplicite
    assert "def appliquer_multiplicite" not in inspect.getsource(B)
    pleine = res["pleines"]["beaucoup"]
    avant = {i: JL.empreinte(j["ev"]) for i, j in pleine["jugements"].items()}
    gen = [i for i, j in pleine["jugements"].items() if j["g"] == 1]
    cartes = [(i, pleine["jugements"][i]["ev"]) for i in gen]
    retenues, issues = B.regle_e_bh(cartes, 0.05, len(cartes), len(cartes))
    assert all("multiplicite" in iss["pari"] for iss in issues.values())          # la règle a modifié sa copie
    assert {i: JL.empreinte(j["ev"]) for i, j in pleine["jugements"].items()} == avant  # pas les issues du banc
    for i, iss in issues.items():
        assert (iss["verdict_final"] == "survit") == (i in retenues)
    a1 = B.jouer_bras("a", pleine, res["communs"], P, JL.JournalNul(), {})
    B.jouer_bras("d", pleine, res["communs"], P, JL.JournalNul(), {})
    a2 = B.jouer_bras("a", pleine, res["communs"], P, JL.JournalNul(), {})
    assert JL.empreinte(a1) == JL.empreinte(a2)
    # retenues = « survit » sur des trajectoires fabriquées
    rng = np.random.default_rng(B.GRAINES(RACINE, "essai2|trajectoires"))
    for _ in range(200):
        m = int(rng.integers(1, 9))
        cartes = []
        for k in range(m):
            traj = [round(float(v), 6) for v in np.cumsum(rng.normal(0.3, 1.2, 8))]
            cartes.append((f"x{k}", {"trajectoire_log_w": traj, "promue": any(v >= math.log(20) for v in traj)}))
        ret, iss = B.regle_e_bh(cartes, 0.05, m, m)
        assert all((iss[i]["verdict_final"] == "survit") == (i in ret) for i in iss)


def _pleine_fabriquee(pleine, tous_juges, graine):
    """Sortie pleine fabriquée (correction 4) : la structure de `pleine` (8 lignées, 6 générations, 2 réceptions par appel),
    des trajectoires tirées (SeedSequence, R9) ; `tous_juges` : toutes les réceptions jugées (m_r = m_s) ; sinon la seconde
    réception de chaque appel est écartée par le quota (m_r = 2 m_s)."""
    rng = np.random.default_rng(B.GRAINES(RACINE, graine))
    recs, jug = [], {}
    for g in range(1, 7):
        for l in range(8):
            for rang in (1, 2):
                i = f"fab-l{l}-g{g}-r{rang:02d}"
                juge = tous_juges or rang == 1
                recs.append({"id": i, "l": l, "g": g, "rang": rang, "empreinte_loi": i, "refus_memoire": False,
                             "refus": None if juge else "quota", "jugee": juge})
                if juge:
                    traj = [round(float(v), 6) for v in np.cumsum(rng.normal(0.9 if l < 2 else 0.0, 1.5, 8))]
                    ev = {"trajectoire_log_w": traj, "promue": any(v >= math.log(20) for v in traj)}
                    jug[i] = {"ev": ev, "cle_ev": JL.empreinte(ev), "l": l, "g": g}
    return dict(pleine, n_var=2, receptions=recs, jugements=jug)


def test_essai02_d_egale_a_prime_quand_m_r_egale_m_s(course_essai):
    """Correction 4 : `jouer_bras("d")` et `jouer_bras("a_prime")` rendent les mêmes promotions, génération par génération,
    sur une course où tous les essais sont jugés ; quand une réception sur deux est écartée, les deux bras lisent des m
    différents (l'essai distingue bien les deux bras)."""
    res, _ = course_essai
    communs = res["communs"]
    pleine = _pleine_fabriquee(res["pleines"]["peu"], True, "essai2|fabriquee|tous")
    d = B.jouer_bras("d", pleine, communs, P, JL.JournalNul(), {})
    ap = B.jouer_bras("a_prime", pleine, communs, P, JL.JournalNul(), {})
    vue = lambda b: [(x["g"], x["en_course"], x["promues"], x["m"], x["alpha"]) for x in b["generations"]]  # noqa: E731
    assert vue(d) == vue(ap)
    assert sum(len(x["promues"]) for x in d["generations"]) > 0, "la course fabriquée doit promouvoir au moins une carte"
    assert all(x["m"] == x["m_s"] == x["m_r"] for x in d["generations"])
    # artefact : la moitié des réceptions écartées (m_r = 2 m_s) : d lit m_r, a′ lit m_s
    demi = _pleine_fabriquee(res["pleines"]["peu"], False, "essai2|fabriquee|demi")
    d2 = B.jouer_bras("d", demi, communs, P, JL.JournalNul(), {})
    ap2 = B.jouer_bras("a_prime", demi, communs, P, JL.JournalNul(), {})
    assert [x["m"] for x in d2["generations"]] == [2 * x["m_s"] for x in d2["generations"]]
    assert [x["m"] for x in ap2["generations"]] == [x["m_s"] for x in ap2["generations"]]
    assert vue(d2) != vue(ap2)


# --- essai 3 : registre ---------------------------------------------------------------------------------------------------
def test_essai03_registre(course_essai):
    res, _ = course_essai
    for classe in ("peu", "beaucoup"):
        pleine = res["pleines"][classe]
        for nom in ("a", "d", "d_E1", "d_E2", "d_E3"):
            for gen in _gens(res, classe, nom):
                m = gen["m_def"]
                assert m["E2"] <= m["E1"] <= m["E0"] <= m["E3"]
                assert m["E2"] >= gen["m_s"] and gen["m_r"] == m["E0"] == pleine["n_var"] * len(gen["en_course"])
        refusees = [r for r in pleine["receptions"] if r["refus"]]
        assert refusees, "la course d'essai doit compter des essais refusés"
        gen1 = _gens(res, classe, "d")[0]
        assert gen1["m_r"] == sum(1 for r in pleine["receptions"] if r["g"] == 1)   # refusés comptés
    recs = [{"id": "x1", "l": 0, "empreinte_loi": "L", "refus_memoire": False},
            {"id": "x2", "l": 0, "empreinte_loi": "L", "refus_memoire": True}]
    m = B.m_par_definition(recs, 0)
    assert m["E0"] == 2 and m["E1"] == 1
    n1, _ = B.numeroter(recs, 2, [0], 1)
    n2, _ = B.numeroter(recs, 2, [0], 1)
    assert n1 == n2 == [["x1", 1], ["x2", 2]]


# --- essai 4 : chaque garde A1 à A17 et chaque porte, cas sain et artefact ------------------------------------------------
def test_garde_A1(tmp_path):
    dossier = os.path.join(ORGANISME, CONFIG["organisme"]["dossier"])
    assert B.verifier_empreintes_organisme(dossier, CONFIG["organisme"]["fichiers"])
    copie = tmp_path / "pole"
    copie.mkdir()
    for n in CONFIG["organisme"]["fichiers"]:
        shutil.copyfile(os.path.join(dossier, n), copie / n)
    assert B.verifier_empreintes_organisme(str(copie), CONFIG["organisme"]["fichiers"])
    octets = bytearray((copie / "cycle.py").read_bytes())
    octets[100] ^= 1
    (copie / "cycle.py").write_bytes(bytes(octets))
    with pytest.raises(B.GardeA1EmpreinteOrganisme):
        B.verifier_empreintes_organisme(str(copie), CONFIG["organisme"]["fichiers"])


def test_garde_A2():
    B.installer_garde_a2()
    B.verifier_aucun_adaptateur()                                  # cas sain : aucun adaptateur chargé
    B.juger_banc(B.lois_essai_a6()[0], B.lois_essai_a6()[1], RACINE, "essai-A2", CONFIG["juge"])
    with pytest.raises(B.GardeA2Connexion):
        socket.create_connection(("127.0.0.1", 9))
    with pytest.raises(B.GardeA2Connexion):
        socket.socket().connect(("127.0.0.1", 9))
    with pytest.raises(B.GardeA2Connexion):
        __import__("anthropic")
    with pytest.raises(B.GardeA2Connexion):
        __import__("pole.adaptateurs_v56")


def test_garde_A3(course_essai):
    res, _ = course_essai
    assert B.verifier_appariement(res["pleines"]["peu"], res["pleines"]["beaucoup"], P["L"] * P["G"])
    communs = res["communs"]
    # artefact 1 : une lignée ôtée d'une classe
    ote = dict(communs, lignees=communs["lignees"][:-1])
    p_ote = B.jouer_course_pleine(ote, "peu", P, JL.JournalNul())
    with pytest.raises(B.GardeA3Appariement):
        B.verifier_appariement(p_ote, res["pleines"]["beaucoup"], P["L"] * P["G"])
    # artefact 2 : une tranche tirée avec la classe dans sa tâche
    autre = copy.deepcopy(communs)
    lg = autre["lignees"][0]
    lg["tranche"] = B.tirer_tranche(lg["loi_monde"], B.rng_tache(RACINE, "classe=peu|course=7|lignee=0|tranche"), 400, 2)
    lg["marginale_tranche"] = B.marginale_empirique(lg["tranche"]["issues"], 3)
    p_autre = B.jouer_course_pleine(autre, "peu", P, JL.JournalNul())
    with pytest.raises(B.GardeA3Appariement):
        B.verifier_appariement(p_autre, res["pleines"]["beaucoup"], P["L"] * P["G"])


def test_garde_A4(course_essai):
    res, _ = course_essai
    pleine = res["pleines"]["beaucoup"]
    vivantes = [r for r in pleine["receptions"] if r["g"] == 1]
    m_s = sum(r["jugee"] for r in vivantes)
    assert B.numeroter(vivantes, pleine["n_var"], list(range(8)), m_s)[1] == len(vivantes)
    sans_refus = [r for r in vivantes if r is not next(x for x in vivantes if x["refus"])]
    with pytest.raises(B.GardeA4Registre):
        B.numeroter(sans_refus, pleine["n_var"], list(range(8)), m_s)


def test_garde_A5(course_essai):
    res, _ = course_essai
    pleine = res["pleines"]["peu"]
    B.jouer_bras("d", pleine, res["communs"], P, JL.JournalNul(), {})
    with pytest.raises(B.GardeA5CompteM):
        B.jouer_bras("d", pleine, res["communs"], P, JL.JournalNul(), {}, m_passe_decalage=-1)
    with pytest.raises(B.GardeA5CompteM):
        B.regle_e_bh([], 0.05, 3, 2)


ROLES8 = ["vraie_forte", "vraie_faible", "vraie_faible", "vraie_faible", "fausse_diffuse", "fausse_diffuse",
          "fausse_tranchante", "fausse_tranchante"]


def sortie_factice(course, classe, promo, etiquette_vraie="vraie", gain=0.01):
    """Sortie brute fabriquée (essais de l'analyse) : 8 lignées (0–3 à effet), 2 cartes jugées par appel ; `promo` :
    {bras: {génération: [lignées promues]}} (la carte de rang 1 de la lignée est promue)."""
    lignees = [{"l": l, "role": ROLES8[l], "a_effet": l < 4, "cible": None, "force": None} for l in range(8)]
    recs, jug, appels = [], {}, []
    for g in range(1, 7):
        for l in range(8):
            for rang in (1, 2):
                i = f"c{course:04d}-{classe}-l{l}-g{g}-r{rang:02d}"
                recs.append({"id": i, "l": l, "g": g, "rang": rang, "type": "transformee", "empreinte": "0" * 64,
                             "empreinte_loi": i, "mots": 11, "caracteres": 66, "d1": 0.03 if l >= 6 and classe == "beaucoup" else 0.0,
                             "d1_fraiche": 0.0, "numero_course_pleine": 0, "premier_essai_appel": 0, "refus": None,
                             "refus_memoire": False, "similarite_max": 0.0, "jugee": True})
                et = "fausse" if l >= 4 else B.etiquette_oracle(gain, CONFIG["verite"]["seuil_vraie"]) if etiquette_vraie == "calcul" else etiquette_vraie
                jug[i] = {"l": l, "g": g, "trajectoire": [0.0] * 8, "promue_seule": False,
                          "verite": {"gain": None if l >= 4 else gain, "etiquette": et}, "empreinte_engagement": i}
            appels.append({"l": l, "g": g, "receptions": 2, "jugees": 2})
    bras = {}
    for nom, par_g in promo.items():
        en_course, gens = set(range(8)), []
        for g in range(1, 7):
            pr = [f"c{course:04d}-{classe}-l{l}-g{g}-r01" for l in par_g.get(g, []) if l in en_course]
            gens.append({"g": g, "en_course": sorted(en_course), "promues": pr, "m": 16})
            en_course -= set(par_g.get(g, []))
        bras[nom] = {"generations": gens, "tirages": 200 * 96, "appels_emis": 48, "m_portes_a_m_s": 0}
    return {"course": course, "classe": classe, "n_var": 2, "lignees": lignees, "appels_programmes": 48, "appels": appels,
            "receptions": recs, "jugements": jug, "bras": bras, "empreintes_communes": {}}


def _sorties(n, promo_par_classe, **k):
    return {c: [sortie_factice(i, c, promo_par_classe[c], **k) for i in range(n)] for c in ("peu", "beaucoup")}


SAIN = {nom: {1: [0]} for nom in ("a", "a_prime", "b", "c", "d", "T0")}


def _rs(n, R=500):
    return AN.Reechantillonnage(n, R, RACINE, "essais|analyse")


def test_garde_A7():
    res = AN.analyser_sorties(_sorties(20, {"peu": SAIN, "beaucoup": SAIN}), CONFIG, _rs(20))
    assert not res["gardes_de_lecture"]
    deplace = dict(CONFIG, verite={"seuil_vraie": 1.0})   # artefact : seuil de vérité déplacé
    s = {c: [sortie_factice(i, c, SAIN, etiquette_vraie="calcul") for i in range(20)] for c in ("peu", "beaucoup")}
    for c in s:
        for x in s[c]:
            for j in x["jugements"].values():
                if j["verite"]["gain"] is not None:
                    j["verite"]["etiquette"] = B.etiquette_oracle(j["verite"]["gain"], deplace["verite"]["seuil_vraie"])
    res = AN.analyser_sorties(s, CONFIG, _rs(20))
    assert any("A7" in r for r in res["gardes_de_lecture"]) and res["table"]["ligne"] == 0


def test_garde_A8_audit_du_generateur():
    rng = np.random.default_rng(B.GRAINES(RACINE, "essai-A8"))
    cartes = []
    for c in range(60):
        roles = rng.permutation(6)
        for l in range(6):
            conc = 1 if roles[l] < 4 else 0
            for _ in range(12):
                cartes.append((c, int(rng.integers(0, 2 ** 32)), l, 1 + 12 * l, conc, conc if rng.random() < 0.5 else None))
    petit = dict(CONFIG, audit=dict(CONFIG["audit"], reechantillons=200))
    sain = E.audit_generateur(cartes, list(range(60)), petit, RACINE, "essai")
    assert sain["tire"] == []
    fuite = [(c, (k[4] << 31) + (k[1] >> 1), k[2], k[3], k[4], k[5]) for k in cartes for c in [k[0]]]  # rôle dans l'identifiant
    tire = E.audit_generateur(fuite, list(range(60)), petit, RACINE, "essai")
    assert "conception / identifiant" in tire["tire"]
    sortie = {"portes": {"prise": {"passee": True}, "cartes_jugees_par_appel": {"passee": True},
                         "audit_generateur": {"passee": False}}, "audit_generateur": {"peu": tire}}
    with pytest.raises(E.GardeA8Audit):
        E.exiger_portes(sortie)


def test_garde_A9_forces_et_prise():
    f, pas = E.dichotomie(lambda f, k: min(1.0, f / 2.0), 0.5, [0.05, 3.0], 0.03, 10)
    assert abs(min(1.0, f / 2) - 0.5) <= 0.03
    with pytest.raises(E.GardeA9Etalonnage):
        E.dichotomie(lambda f, k: 0.0, 0.9, [0.05, 3.0], 0.03, 10)
    petit = dict(CONFIG, etalonnage=dict(CONFIG["etalonnage"], reechantillons_prise=500))
    assert E.porte_prise([0.2, 0.1, 0.15, 0.3] * 50, petit, RACINE)["passee"]
    manquee = E.porte_prise([0.0] * 200, petit, RACINE)               # grille réduite à un couple sans effet : T0 sans prise
    assert not manquee["passee"]
    with pytest.raises(E.GardeA9Etalonnage):
        E.exiger_portes({"portes": {"prise": manquee, "cartes_jugees_par_appel": {"passee": True},
                                    "audit_generateur": {"passee": True}}})


def test_garde_A10():
    assert B.exiger_fini([0.0, -3.5, 2], "essai")
    with pytest.raises(B.GardeA10NonFini):
        B.exiger_fini([0.0, float("nan")], "essai")
    with pytest.raises(B.GardeA10NonFini):
        _rs(3).bornes([0.0, float("inf"), 1.0])


def test_garde_A11():
    res = AN.analyser_sorties(_sorties(30, {"peu": SAIN, "beaucoup": SAIN}), CONFIG, _rs(30))
    assert not any("A11" in r for r in res["gardes_de_lecture"])
    seuil_seul = dict(SAIN, a={1: [0, 4]})        # artefact : la règle remplacée par le seuil 1/α (fausses promues)
    res = AN.analyser_sorties(_sorties(30, {"peu": seuil_seul, "beaucoup": seuil_seul}), CONFIG, _rs(30))
    assert any("A11" in r for r in res["gardes_de_lecture"]) and res["table"]["ligne"] == 0


def _mini_decisive(dossier, courses=(0, 1)):
    d_c = os.path.join(dossier, "courses")
    os.makedirs(d_c)
    fichiers = {}
    for c in courses:
        r = B.jouer_course(c, RACINE, P, d_c, SHA_CONFIG, None)
        fichiers.update({n: {"sha256": f["sha256"], "octets": f["octets"]} for n, f in r["fichiers"].items()})
    etal = os.path.join(dossier, "etalonnage-factice.json")
    B.ecrire_json_scelle(etal, {"mesures": {"indeterminees": {}}, "portes": {"prise": {"borne_basse": 0.1}}})
    man = {"code": {"analyse_ligne1_v2.py": B.sha256_fichier(os.path.join(CODE, "analyse_ligne1_v2.py"))},
           "fichiers": fichiers, "courses": list(courses),
           "etalonnage": {"chemin": etal, "sha256": B.sha256_fichier(etal)}}
    ch_m = os.path.join(dossier, LA.NOM_MANIFESTE)
    B.ecrire_json_scelle(ch_m, man)
    rapport = RJ.rejouer_dossier(d_c, 1, attendus=2 * len(courses))
    rapport["manifeste_sha256"] = B.sha256_fichier(ch_m)
    B.ecrire_json_scelle(os.path.join(dossier, AN.NOM_REJEU), rapport)
    return ch_m, man


def test_garde_A12_et_chaine_d_analyse(tmp_path):
    ch_m, man = _mini_decisive(str(tmp_path))
    AN.verifier_scellement_avant_analyse(str(tmp_path), ch_m)
    petit = dict(CONFIG, reechantillonnage=dict(CONFIG["reechantillonnage"], reechantillons=200),
                 racines=dict(CONFIG["racines"], reechantillonnage=RACINE))
    res, sha = AN.analyser_dossier(str(tmp_path), petit, ch_m)
    assert B.verifier_scelle_fichier(os.path.join(str(tmp_path), AN.NOM_LECTURE)) and "table" in res
    # artefact : empreinte du programme d'analyse changée dans le manifeste
    faux = os.path.join(str(tmp_path), "manifeste-faux.json")
    B.ecrire_json_scelle(faux, dict(man, code={"analyse_ligne1_v2.py": "0" * 64}))
    with pytest.raises(AN.GardeA12Scellement):
        AN.verifier_scellement_avant_analyse(str(tmp_path), faux)
    # artefact : une sortie brute non scellée
    nom = next(n for n in man["fichiers"] if n.startswith("sortie-"))
    os.remove(os.path.join(str(tmp_path), "courses", nom + ".sha256"))
    with pytest.raises(AN.GardeA12Scellement):
        AN.verifier_scellement_avant_analyse(str(tmp_path), ch_m)


def test_garde_A13(tmp_path):
    arrets = str(tmp_path / "arrets.jsonl")
    code, _ = LA.surveiller([sys.executable, "-B", "-c", "pass"], 60, 0.0, arrets, intervalle=0.1)
    assert code == 0 and not os.path.exists(arrets)
    t = time.monotonic()
    with pytest.raises(LA.GardeA13Duree):
        LA.surveiller([sys.executable, "-B", "-c", "import time; time.sleep(60)"], 1, 0.0, arrets, intervalle=0.1)
    assert time.monotonic() - t < 30
    arret = json.loads(open(arrets, encoding="utf-8").read().splitlines()[0])
    assert arret["garde"] == "A13"
    with pytest.raises(ProcessLookupError):
        os.kill(arret["pid"], 0)


def test_garde_A14():
    sc = CONFIG["preenregistrement"]["horodatage_scellement"]
    assert LA.verifier_derivations({str(2026111902): "2026-11-20T08:00:00.000000Z"}, sc, (2026111902,))
    with pytest.raises(LA.GardeA14Graine):
        LA.verifier_derivations({str(2026111902): "2026-11-19T10:00:00.000000Z"}, sc, (2026111902,))


def test_garde_A15_et_porte(tmp_path):
    assert E.porte_cartes_par_appel({"peu": 2.0, "beaucoup": 1.95}, CONFIG)["passee"]
    r = B.jouer_course(11, RACINE, P, str(tmp_path), SHA_CONFIG, None, bras=("T0",), ecrire=False,
                       memoire_seuil_par_classe={"peu": 0.1})               # artefact : mémoire à 0,1 dans une seule classe
    par = {k: sum(a["jugees"] for a in r["pleines"][k]["appels"]) / len(r["pleines"][k]["appels"]) for k in ("peu", "beaucoup")}
    porte = E.porte_cartes_par_appel(par, CONFIG)
    assert not porte["passee"]
    with pytest.raises(E.GardeA15CartesParAppel):
        E.exiger_portes({"portes": {"prise": {"passee": True}, "cartes_jugees_par_appel": porte,
                                    "audit_generateur": {"passee": True}}})


def test_garde_A16(course_essai, tmp_path):
    _, d = course_essai
    ch = os.path.join(d, "journal-c0007-beaucoup.jsonl.xz")
    assert RJ.rejouer_fichier(ch)["differentes"] == 0
    lignes = lzma.open(ch).read().splitlines()
    # artefact 1 : une trajectoire modifiée dans le journal
    k = next(i for i, l in enumerate(lignes) if b'"trajectoire_log_w"' in l)
    obj = json.loads(lignes[k])
    obj["valeur"]["trajectoire_log_w"][3] += 0.5
    modif = lignes[:k] + [JL.canonique(obj)] + lignes[k + 1:]
    f1 = tmp_path / "j1.jsonl.xz"
    f1.write_bytes(lzma.compress(b"\n".join(modif) + b"\n"))
    with pytest.raises(RJ.GardeA16Rejeu):
        RJ.rejouer_fichier(str(f1))
    # artefact 2 : une ligne ôtée
    f2 = tmp_path / "j2.jsonl.xz"
    f2.write_bytes(lzma.compress(b"\n".join(lignes[:50] + lignes[51:]) + b"\n"))
    with pytest.raises(RJ.GardeA16Rejeu):
        RJ.rejouer_fichier(str(f2))


def test_garde_A17(course_essai):
    res, _ = course_essai
    with B.contexte_etalonnage():
        B.jouer_bras("T0", res["pleines"]["peu"], res["communs"], P, JL.JournalNul(), {})
        with pytest.raises(B.GardeA17BrasEtalonnage):
            B.jouer_bras("a", res["pleines"]["peu"], res["communs"], P, JL.JournalNul(), {})
    assert E.verifier_sortie_sans_bras_interdit({"x": {"bras": {"T0": {}}}})
    with pytest.raises(B.GardeA17BrasEtalonnage):
        E.verifier_sortie_sans_bras_interdit({"x": [{"bras": {"T0": {}, "a": {}}}]})


# --- essai 5 : graines -------------------------------------------------------------------------------------------------------
def test_essai05_graines(course_essai, tmp_path):
    res, _ = course_essai
    r2 = B.jouer_course(7, RACINE, P, str(tmp_path), SHA_CONFIG, None)
    assert {n: f["sha256"] for n, f in res["fichiers"].items()} == {n: f["sha256"] for n, f in r2["fichiers"].items()}
    assert B.GRAINES(RACINE, "tache-a") != B.GRAINES(RACINE, "tache-b")
    assert res["pleines"]["peu"]["empreintes_communes"] == res["pleines"]["beaucoup"]["empreintes_communes"]


# --- essai 6 : vérités --------------------------------------------------------------------------------------------------------
def test_essai06_verites(course_essai):
    res, _ = course_essai
    for lg in res["communs"]["lignees"]:
        if lg["a_effet"]:
            assert B.gain_oracle(lg["loi_monde"], lg["oracle"]) > 0.0
    assert [B.etiquette_oracle(g, 0.005) for g in (0.006, 0.003, -0.001)] == ["vraie", "indeterminee", "fausse"]
    s = sortie_factice(0, "peu", {"a": {1: [4, 6], 2: [0]}}, etiquette_vraie="indeterminee")
    m = AN.mesures_course(s, "a", 0.02)
    assert m["fausses_nul"] == 2 and m["promotions"] == 3 and m["M1_nul"] == 2 / 3
    assert m["M1_oracle"] == 2 / 3                       # carte indéterminée : au dénominateur, hors du numérateur
    assert m["M3"]["stricte"]["toutes"] == 0.0 and m["M3"]["large"]["toutes"] == 0.25


# --- essai 7 : bras b et c -----------------------------------------------------------------------------------------------------
def test_essai07_bras_b_et_c(course_essai):
    seuil = math.log(6 * 2 / 0.05)
    juste = [round(seuil + 1e-6, 6)] + [0.0] * 7
    sous = [round(seuil - 1e-3, 6)] * 8
    cartes = [("x", {"trajectoire_log_w": [0.0] * 7 + juste[:1]}), ("y", {"trajectoire_log_w": sous})]
    assert B.regle_bonferroni(cartes, 0.05, 6, 2) == ["x"]
    c = [("b", {"trajectoire_log_w": [0, 0, 0, 5, 0, 0, 0, 9]}), ("a", {"trajectoire_log_w": [0, 0, 0, 5, 0, 0, 0, 1]}),
         ("c", {"trajectoire_log_w": [9, 9, 9, 4, 9, 9, 9, 9]})]
    assert B.choisir_c(c, 4) == "a"
    res, _ = course_essai
    for classe in ("peu", "beaucoup"):
        b = res["sorties"][classe]["bras"]["c"]
        assert len({x["g"] for x in b["confirmations"]}) == len(b["confirmations"])
        for x in b["confirmations"]:
            assert x["empreinte_engagement"] != x["empreinte_engagement_tri"]
            assert len(x["trajectoire"]) == 8
        for gen in b["generations"]:
            assert len(gen["promues"]) <= 1


# --- essai 8 : témoins sur un jouet analytique ------------------------------------------------------------------------------
def test_essai08_jouet_analytique():
    rng = np.random.default_rng(B.GRAINES(RACINE, "essai8|jouet"))
    n = 4000
    m1 = {x: np.zeros(n) for x in ("a", "a_prime", "b", "d")}
    for i in range(n):
        u = rng.random(6)
        es = np.where(u < 0.02, 25.0, np.where(u < 0.024, 125.0, math.exp(-50)))   # e-valeur exacte : E[e] = 1
        for x in m1:
            for g in range(6):
                cartes = [("n", {"trajectoire_log_w": [round(math.log(es[g]), 6)] * 8, "promue": es[g] >= 20})]
                if x == "a":
                    p, _ = B.regle_e_bh(cartes, 0.05, 1, 1)
                elif x in ("a_prime", "d"):
                    p, _ = B.regle_e_bh(cartes, 0.05 / 6, 1, 1)
                else:
                    p = B.regle_bonferroni(cartes, 0.05, 6, 1)
                if p:
                    m1[x][i] = 1.0
                    break
    rs = AN.Reechantillonnage(n, 2000, RACINE, "essai8|reechantillonnage")
    assert AN.mot_niveau(rs.bornes(m1["a"]), 0.05) == "dépasse"
    for x in ("a_prime", "b", "d"):
        assert AN.mot_niveau(rs.bornes(m1[x]), 0.05) == "tient"


# --- essai 9 : table de lecture -----------------------------------------------------------------------------------------------
def _q(**k):
    base = {"arret": [], "delta_a_positif": False, "d_contre_c": "indécis"}
    for x in ("a", "a_prime", "b", "c", "d", "T0"):
        base[x] = {"peu": "tient", "beaucoup": "tient"}
    for cle, v in k.items():
        if isinstance(v, dict):
            base[cle] = dict(base[cle], **v)
        else:
            base[cle] = v
    return base


OUI = dict(a={"beaucoup": "dépasse"}, b={"beaucoup": "indécis"}, a_prime={"beaucoup": "indécis"}, delta_a_positif=True,
           d_contre_c="d ne tombe pas sous c")


@pytest.mark.parametrize("q, ligne", [
    (_q(arret=["A7"]), 0),
    (_q(d={"peu": "dépasse"}), 1),
    (_q(T0={"beaucoup": "dépasse"}), 2),
    (_q(T0={"beaucoup": "indécis"}), 3),
    (_q(a={"beaucoup": "dépasse"}, b={"beaucoup": "indécis"}), 4),
    (_q(**OUI), 5),
    (_q(a={"beaucoup": "dépasse"}, a_prime={"beaucoup": "indécis"}, b={"beaucoup": "indécis"}, d_contre_c="c domine"), 6),
    (_q(a={"beaucoup": "indécis"}), 7),
    (_q(a_prime={"beaucoup": "dépasse"}), 1),
    (_q(b={"peu": "dépasse"}), 1),
    (_q(a={"beaucoup": "dépasse"}, a_prime={"beaucoup": "indécis"}), 4),
    (_q(**dict(OUI, d_contre_c=AN.mot_d_contre_c({"stricte": {"borne_basse": -0.01, "borne_haute": 0.1},
                                                     "large": {"borne_basse": -0.2, "borne_haute": -0.1}}, "tient", 0.05))), 7),
    (_q(**dict(OUI, b={"peu": "indécis", "beaucoup": "tient"})), 7),
])
def test_essai09_table_de_lecture(q, ligne):
    assert AN.appliquer_table(q)["ligne"] == ligne


# --- essai 10 : journal, rejeu au bit près, mécanisme modifié ----------------------------------------------------------------
def test_essai10_rejeu(course_essai):
    _, d = course_essai
    for classe in ("peu", "beaucoup"):
        ch = os.path.join(d, f"journal-c0007-{classe}.jsonl.xz")
        r = RJ.rejouer_fichier(ch)
        assert r["differentes"] == 0 and r["decisions"] > 0
        assert set(r["par_mecanisme"]) >= {"reception", "memoire", "affinage", "quota", "jugement", "registre",
                                            "promotion_e_bh", "promotion_bonferroni", "promotion_seule", "choix_c", "arret"}
    modifie = RJ.rejouer_fichier(os.path.join(d, "journal-c0007-beaucoup.jsonl.xz"), {"memoire_seuil": 0.3}, lever=False)
    assert modifie["differentes"] > 0 and {x["mecanisme"] for x in modifie["premieres_differences"]} == {"memoire"}


# --- essai 11 : texte des cartes et mémoire ----------------------------------------------------------------------------------
def _transformee(poids, biais, g=1.0, incl=(0.0, 0.0, 0.0)):
    return {"type": "transformee", "base": {"type": "softmax", "poids": poids, "biais": biais}, "puissance": g,
            "inclinaison": list(incl)}


def test_essai11_texte_et_memoire(course_essai, monkeypatch):
    res, _ = course_essai
    textes = [r["texte"] for k in ("peu", "beaucoup") for r in res["pleines"][k]["receptions"]]
    longueurs = {}
    for k in ("peu", "beaucoup"):
        for r in res["pleines"][k]["receptions"]:
            longueurs.setdefault(r["type"], set()).add((len(r["texte"].split()), len(r["texte"])))
    assert longueurs["transformee"] == {(11, len("w00+0.00 " * 6) + len("b0+0.00 " * 3) + len("i1+0.00 i2+0.00"))}
    assert longueurs["si_sinon"] == {(7, len("t+0.00 s+0.00 y+0.00 c+0.00 m0+0.00 m1+0.00 m2+0.00"))}
    for t in textes:
        assert len(set(t.split())) == len(t.split()) and "-0.00" not in t
    assert B.ecrire_valeur(-0.004) == B.ecrire_valeur(0.004) == "+0.00"
    W = [[0.5, -0.3], [0.2, 0.7], [-0.4, 0.5]]
    b = [0.1, -0.2, 0.3]
    t0 = B.texte_carte(_transformee(W, b, incl=(0.0, 0.3, -0.2)))
    sim = lambda x, y: B.similarite(x, y, 3)                                  # noqa: E731
    assert sim(t0, B.texte_carte(_transformee(W, b, incl=(0.0, 0.3, -0.2)))) == 1.0
    assert sim(B.texte_carte(_transformee(W, b, incl=(0.0, 0.004, -0.2))), B.texte_carte(_transformee(W, b, incl=(0.0, -0.004, -0.2)))) == 1.0
    dernier = B.texte_carte(_transformee(W, b, incl=(0.0, 0.3, 0.2)))
    dixieme = B.texte_carte(_transformee(W, b, incl=(0.0, -0.3, -0.2)))
    W6 = [[0.5, -0.3], [0.2, 0.7], [-0.4, -0.5]]
    sixieme = B.texte_carte(_transformee(W6, b, incl=(0.0, 0.3, -0.2)))
    assert sim(t0, dernier) == 8 / 10 and sim(t0, dixieme) == 7 / 11 and sim(t0, sixieme) == 6 / 12
    assert B.decider_memoire(dernier, [t0], 0.6, 3, 1e-12)[1] and B.decider_memoire(dixieme, [t0], 0.6, 3, 1e-12)[1]
    assert not B.decider_memoire(sixieme, [t0], 0.6, 3, 1e-12)[1]
    marg = [0.3, 0.3, 0.4]
    s1 = {"type": "si_sinon", "condition": {"indice": 0, "seuil": 1.31}, "si": {"type": "fixe", "probas": [0.75, 0.125, 0.125]},
          "sinon": {"type": "fixe", "probas": marg}}
    s2 = copy.deepcopy(s1)
    s2["condition"]["indice"] = 1
    assert sim(B.texte_carte(s1), B.texte_carte(s2)) == 4 / 6
    assert B.decider_memoire(B.texte_carte(s2), [B.texte_carte(s1)], 0.6, 3, 1e-12)[1]
    # la voie écartée n'est jamais appelée (interception)
    def interdit(*a, **k):
        raise AssertionError("voie écartée appelée")
    monkeypatch.setattr(B.MEM, "Memoire", interdit)
    monkeypatch.setattr(B.MEM, "texte_fiche", interdit)
    monkeypatch.setattr(B.MEM, "normaliser_texte", interdit)
    monkeypatch.setattr(B.OUT, "normaliser_texte", interdit)
    B.jouer_course_pleine(res["communs"], "beaucoup", P, JL.JournalNul())
    # une carte n'est comparée qu'aux textes de sa lignée ; mémoire et d-E2 passent par la même fonction
    _, d = course_essai
    _, objets, decisions = JL.lire(os.path.join(d, "journal-c0007-beaucoup.jsonl.xz"))
    lignee_du_texte = {x["entrees"]["texte"]: x["entrees"]["lignee"] for x in decisions if x["mecanisme"] == "reception"}
    for x in decisions:
        if x["mecanisme"] == "memoire":
            l = lignee_du_texte[x["entrees"]["texte"]]
            assert all(lignee_du_texte[c] == l for c in x["entrees"]["comparees"])
    source = inspect.getsource(B)
    assert source.count("MEM.jaccard(") == 1 and source.count("MEM.bardeaux(") == 2
    assert "similarite(" in inspect.getsource(B.decider_memoire)
    assert 'r["refus_memoire"]' in inspect.getsource(B.m_par_definition)


# --- dépôt : morceaux, manifeste scellé, refus au-delà du plafond --------------------------------------------------------------
def test_depot_morceaux_et_plafond(tmp_path):
    src = tmp_path / "chaine"
    (src / "decisive" / "courses").mkdir(parents=True)
    rng = np.random.default_rng(B.GRAINES(RACINE, "essai-depot"))
    for i in range(6):
        ch = src / "decisive" / "courses" / f"journal-c{i:04d}-peu.jsonl.xz"
        ch.write_bytes(lzma.compress(rng.bytes(300_000), preset=0))
    m, sha = LA.empaqueter(str(src), str(tmp_path / "depot"))                      # réglages réels : un seul morceau
    assert len(m["parties"]) == 1 and sum(len(p["membres"]) for p in m["parties"]) == 6
    assert B.verifier_scelle_fichier(str(tmp_path / "depot" / LA.NOM_DEPOT))
    m2, _ = LA.empaqueter(str(src), str(tmp_path / "depot2"), morceau_max=700_000, marge=0)   # morceaux de deux fichiers
    assert len(m2["parties"]) == 3 and sum(len(p["membres"]) for p in m2["parties"]) == 6
    for p in m2["parties"]:
        assert B.verifier_scelle_fichier(str(tmp_path / "depot2" / p["nom"])) and p["octets"] <= 700_000
    with pytest.raises(LA.DepotTropGros):
        LA.empaqueter(str(src), str(tmp_path / "depot3"), depot_max=1_000_000)          # au-delà du plafond du dépôt


# ==============================================================================================================================
# Code v2 : essais des corrections, chacune sur un cas sain et sur un artefact (R5)
# ==============================================================================================================================
CLASSES = tuple(CONFIG["proposeurs"]["engagements_par_appel"])


def _jouer_t0(dossier):
    return lambda c: B.jouer_course(c, RACINE, P, dossier, SHA_CONFIG, None, bras=("T0",))


def _empreintes_course(dossier, course):
    return {n: B.sha256_fichier(os.path.join(dossier, n)) for n in E.fichiers_de_course(dossier, course)}


# --- correction 1 : fichiers d'une course interrompue déplacés, inventoriés, jamais effacés ---------------------------------------
def test_correction1_recuperation_des_partiels(tmp_path, monkeypatch):
    propre = str(tmp_path / "propre")
    os.makedirs(propre)
    _jouer_t0(propre)(0)
    attendues = _empreintes_course(propre, 0)
    assert E.course_deja_faite(propre, 0, CLASSES) and len(attendues) == 8
    # cas sain : course scellée, jouer_courses ne la rejoue pas et ne déplace rien ; aucun dossier de récupération créé
    assert E.jouer_courses(None, propre, 1, _jouer_t0(propre), CLASSES) == []
    assert _empreintes_course(propre, 0) == attendues
    assert E.recuperer_partiels(propre, []) == [] and E.inventaire_recuperes(propre) == []
    assert not os.path.exists(os.path.join(propre, E.DOSSIER_RECUPERES))
    # course interrompue : la sortie « beaucoup » encore provisoire, son compagnon absent, un journal provisoire de la course 1
    d = str(tmp_path / "interrompue")
    shutil.copytree(propre, d)
    os.replace(os.path.join(d, "sortie-c0000-beaucoup.json.xz"), os.path.join(d, "sortie-c0000-beaucoup.json.xz.partiel"))
    os.remove(os.path.join(d, "sortie-c0000-beaucoup.json.xz.sha256"))
    with open(os.path.join(d, "journal-c0001-peu.jsonl.xz.partiel"), "wb") as f:
        f.write(b"partiel")
    avant = {n: B.sha256_fichier(os.path.join(d, n)) for n in os.listdir(d)}
    assert not E.course_deja_faite(d, 0, CLASSES)
    # jouer_courses : récupère (déplace) puis rejoue les courses 0 et 1 depuis leurs graines
    E.jouer_courses(None, d, 2, _jouer_t0(d), CLASSES)
    assert E.course_deja_faite(d, 0, CLASSES) and E.course_deja_faite(d, 1, CLASSES)
    assert _empreintes_course(d, 0) == attendues                                   # rejouée au bit près
    rep = os.path.join(d, E.DOSSIER_RECUPERES, "reprise-01")
    inv = B.lire_json_verifie(os.path.join(rep, E.NOM_INVENTAIRE_RECUPERES))
    assert sorted(x["nom"] for x in inv["fichiers"]) == sorted(avant)              # rien d'effacé : tout est déplacé
    for x in inv["fichiers"]:
        assert B.sha256_fichier(os.path.join(rep, x["nom"])) == avant[x["nom"]] == x["sha256"]
    listes = {x["chemin"] for x in E.inventaire_recuperes(d)}
    assert {os.path.join(E.DOSSIER_RECUPERES, "reprise-01", n) for n in avant} <= listes
    # le rejeu ne voit pas les fichiers récupérés (dossier à part) et recoupe les courses rejouées
    assert RJ.rejouer_dossier(d, 1, attendus=4)["recoupement"]["verdict"] == "concordant"
    # une seconde reprise prend un nom neuf (on n'écrase jamais)
    with open(os.path.join(d, "journal-c0002-peu.jsonl.xz.partiel"), "wb") as f:
        f.write(b"autre")
    E.recuperer_partiels(d, [2])
    assert os.path.isdir(os.path.join(d, E.DOSSIER_RECUPERES, "reprise-02")) and os.path.isfile(os.path.join(rep, "journal-c0001-peu.jsonl.xz.partiel"))
    # artefact : un fichier qui change pendant son déplacement lève un arrêt nommé
    with open(os.path.join(d, "journal-c0003-peu.jsonl.xz.partiel"), "wb") as f:
        f.write(b"x")
    vrai_rename = os.rename

    def rename_alterant(src, dst):
        vrai_rename(src, dst)
        with open(dst, "ab") as f:
            f.write(b"!")
    monkeypatch.setattr(E.os, "rename", rename_alterant)
    with pytest.raises(B.ArretBanc):
        E.recuperer_partiels(d, [3])
    monkeypatch.setattr(E.os, "rename", vrai_rename)
    # artefact du code v1 : `nettoyer_partiels` effaçait ; le code v2 n'efface rien
    assert "os.remove" not in inspect.getsource(E.recuperer_partiels) and not hasattr(E, "nettoyer_partiels")


# --- correction 2 : la reprise de l'étalonnage refait les portes ---------------------------------------------------------------
def _sortie_etal(passees=(True, True, True), bloquantes=True, en_tete=(), code=None):
    p = dict(zip(("prise", "cartes_jugees_par_appel", "audit_generateur"), passees))
    return {"portes": {"prise": {"passee": p["prise"]},
                       "cartes_jugees_par_appel": {"passee": p["cartes_jugees_par_appel"], "ecart": 0.2, "seuil": 0.1},
                       "audit_generateur": {"passee": p["audit_generateur"]}},
            "audit_generateur": {}, "portes_bloquantes": bloquantes, "en_tete": list(en_tete),
            "configuration_sha256": SHA_CONFIG, "code": {"fichiers": code or {"x": "0"}}, "bras_calcules": ["T0"],
            "parametres": {"forces_dans_l_ordre_des_roles": PE["forces"], "s": PE["s"], "c": PE["c"]}}


def test_correction2_reprise_de_l_etalonnage_exige_les_portes(tmp_path):
    for nom, sortie, attendu in (("saine", _sortie_etal(), None),
                                 ("a15", _sortie_etal((True, False, True)), E.GardeA15CartesParAppel),
                                 ("a9", _sortie_etal((False, True, True)), E.GardeA9Etalonnage),
                                 ("a8", _sortie_etal((True, True, False)), E.GardeA8Audit),
                                 ("fumee", _sortie_etal(bloquantes=False), B.ArretBanc)):
        d = str(tmp_path / nom)
        os.makedirs(d)
        B.ecrire_json_scelle(os.path.join(d, E.NOM_SORTIE), sortie)
        if attendu is None:
            assert E.etalonner(d, CONFIG, SHA_CONFIG, None)["portes"]["prise"]["passee"]
        else:
            with pytest.raises(attendu):
                E.etalonner(d, CONFIG, SHA_CONFIG, None)                         # reprise, portes bloquantes
        # en fumée (portes non bloquantes), la reprise rend la sortie sans arrêter
        assert E.etalonner(d, CONFIG, SHA_CONFIG, None, portes_bloquantes=False)["portes"]
    # artefact : une sortie altérée après scellement est refusée à la reprise
    d = str(tmp_path / "saine")
    with open(os.path.join(d, E.NOM_SORTIE), "a", encoding="utf-8") as f:
        f.write(" ")
    with pytest.raises(B.ArretBanc):
        E.etalonner(d, CONFIG, SHA_CONFIG, None)


# --- correction 3 : la dichotomie écrit ses pas avant la garde A9 --------------------------------------------------------------
def test_correction3_dichotomie_ecrit_ses_pas(tmp_path, monkeypatch):
    d = str(tmp_path)
    ch = E.chemin_libre(d, "pas", ".json")
    f, pas = E.dichotomie(lambda f, k: min(1.0, f / 2.0), 0.5, [0.05, 3.0], 0.03, 10, chemin_pas=ch)
    assert pas and not os.path.exists(ch)                                        # cas sain : rien d'écrit
    with pytest.raises(E.GardeA9Etalonnage) as e:
        E.dichotomie(lambda f, k: 0.0, 0.9, [0.05, 3.0], 0.03, 10, chemin_pas=ch, contexte={"forces_deja_atteintes": {"0.9": 1}})
    ecrit = B.lire_json_verifie(ch)
    assert len(ecrit["pas"]) == 10 == len(e.value.pas) and ecrit["contexte"]["forces_deja_atteintes"] == {"0.9": 1}
    assert e.value.chemin_pas == ch and ecrit["garde"] == "A9"
    # étage des forces : la cible manquée laisse un fichier neuf par échec, les forces déjà atteintes comprises (aucun
    # jugement : la promotion est remplacée par un taux fabriqué ; racine des essais)
    cfg = copy.deepcopy(CONFIG)
    cfg["etalonnage"]["forces"].update(jugements_par_pas=4, pas_max=3, tolerance=0.1)
    E._ETAT.update(P=B.parametres(cfg, PE["forces"], PE["s"], PE["c"]), racine=RACINE)
    # taux fabriqué : la cible elle-même pour les cibles 0,90 et 0,50 (atteintes au premier pas), zéro pour 0,30 (manquée)
    monkeypatch.setattr(E, "_promotion_monde_seul", lambda args: args[0] if args[0] >= 0.5 else 0.0)
    for k in (1, 2):
        with pytest.raises(E.GardeA9Etalonnage):
            E.etalonner_forces(None, [], d)
        ecrit = B.lire_json_verifie(os.path.join(d, f"etape-forces-echec-A9-{k:02d}.json"))
        assert ecrit["cible"] == 0.3 and len(ecrit["pas"]) == 3 and sorted(ecrit["contexte"]["forces_deja_atteintes"]) == ["0.5", "0.9"]


# --- correction 5 : gardes ajoutées par le développeur v1, cas sain et artefact ------------------------------------------------
def test_correction5_refus_de_la_course_decisive(tmp_path, monkeypatch):
    code = {"commit": "0" * 40, "arbre_propre": True, "fichiers": {"x": "0"}}
    assert LA.verifier_etalonnage_pour_decisive(_sortie_etal(), SHA_CONFIG, code, "reel")
    for sortie, attendu in ((_sortie_etal((True, False, True)), B.ArretBanc),
                            (_sortie_etal(bloquantes=False), B.ArretBanc),
                            (_sortie_etal(en_tete=["part des cartes indéterminées 0.25 au-dessus de 0.2"]), LA.DecisionMereRequise),
                            (dict(_sortie_etal(), configuration_sha256="0" * 64), B.ArretBanc),
                            (_sortie_etal(code={"x": "1"}), B.ArretBanc),
                            (dict(_sortie_etal(), x={"bras": {"a": {}}}), B.GardeA17BrasEtalonnage)):
        with pytest.raises(attendu):
            LA.verifier_etalonnage_pour_decisive(sortie, SHA_CONFIG, code, "reel")
    assert LA.verifier_etalonnage_pour_decisive(_sortie_etal((True, False, True)), SHA_CONFIG, code, "fumee")
    # la course décisive appelle bien ces refus avant toute graine ou course : sortie d'étalonnage avec la part en tête
    d = str(tmp_path)
    os.makedirs(os.path.join(d, "etalonnage"))
    B.ecrire_json_scelle(os.path.join(d, "etalonnage", E.NOM_SORTIE), _sortie_etal(en_tete=["part au-dessus de 0.2"]))
    monkeypatch.setattr(LA, "exiger_code_commis", lambda mode, dossier=None: code)
    a = types.SimpleNamespace(sortie=d, processus=1)
    with pytest.raises(LA.DecisionMereRequise):
        LA.decisive(a, CONFIG, SHA_CONFIG, None, "reel")
    assert not os.path.exists(os.path.join(d, "decisive", "courses"))
    # sortie d'étalonnage absente : refus
    with pytest.raises(B.ArretBanc):
        LA.decisive(types.SimpleNamespace(sortie=str(tmp_path / "vide"), processus=1), CONFIG, SHA_CONFIG, None, "reel")


def _git(dossier, *args):
    return subprocess.run(["git", "-C", dossier, "-c", "user.name=essai", "-c", "user.email=essai@exemple.invalid", *args],
                          capture_output=True, text=True, check=True)


def test_correction5_code_commis(tmp_path):
    d = str(tmp_path / "depot")
    os.makedirs(d)
    for n in E.FICHIERS_CODE:
        shutil.copyfile(os.path.join(CODE, n), os.path.join(d, n))
    _git(d, "init", "-q")
    _git(d, "add", "-A")
    _git(d, "commit", "-qm", "code")
    e = LA.exiger_code_commis("reel", d)
    assert e["arbre_propre"] and e["fichiers"] == {n: B.sha256_fichier(os.path.join(CODE, n)) for n in E.FICHIERS_CODE}
    # artefact 1 : un fichier neuf non suivi
    with open(os.path.join(d, "neuf.py"), "w", encoding="utf-8") as f:
        f.write("# neuf\n")
    with pytest.raises(B.ArretBanc):
        LA.exiger_code_commis("reel", d)
    assert not LA.exiger_code_commis("fumee", d)["arbre_propre"]                  # toléré en fumée, et dit
    os.remove(os.path.join(d, "neuf.py"))
    assert LA.exiger_code_commis("reel", d)["arbre_propre"]
    # artefact 2 : un octet changé dans un fichier suivi
    ch = os.path.join(d, "lancer_ligne1_v2.py")
    octets = bytearray(open(ch, "rb").read())
    octets[10] ^= 1
    open(ch, "wb").write(bytes(octets))
    with pytest.raises(B.ArretBanc):
        LA.exiger_code_commis("reel", d)
    # artefact 3 : hors d'un dépôt
    with pytest.raises(B.ArretBanc):
        LA.exiger_code_commis("reel", str(tmp_path))


def test_correction5_racines_et_preparer():
    assert LA.verifier_racines(CONFIG, "reel")
    assert LA.verifier_racines(LA.configuration_fumee(CONFIG), "fumee")
    for k in ("essais", "etalonnage", "decisive", "reechantillonnage"):
        with pytest.raises(B.ConfigurationRefusee):
            LA.verifier_racines(dict(CONFIG, racines=dict(CONFIG["racines"], **{k: 1})), "reel")
        fumee = LA.configuration_fumee(CONFIG)
        with pytest.raises(B.ConfigurationRefusee):
            LA.verifier_racines(dict(fumee, racines=dict(fumee["racines"], **{k: CONFIG["racines"]["decisive"]})), "fumee")
    config, sha, prov = LA.preparer(ORGANISME, "reel")
    assert sha == SHA_CONFIG and prov["sha256"] == B.PREREG_SHA256 and config["version"] == "configuration-ligne1-v2"


def test_correction5_refus_d_ecraser(tmp_path):
    ch = str(tmp_path / "x.json")
    assert B.ecrire_json_scelle(ch, {"a": 1})
    with pytest.raises(FileExistsError):
        B.ecrire_json_scelle(ch, {"a": 2})
    chx = str(tmp_path / "x.json.xz")
    assert B.ecrire_json_xz_scelle(chx, {"a": 1})
    with pytest.raises(FileExistsError):
        B.ecrire_json_xz_scelle(chx, {"a": 2})
    j = JL.Journal(str(tmp_path / "j.jsonl.xz"), {"course": 0})
    j.fermer()
    with pytest.raises(FileExistsError):
        JL.Journal(str(tmp_path / "j.jsonl.xz"), {"course": 0})
    os.makedirs(str(tmp_path / "src"))
    LA.empaqueter(str(tmp_path / "src"), str(tmp_path / "depot"))
    with pytest.raises(FileExistsError):
        LA.empaqueter(str(tmp_path / "src"), str(tmp_path / "depot"))
    assert B.lire_json_verifie(ch) == {"a": 1} and B.lire_json_xz_verifie(chx) == {"a": 1}


def test_configuration_v2_porte_les_empreintes_du_code(tmp_path):
    assert LA.verifier_code_configuration(CONFIG)
    assert CONFIG["version"] == "configuration-ligne1-v2"
    # artefact 1 : une empreinte fausse dans la configuration
    faux = copy.deepcopy(CONFIG)
    faux["code"]["fichiers"]["lancer_ligne1_v2.py"] = "0" * 64
    with pytest.raises(LA.CodeDifferentDeLaConfiguration):
        LA.verifier_code_configuration(faux)
    # artefact 2 : un fichier du code v2 absent de la liste
    faux = copy.deepcopy(CONFIG)
    del faux["code"]["fichiers"]["rejouer_journal_ligne1_v2.py"]
    with pytest.raises(LA.CodeDifferentDeLaConfiguration):
        LA.verifier_code_configuration(faux)
    # artefact 3 : un octet changé dans une copie du code
    d = str(tmp_path / "code")
    os.makedirs(os.path.join(d, "essais"))
    for n in list(E.FICHIERS_CODE) + list(E.FICHIERS_ESSAIS):
        shutil.copyfile(os.path.join(CODE, n), os.path.join(d, n))
    assert LA.verifier_code_configuration(CONFIG, d)
    ch = os.path.join(d, "etalonnage_ligne1_v2.py")
    octets = bytearray(open(ch, "rb").read())
    octets[5] ^= 1
    open(ch, "wb").write(bytes(octets))
    with pytest.raises(LA.CodeDifferentDeLaConfiguration):
        LA.verifier_code_configuration(CONFIG, d)


def test_en_tete_du_journal_porte_le_code_v2(course_essai):
    _, d = course_essai
    entete, _, _ = JL.lire(os.path.join(d, "journal-c0007-peu.jsonl.xz"))
    assert set(entete["code"]) == set(E.FICHIERS_CODE)
    assert entete["code"] == {n: B.sha256_fichier(os.path.join(CODE, n)) for n in E.FICHIERS_CODE}


# --- correction 6 : empreinte de l'ensemble du dépôt ----------------------------------------------------------------------------
def test_correction6_empreinte_de_l_ensemble(tmp_path):
    src = tmp_path / "chaine"
    (src / "decisive" / "courses" / E.DOSSIER_RECUPERES / "reprise-01").mkdir(parents=True)
    rng = np.random.default_rng(B.GRAINES(RACINE, "essai-depot-v2"))
    for i in range(4):
        (src / "decisive" / "courses" / f"journal-c{i:04d}-peu.jsonl.xz").write_bytes(lzma.compress(rng.bytes(200_000), preset=0))
    recup = src / "decisive" / "courses" / E.DOSSIER_RECUPERES / "reprise-01" / "journal-c0004-peu.jsonl.xz.partiel"
    recup.write_bytes(b"partiel")
    (src / "etat.json.partiel").write_bytes(b"{}")                                 # provisoire hors récupération : exclu
    m, _ = LA.empaqueter(str(src), str(tmp_path / "depot"), morceau_max=500_000, marge=0)
    membres = {k for p in m["parties"] for k in p["membres"]}
    assert os.path.relpath(str(recup), str(src)) in membres and "etat.json.partiel" not in membres
    attendu = JL.empreinte(sorted([os.path.relpath(str(f), str(src)), B.sha256_fichier(str(f)), os.path.getsize(str(f))]
                                  for f in [recup] + sorted((src / "decisive" / "courses").glob("journal-*.xz"))))
    assert m["empreinte_ensemble"]["sha256"] == attendu == LA.verifier_depot(str(tmp_path / "depot"))
    assert len(m["parties"]) > 1 and m["membres"] == 5
    # artefact 1 : un octet changé dans les données d'un membre, à l'intérieur d'un morceau
    ch = str(tmp_path / "depot" / m["parties"][0]["nom"])
    with tarfile.open(ch) as tf:
        premier = tf.getmembers()[0]
        position = premier.offset_data
    octets = bytearray(open(ch, "rb").read())
    octets[position + 10] ^= 1
    open(ch, "wb").write(bytes(octets))
    with pytest.raises(LA.DepotIncoherent):
        LA.verifier_depot(str(tmp_path / "depot"))
    # artefact 2 : manifeste refait avec une empreinte d'ensemble fausse
    m2, _ = LA.empaqueter(str(src), str(tmp_path / "depot2"), morceau_max=500_000, marge=0)
    faux = dict(m2, empreinte_ensemble=dict(m2["empreinte_ensemble"], sha256="0" * 64))
    os.remove(str(tmp_path / "depot2" / LA.NOM_DEPOT))
    os.remove(str(tmp_path / "depot2" / (LA.NOM_DEPOT + ".sha256")))
    B.ecrire_json_scelle(str(tmp_path / "depot2" / LA.NOM_DEPOT), faux)
    with pytest.raises(LA.DepotIncoherent):
        LA.verifier_depot(str(tmp_path / "depot2"))
    # artefact 3 : l'empreinte d'un membre changée au manifeste, empreinte de l'ensemble recalculée en conséquence : seule
    # la relecture des membres dans le morceau le voit
    m3, _ = LA.empaqueter(str(src), str(tmp_path / "depot3"), morceau_max=500_000, marge=0)
    faux = copy.deepcopy(m3)
    membre = sorted(faux["parties"][0]["membres"])[0]
    faux["parties"][0]["membres"][membre]["sha256"] = "0" * 64
    faux["empreinte_ensemble"]["sha256"] = LA.empreinte_ensemble(faux["parties"])
    os.remove(str(tmp_path / "depot3" / LA.NOM_DEPOT))
    os.remove(str(tmp_path / "depot3" / (LA.NOM_DEPOT + ".sha256")))
    B.ecrire_json_scelle(str(tmp_path / "depot3" / LA.NOM_DEPOT), faux)
    with pytest.raises(LA.DepotIncoherent):
        LA.verifier_depot(str(tmp_path / "depot3"))


# --- correction 7 : versions et commit de l'organisme dans la sortie de l'étalonnage -------------------------------------------
def test_correction7_provenance_dans_la_sortie_de_l_etalonnage(tmp_path):
    """La sortie de l'étalonnage porte versions et commit de l'organisme. Essai de construction de la sortie seulement :
    racine des essais pour toutes les étapes, forces et couple (s, c) fabriqués (valeurs d'essai déposées comme étapes
    déjà faites : aucune dichotomie ni grille n'est calculée), deux courses par classe rejouées par T0, portes non
    bloquantes ; aucune valeur de porte ni de mesure n'est lue par l'essai."""
    prov = E.provenance_calcul(CONFIG)
    assert prov["versions"]["python"] == sys.version and prov["versions"]["numpy"] == np.__version__
    assert prov["organisme"]["commit_attendu"] == CONFIG["organisme"]["commit"]
    assert prov["organisme"]["fichiers"] == CONFIG["organisme"]["fichiers"]
    cfg = copy.deepcopy(CONFIG)
    cfg["racines"] = {k: RACINE for k in cfg["racines"]}
    cfg["etalonnage"].update(courses_par_classe=2, reechantillons_prise=50)
    cfg["audit"]["reechantillons"] = 20
    d = str(tmp_path / "etalonnage")
    os.makedirs(d)
    cibles = [r["cible"] for r in cfg["monde"]["roles"] if r["a_effet"]]
    B.ecrire_json_scelle(os.path.join(d, "etape-forces.json"), {str(c): {"force": f, "pas": []} for c, f in zip(cibles, PE["forces"])})
    B.ecrire_json_scelle(os.path.join(d, "etape-grille.json"), {"couples": [], "retenu": {"s": PE["s"], "c": PE["c"], "taux": None}})
    sortie = E.etalonner(d, cfg, SHA_CONFIG, None, processus=1, portes_bloquantes=False, code={"fichiers": {}})
    assert sortie["versions"] == prov["versions"] and sortie["organisme"]["commit_attendu"] == CONFIG["organisme"]["commit"]
    assert sortie["partiels_recuperes"] == [] and sortie["bras_calcules"] == ["T0"]
    assert B.verifier_scelle_fichier(os.path.join(d, E.NOM_SORTIE))
    # artefact : la reprise de cette sortie (écrite sans portes bloquantes) par une étape réelle est refusée
    with pytest.raises(B.ArretBanc):
        E.etalonner(d, cfg, SHA_CONFIG, None)
    # le manifeste de la course décisive porte les mêmes champs (lecture du code : la course décisive n'est pas jouée ici)
    source = inspect.getsource(LA.decisive)
    assert "E.provenance_calcul(config)" in source and "partiels_recuperes" in source and "versions_identiques" in source


# --- recommandation (a) : recoupement du rejeu avec la sortie brute ; M1-nul de l'audit de symétrie ---------------------------
def _rechainer(lignes):
    import hashlib
    out, precedente = [], JL.ZERO
    for i, b in enumerate(lignes):
        o = json.loads(b)
        o["precedente"], o["n"] = precedente, i
        b = JL.canonique(o)
        out.append(b)
        precedente = hashlib.sha256(b).hexdigest()
    return out


def test_rejeu_recoupement_avec_la_sortie_brute(course_essai, tmp_path):
    _, d = course_essai
    for k in CLASSES:
        ch = os.path.join(d, f"journal-c0007-{k}.jsonl.xz")
        r = RJ.rejouer_fichier(ch, sortie=RJ.sortie_de_journal(ch), m1_nul=True)
        assert r["recoupement"]["ecarts"] == 0 and r["recoupement"]["controles"] > 100
        assert set(r["recoupement"]["m1_nul_concorde"]) == set(B.BRAS) and all(r["recoupement"]["m1_nul_concorde"].values())
    rapport = RJ.rejouer_dossier(d, 1, courses=[7], m1_nul=True)
    assert rapport["recoupement"]["verdict"] == "concordant" and rapport["recoupement"]["m1_nul"] == "concordant"
    assert "M1_nul" not in json.dumps(rapport)                                     # aucune valeur de métrique écrite
    ch = os.path.join(d, "journal-c0007-beaucoup.jsonl.xz")
    entete, objets, decisions = JL.lire(ch)
    brute = B.lire_json_xz_verifie(RJ.sortie_de_journal(ch))
    assert RJ.recouper(entete, objets, decisions, brute)[0] == []
    # artefacts en mémoire : m d'une promotion, m_brut, promues d'un arrêt, effet d'une lignée, M1-nul
    def premier(mec, nom=None):
        return next(i for i, x in enumerate(decisions) if x["mecanisme"] == mec and (nom is None or x["partie"] == f"bras={nom}"))
    for champ, delta in (("m", 1), ("m_brut", 1)):
        dec = copy.deepcopy(decisions)
        dec[premier("promotion_e_bh", "d")]["entrees"][champ] += delta
        assert RJ.recouper(entete, objets, dec, brute)[0]
    # m changé à la fois dans le journal et dans la sortie brute : seul le registre le voit
    dec = copy.deepcopy(decisions)
    i_p = premier("promotion_e_bh", "d")
    dec[i_p]["entrees"]["m"] += 1
    meme = copy.deepcopy(brute)
    g_p = dec[i_p]["entrees"]["generation"]
    next(x for x in meme["bras"]["d"]["generations"] if x["g"] == g_p)["m"] += 1
    ecarts = RJ.recouper(entete, objets, dec, meme)[0]
    assert ecarts and all("m du registre" in x or "registre" in x for x in ecarts)
    dec = copy.deepcopy(decisions)
    dec[premier("arret", "T0")]["entrees"]["promues"].append(["inventee", 0])
    assert RJ.recouper(entete, objets, dec, brute)[0]
    promue = next((g["promues"][0], s) for s in B.BRAS for g in brute["bras"][s]["generations"] if g["promues"])
    l_promue = brute["jugements"][promue[0]]["l"]
    fausse = copy.deepcopy(brute)
    for x in fausse["lignees"]:
        if x["l"] == l_promue:
            x["a_effet"] = not x["a_effet"]
    assert RJ.recouper(entete, objets, decisions, fausse)[0]
    assert not all(RJ.recouper_m1_nul(objets, decisions, fausse).values())
    # artefact sur fichiers : sortie brute réécrite (lignées en course d'un bras changées), scellée de nouveau
    d2 = str(tmp_path)
    shutil.copyfile(ch, os.path.join(d2, os.path.basename(ch)))
    shutil.copyfile(ch + ".sha256", os.path.join(d2, os.path.basename(ch) + ".sha256"))
    alteree = copy.deepcopy(brute)
    alteree["bras"]["d"]["generations"][1]["en_course"] = alteree["bras"]["d"]["generations"][1]["en_course"][1:]
    sortie2 = os.path.join(d2, "sortie-c0007-beaucoup.json.xz")
    B.ecrire_json_xz_scelle(sortie2, alteree)
    with pytest.raises(RJ.GardeA16Recoupement):
        RJ.rejouer_fichier(os.path.join(d2, os.path.basename(ch)), sortie=sortie2)
    with pytest.raises(RJ.GardeA16Recoupement):
        RJ.rejouer_dossier(d2, 1)
    # artefact sur fichiers : m d'une promotion changé dans le journal, chaîne refaite (le rejeu compte la différence
    # sans lever, le recoupement lève)
    lignes = lzma.open(ch).read().splitlines()
    k = next(i for i, b in enumerate(lignes) if b'"mecanisme":"promotion_e_bh"' in b and b'"partie":"bras=d"' in b)
    o = json.loads(lignes[k])
    o["entrees"]["m"] += 1
    lignes[k] = JL.canonique(o)
    f3 = str(tmp_path / "j3.jsonl.xz")
    open(f3, "wb").write(lzma.compress(b"\n".join(_rechainer(lignes)) + b"\n"))
    with pytest.raises(RJ.GardeA16Recoupement):
        RJ.rejouer_fichier(f3, lever=False, sortie=RJ.sortie_de_journal(ch))
    # artefact : sortie brute absente
    with pytest.raises(RJ.GardeA16Recoupement):
        RJ.rejouer_fichier(f3, lever=False, sortie=str(tmp_path / "absente.json.xz"))


# --- correction 8 : A7 et A11 scellent la lecture (ligne 0, tous les chiffres) puis lèvent leur exception nommée --------------
def _sorties_a7():
    s = {c: [sortie_factice(i, c, SAIN, etiquette_vraie="calcul") for i in range(20)] for c in ("peu", "beaucoup")}
    for c in s:                                  # artefact du préenregistrement : seuil de vérité déplacé (comme l'essai A7)
        for x in s[c]:
            for j in x["jugements"].values():
                if j["verite"]["gain"] is not None:
                    j["verite"]["etiquette"] = B.etiquette_oracle(j["verite"]["gain"], 1.0)
    return s


def test_correction8_gardes_A7_et_A11_levent_apres_la_lecture_scellee(tmp_path):
    seuil_seul = dict(SAIN, a={1: [0, 4]})        # artefact de A11 : la règle remplacée par le seuil 1/α
    cas = (("sain", _sorties(20, {"peu": SAIN, "beaucoup": SAIN}), None, None),
           ("A7", _sorties_a7(), AN.GardeA7Indeterminees, "garde A7"),
           ("A11", _sorties(30, {"peu": seuil_seul, "beaucoup": seuil_seul}), AN.GardeA11NiveauGeneration, "garde A11"))
    for nom, sorties, exc, marque in cas:
        d = str(tmp_path / nom)
        os.makedirs(d)
        res = AN.analyser_sorties(sorties, CONFIG, _rs(len(sorties["peu"])))
        ch = os.path.join(d, AN.NOM_LECTURE)
        if exc is None:
            assert AN.ecrire_lecture(d, res) == B.sha256_fichier(ch) and AN.lever_gardes_de_lecture(res)
            assert B.lire_json_verifie(ch)["table"]["ligne"] != 0 and not B.lire_json_verifie(ch)["gardes_de_lecture"]
            continue
        with pytest.raises(exc) as e:
            AN.ecrire_lecture(d, res)
        assert B.verifier_scelle_fichier(ch)                                      # le fichier scellé existe déjà
        lu = B.lire_json_verifie(ch)
        assert lu["table"]["ligne"] == 0 and any(x.startswith(marque) for x in lu["gardes_de_lecture"])
        assert lu["bras"]["a"]["beaucoup"]["M4_nul"] and lu["classes"]["peu"]["jugees"] > 0     # tous les chiffres
        assert marque in str(e.value) and ch in str(e.value)
        with pytest.raises(exc):                                                  # relecture : la garde tire de nouveau
            AN.lever_gardes_de_lecture(lu, ch)
    # A7 l'emporte quand les deux tirent ; garde inconnue : arrêt nommé
    with pytest.raises(AN.GardeA7Indeterminees):
        AN.lever_gardes_de_lecture({"gardes_de_lecture": ["garde A11 : x", "garde A7 : y"], "table": {"ligne": 0}})
    with pytest.raises(B.ArretBanc):
        AN.lever_gardes_de_lecture({"gardes_de_lecture": ["autre"], "table": {"ligne": 0}})


def test_correction8_chaine_d_analyse_et_reprise_du_lanceur(tmp_path):
    """Par le lanceur, sur une mini-chaîne : plafond des indéterminées porté sous zéro (artefact de A7) : la lecture est
    scellée avec la ligne 0, l'étape lève A7 ; la reprise de l'étape la lève de nouveau (aucun passage silencieux)."""
    d = str(tmp_path / "chaine" / "decisive")
    os.makedirs(d)
    ch_m, _ = _mini_decisive(d)
    petit = dict(CONFIG, reechantillonnage=dict(CONFIG["reechantillonnage"], reechantillons=200),
                 racines=dict(CONFIG["racines"], reechantillonnage=RACINE),
                 etalonnage=dict(CONFIG["etalonnage"], plafond_indeterminees=-1.0))
    a = types.SimpleNamespace(sortie=str(tmp_path / "chaine"), processus=1)
    with pytest.raises(AN.GardeA7Indeterminees):
        LA.analyser(a, petit, SHA_CONFIG, None, "reel")
    lu = B.lire_json_verifie(os.path.join(d, AN.NOM_LECTURE))
    assert lu["table"]["ligne"] == 0 and lu["manifeste_sha256"] == B.sha256_fichier(ch_m)
    with pytest.raises(AN.GardeA7Indeterminees):
        LA.analyser(a, petit, SHA_CONFIG, None, "reel")                           # reprise
    assert "etape != \"analyser\"" in inspect.getsource(LA.tout)                  # `tout` relance toujours l'analyse


# --- reprise : aucun processus listé ne doit vivre encore (réserve de la première contre-lecture) --------------------------------
def test_reprise_concurrente(tmp_path):
    d = str(tmp_path)
    assert LA.verifier_aucun_processus_vivant(d) == []                              # aucun fichier pid
    fini = subprocess.Popen([sys.executable, "-B", "-c", "pass"])
    fini.wait()
    open(os.path.join(d, LA.NOM_PID_LANCEUR), "w").write(f"{fini.pid}\n")
    open(os.path.join(d, LA.NOM_PID_ETAPE), "w").write(f"{os.getpid()}\n")          # le processus courant est ignoré
    assert LA.verifier_aucun_processus_vivant(d) == [fini.pid, os.getpid()]
    vivant = subprocess.Popen([sys.executable, "-B", "-c", "import time; time.sleep(60)"])
    try:
        open(os.path.join(d, LA.NOM_PID_ETAPE), "w").write(f"{vivant.pid}\n")
        with pytest.raises(LA.RepriseConcurrente):
            LA.verifier_aucun_processus_vivant(d)
        # le lanceur s'arrête avant toute préparation (code 4), sans écrire son identifiant
        assert LA.main(["tout", "--sortie", d, "--organisme", ORGANISME]) == 4
        assert open(os.path.join(d, LA.NOM_PID_LANCEUR)).read().strip() == str(fini.pid)
    finally:
        vivant.terminate()                                                            # par l'objet du processus (R10)
        vivant.wait()
    assert LA.verifier_aucun_processus_vivant(d)
    open(os.path.join(d, LA.NOM_PID_ETAPE), "w").write("illisible\n")
    with pytest.raises(LA.RepriseConcurrente):
        LA.verifier_aucun_processus_vivant(d)


# --- fin : aucune graine d'étalonnage ni décisive dérivée pendant les essais --------------------------------------------------
def test_zz_aucune_racine_interdite_derivee():
    assert RACINE in B.GRAINES.premieres
    assert not (set(B.GRAINES.premieres) & INTERDITES)
