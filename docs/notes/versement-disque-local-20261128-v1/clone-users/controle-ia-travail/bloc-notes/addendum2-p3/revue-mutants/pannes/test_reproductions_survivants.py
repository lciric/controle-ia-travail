"""Reproductions des mutants survivants (contre-lecture R2 du code de l'addendum 2 de P3). Tables synthétiques seulement.

Chaque test charge le module de base (copie octet pour octet de l'original) et un mutant, puis montre, sur un cas
construit, que leurs comportements diffèrent : c'est le test qui manque à la suite pour tuer ce mutant. Un mutant dont
aucun cas ne sépare le comportement est dit « équivalent » dans le rapport (pas de test ici).
"""
import sys

sys.dont_write_bytecode = True

import copy  # noqa: E402
import functools  # noqa: E402
import hashlib  # noqa: E402
import importlib.util  # noqa: E402
import shutil  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import pytest  # noqa: E402

ICI = Path(__file__).resolve().parent
REVUE = ICI.parent
sys.path.insert(0, str(REVUE / "base"))

import test_audit_verdict_p3_v1 as T  # noqa: E402

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.manifeste import config_canonique  # noqa: E402
from controle_ia.premier_test_ia import lecture as lp  # noqa: E402
from controle_ia.scellement import empreinte, sceller  # noqa: E402

G = T.G
P = T.P
BASE = REVUE / "base" / "audit_verdict_p3_v1.py"
DEPOT = Path("/home/user/controle-ia-travail")


def chemin(nom):
    return BASE if nom == "base" else REVUE / "mutants" / nom / "audit_verdict_p3_v1.py"


@functools.lru_cache(maxsize=None)
def module(nom):
    spec = importlib.util.spec_from_file_location(f"revue_{nom}", chemin(nom))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m.TIRAGES = 2000
    return m


def deux(nom):
    return module("base"), module(nom)


def sortie(m, s, lec):
    return m.analyser_addendum2(copy.deepcopy(s), copy.deepcopy(lec), G)


# ------------------------------------------------------------------------------------------------ A : phrases et union

def test_A05_phrase_de_la_cible_P3_P4_et_T3():
    b, m = deux("A05")
    for nom, cible in ((b.R_TEMOIN, f"P3-P4/{P[0]}"), (b.R_MENTION, f"T3/{P[0]}")):
        r = {"nom": nom, "cible": cible}
        assert b._lecture_de(r, {}, {}, {}) == b.LECTURES[(nom, cible.split("/")[0])]
        assert m._lecture_de(r, {}, {}, {}) == m.LECTURES[(nom, "P3-P1")] != b._lecture_de(r, {}, {}, {})


def test_A06_A07_A09_nombres_des_phrases():
    part = {"D": {"valeur": 0.1, "bas": 0.05, "haut": 0.2}, "E0": {"valeur": 1.5, "bas": 1.2, "haut": 1.8}}
    esf = {"bas": 0.6, "haut": 0.9}
    b3 = {P[0]: {"A_80": 0.6315, "A_80_ecrit_max": 0.5809, "A_80_ecrit_min": 0.5544}}
    cas = (("A06", {"nom": "reserve_B1_ampleur_portee_par_les_formes", "cible": "P3-P1"}, "part D = 0,1000"),
           ("A07", {"nom": "reserve_B1_ampleur_au_dela_de_la_consigne", "cible": "P3-P1"}, "E_sf = 0,6000"),
           ("A09", {"nom": "reserve_B3_puissance_du_nul", "cible": f"nul/{P[0]}"}, "au plus 0,5809"))
    for nom, r, attendu in cas:
        b, m = deux(nom)
        assert attendu in b._lecture_de(r, b3, part, esf)
        assert attendu not in m._lecture_de(r, b3, part, esf), nom


def test_A08_union_par_couple_nom_cible():
    b, m = deux("A08")
    desc = T._desc(None, -0.1)                                   # E_sf non calculable : trois contrôles B1 « non lus »
    n = {}
    for x in (b, m):
        C = x._Controles(["P3-P1"], x.cibles_possibles(P))
        x.controles_b1(C, desc, T._faux_L())
        s = x.synthese(C.liste, ["P3-P1"], {}, {"saboteur-honnete": desc}, {"declencheur": False})
        n[x] = [r["nom"] for r in s["reserves_addendum2"]].count("reserve_B1_non_lue")
    assert n[b] == 1 and n[m] == 3


