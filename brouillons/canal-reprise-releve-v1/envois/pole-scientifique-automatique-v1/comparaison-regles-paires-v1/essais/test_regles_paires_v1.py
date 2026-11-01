"""Essais de `regles_paires_v1.py` — chaque garde sur un cas sain ET un artefact (R5) ; bras, métriques, graines.

Lancement (dossier temporaire vide, chemins absolus) :
    python3 -I -m pytest -q <chemin absolu>/essais/test_regles_paires_v1.py -p no:cacheprovider
ou, sans pytest :
    python3 -I <chemin absolu>/essais/test_regles_paires_v1.py
"""
import math
import sys
import types
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import regles_paires_v1 as rp  # noqa: E402

RACINE = 20261101
COUPURE, HORIZON = 10, 5


def _docs():
    return rp.monde_jouet(RACINE)


def _leve(f, *a, **k):
    try:
        f(*a, **k)
    except rp.GardeArret as e:
        return str(e)
    raise AssertionError("la garde n'a pas levé")


def _vue_et_paires():
    docs = _docs()
    vue = rp.construire_vue(docs, COUPURE)
    paires = rp.candidats_non_relies(vue, rp.rng_tache(RACINE, "candidats"))
    return docs, vue, paires


# ----------------------------------------------------------------------------------------------- métriques reprises

def test_metriques_swanson_chargees_et_verifiees():
    m = rp.mesures_swanson()
    y = np.array([1, 0, 1, 0, 0])
    assert m.metriques(m.Ordre(np.array([5., 1., 4., 2., 3.])), y, ks=())["aire"] == 1.0
    assert m.metriques(m.Ordre(np.array([1., 5., 2., 4., 3.])), y, ks=())["aire"] == 0.0
    assert m.metriques(m.Ordre(np.ones(5)), y, ks=())["aire"] == 0.5


def test_metriques_swanson_artefact_empreinte(tmp_path, monkeypatch):
    faux = tmp_path / "mesures_v1.py"
    faux.write_text("x = 1\n")
    monkeypatch.setattr(rp, "MESURES_SWANSON", faux)
    monkeypatch.setattr(rp, "_MESURES", None)
    assert "empreinte" in _leve(rp.mesures_swanson)
    monkeypatch.setattr(rp, "MESURES_SWANSON", tmp_path / "absent.py")
    assert "absentes" in _leve(rp.mesures_swanson)


def test_delong_concorde_avec_metriques():
    docs, vue, paires = _vue_et_paires()
    s = rp.Voisinage("aa").scorer(vue, paires, None)
    y = (rp.rng_tache(RACINE, "y").random(len(paires)) < 0.3).astype(int)
    m = rp.mesures_swanson()
    aires, S = rp.delong([s], y)
    assert abs(aires[0] - m.metriques(m.Ordre(s), y, ks=())["aire"]) < 1e-12
    assert S[0, 0] > 0


def test_holm_exemple_connu():
    h = rp.holm({"a": 0.01, "b": 0.04, "c": 0.03, "d": 0.005}, alpha=0.05)
    assert h["d"]["rejet"] and h["a"]["rejet"]          # 0,005 ≤ 0,0125 ; 0,01 ≤ 0,0167
    assert not h["c"]["rejet"] and not h["b"]["rejet"]  # 0,03 > 0,025 : arrêt
    assert abs(h["d"]["p_holm"] - 0.02) < 1e-12 and abs(h["a"]["p_holm"] - 0.03) < 1e-12


# ------------------------------------------------------------------------------------------------------------ bras

