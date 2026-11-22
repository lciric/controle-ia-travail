# Collisionneur v9-v8f : rapport du développeur

Écrit à 2026-11-22T07:56:31Z (`date -u`). Classe B, Opus 5.5, session des collisionneurs. Aucun réseau, aucune clé, aucune course ; **aucune course sur la v8e ni la v8f avant le feu de la mère**.

- `collisionneur_v9_v8f.py` (445fe2d3…), copie de la v8e (0d591933…, intacte, R12) par `fabriquer_v8f_depuis_v8e_v1.py` ; essais `test_collisionneur_v9_v8f.py` : 356 passés, 3 sautés.
- Contre-lecture de la v8e par un Opus neuf : `verification-collisionneur-v9-v8e-opus-v1.md` (à corriger, deux bloquants ; texte de Fable, places, refus sans place, lecture de la place : tiennent ; six mutations prises).

## Corrections
- **B1** : seuls les essais de l'étage III (« E3- ») font refuser un dossier sans `consignes-etage3.json` ; un dossier ouvert sous ce script aux étages I et II passe à l'étage III. Conséquence à savoir : un dossier dont les étages I et II viennent d'un script plus ancien est désormais accepté à l'étage III (avec `--reprise` déclarée) : l'étage III, lui, est tout entier balisé.
- **B2** : le refus est contrôlé dans `principal`, juste après la place, avant tout versement (faits, question, composition) ; un dossier refusé ne reçoit aucun fichier neuf (`etat.md`, dérivé, reste réécrit par l'`except` de la v8d).
- **Non-bloquant porté** : `verifier` signale, pour les essais des tours III.1 et III.3 faits sous ce script, un `consignes-etage3.json` absent et une invite qui ne contient pas la consigne scellée de son tour.
- **Non-bloquant porté** : dix essais sautés (deux fonctions paramétrées, copies des runs à reprendre), faux par construction sous la v8e : retirés comme les six autres (`retire_v8f_…`).
- Mutations : B1, B2 et le contrôle de `verifier` retirés, chacune prise par son essai.

## Non portés
- Essais de la ligne de reprise par `principal` (`--go-ligne`), de la croissance du pire cas et de l'issue « Plafond retenu : None » sur un dossier de la v8f : fonctions inchangées depuis la v8d, couvertes là.
- `--place-iii3` au `devis` : de forme seulement (le devis ne construit aucune consigne).

Points ouverts pour Fable : ceux du rapport de la v8e, inchangés.
