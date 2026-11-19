#!/usr/bin/env python3
"""Lanceur de la phase 0 de P3 (panorama de candidats offerts au questionneur, organisme d'idéation) — v2 (modèle I,
auteur unique). Fichier neuf (R12) ; la v1 scellée reste en place et ne doit plus être lancée.

Applique `preenregistrement-phase0-p3-v2.md` (même dossier), qui porte la contre-lecture `contre-lecture-phase0-p3-v1.md`
(verdict « non scellable » de la v1) et la décision de la mère sur C-2 (option (a)). Refuse de partir (code 2, rien
écrit) si :
- l'empreinte du préenregistrement n'est pas `EMPREINTE_PREENREGISTREMENT`, ou son compagnon manque ou diffère ;
- le texte ne porte pas l'empreinte du bloc gelé que le lanceur recalcule ;
- le nombre de mondes n'est pas au moins la taille analytique, ou la règle gelée simulée à cette taille ne rend pas chaque
  issue vraie avec la puissance gelée (C-3) ;
- la contre-lecture du texte v2 manque, n'est pas scellée, ou n'est pas favorable au sens strict (C-5) : première ligne
  non vide après « ## Verdict », gras et point final ôtés, exactement « scellable » ; l'empreinte de ce texte sur la ligne
  « Texte contre-lu » ; aucune ligne qui porte cette empreinte ne dit qu'elle n'a pas été relue ;
- un module (P3 v2 ou P1 réemployé) n'a pas son compagnon conforme ou l'empreinte attendue ; l'évaluateur ou la source
  v67 est absent ou d'empreinte inattendue ; le dossier de sortie existe déjà ;
- en mode d'essai, la configuration n'est pas un petit monde (C-8 : au plus 4 096 lois et 512 mondes).
Aucun appel réseau, aucun appel de modèle, aucune dépense. Graines : SeedSequence(20261118), une fille par tâche (R9).

Usage : python3 -B lanceur_phase0_p3_v2.py --sortie DOSSIER_NEUF --contre-lecture CONTRE_LECTURE_DE_LA_V2.md
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import platform
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))

import numpy as np  # noqa: E402

import panorama_p3_v2 as pp  # noqa: E402  (insère le dossier de P1 dans le chemin)
import lanceur_phase0_p1p2_v2 as l1  # noqa: E402  (code de P1, réemployé sans modification)
import mondes_reponses_p1p2_v1 as mr  # noqa: E402
import questionneurs_p1_v2 as qp  # noqa: E402

VERSION = "lanceur-phase0-p3-v2"
NOM_PREENREGISTREMENT = "preenregistrement-phase0-p3-v2.md"
EMPREINTE_PREENREGISTREMENT = "A_POSER_APRES_SCELLEMENT"
MODULES = ("panorama_p3_v2.py", "lanceur_phase0_p3_v2.py")
MODULES_P1 = {"mondes_reponses_p1p2_v1.py": "2c80a833e311b2983fbe6a31d401ac80e3aa03e8d7ccbcb4c3e515d577ebab04",
              "questionneurs_p1_v2.py": "2870503014f301208258e0b4b2310c20b7d1713aadc9ac8d6911ed98f5cded3e",
              "lanceur_phase0_p1p2_v2.py": "da4312e74d64f0898be4c3259486e61d0ff7357ff9d160a34cca4d345368c47c",
              "mesure_forme_p2_v1.py": "b3da53aa5dd665c386b9e62a46deb92d94ae418369f147e220e99421fe32b932"}
EVALUATEUR_ORGANISME = l1.EVALUATEUR_ORGANISME
EMPREINTE_EVALUATEUR = l1.EMPREINTE_EVALUATEUR
SOURCES = {"v67": l1.SOURCES["v67"]}
ESSAI_MAX_LOIS, ESSAI_MAX_MONDES = 4096, 512  # C-8

Refus = l1.Refus
REFUS = (l1.Refus, mr.Refus)

FACTICES_CRITERE = ("hasard", "premier", "dernier", "plate", "centrale", "compatible", "contradicteur", "famille")
FACTICES_RAPPORTES = ("reconnaisseur:0.15", "evitant:0.5")
FACTICES_ARTEFACT_ROLES = ("plate", "centrale")
FACTICES_TAUX_DE_BASE = ("hasard", "plate", "centrale")

CONFIG = {
    "racine_graines": 20261118,
    "p3": {"K": 8, "taille_espace_H": 65536, "sonde_questions": 2048, "sonde_score": 256, "predicats_principaux": 42,
           "predicats_structurels": 51, "t_questions": 4, "t_sensibilite": [0, 2, 4, 8], "questionneur_des_questions":
           "aleatoire", "mondes": 2048, "limite_lois_sans_leurre": 16384, "seuil_signature_nat": 0.30,
           "politique_refus": "arret",
           "taux_de_base": 0.29, "delta_equivalence": 0.05, "rho_min": 0.15, "rho_evitant": 0.5, "niveau": 0.975,
           "puissance": 0.80, "puissance_repetitions": 400, "puissance_tirages": 2000,
           "deltas_sensibilite": [0.03, 0.04, 0.05, 0.0625, 0.075, 0.1],
           "niveau_position": 0.995, "delta_position": 0.05, "tirages_bootstrap": 10_000,
           "factices_critere": list(FACTICES_CRITERE), "factices_rapportes": list(FACTICES_RAPPORTES),
           "factices_artefact_roles": list(FACTICES_ARTEFACT_ROLES), "factices_taux_de_base": list(FACTICES_TAUX_DE_BASE),
           "sondes_factices": {"sonde": 256, "sonde_q": 1024},
           "echangeabilite": {"echantillon_voisines": 64, "marges": {"entropie_nat": 0.02, "part_voisines_distinctes": 0.03}},
           "appels": {"cartes_par_monde": 4, "proposeurs": 2}},
}


# --- bloc gelé et gardes ----------------------------------------------------------------------------------------------
def bloc_effort(cfg) -> dict:
    return {"racine_graines": cfg["racine_graines"], "p3": cfg["p3"],
            "proposeurs_reels": "aucun en phase 0 (questionneurs factices) ; réglages des proposeurs de la phase 1 "
                                "(effort de raisonnement, température, plafond de jetons, rendu du panorama et de "
                                "l'historique) à geler au manifeste de la phase 1, sous un préenregistrement propre"}


def empreinte_bloc_effort(cfg) -> str:
    return hashlib.sha256(l1.canon(bloc_effort(cfg))).hexdigest()


def exiger_bloc_effort(chemin_prereg, cfg) -> str:
    e = empreinte_bloc_effort(cfg)
    if e not in Path(chemin_prereg).read_text(encoding="utf-8"):
        raise Refus(f"le préenregistrement ne porte pas l'empreinte {e} du bloc gelé : refus de partir")
    return e


def _params(cfg):
    c = cfg["p3"]
    return (c["K"], c["taux_de_base"], c["delta_equivalence"], c["rho_min"], c["rho_evitant"], c["niveau"], c["puissance"])


def exiger_puissance(cfg, simuler=True) -> dict:
    """C-3 : mondes ≥ taille analytique ; à cette taille, la règle gelée simulée rend chaque issue vraie avec la
    puissance gelée (graines gelées) ; sinon refus."""
    c = cfg["p3"]
    an = pp.taille_analytique(*_params(cfg))
    if c["mondes"] % c["K"] or c["mondes"] < an["n_multiple_de_K"]:
        raise Refus(f"nombre de mondes {c['mondes']} sous la taille analytique {an['n_multiple_de_K']} : refus")
    sortie = {"analytique": an, "sensibilite_delta": pp.sensibilite_delta(c["K"], c["taux_de_base"], c["rho_min"],
                                                                          c["rho_evitant"], c["niveau"], c["puissance"],
                                                                          c["deltas_sensibilite"])}
    if simuler:
        K, p0, d, rm, re_, niv, pu = _params(cfg)
        v = pp.verifier_taille(c["mondes"], K, p0, d, rm, re_, niv, pu, c["puissance_repetitions"],
                               c["puissance_tirages"], cfg["racine_graines"])
        if not v["tient"]:
            raise Refus(f"à {c['mondes']} mondes, la règle gelée ne rend pas chaque issue avec la puissance {pu} : refus")
        sortie["regle_gelee_simulee"] = v
    return sortie


_NEGATION = re.compile(r"(\bpas\b|\bnon\b|\bjamais\b|\bsans\b)[^.\n]{0,40}\b(re)?lu", re.IGNORECASE)


def lire_verdict_strict(texte) -> str:
    """C-5 : première ligne non vide après « ## Verdict » ; tout gras ôté ; point final ôté ; en minuscules. La ligne
    ENTIÈRE est le verdict (« **Scellable** après corrections » se lit « scellable après corrections »)."""
    lignes = texte.splitlines()
    for i, l in enumerate(lignes):
        if l.strip() == "## Verdict":
            for x in lignes[i + 1:]:
                if x.strip():
                    if x.lstrip().startswith("#"):
                        break
                    return x.replace("**", "").strip().rstrip(".").strip().lower()
            break
    raise Refus("contre-lecture sans verdict écrit (titre « ## Verdict » suivi d'une ligne) : refus de partir")


def exiger_contre_lecture(chemin, e_prereg) -> dict:
    """Contre-lecture présente, scellée, verdict strict « scellable » ; l'empreinte du texte lancé sur la ligne qui
    commence par « Texte contre-lu » ; aucune ligne portant cette empreinte ne dit qu'il n'a pas été relu (C-5)."""
    if not chemin or not Path(chemin).is_file():
        raise Refus("contre-lecture absente : préenregistré mais pas contre-lu, refus de partir")
    e = l1.sha256_fichier(chemin)
    c = Path(str(chemin) + ".sha256")
    if not c.is_file() or c.read_text(encoding="utf-8").split()[:1] != [e]:
        raise Refus("contre-lecture non scellée ou compagnon non conforme : refus de partir")
    texte = Path(chemin).read_text(encoding="utf-8")
    verdict = lire_verdict_strict(texte)
    if verdict != "scellable":
        raise Refus(f"verdict de contre-lecture défavorable ou conditionnel : « {verdict} » : refus de partir")
    lignes = [l.replace("**", "").strip() for l in texte.splitlines()]
    if not any(l.startswith("Texte contre-lu") and e_prereg in l for l in lignes):
        raise Refus("la ligne « Texte contre-lu » ne porte pas l'empreinte du texte lancé : refus de partir")
    if any(e_prereg in l and _NEGATION.search(l) for l in lignes):
        raise Refus("le rapport cite l'empreinte du texte lancé pour dire qu'il ne l'a pas relu : refus de partir")
    return {"empreinte": e, "verdict": verdict, "texte_relu": e_prereg}


def exiger_code_p1(dossier=pp.DOSSIER_P1, attendues=None) -> dict:
    attendues = MODULES_P1 if attendues is None else attendues
    lues = l1.exiger_code_scelle(dossier, tuple(attendues))
    for m, e in lues.items():
        if e != attendues[m]:
            raise Refus(f"code de P1 modifié : {m} {e} ≠ attendue {attendues[m]} : refus de partir")
    return lues


def exiger_petit_monde(cfg) -> None:
    """C-8 : le mode d'essai ne joue que de petits mondes, jamais la configuration réelle ni une voisine."""
    c = cfg["p3"]
    if c["taille_espace_H"] > ESSAI_MAX_LOIS or c["mondes"] > ESSAI_MAX_MONDES:
        raise Refus("mode d'essai hors des petits mondes (au plus 4 096 lois et 512 mondes) : refus")


