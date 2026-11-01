"""Comparaison à plusieurs bras des règles de choix de paire du bisociateur — interface commune, bras, rétrodiction — v1.

Conception : `conception-comparaison-regles-paires-v1.md` (même dossier). Préenregistrement : brouillon 1, même dossier.

Ce module fournit :
- l'interface commune (`RegleDePaires`) : entrée = vue « avant coupure » d'un graphe de concepts daté (et, pour l'épreuve 2,
  un vivier de fiches ramené à des sacs de concepts) ; sortie = un score par paire candidate (plus haut = mieux classé) ;
- quatre bras codés et éprouvés sur graphe jouet : hasard (témoin obligatoire), « loin mais proche » (score du
  préenregistrement scellé de bisociation à deux espaces v2), marche de Swanson A-B-C (formule de la rétrodiction de
  Swanson v1, transposée au graphe), prédiction de liens par voisinage (Adamic-Adar ; Jaccard, allocation de ressources,
  voisins communs et attachement préférentiel en diagnostic) ;
- trois adaptateurs factices, à brancher : Gu-Krenn (code Impact4Cast relancé), méta (« trou à structure commune »),
  nouveauté atypique d'Uzzi ; ils refusent d'entrer dans une course tant qu'ils ne sont pas branchés (garde G8) ;
- la rétrodiction à date de coupure (jouet) et ses métriques, reprises **telles quelles** du code scellé de la
  rétrodiction de Swanson (`retrodiction-swanson/code/mesures_v1.py`, empreinte vérifiée au chargement) ;
- les gardes R5 (G1 à G10), chacune éprouvée sur un cas sain et un artefact dans `essais/test_regles_paires_v1.py`.

Aucun modèle de langage n'est appelé ni importé (fermeture algorithmique, garde G3). Graines : `numpy.random.SeedSequence`
dérivées par tâche (R9). Aucune donnée réelle n'est lue : seuls des mondes jouets.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from dataclasses import dataclass, field
from pathlib import Path
from statistics import NormalDist

import numpy as np

VERSION = "regles-paires-v1"
ICI = Path(__file__).resolve().parent
MESURES_SWANSON = ICI.parent / "retrodiction-swanson" / "code" / "mesures_v1.py"
MESURES_SWANSON_SHA256 = "f462dbd52ecd9181e387da1ff1ceb1a529f3bcd07e6ca85d83e9a5898af0888f"

# Modules de modèles de langage interdits dans toute la chaîne de génération des paires (fermeture algorithmique, G3).
MODULES_INTERDITS = ("openai", "anthropic", "transformers", "sentence_transformers", "vllm", "llama_cpp",
                     "google.generativeai", "google.genai", "mistralai", "cohere", "litellm", "langchain")

E_LOIN, BETA, EPS = 8.5, 1.0, 0.05   # bras « loin mais proche » : forme scellée de bisociation v2 (D-c, D-d)


class GardeArret(RuntimeError):
    """Arrêt d'une garde (R5) : jamais de repli silencieux."""


# ---------------------------------------------------------------------------------------------------------------------
# Graines (R9)
# ---------------------------------------------------------------------------------------------------------------------

def graine_tache(racine: int, tache: str) -> np.random.SeedSequence:
    """SeedSequence dérivée par tâche : même racine et même nom → même flux ; noms différents → flux indépendants."""
    cle = int.from_bytes(hashlib.sha256(tache.encode("utf-8")).digest()[:8], "big")
    return np.random.SeedSequence(entropy=racine, spawn_key=(cle,))


def rng_tache(racine: int, tache: str) -> np.random.Generator:
    return np.random.default_rng(graine_tache(racine, tache))


# ---------------------------------------------------------------------------------------------------------------------
# Métriques reprises telles quelles (rétrodiction de Swanson v1)
# ---------------------------------------------------------------------------------------------------------------------

_MESURES = None


def mesures_swanson():
    """Charge `mesures_v1.py` de la rétrodiction de Swanson après vérification de son empreinte (R6, R11) ; sinon arrêt."""
    global _MESURES
    if _MESURES is not None:
        return _MESURES
    if not MESURES_SWANSON.is_file():
        raise GardeArret(f"métriques de la rétrodiction de Swanson absentes : {MESURES_SWANSON}")
    sha = hashlib.sha256(MESURES_SWANSON.read_bytes()).hexdigest()
    if sha != MESURES_SWANSON_SHA256:
        raise GardeArret(f"empreinte de {MESURES_SWANSON.name} inattendue : {sha}")
    spec = importlib.util.spec_from_file_location("mesures_swanson_v1", MESURES_SWANSON)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    _MESURES = mod
    return mod


