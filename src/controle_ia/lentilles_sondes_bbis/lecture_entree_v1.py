"""Lecture côté entrée par notre lentille S, référence « plongements seuls », gardes de la seconde passe.

Texte : `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (`a2bbed7a…`), « Métrique », points 3 et 4 ; « Plan d'analyse »,
points 5 et 6 ; « Liste d'arrêt » (garde de la fonction de lecture de notre R, de ses moitiés ou de notre S). Le texte décide.

- **Lecture par notre S** d'un vecteur c (direction `w` ou `q` d'une sonde, direction nulle ou témoin), à la couche ℓ de la
  sonde : g = c · K_ℓ (covecteur des plongements) ; ‖g‖ nul ou non fini : « non calculable » ; sinon û = g / ‖g‖, et le score
  d'entrée du jeton gardé t est s_t(c) = û · (e_t − ē), e_t la ligne t de `model.embed_tokens.weight`, ē la moyenne des e_t
  sur les jetons gardés. Tout en simple précision (le voisin calcule en demi-précision : écart déclaré). s_t(−c) = −s_t(c) ;
  la lecture ne dépend pas de la norme de c (normalisation exacte) : le rapport à ε est **sans objet** pour notre S.
- **Référence « plongements seuls »** : s⁰_t(c) = (c / ‖c‖) · (e_t − ē), K remplacée par l'identité, **même code** ; aucun
  nul, aucun p, aucun libellé.
- **Chemin indépendant** de la garde de notre S : il recopie l'expression du voisin (`c @ K`, normé, puis produit par les
  plongements centrés), en double précision, par `numpy`. Il partage avec le code l'hypothèse d'orientation de K (covecteur à
  gauche ; « Frontière », point 18).
- **Notre R** se lit par la fonction de la première passe, `lecture_v1.lire`, telle quelle, avec J_ℓ = la matrice de notre R ;
  sa garde est celle de `lecture_v1.garde_fonction_lecture` (artefact : la matrice de notre R de la couche suivante).
"""
from __future__ import annotations

import numpy as np
import torch

from . import constantes_v1 as K
from . import constantes_v2 as K2
from . import lecture_v1 as le
from .constantes_v1 import Arret

MOTIF_NORME_NULLE = "non calculable : norme nulle ou non finie du covecteur des plongements (c · K)"
SANS_OBJET_PLONGEMENTS_LIES = ("sans objet : `model.embed_tokens.weight` et `lm_head.weight` sont égaux (plongements liés) ; les "
                               "artefacts (i) et (ii) suffisent")
ARTEFACT_COUCHE_SUIVANTE = "(i) matrice de notre S de la couche suivante"
ARTEFACT_TRANSPOSEE = "(ii) transposée de K"
ARTEFACT_LIGNES_DE_SORTIE = "(iii) lignes de `lm_head.weight` à la place des plongements"


def _colonnes(c) -> torch.Tensor:
    t = torch.as_tensor(np.asarray(c, dtype=np.float32) if not isinstance(c, torch.Tensor) else c, dtype=torch.float32)
    return t[:, None] if t.ndim == 1 else t


def centrer(plongements: torch.Tensor) -> torch.Tensor:
    """e_t − ē : lignes gardées de `model.embed_tokens.weight`, en simple précision, moins leur moyenne sur les jetons gardés."""
    if plongements.dtype != torch.float32 or plongements.ndim != 2:
        raise Arret("plongements attendus en simple précision, [jetons gardés, largeur]")
    return plongements - plongements.mean(0, keepdim=True)


def covecteur(c, k: torch.Tensor | None) -> torch.Tensor:
    """g = c · K, pour chaque colonne de c : `[largeur des plongements, n]`. `k` `None` : identité (plongements seuls).
    K est orientée [sortie du bloc ℓ, plongement] : le covecteur est à gauche (`c @ K`)."""
    c = _colonnes(c)
    if k is None:
        return c
    if k.dtype != torch.float32 or k.ndim != 2 or k.shape[0] != c.shape[0]:
        raise Arret(f"matrice de notre S de forme {tuple(k.shape)} ({k.dtype}) ; [{c.shape[0]}, largeur] en simple précision "
                    "attendue")
    return k.T @ c


