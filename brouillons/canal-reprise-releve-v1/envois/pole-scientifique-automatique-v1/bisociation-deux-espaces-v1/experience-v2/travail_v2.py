"""Exécution d'une condition de mondes, sur 1 ou 2 processus (R9 : chaque tâche reçoit sa SeedSequence du § 7 ;
aucun état global partagé, donc le résultat ne dépend pas du nombre de processus).

Un travailleur reçoit (condition, racine, indice, liste de bras, aux_extra) et rend la ligne de résultats du monde
(dictionnaire simple, sans objet Obs ni Latent : rien de latent ne sort du travailleur).
"""
import multiprocessing as mp

from controle_ia.gardes import GardeArret

import bras_v2 as br
import graines_v2 as gr
import mesures_v2 as ms
import monde_v2 as mo

# Bras exécutés dans une condition de décision ou descriptive : tous ceux de la liste figée, sauf N_grille, qui ne
# tourne que sur les 200 mondes de validation « moyen » (§ 5, § 9).
BRAS_DECISION = [b for b in br.ORDRE_BRAS if b != "N_grille"]


def evaluer_monde(tache):
    condition, racine, indice, bras, aux_extra = tache
    monde = mo.generer(condition, racine, indice)
    return ms.executer_monde(monde, condition, racine, indice, bras, aux_extra)


def executer_condition(condition, racine, indices, bras=None, processus=1, aux_extra=None, evaluer=evaluer_monde,
                       rapport=None):
    """Lignes de résultats des mondes `indices` d'une condition, dans l'ordre des indices. `processus` ∈ {1, 2, …}.
    `evaluer` est remplaçable dans les essais (jamais dans une exécution réelle). Une exception d'un monde (GardeArret,
    AccesLatent) arrête tout : elle est propagée, jamais comptée comme un échec silencieux."""
    bras = list(BRAS_DECISION if bras is None else bras)
    taches = [(condition, racine, int(i), bras, aux_extra) for i in indices]
    if processus <= 1 or len(taches) < 2 * processus:
        lignes = []
        for k, t in enumerate(taches):
            lignes.append(evaluer(t))
            if rapport:
                rapport(condition, k + 1, len(taches))
        return lignes
    lignes = []
    with mp.get_context("fork").Pool(processus) as pool:
        for k, ligne in enumerate(pool.imap(evaluer, taches, chunksize=8)):
            lignes.append(ligne)
            if rapport and (k + 1) % 200 == 0:
                rapport(condition, k + 1, len(taches))
    if len(lignes) != len(taches):
        raise GardeArret(f"{condition} : {len(lignes)} lignes rendues pour {len(taches)} mondes")
    return lignes
