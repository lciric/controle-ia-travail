"""Essais automatiques — rétrodiction Swanson v1 (préenregistrement, section 10 c).

Lancement : python -I essais_v1.py CHEMIN_PREENREGISTREMENT
Chaque essai lève AssertionError en cas d'échec ; la garde de fuite est éprouvée sur un cas sain et sur un artefact.
"""
import itertools
import math
import os
import re
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import chaine_v1 as ch  # noqa: E402
import corpus_v1 as co  # noqa: E402
import mesures_v1 as me  # noqa: E402
from termes_v1 import MOTS_GENERIQUES, MOTS_VIDES, VIDES, groupe_de, termes_document  # noqa: E402

PARAMS_ESSAI = dict(df_min=3, df_max_frac=0.3, cand_df_min=3, cand_df_max=60, part_min=0.6, n_paires=300,
                    seuil_issue=1, frac_top=0.05, seuil_domine=0.5)
DECOUPAGE_ESSAI = [dict(nom="essai", avant=(2003, 2010), apres=(2011, 2016))]


def essai_listes_conformes(chemin_prereg):
    texte = open(chemin_prereg, encoding="utf-8").read()
    for etiquette, liste in (("liste-mots-vides", MOTS_VIDES), ("liste-mots-generiques", MOTS_GENERIQUES)):
        bloc = re.search(r"```" + etiquette + r"\n(.*?)```", texte, re.S)
        assert bloc is not None, etiquette
        assert frozenset(bloc.group(1).split()) == liste, f"{etiquette} : liste du code ≠ liste préenregistrée"


def essai_termes():
    cas = [
        (("Dark Matter Halos", "We study dark matter halos."),
         {"dark", "matter", "halos", "dark matter", "matter halos"}),
        (("", "Poincar\\'e conjecture"), {"poincare", "conjecture", "poincare conjecture"}),
        (("", 'Schr\\"{o}dinger equation'), {"schrodinger", "equation", "schrodinger equation"}),
        (("", "magnetic $B$ field"), {"magnetic", "field"}),
        (("", "magnetic $$B=\\nabla A$$ field"), {"magnetic", "field"}),
        (("", "magnetic \\(B\\) field"), {"magnetic", "field"}),
        (("", "two-dimensional systems"),
         {"two", "dimensional", "systems", "two dimensional", "dimensional systems"}),
        (("", "theory of everything"), {"theory"}),
        (("", "Poincaré duality"), {"poincare", "duality", "poincare duality"}),
        (("", "an X-ray source"), {"ray", "source", "ray source"}),
        (("", "3D printing"), {"printing"}),
        (("", "\\emph{dark} energy"), {"dark", "energy", "dark energy"}),
        (("Quantum", "Gravity"), {"quantum", "gravity"}),
        (("", "\\textbf{Neural} networks, deep"), {"neural", "networks", "neural networks", "deep"}),
        (("", "spin \\begin{equation} x \\end{equation} glass"), {"spin", "glass"}),
        (("", "paper results using based method"), set()),
        (("", "Hilbert's space"), {"hilbert", "space"}),
    ]
    for (titre, resume), attendu in cas:
        obtenu = termes_document(titre, resume)
        assert obtenu == attendu, (titre, resume, obtenu, attendu)


def essai_groupes():
    attendus = {"math.AG cs.LG": 0, "cs.AI math.OC": 1, "hep-th": 2, "astro-ph.CO": 2, "math-ph math.MP": 2,
                "q-bio.NC": 3, "q-fin.ST": 4, "stat.ML": 5, "eess.SP cs.SY": 6, "econ.EM": 6, "nucl-th": 2,
                "nlin.CD": 2, "physics.optics": 2, "quant-ph": 2, "gr-qc": 2, "cond-mat.str-el": 2, "hep-ex": 2,
                "nucl-ex": 2, "hep-lat": 2, "astro-ph": 2, "cond-mat": 2, "": 6}
    for categories, code in attendus.items():
        assert groupe_de(categories) == code, (categories, groupe_de(categories), code)


