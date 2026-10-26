"""Pilote des essais de la brique 1 (encodage et mémoire spectrale), version 1.

Usage : python3 -I -B pilote_brique1_v1.py <essai> --horodatage AAAA-MM-JJTHH:MM:SSZ [--rapide]
Essais : verifications, reel, essai1, essai2, essai3, generations (essais 1, 2 et 4), essai5.
Écrit sortie/resultats/<essai>-v1.json (ou -rapide-v1.json). Bibliothèque standard seule ;
lit seulement fournis/ (rapport, json réel, module original pour comparer l'empreinte).
"""
import argparse
import hashlib
import importlib.util
import json
import math
import platform
import random
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent
FOURNIS = RACINE / "fournis"


def _charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, str(chemin))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


C = _charger("brique1_communs_v1", ICI / "brique1_communs_v1.py")
SH = _charger("simhash_ngrammes_v1", ICI / "simhash_ngrammes_v1.py")
MI = C.instance_memoire("memoire_isvd_code")


def empreinte(chemin):
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def encodeurs():
    return {
        "i": C.memoiser(MI.extraire_vecteur_koopman),
        "ii": C.memoiser(C.encodeur_base_normee),
        "simhash": C.memoiser(lambda t: C.relever_normaliser(C.normer(SH.projection(C.jetons(t))))),
        "simhash_bin": C.memoiser(lambda t: C.relever_normaliser(C.normer(SH.binaire(C.jetons(t))))),
        "nul": C.memoiser(C.encodeur_nul),
        "base": C.memoiser(lambda t: C.normer(C.base_sha256(C.jetons(t)))),
    }


# variante -> (encodeur, centrer) ; « base » ne sert qu'à la mesure d'information (pas de relèvement)
VARIANTES = {
    "i": ("i", False), "ii": ("ii", False), "iii": ("i", True), "iv": ("ii", True),
    "v": ("simhash", False), "vi": ("simhash", True), "v_bin": ("simhash_bin", False),
    "vi_bin": ("simhash_bin", True), "nul": ("nul", False), "nul_c": ("nul", True), "base": ("base", False),
}


# ---------------------------------------------------------------- analyse statique d'un corpus
def analyser(textes, enc, centrer, mat_j):
    psis = [enc(t["texte"]) for t in textes]
    ws = [t["poids"] for t in textes]
    m, mu, w = C.matrice_moment(psis, ws, centrer)
    u_code, s_code = MI.decomposer_jacobi_symetrique(m, C.DIM)
    vals, u_ex, hors_ex, balayages = C.jacobi_exact(m)
    s_ex = [abs(x) for x in vals]
    reps = [[p[i] - mu[i] for i in range(C.DIM)] for p in psis] if centrer else psis
    r1, hasard = C.rappel_plus_proche_voisin(reps, mat_j)
    r1_6_code, _ = C.rappel_plus_proche_voisin(C.coordonnees_rang(reps, u_code), mat_j)
    r1_6_ex, _ = C.rappel_plus_proche_voisin(C.coordonnees_rang(reps, u_ex), mat_j)
    norme_mu = math.sqrt(C.produit_scalaire(mu, mu))
    mu_hat = [x / norme_mu for x in mu] if norme_mu > 1e-15 else [0.0] * C.DIM
    cos_mu = [C.produit_scalaire(p, mu_hat) for p in psis]
    m_brute = m if not centrer else C.matrice_moment(psis, ws, False)[0]
    rayleigh = sum(mu_hat[i] * m_brute[i][j] * mu_hat[j] for i in range(C.DIM) for j in range(C.DIM))
    u1 = [u_ex[i][0] for i in range(C.DIM)]
    classes_psi = [C.parts_classes(p) for p in psis]
    return {
        "sigma_code": [round(x, 6) for x in s_code[:C.RANG]],
        "sigma_exact": [round(x, 6) for x in s_ex[:C.RANG]],
        "ratio_code": s_code[0] / s_code[5] if s_code[5] > 0 else float("inf"),
        "ratio_exact": s_ex[0] / s_ex[5] if s_ex[5] > 0 else float("inf"),
        "ratio_1_2_exact": s_ex[0] / s_ex[1], "ratio_1_5_exact": s_ex[0] / s_ex[4], "ratio_5_6_exact": s_ex[4] / s_ex[5],
        "ecart_rel_max_sigma_code": max(abs(a - b) / b for a, b in zip(s_code[:C.RANG], s_ex[:C.RANG]) if b > 0),
        "residu_hors_diag_code": C.residu_hors_diagonale(m, u_code),
        "residu_hors_diag_exact": hors_ex, "balayages_exact": balayages,
        "part_trace_rang6": sum(s_ex[:C.RANG]) / sum(s_ex),
        "entropie_effective_rang6": C.entropie_effective(s_ex[:C.RANG]),
        "classes_vecteurs_propres": [C.parts_classes([u_ex[i][k] for i in range(C.DIM)]) for k in range(C.RANG)],
        "classes_psi_moyennes": {c: sum(cp[c] for cp in classes_psi) / len(psis) for c in C.CLASSES},
        "poids_total": w,
        "cos_moyen_psi_moyenne": sum(wi * c for wi, c in zip(ws, cos_mu)) / w,
        "cos2_moyen_psi_moyenne": sum(wi * c * c for wi, c in zip(ws, cos_mu)) / w,
        "rayleigh_moyenne_sur_sigma1": rayleigh / s_ex[0] if not centrer else None,
        "W_mu2_sur_sigma1": w * norme_mu ** 2 / s_ex[0] if not centrer else None,
        "alignement_u1_moyenne": abs(C.produit_scalaire(u1, mu_hat)),
        "R1": r1, "R1_hasard": hasard, "R1_rang6_code": r1_6_code, "R1_rang6_exact": r1_6_ex,
        "spearman_cos_jaccard": C.spearman_paires(reps, mat_j),
        "spearman_rang6_code": C.spearman_paires(C.coordonnees_rang(reps, u_code), mat_j),
    }


