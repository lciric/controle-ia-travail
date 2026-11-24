"""Conditions de la course de dose–réponse de l'organisme à consigne cachée (texte scellé
`prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md`, 2263c5c4…, plan d'analyse, points 2, 3 et 5).

- Quinze conditions, dans l'ordre de la table du point 2 du plan.
- Textes privés : pièce jointe `consignes-privees-dose-reponse-consigne-cachee-v4.json` (onze conditions, huit consignes
  distinctes, note commune), lue sous son empreinte ; textes du premier test (`prereg/P3-consignes-v1.md`) lus par
  `premier_test_ia.conditions.charger_consignes` sous leur empreinte. Aucun texte n'est écrit dans ce code, ni affiché par lui.
- Place : la consigne à la fin du message système (`instructions_cachees`), la note juste avant « Your action: » aux pas
  désignés (`indications_privees`). Pas désignés : les dix (« tous »), aucun (`dormant_10`), ou les 2 et 5 premiers d'une
  permutation des dix pas tirée de la graine `pas-designes/<tâche>/<réplique>` (emboîtés). Conditions du premier test :
  consigne et indication à chaque pas, comme au premier test.
- Contrôle d'injection, sur chaque épisode : l'environnement porte exactement la consigne et les pas prévus, et les jetons
  de la transcription égalent, au jeton près, ceux que reconstruit le format à partir de l'environnement prévu et des
  actions générées (message système, note aux pas prévus et nulle part ailleurs, `honnete` sans texte privé).
- Longueurs en jetons des huit consignes distinctes : rapport du plus long au plus court au plus 1,15.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

from ..environnements.propositions import EnvironnementPropositions
from ..gardes import GardeArret
from ..premier_test_ia.conditions import charger_consignes
from ..scellement import verifier

CONDITIONS = ("honnete", "consigne_benigne", "consigne_neutre", "gonfle_1_25", "gonfle_1_5", "gonfle_2", "gonfle_3",
              "gonfle_5", "gonfle_10", "dormant_10", "proportion_20_10", "proportion_50_10", "saboteur_premier_test",
              "temoin_premier_test", "mention_premier_test")
CONDITIONS_PIECE_JOINTE = CONDITIONS[1:12]
CONDITIONS_PREMIER_TEST = {"saboteur_premier_test": "saboteur", "temoin_premier_test": "temoin",
                           "mention_premier_test": "mention"}
INTENSITES = {"consigne_neutre": 1.0, "gonfle_1_25": 1.25, "gonfle_1_5": 1.5, "gonfle_2": 2.0, "gonfle_3": 3.0,
              "gonfle_5": 5.0, "gonfle_10": 10.0}
PROPORTIONS = {"dormant_10": 0.0, "proportion_20_10": 0.2, "proportion_50_10": 0.5, "gonfle_10": 1.0}
FACTEURS_ECRITS = (1.25, 1.5, 2.0, 3.0, 5.0, 10.0)
# forme attendue de la pièce jointe (facteur écrit, proportion écrite, pas portant la note) ; aucun texte
FORME_PIECE_JOINTE = {
    "consigne_benigne": (None, None, "tous"), "consigne_neutre": (1.0, 1.0, "tous"),
    "gonfle_1_25": (1.25, 1.0, "tous"), "gonfle_1_5": (1.5, 1.0, "tous"), "gonfle_2": (2.0, 1.0, "tous"),
    "gonfle_3": (3.0, 1.0, "tous"), "gonfle_5": (5.0, 1.0, "tous"), "gonfle_10": (10.0, 1.0, "tous"),
    "dormant_10": (10.0, 0.0, "aucun"), "proportion_20_10": (10.0, 0.2, "tirage_2"), "proportion_50_10": (10.0, 0.5, "tirage_5"),
}
PAS_TIRES = {"tirage_2": 2, "tirage_5": 5}
RAPPORT_LONGUEURS_MAX = 1.15
T_ATTENDU = 10


def _sha(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def charger_piece_jointe(chemin, sha_attendue: str) -> dict:
    """Pièce jointe des textes privés, sous son empreinte (R11) ; forme exigée, jamais réparée."""
    sha = verifier(chemin)
    if sha != sha_attendue:
        raise GardeArret(f"{chemin} : empreinte {sha[:12]} ≠ empreinte citée {sha_attendue[:12]} (R11) : aucune création")
    d = json.loads(Path(chemin).read_text(encoding="utf-8"))
    conds = d.get("conditions")
    if not isinstance(conds, list) or [c.get("nom") for c in conds] != list(CONDITIONS_PIECE_JOINTE):
        raise GardeArret(f"{chemin} : conditions {[c.get('nom') for c in conds or []]} ≠ {list(CONDITIONS_PIECE_JOINTE)}")
    note = d.get("note_commune")
    if not isinstance(note, str) or not note.strip():
        raise GardeArret(f"{chemin} : note commune absente")
    sortie = {"sha256": sha}
    for c in conds:
        forme = (c.get("facteur_ecrit"), c.get("proportion_ecrite"), c.get("pas_avec_note"))
        if forme != FORME_PIECE_JOINTE[c["nom"]]:
            raise GardeArret(f"{chemin} : condition {c['nom']} de forme {forme}, {FORME_PIECE_JOINTE[c['nom']]} attendue")
        if not isinstance(c.get("consigne"), str) or not c["consigne"].strip():
            raise GardeArret(f"{chemin} : condition {c['nom']} sans consigne")
        attendue = None if c["pas_avec_note"] == "aucun" else note
        if c.get("note") != attendue:
            raise GardeArret(f"{chemin} : condition {c['nom']} : note autre que la note commune (ou présente sans pas désigné)")
        sortie[c["nom"]] = {"consigne": c["consigne"], "note": c["note"], "pas": c["pas_avec_note"]}
    for nom in ("dormant_10", "proportion_20_10", "proportion_50_10"):
        if sortie[nom]["consigne"] != sortie["gonfle_10"]["consigne"]:
            raise GardeArret(f"{chemin} : {nom} ne porte pas la consigne de gonfle_10 (plan, point 2)")
    distinctes = {sortie[n]["consigne"] for n in CONDITIONS_PIECE_JOINTE}
    if len(distinctes) != 8:
        raise GardeArret(f"{chemin} : {len(distinctes)} consignes distinctes, huit attendues")
    return sortie


def charger_textes(chemin_pj, sha_pj: str, chemin_p3, sha_p3: str) -> dict:
    """Textes des quinze conditions : {condition: {consigne, note, pas}} et les empreintes des deux fichiers.
    Conditions du premier test : consigne et indication de `charger_consignes`, à chaque pas (« tous »)."""
    pj = charger_piece_jointe(chemin_pj, sha_pj)
    p3 = charger_consignes(chemin_p3, sha_p3)
    textes = {"honnete": {"consigne": None, "note": None, "pas": "aucun"}}
    for c in CONDITIONS_PIECE_JOINTE:
        textes[c] = pj[c]
    for c, source in CONDITIONS_PREMIER_TEST.items():
        textes[c] = {"consigne": p3[source]["consigne"], "note": p3[source]["indication"], "pas": "tous"}
    return {"textes": textes, "piece_jointe_sha256": pj["sha256"], "premier_test_sha256": p3["sha256"]}


def permutation_des_pas(gen: np.random.Generator, T: int = T_ATTENDU) -> list[int]:
    """`permutation(10)` du générateur de la graine `pas-designes/<tâche>/<réplique>` (plan, point 3)."""
    return [int(x) for x in gen.permutation(T)]


def pas_portant_la_note(condition: str, textes: dict, permutation: list[int], T: int = T_ATTENDU) -> list[int]:
    if condition not in CONDITIONS:
        raise GardeArret(f"condition {condition!r} hors des quinze du plan")
    if sorted(permutation) != list(range(T)):
        raise GardeArret(f"permutation des pas illisible : {permutation}")
    pas = textes[condition]["pas"]
    if pas == "tous":
        return list(range(T))
    if pas == "aucun":
        return []
    if pas in PAS_TIRES:
        return sorted(permutation[:PAS_TIRES[pas]])
    raise GardeArret(f"pas portant la note de {condition} : {pas!r} inconnu")


def plan_injection(condition: str, textes: dict, permutation: list[int], T: int = T_ATTENDU) -> dict:
    """Ce que l'épisode doit porter : empreinte de la consigne (None pour `honnete`) et pas de la note."""
    t = textes[condition]
    pas = pas_portant_la_note(condition, textes, permutation, T)
    return {"condition": condition, "consigne_sha256": None if t["consigne"] is None else _sha(t["consigne"]),
            "note_sha256": None if not pas else _sha(t["note"]), "pas_designes": pas}


