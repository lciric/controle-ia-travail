#!/usr/bin/env python3
"""Recalcul des chiffres du devis de la banque d'épisodes de la famille aveugle de réserve du cycle 2 (v2).

Remplace le programme v1, resté à côté et intact, après la contre-lecture du devis v1. Bibliothèque standard seule ;
aucun réseau, aucun fichier lu, aucun hasard. Chaque constante porte sa source, telle que le devis la cite (chemin:ligne).
Lancer : python3 calcul-devis-banque-d-episodes-famille-reserve-cycle-2-v2.py
Trois lettres, comme au devis : M = relevé sur une pièce ; C = calculé ici ; S = supposé, sans mesure.

Ce qui change par rapport au programme v1, remarque par remarque de la contre-lecture :
- remarque 1 : repli chiffré si le lecteur Claude est écarté (Gemini 4 Neon et Mistral Large 4), section 11 ;
- remarque 2 : plafond de chaque file de lecture, par lecteur et par étape, séparé du pire cas d'un seul envoi, section 5 ;
- remarque 4 : marge de change de 5 % sur la part du compte Mistral, dont la devise n'est pas relevée, sections 5 et 7 ;
- remarque 6 : ce que le plafond ne couvre pas (mode rapide, géographie d'inférence, écriture du cache), section 3 ;
- remarque 7 : coût du lecteur Claude selon l'effort, section 10 ;
- remarque 8 : constantes de la lecture groupée et sorties de Neon nommées en tête et rappelées en section 12 ;
- remarque 9 : attendu bas de la carte au prix de l'offre, stockage compris ; prix d'une action à cinq décimales ;
- remarque 10 : minuterie du lancement 2 recalculée par la formule de son plafond, section 2 ;
- remarque 12 : variante à 200 épisodes par dose, section 8.
Les sections 1, 3 et 4 rendent les mêmes chiffres que le programme v1 (dollars comptés, sans marge de change).
"""
import math

# ---------- tailles de principe (pièce 6 de la famille, section 3) ----------
N_TACHES = 60        # M : pièce 6, section 3 (fichier des tâches du pilote)
E = 1                # M : pièce 6, section 3
N_F = 20             # M : pièce 6, section 3
A_PAS = 10           # S : réglage de la chaîne réemployée (devis du bras A v2, ligne 38) ; propositions.py:26 borne à 10
RELECTURES_EPREUVES = 60   # M : pièce 6 version 1, section 2, poste D (« de l'ordre de 3 x 20 ensembles »)
VALEURS_K = (3, 4, 6, 8)   # S : k, nombre moyen d'éléments lus par tâche, est au coffre ; le plafond se calcule à K_MAX
K_MAX = 8
K_CENTRE = 6

# ---------- carte louée ----------
D_HAUT, D_BAS = 42.8, 40.2      # M : secondes par épisode, devis du bras A v2, ligne 54 (autre chaîne : S pour ce banc)
MISE_EN_ROUTE_H = 1.0           # S : devis du bras A v2, ligne 56
PRIX_RELEVE_CARTE = 1.1833      # M : registres/depenses.md:515, carte seule (2026-11-18T15:44:24Z)
PRIX_RELEVE_OFFRE = 1.1843      # M : même ligne, offre, stockage compris ; retenu pour l'attendu bas (remarque 9)
PRIX_CARTE, STOCKAGE = 1.30, 0.08   # M : devis du bras A v2, lignes 67 et 69 (bornes)
PRIX_DEVIS = PRIX_CARTE + STOCKAGE  # C : 1,38
TEL_BAS, TEL_HAUT = 1.0, 2.0    # M : devis du bras A v2, ligne 69 (20 à 40 Go à 0,05 dollar par Go)
FACTEUR_PESSIMISTE = 4.0        # M (méthode) : devis du bras A v2, ligne 81 (débit deux fois plus lent, une relance complète)
TEL_PESSIMISTE = 4.0            # M (méthode) : même ligne (deux mises en route à 2 dollars)
MAJORATION_SABOTAGE = 1.5       # S : épisodes « sabotage demandé » supposés moitié plus longs, pour le plafond recalculé

# ---------- lecteurs : prix en dollars par million de jetons (entrée, sortie) ----------
PRIX = {
    "opus": (4.0, 20.0),            # M : page scellée d'Anthropic 78aff5c8… ; relais_reel.py:50 ; collisionneur_v9_v3.py:131
    "sonnet": (2.0, 10.0),          # M : même page ; relais_reel.py:51
    "mistral": (0.77, 2.31),        # C sur relevé non scellé : 0,70 et 2,10 x 1,1 (point d'accès européen), choix-mistral-deepseek-v1.md:19
    "mistral_repli": (1.54, 4.62),  # C : le double, tant que la page de prix de Mistral n'est pas versée et scellée
    "neon": (3.0, 15.0),            # M : page scellée de Google 89c58281…, section « Gemini 4 Neon », onglet « Standard »
}
ENTREE_ATT, ENTREE_PESS = 4000, 6000    # S : ordre de 4 000 jetons par plan (esquisse en clair du premier cycle, ligne 43)
SORTIE_ATT = {"opus": 500, "sonnet": 500, "mistral": 3000, "mistral_repli": 3000, "neon": 1500}     # S (Neon : remarque 8)
SORTIE_PESS = {"opus": 2000, "sonnet": 2000, "mistral": 9000, "mistral_repli": 9000, "neon": 6000}   # S (Neon : remarque 8)
ENVOIS_ATT, ENVOIS_PESS = 1.05, 1.15    # S : reprises et redemandes de forme, 5 % attendus, 15 % au plafond
ENTREE_GARDE, SORTIE_MAX_CLAUDE, SORTIE_MAX_MISTRAL = 24000, 8192, 16384   # M / M / S : garde par envoi (un jeton par octet)

