"""Verdicts de la tranche de l'ajustement de nos lentilles (lecture par lentille neuronale, Llama 3.1 8B Instruct, nos lentilles R et S) — v2.

Remplace la v1 (`verdicts_b_beta_v1.py`, archivée) selon la contre-lecture `docs/notes/neuron-lens-v1/correctifs-b-beta/contre-lecture-verdicts-b-beta-v1.md`
(à corriger : 4 majeures, 9 mineures, 4 points discutables).

Met en œuvre, sans rien y changer, les sections « Seuil », « Chaîne en défaut », « Critères de lecture gelés » (verdict d'ensemble,
B-6 et audit A6, B-7, audits A1 à A6) du texte gelé scellé
`docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md` (`f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454`).
Aucun modèle, aucun réseau, aucun code du dépôt voisin : des tables en entrée, des verdicts en sortie. Joué sur la machine (P.3,
étape 7) et, avant la course, sur les cas de P.4 (essais `tests/test_neuron_lens_verdicts_b_beta_v1.py`).

Deux temps : `declencheurs(entrees)` rend les audits à jouer sur la machine ; `verdict(entrees, audits)` rend le verdict unique, une
fois les audits joués (ou marqués « non joué »).

Lectures **reprises du code des verdicts de la tranche des lentilles publiques** (`verdicts_b_alpha_v3.py`, contre-lu) : le texte
gelé de cette tranche ne les écrit pas mot pour mot ; elles sont déclarées ici et soumises à la mère (point discutable de la
contre-lecture) :
- une clause « non reproduit » n'est pas jugée sur une bande partielle (plus du quart de couches non lisibles) : la mesure est alors
  « autre » (le texte : une telle bande rend la mesure « partielle ») ;
- le témoin de B-2 est compté sur les seules couches lisibles de 0 à 27 ;
- les différences de deux valeurs écrites à 4 décimales par `score` sont arrondies à 4 décimales avant comparaison ;
- les valeurs de `score` sont prises telles qu'écrites (4 décimales) ; toute autre valeur est refusée.
Lecture propre à cette tranche : la garde (a) porte aussi sur les lentilles des deux moitiés (« l'une des lentilles notées »).
Les valeurs de B-1 et de B-5 sont non arrondies (texte gelé, « Seuil ») ; les moyennes de B-5 sont calculées en fractions exactes
des valeurs données, pour qu'aucun bruit flottant ne décide d'une égalité (contre-lecture, M4).
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from fractions import Fraction

import numpy as np

CIBLES = ("steer 1x", "steer 4x", "ablate pos", "ablate win")
NOTRE_R = "R:dclm-llama"
MOITIES = ("R:dclm-llama-even", "R:dclm-llama-odd")
LENTILLES = ("logit", "J", "npJpp", "npR", NOTRE_R) + MOITIES
N_COUCHES = 32
N_POLES = 64
N_LISIBLE = 48
QWEN_COUCHES = 36
COUCHES_ACCORD = (2, 7, 12, 18, 23, 28)
CIBLES_STABILITE = {("R", "out"): 31, ("R", "mid"): 32, ("S", "mid"): 32, ("S", "out"): 32}
GARDES_MACHINE = ("d", "f", "g", "h", "i", "k", "n", "o", "p", "q", "r", "s")  # constatées sur la machine, entrées booléennes
CHAINE = "chaîne en défaut"
NON_CONCLU = "non conclu"
NON_REPRODUIT = "non reproduit avec nos lentilles"
REPRODUIT = "reproduit avec nos lentilles"
PARTIEL = "partiel"
NON_JOUE = "non joué"


def couches(a: int, b: int) -> list[int]:
    return list(range(a, b + 1))


def r4(x):
    return np.round(np.asarray(x, float), 4)


@dataclass
class Mesure:
    verdict: str  # « reproduit », « non reproduit », « autre », et pour B-5 « non lisible »
    details: dict = field(default_factory=dict)


@dataclass
class Entrees:
    """`score` : `table[cible][lentille]` (listes par couche `layer`, `r_med`, `pass`, `control_med`, 4 décimales) ; `n[cible]` : pôles
    retenus par couche (recalculés) ; `repere_npR` : `r_med` « steer 1x » de la série repère de B-α (32 valeurs) ; `stabilite` :
    `{(lentille, cible): [différence entre moitiés non arrondie par couche]}` ; `accord` : `{couche: accord du premier jeton}` aux six
    couches ; `reads` : couches de `reads_at_firings` (listes `read_S`, `silent`, 32 valeurs) ; `gardes` : `{lettre: True si en défaut}`
    pour les gardes constatées sur la machine (d, f à i, k, n à s) et `identite` (garde (e), matrices)."""
    score: dict
    n: dict
    repere_npR: list
    stabilite: dict
    accord: dict
    read_S: list
    silent: list
    gardes: dict


def valider_table(t: dict, n: dict, lentilles=LENTILLES) -> None:
    """Refuse toute table de `score` ou tout n incomplet, non fini ou mal formé (aussi pour la graine 1)."""
    for c in CIBLES:
        if c not in n or len(n[c]) != N_COUCHES:
            raise ValueError(f"n[{c}] absent ou sans {N_COUCHES} couches")
        if any(isinstance(x, bool) or not (isinstance(x, (int, np.integer)) and 0 <= x <= N_POLES) for x in n[c]):
            raise ValueError(f"n[{c}] hors de [0, {N_POLES}] ou non entier")
        for le in lentilles:
            if le not in t.get(c, {}):
                raise ValueError(f"lentille absente de score : {c}, {le}")
            s = t[c][le]
            if list(s["layer"]) != list(range(N_COUCHES)):
                raise ValueError(f"couches manquantes ou désordonnées : {c}, {le}")
            for k in ("r_med", "pass", "control_med"):
                v = np.asarray(s[k], float)
                if v.shape != (N_COUCHES,) or not np.all(np.isfinite(v)):
                    raise ValueError(f"valeur absente ou non finie : {c}, {le}, {k}")
                if not np.all(np.round(v, 4) == v):
                    raise ValueError(f"valeur non écrite à 4 décimales : {c}, {le}, {k}")


def valider(e: Entrees) -> None:
    """Refuse toute entrée incomplète, non finie ou mal formée (R5 : aucun repli silencieux). Une différence entre moitiés non finie
    n'est pas refusée : c'est la garde (g)."""
    valider_table(e.score, e.n)
    rep_ = np.asarray(e.repere_npR, float)
    if rep_.shape != (N_COUCHES,) or not np.all(np.isfinite(rep_)):
        raise ValueError("série repère sans 32 couches finies")
    for (le, ci), nb in CIBLES_STABILITE.items():
        if (le, ci) not in e.stabilite or len(e.stabilite[(le, ci)]) != nb:
            raise ValueError(f"différences entre moitiés absentes ou sans {nb} couches : {le}, {ci}")
    if sorted(e.accord) != list(COUCHES_ACCORD):
        raise ValueError(f"accord du premier jeton attendu aux couches {COUCHES_ACCORD}")
    if any(not math.isfinite(a) for a in e.accord.values()):
        raise ValueError("accord du premier jeton non fini")
    if len(e.read_S) != N_COUCHES or len(e.silent) != N_COUCHES:
        raise ValueError("read_S ou silent sans 32 couches")
    if any(not math.isfinite(float(x)) for x in list(e.read_S) + list(e.silent)):
        raise ValueError("read_S ou silent non fini")
    mal = [g for g in GARDES_MACHINE + ("identite",) if not isinstance(e.gardes.get(g), bool)]
    if mal:
        raise ValueError(f"gardes non renseignées par un booléen : {mal}")


# ---------------------------------------------------------------- bandes (règles du texte gelé v6, inchangées)

def _lisibles(n_cible, bande):
    return [l for l in bande if n_cible[l] >= N_LISIBLE]


def _bande(valeurs, n_cible, bande, ok, contraire=None):
    """(toutes les couches lisibles ok, plus de la moitié des lisibles « contraire », bande partielle)."""
    lis = _lisibles(n_cible, bande)
    partielle = (len(bande) - len(lis)) > len(bande) / 4
    tout_ok = bool(lis) and all(ok(valeurs[l]) for l in lis)
    maj = bool(lis) and contraire is not None and sum(bool(contraire(valeurs[l])) for l in lis) > len(lis) / 2
    return tout_ok, maj, partielle


def _mesure(clauses_ok, clauses_non):
    if any(maj and not part for maj, part in clauses_non):
        return "non reproduit"
    if all(ok and not part for ok, part in clauses_ok):
        return "reproduit"
    return "autre"


# ---------------------------------------------------------------- mesures

def stabilite_non_finie(e: Entrees) -> bool:
    return any(not math.isfinite(x) for v in e.stabilite.values() for x in v)


def verdict_b1(e: Entrees) -> Mesure:
    diffs = [x for v in e.stabilite.values() for x in v]
    acc = [e.accord[l] for l in COUCHES_ACCORD]
    if any(x > 0.20 for x in diffs) or any(a < 0.60 for a in acc):
        v = "non reproduit"
    elif all(x <= 0.10 for x in diffs) and all(a >= 0.80 for a in acc):
        v = "reproduit"
    else:
        v = "autre"
    return Mesure(v, {"difference_max": max(diffs), "accord_min": min(acc)})


def verdict_b2(t, n, lentille=NOTRE_R) -> Mesure:
    s, ns = t["steer 1x"][lentille], n["steer 1x"]
    r1 = _bande(s["r_med"], ns, couches(8, 15), lambda v: v >= 0.40)
    r2 = _bande(s["r_med"], ns, couches(16, 23), lambda v: v >= 0.60, lambda v: v < 0.30)
    r3 = _bande(s["r_med"], ns, couches(24, 27), lambda v: v >= 0.85)
    p = _bande(s["pass"], ns, couches(8, 27), lambda v: v >= 0.90)
    p_non = _bande(s["pass"], ns, couches(16, 27), lambda v: True, lambda v: v < 0.50)
    bt = couches(0, 27)
    lis = _lisibles(ns, bt)
    hors05 = sum(abs(s["control_med"][l]) > 0.05 for l in lis)
    hors10 = sum(abs(s["control_med"][l]) > 0.10 for l in lis)
    part_t = (len(bt) - len(lis)) > len(bt) / 4
    ok = [(r1[0], r1[2]), (r2[0], r2[2]), (r3[0], r3[2]), (p[0], p[2]), (hors05 <= 1 and hors10 == 0, part_t)]
    non = [(p_non[1], p_non[2]), (r2[1], r2[2])]
    return Mesure(_mesure(ok, non), {"temoin_hors_005": hors05, "temoin_hors_010": hors10})


def verdict_b3(t, n, lentille=NOTRE_R) -> Mesure:
    r = r4(np.asarray(t["steer 1x"][lentille]["r_med"], float) - np.asarray(t["steer 1x"]["logit"]["r_med"], float))
    b = _bande(r, n["steer 1x"], couches(4, 15), lambda v: v >= 0.20, lambda v: v <= 0)
    return Mesure(_mesure([(b[0], b[2])], [(b[1], b[2])]), {"ecart_min_4_15": float(np.min(r[4:16]))})


def ecarts_b4(t) -> dict:
    s = t["steer 1x"]
    r = np.asarray(s[NOTRE_R]["r_med"], float)
    return {k: [float(x) for x in r4(r - np.asarray(s[k]["r_med"], float))[4:24]] for k in ("J", "npJpp")}


def verdict_b5(e: Entrees) -> Mesure:
    rs, si = [Fraction(float(x)) for x in e.read_S], [Fraction(float(x)) for x in e.silent]
    moy_sil = sum(si[1:8]) / 7
    m17, m1223 = sum(rs[1:8]) / 7, sum(rs[12:24]) / 12
    det = {"read_S_0": float(rs[0]), "moyenne_1_7": float(m17), "moyenne_12_23": float(m1223), "ecart": float(m17 - m1223),
           "silent_0": float(si[0]), "silent_moyen_1_7": float(moy_sil)}
    if si[0] > Fraction("0.40") or moy_sil > Fraction("0.50"):
        return Mesure("non lisible", det)
    if rs[0] < Fraction("0.30") or m17 <= m1223:
        return Mesure("non reproduit", det)
    if rs[0] >= Fraction("0.60") and m17 - m1223 >= Fraction("0.10"):
        return Mesure("reproduit", det)
    return Mesure("autre", det)


def verdict_b6(t) -> Mesure:
    ec = np.abs(r4(np.asarray(t["steer 1x"][NOTRE_R]["r_med"], float) - np.asarray(t["steer 1x"]["npR"]["r_med"], float)))[:28]
    if np.any(ec > 0.15):
        v = "désaccord"
    elif np.sum(ec <= 0.05) >= 21:
        v = "accord"
    else:
        v = "intermédiaire"
    return Mesure(v, {"ecarts": [float(x) for x in ec], "couches_au_dela_015": [int(l) for l in np.nonzero(ec > 0.15)[0]]})


def verdict_b7(t, n, lentille=NOTRE_R) -> Mesure:
    a, na = t["ablate win"][lentille]["r_med"], n["ablate win"]
    bas = _bande(a, na, couches(0, 15), lambda v: v < 0.25)
    bas_non = _bande(a, na, couches(8, 15), lambda v: True, lambda v: v >= 0.40)
    haut = _bande(a, na, couches(26, 29), lambda v: v >= 0.50, lambda v: v < 0.30)
    v = _mesure([(bas[0], bas[2]), (haut[0], haut[2])], [(bas_non[1], bas_non[2]), (haut[1], haut[2])])
    return Mesure(v, {"par_le_haut": bool(bas_non[1] and not bas_non[2]), "par_le_bas": bool(haut[1] and not haut[2])})


# ---------------------------------------------------------------- chaîne en défaut

def defauts_score(t, n, lentilles=LENTILLES, avec_e=True) -> list[str]:
    """Gardes (a), (b), (c) et, si `avec_e`, la part « score » de (e). Sur la sortie de la graine 1 (audits A1 et A5), le texte
    n'applique que (a) à (c) : `avec_e=False` (contre-lecture, M1)."""
    d = []
    for c in CIBLES:
        for le in lentilles:
            if any(abs(t[c][le]["control_med"][l]) > 0.10 for l in couches(0, 27)):
                d.append(f"(a) témoin hors de ±0,10 : {c}, {le}")
    if any(n["steer 1x"][l] < N_POLES / 2 for l in couches(0, 27)):
        d.append("(b) pilotage sans effet")
    seuils_c = {"logit": 0.80, "npR": 0.85, NOTRE_R: 0.85}
    for le, sc in seuils_c.items():
        if le in lentilles and any(t["steer 1x"][le]["r_med"][l] < sc for l in couches(28, 30)):
            d.append(f"(c) cas sain manqué : {le}")
    lg = np.asarray(t["steer 1x"]["logit"]["r_med"], float)
    for le in ("J", "npJpp", "npR", NOTRE_R) if avec_e else ():
        if le in lentilles and np.any(np.abs(r4(np.asarray(t["steer 1x"][le]["r_med"], float)[:24] - lg[:24])) < 1e-3):
            d.append(f"(e) repli sur les logits : {le}")
    return d


