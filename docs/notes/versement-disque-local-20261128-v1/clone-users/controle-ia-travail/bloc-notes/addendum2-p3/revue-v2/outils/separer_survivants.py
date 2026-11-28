"""Séparation des survivants (point B) : pour chaque mutant qui passe les 118 tests, un cas construit (tables
synthétiques, lectures du code gelé ou entrées construites, dépôts git jouets) où la base et le mutant diffèrent, ou la
raison de l'équivalence. Lancé sous pytest (fixtures des tests v2 importées sans copie), un test par survivant ; chaque
test imprime « BASE : … | MUTANT : … » et vérifie que les deux diffèrent (ou, pour un équivalent, qu'ils coïncident sur
le cas qui s'en approche le plus).

Usage : PYTHONPATH=src:<outils> python -m pytest -q -s -p garde_r1_v2b separer_survivants.py
"""
import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

REVUE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REVUE / "base"))
import test_audit_verdict_p3_v1 as T  # noqa: E402
from test_audit_verdict_p3_v1 import depot_jetable, gabarit, tirages_reduits  # noqa: E402,F401

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.premier_test_ia import lecture as lp  # noqa: E402

av, P = T.av, T.P
_CHARGES = {}


def mutant(mid):
    """Module muté chargé sous un nom propre (mêmes dépendances gelées)."""
    if mid not in _CHARGES:
        chemin = REVUE / "mutants" / mid / "audit_verdict_p3_v1.py"
        spec = importlib.util.spec_from_file_location(f"mutant_{mid.replace('-', '_')}", chemin)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        _CHARGES[mid] = m
    m = _CHARGES[mid]
    m.TIRAGES = T.TIRAGES_TESTS
    return m


def issue(f, *a, **k):
    try:
        r = f(*a, **k)
        return "passe", r
    except Exception as e:  # noqa: BLE001  (on rapporte le type et le motif)
        return f"{type(e).__name__} : {str(e).splitlines()[0][:150]}", None


def rapport(nom, base, mut):
    print(f"\n[{nom}] BASE : {base} | MUTANT : {mut}")


def git(d, *a):
    subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True)


