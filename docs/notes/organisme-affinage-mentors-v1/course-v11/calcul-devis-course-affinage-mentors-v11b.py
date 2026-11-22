#!/usr/bin/env python3
"""Calcul des chiffres du devis v11b de la course d'affinage des idées des mentors.

v11b : le programme du devis v11 (`calcul-devis-course-affinage-mentors-v11.py`,
`deac25b6fe59332b646cd7b67580126221f3aa5f547623a6270c58b2330428ee`), inchangé, plus un bloc final sur le seuil de la
recharge automatique de la clé LUC (5 USD, R-5042). Aucun chiffre du devis v11 ne change.

Aucun appel, aucun réseau, aucune lecture de fichier : toutes les entrées sont écrites ici, avec leur source.
Usage : python3 -I calcul-devis-course-affinage-mentors-v11b.py
Sortie : une ligne par chiffre du devis (et du préenregistrement v11 qui le cite) ; code 0 si tous les contrôles passent.
Arithmétique exacte (fractions) ; les arrondis sont faits à l'affichage seulement, au plus proche.

Trois jeux de prix pour Argon et Carbon (USD par million de jetons, entrée et sortie) :
  - « prix déclarés » : 4 et 20, prix le plus haut de la page de prix versée (à partir du 1er décembre 2026), retenus par
    la mère pour le gabarit v11 (R-5018) : devis v11, § 1 à § 7 ;
  - « bornes des v6 à v10 » : 8,3 et 41,5, prix comptés par les commandes épinglées des v6 à v10 : devis v11, § 8 ;
  - « page, jusqu'au 30 novembre » : 2 et 10 (même page) : devis v11, § 8.
"""
from fractions import Fraction as F
import math
import sys

M = 10 ** 6

# --- Entrées, avec leur source -------------------------------------------------------------------------------------
DECLARES = (F(4), F(20))              # page de prix versée du 22 novembre, l. 153-163 (Carbon) et 372-382 (Argon) ; R-5018
BORNES = (F("8.3"), F("41.5"))        # commande d'Argon l. 345-346 et enveloppe l. 29 ; R-3271 pour Carbon (préenregistrement v10)
PAGE_NOVEMBRE = (F(2), F(10))         # même page, « through November 30, 2026 »
CASES = 16                            # seize fils servis
ESPECES = 5                           # deux Claude, Argon, Astra, Carbon
CARTES = CASES * ESPECES * 2          # deux cartes par appel de proposeur : 160
APPELS_PROPOSEURS = CASES * ESPECES   # 80
APPELS_AIGUILLEUR = CARTES            # 160
APPELS_JUGE_PAR_JUGE = CARTES         # 160 par juge, deux juges
# Prix par appel du devis v6 (§ 1 et § 2), repris par les devis v8 à v10 ; ceux d'Argon y sont comptés aux bornes
P_CLAUDE_1, P_CLAUDE_2 = F("0.141"), F("0.3525")
P_HORS_CLAUDE = F("0.276")            # Argon (mesuré, aux bornes), Astra (supposé)
P_AIGUILLEUR, P_JUGE_CLAUDE, P_JUGE_ARGON = F("0.031"), F("0.037"), F("0.0347")
# Carbon, hypothèses du devis v10, § 2
CARBON_ENTREE, CARBON_REFLEXION, CARBON_REPONSE = 2618, 20000, 3500
CARBON_PRIX_LOT_V10 = F("0.4985")     # devis v10, § 2 (prix du lot, aux bornes)
CARBON_REFLEXION_HAUTE = 44101        # plus forte réflexion de Carbon en flux relevée dans le collisionneur (note f6342515…, § 3)
SOUS_TOTAL_V10 = F("41.136")          # devis v10, § 3
# Plafonds de session (configuration v9 : proposeur 3,00 ; aiguilleur 0,25 ; juge 0,60)
PS_PROPOSEUR, PS_AIGUILLEUR, PS_JUGE_V10 = F("3.00"), F("0.25"), F("0.60")
PLAFOND_ARRET = F(150)
# Garde gelée des appels aux modèles de Google (garde commune v3)
TEXTE_MIN = 16000
ARGON_LIMITE_HORS_FLUX, CARBON_LIMITE_FLUX = 32768, 65536
ARGON_PLAFOND_SORTIE, ARGON_PROVISION = 32768, 16384   # réglages d'Argon sous la garde (note 9cf6799f…, § 3)
CARBON_PROVISION_GARDE = 49152                         # réglage de Carbon sous la garde (même note, § 3)
# Entrée d'un appel de juge
CONSIGNE_JUGE_CARACTERES = 1514       # 1 563 octets, 1 514 caractères (a32583b1…)
CARTE_CARACTERES_MAX = 9000           # consigne du proposeur, l. 20
CADRE_CARACTERES = 500                # supposé
MARGE_ENTREE = F("0.05")              # défaut de la commande d'Argon
ENTREE_LA_PLUS_LONGUE = 2618          # jetons, devis v10, § 1 (fil le plus long)
RESERVE_RELAIS_CLAUDE = F("0.40")     # défaut du relais Claude épinglé
PLAFOND_PART_CLAUDE = F(45)           # R-5007 (a), GO-2026-11-22-124

