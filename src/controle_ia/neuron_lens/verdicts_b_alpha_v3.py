"""Verdicts de la tranche B-α de « Neuron Lens » (Llama 3.1 8B Instruct, lentilles publiques de Neuronpedia) — v3.

Remplace la v2 (archivée) après la contre-lecture 2 (`docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-2-code-et-addendum-v2.md`),
la v2 ayant remplacé la v1 après la contre-lecture 1. Met en œuvre, sans rien y changer, les sections
« Seuil » (B), « Critères de lecture gelés » (tranche B-α et B-7) et l'audit R4 de B-α du texte gelé
`docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` (`34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131`),
les contrôles de B0 (`controle_lentille`) et le recalcul de n (`n_par_couche`, `n_depuis_causal`). Aucun modèle, aucun réseau.

Lectures déclarées du texte (le texte ne tranche pas ces points ; elles sont choisies ici et contre-lues) :
- une clause « non reproduit » n'est **pas jugée** sur une bande partielle (plus du quart de couches non lisibles) : la mesure est alors
  « partielle » pour cette bande ;
- les différences de deux valeurs écrites à 4 décimales sont **arrondies à 4 décimales** avant comparaison aux seuils ;
- un verdict de reproduction accompagné d'un déclencheur d'audit de reproduction (« trop beau », « tout négatif ») est rendu « en attente
  d'audit R4 » ; B-7 « non reproduit » par le haut est un déclencheur d'audit de **B-7** seulement (`audit_requis`), qui ne préfixe pas le
  verdict de reproduction (B-7 est hors du verdict de reproduction) ; « en attente » ne suspend pas B-β (seule la chaîne en défaut le fait) ;
- les entrées sont les valeurs telles que `score` les écrit (4 décimales) : toute autre valeur est refusée.

Forme des données (celle du JSON publié de `score`) : `table[cible][lentille]` porte `layer` (liste des couches écrites) et les listes
par couche `r_med`, `pass`, `control_med`. `n[cible]` : liste par couche des pôles retenus (obligatoire).
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

CIBLES = ("steer 1x", "steer 4x", "ablate pos", "ablate win")
LENTILLES = ("logit", "J", "npJpp", "npR")
N_COUCHES = 32
N_TIRES = 32  # neurones tirés au hasard par couche (défaut publié de `measure`)
N_POLES = 2 * N_TIRES
N_LISIBLE = 48
QWEN_COUCHES = 36
N_REFERENCE = {c: [N_POLES] * N_COUCHES for c in CIBLES}  # pour l'essai B.3 seulement (texte : « n pris égal à 64 »)
EN_DEFAUT = "chaîne en défaut ou mode commun réel, audit"


def couches(a: int, b: int) -> list[int]:
    return list(range(a, b + 1))


@dataclass
class Mesure:
    verdict: str
    details: dict = field(default_factory=dict)


@dataclass
class VerdictBAlpha:
    verdict: str
    defauts: list[str]
    audit_requis: list[str]
    b2: Mesure | None
    b3: Mesure | None
    b7: Mesure | None
    b4: dict


def valider(t: dict, n: dict) -> None:
    """Refuse toute table où une couche manque, est désordonnée, ou porte une valeur non finie ou non écrite à 4 décimales, et tout `n`
    qui n'est pas un entier de [0, 64] par couche (R5 : aucun repli silencieux)."""
    for c in CIBLES:
        if c not in n or len(n[c]) != N_COUCHES:
            raise ValueError(f"n[{c}] absent ou sans {N_COUCHES} couches")
        for x in n[c]:
            if not (isinstance(x, (int, np.integer)) and 0 <= x <= N_POLES):
                raise ValueError(f"n[{c}] : valeur hors de [0, {N_POLES}] ou non entière : {x!r}")
        for le in LENTILLES:
            s = t[c][le]
            if list(s["layer"]) != list(range(N_COUCHES)):
                raise ValueError(f"couches manquantes ou désordonnées : {c}, {le}")
            for k in ("r_med", "pass", "control_med"):
                v = np.asarray(s[k], dtype=float)
                if v.shape != (N_COUCHES,) or not np.all(np.isfinite(v)):
                    raise ValueError(f"valeur absente ou non finie : {c}, {le}, {k}")
                if not np.all(np.round(v, 4) == v):
                    raise ValueError(f"valeur non écrite à 4 décimales : {c}, {le}, {k}")


def _lisibles(n_cible, bande):
    return [l for l in bande if n_cible[l] >= N_LISIBLE]


