"""Bras comparés (v1), tels que fixés par le préenregistrement `preenregistrement-trancher-recombinaison-v1.md`.

Chaque bras rend une suite d'au plus BUDGET paires distinctes, prises parmi les paires valides du monde (l'étage
commun « opérateur choisi après tirage + filtre de compatibilité » est appliqué par monde_v1 : `valides`).
Une loi tirée sans remise parmi les paires valides équivaut à « tirer, passer l'étage commun, recommencer si rejet
ou déjà acceptée ». Bibliothèque standard ; chaque bras aléatoire a sa graine random.Random(f"{graine}-{bras}").
"""
import math
import random
from collections import Counter

K_PAR_GENERATION, GENERATIONS = 4, 3
BUDGET = K_PAR_GENERATION * GENERATIONS
GAMMA_CORRECTIF = 1e-3


def tirer_sans_remise(rng, items, poids, nombre):
    """Tirage séquentiel pondéré sans remise (poids nuls jamais tirés)."""
    items = [x for x, w in zip(items, poids) if w > 0]
    poids = [w for w in poids if w > 0]
    choisis = []
    while items and len(choisis) < nombre:
        u, acc, idx = rng.random() * sum(poids), 0.0, len(items) - 1
        for k, w in enumerate(poids):
            acc += w
            if u < acc:
                idx = k
                break
        choisis.append(items.pop(idx))
        poids.pop(idx)
    return choisis


# --- (a) forme corrigée et ses diagnostics --------------------------------------------------------

def ordre_glouton(monde, q):
    """Ordre glouton complet du déterminant maximal, L = diag(q)(S + gamma I)diag(q), S = cos², par Cholesky
    incrémentale (Chen et al. 2018, comme commun_v1.glouton_cholesky ; départage au premier indice)."""
    n, cos = monde["n"], monde["cos"]
    l = [[q[i] * q[j] * (cos[i][j] ** 2 + (GAMMA_CORRECTIF if i == j else 0.0)) for j in range(n)] for i in range(n)]
    d2 = [l[i][i] for i in range(n)]
    lignes, ordre, pris = [], [], set()
    j = max(range(n), key=lambda i: d2[i])
    while True:
        ordre.append(j)
        pris.add(j)
        if len(ordre) == n:
            return ordre
        dj = math.sqrt(max(d2[j], 1e-300))
        e = [(l[j][i] - sum(c[j] * c[i] for c in lignes)) / dj for i in range(n)]
        lignes.append(e)
        for i in range(n):
            d2[i] -= e[i] ** 2
        j = max((i for i in range(n) if i not in pris), key=lambda i: d2[i])


def corrige(monde, q):
    rang = {a: r for r, a in enumerate(ordre_glouton(monde, q))}
    paires = monde["paires"]
    cle = lambda x: (max(rang[paires[x]["i"]], rang[paires[x]["j"]]), rang[paires[x]["i"]] + rang[paires[x]["j"]])
    return sorted(monde["valides"], key=cle)[:BUDGET]


def dpp_paires(monde, rng):
    """Diagnostic : processus déterminantal exact à 2 éléments avec le noyau corrigé, P ∝ det L_{ij}."""
    arts, paires, cos = monde["arts"], monde["paires"], monde["cos"]
    poids = []
    for x in monde["valides"]:
        i, j = paires[x]["i"], paires[x]["j"]
        poids.append(arts[i]["q"] ** 2 * arts[j]["q"] ** 2 * ((1 + GAMMA_CORRECTIF) ** 2 - cos[i][j] ** 4))
    return tirer_sans_remise(rng, monde["valides"], poids, BUDGET)


# --- (b) tirage stratifié, (c) uniforme, (b_eloigne) diagnostic ---------------------------------------

def _strates(monde):
    arts, paires, strates = monde["arts"], monde["paires"], {}
    for x in monde["valides"]:
        cle = tuple(sorted((arts[paires[x]["i"]]["dom_obs"], arts[paires[x]["j"]]["dom_obs"])))
        strates.setdefault(cle, []).append(x)
    return strates


def _tour_des_strates(rng, strates, ordre_paliers, sortie):
    for palier in ordre_paliers:
        actives = sorted(s for s in palier if strates.get(s))
        while actives and len(sortie) < BUDGET:
            tour = list(actives)
            rng.shuffle(tour)
            for s in tour:
                if len(sortie) >= BUDGET:
                    break
                sortie.append(strates[s].pop(rng.randrange(len(strates[s]))))
            actives = [s for s in actives if strates[s]]
    return sortie