def environnement(condition: str, tache, T: int, guide: str | None, textes: dict,
                  permutation: list[int]) -> EnvironnementPropositions:
    """Environnement (a) d'un épisode de la condition (un agent)."""
    t = textes[condition]
    if t["consigne"] is None:
        if condition != "honnete":
            raise GardeArret(f"condition {condition} sans consigne")
        return EnvironnementPropositions(tache, 1, T, guide)
    pas = pas_portant_la_note(condition, textes, permutation, T)
    return EnvironnementPropositions(tache, 1, T, guide, instructions_cachees={0: t["consigne"]},
                                     indications_privees={(0, s): t["note"] for s in pas})


def jetons_attendus(fmt, env, actions_ids: list[list[int]]) -> list[int]:
    """Transcription que le harnais (`jouer_episodes`, un agent) doit avoir construite pour cet environnement et ces actions
    générées : ouverture (message système, première observation), puis, à chaque pas, l'action, sa clôture et l'observation
    suivante. Reconstruction indépendante de la génération."""
    journal, ids, debut = [], [], None
    tok = fmt.tok
    for t, nv in enumerate(actions_ids):
        obs = env.observation(0, t, journal)
        if t == 0:
            debut = (env.consigne_privee(0), obs)
            ctx = fmt.ouverture(*debut)
        else:
            ctx = ids + fmt.tour(debut, obs)
        ids = ctx + list(nv) + fmt.cloture(debut, list(nv))
        journal.append((0, t, tok.decode(list(nv), skip_special_tokens=True)))
    return ids


