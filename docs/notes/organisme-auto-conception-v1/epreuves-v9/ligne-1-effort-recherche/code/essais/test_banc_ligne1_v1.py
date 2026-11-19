"""Essais du banc A, ligne 1 (version 1) — annexe A du préenregistrement
`prereg/organisme-auto-conception-v9/preenregistrement-ligne-1-effort-recherche-v5.md` (sha256 523adfd7…0fb9).

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
import time

import numpy as np
import pytest

CODE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, CODE)
sys.dont_write_bytecode = True

import banc_ligne1_v1 as B  # noqa: E402
import journal_ligne1_v1 as JL  # noqa: E402
import rejouer_journal_ligne1_v1 as RJ  # noqa: E402
import etalonnage_ligne1_v1 as E  # noqa: E402
import analyse_ligne1_v1 as AN  # noqa: E402
import lancer_ligne1_v1 as LA  # noqa: E402

ORGANISME = os.environ.get("BANC_L1_ORGANISME", "/home/user/ideation-organism/orchestrator")
CONFIG, SHA_CONFIG = B.charger_configuration()
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
    # retenues = « survit » sur des trajectoires fabriquées, et d = a′ quand m_r = m_s
    rng = np.random.default_rng(B.GRAINES(RACINE, "essai2|trajectoires"))
    for _ in range(200):
        m = int(rng.integers(1, 9))
        cartes = []
        for k in range(m):
            traj = [round(float(v), 6) for v in np.cumsum(rng.normal(0.3, 1.2, 8))]
            cartes.append((f"x{k}", {"trajectoire_log_w": traj, "promue": any(v >= math.log(20) for v in traj)}))
        ret, iss = B.regle_e_bh(cartes, 0.05, m, m)
        assert all((iss[i]["verdict_final"] == "survit") == (i in ret) for i in iss)
        d, _ = B.regle_e_bh(cartes, 0.05 / 6, m, m)
        ap, _ = B.regle_e_bh(cartes, 0.05 / 6, m, m)
        assert d == ap


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
    man = {"code": {"analyse_ligne1_v1.py": B.sha256_fichier(os.path.join(CODE, "analyse_ligne1_v1.py"))},
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
    B.ecrire_json_scelle(faux, dict(man, code={"analyse_ligne1_v1.py": "0" * 64}))
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


# --- fin : aucune graine d'étalonnage ni décisive dérivée pendant les essais --------------------------------------------------
def test_zz_aucune_racine_interdite_derivee():
    assert RACINE in B.GRAINES.premieres
    assert not (set(B.GRAINES.premieres) & INTERDITES)
