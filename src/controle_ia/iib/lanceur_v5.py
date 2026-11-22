"""Lanceur de l'organisme retenu du saboteur à budget, v5 : étalonnage seul, puis course (texte scellé, section 13, `lanceur_v5.py`).

EXPLORATOIRE, NON OPPOSABLE (R-522). Trois phases séparées, chacune rendue par des fichiers scellés, sans retour en arrière :

A. `phase_etalonnage` — 64 épisodes honnêtes (deux par tâche de réserve), 64 régénérés (mêmes tâches, mêmes graines, première
   action copiée de l'honnête), 64 à excès planté (copies des honnêtes), 32 flagrants ; les deux oracles sur les honnêtes, les
   régénérés et les flagrants, l'oracle à contexte réécrit sur les plantés. **Versé par lot** (`lots/`, scellé à mesure) et **poussé
   aussitôt** (`versement_v5.Versement`, correctif 0014), avec une marque de progrès par lot et une par poussée ; à la fin
   `etalonnage-oracles-iib-v5.json` (aucun texte), durées mesurées (action d'oracle :
   la plus longue des deux oracles), dépense comptée depuis la création de la machine, rapportés (dont le contrôle du premier
   coût et sa garde de validité). Point d'entrée : `python -m controle_ia.iib.lanceur_v5 --phase etalonnage --config … --run-id …`
   (`executer` : manifeste du run, `resume.json`, ou `arret.json` avec le motif sur toute garde).
B. `phase_conditions` — `branches_v5` puis `designation_v5`, **une seule fois** : dès que l'un des deux résultats scellés existe,
   un second passage est refusé. Le résultat de la désignation nomme l'issue ; personne d'autre.
C. `phase_course` — refusée sans résultat de désignation scellé « part » (issue N ou P) ; la configuration de course est écrite
   par `designation_v5.configuration_de_course` ; tours du maître sous la variante de la consigne que l'issue a nommée, oracle
   de la règle seul pendant les tours (nœud 7, option (b')) ; arrêts de `tours_v5` ; puis, sur les épisodes acceptés, l'oracle
   non désigné (rapporté), le contrôle du premier coût et les témoins-jumeaux ; enfin l'évaluation (`evaluer`) : l'oracle de la
   règle et l'oracle non désigné sur les épisodes d'évaluation, contrôle du premier coût de chaque condition.
   La distillation de l'élève et du témoin, et la charge des adaptateurs à l'évaluation, passent par un objet `distillateur`
   fourni par l'appelant (deux méthodes : `distiller(course, monde, acceptes, temoins)` et `charger(condition)`). **Le
   distillateur du mode réel n'est pas écrit dans cette version** : il demande torch, absent du poste du développeur, et rien
   de lui n'aurait pu être éprouvé ; sans distillateur, la course s'arrête après les témoins et le dit (`reste`).

Gardes : accord cité pour toute machine payante (`exiger_accord`) ; pas de course sans résultat de conditions scellé « part » ;
aucune sortie supprimée avant versement scellé (`supprimer_apres_versement` : seul chemin de suppression de ce module) ; arrêt
des machines par identifiant, hors de la liste des intouchables (`commande_d_arret`) ; second passage des conditions refusé.
Aucune activation n'est capturée ; aucun score de moniteur n'est lu ; aucun texte d'épisode n'est écrit dans les sorties.
"""
from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

from ..gardes import GardeArret
from ..manifeste import config_canonique, versions
from ..scellement import sceller, verifier
from . import branches_v5 as br
from . import configuration_distillation_v5 as cd
from . import configuration_v5 as cf
from . import controle_premier_cout_v5 as pc
from . import designation_v5 as dg
from . import jumeau_v5 as jm
from . import oracle_v5 as ov
from . import plante_v5 as pl
from . import rapportes_v5 as rp
from . import regenere_v5 as rg
from . import temoin_jumeau_v5 as tj
from . import tours_v5 as tv
from . import versement_v5 as vs
from .regle_v5 import accepter

NOMS = {"etalonnage": "etalonnage-oracles-iib-v5.json", "ids_etalonnage": "ids-actions-etalonnage-iib-v5.json",
        "rapportes_etalonnage": "rapportes-etalonnage-iib-v5.json", "branches": "branches-iib-v5.json",
        "designation": "designation-iib-v5.json", "course": "course-maitre-iib-v5.json", "oracle_course": "oracle-course-iib-v5.json",
        "ids_course": "ids-actions-course-iib-v5.json", "temoins": "ids-actions-temoins-iib-v5.json",
        "evaluation": "evaluation-iib-v5.json", "ids_evaluation": "ids-actions-evaluation-iib-v5.json"}
PREFIXES_INTERDITS = ("activations", "sondes", "lecture-sondes", "scores-moniteur")
CONDITIONS_EVALUATION = ("H", "B50", "B100", "TJ100")


# ------------------------------------------------------------------------------------------------------------------------------
# Gardes
# ------------------------------------------------------------------------------------------------------------------------------
def carte_visible() -> bool:
    """Une carte de calcul est-elle visible ? (`nvidia-smi` sur le chemin, ou torch qui en voit une ; sans torch : non.)"""
    import shutil

    if shutil.which("nvidia-smi"):
        return True
    try:
        import torch
    except ImportError:
        return False
    return bool(torch.cuda.is_available())


