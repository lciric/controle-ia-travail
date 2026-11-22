"""Diagnostic de fuite de la banque d'énoncés plantés, version 6 du générateur (« mathématiques nouvelles ») — v1.

Pièce d'instrument (classe B). Vérificateur : Opus 5.5, session neuve, le 2026-11-22. Processeur seul ; aucun appel de
modèle ; aucune dépense ; aucun réseau. Racines d'essai déjà exposées SEULEMENT : 0 à 39 et 20261122 (41 racines). Aucune
banque réelle, aucun fichier de clé versé n'est ouvert : les banques et les sous-banques d'essai sont régénérées en
mémoire par le paquet figé `src/controle_ia/oracles_plantes_v6/` (lu, jamais modifié).

Ce script est écrit indépendamment du script de la première passe (`juge-fable-max-v1-diagnostic-style.py`) : découpeur,
classifieur bayésien naïf, aire, rappel à fausses alarmes plafonnées et règle des chiffres sont réécrits ici, puis
confrontés au paquet (découpeur et score identiques à l'octet, aire qui fait foi identique à `forme_seule.mesurer`).

Parties (liste a à h du juge Opus, § 2.2 point 1, et ajouts du juge Fable, § 3.2 point 1) :
  V  vérification des nombres du § 2 du jugement Fable ;
  a  table gabarit × strate × famille (banque et sous-banque), un texte d'exemple par gabarit ;
  b  jetons aux plus forts rapports de vraisemblance, par famille ;
  c  aire et rappel à fausses alarmes <= 0,10 (blocs d'ex æquo entiers, aucun tirage) ; deux réglages du seuil ;
  d  classifieur sur l'identifiant de gabarit / de famille ; style à l'intérieur des gabarits ; style sur gabarits tenus
     à l'écart ;
  e  sonde numérique prototype (littéraux seulement), même validation croisée par mondes entiers ;
  f  contrôle de chaîne ;
  g  profil des témoins des faux dans [0 .. 3N] ; règle A ; 3N seul ; instances saillantes ;
  h  puissance de la lecture en preuve (E1, E2, E4) par simulation.

Graines (R9) : les banques viennent de l'arbre du paquet (racines d'essai). Les seuls tirages propres à ce script sont
le rééchantillonnage des racines (intervalles à 90 %) et la simulation de puissance ; ils viennent de
`numpy.random.SeedSequence(20261122, spawn_key=(1000 + i,))`, i = 0 (rééchantillonnage), i = 1 (puissance) — enfants
hors de l'arbre du paquet (qui n'a que 0 à 10), consignés dans la sortie.

Emploi (depuis la racine de l'arbre `maths`) :
  PYTHONPATH=src python3 docs/notes/.../diagnostic-opus-v1/diagnostic-fuite-v6-opus-v1.py SORTIE.json > SORTIE.txt
"""
from __future__ import annotations

import bisect
import hashlib
import json
import math
import re
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

import numpy as np

from controle_ia.oracles_plantes_v6 import banque as pk_banque
from controle_ia.oracles_plantes_v6 import parametres as pk_parametres
from controle_ia.oracles_plantes_v6.evaluation import parcourir, prefixe
from controle_ia.oracles_plantes_v6.exact import HorsCapacite, Indefini
from controle_ia.oracles_plantes_v6.forme_seule import BayesNaif, jetons_de_style, mesurer, regle_forme_seule
from controle_ia.oracles_plantes_v6.graines import generateur
from controle_ia.oracles_plantes_v6.grammaire import lexer
from controle_ia.oracles_plantes_v6.sous_banque import identifiants_opaques, tirer_sous_banque
from controle_ia.oracles_plantes_v6.tests_de_mort import verifier_instance

RACINES = list(range(40)) + [20261122]
ANALYS = ("VERITE_PLANTEE", "FAUX_TOT", "PIEGE")
V, FT, PG = ANALYS
FAMILLES = ("F1", "F2", "F3")
PLIS = 4
FA10 = Fraction(1, 10)
FA05 = Fraction(1, 20)
GRAINE_SCRIPT = 20261122
T0 = time.time()


def journal(msg):
    print(f"[{time.time() - T0:7.1f} s] {msg}", file=sys.stderr, flush=True)


# =============================================================================== outils statistiques (réécrits)
def aire(pos, neg):
    """Mann-Whitney exact : P(pos > neg) + 1/2 P(égalité). Scores comparables exactement (Fraction ou flottants)."""
    if not pos or not neg:
        return None
    sn = sorted(neg)
    s = Fraction(0)
    for p in pos:
        lo = bisect.bisect_left(sn, p)
        hi = bisect.bisect_right(sn, p)
        s += lo + Fraction(hi - lo, 2)
    return s / (len(pos) * len(neg))


def rappel_plafonne(pos, neg, plafond):
    """Rappel maximal sur `pos` sous fausses alarmes <= plafond sur `neg`, seuil choisi parmi les scores, règle
    « positif si score >= s » : un bloc d'ex æquo est franchi entier ou pas du tout ; aucun tirage. Rend (rappel, fa)."""
    if not pos or not neg:
        return None, None
    sp, sn = sorted(pos), sorted(neg)
    meilleur = (Fraction(0), Fraction(0))
    for s in sorted(set(pos) | set(neg)):
        fa = Fraction(len(sn) - bisect.bisect_left(sn, s), len(sn))
        if fa <= plafond:
            r = Fraction(len(sp) - bisect.bisect_left(sp, s), len(sp))
            if r > meilleur[0] or (r == meilleur[0] and fa < meilleur[1]):
                meilleur = (r, fa)
    return meilleur


def seuil_regle(neg_calib, plafond):
    """Seuil réglé sur des vrais de calibrage : plus grande valeur v* telle que la part des vrais de score >= v*
    dépasse le plafond ; on déclare « faux » si score > v* (bloc d'ex æquo entier). None : aucun bloc ne dépasse."""
    sn = sorted(neg_calib)
    n = len(sn)
    vstar = None
    for v in sorted(set(sn)):
        if Fraction(n - bisect.bisect_left(sn, v), n) > plafond:
            vstar = v
    return vstar


def f(x, nd=10):
    return None if x is None else round(float(x), nd)


def resume(vals):
    v = [float(x) for x in vals if x is not None]
    if not v:
        return None
    a = np.array(v)
    return {"n": len(v), "min": round(float(a.min()), 4), "moyenne": round(float(a.mean()), 4),
            "mediane": round(float(np.median(a)), 4), "max": round(float(a.max()), 4)}


def intervalle_moyenne(vals, rng, tirages=2000):
    v = np.array([float(x) for x in vals if x is not None])
    if len(v) == 0:
        return None
    idx = rng.integers(0, len(v), size=(tirages, len(v)))
    m = v[idx].mean(axis=1)
    return [round(float(np.quantile(m, 0.05)), 4), round(float(np.quantile(m, 0.95)), 4)]


# =============================================================================== découpeur et bayésien naïf (réécrits)
_JET = re.compile(r"\d+\.\d+|\d+|[A-Za-z_][A-Za-z0-9_]*|\.\.|<=|>=|!=|[=<>+\-*/^(),\[\]]")


def jetons_bruts(texte):
    return _JET.findall(texte)


def jetons_style(texte, mode="NUM"):
    """mode « NUM » : nombres masqués (classifieur du paquet) ; mode « LONG » : nombre remplacé par sa longueur."""
    toks = []
    for t in jetons_bruts(texte):
        if t[0].isdigit():
            toks.append("NUM" if mode == "NUM" else f"NUM{len(t)}")
        else:
            toks.append(t)
    return toks + [f"{a}·{b}" for a, b in zip(toks, toks[1:])]


class BN:
    """Bayésien naïf multinomial, lissage de Laplace 1, rationnels exacts ; « faux » = True."""

    def __init__(self, listes, ys):
        self.c = {True: Counter(), False: Counter()}
        self.n = {True: 0, False: 0}
        voc = set()
        for js, y in zip(listes, ys):
            self.n[y] += 1
            self.c[y].update(js)
            voc.update(js)
        self.V = len(voc) + 1
        self.T = {y: sum(self.c[y].values()) for y in (True, False)}
        self.dF = self.T[True] + self.V
        self.dV = self.T[False] + self.V
        self.r0 = Fraction(self.n[True] + 1, self.n[False] + 1)
        self._cache = {}

    def rapport(self, j):
        r = self._cache.get(j)
        if r is None:
            r = Fraction((self.c[True].get(j, 0) + 1) * self.dV, (self.c[False].get(j, 0) + 1) * self.dF)
            self._cache[j] = r
        return r

    def score(self, js):
        r = self.r0
        for j in js:
            r *= self.rapport(j)
        return r

    def log_rapports(self):
        return {j: math.log(self.rapport(j)) for j in set(self.c[True]) | set(self.c[False])}


