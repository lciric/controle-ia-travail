"""Cœur de la course du bras A des organismes discrets (préenregistrement `prereg/T0.7-organismes-discrets-v-a-v1.md`,
06ab6a2f… ; addenda `…-addendum-lecture-lot-de-huit-v1.md`, bd6ae8df…, et `…-addendum-2-pas-de-distillation-v1.md`,
4f9af3c5… ; registre `registres/organismes-discrets-v-a-addenda-v2.md`).

Ce module ne fait que du calcul sur un modèle déjà chargé ; il n'ouvre aucune machine et ne lit aucune ligne de dépense
(la session de machine louée et ses gardes viendront dans un module à part). Il **n'importe aucun module de sondes, de
bases ni de lecture** : ni `environnements.lancer_pilote_a`, ni les lanceurs et configurations de `t06` (qui en chargent).

Étapes, dans l'ordre :
1. `jouer_honnetes` : épisodes honnêtes du modèle de base (une action par épisode et par pas, lot d'épisodes en
   parallèle ; graines par (tâche, épisode), puis par (agent, pas) — addendum 1, section 1) ;
2. `fabriquer` : déplacement du champ entre les actions de chaque épisode, au grain du jeton (identifiants déplacés tels
   quels, jamais retokenisés), par `fabrication_v3` (v2 du lanceur : seul changement, la fabrication v3, qui admet un jeton à cheval fait de blancs) ; textes recalculés ; garde « le contexte honnête reconstruit ne
   change pas » ; comptes au bilan ;
3. `exemples` : transcriptions honnêtes reconstruites, perte sur les seuls jetons d'action, aucune exclusion ;
4. `distiller_tous` : un adaptateur par condition distillée, tous au même nombre de pas déclaré (addendum 2 : garde,
   arrêt avant distillation si le nombre calculé diffère), base inchangée vérifiée par empreinte ;
5. `controler_identite` : à l'échelle 0, logits égaux au bit près à ceux de la base ; à l'échelle 1, différents (M-4) ;
6. `rejouer` : épisodes des tâches de vérification, condition honnête sans adaptation puis chaque adaptateur à l'échelle 1,
   **mêmes graines d'action d'une condition à l'autre** ; état de phase vérifié avant et après chaque lot.
Les activations capturées par le jeu d'épisodes ne sont ni gardées ni lues (le texte scellé n'en demande aucune).
"""
from __future__ import annotations

import hashlib

import torch

from ..environnements.pilote_a import graines_des_actions, tache_de
from ..gardes import GardeArret
from ..harnais.episode import jouer_episodes
from ..harnais.formats import FormatChat
from ..manifeste import generateur
from ..organismes import lora as lo
from ..premier_test_ia.conditions import environnement
from ..t06 import distillation_transcription as dt
from ..t06.identite import controle_identite, exiger_etat_de_phase, logits_de_controle
from . import fabrication_v3 as fab

CONDITION_HONNETE = "H"