controles = []


def usd(x, n=2):
    """Arrondi au plus proche à n décimales, écrit à la française (virgule)."""
    q = 10 ** n
    v = math.floor(x * q + F(1, 2))
    entier, frac = divmod(v, q)
    return str(entier) if n == 0 else f"{entier},{str(frac).rjust(n, '0')}"


def dire(nom, valeur, attendu=None):
    print(f"{nom} : {valeur}")
    if attendu is not None:
        controles.append((nom, str(valeur), attendu))


def au_dixieme_superieur(x):
    return F(math.ceil(x * 10), 10)


def jeu(nom, prix, a):
    """Tous les chiffres du devis pour un jeu de prix de Google ; `a` : valeurs écrites au devis, contrôlées."""
    pe, ps = prix
    echelle = ps / BORNES[1]
    assert pe / BORNES[0] == echelle  # les deux prix changent du même facteur : les postes mesurés d'Argon changent d'autant
    print(f"\n=== {nom} : {usd(pe, 1)} et {usd(ps, 1)} USD par million de jetons ===")

    def cout(entree, sortie):
        return (entree * pe + sortie * ps) / M

    vus = set()

    def d(cle, valeur):
        vus.add(cle)
        dire(f"[{nom}] {cle}", valeur, a.get(cle))

    # plafond de session des juges
    d("16 000 jetons de texte au prix de sortie (USD)", usd(cout(0, TEXTE_MIN), 3))
    caracteres = CONSIGNE_JUGE_CARACTERES + CARTE_CARACTERES_MAX + CADRE_CARACTERES
    jetons_3 = math.ceil(F(caracteres, 3) * (1 + MARGE_ENTREE))
    jetons_4 = math.ceil(F(caracteres, 4) * (1 + MARGE_ENTREE))
    d("entrée d'un appel de juge (caractères)", caracteres)
    d("entrée d'un appel de juge, 3 caractères par jeton, marge 5 % (jetons)", jetons_3)
    d("entrée d'un appel de juge, 4 caractères par jeton, marge 5 % (jetons)", jetons_4)
    entree_juge = cout(jetons_3, 0)
    d("coût de cette entrée (USD)", usd(entree_juge, 4))
    dedans = cout(0, ARGON_PLAFOND_SORTIE)
    dessus = cout(0, ARGON_PLAFOND_SORTIE + ARGON_PROVISION)
    d("sortie comptée, réflexion dans le plafond de sortie (USD)", usd(dedans, 4))
    d("pire cas d'un appel de juge d'Argon, réflexion dans le plafond (USD)", usd(entree_juge + dedans, 4))
    d("sortie comptée, provision en plus du plafond de sortie (USD)", usd(dessus, 4))
    d("pire cas d'un appel de juge d'Argon, provision en plus (USD)", usd(entree_juge + dessus, 4))
    ps_juge = au_dixieme_superieur(entree_juge + dessus)
    ps_juge_dedans = au_dixieme_superieur(entree_juge + dedans)
    d("plafond de session des juges, au dixième, provision en plus (USD)", usd(ps_juge, 2))
    d("plafond de session des juges, au dixième, réflexion dans le plafond (USD)", usd(ps_juge_dedans, 2))
    d("entrée de juge couverte sous ce plafond, provision en plus (jetons)", math.floor((ps_juge - dessus) * M / pe))
    d("entrée de juge couverte sous ce plafond, réflexion dans le plafond (jetons)", math.floor((ps_juge - dedans) * M / pe))
    d("entrée de juge couverte un dixième de dollar plus haut, provision en plus (jetons)",
      math.floor((ps_juge + F(1, 10) - dessus) * M / pe))
    d("marge de ce plafond sur l'entrée de juge attendue, provision en plus (jetons)",
      math.floor((ps_juge - dessus) * M / pe) - jetons_3)
    assert ARGON_PLAFOND_SORTIE - ARGON_PROVISION >= TEXTE_MIN and ARGON_PLAFOND_SORTIE <= ARGON_LIMITE_HORS_FLUX
    d("texte restant d'Argon au plafond de sortie retenu (jetons)", ARGON_PLAFOND_SORTIE - ARGON_PROVISION)
    d("plus petit plafond de sortie d'Argon que la garde admet à cette provision (jetons)", ARGON_PROVISION + TEXTE_MIN)
    d("pire cas d'un appel de juge d'Argon à ce plus petit plafond, réflexion dans le plafond (USD)",
      usd(entree_juge + cout(0, ARGON_PROVISION + TEXTE_MIN), 4))
    borne = (APPELS_PROPOSEURS * PS_PROPOSEUR + APPELS_AIGUILLEUR * PS_AIGUILLEUR + 2 * APPELS_JUGE_PAR_JUGE * ps_juge)
    d("borne des plafonds de session (USD)", usd(borne, 0))
    # proposeurs de Google sous le plafond de session d'un proposeur
    argon_prop_dessus = cout(ENTREE_LA_PLUS_LONGUE, ARGON_PLAFOND_SORTIE + ARGON_PROVISION)
    argon_prop_dedans = cout(ENTREE_LA_PLUS_LONGUE, ARGON_PLAFOND_SORTIE)
    d("pire cas d'un appel de proposeur d'Argon, provision en plus (USD)", usd(argon_prop_dessus, 4))
    d("pire cas d'un appel de proposeur d'Argon, réflexion dans le plafond (USD)", usd(argon_prop_dedans, 4))
    carbon_dedans = cout(ENTREE_LA_PLUS_LONGUE, CARBON_LIMITE_FLUX)
    d("pire cas d'un appel de Carbon en flux au plafond de sortie le plus haut, réflexion dans le plafond (USD)",
      usd(carbon_dedans, 4))
    assert argon_prop_dessus < PS_PROPOSEUR and carbon_dedans < PS_PROPOSEUR
    assert CARBON_LIMITE_FLUX - CARBON_PROVISION_GARDE >= TEXTE_MIN
    d("pire cas de Carbon au plafond de sortie 65 536 et à la provision 49 152, provision en plus (USD)",
      usd(cout(ENTREE_LA_PLUS_LONGUE, CARBON_LIMITE_FLUX + CARBON_PROVISION_GARDE), 4))
    reste = (PS_PROPOSEUR - cout(ENTREE_LA_PLUS_LONGUE, 0)) * M / ps
    d("provision de Carbon la plus haute sous 3,00 USD, provision en plus, plafond = provision + 16 000 (jetons)",
      math.floor((reste - TEXTE_MIN) / 2))
    d("pire cas de Carbon à la provision de 25 870 jetons, provision en plus (USD)",
      usd(cout(ENTREE_LA_PLUS_LONGUE, 2 * 25870 + TEXTE_MIN), 4))
    # estimation
    prop_claude = CASES * P_CLAUDE_1 + CASES * P_CLAUDE_2
    prop_argon = CASES * P_HORS_CLAUDE * echelle
    prop_astra = CASES * P_HORS_CLAUDE
    carbon_appel = cout(CARBON_ENTREE, CARBON_REFLEXION + CARBON_REPONSE)
    prop_carbon = CASES * carbon_appel
    aiguilleur = APPELS_AIGUILLEUR * P_AIGUILLEUR
    juge_claude = APPELS_JUGE_PAR_JUGE * P_JUGE_CLAUDE
    juge_argon = APPELS_JUGE_PAR_JUGE * P_JUGE_ARGON * echelle
    d("proposeurs Claude (USD)", usd(prop_claude, 3))
    d("proposeur Argon, par appel (USD)", usd(P_HORS_CLAUDE * echelle, 4))
    d("proposeur Argon (USD)", usd(prop_argon, 3))
    d("proposeur Astra (USD)", usd(prop_astra, 3))
    d("Carbon, par appel, prix plein (USD)", usd(carbon_appel, 4))
    d("proposeur Carbon (USD)", usd(prop_carbon, 3))
    d("aiguilleur (USD)", usd(aiguilleur, 2))
    d("juge Claude (USD)", usd(juge_claude, 2))
    d("juge Argon, par appel (USD)", usd(P_JUGE_ARGON * echelle, 4))
    d("juge Argon (USD)", usd(juge_argon, 3))
    proposeurs = prop_claude + prop_argon + prop_astra + prop_carbon
    sous_total = proposeurs + aiguilleur + juge_claude + juge_argon
    d("proposeurs, ensemble (USD)", usd(proposeurs, 2))
    d("juges, ensemble (USD)", usd(juge_claude + juge_argon, 2))
    d("sous-total, sans la réflexion d'Argon (USD)", usd(sous_total, 3))
    d("marge de 10 % (USD)", usd(sous_total / 10, 2))
    d("total, marge comprise (USD)", usd(sous_total * F("1.1"), 2))
    carbon_haut = cout(CARBON_ENTREE, CARBON_REFLEXION_HAUTE + CARBON_REPONSE)
    d("Carbon, par appel, à la plus forte réflexion relevée ailleurs (USD)", usd(carbon_haut, 4))
    d("proposeur Carbon à cette réflexion (USD)", usd(CASES * carbon_haut, 2))
    d("proposeur Carbon à cette réflexion, en plus de l'estimation (USD)", usd(CASES * (carbon_haut - carbon_appel), 2))
    # réflexion d'Argon
    par_millier_prop = cout(0, CASES * 1000)
    par_millier_juge = cout(0, APPELS_JUGE_PAR_JUGE * 1000)
    d("réflexion d'Argon, par millier de jetons moyens : proposeur (USD)", usd(par_millier_prop, 2))
    d("réflexion d'Argon, par millier de jetons moyens : juge (USD)", usd(par_millier_juge, 2))
    d("réflexion d'Argon, par millier de jetons moyens : ensemble (USD)", usd(par_millier_prop + par_millier_juge, 2))
    d("appels d'Argon dans la course", CASES + APPELS_JUGE_PAR_JUGE)
    for t in (2000, 4096, 8192, 16384):
        plus_prop, plus_juge = cout(0, CASES * t), cout(0, APPELS_JUGE_PAR_JUGE * t)
        st = sous_total + plus_prop + plus_juge
        d(f"réflexion moyenne {t} : proposeur Argon en plus (USD)", usd(plus_prop, 2))
        d(f"réflexion moyenne {t} : juge Argon en plus (USD)", usd(plus_juge, 2))
        d(f"réflexion moyenne {t} : sous-total (USD)", usd(st, 2))
        d(f"réflexion moyenne {t} : avec la marge de 10 % (USD)", usd(st * F("1.1"), 2))
    st_haut = sous_total + cout(0, (CASES + APPELS_JUGE_PAR_JUGE) * ARGON_PROVISION) + CASES * (carbon_haut - carbon_appel)
    d("sous-total, Argon à sa provision entière à chaque appel et Carbon à la plus forte réflexion relevée ailleurs (USD)",
      usd(st_haut, 2))
    d("le même, marge de 10 % comprise (USD)", usd(st_haut * F("1.1"), 2))
    # ce que le plafond d'arrêt fait de ces chiffres
    cumul_avant_juges = proposeurs + aiguilleur
    d("cumul estimé avant les juges, sans la réflexion d'Argon (USD)", usd(cumul_avant_juges, 2))
    d("plafond dur de l'étape des juges à ce cumul (USD)", usd(max(F(50), PLAFOND_ARRET - cumul_avant_juges), 2))
    par_jeton = cout(0, CASES + APPELS_JUGE_PAR_JUGE)
    d("réflexion moyenne par appel d'Argon au-delà de laquelle le sous-total passe 150 USD (jetons)",
      math.floor((PLAFOND_ARRET - sous_total) / par_jeton))
    d("la même, les autres postes à leur marge de 10 % (jetons)",
      math.floor((PLAFOND_ARRET - sous_total * F("1.1")) / par_jeton))
    # par clé
    claude = (prop_claude + aiguilleur + juge_claude) * F("1.1")
    argon = (prop_argon + juge_argon) * F("1.1")
    carbon = prop_carbon * F("1.1")
    astra = prop_astra * F("1.1")
    d("part Claude estimée, marge comprise (USD)", usd(claude, 2))
    d("Argon estimé, marge comprise, sans sa réflexion (USD)", usd(argon, 2))
    d("Carbon estimé, marge comprise (USD)", usd(carbon, 2))
    d("clé de Google, estimation, marge comprise, sans la réflexion d'Argon (USD)", usd(argon + carbon, 2))
    d("Astra estimé, marge comprise (USD)", usd(astra, 2))
    d("somme des estimations par clé (USD)", usd(claude + argon + carbon + astra, 2))
    d("réflexion d'Argon sur la clé de Google, par millier de jetons moyens, marge comprise (USD)",
      usd((par_millier_prop + par_millier_juge) * F("1.1"), 2))
    d("rapport des bornes aux prix de ce jeu", usd(BORNES[1] / ps, 3))
    inconnus = set(a) - vus
    assert not inconnus, inconnus   # toute valeur attendue doit correspondre à un chiffre calculé
    return {"sous_total": sous_total, "prop_claude": prop_claude, "aiguilleur": aiguilleur}


