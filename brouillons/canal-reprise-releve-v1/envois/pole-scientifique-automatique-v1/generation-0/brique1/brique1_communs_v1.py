"""Outils communs des essais de la brique 1 (encodage et mémoire spectrale), version 1.

Bibliothèque standard seule. Chargé par chemin (importlib) depuis le pilote, pour rester
compatible avec `python3 -I` (le dossier du script n'est pas dans sys.path).
Le module de l'organisme est importé depuis la copie `organisme_copie/memoire_isvd.py`
(empreinte identique à `fournis/organisme/memoire_isvd.py`, vérifiée par le pilote).
Graines : `random.Random(graine)` (même générateur que `random.seed(graine)`, mais dédié),
graine dérivée par tâche de la graine maîtresse par SHA-256 (fonction `graine`).
"""
import bisect
import hashlib
import importlib.util
import math
import random
import re
from pathlib import Path

ICI = Path(__file__).resolve().parent
CHEMIN_COPIE = ICI / "organisme_copie" / "memoire_isvd.py"
DIM = 16
RANG = 6
MOTIF_JETON = r"[a-zA-Z0-9_\\]+"  # identique à memoire_isvd.extraire_vecteur_koopman
GRAINE_MAITRESSE = 20261026
CLASSES = ("lin", "sin", "car")  # i % 3 == 0 : v ; i % 3 == 1 : sin(v) ; i % 3 == 2 : v²


# ---------------------------------------------------------------- chargement et graines
def charger_module(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, str(chemin))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def instance_memoire(nom, encodeur=None, decomposeur=None):
    """Instance séparée du module de l'organisme ; encodeur ou décomposeur remplacés si demandé."""
    module = charger_module(nom, CHEMIN_COPIE)
    if encodeur is not None:
        module.extraire_vecteur_koopman = lambda texte, dim=DIM: encodeur(texte)
    if decomposeur is not None:
        module.decomposer_jacobi_symetrique = decomposeur
    return module


def graine(tache, *indices):
    texte = "|".join([str(GRAINE_MAITRESSE), tache] + [str(i) for i in indices])
    return int.from_bytes(hashlib.sha256(texte.encode("utf-8")).digest()[:8], "big")


# ---------------------------------------------------------------- vocabulaires synthétiques
FONCTION = ("the of and to in a is that for with as by on we this are be from an which at or can it "
            "our these not has have its their such also both between into under over than more").split()
METHODE = ("model method analysis data results approach propose based using new study problem performance "
           "framework show estimate bound theorem proof error optimal algorithm function distribution "
           "parameter structure linear nonlinear condition approximation").split()
DOMAINES = {
    "physique": ("quantum particle energy spin lattice thermodynamic phase transition magnetic hamiltonian "
                 "oscillator wave photon electron scattering cosmology gravity relativity plasma fluid turbulence "
                 "viscosity symmetry gauge boson fermion superconductivity crystal phonon laser optics diffraction "
                 "resonance damping momentum inertia torque pressure temperature heat radiation nucleus decay "
                 "isotope collision vacuum entanglement qubit hadron neutrino").split(),
    "biologie": ("protein gene cell enzyme receptor membrane neuron synapse mutation genome transcription pathway "
                 "tissue organism species evolution population fitness selection metabolism mitochondria ribosome "
                 "antibody antigen virus bacteria infection immune tumor cancer signaling kinase ligand binding "
                 "folding chromatin methylation embryo development stem differentiation hormone insulin glucose "
                 "lipid peptide plasmid microbiome cytokine apoptosis").split(),
    "apprentissage": ("network neural training gradient loss layer attention transformer embedding token classifier "
                      "regression dataset leaderboard accuracy overfitting regularization dropout convolution "
                      "recurrent reinforcement policy reward agent graph node edge cluster kernel feature encoder "
                      "decoder latent generative adversarial diffusion sampling inference retrieval prompt language "
                      "vision pretraining finetuning optimizer batch epoch validation scaling tokenizer").split(),
    "economie": ("market price demand supply equilibrium utility consumer firm labor wage inflation monetary fiscal "
                 "trade tariff growth capital investment interest bond stock portfolio risk volatility option "
                 "arbitrage hedging liquidity credit default bank auction mechanism incentive contract welfare tax "
                 "household income inequality poverty unemployment productivity innovation competition monopoly "
                 "subsidy pension exchange currency").split(),
    "mathematiques": ("martingale measure integral manifold topology homology cohomology sheaf category functor "
                      "morphism group ring module algebra operator eigenvalue matrix vector norm banach hilbert "
                      "sobolev convergence series limit derivative differential equation stochastic brownian markov "
                      "ergodic spectral variational convex polynomial prime combinatorics probability random "
                      "isomorphism symplectic geodesic curvature lemma conjecture invariant quotient fibration").split(),
}


