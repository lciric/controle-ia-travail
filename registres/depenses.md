# Registre des dépenses

Aucune dépense sans GO sur devis. Alerte à Lazar à 80 % d'un devis approuvé.

| date | GO | devis | instance (identifiant) | type | heures | coût (USD) | cumul sur devis | note |
|---|---|---|---|---|---|---|---|---|
| 2026-10-04 | GO-2026-10-04-08 | phase 0 (T0.4) | 54183350 | carte H100 SXM, à la demande (3,124 USD/h tout compris) | 0,15 (18:03 → 18:12) | ≈ 0,47 | ≈ 0,5 sur 150 | premier lancement de la validation de T0.4 : échec avant le clonage (jeton GitHub refusé) ; s'y ajoutent le disque de l'instance arrêtée (0,074 USD/h tant qu'elle existe) et le tirage de l'image (≈ 1 Go à 0,038 USD/Go) |
| 2026-10-05 | GO-2026-10-04-08 | phase 0 (T0.4) | 54285455 | carte A100 SXM4, à la demande (1,093 USD/h tout compris) | 0,04 (08:28:54 → 08:31:20) | ≈ 0,05 | ≈ 0,55 sur 150 (plus les disques) | relancement de la validation de T0.4 : même échec avant le clonage (jeton GitHub refusé) ; disque de l'instance arrêtée : ≈ 0,027 USD/h tant qu'elle existe |
| 2026-10-05 | GO-2026-10-04-08 | phase 0 (T0.4) | 54298522 | carte A100 SXM4, à la demande (1,093 USD/h tout compris) | 0,22 (10:18:07 → 10:31:03) | ≈ 0,24 | ≈ 0,8 sur 150 (plus les disques) | troisième lancement : clonage, mise en place, 178 tests, run A arrêté en phase de logique (P2 non concluant) ; téléchargement du modèle (≈ 16 Go) et des roues ; disque de l'instance arrêtée ≈ 0,027 USD/h |

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
- 2026-10-05 08:31 UTC — instance 54285455 arrêtée après 0,04 heure ; plafond cumulatif de T0.4 : 0,19 heure consommée sur 6 (reste 5,81).
- 2026-10-05 10:17 UTC — troisième lancement de la validation de T0.4 (procédure v2, GO-2026-10-04-08), après la correction du jeton GitHub déclarée par Lazar (« c'est fait », N-009). Trois offres conformes ; la moins chère retenue : 29019328 (machine 30574), A100 SXM4 80 Go, CUDA maximale 13.0, pilote 580.159.03, 1,093 USD/h tout compris ; reste du plafond cumulatif : 5,81 heures, soit au plus ≈ 6,4 + 0,8 ≈ 7,2 USD ; attendu 1 à 2 heures (1,1 à 2,2 USD).
- 2026-10-05 10:31 UTC — instance 54298522 arrêtée après 0,22 heure ; plafond cumulatif de T0.4 : 0,41 heure consommée sur 6 (reste 5,59).
- 2026-10-05 12:05 UTC — sonde de mémoire de la version 2 de T0.4 (non décisive : chargement en double précision et charge de la phase de logique au pire cas ; mémoire et durées seulement), sous GO-2026-10-04-08, avant le préenregistrement v2 (le choix de la carte en dépend). Offre 49506600 (machine 149396) : A100 SXM4 80 Go, CUDA 13.2, pilote 595.71.05, vérifiée, 129 Go de mémoire vive, 1,08 USD/h. Attendu : environ 15 minutes, ≈ 0,3 USD ; plafond de la sonde : 40 minutes (≈ 0,7 USD) ; compté dans le budget de carte de T0.4 (reste 5,59 heures).
- 2026-10-05 12:14 UTC — instance 54311651 (sonde de mémoire) arrêtée après 0,146 heure (12:05:41 → 12:14:25), ≈ 0,16 USD ; plafond cumulatif de T0.4 : 0,56 heure consommée sur 6 (reste 5,44). Disques des quatre instances arrêtées facturés jusqu'à leur destruction (décision de Lazar, N-009).
- 2026-10-05 14:44 UTC — lancement de la validation de T0.4, version 2 (préenregistrement v2 scellé 886c8c07…, procédure v3, GO-2026-10-04-08). Recherche archivée et scellée : `traces/t04-offres-20261005-144349/` (4 offres conformes). Offre retenue, la moins chère : 47386263, H200 NVL 140,4 Gio, CUDA 13.0, pilote 580.95.05, 189 Go de mémoire vive, fiabilité 0,9973, vérifiée, en centre de données ; **4,441 USD/h** tout compris pendant la marche ; stockage ≈ 0,69 USD par Go et par mois (≈ 1,85 USD par jour pour 80 Go, facturé tant que l'instance existe) ; téléchargement ≈ 0,038 USD par Go (modèle ≈ 16 Go, ≈ 0,6 USD).
  - reste du plafond cumulatif de T0.4 : 5,44 heures, soit au plus ≈ 24,2 + 0,6 ≈ 24,8 USD ; attendu : 1 à 1,5 heure, soit 4,4 à 6,7 USD ;
  - cumul engagé au plafond : ≈ 1,0 + 24,8 USD, plus les disques, sur 150 (alerte à 120).
- 2026-10-05 14:55 UTC — instance 54332340 arrêtée après 0,179 heure (14:44:22 → 14:55:07), ≈ 0,80 USD de marche plus ≈ 0,6 USD de téléchargement ; plafond cumulatif de T0.4 : 0,74 heure consommée sur 6 (reste 5,26). Cumul de la phase 0 ≈ 2,4 USD plus les disques des cinq instances arrêtées (≈ 1,85 USD par jour pour la H200 NVL).
