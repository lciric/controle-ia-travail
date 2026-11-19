# Geste d'organisation : rejeu du relevé des têtes du distant (§ 1.1 de la commande de lecture version 3) — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Session conductrice `session_013QMayjNC5GKdDFTN87oAV5`, 2026-11-18.

## Fait
Le premier jeu du § 1.1 par le lecteur-opérateur (relevé du 2026-11-18T23:41:34Z) conclut « ON NE LANCE PAS » pour une seule ligne : trois branches du distant avaient avancé depuis la récupération complète de l'étape 0 (`main`, `claude/affectionate-bardeen-j7kddp`, `calcul/neuron-lens-b-beta-v1` ; noms et identifiants de commit seulement). Rien n'est consommé : aucun arbre de lecture monté, aucune preuve écrite, aucun commit, la lecture n'a pas été lancée. Relevé gardé dans le dossier temporaire de la session : `scratchpad/lecture-bbis/releve-mise-en-place.txt`, empreinte `06b2735d8d4240636a3ca432b35b16fa0c6f91fb246b5052dc065fb2e45ddab3`. C'est le cas que la commande prévoit (étape 0, § 1.1 ; contre-lecture de la version 3, point 4 : « c'est le bon comportement »).

## Défaut de la commande, relevé par l'opérateur
La commande dit que l'opérateur « rejoue le § 1.1 sous un nom de relevé neuf », mais ses blocs écrivent et lisent le relevé sous un nom fixe (`releve-mise-en-place.txt`) : le § 1.1 refuse de l'écraser, et les § 1.2 et § 2 exigent « CONCLUSION : conforme » dans le fichier de ce nom. La commande n'écrit pas comment le rejeu se fait.

## Geste décidé par la conductrice (organisation ; aucun bloc de la commande n'est changé)
Avant chaque rejeu du § 1.1, l'opérateur **renomme** le relevé refusé, dans le dossier temporaire, en `releve-mise-en-place-refuse-<k>.txt` (k = 1, 2, …), après en avoir relevé l'empreinte ; il ne le supprime pas et ne le modifie pas. Puis il rejoue le § 1.1 tel qu'il est écrit, qui écrit un relevé neuf sous le nom que les blocs suivants lisent. Les fichiers de noms et de têtes que le § 1.1 réécrit sans garde sont réécrits. Le fichier des paramètres n'est pas recréé. Chaque relevé refusé est rendu par son chemin et son empreinte, et versé au dépôt avec les autres relevés à la fin.
Ce geste ne touche à aucune donnée, à aucun registre, à aucun fichier du dépôt ; il ne change le sens d'aucun contrôle : le relevé qui compte est celui du dernier jeu, conforme en entier, et les relevés refusés restent.

## Fenêtre accordée par la session mère (message du 2026-11-18 à 23:41:26Z, R-3532)
La conductrice envoie « fenêtre main : début » avant sa récupération complète ; la mère ne pousse plus sur `main` jusqu'à « fenêtre main : fin ». Les autres sessions poussent sur leurs branches : si l'une avance, même règle — nouvelle récupération, relevé rejoué.

## Réserve
Ce geste n'a pas été contre-lu. Il est à citer par le juge parmi les écarts de conduite s'il juge qu'il touche la lecture.
