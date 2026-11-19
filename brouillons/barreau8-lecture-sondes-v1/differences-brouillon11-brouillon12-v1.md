# Différences entre le brouillon 11 et le brouillon 12 du texte « lecture des sondes du barreau 8 et passe de recalcul de l'activité interne » — v1

- Brouillon 11 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon11.md`, empreinte `32c6da0125e3280e5b15316947f768da5025499613e9be8c97c0f2fb6e08fdf7`.
- Contre-lecture du brouillon 11 (Opus 5.5, contre-lecteur neuf) : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon11-v1.md`, empreinte `48480a70c25190696c01326641b6b7d5e323551bae5117df38089714f6cec823` (vérifiée ; lue en entier).
- Brouillon 12 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon12.md` (empreinte : son compagnon `.sha256`).
- Rédacteur : Fable 5.2. Écrit le 2026-11-19 entre 2026-11-19T03:36Z et 2026-11-19T03:38Z (`date -u` ; mêmes heures que la ligne de date du brouillon 12), par programme, à partir du brouillon 11 : remplacements contrôlés (chaque texte cherché doit paraître exactement une fois, sinon rien n'est écrit ; trois lignes de l'essai de la chaîne remplacées entières). Le programme vérifie que les chaînes de la procédure de remplissage restent uniques, qu'il reste exactement deux marqueurs, que la ligne 76 (F-3) est identique à celle du brouillon 11, que le bloc « Noms et champs, liste fermée » est identique au caractère près, et qu'il ne reste aucune mention de l'étiquetage par moitié de tâches hors de la « forme écartée ». Ni le code ni ses essais n'ont été lus.

## 1. Remarques de la contre-lecture du brouillon 11

| n° | objet | état | où, dans le brouillon 12 |
|---|---|---|---|
| N-1 (bloquante) | la commande de réception seule exige le code attesté | appliquée mot pour mot (trois remplacements) | condition de départ D-11 (deux remplacements) ; conditions d'ordre du registre (« avant toute lecture et avant toute réception de la livraison ») |
| N-2 | l'index des invites publiées dans la liste fermée des lectures | appliquée mot pour mot | garde P8 |
| N-3 (mineure) | les deux cas d'arrêt nouveaux de la règle des sondes lues énumérés aux trois endroits | appliquée mot pour mot (trois remplacements) | garde P1 ; plan, point 3 ; liste d'arrêt, ligne 8 |
| O-2 | les quatre empreintes des fichiers de configuration de la révision | écrites | garde P2. Reprises par programme de la note d'interface version 6, question (1) (empreinte de la note vérifiée ; chaque empreinte extraite par motif, une occurrence exigée, jamais recopiée à la main) ; celle de `tokenizer_config.json` est contrôlée égale à celle que la garde P3 (b) citait déjà |

## 2. Décision de plan : forme (A) de l'essai de la chaîne

| objet | état | où |
|---|---|---|
| chapeau : « actions étiquetées » | texte du contre-lecteur, mot pour mot | essai A0, chapeau |
| (i) cas sain : cinq actions sur dix étiquetées dans chaque tâche | texte du contre-lecteur, ligne entière, mot pour mot | essai A0, (i) |
| (iii) artefact d'alignement | texte du contre-lecteur, ligne entière, mot pour mot | essai A0, (iii) |
| limite déclarée de l'essai (remplace celle du brouillon 11) ; sortie de diagnostic gardée, « sans autre effet » | texte du contre-lecteur, ligne entière, mot pour mot | essai A0, dernière ligne. La cause « plancher haut sur le jeu de l'essai » et la réserve en tête sous L5 du brouillon 11 disparaissent avec la forme (R) |
| (ii), rejeu unique, « Si A0 échoue… » | inchangés | — |
| bloc de décision : (A) scellée, (R) non retenue, raison, fréquences citées par chemin et empreinte du rapport | ajouté | « Choix des sondes et des couches », après le bloc de la clause (2) |

**Relecture du texte de la forme (A) contre le reste du texte — cas trouvés et ce qui a été complété**

- Graines et clés : (i) tire sous `sain/<sonde>` ; (ii) reprend les étiquettes de (i) et tire son jeton sous `artefact/<sonde>` ; (iii) tire sous `alignement/<sonde>` ; le rejeu unique emploie `sain-2`, `artefact-2`, `alignement-2` ; toutes sont au plan, point 5. La phrase du chapeau « la graine entière de sa clé sert d'abord au tirage de l'essai, puis au rééchantillonnage » vaut telle quelle. **Rien à compléter.**
- Actions sans jeton noté : les étiquettes sont tirées sur les dix rangs de pas, avant le retrait ; une tâche peut donc porter moins de cinq actions d'une classe, ou une seule classe ; aucun nombre impair n'est à trancher, puisque le tirage ne dépend pas du nombre d'actions restantes. Les dix pas par tâche sont garantis par la garde P3 (d). Une tâche réduite à une classe reste un bloc valide du rééchantillonnage (l'aire est regroupée sur toutes les tâches) ; la règle des 1 % de tirages à une seule classe est inchangée. **Rien à compléter.**
- Rééchantillonnage par blocs de tâches, ligne L5, étape (d) du plan : inchangés et cohérents.
- **Un cas complété : le passage (b-5) du retour à l'option sans scores par jeton.** Il disait « le chapeau, (i), (ii) et (iii) reprennent leur forme du brouillon 4 », ce qui aurait ramené l'étiquetage par moitié de tâches. Réécrit : sous l'option sans scores par jeton, **l'étiquetage reste celui de la forme (A)** ; seuls changent les passages qui supposent les scores par jeton (chapeau, phrase du maximum en (i), (ii) sur le score d'action livré, « scores d'action » en (iii)). C'est la lecture la plus stricte : la décision de plan ne se défait pas par le retour sur les scores par jeton.

## 3. Six précisions du développeur du code de la lecture (version 2 de son code)

| n° | objet | état | où |
|---|---|---|---|
| 1 | au scellement, la cellule de F-3 ne porte que l'entier | portée | plan, point 5 (la cellule elle-même est inchangée au caractère près) |
| 2 | l'audit s'ouvre au moins une seconde après l'inscription de la ligne `LECTURE-SONDES-IIB` | portée telle quelle | audit, « Issue » |
| 3 | le bordereau du code est écrit par la même forme de lancement que la commande qu'il couvre | portée telle quelle | « Code, registre et contrôle de conformité », bordereaux |
| 4 | ce que la lecture lit du bordereau du code de la passe | portée telle quelle | même endroit |
| 5 | clés de graines consignées par la lecture et par la passe | portée | plan, point 5 |
| 6 | nom de la course et commit de lancement dans la trace : type seulement, recopiés en tête | portée | garde de réception r4 |

## 4. Autres changements (demandés, ou de conséquence)

- En-tête : titre et statut « brouillon 12 » ; ligne de date ; contre-lecteur du brouillon 11 ; ce rapport cité avec son empreinte ; « le code de la lecture est en version 2 », la ligne de registre de chaque code faisant foi sur sa version.
- Section « Contre-lecture » : entrée « Contre-lecture 3 septies » ajoutée ; la phrase de renvoi de l'entrée « 3 sexies » devient « cette différence est contre-lue par l'entrée 3 septies » (même correction que celle demandée au brouillon 11 pour l'entrée « 3 quater »).

Ni hypothèse, ni prédiction, ni métrique, ni seuil, ni niveau, ni ligne de la table des issues ne changent.

## 5. À réaligner dans le code (tiré des rapports seuls : le rédacteur n'a lu aucun code)

**Code de la lecture**
1. Essai de la chaîne : tirage des étiquettes de la forme (A) (par tâche dans l'ordre du tri des chaînes, `permutation(10)`, cinq premières positions à 1, avant le retrait des actions sans jeton noté) ; plus de cause « plancher haut » ni de réserve en tête sous L5 ; la sortie de diagnostic reste.
2. Commande de réception seule : exiger les lignes `SCELLEMENT-SONDES-IIB`, `CODE-LECTURE-SONDES-IIB` et `LIVRAISON-PASSE-IIB`, le texte scellé à l'empreinte de sa ligne et les modules exactement ceux du bordereau, avant d'ouvrir la livraison ; aucune cause de refus ne porte un score ni un écart de score (les refus de r6 et r7 ne doivent donc pas imprimer l'écart).
3. Règle des sondes lues : vecteur ou biais non fini, nom des couches 7 ou 23 en double : refus.

**Code de la passe**
1. Garde des chemins : rien à changer si l'index des invites publiées est déjà dans sa liste (notice version 3) ; à vérifier.
2. Garde du modèle : les quatre empreintes écrites au texte sont celles de la note d'interface ; à vérifier qu'elles sont celles du code.

## 6. Marqueurs restants

Deux, et deux seulement : F-3 (entropie racine des graines, ligne 76, inchangée au caractère près) et l'entrée « Contre-lecture 4 (finale, texte rempli) ». Sortie exacte du validateur sur le brouillon 12 : `['section vide ou à remplir : Contre-lecture']`.
