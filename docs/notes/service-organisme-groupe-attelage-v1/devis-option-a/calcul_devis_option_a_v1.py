#!/usr/bin/env python3
"""Calcul du devis de la course « atelier » (option (a)) : service de la question fusionnée neutre à l'organisme d'idéation,
protocole X version 2 (questions témoins, lecture double à l'aveugle, contrôles par programme, bras témoin), puis étage des
tests de mort existant (mesure de l'expérimentateur sur les témoins, puis fiches des propositions et contrôles cachés).

Classe A (devis). Rédigé par Opus 5.5 en écart à la règle « Fable écrit les devis » (quota de Fable gelé jusqu'au
2 décembre, R-5297). À contre-lire. Hors ligne : aucun appel de modèle, aucun réseau, aucune machine.

Ce que fait ce programme, et rien d'autre :
1. relit chaque source citée (fichier du dépôt, ou fichier d'une branche par `git show`), en calcule l'empreinte et retrouve
   la ligne qui porte le chiffre (recherche d'une sous-chaîne écrite ici) ; une source absente ou une sous-chaîne introuvable
   arrête le calcul (code 2) : aucun chiffre sans renvoi ;
2. recalcule chaque poste (attendu, haut, pire compté avec les relances permises, pire payé, clé gratuite à zéro) ;
3. passe les corps de génération proposés pour Google à la garde commune (`src/controle_ia/garde_google_v3.py`) : ils doivent
   passer ; les réglages de la course v9 (aucun réglage de réflexion, ou budget de réflexion, sortie 65 536 non diffusée)
   doivent être refusés ; sinon arrêt (code 3).

Usage (racine du dépôt) : PYTHONDONTWRITEBYTECODE=1 python3 -I docs/notes/service-organisme-groupe-attelage-v1/devis-option-a/calcul_devis_option_a_v1.py
Paramètres : `--faits-car`, `--question-car`, `--cases`, `--fiches-propositions`, `--controles-caches` (défauts du mandat).
Bibliothèque standard seulement (plus la garde du dépôt, chargée par son chemin).
"""
import argparse
import hashlib
import importlib.util
import json
import math
import subprocess
import sys
from pathlib import Path

DEPOT = Path(__file__).resolve().parents[4]
BRANCHE_ORGANISME = "origin/lot/compte-organisme-v1"
VERSION = "calcul-devis-option-a-v1"


class Arret(Exception):
    pass


# ---------------------------------------------------------------------------------------------------------------------------
# 1. Sources : (clé, emplacement, sous-chaîne qui porte le chiffre). Emplacement « git:REF:chemin » = lu par `git show`.
# ---------------------------------------------------------------------------------------------------------------------------
P_PRIX_A = "docs/sources/prix/page-prix-anthropic-docs-20261122T104128Z.md"
P_PRIX_G = "docs/sources/prix/page-prix-gemini-api-20261122T104129Z.html"
P_RELEVE = "docs/notes/service-collisionneur-modes-v8-v1/calculs/releve-journaux-v2.json"
P_COL = "docs/notes/collisionneur-v9/collisionneur_v9_v8m.py"
P_COL_DEVIS = "docs/notes/protocole-x-structure-du-langage-v1/calcul_devis_collisionneur_groupe_v1.py"
P_ASTRA = "docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py"
P_V9 = "scripts/lancer_course_auto_conception_v9.py"
P_ORCH = "docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/pole/"
P_CONC = "docs/notes/experimentateurs-et-tests-de-mort-v1/conception-branchement-experimentateurs-tests-de-mort-v1.md"
P_DEP = "registres/depenses.md"
P_GARDE = "src/controle_ia/garde_google_v3.py"
P_DEMANDE = "docs/notes/service-organisme-groupe-attelage-v1/demande-reformulee-quatre-points-v1.md"
G = "git:" + BRANCHE_ORGANISME + ":docs/notes/organisme-auto-conception-v1/"

