"""Bras de l'expérience v2 (§ 3, § 4, § 4 bis du préenregistrement scellé, e821e875…).

Chaque bras est une fonction (obs, rng, aux) -> liste d'au plus BUDGET indices de paires valides distinctes.
`obs` est la vue observée (monde_v2.Obs) ; `rng` un numpy.random.Generator issu de la SeedSequence
(code_condition, indice_monde, 10 + rang du bras) ; `aux` porte les permutations des placebos et les
hyperparamètres de N_grille. Aucun bras ne lit un champ latent (balayage statique : essais/essais_gardes_v2.py) ;
aucun `try` ni `except` dans ce module. L'oracle, qui lit la vérité, n'est pas ici : il est dans mesures_v2.py.
"""
import math

import numpy as np

from controle_ia.gardes import GardeArret

import noyaux_v2 as ny

BUDGET = 12
E_PRIORI, BETA_PRIORI, EPSILON = 8.5, 1.0, 0.05     # § 5, défauts D-c et D-d confirmés (R-580)
GAMMA = ny.GAMMA
PHI = 4                                              # S16f
TOLERANCE_KAPPA = 1e-9

ORDRE_BRAS = ["N", "b", "a", "d1", "d1c", "c", "b_eloigne", "oracle", "N_beta0", "N_alpha0", "N_filtre", "N_aleat",
              "N_global", "N_dpp", "N_dpp_beta0", "N_fiches", "N_q", "N_rare", "N_PC", "N_PCg", "N_grille"]
RANG = {b: r for r, b in enumerate(ORDRE_BRAS)}


# --- quantités du candidat (§ 3) ----------------------------------------------------------------------------

def vecteurs_concepts(obs):
    """Vecteurs de concepts observés, poids log(n / df), norme 1 ; vecteur nul déclaré et compté (jamais NaN)."""
    labels = sorted({l for e in obs.etiq_co for l in e})
    pos = {l: k for k, l in enumerate(labels)}
    v = np.zeros((obs.n, max(1, len(labels))))
    for i, e in enumerate(obs.etiq_co):
        for l in e:
            v[i, pos[l]] = math.log(obs.n / obs.df[l])
    normes = np.sqrt((v ** 2).sum(axis=1))
    nuls = normes == 0
    v[~nuls] = v[~nuls] / normes[~nuls, None]
    return v, int(nuls.sum())


def kappa(v):
    k = v @ v.T
    if np.isnan(k).any() or k.min() < -TOLERANCE_KAPPA or k.max() > 1 + TOLERANCE_KAPPA:
        raise GardeArret(f"κ hors [0, 1] ou NaN (min {np.nanmin(k):.3e}, max {np.nanmax(k):.3e})")
    return np.clip(k, 0.0, 1.0)


def scores(obs, e, beta, kap, avec_q=False):
    """s_ij = (1 − cos²)^e × (κ + ε)^β × [q_i q_j], sur toutes les paires (matrice n × n)."""
    cos = obs.cos
    s = np.power(np.clip(1.0 - cos ** 2, 0.0, None), e) * np.power(kap + EPSILON, beta)
    if avec_q:
        q = np.asarray(obs.q)
        s = s * np.outer(q, q)
    if not np.isfinite(s).all():
        raise GardeArret("NaN ou infini dans un score")
    return s


def strate(obs, x):
    i, j = obs.paires[x]
    return tuple(sorted((obs.dom_obs[i], obs.dom_obs[j])))


def _strates(obs, paires=None):
    st = {}
    for x in (obs.valides if paires is None else paires):
        st.setdefault(strate(obs, x), []).append(x)
    return st


# --- algorithme de N (§ 4, CB-06) ---------------------------------------------------------------------------

def tour_par_score(obs, s, rng, ordre_aleatoire=False):
    """Passages sur les strates ; score de strate = plus fort s_ij restant ; une paire par strate et par passage ;
    égalités tirées par la graine du bras ; scores recalculés à chaque passage."""
    sx = {x: s[obs.paires[x]] for x in obs.valides}
    restantes = _strates(obs)
    sortie = []
    while len(sortie) < BUDGET:
        actives = sorted(k for k, v in restantes.items() if v)
        if not actives:
            break
        if ordre_aleatoire:
            ordre = [actives[int(i)] for i in rng.permutation(len(actives))]
        else:
            u = rng.random(len(actives))
            ordre = [k for _, _, k in sorted(((-max(sx[x] for x in restantes[k]), u[t], k)
                                               for t, k in enumerate(actives)), key=lambda z: (z[0], z[1]))]
        for k in ordre:
            if len(sortie) >= BUDGET:
                break
            meilleur = max(sx[x] for x in restantes[k])
            ex = [x for x in restantes[k] if sx[x] == meilleur]
            x = ex[int(rng.integers(len(ex)))] if len(ex) > 1 else ex[0]
            restantes[k].remove(x)
            sortie.append(x)
    return sortie


