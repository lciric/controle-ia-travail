# Note de conception — simulation S1 de la courbe de la chaîne complète : la chaîne sans agents sur les mondes W_λ — v1

10 novembre 2026, ≈ 11:12 UTC. Session « attaquant informé ». Écrite et scellée **avant** le run. C'est un calcul de
dimensionnement, pas une expérience décisive : il ne porte aucune hypothèse ni aucun signe, et ne dit rien des agents. Il
fournit au préenregistrement de la courbe (`preenregistrement-courbe-chaine-complete-v1-brouillon2.md`, `df311ffe…`) les
valeurs g(λ) (<<G_LAMBDA>>) et la courbe du juge seul attendue (<<COURBE_JUGE_ATTENDUE>>), et dit si la grille de λ doit se
resserrer.

## Code employé

- Copie empreintée du code de l'organisme au commit `94bfd92` (53 fichiers), versée par la session de dépôt :
  - branche `claude/upbeat-cray-dmauvv`, commit `8668f0ae` ;
  - dossier `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/` ;
  - empreintes `empreintes-copie-v1.txt` (`0153e02d…`), toutes vérifiées le 10 novembre à 11:08 UTC, 53 sur 53 conformes.
- Le code est importé tel quel depuis une extraction hors du dépôt, et rien n'y est écrit. Fonctions employées :
  - `a_blanc_v59.charger_monde` et `juger_carte`, sous le nul v8, avec 200 tirages frais ;
  - `selection_pari.proba`, `tirer_instances` et `tirer_categorie` ;
  - `boucle_fermee_v59.graine_de_tache` ;
  - `oracle_tour_ferme_v60.Oracle.mesurer`.
- Le script reprend la logique du script de puissance de la plus petite course
  (`docs/notes/organisme-boucle-reelle-v1/puissance-boucle-reelle-v1.py`, `a2afcdd3…`) et l'ajustement de K1
  (`essai-a-blanc-v1/ajuster_k1_v1.py`).

## Dessin

- **Mondes** : W_λ est la loi S-V1 dont les poids du trait z1 sont multipliés par λ. Grille de dimensionnement, plus fine que
  la grille du préenregistrement pour voir où la chaîne bascule : λ = 0 ; 0,1 ; 0,2 ; 0,25 ; 0,3 ; 0,4 ; 0,5 ; 0,75 ; 1.
- **Archive** : K1_λ, la meilleure loi softmax du seul trait z0 sous W_λ, ajustée une fois par dose au maximum de
  vraisemblance attendue sur les 4 000 instances de l'oracle, comme K1, et arrondie à 6 décimales.
- **Dose en unités de l'oracle** : g(λ) = gain de W_λ au-delà de {K1_λ} (`delta_gain_nat`).
- **Lois jugées à chaque répétition**, en proposeurs scriptés, avec l'archive {K1_λ} :
  - W, la loi du monde elle-même : un proposeur qui trouverait la loi exacte ;
  - V2, la part du seul trait z1 de W_λ (poids de z1 multipliés par λ, biais de S-V1) : un proposeur qui ne trouverait que
    le trait nouveau ;
  - F1, une copie renommée de K1_λ ;
  - F2, le mélange 0,8 K1_λ + 0,2 uniforme : deux fausses de la classe couverte.
- **Promotion** : promue par le juge, avec un log e au moins égal à log(22/0,05) (règle « hors famille », m = 22 comme dans
  la plus petite course).
- **Test de mort** : la statistique gelée sur une tranche de 400 épisodes de W_λ, au seuil de 0,02 nat.
- **Classement par l'oracle** : une vraie découverte doit avoir un gain d'au moins 0,02 et un gain au-delà de l'archive d'au
  moins 0,02.
- **Répétitions** : 200 par dose. Graines : racine `numpy.random.SeedSequence(20261111)`, un enfant par couple (dose,
  répétition) ; tâches dérivées par `graine_de_tache`. L'oracle et l'ajustement de K1_λ ont une racine fixe, l'enfant
  `spawn_key = (10**6,)`.

## Sorties

Par dose :
- g(λ) ;
- part des répétitions où W, puis V2, est promue puis survivante, avec son intervalle de Wilson ;
- part où F1 ou F2 est promue ;
- médiane du log W maximal.

## Ce que le calcul décide

- Les valeurs g(λ) écrites au préenregistrement.
- La courbe du juge seul attendue (témoin de dose, P3 du préenregistrement).
- La grille : si la chaîne passe de 0 à 1 entre deux doses de la grille du préenregistrement (0 ; 0,25 ; 0,5 ; 0,75 ; 1),
  sans point entre elles, le brouillon 3 propose de resserrer la grille vers ces doses.

Ce calcul ne dit rien de la probabilité qu'un proposeur réel trouve la loi : c'est ce que la courbe mesurera.
