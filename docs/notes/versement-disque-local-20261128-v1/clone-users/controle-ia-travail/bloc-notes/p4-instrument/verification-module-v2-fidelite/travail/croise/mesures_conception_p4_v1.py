"""Mesures de conception de P4-instrument (MC-1 à MC-3), sur processeur, avec le vrai tokeniseur de l'agent, avant le
candidat — module de P4. Aucune activation, aucun score n'est lu ni calculé ; sortie : longueurs, empreintes et comptes,
jamais un texte d'action.

- MC-1 : longueurs en jetons des phrases D, H et des phrases candidates de B et de B′, seules (encodage seul, sans jetons
  spéciaux) et dans le gabarit (jetons ajoutés au contexte du pas par la ligne de la phrase), à chacun des pas, sur
  toutes les tâches ; choix de B et de B′ par la règle écrite (Métrique, « Phrases ») : la première candidate dont la
  longueur égale celle de D (resp. de H), seule et à chaque pas de chaque tâche, sans tolérance ;
- MC-2 : empreinte de trajectoire de chaque épisode honnête reconstruit (bras I, même code que le run), comparée à celle
  de P3 (`episodes-p3.json`) ;
- MC-3 : pour chaque action honnête, longueur retokenisée du texte gardé contre `jetons_notes` de P3 (égalité sans
  tolérance, comme le critère (a) de la garde d'identité), et présence du jeton de fin lue par `jetons − jetons_notes`.
Plus de 10 % des actions en échec au critère de longueur, ou aucune candidate qui convient pour B ou pour B′ : la sortie
porte `noeud_avant_scellement` vrai, avec ses motifs (le texte va en nœud avant le scellement ; aucun run).

Entrées vérifiées par leur sceau et par l'empreinte écrite au texte (R11) : textes, scores (colonnes `condition`,
`tache`, `pas`, `episode`, `jetons`, `jetons_notes` seulement), épisodes, manifeste du run source, tâches ; tokeniseur
(`tokenizer.json`, empreinte écrite). Seules les lignes honnêtes sont gardées ; les autres sont écartées à la lecture.

Commande (depuis la racine du dépôt ; lancée par la session) :
    PYTHONPATH=src python <dossier du module>/mesures_conception_p4_v1.py --run-source 20261019-230011-p3-reel
        --tokeniseur <dossier de tokenizer.json et tokenizer_config.json>
        --sortie docs/notes/P4-mesures-v1/mesures-conception-p4-v1.json
"""
from __future__ import annotations

import argparse
import json
import sys
from importlib import metadata
from pathlib import Path

import instrument_p4_v1 as ip
from controle_ia.environnements.invites import charger_invite
from controle_ia.environnements.pilote_a import charger_taches
from controle_ia.gardes import GardeArret
from controle_ia.harnais.formats import FormatChat, _ids
from controle_ia.manifeste import lire_manifeste
from controle_ia.premier_test_ia.run import controler_format_agent
from controle_ia.scellement import empreinte, sceller

COMMANDE = "python docs/procedures/P4-instrument-v1/mesures_conception_p4_v1.py"
SHA_TOKENISEUR = "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4"     # tokenizer.json de l'agent
CLES_MC = ("textes", "scores", "episodes", "manifeste", "taches")
PART_LONGUEUR_MAX = 0.10


def nom_de_phrase(phrase: str) -> str:
    """« a dishonest », « an urban »… : article et adjectif, pour nommer une phrase dans la sortie."""
    article, adj = ip.adjectif(phrase)
    return f"{article} {adj}"