def _famille_N(obs, rng, e, beta, avec_q=False, perm=None, kap_remplace=None):
    v, nuls = vecteurs_concepts(obs)
    if perm is not None:
        v = v[np.asarray(perm)]
    kap = kappa(v) if kap_remplace is None else kap_remplace
    return tour_par_score(obs, scores(obs, e, beta, kap, avec_q), rng), nuls


def bras_N(obs, rng, aux):
    return _famille_N(obs, rng, E_PRIORI, BETA_PRIORI)[0]


def bras_N_beta0(obs, rng, aux):
    return _famille_N(obs, rng, E_PRIORI, 0.0)[0]


def bras_N_alpha0(obs, rng, aux):
    return _famille_N(obs, rng, 0.0, BETA_PRIORI)[0]


def bras_N_q(obs, rng, aux):
    return _famille_N(obs, rng, E_PRIORI, BETA_PRIORI, avec_q=True)[0]


def bras_N_PC(obs, rng, aux):
    return _famille_N(obs, rng, E_PRIORI, BETA_PRIORI, perm=aux["perm_PC"])[0]


def bras_N_PCg(obs, rng, aux):
    return _famille_N(obs, rng, E_PRIORI, BETA_PRIORI, perm=aux["perm_PCg"])[0]


def bras_N_grille(obs, rng, aux):
    e, beta = aux["grille_e_beta"]
    return _famille_N(obs, rng, e, beta)[0]


def bras_N_rare(obs, rng, aux):
    """κ remplacé par la rareté de l'étiquette partagée la plus rare (pont de l'étage commun) :
    log(40 / fréquence) / log(20), pour les paires valides ; 0 ailleurs (jamais tirées)."""
    r = np.zeros((obs.n, obs.n))
    for x in obs.valides:
        i, j = obs.paires[x]
        r[i, j] = r[j, i] = math.log(obs.n / obs.df[obs.pont[x]]) / math.log(20)
    return tour_par_score(obs, scores(obs, E_PRIORI, BETA_PRIORI, r), rng)


def bras_N_aleat(obs, rng, aux):
    v, _ = vecteurs_concepts(obs)
    return tour_par_score(obs, scores(obs, E_PRIORI, BETA_PRIORI, kappa(v)), rng, ordre_aleatoire=True)


def bras_N_global(obs, rng, aux):
    v, _ = vecteurs_concepts(obs)
    s = scores(obs, E_PRIORI, BETA_PRIORI, kappa(v))
    u = rng.random(len(obs.valides))
    cle = sorted(((-s[obs.paires[x]], u[t], x) for t, x in enumerate(obs.valides)), key=lambda z: (z[0], z[1]))
    return [x for _, _, x in cle[:BUDGET]]


# --- placebos de concepts (§ 4 bis) ---------------------------------------------------------------------------

def placebo_permutation(obs, rng, portee):
    """Permutation des vecteurs de concepts entre articles : « domaine » (même domaine observé ; N_PC, rôle 4)
    ou « global » (tous les articles ; N_PCg, rôle 6). L'article i reçoit le vecteur de perm[i]."""
    perm = np.arange(obs.n)
    if portee == "global":
        return rng.permutation(obs.n)
    if portee != "domaine":
        raise GardeArret(f"portée de placebo inconnue : {portee}")
    for d in sorted(set(obs.dom_obs)):
        membres = np.array([i for i in range(obs.n) if obs.dom_obs[i] == d])
        perm[membres] = membres[rng.permutation(len(membres))]
    return perm


# --- témoins de v1 (b, b_eloigne, c, d1, a) et d1c --------------------------------------------------------

def tour_des_strates(rng, strates, ordre_paliers, sortie):
    """methodes_v1._tour_des_strates, servi par un numpy.random.Generator."""
    for palier in ordre_paliers:
        actives = sorted(s for s in palier if strates.get(s))
        while actives and len(sortie) < BUDGET:
            tour = list(actives)
            tour = [tour[int(i)] for i in rng.permutation(len(tour))]
            for s in tour:
                if len(sortie) >= BUDGET:
                    break
                sortie.append(strates[s].pop(int(rng.integers(len(strates[s])))))
            actives = [s for s in actives if strates[s]]
    return sortie


