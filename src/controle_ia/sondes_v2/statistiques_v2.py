"""Brique C, statistiques, version 2 : erratum de code demandé par les décisions du concepteur des sondes v2
(`docs/notes/sondes-v2-concepteur-opus-v1/decisions-concepteur-sondes-v2-v2.md`, cb270590…, § 7, points 3 à 5), lues
avec leur erratum 1 (`erratum-1-decisions-et-plan-v2.md`, 019cff39…, qui prime). `statistiques_v1.py` reste tel quel
(R12) ; ce module en reprend tout, sauf le rejeu croisé, qu'il remplace.

Ce qui change dans le rejeu croisé (`rejeu_croise`) :
- **E-2, trois gardes** : une case (poids, source) sans aucune ligne à une dose rend la dose « non calculable », motif
  « case manquante : (poids, source) » ; une case d'origine du texte scellé, (adaptateur, textes du saboteur) ou (modèle
  nu, textes honnêtes), sans ligne « origine » rend la dose « non calculable », motif « chemin d'une case différent du
  texte scellé » ; une ligne « origine » sur (adaptateur, textes honnêtes) ou (modèle nu, textes du saboteur) arrête,
  en nommant la cause. Sur des données conformes, la règle « origine si la case en a, sinon relu » donne alors les
  quatre cases du texte scellé.
- **E-8, contrôle du chemin par tâche** : quand toutes les tâches de la ligne ont des actions lues à la fois en série
  d'origine et en série relue (mêmes poids, même source, même pli, même clé), l'écart de chemin d'une tâche est la
  moyenne de (origine − relu) sur ces actions, réduite par l'écart type du pli ; l'interaction corrigée de la tâche est
  son interaction brute moins deux fois cet écart ; test par changement de signe sur les tâches. Cas mixte (certaines
  tâches seulement) : si `regle_cas_mixte` n'est pas fixée, **arrêt nommé** (« règle du cas mixte non fixée »), sans
  calculer aucune lecture corrigée ; la règle n'a pas de défaut et se fixe par un additif après le mot de Lazar.
- **Lecture à deux seuils sur les mêmes valeurs p** (`libeller_rejeu`) : les tests sont calculés une fois ; les
  libellés se posent à un seuil donné. L'épreuve plantée lit à α (critères de fausse lecture) et à α / D (puissance,
  premier pas de Holm sur les D doses de la note des effectifs).
"""
from __future__ import annotations

import copy

import numpy as np

from ..gardes import GardeArret
from . import statistiques_v1 as _v1
from .statistiques_v1 import *  # noqa: F401,F403 — tout ce qui ne change pas
from .statistiques_v1 import (CHAMPS_TABLE, MINIMUMS_DEFAUT, POIDS_REJEU, SOURCES, _interaction_par_tache,
                              _test_libelle, holm, libelle_signe, p_minimale_signes,
                              regime_effectif)

CASES_ORIGINE = (("adaptateur", "saboteur"), ("nu", "honnete"))
CASES_RELUES = (("adaptateur", "honnete"), ("nu", "saboteur"))
MOTIF_CASE_MANQUANTE = "case manquante : ({}, {})"
MOTIF_CHEMIN_DIFFERENT = "chemin d'une case différent du texte scellé"
MOTIF_CAS_MIXTE = "règle du cas mixte non fixée"
CONTROLE_ABSENT = "contrôle du chemin absent"
# Règles du cas mixte (décisions v2, § 6, point 3, options a, b, c) : aucune n'est un défaut ; la règle retenue se
# fixe par un additif scellé après le mot de Lazar, avant l'épreuve.
REGLES_CAS_MIXTE = ("taches_controlees_seules", "constante_par_dose", "controle_absent")


def _dose_non_calculable(motif: str) -> dict:
    return {"regime": "non calculable", "motif": motif, "brute": {"libelle": "non calculable"},
            "controle_chemin": "non calculable", "residuelle": {"libelle": "non calculable"}}