def _bande(valeurs, n_cible, bande, ok, contraire=None):
    """(toutes les lisibles ok, plus de la moitié des lisibles « contraire », bande partielle)."""
    lis = _lisibles(n_cible, bande)
    partielle = (len(bande) - len(lis)) > len(bande) / 4
    tout_ok = bool(lis) and all(ok(valeurs[l]) for l in lis)
    maj = bool(lis) and contraire is not None and sum(contraire(valeurs[l]) for l in lis) > len(lis) / 2
    return tout_ok, maj, partielle


def _mesure(clauses_ok, clauses_non):
    """clauses_ok : (tout_ok, partielle) ; clauses_non : (majorité contraire, partielle). Une clause « non reproduit » n'est pas
    jugée sur une bande partielle (lecture déclarée)."""
    if any(maj and not part for maj, part in clauses_non):
        return "non reproduit"
    if all(ok and not part for ok, part in clauses_ok):
        return "reproduit"
    return "partiel"


def verdict_b2(t, n):
    s, ns = t["steer 1x"]["npR"], n["steer 1x"]
    r1 = _bande(s["r_med"], ns, couches(8, 15), lambda v: v >= 0.40)
    r2 = _bande(s["r_med"], ns, couches(16, 23), lambda v: v >= 0.60, lambda v: v < 0.30)
    r3 = _bande(s["r_med"], ns, couches(24, 27), lambda v: v >= 0.85)
    p = _bande(s["pass"], ns, couches(8, 27), lambda v: v >= 0.90)
    p_non = _bande(s["pass"], ns, couches(16, 27), lambda v: True, lambda v: v < 0.50)
    bande_t = couches(0, 27)
    lis = _lisibles(ns, bande_t)
    hors05 = sum(abs(s["control_med"][l]) > 0.05 for l in lis)
    hors10 = sum(abs(s["control_med"][l]) > 0.10 for l in lis)
    part_t = (len(bande_t) - len(lis)) > len(bande_t) / 4
    ok = [(r1[0], r1[2]), (r2[0], r2[2]), (r3[0], r3[2]), (p[0], p[2]), (hors05 <= 1 and hors10 == 0, part_t)]
    non = [(p_non[1], p_non[2]), (r2[1], r2[2])]
    return Mesure(_mesure(ok, non), {"temoin_hors_005": hors05, "temoin_hors_010": hors10})


def verdict_b3(t, n):
    r = np.round(np.asarray(t["steer 1x"]["npR"]["r_med"], float) - np.asarray(t["steer 1x"]["logit"]["r_med"], float), 4)
    b = _bande(r, n["steer 1x"], couches(4, 15), lambda v: v >= 0.20, lambda v: v <= 0)
    return Mesure(_mesure([(b[0], b[2])], [(b[1], b[2])]), {"ecart_min_4_15": float(np.min(r[4:16]))})


def verdict_b7(t, n):
    a, na = t["ablate win"]["npR"]["r_med"], n["ablate win"]
    bas = _bande(a, na, couches(0, 15), lambda v: v < 0.25)
    bas_non = _bande(a, na, couches(8, 15), lambda v: True, lambda v: v >= 0.40)
    haut = _bande(a, na, couches(26, 29), lambda v: v >= 0.50, lambda v: v < 0.30)
    v = _mesure([(bas[0], bas[2]), (haut[0], haut[2])], [(bas_non[1], bas_non[2]), (haut[1], haut[2])])
    return Mesure(v, {"par_le_haut": bool(bas_non[1] and not bas_non[2]), "par_le_bas": bool(haut[1] and not haut[2])})


def ecarts_b4(t):
    s = t["steer 1x"]
    r = np.asarray(s["npR"]["r_med"], float)
    return {k: [float(x) for x in np.round(r - np.asarray(s[k]["r_med"], float), 4)[4:24]] for k in ("J", "npJpp")}


def defauts_chaine(t, n, essais_ok: bool, matrices_identite: bool):
    d = []
    for c in CIBLES:
        for le in LENTILLES:
            if any(abs(t[c][le]["control_med"][l]) > 0.10 for l in couches(0, 27)):
                d.append(f"(a) témoin hors de ±0,10 : {c}, {le}")
    if any(n["steer 1x"][l] < N_POLES / 2 for l in couches(0, 27)):
        d.append("(b) pilotage sans effet")
    if any(t["steer 1x"]["logit"]["r_med"][l] < 0.80 for l in couches(28, 30)):
        d.append("(c) cas sain des logits manqué")
    if any(t["steer 1x"]["npR"]["r_med"][l] < 0.85 for l in couches(28, 30)):
        d.append("(c) cas sain de npR manqué")
    if not essais_ok:
        d.append("(d) essai ou fumée en échec")
    lg = np.asarray(t["steer 1x"]["logit"]["r_med"], float)
    for le in ("J", "npJpp", "npR"):
        ec = np.abs(np.round(np.asarray(t["steer 1x"][le]["r_med"], float)[:24] - lg[:24], 4))
        if np.any(ec < 1e-3):
            d.append(f"(e) repli sur les logits : {le}")
    if matrices_identite:
        d.append("(e) matrice égale à l'identité")
    return d