def defaut_j(t, repere) -> list[str]:
    ec = np.abs(r4(np.asarray(t["steer 1x"]["npR"]["r_med"], float) - np.asarray(repere, float)))[:28]
    if np.sum(ec > 0.05) > 2 or np.any(ec > 0.10):
        return [f"(j) lentille R publique écartée de la série repère (max {float(ec.max()):.4f}, {int(np.sum(ec > 0.05))} couches au-delà de 0,05)"]
    return []


def defauts_chaine(e: Entrees) -> list[str]:
    d = defauts_score(e.score, e.n)
    if stabilite_non_finie(e):
        d.append("(g) différence entre moitiés non finie")
    if e.gardes["identite"]:
        d.append("(e) matrice égale à l'identité")
    d += defaut_j(e.score, e.repere_npR)
    d += [f"({g}) constatée sur la machine" for g in GARDES_MACHINE if e.gardes[g]]
    return d


# ---------------------------------------------------------------- déclencheurs d'audit

def declencheurs(e: Entrees) -> list[str]:
    """Audits à jouer sur la machine (hors A6, calculé ici). Rend une liste parmi « A1 », « A2 », « A3 », « A4 », « A5 »."""
    valider(e)
    t, out = e.score, []
    s = t["steer 1x"][NOTRE_R]
    if any(s["r_med"][l] >= 0.95 for l in couches(0, 7)) or sum(abs(s["control_med"][l]) == 0 for l in couches(0, 27)) >= 2:
        out.append("A1")
    if not stabilite_non_finie(e):  # sinon garde (g) : aucun audit de B-1
        diffs = [x for v in e.stabilite.values() for x in v]
        if any(x < 1e-6 for x in diffs) or all(e.accord[l] == 1 for l in COUCHES_ACCORD):
            out.append("A2")
        if verdict_b1(e).verdict == "non reproduit":
            out.append("A3")
    if e.read_S[0] >= 0.99 or all(x == 0 for x in e.read_S):
        out.append("A4")
    if verdict_b7(t, e.n).details["par_le_haut"]:
        out.append("A5")
    return out


