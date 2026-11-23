#!/usr/bin/env python3
"""Fabrique calcul-devis-voie-A-v5.py depuis la v4, par remplacements exacts (chacun doit se trouver une seule fois)."""
import pathlib
import sys

D = pathlib.Path(sys.argv[1])
src = (D / "calcul-devis-voie-A-v4.py").read_text(encoding="utf-8")


def r(vieux: str, neuf: str, n: int = 1) -> None:
    global src
    assert src.count(vieux) == n, (src.count(vieux), vieux[:90])
    src = src.replace(vieux, neuf)


r('''# Écrit par Claude Fable 5.2 (rédacteur), sur la v3 d'Opus 5.5, relue. Bibliothèque standard seule.
"""Arithmétique du devis de la voie (A) du saboteur à budget, version 5, sous la ligne GO-2026-11-22-75 — v4.

Remplace `calcul-devis-voie-A-v3.py` (intact, R12). Changements, et eux seuls :
  - lignes neuves [M29] à [M32] : pire de la voie selon le rempart qui joue ; règle du second rempart ; crédit relu ; ligne de session ;
  - sous-commande neuve `second-rempart` (règle de l'exécutante à l'échéance plus 10 minutes) ;
  - `echeance` imprime le compte à trois décimales (la valeur à déclarer reste arrondie au centime supérieur), d'où [M24] et [M25] ;
  - [M05] dit que le crédit de 12,995 USD est une valeur d'origine.
Aucune autre ligne ne change (à comparer à la sortie v3).
Sans argument : imprime toutes les lignes [Mnn] citées par le devis et l'additif de la voie (A), brouillons 4.
''', '''# Écrit par Claude Fable 5.2 (rédacteur), sur sa v4. Bibliothèque standard seule.
"""Arithmétique du devis de la voie (A) du saboteur à budget, version 5, sous la ligne GO-2026-11-22-75 — v5.

Remplace `calcul-devis-voie-A-v4.py` (intact, R12). Changements, et eux seuls (décisions de la mère du 22 novembre à 18:21Z [S13]) :
  - seuil du second rempart : l'échéance plus 80 minutes (4 800 s), et non plus 10. À l'échéance, la minuterie de l'amorce consigne
    2 400 s au plus, puis tente la destruction 1 800 s au plus : avant ce seuil, une machine qui tourne peut être dans le
    fonctionnement normal de la minuterie ;
  - aucune destruction sans rapatriement vérifié : le code 6 de `second-rempart`, qui détruisait « vérifié ou non », est retiré et
    n'est plus jamais rendu ; deux heures après l'arrêt : code 7, machine gardée à l'arrêt, disque gardé, nœud à Lazar ;
  - un instant d'arrêt placé dans le futur est refusé (code 2) ; huitième cas à [M30] ;
  - [M29], [M30] et [M32] refaits ; le chemin (b bis) est ajouté à [M29].
Aucune autre ligne ne change (à comparer à la sortie v4).
Sans argument : imprime toutes les lignes [Mnn] citées par le devis et l'additif de la voie (A), brouillons 5.
''')

r('''        ETAT : « tourne », « arret » ou « absente », lu à l'inventaire en champs filtrés. Code 0 : rien à faire. Code 4 :
        arrêter la machine par son identifiant (elle tourne encore 10 minutes après son échéance : la minuterie de l'amorce a
        fait défaut). Code 5 : machine arrêtée par cette règle, rapatrier. Code 6 : la détruire par son identifiant. Code 2 :
        état ou instant illisible, nœud.
''', '''        ETAT : « tourne », « arret » ou « absente », lu à l'inventaire en champs filtrés. Code 0 : rien à faire. Code 4 :
        arrêter la machine par son identifiant (elle tourne encore 80 minutes après son échéance, au-delà des 70 minutes que
        prend au plus la minuterie de l'amorce : celle-ci a fait défaut). Code 5 : machine arrêtée par cette règle, rapatrier
        et vérifier ; destruction après rapatriement vérifié seulement. Code 7 : deux heures après l'arrêt ; sans
        rapatriement vérifié, machine gardée à l'arrêt, disque gardé, aucune destruction, nœud à Lazar. Code 2 : état ou
        instant illisible ou incohérent, nœud. Cette règle n'ordonne jamais une destruction ; le code 6 n'existe plus.
''')

