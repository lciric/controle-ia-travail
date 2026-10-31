"""Diagnostic de plomberie de l'échec de V5 (expérience v2 de bisociation à deux espaces) — v1.

Mondes d'essai SEULEMENT : RACINE_VALIDATION, indices 990000 à 990199 (hors de toute plage du § 7 du texte scellé :
validation 0 à 299, étape (1) 300 à 499, reproduction NR 0 à 1199, décision sous RACINE ; hors des plages d'essai déjà
employées 920000+, 930000+, 950000-956009, 960000-960002, 970000-972399, 980000-980059). Conditions M_bien et M_moyen.

Ne modifie aucun module : `monde_v2`, `validation_v2` sont importés tels quels ; les variantes de générateur sont des
remplacements EN MÉMOIRE de deux fonctions de `monde_v2` dans ce seul processus (restaurées après chaque variante).
Aucun bras, aucune précision, aucun contraste n'est calculé ; seule la grandeur de V5 et sa décomposition.

Usage : PYTHONPATH=<dépôt>/src python3 -B diagnostic_v5_v1.py > diagnostic-v5-v1-sortie.txt
"""
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

EXP = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(EXP))
import graines_v2 as gr  # noqa: E402
import monde_v2 as mo  # noqa: E402
import validation_v2 as va  # noqa: E402
from monde_v2 import JETON_MESURE  # noqa: E402

INDICES = range(990000, 990200)
RACINE = gr.RACINE_VALIDATION
CONDITIONS = ("M_bien", "M_moyen")
SEUIL_V5 = va.S13["V5"]
STATUTS = list(va.STATUTS_V5)
RARES3 = ("vrai_conceptuel", "faux", "proche")

# garde : aucune plage du § 7 ni plage d'essai déjà employée
for a, b in ((0, 1200), (920000, 931000), (950000, 956010), (960000, 960003), (970000, 972400), (980000, 980060)):
    assert not (set(INDICES) & set(range(a, b))), (a, b)


# --- outils ---------------------------------------------------------------------------------------------------

def cle_statut(st):
    for k, sts in va.STATUTS_V5.items():
        if st in sts:
            return k
    raise KeyError(st)


def type_etiquette(m, st, pl):
    if m.startswith("op:j"):
        return "op_exclusif_jumeau"
    if m.startswith("op:e"):
        return "op_exclusif_surface_variante"
    if m.startswith("op:s"):
        return "op_exclusif_solo"
    if m.startswith("op:h"):
        return "repli_moyeu_op"
    if m.startswith("op:g"):
        if st == "greffe" and m == "op:" + pl["op"]:
            return "op_groupe_greffe_plante"
        if st == "surface" and m == "op:" + str(pl.get("o_b")):
            return "op_groupe_homonyme_plante"
        return "op_groupe_autre"
    if m == "co:H":
        return "repli_moyeu_concept"
    if m.startswith("co:F"):
        return "repli_fond"
    if m.startswith("co:R"):
        return "co_rare_plante" if pl.get("rare") is not None and m == "co:R%d" % pl["rare"] else "co_rare_autre"
    return "autre"


def generer_tous(cond, surcharge=None):
    out = []
    for i in INDICES:
        if VARIANTE["actif"]:
            VARIANTE["rng"] = np.random.default_rng(np.random.SeedSequence(entropy=RACINE, spawn_key=(i, 7777)))
        out.append(mo.generer(cond, RACINE, i, surcharge))
    return out


def lignes_ponts(ws):
    """Une ligne par pont planté valide : statut V5, statut fin, type de l'étiquette retenue, df, et grandeurs."""
    L_ = []
    for w in ws:
        obs, L = w.obs, w.latent(JETON_MESURE)
        pl_de = {(min(p["a"], p["b"]), max(p["a"], p["b"])): p for p in L.plantes}
        val = set(obs.valides)
        for x, st in L.plante.items():
            if x not in val:
                continue
            p = pl_de[obs.paires[x]]
            i, j = obs.paires[x]
            m = obs.pont[x]
            ei = obs.etiq_op[i] | obs.etiq_co[i]
            ej = obs.etiq_op[j] | obs.etiq_co[j]
            fin = st + ("" if st not in ("greffe", "jumeau") else ("+trace" if p.get("rare") is not None else "-trace"))
            r_lab = "co:R%d" % p["rare"] if p.get("rare") is not None else None
            L_.append({
                "v5": cle_statut(st), "fin": fin, "type": type_etiquette(m, st, p), "df": obs.df[m],
                "n_partagees": len(ei & ej), "degre": (len(ei) + len(ej)) / 2,
                "rare_vu_des_deux": bool(r_lab and r_lab in ei and r_lab in ej),
                "df_rare_plante": obs.df.get(r_lab) if r_lab and r_lab in ei and r_lab in ej else None,
                "meme_champ": L.champ[L.arts[i]["dom"]] == L.champ[L.arts[j]["dom"]],
            })
    return L_