def _brut_metriques(score, y, k):
    """Références lentes : précision à k moyennée sur tous les départages, précision moyenne par seuils, aire par paires."""
    n = len(score)
    total = 0.0
    perms = list(itertools.permutations(range(n)))
    for p in perms:
        ordre = sorted(range(n), key=lambda i: (-score[i], p[i]))
        total += sum(y[i] for i in ordre[:k]) / k
    p_at_k = total / len(perms)
    seuils = sorted(set(score), reverse=True)
    n_pos = sum(y)
    pm, rappel_prec = 0.0, 0.0
    for s in seuils:
        tp = sum(1 for i in range(n) if score[i] >= s and y[i])
        fp = sum(1 for i in range(n) if score[i] >= s and not y[i])
        rappel = tp / n_pos
        pm += (rappel - rappel_prec) * tp / (tp + fp)
        rappel_prec = rappel
    num = 0.0
    for i in range(n):
        for j in range(n):
            if y[i] and not y[j]:
                num += 1.0 if score[i] > score[j] else (0.5 if score[i] == score[j] else 0.0)
    aire = num / (n_pos * (n - n_pos))
    return p_at_k, pm, aire


def essai_mesures():
    rng = np.random.default_rng(12345)
    for essai in range(25):
        n = 7
        score = rng.integers(0, 3, n).astype(float)
        y = rng.integers(0, 2, n)
        if y.sum() in (0, n):
            y[0], y[1] = 1, 0
        k = int(rng.integers(1, n))
        p_k, pm, aire = _brut_metriques(score.tolist(), y.tolist(), k)
        res = me.metriques(me.Ordre(score), y, None, ks=(k,))
        assert math.isclose(res[f"P@{k}"], p_k, abs_tol=1e-12), (res, p_k)
        assert math.isclose(res["PM"], pm, abs_tol=1e-12), (res, pm)
        assert math.isclose(res["aire"], aire, abs_tol=1e-12), (res, aire)
    for essai in range(25):
        n = 40
        score = rng.integers(0, 6, n).astype(float)
        y = rng.integers(0, 2, n)
        poids = rng.integers(0, 3, n)
        etendu = np.repeat(np.arange(n), poids)
        if poids.sum() < 12 or y[etendu].sum() in (0, etendu.size):
            continue
        a = me.metriques(me.Ordre(score), y, poids.astype(float), ks=(5, 11))
        b = me.metriques(me.Ordre(score[etendu]), y[etendu], None, ks=(5, 11))
        for cle in a:
            assert math.isclose(a[cle], b[cle], rel_tol=1e-12, abs_tol=1e-12), (cle, a[cle], b[cle])


def essai_stratifie():
    rng = np.random.default_rng(7)
    strate = rng.choice(5, size=20000, p=[0.5, 0.2, 0.15, 0.1, 0.05])
    score = me.score_stratifie(strate, np.random.default_rng(8))
    ordre = np.argsort(-score, kind="stable")
    effectifs = np.bincount(strate, minlength=5)
    for k in (10, 100, 1000, 5000):
        pris = np.bincount(strate[ordre[:k]], minlength=5)
        attendu = k * effectifs / strate.size
        assert np.all(np.abs(pris - attendu) <= 1.0 + 1e-9), (k, pris, attendu)
    assert np.unique(score).size == score.size
    u = me.score_uniforme(1000, np.random.default_rng(9))
    assert np.array_equal(np.sort(u), np.arange(1, 1001))


def essai_allouer():
    for N_s, total in (([10, 20, 30], 7), ([5, 0, 5], 3), ([3, 3, 3], 100), ([10**9, 3, 7 * 10**8], 1000)):
        n = ch.allouer(N_s, total)
        assert n.sum() == min(total, sum(N_s)) and np.all(n <= np.array(N_s)), (N_s, total, n)


def corpus_synthetique(graine=2026, n_avant_par_an=150, n_apres_par_an=100):
    rng = np.random.default_rng(graine)
    lettres = np.array(list("bcdfghjklmnpqrstvwxz"))
    voyelles = np.array(list("aeiou"))
    vus = set()

    def mot():
        while True:
            m = "".join(rng.choice(lettres) + rng.choice(voyelles) for _ in range(int(rng.integers(3, 5))))
            if m not in vus and m not in VIDES:
                vus.add(m)
                return m

    propres = [[mot() for _ in range(60)] for _ in range(6)]
    communs = [mot() for _ in range(30)]
    categories = ["math.AG", "cs.LG", "hep-th", "q-bio.NC", "q-fin.ST", "stat.ML"]
    ids, annees, groupes, titres, resumes = [], [], [], [], []
    numero = 0
    for annee in range(2003, 2017):
        n = n_avant_par_an if annee <= 2010 else n_apres_par_an
        for _ in range(n):
            g = int(rng.integers(0, 6))
            mots = []
            for _ in range(int(rng.integers(10, 20))):
                u = rng.random()
                if u < 0.75:
                    mots.append(propres[g][int(rng.integers(0, 60))])
                elif u < 0.95:
                    mots.append(communs[int(rng.integers(0, 30))])
                else:
                    mots.append(propres[int(rng.integers(0, 6))][int(rng.integers(0, 60))])
                if rng.random() < 0.3:
                    mots.append("the")
            numero += 1
            ids.append(f"s{numero:06d}")
            annees.append(annee)
            groupes.append(groupe_de(categories[g]))
            titres.append(" ".join(mots[:3]))
            resumes.append(" ".join(mots[3:]) + ".")
    return dict(ids=ids, annees=np.array(annees, np.int32), groupes=np.array(groupes, np.int8), titres=titres,
                resumes=resumes, n_lignes=len(ids))