# ---------------------------------------------------------------------------------------------------------------------
# Graphe de concepts daté : vue « avant coupure » (seule visible des bras) et issues (lisibles après scellement)
# ---------------------------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class Document:
    """Métadonnées seules : date (entier, jours ou années), concepts repérés (titre et résumé), catégorie, lieu."""
    date: int
    concepts: tuple
    categorie: str = ""
    lieu: str = ""


@dataclass
class VueAvant:
    """Tout ce qu'un bras peut lire : documents datés strictement avant la coupure (ou à la coupure incluse)."""
    coupure: int
    concepts: list
    n: np.ndarray            # n[X, Y] = nombre de documents d'avant contenant X et Y (diagonale nulle)
    df: np.ndarray           # fréquence documentaire d'avant
    n_docs: int
    categories: list
    domaine: np.ndarray      # domaine[X, c] = documents d'avant de catégorie c contenant X
    lieux: list              # lieux[X] = dict lieu → nombre de documents d'avant
    docs_lieux: list         # pour chaque document d'avant : (tuple d'indices de concepts, lieu)

    @property
    def V(self) -> int:
        return len(self.concepts)

    def voisins(self) -> np.ndarray:
        return self.n > 0

    def degre(self) -> np.ndarray:
        return self.voisins().sum(axis=1)


def construire_vue(documents, coupure: int, df_min: int = 1, vocabulaire=None) -> VueAvant:
    """Vocabulaire gelé sur les seuls documents d'avant (df ≥ df_min) ; `vocabulaire` imposé = artefact possible (G2)."""
    avant = [d for d in documents if d.date <= coupure]
    if not avant:
        raise GardeArret("aucun document avant la coupure")
    if vocabulaire is None:
        compte = {}
        for d in avant:
            for c in set(d.concepts):
                compte[c] = compte.get(c, 0) + 1
        vocabulaire = sorted(c for c, k in compte.items() if k >= df_min)
    concepts = list(vocabulaire)
    idx = {c: i for i, c in enumerate(concepts)}
    categories = sorted({d.categorie for d in avant})
    icat = {c: i for i, c in enumerate(categories)}
    V = len(concepts)
    n = np.zeros((V, V), np.int64)
    df = np.zeros(V, np.int64)
    dom = np.zeros((V, len(categories)), np.int64)
    lieux = [dict() for _ in range(V)]
    docs_lieux = []
    for d in avant:
        ids = sorted({idx[c] for c in d.concepts if c in idx})
        docs_lieux.append((tuple(ids), d.lieu))
        for i in ids:
            df[i] += 1
            dom[i, icat[d.categorie]] += 1
            lieux[i][d.lieu] = lieux[i].get(d.lieu, 0) + 1
        for a in range(len(ids)):
            for b in range(a + 1, len(ids)):
                n[ids[a], ids[b]] += 1
                n[ids[b], ids[a]] += 1
    return VueAvant(coupure, concepts, n, df, len(avant), categories, dom, lieux, docs_lieux)


@dataclass(frozen=True)
class Jeton:
    """Preuve que les scores ont été scellés (empreinte) avant toute lecture d'issue (G10)."""
    empreinte: str
    noms: tuple


def empreinte_scores(scores: dict, paires: np.ndarray) -> str:
    h = hashlib.sha256()
    h.update(np.ascontiguousarray(paires, dtype=np.int64).tobytes())
    for nom in sorted(scores):
        h.update(nom.encode("utf-8"))
        h.update(np.ascontiguousarray(scores[nom], dtype=np.float64).tobytes())
    return h.hexdigest()


def sceller_scores(scores: dict, paires: np.ndarray) -> Jeton:
    return Jeton(empreinte_scores(scores, paires), tuple(sorted(scores)))


