#!/usr/bin/env python3
"""Calcul des chiffres du devis v11c de la course d'affinage des idées des mentors.

v11c : le programme du devis v11b (`calcul-devis-course-affinage-mentors-v11b.py`,
`cf316ba4db4005e2d64a114f4f4aea93187ebfa372a3bf072594e5513f8cd0e6`) refait aux réglages d'Argon du lanceur (provision de
réflexion 24 576 jetons, sortie maximale 45 056, en flux ; lanceurs v11 à v11c) et à la seule lecture « réflexion comprise
dans la sortie maximale » (page de Google versée sur `main`, `fe0b8d88…`, l. 914-916, 1220-1222 et 1273-1274 ; contre-lecture
du lanceur v11b, `cd7e5455…`). Les chiffres qui ne dépendent pas de ces réglages (estimation, part Claude, parts au pire par
clé, seuil de recharge de la clé LUC) sont recalculés à l'identique du v11b et contrôlés aux mêmes valeurs.
Écrit par Opus 5.5 en effort maximal (GO-2026-11-22-145 ; écart à R-3735 et à GO-2026-11-21-75 déclaré au devis v11c).

Aucun appel, aucun réseau, aucune lecture de fichier : toutes les entrées sont écrites ici, avec leur source.
Usage : python3 -I calcul-devis-course-affinage-mentors-v11c.py
Sortie : une ligne par chiffre du devis v11c (et du brouillon 4 du préenregistrement v11 qui le cite) ; code 0 si tous les
contrôles passent. Arithmétique exacte (fractions) ; les arrondis sont faits à l'affichage seulement, au plus proche.

Trois jeux de prix pour Argon et Carbon (USD par million de jetons, entrée et sortie) :
  - « prix déclarés » : 4 et 20, prix le plus haut de la page de prix versée (à partir du 1er décembre 2026), R-5018 :
    devis v11c, § 1 à § 7 ;
  - « bornes des v6 à v10 » : 8,3 et 41,5 : devis v11c, § 8 ;
  - « page, jusqu'au 30 novembre » : 2 et 10 (même page) : devis v11c, § 8.
"""
from fractions import Fraction as F
import json
import math
import sys

M = 10 ** 6