# =============================================================================== littéraux et sonde numérique
def litteraux(texte):
    """Littéraux de l'énoncé, lus sur les jetons seuls : « ( a / b ) », « ( - a / b ) », « ( - a ) » donnent un
    rationnel ; tout autre nombre isolé est un entier. Rend [(valeur Fraction, est_fraction, chiffres_num, chiffres_den)]."""
    t = jetons_bruts(texte)
    out, i = [], 0
    while i < len(t):
        if t[i] == "(":
            # ( - a / b ) ou ( a / b ) ou ( - a )
            j, signe = i + 1, 1
            if j < len(t) and t[j] == "-":
                signe, j = -1, j + 1
            if j + 3 < len(t) + 1 and j < len(t) and t[j].isdigit():
                if j + 3 < len(t) and t[j + 1] == "/" and t[j + 2].isdigit() and t[j + 3] == ")":
                    out.append((signe * Fraction(int(t[j]), int(t[j + 2])), True, len(t[j]), len(t[j + 2])))
                    i = j + 4
                    continue
                if signe == -1 and j + 1 < len(t) and t[j + 1] == ")":
                    out.append((Fraction(-int(t[j])), False, len(t[j]), 1))
                    i = j + 2
                    continue
        if t[i][0].isdigit():
            out.append((Fraction(t[i]), False, len(t[i]), 1))
        i += 1
    return out


NOMS_NUM = ["nb_litteraux", "nb_fractions", "nb_zero", "nb_un", "nb_deux", "log10_max_numerateur",
            "log10_max_denominateur", "log10_max_valeur", "chiffres_max", "frac_entre_0_et_1", "nb_egal_constante",
            "nb_au_dessus_3N", "nb_entre_N_et_3N", "nb_au_dessus_constantes", "log10_max_sur_N"]


def traits_numeriques(texte, monde):
    L = litteraux(texte)
    csts = sorted({abs(v) for v in monde.constantes().values()})
    N, N3 = monde.N, 3 * monde.N
    cmax = max(csts)
    vals = [abs(v) for v, *_ in L]
    if not L:
        return [0.0] * len(NOMS_NUM)
    return [
        len(L), sum(1 for x in L if x[1]),
        sum(1 for v in vals if v == 0), sum(1 for v in vals if v == 1), sum(1 for v in vals if v == 2),
        max(math.log10(abs(v.numerator) + 1) for v, *_ in L),
        max(math.log10(v.denominator) for v, *_ in L),
        max(math.log10(float(v) + 1) for v in vals),
        max(max(a, b) for _v, _e, a, b in L),
        float(any(0 < v < 1 for v in vals)),
        sum(1 for v in vals if v in csts),
        sum(1 for v in vals if v > N3), sum(1 for v in vals if N < v <= N3), sum(1 for v in vals if v > cmax),
        max(math.log10((float(v) + 1) / N) for v in vals),
    ]


class Logistique:
    """Régression logistique pénalisée (ridge, lambda = 1 sur traits centrés réduits), Newton exact, déterministe."""

    def __init__(self, X, y, lam=1.0, iters=50):
        X = np.asarray(X, float)
        self.mu = X.mean(axis=0)
        self.sd = X.std(axis=0)
        self.sd[self.sd == 0] = 1.0
        Z = np.hstack([np.ones((len(X), 1)), (X - self.mu) / self.sd])
        y = np.asarray(y, float)
        w = np.zeros(Z.shape[1])
        P = lam * np.eye(Z.shape[1])
        P[0, 0] = 0.0
        for _ in range(iters):
            p = 1 / (1 + np.exp(-(Z @ w)))
            g = Z.T @ (p - y) + P @ w
            H = (Z * (p * (1 - p))[:, None]).T @ Z + P
            pas = np.linalg.solve(H, g)
            w -= pas
            if np.max(np.abs(pas)) < 1e-12:
                break
        self.w = w

    def score(self, X):
        X = np.asarray(X, float)
        Z = np.hstack([np.ones((len(X), 1)), (X - self.mu) / self.sd])
        # arrondi : des traits identiques donnent le même score exact (ex æquo vrais)
        return [round(float(s), 10) for s in Z @ self.w]


def chiffres_plus_grand_litteral(texte):
    return max((len(x) for x in re.findall(r"\d+", texte)), default=0)


# =============================================================================== instances : règle A, saillantes
def instance_uniforme(monde, arbre, a):
    """Variables NAT du préfixe à a ; variables bornées à la plus petite valeur de leur domaine (comme la règle A)."""
    pre, _ = prefixe(arbre)
    env, inst = {}, {}
    for var, dom in pre:
        if dom[0] == "NAT":
            x = a
        else:
            try:
                vals = monde.ev.valeurs_domaine(dom, env, borne=None)
            except (Indefini, HorsCapacite):
                return None
            if len(vals) == 0:
                return None
            x = vals[0]
        inst[var] = int(x)
        env[var] = Fraction(int(x))
    return inst


def touche(monde, arbre, inst):
    if inst is None:
        return False
    st, _ = verifier_instance(arbre, monde, inst, monde.borne_verification())
    return st == "verifie"


def regle_A(monde, arbre):
    vues, res = [], {}
    for nom, a in (("3N", monde.borne_verification()), ("1", 1), ("N+1", monde.N + 1)):
        inst = instance_uniforme(monde, arbre, a)
        if inst is None or inst in vues:
            res[nom] = False
            continue
        vues.append(inst)
        res[nom] = touche(monde, arbre, inst)
    return res


def valeurs_saillantes(monde, texte):
    N, N3 = monde.N, monde.borne_verification()
    base = {0, 1, 2, N, N + 1, 2 * N, N3}
    for t in jetons_bruts(texte):
        if t.isdigit():
            c = int(t)
            base |= {c - 1, c, c + 1}
    return sorted(v for v in base if 0 <= v <= N3)


def profil_instances(monde, arbre):
    """Toutes les instances du préfixe jusqu'à 3N : comptes, et valeurs du plus grand NAT où l'énoncé est faux."""
    N3 = monde.borne_verification()
    pre, _ = prefixe(arbre)
    nats = [v for v, d in pre if d[0] == "NAT"]
    n = nf = nh = 0
    nat_faux = set()
    premier = None
    try:
        for inst, st in parcourir(monde.ev, arbre, N3):
            n += 1
            if st in ("F", "I"):
                nf += 1
                m = max((int(inst[v]) for v in nats if v in inst), default=-1)
                nat_faux.add(m)
                if premier is None:
                    premier = {k: int(v) for k, v in inst.items()}
            elif st == "H":
                nh += 1
    except HorsCapacite:
        return {"hors_capacite": True}
    return {"n_instances": n, "n_fausses": nf, "n_hors_capacite": nh, "nat_max_des_fausses": sorted(nat_faux),
            "premiere_fausse": premier, "nb_variables_nat": len(nats), "nb_variables": len(pre)}


# =============================================================================== validation croisée générique
def plis_de(racine, nb_mondes):
    ordre = [int(i) for i in generateur(racine, 10, 0).permutation(nb_mondes)]
    return {w: k % PLIS for k, w in enumerate(ordre)}


def validation_croisee(items, pli_de, ajuster, noter, emboite=False):
    """items : dicts avec « w », « y » (faux = True), « cle ». Rend {cle: score}, {cle: vu (texte à l'apprentissage)},
    et, si `emboite`, {cle: déclaré faux au seuil transporté} : seuil réglé par validation interne sur les seuls mondes
    d'apprentissage (3 plis internes = les 3 autres plis externes), vrais internes à fausses alarmes <= 0,10."""
    scores, vus, decl = {}, {}, {}
    for k in range(PLIS):
        app = [x for x in items if pli_de[x["w"]] != k]
        test = [x for x in items if pli_de[x["w"]] == k]
        if not test:
            continue
        m = ajuster(app)
        textes_app = {x["texte"] for x in app}
        s = noter(m, test)
        for x, sc in zip(test, s):
            scores[x["cle"]] = sc
            vus[x["cle"]] = x["texte"] in textes_app
        if emboite:
            calib = []
            for j in range(PLIS):
                if j == k:
                    continue
                app2 = [x for x in app if pli_de[x["w"]] != j]
                tst2 = [x for x in app if pli_de[x["w"]] == j and not x["y"]]
                if tst2:
                    calib += noter(ajuster(app2), tst2)
            vstar = seuil_regle(calib, FA10)
            for x, sc in zip(test, s):
                decl[x["cle"]] = True if vstar is None else sc > vstar
    return scores, vus, decl


