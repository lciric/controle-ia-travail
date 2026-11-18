"""Plan d'analyse de la grille, version v1 (sections 5, 8 et 10), écrit avant tout codage.
Remplace analyser_codage_v2.py. Seul ajout : une description de plus dans le bloc « aveugle »,
les différences rejouées sans les billets reconnus OU devinés (pari juste) par un codeur au moins.
Aucune règle de décision ne la lit.

Lit modalités, indicateurs et statuts DANS LA GRILLE. Ne lit aucun texte de billet : seulement le
manifeste v2 (classe, appariement, moitié), la table des identifiants neutres, les marquages, les
fichiers de codage, la liste des commentaires codables.

Modes :
  tenue      : --codeur1 --codeur2 --arbitre-gestes (désaccords seulement) [--obj1 --obj2
               --arbitre-objections --codables] --table --sortie
  --pilote   : --pilote LISTE --table --codeur1 --codeur2 [--obj1 --obj2 --codables] --sortie
  --essai-synthetique : codages tirés au hasard sur CETTE grille (jamais un résultat)
"""
import argparse
import hashlib
import json
import math
import os
import re
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from controler_depot_v1 import lire_grille, lire_jsonl, PARIS, CLASSES_O, Refus as RefusControle  # noqa: E402

ENTROPIE = 17963430407690202368587404665739133625  # grille, section 5.3
B = 10_000
SEUIL_KAPPA = 0.60
ENSEMBLES = ["tous", "sans_marquage_1", "sans_marquage_2", "sans_reunion"]


class Refus(Exception):
    pass


# ---------- codages ----------
def gestes_et_aveugle(lignes, gestes, billets, nom):
    c, av = {}, {}
    for l in lignes:
        if l["billet"] not in billets:
            raise Refus(f"{nom} : billet inconnu {l['billet']}")
        if l["geste"] == "AVEUGLE":
            if l.get("pari_statut") not in PARIS:
                raise Refus(f"{nom} : ligne AVEUGLE mal formée {l['billet']}")
            av[l["billet"]] = l
            continue
        k = (l["billet"], l["geste"])
        if k in c:
            raise Refus(f"{nom} : doublon {k}")
        if l["geste"] not in gestes or l["modalite"] not in gestes[l["geste"]]["modalites"]:
            raise Refus(f"{nom} : modalité hors grille {k}")
        c[k] = l["modalite"]
    if len(c) != len(billets) * len(gestes) or len(av) != len(billets):
        raise Refus(f"{nom} : fichier incomplet ({len(c)} lignes de geste, {len(av)} lignes AVEUGLE)")
    return c, av


def objections(lignes, attendus, nom):
    o = {}
    for l in lignes:
        k = (l["billet"], l["commentaire"])
        if k not in attendus or k in o or l["classe"] not in CLASSES_O:
            raise Refus(f"{nom} : ligne invalide {k}")
        o[k] = l["classe"]
    if set(o) != attendus:
        raise Refus(f"{nom} : {len(o)} lignes, {len(attendus)} attendues")
    return o


def construire_arbitrage(c1, c2, choix, cle_choix, nom):
    """Valeur commune si accord, choix de l'arbitre sinon ; refus si un choix n'est pas l'une des deux."""
    ar = {}
    for k in c1:
        if c1[k] == c2[k]:
            ar[k] = c1[k]
        else:
            if k not in choix:
                raise Refus(f"{nom} : désaccord non arbitré {k}")
            if choix[k] not in (c1[k], c2[k]):
                raise Refus(f"{nom} : choix hors des deux codages {k}")
            ar[k] = choix[k]
    extra = set(choix) - set(k for k in c1 if c1[k] != c2[k])
    if extra:
        raise Refus(f"{nom} : choix sur des lignes sans désaccord {sorted(extra)[:3]}")
    return ar


# ---------- statistiques ----------
def kappa(a, b):
    a, b = list(a), list(b)
    n = len(a)
    if n == 0:
        return float("nan"), float("nan")
    po = sum(x == y for x, y in zip(a, b)) / n
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in set(a) | set(b))
    return po, (float("nan") if pe == 1 else (po - pe) / (1 - pe))


