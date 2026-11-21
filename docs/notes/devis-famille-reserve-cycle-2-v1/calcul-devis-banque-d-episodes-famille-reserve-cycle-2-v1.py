#!/usr/bin/env python3
"""Recalcul des chiffres du devis de la banque d'épisodes de la famille aveugle de réserve du cycle 2 (v1).

Bibliothèque standard seule ; aucun réseau, aucun fichier lu, aucun hasard. Chaque constante porte sa source, telle que le
devis la cite (chemin:ligne). Lancer : python3 calcul-devis-banque-d-episodes-famille-reserve-cycle-2-v1.py
Trois lettres, comme au devis : M = relevé sur une pièce ; C = calculé ici ; S = supposé, sans mesure.
"""
import math

# ---------- tailles de principe (pièce 6 de la famille, section 3) ----------
N_TACHES = 60        # M : pièce 6, section 3 (fichier des tâches du pilote)
E = 1                # M : pièce 6, section 3
N_F = 20             # M : pièce 6, section 3
A_PAS = 10           # S : réglage de la chaîne réemployée (devis du bras A v2, ligne 38) ; propositions.py:26 borne à 10
RELECTURES_EPREUVES = 60   # M : pièce 6, section 2, poste D (« de l'ordre de 3 x 20 ensembles »)
VALEURS_K = (3, 4, 6, 8)   # S : k est au coffre ; table ; le plafond se calcule à K_MAX
K_MAX = 8
K_CENTRE = 6

# ---------- carte louée ----------
D_HAUT, D_BAS = 42.8, 40.2      # M : secondes par épisode, devis du bras A v2, lignes 42-43 et 54 (autre chaîne : S pour ce banc)
MISE_EN_ROUTE_H = 1.0           # S : devis du bras A v2, ligne 56
PRIX_RELEVE = 1.1833            # M : registres/depenses.md:515 (2026-11-18T15:44:24Z)
PRIX_CARTE, STOCKAGE = 1.30, 0.08   # M : devis du bras A v2, lignes 67 et 69 (bornes)
PRIX_DEVIS = PRIX_CARTE + STOCKAGE  # C : 1,38
TEL_BAS, TEL_HAUT = 1.0, 2.0    # M : devis du bras A v2, ligne 69 (20 à 40 Go à 0,05 dollar par Go)
FACTEUR_PESSIMISTE = 4.0        # M (méthode) : devis du bras A v2, ligne 81 (débit deux fois plus lent, une relance complète)
TEL_PESSIMISTE = 4.0            # M (méthode) : même ligne (deux mises en route à 2 dollars)

# ---------- lecteurs : prix en dollars par million de jetons (entrée, sortie) ----------
PRIX = {
    "opus": (4.0, 20.0),            # M : page scellée d'Anthropic 78aff5c8… ; relais_reel.py:50 ; collisionneur_v9_v3.py:131
    "sonnet": (2.0, 10.0),          # M : même page ; relais_reel.py:51
    "mistral": (0.77, 2.31),        # C sur relevé non scellé : 0,70 et 2,10 x 1,1 (point d'accès européen), choix-mistral-deepseek-v1.md:19
    "mistral_repli": (1.54, 4.62),  # C : le double, tant que la page de prix de Mistral n'est pas versée et scellée
    "neon": (3.0, 15.0),            # M : page scellée de Google 89c58281…, section « Gemini 4 Neon » ; registres/go.md:589
}
ENTREE_ATT, ENTREE_PESS = 4000, 6000    # S : ordre de 4 000 jetons par plan (esquisse en clair du premier cycle, ligne 43)
SORTIE_ATT = {"opus": 500, "sonnet": 500, "mistral": 3000, "mistral_repli": 3000, "neon": 1500}     # S
SORTIE_PESS = {"opus": 2000, "sonnet": 2000, "mistral": 9000, "mistral_repli": 9000, "neon": 6000}   # S
ENVOIS_ATT, ENVOIS_PESS = 1.05, 1.15    # S : reprises et redemandes de forme, 5 % attendus, 15 % au plafond
ENTREE_GARDE, SORTIE_MAX_CLAUDE, SORTIE_MAX_MISTRAL = 24000, 8192, 16384   # M / M / S : garde par envoi (un jeton par octet)

# ---------- essai d'admission et de mesure ; ancre ----------
ENSEMBLES_ESSAI = 12      # S : 8 ensembles honnêtes et 4 de dose flagrante par lecteur
ELEMENTS_ANCRE = 30       # M : pièce 6, section 2 (ancre humaine sur 30 éléments)
ADMISSION_JUGE = 8        # M : précédent du bras A, registres/go.md:632 (huit lectures d'admission)


def dollars(x, n=2):
    return f"{x:.{n}f}".replace(".", ",")


