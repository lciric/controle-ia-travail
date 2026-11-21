# Note du développeur — code de l'organisme retenu du saboteur à budget, version 5 — dernier pas avant l'ordre (v4)

Date : 2026-11-21. Pièce d'instrument (classe B). Développeur : Claude Fable 5.2, côté saboteur. Rien poussé, aucune dépense, aucune machine, aucun appel à un loueur, aucun refus d'outil, aucune pièce interdite ouverte, aucune consigne privée lue.

## 1. Fait
1. **Les trois correctifs du distillateur** (section de configuration, distillateur, raccord ; compagnons vérifiés d'abord) appliqués par `git am` sur 38a7475f5 : **aucun conflit**. Têtes : 34418363d, 6b375751f, 66398c8f1.
2. **Commit de tête : 45f9ba7aaca27fdab8a458072f883825991dd2fb** (branche locale `prep/iib-code-v5-local`). Correctif : `correctifs-v4/0009-….patch` (4287a688…7661), à appliquer après les correctifs 0001 à 0008 puis les trois du distillateur.
3. **Liste figée des essais, version 4** : `scripts/tests-cibles-iib-v5-v4.txt`, **23 fichiers**, empreinte `342ee21d495b54cb5fd4a8ae6d7427043edb3c228cc16afd57ab4f9e3d099b68`, écrite en dur dans `scripts/amorce_instance_iib_v5.sh`. Elle porte tous les fichiers d'essais en version 5, dont trois du distillateur (section de configuration, distillateur, bout en bout sur le monde jouet), sauf deux : l'essai du tokeniseur réel et l'essai du moteur à torch du distillateur (`tests/test_iib_distillation_torch_v5.py`), qui se sautent sans leurs dépendances. **Nombre attendu : 267** (`TESTS_ATTENDUS=267` pour l'ordre ; constante de la répétition mise à jour).
4. **Erratum 2 du texte scellé et erratum 1 du devis** : la constante du nœud 7 (b') passe de 3 520 à **3 830** actions d'oracle hors tours (1 270 + 2 560 ; jusqu'à 127 épisodes distillés) dans `configuration_v5.py` ; le fichier d'entrées doit porter 3 830, toute autre valeur est refusée. La cible des tours (96) et le minimum (48) ne changent pas ; la garde « 48 à 127 » du distillateur était déjà juste. Deux essais du monde jouet suivent (plafond de tours du jouet : 105 au lieu de 106).
5. **Gabarit de configuration, version 4** : `docs/notes/barreau8-iib-v1/config-iib-organisme-retenu-v5-gabarit-v4.json` (scellé, `eb329185948ef80d37e724f73d8c210a02d72312befbf6c0fd5e489b255fc9e1`). Il ne diffère de la version 3 que par deux clés : `noeud_7` (3 830) et la section `distillation_evaluation` (constantes de la conception d'origine, vérifiées à l'égalité). `gabarit("reel", entropie, premiere_action)` la produit ; un essai compare le fichier versé au code.
6. **Première action dans la perte de distillation : `gardee`** dans le gabarit. **À confirmer par le mot de Lazar avant le scellement de la configuration** (recommandation portée à Lazar, défaut). Le code accepte `gardee` ou `exclue` ; vide, tout lancement de la course est refusé.

## 2. Essais joués (tête 45f9ba7aa, arbre non touché pendant les passages)
- Liste figée version 4 entière : **267 réussis en 6 min 55**, aucun sauté (`sortie-essais-cibles-v5-v4.txt`).
- Répétition locale entière, liste figée, dossier neuf `repetition/liste-figee-3` : **réussie, code 0** (`sortie-repetition-locale-v2.txt`) : lanceur de session version 3, amorce version 5 (267 essais), étalonnage jouet versé par lot et poussé, destruction par l'identifiant, conditions de départ et désignation (issue P, 12 tours), second passage refusé.

## 3. Lecture gardée du calendrier
« Dernière création le 2026-11-27T00:00Z » : je lis que la création d'une machine est permise **jusqu'à cet instant exclu**, donc que le dernier jour de création est le **26 novembre** ; le gabarit porte `dernier_jour_creation` 2026-11-26 et `fin_go_utc` 2026-12-01T00:00:00Z. Lecture inchangée.

## 4. Restes, un par ligne
1. **Le point d'entrée de la course n'est pas écrit** (consigne : pas maintenant). Le rapport du distillateur en donne les trois lignes ; c'est le modèle surveillé du distillateur qui doit aller au lanceur.
2. **`tests/test_iib_distillation_torch_v5.py` n'a jamais été joué** et n'est pas dans la liste figée : à jouer à part sur un poste ou une machine qui a torch avant l'ordre de la course (il ne concerne pas l'étalonnage).
3. La chaîne de documentation de `lanceur_v5.py` (ligne 21) dit encore « le distillateur du mode réel n'est pas écrit » : non corrigée, pour ne pas toucher le lanceur après la répétition ; à corriger avec le point d'entrée.
4. Non éprouvés, inchangés : mode réel (torch absent), `MondeReel`, chargement du modèle réel, moteur à torch du distillateur, règle de surveillance à 12 dollars de l'étalonnage (non écrite dans le code).
5. Les essais du monde jouet qui lisaient 3 520 lisent 3 830 ; aucune règle, aucun seuil, aucune épreuve n'a changé.