def audit_a6(t) -> str | None:
    b6 = verdict_b6(t)
    if b6.verdict != "désaccord":
        return None
    r = np.asarray(t["steer 1x"][NOTRE_R]["r_med"], float)
    moities = [np.asarray(t["steer 1x"][m]["r_med"], float) for m in MOITIES]
    stable = all(all(abs(round(float(mo[l] - r[l]), 4)) < 0.05 for mo in moities) for l in b6.details["couches_au_dela_015"])
    return "écart de corpus" if stable else "écart d'ajustement"


# ---------------------------------------------------------------- verdict

@dataclass
class Verdict:
    verdict: str
    defauts: list
    reserves: list
    audits: dict
    mesures: dict


def verdict(e: Entrees, audits: dict | None = None) -> Verdict:
    """`audits` : pour chaque audit déclenché, son résultat ou `NON_JOUE` :
    A1 et A5 : `{"temoin_distinct": bool, "normes_non_nulles": bool, "score": table de la graine 1 (lentilles logit, npR, notre R),
    "n": n de la graine 1}` ; A2 et A3 : `{"controles_ok": bool}` ; A4 : `{"permutation_ok": bool, "lentille_S_ok": bool}`."""
    valider(e)
    audits = dict(audits or {})
    attendus = declencheurs(e)
    absents = [a for a in attendus if a not in audits]
    if absents:
        raise ValueError(f"audits déclenchés sans résultat : {absents}")
    t, n = e.score, e.n
    if stabilite_non_finie(e):
        return Verdict(CHAINE, defauts_chaine(e), [], {}, {})
    m = {"B-1": verdict_b1(e), "B-2": verdict_b2(t, n), "B-3": verdict_b3(t, n), "B-5": verdict_b5(e), "B-6": verdict_b6(t),
         "B-7": verdict_b7(t, n)}
    b4 = ecarts_b4(t)
    d = defauts_chaine(e)
    reserves, non_conclu = [], []
    # A1 et A5 : graine 1 (une seule relance)
    for a in ("A1", "A5"):
        if a not in attendus:
            continue
        r = audits[a]
        if r == NON_JOUE:
            if a == "A1":
                non_conclu.append("A1")
            else:
                m["B-7"] = Mesure("autre", m["B-7"].details | {"audit_A5": NON_JOUE})
            continue
        if not (r["temoin_distinct"] is True and r["normes_non_nulles"] is True):
            d.append(f"(l) témoin ou pilotage dégénéré ({a})")
            continue
        g1 = r["score"]
        valider_table(g1, r["n"], lentilles=("logit", "npR", NOTRE_R))
        defs_g1 = defauts_score(g1, r["n"], lentilles=("logit", "npR", NOTRE_R), avec_e=False)
        if defs_g1:
            d.append(f"(l) garde (a) à (c) manquée sous la graine 1 ({a}) : " + " ; ".join(defs_g1))
            continue
        if a == "A1":
            for k, f in (("B-2", verdict_b2), ("B-3", verdict_b3), ("B-7", verdict_b7)):
                if f(g1, r["n"]).verdict != m[k].verdict:
                    m[k] = Mesure("autre", m[k].details | {"audit_A1": "verdict différent sous la graine 1"})
        else:
            if not verdict_b7(g1, r["n"]).details["par_le_haut"]:
                m["B-7"] = Mesure("autre", m["B-7"].details | {"audit_A5": "non confirmé sous la graine 1"})
    for a in ("A2", "A3"):
        if a in attendus:
            if audits[a] == NON_JOUE:
                non_conclu.append(a)
            elif not audits[a]["controles_ok"]:
                d.append(f"(g) moitiés ou documents non conformes ({a})")
    if "A4" in attendus:
        r = audits["A4"]
        if r == NON_JOUE:
            non_conclu.append("A4")
        else:
            if not r["permutation_ok"]:
                d.append("(m) appariement dégénéré de B-5 (A4)")
            if not r["lentille_S_ok"]:
                d.append("(k) lentille S lue différente de l'ajustement (A4)")
    a6 = audit_a6(t)
    if a6:
        reserves.append(a6)
    mesures = {k: {"verdict": v.verdict, **v.details} for k, v in m.items()} | {"B-4": b4}
    if d:  # « aucun verdict de mesure » (rang 1 ; contre-lecture, M2)
        return Verdict(CHAINE, d, reserves, {a: audits[a] if audits[a] == NON_JOUE else "joué" for a in attendus}, {})
    if non_conclu:
        return Verdict(NON_CONCLU, [], reserves + [f"audit non joué : {', '.join(non_conclu)}"],
                       {a: audits[a] if audits[a] == NON_JOUE else "joué" for a in attendus}, mesures)
    if "non reproduit" in (m["B-2"].verdict, m["B-3"].verdict):
        v = NON_REPRODUIT
        reserves.append("défaut dans notre lentille")
    elif all(m[k].verdict == "reproduit" for k in ("B-1", "B-2", "B-3", "B-5")):
        v = REPRODUIT
    else:
        v = PARTIEL
    return Verdict(v, [], reserves, {a: audits[a] if audits[a] == NON_JOUE else "joué" for a in attendus}, mesures)