r('''# [S11] mot de la mère sur le second rempart (erratum 1 du mandat du brouillon 4, 4642543b…) : destruction par l'exécutante, échéance plus 10 minutes
''', '''# [S11] mot de la mère sur le second rempart (erratum 1 du mandat du brouillon 4, 4642543b…) : destruction par l'exécutante, échéance plus 10 minutes ; remplacé par [S13]
''')

r('''# [S12] registres/go.md de main : GO-2026-11-22-94, ligne de session de l'exécutante, échéance 2026-11-25
''', '''# [S12] registres/go.md de main : GO-2026-11-22-94, ligne de session de l'exécutante, échéance 2026-11-25
# [S13] décisions de la mère du 22 novembre à 18:21Z (mandat du brouillon 5, c25267a7… ; registre des nœuds de l'exécutante, étage 2,
#       GO-2026-11-22-106), sur la vérification du brouillon 4 (b5e73a07…, majeurs M1 et M2, mineur m1) : seuil du second rempart à
#       l'échéance plus 80 minutes ; aucune destruction sans rapatriement vérifié ; instant d'arrêt dans le futur refusé
''')

r('''DELAI_REMPART_S = 600                               # [S11] l'exécutante agit à l'échéance plus 10 minutes
''', '''MARGE_SEUIL_S = 600                                 # [S13] dix minutes au-delà de la fenêtre normale de la minuterie
DELAI_REMPART_S = CONSIGNATION_S + MARGE_DESTRUCTION_S + MARGE_SEUIL_S   # [S13] 4 800 s : l'exécutante agit à l'échéance plus 80 minutes
DELAI_REMPART_V4_S = 600                            # [S11] seuil du brouillon 4, gardé pour dire d'où vient le chiffre de 59,30 USD
''')

r('''FENETRE_RAPATRIEMENT_S = 7200                       # entre l'arrêt par cette règle et la destruction : choix du rédacteur (stockage seul)
''', '''FENETRE_RAPATRIEMENT_S = 7200                       # après l'arrêt par cette règle : deux heures pour rapatrier et vérifier ; au-delà, nœud à Lazar [S13]
''')

r('''    """Règle de l'exécutante [S11]. Le lanceur ne détruit jamais une machine qui tourne : arrêt d'abord, destruction ensuite."""
    seuil = echeance_s + DELAI_REMPART_S
    if etat not in ("tourne", "arret", "absente") or echeance_s <= 0 or maintenant_s <= 0 or (arret_s is not None and arret_s < seuil):
        return 2, "ILLISIBLE : état hors de « tourne », « arret », « absente », ou instant incohérent : aucun geste par cette règle, nœud"
''', '''    """Règle de l'exécutante [S11] [S13]. Elle n'ordonne jamais une destruction : le lanceur ne détruit pas une machine qui tourne,
    et aucune machine n'est détruite sans rapatriement vérifié. Le code 6 de la v4 n'est plus jamais rendu."""
    seuil = echeance_s + DELAI_REMPART_S
    if (etat not in ("tourne", "arret", "absente") or echeance_s <= 0 or maintenant_s <= 0
            or (arret_s is not None and (arret_s < seuil or arret_s > maintenant_s))):
        return 2, ("ILLISIBLE : état hors de « tourne », « arret », « absente », ou instant incohérent (arrêt avant le seuil, ou placé dans le futur) : "
                   "aucun geste par cette règle, nœud")
''')