def ecart(moy, statuts):
    v = [moy[s] for s in statuts]
    return max(v) - min(v)


def fmt(moy):
    return " ; ".join(f"{k} {moy[k]:.3f}" for k in moy)


def v5_et_ecarts(ws, titre):
    r = va.v5_rarete(ws)  # la fonction scellée, telle quelle
    moy = r["moyennes"]
    e3 = ecart(moy, RARES3)
    print(f"  {titre} : V5 écart 5 statuts = {r['ecart_max']:.4f} "
          f"({'≤' if r['ecart_max'] <= SEUIL_V5 else '>'} {SEUIL_V5}) ; écart des 3 statuts à concept rare = {e3:.4f}")
    print(f"    moyennes : {fmt(moy)}")
    return r["ecart_max"], e3, moy


# --- variantes de générateur, en mémoire ---------------------------------------------------------------------

VARIANTE = {"actif": False, "jumeau": False, "surface": False, "rng": None}
_ORIG_ATTRIBUER = mo._attribuer_rares
_ORIG_OBSERVER = mo._observer_operateurs


def _attribuer_variante(rng, p, plantes, n_arts):
    """Appelle la fonction d'origine, puis, avec un flux À PART (clé (indice, 7777), hors § 7), donne aux étiquettes
    d'opérateur de pont la loi S16d : L ~ uniforme{2,3,4}, L − 2 émetteurs de surface parmi les 38 autres articles.
    jumeau : étiquette j{t} ; surface : étiquette homonyme EXCLUSIVE e{t} (au lieu de l'opérateur o_b)."""
    rares = _ORIG_ATTRIBUER(rng, p, plantes, n_arts)
    g = VARIANTE["rng"]
    VARIANTE["emetteurs"] = []
    t_j = t_e = 0
    for pl in plantes:
        if pl["statut"] == "jumeau" and VARIANTE["jumeau"]:
            lab = pl["op"]
            t_j += 1
        elif pl["statut"] == "surface" and VARIANTE["surface"]:
            lab = f"e{t_e}"
            pl["lab_variante"] = lab
            t_e += 1
        else:
            continue
        L = int(g.choice(mo.S16["loi_emetteurs"]))
        autres = [i for i in range(n_arts) if i not in (pl["a"], pl["b"])]
        VARIANTE["emetteurs"].append((lab, [autres[int(k)] for k in g.choice(len(autres), size=L - 2, replace=False)]))
    return rares