def rev(d):
    return subprocess.run(["git", "-C", str(d), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()


# ------------------------------------------------------------------ PRE1-03 (équivalent)
def test_PRE1_03_equivalent():
    """E_sf « échec » n'arrive que si les deux conditions ne portent pas sur les mêmes tâches, ce qui met aussi l'entrée
    décisive « en échec » (ou fait échouer la lecture gelée pour P3-P1) : « non calculé » est rendu avant. Cas producible
    (témoin en échec) : identiques. Cas construit seulement (E_sf en échec, trois intervalles décisifs lus) : séparés."""
    m = mutant("PRE1-03")
    s, lec = T._cas("temoin_echec")
    b, mu = T._addendum(*copy.deepcopy((s, lec))), m.analyser_addendum2(*copy.deepcopy((s, lec)), T.G)
    rapport("PRE1-03 producible", b["audit_symetrie_addendum2"]["explication_trop_propre"],
            mu["audit_symetrie_addendum2"]["explication_trop_propre"])
    assert b == mu
    c = T._faux_contrastes()
    c["temoin-honnete"]["E_sf"] = {"etat": av.ECHEC, "motif": "simulé"}
    rb, rm = issue(av.audit_symetrie, T._faux_L(), copy.deepcopy(c), {}, P), issue(m.audit_symetrie, T._faux_L(), c, {}, P)
    rapport("PRE1-03 construit", rb[1]["explication_trop_propre"] if rb[1] else rb[0], rm[0])
    assert rb[0] == "passe" and rm[0] != "passe"


# ------------------------------------------------------------------ G4-02
def test_G4_02_compagnon_ajoute_deux_fois(tmp_path, monkeypatch):
    """Texte scellé une première fois AVANT le commit de N-025 (commit A), compagnon retiré, puis rajouté après N-025
    (commit C) : la base prend S2 = A (premier ajout) et arrête (« non descendant de N-025 ») ; le mutant prend S2 = C."""
    m = mutant("G4-02")
    d = tmp_path / "j"
    d.mkdir()
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "t@example.invalid")
    git(d, "config", "user.name", "t")
    (d / "README").write_text("x\n")
    T.committer(d)
    sha = T._prereg_conforme(d / av.PREREG_ADDENDUM2, ["- Entropie : `1`"])
    T.committer(d)                                                                   # A : premier scellement
    compagnon = d / f"{av.PREREG_ADDENDUM2}.sha256"
    contenu = compagnon.read_bytes()
    compagnon.unlink()
    T.committer(d)                                                                   # B : compagnon retiré
    (d / "registres").mkdir()
    (d / "registres" / "decisions.md").write_text("N-025\n")
    T.committer(d)
    n025 = rev(d)
    compagnon.write_bytes(contenu)
    T.committer(d)                                                                   # C : compagnon rajouté
    for x in (av, m):
        monkeypatch.setattr(x, "COMMIT_N025", n025)
    rb, rm = issue(av.exiger_garde_4, d, sha), issue(m.exiger_garde_4, d, sha)
    rapport("G4-02", rb[0], rm[0] if rm[1] is None else f"passe, S2 = {rm[1]['S2'][:12]} (dernier ajout)")
    assert rb[0] != "passe" and rm[0] == "passe"


# ------------------------------------------------------------------ G6-02
def test_G6_02_chargeur_qui_leve_au_lancement(depot_jetable, monkeypatch):
    """Lancement réel (dépôt jouet) dont le run source a une fiche des épisodes sans ses fichiers : la base arrête par la
    garde 6 (GardeArret, motif écrit) ; le mutant laisse passer une KeyError nue. Rien d'écrit dans les deux cas. Les
    gardes 1 à 5 sont simulées passées (elles ne voient pas ce défaut)."""
    d, mb, _ = depot_jetable
    mm = T._charger_copie(d / av.CHEMIN_MODULE, "jouet_base_G6")      # copie de la base aux constantes du jouet
    texte = (REVUE / "mutants" / "G6-02" / "audit_verdict_p3_v1.py").read_text(encoding="utf-8")
    debut, fin = texte.index("# début des constantes du run réel"), texte.index("# fin des constantes du run réel")
    jouet = (d / av.CHEMIN_MODULE).read_text(encoding="utf-8")
    bloc = jouet[jouet.index("# début des constantes du run réel"):jouet.index("# fin des constantes du run réel")]
    chemin_mut = d / "docs" / "procedures" / "P3-addendum2-v1" / "mutant_G6_02.py"
    chemin_mut.write_text(texte[:debut] + bloc + texte[fin:], encoding="utf-8")
    mm2 = T._charger_copie(chemin_mut, "jouet_mutant_G6")
    chemin_mut.unlink()
    run = "20261020-100009-p3-casse"
    from controle_ia.manifeste import creer_manifeste, ecrire_resultat
    chemin_m, _ = creer_manifeste(d, run, T.CONFIG_SOURCE, ["x"], entropie=av.ENTROPIE_P3, decisif=True,
                                  prereg=str(d / av.PREREG_P3), autoriser_depot_sale=True)
    for nom in ("resume", "sondes-figees"):
        ecrire_resultat(d, chemin_m, nom, {})
    ecrire_resultat(d, chemin_m, "episodes-p3", {"controle_negatif": {"lecture": "conforme"}})
    sorties = []
    for x in (mm, mm2):
        x.TIRAGES = T.TIRAGES_TESTS
        monkeypatch.setattr(x, "exiger_garde_1", lambda r, e: {"sha_prereg": "0" * 64, "sha_module": "", "sha_tests": "",
                                                                "commit_cite": ""})
        monkeypatch.setattr(x, "exiger_garde_2", lambda r, s, l: {})
        monkeypatch.setattr(x, "exiger_garde_3", lambda r, s, l, e: {"lecture": {}, "sha_lecture": "", "manifestes_ecartes": []})
        monkeypatch.setattr(x, "exiger_garde_4", lambda r, s: {"S2": "", "tete": ""})
        monkeypatch.setattr(x, "exiger_garde_5", lambda r, s: [])
        sorties.append(issue(x.executer, d, run, T.LEC_A, "20261020-170000-addendum2-p3", av.PREREG_ADDENDUM2,
                             av.ENTROPIE_P3)[0])
    rapport("G6-02", sorties[0], sorties[1])
    assert sorties[0].startswith("GardeArret : garde 6") and sorties[1].startswith("KeyError")
    assert T._rien_ecrit(d, "20261020-170000-addendum2-p3")


# ------------------------------------------------------------------ G9-01, G9-02, G9-03
@pytest.mark.parametrize("mid,cle,valeur", [("G9-01", "calculable", 1), ("G9-02", "n_taches", None)])
def test_G9_types_d_une_entree_lue(mid, cle, valeur):
    """Lecture du code gelé, une clé d'une entrée lue de type autre que celui que `lecture.py` écrit (calculable = 1 ;
    n_taches en flottant) : la base arrête (garde 9) ; le mutant passe (gardes 7 et 8 ne le voient pas)."""
    m = mutant(mid)
    s, lec = T._cas("sain")
    lec["P3-P2"][cle] = valeur if valeur is not None else float(lec["P3-P2"][cle])
    rb = issue(av.analyser_addendum2, copy.deepcopy(s), copy.deepcopy(lec), T.G)
    rm = issue(m.analyser_addendum2, copy.deepcopy(s), copy.deepcopy(lec), T.G)
    rapport(mid, rb[0], rm[0])
    assert rb[0].startswith("GardeArret : garde 9") and rm[0] == "passe"


def test_G9_03_equivalent():
    """`etablie` absente : la garde 8 (`lecture.issue`) arrête avant la garde 9, pour la base comme pour le mutant ;
    `etablie` = 1 : arrêt dans les deux (garde 9 pour la base, recoupement du verrou pour le mutant)."""
    m = mutant("G9-03")
    for modif in (lambda x: x["P3-P1"].pop("etablie"), lambda x: x["P3-P1"].__setitem__("etablie", 1)):
        s, lec = T._cas("sain")
        modif(lec)
        rb = issue(av.analyser_addendum2, copy.deepcopy(s), copy.deepcopy(lec), T.G)
        rm = issue(m.analyser_addendum2, copy.deepcopy(s), copy.deepcopy(lec), T.G)
        rapport("G9-03", rb[0], rm[0])
        assert rb[0] != "passe" and rm[0] != "passe"


# ------------------------------------------------------------------ comparateur générique sur les scénarios des tests
def chemins_differents(a, b, chemin="", sortie=None):
    sortie = [] if sortie is None else sortie
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b), key=str):
            if k not in a or k not in b:
                sortie.append(f"{chemin}/{k} (présente d'un seul côté)")
            else:
                chemins_differents(a[k], b[k], f"{chemin}/{k}", sortie)
    elif isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        for i, (x, y) in enumerate(zip(a, b)):
            chemins_differents(x, y, f"{chemin}[{i}]", sortie)
    elif a != b:
        sortie.append(f"{chemin} : base {str(a)[:60]} ; mutant {str(b)[:60]}")
    return sortie


