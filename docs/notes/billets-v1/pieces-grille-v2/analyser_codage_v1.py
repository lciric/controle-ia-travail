"""Plan d'analyse de la grille brouillon 2 (sections 5 et 8), écrit avant tout codage.

Lit les modalités, indicateurs et statuts d'analyse DANS LA GRILLE (seule source). Ne lit aucun texte
de billet : seulement le manifeste v2 (classe, appariement, moitié), la table de correspondance des
identifiants neutres, les deux fichiers de marquage et les fichiers de codage.

Usage :
  python analyser_codage_v1.py --grille G --manifeste M --table T --marques1 M1 --marques2 M2 \
      --codeur1 C1.jsonl --codeur2 C2.jsonl --arbitre A.jsonl \
      [--obj1 O1.jsonl --obj2 O2.jsonl --obj-arbitre OA.jsonl] --sortie S.json
  python analyser_codage_v1.py --essai-synthetique ... --sortie S.json   (codages tirés au hasard)
"""
import argparse
import hashlib
import json
import math
import re
import sys

import numpy as np

ENTROPIE = 17963430407690202368587404665739133625  # grille brouillon 2, section 5.3
B = 10_000
SEUIL_KAPPA = 0.60
ENSEMBLES = ["tous", "sans_marquage_1", "sans_marquage_2", "sans_reunion"]
CLASSES_O = [f"O{i}" for i in range(13)]


class Refus(Exception):
    pass


# ---------- lecture de la grille ----------
def lire_grille(p):
    t = open(p, encoding="utf-8").read()
    gestes = {}
    for m in re.finditer(r"^### (G\d{2})\. .*?$(.*?)(?=^### |^## |^---|\Z)", t, re.M | re.S):
        corps = m.group(2)
        mods = re.findall(r"`([^`]+)`", re.search(r"^- \*\*Modalités\*\* : (.*)$", corps, re.M).group(1))
        ind = re.findall(r"`([^`]+)`", re.search(r"^- \*\*Indicateur\*\* : (.*)$", corps, re.M).group(1))
        ana = re.search(r"^- \*\*Analyse\*\* : (comparée|descriptive)", corps, re.M).group(1)
        gestes[m.group(1)] = {"modalites": mods, "indicateur": set(ind), "analyse": ana}
    if sorted(gestes) != [f"G{i:02d}" for i in range(1, 26)]:
        raise Refus("grille : gestes G01 à G25 attendus")
    return gestes


# ---------- lecture et contrôle des codages ----------
def lire_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def controler_gestes(lignes, gestes, billets, nom):
    vus = {}
    for l in lignes:
        cle = (l["billet"], l["geste"])
        if cle in vus:
            raise Refus(f"{nom} : doublon {cle}")
        if l["billet"] not in billets:
            raise Refus(f"{nom} : billet inconnu {l['billet']}")
        if l["geste"] not in gestes or l["modalite"] not in gestes[l["geste"]]["modalites"]:
            raise Refus(f"{nom} : modalité hors grille {cle} {l.get('modalite')}")
        vus[cle] = l["modalite"]
    attendu = len(billets) * len(gestes)
    if len(vus) != attendu:
        raise Refus(f"{nom} : {len(vus)} lignes, {attendu} attendues")
    return vus


def controler_objections(lignes, coms, nom):
    vus = {}
    for l in lignes:
        cle = (l["billet"], l["commentaire"])
        if cle in vus:
            raise Refus(f"{nom} : doublon {cle}")
        if cle not in coms:
            raise Refus(f"{nom} : commentaire inconnu ou réponse d'auteur {cle}")
        if l["classe"] not in CLASSES_O:
            raise Refus(f"{nom} : classe hors grille {cle}")
        vus[cle] = l["classe"]
    if len(vus) != len(coms):
        raise Refus(f"{nom} : {len(vus)} lignes, {len(coms)} attendues")
    return vus


# ---------- statistiques ----------
def kappa(a, b):
    a, b = list(a), list(b)
    n = len(a)
    if n == 0:
        return float("nan"), float("nan")
    po = sum(x == y for x, y in zip(a, b)) / n
    cats = set(a) | set(b)
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
    k = float("nan") if pe == 1 else (po - pe) / (1 - pe)
    return po, k


def ic_boot(stat, n, rng, niveau=0.95, garder=None):
    vals = []
    for _ in range(B):
        idx = rng.integers(0, n, n)
        v = stat(idx)
        if not math.isnan(v):
            vals.append(v)
    if garder is not None:
        garder.extend(vals)
    if not vals:
        return [None, None]
    a = (1 - niveau) / 2
    return [float(np.quantile(vals, a)), float(np.quantile(vals, 1 - a))]


