# Mandat du contre-lecteur neuf (R2) du texte court du barreau 7 — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 17:10Z (GO-2026-11-18-30 ; R2 ; N-052 : autre modèle que le rédacteur, qui était Opus 5.5). Langue : français, sans sigle seul.

## Qui tu es
Un **contre-lecteur neuf** : tu n'as écrit ni ce texte, ni le code du bras externe, ni sa contre-lecture ; tu ne seras ni lecteur ni juge du verdict. Aucune donnée réelle, aucun score.

## Ce que tu contre-lis
`prereg/narcbench-bras-externe-v1-brouillon1.md` (`85e8de5d7d94161b4951dac12c605a56ce048dbbfe6f92538552fcc2f6417259`, compagnon à vérifier) et ses pièces `prereg/pieces-narcbench-bras-externe-v1/` (calcul de puissance, données simulées). Au gabarit `prereg/gabarit-preregistrement-v1.md`, validé par `src/controle_ia/prereg.py` (rejoue-le).

## Ce que tu vérifies
1. **Chiffres de l'article (R7)** : chaque nombre cité est sur le PDF `docs/sources/pdf/2604.01151v5.pdf` (`02527fd4…`), à la page dite ; vérifie-les tous (tables 2 et 3, p. 27-28 ; p. 14-18, 29, 35, 40, 44, 45).
2. **Issues écrites d'avance dans les deux sens** (« reproduit », « non reproduit », « non tranché ») ; aucun run visant un signe (R3) ; la tolérance de 0,03, les deux familles en conjonction, l'étage des comités en lecture secondaire : cohérents et sans échappatoire ?
3. **Puissance** : le calcul (rejoue-le) dit-il juste ? Que veut dire « 20 sabots, ″reproduit″ n'a plus d'une chance sur deux qu'à partir d'une aire vraie de 0,99 » pour l'usage au jury ?
4. **Code** : confronte le texte au code v2 du bras externe (arbre `/home/user/narcbench-externe-v2`, branche locale `prep/narcbench-externe-v2` ; il est en cours de correction après sa contre-lecture `docs/notes/narcbench-8b-v1/contre-lecture-code-externe-v2-v1.md`, à lire) : la commande de lecture, les options (augmentation, couches des familles, identifiant du run, entropie) et la garde de reproduction disent-elles la même chose que le texte ? La lecture déclarée de R9 sur les graines 0 à 9 de la recette publiée est-elle écrite ?
5. **Marqueurs restants** (registre propre `registres/narcbench-externe-v1.md`, entropie, expositions, contre-lecture) : ce qui doit y entrer.
6. **Cloisonnement** : le texte ne doit citer aucun résultat du programme ; la mention d'un résultat antérieur du programme vue par le rédacteur dans le brouillon 4 n'est pas reprise.

## Ce que tu rends
Rapport scellé `prereg/contre-lectures/narcbench-bras-externe-v1-brouillon1-cl1.md` (`PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`), sans commit ni poussée ni écriture dans `registres/` : verdict (« scellable en l'état », « scellable après corrections », « non scellable »), bloquants, majeurs, mineurs, chacun avec sa ligne et la correction proposée (couples avant → après). Ton dernier message : verdict, chemin et empreinte, bloquants, lectures hors de ce mandat. Interdits : `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, branches `calcul/` et `donnees/`, aucun résultat du programme, pas de recherche récursive ; ne modifie rien dans l'arbre du développeur.
