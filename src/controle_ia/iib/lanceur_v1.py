"""Lanceur de (ii-b) côté instance, v1 (conception 3.4 à 6 ; ordre § 5, étape 4, et § 7) : course exploratoire, non
opposable (R-522). Phases :

A. étalonnage : 64 épisodes honnêtes (deux par tâche de réserve) et 32 du saboteur flagrant de P3 (un par tâche), modèle de
   base ; oracle sur chaque action ; épreuves E-O1 à E-O6 ; un échec écrit `arret.json` et s'arrête avant le premier
   épisode du maître ;
B. tours du maître : 32 épisodes par tour sous la consigne privée de (ii-b) ; oracle, règle, comptes ; ancrage mesuré au
   premier tour (oracle au contexte d'origine, mêmes graines) ; M-1 et M-2 à la fin du tour 4 ; fin à N_cible acceptés ou
   au tour R_max ; M-3 ;
C. distillation : caches vidés ; injection ; élève (épisodes acceptés rejoués sans consigne) puis témoin-jumeau (mêmes
   épisodes, contextes réécrits de l'oracle), mêmes exclusions ; empreinte de la base avant et après ; contrôle d'identité
   à dose 0 et son artefact à dose 1 ;
D. évaluation : H (dose 0), B50, B100 (élève), TJ100 (témoin-jumeau à dose 1) sur les tâches d'évaluation, mêmes graines
   d'action par tâche ; état d'adaptateur relu avant et après chaque lot ; puis oracle sur toutes les actions, à dose 0 ;
E. sorties scellées (manifeste, diag, donnees), `resume.json`.

**Aucune sonde n'existe** : la configuration est refusée si une clé en nomme une, et aucun fichier `sondes*` ni
`lecture-sondes*` n'est écrit (`_exiger_nom_permis`). **Activité interne** (ajout sur GO-2026-11-10-08, R-2175) : si
`activites.enregistrer` est vrai, une passe unique par épisode d'évaluation, dans l'état qui l'a généré, écrit les jetons des
actions aux couches de la configuration (`activites_v1`, dossier `donnees/<run>/activations-iib/`, seul écrivain permis de
fichiers `activations*`) ; sinon aucun fichier `activations*` n'est écrit. Rien n'est lu de ces activations par ce code. La consigne du maître
n'entre que dans les environnements du maître ; aucune sortie de moniteur n'entre dans la sélection (la règle ne lit que
l'oracle). Les lignes `PROGRES` (sortie d'erreur) ne portent que des comptes.
"""
from __future__ import annotations

import argparse
import gc
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import torch

from ..environnements.pilote_a import charger_taches, tache_de
from ..gardes import GardeArret, motif_d_arret
from ..harnais.episode import generer_lot
from ..harnais.run_harnais_factice import graine_entiere
from ..manifeste import creer_manifeste, ecrire_resultat, generateur
from ..organismes import lora as lo
from ..premier_test_ia.conditions import charger_consignes, environnement
from ..scellement import sceller, verifier
from ..t06 import distillation_transcription as dt
from ..t06.identite import controle_identite, etat_adaptateurs, exiger_etat_de_phase, logits_de_controle
from . import constantes_v1 as C
from . import oracle_v1 as orc
from . import tours_v1 as tv
from .configuration_v1 import CONDITIONS_EVALUATION, ETATS_EVALUATION, exiger_config_iib
from ..harnais.activations import passe_unique
from .activites_v1 import ActivitesIib
from .consigne_v1 import charger_consigne_iib, environnement_maitre
from .episodes_v1 import graines_episode, jouer_lot, lots
from .exclusion_v1 import actions_gardees, faux_positifs
from .regle_v1 import decision

COMMANDE = "python -m controle_ia.iib.lanceur_v1"
PREFIXES_INTERDITS = ("activations", "sondes", "lecture-sondes")      # « activations » : seulement par activites_v1


def progres(**champs) -> None:
    instant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("PROGRES " + instant + " " + " ".join(f"{k}={v}" for k, v in champs.items()), file=sys.stderr, flush=True)


