"""Papier C — stabilité de rang : C-P3a, C-P3b, C-P3c, dans leurs deux versions (v1).

Texte de référence : version r1 (`e12f16fa…`), section « Prédiction », bloc « Stabilité de rang » (lignes 550 à 602),
section « Seuil » (lignes 940 à 942), tableau de la stabilité de rang des « Critères de lecture gelés ».

Deux versions, choisies par la configuration (champ `stabilite_rang.version`), sans changer le code :
- version « a » : trois lectures de la loi nette (calibrée ; sans calibrage ; calibrée par ρ̂/r̂) ; « établie »
  seulement si les trois concluent ; une statistique nommée par la clause de repli est « rapportée sans verdict » ;
- version « b » (repli écrit d'avance, lettre de P-021) : deux lectures (calibrée ; sans calibrage) ; C-P3a et C-P3b
  « rapportées sans verdict » ; C-P3c garde le verdict du tableau, à deux lectures, sous la clause de repli.
Dans les deux cas les statistiques sont calculées aux trois lectures et écrites (ligne 573).

Aucune réfutation n'existe pour ces trois lignes : « établie », « non établie », ou « rapportée sans verdict ».
"""
from __future__ import annotations

import itertools

import numpy as np

from papier_c_erreurs_v1 import ConfigurationInvalide
from papier_c_reechantillonnage_v1 import p_depassement

LECTURES_VERSION = {"a": ("calibree", "sans_calibrage", "rho_sur_r"), "b": ("calibree", "sans_calibrage")}
TOUTES_LES_LECTURES = ("calibree", "sans_calibrage", "rho_sur_r")
ETABLIE, NON_ETABLIE, SANS_VERDICT = "établie", "non établie", "rapportée sans verdict"
MENTION_GRILLE = "niveau non vérifié sur la grille"


def rangs_des_objets(valeurs) -> np.ndarray:
    """Rangs (1 = plus petit) le long du dernier axe ; égalités : rang moyen. Vectorisé."""
    v = np.asarray(valeurs, dtype=np.float64)
    plus_petits = (v[..., None, :] < v[..., :, None]).sum(-1)
    egaux = (v[..., None, :] == v[..., :, None]).sum(-1) - 1
    return 1.0 + plus_petits + 0.5 * egaux


def w_de_kendall(valeurs) -> np.ndarray:
    """W de Kendall. `valeurs` de forme (…, évaluateurs, objets) : chaque évaluateur (une famille, ou une mesure)
    classe les objets (les trois juges). W = 12 S / (m² (n³ − n)), S = somme des carrés des écarts des sommes de
    rangs à leur moyenne ; aucune correction d'égalité (le texte n'en écrit pas ; point ouvert PO-13)."""
    v = np.asarray(valeurs, dtype=np.float64)
    if v.ndim < 2 or v.shape[-1] < 2 or v.shape[-2] < 2:
        raise ConfigurationInvalide("W de Kendall : au moins deux évaluateurs et deux objets")
    m, n = v.shape[-2], v.shape[-1]
    sommes = rangs_des_objets(v).sum(-2)
    S = ((sommes - m * (n + 1) / 2.0) ** 2).sum(-1)
    return 12.0 * S / (m * m * (n ** 3 - n))


def loi_exacte_du_w(evaluateurs: int, objets: int = 3) -> tuple[np.ndarray, np.ndarray]:
    """Loi exacte de W sous le nul (classements indépendants et uniformes) : (valeurs triées, probabilités).
    Trois objets : 6^m affectations (7 776 pour cinq évaluateurs, 1 296 pour quatre)."""
    perms = np.array(list(itertools.permutations(range(1, objets + 1))), dtype=np.float64)
    comptes: dict[float, int] = {}
    total = 0
    for choix in itertools.product(range(len(perms)), repeat=evaluateurs):
        sommes = perms[list(choix)].sum(0)
        S = float(((sommes - evaluateurs * (objets + 1) / 2.0) ** 2).sum())
        w = round(12.0 * S / (evaluateurs ** 2 * (objets ** 3 - objets)), 12)
        comptes[w] = comptes.get(w, 0) + 1
        total += 1
    valeurs = np.array(sorted(comptes))
    return valeurs, np.array([comptes[w] / total for w in valeurs])


_LOIS: dict[tuple[int, int], tuple[np.ndarray, np.ndarray]] = {}


def p_exact_du_w(w: float, evaluateurs: int, objets: int = 3) -> float:
    """P(W ≥ w) sous le nul exact."""
    cle = (int(evaluateurs), int(objets))
    if cle not in _LOIS:
        _LOIS[cle] = loi_exacte_du_w(*cle)
    valeurs, probas = _LOIS[cle]
    return float(probas[valeurs >= float(w) - 1e-9].sum())


