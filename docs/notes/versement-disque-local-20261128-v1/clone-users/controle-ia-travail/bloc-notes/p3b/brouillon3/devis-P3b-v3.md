# Devis de P3b (passe sur carte de la seconde lecture de P3) — v2

- Rédacteur neuf (Claude, sous-agent), brouillon 3, session 16, 2026-10-21 vers 01:32 UTC (heure vraie). Joint à
  `P3b-seconde-lecture-v1-brouillon3.md` (même dossier). Remplace pour la suite la v2 (`…/p3b/brouillon2/devis-P3b-v2.md`,
  `7dd3cfeeb25a7fbe27ac4f59098e4de3a14665a6d388e6d0ec994424ef1ddc78`, écrite vers 00:52 UTC le 2026-10-21), gardée telle
  quelle (R12), qui remplaçait la v1 (`…/p3b/brouillon1/devis-P3b-v1.md`, `77e46dc3…`). Changements du brouillon 3 :
  CR2-P3b-texte-07, -08 et -12, CR2-P3b-methode-04 et -06 (table `table-traitement-brouillon3-v1.md`).
- « P3 l. … » renvoie à `prereg/P3-premier-test-i-a-v1.md` (`d975e981…`).
- Toutes les durées sont des **estimations des rédacteurs**, non mesurées : aucun pilote, aucune donnée de P3 ouverte. À
  recaler avant le scellement (questions ouvertes, Q-12). Les postes ajoutés par le brouillon 2 sont marqués « estimation ».
- Cadre : délégation R-217 prolongée (GO-2026-10-20-07) : **10 USD au plus par lancement**, un lancement à la fois, dans le
  plafond de la phase (GO-2026-10-04-08 prolongé par GO-2026-10-20-06 : 150 USD, alerte à 120 USD). GO-2026-10-20-11 (nuit du
  20 au 21 octobre) ne s'applique que si le lancement a lieu avant son échéance ; ce devis n'en a pas besoin.

## 1. En une ligne

**≈ 1,25 à 1,95 heure de carte A100 SXM4 80 Go (≈ 1,35 à 2,25 avec la lentille jacobienne), soit ≈ 1,4 à
2,1 USD (≈ 1,5 à 2,5) à 1,09 USD de l'heure (plus téléchargement et disque,
bornés au § 4) ; borne par lancement 7,5 USD (Version de repli (B) de P-024 : 8,6 USD) ; tout le reste sur processeur,
0 USD.**

## 2. Carte et offre

- Type : A100 SXM4 80 Go sur AMD EPYC 7513, une carte (filtre de P3, l. 352-358) : au plus 1,30 USD de l'heure, au moins
  16 cœurs effectifs, au moins 128 000 Mo de mémoire vive, téléchargement au plus 0,05 USD par Go, stockage au plus
  0,03 USD de l'heure ; l'offre conforme la moins chère est prise à la création.
- Prix retenu : **1,09 USD de l'heure** environ (offres conformes relevées de 1,08 à 1,2133 USD de l'heure,
  `registres/depenses.md` l. 76 ; P3 à 1,0889, l. 88 ; registre relu à l'empreinte `f4d6ee90…`). Facturé au-delà de la
  carte : pour P3, 4,71 USD (l. 90) pour ≈ 3,96 USD de carte (l. 88) ; l'écart vient du téléchargement et du disque de
  l'instance gardée arrêtée, il est borné au § 4.

## 3. Heures de carte, par poste (version (A) de la partition : 60 tâches, 240 épisodes)