def test_bras_formes_et_valeurs_a_la_main():
    # trois documents d'avant : {a,b}, {b,c}, {c,d} ; catégories x, x, y
    docs = [rp.Document(1, ("a", "b"), "x"), rp.Document(2, ("b", "c"), "x"), rp.Document(3, ("c", "d"), "y")]
    vue = rp.construire_vue(docs, 5)
    i = {c: k for k, c in enumerate(vue.concepts)}
    p = np.array([[i["a"], i["c"]], [i["a"], i["d"]], [i["b"], i["d"]]])
    rp.garde_candidats(vue, p)
    aa = rp.Voisinage("aa").scorer(vue, p, None)
    assert abs(aa[0] - 1 / math.log(2)) < 1e-12 and aa[1] == 0.0      # a–c partagent b (degré 2)
    ra = rp.Voisinage("ra").scorer(vue, p, None)
    assert abs(ra[2] - 0.5) < 1e-12                                     # b–d partagent c (degré 2)
    cn = rp.Voisinage("cn").scorer(vue, p, None)
    assert list(cn) == [1.0, 0.0, 1.0]
    jac = rp.Voisinage("jaccard").scorer(vue, p, None)
    assert abs(jac[0] - 0.5) < 1e-12                                    # Γ(a) = {b}, Γ(c) = {b, d} → 1/2
    pa = rp.Voisinage("pa").scorer(vue, p, None)
    assert list(pa) == [2.0, 1.0, 2.0]
    sw = rp.SwansonABC().scorer(vue, p, None)
    # K(a,c) = n(a,b)·n(b,c)·idf(b)/r(b) = 1·1·ln(3/2)/2 ; r(a) = 1, r(c) = 2 → S = ½(K/1 + K/2)
    K = math.log(3 / 2) / 2
    assert abs(sw[0] - 0.5 * (K + K / 2)) < 1e-12 and sw[1] == 0.0
    lmp = rp.LoinMaisProche().scorer(vue, p, None)
    assert np.all(lmp >= 0) and lmp[1] > 0                              # a (x) et d (y) : cos 0 → poids 1, κ = 0 → 0,05
    assert abs(lmp[1] - 0.05) < 1e-12


def test_jaccard_valeur_exacte():
    docs = [rp.Document(1, ("a", "b"), "x"), rp.Document(2, ("b", "c"), "x"), rp.Document(3, ("c", "d"), "y")]
    vue = rp.construire_vue(docs, 5)
    i = {c: k for k, c in enumerate(vue.concepts)}
    j = rp.jaccard_voisins(vue, np.array([[i["a"], i["c"]]]))
    assert abs(j[0] - 0.5) < 1e-12


def test_hasard_et_hasard_stratifie_sont_des_permutations():
    docs, vue, paires = _vue_et_paires()
    for r in (rp.Hasard(), rp.HasardStratifie()):
        s = r.scorer(vue, paires, rp.rng_tache(RACINE, "h"))
        assert sorted(s) == list(range(1, len(paires) + 1))


def test_retrodiction_jouet_bout_en_bout():
    res = rp.retrodiction(_docs(), COUPURE, HORIZON, 1,
                          [rp.Hasard(), rp.LoinMaisProche(), rp.SwansonABC(), rp.Voisinage("aa")], racine=RACINE)
    aire = {k: v["aire"] for k, v in res["metriques"].items()}
    assert abs(aire["hasard"] - 0.5) < 0.05
    # le monde jouet est construit par fermeture de triangles : Adamic-Adar et Swanson doivent battre le hasard
    assert aire["adamic_adar"] > aire["hasard"] + 0.05 and aire["swanson_abc"] > aire["hasard"] + 0.05
    assert res["holm"]["adamic_adar"]["rejet"] and res["holm"]["swanson_abc"]["rejet"]
    assert "adamic_adar" in rp.regle_entree_course_2(res["holm"])
    assert res["manifeste"]["n_positives"] >= 50 and len(res["manifeste"]["empreinte_scores"]) == 64


def test_retrodiction_monde_nul_aucun_bras_n_entre():
    # artefact symétrique (R4) : issues sans lien avec le passé (fermeture = 0) → aucun bras ne doit battre le hasard
    docs = rp.monde_jouet(RACINE, fermeture=0.0, n_apres=1500)
    res = rp.retrodiction(docs, COUPURE, HORIZON, 1,
                          [rp.Hasard(), rp.SwansonABC(), rp.Voisinage("aa")], racine=RACINE)
    assert rp.regle_entree_course_2(res["holm"]) == [] or all(
        res["comparaison"][k]["delta"] < 0.06 for k in res["comparaison"])


# ---------------------------------------------------------------------------------------------- gardes : sain + artefact