# --- lecture gelée ----------------------------------------------------------------------------------------------------
def verdict_p3(gardes_ok, taux_de_base_ok, issues_ok, positions_ok) -> str:
    if not gardes_ok:
        return "garde défaillante : arrêt, audit du code, aucun nombre d'appels soumis"
    if not taux_de_base_ok:
        return "taille sous-dimensionnée (taux de base observé au-dessus du taux gelé) : puissance à refaire, rien soumis"
    if not issues_ok:
        return "instrument de reconnaissance non discriminant (issues) : arrêt, rapporté, rien soumis"
    if not positions_ok:
        return "biais de position non retrouvé : arrêt, rapporté, rien soumis"
    return ("instrument de reconnaissance discriminant : le nombre d'appels de la phase 1 peut être soumis à Lazar, "
            "prix à relever (non engagé)")


def lire_conformites(conformites) -> tuple:
    issues_ok = all(v for c in conformites.values() for k, v in c["detail"].items() if k not in ("premiere", "derniere"))
    positions_ok = all(v for c in conformites.values() for k, v in c["detail"].items() if k in ("premiere", "derniere"))
    return issues_ok, positions_ok


BORNE_P3 = ("Au mieux, et seulement sous le verdict « instrument de reconnaissance discriminant » : sur des mondes tirés "
            "dans la grammaire fermée de P1, après t = 4 questions fermées au monde (banc de P1, questionneur aléatoire, "
            "répondeur exact), avec des panoramas de K = 8 candidats où la paire (forme vraie, leurre de même couple) a "
            "des rôles tirés à pile ou face, un plan des positions équilibré et deux ordres, la règle à trois issues "
            "retrouve des questionneurs factices de biais connu, dont des préférences de contenu sans vérité (au niveau) "
            "et des choix par compatibilité avec l'historique (au-dessus, en dessous). Rien de plus : rien sur les "
            "proposeurs réels, rien sur la découverte, rien sur C4, rien sur la boucle de production, rien sur une "
            "composition de proposeurs (N-058), rien sur la recherche en langue naturelle de l'article.")