def stratifie(monde, rng):
    strates = _strates(monde)
    return _tour_des_strates(rng, strates, [list(strates)], [])


def stratifie_eloigne(monde, rng):
    """Diagnostic : strates de cosinus moyen (entre domaines observés) <= médiane servies d'abord."""
    arts, cos, n = monde["arts"], monde["cos"], monde["n"]
    somme = Counter()
    nombre = Counter()
    for i in range(n):
        for j in range(i + 1, n):
            a, b = arts[i]["dom_obs"], arts[j]["dom_obs"]
            if a != b:
                cle = tuple(sorted((a, b)))
                somme[cle] += cos[i][j]
                nombre[cle] += 1
    moyenne = {s: somme[s] / nombre[s] for s in nombre}
    valeurs = sorted(moyenne.values())
    mediane = valeurs[len(valeurs) // 2] if len(valeurs) % 2 else 0.5 * (valeurs[len(valeurs) // 2 - 1] + valeurs[len(valeurs) // 2])
    strates = _strates(monde)
    loin = [s for s in strates if moyenne.get(s, 0.0) <= mediane]
    pres = [s for s in strates if moyenne.get(s, 0.0) > mediane]
    return _tour_des_strates(rng, strates, [loin, pres], [])


def uniforme(monde, rng):
    return rng.sample(monde["valides"], min(BUDGET, len(monde["valides"])))


# --- (d1) marche de Swanson, (d2) structure de cooccurrences étiquette x domaine ------------------------

def marche_swanson(monde, rng, df, ponderation="idf"):
    """Loi exacte de la marche ancre -> étiquette (∝ poids de rareté) -> porteur d'un autre domaine observé."""
    arts, paires, n = monde["arts"], monde["paires"], monde["n"]
    etiq = [set(a["etiquettes"]) for a in arts]
    ancres = [i for i in range(n) if etiq[i]]
    if not ancres:
        return []
    porteurs = {}
    for i in range(n):
        for m in etiq[i]:
            porteurs.setdefault(m, []).append(i)
    poids_m = (lambda m: math.log(n / df[m])) if ponderation == "idf" else (lambda m: 1.0 / df[m])
    index = {(paires[x]["i"], paires[x]["j"]): x for x in monde["valides"]}
    proba = Counter()
    for a in ancres:
        total = sum(poids_m(m) for m in etiq[a])
        for m in etiq[a]:
            pm = poids_m(m) / total if total > 0 else 1.0 / len(etiq[a])
            arrivees = [b for b in porteurs[m] if b != a and arts[b]["dom_obs"] != arts[a]["dom_obs"]]
            for b in arrivees:
                x = index.get((min(a, b), max(a, b)))
                if x is not None:
                    proba[x] += pm / (len(ancres) * len(arrivees))
    valides = monde["valides"]
    return tirer_sans_remise(rng, valides, [proba[x] for x in valides], BUDGET)


def contraste_import(monde, rng):
    """Score = max sur les étiquettes partagées de |f(m | domaine_i) - f(m | domaine_j)| (signature d'un import)."""
    arts, paires = monde["arts"], monde["paires"]
    if not any(a["etiquettes"] for a in arts):
        return []
    n_dom = Counter(a["dom_obs"] for a in arts)
    porte = Counter((a["dom_obs"], m) for a in arts for m in a["etiquettes"])
    f = lambda m, d: porte[(d, m)] / n_dom[d]
    score, alea = {}, {}
    for x in monde["valides"]:
        di, dj = arts[paires[x]["i"]]["dom_obs"], arts[paires[x]["j"]]["dom_obs"]
        score[x] = max((abs(f(m, di) - f(m, dj)) for m in paires[x]["partage"]), default=0.0)
        alea[x] = rng.random()
    return sorted(monde["valides"], key=lambda x: (-score[x], alea[x]))[:BUDGET]


# --- (e) forme du rapport de Gemini, réparée pour tourner ----------------------------------------------

def sinkhorn_knopp(a, iterations=5):
    """Comme commun_v1.sinkhorn_knopp : version symétrique D A D, ou None si une somme devient non positive."""
    n = len(a)
    r, c = [1.0] * n, [1.0] * n
    for _ in range(iterations):
        ac = [sum(a[i][j] * c[j] for j in range(n)) for i in range(n)]
        if any(v <= 0 for v in ac):
            return None
        r = [1.0 / v for v in ac]
        atr = [sum(a[i][j] * r[i] for i in range(n)) for j in range(n)]
        if any(v <= 0 for v in atr):
            return None
        c = [1.0 / v for v in atr]
    d = [math.sqrt(r[i] * c[i]) for i in range(n)]
    return [[d[i] * a[i][j] * d[j] for j in range(n)] for i in range(n)]


def _cholesky_reussit(m, gamma):
    n = len(m)
    l = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = m[i][j] + (gamma if i == j else 0.0) - sum(l[i][k] * l[j][k] for k in range(j))
            if i == j:
                if s <= 0:
                    return False
                l[i][i] = math.sqrt(s)
            else:
                l[i][j] = s / l[j][j]
    return True


def gamma_minimal(m, iterations=30):
    """Plus petit gamma rendant m + gamma I semi-définie positive (bissection par Cholesky, précision relative 2^-30)."""
    n = len(m)
    bas = max((abs(m[i][j]) for i in range(n) for j in range(n) if i != j), default=0.0) - max(m[i][i] for i in range(n))
    bas = max(bas, 0.0)
    haut = max(sum(abs(m[i][j]) for j in range(n) if j != i) - m[i][i] for i in range(n)) + 1e-12
    for _ in range(iterations):
        milieu = 0.5 * (bas + haut)
        if _cholesky_reussit(m, milieu + 1e-12):
            haut = milieu
        else:
            bas = milieu
    return haut


def rapport_gemini(monde, rng):
    arts, paires, cos, n = monde["arts"], monde["paires"], monde["cos"], monde["n"]
    etiq = [set(a["etiquettes"]) for a in arts]
    q = [a["q"] for a in arts]

    def g(i, j):
        return len(etiq[i] & etiq[j]) / math.sqrt(len(etiq[i]) * len(etiq[j])) if etiq[i] and etiq[j] else 0.0

    l = [[q[i] * q[j] * g(i, j) ** 2 * (1.0 - cos[i][j] ** 2) for j in range(n)] for i in range(n)]
    actifs = [i for i in range(n) if any(l[i][j] > 0 for j in range(n) if j != i)]
    if len(actifs) < 2:
        return [], None
    sous = [[l[i][j] for j in actifs] for i in actifs]
    m = sinkhorn_knopp(sous)
    if m is None:
        return [], None
    gamma = gamma_minimal(m) + 1e-9
    pos = {a: k for k, a in enumerate(actifs)}
    poids = []
    for x in monde["valides"]:
        i, j = paires[x]["i"], paires[x]["j"]
        if i in pos and j in pos:
            a, b = pos[i], pos[j]
            poids.append(max(0.0, (m[a][a] + gamma) * (m[b][b] + gamma) - m[a][b] ** 2))
        else:
            poids.append(0.0)
    return tirer_sans_remise(rng, monde["valides"], poids, BUDGET), gamma


# --- plafond ------------------------------------------------------------------------------------------

def oracle(monde, rng):
    vrais = [x for x in monde["valides"] if x in monde["vrais"]]
    autres = [x for x in monde["valides"] if x not in monde["vrais"]]
    rng.shuffle(vrais)
    rng.shuffle(autres)
    return (vrais + autres)[:BUDGET]


BRAS = ["a_corrige", "b_stratifie", "c_uniforme", "d1_marche_swanson", "d2_contraste_import", "e_rapport_gemini",
        "a_2dpp", "a_q1", "b_eloigne", "d1_inv", "oracle"]


def executer(monde, df):
    """Rend {bras: suite de paires} et le gamma de la forme du rapport (None si elle ne tourne pas)."""
    g = monde["graine"]
    rng = lambda nom: random.Random(f"{g}-{nom}")
    q = [a["q"] for a in monde["arts"]]
    sortie_e, gamma_e = rapport_gemini(monde, rng("e_rapport_gemini"))
    return {
        "a_corrige": corrige(monde, q),
        "b_stratifie": stratifie(monde, rng("b_stratifie")),
        "c_uniforme": uniforme(monde, rng("c_uniforme")),
        "d1_marche_swanson": marche_swanson(monde, rng("d1_marche_swanson"), df, "idf"),
        "d2_contraste_import": contraste_import(monde, rng("d2_contraste_import")),
        "e_rapport_gemini": sortie_e,
        "a_2dpp": dpp_paires(monde, rng("a_2dpp")),
        "a_q1": corrige(monde, [1.0] * monde["n"]),
        "b_eloigne": stratifie_eloigne(monde, rng("b_eloigne")),
        "d1_inv": marche_swanson(monde, rng("d1_inv"), df, "inverse"),
        "oracle": oracle(monde, rng("oracle")),
    }, gamma_e
