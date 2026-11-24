# Note à la fille 1 — préenregistrement et devis du modèle ouvert, v1

Fable 5.2, 24 novembre 2026. Rien de scellé ni de modifié dans le dépôt. Tables du devis : `calc/devis_calc.py`.

## Écarts à la carte des prédictions

1. **Un seul algorithme.** Tous les bras sont un affinage supervisé repondéré ; la pénalité est un poids sur la récompense moyenne (opérateur B), non un gradient de politique ancré. P4 et P5 ne sont pas testés.
2. **Contraste 2 reformulé.** La loi jointe n'a pas de second bassin (`rem:mean-field`) : le test devient le sens de variation du taux de triche sous pénalité, qui départage loi jointe et loi factorisée à dose faible, sans coût dans la tranche A. Sans ancrage, `prop:bistability` n'est pas éprouvée.
3. **Départ amorcé**, sauf si le modèle de base est admissible.
4. **Tâches à avantage** mutées par programme ; ni ImpossibleBench ni School of Reward Hacks ; tests non modifiables.
5. **Interception tirée au sort** selon le score : la survie est une probabilité.
6. Price : descriptif. Sonde figée : signe conjecturé, le théorème ne donne que le déplacement.
7. Étalonnage sur le modèle de 7 milliards (licence du plus petit non lue).

## Hypothèses non vérifiées

- EvalPlus : licence, 475 tâches disponibles, mutation possible partout.
- Carte de 24 Go ; débits et longueurs.
- Le juge sépare les survies ; l'amorçage donne un départ admissible.
- À neuf paires, la famille secondaire sous Holm exige l'unanimité.
- Dynamique et découplage sont « à revoir » : empreintes à recopier au scellement.

Exemple arithmétique sur valeurs inventées, non prédictif : p = (0,80 ; 0,16 ; 0,04), β = (0,97 ; 0,25 ; 0,90), γ = 1, K = 4 donnent U = 354 (S), 597 (R), 519 (P) ; sous P, depuis q = 200 et 20 % sans mention : 586 (jointe), 132 (factorisée).

## Avant scellement

Lire le dépôt EvalPlus ; écrire et empreinter la consigne, l'invite du juge, le lexique, le programme de mutation, les trois détecteurs et leurs cas plantés ; contre-lecture des deux pièces par un Opus 5.5 neuf, corrections, vérification. Le validateur ne réclame plus que les deux empreintes de contre-lecture.

## Questions à Lazar

1. Tranches financées (A ; A et B ; A, B et C) et plafond de l'étage 1 (50 heures de carte proposées).
2. Accès à `Llama-3.1-8B-Instruct`, ou autre modèle d'audit.
3. Écarts 1 à 3 acceptés ?
4. Couche de la sonde : deux tiers de la profondeur, dernier jeton (recommandé).
5. Lieu durable des adaptateurs (6 à 40 Go).
6. Lecteurs de l'audit de symétrie : agents ou personnes ?