def ic_boot(stat, n, rng, garder=None):
    vals = []
    for _ in range(B):
        v = stat(rng.integers(0, n, n))
        if not math.isnan(v):
            vals.append(v)
    if garder is not None:
        garder.extend(vals)
    return [float(np.quantile(vals, 0.025)), float(np.quantile(vals, 0.975))] if vals else [None, None]


def signe_exact(n_pos, n_neg):
    n = n_pos + n_neg
    if n == 0:
        return 1.0
    return min(1.0, 2 * sum(math.comb(n, i) for i in range(min(n_pos, n_neg) + 1)) / 2 ** n)


def holm(p):
    ordre = sorted(p, key=lambda k: p[k])
    adj, cour = {}, 0.0
    for r, k in enumerate(ordre):
        cour = max(cour, min(1.0, (len(ordre) - r) * p[k]))
        adj[k] = cour
    return adj


def statut_fiab(r):
    if r["prevalence_indicateur"] > 0.90:
        return "non-evaluable-haute"
    if r["prevalence_indicateur"] < 0.10:
        return "non-evaluable-basse"
    return "fiable" if (not math.isnan(r["kappa_indicateur"]) and r["kappa_indicateur"] >= SEUIL_KAPPA) else "non-fiable"


# ---------- analyse de la tenue ----------
def analyser(gestes, man, table, m1, m2, c1, c2, ar, av1, av2, obj=None):
    s2n = {v: k for k, v in table.items()}
    tenue = {b["identifiant"]: b for b in man["billets"] if b["moitie"] == "tenue-a-l-ecart"}
    if set(s2n) != set(tenue):
        raise Refus("table de correspondance : ne couvre pas exactement la tenue à l'écart")
    m1, m2 = m1 & set(tenue), m2 & set(tenue)
    ens = {"tous": set(tenue), "sans_marquage_1": set(tenue) - m1, "sans_marquage_2": set(tenue) - m2,
           "sans_reunion": set(tenue) - m1 - m2}
    gr = {e: s.spawn(28) for e, s in zip(ENSEMBLES, np.random.SeedSequence(ENTROPIE).spawn(4))}
    codes = sorted(gestes)
    res, tirages = {"ensembles": {}}, {}

    def ind(c, i, g):
        return c[(s2n[i], g)] in gestes[g]["indicateur"]

    def bloc(S, e, cles_rng=True):
        bn = sorted(i for i in S if tenue[i]["classe"] == "bien-note")
        paires = sorted((i, tenue[i]["apparie_a"]) for i in bn if not tenue[i]["sans_apparie"] and tenue[i]["apparie_a"] in S)
        sa = [i for i in bn if tenue[i]["sans_apparie"]]
        R = {"billets": len(S), "bien_notes": len(bn), "paires": len(paires), "sans_apparie": len(sa), "gestes": {}}
        liste = sorted(S)
        rf = np.random.default_rng(gr[e][25])
        for gi, g in enumerate(codes):
            a = [c1[(s2n[i], g)] for i in liste]
            b = [c2[(s2n[i], g)] for i in liste]
            ab = [x in gestes[g]["indicateur"] for x in a]
            bb = [x in gestes[g]["indicateur"] for x in b]
            po_m, k_m = kappa(a, b)
            po_i, k_i = kappa(ab, bb)
            r = {"analyse": gestes[g]["analyse"], "accord_brut_modalites": po_m, "kappa_modalites": k_m,
                 "accord_brut_indicateur": po_i, "kappa_indicateur": k_i,
                 "ic95_kappa_indicateur": ic_boot(lambda ix: kappa([ab[j] for j in ix], [bb[j] for j in ix])[1], len(liste), rf),
                 "prevalence_indicateur": (sum(ab) + sum(bb)) / (2 * len(liste))}
            x = {i: ind(ar, i, g) for i in S}
            r["freq_bien_notes"] = float(np.mean([x[i] for i in bn])) if bn else None
            r["freq_apparies"] = float(np.mean([x[j] for _, j in paires])) if paires else None
            r["freq_bien_notes_sans_apparie"] = float(np.mean([x[i] for i in sa])) if sa else None
            if paires:
                d = np.array([int(x[i]) - int(x[j]) for i, j in paires])
                tirages[(e, g)] = []
                r["d"] = float(d.mean())
                r["ic95_d"] = ic_boot(lambda ix: float(d[ix].mean()), len(d), np.random.default_rng(gr[e][gi]), tirages[(e, g)])
                r["p_signe_exact"] = signe_exact(int((d > 0).sum()), int((d < 0).sum()))
                r["d_codeur_1"] = float(np.mean([int(ind(c1, i, g)) - int(ind(c1, j, g)) for i, j in paires]))
                r["d_codeur_2"] = float(np.mean([int(ind(c2, i, g)) - int(ind(c2, j, g)) for i, j in paires]))
            R["gestes"][g] = r
        return R

    for e in ENSEMBLES:
        res["ensembles"][e] = bloc(ens[e], e)
    T, S1, SU = (res["ensembles"][k]["gestes"] for k in ("tous", "sans_marquage_1", "sans_reunion"))

    fiab = {}
    for g in codes:
        s_t, s_1 = statut_fiab(T[g]), statut_fiab(S1[g])
        if "non-evaluable-haute" in (s_t, s_1):
            st = "non-evaluable-haute"
        elif "non-evaluable-basse" in (s_t, s_1):
            st = "non-evaluable-basse"
        else:
            st = "fiable" if s_t == s_1 == "fiable" else "non-fiable"
        fiab[g] = {"statut": st, "tous": s_t, "sans_marquage_1": s_1}
    comparees = [g for g in codes if fiab[g]["statut"] == "fiable" and gestes[g]["analyse"] == "comparée"]
    m = len(comparees)
    for e in ENSEMBLES:
        P = {g: res["ensembles"][e]["gestes"][g].get("p_signe_exact", 1.0) for g in comparees}
        for g, p in (holm(P) if P else {}).items():
            res["ensembles"][e]["gestes"][g]["p_holm"] = p
            v = tirages.get((e, g))
            if v:
                a = 0.05 / m / 2
                res["ensembles"][e]["gestes"][g]["ic_bonferroni_d"] = [float(np.quantile(v, a)), float(np.quantile(v, 1 - a))]
    res["fiabilite"], res["m_comparaisons"] = fiab, m

    # Règle du gabarit, dans l'ordre de la section 8 (correction lue sur « tous »).
    cons = {}
    for g in codes:
        st, r, su = fiab[g]["statut"], T[g], SU[g]
        comp = gestes[g]["analyse"] == "comparée"
        if st == "non-evaluable-haute":
            cons[g] = "convention du genre (fiabilité non mesurée)" if comp else "quasi universel, descriptif"
        elif st in ("non-evaluable-basse", "non-fiable"):
            cons[g] = "exclu (" + ("rare, non évaluable" if st == "non-evaluable-basse" else "non fiable") + ")"
        elif not comp:
            cons[g] = "descriptif : jamais consigne"
        elif r.get("p_holm", 1) < 0.05 and r["d"] < 0:
            cons[g] = "à éviter"
        else:
            maj = r["freq_bien_notes"] is not None and r["freq_bien_notes"] >= 0.5
            d23, d11 = r.get("d", -1), su.get("d", -1)
            if maj and d23 >= 0 and d11 >= 0 and r.get("p_holm", 1) < 0.05 and d23 > 0:
                cons[g] = "consigne distinctive"
            elif maj and d23 >= 0 and d11 >= 0:
                cons[g] = "consigne — pratique majoritaire, non contredite"
            elif maj and d23 >= 0 and d11 < 0:
                cons[g] = "consigne sous réserve"
            elif not maj and r.get("ic95_d", [None])[0] is not None and r["ic95_d"][0] > 0:
                cons[g] = "piste"
            else:
                cons[g] = "aucune consigne"
    res["consignes"] = cons

    # Aveugle : paris justes, billets reconnus, sensibilité sans les reconnus.
    rng_av = np.random.default_rng(gr["tous"][27])
    vrai = {s2n[i]: ("bien-noté" if tenue[i]["classe"] == "bien-note" else "peu-noté") for i in tenue}
    av = {}
    for nom, A in (("codeur_1", av1), ("codeur_2", av2)):
        paris = [(n, l["pari_statut"]) for n, l in A.items() if l["pari_statut"] != "ne-sait-pas"]
        justes = np.array([p == vrai[n] for n, p in paris], dtype=float)
        av[nom] = {"paris": len(paris), "part_juste": float(justes.mean()) if len(justes) else None,
                   "ic95": ic_boot(lambda ix: float(justes[ix].mean()), len(justes), rng_av) if len(justes) else None,
                   "reconnus": sum(1 for l in A.values() if l["reconnu"])}
    reconnus = {table[n] for A in (av1, av2) for n, l in A.items() if l["reconnu"]}
    if reconnus:
        Sr = set(tenue) - reconnus
        Rr = bloc(Sr, "tous")
        av["sensibilite_sans_reconnus"] = {"billets": Rr["billets"], "paires": Rr["paires"],
                                           "d": {g: Rr["gestes"][g].get("d") for g in codes}}
    devines = {table[n] for A in (av1, av2) for n, l in A.items() if l["pari_statut"] == vrai[n]}
    Sd = set(tenue) - reconnus - devines
    if Sd != set(tenue):
        Rd = bloc(Sd, "tous") if Sd else None
        av["description_sans_reconnus_ni_devines"] = {
            "billets": len(Sd), "paires": Rd["paires"] if Rd else 0,
            "freq_bien_notes": {g: Rd["gestes"][g].get("freq_bien_notes") for g in codes} if Rd else None,
            "freq_apparies": {g: Rd["gestes"][g].get("freq_apparies") for g in codes} if Rd else None,
            "d": {g: Rd["gestes"][g].get("d") for g in codes} if Rd else None,
            "avertissement": "sous-ensemble choisi sur une variable qui dépend du statut : description seulement"}
    res["aveugle"] = av

    if obj:
        res["objections"] = {e: analyser_objections(obj, ens[e], s2n, tenue, np.random.default_rng(gr[e][26]))
                             for e in ENSEMBLES}
    return res


