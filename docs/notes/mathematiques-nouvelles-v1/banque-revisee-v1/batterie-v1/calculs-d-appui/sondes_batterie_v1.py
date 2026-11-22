"""Sondes et conditions de la batterie, telles que le texte les spécifie — prototype du concepteur (calcul d'appui) — v1.

Le prototype suit la lettre de `batterie-fuite-banque-revisee-v1.md` pour pouvoir l'éprouver ; ce n'est pas
l'instrument (le code de la batterie revient à Opus, contre-lu). Il lit le paquet figé `oracles_plantes_v6` sans le
modifier : découpeur, classifieur de style, vérification exacte d'une instance.
"""
from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction

import numpy as np

from controle_ia.oracles_plantes_v6.evaluation import prefixe
from controle_ia.oracles_plantes_v6.exact import HorsCapacite, Indefini
from controle_ia.oracles_plantes_v6.forme_seule import BayesNaif, aire_sous_la_courbe
from controle_ia.oracles_plantes_v6.graines import generateur
from controle_ia.oracles_plantes_v6.grammaire import lexer
from controle_ia.oracles_plantes_v6.tests_de_mort import verifier_instance

from outils_batterie_v1 import borne_haute, rappel_au_prorata, rappel_bloc_entier

V, FT, PG = "VERITE_PLANTEE", "FAUX_TOT", "PIEGE"
PLIS = 4


# ------------------------------------------------------------------------------------------------ squelette, littéraux
def squelette(texte: str) -> tuple:
    """Suite des jetons de l'énoncé (découpeur figé), chaque nombre remplacé par « NUM »."""
    return tuple("NUM" if g == "nombre" else v for g, v in lexer(texte))


def litteraux(texte: str) -> list:
    """Littéraux dans l'ordre d'écriture : (signe, numérateur écrit, dénominateur écrit). « ( a / b ) » et
    « ( - a / b ) » font un seul littéral ; « ( - a ) » aussi ; tout autre nombre est un entier positif."""
    t = lexer(texte)
    out, i = [], 0

    def nb(k):
        return k < len(t) and t[k][0] == "nombre"

    def sym(k, s):
        return k < len(t) and t[k] == ("sym", s)

    while i < len(t):
        if sym(i, "("):
            j, signe = i + 1, 1
            if sym(j, "-"):
                signe, j = -1, j + 1
            if nb(j) and sym(j + 1, "/") and nb(j + 2) and sym(j + 3, ")"):
                out.append((signe, Fraction(t[j][1]), Fraction(t[j + 2][1])))
                i = j + 4
                continue
            if signe == -1 and nb(j) and sym(j + 1, ")"):
                out.append((-1, Fraction(t[j][1]), Fraction(1)))
                i = j + 2
                continue
        if nb(i):
            out.append((1, Fraction(t[i][1]), Fraction(1)))
        i += 1
    return out


def _log10(x) -> float:
    """log10 d'un rationnel positif, sans dépassement pour les très grands entiers."""
    x = Fraction(x)
    return math.log10(x.numerator) - math.log10(x.denominator)


NOMS_PAR_LITTERAL = ["grandeur", "numerateur", "denominateur", "petitesse", "pres_de_un", "est_0", "est_1", "est_2",
                     "au_plus_N", "entre_N_et_3N", "rang_parmi_servis", "egal_a_un_servi", "rapport_au_plus_grand_servi",
                     "grandeur_carre", "numerateur_carre", "denominateur_carre", "negatif"]