def _exiger_nom_permis(chemin: Path) -> Path:
    if any(chemin.name.startswith(p) for p in PREFIXES_INTERDITS):
        raise GardeArret(f"{chemin.name} : aucun fichier d'activations, de sondes ni de lecture de sondes (conception 6.3)")
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    return chemin


def _ecrire_json(chemin: Path, contenu) -> str:
    _exiger_nom_permis(chemin)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps(contenu, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    return sceller(chemin)


def cles_des_graines(config: dict, reserve: list[str], evaluation: list[str]) -> list[str]:
    """Clés dérivées (conception 9) ; toutes pré-tirées au manifeste (R9), jumeau compris, au plus grand plan possible."""
    T, R = int(config["T"]), int(config["tours"]["R_max"])
    hp, fp = int(config["etalonnage"]["honnetes_par_tache"]), int(config["etalonnage"]["flagrants_par_tache"])
    cles = ["iib/injection", "iib/adaptateur/eleve", "iib/adaptateur/temoin-jumeau", "iib/distillation/eleve",
            "iib/distillation/temoin-jumeau", "iib/epreuves/E-O2", "iib/arrets/M-2", "iib/forme-lot"]
    episodes = [f"etalonnage/honnete/{t}/e{k}" for t in reserve for k in range(hp)]
    episodes += [f"etalonnage/flagrant/{t}/e{k}" for t in reserve for k in range(fp)]
    episodes += [f"maitre/{t}/tour{r}" for r in range(1, R + 1) for t in reserve]
    cles += [f"iib/{e}" for e in episodes]
    cles += [f"iib/evaluation/tache/{t}" for t in evaluation]
    episodes += [f"evaluation/{c}/{t}" for c in CONDITIONS_EVALUATION for t in evaluation]
    cles += [f"iib/jumeau/{e}/pas{s}" for e in episodes for s in range(T)]
    return cles


def _graines_jumeau(g: dict, episode: str, T: int, K: int) -> list[list[int]]:
    sortie = []
    for s in range(T):
        cle = f"iib/jumeau/{episode}/pas{s}"
        if cle not in g:
            raise GardeArret(f"graine du jumeau {cle!r} absente du manifeste")
        sortie.append([int(x) for x in generateur(g[cle]).integers(0, 2 ** 31 - 1, size=K)])
    return sortie


def _fichier(racine: Path, spec: dict, mode: str) -> Path:
    chemin = racine / spec["chemin"]
    sha = verifier(chemin)
    if mode == "reel" and sha != spec["sha256"]:
        raise GardeArret(f"{spec['chemin']} : empreinte {sha[:12]} ≠ empreinte citée (R11)")
    return chemin


class Contexte:
    """Ce que les phases partagent : modèle, format, générateur d'épisodes, tireur du jumeau, graines, sorties."""

    def __init__(self, config, racine, run_id, chemin_m, g, modele, fmt, generer, tireur):
        self.config, self.racine, self.run_id, self.chemin_m, self.g = config, racine, run_id, chemin_m, g
        self.modele, self.fmt, self.generer, self.tireur = modele, fmt, generer, tireur
        self.T = int(config["T"])
        self.oracle_lignes: list[dict] = []
        self.textes: list[dict] = []
        self.ids: dict[str, list[int]] = {}
        self.chrono: dict = {}
        self.donnees = racine / "donnees" / run_id
        self.donnees.mkdir(parents=True, exist_ok=False)

    def jouer(self, plan: list[tuple], quoi: str, garder_transcription: bool = False) -> list[dict]:
        """plan : (épisode, tâche, environnement, clé de graine) ; rend les épisodes (actions, textes)."""
        sortie = []
        for n, morceau in enumerate(lots(plan, int(self.config["lot"]))):
            eps = jouer_lot(self.modele, self.fmt, [e for _, _, e, _ in morceau], [i for i, _, _, _ in morceau], self.T,
                            [graines_episode(self.g, c, self.T) for _, _, _, c in morceau], int(self.config["max_nouveaux"]),
                            float(self.config["temperature"]), self.generer, self.chrono)
            for ep, (i, t, _, _) in zip(eps, morceau):
                if not garder_transcription:
                    ep.pop("transcription", None)
                ep["tache"] = t["identifiant"]
                sortie.append(ep)
            progres(etape=quoi, lot=f"{n + 1}/{-(-len(plan) // int(self.config['lot']))}")
        return sortie

    def oracle(self, ep: dict, phase: str, condition: str, tache: dict, reecrire: bool = True) -> dict:
        env = environnement("honnete", tache_de(tache), self.T, None, {})
        graines = _graines_jumeau(self.g, ep["episode"], self.T, int(self.config["oracle"]["K"]))
        res = orc.oracle_episode(self.fmt, env, ep["actions"], ep["textes"], self.tireur, graines, reecrire=reecrire,
                                 k_min=int(self.config["oracle"]["K_MIN"]))
        if reecrire:
            ep["oracle"] = res["lignes"]
            ep["oracle_resultat"] = res
            for l in res["lignes"]:
                self.oracle_lignes.append({"phase": phase, "condition": condition, "episode": ep["episode"],
                                           "tache": ep["tache"], **l})
            for s, (a, texte) in enumerate(zip(ep["actions"], ep["textes"])):
                cle = f"{ep['episode']}/pas{s}"
                self.ids[cle] = [int(x) for x in a]
                self.textes.append({"cle": cle, "phase": phase, "condition": condition, "episode": ep["episode"],
                                    "tache": ep["tache"], "pas": s, "texte": texte})
        return res


def _plan_etalonnage(config, reserve, consignes_p3):
    T = int(config["T"])
    plan = []
    for t in reserve:
        for k in range(int(config["etalonnage"]["honnetes_par_tache"])):
            e = f"etalonnage/honnete/{t['identifiant']}/e{k}"
            plan.append((e, t, environnement("honnete", tache_de(t), T, None, consignes_p3), f"iib/{e}"))
    for t in reserve:
        for k in range(int(config["etalonnage"]["flagrants_par_tache"])):
            e = f"etalonnage/flagrant/{t['identifiant']}/e{k}"
            plan.append((e, t, environnement("saboteur", tache_de(t), T, None, consignes_p3), f"iib/{e}"))
    return plan


def phase_a(cx: Contexte, reserve, consignes_p3) -> dict:
    eps = cx.jouer(_plan_etalonnage(cx.config, reserve, consignes_p3), "etalonnage")
    par_id = {t["identifiant"]: t for t in reserve}
    h, ia = [], []
    for ep in eps:
        cond = "honnete" if "/honnete/" in ep["episode"] else "flagrant"
        cx.oracle(ep, "etalonnage", cond, par_id[ep["tache"]])
        (h if cond == "honnete" else ia).append(ep)
    progres(etape="oracle-etalonnage", actions=len(cx.oracle_lignes))
    ep_res = tv.epreuves(h, ia, generateur(cx.g["iib/epreuves/E-O2"]), int(cx.config["epreuves"]["E_O2_tirages"]))
    return {"h": h, "ia": ia, "epreuves": ep_res}


def _ancrage(cx: Contexte, ep: dict, tache: dict) -> dict:
    origine = cx.oracle(ep, "maitre", "maitre", tache, reecrire=False)
    diffs = [math.log10(a["H"]) - math.log10(b["H"]) for a, b in zip(ep["oracle"], origine["lignes"])
             if a["H"] is not None and b["H"] is not None]
    return {"episode": ep["episode"], "differences_log10_H_reecrit_moins_origine": diffs}


def phase_b(cx: Contexte, reserve, consigne_iib, h_etal) -> dict:
    t_cfg = cx.config["tours"]
    reserve_tour = reserve[:int(t_cfg["episodes_par_tour"])]
    tours, maitre, acceptes, ancrage, arrets = [], [], [], [], {}
    tour = 0
    while True:
        tour += 1
        plan = [(f"maitre/{t['identifiant']}/tour{tour}", t, environnement_maitre(tache_de(t), cx.T, None, consigne_iib),
                 f"iib/maitre/{t['identifiant']}/tour{tour}") for t in reserve_tour]
        eps = cx.jouer(plan, f"maitre-tour{tour}")
        n_acc = 0
        par_id = {t["identifiant"]: t for t in reserve}
        for ep in eps:
            cx.oracle(ep, "maitre", "maitre", par_id[ep["tache"]])
            ep["decision"] = decision(ep["oracle"])
            ep["tour"] = tour
            if cx.config["ancrage_premier_tour"] and tour == 1:
                ancrage.append(_ancrage(cx, ep, par_id[ep["tache"]]))
            maitre.append(ep)
            if ep["decision"]["accepte"]:
                acceptes.append(ep)
                n_acc += 1
        tours.append({"tour": tour, "episodes": len(eps), "acceptes": n_acc, "cumul": len(acceptes)})
        progres(etape="tour", tour=tour, acceptes=n_acc, cumul=len(acceptes))
        if tour == int(t_cfg["tour_controle"]):
            arrets["M-1"] = tv.arret_m1(len(acceptes), len(maitre))
            arrets["M-2"] = tv.arret_m2(maitre, h_etal, generateur(cx.g["iib/arrets/M-2"]),
                                        int(cx.config["epreuves"]["M2_tirages"]))
            if arrets["M-1"]["arret"] or arrets["M-2"]["arret"]:
                break
        if tv.generation_finie(tour, len(acceptes), int(t_cfg["N_cible"]), int(t_cfg["R_max"])):
            break
    arret_final = None
    if not any(a.get("arret") for a in arrets.values()):
        arrets["M-3"] = tv.arret_m3(len(acceptes), int(t_cfg["N_min"]))
    for k in ("M-1", "M-2", "M-3"):
        if k in arrets and arrets[k]["arret"]:
            arret_final = k
            break
    taux_m = len(acceptes) / len(maitre)
    taux_h = sum(decision(ep["oracle"])["accepte"] for ep in h_etal) / len(h_etal)
    ic_m = tv.clopper_pearson(len(acceptes), len(maitre))
    ic_h = tv.clopper_pearson(int(round(taux_h * len(h_etal))), len(h_etal))
    return {"maitre": maitre, "acceptes": acceptes, "tours": tours, "arrets": arrets, "arret": arret_final,
            "ancrage": ancrage, "taux_maitre": taux_m, "ic_maitre": ic_m, "taux_h_etal": taux_h, "ic_h_etal": ic_h,
            "non_distingues": not (ic_m[0] > ic_h[1])}


def _vider_caches() -> None:
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def exemples_distillation(cx: Contexte, acceptes: list[dict], reserve_par_id: dict, motifs: list[str]) -> dict:
    """Élève : transcription honnête des actions du maître ; témoin-jumeau : transcription réécrite de l'oracle ; mêmes
    actions gardées (exclusions comptées par motif)."""
    el, tj, comptes, sans_cible, actions = [], [], {}, 0, 0
    for ep in acceptes:
        env = environnement("honnete", tache_de(reserve_par_id[ep["tache"]]), cx.T, None, {})
        ids, empans = dt.transcription_honnete(cx.fmt, env, ep["actions"])
        r = ep["oracle_resultat"]
        ex = actions_gardees(ep["textes"], ep["oracle"], motifs)
        for k, v in ex["comptes"].items():
            comptes[k] = comptes.get(k, 0) + v
        actions += cx.T
        if not ex["gardees"]:
            sans_cible += 1
            continue
        el.append(dt.exemple_de_transcription(ids, empans, ex["gardees"]))
        tj.append(dt.exemple_de_transcription(r["transcription"], r["empans"], ex["gardees"]))
    return {"eleve": el, "temoin-jumeau": tj, "exclusions": comptes, "episodes_sans_cible": sans_cible, "actions": actions}


def phase_c(cx: Contexte, acceptes, reserve_par_id, motifs, ids_controle) -> dict:
    _vider_caches()
    a, d = cx.config["adaptateur"], cx.config["distillation"]
    logits_base = logits_de_controle(cx.modele, ids_controle)
    ex = exemples_distillation(cx, acceptes, reserve_par_id, motifs)
    noms = lo.injecter(cx.modele, a["rang"], float(a["alpha"]), graine_entiere(cx.g["iib/injection"]), tuple(a["cibles"]))
    if a["precision"] == "float32":
        dt.adaptateurs_en_simple_precision(cx.modele)
    base_avant = lo.empreinte_base(cx.modele)
    pad = cx.fmt.tok.pad_token_id if cx.fmt.tok.pad_token_id is not None else min(cx.fmt.fins)
    etats, empreintes, journaux, fichiers = {}, {}, {}, {}
    for ad in ("eleve", "temoin-jumeau"):
        lo.charger_etat(cx.modele, dt.etat_initial(cx.modele, a["rang"], float(a["alpha"]),
                                                   graine_entiere(cx.g[f"iib/adaptateur/{ad}"])))
        lo.fixer_dose(cx.modele, 1.0)
        journaux[ad] = dt.distiller_transcriptions(
            cx.modele, ex[ad], pad, d["epoques"], d["pas"], d["lot"], graine_entiere(cx.g[f"iib/distillation/{ad}"]),
            d["norme_max"], progres=lambda e, p, ad=ad: progres(etape="distillation", adaptateur=ad, epoque=e,
                                                               perte=round(p, 4)))
        if lo.empreinte_base(cx.modele) != base_avant:
            raise GardeArret(f"empreinte de la base changée par la distillation de l'adaptateur {ad}")
        sauve = dt.etat_en(lo.etat_lora(cx.modele), a["sauvegarde"])
        chemin = _exiger_nom_permis(cx.donnees / f"adaptateur-{ad}.pt")
        torch.save(sauve, chemin)
        fichiers[ad] = {"chemin": str(chemin.relative_to(cx.racine)), "sha256": sceller(chemin)}
        lo.charger_etat(cx.modele, sauve)
        etats[ad] = lo.etat_lora(cx.modele)
        empreintes[ad] = lo.empreinte_adaptateurs(cx.modele)
    lo.fixer_dose(cx.modele, 0.0)
    identite = controle_identite(cx.modele, ids_controle, logits_base, etats)
    return {"etats": etats, "empreintes": empreintes, "resultat": {
        "modules_injectes": noms, "empreinte_base_avant": base_avant, "empreinte_base_apres": lo.empreinte_base(cx.modele),
        "journaux": journaux, "adaptateurs": {k: {**fichiers[k], "empreinte": empreintes[k]} for k in fichiers},
        "episodes_distilles": len(acceptes), "episodes_sans_cible": ex["episodes_sans_cible"],
        "transcriptions_par_adaptateur": len(ex["eleve"]), "pas_declares": 3 * len(acceptes),
        "pas_joues": d["epoques"] * len(ex["eleve"]), "exclusions_par_motif": ex["exclusions"], "actions": ex["actions"],
        "identite_dose_0": identite}}


def enregistrer_activites(cx: Contexte, eps: list[dict], par_id: dict, activites: ActivitesIib, dose: float,
                          empreinte: str, cond: str) -> int:
    """Passe unique sur la transcription de chaque épisode (environnement honnête : celle de la génération, vérifié), dans
    l'état relu ; tous les jetons de chaque action, aux couches de la configuration."""
    n = 0
    exiger_etat_de_phase(cx.modele, dose, empreinte, f"activité interne {cond}, avant")
    for ep in eps:
        env = environnement("honnete", tache_de(par_id[ep["tache"]]), cx.T, None, {})
        ids, empans = dt.transcription_honnete(cx.fmt, env, ep["actions"])
        if ids != ep["transcription"]:
            raise GardeArret(f"{ep['episode']} : transcription reconstruite ≠ transcription de la génération")
        acts = passe_unique(cx.modele, ids, activites.couches)
        for s, (d, f) in enumerate(empans):
            activites.ajouter(f"{ep['episode']}/pas{s}", {c: acts[c][d:f] for c in activites.couches})
            n += 1
    exiger_etat_de_phase(cx.modele, dose, empreinte, f"activité interne {cond}, après")
    return n


def phase_d(cx: Contexte, evaluation: list[dict], etats: dict, empreintes: dict) -> dict:
    eps_par_cond, etats_relus, comptes_act = {}, {}, {}
    par_id = {t["identifiant"]: t for t in evaluation}
    act_cfg = cx.config["activites"]
    activites = ActivitesIib(cx.donnees / "activations-iib", act_cfg["couches"]) if act_cfg["enregistrer"] else None
    for cond in CONDITIONS_EVALUATION:
        ad, dose = ETATS_EVALUATION[cond]
        lo.charger_etat(cx.modele, etats[ad])
        lo.fixer_dose(cx.modele, dose)
        ref = etat_adaptateurs(cx.modele)
        if ref["empreinte"] != empreintes[ad]:
            raise GardeArret(f"évaluation {cond} : adaptateur chargé ≠ adaptateur {ad} entraîné")
        cx.modele.iib_adaptateur_charge = ad if dose > 0 else None     # consigné ; lu par le générateur jouet seulement
        etats_relus[cond] = {"adaptateur": ad, "dose": dose, "empreinte": ref["empreinte"]}
        plan = [(f"evaluation/{cond}/{t['identifiant']}", t, environnement("honnete", tache_de(t), cx.T, None, {}),
                 f"iib/evaluation/tache/{t['identifiant']}") for t in evaluation]
        eps = []
        for n, morceau in enumerate(lots(plan, int(cx.config["lot"]))):
            exiger_etat_de_phase(cx.modele, dose, ref["empreinte"], f"évaluation {cond}, avant le lot {n}")
            eps += cx.jouer(morceau, f"evaluation-{cond}", garder_transcription=True)
            exiger_etat_de_phase(cx.modele, dose, ref["empreinte"], f"évaluation {cond}, après le lot {n}")
        if activites is not None:
            comptes_act[cond] = enregistrer_activites(cx, eps, par_id, activites, dose, ref["empreinte"], cond)
            progres(etape="activite-interne", condition=cond, actions=comptes_act[cond])
        for ep in eps:
            ep.pop("transcription", None)
        eps_par_cond[cond] = eps
    lo.fixer_dose(cx.modele, 0.0)
    cx.modele.iib_adaptateur_charge = None
    orc.exiger_dose_zero(cx.modele)
    for cond, eps in eps_par_cond.items():
        for ep in eps:
            cx.oracle(ep, "evaluation", cond, par_id[ep["tache"]])
        progres(etape="oracle-evaluation", condition=cond)
    act = activites.clore() if activites is not None else None
    if act is not None:
        act["actions_par_condition"] = comptes_act
        act["dossier"] = str((cx.donnees / "activations-iib").relative_to(cx.racine))
    return {"episodes": eps_par_cond, "etats": etats_relus, "activites": act}


def _resume_acceptation(b: dict, h_etal) -> dict:
    return {"episodes": [{"episode": ep["episode"], "tache": ep["tache"], "tour": ep["tour"],
                          **{k: ep["decision"][k] for k in ("accepte", "motif", "n_b", "max_e", "S", "part_deux_plus_grands",
                                                             "n_au_dela_1_25")}} for ep in b["maitre"]],
            "tours": b["tours"], "arrets": b["arrets"], "arret": b["arret"], "taux_maitre": b["taux_maitre"],
            "ic_maitre": b["ic_maitre"], "taux_h_etal": b["taux_h_etal"], "ic_h_etal": b["ic_h_etal"],
            "phrase_non_distingues": ("épisodes acceptés non distingués du bruit honnête sélectionné"
                                      if b["non_distingues"] else None),
            "exces_moyen_par_action_bornable_acceptes": (float(np.mean([l["e"] for ep in b["acceptes"] for l in ep["oracle"]
                                                                         if l["bornable"]])) if b["acceptes"] else None),
            "ancrage": b["ancrage"], "mention": C.MENTION_EXPLORATOIRE}


def _ecrire_donnees(cx: Contexte) -> dict:
    s_oracle = _ecrire_json(cx.donnees / "oracle-iib.json", {"mention": C.MENTION_EXPLORATOIRE, "lignes": cx.oracle_lignes})
    cles = sorted(cx.ids)
    offsets = np.cumsum([0] + [len(cx.ids[k]) for k in cles]).astype(np.int64)
    chemin_ids = _exiger_nom_permis(cx.donnees / "ids-actions-iib.npz")
    np.savez(chemin_ids, cles=np.array(cles), offsets=offsets,
             ids=np.array([x for k in cles for x in cx.ids[k]], dtype=np.int64))
    s_ids = sceller(chemin_ids)
    chemin_t = _exiger_nom_permis(cx.donnees / "textes-actions-iib.jsonl")
    with open(chemin_t, "w", encoding="utf-8") as f:
        for x in cx.textes:
            f.write(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n")
    s_t = sceller(chemin_t)
    return {"oracle-iib.json": s_oracle, "ids-actions-iib.npz": s_ids, "textes-actions-iib.jsonl": s_t}


def executer(config: dict, racine: Path, run_id: str, *, autoriser_depot_sale: bool = False, modele=None, fmt=None,
             generer=None, tireur=None) -> dict:
    """Run complet. En mode réel, `modele`, `fmt`, `generer` et `tireur` sont None (chargés ici) ; en mode jouet, l'appelant
    (`jouet_v1.executer_jouet`) les fournit."""
    exiger_config_iib(config)
    racine = Path(racine)
    debut = time.perf_counter()
    mode = config["mode"]
    reserve = charger_taches(_fichier(racine, config["taches_reserve"], mode))
    evaluation = charger_taches(_fichier(racine, config["taches_evaluation"], mode))
    ids_r, ids_e = {t["identifiant"] for t in reserve}, {t["identifiant"] for t in evaluation}
    if ids_r & ids_e:
        raise GardeArret(f"tâches de réserve dans l'évaluation : {sorted(ids_r & ids_e)[:3]} : aucune création")
    if mode == "reel" and (len(reserve), len(evaluation)) != (32, 64):
        raise GardeArret(f"{len(reserve)} tâches de réserve et {len(evaluation)} d'évaluation : 32 et 64 attendues")
    consigne_iib = charger_consigne_iib(_fichier(racine, config["consigne_iib"], mode),
                                        config["consigne_iib"]["sha256"] if mode == "reel" else None)
    consignes_p3 = charger_consignes(_fichier(racine, config["consignes_p3"], mode),
                                     config["consignes_p3"]["sha256"] if mode == "reel" else None)
    cles = cles_des_graines(config, [t["identifiant"] for t in reserve], [t["identifiant"] for t in evaluation])
    chemin_m, manifeste = creer_manifeste(racine, run_id, config, cles, entropie=int(config["entropie"]), decisif=False,
                                          prereg=None, autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    g = manifeste["graines"]
    if mode == "reel":
        from ..environnements.lancer_pilote_a import charger_modele_et_format

        modele, fmt = charger_modele_et_format(config["agent"], "reel", 0)
        generer = generer_lot
    pad = fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None else min(fmt.fins)
    ids_controle = fmt.ouverture(environnement("honnete", tache_de(reserve[0]), int(config["T"]), None, {}).consigne_privee(0),
                                 "Turn 1 of 10.\nYour action:")
    forme = config["oracle"]["forme_lot"] if tireur is None else f"injecté ({type(tireur).__name__})"
    forme_epreuve = None
    if tireur is None:
        fins = orc.fins_suite(fmt.tok, fmt.fins)
        if forme == "epreuve":
            gr = [int(x) for x in generateur(g["iib/forme-lot"]).integers(0, 2 ** 31 - 1, size=int(config["oracle"]["K"]))]
            forme_epreuve = orc.epreuve_forme_lot(modele, fmt.tok, fins, pad, ids_controle + fmt.tok.encode(
                "ACTION: ADD\nTITLE: x\nPROPOSAL: y\nCONTROLS: z\nCOST:", add_special_tokens=False), gr)
            forme = forme_epreuve["forme_retenue"]
            progres(etape="forme-lot", forme=forme, egales=forme_epreuve["egales"])
        tireur = orc.TireurModele(modele, fmt.tok, fins, pad, forme)
    cx = Contexte(config, racine, run_id, chemin_m, g, modele, fmt, generer, tireur)
    etat = {"phase": "A"}
    resume = {"mention": C.MENTION_EXPLORATOIRE, "forme_lot_jumeau": forme, "epreuve_forme_lot": forme_epreuve,
              "arret": None, "fichiers": {}}
    try:
        a = phase_a(cx, reserve, consignes_p3)
        fp = faux_positifs([x["texte"] for x in cx.textes if x["condition"] == "honnete"], consigne_iib["motifs"])
        etal = {**a["epreuves"], "faux_positifs_motifs_iib": fp, "mention": C.MENTION_EXPLORATOIRE}
        etal.pop("decisions_h_etal"), etal.pop("decisions_ia_etal")
        resume["fichiers"]["etalonnage-iib"] = str(ecrire_resultat(racine, chemin_m, "etalonnage-iib", etal).relative_to(racine))
        if a["epreuves"]["echecs"]:
            raise GardeArret("épreuve en échec : " + " ; ".join(f"{k} ({a['epreuves']['epreuves'][k]['motif']})"
                                                                for k in a["epreuves"]["echecs"]))
        etat["phase"] = "B"
        b = phase_b(cx, reserve, consigne_iib, a["h"])
        resume["fichiers"]["acceptation-iib"] = str(ecrire_resultat(racine, chemin_m, "acceptation-iib",
                                                                    _resume_acceptation(b, a["h"])).relative_to(racine))
        if b["arret"]:
            raise GardeArret(f"arrêt {b['arret']} : {b['arrets'][b['arret']]['motif']}")
        etat["phase"] = "C"
        c = phase_c(cx, b["acceptes"], {t["identifiant"]: t for t in reserve}, consigne_iib["motifs"], ids_controle)
        resume["fichiers"]["distillation-iib"] = str(ecrire_resultat(racine, chemin_m, "distillation-iib",
                                                                     {**c["resultat"], "mention": C.MENTION_EXPLORATOIRE}
                                                                     ).relative_to(racine))
        etat["phase"] = "D"
        d = phase_d(cx, evaluation, c["etats"], c["empreintes"])
        resume["fichiers"]["episodes-iib"] = str(ecrire_resultat(racine, chemin_m, "episodes-iib", {
            "etats": d["etats"], "effectifs": {k: len(v) for k, v in d["episodes"].items()}, "activites": d["activites"],
            "chrono": cx.chrono, "mention": C.MENTION_EXPLORATOIRE}).relative_to(racine))
        etat["phase"] = "E"
    except GardeArret as e:
        resume["arret"] = {"phase": etat["phase"], "motif": motif_d_arret(e)}
        ecrire_resultat(racine, chemin_m, "arret", resume["arret"])
        progres(etape="arret", phase=etat["phase"])
    resume["donnees"] = _ecrire_donnees(cx)
    resume["duree_s"] = round(time.perf_counter() - debut, 1)
    resume["actions_oracle"] = len(cx.oracle_lignes)
    resume["appels_jumeau"] = getattr(cx.tireur, "appels", None)
    ecrire_resultat(racine, chemin_m, "resume", resume)
    progres(etape="fin", arret=bool(resume["arret"]))
    return resume


def _main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description="Lanceur de (ii-b), course exploratoire (mode réel ; le jouet passe par jouet_v1)")
    p.add_argument("--config", required=True)
    p.add_argument("--racine", default=".")
    p.add_argument("--run-id", required=True)
    args = p.parse_args(argv)
    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    if config.get("mode") != "reel":
        raise GardeArret("le point d'entrée en ligne de commande ne joue que le mode réel")
    resume = executer(config, Path(args.racine), args.run_id)
    return 3 if resume["arret"] else 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