SOURCES = {
    "prix_fable51": (P_PRIX_A, "| Claude Fable 5.1 | $10 / MTok |"),
    "prix_opus55": (P_PRIX_A, "| Claude Opus 5.5 | $4 / MTok |"),
    "prix_sonnet55": (P_PRIX_A, "| Claude Sonnet 5.5 | $2 / MTok |"),
    "prix_carbon_entree": (P_PRIX_G, "$4.00 starting December 1, 2026."),          # première occurrence : Carbon (l. 156)
    "prix_carbon_sortie": (P_PRIX_G, "$20.00 starting December 1, 2026."),         # Carbon (l. 163)
    "carbon_pas_de_palier_gratuit": (P_PRIX_G, "Gemini 4 Carbon is not available on the Free tier."),
    "prix_argon_titre": (P_PRIX_G, "## Gemini 4 Argon"),
    "prix_astra": (P_ASTRA, 'a.add_argument("--prix-sortie", type=float, default=50.0)'),
    "astra_max_sortie": (P_ASTRA, 'a.add_argument("--max-sortie-jetons", type=int, default=32768)'),
    "astra_pire": (P_ASTRA, "pire = (len(corps) + 1024) * args.prix_entree / 1e6 + n * args.prix_sortie / 1e6"),
    "releve_journaux": (P_RELEVE, '"carbon|E3-T1"'),
    "col_opus_max": (P_COL, '"opus": {"id": "claude-opus-5-5", "fournisseur": "anthropic", "prix": (4.0, 20.0),'),
    "col_fable_max": (P_COL, "MAX_FABLE_V3 = 49000"),
    "col_argon": (P_COL, '"max": 65536, "max_relance": 65536, "budget": None, "niveau_reflexion": "high", "provision": 16384,'),
    "col_carbon_provision": (P_COL, "PROVISION_CARBON_V6 = 49152"),
    "col_pire_garde": (P_COL, 'return garde / 1e6 * m["prix"][0] + (max_tokens + m["provision"]) / 1e6 * m["prix"][1]'),
    "col_relances": (P_COL_DEVIS, 'relances = 2 if (m["fournisseur"] == "gemini" and col.reglage_de_relance(m)[1]) else 1'),
    "v9_octets_par_jeton": (P_V9, "OCTETS_PAR_JETON_AU_PIRE = 2.0"),
    "v9_devis_par_appel": (P_V9, 'DEVIS_V1_PAR_APPEL = {"prop-opus": 0.2536'),
    "v9_cle_minuit": (P_V9, 'CLE_CLAUDE_TENTATIVE = "RR_ANTHROPIC_API_KEY_MINUIT"'),
    "v2i_aiguillage": (G + "course-v4/devis-course-auto-conception-v2i.md", "| aiguillage | 3,41 | 20,46 | |"),
    "v2i_juges": (G + "course-v4/devis-course-auto-conception-v2i.md", "| juges | 7,89 | 47,32 | |"),
    "v2_appels": (G + "devis-course-auto-conception-v2.md", "| + Astra + Carbon | 55 / 110 / 220 |"),
    "v5_cartes_par_appel": (G + "course-v4/configuration-course-auto-conception-v5.json", '"cartes_par_appel": 2,'),
    "v5_plafond_aiguilleur": (G + "course-v4/configuration-course-auto-conception-v5.json", '"aiguilleur": 0.25,'),
    "v5_plafond_juge": (G + "course-v4/configuration-course-auto-conception-v5.json", '"juge": 0.6,'),
    "consigne_proposeur_v2": (G + "course-v2/consigne-proposeur-auto-conception-v2.md", "#"),
    "tdm_nombre_max": (P_ORCH + "tests_de_mort_v2.py", "NOMBRE_MAX = 12"),
    "tdm_lecteur_defaut": (P_ORCH + "tests_de_mort_v2.py", "BUDGET_LECTEUR_USD_DEFAUT = 0.1"),
    "tf_budget_exp": (P_ORCH + "tour_ferme_v64.py", "BUDGET_EXPERIMENTATEUR_PAR_CARTE_USD = 0.80"),
    "tf_douze_tours": (P_ORCH + "tour_ferme_v64.py", "12 × 0,06 = 0,72 USD"),
    "tf_duree": (P_ORCH + "tour_ferme_v64.py", "DUREE_ETAGE_1_H = 72.0"),
    "tf_temoins": (P_ORCH + "tour_ferme_v64.py", '"T-VRAIE": v, "T-F1"'),
    "conc_releve_v67": (P_CONC, "au plus 0,081 USD par test pour l'expérimentateur et 0,061 pour le lecteur"),
    "dep_machine_v66": (P_DEP, "machine Hetzner 175751768 (cpx32, hel1, debian-13), 00:01:08Z → 00:22:29Z (21 min 21 s) ; ≈ 0,059 EUR TTC"),
    "dep_machine_v67": (P_DEP, "machine Hetzner 175834755 (cpx32, hel1, debian-13), 14:01:34Z → 17:19:43Z (3 h 18 min 9 s) ; ≈ 0,235 EUR TTC"),
    "dep_taux": (P_DEP, "0,22692 EUR ≈ 0,28 USD (taux 1,25)"),
    "dep_v9_close": (P_DEP, "Organisme v9 : course de l'auto-conception CLOSE, code 0 (Claude 36,457056 sur Minuit ; Carbon 24,719127"),
    "garde_limites": (P_GARDE, 'LIMITES_SORTIE = {"argon": {"flux": 65536, "non_diffuse": 32768},'),
    "garde_texte_min": (P_GARDE, "TEXTE_MIN_GOOGLE = 16000"),
    "garde_jetons_par_mot": (P_GARDE, 'JETONS_PAR_MOT_MESURES = {"argon": 5.1, "carbon": 4.2, "neon": 5.1}'),
    "demande_octets": (P_DEMANDE, "# Demande reformulée en quatre points"),
}


def lire_source(emplacement: str) -> bytes:
    if emplacement.startswith("git:"):
        _, ref, chemin = emplacement.split(":", 2)
        r = subprocess.run(["git", "-C", str(DEPOT), "show", f"{ref}:{chemin}"], capture_output=True)
        if r.returncode != 0:
            raise Arret(f"source absente : {emplacement} ({r.stderr.decode(errors='replace').strip()[:200]})")
        return r.stdout
    p = DEPOT / emplacement
    if not p.is_file():
        raise Arret(f"source absente : {emplacement}")
    return p.read_bytes()


def resoudre_sources() -> dict:
    out, cache = {}, {}
    for cle, (emp, aiguille) in SOURCES.items():
        if emp not in cache:
            cache[emp] = lire_source(emp)
        octets = cache[emp]
        lignes = octets.decode("utf-8", errors="replace").splitlines()
        n = next((i for i, l in enumerate(lignes, 1) if aiguille in l), None)
        if n is None:
            raise Arret(f"source {cle} : « {aiguille[:60]} » introuvable dans {emp}")
        out[cle] = {"fichier": emp, "ligne": n, "sha256": hashlib.sha256(octets).hexdigest(), "octets": len(octets),
                    "caracteres": len(octets.decode("utf-8", errors="replace"))}
    return out


