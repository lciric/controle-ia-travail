#!/usr/bin/env python3
"""Recalcul des chiffres du devis de la banque d'épisodes de la famille aveugle de réserve du cycle 2 (v3).

Remplace le programme v2, resté à côté et intact, après la vérification des corrections du devis v2 et le rapprochement
du devis avec la pièce 6 de la famille en version 2 (62b99079…). Bibliothèque standard seule ; aucun réseau, aucun
fichier lu, aucun hasard. Chaque constante porte sa source, telle que le devis la cite (chemin:ligne).
Lancer : python3 calcul-devis-banque-d-episodes-famille-reserve-cycle-2-v3.py
Trois lettres, comme au devis : M = relevé sur une pièce ; C = calculé ici ; S = supposé, sans mesure.

Ce qui change par rapport au programme v2 :
- rapprochement avec la pièce 6 version 2 : relectures des épreuves, 60 -> 200 ensembles (poste D2) ; poste neuf des
  oracles rapportés à côté, 240 ensembles x k' (poste D3) ; ancre jugée par un agent, 30 questions (poste D4) ;
  sections 1, 4, 5, 8 et 14 ;
- point A de la vérification : règle de lancement d'une file après mesure, changée (voie 2), section 6 ;
- point B de la vérification : prix à retenir arrondis au-dessus, section 3 ;
- point C de la vérification : le repli chiffré « Neon et Mistral » (548) est retiré ; un second lecteur de rechange
  n'a que des ordres de grandeur, sans plafond (section 12) ; l'ancre par Neon est chiffrée selon la règle des appels
  aux modèles de Google (section 7) ;
- l'essai mesure aussi la forme de question du poste D3 (section 7) ;
- la garde compte la file de Mistral au prix de repli tant que sa page de prix n'est pas scellée : les exemples de la
  règle après mesure le suivent (section 6 ; le programme v2 les donnait au prix relevé).
Les sections 2 et 3 rendent, pour la carte et pour le prix d'une question, les mêmes chiffres que le programme v2.
"""
import math

# ---------- tailles de principe (pièce 6 de la famille, version 2, section 3) ----------
N_TACHES = 60        # M : pièce 6 v2, section 3 (fichier des tâches du pilote)
E = 1                # M : pièce 6 v2, section 3
N_F = 20             # M : pièce 6 v2, section 3
A_PAS = 10           # S : réglage de la chaîne réemployée (devis du bras A v2, ligne 38) ; propositions.py:26 borne à 10
RELECTURES_EPREUVES = 200      # M : pièce 6 v2, section 2, poste D2 (« au moins 200 ensembles » : 5 x 20 manipulés, autant d'intacts)
RELECTURES_EPREUVES_V1 = 60    # M : pièce 6 v1, section 2, poste D (« de l'ordre de 3 x 20 ensembles »), pour mémoire
VALEURS_K = (3, 4, 6, 8)       # S : k, nombre moyen d'éléments lus par tâche, est au coffre ; le plafond se calcule à K_MAX
K_MAX, K_CENTRE = 8, 6
KP_MAX, KP_CENTRE = 8, 6       # S : k', nombre moyen d'éléments des oracles rapportés à côté (poste D3), est au coffre ;
                               #     pris égal à k faute de toute indication

# ---------- carte louée (inchangé depuis le programme v2) ----------
D_HAUT, D_BAS = 42.8, 40.2      # M : secondes par épisode, devis du bras A v2, ligne 54 (autre chaîne : S pour ce banc)
MISE_EN_ROUTE_H = 1.0           # S : devis du bras A v2, ligne 56
PRIX_RELEVE_CARTE = 1.1833      # M : registres/depenses.md:515, carte seule (2026-11-18T15:44:24Z)
PRIX_RELEVE_OFFRE = 1.1843      # M : même ligne, offre, stockage compris ; retenu pour l'attendu bas
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
    "neon": (3.0, 15.0),            # M : pages de prix de Google 89c58281… (scellée) et 40202cdd… (versée le 21 novembre),
                                    #     section « Gemini 4 Neon », onglet « Standard », sortie « including thinking tokens »
}
ENTREE_ATT, ENTREE_PESS = 4000, 6000    # S : ordre de 4 000 jetons par plan (esquisse en clair du premier cycle, ligne 43)
SORTIE_ATT = {"opus": 500, "sonnet": 500, "mistral": 3000, "mistral_repli": 3000}     # S
SORTIE_PESS = {"opus": 2000, "sonnet": 2000, "mistral": 9000, "mistral_repli": 9000}   # S
ENVOIS_ATT, ENVOIS_PESS = 1.05, 1.15    # S : reprises et redemandes de forme, 5 % attendus, 15 % au plafond
ENTREE_GARDE, SORTIE_MAX_CLAUDE, SORTIE_MAX_MISTRAL = 24000, 8192, 16384   # M / M / S : garde par envoi (un jeton par octet)

# ---------- lecture groupée : un appel par ensemble, les questions dedans (S) ----------
GROUPE_ENTREE_PAR_QUESTION = 150    # S : jetons d'entrée ajoutés par question (un élément de référence de plus)
GROUPE_SORTIE_PAR_QUESTION = 150    # S : jetons de sortie par question (verdict et extrait cité)
GROUPE_REFLEXION = {"opus": 300, "sonnet": 300, "mistral": 3000, "mistral_repli": 3000}   # S : par appel

# ---------- marge de change ----------
MARGE_CHANGE = 0.05   # M : 5 % acceptés par Lazar pour le bras A (registres/go.md:667) ; sur la part de Mistral, dont le
                      #     crédit est relevé en euros (registres/go.md:674), et sur le compte Google de l'ancre (euros)

# ---------- ce que le plafond ne couvre pas, page scellée d'Anthropic 78aff5c8… ----------
PRIX_OPUS_RAPIDE = (8.0, 40.0)   # M : « Fast mode pricing », Claude Opus 5.5
FACTEUR_GEO_US = 1.1             # M : « Data residency pricing », inference_geo « us »
ECRITURE_CACHE_OPUS = 5.0        # M : tableau des modèles, « 5m writes » ; relais_reel.py:50

# ---------- effort du lecteur Claude ----------
SORTIE_EFFORT = (("bas", 500), ("moyen", 1000), ("haut", 2000))   # S : bas et moyen d'après devis-essai…:144 ; haut sans source

# ---------- règle de lancement d'une file après mesure (point A de la vérification, voie 2) ----------
MARGE_LANCEMENT = 0.5            # S : la file part si le coût projeté, majoré de moitié, tient dans son plafond pessimiste
FACTEUR_PLAFOND_MESURE = 2.0     # M (méthode) : devis v2, deux fois le coût mesuré
FACTEUR_REGLE_V2 = 2.0           # pour mémoire : la règle du devis v2 arrêtait la file dès que 2 x coût projeté dépassait le plafond

# ---------- règle des appels aux modèles de Google (CLAUDE.md ; garde commune src/controle_ia/garde_google_v1.py, 04d233bd…) ----------
TEXTE_MIN_GOOGLE = 16000         # M : CLAUDE.md, « Appels aux modèles de Google » ; garde_google_v1.py:58
LIMITE_SORTIE_NEON = 65536       # M : page du modèle Neon versée (2eadc192…), ligne 53 ; garde_google_v1.py:56
SORTIE_ATT_NEON = 8000           # S : sortie attendue d'un appel de Neon au niveau de réflexion le plus haut ; aucune mesure

# ---------- essai d'admission et de mesure ; ancre ----------
ENSEMBLES_ESSAI = 12      # S : 8 ensembles honnêtes et 4 de dose flagrante par lecteur, forme du poste D1 (k questions)
ENSEMBLES_ESSAI_D3 = 8    # S : les 8 ensembles honnêtes de l'essai, relus dans la forme du poste D3 (k' questions)
ELEMENTS_ANCRE = 30       # M : pièce 6 v2, section 2, poste D4 (30 questions pour l'agent de l'ancre)
ADMISSION_JUGE = 8        # M : précédent du bras A, registres/go.md:632 (huit lectures d'admission)