# ---------- lecture groupée : un appel par ensemble, k questions dedans (S, remarque 8) ----------
GROUPE_ENTREE_PAR_QUESTION = 150    # S : jetons d'entrée ajoutés par question (un élément de référence de plus)
GROUPE_SORTIE_PAR_QUESTION = 150    # S : jetons de sortie par question (verdict et extrait cité)
GROUPE_REFLEXION = {"opus": 300, "sonnet": 300, "mistral": 3000, "mistral_repli": 3000, "neon": 1500}   # S : par appel

# ---------- marge de change (remarque 4) ----------
MARGE_CHANGE = 0.05   # M : 5 % acceptés par Lazar pour le bras A, registres/go.md:667 ; ici sur la part de Mistral (devise non relevée)

# ---------- ce que le plafond ne couvre pas (remarque 6), page scellée d'Anthropic 78aff5c8… ----------
PRIX_OPUS_RAPIDE = (8.0, 40.0)   # M : « Fast mode pricing », Claude Opus 5.5
FACTEUR_GEO_US = 1.1             # M : « Data residency pricing », inference_geo « us »
ECRITURE_CACHE_OPUS = 5.0        # M : tableau des modèles, « 5m writes » ; relais_reel.py:50

# ---------- effort du lecteur Claude (remarque 7) ----------
SORTIE_EFFORT = (("bas", 500), ("moyen", 1000), ("haut", 2000))   # S : bas et moyen d'après devis-essai…:144 ; haut sans source

# ---------- essai d'admission et de mesure ; ancre ----------
ENSEMBLES_ESSAI = 12      # S : 8 ensembles honnêtes et 4 de dose flagrante par lecteur
ELEMENTS_ANCRE = 30       # M : pièce 6 version 1, section 2 (ancre humaine sur 30 éléments)
ADMISSION_JUGE = 8        # M : précédent du bras A, registres/go.md:632 (huit lectures d'admission)


def dollars(x, n=2):
    return f"{x:.{n}f}".replace(".", ",")


def tronque(x, n=1):
    """Tronque vers le bas : une minuterie ne doit jamais permettre plus d'heures que le plafond n'en paie."""
    return math.floor(x * 10 ** n) / 10 ** n


def cout_question(modele, attendu=True, sortie=None, prix=None):
    pe, ps = prix if prix else PRIX[modele]
    if attendu:
        s = SORTIE_ATT[modele] if sortie is None else sortie
        return (ENTREE_ATT * pe + s * ps) * ENVOIS_ATT / 1e6
    s = SORTIE_PESS[modele] if sortie is None else sortie
    return (ENTREE_PESS * pe + s * ps) * ENVOIS_PESS / 1e6


def cout_ensemble_groupe(modele, k, attendu=True):
    """Variante « un appel par ensemble, k questions dedans » (S). Pessimiste : entrée x 1,5, sortie multipliée comme
    pour une question (SORTIE_PESS / SORTIE_ATT), envois x 1,15."""
    pe, ps = PRIX[modele]
    entree = ENTREE_ATT + GROUPE_ENTREE_PAR_QUESTION * k
    sortie = GROUPE_REFLEXION[modele] + GROUPE_SORTIE_PAR_QUESTION * k
    if attendu:
        return (entree * pe + sortie * ps) * ENVOIS_ATT / 1e6
    facteur_entree = ENTREE_PESS / ENTREE_ATT
    facteur_sortie = SORTIE_PESS[modele] / SORTIE_ATT[modele]
    return (entree * facteur_entree * pe + sortie * facteur_sortie * ps) * ENVOIS_PESS / 1e6


def lancement(nb_episodes):
    h = nb_episodes * D_HAUT / 3600 + MISE_EN_ROUTE_H
    h_bas = nb_episodes * D_BAS / 3600 + MISE_EN_ROUTE_H
    att_bas = h_bas * PRIX_RELEVE_OFFRE + TEL_BAS
    att_haut = h * PRIX_DEVIS + TEL_HAUT
    pire = h * FACTEUR_PESSIMISTE * PRIX_DEVIS + TEL_PESSIMISTE
    return h, att_bas, att_haut, pire, math.ceil(pire)


def heures_payees(plafond_non_arrondi):
    """Heures cumulées que le plafond paie, au prix du devis, téléchargement pessimiste retiré."""
    return (plafond_non_arrondi - TEL_PESSIMISTE) / PRIX_DEVIS


def lancement_2_recalcule(d, nb_episodes):
    """Plafond du lancement 2 sur le débit d mesuré au lancement 1 (secondes par épisode), et heures qu'il paie."""
    heures = 2 * (MISE_EN_ROUTE_H + nb_episodes * MAJORATION_SABOTAGE * d / 3600)
    return PRIX_DEVIS * heures + TEL_PESSIMISTE, heures


def volumes(n_taches, e, n_f):
    ep_a, ep_b, ep_c = 2 * n_taches * e, 2 * n_taches * e, n_f * e
    ens_1 = ep_a + ep_c + RELECTURES_EPREUVES      # étape 1 : honnêtes, dose flagrante, relectures des épreuves
    ens_2 = ep_b                                   # étape 2 : « sabotage demandé »
    return ep_a, ep_b, ep_c, ens_1, ens_2


def files(ensembles, k, l1="opus", l2="mistral_repli", marge_l1=0.0, marge_l2=MARGE_CHANGE, groupe=False):
    """Plafond de chaque file de lecture : dollars comptés par la garde, et engagement, marge de change comprise."""
    if groupe:
        c1 = ensembles * cout_ensemble_groupe(l1, k, False)
        c2 = ensembles * cout_ensemble_groupe(l2, k, False)
    else:
        c1 = ensembles * k * cout_question(l1, False)
        c2 = ensembles * k * cout_question(l2, False)
    e1, e2 = c1 * (1 + marge_l1), c2 * (1 + marge_l2)
    return c1, c2, e1, e2, math.ceil(e1 + e2)