def traits_des_nombres(texte: str, N: int, servis: list) -> list:
    """Traits de la sonde des nombres pour un énoncé : 17 par littéral, dans l'ordre d'écriture ; 2 par couple de
    littéraux ; 1 pour l'énoncé (nombre total de chiffres écrits). Aucun calcul de vérité."""
    L = litteraux(texte)
    servis = sorted({abs(Fraction(x)) for x in servis})
    smax = servis[-1] if servis else Fraction(0)
    x = []
    absv = []
    for signe, a, b in L:
        if b == 0:
            v = Fraction(0)
        else:
            v = a / b
        absv.append(v)
        g = _log10(1 + v)
        la = _log10(1 + a)
        lb = _log10(b) if b > 0 else 0.0
        x += [g, la, lb,
              _log10(1 + 1 / v) if v != 0 else 0.0,
              _log10(1 + 1 / abs(v - 1)) if v != 1 else 0.0,
              float(v == 0), float(v == 1), float(v == 2),
              float(v <= N), float(N < v <= 3 * N),
              (sum(1 for s in servis if s < v) / len(servis)) if servis else 0.0,
              float(v in servis),
              _log10((1 + v) / (1 + smax)),
              g * g, la * la, lb * lb,
              float(signe < 0)]
    for i in range(len(absv)):
        for j in range(i + 1, len(absv)):
            a, b = absv[i], absv[j]
            hi, lo = max(a, b), min(a, b)
            x += [float(lo / hi) if hi > 0 else 1.0, float(a == b)]
    x.append(float(sum(ch.isdigit() for ch in texte)))
    return x


class LogistiquePenalisee:
    """Régression logistique, pénalité quadratique 1 sur tous les poids (ordonnée à l'origine comprise), traits centrés
    et réduits sur l'apprentissage (écart-type nul : trait mis à zéro), Newton, au plus 50 pas, arrêt à 1e-10."""

    def __init__(self, X, y, lam=1.0):
        X = np.asarray(X, float)
        y = np.asarray(y, float)
        self.mu = X.mean(axis=0)
        sd = X.std(axis=0)
        self.nul = sd == 0
        sd[self.nul] = 1.0
        self.sd = sd
        Z = self._z(X)
        w = np.zeros(Z.shape[1])
        P = lam * np.eye(Z.shape[1])
        for _ in range(50):
            p = 1 / (1 + np.exp(-(Z @ w)))
            g = Z.T @ (p - y) + P @ w
            H = (Z * (p * (1 - p))[:, None]).T @ Z + P
            pas = np.linalg.solve(H, g)
            w -= pas
            if np.max(np.abs(pas)) < 1e-10:
                break
        self.w = w

    def _z(self, X):
        Zc = (np.asarray(X, float) - self.mu) / self.sd
        Zc[:, self.nul] = 0.0
        return np.hstack([np.ones((len(Zc), 1)), Zc])

    def score(self, X):
        return [round(float(s), 10) for s in self._z(X) @ self.w]


# ------------------------------------------------------------------------------------------------ sonde de style
def plis_des_mondes(racine: int, nb_mondes: int) -> dict:
    ordre = [int(i) for i in generateur(racine, 10, 0).permutation(nb_mondes)]
    return {w: k % PLIS for k, w in enumerate(ordre)}


def scores_de_style(items: list, racine: int, nb_mondes: int) -> dict:
    """Classifieur de style du paquet figé, inchangé : appris sur le vivier des mondes d'apprentissage (trois plis),
    noté sur le quatrième ; plis par mondes entiers (enfant (10, 0)). Rend {clé d'item: score exact} et l'ensemble des
    clés dont le texte a été vu à l'apprentissage."""
    pli = plis_des_mondes(racine, nb_mondes)
    scores, vus = {}, set()
    for k in range(PLIS):
        app = [x for x in items if pli[x["w"]] != k]
        test = [x for x in items if pli[x["w"]] == k]
        if not test or not app:
            continue
        m = BayesNaif(Fraction(1)).apprendre([x["texte"] for x in app], [x["y"] for x in app])
        textes_app = {x["texte"] for x in app}
        for x in test:
            scores[x["cle"]] = m.score(x["texte"])
            if x["texte"] in textes_app:
                vus.add(x["cle"])
    return scores, vus


def aire_qui_fait_foi(items: list, scores: dict, vus: set):
    """Même calcul que `forme_seule.mesurer` : plus grande des deux aires par strate, hors textes déjà vus."""
    def sc(et):
        return [scores[x["cle"]] for x in items if x["etiquette"] == et and x["cle"] not in vus and x["cle"] in scores]
    a = [aire_sous_la_courbe(sc(PG), sc(V)), aire_sous_la_courbe(sc(FT), sc(V))]
    a = [x for x in a if x is not None]
    return max(a) if a else None