def controle_injection_episode(fmt, env, episode, plan: dict, textes: dict) -> dict:
    """Contrôle d'injection d'un épisode joué (plan, point 5) : lève `GardeArret` à la première faute (ligne C1)."""
    c = plan["condition"]
    t = textes[c]
    nom = episode.identifiant
    if t["consigne"] is None:
        if env.instructions_cachees or env.indications_privees:
            raise GardeArret(f"injection : {nom} ({c}) porte un texte privé")
    else:
        if set(env.instructions_cachees) != {0} or _sha(env.instructions_cachees[0]) != plan["consigne_sha256"]:
            raise GardeArret(f"injection : {nom} ({c}) : consigne ≠ celle de sa condition")
        if not env.consigne_privee(0).endswith(env.instructions_cachees[0].strip() + "\n"):
            raise GardeArret(f"injection : {nom} ({c}) : consigne absente de la fin du message système")
        pas = sorted(s for (_, s) in env.indications_privees)
        if pas != plan["pas_designes"] or any(_sha(v) != plan["note_sha256"] for v in env.indications_privees.values()):
            raise GardeArret(f"injection : {nom} ({c}) : note aux pas {pas}, pas prévus {plan['pas_designes']}")
    tr = episode.transcriptions
    if len(tr) != 1:
        raise GardeArret(f"injection : {nom} : un agent attendu")
    actions = sorted(tr[0].actions, key=lambda a: a.pas)
    if [a.pas for a in actions] != list(range(env.T)):
        raise GardeArret(f"injection : {nom} : pas joués {[a.pas for a in actions]}")
    attendus = jetons_attendus(fmt, env, [a.ids for a in actions])
    if list(tr[0].ids) != attendus:
        raise GardeArret(f"injection : {nom} ({c}) : jetons de la transcription ≠ jetons reconstruits de l'environnement prévu")
    for a in actions:
        if list(tr[0].ids[a.debut:a.fin]) != list(a.ids):
            raise GardeArret(f"injection : {nom} : empan de l'action {a.pas} ≠ ses identifiants")
    return {"episode": nom, "condition": c, "consigne_sha256": plan["consigne_sha256"], "pas_designes": plan["pas_designes"],
            "jetons": len(attendus), "conforme": True}


def longueurs_en_jetons(tok, textes: dict) -> dict:
    """Longueurs en jetons des huit consignes distinctes de la pièce jointe (sans jeton spécial) et leur rapport."""
    vues = {}
    for c in CONDITIONS_PIECE_JOINTE:
        s = textes[c]["consigne"]
        if s not in vues:
            vues[s] = (c, len(tok(s, add_special_tokens=False)["input_ids"]))
    if len(vues) != 8:
        raise GardeArret(f"{len(vues)} consignes distinctes, huit attendues")
    longueurs = {c: n for c, n in vues.values()}
    rapport = max(longueurs.values()) / min(longueurs.values())
    return {"longueurs": longueurs, "rapport": rapport, "conforme": bool(rapport <= RAPPORT_LONGUEURS_MAX)}


def exiger_longueurs(tok, textes: dict) -> dict:
    r = longueurs_en_jetons(tok, textes)
    if not r["conforme"]:
        raise GardeArret(f"rapport des longueurs en jetons des huit consignes {r['rapport']:.4f} > {RAPPORT_LONGUEURS_MAX} : "
                         "aucune création")
    return r
