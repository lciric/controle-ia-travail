"""Outils hors ligne de la conception « monde riche écrit par Kimi et regroupement des doublons » — v1.

Concepteur neuf (Claude Opus 5.5, `claude-opus-5-5`), 12 novembre 2026. Aucun appel de modèle, aucun réseau, aucune clé.
numpy seul (interpréteur système). Rien n'est importé du dépôt de l'organisme (absent de cette machine) : le juge ci-dessous
est un **modèle simplifié** du juge de la boucle (nul v8 avec l'archive, `a_blanc_v59.juger_carte`), écrit d'après
`pole/nul_filles_v2.py`, `pole/selection_pari.py` et `pole/cycle.py` (`membres_de_l_archive`, `appliquer_multiplicite`) de
la copie `docs/notes/ideation-organisme-v1/orchestrateur-v52b/` ; son étalonnage contre les chiffres publiés de la course
v67 (monde S-V1) est fait par `puissance_monde_riche_v1.py etalonnage`.

Contenu :
- `probas` : évaluateur vectorisé de la grammaire des lois (types sans historique), égal à `selection_pari.proba` (essai) ;
- `compiler_monde` : d'un « devis de monde » (effets nommés : principal, seuil, interactions, sous-population, latent) à une
  loi de la grammaire existante (par_sous_population → si_sinon → softmax ; mélange pour le trait latent) ;
- `generer_monde_synthetique` : mondes de la famille MR-1 écrits par programme (calcul de puissance seulement) ;
- `Oracle` : gains exacts en espérance sur un échantillon d'instances (gain, au-delà de l'archive, au-delà de l'enveloppe
  du nul v8 de l'archive, information de chaque effet, attribution des effets à une loi) ;
- `juger` : juge simplifié (pari apparié, nul v8 avec l'archive, lecture aux instants fixés) ; `test_de_mort` ;
  `e_bh` (règle e-BH, avec groupes) ;
- `forme_canonique`, `distances_doublons`, `grouper` : regroupement des doublons ;
- `signature_traits`, `diversite_programme` : diversité sans oracle.
"""

import hashlib
import json
import math

import numpy as np

PLANCHER = 1e-12
ALPHA = 0.05
GRILLE = tuple(round(i / 20, 2) for i in range(21))
SEUIL_ORACLE = 0.02
SEUIL_MORT = 0.02
FENETRES = (5, 10, 20, 50)


def instants(n, pas=8):
    """Instants de lecture : `pas` instants régulièrement espacés, le dernier égal à n (25, 50, …, 200 pour n = 200)."""
    return tuple(sorted({max(1, round(n * (i + 1) / pas)) for i in range(pas)} | {n}))