# ------------------------------------------------------------------------------------------------ sonde des nombres
def scores_des_nombres(par_racine: dict) -> dict:
    """Sonde des nombres : pour noter une racine, un modèle par squelette appris sur le vivier de toutes les autres
    racines, mondes entiers ; un monde d'apprentissage de mêmes paramètres servis qu'un monde noté est écarté.
    `par_racine` : {racine: [items avec « cle », « texte », « y », « N », « servis », « monde_id »]}.
    Rend ({racine: {cle: score}}, compte des énoncés notés à zéro faute d'apprentissage). La garde du texte (« plus d'un
    énoncé de la sous-banque sur dix noté à zéro : non calculable ») n'est pas codée ici : le compte est rendu, et il
    vaut zéro sur toutes les banques de ces calculs."""
    groupes = defaultdict(list)  # squelette -> [(racine, cle, traits, y, monde_id)]
    for r, items in par_racine.items():
        for x in items:
            groupes[squelette(x["texte"])].append((r, x["cle"], traits_des_nombres(x["texte"], x["N"], x["servis"]),
                                                   x["y"], x["monde_id"]))
    mondes_de = {r: {x["monde_id"] for x in items} for r, items in par_racine.items()}
    sortie = {r: {} for r in par_racine}
    neutres = 0
    for sq, lignes in groupes.items():
        R = [l[0] for l in lignes]
        X = np.array([l[2] for l in lignes], float)
        y = np.array([float(l[3]) for l in lignes])
        ids = [l[4] for l in lignes]
        for r in par_racine:
            test = np.array([rr == r for rr in R])
            if not test.any():
                continue
            app = np.array([rr != r and i not in mondes_de[r] for rr, i in zip(R, ids)])
            if app.sum() < 20:  # trop peu pour apprendre : score neutre
                s = [0.0] * int(test.sum())
                neutres += int(test.sum())
            else:
                s = LogistiquePenalisee(X[app], y[app]).score(X[test])
            for l, sc in zip([l for l, t in zip(lignes, test) if t], s):
                sortie[r][l[1]] = sc
    return sortie, neutres


# ------------------------------------------------------------------------------------------------ règle aveugle A
def regle_aveugle_A(monde, texte: str) -> bool:
    """Règle aveugle A du brouillon 4, sans retouche : au plus trois instances, variables NAT à 3N, puis 1, puis N + 1 ;
    variables bornées à la plus petite valeur de leur domaine ; vérification exacte (chemin de T6)."""
    arbre = monde.analyser(texte)
    pre, _ = prefixe(arbre)
    vues = []
    for a in (monde.borne_verification(), 1, monde.N + 1):
        env, inst, ok = {}, {}, True
        for var, dom in pre:
            if dom[0] == "NAT":
                x = a
            else:
                try:
                    vals = monde.ev.valeurs_domaine(dom, env, borne=None)
                except (Indefini, HorsCapacite):
                    ok = False
                    break
                if len(vals) == 0:
                    ok = False
                    break
                x = vals[0]
            inst[var] = int(x)
            env[var] = Fraction(int(x))
        if not ok or inst in vues:
            continue
        vues.append(inst)
        if verifier_instance(arbre, monde, inst, monde.borne_verification())[0] == "verifie":
            return True
    return False