# --- Jeu principal : prix déclarés, 4 et 20 (devis v11, § 1 à § 7) --------------------------------------------------
ATTENDUS_DECLARES = {
    "16 000 jetons de texte au prix de sortie (USD)": "0,320",
    "entrée d'un appel de juge (caractères)": "11014",
    "entrée d'un appel de juge, 3 caractères par jeton, marge 5 % (jetons)": "3855",
    "entrée d'un appel de juge, 4 caractères par jeton, marge 5 % (jetons)": "2892",
    "coût de cette entrée (USD)": "0,0154",
    "sortie comptée, réflexion dans le plafond de sortie (USD)": "0,6554",
    "pire cas d'un appel de juge d'Argon, réflexion dans le plafond (USD)": "0,6708",
    "sortie comptée, provision en plus du plafond de sortie (USD)": "0,9830",
    "pire cas d'un appel de juge d'Argon, provision en plus (USD)": "0,9985",
    "plafond de session des juges, au dixième, provision en plus (USD)": "1,00",
    "plafond de session des juges, au dixième, réflexion dans le plafond (USD)": "0,70",
    "entrée de juge couverte sous ce plafond, provision en plus (jetons)": "4240",
    "entrée de juge couverte sous ce plafond, réflexion dans le plafond (jetons)": "86160",
    "entrée de juge couverte un dixième de dollar plus haut, provision en plus (jetons)": "29240",
    "marge de ce plafond sur l'entrée de juge attendue, provision en plus (jetons)": "385",
    "texte restant d'Argon au plafond de sortie retenu (jetons)": "16384",
    "plus petit plafond de sortie d'Argon que la garde admet à cette provision (jetons)": "32384",
    "pire cas d'un appel de juge d'Argon à ce plus petit plafond, réflexion dans le plafond (USD)": "0,6631",
    "borne des plafonds de session (USD)": "600",
    "pire cas d'un appel de proposeur d'Argon, provision en plus (USD)": "0,9935",
    "pire cas d'un appel de proposeur d'Argon, réflexion dans le plafond (USD)": "0,6658",
    "pire cas d'un appel de Carbon en flux au plafond de sortie le plus haut, réflexion dans le plafond (USD)": "1,3212",
    "pire cas de Carbon au plafond de sortie 65 536 et à la provision 49 152, provision en plus (USD)": "2,3042",
    "provision de Carbon la plus haute sous 3,00 USD, provision en plus, plafond = provision + 16 000 (jetons)": "66738",
    "proposeurs Claude (USD)": "7,896", "proposeur Argon, par appel (USD)": "0,1330", "proposeur Argon (USD)": "2,128",
    "proposeur Astra (USD)": "4,416",
    "Carbon, par appel, prix plein (USD)": "0,4805", "proposeur Carbon (USD)": "7,688",
    "aiguilleur (USD)": "4,96", "juge Claude (USD)": "5,92", "juge Argon, par appel (USD)": "0,0167", "juge Argon (USD)": "2,676",
    "proposeurs, ensemble (USD)": "22,13", "juges, ensemble (USD)": "8,60",
    "sous-total, sans la réflexion d'Argon (USD)": "35,683",
    "marge de 10 % (USD)": "3,57", "total, marge comprise (USD)": "39,25",
    "Carbon, par appel, à la plus forte réflexion relevée ailleurs (USD)": "0,9625",
    "proposeur Carbon à cette réflexion (USD)": "15,40",
    "proposeur Carbon à cette réflexion, en plus de l'estimation (USD)": "7,71",
    "réflexion d'Argon, par millier de jetons moyens : proposeur (USD)": "0,32",
    "réflexion d'Argon, par millier de jetons moyens : juge (USD)": "3,20",
    "réflexion d'Argon, par millier de jetons moyens : ensemble (USD)": "3,52",
    "appels d'Argon dans la course": "176",
    "réflexion moyenne 2000 : proposeur Argon en plus (USD)": "0,64", "réflexion moyenne 2000 : juge Argon en plus (USD)": "6,40",
    "réflexion moyenne 2000 : sous-total (USD)": "42,72", "réflexion moyenne 2000 : avec la marge de 10 % (USD)": "47,00",
    "réflexion moyenne 4096 : proposeur Argon en plus (USD)": "1,31", "réflexion moyenne 4096 : juge Argon en plus (USD)": "13,11",
    "réflexion moyenne 4096 : sous-total (USD)": "50,10", "réflexion moyenne 4096 : avec la marge de 10 % (USD)": "55,11",
    "réflexion moyenne 8192 : proposeur Argon en plus (USD)": "2,62", "réflexion moyenne 8192 : juge Argon en plus (USD)": "26,21",
    "réflexion moyenne 8192 : sous-total (USD)": "64,52", "réflexion moyenne 8192 : avec la marge de 10 % (USD)": "70,97",
    "réflexion moyenne 16384 : proposeur Argon en plus (USD)": "5,24", "réflexion moyenne 16384 : juge Argon en plus (USD)": "52,43",
    "réflexion moyenne 16384 : sous-total (USD)": "93,36", "réflexion moyenne 16384 : avec la marge de 10 % (USD)": "102,69",
    "sous-total, Argon à sa provision entière à chaque appel et Carbon à la plus forte réflexion relevée ailleurs (USD)": "101,07",
    "le même, marge de 10 % comprise (USD)": "111,17",
    "cumul estimé avant les juges, sans la réflexion d'Argon (USD)": "27,09",
    "plafond dur de l'étape des juges à ce cumul (USD)": "122,91",
    "réflexion moyenne par appel d'Argon au-delà de laquelle le sous-total passe 150 USD (jetons)": "32476",
    "la même, les autres postes à leur marge de 10 % (jetons)": "31462",
    "part Claude estimée, marge comprise (USD)": "20,65",
    "Argon estimé, marge comprise, sans sa réflexion (USD)": "5,28",
    "Carbon estimé, marge comprise (USD)": "8,46",
    "clé de Google, estimation, marge comprise, sans la réflexion d'Argon (USD)": "13,74",
    "Astra estimé, marge comprise (USD)": "4,86",
    "somme des estimations par clé (USD)": "39,25",
    "réflexion d'Argon sur la clé de Google, par millier de jetons moyens, marge comprise (USD)": "3,87",
    "rapport des bornes aux prix de ce jeu": "2,075",
}
r = jeu("prix déclarés", DECLARES, ATTENDUS_DECLARES)
print()
dire("proposeur Carbon au devis v10 (USD)", usd(CASES * CARBON_PRIX_LOT_V10, 3), "7,976")
dire("total v10, marge comprise (USD)", usd(SOUS_TOTAL_V10 * F("1.1"), 2), "45,25")
dire("sous-total v10 moins sous-total v11 (USD)", usd(SOUS_TOTAL_V10 - r["sous_total"], 3), "5,453")
dire("borne des plafonds de session, v10 (USD)",
     usd(APPELS_PROPOSEURS * PS_PROPOSEUR + APPELS_AIGUILLEUR * PS_AIGUILLEUR + 2 * APPELS_JUGE_PAR_JUGE * PS_JUGE_V10, 0), "472")
