"""Une seule cellule (une lettre) du tour III.1 de l'étage III du collisionneur v2.5 : variante de
`tour_unique_etage3_v1.py` (`be609dc5…`) écrite par la lignée « session-depot » le 25 octobre 2026 (12:2x UTC, R-422),
pour poser une question distincte à un seul modèle ; seule différence : la boucle ne parcourt que la lettre donnée.
Usage : python -I -B tour_une_cellule_etage3_v1.py OUTIL DOSSIER FAITS QUESTION PLAFOND_USD LETTRE

Texte d'origine : un seul tour de l'étage III du collisionneur v2.5 (III.1, « conception », trois modèles), sur la décision de Lazar
du 25 octobre 2026, 00:05 heure de Paris, relayée par « conv-audit » (message n° 28 § 1 : « Étage III, un seul tour
(III.1) »), sous GO-2026-10-24-07. Écrit par la lignée « session-depot » le 24 octobre 2026 (23:40 UTC).

L'outil (`collisionneur_v2.py`, `213b52ef…`, non modifié) n'a pas d'option « un tour » : `etage3` enchaîne III.1, III.2
et III.3. Ce pilote appelle ses propres fonctions dans l'ordre de `lancer_etage`, pour le seul tour `E3-T1` : entrées
versées une fois et scellées (`verser_une_fois`), une cellule par lettre (`construire_prompt`, `executer_cellule` : même
préambule, mêmes règles d'intégrité, même plafond vérifié avant chaque appel, mêmes relances bornées), un refus est
définitif, aucune reformulation ; puis `ecrire_etat`. Codes : ceux de l'outil (0 fini, 2 porte fermée, 4 plafond…).
Usage : python -I -B tour_unique_etage3_v1.py OUTIL DOSSIER FAITS QUESTION PLAFOND_USD
"""
import importlib.util
import sys
from pathlib import Path


def principal(argv, appelants=None):
    if len(argv) != 6 or argv[5] not in ("A", "B", "C"):
        print(__doc__)
        return 1
    outil, dossier, faits, question, plafond = argv[0], Path(argv[1]), argv[2], argv[3], float(argv[4])
    lettres = (argv[5],)
    cv = sys.modules.get("collisionneur_v2")  # essais : module déjà chargé, appelants factices
    if cv is None:
        spec = importlib.util.spec_from_file_location("collisionneur_v2", outil)
        cv = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cv)
    appelants = appelants or cv.APPELANTS
    if dossier.exists():
        print(f"{dossier} existe déjà (R12)", file=sys.stderr)
        return cv.CODE_USAGE
    tour = "E3-T1"
    try:
        cv.verser_une_fois(dossier / "faits.md", faits, "--faits")
        cv.verser_une_fois(dossier / "question-etage3.md", question, "--question")
        cv.consigner_absences(dossier, [])
        bloquees = []
        assert set(lettres) <= set(cv.LETTRES)
        for lettre in lettres:
            cid = cv.id_cellule(tour, lettre)
            prompt, pieces = cv.construire_prompt(dossier, tour, lettre, [], set())
            if cv.executer_cellule(dossier, tour, lettre, prompt, pieces, plafond, appelants) != "OK":
                bloquees.append(cid)
        cv.ecrire_etat(dossier)
        print(f"Tour {tour} fini ; dépense {cv.depense(dossier):.2f} USD ; cellules non valides : {bloquees or 'aucune'}.")
        return cv.CODE_PORTE if bloquees else cv.CODE_FINI
    except cv.Arret as e:
        cv.ecrire_etat(dossier) if dossier.exists() else None
        print(f"ARRÊT (code {e.code}) : {e}", file=sys.stderr)
        return e.code


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