# ---------------------------------------------------------------- référence de Qwen3-8B (essai de P.4, cas (i))

def depuis_reference_qwen(table_qwen: dict) -> dict:
    """Référence publiée convertie : couche Llama l ← couche Qwen ⌊l × 36/32⌋ ; « R:dclm » joue notre R, ses deux moitiés et `npR` ;
    « J » joue `J` et `npJpp` ; « logit » joue `logit`."""
    role = {"logit": "logit", "J": "J", "npJpp": "J", "npR": "R:dclm", NOTRE_R: "R:dclm", MOITIES[0]: "R:dclm", MOITIES[1]: "R:dclm"}
    out = {}
    for c in CIBLES:
        out[c] = {}
        for le, src in role.items():
            q = table_qwen[c][src]
            if list(q["layer"]) != list(range(QWEN_COUCHES)):
                raise ValueError(f"référence : couches manquantes ({c}, {src})")
            out[c][le] = {"layer": list(range(N_COUCHES))}
            out[c][le] |= {k: [q[k][(l * QWEN_COUCHES) // N_COUCHES] for l in range(N_COUCHES)] for k in ("r_med", "pass", "control_med")}
    return out


def reads_depuis_reference_qwen(reads_qwen: dict) -> tuple[list, list]:
    """`read_S` et `silent` de la référence publiée ramenés à 32 couches par la même règle."""
    L = reads_qwen["neurons"]["layers"]
    if [x["layer"] for x in L] != list(range(QWEN_COUCHES)):
        raise ValueError("référence des lectures aux activations : couches manquantes")
    idx = [(l * QWEN_COUCHES) // N_COUCHES for l in range(N_COUCHES)]
    return [L[i]["read_S"] for i in idx], [L[i]["silent"] for i in idx]
