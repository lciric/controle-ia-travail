# Duel des proposeurs — course 1 (nulle par plomberie) — preuves — v1

Versé par « session-depot » le 2026-10-28T12:05:03Z, avant passation à une instance neuve. GO-2026-10-28-01 (100 USD) ;
course du 28 octobre 07:46–07:52 UTC ; **0 USD de modèles dépensé** (R-599). Modèle servant déclaré : Fable 5.1.

## Ce que ces quatre fichiers prouvent (R-620)
- `controle-cle-proc.json` : contrôle `/proc` du processus lancé — « aucune variable de clé : cas sain ». La condition (iii)
  du GO (bac à sable à `/proc` neuf) était **tenue**.
- `repetition-simulee.log` : répétition à blanc avant la course (condition (ii), relais par fichier à lecture unique, versé).
- `course.log` : la course réelle. Les bras à modèle `M-expl` et `M-aveugle` ont dépensé **0,0** et promu **0 structure** ;
  le bras `mecanique` tournait (9 promues) ; arrêt « après 10 mondes : M-expl n'a retrouvé aucune structure ».
  **Diagnostic** : la clé n'atteignait pas les bras qui appellent les modèles — le bac à sable l'a écartée de leur
  environnement (voulu) sans que le relais par fichier la leur serve. Défaut de **relais**, pas de conditions.
- `relais-sortie.txt` : sortie du relais (contrôlée sans secret par motif avant versement).

## Non versé, perdu avec le conteneur
`course/` et `repetition-simulee/` (≈ 449 Mo, 80 706 fichiers : les mondes de l'orchestrateur) — reproductibles depuis le
code v28 (`19d2c398`, conv-audit). Rien n'y est un résultat.

## Suite (en pause à la passation)
Ne rien relancer tant que le chemin de la clé vers les bras à modèle n'est pas démontré sur une répétition simulée à zéro
dépense (message n° 104 à conv-audit, point 4).
