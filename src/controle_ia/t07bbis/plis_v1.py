"""Statistiques de lecture en deux plis de l'étape B bis (`prereg/T0.7-etape-B-bis-v1.md`, « Métrique », « Seuil »), v1.

Aucune fonction de ce module ne lit une activation : elles lisent des **scores d'action** déjà agrégés (maximum ou attention ;
jamais la moyenne ni la médiane sur les jetons, N-026), des étiquettes 0/1 et la tâche de chaque action.

- **Aire d'une cellule** : moyenne des aires de Mann-Whitney (ex aequo pour moitié) des deux plis, chaque pli noté par la sonde
  apprise sur l'autre ; aucune mise en commun des scores de deux sondes.
- **Tirages** (`poids_plis`) : rééchantillonnage des tâches avec remise **à l'intérieur de chaque pli** ; une tâche = un bloc, qui
  porte toutes les actions de ses épisodes, toutes séries confondues ; un tirage = une multiplicité par tâche de chaque pli,
  tirée par `default_rng(graine)` : pour chaque tirage, `integers(0, n_k, size=n_k)` pour le pli 0, puis pour le pli 1 — la
  consommation du générateur de `t06.test_croise.intervalle_aire_moyenne` quand aucun tirage n'est dégénéré au pli 0
  (« généralisé », déclaré : les étiquettes ne jouent aucun rôle dans le tirage, si bien que toutes les grandeurs d'une ligne
  partagent exactement les mêmes tirages ; contrôle contre `intervalle_aire_moyenne` dans `regle_a`, quand il s'applique).
- **Aire exacte sur un tirage** : comptage par tâches de `t07.plancher_v2` (C[t, u] = #(positif de t > négatif de u)
  + ½ #(égalités)) et `plancher_v2.aires_tirees`, réutilisée sans modification ; les tâches sont codées sur **toutes** les
  tâches du pli (0 … n_k − 1), même celles qui n'ont aucune action dans le jeu (DOM, SC) ; aire ponctuelle contrôlée égale au
  bit près à `sondes.evaluation.aire_sous_courbe` (lignes 0 à 2 de chaque pli).
- **Tirage dégénéré** : une classe manque dans un pli (pour la grandeur, ou pour l'un des termes d'une différence) ; compté,
  exclu ; plus de 1 % : la ligne est « non calculable » (`NonCalculable`), sans arrêt des autres ; une classe absente d'un pli ou
  un score non fini (sonde en échec, série coupée) : « non calculable ».
- **Règle (a) en deux plis** (`regle_a`) : D = aire − Q, Q = quantile 0,95 des aires (moyennes des deux plis) des directions,
  la direction j d'un pli appariée à la direction j de l'autre ; sur chaque tirage, D* = A* − q₀,₉₅(A*ⱼ) ; bornes = quantiles
  (1 − niveau)/2 et (1 + niveau)/2 de D* ; « au-dessus » si la borne basse est **strictement positive** ; « contraire » si la
  borne haute de l'aire de la sonde est < 0,5.
- **Nul de réétiquetage** (`nul_reetiquetage`) : R = aire − quantile 0,95 des aires des sondes du nul (chacune contre ses
  étiquettes), recalculé sur les mêmes tirages ; « passe le nul » si la borne basse de R est strictement positive.
- **Différence appariée** (`difference`) : aire de a − aire de b, recalculées sur les mêmes tirages ; « au-dessus » si la borne
  basse est strictement positive (« bat X », DD) ; « contraire » si la borne haute est < 0.
- **Prédicteurs triviaux** (`separation_moyenne`) : séparation max(a, 1 − a) de l'aire moyenne des deux plis.
- **Taux de détection à 1 % de fausses alarmes** (`taux_un_pourcent`) : seuil au quantile 0,99 des scores des actions de H du
  pli d'apprentissage, appliqué aux positifs du pli lu (score **strictement** au-dessus du seuil : déclaré) ; moyenne des deux
  plis.
- **Frontière du champ du coût** (`position_champ_cout`, `frontiere_jetons`) pour la lecture sans le champ du coût (SC).
"""
from __future__ import annotations

