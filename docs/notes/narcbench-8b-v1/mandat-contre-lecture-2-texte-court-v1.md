# Mandat de la contre-lecture 2 (vérification courte) du texte court du barreau 7 — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 17:55Z (R2 ; autre modèle que le rédacteur, qui était Opus 5.5 ; agent neuf, distinct du contre-lecteur 1). Langue : français, sans sigle seul.

## Objet
Vérifier `prereg/narcbench-bras-externe-v1-brouillon2.md` (`7bb21dc0bec7a5fcbff41c84ee2554966e7ddc0acf8703cf7fe8f78d224acb02`, compagnon à vérifier) contre : le brouillon 1 (`85e8de5d…`), la contre-lecture 1 (`prereg/contre-lectures/narcbench-bras-externe-v1-brouillon1-cl1.md`, `9217284f…`), la contre-lecture du code (`docs/notes/narcbench-8b-v1/contre-lecture-code-externe-v2-v1.md`, `9b90884a…`) et les choix de la mère (lignes R-3335 et R-3341 de `registres/decisions.md`, par leur numéro).

## Ce que tu vérifies
1. Chaque remarque de la contre-lecture 1 (B1 à B4, M1 à M5, mineurs) est traitée comme le tableau de traitement le dit ; rien n'est changé hors de ce tableau sans être déclaré (rejoue `diff` entre les brouillons 1 et 2).
2. Les **choix du rédacteur hors des remarques** (perceptron retiré ; une graine par couche pour nos familles ; lecture par agent ; étage des comités sans plancher ni placebo ; Mahalanobis à l'étage stéganographique seulement ; refus si scikit-learn absent ou d'une autre version ; relance permise tant que les activations ne sont pas ouvertes) : chacun est-il déclaré, justifié sans regard à un résultat, et sans échappatoire (R3) ?
3. La **réserve de l'intervalle** : « reproduit » sort à tort dans 0,185 des simulations quand l'aire vraie est exactement à la marge du pic. Rejoue le calcul ; dis si le texte le déclare assez clairement pour un lecteur du verdict, et propose la phrase.
4. La **section « Configuration canonique de la commande »** : six lignes `clé : valeur`, une fois chacune ; la ligne `Entropie : <entier>` reste le seul marqueur ; les clés `SCELLEMENT-NARC-EXT`, `CODE-NARC-EXT`, `LECTURE-NARC-EXT` et le registre `registres/narcbench-externe-v1.md` sont cohérents partout.
5. La **liste des 18 écarts texte-code** : complète contre le code v2 (arbre `/home/user/narcbench-externe-v2`, branche locale `prep/narcbench-externe-v2`, lecture seule ; le développeur y corrige en ce moment : dis à quelle tête tu as lu) ; lesquels exigent du code avant que la ligne `CODE-NARC-EXT` puisse s'écrire.
6. Les chiffres de l'article ajoutés ou déplacés depuis le brouillon 1 (PDF `docs/sources/pdf/2604.01151v5.pdf`, pages citées) ; le validateur `src/controle_ia/prereg.py` (seuls manques admis : l'entropie et l'entrée de cette contre-lecture).

## Ce que tu rends
Rapport scellé `prereg/contre-lectures/narcbench-bras-externe-v1-brouillon2-cl2.md` (`PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`) : verdict (« scellable en l'état », « scellable après corrections », « non scellable »), bloquants et majeurs avec couples avant → après. Ni commit, ni poussée, rien dans `registres/` ; aucune donnée réelle, aucun score, aucun résultat du programme ; rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; ne modifie pas l'arbre du développeur. Dernier message : verdict, chemin, empreinte, bloquants, lectures hors mandat.