def tau_de_kendall(x, y) -> np.ndarray:
    """τ de Kendall (τ-b, égal au τ sans correction quand il n'y a pas d'égalité) le long du dernier axe. Vectorisé."""
    x, y = np.asarray(x, dtype=np.float64), np.asarray(y, dtype=np.float64)
    if x.shape[-1] != y.shape[-1] or x.shape[-1] < 2:
        raise ConfigurationInvalide("τ de Kendall : deux suites de même longueur, au moins deux valeurs")
    i, j = np.triu_indices(x.shape[-1], 1)
    sx, sy = np.sign(x[..., i] - x[..., j]), np.sign(y[..., i] - y[..., j])
    with np.errstate(divide="ignore", invalid="ignore"):
        return (sx * sy).sum(-1) / np.sqrt((sx != 0).sum(-1) * (sy != 0).sum(-1))


def ecarts_intra_famille(G) -> np.ndarray:
    """Ḡ_{j,f} moins la moyenne des trois juges de la famille f. `G` de forme (…, familles, juges)."""
    G = np.asarray(G, dtype=np.float64)
    return G - G.mean(-1, keepdims=True)


# ------------------------------------------------------------------------------------------------------------------
# Statistiques d'une lecture
# ------------------------------------------------------------------------------------------------------------------
def c_p3a_lecture(G_obs, G_tirages, niveau: float = 0.05) -> dict:
    """C-P3a pour une lecture. `G_obs` (familles, juges) ; `G_tirages` (B, familles, juges), mêmes tirages par tâches
    pour les trois juges. Valeur p exacte et valeur p par rééchantillonnage centré : W* sur les rangs des écarts
    Ḡ*_{j,f} − Ḡ_{j,f}, p = (1 + #{W* ≥ W}) / (B + 1). Conclut si les deux sont ≤ 0,05."""
    G, Gb = np.asarray(G_obs, dtype=np.float64), np.asarray(G_tirages, dtype=np.float64)
    if G.ndim != 2 or Gb.ndim != 3 or Gb.shape[1:] != G.shape:
        raise ConfigurationInvalide("C-P3a : G (familles, juges) et tirages (B, familles, juges) attendus")
    w = float(w_de_kendall(G))
    p_exact = p_exact_du_w(w, G.shape[0], G.shape[1])
    p_centre = p_depassement(w_de_kendall(Gb - G[None]), w)
    return {"W": w, "p_exact": p_exact, "p_centre": p_centre, "conclut": bool(p_exact <= niveau and p_centre <= niveau)}


def c_p3b_lecture(GA_obs, GA_tirages, GB_obs, GB_tirages, niveau: float = 0.05, permutations: int = 100_000,
                  rng: np.random.Generator | None = None) -> dict:
    """C-P3b pour une lecture : τ entre les quinze écarts intra-famille nets du corpus A et les quinze du corpus B ;
    p unilatéral par rééchantillonnage centré des deux corpus (tirages indépendants par tâches et par items).
    Rapporté sans verdict : τ des quinze valeurs Ḡ elles-mêmes, avec sa valeur p par permutation des valeurs du
    corpus B (100 000 permutations ; clé de graine `papier-C/etape2/permutations`), si `rng` est donné."""
    GA, GB = np.asarray(GA_obs, dtype=np.float64), np.asarray(GB_obs, dtype=np.float64)
    GAb, GBb = np.asarray(GA_tirages, dtype=np.float64), np.asarray(GB_tirages, dtype=np.float64)
    if GA.shape != GB.shape or GAb.shape[1:] != GA.shape or GBb.shape[1:] != GB.shape or GAb.shape[0] != GBb.shape[0]:
        raise ConfigurationInvalide("C-P3b : tableaux des deux corpus de formes incompatibles")
    tau = float(tau_de_kendall(ecarts_intra_famille(GA).ravel(), ecarts_intra_famille(GB).ravel()))
    B = GAb.shape[0]
    taus = tau_de_kendall(ecarts_intra_famille(GAb - GA[None]).reshape(B, -1),
                          ecarts_intra_famille(GBb - GB[None]).reshape(B, -1))
    p_centre = p_depassement(taus, tau)
    sortie = {"tau": tau, "p_centre": p_centre, "conclut": bool(p_centre <= niveau)}
    tau_valeurs = float(tau_de_kendall(GA.ravel(), GB.ravel()))
    sortie["tau_des_quinze_valeurs"] = tau_valeurs
    if rng is not None:
        a, b = GA.ravel(), GB.ravel()
        permute = np.stack([rng.permutation(b) for _ in range(int(permutations))])
        sortie["p_permutation_des_quinze_valeurs"] = p_depassement(tau_de_kendall(a[None, :], permute), tau_valeurs)
        sortie["permutations"] = int(permutations)
    return sortie


