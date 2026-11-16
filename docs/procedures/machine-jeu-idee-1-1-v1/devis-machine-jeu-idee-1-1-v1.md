# Devis de la machine louée du jeu relancé de l'idée 1.1 — v1

- **Pour** : GO-2026-11-16-09, point (2) (« dépense sous sa propre ligne de type « calcul », … sur un devis écrit et contre-lu
  (ordre de grandeur 1 à 3 USD) ») ; procédure `procedure-machine-jeu-idee-1-1-v1.md` du même dossier.
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
| Échéance de la minuterie | 49 h 45 après l'impression de la ligne (bornes du lanceur : 49 h 30 à 50 h) | lanceur, amorce |
| Plafond de la ligne de GO proposé | **3.5 USD** (lu par la garde de dépense : cumul + une heure ≥ plafond → destruction) | ligne de GO à inscrire |

## 2. Durées

- Mise en place sur la machine : démarrage de l'image (382 664 644 octets compressés pour amd64, relevé sur Docker Hub à 20:49Z), installation de trois paquets, clone partiel du dépôt
  (≈ 2,9 Go d'arbre extrait au commit, plus son histoire sans contenus) : **15 à 30 minutes** (estimation, non une mesure ;
  à 100 Mb/s, 4 Go se descendent en ≈ 6 minutes).
- Contrôles avant jeu du lanceur (essais, dix-sept mutations, essais d'égalité) : **≈ 17 minutes** sur le conteneur
  (17:17:27Z à 17:34:28Z au run invalide ; addendum de relance 4.7).
- Jeu : **D = 15,667 h** mesurées sur le conteneur (addendum d'empreintes § 3 et § 5). Sur un autre processeur la durée
  peut différer (addendum de relance 4.10) ; elle est suivie chaque heure (`etat.txt`).
- Poussée des sorties (≈ 0,22 Go estimés par l'addendum de relance, 4.4) et fin : **≈ 5 à 10 minutes**.
- **Attendu : ≈ 16,7 h** de machine ; si le processeur est 1,5 fois plus lent : ≈ 24,4 h.

## 3. Coût

| Cas | Calcul | USD |
|---|---|---|
| Attendu, au prix relevé (0,0522) | 16,7 h × 0,0522 | **0,87** |
| Attendu, au prix garde maximal (0,06) | 16,7 h × 0,06 | 1,00 |
| Processeur 1,5 fois plus lent, au maximum | 24,4 h × 0,06 | 1,46 |
| Après la fin : machine arrêtée jusqu'à sa destruction par la session (12 h au plus, stockage seul) | 12 h × 0,01 | 0,12 |
| Départ manqué (aucune première poussée, destruction à 30 minutes) | 0,5 h × 0,06 | 0,03 |
| **Pire cas avec la minuterie** : la machine vit jusqu'à son échéance, 50 h au plus après l'impression | 50 h × 0,06 | **3,00** |
| Pire cas, plus 24 h arrêtée avant la destruction par la session | 3,00 + 24 h × 0,01 | **3,24** |
| Une relance permise (seulement si la première machine s'est arrêtée avant le jeu, ≤ 1 h) | + 1 h × 0,06 | ≤ 3,30 |

Le pire cas tient sous le plafond proposé de 3,5 USD (garde de dépense : arrêt et destruction dès que cumul + une heure
l'atteint). Le crédit n'est pas une contrainte (recharge automatique du loueur, seuil 5 USD, montant 5 USD, R-2996).

**Pourquoi 49 h 45 et non 48 h** : la borne dure du texte (48 heures murales) est comptée par le code **depuis
`depart.json`**, écrit après la mise en place et les ≈ 17 minutes de contrôles. Une minuterie de 48 h exactes depuis la
création couperait donc un jeu encore dans sa borne, sans `arret.json`. Avec 49 h 45 : l'amorce refuse de lancer le jeu si
l'échéance laisse moins de 48 h 40 ; un jeu qui passe sa borne est arrêté par son propre code (`arret.json`), et la minuterie
ne lui envoie TERM, par son PID, que 20 minutes avant l'échéance et seulement s'il a passé sa borne depuis la date de
`depart.json`. Le coût de ces 1 h 45 de plus au pire : 0,105 USD. Si la mère préfère 48 h exactes, il faut changer les
constantes du lanceur (`ECH_MIN`, `ECH_MAX`) et de l'amorce (`ECH_MIN`, `MARGE_JEU`) dans une v2 : nœud déclaré au rapport.

## 4. Ce que le devis ne couvre pas

- Une machine qui survivrait à sa minuterie et à l'arrêt demandé (le code ne juge jamais une destruction ; la session la
  prouve par la liste des instances).
- Une relance après un jeu commencé puis perdu (run invalide) : addendum neuf et devis neuf.
- Toute autre machine (B bis, pilote) : hors de cette ligne.