r('''        if maintenant_s < limite:
            return 5, f"RAPATRIER : machine arrêtée par cette règle ; destruction par l'identifiant au plus tard à {limite}"
        return 6, "DETRUIRE par l'identifiant, maintenant, rapatriement vérifié ou non (mot de la mère donné d'avance)"
    if maintenant_s < seuil:
        return 0, f"RIEN : avant l'échéance plus 10 minutes ({seuil})"
    if etat == "tourne":
        return 4, "ARRETER par l'identifiant, maintenant : la machine tourne 10 minutes après son échéance ; puis relire son état"
''', '''        if maintenant_s < limite:
            return 5, (f"RAPATRIER ET VERIFIER : machine arrêtée par cette règle ; destruction par l'identifiant après rapatriement vérifié seulement ; "
                       f"sans rapatriement vérifié à {limite} : machine gardée à l'arrêt, nœud à Lazar")
        return 7, "GARDER A L'ARRET : deux heures après l'arrêt ; sans rapatriement vérifié, disque gardé, aucune destruction, nœud à Lazar"
    if maintenant_s < seuil:
        return 0, f"RIEN : avant l'échéance plus 80 minutes ({seuil}) ; la minuterie de l'amorce a 70 minutes pour consigner puis détruire"
    if etat == "tourne":
        return 4, "ARRETER par l'identifiant, maintenant : la machine tourne 80 minutes après son échéance, la minuterie a fait défaut ; puis relire son état"
''')

r('''    amorce_seule = COUPURE + (CONSIGNATION_S + MARGE_DESTRUCTION_S) / HEURE * PRIX_BORNE
    executante = COUPURE + (DELAI_REMPART_S + GESTE_S) / HEURE * PRIX_BORNE + FENETRE_RAPATRIEMENT_S / HEURE * STOCKAGE_BORNE
    fin_normale = COUPURE + ARRET_48_H_USD
''', '''    amorce_seule = COUPURE + (CONSIGNATION_S + MARGE_DESTRUCTION_S) / HEURE * PRIX_BORNE
    marche_usd = (DELAI_REMPART_S + GESTE_S) / HEURE * PRIX_BORNE            # la machine tourne de l'échéance à l'arrêt par l'exécutante
    executante = COUPURE + marche_usd + FENETRE_RAPATRIEMENT_S / HEURE * STOCKAGE_BORNE
    a_l_arret = COUPURE + marche_usd                                         # (b bis) total de la voie à l'instant de l'arrêt
    gardee_24, gardee_48 = a_l_arret + 24 * STOCKAGE_BORNE, a_l_arret + ARRET_48_H_USD
    h_sous_pire = math.floor((pire - a_l_arret) / STOCKAGE_BORNE * 10 + 1e-9) / 10       # arrondi par défaut, au dixième d'heure
    h_sous_plafond = math.floor((PLAFOND - a_l_arret) / STOCKAGE_BORNE * 10 + 1e-9) / 10
    gardee_48_v4 = COUPURE + (DELAI_REMPART_V4_S + GESTE_S) / HEURE * PRIX_BORNE + ARRET_48_H_USD
    fin_normale = COUPURE + ARRET_48_H_USD
''')

r('''              f"(b) la minuterie fait défaut, l'exécutante arrête à l'échéance plus 10 minutes puis détruit : {COUPURE:g} + ({DELAI_REMPART_S} + {GESTE_S}) s × {PRIX_BORNE:.2f} + {FENETRE_RAPATRIEMENT_S / HEURE:g} h × {STOCKAGE_BORNE:.2f} = {executante:.2f} USD ; "
              f"(c) fin normale à la coupure, puis 48 h d'arrêt : {COUPURE:g} + {ARRET_48_H_USD:.2f} = {fin_normale:.2f} USD ; "
              f"le plus grand des trois, {tenu:.2f} USD, est sous le pire annoncé de {pire:.2f} USD [M14] : {'oui' if tenu <= pire else 'NON'} ; "
''', '''              f"(b) la minuterie fait défaut, l'exécutante arrête à l'échéance plus {DELAI_REMPART_S // 60} minutes, le rapatriement est vérifié en {FENETRE_RAPATRIEMENT_S / HEURE:g} h au plus, puis elle détruit : "
              f"{COUPURE:g} + ({DELAI_REMPART_S} + {GESTE_S}) s × {PRIX_BORNE:.2f} + {FENETRE_RAPATRIEMENT_S / HEURE:g} h × {STOCKAGE_BORNE:.2f} = {executante:.2f} USD ; "
              f"(b bis) même chemin, rapatriement non vérifié à {FENETRE_RAPATRIEMENT_S / HEURE:g} h : machine gardée à l'arrêt, aucune destruction, nœud à Lazar : "
              f"{COUPURE:g} + {marche_usd:.2f} = {a_l_arret:.2f} USD à l'arrêt, puis {STOCKAGE_BORNE:.2f} USD par heure : {gardee_24:.2f} USD à 24 h, {gardee_48:.2f} USD à 48 h ; "
              f"sous le pire annoncé de {pire:.2f} USD jusqu'à {h_sous_pire:.1f} h d'arrêt, sous le plafond de {PLAFOND:g} USD jusqu'à {h_sous_plafond:.1f} h ; "
              f"à 48 h : {'sous le plafond' if gardee_48 <= PLAFOND else 'AU-DELÀ DU PLAFOND, RÉSERVE NOMMÉE'} "
              f"(au seuil de {DELAI_REMPART_V4_S // 60} minutes du brouillon 4, ce chemin donnait {gardee_48_v4:.2f} USD à 48 h : ce chiffre ne vaut plus) ; "
              f"(c) fin normale à la coupure, puis 48 h d'arrêt : {COUPURE:g} + {ARRET_48_H_USD:.2f} = {fin_normale:.2f} USD ; "
              f"le plus grand de (a), (b) et (c), {tenu:.2f} USD, est sous le pire annoncé de {pire:.2f} USD [M14] : {'oui' if tenu <= pire else 'NON'} ; "
''')