# ---------- pour mémoire : totaux du devis v2 (sortie scellée du programme v2, 1e5586d4…) ----------
V2_ATTENDU_CENTRE, V2_PLAFOND, V2_ENSEMBLES = 84.7349, 396, 320


def dollars(x, n=2):
    return f"{x:.{n}f}".replace(".", ",")


def tronque(x, n=1):
    """Tronque vers le bas : une minuterie ne doit jamais permettre plus d'heures que le plafond n'en paie."""
    return math.floor(x * 10 ** n) / 10 ** n


def dessus(x, n=3):
    """Arrondi au-dessus à n décimales : un prix à retenir ne doit jamais être sous le prix calculé (point B)."""
    return math.ceil(round(x * 10 ** n, 9)) / 10 ** n


def plafond_entier(x):
    return math.ceil(round(x, 9))


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


def volumes(n_x_e, n_f_x_e, relectures=RELECTURES_EPREUVES):
    """Postes de la pièce 6 version 2, en épisodes et en ensembles lus par lecteur."""
    ep_a, ep_b, ep_c = 2 * n_x_e, 2 * n_x_e, n_f_x_e
    return {"ep_a": ep_a, "ep_b": ep_b, "ep_c": ep_c,
            "d1_1": ep_a + ep_c,   # poste D1, étape 1 : honnêtes et dose flagrante
            "d1_2": ep_b,          # poste D1, étape 2 : « sabotage demandé »
            "d2": relectures,      # poste D2, étape 1 : relectures des épreuves de manipulation
            "d3_a": ep_a,          # poste D3 sur les épisodes honnêtes
            "d3_b": ep_b}          # poste D3 sur les épisodes « sabotage demandé »


def files_de(v):
    """Files de lecture, par lecteur : (nom, ensembles lus avec k questions, ensembles lus avec k' questions)."""
    return (("essai", ENSEMBLES_ESSAI, ENSEMBLES_ESSAI_D3),
            ("étape 1 (D1 sur A et C, D2)", v["d1_1"] + v["d2"], 0),
            ("D3 sur les honnêtes", 0, v["d3_a"]),
            ("étape 2 (D1 et D3 sur B)", v["d1_2"], v["d3_b"]))


def questions(ens_k, ens_kp, k, kp):
    return ens_k * k + ens_kp * kp


def file_plafond(ens_k, ens_kp, k, kp, l1="opus", l2="mistral_repli", marge_l1=0.0, marge_l2=MARGE_CHANGE, groupe=False):
    """Plafond pessimiste d'une paire de files (un lecteur chacune) : dollars comptés par la garde, et engagement,
    marge de change comprise."""
    if groupe:
        c1 = ens_k * cout_ensemble_groupe(l1, k, False) + ens_kp * cout_ensemble_groupe(l1, kp, False)
        c2 = ens_k * cout_ensemble_groupe(l2, k, False) + ens_kp * cout_ensemble_groupe(l2, kp, False)
    else:
        q = questions(ens_k, ens_kp, k, kp)
        c1, c2 = q * cout_question(l1, False), q * cout_question(l2, False)
    e1, e2 = c1 * (1 + marge_l1), c2 * (1 + marge_l2)
    return c1, c2, e1, e2, plafond_entier(e1 + e2)


def regle_lancement(cout_projete, plafond_pessimiste):
    """Règle v3 : la file part si le coût projeté, majoré de la marge, tient dans le plafond pessimiste ; son plafond
    est alors le plus petit de deux fois le coût projeté et du plafond pessimiste."""
    part = (1 + MARGE_LANCEMENT) * cout_projete <= plafond_pessimiste + 1e-9
    return part, min(FACTEUR_PLAFOND_MESURE * cout_projete, plafond_pessimiste)


def sortie_equivalente(cout, modele):
    """Sortie moyenne par question, en jetons, qui donne ce coût aux entrées et aux reprises attendues."""
    pe, ps = PRIX[modele]
    return (cout * 1e6 / ENVOIS_ATT - ENTREE_ATT * pe) / ps


def variante(n_x_e):
    v = volumes(n_x_e, N_F)
    carte, carte2 = lancement(v["ep_a"] + v["ep_c"]), lancement(v["ep_b"])
    att = cout_question("opus") + cout_question("mistral")
    f = files_de(v)
    ens = v["d1_1"] + v["d1_2"] + v["d2"] + v["d3_a"] + v["d3_b"]
    lect_att = sum(questions(ek, ekp, K_CENTRE, KP_CENTRE) for _, ek, ekp in f[1:]) * att
    plafonds = [file_plafond(ek, ekp, K_MAX, KP_MAX)[4] for _, ek, ekp in f]
    return (v["ep_a"] + v["ep_b"] + v["ep_c"], ens, carte[1] + carte2[1], carte[2] + carte2[2], carte[4] + carte2[4],
            lect_att, sum(plafonds[1:]), carte[4] + carte2[4] + sum(plafonds))


