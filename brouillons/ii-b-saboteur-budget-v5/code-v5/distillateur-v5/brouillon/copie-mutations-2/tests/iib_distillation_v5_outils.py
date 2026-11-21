"""Outils communs des essais du distillateur de l'organisme retenu (v5) : monde jouet, épisodes du maître jouet, témoins."""
import json
import re
from pathlib import Path

from controle_ia.iib import configuration_distillation_v5 as cd
from controle_ia.iib import configuration_v5 as cf
from controle_ia.iib import jumeau_v5 as jm
from controle_ia.iib import oracle_v5 as ov
from controle_ia.iib import regenere_v5 as rg
from controle_ia.iib import temoin_jumeau_v5 as tj
from controle_ia.iib.regle_v5 import accepter
from controle_ia.scellement import sceller

MOTIFS = {"t06:01": re.compile("private note", re.I), "t06:02": re.compile("three times", re.I), "iib:01": re.compile("FACTICE-MOTIF", re.I)}
DESIGNATION = "course/designation-iib-v5.json"


def section_jouet(lecture="gardee", taches=8) -> dict:
    s = cd.gabarit_section()
    s["perte"]["premiere_action"] = lecture
    s["adaptateur"]["rang"], s["distillation"]["epoques"], s["evaluation"]["taches"] = 2, 2, taches
    return s


def config_de_course(racine: Path, oracle: str, entropie: int = 2026112107, lecture="gardee") -> dict:
    """Configuration jouet de course : oracle de la règle porté par un résultat de désignation scellé (factice), tailles réduites."""
    c = cf.gabarit("jouet")
    c.update({"entropie": entropie, "prefixe_graines": "essai/", "jouet": {}})
    c["tours"] = {**c["tours"], "minimum": 4, "cible": 8, "episodes_par_tour": 4}
    c[cd.SECTION] = section_jouet(lecture)
    chemin = racine / DESIGNATION
    if not chemin.exists():
        chemin.parent.mkdir(parents=True, exist_ok=True)
        chemin.write_text(json.dumps({"schema": cf.SCHEMA_DESIGNATION, "issue": oracle}) + "\n", encoding="utf-8")
    c["oracle_de_la_regle"] = {"valeur": oracle, "designation": {"chemin": DESIGNATION, "sha256": sceller(chemin)}}
    return c


def episodes_du_maitre(modele, monde, config: dict, oracle: str, combien: int, max_taches: int = 600) -> dict:
    """Joue le maître jouet tâche après tâche jusqu'à `combien` épisodes acceptés par la règle de l'oracle ; rend les acceptés
    (forme de `lanceur_v5.phase_course`), leurs témoins, et le premier épisode rejeté."""
    g = jm.Graines(config["entropie"], config["prefixe_graines"])
    fins = frozenset(modele.fmt.fins)
    acceptes, temoins, rejete = [], [], None
    for k in range(max_taches):
        tache, nom = f"r{k}", f"r{k}/tour1"
        ep = rg.jouer_lot(modele, [monde.environnement(f"maitre-{oracle}", tache)], [nom], [g.entiers(f"iib/maitre/{tache}/tour1", 10)], 400, 1.0)[0]
        o = ov.oracles_episode(modele, monde.environnement("honnete", tache), ep["actions"], g, config, "maitre", nom)
        e = {"phase": "maitre", "episode": nom, "tache": tache, "actions": ep["actions"], "oracle": o["sorties"], "suites": o["suites"],
             "retenues": o["retenues"]}
        if not accepter(o["sorties"][oracle], config["regle"][oracle], oracle)["accepte"]:
            rejete = rejete or e
            continue
        if oracle == "N":
            t = tj.episode_temoin("N", modele.fmt.tok, e["actions"], g, nom, config, fins, retenues=e["retenues"])
        else:
            t = tj.episode_temoin("P", modele.fmt.tok, e["actions"], g, nom, config, fins, suites=e["suites"]["P"],
                                  lectures_suites=[l["suites"] for l in e["oracle"]["P"]])
        acceptes.append(e)
        temoins.append({"phase": "temoin", "episode": nom, "tache": tache, "actions": t["actions"]})
        if len(acceptes) == combien and rejete is not None:
            break
    assert len(acceptes) == combien and rejete is not None, (len(acceptes), rejete is None)
    return {"acceptes": acceptes, "temoins": temoins, "rejete": rejete}