def signe_exact(n_pos, n_neg):
    n = n_pos + n_neg
    if n == 0:
        return 1.0
    k = min(n_pos, n_neg)
    p = 2 * sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n
    return min(1.0, p)


def holm(pvals):
    ordre = sorted(pvals, key=lambda k: pvals[k])
    m = len(ordre)
    adj, courant = {}, 0.0
    for r, k in enumerate(ordre):
        courant = max(courant, min(1.0, (m - r) * pvals[k]))
        adj[k] = courant
    return adj


# ---------- analyse ----------
def ensembles(billets_site, m1, m2):
    return {
        "tous": set(billets_site),
        "sans_marquage_1": set(billets_site) - m1,
        "sans_marquage_2": set(billets_site) - m2,
        "sans_reunion": set(billets_site) - m1 - m2,
    }


def analyser(gestes, man, table, m1, m2, c1, c2, arb, obj=None):
    site_vers_neutre = {v: k for k, v in table.items()}
    tenue = {b["identifiant"]: b for b in man["billets"] if b["moitie"] == "tenue-a-l-ecart"}
    if set(site_vers_neutre) != set(tenue):
        raise Refus("table de correspondance : ne couvre pas exactement la tenue à l'écart")
    ens = ensembles(tenue, m1 & set(tenue), m2 & set(tenue))
    ss = np.random.SeedSequence(ENTROPIE).spawn(4)
    graines = {e: s.spawn(27) for e, s in zip(ENSEMBLES, ss)}
    codes = sorted(gestes)
    res = {"ensembles": {}, "consignes": {}}
    tirages_d = {}

    for e in ENSEMBLES:
        S = ens[e]
        bn = sorted(i for i in S if tenue[i]["classe"] == "bien-note")
        paires = sorted((i, tenue[i]["apparie_a"]) for i in bn
                        if not tenue[i]["sans_apparie"] and tenue[i]["apparie_a"] in S)
        sans_ap = [i for i in bn if tenue[i]["sans_apparie"]]
        R = {"billets": len(S), "bien_notes": len(bn), "paires": len(paires), "sans_apparie": len(sans_ap),
             "gestes": {}}
        liste = sorted(S)
        rng_fiab = np.random.default_rng(graines[e][25])
        pvals = {}
        for gi, g in enumerate(codes):
            G = gestes[g]
            ind = G["indicateur"]
            a = [c1[(site_vers_neutre[i], g)] for i in liste]
            b = [c2[(site_vers_neutre[i], g)] for i in liste]
            ab, bb = [x in ind for x in a], [x in ind for x in b]
            po_m, k_m = kappa(a, b)
            po_i, k_i = kappa(ab, bb)
            prev = (sum(ab) + sum(bb)) / (2 * len(liste))
            ic_k = ic_boot(lambda idx: kappa([ab[j] for j in idx], [bb[j] for j in idx])[1], len(liste), rng_fiab)
            x = {i: arb[(site_vers_neutre[i], g)] in ind for i in S}
            x1 = {i: c1[(site_vers_neutre[i], g)] in ind for i in S}
            x2 = {i: c2[(site_vers_neutre[i], g)] in ind for i in S}
            r = {"accord_brut_modalites": po_m, "kappa_modalites": k_m, "accord_brut_indicateur": po_i,
                 "kappa_indicateur": k_i, "ic95_kappa_indicateur": ic_k, "prevalence_indicateur": prev,
                 "analyse": G["analyse"]}
            r["freq_bien_notes"] = float(np.mean([x[i] for i in bn])) if bn else None
            r["freq_apparies"] = float(np.mean([x[j] for _, j in paires])) if paires else None
            r["freq_bien_notes_sans_apparie"] = float(np.mean([x[i] for i in sans_ap])) if sans_ap else None
            if paires:
                d = np.array([int(x[i]) - int(x[j]) for i, j in paires])
                rng = np.random.default_rng(graines[e][gi])
                r["d"] = float(d.mean())
                tirages_d[(e, g)] = []
                r["ic95_d"] = ic_boot(lambda idx: float(d[idx].mean()), len(d), rng, garder=tirages_d[(e, g)])
                r["p_signe_exact"] = signe_exact(int((d > 0).sum()), int((d < 0).sum()))
                r["d_codeur_1"] = float(np.mean([int(x1[i]) - int(x1[j]) for i, j in paires]))
                r["d_codeur_2"] = float(np.mean([int(x2[i]) - int(x2[j]) for i, j in paires]))
            R["gestes"][g] = r
        # fiabilité (règle 5.2) : décidée plus bas sur « tous » et « sans_marquage_1 »
        res["ensembles"][e] = R

    # Fiabilité, multiplicité, règle du gabarit (section 8).
    T, S1, SU = (res["ensembles"][k]["gestes"] for k in ("tous", "sans_marquage_1", "sans_reunion"))

    def statut_fiab(r):
        if r["prevalence_indicateur"] > 0.90:
            return r["accord_brut_indicateur"] >= 0.90, "prévalence haute : accord brut"
        if r["prevalence_indicateur"] < 0.10:
            return False, "prévalence basse : non évaluable"
        return (not math.isnan(r["kappa_indicateur"])) and r["kappa_indicateur"] >= SEUIL_KAPPA, "kappa"

    fiables = {}
    for g in codes:
        f1, m1_ = statut_fiab(T[g])
        f2, m2_ = statut_fiab(S1[g])
        fiables[g] = {"fiable": f1 and f2, "motif": f"{m1_} / {m2_}"}
    comparees = [g for g in codes if fiables[g]["fiable"] and gestes[g]["analyse"] == "comparée"]
    m = len(comparees)
    for e in ENSEMBLES:
        P = {g: res["ensembles"][e]["gestes"][g].get("p_signe_exact", 1.0) for g in comparees}
        adj = holm(P) if P else {}
        for g in comparees:
            res["ensembles"][e]["gestes"][g]["p_holm"] = adj[g]
    res["fiabilite"] = fiables
    res["m_comparaisons"] = m
    # Intervalles ajustés de Bonferroni (niveau 1 - 0,05/m), sur les mêmes tirages que l'intervalle à 95 %.
    if m:
        a = 0.05 / m / 2
        for e in ENSEMBLES:
            for g in comparees:
                v = tirages_d.get((e, g))
                if v:
                    res["ensembles"][e]["gestes"][g]["ic_bonferroni_d"] = [float(np.quantile(v, a)),
                                                                           float(np.quantile(v, 1 - a))]
    for g in codes:
        if not fiables[g]["fiable"]:
            res["consignes"][g] = "non fiable : exclu"
            continue
        if gestes[g]["analyse"] == "descriptive":
            res["consignes"][g] = "descriptif : jamais consigne"
            continue
        r = T[g]
        su = SU[g]
        if r.get("p_holm", 1) < 0.05 and r["d"] < 0:
            res["consignes"][g] = "à éviter"
            continue
        c3 = r["freq_bien_notes"] is not None and r["freq_bien_notes"] >= 0.5
        c4a, c4b = r.get("d", -1) >= 0, su.get("d", -1) >= 0
        if c3 and c4a and c4b:
            res["consignes"][g] = "consigne distinctive" if (r.get("p_holm", 1) < 0.05 and r["d"] > 0) else "consigne"
        elif c3 and (c4a or c4b):
            res["consignes"][g] = "consigne sous réserve"
        elif not c3 and r.get("ic95_d", [None])[0] is not None and r["ic95_d"][0] > 0:
            res["consignes"][g] = "piste"
        else:
            res["consignes"][g] = "aucune"

    if obj:
        res["objections"] = analyser_objections(obj, tenue_ids={b["identifiant"]: b for b in man["billets"]
                                                                 if b["moitie"] == "tenue-a-l-ecart"},
                                                site_vers_neutre=site_vers_neutre, graine=graines["tous"][26])
    return res