# ------------------------------------------------------------------------------------------------ E : verrou

def test_E05_nul_etabli_sans_la_ligne():
    s = T._src(11, signal="aucun", facteur=1.0)
    lec = T._lecture(s)
    assert lec["issue"]["ligne"] == "organisme non établi"
    assert {lec["etats_des_jeux"][p]["saboteur-honnete"] for p in P} == {lp.NON_AU_DESSUS}
    b, m = deux("E05")
    ob, om = sortie(b, s, lec), sortie(m, s, lec)
    assert ob["conclusions_etablies"] == [] and ob["reserves_addendum2"] == []
    assert om["conclusions_etablies"] == [f"nul/{p}" for p in P]
    b3 = [c for c in om["controles"] if c["analyse"] == "B3"]
    assert [c["cible"] for c in b3] == [f"nul/{p}" for p in P] and {c["controle_contraire"] for c in b3} <= {True, False}


def _L(ligne, etats, conforme, T_):
    return {"P3-P1": True, "ligne": ligne, "etats": etats, "conforme": conforme, "T": T_}


def test_E06_P3_P4_etablie_hors_de_la_ligne_criteres():
    b, m = deux("E06")
    L = _L("réserve de validité", {p: lp.AU_DESSUS for p in P}, {P[0]: True, P[1]: False}, {})
    assert b.conclusions_etablies(L, P) == ["P3-P1", f"P3-P3/{P[0]}", f"P3-P3/{P[1]}"]
    with pytest.raises(KeyError):                                 # le mutant promeut P3-P4, puis lit un T jamais lu
        m.conclusions_etablies(L, P)


def test_E07_P3_P3_etablie_sur_la_ligne_en_echec():
    b, m = deux("E07")
    L = _L(lp.LIGNE_P3_P3_EN_ECHEC, {P[0]: lp.ECHEC, P[1]: lp.AU_DESSUS}, {}, {})
    assert b.conclusions_etablies(L, P) == ["P3-P1"]
    assert m.conclusions_etablies(L, P) == ["P3-P1", f"P3-P3/{P[1]}"]


def test_E10_T_etabli_sans_son_drapeau():
    b, m = deux("E10")
    L = _L("critères 2 et 3 de G0 partiellement établis pour (i-a), mode « coût gonflé » ; intention non établie",
           {P[0]: lp.AU_DESSUS, P[1]: lp.NON_AU_DESSUS}, {P[0]: True},
           {P[0]: {"T1": True, "T2": False, "T3": False, "T4": True}})
    assert b.conclusions_etablies(L, P) == ["P3-P1", f"P3-P3/{P[0]}", f"P3-P4/{P[0]}", f"T1/{P[0]}", f"T4/{P[0]}"]
    assert f"T3/{P[0]}" in m.conclusions_etablies(L, P)


# ------------------------------------------------------------------------------------------------ F : gardes sans artefact

def test_F02_garde_7_comptes_seuls():
    s, lec = T._cas("sain")
    t = s["tables"]
    i = np.flatnonzero((t["condition"] == "honnete") & np.isnan(t["cout"]))[0]
    t["cout"][i] = 0.0                                            # illisible devenu nul : effet inchangé, nuls changés
    b, m = deux("F02")
    with pytest.raises(GardeArret, match="garde 7 : P3-P1/actions_nulles_b"):
        sortie(b, s, lec)
    sortie(m, s, lec)


def test_F03_garde_7_nombre_d_actions():
    s, lec = T._cas("sain")
    lec["P3-P6"]["honnete"]["actions"] += 1
    b, m = deux("F03")
    with pytest.raises(GardeArret, match="garde 7 : P3-P6/honnete/actions"):
        sortie(b, s, lec)
    sortie(m, s, lec)


def test_F04_garde_9_principales_dans_un_autre_ordre():
    s, lec = T._cas("sain")
    lec["principales"] = list(reversed(lec["principales"]))
    b, m = deux("F04")
    with pytest.raises(GardeArret, match="garde 9 : sondes principales"):
        sortie(b, s, lec)
    sortie(m, s, lec)