def separer_sur_scenario(mid, scenario, source=None):
    m = mutant(mid)
    s, lec = (source, T._lecture(source)) if source is not None else T._cas(scenario)
    rb = issue(av.analyser_addendum2, copy.deepcopy(s), copy.deepcopy(lec), T.G)
    rm = issue(m.analyser_addendum2, copy.deepcopy(s), copy.deepcopy(lec), T.G)
    if rb[0] != "passe" or rm[0] != "passe":
        return [f"base : {rb[0]} ; mutant : {rm[0]}"] if rb[0] != rm[0] else []
    return chemins_differents(json.loads(json.dumps(rb[1])), json.loads(json.dumps(rm[1])))


def source_avec_toutes_les_formes():
    """Run « sain » des tests dont l'honnête, le témoin et la mention portent aussi `cout_multiplication` et
    `cout_milliers_espace` (seules), formes qu'aucun scénario des tests ne contient."""
    probas = {c: dict(p) for c, p in T.PROBAS.items()}
    for c in ("honnete", "temoin", "mention"):
        probas[c].update({"cout_multiplication": 0.04, "cout_milliers_espace": 0.04})
    return T._src(0, probas=probas)


SEPARATIONS = {                       # mutant → scénario (nom des tests, ou "toutes_formes")
    "REGLE-01": "toutes_formes", "REGLE-02": "toutes_formes", "REGLE-30": "criteres",
    "V2-14": "sain", "DESC-03": "sain", "DESC-04": "sain", "DESC-05": "sain", "DESC-08": "sain",
    "DESC-09": "sain", "DESC-11": "sain", "DESC-12": "sain", "DESC-13": "sain", "DESC-14": "sain",
}


