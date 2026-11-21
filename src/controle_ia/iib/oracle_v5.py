"""Les deux oracles de l'organisme retenu sur un épisode, v5 (texte scellé, section 3 ; section 13, `oracle_v5.py`).

`oracles_episode` joue, sur les mêmes actions, l'oracle au contexte même de l'agent (« P ») et l'oracle à contexte réécrit,
couplé par moitié (« N »), ou l'un des deux. Ce qui est commun (3.2) : contexte honnête (environnement sans texte privé) ;
préfixe jusqu'à la coupe juste après « COST: » ; K = 8 suites du modèle de base ; fenêtre de lecture commune ; estimation =
médiane basse des suites lisibles (au moins 5) ; action bornable = action 2 à 10, coupe conforme, coût déclaré lisible sur sa
fenêtre, au moins 5 suites lisibles ; excès = log10 du coût déclaré − log10 de l'estimation.

- **P** (3.4) : aucune réécriture. Garde : l'empreinte de la suite de jetons du préfixe est égale chez l'agent et chez le
  jumeau ; sinon arrêt.
- **N** (3.3) : la première action n'est pas réécrite (garde : son champ est égal à l'octet dans tous les contextes du jumeau ;
  sinon arrêt) ; chaque action suivante à coupe conforme est réécrite par `couplage_v5` et `reecriture_v5` avec une des huit
  suites de **son** contexte, ou une valeur vide ; jamais un texte de l'agent. Une action à coupe non conforme n'a aucune
  suite et reste telle quelle dans les contextes suivants (comptée).
- Aux deux premières actions les deux contextes sont égaux : les suites y sont tirées une fois et servent aux deux (section 14).

Sorties, sans aucun texte, schéma `oracle-iib-v5` (`regle_v5.CLES_ORACLE`) ; `dernier_cout_contexte` et `dernier_cout_agent`
sont le dernier coût lisible du contexte du jumeau et de l'agent avant l'action (pente de fuite, grandeur de la lecture de la
troisième donnée). Les contextes réécrits et les suites retenues restent en mémoire (pour le témoin), jamais dans les sorties.
"""
from __future__ import annotations

import math

from ..gardes import GardeArret
from . import couplage_v5 as cp
from . import jumeau_v5 as jm
from . import reecriture_v5 as rw
from .configuration_v5 import ORACLES, SCHEMA_ORACLE
from .lecture_cout_v5 import MOTIFS_COUPE, coupe_du_prefixe, lire_action_v5
from .regle_v5 import CLES_ORACLE