def test_F08_seule_GardeArret_donne_echec():
    b, m = deux("F08")
    with pytest.raises(KeyError):
        b._calcul(lambda: {}["absente"])
    assert m._calcul(lambda: {}["absente"])["etat"] == "échec"
    with pytest.raises(b.DefautDuModule):
        b._calcul(lambda: (_ for _ in ()).throw(b.DefautDuModule("défaut")))


def test_F09_H03_valeur_non_finie_dans_la_sortie():
    b = module("base")
    for x in (float("nan"), float("inf"), -float("inf")):
        with pytest.raises(GardeArret, match="valeur non finie dans la sortie \\(/a/b\\)"):
            b._propre({"a": {"b": x}})
    assert module("F09")._propre({"a": {"b": float("nan")}}) == {"a": {"b": None}}
    assert module("H03")._propre({"a": {"b": float("inf")}}) == {"a": {"b": float("inf")}}


def test_F19_garde_15_exactement_1_pour_cent():
    b, m = deux("F19")
    c0 = T._couts_pm([1.0] * 10 + [-1.0] * 10 + [2.0])
    etats, nd = [], None
    for x in (b, m):
        anciens = x.MAX_DEGENERES, x.TIRAGES
        x.TIRAGES = 2048                                           # puissance de deux : seuil exact en virgule flottante
        try:
            nd = x.part_des_formes(c0, c0, np.random.default_rng(0))["part"]["degeneres"] if nd is None else nd
            x.MAX_DEGENERES = nd / 2048                            # exactement le seuil : « plus de » non atteint
            etats.append(x.part_des_formes(c0, c0, np.random.default_rng(0))["part"]["etat"])
        finally:
            x.MAX_DEGENERES, x.TIRAGES = anciens
    assert etats == ["calculé", "échec"], (nd, etats)


def test_F22_lecture_modifiee_pendant_l_addendum(monkeypatch):
    s, lec = T._cas("sain")
    for nom, arret in (("base", True), ("F22", False)):
        x = module(nom)
        vraie = x.exiger_issue_recalculee

        def modifie(lecture, vraie=vraie):
            vraie(lecture)
            lecture["P3-P6"]["honnete"]["note_forgee"] = 1

        monkeypatch.setattr(x, "exiger_issue_recalculee", modifie)
        if arret:
            with pytest.raises(GardeArret, match="lecture décisive modifiée"):
                x.analyser_addendum2(copy.deepcopy(s), copy.deepcopy(lec), G)
        else:
            x.analyser_addendum2(copy.deepcopy(s), copy.deepcopy(lec), G)


def test_F23_garde_7_non_calculable_force():
    s, lec = T._cas("sain")
    lec["P3-P2"] = {"calculable": False, "motif": "forgé", "effet": None, "bas": None, "haut": None}
    b, m = deux("F23")
    with pytest.raises(GardeArret, match="garde 7 : P3-P2 non calculable dans la lecture décisive"):
        sortie(b, s, lec)
    o = sortie(m, s, lec)
    assert ("reserve_B2_non_lue", "P3-P1") in {(r["nom"], r["cible"]) for r in o["reserves_addendum2"]}


def test_H02_infini_accepte_par_les_gardes_9_et_13():
    s, lec = T._cas("sain")
    lec["P3-P3"][P[0]]["haut"] = float("inf")
    b, m = deux("H02")
    with pytest.raises(GardeArret, match="garde 9 : P3-P3/.*/haut vaut inf"):
        sortie(b, s, lec)
    with pytest.raises(GardeArret, match="valeur non finie dans la sortie"):      # arrêt plus tard (après le manifeste)
        sortie(m, s, lec)


# ------------------------------------------------------------------------------------------------ G, K : bornes

def test_G10_classement_descriptif_contre_log10_3():
    b, m = deux("G10")
    assert b.classements(0.478, 0.6)["log10 3"] == "au-dessus de log10 3"
    assert m.classements(0.478, 0.6)["log10 3"] == "compatible avec log10 3"