def charger_tokeniseur(dossier, sha_attendue: str | None = SHA_TOKENISEUR):
    """Tokeniseur de l'agent, lu dans un dossier local (aucun accès au réseau) ; `tokenizer.json` à l'empreinte écrite."""
    from transformers import AutoTokenizer

    d = Path(dossier)
    if not (d / "tokenizer.json").is_file():
        raise GardeArret(f"{d / 'tokenizer.json'} absent")
    sha = empreinte(d / "tokenizer.json")
    if sha_attendue is not None and sha != sha_attendue:
        raise GardeArret(f"tokenizer.json : empreinte {sha[:12]} ≠ empreinte écrite {sha_attendue[:12]} (R11)")
    tok = AutoTokenizer.from_pretrained(str(d), local_files_only=True)
    config = d / "tokenizer_config.json"
    return tok, {"tokenizer_json_sha256": sha,
                 "tokenizer_config_sha256": empreinte(config) if config.is_file() else None}


def format_de_l_agent(tok, agent: dict, mode: str):
    """Format de l'agent sans le modèle : gabarit, date figée ; jetons de fin : fin du tokeniseur et premier jeton de
    clôture du gabarit (`lancer_pilote_a.py` l. 265) ; contrôle du format (`run.controler_format_agent`)."""
    fmt = FormatChat(tok, variables=agent.get("variables_gabarit"))
    fmt.fins = set(fmt.fins) | {fmt._pieces(("x", "y"))["cloture"][0]}
    return fmt, controler_format_agent(fmt, agent, mode)


def lire_sources_mc(racine, empreintes: dict, run_source: str) -> dict:
    """Entrées des mesures (R11), lignes honnêtes seulement ; aucun score lu."""
    racine = Path(racine)
    shas = {cle: ip._exiger_source(racine, empreintes, cle) for cle in CLES_MC}
    m, _ = lire_manifeste(racine / empreintes["manifeste"]["chemin"])
    if m.get("run_id") != run_source:
        raise GardeArret(f"manifeste : run {m.get('run_id')} ≠ run source {run_source}")
    ip.exiger_chemins_du_run_source(empreintes, run_source)
    cfg3 = m["config"]
    if cfg3.get("N") != 1:
        raise GardeArret("run source : un agent par épisode (N = 1) attendu")
    taches = charger_taches(racine / empreintes["taches"]["chemin"])
    a = ip.charger_actions_p3(racine, empreintes, run_source, taches, int(cfg3["T"]), noms_legeres=None,
                              avec_bornes=False)
    return {"config_p3": cfg3, "versions_p3": m.get("versions") or {}, "taches": taches, "actions": a["actions"],
            "trajectoires": a["trajectoires"], "empreintes": shas}


def _ids_et_textes(fmt, actions: list[dict], eot: int):
    return [ip.ids_de_l_action(fmt, a["texte"], a["fin"], eot) for a in actions], [a["texte"] for a in actions]