def analyser_objections(obj, tenue_ids, site_vers_neutre, graine):
    o1, o2, oa = obj
    cles = sorted(oa)
    a, b = [o1[k] for k in cles], [o2[k] for k in cles]
    po, k = kappa(a, b)
    par_classe = {}
    rng = np.random.default_rng(graine)
    billets = sorted({k[0] for k in cles})
    idx_par_billet = {bi: [j for j, k_ in enumerate(cles) if k_[0] == bi] for bi in billets}
    n_bn = sum(1 for b_ in tenue_ids.values() if b_["classe"] == "bien-note")
    for c in CLASSES_O:
        ab, bb = [x == c for x in a], [x == c for x in b]
        pc, kc = kappa(ab, bb)
        y = np.array([oa[k_] == c for k_ in cles], dtype=float)

        def part(ix):
            sel = [j for bi in ix for j in idx_par_billet[billets[bi]]]
            return float(y[sel].mean()) if sel else float("nan")

        ic = ic_boot(part, len(billets), rng)
        part_billets = sum(1 for bi in billets if y[idx_par_billet[bi]].any()) / n_bn
        prevenir = (not math.isnan(kc)) and kc >= SEUIL_KAPPA and y.mean() >= 0.10 and part_billets >= 0.25
        par_classe[c] = {"kappa_binaire": kc, "accord_brut": pc, "part": float(y.mean()), "ic95_part": ic,
                         "part_des_bien_notes_touches": part_billets,
                         "objection_a_prevenir": bool(prevenir and c != "O0")}
    return {"commentaires_codables": len(cles), "accord_brut_classe": po, "kappa_classe": k, "classes": par_classe}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def synthetique(gestes, man, rng):
    """Codages tirés au hasard pour éprouver le code (jamais un résultat)."""
    tenue = sorted(b["identifiant"] for b in man["billets"] if b["moitie"] == "tenue-a-l-ecart")
    table = {f"B{k:06d}": i for k, i in zip(rng.choice(10 ** 6, len(tenue), replace=False), tenue)}
    c1, c2, ar = {}, {}, {}
    for n in table:
        for g, G in gestes.items():
            mods = G["modalites"]
            v = mods[rng.integers(len(mods))]
            w = v if rng.random() < 0.8 else mods[rng.integers(len(mods))]
            c1[(n, g)], c2[(n, g)] = v, w
            ar[(n, g)] = v if rng.random() < 0.5 else w
    bn = {b["identifiant"]: b for b in man["billets"] if b["moitie"] == "tenue-a-l-ecart" and b["classe"] == "bien-note"}
    inv = {v: k for k, v in table.items()}
    coms = [(inv[i], f"c{j + 1:02d}") for i, b in bn.items() for j in range(len(b["commentaires_retenus"]))]
    o1 = {k: CLASSES_O[rng.integers(13)] for k in coms}
    o2 = {k: (o1[k] if rng.random() < 0.7 else CLASSES_O[rng.integers(13)]) for k in coms}
    oa = {k: (o1[k] if rng.random() < 0.5 else o2[k]) for k in coms}
    return table, c1, c2, ar, (o1, o2, oa)


