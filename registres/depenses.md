# Registre des dépenses

Aucune dépense sans GO sur devis. Alerte à Lazar à 80 % d'un devis approuvé.

| date | GO | devis | instance (identifiant) | type | heures | coût (USD) | cumul sur devis | note |
|---|---|---|---|---|---|---|---|---|
| 2026-10-04 | GO-2026-10-04-08 | phase 0 (T0.4) | 54183350 | carte H100 SXM, à la demande (3,124 USD/h tout compris) | 0,15 (18:03 → 18:12) | ≈ 0,47 | ≈ 0,5 sur 150 | premier lancement de la validation de T0.4 : échec avant le clonage (jeton GitHub refusé) ; s'y ajoutent le disque de l'instance arrêtée (0,074 USD/h tant qu'elle existe) et le tirage de l'image (≈ 1 Go à 0,038 USD/Go) |

Devis approuvé : phase 0, plafond 150 USD, alerte à 120 USD (GO-2026-10-04-08, échéance 2026-11-01).

Cumul au 2026-10-04 11:26 UTC : 0 USD sur 150 (aucune instance créée).

## Engagements avant création d'instance

- 2026-10-04 18:02 UTC — validation de T0.4 sur modèle réel (GO-2026-10-04-08 ; procédure `docs/procedures/validation-T0.4-modele-reel-v1.md`, section 3). Une seule offre répond aux critères scellés :
  - offre 48704113 (machine 148671, hôte 214845) : H100 SXM, 80 Go ; CUDA maximale 13.3, pilote 610.57.04 ; vérifiée ; centre de données ; Tchéquie ; fiabilité 0,996 ; 129 Go de mémoire vive ; 24 cœurs effectifs ;
  - prix : 3,124 USD de l'heure tout compris, dont 0,074 USD de l'heure pour 80 Go de stockage ; téléchargement 0,038 USD par Go (environ 20 Go : modèle, roues), soit environ 0,8 USD ;
  - coût au plafond de 6 heures : 18,75 + 0,8 ≈ 19,6 USD ; plus environ 1,8 USD par jour tant que l'instance arrêtée est gardée (disque, gros tableaux), jusqu'au verdict ;
  - attendu : 1 à 2 heures, soit environ 4 à 7 USD ;
  - cumul engagé au plafond : 19,6 USD sur 150 (alerte à 120).
- 2026-10-04 18:12 UTC — instance 54183350 arrêtée après 0,15 heure ; plafond cumulatif de T0.4 : 0,15 heure consommée sur 6.
- 2026-10-05 08:28 UTC — relancement de la validation de T0.4 (procédure v2, GO-2026-10-04-08 ; feu vert de Lazar : « on a le budget, passe à la suite »). Cinq offres conformes ; la moins chère est retenue :
  - offre 29019328 (machine 30574) : A100 SXM4, 80 Go ; CUDA maximale 13.0, pilote 580.159.03 ; vérifiée ; centre de données ; Tchéquie ; fiabilité 0,9986 ; 129 Go de mémoire vive ;
  - prix : 1,093 USD de l'heure tout compris, dont 0,027 USD de l'heure de stockage ; téléchargement 0,039 USD par Go (≈ 20 Go, ≈ 0,8 USD) ;
  - reste du plafond cumulatif de T0.4 : 5,85 heures, soit au plus ≈ 6,4 + 0,8 ≈ 7,2 USD ; attendu : 1 à 2 heures, soit 1,1 à 2,2 USD ;
  - s'y ajoute le disque de l'instance 54183350, arrêtée (≈ 0,074 USD/h depuis le 2026-10-04 18:12 UTC) ;
  - cumul engagé au plafond : ≈ 0,5 + 7,2 + disque ≈ 9 USD sur 150.
