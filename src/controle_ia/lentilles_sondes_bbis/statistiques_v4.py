"""Statistiques par direction, lentille et nul — version 4 : la **seconde passe** (statistique corrigée et règle de départage).

Texte : `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (`a2bbed7ac34180b69864f143d1a910c8c29687dc73cca359c85256b6d9b78d15`),
« Métrique », points 6 et 7 ; « Code neuf », brouillon 4. Le texte décide, le code suit.

Ce que ce module change par rapport à `statistiques_v3` (première passe, garde d'égalité à trois étages de l'addendum de
concentration) :
- **règle de départage** (nœud N18 tranché, GO-2026-11-19-92) : toute liste de vingt premiers jetons est faite des vingt premiers
  de l'ordre total « valeur décroissante, puis **identifiant de jeton croissant** » ; les égalités sont exactes, dans la précision
  où la liste est classée (simple précision). La règle est la même pour la direction lue (chaque signe), les directions nulles de
  chaque nul, les témoins, la liste par z, les listes du témoin de couche et la référence « plongements seuls ». Elle ne dépend
  pas de l'ordre dans lequel les jetons sont donnés au code : elle lit les identifiants, non les positions. Le signe − se classe
  sur le score opposé (l'appelant passe −a) : ce n'est pas la liste de v lue à l'envers.
- **listes de dix** : les dix premiers jetons d'un pôle suivent la même règle (égalité lue entre la dixième et la onzième
  valeur) ; les dix pôles sont les dix premiers de l'ordre total « cosinus décroissant, puis **indice de neurone croissant**, puis
  **signe + avant signe −** », classés pour v au signe + ; pour −v, ce sont les mêmes pôles, de signe opposé, sans nouveau
  classement (`poles_opposes`).
- **aucune garde d'égalité** : ni arrêt, ni marque, ni p_bas et p_haut. La valeur p écrite est celle que donne le départage ;
  l'attendu d'une famille sous le nul est la moyenne sur **toutes** les directions nulles.
- **comptes d'égalités écrits** : nombre de listes dont la vingtième et la vingt-et-unième valeur sont égales (la dixième et la
  onzième pour une liste de dix), par (couche, lentille, nul) et par sorte de direction (`ComptesEgalites`). Une égalité ailleurs
  dans le classement ne compte pas. Une liste de moins de vingt-et-un éléments (ou de onze), jouets seulement : « sans objet ».

Repris tels quels, par appel : la statistique corrigée de l'addendum (`statistiques_v2.concentrations_sans_soi`,
`quantiles_sans_soi` : chaque direction nulle jugée sans elle-même, EC-1 et EC-2) ; la comparaison C(u_j) ≥ C(v) en simple
précision (`statistiques_v3.p_concentration`, C5) ; familles, libellés, z, rang empirique, jeton de début, cosinus
(`statistiques_v1`).
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import torch

from . import constantes_v1 as K
from .constantes_v1 import Arret
from . import statistiques_v1 as _origine
from . import statistiques_v2 as _v2
from . import statistiques_v3 as _v3
from .statistiques_v1 import _quantile_par_jeton

LIBELLE_CONCENTREE, LIBELLE_INTERMEDIAIRE, LIBELLE_NON_DISTINCTE = (_origine.LIBELLE_CONCENTREE, _origine.LIBELLE_INTERMEDIAIRE,
                                                                    _origine.LIBELLE_NON_DISTINCTE)
famille_de, masques_familles, libelle, sur_representee = _origine.famille_de, _origine.masques_familles, _origine.libelle, _origine.sur_representee
z_scores, concentrations_temoins, p_temoins, p_empirique = _origine.z_scores, _origine.concentrations_temoins, _origine.p_temoins, _origine.p_empirique
jeton_de_debut, cosinus_colonnes, poles_opposes = _origine.jeton_de_debut, _origine.cosinus_colonnes, _origine.poles_opposes
cosinus, jetons_communs, vecteur_calculable = _origine.cosinus, _origine.jetons_communs, _origine.vecteur_calculable
concentrations_sans_soi, quantiles_sans_soi = _v2.concentrations_sans_soi, _v2.quantiles_sans_soi
p_concentration, paires_de_lignes_egales = _v3.p_concentration, _v3.paires_de_lignes_egales

REGLE_DEPARTAGE = ("valeur décroissante, puis identifiant de jeton croissant (égalités exactes, simple précision) ; "
                   "GO-2026-11-19-92")
REGLE_POLES = "cosinus décroissant, puis indice de neurone croissant, puis signe + avant signe −, pour v au signe +"
SANS_OBJET = "sans objet : liste de moins de k + 1 valeurs (jouets seulement)"
SORTES = ("lue", "nulle", "temoin")
LISTE_PAR_SCORE = "liste par score"


def _identifiants(ids, n: int) -> torch.Tensor:
    t = torch.as_tensor(np.asarray(ids)).to(torch.int64).reshape(-1)
    if t.numel() != n:
        raise Arret("départage : un identifiant par valeur est attendu")
    return t


# --- la règle de départage, pour une liste et pour les colonnes d'une matrice ---------------------------------------------------------
def premiers_departages(valeurs: torch.Tensor, ids, k: int) -> dict:
    """Les `k` premiers d'un vecteur dans l'ordre total « valeur décroissante, puis identifiant croissant ».
    Rend `rangs` (positions dans le vecteur), `valeurs`, `ids`, `objet` (il existe une (k + 1)-ième valeur) et `egalite` (la
    k-ième et la (k + 1)-ième valeur sont égales : c'est le seul cas où le départage choisit qui entre dans la liste)."""
    if valeurs.ndim != 1:
        raise Arret("départage : un vecteur de valeurs est attendu")
    if not bool(torch.isfinite(valeurs).all()):
        raise Arret("valeur non finie dans une lecture ou un nul : arrêt")
    n = int(valeurs.numel())
    idt = _identifiants(ids, n)
    k = min(int(k), n)
    objet = bool(n >= k + 1)
    seuil = valeurs.topk(k).values[-1]
    candidats = torch.nonzero(valeurs >= seuil)[:, 0]           # tous les jetons de valeur au moins égale à la k-ième
    ordre = np.lexsort((idt[candidats].numpy(), -(valeurs[candidats].double().numpy() + 0.0)))
    rangs = candidats[torch.as_tensor(ordre[:k].copy())]
    return {"rangs": rangs, "valeurs": valeurs[rangs], "ids": idt[rangs], "k": k, "objet": objet,
            "egalite": bool(objet and candidats.numel() > k)}


def premiers_departages_colonnes(scores: torch.Tensor, ids, k: int = K.K_JETONS) -> dict:
    """La même règle pour chaque colonne de `scores` `[jetons, n]` : `rangs` et `valeurs` `[k, n]`, `egalite` `[n]`.
    Les colonnes sans égalité à la limite sont tirées d'un seul classement ; celles qui en ont une sont reprises une à une."""
    if scores.ndim != 2:
        raise Arret("départage : une matrice [jetons, directions] est attendue")
    if not bool(torch.isfinite(scores).all()):
        raise Arret("valeur non finie dans une lecture ou un nul : arrêt")
    n_jetons, n = scores.shape
    idt = _identifiants(ids, n_jetons)
    k = min(int(k), n_jetons)
    objet = bool(n_jetons >= k + 1)
    haut = scores.topk(k + 1 if objet else k, dim=0)
    rangs = haut.indices[:k].clone()
    egalite = (haut.values[k - 1] == haut.values[k]) if objet else torch.zeros(n, dtype=torch.bool)
    for j in torch.nonzero(egalite)[:, 0].tolist():
        rangs[:, j] = premiers_departages(scores[:, j], idt, k)["rangs"]
    # ordre dans la liste : identifiant croissant d'abord (tri stable), puis valeur décroissante (tri stable)
    par_id = torch.argsort(idt[rangs], dim=0, stable=True)
    rangs = torch.gather(rangs, 0, par_id)
    valeurs = torch.gather(scores, 0, rangs)
    par_valeur = torch.argsort(valeurs, dim=0, descending=True, stable=True)
    rangs = torch.gather(rangs, 0, par_valeur)
    return {"rangs": rangs, "valeurs": torch.gather(scores, 0, rangs), "k": k, "objet": objet, "egalite": egalite}


def egalites_par_colonne(scores: torch.Tensor, k: int = K.K_JETONS) -> torch.Tensor:
    """Pour chaque colonne : la k-ième et la (k + 1)-ième valeur sont-elles égales ? `[n]`, booléen ; faux si sans objet."""
    return _v3.egalites_par_colonne(scores, k)


# --- comptes d'égalités écrits dans les tables -----------------------------------------------------------------------------------------
@dataclass
class ComptesEgalites:
    """Nombre de listes dont la valeur de rang k et celle de rang k + 1 sont égales. Listes de vingt : par (couche, lentille,
    nul ou liste) et par sorte de direction (lue, nulle, témoin). Listes de dix : pôles par cosinus, par couche et par sorte
    de direction ; jetons d'un pôle, par couche et par lentille. Chaque case porte le nombre de listes vues, le nombre de
    listes à égalité, et le nombre de listes « sans objet » (moins de k + 1 éléments, jouets seulement)."""
    vingt: dict = field(default_factory=dict)
    poles: dict = field(default_factory=dict)
    jetons_pole: dict = field(default_factory=dict)

    @staticmethod
    def _ajouter(case: dict, listes: int, a_egalite: int, sans_objet: bool) -> None:
        case["listes"] = case.get("listes", 0) + int(listes)
        case["a_egalite"] = case.get("a_egalite", 0) + int(a_egalite)
        case["sans_objet"] = case.get("sans_objet", 0) + (int(listes) if sans_objet else 0)

    def liste_de_vingt(self, couche: int, lentille: str, nul: str, sorte: str, listes: int, a_egalite: int,
                       sans_objet: bool = False) -> None:
        if sorte not in SORTES:
            raise Arret(f"compte d'égalités : sorte de direction inconnue ({sorte!r})")
        self._ajouter(self.vingt.setdefault((int(couche), lentille, nul), {}).setdefault(sorte, {}), listes, a_egalite, sans_objet)

    def poles_par_cosinus(self, couche: int, sorte: str, listes: int, a_egalite: int, sans_objet: bool = False) -> None:
        if sorte not in SORTES:
            raise Arret(f"compte d'égalités : sorte de direction inconnue ({sorte!r})")
        self._ajouter(self.poles.setdefault(int(couche), {}).setdefault(sorte, {}), listes, a_egalite, sans_objet)

    def jetons_d_un_pole(self, couche: int, lentille: str, listes: int, a_egalite: int, sans_objet: bool = False) -> None:
        self._ajouter(self.jetons_pole.setdefault((int(couche), lentille), {}), listes, a_egalite, sans_objet)

    def table(self) -> dict:
        """La forme écrite dans les tables (clés en clair ; « sans objet » dit en toutes lettres)."""
        def case(c: dict) -> dict:
            s = {"listes": c["listes"], "a_egalite_a_la_limite": c["a_egalite"], "sans_objet": c["sans_objet"]}
            if c["sans_objet"]:
                s["note"] = SANS_OBJET
            return s
        vingt = {}
        for (couche, lentille, nul), par_sorte in sorted(self.vingt.items()):
            vingt.setdefault(str(couche), {}).setdefault(lentille, {})[nul] = {s: case(c) for s, c in sorted(par_sorte.items())}
        return {"regle": REGLE_DEPARTAGE, "regle_des_poles": REGLE_POLES,
                "listes_de_vingt": vingt,
                "listes_de_dix": {
                    "poles_par_cosinus": {str(c): {s: case(x) for s, x in sorted(p.items())} for c, p in sorted(self.poles.items())},
                    "jetons_d_un_pole": {f"{c}/{l}": case(x) for (c, l), x in sorted(self.jetons_pole.items())}},
                "total_a_egalite": (sum(c["a_egalite"] for p in self.vingt.values() for c in p.values())
                                    + sum(c["a_egalite"] for p in self.poles.values() for c in p.values())
                                    + sum(c["a_egalite"] for c in self.jetons_pole.values()))}


# --- résumé d'un nul ------------------------------------------------------------------------------------------------------------------
@dataclass
class ResumeNul:
    """Résumé des M directions nulles d'un nul, pour une lentille. Moyenne, écart type et quantile : sur les M directions
    (direction lue, témoins, z des tables). Concentration, part et familles de chaque direction nulle : sans elle-même, sur
    ses vingt premiers jetons départagés. `rangs_premiers` porte ces vingt premiers (positions parmi les jetons gardés) : ce
    sont eux qui portent les p de recouvrement."""
    moyenne: torch.Tensor          # [jetons]
    ecart_type: torch.Tensor       # [jetons]
    quantile: torch.Tensor         # [jetons], quantile 0,99 des M scores nuls du jeton
    concentration: torch.Tensor    # [M], C(u_j) sans elle-même, simple précision
    compte_part: torch.Tensor      # [M], entier : nombre des k premiers jetons de u_j au-dessus du quantile des M − 1 autres
    familles: dict                 # nom → [M], compte dans les k premiers jetons de u_j
    egalite: torch.Tensor          # [M], booléen : k-ième et (k + 1)-ième score de u_j égaux
    rangs_premiers: torch.Tensor   # [k, M]
    k: int = K.K_JETONS
    sans_objet: bool = False

    @property
    def m(self) -> int:
        return int(self.concentration.numel())

    @property
    def n_egalites(self) -> int:
        return int(self.egalite.sum())

    @property
    def part(self) -> torch.Tensor:
        return self.compte_part.to(torch.float32) / self.k


def resumer_nul(scores_nuls: torch.Tensor, masques: dict[str, torch.Tensor], ids_gardes, k: int = K.K_JETONS) -> ResumeNul:
    """Résumé des scores `[jetons, M]` des M directions nulles, listes départagées. La règle vaut pour toute lentille : la
    fonction ne connaît que des scores."""
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
    haut = premiers_departages_colonnes(scores_nuls, ids_gardes, k)
    rangs, valeurs = haut["rangs"], haut["valeurs"]
    compte = (valeurs > quantiles_sans_soi(scores_nuls, rangs, valeurs)).sum(0).to(torch.int64)
    familles = {nom: m[rangs].sum(0).to(torch.int64) for nom, m in masques.items()}
    return ResumeNul(moyenne, ecart, quantile, concentration, compte, familles, haut["egalite"], rangs, haut["k"], not haut["objet"])


# --- une direction à un signe ----------------------------------------------------------------------------------------------------------
def lecture_signe(a: torch.Tensor, nuls: dict[str, tuple[torch.Tensor, ResumeNul]], masques: dict[str, torch.Tensor],
                  ids_gardes: np.ndarray, k: int = K.K_JETONS) -> dict:
    """Tables d'une direction à un signe : `a` `[jetons]` est le score au signe voulu (**−a pour le signe −** : la liste du
    signe − est classée sur le score opposé, puis identifiant croissant). `nuls` : nom du nul → (scores nuls, résumé).
    Aucune égalité n'arrête : la liste est départagée, et l'égalité à la limite est écrite."""
    if not bool(torch.isfinite(a).all()):
        raise Arret("valeur non finie dans une lecture : arrêt")
    for nom_nul, (_, resume) in nuls.items():
        if resume.k != min(int(k), a.numel()) or set(resume.familles) != set(masques):
            raise Arret(f"nul {nom_nul} résumé sur {resume.k} premiers jetons ou d'autres familles que la direction")
    haut = premiers_departages(a, ids_gardes, k)
    rangs, k = haut["rangs"], haut["k"]
    sortie = {"premiers_par_score": {"rangs_gardes": rangs.tolist(), "ids": haut["ids"].tolist(),
                                    "scores": [float(x) for x in haut["valeurs"]]},
              "egalite_a_la_limite": {"par_score": haut["egalite"], "par_z": {}, "sans_objet": not haut["objet"],
                                      "note": SANS_OBJET if not haut["objet"] else None},
              "nuls": {}, "familles": {nom: {"n": int(m[rangs].sum())} for nom, m in masques.items()}}
    for nom_nul, (scores_nuls, resume) in nuls.items():
        z = z_scores(a, resume)
        c = z.max()
        compte = int((a[rangs] > resume.quantile[rangs]).sum())
        rang_empirique = (1 + (scores_nuls[rangs] > a[rangs][:, None]).sum(1)).tolist()
        t = {"z_des_premiers": [float(x) for x in z[rangs]], "rang_empirique_des_premiers": [int(x) for x in rang_empirique],
             "concentration": float(c), "p_concentration": p_concentration(resume.concentration, c),
             "part": compte / k, "p_part": p_empirique(resume.compte_part, compte), "m": resume.m,
             "directions_nulles_a_egalite_a_la_limite": resume.n_egalites, "familles": {}}
        for nom, masque in masques.items():
            n = int(masque[rangs].sum())
            t["familles"][nom] = {"n": n, "attendu": float(resume.familles[nom].double().mean()),
                                  "p": p_empirique(resume.familles[nom], n)}
        if nom_nul in (K.NUL_ISOTROPE, K.NUL_ISOTROPE_PAR_DIRECTION):
            hz = premiers_departages(z, ids_gardes, k)
            t["premiers_par_z"] = {"rangs_gardes": hz["rangs"].tolist(), "ids": hz["ids"].tolist(),
                                   "z": [float(x) for x in hz["valeurs"]]}
            sortie["egalite_a_la_limite"]["par_z"][nom_nul] = hz["egalite"]
        sortie["nuls"][nom_nul] = t
    sortie["jeton_de_debut"] = jeton_de_debut(a, ids_gardes, rangs)
    return sortie


# --- pôles alignés (point 7) -----------------------------------------------------------------------------------------------------------
def ordre_des_poles(cos: torch.Tensor, k: int = K.K_POLES) -> dict:
    """Les `k` premiers pôles de l'ordre total « cosinus décroissant, puis indice de neurone croissant, puis signe + avant
    signe − ». `cos` `[neurones]` : cosinus de v avec chaque colonne (pôle +) ; le pôle − a le cosinus opposé."""
    if cos.ndim != 1 or not bool(torch.isfinite(cos).all()):
        raise Arret("valeur non finie dans les pôles alignés : arrêt")
    f = int(cos.numel())
    signes = torch.cat([cos, -cos])                       # pôles (n, +) puis (n, −)
    k = min(int(k), 2 * f)
    objet = bool(2 * f >= k + 1)
    seuil = signes.topk(k).values[-1]
    candidats = torch.nonzero(signes >= seuil)[:, 0].numpy()
    neurone, moins = candidats % f, (candidats >= f).astype(np.int64)
    ordre = np.lexsort((moins, neurone, -(signes.numpy()[candidats].astype(np.float64) + 0.0)))[:k]
    choisis = candidats[ordre]
    return {"neurones": [int(i % f) for i in choisis], "signes": ["+" if int(i) < f else "-" for i in choisis],
            "cosinus": [float(signes[int(i)]) for i in choisis], "k": k, "objet": objet,
            "egalite": bool(objet and candidats.size > k)}


def poles_alignes(v: torch.Tensor, w_down: torch.Tensor, nuls: dict[str, torch.Tensor], k: int = K.K_POLES) -> dict:
    """Les dix pôles de v (signe +) dans l'ordre total du point 7, le rang de chacun parmi les maxima nuls, la concentration
    des pôles (cosinus maximal) et son p sous chaque nul. La concentration et son rang n'emploient aucune liste : inchangés."""
    normes = w_down.norm(dim=0)
    cos = cosinus_colonnes(v, w_down, normes)[:, 0]
    maxima = {nom: cosinus_colonnes(u, w_down, normes).abs().max(0).values for nom, u in nuls.items()}
    if not bool(torch.isfinite(cos).all()) or not all(bool(torch.isfinite(m).all()) for m in maxima.values()):
        raise Arret("valeur non finie dans les pôles alignés : arrêt")
    o = ordre_des_poles(cos, k)
    poles = [{"neurone": n, "signe": s, "cosinus": c,
              "rang_parmi_maxima_nuls": {nom: int((m > c).sum()) + 1 for nom, m in maxima.items()}}
             for n, s, c in zip(o["neurones"], o["signes"], o["cosinus"])]
    c_max = float(cos.abs().max())
    return {"poles": poles, "concentration": c_max, "p": {nom: p_empirique(m, c_max) for nom, m in maxima.items()},
            "maxima_nuls": dict(maxima), "egalite_a_la_limite": o["egalite"], "sans_objet": not o["objet"]}


def premiers_jetons_d_un_pole(scores: torch.Tensor, ids_gardes, k: int = K.K_JETONS_POLE) -> dict:
    """Les dix premiers jetons de la lecture d'un pôle, par toute lentille qui le lit : règle du point 6, l'égalité lue entre
    la dixième et la onzième valeur."""
    h = premiers_departages(scores, ids_gardes, k)
    return {"rangs_gardes": h["rangs"].tolist(), "ids": h["ids"].tolist(), "scores": [float(x) for x in h["valeurs"]],
            "egalite_a_la_limite": h["egalite"], "sans_objet": not h["objet"]}