class Issues:
    """Documents d'après (coupure, coupure + horizon] ; lisibles seulement avec le jeton des scores scellés (G10)."""

    def __init__(self, documents, vue: VueAvant, horizon: int):
        self._apres = [d for d in documents if vue.coupure < d.date <= vue.coupure + horizon]
        self._idx = {c: i for i, c in enumerate(vue.concepts)}

    def etiquettes(self, paires: np.ndarray, jeton: Jeton, scores: dict, w: int) -> np.ndarray:
        if not isinstance(jeton, Jeton):
            raise GardeArret("issues demandées sans jeton de scellement (G10)")
        if jeton.empreinte != empreinte_scores(scores, paires):
            raise GardeArret("le jeton ne correspond pas aux scores présentés : scores modifiés après scellement (G10)")
        compte = {}
        for d in self._apres:
            ids = sorted({self._idx[c] for c in d.concepts if c in self._idx})
            for a in range(len(ids)):
                for b in range(a + 1, len(ids)):
                    compte[(ids[a], ids[b])] = compte.get((ids[a], ids[b]), 0) + 1
        return np.array([1 if compte.get((min(i, j), max(i, j)), 0) >= w else 0 for i, j in paires], np.int64)


def candidats_non_relies(vue: VueAvant, rng: np.random.Generator, n_max: int | None = None,
                         degre_min: int = 1) -> np.ndarray:
    """Paires (i < j) jamais reliées avant la coupure, deux extrémités de degré ≥ degre_min ; tirage uniforme si n_max."""
    deg = vue.degre()
    i, j = np.triu_indices(vue.V, k=1)
    m = (vue.n[i, j] == 0) & (deg[i] >= degre_min) & (deg[j] >= degre_min)
    paires = np.stack([i[m], j[m]], axis=1)
    if n_max is not None and len(paires) > n_max:
        paires = paires[np.sort(rng.choice(len(paires), n_max, replace=False))]
    return paires


# ---------------------------------------------------------------------------------------------------------------------
# Interface commune des bras
# ---------------------------------------------------------------------------------------------------------------------

class RegleDePaires:
    """Interface commune. `scorer(vue, paires, rng)` → tableau de scores (float, fini), un par paire candidate.

    Attributs déclarés : `nom` ; `reelle` (False pour un adaptateur factice : refusé en course, G8) ;
    `utilise_modele_de_langage` (doit rester False dans l'épreuve 1, G3) ; `repris_tel_quel` (texte : ce qui vient
    d'ailleurs, avec chemin ou lien) ; `code_ici` (texte : ce qui est codé ici)."""
    nom = "abstrait"
    reelle = True
    utilise_modele_de_langage = False
    repris_tel_quel = ""
    code_ici = ""

    def scorer(self, vue: VueAvant, paires: np.ndarray, rng: np.random.Generator) -> np.ndarray:
        raise NotImplementedError


class Hasard(RegleDePaires):
    """Témoin obligatoire : permutation uniforme (score_uniforme de la rétrodiction de Swanson, tel quel)."""
    nom = "hasard"
    repris_tel_quel = "mesures_v1.score_uniforme (rétrodiction de Swanson v1)"

    def scorer(self, vue, paires, rng):
        return mesures_swanson().score_uniforme(len(paires), rng)


class HasardStratifie(RegleDePaires):
    """Témoin secondaire : hasard stratifié par classes log2 des degrés (bas, haut) ; score_stratifie tel quel."""
    nom = "hasard_stratifie"
    repris_tel_quel = "mesures_v1.score_stratifie (rétrodiction de Swanson v1)"

    def scorer(self, vue, paires, rng):
        deg = vue.degre()
        a = np.floor(np.log2(np.maximum(deg[paires[:, 0]], 1))).astype(np.int64)
        b = np.floor(np.log2(np.maximum(deg[paires[:, 1]], 1))).astype(np.int64)
        strate = np.minimum(a, b) * 1000 + np.maximum(a, b)
        return mesures_swanson().score_stratifie(strate, rng)


def jaccard_voisins(vue: VueAvant, paires: np.ndarray) -> np.ndarray:
    G = vue.voisins()
    a, b = G[paires[:, 0]], G[paires[:, 1]]
    inter = (a & b).sum(axis=1)
    union = (a | b).sum(axis=1)
    return np.where(union > 0, inter / np.where(union > 0, union, 1), 0.0)


def cosinus_domaine(vue: VueAvant, paires: np.ndarray) -> np.ndarray:
    D = vue.domaine.astype(np.float64)
    norme = np.linalg.norm(D, axis=1)
    a, b = paires[:, 0], paires[:, 1]
    num = (D[a] * D[b]).sum(axis=1)
    den = norme[a] * norme[b]
    return np.where(den > 0, num / np.where(den > 0, den, 1), 0.0)


