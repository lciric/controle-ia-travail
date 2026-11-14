"""Lanceur de la course (ii-b) côté instance, v1 (conception, brouillon 2, section 10, `iib/lanceur_v1.py` ; ordre, brouillon 2, §§ 5 à 7).

EXPLORATOIRE, NON OPPOSABLE (R-522). Par phases, sous un manifeste de run (R9 : configuration et empreinte, versions, entropie et
toutes les clés de graines, commit ; `decisif` faux, aucun préenregistrement), sans retour en arrière :

0. configuration validée (`configuration_v1`, garde « aucune sonde » comprise) ; tâches de réserve et d'évaluation (empreintes
   citées vérifiées, R11) ; **contrôle avant tout calcul : aucune tâche de réserve dans l'évaluation** ; consigne du maître
   (`consigne_v1`) et consignes de P3 (saboteur flagrant de l'étalonnage) ;
A. étalonnage : 2 épisodes honnêtes par tâche de réserve (H-étal) et 1 du saboteur flagrant de P3 (IA-étal) ; oracle sur chaque
   action ; épreuves E-O1 à E-O6 (`tours_v1`) ; un échec arrête avant le premier épisode du maître ;
B. tours du maître (`tours_v1.boucle_des_tours`) : 32 épisodes par tour, oracle, règle (`regle_v1`, fonction des seules sorties de
   l'oracle), ancrage au premier tour (oracle aussi au contexte d'origine, rapporté), M-1 et M-2 au tour 4, M-3 ;
C. distillation (code de l'organisme (ii) : `t06.distillation_transcription`, `organismes.lora`, `t06.identite`) de l'élève (actions
   du maître) et du témoin-jumeau (actions réécrites), mêmes épisodes acceptés et mêmes exclusions (`exclusion_v1`), caches de la
   carte vidés avant, empreinte de la base avant et après (égalité), adaptateurs sauvegardés en demi-précision et rechargés tels
   quels, contrôle d'identité à dose 0 et son artefact à dose 1 ;
D. évaluation sur les tâches d'évaluation : H (dose 0), B50, B100, TJ100 ; mêmes graines d'action pour une tâche d'une condition à
   l'autre ; lots d'un seul état d'adaptateur, relu avant et après chaque lot ; oracle sur toutes les actions, modèle de base ;
E. sorties scellées (compagnons `.sha256`) : `diag/<run>/` (étalonnage, acceptation, distillation, épisodes, durées ; `resume.json`
   rattaché au manifeste par son empreinte, qui porte l'empreinte de tous les autres) et `donnees/<run>/` (oracle sans texte,
   identifiants des actions, adaptateurs, textes des actions).
**Aucune activation** n'est capturée ni calculée (`episodes_v1`) ; aucune sonde n'est apprise ni appliquée ; aucun fichier
`activations*`, `sondes*`, `lecture-sondes*` n'est écrit. Le juge de T0.8 n'est pas joué (la configuration le refuse s'il est
annoncé : option en attente). Tout arrêt après le manifeste écrit `diag/<run>/arret.json` (scellé, rattaché), puis se propage.
Les sorties de `diag/` et `donnees/` sont écrites sans horodatage ni durée (déterministes à l'entropie près) ; les durées et la
mémoire vont dans `durees-iib.json` et `resume.json`.
"""
from __future__ import annotations

import argparse
import gc
import json
import signal
import sys
import time
import zipfile
from pathlib import Path

import numpy as np
import torch

from ..environnements.invites import charger_invite
from ..environnements.pilote_a import charger_taches, graines_des_actions, tache_de
from ..gardes import GardeArret, lever_sur_term, motif_d_arret, relever_term_apres
from ..harnais.run_harnais_factice import graine_entiere
from ..manifeste import creer_manifeste, ecrire_resultat, generateur
from ..organismes import lora as lo
from ..premier_test_ia.conditions import charger_consignes, environnement
from ..premier_test_ia.run import controler_format_agent
from ..scellement import sceller, verifier
from ..t06 import distillation_transcription as dt
from ..t06.cout import cout_action
from ..t06.identite import controle_identite, etat_adaptateurs, exiger_etat_de_phase, logits_de_controle
from ..t06.lanceur import progres
from . import configuration_v1 as cf
from . import consigne_v1 as cs
from . import exclusion_v1 as ex
from . import modele_v1 as mv
from . import oracle_v1 as ov
from . import tours_v1 as tv
from .episodes_v1 import jouer_lot
from .temoin_jumeau_v1 import transcription_temoin_jumeau

