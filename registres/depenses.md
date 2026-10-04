# Registre des dépenses

Aucune dépense sans GO sur devis. Alerte à Lazar à 80 % d'un devis approuvé.

| date | GO | devis | instance (identifiant) | type | heures | coût (USD) | cumul sur devis | note |
|---|---|---|---|---|---|---|---|---|

Devis approuvé : phase 0, plafond 150 USD, alerte à 120 USD (GO-2026-10-04-08, échéance 2026-11-01).

Cumul au 2026-10-04 11:26 UTC : 0 USD sur 150 (aucune instance créée).

## Engagements avant création d'instance

- 2026-10-04 18:02 UTC — validation de T0.4 sur modèle réel (GO-2026-10-04-08 ; procédure `docs/procedures/validation-T0.4-modele-reel-v1.md`, section 3). Une seule offre répond aux critères scellés :
  - offre 48704113 (machine 148671, hôte 214845) : H100 SXM, 80 Go ; CUDA maximale 13.3, pilote 610.57.04 ; vérifiée ; centre de données ; Tchéquie ; fiabilité 0,996 ; 129 Go de mémoire vive ; 24 cœurs effectifs ;
  - prix : 3,124 USD de l'heure tout compris, dont 0,074 USD de l'heure pour 80 Go de stockage ; téléchargement 0,038 USD par Go (environ 20 Go : modèle, roues), soit environ 0,8 USD ;
  - coût au plafond de 6 heures : 18,75 + 0,8 ≈ 19,6 USD ; plus environ 1,8 USD par jour tant que l'instance arrêtée est gardée (disque, gros tableaux), jusqu'au verdict ;
  - attendu : 1 à 2 heures, soit environ 4 à 7 USD ;
  - cumul engagé au plafond : 19,6 USD sur 150 (alerte à 120).