def ensembles_jetons(textes, cle="texte"):
    if cle == "lemmes":
        return [set(t["lemmes"]) for t in textes]
    return [set(C.jetons(t["texte"])) for t in textes]


def analyser_corpus(textes, encs, variantes, etalon="texte"):
    mat_j = C.matrice_jaccard(ensembles_jetons(textes, etalon))
    return {v: analyser(textes, encs[VARIANTES[v][0]], VARIANTES[v][1], mat_j) for v in variantes}


def agreger(liste, cles):
    sortie = {}
    for cle in cles:
        vals = [x[cle] for x in liste if x.get(cle) is not None]
        if not vals:
            continue
        m, e = C.moyenne_ecart(vals)
        d = {"moyenne": m, "ecart": e, "min": min(vals), "max": max(vals), "n": len(vals)}
        if cle.startswith("ratio"):
            d["part_inf_egal_12"] = sum(1 for x in vals if x <= 12.0) / len(vals)
        sortie[cle] = d
    return sortie


CLES_AGREGEES = ["ratio_code", "ratio_exact", "ratio_1_2_exact", "ratio_1_5_exact", "ratio_5_6_exact",
                 "ecart_rel_max_sigma_code", "residu_hors_diag_code", "part_trace_rang6", "entropie_effective_rang6",
                 "cos_moyen_psi_moyenne", "cos2_moyen_psi_moyenne", "rayleigh_moyenne_sur_sigma1",
                 "W_mu2_sur_sigma1", "alignement_u1_moyenne", "R1", "R1_hasard", "R1_rang6_code", "R1_rang6_exact",
                 "spearman_cos_jaccard", "spearman_rang6_code"]


def differences_appariees(resultats, variante, reference, cle, tache):
    diffs = [r[variante][cle] - r[reference][cle] for r in resultats]
    m, e = C.moyenne_ecart(diffs)
    bas, haut = C.intervalle_bootstrap(diffs, C.graine("bootstrap", tache, variante, reference, cle))
    return {"moyenne": m, "ecart": e, "ic95": [bas, haut], "n": len(diffs)}


