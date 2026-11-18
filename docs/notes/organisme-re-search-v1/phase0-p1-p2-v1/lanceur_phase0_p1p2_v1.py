#!/usr/bin/env python3
"""Lanceur de la phase 0 de P1 et P2 (organisme d'idéation, propositions Re-Search) — v1 (modèle I, auteur unique).
Fichier neuf (R12).

Applique le préenregistrement scellé `preenregistrement-phase0-p1-p2-v1.md` (même dossier). Refuse de partir (code 2,
rien écrit) si :
- l'empreinte du préenregistrement n'est pas `EMPREINTE_PREENREGISTREMENT`, ou son compagnon `.sha256` manque ou diffère ;
- le préenregistrement ne porte pas l'empreinte du bloc « effort et échantillonnage gelés » que le lanceur recalcule
  (conditions de la mère R-3186, P1 a) ;
- la contre-lecture (`--contre-lecture`) manque, n'est pas scellée, ou ne cite pas l'empreinte du préenregistrement
  (conditions de la mère R-3181 : préenregistré et contre-lu avant toute exécution) ;
- un module de code (ce lanceur compris) n'a pas son compagnon `.sha256` ou ne lui est pas conforme ;
- une source n'a pas l'empreinte attendue ; le dossier de sortie existe déjà (R12).
Écrit dans le dossier de sortie : `sortie-phase0-p1-p2-v1.json` (mesures, critères gelés appliqués par le code, lecture
proposée), `manifeste-phase0-p1-p2-v1.json` (configuration et son empreinte, bloc d'effort gelé et son empreinte, graines,
versions, empreintes du code, du préenregistrement, de la contre-lecture et des sources, commit),
`journal-fichiers-ouverts-phase0-p1-p2-v1.txt` (chaque fichier ouvert, avec son empreinte) ; chacun scellé (`.sha256`).
La lecture proposée par le code n'est pas le prononcé : l'issue est lue par un lecteur neuf qui applique les critères
gelés (R13).

Aucun appel réseau, aucun appel de modèle, aucune dépense. Graines : SeedSequence(20261118), une graine fille par tâche (R9).

Usage :
  python3 -B lanceur_phase0_p1p2_v1.py --sortie DOSSIER_NEUF --contre-lecture RAPPORT_SCELLE
Mode d'essai (essais R5 seulement) : `--essai --essais-json F.json`, où F.json remplace les empreintes attendues
(clé « preenregistrement »), les chemins et empreintes des sources (« sources »), la configuration (« config »),
l'évaluateur, et dit si le code et la contre-lecture sont contrôlés ; la sortie porte alors "essai": true et rien n'y est
déclaré vérifié contre les empreintes réelles.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import platform
import runpy
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))

import numpy as np  # noqa: E402

import mesure_forme_p2_v1 as p2  # noqa: E402
import mondes_reponses_p1p2_v1 as mr  # noqa: E402
import questionneurs_p1_v1 as qp  # noqa: E402

VERSION = "lanceur-phase0-p1p2-v1"
NOM_PREENREGISTREMENT = "preenregistrement-phase0-p1-p2-v1.md"
EMPREINTE_PREENREGISTREMENT = "8c8240fa4b7def4ed0daa396c9c0e879307b4042f8e96ebd9223e78fee4713c0"
MODULES = ("mondes_reponses_p1p2_v1.py", "questionneurs_p1_v1.py", "mesure_forme_p2_v1.py", "lanceur_phase0_p1p2_v1.py")
EVALUATEUR_ORGANISME = "/home/user/ideation-organism/orchestrator/pole/evaluateur_lois_v62.py"

SOURCES = {
    "v67": ("/home/user/ideation-organism/resultats/course-v67/poste-local-v1/boucle-reelle-v66.json",
            "21bc75f4d81825695b30b2b32f21feaa91322293f6c2c3161a28dc179ec6df71"),
    "goodhart_v3": ("/tmp/claude-0/-home-user/a4afe5e0-34e3-5a46-aa07-762507893585/scratchpad/goodhart/donnees/"
                    "attaque-goodhart-v3-a1v3-troisieme-v1/sortie-attaque-goodhart-v3/attaque-goodhart-v3.json",
                    "e0b3145bf3b7f619c648652e2fb89dd715cb272ce447ed4ff4b56de5cb6f9505"),
    "goodhart_v5": ("/tmp/claude-0/-home-user/a4afe5e0-34e3-5a46-aa07-762507893585/scratchpad/goodhart/donnees/"
                    "attaque-goodhart-v4-a1v4-v1/sortie-attaque-goodhart-v5/attaque-goodhart-v5.json",
                    "cff69d8653b974ff2ca2a9c61dac1613e7ed3427feebbe76bc647297b21750bf"),
}

# Bras du banc principal (répondeur exact, variante empirique). « nom#2 » : copie (graines du questionneur et de l'ordre
# différentes : A/A) ; « nom#ordre » : même graine de questionneur que « nom », seule la graine de l'ordre de présentation
# change (effet de l'ordre, conditions de la mère R-3186, P1 b).
BRAS_PRINCIPAL = ("aleatoire", "aleatoire#2", "aleatoire#ordre", "bissection", "bissection#2", "bissection#ordre",
                  "repeteur", "repeteur#ordre", "disperseur", "oracle")
BRAS_INVERSE = ("aleatoire", "bissection")
BRAS_HASARD = ("aleatoire", "bissection")
BRAS_STRUCTURELLE = ("aleatoire", "bissection", "repeteur", "disperseur")
# Famille A/A (C-P1-2) : trois comparaisons, intervalles « contient 0 » corrigés de Bonferroni sur 3.
FAMILLE_AA = (("aa_aleatoire", "aleatoire#2", "aleatoire"),
              ("ordre_aleatoire", "aleatoire#ordre", "aleatoire"),
              ("ordre_bissection", "bissection#ordre", "bissection"))

CONFIG = {
    "racine_graines": 20261118,
    "p1": {"mondes": 200, "taille_espace_H": 65536, "questions_T": 16, "points_de_carte": [0, 4, 8, 16],
           "sonde_questions": 2048, "sonde_score": 256, "predicats_principaux": 42, "predicats_structurels": 51,
           "taux_inversion_artefact": 0.10, "tirages_bootstrap": 10_000, "fraction_largeur_aa": 0.5,
           "seuil_fuite": 0.05, "seuil_audit_trop_facile": 0.95, "mondes_information_phase1": 8,
           "politique_refus": "arret", "bras_principal": list(BRAS_PRINCIPAL), "bras_inverse_10": list(BRAS_INVERSE),
           "bras_hasard": list(BRAS_HASARD), "bras_structurelle": list(BRAS_STRUCTURELLE)},
    "p2": {"tirages_reference": 10_000, "tirages_reference_m4": 1_000, "seuil": 0.25,
           "quota_principal": p2.QUOTA_PRINCIPAL, "quota_plage_sensibilite": list(p2.QUOTA_PLAGE_SENSIBILITE),
           "observe_attendu_analyse": {"cartes": 23, "repetent": 9},
           "m4_attendu_analyse": {"goodhart_v3": {"retour": 0.414583, "temoin": 0.32043},
                                  "goodhart_v5": {"retour": 0.359626, "temoin": 0.165945}}},
}


class Refus(Exception):
    pass


def sha256_fichier(chemin) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def canon(o) -> bytes:
    return json.dumps(o, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


# --- effort et échantillonnage gelés (conditions de la mère R-3186, P1 a) ----------------------------------------------
def bloc_effort(cfg) -> dict:
    """Budget de questions, nombre de mondes, tailles, tirages, bras et règle des refus : ce que le manifeste gèle. Toute
    différence avec le bloc dont le préenregistrement porte l'empreinte est un refus de partir."""
    c, d = cfg["p1"], cfg["p2"]
    return {"racine_graines": cfg["racine_graines"],
            "p1": {k: c[k] for k in ("mondes", "taille_espace_H", "questions_T", "points_de_carte", "sonde_questions",
                                     "sonde_score", "predicats_principaux", "predicats_structurels",
                                     "taux_inversion_artefact", "tirages_bootstrap", "politique_refus", "bras_principal",
                                     "bras_inverse_10", "bras_hasard", "bras_structurelle")},
            "p2": {k: d[k] for k in ("tirages_reference", "tirages_reference_m4", "quota_principal",
                                     "quota_plage_sensibilite")},
            "proposeurs_reels": "aucun en phase 0 (questionneurs factices) ; réglages des proposeurs de la phase 1 "
                                "(effort de raisonnement, température, plafond de jetons, nombre de parties) à geler au "
                                "manifeste de la phase 1, avant tout appel"}


