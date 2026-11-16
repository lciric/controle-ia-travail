# Devis de la machine louée du jeu relancé de l'idée 1.1 — v2

- **Pour** : GO-2026-11-16-09, point (2) (« dépense sous sa propre ligne de type « calcul », … sur un devis écrit et contre-lu
  (ordre de grandeur 1 à 3 USD) »), et GO-2026-11-16-10 (écart D7 accepté ; même ordre de grandeur de 1 à 3 USD) ; procédure
  `procedure-machine-jeu-idee-1-1-v5.md` du même dossier.
- **Version** : v2 ; suit la v1 (`1ae229ebac9f14e729121b5d04bf04ac169d3eb3ad17909592924a63de62758a`) par les couples 5, 11,
  16 et 17 de la contre-lecture du tour 1 (`contre-lecture-machine-jeu-idee-1-1-tour1-v1.md`), demandés de nouveau aux tours 2
  et 3 (M1' point 2, M1'' point 2) ; par la minuterie de 49 h 45 acceptée par la mère (R-3026) ; et par le coût de la reprise
  de la poussée des sorties de l'amorce v2 (remarque facultative du tour 2), § 2 et § 4. Rien d'autre ne change.
- **Prix relevés hors ligne, aucune offre consultée** (consigne : aucun appel au loueur). Sources, au registre :
  - R-2961 (2026-11-16) : machine du pilote MR-2 v13, une carte inutilisée, **0,050 USD/h** ;
  - R-2968 (2026-11-16) : machine du pilote MR-2 v14, offre 50850386, une carte inutilisée, 12 processeurs, 16 Go,
    **0,0522 USD/h relu** ;
  - stockage : `storage_cost` de 0,1 à 0,4 USD par Go et par mois dans la recherche gardée de B bis
    (`/home/user/bbis-course-envoi-v3/recherche.json`, champs relevés seulement) : pour 20 Go, **0,003 à 0,011 USD/h**.
  Ces prix datent du jour et ne valent pas offre : la garde décide sur la recherche du moment (geste 4).

## 1. Bornes fixées dans les gardes

| Borne | Valeur | Où |
|---|---|---|
| Prix garde de l'offre (prix total de l'outil + stockage de 20 Go, compte double possible : sens sûr) | ≤ 0,06 USD/h | `garde_machine_jeu_idee_1_1_v1.py`, `PRIX_MAX_USD_H` |
| Stockage seul (facturé quand la machine est arrêtée) | ≤ 0,01 USD/h | `STOCKAGE_MAX_USD_H` |
| Prix relu après création | ≤ 0,06 USD/h, sinon destruction aussitôt | `prix-relu` |
| Machine | amd64, ≥ 4 cœurs effectifs, ≥ 8 000 Mo, ≥ 20 Go de disque, fiabilité ≥ 0,98, ≥ 100 Mb/s, avec ou sans carte | `fautes_offre_brute` |
| Échéance de la minuterie | 49 h 45 après l'impression de la ligne (bornes du lanceur : 49 h 30 à 50 h) ; acceptée par la mère (R-3026) | lanceur, amorce |
| Plafond de la ligne de GO proposé | **3.5 USD** (lu par la garde de dépense : cumul + une heure ≥ plafond → destruction) | ligne de GO à inscrire |
| Échéance de la ligne de GO proposée | **2026-11-22** au plus tôt (celle de GO-2026-11-16-09 et GO-2026-11-16-10) ; ne jamais la raccourcir : la garde de dépense relit la ligne à chaque appel horaire, et un jeu de 17 à 50 h plus un arrêt de 24 h tient sur trois dates civiles | ligne de GO à inscrire |

## 2. Durées

- Mise en place sur la machine : démarrage de l'image (382 664 644 octets compressés pour amd64, relevé sur Docker Hub à 20:49Z), installation de trois paquets, clone partiel du dépôt
  (≈ 2,9 Go d'arbre extrait au commit, plus son histoire sans contenus) : **15 à 30 minutes** (estimation, non une mesure ;
  à 100 Mb/s, 4 Go se descendent en ≈ 6 minutes).