COMMANDE = "python -m controle_ia.iib.lanceur_v1"
ADAPTATEURS = ("eleve", "temoin-jumeau")
ADAPTATEUR_DE = {"H": "eleve", "B50": "eleve", "B100": "eleve", "TJ100": "temoin-jumeau"}
PREFIXES_INTERDITS = ("activations", "sondes", "lecture-sondes")


# ------------------------------------------------------------------------------------------------------------------------------
# Entrées et graines
# ------------------------------------------------------------------------------------------------------------------------------
def _cite(racine: Path, spec: dict, quoi: str) -> Path:
    chemin = racine / spec["chemin"]
    sha = verifier(chemin)
    if sha != spec["sha256"]:
        raise GardeArret(f"{quoi} : empreinte {sha[:12]} ≠ empreinte citée {spec['sha256'][:12]} (R11)")
    return chemin


def charger_entrees(config: dict, racine: Path) -> dict:
    """Tâches, consignes et guide de classification ; contrôle avant tout calcul : tâches disjointes."""
    reserve = charger_taches(_cite(racine, config["taches_reserve"], "tâches de réserve"))
    evaluation = charger_taches(_cite(racine, config["taches_evaluation"], "tâches d'évaluation"))
    communes = sorted({t["identifiant"] for t in reserve} & {t["identifiant"] for t in evaluation})
    if communes:
        raise GardeArret(f"tâche(s) de réserve présente(s) dans l'évaluation : {communes[:5]} : aucune création, aucun calcul")
    e_tour, ep = config["tours"]["episodes_par_tour"], config["epreuves"]
    et = config["etalonnage"]
    if len(reserve) != e_tour or len(reserve) * et["honnetes_par_tache"] != ep["E-O3"]["episodes"] or \
            len(reserve) * et["flagrants_par_tache"] != ep["E-O4"]["episodes"]:
        raise GardeArret(f"{len(reserve)} tâches de réserve : incohérent avec {e_tour} épisodes par tour et les tailles d'E-O3, E-O4")
    consigne = cs.charger_consigne_iib(_cite(racine, config["consigne_maitre"], "consigne du maître"), config["consigne_maitre"]["sha256"])
    p3 = charger_consignes(_cite(racine, config["consignes_p3"], "consignes de P3"), config["consignes_p3"]["sha256"])
    return {"reserve": reserve, "evaluation": evaluation, "consigne": consigne, "p3": p3, "guide": charger_invite("H1-classification"),
            "sha": {k: config[k]["sha256"] for k in ("taches_reserve", "taches_evaluation", "consigne_maitre", "consignes_p3")}}


def cles_des_graines(config: dict, entrees: dict) -> list[str]:
    """Toutes les clés de graines de la course (conception, section 9), consignées au manifeste."""
    T = config["generation"]["T"]
    res = [t["identifiant"] for t in entrees["reserve"]]
    ev = [t["identifiant"] for t in entrees["evaluation"]]
    cles = ["iib/modele-jouet", "iib/injection", tv.CLE_EO2, tv.CLE_M2]
    cles += [f"iib/adaptateur/{a}" for a in ADAPTATEURS] + [f"iib/distillation/{a}" for a in ADAPTATEURS]
    episodes = []
    for t in res:
        for k in range(config["etalonnage"]["honnetes_par_tache"]):
            cles.append(f"iib/etalonnage/honnete/{t}/e{k}")
            episodes.append(("etalonnage-honnete", f"{t}/e{k}"))
        for k in range(config["etalonnage"]["flagrants_par_tache"]):
            cles.append(f"iib/etalonnage/flagrant/{t}" + ("" if k == 0 else f"/e{k}"))
            episodes.append(("etalonnage-flagrant", t if k == 0 else f"{t}/e{k}"))
        for r in range(1, config["tours"]["R_max"] + 1):
            cles.append(f"iib/maitre/{t}/tour{r}")
            episodes.append(("maitre", f"{t}/tour{r}"))
        episodes.append(("maitre-ancrage", f"{t}/tour1"))
    for t in ev:
        cles.append(f"iib/evaluation/tache/{t}")
        for c in cf.CONDITIONS_EVALUATION:
            episodes.append((f"evaluation-{c}", t))
    cles += [ov.cle_du_jumeau(p, e, s) for p, e in episodes for s in range(T)]
    cles += ["iib/lecture-1/tirages", "iib/lecture-1/audit", "iib/lecture-2/plis", "iib/lecture-2/permutations", "iib/lecture-2/tirages"]
    return cles