def empreinte_bloc_effort(cfg) -> str:
    return hashlib.sha256(canon(bloc_effort(cfg))).hexdigest()


# --- gardes -------------------------------------------------------------------------------------------------------------
def exiger_preenregistrement(chemin, attendue, exiger_compagnon=False) -> str:
    if not Path(chemin).is_file():
        raise Refus(f"préenregistrement absent : {chemin}")
    e = sha256_fichier(chemin)
    if e != attendue:
        raise Refus(f"empreinte du préenregistrement {e} ≠ attendue {attendue} : refus de partir")
    if exiger_compagnon:
        c = Path(str(chemin) + ".sha256")
        if not c.is_file():
            raise Refus("préenregistrement non scellé (compagnon .sha256 absent) : refus de partir")
        lu = c.read_text(encoding="utf-8").split()
        if not lu or lu[0] != e:
            raise Refus("compagnon du préenregistrement non conforme : refus de partir")
    return e


def exiger_bloc_effort(chemin_prereg, cfg) -> str:
    e = empreinte_bloc_effort(cfg)
    if e not in Path(chemin_prereg).read_text(encoding="utf-8"):
        raise Refus(f"le préenregistrement ne porte pas l'empreinte {e} du bloc « effort et échantillonnage gelés » : "
                    "configuration différente de celle préenregistrée, refus de partir")
    return e