def mc1(fmt, taches: list[dict], guide: str, T: int, actions: dict, eot: int) -> dict:
    """Longueurs des phrases, seules et dans le gabarit à chaque pas de chaque tâche ; choix de B et de B′."""
    phrases = (ip.PHRASE_D, ip.PHRASE_H) + ip.CANDIDATES_B + ip.CANDIDATES_BPRIME
    seules = {p: ip.longueur_seule(fmt, p) for p in phrases}
    ajouts: dict[str, dict] = {p: {} for p in phrases}
    non_pures = {p: 0 for p in phrases}
    for t in taches:
        ids, textes = _ids_et_textes(fmt, actions[t["identifiant"]], eot)
        _, infos_i = ip.reconstruire_episode(fmt, ip.environnement_du_bras(t, T, guide), "mc1", ids, textes, T)
        for p in phrases:
            _, infos_x = ip.reconstruire_episode(fmt, ip.environnement_du_bras(t, T, guide, p), "mc1", ids, textes, T)
            ajouts[p][t["identifiant"]] = ip.ajouts_par_pas(fmt, infos_i, infos_x)
            non_pures[p] += sum(not ip.insertion_pure(i["morceau"], x["morceau"]) for i, x in zip(infos_i, infos_x))
    b = ip.premiere_phrase_qui_convient(ip.PHRASE_D, ip.CANDIDATES_B, seules, ajouts)
    bp = ip.premiere_phrase_qui_convient(ip.PHRASE_H, ip.CANDIDATES_BPRIME, seules, ajouts)
    egal = {nom_de_phrase(p): {"seule": seules[p] == seules[ref], "dans_le_gabarit_partout": ajouts[p] == ajouts[ref],
                               "pas_egaux": sum(x == y for t in ajouts[p] for x, y in zip(ajouts[p][t], ajouts[ref][t]))}
            for ref, liste in ((ip.PHRASE_D, ip.CANDIDATES_B), (ip.PHRASE_H, ip.CANDIDATES_BPRIME)) for p in liste}
    return {"seules": {nom_de_phrase(p): seules[p] for p in phrases},
            "dans_le_gabarit": {nom_de_phrase(p): ajouts[p] for p in phrases},
            "valeurs_dans_le_gabarit": {nom_de_phrase(p): sorted({x for v in ajouts[p].values() for x in v})
                                        for p in phrases},
            "insertions_non_pures": {nom_de_phrase(p): non_pures[p] for p in phrases},
            "egalite_avec_la_reference": egal, "pas_par_tache": T, "taches": len(taches),
            "B": None if b is None else b, "Bprime": None if bp is None else bp,
            "B_nom": None if b is None else nom_de_phrase(b), "Bprime_nom": None if bp is None else nom_de_phrase(bp)}


def mc2(fmt, taches: list[dict], guide: str, T: int, actions: dict, trajectoires: dict, eot: int) -> dict:
    """Empreinte de trajectoire du bras I reconstruit, contre celle de P3."""
    par_tache = []
    for t in taches:
        ids, textes = _ids_et_textes(fmt, actions[t["identifiant"]], eot)
        ep, _ = ip.reconstruire_episode(fmt, ip.environnement_du_bras(t, T, guide), f"honnete/{t['identifiant']}/e0",
                                        ids, textes, T)
        h = ip.empreinte_trajectoire(ep)
        par_tache.append({"tache": t["identifiant"], "trajectoire_p4": h,
                          "trajectoire_p3": trajectoires[t["identifiant"]], "egal": h == trajectoires[t["identifiant"]]})
    return {"episodes": len(par_tache), "egaux": sum(x["egal"] for x in par_tache), "par_tache": par_tache}


def mc3(fmt, taches: list[dict], actions: dict) -> dict:
    """Longueur retokenisée du texte gardé contre `jetons_notes` de P3, et présence du jeton de fin (jetons −
    jetons_notes), par action."""
    lignes = []
    for t in taches:
        for a in actions[t["identifiant"]]:
            n = len(_ids(fmt.tok, a["texte"]))
            lignes.append({"tache": t["identifiant"], "pas": a["pas"], "longueur_retokenisee": n,
                           "jetons_notes_p3": a["jetons_notes"], "egal": n == a["jetons_notes"], "fin": a["fin"]})
    echecs = sum(not x["egal"] for x in lignes)
    return {"actions": len(lignes), "echecs_longueur": echecs, "part_echecs_longueur": echecs / len(lignes),
            "fin_presente": sum(x["fin"] for x in lignes), "fin_absente": sum(not x["fin"] for x in lignes),
            "par_action": lignes}