def main():
    v = volumes(N_TACHES * E, N_F * E)
    ep_a, ep_b, ep_c = v["ep_a"], v["ep_b"], v["ep_c"]
    f = files_de(v)
    f_lect = f[1:]
    ens_d1, ens_d2, ens_d3 = v["d1_1"] + v["d1_2"], v["d2"], v["d3_a"] + v["d3_b"]
    ens_tot = ens_d1 + ens_d2 + ens_d3
    ens_k_tot, ens_kp_tot = ens_d1 + ens_d2, ens_d3

    print("== 1. Volumes (tailles de principe de la pièce 6, version 2) ==")
    print(f"épisodes honnêtes A = {ep_a} ; « sabotage demandé » B = {ep_b} ; dose flagrante C = {ep_c} ; total = {ep_a + ep_b + ep_c}")
    print(f"actions = {(ep_a + ep_b + ep_c) * A_PAS} (a = {A_PAS})")
    print(f"ensembles lus par lecteur : poste D1 = {ens_d1} (étape 1 : {v['d1_1']} ; étape 2 : {v['d1_2']}) ; poste D2 = {ens_d2} "
          f"(étape 1) ; poste D3 = {ens_d3} (honnêtes : {v['d3_a']} ; « sabotage demandé » : {v['d3_b']}) ; total = {ens_tot} ; "
          f"pour mémoire, devis v2 : {V2_ENSEMBLES} ; rapport : {dollars(ens_tot / V2_ENSEMBLES, 2)}")
    print(f"questions par lecteur : {ens_k_tot} x k + {ens_kp_tot} x k'")
    for k in VALEURS_K:
        print(f"  k = k' = {k} : questions par lecteur = {questions(ens_k_tot, ens_kp_tot, k, k)} ; par file : " + " ; ".join(
            f"{nom} = {questions(ek, ekp, k, k)}" for nom, ek, ekp in f))
    controle_ep = ep_a // 2 + ep_c
    controle_ens = controle_ep + ens_d2
    mesure_ens = ep_a // 2 + ep_b
    print(f"part des contrôles : {controle_ep} épisodes sur {ep_a + ep_b + ep_c} ({100 * controle_ep / (ep_a + ep_b + ep_c):.0f} %) ; "
          f"ensembles lus par lecteur : contrôles {controle_ens} sur {ens_tot} ({100 * controle_ens / ens_tot:.0f} %), "
          f"oracles rapportés à côté {ens_d3} ({100 * ens_d3 / ens_tot:.0f} %), mesure principale {mesure_ens} ({100 * mesure_ens / ens_tot:.0f} %)")

    print("\n== 2. Carte : prix d'une action, lancements, minuteries (inchangé depuis le devis v2) ==")
    pa_bas, pa_haut = D_HAUT / A_PAS * PRIX_RELEVE_OFFRE / 3600, D_HAUT / A_PAS * PRIX_DEVIS / 3600
    print(f"prix d'une action p_a = {dollars(pa_bas, 5)} à {dollars(pa_haut, 5)} dollar ({dollars(D_HAUT / A_PAS, 2)} s par action ; "
          f"bas au prix de l'offre, stockage compris, {dollars(PRIX_RELEVE_OFFRE, 4)} ; haut à {dollars(PRIX_DEVIS)}) ; "
          f"arrondi au-dessus, à quatre décimales : {dollars(dessus(pa_bas, 4), 4)} à {dollars(dessus(pa_haut, 4), 4)} ; "
          f"par épisode : {dollars(D_HAUT * PRIX_RELEVE_OFFRE / 3600, 4)} à {dollars(D_HAUT * PRIX_DEVIS / 3600, 4)}")
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
    print(f"lancement 2 recalculé sur le débit d mesuré au lancement 1 : heures = 2 x (1,0 + {ep_b} x 1,5 x d / 3600) ; "
          f"plafond = {dollars(PRIX_DEVIS)} x heures + 4 ; pour d = {dollars(D_HAUT, 1)} : plafond {dollars(plafond_l2_recalc)} ; "
          f"heures payées {dollars(heures_l2_recalc)} ; minuterie, tronquée : {dollars(tronque(heures_l2_recalc), 1)} h")
    plafond_carte_l2 = lancement(ep_b)[4]
    d_max = ((plafond_carte_l2 - TEL_PESSIMISTE) / (2 * PRIX_DEVIS) - MISE_EN_ROUTE_H) * 3600 / (ep_b * MAJORATION_SABOTAGE)
    print(f"débit au-delà duquel la formule sort du plafond de {plafond_carte_l2} du lancement 2 : {dollars(d_max, 1)} s par épisode")
    carte_att_centre = (total_att_bas + total_att_haut) / 2
    carte_plafond = total_plafond

    print("\n== 3. Lecteurs : prix d'une lecture (une question, le plan renvoyé à chaque appel) ==")
    for m in ("opus", "sonnet", "mistral", "mistral_repli"):
        print(f"{m:14s} attendu {dollars(cout_question(m), 4)} ; pessimiste {dollars(cout_question(m, False), 4)}")
    q_opus_att, q_opus_pess = cout_question("opus"), cout_question("opus", False)
    q_mistral_att, q_mistral_pess = cout_question("mistral"), cout_question("mistral_repli", False)
    q_mistral_compte_att = cout_question("mistral_repli")
    print(f"prix à retenir au point 1, arrondis au-dessus à trois décimales (point B de la vérification) : Opus 5.5 "
          f"{dollars(dessus(q_opus_att), 3)} attendu et {dollars(dessus(q_opus_pess), 3)} au pire ; Mistral Large 4 "
          f"{dollars(dessus(q_mistral_att), 3)} attendu et {dollars(dessus(q_mistral_pess), 3)} au pire, "
          f"{dollars(dessus(q_mistral_pess * (1 + MARGE_CHANGE)), 3)} avec la marge de change ; valeurs à cinq décimales : "
          f"{dollars(q_opus_att, 5)}, {dollars(q_opus_pess, 5)}, {dollars(q_mistral_att, 5)}, {dollars(q_mistral_pess, 5)} et "
          f"{dollars(q_mistral_pess * (1 + MARGE_CHANGE), 5)}")
    print(f"coût attendu d'une question de Mistral tel que la garde le compte, au prix de repli : {dollars(q_mistral_compte_att, 4)} "
          f"(le double de la facture attendue au prix relevé, {dollars(q_mistral_att, 4)}) ; question de Mistral au pire, au prix de repli, "
          f"avec la marge de change : {dollars(q_mistral_pess * (1 + MARGE_CHANGE), 4)}")
    envoi_opus = (ENTREE_GARDE * PRIX["opus"][0] + SORTIE_MAX_CLAUDE * PRIX["opus"][1]) / 1e6
    envoi_sonnet = (ENTREE_GARDE * PRIX["sonnet"][0] + SORTIE_MAX_CLAUDE * PRIX["sonnet"][1]) / 1e6
    envoi_mistral = (ENTREE_GARDE * PRIX["mistral_repli"][0] + SORTIE_MAX_MISTRAL * PRIX["mistral_repli"][1]) / 1e6
    print(f"pire cas d'un seul envoi, qui sert à la garde avant l'envoi ({ENTREE_GARDE} jetons d'entrée comptés, sortie maximale pleine) : "
          f"opus {dollars(envoi_opus, 4)} ; sonnet {dollars(envoi_sonnet, 4)} ; mistral au prix de repli {dollars(envoi_mistral, 4)} "
          f"(sortie maximale supposée {SORTIE_MAX_MISTRAL})")
    rapide = cout_question("opus", False, prix=PRIX_OPUS_RAPIDE)
    cache = cout_question("opus", False, prix=(ECRITURE_CACHE_OPUS, PRIX["opus"][1]))
    q_tot_max = sum(questions(ek, ekp, K_MAX, KP_MAX) for _, ek, ekp in f)
    q_tot_centre = sum(questions(ek, ekp, K_CENTRE, KP_CENTRE) for _, ek, ekp in f)
    q_lect_max = questions(ens_k_tot, ens_kp_tot, K_MAX, KP_MAX)
    q_lect_centre = questions(ens_k_tot, ens_kp_tot, K_CENTRE, KP_CENTRE)
    print(f"ce que le plafond ne couvre pas, par question d'Opus 5.5 au pire : mode rapide {dollars(rapide, 4)} "
          f"(x {dollars(rapide / q_opus_pess, 1)}) ; géographie « us » {dollars(q_opus_pess * FACTEUR_GEO_US, 4)} (x {dollars(FACTEUR_GEO_US, 1)}) ; "
          f"les deux {dollars(rapide * FACTEUR_GEO_US, 4)} (x {dollars(rapide * FACTEUR_GEO_US / q_opus_pess, 1)}) ; "
          f"entrée écrite au cache à {dollars(ECRITURE_CACHE_OPUS, 0)} dollars : {dollars(cache, 4)} (x {dollars(cache / q_opus_pess, 3)}), "
          f"soit {dollars((cache - q_opus_pess) * q_tot_max)} de plus sur la part de Claude à k = k' = {K_MAX} ({q_tot_max} questions, essai compris) ; "
          f"pire cas d'un envoi avec l'entrée à {dollars(ECRITURE_CACHE_OPUS, 0)} : "
          f"{dollars((ENTREE_GARDE * ECRITURE_CACHE_OPUS + SORTIE_MAX_CLAUDE * PRIX['opus'][1]) / 1e6, 4)}")

    print("\n== 4. Lectures du dommage, deux lecteurs, par valeur de k (k' = k ; dollars comptés, sans marge de change) ==")
    paires = (("opus", "mistral", "mistral_repli"), ("sonnet", "mistral", "mistral_repli"))
    for l1, l2, l2_repli in paires:
        att = cout_question(l1) + cout_question(l2)
        pess = cout_question(l1, False) + cout_question(l2_repli, False)
        pess_scelle = cout_question(l1, False) + cout_question(l2, False)
        print(f"paire {l1} + mistral : par question, attendu {dollars(att, 4)} ; pessimiste {dollars(pess, 4)} "
              f"(prix de Mistral scellé : {dollars(pess_scelle, 4)})")
        for k in VALEURS_K:
            q = questions(ens_k_tot, ens_kp_tot, k, k)
            groupe = (ens_k_tot + ens_kp_tot) * (cout_ensemble_groupe(l1, k) + cout_ensemble_groupe(l2, k))
            print(f"  k = k' = {k} : {q} questions par lecteur ; attendu {dollars(q * att)} (D1 : {dollars(ens_d1 * k * att)} ; "
                  f"D2 : {dollars(ens_d2 * k * att)} ; D3 : {dollars(ens_d3 * k * att)}) ; pessimiste {dollars(q * pess)} ; "
                  f"prix de Mistral scellé : {dollars(q * pess_scelle)} ; variante groupée, attendu {dollars(groupe)}")
    att = q_opus_att + q_mistral_att
    pess = q_opus_pess + q_mistral_pess
    lect_centre = q_lect_centre * att
    print(f"attendu au centre (k = k' = {K_CENTRE}), par file : " + " ; ".join(
        f"{nom} = {dollars(questions(ek, ekp, K_CENTRE, KP_CENTRE) * att)}" for nom, ek, ekp in f))
    print(f"si k' diffère de k : chaque unité de k' ajoute {ens_kp_tot} questions par lecteur, soit {dollars(ens_kp_tot * att)} à l'attendu "
          f"et {dollars(ens_kp_tot * (q_opus_pess + q_mistral_pess * (1 + MARGE_CHANGE)))} au plafond ; chaque unité de k, {ens_k_tot} questions, "
          f"soit {dollars(ens_k_tot * att)} et {dollars(ens_k_tot * (q_opus_pess + q_mistral_pess * (1 + MARGE_CHANGE)))}")

    print("\n== 5. Plafond pessimiste de chaque file de lecture, à k = k' = 8 ; marge de change sur la part de Mistral ==")
    print(f"marge de change : {100 * MARGE_CHANGE:.0f} % sur la part du compte Mistral (crédit relevé en euros) ; la garde compte en dollars, "
          f"sans la marge, la file de Mistral au prix de repli ; l'engagement porte la marge")
    somme_opus = somme_mistral = somme_mistral_eng = 0.0
    plafonds = {}
    files_p = {}
    for nom, ek, ekp in f:
        c1, c2, e1, e2, plafond = file_plafond(ek, ekp, K_MAX, KP_MAX)
        somme_opus += c1
        somme_mistral += c2
        somme_mistral_eng += e2
        plafonds[nom] = plafond
        files_p[nom] = (c1, c2, e2)
        print(f"{nom:28s} : {questions(ek, ekp, K_MAX, KP_MAX)} questions par lecteur ; file d'Opus 5.5 = {dollars(c1)} ; "
              f"file de Mistral au prix de repli = {dollars(c2)} comptés, {dollars(e2)} à l'engagement ; "
              f"les deux files, à l'engagement = {dollars(e1 + e2)} ; plafond = {plafond}")
    plafond_essai = plafonds["essai"]
    plafond_lectures = sum(p for nom, p in plafonds.items() if nom != "essai")
    print(f"plafonds des paires de files : essai {plafond_essai} ; lectures " + " + ".join(str(plafonds[nom]) for nom, _, _ in f_lect)
          + f" = {plafond_lectures} ; lectures et essai = {plafond_lectures + plafond_essai}")
    print(f"par compte, essai compris (k = k' = {K_MAX}) : Claude {dollars(somme_opus)}, plafond {plafond_entier(somme_opus)} ; "
          f"Mistral {dollars(somme_mistral)} comptés, {dollars(somme_mistral_eng)} à l'engagement "
          f"(marge de change : {dollars(somme_mistral_eng - somme_mistral)}), plafond {plafond_entier(somme_mistral_eng)} ; "
          f"ensemble {plafond_entier(somme_opus) + plafond_entier(somme_mistral_eng)}")
    print(f"somme des huit files : {dollars(somme_opus + somme_mistral)} comptés ; {dollars(somme_opus + somme_mistral_eng)} à l'engagement")
    print(f"attendu par compte au centre, essai compris (k = k' = {K_CENTRE}, {q_tot_centre} questions) : Claude {dollars(q_tot_centre * q_opus_att)} ; "
          f"Mistral {dollars(q_tot_centre * q_mistral_att)}")
    print(f"compte Mistral : crédit relevé « d'au moins 7,87 € » (registres/go.md:674) ; part de cette banque : {dollars(q_tot_centre * q_mistral_att)} dollars "
          f"attendus au centre, {plafond_entier(somme_mistral_eng)} au plafond")
    prix_question_engagement = q_opus_pess + q_mistral_pess * (1 + MARGE_CHANGE)
    print(f"prix pessimiste d'une question pour les deux lecteurs : {dollars(pess, 4)} compté ; {dollars(prix_question_engagement, 4)} "
          f"avec la marge de change ; formule si k ou k' dépasse {K_MAX} : ({ens_k_tot} x k + {ens_kp_tot} x k') x {dollars(prix_question_engagement, 4)}")
    print("lectures au pire, marge de change comprise, par valeur de k (k' = k) : " + " ; ".join(
        f"k = {k} : {dollars(questions(ens_k_tot, ens_kp_tot, k, k) * prix_question_engagement)}" for k in VALEURS_K))
    scelle = q_lect_max * (q_opus_pess + cout_question("mistral", False) * (1 + MARGE_CHANGE))
    repli = q_lect_max * prix_question_engagement
    print(f"si la page de prix de Mistral est scellée au prix relevé, lectures à k = k' = {K_MAX} : {dollars(q_lect_max * pess)} comptés "
          f"deviennent {dollars(q_lect_max * (q_opus_pess + cout_question('mistral', False)))} ; marge de change comprise, {dollars(repli)} devient {dollars(scelle)}")
    refus_opus = math.ceil(envoi_opus / (q_opus_pess / ENVOIS_PESS)) - 1
    refus_mistral = math.ceil(envoi_mistral / (q_mistral_pess / ENVOIS_PESS)) - 1
    print(f"effet de bord de la garde avant l'envoi : une file s'arrête dès que le cumul compté dépasse son plafond moins le pire cas "
          f"d'un envoi ; si chaque envoi coûtait exactement le prix pessimiste, derniers envois refusés : Opus {refus_opus} ; Mistral {refus_mistral}")

    print("\n== 6. Règle de lancement d'une file après mesure (point A de la vérification, voie 2) ==")
    print(f"règle : coût projeté = coût mesuré par question à l'essai (dépense comptée par la garde, reprises comprises) x nombre de questions "
          f"de la file ; la file part si {dollars(1 + MARGE_LANCEMENT, 1)} x coût projeté <= plafond pessimiste de la file ; son plafond est alors "
          f"min({dollars(FACTEUR_PLAFOND_MESURE, 0)} x coût projeté ; plafond pessimiste) ; sinon devis neuf")
    print(f"conséquence : le plafond d'une file qui part vaut entre {dollars(1 + MARGE_LANCEMENT, 1)} et {dollars(FACTEUR_PLAFOND_MESURE, 0)} fois son coût projeté ; "
          f"sa garde ne la coupe que si le coût réel dépasse le coût projeté de {100 * MARGE_LANCEMENT:.0f} % au moins")
    print("seuil du coût mesuré par question au-dessous duquel la file part (k' = k), et sortie moyenne équivalente aux entrées et reprises attendues :")
    for k in VALEURS_K:
        s_opus = q_opus_pess * K_MAX / ((1 + MARGE_LANCEMENT) * k)
        s_mistral = q_mistral_pess * K_MAX / ((1 + MARGE_LANCEMENT) * k)
        v2_opus = q_opus_pess * K_MAX / (FACTEUR_REGLE_V2 * k)
        v2_mistral = q_mistral_pess * K_MAX / (FACTEUR_REGLE_V2 * k)
        print(f"  k = {k} : Opus 5.5 {dollars(s_opus, 4)} ({sortie_equivalente(s_opus, 'opus'):.0f} jetons) ; Mistral, compté au prix de repli, "
              f"{dollars(s_mistral, 4)} ({sortie_equivalente(s_mistral, 'mistral_repli'):.0f} jetons) ; pour mémoire, règle du devis v2 : "
              f"Opus {dollars(v2_opus, 4)} ({sortie_equivalente(v2_opus, 'opus'):.0f} jetons), Mistral {dollars(v2_mistral, 4)} "
              f"({sortie_equivalente(v2_mistral, 'mistral_repli'):.0f} jetons)")
    print(f"seuils en jetons de sortie, arrondis à la dizaine au-dessous, à k = k' = {K_CENTRE} puis {K_MAX} : Opus 5.5 "
          + " et ".join(str(int(sortie_equivalente(q_opus_pess * K_MAX / ((1 + MARGE_LANCEMENT) * k), 'opus') // 10 * 10)) for k in (K_CENTRE, K_MAX))
          + " ; Mistral "
          + " et ".join(str(int(sortie_equivalente(q_mistral_pess * K_MAX / ((1 + MARGE_LANCEMENT) * k), 'mistral_repli') // 10 * 10)) for k in (K_CENTRE, K_MAX))
          + f" ; sorties supposées : Opus {SORTIE_ATT['opus']} attendus et {SORTIE_PESS['opus']} au pire, Mistral {SORTIE_ATT['mistral']} et {SORTIE_PESS['mistral']}")
    q_v2_etape1 = (2 * N_TACHES * E + N_F * E + RELECTURES_EPREUVES_V1) * K_MAX
    c_moyen = cout_question("opus", True, sortie=1000)
    print(f"pour mémoire, sur les volumes du devis v2 : file d'Opus 5.5 de l'étape 1, {q_v2_etape1} questions à k = {K_MAX}, plafond "
          f"{dollars(q_v2_etape1 * q_opus_pess)} ; à l'effort moyen, coût projeté {dollars(q_v2_etape1 * c_moyen)}, deux fois : "
          f"{dollars(2 * q_v2_etape1 * c_moyen)} : la règle du devis v2 arrêtait la file ; exemples du devis v2 pour Mistral, au prix relevé, "
          f"à k = {K_CENTRE} : {dollars(2 * (q_v2_etape1 // K_MAX) * K_CENTRE * q_mistral_att)} et "
          f"{dollars(2 * (2 * N_TACHES * E) * K_CENTRE * q_mistral_att)}")
    print("lecteur Claude selon l'effort (sorties supposées, S) : la file d'Opus 5.5 part-elle ?")
    for nom, sortie in SORTIE_EFFORT + (("sortie maximale du corps", SORTIE_MAX_CLAUDE),):
        c = cout_question("opus", True, sortie=sortie)
        k_lim = q_opus_pess * K_MAX / ((1 + MARGE_LANCEMENT) * c)
        k_lim_v2 = q_opus_pess * K_MAX / (FACTEUR_REGLE_V2 * c)
        etats = " ; ".join(f"k = {k} : {'part' if (1 + MARGE_LANCEMENT) * c * k <= q_opus_pess * K_MAX + 1e-12 else 'ne part pas'} "
                           f"(1,5 x {dollars(c, 4)} x {k} = {dollars((1 + MARGE_LANCEMENT) * c * k, 4)} contre {dollars(q_opus_pess * K_MAX, 4)})"
                           for k in (K_CENTRE, K_MAX))
        print(f"  effort {nom} ({sortie} jetons, {dollars(c, 4)} par question) : {etats} ; part tant que k <= {dollars(k_lim, 2)} "
              f"(règle du devis v2 : k <= {dollars(k_lim_v2, 2)})")
    c_haut = cout_question("opus", True, sortie=2000)
    print(f"devis neuf qui suivrait un arrêt à l'effort haut, k = k' = {K_MAX} : part de Claude projetée {dollars(q_tot_max * c_haut)} "
          f"(essai compris), plafond à deux fois : {dollars(2 * q_tot_max * c_haut)}, soit {plafond_entier(2 * q_tot_max * c_haut)} "
          f"au lieu de {plafond_entier(somme_opus)} ({plafond_entier(2 * q_tot_max * c_haut) - plafond_entier(somme_opus)} de plus)")
    print(f"exemple : la mesure vaut l'attendu, k = k' = {K_CENTRE} (Mistral compté au prix de repli, {dollars(q_mistral_compte_att, 4)} par question) :")
    somme_recalc = 0
    for nom, ek, ekp in f_lect:
        q = questions(ek, ekp, K_CENTRE, KP_CENTRE)
        c1, c2, _ = files_p[nom]
        v1, v2_ = q * q_opus_att, q * q_mistral_compte_att
        ok1, p1 = regle_lancement(v1, c1)
        ok2, p2 = regle_lancement(v2_, c2)
        somme_recalc += plafond_entier(p1 + p2 * (1 + MARGE_CHANGE))
        print(f"  {nom} ({q} questions) : Opus projeté {dollars(v1)}, {'part' if ok1 else 'ne part pas'}, plafond min({dollars(2 * v1)} ; {dollars(c1)}) = {dollars(p1)} ; "
              f"Mistral projeté {dollars(v2_)}, {'part' if ok2 else 'ne part pas'}, plafond min({dollars(2 * v2_)} ; {dollars(c2)}) = {dollars(p2)} comptés, "
              f"{dollars(p2 * (1 + MARGE_CHANGE))} à l'engagement ; les deux : {dollars(p1 + p2 * (1 + MARGE_CHANGE))}, plafond {plafond_entier(p1 + p2 * (1 + MARGE_CHANGE))}")
    print(f"  somme des plafonds des lectures après une mesure égale à l'attendu : {somme_recalc} au lieu de {plafond_lectures}")

    print("\n== 7. Essai d'admission et de mesure ; ancre jugée par un agent (poste D4) ==")
    q_essai_centre = questions(ENSEMBLES_ESSAI, ENSEMBLES_ESSAI_D3, K_CENTRE, KP_CENTRE)
    q_essai_max = questions(ENSEMBLES_ESSAI, ENSEMBLES_ESSAI_D3, K_MAX, KP_MAX)
    essai_att = q_essai_centre * att
    c1, c2, e2 = files_p["essai"]
    print(f"essai : {ENSEMBLES_ESSAI} ensembles par lecteur dans la forme du poste D1 et {ENSEMBLES_ESSAI_D3} dans la forme du poste D3 ; "
          f"{q_essai_centre} questions par lecteur à k = k' = {K_CENTRE}, {q_essai_max} à k = k' = {K_MAX} ; attendu au centre : {dollars(essai_att)} ; "
          f"pessimiste : file d'Opus 5.5 {dollars(c1)}, file de Mistral {dollars(c2)} comptés, {dollars(e2)} à l'engagement ; plafond {plafond_essai} ; "
          f"pour mémoire, essai du devis v2 (12 ensembles, forme D1 seule) : plafond 13")
    honnetes = file_plafond(ENSEMBLES_ESSAI_D3, ENSEMBLES_ESSAI_D3, K_MAX, KP_MAX)
    flagrants = file_plafond(ENSEMBLES_ESSAI - ENSEMBLES_ESSAI_D3, 0, K_MAX, KP_MAX)
    print(f"essai, par partie, à k = k' = {K_MAX} : ensembles honnêtes seuls ({ENSEMBLES_ESSAI_D3} en forme D1 et {ENSEMBLES_ESSAI_D3} en forme D3, "
          f"{questions(ENSEMBLES_ESSAI_D3, ENSEMBLES_ESSAI_D3, K_MAX, KP_MAX)} questions par lecteur) : Opus {dollars(honnetes[0])}, Mistral {dollars(honnetes[1])} comptés, "
          f"{dollars(honnetes[3])} à l'engagement, ensemble {dollars(honnetes[2] + honnetes[3])} ; ensembles de dose flagrante "
          f"({ENSEMBLES_ESSAI - ENSEMBLES_ESSAI_D3} en forme D1, {questions(ENSEMBLES_ESSAI - ENSEMBLES_ESSAI_D3, 0, K_MAX, KP_MAX)} questions) : Opus {dollars(flagrants[0])}, "
          f"Mistral {dollars(flagrants[1])} comptés, {dollars(flagrants[3])} à l'engagement, ensemble {dollars(flagrants[2] + flagrants[3])}")
    appels_ancre = ELEMENTS_ANCRE + ADMISSION_JUGE
    envois_ancre_pire = math.ceil(appels_ancre * ENVOIS_PESS)
    envoi_neon_pire = (ENTREE_GARDE * PRIX["neon"][0] + LIMITE_SORTIE_NEON * PRIX["neon"][1]) / 1e6
    ancre_compte = envois_ancre_pire * envoi_neon_pire
    ancre_eng = ancre_compte * (1 + MARGE_CHANGE)
    ancre_plafond = plafond_entier(ancre_eng)
    appel_neon_att = (ENTREE_ATT * PRIX["neon"][0] + SORTIE_ATT_NEON * PRIX["neon"][1]) * ENVOIS_ATT / 1e6
    ancre_att = appels_ancre * appel_neon_att
    print(f"règle des appels aux modèles de Google, pour Gemini 4 Neon : niveau de réflexion le plus haut admis, explicite dans le corps ; "
          f"plafond de sortie {LIMITE_SORTIE_NEON} (limite d'un appel), soit {LIMITE_SORTIE_NEON - TEXTE_MIN_GOOGLE} jetons de réflexion "
          f"au plus et {TEXTE_MIN_GOOGLE} de texte ; pire cas d'un envoi, borné par le corps : ({ENTREE_GARDE} x {dollars(PRIX['neon'][0], 0)} + "
          f"{LIMITE_SORTIE_NEON} x {dollars(PRIX['neon'][1], 0)}) / 1 000 000 = {dollars(envoi_neon_pire, 4)} dollar "
          f"({dollars(envoi_neon_pire / envoi_opus, 1)} fois celui d'Opus 5.5)")
    print(f"ancre par Gemini 4 Neon : {appels_ancre} appels ({ELEMENTS_ANCRE} questions et {ADMISSION_JUGE} lectures d'admission) ; au pire, "
          f"{envois_ancre_pire} envois ({appels_ancre} x {dollars(ENVOIS_PESS)}, arrondi au-dessus), chacun compté à sa borne : "
          f"{dollars(ancre_compte)} comptés, {dollars(ancre_eng)} avec la marge de change (compte Google affiché en euros) ; plafond {ancre_plafond} ; "
          f"attendu, à {SORTIE_ATT_NEON} jetons de sortie par appel (S) : {dollars(appel_neon_att, 4)} par appel, {dollars(ancre_att)} ; "
          f"pour mémoire, devis v2 : plafond 5, sur des sorties de 1 500 et 6 000 jetons, sans la règle")
    print(f"prix d'une lecture par l'agent de l'ancre, p_anc, si c'est Neon, arrondi au-dessus à trois décimales : {dollars(dessus(appel_neon_att), 3)} "
          f"attendu (S) ; {dollars(dessus(envoi_neon_pire), 3)} au pire, borné par le corps ; {dollars(dessus(envoi_neon_pire * (1 + MARGE_CHANGE)), 3)} "
          f"avec la marge de change ; à quatre décimales : {dollars(appel_neon_att, 4)}, {dollars(envoi_neon_pire, 4)} et "
          f"{dollars(envoi_neon_pire * (1 + MARGE_CHANGE), 4)}")
    ancre_claude = appels_ancre * q_opus_pess
    print(f"ancre par un agent Claude : en session, 0 dollar de ligne ; par appel de programme sur la clé Claude (Opus 5.5), au pire "
          f"{appels_ancre} x {dollars(q_opus_pess, 4)} = {dollars(ancre_claude)}")

    print("\n== 8. Totaux ==")
    centre = carte_att_centre + lect_centre + essai_att
    print(f"attendu, centre (k = k' = {K_CENTRE}, une question par appel, opus + mistral), hors ancre : carte {dollars(carte_att_centre)} + "
          f"lectures {dollars(lect_centre)} + essai {dollars(essai_att)} = {dollars(centre)} ; avec l'ancre par Neon ({dollars(ancre_att)}) : "
          f"{dollars(centre + ancre_att)}")
    c_l1 = sum(lancement(ep_a + ep_c)[1:3]) / 2
    c_l2 = sum(lancement(ep_b)[1:3]) / 2
    att_f = {nom: questions(ek, ekp, K_CENTRE, KP_CENTRE) * att for nom, ek, ekp in f}
    etape1_att = c_l1 + att_f["essai"] + att_f["étape 1 (D1 sur A et C, D2)"] + att_f["D3 sur les honnêtes"]
    etape2_att = c_l2 + att_f["étape 2 (D1 et D3 sur B)"]
    print(f"attendu au centre, par étape, hors ancre : étape 1 = carte {dollars(c_l1)} + essai {dollars(att_f['essai'])} + lectures "
          f"{dollars(att_f['étape 1 (D1 sur A et C, D2)'])} + D3 sur les honnêtes {dollars(att_f['D3 sur les honnêtes'])} = {dollars(etape1_att)} ; "
          f"étape 2 = carte {dollars(c_l2)} + lectures {dollars(att_f['étape 2 (D1 et D3 sur B)'])} = {dollars(etape2_att)}")
    n_appels_groupe = ENSEMBLES_ESSAI + ENSEMBLES_ESSAI_D3 + ens_k_tot + ens_kp_tot
    groupe_bas = cout_ensemble_groupe("sonnet", 3) + cout_ensemble_groupe("mistral", 3)
    bas = total_att_bas + n_appels_groupe * groupe_bas
    haut = total_att_haut + q_tot_max * att
    print(f"attendu, fourchette, hors ancre : bas (k = k' = 3, lecture groupée, sonnet + mistral, {n_appels_groupe} appels par lecteur) {dollars(bas)} ; "
          f"haut (k = k' = {K_MAX}, une question par appel, opus + mistral) {dollars(haut)} ; par ligne : lectures "
          f"{dollars((ens_k_tot + ens_kp_tot) * groupe_bas)} à {dollars(q_lect_max * att)} ; essai "
          f"{dollars((ENSEMBLES_ESSAI + ENSEMBLES_ESSAI_D3) * groupe_bas)} à {dollars(q_essai_max * att)} ; avec l'ancre "
          f"(0 par un agent Claude de session, {dollars(ancre_att)} par Neon) : {dollars(bas)} à {dollars(haut + ancre_att)}")
    plafond_total = carte_plafond + plafond_lectures + plafond_essai
    print(f"plafond pessimiste (k <= {K_MAX}, k' <= {KP_MAX}), hors ancre : carte {carte_plafond:.0f} + lectures {plafond_lectures} + essai {plafond_essai} = "
          f"{plafond_total:.0f} ; avec l'ancre par Neon ({ancre_plafond}) : {plafond_total + ancre_plafond:.0f} ; pour mémoire, devis v2 : {V2_PLAFOND}")
    print(f"sans aucun arrondi, engagement : carte {dollars(pire_tot)} + lectures et essai {dollars(somme_opus + somme_mistral_eng)} = "
          f"{dollars(pire_tot + somme_opus + somme_mistral_eng)} ; avec l'ancre {dollars(pire_tot + somme_opus + somme_mistral_eng + ancre_eng)}")
    print(f"marge, hors ancre : plafond moins attendu au centre = {dollars(plafond_total - centre)} ; rapport {dollars(plafond_total / centre, 1)} ; "
          f"seuil d'alerte à 80 % du plafond = {dollars(0.8 * plafond_total)} ; avec l'ancre par Neon : marge "
          f"{dollars(plafond_total + ancre_plafond - centre - ancre_att)}, rapport {dollars((plafond_total + ancre_plafond) / (centre + ancre_att), 1)}, "
          f"seuil {dollars(0.8 * (plafond_total + ancre_plafond))}")
    etape1 = lancement(ep_a + ep_c)[4] + plafond_essai + plafonds["étape 1 (D1 sur A et C, D2)"] + plafonds["D3 sur les honnêtes"]
    etape2 = lancement(ep_b)[4] + plafonds["étape 2 (D1 et D3 sur B)"]
    print(f"par étape, hors ancre : étape 1 (lancement 1, essai, lectures 1, D3 sur les honnêtes) = {etape1} ; étape 2 (lancement 2, lectures 2) = {etape2} ; "
          f"l'ancre ({ancre_plafond}) va avec les épreuves, à l'étape 1 : {etape1 + ancre_plafond} ; si le poste D3 sur les honnêtes attend l'étape 2 : "
          f"{etape1 - plafonds['D3 sur les honnêtes']} et {etape2 + plafonds['D3 sur les honnêtes']}")
    tout_claude = carte_plafond + sum(file_plafond(ek, ekp, K_MAX, KP_MAX, marge_l1=MARGE_CHANGE)[4] for _, ek, ekp in f)
    tout_euros = (sum(math.ceil(lancement(n_)[3] * (1 + MARGE_CHANGE)) for n_ in (ep_a + ep_c, ep_b))
                  + sum(file_plafond(ek, ekp, K_MAX, KP_MAX, marge_l1=MARGE_CHANGE)[4] for _, ek, ekp in f))
    print(f"variantes de la marge de change, hors ancre : si le compte Claude désigné était aussi facturé en euros, part de Claude "
          f"{dollars(somme_opus * (1 + MARGE_CHANGE))} (soit {dollars(somme_opus * MARGE_CHANGE)} de plus), plafond total {tout_claude:.0f} ; "
          f"si toute la dépense l'était, carte comprise : {tout_euros:.0f}")
    g = {nom: file_plafond(ek, ekp, K_MAX, KP_MAX, groupe=True) for nom, ek, ekp in f}
    groupe_pess = cout_ensemble_groupe("opus", K_MAX, False) + cout_ensemble_groupe("mistral_repli", K_MAX, False)
    groupe_eng = cout_ensemble_groupe("opus", K_MAX, False) + cout_ensemble_groupe("mistral_repli", K_MAX, False) * (1 + MARGE_CHANGE)
    g_lect = sum(g[nom][4] for nom, _, _ in f_lect)
    print(f"si la lecture groupée est attestée (un appel par ensemble, k <= {K_MAX} et k' <= {KP_MAX}) : par ensemble, pessimiste {dollars(groupe_pess, 4)} comptés, "
          f"{dollars(groupe_eng, 4)} à l'engagement ; lectures " + " + ".join(str(g[nom][4]) for nom, _, _ in f_lect) + f" = {g_lect} ; essai {g['essai'][4]} ; "
          f"plafond total, hors ancre : {carte_plafond + g_lect + g['essai'][4]:.0f} ; avec l'ancre par Neon : {carte_plafond + g_lect + g['essai'][4] + ancre_plafond:.0f} ; files : "
          + " ; ".join(f"{nom}, Opus {dollars(g[nom][0])} et Mistral {dollars(g[nom][1])} comptés ({dollars(g[nom][3])})" for nom, _, _ in f))

    print("\n== 9. Variantes de taille : 100 et 200 épisodes par dose ==")
    for n_x_e in (100, 200):
        ep, ens, carte_bas, carte_haut, carte_plaf, l_att, l_plafond, total = variante(n_x_e)
        print(f"n x e = {n_x_e} : épisodes {ep} ; ensembles lus par lecteur {ens} ; carte attendu {dollars(carte_bas)} à {dollars(carte_haut)}, "
              f"plafond {carte_plaf} ; lectures attendu à k = k' = {K_CENTRE} : {dollars(l_att)}, plafond à k = k' = {K_MAX} : {l_plafond} ; "
              f"plafond total avec l'essai, hors ancre : {total}")

    print("\n== 10. Chiffres dérivés cités au devis ==")
    print(f"lectures : plafond sur attendu au centre = {dollars(plafond_lectures / lect_centre, 1)} ; "
          f"économie de Sonnet 5.5 au centre = {dollars(lect_centre - q_lect_centre * (cout_question('sonnet') + q_mistral_att))}")
    part_controles = (controle_ens * K_CENTRE * att) + controle_ep * D_HAUT * PRIX_DEVIS / 3600
    print(f"part des conditions de contrôle dans l'attendu au centre = {dollars(part_controles)} (lectures {dollars(controle_ens * K_CENTRE * att)}, "
          f"carte {dollars(controle_ep * D_HAUT * PRIX_DEVIS / 3600)}) ; oracles rapportés à côté = {dollars(ens_d3 * KP_CENTRE * att)}")
    print(f"reprises des lectures : dans l'attendu au centre = {dollars((lect_centre + essai_att) * (ENVOIS_ATT - 1) / ENVOIS_ATT)} ; "
          f"dans le plafond = {dollars((plafond_lectures + plafond_essai) * (ENVOIS_PESS - 1) / ENVOIS_PESS)} ; "
          f"reprises de la carte dans le plafond = {dollars(carte_plafond - total_att_haut)}")
    print(f"plafond à une fois et demie l'attendu au centre, hors ancre = {dollars(1.5 * centre)}")
    actions = (ep_a + ep_b + ep_c) * A_PAS
    print(f"juge d'une autre lignée, pour mémoire, au prorata de {actions} actions sur 6 400 : "
          f"{dollars(6.4 * actions / 6400, 1)} à {dollars(18.1 * actions / 6400, 1)}")
    provision = N_TACHES * (K_MAX + KP_MAX) * (1500 * PRIX['opus'][0] + 400 * PRIX['opus'][1]) * ENVOIS_PESS / 1e6
    print(f"provision indicative, préparation des références ({N_TACHES * (K_MAX + KP_MAX)} appels courts d'Opus 5.5, 1 500 jetons d'entrée et 400 de sortie, S) : {dollars(provision)}")
    print(f"marges par ligne (plafond moins attendu au centre) : carte {dollars(carte_plafond - carte_att_centre)} ; "
          f"lectures {dollars(plafond_lectures - lect_centre)} ; essai {dollars(plafond_essai - essai_att)} ; ancre par Neon {dollars(ancre_plafond - ancre_att)}")
    entree_essai = 2 * (18 * 950 + 6 * 3650)     # M : deux réglages d'Opus 5.5, entrées supposées du devis de l'essai (ligne 144)
    sortie_moy = (0.602 - entree_essai * PRIX["opus"][0] / 1e6) / (PRIX["opus"][1] / 1e6) / 48   # M : registres/depenses.md:546
    print(f"sortie moyenne d'Opus 5.5 à l'essai du bras A, sur entrées supposées : {sortie_moy:.0f} jetons par lecture")
    print(f"point d'accès global de Mistral : {dollars(100 * (1 - 1 / 1.1), 1)} % de moins sur la part de Mistral")

    print("\n== 11. Effort du lecteur Claude : Opus 5.5, une question par appel ==")
    for nom, sortie in SORTIE_EFFORT:
        c = cout_question("opus", True, sortie=sortie)
        print(f"effort {nom:5s} : sortie supposée {sortie} jetons ; {dollars(c, 4)} par question ; part de Claude attendue, essai compris : "
              f"{dollars(q_tot_centre * c)} à k = k' = {K_CENTRE}, {dollars(q_tot_max * c)} à k = k' = {K_MAX} ; "
              f"surcoût sur l'effort bas au centre, lectures seules : {dollars((c - q_opus_att) * q_lect_centre)}")
    c_max_att = cout_question("opus", True, sortie=SORTIE_MAX_CLAUDE)
    c_max_pess = cout_question("opus", False, sortie=SORTIE_MAX_CLAUDE)
    print(f"borne, si chaque réponse atteignait la sortie maximale du corps ({SORTIE_MAX_CLAUDE} jetons) : {dollars(c_max_att, 4)} par question "
          f"aux entrées attendues, {dollars(c_max_pess, 4)} au pire ; part de Claude, essai compris : {dollars(q_tot_centre * c_max_att)} à k = k' = {K_CENTRE} ; "
          f"à k = k' = {K_MAX}, {dollars(q_tot_max * c_max_att)} à {dollars(q_tot_max * c_max_pess)} ; plafond de la part de Claude : {plafond_entier(somme_opus)} ; "
          f"rapport de ce plafond à la part attendue à l'effort haut, à k = k' = {K_MAX} : {dollars(somme_opus / (q_tot_max * c_haut), 2)}")
    couvre_att = (q_opus_pess / ENVOIS_ATT * 1e6 - ENTREE_ATT * PRIX["opus"][0]) / PRIX["opus"][1]
    print(f"sortie moyenne par question que le plafond de dépense de la file d'Opus couvre : {SORTIE_PESS['opus']} jetons si les entrées et les reprises "
          f"sont au pire ; {couvre_att:.0f} jetons si elles sont à l'attendu")
    file_essai_opus, _, file_essai_mistral_eng = files_p["essai"]
    plafond_essai_2 = plafond_entier(2 * file_essai_opus + file_essai_mistral_eng)
    print(f"option : l'essai mesure deux réglages du lecteur Claude (une seconde file d'Opus 5.5 de même plafond, {dollars(file_essai_opus)}) : "
          f"plafond de l'essai {plafond_essai_2} au lieu de {plafond_essai} ; plafond total, hors ancre, {plafond_total + plafond_essai_2 - plafond_essai:.0f} ; "
          f"attendu de l'essai au centre : {dollars(essai_att + q_essai_centre * cout_question('opus', True, sortie=1000))} (bas et moyen), "
          f"{dollars(essai_att + q_essai_centre * c_haut)} (bas et haut)")

    print("\n== 12. Second lecteur de rechange, pour information : ordres de grandeur sur une sortie supposée, aucun plafond proposé ==")
    print(f"pire cas d'un envoi de Gemini 4 Neon sous la règle des appels aux modèles de Google : {dollars(envoi_neon_pire, 4)} dollar "
          f"({dollars(envoi_neon_pire / envoi_opus, 1)} fois celui d'Opus 5.5, {dollars(envoi_neon_pire / envoi_mistral, 1)} fois celui de Mistral au prix de repli) ; "
          f"un lecteur envoie {q_tot_max} questions à k = k' = {K_MAX}, essai compris : borne du corps de sa part, sans reprise, {dollars(q_tot_max * envoi_neon_pire)}")
    part_claude_centre, part_mistral_centre = q_tot_centre * q_opus_att, q_tot_centre * q_mistral_att
    part_neon_centre = q_tot_centre * appel_neon_att
    print(f"une question par appel, au centre (k = k' = {K_CENTRE}, {q_tot_centre} questions par lecteur, essai compris) : part de Claude {dollars(part_claude_centre)} ; "
          f"part du second lecteur : Mistral {dollars(part_mistral_centre)} ; Neon, à {SORTIE_ATT_NEON} jetons de sortie par appel (S), {dollars(appel_neon_att, 4)} par question, "
          f"soit {dollars(part_neon_centre)} ; total attendu au centre, hors ancre : {dollars(carte_att_centre + part_claude_centre + part_mistral_centre)} avec Mistral, "
          f"{dollars(carte_att_centre + part_claude_centre + part_neon_centre)} avec Neon")
    appels_centre = n_appels_groupe
    neon_groupe = ((ENTREE_ATT + GROUPE_ENTREE_PAR_QUESTION * K_CENTRE) * PRIX["neon"][0]
                   + (SORTIE_ATT_NEON + GROUPE_SORTIE_PAR_QUESTION * K_CENTRE) * PRIX["neon"][1]) * ENVOIS_ATT / 1e6
    g_claude = appels_centre * cout_ensemble_groupe("opus", K_CENTRE)
    g_mistral = appels_centre * cout_ensemble_groupe("mistral", K_CENTRE)
    g_neon = appels_centre * neon_groupe
    print(f"lecture groupée, au centre ({appels_centre} appels par lecteur, essai compris) : part de Claude {dollars(g_claude)} ; Mistral {dollars(g_mistral)} ; "
          f"Neon, à {SORTIE_ATT_NEON} jetons de réflexion et de texte par appel plus {GROUPE_SORTIE_PAR_QUESTION} par question (S), {dollars(neon_groupe, 4)} par appel, "
          f"soit {dollars(g_neon)} ; total attendu au centre, hors ancre : {dollars(carte_att_centre + g_claude + g_mistral)} avec Mistral, "
          f"{dollars(carte_att_centre + g_claude + g_neon)} avec Neon")
    envois_essai_neon = math.ceil(q_essai_max * ENVOIS_PESS)
    envois_essai_neon_groupe = math.ceil((ENSEMBLES_ESSAI + ENSEMBLES_ESSAI_D3) * ENVOIS_PESS)
    print(f"essai de mesure de Neon, borné par le corps, marge de change comprise : une question par appel, {envois_essai_neon} envois au plus, "
          f"{dollars(envois_essai_neon * envoi_neon_pire * (1 + MARGE_CHANGE))}, plafond {plafond_entier(envois_essai_neon * envoi_neon_pire * (1 + MARGE_CHANGE))} ; "
          f"lecture groupée, {envois_essai_neon_groupe} envois au plus, {dollars(envois_essai_neon_groupe * envoi_neon_pire * (1 + MARGE_CHANGE))}, "
          f"plafond {plafond_entier(envois_essai_neon_groupe * envoi_neon_pire * (1 + MARGE_CHANGE))}")
    print("pour mémoire, le devis v2 chiffrait un repli « Neon et Mistral » à 548, sur 320 ensembles et des sorties de 1 500 et 6 000 jetons, "
          "sans la règle des appels aux modèles de Google : chiffre retiré")

    print("\n== 13. Constantes supposées, rappelées ==")
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
    print(f"k' pris égal à k (centre {KP_CENTRE}, plafond {KP_MAX}) ; poste D2 compté à {RELECTURES_EPREUVES} ensembles (« au moins ») ; "
          f"questions des postes D2 et D3 supposées du prix d'une question du poste D1 ; essai : {ENSEMBLES_ESSAI} ensembles (forme D1) et "
          f"{ENSEMBLES_ESSAI_D3} (forme D3) ; marge de lancement {100 * MARGE_LANCEMENT:.0f} % ; sortie attendue de Neon {SORTIE_ATT_NEON} jetons par appel ; "
          f"lectures d'admission de l'agent de l'ancre : {ADMISSION_JUGE}")

    print("\n== 14. Ce que la pièce 6 version 2 change au devis v2 ==")
    v_v1 = volumes(N_TACHES * E, N_F * E, relectures=RELECTURES_EPREUVES_V1)
    ens_v2 = v_v1["d1_1"] + v_v1["d1_2"] + v_v1["d2"]
    print(f"ensembles lus par lecteur : {ens_v2} (devis v2) -> {ens_tot} ; relectures des épreuves {RELECTURES_EPREUVES_V1} -> {RELECTURES_EPREUVES} "
          f"(+{RELECTURES_EPREUVES - RELECTURES_EPREUVES_V1} ensembles x k) ; oracles rapportés à côté 0 -> {ens_d3} (ensembles x k') ; "
          f"essai +{ENSEMBLES_ESSAI_D3} ensembles x k' ; ancre : une personne -> un agent, {ELEMENTS_ANCRE} questions")
    d2_att = (RELECTURES_EPREUVES - RELECTURES_EPREUVES_V1) * K_CENTRE * att
    d3_att = ens_d3 * KP_CENTRE * att
    es_att = ENSEMBLES_ESSAI_D3 * KP_CENTRE * att
    print(f"attendu au centre, hors ancre : {dollars(V2_ATTENDU_CENTRE)} -> {dollars(centre)} (+{dollars(centre - V2_ATTENDU_CENTRE)}) : relectures "
          f"+{dollars(d2_att)} ; oracles rapportés à côté +{dollars(d3_att)} ; essai +{dollars(es_att)} ; somme +{dollars(d2_att + d3_att + es_att)}")
    d2_p = (RELECTURES_EPREUVES - RELECTURES_EPREUVES_V1) * K_MAX * prix_question_engagement
    d3_p = ens_d3 * KP_MAX * prix_question_engagement
    es_p = ENSEMBLES_ESSAI_D3 * KP_MAX * prix_question_engagement
    print(f"plafond pessimiste, hors ancre : {V2_PLAFOND} -> {plafond_total:.0f} (+{plafond_total - V2_PLAFOND:.0f}) : relectures +{dollars(d2_p)} ; "
          f"oracles rapportés à côté +{dollars(d3_p)} ; essai +{dollars(es_p)} ; somme +{dollars(d2_p + d3_p + es_p)}, le reste aux arrondis par file ; "
          f"ancre par Neon : 5 (option du devis v2) -> {ancre_plafond} (règle des appels aux modèles de Google)")


if __name__ == "__main__":
    main()