def analyser_objections(obj, S, s2n, tenue, rng):
    o1, o2, oa = obj
    neutres = {s2n[i] for i in S}
    cles = sorted(k for k in oa if k[0] in neutres)
    if not cles:
        return {"commentaires_codables": 0}
    a, b = [o1[k] for k in cles], [o2[k] for k in cles]
    po, k = kappa(a, b)
    billets = sorted({k_[0] for k_ in cles})
    par_b = {bi: [j for j, k_ in enumerate(cles) if k_[0] == bi] for bi in billets}
    n_bn = sum(1 for i in S if tenue[i]["classe"] == "bien-note")
    out = {}
    for c in CLASSES_O:
        ab, bb = [x == c for x in a], [x == c for x in b]
        pc, kc = kappa(ab, bb)
        prev = (sum(ab) + sum(bb)) / (2 * len(cles))
        y = np.array([oa[k_] == c for k_ in cles], dtype=float)

        def part(ix):
            sel = [j for bi in ix for j in par_b[billets[bi]]]
            return float(y[sel].mean()) if sel else float("nan")

        touches = sum(1 for bi in billets if y[par_b[bi]].any()) / n_bn if n_bn else 0.0
        fiable = 0.10 <= prev <= 0.90 and not math.isnan(kc) and kc >= SEUIL_KAPPA
        out[c] = {"kappa_binaire": kc, "accord_brut": pc, "prevalence": prev, "part": float(y.mean()),
                  "ic95_part": ic_boot(part, len(billets), rng), "part_des_bien_notes_touches": touches,
                  "objection_a_prevenir": bool(c not in ("O0", "O12", "O13") and fiable and y.mean() >= 0.10 and touches >= 0.25)}
    return {"commentaires_codables": len(cles), "accord_brut_classe": po, "kappa_classe": k, "classes": out}


