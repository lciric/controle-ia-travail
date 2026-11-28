"""Vérification indépendante de l'appariement items <-> c2a / c2b — v2 (v1 + lecture du dict b2_neu).

Ne lit AUCUNE sortie de l'extracteur. Lecture seule des sources.
Usage : python3 -I verif_appariement_v1.py DOSSIER_SORTIE
"""
import hashlib
import json
import re
import sys
from pathlib import Path

import numpy as np

DONNEES = Path("/home/user/controle-ia-travail/donnees/P1-loi-attraction-v1")
N200 = Path("/home/user/archive-2026-09/depots/sycophancy-construct-validity/results/n200_complete_results.json")
B2NEU = Path("/home/user/archive-2026-09/depots/sycophancy-construct-validity/analysis/ccG_2026-08-11/depot_B2/b2_neu.json")

EMPREINTES = {
    DONNEES / "c2a_generations.json": "a7c85816e2ce60fd86727fe367cb1d63335940a13b50ba3e33c9e16b3ba6189a",
    DONNEES / "c2b_generations.json": "ec2f7ca5cc80c249fd861a77fb360a8e1c4d59f1788ada2a7864b88ec72586c2",
    N200: "64894c215d68a4566bb0f232cf9c565285a23b3186607bdf0a436384b7a759e9",
    B2NEU: "b8818b844f163c934804f2699a2cea99383dcb61824ae073c4e8f870d8e348d3",
}

SEUIL_MARGE_FAIBLE = 0.10
GRAINE_RACINE = 20261020  # consignée ; dérivations par tâche via SeedSequence.spawn

MOTS_VIDES = set("""
a about above after again against all am an and any are aren't as at be because been before being
below between both but by can can't cannot could couldn't did didn't do does doesn't doing don't down
during each few for from further had hadn't has hasn't have haven't having he he'd he'll he's her here
here's hers herself him himself his how how's i i'd i'll i'm i've if in into is isn't it it's its itself
let's me more most mustn't my myself no nor not of off on once only or other ought our ours ourselves
out over own same shan't she she'd she'll she's should shouldn't so some such than that that's the their
theirs them themselves then there there's these they they'd they'll they're they've this those through
to too under until up very was wasn't we we'd we'll we're we've were weren't what what's when when's
where where's which while who who's whom why why's with won't would wouldn't you you'd you'll you're
you've your yours yourself yourselves also just will may might must shall us one would could however
yet still even much many every within without upon via thus therefore
""".split())

MOT = re.compile(r"[a-z]+(?:'[a-z]+)?")


class ArretNomme(Exception):
    pass


