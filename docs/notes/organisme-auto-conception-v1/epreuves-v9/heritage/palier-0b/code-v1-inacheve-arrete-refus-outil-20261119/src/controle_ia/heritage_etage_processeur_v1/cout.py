"""B6 — le compteur de coût simulé et les deux règles de retrait.

- Appels : cinq espèces, onze appels chacune par génération ; coût d'un appel = coût réel du rôle à la course v9 / 11.
- Épreuve : 0,18 USD par tentative éprouvée ; chaque appel provisionne deux épreuves.
- Budget d'une génération d'un bras : coût des 55 appels sans lecture, plus leur provision d'épreuve ; le même pour les trois bras.
- Lecture : par appel d'un bras qui sert un registre, prix par entrée × nombre d'entrées mesuré au début de la génération ;
  repère principal : 282 entrées sur 55 appels coûtent 14,1 % du coût de proposition d'une génération.
- Règle de retrait de la version 2 du plan (la seule qui décide) : appels retirés un à un dans l'ordre d'une permutation semée
  jusqu'à ce que le coût prévu des appels restants (espèce, lecture, provision) tienne dans le budget ; arrêt au premier appel
  retiré qui y suffit ; le reliquat n'est pas dépensé.
- Règle de la version 1 (point 8 seulement) : par espèce, appels gardés = entier inférieur de 11 × (coût sans lecture / coût avec
  lecture). SILENCE : « coût d'un appel » y comprend la provision d'épreuve, comme dans la règle de la version 2.
"""

import math

import numpy as np

from .constantes import (APPELS_PAR_ESPECE, APPELS_PAR_GENERATION, COUT_EPREUVE_USD, COUTS_ROLE_V9_USD,
                         EPREUVES_PROVISIONNEES_PAR_APPEL, ESPECES, REPERE_LECTURE, TAILLE_REGISTRE_PLEIN)

COUT_APPEL = np.array([c / APPELS_PAR_ESPECE for c in COUTS_ROLE_V9_USD])
ESPECE_DE_L_APPEL = np.repeat(np.arange(ESPECES), APPELS_PAR_ESPECE)  # appels 0..54 : espèce de chacun
COUT_PROPOSITION_GENERATION = float(sum(COUTS_ROLE_V9_USD))
PROVISION_PAR_APPEL = EPREUVES_PROVISIONNEES_PAR_APPEL * COUT_EPREUVE_USD
BUDGET_GENERATION = COUT_PROPOSITION_GENERATION + APPELS_PAR_GENERATION * PROVISION_PAR_APPEL


class ArretCout(RuntimeError):
    pass


def prix_lecture_par_entree(repere=REPERE_LECTURE):
    return repere * COUT_PROPOSITION_GENERATION / (TAILLE_REGISTRE_PLEIN * APPELS_PAR_GENERATION)


def cout_lecture_par_appel(entrees, repere=REPERE_LECTURE):
    return prix_lecture_par_entree(repere) * np.asarray(entrees, dtype=float)


def retrait_v2(permutation, lecture_par_appel, budget=BUDGET_GENERATION):
    """Une source. `permutation` : ordre semé des 55 appels. Rend (appels gardés (indices triés), appels retirés dans l'ordre,
    reliquat)."""
    cout = COUT_APPEL[ESPECE_DE_L_APPEL] + lecture_par_appel + PROVISION_PAR_APPEL
    restant = float(cout.sum())
    retires = []
    for a in permutation:
        if restant <= budget + 1e-9:
            break
        restant -= float(cout[a])
        retires.append(int(a))
    if restant > budget + 1e-9:
        raise ArretCout("règle de retrait : aucun ensemble d'appels ne tient dans le budget")
    gardes = sorted(set(range(APPELS_PAR_GENERATION)) - set(retires))
    return gardes, retires, budget - restant


