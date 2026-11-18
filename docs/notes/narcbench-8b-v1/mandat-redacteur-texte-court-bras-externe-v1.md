# Mandat du rédacteur neuf du texte court du barreau 7 (bras externe NARCBench, au processeur) — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 16:40Z, sous GO-2026-11-18-30 et R-3310 (voie décidée par Lazar le 10 novembre, D-3 (a), R-2175 : « bras externe sur les activations publiées par les auteurs, au processeur, 0 USD, sous un texte court neuf ») ; demande de Lazar d'accélérer. Langue : français, sans sigle seul.

## Qui tu es
Un **rédacteur neuf**, sous-agent de la session mère, **distinct du développeur** du bras externe (qui travaille en parallèle sur `prep/narcbench-externe-v2`, mandat `docs/notes/narcbench-8b-v1/mandat-developpeur-externe-v2-v1.md`) ; tu ne seras ni contre-lecteur de ce texte ni lecteur de son verdict. Tu n'as lu et ne liras aucune donnée réelle ni aucun score.

## Objet
Écrire le **préenregistrement court** du barreau 7 : « notre chaîne reproduit-elle un résultat positif déjà publié ? » — nos sondes (la chaîne du programme) appliquées aux **activations publiées par les auteurs du banc NARCBench**, au processeur, 0 USD. Sous `prereg/narcbench-bras-externe-v1-brouillon1.md`, au gabarit `prereg/gabarit-preregistrement-v1.md` (validé par `src/controle_ia/prereg.py`) : hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse, critères de lecture gelés, liste d'arrêt, puissance, lignes de registre (clés propres : scellement, code, lecture), code (référence laissée au développeur : « à inscrire par la ligne de code avant toute exécution »), « ce que les auteurs savaient avant le scellement », frontière (ce que le texte ne dit pas : rien sur G1, rien sur nos organismes).

## Règles de fond
- **R7** : tout chiffre de l'article publié (le résultat à reproduire, ses conditions, sa tolérance) est **vérifié sur le PDF empreinté, page citée** ; cherche le PDF sous `docs/sources/pdf/` par son nom, sinon dis qu'il manque (la mère le fera verser) — **aucun chiffre non vérifié dans le texte**.
- **R8** : une limitation de l'article n'est pas un trou du champ.
- Le texte définit d'avance **ce que « reproduire » veut dire** (tolérance, intervalle, signe), et les deux issues écrites d'avance (reproduit, non reproduit), sans viser un signe (R3).
- Interdit du programme : aucune moyenne ni médiane sur les jetons dans une sonde de production ; graines par `numpy.random.SeedSequence` (R9).

## Ce que tu lis
`docs/decisions/decision-N-061-v1.md` ; lignes R-2175, R-2184, R-2735, R-3310 de `registres/decisions.md` (par leur numéro) ; `docs/notes/narcbench-8b-v1/devis-narcbench-8b-v2.md` ; le brouillon 4 (`prereg/brouillon-narcbench-8b-descriptif-v1-brouillon4.md`) et sa contre-lecture 3 (`prereg/contre-lectures/narcbench-8b-descriptif-v1-brouillon4-cl3.md`), pour reprendre ce qui vaut pour le bras externe ; les **interfaces** du code existant (branches `origin/prep/narcbench-externe-v1` et `origin/prep/narcbench-8b-code-v1`, noms de fonctions, entrées et sorties ; pas besoin de tout le code) ; le PDF de l'article. **Jamais** : les fichiers de données, `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, branches `calcul/` et `donnees/`, aucun résultat du programme ; pas de recherche récursive dans le dépôt.

## Ce que tu rends
Le brouillon 1 scellé (`PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`), sans commit ni poussée ni écriture dans `registres/` ; ton dernier message : chemin et empreinte, les chiffres de l'article vérifiés (page), les points ouverts avec recommandation, et toute lecture hors de ce mandat. Puis viendront la contre-lecture R2 par un agent neuf d'un autre modèle, les corrections, le scellement.