def lire_entree(c, k: torch.Tensor | None, plongements_centres: torch.Tensor, bloc: int = 256) -> tuple[torch.Tensor, np.ndarray]:
    """Scores d'entrée de **tous** les jetons gardés pour chaque colonne de c : (`[jetons, n]` en simple précision, calculable
    `[n]`). Une colonne dont ‖c · K‖ est nulle ou non finie est « non calculable » : ses scores sont rendus nuls et son drapeau
    faux (l'appelant écrit le motif, ou arrête s'il s'agit d'une direction nulle ou d'un témoin). Une autre valeur non finie :
    arrêt."""
    g = covecteur(c, k)
    normes = g.norm(dim=0)
    calculable = torch.isfinite(normes) & (normes > 0) & torch.isfinite(g).all(0)
    u = torch.where(calculable[None, :], g / torch.where(calculable, normes, torch.ones_like(normes))[None, :], torch.zeros_like(g))
    if plongements_centres.dtype != torch.float32 or plongements_centres.shape[1] != u.shape[0]:
        raise Arret("plongements centrés attendus en simple précision, de la largeur du covecteur")
    scores = torch.empty((plongements_centres.shape[0], u.shape[1]), dtype=torch.float32)
    for s in range(0, u.shape[1], bloc):
        scores[:, s:s + bloc] = plongements_centres @ u[:, s:s + bloc]
    if not bool(torch.isfinite(scores).all()):
        raise Arret("valeur non finie dans une lecture : arrêt")
    return scores, calculable.numpy()


def lire_entree_exigee(c, k: torch.Tensor | None, plongements_centres: torch.Tensor) -> torch.Tensor:
    """Lecture de directions nulles ou témoins : une colonne non calculable est une valeur non finie dans un nul : arrêt."""
    scores, calculable = lire_entree(c, k, plongements_centres)
    if not bool(calculable.all()):
        raise Arret("valeur non finie dans un nul (norme nulle du covecteur des plongements) : arrêt")
    return scores


def lire_plongements_seuls(c, plongements_centres: torch.Tensor) -> tuple[torch.Tensor, np.ndarray]:
    """Référence « plongements seuls » : la même lecture, K remplacée par l'identité (même code)."""
    return lire_entree(c, None, plongements_centres)


def relire_par_chemin_independant(c: np.ndarray, k: np.ndarray, plongements: np.ndarray) -> np.ndarray:
    """Chemin indépendant, en double précision : l'expression du voisin, recopiée — `c @ K`, normé, puis produit par les
    plongements centrés. `c` `[largeur]` ou `[n, largeur]` (covecteurs en lignes) ; rend `[n, jetons]`."""
    lignes = np.atleast_2d(np.asarray(c, dtype=np.float64))
    g = lignes @ np.asarray(k, dtype=np.float64)
    g = g / np.linalg.norm(g, axis=1, keepdims=True)
    e = np.asarray(plongements, dtype=np.float64)
    return g @ (e - e.mean(axis=0, keepdims=True)).T


def _dix(scores: torch.Tensor) -> list[set]:
    return [set(x) for x in scores.topk(min(K.K_GARDE, scores.shape[0]), dim=0).indices.T.tolist()]


def garde_fonction_lecture_entree(colonnes, k: torch.Tensor, k_suivante: torch.Tensor, plongements: torch.Tensor,
                                  lignes_de_sortie: torch.Tensor, couche: int, plongements_lies: bool) -> dict:
    """Plan, point 5, notre S : sur les mêmes 64 colonnes prises comme covecteurs, les dix premiers jetons rendus par notre
    code égalent, au rang près, ceux du chemin indépendant en double précision (cas sain ; un écart limité à des jetons dont
    les scores diffèrent de moins de 10⁻⁴ en valeur relative est compté et rapporté, sans arrêt ; deux scores égaux, nuls
    compris, comptent pour une différence relative nulle) ; tout autre écart : arrêt. Artefacts : (i) la matrice de notre S de
    la couche suivante, (ii) la transposée de K, (iii) les lignes de `lm_head.weight` à la place des plongements ; pour
    chacun, au moins 32 des 64 colonnes diffèrent du cas sain ; sinon arrêt. Plongements liés : (iii) est « sans objet »."""
    colonnes = _colonnes(colonnes)
    n = colonnes.shape[1]
    centres = centrer(plongements)
    scores, calculable = lire_entree(colonnes, k, centres)
    if not bool(calculable.all()):
        raise Arret(f"garde de la fonction de lecture (notre S, couche {couche}) : colonne non calculable : arrêt avant tout calcul")
    sain = _dix(scores)
    independant = torch.from_numpy(relire_par_chemin_independant(colonnes.T.numpy(), k.numpy(), plongements.numpy()).T)
    autre = _dix(independant)
    quasi = 0
    for j in range(n):
        if sain[j] == autre[j]:
            continue
        seuil = float(scores[:, j].topk(min(K.K_GARDE, scores.shape[0])).values[-1])
        if all(abs(float(scores[i, j]) - seuil) <= K.TOLERANCE_EGALITE_GARDE * abs(seuil) for i in sain[j] ^ autre[j]):
            quasi += 1
            continue
        raise Arret(f"garde de la fonction de lecture (notre S, couche {couche}) : écart sur le cas sain à la colonne {j} : arrêt "
                    "avant tout calcul")
    artefacts = {}

    def artefact(nom: str, k_art: torch.Tensor, e_art: torch.Tensor) -> None:
        differentes = sum(a != b for a, b in zip(sain, _dix(lire_entree(colonnes, k_art, centrer(e_art))[0])))
        if differentes < K.MIN_COLONNES_ARTEFACT:
            raise Arret(f"garde de la fonction de lecture (notre S, couche {couche}) : artefact {nom} vu sur {differentes} "
                        f"colonnes sur {n} seulement (au moins {K.MIN_COLONNES_ARTEFACT} exigées) : arrêt avant tout calcul")
        artefacts[nom] = int(differentes)

    artefact(ARTEFACT_COUCHE_SUIVANTE, k_suivante, plongements)
    artefact(ARTEFACT_TRANSPOSEE, k.T.contiguous(), plongements)
    if plongements_lies:
        artefacts[ARTEFACT_LIGNES_DE_SORTIE] = SANS_OBJET_PLONGEMENTS_LIES
    else:
        artefact(ARTEFACT_LIGNES_DE_SORTIE, k, lignes_de_sortie)
    return {"lentille": K2.LENTILLE_NOTRE_S, "couche": int(couche), "colonnes": n, "ecarts_de_quasi_egalite": quasi,
            "colonnes_differentes_sur_artefact": artefacts, "tenue": True}


