"""Sonde de réussite attendue par différence temporelle ; aire sous la courbe ; grille d'élagage (exploratoire).

Papier (arXiv 2602.00986v2) : perceptron à deux couches, activation ReLU, sortie scalaire (p. 3) ; erreur de différence
temporelle (équation 8, p. 4) δ_t = γ V(s_t) − V(s_{t−1}) pour t = 1…T, δ_{T+1} = r − V(s_T) ; objectif (équation 9) :
E[Σ_{t=1}^{T+1} δ_t²]. Tableau 7 (p. 19) : AdamW, pas 1e-4, décroissance des poids 0,01, 100 époques, lots de 4,
part d'entraînement 0,8, γ = 1 − 1e-5, 1024 unités cachées. Lecture au dernier jeton de l'énoncé : aire sous la courbe de
V(s_0) contre r (p. 4). Élagage (p. 4) : norme L1 des poids qui relient chaque dimension d'entrée à la couche cachée ; on
garde les (1 − p)N dimensions de plus forte norme ; grille des quinze taux du tableau 8 (p. 20).

Points que le papier ne fixe pas, choisis ici et écrits au manifeste (à trancher par le plan des étapes 0-1) :
- gradient : « complet » (défaut, minimisation littérale de l'équation 9) ou « semi » (cible γV(s_t) et r détachées) ;
- perte d'un lot : moyenne sur les séquences de la somme des δ² de chaque séquence ;
- élagage : sonde complète masquée, ⌊p·N⌋ entrées de plus petite norme mises à zéro, sans réapprentissage (défaut,
  plan des étapes 0-1, § B.2 et B.3 point 6), ou sonde réapprise sur les entrées gardées (variante) ;
- meilleur taux : le meilleur des quinze PAR COUCHE, puis moyenne sur les couches (plan, § B.4) ; un taux commun aux
  couches est rapporté à côté ;
- découpage : « plis » (cinq plis de 100 questions, chaque sonde apprise sur 400 ; plan, § B.3 point 7) ou « part ».
"""
from __future__ import annotations

import numpy as np
from scipy.stats import rankdata

from ..gardes import GardeArret

RECETTE_TABLEAU_7 = {"optimiseur": "AdamW", "pas": 1e-4, "decroissance": 0.01, "epoques": 100, "lot": 4,
                     "part_entrainement": 0.8, "gamma": 1 - 1e-5, "cachee": 1024}
TAUX_ELAGAGE_TABLEAU_8 = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.92, 0.94, 0.96, 0.98, 0.99)
GRADIENTS = ("complet", "semi")


def exiger_recette(recette: dict, *, jouet: bool = False) -> dict:
    """La recette est celle du tableau 7 ; le jouet seul peut réduire `epoques` et `cachee` (essais rapides)."""
    for cle, v in RECETTE_TABLEAU_7.items():
        if cle in ("epoques", "cachee") and jouet:
            x = recette.get(cle)
            if isinstance(x, bool) or not isinstance(x, int) or x < 1:
                raise GardeArret(f"recette de la sonde : {cle} = {x!r} illisible")
            continue
        if recette.get(cle) != v:
            raise GardeArret(f"recette de la sonde : {cle} = {recette.get(cle)!r}, {v!r} attendu (tableau 7, p. 19)")
    if recette.get("gradient", "complet") not in GRADIENTS:
        raise GardeArret(f"gradient {recette.get('gradient')!r} inconnu ({GRADIENTS})")
    return recette


# --- aire sous la courbe ---------------------------------------------------------------------------------------------

