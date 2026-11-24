# Passation — session fille développeuse du code de la course de dose–réponse de l'organisme à consigne cachée — 2026-11-24 13:38 UTC

Session fille de la mère `session_01Qi7Gr3Ggccg85kjmP654WC` ; modèle Opus 5.5, effort élevé. Branche `code/dose-reponse-consigne-cachee-v1` (demande de fusion en brouillon n° 106). Mandat : `docs/notes/conception-g0-criteres-2-3-v1/mandat-developpeur-code-course-dose-reponse-v1.md` (b8d2f5fc…).

## Fait

- Code de la course et de sa lecture hors ligne pour le texte scellé `prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md` (2263c5c4…) : paquet `src/controle_ia/dose_reponse/` (conditions_v1 ; controles, course, lecture en v1 puis v2), amorce, lanceur et écriture de la configuration (v1 puis v2), essais (`tests/test_dose_reponse_v2.py`, 45 verts).
- Contre-lecture de classe B par Sonnet 5.5 (effort élevé, accordé par la mère) : « prêt sous corrections listées » ; corrections en v2 (commit `a02b6540070aa5731875d07fbbe124f2dbe27f3b`) ; vérification par le même contre-lecteur : « prêt », quatre réserves mineures. Rapports versés dans `docs/notes/code-dose-reponse-consigne-cachee-v1/`.
- Ligne `CODE-DOSE-REPONSE-CONSIGNE-CACHEE` proposée, inscrite par la mère sur `main` (R-5292) : `registres/code-dose-reponse-consigne-cachee/CODE-DOSE-REPONSE-CONSIGNE-CACHEE-a02b6540…-v1.json`.
- Ordre de lancement v2 proposé (`docs/notes/code-dose-reponse-consigne-cachee-v1/ordre-de-lancement-propose-dose-reponse-v2.md`, aeb89318…), non scellé par la mère (la banque manque).
- Déclaration « aucune génération sous texte privé » ; liste « qui a lu quoi » close.
- Décisions reçues de la mère : contre-lecteur Sonnet 5.5 ; quinze conditions seulement, contrôles croisés reportés (R-5280).

## Reste

- Banque de 64 tâches et ligne `BANQUE-DOSE-REPONSE-CONSIGNE-CACHEE` (autre session ; arrêtée au seuil de contre-vérification, diagnostic en cours selon la mère).
- Branche de lancement à bâtir **depuis le commit du code `a02b6540…`, jamais depuis `main`** (le lanceur et l'amorce exigent le code égal à ce commit), avec la banque, la configuration (`scripts/ecrire_configuration_dose_reponse_v2.py`) et les registres de `main` ; puis contrôles, création, surveillance (ordre v2).
- Suite complète du dépôt : 1 655 essais passés jusqu'à un échec d'un autre chantier (`tests/test_barreau8_moniteurs_passe_v6.py::test_ligne_de_commande_refuse_un_parametre_absent_et_liste_les_modules`), qui dépend de l'ordre des essais et passe seul sur cette branche comme sur `main` ; la fin de la suite tournait encore à la clôture, sans résultat lu.

## Réserves

- V2-01 : la configuration est figée par égalité (GO d'origine, dernier jour de création du 12 décembre) : une prolongation de GO demande une version nouvelle du code.
- V2-03 : la session de lancement doit avoir l'environnement du dépôt (`transformers`) et `HF_TOKEN` pour le contrôle des longueurs en jetons d'avant création.
- Choix d'interprétation nommés dans la ligne CODE (sélectivité « établie » = les deux proportions ; conditions de sabotage et de gonflement des réserves et de l'audit).

## Prochaine action

Quand la banque est inscrite : la mère (ou une session de lancement) bâtit la branche de lancement depuis `a02b6540…`, scelle l'ordre de lancement v2 et joue `GO_ID=GO-2026-11-24-25 … bash scripts/lancer_dose_reponse_v2.sh controles <dossier>`.

## Instances actives

Aucune créée par cette session ; aucune dépense.
