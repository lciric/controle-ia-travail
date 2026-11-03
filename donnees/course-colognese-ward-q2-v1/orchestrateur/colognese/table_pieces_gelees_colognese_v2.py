#!/usr/bin/env python3
"""KIT COLOGNESE-WARD Q2 v2 (sous-agent de session-depot, 3 novembre 2026) : v1 (gardée, R12) plus deux variantes sans Opus (« sans-opus », « sans-opus-argon » : Fable 5.1 aiguilleur, juge et lecteur), après le premier run arrêté sur un refus d'Opus (C13) ; les trois configurations v1 restent inchangées ; S17 par variante (198, ou 237 pour « sans-opus-argon ») ; une ligne de GO par variante neuve.
KIT COLOGNESE-WARD Q2, v1 (sous-agent de session-depot, 3 novembre 2026) : dérivé du kit Ibrahim v2 (outils/course-ibrahim-q1-v1, 965eb21b) par substitution de noms et par les changements de la course Colognese-Ward Q2 (deux pièces servies, trois variantes comme Ibrahim, garde lexicale sans « openai », juge du n° 419, marge d'appels 2 × plan + 5).
(TABLE COLOGNESE-WARD Q2 v2, sous-agent de session-depot, 3 novembre 2026 : table_pieces_gelees_colognese_v2.py, gardée, R12, appliquée aux trois configurations Colognese-Ward Q2 q1-v2 ; gèle aussi la source Gu-Krenn v2, le lanceur shell v2, le constructeur des configurations v2, la course à blanc v2, les essais v2, le faux mandataire v2, la répétition v2 (son résultat est cité à son empreinte au § 7 de la fiche, pas dans la table, pour éviter une dépendance circulaire). Les lignes suivantes sont héritées.)
(v2 = table_pieces_gelees_colognese_v2.py, gardée, R12, appliquée aux configurations v2 ; gèle aussi le lanceur shell v2,
la répétition v2, les résultats des essais et de la répétition.)
Table « ### Pièces gelées » de la fiche de lancement de la course Colognese-Ward Q2 — v3 (sous-agent de session-depot, 3 novembre 2026) :
v2 (gardée, R12) appliquée aux configurations v2, au lanceur Python v2 et au lanceur shell v3, et qui gèle les pièces v2.

`lignes` imprime les lignes `| \\`chemin depuis la racine du dépôt\\` | \\`sha256\\` | rôle |` de tout ce que le lanceur exige
(`lancer_course_colognese_v2.exigees`) pour les TROIS configurations (une seule fiche sert la variante retenue), plus le
devis et la note de vérification de la copie ; `--verifier FICHE` contrôle qu'une fiche gèle tout cela, à l'empreinte
actuelle. Aucune écriture.

  python3 -I -B table_pieces_gelees_colognese_v2.py lignes
  python3 -I -B table_pieces_gelees_colognese_v2.py --verifier FICHE
"""

import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ICI))
sys.path.insert(0, ICI)
import lancer_course_colognese_v2 as L  # noqa: E402

CONFS = ('configuration-course-colognese-ward-q2-v1-sans-kimi.json', 'configuration-course-colognese-ward-q2-v1-avec-kimi.json', 'configuration-course-colognese-ward-q2-v1-cinq-especes.json', 'configuration-course-colognese-ward-q2-v1-sans-opus.json', 'configuration-course-colognese-ward-q2-v1-sans-opus-argon.json')
EN_PLUS = ('colognese/pieces/conv-audit/specification-course-colognese-ward-v1.md', 'colognese/devis-course-colognese-v1.txt', 'colognese/devis-course-colognese-v1.json', 'colognese/calcul_devis_course_colognese_v1.py', 'colognese/course-a-blanc-colognese-v1.txt', 'colognese/test_course_colognese_v1.py', 'colognese/mutations_colognese_v1.py', 'colognese/repetition/repetition_complete_colognese_v1.sh', 'colognese/lancer-course-colognese-v1.sh', 'colognese/lancer_course_colognese_v1.py', 'colognese/course_colognese_v1.py', 'colognese/calcul_devis_course_colognese_v2.py', 'colognese/devis-course-colognese-v2.txt', 'colognese/devis-course-colognese-v2.json', 'colognese/VERIFICATION-COPIE-orchestrateur-v56-v1.txt', 'colognese/EMPREINTES-orchestrateur-course-colognese-ward-q2-v1.txt', 'colognese/construire_consigne_proposeur_colognese_v1.py', 'colognese/pieces/conv-audit/protocole-rapport-mentors-soir-v1.md', 'colognese/pieces/conv-audit/conv-audit_2026-11-03_n419.md', 'colognese/lancer-course-colognese-v2.sh', 'colognese/course_a_blanc_colognese_v2.py', 'colognese/course-a-blanc-colognese-v2.txt', 'colognese/test_course_colognese_v2.py', 'colognese/mutations_colognese_v2.py', 'colognese/repetition/faux_mandataire_tls_colognese_v1.py', 'colognese/repetition/repetition_complete_colognese_v2.sh', 'colognese/repetition/autorite_factice_colognese_v1.sh')


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