r('''    cas = (("avant le seuil, machine qui tourne (cas sain)", (E0, E0 + 599, "tourne", None)),
           ("au seuil, machine qui tourne (artefact : la minuterie a fait défaut)", (E0, E0 + 600, "tourne", None)),
           ("après le seuil, machine absente (cas sain : la minuterie a détruit)", (E0, E0 + 600, "absente", None)),
           ("après le seuil, machine à l'arrêt avant cette règle", (E0, E0 + 600, "arret", None)),
           ("arrêtée par cette règle depuis 1 h 59", (E0, E0 + 700 + 7199, "arret", E0 + 700)),
           ("arrêtée par cette règle depuis 2 h", (E0, E0 + 700 + 7200, "arret", E0 + 700)),
           ("état illisible (artefact)", (E0, E0 + 600, "running", None)))
''', '''    seuil_s = DELAI_REMPART_S
    cas = (("une seconde avant le seuil, machine qui tourne (cas sain)", (E0, E0 + seuil_s - 1, "tourne", None)),
           ("au seuil, machine qui tourne (artefact : la minuterie a fait défaut)", (E0, E0 + seuil_s, "tourne", None)),
           ("après le seuil, machine absente (cas sain : la minuterie a détruit)", (E0, E0 + seuil_s, "absente", None)),
           ("après le seuil, machine à l'arrêt avant cette règle", (E0, E0 + seuil_s, "arret", None)),
           ("arrêtée par cette règle depuis 1 h 59", (E0, E0 + seuil_s + 100 + 7199, "arret", E0 + seuil_s + 100)),
           ("arrêtée par cette règle depuis 2 h", (E0, E0 + seuil_s + 100 + 7200, "arret", E0 + seuil_s + 100)),
           ("état illisible (artefact)", (E0, E0 + seuil_s, "running", None)),
           ("instant d'arrêt placé dans le futur (artefact)", (E0, E0 + seuil_s + 100, "arret", E0 + seuil_s + 200)))
''')

r('''    ligne(30, "second rempart, règle de l'exécutante, échéance " + str(E0) + " : " + ''', '''    ligne(30, "second rempart, règle de l'exécutante, échéance " + str(E0) + ", seuil " + str(E0 + seuil_s) + ", " + str(len(cas)) + " cas : " + ''')

r('''              f"demande l'exécutante jusqu'à {reste / HEURE:.2f} h après la création : création au plus tard à ''', '''              f"demande l'exécutante jusqu'à {DELAI_REMPART_S + GESTE_S + FENETRE_RAPATRIEMENT_S} s après l'échéance ({DELAI_REMPART_S} + {GESTE_S} + {FENETRE_RAPATRIEMENT_S}), soit {reste / HEURE:.2f} h après la création : création au plus tard à ''')

(D / "calcul-devis-voie-A-v5.py").write_text(src, encoding="utf-8")
print("écrit")
