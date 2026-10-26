"""Outils textuels de la brique 3 : jetons de l'organisme, listes d'arrêt, corpus de ponts, remèdes.

Jetons : même expression que mitose_spectrale.calculer_capacite_shannon_gram, [a-zA-Z0-9_]{3,} sur le
texte en minuscules (ASCII seulement : un mot accentué est coupé en fragments, « bilinéaire » -> « bilin », « aire »).
"""
import math
import re
from collections import Counter
from itertools import combinations

import numpy as np

MOTIF = re.compile(r"[a-zA-Z0-9_]{3,}")

ARRET_FR = """
les des une uns est dans pour par sur aux avec que qui quoi pas plus moins son ses sont ces cet cette mais donc
comme entre sans sous leur leurs elle elles ils nous vous tout tous toute toutes aussi ainsi alors dont peut
peuvent fait faire font cela ceci celle celles celui ceux car chaque selon vers chez lors lorsque lorsqu puis
quand quel quelle quels quelles etre tre avoir ont notre nos votre vos mon mes ton tes lui eux soit sera seront
serait via non oui tant tandis trop tres bien encore jamais toujours souvent ici ensuite enfin parce pourquoi
comment doit doivent peu autre autres meme galement apr contre depuis pendant avant afin certains certaines
plusieurs aucun aucune chacun rien sinon cependant toutefois notamment partir sein outre tel telle tels telles
qu une ceux voici voila deux trois ont avait avaient sommes etes
""".split()
ARRET_EN = """
the and for with that this are from which not can has have had was were its but all also than these those such
into between using based each may more most our their there they them then thus when where while both other only
over under how what who whom why will would should could been being does did doing any some many much very same
own out off about above below after before again further once here nor too you your his her him she itself per
upon within without across among however therefore hence whether because since until although though yet still
even just like one two use used
""".split()
ARRET = frozenset(ARRET_FR) | frozenset(ARRET_EN)


def jetons(texte: str) -> list:
    return MOTIF.findall(str(texte).lower())


def est_arret(tok: str) -> bool:
    return tok in ARRET or tok.isdigit()


def seuil_saturation(n: int) -> int:
    return max(2, int(0.75 * n))


def frequences_document(docs: list) -> Counter:
    df = Counter()
    for d in docs:
        for t in set(d):
            df[t] += 1
    return df


def satures_depuis_df(df: Counter, n: int, plafond: int = 6, exclus=frozenset()) -> list:
    """Même règle que l'organisme : df >= max(2, int(0,75 n)), tri (-df, jeton), 6 premiers."""
    s = seuil_saturation(n)
    cands = sorted([(t, c) for t, c in df.items() if n > 1 and c >= s and t not in exclus], key=lambda kv: (-kv[1], kv[0]))
    return [t for t, _ in cands[:plafond]]


# --- Remèdes -----------------------------------------------------------------------------------

def remede_a(textes: list, capacite) -> list:
    """(a) Liste d'arrêt (français, anglais, jetons numériques) avant le compte, puis la fonction de l'organisme."""
    filtres = [" ".join(t for t in jetons(x) if not est_arret(t)) for x in textes]
    return capacite(filtres)["termes_satures"]


def _tfidf(docs: list, exclus: set):
    n = len(docs)
    df = frequences_document(docs)
    vocab = sorted(t for t in df if t not in exclus)
    pos = {t: i for i, t in enumerate(vocab)}
    x = np.zeros((n, len(vocab)))
    for i, d in enumerate(docs):
        for t, c in Counter(d).items():
            if t in pos:
                x[i, pos[t]] = c * math.log(1.0 + n / df[t])
    nrm = np.linalg.norm(x, axis=1, keepdims=True)
    nrm[nrm == 0] = 1.0
    return x / nrm


def bipartition(docs: list, exclus: set) -> np.ndarray:
    """Bissection spectrale (signe du vecteur de Fiedler, laplacien normalisé) de la similarité cosinus ;
    repli sur la médiane si un côté est vide."""
    x = _tfidf(docs, exclus)
    w = np.clip(x @ x.T, 0.0, None)
    np.fill_diagonal(w, 0.0)
    deg = w.sum(1)
    deg[deg == 0] = 1e-12
    dm = 1.0 / np.sqrt(deg)
    lap = np.eye(len(docs)) - dm[:, None] * w * dm[None, :]
    _, vec = np.linalg.eigh(lap)
    f = vec[:, 1] * dm
    g = (f > 0).astype(int)
    if g.min() == g.max():
        g = (f > np.median(f)).astype(int)
    return g


