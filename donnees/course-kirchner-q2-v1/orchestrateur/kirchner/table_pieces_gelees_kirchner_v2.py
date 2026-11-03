#!/usr/bin/env python3
"""(v2 = table_pieces_gelees_kirchner_v1.py, gardée, R12, appliquée aux configurations v2 ; gèle aussi le lanceur shell v2,
la répétition v2, les résultats des essais et de la répétition.)
Table « ### Pièces gelées » de la fiche de lancement de la course Kirchner Q2 — v3 (sous-agent de session-depot, 3 novembre 2026) :
(Kit Kirchner Q2, v1, dérivé à l'octet près des substitutions de nom du kit Heimersheim — branche outils/course-heimersheim-v1 — par un sous-agent de session-depot, 3 novembre 2026 ; les mentions de versions antérieures ci-dessous sont celles du kit Heimersheim.)
v2 (gardée, R12) appliquée aux configurations v2, au lanceur Python v2 et au lanceur shell v3, et qui gèle les pièces v2.

`lignes` imprime les lignes `| \\`chemin depuis la racine du dépôt\\` | \\`sha256\\` | rôle |` de tout ce que le lanceur exige
(`lancer_course_kirchner_v1.exigees`) pour les TROIS configurations (une seule fiche sert la variante retenue), plus le
devis et la note de vérification de la copie ; `--verifier FICHE` contrôle qu'une fiche gèle tout cela, à l'empreinte
actuelle. Aucune écriture.

  python3 -I -B table_pieces_gelees_kirchner_v2.py lignes
  python3 -I -B table_pieces_gelees_kirchner_v2.py --verifier FICHE
"""

import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ICI))
sys.path.insert(0, ICI)
import lancer_course_kirchner_v1 as L  # noqa: E402

CONFS = ("configuration-course-kirchner-q2-v2-sans-kimi.json", "configuration-course-kirchner-q2-v2-avec-kimi.json",
         "configuration-course-kirchner-q2-v2-cinq-especes.json")
EN_PLUS = ("kirchner/calcul_devis_course_kirchner_v1.py", "kirchner/devis-course-kirchner-v1.txt",
           "kirchner/devis-course-kirchner-v1.json", "kirchner/VERIFICATION-COPIE-orchestrateur-v56-v1.txt",
           "kirchner/EMPREINTES-orchestrateur-course-kirchner-q2-v1.txt",
           "kirchner/construire_consigne_proposeur_kirchner_v1.py",
           "kirchner/pieces/conv-audit/specification-kirchner-q2-v1.md",
           "kirchner/pieces/conv-audit/protocole-rapport-idees-kirchner-v1.md", "kirchner/lancer-course-kirchner-v2.sh",
           "kirchner/repetition/repetition_complete_kirchner_v2.sh", "kirchner/construire_configurations_kirchner_v2.py",
           "kirchner/course-a-blanc-kirchner-v2.txt", "kirchner/resultat-mutations-kirchner-v1.txt",
           "kirchner/test_course_kirchner_v2.py",
           "kirchner/repetition/repetition_complete_kirchner_v1.sh",
           "kirchner/course-a-blanc-kirchner-v1.txt")


def role(chemin):
    for motif, r in (("configuration-", "configuration"), ("consigne-", "consigne"), ("concepts-", "liste fermée"),
                     ("source-gu-krenn", "source du substitut Gu-Krenn"), ("question-", "question servie"),
                     ("piece-etat", "pièce servie"), ("specification-", "spécification de conv-audit"),
                     ("garde_calcul", "garde du dépôt"), ("lancer", "lanceur"), ("commande", "commande"), ("relais_kimi", "relais"),
                     ("collisionneur", "relais (appel de l'interface)"), ("registre_depense", "registre cumulé"),
                     ("trace_agregee", "trace agrégée"), ("chercher_cles", "recherche des clés"), ("devis", "devis"),
                     ("EMPREINTES", "empreintes de la copie"), ("VERIFICATION", "vérification de la copie"), ("course", "génération")):
        if motif in os.path.basename(chemin):
            return r
    return "pièce"


def chemins():
    e = set()
    for nom in CONFS:
        p = os.path.join(ICI, nom)
        with open(p, encoding="utf-8") as f:
            conf = json.load(f)
        e |= L.exigees(conf, p)
    e |= {os.path.relpath(os.path.join(L.RACINE, x), L.DEPOT) for x in EN_PLUS}
    return sorted(e)


def lignes():
    sortie = []
    for c in chemins():
        p = os.path.join(L.DEPOT, c)
        if not os.path.isfile(p):
            raise SystemExit(f"pièce à geler absente : {c}")
        sortie.append(f"| `{c}` | `{L.sha256_fichier(p)}` | {role(c)} |")
    return sortie


def principal(argv):
    if argv[:1] == ["lignes"]:
        print("\n".join(lignes()))
        return 0
    if argv[:1] == ["--verifier"] and len(argv) == 2:
        with open(argv[1], encoding="utf-8") as f:
            vues = dict(L.pieces_gelees(f.read()))
        manquent = [c for c in chemins() if c not in vues]
        fausses = [c for c, s in vues.items() if not os.path.isfile(os.path.join(L.DEPOT, c))
                   or L.sha256_fichier(os.path.join(L.DEPOT, c)) != s]
        if manquent or fausses:
            print(f"NON CONFORME : manquent {manquent} ; empreintes fausses {fausses}")
            return 3
        print(f"conforme : {len(vues)} pièces gelées, toutes à leur empreinte, aucune manquante")
        return 0
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
