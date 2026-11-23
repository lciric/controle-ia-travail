# Vérification de la garde de l'instance (360979d1)

Lu : diff 01fe0ea5..360979d1 (entrees_v1, test_t08_entrees_rendu_v1) ; aucun écart src/tests jusqu'à HEAD. Rejoué : `-k amorce` : 4 passés. Mutation A29 non rejouée. Mêmes interdits respectés.

- CA-10 vérifié : `-z` sur `git log`, `core.quotePath=false` sur `rev-list` ; le test neuf (chemin non ASCII avec espace, blob dédoublé nommé par `a/autre.json`) est probant.
- CA-11 vérifié : sorties lues en octets, décodées en `surrogateescape`, erreurs d'`stderr` en `replace`.

**CA-13 — à corriger (léger)** — `entrees_v1.py`, ligne `set(r.stdout.decode(...).replace("\n", "\0").split("\0"))`. Remplacer les sauts de ligne par NUL coupe un chemin qui contient un saut de ligne. Vérifié sur un dépôt d'essai : `diag/<run>/d\nx/resume.json` (blob dédoublé, retiré du disque) donne `interdits: 0` : la garde ne l'attrape pas. Cas tordu mais de même nature que CA-10. Correction : ne pas remplacer ; découper sur NUL seulement et retirer un éventuel saut de ligne initial de chaque entrée (séparateur de commits), `l.lstrip("\n")` ; ajouter l'essai (dossier avec saut de ligne, blob dédoublé) et une mutation.

## Verdict : CA-10 et CA-11 vérifiés ; **conforme après correction de CA-13** (petite). CA-12 reste au rapport.
