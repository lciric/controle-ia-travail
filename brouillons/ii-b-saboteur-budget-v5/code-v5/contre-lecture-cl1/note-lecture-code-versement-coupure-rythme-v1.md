# Note — lecture du code au commit de lancement 43d6d067 : versement, coupure, rythme — v1

Date : 2026-11-22. Lecture du code seulement (`git show 43d6d067:<chemin>`) ; aucun fichier de `diag/`, `donnees/`, `runs/` ni `traces/` n'a été lu.

**(1) Pas de poussée par lot.**
- `lanceur_v5.phase_etalonnage` (fonction `verser`) ne fait qu'écrire et sceller chaque lot sur le disque de la machine, sous `diag/<run>/lots/` et `donnees/<run>/lots/`.
- L'amorce (`scripts/amorce_instance_iib_v5.sh` à 43d6d067) ne pousse qu'à cinq moments :
  - la poussée initiale de la branche (l. 349) ;
  - la fin normale du run (l. 433-466) ;
  - la sortie en erreur du lanceur, avec ou sans `arret.json` (l. 419-429, `consigner_arret`) ;
  - la minuterie, à dépense épuisée (55) ou à l'échéance (l. 84 et 91) ;
  - un second démarrage (l. 182-196).
  
  « Versé par lot et poussé » (ordre, § 3 et § 7) est donc faux pour la poussée. C'était la forme de M1 dans ma contre-lecture, et je ne l'ai pas relevé à la vérification.

**(2) À la coupure à 12 USD**, c'est l'exécutante qui arrête la machine par son identifiant (`lancer_iib_v3.sh` l. 440) : aucune consignation n'est garantie, et la branche reste au commit de lancement.
- Ce qui reste : les lots scellés sur le **disque de la machine arrêtée**.
- Pour les pousser, il faut redémarrer la machine. L'amorce voit alors le dépôt déjà extrait et prend le chemin « redémarrage d'un run interrompu » (l. 195-196) : elle consigne et pousse `runs`, `diag` et les identifiants (`consigner_partiel`, l. 304-312), puis **refuse et demande la destruction** (`refus`, l. 121 et 196). Il faut le mot de la mère, puisque l'ordre interdit toute relance et toute destruction sans lui.
- **Un étalonnage coupé n'est pas exploitable.** `etalonnage-oracles-iib-v5.json` n'est écrit qu'à la fin de `phase_etalonnage`. Sans lui, `phase_conditions` s'arrête sur une garde : `verifier` lève « fichier absent » (`scellement.py` l. 80-81, `lanceur_v5.py` l. 346-350). Aucun code n'assemble les lots, si bien qu'aucune issue scellée n'est écrite, ni « non calculable » ni « ne part pas ».
- Sur le fond, ce serait « non calculable » (texte 10.3, étape 1 : moins de 64 épisodes), d'autant que les flagrants sont joués en dernier (`lanceur_v5.py`, boucle `plan_f`).

**(3) Rythme.** Le devis annonce environ 6,6 minutes par lot à deux oracles (8 × 39 s de génération, plus 160 actions × 0,511 s) et 41 s pour 80 actions de l'oracle seul. Les durées observées sont 5 à 7 fois plus longues :
- 5 minutes pour les plantés, soit environ 3,75 s par action ;
- 34 minutes pour les régénérés ;
- 51 minutes pour le premier lot, chargement compris.

Le ralentissement est à peu près **uniforme sur la génération et sur l'oracle**.
- **Je ne trouve aucun réglage faux dans le code** : réglages du modèle égaux à ceux de la première course (`configuration_v5.MODELE_REEL` : bfloat16, cuda, sdpa ; forme du lot des suites `cache_duplique`) ; lot de 8, 400 jetons au plus par action, 16 jetons au plus par suite, prérempli unique dupliqué pour les huit suites (`modele_v1.py` l. 61-96). Les correctifs 0011 et 0012 ne touchent ni le modèle ni l'environnement du run.
- Deux causes possibles, à éprouver sans lire de sortie :
  - **(a)** dans les deux boucles, l'échantillonnage se fait **jeton par jeton sur le processeur** (`logits[:, -1].to("cpu", float32)`, puis une loi sur 128 000 jetons par ligne : `harnais/episode.py` l. 111-119, `modele_v1.py` l. 79-84). La vitesse dépend donc du processeur de l'hôte : un hôte plus lent que celui de la première course ralentit tout uniformément. C'est la cause compatible avec ce qu'on voit ; l'exécutante peut regarder l'utilisation de la carte et du processeur.
  - **(b)** un repli de `cache_duplique` vers `prerempli_par_suite` (`modele_v1.py` l. 101-108) ne ralentirait que l'oracle. Or **la version 5 n'écrit nulle part `modele.replis`** : un tel repli serait silencieux. C'est un défaut à corriger, mais il n'explique pas la lenteur de la génération.