def _observer_variante(rng, p, arts, champ, groupe, n_groupes, ops_groupe, forces):
    """Copie de monde_v2._observer_operateurs (même ordre de tirages) avec deux ajouts : (1) les articles émetteurs de
    surface d'une étiquette d'opérateur de pont émettent un mot de cette étiquette (sans la porter en latent) ;
    (2) en variante « surface », le mot forcé du pont de surface t est étiqueté e{t} (exclusif) au lieu de o_b."""
    for a in arts:
        a.setdefault("ops_surface", [])
    b = dict(mo.mo.BASE)
    couverture, p_parasite, p_homonyme = mo.mo.NIVEAUX[p["niveau"]]
    k = len(champ)
    mot = {}

    def mots_de(op, d):
        cle_d = None if op.startswith("h") else d
        return [mot.setdefault((op, cle_d, i), f"w_{op}_{cle_d}_{i}") for i in range(2)]

    homonymes = {}
    combos = sorted({(a["dom"], o) for a in arts for o in a["ops"] if o.startswith("g")})
    for d, o in combos:
        if groupe[d] != int(o[1:o.index("o")]) or rng.random() >= p_homonyme:
            continue
        g2 = rng.choice([g for g in range(n_groupes) if g != groupe[d]])
        m2 = rng.choice(ops_groupe[g2])
        d2 = rng.choice([x for x in range(k) if groupe[x] == g2])
        partage = mots_de(m2, d2)[0]
        mot[(o, d, 0)] = partage
        homonymes[partage] = m2
    for t, (o_a, d_a, o_b, d_b) in enumerate(forces):
        w = mots_de(o_b, d_b)[0]
        mot[(o_a, d_a, 0)] = mot[(o_a, d_a, 1)] = w
        mot[(o_b, d_b, 1)] = w
        homonymes[w] = f"e{t}" if VARIANTE["surface"] else o_b
    lexique, zipf = {}, mo.mo._zipf(b["vocab_general"], b["zipf_general"])

    def dans_lexique(w, canon, cov):
        if w not in lexique:
            lexique[w] = canon if rng.random() < cov else None
        return lexique[w]

    labels_fond = [o for g in range(n_groupes) for o in ops_groupe[g]]
    for a in arts:
        sac, etiq = [], {}
        for o in a["ops"] + a["moyeux"] + a["ops_surface"]:
            w = rng.choice(mots_de(o, a["dom"]))
            canon = homonymes.get(w, o)
            cov = b["couverture_moyeu"] if o.startswith("h") else couverture
            lab = dans_lexique(w, canon, cov)
            if lab is None:
                sac.append(w)
            else:
                prov = "moyeu" if lab.startswith("h") else ("vrai" if lab in a["ops"] else "homonyme")
                if etiq.get(lab) != "vrai":
                    etiq[lab] = prov
        if rng.random() < p_parasite:
            lab = rng.choice(labels_fond)
            if lab not in etiq:
                etiq[lab] = "vrai" if lab in a["ops"] else "parasite"
        for _ in range(b["mots_domaine"]):
            u = rng.random()
            if u < b["p_mot_global"]:
                sac.append(f"x{rng.randrange(b['vocab_global'])}")
            elif u < b["p_mot_global"] + b["p_mot_champ"]:
                sac.append(f"c{a['champ']}_{rng.randrange(b['vocab_champ'])}")
            else:
                sac.append(f"d{a.get('dom_mots', a['dom'])}_{rng.randrange(b['vocab_propre'])}")
        sac += [f"z{x}" for x in rng.choices(range(b["vocab_general"]), weights=zipf, k=b["mots_generaux"])]
        a["sac_domaine"], a["etiq_op"] = sac, etiq
        if rng.random() < b["p_etiquette_domaine_fausse"]:
            voisins = [d for d in range(k) if champ[d] == a["champ"] and d != a["dom"]]
            a["dom_obs"] = rng.choice(voisins or [d for d in range(k) if d != a["dom"]])
        else:
            a["dom_obs"] = a["dom"]


# Les émetteurs sont tirés en indices d'AVANT le réordonnancement des articles ; `_attribuer_rares` ne reçoit pas
# les articles : on les capte par `_planter_v2` (appelé juste avant, sur la liste qui sera réordonnée) et on pose le
# champ `_ops_surface_variante` sur les dictionnaires d'articles, qui suivent le réordonnancement.
_ORIG_PLANTER = mo._planter_v2
_CAPTE = {}


def _planter_capte(rng, p, arts, champ, groupe, ops_groupe):
    _CAPTE["arts"] = arts
    return _ORIG_PLANTER(rng, p, arts, champ, groupe, ops_groupe)


def _attribuer_pose(rng, p, plantes, n_arts):
    rares = _attribuer_variante(rng, p, plantes, n_arts)
    arts = _CAPTE["arts"]
    for a in arts:
        a["_ops_surface_variante"] = []
    for lab, ems in VARIANTE["emetteurs"]:
        for e in ems:
            arts[e]["_ops_surface_variante"].append(lab)
    return rares


class Variante:
    def __init__(self, jumeau, surface):
        self.j, self.s = jumeau, surface

    def __enter__(self):
        VARIANTE.update(actif=True, jumeau=self.j, surface=self.s)
        mo._planter_v2 = _planter_capte
        mo._attribuer_rares = _attribuer_pose

        def observer(rng, p, arts, champ, groupe, n_groupes, ops_groupe, forces):
            for a in arts:
                a["ops_surface"] = list(a.get("_ops_surface_variante", []))
            _observer_variante(rng, p, arts, champ, groupe, n_groupes, ops_groupe, forces)

        mo._observer_operateurs = observer
        return self

    def __exit__(self, *exc):
        mo._planter_v2 = _ORIG_PLANTER
        mo._attribuer_rares = _ORIG_ATTRIBUER
        mo._observer_operateurs = _ORIG_OBSERVER
        VARIANTE.update(actif=False, jumeau=False, surface=False, rng=None)
        return False


# --- décomposition --------------------------------------------------------------------------------------------