def ref(src: dict, cle: str) -> str:
    s = src[cle]
    return f"{s['fichier'].split(':')[-1]} l. {s['ligne']} ({s['sha256'][:8]}…)"


# ---------------------------------------------------------------------------------------------------------------------------
# 2. Modèles, prix (USD par million de jetons) et réglages proposés. Chaque valeur renvoie à une source ci-dessus.
# ---------------------------------------------------------------------------------------------------------------------------
MODELES = {
    # nom : identifiant, fournisseur, clé (par son nom), (prix entrée, sortie), plafond de sortie, provision de réflexion
    # comptée (Google), niveau de réflexion (Google), source du prix, source du réglage
    "opus": dict(id="claude-opus-5-5", fournisseur="anthropic", cle="RR_ANTHROPIC_API_KEY_LUC", prix=(4.0, 20.0),
                 max=64000, provision=0, payant=True, src_prix="prix_opus55", src_reglage="col_opus_max"),
    "fable51": dict(id="claude-fable-5-1", fournisseur="anthropic", cle="RR_ANTHROPIC_API_KEY_LUC", prix=(10.0, 50.0),
                    max=49000, provision=0, payant=True, src_prix="prix_fable51", src_reglage="col_fable_max"),
    "sonnet": dict(id="claude-sonnet-5-5", fournisseur="anthropic", cle="RR_ANTHROPIC_API_KEY_LUC", prix=(2.0, 10.0),
                   max=None, provision=0, payant=True, src_prix="prix_sonnet55", src_reglage=None),
    "argon": dict(id="gemini-4-argon", fournisseur="google", cle="GEMINI_API_KEY", prix=(4.0, 20.0),
                  max=65536, provision=16384, niveau="high", payant=True, src_prix="prix_argon_titre",
                  src_reglage="col_argon"),
    # Argon juge et lecteur témoin de l'étage : sortie 32 768 en flux, provision 16 384 (texte 16 384 ≥ 16 000)
    "argon_court": dict(id="gemini-4-argon", fournisseur="google", cle="GEMINI_API_KEY", prix=(4.0, 20.0),
                        max=32768, provision=16384, niveau="high", payant=True, src_prix="prix_argon_titre",
                        src_reglage="garde_limites"),
    "carbon": dict(id="gemini-4-carbon", fournisseur="google", cle="GEMINI_API_KEY_FREE", prix=(4.0, 20.0),
                   max=65536, provision=49152, niveau="high", payant=False, src_prix="prix_carbon_sortie",
                   src_reglage="col_carbon_provision"),
    "astra": dict(id="gpt-6.2-astra", fournisseur="openai", cle="OPENAI_API_KEY", prix=(10.0, 50.0),
                  max=32768, provision=0, payant=True, src_prix="prix_astra", src_reglage="astra_max_sortie"),
}

# relevé des journaux réels du collisionneur (sorties médianes, 90e centile ; caractères par jeton d'entrée) : espèce du
# relevé et tour pris comme analogue de chaque rôle ; Fable 5.1 lu sur le relevé de Fable 5.2 (même lignée ; illustratif)
ANALOGUE_RELEVE = {"opus": "opus", "fable51": "fable", "argon": "argon", "argon_court": "argon", "carbon": "carbon",
                   "astra": "astra"}

# Paramètres de la course (défauts du mandat ; « illustratif » quand aucune mesure ne les fonde)
DEFAUTS = dict(
    faits_car=10700,            # mandat (complément de la mère)
    question_car=15000,         # mandat (complément de la mère)
    temoins_car=1600,           # quatre questions témoins courtes, 4 × 400 caractères : illustratif
    temoins_sortie_att=1000,    # réponses et confiances des quatre témoins, jetons : illustratif
    temoins_sortie_haut=2000,   # illustratif
    cases=7,                    # un cas par point prioritaire de la demande reformulée (sept points) : proposition
    especes=("opus", "fable51", "argon", "astra", "carbon"),   # composition de la course v9 (configuration v5), sans Kimi
    carte_car=6000,             # taille d'une carte au gabarit de la demande reformulée : illustratif
    consigne_critique_car=3000,  # illustratif (consigne non écrite)
    consigne_lecteur_car=4000,   # illustratif (consigne non écrite)
    liste_lot_car=8000,          # liste d'un lecteur pour un cas : illustratif
    fiches_propositions=20,      # propositions passées à l'étage : proposition (au plus 12 fiches par étage)
    controles_caches=4,          # constructions déjà réfutées glissées en contrôles cachés : proposition
    temoins_tour_ferme=7,        # sept témoins par génération du tour fermé (T-VRAIE … T-MAL)
    heures_machine=(10.0, 24.0, 72.0),
    juge_argon=False,            # base : juge a priori unique (Opus) ; variante : + juge Argon (configuration v5)   # attendu (14 tests en 3 h 18 à la v67, mis à l'échelle), haut, pire (durée de l'étage)
)
# relances permises : une relance après panne technique (mot de Lazar, GO-2026-11-22-77) pour tout appel ; les appels de
# Google joués hors de l'orchestrateur par un script du type collisionneur ont deux relances (identique, puis finale)
R_ORCHESTRATEUR = 1
R_SCRIPT_GOOGLE = 2
R_SCRIPT_AUTRE = 1
EUR_PAR_HEURE_CPX32 = 0.235 / 4     # 3 h 18 min facturées 4 heures (dépenses, ligne de la v67) ; égal à la v66 (0,059)
USD_PAR_EUR = 1.25


