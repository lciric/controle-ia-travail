#!/usr/bin/env python3
"""Commande de la phase C du compte 3 : version 3 -> brouillon 1 de la version 4, par couples « ancien -> nouveau ».

Décision de la mère R-2980 : le bloc C5 remet en plus au lecteur B `diag/$R7/sondes-t07.json` et son compagnon.
Gardes : empreinte de la version 3 vérifiée ; chaque « ancien » présent une seule fois ; cible jamais écrasée (R12).
Usage, depuis la racine du dépôt :  python3 -I -B <ce fichier>
Écrit par le rédacteur de la version 4 (sous-agent neuf, modèle B), le 2026-11-16 à partir de 12:58:48Z (`date -u`).
"""
import hashlib
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI / "commande-compte-3-phase-c-v3.md"
CIBLE = ICI / "commande-compte-3-phase-c-v4-brouillon1.md"
EMPREINTE_V3 = "9d7889198238c171447a06f56f1a37beb4190572c3a9ceceb18144541c258d2e"

COUPLES = [
    # 1. titre
    ("son lecteur de verdict — v3\n", "son lecteur de verdict — v4\n"),
    # 2. puce « Version 4 » en tête des puces de version
    ("- **Version 3** : la version 2 (`commande-compte-3-phase-c-v2.md`, `fee4caaa…`, scellée, répétée 44 sur 44, gardée, R12), plus deux\n",
     "- **Version 4** : la version 3 (`commande-compte-3-phase-c-v3.md`,\n"
     "  `9d7889198238c171447a06f56f1a37beb4190572c3a9ceceb18144541c258d2e`, scellée, répétée 53 sur 53, gardée, R12), plus un seul changement :\n"
     "  le bloc C5 remet au lecteur B, en plus de ses treize fichiers, `diag/$R7/sondes-t07.json` et son compagnon, que le bloc C2 place déjà\n"
     "  dans la racine et compare à la ligne `SONDES-T07` (quatorze fichiers et leurs compagnons, plus l'extrait : 29 fichiers au bordereau).\n"
     "  Raisons (décision de la mère R-2980, registre des décisions) : le texte scellé de T0.7 renvoie le lecteur du verdict à ce fichier\n"
     "  (l. 1539 : effectifs des « paires des jeux » ; l. 2659, défaut DF-05 : le vrai motif d'un échec de T7-P6 dès l'apprentissage y est\n"
     "  écrit, « où le lecteur du verdict (R13) le lit ») et la version 3 ne le lui remettait pas ; aucun de ses noms n'est touché par les\n"
     "  filtres du bloc 1C (contrôlé par programme, `rapport-commande-phase-c-v4-v1.md`). Rien d'autre ne change : noms du bac, des fichiers\n"
     "  de marque, des branches et des marqueurs **inchangés, à dessein** (mêmes raisons qu'à la version 3) ; phase A inchangée.\n"
     "- **Version 3** : la version 2 (`commande-compte-3-phase-c-v2.md`, `fee4caaa…`, scellée, répétée 44 sur 44, gardée, R12), plus deux\n"),
    # 3. puce « Rédacteur » complétée
    ("  12:07:52Z (`date -u`), version 3 à partir de 13:04:29Z ; ni lecteur ni juge ; aucune sortie de 7a, 7b ou T0.7 ouverte.\n",
     "  12:07:52Z (`date -u`), version 3 à partir de 13:04:29Z ; ni lecteur ni juge ; aucune sortie de 7a, 7b ou T0.7 ouverte.\n"
     "  **Version 4** : un sous-agent neuf, modèle B, de la session mère `session_016QhUrtmLyFWJP6Cy7rgfXH`, le 2026-11-16 à partir de\n"
     "  12:58:48Z (`date -u`) ; ni lecteur ni juge ; aucun fichier de `diag/`, `runs/` ou `donnees/` ouvert.\n"),
    # 4. table des pièces : répétition v4 ajoutée, v3 gardée
    ("| `repetition_phase_c_jouet_v3.sh`, sortie `repetition-phase-c-jouet-sortie-v3.txt` | voir le rapport v2 | répétition de bout en bout des blocs de cette commande sur dépôts jouets, appel interrompu, poussées refusées et artefacts des gardes compris |\n",
     "| `repetition_phase_c_jouet_v4.sh`, sortie `repetition-phase-c-jouet-v4-sortie-brouillon1-v1.txt` | voir `rapport-commande-phase-c-v4-v1.md` | répétition de bout en bout des blocs de cette commande sur dépôts jouets, appel interrompu, poussées refusées et artefacts des gardes compris ; bordereau de 29 fichiers, `sondes-t07.json` et son compagnon compris |\n"
     "| `commande-compte-3-phase-c-v3.md`, `repetition_phase_c_jouet_v3.sh`, sortie `repetition-phase-c-jouet-sortie-v3.txt` | `9d788919…`, `8be57168…`, voir le rapport v2 | version 3, gardée (R12) : 53 sur 53 |\n"),
    # 5. bloc 0b-C : nom définitif de la version 4
    ("sha256sum docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-c-v3.md\n",
     "sha256sum docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-c-v4.md\n"),
    # 6. bloc C5 : la pièce ajoutée
    ('"diag/$R7/lecture-t07.json" "runs/$R7/manifeste.json"',
     '"diag/$R7/lecture-t07.json" "diag/$R7/sondes-t07.json" "runs/$R7/manifeste.json"'),
    # 7. bloc C5 : commentaire « attendu »
    ("# attendu : treize fichiers et leurs compagnons conformes, plus l'extrait (27 fichiers)",
     "# attendu : quatorze fichiers et leurs compagnons conformes, plus l'extrait (29 fichiers)"),
    # 8. bloc F-C : auto-référence de version au journal provisoire
    ("commande phase C v2 depuis", "commande phase C v4 depuis"),
    # 9. annexe d'essais
    ("- **Répétition de bout en bout** (CL3-07) : `repetition_phase_c_jouet_v3.sh`, sortie `repetition-phase-c-jouet-sortie-v3.txt` : blocs 0b-C,\n",
     "- **Répétition de bout en bout** (CL3-07) : `repetition_phase_c_jouet_v4.sh`, sortie `repetition-phase-c-jouet-v4-sortie-brouillon1-v1.txt`\n"
     "  (bordereau de 29 fichiers, `sondes-t07.json` et son compagnon compris ; version 3 : 53 sur 53, gardée) : blocs 0b-C,\n"),
]


def main() -> int:
    octets = SOURCE.read_bytes()
    h = hashlib.sha256(octets).hexdigest()
    if h != EMPREINTE_V3:
        print(f"ARRÊT : empreinte de la version 3 autre ({h})")
        return 1
    t = octets.decode("utf-8")
    for i, (ancien, nouveau) in enumerate(COUPLES, 1):
        n = t.count(ancien)
        if n != 1:
            print(f"ARRÊT : couple {i} : « ancien » présent {n} fois (une seule attendue)")
            return 1
        t = t.replace(ancien, nouveau)
    try:
        with open(CIBLE, "x", encoding="utf-8", newline="") as f:
            f.write(t)
    except FileExistsError:
        print(f"ARRÊT : {CIBLE.name} existe déjà (R12) : rien n'est écrit")
        return 1
    print(f"{len(COUPLES)} couples appliqués ; {CIBLE.name} : {hashlib.sha256(t.encode('utf-8')).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