class LoinMaisProche(RegleDePaires):
    """Bras basique : s = (1 − cos²_domaine)^8,5 × (κ_concept + 0,05).

    Forme et constantes reprises du préenregistrement scellé de bisociation à deux espaces v2 (§ 5 : e = 8,5, β = 1,
    ε = 0,05). Transposition déclarée aux paires de concepts : domaine d'un concept = répartition de ses documents
    d'avant entre catégories ; κ = Jaccard des voisinages d'avant (proximité de concept)."""
    nom = "loin_mais_proche"
    repris_tel_quel = "forme s_ij et constantes de prereg/preenregistrement-bisociation-deux-espaces-v2.md (§ 5)"
    code_ici = "domaine = catégories des documents d'avant ; κ = Jaccard des voisinages d'avant"

    def scorer(self, vue, paires, rng):
        cos = cosinus_domaine(vue, paires)
        kappa = jaccard_voisins(vue, paires)
        return (1.0 - cos ** 2) ** E_LOIN * (kappa + EPS) ** BETA


class SwansonABC(RegleDePaires):
    """S = ½ [K/r(A) + K/r(C)], K = Σ_B n(A,B)·n(B,C)·idf(B)/r(B) (préenregistrement de la rétrodiction de Swanson,
    § 7) ; ici n(·,·) = cooccurrences du graphe d'avant, idf(B) = ln(N_avant/df(B))."""
    nom = "swanson_abc"
    repris_tel_quel = "formule S de retrodiction-swanson/preenregistrement-retrodiction-v1.md § 7 (moyenne des deux sens)"
    code_ici = "calcul matriciel sur le graphe (le code d'origine travaille sur la matrice documents × termes)"

    def scorer(self, vue, paires, rng):
        n = vue.n.astype(np.float64)
        r = n.sum(axis=1)
        idf = np.log(vue.n_docs / np.maximum(vue.df, 1))
        poids = np.where(r > 0, idf / np.where(r > 0, r, 1), 0.0)
        a, c = paires[:, 0], paires[:, 1]
        K = np.einsum("ij,j,ij->i", n[a], poids, n[c])
        ra, rc = r[a], r[c]
        sa = np.where(ra > 0, K / np.where(ra > 0, ra, 1), 0.0)
        sc = np.where(rc > 0, K / np.where(rc > 0, rc, 1), 0.0)
        return 0.5 * (sa + sc)


class Voisinage(RegleDePaires):
    """Prédiction de liens sans apprentissage : 'aa' Adamic-Adar (bras), 'ra' allocation de ressources (référence à
    battre, gagnante de la rétrodiction de Swanson), 'jaccard', 'cn' voisins communs, 'pa' attachement préférentiel."""
    repris_tel_quel = "définitions de retrodiction-swanson/preenregistrement-retrodiction-v1.md § 7 (AA, RA, CN, PA)"

    def __init__(self, mesure: str = "aa"):
        if mesure not in ("aa", "ra", "jaccard", "cn", "pa"):
            raise ValueError(mesure)
        self.mesure = mesure
        self.nom = {"aa": "adamic_adar", "ra": "allocation_ressources", "jaccard": "jaccard",
                    "cn": "voisins_communs", "pa": "attachement_preferentiel"}[mesure]

    def scorer(self, vue, paires, rng):
        G = vue.voisins()
        deg = G.sum(axis=1).astype(np.float64)
        a, c = paires[:, 0], paires[:, 1]
        if self.mesure == "pa":
            return vue.df[a].astype(np.float64) * vue.df[c].astype(np.float64)
        if self.mesure == "jaccard":
            return jaccard_voisins(vue, paires)
        commun = G[a] & G[c]
        if self.mesure == "cn":
            return commun.sum(axis=1).astype(np.float64)
        if self.mesure == "ra":
            w = np.where(deg > 0, 1.0 / np.where(deg > 0, deg, 1), 0.0)
        else:  # aa : un voisin commun a un degré ≥ 2, donc ln > 0
            w = np.where(deg >= 2, 1.0 / np.log(np.where(deg >= 2, deg, 2)), 0.0)
        return (commun * w).sum(axis=1)