def comparaisons(items, scores, vus=None, decl=None):
    """Toutes les comparaisons demandées (c) sur des scores hors pli."""
    def sc(sel, hors_vus=False):
        return [scores[x["cle"]] for x in items if sel(x) and (not hors_vus or not vus[x["cle"]])]

    defs = {
        "tous_faux__tous_vrais": (lambda x: x["y"], lambda x: not x["y"]),
        "faux_tot__tous_vrais": (lambda x: x["etiquette"] == FT, lambda x: not x["y"]),
        "pieges__tous_vrais": (lambda x: x["etiquette"] == PG, lambda x: not x["y"]),
        # « vrais des mêmes gabarits » : sans objet (aucun gabarit n'a deux strates) ; substitut : même forme grossière
        "faux_tot_seuil__vrais_seuil": (lambda x: x["etiquette"] == FT and x["seuil"],
                                        lambda x: not x["y"] and x["seuil"]),
        "faux_tot_non_seuil__vrais_non_seuil": (lambda x: x["etiquette"] == FT and not x["seuil"],
                                                lambda x: not x["y"] and not x["seuil"]),
        "pieges__vrais_seuil": (lambda x: x["etiquette"] == PG, lambda x: not x["y"] and x["seuil"]),
        "pieges__faux_tot": (lambda x: x["etiquette"] == PG, lambda x: x["etiquette"] == FT),
    }
    for fam in FAMILLES:
        defs[f"famille_{fam}__faux__vrais"] = (lambda x, fam=fam: x["fam"] == fam and x["y"],
                                               lambda x, fam=fam: x["fam"] == fam and not x["y"])
        for et, nom in ((FT, "faux_tot"), (PG, "pieges")):
            defs[f"famille_{fam}__{nom}__vrais"] = (lambda x, fam=fam, et=et: x["fam"] == fam and x["etiquette"] == et,
                                                    lambda x, fam=fam: x["fam"] == fam and not x["y"])
    out = {}
    for nom, (sp, sn) in defs.items():
        pos, neg = sc(sp), sc(sn)
        r10, fa10 = rappel_plafonne(pos, neg, FA10)
        r05, _ = rappel_plafonne(pos, neg, FA05)
        d = {"n_pos": len(pos), "n_neg": len(neg), "aire": f(aire(pos, neg)), "rappel_fa10": f(r10),
             "fa_obtenue_fa10": f(fa10), "exces_fa10": None if r10 is None else f(r10 - FA10), "rappel_fa05": f(r05)}
        if vus is not None:
            d["aire_hors_vus"] = f(aire(sc(sp, True), sc(sn, True)))
        if decl and not nom.endswith("__faux_tot"):  # seuil réglé sur des vrais : sans objet contre les faux tôt
            pp = [decl[x["cle"]] for x in items if sp(x)]
            nn = [decl[x["cle"]] for x in items if sn(x)]
            d["seuil_transporte_rappel"] = f(Fraction(sum(pp), len(pp))) if pp else None
            d["seuil_transporte_fa"] = f(Fraction(sum(nn), len(nn))) if nn else None
        out[nom] = d
    return out


# =============================================================================== passe principale par racine
def gabarits_tenus_a_l_ecart(params):
    """4 groupes de gabarits, sans tirage : dans chaque famille et chaque strate, gabarits triés par nom, rang mod 4."""
    g = {}
    for fam in FAMILLES:
        G = params["gabarits"][fam]
        for cle in ("verites", "faux_tot", "pieges"):
            for i, nom in enumerate(sorted(G[cle])):
                g[(fam, nom)] = i % 4
    return g