# ---------- pilote ----------
def analyser_pilote(gestes, table, c1, c2, av1, av2, lignes1, lignes2, man, obj=None):
    classe = {b["identifiant"]: b["classe"] for b in man["billets"]}
    neutres = sorted(table)
    doutes = {g: 0 for g in gestes}
    for L in (lignes1, lignes2):
        for l in L:
            if l["geste"] in doutes and l.get("doute"):
                doutes[l["geste"]] += 1
    res = {"billets": len(neutres), "gestes": {}}
    for g in sorted(gestes):
        a = [c1[(n, g)] for n in neutres]
        b = [c2[(n, g)] for n in neutres]
        ab = [x in gestes[g]["indicateur"] for x in a]
        bb = [x in gestes[g]["indicateur"] for x in b]
        po_m, k_m = kappa(a, b)
        po_i, k_i = kappa(ab, bb)
        des = sum(x != y for x, y in zip(ab, bb))
        palier = "inchangé" if des <= 1 else ("préciser un cas limite permis" if des <= 3 else "réécrire, fusionner ou retirer")
        if des <= 1 and doutes[g] >= 3:
            palier = "préciser un cas limite permis (doutes)"
        res["gestes"][g] = {"accord_brut_modalites": po_m, "kappa_modalites": k_m, "accord_brut_indicateur": po_i,
                            "kappa_indicateur": k_i, "desaccords_indicateur": des,
                            "desaccords_modalites": sum(x != y for x, y in zip(a, b)), "doutes": doutes[g],
                            "palier_section_10_5": palier}
    vrai = {n: ("bien-noté" if classe[table[n]] == "bien-note" else "peu-noté") for n in neutres}
    res["aveugle"] = {nom: {"paris_justes": sum(1 for n, l in A.items() if l["pari_statut"] == vrai[n]),
                            "paris_faux": sum(1 for n, l in A.items() if l["pari_statut"] not in ("ne-sait-pas", vrai[n])),
                            "ne_sait_pas": sum(1 for l in A.values() if l["pari_statut"] == "ne-sait-pas"),
                            "reconnus": sum(1 for l in A.values() if l["reconnu"])}
                      for nom, A in (("codeur_1", av1), ("codeur_2", av2))}
    if obj:
        o1, o2 = obj
        cles = sorted(o1)
        a, b = [o1[k] for k in cles], [o2[k] for k in cles]
        po, k = kappa(a, b)
        par = {}
        for c in CLASSES_O:
            par[c] = sum(1 for x, y in zip(a, b) if x != y and c in (x, y))
        res["objections"] = {"commentaires": len(cles), "accord_brut": po, "kappa": k, "desaccords": sum(x != y for x, y in zip(a, b)),
                             "desaccords_par_classe": par}
    return res