def exiger_contre_lecture(chemin, e_prereg) -> str:
    """Contre-lecture faite avant toute exécution : fichier présent, scellé (compagnon conforme), et qui cite l'empreinte
    du préenregistrement qu'elle a relu."""
    if not chemin or not Path(chemin).is_file():
        raise Refus("contre-lecture absente : préenregistré mais pas contre-lu, refus de partir (R-3181)")
    e = sha256_fichier(chemin)
    c = Path(str(chemin) + ".sha256")
    if not c.is_file() or c.read_text(encoding="utf-8").split()[:1] != [e]:
        raise Refus("contre-lecture non scellée ou compagnon non conforme : refus de partir")
    if e_prereg not in Path(chemin).read_text(encoding="utf-8"):
        raise Refus("la contre-lecture ne cite pas l'empreinte du préenregistrement lancé : refus de partir")
    return e


def exiger_code_scelle(dossier, modules=MODULES) -> dict:
    sortie = {}
    for m in modules:
        p = Path(dossier) / m
        c = Path(str(p) + ".sha256")
        if not c.is_file():
            raise Refus(f"compagnon absent pour {m} : code non scellé, refus de partir")
        lignes = [l for l in c.read_text(encoding="utf-8").splitlines() if l.strip()]
        if len(lignes) != 1 or "  " not in lignes[0]:
            raise Refus(f"compagnon illisible pour {m}")
        attendue, nom = lignes[0].split("  ", 1)
        if nom != m:
            raise Refus(f"compagnon de {m} nomme {nom}")
        e = sha256_fichier(p)
        if e != attendue:
            raise Refus(f"{m} : empreinte {e} ≠ scellée {attendue} : refus de partir")
        sortie[m] = e
    return sortie


def charger_source(cle, chemin, attendue, journal):
    e = sha256_fichier(chemin)
    if e != attendue:
        raise Refus(f"source {cle} ({chemin}) : empreinte {e} ≠ attendue {attendue}")
    journal.append(f"{e}  {chemin}  (source {cle})")
    with open(chemin, encoding="utf-8") as f:
        return json.load(f), e


def exiger_reproduction_m2(observee, attendu):
    if observee["cartes"] != attendu["cartes"] or observee["repetent"] != attendu["repetent"]:
        raise Refus(f"mesure M2 non reproduite : {observee['repetent']}/{observee['cartes']} au lieu de "
                    f"{attendu['repetent']}/{attendu['cartes']} (analyse de nos journaux) : arrêt de P2")


def dossier_neuf(chemin):
    p = Path(chemin)
    if p.exists():
        raise Refus(f"dossier de sortie déjà présent : {p} (R12 : on n'écrase jamais)")
    return p


# --- règles de décision gelées (fonctions pures, essayées à part) -------------------------------------------------------
def tient_ordre(comp) -> bool:
    """Un écart d'ordre tient si les DEUX statistiques (médianes, moyennes) ont un point et une borne basse à 95 %
    strictement positifs."""
    return all(comp[s]["point"] > 0 and comp[s]["ic95"][0] > 0 for s in ("medianes", "moyennes"))


def tient_aa(comp, ecarts, fraction) -> dict:
    """Comparaison A/A (ou d'ordre de présentation) : pour CHAQUE statistique, l'intervalle corrigé de Bonferroni contient
    0 ET la largeur de l'intervalle à 95 % est strictement inférieure à `fraction` × l'écart entre les questionneurs
    bornes (médiane ou moyenne de l'aléatoire moins celle de la bissection, mêmes mondes) ; un écart nul ou négatif fait
    échouer le critère de largeur."""
    detail = {}
    for s in ("medianes", "moyennes"):
        lo, hi = comp[s]["ic_corrige"]
        contient = lo <= 0.0 <= hi
        etroit = ecarts[s] > 0 and comp[s]["largeur95"] < fraction * ecarts[s]
        detail[s] = {"contient_0": contient, "largeur95": comp[s]["largeur95"],
                     "largeur_max": fraction * ecarts[s] if ecarts[s] > 0 else 0.0, "etroit": etroit}
    return {"tient": all(d["contient_0"] and d["etroit"] for d in detail.values()), "detail": detail}


def tient_degradation(comp) -> bool:
    """Inversion de 10 % (artefact R5) : la dégradation doit être vue par la différence des MOYENNES (borne basse > 0).
    La médiane est rapportée sans décider : avec une masse de divergences nulles au-delà de la moitié, elle ne la voit pas."""
    return comp["moyennes"]["ic95"][0] > 0


