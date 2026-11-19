"""Schéma de permutation des étiquettes des épisodes pour le plancher d'un moniteur, bras A des organismes discrets,
version 7 du code (préenregistrement `prereg/T0.7-organismes-discrets-v-a-v2-brouillon25.md`, 6.9 ; 8.4 ; section 12,
point 17 ; case « schéma de permutation », 13.1).

Ce qui change depuis la version 5 (contre-lecture du code de la version 5, défaut C-2) : **les déclarations du schéma
ne viennent plus de l'appelant**. `exiger_schema_de_la_livraison` reçoit la configuration lue du fichier scellé
(`configuration_bras_a_v7.lire_la_configuration_scellee`) : le schéma retenu y est un choix nommé, et ce que la
livraison doit porter sous chaque schéma y est inscrit à la lettre. Il n'y a plus de table dans ce module, ni de
valeur par défaut, ni de dictionnaire libre : une livraison qui se déclare elle-même ne peut plus servir de preuve.
Le tirage à clé vient de `graines_bras_a_v7` (un tirage ne sert qu'une fois). Le reste est celui de la version 5.

**Lazar n'a pas tranché** entre la permutation libre par épisode (option 1) et l'échange dans chaque paire d'épisodes
de même tâche et de même rang (option 2) : le nœud est ouvert, sans défaut. Ce module **ne choisit pas** : le schéma
est partout un argument obligatoire, sans valeur par défaut, écrit en toutes lettres — `SCHEMA_LIBRE` (« libre par
episode ») ou `SCHEMA_ECHANGE_DANS_CHAQUE_PAIRE` (« echange dans chaque paire »).

Ce qui change depuis `permutation_etiquettes_bras_a_v4.py` (laissé tel quel, R12), d'après la contre-lecture du code
de la version 4 (`docs/notes/relance-organismes-discrets-v1/contre-lecture-code-v4-bras-a-v1.md`) :
- **le schéma entre dans la chaîne de l'analyse** (défaut C-8 de la version 4) : `exiger_schema_de_la_livraison`
  confronte le schéma retenu à ce que la livraison du côté habilité **déclare** dans ses réglages
  (`reglages.permutation`, `reglages.unite_de_la_permutation`) ;
- **le schéma libre ne dépend plus de l'ordre des épisodes reçus** (défaut mineur M-1 ; 6.2 : « avant tout tirage,
  la liste où l'on tire est triée ») : dans chaque tâche, les places sont triées par (rang, étiquette), non par leur
  rang dans la liste reçue ;
- **tirage à clé** (défaut C-7) : la fonction qui tire reçoit un tirage qui porte sa clé
  (`graines_bras_a_v7.TirageAClef`), d'une clé `perm/moniteur/{moniteur}/{dose}`, et non un générateur nu. Ces clés
  sont tirées **côté habilité** : la chaîne de la relance n'appelle jamais ce tirage ; le module écrit la lettre du
  schéma et ses gardes, pour que les deux côtés aient la même.

Ce qu'il fait : il rend des étiquettes permutées, épisode par épisode (l'unité de la permutation est l'épisode, quelle
que soit l'unité de l'aire : les actions d'un épisode gardent ensemble l'étiquette tirée pour lui). Il ne lit aucun
fichier, aucun score, aucun interne de moniteur ; il ne calcule ni aire ni valeur p.

Deux schémas, dans chaque tâche :
- **libre par épisode** : les étiquettes des épisodes de la tâche sont rebattues entre eux (les effectifs de chaque
  classe sont gardés) ;
- **échange dans chaque paire** : pour chaque rang, l'épisode honnête et l'épisode dosé de ce rang échangent leurs
  étiquettes, ou non, à pile ou face.

**Nombre de permutations distinctes** (2^(nombre de paires) sous l'échange : 2⁸ = 256 par tâche, 2¹²⁸ pour seize
tâches ; produit des combinaisons sous le schéma libre : 12 870 par tâche) : avec 2 000 tirages, les répétitions sont
négligeables. **Aucune énumération complète** n'est faite (6.9 : « toujours tirées, jamais énumérées ») ; le nombre de
permutations distinctes possibles est rendu avec le tirage (`distinctes_possibles`), et signalé s'il est inférieur au
nombre de tirages (`moins_de_distinctes_que_de_tirages`), sans rien changer au tirage.

**Rééchantillonnage par tâche et paires** : un rééchantillonnage qui tire des tâches entières garde les paires ;
`exiger_paires_gardees` le contrôle sur des poids par épisode (un tirage épisode par épisode y est refusé). Cette
garde n'est appelée par aucun calcul de l'analyse (défaut mineur M-9) : le rééchantillonnage de l'aire conditionnelle
garde les paires par construction (`analyse_bras_a_v7.tirages_des_taches` tire des tâches entières) ; elle sert à
éprouver un tirage reçu d'ailleurs.
"""
from __future__ import annotations

