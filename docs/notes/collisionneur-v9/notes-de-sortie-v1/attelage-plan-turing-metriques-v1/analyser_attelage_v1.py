#!/usr/bin/env python3
"""Analyse deterministe du collisionneur sur l'attelage du Plan Turing (GO-2026-11-24-39).

Produit : metriques-attelage-v1.json
Regles couvertes : Protocole X v2 / v2.1 (regles 1 en 2.1, 3, 4, 6, 7).
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path
from statistics import NormalDist

ROOT = Path(
    r"C:\Users\lciri\.gemini\antigravity-cli\brain\54d22d59-e9ed-4f2e-9191-bbb2bfc9cf24\scratch\note-attelage"
)
SOURCES = ROOT / "sources"
RUN_REL = "runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153"
RUN_DIR = SOURCES / "run" / RUN_REL
MAIN_DIR = SOURCES / "main"
OUT_JSON = ROOT / "metriques-attelage-v1.json"

NORM = NormalDist(0.0, 1.0)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def beta_reg_inc_binom_tail(k: int, n: int, p: float) -> float:
    """Calcule P(Binomiale(n, p) <= k) de maniere exacte en virgule flottante stable."""
    if p <= 0.0:
        return 1.0
    if p >= 1.0:
        return 1.0 if k >= n else 0.0
    log_q = math.log1p(-p)
    log_p = math.log(p)
    total = 0.0
    for i in range(k + 1):
        log_term = (
            math.lgamma(n + 1)
            - math.lgamma(i + 1)
            - math.lgamma(n - i + 1)
            + i * log_p
            + (n - i) * log_q
        )
        total += math.exp(log_term)
    return min(1.0, total)


def clopper_pearson_upper(k: int, n: int, alpha: float) -> float:
    """Borne superieure unilaterale exacte de Clopper-Pearson au niveau 1 - alpha."""
    if k >= n:
        return 1.0
    if k == 0:
        return 1.0 - (alpha ** (1.0 / n))
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if beta_reg_inc_binom_tail(k, n, mid) > alpha:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def cohen_kappa(a: int, b: int, c: int, d: int) -> dict:
    """Table 2x2 : a=OUI/OUI, b=OUI/NON, c=NON/OUI, d=NON/NON."""
    n = a + b + c + d
    po = (a + d) / n
    p_l1_oui = (a + b) / n
    p_l2_oui = (a + c) / n
    p_l1_non = (c + d) / n
    p_l2_non = (b + d) / n
    pe = p_l1_oui * p_l2_oui + p_l1_non * p_l2_non
    kappa = (po - pe) / (1.0 - pe) if pe < 1.0 else 1.0
    # Erreur type asymptotique de Fleiss-Cohen-Everitt (1969) sous hypothese generale
    # Approchee par la formule standard de Cohen (1960) / Fleiss pour 2x2
    se_approx = math.sqrt(po * (1.0 - po) / (n * ((1.0 - pe) ** 2))) if pe < 1.0 else 0.0
    # Ecart-type sous H0 (kappa = 0)
    se_h0 = math.sqrt(pe / (n * (1.0 - pe))) if pe < 1.0 else 0.0
    return {
        "n": n,
        "table_2x2": {
            "opus_oui_astra_oui": a,
            "opus_oui_astra_non": b,
            "opus_non_astra_oui": c,
            "opus_non_astra_non": d,
        },
        "accord_observe_po": round(po, 4),
        "accord_hasard_pe": round(pe, 4),
        "kappa_cohen": round(kappa, 4),
        "se_approx": round(se_approx, 4),
        "ic95_approx": [
            round(max(-1.0, kappa - 1.96 * se_approx), 4),
            round(min(1.0, kappa + 1.96 * se_approx), 4),
        ],
        "se_sous_h0": round(se_h0, 4),
        "pabak": round(2.0 * po - 1.0, 4),
    }


def verifier_empreintes() -> dict:
    files_to_hash = []
    for p in sorted(MAIN_DIR.rglob("*")):
        if p.is_file():
            rel = str(p.relative_to(MAIN_DIR)).replace("\\", "/")
            files_to_hash.append(("main", rel, p))
    for p in sorted(RUN_DIR.rglob("*")):
        if p.is_file() and not p.name.endswith(".sha256"):
            rel = f"{RUN_REL}/" + str(p.relative_to(RUN_DIR)).replace("\\", "/")
            files_to_hash.append(("831a7e38", rel, p))
    ref_dir = SOURCES / "ref-style"
    if ref_dir.exists():
        for p in sorted(ref_dir.glob("*")):
            if p.is_file():
                files_to_hash.append(("831a7e38", p.name, p))

    hashes = []
    verifs_sha = []
    all_ok = True
    for ref, rel, p in files_to_hash:
        h = sha256_file(p)
        comp = p.with_name(p.name + ".sha256")
        statut = "sans_compagnon"
        if comp.exists():
            txt = comp.read_text(encoding="utf-8", errors="replace").strip()
            expected = txt.split()[0].lower() if txt else ""
            ok = h == expected
            if not ok:
                all_ok = False
            statut = "OK" if ok else f"ECART (attendu {expected})"
            verifs_sha.append({"fichier": rel, "ok": ok, "sha256": h})
        hashes.append(
            {
                "reference_git": ref,
                "chemin_depot": rel,
                "octets": p.stat().st_size,
                "sha256": h,
                "verification_compagnon": statut,
            }
        )

    # Verification egalite faits.md == question-etage3.md
    h_faits = sha256_file(RUN_DIR / "faits.md")
    h_q = sha256_file(RUN_DIR / "question-etage3.md")
    h_dossier_comp = (RUN_DIR / "lecture-double" / "dossier-aveugle-v1.md.sha256").read_text(
        encoding="utf-8"
    ).strip().split()[0]

    return {
        "tous_compagnons_valides": all_ok,
        "nombre_compagnons_verifies": len(verifs_sha),
        "faits_identique_question": h_faits == h_q,
        "sha256_faits_et_question": h_faits,
        "sha256_dossier_aveugle_declare": h_dossier_comp,
        "fichiers": hashes,
    }


def analyser_couts() -> dict:
    especes = json.loads((RUN_DIR / "especes.json").read_text(encoding="utf-8"))
    fournisseur_map = {
        "fable": "Anthropic",
        "opus": "Anthropic",
        "astra": "OpenAI",
        "carbon": "Google",
        "neon": "Google",
    }
    lettre_map = {v["espece"]: k for k, v in especes["lettres"].items()}

    lignes = [
        json.loads(line)
        for line in (RUN_DIR / "journal.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    appels = [x for x in lignes if "cellule" in x]

    par_cellule = []
    par_espece: dict[str, dict] = {}
    par_fournisseur: dict[str, dict] = {}
    par_tour: dict[str, float] = {"T1": 0.0, "T2": 0.0, "T3": 0.0}

    total_compte = 0.0
    total_pire = 0.0
    for a in appels:
        esp = a["espece"]
        fourn = fournisseur_map[esp]
        cout = float(a["cout_usd"])
        pire = float(a["cout_pire_usd"])
        cell = a["cellule"]
        tour = cell.split("-")[1]  # T1, T2, T3
        par_tour[tour] += cout
        total_compte += cout
        total_pire += pire

        u = a["usage"]
        entree = int(u.get("entree", 0))
        sortie = int(u.get("sortie", 0))
        reflexion = int(u.get("reflexion", 0))
        par_cellule.append(
            {
                "cellule": cell,
                "lettre": lettre_map[esp],
                "espece": esp,
                "modele_servi": a["modele_servi"],
                "fournisseur": fourn,
                "statut": a["statut"],
                "essai": a["essai"],
                "entree_jetons": entree,
                "sortie_jetons": sortie,
                "reflexion_jetons": reflexion,
                "caracteres": int(a["caracteres"]),
                "cout_usd": round(cout, 4),
                "cout_pire_usd": round(pire, 4),
            }
        )

        pe = par_espece.setdefault(
            esp,
            {
                "lettre": lettre_map[esp],
                "modele": a["modele_servi"],
                "fournisseur": fourn,
                "appels": 0,
                "entree_jetons": 0,
                "sortie_jetons": 0,
                "cout_usd": 0.0,
                "cout_pire_usd": 0.0,
            },
        )
        pe["appels"] += 1
        pe["entree_jetons"] += entree
        pe["sortie_jetons"] += sortie
        pe["cout_usd"] += cout
        pe["cout_pire_usd"] += pire

        pf = par_fournisseur.setdefault(
            fourn,
            {"appels": 0, "cout_usd": 0.0, "cout_pire_usd": 0.0},
        )
        pf["appels"] += 1
        pf["cout_usd"] += cout
        pf["cout_pire_usd"] += pire

    for d in par_espece.values():
        d["cout_usd"] = round(d["cout_usd"], 4)
        d["cout_pire_usd"] = round(d["cout_pire_usd"], 4)
    for d in par_fournisseur.values():
        d["cout_usd"] = round(d["cout_usd"], 4)
        d["cout_pire_usd"] = round(d["cout_pire_usd"], 4)

    # Lecture double : lecteur Astra
    j_astra_lines = (
        (RUN_DIR / "lecture-double" / "journal-lecteur-astra-2.txt")
        .read_text(encoding="utf-8")
        .splitlines()
    )
    meta_astra = json.loads(j_astra_lines[1])
    cout_lecteur_astra = float(meta_astra["cout_usd"])

    cout_anthropic = par_fournisseur["Anthropic"]["cout_usd"]
    cout_openai_course = par_fournisseur["OpenAI"]["cout_usd"]
    cout_google = par_fournisseur["Google"]["cout_usd"]

    paye_compte_course = cout_anthropic + cout_openai_course
    paye_compte_avec_lecture_astra = paye_compte_course + cout_lecteur_astra
    total_compte_avec_lecture_astra = total_compte + cout_lecteur_astra

    plafond_go_paye = 25.0
    ligne_comptee = 40.0
    devis_compte = 37.74
    devis_paye_pire = 14.71

    return {
        "nombre_cellules_ok": sum(1 for c in par_cellule if c["statut"] == "OK"),
        "nombre_cellules_total": len(par_cellule),
        "collisionneur_etage3": {
            "cout_compte_total_usd": round(total_compte, 4),
            "cout_compte_arrondi_2dec_usd": round(total_compte, 2),
            "somme_couts_pire_cellules_usd": round(total_pire, 4),
            "par_tour_usd": {k: round(v, 4) for k, v in par_tour.items()},
            "par_espece": par_espece,
            "par_fournisseur": par_fournisseur,
            "paye_compte_anthropic_plus_openai_usd": round(paye_compte_course, 4),
            "google_compte_sous_reserve_gratuite_usd": round(cout_google, 4),
            "detail_cellules": par_cellule,
        },
        "lecture_double": {
            "lecteur_astra_modele": meta_astra["modele_servi"],
            "lecteur_astra_entree_jetons": meta_astra["usage"]["entree"],
            "lecteur_astra_sortie_jetons": meta_astra["usage"]["sortie"],
            "lecteur_astra_cout_usd": round(cout_lecteur_astra, 4),
            "lecteur_opus_note": "Exécute dans la session Claude Code (quota d'abonnement), aucun appel API facturé séparément ; coût API marginal = 0,00 USD.",
        },
        "synthese_dossier": {
            "total_compte_course_seule_usd": round(total_compte, 4),
            "total_compte_avec_lecture_astra_usd": round(total_compte_avec_lecture_astra, 4),
            "paye_compte_course_seule_usd": round(paye_compte_course, 4),
            "paye_compte_avec_lecture_astra_usd": round(paye_compte_avec_lecture_astra, 4),
            "google_sous_reserve_gratuite_usd": round(cout_google, 4),
            "statut_cle_google": "GEMINI_API_KEY_FREE : gratuité supposée au devis (0 USD réel), non établie sur relevé bancaire ; montant compté Google rapporté séparément (5,03 USD).",
            "plafond_go_2026_11_24_39_paye_usd": plafond_go_paye,
            "ligne_comptee_ouverte_usd": ligne_comptee,
            "devis_initial_compte_usd": devis_compte,
            "devis_initial_paye_pire_usd": devis_paye_pire,
            "marge_sous_plafond_go_course_seule_usd": round(plafond_go_paye - paye_compte_course, 4),
            "marge_sous_plafond_go_avec_lecture_astra_usd": round(
                plafond_go_paye - paye_compte_avec_lecture_astra, 4
            ),
            "marge_sous_plafond_go_si_google_facture_usd": round(
                plafond_go_paye - total_compte_avec_lecture_astra, 4
            ),
            "conforme_plafond_go": total_compte_avec_lecture_astra <= plafond_go_paye,
        },
    }


def analyser_alignement_et_fournisseurs() -> dict:
    # Alignement canonique des 31 unites distinctes examinees par les deux lecteurs aveugles
    # (lecture-opus-v1.md : 15 retenues P1..P15, 10 non retenues N1..N10 ;
    #  lecture-astra-v1.md : 14 retenues P1..P14, 8 non retenues N1..N8).
    # Pour chaque proposition, on indique :
    # - decision_opus (True=retenue, False=non retenue)
    # - decision_astra (True=retenue, False=non retenue)
    # - explicite_deux_lecteurs (True si explicitement listee en P ou N chez les deux)
    # - soutiens_t3 : lettres A..E qui adoptent/defendent la proposition au tour III.3
    unites = [
        # --- 11 ACCORDS OUI / OUI ---
        {
            "id": "U01",
            "intitule": "Étroitesse définie contre un panel de référence nommé et disjoint des bras concurrents (ou à budget de sonde découplé du duel)",
            "ref_opus": "P1",
            "ref_astra": "P5",
            "decision_opus": True,
            "decision_astra": True,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": ["A", "B", "C", "D", "E"],
            "note": "Consensus unanime au tour III.3 sur la borne de handicap (B T2) ; remède divergent entre panel disjoint (B, C) et budget court b0 << B (A, D, E).",
        },
        {
            "id": "U02",
            "intitule": "Étroitesse certifiée par borne supérieure binomiale unilatérale sur tirages disjoints, étiquette binaire censurée et coût de sensibilité calculé avant tirage",
            "ref_opus": "P2",
            "ref_astra": "P1",
            "decision_opus": True,
            "decision_astra": True,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": ["A", "B", "C", "D", "E"],
            "note": "Clopper-Pearson unilatéral et disjonction des tirages adoptés par les cinq modèles au tour III.3.",
        },
        {
            "id": "U03",
            "intitule": "Nomination scellée choisie avant ouverture du coffre (nombre fixe ou unique), séparation atteinte/livraison et contrôle du volume",
            "ref_opus": "P3",
            "ref_astra": "P8",
            "decision_opus": True,
            "decision_astra": True,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": ["A", "B", "C", "D", "E"],
            "note": "Nomination scellée avant coffre adoptée par tous (k=3 chez A, k fixe chez B, nomination unique + journal chez C, unique chez D et E).",
        },
        {
            "id": "U04",
            "intitule": "Profondeur mesurée comme gain aval d'un résolveur mécanique figé contre résolveur nu sur buts gelés, avec idée vraie inerte et double vérification (deux jeux de buts, deux résolveurs)",
            "ref_opus": "P4",
            "ref_astra": "P4",
            "decision_opus": True,
            "decision_astra": True,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": ["A", "B", "C", "D", "E"],
            "note": "A, B, C en résolution mécanique directe ; D et E sur compression / réduction de pas de prouveur Lean étalonnée sur loi nulle.",
        },
        {
            "id": "U05",
            "intitule": "Canonicalisation des assertions éprouvée des deux côtés (fausses fusions et fausses scissions), y compris sur obscurcissements produits hors règles du canoniseur",
            "ref_opus": "P6",
            "ref_astra": "P2 (volet audit bilatéral)",
            "decision_opus": True,
            "decision_astra": True,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": ["A", "B", "C", "D", "E"],
            "note": "Contrôle bilatéral adopté par tous les modèles au tour III.3.",
        },
        {
            "id": "U06",
            "intitule": "Comparaison principale par intersection-union (minimum des écarts moyens appariés par monde contre chaque référence), dimensionnée contre la marge utile non nulle",
            "ref_opus": "P7",
            "ref_astra": "P10",
            "decision_opus": True,
            "decision_astra": True,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": ["A", "B", "C", "D", "E"],
            "note": "Abandon unanime de l'enveloppe par problème et correction du dimensionnement contre la marge (160 à 935 problèmes illustratifs).",
        },
        {
            "id": "U07",
            "intitule": "Attribution par témoins multiples sur viviers gelés et lots frais : message neutre du même dossier, silence à budget réalloué, critique permutée réservée à la nuisance, hétérogénéité contre homogène",
            "ref_opus": "P9",
            "ref_astra": "P13",
            "decision_opus": True,
            "decision_astra": True,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": ["A", "B", "C", "D", "E"],
            "note": "Tous les modèles au tour III.3 remplacent la critique hors sujet comme unique témoin par un ensemble de témoins distincts.",
        },
        {
            "id": "U08",
            "intitule": "Intégrité de la mesure sous retour séparée de l'utilité du retour : trois jeux (renvoyé, scellé, vierge), différence d'écarts, témoin de fuite délibérée ; étroitesse jamais renvoyée",
            "ref_opus": "P10",
            "ref_astra": "P11",
            "decision_opus": True,
            "decision_astra": True,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": ["A", "B", "C", "D", "E"],
            "note": "Accord unanime sur le secret absolu de l'étroitesse et la séparation entre utilité du retour et corruption de mesure.",
        },
        {
            "id": "U09",
            "intitule": "Plafond de fausses alertes dérivé de la prévalence visée (identité de Bayes) et contrôlé strate par strate ; aucun juge de langage dans la quantité primaire",
            "ref_opus": "P11 + P12 (noyau)",
            "ref_astra": "P7",
            "decision_opus": True,
            "decision_astra": True,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": ["A", "B", "C", "D", "E"],
            "note": "Identité de Bayes adoptée par A, B, C, E (D emploie Begg-Greenes et un plan 2x2 pour le juge) ; exclusion du juge du primaire unanime.",
        },
        {
            "id": "U10",
            "intitule": "Contrôle positif d'instrument sur micromonde à quatre quadrants avec deux lois utiles dont une seule signalée au constructeur et assertion vraie rare sur observable inutilisée",
            "ref_opus": "P13",
            "ref_astra": "P3",
            "decision_opus": True,
            "decision_astra": True,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": ["A", "B", "C"],
            "note": "Porté explicitement par A (T2/T3), B (T3 E1') et C (T3) ; D et E valident les quatre quadrants sans l'exigence de seconde loi non documentée.",
        },
        {
            "id": "U11",
            "intitule": "Choix des régions testé comme rendement net sur familles neuves (exclues du duel), descripteurs calculés sur l'énoncé public seul et sonde disjointe, coût de prospection imputé",
            "ref_opus": "P15",
            "ref_astra": "P12",
            "decision_opus": True,
            "decision_astra": True,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": ["A", "B", "C", "D", "E"],
            "note": "Accord unanime sur la correction de circularité et l'imputation du coût de prospection ; confiance basse chez tous (0,25 à 0,65).",
        },
        # --- 4 DÉSACCORDS OUI OPUS / NON ASTRA ---
        {
            "id": "U12",
            "intitule": "Score de profondeur par longueur de description minimale signé et ramené par observation, sans troncature par régime, constantes figées sur l'apprentissage",
            "ref_opus": "P5",
            "ref_astra": "absent des retenues (ancienne forme en N4)",
            "decision_opus": True,
            "decision_astra": False,
            "explicite_deux_lecteurs": False,
            "soutiens_t3": ["D", "E"],
            "note": "Défendu par D (T3) et E (T3, lambda=1 nat) ; A, B et C utilisent un solveur mécanique de conséquences plutôt qu'une compression explicite.",
        },
        {
            "id": "U13",
            "intitule": "Contrôle négatif actif « chasseur d'étroitesse » (CN-2) en complément du bras de divergence triviale (CN-1)",
            "ref_opus": "P8",
            "ref_astra": "absent des retenues (seul le bras divergent figure dans P5)",
            "decision_opus": True,
            "decision_astra": False,
            "explicite_deux_lecteurs": False,
            "soutiens_t3": ["A", "B", "C", "D", "E"],
            "note": "Proposé par B (T2), adopté par les cinq modèles au tour III.3 ; retenu explicitement par Opus, omis de la liste finale d'Astra.",
        },
        {
            "id": "U14",
            "intitule": "Module optionnel de juge de langage hors primaire : plan factoriel 2x2 vérité x style et correction assistée uniquement face à un oracle externe objectif",
            "ref_opus": "P12 (volet optionnel)",
            "ref_astra": "absent des retenues (limites en N8)",
            "decision_opus": True,
            "decision_astra": False,
            "explicite_deux_lecteurs": False,
            "soutiens_t3": ["D", "E"],
            "note": "A, B et C excluent le juge ou préfèrent un audit humain aveugle ; D (Exp. VI) et E (E2b optionnel) gardent ce module conditionnel.",
        },
        {
            "id": "U15",
            "intitule": "Épreuve dédiée de dépendance de l'étroitesse au codage (traductions non conservatrices de taille entre formalismes) et au changement de référence au seuil",
            "ref_opus": "P14",
            "ref_astra": "partiel (retrait de référence dans P5, sans recodage)",
            "decision_opus": True,
            "decision_astra": False,
            "explicite_deux_lecteurs": False,
            "soutiens_t3": ["A", "B", "D", "E"],
            "note": "A (E2'), B (E2'), D (Exp. I) et E (E2a) en font une épreuve de tête contre le cadrage ; Astra ne retient pas le volet recodage non conservatif.",
        },
        # --- 4 DÉSACCORDS NON OPUS / OUI ASTRA ---
        {
            "id": "U16",
            "intitule": "Identité d'assertion par clé partielle extensionnelle (observable cible, portée déclarée, vecteur de réponses) livrée au résolveur par interface commune",
            "ref_opus": "N7 (explicitement écartée)",
            "ref_astra": "P2",
            "decision_opus": False,
            "decision_astra": True,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": ["C"],
            "note": "Proposée par C (T3) ; Opus la rejette provisoirement en N7 faute d'épreuve chiffrée, Astra la retient en P2.",
        },
        {
            "id": "U17",
            "intitule": "Étalonnage de la décision complète par campagnes A/A indépendantes (rejouant calibration, sélection et analyse) et par injection en sortie finale après gel de la rareté",
            "ref_opus": "absent des retenues (A/A cité en épreuve de P7)",
            "ref_astra": "P6",
            "decision_opus": False,
            "decision_astra": True,
            "explicite_deux_lecteurs": False,
            "soutiens_t3": ["A", "B", "E"],
            "note": "Portée par A (E3a/E3b), B (E4' A/A complet) et E (E1 A/A complet) ; Astra en fait une proposition retenue autonome (P6).",
        },
        {
            "id": "U18",
            "intitule": "Panel de concurrents réalisables gelés sur développement à comptabilité matérielle complète (préremplissage, décodage, outils, essais abandonnés) et double régime budgétaire",
            "ref_opus": "absent des retenues (rejet de l'ancien en N8)",
            "ref_astra": "P9",
            "decision_opus": False,
            "decision_astra": True,
            "explicite_deux_lecteurs": False,
            "soutiens_t3": ["A", "B", "C", "D", "E"],
            "note": "Accord de fond des cinq modèles au tour III.3 sur la comptabilité complète et la séparation des régimes ; seul Astra l'élève en proposition autonome.",
        },
        {
            "id": "U19",
            "intitule": "Réplication dans un second domaine (preuve formelle, certificat, dépendances autorisées et aide à un prouveur sur buts réservés) sans promettre le transfert",
            "ref_opus": "absent des retenues",
            "ref_astra": "P14",
            "decision_opus": False,
            "decision_astra": True,
            "explicite_deux_lecteurs": False,
            "soutiens_t3": ["A", "B", "C", "D", "E"],
            "note": "Présente chez les cinq modèles (Lean 4) mais avec portée réduite à la non-contradiction ; retenue comme proposition dédiée par Astra seul.",
        },
        # --- 12 ACCORDS NON / NON ---
        {
            "id": "U20",
            "intitule": "Enveloppe des lignes de base prise problème par problème (max par problème)",
            "ref_opus": "N1",
            "ref_astra": "N3",
            "decision_opus": False,
            "decision_astra": False,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": [],
            "note": "Tuée par l'inégalité de Jensen E[max] >= max E ; abandonnée par B et E au tour III.3.",
        },
        {
            "id": "U21",
            "intitule": "Score primaire égal au maximum de profondeur sur tout le vivier, aire sous courbe découverte-budget et seuils en écarts-types estimés",
            "ref_opus": "N2",
            "ref_astra": "N2",
            "decision_opus": False,
            "decision_astra": False,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": [],
            "note": "Fait du coffre un sélecteur gratuit et récompense le volume en sqrt(2 ln m) ; retirée par E au tour III.3.",
        },
        {
            "id": "U22",
            "intitule": "Score de compression tronqué à zéro régime par régime en nats extensifs",
            "ref_opus": "N3",
            "ref_astra": "N4",
            "decision_opus": False,
            "decision_astra": False,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": [],
            "note": "Crédite les lois nulles bruitées (E[(G)+] = E|G|/2) et efface les réfutations ; remplacé par D au tour III.3.",
        },
        {
            "id": "U23",
            "intitule": "Étroitesse comme scalaire validée par corrélation de rang (Spearman/Kendall) entre références",
            "ref_opus": "N4",
            "ref_astra": "N5",
            "decision_opus": False,
            "decision_astra": False,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": [],
            "note": "Dominée par les ex æquo censurés et ne garantit pas l'accord au seuil ; révisée par A, B, D et E au tour III.3.",
        },
        {
            "id": "U24",
            "intitule": "Sélecteurs de régions nourris par la vérité retenue (déceptivité) ou par les résidus de la référence qui définit l'étroitesse",
            "ref_opus": "N5",
            "ref_astra": "écartée dans P12",
            "decision_opus": False,
            "decision_astra": False,
            "explicite_deux_lecteurs": False,
            "soutiens_t3": [],
            "note": "Fuite d'oracle (A T1) et circularité (D T1) ; abandonnés par leurs auteurs au tour III.3.",
        },
        {
            "id": "U25",
            "intitule": "Critique tirée d'un autre problème comme unique témoin de l'apport de la critique",
            "ref_opus": "N6",
            "ref_astra": "N6",
            "decision_opus": False,
            "decision_astra": False,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": [],
            "note": "Un placebo hors sujet peut distraire et fabriquer un avantage illusoire ; restreinte au rôle de diagnostic de nuisance.",
        },
        {
            "id": "U26",
            "intitule": "Identité d'idée par égalité extensionnelle totale sur tout le domaine avec toute règle fausse inéligible (C T1)",
            "ref_opus": "N7 (partie T1)",
            "ref_astra": "écartée (remplacée en P2 par portée partielle)",
            "decision_opus": False,
            "decision_astra": False,
            "explicite_deux_lecteurs": False,
            "soutiens_t3": [],
            "note": "Écrase les classes éligibles à une seule fonction vraie par monde ; abandonnée par C au tour III.3.",
        },
        {
            "id": "U27",
            "intitule": "Égalisation simultanée de toutes les composantes du budget ou plafond identique d'appels au vérificateur pour tous les bras",
            "ref_opus": "N8",
            "ref_astra": "écartée dans P9",
            "decision_opus": False,
            "decision_astra": False,
            "explicite_deux_lecteurs": False,
            "soutiens_t3": [],
            "note": "Physiquement impossible entre processeur et processeur graphique, bride l'énumérateur par construction.",
        },
        {
            "id": "U28",
            "intitule": "Borne du biais d'un juge par accord de style seul ou par inférence assistée sur audit d'experts humains",
            "ref_opus": "N9",
            "ref_astra": "N8",
            "decision_opus": False,
            "decision_astra": False,
            "explicite_deux_lecteurs": True,
            "soutiens_t3": [],
            "note": "Ne borne pas un biais commun entre juge et experts ni les faussetés plausibles à style constant.",
        },
        {
            "id": "U29",
            "intitule": "Arrêt du programme entier sur une absence de significativité en petit pilote ou futilité sans plancher de paires discordantes",
            "ref_opus": "N10",
            "ref_astra": "écartée dans P10",
            "decision_opus": False,
            "decision_astra": False,
            "explicite_deux_lecteurs": False,
            "soutiens_t3": [],
            "note": "Confond résultat non concluant et réfutation ; corrigé par D et E au tour III.3.",
        },
        {
            "id": "U30",
            "intitule": "Rareté infinie après zéro occurrence par estimateur ponctuel (-log p chapeau)",
            "ref_opus": "écartée dans P2",
            "ref_astra": "N1",
            "decision_opus": False,
            "decision_astra": False,
            "explicite_deux_lecteurs": False,
            "soutiens_t3": [],
            "note": "Non défini sur l'événement dominant (zéro occurrence) ; retiré par B et E au tour III.3.",
        },
        {
            "id": "U31",
            "intitule": "Rétrodiction à coupure temporelle comme arbitre du rappel contre la découverte",
            "ref_opus": "absente des retenues",
            "ref_astra": "N7",
            "decision_opus": False,
            "decision_astra": False,
            "explicite_deux_lecteurs": False,
            "soutiens_t3": [],
            "note": "La présence en corpus, la date et le renommage ne séparent pas exposition, difficulté et déduction ; portée réduite par B et E au tour III.3.",
        },
    ]

    # Table 2x2 principale (toutes les 31 unites canoniques)
    a = sum(1 for u in unites if u["decision_opus"] and u["decision_astra"])
    b = sum(1 for u in unites if u["decision_opus"] and not u["decision_astra"])
    c = sum(1 for u in unites if not u["decision_opus"] and u["decision_astra"])
    d = sum(1 for u in unites if not u["decision_opus"] and not u["decision_astra"])
    kappa_principal = cohen_kappa(a, b, c, d)

    # Sensibilite 1 : uniquement les unites explicitement listees en P ou N chez les deux lecteurs
    exp_u = [u for u in unites if u["explicite_deux_lecteurs"]]
    a1 = sum(1 for u in exp_u if u["decision_opus"] and u["decision_astra"])
    b1 = sum(1 for u in exp_u if u["decision_opus"] and not u["decision_astra"])
    c1 = sum(1 for u in exp_u if not u["decision_opus"] and u["decision_astra"])
    d1 = sum(1 for u in exp_u if not u["decision_opus"] and not u["decision_astra"])
    kappa_explicites = cohen_kappa(a1, b1, c1, d1)

    # Sensibilite 2 : si l'on considere U13 (CN-2) comme rattache a U01/Astra P5 et U15 (recodage)
    # comme rattache a Astra P5 (interpretation large des recoupements) : +2 en OUI/OUI, -2 en OUI/NON
    kappa_large = cohen_kappa(a + 2, b - 2, c, d)

    # Regle 6 : Comptes d'accord par fournisseur (A+B = Anthropic 1 voix, C = OpenAI 1 voix, D+E = Google 1 voix)
    fournisseur_lettre = {
        "A": "Anthropic",
        "B": "Anthropic",
        "C": "OpenAI",
        "D": "Google",
        "E": "Google",
    }
    comptes_fournisseurs = []
    for u in unites:
        if u["decision_opus"] or u["decision_astra"]:
            soutiens = u["soutiens_t3"]
            fournisseurs = sorted({fournisseur_lettre[x] for x in soutiens})
            comptes_fournisseurs.append(
                {
                    "id": u["id"],
                    "intitule": u["intitule"],
                    "decision_opus": u["decision_opus"],
                    "decision_astra": u["decision_astra"],
                    "accord_lecteurs": (
                        "accord_oui"
                        if u["decision_opus"] and u["decision_astra"]
                        else "desaccord_opus_seul"
                        if u["decision_opus"]
                        else "desaccord_astra_seul"
                    ),
                    "compte_brut_modeles": f"{len(soutiens)}/5",
                    "lettres_t3": soutiens,
                    "compte_fournisseurs": f"{len(fournisseurs)}/3",
                    "fournisseurs_t3": fournisseurs,
                }
            )

    return {
        "convention_fournisseurs_regle_6": {
            "Anthropic": ["A (Claude Fable 5.2)", "B (Claude Opus 5.5)"],
            "OpenAI": ["C (GPT-6.2 Astra)"],
            "Google": ["D (Gemini 4 Carbon)", "E (Gemini 4 Neon)"],
        },
        "total_unites_canoniques": len(unites),
        "kappa_principal_31_unites": kappa_principal,
        "kappa_sensibilite_explicites_deux_lecteurs": kappa_explicites,
        "kappa_sensibilite_recoupement_large": kappa_large,
        "unites": unites,
        "comptes_par_fournisseur_propositions_retenues_au_moins_un_lecteur": comptes_fournisseurs,
    }


def analyser_statuts_verifie() -> dict:
    """Regle 4 : comptage des mentions VERIFIE / verifie et RAPPORTE / rapporte dans les 15 cellules."""
    especes = json.loads((RUN_DIR / "especes.json").read_text(encoding="utf-8"))
    lettres = ["A", "B", "C", "D", "E"]
    tours = [
        ("T1", "E3-T1-conception"),
        ("T2", "E3-T2-critique-croisee"),
        ("T3", "E3-T3-reponse"),
    ]

    # Patterns : on distingue les etiquettes de statut (majuscules VERIFIE / RAPPORTE)
    # et les occurrences en minuscules (verifie / verifiee / verifiees / verifies).
    re_verifie_maj = re.compile(r"\bVÉRIFIÉ[ES]?\b")
    re_verifie_any = re.compile(r"\bvérifié(?:e|es|s)?\b", re.IGNORECASE)
    re_rapporte_maj = re.compile(r"\bRAPPORTÉ[ES]?\b")
    re_non_verifie = re.compile(r"\bnon vérifié(?:e|es|s)?\b|\bà vérifier\b", re.IGNORECASE)

    par_cellule = []
    par_modele = {}

    for l in lettres:
        esp = especes["lettres"][l]["espece"]
        mid = especes["lettres"][l]["id"]
        tot_vmaj = 0
        tot_vany = 0
        tot_rmaj = 0
        tot_nonv = 0
        extraits_vmaj = []
        for tcode, prefix in tours:
            p = RUN_DIR / "cellules" / f"{prefix}-{l}.md"
            txt = p.read_text(encoding="utf-8")
            vmaj = len(re_verifie_maj.findall(txt))
            vany = len(re_verifie_any.findall(txt))
            rmaj = len(re_rapporte_maj.findall(txt))
            nonv = len(re_non_verifie.findall(txt))
            tot_vmaj += vmaj
            tot_vany += vany
            tot_rmaj += rmaj
            tot_nonv += nonv

            lignes_vmaj = []
            for idx, line in enumerate(txt.splitlines(), 1):
                if re_verifie_maj.search(line):
                    lignes_vmaj.append({"ligne": idx, "extrait": line.strip()[:180]})
            if lignes_vmaj:
                extraits_vmaj.append({"tour": tcode, "occurrences": lignes_vmaj})

            par_cellule.append(
                {
                    "cellule": f"{prefix}-{l}",
                    "lettre": l,
                    "espece": esp,
                    "tour": tcode,
                    "verifie_majuscules": vmaj,
                    "verifie_toutes_casses": vany,
                    "rapporte_majuscules": rmaj,
                    "mentions_a_verifier_ou_non_verifie": nonv,
                }
            )

        par_modele[l] = {
            "lettre": l,
            "espece": esp,
            "modele": mid,
            "verifie_majuscules_total": tot_vmaj,
            "verifie_toutes_casses_total": tot_vany,
            "rapporte_majuscules_total": tot_rmaj,
            "mentions_a_verifier_ou_non_verifie_total": tot_nonv,
            "details_occurrences_verifie_maj": extraits_vmaj,
        }

    # Audit des etiquettes VERIFIE abusives relevees par confrontation a faits.md (qui ne contient aucun fait empirique)
    # et par examen de chaque occurrence VÉRIFIÉ en majuscules :
    audit_statuts = {
        "faits_servis_resume": "faits.md est bit pour bit identique a question-etage3.md (414 mots) : aucun fait empirique, aucun resultat d'essai, aucune citation verifiee sur PDF.",
        "anomalies_statut_par_modele": {
            "A": {
                "verifie_majuscules_t1_t2_t3": [1, 3, 3],
                "etiquettes_verifie_propres_abusives_relevees": 0,
                "commentaire": "Aucune etiquette VÉRIFIÉ posee a tort sur ses propres enonces (les 7 occurrences sur T1-T3 sont des declarations explicites d'absence de fait verifie ou des reprises du statut pose par C, D et E).",
            },
            "B": {
                "verifie_majuscules_t1_t2_t3": [1, 3, 1],
                "etiquettes_verifie_propres_abusives_relevees": 0,
                "commentaire": "Aucune etiquette VÉRIFIÉ posee a tort (les 5 occurrences sur T1-T3 sont des constats d'absence de fait verifie ou des signalements d'usage abusif chez C et D).",
            },
            "C": {
                "verifie_majuscules_t1_t2_t3": [4, 9, 2],
                "etiquettes_verifie_propres_abusives_relevees": 1,
                "commentaire": "15 occurrences au total. En T1 ligne 28, C etiquette VÉRIFIÉ deux references bibliographiques (de Moura et al. 2015 ; Ioannidis 2005) sans verification sur piece (signale par B en T2, corrige en RAPPORTÉ en T3). Ses autres etiquettes VÉRIFIÉ portent sur des identites mathematiques ou lectures directes.",
            },
            "D": {
                "verifie_majuscules_t1_t2_t3": [43, 32, 28],
                "etiquettes_verifie_propres_abusives_relevees": 10,
                "commentaire": "Usage massif de [VÉRIFIÉ] (43 en T1, 32 en T2, 28 en T3 ; 103 au total) : au moins 10 occurrences documentees qualifient des choix de conception, des conjectures empiriques ou des affirmations d'ingenierie non soutenues par faits.md (ex. T1 L25 e-graphes/grille dense, L28 formule MDL tronquee, L70 obfuscation, L91/L179/L182 pile et absence de derive, T3 L114/L119/L123 conclusions de faisabilite non demontrees empiriquement). Signale par A, B et E en T2, partiellement corrige en T3.",
            },
            "E": {
                "verifie_majuscules_t1_t2_t3": [5, 7, 9],
                "etiquettes_verifie_propres_abusives_relevees": 2,
                "commentaire": "21 occurrences au total. En T1, 2 doubles etiquettes composites ambigues (VÉRIFIÉ/RAPPORTÉ, L55 et L64) et un RAPPORTÉ sans reference en P1 (signales par A et B en T2 ; discipline d'etiquette unique appliquee en T3).",
            },
        },
    }

    return {
        "par_modele": par_modele,
        "par_cellule": par_cellule,
        "audit_confrontation_faits": audit_statuts,
    }


def rejouer_calculs() -> dict:
    """Regle 4 : rejeu arithmetique par code de tous les calculs chiffres cles cites dans les 15 cellules et les 2 lectures."""
    z975 = NORM.inv_cdf(0.975)  # 1.959964
    z95 = NORM.inv_cdf(0.95)    # 1.644854
    z995 = NORM.inv_cdf(0.995)  # 2.575829
    z80 = NORM.inv_cdf(0.80)    # 0.841621
    z93 = NORM.inv_cdf(0.93)    # 1.475791

    checks = []

    def add_check(
        cid: str,
        modele: str,
        cellule: str,
        description: str,
        valeur_citee: str,
        valeur_calculee: float,
        statut: str,
        commentaire: str = "",
    ) -> None:
        checks.append(
            {
                "id": cid,
                "modele": modele,
                "cellule": cellule,
                "description": description,
                "valeur_citee": valeur_citee,
                "valeur_calculee": round(valeur_calculee, 6),
                "statut": statut,
                "commentaire": commentaire,
            }
        )

    # --- MODELE A (Fable 5.2) ---
    add_check(
        "C-A01", "A", "T1",
        "Plafond d'etroitesse log2(K/3) pour K=300",
        "≈ 6,6 bits",
        math.log2(300 / 3),
        "exact",
        "Exact par regle de trois (6,6439 bits ; Clopper-Pearson exact : 6,6528 bits).",
    )
    n_a_t1_unpooled = ((z975 + z80) ** 2) * (0.05 * 0.95 + 0.15 * 0.85) / (0.10 ** 2)
    n_a_t1_pooled = (
        (z975 * math.sqrt(2 * 0.10 * 0.90) + z80 * math.sqrt(0.05 * 0.95 + 0.15 * 0.85)) / 0.10
    ) ** 2
    add_check(
        "C-A02", "A", "T1",
        "Taille d'echantillon E4 (5 % vs 15 %, alpha=0,05 bilateral, puissance 0,80) testee contre 0 vs regle > +5 pts",
        "≈ 140 (retenu 150)",
        n_a_t1_pooled,
        "erreur_regle_decision",
        f"Arithmetique contre 0 exacte (pooled={n_a_t1_pooled:.1f}, unpooled={n_a_t1_unpooled:.1f}), mais contredit la regle de E4 exigeant IC > +5 pts (reconnue et corrigee en T3 a 600 mondes).",
    )
    add_check(
        "C-A03", "A", "T1",
        "Plancher mesurable a 0/150 (borne superieure 95 %)",
        "≈ 2 %",
        clopper_pearson_upper(0, 150, 0.05),
        "exact",
        "1 - 0,05^(1/150) = 1,977 %.",
    )
    add_check(
        "C-A04", "A", "T1",
        "Cout etape 4 : 150 x 300 x 20000 jetons a 2000 j/s et 2 EUR/h",
        "9e8 jetons, 125 h-GPU, 250 EUR",
        (150 * 300 * 20000) / 2000 / 3600 * 2,
        "exact",
    )
    add_check(
        "C-A05", "A", "T2",
        "Fausse reussite par run 1 - (1 - 0,05)^50",
        "≈ 0,92",
        1.0 - (0.95 ** 50),
        "exact",
    )
    add_check(
        "C-A06", "A", "T2",
        "VPP a prevalence 0,01, sensibilite 0,80, FPR 0,05",
        "≈ 0,14",
        (0.80 * 0.01) / (0.80 * 0.01 + 0.05 * 0.99),
        "exact",
    )
    add_check(
        "C-A07", "A", "T2",
        "Sensibilite de certification (1 - 0,005)^300",
        "≈ 0,22",
        (1.0 - 0.005) ** 300,
        "exact",
    )
    add_check(
        "C-A08", "A", "T2",
        "Clopper-Pearson M0=1000 alpha=0,05 : -ln(u(0)) et -ln(u(1))",
        "5,81 nats (0 occ.) ; 5,35 nats (1 occ.)",
        -math.log(clopper_pearson_upper(1, 1000, 0.05)),
        "exact",
        f"0 occ.: {-math.log(clopper_pearson_upper(0, 1000, 0.05)):.4f} ; 1 occ.: {-math.log(clopper_pearson_upper(1, 1000, 0.05)):.4f}.",
    )
    add_check(
        "C-A09", "A", "T2",
        "Correlation intra-paire minimale pour demi-largeur 1,96*sqrt(2(1-r)/200) <= 0,05",
        "r >= 0,935",
        1.0 - ((0.05 / 1.96) ** 2) * 100.0,
        "exact",
    )
    add_check(
        "C-A10", "A", "T3",
        "Taille revisee E4' : n pour Delta=0,10, marge=0,05, q=0,20, alpha=0,05 bilat., puiss.=0,80",
        "600 mondes",
        ((z975 + z80) ** 2) * (0.20 - 0.10 ** 2) / ((0.10 - 0.05) ** 2),
        "exact",
        "Exact = 596,5 mondes.",
    )

    # --- MODELE B (Opus 5.5) ---
    add_check(
        "C-B01", "B", "T1",
        "Demi-largeur IC 95 % d'une proportion 0,8 sur n=200",
        "±0,055",
        z975 * math.sqrt(0.8 * 0.2 / 200),
        "exact",
    )
    n_b_t1 = 7.84 * (0.30 * 0.70 + 0.15 * 0.85) / (0.15 ** 2)
    add_check(
        "C-B02", "B", "T1",
        "Taille d'echantillon E4 (0,30 vs 0,15) testee contre 0 au lieu de Delta_min = 0,10",
        "≈ 118 problemes",
        n_b_t1,
        "erreur_regle_decision",
        "Arithmetique contre 0 exacte (117,6), mais donne seulement ~0,15 de puissance contre Delta_min=0,10 (reconnue et corrigee en T3 a 270 problemes).",
    )
    add_check(
        "C-B03", "B", "T1",
        "Phase 2 : 30000 x 20 x 3 x 1000 jetons a 10^4 j/s",
        "1,8e9 jetons, ≈ 50 h GPU",
        (30000 * 20 * 3 * 1000) / 1e4 / 3600,
        "exact",
    )
    add_check(
        "C-B04", "B", "T2",
        "Plafond nu <= log2(1/0,20) pour q=0,20",
        "≈ 2,3 bits",
        math.log2(1.0 / 0.20),
        "exact",
    )
    add_check(
        "C-B05", "B", "T2",
        "Taille pour D phase IV contre delta_min=0,10 (ecart effectif 0,03, q=0,2)",
        "≈ 1,7e3 paires",
        ((1.96 + 0.84) ** 2) * 0.2 / (0.03 ** 2),
        "exact",
    )
    facteur_i1 = math.log(3 * 60 / 0.05) / (-math.log(0.8))
    add_check(
        "C-B06", "B", "T3",
        "Identite I1 : facteur de rarete effective ln(3*60/0,05) / (-ln 0,8)",
        "≈ 37 fois tau",
        facteur_i1,
        "exact",
        f"ln(3600) = {math.log(3600):.4f}, ratio = {facteur_i1:.2f}.",
    )
    fpr_i2 = (0.8 * 0.01 * 0.2) / (0.99 * 0.8)
    add_check(
        "C-B07", "B", "T3",
        "Identite I2 : FPR cible pour pi=0,01, s=0,8, q*=0,2 et effectif a 0 alerte",
        "FPR ≈ 0,002 ; 1 500 negatifs",
        fpr_i2,
        "exact",
        f"FPR exact = {fpr_i2:.5f}, 3/FPR = {3/fpr_i2:.1f}.",
    )
    n_b_t3_1 = ((z975 + z80) ** 2) * (0.25 - 0.15 ** 2) / ((0.15 - 0.05) ** 2)
    n_b_t3_3 = ((z975 + z93) ** 2) * (0.25 - 0.15 ** 2) / ((0.15 - 0.05) ** 2)
    add_check(
        "C-B08", "B", "T3",
        "Identite I3 : taille E4' (1 contraste a 0,80 et 3 contrastes a 0,93)",
        "178 (1 contraste) ; ≈ 270 (3 contrastes)",
        n_b_t3_3,
        "exact",
        f"1 contraste = {n_b_t3_1:.1f}, 3 contrastes = {n_b_t3_3:.1f}.",
    )
    add_check(
        "C-B09", "B", "T3",
        "Phase P : 270 x 3 x 30000 x 1000 jetons a 10^4 j/s",
        "≈ 2,4e10 jetons, ≈ 680 h GPU",
        (270 * 3 * 30000 * 1000) / 1e4 / 3600,
        "exact",
        "Exact = 2,43e10 jetons, 675 h GPU.",
    )

    # --- MODELE C (Astra) ---
    fpr_c = (0.01 * 0.80 * 0.10) / (0.99 * 0.90)
    add_check(
        "C-C01", "C", "T1",
        "FPR maximal par Bayes pour prevalence 1 %, sensibilite 0,80, FDR <= 10 %",
        "≈ 0,00090",
        fpr_c,
        "exact",
        f"Exact = {fpr_c:.6f}.",
    )
    add_check(
        "C-C02", "C", "T1",
        "Nombre de negatifs a 0 alerte (alpha=0,05) pour borner FPR <= 0,00090",
        "≈ 3 330 negatifs",
        math.log(0.05) / math.log(1.0 - fpr_c),
        "exact",
        "1 - 0,05^(1/3330) = 0,0008992.",
    )
    add_check(
        "C-C03", "C", "T1",
        "Taille duel principal (q=0,20, g=0,05, unilateral 0,05, puissance 0,80)",
        "≈ 500 paires",
        ((z95 + z80) ** 2) * 0.20 / (0.05 ** 2),
        "exact",
        "Exact = 494,6 paires.",
    )
    add_check(
        "C-C04", "C", "T1",
        "Devis comparaison (500 x 4 x 20000 jetons a 40 j/s et 3 EUR/h)",
        "40M jetons, ≈ 280 h, 840 EUR",
        (500 * 4 * 20000) / 40 / 3600 * 3,
        "exact",
        "Exact = 277,8 h et 833,3 EUR.",
    )
    add_check(
        "C-C05", "C", "T1",
        "Devis solo de reference (500 x 300 x 20000 jetons a 40 j/s et 3 EUR/h)",
        "3 milliards de jetons, 62 500 EUR",
        (500 * 300 * 20000) / 40 / 3600 * 3,
        "exact",
        "Exact au centime : 62 500,00 EUR.",
    )
    add_check(
        "C-C06", "C", "T3",
        "Taille duel principal apres allocation alpha=0,005 unilateral (q=0,20, g=0,05, puiss. 0,80)",
        "≈ 935 paires",
        ((z995 + z80) ** 2) * 0.20 / (0.05 ** 2),
        "exact",
        "Exact = 934,3 paires.",
    )

    # --- MODELE D (Carbon) ---
    add_check(
        "C-D01", "D", "T1",
        "Plafond Clopper-Pearson M0=1000, alpha=0,05 en nats et en bits",
        "≈ 5,8 nats (≈ 8,4 bits)",
        -math.log(clopper_pearson_upper(0, 1000, 0.05)),
        "exact",
        f"5,8106 nats = {5.8106/math.log(2):.2f} bits.",
    )
    add_check(
        "C-D02", "D", "T1",
        "Phase IV : 100 problemes pour 0,05 -> 0,18 contre delta_min=0,10 (alpha=0,025 unilat.)",
        "100 problemes (puissance 0,80)",
        NORM.cdf((0.13 - 0.10) / math.sqrt((0.23 - 0.13 ** 2) / 100) - z975),
        "erreur_regle_decision",
        "Dimensionne contre 0 au lieu de delta_min=0,10 : puissance reelle ~0,09 contre delta_min=0,10 (corrigee en T3 a 220 problemes pour delta_min=0,05).",
    )
    add_check(
        "C-D03", "D", "T1",
        "Somme budgetaire T1 (20 + 1060 + 2800 + 6600 USD)",
        "10 480 USD (1 080 USD Phases I-II)",
        20 + 1060 + 2800 + 6600,
        "exact",
    )
    add_check(
        "C-D04", "D", "T2",
        "FDR a prevalence 0,01, sensibilite 0,80 : FPR=0,10 (A) et FPR=0,05 (B)",
        "> 0,91 (A) et ≈ 86 % (B)",
        (0.99 * 0.10) / (0.99 * 0.10 + 0.01 * 0.80),
        "exact",
        f"FPR=0,10 -> FDR={0.099/0.107:.4f} ; FPR=0,05 -> FDR={0.0495/0.0575:.4f}.",
    )
    u_cp_d_7 = clopper_pearson_upper(7, 4000, 0.05 / 3)
    u_cp_d_8 = clopper_pearson_upper(8, 4000, 0.05 / 3)
    p_star_d = math.exp(-5.5)
    add_check(
        "C-D05", "D", "T3",
        "Clopper-Pearson M0=4000, alpha=0,05/3 : nombre max d'occurrences sous exp(-5,5)=0,004087",
        "jusqu'a 7 occurrences",
        u_cp_d_7,
        "exact",
        f"p*=0,004087 ; k=7 -> u={u_cp_d_7:.6f} (< p*) ; k=8 -> u={u_cp_d_8:.6f} (> p*). Le maximum exact est bien 7 occurrences.",
    )
    add_check(
        "C-D06", "D", "T3",
        "Plafond d'union BestOfN-Mono(B) a b0=B/64 : 1 - (1 - e^(-5,5))^64",
        "≈ 0,23",
        1.0 - ((1.0 - p_star_d) ** 64),
        "exact",
    )
    se_d_t3 = math.sqrt((0.22 - 0.15 ** 2) / 220)
    puiss_d_1 = NORM.cdf((0.15 - 0.05) / se_d_t3 - z975)
    add_check(
        "C-D07", "D", "T3",
        "Exp. II revisee : SE et puissance pour M_prob=220, Delta=0,15, delta_min=0,05, q=0,22",
        "SE = 0,030 ; puissance conjointe 0,75 a 0,85",
        se_d_t3,
        "exact",
        f"SE exacte = {se_d_t3:.5f} ; puissance sur 1 contraste = {puiss_d_1:.3f}, sur 4 contrastes independants ≈ {puiss_d_1**4:.3f} (borne Bonferroni ≈ {max(0, 1 - 4*(1-puiss_d_1)):.3f}).",
    )
    add_check(
        "C-D08", "D", "T3",
        "Budget revise D T3 : 5400 GPU-h * 3 + 18000 CPU-h * 0,10",
        "18 000 USD (Phase I : 140 USD)",
        5400 * 3 + 18000 * 0.10,
        "exact",
    )

    # --- MODELE E (Neon) ---
    n_e_t1 = ((NORM.inv_cdf(0.995) + z80) ** 2) / (0.50 ** 2)
    add_check(
        "C-E01", "E", "T1",
        "Taille E5 (d=0,50, alpha=0,01, puissance 0,80) testee contre 0 au lieu de delta_5=0,20 sigma",
        "N ≈ 50-60 problemes",
        n_e_t1,
        "erreur_regle_decision",
        f"Contre 0 : N={n_e_t1:.1f} (bilateral) ; contre delta_5=0,20 sigma (ecart 0,30 sigma), il faut ~2,8 fois plus (~130-155, corrigee en T3 a 160/famille).",
    )
    add_check(
        "C-E02", "E", "T1",
        "Somme budgetaire E T1 (75 + 160 + 400 + 290 + 2750 + 2025 USD)",
        "5 700 USD (~925 USD avant E5, 84 % protege)",
        75 + 160 + 400 + 290 + 2750 + 2025,
        "exact",
        f"Avant E5 = 925 USD, protege = {(1 - 925/5700)*100:.2f} %.",
    )
    se_a_lo = math.sqrt((0.10 - 0.01) / 150)
    se_a_hi = math.sqrt((0.20 - 0.01) / 150)
    p_a_lo = NORM.cdf(0.05 / se_a_hi - z975)
    p_a_hi = NORM.cdf(0.05 / se_a_lo - z975)
    add_check(
        "C-E03", "E", "T2",
        "Puissance reelle de A (n=150, Delta=0,10 contre 0,05, q in [0,10;0,20])",
        "[0,29 ; 0,53]",
        p_a_hi,
        "exact",
        f"Exact : [{p_a_lo:.3f} ; {p_a_hi:.3f}].",
    )
    add_check(
        "C-E04", "E", "T2",
        "Biais de l'enveloppe par probleme pour B=4 copies i.i.d. a p=0,15",
        "-0,328",
        0.15 - (1.0 - 0.85 ** 4),
        "exact",
    )
    add_check(
        "C-E05", "E", "T2",
        "Puissance de B a n=118 et n=200 (0,30 vs 0,15 contre Delta_min=0,10)",
        "0,15 (n=118) ; 0,23 (n=200)",
        NORM.cdf(0.05 / math.sqrt(0.3375 / 118) - z975),
        "exact",
        f"n=118 : {NORM.cdf(0.05/math.sqrt(0.3375/118)-z975):.3f} ; n=200 : {NORM.cdf(0.05/math.sqrt(0.3375/200)-z975):.3f}.",
    )
    add_check(
        "C-E06", "E", "T2",
        "Puissance OR de D (n1=n0=60, 0,15 vs 0,05, seuil OR=2,5)",
        "OR=3,35 ; SE=0,694 ; puissance=0,06",
        NORM.cdf((math.log((0.15 / 0.85) / (0.05 / 0.95)) - math.log(2.5)) / math.sqrt(1 / (60 * 0.15 * 0.85) + 1 / (60 * 0.05 * 0.95)) - z975),
        "exact",
    )
    add_check(
        "C-E07", "E", "T2",
        "Probabilite >= 2 alertes sur 500 negatifs a FPR=0,008",
        "0,91 (puissance validation 0,09)",
        1.0 - (0.992 ** 500) - 500 * 0.008 * (0.992 ** 499),
        "exact",
    )
    add_check(
        "C-E08", "E", "T3",
        "Certification K_ref=800, 3 politiques x 5 bras, alpha=0,01 : 1 - (0,01/15)^(1/800)",
        "≈ 0,0091 < 0,01",
        clopper_pearson_upper(0, 800, 0.01 / 15),
        "exact",
    )
    add_check(
        "C-E09", "E", "T3",
        "Borne a 0 alerte pour N_- = 2000 (alpha=0,025 unilateral) et ambiguite 'stratifies'",
        "≈ 0,0018 < 0,002",
        clopper_pearson_upper(0, 2000, 0.025),
        "ambiguite_stratification",
        f"Exact si 2000 negatifs PAR strate ({clopper_pearson_upper(0, 2000, 0.025):.5f} < 0,002), mais si 2000 sont REPARTIS entre 3 strates (~667/strate), la borne par strate monte a {clopper_pearson_upper(0, 667, 0.025):.5f} > 0,002.",
    )
    add_check(
        "C-E10", "E", "T3",
        "Dimensionnement E5 revise : (1,96+0,84)^2 * (0,22 - 0,15^2) / 0,10^2",
        "≈ 155 (retenu 160/famille)",
        ((1.96 + 0.84) ** 2) * (0.22 - 0.15 ** 2) / (0.10 ** 2),
        "exact",
    )
    add_check(
        "C-E11", "E", "T3",
        "Somme budgetaire E T3 (250+250+300+1400+500+8000+5500 USD)",
        "16 200 USD (~2 700 USD avant E5, 83 % protege)",
        250 + 250 + 300 + 1400 + 500 + 8000 + 5500,
        "exact",
    )

    # --- LECTEURS AVEUGLES ---
    add_check(
        "C-L01", "Lecteur Astra", "lecture-astra-v1",
        "Borne superieure 95 % pour 0/100 : 1 - 0,05^(1/100)",
        "≈ 2,95 %",
        clopper_pearson_upper(0, 100, 0.05),
        "exact",
    )
    add_check(
        "C-L02", "Lecteur Astra", "lecture-astra-v1",
        "VPP a 1 % prevalence, 80 % sensibilite, 5 % fausses alertes : 0,008/(0,008+0,0495)",
        "≈ 14 %",
        0.008 / (0.008 + 0.0495),
        "exact",
    )

    # Synthese taux d'erreur de calcul par modele
    synthese_modele = {}
    for m in ["A", "B", "C", "D", "E", "Lecteur Astra"]:
        sub = [c for c in checks if c["modele"] == m]
        exacts = sum(1 for c in sub if c["statut"] == "exact")
        erreurs_regle = sum(1 for c in sub if c["statut"] == "erreur_regle_decision")
        ambig = sum(1 for c in sub if c["statut"] == "ambiguite_stratification")
        synthese_modele[m] = {
            "calculs_rejoues": len(sub),
            "exacts": exacts,
            "erreurs_dimensionnement_t1_corrigees_t3": erreurs_regle,
            "ambiguites_a_lever": ambig,
            "taux_defaut_sur_calculs_rejoues": round((len(sub) - exacts) / len(sub), 4) if sub else 0.0,
        }

    return {
        "nombre_total_calculs_rejoues": len(checks),
        "synthese_par_modele": synthese_modele,
        "details": checks,
    }


def relever_references() -> list[dict]:
    """Regle 4 / R7 : inventaire consolide des references bibliographiques citees dans le dossier (toutes a verifier sur PDF)."""
    refs = [
        ("Angelopoulos et al. (2023)", "Prediction-Powered Inference", "Science", ["E1", "D2", "E2", "E3", "Opus-L"], "Correction statistique d'un juge avec échantillon audité"),
        ("Begg & Greenes (1983)", "Assessment of diagnostic tests when disease verification is subject to selection bias", "Biometrics", ["A2", "D3", "Opus-L", "Astra-L"], "Biais de vérification lors d'un audit stratifié par verdict"),
        ("Benjamini & Hochberg (1995)", "Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing", "JRSS Series B", ["E1"], "Contrôle du taux de fausses découvertes"),
        ("Bennett (1988)", "Logical Depth and Physical Complexity", "The Universal Turing Machine: A Half-Century Survey (OUP)", ["D1", "E1", "D3", "E3"], "Distinction entre complexité aléatoire et profondeur logique"),
        ("Berger (1982)", "Multiparameter Hypothesis Testing and Acceptance Sampling", "Technometrics", ["D1", "D3", "E2", "E3", "Opus-L", "Astra-L"], "Test d'intersection-union contre plusieurs lignes de base"),
        ("Blum & Hardt (2015)", "The Ladder: A Reliable Leaderboard for Machine Learning Competitions", "ICML", ["A1", "Opus-L"], "Protection contre le sur-ajustement adaptatif d'un classement"),
        ("Boden (1990)", "The Creative Mind: Myths and Mechanisms", "Ouvrage", ["A1"], "Distinction entre nouveauté et valeur"),
        ("Campbell (1979)", "Assessing the Impact of Planned Social Change", "Evaluation and Program Planning", ["A1"], "Corruption d'indicateur utilisé comme cible"),
        ("Chen et al. (2021)", "Evaluating Large Language Models Trained on Code", "prépublication arXiv (identifiant non fourni)", ["B1", "E2"], "Estimateur pass@k"),
        ("Clopper & Pearson (1934)", "The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial", "Biometrika", ["D1", "C3", "D3", "E2", "E3", "Opus-L", "Astra-L"], "Bornes de confiance binomiales exactes"),
        ("Cranmer (2023)", "Interpretable Machine Learning for Science with PySR and SymbolicRegression.jl", "prépublication arXiv (lieu à vérifier)", ["A1", "B1", "D2", "Opus-L"], "Régression symbolique évolutionnaire (PySR)"),
        ("Dwork et al. (2015)", "The Reusable Holdout: Preserving Validity in Adaptive Data Analysis", "Science", ["A1", "D1", "E1", "A3", "D3", "E2", "E3", "Opus-L", "Astra-L"], "Dégradation adaptative d'un jeu de test et mécanisme Thresholdout"),
        ("Efron & Tibshirani (1993)", "An Introduction to the Bootstrap", "Chapman & Hall", ["E1", "D2"], "Bootstrap en grappes"),
        ("Fieller (1954)", "Some Problems in Interval Estimation", "JRSS Series B", ["D2", "A3", "Opus-L"], "Régions de confiance non bornées pour un rapport d'estimateurs"),
        ("Golchin & Surdeanu (2024)", "Time Travel in LLMs: Tracing Data Contamination in Large Language Models", "ICLR", ["A1", "Opus-L"], "Détection de contamination par complétion"),
        ("Grünwald (2007)", "The Minimum Description Length Principle", "MIT Press", ["D1", "D3", "Opus-L"], "Principe de longueur de description minimale"),
        ("Hanley & Lippman-Hand (1983)", "If Nothing Goes Wrong, Is Everything All Right?", "JAMA", ["A1", "A3", "Opus-L"], "Règle de trois (borne 3/K à zéro occurrence)"),
        ("Holm (1979)", "A Simple Sequentially Rejective Multiple Test Procedure", "Scandinavian Journal of Statistics", ["E1"], "Correction de multiplicité séquentielle"),
        ("Ioannidis (2005)", "Why Most Published Research Findings Are False", "PLoS Medicine", ["C1"], "Valeur prédictive positive sous faible prévalence"),
        ("Kaplan & Meier (1958)", "Nonparametric Estimation from Incomplete Observations", "JASA", ["D2"], "Non-identifiabilité de la médiane sous censure à droite"),
        ("La Cava et al. (2021)", "Contemporary Symbolic Regression Methods and their Relative Performance", "NeurIPS Datasets and Benchmarks", ["A1", "Opus-L"], "Banc comparatif de régression symbolique (SRBench)"),
        ("Lehman & Stanley (2011)", "Abandoning Objectives: Evolution Through the Search for Novelty Alone", "Evolutionary Computation", ["A1", "B1", "Opus-L"], "Recherche de nouveauté"),
        ("Li & Vitányi (2008)", "An Introduction to Kolmogorov Complexity and Its Applications", "Springer", ["D3"], "Invariance de la complexité descriptive à une constante additive près"),
        ("Manheim & Garrabrant (2018)", "Categorizing Variants of Goodhart's Law", "prépublication arXiv (identifiant non fourni)", ["B1"], "Taxonomie de la loi de Goodhart"),
        ("de Moura et al. (2015)", "The Lean Theorem Prover (System Description)", "CADE", ["C1", "C3"], "Noyau de preuve formelle Lean (version 2/3)"),
        ("de Moura & Ullrich (2021)", "The Lean 4 Theorem Prover and Programming Language", "CADE 28 (Springer)", ["D1", "D3", "Opus-L", "Astra-L"], "Noyau de preuve formelle Lean 4"),
        ("Mouret & Clune (2015)", "Illuminating search spaces by mapping elites", "prépublication arXiv (identifiant non fourni)", ["B1"], "Illumination d'espaces de recherche (MAP-Elites)"),
        ("Newcombe (1998)", "Improved confidence intervals for the difference between binomial proportions based on paired data", "Statistics in Medicine", ["A3", "Opus-L", "Astra-L"], "Intervalles de confiance pour différences de proportions appariées"),
        ("Nosek et al. (2018)", "The preregistration revolution", "PNAS", ["B1"], "Préenregistrement des seuils et hypothèses"),
        ("O'Brien & Fleming (1979)", "A multiple testing procedure for clinical trials", "Biometrics", ["B1", "D2", "Opus-L"], "Frontières d'arrêt séquentiel de groupe"),
        ("Panickssery, Bowman & Feng (2024)", "LLM Evaluators Recognize and Favor Their Own Generations", "NeurIPS", ["A1", "B1", "A3", "B3", "Opus-L"], "Auto-reconnaissance et auto-préférence des juges de langage"),
        ("Pearl (2009)", "Causality: Models, Reasoning, and Inference", "Cambridge University Press", ["D1", "E1", "D3"], "Interventions causales do(.) et indistinguabilité observationnelle"),
        ("Platt (1964)", "Strong Inference", "Science", ["A1", "B1", "D1", "E1", "D3", "Opus-L"], "Cadre d'expériences décisives en inférence forte"),
        ("Popper (1959)", "The Logic of Scientific Discovery", "Hutchinson", ["D1", "E1", "D3"], "Réfutabilité et expériences cruciales"),
        ("Rice (1953)", "Classes of Recursively Enumerable Sets and Their Decision Problems", "Trans. Amer. Math. Soc.", ["D1", "D3"], "Indécidabilité de l'équivalence sémantique générale"),
        ("Rissanen (1978)", "Modeling by shortest data description", "Automatica", ["D1", "E1", "D3", "E3", "Opus-L"], "Principe de longueur de description minimale"),
        ("Rogan & Gladen (1978)", "Estimating Prevalence from the Results of a Screening Test", "American Journal of Epidemiology", ["D1", "D3", "E2", "Opus-L"], "Correction de prévalence pour un test imparfait"),
        ("Romera-Paredes et al. (2024)", "Mathematical discoveries from program search with large language models", "Nature", ["B1"], "Recherche de programmes assistée par modèle (FunSearch)"),
        ("Schmidt & Lipson (2009)", "Distilling Free-Form Natural Laws from Experimental Data", "Science", ["B1"], "Découverte symbolique mécanique de lois naturelles"),
        ("Schwartz (1980)", "Fast Probabilistic Algorithms for Verification of Polynomial Identities", "J. ACM", ["D3", "Opus-L"], "Test probabiliste d'identité polynomiale hors grille"),
        ("Shannon (1948)", "A Mathematical Theory of Communication", "Bell System Technical Journal", ["E1", "E3"], "Entropie et complexité aléatoire"),
        ("Simmons, Nelson & Simonsohn (2011)", "False-Positive Psychology", "Psychological Science", ["A1"], "Degrés de liberté du chercheur"),
        ("Solomonoff (1964)", "A Formal Theory of Inductive Inference. Part I", "Information and Control", ["E1", "E3"], "Dépendance de la complexité descriptive au langage de codage"),
        ("The mathlib Community (2020)", "The Lean Mathematical Library", "CPP", ["A1", "B1", "Opus-L"], "Bibliothèque mathématique formelle Mathlib"),
        ("Udrescu & Tegmark (2020)", "AI Feynman: a physics-inspired method for symbolic regression", "Science Advances", ["B1", "D1", "E1", "D3"], "Régression symbolique mécanique (AI Feynman)"),
        ("Uzzi et al. (2013)", "Atypical Combinations and Scientific Impact", "Science", ["A1"], "Combinaisons atypiques et impact scientifique"),
        ("Wald (1945)", "Sequential Tests of Statistical Hypotheses", "Annals of Mathematical Statistics", ["E1"], "Tests séquentiels"),
        ("Wang, Veugelers & Stephan (2017)", "Bias Against Novelty in Science", "Research Policy", ["A1"], "Reconnaissance tardive des travaux atypiques"),
        ("Wolpert & Macready (1997)", "No Free Lunch Theorems for Optimization", "IEEE Trans. Evol. Comp.", ["B1", "E1", "E3", "Opus-L"], "Absence de domination universelle sans structure"),
        ("Zheng et al. (2023)", "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", "NeurIPS Datasets and Benchmarks", ["A1", "B1", "A3", "B3", "Opus-L"], "Biais d'auto-valorisation, position et verbosité des juges de langage"),
    ]
    return [
        {
            "auteurs_annee": a,
            "titre_cite": t,
            "lieu_cite": v,
            "cite_par": c,
            "usage_dans_dossier": u,
            "etat_r7": "à vérifier sur PDF (non vérifiée ici)",
        }
        for a, t, v, c, u in refs
    ]


def preparer_graine_regle_1c() -> dict:
    """Protocole X 2.1, regle 1 c : liste des propositions non retenues admissibles sur processeur
    et proposition de graine SeedSequence prete a etre engagee avant tirage (sans tirer avant engagement)."""
    eligibles_cpu = [
        {
            "indice": 0,
            "id": "U20",
            "intitule": "Enveloppe des lignes de base prise problème par problème (max par problème)",
            "epreuve_processeur": "Simulation A/A multi-copies (une copie contre l'enveloppe de 4 copies identiques) sur 1 000 campagnes : mesurer le biais négatif exact.",
            "cout_estime": "< 5 USD (processeur seul, < 1 heure)",
        },
        {
            "id": "U21",
            "indice": 1,
            "intitule": "Score primaire égal au maximum de profondeur sur tout le vivier (sans nomination scellée)",
            "epreuve_processeur": "Simulation sur viviers de tailles 10 à 1 000 à profondeur vraie identique et bruit gaussien : mesurer la pente en sqrt(2 ln m).",
            "cout_estime": "< 5 USD (processeur seul, < 1 heure)",
        },
        {
            "indice": 2,
            "id": "U22",
            "intitule": "Score de compression tronqué à zéro régime par régime",
            "epreuve_processeur": "Simulation de prédicteurs sans gain net à variance croissante sur R régimes : mesurer le taux de franchissement du seuil.",
            "cout_estime": "< 5 USD (processeur seul, < 1 heure)",
        },
        {
            "indice": 3,
            "id": "U23",
            "intitule": "Étroitesse scalaire comparée par corrélation de rang (Spearman) entre références sous censure",
            "epreuve_processeur": "Simulation sur un panel de classes à probabilités rares connues (K=300) : mesurer la proportion d'ex æquo à zéro et l'effondrement de la fiabilité demi-échantillons.",
            "cout_estime": "< 5 USD (processeur seul, < 1 heure)",
        },
        {
            "indice": 4,
            "id": "U16",
            "intitule": "Clé partielle extensionnelle (observable, portée déclarée, vecteur de réponses) livrée au résolveur par interface commune [désaccord lecteurs : écartée par Opus en N7, retenue par Astra en P2]",
            "epreuve_processeur": "Micromonde fini sur processeur : comparer table et formule équivalentes par la même interface et mesurer la sensibilité à une règle différant sur une seule entrée.",
            "cout_estime": "< 10 USD (processeur seul)",
        },
    ]
    # Entier deterministe derive du SHA-256 de l'engagement, propose a inscrire avant tirage
    h_eng = sha256_file(RUN_DIR / "engagement.md")
    graine_proposee = int(h_eng[:16], 16)
    return {
        "statut": "proposition_prete_a_engager_avant_tirage",
        "explication": "Conformément à la règle 1 c du Protocole X version 2.1, la graine doit être inscrite dans le journal avant le tirage effectif ; le script ne révèle aucun tirage avant inscription par la mère ou Lazar.",
        "methode": "numpy.random.default_rng(numpy.random.SeedSequence(graine)).integers(0, len(eligibles_cpu))",
        "graine_proposee_depuis_engagement_sha256_64bits": graine_proposee,
        "source_graine": f"64 premiers bits du SHA-256 de engagement.md ({h_eng})",
        "propositions_non_retenues_ou_contestees_admissibles_processeur": eligibles_cpu,
    }


def main() -> None:
    result = {
        "meta": {
            "dossier": RUN_REL,
            "accord": "GO-2026-11-24-39",
            "protocole": "lancé en version 1 du Protocole X ; note rendue en version 2 / 2.1 (règles 1 en 2.1, 3, 4, 6, 7 appliquées ; écarts 2 et 5 déclarés)",
            "script": "analyser_attelage_v1.py",
        },
        "empreintes_et_integrite": verifier_empreintes(),
        "couts": analyser_couts(),
        "lecture_double_et_fournisseurs": analyser_alignement_et_fournisseurs(),
        "controles_statuts_regle_4": analyser_statuts_verifie(),
        "controles_calculs_regle_4": rejouer_calculs(),
        "references_a_verifier_r7": relever_references(),
        "regle_1c_tirage_non_retenue": preparer_graine_regle_1c(),
    }
    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Affichage synthese console
    print("=== INTEGRITE ===")
    print("Tous compagnons SHA-256 valides :", result["empreintes_et_integrite"]["tous_compagnons_valides"],
          f"({result['empreintes_et_integrite']['nombre_compagnons_verifies']} fichiers)")
    print("faits.md == question-etage3.md :", result["empreintes_et_integrite"]["faits_identique_question"])

    print("\n=== COUTS (USD) ===")
    sc = result["couts"]["synthese_dossier"]
    ce = result["couts"]["collisionneur_etage3"]
    print(f"Course etage III comptee : {ce['cout_compte_total_usd']:.4f} USD (arrondi {ce['cout_compte_arrondi_2dec_usd']:.2f})")
    print("Par fournisseur (etage III) :", ce["par_fournisseur"])
    print("Par espece (etage III) :", {k: v["cout_usd"] for k, v in ce["par_espece"].items()})
    print("Par tour (etage III) :", ce["par_tour_usd"])
    print(f"Lecteur Astra (lecture-double) : {result['couts']['lecture_double']['lecteur_astra_cout_usd']:.4f} USD")
    print(f"Paye compte (Anthropic+OpenAI) course seule : {sc['paye_compte_course_seule_usd']:.4f} USD")
    print(f"Paye compte (Anthropic+OpenAI) avec lecteur Astra : {sc['paye_compte_avec_lecture_astra_usd']:.4f} USD")
    print(f"Google compte (sous reserve gratuite) : {sc['google_sous_reserve_gratuite_usd']:.4f} USD")
    print(f"Total compte dossier (course + lecteur Astra) : {sc['total_compte_avec_lecture_astra_usd']:.4f} USD (plafond GO = 25 USD)")

    print("\n=== LECTURE DOUBLE & KAPPA DE COHEN ===")
    ld = result["lecture_double_et_fournisseurs"]
    print("Principal (31 unites) :", ld["kappa_principal_31_unites"])
    print("Sensibilite explicites des 2 cotes :", ld["kappa_sensibilite_explicites_deux_lecteurs"])
    print("Sensibilite recoupement large :", ld["kappa_sensibilite_recoupement_large"])

    print("\n=== CONTROLES REGLE 4 ===")
    print("Mentions VERIFIE (maj) par modele :",
          {k: v["verifie_majuscules_total"] for k, v in result["controles_statuts_regle_4"]["par_modele"].items()})
    print("Calculs rejoues :", result["controles_calculs_regle_4"]["nombre_total_calculs_rejoues"])
    print("Synthese calculs par modele :", result["controles_calculs_regle_4"]["synthese_par_modele"])
    print("References R7 relevees :", len(result["references_a_verifier_r7"]))
    print("JSON ecrit :", OUT_JSON, "sha256=", sha256_file(OUT_JSON))


if __name__ == "__main__":
    main()