def test_G1_absence_de_fuite_sain_et_artefact():
    docs = _docs()
    for r in (rp.Hasard(), rp.LoinMaisProche(), rp.SwansonABC(), rp.Voisinage("aa")):
        rp.garde_absence_fuite(r, docs, COUPURE, RACINE)          # cas sain

    class Tricheur(rp.RegleDePaires):                             # artefact : lit les documents d'après
        nom = "tricheur"

        def __init__(self, documents):
            self.documents = documents

        def scorer(self, vue, paires, rng):
            futur = {}
            idx = {c: i for i, c in enumerate(vue.concepts)}
            for d in self.documents:
                if d.date > vue.coupure:
                    ids = sorted(idx[c] for c in d.concepts if c in idx)
                    for a in ids:
                        for b in ids:
                            futur[(a, b)] = 1
            return np.array([futur.get((i, j), 0) for i, j in paires], float)

    # l'artefact reçoit les documents réels ; la garde les remplace dans la vue mais pas dans le tricheur → on
    # l'éprouve en lui donnant la liste que la garde perturbe : il suit les documents que la vue lui montre
    class TricheurVue(Tricheur):
        def scorer(self, vue, paires, rng):
            self.documents = vue._documents_complets
            return super().scorer(vue, paires, rng)

    original = rp.construire_vue

    def vue_qui_fuit(documents, coupure, df_min=1, vocabulaire=None):
        v = original(documents, coupure, df_min, vocabulaire)
        v._documents_complets = list(documents)
        return v

    rp.construire_vue = vue_qui_fuit
    try:
        assert "fuite" in _leve(rp.garde_absence_fuite, TricheurVue(docs), docs, COUPURE, RACINE)
    finally:
        rp.construire_vue = original


def test_G2_vocabulaire_sain_et_artefact():
    docs = _docs()
    vue = rp.construire_vue(docs, COUPURE)
    rp.garde_vocabulaire_avant(vue, docs)                          # sain
    docs2 = docs + [rp.Document(COUPURE + 2, ("concept_ne_apres", "c000"), "cat0")]
    vue2 = rp.construire_vue(docs2, COUPURE, vocabulaire=sorted(set(vue.concepts) | {"concept_ne_apres"}))
    assert "vocabulaire" in _leve(rp.garde_vocabulaire_avant, vue2, docs2)


def test_G3_sans_modele_de_langage_sain_et_artefacts():
    regles = [rp.Hasard(), rp.LoinMaisProche(), rp.SwansonABC(), rp.Voisinage("aa")]
    rp.garde_sans_modele_de_langage(regles)                        # sain

    class AvecModele(rp.Hasard):
        nom = "avec_modele"
        utilise_modele_de_langage = True

    assert "déclare" in _leve(rp.garde_sans_modele_de_langage, regles + [AvecModele()])
    sys.modules["openai"] = types.ModuleType("openai")            # artefact : module de modèle de langage chargé
    try:
        assert "chargés" in _leve(rp.garde_sans_modele_de_langage, regles)
    finally:
        del sys.modules["openai"]


def test_G4_candidats_sain_et_artefacts():
    docs, vue, paires = _vue_et_paires()
    rp.garde_candidats(vue, paires)                                # sain
    i, j = np.argwhere(np.triu(vue.n) > 0)[0]
    assert "déjà reliée" in _leve(rp.garde_candidats, vue, np.vstack([paires, [[i, j]]]))
    assert "double" in _leve(rp.garde_candidats, vue, np.vstack([paires, paires[:1]]))
    assert "non ordonnée" in _leve(rp.garde_candidats, vue, paires[:, ::-1])


def test_G5_scores_sain_et_artefacts():
    rp.garde_scores({"a": np.zeros(4)}, 4)                         # sain
    assert "non fini" in _leve(rp.garde_scores, {"a": np.array([0, np.nan, 1, 2.])}, 4)
    assert "scores pour" in _leve(rp.garde_scores, {"a": np.zeros(3)}, 4)


def test_G6_jugeabilite_sain_et_artefact():
    rp.garde_jugeabilite(np.r_[np.ones(60), np.zeros(100)].astype(int))   # sain
    assert "non lançable" in _leve(rp.garde_jugeabilite, np.r_[np.ones(10), np.zeros(100)].astype(int))
    docs = _docs()                                                 # artefact de bout en bout : horizon vide
    assert "non lançable" in _leve(rp.retrodiction, docs, COUPURE, 0, 1, [rp.Hasard()], racine=RACINE)


def test_G7_hasard_au_taux_de_base_sain_et_artefact():
    docs, vue, paires = _vue_et_paires()
    y = (rp.rng_tache(RACINE, "y7").random(len(paires)) < 0.3).astype(int)
    rp.garde_hasard_au_taux_de_base(y, rp.Hasard().scorer(vue, paires, rp.rng_tache(RACINE, "h7")))   # sain
    faux_hasard = y + 0.1 * rp.rng_tache(RACINE, "b7").random(len(y))   # artefact : « hasard » qui voit l'issue
    assert "hors du taux de base" in _leve(rp.garde_hasard_au_taux_de_base, y, faux_hasard)