def tient_disparition(comp) -> bool:
    """Répondeur au hasard (artefact R5) : l'avantage de la bissection doit disparaître pour les DEUX statistiques
    (borne basse à 95 % ≤ 0) ; si l'une des deux le voit encore, la garde échoue (fuite possible)."""
    return all(comp[s]["ic95"][0] <= 0 for s in ("medianes", "moyennes"))


def verdict_p1(gardes_ok, ordre_ok, aa_ok, presentation_ok) -> str:
    """Table gelée de P1. Les gardes priment : un instrument dont un artefact passe ne mesure rien de sûr."""
    if not gardes_ok:
        return "garde défaillante : arrêt, audit du code, aucune phase 1"
    if not ordre_ok:
        return "instrument non discriminant (ordre) : arrêt, aucune phase 1"
    if not aa_ok:
        return "instrument non discriminant (A/A) : arrêt, aucune phase 1"
    if not presentation_ok:
        return "instrument sensible à l'ordre de présentation : arrêt, aucune phase 1"
    return "instrument discriminant : une phase 1 peut être proposée à Lazar, sur devis (non engagée)"


def decision_p2(med_r1, med_r1_entiers, med_r2, med_hs, part_hs_obs, p_ref_r1, seuil, n_cartes) -> dict:
    """Table gelée de P2 (forme principale, toutes cartes) ; lectures et réserves écrites par le code."""
    ferme = med_r1 > seuil
    decision = ("C3 se referme (ne change pas) : la médiane de la référence R1 dépasse un quart (effet de la grammaire)"
                if ferme else
                "C3 n'est pas refermée par la référence : la médiane de la référence R1 ne dépasse pas un quart")
    lectures = []
    if not ferme:
        lectures.append("part observée au-dessus du quantile 95 % de la référence R1" if p_ref_r1 < 0.05
                        else "part observée non distincte de la référence R1 (au moins 5 % des tirages l'atteignent) : réserve")
        if part_hs_obs <= seuil:
            lectures.append("A-1 : hors softmax, la part observée ne dépasse pas un quart : dans la boucle de production, "
                            "le seuil n'est franchi que par les softmax")
    if (med_hs > seuil) != ferme:
        lectures.append("A-1 : la décision diffère sans les softmax (référence HS sur les emplacements non softmax) : "
                        "réserve, la conclusion dépend des cartes softmax")
    if (med_r2 > seuil) != ferme:
        lectures.append("P-8 : la décision change avec la loi de tirage des types (R2) : réserve, la conclusion dépend de "
                        "la loi de tirage")
    if (med_r1_entiers > seuil) != ferme:
        lectures.append("A-3 : la décision change quand les entiers sont gardés : réserve")
    audit = (5 / n_cartes) - 1e-12 <= med_r1 <= (7 / n_cartes) + 1e-12 if n_cartes == 23 else \
        abs(med_r1 - seuil) <= 1.0 / n_cartes + 1e-12
    return {"decision": decision, "ferme": ferme, "lectures": lectures, "audit_symetrie_R4_declenche": bool(audit)}


# --- P1 -----------------------------------------------------------------------------------------------------------------
def lois_de_reference_v67(boucle):
    r = boucle["releve"]
    return [p["loi"] for p in r["plantees"]] + [c["loi"] for c in r["cartes"]]


def probas_organisme(lois, Z, G, chemin_evaluateur=EVALUATEUR_ORGANISME):
    """Probabilités des lois de référence par l'évaluateur de l'organisme (lecture seule, runpy)."""
    ev = runpy.run_path(chemin_evaluateur)
    sortie = []
    for loi in lois:
        try:  # loi de type hors gabarit (l'évaluateur lève ValueError) : arrêt de P1, motif écrit
            sortie.append(np.array([ev["proba"](loi, {"z": [float(Z[n, 0]), float(Z[n, 1])], "g": int(G[n])})
                                    for n in range(Z.shape[0])]))
        except (ValueError, KeyError, TypeError) as e:
            raise Refus(f"loi de référence hors gabarit : {e}") from e
    return sortie