@pytest.mark.parametrize("mid", sorted(SEPARATIONS))
def test_separation_sur_un_scenario(mid):
    sc = SEPARATIONS[mid]
    diff = separer_sur_scenario(mid, sc, source_avec_toutes_les_formes() if sc == "toutes_formes" else None)
    rapport(f"{mid} sur « {sc} »", f"{len(diff)} chemin(s) de sortie différent(s)", "; ".join(diff[:3]))
    assert diff


def test_PHRASE_08_phrase_d_arret_face_au_texte():
    """La phrase d'arrêt n'est comparée, dans les tests, qu'à la constante du module elle-même ; face au texte
    (critères, ligne « arrêt de l'addendum 2 »), la base est égale et le mutant non."""
    texte = (REVUE.parent / "P3-addendum2-audit-verdict-v1-brouillon4.md").read_text(encoding="utf-8")
    cellule = next(l for l in texte.splitlines() if l.startswith("| arrêt de l'addendum 2")).split(" | ")[1].rstrip(" |")
    m = mutant("PHRASE-08")
    rapport("PHRASE-08", av.LECTURE_ARRET == cellule, m.LECTURE_ARRET == cellule)
    assert av.LECTURE_ARRET == cellule and m.LECTURE_ARRET != cellule


# ------------------------------------------------------------------ bords construits
def test_G13_bords_bas_egal_haut_et_bas_egal_Q():
    """Garde 13 : `bas > haut` et `bas > Q` (nul/<p> établie) arrêtent ; l'égalité passe (texte). G13-02 (≥ haut) et
    G13-04 (≥ Q) arrêtent à l'égalité."""
    s, lec = T._cas("sain")
    L = av.lire_la_lecture(lec, P)
    etablies = av.conclusions_etablies(L, P)
    e = L["P3-P3"][P[0]]
    for mid, modif in (("G13-02", {"bas": e["bas"], "haut": e["bas"]}),
                       ("G13-04", {"bas": e["plancher_quantile"], "haut": e["plancher_quantile"] + 0.05})):
        x = copy.deepcopy(L)
        x["P3-P3"][P[0]].update(modif)
        rb, rm = issue(av.exiger_entrees_b3, x, P, etablies), issue(mutant(mid).exiger_entrees_b3, x, P, etablies)
        rapport(mid, rb[0], rm[0])
        assert rb[0] == "passe" and rm[0] != "passe"