# ---------------------------------------------------------------- vérifications (cas sains et artefacts)
def essai_verifications(rapide):
    out = {}
    out["empreinte_copie"] = empreinte(C.CHEMIN_COPIE)
    out["empreinte_original"] = empreinte(FOURNIS / "organisme" / "memoire_isvd.py")
    out["copie_identique"] = out["empreinte_copie"] == out["empreinte_original"]
    communs, tailles = C.verifier_vocabulaires()
    out["vocabulaires_mots_partages"] = communs
    out["vocabulaires_tailles"] = tailles
    textes = C.generer_corpus(C.graine("verif", 0), 40, 3, 300, 0.3)
    textes += [{"texte": "", "poids": 0.5}, {"texte": "é à ç", "poids": 0.5}, {"texte": "x", "poids": 0.5}]
    out["encodeur_i_reimplante_egal_code"] = all(
        C.encodeur_reimplante_i(t["texte"]) == MI.extraire_vecteur_koopman(t["texte"]) for t in textes)
    # Jacobi exact : spectre connu
    rng = random.Random(C.graine("verif", 1))
    q = []
    for _ in range(C.DIM):
        v = [rng.gauss(0, 1) for _ in range(C.DIM)]
        for b in q:
            pr = C.produit_scalaire(v, b)
            v = [x - pr * y for x, y in zip(v, b)]
        q.append(C.normer(v))
    lam = sorted([rng.uniform(0.01, 300.0) for _ in range(C.DIM)], reverse=True)
    a = [[sum(q[k][i] * lam[k] * q[k][j] for k in range(C.DIM)) for j in range(C.DIM)] for i in range(C.DIM)]
    vals, _, hors, bal = C.jacobi_exact(a)
    out["jacobi_exact_spectre_connu_ecart_rel_max"] = max(abs(x - y) / y for x, y in zip(vals, lam))
    out["jacobi_exact_spectre_connu_balayages"] = bal
    _, s_code_long = MI.decomposer_jacobi_symetrique(a, C.DIM, max_iter=20000)
    out["jacobi_code_20000_iter_ecart_rel_max"] = max(abs(x - y) / y for x, y in zip(s_code_long, lam))
    _, s_code = MI.decomposer_jacobi_symetrique(a, C.DIM)
    out["jacobi_code_120_iter_spectre_connu_ecart_rel_max_rang6"] = max(
        abs(x - y) / y for x, y in zip(s_code[:6], lam[:6]))
    # mémoire générationnelle : chemin non centré du pilote = fonction de l'organisme, bit à bit
    enc = encodeurs()
    lots = [C.generer_corpus(C.graine("verif", 2, g), 30, 20, 100, 0.3) for g in range(12)]
    etat_mod, etat_pil, egal = {}, {}, True
    for g, lot in enumerate(lots, start=1):
        traces = [{"texte": t["texte"], "poids": t["poids"]} for t in lot]
        etat_mod = MI.mettre_a_jour_memoire_isvd(etat_mod, traces, generation=g)
        etat_pil = C.maj_memoire(etat_pil, traces, enc["i"], MI.decomposer_jacobi_symetrique, MI, centrer=False)
        egal = egal and etat_mod["Sigma"] == etat_pil["Sigma"] and etat_mod["U"] == etat_pil["U"]
    out["maj_non_centree_egale_organisme_12_generations"] = egal
    # mise à jour centrée sans troncature (rang 16) = dispersion centrée calculée d'un bloc
    etat = {}
    tous_psi, tous_w = [], []
    for lot in lots[:5]:
        etat = C.maj_memoire(etat, lot, enc["ii"], C.decomposeur_exact, MI, centrer=True, rang=C.DIM)
        tous_psi += [enc["ii"](t["texte"]) for t in lot]
        tous_w += [t["poids"] for t in lot]
    m_bloc, _, _ = C.matrice_moment(tous_psi, tous_w, centrer=True)
    vals_bloc, _, _, _ = C.jacobi_exact(m_bloc)
    out["maj_centree_rang16_egale_bloc_ecart_rel_max"] = max(
        abs(x - abs(y)) / abs(y) for x, y in zip(etat["Sigma"], vals_bloc) if abs(y) > 1e-9)
    # garde de la mesure R@1 : cas sain (sacs de mots complets) et artefact (encodage nul)
    corpus = C.generer_corpus(C.graine("verif", 3), 50, 30, 300, 0.3)
    mat_j = C.matrice_jaccard(ensembles_jetons(corpus))
    vocab = sorted(set().union(*ensembles_jetons(corpus)))
    index = {m: k for k, m in enumerate(vocab)}
    sacs = []
    for t in corpus:
        v = [0.0] * len(vocab)
        for j in set(C.jetons(t["texte"])):
            v[index[j]] = 1.0
        sacs.append(v)
    out["garde_R1_sac_binaire_complet"] = C.rappel_plus_proche_voisin(sacs, mat_j)
    out["garde_R1_encodage_nul"] = C.rappel_plus_proche_voisin([enc["nul"](t["texte"]) for t in corpus], mat_j)
    return out


# ---------------------------------------------------------------- corpus réel d'ancrage (fournis/)
def corpus_reel():
    d = json.loads((FOURNIS / "memoire-isvd-gen18.json").read_text(encoding="utf-8"))
    textes, vus = [], set()
    for e in d["exemplaires"] + [x for a in d["archive_genealogique"] for x in a["exemplaires"]]:
        if e["texte"] not in vus:
            vus.add(e["texte"])
            textes.append({"texte": e["texte"], "poids": e["poids"], "source": "json"})
    lignes = (FOURNIS / "rapport-meta-conception.md").read_text(encoding="utf-8").splitlines()
    for ligne in lignes[68:83]:
        if ligne.startswith("- **["):
            brut = ligne[2:].replace("**", "").replace("`", "")
            poids = 0.82 if "Document" in brut[:30] else 0.72
            textes.append({"texte": ("Moisson " + brut)[:500], "poids": poids, "source": "rapport"})
    return d, textes


def essai_reel(rapide):
    d, textes = corpus_reel()
    enc = encodeurs()
    out = {"n_textes": len(textes), "n_json": sum(1 for t in textes if t["source"] == "json"),
           "jetons_par_texte": [len(C.jetons(t["texte"])) for t in textes]}
    sig, u = d["Sigma"], d["U"]
    out["json_sigma"] = sig
    out["json_ratio"] = sig[0] / sig[5]
    out["json_ratio_1_2"], out["json_ratio_1_5"], out["json_ratio_5_6"] = sig[0] / sig[1], sig[0] / sig[4], sig[4] / sig[5]
    out["json_entropie_effective_sigma"] = C.entropie_effective(sig)
    out["json_entropie_effective_sigma_carre"] = C.entropie_effective([s * s for s in sig])
    out["json_classes_vecteurs_propres"] = [C.parts_classes([u[i][k] for i in range(C.DIM)]) for k in range(C.RANG)]
    out["json_signes_u1_sur_carres"] = [u[i][0] for i in range(2, C.DIM, 3)]
    out["json_trajectoire_ratio"] = {a["generation"]: a["Sigma"][0] / a["Sigma"][5] for a in d["archive_genealogique"]}
    u1 = [u[i][0] for i in range(C.DIM)]
    ex = [t for t in textes if t["source"] == "json"]
    out["json_exemplaires_cos_u1"] = [C.produit_scalaire(enc["i"](t["texte"]), u1) for t in ex]
    out["json_exemplaires_classes_psi"] = [C.parts_classes(enc["i"](t["texte"])) for t in ex]
    out["variantes"] = analyser_corpus(textes, enc, ["i", "ii", "iii", "iv", "v", "vi", "nul", "nul_c", "base"])
    return out


