"""Schéma de permutation des étiquettes des épisodes pour le plancher d'un moniteur, bras A des organismes discrets,
version 4 du code (préenregistrement `prereg/T0.7-organismes-discrets-v-a-v2-brouillon17.md`, 6.9, ligne 673 ; 8.4,
ligne 893) — module neuf, sans version antérieure.

D'où il vient : demande du coordinateur de la session de relance, d'après la vérification du côté habilité. Le lanceur
joue l'épisode honnête et l'épisode dosé de même rang avec les mêmes graines ; la permutation libre des étiquettes par
épisode, celle du texte (« une permutation échange, dans chaque tâche, les étiquettes des seize épisodes »), ignore ces
paires. Le contre-lecteur recommande l'échange dans chaque paire ; **Lazar n'a pas tranché, et le texte ne connaît que
la permutation libre**. Ce module **ne choisit pas** : le schéma est un argument obligatoire, sans valeur par défaut,
écrit en toutes lettres — `SCHEMA_LIBRE` ou `SCHEMA_ECHANGE_DANS_CHAQUE_PAIRE`.

Ce qu'il fait : il rend des étiquettes permutées, épisode par épisode (l'unité de la permutation est l'épisode, quelle
que soit l'unité de l'aire : les actions d'un épisode gardent ensemble l'étiquette tirée pour lui). Il ne lit aucun
fichier, aucun score, aucun interne de moniteur ; il ne calcule ni aire ni valeur p. Sous le brouillon 17, la
permutation est faite du côté habilité, et l'instance d'analyse ne reçoit que des nombres : ce module n'est appelé par
aucun module de l'analyse ; il écrit le schéma et ses gardes pour que les deux côtés aient la même lettre (signalé dans
le quatrième relevé des défauts).

Deux schémas, dans chaque tâche :
- **libre** : les étiquettes des épisodes de la tâche sont rebattues entre eux (les effectifs de chaque classe sont
  gardés) ;
- **échange dans chaque paire** : pour chaque rang, l'épisode honnête et l'épisode dosé de ce rang échangent leurs
  étiquettes, ou non, à pile ou face.

**Nombre de permutations distinctes** (2^(nombre de paires) sous l'échange : 2⁸ = 256 par tâche, 2¹²⁸ pour seize
tâches ; produit des combinaisons sous le schéma libre : 12 870 par tâche) : avec 2 000 tirages, les répétitions sont
négligeables (pièce relue sans interne, `pour-la-relance-lanceur-et-appariement-sans-interne-v1.md`, `3bec0ee9…`,
section 3). **Aucune énumération complète** n'est faite (précision du coordinateur) : les permutations sont toujours
tirées, et le compte de permutations perdues ou dégénérées du côté habilité reste tel quel. Le nombre de permutations
distinctes possibles est rendu avec le tirage (`distinctes_possibles`) ; ce que devient un plan où il serait petit
devant le nombre de tirages n'est pas écrit au texte (quatrième relevé des défauts) : ici, rien n'est changé, il est
seulement rapporté (`moins_de_distinctes_que_de_tirages`).

**Rééchantillonnage par tâche et paires** : un rééchantillonnage qui tire des tâches entières garde les paires ;
`exiger_paires_gardees` le contrôle sur des poids par épisode (un tirage épisode par épisode y est refusé).

Graine : le générateur est donné par l'appelant, tiré d'une clé de 6.2 (R9) ; aucun tirage sans générateur.
"""
from __future__ import annotations

import math
from typing import Sequence

import numpy as np

from ..gardes import GardeArret

SCHEMA_LIBRE = "libre"
SCHEMA_ECHANGE_DANS_CHAQUE_PAIRE = "echange dans chaque paire"
SCHEMAS = (SCHEMA_LIBRE, SCHEMA_ECHANGE_DANS_CHAQUE_PAIRE)
HONNETE, DOSE = 0, 1