def sha256(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def mots_pleins(s):
    out = set()
    for m in MOT.findall(s.lower()):
        if m.endswith("'s"):
            m = m[:-2]
        if len(m) <= 2 or m in MOTS_VIDES:
            continue
        out.add(m)
    return out


def matrice(textes_mots, reponses_mots_par_item):
    """R[i, j] = moyenne sur les réponses r de l'item j de |T_i ∩ r| / |T_i|."""
    n, m = len(textes_mots), len(reponses_mots_par_item)
    R = np.zeros((n, m))
    for i, T in enumerate(textes_mots):
        if not T:
            raise ArretNomme(f"texte {i} sans mot plein")
        for j, reps in enumerate(reponses_mots_par_item):
            R[i, j] = np.mean([len(T & r) / len(T) for r in reps])
    return R


def marges(R, attendu=None):
    """attendu[p] = item attendu pour la ligne p (défaut : identité). Matrice carrée."""
    n = R.shape[0]
    if attendu is None:
        attendu = list(range(n))
    lignes, colonnes = [], []
    for p in range(n):
        j = attendu[p]
        hors = np.delete(R[p, :], j)
        lignes.append(float(R[p, j] - hors.max()))
    inv = {j: p for p, j in enumerate(attendu)}
    for j in range(R.shape[1]):
        p = inv[j]
        hors = np.delete(R[:, j], p)
        colonnes.append(float(R[p, j] - hors.max()))
    return lignes, colonnes


def garde(R, attendu=None, nom=""):
    lignes, colonnes = marges(R, attendu)
    # lignes : positions p ; colonnes : items j (identiques quand attendu est l'identité)
    defaut = sorted({p for p, x in enumerate(lignes) if x <= 0} |
                    {j for j, x in enumerate(colonnes) if x <= 0})
    if defaut:
        raise ArretNomme(f"ARRET NOMME {nom} : diagonale non dominante, lignes/colonnes {defaut}")
    return min(min(lignes), min(colonnes))


def main(sortie):
    sortie = Path(sortie)
    res = {"version": "verif-appariement-v2", "graine_racine": GRAINE_RACINE,
           "seuil_marge_faible": SEUIL_MARGE_FAIBLE, "numpy": np.__version__}

    # 0. Empreintes des sources
    emp = {}
    for p, attendu in EMPREINTES.items():
        h = sha256(p)
        emp[str(p)] = {"sha256": h, "conforme": h == attendu}
        if h != attendu:
            raise ArretNomme(f"ARRET NOMME empreinte {p}")
    res["empreintes_sources"] = emp

    c2a = json.loads((DONNEES / "c2a_generations.json").read_text())
    c2b = json.loads((DONNEES / "c2b_generations.json").read_text())
    n200 = json.loads(N200.read_text())["texts"]
    b2d = json.loads(B2NEU.read_text())["prompts_en_clair"]  # v2 : dict de clés "0".."29"
    if sorted(b2d.keys(), key=int) != [str(i) for i in range(30)]:
        raise ArretNomme(f"ARRET NOMME cles b2_neu inattendues {sorted(b2d.keys())}")
    b2 = [b2d[str(i)] for i in range(30)]

    # 1. Structure, graines, ordre
    struct = {}
    for nom, d, base, cond_p in (("c2a", c2a, 9000, "hate"), ("c2b", c2b, 9500, "praise")):
        rows = d["rows"]
        items = sorted({r["item"] for r in rows})
        cles = [(r["item"], r["k"], r["cond"]) for r in rows]
        compte = {}
        for r in rows:
            compte[(r["item"], r["cond"])] = compte.get((r["item"], r["cond"]), 0) + 1
        graines_ok = all(r["seed"] == base + 100 * r["item"] + r["k"] for r in rows)
        conds = sorted({r["cond"] for r in rows})
        ordre_items = []
        for r in rows:
            if not ordre_items or ordre_items[-1] != r["item"]:
                ordre_items.append(r["item"])
        struct[nom] = {
            "n_lignes": len(rows), "items": items == list(range(30)), "conditions": conds,
            "dix_par_item_et_condition": all(v == 10 for v in compte.values()) and len(compte) == 60,
            "graines_conformes_formule": graines_ok,
            "k_distincts_0_9": all(sorted(r["k"] for r in rows if r["item"] == i and r["cond"] == "neutral") == list(range(10)) for i in range(30)),
            "ordre_des_blocs_item": ordre_items,
            "doublons_cle": len(cles) - len(set(cles)),
        }
        if conds != sorted(["neutral", cond_p]):
            raise ArretNomme(f"ARRET NOMME conditions inattendues {nom} {conds}")
    seq_a = [(r["item"], r["k"]) for r in c2a["rows"]]
    seq_b = [(r["item"], r["k"]) for r in c2b["rows"]]
    seq_a_c = [(r["item"], r["k"], r["cond"].replace("hate", "P")) for r in c2a["rows"]]
    seq_b_c = [(r["item"], r["k"], r["cond"].replace("praise", "P")) for r in c2b["rows"]]
    struct["meme_suite_item_k"] = seq_a == seq_b
    struct["meme_suite_item_k_condition"] = seq_a_c == seq_b_c
    res["structure"] = struct

    def reps(d, cond):
        out = []
        for i in range(30):
            rr = sorted((r for r in d["rows"] if r["item"] == i and r["cond"] == cond), key=lambda r: r["k"])
            out.append([mots_pleins(r["resp"]) for r in rr])
        return out

    neu_a, neu_b = reps(c2a, "neutral"), reps(c2b, "neutral")
    pre_a, pre_b = reps(c2a, "hate"), reps(c2b, "praise")

    # 2. Recalcul indépendant sur les 200 textes
    M200 = [mots_pleins(t) for t in n200]
    tout = {}
    for nom, rp in (("c2a", neu_a), ("c2b", neu_b)):
        R = matrice(M200, rp)  # 200 x 30
        par_item = []
        for j in range(30):
            col = R[:, j]
            ordre = np.argsort(-col, kind="stable")
            best = int(ordre[0])
            egaux = [int(x) for x in np.where(np.isclose(col, col[best], atol=1e-12))[0]]
            autres = [x for x in ordre if n200[x] != n200[best]]
            second = int(autres[0])
            par_item.append({"item": j, "meilleur_indice": best, "egalites": egaux,
                             "score": float(col[best]), "second_texte_distinct": second,
                             "marge_vs_second_distinct": float(col[best] - col[second]),
                             "indice_j_parmi_meilleurs": j in egaux})
        tout[nom] = {"tous_items_retrouvent_leur_indice": all(x["indice_j_parmi_meilleurs"] for x in par_item),
                     "marge_min_vs_texte_distinct": min(x["marge_vs_second_distinct"] for x in par_item),
                     "items_avec_egalite": [x for x in par_item if len(x["egalites"]) > 1],
                     "par_item": par_item}
    res["recalcul_200_textes"] = tout

    # Doublons exacts dans n200
    vus = {}
    doublons = []
    for i, t in enumerate(n200):
        if t in vus:
            doublons.append([vus[t], i])
        else:
            vus[t] = i
    res["doublons_exacts_n200"] = doublons

    # 3. Liste candidate L = n200[0:30]
    L = n200[:30]
    ML = [mots_pleins(t) for t in L]
    distinct = {
        "exact": len(set(L)) == 30,
        "normalise": len({re.sub(r"\s+", " ", t.strip().lower()) for t in L}) == 30,
    }
    jac = np.zeros((30, 30))
    for i in range(30):
        for j in range(30):
            jac[i, j] = len(ML[i] & ML[j]) / len(ML[i] | ML[j])
    np.fill_diagonal(jac, 0)
    i_, j_ = np.unravel_index(np.argmax(jac), jac.shape)
    distinct["jaccard_max_paire"] = {"paire": [int(i_), int(j_)], "jaccard": float(jac[i_, j_])}
    res["textes_distincts"] = distinct

    inclusion = [L[i] in b2[i] for i in range(30)]
    inclusion_ailleurs = [[k for k in range(len(b2)) if L[i] in b2[k]] for i in range(30)]
    res["inclusion_b2_neu"] = {"n_prompts": len(b2), "inclus_meme_rang": sum(inclusion),
                               "rangs_contenant": inclusion_ailleurs}

    mats = {}
    for nom, rp in (("c2a_neutre", neu_a), ("c2b_neutre", neu_b), ("c2a_hate", pre_a), ("c2b_praise", pre_b)):
        R = matrice(ML, rp)
        lig, col = marges(R)
        diag = np.diag(R)
        hors = R[~np.eye(30, dtype=bool)]
        faibles = sorted({i for i, x in enumerate(lig) if x < SEUIL_MARGE_FAIBLE} |
                         {j for j, x in enumerate(col) if x < SEUIL_MARGE_FAIBLE})
        mats[nom] = {"matrice": [[round(float(x), 4) for x in row] for row in R],
                     "diagonale": [round(float(x), 4) for x in diag],
                     "moyenne_diagonale": float(diag.mean()), "min_diagonale": float(diag.min()),
                     "moyenne_hors_diagonale": float(hors.mean()), "max_hors_diagonale": float(hors.max()),
                     "marges_lignes": [round(x, 4) for x in lig], "marges_colonnes": [round(x, 4) for x in col],
                     "marge_min": float(min(min(lig), min(col))),
                     "item_marge_min_ligne": int(np.argmin(lig)), "item_marge_min_colonne": int(np.argmin(col)),
                     "items_marge_faible": faibles,
                     "garde": "tenue" if min(min(lig), min(col)) > 0 else "ARRET"}
    res["matrices_liste_n200_0_30"] = mats
    # garde décisive (neutres)
    for nom, rp in (("c2a", neu_a), ("c2b", neu_b)):
        garde(matrice(ML, rp), nom=f"liste n200[:30] / {nom}")

    # 4. Réponses c2a contre réponses c2b (sans texte)
    Rab = np.zeros((30, 30))
    for i in range(30):
        for j in range(30):
            Rab[i, j] = np.mean([len(a & b) / max(1, len(a | b)) for a in neu_a[i] for b in neu_b[j]])
    lig, col = marges(Rab)
    res["reponses_c2a_contre_c2b"] = {
        "moyenne_diagonale": float(np.diag(Rab).mean()),
        "moyenne_hors_diagonale": float(Rab[~np.eye(30, dtype=bool)].mean()),
        "marge_min": float(min(min(lig), min(col))),
        "marges_lignes": [round(x, 4) for x in lig], "marges_colonnes": [round(x, 4) for x in col],
        "garde": "tenue" if min(min(lig), min(col)) > 0 else "ARRET",
    }

    # 5. Cas sain et artefacts (R5)
    ss = np.random.SeedSequence(GRAINE_RACINE)
    g_perm, g_mel, g_transp = [np.random.default_rng(s) for s in ss.spawn(3)]
    pi = [int(x) for x in g_perm.permutation(30)]
    Lp = [L[pi[p]] for p in range(30)]
    MLp = [mots_pleins(t) for t in Lp]
    sain = {"permutation": pi, "points_fixes": sum(1 for p in range(30) if pi[p] == p)}
    for nom, rp in (("c2a", neu_a), ("c2b", neu_b)):
        R = matrice(MLp, rp)
        arg = [int(np.argmax(R[p])) for p in range(30)]
        suit = arg == pi
        argcol = [int(np.argmax(R[:, j])) for j in range(30)]
        suit_col = all(pi[argcol[j]] == j for j in range(30))
        try:
            mm = garde(R, attendu=pi, nom=f"cas sain {nom}")
            g = f"tenue (marge min {mm:.4f})"
        except ArretNomme as e:
            g = str(e)
        # et lue à tort comme identité : doit s'arrêter
        try:
            garde(R, nom=f"cas sain lu comme identite {nom}")
            g_id = "PASSE (anormal)"
        except ArretNomme as e:
            g_id = "arret (attendu)"
        sain[nom] = {"argmax_lignes_suit_pi": suit, "argmax_colonnes_suit_pi": suit_col,
                     "garde_relative_a_pi": g, "garde_lue_identite": g_id}
    res["cas_sain_permutation"] = sain

    arte = {}
    mel = [int(x) for x in g_mel.permutation(30)]
    pf = [p for p in range(30) if mel[p] == p]
    Lm = [L[mel[p]] for p in range(30)]
    a1 = {"melange": mel, "points_fixes": pf}
    for nom, rp in (("c2a", neu_a), ("c2b", neu_b)):
        R = matrice([mots_pleins(t) for t in Lm], rp)
        lig, col = marges(R)
        dom = [p for p in range(30) if lig[p] > 0 and col[p] > 0]
        try:
            garde(R, nom=f"A1 {nom}")
            g = "PASSE (anormal)"
        except ArretNomme as e:
            g = str(e)
        a1[nom] = {"moyenne_diagonale": float(np.diag(R).mean()),
                   "moyenne_hors_diagonale": float(R[~np.eye(30, dtype=bool)].mean()),
                   "lignes_dominantes": dom, "dominantes_egal_points_fixes": dom == pf, "garde": g}
    arte["A1_melange"] = a1

    a, b = sorted(int(x) for x in g_transp.choice(30, size=2, replace=False))
    Lt = list(L)
    Lt[a], Lt[b] = Lt[b], Lt[a]
    a2 = {"echange": [a, b]}
    for nom, rp in (("c2a", neu_a), ("c2b", neu_b)):
        R = matrice([mots_pleins(t) for t in Lt], rp)
        lig, col = marges(R)
        nommes = sorted({i for i, x in enumerate(lig) if x <= 0} | {j for j, x in enumerate(col) if x <= 0})
        a2[nom] = {"items_nommes": nommes, "exactement_les_deux": nommes == [a, b]}
    arte["A2_transposition"] = a2

    Lf = n200[100:130]
    a3 = {}
    for nom, rp in (("c2a", neu_a), ("c2b", neu_b)):
        R = matrice([mots_pleins(t) for t in Lf], rp)
        lig, col = marges(R)
        a3[nom] = {"moyenne_diagonale": float(np.diag(R).mean()),
                   "moyenne_hors_diagonale": float(R[~np.eye(30, dtype=bool)].mean()),
                   "max_global": float(R.max()),
                   "lignes_et_colonnes_dominantes": sum(1 for p in range(30) if lig[p] > 0 and col[p] > 0)}
    arte["A3_textes_faux_n200_100_130"] = a3
    res["artefacts"] = arte

    # Liste L consignée par empreinte (pour comparaison ultérieure à l'extracteur)
    res["liste_L_sha256_json"] = hashlib.sha256(json.dumps(L, ensure_ascii=False).encode()).hexdigest()
    res["liste_L_sha256_par_texte"] = [hashlib.sha256(t.encode()).hexdigest() for t in L]

    out = sortie / "resultats-appariement-v2.json"
    out.write_text(json.dumps(res, ensure_ascii=False, indent=1))
    return res


if __name__ == "__main__":
    r = main(sys.argv[1])
    m = r["matrices_liste_n200_0_30"]
    print("structure", {k: v for k, v in r["structure"].items() if k not in ("c2a", "c2b")})
    for k in ("c2a", "c2b"):
        s = r["structure"][k]
        print(k, {x: s[x] for x in s if x != "ordre_des_blocs_item"}, "ordre", s["ordre_des_blocs_item"] == list(range(30)))
    for k, v in m.items():
        print(k, "diag", round(v["moyenne_diagonale"], 3), "hors", round(v["moyenne_hors_diagonale"], 3),
              "marge_min", round(v["marge_min"], 4), "faibles", v["items_marge_faible"], v["garde"])
