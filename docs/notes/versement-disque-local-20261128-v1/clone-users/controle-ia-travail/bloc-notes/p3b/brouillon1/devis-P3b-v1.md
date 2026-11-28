# Devis de P3b (passe sur carte de la seconde lecture de P3) — v1

- Rédacteur neuf (Claude), brouillon 1, 2026-10-20 vers 23:45 UTC. Joint à `P3b-seconde-lecture-v1-brouillon1.md` (même
  dossier). Toutes les durées sont des **estimations du rédacteur**, non mesurées : aucun pilote, aucune donnée de P3 ouverte.
  À recaler avant le scellement (questions ouvertes, Q-12).
- Cadre : délégation R-217 prolongée (GO-2026-10-20-07) : **10 USD au plus par lancement**, un lancement à la fois, dans le
  plafond de la phase (GO-2026-10-04-08 prolongé par GO-2026-10-20-06 : 150 USD, alerte à 120 USD). GO-2026-10-20-11 (nuit du
  20 au 21 octobre) ne s'applique que si le lancement a lieu avant son échéance ; ce devis n'en a pas besoin.

## 1. En une ligne

**≈ 1,2 à 2,1 heures de carte A100 SXM4 80 Go, soit ≈ 1,3 à 2,3 USD à 1,09 USD de l'heure (≈ 1,6 à 2,8 USD facturés avec
≈ 20 % de frais) ; borne par lancement 7,5 USD ; tout le reste sur processeur, 0 USD.**

## 2. Carte et offre

- Type : A100 SXM4 80 Go, une carte, même filtre que P3 (préenregistrement de P3, l. 352-358) : au plus 1,30 USD de l'heure,
  au moins 16 cœurs effectifs, au moins 128 000 Mo de mémoire vive, téléchargement au plus 0,05 USD par Go, stockage au plus
  0,03 USD de l'heure ; l'offre conforme la moins chère est prise à la création.