def exiger_schema(schema: object) -> str:
    """Le schéma est obligatoire et écrit en toutes lettres : absent, vide, ou approchant, il est refusé — aucun
    schéma par défaut (Lazar n'a pas tranché)."""
    if schema not in SCHEMAS or not isinstance(schema, str):
        raise GardeArret(f"schéma de permutation {schema!r} : l'un de {SCHEMAS} exigé, écrit en toutes lettres — aucun "
                         "schéma par défaut")
    return schema


def exiger_episodes(episodes: Sequence[tuple[str, int, int]], schema: str) -> dict[str, dict[int, dict[int, int]]]:
    """Gardes sur les épisodes, donnés par (tâche, rang, étiquette), étiquette 0 pour l'honnête et 1 pour la dose. Rend
    `{tâche: {rang: {étiquette: place dans la liste}}}`.
    - sous les deux schémas : **rang en double** refusé (deux épisodes de même tâche, même rang, même étiquette) ;
      chaque tâche porte les deux classes ;
    - sous l'échange dans chaque paire : **paire incomplète** refusée (un rang sans son épisode honnête ou sans son
      épisode dosé)."""
    exiger_schema(schema)
    par_tache: dict[str, dict[int, dict[int, int]]] = {}
    if isinstance(episodes, (str, bytes)) or len(episodes) == 0:
        raise GardeArret("aucun épisode")
    for place, e in enumerate(episodes):
        if not isinstance(e, tuple) or len(e) != 3:
            raise GardeArret(f"épisode {e!r} : (tâche, rang, étiquette) exigé")
        tache, rang, etiquette = e
        if not isinstance(tache, str) or not tache:
            raise GardeArret(f"épisode {e!r} : tâche non vide exigée")
        if isinstance(rang, bool) or not isinstance(rang, (int, np.integer)) or rang < 0:
            raise GardeArret(f"épisode {e!r} : rang entier positif ou nul exigé")
        if isinstance(etiquette, bool) or etiquette not in (HONNETE, DOSE):
            raise GardeArret(f"épisode {e!r} : étiquette 0 (honnête) ou 1 (dose) exigée")
        rangs = par_tache.setdefault(tache, {}).setdefault(int(rang), {})
        if int(etiquette) in rangs:
            raise GardeArret(f"tâche {tache}, rang {rang} : rang en double pour l'étiquette {etiquette} — refusé")
        rangs[int(etiquette)] = place
    for tache, rangs in par_tache.items():
        classes = {c for paire in rangs.values() for c in paire}
        if classes != {HONNETE, DOSE}:
            raise GardeArret(f"tâche {tache} : une classe absente — rien à permuter")
        if schema == SCHEMA_ECHANGE_DANS_CHAQUE_PAIRE:
            incompletes = sorted(r for r, paire in rangs.items() if len(paire) != 2)
            if incompletes:
                raise GardeArret(f"tâche {tache} : paire incomplète au(x) rang(s) {incompletes} — sous l'échange dans "
                                 "chaque paire, chaque rang porte son épisode honnête et son épisode dosé")
    return par_tache


def nombre_de_permutations_distinctes(episodes: Sequence[tuple[str, int, int]], schema: str) -> int:
    """Nombre de permutations distinctes possibles : sous l'échange, 2^(nombre de paires) ; sous le schéma libre, le
    produit, sur les tâches, du nombre de façons de placer les étiquettes de la dose parmi les épisodes de la tâche."""
    par_tache = exiger_episodes(episodes, schema)
    if schema == SCHEMA_ECHANGE_DANS_CHAQUE_PAIRE:
        return 2 ** sum(len(rangs) for rangs in par_tache.values())
    total = 1
    for rangs in par_tache.values():
        etiquettes = [c for paire in rangs.values() for c in paire]
        total *= math.comb(len(etiquettes), sum(etiquettes))
    return total