# ---------------------------------------------------------------- essai 1 : forme du spectre, balayage en longueur
def essai1(rapide):
    enc = encodeurs()
    graines = 4 if rapide else 10
    out = {"parametres": {"N": 50, "p_commun": 0.3, "p_pont": 0.2, "graines": graines,
                          "longueurs": [3, 10, 30, 60, 100, 300]}, "par_longueur": {}}
    for n in out["parametres"]["longueurs"]:
        res = []
        for s in range(graines):
            textes = C.generer_corpus(C.graine("essai1", n, s), 50, n, n, 0.3)
            res.append(analyser_corpus(textes, enc, ["i", "ii", "iii", "iv"]))
        out["par_longueur"][n] = {v: agreger([r[v] for r in res], CLES_AGREGEES) for v in ["i", "ii", "iii", "iv"]}
        out["par_longueur"][n]["classes_psi_i"] = {
            c: sum(r["i"]["classes_psi_moyennes"][c] for r in res) / len(res) for c in C.CLASSES}
        out["par_longueur"][n]["classes_psi_ii"] = {
            c: sum(r["ii"]["classes_psi_moyennes"][c] for r in res) / len(res) for c in C.CLASSES}
    return out


# ---------------------------------------------------------------- essai 2 : quatre variantes, corpus statiques
def essai2(rapide):
    enc = encodeurs()
    graines = 4 if rapide else 20
    variantes = ["i", "ii", "iii", "iv", "v", "vi", "v_bin", "vi_bin", "nul", "nul_c", "base"]
    out = {"parametres": {"N": [12, 25, 50], "p_commun": [0.0, 0.3, 0.6], "n_jetons": [30, 300], "p_pont": 0.2,
                          "domaines": 5, "graines_par_cellule": graines}, "cellules": {}, "tous": {}}
    tous = []
    for n_textes in out["parametres"]["N"]:
        for pc in out["parametres"]["p_commun"]:
            res = []
            for s in range(graines):
                textes = C.generer_corpus(C.graine("essai2", n_textes, pc, s), n_textes, 30, 300, pc)
                res.append(analyser_corpus(textes, enc, variantes))
            tous += res
            cle = f"N={n_textes}|p_commun={pc}"
            out["cellules"][cle] = {v: agreger([r[v] for r in res], CLES_AGREGEES) for v in variantes}
            out["cellules"][cle]["exemple_graine0"] = {v: {k: res[0][v][k] for k in (
                "sigma_code", "sigma_exact", "classes_vecteurs_propres")} for v in ["i", "ii", "iii", "iv"]}
    out["tous"] = {v: agreger([r[v] for r in tous], CLES_AGREGEES) for v in variantes}
    out["differences_R1_vs_i"] = {v: differences_appariees(tous, v, "i", "R1", "essai2")
                                  for v in variantes if v != "i"}
    out["differences_R1_rang6_vs_i"] = {v: differences_appariees(tous, v, "i", "R1_rang6_code", "essai2")
                                        for v in variantes if v not in ("i", "base")}
    out["differences_R1_vs_ii"] = {v: differences_appariees(tous, v, "ii", "R1", "essai2")
                                   for v in ["iv", "v", "vi", "v_bin", "vi_bin"]}
    # supplément : corpus fléchi, étalon par jetons et étalon par lemmes
    res_j, res_l = [], []
    for s in range(graines):
        textes = C.generer_corpus(C.graine("essai2-flexion", s), 50, 30, 300, 0.3, p_flexion=0.5)
        res_j.append(analyser_corpus(textes, enc, ["i", "ii", "iv", "v", "vi", "base"], etalon="texte"))
        res_l.append(analyser_corpus(textes, enc, ["i", "ii", "iv", "v", "vi", "base"], etalon="lemmes"))
    out["flexion"] = {
        "etalon_jetons": {v: agreger([r[v] for r in res_j], ["R1", "R1_hasard", "R1_rang6_code", "spearman_cos_jaccard"])
                          for v in ["i", "ii", "iv", "v", "vi", "base"]},
        "etalon_lemmes": {v: agreger([r[v] for r in res_l], ["R1", "R1_hasard", "R1_rang6_code", "spearman_cos_jaccard"])
                          for v in ["i", "ii", "iv", "v", "vi", "base"]},
        "diff_R1_lemmes_vi_moins_iv": differences_appariees(res_l, "vi", "iv", "R1", "flexion"),
        "diff_R1_lemmes_v_moins_ii": differences_appariees(res_l, "v", "ii", "R1", "flexion"),
    }
    return out