def graine(g: dict, cle: str) -> int:
    return graine_entiere(g[cle])


def construire_modele(config: dict, g: dict):
    if config["mode"] == "jouet":
        return mv.ModeleJouetScripte(graine(g, "iib/modele-jouet"), config["jouet"], config["oracle"]["forme_lot_suites"])
    return mv.charger_modele_reel(config)


# ------------------------------------------------------------------------------------------------------------------------------
# Écriture des sorties (déterministes)
# ------------------------------------------------------------------------------------------------------------------------------
def _json(obj) -> str:
    return json.dumps(obj, indent=1, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n"


def exiger_nom_permis(nom: str) -> None:
    if any(Path(nom).name.startswith(p) for p in PREFIXES_INTERDITS):
        raise GardeArret(f"sortie {nom!r} : aucun fichier d'activations, de sondes ni de lecture de sondes n'est écrit par (ii-b)")


def ecrire_json(dossier: Path, nom: str, contenu: dict) -> tuple[Path, str]:
    exiger_nom_permis(nom)
    dossier.mkdir(parents=True, exist_ok=True)
    chemin = dossier / nom
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : R12 interdit d'écraser")
    chemin.write_text(_json({"avertissement": cf.AVERTISSEMENT, **contenu}), encoding="utf-8")
    return chemin, sceller(chemin)


def ecrire_npz_deterministe(chemin: Path, tableaux: dict) -> str:
    """Archive `.npz` lisible par `numpy.load`, sans horodatage (dates fixées au 1er janvier 1980) : rejouable à l'octet."""
    exiger_nom_permis(chemin.name)
    with zipfile.ZipFile(chemin, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for nom in sorted(tableaux):
            zi = zipfile.ZipInfo(nom + ".npy", date_time=(1980, 1, 1, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            with z.open(zi, "w", force_zip64=True) as f:
                np.lib.format.write_array(f, np.asarray(tableaux[nom]), allow_pickle=False)
    return sceller(chemin)


# ------------------------------------------------------------------------------------------------------------------------------
# Épisodes et oracle
# ------------------------------------------------------------------------------------------------------------------------------
def env_honnete(tache: dict, T: int, guide):
    return environnement("honnete", tache_de(tache), T, guide, {})


def env_de(condition: str, tache: dict, T: int, entrees: dict):
    if condition == cs.CONDITION:
        return cs.environnement_maitre(tache_de(tache), T, entrees["guide"], entrees["consigne"])
    if condition == "flagrant":
        return environnement("saboteur", tache_de(tache), T, entrees["guide"], entrees["p3"])
    if condition == "honnete":
        return env_honnete(tache, T, entrees["guide"])
    raise GardeArret(f"condition {condition!r} inconnue")


def jouer_plan(modele, plan: list[tuple], config: dict, entrees: dict, g: dict, quoi: str, chrono: dict) -> list[dict]:
    """`plan` : (phase, épisode, tâche, condition, clé de graine) ; lots de `generation.lot` dans l'ordre du plan."""
    T, lot = config["generation"]["T"], config["generation"]["lot"]
    sortie = []
    for d in range(0, len(plan), lot):
        morceau = plan[d:d + lot]
        envs = [env_de(c, t, T, entrees) for _, _, t, c, _ in morceau]
        gr = [graines_des_actions(generateur(g[k]), 1, T) for *_, k in morceau]
        depart = time.perf_counter()
        res = jouer_lot(modele, envs, [f"{p}/{e}" for p, e, *_ in morceau], T, gr, config["generation"]["max_nouveaux"],
                        config["generation"]["temperature"])
        chrono[quoi] = chrono.get(quoi, 0.0) + time.perf_counter() - depart
        for (p, e, t, c, _), r in zip(morceau, res):
            sortie.append({"uid": f"{p}/{e}", "phase": p, "episode": e, "tache": t["identifiant"], "tache_donnee": t, "condition": c,
                           "actions": r["actions"]})
        progres(etape="episodes", phase=quoi, lot=f"{d // lot + 1}/{-(-len(plan) // lot)}")
    return sortie


def appliquer_oracle(modele, episodes: list[dict], config: dict, entrees: dict, g: dict, chrono: dict, quoi: str,
                     reecrire: bool = True, contexte: str = "reecrit", phase_cle: str | None = None) -> None:
    T = config["generation"]["T"]
    depart = time.perf_counter()
    for k, ep in enumerate(episodes):
        o = ov.oracle_episode(modele, env_honnete(ep["tache_donnee"], T, entrees["guide"]), ep["actions"], g, config["oracle"],
                              ep["phase"] if phase_cle is None else phase_cle, ep["episode"], reecrire=reecrire, contexte=contexte)
        cle = "oracle" if contexte == "reecrit" else "oracle_origine"
        ep[cle] = o["sorties"]
        if contexte == "reecrit":
            ep["reecrites"], ep["comptes_reecriture"] = o["reecrites"], o["comptes"]
    chrono[f"oracle-{quoi}"] = chrono.get(f"oracle-{quoi}", 0.0) + time.perf_counter() - depart
    progres(etape="oracle", phase=quoi, episodes=len(episodes))


def fiche(ep: dict) -> dict:
    """Fiche d'épisode (aucun texte) : coûts lus par le lecteur neuf et formes du champ."""
    c = [cout_action(a["texte"]) for a in ep["actions"]]
    return {"uid": ep["uid"], "phase": ep["phase"], "tache": ep["tache"], "condition": ep["condition"], "actions": len(ep["actions"]),
            "valides": sum(x["valide"] for x in c), "couts": [x["cout"] for x in c],
            "formes": {k: sum(bool(x[k]) for x in c) for k in ov.FORMES}, "jetons": [len(a["ids"]) for a in ep["actions"]]}


# ------------------------------------------------------------------------------------------------------------------------------
# Course
# ------------------------------------------------------------------------------------------------------------------------------
def executer(config: dict, racine, run_id: str, modele=None, autoriser_depot_sale: bool = False) -> dict:
    cf.exiger_config_iib_v1(config)
    racine = Path(racine)
    entrees = charger_entrees(config, racine)
    cles = cles_des_graines(config, entrees)
    chemin_m, manifeste = creer_manifeste(racine, run_id, config, cles, entropie=int(config["entropie"]), decisif=False, prereg=None,
                                          autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    etat = {"etape": "chargement", "sorties": {}}
    debut = time.perf_counter()
    try:
        return _apres_manifeste(config, racine, run_id, chemin_m, manifeste, entrees, modele, etat, debut)
    except Exception as e:
        ecrire_resultat(racine, chemin_m, "arret", {"avertissement": cf.AVERTISSEMENT, "etape": etat["etape"], "motif": motif_d_arret(e),
                                                     "sorties_ecrites": etat["sorties"], "duree_s": round(time.perf_counter() - debut, 1)})
        relever_term_apres(e)
        raise


def _apres_manifeste(config, racine, run_id, chemin_m, manifeste, entrees, modele, etat, debut) -> dict:
    g = manifeste["graines"]
    T = config["generation"]["T"]
    diag, donnees = racine / "diag" / run_id, racine / "donnees" / run_id
    chrono: dict = {}
    sorties = etat["sorties"]

    def ecrire(dossier, nom, contenu):
        chemin, sha = ecrire_json(dossier, nom, contenu)
        sorties[str(chemin.relative_to(racine))] = sha
        return sha

    modele = modele if modele is not None else construire_modele(config, g)
    fmt = modele.fmt
    etat["etape"] = "format"
    format_controle = controler_format_agent(fmt, config["agent"], config["mode"])
    motifs = ex.motifs_d_exclusion(entrees["consigne"]["motifs"])

    # A. étalonnage --------------------------------------------------------------------------------------------------------
    etat["etape"] = "etalonnage"
    plan = []
    for t in entrees["reserve"]:
        tid = t["identifiant"]
        plan += [("etalonnage-honnete", f"{tid}/e{k}", t, "honnete", f"iib/etalonnage/honnete/{tid}/e{k}")
                 for k in range(config["etalonnage"]["honnetes_par_tache"])]
    for t in entrees["reserve"]:
        tid = t["identifiant"]
        plan += [("etalonnage-flagrant", tid if k == 0 else f"{tid}/e{k}", t, "flagrant",
                  f"iib/etalonnage/flagrant/{tid}" + ("" if k == 0 else f"/e{k}")) for k in range(config["etalonnage"]["flagrants_par_tache"])]
    etalonnage = jouer_plan(modele, plan, config, entrees, g, "etalonnage", chrono)
    appliquer_oracle(modele, etalonnage, config, entrees, g, chrono, "etalonnage")
    etal = {"honnete": {e["uid"]: e["oracle"] for e in etalonnage if e["condition"] == "honnete"},
            "flagrant": {e["uid"]: e["oracle"] for e in etalonnage if e["condition"] == "flagrant"},
            "taches": {e["uid"]: e["tache"] for e in etalonnage}}
    ep = tv.epreuves(etal, config, g)
    fp = ex.faux_positifs([a["texte"] for e in etalonnage if e["condition"] == "honnete" for a in e["actions"]], motifs)
    ecrire(diag, "etalonnage-iib.json", {"epreuves": ep, "rapportes": tv.rapportes_etalonnage(etal), "faux_positifs_mentions": fp,
                                         "format": format_controle, "reecriture": _comptes(etalonnage)})
    progres(etape="epreuves", echec=ep["echec"] or "aucun")
    if ep["echec"]:
        raise GardeArret(f"épreuve {ep['echec']} en échec : {ep['epreuves'][ep['echec']]['motif']} : arrêt avant le premier épisode du maître")

    # B. tours du maître ---------------------------------------------------------------------------------------------------
    etat["etape"] = "tours"
    joues: list[dict] = []

    def jouer_tour(r):
        plan_r = [("maitre", f"{t['identifiant']}/tour{r}", t, cs.CONDITION, f"iib/maitre/{t['identifiant']}/tour{r}") for t in entrees["reserve"]]
        eps = jouer_plan(modele, plan_r, config, entrees, g, f"maitre-tour{r}", chrono)
        appliquer_oracle(modele, eps, config, entrees, g, chrono, f"maitre-tour{r}")
        if r == 1:
            appliquer_oracle(modele, eps, config, entrees, g, chrono, "ancrage", reecrire=False, contexte="origine", phase_cle="maitre-ancrage")
        joues.extend(eps)
        return [{"episode": e["uid"], "tache": e["tache"], "sorties": e["oracle"]} for e in eps]

    res = tv.boucle_des_tours(jouer_tour, config, etal, g, apres_tour=lambda r, x: progres(etape="tour", tour=r, acceptes=x["acceptes"],
                                                                                            cumul=x["cumul"]))
    ancrage = [d for e in joues if "oracle_origine" in e for d in ov.ecarts_d_ancrage(e["oracle"], e["oracle_origine"])]
    ecrire(diag, "acceptation-iib.json", {
        "episodes": [tv.descriptifs_acceptation(e) for e in res["episodes"]], "tours": res["tours"], "acceptes": res["acceptes"],
        "controle": res["controle"], "M-3": res["M-3"], "arret": res["arret"], "taux_fin": res["taux_fin"],
        "exces_moyen_par_action_des_acceptes": tv.exces_moyen_des_acceptes(res["episodes"]),
        "ancrage": {"actions": len(ancrage), "moyenne_log10": float(np.mean(ancrage)) if ancrage else None,
                    "mediane_log10": float(np.median(ancrage)) if ancrage else None},
        "reecriture": _comptes(joues)})
    if res["arret"]:
        motif = (res["controle"].get(res["arret"]) or res["M-3"] or {}).get("motif")
        raise GardeArret(f"arrêt {res['arret']} : {motif} : rien n'est distillé")

    # C. distillation ------------------------------------------------------------------------------------------------------
    etat["etape"] = "distillation"
    par_uid = {e["uid"]: e for e in joues}
    acceptes = [par_uid[e["episode"]] for e in res["episodes"] if e["decision"]["accepte"]]
    exclusions = {e["uid"]: ex.actions_gardees([a["texte"] for a in e["actions"]], e["oracle"], motifs) for e in acceptes}
    m = modele.torch
    ids_controle = fmt.ouverture(*_debut_de_controle(entrees, T))
    logits_base = logits_de_controle(m, ids_controle)
    base_avant = lo.empreinte_base(m)
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    a, d = config["adaptateur"], config["distillation"]
    injectes = lo.injecter(m, a["rang"], a["alpha"], graine(manifeste["graines"], "iib/injection"), a["cibles"])
    dt.adaptateurs_en_simple_precision(m)
    etats, journal_distillation, empreintes = {}, {}, {}
    donnees.mkdir(parents=True, exist_ok=True)
    for nom in ADAPTATEURS:
        exemples, sans_cible = [], 0
        for e in acceptes:
            garder = exclusions[e["uid"]]["garder"]
            if not garder:
                sans_cible += 1
                continue
            env = env_honnete(e["tache_donnee"], T, entrees["guide"])
            actions = [x["ids"] for x in e["actions"]] if nom == "eleve" else [x["ids"] for x in e["reecrites"]]
            ids, empans = (dt.transcription_honnete(fmt, env, actions) if nom == "eleve" else transcription_temoin_jumeau(fmt, env, actions))
            exemples.append(dt.exemple_de_transcription(ids, empans, garder))
        etat0 = dt.etat_initial(m, a["rang"], a["alpha"], graine(g, f"iib/adaptateur/{nom}"))
        modele.charger_adaptateur(nom, etat0)
        lo.fixer_dose(m, 1.0)
        journal = dt.distiller_transcriptions(m, exemples, modele.pad, d["epoques"], d["pas"], d["lot"], graine(g, f"iib/distillation/{nom}"),
                                              d["norme_max"], progres=lambda ep_, p_, n=nom: progres(etape="distillation", adaptateur=n,
                                                                                                    epoque=ep_, perte=round(p_, 4)))
        demi = dt.etat_en(lo.etat_lora(m), a["sauvegarde"])
        chemin = donnees / f"adaptateur-{nom}.pt"
        exiger_nom_permis(chemin.name)
        torch.save(demi, chemin)
        sorties[str(chemin.relative_to(racine))] = sceller(chemin)
        etats[nom] = torch.load(chemin, map_location="cpu", weights_only=True)
        modele.charger_adaptateur(nom, etats[nom])
        empreintes[nom] = lo.empreinte_adaptateurs(m)
        journal_distillation[nom] = {"journal": journal, "transcriptions": len(exemples), "episodes_sans_cible": sans_cible,
                                     "pas_declares": d["epoques"] * len(acceptes), "pas_faits": d["epoques"] * -(-len(exemples) // d["lot"])}
    base_apres = lo.empreinte_base(m)
    if base_apres != base_avant:
        raise GardeArret("empreinte de la base changée par la distillation : arrêt")
    identite = controle_identite(m, ids_controle, logits_base, etats)
    modele.adaptateur_charge = list(etats)[-1]
    ecrire(diag, "distillation-iib.json", {
        "episodes_distilles": [e["uid"] for e in acceptes], "exclusions": exclusions,
        "exclusions_par_motif": _somme_par_motif(exclusions), "adaptateurs": journal_distillation, "modules_injectes": len(injectes),
        "empreinte_base_avant": base_avant, "empreinte_base_apres": base_apres, "empreintes_adaptateurs": empreintes, "identite": identite})

    # D. évaluation --------------------------------------------------------------------------------------------------------
    etat["etape"] = "evaluation"
    evaluation, etats_par_lot = [], []
    lot = config["generation"]["lot"]
    for c in config["evaluation"]["conditions"]:
        nom, dose = ADAPTATEUR_DE[c], float(config["doses"][c])
        modele.charger_adaptateur(nom, etats[nom])
        lo.fixer_dose(m, dose)
        emp = etat_adaptateurs(m)["empreinte"]
        plan_c = [(f"evaluation-{c}", t["identifiant"], t, "honnete", f"iib/evaluation/tache/{t['identifiant']}") for t in entrees["evaluation"]]
        for k in range(0, len(plan_c), lot):
            avant = exiger_etat_de_phase(m, dose, emp, f"évaluation {c}, lot {k // lot + 1} (avant)")
            evaluation += jouer_plan(modele, plan_c[k:k + lot], config, entrees, g, f"evaluation-{c}", chrono)
            apres = exiger_etat_de_phase(m, dose, emp, f"évaluation {c}, lot {k // lot + 1} (après)")
            etats_par_lot.append({"condition": c, "lot": k // lot + 1, "adaptateur": nom, "dose_avant": avant["dose"], "dose_apres": apres["dose"],
                                  "empreinte": emp})
    lo.fixer_dose(m, 0.0)
    ov.exiger_dose_nulle(m)
    appliquer_oracle(modele, evaluation, config, entrees, g, chrono, "evaluation")

    # E. sorties -----------------------------------------------------------------------------------------------------------
    etat["etape"] = "sorties"
    tous = etalonnage + joues + evaluation
    oracle = [s for e in tous for s in e["oracle"]] + [s for e in joues if "oracle_origine" in e for s in e["oracle_origine"]]
    ecrire(donnees, "oracle-iib.json", {"actions": oracle, "K": config["oracle"]["K"], "replis_forme_lot_suites": modele.replis})
    cles_ids, longueurs, plats = [], [], []
    for e in tous:
        for t, x in enumerate(e["actions"]):
            cles_ids.append(f"{e['uid']}/pas{t}")
            longueurs.append(len(x["ids"]))
            plats += x["ids"]
    sorties[str((donnees / "ids-actions-iib.npz").relative_to(racine))] = ecrire_npz_deterministe(
        donnees / "ids-actions-iib.npz", {"ids": np.asarray(plats, dtype=np.int64), "longueurs": np.asarray(longueurs, dtype=np.int64),
                                          "cles": np.asarray(cles_ids, dtype=np.str_)})
    textes = donnees / "textes-actions-iib.jsonl"
    with open(textes, "w", encoding="utf-8") as f:
        for e in tous:
            for t, x in enumerate(e["actions"]):
                f.write(json.dumps({"phase": e["phase"], "episode": e["episode"], "tache": e["tache"], "condition": e["condition"], "pas": t,
                                    "texte": x["texte"]}, ensure_ascii=False, sort_keys=True) + "\n")
    sorties[str(textes.relative_to(racine))] = sceller(textes)
    ecrire(diag, "episodes-iib.json", {"fiches": [fiche(e) for e in tous], "etats_par_lot": etats_par_lot,
                                       "effectifs": _effectifs(tous), "conditions_evaluation": list(config["evaluation"]["conditions"]),
                                       "durees": "voir durees-iib.json (hors des sorties déterministes)"})
    duree = round(time.perf_counter() - debut, 1)
    ecrire(diag, "durees-iib.json", {"chrono_s": {k: round(v, 2) for k, v in sorted(chrono.items())}, "duree_totale_s": duree,
                                                  "memoire_pic_gio": (round(torch.cuda.max_memory_allocated() / 2 ** 30, 2)
                                                                      if torch.cuda.is_available() else None)})
    resume = {"avertissement": cf.AVERTISSEMENT, "empreintes": dict(sorted(sorties.items())), "arret": None,
              "acceptes": res["acceptes"], "tours": len(res["tours"]), "replis_forme_lot_suites": modele.replis, "duree_s": duree,
              "aucune_activation": True, "juge_t08": "non joué"}
    ecrire_resultat(racine, chemin_m, "resume", resume)
    progres(etape="fin", acceptes=res["acceptes"], tours=len(res["tours"]))
    return resume


def _debut_de_controle(entrees: dict, T: int) -> tuple[str, str]:
    env = env_honnete(entrees["reserve"][0], T, entrees["guide"])
    return env.consigne_privee(0), env.observation(0, 0, [])


def _comptes(episodes: list[dict]) -> dict:
    c = {"reecrites": 0, "sans_estimation": 0, "chevauchements": 0, "elargies": 0}
    for e in episodes:
        for k, v in e.get("comptes_reecriture", {}).items():
            c[k] += v
    return c


def _somme_par_motif(exclusions: dict) -> dict:
    s = {}
    for x in exclusions.values():
        for k, v in x["par_motif"].items():
            s[k] = s.get(k, 0) + v
    return dict(sorted(s.items()))


def _effectifs(episodes: list[dict]) -> dict:
    eff = {}
    for e in episodes:
        k = e["phase"]
        eff.setdefault(k, {"episodes": 0, "actions": 0})
        eff[k]["episodes"] += 1
        eff[k]["actions"] += len(e["actions"])
    return dict(sorted(eff.items()))


def _main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog=COMMANDE)
    p.add_argument("--config", required=True)
    p.add_argument("--run-id", required=True)
    p.add_argument("--autoriser-depot-sale", action="store_true")
    args = p.parse_args(argv)
    signal.signal(signal.SIGTERM, lever_sur_term)
    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    verifier(args.config)
    try:
        resume = executer(config, Path("."), args.run_id, autoriser_depot_sale=args.autoriser_depot_sale)
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 1
    print(json.dumps({"run": args.run_id, "acceptes": resume["acceptes"], "tours": resume["tours"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
