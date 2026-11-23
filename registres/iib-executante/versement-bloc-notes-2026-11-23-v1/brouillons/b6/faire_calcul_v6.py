#!/usr/bin/env python3
"""Fabrique calcul-devis-voie-A-v6.py depuis la v5, par remplacements exacts (chacun doit se trouver le nombre de fois attendu)."""
import pathlib
import sys

D = pathlib.Path(sys.argv[1])
src = (D / "calcul-devis-voie-A-v5.py").read_text(encoding="utf-8")


def r(vieux: str, neuf: str, n: int = 1) -> None:
    global src
    assert src.count(vieux) == n, (src.count(vieux), vieux[:90])
    src = src.replace(vieux, neuf)


r('''# Écrit par Claude Fable 5.2 (rédacteur), sur sa v4. Bibliothèque standard seule.
"""Arithmétique du devis de la voie (A) du saboteur à budget, version 5, sous la ligne GO-2026-11-22-75 — v5.

Remplace `calcul-devis-voie-A-v4.py` (intact, R12). Changements, et eux seuls (décisions de la mère du 22 novembre à 18:21Z [S13]) :
''', '''# Écrit par Claude Fable 5.2 (rédacteur), sur sa v5. Bibliothèque standard seule.
"""Arithmétique du devis de la voie (A) du saboteur à budget, version 5, sous la ligne GO-2026-11-22-75 — v6.

Remplace `calcul-devis-voie-A-v5.py` (intact, R12). Changements, et eux seuls (décision de la mère du 22 novembre à 18:42Z [S14]) :
  - borne horaire du nœud porté à Lazar après un code 7 : sous-commande `borne-du-noeud` ajoutée ; elle rend trois instants
    absolus, comptés depuis l'arrêt (24, 33 et 36 heures), et n'ordonne jamais une destruction ;
  - [M33] ajoutée.
Aucune autre ligne ne change : les 28 lignes de la sortie v5 sont rendues égales à l'octet ; `second-rempart` est inchangée.
Rappel des changements de la v5 sur la v4 (décisions de la mère du 22 novembre à 18:21Z [S13]) :
''')
r('''Aucune autre ligne ne change (à comparer à la sortie v4).
Sans argument : imprime toutes les lignes [Mnn] citées par le devis et l'additif de la voie (A), brouillons 5.
Quatre sous-commandes portent des règles écrites d'avance, jouées par l'exécutante sans rien lire d'une sortie de mesure :
''', '''Sans argument : imprime toutes les lignes [Mnn] citées par le devis et l'additif de la voie (A), brouillons 6.
Cinq sous-commandes portent des règles écrites d'avance, jouées par l'exécutante ou par la mère sans rien lire d'une sortie de mesure :
''')
r('''        instant illisible ou incohérent, nœud. Cette règle n'ordonne jamais une destruction ; le code 6 n'existe plus.
''', '''        instant illisible ou incohérent, nœud. Cette règle n'ordonne jamais une destruction ; le code 6 n'existe plus.
    borne-du-noeud ARRET_PAR_LE_REMPART_S MAINTENANT_S
        après un code 7 : la machine est gardée à l'arrêt, le nœud est porté à Lazar. Rend trois instants absolus, en secondes
        et en UTC : l'arrêt plus 33 heures (porté au nœud : réponse demandée avant lui), l'arrêt plus 24 heures (relance par
        la mère), l'arrêt plus 36 heures (passage du plafond déclaré comme dépense hors devis). Code 0 : nœud porté, attendre
        le mot de Lazar. Code 8 : 24 heures sans mot, la mère relance Lazar. Code 9 : 36 heures sans mot, déclarer la dépense
        hors devis. Code 2 : instant illisible ou incohérent. Aucun de ces codes n'ordonne une destruction : le silence de
        Lazar ne vaut jamais accord de destruction.
''')
r('''#       l'échéance plus 80 minutes ; aucune destruction sans rapatriement vérifié ; instant d'arrêt dans le futur refusé
''', '''#       l'échéance plus 80 minutes ; aucune destruction sans rapatriement vérifié ; instant d'arrêt dans le futur refusé
# [S14] décision de la mère du 22 novembre à 18:42Z (mandat du brouillon 6, b9e923fb… ; registre des nœuds de l'exécutante, étage 2,
#       GO-2026-11-22-106), selon la règle la plus étroite de la vérification du brouillon 5 (5a09da27…, section C) : le nœud du code 7
#       porte l'instant « arrêt plus 33 heures » ; relance de Lazar par la mère à l'arrêt plus 24 heures ; à l'arrêt plus 36 heures, le
#       passage du plafond est déclaré comme dépense hors devis ; le silence de Lazar ne vaut jamais accord de destruction
''')
r('''FENETRE_RAPATRIEMENT_S = 7200                       # après l'arrêt par cette règle : deux heures pour rapatrier et vérifier ; au-delà, nœud à Lazar [S13]
''', '''FENETRE_RAPATRIEMENT_S = 7200                       # après l'arrêt par cette règle : deux heures pour rapatrier et vérifier ; au-delà, nœud à Lazar [S13]
NOEUD_RELANCE_H, NOEUD_BORNE_H, NOEUD_HORS_DEVIS_H = 24, 33, 36   # [S14] heures comptées depuis l'arrêt par le second rempart
''')
r('''def usd(h: float, prix: float, telechargement: float, stockage: float) -> float:
''', '''def utc(s: int) -> str:
    return datetime.datetime.fromtimestamp(s, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def total_gardee_a_l_arret(heures: float) -> float:
    """Total de la voie, au plus, quand la machine arrêtée par le second rempart est gardée à l'arrêt depuis `heures` : [M29], (b bis)."""
    return COUPURE + (DELAI_REMPART_S + GESTE_S) / HEURE * PRIX_BORNE + heures * STOCKAGE_BORNE


def borne_du_noeud(arret_s: int, maintenant_s: int) -> tuple[int, str]:
    """Borne horaire du nœud porté à Lazar après un code 7 [S14]. Elle n'ordonne jamais une destruction."""
    if arret_s <= 0 or maintenant_s < arret_s + FENETRE_RAPATRIEMENT_S:
        return 2, ("ILLISIBLE : instant incohérent (avant l'arrêt plus deux heures, où vient le code 7, ou arrêt placé dans le futur) : "
                   "aucun geste par cette règle, message à la mère")
    relance, borne, hors = (arret_s + h * 3600 for h in (NOEUD_RELANCE_H, NOEUD_BORNE_H, NOEUD_HORS_DEVIS_H))
    instants = (f"BORNE_DU_NOEUD_UTC_S={borne} = {utc(borne)} : réponse de Lazar demandée avant cet instant, total {total_gardee_a_l_arret(NOEUD_BORNE_H):.2f} USD au plus ; "
                f"relance par la mère à {relance} = {utc(relance)}, {total_gardee_a_l_arret(NOEUD_RELANCE_H):.2f} USD au plus ; "
                f"dépense hors devis déclarée à {hors} = {utc(hors)}, {total_gardee_a_l_arret(NOEUD_HORS_DEVIS_H):.2f} USD au plus, puis {STOCKAGE_BORNE:.2f} USD par heure ; "
                f"machine gardée à l'arrêt, aucune destruction : le silence de Lazar ne vaut jamais accord de destruction ; "
                f"totaux comptés pour un arrêt à l'échéance plus {(DELAI_REMPART_S + GESTE_S) // 60} minutes au plus : le compte vrai de la voie prime")
    if maintenant_s < relance:
        return 0, "NOEUD PORTE A LAZAR : attendre son mot ; " + instants
    if maintenant_s < hors:
        return 8, f"RELANCER LAZAR, par la mère : {NOEUD_RELANCE_H} heures d'arrêt sans son mot ; destruction sur son mot exprès, ou relèvement du plafond de la ligne ; " + instants
    return 9, f"DECLARER LA DEPENSE HORS DEVIS, par la mère, à Lazar : {NOEUD_HORS_DEVIS_H} heures d'arrêt sans son mot, le plafond de {PLAFOND:g} USD va être passé ; " + instants


def usd(h: float, prix: float, telechargement: float, stockage: float) -> float:
''')
r('''    if argv:
        print(__doc__, file=sys.stderr)
        return 2
''', '''    if argv and argv[0] == "borne-du-noeud" and len(argv) == 3:
        try:
            code, texte = borne_du_noeud(int(argv[1]), int(argv[2]))
        except ValueError:
            code, texte = 2, "ILLISIBLE : instant non entier : aucun geste par cette règle, message à la mère"
        print(texte)
        return code
    if argv:
        print(__doc__, file=sys.stderr)
        return 2
''')
r('''    print("\\n".join(L))
    return 0
''', '''    A0 = E0 + seuil_s + 100
    cas_noeud = (("deux heures après l'arrêt, le code 7 vient d'être rendu (cas sain)", (A0, A0 + FENETRE_RAPATRIEMENT_S)),
                 ("une seconde avant l'arrêt plus 24 h (cas sain)", (A0, A0 + NOEUD_RELANCE_H * 3600 - 1)),
                 ("à l'arrêt plus 24 h, sans mot de Lazar", (A0, A0 + NOEUD_RELANCE_H * 3600)),
                 ("une seconde avant l'arrêt plus 36 h, sans mot de Lazar", (A0, A0 + NOEUD_HORS_DEVIS_H * 3600 - 1)),
                 ("à l'arrêt plus 36 h, sans mot de Lazar", (A0, A0 + NOEUD_HORS_DEVIS_H * 3600)),
                 ("une heure après l'arrêt, avant tout code 7 (artefact)", (A0, A0 + 3600)),
                 ("instant d'arrêt placé dans le futur (artefact)", (A0 + 200, A0 + 100)))
    t24, t33, t36 = (total_gardee_a_l_arret(x) for x in (NOEUD_RELANCE_H, NOEUD_BORNE_H, NOEUD_HORS_DEVIS_H))
    ligne(33, f"borne horaire du nœud porté à Lazar après un code 7 (machine gardée à l'arrêt, {a_l_arret:.2f} USD à l'arrêt, puis {STOCKAGE_BORNE:.2f} USD par heure, [M29] (b bis)) : "
              f"à l'arrêt plus {NOEUD_RELANCE_H} h, {t24:.2f} USD : la mère relance Lazar ; "
              f"à l'arrêt plus {NOEUD_BORNE_H} h, {t33:.2f} USD, sous le pire annoncé de {pire:.2f} USD : {'oui' if t33 <= pire else 'NON'} : instant porté au nœud ; "
              f"à l'arrêt plus {NOEUD_HORS_DEVIS_H} h, {t36:.2f} USD, sous le plafond de {PLAFOND:g} USD : {'oui' if t36 <= PLAFOND else 'NON'} : le passage du plafond, qui vient après {h_sous_plafond:.1f} h d'arrêt, "
              f"est déclaré comme dépense hors devis ; aucun de ces instants n'ordonne une destruction ; règle `borne-du-noeud`, arrêt {A0}, {len(cas_noeud)} cas : "
              + " ; ".join(f"{nom} : code {borne_du_noeud(*args)[0]}, « {borne_du_noeud(*args)[1].split(' ; ')[0]} »" for nom, args in cas_noeud)
              + f" ; instants rendus pour cet arrêt : « {borne_du_noeud(A0, A0 + FENETRE_RAPATRIEMENT_S)[1].split(' ; ', 1)[1]} »")
    print("\\n".join(L))
    return 0
''')
(D / "calcul-devis-voie-A-v6.py").write_text(src, encoding="utf-8")