def charger_releve(src_brut: bytes) -> dict:
    return json.loads(src_brut.decode("utf-8"))


def jetons_entree(car: float, cpj: float) -> float:
    return car / cpj


def pire_entree_jetons(car: float, octets_par_car: float) -> float:
    """Borne prudente du lanceur v9 : octets / 2."""
    return math.ceil(car * octets_par_car / 2.0)


def cout(m: dict, jin: float, jout: float) -> float:
    return jin / 1e6 * m["prix"][0] + jout / 1e6 * m["prix"][1]


def pire_appel(nom: str, car: float, opc: float) -> float:
    m = MODELES[nom]
    if m["fournisseur"] == "openai":   # formule de la commande d'Astra : (octets du corps + 1024) jetons au prix d'entrée
        return (car * opc + 1024) * m["prix"][0] / 1e6 + m["max"] * m["prix"][1] / 1e6
    # convention du collisionneur : entrée gardée, plus plafond de sortie ET provision de réflexion au prix de sortie
    return pire_entree_jetons(car, opc) * m["prix"][0] / 1e6 + (m["max"] + m["provision"]) * m["prix"][1] / 1e6


def poste(nom_poste, role, nom, appels, car_entree, tour, R, releve, opc, att=None, haut=None, pire=None, note=""):
    """Un poste : `appels` appels du rôle `role` par le modèle `nom`. Attendu : entrée / caractères par jeton médian,
    sortie médiane du relevé ; haut : entrée / caractères par jeton minimal, sortie au 90e centile ; pire : `pire_appel`.
    `att`, `haut`, `pire` imposés (par appel) quand le rôle a ses propres sources (aiguilleur, juges, étage)."""
    m = MODELES[nom]
    r = releve.get(f"{ANALOGUE_RELEVE.get(nom, nom)}|{tour}") if tour else None
    if att is None:
        att = cout(m, jetons_entree(car_entree, r["car_par_jeton_entree_med"]), r["sortie_med"])
    if haut is None:
        haut = cout(m, jetons_entree(car_entree, r["car_par_jeton_entree_min"]), r["sortie_p90"])
    if pire is None:
        pire = pire_appel(nom, car_entree, opc)
    return dict(poste=nom_poste, role=role, modele=m["id"], cle=m["cle"], payant=m["payant"], appels=appels,
                car_entree=round(car_entree), att_appel=att, haut_appel=haut, pire_appel=pire, relances=R,
                attendu=appels * att, haut=appels * haut, pire_compte=appels * pire * (1 + R),
                pire_paye=appels * pire * (1 + R) if m["payant"] else 0.0, note=note)


