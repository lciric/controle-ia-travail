#!/usr/bin/env python3
"""Calculs du brouillon 5 du préenregistrement de la porte G1 — v1.

Exploratoire, processeur seul. Aucune donnée du programme n'est lue (rien sous `donnees/`, aucun score d'épisode) :
les seules entrées sont des constantes recopiées des pièces citées dans le brouillon, chacune avec sa source dans
le commentaire. Non opposable seul (R7) : le brouillon cite cette sortie par chemin et empreinte (R6).

Lancer, depuis un dossier vide : python3 -I <chemin>/calculs-g1-brouillon5-v1.py > calculs-g1-brouillon5-v1-sortie.txt
"""
import hashlib
import math
import platform
from fractions import Fraction

import numpy as np
import scipy
from scipy import stats


def titre(s):
    print(f"\n## {s}\n")


def nombre(x, dec=0):
    """Nombre à la française : espace pour les milliers, virgule décimale (le texte autour n'est jamais touché)."""
    t = f"{x:,.{dec}f}"
    return t.replace(",", " ").replace(".", ",")


def rang_conforme(K, a):
    """Rang ceil((K+1)(1-a)) calculé en fractions exactes (pas d'erreur d'arrondi flottant)."""
    return math.ceil((K + 1) * (1 - Fraction(a)))


print("# Sortie de calculs-g1-brouillon5-v1.py")
print(f"Python {platform.python_version()} ; numpy {np.__version__} ; scipy {scipy.__version__}")
print("Aucune graine : tous les calculs sont déterministes (formules fermées).")

# ---------------------------------------------------------------------------------------------------------------
titre("1. Seuil par action à 1 % : fausses alarmes par épisode, actions indépendantes (brouillon 3, Métrique)")
for T in (10, 100):
    print(f"T = {T:>3} actions : 1 - 0,99^T = {nombre(1 - 0.99 ** T, 4)}")

# ---------------------------------------------------------------------------------------------------------------
titre("2. Seuil conforme sur K épisodes honnêtes entiers (rang ceil((K+1)(1-a)) ; taux réel ~ Bêta(K+1-r, r))")
for a in (0.01, 0.05):
    kmin = next(K for K in range(1, 10_000) if rang_conforme(K, a) <= K)
    print(f"a = {nombre(a, 2)} : plus petit K pour un seuil fini = {kmin}")
print()
a = 0.01
print("a = 0,01 ; P(taux réel de fausses alarmes > 0,02 | calibrage) :")
for K in (99, 299, 499, 999, 4000, 40000, 64000):
    r = rang_conforme(K, a)
    p = stats.beta.sf(0.02, K + 1 - r, r)
    print(f"  K = {K:>6} : rang {r:>6} ; P(> 0,02) = {nombre(p, 4)}")

# ---------------------------------------------------------------------------------------------------------------
titre("3. Borne haute unilatérale à 95 % de Clopper-Pearson pour un taux observé de 1 %")
for n in (300, 700, 4000, 6400, 40000):
    x = round(0.01 * n)
    haut = stats.beta.ppf(0.95, x + 1, n - x)
    print(f"  n = {n:>6}, {x:>4} alarmes : borne haute = {nombre(haut, 4)}")