def test_G8_factices_refuses_sain_et_artefacts():
    rp.garde_bras_reels([rp.Hasard(), rp.SwansonABC()])            # sain
    for F in rp.BRAS_FACTICES:
        assert "factices" in _leve(rp.garde_bras_reels, [rp.Hasard(), F()])
        assert "non branché" in _leve(F().scorer, None, np.zeros((2, 2), int), None)
        assert F(mode_essai=True).scorer(None, np.zeros((3, 2), int), None).tolist() == [0.0, 0.0, 0.0]
        assert F.repris_tel_quel and F.a_brancher and F.entrees_requises
    assert "hasard absent" in _leve(rp.garde_bras_reels, [rp.SwansonABC()])
    assert "factices" in _leve(rp.retrodiction, _docs(), COUPURE, HORIZON, 1, [rp.Hasard(), rp.UzziFactice()],
                               racine=RACINE)


def test_G9_graines_reproductibles_et_independantes():
    a = rp.rng_tache(RACINE, "bras-hasard").random(5)
    b = rp.rng_tache(RACINE, "bras-hasard").random(5)
    c = rp.rng_tache(RACINE, "bras-autre").random(5)
    assert np.array_equal(a, b) and not np.array_equal(a, c)
    r1 = rp.retrodiction(_docs(), COUPURE, HORIZON, 1, [rp.Hasard(), rp.Voisinage("aa")], racine=RACINE)
    r2 = rp.retrodiction(_docs(), COUPURE, HORIZON, 1, [rp.Hasard(), rp.Voisinage("aa")], racine=RACINE)
    assert r1["manifeste"]["empreinte_scores"] == r2["manifeste"]["empreinte_scores"]
    r3 = rp.retrodiction(_docs(), COUPURE, HORIZON, 1, [rp.Hasard(), rp.Voisinage("aa")], racine=RACINE + 1)
    assert r1["manifeste"]["empreinte_scores"] != r3["manifeste"]["empreinte_scores"]


def test_G10_issues_apres_scellement_sain_et_artefacts():
    docs, vue, paires = _vue_et_paires()
    scores = {"hasard": rp.Hasard().scorer(vue, paires, rp.rng_tache(RACINE, "h10"))}
    jeton = rp.sceller_scores(scores, paires)
    iss = rp.Issues(docs, vue, HORIZON)
    y = iss.etiquettes(paires, jeton, scores, 1)                   # sain
    assert y.shape == (len(paires),)
    assert "sans jeton" in _leve(iss.etiquettes, paires, None, scores, 1)
    modifies = {"hasard": scores["hasard"][::-1].copy()}           # artefact : scores changés après scellement
    assert "après scellement" in _leve(iss.etiquettes, paires, jeton, modifies, 1)


def test_pont_fiches_sain_et_artefact():
    docs, vue, paires = _vue_et_paires()
    a = list(vue.concepts[:4])
    b = list(vue.concepts[20:24])
    note = rp.score_paire_fiches(rp.Voisinage("aa"), vue, a, b, m=3)
    assert note >= 0
    assert "non notable" in _leve(rp.score_paire_fiches, rp.Voisinage("aa"), vue, ["inconnu"], ["autre"])


if __name__ == "__main__":
    import tempfile

    class _MP:
        def __init__(self):
            self.annul = []

        def setattr(self, obj, nom, val):
            self.annul.append((obj, nom, getattr(obj, nom)))
            setattr(obj, nom, val)

        def defaire(self):
            for obj, nom, val in reversed(self.annul):
                setattr(obj, nom, val)

    echecs = 0
    fonctions = [(k, v) for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for nom, f in fonctions:
        mp = _MP()
        try:
            if f.__code__.co_argcount == 2:
                with tempfile.TemporaryDirectory() as d:
                    f(Path(d), mp)
            else:
                f()
            print("ok   ", nom)
        except Exception as e:  # noqa: BLE001
            echecs += 1
            print("ÉCHEC", nom, type(e).__name__, e)
        finally:
            mp.defaire()
    print(f"{len(fonctions) - echecs}/{len(fonctions)} essais réussis")
    sys.exit(1 if echecs else 0)