class TirageZipf:
    """Tirage d'un mot selon une loi de Zipf d'exposant donné sur le rang dans la liste."""

    def __init__(self, mots, exposant=1.0):
        self.mots = list(mots)
        self.cumul = []
        total = 0.0
        for k in range(len(self.mots)):
            total += 1.0 / (k + 1) ** exposant
            self.cumul.append(total)
        self.total = total

    def tirer(self, rng):
        return self.mots[bisect.bisect_left(self.cumul, rng.random() * self.total)]


TIRAGES = {"fonction": TirageZipf(FONCTION), "methode": TirageZipf(METHODE)}
TIRAGES.update({d: TirageZipf(m) for d, m in DOMAINES.items()})


def verifier_vocabulaires():
    """Aucun mot partagé entre listes : le recouvrement ne passe que par p_commun et les textes ponts."""
    listes = {"fonction": FONCTION, "methode": METHODE}
    listes.update(DOMAINES)
    noms = sorted(listes)
    communs = {}
    for a in range(len(noms)):
        for b in range(a + 1, len(noms)):
            inter = set(listes[noms[a]]) & set(listes[noms[b]])
            if inter:
                communs[f"{noms[a]}/{noms[b]}"] = sorted(inter)
    tailles = {n: (len(listes[n]), len(set(listes[n]))) for n in noms}
    return communs, tailles


def flechir(mot):
    if mot.endswith(("s", "x", "ch", "sh")):
        return mot + "es"
    if mot.endswith("y") and len(mot) > 2 and mot[-2] not in "aeiou":
        return mot[:-1] + "ies"
    return mot + "s"


def generer_texte(rng, domaines_texte, n, p_fonction, p_methode, p_flexion=0.0):
    surface, lemmes = [], []
    for _ in range(n):
        u = rng.random()
        if u < p_fonction:
            mot, flechissable = TIRAGES["fonction"].tirer(rng), False
        elif u < p_fonction + p_methode:
            mot, flechissable = TIRAGES["methode"].tirer(rng), True
        else:
            mot, flechissable = TIRAGES[rng.choice(domaines_texte)].tirer(rng), True
        lemmes.append(mot)
        if flechissable and p_flexion > 0.0 and rng.random() < p_flexion:
            mot = flechir(mot)
        surface.append(mot)
    return " ".join(surface), lemmes


def generer_corpus(graine_corpus, n_textes, n_min, n_max, p_commun, p_pont=0.2, domaines=None,
                   p_flexion=0.0, poids_min=0.6, poids_max=0.9):
    """Corpus synthétique : p_commun = part des jetons tirés du vocabulaire partagé
    (2/3 mots-outils, 1/3 vocabulaire de méthode), le reste du ou des domaines du texte."""
    rng = random.Random(graine_corpus)
    domaines = list(domaines or DOMAINES.keys())
    p_fonction, p_methode = p_commun * 2.0 / 3.0, p_commun / 3.0
    textes = []
    for _ in range(n_textes):
        if len(domaines) > 1 and rng.random() < p_pont:
            dt = rng.sample(domaines, 2)
        else:
            dt = [rng.choice(domaines)]
        n = rng.randint(n_min, n_max)
        texte, lemmes = generer_texte(rng, dt, n, p_fonction, p_methode, p_flexion)
        textes.append({"texte": texte, "lemmes": lemmes, "domaines": dt, "n": n,
                       "poids": rng.uniform(poids_min, poids_max)})
    return textes


# ---------------------------------------------------------------- encodages
def jetons(texte):
    liste = re.findall(MOTIF_JETON, str(texte).lower())
    return liste if liste else [str(texte)]


_CACHE_HACHAGE = {}


def vecteur_jeton_sha256(jeton, dim=DIM):
    v = _CACHE_HACHAGE.get(jeton)
    if v is None:
        h = hashlib.sha256(jeton.encode("utf-8")).digest()
        v = [(h[i] / 127.5) - 1.0 for i in range(dim)]
        _CACHE_HACHAGE[jeton] = v
    return v


def base_sha256(liste_jetons, dim=DIM):
    """Somme des hachages par jeton, dans l'ordre des jetons (même arithmétique que l'organisme)."""
    base = [0.0] * dim
    for jeton in liste_jetons:
        v = vecteur_jeton_sha256(jeton, dim)
        for i in range(dim):
            base[i] += v[i]
    return base


