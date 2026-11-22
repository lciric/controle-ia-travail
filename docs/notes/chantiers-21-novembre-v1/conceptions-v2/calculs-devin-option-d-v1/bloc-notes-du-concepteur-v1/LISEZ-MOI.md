# Bloc-notes du concepteur — erratum 1 de la conception 2 (épreuves du devin), v3 consolidée

- Classe C, sans valeur de pièce. Versé avant la fin du conteneur de la session, selon la règle « récupérer ce qui est récupérable ».
- Les pièces qui font foi sont ailleurs : l'erratum (`../../conception-2-epreuves-du-devin-v3-consolidee-erratum-1.md`), le script de calcul et sa sortie (`../calculs-devin-option-d-v1.py`, `../calculs-devin-option-d-v1-sortie.txt`, `../calculs-devin-option-d-v1-sortie.json`), le programme de vérification des couples et son compte rendu (`../verification-couples-erratum-1-v3-consolidee-v1.py`, `../verification-couples-erratum-1-v3-consolidee-v1-sortie.txt`).

## Ce que le dossier contient

| Fichier | Ce que c'est |
|---|---|
| `batir_erratum.py` | L'assembleur de l'erratum. Il lit les deux fichiers de textes, contrôle que chaque ancien figure une seule fois dans la v3 consolidée, et écrit l'erratum au format des errata de la v2. Rejoué depuis ce dossier, il redonne l'erratum scellé à l'octet près (contrôlé le 22 novembre 2026). |
| `erratum_textes.py` | L'en-tête, les sections 1 à 3, 5 et 6 de l'erratum. |
| `erratum_couples.py` | Les 37 couples (identifiant, lieu, ancien, nouveau). |
| `exploration-valeurs-critiques-v1.py` | Première exploration : valeurs critiques du maximum avec et sans scores de queue. Remplacée par la section C2 du script de calcul. |
| `exploration-fenetres-v1.py` | Première exploration : puissance sur une fenêtre sans audit, ex æquo départagés au hasard. Remplacée par la section C3 du script, où les ex æquo sont compris dans l'ensemble. |
| `sortie-premiere-course-complete-v1.txt` | Sortie de la première course complète du script, avant trois retouches de forme (fichier de chiffres clés sans valeur « NaN », tailles interpolées du prédicteur appris, calcul du test de tendance). |

## Ce que la première course montre

La sortie scellée vient d'une seconde course complète, lancée après les trois retouches. Comparées ligne à ligne, durées mises à part, les deux sorties ne diffèrent que par ce qui a été retouché : la ligne de l'empreinte du script ; douze lignes de résultat de la section C3, dont seul le libellé change (« hors de la grille » au lieu de « nan ») ; cinq lignes neuves pour la section E3 et quatre pour la section F. Tous les chiffres communs sont identiques : le script se rejoue. La version du script qui a produit la première sortie (empreinte 22e49226be2ac844d3b83b9e3b2ff9e5ff40715eaa6466ccd7eafaa49d9d794f) n'est pas versée : elle ne différait de la version scellée que par ces trois retouches.

## Pour corriger l'erratum après la contre-lecture

Un erratum scellé ne se réécrit pas. Une version corrigée se bâtit sous un nom neuf : copier ce dossier sous un nom versionné, changer les textes, lancer `python batir_erratum.py CHEMIN_NEUF`, puis le programme de vérification des couples, adapté au nom neuf.