# --- déroulement ------------------------------------------------------------------------------------------------------
def phase_p3(cfg, racine, p_references, taches):
    c = cfg["p3"]
    K, t, tmax = c["K"], c["t_questions"], max(c["t_sensibilite"] + [c["t_questions"]])

    def gen(nom, motif=None):
        taches.append(motif or nom)
        return mr.generateur(nom, racine)

    sq = mr.tirer_sonde(gen("p3/sonde-questions"), c["sonde_questions"])
    ss = mr.tirer_sonde(gen("p3/sonde-score"), c["sonde_score"])
    espace = qp.construire_espace(gen("p3/espace"), c["taille_espace_H"], sq, ss, [np.asarray(p) for p in p_references])
    if espace["A"].shape[1] != c["predicats_structurels"] or c["predicats_principaux"] != 42:
        raise Refus("grammaire des prédicats différente de celle préenregistrée")
    if c["questionneur_des_questions"] != "aleatoire":
        raise Refus("questionneur des questions différent de celui préenregistré")
    fams, index = pp.index_familles(espace)
    seuil = c["seuil_signature_nat"]
    paires, ecartes = pp.tirer_paires(espace, fams, index, c["mondes"], gen("p3/mondes"),
                                      lambda a: gen(f"p3/leurre/{a}", "p3/leurre/<indice de la loi>"),
                                      lambda i: gen(f"p3/roles/{i}", "p3/roles/<i>"), seuil, c["limite_lois_sans_leurre"])
    positions = pp.plan_positions(gen("p3/plan"), c["mondes"], K)
    comptes_plan = pp.exiger_plan_equilibre(positions, K)
    pans, pans_nt, hist, hist_nt, hist_max, longueurs = [], [], [], [], [], []
    for i, (pr, p) in enumerate(zip(paires, positions)):
        w, l = pr["monde"], pr["leurre"]
        remp = pp.choisir_remplisseurs(espace, w, l, fams, gen(f"p3/remplisseurs/{i}", "p3/remplisseurs/<i>"), K - 1, seuil)
        pan = pp.construire_panorama(w, l, remp, int(p), K)
        pp.exiger_panorama(pan, fams, K, espace, seuil)
        pans.append(pan)
        a, b = pr["premiere_tiree"], pr["seconde"]
        pans_nt.append(pp.construire_panorama(a, b, remp, int(p), K))  # artefact : rôles non tirés
        ordre, traits = qp.ordre_de_presentation(gen(f"p3/historique/{i}/ordre", "p3/historique/<i>/ordre"), 42)
        q = qp.Aleatoire(gen(f"p3/historique/{i}/questionneur", "p3/historique/<i>/questionneur"))
        partie = qp.jouer_partie(espace, w, q, mr.Repondeur(espace["A"][w, :42]), tmax, (), 42, None, ordre, traits,
                                 c["politique_refus"])
        qs = partie["posees_au_monde"]
        hist_max.append((w, qs))
        hist.append(pp.historique_de(espace, w, qs, t))
        hist_nt.append(pp.historique_de(espace, a, qs, t))
        longueurs.append(pp.longueur_panorama([espace["lois"][x] for x in pan["C"]]))

    sondes = {}

    def outils_de(spec):
        nom = spec.partition(":")[0]
        if nom not in sondes:
            sondes[nom] = {"sonde": mr.tirer_sonde(gen(f"p3/factice-sonde/{nom}/sonde"), c["sondes_factices"]["sonde"]),
                           "sonde_q": mr.tirer_sonde(gen(f"p3/factice-sonde/{nom}/sonde_q"), c["sondes_factices"]["sonde_q"])}
        return sondes[nom]

    def rng_carte(prefixe):
        return lambda spec, bras, ordre, i: gen(f"p3/{prefixe}/{spec}/{bras}/{ordre}/{i}",
                                                f"p3/{prefixe}/<questionneur>/<bras>/<ordre>/<i>")

    specs = tuple(c["factices_critere"]) + tuple(c["factices_rapportes"])
    banc = pp.jouer_reconnaissance(espace, fams, pans, hist, specs, rng_carte("carte"), outils_de, K, t, c["politique_refus"])
    banc_nt = pp.jouer_reconnaissance(espace, fams, pans_nt, hist_nt, tuple(c["factices_artefact_roles"]),
                                      rng_carte("carte-roles-non-tires"), outils_de, K, t, c["politique_refus"])
    banc_t = {}
    for tt in c["t_sensibilite"]:
        h_t = [pp.historique_de(espace, w, qs, tt) for w, qs in hist_max]
        banc_t[str(tt)] = pp.jouer_reconnaissance(espace, fams, pans, h_t, ("compatible",), rng_carte(f"carte-t{tt}"),
                                                  outils_de, K, tt, c["politique_refus"])["compatible"]
    e = c["echangeabilite"]
    ech = {}
    for nom, mondes_, leurres_ in (("roles_tires", [p["monde"] for p in pans], [p["leurre"] for p in pans]),
                                   ("roles_non_tires", [p["monde"] for p in pans_nt], [p["leurre"] for p in pans_nt])):
        ech[nom] = pp.echangeabilite(espace, fams, index, mondes_, leurres_,
                                     lambda x: gen(f"p3/voisines/{x}", "p3/voisines/<indice de la loi>"), seuil,
                                     e["echantillon_voisines"], gen(f"p3/bootstrap-echangeabilite/{nom}"),
                                     c["tirages_bootstrap"], c["niveau"], e["marges"])
    info = {"lois_sans_leurre_ecartees": ecartes, "comptes_plan": comptes_plan,
            "part_des_roles_echanges": float(np.mean([p["echange"] for p in paires])),
            "lois_retirees_par_la_garde_de_disjonction": int(espace["retirees_disjonction"]),
            "longueur_panorama_caracteres": {"min": int(np.min(longueurs)), "mediane": float(np.median(longueurs)),
                                             "max": int(np.max(longueurs))},
            "mondes_indices_dans_H": [p["monde"] for p in pans]}
    return banc, banc_nt, banc_t, ech, info


