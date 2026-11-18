# Mandat du relevé des réglages de la base textuelle « mots et coût » pour son portage dans la lecture du saboteur à budget — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 19:20Z (GO-2026-11-18-30, GO-2026-11-18-37 ; ligne R-3389 du registre des décisions, par son numéro). Agent neuf. Langue : français, sans sigle seul. La session mère, exposée à un résultat du programme, ne fixe aucun de ces réglages.

## Qui tu es
Un **releveur neuf, du côté des moniteurs** : tu n'as lu et ne liras **aucune pièce du saboteur à budget** (ni sa conception, ni sa consigne, ni son code, ni ses rapports : jamais `brouillons/ii-b-saboteur-budget-v1/`, jamais `src/controle_ia/iib/`, jamais les branches `prep/iib-code-*` ni `lot/compte-4-v1`, jamais les autres fichiers de `docs/notes/barreau8-iib-v1/`). Tu ne lis aucun résultat du programme.

## Objet
La lecture du barreau 8 compare des sondes à une base textuelle. Cette base doit être **la base (A) « mots et coût » telle qu'elle est scellée**, portée sans invention. Le code du portage a été écrit d'après une description, sans ouvrir la base : neuf réglages restent à fixer avant la course. Tu relèves, pour chacun, **ce que dit la définition scellée**, et rien d'autre.

## Ce que tu lis
- Le texte scellé `prereg/T0.8-base-A-mots-et-cout-v1.md` (compagnon à vérifier) et ses addenda s'il en a (même préfixe de nom sous `prereg/`).
- Le code de cette base sous `src/controle_ia/bases/` (code seulement ; liste le dossier, puis lis les modules que le texte scellé cite).
- Rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `registres/` ; aucune branche `calcul/` ou `donnees/` ; pas de recherche récursive hors de ces chemins.

## Les neuf réglages (libellés du vérificateur du code, recopiés sans rien fixer)
(a) portage complet de la base textuelle, ou forme hybride déclarée ; (b) la liste exacte des traits de la base « traits » ; (c) l'unité de longueur : caractères, ou jetons (et alors quel jetoniseur, à quelle révision) ; (d) garder ou retirer le trait redondant de validité ; (e) la règle « sans centre » : nombre minimal de coûts lisibles par tâche, et traitement d'une tâche sans centre ; (f) le centrage : quelle statistique, quelles conditions mises en commun, calcul global ou par pli ; (g) la méthode d'ajustement : méthode, régularisation, nombre maximal d'itérations, tolérance, critère d'arrêt, facteur du seuil de non-convergence, gradient lu avant ou après le dernier pas ; (h) le vocabulaire de la base « mots et coût », à confirmer ; (i) dans les deux options, l'en-tête du module à mettre à jour et les essais du portage à écrire.

## Ce que tu rends
Une note scellée `docs/notes/barreau8-iib-v1/releve-reglages-base-textuelle-v1.md` (`PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`) : pour chaque réglage (a) à (h), **la valeur exacte que fixe la définition scellée**, citée mot pour mot avec chemin et ligne (texte scellé d'abord ; code ensuite, avec le nom de la constante ou de la fonction) ; ou « non fixé par la définition scellée », avec ce que le code fait de fait et les options ouvertes ; si le texte scellé et le code se contredisent, dis-le. Pour (i) : la liste des essais qu'un portage fidèle devrait passer (cas sain et artefact, R5), décrits sans code. En tête, une section pour Lazar, en mots clairs : ce qui est fixé sans choix, et les seuls points où un choix reste, chacun au format « décision en une phrase ; enjeu ; deux ou trois options (avantage, inconvénient) ; recommandation et confiance ». Ni commit, ni poussée. Arrêt au premier refus, texte exact rendu. Dernier message : chemin, empreinte, nombre de réglages fixés par la définition, nombre de choix restants, lectures hors mandat.