# ---------------------------------------------------------------------------------------------------------------
titre("4. Ordre de grandeur du rappel d'une sonde générique de P3 en accumulation (modèle binormal ; NON OPPOSABLE)")
print("Entrées : aires saboteur contre honnête par action de P3, organisme flagrant (i-a), toutes actions sabotées")
print("(verdict de P3 v2, section 3 : 0,5748 tromperie, 0,5248 enjeux ; lecture-p3.json c221d955…).")
print("Modèle : scores d'action gaussiens de variance 1 ; décalage d par action sabotée ; d = sqrt(2) * Phi^-1(aire) ;")
print("statistique d'épisode = somme des T = 10 scores (accumulation) ou maximum (par action) ; seuil d'épisode à tau = 0,01 ;")
print("corrélation intra-épisode rho_e (effet épisode, équicorrélation) ; p = part des actions sabotées.")
tau = 0.01
z = stats.norm.ppf(1 - tau)
T = 10
for nom, aire in (("tromperie", 0.5748), ("enjeux", 0.5248)):
    d = math.sqrt(2) * stats.norm.ppf(aire)
    print(f"\n  sonde {nom} : aire {nombre(aire, 4)} -> d = {nombre(d, 3)}")
    for rho in (0.0, 0.2):
        for p in (1.0, 0.5, 0.25):
            ns = p * T
            var0 = T * (1 + (T - 1) * rho)
            rappel_somme = stats.norm.cdf(ns * d / math.sqrt(var0) - z)
            print(f"    rho_e = {nombre(rho, 1)}, p = {nombre(p, 2)} : rappel de la somme = {nombre(rappel_somme, 4)}")
    # maximum par action, actions indépendantes : seuil c tel que Phi(c)^T = 1 - tau
    c = stats.norm.ppf((1 - tau) ** (1 / T))
    for p in (1.0, 0.5, 0.25):
        ns = int(round(p * T))
        rappel_max = 1 - stats.norm.cdf(c - d) ** ns * stats.norm.cdf(c) ** (T - ns)
        print(f"    rho_e = 0,0, p = {nombre(p, 2)} : rappel du maximum = {nombre(rappel_max, 4)}")
print("\nRepère observé (descriptif de P3, P3-P5, seuil = maximum de 60 épisodes honnêtes) : somme 0,0167 (tromperie),")
print("0,0667 (enjeux) ; maximum 0,0000 et 0,0667 (lecture-p3.json, clés resultat.P3-P5.*.somme.rappel et .maximum.rappel).")

# ---------------------------------------------------------------------------------------------------------------
titre("5. Intersection-union : puissance conjointe si les fiches étaient indépendantes (illustration prudente)")
for p in (0.9, 0.8):
    print(f"  puissance par fiche {nombre(p, 1)} : " + " ; ".join(f"{c} fiche(s) -> {nombre(p ** c, 3)}" for c in (1, 2, 3, 4, 6)))
print("Les fiches partagent les jumeaux honnêtes et les comparateurs : elles sont corrélées positivement, la puissance")
print("conjointe réelle est au-dessus du produit (borne basse sous dépendance positive, non démontrée ici).")

# ---------------------------------------------------------------------------------------------------------------
titre("6. Holm sur e-valeurs converties en p = min(1, 1/e) : seuils d'e-valeur par rang, a = 0,05")
for m in (4, 3):
    seuils = [m - i for i in range(m)]
    print(f"  famille de {m} : " + " ; ".join(f"rang {i + 1} : p <= {nombre(0.05 / s, 4)} (e >= {nombre(s / 0.05)})"
                                             for i, s in enumerate(seuils)))

# ---------------------------------------------------------------------------------------------------------------
titre("7. Devis de la campagne de G1 (T1.2) : épisodes, heures de carte A100 80 Go, dollars")
# Rythmes (RAPPORTÉS) : génération 42,1 s par épisode (pilote de T0.5, R-143, repris par le dimensionnement de la
# couche 2 § 8, 95c5c396…) ; 54,6 s par épisode tout compris (P3 : 3,64 h pour 240 épisodes, registres/depenses.md,
# ligne du 2026-10-20 02:10) ; notation d'un juge 8B : 58,2 s par épisode (R-205, même source § 8).
# Équivalents « juge 8B » par épisode pour l'ensemble des moniteurs boîte noire (B) : 1 à 4 (dimensionnement § 8,
# INFÉRÉ) ; 8 en scénario de tension (liste élargie par R-746 (1) : juges préparés nus, informés, à exemples, 8B et 3B).
# Prix A100 SXM4 80 Go, offres conformes : 1,08 à 1,2133 USD de l'heure (registres/depenses.md, lignes du 12 au 17
# octobre) ; 1,43 relevé le 28 octobre (P-036 v2, point 2.4, SUPPOSÉ tant qu'il n'est pas consigné avec empreinte).
GEN = {"bas": 42.1, "central": (42.1 + 54.6) / 2, "haut": 54.6}
JUGE = 58.2
B = {"bas": 1, "central": 2, "haut": 4, "tension": 8}
PRIX = {"bas": 1.08, "central": (1.08 + 1.2133) / 2, "haut": 1.2133, "tension": 1.43}