def bras_b(obs, rng, aux):
    st = _strates(obs)
    return tour_des_strates(rng, st, [list(st)], [])


def cos_moyen_strates(obs):
    somme, nombre = {}, {}
    for i in range(obs.n):
        for j in range(i + 1, obs.n):
            a, b = obs.dom_obs[i], obs.dom_obs[j]
            if a != b:
                k = tuple(sorted((a, b)))
                somme[k] = somme.get(k, 0.0) + float(obs.cos[i, j])
                nombre[k] = nombre.get(k, 0) + 1
    moyenne = {k: somme[k] / nombre[k] for k in nombre}
    valeurs = sorted(moyenne.values())
    h = len(valeurs)
    mediane = valeurs[h // 2] if h % 2 else 0.5 * (valeurs[h // 2 - 1] + valeurs[h // 2])
    return moyenne, mediane


def bras_b_eloigne(obs, rng, aux):
    moyenne, mediane = cos_moyen_strates(obs)
    st = _strates(obs)
    loin = [s for s in st if moyenne.get(s, 0.0) <= mediane]
    pres = [s for s in st if moyenne.get(s, 0.0) > mediane]
    return tour_des_strates(rng, st, [loin, pres], [])


def bras_c(obs, rng, aux):
    k = min(BUDGET, len(obs.valides))
    return [obs.valides[int(i)] for i in rng.choice(len(obs.valides), size=k, replace=False)]


def tirer_sans_remise(rng, items, poids, nombre):
    """methodes_v1.tirer_sans_remise, servi par un numpy.random.Generator."""
    items = [x for x, w in zip(items, poids) if w > 0]
    poids = [w for w in poids if w > 0]
    choisis = []
    while items and len(choisis) < nombre:
        u, acc, idx = float(rng.random()) * sum(poids), 0.0, len(items) - 1
        for k, w in enumerate(poids):
            acc += w
            if u < acc:
                idx = k
                break
        choisis.append(items.pop(idx))
        poids.pop(idx)
    return choisis


def marche_swanson(obs, rng, etiquettes):
    """Loi exacte de methodes_v1.marche_swanson (poids idf) sur un jeu d'étiquettes observées."""
    n = obs.n
    etiq = [set(e) for e in etiquettes]
    ancres = [i for i in range(n) if etiq[i]]
    if not ancres:
        return []
    porteurs = {}
    for i in range(n):
        for m in etiq[i]:
            porteurs.setdefault(m, []).append(i)
    poids_m = lambda m: math.log(n / obs.df[m])
    index = {obs.paires[x]: x for x in obs.valides}
    proba = {}
    for a in ancres:
        total = sum(poids_m(m) for m in etiq[a])
        for m in sorted(etiq[a]):
            pm = poids_m(m) / total if total > 0 else 1.0 / len(etiq[a])
            arrivees = [b for b in porteurs[m] if b != a and obs.dom_obs[b] != obs.dom_obs[a]]
            for b in arrivees:
                x = index.get((min(a, b), max(a, b)))
                if x is not None:
                    proba[x] = proba.get(x, 0.0) + pm / (len(ancres) * len(arrivees))
    return tirer_sans_remise(rng, list(obs.valides), [proba.get(x, 0.0) for x in obs.valides], BUDGET)


def bras_d1(obs, rng, aux):
    return marche_swanson(obs, rng, obs.etiq_op)


def bras_d1c(obs, rng, aux):
    """Non applicable dans NR et V_concepts_absents : exclu d'avance par mesures_v2.NON_APPLICABLES, jamais exécuté
    (la vue observée ne porte plus d'indicateur de condition, CLA-09)."""
    return marche_swanson(obs, rng, obs.etiq_co)


def corrige_par_ordre(obs, ordre):
    rang = {a: r for r, a in enumerate(ordre)}
    cle = lambda x: (max(rang[obs.paires[x][0]], rang[obs.paires[x][1]]), rang[obs.paires[x][0]] + rang[obs.paires[x][1]])
    return sorted(obs.valides, key=cle)[:BUDGET]


def bras_a(obs, rng, aux):
    """Forme corrigée v6.3 (corrige, avec q) par la copie gardée de ordre_glouton."""
    cos = obs.cos.tolist()
    return corrige_par_ordre(obs, ny.ordre_glouton_garde(ny.noyau_v1(cos, list(obs.q))))


def bras_N_fiches(obs, rng, aux):
    """Noyau sur les fiches S_ij = cos_ij² κ_ij², q ≡ 1, + γ I ; même chaîne que (a)."""
    v, _ = vecteurs_concepts(obs)
    kap = kappa(v)
    s = (obs.cos ** 2) * (kap ** 2)
    s = 0.5 * (s + s.T)
    l = (s + GAMMA * np.eye(obs.n)).tolist()
    return corrige_par_ordre(obs, ny.ordre_glouton_garde(l))


# --- N_filtre renforcé (CB2-03) -----------------------------------------------------------------------------

def paliers_filtre(obs):
    moyenne, mediane = cos_moyen_strates(obs)
    v, _ = vecteurs_concepts(obs)
    kap = kappa(v)
    p1, p2, p3 = [], [], []
    for x in obs.valides:
        i, j = obs.paires[x]
        loin = moyenne.get(strate(obs, x), 0.0) <= mediane
        partage_co = obs.etiq_co[i] & obs.etiq_co[j]
        if loin and partage_co and min(obs.df[m] for m in partage_co) <= PHI:
            p1.append(x)
        elif loin and kap[i, j] > 0:
            p2.append(x)
        else:
            p3.append(x)
    return p1, p2, p3


def bras_N_filtre(obs, rng, aux):
    """Tour stratifié servi par paliers ; le nombre de paires prises à chaque palier est rapporté (aux)."""
    sortie, compte = [], []
    for palier in paliers_filtre(obs):
        avant = len(sortie)
        st = _strates(obs, palier)
        tour_des_strates(rng, st, [list(st)], sortie)
        compte.append(len(sortie) - avant)
    aux.setdefault("rapport", {})["N_filtre_paliers"] = compte
    return sortie


# --- N_dpp, N_dpp_beta0 (forme O3) ----------------------------------------------------------------------

def noyau_paires(obs, beta0=False):
    v, _ = vecteurs_concepts(obs)
    kap = kappa(v)
    s_mat = scores(obs, E_PRIORI, 0.0 if beta0 else BETA_PRIORI, kap)
    P = np.array([obs.paires[x] for x in obs.valides])
    I, J = P[:, 0], P[:, 1]
    C = np.asarray(obs.cos)
    cij = C[I, J]
    sd = (C[np.ix_(I, I)] * C[np.ix_(J, J)] + C[np.ix_(I, J)] * C[np.ix_(J, I)])
    sd = sd / np.sqrt(np.outer(1 + cij ** 2, 1 + cij ** 2))
    if beta0:
        sc = np.ones_like(sd)
    else:
        psi = v[I] * v[J]
        normes = np.sqrt((psi ** 2).sum(axis=1))
        sans = normes == 0
        psi[~sans] = psi[~sans] / normes[~sans, None]
        sc = psi @ psi.T
        idx = np.flatnonzero(sans)
        sc[idx, :] = 0.0
        sc[:, idx] = 0.0
        sc[idx, idx] = 1.0  # vecteur propre à la paire si elle ne partage aucun concept
    qual = s_mat[I, J]
    racine = np.sqrt(qual)
    L = racine[:, None] * (sd * sc) * racine[None, :]
    L = 0.5 * (L + L.T) + GAMMA * np.eye(len(I))
    return L


def bras_N_dpp(obs, rng, aux):
    choisis, non_pos = ny.glouton_paires(noyau_paires(obs), BUDGET)
    aux.setdefault("rapport", {})["N_dpp_pivots_non_positifs"] = non_pos
    return [obs.valides[k] for k in choisis]


def bras_N_dpp_beta0(obs, rng, aux):
    choisis, non_pos = ny.glouton_paires(noyau_paires(obs, beta0=True), BUDGET)
    aux.setdefault("rapport", {})["N_dpp_beta0_pivots_non_positifs"] = non_pos
    return [obs.valides[k] for k in choisis]


FONCTIONS = {
    "N": bras_N, "b": bras_b, "a": bras_a, "d1": bras_d1, "d1c": bras_d1c, "c": bras_c, "b_eloigne": bras_b_eloigne,
    "N_beta0": bras_N_beta0, "N_alpha0": bras_N_alpha0, "N_filtre": bras_N_filtre, "N_aleat": bras_N_aleat,
    "N_global": bras_N_global, "N_dpp": bras_N_dpp, "N_dpp_beta0": bras_N_dpp_beta0, "N_fiches": bras_N_fiches,
    "N_q": bras_N_q, "N_rare": bras_N_rare, "N_PC": bras_N_PC, "N_PCg": bras_N_PCg, "N_grille": bras_N_grille,
}