def trop_beau(t):
    s = t["steer 1x"]["npR"]
    out = []
    if any(s["r_med"][l] >= 0.95 for l in couches(0, 7)):
        out.append("trop beau : r_med ≥ 0,95 à une couche 0–7")
    if sum(abs(s["control_med"][l]) == 0 for l in couches(0, 27)) >= 2:
        out.append("trop beau : control_med écrit 0 à au moins 2 couches 0–27")
    return out


def verdict(t: dict, n: dict, *, essais_ok: bool, matrices_identite: bool) -> VerdictBAlpha:
    valider(t, n)
    d = defauts_chaine(t, n, essais_ok, matrices_identite)
    b4 = ecarts_b4(t)
    if d:
        return VerdictBAlpha(EN_DEFAUT, d, [], None, None, None, b4)
    b2, b3, b7 = verdict_b2(t, n), verdict_b3(t, n), verdict_b7(t, n)
    if b2.verdict == "reproduit" and b3.verdict == "reproduit":
        v = "reproduit avec la lentille R publique"
    elif "non reproduit" in (b2.verdict, b3.verdict):
        v = "non reproduit avec la lentille R publique"
    else:
        v = "partiel"
    audit = trop_beau(t)
    if b2.verdict == "non reproduit" and b3.verdict == "non reproduit":
        audit.append("tout négatif : B-2 et B-3 « non reproduit »")
    if audit:
        v = "en attente d'audit R4 : " + v
    if b7.details["par_le_haut"]:
        audit.append("B-7 « non reproduit » par le haut : audit avant toute lecture de B-7")
    return VerdictBAlpha(v, d, audit, b2, b3, b7, b4)


