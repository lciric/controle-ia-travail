#!/usr/bin/env python3
"""Calculs du devis de l'étape 1 (rejeu exploratoire du chiffre publié sur MATH500)
et des deux calculs de l'étape 0 — EXPLORATOIRE, non opposable.

Bibliothèque standard seulement ; aucun tirage ; aucune donnée du programme.
Entrée unique : le relevé d'offres du loueur de cartes (chemin en argument).
Rejeu : python calculs-devis-etape-1-rejeu-math500-exploratoire-v1.py \
          ../releve-offres-loueur-cartes-2026-11-21T1055Z-v1.json
"""
import hashlib
import json
import math
import statistics
import sys

# ----------------------------------------------------------------------------
# Paramètres. « supposé » = aucune mesure ni pièce lue ne le porte.
# ----------------------------------------------------------------------------
N_QUESTIONS = 500            # MATH500, effectif du nom ; à vérifier par la garde du jeu
PLAFOND_JETONS = 16_000      # tableau 6, p. 19
DIM = 4096                   # largeur de Llama-3.1-8B
OCTETS_PAR_VALEUR = 2        # états gardés en demi-précision
COUCHES_NOYAU = 3            # couches 2, 3, 4
COUCHES_TOUTES = 8           # 1, 2, 3, 4, 5, 7, 15, 23
MODELE_GO = 16.0             # poids du modèle en demi-précision
OUTILS_GO = 10.0             # environnement, caches
MARGE_GO = 5.0
DISQUE_GO = 90               # disque demandé
HEURES_PAR_MOIS = 720        # 0,2 USD/Go/mois <-> 0,00222 USD/h pour 8 Go dans le relevé

# Bornes de l'offre (celles du devis voisin, l. 51, sauf cœurs et mémoire vive)
BORNE_CARTE = 1.30           # USD par heure, carte seule
BORNE_STOCKAGE = 0.08        # USD par heure, pour DISQUE_GO
BORNE_TOUT_COMPRIS = BORNE_CARTE + BORNE_STOCKAGE
COEURS_MIN = 12
MEMOIRE_MIN_MO = 64_000

# Volumes de réseau
DESCENTE_GO = 21.0           # modèle 16 Go + paquets 5 Go
MONTEE_GO = 3.0              # poids des sondes, états de la position de lecture, textes, scores

# Sondes à entraîner (une sonde = 100 époques, lots de 4 réponses)
BLOCS = [  # (nom, nombre de sondes, noyau ?)
    ("noyau a : couches 2-4, 5 plis, graine 0", 15, True),
    ("noyau b : étiquettes permutées, couche 3, 5 plis", 5, True),
    ("noyau c : vérité plantée, couche 3, 5 plis", 5, True),
    ("bloc d : deux graines de plus, couches 2-4", 30, False),
    ("bloc e : taux d'élagage par validation emboîtée, couches 2-4", 15, False),
    ("bloc f : couches 7, 15, 23", 15, False),
    ("bloc h : variante à cible gelée (semi-gradient), couches 2-4", 15, False),
    ("bloc g : couches 1 et 5 (indice de couche décalé)", 10, False),
]
EPOQUES = 100
REPONSES_PAR_LOT = 4
PART_ENTRAINEMENT = 0.8

# Scénarios. L = jetons moyens par réponse (supposé) ; debit = jetons par seconde,
# toutes séquences confondues (supposé) ; lenteur = facteur d'hôte.
SCENARIOS = {
    "attendu":    dict(L=750,  debit=400.0, lenteur=1.0, mise=0.35, conf=0.03, extr=0.10, rapat=0.25),
    "pessimiste": dict(L=2000, debit=150.0, lenteur=1.5, mise=0.75, conf=0.10, extr=0.30, rapat=0.50),
}
# Temps d'une sonde : frais fixes par pas + part proportionnelle au nombre d'états.
S_FIXE_PAR_PAS = 0.002       # secondes par pas d'optimiseur (supposé)
S_PAR_ETAT = 2.0e-6          # secondes par état vu (supposé : ~60 Gflop par lot de 3 000 états)

PLAFOND_USD = 10.0
MINUTERIE_H = 6.5            # destruction, depuis la création
ARRET_LANCEMENTS_H = 5.5     # plus aucun bloc lancé après