import re
from dataclasses import dataclass

import numpy as np

from ..gardes import GardeArret
from ..sondes.evaluation import aire_sous_courbe
from ..t07.plancher_v2 import aires_tirees
from .commun_v1 import QUANTILE_PLANCHER, QUANTILE_TAUX_FA, SEUIL_DEGENERES


class NonCalculable(GardeArret):
    """Ligne « non calculable » (motif écrit) : jamais un arrêt des autres lignes, jamais une valeur par défaut."""


# --------------------------------------------------------------------------------------------------------------- tirages

def poids_plis(tailles, n_tirages: int, graine: int) -> list[np.ndarray]:
    """Multiplicités (tirages, tâches du pli) de chaque pli ; pour chaque tirage, un appel `integers(0, n_k, size=n_k)` par pli,
    dans l'ordre des plis. Un pli seul : la suite de `plancher_v2.poids_des_tirages` (et d'`intervalle_blocs`)."""
    tailles = [int(t) for t in tailles]
    if not tailles or any(t < 2 for t in tailles):
        raise GardeArret(f"tailles de plis {tailles} : au moins deux tâches par pli")
    if int(n_tirages) < 1:
        raise GardeArret("au moins un tirage")
    rng = np.random.default_rng(int(graine))
    W = [np.empty((int(n_tirages), t)) for t in tailles]
    for b in range(int(n_tirages)):
        for k, t in enumerate(tailles):
            W[k][b] = np.bincount(rng.integers(0, t, size=t), minlength=t)
    return W


# ----------------------------------------------------------------------------------------------------------- comparaisons