def cout_question(modele, attendu=True):
    pe, ps = PRIX[modele]
    if attendu:
        return (ENTREE_ATT * pe + SORTIE_ATT[modele] * ps) * ENVOIS_ATT / 1e6
    return (ENTREE_PESS * pe + SORTIE_PESS[modele] * ps) * ENVOIS_PESS / 1e6


def cout_ensemble_groupe(modele, k, attendu=True):
    """Variante « un appel par ensemble, k questions dedans » (S). Pessimiste : entrée x 1,5, sortie multipliée comme
    pour une question (SORTIE_PESS / SORTIE_ATT), envois x 1,15."""
    pe, ps = PRIX[modele]
    reflexion = {"opus": 300, "sonnet": 300, "mistral": 3000, "mistral_repli": 3000, "neon": 1500}[modele]
    entree, sortie = ENTREE_ATT + 150 * k, reflexion + 150 * k
    if attendu:
        return (entree * pe + sortie * ps) * ENVOIS_ATT / 1e6
    facteur_entree = ENTREE_PESS / ENTREE_ATT
    facteur_sortie = SORTIE_PESS[modele] / SORTIE_ATT[modele]
    return (entree * facteur_entree * pe + sortie * facteur_sortie * ps) * ENVOIS_PESS / 1e6


def lancement(nb_episodes):
    h = nb_episodes * D_HAUT / 3600 + MISE_EN_ROUTE_H
    h_bas = nb_episodes * D_BAS / 3600 + MISE_EN_ROUTE_H
    att_bas = h_bas * PRIX_RELEVE + TEL_BAS
    att_haut = h * PRIX_DEVIS + TEL_HAUT
    pire = h * FACTEUR_PESSIMISTE * PRIX_DEVIS + TEL_PESSIMISTE
    return h, att_bas, att_haut, pire, math.ceil(pire)


def volumes(n_taches, e, n_f):
    ep_a, ep_b, ep_c = 2 * n_taches * e, 2 * n_taches * e, n_f * e
    ens_1 = ep_a + ep_c + RELECTURES_EPREUVES      # étape 1 : honnêtes, dose flagrante, relectures des épreuves
    ens_2 = ep_b                                   # étape 2 : « sabotage demandé »
    return ep_a, ep_b, ep_c, ens_1, ens_2


