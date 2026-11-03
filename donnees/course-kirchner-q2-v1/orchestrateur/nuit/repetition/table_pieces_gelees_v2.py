#!/usr/bin/env python3
"""Imprime (ou insère) la table « Pièces gelées » du préenregistrement v2 de la mini-course — version 2 (pièces v2 de la
contre-lecture ; garde du dépôt gelée, CLM-08 ; `table_pieces_gelees_v1.py` inchangé, R12).

`python3 -I -B table_pieces_gelees_v1.py` imprime les lignes ; `--inserer PREREG` remplace la ligne `TABLE_DES_PIECES` (une
seule fois, avant la contre-lecture) ; `--verifier PREREG` compare la table écrite aux empreintes sur disque (code 1 si écart).
"""

import hashlib
import os
import re
import sys

DEPOT = "/home/user/controle-ia-travail"
O = "donnees/mini-course-kimi-argon-v1/orchestrateur"
PIECES = (
    (f"{O}/nuit/configuration-mini-course-kimi-argon-v2.json", "configuration figée v2 (scénario B ; commande d'Argon v2)"),
    (f"{O}/nuit/pieces/consigne-proposeur-mini-course-v1.md", "consigne figée du proposeur"),
    (f"{O}/nuit/pieces/consigne-aiguilleur-mini-course-v1.md", "consigne figée de l'aiguilleur"),
    (f"{O}/nuit/pieces/consigne-juge-mini-course-v1.md", "consigne figée des juges"),
    (f"{O}/nuit/pieces/consigne-lecteur-mini-course-v1.md", "consigne figée des lecteurs d'étiquettes"),
    (f"{O}/nuit/pieces/consigne-metteur-mini-course-v1.md", "consigne figée du metteur en fusion"),
    (f"{O}/nuit/pieces/concepts-mini-course-v1.json", "liste fermée des concepts (bras basique)"),
    (f"{O}/pole/course2_nuit_v1.py", "génération sans passe tableau, liste d'arrêt (v1)"),
    (f"{O}/pole/course2_nuit_v2.py", "adaptateur v2 : dépassement de réserve et plafonds hors noyau = arrêt"),
    (f"{O}/nuit/lancer_mini_course_v2.py", "lanceur Python v2 (gardes, moteur réel)"),
    (f"{O}/nuit/lancer-mini-course-v2.sh", "lanceur shell v2 (course sous wait, piège, relais 3 et 7 USD)"),
    (f"{O}/nuit/commande_kimi_v2.py", "commande externe de Kimi"),
    (f"{O}/nuit/commande_argon_v56_nuit_v2.py", "commande externe et relais d'Argon (v2)"),
    (f"{O}/nuit/registre_depense_cumulee_v1.py", "garde cumulée au pire cas"),
    (f"{O}/nuit/trace_agregee_mini_course_v2.py", "agrégateur v2 de la trace publique"),
    (f"{O}/nuit/chercher_cles_v1.py", "recherche des clés (valeurs lues dans l'environnement)"),
    (f"{O}/nuit/EMPREINTES-orchestrateur-v56-copie-v1.txt", "copie de l'orchestrateur v56 (archive 29b1b38c…)"),
    ("docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v3.py", "relais Kimi local"),
    ("donnees/espece-seule-v1/collisionneur_v7.py", "appeler_gemini (Argon)"),
    (".claude/hooks/garde_calcul.py", "garde du dépôt : lecture du registre des GO (CLM-08)"),
)


def sha(chemin):
    with open(os.path.join(DEPOT, chemin), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def lignes():
    return [f"| `{c}` | `{sha(c)}` | {r} |" for c, r in PIECES]


def principal(argv):
    if len(argv) == 2 and argv[0] == "--inserer":
        texte = open(argv[1], encoding="utf-8").read()
        if texte.count("TABLE_DES_PIECES") != 1:
            print("jeton TABLE_DES_PIECES absent ou multiple", file=sys.stderr)
            return 2
        with open(argv[1], "w", encoding="utf-8") as f:
            f.write(texte.replace("TABLE_DES_PIECES", "\n".join(lignes())))
        return 0
    if len(argv) == 2 and argv[0] == "--verifier":
        texte = open(argv[1], encoding="utf-8").read()
        ecrites = dict(re.findall(r"^\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|", texte, re.M))
        ecarts = [c for c, _ in PIECES if ecrites.get(c) != sha(c)]
        print("conforme" if not ecarts else "écarts : " + ", ".join(ecarts))
        return 1 if ecarts else 0
    print("\n".join(lignes()))
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