def contraste_groupes(x: np.ndarray, groupes: np.ndarray, colonne_exclue: int = None) -> float:
    """Contraste entre deux groupes de textes : 1 - (similarité cosinus moyenne entre groupes) /
    (similarité cosinus moyenne dans les groupes), la colonne du terme testé retirée puis les vecteurs
    renormalisés. Vaut environ 0 pour des textes d'un même sujet, environ 1 pour des domaines disjoints."""
    y = x.copy()
    if colonne_exclue is not None:
        y[:, colonne_exclue] = 0.0
    nrm = np.linalg.norm(y, axis=1, keepdims=True)
    nrm[nrm == 0] = 1.0
    y = y / nrm
    w = y @ y.T
    n = len(groupes)
    intra, inter = [], []
    for i in range(n):
        for j in range(i + 1, n):
            (intra if groupes[i] == groupes[j] else inter).append(w[i, j])
    if not intra or not inter or np.mean(intra) <= 0:
        return 0.0
    return float(np.clip(1.0 - np.mean(inter) / np.mean(intra), 0.0, 1.0))


def remede_b(textes: list, rho: float = 0.25, tau: float = 0.5, fond_df: dict = None, beta: float = 0.1) -> dict:
    """(b) Liste d'arrêt, puis exemption des ponts entre groupes contrastés. Groupes : bissection spectrale de la
    similarité cosinus (pondération de l'organisme, mots-outils retirés). Un candidat saturé t est exempté s'il est
    présent dans au moins rho des textes de chacun des deux groupes et si le contraste entre groupes, calculé sans
    la coordonnée de t, est >= tau. Variante (b+) si fond_df est fourni : exemption seulement si la fréquence
    documentaire de t dans un corpus de fond est <= beta (terme spécifique, pas un hub générique)."""
    docs = [[t for t in jetons(x) if not est_arret(t)] for x in textes]
    n = len(docs)
    df = frequences_document(docs)
    s = seuil_saturation(n)
    cands = {t for t, c in df.items() if n > 1 and c >= s}
    groupes = bipartition(docs, set())
    vocab = sorted(df)
    pos = {t: i for i, t in enumerate(vocab)}
    x = _tfidf(docs, set())
    ensembles = [set(d) for d in docs]
    exemptes, contrastes = set(), {}
    for t in sorted(cands):
        pres = [np.mean([t in ensembles[i] for i in range(n) if groupes[i] == g]) if np.any(groupes == g) else 0.0
                for g in (0, 1)]
        contrastes[t] = contraste_groupes(x, groupes, pos[t])
        if min(pres) >= rho and contrastes[t] >= tau:
            if fond_df is None or fond_df.get(t, 0.0) <= beta:
                exemptes.add(t)
    return {"termes_satures": satures_depuis_df(df, n, exclus=exemptes), "exemptes": sorted(exemptes),
            "contraste_global": contraste_groupes(x, groupes), "contrastes_candidats": contrastes,
            "groupes": groupes.tolist()}


def paires_cooccurrence(doc: list) -> set:
    v = sorted(set(doc))
    return set(combinations(v, 2))


def bigrammes(doc: list) -> set:
    return set(zip(doc[:-1], doc[1:]))


def remede_c(textes: list, mode: str = "cooccurrence", arret: bool = False, plafond: int = 6) -> dict:
    """(c) Répulsion sur les paires (nœuds du graphe de ligne) : paires présentes dans au moins
    max(2, int(0,75 n)) textes, tri (-df, paire), 6 premières. Coût : nombre de paires comptées."""
    docs = [[t for t in jetons(x) if not (arret and est_arret(t))] for x in textes]
    n = len(docs)
    df = Counter()
    comptees = 0
    for d in docs:
        ps = paires_cooccurrence(d) if mode == "cooccurrence" else bigrammes(d)
        comptees += len(ps)
        df.update(ps)
    s = seuil_saturation(n)
    cands = sorted([(p, c) for p, c in df.items() if n > 1 and c >= s], key=lambda kv: (-kv[1], kv[0]))
    return {"paires_saturees": [p for p, _ in cands[:plafond]], "paires_comptees": comptees,
            "paires_distinctes": len(df), "candidats": len(cands)}