def _chaine_complete(corpus, n_proc=1, calculateur=None):
    """La chaîne même du calcul réel, sur un corpus donné ; renvoie tout ce qui doit être invariant et les issues."""
    d = co.preparer(corpus, DECOUPAGE_ESSAI, PARAMS_ESSAI, n_proc)[0]
    st = ch.structure_avant(d["X_avant"], d["groupes_avant"], PARAMS_ESSAI)
    n_s = ch.allouer(st["N_s"], PARAMS_ESSAI["n_paires"])
    racine = np.random.SeedSequence(entropy=99).spawn(6)
    A, C, strate, _ = ch.tirer_paires(st["XT"], st, n_s, racine[0])
    XT_apres = ch.transposee(d["X_apres"])
    if calculateur is None:
        scores = ch.scorer(d["X_avant"], st, A, C, n_proc=n_proc, taille_bloc=7, budget_L=200)
    else:
        scores = calculateur(d, st, A, C, XT_apres)
    n_apres, y = ch.issues(XT_apres, A, C, PARAMS_ESSAI["seuil_issue"])
    invariant = dict(termes=np.array(d["termes"]), df=st["df"], champ=st["champ"], candidat=st["candidat"],
                     deg=st["deg"], r=st["r"], N_s=st["N_s"], A=A, C=C, strate=strate,
                     **{f"score_{k}": v for k, v in scores.items()})
    return invariant, n_apres, d, st


def _identiques(a, b):
    return a.keys() == b.keys() and all(np.array_equal(a[k], b[k]) for k in a)


def _copie(corpus):
    return {k: (list(v) if isinstance(v, list) else (v.copy() if isinstance(v, np.ndarray) else v))
            for k, v in corpus.items()}


def _variantes(corpus, paires):
    """Corpus aux documents d'après modifiés (bourrés de cooccurrences des paires), retirés, ou mélangés."""
    fin_avant = int(np.sum(corpus["annees"] <= 2010))
    bourre = _copie(corpus)
    for i, (a, c) in enumerate(paires):
        j = fin_avant + (i % (len(corpus["ids"]) - fin_avant))
        bourre["resumes"][j] = bourre["resumes"][j] + f" . {a} . {c}"
    retire = {k: (v[:fin_avant] if not isinstance(v, int) else fin_avant) for k, v in corpus.items()}
    melange = _copie(corpus)
    rng = np.random.default_rng(5)
    perm = rng.permutation(np.arange(fin_avant, len(corpus["ids"])))
    melange["resumes"][fin_avant:] = [corpus["resumes"][i] for i in perm]
    return dict(bourre=bourre, retire=retire, melange=melange)


def garde_fuite(corpus, calculateur=None):
    """Vrai si tout ce qui sert aux scores est invariant aux documents d'après et sensible aux documents d'avant."""
    reference, n_apres_ref, d, st = _chaine_complete(corpus, calculateur=calculateur)
    termes = d["termes"]
    paires = [(termes[a], termes[c]) for a, c in zip(reference["A"][:80], reference["C"][:80])]
    for nom, variante in _variantes(corpus, paires).items():
        if nom == "retire":
            continue
        autre, n_apres, _, _ = _chaine_complete(variante, calculateur=calculateur)
        if not _identiques(reference, autre):
            return False
        if nom == "bourre" and not np.any(n_apres > n_apres_ref):
            raise AssertionError("le bourrage des documents d'après n'a pas changé les issues")
    sans_apres = {k: v for k, v in _variantes(corpus, paires)["retire"].items()}
    sans_apres["titres"] = sans_apres["titres"] + ["bourre"]
    sans_apres["resumes"] = sans_apres["resumes"] + ["bourre"]
    sans_apres["ids"] = sans_apres["ids"] + ["s999999"]
    sans_apres["annees"] = np.concatenate([sans_apres["annees"], [2011]]).astype(np.int32)
    sans_apres["groupes"] = np.concatenate([sans_apres["groupes"], [0]]).astype(np.int8)
    autre, _, _, _ = _chaine_complete(sans_apres, calculateur=calculateur)
    if not _identiques(reference, autre):
        return False
    modifie = _copie(corpus)
    modifie["resumes"][0] = modifie["resumes"][0] + " " + " ".join(f"{a} {c}" for a, c in paires[:5])
    autre, _, _, _ = _chaine_complete(modifie, calculateur=calculateur)
    if _identiques(reference, autre):
        raise AssertionError("modifier un document d'avant ne change rien : l'essai serait aveugle")
    return True