dire("part au pire de la clé de Google (USD)", usd(PLAFOND_ARRET + CASES * PS_PROPOSEUR, 2), "198,00")
dire("part au pire de la clé d'OpenAI (USD)", usd(CASES * PS_PROPOSEUR, 2), "48,00")
dire("plafond de la part Claude (USD)", usd(PLAFOND_PART_CLAUDE, 2), "45,00")
dire("part Claude engagée à partir de laquelle le relais refuse un appel (USD)",
     usd(PLAFOND_PART_CLAUDE - RESERVE_RELAIS_CLAUDE, 2), "44,60")
dire("part Claude estimée après la proposition (USD)", usd(r["prop_claude"] * F("1.1"), 2), "8,69")
dire("part Claude estimée après l'aiguillage (USD)", usd((r["prop_claude"] + r["aiguilleur"]) * F("1.1"), 2), "14,14")

# --- Comparaison : bornes des v6 à v10 (devis v11, § 8) ------------------------------------------------------------
ATTENDUS_BORNES = {
    "16 000 jetons de texte au prix de sortie (USD)": "0,664",
    "pire cas d'un appel de juge d'Argon, réflexion dans le plafond (USD)": "1,3919",
    "pire cas d'un appel de juge d'Argon, provision en plus (USD)": "2,0718",
    "plafond de session des juges, au dixième, provision en plus (USD)": "2,10",
    "plafond de session des juges, au dixième, réflexion dans le plafond (USD)": "1,40",
    "borne des plafonds de session (USD)": "952",
    "pire cas d'un appel de Carbon en flux au plafond de sortie le plus haut, réflexion dans le plafond (USD)": "2,7415",
    "pire cas de Carbon au plafond de sortie 65 536 et à la provision 49 152, provision en plus (USD)": "4,7813",
    "provision de Carbon la plus haute sous 3,00 USD, provision en plus, plafond = provision + 16 000 (jetons)": "27882",
    "proposeur Argon (USD)": "4,416", "Carbon, par appel, prix plein (USD)": "0,9970", "proposeur Carbon (USD)": "15,952",
    "juge Argon (USD)": "5,552",
    "sous-total, sans la réflexion d'Argon (USD)": "49,112", "total, marge comprise (USD)": "54,02",
    "réflexion d'Argon, par millier de jetons moyens : ensemble (USD)": "7,30",
    "réflexion moyenne 16384 : sous-total (USD)": "168,78",
    "réflexion moyenne par appel d'Argon au-delà de laquelle le sous-total passe 150 USD (jetons)": "13812",
    "la même, les autres postes à leur marge de 10 % (jetons)": "13140",
    "juges, ensemble (USD)": "11,47",
    "rapport des bornes aux prix de ce jeu": "1,000",
}
rb = jeu("bornes des v6 à v10", BORNES, ATTENDUS_BORNES)
assert SOUS_TOTAL_V10 == rb["sous_total"] - CASES * ((CARBON_ENTREE * BORNES[0] + (CARBON_REFLEXION + CARBON_REPONSE) * BORNES[1]) / M) \
    + CASES * CARBON_PRIX_LOT_V10