def phase_p1(cfg, racine, p_references, taches):
    c = cfg["p1"]
    gen = lambda nom: mr.generateur(nom, racine)  # noqa: E731
    taches += ["p1/sonde-questions", "p1/sonde-score", "p1/espace", "p1/mondes"]
    sq = mr.tirer_sonde(gen("p1/sonde-questions"), c["sonde_questions"])
    ss = mr.tirer_sonde(gen("p1/sonde-score"), c["sonde_score"])
    refs = [np.asarray(p) for p in p_references]
    espace = qp.construire_espace(gen("p1/espace"), c["taille_espace_H"], sq, ss, refs)
    if espace["A"].shape[1] != c["predicats_structurels"] or c["predicats_principaux"] != 42:
        raise Refus("grammaire des prédicats différente de celle préenregistrée")
    mondes = qp.tirer_mondes(gen("p1/mondes"), espace, c["mondes"])

    def rng_partie(prefixe):
        return lambda nom, i, role: gen(f"p1/partie/{prefixe}/{nom}/{i}/{role}")

    T, points, pol = c["questions_T"], tuple(c["points_de_carte"]), c["politique_refus"]
    k = c["predicats_principaux"]
    bras = {
        "principal": qp.jouer_banc(espace, mondes, tuple(c["bras_principal"]), rng_partie("principal"), "exact", 0.0,
                                   T, points, k, pol),
        "inverse_10": qp.jouer_banc(espace, mondes, tuple(c["bras_inverse_10"]), rng_partie("inverse_10"), "inverse",
                                    c["taux_inversion_artefact"], T, points, k, pol),
        "hasard": qp.jouer_banc(espace, mondes, tuple(c["bras_hasard"]), rng_partie("hasard"), "hasard", 0.0, T,
                                points, k, pol),
        "structurelle": qp.jouer_banc(espace, mondes, tuple(c["bras_structurelle"]), rng_partie("structurelle"),
                                      "exact", 0.0, T, points, None, pol),
    }
    taches.append("p1/partie/<bras>/<questionneur>/<indice du monde>/<role> (règle ; rôles : questionneur, ordre, "
                  "repondeur)")
    return espace, mondes, bras


