"""Orchestration — rétrodiction Swanson v1.

Étapes (dans cet ordre) : essais | scores | issues | synthese
  python -I lancer_v1.py scores   → corpus, vocabulaires, champs, candidats, tirage, scores, contrôles de fuite sur les
                                     données réelles ; scores écrits et empreintés AVANT tout calcul d'issue.
  python -I lancer_v1.py issues   → issues, mesures, intervalles, permutations, strate dominée, décisions par découpage.
  python -I lancer_v1.py synthese → D1, D2 (découpage principal), stabilité de l'ordre (placebo), contrôles.
Aucun fichier n'est réécrit (règle des versions) : une étape refuse d'écraser un résultat existant.
"""
import hashlib
import json
import math
import os
import platform
import sys

import numpy as np
import scipy
from scipy import sparse

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

import chaine_v1 as ch  # noqa: E402
import corpus_v1 as co  # noqa: E402
import essais_v1 as es  # noqa: E402
import mesures_v1 as me  # noqa: E402
from termes_v1 import CHAMPS  # noqa: E402

RACINE = "/var/tmp/retrodiction-swanson-v1"
DONNEES = RACINE + "/donnees/arxiv-2003-2016-v1.parquet"
EMPREINTES_DONNEES = RACINE + "/donnees/EMPREINTES-donnees-v1.txt"
SORTIE = RACINE + "/sortie"
TRAVAIL = SORTIE + "/travail"
RESULTATS = SORTIE + "/resultats"
PREREG = SORTIE + "/preenregistrement-retrodiction-v1.md"
ENTROPIE = 20261026
DECOUPAGES = [dict(nom="principal", avant=(2003, 2010), apres=(2011, 2016)),
              dict(nom="placebo", avant=(2003, 2006), apres=(2007, 2010))]
N_PROC = 2
A_SCORE = ["S", "AA", "RA", "CN", "PA"]
METHODES = ["S", "AA", "RA", "CN", "PA", "ST", "U"]
SECONDAIRES = ["S_AC", "S_CA"]
CLASSIQUES = ["AA", "RA", "CN", "PA"]
N_TIRAGES = 1000
N_PERMUTATIONS = 20
N_REFERENCE_PAIRES = 1000
N_REFERENCE_TERMES = 300
TACHES = ["tirage", "ST", "U", "reechantillonnage", "permutations", "essai"]


def journal(*args):
    print(co.heure_utc(), *args, flush=True)