def aire_sous_courbe(scores, etiquettes) -> float:
    """Aire sous la courbe ROC par les rangs (ex aequo moyennés) ; refus si une seule issue est présente."""
    s = np.asarray(scores, dtype=float)
    y = np.asarray(etiquettes)
    if s.shape != y.shape or s.ndim != 1:
        raise GardeArret("scores et étiquettes : vecteurs de même longueur attendus")
    if not np.isin(y, (0, 1)).all():
        raise GardeArret("étiquettes non binaires")
    if not np.isfinite(s).all():
        raise GardeArret("score non fini")
    n1, n0 = int(y.sum()), int((1 - y).sum())
    if n1 == 0 or n0 == 0:
        raise GardeArret(f"aire sous la courbe indéfinie : {n1} réussites, {n0} échecs")
    r = rankdata(s)
    return float((r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


# --- découpages ------------------------------------------------------------------------------------------------------

def decoupages(n: int, mode: str, graine: int, part: float = 0.8, plis: int = 5) -> list[tuple[np.ndarray, np.ndarray]]:
    rng = np.random.default_rng(int(graine))
    perm = rng.permutation(n)
    if mode == "part":
        k = int(round(part * n))
        if not 0 < k < n:
            raise GardeArret(f"part {part} sur {n} questions : découpage vide")
        return [(np.sort(perm[:k]), np.sort(perm[k:]))]
    if mode == "plis":
        if not 2 <= plis <= n:
            raise GardeArret(f"{plis} plis pour {n} questions")
        morceaux = np.array_split(perm, plis)
        return [(np.sort(np.concatenate([m for j, m in enumerate(morceaux) if j != i])), np.sort(morceaux[i]))
                for i in range(plis)]
    raise GardeArret(f"découpage {mode!r} inconnu (part, plis)")


# --- sonde et perte --------------------------------------------------------------------------------------------------

def _torch():
    import torch
    return torch


def sonde(d: int, cachee: int):
    nn = _torch().nn
    return nn.Sequential(nn.Linear(d, cachee), nn.ReLU(), nn.Linear(cachee, 1))


def perte_td(valeurs, longueurs, recompenses, gamma: float, gradient: str = "complet"):
    """valeurs : (B, Lmax) valeurs V(s_0…s_T) complétées à droite ; longueurs : T + 1 par séquence ; recompenses : (B,).
    Rend la moyenne sur le lot de Σ_{t=1}^{T+1} δ_t² (équations 8 et 9)."""
    torch = _torch()
    if gradient not in GRADIENTS:
        raise GardeArret(f"gradient {gradient!r} inconnu")
    B, L = valeurs.shape
    lg = torch.as_tensor(longueurs, device=valeurs.device)
    if (lg < 1).any() or (lg > L).any():
        raise GardeArret("longueurs hors de [1, Lmax]")
    cible = valeurs.detach() if gradient == "semi" else valeurs
    t = torch.arange(L, device=valeurs.device)
    masque_inter = (t[1:].unsqueeze(0) < lg.unsqueeze(1)).to(valeurs.dtype)          # δ_t, t = 1…T
    d_inter = (gamma * cible[:, 1:] - valeurs[:, :-1]) * masque_inter
    v_fin = valeurs.gather(1, (lg - 1).unsqueeze(1)).squeeze(1)                       # V(s_T)
    d_fin = recompenses.to(valeurs.dtype) - v_fin                                      # δ_{T+1}
    return ((d_inter ** 2).sum(1) + d_fin ** 2).mean()


def _vers_appareil(sequences, dims, appareil):
    torch = _torch()
    sortie = []
    for s in sequences:
        a = np.asarray(s)
        if dims is not None:
            a = a[:, dims]
        sortie.append(torch.as_tensor(np.ascontiguousarray(a), dtype=torch.float16, device=appareil))
    return sortie


def entrainer(sequences: list, recompenses: np.ndarray, recette: dict, graine: int, dims=None, appareil: str = "cpu",
              *, jouet: bool = False):
    """Apprend une sonde sur des trajectoires (T + 1, d) ; `dims` : dimensions gardées (élagage). Rend la sonde."""
    torch = _torch()
    recette = exiger_recette(recette, jouet=jouet)
    r = np.asarray(recompenses)
    if len(sequences) != len(r) or len(r) == 0:
        raise GardeArret("autant de récompenses que de trajectoires, au moins une, attendu")
    if not np.isin(r, (0, 1)).all():
        raise GardeArret("récompenses non binaires")
    torch.manual_seed(int(graine))
    gen = torch.Generator().manual_seed(int(graine))
    x = _vers_appareil(sequences, dims, appareil)
    d = x[0].shape[1]
    m = sonde(d, recette["cachee"]).to(appareil)
    opt = torch.optim.AdamW(m.parameters(), lr=recette["pas"], weight_decay=recette["decroissance"])
    rt = torch.as_tensor(r, dtype=torch.float32, device=appareil)
    n, b = len(x), recette["lot"]
    for _ in range(recette["epoques"]):
        perm = torch.randperm(n, generator=gen).tolist()
        for i in range(0, n, b):
            idx = perm[i:i + b]
            lg = [x[j].shape[0] for j in idx]
            pad = torch.zeros(len(idx), max(lg), d, device=appareil, dtype=torch.float32)
            for k, j in enumerate(idx):
                pad[k, :lg[k]] = x[j].float()
            v = m(pad).squeeze(-1)
            perte = perte_td(v, lg, rt[idx], recette["gamma"], recette.get("gradient", "complet"))
            opt.zero_grad()
            perte.backward()
            opt.step()
    return m


def valeurs_s0(m, sequences: list, dims=None, appareil: str = "cpu") -> np.ndarray:
    torch = _torch()
    x0 = np.stack([np.asarray(s)[0] for s in sequences])
    if dims is not None:
        x0 = x0[:, dims]
    with torch.no_grad():
        v = m(torch.as_tensor(x0.astype(np.float32), device=appareil)).squeeze(-1)
    return v.cpu().numpy().astype(float)


def importance_l1(m) -> np.ndarray:
    """Norme L1, par dimension d'entrée, des poids vers la couche cachée (p. 4)."""
    return m[0].weight.detach().abs().sum(0).cpu().numpy()


def dimensions_gardees(importance: np.ndarray, taux: float) -> np.ndarray:
    """On masque ⌊p·N⌋ entrées de plus petite norme (à 0,99 sur 4 096, il en reste 41) ; ensembles emboîtés."""
    import math
    N = len(importance)
    k = max(1, N - int(math.floor(float(taux) * N + 1e-9)))
    ordre = np.argsort(-importance, kind="stable")
    return np.sort(ordre[:k])


def grille_elagage(seq_app: list, r_app, seq_val: list, r_val, recette: dict, graine: int, taux=TAUX_ELAGAGE_TABLEAU_8,
                   reapprendre: bool = False, appareil: str = "cpu", *, jouet: bool = False,
                   graine_de=None, sonde_complete=None) -> dict:
    """Aire sous la courbe de V(s_0) sur la validation, et les scores eux-mêmes (pour l'aire mise en commun sur les plis),
    pour chaque taux. `graine_de(taux) -> int` : graine de la sonde réapprise (défaut : celle de la sonde complète)."""
    complete = sonde_complete if sonde_complete is not None else entrainer(seq_app, r_app, recette, graine,
                                                                            appareil=appareil, jouet=jouet)
    imp = importance_l1(complete)
    sortie = {}
    for p in taux:
        dims = dimensions_gardees(imp, p)
        if p == 0.0:
            v = valeurs_s0(complete, seq_val, appareil=appareil)
        elif reapprendre:
            g = graine if graine_de is None else graine_de(p)
            mp = entrainer(seq_app, r_app, recette, g, dims=dims, appareil=appareil, jouet=jouet)
            v = valeurs_s0(mp, seq_val, dims=dims, appareil=appareil)
        else:
            torch = _torch()
            masque = np.zeros(len(imp), dtype=np.float32)
            masque[dims] = 1.0
            x0 = np.stack([np.asarray(s)[0] for s in seq_val]).astype(np.float32) * masque
            with torch.no_grad():
                v = complete(torch.as_tensor(x0, device=appareil)).squeeze(-1).cpu().numpy().astype(float)
        sortie[float(p)] = {"aire": aire_sous_courbe(v, r_val), "dimensions_gardees": int(len(dims)),
                            "scores": [float(x) for x in v]}
    return sortie


def meilleur_taux(aires_par_couche: dict[int, dict[float, float]]) -> dict:
    """Lecture principale (plan, § B.4) : pour chaque couche, le maximum sur les taux ; puis la moyenne sur les couches.
    À côté : le taux commun aux couches (plus forte moyenne ; ex aequo : le plus petit) et l'aire au taux 0."""
    couches = sorted(aires_par_couche)
    taux = sorted(set.intersection(*(set(aires_par_couche[c]) for c in couches)))
    if not taux:
        raise GardeArret("aucun taux commun aux couches")
    par_couche = {c: max(taux, key=lambda p: (aires_par_couche[c][p], -p)) for c in couches}
    moy = {p: float(np.mean([aires_par_couche[c][p] for c in couches])) for p in taux}
    commun = max(taux, key=lambda p: (moy[p], -p))
    return {"aire_au_meilleur_taux": float(np.mean([aires_par_couche[c][par_couche[c]] for c in couches])),
            "meilleur_taux_par_couche": {str(c): par_couche[c] for c in couches},
            "taux_commun": commun, "aire_au_taux_commun": moy[commun],
            "aire_au_taux_0": moy.get(0.0), "moyenne_par_taux": moy, "couches": couches}


def intervalle_aire(scores, y, rng: np.random.Generator, tirages: int = 2000, niveau: float = 0.95,
                    groupes=None) -> tuple[float, float]:
    """Intervalle par rééchantillonnage des questions (dans chaque groupe — pli — s'ils sont donnés), percentiles."""
    s, y = np.asarray(scores, dtype=float), np.asarray(y)
    g = np.zeros(len(s), dtype=int) if groupes is None else np.asarray(groupes)
    idx_g = [np.flatnonzero(g == k) for k in np.unique(g)]
    vals = []
    for _ in range(int(tirages)):
        i = np.concatenate([rng.choice(ix, len(ix), replace=True) for ix in idx_g])
        if y[i].min() == y[i].max():
            continue
        vals.append(aire_sous_courbe(s[i], y[i]))
    if len(vals) < 0.9 * tirages:
        raise GardeArret("intervalle : trop de tirages à une seule issue")
    a = (1 - niveau) / 2
    return float(np.quantile(vals, a)), float(np.quantile(vals, 1 - a))


def lecture_plantee_par_pli(scores, y, groupes, rng: np.random.Generator, seuil: float = 0.9, tirages: int = 2000,
                            niveau: float = 0.95, ecart_signal: float = 0.05) -> dict:
    """Garde de la vérité plantée, lecture (c) de la réponse 39 de Fable (docs/notes/demandes-fable-api-2026-11-22-v1/
    reponse-39/relecture-fable-api.md, § 1) : pour chaque pli k, A_k = aire au taux 0 sur les questions du pli, B_k =
    percentile bas de A_k sur `tirages` tirages avec remise dans le pli (tirage à une seule classe refait et compté).
    ARRÊT (champ « arret », liste de motifs ; vide = la garde passe) : plus petit B_k sous `seuil`, pli à une seule
    classe, score non fini. RAPPORTÉ sans arrêter : A_k, B_k, leur moyenne et sa borne basse, aire commune brute et
    recalée (rang moyen dans le pli ÷ effectif du pli), médianes des scores par classe et par pli, drapeau « écart
    d'échelle entre plis » si moyenne des A_k − aire commune brute > `ecart_signal` (seuil de signalement)."""
    s, y, g = np.asarray(scores, dtype=float), np.asarray(y), np.asarray(groupes)
    if not (s.shape == y.shape == g.shape) or s.ndim != 1:
        raise GardeArret("lecture plantée : scores, issues et plis de même longueur attendus")
    arret = []
    if not np.isfinite(s).all():
        return {"arret": ["score non fini"], "plis": []}
    ks = [int(k) for k in np.unique(g)]
    idx = {k: np.flatnonzero(g == k) for k in ks}
    plis, a_k = [], {}
    for k in ks:
        yk = y[idx[k]]
        n1, n0 = int(yk.sum()), int(len(yk) - yk.sum())
        if n1 == 0 or n0 == 0:
            arret.append(f"pli {k} à une seule classe ({n1} issues 1, {n0} issues 0)")
            continue
        a_k[k] = aire_sous_courbe(s[idx[k]], yk)
    if arret:
        return {"arret": arret, "plis": [{"pli": k, "aire": a_k.get(k)} for k in ks]}
    a = (1 - niveau) / 2
    vals, refaits = {k: [] for k in ks}, {k: 0 for k in ks}
    moyennes = []
    for _ in range(int(tirages)):
        cur = {}
        for k in ks:
            while True:
                i = rng.choice(idx[k], len(idx[k]), replace=True)
                if y[i].min() != y[i].max():
                    break
                refaits[k] += 1
                if refaits[k] > 10 * int(tirages):
                    raise GardeArret(f"lecture plantée : pli {k}, tirages à une seule classe sans fin")
            cur[k] = aire_sous_courbe(s[i], y[i])
            vals[k].append(cur[k])
        moyennes.append(float(np.mean([cur[k] for k in ks])))
    rang = np.empty(len(s))
    for k in ks:
        rang[idx[k]] = rankdata(s[idx[k]]) / len(idx[k])
    for k in ks:
        sk, yk = s[idx[k]], y[idx[k]]
        plis.append({"pli": k, "questions": int(len(idx[k])), "aire": a_k[k],
                     "borne_basse": float(np.quantile(vals[k], a)), "tirages_refaits": refaits[k],
                     "mediane_issue_1": float(np.median(sk[yk == 1])), "mediane_issue_0": float(np.median(sk[yk == 0]))})
    pire = min(p["borne_basse"] for p in plis)
    if pire < seuil:
        arret.append(f"pire pli : borne basse {pire:.3f} < {seuil}")
    moy = float(np.mean([a_k[k] for k in ks]))
    commun_brut = aire_sous_courbe(s, y)
    return {"arret": arret, "seuil": float(seuil), "niveau": float(niveau), "tirages": int(tirages), "plis": plis,
            "pire_borne_basse": float(pire), "aire_moyenne_des_plis": moy,
            "borne_basse_moyenne_des_plis": float(np.quantile(moyennes, a)),
            "aire_commune_brute": commun_brut, "aire_commune_recalee": aire_sous_courbe(rang, y),
            "ecart_d_echelle_entre_plis": bool(moy - commun_brut > ecart_signal), "ecart_signal": float(ecart_signal)}


def exiger_terme_final(gamma: float = RECETTE_TABLEAU_7["gamma"]) -> None:
    """Garde : la sonde nulle a une perte strictement positive dès qu'une issue vaut 1 (le terme final r − V(s_T) est
    compté, une fois par réponse). Sans ce terme, la sonde nulle aurait une perte nulle."""
    torch = _torch()
    v = torch.zeros(2, 3)
    p = float(perte_td(v, [3, 2], torch.tensor([1.0, 0.0]), gamma))
    if abs(p - 0.5) > 1e-9:
        raise GardeArret(f"terme final : perte de la sonde nulle {p}, 0,5 attendu (une réponse réussie sur deux)")


# --- contrôles de l'étape 1 ------------------------------------------------------------------------------------------

def etiquettes_permutees(r, rng: np.random.Generator) -> np.ndarray:
    return rng.permutation(np.asarray(r))


def verite_plantee(x0: np.ndarray, force: float, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Issue plantée lisible dans s_0 : direction tirée au hasard, P(r = 1) = sigmoïde(force × score centré réduit).
    Rend (étiquettes, direction)."""
    x = np.asarray(x0, dtype=np.float64)
    u = rng.standard_normal(x.shape[1])
    u /= np.linalg.norm(u)
    z = (x - x.mean(0)) @ u
    sd = z.std()
    if sd == 0:
        raise GardeArret("vérité plantée : projection constante")
    p = 1 / (1 + np.exp(-float(force) * z / sd))
    return (rng.random(len(p)) < p).astype(int), u


def injecter_verite(seqs_par_couche: dict, force: float, rng: np.random.Generator) -> tuple[dict, np.ndarray, np.ndarray]:
    """Vérité plantée par injection (plan des étapes 0-1, § B.3 point 9) : issue tirée à pile ou face par question ; une
    direction fixe u, tirée au hasard, est ajoutée à TOUS les états de la question, de signe égal à l'issue, de force
    a fois l'écart type de la projection des états (tous) de la couche sur u (a = 4 au plan). Rend (trajectoires
    injectées par couche, issues, u)."""
    couches = sorted(seqs_par_couche)
    n = len(seqs_par_couche[couches[0]])
    d = np.asarray(seqs_par_couche[couches[0]][0]).shape[1]
    y = rng.integers(0, 2, n)
    if y.min() == y.max():
        raise GardeArret("vérité plantée : une seule issue tirée")
    u = rng.standard_normal(d)
    u /= np.linalg.norm(u)
    sortie = {}
    for c in couches:
        proj = np.concatenate([np.asarray(t, dtype=np.float64) @ u for t in seqs_par_couche[c]])
        sd = float(proj.std())
        if sd == 0:
            raise GardeArret(f"vérité plantée : projection constante à la couche {c}")
        sortie[c] = [(np.asarray(t, dtype=np.float32) + np.float32(force * sd * (2 * y[i] - 1)) * u.astype(np.float32))
                     .astype(np.float16) for i, t in enumerate(seqs_par_couche[c])]
    return sortie, y, u


def poids_float16(m) -> dict:
    return {k: v.detach().cpu().numpy().astype(np.float16) for k, v in m.state_dict().items()}