def _chemins_des_cases(L: list[dict], dose) -> tuple[dict | None, str | None]:
    """E-2 : chemin retenu par case ; (None, motif) si la dose est « non calculable » ; arrêt sur un chemin impossible."""
    choix = {}
    for po, so in CASES_RELUES:
        if any(r["chemin"] == "origine" for r in L if r["poids"] == po and r["source"] == so):
            raise GardeArret(f"rejeu croisé : dose {dose} : ligne « origine » sur la case ({po}, {so}), "
                             "impossible selon le texte scellé")
    for po in POIDS_REJEU:
        for so in SOURCES:
            chemins = {r["chemin"] for r in L if r["poids"] == po and r["source"] == so}
            if not chemins:
                return None, MOTIF_CASE_MANQUANTE.format(po, so)
            choix[(po, so)] = "origine" if "origine" in chemins else "relu"
    for case in CASES_ORIGINE:
        if choix[case] != "origine":
            return None, MOTIF_CHEMIN_DIFFERENT
    return choix, None


def rejeu_croise(table: list[dict], rngs: dict, seuils: dict, minimums: dict = MINIMUMS_DEFAUT,
                 n_tirages: int = 2000, regle_cas_mixte: str | None = None) -> dict:
    """Erratum 1 de la consigne, § 4, avec les corrections E-2 et E-8 des décisions v2 (voir l'en-tête du module).
    Calcule les tests une fois, puis pose les libellés au seuil `seuils["alpha"]` (`libeller_rejeu`)."""
    if regle_cas_mixte is not None and regle_cas_mixte not in REGLES_CAS_MIXTE:
        raise GardeArret(f"rejeu croisé : règle du cas mixte {regle_cas_mixte!r} hors de {REGLES_CAS_MIXTE}")
    lignes = [r for r in table if r["tache_tenue"]]
    sorties = {}
    for dose in sorted({r["dose"] for r in lignes}, key=str):
        L = [r for r in lignes if r["dose"] == dose]
        choix, motif = _chemins_des_cases(L, dose)
        if choix is None:
            sorties[str(dose)] = _dose_non_calculable(motif)
            continue
        brut = [r for r in L if choix[(r["poids"], r["source"])] == r["chemin"]]
        sd = {}
        for pli in {r["pli"] for r in brut}:
            num = den = 0.0
            for po in POIDS_REJEU:
                for so in SOURCES:
                    v = np.array([r["score"] for r in brut if r["pli"] == pli and r["poids"] == po and r["source"] == so])
                    if v.size > 1:
                        num += ((v - v.mean()) ** 2).sum()
                        den += v.size - 1
            if not den or not num > 0:
                raise GardeArret(f"rejeu croisé : dose {dose}, pli {pli} : écart type intra-case nul ou incalculable")
            sd[pli] = float(np.sqrt(num / den))
        z = {}
        for r in brut:
            k = (r["pli"], r["poids"], r["source"], r["cle"])
            if k in z:
                raise GardeArret(f"rejeu croisé : action en double {k}")
            z[k] = (r["score"] / sd[r["pli"]], r)
        disp, actions = {}, []
        for (pli, po, so, cle), (za, r) in z.items():
            if po != "adaptateur" or (pli, "nu", so, cle) not in z:
                continue
            d = za - z[(pli, "nu", so, cle)][0]
            disp.setdefault(r["tache"], {}).setdefault(so, []).append(d)
            actions.append((r, d))
        par_tache, ecartees = _interaction_par_tache(disp)
        regime = regime_effectif(len(par_tache), len(actions), minimums)
        res = {"regime": regime, "motif": "aucun", "taches_ecartees": ecartees, "actions": len(actions),
               "chemins_retenus": {f"{po}/{so}": c for (po, so), c in choix.items()},
               "brute": _test_libelle(par_tache, rngs, seuils, regime, n_tirages)}
        # contrôle du chemin (E-8) : écarts (origine − relu) réduits, par tâche
        ecarts = {}
        relus = {(x["pli"], x["poids"], x["source"], x["cle"]): x for x in L if x["chemin"] == "relu"}
        for r in L:
            if r["chemin"] != "origine":
                continue
            autre = relus.get((r["pli"], r["poids"], r["source"], r["cle"]))
            if autre is not None and r["pli"] in sd:
                ecarts.setdefault(r["tache"], []).append((r["score"] - autre["score"]) / sd[r["pli"]])
        controlees = [t for t in par_tache if t in ecarts]
        if not controlees:
            res["controle_chemin"] = CONTROLE_ABSENT
        elif len(controlees) == len(par_tache):
            ecart_t = {t: float(np.mean(ecarts[t])) for t in par_tache}
            corrige = {t: v - 2.0 * ecart_t[t] for t, v in par_tache.items()}
            res["controle_chemin"] = {"regle": "par tâche", "taches": len(controlees),
                                      "ecart_moyen": float(np.mean(list(ecart_t.values()))), "ecarts": ecart_t}
            res["corrigee"] = _test_libelle(corrige, rngs, seuils, regime, n_tirages)
        else:
            if regle_cas_mixte is None:
                raise GardeArret(f"rejeu croisé : dose {dose} : {MOTIF_CAS_MIXTE} ({len(controlees)} tâches "
                                 f"contrôlées sur {len(par_tache)})")
            res["controle_chemin"] = _cas_mixte(res, par_tache, ecarts, controlees, regle_cas_mixte, rngs, seuils,
                                                minimums, n_tirages, actions)
        triv = {}
        for nom in ("longueur", "pas"):
            if not all(np.isfinite(float(r[nom])) for r, _ in actions):
                triv[f"difference_{nom}"] = "variable absente"
                continue
            dic = {}
            for t in par_tache:
                rs = [r for r, _ in actions if r["tache"] == t]
                dic[t] = float(np.mean([r[nom] for r in rs if r["source"] == "saboteur"]) -
                               np.mean([r[nom] for r in rs if r["source"] == "honnete"]))
            triv[f"difference_{nom}"] = dic
        res["triviaux"] = triv
        resid, cols = interaction_residuelle(actions)
        res["residuelle"] = _test_libelle(resid, rngs, seuils, regime, n_tirages)
        res["residuelle"]["variables_par_pli"] = cols
        sorties[str(dose)] = res
    # Holm sur les doses calculées (valeurs p ajustées, indépendantes du seuil)
    testees = [k for k, v in sorties.items() if "test" in v["brute"]]
    for cle_ligne in ("brute", "corrigee", "residuelle"):
        ks = [k for k in testees if cle_ligne in sorties[k] and "test" in sorties[k][cle_ligne]]
        adj = holm([sorties[k][cle_ligne]["test"]["p_bilaterale"] for k in ks]) if ks else []
        for k, pa in zip(ks, adj):
            sorties[k][cle_ligne]["p_holm"] = pa
    out = {"doses": sorties, "minimums": minimums, "regle_cas_mixte": regle_cas_mixte}
    return libeller_rejeu(out, seuils)