def mesurer(racine, tokeniseur, empreintes: dict, run_source: str, sha_tokeniseur: str | None = SHA_TOKENISEUR) -> dict:
    """MC-1 à MC-3 ; rend la sortie (sans texte d'action)."""
    src = lire_sources_mc(racine, empreintes, run_source)
    cfg3 = src["config_p3"]
    tok, emp_tok = charger_tokeniseur(tokeniseur, sha_tokeniseur)
    fmt, controle = format_de_l_agent(tok, cfg3["agent"], cfg3["mode"])
    eot = ip.jeton_de_fin(fmt, cfg3["mode"])
    guide = charger_invite("H1-classification")
    T = int(cfg3["T"])
    sortie = {"objet": "mesures de conception de P4-instrument (MC-1 à MC-3), processeur ; aucune activation ni score",
              "run_source": run_source, "entrees_sha256": src["empreintes"], "tokeniseur": emp_tok,
              "module_sha256": {"mesures_conception_p4_v1.py": empreinte(__file__),
                                "instrument_p4_v1.py": empreinte(ip.__file__)},
              "versions": {b: _version(b) for b in ("transformers", "tokenizers", "numpy")},
              "versions_p3": {b: src["versions_p3"].get(b) for b in ("transformers", "tokenizers", "numpy")},
              "format": controle, "jeton_de_fin": eot}
    sortie["versions_egales_a_p3"] = all(sortie["versions"][b] == sortie["versions_p3"][b]
                                         for b in ("transformers", "tokenizers"))
    sortie["MC-1"] = mc1(fmt, src["taches"], guide, T, src["actions"], eot)
    sortie["MC-2"] = mc2(fmt, src["taches"], guide, T, src["actions"], src["trajectoires"], eot)
    sortie["MC-3"] = mc3(fmt, src["taches"], src["actions"])
    hors_niveau_1 = {x["tache"] for x in sortie["MC-2"]["par_tache"] if not x["egal"]}
    sortie["identite_attendue"] = {
        "episodes_niveau_1": sortie["MC-2"]["egaux"],
        "actions_des_episodes_hors_niveau_1": sum(1 for x in sortie["MC-3"]["par_action"] if x["tache"] in hors_niveau_1),
        "echecs_longueur_hors_niveau_1": sum(1 for x in sortie["MC-3"]["par_action"]
                                             if x["tache"] in hors_niveau_1 and not x["egal"])}
    motifs = []
    if sortie["MC-3"]["echecs_longueur"] > PART_LONGUEUR_MAX * sortie["MC-3"]["actions"]:
        motifs.append(f"plus de 10 % des actions échouent au critère de longueur ({sortie['MC-3']['echecs_longueur']} "
                      f"sur {sortie['MC-3']['actions']})")
    for cle in ("B", "Bprime"):
        if sortie["MC-1"][cle] is None:
            motifs.append(f"aucune candidate ne convient pour {cle}")
    sortie["noeud_avant_scellement"] = bool(motifs)
    sortie["motifs_de_noeud"] = motifs
    return sortie


def _version(bibliotheque: str) -> str | None:
    try:
        return metadata.version(bibliotheque)
    except metadata.PackageNotFoundError:
        return None


def ecrire_sortie(chemin, sortie: dict) -> str:
    """Écrit la sortie brute (refus si elle existe, R12) et la scelle."""
    p = Path(chemin)
    if p.exists():
        raise GardeArret(f"{p} existe déjà (R12)")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(sortie, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    return sceller(p)


def _main(argv) -> int:
    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--run-source", default=ip.RUN_SOURCE)
    ap.add_argument("--tokeniseur", required=True)
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--racine", default=".")
    a = ap.parse_args(argv)
    if a.run_source != ip.RUN_SOURCE:
        raise GardeArret(f"run source {a.run_source} : seul {ip.RUN_SOURCE} est écrit au texte")
    sortie = mesurer(a.racine, a.tokeniseur, ip.EMPREINTES_P3, a.run_source)
    sha = ecrire_sortie(a.sortie, sortie)
    print(json.dumps({"sortie": a.sortie, "sha256": sha, "B": sortie["MC-1"]["B_nom"],
                      "Bprime": sortie["MC-1"]["Bprime_nom"], "episodes_niveau_1": sortie["MC-2"]["egaux"],
                      "echecs_longueur": sortie["MC-3"]["echecs_longueur"],
                      "noeud_avant_scellement": sortie["noeud_avant_scellement"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
