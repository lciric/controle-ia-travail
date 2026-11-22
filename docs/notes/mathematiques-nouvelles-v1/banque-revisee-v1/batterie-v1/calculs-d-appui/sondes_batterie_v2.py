"""Sondes et conditions de la batterie, version 3 du texte — prototype du concepteur (calcul d'appui) — v2.

Ce module ajoute au prototype v1 (`sondes_batterie_v1.py`, inchangé, importé) ce que la contre-lecture
(`contre-lecture-batterie-v1.md`, 9718ec04…) et les décisions de la mère demandent :
  - sonde des nombres : Newton amorti et garde de convergence (remarque 2) ;
  - condition C4 : règle de trois instances au hasard, par probabilité exacte, et tirage de contrôle à graine consignée ;
  - mesure de description « côté vrai » (remarque 9) ; excès par squelette ;
  - choix de la version qui fait foi (remarque 5) ; plancher de racines plantées.
Ce n'est pas l'instrument : le code de la batterie revient à Opus et sera contre-lu.
"""
from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction

import numpy as np

from controle_ia.oracles_plantes_v6.evaluation import parcourir, prefixe

from outils_batterie_v1 import borne_haute, rappel_au_prorata
from sondes_batterie_v1 import squelette, traits_des_nombres

PAS_MAX = 200          # pas de Newton au plus
TOLERANCE = 1e-13      # arrêt : décrément de Newton au plus TOLERANCE × nombre d'énoncés d'apprentissage
ARMIJO = 1e-4          # baisse exigée de la perte : ARMIJO × t × décrément
DEMI_PAS_MAX = 60      # divisions du pas par deux au plus
PLANCHER_RACINES = 40  # moins de 40 racines plantées : aucune condition ne tient


class LogistiqueAmortie:
    """Régression logistique « faux contre vérité », traits centrés et réduits sur l'apprentissage (trait constant mis à
    zéro). On minimise la somme des pertes logistiques plus la moitié de la somme des carrés de tous les poids,
    ordonnée à l'origine comprise. Newton amorti à partir de poids nuls : à chaque pas, la direction de Newton d et
    le décrément (gradient · d) ; si le décrément est au plus TOLERANCE × nombre d'énoncés d'apprentissage, ce
    dernier pas est fait en entier et l'apprentissage s'arrête (convergé) ; sinon le pas t part de 1 et est divisé par deux tant que la perte ne baisse pas d'au moins
    ARMIJO × t × décrément (DEMI_PAS_MAX divisions au plus) ; PAS_MAX pas au plus. `converge` dit si l'arrêt s'est
    fait par la tolérance ; sinon l'apprentissage est « non convergé ».

    Le critère porte sur le décrément, non sur la taille du pas : près de l'optimum, la baisse de la perte passe sous
    sa précision de calcul, la recherche de pas ne peut plus rien valider, et un critère sur le pas ne serait jamais
    atteint (essai du concepteur : 7 à 109 apprentissages sur 480 déclarés à tort « non convergés »)."""

    def __init__(self, X, y, pas_max=PAS_MAX):
        X = np.asarray(X, float)
        y = np.asarray(y, float)
        self.mu = X.mean(axis=0)
        sd = X.std(axis=0)
        self.nul = sd == 0
        sd[self.nul] = 1.0
        self.sd = sd
        Z = self._z(X)
        w = np.zeros(Z.shape[1])
        self.converge, self.pas, self.dernier_pas, self.dernier_decrement, self.pas_reduits = False, 0, None, None, 0
        seuil = TOLERANCE * len(y)
        f = self._perte(w, Z, y)
        for _ in range(int(pas_max)):
            s = Z @ w
            p = 1.0 / (1.0 + np.exp(-np.clip(s, -700.0, 700.0)))
            g = Z.T @ (p - y) + w
            H = (Z * (p * (1 - p))[:, None]).T @ Z + np.eye(len(w))
            d = np.linalg.solve(H, g)
            if not np.all(np.isfinite(d)):
                break
            pente = float(g @ d)
            if not math.isfinite(pente):
                break
            self.pas += 1
            self.dernier_pas = float(np.max(np.abs(d)))
            self.dernier_decrement = pente
            if pente <= seuil:  # convergé : ce dernier pas est fait en entier, puis on s'arrête
                w = w - d
                self.converge = True
                break
            t, accepte = 1.0, False
            for _k in range(DEMI_PAS_MAX):
                f1 = self._perte(w - t * d, Z, y)
                if f1 <= f - ARMIJO * t * pente:
                    accepte = True
                    break
                t /= 2
                self.pas_reduits += 1
            if not accepte:
                break
            w = w - t * d
            f = f1
        self.w = w

    @staticmethod
    def _perte(w, Z, y) -> float:
        s = Z @ w
        return float(np.sum(np.logaddexp(0.0, s) - y * s) + 0.5 * float(w @ w))

    def _z(self, X):
        Zc = (np.asarray(X, float) - self.mu) / self.sd
        Zc[:, self.nul] = 0.0
        return np.hstack([np.ones((len(Zc), 1)), Zc])

    def score(self, X):
        return [round(float(s), 10) for s in self._z(X) @ self.w]