def relever_normaliser(base):
    """Lignes 17 à 29 de memoire_isvd.py recopiées : [v, sin v, v²] puis norme 1 en sortie."""
    releve = [0.0] * len(base)
    for i, val in enumerate(base):
        if i % 3 == 0:
            releve[i] = val
        elif i % 3 == 1:
            releve[i] = math.sin(val)
        else:
            releve[i] = val * val
    norme = math.sqrt(sum(x * x for x in releve))
    if norme > 1e-12:
        return [x / norme for x in releve]
    releve[0] = 1.0
    return releve


def normer(v):
    n = math.sqrt(sum(x * x for x in v))
    return [x / n for x in v] if n > 1e-12 else list(v)


def encodeur_base_normee(texte):
    """Variante (ii) : base ramenée à norme 1 AVANT le relèvement (remède du rapport)."""
    return relever_normaliser(normer(base_sha256(jetons(texte))))


def encodeur_reimplante_i(texte):
    """Réimplantation de (i), pour vérifier l'égalité exacte avec la fonction de l'organisme."""
    return relever_normaliser(base_sha256(jetons(texte)))


def encodeur_nul(texte, dim=DIM):
    """Encodage sans information : direction aléatoire propre à chaque texte (graine = SHA-256 du texte)."""
    g = int.from_bytes(hashlib.sha256(("nul|" + str(texte)).encode("utf-8")).digest()[:8], "big")
    rng = random.Random(g)
    return normer([rng.gauss(0.0, 1.0) for _ in range(dim)])


def memoiser(encodeur):
    cache = {}

    def f(texte):
        v = cache.get(texte)
        if v is None:
            v = encodeur(texte)
            cache[texte] = v
        return v
    return f


# ---------------------------------------------------------------- algèbre
def produit_scalaire(a, b):
    return sum(x * y for x, y in zip(a, b))


def cosinus(a, b):
    na = math.sqrt(produit_scalaire(a, a))
    nb = math.sqrt(produit_scalaire(b, b))
    if na < 1e-15 or nb < 1e-15:
        return 0.0
    return produit_scalaire(a, b) / (na * nb)


def matrice_moment(vecteurs, poids, centrer=False):
    """Somme pondérée des produits extérieurs, autour de 0 ou de la moyenne pondérée."""
    d = len(vecteurs[0])
    total = sum(poids)
    mu = [sum(w * v[i] for v, w in zip(vecteurs, poids)) / total for i in range(d)]
    m = [[0.0] * d for _ in range(d)]
    for v, w in zip(vecteurs, poids):
        x = [v[i] - mu[i] for i in range(d)] if centrer else v
        for i in range(d):
            wi = w * x[i]
            ligne = m[i]
            for j in range(d):
                ligne[j] += wi * x[j]
    return m, mu, total


def jacobi_exact(a_init, tol_rel=1e-14, max_balayages=60):
    """Jacobi cyclique jusqu'à convergence (référence indépendante du code de l'organisme).
    Renvoie (valeurs triées par |valeur| décroissante, vecteurs en colonnes [ligne][k], hors-diagonale relative, balayages)."""
    n = len(a_init)
    a = [ligne[:] for ligne in a_init]
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    frob = math.sqrt(sum(a[i][j] ** 2 for i in range(n) for j in range(n))) or 1.0
    balayages = 0
    for balayages in range(1, max_balayages + 1):
        hors = math.sqrt(sum(a[i][j] ** 2 for i in range(n) for j in range(n) if i != j))
        if hors <= tol_rel * frob:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                apq = a[p][q]
                if abs(apq) < 1e-300:
                    continue
                theta = (a[q][q] - a[p][p]) / (2.0 * apq)
                t = (1.0 if theta >= 0 else -1.0) / (abs(theta) + math.sqrt(theta * theta + 1.0))
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
                tau = s / (1.0 + c)
                a[p][p] -= t * apq
                a[q][q] += t * apq
                a[p][q] = a[q][p] = 0.0
                for r in range(n):
                    if r != p and r != q:
                        arp, arq = a[r][p], a[r][q]
                        a[r][p] = a[p][r] = arp - s * (arq + tau * arp)
                        a[r][q] = a[q][r] = arq + s * (arp - tau * arq)
                for r in range(n):
                    vrp, vrq = v[r][p], v[r][q]
                    v[r][p] = vrp - s * (vrq + tau * vrp)
                    v[r][q] = vrq + s * (vrp - tau * vrq)
    hors = math.sqrt(sum(a[i][j] ** 2 for i in range(n) for j in range(n) if i != j)) / frob
    valeurs = [a[i][i] for i in range(n)]
    ordre = sorted(range(n), key=lambda k: abs(valeurs[k]), reverse=True)
    return [valeurs[k] for k in ordre], [[v[r][k] for k in ordre] for r in range(n)], hors, balayages