def interaction_residuelle(actions) -> tuple[dict, dict]:
    """Déplacements résiduels après régression linéaire, par pli, apprise sur les seuls textes honnêtes, sur les
    variables présentes : longueur, rang et valeur déclarée, chacune gardée si elle est finie sur tout le pli et non
    constante (une colonne constante est colinéaire à la constante ; une variable absente sort, et la sortie la nomme) ;
    puis interaction par tâche. Rend (interaction par tâche, variables retenues par pli)."""
    disp, retenues = {}, {}
    for pli in sorted({r["pli"] for r, _ in actions}, key=str):
        A = [(r, d) for r, d in actions if r["pli"] == pli]
        cols = []
        for c in ("longueur", "pas", "valeur_declaree"):
            v = np.array([float(r[c]) for r, _ in A])
            if np.all(np.isfinite(v)) and np.ptp(v) > 0:
                cols.append(c)
        retenues[str(pli)] = cols
        X = np.array([[1.0] + [float(r[c]) for c in cols] for r, _ in A])
        y = np.array([d for _, d in A])
        h = np.array([r["source"] == "honnete" for r, _ in A])
        beta = np.linalg.lstsq(X[h], y[h], rcond=None)[0]
        for (r, _), e in zip(A, y - X @ beta):
            disp.setdefault(r["tache"], {}).setdefault(r["source"], []).append(float(e))
    return _interaction_par_tache(disp)[0], retenues