def decomposer(lignes, titre):
    print(f"\n  Décomposition — {titre} (ponts plantés valides)")
    par_fin = defaultdict(list)
    for l_ in lignes:
        par_fin[l_["fin"]].append(l_)
    print("    statut fin           n    moy df  | part rare planté vu des deux | moy étiquettes partagées | degré moyen"
          " | part même champ")
    for f in sorted(par_fin):
        v = par_fin[f]
        print(f"    {f:18s} {len(v):5d}  {np.mean([x['df'] for x in v]):6.3f}  | "
              f"{np.mean([x['rare_vu_des_deux'] for x in v]):5.3f}                        | "
              f"{np.mean([x['n_partagees'] for x in v]):5.3f}                    | {np.mean([x['degre'] for x in v]):5.2f}"
              f"       | {np.mean([x['meme_champ'] for x in v]):4.2f}")
    print("    Composition par statut V5 : type d'étiquette retenue -> part ; df moyen")
    par_v5 = defaultdict(list)
    for l_ in lignes:
        par_v5[l_["v5"]].append(l_)
    for s in STATUTS:
        v = par_v5[s]
        c = Counter(x["type"] for x in v)
        moy_t = {t: np.mean([x["df"] for x in v if x["type"] == t]) for t in c}
        tot = np.mean([x["df"] for x in v])
        parts = ", ".join(f"{t} {c[t] / len(v):.3f} ; {moy_t[t]:.2f}" for t in sorted(c, key=lambda t: -c[t]))
        print(f"    {s:16s} (n={len(v)}, moyenne {tot:.3f}) : {parts}")
    # contribution du repli (fond, moyeux) : moyenne avec et sans repli
    print("    Moyenne par statut V5 sans les ponts dont l'étiquette retenue est un repli (fond, moyeu op, moyeu concept),"
          " et part de repli :")
    moy_sans = {}
    for s in STATUTS:
        v = par_v5[s]
        sans = [x["df"] for x in v if not x["type"].startswith("repli")]
        moy_sans[s] = float(np.mean(sans))
        print(f"      {s:16s} part repli {1 - len(sans) / len(v):.3f} ; moyenne sans repli {moy_sans[s]:.3f}")
    print(f"      écart 5 statuts sans repli {ecart(moy_sans, STATUTS):.4f} ; 3 statuts à concept rare sans repli "
          f"{ecart(moy_sans, RARES3):.4f}")
    return par_v5


def lecture_texte_T2(lignes, titre):
    """Variante de TEXTE T2 : fréquence documentaire observée de l'étiquette du concept rare PLANTÉ, sur les ponts
    plantés valides où les deux articles l'observent, par statut portant un concept rare (vrai conceptuel, faux,
    proche, vrai d'opérateur avec trace). C'est la grandeur que S16d égalise."""
    acc = defaultdict(list)
    for l_ in lignes:
        if l_["df_rare_plante"] is not None:
            k = l_["v5"] if l_["v5"] != "vrai_operateur" else "vrai_operateur_avec_trace"
            acc[k].append(l_["df_rare_plante"])
    moy = {k: float(np.mean(v)) for k, v in acc.items()}
    print(f"  T2 ({titre}) : df du concept rare planté, vu des deux côtés : {fmt(moy)} ; "
          f"écart = {ecart(moy, list(moy)):.4f} (n : {', '.join(f'{k} {len(v)}' for k, v in acc.items())})")
    return ecart(moy, list(moy))


def lecture_texte_T3(lignes, titre):
    """Variante de TEXTE T3 (rapportée, non proposée comme seuil) : médiane au lieu de moyenne, 5 statuts."""
    par = defaultdict(list)
    for l_ in lignes:
        par[l_["v5"]].append(l_["df"])
    med = {s: float(np.median(par[s])) for s in STATUTS}
    print(f"  T3 ({titre}) : médianes {fmt(med)} ; écart {ecart(med, STATUTS):.4f}")


# --- programme ------------------------------------------------------------------------------------------------

