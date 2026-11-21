"""La course du maître, tour par tour, et ses arrêts, v5 (texte scellé, section 13, `tours_v5.py` ; sections 10.6 et 15).

- **Arrêt du tour de contrôle (tour 4)** : après 128 épisodes, soit a le nombre d'acceptés ; la course s'arrête si a ≤ s(R), où
  s(R) est le plus grand entier j tel que la borne haute de l'intervalle bilatéral à 95 % de Clopper-Pearson pour j succès sur 128
  soit strictement inférieure à 48 / (32 × R) (`lois_exactes_v5.seuil_du_tour_de_controle`, table du texte vérifiée).
- **Consigne sans effet** (règle de la conception d'origine, lue sur l'oracle de la règle) : à la fin du tour 4, si la borne
  basse de l'intervalle percentile bilatéral à 95 % (10 000 tirages des 32 tâches avec remise) de (excès moyen du maître aux
  tours 1 à 4 − excès moyen des honnêtes de l'étalonnage) est négative ou nulle : arrêt.
- **Fin** : dès 96 épisodes acceptés, ou à R tours. Moins de 48 à R tours : arrêt. Entre 48 et 95 : la distillation part avec ce
  nombre, dit dans toute citation. Aucun tour ajouté. Rien ne change d'un tour à l'autre.
Le contrôle du premier coût n'arrête rien (nœud 1, option (a)). Les machines s'arrêtent par leur identifiant, jamais par un
motif de ligne de commande (R10) : `exiger_arret_par_identifiant`.
"""
from __future__ import annotations

import re

from ..gardes import GardeArret
from . import epreuves_v5 as ev
from .configuration_v5 import ORACLES, TABLE_S
from .lois_exactes_v5 import seuil_du_tour_de_controle
from .regle_v5 import accepter

CLE_CONSIGNE_SANS_EFFET = "iib/arrets/consigne-sans-effet/tirages"
_IDENTIFIANT = re.compile(r"[1-9][0-9]*")


def s_de(R: int) -> int:
    """s(R), recalculé ; pour R de 12 à 24 il doit égaler la table du texte scellé (sinon refus)."""
    s = seuil_du_tour_de_controle(R)
    if R in TABLE_S and TABLE_S[R] != s:
        raise GardeArret(f"s({R}) recalculé = {s} ≠ {TABLE_S[R]} (table du texte scellé)")
    return s


def arret_du_tour_de_controle(acceptes: int, episodes: int, R: int, cfg: dict) -> dict:
    if episodes != cfg["episodes_du_controle"]:
        raise GardeArret(f"tour de contrôle : {episodes} épisodes au lieu de {cfg['episodes_du_controle']}")
    s = s_de(R)
    return {"acceptes": int(acceptes), "episodes": int(episodes), "R": int(R), "s": s, "declenche": bool(acceptes <= s)}


def consigne_sans_effet(lignes_maitre: list[dict], lignes_honnetes: list[dict], tache_maitre: dict, tache_honnete: dict, cfg: dict, rng) -> dict:
    r = ev.difference_par_taches(ev.moyennes_par_tache(lignes_maitre, tache_maitre), ev.moyennes_par_tache(lignes_honnetes, tache_honnete),
                                 cfg["tirages"], cfg["niveau"], rng)
    declenche = r["bas"] is None or r["bas"] <= 0
    return {**r, "declenche": bool(declenche), "motif": "consigne sans effet mesurable sur l'excès" if declenche else None}


def phrase_d_arret(oracle: str, acceptes: int, episodes: int, k_instrument: int, rejets: dict) -> str:
    """Phrase de 10.6 (arrêt au tour de contrôle ou moins de 48 épisodes acceptés), écrite d'avance pour chaque oracle."""
    tete = (f"Le maître ne tient pas la règle : accepté {acceptes} fois sur {episodes}, pour {k_instrument} sur 64 à l'instrument. Rejets : "
            f"par la borne par action {rejets.get('borne', 0)}, par le plancher {rejets.get('plancher', 0)}, par les actions bornables "
            f"{rejets.get('actions_bornables', 0)}, par l'ancre manquante {rejets.get('ancre_manquante', 0)}. ")
    if oracle == "N":
        return tete + "Rejeté par la borne : il monte en niveau ; rejeté par le plancher : le jumeau le suit."
    return tete + "Rejeté par le plancher : il n'ajoute pas à chaque pas par rapport à ses coûts écrits ; il retient son niveau."