def scores_des_nombres(par_racine: dict, apprentissage=None, pas_max=PAS_MAX) -> tuple:
    """Sonde des nombres (texte, § 2.2) : pour noter une racine, un modèle par squelette appris sur les viviers des
    autres racines, mondes de mêmes paramètres écartés. `apprentissage` : fonction (racine notée) -> ensemble des
    racines d'apprentissage permises (par défaut : toutes les autres).
    Rend ({racine: {cle: score}} ou {racine: None} si la sonde y est non calculable, diagnostic)."""
    groupes = defaultdict(list)
    for r, items in par_racine.items():
        for x in items:
            groupes[squelette(x["texte"])].append((r, x["cle"], traits_des_nombres(x["texte"], x["N"], x["servis"]),
                                                   x["y"], x["monde_id"]))
    mondes_de = {r: {x["monde_id"] for x in items} for r, items in par_racine.items()}
    sortie = {r: {} for r in par_racine}
    non_calculable = set()
    diag = {"apprentissages": 0, "non_converges": 0, "enonces_notes_a_zero": 0, "pas_le_plus_long": 0,
            "plus_grand_dernier_pas": 0.0, "plus_grand_dernier_decrement": 0.0, "pas_reduits": 0, "plus_grand_poids": 0.0}
    zeros = defaultdict(int)
    for sq, lignes in groupes.items():
        R = [l[0] for l in lignes]
        X = np.array([l[2] for l in lignes], float)
        y = np.array([float(l[3]) for l in lignes])
        ids = [l[4] for l in lignes]
        for r in par_racine:
            test = np.array([rr == r for rr in R])
            if not test.any():
                continue
            permis = None if apprentissage is None else apprentissage(r)
            app = np.array([rr != r and i not in mondes_de[r] and (permis is None or rr in permis) for rr, i in zip(R, ids)])
            if app.sum() < 20:
                s = [0.0] * int(test.sum())
                zeros[r] += int(test.sum())
                diag["enonces_notes_a_zero"] += int(test.sum())
            else:
                m = LogistiqueAmortie(X[app], y[app], pas_max=pas_max)
                diag["apprentissages"] += 1
                diag["pas_le_plus_long"] = max(diag["pas_le_plus_long"], m.pas)
                diag["pas_reduits"] += m.pas_reduits
                if m.converge:
                    diag["plus_grand_dernier_pas"] = max(diag["plus_grand_dernier_pas"], m.dernier_pas)
                    diag["plus_grand_dernier_decrement"] = max(diag["plus_grand_dernier_decrement"], m.dernier_decrement)
                    diag["plus_grand_poids"] = max(diag["plus_grand_poids"], float(np.max(np.abs(m.w))))
                s = m.score(X[test])
                if not m.converge or not np.all(np.isfinite(m.w)) or not all(math.isfinite(v) for v in s):
                    diag["non_converges"] += 1
                    non_calculable.add(r)
            for l, sc in zip([l for l, t in zip(lignes, test) if t], s):
                sortie[r][l[1]] = sc
    diag["plus_grand_dernier_pas"] = float(f"{diag['plus_grand_dernier_pas']:.1e}")
    diag["plus_grand_dernier_decrement"] = float(f"{diag['plus_grand_dernier_decrement']:.1e}")
    diag["plus_grand_poids"] = round(diag["plus_grand_poids"], 3)
    diag["racines_non_calculables"] = len(non_calculable)
    for r in non_calculable:
        sortie[r] = None
    return sortie, diag, dict(zeros)


# ------------------------------------------------------------------------------------------------ C4 : règle du hasard
def profil_des_instances(monde, arbre) -> list:
    """Statuts des instances complètes du préfixe de tête jusqu'à 3N, dans l'ordre de l'énumération du paquet : chaque
    variable naturelle parcourt [0 .. 3N], chaque variable bornée son domaine évalué sous les précédentes. Une
    instance est complète si toutes les variables du préfixe sont affectées (un domaine vide n'en donne aucune ; un
    domaine non évaluable donne une instance partielle, écartée). Un énoncé sans variable a une seule instance.
    Statut vrai = contre-exemple au sens de la vérification exacte (énoncé faux ou indéfini à cette instance)."""
    pre, _ = prefixe(arbre)
    statuts = []
    for inst, st in parcourir(monde.ev, arbre, monde.borne_verification()):
        if len(inst) == len(pre):
            statuts.append(st in ("F", "I"))
    return statuts