def garde_fonction_lecture_notre_r(lire_voisin, colonnes, gamma: torch.Tensor, wu: torch.Tensor, matrice: torch.Tensor,
                                   matrice_suivante: torch.Tensor, lentille: str, couche: int) -> dict:
    """Plan, point 5, notre R et chacune de ses moitiés : la garde de la première passe, telle quelle (mêmes 64 colonnes,
    mêmes règles) ; artefact : la matrice de notre R de la couche suivante (7 → 15 → 23 → 7)."""
    return le.garde_fonction_lecture(lire_voisin, colonnes, gamma, wu, matrice, matrice_suivante, lentille, couche)


def plongements_lies(plongements: torch.Tensor, lignes_de_sortie: torch.Tensor) -> bool:
    """Les lignes gardées de `model.embed_tokens.weight` et de `lm_head.weight` sont-elles égales ?"""
    return bool(plongements.shape == lignes_de_sortie.shape and torch.equal(plongements, lignes_de_sortie))


# --- garde du rapport à ε, étendue aux lentilles de la seconde passe (plan, point 6) -----------------------------------------------------
LENTILLES_DU_RAPPORT = (K.LENTILLE_PUBLIQUE, K.LENTILLE_LOGITS, K2.LENTILLE_NOTRE_R, K2.MOITIE_PAIRE, K2.MOITIE_IMPAIRE)
MOTIF_MOITIES_NUL_REFAIT = "non calculable : nuls isotropes refaits par direction à cette couche (garde du rapport à ε)"


def garde_rapport_epsilon(rho_min: dict) -> dict:
    """`rho_min` : lentille → minimum de ρ à une couche, pour la lentille publique, la lentille des logits, notre R et ses
    moitiés (celles qui sont lues). Si le minimum est < 100 pour l'une d'elles : le nul isotrope est refait par vecteur **pour
    la lentille publique, la lentille des logits et notre R** de cette couche (l'appariement du recouvrement est gardé), et le
    recouvrement des moitiés et son p sont « non calculables » à cette couche. Notre S n'est pas concernée (lecture
    exactement indépendante de la norme)."""
    inconnues = set(rho_min) - set(LENTILLES_DU_RAPPORT)
    if inconnues:
        raise Arret(f"garde du rapport à ε : lentille(s) hors de la garde ({sorted(inconnues)}) ; notre S n'est pas concernée")
    tenue = {l: le.independance_tenue(v) for l, v in rho_min.items()}
    repli = not all(tenue.values())
    return {"rho_min": {l: float(v) for l, v in rho_min.items()}, "independance_tenue": tenue, "repli": repli,
            "lentilles_refaites": [l for l in K2.LENTILLES_R if repli and l in rho_min],
            "moities": MOTIF_MOITIES_NUL_REFAIT if repli else None,
            "notre_s": "sans objet : lecture exactement indépendante de la norme"}