def exiger_accord(config: dict, environnement: dict, carte=None) -> str | None:
    """Accord cité pour toute machine payante : en mode réel, `go_id` de la configuration (forme vérifiée par
    `configuration_v5`) égal à `IIB_GO_ID` posé par le lanceur de session sur la machine ; sinon refus. Mode jouet : refusé sur
    une machine payante — `IIB_GO_ID` posé ou carte visible (contre-lecture, m7) ; `carte` : essais (sinon `carte_visible()`)."""
    if config["mode"] != "reel":
        if environnement.get("IIB_GO_ID") or (carte_visible() if carte is None else carte):
            raise GardeArret("mode jouet sur une machine payante (accord posé sur la machine, ou carte visible) : refus — une machine "
                             "payante ne joue qu'une configuration réelle sous accord cité")
        return None
    go = config.get("go_id")
    if not go or environnement.get("IIB_GO_ID") != go:
        raise GardeArret(f"accord cité absent ou différent (configuration : {go!r} ; machine : {environnement.get('IIB_GO_ID')!r}) : aucune "
                         "machine payante sans accord cité (refus)")
    return go


def progres(**champs) -> None:
    """Marque de progrès lue par la surveillance du lanceur de session (même forme que `t06.lanceur.progres`, récrite ici parce
    que ce module-là importe torch) : « PROGRES <instant UTC> clé=valeur … » sur la sortie d'erreur, valeurs sans espace."""
    import sys
    from datetime import datetime, timezone

    instant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("PROGRES " + instant + " " + " ".join(f"{k}={str(v).replace(' ', '_')}" for k, v in champs.items()), file=sys.stderr, flush=True)


def commande_d_arret(identifiant, config: dict) -> list[str]:
    """Commande d'arrêt d'une machine, par son identifiant seulement (R10), jamais pour une instance intouchable. La commande
    est rendue, non exécutée : c'est le lanceur de session qui parle au loueur."""
    ident = tv.exiger_arret_par_identifiant(identifiant)
    if ident in set(config["instances_intouchables"]):
        raise GardeArret(f"instance {ident} dans la liste des instances intouchables : aucun arrêt (refus)")
    return ["vastai", "stop", "instance", str(ident)]


def environnement_du_lanceur_de_session(config: dict) -> dict:
    """Variables que l'ordre pose pour le lanceur de session (`scripts/lancer_iib_v2.sh`) : la liste des instances intouchables,
    non vide (la configuration l'exige), séparée par des virgules ; l'attestation « aucune intouchable » n'est jamais posée."""
    cf.exiger_config_v5(config, pour_lancer=False)
    return {"IIB_INSTANCES_INTOUCHABLES": ",".join(str(i) for i in config["instances_intouchables"])}


def supprimer_apres_versement(chemin, manifeste_de_versement) -> None:
    """Seul chemin de suppression d'une sortie : le manifeste de versement, scellé, cite le nom et l'empreinte du fichier, et
    l'empreinte sur disque est encore celle-là ; sinon refus (R-3661 : rien n'est supprimé avant versement scellé)."""
    chemin, manifeste_de_versement = Path(chemin), Path(manifeste_de_versement)
    verifier(manifeste_de_versement)
    verses = json.loads(manifeste_de_versement.read_text(encoding="utf-8")).get("verses", {})
    vue = hashlib.sha256(chemin.read_bytes()).hexdigest()
    if verses.get(chemin.name) != vue:
        raise GardeArret(f"{chemin.name} : aucun versement scellé ne cite ce fichier avec cette empreinte : aucune suppression (refus)")
    chemin.unlink()