def traiter_racine(r, params, groupe_gab):
    B = pk_banque.construire_banque(r, params)
    pli = plis_de(r, len(B))
    ids_mondes = identifiants_opaques(generateur(r, 3, 0), len(B), "monde-")
    servie, cle_sb = tirer_sous_banque(B, ids_mondes, r, params["sous_banque"])
    mondes = [m for m, _ in B]
    res = {"racine": r, "plis_par_monde": [pli[w] for w in range(len(B))]}
    # ---------------------------------------------------------------- items de la banque
    items = []
    temoins = []
    for w, (m, plantes) in enumerate(B):
        for p in plantes:
            if p.etiquette not in ANALYS:
                temoins.append(p)
                continue
            arbre = m.analyser(p.texte)
            items.append({"cle": (w, p.gabarit), "w": w, "fam": m.famille, "gabarit": p.gabarit,
                          "etiquette": p.etiquette, "y": p.etiquette != V, "texte": p.texte,
                          "seuil": bool(regle_forme_seule(arbre)), "monde": m, "arbre": arbre})
    # ---------------------------------------------------------------- f : chaîne
    chaine = {}
    ecarts_jetons = sum(1 for x in items if jetons_bruts(x["texte"]) != [v for _g, v in lexer(x["texte"])])
    ecarts_jetons += sum(1 for x in items if jetons_style(x["texte"]) != jetons_de_style(x["texte"]))
    chaine["jetons_differents_du_paquet"] = ecarts_jetons
    par_cle = {(ids_mondes[x["w"]], x["etiquette"], x["gabarit"]): x for x in items}
    enonce_servi = {it["identifiant"]: it for it in servie["items"]}
    sb_items, octets_diff, cles_servies = [], 0, set()
    for c in cle_sb["items"]:
        it = enonce_servi[c["identifiant"]]
        cles_servies |= set(it)
        if c["role"] != "analyse":
            continue
        x = par_cle[(c["identifiant_monde"], c["etiquette"], c["gabarit"])]
        if it["enonce"].encode("utf-8") != x["texte"].encode("utf-8"):
            octets_diff += 1
        sb_items.append(dict(x, cle=("sb",) + x["cle"], texte=it["enonce"]))
    chaine["sous_banque_items_analyses"] = len(sb_items)
    chaine["sous_banque_octets_differents_du_texte_plante"] = octets_diff
    chaine["cles_d_un_item_servi"] = sorted(cles_servies)
    chaine["cles_de_l_objet_servi"] = sorted(servie)
    # position de service et valeur de l'identifiant : rien ne doit prédire la strate
    pos = {it["identifiant"]: k for k, it in enumerate(servie["items"])}
    lab = {c["identifiant"]: c["etiquette"] for c in cle_sb["items"] if c["role"] == "analyse"}
    pf = [pos[i] for i, e in lab.items() if e != V]
    pv = [pos[i] for i, e in lab.items() if e == V]
    chaine["aire_position_de_service"] = f(aire(pf, pv))
    hf = [int(i[5:], 16) for i, e in lab.items() if e != V]
    hv = [int(i[5:], 16) for i, e in lab.items() if e == V]
    chaine["aire_valeur_identifiant"] = f(aire(hf, hv))
    chaine["aire_longueur_en_caracteres_banque"] = f(aire([len(x["texte"]) for x in items if x["y"]],
                                                          [len(x["texte"]) for x in items if not x["y"]]))
    chaine["aire_longueur_en_jetons_banque"] = f(aire([len(jetons_bruts(x["texte"])) for x in items if x["y"]],
                                                       [len(jetons_bruts(x["texte"])) for x in items if not x["y"]]))
    # plis : mondes d'un pli disjoints, et nombre de mondes d'apprentissage de la même famille que le pli de test
    fam_par_pli = defaultdict(list)
    for w, m in enumerate(mondes):
        fam_par_pli[pli[w]].append(m.famille)
    chaine["familles_par_pli"] = {str(k): sorted(v) for k, v in sorted(fam_par_pli.items())}
    chaine["mondes_d_apprentissage_meme_famille_par_monde_test"] = [
        sum(1 for w2, m2 in enumerate(mondes) if pli[w2] != pli[w] and m2.famille == m.famille)
        for w, m in enumerate(mondes)]
    # ---------------------------------------------------------------- classifieur de style (réécrit) : banque
    for x in items + sb_items:
        x["js"] = jetons_style(x["texte"])
        x["jsL"] = jetons_style(x["texte"], "LONG")

    def ajuster_bn(app, champ="js"):
        return BN([x[champ] for x in app], [x["y"] for x in app])

    def noter_bn(m, test, champ="js"):
        return [m.score(x[champ]) for x in test]

    sc_b, vu_b, dec_b = validation_croisee(items, pli, ajuster_bn, noter_bn, emboite=True)
    # contrôle : mon score = score du paquet, à l'octet, sur chaque pli
    diff_score = 0
    for k in range(PLIS):
        app = [x for x in items if pli[x["w"]] != k]
        mp = BayesNaif(Fraction(1)).apprendre([x["texte"] for x in app], [x["y"] for x in app])
        for x in items:
            if pli[x["w"]] == k and mp.score(x["texte"]) != sc_b[x["cle"]]:
                diff_score += 1
    chaine["scores_differents_du_paquet"] = diff_score
    off = mesurer(B, generateur(r, 10, 0), PLIS, Fraction(1))["classifieur_de_style"]
    chaine["plis_identiques_au_paquet"] = off["plis_par_monde"] == [pli[w] for w in range(len(B))]
    res["style_banque"] = comparaisons(items, sc_b, vu_b, dec_b)
    res["aire_qui_fait_foi_paquet"] = off["aire_qui_fait_foi"]
    a_p = res["style_banque"]["pieges__tous_vrais"]["aire_hors_vus"]
    a_f = res["style_banque"]["faux_tot__tous_vrais"]["aire_hors_vus"]
    res["aire_qui_fait_foi"] = max(a_p, a_f)
    chaine["aire_qui_fait_foi_egale_au_paquet"] = abs(res["aire_qui_fait_foi"] - float(Fraction(off["aire_qui_fait_foi"]))) < 1e-9
    res["effectifs_hors_vus"] = {e: sum(1 for x in items if x["etiquette"] == e and not vu_b[x["cle"]]) for e in ANALYS}
    # poids, définition de la première passe (pli 0, logarithme du rapport faux / vrai)
    app0 = [x for x in items if pli[x["w"]] != 0]
    poids_pli0 = BN([x["js"] for x in app0], [x["y"] for x in app0]).log_rapports()
    # ---------------------------------------------------------------- style : sous-banque
    sc_s, vu_s, dec_s = validation_croisee(sb_items, pli, ajuster_bn, noter_bn, emboite=True)
    res["style_sous_banque"] = comparaisons(sb_items, sc_s, vu_s, dec_s)
    # ---------------------------------------------------------------- e' : style avec la longueur des nombres
    sc_l, vu_l, _ = validation_croisee(items, pli, lambda a: ajuster_bn(a, "jsL"), lambda m, t: noter_bn(m, t, "jsL"))
    res["style_longueur_des_nombres_banque"] = comparaisons(items, sc_l, vu_l)
    # ---------------------------------------------------------------- d : identifiant de gabarit, de famille
    def ajuster_id(app, champ):
        c = defaultdict(lambda: [0, 0])
        for x in app:
            c[champ(x)][0] += int(x["y"])
            c[champ(x)][1] += 1
        return c

    for nom, champ in (("gabarit", lambda x: (x["fam"], x["gabarit"])), ("famille", lambda x: x["fam"])):
        sc_i, _, _ = validation_croisee(items, pli, lambda a, ch=champ: ajuster_id(a, ch),
                                        lambda m, t, ch=champ: [Fraction(m[ch(x)][0] + 1, m[ch(x)][1] + 2) for x in t])
        res[f"identifiant_{nom}_banque"] = comparaisons(items, sc_i)
        sc_i2, _, _ = validation_croisee(sb_items, pli, lambda a, ch=champ: ajuster_id(a, ch),
                                         lambda m, t, ch=champ: [Fraction(m[ch(x)][0] + 1, m[ch(x)][1] + 2) for x in t])
        res[f"identifiant_{nom}_sous_banque"] = comparaisons(sb_items, sc_i2)
    # style à l'intérieur de chaque gabarit : nombre de gabarits portant les deux classes
    par_gab = defaultdict(set)
    for x in items:
        par_gab[(x["fam"], x["gabarit"])].add(x["y"])
    res["gabarits_a_deux_classes"] = sum(1 for v in par_gab.values() if len(v) == 2)
    # style sur gabarits tenus à l'écart (tous mondes) : la forme se transporte-t-elle à des gabarits jamais vus ?
    sc_g = {}
    for g in range(4):
        app = [x for x in items if groupe_gab[(x["fam"], x["gabarit"])] != g]
        tst = [x for x in items if groupe_gab[(x["fam"], x["gabarit"])] == g]
        m = ajuster_bn(app)
        for x, s in zip(tst, noter_bn(m, tst)):
            sc_g[x["cle"]] = s
    res["style_gabarits_tenus_a_l_ecart_banque"] = comparaisons(items, sc_g)
    # et gabarits ET mondes tenus à l'écart (16 croisements)
    sc_gm = {}
    for g in range(4):
        for k in range(PLIS):
            app = [x for x in items if groupe_gab[(x["fam"], x["gabarit"])] != g and pli[x["w"]] != k]
            tst = [x for x in items if groupe_gab[(x["fam"], x["gabarit"])] == g and pli[x["w"]] == k]
            if not tst:
                continue
            m = ajuster_bn(app)
            for x, s in zip(tst, noter_bn(m, tst)):
                sc_gm[x["cle"]] = s
    res["style_gabarits_et_mondes_tenus_a_l_ecart_banque"] = comparaisons(items, sc_gm)
    # ---------------------------------------------------------------- e : sonde numérique
    for x in items + sb_items:
        x["num"] = traits_numeriques(x["texte"], x["monde"])

    def ajuster_num(app):
        return Logistique([x["num"] for x in app], [int(x["y"]) for x in app])

    def noter_num(m, t):
        return m.score([x["num"] for x in t])

    sc_n, vu_n, dec_n = validation_croisee(items, pli, ajuster_num, noter_num, emboite=True)
    res["numerique_banque"] = comparaisons(items, sc_n, vu_n, dec_n)
    sc_ns, vu_ns, dec_ns = validation_croisee(sb_items, pli, ajuster_num, noter_num, emboite=True)
    res["numerique_sous_banque"] = comparaisons(sb_items, sc_ns, vu_ns, dec_ns)
    poids_num = Logistique([x["num"] for x in items], [int(x["y"]) for x in items]).w.tolist()
    # règle sans apprentissage de la première passe
    sc_c = {x["cle"]: chiffres_plus_grand_litteral(x["texte"]) for x in items}
    res["chiffres_plus_grand_litteral_banque"] = comparaisons(items, sc_c)
    sc_cs = {x["cle"]: chiffres_plus_grand_litteral(x["texte"]) for x in sb_items}
    res["chiffres_plus_grand_litteral_sous_banque"] = comparaisons(sb_items, sc_cs)
    # ---------------------------------------------------------------- g : profil des témoins
    profils = []
    sb_cles = {x["cle"][1:] for x in sb_items}
    for x in items:
        if not x["y"]:
            continue
        m, arbre = x["monde"], x["arbre"]
        pr = profil_instances(m, arbre)
        A = regle_A(m, arbre)
        sal = [v for v in valeurs_saillantes(m, x["texte"]) if touche(m, arbre, instance_uniforme(m, arbre, v))]
        pr.update({"w": x["w"], "famille": x["fam"], "strate": x["etiquette"], "gabarit": x["gabarit"],
                   "N": m.N, "dans_sous_banque": x["cle"] in sb_cles, "regle_A": any(A.values()), "A_3N": A["3N"],
                   "A_1": A["1"], "A_N+1": A["N+1"], "saillante": bool(sal), "valeurs_saillantes_qui_touchent": sal,
                   "seuil": x["seuil"]})
        profils.append(pr)
    # aucune vérité ne doit être touchée par une instance saillante
    res["verites_touchees_saillantes"] = sum(
        1 for x in items if not x["y"] and any(touche(x["monde"], x["arbre"], instance_uniforme(x["monde"], x["arbre"], v))
                                               for v in valeurs_saillantes(x["monde"], x["texte"])))
    res["chaine"] = chaine
    # ---------------------------------------------------------------- a : table
    table = Counter((x["fam"], x["etiquette"], x["gabarit"]) for x in items)
    table_sb = Counter((x["fam"], x["etiquette"], x["gabarit"]) for x in sb_items)
    exemples = {}
    for x in items:
        exemples.setdefault((x["fam"], x["etiquette"], x["gabarit"]), (x["texte"], x["seuil"]))
    # sorties à garder pour l'agrégat
    jetons_par_famille = {}
    for fam in FAMILLES:
        jetons_par_famille[fam] = {True: Counter(), False: Counter()}
        for x in items:
            if x["fam"] == fam:
                jetons_par_famille[fam][x["y"]].update(x["js"])
    textes = defaultdict(set)
    for x in items:
        textes[(x["fam"], x["etiquette"], x["gabarit"])].add(x["texte"])
    return res, profils, poids_pli0, poids_num, table, table_sb, exemples, jetons_par_famille, textes