# --- Entrées, avec leur source -------------------------------------------------------------------------------------
DECLARES = (F(4), F(20))              # page de prix versée du 22 novembre, l. 153-163 (Carbon) et 372-382 (Argon) ; R-5018
BORNES = (F("8.3"), F("41.5"))        # commande d'Argon des v6 à v10, l. 345-346, et enveloppe l. 29 ; R-3271 pour Carbon
PAGE_NOVEMBRE = (F(2), F(10))         # même page, « through November 30, 2026 »
CASES = 16                            # seize fils servis
ESPECES = 5                           # deux Claude, Argon, Astra, Carbon
CARTES = CASES * ESPECES * 2          # deux cartes par appel de proposeur : 160
APPELS_PROPOSEURS = CASES * ESPECES   # 80
APPELS_AIGUILLEUR = CARTES            # 160
APPELS_JUGE_PAR_JUGE = CARTES         # 160 par juge, deux juges
# Prix par appel du devis v6 (§ 1 et § 2), repris par les devis v8 à v11b ; ceux d'Argon y sont comptés aux bornes
P_CLAUDE_1, P_CLAUDE_2 = F("0.141"), F("0.3525")
P_HORS_CLAUDE = F("0.276")            # Argon (mesuré, aux bornes, sans la garde), Astra (supposé)
P_AIGUILLEUR, P_JUGE_CLAUDE, P_JUGE_ARGON = F("0.031"), F("0.037"), F("0.0347")
# Carbon, hypothèses du devis v10, § 2
CARBON_ENTREE, CARBON_REFLEXION, CARBON_REPONSE = 2618, 20000, 3500
CARBON_PRIX_LOT_V10 = F("0.4985")     # devis v10, § 2 (prix du lot, aux bornes)
CARBON_REFLEXION_HAUTE = 44101        # plus forte réflexion de Carbon en flux relevée dans le collisionneur (note f6342515…, § 3)
SOUS_TOTAL_V10 = F("41.136")          # devis v10, § 3
# Plafonds de session (configuration v9 : proposeur 3,00 ; aiguilleur 0,25 ; juge 0,60 ; v11 : juge 1,00, R-5018)
PS_PROPOSEUR, PS_AIGUILLEUR, PS_JUGE_V10, PS_JUGE_V11 = F("3.00"), F("0.25"), F("0.60"), F("1.00")
PLAFOND_ARRET = F(150)
# Garde gelée des appels aux modèles de Google (garde commune v3, `src/controle_ia/garde_google_v3.py`, 923679b5…,
# LIMITES_SORTIE : Argon et Carbon à 65 536 en flux, 32 768 hors flux) et règle des 16 000 jetons de texte
TEXTE_MIN = 16000
LIMITE_FLUX, LIMITE_HORS_FLUX = 65536, 32768
# Réglages des commandes en flux, arguments épinglés des lanceurs v11, v11b et du brouillon v11c (ARGUMENTS_COMMANDES)
ARGON_PROVISION, ARGON_SORTIE = 24576, 45056      # niveau « high » ; provision SUPPOSÉE par le développeur (rapport v11)
CARBON_PROVISION, CARBON_SORTIE = 28672, 65536    # niveau « high »
ARGON_PROVISION_V11B, ARGON_SORTIE_V11B = 16384, 32768   # réglages sur lesquels chiffraient le devis v11b et le brouillon 3
CARBON_PROVISION_V11B = 49152                            # provision de Carbon du devis v11b (note 9cf6799f…, § 3)
CARTES_PAR_APPEL, CARACTERES_PAR_CARTE = 2, 9000         # consigne du proposeur ; limite de l'invite contrôlée par le lanceur
# Entrée d'un appel de juge
CONSIGNE_JUGE_CARACTERES = 1514       # course-v1/consigne-juge-course-affinage-mentors-v1.md, a32583b1… : 1 563 octets, 1 514
CONSIGNE_JUGE_SANS_FIN = 1513         # caractères ; 1 513 sans le saut de ligne final (`rstrip`, entrée bâtie par le lanceur v11c)
CARTE_CARACTERES_MAX = 9000           # consigne du proposeur, l. 20
CADRE_DEVIS = 500                     # cadre supposé par le devis (entrée attendue)
CADRE_LANCEUR = 1000                  # cadre supposé par les lanceurs v11b et v11c (pire cas contrôlé avant le départ)
MARGE_ENTREE = F("0.05")              # commande en flux : entrée gardée = ⌈caractères / 3 × 1,05⌉ (au moins)
ENTREE_LA_PLUS_LONGUE = 2618          # jetons : 7 478 caractères, fil le plus long (devis v10, § 1 ; rapport du lanceur v11)
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


def au_centime_superieur(x):
    return F(math.ceil(x * 100), 100)


def jetons_gardes(caracteres):
    return math.ceil(F(caracteres, 3) * (1 + MARGE_ENTREE))