def titre(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def secondes_par_sonde(L, lenteur):
    reponses = N_QUESTIONS * PART_ENTRAINEMENT
    pas = EPOQUES * reponses / REPONSES_PAR_LOT
    etats = EPOQUES * reponses * (L + 1)
    return (pas * S_FIXE_PAR_PAS + etats * S_PAR_ETAT) * lenteur


def hanley_mcneil(a, n1, n0):
    q1 = a / (2 - a)
    q2 = 2 * a * a / (1 + a)
    v = (a * (1 - a) + (n1 - 1) * (q1 - a * a) + (n0 - 1) * (q2 - a * a)) / (n1 * n0)
    return math.sqrt(v)


def main(chemin):
    brut = open(chemin, "rb").read()
    titre("BLOC 1 - Le relevé d'offres")
    print("fichier :", chemin.split("/")[-1])
    print("empreinte sha256 :", hashlib.sha256(brut).hexdigest())
    offres = json.loads(brut)["offers"]
    o80 = [o for o in offres if o["gpu_ram"] >= 80_000 and o["num_gpus"] == 1]
    print(f"offres : {len(offres)} ; cartes A100 SXM4 de 80 Go : {len(o80)}")

    def tout_compris(o, disque=DISQUE_GO):
        return o["dph_base"] + o["storage_cost"] * disque / HEURES_PAR_MOIS

    def motif(o, disque=DISQUE_GO):
        m = []
        if o["verification"] != "verified":
            m.append("non vérifiée")
        if o["dph_base"] > BORNE_CARTE:
            m.append("carte > 1,30")
        if o["storage_cost"] * disque / HEURES_PAR_MOIS > BORNE_STOCKAGE:
            m.append("stockage > 0,08")
        if o["disk_space"] < disque:
            m.append(f"disque < {disque} Go")
        if o["cpu_cores_effective"] < COEURS_MIN:
            m.append("coeurs < 12")
        if o["cpu_ram"] < MEMOIRE_MIN_MO:
            m.append("mémoire < 64 Go")
        return m

    print(f"\nPrix tout compris pour un disque de {DISQUE_GO} Go (carte + stockage), USD par heure :")
    print(f"{'offre':>9} {'carte':>6} {'stock.':>6} {'total':>6} {'disque':>6} {'descente':>8} {'montée':>7}  lieu ; motif d'écart")
    retenues = []
    for o in sorted(o80, key=tout_compris):
        m = motif(o)
        if not m:
            retenues.append(o)
        print(f"{o['id']:>9} {o['dph_base']:6.3f} {o['storage_cost'] * DISQUE_GO / HEURES_PAR_MOIS:6.3f} "
              f"{tout_compris(o):6.3f} {o['disk_space']:6.0f} {o['internet_down_cost_per_tb']:8.2f} "
              f"{o['internet_up_cost_per_tb']:7.2f}  {o['geolocation']} ; {', '.join(m) if m else 'RETENUE'}")
    prix = sorted(tout_compris(o) for o in retenues)
    print(f"\noffres retenues sous les bornes, disque de {DISQUE_GO} Go : {len(retenues)} ; prix tout compris : "
          + ", ".join(f"{p:.3f}" for p in prix))
    r60 = sorted(tout_compris(o, 60) for o in o80 if not motif(o, 60))
    print("repli à 60 Go de disque : " + str(len(r60)) + " offres ; prix : " + ", ".join(f"{p:.3f}" for p in r60))
    prix_attendu = statistics.median(prix)
    prix_haut = BORNE_TOUT_COMPRIS
    print(f"prix du cas attendu (médiane des retenues) : {prix_attendu:.3f} USD/h ; prix haut (borne) : {prix_haut:.2f} USD/h")
    reseau = max(DESCENTE_GO * o["internet_down_cost_per_tb"] / 1000 + MONTEE_GO * o["internet_up_cost_per_tb"] / 1000
                 for o in retenues)
    reseau_min = min(DESCENTE_GO * o["internet_down_cost_per_tb"] / 1000 + MONTEE_GO * o["internet_up_cost_per_tb"] / 1000
                     for o in retenues)
    print(f"réseau ({DESCENTE_GO:.0f} Go descendus, {MONTEE_GO:.0f} Go montés) : de {reseau_min:.2f} à {reseau:.2f} USD selon l'offre retenue")
    o40 = sorted(o["dph_total"] for o in offres if o["gpu_ram"] < 80_000 and o["verification"] == "verified")
    print(f"pour mémoire, cartes de 40 Go vérifiées : {len(o40)} offres, de {o40[0]:.2f} à {o40[-1]:.2f} USD/h (disque du relevé)")

    titre("BLOC 2 - Volumes (jetons, disque)")
    for nom, L in (("attendu", 750), ("pessimiste", 2000), ("garde de volume", 2400), ("tout au plafond", PLAFOND_JETONS)):
        jetons = N_QUESTIONS * L
        etats = N_QUESTIONS * (L + 1)
        go_couche = etats * DIM * OCTETS_PAR_VALEUR / 1e9
        d3 = MODELE_GO + OUTILS_GO + MARGE_GO + COUCHES_NOYAU * go_couche
        d8 = MODELE_GO + OUTILS_GO + MARGE_GO + COUCHES_TOUTES * go_couche
        print(f"{nom:>16} : {L:>6} jetons par réponse, {jetons / 1e6:5.2f} M de jetons, {go_couche:6.2f} Go par couche ; "
              f"disque avec 3 couches {d3:6.1f} Go, avec 8 couches {d8:6.1f} Go")
    print(f"mémoire d'une séquence au plafond pendant la génération (clés et valeurs, 32 couches, 8 têtes, 128, 2 octets) : "
          f"{2 * 32 * 8 * 128 * 2 * PLAFOND_JETONS / 1e9:.2f} Go")

    titre("BLOC 3 - Sondes à entraîner")
    n_noyau = sum(n for _, n, noy in BLOCS if noy)
    n_tout = sum(n for _, n, _ in BLOCS)
    for nom, n, noy in BLOCS:
        print(f"{n:>4} sondes  {nom}")
    print(f"noyau : {n_noyau} sondes ; complet : {n_tout} sondes")
    for sc, p in SCENARIOS.items():
        print(f"temps d'une sonde, cas {sc} : {secondes_par_sonde(p['L'], p['lenteur']):.0f} s "
              f"(L = {p['L']}, hôte x{p['lenteur']})")

    titre("BLOC 4 - Durées et coûts par scénario")
    res = {}
    for sc, p in SCENARIOS.items():
        gen = N_QUESTIONS * p["L"] / p["debit"] / 3600
        t1 = secondes_par_sonde(p["L"], p["lenteur"]) / 3600
        fixe = p["mise"] + gen + p["conf"] + p["extr"] + p["rapat"]
        h_noyau = fixe + n_noyau * t1
        h_tout = fixe + n_tout * t1
        prix_sc = prix_attendu if sc == "attendu" else prix_haut
        res_sc = reseau_min if sc == "attendu" else reseau
        res[sc] = dict(gen=gen, t1=t1, fixe=fixe, h_noyau=h_noyau, h_tout=h_tout, prix=prix_sc, reseau=res_sc)
        print(f"\ncas {sc} (prix {prix_sc:.3f} USD/h, réseau {res_sc:.2f} USD)")
        print(f"  mise en place {p['mise']:.2f} h ; génération {gen:.2f} h ({N_QUESTIONS * p['L'] / 1e6:.2f} M de jetons à {p['debit']:.0f} par seconde) ; "
              f"confiance demandée {p['conf']:.2f} h ; extraction {p['extr']:.2f} h ; inventaire et rapatriement {p['rapat']:.2f} h")
        print(f"  hors sondes : {fixe:.2f} h")
        cumul = fixe
        for nom, n, noy in BLOCS:
            cumul += n * t1
            print(f"  après {nom:<62} : {cumul:5.2f} h, {cumul * prix_sc + res_sc:6.2f} USD")
        print(f"  NOYAU   : {h_noyau:.2f} h, {h_noyau * prix_sc + res_sc:.2f} USD")
        print(f"  COMPLET : {h_tout:.2f} h, {h_tout * prix_sc + res_sc:.2f} USD")

    titre("BLOC 5 - Plafond, arrêt des lancements, minuterie de destruction")
    pire_payable = MINUTERIE_H * prix_haut + reseau
    print(f"plafond proposé : {PLAFOND_USD:.2f} USD ; arrêt des lancements à {ARRET_LANCEMENTS_H} h ; destruction à {MINUTERIE_H} h")
    print(f"pire cas payable = minuterie x prix haut + réseau haut = {MINUTERIE_H} x {prix_haut:.2f} + {reseau:.2f} = {pire_payable:.2f} USD")
    print(f"pire cas sans coupure (cas pessimiste, complet) : {res['pessimiste']['h_tout']:.2f} h, "
          f"{res['pessimiste']['h_tout'] * prix_haut + reseau:.2f} USD")
    tout_plafond_gen = N_QUESTIONS * PLAFOND_JETONS / SCENARIOS["pessimiste"]["debit"] / 3600
    print(f"génération si toutes les réponses atteignaient le plafond, au débit pessimiste : {tout_plafond_gen:.1f} h "
          f"({tout_plafond_gen * prix_haut:.2f} USD) : empêché par la tranche de mesure et par la minuterie")
    # Blocs atteints avant l'arrêt des lancements, cas pessimiste
    p = SCENARIOS["pessimiste"]
    cumul = res["pessimiste"]["fixe"] - p["rapat"]
    atteints = []
    for nom, n, noy in BLOCS:
        if cumul + n * res["pessimiste"]["t1"] <= ARRET_LANCEMENTS_H:
            cumul += n * res["pessimiste"]["t1"]
            atteints.append(nom.split(" :")[0])
        else:
            break
    print(f"cas pessimiste : blocs finis avant l'arrêt des lancements : {', '.join(atteints)} (fin à {cumul:.2f} h, "
          f"puis rapatriement {p['rapat']:.2f} h, soit {cumul + p['rapat']:.2f} h)")

    titre("BLOC 6 - Objets de contrôle du devis")
    essais = [
        ("faux : le complet pessimiste tient sous le plafond", res["pessimiste"]["h_tout"] * prix_haut + reseau, False),
        ("faux : la génération tout au plafond tient sous le plafond", tout_plafond_gen * prix_haut, False),
        ("vrai : le pire cas payable (minuterie) tient sous le plafond", pire_payable, True),
        ("vrai : le noyau pessimiste tient sous le plafond", res["pessimiste"]["h_noyau"] * prix_haut + reseau, True),
        ("vrai : le complet attendu tient sous le plafond", res["attendu"]["h_tout"] * prix_attendu + reseau_min, True),
    ]
    tout_bon = True
    for nom, cout, attendu_sous in essais:
        sous = cout <= PLAFOND_USD
        bon = (sous == attendu_sous)
        tout_bon &= bon
        print(f"{'conforme' if bon else 'NON CONFORME'} | {nom} : {cout:.2f} USD -> {'sous' if sous else 'au-dessus'}")
    print(f"le noyau pessimiste finit avant la minuterie : {res['pessimiste']['h_noyau']:.2f} h <= {MINUTERIE_H} h : "
          f"{res['pessimiste']['h_noyau'] <= MINUTERIE_H}")
    print("tous les objets de contrôle rendent ce qui était prévu :", tout_bon)

    titre("BLOC 7 - Étape 0, point 1 : effectif du tableau 4 (p. 9), par l'arithmétique des pourcentages")
    valeurs = [72.2, 75.0, 77.8]

    def atteignable(v, denominateur):
        k0 = int(v * denominateur / 100)
        return any(abs(100 * k / denominateur - v) < 0.05 - 1e-12 for k in (k0 - 1, k0, k0 + 1, k0 + 2))

    lecture_a = [n for n in range(1, 501) if all(atteignable(v, 3 * n) for v in valeurs)]
    lecture_b = [n for n in range(1, 501) if atteignable(72.2, n) and all(atteignable(v, 3 * n) for v in (75.0, 77.8))]
    print("lecture A (chaque exactitude est une moyenne de 3 graines sur n questions) : effectifs compatibles <= 150 :")
    print("  ", [n for n in lecture_a if n <= 150])
    print("lecture B (décodage glouton déterministe : 72,2 = k/n ; les autres, moyennes de 3 graines) : effectifs compatibles <= 150 :")
    print("  ", [n for n in lecture_b if n <= 150])
    for n in (100, 500):
        print(f"n = {n} : lecture A {'compatible' if n in lecture_a else 'INCOMPATIBLE'} ; lecture B {'compatible' if n in lecture_b else 'INCOMPATIBLE'}")
    for nom, liste in (("A", lecture_a), ("B", lecture_b)):
        dernier_exclu = max(n for n in range(1, 501) if n not in liste)
        print(f"lecture {nom} : {len(liste)} effectifs compatibles sur 500 ; plus grand effectif exclu : {dernier_exclu}"
              + (" (au-delà, la grille des pourcentages est trop fine pour exclure quoi que ce soit)" if nom == "A" else ""))
    print("de 90 à 110 : lecture A", [n for n in lecture_a if 90 <= n <= 110], "; lecture B", [n for n in lecture_b if 90 <= n <= 110])
    print("tableau 2 (p. 5), exactitude d'origine 75,2 % : k/500 =", 75.2 * 5, "-> entier ; k/100 =", 75.2, "-> non entier")

    titre("BLOC 8 - Erreur d'échantillonnage d'une aire de 0,69 (Hanley et McNeil)")
    for n1, n0 in ((50, 50), (40, 60), (30, 70), (250, 250), (200, 300), (150, 350), (100, 400)):
        es = hanley_mcneil(0.69, n1, n0)
        print(f"{n1 + n0:>4} questions ({n1:>3} réussites, {n0:>3} échecs) : écart type {es:.4f}, demi-largeur à 95 % {1.96 * es:.3f}")


if __name__ == "__main__":
    main(sys.argv[1])