def calculer(p: dict, releve: dict, src: dict) -> dict:
    opc = src["demande_octets"]["octets"] / src["demande_octets"]["caracteres"]   # octets par caractère, mesuré
    consigne_prop = src["consigne_proposeur_v2"]["caracteres"]                    # borne : consigne v2 (29 299)
    dossier = p["faits_car"] + p["question_car"]
    n_cartes_cas = len(p["especes"]) * 2                                           # cartes_par_appel = 2 (configuration v5)
    postes = []
    for bras in ("principal", "temoin"):
        B = f"bras {bras}"
        # proposeurs (orchestrateur) : cases × espèces
        for e in p["especes"]:
            postes.append(poste(f"{B} : proposition", "proposeur", e, p["cases"], consigne_prop + dossier, "E3-T1",
                                R_ORCHESTRATEUR, releve, opc))
        # questions témoins (règle 2) : surcoût d'entrée et de sortie, mêmes appels ; le plafond de sortie ne change pas
        for e in p["especes"]:
            m = MODELES[e]
            r = releve[f"{ANALOGUE_RELEVE[e]}|E3-T1"]
            att = cout(m, p["temoins_car"] / r["car_par_jeton_entree_med"], p["temoins_sortie_att"])
            haut = cout(m, p["temoins_car"] / r["car_par_jeton_entree_min"], p["temoins_sortie_haut"])
            pire = (p["temoins_car"] * opc * m["prix"][0] / 1e6) if m["fournisseur"] == "openai" else \
                (math.ceil(p["temoins_car"] * opc / 2.0) * m["prix"][0] / 1e6)
            postes.append(poste(f"{B} : questions témoins (règle 2)", "proposeur (surcoût)", e, p["cases"], p["temoins_car"],
                                None, R_ORCHESTRATEUR, releve, opc, att=att, haut=haut, pire=pire,
                                note="plafond de sortie inchangé : le pire n'ajoute que l'entrée"))
        # critiques (hors orchestrateur v56 : rôle à jouer par un script du type collisionneur), deux familles
        car_crit = p["consigne_critique_car"] + dossier + n_cartes_cas * p["carte_car"]
        for e, R in (("opus", R_SCRIPT_AUTRE), ("carbon", R_SCRIPT_GOOGLE)):
            postes.append(poste(f"{B} : critiques", "critique", e, p["cases"], car_crit, "E3-T2", R, releve, opc))
        # aiguilleur et juges (orchestrateur ; le juge est rétrogradé en a priori, sans effet sur la sélection)
        n_cartes = p["cases"] * n_cartes_cas
        ag_haut = 20.46 / 110
        ju_haut = 47.322 / 220
        postes.append(poste(f"{B} : aiguillage", "aiguilleur", "opus", n_cartes, 0, None, R_ORCHESTRATEUR, releve, opc,
                            att=0.031, haut=ag_haut, pire=0.25))
        postes.append(poste(f"{B} : juges a priori", "juge", "opus", n_cartes, 0, None, R_ORCHESTRATEUR, releve, opc,
                            att=0.037, haut=ju_haut, pire=0.60))
        car_juge = 4273 + p["carte_car"]   # consigne du juge v1 (4 273 octets, ASCII) + une carte
        r_ar = releve["argon|E3-T1"]
        pire_juge_argon = pire_appel("argon_court", car_juge, opc)
        if p["juge_argon"]:   # variante : second juge (Argon) de la configuration v5 ; hors de la base recommandée
            postes.append(poste(
                f"{B} : juges a priori", "juge", "argon_court", n_cartes, car_juge, None, R_ORCHESTRATEUR,
                releve, opc, att=ju_haut,
                haut=cout(MODELES["argon_court"], car_juge / r_ar["car_par_jeton_entree_min"], r_ar["sortie_p90"]),
                pire=pire_juge_argon, note="réglage conforme à la garde : plafond de session du juge 0,60 → 1,00"))
        # lecture double à l'aveugle (règle 3) : chaque lecteur lit toutes les sorties ; un appel par cas, puis une synthèse
        car_lot = p["consigne_lecteur_car"] + dossier + n_cartes_cas * p["carte_car"]
        car_synth = p["consigne_lecteur_car"] + p["cases"] * p["liste_lot_car"]
        for e, R in (("opus", R_SCRIPT_AUTRE), ("carbon", R_SCRIPT_GOOGLE)):
            postes.append(poste(f"{B} : lecture double (règle 3)", "lecteur aveugle", e, p["cases"], car_lot, "E3-T3", R,
                                releve, opc))
            postes.append(poste(f"{B} : lecture double (règle 3)", "lecteur aveugle (synthèse)", e, 1, car_synth, "E3-T3",
                                R, releve, opc))
    # sondes du jour (format, avant la course) : un appel de chaque espèce de Google sur la plus grande entrée ; Astra 0,05
    for e in ("carbon", "argon"):
        postes.append(poste("sondes du jour", "sonde", e, 1, consigne_prop + dossier + p["temoins_car"], "E3-T1",
                            R_SCRIPT_GOOGLE, releve, opc))
    postes.append(poste("sondes du jour", "sonde", "astra", 1, 0, None, 0, releve, opc, att=0.05, haut=0.05, pire=0.05,
                        note="sonde d'Astra du devis v2i (≤ 0,05)"))
    # étage des tests de mort : mesure de l'expérimentateur sur les sept témoins du tour fermé (Sonnet, puis Opus en
    # repli mesuré), lecteur témoin Argon ; puis fiches des propositions et contrôles cachés
    n_t = p["temoins_tour_ferme"]
    exp_son = dict(att=0.081, haut=0.72, pire=0.80)
    exp_opus = dict(att=0.162, haut=1.44, pire=1.60)
    lect = dict(att=ju_haut, haut=cout(MODELES["argon_court"], 10000 / releve["argon|E3-T1"]["car_par_jeton_entree_min"],
                                        releve["argon|E3-T1"]["sortie_p90"]),
                pire=pire_appel("argon_court", 10000, opc))
    postes.append(poste("étage : mesure sur les témoins", "expérimentateur", "sonnet", n_t, 0, None, R_ORCHESTRATEUR,
                        releve, opc, **exp_son, note="plafond par fiche 0,80 (tour fermé v64)"))
    postes.append(poste("étage : mesure sur les témoins", "expérimentateur (repli mesuré)", "opus", n_t, 0, None,
                        R_ORCHESTRATEUR, releve, opc, **exp_opus, note="plafond par fiche proposé 1,60 (douze tours au tarif d'Opus)"))
    postes.append(poste("étage : mesure sur les témoins", "lecteur témoin", "argon_court", 2 * n_t, 10000, None,
                        R_ORCHESTRATEUR, releve, opc, **lect, note="plafond du lecteur 0,10 → 1,00 (garde Google)"))
    n_f = p["fiches_propositions"] + p["controles_caches"]
    postes.append(poste("étage : propositions et contrôles cachés", "expérimentateur", "sonnet", n_f, 0, None,
                        R_ORCHESTRATEUR, releve, opc, att=exp_son["att"], haut=exp_son["haut"], pire=exp_opus["pire"],
                        note="pire au plafond d'Opus : couvre le repli"))
    postes.append(poste("étage : propositions et contrôles cachés", "lecteur témoin", "argon_court", n_f, 10000, None,
                        R_ORCHESTRATEUR, releve, opc, **lect))
    # machine louée de l'étage (bac à sable réel) : Hetzner cpx32 hel1
    h_att, h_haut, h_pire = p["heures_machine"]
    usd_h = EUR_PAR_HEURE_CPX32 * USD_PAR_EUR
    postes.append(dict(poste="étage : machine louée", role="bac à sable", modele="Hetzner cpx32 hel1", cle="HCLOUD_TOKEN",
                       payant=True, appels=0, car_entree=0, att_appel=usd_h, haut_appel=usd_h, pire_appel=usd_h, relances=0,
                       attendu=math.ceil(h_att) * usd_h, haut=math.ceil(h_haut) * usd_h, pire_compte=math.ceil(h_pire) * usd_h,
                       pire_paye=math.ceil(h_pire) * usd_h, note="heures facturées entamées"))
    return dict(postes=postes, octets_par_caractere=opc, consigne_proposeur_car=consigne_prop, dossier_car=dossier,
                cartes_par_cas=n_cartes_cas, fiches_etage=n_f, etages_de_12=math.ceil(n_f / 12), usd_par_heure=usd_h)


