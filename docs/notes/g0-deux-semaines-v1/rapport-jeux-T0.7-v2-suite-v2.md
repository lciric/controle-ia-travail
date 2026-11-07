# Rapport additif — jeux synthétiques de T0.7, suite : r30–r31 et courbe de l'aire (fille 12, Sonnet 5.5) — v2

Complète `rapport-jeux-T0.7-v2-suite-v1.md` (inchangé, R12). Écrit le 2026-11-07 (relevé `date -u`) ; branche `prep/fille-12-t07-v1`. Mêmes conditions : aucune clé, aucune location, aucune dépense, rien sous `donnees/`, `diag/`, `runs/` ; tokeniseur factice (`cfc0c143…`, non opposable) ; réserve de travail bâtie sur la projection ; jeux **non scellables, non contre-lus**. Aucune règle changée.

## 1. État exact

J-D et J-A existent pour les **32 tâches** (r00–r31). r30 et r31 : écrits chacun par un écrivain neuf (consigne `consigne-ecrivain-fille12-v1.md`, leçons des lots précédents ajoutées), pré-contrôle mécanique propre, puis script officiel : aucun défaut dur hors jetons. **J-C : toujours aucune tâche.**

## 2. Script officiel sur les 32 tâches (assemblage `--nombre-taches 32`, graine 20261105)

- Contrôles 1 à 5 et 7 à 10 : OK (comptes 10, 10 et 5 + 5 pour chaque tâche ; défauts durs de fréquence documentaire : 0).
- Contrôle 6 : **16 écarts en jetons** (> 15 %) sous le tokeniseur factice, **non opposables** ; un seul nouveau (r30 p9, avant COST 227 / 188). Aucun écart en mots ni en caractères.
- Aires du sac de mots, 32 plis : **contrôles 0,815 (réponse entière) / 0,806 (avant COST)** ; **direction 0,739 / 0,740**. Aucune n'atteint 0,90 ; aucune réserve de surface levée.
- Journal : `mesures/journal-verification-r00-r31-v1.txt`.

## 3. Courbe de l'aire selon le nombre de tâches (préfixes dans l'ordre du fichier des énoncés ; même assemblage, même graine ; régression sans tirage)

| tâches | contrôles, entière | contrôles, avant COST | direction, entière | direction, avant COST |
|---|---|---|---|---|
| 8 | 0,745 | 0,805 | 0,660 | 0,600 |
| 16 | 0,753 | 0,738 | 0,752 | 0,782 |
| 24 | 0,797 | 0,793 | 0,727 | 0,767 |
| 32 | 0,815 | 0,806 | 0,739 | 0,740 |

Lecture (sans décision, qui revient à la mère) : le mode « contrôles » sur la réponse entière monte de façon continue (+0,07 de 8 à 32 tâches) ; avant COST il remonte après un creux à 16 ; le mode « direction » reste plat autour de 0,74 depuis 16 tâches. Les valeurs du préfixe 8, 16, 24 coïncident avec les lancements d'étape (0,745 ; 0,753 ; 0,797). Fichier : `mesures/courbe-aire-selon-nombre-de-taches-v1.json`, outil `outils/courbe_aire_v1.py` (importe la fonction du script officiel sans la modifier). Réserve : l'aire par préfixe dépend de l'ordre des tâches et du tokeniseur n'y entre pas ; chaque pli lit 20 documents.

## 4. Reste

J-C (640 séquences) ; tokeniseur conforme, réserve et évaluation scellées, textes de P3 et de T0.6 pour le contrôle 9 ; contre-vérification à l'aveugle ; scellement.