def retrait_v2_vectorise(permutations, lecture_par_appel, budget=BUDGET_GENERATION):
    """Toutes les sources d'un coup. `permutations` : S × 55 ; `lecture_par_appel` : S. Rend (gardé : S × 55 booléens par
    indice d'appel, nombre d'appels gardés par espèce S × 5, reliquat S)."""
    S = permutations.shape[0]
    lecture = np.asarray(lecture_par_appel, dtype=float)
    cout_ordonne = COUT_APPEL[ESPECE_DE_L_APPEL][permutations] + lecture[:, None] + PROVISION_PAR_APPEL
    total = cout_ordonne.sum(axis=1)
    restant_apres = total[:, None] - np.cumsum(cout_ordonne, axis=1)  # après le retrait des r+1 premiers
    tient_avant = total <= budget + 1e-9
    premier = np.argmax(restant_apres <= budget + 1e-9, axis=1)  # indice du premier retrait qui suffit
    retires = np.where(tient_avant, 0, premier + 1)
    if np.any(~tient_avant & ~np.any(restant_apres <= budget + 1e-9, axis=1)):
        raise ArretCout("règle de retrait : aucun ensemble d'appels ne tient dans le budget")
    rang = np.empty_like(permutations)
    rang[np.arange(S)[:, None], permutations] = np.arange(APPELS_PAR_GENERATION)[None, :]
    garde = rang >= retires[:, None]
    par_espece = garde.reshape(S, ESPECES, APPELS_PAR_ESPECE).sum(axis=2)
    restant = np.where(tient_avant, total, total - np.take_along_axis(np.cumsum(cout_ordonne, axis=1),
                                                                      np.maximum(retires - 1, 0)[:, None], axis=1)[:, 0])
    return garde, par_espece, budget - restant


def retrait_v1(lecture_par_appel):
    """Par espèce, appels gardés = ⌊11 × (c + provision) / (c + provision + lecture)⌋. Rend le nombre gardé par espèce."""
    lecture = np.atleast_1d(np.asarray(lecture_par_appel, dtype=float))
    base = COUT_APPEL + PROVISION_PAR_APPEL
    rapport = base[None, :] / (base[None, :] + lecture[:, None])
    return np.floor(APPELS_PAR_ESPECE * rapport + 1e-12).astype(np.int64)


def verifier_retrait(permutation, gardes, retires, lecture_par_appel, budget=BUDGET_GENERATION):
    """Garde 18 : le coût prévu des appels gardés tient dans le budget ; les appels retirés sont les premiers de la permutation
    semée, dans son ordre ; le retrait s'arrête au premier appel qui suffit (avant le dernier retrait, le coût ne tenait pas)."""
    cout = COUT_APPEL[ESPECE_DE_L_APPEL] + lecture_par_appel + PROVISION_PAR_APPEL
    if float(cout[list(gardes)].sum()) > budget + 1e-9:
        raise ArretCout("garde 18 : coût prévu des appels gardés hors du budget")
    if list(retires) != [int(a) for a in list(permutation)[:len(retires)]]:
        raise ArretCout("garde 18 : appels retirés hors de l'ordre de la permutation semée")
    if retires:
        avant = float(cout.sum()) - float(cout[list(retires[:-1])].sum())
        if avant <= budget + 1e-9:
            raise ArretCout("garde 18 : le retrait ne s'est pas arrêté au premier appel qui suffit")
    return True


def nombre_de_tentatives(appels, rng):
    """Un appel rend une tentative, ou deux avec la probabilité 0,71 (B6)."""
    appels = np.asarray(appels)
    from .constantes import PROBA_DEUX_TENTATIVES
    return appels + rng.binomial(appels, PROBA_DEUX_TENTATIVES)


def epreuves_budget(n_tentatives, appels_gardes):
    """Nombre d'épreuves que la provision paie : deux par appel gardé (toujours au moins le nombre de tentatives)."""
    return np.minimum(n_tentatives, EPREUVES_PROVISIONNEES_PAR_APPEL * np.asarray(appels_gardes))


def math_floor(x):
    return int(math.floor(x + 1e-12))