def sommes(postes, filtre=lambda x: True):
    s = {k: 0.0 for k in ("attendu", "haut", "pire_compte", "pire_paye")}
    s["attendu_paye"] = 0.0
    s["haut_paye"] = 0.0
    for x in postes:
        if filtre(x):
            for k in ("attendu", "haut", "pire_compte", "pire_paye"):
                s[k] += x[k]
            if x["payant"]:
                s["attendu_paye"] += x["attendu"]
                s["haut_paye"] += x["haut"]
    return s


# ---------------------------------------------------------------------------------------------------------------------------
# 3. Garde de Google : les corps proposés passent, les réglages de la course v9 sont refusés.
# ---------------------------------------------------------------------------------------------------------------------------
def charger_garde():
    spec = importlib.util.spec_from_file_location("garde_google_v3", DEPOT / P_GARDE)
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    return g


def corps(maxi, pensee):
    return {"contents": [{"role": "user", "parts": [{"text": "x"}]}],
            "generationConfig": {"maxOutputTokens": maxi, "thinkingConfig": pensee}}


def controler_garde(g) -> dict:
    mots = 3500   # limite de mots à écrire dans la consigne servie à Google (2 cartes ≈ 2 × 6 000 caractères ≈ 2 000 mots)
    mots_court = 1500   # juge et lecteur témoin : verdict court ; 1 500 × 5,1 = 7 650 < 16 384
    acceptes = {
        "carbon (proposeur, critique, lecteur)": ("carbon", corps(65536, {"thinkingLevel": "high", "includeThoughts": True}), 49152, mots),
        "argon (proposeur)": ("argon", corps(65536, {"thinkingLevel": "high", "includeThoughts": True}), 16384, mots),
        "argon (juge, lecteur témoin)": ("argon", corps(32768, {"thinkingLevel": "high", "includeThoughts": True}), 16384, mots_court),
    }
    refuses = {
        "carbon v9 : sans réglage de réflexion, 65 536 non diffusé": ("carbon", corps(65536, {}), 65536, "non_diffuse"),
        "argon juge v9 : budget de réflexion 8 192": ("argon", corps(65536, {"thinkingBudget": 8192}), 8192, "non_diffuse"),
        "carbon : plafond étroit (2 048, niveau bas)": ("carbon", corps(2048, {"thinkingLevel": "low", "includeThoughts": True}), 1024, "flux"),
        "argon juge sous 0,60 USD (sortie 8 000)": ("argon", corps(8000, {"thinkingLevel": "high", "includeThoughts": True}), 4096, "flux"),
    }
    res = {"acceptes": {}, "refuses": {}}
    for nom, (esp, c, prov, n_mots) in acceptes.items():
        pb = g.verifier_reglages_google(esp, c, prov, mots=n_mots, mode="flux")
        res["acceptes"][nom] = pb
        if pb:
            raise Arret(f"garde Google : le réglage proposé « {nom} » est refusé : {pb}")
    for nom, (esp, c, prov, mode) in refuses.items():
        pb = g.verifier_reglages_google(esp, c, prov, mots=mots, mode=mode)
        res["refuses"][nom] = pb
        if not pb:
            raise Arret(f"garde Google : le réglage fautif « {nom} » passe la garde")
    if g.defaut_reponse_google("STOP", "texte", 0) != g.STATUT_SANS_PENSEES:
        raise Arret("garde Google : une réponse sans pensée n'est pas refusée")
    if g.defaut_reponse_google("MAX_TOKENS", "", 100) != "MAX_TOKENS":
        raise Arret("garde Google : une fin en MAX_TOKENS n'est pas refusée")
    res["mots"] = {"proposeur, critique, lecteur": mots, "juge, lecteur témoin": mots_court}
    return res


# ---------------------------------------------------------------------------------------------------------------------------
def fmt(x):
    return f"{x:,.2f}".replace(",", " ").replace(".", ",")