def main():
    ep_a, ep_b, ep_c, ens_1, ens_2 = volumes(N_TACHES, E, N_F)
    print("== 1. Volumes (tailles de principe de la pièce 6) ==")
    print(f"épisodes honnêtes A = {ep_a} ; « sabotage demandé » B = {ep_b} ; dose flagrante C = {ep_c} ; total = {ep_a + ep_b + ep_c}")
    print(f"actions = {(ep_a + ep_b + ep_c) * A_PAS} (a = {A_PAS})")
    print(f"ensembles lus par lecteur : étape 1 = {ens_1} ; étape 2 = {ens_2} ; total = {ens_1 + ens_2}")
    for k in VALEURS_K:
        print(f"  k = {k} : questions par lecteur = {(ens_1 + ens_2) * k} (étape 1 : {ens_1 * k} ; étape 2 : {ens_2 * k})")
    mesure, controle = ep_a // 2 + ep_b, ep_a // 2 + ep_c
    print(f"part des contrôles : {controle} épisodes sur {mesure + controle} ({100 * controle / (mesure + controle):.0f} %) ; "
          f"{controle + RELECTURES_EPREUVES} ensembles lus sur {ens_1 + ens_2} ({100 * (controle + RELECTURES_EPREUVES) / (ens_1 + ens_2):.0f} %)")

    print("\n== 2. Carte : prix d'une action et lancements ==")
    print(f"prix d'une action p_a = {dollars(D_HAUT / A_PAS * PRIX_RELEVE / 3600, 5)} à {dollars(D_HAUT / A_PAS * PRIX_DEVIS / 3600, 5)} dollar "
          f"({dollars(D_HAUT / A_PAS, 2)} s par action) ; par épisode : {dollars(D_HAUT * PRIX_RELEVE / 3600, 4)} à {dollars(D_HAUT * PRIX_DEVIS / 3600, 4)}")
    print(f"coût fixe d'un lancement : {dollars(MISE_EN_ROUTE_H * PRIX_RELEVE + TEL_BAS)} à {dollars(MISE_EN_ROUTE_H * PRIX_DEVIS + TEL_HAUT)} dollars")
    total_att_bas = total_att_haut = total_plafond = 0.0
    for nom, nb in (("lancement 1 (A et C)", ep_a + ep_c), ("lancement 2 (B)", ep_b)):
        h, att_bas, att_haut, pire, plafond = lancement(nb)
        total_att_bas += att_bas
        total_att_haut += att_haut
        total_plafond += plafond
        print(f"{nom} : {nb} épisodes ; {dollars(h)} h ; attendu {dollars(att_bas)} à {dollars(att_haut)} ; "
              f"pire cas {dollars(pire)} ; plafond {plafond} ; durée au pire {dollars(h * FACTEUR_PESSIMISTE)} h")
    h_tot = round(lancement(ep_a + ep_c)[0], 2) + round(lancement(ep_b)[0], 2)
    pire_tot = round(lancement(ep_a + ep_c)[3], 2) + round(lancement(ep_b)[3], 2)
    print(f"carte, total : attendu {dollars(total_att_bas)} à {dollars(total_att_haut)} ; plafond {total_plafond:.0f} ; "
          f"durée attendue {dollars(h_tot)} h ; pire cas {dollars(pire_tot)} ; prix arrondis d'une lecture au point 1 : "
          f"{dollars(cout_question('opus'), 3)} et {dollars(cout_question('opus', False), 3)} ; "
          f"{dollars(cout_question('mistral'), 3)} et {dollars(cout_question('mistral_repli', False), 3)}")
    h, att_bas, att_haut, pire, plafond = lancement(ep_a + ep_b + ep_c)
    print(f"variante, un seul lancement (A, B et C) : {dollars(h)} h ; attendu {dollars(att_bas)} à {dollars(att_haut)} ; pire cas {dollars(pire)} ; plafond {plafond}")
    carte_att_centre = (total_att_bas + total_att_haut) / 2
    carte_plafond = total_plafond

    print("\n== 3. Lecteurs : prix d'une lecture (une question, le plan renvoyé à chaque appel) ==")
    for m in ("opus", "sonnet", "mistral", "mistral_repli", "neon"):
        print(f"{m:14s} attendu {dollars(cout_question(m), 4)} ; pessimiste {dollars(cout_question(m, False), 4)}")
    print(f"garde par envoi (pire cas d'un seul envoi) : opus {dollars((ENTREE_GARDE * 4 + SORTIE_MAX_CLAUDE * 20) / 1e6, 3)} ; "
          f"sonnet {dollars((ENTREE_GARDE * 2 + SORTIE_MAX_CLAUDE * 10) / 1e6, 3)} ; "
          f"mistral au prix de repli {dollars((ENTREE_GARDE * 1.54 + SORTIE_MAX_MISTRAL * 4.62) / 1e6, 3)}")

    print("\n== 4. Lectures du dommage, deux lecteurs, par valeur de k ==")
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
    plafond_l1 = math.ceil(ens_1 * K_MAX * pess)
    plafond_l2 = math.ceil(ens_2 * K_MAX * pess)
    lect_centre = (ens_1 + ens_2) * K_CENTRE * att
    print(f"plafonds des lectures à k = {K_MAX} (opus + mistral au prix de repli) : étape 1 = {plafond_l1} ; étape 2 = {plafond_l2}")
    print(f"plafond recalculé après mesure, si la mesure vaut l'attendu, à k = {K_CENTRE} : "
          f"étape 1 = {dollars(2 * ens_1 * K_CENTRE * att)} ; étape 2 = {dollars(2 * ens_2 * K_CENTRE * att)}")

    print("\n== 5. Essai d'admission et de mesure ; ancre ==")
    essai_att = ENSEMBLES_ESSAI * K_CENTRE * att
    essai_pess = ENSEMBLES_ESSAI * K_MAX * pess
    plafond_essai = math.ceil(essai_pess)
    print(f"essai : {ENSEMBLES_ESSAI} ensembles par lecteur ; attendu à k = {K_CENTRE} : {dollars(essai_att)} ; "
          f"pessimiste à k = {K_MAX} : {dollars(essai_pess)} ; plafond {plafond_essai}")
    appels_ancre = ELEMENTS_ANCRE + ADMISSION_JUGE
    ancre_att = appels_ancre * cout_question("neon")
    ancre_pess = appels_ancre * cout_question("neon", False)
    print(f"ancre jugée par un agent (option du nœud), Gemini 4 Neon : {appels_ancre} appels ; attendu {dollars(ancre_att)} ; "
          f"pessimiste {dollars(ancre_pess)} ; plafond {math.ceil(ancre_pess)}")

    print("\n== 6. Totaux ==")
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
    print(f"plafond pessimiste (k <= {K_MAX}) : carte {carte_plafond:.0f} + lectures {plafond_l1} + {plafond_l2} + essai {plafond_essai} "
          f"= {plafond_total:.0f} ; avec l'ancre jugée par un agent : {plafond_total + math.ceil(ancre_pess):.0f}")
    print(f"marge : plafond moins attendu au centre = {dollars(plafond_total - centre)} ; rapport {dollars(plafond_total / centre, 1)} ; "
          f"seuil d'alerte à 80 % du plafond = {dollars(0.8 * plafond_total)}")
    etape1 = lancement(ep_a + ep_c)[4] + plafond_essai + plafond_l1
    etape2 = lancement(ep_b)[4] + plafond_l2
    print(f"par étape : étape 1 (lancement 1, essai, lectures 1) = {etape1} ; étape 2 (lancement 2, lectures 2) = {etape2}")
    groupe_pess = cout_ensemble_groupe("opus", K_MAX, False) + cout_ensemble_groupe("mistral_repli", K_MAX, False)
    g1, g2, ge = math.ceil(ens_1 * groupe_pess), math.ceil(ens_2 * groupe_pess), math.ceil(ENSEMBLES_ESSAI * groupe_pess)
    print(f"si la lecture groupée est attestée (un appel par ensemble, k <= {K_MAX}) : par ensemble, pessimiste {dollars(groupe_pess, 4)} ; "
          f"lectures {g1} + {g2} ; essai {ge} ; plafond total {carte_plafond + g1 + g2 + ge:.0f}")
    d = D_HAUT
    print(f"plafond du lancement 2 recalculé sur le débit mesuré d (secondes par épisode) : "
          f"2 x {dollars(PRIX_DEVIS)} x (1,0 + 120 x 1,5 x d / 3600) + 4 ; pour d = {dollars(d, 1)} : "
          f"{dollars(2 * PRIX_DEVIS * (1.0 + 120 * 1.5 * d / 3600) + 4)}")

    print("\n== 7. Variante : 100 épisodes par dose (n x e = 100) ==")
    ep_a, ep_b, ep_c, ens_1, ens_2 = volumes(100, 1, N_F)
    carte = lancement(ep_a + ep_c)
    carte2 = lancement(ep_b)
    lect_att = (ens_1 + ens_2) * K_CENTRE * att
    lect_pess = math.ceil(ens_1 * K_MAX * pess) + math.ceil(ens_2 * K_MAX * pess)
    print(f"épisodes {ep_a + ep_b + ep_c} ; ensembles lus par lecteur {ens_1 + ens_2} ; carte attendu "
          f"{dollars(carte[1] + carte2[1])} à {dollars(carte[2] + carte2[2])}, plafond {carte[4] + carte2[4]} ; "
          f"lectures attendu à k = {K_CENTRE} : {dollars(lect_att)}, plafond à k = {K_MAX} : {lect_pess} ; "
          f"plafond total avec l'essai : {carte[4] + carte2[4] + lect_pess + plafond_essai}")

    print("\n== 8. Chiffres dérivés cités au devis ==")
    ep_a, ep_b, ep_c, ens_1, ens_2 = volumes(N_TACHES, E, N_F)
    q_plafond = (ens_1 + ens_2 + ENSEMBLES_ESSAI) * K_MAX
    claude = q_plafond * cout_question("opus", False)
    mistral = q_plafond * cout_question("mistral_repli", False)
    print(f"plafond par compte, essai compris (k = {K_MAX}) : Claude {math.ceil(claude)} ; Mistral {math.ceil(mistral)} ; "
          f"ensemble {plafond_l1 + plafond_l2 + plafond_essai}")
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
    moyen = (ENTREE_ATT * PRIX["opus"][0] + 2 * SORTIE_ATT["opus"] * PRIX["opus"][1]) * ENVOIS_ATT / 1e6
    print(f"Opus 5.5 à l'effort moyen (sortie supposée double, S) : {dollars(moyen, 4)} par question ; "
          f"surcoût attendu au centre = {dollars((moyen - cout_question('opus')) * (ens_1 + ens_2) * K_CENTRE)}")
    entree_essai = 2 * (18 * 950 + 6 * 3650)     # M : deux réglages d'Opus 5.5, entrées supposées du devis de l'essai (ligne 144)
    sortie_moy = (0.602 - entree_essai * PRIX["opus"][0] / 1e6) / (PRIX["opus"][1] / 1e6) / 48   # M : registres/depenses.md:546
    print(f"sortie moyenne d'Opus 5.5 à l'essai du bras A, sur entrées supposées : {sortie_moy:.0f} jetons par lecture")
    print(f"point d'accès global de Mistral : {dollars(100 * (1 - 1 / 1.1), 1)} % de moins sur la part de Mistral")
    print(f"minuteries d'arrêt dur (heures cumulées au pire) : lancement 1 = {dollars(lancement(ep_a + ep_c)[0] * FACTEUR_PESSIMISTE)} ; "
          f"lancement 2 = {dollars(lancement(ep_b)[0] * FACTEUR_PESSIMISTE)}")


if __name__ == "__main__":
    main()
