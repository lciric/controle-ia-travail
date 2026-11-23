# Synthèse — lecture sur PDF des 16 papiers « saboteur et sondes » — v1

Mandat GO-2026-11-23-16, repris par GO-2026-11-23-30. Rédaction : Opus 5.5 (mère de la lecture), d'après les 16 fiches scellées de ce dossier ; lectures faites par quatre lecteurs Opus 5.5, effort élevé. Les 16 empreintes de PDF ont été recalculées par la mère le 23 novembre vers 08:40Z et concordent avec les douze premiers signes donnés au registre `registres/veille-de-cap/papiers-du-depot-v1.md` (R11) ; chaque fiche donne l'empreinte complète. Chaque chiffre ci-dessous renvoie à la page du PDF, telle que la fiche la cite. Les fiches font foi.

## Verdict d'ensemble

Quatre papiers permettent ce que la décision du dépôt voulait en tirer : la théorie du danger (0801.3549, pour la seule forme à deux signaux), « Overthinking the Truth » (2307.09476), DiscoveryWorld (2406.06769) et l'ensemble aveugle de 2609.23254. Dix le permettent en partie, dont Singh (2610.18948), qui le permet pour la N-076 et en partie pour le GO-2026-11-21-59. Deux ne le permettent pas tel qu'écrit : He et al. (1612.09027), qui est un contre-indice, et Arnold et al. (2109.11761), qui ne traite pas le bilan visé mais occupe le nul par acte. Les écarts de lecture les plus nets sont dans la N-075 v3 : « et sa calibration » pour le papier dopamine, et la lecture de « Watch the Weights ». La N-076 a besoin de deux nuances. Aucune dépense n'est nécessaire avant le 1er décembre.

## Les trois papiers les plus utiles avant le 1er décembre

1. **Sélection d'attaque en cadre agentique (2606.06529).** Il répond à l'objection 8 de la note d'entretien v6. Un attaquant qui choisit quand attaquer et quand abandonner abaisse la sûreté sous un audit des trajectoires les plus suspectes. Le résumé annonce −20 points au budget d'audit de 1 % (p. 1). Mais une seule baisse a un intervalle de confiance qui exclut zéro : −28 points, de −37 à −8, sur 23 trajectoires (p. 5). Les auteurs la disent « heuristic upper bound » (p. 11). Le tirage d'audit au hasard n'y est jamais testé : le papier motive notre plancher au hasard, il ne prouve pas qu'il tient. Il fournit une épreuve, avec ses politiques de départ et d'arrêt, pour le bras d'attaque informé.
2. **Le papier dopamine (2602.00986).** Parmi les 16 papiers lus, c'est le seul qui lise la réussite attendue dans des neurones épars ; la fiche note que cette zone est occupée. Il établit le pouvoir de séparation, pas la calibration : le mot n'est pas dans le PDF. Il donne une base bon marché à battre : la longueur de la question seule atteint une aire sous la courbe de 0,62, contre 0,67 pour les neurones de valeur (p. 8). L'ablation de 1 % des neurones de valeur fait passer l'exactitude de 75,2 % à 20,3 % (p. 5) : c'est un gabarit d'épreuve pour les lentilles. Sur les tâches floues, il faut concéder : ni récompense, ni adversaire n'y sont testés (p. 25).
3. **Attaque étagée d'une chaîne de garde-fous (2506.24068, STACK).** Il prévient l'objection « vos deux regards, c'est la défense en profondeur, que STACK casse ». L'attaque étagée atteint 71 % de succès, et 33 % par transfert sans accès à la chaîne (p. 1, 10). Ces 71 % supposent que l'attaquant voit quel étage l'a bloqué (p. 10). On en tire une règle pour le bras d'attaque : aucun retour à l'agent sur le regard qui a sonné. Le papier ne traite que l'abus par requête, pas le sabotage ; aucune sonde sur les activations n'entre dans la chaîne (p. 3).

**Juste après :**
- Singh (2610.18948) : un excès borné à l'ordre de la racine de l'horizon (p. 9). Il appuie « la référence est hors de sa garantie ».
- Sobers et al. (1608.00698) : un débit constant ne tient que si le bruit est retiré à chaque fenêtre (p. 5). Il appuie « l'obstacle est la référence honnête ».
- L'autocohérence corrélée (2611.26592) : une corrélation estimée de 0,435 et 0,480 (p. 1). Un épisode vaut donc environ deux tirages indépendants, et l'unité de mesure est l'épisode.

## Corrections à porter, sans dépense (environ une heure en tout, selon les coûts des fiches)

- **N-075, version 4** :
  - « et sa calibration » devient « et son pouvoir de séparation » (dopamine, p. 8).
  - La réserve « sous audit des plus suspects ; une baisse significative à 1 % » s'ajoute pour 2606.06529 (p. 5).
  - « Watch the Weights » se relit ainsi : la répétition d'un écart déjà signalé passe en silence, tandis qu'un écart qui grandit est signalé (p. 5).
  - La page 10 de STACK est citée.
- **N-076, prochain erratum** : 1612.09027 est cité comme nuance de 1608.00698. Le débit constant n'existe qu'à probabilité de détection fixée, et tend vers zéro avec elle (p. 4).
- **Registre des papiers** : du code exploratoire est écrit pour le papier dopamine, non lancé.

## Réserves

Contre-lecture : `contre-lecture-synthese-v1.md` (Opus 5.5, effort moyen, agent neuf) — « tient avec corrections » ; cinq chiffres tirés au hasard, tous trouvés aux pages citées ; ses quatre écarts sont portés dans cette version. Le lecteur de Singh n'a lu que 6 pages sur 66 (p. 1-3, 9, 48-49). Les synthèses de la décision N-047 valent pour la N-053, qui la remplace avec le même contenu, vérifié par comparaison. Toute rejouée sur notre banc (attaque étagée, sélection d'attaque, base « longueur de la question ») demande un devis et un GO.