def lire_p1(cfg, racine, espace, mondes, bras, taches):
    """Applique les critères gelés de P1 (section « Critères de lecture gelés » du préenregistrement)."""
    c = cfg["p1"]
    B = c["tirages_bootstrap"]
    T = c["questions_T"]
    pts = c["points_de_carte"]
    if 0 not in pts or T not in pts or len(pts) < 3:
        raise Refus("points de carte incohérents avec T (0, un point intermédiaire et T exigés)")
    t_prec = pts[1]

    def boot(nom, a, b, k=1):
        taches.append(f"p1/bootstrap/{nom}")
        return qp.bootstrap_double(a, b, mr.generateur(f"p1/bootstrap/{nom}", racine), B, k)

    pr = bras["principal"]
    kl = {n: qp.colonne(pr[n], T) for n in pr}
    d_al_bis = boot("aleatoire-moins-bissection", kl["aleatoire"], kl["bissection"])
    d_rep_al = boot("repeteur-moins-aleatoire", kl["repeteur"], kl["aleatoire"])
    ordre_ok = tient_ordre(d_al_bis) and tient_ordre(d_rep_al)
    ecarts = {s: d_al_bis[s]["point"] for s in ("medianes", "moyennes")}
    famille = {}
    for nom, a, b in FAMILLE_AA:
        comp = boot(nom, kl[a], kl[b], len(FAMILLE_AA))
        famille[nom] = {**comp, **tient_aa(comp, ecarts, c["fraction_largeur_aa"])}
    aa_ok = famille["aa_aleatoire"]["tient"]
    presentation_ok = famille["ordre_aleatoire"]["tient"] and famille["ordre_bissection"]["tient"]
    bruit = boot("bissection-inverse10-moins-exacte", qp.colonne(bras["inverse_10"]["bissection"], T), kl["bissection"])
    bruit_ok = tient_degradation(bruit)
    hasard = boot("hasard-aleatoire-moins-bissection", qp.colonne(bras["hasard"]["aleatoire"], T),
                  qp.colonne(bras["hasard"]["bissection"], T))
    hasard_ok = tient_disparition(hasard)
    fuite = {n: qp.taux_fuite([p["cartes"][0]["exacte"] for p in pr[n]]) for n in pr}
    oracle_signale = fuite["oracle"] > c["seuil_fuite"]
    classes_signales = [n for n in pr if n != "oracle" and fuite[n] > c["seuil_fuite"]]
    oracle_nul = all(float(np.max(qp.colonne(pr["oracle"], t))) == 0.0 for t in pts)
    refus = int(sum(p["refus_hors_grammaire"] for parties in bras.values() for ps in parties.values() for p in ps))
    gardes_ok = bruit_ok and hasard_ok and oracle_signale and not classes_signales and oracle_nul and refus == 0
    verdict = verdict_p1(gardes_ok, ordre_ok, aa_ok, presentation_ok)
    exacte_T = {n: float(np.mean([p["cartes"][T]["exacte"] for p in pr[n]])) for n in pr}
    # R4 : même audit pour un résultat trop beau ou trop net dans un sens comme dans l'autre
    motifs_r4 = []
    if exacte_T["aleatoire"] >= c["seuil_audit_trop_facile"]:
        motifs_r4.append("le questionneur aléatoire recouvre exactement le monde dans au moins 95 % des parties")
    for nom, comp in (("aleatoire-bissection", d_al_bis), ("repeteur-aleatoire", d_rep_al)):
        for s in ("medianes", "moyennes"):
            if comp[s]["largeur95"] == 0.0:
                motifs_r4.append(f"intervalle d'ordre {nom} ({s}) de largeur nulle")
            if comp[s]["ic95"][1] < 0:
                motifs_r4.append(f"ordre {nom} ({s}) inversé avec un intervalle éloigné de 0 (négatif trop net)")
    # information pour la phase 1 (aucune décision) : dispersion de l'écart A/A sur 8 mondes, rapportée à l'écart
    taches.append("p1/information/aa-sur-8-mondes")
    rng8 = mr.generateur("p1/information/aa-sur-8-mondes", racine)
    idx = rng8.integers(0, len(mondes), (B, c["mondes_information_phase1"]))
    d8 = np.median(kl["aleatoire#2"][idx], axis=1) - np.median(kl["aleatoire"][idx], axis=1)
    q8 = np.quantile(d8, [0.025, 0.975], method="inverted_cdf")
    desc = {}
    for nom_bras, parties in bras.items():
        desc[nom_bras] = {}
        for n, ps in parties.items():
            k0, kp, kT = (qp.colonne(ps, t) for t in (0, t_prec, T))
            desc[nom_bras][n] = {
                "kl_mediane_par_point": {str(t): float(np.median(qp.colonne(ps, t))) for t in pts},
                "kl_moyenne_par_point": {str(t): float(np.mean(qp.colonne(ps, t))) for t in pts},
                "part_carte_exacte_par_point": {str(t): float(np.mean(qp.colonne(ps, t, "exacte"))) for t in pts},
                "part_forme_egale_par_point": {str(t): float(np.mean(qp.colonne(ps, t, "forme_egale"))) for t in pts},
                "rendement_precoce_par_question_mediane": float(np.median((k0 - kp) / t_prec)),
                "rendement_tardif_par_question_mediane": float(np.median((kp - kT) / (T - t_prec))),
                "information_par_question_bits_moyenne": float(np.nanmean([np.nanmean(p["information_par_question_bits"]) for p in ps])),
                "part_meme_direction_moyenne": float(np.nanmean([p["part_meme_direction_que_la_precedente"] for p in ps])),
                "directions_ouvertes_moyenne": float(np.mean([p["directions_ouvertes"] for p in ps])),
                "questions_reposees": int(sum(p["questions_reposees"] for p in ps)),
                "refus_hors_grammaire": int(sum(p["refus_hors_grammaire"] for p in ps)),
                "questions_perdues": int(sum(p["questions_perdues"] for p in ps)),
                "temps_processeur_moyen_s": float(np.mean([p["temps_processeur_s"] for p in ps])),
                "cout_usd": 0.0,
            }
    carte_zero = {n: {"kl_mediane": float(np.median(qp.colonne(pr[n], 0))), "kl_moyenne": float(np.mean(qp.colonne(pr[n], 0))),
                      "part_exacte": fuite[n]} for n in pr}
    s = bras["structurelle"]
    ks = {n: qp.colonne(s[n], T) for n in s}
    return {
        "verdict_propose_par_le_code": verdict,
        "criteres": {
            "C-P1-1_ordre": {"aleatoire_moins_bissection": d_al_bis, "repeteur_moins_aleatoire": d_rep_al,
                             "tient": ordre_ok},
            "C-P1-2_famille_aa": {"ecarts_entre_bornes": ecarts, "fraction": c["fraction_largeur_aa"],
                                  "comparaisons": famille, "aa_tient": aa_ok, "ordre_de_presentation_tient": presentation_ok},
            "C-P1-3_inversion_10_pour_cent": {**bruit, "statistique_decisive": "moyennes", "tient": bruit_ok},
            "C-P1-4_repondeur_au_hasard": {**hasard, "statistique_decisive": "les deux", "tient": hasard_ok},
            "C-P1-5_fuite": {"taux_par_questionneur": fuite, "oracle_signale": oracle_signale,
                             "questionneurs_non_oracle_signales": classes_signales, "oracle_divergence_nulle": oracle_nul},
            "C-P1-6_refus": {"refus_hors_grammaire": refus, "tient": refus == 0},
            "gardes_tiennent": gardes_ok,
        },
        "audit_symetrie_R4": {"declenche": bool(motifs_r4), "motifs": motifs_r4},
        "carte_a_zero_question_par_questionneur": carte_zero,
        "part_carte_exacte_a_T": exacte_T,
        "rapporte_sans_decision": {
            "aa_bissection": boot("aa-bissection", kl["bissection#2"], kl["bissection"]),
            "ordre_repeteur": boot("ordre-repeteur", kl["repeteur#ordre"], kl["repeteur"]),
            "disperseur_moins_aleatoire": boot("disperseur-moins-aleatoire", kl["disperseur"], kl["aleatoire"]),
            "structurelle_aleatoire_moins_bissection": boot("structurelle-aleatoire-moins-bissection", ks["aleatoire"], ks["bissection"]),
            "structurelle_repeteur_moins_aleatoire": boot("structurelle-repeteur-moins-aleatoire", ks["repeteur"], ks["aleatoire"]),
            "inversion_mediane_rapportee": bruit["medianes"],
            "aa_sur_8_mondes_quantiles_2_5_97_5": [float(q8[0]), float(q8[1])],
            "aa_sur_8_mondes_largeur_sur_ecart_medianes": float((q8[1] - q8[0]) / ecarts["medianes"]) if ecarts["medianes"] > 0 else None,
            "lois_retirees_par_la_garde_de_disjonction": int(espace["retirees_disjonction"]),
            "mondes_indices_dans_H": mondes,
        },
        "descriptions": desc,
        "borne_de_ce_que_l_instrument_permet_de_revendiquer": BORNE_P1,
    }