def depuis_reference_qwen(table_qwen: dict) -> dict:
    """Référence publiée de Qwen3-8B convertie (texte gelé, B.3) : couche Llama l ← couche Qwen ⌊l × 36/32⌋ ; « R:dclm » joue `npR`,
    « J » joue `J` et `npJpp`, « logit » joue `logit`."""
    role = {"logit": "logit", "J": "J", "npJpp": "J", "npR": "R:dclm"}
    out = {}
    for c in CIBLES:
        out[c] = {}
        for le, src in role.items():
            q = table_qwen[c][src]
            if list(q["layer"]) != list(range(QWEN_COUCHES)):
                raise ValueError(f"référence : couches manquantes ({c}, {src})")
            out[c][le] = {"layer": list(range(N_COUCHES))}
            out[c][le] |= {k: [q[k][(l * QWEN_COUCHES) // N_COUCHES] for l in range(N_COUCHES)]
                           for k in ("r_med", "pass", "control_med")}
    return out


def controle_lentille(J: dict, n_attendu: int = 31, tol: float = 1e-6, couches_identite=range(0, 28)):
    """Contrôle de B0 sur un fichier de lentille déjà lu (`{couche: matrice}`). Rend (arrêts, défauts) :
    arrêts (→ arrêt de B-α, écart écrit) : couches non contiguës, nombre de couches lues ≠ 31, matrice non carrée ou non 2D ;
    défauts (→ chaîne en défaut (e)) : matrice égale à l'identité (écart maximal en valeur absolue ≤ tol, en float32) aux couches 0–27."""
    arrets, defauts = [], []
    cles = sorted(J)
    if cles != list(range(len(cles))):
        arrets.append("couches non contiguës 0..n−1")
    if len(cles) != n_attendu:
        arrets.append(f"nombre de couches lues {len(cles)} ≠ {n_attendu}")
    for l in cles:
        m = np.asarray(J[l], dtype=np.float32)
        if m.ndim != 2 or m.shape[0] != m.shape[1]:
            arrets.append(f"matrice non carrée ou non 2D à la couche {l}")
            continue
        if not np.all(np.isfinite(m)):
            arrets.append(f"matrice non finie à la couche {l}")
            continue
        if l in couches_identite and np.max(np.abs(m - np.eye(m.shape[0], dtype=np.float32))) <= tol:
            defauts.append(f"matrice égale à l'identité à la couche {l}")
    return arrets, defauts


def random_neurons(n_layers: int, f: int, per_layer: int, seed: int = 0) -> list[tuple[int, int]]:
    """Recopie de `random_neurons` de `causal_lens.py` (copie empreintée, lignes 66-68) : le tirage que `measure` et `score` font."""
    import random
    rng = random.Random(seed)
    return [(l, n) for l in range(n_layers) for n in sorted(rng.sample(range(f), per_layer))]


def n_par_couche(picks, aleatoires, cibles: dict, fired, nv: int):
    """Recalcul de n par la règle de `score` (copie de `causal_lens.py`, lignes ~300-315) : par couche et cible, pôles retenus parmi
    les neurones tirés au hasard (`is_rand`) : cible de norme non nulle sur les `nv` lignes du tokeniseur ; pour l'ablation, pôle qui
    a des contextes (`fired`). Rend (n, écartés par motif). Motifs exclusifs, priorité à « sans contexte » (la cause première :
    `measure` laisse la cible à zéro sans contexte ; `score` ne distingue pas les motifs). Exige : `picks` sans doublon ; `aleatoires`
    inclus dans `picks` ; 32 neurones tirés au hasard à chacune des 32 couches ; couches dans [0, 32) ; `nv` ≤ taille du vocabulaire ;
    n + écartés == 64 par couche et cible."""
    picks = [tuple(p) for p in picks]
    if len(set(picks)) != len(picks):
        raise ValueError("doublon dans picks")
    if not set(aleatoires) <= set(picks):
        raise ValueError("neurone tiré au hasard absent de picks")
    par_couche = {}
    for l, neur in aleatoires:
        if not 0 <= l < N_COUCHES:
            raise ValueError(f"couche hors de [0, {N_COUCHES}) : {l}")
        par_couche[l] = par_couche.get(l, 0) + 1
    if sorted(par_couche) != list(range(N_COUCHES)) or any(v != N_TIRES for v in par_couche.values()):
        raise ValueError("32 neurones tirés au hasard à chacune des 32 couches exigés")
    fired = np.asarray(fired, dtype=bool)
    n = {c: [0] * N_COUCHES for c in cibles}
    ecartes = {c: {"effet nul": [0] * N_COUCHES, "sans contexte": [0] * N_COUCHES} for c in cibles}
    for c, t in cibles.items():
        t = np.asarray(t, dtype=np.float32)
        if t.ndim != 3 or t.shape[:2] != (len(picks), 2) or nv > t.shape[2]:
            raise ValueError(f"forme de la cible {c} : {t.shape} (nv = {nv})")
        effet = np.abs(t[:, :, :nv]).sum(-1) > 0
        ablation = not c.startswith("steer")
        for i, (l, neur) in enumerate(picks):
            if (l, neur) not in aleatoires:
                continue
            for pole in (0, 1):
                if ablation and not fired[i, pole]:
                    ecartes[c]["sans contexte"][l] += 1
                elif not effet[i, pole]:
                    ecartes[c]["effet nul"][l] += 1
                else:
                    n[c][l] += 1
        for l in range(N_COUCHES):
            if n[c][l] + ecartes[c]["effet nul"][l] + ecartes[c]["sans contexte"][l] != N_POLES:
                raise ValueError(f"n + écartés ≠ {N_POLES} : {c}, couche {l}")
    return n, ecartes


def n_depuis_causal(saved: dict, nv: int, f: int):
    """Dérive les entrées de `n_par_couche` du fichier `-causal.pt` comme le fait `score` : steer 1x = `steer[:, :, 0]` (dose 1×), steer
    4x = `steer[:, :, 1]`, `ablate_pos`, `ablate_win`, `fired = (saved["fired"] > 0).any(-1)` ; `nv` = `len(tokenizer)` ; neurones tirés
    au hasard = `random_neurons(32, f, meta["per_layer"])` (f = 14 336 neurones par couche pour Llama). Formes affirmées."""
    meta = saved["meta"]
    if list(meta["doses"]) != [1.0, 4.0] or meta["per_layer"] != N_TIRES:
        raise ValueError(f"meta inattendu : doses {meta['doses']}, per_layer {meta['per_layer']}")
    steer = np.asarray(saved["steer"])
    if steer.ndim != 4 or steer.shape[1:3] != (2, 2) or np.asarray(saved["fired"]).ndim != 3:
        raise ValueError(f"formes inattendues : steer {steer.shape}, fired {np.asarray(saved['fired']).shape}")
    aleatoires = random_neurons(N_COUCHES, f, meta["per_layer"])
    cibles = {"steer 1x": steer[:, :, 0], "steer 4x": steer[:, :, 1],
              "ablate pos": np.asarray(saved["ablate_pos"]), "ablate win": np.asarray(saved["ablate_win"])}
    fired = (np.asarray(saved["fired"]) > 0).any(-1)
    return n_par_couche([tuple(p) for p in saved["picks"]], set(map(tuple, aleatoires)), cibles, fired, nv)
