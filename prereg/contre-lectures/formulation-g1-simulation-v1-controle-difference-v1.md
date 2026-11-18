# Contrôle de la différence entre le brouillon 3 et le texte candidat — étude par simulation des formulations du contraste à témoin apparié de la porte de fin de phase 1

- Contrôleur : sous-agent neuf de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, Claude Sonnet 5.5 (`claude-sonnet-5-5`) ; il n'a écrit ni le brouillon, ni le candidat, ni le programme, ni la vérification 1 de la même session.
- Date (UTC) : 18 novembre 2026.
- Empreintes recalculées, égales à celles du mandat : brouillon 3 `d20d605c…` ; candidat `prereg/formulation-g1-simulation-v1.md` `d04da7903b89d0835ce16a77d5338e5a11ada20908f7c13dd65fd61191a08a87` ; vérification 1 `958707bd…` ; liste des différences `2f39ae5a…` ; programme `f05bb378…`.

## Verdict : à sceller tel quel

(Une remarque non bloquante au point 3.)

## 1. Rejeu du programme

Copie du seul brouillon 3 dans un dossier du bac à sable, `.venv/bin/python -B <programme> <dossier> 7f73ec743` : 23 remplacements (chaque « avant » trouvé une fois), fichier produit **identique à l'octet** au candidat (`cmp`), même empreinte `d04da790…`. Rien écrit dans le dépôt (`git status` propre). `7f73ec743` est un ancêtre de la tête actuelle `0d71e3d6a` ; le texte dit « tête à l'écriture », ce qui reste exact.

## 2. Les 12 hunks de `diff -u` (brouillon 3 vers candidat)

| hunk (lignes du brouillon) | rattachement |
|---|---|
| 1-3, 5-8 : titre, statut, auteur, date, brouillons repris, commit | statut de version ; empreinte du brouillon 3 et de la liste 2→3 (déjà connues) ; commit : tête `7f73ec743` |
| 22 : essais « rejoués par le vérificateur vers 22:45 » | fait écrit dans la vérification 1 ; statut de version |
| 44 : « Budgets d'épisodes du témoin » | C3 (premier passage), mot pour mot |
| 54 : « Deux réserves sur δ » | hors couple (§ 9 de la vérification, deux puces : δ à 50 tâches et unités de trois épisodes) |
| 151 : « Ordre » | C4 (première moitié) ; « ce texte scellé par la session mère » : statut de version |
| 174 : « B à 300 » devient « B sur 300 » | hors couple (§ 9, première puce) ; plus aucune occurrence de « B à 300 » |
| 182 : sixième rejeu | C3 (second passage), mot pour mot |
| 192 : limite sur la composante B sans la garde | hors couple (§ 4 point 1, remarque) |
| 196 : « Décision » | C1, mot pour mot |
| 212, 228 : « sceller ce texte », « de ce texte » | statut de version |
| 272 : point 8 | C2, mot pour mot |
| 277 : borne 18 et bornes « ≥ 19 » | hors couple (§ 5, remarque) |
| 280 : « relus par la vérification 1… » | statut de version (C4, mention de la vérification) |
| 323-340 : remplacement de « À venir », puis table de traitement | C4 (seconde moitié, avec l'empreinte du rapport en plus, déclarée) ; la table et le paragraphe final consignent le traitement de C1 à C4 et des points hors couple |

Aucun hunk sans rattachement. Aucune ligne de chiffre, de seuil, de règle, de prédiction ou de critère n'est touchée.

## 3. C1 à C4 et ajouts hors couple

- C1, C2, C3 (deux passages), C4 (« Ordre » avec `lecture_v3.indicateurs(…)`, entrée « Vérification 1 du brouillon 3 ») : textes de la vérification repris tels quels ; seules les « … » des couples sont remplies par le texte du brouillon, sans changement. Écart déclaré : l'empreinte du rapport est écrite en plus, ce qui est neutre (c'est `958707bd…`, vraie).
- Hors couple : tous du texte, sans toucher au code, et tous dans le sens de la prudence (réserves, limites, unification d'une graphie). Aucun ne penche vers A ou vers B/C : la limite sur la composante B sans la garde est un aveu symétrique, que la vérification a elle-même relevé.
- Remarque non bloquante : au point 277, « écrites avant de le jouer et jamais retouchées » est une affirmation d'historique que la vérification 1 n'a pas émise (elle dit seulement « de même nature ») et que je ne peux pas établir par l'historique du dépôt (fichiers d'essais versés en bloc). Elle repose sur le témoignage du rédacteur. Ne penche vers aucune formulation ; la session mère peut la garder ou la retirer, au risque de l'écart.

## 4. `prereg.problemes`

`PYTHONPATH=src .venv/bin/python -B -c "…prereg.problemes('prereg/formulation-g1-simulation-v1.md')"` rend `[]`.

## Limites

Je n'ai relu ni le code ni les essais ; je n'ai rien ouvert sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `registres/`. Ni commit ni poussée ; candidat non modifié ; seuls fichiers écrits : ce rapport et son compagnon, et un dossier de rejeu dans le bac à sable.
