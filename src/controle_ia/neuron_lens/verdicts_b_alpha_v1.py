"""Verdicts de la tranche B-α de « Neuron Lens » (Llama 3.1 8B Instruct, lentilles publiques de Neuronpedia) — v1.

Met en œuvre, sans rien y changer, les sections « Seuil » (B), « Critères de lecture gelés » (tranche B-α) et l'audit « B-α, trop
beau » du texte gelé `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md`
(`34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131`), ainsi que les contrôles de B0 (`controle_lentille`) et le recalcul
de n (`n_par_couche`). Aucun modèle, aucun réseau : ce code lit des tableaux déjà calculés (sortie JSON de `causal_lens.py score`).

Forme des données (celle du JSON publié de `score`) : `table[cible][lentille]` est un dict avec les listes par couche `r_med`, `pass`,
`control_med` (indice = couche). Cibles : « steer 1x », « steer 4x », « ablate pos », « ablate win ». Lentilles de B-α : « logit »,
« J », « npJpp », « npR ». `n[cible]` : liste par couche des pôles retenus (64 par défaut).
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

CIBLES = ("steer 1x", "steer 4x", "ablate pos", "ablate win")
LENTILLES = ("logit", "J", "npJpp", "npR")
N_COUCHES = 32
N_POLES = 64
N_LISIBLE = 48
QWEN_COUCHES = 36


def couches(a: int, b: int) -> list[int]:
    return list(range(a, b + 1))


@dataclass
class Mesure:
    verdict: str  # « reproduit », « non reproduit », « partiel »
    details: dict = field(default_factory=dict)


@dataclass
class VerdictBAlpha:
    verdict: str  # « chaîne en défaut ou mode commun réel, audit » | « reproduit … » | « non reproduit … » | « partiel »
    defauts: list[str]
    trop_beau: list[str]
    b2: Mesure | None
    b3: Mesure | None
    b7: Mesure | None
    b4: dict


def _lisibles(n_cible, bande):
    return [l for l in bande if n_cible[l] >= N_LISIBLE]


def _bande(valeurs, n_cible, bande, ok, contraire):
    """Pour une bande : (toutes lisibles ok, plus de la moitié des lisibles « contraire », bande partielle)."""
    lis = _lisibles(n_cible, bande)
    partielle = (len(bande) - len(lis)) > len(bande) / 4
    tout_ok = bool(lis) and all(ok(valeurs[l]) for l in lis)
    nb_contraire = sum(contraire(valeurs[l]) for l in lis) if contraire else 0
    majorite_contraire = bool(lis) and nb_contraire > len(lis) / 2
    return tout_ok, majorite_contraire, partielle


def _mesure(clauses_ok, clauses_non):
    """clauses_ok : liste de (tout_ok, partielle) ; clauses_non : liste de booléens « non reproduit »."""
    if any(clauses_non):
        return "non reproduit"
    if all(ok and not part for ok, part in clauses_ok):
        return "reproduit"
    return "partiel"


def verdict_b2(t, n):
    s = t["steer 1x"]["npR"]
    ns = n["steer 1x"]
    r1 = _bande(s["r_med"], ns, couches(8, 15), lambda v: v >= 0.40, None)
    r2 = _bande(s["r_med"], ns, couches(16, 23), lambda v: v >= 0.60, lambda v: v < 0.30)
    r3 = _bande(s["r_med"], ns, couches(24, 27), lambda v: v >= 0.85, None)
    p = _bande(s["pass"], ns, couches(8, 27), lambda v: v >= 0.90, None)
    p_non = _bande(s["pass"], ns, couches(16, 27), lambda v: True, lambda v: v < 0.50)
    lis = _lisibles(ns, couches(0, 27))
    hors05 = sum(abs(s["control_med"][l]) > 0.05 for l in lis)
    hors10 = sum(abs(s["control_med"][l]) > 0.10 for l in lis)
    temoin_ok = hors05 <= 1 and hors10 == 0
    ok = [(r1[0], r1[2]), (r2[0], r2[2]), (r3[0], r3[2]), (p[0], p[2]), (temoin_ok, False)]
    non = [p_non[1], r2[1]]
    return Mesure(_mesure(ok, non), {"temoin_hors_005": hors05, "temoin_hors_010": hors10})


def verdict_b3(t, n):
    r = np.asarray(t["steer 1x"]["npR"]["r_med"]) - np.asarray(t["steer 1x"]["logit"]["r_med"])
    b = _bande(r, n["steer 1x"], couches(4, 15), lambda v: v >= 0.20, lambda v: v <= 0)
    return Mesure(_mesure([(b[0], b[2])], [b[1]]), {"ecart_min_4_15": float(np.min(r[4:16]))})


def verdict_b7(t, n):
    a = t["ablate win"]["npR"]["r_med"]
    na = n["ablate win"]
    bas = _bande(a, na, couches(0, 15), lambda v: v < 0.25, None)
    bas_non = _bande(a, na, couches(8, 15), lambda v: True, lambda v: v >= 0.40)
    haut = _bande(a, na, couches(26, 29), lambda v: v >= 0.50, lambda v: v < 0.30)
    return Mesure(_mesure([(bas[0], bas[2]), (haut[0], haut[2])], [bas_non[1], haut[1]]))


def ecarts_b4(t):
    s = t["steer 1x"]
    r = np.asarray(s["npR"]["r_med"])
    return {k: [float(x) for x in (r - np.asarray(s[k]["r_med"]))[4:24]] for k in ("J", "npJpp")}


def defauts_chaine(t, n, essais_ok=True, matrices_identite=False):
    d = []
    for c in CIBLES:
        for le in LENTILLES:
            cm = t[c][le]["control_med"]
            if any(abs(cm[l]) > 0.10 for l in couches(0, 27)):
                d.append(f"(a) témoin hors de ±0,10 : {c}, {le}")
    if any(n["steer 1x"][l] < N_POLES / 2 for l in couches(0, 27)):
        d.append("(b) pilotage sans effet")
    if any(t["steer 1x"]["logit"]["r_med"][l] < 0.80 for l in couches(28, 30)):
        d.append("(c) cas sain des logits manqué")
    if any(t["steer 1x"]["npR"]["r_med"][l] < 0.85 for l in couches(28, 30)):
        d.append("(c) cas sain de npR manqué")
    if not essais_ok:
        d.append("(d) essai ou fumée en échec")
    lg = np.asarray(t["steer 1x"]["logit"]["r_med"])
    for le in ("J", "npJpp", "npR"):
        if np.any(np.abs(np.asarray(t["steer 1x"][le]["r_med"])[:24] - lg[:24]) < 1e-3):
            d.append(f"(e) repli sur les logits : {le}")
    if matrices_identite:
        d.append("(e) matrice égale à l'identité")
    return d


def trop_beau(t):
    s = t["steer 1x"]["npR"]
    out = []
    if any(s["r_med"][l] >= 0.95 for l in couches(0, 7)):
        out.append("r_med ≥ 0,95 à une couche 0–7")
    if sum(abs(s["control_med"][l]) == 0 for l in couches(0, 27)) >= 2:
        out.append("control_med écrit 0 à au moins 2 couches 0–27")
    return out


def verdict(t, n=None, essais_ok=True, matrices_identite=False) -> VerdictBAlpha:
    n = n or {c: [N_POLES] * N_COUCHES for c in CIBLES}
    d = defauts_chaine(t, n, essais_ok, matrices_identite)
    tb = trop_beau(t)
    if d:
        return VerdictBAlpha("chaîne en défaut ou mode commun réel, audit", d, tb, None, None, None, ecarts_b4(t))
    b2, b3, b7 = verdict_b2(t, n), verdict_b3(t, n), verdict_b7(t, n)
    if b2.verdict == "reproduit" and b3.verdict == "reproduit":
        v = "reproduit avec la lentille R publique"
    elif "non reproduit" in (b2.verdict, b3.verdict):
        v = "non reproduit avec la lentille R publique"
    else:
        v = "partiel"
    return VerdictBAlpha(v, d, tb, b2, b3, b7, ecarts_b4(t))


def depuis_reference_qwen(table_qwen: dict) -> dict:
    """Référence publiée de Qwen3-8B convertie (texte gelé, B.3) : couche Llama l ← couche Qwen ⌊l × 36/32⌋ ; « R:dclm » joue
    `npR`, « J » joue `J` et `npJpp`, « logit » joue `logit`."""
    role = {"logit": "logit", "J": "J", "npJpp": "J", "npR": "R:dclm"}
    out = {}
    for c in CIBLES:
        out[c] = {}
        for le, src in role.items():
            q = table_qwen[c][src]
            out[c][le] = {k: [q[k][(l * QWEN_COUCHES) // N_COUCHES] for l in range(N_COUCHES)]
                          for k in ("r_med", "pass", "control_med")}
    return out


def controle_lentille(J: dict, n_attendu: int = 31, tol: float = 1e-6, couches_identite=range(0, 28)) -> list[str]:
    """Contrôle de B0 sur un fichier de lentille déjà lu (`{couche: matrice}`) : nombre de couches lues == 31, couches contiguës
    `0..n−1`, aucune matrice égale à l'identité (écart maximal en valeur absolue ≤ tol, en float32) aux couches 0 à 27."""
    pb = []
    cles = sorted(J)
    if cles != list(range(len(cles))):
        pb.append("couches non contiguës 0..n−1")
    if len(cles) != n_attendu:
        pb.append(f"nombre de couches lues {len(cles)} ≠ {n_attendu}")
    for l in couches_identite:
        if l in J:
            m = np.asarray(J[l], dtype=np.float32)
            if m.ndim == 2 and m.shape[0] == m.shape[1] and np.max(np.abs(m - np.eye(m.shape[0], dtype=np.float32))) <= tol:
                pb.append(f"matrice égale à l'identité à la couche {l}")
    return pb


def n_par_couche(picks, aleatoires, cibles: dict, fired, nv: int) -> dict:
    """Recalcul de n par la règle de `score` (copie de `causal_lens.py`, lignes ~300-315) : pour chaque couche et cible, nombre de
    pôles retenus parmi les neurones tirés au hasard (`is_rand`) : pôle dont la cible a une norme non nulle sur les `nv` lignes du
    tokeniseur ; pour l'ablation, pôle qui a des contextes (`fired`). `cibles[nom]` : tableau [picks, 2, V] ; `fired` : [picks, 2]
    booléen ; `picks` : liste de (couche, neurone) ; `aleatoires` : ensemble des (couche, neurone) tirés au hasard."""
    out = {c: [0] * N_COUCHES for c in cibles}
    fired = np.asarray(fired, dtype=bool)
    for c, t in cibles.items():
        t = np.asarray(t)
        effet = np.abs(t[:, :, :nv]).sum(-1) > 0  # [picks, 2]
        garde = effet if c.startswith("steer") else (effet & fired)
        for i, (l, neur) in enumerate(picks):
            if (l, neur) in aleatoires:
                out[c][l] += int(garde[i].sum())
    return out