def variante(n_x_e):
    ep_a, ep_b, ep_c, ens_1, ens_2 = volumes(n_x_e, 1, N_F)
    carte, carte2 = lancement(ep_a + ep_c), lancement(ep_b)
    att = cout_question("opus") + cout_question("mistral")
    lect_att = (ens_1 + ens_2) * K_CENTRE * att
    p1, p2 = files(ens_1, K_MAX)[4], files(ens_2, K_MAX)[4]
    essai = files(ENSEMBLES_ESSAI, K_MAX)[4]
    return (ep_a + ep_b + ep_c, ens_1 + ens_2, carte[1] + carte2[1], carte[2] + carte2[2], carte[4] + carte2[4],
            lect_att, p1 + p2, carte[4] + carte2[4] + p1 + p2 + essai)


def main():
    ep_a, ep_b, ep_c, ens_1, ens_2 = volumes(N_TACHES, E, N_F)
    print("== 1. Volumes (tailles de principe de la pièce 6, version 1) ==")
    print(f"épisodes honnêtes A = {ep_a} ; « sabotage demandé » B = {ep_b} ; dose flagrante C = {ep_c} ; total = {ep_a + ep_b + ep_c}")
    print(f"actions = {(ep_a + ep_b + ep_c) * A_PAS} (a = {A_PAS})")
    print(f"ensembles lus par lecteur : étape 1 = {ens_1} ; étape 2 = {ens_2} ; total = {ens_1 + ens_2}")
    for k in VALEURS_K:
        print(f"  k = {k} : questions par lecteur = {(ens_1 + ens_2) * k} (étape 1 : {ens_1 * k} ; étape 2 : {ens_2 * k})")
    mesure, controle = ep_a // 2 + ep_b, ep_a // 2 + ep_c
    print(f"part des contrôles : {controle} épisodes sur {mesure + controle} ({100 * controle / (mesure + controle):.0f} %) ; "
          f"{controle + RELECTURES_EPREUVES} ensembles lus sur {ens_1 + ens_2} ({100 * (controle + RELECTURES_EPREUVES) / (ens_1 + ens_2):.0f} %)")

    print("\n== 2. Carte : prix d'une action, lancements, minuteries ==")
    pa_bas, pa_haut = D_HAUT / A_PAS * PRIX_RELEVE_OFFRE / 3600, D_HAUT / A_PAS * PRIX_DEVIS / 3600
    print(f"prix d'une action p_a = {dollars(pa_bas, 5)} à {dollars(pa_haut, 5)} dollar ({dollars(D_HAUT / A_PAS, 2)} s par action ; "
          f"bas au prix de l'offre, stockage compris, {dollars(PRIX_RELEVE_OFFRE, 4)} ; haut à {dollars(PRIX_DEVIS)}) ; "
          f"arrondi au-dessus, à quatre décimales : {dollars(math.ceil(pa_bas * 1e4) / 1e4, 4)} à {dollars(math.ceil(pa_haut * 1e4) / 1e4, 4)} ; "
          f"par épisode : {dollars(D_HAUT * PRIX_RELEVE_OFFRE / 3600, 4)} à {dollars(D_HAUT * PRIX_DEVIS / 3600, 4)}")
    print(f"écart entre la carte seule ({dollars(PRIX_RELEVE_CARTE, 4)}) et l'offre, stockage compris ({dollars(PRIX_RELEVE_OFFRE, 4)}) : "
          f"{dollars(PRIX_RELEVE_OFFRE - PRIX_RELEVE_CARTE, 4)} dollar par heure, soit "
          f"{dollars((PRIX_RELEVE_OFFRE - PRIX_RELEVE_CARTE) * (lancement(ep_a + ep_c)[0] + lancement(ep_b)[0]), 3)} dollar sur les deux lancements")
    print(f"coût fixe d'un lancement : {dollars(MISE_EN_ROUTE_H * PRIX_RELEVE_OFFRE + TEL_BAS)} à {dollars(MISE_EN_ROUTE_H * PRIX_DEVIS + TEL_HAUT)} dollars")
    total_att_bas = total_att_haut = total_plafond = 0.0
    for nom, nb in (("lancement 1 (A et C)", ep_a + ep_c), ("lancement 2 (B)", ep_b)):
        h, att_bas, att_haut, pire, plafond = lancement(nb)
        total_att_bas += att_bas
        total_att_haut += att_haut
        total_plafond += plafond
        print(f"{nom} : {nb} épisodes ; {dollars(h)} h ; attendu {dollars(att_bas)} à {dollars(att_haut)} ; "
              f"pire cas {dollars(pire)} ; plafond {plafond} ; durée au pire {dollars(h * FACTEUR_PESSIMISTE)} h ; "
              f"heures que le pire cas paie {dollars(heures_payees(pire))} ; minuterie, tronquée : {dollars(tronque(heures_payees(pire)), 1)} h")
    h_tot = round(lancement(ep_a + ep_c)[0], 2) + round(lancement(ep_b)[0], 2)
    pire_tot = round(lancement(ep_a + ep_c)[3], 2) + round(lancement(ep_b)[3], 2)
    print(f"carte, total : attendu {dollars(total_att_bas)} à {dollars(total_att_haut)} ; plafond {total_plafond:.0f} ; "
          f"durée attendue {dollars(h_tot)} h ; pire cas {dollars(pire_tot)} ; marge du plafond sur l'attendu haut : "
          f"lancement 1 = {dollars(lancement(ep_a + ep_c)[4] - lancement(ep_a + ep_c)[2], 1)} ; "
          f"lancement 2 = {dollars(lancement(ep_b)[4] - lancement(ep_b)[2], 1)} ; total = {dollars(total_plafond - total_att_haut, 1)}")
    h, att_bas, att_haut, pire, plafond = lancement(ep_a + ep_b + ep_c)
    print(f"variante, un seul lancement (A, B et C) : {dollars(h)} h ; attendu {dollars(att_bas)} à {dollars(att_haut)} ; pire cas {dollars(pire)} ; plafond {plafond}")
    plafond_l2_recalc, heures_l2_recalc = lancement_2_recalcule(D_HAUT, ep_b)
    print(f"lancement 2 recalculé sur le débit d mesuré au lancement 1 (remarque 10) : heures = 2 x (1,0 + {ep_b} x 1,5 x d / 3600) ; "
          f"plafond = {dollars(PRIX_DEVIS)} x heures + 4 ; pour d = {dollars(D_HAUT, 1)} : plafond {dollars(plafond_l2_recalc)} ; "
          f"heures payées {dollars(heures_l2_recalc)} ; minuterie, tronquée : {dollars(tronque(heures_l2_recalc), 1)} h")
    plafond_l2 = lancement(ep_b)[4]
    d_max = ((plafond_l2 - TEL_PESSIMISTE) / (2 * PRIX_DEVIS) - MISE_EN_ROUTE_H) * 3600 / (ep_b * MAJORATION_SABOTAGE)
    print(f"débit au-delà duquel la formule sort du plafond de {plafond_l2} du lancement 2 : {dollars(d_max, 1)} s par épisode")
    carte_att_centre = (total_att_bas + total_att_haut) / 2
    carte_plafond = total_plafond

    print("\n== 3. Lecteurs : prix d'une lecture (une question, le plan renvoyé à chaque appel) ==")
    for m in ("opus", "sonnet", "mistral", "mistral_repli", "neon"):
        print(f"{m:14s} attendu {dollars(cout_question(m), 4)} ; pessimiste {dollars(cout_question(m, False), 4)}")
    envoi_opus = (ENTREE_GARDE * PRIX["opus"][0] + SORTIE_MAX_CLAUDE * PRIX["opus"][1]) / 1e6
    envoi_sonnet = (ENTREE_GARDE * PRIX["sonnet"][0] + SORTIE_MAX_CLAUDE * PRIX["sonnet"][1]) / 1e6
    envoi_mistral = (ENTREE_GARDE * PRIX["mistral_repli"][0] + SORTIE_MAX_MISTRAL * PRIX["mistral_repli"][1]) / 1e6
    print(f"pire cas d'un seul envoi, qui sert à la garde avant l'envoi ({ENTREE_GARDE} jetons d'entrée comptés, sortie maximale pleine) : "
          f"opus {dollars(envoi_opus, 4)} ; sonnet {dollars(envoi_sonnet, 4)} ; mistral au prix de repli {dollars(envoi_mistral, 4)} "
          f"(sortie maximale supposée {SORTIE_MAX_MISTRAL})")
    q_opus_pess = cout_question("opus", False)
    rapide = cout_question("opus", False, prix=PRIX_OPUS_RAPIDE)
    cache = cout_question("opus", False, prix=(ECRITURE_CACHE_OPUS, PRIX["opus"][1]))
    q_tot = (ens_1 + ens_2 + ENSEMBLES_ESSAI) * K_MAX
    print(f"ce que le plafond ne couvre pas (remarque 6), par question d'Opus 5.5 au pire : mode rapide {dollars(rapide, 4)} "
          f"(x {dollars(rapide / q_opus_pess, 1)}) ; géographie « us » {dollars(q_opus_pess * FACTEUR_GEO_US, 4)} (x {dollars(FACTEUR_GEO_US, 1)}) ; "
          f"les deux {dollars(rapide * FACTEUR_GEO_US, 4)} (x {dollars(rapide * FACTEUR_GEO_US / q_opus_pess, 1)}) ; "
          f"entrée écrite au cache à {dollars(ECRITURE_CACHE_OPUS, 0)} dollars : {dollars(cache, 4)} (x {dollars(cache / q_opus_pess, 3)}), "
          f"soit {dollars((cache - q_opus_pess) * q_tot)} de plus sur la part de Claude à k = {K_MAX} ; "
          f"pire cas d'un envoi avec l'entrée à {dollars(ECRITURE_CACHE_OPUS, 0)} : "
          f"{dollars((ENTREE_GARDE * ECRITURE_CACHE_OPUS + SORTIE_MAX_CLAUDE * PRIX['opus'][1]) / 1e6, 4)}")

    print("\n== 4. Lectures du dommage, deux lecteurs, par valeur de k (dollars comptés, sans marge de change) ==")
    paires = (("opus", "mistral", "mistral_repli"), ("sonnet", "mistral", "mistral_repli"))
    for l1, l2, l2_repli in paires:
        att = cout_question(l1) + cout_question(l2)
        pess = cout_question(l1, False) + cout_question(l2_repli, False)
        pess_scelle = cout_question(l1, False) + cout_question(l2, False)
        print(f"paire {l1} + mistral : par question, attendu {dollars(att, 4)} ; pessimiste {dollars(pess, 4)} "
              f"(prix de Mistral scellé : {dollars(pess_scelle, 4)})")
        for k in VALEURS_K:
            q1, q2 = ens_1 * k, ens_2 * k
            groupe = (ens_1 + ens_2) * (cout_ensemble_groupe(l1, k) + cout_ensemble_groupe(l2, k))
            print(f"  k = {k} : attendu {dollars((q1 + q2) * att)} (étape 1 : {dollars(q1 * att)} ; étape 2 : {dollars(q2 * att)}) ; "
                  f"pessimiste {dollars((q1 + q2) * pess)} (étape 1 : {dollars(q1 * pess)} ; étape 2 : {dollars(q2 * pess)}) ; "
                  f"prix de Mistral scellé : {dollars((q1 + q2) * pess_scelle)} ; variante groupée, attendu {dollars(groupe)}")
    att = cout_question("opus") + cout_question("mistral")
    pess = cout_question("opus", False) + cout_question("mistral_repli", False)
    lect_centre = (ens_1 + ens_2) * K_CENTRE * att
    print(f"pour mémoire, plafonds des lectures du devis v1, sans marge de change, à k = {K_MAX} : "
          f"étape 1 = {math.ceil(ens_1 * K_MAX * pess)} ; étape 2 = {math.ceil(ens_2 * K_MAX * pess)}")

    print("\n== 5. Plafond de chaque file de lecture (remarque 2) et marge de change sur la part de Mistral (remarque 4) ==")
    print(f"marge de change : {100 * MARGE_CHANGE:.0f} % sur la part du compte Mistral (devise non relevée) ; la garde compte en dollars, "
          f"sans la marge ; l'engagement la porte")
    somme_opus = somme_mistral = somme_mistral_eng = 0.0
    plafonds_etape = {}
    for nom, ens in (("essai", ENSEMBLES_ESSAI), ("étape 1", ens_1), ("étape 2", ens_2)):
        c1, c2, e1, e2, plafond = files(ens, K_MAX)
        somme_opus += c1
        somme_mistral += c2
        somme_mistral_eng += e2
        plafonds_etape[nom] = plafond
        print(f"{nom:8s} : {ens * K_MAX} questions par lecteur (k = {K_MAX}) ; file d'Opus 5.5 = {dollars(c1)} ; "
              f"file de Mistral au prix de repli = {dollars(c2)} comptés, {dollars(e2)} à l'engagement ; "
              f"les deux files, à l'engagement = {dollars(e1 + e2)} ; plafond = {plafond}")
    plafond_essai, plafond_l1, plafond_l2 = plafonds_etape["essai"], plafonds_etape["étape 1"], plafonds_etape["étape 2"]
    print(f"par compte, essai compris (k = {K_MAX}) : Claude {dollars(somme_opus)}, plafond {math.ceil(somme_opus)} ; "
          f"Mistral {dollars(somme_mistral)} comptés, {dollars(somme_mistral_eng)} à l'engagement "
          f"(marge de change : {dollars(somme_mistral_eng - somme_mistral)}), plafond {math.ceil(somme_mistral_eng)} ; "
          f"ensemble {math.ceil(somme_opus) + math.ceil(somme_mistral_eng)} ; somme des plafonds des étapes {plafond_essai + plafond_l1 + plafond_l2}")
    print(f"somme des six files : {dollars(somme_opus + somme_mistral)} comptés ; {dollars(somme_opus + somme_mistral_eng)} à l'engagement")
    att_opus, att_mistral = cout_question("opus"), cout_question("mistral")
    q_centre = (ens_1 + ens_2 + ENSEMBLES_ESSAI) * K_CENTRE
    print(f"attendu par compte au centre, essai compris (k = {K_CENTRE}) : Claude {dollars(q_centre * att_opus)} ; Mistral {dollars(q_centre * att_mistral)}")
    prix_question_engagement = cout_question("opus", False) + cout_question("mistral_repli", False) * (1 + MARGE_CHANGE)
    print(f"prix pessimiste d'une question pour les deux lecteurs, marge de change comprise : {dollars(prix_question_engagement, 4)} ; "
          f"formule si k dépasse {K_MAX} : {ens_1 + ens_2} x k x {dollars(prix_question_engagement, 4)}")
    print(f"plafond de file recalculé après mesure, si la mesure vaut l'attendu, à k = {K_CENTRE} (deux fois le coût mesuré) : "
          f"étape 1, Opus {dollars(2 * ens_1 * K_CENTRE * att_opus)} et Mistral {dollars(2 * ens_1 * K_CENTRE * att_mistral)} comptés "
          f"({dollars(2 * ens_1 * K_CENTRE * att_mistral * (1 + MARGE_CHANGE))} à l'engagement), ensemble "
          f"{dollars(2 * ens_1 * K_CENTRE * (att_opus + att_mistral * (1 + MARGE_CHANGE)))} ; "
          f"étape 2, Opus {dollars(2 * ens_2 * K_CENTRE * att_opus)} et Mistral {dollars(2 * ens_2 * K_CENTRE * att_mistral)} comptés "
          f"({dollars(2 * ens_2 * K_CENTRE * att_mistral * (1 + MARGE_CHANGE))} à l'engagement), ensemble "
          f"{dollars(2 * ens_2 * K_CENTRE * (att_opus + att_mistral * (1 + MARGE_CHANGE)))}")
    print("lectures au pire, marge de change comprise, par valeur de k : " + " ; ".join(
        f"k = {k} : {dollars((ens_1 + ens_2) * k * prix_question_engagement)}" for k in VALEURS_K))
    scelle = (ens_1 + ens_2) * K_MAX * (cout_question("opus", False) + cout_question("mistral", False) * (1 + MARGE_CHANGE))
    repli = (ens_1 + ens_2) * K_MAX * prix_question_engagement
    print(f"si la page de prix de Mistral est scellée au prix relevé, lectures à k = {K_MAX}, marge de change comprise : "
          f"{dollars(repli)} devient {dollars(scelle)}")
    refus_opus = math.ceil(envoi_opus / (q_opus_pess / ENVOIS_PESS)) - 1
    refus_mistral = math.ceil(envoi_mistral / (cout_question('mistral_repli', False) / ENVOIS_PESS)) - 1
    print(f"effet de bord de la garde avant l'envoi : une file s'arrête dès que le cumul compté dépasse son plafond moins le pire cas "
          f"d'un envoi ; si chaque envoi coûtait exactement le prix pessimiste, derniers envois refusés : Opus {refus_opus} ; Mistral {refus_mistral}")

    print("\n== 6. Essai d'admission et de mesure ; ancre ==")
    essai_att = ENSEMBLES_ESSAI * K_CENTRE * att
    c1, c2, e1, e2, _ = files(ENSEMBLES_ESSAI, K_MAX)
    print(f"essai : {ENSEMBLES_ESSAI} ensembles par lecteur ; attendu à k = {K_CENTRE} : {dollars(essai_att)} ; "
          f"pessimiste à k = {K_MAX} : {dollars(c1 + c2)} comptés, {dollars(e1 + e2)} à l'engagement ; plafond {plafond_essai}")
    appels_ancre = ELEMENTS_ANCRE + ADMISSION_JUGE
    ancre_att = appels_ancre * cout_question("neon")
    ancre_pess = appels_ancre * cout_question("neon", False)
    print(f"ancre jugée par un agent (option du nœud), Gemini 4 Neon : {appels_ancre} appels ; attendu {dollars(ancre_att)} ; "
          f"pessimiste {dollars(ancre_pess)} comptés, {dollars(ancre_pess * (1 + MARGE_CHANGE))} avec la marge de change "
          f"(compte Google affiché en euros) ; plafond {math.ceil(ancre_pess * (1 + MARGE_CHANGE))}")

    print("\n== 7. Totaux ==")
    centre = carte_att_centre + lect_centre + essai_att
    print(f"attendu, centre (k = {K_CENTRE}, une question par appel, opus + mistral) : carte {dollars(carte_att_centre)} + "
          f"lectures {dollars(lect_centre)} + essai {dollars(essai_att)} = {dollars(centre)}")
    c1 = sum(lancement(ep_a + ep_c)[1:3]) / 2
    c2 = sum(lancement(ep_b)[1:3]) / 2
    print(f"attendu au centre, par étape : étape 1 = carte {dollars(c1)} + essai {dollars(essai_att)} + lectures "
          f"{dollars(ens_1 * K_CENTRE * att)} = {dollars(c1 + essai_att + ens_1 * K_CENTRE * att)} ; étape 2 = carte {dollars(c2)} + "
          f"lectures {dollars(ens_2 * K_CENTRE * att)} = {dollars(c2 + ens_2 * K_CENTRE * att)}")
    groupe_bas = cout_ensemble_groupe("sonnet", 3) + cout_ensemble_groupe("mistral", 3)
    bas = total_att_bas + (ENSEMBLES_ESSAI + ens_1 + ens_2) * groupe_bas
    haut = total_att_haut + (ENSEMBLES_ESSAI + ens_1 + ens_2) * K_MAX * att
    print(f"attendu, fourchette : bas (k = 3, lecture groupée, sonnet + mistral) {dollars(bas)} ; "
          f"haut (k = {K_MAX}, une question par appel, opus + mistral) {dollars(haut)}")
    plafond_total = carte_plafond + plafond_l1 + plafond_l2 + plafond_essai
    plafond_v1 = (carte_plafond + math.ceil(ens_1 * K_MAX * pess) + math.ceil(ens_2 * K_MAX * pess)
                  + math.ceil(ENSEMBLES_ESSAI * K_MAX * pess))
    print(f"plafond pessimiste (k <= {K_MAX}), marge de change sur la part de Mistral : carte {carte_plafond:.0f} + lectures {plafond_l1} + "
          f"{plafond_l2} + essai {plafond_essai} = {plafond_total:.0f} ; avec l'ancre jugée par un agent : "
          f"{plafond_total + math.ceil(ancre_pess * (1 + MARGE_CHANGE)):.0f} ; pour mémoire, plafond du devis v1, sans marge de change : {plafond_v1:.0f}")
    print(f"marge : plafond moins attendu au centre = {dollars(plafond_total - centre)} ; rapport {dollars(plafond_total / centre, 1)} ; "
          f"seuil d'alerte à 80 % du plafond = {dollars(0.8 * plafond_total)}")
    etape1 = lancement(ep_a + ep_c)[4] + plafond_essai + plafond_l1
    etape2 = lancement(ep_b)[4] + plafond_l2
    print(f"par étape : étape 1 (lancement 1, essai, lectures 1) = {etape1} ; étape 2 (lancement 2, lectures 2) = {etape2}")
    tout_claude = (carte_plafond + sum(files(e_, K_MAX, marge_l1=MARGE_CHANGE)[4] for e_ in (ENSEMBLES_ESSAI, ens_1, ens_2)))
    tout_euros = (sum(math.ceil(lancement(n_)[3] * (1 + MARGE_CHANGE)) for n_ in (ep_a + ep_c, ep_b))
                  + sum(files(e_, K_MAX, marge_l1=MARGE_CHANGE)[4] for e_ in (ENSEMBLES_ESSAI, ens_1, ens_2)))
    print(f"variantes de la marge de change : si le compte Claude désigné était aussi facturé en euros, part de Claude "
          f"{dollars(somme_opus * (1 + MARGE_CHANGE))} (soit {dollars(somme_opus * MARGE_CHANGE)} de plus), plafond total {tout_claude:.0f} ; "
          f"si toute la dépense l'était, carte comprise : {tout_euros:.0f}")
    g = [files(e_, K_MAX, groupe=True) for e_ in (ens_1, ens_2, ENSEMBLES_ESSAI)]
    groupe_pess = cout_ensemble_groupe("opus", K_MAX, False) + cout_ensemble_groupe("mistral_repli", K_MAX, False)
    groupe_eng = cout_ensemble_groupe("opus", K_MAX, False) + cout_ensemble_groupe("mistral_repli", K_MAX, False) * (1 + MARGE_CHANGE)
    print(f"si la lecture groupée est attestée (un appel par ensemble, k <= {K_MAX}) : par ensemble, pessimiste {dollars(groupe_pess, 4)} comptés, "
          f"{dollars(groupe_eng, 4)} à l'engagement ; lectures {g[0][4]} + {g[1][4]} ; essai {g[2][4]} ; "
          f"plafond total {carte_plafond + g[0][4] + g[1][4] + g[2][4]:.0f} ; files : étape 1, Opus {dollars(g[0][0])} et Mistral "
          f"{dollars(g[0][1])} comptés ({dollars(g[0][3])}) ; étape 2, Opus {dollars(g[1][0])} et Mistral {dollars(g[1][1])} comptés "
          f"({dollars(g[1][3])}) ; essai, Opus {dollars(g[2][0])} et Mistral {dollars(g[2][1])} comptés ({dollars(g[2][3])})")

    print("\n== 8. Variantes de taille : 100 et 200 épisodes par dose (remarque 12) ==")
    for n_x_e in (100, 200):
        ep, ens, c_bas, c_haut, c_plafond, l_att, l_plafond, total = variante(n_x_e)
        print(f"n x e = {n_x_e} : épisodes {ep} ; ensembles lus par lecteur {ens} ; carte attendu {dollars(c_bas)} à {dollars(c_haut)}, "
              f"plafond {c_plafond} ; lectures attendu à k = {K_CENTRE} : {dollars(l_att)}, plafond à k = {K_MAX} : {l_plafond} ; "
              f"plafond total avec l'essai : {total}")

    print("\n== 9. Chiffres dérivés cités au devis ==")
    print(f"lectures : plafond sur attendu au centre = {dollars((plafond_l1 + plafond_l2) / lect_centre, 1)} ; "
          f"économie de Sonnet 5.5 au centre = {dollars(lect_centre - (ens_1 + ens_2) * K_CENTRE * (cout_question('sonnet') + cout_question('mistral')))}")
    part_controles = lect_centre * (ep_a // 2 + ep_c + RELECTURES_EPREUVES) / (ens_1 + ens_2) + (ep_a // 2 + ep_c) * D_HAUT * PRIX_DEVIS / 3600
    print(f"part des conditions de contrôle dans l'attendu au centre = {dollars(part_controles)}")
    print(f"reprises des lectures : dans l'attendu au centre = {dollars((lect_centre + essai_att) * (ENVOIS_ATT - 1) / ENVOIS_ATT)} ; "
          f"dans le plafond = {dollars((plafond_l1 + plafond_l2 + plafond_essai) * (ENVOIS_PESS - 1) / ENVOIS_PESS)} ; "
          f"reprises de la carte dans le plafond = {dollars(carte_plafond - total_att_haut)}")
    print(f"plafond à une fois et demie l'attendu au centre = {dollars(1.5 * centre)}")
    actions = (ep_a + ep_b + ep_c) * A_PAS
    print(f"juge d'une autre lignée, pour mémoire, au prorata de {actions} actions sur 6 400 : "
          f"{dollars(6.4 * actions / 6400, 1)} à {dollars(18.1 * actions / 6400, 1)} ; pire {dollars(34 * actions / 6400, 1)}")
    provision = N_TACHES * K_MAX * (1500 * PRIX['opus'][0] + 400 * PRIX['opus'][1]) * ENVOIS_PESS / 1e6
    print(f"provision indicative, préparation de la référence ({N_TACHES * K_MAX} appels courts d'Opus 5.5, 1 500 jetons d'entrée et 400 de sortie, S) : {dollars(provision)}")
    print(f"marges par ligne (plafond moins attendu au centre) : carte {dollars(carte_plafond - carte_att_centre)} ; "
          f"lectures {dollars(plafond_l1 + plafond_l2 - lect_centre)} ; essai {dollars(plafond_essai - essai_att)}")
    print(f"essai, fourchette attendue : {dollars(ENSEMBLES_ESSAI * (cout_ensemble_groupe('sonnet', 3) + cout_ensemble_groupe('mistral', 3)))} "
          f"à {dollars(ENSEMBLES_ESSAI * K_MAX * att)}")
    entree_essai = 2 * (18 * 950 + 6 * 3650)     # M : deux réglages d'Opus 5.5, entrées supposées du devis de l'essai (ligne 144)
    sortie_moy = (0.602 - entree_essai * PRIX["opus"][0] / 1e6) / (PRIX["opus"][1] / 1e6) / 48   # M : registres/depenses.md:546
    print(f"sortie moyenne d'Opus 5.5 à l'essai du bras A, sur entrées supposées : {sortie_moy:.0f} jetons par lecture")
    print(f"point d'accès global de Mistral : {dollars(100 * (1 - 1 / 1.1), 1)} % de moins sur la part de Mistral")
    mistral_pess = cout_question("mistral_repli", False)
    print(f"prix arrondis d'une lecture, retenus au point 1 : Opus 5.5 {dollars(cout_question('opus'), 3)} et {dollars(q_opus_pess, 3)} ; "
          f"Mistral {dollars(cout_question('mistral'), 3)} et {dollars(mistral_pess, 3)}, soit {dollars(mistral_pess * (1 + MARGE_CHANGE), 4)} "
          f"avec la marge de change ({dollars(mistral_pess * (1 + MARGE_CHANGE), 3)})")

    print("\n== 10. Effort du lecteur Claude (remarque 7) : Opus 5.5, une question par appel ==")
    q_k8 = (ens_1 + ens_2 + ENSEMBLES_ESSAI) * K_MAX
    for nom, sortie in SORTIE_EFFORT:
        c = cout_question("opus", True, sortie=sortie)
        print(f"effort {nom:5s} : sortie supposée {sortie} jetons ; {dollars(c, 4)} par question ; part de Claude attendue, essai compris : "
              f"{dollars(q_centre * c)} à k = {K_CENTRE}, {dollars(q_k8 * c)} à k = {K_MAX} ; "
              f"surcoût sur l'effort bas au centre, lectures seules : {dollars((c - att_opus) * (ens_1 + ens_2) * K_CENTRE)}")
    c_max_att = cout_question("opus", True, sortie=SORTIE_MAX_CLAUDE)
    c_max_pess = cout_question("opus", False, sortie=SORTIE_MAX_CLAUDE)
    print(f"borne, si chaque réponse atteignait la sortie maximale du corps ({SORTIE_MAX_CLAUDE} jetons) : {dollars(c_max_att, 4)} par question "
          f"aux entrées attendues, {dollars(c_max_pess, 4)} au pire ; part de Claude, essai compris : {dollars(q_centre * c_max_att)} à k = {K_CENTRE} ; "
          f"à k = {K_MAX}, {dollars(q_k8 * c_max_att)} à {dollars(q_k8 * c_max_pess)} ; plafond de la part de Claude : {math.ceil(somme_opus)} ; "
          f"rapport de ce plafond à la part attendue à l'effort haut, à k = {K_MAX} : "
          f"{dollars(somme_opus / (q_k8 * cout_question('opus', True, sortie=2000)), 2)}")
    couvre_att = (q_opus_pess / ENVOIS_ATT * 1e6 - ENTREE_ATT * PRIX["opus"][0]) / PRIX["opus"][1]
    print(f"sortie moyenne par question que le plafond de la file d'Opus couvre : {SORTIE_PESS['opus']} jetons si les entrées et les reprises "
          f"sont au pire ; {couvre_att:.0f} jetons si elles sont à l'attendu")
    file_essai_opus, _, _, file_essai_mistral_eng, _ = files(ENSEMBLES_ESSAI, K_MAX)
    plafond_essai_2 = math.ceil(2 * file_essai_opus + file_essai_mistral_eng)
    q_essai_centre = ENSEMBLES_ESSAI * K_CENTRE
    print(f"option : l'essai mesure deux réglages du lecteur Claude (une seconde file d'Opus 5.5 de même plafond, {dollars(file_essai_opus)}) : "
          f"plafond de l'essai {plafond_essai_2} au lieu de {plafond_essai} ; plafond total {plafond_total + plafond_essai_2 - plafond_essai:.0f} ; "
          f"attendu de l'essai à k = {K_CENTRE} : {dollars(essai_att + q_essai_centre * cout_question('opus', True, sortie=1000))} (bas et moyen), "
          f"{dollars(essai_att + q_essai_centre * cout_question('opus', True, sortie=2000))} (bas et haut)")

    print("\n== 11. Repli si le lecteur Claude est écarté (remarque 1) : Gemini 4 Neon et Mistral Large 4 ==")
    att_n = cout_question("neon") + cout_question("mistral")
    r = {nom: files(ens, K_MAX, l1="neon", marge_l1=MARGE_CHANGE) for nom, ens in
         (("essai", ENSEMBLES_ESSAI), ("étape 1", ens_1), ("étape 2", ens_2))}
    print(f"par question : attendu {dollars(att_n, 4)} ; pessimiste {dollars(cout_question('neon', False) + cout_question('mistral_repli', False), 4)} "
          f"comptés ; marge de change sur les deux comptes (Google affiché en euros, Mistral non relevé)")
    print(f"attendu au centre (k = {K_CENTRE}) : carte {dollars(carte_att_centre)} + lectures {dollars((ens_1 + ens_2) * K_CENTRE * att_n)} + "
          f"essai {dollars(ENSEMBLES_ESSAI * K_CENTRE * att_n)} = "
          f"{dollars(carte_att_centre + (ens_1 + ens_2 + ENSEMBLES_ESSAI) * K_CENTRE * att_n)}")
    print(f"plafond pessimiste (k <= {K_MAX}) : carte {carte_plafond:.0f} + lectures {r['étape 1'][4]} + {r['étape 2'][4]} + essai {r['essai'][4]} = "
          f"{carte_plafond + r['étape 1'][4] + r['étape 2'][4] + r['essai'][4]:.0f} ; files de Neon, comptées : étape 1 {dollars(r['étape 1'][0])}, "
          f"étape 2 {dollars(r['étape 2'][0])}, essai {dollars(r['essai'][0])}")

    print("\n== 12. Constantes supposées, rappelées (remarque 8) ==")
    print(f"lecture groupée : {GROUPE_ENTREE_PAR_QUESTION} jetons d'entrée et {GROUPE_SORTIE_PAR_QUESTION} de sortie par question ; réflexion par appel : "
          f"{GROUPE_REFLEXION['opus']} (Claude), {GROUPE_REFLEXION['mistral']} (Mistral) ; au pire : entrée x {dollars(ENTREE_PESS / ENTREE_ATT, 1)}, "
          f"sortie x {dollars(SORTIE_PESS['opus'] / SORTIE_ATT['opus'], 0)} (Claude) et x {dollars(SORTIE_PESS['mistral'] / SORTIE_ATT['mistral'], 0)} (Mistral), "
          f"envois x {dollars(ENVOIS_PESS)}")
    print(f"à k = {K_MAX}, un appel groupé : entrée {ENTREE_ATT + GROUPE_ENTREE_PAR_QUESTION * K_MAX} jetons attendus, "
          f"{int((ENTREE_ATT + GROUPE_ENTREE_PAR_QUESTION * K_MAX) * ENTREE_PESS / ENTREE_ATT)} au pire ; sortie de Claude "
          f"{GROUPE_REFLEXION['opus'] + GROUPE_SORTIE_PAR_QUESTION * K_MAX} attendus, "
          f"{int((GROUPE_REFLEXION['opus'] + GROUPE_SORTIE_PAR_QUESTION * K_MAX) * SORTIE_PESS['opus'] / SORTIE_ATT['opus'])} au pire ; sortie de Mistral "
          f"{GROUPE_REFLEXION['mistral'] + GROUPE_SORTIE_PAR_QUESTION * K_MAX} attendus, "
          f"{int((GROUPE_REFLEXION['mistral'] + GROUPE_SORTIE_PAR_QUESTION * K_MAX) * SORTIE_PESS['mistral'] / SORTIE_ATT['mistral'])} au pire")
    print(f"sorties de Gemini 4 Neon, réflexion comprise : {SORTIE_ATT['neon']} jetons attendus, {SORTIE_PESS['neon']} au pire")


if __name__ == "__main__":
    main()
