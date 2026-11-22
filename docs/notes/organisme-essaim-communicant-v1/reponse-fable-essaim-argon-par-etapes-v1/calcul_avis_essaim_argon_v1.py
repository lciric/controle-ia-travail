"""Calculs de l'avis rendu sur le mandat « essai en essaim de l'organisme avec Argon, par étapes » — v1.

Écrit le 22 novembre 2026 par la session fille mandatée (abonnement), pour le mandat
docs/notes/organisme-essaim-communicant-v1/mandats-fable-abonnement-v1/mandat-fable-essaim-argon-par-etapes-v1.md
(93bec410…). Pièce de calcul, à contre-lire.

Sans réseau, sans clé, sans dépense, bibliothèque standard seule. Aucun tirage aléatoire : la sortie est la même à
l'octet à chaque rejeu (pas d'horodatage dans la sortie).

Emploi :
    python3 calcul_avis_essaim_argon_v1.py SORTIE.json [--garde CHEMIN/garde_google_v3.py]

Avec --garde, la garde de Google v3 est chargée APRÈS vérification de son empreinte (923679b5…, branche main) et
exécutée sur les réglages proposés par l'avis. Sans --garde, la sortie dit en clair « non exécutée » : aucun repli
silencieux (R5).

Statut des entrées : les tarifs et les hypothèses de volume viennent du mandat (non vérifiés sur pièce primaire) ; les
scénarios « prévision de l'avis » et « prudent » sont des hypothèses de l'avis ; le nombre de requêtes par monde (62) est
une lecture de 744 = 12 × 62, à confirmer par l'organisme.
"""
import argparse
import datetime
import hashlib
import importlib.util
import json
import math
import sys

EMPREINTE_GARDE_V3 = "923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91"

# Tarifs d'Argon, USD par million de jetons (mandat, tableau du devis préliminaire ; non vérifiés sur pièce primaire).
TARIFS = {"novembre": {"entree": 2.0, "sortie": 10.0}, "decembre": {"entree": 4.0, "sortie": 20.0}}

N_PILOTE = 748      # rapport v5 : 748 requêtes pour 748 réserves
N_QUART = 187       # mandat : 748 / 4
N_MONDE = 62        # lecture : 744 appels / 12 mondes (à confirmer : 748 n'est pas divisible par 12)
PLAFOND_FLUX = 65536        # garde v3 : limite de sortie d'Argon en flux
PLAFOND_NON_DIFFUSE = 32768  # garde v3 : limite de sortie d'Argon hors flux
TEXTE_MIN = 16000           # garde v3 : jetons de texte au moins
JETONS_PAR_MOT_ARGON = 5.1  # garde v3 : plus haut mesuré pour Argon, arrondi au dixième supérieur
BUDGET_REPLI_ARGON = 16384  # garde v3 : « supposé »
OCTETS_MAX = 64960          # lecture du cas d'artefact « 64 961 octets » du rapport v5 (à confirmer)
MISE_EN_FORME = 256         # H3 de la liste « à faire » : 256 jetons de mise en forme (établi pour Kimi, pas pour Argon)
ENTREE_PIRE = OCTETS_MAX + MISE_EN_FORME  # 65 216 jetons si « un jeton couvre au moins un octet » tient pour Argon

# Scénarios par requête : (jetons d'entrée, jetons de sortie réflexion comprise).
SCENARIOS = {
    "attendu_organisme": (10000, 8000),
    "haut_organisme": (20000, 16000),
    "prevision_avis": (25000, 15000),
    "prudent": (40000, 32768),
    "pire_enonce_organisme": (20000, PLAFOND_FLUX),
    "pire_plafond_et_octets": (ENTREE_PIRE, PLAFOND_FLUX),
}
TABLE_ORGANISME = {"novembre": {"attendu": 75, "haut": 150, "pire": 526},
                   "decembre": {"attendu": 150, "haut": 299, "pire": 1052}}