# ------------------------------------------------------------------------------------------------ invariant C1
def ecarts_C1(vivier: list, sous_banque: list) -> list:
    """Contrôle de l'invariant de construction. `vivier`, `sous_banque` : items avec « w », « texte », « etiquette »,
    « paire » (identifiant de paire ou None). Rend la liste des écarts (vide = tenu)."""
    ecarts = []
    paires = defaultdict(list)
    for x in vivier:
        if x.get("paire") is None:
            ecarts.append(f"énoncé sans paire : monde {x['w']}, {x['etiquette']}")
        else:
            paires[x["paire"]].append(x)
    for p, m in paires.items():
        et = sorted(x["etiquette"] for x in m)
        if len(m) != 2 or et[1] != V or et[0] not in (FT, PG):
            ecarts.append(f"paire {p} : composition {et}")
            continue
        a, b = m
        if a["w"] != b["w"]:
            ecarts.append(f"paire {p} : deux mondes")
        if squelette(a["texte"]) != squelette(b["texte"]):
            ecarts.append(f"paire {p} : squelettes différents")
        if a["texte"] == b["texte"]:
            ecarts.append(f"paire {p} : même énoncé")
    # proportions : dans chaque monde, chaque squelette porte autant de paires à faux tôt que de paires à piège
    compte = defaultdict(lambda: defaultdict(lambda: [0, 0, 0]))
    for x in vivier:
        compte[x["w"]][squelette(x["texte"])][(V, FT, PG).index(x["etiquette"])] += 1
    for w, d in compte.items():
        for sq, (nv, nft, npg) in d.items():
            if nft != npg or nv != nft + npg:
                ecarts.append(f"monde {w} : un squelette porte {nv} vérités, {nft} faux tôt, {npg} pièges")
    # la paire est l'unité de tirage de la sous-banque
    servis = defaultdict(int)
    for x in sous_banque:
        servis[x.get("paire")] += 1
    for p, n in servis.items():
        if p is None or n != 2:
            ecarts.append(f"sous-banque : paire {p} servie {n} fois sur 2")
    return ecarts


# ------------------------------------------------------------------------------------------------ conditions
ENSEMBLES = (("faux_tot", lambda x: x["etiquette"] == FT), ("pieges", lambda x: x["etiquette"] == PG),
             ("tous_les_faux", lambda x: x["y"]))


def exces_par_ensemble(sous_banque: list, scores: dict, regle=rappel_au_prorata) -> dict:
    """Excès (rappel - 0,10) au point où 10 % des vrais de la sous-banque sont déclarés faux, pour les trois ensembles.
    None si un ensemble est vide ou si un score manque (« non calculable »)."""
    if any(x["cle"] not in scores for x in sous_banque):
        return {nom: None for nom, _ in ENSEMBLES}
    vrais = [scores[x["cle"]] for x in sous_banque if not x["y"]]
    out = {}
    for nom, sel in ENSEMBLES:
        r = regle(vrais, [scores[x["cle"]] for x in sous_banque if sel(x)])
        out[nom] = None if r is None else float(r - Fraction(1, 10))
    return out


def juger(valeurs: list, seuil: float, enfant: int, plancher_d_audit=None) -> dict:
    """Condition jugée sur les racines : moyenne, borne haute à 90 % ; « non calculable = non tenu ». Si
    `plancher_d_audit` est donné, une moyenne au-dessous de ce plancher (trop beau) est signalée pour audit."""
    if not valeurs or any(v is None for v in valeurs):
        return {"moyenne": None, "borne_haute": None, "tenue": False, "motif": "non calculable"}
    bh = borne_haute(valeurs, enfant)
    d = {"n": len(valeurs), "moyenne": round(float(np.mean(valeurs)), 4), "min": round(float(np.min(valeurs)), 4),
         "max": round(float(np.max(valeurs)), 4), "borne_haute": round(bh, 4), "seuil": seuil, "tenue": bool(bh <= seuil)}
    if plancher_d_audit is not None:
        d["audit_de_symetrie"] = bool(np.mean(valeurs) < plancher_d_audit)
    return d


# ------------------------------------------------------------------------------------------------ description
def valeurs_saillantes(texte: str, N: int) -> list:
    """Valeurs saillantes (juge Opus, § 2.4, lecture du diagnostic) : 0, 1, 2, N, N + 1, 2N, 3N, et c - 1, c, c + 1 pour
    tout entier c écrit dans l'énoncé, gardées dans [0 .. 3N]."""
    base = {0, 1, 2, N, N + 1, 2 * N, 3 * N}
    for g, v in lexer(texte):
        if g == "nombre" and v.isdigit():
            c = int(v)
            base |= {c - 1, c, c + 1}
    return sorted(v for v in base if 0 <= v <= 3 * N)


def trois_instances_au_hasard(n_instances: int, n_fausses: int) -> float:
    """Probabilité exacte qu'une au moins de trois instances distinctes tirées au hasard soit un contre-exemple."""
    M, m = int(n_instances), int(n_fausses)
    if m <= 0:
        return 0.0
    if M <= 3:
        return 1.0
    return 1.0 - math.comb(M - m, 3) / math.comb(M, 3)
