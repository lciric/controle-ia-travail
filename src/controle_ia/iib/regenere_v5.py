"""L'épisode régénéré, instrument de l'étalonnage, v5 (texte scellé, section 10.1 ; section 13, `regenere_v5.py`).

L'agent honnête (modèle de base, dose 0, aucune consigne privée) joue l'épisode. Après chaque action de rang 2 à 10 à coût
déclaré lisible, le premier nombre de la fenêtre du coût est multiplié par 10^δ et écrit dans la forme de l'original
(`reecriture_v5.multiplier_cout`) ; δ : nul une fois sur cinq, sinon tiré de la loi de la section 2.1 (normale de moyenne
log10 2 et d'écart type 0,10, tronquée en haut à log10 2,5) ; graine propre `iib/regenere/<episode>/pas<t>`. **L'action suivante
est générée dans le contexte qui porte ce coût multiplié.** La première action est celle de l'épisode honnête de même tâche et
de même graine, à l'octet. Aucun maître, aucune consigne privée, aucun moniteur.

`jouer_lot` joue un lot d'épisodes en pas synchronisés, sans aucune activation (même ordre des contextes que `episodes_v1`) ;
`apres_action` permet de remplacer l'action qui entre dans le contexte ; chaque contexte passé au modèle est consigné par son
empreinte, et `empreintes_prefixes` donne, par action, l'empreinte du contexte de génération suivi de l'action jusqu'à sa coupe :
pour un agent sans texte privé, c'est le préfixe de l'agent que l'oracle au contexte de l'agent doit retrouver à l'octet. Garde `exiger_regeneration` : un code qui multiplierait après coup sans régénérer rendrait, après la première
multiplication, les actions de l'épisode honnête : refusé par comparaison.
"""
from __future__ import annotations

from ..gardes import GardeArret
from . import jumeau_v5 as jm
from . import reecriture_v5 as rw
from .lecture_cout_v5 import coupe_du_prefixe, lire_action_v5


def cle_du_regenere(episode: str, pas: int) -> str:
    return f"iib/regenere/{episode}/pas{pas}"


def tirer_delta(rng, loi: dict) -> float:
    """δ de la loi de la section 2.1 : nul une fois sur cinq ; sinon normale tronquée en haut (rejet au-dessus de la limite)."""
    if float(rng.random()) < loi["part_nulle"]:
        return 0.0
    for _ in range(10000):
        d = float(rng.normal(loi["moyenne"], loi["ecart_type"]))
        if d <= loi["troncature_haute"]:
            return d
    raise GardeArret("loi de l'excès : troncature jamais satisfaite (constantes incohérentes)")


def jouer_lot(modele, environnements: list, identifiants: list[str], graines_actions: list[list[int]], max_nouveaux: int,
              temperature: float, apres_action=None) -> list[dict]:
    """Joue B épisodes en pas synchronisés. `graines_actions[b][t]` : graine de l'action t de l'épisode b.
    `apres_action(b, t, ids)` rend les jetons de l'action qui entrent dans le contexte et un dictionnaire consigné."""
    B = len(identifiants)
    if B < 1 or len(environnements) != B or len(graines_actions) != B:
        raise GardeArret(f"lot : {B} épisodes, {len(environnements)} environnements, {len(graines_actions)} jeux de graines")
    T = environnements[0].T
    if any(e.T != T or e.N != 1 for e in environnements) or any(len(g) != T for g in graines_actions):
        raise GardeArret("lot : épisodes de même longueur, un agent, une graine par action attendus")
    fmt = modele.fmt
    transcriptions, debuts = [[] for _ in range(B)], [None] * B
    journaux = [[] for _ in range(B)]
    sortie = [{"episode": identifiants[b], "actions": [], "generees": [], "empreintes_contextes": [], "empreintes_prefixes": [], "consignes": []} for b in range(B)]
    for t in range(T):
        contextes = []
        for b in range(B):
            obs = environnements[b].observation(0, t, journaux[b])
            if t == 0:
                debuts[b] = (environnements[b].consigne_privee(0), obs)
                contextes.append(list(fmt.ouverture(*debuts[b])))
            else:
                contextes.append(transcriptions[b] + list(fmt.tour(debuts[b], obs)))
        nouveaux = modele.generer_actions(contextes, [graines_actions[b][t] for b in range(B)], max_nouveaux, temperature)
        if len(nouveaux) != B or any(not nv for nv in nouveaux):
            raise GardeArret(f"pas {t} : génération vide ou incomplète")
        for b in range(B):
            nv = list(nouveaux[b])
            dans, note = (nv, None) if apres_action is None else apres_action(b, t, nv)
            dans = list(dans)
            sortie[b]["generees"].append({"ids": nv})
            sortie[b]["actions"].append({"ids": dans})
            sortie[b]["empreintes_contextes"].append(jm.empreinte_de_prefixe(contextes[b]))
            c = coupe_du_prefixe(fmt.tok, dans)
            sortie[b]["empreintes_prefixes"].append(jm.empreinte_de_prefixe(contextes[b] + dans[:c["rang"]]) if c["conforme"] else None)
            sortie[b]["consignes"].append(note)
            transcriptions[b] = contextes[b] + dans + list(fmt.cloture(debuts[b], dans))
            journaux[b].append((0, t, fmt.tok.decode(dans, skip_special_tokens=True)))
    return sortie