- Prix retenu pour l'estimation : **1,09 USD de l'heure** environ (consigne ; relevés A100 80 Go de 1,09 à 1,21 USD de
  l'heure cités par la réponse au prompt unique, `registres/depenses.md` l. 80-88, non relus ici).
- Frais : ≈ 20 % au-dessus du prix de la carte (même source : P3 entier ≈ 3,64 h, ≈ 3,96 USD de carte, 4,71 USD facturés).

## 3. Heures de carte, par poste (version (A) de la partition : 60 tâches, 240 épisodes)

| poste | heures (estimation) | base de l'estimation |
|---|---|---|
| démarrage, clonage, installation | ≈ 0,05 | P3 l. 382 : installation ≈ 99 s au pilote |
| suite des tests sur l'instance | ≈ 0,45 (complète) ou ≈ 0,1 (sous-ensemble) | P3 l. 383-384 : 1 603 s pour la suite complète au commit du code de P3 ; choix en Q-11 |
| téléchargement et chargement du modèle (≈ 16 Go) | ≈ 0,1 | estimation |
| contrôle positif de la lentille (200 items courts) | ≈ 0,05 | 200 passes de moins de 100 jetons |
| reconstitution et passes avant (240 épisodes, 32 couches gardées en mémoire, extraction aux positions utiles) | ≈ 0,15 à 0,5 | estimation : une passe de quelques milliers à ≈ 16 000 jetons par épisode, plus le transfert des états ; aucune génération (P3 : ≈ 38 s par épisode **avec** génération, l. 385) |
| gardes de reconstitution, scores localisés (2 sondes principales, 400 sondes de plancher, 424 sondes légères pour la garde) | ≈ 0,05 | produits de matrices sur la carte, comme la notation de P3 |
| oracle : choix (15 réglages × 5 plis), validation croisée (5 plis), 200 répliques du plancher | ≈ 0,1 à 0,25 | ≈ 16 000 résolutions de systèmes de taille au plus ≈ 2 100, double précision, noyaux calculés une fois par bande |
| lentille des logits : 2 400 actions × 32 couches, plus 200 rotations par couche (logits restreints à 2 identifiants par action) | ≈ 0,05 à 0,2 | estimation |
| lentille jacobienne, si présente (téléchargement ≈ 1 à 2 Go ; un produit 4 096 × 4 096 par état et par rotation) | + 0,1 à 0,3 | estimation ; poste retiré si le fichier manque |
| écriture, contrôle des fichiers, poussée | ≈ 0,1 | P3 et P4 |
| **total** | **≈ 1,2 à 2,1** (≈ 0,85 à 1,75 avec le sous-ensemble des tests) | — |

Version (B) de la partition (40 tâches lues, 160 épisodes) : passes et lentille réduites d'un tiers ; total ≈ 1,1 à 1,8 h.

## 4. Dollars

- Au prix de 1,09 USD de l'heure : ≈ 1,3 à 2,3 USD ; facturés avec ≈ 20 % de frais : ≈ 1,6 à 2,8 USD.
- **Borne par lancement : 7,5 USD**, sous les 10 USD de la délégation :
  - surveillance de la session à la création + 14 400 s, au prix plafond : 4 h × 1,30 = 5,20 USD ;
  - arrêt en dix minutes : 0,22 USD ;
  - téléchargement au plus 20 Go à 0,05 USD par Go : 1,00 USD ;
  - stockage, si l'instance doit être gardée arrêtée après une récupération non conforme : au plus 24 h × 0,03 = 0,72 USD ;
  - somme : 7,14 USD, arrondie à 7,5 USD. Au-delà : arrêt de l'instance par son identifiant (R10).
- Crédit exigé à la création : 4,5 h × (prix de l'offre + autres projets en marche) + 1,2 USD, soit 7,05 USD au prix plafond
  sans autre projet ; le compte est à recharge automatique (R-283, d'après la revue v4).
- Dépense cumulée de la phase : à relire dans `registres/depenses.md` avant la ligne d'accord (non lue ici) ; la chaîne refait la
  somme sous la forme de P4 : « dépense consignée X USD + borne 7,50 USD = Y USD < 150 USD », alerte à 120 USD.

## 5. Bornes de durée (reliées aux constantes des scripts par les contrôles avant dépense)

- Passe (`duree_max_s`) : 7 200 s depuis le début du module, relue à chaque épisode, à chaque réplique de l'oracle et à chaque
  couche de la lentille.
- Délai externe de la passe : 150 minutes (TERM converti en arrêt consigné, KILL cinq minutes plus tard).
- Plafond de l'amorce (installation, tests, passe, poussées) : 210 minutes.
- Surveillance de la session : création + 14 400 s, puis arrêt par identifiant (R10). Marge entre la surveillance et le KILL de
  l'amorce : au moins 25 minutes.
- Contrôle à cinq minutes : forme de la chaîne v2 de P4 (offre, prix, stockage, téléchargement, étiquette).

## 6. Ce qui tourne sur processeur (0 USD)

- Écriture du code et des tests sous `docs/procedures/P3b-v1/`, suite complète dans l'environnement de la session au commit S.
- Mesures de conception avant le scellement : puissance à 40 tâches (M-P3b-1) ; comptes de tokenisation des textes gardés, si
  Lazar l'admet (M-P3b-2, Q-03) ; aucune de ces mesures ne lit une activation ni un score.
- Bancs de la chaîne et répétition jouet (modèle jouet, tokeniseur par caractères, textes synthétiques avec chaîne canari).
- Lecture décisive (`lecture_p3b_v1.py`) sur les fichiers poussés : aires, 2 000 tirages par jeu, planchers de 200,
  régressions croisées, double comptabilité : ≈ 10 à 30 minutes (estimation).
- Contre-lectures, verdict R13 : sous-agents neufs, sans calcul payant.

## 7. Ce que ce devis ne couvre pas

- Réajustement de la lentille jacobienne sur le 8B (permis par GO-2026-10-20-10, coût non mesuré : devis séparé).
- Sonde de valeur, rejeu contrefactuel, P3c, bras « moyenne », question ajoutée après l'action : hors périmètre.
- Tout relancement : nœud de Lazar.