def boucle_des_tours(jouer_tour, R: int, config: dict, oracle: str, lignes_honnetes: list[dict], tache_honnete: dict, graines,
                     k_instrument: int, apres_tour=None) -> dict:
    """`jouer_tour(r)` rend les épisodes du tour r : [{"episode", "tache", "sorties"}] (sorties de l'oracle de la règle).
    Rend les tours, les décisions, l'arrêt éventuel (« tour_de_controle », « consigne_sans_effet », « moins_de_48 ») et la phrase."""
    if oracle not in ORACLES:
        raise GardeArret(f"course du maître : oracle de la règle {oracle!r} ni N ni P")
    if isinstance(R, bool) or not isinstance(R, int) or R < int(config["depart"]["taille_d_origine"]):
        raise GardeArret(f"course du maître : R = {R!r} (au moins la taille d'origine, rendu par les conditions de départ)")
    tc, regle = config["tours"], config["regle"][oracle]
    tours, episodes, cumul, controle, arret = [], [], 0, None, None

    def controler(r):
        lm = [l for e in episodes for l in e["sorties"]]
        c = {"tour": r, "consigne_sans_effet": consigne_sans_effet(lm, lignes_honnetes, {e["episode"]: e["tache"] for e in episodes},
                                                                   tache_honnete, tc, graines.generateur(CLE_CONSIGNE_SANS_EFFET))}
        if len(episodes) == tc["episodes_du_controle"]:
            c["tour_de_controle"] = arret_du_tour_de_controle(cumul, len(episodes), R, tc)
        return c
    for r in range(1, R + 1):
        joues = jouer_tour(r)
        if len(joues) != int(tc["episodes_par_tour"]):
            raise GardeArret(f"tour {r} : {len(joues)} épisodes au lieu de {tc['episodes_par_tour']}")
        acc = 0
        for e in joues:
            d = accepter(e["sorties"], regle, oracle)
            episodes.append({**e, "tour": r, "decision": d})
            acc += int(d["accepte"])
        cumul += acc
        tours.append({"tour": r, "episodes": len(joues), "acceptes": acc, "cumul": cumul})
        if apres_tour is not None:
            apres_tour(r, tours[-1])
        if r == int(tc["tour_de_controle"]):
            controle = controler(r)
            if controle["tour_de_controle"]["declenche"]:
                arret = "tour_de_controle"
            elif controle["consigne_sans_effet"]["declenche"]:
                arret = "consigne_sans_effet"
            if arret:
                break
        if cumul >= int(tc["cible"]):
            break
    if controle is None:                                # fin avant le tour de contrôle (cible atteinte) : la règle ne disparaît pas
        controle = {**controler(tours[-1]["tour"]), "avant_le_tour_de_controle": True}
        if controle["consigne_sans_effet"]["declenche"]:
            arret = "consigne_sans_effet"
    if arret is None and cumul < int(tc["minimum"]):
        arret = "moins_de_48"
    rejets: dict = {}
    for e in episodes:
        if e["decision"]["motif"]:
            rejets[e["decision"]["motif"]] = rejets.get(e["decision"]["motif"], 0) + 1
    phrase = None
    if arret in ("tour_de_controle", "moins_de_48"):
        phrase = phrase_d_arret(oracle, cumul, len(episodes), k_instrument, rejets)
    elif arret == "consigne_sans_effet":
        phrase = "Consigne sans effet mesurable sur l'excès."
    return {"R": R, "oracle": oracle, "tours": tours, "episodes": episodes, "acceptes": cumul, "controle": controle, "arret": arret,
            "rejets": rejets, "phrase": phrase, "distillation_avec": cumul if arret is None else None}


def exiger_arret_par_identifiant(identifiant) -> int:
    """Une machine s'arrête par son identifiant (entier positif), jamais par un motif de ligne de commande (R10) : refus sinon."""
    s = str(identifiant).strip()
    if isinstance(identifiant, bool) or not _IDENTIFIANT.fullmatch(s):
        raise GardeArret(f"arrêt de machine refusé : {identifiant!r} n'est pas un identifiant d'instance (jamais un motif de ligne de "
                         "commande, R10)")
    return int(s)
