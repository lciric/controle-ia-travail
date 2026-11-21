"""Statistiques par direction, lentille et nul — version 3 : le code de l'addendum de concentration **scellé**.

Texte : `prereg/lecture-sondes-bbis-par-lentilles-v1.md` (`ca5066d7…`), corrigé par l'addendum scellé
`prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`
(`7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970`). Le texte décide, le code suit.

Depuis `statistiques_v2` (dont les formules de EC-1 et de EC-2 sont reprises telles quelles, par appel) :
- **EC-6, garde d'égalité au vingtième rang, option 3** (GO-2026-11-19-78) : le code relève les vingt-et-un plus grandes
  valeurs de chaque liste de vingt premiers ; il y a égalité au vingtième rang quand la vingtième et la vingt-et-unième sont
  égales, par égalité exacte, dans la précision où la liste est classée (simple précision). Une égalité ailleurs ne compte pas.
  (i) direction lue : arrêt nommé (`EgaliteDirectionLue`) ; (ii) direction nulle : marquée ; S_min et S_max de chaque
  statistique qui dépend des vingt premiers (part au-dessus du nul, compte de chaque famille) ; p_bas et p_haut ; la valeur p
  écrite est p_haut ; l'attendu d'une famille est la moyenne sur les seules directions non marquées ; libellé calculé aux deux
  bornes, arrêt nommé (`EgaliteNulleDecisive`) s'ils diffèrent ; (iii) témoin : compté, sans arrêt.
- **C5** : C(u_j), calculé en double précision, est rendu en simple précision comme C(v) ; la comparaison C(u_j) ≥ C(v) se
  fait en simple précision, une égalité compte contre v (`p_concentration`).
- La part au-dessus du nul est tenue par son **compte** entier (nombre des vingt premiers jetons au-dessus du quantile) : la
  comparaison P(u_j) ≥ P(v) se fait sur les comptes, à k égal ; la part écrite est le compte divisé par k.
Inchangés et repris de `statistiques_v1` : familles, libellés, z, rang empirique, jeton de début, cosinus, comparaisons ;
la moyenne, l'écart type et le quantile des M directions pour la direction lue et les témoins (addendum, § 4, points 2 et 3).
Une liste de moins de vingt-et-un jetons (jouets seulement) n'a pas de vingt-et-unième valeur : garde sans objet, écrit.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass

import numpy as np
import torch

from . import constantes_v1 as K
from .constantes_v1 import Arret
from . import statistiques_v1 as _origine
from . import statistiques_v2 as _v2
from .statistiques_v1 import _quantile_par_jeton

# Repris tels quels de `statistiques_v1` (inchangés par l'addendum, § 5).
LIBELLE_CONCENTREE, LIBELLE_INTERMEDIAIRE, LIBELLE_NON_DISTINCTE = (_origine.LIBELLE_CONCENTREE, _origine.LIBELLE_INTERMEDIAIRE,
                                                                    _origine.LIBELLE_NON_DISTINCTE)
famille_de, masques_familles, libelle, sur_representee = _origine.famille_de, _origine.masques_familles, _origine.libelle, _origine.sur_representee
z_scores, concentrations_temoins, p_temoins = _origine.z_scores, _origine.concentrations_temoins, _origine.p_temoins
jeton_de_debut, cosinus_colonnes, poles_opposes = _origine.jeton_de_debut, _origine.cosinus_colonnes, _origine.poles_opposes
cosinus, jetons_communs, vecteur_calculable = _origine.cosinus, _origine.jetons_communs, _origine.vecteur_calculable
# Repris tels quels de `statistiques_v2` (formules de EC-1 et de EC-2).
concentrations_sans_soi, quantiles_sans_soi = _v2.concentrations_sans_soi, _v2.quantiles_sans_soi

# --- messages nommés de la « Liste d'arrêt » (addendum, EC-6) -----------------------------------------------------------------------
MESSAGE_EGALITE_LUE = "égalité de score au vingtième rang d'une direction lue"
MESSAGE_EGALITE_NULLE = "égalité au vingtième rang d'une direction nulle, décisive pour un libellé"
LISTE_PAR_SCORE = "vingt premiers jetons par score"
LISTE_PAR_Z = "vingt premiers jetons par z sous le nul {nul}"
LISTE_TEMOIN_DE_COUCHE = "vingt premiers jetons du témoin de couche, lecture à la couche {couche}"
LISTE_POLES = "dix pôles par cosinus (égalité lue entre la dixième et la onzième valeur)"
LISTE_JETONS_POLE = ("dix premiers jetons de la lecture du pôle (neurone {neurone}, signe {signe}) (égalité lue entre la "
                     "dixième et la onzième valeur)")
SANS_OBJET = "garde d'égalité sans objet : liste de moins de k + 1 valeurs (jouets seulement)"
CHAMPS_CONTEXTE = ("cellule", "pli", "role", "vecteur", "signe", "lentille", "couche")
NOMS_CONTEXTE = {"cellule": "cellule", "pli": "pli", "role": "rôle", "vecteur": "vecteur", "signe": "signe",
                 "lentille": "lentille", "couche": "couche"}


def _ou(contexte: dict | None) -> str:
    c = contexte or {}
    return ", ".join(f"{NOMS_CONTEXTE[n]} {c.get(n, 'non précisé')}" for n in CHAMPS_CONTEXTE)


class EgaliteDirectionLue(Arret):
    """EC-6, étage (i) : égalité au vingtième rang d'une liste d'une direction lue (ou au dixième rang d'une liste de dix des
    pôles) : arrêt du calcul avant toute écriture de table ; nœud."""

    def __init__(self, liste: str, identifiants: tuple, valeur: float, contexte: dict | None = None):
        self.liste, self.identifiants, self.valeur, self.contexte = liste, tuple(identifiants), float(valeur), dict(contexte or {})
        super().__init__(f"{MESSAGE_EGALITE_LUE} : {_ou(contexte)}, liste « {liste} », identifiants {identifiants[0]} et "
                         f"{identifiants[1]}, valeur commune {float(valeur)!r} : arrêt avant toute écriture de table ; nœud")


class EgaliteNulleDecisive(Arret):
    """EC-6, étage (ii) : le libellé calculé avec p_bas sous les deux nuls diffère de celui calculé avec p_haut : arrêt ; nœud."""

    def __init__(self, statistique: str, par_nul: dict, libelle_bas, libelle_haut, contexte: dict | None = None):
        self.statistique, self.par_nul, self.contexte = statistique, dict(par_nul), dict(contexte or {})
        self.libelle_bas, self.libelle_haut = libelle_bas, libelle_haut
        detail = " ; ".join(f"nul {nul} : p_bas {d['p_bas']!r}, p_haut {d['p_haut']!r}, {d['marquees']} direction(s) nulle(s) "
                            "marquée(s)" for nul, d in sorted(par_nul.items()))
        super().__init__(f"{MESSAGE_EGALITE_NULLE} : direction lue : {_ou(contexte)} ; statistique « {statistique} » ; {detail} ; "
                         f"libellé à p_bas : {libelle_bas!r} ; libellé à p_haut : {libelle_haut!r} : arrêt ; nœud")


# --- garde d'égalité au rang k d'une liste de k premiers ----------------------------------------------------------------------------
def premiers_gardes(valeurs: torch.Tensor, k: int) -> dict:
    """Les `k` plus grandes valeurs d'un vecteur et leurs rangs, avec le relevé de la garde : `objet` (il existe une valeur de
    rang k + 1), `egalite` (la k-ième et la (k + 1)-ième valeur sont égales, par égalité exacte, dans la précision du vecteur),
    et, s'il y a égalité, les deux rangs et la valeur commune. Ne décide rien : l'appelant arrête, marque ou compte."""
    if valeurs.ndim != 1:
        raise Arret("garde d'égalité : un vecteur de valeurs est attendu")
    k = min(int(k), int(valeurs.numel()))
    objet = bool(valeurs.numel() >= k + 1)
    haut = valeurs.topk(k + 1 if objet else k)
    egalite = bool(objet and haut.values[k - 1] == haut.values[k])
    return {"valeurs": haut.values[:k], "rangs": haut.indices[:k], "k": k, "objet": objet, "egalite": egalite,
            "rangs_a_egalite": (int(haut.indices[k - 1]), int(haut.indices[k])) if egalite else None,
            "valeur_commune": float(haut.values[k]) if egalite else None}


def exiger_sans_egalite(valeurs: torch.Tensor, k: int, liste: str, identifiants, contexte: dict | None = None) -> dict:
    """Étage (i) : liste d'une direction lue. Égalité au rang k : arrêt nommé, qui rend les deux identifiants et la valeur
    commune. `identifiants` : fonction (ou tableau) qui rend l'identifiant d'un rang."""
    g = premiers_gardes(valeurs, k)
    if g["egalite"]:
        nom = identifiants if callable(identifiants) else (lambda i: int(identifiants[i]))
        raise EgaliteDirectionLue(liste, tuple(nom(i) for i in g["rangs_a_egalite"]), g["valeur_commune"], contexte)
    return g


def egalites_par_colonne(scores: torch.Tensor, k: int = K.K_JETONS) -> torch.Tensor:
    """Pour chaque colonne de `scores` `[jetons, n]` : y a-t-il égalité au rang k de sa liste par score ? `[n]`, booléen ;
    tout faux si la liste a moins de k + 1 valeurs (garde sans objet)."""
    k = min(int(k), scores.shape[0])
    if scores.shape[0] < k + 1:
        return torch.zeros(scores.shape[1], dtype=torch.bool)
    haut = scores.topk(k + 1, dim=0).values
    return haut[k - 1] == haut[k]


def egalites_temoins(scores_temoins: torch.Tensor, k: int = K.K_JETONS) -> dict:
    """Étage (iii) : nombre de témoins à égalité au vingtième rang ; pas d'arrêt ; le compte de calibration n'en dépend pas."""
    k_eff = min(int(k), scores_temoins.shape[0])
    return {"temoins": int(scores_temoins.shape[1]), "a_egalite_au_vingtieme_rang": int(egalites_par_colonne(scores_temoins, k).sum()),
            "garde_sans_objet": bool(scores_temoins.shape[0] < k_eff + 1)}


def paires_de_lignes_egales(lignes: np.ndarray) -> dict:
    """Addendum, EC-6 (couple H2) : nombre de paires de jetons gardés dont les lignes de `lm_head.weight` sont égales octet
    pour octet. Écrit au montage, sans arrêt. `lignes` : les lignes gardées, dans la précision où elles sont chargées (la
    conversion de bfloat16 en simple précision est exacte et ne confond pas deux lignes d'octets différents)."""
    a = np.ascontiguousarray(lignes)
    if a.ndim != 2:
        raise Arret("lignes de sortie : une matrice [jetons, largeur] est attendue")
    par_empreinte: dict[bytes, list[int]] = {}
    for i in range(a.shape[0]):                             # une empreinte par ligne : aucune copie de la matrice
        par_empreinte.setdefault(hashlib.sha256(a[i].tobytes()).digest(), []).append(i)
    tailles = []
    for candidats in par_empreinte.values():
        if len(candidats) > 1:                              # l'égalité est vérifiée octet pour octet, non sur la seule empreinte
            par_octets: dict[bytes, int] = {}
            for i in candidats:
                cle = a[i].tobytes()
                par_octets[cle] = par_octets.get(cle, 0) + 1
            tailles += [n for n in par_octets.values() if n > 1]
    groupes = np.asarray(tailles, dtype=np.int64)
    return {"jetons": int(a.shape[0]), "paires_de_lignes_egales_octet_pour_octet": int((groupes * (groupes - 1) // 2).sum()),
            "groupes_de_lignes_egales": int(groupes.size), "jetons_dans_un_groupe": int(groupes.sum())}


# --- résumé d'un nul ------------------------------------------------------------------------------------------------------------------
@dataclass
class ResumeNul:
    """Résumé des M directions nulles d'un nul, pour une lentille. Moyenne, écart type et quantile : sur les M directions
    (direction lue, témoins, z des tables). Concentration, part et familles de chaque direction nulle : sans elle-même
    (EC-1, EC-2). Pour une direction marquée (égalité au vingtième rang), `*_min` et `*_max` sont S_min et S_max ; pour une
    direction non marquée, les deux sont égales à S."""
    moyenne: torch.Tensor          # [jetons]
    ecart_type: torch.Tensor       # [jetons]
    quantile: torch.Tensor         # [jetons], quantile 0,99 des M scores nuls du jeton
    concentration: torch.Tensor    # [M], C(u_j) sans elle-même, simple précision
    compte_part_min: torch.Tensor  # [M], entier : nombre des k premiers jetons de u_j au-dessus du quantile des M − 1 autres
    compte_part_max: torch.Tensor  # [M]
    familles_min: dict             # nom → [M], compte dans les k premiers jetons de u_j
    familles_max: dict
    marquee: torch.Tensor          # [M], booléen : égalité au rang k de la liste par score de u_j
    k: int = K.K_JETONS
    garde_sans_objet: bool = False  # moins de k + 1 jetons : pas de (k + 1)-ième valeur

    @property
    def m(self) -> int:
        return int(self.concentration.numel())

    @property
    def n_marquees(self) -> int:
        return int(self.marquee.sum())

    @property
    def part_min(self) -> torch.Tensor:
        return self.compte_part_min.to(torch.float32) / self.k

    @property
    def part_max(self) -> torch.Tensor:
        return self.compte_part_max.to(torch.float32) / self.k


def bornes_min_max(base: int, places: int, egaux_a_un: int, egaux: int) -> tuple[int, int]:
    """S_min et S_max d'un compte : `base` vient des jetons de score strictement plus grand que le k-ième ; `places` places
    restent à donner, de toutes les façons possibles, aux `egaux` jetons de score égal au k-ième, dont `egaux_a_un` comptent
    pour 1 et les autres pour 0."""
    return base + max(0, places - (egaux - egaux_a_un)), base + min(places, egaux_a_un)


def bornes_de_departage(scores_nuls: torch.Tensor, j: int, k: int, masques: dict[str, torch.Tensor]) -> dict:
    """S_min et S_max de la direction nulle marquée `j` (colonne), pour la part au-dessus du nul (en compte) et pour le compte
    de chaque famille : la plus petite et la plus grande valeur quand les places des k premiers que laissent les jetons de
    score strictement plus grand que le k-ième sont données, de toutes les façons possibles, aux jetons de score égal au
    k-ième (addendum, EC-6, étage (ii))."""
    colonne = scores_nuls[:, j]
    seuil = colonne.topk(k).values[-1]
    plus = torch.nonzero(colonne > seuil)[:, 0]
    egaux = torch.nonzero(colonne == seuil)[:, 0]
    places = k - int(plus.numel())
    if places < 1 or int(egaux.numel()) <= places:
        raise Arret("bornes de départage demandées pour une direction nulle sans égalité au rang k")
    jetons = torch.cat([plus, egaux])
    valeurs = colonne[jetons]
    depasse = valeurs > quantiles_sans_soi(scores_nuls, jetons[:, None], valeurs[:, None])[:, 0]
    g, e = int(plus.numel()), int(egaux.numel())
    sortie = {"part": bornes_min_max(int(depasse[:g].sum()), places, int(depasse[g:].sum()), e), "familles": {},
              "jetons_plus_grands": g, "jetons_a_egalite": e, "places": places}
    for nom, masque in masques.items():
        sortie["familles"][nom] = bornes_min_max(int(masque[plus].sum()), places, int(masque[egaux].sum()), e)
    return sortie


def resumer_nul(scores_nuls: torch.Tensor, masques: dict[str, torch.Tensor], k: int = K.K_JETONS) -> ResumeNul:
    """Résumé des scores `[jetons, M]` des M directions nulles. Les directions nulles à égalité au rang k sont marquées, et
    leurs S_min et S_max calculés ; aucune n'arrête à elle seule."""
    if not bool(torch.isfinite(scores_nuls).all()):
        raise Arret("valeur non finie dans un nul : arrêt")
    moyenne = scores_nuls.mean(1)
    ecart = scores_nuls.std(1, correction=0)
    if not bool((ecart > 0).all()):
        raise Arret("écart type nul d'un jeton sous un nul : z non fini : arrêt")
    quantile = _quantile_par_jeton(scores_nuls, K.QUANTILE_PART)
    concentration = concentrations_sans_soi(scores_nuls)
    if concentration.dtype != torch.float32:
        raise Arret("concentration des directions nulles : simple précision attendue pour la comparaison à C(v)")
    k = min(int(k), scores_nuls.shape[0])
    objet = bool(scores_nuls.shape[0] >= k + 1)
    haut = scores_nuls.topk(k + 1 if objet else k, dim=0)
    valeurs, rangs = haut.values[:k], haut.indices[:k]
    marquee = (haut.values[k - 1] == haut.values[k]) if objet else torch.zeros(scores_nuls.shape[1], dtype=torch.bool)
    compte = (valeurs > quantiles_sans_soi(scores_nuls, rangs, valeurs)).sum(0).to(torch.int64)
    familles = {nom: m[rangs].sum(0).to(torch.int64) for nom, m in masques.items()}
    compte_min, compte_max = compte.clone(), compte.clone()
    familles_min, familles_max = {n: c.clone() for n, c in familles.items()}, {n: c.clone() for n, c in familles.items()}
    for j in torch.nonzero(marquee)[:, 0].tolist():
        b = bornes_de_departage(scores_nuls, j, k, masques)
        compte_min[j], compte_max[j] = b["part"]
        for nom in masques:
            familles_min[nom][j], familles_max[nom][j] = b["familles"][nom]
    return ResumeNul(moyenne, ecart, quantile, concentration, compte_min, compte_max, familles_min, familles_max, marquee, k,
                     not objet)


# --- valeurs p -------------------------------------------------------------------------------------------------------------------------
def p_concentration(concentrations_nulles: torch.Tensor, c: torch.Tensor | float) -> float:
    """p = (1 + #{j : C(u_j) ≥ C(v)}) / (M + 1), la comparaison faite **en simple précision** (addendum, EC-1, couple C5) :
    C(u_j) et C(v) sont ramenés en simple précision avant d'être comparés ; une égalité compte contre v."""
    nulles = torch.as_tensor(concentrations_nulles)
    if nulles.dtype != torch.float32:
        raise Arret("concentration des directions nulles : simple précision attendue pour la comparaison à C(v)")
    c32 = torch.as_tensor(c, dtype=torch.float32)
    return float((1 + int((nulles >= c32).sum())) / (nulles.numel() + 1))


def p_bornes(s_min: torch.Tensor, s_max: torch.Tensor, valeur: int) -> tuple[float, float]:
    """(p_bas, p_haut) d'une statistique entière S qui dépend des vingt premiers jetons :
    p_bas = (1 + #{j : S_min(u_j) ≥ S(v)}) / (M + 1) et p_haut = (1 + #{j : S_max(u_j) ≥ S(v)}) / (M + 1) ; pour une direction
    non marquée S_min = S = S_max, de sorte que les deux formules sont celles de l'addendum (EC-6, étage (ii))."""
    m = int(s_min.numel())
    return (float((1 + int((s_min >= int(valeur)).sum())) / (m + 1)), float((1 + int((s_max >= int(valeur)).sum())) / (m + 1)))


def attendu_sans_les_marquees(comptes: torch.Tensor, marquee: torch.Tensor) -> float:
    """Attendu sous le nul d'une famille : moyenne de ses comptes sur les seules directions non marquées. Si toutes les
    directions du nul sont marquées, cette moyenne n'existe pas : valeur non finie dans un nul, arrêt (« Liste d'arrêt »)."""
    libres = comptes[~marquee]
    if not libres.numel():
        raise Arret("attendu d'une famille : toutes les directions nulles sont marquées : valeur non finie dans un nul : arrêt")
    return float(libres.double().mean())


# --- une direction à un signe ----------------------------------------------------------------------------------------------------------
def lecture_signe(a: torch.Tensor, nuls: dict[str, tuple[torch.Tensor, ResumeNul]], masques: dict[str, torch.Tensor],
                  ids_gardes: np.ndarray, k: int = K.K_JETONS, contexte: dict | None = None) -> dict:
    """Tables d'une direction à un signe : `a` `[jetons]` est le score au signe voulu (−a pour le signe −) ; `nuls` : nom du
    nul → (scores nuls `[jetons, M]`, résumé). Une égalité au rang k de la liste par score, ou de la liste par z sous un nul
    isotrope : arrêt nommé (EC-6, étage (i)). Sous chaque nul, la valeur p écrite pour la part et pour chaque famille est
    p_haut ; p_bas est écrit à côté, avec le nombre de directions nulles marquées."""
    if not bool(torch.isfinite(a).all()):
        raise Arret("valeur non finie dans une lecture : arrêt")
    k = min(int(k), a.numel())
    for nom_nul, (_, resume) in nuls.items():
        if resume.k != k or set(resume.familles_min) != set(masques):
            raise Arret(f"nul {nom_nul} résumé sur {resume.k} premiers jetons ou d'autres familles que la direction ({k})")
    haut = exiger_sans_egalite(a, k, LISTE_PAR_SCORE, ids_gardes, contexte)
    rangs = haut["rangs"]
    sortie = {"premiers_par_score": {"rangs_gardes": rangs.tolist(), "ids": [int(ids_gardes[i]) for i in rangs.tolist()],
                                    "scores": [float(x) for x in haut["valeurs"]]},
              "garde_egalite": {"sans_objet": not haut["objet"], "note": SANS_OBJET if not haut["objet"] else None},
              "nuls": {}, "familles": {nom: {"n": int(m[rangs].sum())} for nom, m in masques.items()}}
    for nom_nul, (scores_nuls, resume) in nuls.items():
        z = z_scores(a, resume)
        c = z.max()
        compte = int((a[rangs] > resume.quantile[rangs]).sum())
        p_part_bas, p_part_haut = p_bornes(resume.compte_part_min, resume.compte_part_max, compte)
        rang_empirique = (1 + (scores_nuls[rangs] > a[rangs][:, None]).sum(1)).tolist()
        t = {"z_des_premiers": [float(x) for x in z[rangs]], "rang_empirique_des_premiers": [int(x) for x in rang_empirique],
             "concentration": float(c), "p_concentration": p_concentration(resume.concentration, c),
             "part": compte / k, "p_part": p_part_haut, "p_part_bas": p_part_bas, "p_part_haut": p_part_haut, "m": resume.m,
             "directions_nulles_marquees": resume.n_marquees, "familles": {}}
        for nom, masque in masques.items():
            n = int(masque[rangs].sum())
            p_bas, p_haut = p_bornes(resume.familles_min[nom], resume.familles_max[nom], n)
            t["familles"][nom] = {"n": n, "attendu": attendu_sans_les_marquees(resume.familles_max[nom], resume.marquee),
                                  "p": p_haut, "p_bas": p_bas, "p_haut": p_haut}
        if nom_nul in (K.NUL_ISOTROPE, K.NUL_ISOTROPE_PAR_DIRECTION):
            hz = exiger_sans_egalite(z, k, LISTE_PAR_Z.format(nul=nom_nul), ids_gardes, contexte)
            t["premiers_par_z"] = {"rangs_gardes": hz["rangs"].tolist(), "ids": [int(ids_gardes[i]) for i in hz["rangs"].tolist()],
                                   "z": [float(x) for x in hz["valeurs"]]}
        sortie["nuls"][nom_nul] = t
    sortie["jeton_de_debut"] = jeton_de_debut(a, ids_gardes, rangs)
    return sortie


# --- libellés sous les deux bornes (EC-6, étage (ii)) -------------------------------------------------------------------------------------
def libelle_sous_departage(regle, statistique: str, bornes_par_nul: dict, contexte: dict | None = None):
    """Le libellé (« Seuil ») est calculé deux fois, avec p_bas sous les deux nuls puis avec p_haut sous les deux nuls.
    Égaux : le libellé est celui-là. Différents : arrêt nommé. `regle(p_isotrope, p_signes)` : `libelle` ou
    `sur_representee` ; `bornes_par_nul` : {« isotrope » : (nom du nul, p_bas, p_haut, marquées), « signes » : (…)}."""
    (nul_i, bas_i, haut_i, n_i), (nul_s, bas_s, haut_s, n_s) = bornes_par_nul["isotrope"], bornes_par_nul["signes"]
    a_bas, a_haut = regle(bas_i, bas_s), regle(haut_i, haut_s)
    if a_bas != a_haut:
        raise EgaliteNulleDecisive(statistique, {nul_i: {"p_bas": bas_i, "p_haut": haut_i, "marquees": n_i},
                                                 nul_s: {"p_bas": bas_s, "p_haut": haut_s, "marquees": n_s}}, a_bas, a_haut,
                                   contexte)
    return a_haut


# --- pôles alignés (point 7) -----------------------------------------------------------------------------------------------------------
def poles_alignes(v: torch.Tensor, w_down: torch.Tensor, nuls: dict[str, torch.Tensor], k: int = K.K_POLES,
                  contexte: dict | None = None) -> dict:
    """Les dix pôles de plus grand cosinus avec v (signe +), le rang de chacun parmi les maxima nuls, la concentration des
    pôles (cosinus maximal) et son p sous chaque nul. Une égalité entre le dixième et le onzième cosinus : arrêt nommé (EC-6,
    étage (i), couple G3). La concentration des pôles et son p n'emploient aucune liste de premiers : inchangés."""
    normes = w_down.norm(dim=0)
    cos = cosinus_colonnes(v, w_down, normes)[:, 0]
    signes = torch.cat([cos, -cos])                       # pôles (n, +) puis (n, −)
    f = cos.numel()
    maxima = {nom: cosinus_colonnes(u, w_down, normes).abs().max(0).values for nom, u in nuls.items()}
    if not bool(torch.isfinite(cos).all()) or not all(bool(torch.isfinite(m).all()) for m in maxima.values()):
        raise Arret("valeur non finie dans les pôles alignés : arrêt")
    haut = exiger_sans_egalite(signes, k, LISTE_POLES, lambda i: f"neurone {int(i) % f} signe {'+' if int(i) < f else '-'}",
                               contexte)
    poles = [{"neurone": int(i % f), "signe": "+" if int(i) < f else "-", "cosinus": float(c),
              "rang_parmi_maxima_nuls": {nom: int((m > c).sum()) + 1 for nom, m in maxima.items()}}
             for c, i in zip(haut["valeurs"], haut["rangs"])]
    c_max = float(cos.abs().max())
    return {"poles": poles, "concentration": c_max, "p": {nom: _origine.p_empirique(m, c_max) for nom, m in maxima.items()},
            "maxima_nuls": {nom: m for nom, m in maxima.items()}, "garde_egalite_sans_objet": not haut["objet"]}