def main():
    ap = argparse.ArgumentParser()
    for a in ("grille", "manifeste", "table", "marques1", "marques2", "codeur1", "codeur2", "arbitre",
              "obj1", "obj2", "obj-arbitre", "sortie"):
        ap.add_argument("--" + a)
    ap.add_argument("--essai-synthetique", action="store_true")
    A = ap.parse_args()
    gestes = lire_grille(A.grille)
    man = json.load(open(A.manifeste, encoding="utf-8"))
    m1 = {d["identifiant"] for d in json.load(open(A.marques1, encoding="utf-8"))["marques"]}
    m2 = {d["identifiant"] for d in json.load(open(A.marques2, encoding="utf-8"))["desaccords_dans_le_corpus"]}
    if A.essai_synthetique:
        rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE).spawn(5)[4])  # enfant hors du plan
        table, c1, c2, ar, obj = synthetique(gestes, man, rng)
    else:
        table = json.load(open(A.table, encoding="utf-8"))["neutre_vers_site"]
        neutres = set(table)
        c1 = controler_gestes(lire_jsonl(A.codeur1), gestes, neutres, "codeur 1")
        c2 = controler_gestes(lire_jsonl(A.codeur2), gestes, neutres, "codeur 2")
        ar = controler_gestes(lire_jsonl(A.arbitre), gestes, neutres, "arbitre")
        for k in ar:
            if ar[k] not in (c1[k], c2[k]):
                raise Refus(f"arbitre : modalité hors des deux codages {k}")
        obj = None
        if A.obj1:
            l1, l2, la = lire_jsonl(A.obj1), lire_jsonl(A.obj2), lire_jsonl(A.obj_arbitre)
            coms = {(l["billet"], l["commentaire"]) for l in la}
            obj = (controler_objections(l1, coms, "objections 1"), controler_objections(l2, coms, "objections 2"),
                   controler_objections(la, coms, "objections arbitre"))
    res = analyser(gestes, man, table, m1, m2, c1, c2, ar, obj)
    res["entrees"] = {k: {"chemin": getattr(A, k), "sha256": sha(getattr(A, k))}
                      for k in ("grille", "manifeste", "marques1", "marques2") if getattr(A, k)}
    res["synthetique"] = bool(A.essai_synthetique)
    res["entropie"] = ENTROPIE
    res["numpy"] = np.__version__
    with open(A.sortie, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, default=float)
        f.write("\n")
    print("gestes fiables :", sum(v["fiable"] for v in res["fiabilite"].values()), "; m =", res["m_comparaisons"])
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Refus as e:
        print("REFUS :", e)
        sys.exit(2)