BORNES = {"novembre": {"fumee": 5.0, "premier_monde": 20.0, "quart": 60.0},
          "decembre": {"fumee": 10.0, "premier_monde": 40.0, "quart": 120.0}}  # en décembre, chaque borne double
PLAFOND_ESSAI_COUPURE = 16001  # essai de coupure au plafond : provision déclarée de 1 jeton, plafond de 16 001
BASCULE_TARIF_AU_PLUS_TOT = datetime.datetime(2026, 11, 30, 10, 0, 0, tzinfo=datetime.timezone.utc)  # minuit, UTC+14


def cout(entree, sortie, tarif):
    """Coût d'une requête en USD."""
    return (entree * tarif["entree"] + sortie * tarif["sortie"]) / 1e6


def arrondi(x, chiffres=6):
    return round(float(x), chiffres)


def loi_binomiale_cumul(k, n, p):
    """P(X ≤ k) pour X binomiale (n, p), calcul exact par somme."""
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(0, k + 1))


def proba_suite(n, p, longueur=3):
    """Probabilité d'au moins une suite de `longueur` succès consécutifs en n épreuves de Bernoulli(p)."""
    etats = [1.0] + [0.0] * (longueur - 1)  # etats[j] : j succès consécutifs en cours, sans suite atteinte
    for _ in range(n):
        nouveaux = [0.0] * longueur
        for j, masse in enumerate(etats):
            nouveaux[0] += masse * (1 - p)
            if j + 1 < longueur:
                nouveaux[j + 1] += masse * p
        etats = nouveaux
    return 1.0 - sum(etats)


def mots_max(plafond, provision, jetons_par_mot):
    """Plus grande limite de mots admise par la règle (3) de la garde : ⌈mots × rapport⌉ < plafond − provision."""
    texte = plafond - provision
    mots = int(texte / jetons_par_mot) + 2
    while mots > 0 and math.ceil(mots * jetons_par_mot) >= texte:
        mots -= 1
    return mots