| poste | heures (estimation) | base de l'estimation |
|---|---|---|
| démarrage, clonage, installation | ≈ 0,05 | P3 l. 382 : installation ≈ 99 s au pilote |
| suite complète des tests sur l'instance, comme P3 (Q-11) | ≈ 0,45 | P3 l. 383-384 : 1 603 s pour la suite complète au commit du code de P3 |
| téléchargement et chargement du modèle (≈ 16 Go) | ≈ 0,1 | estimation |
| contrôle positif de la lentille, items (i) à (iv) (200 items courts) | ≈ 0,05 | 200 passes de moins de 100 jetons |
| contrôle positif, items (v) « motif de transformation » : 200 passes courtes de plus | ≈ + 0,05 | estimation (brouillon 2, CR-P3b-methode-06) |
| contrôle positif, items (vi) « valeur calculée absente du contexte » : 200 passes courtes de plus | ≈ + 0,05 | estimation (brouillon 3, CR2-P3b-methode-04) |
| reconstitution et passes avant (240 épisodes, 32 couches gardées en mémoire, extraction aux positions utiles), critère d'épisode et propagation | ≈ 0,15 à 0,5 | estimation : une passe de quelques milliers à ≈ 16 000 jetons par épisode, plus le transfert des états ; aucune génération (pilote de T0.5 cité par P3 l. 385 : ≈ 38 s par épisode **avec** génération) ; la recherche conjointe des jetons de fin (au plus 10⁶ combinaisons par épisode) porte sur des empreintes de texte, sans passe |
| contrôle négatif de la tolérance (≈ 5 % des actions, une passe partielle chacune) | ≈ + 0,05 à 0,1 | estimation, à recaler (Q-12) (brouillon 2, CR-P3b-methode-03) |
| gardes de reconstitution, scores localisés (2 sondes principales, 400 sondes de plancher, 424 sondes légères pour la garde) | ≈ 0,05 | produits de matrices sur la carte, comme la notation de P3 |
| oracle : choix (15 réglages × 5 plis), validation croisée (5 plis), 200 répliques du plancher ; placebo et loi nulle sans réapprentissage | ≈ 0,1 à 0,25 | ≈ 16 000 résolutions de systèmes de taille au plus ≈ 2 100, double précision, noyaux calculés une fois par bande ; placebo et loi nulle : nouvelles notations seules, négligeables |
| lentille des logits : 2 400 actions × 32 couches, plus 200 rotations par couche (logits restreints à 2 identifiants par action), drapeaux d'amorçage | ≈ 0,05 à 0,2 | estimation ; les drapeaux se lisent sur les identifiants, sans passe |
| lentille jacobienne, si présente (téléchargement ≈ 1 à 2 Go ; un produit 4 096 × 4 096 par état et par rotation) | + 0,1 à 0,3 | estimation ; poste retiré si le fichier manque |
| écriture, contrôle des fichiers, poussée | ≈ 0,1 | P3 et P4 |
| **total** | **≈ 1,25 à 1,95 (1,35 à 2,25 avec la lentille jacobienne)** | — |

Version de repli (B) de P-016 (40 tâches lues, 160 épisodes) : passes et lentille réduites d'un tiers ; total ≈ 1,15 à 1,75 h (≈ 1,25 à 1,95 avec la lentille jacobienne).

## 4. Dollars

- Au prix de 1,09 USD de l'heure : ≈ 1,4 à 2,1 USD de carte (≈ 1,5 à 2,5 avec la lentille jacobienne), plus téléchargement et disque (bornés ci-dessous).
- **Borne par lancement : 7,5 USD**, sous les 10 USD de la délégation :
  - surveillance de la session à la création + 14 400 s, au prix plafond : 4 h × 1,30 = 5,20 USD ;
  - arrêt en dix minutes : 0,22 USD ;
  - téléchargement au plus 20 Go à 0,05 USD par Go : 1,00 USD ;
  - stockage, si l'instance doit être gardée arrêtée après un refus de poussée : au plus 24 h × 0,03 = 0,72 USD (garde
    bornée à 24 heures, puis destruction par identifiant, sauf GO de Lazar qui la prolonge : dépense nouvelle, consignée) ;
  - somme : 7,14 USD, arrondie à 7,5 USD. Au-delà : arrêt de l'instance par son identifiant (R10).
