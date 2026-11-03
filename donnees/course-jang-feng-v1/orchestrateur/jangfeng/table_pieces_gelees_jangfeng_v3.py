#!/usr/bin/env python3
"""KIT JANGFENG v3 (sous-agent de session-depot, 3 novembre 2026) : v2 (gardée, R12) plus la variante « sans-claude » (proposeurs Argon, Kimi, Astra ; aiguilleur Astra ; juges Astra et Argon ; lecteurs Astra et Argon ; metteur Astra ; aucun rôle Claude ; relais 8806 non démarré, contrôle de Claude non joué) ; S17 propre à cette variante ; les configurations existantes ne sont ni réécrites ni changées.
KIT JANG-FENG v2 (sous-agent de session-depot, 3 novembre 2026) : v1 (gardée, R12) plus deux variantes sans Opus (« sans-opus », « sans-opus-argon » : Fable 5.1 aiguilleur, juge et lecteur), contre-lecture CLJ-01 ; les trois configurations v1 restent inchangées ; S17 par variante (198, ou 237 pour « sans-opus-argon »).
KIT JANG-FENG, v1 (sous-agent de session-depot, 3 novembre 2026) : dérivé du kit Ibrahim v2 (outils/course-ibrahim-q1-v1, 965eb21b) par substitution de noms et par les changements de la course Jang-Feng (question à une section servie et ses règles d'intégrité, deux pièces servies, trois variantes comme Ibrahim, juge du n° 419, marge d'appels 2 × plan + 5).
(TABLE JANG-FENG v2, sous-agent de session-depot, 3 novembre 2026 : table_pieces_gelees_jangfeng_v3.py, gardée, R12, appliquée aux trois configurations Jang-Feng q1-v2 ; gèle aussi la source Gu-Krenn v2, le lanceur shell v2, le constructeur des configurations v2, la course à blanc v2, les essais v2, le faux mandataire v2, la répétition v2 (son résultat est cité à son empreinte au § 7 de la fiche, pas dans la table, pour éviter une dépendance circulaire). Les lignes suivantes sont héritées.)
(v2 = table_pieces_gelees_jangfeng_v3.py, gardée, R12, appliquée aux configurations v2 ; gèle aussi le lanceur shell v2,
la répétition v2, les résultats des essais et de la répétition.)
Table « ### Pièces gelées » de la fiche de lancement de la course Jang-Feng — v3 (sous-agent de session-depot, 3 novembre 2026) :
v2 (gardée, R12) appliquée aux configurations v2, au lanceur Python v2 et au lanceur shell v3, et qui gèle les pièces v2.

`lignes` imprime les lignes `| \\`chemin depuis la racine du dépôt\\` | \\`sha256\\` | rôle |` de tout ce que le lanceur exige
(`lancer_course_jangfeng_v3.exigees`) pour les TROIS configurations (une seule fiche sert la variante retenue), plus le
devis et la note de vérification de la copie ; `--verifier FICHE` contrôle qu'une fiche gèle tout cela, à l'empreinte
actuelle. Aucune écriture.

  python3 -I -B table_pieces_gelees_jangfeng_v3.py lignes
  python3 -I -B table_pieces_gelees_jangfeng_v3.py --verifier FICHE
"""

import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ICI))
sys.path.insert(0, ICI)
import lancer_course_jangfeng_v3 as L  # noqa: E402

CONFS = ('configuration-course-jang-feng-v1-sans-kimi.json', 'configuration-course-jang-feng-v1-avec-kimi.json', 'configuration-course-jang-feng-v1-cinq-especes.json', 'configuration-course-jang-feng-v1-sans-opus.json', 'configuration-course-jang-feng-v1-sans-opus-argon.json', 'configuration-course-jang-feng-v1-sans-claude.json')
EN_PLUS = ('jangfeng/calcul_devis_course_jangfeng_v2.py', 'jangfeng/devis-course-jangfeng-v2.txt', 'jangfeng/devis-course-jangfeng-v2.json', 'jangfeng/course_jangfeng_v2.py', 'jangfeng/lancer_course_jangfeng_v2.py', 'jangfeng/lancer-course-jangfeng-v2.sh', 'jangfeng/test_course_jangfeng_v2.py', 'jangfeng/mutations_jangfeng_v2.py', 'jangfeng/course-a-blanc-jangfeng-v2.txt', 'jangfeng/repetition/repetition_complete_jangfeng_v2.sh', 'jangfeng/devis-course-jangfeng-v1.txt', 'jangfeng/devis-course-jangfeng-v1.json', 'jangfeng/calcul_devis_course_jangfeng_v1.py', 'jangfeng/course-a-blanc-jangfeng-v1.txt', 'jangfeng/test_course_jangfeng_v1.py', 'jangfeng/mutations_jangfeng_v1.py', 'jangfeng/repetition/repetition_complete_jangfeng_v1.sh', 'jangfeng/lancer-course-jangfeng-v1.sh', 'jangfeng/lancer_course_jangfeng_v1.py', 'jangfeng/course_jangfeng_v1.py', 'jangfeng/calcul_devis_course_jangfeng_v3.py', 'jangfeng/devis-course-jangfeng-v3.txt', 'jangfeng/devis-course-jangfeng-v3.json', 'jangfeng/VERIFICATION-COPIE-orchestrateur-v56-v1.txt', 'jangfeng/EMPREINTES-orchestrateur-course-jang-feng-v1.txt', 'jangfeng/construire_consigne_proposeur_jangfeng_v1.py', 'jangfeng/pieces/conv-audit/protocole-rapport-mentors-soir-v1.md', 'jangfeng/pieces/conv-audit/conv-audit_2026-11-03_n419.md', 'jangfeng/lancer-course-jangfeng-v3.sh', 'jangfeng/course_a_blanc_jangfeng_v3.py', 'jangfeng/course-a-blanc-jangfeng-v3.txt', 'jangfeng/test_course_jangfeng_v3.py', 'jangfeng/mutations_jangfeng_v3.py', 'jangfeng/repetition/faux_mandataire_tls_jangfeng_v1.py', 'jangfeng/repetition/repetition_complete_jangfeng_v3.sh', 'jangfeng/repetition/autorite_factice_jangfeng_v1.sh')


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
