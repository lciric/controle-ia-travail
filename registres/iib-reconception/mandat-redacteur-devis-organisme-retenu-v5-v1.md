# Mandat du rédacteur du devis de l'étalonnage et de la course de l'organisme retenu — v1

Écrit le 2026-11-21 par la session de reconception (côté saboteur). Pièce de classe A (devis). Accord : GO-2026-11-21-66 (ligne de calcul neuve accordée, plafond inscrit sur ce devis).

## 1. Qui tu es
Rédacteur neuf, Claude Fable 5.2, côté saboteur. Tu écris dans `/tmp/claude-0/-home-user-controle-ia-travail/6e2b0069-d4f4-5fd1-be63-f516f6a3ee23/scratchpad/devis-v5/` seulement. Pas de routine de reprise, pas de poussée, aucune dépense, aucune machine, aucun appel à un loueur, aucune suppression de fichier, jamais la suite d'essais complète. Au premier refus d'un outil (permission, crochet, classifieur) : arrêt, texte exact rendu, aucun contournement. Interdits côté sondes : `prereg/lecture-sondes-barreau8-v1.md`, `src/controle_ia/barreau8_moniteurs/`, `brouillons/barreau8-lecture-sondes-v1/`, branche `lot/compte-4-v1`, ligne R-2059, `docs/verdicts/` ; tu entres dans la liste d'exclusion des rôles côté sondes. Interdits aussi : les données mesurées de la première course (branche `essai/iib-explo-v1`, dossiers `diag/`, `donnees/`, `runs/`, `traces/` du saboteur à budget). Français, aucun sigle seul ; un compagnon `.sha256` pour chaque fichier rendu. Tu ne lis aucune consigne privée.

## 2. Ce que tu lis
- Le texte scellé `brouillons/ii-b-saboteur-budget-v5/conception-organisme-retenu-ii-b-v5-scellee-v1.md` (sha256 c1dc54597a1ab4b467331673607d986e46a706c06253bb40070e5d15caaa61f2 ; nœuds tous à leur défaut, nœud 7 en (b')) : sections 10.1, 10.2 (plafond de tours en formule), 12 (coût en appels du modèle), la table des nœuds (nœud 7 (b') : un oracle par tour, 3 520 actions d'oracle hors tours) et 15.
- Le devis de la première course et son calcul : `brouillons/ii-b-saboteur-budget-v1/devis-ii-b-v1-brouillon6.md`, `calcul-devis-ii-b-v3.py` et sa sortie ; l'ordre scellé `brouillons/ii-b-saboteur-budget-v1/ordre-exploratoire-ii-b-v1.md` (machine, coupures).
- Les durées et dépenses réelles de la première course, par `git show origin/claude/iib-executante-v1:<chemin>` dans `registres/iib-executante/course-836c7ccc-v1/` (inventaire, diagnostic : horodatages, prix horaire, dépense) : seulement durées, prix et dépenses, rien d'autre.

## 3. Ce que tu écris
Un devis en deux étapes sous une ligne neuve : (1) l'étalonnage (les deux oracles ; épisodes honnêtes, régénérés, flagrants, comme le texte les compte) ; (2) la course, si la règle de désignation dit « part » : tours jusqu'au plafond, oracle non désigné selon (b'), distillation, évaluation. Pour chacune : nombre d'appels, durée attendue et au pire (marge justifiée par les durées réelles de la première course), prix horaire de la machine, stockage, total attendu et au pire, **plafond proposé et coupure** (la coupure avant le plafond, comme sur la première ligne). Calcul par un script versé (`calcul-devis-ii-b-v5.py`) et sa sortie ; chaque chiffre renvoie à une ligne de la sortie ou à un chemin. Dis aussi le plafond de tours qui en découle (10.2) et ce qui se passe si la course le dépasse.

## 4. Ce que tu rends
`devis-ii-b-v5-brouillon1.md`, script, sortie, compagnons. Retour : dix lignes au plus (totaux attendus et au pire par étape, plafond et coupure proposés, plafond de tours).