- Contrôles avant jeu du lanceur (essais, dix-sept mutations, essais d'égalité) : **≈ 17 minutes** sur le conteneur
  (17:17:27Z à 17:34:28Z au run invalide ; addendum de relance 4.7).
- Jeu : **D = 15,667 h** mesurées sur le conteneur (addendum d'empreintes § 3 et § 5). Sur un autre processeur la durée
  peut différer (addendum de relance 4.10) ; elle est suivie chaque heure (`etat.txt`).
- Poussée des sorties (≈ 0,22 Go estimés par l'addendum de relance, 4.4) et fin : **≈ 5 à 10 minutes**.
- Trafic réseau (≈ 5 Go descendants, 0,3 Go montants) : facturé par certaines offres, non borné par la garde d'offre ; au plus 0,10 USD à 20 USD le téraoctet ; à relever sur l'offre retenue si l'outil donne son coût de trafic.
- **Reprise de la poussée des sorties** (amorce v2) : si une poussée des sorties échoue, la machine reste **vivante** et la
  reprend toutes les 5 minutes, jusqu'à 20 minutes avant l'échéance au plus ; reprises épuisées, elle s'arrête (« stopped »)
  et la minuterie la détruit à l'échéance. Ce temps est compris dans le pire cas de la minuterie (50 h) : **rien n'est ajouté
  au pire cas** (§ 3). Une reprise réussie au bout de quelques minutes ajoute ces minutes à l'attendu (0,06 USD/h).
- **Attendu : ≈ 16,7 h** de machine ; si le processeur est 1,5 fois plus lent : ≈ 24,4 h.

## 3. Coût

| Cas | Calcul | USD |
|---|---|---|
| Attendu, au prix relevé (0,0522) | 16,7 h × 0,0522 | **0,87** |
| Attendu, au prix garde maximal (0,06) | 16,7 h × 0,06 | 1,00 |
| Processeur 1,5 fois plus lent, au maximum | 24,4 h × 0,06 | 1,46 |
| Après la fin : machine arrêtée jusqu'à sa destruction par la session (12 h au plus, stockage seul) | 12 h × 0,01 | 0,12 |
| Départ manqué (aucune première poussée, destruction à 30 minutes) | 0,5 h × 0,06 | 0,03 |
| Poussée des sorties jamais acceptée : machine vivante jusqu'à l'échéance − 20 minutes (49 h 40 au plus après l'impression), puis arrêtée 20 minutes et détruite par la minuterie | 49,67 h × 0,06 + 0,33 h × 0,01 | ≤ 2,99 |
| **Pire cas avec la minuterie** : la machine vit jusqu'à son échéance, 50 h au plus après l'impression | 50 h × 0,06 | **3,00** |
| Pire cas, plus 24 h arrêtée avant la destruction par la session | 3,00 + 24 h × 0,01 | **3,24** |
| Une relance permise (seulement si la première machine s'est arrêtée avant le jeu, ≤ 1 h) | + 1 h × 0,06 | ≤ 3,30 |

Le pire cas des cas cumulés (3,24 à 3,30 USD) dépasse l'ordre de grandeur de 1 à 3 USD des deux GO ; l'attendu (0,87 USD) et le pire cas de la seule minuterie (3,00 USD) y tiennent ; le plafond de 3,5 USD est à faire accorder tel quel par Lazar. Le pire cas tient sous le plafond proposé de 3,5 USD (garde de dépense : arrêt et destruction dès que cumul + une heure
l'atteint). Le crédit n'est pas une contrainte (recharge automatique du loueur, seuil 5 USD, montant 5 USD, R-2996).

**Pourquoi 49 h 45 et non 48 h** (accepté par la mère, R-3026) : la borne dure du texte (48 heures murales) est comptée par
le code **depuis `depart.json`**, écrit après la mise en place et les ≈ 17 minutes de contrôles. Une minuterie de 48 h exactes
depuis la création couperait donc un jeu encore dans sa borne, sans `arret.json`. Avec 49 h 45 : l'amorce refuse de lancer le
jeu si l'échéance laisse moins de 48 h 40 ; un jeu qui passe sa borne est arrêté par son propre code (`arret.json`), et la
minuterie ne lui envoie TERM, par son PID, que 20 minutes avant l'échéance et seulement s'il a passé sa borne depuis la date de
`depart.json`. Le coût de ces 1 h 45 de plus au pire : 0,105 USD.

## 4. Ce que le devis ne couvre pas

- Une machine qui survivrait à sa minuterie et à l'arrêt demandé (le code ne juge jamais une destruction ; la session la
  prouve par la liste des instances).
- Une relance après un jeu commencé puis perdu (run invalide) : addendum neuf et devis neuf.
- Toute autre machine (B bis, pilote) : hors de cette ligne.
- **Trafic montant des reprises, cas extrême** : une poussée refusée **après** que le dépôt distant a reçu le paquet des
  sorties (≈ 0,22 Go) le fait renvoyer à chaque essai ; avec la reprise de l'amorce v2 (six essais par cycle d'environ
  13 minutes : trois pour les sorties, trois pour le journal), sur les ≈ 32 h qui séparent la fin du jeu de l'échéance
  − 20 minutes, cela ferait au plus ≈ 150 cycles × 6 × 0,22 Go ≈ 200 Go montants, soit ≈ 4 USD à 20 USD le téraoctet, hors
  de la garde de dépense (elle ne compte que les heures). Les causes ordinaires d'un refus (réseau coupé, jeton refusé,
  limite de débit) arrêtent la poussée avant l'envoi du paquet et ne coûtent rien de plus. À relever : le coût de trafic de
  l'offre retenue (ligne du trafic ci-dessus) ; et, sur « RESERVE : poussée des sorties impossible » au journal, la durée des
  reprises est un nœud de la mère (procédure, geste 13).
