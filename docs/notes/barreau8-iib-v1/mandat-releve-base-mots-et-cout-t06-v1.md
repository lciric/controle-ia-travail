# Mandat du relevé de la base « mots et coût » de T0.6 (vocabulaire et règle), pour son portage dans la lecture du saboteur à budget — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 19:25Z (suite du relevé `docs/notes/barreau8-iib-v1/releve-reglages-base-textuelle-v1.md`, `98284ec7f6ac6bafbae0400234945d2b769db51fe7304b1ae5b181247ddde692`, qui établit que la base (A) de T0.8 ne lit aucun mot et renvoie le vocabulaire à la base (B) de T0.6 ; ligne R-3390 du registre des décisions, par son numéro). Agent neuf. Langue : français, sans sigle seul. La session mère ne fixe aucun de ces réglages.

## Qui tu es
Un **releveur neuf, du côté des moniteurs** : tu n'as lu et ne liras **aucune pièce du saboteur à budget** (jamais `brouillons/ii-b-saboteur-budget-v1/`, `src/controle_ia/iib/`, les branches `prep/iib-code-*` et `lot/compte-4-v1`, ni les autres fichiers de `docs/notes/barreau8-iib-v1/` que ce mandat et le relevé cité). Tu ne lis aucun résultat du programme.

## Ce que tu lis
- Le relevé cité ci-dessus (pour ne pas refaire ce qui est fait).
- Le texte scellé `prereg/T0.6-organismes-v0-v1.md` (compagnon à vérifier) : **seulement** les sections qui définissent la base textuelle dite (B) ou « mots et coût » (vocabulaire, traits, règle de décision, seuils, critère par lequel cette base est dite échouer ou non), repérées par le plan du texte (`grep -n '^#'`) et par une recherche des mots « mots et coût », « vocabulaire », « base (B) » ; ses addenda de même préfixe sous `prereg/`, s'il y en a, pour ces sections ; la décision `docs/decisions/` N-063 (version 2) et N-029, qui parlent de cette base.
- Le module de code que ces sections citent, s'il existe au dépôt (code seulement).
- Rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `registres/` ; aucune branche `calcul/` ou `donnees/` ; pas de recherche récursive hors de ces chemins. Si une section lue contient un résultat, arrête la lecture de cette section et dis-le.

## Ce que tu rends
Une note scellée `docs/notes/barreau8-iib-v1/releve-base-mots-et-cout-t06-v1.md` (`PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`) : ce que la définition scellée fixe (le vocabulaire exact s'il est écrit, ou la règle qui le construit ; les traits ; la règle ; les seuils), mot pour mot avec chemin et ligne ; ce qu'elle ne fixe pas pour un portage dans une autre chaîne, avec les options ; le lien exact entre la base (A) de T0.8 et cette base (B) (sont-elles deux bases, ou une base et son complément ?). En tête, une section pour Lazar en mots clairs : ce qui est fixé sans choix, et les seuls choix restants au format « décision en une phrase ; enjeu ; deux ou trois options (avantage, inconvénient) ; recommandation et confiance ». Ni commit, ni poussée. Arrêt au premier refus, texte exact rendu. Dernier message : chemin, empreinte, ce qui est fixé, choix restants (une ligne chacun), lectures hors mandat.