def decomposeur_exact(matrice, dim=DIM, max_iter=None):
    """Même signature et même format de sortie que memoire_isvd.decomposer_jacobi_symetrique."""
    valeurs, vecteurs, _, _ = jacobi_exact(matrice)
    return vecteurs, [abs(x) for x in valeurs]


def residu_hors_diagonale(matrice, u_tri):
    """Hors-diagonale relative de Uᵀ M U (0 si U diagonalise exactement M)."""
    n = len(matrice)
    mu_ = [[sum(matrice[i][k] * u_tri[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    a = [[sum(u_tri[k][i] * mu_[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    frob = math.sqrt(sum(matrice[i][j] ** 2 for i in range(n) for j in range(n))) or 1.0
    return math.sqrt(sum(a[i][j] ** 2 for i in range(n) for j in range(n) if i != j)) / frob


def parts_classes(vecteur):
    """Part de la norme au carré portée par chaque classe de coordonnées (lin, sin, car)."""
    tot = sum(x * x for x in vecteur) or 1.0
    return {c: sum(vecteur[i] ** 2 for i in range(len(vecteur)) if i % 3 == k) / tot
            for k, c in enumerate(CLASSES)}


def entropie_effective(sigma):
    s = [x for x in sigma if x > 0]
    tot = sum(s)
    return math.exp(-sum((x / tot) * math.log(x / tot) for x in s))


# ---------------------------------------------------------------- mesures d'information
def jaccard(a, b):
    u = len(a | b)
    return len(a & b) / u if u else 0.0


def matrice_jaccard(ensembles):
    n = len(ensembles)
    j = [[0.0] * n for _ in range(n)]
    for a in range(n):
        for b in range(a + 1, n):
            j[a][b] = j[b][a] = jaccard(ensembles[a], ensembles[b])
    return j


def rappel_plus_proche_voisin(vecteurs, mat_jaccard):
    """R@1 : part des textes dont le plus proche voisin par cosinus appartient à l'ensemble
    (ex aequo compris) des plus proches voisins par Jaccard des jetons. Renvoie (R@1, hasard)."""
    n = len(vecteurs)
    unit = [normer(v) for v in vecteurs]
    succes, hasard = 0, 0.0
    for i in range(n):
        jmax = max(mat_jaccard[i][j] for j in range(n) if j != i)
        etalon = {j for j in range(n) if j != i and mat_jaccard[i][j] == jmax}
        meilleur, cmax = None, -3.0
        for j in range(n):
            if j == i:
                continue
            c = produit_scalaire(unit[i], unit[j])
            if c > cmax:
                meilleur, cmax = j, c
        succes += 1 if meilleur in etalon else 0
        hasard += len(etalon) / (n - 1)
    return succes / n, hasard / n


def rangs_moyens(valeurs):
    ordre = sorted(range(len(valeurs)), key=lambda k: valeurs[k])
    rangs = [0.0] * len(valeurs)
    k = 0
    while k < len(ordre):
        fin = k
        while fin + 1 < len(ordre) and valeurs[ordre[fin + 1]] == valeurs[ordre[k]]:
            fin += 1
        moyen = (k + fin) / 2.0 + 1.0
        for t in range(k, fin + 1):
            rangs[ordre[t]] = moyen
        k = fin + 1
    return rangs


def spearman(x, y):
    rx, ry = rangs_moyens(x), rangs_moyens(y)
    mx, my = sum(rx) / len(rx), sum(ry) / len(ry)
    sxy = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    sxx = sum((a - mx) ** 2 for a in rx)
    syy = sum((b - my) ** 2 for b in ry)
    return sxy / math.sqrt(sxx * syy) if sxx > 0 and syy > 0 else 0.0


def spearman_paires(vecteurs, mat_jaccard):
    n = len(vecteurs)
    cs, js = [], []
    for a in range(n):
        for b in range(a + 1, n):
            cs.append(cosinus(vecteurs[a], vecteurs[b]))
            js.append(mat_jaccard[a][b])
    return spearman(cs, js)


def coordonnees_rang(vecteurs, u_tri, rang=RANG):
    """Coordonnées des vecteurs sur les `rang` premiers vecteurs propres (projection de la mémoire)."""
    return [[sum(u_tri[i][k] * v[i] for i in range(len(v))) for k in range(rang)] for v in vecteurs]


def aire_sous_courbe(positifs, negatifs):
    """Probabilité qu'un positif dépasse un négatif (ex aequo comptés 1/2)."""
    tot = 0.0
    for p in positifs:
        for q in negatifs:
            tot += 1.0 if p > q else (0.5 if p == q else 0.0)
    return tot / (len(positifs) * len(negatifs))


def moyenne_ecart(valeurs):
    n = len(valeurs)
    m = sum(valeurs) / n
    e = math.sqrt(sum((x - m) ** 2 for x in valeurs) / (n - 1)) if n > 1 else 0.0
    return m, e


def intervalle_bootstrap(valeurs, graine_boot, n_tirages=2000, niveau=0.95):
    rng = random.Random(graine_boot)
    n = len(valeurs)
    moyennes = sorted(sum(valeurs[rng.randrange(n)] for _ in range(n)) / n for _ in range(n_tirages))
    bas = moyennes[int((1.0 - niveau) / 2.0 * n_tirages)]
    haut = moyennes[int((1.0 + niveau) / 2.0 * n_tirages) - 1]
    return bas, haut


# ---------------------------------------------------------------- mémoire générationnelle
def poids_organisme(module, item):
    """Poids d'une trace comme dans mettre_a_jour_memoire_isvd (sans fn_ponderation)."""
    poids_brut = max(0.05, min(1.0, float(item.get("poids", 0.5))))
    if module._detecter_confirmation_multi_familles(item["texte"]):
        return min(1.0, round(poids_brut * 1.15, 4))
    return poids_brut


def maj_memoire(etat, lot, encodeur, decomposeur, module, centrer, dim=DIM, rang=RANG):
    """Une génération de mémoire. centrer=False : même construction que l'organisme
    (m = U Σ Uᵀ + Σ w ψψᵀ, décomposition, troncature au rang 6, Σ arrondi à 6 décimales).
    centrer=True : même construction sur la dispersion centrée, mise à jour exacte par la
    formule des axes parallèles (moyenne courante et poids total gardés dans l'état)."""
    u_prec = etat.get("U", [[0.0] * rang for _ in range(dim)])
    sigma_prec = etat.get("Sigma", [0.0] * rang)
    r = min(rang, len(sigma_prec))
    m = [[0.0] * dim for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            somme = 0.0
            for k in range(r):
                somme += u_prec[i][k] * sigma_prec[k] * u_prec[j][k]
            m[i][j] = somme
    psis, ws = [], []
    for item in lot:
        texte = str(item.get("texte", "")).strip()
        if not texte:
            continue
        ws.append(poids_organisme(module, item))
        psis.append(encodeur(texte))
    s0 = etat.get("S0", 0.0)
    mu = etat.get("mu", [0.0] * dim)
    if centrer:
        wb = sum(ws)
        mub = [sum(w * p[i] for p, w in zip(psis, ws)) / wb for i in range(dim)]
        for p, w in zip(psis, ws):
            x = [p[i] - mub[i] for i in range(dim)]
            for i in range(dim):
                for j in range(dim):
                    m[i][j] += w * x[i] * x[j]
        coef = s0 * wb / (s0 + wb)
        d = [mub[i] - mu[i] for i in range(dim)]
        for i in range(dim):
            for j in range(dim):
                m[i][j] += coef * d[i] * d[j]
        mu = [(s0 * mu[i] + wb * mub[i]) / (s0 + wb) for i in range(dim)]
        s0 = s0 + wb
    else:
        for p, w in zip(psis, ws):
            for i in range(dim):
                for j in range(dim):
                    m[i][j] += w * p[i] * p[j]
        wb = sum(ws)
        mub = [sum(w * p[i] for p, w in zip(psis, ws)) / wb for i in range(dim)]
        mu = [(s0 * mu[i] + wb * mub[i]) / (s0 + wb) for i in range(dim)]  # suivi seulement, sans effet sur m
        s0 = s0 + wb
    u_complet, sigma_complet = decomposeur(m, dim=dim)
    return {
        "U": [[u_complet[i][k] for k in range(rang)] for i in range(dim)],
        "Sigma": [round(sigma_complet[k], 6) for k in range(rang)],
        "S0": s0,
        "mu": mu,
        "queue": math.sqrt(sum(s * s for s in sigma_complet[rang:])),
        "totale": math.sqrt(sum(s * s for s in sigma_complet)),
        "trace_avant": sum(m[i][i] for i in range(dim)),
        "trace_gardee": sum(sigma_complet[:rang]),
    }