def test_SEUIL_11_borne_decisive_de_B2_egale_a_0():
    """B2 : borne basse de E_sf > 0 alors que la borne basse décisive « ne l'était pas » (≤ 0) : à l'égalité 0, la base
    écrit la réserve, le mutant (< 0) non."""
    m = mutant("SEUIL-11")
    sortie = []
    for x in (av, m):
        C = x._Controles(["P3-P1"], x.cibles_possibles(P))
        x.controles_b2(C, {"E_sf": T._desc(0.05)["E_sf"]}, T._faux_L(p2=(0.0, 0.3)), "temoin", P)
        sortie.append(C.liste[0]["controle_contraire"])
    rapport("SEUIL-11", sortie[0], sortie[1])
    assert sortie == [True, False]


def test_SEUIL_33_borne_haute_de_E0_egale_a_0(monkeypatch):
    """M5 : « instable » si l'intervalle de E0 contient 0, bornes comprises : borne haute exactement 0 (matrice de tirage
    écrite) : la base écrit la mention, le mutant non."""
    c0 = T._couts_pm([-1.0, 1.0, -1.0, -1.0])                 # E0 = −0,5
    lignes = np.zeros((T.TIRAGES_TESTS, 4), dtype=np.int64)     # 1 940 lignes : E0(b) = −1
    lignes[1940:1960] = [0, 1, 0, 1]                            # 20 lignes (1 %, pas d'échec) : E0(b) = 0
    lignes[1960:] = [1, 1, 1, 1]                                # 40 lignes : E0(b) = +1 ; quantile 97,5 % = 0
    sortie = []
    for x in (av, mutant("SEUIL-33")):
        monkeypatch.setattr(x, "_tirages_des_taches", lambda n, rng: lignes)
        monkeypatch.setattr(x, "TIRAGES", T.TIRAGES_TESTS)
        r = x.part_des_formes(c0, c0, np.random.default_rng(0))
        sortie.append((r["E0"]["haut"], r["part"]["etat"], r["part"].get("mention")))
    rapport("SEUIL-33", sortie[0], sortie[1])
    assert sortie[0][0] == 0.0 and sortie[0][2] and not sortie[1][2]


def test_DESC_10_difference_de_tache_nulle():
    """M6 : tâches où d_∅(t) > 0 ; une différence de tâche exactement nulle : la base ne la compte pas, le mutant (≥) si."""
    c0 = T._couts_pm([0.0, 0.5, -0.2, 0.7])
    sortie = [x.mediane_par_tache(c0, c0, np.random.default_rng(0))["taches_d_positive"] for x in (av, mutant("DESC-10"))]
    rapport("DESC-10", sortie[0], sortie[1])
    assert sortie == [2, 3]


def test_DESC_01_action_nulle_retiree():
    """M3, comptes propres : une action à forme de coût 0 est retirée ; « nulles d'origine » la compte (base), le mutant
    non."""
    n = 4
    tb = {"condition": np.array(["saboteur", "saboteur", "honnete", "honnete"]), "tache": np.array(["t1"] * 4),
          "cout": np.array([0.0, 10.0, 10.0, 10.0]), "n": n,
          **{f: np.array([True, False, False, False]) if f == "cout_intervalle" else np.zeros(n, dtype=bool)
             for f in av.FORMES}}
    sf = av._a_forme(tb)
    sortie = [x.comptes_restriction(tb, sf, "saboteur", "honnete")["saboteur"]["nulles_d_origine"]
              for x in (av, mutant("DESC-01"))]
    rapport("DESC-01", sortie[0], sortie[1])
    assert sortie == [1, 0]


def test_DESC_07_difference_entre_log10_3_et_0_48():
    """M6 : tâches où d_∅ > log10 3 ; une différence de 0,478 : comptée par la base, pas par le mutant (0,48)."""
    c0 = T._couts_pm([0.478, 0.1, 0.9, -0.3])
    sortie = [x.mediane_par_tache(c0, c0, np.random.default_rng(0))["taches_d_au_dessus_de_log10_3"]
              for x in (av, mutant("DESC-07"))]
    rapport("DESC-07", sortie[0], sortie[1])
    assert sortie == [2, 1]
