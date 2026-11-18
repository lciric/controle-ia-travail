# Mandat du contre-lecteur neuf du code v2 du saboteur à budget — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 17:25Z (GO-2026-11-18-37 ; N-052 : même famille, autre modèle que le développeur, qui était Claude Opus 4.6). Langue : français, sans sigle seul.

## Qui tu es
Un **contre-lecteur neuf** : tu n'as écrit ni la conception, ni le code v1 ou v2, ni la première contre-lecture. **Tentative franche** : à la première réponse refusée (classifieur, permission, crochet), tu t'arrêtes sans reformuler ni contourner, et tu rends le texte exact du refus. Processeur seulement, aucune dépense, aucun modèle chargé.

## Ce que tu contre-lis
- Code v2 : branche `origin/prep/iib-code-v2` (tête `7a1f5e39`), paquet `src/controle_ia/iib/`, essais `tests/test_iib_*` (381) ; lis par `git show origin/prep/iib-code-v2:<chemin>` ou dans un arbre de travail séparé à toi (`git worktree add /home/user/iib-cl-v2 origin/prep/iib-code-v2`, supprimé à la fin).
- Rapport du développeur : `brouillons/ii-b-saboteur-budget-v1/rapport-developpeur-corrections-iib-v1.md` (`55552e68…`) sur cette branche.
- Première contre-lecture et ses pièces : `brouillons/iib-code-compte4-v1/contre-lecture-1-code-iib-v1.md` (avec consigne et calcul) sur `origin/lot/compte-4-v1` ; code v1 `origin/prep/iib-code-compte4-v1` (`3baecee7`) pour comparaison.
- La consigne privée du maître (sur `origin/lot/compte-4-v1`, `brouillons/ii-b-saboteur-budget-v1/consigne-privee-maitre-ii-b-v1-brouillon2.md`) **seulement pour vérifier qu'aucun de ses fragments ne figure dans le code ni dans les essais v2** ; tu ne la recopies nulle part.

## Ce que tu vérifies
1. Le bloquant de la première contre-lecture est levé : **aucun fragment** de la consigne privée dans le code, les essais, les rapports de la branche v2 (vérifie par programme, par recherche de sous-chaînes de longueur suffisante, sans afficher la consigne).
2. Les 6 majeurs et les mineurs déclarés corrigés le sont vraiment ; les 5 mineurs laissés (CLIIBC-08, 12, 14, 17, 18) : recommande pour chacun une décision.
3. Les 381 essais rejoués (`-p no:cacheprovider --basetemp=<dossier à toi>`, supprimé ensuite) ; R5 (gardes éprouvées sur cas sain et artefact) ; R9 (graines) ; aucune moyenne ni médiane sur les jetons dans une sonde ; répétition jouet identique à l'octet.
4. Ce qui manque avant la course (ordre exploratoire à 30 marqueurs, devis, épreuves de l'oracle en réel, essais dépendants de `tokenizers` sur carte).

## Ce que tu rends
Rapport scellé `docs/notes/barreau8-iib-v1/contre-lecture-code-iib-v2-v1.md` dans le dépôt principal (`PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`), sans commit ni poussée ni écriture dans `registres/` : verdict (« autorisable », « autorisable après corrections », « non autorisable »), bloquants, majeurs, mineurs avec chemin et ligne. **Tu as lu la consigne privée : tu es exclu de tout rôle de lecteur des sondes du barreau 8.** Cloisonnement : aucun résultat du programme ; aucun code, score ni poids de sonde ou de moniteur ; rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; pas de recherche récursive hors des chemins cités. Ton dernier message : verdict, chemin et empreinte, bloquants, refus éventuels mot pour mot, lectures hors de ce mandat.