# =============================================================================== h : puissance par simulation
def score_apparie(n10, n01, n, d0):
    """Score apparié du brouillon 4 (§ Plan d'analyse) ; vectorisé ; se réduit à McNemar en d0 = 0."""
    n10 = np.asarray(n10, float)
    n01 = np.asarray(n01, float)
    A = 2 * n
    Bq = -n10 - n01 + (2 * n - n10 + n01) * d0
    C = -n01 * d0 * (1 - d0)
    q = (np.sqrt(np.maximum(Bq * Bq - 4 * A * C, 0)) - Bq) / (2 * A)
    den = np.sqrt(n * (2 * q + d0 * (1 - d0)))
    with np.errstate(divide="ignore", invalid="ignore"):
        s = (n10 - n01 - n * d0) / den
    return np.where(den > 0, s, 0.0)


Z_B0, Z_BD, Z_HD = 2.2504, 2.3099, 2.2754


def puissance(profils_par_racine, rng, tirages=2000):
    """Modèle déclaré. Sur chaque racine, les 75 faux de la sous-banque et l'issue de la règle A (calculée, fixe).
    S rend un témoin sur un faux à portée de A avec probabilité p_in, hors de portée avec p_out. N rend un témoin avec
    probabilité q_in à portée de A et q_in·rho hors de portée, q_in réglé pour que E[v_N] = v_N ; S et N indépendants
    sachant l'item. Scénario « banque v6 » : motif de A réel de chaque racine ; scénario « cible v7 » : part des faux hors
    de portée fixée à 0,50 (38 sur 75)."""
    sortie = []
    motifs = [np.array([p["regle_A"] for p in pr if p["dans_sous_banque"]], bool) for pr in profils_par_racine]
    n = 75
    scenarios = {"banque_v6": motifs, "cible_v7_moitie_hors_de_portee": [np.array([True] * 37 + [False] * 38)]}
    for nom_sc, liste in scenarios.items():
        for p_in in (0.90, 1.00):
            for p_out in (0.0, 0.25, 0.5, 0.75, 1.0):
                for vN in (0.2, 0.5, 0.85):
                    for rho in (1.0, 0.0):
                        e1 = e2 = e4 = 0
                        vS_m = vN_m = vA_m = 0.0
                        tot = 0
                        sautes = 0
                        par_motif = max(1, tirages // len(liste))
                        for a in liste:
                            assert len(a) == n
                            fa = a.mean()
                            q_in = vN / (fa + (1 - fa) * rho) if (fa + (1 - fa) * rho) > 0 else 0.0
                            if q_in > 1:
                                sautes += 1
                                continue  # v_N inatteignable sous ce modèle (rho = 0 et v_N > v_A)
                            pS = np.where(a, p_in, p_out)
                            pN = np.where(a, q_in, q_in * rho)
                            S = rng.random((par_motif, n)) < pS
                            Nn = rng.random((par_motif, n)) < pN
                            A = np.broadcast_to(a, S.shape)
                            n10 = (S & ~Nn).sum(1)
                            n01 = (~S & Nn).sum(1)
                            e1 += int((score_apparie(n10, n01, n, 0.0) >= Z_B0).sum())
                            e2 += int((score_apparie(n10, n01, n, 0.2) >= Z_BD).sum())
                            m10 = (S & ~A).sum(1)
                            m01 = (~S & A).sum(1)
                            e4 += int((score_apparie(m10, m01, n, 0.0) >= Z_B0).sum())
                            vS_m += S.mean(1).sum()
                            vN_m += Nn.mean(1).sum()
                            vA_m += fa * par_motif
                            tot += par_motif
                        if tot == 0:
                            sortie.append({"scenario": nom_sc, "p_in": p_in, "p_out": p_out, "v_N": vN, "rho": rho,
                                           "inatteignable": True})
                            continue
                        sortie.append({"scenario": nom_sc, "p_in": p_in, "p_out": p_out, "v_N": vN, "rho": rho,
                                       "tirages": tot, "motifs_sautes_v_N_inatteignable": sautes, "v_S_moyen": round(vS_m / tot, 4),
                                       "v_N_moyen": round(vN_m / tot, 4), "v_A_moyen": round(vA_m / tot, 4),
                                       "puissance_E1": round(e1 / tot, 4), "puissance_E2": round(e2 / tot, 4),
                                       "puissance_E4": round(e4 / tot, 4)})
    # seuil exact de E4 quand S ne manque aucun faux à portée de A (n01 = 0) : plus petit n10
    n10_min = next(k for k in range(1, 76) if score_apparie(k, 0, 75, 0.0) >= Z_B0)
    # et quand S manque un ou deux faux à portée de A
    n10_min_1 = next(k for k in range(1, 76) if score_apparie(k, 1, 75, 0.0) >= Z_B0)
    n10_min_2 = next(k for k in range(1, 76) if score_apparie(k, 2, 75, 0.0) >= Z_B0)
    return sortie, {"n10_min_E4_si_n01_0": n10_min, "n10_min_E4_si_n01_1": n10_min_1, "n10_min_E4_si_n01_2": n10_min_2}


# =============================================================================== principal
def main(chemin_json):
    params, sha_params = pk_parametres.charger()
    ss = {i: np.random.SeedSequence(GRAINE_SCRIPT, spawn_key=(1000 + i,)) for i in (0, 1)}
    rng_boot = np.random.default_rng(ss[0])
    rng_puis = np.random.default_rng(ss[1])
    groupe_gab = gabarits_tenus_a_l_ecart(params)
    lignes, profils_par_racine = [], []
    poids_somme = Counter()
    poids_num = []
    table, table_sb_par_racine, exemples = Counter(), [], {}
    jpf = {fam: {True: Counter(), False: Counter()} for fam in FAMILLES}
    textes_gab = defaultdict(set)
    for r in RACINES:
        res, profils, p0, pn, t, tsb, ex, jf, tx = traiter_racine(r, params, groupe_gab)
        lignes.append(res)
        profils_par_racine.append(profils)
        for j, v in p0.items():
            poids_somme[j] += v
        poids_num.append(pn)
        table.update(t)
        table_sb_par_racine.append(tsb)
        for k, v in ex.items():
            exemples.setdefault(k, v)
        for fam in FAMILLES:
            for y in (True, False):
                jpf[fam][y].update(jf[fam][y])
        for k, v in tx.items():
            textes_gab[k] |= v
        journal(f"racine {r} faite ; foi {res['aire_qui_fait_foi']:.4f}")
    nR = len(RACINES)

    # ------------------------------------------------------------------ agrégats
    def agr(cle_bloc, comp, champ):
        return resume([x[cle_bloc][comp][champ] for x in lignes])

    blocs = ["style_banque", "style_sous_banque", "style_longueur_des_nombres_banque", "identifiant_gabarit_banque",
             "identifiant_gabarit_sous_banque", "identifiant_famille_banque", "identifiant_famille_sous_banque",
             "style_gabarits_tenus_a_l_ecart_banque", "style_gabarits_et_mondes_tenus_a_l_ecart_banque",
             "numerique_banque", "numerique_sous_banque", "chiffres_plus_grand_litteral_banque",
             "chiffres_plus_grand_litteral_sous_banque"]
    agregats = {}
    for b in blocs:
        agregats[b] = {}
        for comp, d in lignes[0][b].items():
            agregats[b][comp] = {champ: agr(b, comp, champ) for champ in d if champ not in ("n_pos", "n_neg")}
            agregats[b][comp]["n_pos_racine_0"] = d["n_pos"]
            agregats[b][comp]["n_neg_racine_0"] = d["n_neg"]
    foi = [x["aire_qui_fait_foi"] for x in lignes]
    agregats["aire_qui_fait_foi"] = resume(foi)
    agregats["aire_qui_fait_foi_intervalle_moyenne_90"] = intervalle_moyenne(foi, rng_boot)
    # intervalles à 90 % (rééchantillonnage des racines) sur les excès principaux
    exces = {}
    for b in ("style_banque", "style_sous_banque", "numerique_banque", "numerique_sous_banque"):
        for comp in ("tous_faux__tous_vrais", "faux_tot__tous_vrais", "pieges__tous_vrais"):
            v = [x[b][comp]["exces_fa10"] for x in lignes]
            exces[f"{b}/{comp}"] = {"moyenne": round(float(np.mean(v)), 4), "intervalle_90": intervalle_moyenne(v, rng_boot)}
    agregats["exces_fa10_intervalles"] = exces

    # ------------------------------------------------------------------ V : vérification de la première passe
    fable = json.loads(Path(__file__).resolve().parents[1].joinpath(
        "juges-recus", "juge-fable-max-v1-diagnostic-style-sortie.json").read_text(encoding="utf-8"))
    corresp = {
        "aire_hors_vus_pieges": ("style_banque", "pieges__tous_vrais", "aire_hors_vus"),
        "aire_hors_vus_faux_tot": ("style_banque", "faux_tot__tous_vrais", "aire_hors_vus"),
        "aire_hors_vus_tous_faux": ("style_banque", "tous_faux__tous_vrais", "aire_hors_vus"),
        "aire_tous_textes_pieges": ("style_banque", "pieges__tous_vrais", "aire"),
        "aire_tous_textes_faux_tot": ("style_banque", "faux_tot__tous_vrais", "aire"),
        "aire_tous_textes_tous_faux": ("style_banque", "tous_faux__tous_vrais", "aire"),
        "aire_pieges_contre_faux_tot": ("style_banque", "pieges__faux_tot", "aire"),
        "rappel_a_10_tous_faux": ("style_banque", "tous_faux__tous_vrais", "rappel_fa10"),
        "rappel_a_5_tous_faux": ("style_banque", "tous_faux__tous_vrais", "rappel_fa05"),
        "rappel_a_10_pieges": ("style_banque", "pieges__tous_vrais", "rappel_fa10"),
        "rappel_a_10_faux_tot": ("style_banque", "faux_tot__tous_vrais", "rappel_fa10"),
        "chiffres_aire_pieges": ("chiffres_plus_grand_litteral_banque", "pieges__tous_vrais", "aire"),
        "chiffres_aire_faux_tot": ("chiffres_plus_grand_litteral_banque", "faux_tot__tous_vrais", "aire"),
        "chiffres_aire_pieges_contre_faux_tot": ("chiffres_plus_grand_litteral_banque", "pieges__faux_tot", "aire"),
        "chiffres_rappel_a_10_pieges": ("chiffres_plus_grand_litteral_banque", "pieges__tous_vrais", "rappel_fa10"),
    }
    verif = {"racines_identiques": fable["racines"] == RACINES, "ecart_max_par_mesure": {}}
    for cle_f, (b, comp, champ) in corresp.items():
        ec = max(abs(lf[cle_f] - lo[b][comp][champ]) for lf, lo in zip(fable["lignes"], lignes))
        verif["ecart_max_par_mesure"][cle_f] = ec
    for fam in FAMILLES:
        ec = max(abs(lf["aire_tous_faux_par_famille"][fam] - lo["style_banque"][f"famille_{fam}__faux__vrais"]["aire"])
                 for lf, lo in zip(fable["lignes"], lignes))
        verif["ecart_max_par_mesure"][f"aire_tous_faux_par_famille_{fam}"] = ec
    verif["ecart_max_foi"] = max(abs(max(lf["aire_hors_vus_pieges"], lf["aire_hors_vus_faux_tot"]) - lo["aire_qui_fait_foi"])
                                 for lf, lo in zip(fable["lignes"], lignes))
    verif["effectifs_hors_vus_identiques"] = all(lf["effectifs_hors_textes_vus"] == lo["effectifs_hors_vus"]
                                                 for lf, lo in zip(fable["lignes"], lignes))
    poids_moy = {j: v / nR for j, v in poids_somme.items()}
    tri_poids = sorted(poids_moy.items(), key=lambda kv: (round(kv[1], 9), kv[0]))
    verif["poids_cites"] = {j: round(poids_moy.get(j, float("nan")), 4) for j in ("<·(", ")·>=", "t·>=", ">=·(")}
    verif["jetons_plus_vrai_12"] = [[j, round(v, 4)] for j, v in tri_poids[:12]]
    verif["jetons_plus_faux_12"] = [[j, round(v, 4)] for j, v in sorted(poids_moy.items(),
                                                                         key=lambda kv: (-round(kv[1], 9), kv[0]))[:12]]

    # ------------------------------------------------------------------ b : jetons par famille (comptes cumulés)
    jetons_famille = {}
    for fam in FAMILLES:
        cF, cV = jpf[fam][True], jpf[fam][False]
        voc = set(cF) | set(cV)
        Vv = len(voc) + 1
        TF, TV = sum(cF.values()), sum(cV.values())
        lr = {j: math.log(((cF.get(j, 0) + 1) / (TF + Vv)) / ((cV.get(j, 0) + 1) / (TV + Vv))) for j in voc}
        cle_tri = lambda kv: (round(kv[1], 9), kv[0])  # noqa: E731
        vr = sorted(lr.items(), key=cle_tri)[:15]
        fx = sorted(lr.items(), key=lambda kv: (-round(kv[1], 9), kv[0]))[:15]
        jetons_famille[fam] = {
            "plus_faux": [[j, round(v, 3), cF.get(j, 0), cV.get(j, 0)] for j, v in fx],
            "plus_vrai": [[j, round(v, 3), cF.get(j, 0), cV.get(j, 0)] for j, v in vr]}

    # ------------------------------------------------------------------ a : table
    table_out = []
    for (fam, et, gab), n in sorted(table.items()):
        sbv = [t.get((fam, et, gab), 0) for t in table_sb_par_racine]
        txt, seuil = exemples[(fam, et, gab)]
        table_out.append({"famille": fam, "strate": et, "gabarit": gab, "banque_total": n,
                          "banque_par_racine": n // nR, "sous_banque_total": sum(sbv), "sous_banque_min": min(sbv),
                          "sous_banque_max": max(sbv), "forme_seuil_P9": seuil,
                          "textes_distincts_41_racines": len(textes_gab[(fam, et, gab)]), "exemple_racine_0": txt})

    # ------------------------------------------------------------------ g : profils agrégés
    tous = [p for pr in profils_par_racine for p in pr]
    sb = [p for p in tous if p["dans_sous_banque"]]

    def taux(lst, cle):
        return round(sum(1 for p in lst if p[cle]) / len(lst), 4) if lst else None

    g_glob = {}
    for nom, lst in (("banque_96_faux", tous), ("sous_banque_75_faux", sb)):
        for strate in (None, FT, PG):
            l2 = [p for p in lst if strate is None or p["strate"] == strate]
            g_glob[f"{nom}/{strate or 'tous'}"] = {
                "n": len(l2), "regle_A": taux(l2, "regle_A"), "A_3N_seul": taux(l2, "A_3N"),
                "A_1": taux(l2, "A_1"), "A_N+1": taux(l2, "A_N+1"), "saillante": taux(l2, "saillante"),
                "hors_de_portee_A_et_saillante": round(sum(1 for p in l2 if not p["regle_A"] and not p["saillante"]) / len(l2), 4),
                "clos_ou_sans_variable_nat": round(sum(1 for p in l2 if p.get("nb_variables_nat", 1) == 0) / len(l2), 4),
                "densite_moyenne_instances_fausses": round(float(np.mean([p["n_fausses"] / p["n_instances"] for p in l2
                                                                          if p.get("n_instances")])), 4)}
    par_racine_sb = []
    for r, pr in zip(RACINES, profils_par_racine):
        s = [p for p in pr if p["dans_sous_banque"]]
        par_racine_sb.append({"racine": r, "n": len(s), "regle_A": sum(p["regle_A"] for p in s),
                              "A_3N": sum(p["A_3N"] for p in s), "saillante": sum(p["saillante"] for p in s)})
    g_gab = {}
    for p in tous:
        k = f"{p['famille']}/{p['strate']}/{p['gabarit']}"
        d = g_gab.setdefault(k, {"n": 0, "regle_A": 0, "A_3N": 0, "A_1": 0, "A_N+1": 0, "saillante": 0,
                                 "densite": [], "premier_nat_faux": [], "n_instances": [], "clos": 0})
        d["n"] += 1
        for c in ("regle_A", "A_3N", "A_1", "A_N+1", "saillante"):
            d[c] += int(p[c])
        if p.get("n_instances"):
            d["densite"].append(p["n_fausses"] / p["n_instances"])
            d["n_instances"].append(p["n_instances"])
            d["premier_nat_faux"].append(min(p["nat_max_des_fausses"]) if p["nat_max_des_fausses"] else None)
        d["clos"] += int(p.get("nb_variables_nat", 1) == 0)
    for k, d in g_gab.items():
        pn = [x for x in d["premier_nat_faux"] if x is not None]
        d["densite"] = round(float(np.mean(d["densite"])), 4) if d["densite"] else None
        d["n_instances_median"] = int(np.median(d["n_instances"])) if d["n_instances"] else None
        del d["n_instances"]
        d["premier_nat_faux"] = resume(pn)
    # valeurs saillantes qui touchent, par gabarit (quelles valeurs suffisent)
    val_sal = defaultdict(Counter)
    for p in tous:
        for v in p["valeurs_saillantes_qui_touchent"]:
            lab = "0" if v == 0 else "1" if v == 1 else "2" if v == 2 else "N" if v == p["N"] else "N+1" if v == p["N"] + 1 \
                else "2N" if v == 2 * p["N"] else "3N" if v == 3 * p["N"] else "texte±1"
            val_sal[f"{p['famille']}/{p['strate']}/{p['gabarit']}"][lab] += 1

    # ------------------------------------------------------------------ h
    puis, seuils_E4 = puissance(profils_par_racine, rng_puis)
    journal("puissance faite")

    sortie = {
        "nature": "diagnostic de fuite, banque v6, racines d'essai seulement ; processeur ; aucun appel de modèle",
        "racines": RACINES, "parametres_sha256": sha_params,
        "paquet": "src/controle_ia/oracles_plantes_v6 (lu, non modifié)",
        "numpy": np.__version__, "python": sys.version.split()[0],
        "graines_du_script": {"racine": GRAINE_SCRIPT, "enfants": {"1000": "rééchantillonnage des racines (2 000)",
                                                                   "1001": "simulation de puissance"},
                              "entropie_et_cles": {str(i): [str(s.entropy), list(s.spawn_key)] for i, s in ss.items()}},
        "groupes_de_gabarits_tenus_a_l_ecart": {f"{a}/{b}": g for (a, b), g in sorted(groupe_gab.items())},
        "noms_traits_numeriques": NOMS_NUM,
        "poids_logistique_toute_banque_moyenne": [round(float(x), 4) for x in np.mean(poids_num, axis=0)],
        "verification_premiere_passe": verif,
        "agregats": agregats,
        "table_gabarits": table_out,
        "jetons_par_famille": jetons_famille,
        "profil_temoins": {"global": g_glob, "par_racine_sous_banque": par_racine_sb, "par_gabarit": g_gab,
                           "valeurs_saillantes_qui_touchent_par_gabarit": {k: dict(sorted(v.items())) for k, v in sorted(val_sal.items())}},
        "puissance": {"modele": puissance.__doc__, "seuils_exacts_E4": seuils_E4, "resultats": puis,
                      "valeurs_critiques": {"B>0": Z_B0, "B>=delta": Z_BD, "H<delta": Z_HD}},
        "lignes_par_racine": lignes,
        "profils_par_item": [dict(p, racine=r) for r, pr in zip(RACINES, profils_par_racine) for p in pr],
    }
    Path(chemin_json).write_text(json.dumps(sortie, ensure_ascii=False, indent=1, sort_keys=True,
                                            default=lambda o: sorted(o) if isinstance(o, set) else str(o)) + "\n",
                                 encoding="utf-8")
    imprimer(sortie)


def imprimer(S):
    A = S["agregats"]
    p = print

    def ligne(nom, d):
        if d is None:
            p(f"   {nom:62s} : —")
        else:
            p(f"   {nom:62s} : min {d['min']:.3f} ; moy {d['moyenne']:.3f} ; méd {d['mediane']:.3f} ; max {d['max']:.3f}")

    p(f"Diagnostic de fuite, banque v6 (oracles_plantes_v6), {len(S['racines'])} racines d'essai : {S['racines']}")
    p(f"paramètres sha256 {S['parametres_sha256']} ; numpy {S['numpy']} ; graines du script : {S['graines_du_script']}")
    p()
    p("V. Vérification de la première passe (écart absolu maximal sur les 41 racines, mesure par mesure)")
    v = S["verification_premiere_passe"]
    p(f"   racines identiques : {v['racines_identiques']} ; effectifs hors vus identiques : {v['effectifs_hors_vus_identiques']}")
    p(f"   aire qui fait foi : écart max {v['ecart_max_foi']:.2e}")
    for k, e in sorted(v["ecart_max_par_mesure"].items()):
        p(f"   {k:45s} écart max {e:.2e}")
    p(f"   poids cités (moyenne sur les racines, pli 0) : {v['poids_cites']}")
    p("   12 jetons les plus « vrai » (ex æquo triés par jeton) : " + " ; ".join(f"{j} {w:+.2f}" for j, w in v["jetons_plus_vrai_12"]))
    p("   12 jetons les plus « faux » (ex æquo triés par jeton) : " + " ; ".join(f"{j} {w:+.2f}" for j, w in v["jetons_plus_faux_12"]))
    p()
    p("a. Table gabarit × strate × famille (41 racines ; banque : 1 par monde et par racine)")
    for t in S["table_gabarits"]:
        p(f"   {t['famille']} {t['strate']:14s} {t['gabarit']:46s} banque {t['banque_total']:4d} ; sous-banque "
          f"{t['sous_banque_total']:3d} (par racine {t['sous_banque_min']}..{t['sous_banque_max']}) ; seuil P9 "
          f"{'oui' if t['forme_seuil_P9'] else 'non'} ; textes distincts {t['textes_distincts_41_racines']:3d}")
        p(f"      ex. : {t['exemple_racine_0']}")
    p()
    p("b. Jetons aux plus forts rapports de vraisemblance, par famille (comptes cumulés sur 41 racines, banque entière ;")
    p("   logarithme du rapport faux / vrai, lissage 1 ; [jeton, poids, compte faux, compte vrai] ; ex æquo triés par jeton)")
    for fam, d in S["jetons_par_famille"].items():
        p(f"   {fam} plus « faux » : " + " ; ".join(f"{j} {w:+.2f} ({a}/{b})" for j, w, a, b in d["plus_faux"][:12]))
        p(f"   {fam} plus « vrai » : " + " ; ".join(f"{j} {w:+.2f} ({a}/{b})" for j, w, a, b in d["plus_vrai"][:12]))
    p()
    p(f"c. Aires et rappels à fausses alarmes plafonnées. Aire qui fait foi : {A['aire_qui_fait_foi']} ; "
      f"intervalle à 90 % de la moyenne : {A['aire_qui_fait_foi_intervalle_moyenne_90']}")
    comps = ["tous_faux__tous_vrais", "faux_tot__tous_vrais", "pieges__tous_vrais", "faux_tot_seuil__vrais_seuil",
             "faux_tot_non_seuil__vrais_non_seuil", "pieges__vrais_seuil", "pieges__faux_tot",
             "famille_F1__faux__vrais", "famille_F2__faux__vrais", "famille_F3__faux__vrais",
             "famille_F1__faux_tot__vrais", "famille_F1__pieges__vrais", "famille_F2__faux_tot__vrais",
             "famille_F2__pieges__vrais", "famille_F3__faux_tot__vrais", "famille_F3__pieges__vrais"]
    for b, titre in (("style_banque", "classifieur de style, banque (192 énoncés analysables par racine)"),
                     ("style_sous_banque", "classifieur de style, sous-banque (150 analysés), plis par mondes"),
                     ("numerique_banque", "e. sonde numérique, banque"),
                     ("numerique_sous_banque", "e. sonde numérique, sous-banque"),
                     ("style_longueur_des_nombres_banque", "e'. style, nombres remplacés par leur longueur, banque"),
                     ("chiffres_plus_grand_litteral_banque", "règle « chiffres du plus grand littéral », banque"),
                     ("chiffres_plus_grand_litteral_sous_banque", "règle « chiffres du plus grand littéral », sous-banque"),
                     ("identifiant_gabarit_banque", "d. identifiant de gabarit seul, banque"),
                     ("identifiant_famille_banque", "d. identifiant de famille seul, banque"),
                     ("identifiant_gabarit_sous_banque", "d. identifiant de gabarit seul, sous-banque"),
                     ("style_gabarits_tenus_a_l_ecart_banque", "d. style, gabarits tenus à l'écart (tous mondes), banque"),
                     ("style_gabarits_et_mondes_tenus_a_l_ecart_banque", "d. style, gabarits et mondes tenus à l'écart, banque")):
        p(f"  {titre}")
        for c in comps:
            d = A[b].get(c)
            if d is None:
                continue
            champs = [("aire", "aire"), ("aire_hors_vus", "aire hors vus"), ("rappel_fa10", "rappel FA<=0,10 (seuil sur les vrais évalués)"),
                      ("fa_obtenue_fa10", "FA obtenue à ce seuil"), ("rappel_fa05", "rappel FA<=0,05"),
                      ("seuil_transporte_rappel", "rappel, seuil réglé sur mondes d'apprentissage"),
                      ("seuil_transporte_fa", "FA obtenue, seuil réglé sur mondes d'apprentissage")]
            p(f"   [{c}] n faux {d['n_pos_racine_0']}, n vrais {d['n_neg_racine_0']} (racine 0)")
            for k, nom in champs:
                if k in d:
                    ligne("  " + nom, d[k])
    p()
    p("   Excès (rappel à FA<=0,10 moins 0,10), moyenne et intervalle à 90 % par rééchantillonnage des racines :")
    for k, d in S["agregats"]["exces_fa10_intervalles"].items():
        p(f"   {k:60s} moyenne {d['moyenne']:.3f} ; intervalle {d['intervalle_90']}")
    p()
    p("d. Gabarits portant les deux classes (vrai et faux) : "
      f"{sorted(set(x['gabarits_a_deux_classes'] for x in S['lignes_par_racine']))} (sur toutes les racines) : "
      "le style « à l'intérieur d'un gabarit » et « contre les vrais des mêmes gabarits » sont sans objet.")
    p(f"   poids moyens de la sonde numérique (toute la banque, traits centrés réduits ; constante d'abord) :")
    p("   " + " ; ".join(f"{n} {w:+.2f}" for n, w in zip(["constante"] + S["noms_traits_numeriques"],
                                                          S["poids_logistique_toute_banque_moyenne"])))
    p()
    p("f. Contrôle de chaîne (sommes ou ensembles sur les 41 racines)")
    L = S["lignes_par_racine"]
    ch = [x["chaine"] for x in L]
    p(f"   découpeur ou jetons différents du paquet : {sum(c['jetons_differents_du_paquet'] for c in ch)}")
    p(f"   scores bayésiens différents du paquet (exacts) : {sum(c['scores_differents_du_paquet'] for c in ch)}")
    p(f"   aire qui fait foi égale à forme_seule.mesurer : {all(c['aire_qui_fait_foi_egale_au_paquet'] for c in ch)}")
    p(f"   plis identiques au paquet : {all(c['plis_identiques_au_paquet'] for c in ch)}")
    p(f"   items analysés de la sous-banque : {sorted(set(c['sous_banque_items_analyses'] for c in ch))} ; textes servis "
      f"différents à l'octet du texte planté : {sum(c['sous_banque_octets_differents_du_texte_plante'] for c in ch)}")
    p(f"   clés d'un item servi : {sorted(set(tuple(c['cles_d_un_item_servi']) for c in ch))} ; clés de l'objet servi : "
      f"{sorted(set(tuple(c['cles_de_l_objet_servi']) for c in ch))}")
    for k in ("aire_position_de_service", "aire_valeur_identifiant", "aire_longueur_en_caracteres_banque",
              "aire_longueur_en_jetons_banque"):
        ligne(k, resume([c[k] for c in ch]))
    p(f"   familles par pli (racine 0) : {ch[0]['familles_par_pli']}")
    cnt = Counter(v for c in ch for v in c["mondes_d_apprentissage_meme_famille_par_monde_test"])
    p(f"   mondes d'apprentissage de la même famille, vus d'un monde de test (comptes sur 41 × 12) : {dict(sorted(cnt.items()))}")
    p()
    G = S["profil_temoins"]
    p("g. Profil des témoins (instances fausses dans [0 .. 3N])")
    for k, d in G["global"].items():
        p(f"   {k:32s} n {d['n']:5d} ; règle A {d['regle_A']:.3f} ; 3N seul {d['A_3N_seul']:.3f} ; à 1 {d['A_1']:.3f} ; "
          f"à N+1 {d['A_N+1']:.3f} ; saillante {d['saillante']:.3f} ; hors A et saillantes {d['hors_de_portee_A_et_saillante']:.3f} ; "
          f"clos {d['clos_ou_sans_variable_nat']:.3f} ; densité {d['densite_moyenne_instances_fausses']:.3f}")
    ra = [x["regle_A"] for x in G["par_racine_sous_banque"]]
    sa = [x["saillante"] for x in G["par_racine_sous_banque"]]
    a3 = [x["A_3N"] for x in G["par_racine_sous_banque"]]
    p(f"   sous-banque, par racine (sur 75) : règle A min {min(ra)} méd {int(np.median(ra))} max {max(ra)} ; 3N seul min "
      f"{min(a3)} méd {int(np.median(a3))} max {max(a3)} ; saillante min {min(sa)} méd {int(np.median(sa))} max {max(sa)}")
    p(f"   vérités touchées par une instance saillante (doit être 0) : {sum(x['verites_touchees_saillantes'] for x in L)}")
    p("   par gabarit (164 = 41 racines × 4 mondes) : règle A ; 3N ; 1 ; N+1 ; saillante ; densité ; plus petit NAT faux (médiane,")
    p("   -1 = énoncé sans variable NAT) ; clos (sans variable NAT)")
    for k, d in sorted(G["par_gabarit"].items()):
        pn = d["premier_nat_faux"]
        p(f"   {k:50s} A {d['regle_A']:3d} ; 3N {d['A_3N']:3d} ; 1 {d['A_1']:3d} ; N+1 {d['A_N+1']:3d} ; sail. {d['saillante']:3d} ; "
          f"dens. {d['densite'] if d['densite'] is not None else '—'} ; prem. {pn['mediane'] if pn else '—'} ; clos {d['clos']}")
    p("   valeurs saillantes qui touchent, par gabarit (comptes de couples énoncé × valeur ; « texte±1 » peut compter")
    p("   plusieurs valeurs d'un même énoncé ; une valeur égale à deux étiquettes prend la première de 0, 1, 2, N, N+1, 2N, 3N) :")
    for k, d in G["valeurs_saillantes_qui_touchent_par_gabarit"].items():
        p(f"   {k:50s} {d}")
    p()
    P = S["puissance"]
    p("h. Puissance de la lecture en preuve (simulation ; modèle déclaré dans le JSON)")
    p(f"   seuils exacts de E4 (n = 75) : {P['seuils_exacts_E4']}")
    for x in P["resultats"]:
        if x.get("inatteignable"):
            p(f"   {x['scenario']:32s} p_in {x['p_in']:.2f} p_out {x['p_out']:.2f} v_N {x['v_N']:.2f} rho {x['rho']:.0f} : inatteignable")
            continue
        p(f"   {x['scenario']:32s} p_in {x['p_in']:.2f} p_out {x['p_out']:.2f} v_N {x['v_N']:.2f} rho {x['rho']:.0f} : "
          f"v_S {x['v_S_moyen']:.3f} v_N {x['v_N_moyen']:.3f} v_A {x['v_A_moyen']:.3f} | E1 {x['puissance_E1']:.3f} "
          f"E2 {x['puissance_E2']:.3f} E4 {x['puissance_E4']:.3f}"
          + (f" (racines sautées : {x['motifs_sautes_v_N_inatteignable']})" if x.get("motifs_sautes_v_N_inatteignable") else ""))


if __name__ == "__main__":
    main(sys.argv[1])