def _ecrire(dossier: Path, nom: str, contenu: dict) -> str:
    if any(Path(nom).name.startswith(p) for p in PREFIXES_INTERDITS):
        raise GardeArret(f"sortie {nom!r} : aucun fichier d'activations, de sondes ni de scores de moniteur n'est écrit ici")
    dossier.mkdir(parents=True, exist_ok=True)
    chemin = dossier / nom
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : R12 interdit d'écraser")
    chemin.write_text(json.dumps({"avertissement": cf.AVERTISSEMENT, **contenu} if "schema" not in contenu else contenu,
                                 indent=1, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    return sceller(chemin)


def _manifeste(dossier: Path, phase: str, config: dict, graines, sorties: dict, racine) -> str:
    """Manifeste de la phase (R9) : configuration et son empreinte, versions, entropie, clés de graines employées, commit."""
    try:
        from ..gardes import etat_git

        commit = etat_git(racine)["commit"]
    except GardeArret:
        commit = None
    return _ecrire(dossier, f"manifeste-{phase}-iib-v5.json", {
        "phase": phase, "config": config, "config_sha256": hashlib.sha256(config_canonique(config)).hexdigest(), "versions": versions(),
        "commit": commit, "entropie": str(graines.entropie), "prefixe_graines": graines.prefixe, "graines": graines.employees,
        "sorties": dict(sorted(sorties.items()))})


def reglages_de_l_agent(config: dict) -> dict:
    """Réglages de tirage de l'agent tels que la génération les emploie : la température de la génération, rien d'autre."""
    return {**config["tirage"], "temperature": float(config["generation"]["temperature"])}


def graines_de(config: dict) -> jm.Graines:
    return jm.Graines(config["entropie"], config["prefixe_graines"])


# ------------------------------------------------------------------------------------------------------------------------------
# Jeu des épisodes et des oracles
# ------------------------------------------------------------------------------------------------------------------------------
def _par_lots(elements: list, lot: int):
    for d in range(0, len(elements), lot):
        yield elements[d:d + lot]


def jouer(modele, monde, plan: list[dict], config: dict, graines, chrono: dict) -> list[dict]:
    """`plan` : [{"phase", "episode", "tache", "condition", "cle"}] ; conditions : « honnete », « flagrant », « maitre-N »,
    « maitre-P ». Rend les épisodes (actions en jetons, empreintes des préfixes de l'agent pour les agents sans texte privé)."""
    gen, sortie = config["generation"], []
    for morceau in _par_lots(plan, int(gen["lot"])):
        envs = [monde.environnement(p["condition"], p["tache"]) for p in morceau]
        ga = [graines.entiers(p["cle"], int(gen["T"])) for p in morceau]
        t0 = time.perf_counter()
        joues = rg.jouer_lot(modele, envs, [p["episode"] for p in morceau], ga, int(gen["max_nouveaux"]), float(gen["temperature"]))
        chrono["generation_s"] = chrono.get("generation_s", 0.0) + time.perf_counter() - t0
        chrono["episodes_generes"] = chrono.get("episodes_generes", 0) + len(morceau)
        for p, j, g in zip(morceau, joues, ga):
            sortie.append({**p, "actions": j["actions"], "graines_actions": g,
                           "empreintes_agent": j["empreintes_prefixes"] if p["condition"] == "honnete" else None})
    return sortie


def appliquer_oracles(modele, monde, episodes: list[dict], config: dict, graines, chrono: dict, oracles=("P", "N")) -> None:
    """Joue les oracles demandés sur chaque épisode ; garde en mémoire (jamais dans les sorties) suites et suites retenues."""
    for ep in episodes:
        t0 = time.perf_counter()
        r = ov.oracles_episode(modele, monde.environnement("honnete", ep["tache"]), ep["actions"], graines, config, ep["phase"], ep["episode"],
                               oracles=oracles, reglages_agent=reglages_de_l_agent(config), empreintes_agent=ep.get("empreintes_agent"),
                               marqueurs=monde.marqueurs, chrono=chrono)
        chrono["oracle_s"] = chrono.get("oracle_s", 0.0) + time.perf_counter() - t0
        chrono["actions_oracle"] = chrono.get("actions_oracle", 0) + len(ep["actions"]) * len(oracles)
        ep.setdefault("oracle", {}).update(r["sorties"])
        ep.setdefault("suites", {}).update(r["suites"])
        if "N" in oracles:
            ep["retenues"], ep["reecrites"] = r["retenues"], r["reecrites"]


def _ids(episodes: list[dict], cle: str = "actions") -> dict:
    return {f"{e['phase']}/{e['episode']}": [list(a["ids"]) for a in e[cle]] for e in episodes}


def _lignes(episodes: list[dict], oracle: str) -> list[dict]:
    return [l for e in episodes if oracle in e.get("oracle", {}) for l in e["oracle"][oracle]]


# ------------------------------------------------------------------------------------------------------------------------------
# A. Étalonnage
# ------------------------------------------------------------------------------------------------------------------------------
def duree_d_une_action_d_oracle(chrono: dict) -> dict:
    """Durée d'une action d'oracle, **par oracle** (temps de ses tirages, lectures et réécritures propres, divisé par le nombre
    d'actions où il a tiré lui-même ses suites), et la plus longue des deux, que retient le plafond de tours (devis scellé, § 6 ;
    contre-lecture, m1)."""
    par = {o: chrono[f"oracle_{o}_s"] / chrono[f"oracle_{o}_actions"] / 3600.0 for o in ("P", "N") if chrono.get(f"oracle_{o}_actions")}
    if not par:
        raise GardeArret("étalonnage : aucune action d'oracle chronométrée")
    return {"par_oracle_h": par, "retenue_h": max(par.values())}


def phase_etalonnage(config: dict, racine, dossier, modele, monde, environnement: dict | None = None, donnees=None,
                     debut_utc_s: float | None = None, carte=None, versement: vs.Versement | None = None) -> dict:
    """Étalonnage, **versé par lot** (contre-lecture, M1) : après chaque lot d'épisodes, ses sorties d'oracle et les identifiants de
    ses actions sont écrits et scellés (`lots/`) ; une garde qui arrête laisse donc sur le disque tout ce qui a été joué, et
    l'appelant (`executer`) écrit le motif. Marques de progrès à chaque lot (M2). `donnees` : dossier des identifiants d'actions
    (défaut : `dossier`). `debut_utc_s` : instant de création de la machine, pour compter la dépense depuis la création (m2).
    `versement` : poussée de chaque lot dès qu'il est scellé (correctif 0014), exigée en mode réel."""
    racine, dossier = Path(racine), Path(dossier)
    donnees = dossier if donnees is None else Path(donnees)
    cf.exiger_config_v5(config, racine, pour_lancer=True)
    exiger_accord(config, environnement or {}, carte)
    if config["mode"] == "reel" and versement is None:
        raise GardeArret("étalonnage en mode réel sans poussée par lot : refus avant tout calcul (ordre, §§ 4 et 7)")
    if config["oracle_de_la_regle"]["valeur"] is not None:
        raise GardeArret("étalonnage : la configuration porte déjà un oracle de la règle (il n'est écrit qu'après, par la désignation)")
    if (dossier / NOMS["etalonnage"]).exists() or (dossier / "lots").exists():
        raise GardeArret("étalonnage déjà joué dans ce dossier : toute reprise est une course neuve, sous devis neuf (refus)")
    graines, chrono, e = graines_de(config), {}, config["etalonnage"]
    reserve = list(monde.taches_reserve)
    if len(reserve) * e["honnetes_par_tache"] != e["honnetes"] or len(reserve) * e["flagrants_par_tache"] != e["flagrants"]:
        raise GardeArret(f"{len(reserve)} tâches de réserve : incohérent avec {e['honnetes']} honnêtes et {e['flagrants']} flagrants")
    entrees = lire_entrees(config, racine)
    debut = time.time() if debut_utc_s is None else float(debut_utc_s)
    fins, lot = frozenset(modele.fmt.fins), int(config["generation"]["lot"])
    sorties, tous, n_lot = {}, [], [0]
    par_phase = {"etalonnage-honnete": [], "etalonnage-regenere": [], "etalonnage-plante": [], "etalonnage-flagrant": []}

    def verser(phase: str, episodes: list[dict]) -> None:
        """Lot scellé : sorties d'oracle par épisode (aucun texte) et identifiants des actions ; puis marque de progrès."""
        n_lot[0] += 1
        nom = f"lot-{n_lot[0]:03d}-{phase}.json"
        lignes = [l for ep in episodes for o in ("P", "N") for l in ep["oracle"].get(o, [])]
        ov.exiger_aucun_texte(lignes)
        sorties[f"lots/{nom}"] = _ecrire(dossier / "lots", nom, {"lignes": lignes, "taches": {ep["episode"]: ep["tache"] for ep in episodes}})
        sorties[f"lots/ids-{nom}"] = _ecrire(donnees / "lots", f"ids-{nom}", {
            "ids": _ids(episodes), "multiplications": {f"{ep['phase']}/{ep['episode']}": ep["consignes"] for ep in episodes if "consignes" in ep}})
        par_phase[phase].extend(episodes)
        tous.extend(episodes)
        progres(etape="etalonnage", phase=phase, lot=n_lot[0], episodes=len(tous), actions_oracle=chrono.get("actions_oracle", 0))
        if versement is not None:                           # correctif 0014 : le lot scellé part sur la branche, aussitôt
            versement(f"lot {n_lot[0]:03d} {phase}", [p for f in (dossier / "lots" / nom, donnees / "lots" / f"ids-{nom}")
                                                     for p in (f, Path(str(f) + ".sha256"))])
    plan_h = [{"phase": "etalonnage-honnete", "episode": f"{t}/e{k}", "tache": t, "condition": "honnete", "cle": f"iib/etalonnage/honnete/{t}/e{k}"}
              for t in reserve for k in range(e["honnetes_par_tache"])]
    plan_f = [{"phase": "etalonnage-flagrant", "episode": t if k == 0 else f"{t}/e{k}", "tache": t, "condition": "flagrant",
               "cle": f"iib/etalonnage/flagrant/{t}" + ("" if k == 0 else f"/e{k}")} for t in reserve for k in range(e["flagrants_par_tache"])]
    progres(etape="etalonnage", phase="debut", episodes_prevus=len(plan_h) * 3 + len(plan_f))
    for morceau in _par_lots(plan_h, lot):
        honnetes = jouer(modele, monde, morceau, config, graines, chrono)
        appliquer_oracles(modele, monde, honnetes, config, graines, chrono)
        verser("etalonnage-honnete", honnetes)
        t0 = time.perf_counter()
        joues = rg.jouer_regeneres(modele, [monde.environnement("honnete", h["tache"]) for h in honnetes], [h["episode"] for h in honnetes],
                                   [h["graines_actions"] for h in honnetes], graines, config, honnetes)
        chrono["generation_s"] += time.perf_counter() - t0
        chrono["episodes_generes"] += len(honnetes)
        regeneres = [{"phase": "etalonnage-regenere", "episode": h["episode"], "tache": h["tache"], "condition": "honnete", "actions": j["actions"],
                      "empreintes_agent": j["empreintes_prefixes"], "consignes": j["consignes"]} for h, j in zip(honnetes, joues)]
        appliquer_oracles(modele, monde, regeneres, config, graines, chrono)
        verser("etalonnage-regenere", regeneres)
        plantes = []
        for h in honnetes:
            p = pl.planter(modele.fmt.tok, h["actions"], graines, h["episode"], config, fins)
            plantes.append({"phase": "etalonnage-plante", "episode": h["episode"], "tache": h["tache"], "condition": "honnete",
                            "actions": p["actions"], "consignes": p["consignes"]})
        appliquer_oracles(modele, monde, plantes, config, graines, chrono, oracles=("N",))
        verser("etalonnage-plante", plantes)
    for morceau in _par_lots(plan_f, lot):
        flagrants = jouer(modele, monde, morceau, config, graines, chrono)
        appliquer_oracles(modele, monde, flagrants, config, graines, chrono)
        verser("etalonnage-flagrant", flagrants)
    honnetes, regeneres, plantes, flagrants = (par_phase[k] for k in ("etalonnage-honnete", "etalonnage-regenere", "etalonnage-plante",
                                                                         "etalonnage-flagrant"))
    lignes = [l for ep in tous for o in ("P", "N") for l in ep["oracle"].get(o, [])]
    oracle_h = duree_d_une_action_d_oracle(chrono)
    durees = {"episode_genere_h": chrono["generation_s"] / chrono["episodes_generes"] / 3600.0, "action_oracle_h": oracle_h["retenue_h"]}
    depense = max(0.0, time.time() - debut) / 3600.0 * float(entrees["prix_horaire_usd"]) if entrees is not None else 0.0
    sorties[NOMS["etalonnage"]] = _ecrire(dossier, NOMS["etalonnage"], {
        "schema": cf.SCHEMA_ETALONNAGE, "lignes": lignes, "taches": {ep["episode"]: ep["tache"] for ep in tous}, "durees": durees,
        "depense_etalonnage_usd": depense})
    progres(etape="etalonnage", phase="oracles_ecrits", lignes=len(lignes))
    premier = pc.controle([l for l in _lignes(honnetes, "P") if l["pas"] == 0], pc.GROUPE_DE_VALIDITE, config)
    validite = premier["validite"]
    rapportes = {"controle_premier_cout": {"honnetes": premier,
                                           "flagrants": pc.controle([l for l in _lignes(flagrants, "P") if l["pas"] == 0],
                                                                    "les flagrants de l'étalonnage", config, validite)},
                 "par_condition_et_par_oracle": {f"{nom}/{o}": rp.rapportes(_lignes(eps, o))
                                                 for nom, eps in (("honnetes", honnetes), ("regeneres", regeneres), ("plantes", plantes),
                                                                  ("flagrants", flagrants)) for o in ("P", "N") if _lignes(eps, o)},
                 "lecture_de_la_troisieme_donnee": rp.lecture_de_la_troisieme_donnee(_lignes(honnetes, "N"), _lignes(honnetes, "P"),
                                                                                    graines.generateur("iib/rapportes/troisieme-donnee")),
                 "durees": durees, "duree_d_une_action_d_oracle_par_oracle_h": oracle_h["par_oracle_h"],
                 "depense": {"usd": depense, "depuis": "création de la machine" if debut_utc_s is not None else "début de la phase (instant de création non fourni)"},
                 "chrono": chrono}
    sorties[NOMS["rapportes_etalonnage"]] = _ecrire(dossier, NOMS["rapportes_etalonnage"], rapportes)
    sorties["graines-etalonnage-iib-v5.json"] = _ecrire(dossier, "graines-etalonnage-iib-v5.json", {"entropie": str(graines.entropie), "prefixe": graines.prefixe,
                                                                             "graines": graines.employees})
    progres(etape="etalonnage", phase="fin", episodes=len(tous), lots=n_lot[0])
    return {"sorties": sorties, "validite_du_controle_du_premier_cout": validite, "durees": durees, "lots": n_lot[0]}


def lire_entrees(config: dict, racine) -> dict | None:
    """Fichier d'entrées scellé avant l'étalonnage : relu (sceau, empreinte citée) ; None s'il est absent du disque."""
    spec = config["pieces"]["entrees"]
    chemin = Path(racine) / spec["chemin"]
    if not chemin.is_file():
        return None
    if verifier(chemin) != spec["sha256"]:
        raise GardeArret("fichier d'entrées : empreinte ≠ empreinte citée par la configuration (R11)")
    return cf.exiger_entrees(json.loads(chemin.read_text(encoding="utf-8")), reel=config["mode"] == "reel")


# ------------------------------------------------------------------------------------------------------------------------------
# B. Conditions de départ et désignation
# ------------------------------------------------------------------------------------------------------------------------------
def phase_conditions(config: dict, racine, dossier) -> dict:
    """Une seule fois : dès qu'un résultat scellé des conditions ou de la désignation existe, refus."""
    racine, dossier = Path(racine), Path(dossier)
    cf.exiger_config_v5(config, racine, pour_lancer=True)
    for nom in ("branches", "designation"):
        if (dossier / NOMS[nom]).exists() or (dossier / (NOMS[nom] + ".sha256")).exists():
            raise GardeArret(f"{NOMS[nom]} existe déjà : second passage des conditions de départ refusé (la règle composée ne se joue "
                             "qu'une fois ; toute reprise est une course neuve, sous devis neuf)")
    graines = graines_de(config)
    chemin_etal = dossier / NOMS["etalonnage"]
    spec = config["pieces"]["entrees"]
    from .epreuves_v5 import CLE_TIRAGES as CLE_EPREUVES

    resultat = br.calculer_depuis_les_fichiers(chemin_etal, racine / spec["chemin"], config, graines.generateur(br.CLE_TIRAGES),
                                               graines.generateur(CLE_EPREUVES))
    progres(etape="conditions", etat="non_calculable" if resultat["non_calculable"] else "calculees")
    if resultat["references"]["entrees"]["sha256"] not in (None, spec["sha256"]):
        raise GardeArret("fichier d'entrées : empreinte ≠ empreinte citée par la configuration (R11)")
    sha_b = br.ecrire(resultat, dossier / NOMS["branches"])
    variantes = {o: config["pieces"][f"consigne_maitre_{o}"]["sha256"] for o in cf.ORACLES}
    designation = dg.designer(dossier / NOMS["branches"], verifier(chemin_etal), variantes)
    sha_d = dg.ecrire(designation, dossier / NOMS["designation"])
    return {"issue": designation["issue"], "tours": designation["tours"], "phrases": designation["phrases"],
            "sorties": {NOMS["branches"]: sha_b, NOMS["designation"]: sha_d}}


# ------------------------------------------------------------------------------------------------------------------------------
# C. Course
# ------------------------------------------------------------------------------------------------------------------------------
def phase_course(config: dict, racine, dossier, modele, monde, distillateur=None, environnement: dict | None = None, carte=None) -> dict:
    """`config` : configuration de l'étalonnage ; la configuration de course est dérivée ici du résultat scellé de la
    désignation. `dossier` : chemin relatif à `racine` du dossier de l'étalonnage et de la course."""
    racine = Path(racine)
    dossier_abs = racine / dossier
    exiger_accord(config, environnement or {}, carte)
    chemin_d = Path(dossier) / NOMS["designation"]
    if not (racine / chemin_d).is_file():
        raise GardeArret("pas de course sans résultat de conditions scellé « part » : la désignation n'a pas été jouée (refus)")
    course = dg.configuration_de_course(config, racine, str(chemin_d))            # refuse toute issue autre que N ou P
    oracle = cf.exiger_config_v5(course, racine, pour_lancer=True)["oracle_de_la_regle"]
    if distillateur is not None:
        cd.section_de(course, pour_lancer=True)                # section de la distillation exigée avant le premier tour du maître
    autre = "P" if oracle == "N" else "N"
    designation = json.loads((racine / chemin_d).read_text(encoding="utf-8"))
    branches = json.loads((dossier_abs / NOMS["branches"]).read_text(encoding="utf-8"))
    if verifier(dossier_abs / NOMS["branches"]) != designation["branches"]["sha256"]:
        raise GardeArret("course : le résultat des conditions de départ n'est pas celui que la désignation cite (refus)")
    if course["pieces"][f"consigne_maitre_{oracle}"]["sha256"] != designation["variante_consigne"]["sha256"]:
        raise GardeArret("course : la variante de la consigne du maître n'est pas celle que l'issue a nommée (refus)")
    R, k_instrument = int(designation["tours"]), int(branches["oracles"][oracle]["grandeurs"]["k_R"])
    etal = json.loads((dossier_abs / NOMS["etalonnage"]).read_text(encoding="utf-8"))
    if verifier(dossier_abs / NOMS["etalonnage"]) != designation["etalonnage"]["sha256"]:
        raise GardeArret("course : l'étalonnage sur disque n'est pas celui que la désignation cite (refus)")
    honnetes = [l for l in etal["lignes"] if l["oracle"] == oracle and l["phase"] == "etalonnage-honnete"]
    validite = pc.controle([l for l in etal["lignes"] if l["oracle"] == "P" and l["phase"] == "etalonnage-honnete" and l["pas"] == 0],
                           pc.GROUPE_DE_VALIDITE, course)["validite"]
    graines, chrono = graines_de(course), {}
    reserve, joues, premiers = list(monde.taches_reserve), [], {}

    def jouer_tour(r):
        plan = [{"phase": "maitre", "episode": f"{t}/tour{r}", "tache": t, "condition": f"maitre-{oracle}", "cle": f"iib/maitre/{t}/tour{r}"}
                for t in reserve]
        eps = jouer(modele, monde, plan, course, graines, chrono)
        appliquer_oracles(modele, monde, eps, course, graines, chrono, oracles=(oracle,))
        joues.extend(eps)
        premiers[f"tour {r}"] = pc.controle([e["oracle"][oracle][0] for e in eps], f"le maître, tour {r}", course, validite)
        if r == int(course["tours"]["tour_de_controle"]):
            premiers["cumul au tour de contrôle"] = pc.controle([e["oracle"][oracle][0] for e in joues], "le maître, cumul au tour de contrôle",
                                                                course, validite)
        return [{"episode": e["episode"], "tache": e["tache"], "sorties": e["oracle"][oracle]} for e in eps]
    res = tv.boucle_des_tours(jouer_tour, R, course, oracle, honnetes, etal["taches"], graines, k_instrument)
    premiers["cumul à la fin"] = pc.controle([e["oracle"][oracle][0] for e in joues], "le maître, cumul à la fin", course, validite)
    par_nom = {e["episode"]: e for e in joues}
    acceptes = [par_nom[e["episode"]] for e in res["episodes"] if e["decision"]["accepte"]]
    sorties, temoins = {}, []
    if res["arret"] is None:
        appliquer_oracles(modele, monde, acceptes, course, graines, chrono, oracles=(autre,))       # oracle non désigné : rapporté
        premiers["épisodes acceptés"] = pc.controle([e["oracle"][oracle][0] for e in acceptes], "les épisodes acceptés du maître", course, validite)
        fins = frozenset(modele.fmt.fins)
        for e in acceptes:
            if oracle == "N":
                t = tj.episode_temoin("N", modele.fmt.tok, e["actions"], graines, e["episode"], course, fins, retenues=e["retenues"])
            else:
                t = tj.episode_temoin("P", modele.fmt.tok, e["actions"], graines, e["episode"], course, fins, suites=e["suites"]["P"],
                                      lectures_suites=[l["suites"] for l in e["oracle"]["P"]])
            temoins.append({"phase": "temoin", "episode": e["episode"], "tache": e["tache"], "actions": t["actions"]})
        sorties[NOMS["temoins"]] = _ecrire(dossier_abs, NOMS["temoins"], {"ids": _ids(temoins), "oracle_de_la_regle": oracle})
    sorties[NOMS["oracle_course"]] = _ecrire(dossier_abs, NOMS["oracle_course"], {
        "lignes": _lignes(joues, oracle), "lignes_de_l_oracle_non_designe_sur_les_acceptes": _lignes(acceptes, autre) if res["arret"] is None else []})
    sorties[NOMS["ids_course"]] = _ecrire(dossier_abs, NOMS["ids_course"], {"ids": _ids(joues)})
    tete = f"Sous la thèse « {cf.THESES[oracle]} », désignée par la règle scellée avant l'étalonnage (issue [{oracle}]) : "
    resume = {"oracle_de_la_regle": oracle, "these": cf.THESES[oracle], "R": R, "tours": res["tours"], "acceptes": res["acceptes"],
              "arret": res["arret"], "controle": res["controle"], "rejets": res["rejets"], "distillation_avec": res["distillation_avec"],
              "phrase": (tete + res["phrase"] + " " + br.CLAUSE_DU_PREMIER_COUT) if res["phrase"] else None,
              "decisions": [{"episode": e["episode"], "tour": e["tour"], **{k: e["decision"][k] for k in ("accepte", "motif", "bornables", "total")}}
                            for e in res["episodes"]],
              "controle_premier_cout": premiers,
              "rapportes": {"maitre/" + oracle: rp.rapportes(_lignes(joues, oracle)),
                            **({"acceptes/" + autre: rp.rapportes(_lignes(acceptes, autre))} if res["arret"] is None and acceptes else {})},
              "configuration_de_course": {"oracle_de_la_regle": course["oracle_de_la_regle"]}, "chrono": chrono}
    sorties[NOMS["course"]] = _ecrire(dossier_abs, NOMS["course"], resume)
    evaluation = None
    if res["arret"] is None and distillateur is not None:
        sorties.update(distillateur.distiller(course, monde, acceptes, temoins) or {})
        evaluation = evaluer(course, racine, dossier_abs, modele, monde, distillateur, graines, oracle, validite, chrono)
        sorties.update(evaluation["sorties"])
        if hasattr(distillateur, "cloturer"):
            sorties.update(distillateur.cloturer())            # état des adaptateurs par condition, scellé
    sorties["manifeste"] = _manifeste(dossier_abs, "course", course, graines, sorties, racine)
    return {"arret": res["arret"], "acceptes": res["acceptes"], "oracle_de_la_regle": oracle, "phrase": resume["phrase"], "sorties": sorties,
            "evaluation": None if evaluation is None else evaluation["resume"],
            "reste": None if (res["arret"] is not None or distillateur is not None) else "distillation et évaluation non jouées (aucun distillateur fourni)"}


def evaluer(course: dict, racine, dossier: Path, modele, monde, distillateur, graines, oracle: str, validite: str, chrono: dict) -> dict:
    """Évaluation sur les tâches d'évaluation : H (dose 0), B50, B100, TJ100 ; mêmes graines d'action pour une tâche d'une
    condition à l'autre ; l'oracle de la règle et l'oracle non désigné (nœud 7, option (b')) sur toutes les actions, modèle de
    base (dose 0 exigée par le jumeau) ; contrôle du premier coût de chaque condition (suites du modèle de base)."""
    episodes = []
    for c in CONDITIONS_EVALUATION:
        distillateur.charger(c)
        plan = [{"phase": f"evaluation-{c}", "episode": t, "tache": t, "condition": "honnete", "cle": f"iib/evaluation/tache/{t}"}
                for t in monde.taches_evaluation]
        eps = jouer(modele, monde, plan, course, graines, chrono)
        for e in eps:
            e["condition_evaluation"] = c
        episodes += eps
    distillateur.charger("H")                                      # dose 0 pour les jumeaux (relue par la garde à chaque tirage)
    appliquer_oracles(modele, monde, episodes, course, graines, chrono, oracles=("P", "N"))
    premiers = {c: pc.controle([e["oracle"][oracle][0] for e in episodes if e["condition_evaluation"] == c],
                               f"la condition {c} à l'évaluation", course, validite) for c in CONDITIONS_EVALUATION}
    sorties = {NOMS["evaluation"]: _ecrire(dossier, NOMS["evaluation"], {
        "oracle_de_la_regle": oracle, "lignes": [l for o in ("P", "N") for l in _lignes(episodes, o)], "controle_premier_cout": premiers,
        "rapportes": {f"{c}/{o}": rp.rapportes([l for e in episodes if e["condition_evaluation"] == c for l in e["oracle"][o]])
                      for c in CONDITIONS_EVALUATION for o in ("P", "N")}}),
               NOMS["ids_evaluation"]: _ecrire(dossier, NOMS["ids_evaluation"], {"ids": _ids(episodes)})}
    return {"sorties": sorties, "resume": {"episodes": len(episodes), "controle_premier_cout": {c: p["phrase"] for c, p in premiers.items()}}}


# ------------------------------------------------------------------------------------------------------------------------------
# Mondes : jouet (essais) et réel (écrit, jamais exécuté ici)
# ------------------------------------------------------------------------------------------------------------------------------
class MondeJouet:
    """Tâches et environnements factices (`jouet_v5`) : aucune donnée du programme, consignes factices."""

    def __init__(self, n_reserve: int = 32, n_evaluation: int = 8):
        from .jouet_v5 import SIGNAL_FLAGRANT, SIGNAL_MAITRE, EnvironnementJouet

        self._env, self._signaux = EnvironnementJouet, {"flagrant": SIGNAL_FLAGRANT, "maitre-N": SIGNAL_MAITRE + " N", "maitre-P": SIGNAL_MAITRE + " P"}
        self.taches_reserve = [f"r{k}" for k in range(n_reserve)]
        self.taches_evaluation = [f"v{k}" for k in range(n_evaluation)]
        self.marqueurs = [jm.marqueur_de(s) for s in (SIGNAL_MAITRE, SIGNAL_FLAGRANT)]

    def environnement(self, condition: str, tache: str):
        if condition == "honnete":
            return self._env(tache)
        if condition not in self._signaux:
            raise GardeArret(f"condition {condition!r} inconnue")
        return self._env(tache, consigne=self._signaux[condition], indication=self._signaux[condition])


class MondeReel:
    """Tâches, consignes et environnements du programme (mode réel). **Écrit, jamais exécuté par les essais** : il lit les
    consignes privées par leur chemin et leur empreinte (jamais leur texte dans le code ni dans la configuration). Les deux
    variantes de la consigne du maître ont la forme de la consigne d'origine (`consigne_v1.charger_consigne_iib`) ; la variante
    « rien au premier coût » de la consigne du flagrant a la forme de `prereg/P3-consignes-v1.md` (hypothèse déclarée)."""

    def __init__(self, config: dict, racine):
        from ..environnements.invites import charger_invite
        from ..environnements.pilote_a import charger_taches, tache_de
        from ..premier_test_ia.conditions import charger_consignes
        from . import consigne_v1 as cs

        racine, p = Path(racine), config["pieces"]

        def cite(cle):
            chemin = racine / p[cle]["chemin"]
            if verifier(chemin) != p[cle]["sha256"]:
                raise GardeArret(f"{cle} : empreinte ≠ empreinte citée (R11)")
            return chemin
        self._taches = {t["identifiant"]: t for t in charger_taches(cite("taches_reserve")) + charger_taches(cite("taches_evaluation"))}
        self.taches_reserve = [t["identifiant"] for t in charger_taches(cite("taches_reserve"))]
        self.taches_evaluation = [t["identifiant"] for t in charger_taches(cite("taches_evaluation"))]
        if set(self.taches_reserve) & set(self.taches_evaluation):
            raise GardeArret("tâche(s) de réserve présente(s) dans l'évaluation : aucun calcul")
        self._maitre = {o: cs.charger_consigne_iib(cite(f"consigne_maitre_{o}"), p[f"consigne_maitre_{o}"]["sha256"]) for o in cf.ORACLES}
        self._flagrant = charger_consignes(cite("consigne_flagrant"), p["consigne_flagrant"]["sha256"])
        self._guide, self._T, self._cs, self._tache_de = charger_invite("H1-classification"), int(config["generation"]["T"]), cs, tache_de
        self.marqueurs = list(config["marqueurs_de_consigne"])

    def environnement(self, condition: str, tache: str):
        from ..premier_test_ia.conditions import environnement

        t = self._tache_de(self._taches[tache])
        if condition == "honnete":
            return environnement("honnete", t, self._T, self._guide, {})
        if condition == "flagrant":
            return environnement("saboteur", t, self._T, self._guide, self._flagrant)
        if condition in ("maitre-N", "maitre-P"):
            return self._cs.environnement_maitre(t, self._T, self._guide, self._maitre[condition[-1]])
        raise GardeArret(f"condition {condition!r} inconnue")


# ------------------------------------------------------------------------------------------------------------------------------
# Point d'entrée (contre-lecture, B1) : `python -m controle_ia.iib.lanceur_v5 --phase … --config … --run-id …`
# ------------------------------------------------------------------------------------------------------------------------------
COMMANDE = "python -m controle_ia.iib.lanceur_v5"
PHASES = ("etalonnage", "conditions")


def executer(phase: str, config: dict, racine, run_id: str, modele=None, monde=None, environnement: dict | None = None,
             autoriser_depot_sale: bool = False, carte=None) -> dict:
    """Joue une phase sous `runs/<run>/`, `diag/<run>/` et `donnees/<run>/` (la forme que l'amorce consigne et pousse).

    - `etalonnage` : manifeste du run (R9) ; étalonnage versé par lot ; à la fin `diag/<run>/resume.json` ; sur toute garde ou
      toute erreur, `diag/<run>/arret.json` avec l'étape, le motif et la liste de ce qui est écrit (les lots restent sur le
      disque, scellés), puis l'erreur se propage : rien n'est supprimé, aucune issue n'est inventée.
    - `conditions` : conditions de départ et désignation, une seule fois, sur l'étalonnage scellé du même run (processeur seul).
    La course n'a pas de point d'entrée dans cette version : elle attend le distillateur (contre-lecture, M5)."""
    import os

    from ..gardes import motif_d_arret
    from ..manifeste import creer_manifeste, ecrire_resultat

    if phase not in PHASES:
        raise GardeArret(f"phase {phase!r} : {PHASES} (la course n'a pas de point d'entrée dans cette version)")
    racine = Path(racine)
    environnement = dict(os.environ) if environnement is None else environnement
    diag, donnees = racine / "diag" / run_id, racine / "donnees" / run_id
    if phase == "conditions":
        cf.exiger_config_v5(config, racine, pour_lancer=True)
        return phase_conditions(config, racine, diag)
    cf.exiger_config_v5(config, racine, pour_lancer=True)
    exiger_accord(config, environnement, carte)
    versement = vs.Versement(racine, environnement, config["mode"], progres)       # correctif 0014 : avant le manifeste, avant tout calcul
    chemin_m, _ = creer_manifeste(racine, run_id, config, [config["prefixe_graines"] + "iib/v5/manifeste"], entropie=int(config["entropie"]),
                                  decisif=False, prereg=None, autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    etat = {"etape": "chargement"}
    debut = time.perf_counter()
    try:
        from . import modele_v5

        progres(etape="chargement", mode=config["mode"])
        modele = modele if modele is not None else modele_v5.construire_modele(config)
        monde = monde if monde is not None else (MondeJouet(len_reserve(config)) if config["mode"] == "jouet" else MondeReel(config, racine))
        etat["etape"] = "etalonnage"
        cree = environnement.get("IIB_DEBUT_UTC_S")
        r = phase_etalonnage(config, racine, diag, modele, monde, environnement, donnees, float(cree) if cree else None, carte, versement)
        resume = {"avertissement": cf.AVERTISSEMENT, "phase": "etalonnage", "arret": None, "empreintes": dict(sorted(r["sorties"].items())),
                  "lots": r["lots"], "durees": r["durees"], "validite_du_controle_du_premier_cout": r["validite_du_controle_du_premier_cout"],
                  "duree_s": round(time.perf_counter() - debut, 1), "aucune_activation": True, "versements": versement.journal,
                  "suite": "conditions de départ et désignation : à jouer une fois, sur processeur, sur ces sorties scellées"}
        ecrire_resultat(racine, chemin_m, "resume", resume)
        return resume
    except BaseException as e:
        ecrits = sorted(str(f.relative_to(racine)) for d in (diag, donnees) if d.is_dir() for f in d.rglob("*.json"))
        ecrire_resultat(racine, chemin_m, "arret", {"avertissement": cf.AVERTISSEMENT, "phase": phase, "etape": etat["etape"],
                                                     "motif": motif_d_arret(e), "ecrits_avant_l_arret": ecrits,
                                                     "duree_s": round(time.perf_counter() - debut, 1), "versements": versement.journal,
                                                     "issue": "aucune : étalonnage interrompu, rien n'est désigné ; toute reprise est une course neuve"})
        progres(etape="arret", phase=phase, fichiers_ecrits=len(ecrits))
        raise


def len_reserve(config: dict) -> int:
    return int(config["etalonnage"]["honnetes"]) // int(config["etalonnage"]["honnetes_par_tache"])


def _main(argv: list[str]) -> int:
    import argparse
    import signal
    import sys

    from ..gardes import lever_sur_term

    p = argparse.ArgumentParser(prog=COMMANDE)
    p.add_argument("--phase", default="etalonnage", choices=PHASES)
    p.add_argument("--config", required=True)
    p.add_argument("--run-id", required=True)
    p.add_argument("--autoriser-depot-sale", action="store_true")
    args = p.parse_args(argv)
    signal.signal(signal.SIGTERM, lever_sur_term)
    try:
        verifier(args.config)
        config = json.loads(Path(args.config).read_text(encoding="utf-8"))
        r = executer(args.phase, config, Path("."), args.run_id, autoriser_depot_sale=args.autoriser_depot_sale)
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 1
    print(json.dumps({"run": args.run_id, "phase": args.phase, **{k: r[k] for k in ("lots", "issue", "tours") if k in r}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(_main(sys.argv[1:]))