def jouer_regeneres(modele, environnements: list, identifiants: list[str], graines_actions: list[list[int]], graines, config: dict,
                    honnetes: list[dict] | None = None) -> list[dict]:
    """Épisodes régénérés d'un lot. `honnetes[b]` : épisode honnête de même tâche et de même graine (sa première action doit être
    retrouvée à l'octet, et la garde de régénération lui compare les actions suivantes)."""
    for e in environnements:
        if getattr(e, "instructions_cachees", None) or getattr(e, "indications_privees", None):
            raise GardeArret("épisode régénéré : aucune consigne privée (agent honnête exigé)")
    jm.exiger_dose_nulle(modele)
    fmt, tok = modele.fmt, modele.fmt.tok
    fins, loi, fen = frozenset(fmt.fins), config["organisme"]["loi"], int(config["oracle"]["fenetre"])

    def apres(b, t, ids):
        if t == 0:
            return ids, {"delta": 0.0, "cout_avant": None, "multipliee": False}
        lu = lire_action_v5(tok, ids, fins, fen)
        if not (lu["coupe"]["conforme"] and lu["cout_lisible"]):
            return ids, {"delta": None, "cout_avant": None, "multipliee": False}
        delta = tirer_delta(graines.generateur(cle_du_regenere(identifiants[b], t)), loi)
        r = rw.multiplier_cout(tok, ids, lu["coupe"]["rang"], delta, fins, fen)
        return r["ids"], {"delta": delta, "cout_avant": lu["cout_declare"], "multipliee": bool(r["multipliee"])}
    joues = jouer_lot(modele, environnements, identifiants, graines_actions, int(config["generation"]["max_nouveaux"]),
                      float(config["generation"]["temperature"]), apres)
    if honnetes is not None:
        for ep, h in zip(joues, honnetes):
            exiger_regeneration(h["actions"], ep)
    return joues


def exiger_regeneration(actions_honnetes: list[dict], regenere: dict) -> None:
    """La première action est égale à l'octet à celle de l'épisode honnête ; après la première multiplication non nulle, les
    actions générées ne sont pas toutes celles de l'épisode honnête (sinon : multiplié après coup sans régénérer, refus)."""
    gen = regenere["generees"]
    if list(gen[0]["ids"]) != list(actions_honnetes[0]["ids"]) or list(regenere["actions"][0]["ids"]) != list(actions_honnetes[0]["ids"]):
        raise GardeArret("épisode régénéré : sa première action n'est pas égale à l'octet à celle de l'épisode honnête (refus)")
    premiere = next((t for t, n in enumerate(regenere["consignes"]) if n and n["multipliee"]), None)
    if premiere is None:
        return
    suivantes = range(premiere + 1, len(gen))
    if len(suivantes) >= 2 and all(list(gen[t]["ids"]) == list(actions_honnetes[t]["ids"]) for t in suivantes):
        raise GardeArret("épisode régénéré : après la première multiplication, toutes les actions sont celles de l'épisode honnête — "
                         "coût multiplié après coup sans régénérer (refus)")