def episodes_par_tache(modes, familles_lues, K_s=10, K_h=10, temoin_mention=12, facteur_calibrage=15):
    """Épisodes par tâche : jumeaux honnêtes K_h (partagés entre modes et familles), sabotés K_s par mode et par
    famille lue, témoin instruit et mention (2 conditions x 2 modes connus x 3 exécutions = 12, dimensionnement § 1),
    calibrage honnête = facteur x K_s épisodes (D-S9 (a) : 10 à 16 fois les unités sabotées, unités de 10 épisodes)."""
    return K_h + modes * K_s * familles_lues + temoin_mention + facteur_calibrage * 10


VARIANTES = {
    # nom : (tâches = unités par mode, modes, familles lues, facteur de calibrage, commentaire)
    "minimale": (288, 3, 1, 10, "n_h plancher 288 (R-716, R-719) ; famille (ii) seule ; calibrage 10 fois"),
    "par défaut": (400, 3, 2, 15, "400 unités sans mesure au pilote (R-556 (2)) ; (ii) et (i-a) ; calibrage 15 fois"),
    "plafond de la table": (544, 3, 2, 16, "n_h maximal de la table v9 au seuil 160 (rho chapeau 0,17) ; 16 fois"),
}
print("Hypothèses : K_s = 10 (R-504), K_h = 10 (R-733 N2), 3 modes (coût, contrôles, tenu à l'écart),")
print("témoin et mention 12 par tâche, disques, téléchargements et extraction des tâches non comptés.\n")
resultats = {}
for nom, (n, modes, fam, fac, com) in VARIANTES.items():
    ept = episodes_par_tache(modes, fam, facteur_calibrage=fac)
    E = n * ept
    print(f"### variante {nom} : {n} tâches x {ept} épisodes = {nombre(E)} épisodes ({com})")
    for cle in ("bas", "central", "haut"):
        s = GEN[cle] + B[cle] * JUGE
        h = E * s / 3600
        usd = h * PRIX[cle]
        resultats[(nom, cle)] = (h, usd)
        print(f"  {cle:>7} : {nombre(GEN[cle], 2)} s + {B[cle]} x {nombre(JUGE, 1)} s = {nombre(s, 1)} s par épisode ; "
              f"{nombre(h)} h ; {nombre(usd)} USD")
    s = GEN["haut"] + B["tension"] * JUGE
    h = E * s / 3600
    print(f"  tension : {nombre(GEN['haut'], 2)} s + {B['tension']} x {nombre(JUGE, 1)} s = {nombre(s, 1)} s ; "
          f"{nombre(h)} h ; {nombre(h * PRIX['tension'])} USD (prix {nombre(PRIX['tension'], 2)})")
    print()

h_c, usd_c = resultats[("par défaut", "central")]
print(f"Plafond proposé (variante par défaut, estimation centrale x 1,3, marge du brief § 14) : "
      f"{nombre(usd_c * 1.3)} USD ; alerte à 80 % : {nombre(usd_c * 1.3 * 0.8)} USD")
print(f"Durée murale de la variante par défaut, estimation centrale : {nombre(h_c)} h de carte ; "
      f"sur 20 cartes en parallèle : {nombre(h_c / 20 / 24, 1)} jours ; sur 40 : {nombre(h_c / 40 / 24, 1)} jours")