import math
from typing import Mapping, Sequence

import numpy as np

from ..gardes import GardeArret
from . import configuration_bras_a_v7 as configuration_bras_a
from . import graines_bras_a_v7 as graines_bras_a
from .arrets_bras_a_v7 import AUCUN_CAS, ETAPE_M, GARDE_REGLAGES, ArretDeLaLectureDeLaDiscretion

SCHEMA_LIBRE = configuration_bras_a.SCHEMA_LIBRE                                # « libre par episode »
SCHEMA_ECHANGE_DANS_CHAQUE_PAIRE = configuration_bras_a.SCHEMA_ECHANGE          # « echange dans chaque paire »
SCHEMAS = (SCHEMA_LIBRE, SCHEMA_ECHANGE_DANS_CHAQUE_PAIRE)
HONNETE, DOSE = 0, 1
CHAMPS_DU_SCHEMA_DANS_LES_REGLAGES = configuration_bras_a.CHAMPS_D_UNE_DECLARATION


def exiger_schema(schema: object) -> str:
    """Le schéma est obligatoire et écrit en toutes lettres : absent, vide, ou approchant, il est refusé — aucun
    schéma par défaut (Lazar n'a pas tranché)."""
    if not isinstance(schema, str) or schema not in SCHEMAS:
        raise GardeArret(f"schéma de permutation {schema!r} : l'un de {SCHEMAS} exigé, écrit en toutes lettres — aucun "
                         "schéma par défaut")
    return schema


def exiger_schema_de_la_livraison(configuration: Mapping, reglages: object) -> dict:
    """Garde du schéma de permutation **dans la chaîne de l'analyse** (6.9, « Contrôle des réglages rendus » ; 8.4,
    « réglages rendus » : « `permutation` ou `unite_de_la_permutation` qui ne nomme pas l'option retenue : refusés ») :
    la livraison du côté habilité doit **déclarer** avoir permuté sous le schéma retenu.
    - `configuration` : la configuration **lue du fichier scellé** ; le schéma retenu est son choix
      `schema_de_permutation` (ce module ne dit pas lequel Lazar retient), et ce que la livraison doit porter sous
      chaque schéma y est inscrit (`declarations_du_schema`). Un dictionnaire fait à la main, sans l'empreinte du
      fichier, est refusé ;
    - `reglages` : les réglages de la livraison.
    Une livraison qui porte autre chose que la déclaration du schéma retenu — dont un module resté à la permutation
    libre quand l'échange dans chaque paire est retenu — **arrête la lecture de la discrétion** (événement nommé,
    garde « réglages rendus », sans aucune valeur de la livraison). Rend ce qui est vérifié, pour le manifeste."""
    schema = configuration_bras_a.choix(configuration, configuration_bras_a.CHOIX_SCHEMA)
    attendu = configuration["chaines_du_module"]["declarations_du_schema"][schema]
    for champ in CHAMPS_DU_SCHEMA_DANS_LES_REGLAGES:
        if not isinstance(reglages, Mapping) or champ not in reglages or reglages[champ] != attendu[champ]:
            raise ArretDeLaLectureDeLaDiscretion(GARDE_REGLAGES, f"reglages.{champ}", AUCUN_CAS, ETAPE_M)
    return {"schema": schema, **{champ: attendu[champ] for champ in CHAMPS_DU_SCHEMA_DANS_LES_REGLAGES}}


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


def permutations_des_etiquettes(schema: str, episodes: Sequence[tuple[str, int, int]], n: int, tirage) -> dict:
    """`n` permutations des étiquettes des épisodes, **dans chaque tâche**, selon le schéma demandé (obligatoire), tirées
    indépendamment par `tirage` — un tirage à clé d'une clé `perm/moniteur/{moniteur}/{dose}`
    (`graines_bras_a_v7.tirage_reconnu_cote_habilite` ; un générateur nu est refusé ; aucune énumération complète).
    Le tirage ne dépend pas de l'ordre où les épisodes sont reçus : tâches triées, puis, dans la tâche, rangs triés
    (échange) ou places triées par (rang, étiquette) (schéma libre). Rend `etiquettes` (tableau : une ligne par
    permutation, une colonne par épisode, dans l'ordre de `episodes`), `schema`, `distinctes_possibles`, et
    `moins_de_distinctes_que_de_tirages` (rapporté, sans rien changer au tirage)."""
    par_tache = exiger_episodes(episodes, schema)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise GardeArret(f"{n!r} permutations : entier ≥ 1 exigé")
    rng = graines_bras_a.generateur_pour(tirage, graines_bras_a.USAGE_PERMUTATION_D_UN_MONITEUR)
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
            # places triées par (rang, étiquette), non par leur rang dans la liste reçue (6.2 ; M-1)
            places = np.array([rangs[r][c] for r in sorted(rangs) for c in sorted(rangs[r])])
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
