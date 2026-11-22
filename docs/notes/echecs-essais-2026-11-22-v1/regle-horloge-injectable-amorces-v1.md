# Règle : horloge injectable pour toute amorce neuve — v1

Pièce de travail (classe C). Décision de la mère du 22 novembre 2026, R-5010, sur la proposition 1 du classement `classement-echecs-essais-v1.md` (même dossier).

## Constat

175 essais des amorces de T0.6 (v2 à v12) échouent depuis le 17 novembre 2026. Ces essais figent `GO-2026-11-02-28` et `FIN_GO = 1794873600`, alors que l'amorce lit l'heure réelle par `date`. Après l'échéance, l'amorce refuse de démarrer, comme elle le doit. C'est l'essai qui vieillit, pas le code. Ces 175 essais sont inscrits dans `tests/echecs-connus-v3.txt`.

## Règle

Toute amorce, ou tout lanceur, écrit à partir du 22 novembre 2026 qui compare l'heure à une échéance, à une période de validité de GO ou à une heure de dépense épuisée suit ces points :

1. Toute lecture de l'heure passe par une seule fonction de l'amorce, par exemple `maintenant_utc_s`.
2. Cette fonction rend la valeur d'une variable `HORLOGE_UTC_S` (entier, en secondes UTC) **seulement si** `AMORCE_ESSAI_LOCAL=1`. Sinon elle lit l'horloge réelle.
3. Hors essai local, si `HORLOGE_UTC_S` est posée, l'amorce refuse de démarrer en le disant. On ne fausse jamais l'heure d'une machine payante.
4. Les essais posent `HORLOGE_UTC_S` à l'intérieur de la période qu'ils figent, et datent toutes leurs constantes (GO, échéance, dépense épuisée) par rapport à cette heure.
5. Chaque amorce a un essai sain et un essai d'artefact de la règle (R5) :
   - avec `HORLOGE_UTC_S` sans `AMORCE_ESSAI_LOCAL`, l'amorce refuse ;
   - avec les deux variables, l'heure injectée est bien celle qui est lue.

Les amorces de T0.6 existantes ne sont pas réécrites : leur ligne est close et elles sont citées par des pièces scellées.