class AdaptateurFactice(RegleDePaires):
    """Bras à brancher. Refusé en course (G8). En mode essai seulement, rend un score constant (aucune information)."""
    reelle = False
    entrees_requises = ()
    a_brancher = ""

    def __init__(self, mode_essai: bool = False):
        self.mode_essai = mode_essai

    def scorer(self, vue, paires, rng):
        if not self.mode_essai:
            raise GardeArret(f"bras « {self.nom} » factice : non branché ({self.a_brancher})")
        return np.zeros(len(paires))


class GuKrennFactice(AdaptateurFactice):
    nom = "gu_krenn"
    repris_tel_quel = ("Impact4Cast (licence MIT, tête d2af4f3d…) : create_concepts/ (RAKE, seuils 9 et 6), "
                       "create_dynamic_edges/, features_utils.py (141 traits, get_norm_features), train_model_utils.py")
    entrees_requises = ("documents d'avant avec titre et résumé", "citations annuelles des documents d'avant",
                        "graphe à y−3 et y pour l'entraînement")
    a_brancher = ("voie 1 : leur code relancé sur notre corpus, sorties lues depuis un fichier de scores ; "
                  "voie 2 si la voie 1 ne marche pas (règle D3) : leur méthode recodée (traits de réseau + réseau "
                  "à quatre couches de 600), pas leur modèle")


class MetaFactice(AdaptateurFactice):
    nom = "meta_trou_structure_commune"
    repris_tel_quel = "annexe-bras-meta-v1-brouillon4.md § 1-6 (pour les fiches) ; transposition au graphe à écrire"
    entrees_requises = ("partition en niches (communautés du graphe d'avant)", "table de communication entre niches",
                        "structures communes typées", "bande d'éloignement non extrême")
    a_brancher = "score = 1[communication faible]·1[structure forte]·1[éloignement dans la bande]·(1 + p·s)"


class UzziFactice(AdaptateurFactice):
    nom = "nouveaute_atypique_uzzi"
    repris_tel_quel = "Novelpy (github.com/Kwirtz/novelpy, indicateur « Atypicality » d'Uzzi et collègues 2013 ; licence à vérifier)"
    entrees_requises = ("lieux (revues) des documents d'avant", "modèle nul par échange préservant les marges")
    a_brancher = "score = −z au 10e centile des paires de lieux (u, v), restreint aux paires de conventionnalité médiane haute"


BRAS_CODES = (Hasard, LoinMaisProche, SwansonABC)
BRAS_FACTICES = (GuKrennFactice, MetaFactice, UzziFactice)


# ---------------------------------------------------------------------------------------------------------------------
# Gardes (R5) — chacune éprouvée sur un cas sain et un artefact
# ---------------------------------------------------------------------------------------------------------------------

def garde_sans_modele_de_langage(regles) -> None:
    """G3 : aucun bras ne déclare de modèle de langage ; aucun module de modèle de langage chargé dans le processus."""
    for r in regles:
        if r.utilise_modele_de_langage:
            raise GardeArret(f"bras « {r.nom} » déclare un modèle de langage : interdit dans la génération des paires")
    charges = [m for m in sys.modules if any(m == p or m.startswith(p + ".") for p in MODULES_INTERDITS)]
    if charges:
        raise GardeArret(f"modules de modèle de langage chargés : {sorted(charges)}")


def garde_vocabulaire_avant(vue: VueAvant, documents, df_min: int = 1) -> None:
    """G2 : chaque concept du vocabulaire apparaît dans au moins df_min documents d'avant."""
    compte = {}
    for d in documents:
        if d.date <= vue.coupure:
            for c in set(d.concepts):
                compte[c] = compte.get(c, 0) + 1
    hors = [c for c in vue.concepts if compte.get(c, 0) < df_min]
    if hors:
        raise GardeArret(f"vocabulaire non gelé avant la coupure : {hors[:5]}")


def garde_candidats(vue: VueAvant, paires: np.ndarray) -> None:
    """G4 : paires distinctes, i < j, jamais reliées avant la coupure."""
    if paires.ndim != 2 or paires.shape[1] != 2:
        raise GardeArret("forme des paires invalide")
    if np.any(paires[:, 0] >= paires[:, 1]):
        raise GardeArret("paire non ordonnée ou boucle")
    if np.any(vue.n[paires[:, 0], paires[:, 1]] > 0):
        raise GardeArret("paire candidate déjà reliée avant la coupure")
    if len(np.unique(paires, axis=0)) != len(paires):
        raise GardeArret("paires candidates en double")


