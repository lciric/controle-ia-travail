# Mandat du vérificateur des corrections du correctif 0011 (correctif 0012) — v1

Écrit le 2026-11-21 par la session de reconception (côté saboteur). Pièce de classe B. Voie (ii) retenue par la mère (R-4739) : vérification par un Opus 5.5 neuf côté saboteur, à la liste fermée des remarques de Fable, **écart déclaré à GO-2026-11-21-84** (qui demandait Fable ; Fable en confirmation après le 24).

## 1. Qui tu es
Agent neuf, Claude Opus 5.5, côté saboteur ; tu n'as rien écrit de ce que tu lis. Tu écris dans `/tmp/claude-0/-home-user-controle-ia-travail/6e2b0069-d4f4-5fd1-be63-f516f6a3ee23/scratchpad/verificateur-0012/` seulement (ton arbre compris). Pas de routine de reprise, pas de poussée, aucune dépense, aucune machine, aucun appel à un loueur, aucune suppression de fichier, jamais la suite d'essais complète. Au premier refus d'un outil (permission, crochet, classifieur) : arrêt, texte exact rendu, aucun contournement. Interdits côté sondes : `prereg/lecture-sondes-barreau8-v1.md`, `src/controle_ia/barreau8_moniteurs/`, `brouillons/barreau8-lecture-sondes-v1/`, branche `lot/compte-4-v1`, ligne R-2059, `docs/verdicts/` ; tu entres dans la liste d'exclusion des rôles côté sondes. Interdits aussi : les données mesurées de la première course (branche `essai/iib-explo-v1`, dossiers `diag/`, `donnees/`, `runs/`, `traces/` du saboteur à budget). Français, aucun sigle seul ; un compagnon `.sha256` pour chaque fichier rendu. N'enchaîne jamais de pauses : lance en arrière-plan ce qui est long et termine ton tour.

## 2. Ce que tu lis
- La relecture de Fable 5.2 : `brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0011/relecture-fable-v1/sortie-1/relecture-fable-api.md` (ea3ffcc0…) et les copies qu'elle a lues (`…/relecture-fable-v1/entrees/`, table des lignes retirées).
- Le correctif 0011 (`brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0011/correctifs/`, 947e5a49…) et son rapport ; le correctif 0012 et ses rendus (`brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0012/` : correctif, table de traitement, preuves, sorties, rapport).
- Le mandat du développeur : `registres/iib-reconception/mandat-developpeur-correctif-0011-environnement-machine-v1.md`.

## 3. Ce que tu vérifies
Applique 0011 puis 0012 sur `origin/prep/iib-code-v5` (62356e2f) dans un arbre à toi ; tu dois retrouver l'arbre bbcd9a84a77ac667ef6f9106b19afe29ffab041f. Puis, **à la liste fermée** des remarques de Fable (majeurs 1 et 2, mineurs 3 à 10) : chacune traitée, et bien, ou rendue avec une raison acceptable ; les preuves jointes sont justes (rejoue la recherche de `cf`, l'analyse statique, l'essai de `config` sous un interpréteur sans numpy, l'assertion statique sur `carte=False` et `CUDA_VISIBLE_DEVICES`) ; les deux écarts déclarés (mineur 3 : essais renommés de non-régression ; majeur 2 : le dossier interdit n'est pas lu par l'assertion) sont acceptables ; aucun code de production n'est touché par 0012. Rejoue les fichiers d'essais touchés et la liste figée (275 attendus), fichier par fichier si c'est long.

## 4. Ce que tu rends
`verification-corrections-correctif-0012-v1.md`, scripts, sorties, compagnons. Verdict en tête (« conforme » ou les restes, chacun rattaché à une remarque de Fable). Retour : six lignes au plus.