# --- Comparaison : page de prix, jusqu'au 30 novembre (devis v11, § 8) ---------------------------------------------
ATTENDUS_NOVEMBRE = {
    "pire cas d'un appel de juge d'Argon, provision en plus (USD)": "0,4992",
    "plafond de session des juges, au dixième, provision en plus (USD)": "0,50",
    "pire cas de Carbon au plafond de sortie 65 536 et à la provision 49 152, provision en plus (USD)": "1,1521",
    "réflexion moyenne 16384 : sous-total (USD)": "58,27",
    "réflexion moyenne par appel d'Argon au-delà de laquelle le sous-total passe 150 USD (jetons)": "68501",
    "sous-total, sans la réflexion d'Argon (USD)": "29,438", "total, marge comprise (USD)": "32,38",
    "réflexion d'Argon, par millier de jetons moyens : ensemble (USD)": "1,76",
    "rapport des bornes aux prix de ce jeu": "4,150",
}
jeu("page, jusqu'au 30 novembre", PAGE_NOVEMBRE, ATTENDUS_NOVEMBRE)

# --- Seuil de la recharge automatique de la clé LUC (devis v11b, § 5 bis) -------------------------------------------
SEUIL_RECHARGE_LUC = F(5)             # USD, lu par Lazar à la console le 22 novembre 2026 (R-5042)