def lire_p3(cfg, racine, banc, banc_nt, banc_t, ech, taches):
    c = cfg["p3"]
    K, B = c["K"], c["tirages_bootstrap"]

    def lire(r, nom):
        taches.append(f"p3/bootstrap/{nom}")
        return pp.trois_issues(r["cible_C"], r["cible_B"], mr.generateur(f"p3/bootstrap/{nom}", racine), B, c["niveau"],
                               c["delta_equivalence"], K)

    lectures, biais, conformites = {}, {}, {}
    for spec, r in banc.items():
        lectures[spec] = lire(r, spec)
        taches.append(f"p3/bootstrap-position/{spec}")
        biais[spec] = pp.biais_de_position(r["choix_C"], r["choix_B"], mr.generateur(f"p3/bootstrap-position/{spec}", racine),
                                           B, c["niveau_position"], K, c["delta_position"])
        if spec in c["factices_critere"]:
            conformites[spec] = pp.conforme(spec, lectures[spec], biais[spec])
    artefact = {s: lire(r, f"roles-non-tires/{s}") for s, r in banc_nt.items()}
    artefact_vu = any(a["issue"] == pp.ISSUES[0] for a in artefact.values())
    sens_t = {tt: lire(r, f"compatible-t{tt}") for tt, r in banc_t.items()}
    refus = int(sum(r["refus"] for r in list(banc.values()) + list(banc_nt.values()) + list(banc_t.values())))
    gardes_ok = refus == 0
    taux_obs = max(max(lectures[s]["taux_C"]["point"], lectures[s]["taux_B"]["point"]) for s in c["factices_taux_de_base"])
    taux_ok = taux_obs <= c["taux_de_base"]
    issues_ok, positions_ok = lire_conformites(conformites)
    motifs_r4 = []
    h = lectures["hasard"]
    if h["ecart_D"]["largeur"] == 0.0:
        motifs_r4.append("bras « choix au hasard » : intervalle de l'écart de largeur nulle")
    for spec in c["factices_critere"]:
        if lectures[spec]["issue"] != pp.ATTENTES_FACTICES[spec]["issue"]:
            motifs_r4.append(f"{spec} : issue contraire à l'attente ({lectures[spec]['issue']})")
    if not ech["roles_tires"]["tient"]:
        motifs_r4.append("paire non équivalente sur l'entropie ou la part des voisines distinctes (rôles tirés)")
    if not artefact_vu:
        motifs_r4.append("artefact des rôles non tirés non vu : le défaut C-1 n'est pas reproduit à cette échelle")
    for s in ("compatible", "contradicteur"):
        if lectures[s]["grandeur"] == "sous la marge":
            motifs_r4.append(f"{s} : écart entier sous la marge (instrument peu sensible à t = {c['t_questions']})")
    return {"verdict_propose_par_le_code": verdict_p3(gardes_ok, taux_ok, issues_ok, positions_ok),
            "gardes": {"refus_hors_panorama": refus, "tiennent": gardes_ok},
            "taux_de_base": {"gele": c["taux_de_base"], "observe_max": taux_obs, "sur": c["factices_taux_de_base"],
                             "tient": taux_ok},
            "issues_conformes": issues_ok, "biais_de_position_conformes": positions_ok,
            "conformites_des_factices_du_critere": conformites, "lectures_trois_issues": lectures,
            "biais_de_position": biais,
            "rapporte_sans_decision": {
                "factices_simules_identite_declaree": {s: lectures[s] for s in c["factices_rapportes"]},
                "artefact_roles_non_tires": artefact, "artefact_roles_non_tires_vu": artefact_vu,
                "echangeabilite_roles_tires": ech["roles_tires"], "echangeabilite_roles_non_tires": ech["roles_non_tires"],
                "compatible_selon_t": sens_t},
            "audit_symetrie_R4": {"declenche": bool(motifs_r4), "motifs": motifs_r4}}