def entree_juge_v11c():
    """Entrée de juge que bâtit le brouillon du lanceur v11c (`entree_juge_la_plus_longue`, forme de l'orchestrateur épinglé,
    `pole/fiches_v54.py`, `entree_une_fiche`) : consigne du juge sans saut de ligne final, « ## La fiche », fiche JSON indentée
    (identifiant de six signes, carte de 9 000 caractères, cadre de 1 000 caractères), en caractères."""
    fiche = {"identifiant": "F" + "x" * 5, "carte": "é" * CARTE_CARACTERES_MAX, "cadre": "é" * CADRE_LANCEUR}
    corps = json.dumps(fiche, ensure_ascii=False, indent=1)
    return CONSIGNE_JUGE_SANS_FIN + len("\n\n## La fiche\n```json\n") + len(corps) + len("\n```\n")


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

    # réglages d'Argon et de Carbon (garde gelée, limite de l'invite)
    texte_argon, texte_carbon = ARGON_SORTIE - ARGON_PROVISION, CARBON_SORTIE - CARBON_PROVISION
    limite_invite = CARTES_PAR_APPEL * CARACTERES_PAR_CARTE
    assert texte_argon >= TEXTE_MIN and texte_argon > limite_invite and ARGON_SORTIE <= LIMITE_FLUX
    assert texte_carbon >= TEXTE_MIN and texte_carbon > limite_invite and CARBON_SORTIE <= LIMITE_FLUX
    assert ARGON_SORTIE > LIMITE_HORS_FLUX            # Argon doit passer en flux à ces réglages
    d("texte d'Argon au-delà de la provision (jetons)", texte_argon)
    d("texte de Carbon au-delà de la provision (jetons)", texte_carbon)
    d("limite de l'invite d'un proposeur (caractères)", limite_invite)
    d("texte d'Argon aux réglages du devis v11b (jetons)", ARGON_SORTIE_V11B - ARGON_PROVISION_V11B)
    d("16 000 jetons de texte au prix de sortie (USD)", usd(cout(0, TEXTE_MIN), 3))
    # entrées d'un appel de juge
    c_devis = CONSIGNE_JUGE_CARACTERES + CARTE_CARACTERES_MAX + CADRE_DEVIS
    c_v11b = CONSIGNE_JUGE_CARACTERES + CARTE_CARACTERES_MAX + CADRE_LANCEUR
    c_v11c = entree_juge_v11c()
    e_devis, e_v11b, e_v11c = jetons_gardes(c_devis), jetons_gardes(c_v11b), jetons_gardes(c_v11c)
    d("entrée de juge attendue (caractères)", c_devis)
    d("entrée de juge attendue (jetons)", e_devis)
    d("entrée de juge du lanceur v11b (caractères)", c_v11b)
    d("entrée de juge du lanceur v11b (jetons)", e_v11b)
    d("entrée de juge du brouillon du lanceur v11c (caractères)", c_v11c)
    d("entrée de juge du brouillon du lanceur v11c (jetons)", e_v11c)
    d("coût de l'entrée de juge attendue (USD)", usd(cout(e_devis, 0), 4))
    # pire cas d'un appel de juge d'Argon, la réflexion comprise dans la sortie maximale
    sortie = cout(0, ARGON_SORTIE)
    d("sortie maximale d'Argon au prix de sortie (USD)", usd(sortie, 5))
    pj_devis, pj_v11b, pj_v11c = cout(e_devis, ARGON_SORTIE), cout(e_v11b, ARGON_SORTIE), cout(e_v11c, ARGON_SORTIE)
    d("pire cas d'un appel de juge d'Argon, entrée attendue (USD)", usd(pj_devis, 5))
    d("pire cas d'un appel de juge d'Argon, entrée du lanceur v11b (USD)", usd(pj_v11b, 6))
    d("pire cas d'un appel de juge d'Argon, entrée du brouillon v11c (USD)", usd(pj_v11c, 6))
    d("plafond minimal au centime, lanceur v11b (USD)", usd(au_centime_superieur(pj_v11b), 2))
    d("plafond minimal au centime, brouillon v11c (USD)", usd(au_centime_superieur(pj_v11c), 2))
    pj_max = max(pj_devis, pj_v11b, pj_v11c)
    plafond_juges = au_dixieme_superieur(pj_max)
    d("plafond de session des juges, au dixième (USD)", usd(plafond_juges, 2))
    couverte = math.floor((plafond_juges - sortie) * M / pe)
    d("entrée de juge couverte sous ce plafond (jetons)", couverte)
    d("marge sur l'entrée de juge du lanceur v11b (jetons)", couverte - e_v11b)
    d("marge sur l'entrée de juge du brouillon v11c (jetons)", couverte - e_v11c)
    d("marge sous le plafond, entrée du lanceur v11b (USD)", usd(plafond_juges - pj_v11b, 6))
    d("marge sous le plafond, entrée du brouillon v11c (USD)", usd(plafond_juges - pj_v11c, 6))
    # repère : la convention retirée (provision ajoutée à la sortie maximale)
    d("repère : juge d'Argon si la provision s'ajoutait à la sortie maximale, entrée du lanceur v11b (USD)",
      usd(cout(e_v11b, ARGON_SORTIE + ARGON_PROVISION), 4))
    # anciens chiffres du devis v11b (réglages 16 384 / 32 768), pour le différentiel
    d("v11b : juge d'Argon, réflexion dans la sortie maximale (USD)", usd(cout(e_devis, ARGON_SORTIE_V11B), 4))
    d("v11b : juge d'Argon, provision en plus (USD)", usd(cout(e_devis, ARGON_SORTIE_V11B + ARGON_PROVISION_V11B), 4))
    # proposeurs de Google sous le plafond de session d'un proposeur
    pp_argon = cout(ENTREE_LA_PLUS_LONGUE, ARGON_SORTIE)
    p_carbon = cout(ENTREE_LA_PLUS_LONGUE, CARBON_SORTIE)
    d("pire cas d'un appel de proposeur d'Argon (USD)", usd(pp_argon, 6))
    d("pire cas d'un appel de Carbon (USD)", usd(p_carbon, 6))
    d("pire cas d'un appel de Carbon, arrondi (USD)", usd(p_carbon, 4))
    d("pire cas d'un appel de Carbon, au centime (USD)", usd(p_carbon, 2))
    d("repère : Carbon si sa provision s'ajoutait à la sortie maximale (USD)",
      usd(cout(ENTREE_LA_PLUS_LONGUE, CARBON_SORTIE + CARBON_PROVISION), 4))
    d("v11b : Carbon à la provision 49 152 en plus de 65 536 (USD)",
      usd(cout(ENTREE_LA_PLUS_LONGUE, CARBON_SORTIE + CARBON_PROVISION_V11B), 4))
    assert pp_argon < PS_PROPOSEUR and p_carbon < PS_PROPOSEUR
    borne = APPELS_PROPOSEURS * PS_PROPOSEUR + APPELS_AIGUILLEUR * PS_AIGUILLEUR + 2 * APPELS_JUGE_PAR_JUGE * plafond_juges
    d("borne des plafonds de session (USD)", usd(borne, 0))
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
    d("proposeur Argon, par appel, au millionième (USD)", usd(P_HORS_CLAUDE * echelle, 6))
    d("proposeur Argon (USD)", usd(prop_argon, 3))
    d("proposeur Astra (USD)", usd(prop_astra, 3))
    d("Carbon, par appel, prix plein (USD)", usd(carbon_appel, 4))
    d("Carbon, par appel, au millionième (USD)", usd(carbon_appel, 6))
    d("proposeur Carbon (USD)", usd(prop_carbon, 3))
    d("aiguilleur (USD)", usd(aiguilleur, 2))
    d("juge Claude (USD)", usd(juge_claude, 2))
    d("juge Argon, par appel (USD)", usd(P_JUGE_ARGON * echelle, 4))
    d("juge Argon, par appel, au millionième (USD)", usd(P_JUGE_ARGON * echelle, 6))
    d("juge Argon (USD)", usd(juge_argon, 3))
    proposeurs = prop_claude + prop_argon + prop_astra + prop_carbon
    sous_total = proposeurs + aiguilleur + juge_claude + juge_argon
    d("proposeurs, ensemble (USD)", usd(proposeurs, 2))
    d("juges, ensemble (USD)", usd(juge_claude + juge_argon, 2))
    d("sous-total, sans la réflexion d'Argon (USD)", usd(sous_total, 3))
    d("sous-total, sans la réflexion d'Argon, au centime (USD)", usd(sous_total, 2))
    d("sous-total, sans la réflexion d'Argon, au millionième (USD)", usd(sous_total, 6))

    def au_millionieme(x):
        return F(math.floor(x * M + F(1, 2)), M)

    # base du lanceur v11c (brouillon) : mêmes postes, prix par appel d'Argon et de Carbon arrondis au millionième d'abord
    sous_total_lanceur = (prop_claude + CASES * au_millionieme(P_HORS_CLAUDE * echelle) + prop_astra
                          + CASES * au_millionieme(carbon_appel) + aiguilleur + juge_claude
                          + APPELS_JUGE_PAR_JUGE * au_millionieme(P_JUGE_ARGON * echelle))
    d("sous-total, prix par appel arrondis au millionième comme le lanceur v11c (USD)", usd(sous_total_lanceur, 6))
    d("les deux sous-totaux, au millième (USD)", f"{usd(sous_total, 3)} ; {usd(sous_total_lanceur, 3)}")
    d("marge de 10 % (USD)", usd(sous_total / 10, 2))
    d("total, marge comprise (USD)", usd(sous_total * F("1.1"), 2))
    carbon_haut = cout(CARBON_ENTREE, CARBON_REFLEXION_HAUTE + CARBON_REPONSE)
    d("Carbon, par appel, à la plus forte réflexion relevée ailleurs (USD)", usd(carbon_haut, 4))
    d("proposeur Carbon à cette réflexion (USD)", usd(CASES * carbon_haut, 2))
    d("proposeur Carbon à cette réflexion, en plus de l'estimation (USD)", usd(CASES * (carbon_haut - carbon_appel), 2))
    d("proposeur Carbon, chaque appel à son pire cas (USD)", usd(CASES * p_carbon, 2))
    # réflexion d'Argon
    par_millier_prop = cout(0, CASES * 1000)
    par_millier_juge = cout(0, APPELS_JUGE_PAR_JUGE * 1000)
    d("réflexion d'Argon, par millier de jetons moyens : proposeur (USD)", usd(par_millier_prop, 2))
    d("réflexion d'Argon, par millier de jetons moyens : juge (USD)", usd(par_millier_juge, 2))
    d("réflexion d'Argon, par millier de jetons moyens : ensemble (USD)", usd(par_millier_prop + par_millier_juge, 2))
    d("appels d'Argon dans la course", CASES + APPELS_JUGE_PAR_JUGE)
    par_jeton = cout(0, CASES + APPELS_JUGE_PAR_JUGE)
    seuil = math.floor((PLAFOND_ARRET - sous_total) / par_jeton)
    seuil_marge = math.floor((PLAFOND_ARRET - sous_total * F("1.1")) / par_jeton)
    for t in (2000, 4096, 8192, 16384, ARGON_PROVISION, seuil, ARGON_SORTIE):
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
    cumul_prov = cumul_avant_juges + cout(0, CASES * ARGON_PROVISION)
    juges_prov = juge_claude + juge_argon + cout(0, APPELS_JUGE_PAR_JUGE * ARGON_PROVISION)
    d("cumul avant les juges, Argon à sa provision (USD)", usd(cumul_prov, 2))
    d("plafond dur de l'étape des juges, Argon à sa provision (USD)", usd(max(F(50), PLAFOND_ARRET - cumul_prov), 2))
    d("coût de l'étape des juges, Argon à sa provision (USD)", usd(juges_prov, 2))
    d("étape des juges coupée, Argon à sa provision", "oui" if juges_prov > PLAFOND_ARRET - cumul_prov else "non")
    d("réflexion moyenne par appel d'Argon au-delà de laquelle le sous-total passe 150 USD (jetons)", seuil)
    d("la même, les autres postes à leur marge de 10 % (jetons)", seuil_marge)
    d("écart du seuil à la provision d'Argon (jetons)", seuil - ARGON_PROVISION)
    d("écart du seuil à la sortie maximale d'Argon (jetons)", ARGON_SORTIE - seuil)
    argon_pire_prop = CASES * pp_argon
    argon_pire_juge = APPELS_JUGE_PAR_JUGE * pj_v11b
    d("Argon, proposeur, chaque appel à son pire cas (USD)", usd(argon_pire_prop, 2))
    d("Argon, juge, chaque appel à son pire cas, entrée du lanceur v11b (USD)", usd(argon_pire_juge, 2))
    d("Argon, ses 176 appels à leur pire cas (USD)", usd(argon_pire_prop + argon_pire_juge, 2))
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