def executer_garde(chemin):
    """Charge la garde v3 après vérification de son empreinte et l'exécute sur les réglages proposés."""
    with open(chemin, "rb") as f:
        octets = f.read()
    empreinte = hashlib.sha256(octets).hexdigest()
    if empreinte != EMPREINTE_GARDE_V3:
        raise SystemExit(f"garde : empreinte {empreinte} ≠ {EMPREINTE_GARDE_V3} ; rien n'est exécuté")
    spec = importlib.util.spec_from_file_location("garde_google_v3", chemin)
    garde = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(garde)

    def corps(plafond, niveau=None, budget=None, pensees=True):
        pensee = {"includeThoughts": pensees}
        if niveau is not None:
            pensee["thinkingLevel"] = niveau
        if budget is not None:
            pensee["thinkingBudget"] = budget
        return {"contents": [], "generationConfig": {"maxOutputTokens": plafond, "thinkingConfig": pensee}}

    v = garde.verifier_reglages_google
    avant = {
        "pilote_high_65536_provision_49536_mots_3137_flux": v("argon", corps(65536, "high"), 49536, mots=3137),
        "pilote_mots_3138_refuse": v("argon", corps(65536, "high"), 49536, mots=3138),
        "pilote_hors_flux_refuse": v("argon", corps(65536, "high"), 49536, mots=3137, mode="non_diffuse"),
        "essai_coupure_16001_provision_1": v("argon", corps(16001, "high"), 1),
        "plafond_16000_provision_1_refuse": v("argon", corps(16000, "high"), 1),
        "niveau_medium_sans_declaration_refuse": v("argon", corps(65536, "medium"), 49536, mots=3137),
        "niveau_medium_declare": v("argon", corps(65536, "medium"), 49536, mots=3137, niveau_attendu="medium"),
        "repli_budget_16384_declare": v("argon", corps(65536, budget=16384), 49536, mots=3137, budget_attendu=16384),
        "niveau_et_budget_refuse": v("argon", corps(65536, "high", 16384), 49536, mots=3137),
        "pensees_non_demandees_refuse": v("argon", corps(65536, "high", pensees=False), 49536, mots=3137),
        "sans_reglage_de_reflexion_refuse": v("argon", {"generationConfig": {"maxOutputTokens": 65536}}, 49536),
    }
    d = garde.defaut_reponse_google
    apres = {
        "STOP_texte_1200_pensees": d("STOP", "texte", 1200),
        "MAX_TOKENS": d("MAX_TOKENS", "texte", 100),
        "STOP_texte_vide": d("STOP", "  ", 100),
        "STOP_zero_pensee": d("STOP", "texte", 0),
        "STOP_pensees_absentes": d("STOP", "texte", None),
        "SAFETY": d("SAFETY", "", 0),
        "RECITATION": d("RECITATION", "texte", 10),
        "fin_absente": d(None, "texte", 10),
        "invite_bloquee": d("STOP", "texte", 10, blocage="PROHIBITED_CONTENT"),
    }
    refus = {
        "400_qui_nomme_le_niveau": garde.niveau_refuse("HTTP 400 : thinking_level 'high' is not supported"),
        "400_autre": garde.niveau_refuse("HTTP 400 : maxOutputTokens out of range"),
        "429": garde.niveau_refuse("HTTP 429 : quota exceeded"),
    }
    return {"executee": True, "empreinte": empreinte, "version": garde.VERSION_GARDE, "avant_envoi": avant,
            "apres_reponse": apres, "niveau_refuse": refus,
            "tables": {"niveau_max_argon": garde.NIVEAU_MAX_REFLEXION["argon"],
                       "limites_sortie_argon": garde.LIMITES_SORTIE["argon"],
                       "jetons_par_mot_argon": garde.JETONS_PAR_MOT_MESURES["argon"],
                       "budget_repli_argon": garde.BUDGETS_REPLI["argon"], "texte_min": garde.TEXTE_MIN_GOOGLE}}