def permutations_des_etiquettes(schema: str, episodes: Sequence[tuple[str, int, int]], n: int,
                                rng: np.random.Generator) -> dict:
    """`n` permutations des étiquettes des épisodes, **dans chaque tâche**, selon le schéma demandé (obligatoire), tirées
    indépendamment par `rng` (exigé ; aucune énumération complète). Rend `etiquettes` (tableau : une ligne par
    permutation, une colonne par épisode, dans l'ordre de `episodes`), `schema`, `distinctes_possibles`, et
    `moins_de_distinctes_que_de_tirages` (rapporté, sans rien changer au tirage)."""
    par_tache = exiger_episodes(episodes, schema)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise GardeArret(f"{n!r} permutations : entier ≥ 1 exigé")
    if not isinstance(rng, np.random.Generator):
        raise GardeArret("générateur exigé, tiré d'une clé de 6.2 (R9) : aucun tirage sans graine consignée")
    observees = np.array([e[2] for e in episodes], dtype=np.int8)
    distinctes = nombre_de_permutations_distinctes(episodes, schema)
    sortie = np.tile(observees, (n, 1))
    for t in sorted(par_tache):
        rangs = par_tache[t]
        if schema == SCHEMA_ECHANGE_DANS_CHAQUE_PAIRE:
            for r in sorted(rangs):
                h, d = rangs[r][HONNETE], rangs[r][DOSE]
                echange = rng.integers(0, 2, size=n).astype(bool)
                sortie[echange, h], sortie[echange, d] = DOSE, HONNETE
        else:
            places = np.array(sorted(p for paire in rangs.values() for p in paire.values()))
            for i in range(n):
                sortie[i, places] = rng.permutation(observees[places])
    return {"schema": schema, "distinctes_possibles": distinctes, "moins_de_distinctes_que_de_tirages": distinctes < n,
            "etiquettes": sortie}


def exiger_paires_gardees(episodes: Sequence[tuple[str, int, int]], poids: Sequence[float]) -> None:
    """Garde du rééchantillonnage par tâche (borne haute, aire conditionnelle) : `poids[i]` est le nombre de fois où
    l'épisode `i` entre dans un tirage. Un tirage de **tâches entières** donne le même poids à tous les épisodes d'une
    tâche, donc aux deux épisodes de chaque paire : il passe. Un tirage épisode par épisode, qui sépare l'épisode
    honnête de l'épisode dosé de même rang, est refusé."""
    par_tache = exiger_episodes(episodes, SCHEMA_ECHANGE_DANS_CHAQUE_PAIRE)
    w = np.asarray(poids, dtype=float)
    if w.shape != (len(episodes),) or not np.all(np.isfinite(w)) or np.any(w < 0):
        raise GardeArret("poids : un nombre positif ou nul par épisode exigé")
    for t, rangs in par_tache.items():
        places = [p for paire in rangs.values() for p in paire.values()]
        if len(set(w[places])) != 1:
            raise GardeArret(f"tâche {t} : ses épisodes n'ont pas tous le même poids — le rééchantillonnage ne tire pas des "
                             "tâches entières, et sépare des paires")


def exiger_permutation_conforme(schema: str, episodes: Sequence[tuple[str, int, int]], etiquettes: Sequence[int]) -> None:
    """Garde sur une permutation reçue (8.4, « unité de la permutation des étiquettes ») : elle garde, dans chaque tâche,
    les effectifs de chaque classe (une permutation entre tâches est refusée) ; sous l'échange dans chaque paire, les
    deux épisodes de chaque rang portent des étiquettes différentes (une permutation libre y est refusée)."""
    par_tache = exiger_episodes(episodes, schema)
    e = np.asarray(etiquettes)
    if e.shape != (len(episodes),) or not np.all(np.isin(e, (HONNETE, DOSE))):
        raise GardeArret("permutation : une étiquette 0 ou 1 par épisode exigée")
    for t, rangs in par_tache.items():
        places = [p for paire in rangs.values() for p in paire.values()]
        if int(e[places].sum()) != sum(episodes[p][2] for p in places):
            raise GardeArret(f"tâche {t} : effectifs des classes changés — permutation entre tâches refusée")
        if schema == SCHEMA_ECHANGE_DANS_CHAQUE_PAIRE:
            for r, paire in rangs.items():
                if e[paire[HONNETE]] == e[paire[DOSE]]:
                    raise GardeArret(f"tâche {t}, rang {r} : les deux épisodes de la paire portent la même étiquette — ce "
                                     "n'est pas un échange dans chaque paire")