def graphe_cooccurrence(docs: list) -> dict:
    voisins = {}
    for d in docs:
        v = sorted(set(d))
        for a, b in combinations(v, 2):
            voisins.setdefault(a, set()).add(b)
            voisins.setdefault(b, set()).add(a)
    return voisins


def aretes_graphe_de_ligne_par(voisins: dict, noeud: str, explicite: bool = True) -> int:
    """Arêtes du graphe de ligne passant par `noeud` : paires d'arêtes du graphe incidentes à ce nœud.
    Comptage explicite (énumération) si demandé, sinon C(d, 2)."""
    vs = sorted(voisins.get(noeud, ()))
    if not explicite:
        return len(vs) * (len(vs) - 1) // 2
    total = 0
    for _ in combinations(vs, 2):
        total += 1
    return total


# --- Corpus synthétiques de ponts ---------------------------------------------------------------

def pseudo_mots(rng, nombre: int, interdits: set, longueur=(5, 9)) -> list:
    lettres = np.array(list("abcdefghijklmnopqrstuvwxyz"))
    out, vus = [], set(interdits)
    while len(out) < nombre:
        m = "".join(rng.choice(lettres, size=int(rng.integers(longueur[0], longueur[1] + 1))))
        if m not in vus and not est_arret(m):
            vus.add(m)
            out.append(m)
    return out


MOTS_OUTILS_FREQUENTS = ["les", "des", "dans", "une", "est", "pour", "par", "sur", "aux", "que", "qui", "avec",
                         "plus", "sont", "pas", "the", "and", "entre", "cette", "ces"]


def corpus_ponts(rng, n: int, m_pivot: int, k_outils: int, pivot: str = "magnesium", hub: str = None,
                 p_hub: float = 0.9, taille_vocab: int = 60, longueur: int = 60, autres_outils: int = 20,
                 vocab=None):
    """n textes, moitié domaine A, moitié domaine C (vocabulaires disjoints, Zipf s = 1,1) ; le pivot est dans
    m_pivot textes répartis en alternance A/C ; k_outils mots-outils présents dans tous les textes ;
    autres_outils mots-outils présents chacun avec probabilité 0,5 ; hub éventuel avec probabilité p_hub."""
    if vocab is None:
        interdits = {pivot} | ({hub} if hub else set())
        vocab = pseudo_mots(rng, 2 * taille_vocab, interdits)
    va, vc = vocab[:taille_vocab], vocab[taille_vocab:2 * taille_vocab]
    poids = 1.0 / np.arange(1, taille_vocab + 1) ** 1.1
    poids /= poids.sum()
    n_a = (n + 1) // 2
    domaines = [0] * n_a + [1] * (n - n_a)
    ordre_a = list(rng.permutation(n_a))
    ordre_c = list(n_a + rng.permutation(n - n_a))
    alterne = []
    while ordre_a or ordre_c:
        if ordre_a:
            alterne.append(int(ordre_a.pop()))
        if ordre_c:
            alterne.append(int(ordre_c.pop()))
    avec_pivot = set(alterne[:m_pivot])
    reserve = ARRET_FR[: autres_outils + 40]
    fixes = MOTS_OUTILS_FREQUENTS[:k_outils]
    variables = [w for w in reserve if w not in fixes][:autres_outils] if k_outils > 0 else []
    textes = []
    for i in range(n):
        v = va if domaines[i] == 0 else vc
        mots = list(rng.choice(v, size=longueur, p=poids))
        mots += fixes
        mots += [w for w in variables if rng.random() < 0.5]
        if i in avec_pivot:
            mots.append(pivot)
        if hub and rng.random() < p_hub:
            mots.append(hub)
        rng.shuffle(mots)
        textes.append(" ".join(mots))
    return textes, domaines, sorted(avec_pivot)