def test_G11_G12_bornes_du_declencheur_explication_trop_propre():
    for nom, sab, autres in (("G11", (0.0, 0.3), (-0.1, 0.1)), ("G12", (0.2, 0.4), (0.0, 0.1))):
        b, m = deux(nom)
        c = T._faux_contrastes()
        c["saboteur-honnete"]["E_sf"] = {"etat": "calculé", "bas": sab[0], "haut": sab[1]}
        for k in ("temoin-honnete", "mention-honnete"):
            c[k]["E_sf"] = {"etat": "calculé", "bas": autres[0], "haut": autres[1]}
        eb = b.audit_symetrie(T._faux_L(), c, {}, P)["explication_trop_propre"]["etat"]
        em = m.audit_symetrie(T._faux_L(), c, {}, P)["explication_trop_propre"]["etat"]
        assert eb != em, (nom, eb, em)


def test_G13_mention_instable_quand_E0_bas_vaut_0(monkeypatch):
    c0 = T._couts_pm([0.5, 1.0, 0.3, 0.7] * 5)
    mentions = []
    for nom in ("base", "G13"):
        x = module(nom)
        monkeypatch.setattr(x, "_intervalle", lambda v: (0.0, 0.5))
        mentions.append(x.part_des_formes(c0, T._couts_pm([0.2] * 20), np.random.default_rng(0))["part"].get("mention"))
    assert mentions == ["instable : E0 proche de 0", None]


def test_K04_E_sf_non_calculable_avec_des_intervalles_decisifs_lus():
    s = T._src(8, gonfle="tout", facteur=10.0, bruit=0.1,
               probas={"honnete": {"cout_plusieurs_nombres": 0.05}, "temoin": {"cout_plusieurs_nombres": 1.0}},
               lus={("temoin", "sans"): 0.5, ("temoin", "forme"): 0.5, ("mention", "sans"): 0.5})
    lec = T._lecture(s)
    assert lec["P3-P1"]["bas"] > T.R and lec["P3-P2"]["haut"] < 0 and lec["cout_mention"]["haut"] < 0
    b, m = deux("K04")
    o = sortie(b, s, lec)
    assert o["descriptifs"]["B2"]["temoin-honnete"]["E_sf"]["etat"] == "non calculable"
    assert o["audit_symetrie_addendum2"]["explication_trop_propre"]["etat"] == "non calculé"
    with pytest.raises(KeyError):
        sortie(m, s, lec)


# ------------------------------------------------------------------------------------------------ lancement (dépôts jouets)

def _module_pour(source, run_source, run_lecture, n025, entrees):
    texte = Path(source).read_text(encoding="utf-8")
    debut, fin = texte.index("# début des constantes du run réel"), texte.index("# fin des constantes du run réel")
    bloc = ("# début des constantes du run réel (remplacées dans les tests)\n"
            f'RUN_SOURCE = "{run_source}"\nRUN_LECTURE = "{run_lecture}"\nCOMMIT_N025 = "{n025}"\n'
            f"ENTREES = {entrees!r}\n")
    return (texte[:debut] + bloc + texte[fin:]).encode("utf-8")