def c_p3c_lecture(gain_plaidoyer_juges, gain_usurpation_juges, G_famille_1, G_famille_4, niveau: float = 0.05) -> dict:
    """C-P3c pour une lecture : W des trois juges, quatre évaluateurs (gain d'écart brut des juges sous le plaidoyer de
    l'agent ; sous l'usurpation de l'agent ; Ḡ net de la famille 1 ; Ḡ net de la famille 4) ; rangs seulement ;
    valeur p exacte (1 296 affectations). Les deux gains d'écart ne dépendent pas de la lecture de la loi nette."""
    ev = np.array([gain_plaidoyer_juges, gain_usurpation_juges, G_famille_1, G_famille_4], dtype=np.float64)
    if ev.shape != (4, 3) or not np.all(np.isfinite(ev)):
        raise ConfigurationInvalide("C-P3c : quatre évaluateurs de trois valeurs finies attendus")
    w = float(w_de_kendall(ev))
    p = p_exact_du_w(w, 4, 3)
    return {"W": w, "p_exact": p, "conclut": bool(p <= niveau)}


# ------------------------------------------------------------------------------------------------------------------
# Verdicts, selon la version de la configuration
# ------------------------------------------------------------------------------------------------------------------
def verdict_stabilite(nom: str, par_lecture: dict, version: str, sans_verdict_par_clause=(),
                      grille_verifiee: bool = True) -> dict:
    """Combine les lectures d'une statistique (`nom` : « C-P3a », « C-P3b » ou « C-P3c »).

    `par_lecture` : {lecture: résultat de `c_p3*_lecture`} pour les trois lectures (toujours calculées et écrites).
    `version` : « a » ou « b ». `sans_verdict_par_clause` : statistiques que le rapport de la grille entière a
    trouvées au-dessus du seuil de la clause de repli (ligne 593 : « rapportée sans verdict, écrit tel quel »).
    `grille_verifiee` : faux tant que la grille ne couvre pas la statistique (C-P3c porte alors la mention « niveau
    non vérifié sur la grille », ligne 601)."""
    if nom not in ("C-P3a", "C-P3b", "C-P3c"):
        raise ConfigurationInvalide(f"statistique de rang {nom!r} inconnue")
    if version not in LECTURES_VERSION:
        raise ConfigurationInvalide(f"version de la stabilité de rang {version!r} : « a » ou « b »")
    manquantes = [l for l in TOUTES_LES_LECTURES if l not in par_lecture]
    if manquantes:
        raise ConfigurationInvalide(f"{nom} : lectures absentes {manquantes} (les trois sont toujours calculées)")
    lues = LECTURES_VERSION[version]
    sortie = {"statistique": nom, "version": version, "lectures_du_verdict": list(lues),
              "par_lecture": {l: par_lecture[l] for l in TOUTES_LES_LECTURES}, "mentions": [], "refutation": None}
    if nom in sans_verdict_par_clause:
        sortie["verdict"] = SANS_VERDICT
        sortie["mentions"].append("clause de repli mécanique : écart partiel à la prédiction 3 de N-005, déclaré")
    elif version == "b" and nom in ("C-P3a", "C-P3b"):
        sortie["verdict"] = SANS_VERDICT
        sortie["mentions"].append("version (b), lettre de P-021 : écart partiel à la prédiction 3 de N-005, déclaré")
    else:
        sortie["verdict"] = ETABLIE if all(par_lecture[l]["conclut"] for l in lues) else NON_ETABLIE
    if nom == "C-P3c" and not grille_verifiee:
        sortie["mentions"].append(MENTION_GRILLE)
    return sortie


def seuil_de_la_clause_de_repli(essais: int) -> float:
    """0,05 + 2 × √(0,05 × 0,95 / R), R essais de la case, au moins 1 000 (ligne 595)."""
    if essais < 1000:
        raise ConfigurationInvalide("clause de repli : au moins 1 000 essais par case")
    return 0.05 + 2.0 * float(np.sqrt(0.05 * 0.95 / essais))


__all__ = ["LECTURES_VERSION", "TOUTES_LES_LECTURES", "ETABLIE", "NON_ETABLIE", "SANS_VERDICT", "MENTION_GRILLE",
           "rangs_des_objets", "w_de_kendall", "loi_exacte_du_w", "p_exact_du_w", "tau_de_kendall",
           "ecarts_intra_famille", "c_p3a_lecture", "c_p3b_lecture", "c_p3c_lecture", "verdict_stabilite",
           "seuil_de_la_clause_de_repli"]