def garde_scores(scores: dict, n: int) -> None:
    """G5 : un score fini par paire, pour chaque bras."""
    for nom, s in scores.items():
        s = np.asarray(s)
        if s.shape != (n,):
            raise GardeArret(f"bras « {nom} » : {s.shape} scores pour {n} paires")
        if not np.all(np.isfinite(s)):
            raise GardeArret(f"bras « {nom} » : score non fini")


def garde_jugeabilite(y: np.ndarray, minimum: int = 50) -> None:
    """G6 : assez de positives pour lire (sinon « non lançable », jamais lu)."""
    k = int(np.sum(y))
    if k < minimum or k == len(y):
        raise GardeArret(f"non lançable : {k} positives (minimum {minimum})")


def garde_hasard_au_taux_de_base(y: np.ndarray, score_hasard: np.ndarray, nb_et: float = 4.0) -> None:
    """G7 : l'aire du témoin hasard reste à moins de nb_et erreurs-types de 0,5 (erreur-type de Mann-Whitney sous H0)."""
    m = mesures_swanson()
    aire = m.metriques(m.Ordre(score_hasard), y, ks=())["aire"]
    n1 = int(y.sum()); n0 = len(y) - n1
    et = math.sqrt((n1 + n0 + 1) / (12.0 * n1 * n0))
    if abs(aire - 0.5) > nb_et * et:
        raise GardeArret(f"témoin hasard hors du taux de base : aire {aire:.4f}, écart {abs(aire - 0.5) / et:.1f} erreurs-types")


def garde_bras_reels(regles) -> None:
    """G8 : aucun adaptateur factice dans une course."""
    f = [r.nom for r in regles if not r.reelle]
    if f:
        raise GardeArret(f"adaptateurs factices refusés en course : {f}")
    if not any(isinstance(r, Hasard) for r in regles):
        raise GardeArret("témoin hasard absent : obligatoire")


def garde_absence_fuite(regle: RegleDePaires, documents, coupure: int, racine: int, df_min: int = 1) -> None:
    """G1 : les scores d'un bras ne changent pas quand on remplace tous les documents d'après la coupure."""
    rng0 = rng_tache(racine, "fuite-perturbation")
    apres = [d for d in documents if d.date > coupure]
    avant = [d for d in documents if d.date <= coupure]
    tous_concepts = sorted({c for d in documents for c in d.concepts})
    perturbes = [Document(d.date, tuple(rng0.choice(tous_concepts, size=len(d.concepts), replace=False)),
                          d.categorie, d.lieu) for d in apres]
    sorties = []
    for docs in (documents, avant + perturbes):
        vue = construire_vue(docs, coupure, df_min)
        paires = candidats_non_relies(vue, rng_tache(racine, "candidats"))
        sorties.append(np.asarray(regle.scorer(vue, paires, rng_tache(racine, "bras-" + regle.nom)), np.float64))
    if sorties[0].shape != sorties[1].shape or not np.array_equal(sorties[0], sorties[1]):
        raise GardeArret(f"bras « {regle.nom} » : scores modifiés par les documents d'après (fuite temporelle)")


# ---------------------------------------------------------------------------------------------------------------------
# Comparaisons : DeLong apparié, Holm
# ---------------------------------------------------------------------------------------------------------------------

def _rangs_moyens(x: np.ndarray) -> np.ndarray:
    """Rangs moyens (1 à n), égalités au rang moyen de leur groupe."""
    _, inverse, compte = np.unique(x, return_inverse=True, return_counts=True)
    fin = np.cumsum(compte)
    return ((fin - compte + 1 + fin) / 2.0)[inverse]