def sha256(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def ecrire_empreinte(chemin):
    with open(chemin + ".sha256", "x") as f:
        f.write(f"{sha256(chemin)}  {os.path.basename(chemin)}\n")


def verifier_empreinte(chemin):
    attendu = open(chemin + ".sha256").read().split()[0]
    if sha256(chemin) != attendu:
        raise RuntimeError(f"empreinte non conforme : {chemin}")
    return attendu


def _convertir(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, (np.bool_,)):
        return bool(o)
    raise TypeError(type(o))


def ecrire_json(chemin, objet):
    with open(chemin, "x", encoding="utf-8") as f:
        json.dump(objet, f, ensure_ascii=False, indent=1, default=_convertir)
    ecrire_empreinte(chemin)


def graines():
    racine = np.random.SeedSequence(entropy=ENTROPIE)
    enfants = racine.spawn(len(DECOUPAGES))
    taches = {d["nom"]: dict(zip(TACHES, e.spawn(len(TACHES)))) for d, e in zip(DECOUPAGES, enfants)}
    description = {nom: {k: dict(entropie=ENTROPIE, cle_engendrement=list(v.spawn_key)) for k, v in t.items()}
                   for nom, t in taches.items()}
    return taches, description


def environnement():
    import duckdb

    code = {f: sha256(os.path.join(ICI, f)) for f in sorted(os.listdir(ICI)) if f.endswith(".py")}
    donnees = {l.split()[1]: l.split()[0] for l in open(EMPREINTES_DONNEES) if l.strip()}
    return dict(python=sys.version, plateforme=platform.platform(), numpy=np.__version__, scipy=scipy.__version__,
                duckdb=duckdb.__version__, code=code, donnees=donnees,
                preenregistrement=verifier_empreinte(PREREG), parametres=ch.PARAMS, decoupages=DECOUPAGES,
                n_processus=N_PROC)


def verifier_donnees():
    for ligne in open(EMPREINTES_DONNEES):
        if ligne.strip():
            h, nom = ligne.split()
            if sha256(os.path.join(RACINE, "donnees", nom)) != h:
                raise RuntimeError(f"empreinte des données non conforme : {nom}")


# ----------------------------------------------------------------------------------------------------------- essais
def etape_essais():
    debut = co.heure_utc()
    bilan = es.tout(PREREG)
    ecrire_json(RESULTATS + "/essais-v1.json", dict(debut=debut, fin=co.heure_utc(), essais_reussis=bilan,
                                                    environnement=environnement()))


# ----------------------------------------------------------------------------------------------------------- scores
def controles_reference(d, st, A, C, scores, rng):
    """Contrôle (c)(ii) : composantes recalculées par l'implémentation lente sur les seuls documents d'avant."""
    X, XT = d["X_avant"], st["XT"]
    idx = np.sort(rng.choice(A.size, size=min(N_REFERENCE_PAIRES, A.size), replace=False))
    ecarts = {k: 0.0 for k in ("K", "K_top", "CN", "AA", "RA", "S", "r_A", "r_C")}
    n_ac_max = 0.0
    for i in idx:
        a, c = int(A[i]), int(C[i])
        r_ = ch.reference_paire(X, XT, a, c, st["idf"], st["r"], st["deg"], st["top1"])
        n_ac_max = max(n_ac_max, r_["n_AC"])
        for k in ("K", "K_top", "CN", "AA", "RA"):
            ecarts[k] = max(ecarts[k], ch.ecart_relatif(r_[k], scores[k][i]))
        ecarts["r_A"] = max(ecarts["r_A"], ch.ecart_relatif(r_["r_A"], st["r"][a]))
        ecarts["r_C"] = max(ecarts["r_C"], ch.ecart_relatif(r_["r_C"], st["r"][c]))
        s_ref = 0.5 * (r_["K"] / r_["r_A"] + r_["K"] / r_["r_C"])
        ecarts["S"] = max(ecarts["S"], ch.ecart_relatif(s_ref, scores["S"][i]))
    termes = rng.choice(st["V"], size=min(N_REFERENCE_TERMES, st["V"]), replace=False)
    ecart_deg, ecart_r = 0, 0.0
    for t in termes:
        deg, r = ch.reference_terme(X, XT, int(t))
        ecart_deg = max(ecart_deg, abs(deg - int(st["deg"][t])))
        ecart_r = max(ecart_r, ch.ecart_relatif(r, st["r"][t]))
    ok = max(ecarts.values()) <= 1e-9 and n_ac_max == 0 and ecart_deg == 0 and ecart_r <= 1e-12
    return dict(n_paires=int(idx.size), ecarts_relatifs_max=ecarts, n_AC_max=n_ac_max, n_termes=int(termes.size),
                ecart_deg_max=int(ecart_deg), ecart_r_max=ecart_r, reussi=bool(ok))


def etape_scores():
    debut = co.heure_utc()
    verifier_donnees()
    env = environnement()
    taches, desc_graines = graines()
    journal("essais automatiques")
    es.tout(PREREG)
    journal("lecture du corpus")
    corpus = co.lire_corpus(DONNEES, TRAVAIL + "/duckdb-temporaire")
    n_docs, n_lignes = len(corpus["ids"]), corpus["n_lignes"]
    journal("documents", n_docs, "lignes", n_lignes)
    prepares = co.preparer(corpus, DECOUPAGES, ch.PARAMS, N_PROC)
    effectifs_annees = {int(a): int(n) for a, n in zip(*np.unique(corpus["annees"], return_counts=True))}
    groupes_docs = np.bincount(corpus["groupes"], minlength=7).tolist()
    del corpus
    journal("passes terminées")
    bilan = dict(debut=debut, environnement=env, graines=desc_graines, n_documents=n_docs, n_lignes=n_lignes,
                 effectifs_annees=effectifs_annees, documents_par_groupe_2003_2016=groupes_docs, decoupages={})
    for dec, d in zip(DECOUPAGES, prepares):
        nom = d["nom"]
        t = taches[nom]
        journal(nom, "vocabulaire", len(d["termes"]), "documents d'avant", d["X_avant"].shape[0],
                "d'après", d["X_apres"].shape[0])
        # contrôle (c)(ii) : seules les années d'avant entrent dans ce qui sert aux scores
        if not (d["annees_avant"].min() >= dec["avant"][0] and d["annees_avant"].max() <= dec["avant"][1]):
            raise RuntimeError("document hors période d'avant dans la matrice d'avant")
        if d["X_avant"].shape[0] != d["n_avant"]:
            raise RuntimeError("nombre de documents d'avant incohérent")
        st = ch.structure_avant(d["X_avant"], d["groupes_avant"], ch.PARAMS)
        if not np.array_equal(np.sort(st["df"]), d["df_passe1"]):
            raise RuntimeError("fréquences d'avant différentes entre passe 1 et matrice d'avant")
        journal(nom, "structure : candidats par champ", [len(x) for x in st["T"]], "N_s", st["N_s"].tolist())
        n_s = ch.allouer(st["N_s"], ch.PARAMS["n_paires"])
        if int(n_s.sum()) != min(ch.PARAMS["n_paires"], int(st["N_s"].sum())):
            raise RuntimeError("allocation incohérente")
        A, C, strate, tires = ch.tirer_paires(st["XT"], st, n_s, t["tirage"])
        n_av = ch.cooccurrences(st["XT"], A, C)
        if np.any(n_av != 0):
            raise RuntimeError("paire tirée cooccurrente avant")
        if np.unique(A.astype(np.int64) * st["V"] + C).size != A.size:
            raise RuntimeError("paire tirée en double")
        if not np.all(st["champ"][A] < st["champ"][C]) or not np.array_equal(np.bincount(strate, minlength=15), n_s):
            raise RuntimeError("strates incohérentes")
        journal(nom, "paires tirées", A.size)
        scores = ch.scorer(d["X_avant"], st, A, C, n_proc=N_PROC)
        journal(nom, "scores calculés")
        ref = controles_reference(d, st, A, C, scores, np.random.default_rng(t["essai"]))
        journal(nom, "contrôle de référence", ref)
        if not ref["reussi"]:
            raise RuntimeError("contrôle de référence en échec : arrêt avant toute issue")
        chemin_scores = RESULTATS + f"/scores-{nom}-v1.npz"
        with open(chemin_scores, "xb") as f:
            np.savez(f, A=A, C=C, strate=strate, **scores)
        ecrire_empreinte(chemin_scores)
        heure_scores = co.heure_utc()
        chemin_vocab = RESULTATS + f"/vocabulaire-{nom}-v1.npz"
        with open(chemin_vocab, "xb") as f:
            np.savez(f, termes=np.array(d["termes"]), df=st["df"], champ=st["champ"], part=st["part"],
                     candidat=st["candidat"], deg=st["deg"], r=st["r"], top1=st["top1"], par_groupe=st["par_groupe"])
        ecrire_empreinte(chemin_vocab)
        chemin_apres = TRAVAIL + f"/apres-{nom}-v1.npz"
        XT_apres = ch.transposee(d["X_apres"])
        with open(chemin_apres, "xb") as f:
            sparse.save_npz(f, XT_apres, compressed=False)
        ecrire_empreinte(chemin_apres)
        dom = (scores["K"] > 0) & (scores["K_top"] > ch.PARAMS["seuil_domine"] * scores["K"])
        bilan["decoupages"][nom] = dict(
            avant=dec["avant"], apres=dec["apres"], n_docs_avant=int(d["X_avant"].shape[0]),
            n_docs_apres=int(d["X_apres"].shape[0]), n_termes_distincts_avant=d["n_termes_distincts_avant"],
            borne_conflit_empreinte=d["n_termes_distincts_avant"] ** 2 / 2.0 ** 65,
            V=st["V"], n_bigrammes=int(sum(" " in x for x in d["termes"])), n_top1=st["n_top"],
            df_seuil_haut=ch.PARAMS["df_max_frac"] * d["X_avant"].shape[0],
            termes_par_document_moyen=float(d["X_avant"].nnz / d["X_avant"].shape[0]),
            specifiques_par_champ=np.bincount(st["champ"][st["specifique"]], minlength=7).tolist(),
            candidats_par_champ=[len(x) for x in st["T"]],
            strates=[f"{CHAMPS[f]}|{CHAMPS[g]}" for f, g in st["strates"]], N_s=st["N_s"].tolist(),
            cooccurrentes_par_strate=[int(st["cooc_inter"][f, g]) for f, g in st["strates"]], n_s=n_s.tolist(),
            tirages_bruts_par_strate=tires, n_paires=int(A.size), K_nul=int(np.sum(scores["K"] == 0)),
            n_dominees=int(dom.sum()), controle_reference=ref,
            fichiers=dict(scores=[chemin_scores, sha256(chemin_scores)], vocabulaire=[chemin_vocab, sha256(chemin_vocab)],
                          apres=[chemin_apres, sha256(chemin_apres)]),
            heure_scores_ecrits=heure_scores)
        del st, scores, d["X_avant"], XT_apres, d["X_apres"]
    bilan["fin"] = co.heure_utc()
    ecrire_json(RESULTATS + "/scores-bilan-v1.json", bilan)
    journal("étape scores terminée")


# ----------------------------------------------------------------------------------------------------------- issues
def _intervalles(tirages):
    return {m: {k: me.intervalle(v) for k, v in mes.items()} for m, mes in tirages.items()}


def etape_issues():
    debut = co.heure_utc()
    env = environnement()
    taches, desc_graines = graines()
    bilan_scores = json.load(open(RESULTATS + "/scores-bilan-v1.json"))
    verifier_empreinte(RESULTATS + "/scores-bilan-v1.json")
    sortie = dict(debut=debut, environnement=env, graines=desc_graines, decoupages={})
    for dec in DECOUPAGES:
        nom = dec["nom"]
        t = taches[nom]
        chemin_scores = RESULTATS + f"/scores-{nom}-v1.npz"
        verifier_empreinte(chemin_scores)
        verifier_empreinte(TRAVAIL + f"/apres-{nom}-v1.npz")
        verifier_empreinte(RESULTATS + f"/vocabulaire-{nom}-v1.npz")
        sc = dict(np.load(chemin_scores))
        vocab = dict(np.load(RESULTATS + f"/vocabulaire-{nom}-v1.npz"))
        XT_apres = sparse.load_npz(TRAVAIL + f"/apres-{nom}-v1.npz").tocsr()
        XT_apres.sort_indices()
        A, C, strate = sc["A"], sc["C"], sc["strate"]
        n = A.size
        journal(nom, "calcul des issues")
        n_apres, y = ch.issues(XT_apres, A, C, ch.PARAMS["seuil_issue"])
        chemin_issues = RESULTATS + f"/issues-{nom}-v1.npz"
        with open(chemin_issues, "xb") as f:
            np.savez(f, n_apres=n_apres, y=y)
        ecrire_empreinte(chemin_issues)
        noms_strates = bilan_scores["decoupages"][nom]["strates"]
        base = me.wilson(int(y.sum()), n)
        par_strate = {noms_strates[s]: me.wilson(int(y[strate == s].sum()), int(np.sum(strate == s)))
                      + [int(np.sum(strate == s))] for s in range(len(noms_strates)) if np.any(strate == s)}
        scores = {m: sc[m] for m in A_SCORE + SECONDAIRES}
        scores["ST"] = me.score_stratifie(strate, np.random.default_rng(t["ST"]))
        scores["U"] = me.score_uniforme(n, np.random.default_rng(t["U"]))
        ordres = {m: me.Ordre(scores[m]) for m in METHODES + SECONDAIRES}
        points = {m: me.metriques(ordres[m], y) for m in ordres}
        meilleur = max(CLASSIQUES, key=lambda m: (points[m]["P@10000"], -CLASSIQUES.index(m)))
        journal(nom, "taux de base", base, "P@10000", {m: round(points[m]["P@10000"], 5) for m in ordres})
        # strate dominée par les termes passe-partout
        K, K_top = sc["K"], sc["K_top"]
        dom = (K > 0) & (K_top > ch.PARAMS["seuil_domine"] * K)
        idx_dom = np.flatnonzero(dom)
        scores_dom = {m: scores[m][idx_dom] for m in METHODES + SECONDAIRES if m != "ST"}
        scores_dom["ST"] = me.score_stratifie(strate[idx_dom], np.random.default_rng(t["ST"].spawn(1)[0]))
        ordres_dom = {m: me.Ordre(scores_dom[m]) for m in METHODES + SECONDAIRES}
        points_dom = {m: me.metriques(ordres_dom[m], y[idx_dom]) for m in ordres_dom}
        base_dom = me.wilson(int(y[idx_dom].sum()), int(idx_dom.size))
        # rééchantillonnage
        journal(nom, "rééchantillonnage")
        differences = [("S", "ST"), ("S", meilleur)] + [("S", m) for m in CLASSIQUES if m != meilleur]
        tirages, diffs = me.reechantillonnage(ordres, y, np.random.default_rng(t["reechantillonnage"]), N_TIRAGES,
                                              sous_ensembles={"domine": (idx_dom, ordres_dom)}, differences=differences)
        ic = _intervalles(tirages["tout"])
        ic_dom = _intervalles(tirages["domine"])
        ic_diffs = {k: me.intervalle(v) for k, v in diffs.items()}
        # permutations des issues
        journal(nom, "permutations")
        rng_p = np.random.default_rng(t["permutations"])
        perm = {m: {k: [] for k in ("P@1000", "P@10000", "PM", "aire")} for m in METHODES + SECONDAIRES}
        for _ in range(N_PERMUTATIONS):
            y_p = y[rng_p.permutation(n)]
            for m in perm:
                res = me.metriques(ordres[m], y_p)
                for k in perm[m]:
                    perm[m][k].append(res[k])
        p = base[0]
        n_pos, n_neg = int(y.sum()), int(n - y.sum())
        et_p10k = math.sqrt(p * (1 - p) / 10000) / math.sqrt(N_PERMUTATIONS)
        et_aire = math.sqrt((n_pos + n_neg + 1) / (12.0 * n_pos * n_neg)) / math.sqrt(N_PERMUTATIONS)
        controle_perm = {}
        for m in perm:
            moy_p = float(np.mean(perm[m]["P@10000"]))
            moy_a = float(np.mean(perm[m]["aire"]))
            controle_perm[m] = dict(moyenne_P10000=moy_p, ecart_en_erreurs_types_P10000=(moy_p - p) / et_p10k,
                                    moyenne_aire=moy_a, ecart_en_erreurs_types_aire=(moy_a - 0.5) / et_aire,
                                    moyenne_P1000=float(np.mean(perm[m]["P@1000"])),
                                    moyenne_PM=float(np.mean(perm[m]["PM"])),
                                    reussi=bool(abs(moy_p - p) < 4 * et_p10k and abs(moy_a - 0.5) < 4 * et_aire))
        # décisions (le découpage principal décide ; le placebo est rapporté)
        d1_ecart = points["S"]["P@10000"] - points["ST"]["P@10000"]
        d2_ecart = points["S"]["P@10000"] - points[meilleur]["P@10000"]
        disjoints = ic["S"]["P@10000"][0] > ic[meilleur]["P@10000"][1]
        exemples = {}
        termes = vocab["termes"]
        for m in ("S", meilleur):
            haut = ordres[m].ordre[:15]
            exemples[m] = [dict(A=str(termes[A[i]]), C=str(termes[C[i]]), strate=noms_strates[strate[i]],
                                score=float(scores[m][i]), n_apres=int(n_apres[i])) for i in haut]
        sortie["decoupages"][nom] = dict(
            n_paires=n, n_positives=n_pos, taux_de_base=base, taux_de_base_par_strate=par_strate,
            ponctuel=points, intervalles=ic, meilleur_classique=meilleur,
            differences_P10000=dict(ponctuel={f"{a}-{b}": points[a]["P@10000"] - points[b]["P@10000"]
                                              for a, b in differences}, intervalles=ic_diffs),
            domine=dict(n_paires=int(idx_dom.size), taux_de_base=base_dom, ponctuel=points_dom, intervalles=ic_dom),
            permutations=dict(n=N_PERMUTATIONS, erreur_type_P10000=et_p10k, erreur_type_aire=et_aire,
                              par_methode=controle_perm, reussi=all(v["reussi"] for v in controle_perm.values())),
            D1=dict(ecart_points=100 * d1_ecart, seuil_points=12.0, retenue=bool(d1_ecart >= 0.12)),
            D2=dict(meilleur=meilleur, ecart_points=100 * d2_ecart, seuil_points=2.0, intervalles_disjoints=bool(disjoints),
                    contribution=bool(d2_ecart >= 0.02 and disjoints)),
            exemples_tete=exemples, n_apres_distribution=np.bincount(np.minimum(n_apres, 10)).tolist(),
            fichiers=dict(issues=[chemin_issues, sha256(chemin_issues)]))
        journal(nom, "D1", sortie["decoupages"][nom]["D1"], "D2", sortie["decoupages"][nom]["D2"])
    sortie["fin"] = co.heure_utc()
    ecrire_json(RESULTATS + "/issues-v1.json", sortie)
    journal("étape issues terminée")


# ----------------------------------------------------------------------------------------------------------- synthèse
def etape_synthese():
    debut = co.heure_utc()
    verifier_empreinte(RESULTATS + "/issues-v1.json")
    iss = json.load(open(RESULTATS + "/issues-v1.json"))
    pr, pl = iss["decoupages"]["principal"], iss["decoupages"]["placebo"]

    def classement(dec, methodes):
        return sorted(methodes, key=lambda m: (-dec["ponctuel"][m]["P@10000"], methodes.index(m)))

    ordre_pr, ordre_pl = classement(pr, A_SCORE), classement(pl, A_SCORE)
    inversions = []
    for i, a in enumerate(ordre_pr):
        for b in ordre_pr[i + 1:]:
            if ordre_pl.index(a) > ordre_pl.index(b):
                recouvre = []
                for dec in (pr, pl):
                    ia, ib = dec["intervalles"][a]["P@10000"], dec["intervalles"][b]["P@10000"]
                    recouvre.append(bool(ia[0] <= ib[1] and ib[0] <= ia[1]))
                inversions.append(dict(paire=[a, b], recouvrement=recouvre, excusee=any(recouvre)))
    if not inversions:
        stabilite = "stable"
    elif all(x["excusee"] for x in inversions):
        stabilite = "partiellement stable"
    else:
        stabilite = "instable"
    sept_pr, sept_pl = classement(pr, METHODES), classement(pl, METHODES)
    synthese = dict(
        debut=debut,
        D1=pr["D1"], D2=pr["D2"],
        P10000_principal={m: [pr["ponctuel"][m]["P@10000"]] + pr["intervalles"][m]["P@10000"] for m in METHODES},
        controle_a_permutations=dict(principal=pr["permutations"]["reussi"], placebo=pl["permutations"]["reussi"]),
        controle_b_placebo=dict(ordre_principal=ordre_pr, ordre_placebo=ordre_pl, inversions=inversions,
                                verdict=stabilite, tau_kendall_sept_methodes=me.tau_kendall(sept_pr, sept_pl),
                                classement_sept_principal=sept_pr, classement_sept_placebo=sept_pl,
                                D1_placebo=pl["D1"], D2_placebo=pl["D2"]),
        controle_c_reference=json.load(open(RESULTATS + "/scores-bilan-v1.json"))["decoupages"],
    )
    synthese["controle_c_reference"] = {k: v["controle_reference"] for k, v in synthese["controle_c_reference"].items()}
    synthese["fin"] = co.heure_utc()
    ecrire_json(RESULTATS + "/synthese-v1.json", synthese)
    journal("synthèse :", json.dumps(dict(D1=synthese["D1"], D2=synthese["D2"], stabilite=stabilite), ensure_ascii=False))


if __name__ == "__main__":
    os.chdir(TRAVAIL)
    etape = sys.argv[1]
    dict(essais=etape_essais, scores=etape_scores, issues=etape_issues, synthese=etape_synthese)[etape]()