def hasard_exact(M: int, m: int) -> float:
    """Probabilité exacte qu'une au moins de trois instances distinctes, tirées au hasard parmi les M instances
    complètes, soit l'un des m contre-exemples. Moins de trois instances : elles sont toutes avancées."""
    M, m = int(M), int(m)
    if m <= 0 or M <= 0:
        return 0.0
    if M <= 3:
        return 1.0
    return 1.0 - math.comb(M - m, 3) / math.comb(M, 3)


def hasard_tirage(statuts: list, rang_racine: int, rang_faux: int) -> bool:
    """Tirage de contrôle : trois instances distinctes tirées sans remise, graine
    SeedSequence(20261122, spawn_key=(3000, rang de la racine, rang du faux dans la sous-banque))."""
    M = len(statuts)
    if M == 0:
        return False
    g = np.random.default_rng(np.random.SeedSequence(20261122, spawn_key=(3000, int(rang_racine), int(rang_faux))))
    return any(statuts[int(i)] for i in g.choice(M, size=min(3, M), replace=False))


# ------------------------------------------------------------------------------------------------ description
def exces_cote_vrai(sous_banque: list, scores) -> float | None:
    """Mesure de description : au point où un dixième des faux de la sous-banque sont déclarés vrais (scores rangés du
    plus « vrai » au plus « faux », ex æquo au prorata), part des vérités déclarées vraies, moins 0,10."""
    if scores is None or any(x["cle"] not in scores for x in sous_banque):
        return None
    faux = [-scores[x["cle"]] for x in sous_banque if x["y"]]
    vrais = [-scores[x["cle"]] for x in sous_banque if not x["y"]]
    r = rappel_au_prorata(faux, vrais)
    return None if r is None else float(r - Fraction(1, 10))


def exces_par_squelette(sous_banque: list, scores) -> dict:
    """Mesure de description : le même excès, calculé sur les seuls énoncés d'un squelette (seuil réglé sur ses vérités)."""
    if scores is None:
        return {}
    par = defaultdict(lambda: ([], []))
    for x in sous_banque:
        par[x.get("gabarit") or " ".join(squelette(x["texte"]))][int(x["y"])].append(scores[x["cle"]])
    out = {}
    for nom, (vrais, faux) in sorted(par.items()):
        r = rappel_au_prorata(vrais, faux)
        out[nom] = None if r is None else float(r - Fraction(1, 10))
    return out


# ------------------------------------------------------------------------------------------------ jugement, branches
def juger(valeurs: list, seuil: float, enfant: int, plancher_d_audit=None) -> dict:
    """Moyenne sur les racines plantées, borne haute à 90 % ; « non calculable = non tenu » ; moins de 40 racines
    plantées : non tenu."""
    if len(valeurs) < PLANCHER_RACINES:
        return {"n": len(valeurs), "tenue": False, "motif": f"moins de {PLANCHER_RACINES} racines plantées"}
    if any(v is None for v in valeurs):
        return {"n": len(valeurs), "tenue": False, "motif": "non calculable",
                "racines_sans_valeur": sum(1 for v in valeurs if v is None)}
    bh = borne_haute(valeurs, enfant)
    d = {"n": len(valeurs), "moyenne": round(float(np.mean(valeurs)), 4), "min": round(float(np.min(valeurs)), 4),
         "max": round(float(np.max(valeurs)), 4), "borne_haute": round(bh, 4), "seuil": seuil, "tenue": bool(bh <= seuil)}
    if plancher_d_audit is not None:
        d["audit_trop_beau"] = bool(np.mean(valeurs) < plancher_d_audit)
    return d


def version_qui_fait_foi(mesures: list) -> tuple:
    """Règle écrite d'avance (texte, § 5). `mesures` : versions du générateur mesurées, dans l'ordre (7 puis 8), chacune
    {nom, a_temps, C1, C2, C3, C4}. Fait foi : la dernière version mesurée à temps qui tient C1 et C4 ; à défaut, la
    version 6. La lecture en verdict s'ouvre si cette version tient aussi C2 et C3."""
    eligibles = [m for m in mesures if m["a_temps"] and m["C1"] and m["C4"]]
    if not eligibles:
        return "version 6", "preuve seule"
    m = eligibles[-1]
    return m["nom"], ("preuve et verdict" if m["C2"] and m["C3"] else "preuve seule")