- **États à t_cost. [Décision de Lazar en attente : P-024 ; défaut (A) le 2026-10-23 vers 00:30 UTC ; recommandation (A),
  confiance ≈ 60 %]** Version (A), écrite ci-dessus : états détruits avec l'instance après une récupération conforme ; aucun
  poste de plus. Version de repli (B) de P-024 : « instance gardée arrêtée, disque seul, jusqu'au verdict R13 scellé,
  72 heures au plus : stockage au plus 72 × 0,03 = 2,16 USD, qui remplace le poste de 24 heures ; somme 5,20 + 0,22 + 1,00 +
  2,16 = 8,58 USD, **borne 8,6 USD**, sous les 10 USD de la délégation ; crédit exigé à la création porté à 4,5 h × (prix de
  l'offre + autres projets en marche) + 1,2 USD + 2,16 USD. » Version de repli (C) de P-024 : « états versés au dépôt privé :
  ≈ 1,3 Go de poussée de plus, dans le temps du poste « écriture, contrôle des fichiers, poussée » (estimation : + 0,05 h) ;
  borne inchangée. »
- Crédit exigé à la création : 4,5 h × (prix de l'offre + autres projets en marche) + 1,2 USD, soit 7,05 USD au prix plafond
  sans autre projet ; le compte est à recharge automatique (R-283).
- Dépense cumulée de la phase : à relire dans `registres/depenses.md` avant la ligne d'accord ; la chaîne refait la somme sous
  la forme de P4 : « dépense consignée X USD + borne 7,50 USD = Y USD < 150 USD », alerte à 120 USD.

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
- Mesure de conception avant le scellement : puissance à 40 et 60 tâches (M-P3b-1), sur les entrées publiées par le verdict
  complété de P3. M-P3b-2 (reconstitution sur processeur) n'est pas une mesure de conception : c'est un contrôle avant
  dépense, après le scellement ; elle lit, pour les tâches lues seulement, les textes gardés, `jetons` et `jetons_notes` de
  `scores-p3.npz`, les bornes gardées et l'empreinte de trajectoire des fiches, aucune activation, aucun score de sonde. **[Décision de Lazar en attente : N-032 ; aucun défaut : sans réponse,
  rien n'est compté avant le scellement, ce qui revient à (C) ; ce paragraphe écrit l'option (C), recommandée]** Version de
  repli (A) de N-032 : « M-P3b-2 avant le scellement, par condition : épisodes des tâches lues rejoués exactement et actions
  reconstituées selon (a) à (c) avec propagation ; lit les textes gardés, `jetons`, `jetons_notes`, les bornes gardées et
  l'empreinte de trajectoire des fiches, aucune activation,
  aucun score de sonde ; sortie brute scellée. » Version de repli (B) de N-032 : « …si Lazar l'admet (M-P3b-2, Q-03, nœud) :
  lit les textes gardés et `jetons_notes` de `scores-p3.npz`, aucune activation, aucun score de sonde ; un seul compte,
  toutes conditions confondues, tâches lues seulement. »
- Bancs de la chaîne et répétition jouet (modèle jouet, tokeniseur par caractères, textes synthétiques avec chaîne canari).
- Lecture décisive (`lecture_p3b_v1.py`) sur les fichiers poussés : aires, 2 000 tirages par jeu, planchers de 200,
  régressions croisées (deux spécifications), réserves reprises de l'addendum 1, double comptabilité : ≈ 10 à 30 minutes
  (estimation).
- Contre-lectures, verdict R13 : sous-agents neufs, sans calcul payant.

## 7. Ce que ce devis ne couvre pas

- Réajustement de la lentille jacobienne sur le 8B (permis par GO-2026-10-20-10, coût non mesuré : préenregistrement
  complémentaire et devis séparé).
- Sonde de valeur, rejeu contrefactuel, manipulation du nombre écrit (P-017 (B), (C), (C′)), P3c, bras « moyenne », question
  ajoutée après l'action : hors périmètre.
- Tout relancement, toute passe nouvelle pour réapprendre l'oracle : nœud de Lazar.