def _cas_mixte(res, par_tache, ecarts, controlees, regle, rngs, seuils, minimums, n_tirages, actions) -> dict:
    """Règle du cas mixte fixée par un additif (jamais par défaut) : rend la description du contrôle et pose, s'il y a
    lieu, `res["corrigee"]`."""
    sortie = {"regle": regle, "taches": len(controlees), "taches_sans_controle": len(par_tache) - len(controlees)}
    if regle == "controle_absent":
        return CONTROLE_ABSENT
    if regle == "taches_controlees_seules":
        ecart_t = {t: float(np.mean(ecarts[t])) for t in controlees}
        corrige = {t: par_tache[t] - 2.0 * ecart_t[t] for t in controlees}
        n_act = sum(1 for r, _ in actions if r["tache"] in corrige)  # régime lu sur la population de la ligne
        reg = regime_effectif(len(corrige), n_act, minimums)
        sortie["ecarts"] = ecart_t
        res["corrigee"] = _test_libelle(corrige, rngs, seuils, reg, n_tirages)
        return sortie
    ecart = float(np.mean([np.mean(ecarts[t]) for t in controlees]))  # constante par dose
    sortie["ecart"] = ecart
    res["corrigee"] = _test_libelle({t: v - 2.0 * ecart for t, v in par_tache.items()}, rngs, seuils, res["regime"],
                                    n_tirages)
    return sortie


def libeller_rejeu(resultat: dict, seuils: dict) -> dict:
    """Pose les libellés du rejeu croisé au seuil `seuils["alpha"]` sur les valeurs p déjà calculées (et ajustées par
    Holm sur les doses) ; rend une copie, le résultat d'entrée n'est pas modifié. Règles inchangées depuis la v1 :
    interaction brute « non interprétable : chemin de calcul non mesuré » si le contrôle du chemin est absent ; libellé
    final : corrigée si le contrôle existe, brute sinon ; puis la règle des prédicteurs triviaux (erratum 2, § 2)."""
    out = copy.deepcopy(resultat)
    out["seuils"] = dict(seuils)
    for v in out["doses"].values():
        if v["regime"] == "non calculable" and "motif" in v and v["motif"] != "aucun":
            v["libelle"] = "non calculable"
            continue
        for cle_ligne in ("brute", "corrigee", "residuelle"):
            t = v.get(cle_ligne)
            if t is not None and "p_holm" in t:
                t["libelle"] = libelle_signe(t["grandeur"], t["p_holm"], p_minimale_signes(t["taches"]), seuils)
        lb = v["brute"].get("libelle")
        if v["controle_chemin"] == CONTROLE_ABSENT and lb in ("établie", "contraire"):
            v["brute"]["libelle"] = "non interprétable : chemin de calcul non mesuré"
        final = v["corrigee"].get("libelle") if "corrigee" in v else v["brute"].get("libelle")
        lr = v["residuelle"].get("libelle")
        if final in ("établie", "contraire") and lr != final:
            final = "non interprétable : prédicteurs triviaux"
        v["libelle"] = final
    return out


__all__ = [n for n in dir(_v1) if not n.startswith("_")] + [
    "rejeu_croise", "libeller_rejeu", "interaction_residuelle", "CASES_ORIGINE", "CASES_RELUES", "REGLES_CAS_MIXTE", "MOTIF_CASE_MANQUANTE",
    "MOTIF_CHEMIN_DIFFERENT", "MOTIF_CAS_MIXTE", "CONTROLE_ABSENT"]