# ---------- essai synthétique ----------
def synthetique(gestes, man, rng):
    tenue = sorted(b["identifiant"] for b in man["billets"] if b["moitie"] == "tenue-a-l-ecart")
    table = {f"B{k:06d}": i for k, i in zip(rng.choice(10 ** 6, len(tenue), replace=False), tenue)}
    c1, c2, choix = {}, {}, {}
    for n in table:
        for g, G in gestes.items():
            mods = G["modalites"]
            v = mods[rng.integers(len(mods))]
            w = v if rng.random() < 0.8 else mods[rng.integers(len(mods))]
            c1[(n, g)], c2[(n, g)] = v, w
            if v != w:
                choix[(n, g)] = v if rng.random() < 0.5 else w
    av = [{n: {"reconnu": bool(rng.random() < 0.1), "pari_statut": list(PARIS)[rng.integers(3)]} for n in table} for _ in range(2)]
    inv = {v: k for k, v in table.items()}
    coms = {(inv[b["identifiant"]], f"c{j + 1:02d}") for b in man["billets"]
            if b["moitie"] == "tenue-a-l-ecart" and b["classe"] == "bien-note" for j in range(len(b["commentaires_retenus"]))}
    o1 = {k: CLASSES_O[rng.integers(14)] for k in sorted(coms)}
    o2 = {k: (o1[k] if rng.random() < 0.7 else CLASSES_O[rng.integers(14)]) for k in sorted(coms)}
    cho = {k: (o1[k] if rng.random() < 0.5 else o2[k]) for k in o1 if o1[k] != o2[k]}
    return table, c1, c2, choix, av, (o1, o2, cho)


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    for a in ("grille", "manifeste", "table", "marques1", "marques2", "codeur1", "codeur2", "arbitre-gestes",
              "obj1", "obj2", "arbitre-objections", "codables", "pilote", "sortie"):
        ap.add_argument("--" + a)
    ap.add_argument("--essai-synthetique", action="store_true")
    A = ap.parse_args()
    gestes = lire_grille(A.grille)
    man = json.load(open(A.manifeste, encoding="utf-8"))
    res = {}
    if A.pilote:
        table = json.load(open(A.table, encoding="utf-8"))["neutre_vers_site"]
        if set(table.values()) != set(json.load(open(A.pilote, encoding="utf-8"))["billets"]):
            raise Refus("pilote : la table ne couvre pas exactement la liste pilote")
        L1, L2 = lire_jsonl(A.codeur1), lire_jsonl(A.codeur2)
        c1, av1 = gestes_et_aveugle(L1, gestes, set(table), "codeur 1")
        c2, av2 = gestes_et_aveugle(L2, gestes, set(table), "codeur 2")
        obj = None
        if A.obj1:
            cod = json.load(open(A.codables, encoding="utf-8"))["codables"]
            att = {(b, c) for b, cs in cod.items() for c in cs}
            obj = (objections(lire_jsonl(A.obj1), att, "objections 1"), objections(lire_jsonl(A.obj2), att, "objections 2"))
        res = analyser_pilote(gestes, table, c1, c2, av1, av2, L1, L2, man, obj)
    else:
        m1 = {d["identifiant"] for d in json.load(open(A.marques1, encoding="utf-8"))["marques"]}
        m2 = {d["identifiant"] for d in json.load(open(A.marques2, encoding="utf-8"))["desaccords_dans_le_corpus"]}
        if A.essai_synthetique:
            rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE).spawn(5)[4])
            table, c1, c2, choix, (av1, av2), (o1, o2, cho) = synthetique(gestes, man, rng)
            ar = construire_arbitrage(c1, c2, choix, None, "arbitre")
            obj = (o1, o2, construire_arbitrage(o1, o2, cho, None, "arbitre objections"))
        else:
            table = json.load(open(A.table, encoding="utf-8"))["neutre_vers_site"]
            c1, av1 = gestes_et_aveugle(lire_jsonl(A.codeur1), gestes, set(table), "codeur 1")
            c2, av2 = gestes_et_aveugle(lire_jsonl(A.codeur2), gestes, set(table), "codeur 2")
            choix = {(l["billet"], l["geste"]): l["modalite"] for l in lire_jsonl(A.arbitre_gestes)}
            ar = construire_arbitrage(c1, c2, choix, None, "arbitre des gestes")
            obj = None
            if A.obj1:
                cod = json.load(open(A.codables, encoding="utf-8"))["codables"]
                att = {(b, c) for b, cs in cod.items() for c in cs}
                o1 = objections(lire_jsonl(A.obj1), att, "objections 1")
                o2 = objections(lire_jsonl(A.obj2), att, "objections 2")
                cho = {(l["billet"], l["commentaire"]): l["classe"] for l in lire_jsonl(A.arbitre_objections)}
                obj = (o1, o2, construire_arbitrage(o1, o2, cho, None, "arbitre des objections"))
        res = analyser(gestes, man, table, m1, m2, c1, c2, ar, av1, av2, obj)
        res["marques"] = {"marquage_1": A.marques1, "marquage_2": A.marques2}
    res["entrees"] = {k: {"chemin": getattr(A, k), "sha256": sha(getattr(A, k))}
                      for k in ("grille", "manifeste", "marques1", "marques2", "pilote") if getattr(A, k)}
    res["synthetique"] = bool(A.essai_synthetique)
    res["entropie"], res["numpy"] = ENTROPIE, np.__version__
    with open(A.sortie, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, default=float)
        f.write("\n")
    print("écrit", A.sortie)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (Refus, RefusControle) as e:
        print("REFUS :", e)
        sys.exit(2)