def delong(scores: list, y: np.ndarray):
    """Aires et matrice de covariance de DeLong (égalités pour moitié) pour plusieurs scores sur les mêmes paires."""
    y = np.asarray(y).astype(bool)
    m, n = int(y.sum()), int((~y).sum())
    aires, V10, V01 = [], [], []
    for s in scores:
        s = np.asarray(s, np.float64)
        pos, neg = s[y], s[~y]
        tx, ty, tz = _rangs_moyens(pos), _rangs_moyens(neg), _rangs_moyens(np.concatenate([pos, neg]))
        aire = (tz[:m].sum() - m * (m + 1) / 2.0) / (m * n)
        aires.append(aire)
        V10.append((tz[:m] - tx) / n)
        V01.append(1.0 - (tz[m:] - ty) / m)
    V10, V01 = np.array(V10), np.array(V01)
    S = np.atleast_2d(np.cov(V10)) / m + np.atleast_2d(np.cov(V01)) / n
    return np.array(aires), S


def comparer_au_hasard(scores: dict, y: np.ndarray, nom_hasard: str = "hasard") -> dict:
    """Pour chaque bras : Δaire = aire(bras) − aire(hasard réalisé), z de DeLong apparié, p unilatérale (bras > hasard)."""
    noms = [k for k in scores if k != nom_hasard]
    aires, S = delong([scores[nom_hasard]] + [scores[k] for k in noms], y)
    sortie = {}
    for i, k in enumerate(noms, start=1):
        d = aires[i] - aires[0]
        var = S[i, i] + S[0, 0] - 2 * S[0, i]
        z = d / math.sqrt(var) if var > 0 else (math.inf if d > 0 else -math.inf if d < 0 else 0.0)
        p = 1.0 - NormalDist().cdf(z) if math.isfinite(z) else (0.0 if z > 0 else 1.0)
        sortie[k] = {"aire": float(aires[i]), "aire_hasard": float(aires[0]), "delta": float(d), "z": z, "p": p}
    return sortie


def holm(pvaleurs: dict, alpha: float = 0.05) -> dict:
    """Procédure de Holm (rejets et p ajustées), contrôle du taux d'erreur familial au niveau alpha."""
    noms = sorted(pvaleurs, key=lambda k: (pvaleurs[k], k))
    m = len(noms)
    sortie, courant, continuer = {}, 0.0, True
    for rang, k in enumerate(noms):
        ajustee = min(1.0, max(courant, (m - rang) * pvaleurs[k]))
        courant = ajustee
        rejet = continuer and pvaleurs[k] <= alpha / (m - rang)
        if not rejet:
            continuer = False
        sortie[k] = {"p": pvaleurs[k], "p_holm": ajustee, "rejet": rejet}
    return sortie


# ---------------------------------------------------------------------------------------------------------------------
# Rétrodiction à coupure (jouet) et pont vers l'épreuve 2
# ---------------------------------------------------------------------------------------------------------------------

def retrodiction(documents, coupure: int, horizon: int, w: int, regles, racine: int, n_max=None, df_min: int = 1,
                 ks=(100,), minimum_positives: int = 50, alpha: float = 0.05) -> dict:
    """Chaîne complète : gardes, vue d'avant, candidats, scores, scellement, issues, métriques, comparaison au hasard."""
    regles = list(regles)
    garde_bras_reels(regles)
    garde_sans_modele_de_langage(regles)
    vue = construire_vue(documents, coupure, df_min)
    garde_vocabulaire_avant(vue, documents, df_min)
    paires = candidats_non_relies(vue, rng_tache(racine, "candidats"), n_max)
    garde_candidats(vue, paires)
    scores = {r.nom: np.asarray(r.scorer(vue, paires, rng_tache(racine, "bras-" + r.nom)), np.float64) for r in regles}
    garde_scores(scores, len(paires))
    jeton = sceller_scores(scores, paires)
    y = Issues(documents, vue, horizon).etiquettes(paires, jeton, scores, w)
    garde_jugeabilite(y, minimum_positives)
    garde_hasard_au_taux_de_base(y, scores["hasard"])
    m = mesures_swanson()
    metr = {k: m.metriques(m.Ordre(s), y, ks=ks) for k, s in scores.items()}
    comp = comparer_au_hasard(scores, y)
    lecture = holm({k: v["p"] for k, v in comp.items()}, alpha)
    manifeste = {"version": VERSION, "racine": racine, "coupure": coupure, "horizon": horizon, "w": w,
                 "n_paires": int(len(paires)), "n_positives": int(y.sum()), "empreinte_scores": jeton.empreinte,
                 "mesures_swanson_sha256": MESURES_SWANSON_SHA256, "numpy": np.__version__,
                 "bras": [{"nom": r.nom, "repris_tel_quel": r.repris_tel_quel, "code_ici": r.code_ici} for r in regles]}
    return {"metriques": metr, "comparaison": comp, "holm": lecture, "manifeste": manifeste}