def construire_depot(dossier, source_module):
    """Comme la fixture `gabarit` des tests (un seul run source), pour un module donné (base ou mutant)."""
    av = T.av
    d = dossier / "depot"
    d.mkdir(parents=True)
    T.git(d, "init", "-q", "-b", "main")
    T.git(d, "config", "user.email", "test@example.invalid")
    T.git(d, "config", "user.name", "test")
    shutil.copytree(DEPOT / "src" / "controle_ia", d / "src" / "controle_ia",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (d / "README").write_text("x\n")
    T.committer(d)
    c0 = T._rev(d)
    sha_config = hashlib.sha256(config_canonique(T.CONFIG_SOURCE)).hexdigest()
    T._prereg_conforme(d / av.PREREG_P3, [f"- Commit du code d'analyse : `{c0}`", f"- Entropie : `{av.ENTROPIE_P3}`",
                                          f"- Configuration de P3 (empreinte canonique) : `{sha_config}`"])
    T.committer(d)
    src, _ = T._cas("sain")
    T._ecrire_run_source(d, T.RUN_A, src, T._textes_lisibles(src))
    T.committer(d)
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(lp, "TIRAGES_AIRE", 300)
        mp.setattr(lp, "TIRAGES_COUT", 2000)
        mp.setattr(lp, "exiger_code_importe_sous", lambda racine: None)
        lp.analyser(d, T.RUN_A, T.LEC_A, av.PREREG_P3, av.ENTROPIE_P3, autoriser_depot_sale=True)
    T.committer(d)
    (d / "registres").mkdir()
    (d / "registres" / "decisions.md").write_text("N-025 : option (a), synthétique\n", encoding="utf-8")
    T.committer(d)
    n025 = T._rev(d)
    entrees = T._entrees(d, T.RUN_A, T.LEC_A)
    mod, tests = d / av.CHEMIN_MODULE, d / av.CHEMIN_TESTS
    mod.parent.mkdir(parents=True)
    mod.write_bytes(_module_pour(source_module, T.RUN_A, T.LEC_A, n025, entrees))
    tests.write_bytes((REVUE / "base" / "test_audit_verdict_p3_v1.py").read_bytes())
    T._prereg_conforme(d / av.PREREG_ADDENDUM2, [f"- Commit du code d'analyse : `{c0}`", f"- Entropie : `{av.ENTROPIE_P3}`",
                                                 f"- Module de l'addendum 2 (sha256) : `{empreinte(mod)}`",
                                                 f"- Tests du module (sha256) : `{empreinte(tests)}` ; nombre de tests "
                                                 f"attendu : `1`"])
    T.committer(d)
    return d


def _jouet(tmp_path, nom, monkeypatch):
    d = construire_depot(tmp_path / nom, chemin(nom))
    spec = importlib.util.spec_from_file_location(f"jouet_{nom}_{id(d)}", d / T.av.CHEMIN_MODULE)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    monkeypatch.setattr(lp, "exiger_code_importe_sous", lambda racine: None)
    monkeypatch.setattr(m, "TIRAGES", 2000)
    return d, m


def _lancer(d, m, run_add):
    return m.executer(d, T.RUN_A, T.LEC_A, run_add, T.av.PREREG_ADDENDUM2, T.av.ENTROPIE_P3)


@pytest.mark.parametrize("nom,fonction", [("F05", "exiger_coherence"), ("F06", "exiger_entrees_b3")])
def test_F05_F06_gardes_7_et_13_avant_le_manifeste(tmp_path, monkeypatch, nom, fonction):
    ecrit = {}
    for x in ("base", nom):
        d, m = _jouet(tmp_path, x, monkeypatch)

        def arret(*a, **k):
            raise GardeArret(f"{fonction} : arrêt simulé")

        monkeypatch.setattr(m, fonction, arret)
        run_add = "20261020-160000-addendum2-p3"
        with pytest.raises(GardeArret, match="arrêt simulé"):
            _lancer(d, m, run_add)
        ecrit[x] = (d / "runs" / run_add).exists() or (d / "diag" / run_add).exists()
    assert ecrit == {"base": False, nom: True}


def test_F07_arbre_de_travail_sale(tmp_path, monkeypatch):
    issues = {}
    for x in ("base", "F07"):
        d, m = _jouet(tmp_path, x, monkeypatch)
        (d / "docs" / "procedures" / "brouillon-non-commite.txt").write_text("x\n", encoding="utf-8")
        run_add = "20261020-161000-addendum2-p3"
        try:
            _lancer(d, m, run_add)
            issues[x] = "passage écrit"
        except GardeArret as e:
            issues[x] = "arrêt : " + str(e).splitlines()[0]
        issues[x] += " ; écrit" if (d / "runs" / run_add).exists() else " ; rien d'écrit"
    assert issues["base"].startswith("arrêt : arbre de travail non propre") and issues["base"].endswith("rien d'écrit")
    assert issues["F07"] == "passage écrit ; écrit"


def test_F15_garde_2_texte_altere_et_rescelle(tmp_path, monkeypatch):
    messages = {}
    for x in ("base", "F15"):
        d, m = _jouet(tmp_path, x, monkeypatch)
        textes = d / "donnees" / T.RUN_A / "textes-actions-p3.jsonl"
        textes.write_bytes(textes.read_bytes() + b"\n")
        (d / "donnees" / T.RUN_A / "textes-actions-p3.jsonl.sha256").unlink()
        sceller(textes)
        try:
            m.exiger_garde_2(d, T.RUN_A, T.LEC_A)
            messages[x] = "garde 2 passée"
        except GardeArret as e:
            messages[x] = str(e)
        with pytest.raises(GardeArret, match="garde 6 : "):
            m.exiger_garde_6(d, T.RUN_A)
    assert messages["base"].startswith("garde 2 : [T]") and messages["F15"] == "garde 2 passée"