# --- Jeu principal : prix déclarés, 4 et 20 (devis v11c, § 1 à § 7) -------------------------------------------------
ATTENDUS_DECLARES = {
    "texte d'Argon au-delà de la provision (jetons)": "20480",
    "texte de Carbon au-delà de la provision (jetons)": "36864",
    "limite de l'invite d'un proposeur (caractères)": "18000",
    "texte d'Argon aux réglages du devis v11b (jetons)": "16384",
    "16 000 jetons de texte au prix de sortie (USD)": "0,320",
    "entrée de juge attendue (caractères)": "11014",
    "entrée de juge attendue (jetons)": "3855",
    "entrée de juge du lanceur v11b (caractères)": "11514",
    "entrée de juge du lanceur v11b (jetons)": "4030",
    "entrée de juge du brouillon du lanceur v11c (caractères)": "11596",
    "entrée de juge du brouillon du lanceur v11c (jetons)": "4059",
    "coût de l'entrée de juge attendue (USD)": "0,0154",
    "sortie maximale d'Argon au prix de sortie (USD)": "0,90112",
    "pire cas d'un appel de juge d'Argon, entrée attendue (USD)": "0,91654",
    "pire cas d'un appel de juge d'Argon, entrée du lanceur v11b (USD)": "0,917240",
    "pire cas d'un appel de juge d'Argon, entrée du brouillon v11c (USD)": "0,917356",
    "plafond minimal au centime, lanceur v11b (USD)": "0,92",
    "plafond minimal au centime, brouillon v11c (USD)": "0,92",
    "plafond de session des juges, au dixième (USD)": "1,00",
    "entrée de juge couverte sous ce plafond (jetons)": "24720",
    "marge sur l'entrée de juge du lanceur v11b (jetons)": "20690",
    "marge sur l'entrée de juge du brouillon v11c (jetons)": "20661",
    "marge sous le plafond, entrée du lanceur v11b (USD)": "0,082760",
    "marge sous le plafond, entrée du brouillon v11c (USD)": "0,082644",
    "repère : juge d'Argon si la provision s'ajoutait à la sortie maximale, entrée du lanceur v11b (USD)": "1,4088",
    "v11b : juge d'Argon, réflexion dans la sortie maximale (USD)": "0,6708",
    "v11b : juge d'Argon, provision en plus (USD)": "0,9985",
    "pire cas d'un appel de proposeur d'Argon (USD)": "0,911592",
    "pire cas d'un appel de Carbon (USD)": "1,321192",
    "pire cas d'un appel de Carbon, arrondi (USD)": "1,3212",
    "pire cas d'un appel de Carbon, au centime (USD)": "1,32",
    "repère : Carbon si sa provision s'ajoutait à la sortie maximale (USD)": "1,8946",
    "v11b : Carbon à la provision 49 152 en plus de 65 536 (USD)": "2,3042",
    "borne des plafonds de session (USD)": "600",
    "proposeurs Claude (USD)": "7,896", "proposeur Argon, par appel (USD)": "0,1330",
    "proposeur Argon, par appel, au millionième (USD)": "0,133012", "proposeur Argon (USD)": "2,128",
    "proposeur Astra (USD)": "4,416",
    "Carbon, par appel, prix plein (USD)": "0,4805", "Carbon, par appel, au millionième (USD)": "0,480472",
    "proposeur Carbon (USD)": "7,688",
    "aiguilleur (USD)": "4,96", "juge Claude (USD)": "5,92", "juge Argon, par appel (USD)": "0,0167",
    "juge Argon, par appel, au millionième (USD)": "0,016723", "juge Argon (USD)": "2,676",
    "proposeurs, ensemble (USD)": "22,13", "juges, ensemble (USD)": "8,60",
    "sous-total, sans la réflexion d'Argon (USD)": "35,683",
    "sous-total, sans la réflexion d'Argon, au centime (USD)": "35,68",
    "sous-total, sans la réflexion d'Argon, au millionième (USD)": "35,683407",
    "sous-total, prix par appel arrondis au millionième comme le lanceur v11c (USD)": "35,683424",
    "les deux sous-totaux, au millième (USD)": "35,683 ; 35,683",
    "marge de 10 % (USD)": "3,57", "total, marge comprise (USD)": "39,25",
    "Carbon, par appel, à la plus forte réflexion relevée ailleurs (USD)": "0,9625",
    "proposeur Carbon à cette réflexion (USD)": "15,40",
    "proposeur Carbon à cette réflexion, en plus de l'estimation (USD)": "7,71",
    "proposeur Carbon, chaque appel à son pire cas (USD)": "21,14",
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
    "réflexion moyenne 24576 : proposeur Argon en plus (USD)": "7,86", "réflexion moyenne 24576 : juge Argon en plus (USD)": "78,64",
    "réflexion moyenne 24576 : sous-total (USD)": "122,19", "réflexion moyenne 24576 : avec la marge de 10 % (USD)": "134,41",
    "réflexion moyenne 32476 : proposeur Argon en plus (USD)": "10,39", "réflexion moyenne 32476 : juge Argon en plus (USD)": "103,92",
    "réflexion moyenne 32476 : sous-total (USD)": "150,00", "réflexion moyenne 32476 : avec la marge de 10 % (USD)": "165,00",
    "réflexion moyenne 45056 : proposeur Argon en plus (USD)": "14,42", "réflexion moyenne 45056 : juge Argon en plus (USD)": "144,18",
    "réflexion moyenne 45056 : sous-total (USD)": "194,28", "réflexion moyenne 45056 : avec la marge de 10 % (USD)": "213,71",
    "sous-total, Argon à sa provision entière à chaque appel et Carbon à la plus forte réflexion relevée ailleurs (USD)": "129,90",
    "le même, marge de 10 % comprise (USD)": "142,89",
    "cumul estimé avant les juges, sans la réflexion d'Argon (USD)": "27,09",
    "plafond dur de l'étape des juges à ce cumul (USD)": "122,91",
    "cumul avant les juges, Argon à sa provision (USD)": "34,95",
    "plafond dur de l'étape des juges, Argon à sa provision (USD)": "115,05",
    "coût de l'étape des juges, Argon à sa provision (USD)": "87,24",
    "étape des juges coupée, Argon à sa provision": "non",
    "réflexion moyenne par appel d'Argon au-delà de laquelle le sous-total passe 150 USD (jetons)": "32476",
    "la même, les autres postes à leur marge de 10 % (jetons)": "31462",
    "écart du seuil à la provision d'Argon (jetons)": "7900",
    "écart du seuil à la sortie maximale d'Argon (jetons)": "12580",
    "Argon, proposeur, chaque appel à son pire cas (USD)": "14,59",
    "Argon, juge, chaque appel à son pire cas, entrée du lanceur v11b (USD)": "146,76",
    "Argon, ses 176 appels à leur pire cas (USD)": "161,34",
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
dire("dépassement possible du plafond de la part Claude par appel de proposeur en vol (USD)",
     usd(PS_PROPOSEUR - RESERVE_RELAIS_CLAUDE, 2), "2,60")
dire("part Claude estimée après la proposition (USD)", usd(r["prop_claude"] * F("1.1"), 2), "8,69")
dire("part Claude estimée après l'aiguillage (USD)", usd((r["prop_claude"] + r["aiguilleur"]) * F("1.1"), 2), "14,14")

# --- Comparaison : bornes des v6 à v10 (devis v11c, § 8) -----------------------------------------------------------
ATTENDUS_BORNES = {
    "pire cas d'un appel de juge d'Argon, entrée du lanceur v11b (USD)": "1,903273",
    "plafond de session des juges, au dixième (USD)": "2,00",
    "borne des plafonds de session (USD)": "920",
    "pire cas d'un appel de proposeur d'Argon (USD)": "1,891553",
    "pire cas d'un appel de Carbon, arrondi (USD)": "2,7415",
    "proposeur Argon (USD)": "4,416", "Carbon, par appel, prix plein (USD)": "0,9970", "proposeur Carbon (USD)": "15,952",
    "juge Argon (USD)": "5,552",
    "sous-total, sans la réflexion d'Argon (USD)": "49,112", "total, marge comprise (USD)": "54,02",
    "réflexion d'Argon, par millier de jetons moyens : ensemble (USD)": "7,30",
    "réflexion moyenne 24576 : sous-total (USD)": "228,61",
    "étape des juges coupée, Argon à sa provision": "oui",
    "réflexion moyenne par appel d'Argon au-delà de laquelle le sous-total passe 150 USD (jetons)": "13812",
    "la même, les autres postes à leur marge de 10 % (jetons)": "13140",
    "juges, ensemble (USD)": "11,47",
    "Argon, ses 176 appels à leur pire cas (USD)": "334,79",
    "rapport des bornes aux prix de ce jeu": "1,000",
}
rb = jeu("bornes des v6 à v10", BORNES, ATTENDUS_BORNES)
assert SOUS_TOTAL_V10 == rb["sous_total"] - CASES * ((CARBON_ENTREE * BORNES[0] + (CARBON_REFLEXION + CARBON_REPONSE) * BORNES[1]) / M) \
    + CASES * CARBON_PRIX_LOT_V10

# --- Comparaison : page de prix, jusqu'au 30 novembre (devis v11c, § 8) --------------------------------------------
ATTENDUS_NOVEMBRE = {
    "pire cas d'un appel de juge d'Argon, entrée du lanceur v11b (USD)": "0,458620",
    "plafond de session des juges, au dixième (USD)": "0,50",
    "borne des plafonds de session (USD)": "440",
    "pire cas d'un appel de Carbon, arrondi (USD)": "0,6606",
    "proposeur Argon (USD)": "1,064", "proposeur Carbon (USD)": "3,844", "juge Argon (USD)": "1,338",
    "Carbon, par appel, prix plein (USD)": "0,2402",
    "étape des juges coupée, Argon à sa provision": "non",
    "réflexion moyenne 24576 : sous-total (USD)": "72,69",
    "réflexion moyenne par appel d'Argon au-delà de laquelle le sous-total passe 150 USD (jetons)": "68501",
    "sous-total, sans la réflexion d'Argon (USD)": "29,438", "total, marge comprise (USD)": "32,38",
    "réflexion d'Argon, par millier de jetons moyens : ensemble (USD)": "1,76",
    "Argon, ses 176 appels à leur pire cas (USD)": "80,67",
    "rapport des bornes aux prix de ce jeu": "4,150",
}
jeu("page, jusqu'au 30 novembre", PAGE_NOVEMBRE, ATTENDUS_NOVEMBRE)

# --- Seuil de la recharge automatique de la clé LUC (devis v11b et v11c, § 5 bis ; inchangé) -------------------------
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
dire("sessions de proposeur à leur plafond de 3,00 USD pour dépenser le seuil", math.ceil(SEUIL_RECHARGE_LUC / PS_PROPOSEUR), "2")
dire("sessions de juge à leur plafond de 1,00 USD pour dépenser le seuil", math.ceil(SEUIL_RECHARGE_LUC / PS_JUGE_V11), "5")
dire("sessions d'aiguilleur à leur plafond de 0,25 USD pour dépenser le seuil", math.ceil(SEUIL_RECHARGE_LUC / PS_AIGUILLEUR), "20")

echecs = [(n, v, a) for n, v, a in controles if v != a]
for n, v, a in echecs:
    print(f"ÉCART : {n} : calculé {v}, écrit {a}", file=sys.stderr)
print(f"\n{len(controles)} chiffres contrôlés, {len(echecs)} écart(s)")
sys.exit(1 if echecs else 0)