def principal(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--faits-car", type=int, default=DEFAUTS["faits_car"])
    a.add_argument("--question-car", type=int, default=DEFAUTS["question_car"])
    a.add_argument("--cases", type=int, default=DEFAUTS["cases"])
    a.add_argument("--fiches-propositions", type=int, default=DEFAUTS["fiches_propositions"])
    a.add_argument("--controles-caches", type=int, default=DEFAUTS["controles_caches"])
    a.add_argument("--juge-argon", action="store_true", help="variante : second juge a priori (Argon) dans les totaux")
    a.add_argument("--json", action="store_true", help="sortie JSON seule")
    args = a.parse_args(argv)
    p = dict(DEFAUTS, faits_car=args.faits_car, question_car=args.question_car, cases=args.cases,
             fiches_propositions=args.fiches_propositions, controles_caches=args.controles_caches, juge_argon=args.juge_argon)
    try:
        src = resoudre_sources()
        releve = charger_releve(lire_source(P_RELEVE))
        c = calculer(p, releve, src)
        garde = controler_garde(charger_garde())
    except Arret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 2 if "source" in str(e) else 3
    P = c["postes"]
    tot = sommes(P)
    princ = sommes(P, lambda x: not x["poste"].startswith("bras temoin"))
    sans_temoin = princ
    temoin = sommes(P, lambda x: x["poste"].startswith("bras temoin"))
    organisme_princ = sommes(P, lambda x: x["poste"].startswith("bras principal"))
    etage = sommes(P, lambda x: x["poste"].startswith("étage"))
    par_cle = {}
    for x in P:
        d = par_cle.setdefault(x["cle"], {"attendu": 0.0, "haut": 0.0, "pire_compte": 0.0, "pire_paye": 0.0})
        for k in d:
            d[k] += x[k]
    par_poste = {}
    for x in P:
        d = par_poste.setdefault(x["poste"], {"attendu": 0.0, "haut": 0.0, "pire_compte": 0.0, "pire_paye": 0.0,
                                               "attendu_paye": 0.0, "haut_paye": 0.0})
        for k in ("attendu", "haut", "pire_compte", "pire_paye"):
            d[k] += x[k]
        if x["payant"]:
            d["attendu_paye"] += x["attendu"]
            d["haut_paye"] += x["haut"]
    # plafonds : par clé payante, le haut payé de la clé plus un tiers, aux 5 USD supérieurs (borne du relais de la clé ; le
    # relais arrête au plafond) ; clé gratuite : arrêt au premier appel facturé (payé 0). Plafond d'arrêt payé = somme.
    def plafonds_par_cle(postes):
        out = {}
        for x in postes:
            if x["payant"]:
                out[x["cle"]] = out.get(x["cle"], 0.0) + x["haut"]
        return {k: math.ceil(v * 4 / 3 / 5) * 5 for k, v in out.items()}
    caps = plafonds_par_cle(P)
    caps_sans_temoin = plafonds_par_cle([x for x in P if not x["poste"].startswith("bras temoin")])
    plafond = sum(caps.values())
    plafond_sans_temoin = sum(caps_sans_temoin.values())
    plafond_pour_pire = math.ceil(tot["pire_paye"] / 10) * 10
    pire_sans_relance = sum(x["pire_compte"] / (1 + x["relances"]) for x in P)
    pire_paye_sans_relance = sum(x["pire_paye"] / (1 + x["relances"]) for x in P)
    pire_tenu = {k: min(par_cle[k]["pire_paye"], v) for k, v in caps.items()}
    # seuils internes : plafond dur par étape (payé), haut payé de l'étape plus un tiers, au dollar supérieur
    etapes = {"proposition et questions témoins (deux bras)": ("proposition", "questions témoins"), "critiques (deux bras)": ("critiques",),
              "aiguillage et juge a priori (deux bras)": ("aiguillage", "juges"), "lecture double (deux bras)": ("lecture",),
              "sondes du jour": ("sondes",), "étage : mesure sur les témoins": ("mesure sur les témoins",),
              "étage : propositions et contrôles cachés": ("propositions et contrôles",), "étage : machine louée": ("machine",)}
    seuils = {}
    for nom_e, mots_e in etapes.items():
        hp = sum(x["haut"] for x in P if x["payant"] and any(m in x["poste"] for m in mots_e))
        ap = sum(x["attendu"] for x in P if x["payant"] and any(m in x["poste"] for m in mots_e))
        seuils[nom_e] = {"attendu_paye": ap, "haut_paye": hp, "plafond_dur": math.ceil(hp * 4 / 3)}
    variante = None
    if not p["juge_argon"]:
        cv = calculer(dict(p, juge_argon=True), releve, src)
        tv = sommes(cv["postes"])
        variante = {k: tv[k] - tot[k] for k in tot}
    resultat = dict(version=VERSION, parametres={k: v for k, v in p.items()}, sources=src, calcul={k: v for k, v in c.items()
                    if k != "postes"}, postes=P, par_poste=par_poste, par_cle=par_cle, totaux=dict(
                        tout=tot, sans_bras_temoin=sans_temoin, bras_temoin=temoin, organisme_bras_principal=organisme_princ,
                        etage=etage), plafonds_par_cle=caps, plafonds_par_cle_sans_bras_temoin=caps_sans_temoin,
                    plafond_recommande_paye=plafond, plafond_sans_bras_temoin=plafond_sans_temoin,
                    pire_paye_brut_sous_plafond=tot["pire_paye"] <= plafond, plafond_qui_couvre_le_pire_paye_brut=plafond_pour_pire,
                    pire_tenu_par_les_plafonds=pire_tenu, pire_compte_sans_relance=pire_sans_relance,
                    pire_paye_sans_relance=pire_paye_sans_relance, seuils_internes=seuils, variante_juge_argon_en_plus=variante,
                    garde_google=garde)
    if args.json:
        print(json.dumps(resultat, ensure_ascii=False, indent=1, default=str))
        return 0
    print(f"{VERSION} — calcul hors ligne, aucun appel. Dépôt : {DEPOT}")
    print("\n== 1. Sources (fichier, ligne, empreinte) ==")
    for k in SOURCES:
        print(f"  {k:32s} {ref(src, k)}")
    print(f"\n  octets par caractère (mesurés sur la demande reformulée) : {c['octets_par_caractere']:.4f}")
    print(f"  consigne du proposeur (borne : consigne v2 de l'auto-conception) : {c['consigne_proposeur_car']} caractères")
    print(f"  dossier servi : faits {p['faits_car']} + question {p['question_car']} = {c['dossier_car']} caractères ; "
          f"questions témoins {p['temoins_car']} ; cas {p['cases']} ; cartes par cas {c['cartes_par_cas']}")
    print(f"  étage : {c['fiches_etage']} fiches de propositions et contrôles cachés, soit {c['etages_de_12']} étages de 12 au plus")
    print("\n== 2. Postes (USD) ==")
    print("  poste | rôle | modèle | clé | appels | entrée (car.) | par appel att / haut / pire | relances | attendu | haut | pire compté | pire payé")
    for x in P:
        print(f"  {x['poste']} | {x['role']} | {x['modele']} | {x['cle']} | {x['appels']} | {x['car_entree']} | "
              f"{x['att_appel']:.4f} / {x['haut_appel']:.4f} / {x['pire_appel']:.4f} | {x['relances']} | {fmt(x['attendu'])} | "
              f"{fmt(x['haut'])} | {fmt(x['pire_compte'])} | {fmt(x['pire_paye'])}" + (f" | {x['note']}" if x['note'] else ""))
    print("\n== 3. Par poste ==")
    print("  poste | attendu (payé) | haut (payé) | pire compté | pire payé")
    for k, d in par_poste.items():
        print(f"  {k} | {fmt(d['attendu'])} ({fmt(d['attendu_paye'])}) | {fmt(d['haut'])} ({fmt(d['haut_paye'])}) | "
              f"{fmt(d['pire_compte'])} | {fmt(d['pire_paye'])}")
    print("\n== 4. Par clé ==")
    for k, d in par_cle.items():
        print(f"  {k} | attendu {fmt(d['attendu'])} | haut {fmt(d['haut'])} | pire compté {fmt(d['pire_compte'])} | "
              f"pire payé {fmt(d['pire_paye'])}")
    print("\n== 5. Totaux ==")
    for nom, s in (("organisme, bras principal", organisme_princ), ("bras témoin (règle 5)", temoin), ("étage des tests de mort", etage),
                   ("tout sans le bras témoin", sans_temoin), ("tout", tot)):
        print(f"  {nom} : attendu {fmt(s['attendu'])} (payé {fmt(s['attendu_paye'])}) ; haut {fmt(s['haut'])} "
              f"(payé {fmt(s['haut_paye'])}) ; pire compté {fmt(s['pire_compte'])} ; pire payé {fmt(s['pire_paye'])}")
    print(f"\n  pire compté sans relance : {fmt(pire_sans_relance)} ; pire payé sans relance : {fmt(pire_paye_sans_relance)}")
    print("\n== 6. Plafonds et seuils ==")
    print("  plafond par clé payante (haut payé de la clé × 4/3, aux 5 USD supérieurs) ; GEMINI_API_KEY_FREE : arrêt au premier appel facturé")
    for k, v in caps.items():
        print(f"  {k} : {v} USD (sans le bras témoin : {caps_sans_temoin.get(k)}) ; pire payé brut {fmt(par_cle[k]['pire_paye'])} ; "
              f"tenu par le plafond {fmt(pire_tenu[k])}")
    print(f"  plafond d'arrêt recommandé (payé, somme des plafonds) : {plafond} USD ; sans le bras témoin : {plafond_sans_temoin} USD")
    print(f"  pire payé tenu par les plafonds, avec le bras témoin : {fmt(sum(pire_tenu.values()))} USD (≤ {plafond} : par construction)")
    print(f"  pire payé brut avec le bras témoin ({fmt(tot['pire_paye'])}) sous le plafond : {'oui' if tot['pire_paye'] <= plafond else 'non'} ; "
          f"plafond qui le couvrirait : {plafond_pour_pire} USD")
    print("  seuils internes (plafond dur par étape, payé, haut × 4/3 au dollar supérieur) :")
    for k, d in seuils.items():
        print(f"    {k} : attendu payé {fmt(d['attendu_paye'])} ; haut payé {fmt(d['haut_paye'])} ; plafond dur {d['plafond_dur']}")
    if variante:
        print(f"  variante « juge Argon en plus » (configuration v5) : attendu +{fmt(variante['attendu'])} ; haut +{fmt(variante['haut'])} ; "
              f"pire compté +{fmt(variante['pire_compte'])} ; pire payé +{fmt(variante['pire_paye'])}")
    print("\n== 7. Garde de Google (src/controle_ia/garde_google_v3.py) ==")
    print(f"  limite de mots servie à Google : {garde['mots']}")
    for nom, pb in garde["acceptes"].items():
        print(f"  accepté : {nom} : {pb or 'aucun problème'}")
    for nom, pb in garde["refuses"].items():
        print(f"  refusé  : {nom} : {pb}")
    print("  réponses : zéro pensée → SANS_PENSEES ; fin MAX_TOKENS → défaut (vérifiés)")
    return 0


if __name__ == "__main__":
    sys.exit(principal())