def regle_entree_course_2(lecture_holm: dict) -> list:
    """Règle gelée : un bras n'entre en course 2 que s'il bat le hasard sur l'épreuve 1 (rejet de Holm)."""
    return sorted(k for k, v in lecture_holm.items() if v["rejet"])


def score_paire_fiches(regle: RegleDePaires, vue: VueAvant, fiche_a, fiche_b, m: int = 3,
                       rng: np.random.Generator | None = None) -> float:
    """Pont vers l'épreuve 2 : note d'une paire de fiches = moyenne des m plus hauts scores de paires de concepts
    (c_a, c_b), c_a ≠ c_b, non reliées avant la coupure (forme du bras Gu-Krenn de M9). Moins d'une paire : arrêt."""
    idx = {c: i for i, c in enumerate(vue.concepts)}
    ca = sorted({idx[c] for c in fiche_a if c in idx})
    cb = sorted({idx[c] for c in fiche_b if c in idx})
    paires = sorted({(min(a, b), max(a, b)) for a in ca for b in cb if a != b and vue.n[a, b] == 0})
    if not paires:
        raise GardeArret("paire de fiches non notable : aucune paire de concepts non reliée dans le vocabulaire")
    p = np.array(paires, np.int64)
    s = np.sort(np.asarray(regle.scorer(vue, p, rng or rng_tache(0, "fiches")), np.float64))[::-1]
    return float(s[:m].mean())


# ---------------------------------------------------------------------------------------------------------------------
# Monde jouet (aucune donnée réelle)
# ---------------------------------------------------------------------------------------------------------------------

def monde_jouet(racine: int, V: int = 60, n_cat: int = 3, n_avant: int = 700, n_apres: int = 500,
                coupure: int = 10, fermeture: float = 0.85) -> list:
    """Documents jouets : avant la coupure, documents tirés dans une catégorie (concepts surtout de la catégorie) ;
    après, une part `fermeture` de documents par fermeture de triangles (A–B–C → {A, C}), le reste au hasard."""
    rng = rng_tache(racine, "monde-jouet")
    concepts = [f"c{i:03d}" for i in range(V)]
    maison = np.arange(V) % n_cat
    popularite = rng.pareto(1.5, V) + 1.0
    lieux = [f"revue{k}" for k in range(2 * n_cat)]
    docs = []
    for t in range(n_avant):
        cat = int(rng.integers(n_cat))
        p = popularite * np.where(maison == cat, 1.0, 0.08)
        k = int(rng.integers(2, 5))
        ids = rng.choice(V, size=k, replace=False, p=p / p.sum())
        docs.append(Document(1 + t * coupure // n_avant, tuple(concepts[i] for i in ids), f"cat{cat}",
                             lieux[2 * cat + int(rng.integers(2))]))
    vue = construire_vue(docs, coupure)
    G = vue.voisins()
    for t in range(n_apres):
        date = coupure + 1 + t * 5 // n_apres
        if rng.random() < fermeture:
            a = int(rng.integers(V))
            vb = np.flatnonzero(G[a])
            if vb.size:
                b = int(rng.choice(vb))
                vc = np.flatnonzero(G[b] & ~G[a])
                vc = vc[vc != a]
                if vc.size:
                    c = int(rng.choice(vc))
                    docs.append(Document(date, (concepts[a], concepts[c]), f"cat{maison[a]}", lieux[2 * maison[a]]))
                    continue
        ids = rng.choice(V, size=2, replace=False)
        docs.append(Document(date, tuple(concepts[i] for i in ids), f"cat{maison[ids[0]]}", lieux[0]))
    return docs


if __name__ == "__main__":  # démonstration jouet, aucune donnée réelle
    docs = monde_jouet(20261101)
    res = retrodiction(docs, 10, 5, 1, [Hasard(), LoinMaisProche(), SwansonABC(), Voisinage("aa"), Voisinage("ra")],
                       racine=20261101)
    print(json.dumps({k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in res["metriques"].items()},
                     ensure_ascii=False, indent=1))
    print(json.dumps(res["holm"], ensure_ascii=False, indent=1))
    print("entrent en course 2 (jouet) :", regle_entree_course_2(res["holm"]))