# ---------------------------------------------------------------- essai 3 : SimHash contre SHA-256 par jeton
PAIRES_FLECHIES = [
    ("spectral", "spectrale"), ("spectral", "spectraux"), ("martingale", "martingales"), ("normalise", "normalisation"),
    ("converge", "convergence"), ("eigenvalue", "eigenvalues"), ("matrice", "matrices"), ("gradient", "gradients"),
    ("optimise", "optimisation"), ("probability", "probabilities"), ("inference", "inferences"),
    ("regularise", "regularisation"), ("estimate", "estimation"), ("estimator", "estimators"), ("kernel", "kernels"),
    ("diffusion", "diffusive"), ("variational", "variationnel"), ("operator", "operateur"), ("manifold", "manifolds"),
    ("topology", "topological"), ("entropy", "entropic"), ("sample", "sampling"), ("learn", "learning"),
    ("train", "training"), ("delegate", "delegation"), ("evaluate", "evaluation"), ("sabotage", "saboteur"),
    ("detect", "detection"), ("monitor", "monitoring"), ("stochastic", "stochastique"),
]
PAIRES_MEME_SUFFIXE = [
    ("spectral", "central"), ("spectraux", "journaux"), ("martingale", "nightingale"), ("normalisation", "conversation"),
    ("convergence", "emergence"), ("eigenvalue", "catalogue"), ("matrices", "practices"), ("gradient", "ingredient"),
    ("optimisation", "organisation"), ("probability", "capability"), ("inference", "conference"),
    ("regularisation", "popularisation"), ("estimation", "animation"), ("estimators", "animators"), ("kernel", "colonel"),
    ("diffusion", "confusion"), ("variational", "rotational"), ("operator", "elevator"), ("manifold", "scaffold"),
    ("topology", "biology"), ("entropy", "philanthropy"), ("sampling", "coupling"), ("learning", "burning"),
    ("training", "draining"), ("delegation", "navigation"), ("evaluation", "population"), ("saboteur", "chauffeur"),
    ("detection", "collection"), ("monitoring", "mentoring"), ("stochastic", "elastic"),
]


def essai3(rapide):
    paires_sans_rapport = [(PAIRES_FLECHIES[k][0], PAIRES_FLECHIES[(k + 11) % 30][1]) for k in range(30)]
    reps = {
        "sha256_par_jeton": lambda w: C.base_sha256([w]),
        "simhash_projection": lambda w: SH.projection([w]),
        "simhash_binaire": lambda w: SH.binaire([w]),
        "releve_i_sha256": lambda w: MI.extraire_vecteur_koopman(w),
        "releve_ii_sha256_base_normee": lambda w: C.encodeur_base_normee(w),
        "releve_simhash_projection_normee": lambda w: C.relever_normaliser(C.normer(SH.projection([w]))),
        "releve_simhash_binaire_norme": lambda w: C.relever_normaliser(C.normer(SH.binaire([w]))),
    }

    def cos_ngrammes(a, b):
        ca, cb = SH.comptes_ngrammes([a]), SH.comptes_ngrammes([b])
        num = sum(ca[g] * cb.get(g, 0) for g in ca)
        return num / math.sqrt(sum(x * x for x in ca.values()) * sum(x * x for x in cb.values()))

    out = {"paires_flechies": PAIRES_FLECHIES, "paires_meme_suffixe": PAIRES_MEME_SUFFIXE,
           "paires_sans_rapport": paires_sans_rapport, "sel_simhash": SH.SEL, "representations": {}}
    familles = {"flechies": PAIRES_FLECHIES, "sans_rapport": paires_sans_rapport, "meme_suffixe": PAIRES_MEME_SUFFIXE}
    toutes = dict(reps)
    toutes["etalon_cosinus_3grammes_exact"] = None
    for nom in toutes:
        cos = {}
        for fam, paires in familles.items():
            if nom == "etalon_cosinus_3grammes_exact":
                cos[fam] = [cos_ngrammes(a, b) for a, b in paires]
            else:
                cos[fam] = [C.cosinus(reps[nom](a), reps[nom](b)) for a, b in paires]
        st = {fam: dict(zip(("moyenne", "ecart"), C.moyenne_ecart(v))) for fam, v in cos.items()}

        def dprime(p, q):
            mp, ep = C.moyenne_ecart(p)
            mq, eq = C.moyenne_ecart(q)
            return (mp - mq) / math.sqrt((ep * ep + eq * eq) / 2.0) if ep + eq > 0 else float("inf")
        out["representations"][nom] = {
            "statistiques": st,
            "aire_flechies_vs_sans_rapport": C.aire_sous_courbe(cos["flechies"], cos["sans_rapport"]),
            "aire_flechies_vs_meme_suffixe": C.aire_sous_courbe(cos["flechies"], cos["meme_suffixe"]),
            "dprime_flechies_vs_sans_rapport": dprime(cos["flechies"], cos["sans_rapport"]),
            "dprime_flechies_vs_meme_suffixe": dprime(cos["flechies"], cos["meme_suffixe"]),
            "cosinus": cos,
        }
    # corrélation entre le cosinus SimHash et l'étalon exact sur les 90 paires
    etalon = sum((out["representations"]["etalon_cosinus_3grammes_exact"]["cosinus"][f] for f in familles), [])
    for nom in ("simhash_projection", "simhash_binaire", "sha256_par_jeton"):
        v = sum((out["representations"][nom]["cosinus"][f] for f in familles), [])
        out["representations"][nom]["spearman_avec_etalon_3grammes"] = C.spearman(v, etalon)
    texte_table, emp_table = SH.table_consignee()
    nom_table = "table-signes-simhash-essai3" + ("-rapide" if rapide else "") + "-v1.tsv"
    if (ICI / "resultats" / nom_table).exists():
        raise SystemExit(f"refus d'écraser {nom_table}")
    (ICI / "resultats" / nom_table).write_text(texte_table, encoding="utf-8")
    out["table_signes"] = {"fichier": "resultats/" + nom_table, "sha256": emp_table,
                           "n_3grammes": texte_table.count("\n")}
    return out