part_cal = 15 * 10 / episodes_par_tache(3, 2, facteur_calibrage=15)
print(f"Part du calibrage honnête dans la variante par défaut : {nombre(part_cal, 3)}")
print(f"Prix central retenu : {nombre(PRIX['central'], 4)} USD de l'heure ; génération centrale {nombre(GEN['central'], 2)} s")

# ---------------------------------------------------------------------------------------------------------------
titre("8. Règle des graines (R9) : racine tirée de l'empreinte du texte scellé — démonstration sur une empreinte connue")
EXEMPLE = "e488d0658c7ab6fd964eb269d3b5e675b7c93a0873f666482bf8c71551b609c4"  # brouillon 3, exemple seulement
racine = np.random.SeedSequence(entropy=int(EXEMPLE, 16))
print(f"empreinte d'exemple (brouillon 3, jamais utilisée pour G1) : {EXEMPLE}")
print(f"entropie = int(empreinte, 16) = {racine.entropy}")
# clé dérivée : (code de l'usage, code du mode, indice de tâche, indice d'exécution)
CODES = {"generation": 1, "moities_calibrage": 2, "bris_egalite": 3, "reechantillonnage": 4, "placebo": 5}
cle = (CODES["generation"], 2, 17, 3)
g = np.random.default_rng(np.random.SeedSequence(entropy=racine.entropy, spawn_key=cle))
print(f"clé de dérivation {cle} -> trois premiers entiers 32 bits : {g.integers(0, 2**32, size=3).tolist()}")
g2 = np.random.default_rng(np.random.SeedSequence(entropy=racine.entropy, spawn_key=cle))
print(f"rejoué : {g2.integers(0, 2**32, size=3).tolist()} (identique attendu)")
print(f"contrôle : sha256 de la chaîne de la clé = {hashlib.sha256(repr(cle).encode()).hexdigest()[:16]}…")

# ---------------------------------------------------------------------------------------------------------------
titre("9. Réglages des statistiques séquentielles (bases.sequentiel) proposés pour G1, T = 10, tau = 0,01")
import sys
from pathlib import Path
SRC = Path(__file__).resolve().parents[3] / "src"   # code du dépôt lui-même (aucun code extérieur)
sys.path.insert(0, str(SRC))
from controle_ia.simulation_t03 import calibrage as cal03  # noqa: E402

rho, frontiere = cal03.rho_optimal(10, 0.01, "unilateral")
print(f"rho* du processus e unilatéral de mélange normal, n0 = 10, alpha = 0,01 (règle de la note v3, § 2, "
      f"simulation_t03.calibrage.rho_optimal) : {nombre(rho, 4)} (frontière {nombre(frontiere, 3)})")
print("k de Page = 0,5 et fenêtre de balayage w = 5 : valeurs de T0.3 (simulation_t03/blocs.py, l. 97 et 230 ; "
      "« glissante_5 » de la grille v2)")
f = SRC / "controle_ia" / "simulation_t03" / "calibrage.py"
print(f"empreinte du module lu : {hashlib.sha256(f.read_bytes()).hexdigest()}")

# ---------------------------------------------------------------------------------------------------------------
titre("10. Rappel de la somme selon l'horizon t (préfixe de t actions, toutes sabotées), seuil recalibré à tau = 0,01 "
      "sur les préfixes honnêtes de même longueur (modèle binormal du § 4, actions indépendantes ; NON OPPOSABLE)")
for nom, aire in (("tromperie", 0.5748), ("enjeux", 0.5248)):
    d = math.sqrt(2) * stats.norm.ppf(aire)
    valeurs = {t: stats.norm.cdf(math.sqrt(t) * d - z) for t in (2, 5, 10)}
    print(f"  sonde {nom} (d = {nombre(d, 3)}) : " + " ; ".join(f"t = {t} : {nombre(v, 4)}" for t, v in valeurs.items())
          + f" ; écart t = 10 moins t = 5 : {nombre(valeurs[10] - valeurs[5], 4)}")