def calculateur_fuyant(d, st, A, C, XT_apres):
    """Artefact : mêmes scores, plus un terme qui lit les documents d'après (doit être pris par la garde)."""
    scores = ch.scorer(d["X_avant"], st, A, C)
    scores["S"] = scores["S"] + 1e-9 * ch.cooccurrences(XT_apres, A, C)
    return scores


def essai_fuite_et_reference():
    corpus = corpus_synthetique()
    assert garde_fuite(corpus) is True, "la chaîne réelle n'est pas invariante aux documents d'après"
    assert garde_fuite(corpus, calculateur=calculateur_fuyant) is False, "la garde ne prend pas l'artefact fuyant"
    ref, _, d, st = _chaine_complete(corpus)
    par2, _, _, _ = _chaine_complete(corpus, n_proc=2)
    assert _identiques(ref, par2), "le calcul à deux processus diffère du calcul à un processus"
    X, XT = d["X_avant"], st["XT"]
    assert np.all(ch.cooccurrences(XT, ref["A"], ref["C"]) == 0)
    assert len(set(zip(ref["A"].tolist(), ref["C"].tolist()))) == ref["A"].size
    assert np.all(st["champ"][ref["A"]] < st["champ"][ref["C"]])
    for i in range(ref["A"].size):
        a, c = int(ref["A"][i]), int(ref["C"][i])
        r_ = ch.reference_paire(X, XT, a, c, st["idf"], st["r"], st["deg"], st["top1"])
        assert r_["n_AC"] == 0
        for cle in ("K", "K_top", "CN", "AA", "RA"):
            assert ch.ecart_relatif(r_[cle], ref[f"score_{cle}"][i]) <= 1e-9, (cle, r_[cle], ref[f"score_{cle}"][i])
        assert ch.ecart_relatif(r_["r_A"], st["r"][a]) <= 1e-12 and ch.ecart_relatif(r_["r_C"], st["r"][c]) <= 1e-12
        s_ac = r_["K"] / r_["r_A"]
        s_ca = r_["K"] / r_["r_C"]
        assert ch.ecart_relatif(0.5 * (s_ac + s_ca), ref["score_S"][i]) <= 1e-9
    for t in range(st["V"]):
        deg, r = ch.reference_terme(X, XT, t)
        assert deg == st["deg"][t] and ch.ecart_relatif(r, st["r"][t]) <= 1e-12, (t, deg, st["deg"][t])
    # effectifs de strates par énumération complète
    docs = [set(XT.indices[XT.indptr[t]:XT.indptr[t + 1]].tolist()) for t in range(st["V"])]
    for k, (f, g) in enumerate(st["strates"]):
        n_ok = 0
        for a in st["T"][f]:
            for c in st["T"][g]:
                n_ok += not (docs[a] & docs[c])
        assert n_ok == st["N_s"][k], (f, g, n_ok, st["N_s"][k])
    # issues : énumération
    XTa = ch.transposee(d["X_apres"])
    n_apres = ch.cooccurrences(XTa, ref["A"], ref["C"])
    for i in range(ref["A"].size):
        da = set(XTa.indices[XTa.indptr[ref["A"][i]]:XTa.indptr[ref["A"][i] + 1]].tolist())
        dc = set(XTa.indices[XTa.indptr[ref["C"][i]]:XTa.indptr[ref["C"][i] + 1]].tolist())
        assert len(da & dc) == n_apres[i]


def tout(chemin_prereg):
    essais = [("listes conformes au préenregistrement", lambda: essai_listes_conformes(chemin_prereg)),
              ("extraction des termes", essai_termes), ("groupes", essai_groupes), ("mesures", essai_mesures),
              ("tirage stratifié", essai_stratifie), ("allocation", essai_allouer),
              ("fuite temporelle (cas sain, artefact) et référence lente", essai_fuite_et_reference)]
    bilan = []
    for nom, f in essais:
        f()
        bilan.append(nom)
        print("réussi :", nom, flush=True)
    return bilan


if __name__ == "__main__":
    tout(sys.argv[1])
    print("tous les essais réussis")