# ---------------------------------------------------------------- générations : essais 1 (forme), 2 (P1 sur 50 cycles) et 4 (Cauchy)
SEUILS_CAUCHY = [0.02, 0.01, 0.005, 0.002]


def premier_declenchement(spectres, eps):
    """Première génération g >= 3 où d(g) < eps et d(g-1) < eps, d(g) = max_k |σ̂_k(g) - σ̂_k(g-1)|,
    σ̂ = Σ / somme(Σ). None si jamais."""
    chap = [[x / sum(s) for x in s] for s in spectres]
    d = [None] + [max(abs(a - b) for a, b in zip(chap[g], chap[g - 1])) for g in range(1, len(chap))]
    for g in range(2, len(chap)):
        if d[g] < eps and d[g - 1] < eps:
            return g + 1, d
    return None, d


def essai_generations(rapide):
    enc = encodeurs()
    graines = 3 if rapide else 10
    n_gen = 50
    taille_lot = 40
    plan = {  # nom -> (encodeur, centrer, décomposeur)
        "i": ("i", False, "code"), "ii": ("ii", False, "code"), "iii": ("i", True, "code"), "iv": ("ii", True, "code"),
        "v": ("simhash", False, "code"), "vi": ("simhash", True, "code"),
        "nul": ("nul", False, "code"), "nul_c": ("nul", True, "code"),
    }
    plan.update({k + "_exact": (e, c, "exact") for k, (e, c, _) in list(plan.items())})
    decomp = {"code": MI.decomposer_jacobi_symetrique, "exact": C.decomposeur_exact}
    out = {"parametres": {"generations": n_gen, "taille_lot": taille_lot, "n_jetons": [20, 100], "p_commun": [0.0, 0.3, 0.6],
                          "p_pont": 0.2, "graines": graines, "seuils_cauchy": SEUILS_CAUCHY}, "par_p_commun": {}}
    for pc in out["parametres"]["p_commun"]:
        flux = []
        for s in range(graines):
            lots = [C.generer_corpus(C.graine("generations", pc, s, g), taille_lot, 20, 100, pc) for g in range(n_gen)]
            traces = [[{"texte": t["texte"], "poids": t["poids"]} for t in lot] for lot in lots]
            rec = {}
            etat, sig_mod, n_ex = {}, [], []
            for g, lot in enumerate(traces, start=1):
                etat = MI.mettre_a_jour_memoire_isvd(etat, lot, generation=g)
                sig_mod.append(etat["Sigma"])
                n_ex.append(len(etat["exemplaires"]))
            rec["module_i"] = {"Sigma": sig_mod, "n_exemplaires": n_ex,
                               "U_final": etat["U"], "erreur_troncature_finale": etat["erreur_troncature_frobenius"]}
            # référence sans troncature : sommes brutes par encodeur, instantanés aux générations 5, 18, 50
            reference = {}
            for e in sorted({x[0] for x in plan.values()}):
                s2 = [[0.0] * C.DIM for _ in range(C.DIM)]
                s1, s0, inst = [0.0] * C.DIM, 0.0, {}
                for g, lot in enumerate(traces, start=1):
                    for item in lot:
                        w = C.poids_organisme(MI, item)
                        p = enc[e](str(item["texte"]).strip())
                        s0 += w
                        for i in range(C.DIM):
                            s1[i] += w * p[i]
                            for j in range(C.DIM):
                                s2[i][j] += w * p[i] * p[j]
                    if g in (5, 18, 50):
                        inst[g] = ([ligne[:] for ligne in s2], s1[:], s0)
                reference[e] = inst

            def sous_espace_vrai(e, centrer, g):
                s2, s1, s0 = reference[e][g]
                m = [[s2[i][j] - (s1[i] * s1[j] / s0 if centrer else 0.0) for j in range(C.DIM)] for i in range(C.DIM)]
                vals, vecs, _, _ = C.jacobi_exact(m)
                return [[vecs[i][k] for k in range(C.RANG)] for i in range(C.DIM)], [abs(x) for x in vals]

            def recouvrement(ua, ub):
                return sum(sum(ua[i][a] * ub[i][b] for i in range(C.DIM)) ** 2
                           for a in range(C.RANG) for b in range(C.RANG)) / C.RANG

            for nom, (e, centrer, dk) in plan.items():
                etat, sigs, parts, pertes, etats = {}, [], [], [], {}
                for g, lot in enumerate(traces, start=1):
                    somme_prec = sum(sigs[-1]) if sigs else 0.0
                    etat = C.maj_memoire(etat, lot, enc[e], decomp[dk], MI, centrer)
                    sigs.append(etat["Sigma"])
                    parts.append(etat["trace_gardee"] / etat["trace_avant"])
                    if g >= 2:
                        pertes.append((etat["trace_avant"] - etat["trace_gardee"]) / (etat["trace_avant"] - somme_prec))
                    if g in (5, 18):
                        etats[g] = etat
                u_vrai5, _ = sous_espace_vrai(e, centrer, 5)
                u_vrai18, s_vrai18 = sous_espace_vrai(e, centrer, 18)
                u_vrai50, s_vrai50 = sous_espace_vrai(e, centrer, 50)
                rec[nom] = {"Sigma": sigs, "part_trace_gardee": parts, "perte_lot": pertes, "U_final": etat["U"],
                            "U_18": etats[18]["U"], "mu_18": etats[18]["mu"], "S0_18": etats[18]["S0"],
                            "recouvrement_memoire_vrai_g18": recouvrement(etats[18]["U"], u_vrai18),
                            "recouvrement_memoire_vrai_g50": recouvrement(etat["U"], u_vrai50),
                            "recouvrement_memoire_g5_g50": recouvrement(etats[5]["U"], etat["U"]),
                            "recouvrement_vrai_g5_g50": recouvrement(u_vrai5, u_vrai50),
                            "ratio_vrai_g18": s_vrai18[0] / s_vrai18[5], "ratio_vrai_g50": s_vrai50[0] / s_vrai50[5]}
            rec["module_egal_pilote_i"] = rec["module_i"]["Sigma"] == rec["i"]["Sigma"]
            flux.append(rec)
        bloc = {"module_egal_pilote_i_tous_flux": all(f["module_egal_pilote_i"] for f in flux),
                "n_exemplaires_module": [f["module_i"]["n_exemplaires"][-1] for f in flux], "variantes": {}}
        for nom in plan:
            r18 = [f[nom]["Sigma"][17][0] / f[nom]["Sigma"][17][5] for f in flux]
            r50 = [f[nom]["Sigma"][49][0] / f[nom]["Sigma"][49][5] for f in flux]
            somme18 = [sum(f[nom]["Sigma"][17]) for f in flux]
            dec = {}
            for eps in SEUILS_CAUCHY:
                gs = [premier_declenchement(f[nom]["Sigma"], eps)[0] for f in flux]
                dec[str(eps)] = {"generations": gs, "jamais": sum(1 for x in gs if x is None)}
            dtraj = [premier_declenchement(f[nom]["Sigma"], 1.0)[1] for f in flux]
            dmoy = {str(g): sum(dt[g - 1] for dt in dtraj) / len(dtraj) for g in (2, 3, 5, 10, 18, 30, 50)}
            fin = flux[0][nom]
            u = fin["U_final"]
            classes18 = [[C.parts_classes([f[nom]["U_18"][i][k] for i in range(C.DIM)]) for k in range(C.RANG)]
                         for f in flux]
            alignements, parts_mu = [], []
            for f in flux:
                mu = f[nom]["mu_18"]
                nmu = math.sqrt(C.produit_scalaire(mu, mu))
                u1 = [f[nom]["U_18"][i][0] for i in range(C.DIM)]
                alignements.append(abs(C.produit_scalaire(u1, mu)) / nmu if nmu > 0 else 0.0)
                parts_mu.append(f[nom]["S0_18"] * nmu ** 2 / f[nom]["Sigma"][17][0])
            bloc["variantes"][nom] = {
                "classes_vecteurs_propres_g18_moyennes": [
                    {c: sum(cl[k][c] for cl in classes18) / len(classes18) for c in C.CLASSES} for k in range(C.RANG)],
                "alignement_u1_moyenne_g18": C.moyenne_ecart(alignements)[0],
                "S0_mu2_sur_sigma1_g18": C.moyenne_ecart(parts_mu)[0],
                "trajectoire_ratio_moyenne": [sum(f[nom]["Sigma"][g][0] / f[nom]["Sigma"][g][5] for f in flux) / len(flux)
                                              for g in range(n_gen)],
                "ratio_g18": dict(zip(("moyenne", "ecart"), C.moyenne_ecart(r18)), min=min(r18), max=max(r18),
                                  part_inf_egal_12=sum(1 for x in r18 if x <= 12) / len(r18)),
                "ratio_g50": dict(zip(("moyenne", "ecart"), C.moyenne_ecart(r50)), min=min(r50), max=max(r50),
                                  part_inf_egal_12=sum(1 for x in r50 if x <= 12) / len(r50)),
                "ratio_1_5_g18": C.moyenne_ecart([f[nom]["Sigma"][17][0] / f[nom]["Sigma"][17][4] for f in flux])[0],
                "ratio_5_6_g18": C.moyenne_ecart([f[nom]["Sigma"][17][4] / f[nom]["Sigma"][17][5] for f in flux])[0],
                "somme_sigma_g18": C.moyenne_ecart(somme18)[0],
                "sigma_g18_graine0": fin["Sigma"][17],
                "classes_vecteurs_propres_final_graine0": [C.parts_classes([u[i][k] for i in range(C.DIM)])
                                                           for k in range(C.RANG)],
                "part_trace_gardee_moyenne_g2_g50": sum(sum(f[nom]["part_trace_gardee"][1:]) / (n_gen - 1)
                                                        for f in flux) / len(flux),
                "perte_lot_moyenne_g2_g50": sum(sum(f[nom]["perte_lot"]) / len(f[nom]["perte_lot"])
                                                for f in flux) / len(flux),
                "recouvrement_memoire_vrai_g18": C.moyenne_ecart([f[nom]["recouvrement_memoire_vrai_g18"] for f in flux])[0],
                "recouvrement_memoire_vrai_g50": C.moyenne_ecart([f[nom]["recouvrement_memoire_vrai_g50"] for f in flux])[0],
                "recouvrement_memoire_g5_g50": C.moyenne_ecart([f[nom]["recouvrement_memoire_g5_g50"] for f in flux])[0],
                "recouvrement_vrai_g5_g50": C.moyenne_ecart([f[nom]["recouvrement_vrai_g5_g50"] for f in flux])[0],
                "ratio_vrai_g18": C.moyenne_ecart([f[nom]["ratio_vrai_g18"] for f in flux])[0],
                "ratio_vrai_g50": C.moyenne_ecart([f[nom]["ratio_vrai_g50"] for f in flux])[0],
                "cauchy_declenchement": dec,
                "cauchy_d_moyen": dmoy,
            }
        out["par_p_commun"][str(pc)] = bloc
    return out