def calculer(chemin_garde=None):
    s = {}
    # 1. Coût par requête et par étape, par scénario et par tarif.
    par_requete = {}
    for nom, (entree, sortie) in SCENARIOS.items():
        par_requete[nom] = {"entree": entree, "sortie": sortie}
        for mois, tarif in TARIFS.items():
            c = cout(entree, sortie, tarif)
            par_requete[nom][mois] = {"par_requete": arrondi(c), "premier_monde_62": arrondi(c * N_MONDE, 2),
                                      "quart_187": arrondi(c * N_QUART, 2), "pilote_748": arrondi(c * N_PILOTE, 2)}
    s["scenarios"] = par_requete

    # 2. Contrôle du tableau de l'organisme.
    controle = {}
    for mois, tarif in TARIFS.items():
        attendu = cout(10000, 8000, tarif) * N_PILOTE
        haut = cout(20000, 16000, tarif) * N_PILOTE
        pire = cout(20000, PLAFOND_FLUX, tarif) * N_PILOTE
        table = TABLE_ORGANISME[mois]
        entree_impliquee = (table["pire"] / N_PILOTE - PLAFOND_FLUX * tarif["sortie"] / 1e6) / (tarif["entree"] / 1e6)
        controle[mois] = {
            "attendu": {"table": table["attendu"], "recalcul": arrondi(attendu, 2)},
            "haut": {"table": table["haut"], "recalcul": arrondi(haut, 2)},
            "pire": {"table": table["pire"], "recalcul_entree_20000": arrondi(pire, 2),
                     "ecart": arrondi(table["pire"] - pire, 2),
                     "entree_impliquee_par_la_table": arrondi(entree_impliquee, 0),
                     "recalcul_entree_24001": arrondi(cout(24001, PLAFOND_FLUX, tarif) * N_PILOTE, 2),
                     "recalcul_borne_d_octets_65216": arrondi(cout(ENTREE_PIRE, PLAFOND_FLUX, tarif) * N_PILOTE, 2)},
        }
    controle["quart_attendu_novembre"] = arrondi(cout(10000, 8000, TARIFS["novembre"]) * N_QUART, 2)
    s["controle_table_organisme"] = controle

    # 3. Essai de fumée : quatre appels normaux, un essai de coupure au plafond (16 001), une requête coupée par le client.
    fumee = {}
    for mois, tarif in TARIFS.items():
        reserve = cout(ENTREE_PIRE, PLAFOND_FLUX, tarif)
        reserve_coupure = cout(ENTREE_PIRE, PLAFOND_ESSAI_COUPURE, tarif)
        pire = 5 * reserve + reserve_coupure
        lignes = {}
        for nom in ("attendu_organisme", "haut_organisme", "prevision_avis", "prudent"):
            entree, sortie = SCENARIOS[nom]
            lignes[nom] = arrondi(4 * cout(entree, sortie, tarif) + cout(entree, PLAFOND_ESSAI_COUPURE, tarif) + reserve, 4)
        fumee[mois] = {"reserve_par_appel_normal": arrondi(reserve), "reserve_essai_coupure": arrondi(reserve_coupure),
                       "somme_des_reserves_pire": arrondi(pire, 4), "borne": BORNES[mois]["fumee"],
                       "borne_couvre_le_pire": BORNES[mois]["fumee"] >= pire,
                       "compte_attendu_requete_coupee_a_sa_reserve": lignes}
    s["fumee"] = fumee

    # 4. Bornes du quart : jusqu'à quel coût moyen la borne laisse finir (réserve écrite avant chaque appel).
    bornes = {}
    for mois, tarif in TARIFS.items():
        reserve = cout(ENTREE_PIRE, PLAFOND_FLUX, tarif)
        b = {}
        for nom, n, borne in (("premier_monde", N_MONDE, BORNES[mois]["premier_monde"]),
                              ("quart", N_QUART, BORNES[mois]["quart"])):
            moyen = (borne - reserve) / (n - 1)
            b[nom] = {"requetes": n, "borne": borne, "cout_moyen_max_pour_finir": arrondi(moyen),
                      "sortie_moyenne_max_si_entree": {
                          str(e): arrondi((moyen - e * tarif["entree"] / 1e6) / (tarif["sortie"] / 1e6), 0)
                          for e in (10000, 25000, 40000)},
                      "requetes_garanties_au_pire": int(borne // reserve),
                      "pire_sans_borne": arrondi(n * reserve, 2)}
        b["pilote_pire_sans_borne"] = arrondi(N_PILOTE * reserve, 2)
        b["devis_pilote_selon_cout_moyen_mesure"] = {
            str(m): {"devis": arrondi(N_PILOTE * m * (tarif["sortie"] / 10.0), 2),
                     "plafond_1_3": math.ceil(1.3 * N_PILOTE * m * (tarif["sortie"] / 10.0))}
            for m in (0.10, 0.15, 0.20, 0.25, 0.318356)}  # m : coût moyen mesuré au tarif de novembre
        bornes[mois] = b
    s["bornes"] = bornes

    # 5. Critères de passage : ce que les seuils distinguent (loi binomiale exacte).
    s["criteres"] = {
        "defauts_au_plus_9_sur_187": {str(p): arrondi(loi_binomiale_cumul(9, N_QUART, p), 4)
                                      for p in (0.01, 0.02, 0.03, 0.05, 0.075, 0.10, 0.15)},
        "coupures_au_plafond_au_plus_3_sur_187": {str(p): arrondi(loi_binomiale_cumul(3, N_QUART, p), 4)
                                                  for p in (0.005, 0.01, 0.02, 0.03, 0.05)},
        "arret_si_7_defauts_ou_plus_sur_62": {str(p): arrondi(1 - loi_binomiale_cumul(6, N_MONDE, p), 4)
                                              for p in (0.02, 0.05, 0.10, 0.20, 0.30)},
        "borne_haute_95_si_zero_defaut": {str(n): arrondi(1 - 0.05 ** (1 / n), 4) for n in (4, 6, 62, 187, 748)},
        "echecs_toleres_a_10_pour_cent": {"748": math.floor(0.1 * N_PILOTE), "187": math.floor(0.1 * N_QUART),
                                          "62": math.floor(0.1 * N_MONDE)},
        "trois_defauts_de_suite_du_meme_type": {
            str(n): {str(p): arrondi(proba_suite(n, p, 3), 5) for p in (0.01, 0.02, 0.05, 0.10)}
            for n in (N_MONDE, N_QUART, N_PILOTE)},
        "cinq_defauts_de_suite": {
            str(n): {str(p): arrondi(proba_suite(n, p, 5), 6) for p in (0.02, 0.05, 0.10, 0.20)}
            for n in (N_QUART, N_PILOTE)},
        # Critère retenu pour le passage du quart au pilote : au plus 4 appels sur 187 dont les cartes sont perdues.
        "appels_a_cartes_perdues_au_plus_4_sur_187": {str(p): arrondi(loi_binomiale_cumul(4, N_QUART, p), 4)
                                                     for p in (0.005, 0.01, 0.02, 0.03, 0.05, 0.10)},
        # Cartes perdues sur douze mondes selon le taux de perte, face à la marge de +24 de la garde du total apparié
        # (lecture : 48 cartes par monde pour le bras (a), 52 pour le bras (c) ; à confirmer par l'organisme).
        "cartes_perdues_sur_douze_mondes": {
            bras: {"cartes": cartes * 12, "marge_de_la_garde": 24,
                   "perdues_selon_taux": {str(t): arrondi(cartes * 12 * t, 1) for t in (0.01, 0.02, 0.05, 0.10)},
                   "taux_qui_mange_la_moitie_de_la_marge": arrondi(12 / (cartes * 12), 4),
                   "taux_qui_mange_toute_la_marge": arrondi(24 / (cartes * 12), 4)}
            for bras, cartes in (("a", 48), ("c", 52))},
    }

    # 5 bis. Où la course s'arrête sous le scénario « prudent » (réserve écrite avant chaque appel, borne du premier monde).
    arrets = {}
    for mois, tarif in TARIFS.items():
        reserve = cout(ENTREE_PIRE, PLAFOND_FLUX, tarif)
        c = cout(*SCENARIOS["prudent"], tarif)
        borne = BORNES[mois]["premier_monde"]
        faits = 0
        while faits < N_MONDE and faits * c + reserve <= borne:
            faits += 1
        arrets[mois] = {"requetes_faites": faits, "depense_comptee": arrondi(faits * c, 2), "borne": borne}
    s["arret_premier_monde_scenario_prudent"] = arrets

    # 5 ter. Cumul du plan (fumée, quart, pilote), selon que le pilote court en novembre ou en décembre.
    cumul = {}
    nov, dec = TARIFS["novembre"], TARIFS["decembre"]
    for nom in ("attendu_organisme", "haut_organisme", "prevision_avis"):
        entree, sortie = SCENARIOS[nom]
        fumee_nov = (4 * cout(entree, sortie, nov) + cout(entree, PLAFOND_ESSAI_COUPURE, nov)
                     + cout(ENTREE_PIRE, PLAFOND_FLUX, nov))
        quart_nov = N_QUART * cout(entree, sortie, nov)
        cumul[nom] = {
            "fumee_et_quart_en_novembre": arrondi(fumee_nov + quart_nov, 2),
            "tout_en_novembre": arrondi(fumee_nov + quart_nov + N_PILOTE * cout(entree, sortie, nov), 2),
            "pilote_en_decembre": arrondi(fumee_nov + quart_nov + N_PILOTE * cout(entree, sortie, dec), 2),
            "surcout_du_pilote_en_decembre": arrondi(N_PILOTE * (cout(entree, sortie, dec) - cout(entree, sortie, nov)), 2),
        }
    s["cumul_du_plan"] = cumul

    # 6. Arithmétique de la garde v3 pour Argon.
    provision = PLAFOND_FLUX - TEXTE_MIN
    s["garde"] = {
        "provision_max_en_flux": provision,
        "provision_max_hors_flux": PLAFOND_NON_DIFFUSE - TEXTE_MIN,
        "mots_max_si_provision_49536": mots_max(PLAFOND_FLUX, provision, JETONS_PAR_MOT_ARGON),
        "provision_selon_limite_de_mots": {
            str(m): min(provision, PLAFOND_FLUX - math.ceil(m * JETONS_PAR_MOT_ARGON) - 1)
            for m in (2000, 3137, 3500, 4000, 6000)},
        "plafond_minimal_au_repli_budget": BUDGET_REPLI_ARGON + TEXTE_MIN,
        "rapport_plafond_argon_sur_plafond_kimi_24000": arrondi(PLAFOND_FLUX / 24000, 3),
        "execution": executer_garde(chemin_garde) if chemin_garde else
        {"executee": False, "motif": "option --garde non donnée : réglages non passés dans la garde"},
    }

    # 7. Durée d'une course séquentielle et dernière heure de départ avant la bascule de tarif (marge de 30 %).
    durees = {}
    for minutes in (1.5, 3.0, 6.0, 10.0):
        ligne = {}
        for nom, n in (("premier_monde_62", N_MONDE), ("quart_187", N_QUART), ("pilote_748", N_PILOTE)):
            heures = n * minutes / 60.0
            depart = BASCULE_TARIF_AU_PLUS_TOT - datetime.timedelta(hours=1.3 * heures)
            ligne[nom] = {"heures": arrondi(heures, 1), "depart_au_plus_tard": depart.strftime("%Y-%m-%dT%H:%MZ")}
        durees[str(minutes)] = ligne
    s["durees_selon_minutes_par_appel"] = durees
    s["bascule_tarif_au_plus_tot"] = BASCULE_TARIF_AU_PLUS_TOT.strftime("%Y-%m-%dT%H:%MZ")

    # 8. Exposition par jour si le quota de requêtes par jour est la seule borne dure (pire par requête).
    s["exposition_par_jour_selon_quota"] = {
        mois: {str(q): arrondi(q * cout(ENTREE_PIRE, PLAFOND_FLUX, tarif), 2) for q in (200, 250, 1000)}
        for mois, tarif in TARIFS.items()}

    s["entrees"] = {"tarifs_usd_par_million": TARIFS, "requetes": {"pilote": N_PILOTE, "quart": N_QUART, "monde": N_MONDE},
                    "plafond_flux": PLAFOND_FLUX, "texte_min": TEXTE_MIN, "entree_pire": ENTREE_PIRE,
                    "bornes_proposees": BORNES, "plafond_essai_coupure": PLAFOND_ESSAI_COUPURE}
    return s


def principal(arguments):
    analyseur = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analyseur.add_argument("sortie")
    analyseur.add_argument("--garde", default=None)
    options = analyseur.parse_args(arguments)
    resultat = calculer(options.garde)
    with open(__file__, "rb") as f:
        resultat["empreinte_du_script"] = hashlib.sha256(f.read()).hexdigest()
    texte = json.dumps(resultat, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    with open(options.sortie, "x", encoding="utf-8") as f:  # « x » : on n'écrase jamais (R12)
        f.write(texte)
    print(f"écrit : {options.sortie} ({len(texte.encode('utf-8'))} octets, sha256 "
          f"{hashlib.sha256(texte.encode('utf-8')).hexdigest()})")
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