def charger_modele_et_format(spec: dict, mode: str, graine_jouet: int, hors_ligne: bool = False):
    """Modèle et format, sans passer par `environnements.lancer_pilote_a` (qui charge des modules de sondes) : mêmes
    réglages que lui (réel : révision et gabarit figés ; jouet : modèle par caractères)."""
    from ..harnais.modeles import charger_modele, fins_du_modele, modele_jouet, tokeniseur_caracteres_chat
    if mode == "jouet":
        tok = tokeniseur_caracteres_chat()
        m = modele_jouet(graine_jouet, len(tok), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
        return m, FormatChat(tok, fins={tok.convert_tokens_to_ids("<|im_end|>"), tok.eos_token_id})
    m, tok = charger_modele(spec["modele"], spec["revision"], "bfloat16", "cuda", "sdpa", hors_ligne=hors_ligne)
    fmt = FormatChat(tok, variables=spec["variables_gabarit"])
    fmt.fins = fins_du_modele(m, tok) | {fmt._pieces(("x", "y"))["cloture"][0]}
    return m, fmt


def graine_entiere(graine: dict) -> int:
    return int(generateur(graine).integers(0, 2 ** 63 - 1))


def nom_adaptateur(champ: str | None, dose: float) -> str:
    """`controls-0.50` (bras A), `identite` (témoin (vi-T)), `prediction-1.00` (témoin (vi-B))."""
    return "identite" if champ is None else f"{champ.lower()}-{dose:.2f}"


def plan_des_adaptateurs(config: dict) -> list[tuple[str, str | None, float]]:
    """(nom, champ, dose de fabrication) : un adaptateur par dose non nulle du bras A, le témoin identité, et le témoin
    bénin aux proportions données par la configuration (une ou plusieurs : lecture à trancher par Lazar)."""
    doses = [float(p) for p in config["doses_fabrication"]]
    benin = [float(p) for p in config["proportions_temoin_benin"]]
    for p in doses + benin:
        if p not in fab.DOSES or p == 0.0:
            raise GardeArret(f"dose {p!r} hors de la grille non nulle {fab.DOSES[1:]}")
    if len(set(doses)) != len(doses) or len(set(benin)) != len(benin) or not doses or not benin:
        raise GardeArret("doses de fabrication et proportions du témoin bénin : listes non vides, sans doublon")
    return ([(nom_adaptateur("CONTROLS", p), "CONTROLS", p) for p in doses] + [("identite", None, 1.0)]
            + [(nom_adaptateur("PREDICTION", p), "PREDICTION", p) for p in benin])


def cles_des_graines(config: dict, fabrication: list[dict], verification: list[dict]) -> list[str]:
    cles = ["modele-jouet", "injection"]
    for nom, _, _ in plan_des_adaptateurs(config):
        cles += [f"adaptateur/{nom}", f"distillation/{nom}"]
    for prefixe, taches in (("fabrication", fabrication), ("verification", verification)):
        cles += [f"{prefixe}/tache/{t['identifiant']}/e{k}" for t in taches for k in range(int(config["episodes_par_tache"]))]
    return cles


def _lots(plan: list, lot: int) -> list[list]:
    return [plan[d:d + lot] for d in range(0, len(plan), lot)]


def jouer_honnetes(modele, fmt, taches: list[dict], config: dict, g: dict, guide, prefixe: str, chrono=None,
                   avant_lot=None, apres_lot=None) -> list[dict]:
    """Épisodes de l'environnement honnête sur les tâches données ; la graine de l'épisode (tâche, k) est la clé
    `{prefixe}/tache/{id}/e{k}`, la même quelle que soit la condition jouée. Rend, par épisode : identifiant, tâche, k,
    identifiants de jetons et texte de chaque action."""
    T, lot = int(config["T"]), int(config["lot"])
    plan = [(f"{prefixe}/{t['identifiant']}/e{k}", t, k) for t in taches for k in range(int(config["episodes_par_tache"]))]
    sorties = []
    for morceau in _lots(plan, lot):
        envs = [environnement("honnete", tache_de(t), T, guide, {}) for _, t, _ in morceau]
        graines = [graines_des_actions(generateur(g[f"{prefixe}/tache/{t['identifiant']}/e{k}"]), 1, T) for _, t, k in morceau]
        if avant_lot is not None:
            avant_lot()
        res = jouer_episodes(modele, fmt, envs, [e for e, _, _ in morceau], 1, T, graines, config["couches"],
                             config["max_nouveaux"], config["temperature"], set(), config["tolerance_equivalence"], chrono=chrono)
        if apres_lot is not None:
            apres_lot()
        for (ep, _acts, _rapport), (e, t, k) in zip(res, morceau):       # activations ni gardées ni lues
            actions = ep.actions_dans_l_ordre()
            if len(actions) != T:
                raise GardeArret(f"épisode {e} : {len(actions)} actions pour {T} pas")
            sorties.append({"episode": e, "tache": t, "k": k, "actions": [list(a.ids) for a in actions],
                            "textes": [a.texte for a in actions]})
    return sorties


def _decoder(fmt):
    return lambda ids: fmt.tok.decode(list(ids), skip_special_tokens=True)


def fabriquer(fmt, episodes: list[dict], champ: str | None, dose: float, entropie: int, config: dict, guide) -> dict:
    """Épisodes fabriqués pour un adaptateur : mêmes épisodes, champ déplacé à la dose donnée (`champ=None` : identité).
    Rend les épisodes (identifiants et textes recalculés) et le bilan des comptes."""
    decoder, T = _decoder(fmt), int(config["T"])
    sorties, fabriques = [], []
    for ep in episodes:
        triplets = []
        for ids, texte in zip(ep["actions"], ep["textes"]):
            if decoder(ids) != texte:
                raise GardeArret(f"épisode {ep['episode']} : le texte d'une action n'est pas le décodage de ses identifiants")
            triplets.append((list(ids), fab.decalages_par_decodage(decoder, ids, texte), texte))
        f = fab.fabriquer_episode_jetons(triplets, dose, champ, entropie, ep["tache"]["identifiant"], ep["k"])
        actions = [list(a) for a in f.actions]
        if [len(a) for a in actions] != [len(a) for a in ep["actions"]] and not f.deplacements:
            raise GardeArret(f"épisode {ep['episode']} : longueurs changées sans déplacement")
        if sorted(x for a in actions for x in a) != sorted(x for a in ep["actions"] for x in a):
            raise GardeArret(f"épisode {ep['episode']} : multiensemble des jetons non conservé (M-3)")
        # garde : le contexte honnête reconstruit hors des actions ne dépend pas du déplacement
        env = environnement("honnete", tache_de(ep["tache"]), T, guide, {})
        avant, empans_a = dt.transcription_honnete(fmt, env, ep["actions"])
        env = environnement("honnete", tache_de(ep["tache"]), T, guide, {})
        apres, empans_b = dt.transcription_honnete(fmt, env, actions)
        if _hors_des_empans(avant, empans_a) != _hors_des_empans(apres, empans_b):
            raise GardeArret(f"épisode {ep['episode']} : le déplacement change le contexte honnête reconstruit")
        sorties.append({"episode": ep["episode"], "tache": ep["tache"], "k": ep["k"], "actions": actions,
                        "textes": [decoder(a) for a in actions], "deplacements": {str(i): j for i, j in f.deplacements.items()},
                        "laisse_honnete": f.laisse_honnete})
        fabriques.append(f)
    return {"episodes": sorties, "bilan": fab.bilan(fabriques)}


def _hors_des_empans(ids: list[int], empans: list[tuple[int, int]]) -> list[list[int]]:
    morceaux, fait = [], 0
    for d, f in empans:
        morceaux.append(list(ids[fait:d]))
        fait = f
    return morceaux + [list(ids[fait:])]


def exemples(fmt, episodes: list[dict], config: dict, guide) -> list[tuple[list[int], list[int]]]:
    """Une transcription honnête reconstruite par épisode, perte sur tous les jetons d'action (aucune exclusion)."""
    T, sortie = int(config["T"]), []
    for ep in episodes:
        env = environnement("honnete", tache_de(ep["tache"]), T, guide, {})
        ids, empans = dt.transcription_honnete(fmt, env, ep["actions"])
        sortie.append(dt.exemple_de_transcription(ids, empans, list(range(T))))
    return sortie


def pas_calcules(n_exemples: int, config: dict) -> int:
    d = config["distillation"]
    return -(-n_exemples // int(d["lot"])) * int(d["epoques"])


def distiller_tous(modele, fmt, episodes: list[dict], config: dict, g: dict, guide, entropie: int, pad_id: int,
                   progres=None) -> dict:
    """Injection (une fois), puis un adaptateur par condition distillée. Rend, par nom : état entraîné (float32), empreinte,
    bilan de fabrication, pas déclarés et calculés, journal de l'entraînement ; et l'empreinte de la base."""
    a, d = config["adaptateur"], config["distillation"]
    plan = plan_des_adaptateurs(config)
    donnees = {nom: fabriquer(fmt, episodes, champ, dose, entropie, config, guide) for nom, champ, dose in plan}
    jeux = {nom: exemples(fmt, donnees[nom]["episodes"], config, guide) for nom, _, _ in plan}
    for nom, jeu in jeux.items():                    # addendum 2 : garde avant toute distillation
        if pas_calcules(len(jeu), config) != int(d["pas_declares"]):
            raise GardeArret(f"adaptateur {nom} : {pas_calcules(len(jeu), config)} pas calculés ≠ {d['pas_declares']} déclarés "
                             "(addendum 2) : arrêt avant distillation, nœud")
    lo.injecter(modele, a["rang"], a["alpha"], graine_entiere(g["injection"]), tuple(a["cibles"]))
    dt.adaptateurs_en_simple_precision(modele)
    base = lo.empreinte_base(modele)
    sortie = {}
    for nom, champ, dose in plan:
        lo.charger_etat(modele, dt.etat_initial(modele, a["rang"], a["alpha"], graine_entiere(g[f"adaptateur/{nom}"])))
        lo.fixer_dose(modele, 1.0)
        journal = dt.distiller_transcriptions(modele, jeux[nom], pad_id, d["epoques"], d["pas"], d["lot"],
                                              graine_entiere(g[f"distillation/{nom}"]), d["norme_max"], progres=progres)
        if lo.empreinte_base(modele) != base:
            raise GardeArret(f"adaptateur {nom} : la base a changé pendant la distillation")
        sortie[nom] = {"etat": {k: v.detach().to("cpu").clone() for k, v in lo.etat_lora(modele).items()},
                       "empreinte": lo.empreinte_adaptateurs(modele), "champ": champ, "dose_fabrication": dose,
                       "bilan_fabrication": donnees[nom]["bilan"], "pas_declares": int(d["pas_declares"]),
                       "pas_calcules": pas_calcules(len(jeux[nom]), config), "journal": journal,
                       "episodes_fabriques": donnees[nom]["episodes"]}
    return {"adaptateurs": sortie, "empreinte_base": base}


def controler_identite(modele, ids_controle: list[int], logits_base: torch.Tensor, adaptateurs: dict) -> dict:
    """M-4 : pour chaque adaptateur, logits égaux au bit près à ceux de la base à l'échelle 0, différents à l'échelle 1."""
    return controle_identite(modele, ids_controle, logits_base, {nom: x["etat"] for nom, x in adaptateurs.items()})


def rejouer(modele, fmt, taches: list[dict], config: dict, g: dict, guide, adaptateurs: dict, chrono=None) -> dict:
    """Épisodes des tâches de vérification : condition honnête (échelle 0 de l'adaptation, base au bit près) puis chaque
    adaptateur à l'échelle 1. Mêmes graines d'action d'une condition à l'autre."""
    sorties = {}
    for condition in [CONDITION_HONNETE] + list(adaptateurs):
        nom = next(iter(adaptateurs)) if condition == CONDITION_HONNETE else condition
        echelle = 0.0 if condition == CONDITION_HONNETE else 1.0
        lo.charger_etat(modele, adaptateurs[nom]["etat"])
        lo.fixer_dose(modele, echelle)
        empreinte = lo.empreinte_adaptateurs(modele)
        garde = lambda: exiger_etat_de_phase(modele, echelle, empreinte, f"rejeu, condition {condition}")  # noqa: E731
        sorties[condition] = jouer_honnetes(modele, fmt, taches, config, g, guide, "verification", chrono,
                                            avant_lot=garde, apres_lot=garde)
    return sorties


def empreinte_des_episodes(episodes: list[dict]) -> str:
    h = hashlib.sha256()
    for ep in episodes:
        h.update(ep["episode"].encode("utf-8"))
        for a in ep["actions"]:
            h.update(b"|" + ",".join(str(int(x)) for x in a).encode("ascii"))
    return h.hexdigest()