BORNE_P1 = ("Au mieux : sur des mondes tirés dans la grammaire fermée écrite au préenregistrement, avec les prédicats "
            "écrits et la règle de carte commune (médoïde), la divergence finale ordonne des questionneurs factices de "
            "qualité connue, à la précision mesurée. Rien sur les proposeurs réels, rien sur la boucle de production, "
            "rien sur une composition de proposeurs (N-058), rien hors de cette grammaire.")


# --- P2 -----------------------------------------------------------------------------------------------------------------
def phase_p2(cfg, racine, boucle, goodhart, taches):
    c = cfg["p2"]
    cartes = boucle["releve"]["cartes"]
    obs = p2.mesure_observee(cartes)
    exiger_reproduction_m2(obs, c["observe_attendu_analyse"])
    refs = {}
    for variante in ("R1", "R2", "HS", "SEQ"):
        taches.append(f"p2/reference/{variante}")
        parts, parts_e = p2.reference_m2(cartes, mr.generateur(f"p2/reference/{variante}", racine), c["tirages_reference"], variante)
        o = obs["hors_softmax"] if variante == "HS" else obs
        refs[variante] = {"forme_principale": p2.resume_reference(parts, o["part"]),
                          "entiers_gardes": p2.resume_reference(parts_e, o["part_entiers_gardes"])}
    d = decision_p2(refs["R1"]["forme_principale"]["mediane"], refs["R1"]["entiers_gardes"]["mediane"],
                    refs["R2"]["forme_principale"]["mediane"], refs["HS"]["forme_principale"]["mediane"],
                    obs["hors_softmax"]["part"], refs["R1"]["forme_principale"]["part_des_tirages_au_moins_egale_a_l_observee"],
                    c["seuil"], obs["cartes"])
    # quota (iii), rejeu hors ligne, sans vérité, sur la plage gelée ; aucun champ d'oracle lu
    if c["quota_principal"] != p2.QUOTA_PRINCIPAL or tuple(c["quota_plage_sensibilite"]) != p2.QUOTA_PLAGE_SENSIBILITE:
        raise Refus("quota ou plage différents de ceux du préenregistrement")
    quota = {str(q): p2.rejeu_quota(cartes, q) for q in p2.QUOTA_PLAGE_SENSIBILITE}
    # Goodhart, description seulement
    desc = {}
    for cle, sortie in goodhart.items():
        suites = sortie["suites"]
        if any(s.get("interrompue") for s in suites):
            raise Refus(f"{cle} : suite interrompue présente (non lue)")
        desc[cle] = {}
        for b in sorted({s["condition"] for s in suites}):
            sb = [s for s in suites if s["condition"] == b]
            part, rep, props = p2.part_m4(sb)
            hs = [{"tentatives": [t for t in s["tentatives"] if t.get("loi") is not None and t["loi"].get("type") != "softmax"]}
                  for s in sb]
            part_hs, _, props_hs = p2.part_m4(hs)
            taches.append(f"p2/m4/{cle}/{b}")
            ref = p2.reference_m4(sb, mr.generateur(f"p2/m4/{cle}/{b}", racine), c["tirages_reference_m4"])
            attendu = c["m4_attendu_analyse"].get(cle, {}).get(b)
            desc[cle][b] = {"propositions": props, "repetent": rep, "part": part,
                            "reproduit_l_analyse": (attendu is not None and abs(round(part, 6) - attendu) < 1e-9),
                            "hors_softmax": {"propositions": props_hs, "part": part_hs},
                            "reference_R1_memes_longueurs": p2.resume_reference(ref, part)}
    return {"observe": obs, "references": refs, "decision_proposee_par_le_code": d["decision"],
            "lectures": d["lectures"], "audit_symetrie_R4": {"declenche": d["audit_symetrie_R4_declenche"]},
            "rejeu_quota_sans_verite": quota,
            "aucune_nouveaute": p2.MENTION_AUCUNE_NOUVEAUTE,
            "goodhart_description_seulement": desc}