def json_canonique(o):
    return json.dumps(o, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode("utf-8")


def empreinte(o):
    return hashlib.sha256(json_canonique(o)).hexdigest()


# --------------------------------------------------------------------------------------------------------------------
# Lois : évaluateur vectorisé (types sans historique de `selection_pari.TYPES_LOI`)
# --------------------------------------------------------------------------------------------------------------------

def _norm(P):
    P = np.maximum(P, PLANCHER)
    return P / P.sum(axis=1, keepdims=True)


def probas(loi, Z, G):
    """Tableau (n, K) des lois prédictives aux instances (Z : (n, D) traits ; G : (n,) sous-populations)."""
    t = loi["type"]
    n = Z.shape[0]
    if t == "fixe":
        p = np.maximum(np.asarray(loi["probas"], float), PLANCHER)
        return np.tile(p / p.sum(), (n, 1))
    if t == "softmax":
        W = np.asarray(loi["poids"], float)
        b = np.asarray(loi["biais"], float)
        S = Z @ W.T + b
        S = S - S.max(axis=1, keepdims=True)
        return _norm(np.exp(S))
    if t == "par_sous_population":
        out = None
        for g in np.unique(G):
            m = G == g
            sous = loi["lois"].get(str(int(g)), loi.get("defaut"))
            if sous is None:
                raise KeyError(f"par_sous_population : aucune loi pour la sous-population {int(g)} et aucun défaut")
            P = probas(sous, Z[m], G[m])
            if out is None:
                out = np.empty((n, P.shape[1]))
            out[m] = P
        return out
    if t == "melange":
        mix = None
        for w, c in zip(loi["poids"], loi["composantes"]):
            P = w * probas(c, Z, G)
            mix = P if mix is None else mix + P
        return _norm(mix)
    if t == "si_sinon":
        c = loi["condition"]
        if "sous_population" in c:
            m = G == c["sous_population"]
        else:
            m = Z[:, c["indice"]] > c.get("seuil", 0.0)
        return np.where(m[:, None], probas(loi["si"], Z, G), probas(loi["sinon"], Z, G))
    if t == "echelle":
        return probas(loi["loi"], Z / np.asarray(loi["facteurs"], float), G)
    if t == "enveloppe":
        tabs = [probas(l, Z, G) for l in loi["lois"]]
        return _norm(np.max(np.stack(tabs), axis=0))
    if t == "transformee":
        p = probas(loi["base"], Z, G)
        if loi.get("melange_aveugle"):
            lam = loi["melange_aveugle"]["lambda"]
            b = np.maximum(np.asarray(loi["melange_aveugle"]["probas"], float), PLANCHER)
            p = (1 - lam) * p + lam * (b / b.sum())
        if loi.get("puissance") is not None:
            p = _norm(np.maximum(p, PLANCHER) ** loi["puissance"])
        if loi.get("inclinaison"):
            p = _norm(p * np.exp(np.asarray(loi["inclinaison"], float)))
        if loi.get("oscillation"):
            o = loi["oscillation"]
            f = np.exp(o["amplitude"] * np.cos(o["frequence"] * Z[:, o["trait"]] + o.get("phase", 0.0)))
            p = p.copy()
            p[:, o["issue"]] *= f
            p = _norm(p)
        return _norm(p)
    raise ValueError(f"type de loi non pris en charge ici : {t!r}")


def tirer_instances(rng, n, D, nsp):
    """Instances publiques : traits indépendants N(0, 1) arrondis à six décimales ; sous-population uniforme."""
    return np.round(rng.standard_normal((n, D)), 6), rng.integers(0, nsp, n)


def tirer_issues(rng, P):
    u = rng.random(P.shape[0])
    return np.minimum((u[:, None] > np.cumsum(P, axis=1)).sum(axis=1), P.shape[1] - 1)


# --------------------------------------------------------------------------------------------------------------------
# Devis de monde → loi de la grammaire existante
# --------------------------------------------------------------------------------------------------------------------

TYPES_EFFETS = ("principal", "seuil", "interaction_seuil", "interaction_sous_population", "sous_population", "latent")


def _conditions(effets):
    return sorted({(e["trait_condition"] if e["type"] == "interaction_seuil" else e["trait"], float(e["seuil"]))
                   for e in effets if e["type"] in ("seuil", "interaction_seuil")})


def compiler_monde(spec, sans=(), facteurs=None):
    """Loi de la grammaire (par_sous_population → si_sinon → softmax ; mélange 1/2-1/2 si un trait latent) qui réalise le
    devis `spec`. `sans` : effets retirés (monde W₋ᵢ) ; `facteurs` : {identifiant : facteur d'échelle} (étalonnage)."""
    K, D, nsp = spec["nombre_issues"], spec["dimension"], spec["sous_populations"]
    effets = [e for e in spec["effets"] if e["id"] not in set(sans)]
    fac = facteurs or {}
    conds = _conditions(effets)
    depend_sp = any(e["type"] in ("interaction_sous_population", "sous_population") for e in effets)
    latents = [e for e in effets if e["type"] == "latent"]
    if len(latents) > 1:
        raise ValueError("au plus un trait latent")

    def feuille(g, actives, signe):
        W = np.zeros((K, D))
        b = np.array(spec["biais"], float)
        for e in effets:
            f, ty = fac.get(e["id"], 1.0), e["type"]
            if ty == "principal":
                W[:, e["trait"]] += f * np.asarray(e["pente"], float)
            elif ty == "seuil" and (e["trait"], float(e["seuil"])) in actives:
                b += f * np.asarray(e["decalage"], float)
            elif ty == "interaction_seuil" and (e["trait_condition"], float(e["seuil"])) in actives:
                W[:, e["trait"]] += f * np.asarray(e["pente"], float)
            elif ty == "interaction_sous_population" and g == e["sous_population"]:
                W[:, e["trait"]] += f * np.asarray(e["pente"], float)
            elif ty == "sous_population" and g == e["sous_population"]:
                b += f * np.asarray(e["decalage"], float)
            elif ty == "latent":
                b += signe * f * np.asarray(e["decalage"], float)
        return {"type": "softmax", "poids": np.round(W, 6).tolist(), "biais": np.round(b, 6).tolist()}

    def arbre(g, i, actives, signe):
        if i == len(conds):
            return feuille(g, actives, signe)
        tr, se = conds[i]
        return {"type": "si_sinon", "condition": {"indice": int(tr), "seuil": se},
                "si": arbre(g, i + 1, actives | {conds[i]}, signe), "sinon": arbre(g, i + 1, actives, signe)}

    def par_sp(signe):
        if not depend_sp:
            return arbre(None, 0, frozenset(), signe)
        return {"type": "par_sous_population", "lois": {str(g): arbre(g, 0, frozenset(), signe) for g in range(nsp)}}

    if latents:
        w = float(latents[0].get("poids_melange", 0.5))
        return {"type": "melange", "composantes": [par_sp(+1.0), par_sp(-1.0)], "poids": [w, 1.0 - w]}
    return par_sp(0.0)


def traits_d_un_effet(e):
    ty = e["type"]
    if ty == "principal" or ty == "seuil":
        return {e["trait"]}
    if ty == "interaction_seuil":
        return {e["trait"], e["trait_condition"]}
    if ty == "interaction_sous_population":
        return {e["trait"], "g"}
    if ty == "sous_population":
        return {"g"}
    return {"latent"}


# --------------------------------------------------------------------------------------------------------------------
# Oracle (lu une seule fois, après la course ; ici, pour la conception et la vérification du monde)
# --------------------------------------------------------------------------------------------------------------------

def _lse(S):
    m = S.max(axis=1, keepdims=True)
    return (m[:, 0] + np.log(np.exp(S - m).sum(axis=1)))


def ajuste_log_doux(Q, A, iterations=60):
    """max_θ Σ_s Σ_k Q_sk log softmax_k(a·log A_sk + β_k), β_0 = 0 (A tempérée et inclinée) ; Q : poids (étiquettes douces,
    ou indicatrices). Rend (valeur, θ)."""
    n, K = A.shape
    L = np.log(np.maximum(A, PLANCHER))
    X = np.zeros((n, K, K))
    X[:, :, 0] = L
    for k in range(1, K):
        X[:, k, k] = 1.0
    theta = np.zeros(K)
    theta[0] = 1.0

    def val(th):
        S = X @ th
        return float((Q * (S - _lse(S)[:, None])).sum()), S

    f, S = val(theta)
    for _ in range(iterations):
        P = np.exp(S - _lse(S)[:, None])
        moy = np.einsum("sk,skp->sp", P, X)
        g = np.einsum("sk,skp->p", Q, X) - Q.sum(axis=1) @ moy
        c = X - moy[:, None, :]
        H = -np.einsum("s,sk,skp,skq->pq", Q.sum(axis=1), P, c, c) - 1e-9 * np.eye(K)
        try:
            pas = np.linalg.solve(H, -g)
        except np.linalg.LinAlgError:
            pas = np.linalg.lstsq(H, -g, rcond=None)[0]
        dec = float(max(0.0, g @ pas))
        if dec < 1e-12:
            break
        u = 1.0
        while u > 1e-8:
            essai = np.clip(theta + u * pas, -60, 60)
            f2, S2 = val(essai)
            if f2 >= f + 1e-4 * u * float(g @ pas) or f2 > f:
                break
            u *= 0.5
        if u <= 1e-8:
            break
        theta, f, S = essai, f2, S2
    return f, theta


def ajuste_lineaire_doux(Q, tables, iterations=4000, tol=1e-7):
    """max sur le simplexe de Σ_s Σ_k Q_sk log(Σ_j π_j T_j[s,k] + Σ_k' ρ_k' 1[k = k']) (lois de l'archive et lois certaines) ;
    espérance-maximisation ; rend (valeur + écart de Frank-Wolfe borné à 0 par excès, poids)."""
    n, K = Q.shape
    comps = [np.asarray(T, float) for T in tables] + [np.tile(np.eye(K)[k], (n, 1)) for k in range(K)]
    C = np.stack(comps, axis=2)  # (n, K, J)
    J = C.shape[2]
    w = np.full(J, 1.0 / J)
    tot = Q.sum()
    for _ in range(iterations):
        M = np.maximum(C @ w, PLANCHER)
        grad = np.einsum("sk,skj->j", Q / M, C)
        ecart = float(grad.max() - tot)
        if ecart < tol * max(1.0, tot):
            break
        w = w * grad / tot
        w /= w.sum()
    M = np.maximum(C @ w, PLANCHER)
    grad = np.einsum("sk,skj->j", Q / M, C)
    ecart = max(0.0, float(grad.max() - tot))
    # M ≤ 1 partout : la log-vraisemblance est ≤ 0, d'où la borne 0 (comme `nul_filles_v2._lineaire`).
    return min(0.0, float((Q * np.log(M)).sum()) + ecart), w


class Oracle:
    """Espérances exactes sur un échantillon fixe d'instances publiques (aucun tirage d'issue)."""

    def __init__(self, monde_loi, D, nsp, n=20000, graine=20261112):
        rng = np.random.default_rng(np.random.SeedSequence(graine))
        self.Z, self.G = tirer_instances(rng, n, D, nsp)
        self.D, self.nsp = D, nsp
        self.Q = probas(monde_loi, self.Z, self.G)
        self.marg = self.Q.mean(axis=0)

    def P(self, loi):
        return probas(loi, self.Z, self.G)

    def gain(self, loi, Q=None):
        """Gain moyen de log-score de la loi sur la marginale, sous le monde (ou sous la loi Q d'un autre monde)."""
        Q = self.Q if Q is None else Q
        m = Q.mean(axis=0)
        return float((Q * (np.log(np.maximum(self.P(loi), PLANCHER)) - np.log(m))).sum(axis=1).mean())

    def gain_au_dela(self, loi, archive):
        """Au sens de l'oracle v60 : gain moins le plus grand gain d'une loi de l'archive prise seule."""
        g = self.gain(loi)
        return g - max([self.gain(a) for a in archive], default=0.0)

    def gain_enveloppe(self, archive):
        """Gain de la meilleure loi de l'enveloppe du nul v8 de l'archive, ajustée sous le monde (étiquettes douces) :
        chaque loi seule, mêlée à l'uniforme (grille), tempérée et inclinée ; mélange linéaire de toutes et des lois
        certaines. Borne haute de ce qu'une recombinaison couverte de l'archive peut gagner."""
        if not archive:
            return 0.0
        n = self.Q.shape[0]
        logm = np.log(self.marg)
        base = float((self.Q * logm).sum()) / n
        tabs = [self.P(a) for a in archive]
        meilleurs = []
        U = np.full_like(self.Q, 1.0 / self.Q.shape[1])
        for T in tabs:
            for w in GRILLE:
                meilleurs.append(float((self.Q * np.log(np.maximum(w * T + (1 - w) * U, PLANCHER))).sum()) / n)
            meilleurs.append(ajuste_log_doux(self.Q, T)[0] / n)
        meilleurs.append(ajuste_lineaire_doux(self.Q, tabs)[0] / n)
        return max(meilleurs) - base

    def gain_au_dela_enveloppe(self, loi, archive):
        return self.gain(loi) - self.gain_enveloppe(archive)

    def information_effet(self, spec, eid):
        """I_i = E_x KL(W(·|x) ‖ W₋ᵢ(·|x)) : information perdue en retirant l'effet i du monde (les autres gardés)."""
        Qm = probas(compiler_monde(spec, sans=(eid,)), self.Z, self.G)
        return float((self.Q * (np.log(np.maximum(self.Q, PLANCHER)) - np.log(np.maximum(Qm, PLANCHER)))).sum(axis=1).mean())

    def attribution(self, loi, spec, tau=None):
        """Δ_i(h) = gain(h | W) − gain(h | W₋ᵢ) pour chaque effet i : la loi « capte » l'effet i si Δ_i ≥ τ_i
        (par défaut τ_i = max(0,005 ; 0,75·I_i) : seuil choisi sur deux mondes synthétiques, où l'effet capté donne
        Δ_i ≥ 1,2·I_i et un effet non capté |Δ_i| ≤ 0,45·I_i ; à éprouver par `puissance_monde_riche_v1.py attribution`)."""
        P = np.log(np.maximum(self.P(loi), PLANCHER))
        out = {}
        g = float((self.Q * (P - np.log(self.marg))).sum(axis=1).mean())
        for e in spec["effets"]:
            Qm = probas(compiler_monde(spec, sans=(e["id"],)), self.Z, self.G)
            gm = float((Qm * (P - np.log(Qm.mean(axis=0)))).sum(axis=1).mean())
            out[e["id"]] = g - gm
        return out


def captes(attr, infos, plancher=0.005, part=0.75):
    return sorted(i for i, d in attr.items() if d >= max(plancher, part * infos[i]))


# --------------------------------------------------------------------------------------------------------------------
# Juge simplifié : pari apparié contre le nul v8 avec l'archive (modèle de `a_blanc_v59.juger_carte`)
# --------------------------------------------------------------------------------------------------------------------

def _traj_marginale_mv(Y, K):
    C = np.cumsum(np.eye(K)[Y], axis=0)
    t = np.arange(1, len(Y) + 1)[:, None]
    with np.errstate(divide="ignore", invalid="ignore"):
        v = np.where(C > 0, C * np.log(C / t), 0.0)
    return v.sum(axis=1)


def _traj_urne(Y, K):
    from math import lgamma
    C = np.zeros(K)
    out = np.empty(len(Y))
    for i, y in enumerate(Y):
        C[y] += 1
        out[i] = sum(lgamma(c + 1) for c in C) - lgamma(i + 2)
    return out


def _traj_moyennes_glissantes(Y, K, lam=0.5):
    meilleure = None
    for w in FENETRES:
        compte = np.zeros(K)
        file, cumul, sortie = [], 0.0, np.empty(len(Y))
        for i, y in enumerate(Y):
            cumul += math.log((compte[y] + lam) / (len(file) + K * lam))
            sortie[i] = cumul
            file.append(y)
            compte[y] += 1
            if len(file) > w:
                compte[file.pop(0)] -= 1
        meilleure = sortie if meilleure is None else np.maximum(meilleure, sortie)
    return meilleure


AVEC_URNE = False  # choisi par l'étalonnage sur la course v67 (voir `puissance_monde_riche_v1.py etalonnage`)


def juger(loi, archive, monde, D, nsp, rng, n=200, lecture=None, avec_standard=True, avec_urne=None):
    """Richesse du pari de `loi` contre le nul v8 de `archive` (liste de lois) sur n tirages frais du monde.

    Membres : marginale ajustée, uniforme, moyennes glissantes (bibliothèque standard v0 ; l'urne de la v1 en option,
    écartée par l'étalonnage) ; par loi d'archive : la loi,
    son mélange à l'uniforme (grille), sa version tempérée et inclinée ajustée ; mélange linéaire de toutes les lois de
    l'archive et des lois certaines, ajusté. Membres ajustés lus aux instants de lecture sur les t premières issues.
    Rend {traj (log W aux instants), log_w_max, dominant, instants}."""
    lecture = lecture or instants(n)
    Z, G = tirer_instances(rng, n, D, nsp)
    Y = tirer_issues(rng, probas(monde, Z, G))
    K = probas(loi, Z[:1], G[:1]).shape[1]
    idx = np.arange(n)
    num = np.cumsum(np.log(np.maximum(probas(loi, Z, G)[idx, Y], PLANCHER)))
    ordinaires = {}
    if avec_standard:
        ordinaires["marginale_empirique"] = _traj_marginale_mv(Y, K)
        ordinaires["uniforme"] = -np.arange(1, n + 1) * math.log(K)
        ordinaires["moyenne_glissante"] = _traj_moyennes_glissantes(Y, K)
        if (AVEC_URNE if avec_urne is None else avec_urne):
            ordinaires["urne"] = _traj_urne(Y, K)
    tabs = [probas(a, Z, G) for a in archive]
    U = 1.0 / K
    for j, T in enumerate(tabs):
        py = T[idx, Y]
        ordinaires[f"archive:{j}"] = np.cumsum(np.log(np.maximum(py, PLANCHER)))
        couvert = np.max(np.stack([np.cumsum(np.log(np.maximum(w * py + (1 - w) * U, PLANCHER))) for w in GRILLE]), axis=0)
        ordinaires[f"archive_couvert:{j}"] = couvert
    Yoh = np.eye(K)[Y]
    traj, dominants = [], []
    for t in lecture:
        cands = [(float(v[t - 1]), nom) for nom, v in ordinaires.items()]
        for j, T in enumerate(tabs):
            f, _ = ajuste_log_doux(Yoh[:t], T[:t])
            cands.append((min(0.0, f), f"ajuste_log:archive:{j}"))
        if tabs:
            f, _ = ajuste_lineaire_doux(Yoh[:t], [T[:t] for T in tabs], iterations=1500, tol=1e-6)
            cands.append((min(0.0, f), "ajuste_lineaire:archive"))
        meilleur, nom = max(cands)
        traj.append(float(num[t - 1]) - meilleur)
        dominants.append(nom)
    return {"traj": traj, "log_w_max": max(traj), "dominant": dominants[-1], "instants": list(lecture)}


def log_e_arrete(traj, seuil):
    return next((v for v in traj if v >= seuil), traj[-1])


def promue_hors_famille(ev, m, alpha=ALPHA):
    seuil = math.log(m / alpha)
    le = log_e_arrete(ev["traj"], seuil)
    return (ev["log_w_max"] >= math.log(1 / alpha)) and le >= seuil, le


def e_bh(log_es, m, alpha=ALPHA):
    """log_es : {clé : log e arrêtée} ; rend la liste des clés retenues (règle e-BH, Wang et Ramdas 2022)."""
    ordre = sorted(log_es, key=lambda c: (-log_es[c], str(c)))
    k_et = 0
    for k, c in enumerate(ordre, 1):
        if log_es[c] >= math.log(m / (alpha * k)):
            k_et = k
    return ordre[:k_et]


def test_de_mort(loi, monde, D, nsp, rng, n=400, seuil=SEUIL_MORT):
    """Statistique gelée du tour fermé : gain moyen de log-score sur la marginale empirique de la tranche (comptes + 0,5)."""
    Z, G = tirer_instances(rng, n, D, nsp)
    Y = tirer_issues(rng, probas(monde, Z, G))
    K = probas(loi, Z[:1], G[:1]).shape[1]
    c = np.bincount(Y, minlength=K) + 0.5
    marg = c / c.sum()
    P = probas(loi, Z, G)
    s = float(np.mean(np.log(np.maximum(P[np.arange(n), Y], PLANCHER)) - np.log(marg[Y])))
    return s, s >= seuil


# --------------------------------------------------------------------------------------------------------------------
# Regroupement des doublons (programme ; aucun tirage d'issue, aucun oracle)
# --------------------------------------------------------------------------------------------------------------------

def _r6(x):
    return float(np.round(float(x), 6)) + 0.0


def forme_canonique(loi):
    """Forme canonique d'une loi : flottants à six décimales ; softmax recentrée sur la ligne 0 (invariance du softmax) ;
    mélange sans poids nul, composantes triées et fusionnées, composante seule déballée ; transformée sans étape déballée ;
    si/sinon à branches égales déballé ; loi fixe normalisée."""
    t = loi["type"]
    if t == "fixe":
        p = np.maximum(np.asarray(loi["probas"], float), 0.0)
        p = p / p.sum()
        return {"type": "fixe", "probas": [_r6(x) for x in p]}
    if t == "softmax":
        W = np.asarray(loi["poids"], float)
        b = np.asarray(loi["biais"], float)
        W, b = W - W[0], b - b[0]
        return {"type": "softmax", "poids": [[_r6(x) for x in l] for l in W], "biais": [_r6(x) for x in b]}
    if t == "melange":
        acc = {}
        for w, c in zip(loi["poids"], loi["composantes"]):
            if w <= 0:
                continue
            cc = forme_canonique(c)
            h = empreinte(cc)
            acc[h] = (acc.get(h, (0.0, cc))[0] + float(w), cc)
        if len(acc) == 1:
            return next(iter(acc.values()))[1]
        cles = sorted(acc)
        return {"type": "melange", "composantes": [acc[h][1] for h in cles], "poids": [_r6(acc[h][0]) for h in cles]}
    if t == "transformee":
        base = forme_canonique(loi["base"])
        out = {"type": "transformee", "base": base}
        if loi.get("melange_aveugle") and loi["melange_aveugle"]["lambda"] > 0:
            out["melange_aveugle"] = {"lambda": _r6(loi["melange_aveugle"]["lambda"]),
                                      "probas": forme_canonique({"type": "fixe", "probas": loi["melange_aveugle"]["probas"]})["probas"]}
        if loi.get("puissance") is not None and abs(loi["puissance"] - 1.0) > 1e-9:
            out["puissance"] = _r6(loi["puissance"])
        if loi.get("inclinaison"):
            b = np.asarray(loi["inclinaison"], float)
            b = b - b[0]
            if np.any(np.abs(b) > 1e-9):
                out["inclinaison"] = [_r6(x) for x in b]
        if loi.get("oscillation"):
            out["oscillation"] = {k: (_r6(v) if isinstance(v, float) else v) for k, v in sorted(loi["oscillation"].items())}
        return base if len(out) == 2 else out
    if t == "si_sinon":
        si, sinon = forme_canonique(loi["si"]), forme_canonique(loi["sinon"])
        if empreinte(si) == empreinte(sinon):
            return si
        c = dict(loi["condition"])
        if "seuil" in c:
            c["seuil"] = _r6(c["seuil"])
        elif "indice" in c:
            c["seuil"] = 0.0
        return {"type": "si_sinon", "condition": c, "si": si, "sinon": sinon}
    if t == "par_sous_population":
        lois = {k: forme_canonique(v) for k, v in sorted(loi["lois"].items())}
        out = {"type": "par_sous_population", "lois": lois}
        if "defaut" in loi:
            out["defaut"] = forme_canonique(loi["defaut"])
        return out
    if t == "echelle":
        return {"type": "echelle", "facteurs": [_r6(x) for x in loi["facteurs"]], "loi": forme_canonique(loi["loi"])}
    if t == "enveloppe":
        lois = sorted((forme_canonique(l) for l in loi["lois"]), key=empreinte)
        return {"type": "enveloppe", "lois": lois}
    return json.loads(json_canonique(loi))


def _kl_moyen(P, Q):
    return float((P * (np.log(np.maximum(P, PLANCHER)) - np.log(np.maximum(Q, PLANCHER)))).sum(axis=1).mean())


def distance_au_nul(Ph, Pa):
    """Ce que la loi h rapporterait par épisode au-delà du nul v8 engendré par la seule loi a, **si h était le monde** :
    min sur les membres m de ce nul (a seule ; a mêlée à toute loi aveugle fixe ; a tempérée et inclinée) de E_x KL(h ‖ m).
    Rend (distance en nat par épisode, borne au pire monde E_x max_y |log h − log m*|)."""
    n = Ph.shape[0]
    f_lin, w = ajuste_lineaire_doux(Ph, [Pa], iterations=3000, tol=1e-8)
    K = Ph.shape[1]
    M_lin = np.maximum(w[0] * Pa + np.tile(w[1:], (n, 1)), PLANCHER)
    _, th = ajuste_log_doux(Ph, Pa)
    S = th[0] * np.log(np.maximum(Pa, PLANCHER)) + np.concatenate([[0.0], th[1:]])[None, :]
    M_log = np.exp(S - _lse(S)[:, None])
    cand = []
    for M in (M_lin, M_log, Pa):
        cand.append((_kl_moyen(Ph, M), float(np.abs(np.log(np.maximum(Ph, PLANCHER)) - np.log(np.maximum(M, PLANCHER))).max(axis=1).mean())))
    return min(cand)


def distances_doublons(lois, Zref, Gref):
    """Matrices (N × N) : d_nul[i][j] = distance au nul de la loi j pour la loi i ; d_inf (borne au pire monde) ;
    canon (formes canoniques égales)."""
    N = len(lois)
    Ps = [probas(l, Zref, Gref) for l in lois]
    can = [empreinte(forme_canonique(l)) for l in lois]
    dn = np.zeros((N, N))
    di = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == j or can[i] == can[j]:
                continue
            dn[i, j], di[i, j] = distance_au_nul(Ps[i], Ps[j])
    return dn, di, can


def grouper(lois, Zref, Gref, eps=0.01, ordre=None):
    """Regroupement par liaison complète : d(i, j) = min(d_nul[i][j], d_nul[j][i]) (0 si formes canoniques égales) ;
    deux groupes fusionnent si toutes leurs paires sont sous `eps` ; la paire de groupes la plus proche d'abord ; égalités
    rompues par l'ordre canonique (empreinte de la forme canonique), jamais par le fournisseur. Rend (groupes : listes
    d'indices, matrices)."""
    dn, di, can = distances_doublons(lois, Zref, Gref)
    N = len(lois)
    d = np.minimum(dn, dn.T)
    for i in range(N):
        for j in range(N):
            if can[i] == can[j]:
                d[i, j] = 0.0
    rang = {i: r for r, i in enumerate(sorted(range(N), key=lambda i: (can[i], i)))} if ordre is None else ordre
    groupes = [[i] for i in sorted(range(N), key=lambda i: rang[i])]
    while True:
        meilleur = None
        for a in range(len(groupes)):
            for b in range(a + 1, len(groupes)):
                dmax = max(d[i, j] for i in groupes[a] for j in groupes[b])
                if dmax < eps:
                    cle = (dmax, rang[groupes[a][0]], rang[groupes[b][0]])
                    if meilleur is None or cle < meilleur[0]:
                        meilleur = (cle, a, b)
        if meilleur is None:
            break
        _, a, b = meilleur
        groupes[a] = sorted(groupes[a] + groupes[b], key=lambda i: rang[i])
        del groupes[b]
    return groupes, {"d": d, "d_nul": dn, "d_inf": di, "canon": can}


def elaguer(ordre, lois, archive, monde, D, nsp, rng_de_tache, m, n=200, alpha=ALPHA):
    """Étape B du regroupement : **élagage par domination**, jugé sur tirages frais (jamais par l'oracle).

    `ordre` : indices des représentants promus, par log e décroissant. Pour chaque représentant h et chaque représentant
    k déjà gardé : k « au-delà de » h = k promu (seuil hors famille log(m/α), tirages neufs, tâche propre à la paire)
    contre le nul v8 de archive ∪ {h} ; de même h au-delà de k. h est **dominé** (écarté) si k va au-delà de h et h pas
    au-delà de k ; si h domine k, k est écarté. Deux lois complémentaires (chacune apporte un effet que l'autre n'a pas)
    ne se dominent pas : elles sont gardées toutes deux. Un élagage plus simple (« garder h seulement s'il bat le nul de
    l'archive et de tous les gardés ») écarte aussi les lois complémentaires : rejeté (essai hors ligne, dit dans la
    conception). Rend (gardés, détail des paires)."""
    gardes, detail = [], []
    for h in ordre:
        domine = False
        for k in list(gardes):
            evk = juger(lois[k], list(archive) + [lois[h]], monde, D, nsp, rng_de_tache((k, h)), n=n)
            evh = juger(lois[h], list(archive) + [lois[k]], monde, D, nsp, rng_de_tache((h, k)), n=n)
            k_sur_h = promue_hors_famille(evk, m, alpha)[0]
            h_sur_k = promue_hors_famille(evh, m, alpha)[0]
            detail.append({"h": h, "k": k, "k_au_dela_de_h": bool(k_sur_h), "h_au_dela_de_k": bool(h_sur_k)})
            if k_sur_h and not h_sur_k:
                domine = True
                break
            if h_sur_k and not k_sur_h:
                gardes.remove(k)
        if not domine:
            gardes.append(h)
    return gardes, detail


def log_e_groupe(log_es):
    """e-valeur d'un groupe : moyenne des e-valeurs (arrêtées) de ses membres ; une moyenne d'e-valeurs est une e-valeur."""
    v = np.asarray(log_es, float)
    m = v.max()
    return float(m + math.log(np.exp(v - m).mean()))


# --------------------------------------------------------------------------------------------------------------------
# Diversité sans oracle
# --------------------------------------------------------------------------------------------------------------------

def signature_traits(loi, Zref, Gref, nsp, rng):
    """Sensibilité de la loi à chaque trait j (E_x KL(h(x) ‖ h(x avec z_j remplacé par un tirage indépendant))) et à la
    sous-population (même chose, g retiré au hasard) : vecteur de longueur D + 1, en nat."""
    P = probas(loi, Zref, Gref)
    out = []
    for j in range(Zref.shape[1]):
        Z2 = Zref.copy()
        Z2[:, j] = np.round(rng.standard_normal(Zref.shape[0]), 6)
        out.append(_kl_moyen(P, probas(loi, Z2, Gref)))
    out.append(_kl_moyen(P, probas(loi, Zref, rng.integers(0, nsp, Zref.shape[0]))))
    return np.asarray(out)


def diversite_programme(lois, Zref, Gref, nsp, rng, eps=0.01, seuil_trait=0.005):
    """Mesures sans oracle d'un ensemble de lois : groupes de doublons, supports de traits distincts, traits couverts,
    entropie de la signature agrégée, distance moyenne entre paires."""
    if not lois:
        return {"lois": 0, "groupes": 0, "supports_distincts": 0, "traits_couverts": 0, "entropie_signature": 0.0,
                "distance_moyenne_paires": None}
    groupes, mats = grouper(lois, Zref, Gref, eps=eps)
    sig = np.stack([signature_traits(l, Zref, Gref, nsp, rng) for l in lois])
    supports = {tuple(np.nonzero(s >= seuil_trait)[0].tolist()) for s in sig}
    couverts = np.nonzero((sig >= seuil_trait).any(axis=0))[0]
    agr = sig.sum(axis=0)
    p = agr / agr.sum() if agr.sum() > 0 else agr
    ent = float(-(p[p > 0] * np.log(p[p > 0])).sum())
    N = len(lois)
    paires = [mats["d"][i, j] for i in range(N) for j in range(i + 1, N)]
    return {"lois": N, "groupes": len(groupes), "supports_distincts": len(supports), "traits_couverts": int(len(couverts)),
            "entropie_signature": round(ent, 4),
            "distance_moyenne_paires": None if not paires else round(float(np.mean(paires)), 5)}


# --------------------------------------------------------------------------------------------------------------------
# Mondes synthétiques de la famille MR-1 (écrits par programme ; jamais par Kimi)
# --------------------------------------------------------------------------------------------------------------------

CLASSES_MR1 = {"forte": (0.10, 0.25), "moyenne": (0.04, 0.08), "faible": (0.02, 0.035)}
GABARIT_MR1 = (("forte", "principal"), ("forte", "principal"), ("moyenne", "interaction_seuil"),
               ("moyenne", "interaction_sous_population"), ("faible", "principal"), ("faible", "seuil"),
               ("faible", "sous_population"))


def _direction(rng, K=3):
    v = rng.standard_normal(K)
    v -= v.mean()
    return v / np.linalg.norm(v)


def generer_monde_synthetique(graine, D=8, nsp=3, K=3, gabarit=GABARIT_MR1, latent=False, n_oracle=8000):
    """Devis de monde MR-1 tiré au hasard puis étalonné (échelle de chaque effet ajustée par bissection pour que son
    information I_i tombe au milieu de sa classe). Rend (spec, informations, cibles)."""
    rng = np.random.default_rng(np.random.SeedSequence(graine))
    traits = list(rng.permutation(D))
    effets, cibles = [], {}
    pris = []
    for i, (classe, ty) in enumerate(gabarit):
        eid = f"E{i + 1}"
        lo, hi = CLASSES_MR1[classe]
        cibles[eid] = (classe, float(rng.uniform(lo + 0.15 * (hi - lo), hi - 0.15 * (hi - lo))))
        if ty == "principal":
            tr = traits.pop(0)
            pris.append(tr)
            effets.append({"id": eid, "type": ty, "trait": int(tr), "pente": _direction(rng, K).tolist()})
        elif ty == "seuil":
            tr = traits.pop(0)
            effets.append({"id": eid, "type": ty, "trait": int(tr), "seuil": float(np.round(rng.uniform(0.3, 1.0), 2)),
                           "decalage": _direction(rng, K).tolist()})
        elif ty == "interaction_seuil":
            tr = traits.pop(0)
            cond = int(pris[0]) if pris else int(traits.pop(0))
            effets.append({"id": eid, "type": ty, "trait_condition": cond, "seuil": 0.0, "trait": int(tr),
                           "pente": _direction(rng, K).tolist()})
        elif ty == "interaction_sous_population":
            tr = traits.pop(0)
            effets.append({"id": eid, "type": ty, "sous_population": int(rng.integers(0, nsp)), "trait": int(tr),
                           "pente": _direction(rng, K).tolist()})
        elif ty == "sous_population":
            effets.append({"id": eid, "type": ty, "sous_population": int(rng.integers(0, nsp)),
                           "decalage": _direction(rng, K).tolist()})
    if latent:
        effets.append({"id": f"E{len(effets) + 1}", "type": "latent", "poids_melange": 0.5, "decalage": _direction(rng, K).tolist()})
        cibles[effets[-1]["id"]] = ("moyenne", 0.05)
    for e in effets:
        e["classe"] = cibles[e["id"]][0]
    spec = {"version": "monde-riche-spec-v1", "nombre_issues": K, "dimension": D, "sous_populations": nsp,
            "biais": np.round(rng.normal(0, 0.3, K), 6).tolist(), "effets": effets, "distracteurs": sorted(int(t) for t in traits)}
    # étalonnage : bissection sur l'échelle de chaque effet, trois passes (les informations dépendent un peu des autres)
    Zg, Gg = tirer_instances(np.random.default_rng(np.random.SeedSequence([graine, 7])), n_oracle, D, nsp)
    fac = {e["id"]: 1.0 for e in effets}

    def info(eid, f):
        f2 = dict(fac, **{eid: f})
        Q = probas(compiler_monde(spec, facteurs=f2), Zg, Gg)
        Qm = probas(compiler_monde(spec, sans=(eid,), facteurs=f2), Zg, Gg)
        return float((Q * (np.log(np.maximum(Q, PLANCHER)) - np.log(np.maximum(Qm, PLANCHER)))).sum(axis=1).mean())

    for _ in range(3):
        for e in effets:
            cible = cibles[e["id"]][1]
            lo, hi = 0.0, 12.0
            for _ in range(28):
                mid = 0.5 * (lo + hi)
                if info(e["id"], mid) < cible:
                    lo = mid
                else:
                    hi = mid
            fac[e["id"]] = 0.5 * (lo + hi)
    for e in effets:
        f = fac[e["id"]]
        for cle in ("pente", "decalage"):
            if cle in e:
                e[cle] = np.round(np.asarray(e[cle]) * f, 6).tolist()
    return spec, cibles


def k1_du_monde(spec, oracle, eid=None):
    """Loi connue de départ : softmax du seul trait de l'effet principal le plus fort (ou de `eid`), ajustée sous le monde
    (étiquettes douces, Newton), arrondie à six décimales."""
    infos = {e["id"]: oracle.information_effet(spec, e["id"]) for e in spec["effets"]}
    if eid is None:
        eid = max((e for e in spec["effets"] if e["type"] == "principal"), key=lambda e: infos[e["id"]])["id"]
    e = next(x for x in spec["effets"] if x["id"] == eid)
    j = e["trait"]
    K, D = spec["nombre_issues"], spec["dimension"]
    # régression softmax sur (1, z_j), étiquettes douces Q
    X = np.stack([np.ones(len(oracle.Z)), oracle.Z[:, j]], axis=1)
    th = np.zeros((K - 1, 2))
    Q = oracle.Q
    for _ in range(50):
        S = np.concatenate([np.zeros((len(X), 1)), X @ th.T], axis=1)
        P = np.exp(S - _lse(S)[:, None])
        g = ((Q[:, 1:] - P[:, 1:])[:, :, None] * X[:, None, :]).sum(axis=0).reshape(-1)
        H = np.zeros(((K - 1) * 2, (K - 1) * 2))
        for a in range(K - 1):
            for b in range(K - 1):
                w = P[:, a + 1] * ((a == b) - P[:, b + 1])
                H[a * 2:(a + 1) * 2, b * 2:(b + 1) * 2] = -(X * w[:, None]).T @ X
        pas = np.linalg.solve(H - 1e-9 * np.eye(len(g)), -g)
        th = th + pas.reshape(K - 1, 2)
        if float(g @ pas) < 1e-12:
            break
    W = np.zeros((K, D))
    W[1:, j] = th[:, 1]
    b = np.concatenate([[0.0], th[:, 0]])
    return {"type": "softmax", "poids": np.round(W, 6).tolist(), "biais": np.round(b, 6).tolist()}, eid, infos


def monde_restreint(spec, garder, k1=None):
    """Loi vraie partielle : le monde réduit aux effets `garder` (les autres retirés), biais gardé."""
    sans = [e["id"] for e in spec["effets"] if e["id"] not in set(garder)]
    return compiler_monde(spec, sans=sans)


def calibrer(loi, oracle):
    """La loi tempérée et inclinée (p ∝ loi^a·exp(β)) au maximum de vraisemblance attendue sous le monde : une loi partielle
    juste mais trop confiante (effets manquants) devient calibrée. Rend une « transformee » de la grammaire."""
    _, th = ajuste_log_doux(oracle.Q, oracle.P(loi))
    return {"type": "transformee", "base": loi, "puissance": round(max(float(th[0]), 1e-3), 6),
            "inclinaison": [0.0] + [round(float(x), 6) for x in th[1:]]}


def diluer(monde, k1, oracle, cible):
    """Mélange λ·monde + (1 − λ)·K1, λ choisi par bissection pour que son gain au-delà de {K1} (sens v60) vaille `cible`.
    Hors de la classe couverte (le monde n'est pas une loi de l'archive) : une vraie « faible » au sens du gain."""
    g1 = oracle.gain(k1)
    lo, hi = 0.0, 1.0
    for _ in range(40):
        lam = 0.5 * (lo + hi)
        g = oracle.gain({"type": "melange", "composantes": [monde, k1], "poids": [lam, 1.0 - lam]}) - g1
        lo, hi = (lam, hi) if g < cible else (lo, lam)
    lam = round(0.5 * (lo + hi), 6)
    return {"type": "melange", "composantes": [monde, k1], "poids": [lam, round(1.0 - lam, 6)]}


UNIFORME3 = {"type": "fixe", "probas": [1.0, 1.0, 1.0]}
AVEUGLE3 = {"type": "fixe", "probas": [0.3, 0.4, 0.3]}


def fausses_couvertes(k):
    """Recombinaisons de la loi connue seule (classe couverte du nul v8, lignes T17s, T03u, T03b, T05s du banc)."""
    return {"F1-copie": json.loads(json.dumps(k)),
            "F2-melee-uniforme": {"type": "melange", "composantes": [k, UNIFORME3], "poids": [0.8, 0.2]},
            "F3-melee-aveugle": {"type": "melange", "composantes": [k, AVEUGLE3], "poids": [0.8, 0.2]},
            "F4-temperee-inclinee": {"type": "transformee", "base": k, "puissance": 1.2, "inclinaison": [0.0, 0.05, -0.05]}}


def jeu_plante_mr1(spec, oracle, dilutions=(0.03, 0.05)):
    """Règle du jeu planté, dérivée par programme du monde (gelée avant l'appel à Kimi) : K1 ; vraies : le monde, « K1 + un
    effet » calibrée pour chaque autre effet, deux mélanges du monde et de K1 au gain visé ; fausses couvertes F1 à F4."""
    k1, eid, infos = k1_du_monde(spec, oracle)
    classes = {e["id"]: e.get("classe") for e in spec["effets"]}
    W = compiler_monde(spec)
    vraies = {"V-monde": {"loi": W, "effets": sorted(classes), "classe": "forte"}}
    for e in spec["effets"]:
        if e["id"] != eid:
            vraies[f"V-K1+{e['id']}"] = {"loi": calibrer(monde_restreint(spec, [eid, e["id"]]), oracle),
                                         "effets": sorted([eid, e["id"]]), "classe": classes[e["id"]]}
    for c in dilutions:
        vraies[f"V-dilue-{c}"] = {"loi": diluer(W, k1, oracle, c), "effets": None, "classe": f"dilution {c}"}
    return k1, eid, infos, vraies, fausses_couvertes(k1)