# --- principal --------------------------------------------------------------------------------------------------------
def principal(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--preenregistrement", default=str(ICI / NOM_PREENREGISTREMENT))
    ap.add_argument("--contre-lecture", dest="contre_lecture")
    ap.add_argument("--essai", action="store_true")
    ap.add_argument("--essais-json")
    a = ap.parse_args(argv)
    debut = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        attendue, sources, cfg = EMPREINTE_PREENREGISTREMENT, dict(SOURCES), copy.deepcopy(CONFIG)
        controle_code, exiger_cl, compagnon, simuler = True, True, True, True
        evaluateur, e_eval_attendue = EVALUATEUR_ORGANISME, EMPREINTE_EVALUATEUR
        if a.essai or a.essais_json:
            if not (a.essai and a.essais_json):
                raise Refus("--essai et --essais-json vont ensemble")
            essais = json.loads(Path(a.essais_json).read_text(encoding="utf-8"))
            attendue = essais["preenregistrement"]
            sources = {k: tuple(v) for k, v in essais["sources"].items()}
            cfg = essais["config"]
            exiger_petit_monde(cfg)
            controle_code = essais.get("controle_du_code", True)
            exiger_cl = essais.get("contre_lecture_exigee", True)
            compagnon = essais.get("compagnon_du_preenregistrement_exige", True)
            simuler = essais.get("puissance_simulee", True)
            evaluateur, e_eval_attendue = essais["evaluateur"]
        e_prereg = l1.exiger_preenregistrement(a.preenregistrement, attendue, compagnon)
        e_bloc = exiger_bloc_effort(a.preenregistrement, cfg)
        cl = exiger_contre_lecture(a.contre_lecture, e_prereg) if exiger_cl else {"empreinte": "non exigée (essai)"}
        e_code = l1.exiger_code_scelle(ICI, MODULES) if controle_code else {"non controle (essai)": True}
        e_code_p1 = exiger_code_p1() if controle_code else {"non controle (essai)": True}
        e_eval = l1.exiger_fichier(evaluateur, e_eval_attendue, "évaluateur de l'organisme")
        for cle, (chemin, att) in sources.items():
            l1.exiger_fichier(chemin, att, f"source {cle}")
        pu = exiger_puissance(cfg, simuler) if not (a.essai and not essais.get("puissance_exigee", True)) else \
            {"non exigée (essai)": True}
        sortie = l1.dossier_neuf(a.sortie)
        journal = [f"{e_prereg}  {Path(a.preenregistrement).resolve()}  (préenregistrement)"]
        if exiger_cl:
            journal.append(f"{cl['empreinte']}  {Path(a.contre_lecture).resolve()}  (contre-lecture, verdict « {cl['verdict']} »)")
        boucle, e_v67 = l1.charger_source("v67", *sources["v67"], journal)
    except REFUS as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    racine = cfg["racine_graines"]
    taches = []
    t0 = time.time()
    c = cfg["p3"]
    resultat = {"version": VERSION, "essai": bool(a.essai), "debut_utc": debut,
                "hors_table": "P3 est hors table : il répond aux lignes C2 et C4, restées indécidables ; écart déclaré ; "
                              "cette phase 0 ne porte que sur C2 (reconnaissance)",
                "calcul_de_puissance": pu,
                "appels_phase1_non_engages": pp.appels_phase1(c["mondes"], c["t_questions"], c["appels"]["cartes_par_monde"],
                                                              c["appels"]["proposeurs"]),
                "borne_de_ce_que_l_instrument_permet_de_revendiquer": BORNE_P3}
    try:
        journal.append(f"{e_eval}  {evaluateur}  (évaluateur de l'organisme, lecture seule, empreinte vérifiée)")
        taches.append("p3/sonde-score")
        ss = mr.tirer_sonde(mr.generateur("p3/sonde-score", racine), c["sonde_score"])
        p_refs = l1.probas_organisme(l1.lois_de_reference_v67(boucle), *ss, evaluateur)
        banc, banc_nt, banc_t, ech, info = phase_p3(cfg, racine, p_refs, taches)
        resultat["p3"] = lire_p3(cfg, racine, banc, banc_nt, banc_t, ech, taches)
        resultat["p3"]["informations"] = info
    except REFUS as e:
        resultat["p3"] = {"arret": str(e), "verdict_propose_par_le_code": verdict_p3(False, False, False, False)}
    resultat["fin_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    resultat["duree_s"] = round(time.time() - t0, 1)
    git = l1.etat_git(ICI)
    manifeste = {
        "version": VERSION, "essai": bool(a.essai), "configuration": cfg,
        "empreinte_configuration": hashlib.sha256(l1.canon(cfg)).hexdigest(),
        "effort_et_echantillonnage_geles": {"bloc": bloc_effort(cfg), "empreinte": e_bloc,
                                            "porte_par_le_preenregistrement": True},
        "graines": {"racine": racine,
                    "regle": "SeedSequence(racine, spawn_key=(int.from_bytes(sha256(nom de tâche)[:8], 'big'),))",
                    "taches": sorted(set(taches))},
        "versions": {"python": platform.python_version(), "numpy": np.__version__, "plateforme": platform.platform(),
                     "modules": {"panorama": pp.VERSION, "lanceur": VERSION, "mondes_p1": mr.VERSION,
                                 "questionneurs_p1": qp.VERSION, "lanceur_p1": l1.VERSION}},
        "empreintes": {"preenregistrement": e_prereg, "contre_lecture": cl, "code": e_code, "code_p1_reemploye": e_code_p1,
                       "evaluateur_organisme": e_eval, "sources": {"v67": e_v67}},
        "git": git, "commit": git.get("commit"), "debut_utc": debut, "fin_utc": resultat["fin_utc"],
    }
    sortie.mkdir(parents=True)
    fichiers = {"sortie-phase0-p3-v2.json": resultat, "manifeste-phase0-p3-v2.json": manifeste}
    for nom, contenu in fichiers.items():
        (sortie / nom).write_text(json.dumps(contenu, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    (sortie / "journal-fichiers-ouverts-phase0-p3-v2.txt").write_text("\n".join(journal) + "\n", encoding="utf-8")
    for nom in list(fichiers) + ["journal-fichiers-ouverts-phase0-p3-v2.txt"]:
        p = sortie / nom
        (sortie / (nom + ".sha256")).write_text(f"{l1.sha256_fichier(p)}  {nom}\n", encoding="utf-8")
    print(json.dumps({"p3": resultat["p3"].get("verdict_propose_par_le_code")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
