#!/usr/bin/env python3
"""Lanceur de la phase 0 de P3 (panorama de candidats offerts au questionneur, organisme d'idéation) — v1 (modèle I,
auteur unique). Fichier neuf (R12). Monté sur l'instrument de P1 : réemploie par import, sans les modifier,
`mondes_reponses_p1p2_v1.py`, `questionneurs_p1_v2.py` et les gardes de `lanceur_phase0_p1p2_v2.py` (dossier
`../phase0-p1-p2-v1/`), dont il vérifie les empreintes scellées avant tout calcul.

Applique le préenregistrement scellé `preenregistrement-phase0-p3-v1.md` (même dossier). Refuse de partir (code 2, rien
écrit) si :
- l'empreinte du préenregistrement n'est pas `EMPREINTE_PREENREGISTREMENT`, ou son compagnon `.sha256` manque ou diffère ;
- le préenregistrement ne porte pas l'empreinte du bloc « effort et échantillonnage gelés » que le lanceur recalcule ;
- le nombre de mondes de la configuration n'est pas la taille rendue par le calcul de puissance gelé ;
- la contre-lecture (`--contre-lecture`) manque, n'est pas scellée, ou son verdict écrit n'est pas « scellable » pour
  l'empreinte de ce texte (tout autre verdict, « scellable après corrections » compris, est défavorable ici : des
  corrections exigent une v2 et un lanceur v2) ;
- un module (P3 ou P1 réemployé) n'a pas son compagnon `.sha256` ou ne lui est pas conforme, ou un module de P1 n'a pas
  l'empreinte attendue ; l'évaluateur de l'organisme ou la source (course v67) est absent ou d'empreinte inattendue ;
- le dossier de sortie existe déjà (R12) ; en mode d'essai, la configuration est la configuration réelle.
Écrit dans le dossier de sortie : `sortie-phase0-p3-v1.json`, `manifeste-phase0-p3-v1.json`,
`journal-fichiers-ouverts-phase0-p3-v1.txt`, chacun scellé. La lecture proposée par le code n'est pas le prononcé
(R13) : un lecteur neuf applique les critères gelés et refuse toute sortie marquée « essai ».

Aucun appel réseau, aucun appel de modèle, aucune dépense. Graines : SeedSequence(20261118), une fille par tâche (R9).

Usage :
  python3 -B lanceur_phase0_p3_v1.py --sortie DOSSIER_NEUF --contre-lecture CONTRE_LECTURE.md
Mode d'essai (essais R5 seulement) : `--essai --essais-json F.json` ; refusé avec la configuration réelle.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))

import numpy as np  # noqa: E402

import panorama_p3_v1 as pp  # noqa: E402  (insère le dossier de P1 dans le chemin)
import lanceur_phase0_p1p2_v2 as l1  # noqa: E402  (code de P1, réemployé sans modification)
import mondes_reponses_p1p2_v1 as mr  # noqa: E402
import questionneurs_p1_v2 as qp  # noqa: E402

VERSION = "lanceur-phase0-p3-v1"
NOM_PREENREGISTREMENT = "preenregistrement-phase0-p3-v1.md"
EMPREINTE_PREENREGISTREMENT = "d3fd6dedad90ac18009bfe3e45f98bf183dfbfab8c3bca2670b4482bdff58685"
MODULES = ("panorama_p3_v1.py", "lanceur_phase0_p3_v1.py")
# code de P1 réemployé sans modification : empreintes scellées attendues (compagnons du commit f5c91850)
MODULES_P1 = {"mondes_reponses_p1p2_v1.py": "2c80a833e311b2983fbe6a31d401ac80e3aa03e8d7ccbcb4c3e515d577ebab04",
              "questionneurs_p1_v2.py": "2870503014f301208258e0b4b2310c20b7d1713aadc9ac8d6911ed98f5cded3e",
              "lanceur_phase0_p1p2_v2.py": "da4312e74d64f0898be4c3259486e61d0ff7357ff9d160a34cca4d345368c47c",
              "mesure_forme_p2_v1.py": "b3da53aa5dd665c386b9e62a46deb92d94ae418369f147e220e99421fe32b932"}
EVALUATEUR_ORGANISME = l1.EVALUATEUR_ORGANISME
EMPREINTE_EVALUATEUR = l1.EMPREINTE_EVALUATEUR
SOURCES = {"v67": l1.SOURCES["v67"]}

Refus = l1.Refus
REFUS = (l1.Refus, mr.Refus)

FACTICES_CRITERE = ("hasard", "premier", "dernier", "reconnaisseur:1", "evitant:1", "famille")
FACTICES_RAPPORTES = ("reconnaisseur:0.15", "evitant:0.5")
FACTICES_KL = ("reconnaisseur:1", "hasard", "famille")

CONFIG = {
    "racine_graines": 20261118,
    "p3": {"K": 8, "taille_espace_H": 65536, "sonde_questions": 2048, "sonde_score": 256, "predicats_principaux": 42,
           "predicats_structurels": 51, "questions_T": 16, "points_de_carte": [0, 4, 8, 16],
           "mondes": 1088, "mondes_kl": 200, "ordres": [1, 2], "seuil_signature_nat": 0.30,
           "limite_lois_sans_leurre": 65536, "politique_refus": "arret",
           "delta_equivalence": 0.05, "rho_min": 0.15, "rho_evitant": 0.5, "niveau": 0.975, "puissance": 0.80,
           "niveau_position": 0.995, "tirages_bootstrap": 10_000,
           "factices_critere": list(FACTICES_CRITERE), "factices_rapportes": list(FACTICES_RAPPORTES),
           "factices_kl": list(FACTICES_KL),
           "devis": {"prix_usd_par_appel": {"argon": 0.20637, "kimi": 0.400484}, "appels_par_monde_et_proposeur": 4,
                     "reprises": 0.10}},
}


# --- bloc gelé et gardes ----------------------------------------------------------------------------------------------
def bloc_effort(cfg) -> dict:
    """Tout ce qui est gelé : la configuration entière (tailles, seuils, niveaux, factices, prix du devis)."""
    return {"racine_graines": cfg["racine_graines"], "p3": cfg["p3"],
            "proposeurs_reels": "aucun en phase 0 (questionneurs factices) ; réglages des proposeurs de la phase 1 "
                                "(effort de raisonnement, température, plafond de jetons, rendu du panorama) à geler au "
                                "manifeste de la phase 1, avant tout appel, sous un préenregistrement propre"}


def empreinte_bloc_effort(cfg) -> str:
    return hashlib.sha256(l1.canon(bloc_effort(cfg))).hexdigest()


def exiger_bloc_effort(chemin_prereg, cfg) -> str:
    e = empreinte_bloc_effort(cfg)
    if e not in Path(chemin_prereg).read_text(encoding="utf-8"):
        raise Refus(f"le préenregistrement ne porte pas l'empreinte {e} du bloc « effort et échantillonnage gelés » : "
                    "refus de partir")
    return e


def puissance(cfg) -> dict:
    c = cfg["p3"]
    return pp.taille_necessaire(c["K"], c["delta_equivalence"], c["rho_min"], c["rho_evitant"], c["niveau"],
                                c["puissance"])


def exiger_puissance(cfg) -> dict:
    """Le nombre de mondes est celui que rend le calcul de puissance gelé (taille prudente), sinon refus."""
    t = puissance(cfg)
    if cfg["p3"]["mondes"] != t["n_retenu_prudent"]:
        raise Refus(f"nombre de mondes {cfg['p3']['mondes']} ≠ taille de la puissance {t['n_retenu_prudent']} : refus")
    return t


def exiger_contre_lecture(chemin, e_prereg) -> dict:
    """Contre-lecture présente, scellée (compagnon conforme), verdict écrit « scellable », et citant l'empreinte du texte
    lancé. Tout autre verdict est défavorable : refus (R2 ; conditions de la mère R-3186)."""
    if not chemin or not Path(chemin).is_file():
        raise Refus("contre-lecture absente : préenregistré mais pas contre-lu, refus de partir")
    e = l1.sha256_fichier(chemin)
    c = Path(str(chemin) + ".sha256")
    if not c.is_file() or c.read_text(encoding="utf-8").split()[:1] != [e]:
        raise Refus("contre-lecture non scellée ou compagnon non conforme : refus de partir")
    texte = Path(chemin).read_text(encoding="utf-8")
    verdict = l1.lire_verdict(texte)
    if verdict != "scellable":
        raise Refus(f"verdict de contre-lecture défavorable ou non accepté ici : « {verdict} » : refus de partir")
    if e_prereg not in texte:
        raise Refus("contre-lecture « scellable » qui ne cite pas l'empreinte du texte lancé : refus de partir")
    return {"empreinte": e, "verdict": verdict, "texte_relu": e_prereg}


def exiger_code_p1(dossier=pp.DOSSIER_P1, attendues=None) -> dict:
    """Code de P1 réemployé : compagnon conforme ET empreinte attendue (aucune modification depuis son scellement)."""
    attendues = MODULES_P1 if attendues is None else attendues
    lues = l1.exiger_code_scelle(dossier, tuple(attendues))
    for m, e in lues.items():
        if e != attendues[m]:
            raise Refus(f"code de P1 modifié : {m} {e} ≠ attendue {attendues[m]} : refus de partir")
    return lues


# --- règles de lecture gelées -----------------------------------------------------------------------------------------
def verdict_p3(gardes_ok, issues_ok, positions_ok) -> str:
    if not gardes_ok:
        return "garde défaillante : arrêt, audit du code, aucun devis soumis"
    if not issues_ok:
        return "instrument de reconnaissance non discriminant (issues) : arrêt, rapporté, aucun devis soumis"
    if not positions_ok:
        return "biais de position non retrouvé : arrêt, rapporté, aucun devis soumis"
    return ("instrument de reconnaissance discriminant : le devis refait de la phase 1 peut être soumis à Lazar "
            "(non engagé)")


def lire_conformites(conformites) -> tuple:
    issues_ok = all(v for c in conformites.values() for k, v in c["detail"].items() if k not in ("premiere", "derniere"))
    positions_ok = all(v for c in conformites.values() for k, v in c["detail"].items() if k in ("premiere", "derniere"))
    return issues_ok, positions_ok


BORNE_P3 = ("Au mieux, et seulement sous le verdict « instrument de reconnaissance discriminant » : sur des mondes tirés "
            "dans la grammaire fermée de P1, avec des panoramas de K candidats (un leurre de même famille et de même "
            "complexité à la place de la forme vraie dans B), un plan des positions équilibré et deux ordres de "
            "présentation, la règle à trois issues retrouve, à la taille de la puissance, des questionneurs factices de "
            "biais connu (position, reconnaissance simulée, évitement, famille). Rien de plus : rien sur les proposeurs "
            "réels (aucun ne joue), rien sur la découverte (le bras C contient la vérité par construction), rien sur C4 "
            "(candidats extérieurs à coût apparié, phase 2 non dimensionnée), rien sur la boucle de production, rien sur "
            "une composition de proposeurs (N-058), rien sur la recherche en langue naturelle de l'article.")


# --- déroulement ------------------------------------------------------------------------------------------------------
def phase_p3(cfg, racine, p_references, taches):
    c = cfg["p3"]
    K = c["K"]

    def gen(nom, motif=None):
        taches.append(motif or nom)
        return mr.generateur(nom, racine)

    sq = mr.tirer_sonde(gen("p3/sonde-questions"), c["sonde_questions"])
    ss = mr.tirer_sonde(gen("p3/sonde-score"), c["sonde_score"])
    espace = qp.construire_espace(gen("p3/espace"), c["taille_espace_H"], sq, ss, [np.asarray(p) for p in p_references])
    if espace["A"].shape[1] != c["predicats_structurels"] or c["predicats_principaux"] != 42:
        raise Refus("grammaire des prédicats différente de celle préenregistrée")
    fams, index = pp.index_familles(espace)
    seuil = c["seuil_signature_nat"]
    mondes, leurres, ecartes = pp.tirer_mondes_avec_leurre(
        espace, fams, index, c["mondes"], gen("p3/mondes"), lambda w: gen(f"p3/leurre/{w}", "p3/leurre/<indice de la loi dans H>"), seuil,
        c["limite_lois_sans_leurre"])
    positions = pp.plan_positions(gen("p3/plan"), c["mondes"], K)
    comptes_plan = pp.exiger_plan_equilibre(positions, K)
    panoramas = []
    for i, (w, l, p) in enumerate(zip(mondes, leurres, positions)):
        remp = pp.choisir_remplisseurs(espace, w, l, fams, gen(f"p3/remplisseurs/{i}", "p3/remplisseurs/<i>"), K - 1, seuil)
        pan = pp.construire_panorama(w, l, remp, int(p), K)
        pp.exiger_panorama(pan, fams, K, espace, seuil)
        panoramas.append(pan)

    def rng_carte(spec, bras, ordre, i):
        return gen(f"p3/carte/{spec}/{bras}/{ordre}/{i}", "p3/carte/<questionneur>/<bras>/<ordre>/<i>")

    specs = tuple(c["factices_critere"]) + tuple(c["factices_rapportes"])
    banc = pp.jouer_reconnaissance(espace, fams, panoramas, specs, rng_carte, K, c["politique_refus"])
    return espace, fams, mondes, panoramas, banc, {"lois_sans_leurre_ecartees": ecartes, "comptes_plan": comptes_plan}


def lire_p3(cfg, racine, banc, taches):
    c = cfg["p3"]
    K, B = c["K"], c["tirages_bootstrap"]
    lectures, conformites, biais = {}, {}, {}
    for spec, r in banc.items():
        taches.append(f"p3/bootstrap/{spec}")
        lectures[spec] = pp.trois_issues(r["cible_C"], r["cible_B"], mr.generateur(f"p3/bootstrap/{spec}", racine), B,
                                         c["niveau"], c["delta_equivalence"], K)
        taches.append(f"p3/bootstrap-position/{spec}")
        biais[spec] = pp.biais_de_position(r["choix_C"], r["choix_B"],
                                           mr.generateur(f"p3/bootstrap-position/{spec}", racine), B,
                                           c["niveau_position"], K)
        if spec in c["factices_critere"]:
            conformites[spec] = pp.conforme(spec, lectures[spec], biais[spec])
    refus = int(sum(r["refus"] for r in banc.values()))
    gardes_ok = refus == 0
    issues_ok, positions_ok = lire_conformites(conformites)
    motifs_r4 = []
    h = lectures.get("hasard")
    if h is not None:
        if h["ecart_D"]["largeur"] == 0.0:
            motifs_r4.append("bras « choix au hasard » : intervalle de l'écart de largeur nulle")
        if h["taux_C"]["point"] == 1.0 / K and h["taux_B"]["point"] == 1.0 / K:
            motifs_r4.append("bras « choix au hasard » : taux exactement 1/K dans C et dans B (trop propre)")
    for spec in c["factices_critere"]:
        if lectures[spec]["issue"] != pp.ATTENTES_FACTICES[spec]["issue"]:
            motifs_r4.append(f"{spec} : issue contraire à l'attente ({lectures[spec]['issue']})")
    return {"verdict_propose_par_le_code": verdict_p3(gardes_ok, issues_ok, positions_ok),
            "gardes_tiennent": gardes_ok, "refus_hors_panorama": refus, "issues_conformes": issues_ok,
            "biais_de_position_conformes": positions_ok, "conformites_des_factices_du_critere": conformites,
            "lectures_trois_issues": lectures, "biais_de_position": biais,
            "rapporte_sans_decision": {s: {"issue": lectures[s]["issue"], "ecart_D": lectures[s]["ecart_D"]}
                                       for s in c["factices_rapportes"]},
            "audit_symetrie_R4": {"declenche": bool(motifs_r4), "motifs": motifs_r4}}


def recouvrement_p1(cfg, racine, espace, panoramas, banc, taches):
    """Recouvrement à T sur l'instrument de P1 (rapporté, sans décision) : bissection de P1, répondeur exact, ordre 1,
    sur les `mondes_kl` premiers mondes du plan (préfixe équilibré). Bras A (seul, carte de P1), B et C (carte de
    reconnaissance gardée tant qu'elle est compatible)."""
    c = cfg["p3"]
    n = c["mondes_kl"]
    if n % c["K"] or n > len(panoramas):
        raise Refus("mondes du recouvrement : préfixe non équilibré ou trop long")
    T, pts, k = c["questions_T"], tuple(c["points_de_carte"]), c["predicats_principaux"]
    carte_t0 = qp.medoide(espace, np.arange(len(espace["lois"])))
    taches += ["p3/kl/partie/<i>/questionneur", "p3/kl/partie/<i>/ordre"]
    parties = []
    for i in range(n):
        w = panoramas[i]["monde"]
        ordre, traits = qp.ordre_de_presentation(mr.generateur(f"p3/kl/partie/{i}/ordre", racine), k)
        q = qp.Bissection(mr.generateur(f"p3/kl/partie/{i}/questionneur", racine))
        rep = mr.Repondeur(espace["A"][w, :k], "exact")
        parties.append(qp.jouer_partie(espace, w, q, rep, T, pts, k, carte_t0, ordre, traits, c["politique_refus"]))
    sortie = {}
    for spec in c["factices_kl"]:
        r = banc[spec]
        bras = {}
        for nom in ("A", "B", "C"):
            cartes = []
            for i in range(n):
                pan = panoramas[i]
                reconnue = None if nom == "A" else pan[nom][int(r[f"choix_{nom}"][i, 0])]
                cartes.append(pp.cartes_avec_reconnaissance(espace, pan["monde"], parties[i], reconnue, pts))
            bras[nom] = cartes
        kl = {nom: np.array([x[T]["kl"] for x in bras[nom]]) for nom in bras}
        comps = {}
        for a, b in (("C", "B"), ("C", "A"), ("B", "A")):
            taches.append(f"p3/kl/bootstrap/{spec}/{a}-moins-{b}")
            comps[f"{a}_moins_{b}"] = qp.bootstrap_double(kl[a], kl[b], mr.generateur(f"p3/kl/bootstrap/{spec}/{a}-moins-{b}",
                                                                                          racine), c["tirages_bootstrap"])
        sortie[spec] = {"comparaisons_a_T": comps,
                        "kl_mediane_par_point": {nom: {str(t): float(np.median([x[t]["kl"] for x in bras[nom]]))
                                                       for t in pts} for nom in bras},
                        "kl_moyenne_par_point": {nom: {str(t): float(np.mean([x[t]["kl"] for x in bras[nom]]))
                                                       for t in pts} for nom in bras},
                        "part_reconnue_gardee_a_T": {nom: float(np.mean([x[T]["reconnue_gardee"] for x in bras[nom]]))
                                                     for nom in ("B", "C")}}
    return {"mondes": n, "ordre": 1, "questionneur_de_questions": "bissection (P1)", "par_factice": sortie}


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
        controle_code, exiger_cl, compagnon, exiger_pu = True, True, True, True
        evaluateur, e_eval_attendue = EVALUATEUR_ORGANISME, EMPREINTE_EVALUATEUR
        if a.essai or a.essais_json:
            if not (a.essai and a.essais_json):
                raise Refus("--essai et --essais-json vont ensemble")
            essais = json.loads(Path(a.essais_json).read_text(encoding="utf-8"))
            attendue = essais["preenregistrement"]
            sources = {k: tuple(v) for k, v in essais["sources"].items()}
            cfg = essais["config"]
            if empreinte_bloc_effort(cfg) == empreinte_bloc_effort(CONFIG):
                raise Refus("mode d'essai avec la configuration réelle : refus")
            controle_code = essais.get("controle_du_code", True)
            exiger_cl = essais.get("contre_lecture_exigee", True)
            compagnon = essais.get("compagnon_du_preenregistrement_exige", True)
            exiger_pu = essais.get("puissance_exigee", True)
            evaluateur, e_eval_attendue = essais["evaluateur"]
        e_prereg = l1.exiger_preenregistrement(a.preenregistrement, attendue, compagnon)
        e_bloc = exiger_bloc_effort(a.preenregistrement, cfg)
        pu = exiger_puissance(cfg) if exiger_pu else puissance(cfg)
        cl = exiger_contre_lecture(a.contre_lecture, e_prereg) if exiger_cl else {"empreinte": "non exigée (essai)"}
        e_code = l1.exiger_code_scelle(ICI, MODULES) if controle_code else {"non controle (essai)": True}
        e_code_p1 = exiger_code_p1() if controle_code else {"non controle (essai)": True}
        e_eval = l1.exiger_fichier(evaluateur, e_eval_attendue, "évaluateur de l'organisme")
        for cle, (chemin, att) in sources.items():
            l1.exiger_fichier(chemin, att, f"source {cle}")
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
    resultat = {"version": VERSION, "essai": bool(a.essai), "debut_utc": debut,
                "hors_table": "P3 est hors table : il répond aux lignes C2 et C4, restées indécidables ; écart déclaré au "
                              "préenregistrement ; cette phase 0 ne porte que sur C2 (reconnaissance)",
                "calcul_de_puissance": pu,
                "devis_refait_non_engage": pp.devis(pu["n_retenu_prudent"], cfg["p3"]["devis"]["prix_usd_par_appel"],
                                                    cfg["p3"]["devis"]["appels_par_monde_et_proposeur"],
                                                    cfg["p3"]["devis"]["reprises"]),
                "devis_variante_optimiste_non_engage": pp.devis(pu["n_optimiste_ordres_independants"],
                                                                cfg["p3"]["devis"]["prix_usd_par_appel"],
                                                                cfg["p3"]["devis"]["appels_par_monde_et_proposeur"],
                                                                cfg["p3"]["devis"]["reprises"]),
                "borne_de_ce_que_l_instrument_permet_de_revendiquer": BORNE_P3}
    try:
        journal.append(f"{e_eval}  {evaluateur}  (évaluateur de l'organisme, lecture seule, empreinte vérifiée)")
        taches.append("p3/sonde-score")
        ss = mr.tirer_sonde(mr.generateur("p3/sonde-score", racine), cfg["p3"]["sonde_score"])
        p_refs = l1.probas_organisme(l1.lois_de_reference_v67(boucle), *ss, evaluateur)
        espace, fams, mondes, panoramas, banc, info = phase_p3(cfg, racine, p_refs, taches)
        resultat["p3"] = lire_p3(cfg, racine, banc, taches)
        resultat["p3"]["informations"] = {**info, "lois_retirees_par_la_garde_de_disjonction": int(espace["retirees_disjonction"]),
                                          "mondes_indices_dans_H": mondes,
                                          "familles_des_mondes": sorted({str(fams[w]) for w in mondes})}
        resultat["p3"]["recouvrement_sur_l_instrument_P1_rapporte"] = recouvrement_p1(cfg, racine, espace, panoramas,
                                                                                      banc, taches)
    except REFUS as e:
        resultat["p3"] = {"arret": str(e), "verdict_propose_par_le_code": verdict_p3(False, False, False)}
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
    fichiers = {"sortie-phase0-p3-v1.json": resultat, "manifeste-phase0-p3-v1.json": manifeste}
    for nom, contenu in fichiers.items():
        (sortie / nom).write_text(json.dumps(contenu, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    (sortie / "journal-fichiers-ouverts-phase0-p3-v1.txt").write_text("\n".join(journal) + "\n", encoding="utf-8")
    for nom in list(fichiers) + ["journal-fichiers-ouverts-phase0-p3-v1.txt"]:
        p = sortie / nom
        (sortie / (nom + ".sha256")).write_text(f"{l1.sha256_fichier(p)}  {nom}\n", encoding="utf-8")
    print(json.dumps({"p3": resultat["p3"].get("verdict_propose_par_le_code")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