# ---------------------------------------------------------------- essai 5 : P1 peut-il échouer ? corpus structurés
def essai5(rapide):
    enc = encodeurs()
    graines = 4 if rapide else 10
    variantes = ["i", "ii", "iii", "iv", "v", "vi", "nul", "nul_c", "base"]
    out = {"parametres": {"N": 50, "n_jetons": [200, 300], "p_pont": 0.0, "graines": graines,
                          "k_domaines": [2, 3, 5], "p_commun": [0.0, 0.3]}, "cellules": {}}
    noms_domaines = list(C.DOMAINES)
    for k in out["parametres"]["k_domaines"]:
        for pc in out["parametres"]["p_commun"]:
            res = []
            for s in range(graines):
                textes = C.generer_corpus(C.graine("essai5", k, pc, s), 50, 200, 300, pc, p_pont=0.0,
                                          domaines=noms_domaines[:k])
                res.append(analyser_corpus(textes, enc, variantes))
            out["cellules"][f"k={k}|p_commun={pc}"] = {v: agreger([r[v] for r in res], CLES_AGREGEES) for v in variantes}
    return out


ESSAIS = {"verifications": essai_verifications, "reel": essai_reel, "essai1": essai1, "essai2": essai2,
          "essai3": essai3, "generations": essai_generations, "essai5": essai5}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("essai", choices=sorted(ESSAIS))
    ap.add_argument("--horodatage", required=True)
    ap.add_argument("--rapide", action="store_true")
    args = ap.parse_args()
    (ICI / "resultats").mkdir(exist_ok=True)
    resultat = ESSAIS[args.essai](args.rapide)
    manifeste = {
        "essai": args.essai, "rapide": args.rapide, "horodatage_utc": args.horodatage,
        "python": sys.version.split()[0], "plateforme": platform.platform(),
        "graine_maitresse": C.GRAINE_MAITRESSE,
        "derivation_graines": "int.from_bytes(sha256('20261026|<tache>|<indices>').digest()[:8], 'big') -> random.Random",
        "empreintes": {
            "pilote_brique1_v1.py": empreinte(Path(__file__)),
            "brique1_communs_v1.py": empreinte(ICI / "brique1_communs_v1.py"),
            "simhash_ngrammes_v1.py": empreinte(ICI / "simhash_ngrammes_v1.py"),
            "organisme_copie/memoire_isvd.py": empreinte(C.CHEMIN_COPIE),
            "fournis/memoire-isvd-gen18.json": empreinte(FOURNIS / "memoire-isvd-gen18.json"),
            "fournis/rapport-meta-conception.md": empreinte(FOURNIS / "rapport-meta-conception.md"),
        },
    }
    suffixe = "-rapide-v1.json" if args.rapide else "-v1.json"
    chemin = ICI / "resultats" / (args.essai + suffixe)
    if chemin.exists():
        raise SystemExit(f"refus d'écraser {chemin.name} (règle : nouvelle version = nouveau nom)")
    chemin.write_text(json.dumps({"manifeste": manifeste, "resultat": resultat}, indent=1, ensure_ascii=False,
                                 default=str), encoding="utf-8")
    print(chemin)


if __name__ == "__main__":
    main()