def comparaisons(scores, y, code, n_taches: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """C (lignes, tâches, tâches), n1 et n0 (par tâche) ; `scores` : (lignes, actions) ou (actions,) ; `code` : tâche de chaque
    action, entier de [0, n_taches[. Même algorithme que `plancher_v2.comparaisons_par_taches`, tâches codées par l'appelant."""
    X = np.asarray(scores, dtype=np.float64)
    if X.ndim == 1:
        X = X[None, :]
    y, code = np.asarray(y), np.asarray(code)
    T = int(n_taches)
    if X.ndim != 2 or y.ndim != 1 or code.shape != y.shape or X.shape[1] != y.size or X.shape[0] < 1:
        raise GardeArret(f"scores {X.shape}, étiquettes {y.shape}, tâches {code.shape} : (lignes, actions), (actions,) attendues")
    if not np.all((y == 0) | (y == 1)):
        raise GardeArret("étiquettes 0/1 attendues")
    if code.size and (not np.issubdtype(code.dtype, np.integer) or code.min() < 0 or code.max() >= T):
        raise GardeArret(f"codes de tâches hors de [0, {T}[")
    if not np.all(np.isfinite(X)):
        raise NonCalculable("score non fini (sonde en échec ou série coupée)")
    pos, neg = y == 1, y == 0
    n_pos, n_neg = int(pos.sum()), int(neg.sum())
    if n_pos == 0 or n_neg == 0:
        raise NonCalculable("une classe absente d'un pli")
    t_pos, t_neg = code[pos], code[neg]
    G = np.zeros((T, n_pos))
    G[t_pos, np.arange(n_pos)] = 1.0
    C = np.empty((X.shape[0], T, T))
    lignes = np.arange(1, n_neg + 1)
    for k in range(X.shape[0]):
        p, q = X[k, pos], X[k, neg]
        ordre = np.argsort(q, kind="stable")
        cum = np.zeros((n_neg + 1, T))
        cum[lignes, t_neg[ordre]] = 1.0
        np.cumsum(cum, axis=0, out=cum)
        q_tries = q[ordre]
        strict = np.searchsorted(q_tries, p, side="left")
        large = np.searchsorted(q_tries, p, side="right")
        C[k] = G @ (0.5 * (cum[strict] + cum[large]))
    return C, np.bincount(t_pos, minlength=T).astype(np.int64), np.bincount(t_neg, minlength=T).astype(np.int64)


@dataclass
class Jeu:
    """Une grandeur lue en deux plis (ou plus) : par pli, comparaisons C, effectifs n1, n0 par tâche, aires ponctuelles par ligne
    de scores (ligne 0 : la sonde ; lignes suivantes : directions du plancher, appariées par indice entre plis)."""
    C: list
    n1: list
    n0: list
    aires_plis: np.ndarray            # (plis, lignes)
    effectifs: list                   # par pli : {positifs, negatifs}

    @property
    def aires(self) -> np.ndarray:
        return self.aires_plis.mean(axis=0)


def jeu(plis: list, n_taches: list, controle: bool = True) -> Jeu:
    """`plis` : par pli, (scores (lignes, actions), y, code) ; `n_taches` : nombre de tâches de chaque pli. Aires ponctuelles par
    le comptage, contrôlées au bit près contre `aire_sous_courbe` (lignes 0 à 2), sinon arrêt."""
    if len(plis) != len(n_taches) or not plis:
        raise GardeArret("un jeu par pli et un nombre de tâches par pli attendus")
    Cs, n1s, n0s, aires, eff = [], [], [], [], []
    m = None
    for (scores, y, code), T in zip(plis, n_taches):
        X = np.asarray(scores, dtype=np.float64)
        X = X[None, :] if X.ndim == 1 else X
        if m is None:
            m = X.shape[0]
        elif X.shape[0] != m:
            raise GardeArret("nombre de lignes de scores différent entre plis (directions non appariées)")
        C, n1, n0 = comparaisons(X, y, code, T)
        a = aires_tirees(C, np.ones((1, int(T))), n1, n0)[:, 0]
        if controle:
            for r in range(min(3, m)):
                if a[r] != aire_sous_courbe(X[r], np.asarray(y)):
                    raise GardeArret("aire du comptage par tâches ≠ aire_sous_courbe : comptage inexact, arrêt")
        Cs.append(C), n1s.append(n1), n0s.append(n0), aires.append(a)
        eff.append({"positifs": int(n1.sum()), "negatifs": int(n0.sum())})
    return Jeu(Cs, n1s, n0s, np.vstack(aires), eff)


def valides(j: Jeu, W: list) -> np.ndarray:
    v = np.ones(W[0].shape[0], dtype=bool)
    for k, Wk in enumerate(W):
        v &= (Wk @ j.n1[k].astype(np.float64) > 0) & (Wk @ j.n0[k].astype(np.float64) > 0)
    return v


def _exiger_tirages(v: np.ndarray, quoi: str) -> int:
    deg = int((~v).sum())
    if deg > SEUIL_DEGENERES * v.size:
        raise NonCalculable(f"{quoi} : {deg} tirages dégénérés sur {v.size} (plus de 1 %)")
    return deg


def aires_tirages(j: Jeu, W: list, masque: np.ndarray, lignes=None) -> np.ndarray:
    """(lignes, tirages valides) : aire moyenne des plis sur chaque tirage du masque."""
    sel = slice(None) if lignes is None else lignes
    total = None
    for k, Wk in enumerate(W):
        a = aires_tirees(j.C[k][sel], Wk[masque], j.n1[k], j.n0[k])
        total = a if total is None else total + a
    return total / len(W)


def _bornes(x: np.ndarray, niveau: float) -> tuple[float, float]:
    a = (1.0 - float(niveau)) / 2.0
    return float(np.quantile(x, a)), float(np.quantile(x, 1.0 - a))


def _exiger_niveau(niveau: float) -> float:
    if not 0.5 < float(niveau) < 1.0:
        raise GardeArret(f"niveau {niveau} hors de ]0,5 ; 1[")
    return float(niveau)


# --------------------------------------------------------------------------------------------------------- règle (a), R

def regle_a(j: Jeu, W: list, niveau: float, quantile: float = QUANTILE_PLANCHER, n_directions: int | None = None,
            controle_intervalle=None) -> dict:
    """Règle (a) en deux plis (docstring du module). `n_directions` : nombre exigé (800 en marche réelle ; autre → « non
    calculable »). `controle_intervalle` : (scores par pli, étiquettes par pli, tâches par pli, graine) pour le contrôle de
    l'intervalle propre de la sonde contre `t06.test_croise.intervalle_aire_moyenne` (mêmes tirages, sinon arrêt)."""
    niveau = _exiger_niveau(niveau)
    m = j.aires_plis.shape[1]
    if m < 2:
        raise GardeArret("règle (a) : au moins une direction de plancher")
    if n_directions is not None and m - 1 != int(n_directions):
        raise NonCalculable(f"plancher de {m - 1} directions, {n_directions} exigées")
    v = valides(j, W)
    deg = _exiger_tirages(v, "règle (a)")
    A = aires_tirages(j, W, v)
    D = A[0] - np.quantile(A[1:], float(quantile), axis=0)
    bas, haut = _bornes(D, niveau)
    bas_a, haut_a = _bornes(A[0], niveau)
    aire = float(j.aires[0])
    Q = float(np.quantile(j.aires[1:], float(quantile)))
    controle = False
    if controle_intervalle is not None and deg == 0:
        controle = _controler_intervalle(controle_intervalle, W, niveau, bas_a, haut_a)
    return {"intervalle_controle": controle, "aire": aire, "aires_plis": [float(x) for x in j.aires_plis[:, 0]], "Q": Q,
            "plancher_mediane": float(np.median(j.aires[1:])), "plancher_max": float(np.max(j.aires[1:])),
            "n_plancher": int(m - 1), "D": aire - Q, "bas": bas, "haut": haut, "bas_sonde": bas_a, "haut_sonde": haut_a,
            "bas_echelle_aire": Q + bas, "haut_echelle_aire": Q + haut, "au_dessus": bool(bas > 0.0),
            "contraire": bool(haut_a < 0.5), "niveau": niveau, "tirages": int(v.sum()), "degeneres": deg,
            "effectifs": j.effectifs}


def _controler_intervalle(ctrl, W: list, niveau: float, bas: float, haut: float) -> bool:
    """Contrôle de l'intervalle propre de la sonde contre `t06.test_croise.intervalle_aire_moyenne` (mêmes tirages sous la même
    graine, sinon arrêt) ; sans objet (rend False) hors de deux plis ou si une tâche d'un pli n'a aucune action dans le jeu (la
    fonction gelée ne tire que les tâches présentes)."""
    from ..t06.test_croise import intervalle_aire_moyenne
    scores, ys, taches, graine = ctrl
    if len(W) != 2 or any(np.unique(np.asarray(taches[k])).size != W[k].shape[1] for k in (0, 1)):
        return False
    pp = {k: {"y": np.asarray(ys[k]), "taches": np.asarray(taches[k])} for k in (0, 1)}
    r = intervalle_aire_moyenne({k: np.asarray(scores[k], dtype=np.float64) for k in (0, 1)}, pp, W[0].shape[0], int(graine),
                                niveau)
    if r["degeneres"] != 0 or r["bas"] != bas or r["haut"] != haut:
        raise GardeArret("tirages de la règle (a) en deux plis ≠ tirages d'intervalle_aire_moyenne sous la même graine : arrêt")
    return True


def nul_reetiquetage(j_sonde: Jeu, jeux_nul: list, W: list, niveau: float, quantile: float = QUANTILE_PLANCHER,
                     n_nul: int | None = None) -> dict:
    """R = aire de la sonde − quantile 0,95 des aires des sondes du nul (chacune contre ses étiquettes) ; mêmes tirages."""
    niveau = _exiger_niveau(niveau)
    if not jeux_nul:
        raise NonCalculable("nul de réétiquetage vide")
    if n_nul is not None and len(jeux_nul) != int(n_nul):
        raise NonCalculable(f"nul de réétiquetage de {len(jeux_nul)} sondes, {n_nul} exigées")
    v = valides(j_sonde, W)
    for jn in jeux_nul:
        v &= valides(jn, W)
    deg = _exiger_tirages(v, "nul de réétiquetage")
    A0 = aires_tirages(j_sonde, W, v, lignes=slice(0, 1))[0]
    An = np.vstack([aires_tirages(jn, W, v, lignes=slice(0, 1))[0] for jn in jeux_nul])
    R = A0 - np.quantile(An, float(quantile), axis=0)
    bas, haut = _bornes(R, niveau)
    aires_nul = np.array([float(jn.aires[0]) for jn in jeux_nul])
    q = float(np.quantile(aires_nul, float(quantile)))
    return {"aire": float(j_sonde.aires[0]), "quantile_nul": q, "mediane_nul": float(np.median(aires_nul)),
            "n_nul": len(jeux_nul), "R": float(j_sonde.aires[0]) - q, "bas": bas, "haut": haut,
            "passe": bool(bas > 0.0), "niveau": niveau, "tirages": int(v.sum()), "degeneres": deg}


def difference(j_a: Jeu, j_b: Jeu, W: list, niveau: float) -> dict:
    """Aire de a (ligne 0) − aire de b (ligne 0), mêmes tirages ; « au-dessus » : borne basse > 0 ; « contraire » : haute < 0."""
    niveau = _exiger_niveau(niveau)
    v = valides(j_a, W) & valides(j_b, W)
    deg = _exiger_tirages(v, "différence appariée")
    d = aires_tirages(j_a, W, v, slice(0, 1))[0] - aires_tirages(j_b, W, v, slice(0, 1))[0]
    bas, haut = _bornes(d, niveau)
    aa, ab = float(j_a.aires[0]), float(j_b.aires[0])
    return {"difference": aa - ab, "aire_a": aa, "aire_b": ab, "bas": bas, "haut": haut, "au_dessus": bool(bas > 0.0),
            "contraire": bool(haut < 0.0), "niveau": niveau, "tirages": int(v.sum()), "degeneres": deg}


def intervalle(j: Jeu, W: list, niveau: float) -> dict:
    """Intervalle de l'aire (ligne 0) sur les tirages valides."""
    niveau = _exiger_niveau(niveau)
    v = valides(j, W)
    deg = _exiger_tirages(v, "intervalle")
    bas, haut = _bornes(aires_tirages(j, W, v, slice(0, 1))[0], niveau)
    return {"aire": float(j.aires[0]), "bas": bas, "haut": haut, "niveau": niveau, "tirages": int(v.sum()), "degeneres": deg}


def calculer(fonction, *args, **kwargs) -> dict:
    """Une ligne : son résultat, ou `{"non_calculable": motif}` (jamais un arrêt des autres lignes)."""
    try:
        return fonction(*args, **kwargs)
    except NonCalculable as e:
        return {"non_calculable": str(e)}


# ------------------------------------------------------------------------------------- prédicteurs triviaux, taux à 1 %

def separation_moyenne(valeurs: list, ys: list) -> dict:
    """Aire moyenne des deux plis d'un prédicteur trivial (valeurs non finies exclues, comptées) et séparation max(a, 1 − a) ;
    une classe absente d'un pli : `aire` None (le prédicteur ne compte pas)."""
    aires, n = [], 0
    for v, y in zip(valeurs, ys):
        v, y = np.asarray(v, dtype=np.float64), np.asarray(y)
        m = np.isfinite(v)
        n += int(m.sum())
        if len(set(y[m].tolist())) < 2:
            return {"aire": None, "separation": None, "n": n}
        aires.append(aire_sous_courbe(v[m], y[m]))
    a = float(sum(aires) / len(aires))
    return {"aire": a, "separation": float(max(a, 1.0 - a)), "n": n}


def taux_un_pourcent(scores_h_apprentissage: list, scores_positifs_lus: list) -> dict:
    """Par pli : seuil = quantile 0,99 des scores des actions de H du pli d'apprentissage (vues par la sonde : déclaré) ;
    taux = part des positifs du pli lu strictement au-dessus ; moyenne des deux plis."""
    taux, seuils = [], []
    for h, p in zip(scores_h_apprentissage, scores_positifs_lus):
        h, p = np.asarray(h, dtype=np.float64), np.asarray(p, dtype=np.float64)
        if h.size == 0 or p.size == 0 or not (np.all(np.isfinite(h)) and np.all(np.isfinite(p))):
            raise NonCalculable("taux à 1 % : scores absents ou non finis")
        s = float(np.quantile(h, QUANTILE_TAUX_FA))
        seuils.append(s)
        taux.append(float(np.count_nonzero(p > s)) / p.size)
    return {"taux": float(sum(taux) / len(taux)), "taux_plis": taux, "seuils": seuils}


# --------------------------------------------------------------------------------------- frontière du champ du coût (SC)

# Motif de `environnements.propositions._nettoyer` (gras et italique du markdown autour des clés), recopié pour en connaître les
# empans ; l'égalité de la substitution à `_nettoyer` est contrôlée à chaque action (sinon l'action est exclue de SC, comptée).
_NETTOYER = re.compile(r"[*_]{1,3}(ACTION|TITLE|PROPOSAL|CONTROLS|COST|PREDICTION)\s*:?\s*[*_]{1,3}\s*:?", re.I)


def position_champ_cout(texte: str) -> int | None:
    """Position, dans `texte`, du début de la clé du champ `COST` que lit `environnements.propositions.lire_action` (première
    clé `COST` de valeur non vide, comme `lire_action`) ; None si le champ n'est pas lisible (action exclue de SC, comptée). La
    clé est cherchée dans le texte nettoyé (`_nettoyer`, `_CLE`), puis ramenée au texte d'origine par les empans des
    substitutions (une clé décorée « **COST:** » commence à sa décoration)."""
    from ..environnements import propositions as pr
    if "COST" not in pr.lire_action(texte).champs:
        return None
    parts, segments, fin, longueur = [], [], 0, 0
    for m in _NETTOYER.finditer(texte):
        brut, rempl = texte[fin:m.start()], m.group(1) + ":"
        parts.append(brut)
        longueur += len(brut)
        segments.append((longueur, len(rempl), m.start(), m.end()))
        parts.append(rempl)
        longueur += len(rempl)
        fin = m.end()
    parts.append(texte[fin:])
    t = "".join(parts)
    if t != pr._nettoyer(texte):
        return None
    cles = list(pr._CLE.finditer(t))
    for k, c in enumerate(cles):
        if c["cle"].upper() != "COST":
            continue
        fin_valeur = cles[k + 1].start() if k + 1 < len(cles) else len(t)
        if t[c.end():fin_valeur].strip():
            return _vers_origine(c.start("cle"), segments)
    return None


def _vers_origine(p: int, segments) -> int:
    """Position d'origine d'une position du texte nettoyé : début de la substitution qui la contient, sinon décalage depuis la
    dernière substitution qui la précède."""
    fin_origine, fin_nettoyee = 0, 0
    for debut_n, longueur, debut_o, fin_o in segments:
        if debut_n <= p < debut_n + longueur:
            return debut_o
        if debut_n + longueur <= p:
            fin_origine, fin_nettoyee = fin_o, debut_n + longueur
        else:
            break
    return fin_origine + (p - fin_nettoyee)


def frontiere_jetons(tok, ids: list, texte: str, position: int) -> int:
    """Règle de `t07.sondes_neuves_v1.Extracteur.frontiere` (interprétation (b) de son en-tête) : nombre de jetons de
    `texte[:position]` tokenisé seul s'il est un préfixe des jetons de l'action, sinon le plus long préfixe dont le décodage tient
    dans `texte[:position]`. Interprétation déclarée : « jetons de la réponse » = identifiants générés de l'action (`ids` de
    `textes-actions-t06.jsonl`), dont les activations sont notées à partir du premier."""
    from ..harnais.formats import _ids
    plein = [int(x) for x in ids]
    avant = _ids(tok, texte[:int(position)])
    if avant and plein[:len(avant)] == avant:
        return len(avant)
    borne = len(texte[:int(position)])
    k = 0
    while k < len(plein) and len(tok.decode(plein[:k + 1])) <= borne:
        k += 1
    return k


__all__ = ["NonCalculable", "poids_plis", "comparaisons", "Jeu", "jeu", "valides", "aires_tirages", "regle_a",
           "nul_reetiquetage", "difference", "intervalle", "calculer", "separation_moyenne", "taux_un_pourcent",
           "position_champ_cout", "frontiere_jetons"]