def main():
    print("Diagnostic V5 v1 — mondes d'essai RACINE_VALIDATION indices 990000-990199 ; seuil S13 V5 =", SEUIL_V5)
    resume = {}
    lig_base = {}
    print("\n=== (A) Générateur scellé, tel quel ===")
    for cond in CONDITIONS:
        ws = generer_tous(cond)
        resume[("base", cond)] = v5_et_ecarts(ws, cond)
        lig_base[cond] = lignes_ponts(ws)
        decomposer(lig_base[cond], cond)

    print("\n=== (B) Hypothèses par surcharge de paramètres (generer(..., surcharge=...)) ===")
    sans_jumeaux = dict(mo.S16["ponts"], jumeaux=0)
    for nom, sc in (("H1 sans jumeaux (vrai d'opérateur = greffes seules)", {"ponts": sans_jumeaux}),
                    ("H2 lambda = 0 (aucune trace conceptuelle sur les ponts d'opérateur)", {"lambda": 0.0}),
                    ("H2' lambda = 1 (trace toujours)", {"lambda": 1.0}),
                    ("H3 sans concept moyeu (p_moyeu_concept = 0 : moins de repli)", {"p_moyeu_concept": 0.0})):
        print(f" {nom}")
        for cond in CONDITIONS:
            resume[(nom, cond)] = v5_et_ecarts(generer_tous(cond, sc), cond)

    print("\n=== (C) Variantes de générateur en mémoire (loi S16d donnée aux étiquettes d'opérateur de pont) ===")
    for nom, j, s in (("G1 jumeau j{t} à émetteurs S16d", True, False),
                      ("G2 surface : homonyme exclusif e{t} à émetteurs S16d", False, True),
                      ("G3 = G1 + G2", True, True)):
        print(f" {nom}")
        with Variante(j, s):
            for cond in CONDITIONS:
                ws = generer_tous(cond)
                resume[(nom, cond)] = v5_et_ecarts(ws, cond)
                if nom.startswith("G3"):
                    decomposer(lignes_ponts(ws), f"{cond}, G3")
    nom = "H4 (décomposition seulement, hors options : lambda=0 est exclu par S16a) G3 + lambda = 0"
    print(f" {nom}")
    with Variante(True, True):
        for cond in CONDITIONS:
            resume[(nom, cond)] = v5_et_ecarts(generer_tous(cond, {"lambda": 0.0}), cond)
    # contrôle : restauration
    assert mo._attribuer_rares is _ORIG_ATTRIBUER and mo._observer_operateurs is _ORIG_OBSERVER
    assert mo._planter_v2 is _ORIG_PLANTER
    ws = generer_tous("M_bien")
    e_apres = va.v5_rarete(ws)["ecart_max"]
    print(f" contrôle de restauration : écart M_bien après variantes = {e_apres:.4f} "
          f"(égal à (A) : {abs(e_apres - resume[('base', 'M_bien')][0]) < 1e-12})")

    print("\n=== (D) Variantes du TEXTE de V5, sur les mondes de (A) ===")
    for cond in CONDITIONS:
        e5, e3, moy = resume[("base", cond)]
        print(f"  T1 ({cond}) : V5 restreinte aux 3 statuts à concept rare : écart = {e3:.4f}")
        lecture_texte_T2(lig_base[cond], cond)
        lecture_texte_T3(lig_base[cond], cond)

    print("\n=== (F) Bruit d'échantillonnage de la statistique (erreur type naïve sd/racine(n), ponts supposés"
          " indépendants ; 200 mondes) ===")
    for cond in CONDITIONS:
        par = defaultdict(list)
        for l_ in lig_base[cond]:
            par[l_["v5"]].append(l_["df"])
        et = {s: float(np.std(par[s], ddof=1) / np.sqrt(len(par[s]))) for s in STATUTS}
        print(f"  {cond} : erreur type par statut : {fmt(et)}")
        for a_, b_ in (("vrai_conceptuel", "faux"), ("vrai_conceptuel", "proche"), ("faux", "proche")):
            print(f"    erreur type de la différence {a_} - {b_} : {np.hypot(et[a_], et[b_]):.3f}")
        t2 = defaultdict(list)
        for l_ in lig_base[cond]:
            if l_["df_rare_plante"] is not None:
                t2[l_["v5"]].append(l_["df_rare_plante"])
        print("    T2, erreur type par statut : " + " ; ".join(
            f"{k} {np.std(v, ddof=1) / np.sqrt(len(v)):.3f}" for k, v in t2.items()))

    print("\n=== (E) Résumé ===")
    print("  variante                                                       M_bien 5 st. | 3 rares || M_moyen 5 st. | 3 rares")
    for nom in dict.fromkeys(k[0] for k in resume):
        b, m = resume[(nom, "M_bien")], resume[(nom, "M_moyen")]
        print(f"  {nom[:62]:62s} {b[0]:7.4f}     | {b[1]:6.4f}  || {m[0]:7.4f}      | {m[1]:6.4f}")


if __name__ == "__main__":
    main()
