# Passation de la session de formation du barreau 5 — 2026-11-20 10:55 UTC

Session `session_01QPDgKjCQYmTHUEjN63ThC8`. Fait suite à `passation-session-formation-2026-11-20-1005.md` (c2cb83e3…). Mère : `session_01QPDgKgejkqwnuaJHJ31Ydo` (confirmée à 10:06Z). Aucun score, aucune sortie de marche lue.

## Fait
- Signal de la mère à 10:40Z : mot de Lazar « recharge automatique seule », GO-2026-11-20-40 (vérifié sur `main`, 4a4adc03f). Cumul convenu avec la mère : heures × prix par instance, somme pour le commun.
- Six instances créées sous `GO_ID=GO-2026-11-19-86`, dans l'ordre 1, 2, 3, 4, 5, 7, crédit ≥ 5 USD vérifié avant chacune (outil `creer_b5f.sh` : crédit, recherche aux bornes du plan, choix mécanique `choisir_offre_b5f.py`, sous-commande `commande` du lanceur au commit 31fca83b, joueur à la ligne imprimée identique à l'octet, garde vérifiée sur le texte du joueur) :

| n | identifiant | offre | prix loueur (offre) USD/h | H (start_date) | run |
|---|---|---|---|---|---|
| 1 | 61624757 | 61617799 | 1,028 (0,988) | 10:42:47Z | 20261120-104209-b5f-formation-1 |
| 2 | 61624840 | 61617800 | 1,028 (0,988) | 10:43:20Z | 20261120-104306-b5f-formation-2 |
| 3 | 61624896 | 61617796 | 1,028 (0,988) | 10:43:41Z | 20261120-104329-b5f-formation-3 |
| 4 | 61624946 | 46608733 | 1,108 (1,068) | 10:44:02Z | 20261120-104350-b5f-formation-4 |
| 5 | 61625067 | 29019285 | 1,170 (1,122) | 10:45:05Z | 20261120-104450-b5f-formation-5 |
| 7 | 61625133 | 29019280 | 1,170 (1,122) | 10:45:52Z | 20261120-104539-b5f-formation-7 |

- Deux créations refusées par le loueur (« no_such_ask », offre périmée ; aucune instance) : 5 sur 46608733, 7 sur 49506599. Fichiers gardés sous le préfixe `essai1-` ; refaites sur une recherche neuve, nouveau run. Les offres déjà prises sont retirées du choix (`offres-utilisees.txt`).
- Étapes « B5F » à 10:47Z : minuteries lancées (échéances 1 → 2026-11-21T13:01:02Z ; 2 → 13:01:59Z ; 3 → 13:02:23Z ; 4 → 11:04:28Z ; 5 → 09:55:39Z ; 7 → 01:55:03Z), dépôt au commit de course, branches de sortie libres.
- Veille de plusieurs instances (`veille_b5f_multi.py`, pas de 600 s ; commun = somme des instances + 9,0 USD fixes pour l'instance 6). Garde de dépense du lanceur éprouvée avant : cas sain accepté (code 0), coupure de l'instance 1 et de l'instance 7, plafond commun refusés (code 2).
- Bloc-notes versé : `versement-bloc-notes-session-formation-v3/` (inventaire `inventaire-v3.tsv` ; listes du loueur, profil, réponses de création gardés hors du dépôt, inventoriés ; contrôle par programme : aucune valeur de clé dans les fichiers versés).

## Reste
- Veiller jusqu'à la fin de chaque instance ; à chaque fin : branche de sortie, preuve, `detruire`, joueur par l'identifiant, `verifier-destruction` (témoin 60988826). Écrire à la mère à chaque étape, arrêt et fin.
- Arrêt par le loueur à crédit nul : ne rien détruire, écrire à la mère.
- Ligne `SORTIES-FORMATION-B5F` à la fin de toutes les instances et de toute relance ; sel, table, `ENGAGEMENT-B5F` : sur le mot exprès de la mère seulement.

## Réserves
- Recharge automatique seule (5 USD sous 5 USD) pour ≈ 6,6 USD/h : une recharge manquée peut arrêter les machines sans versement (risque accepté par GO-2026-11-20-40).
- Le prix du loueur (stockage compris) sert au cumul ; il dépasse de 0,04 à 0,05 USD/h le prix de l'offre.

## Prochaine action
Relancer la veille si elle sort : `cd $S && PAS_VEILLE_S=600 python3 -I outils/veille_b5f_multi.py b5f/veille-conf.json b5f/veille-multi-etat.json b5f/veille-multi.txt` (S = bloc-notes de cette session). Codes : 10 étape → mère ; 20 fin/ARRET/SIGNAL → mère, puis preuve et destruction de l'instance finie, la retirer de `suivies` et y écrire `"fin"` (epoch) ; 30 refus de la garde, 40 hors marche, 50 loueur → ne rien détruire, mère.

## Instances en cours (10:55Z)
1 61624757, 2 61624840, 3 61624896, 4 61624946, 5 61625067, 7 61625133 : en marche. 58936096, 58936099, 58936100 intouchables ; 60988826 témoin. 61552174 (6) détruite.