def pct(x):
    return str(math.floor(x * 100 + F(1, 2)))


print("\n=== seuil de la recharge automatique de la clé LUC : 5 USD ===")
juge_claude_total = APPELS_JUGE_PAR_JUGE * P_JUGE_CLAUDE
part_claude_sans_marge = r["prop_claude"] + r["aiguilleur"] + juge_claude_total
dire("part Claude estimée, sans marge (USD)", usd(part_claude_sans_marge, 3), "18,776")
dire("seuil rapporté à la part Claude estimée, sans marge (%)", pct(SEUIL_RECHARGE_LUC / part_claude_sans_marge), "27")
dire("seuil rapporté à la part Claude estimée, marge comprise (%)",
     pct(SEUIL_RECHARGE_LUC / (part_claude_sans_marge * F("1.1"))), "24")
dire("seuil rapporté à la part Claude de la proposition (%)", pct(SEUIL_RECHARGE_LUC / r["prop_claude"]), "63")
dire("seuil rapporté à l'aiguillage (%)", pct(SEUIL_RECHARGE_LUC / r["aiguilleur"]), "101")
dire("seuil rapporté à la part Claude des juges (%)", pct(SEUIL_RECHARGE_LUC / juge_claude_total), "84")
dire("appels estimés du proposeur de la première espèce Claude pour dépenser le seuil", math.ceil(SEUIL_RECHARGE_LUC / P_CLAUDE_1), "36")
dire("appels estimés du proposeur de la seconde espèce Claude pour dépenser le seuil", math.ceil(SEUIL_RECHARGE_LUC / P_CLAUDE_2), "15")
dire("appels estimés de l'aiguilleur pour dépenser le seuil", math.ceil(SEUIL_RECHARGE_LUC / P_AIGUILLEUR), "162")
dire("appels estimés du juge Claude pour dépenser le seuil", math.ceil(SEUIL_RECHARGE_LUC / P_JUGE_CLAUDE), "136")
dire("appels de chaque proposeur Claude dans la course", CASES, "16")
dire("appels de l'aiguilleur, et du juge Claude, dans la course", APPELS_AIGUILLEUR, "160")
PS_JUGE_V11 = F("1.00")
dire("sessions de proposeur à leur plafond de 3,00 USD pour dépenser le seuil", math.ceil(SEUIL_RECHARGE_LUC / PS_PROPOSEUR), "2")
dire("sessions de juge à leur plafond de 1,00 USD pour dépenser le seuil", math.ceil(SEUIL_RECHARGE_LUC / PS_JUGE_V11), "5")
dire("sessions d'aiguilleur à leur plafond de 0,25 USD pour dépenser le seuil", math.ceil(SEUIL_RECHARGE_LUC / PS_AIGUILLEUR), "20")

echecs = [(n, v, a) for n, v, a in controles if v != a]
for n, v, a in echecs:
    print(f"ÉCART : {n} : calculé {v}, écrit {a}", file=sys.stderr)
print(f"\n{len(controles)} chiffres contrôlés, {len(echecs)} écart(s)")
sys.exit(1 if echecs else 0)