# --- principal ----------------------------------------------------------------------------------------------------------
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
        controle_code, exiger_cl, evaluateur, compagnon = True, True, EVALUATEUR_ORGANISME, True
        if a.essai or a.essais_json:
            if not (a.essai and a.essais_json):
                raise Refus("--essai et --essais-json vont ensemble")
            essais = json.loads(Path(a.essais_json).read_text(encoding="utf-8"))
            attendue = essais["preenregistrement"]
            sources = {k: tuple(v) for k, v in essais["sources"].items()}
            cfg = essais["config"]
            controle_code = essais.get("controle_du_code", True)
            exiger_cl = essais.get("contre_lecture_exigee", True)
            compagnon = essais.get("compagnon_du_preenregistrement_exige", True)
            evaluateur = essais.get("evaluateur", EVALUATEUR_ORGANISME)
        e_prereg = exiger_preenregistrement(a.preenregistrement, attendue, compagnon)
        e_bloc = exiger_bloc_effort(a.preenregistrement, cfg)
        e_cl = exiger_contre_lecture(a.contre_lecture, e_prereg) if exiger_cl else "non exigée (essai)"
        e_code = exiger_code_scelle(ICI) if controle_code else {"non controle (essai)": True}
        sortie = dossier_neuf(a.sortie)
        journal = [f"{e_prereg}  {Path(a.preenregistrement).resolve()}  (préenregistrement)"]
        if exiger_cl:
            journal.append(f"{e_cl}  {Path(a.contre_lecture).resolve()}  (contre-lecture)")
        empreintes_sources = {}
        boucle, empreintes_sources["v67"] = charger_source("v67", *sources["v67"], journal)
        goodhart = {}
        for cle in ("goodhart_v3", "goodhart_v5"):
            if cle in sources:
                goodhart[cle], empreintes_sources[cle] = charger_source(cle, *sources[cle], journal)
    except Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    racine = cfg["racine_graines"]
    taches = []
    t0 = time.time()
    resultat = {"version": VERSION, "essai": bool(a.essai), "debut_utc": debut}
    try:
        journal.append(f"{sha256_fichier(evaluateur)}  {evaluateur}  (évaluateur de l'organisme, lecture seule)")
        taches.append("p1/sonde-score")
        ss = mr.tirer_sonde(mr.generateur("p1/sonde-score", racine), cfg["p1"]["sonde_score"])
        p_refs = probas_organisme(lois_de_reference_v67(boucle), *ss, evaluateur)
        espace, mondes, bras = phase_p1(cfg, racine, p_refs, taches)
        resultat["p1"] = lire_p1(cfg, racine, espace, mondes, bras, taches)
    except (Refus, mr.Refus) as e:
        resultat["p1"] = {"arret": str(e)}
    try:
        resultat["p2"] = phase_p2(cfg, racine, boucle, goodhart, taches)
    except (Refus, mr.Refus) as e:
        resultat["p2"] = {"arret": str(e)}
    resultat["fin_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    resultat["duree_s"] = round(time.time() - t0, 1)
    try:
        commit = subprocess.run(["git", "-C", str(ICI), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    except OSError:
        commit = "inconnu"
    manifeste = {
        "version": VERSION, "essai": bool(a.essai), "configuration": cfg,
        "empreinte_configuration": hashlib.sha256(canon(cfg)).hexdigest(),
        "effort_et_echantillonnage_geles": {"bloc": bloc_effort(cfg), "empreinte": e_bloc,
                                            "porte_par_le_preenregistrement": True},
        "graines": {"racine": racine,
                    "regle": "SeedSequence(racine, spawn_key=(int.from_bytes(sha256(nom de tâche)[:8], 'big'),))",
                    "taches": sorted(set(taches))},
        "versions": {"python": platform.python_version(), "numpy": np.__version__, "plateforme": platform.platform(),
                     "modules": {"mondes": mr.VERSION, "questionneurs": qp.VERSION, "mesure_forme": p2.VERSION,
                                 "lanceur": VERSION}},
        "empreintes": {"preenregistrement": e_prereg, "contre_lecture": e_cl, "code": e_code,
                       "sources": empreintes_sources},
        "commit": commit, "debut_utc": debut, "fin_utc": resultat["fin_utc"],
    }
    sortie.mkdir(parents=True)
    fichiers = {"sortie-phase0-p1-p2-v1.json": resultat, "manifeste-phase0-p1-p2-v1.json": manifeste}
    for nom, contenu in fichiers.items():
        (sortie / nom).write_text(json.dumps(contenu, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    (sortie / "journal-fichiers-ouverts-phase0-p1-p2-v1.txt").write_text("\n".join(journal) + "\n", encoding="utf-8")
    for nom in list(fichiers) + ["journal-fichiers-ouverts-phase0-p1-p2-v1.txt"]:
        p = sortie / nom
        (sortie / (nom + ".sha256")).write_text(f"{sha256_fichier(p)}  {nom}\n", encoding="utf-8")
    print(json.dumps({"p1": resultat.get("p1", {}).get("verdict_propose_par_le_code", resultat.get("p1")),
                      "p2": resultat.get("p2", {}).get("decision_proposee_par_le_code", resultat.get("p2"))}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