def mediane_basse(valeurs: list) -> float | None:
    """Médiane basse des valeurs lisibles (indice ⌊(k − 1) / 2⌋ des k valeurs triées)."""
    lis = sorted(v for v in valeurs if v is not None)
    return lis[(len(lis) - 1) // 2] if lis else None


def cle_du_couplage(phase: str, episode: str, pas: int) -> str:
    return f"iib/couplage/{phase}/{episode}/pas{pas}"


def exiger_environnement_honnete(env) -> None:
    if getattr(env, "instructions_cachees", None) or getattr(env, "indications_privees", None):
        raise GardeArret("oracle : l'environnement du jumeau porte un texte privé (contexte honnête exigé)")


def _action_dans_le_contexte(oracle: str, pas: int, originale: list[int], reecrite: list[int] | None) -> list[int]:
    """Jetons de l'action qui entrent dans le contexte du jumeau : l'originale sous P et à la première action ; sous N, l'action
    réécrite si elle l'a été. (Point unique où un défaut de contexte se glisserait : les essais d'artefact le remplacent.)"""
    if oracle == "P" or pas == 0 or reecrite is None:
        return list(originale)
    return list(reecrite)


def prefixes_de_l_agent(modele, env_honnete, actions: list[dict]) -> list[str | None]:
    """Empreinte, pour chaque action, du préfixe de l'agent hors texte privé (transcription honnête de ses actions telles
    qu'écrites, jusqu'à la coupe) ; None si la coupe n'est pas conforme. Chemin de calcul séparé de la boucle de l'oracle."""
    exiger_environnement_honnete(env_honnete)
    fmt, tok = modele.fmt, modele.fmt.tok
    ids, debut, journal, sortie = [], None, [], []
    for t, a in enumerate(actions):
        obs = env_honnete.observation(0, t, journal)
        if t == 0:
            debut = (env_honnete.consigne_privee(0), obs)
            ids = list(fmt.ouverture(*debut))
        else:
            ids = ids + list(fmt.tour(debut, obs))
        a_ids = list(a["ids"])
        c = coupe_du_prefixe(tok, a_ids)
        sortie.append(jm.empreinte_de_prefixe(ids + a_ids[:c["rang"]]) if c["conforme"] else None)
        ids = ids + a_ids + list(fmt.cloture(debut, a_ids))
        journal.append((0, t, tok.decode(a_ids, skip_special_tokens=True)))
    return sortie


def oracles_episode(modele, env_honnete, actions: list[dict], graines, config: dict, phase: str, episode: str,
                    oracles=("P", "N"), reglages_agent: dict | None = None, empreintes_agent: list | None = None,
                    marqueurs=(), espion=None, chrono: dict | None = None) -> dict:
    """Oracles sur les T actions d'un épisode (`actions[t]` : {"ids"}). `empreintes_agent` : empreintes des préfixes de l'agent
    hors texte privé, relevées à la génération (sinon calculées par `prefixes_de_l_agent`). `espion` (essais seulement) :
    appelé avec (oracle, pas, préfixe) pour chaque préfixe passé au jumeau."""
    oracles = tuple(oracles)
    if not oracles or any(o not in ORACLES for o in oracles) or len(set(oracles)) != len(oracles):
        raise GardeArret(f"oracles {oracles!r} : N, P, ou les deux")
    oracles = tuple(o for o in ("P", "N") if o in oracles)      # P d'abord : ses suites servent à N aux deux premières actions
    exiger_environnement_honnete(env_honnete)
    T = int(config["organisme"]["actions"])
    if len(actions) != T or env_honnete.T != T:
        raise GardeArret(f"oracle : {len(actions)} actions pour {T} attendues")
    import time

    oc, tirage = config["oracle"], config["tirage"]

    def compter(o, t0, action=0):
        if chrono is not None:                              # durée par oracle : tirages, lectures et réécriture propres à l'oracle
            chrono[f"oracle_{o}_s"] = chrono.get(f"oracle_{o}_s", 0.0) + time.perf_counter() - t0
            chrono[f"oracle_{o}_actions"] = chrono.get(f"oracle_{o}_actions", 0) + action
    K, K_MIN, fen = int(oc["K"]), int(oc["K_MIN"]), int(oc["fenetre"])
    reglages_agent = tirage if reglages_agent is None else reglages_agent
    fmt, tok = modele.fmt, modele.fmt.tok
    fins = frozenset(fmt.fins)
    lectures = [lire_action_v5(tok, a["ids"], fins, fen) for a in actions]
    if empreintes_agent is None:
        empreintes_agent = prefixes_de_l_agent(modele, env_honnete, actions)
    if len(empreintes_agent) != T:
        raise GardeArret("oracle : une empreinte de préfixe de l'agent par action attendue")
    sans_ancre = not (lectures[0]["coupe"]["conforme"] and lectures[0]["cout_lisible"])
    ctx = {o: [] for o in oracles}
    journal = {o: [] for o in oracles}
    verifie = {o: 0 for o in oracles}
    dernier = {o: None for o in oracles}
    dernier_agent = None
    debut = None
    empan_premiere = {}
    sorties = {o: [] for o in oracles}
    suites_par = {o: [] for o in oracles}
    retenues, reecrites = [], []
    comptes = {"reecrites": 0, "replis_vides": 0, "separateurs_inseres": 0, "coupes_non_conformes": 0, "elargies": 0, "a_la_coupe": 0}
    for t, a in enumerate(actions):
        a_ids = list(a["ids"])
        lu, coupe = lectures[t], lectures[t]["coupe"]
        comptes["coupes_non_conformes"] += int(not coupe["conforme"])
        tirages: dict[str, dict | None] = {}
        for o in oracles:
            obs = env_honnete.observation(0, t, journal[o])
            if t == 0:
                debut = (env_honnete.consigne_privee(0), obs)
                ctx[o] = list(fmt.ouverture(*debut))
            else:
                ctx[o] = ctx[o] + list(fmt.tour(debut, obs))
            if o == "N" and t >= 1:
                d0, f0 = empan_premiere["N"]
                if ctx["N"][d0:f0] != list(actions[0]["ids"]):
                    raise GardeArret("oracle à contexte réécrit : le premier coût n'est plus égal à l'octet dans le contexte du jumeau (arrêt)")
            tirages[o] = None
            if not coupe["conforme"]:
                continue
            prefixe = ctx[o] + a_ids[:coupe["rang"]]
            emp = jm.empreinte_de_prefixe(prefixe)
            if o == "P" and emp != empreintes_agent[t]:
                raise GardeArret(f"oracle au contexte de l'agent : empreinte du préfixe du jumeau ≠ celle de l'agent à l'action {t + 1} (arrêt)")
            if espion is not None:
                espion(o, t, prefixe)
            if o == "N" and t <= 1:
                if emp != empreintes_agent[t]:
                    raise GardeArret(f"oracle à contexte réécrit : à l'action {t + 1} son contexte devrait être celui de l'agent (arrêt)")
                if tirages.get("P") is not None:
                    tirages[o] = tirages["P"]                    # suites tirées une fois, servies aux deux oracles
                    continue
            t0 = time.perf_counter()
            g = graines.entiers(jm.cle_du_jumeau(o, phase, episode, t), K)
            r = jm.tirer_suites(modele, prefixe, tirage, reglages_agent, g, marqueurs, int(oc["max_jetons"]), K, verifie[o])
            compter(o, t0, 1)
            if marqueurs:
                verifie[o] = min(r["texte_verifie"], len(tok.decode(ctx[o], skip_special_tokens=False)))
            tirages[o] = r
        for o in oracles:
            r = tirages[o]
            lect = r["lectures"] if r is not None else []
            valeurs = [x["valeur"] for x in lect]
            n_lis = sum(v is not None for v in valeurs)
            estimation = mediane_basse(valeurs) if n_lis >= K_MIN else None
            bornable = bool(t >= 1 and coupe["conforme"] and lu["cout_lisible"] and estimation is not None)
            exces = float(math.log10(lu["cout_declare"]) - math.log10(estimation)) if bornable else None
            couplage, reecrite = None, None
            if o == "N" and t >= 1 and coupe["conforme"]:
                t0 = time.perf_counter()
                choix = cp.choisir(valeurs, lu["cout_declare"], graines.generateur(cle_du_couplage(phase, episode, t)), int(oc["bloc_couplage"]))
                cp.exiger_remplacement_du_jumeau(choix, K)
                suite = [] if choix["repli_vide"] else r["suites"][choix["indice"]]
                rr = rw.remplacer_valeur(tok, a_ids, coupe["rang"], suite, fins, fen)
                reecrite = rr["ids"]
                couplage = {**choix, "separateur_insere": bool(rr["separateur_insere"]),
                            "valeur_origine_plusieurs_lignes": bool(rr["valeur_origine_plusieurs_lignes"])}
                comptes["reecrites"] += 1
                comptes["replis_vides"] += int(choix["repli_vide"])
                comptes["separateurs_inseres"] += int(rr["separateur_insere"])
                comptes["elargies"] += int(rr["elargie"])
                comptes["a_la_coupe"] += int(rr["a_la_coupe"])
                compter(o, t0)
            sortie = {"schema": SCHEMA_ORACLE, "oracle": o, "phase": phase, "episode": episode, "pas": t,
                      "champ_cout": bool(coupe["champ_cout"]), "coupe_conforme": bool(coupe["conforme"]), "rang_coupe": coupe["rang"],
                      "motif_coupe": coupe["motif"], "cout_declare": lu["cout_declare"], "cout_lisible": bool(lu["cout_lisible"]),
                      "fenetre": lu["fenetre"], "ancien_lecteur": lu["ancien_lecteur"],
                      "ecart_des_deux_lecteurs": bool(lu["ecart_des_deux_lecteurs"]), "suites": lect, "n_lisibles": int(n_lis),
                      "estimation": estimation, "bornable": bornable, "exces": exces, "sans_ancre_commune": bool(sans_ancre),
                      "empreinte_prefixe": r["empreinte"] if r is not None else None, "dernier_cout_contexte": dernier[o],
                      "dernier_cout_agent": dernier_agent, "couplage": couplage}
            if set(sortie) != CLES_ORACLE:
                raise GardeArret("oracle : sortie hors du schéma (défaut de code)")
            sorties[o].append(sortie)
            suites_par[o].append(r["suites"] if r is not None else [])
            dans = _action_dans_le_contexte(o, t, a_ids, reecrite)
            if t == 0:
                empan_premiere[o] = (len(ctx[o]), len(ctx[o]) + len(dans))
            ctx[o] = ctx[o] + dans + list(fmt.cloture(debut, dans))
            journal[o].append((0, t, tok.decode(dans, skip_special_tokens=True)))
            if o == "N":
                retenues.append(None if couplage is None or couplage["repli_vide"] else list(r["suites"][couplage["indice"]]))
                reecrites.append({"ids": list(dans), "reecrite": reecrite is not None, "repli_vide": bool(couplage and couplage["repli_vide"])})
            # dernier coût lisible porté par le contexte du jumeau après cette action
            if o == "N" and reecrite is not None:
                v = None if couplage["repli_vide"] else lect[couplage["indice"]]["valeur"]
            else:
                v = lu["cout_declare"] if coupe["conforme"] else lu["ancien_lecteur"]
            if v is not None:
                dernier[o] = float(v)
        va = lu["cout_declare"] if coupe["conforme"] else lu["ancien_lecteur"]
        if va is not None:
            dernier_agent = float(va)
    return {"sorties": sorties, "suites": suites_par, "retenues": retenues, "reecrites": reecrites, "comptes": comptes,
            "lectures": lectures, "sans_ancre_commune": sans_ancre}


def exiger_aucun_texte(sorties) -> None:
    """Aucun texte dans les sorties : toute chaîne est le schéma, le nom de l'oracle, de la phase ou de l'épisode, un code de
    motif de coupe, un cas du couplage ou une empreinte."""
    for s in sorties:
        permis = {s["schema"], s["oracle"], s["phase"], s["episode"], s["empreinte_prefixe"], *MOTIFS_COUPE, "a", "b"}

        def voir(x):
            if isinstance(x, dict):
                for v in x.values():
                    voir(v)
            elif isinstance(x, (list, tuple)):
                for v in x:
                    voir(v)
            elif isinstance(x, str) and x not in permis:
                raise GardeArret("sortie de l'oracle : une chaîne qui n'est ni un code ni une empreinte (aucun texte permis)")
        voir(s)
