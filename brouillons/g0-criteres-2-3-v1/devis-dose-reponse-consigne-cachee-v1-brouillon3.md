# Devis — course de dose–réponse de l'organisme à consigne cachée (partie (i) du critère 2 de la porte G0) — v1 — brouillon 3

Pièce de classe A, jointe au préenregistrement `T0.6-organisme-consigne-cachee-dose-reponse-v1-brouillon3.md`. Écrite le 2026-11-24 par la session fille de conception `session_01Qi7Gr4GahKn8qRTN5FTWv3` ; brouillon 2 (`68201f2731348a1af7c8dddfd842ed43e18144322ff6e71d04a582bb42de4b30`) corrigé après la vérification 1 (constat V1-08) et après le message de la mère du 24 novembre (les deux témoins instruits du premier test s'ajoutent : quinze conditions, 1 920 épisodes au lieu de 1 664 ; arithmétique : `pieces/construire-brouillons-3-v1/calcul-devis-quinze-conditions.txt`) ; le brouillon 2 corrigeait le brouillon 1 après la contre-lecture 1. **Aucune dépense avant le mot de Lazar sur ce devis** et la ligne de GO au registre.

## Décision demandée

Accorder la dépense de calcul d'une course de 1 920 épisodes sur une carte louée, **attendu 26 à 41 dollars, plafond 90 dollars**.

## Enjeu

Le critère 2 de la porte G0 demande une dose–réponse pour l'organisme à consigne cachée ; aucune course ne l'a mesurée. Quinze conditions : l'agent honnête, six intensités écrites, deux proportions de pas désignés, trois témoins de consigne sur le gabarit du préenregistrement, et les trois conditions instruites du premier test (son saboteur, témoin positif, et ses deux témoins, second gabarit). La même course fournit les épisodes sur lesquels le critère 3 sera rejugé (texte de désignation, à part).

## Ce qui est acheté

| poste | quantité | durée | source du chiffre |
|---|---|---|---|
| épisodes | 15 conditions × 64 tâches × 2 répliques = 1 920 | 21,4 à 22,8 h | 40,2 s par épisode en lots de 8 (premier test) à 42,8 s (course exploratoire de l'organisme à adaptateur : 6,85 h pour 576 épisodes) |
| passe d'activations | 1 920 épisodes × 0,45 s | 0,2 h | premier test : 108,4 s pour 240 épisodes |
| mise en place, essais, poussées | — | ≈ 1,2 h | course exploratoire : essais 0,58 h |
| **marche totale** | | **≈ 22,9 à 24,3 h** | |

Chiffres de débit et de prix : texte scellé `prereg/T0.6-organismes-v0-v1.md` (`ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169`), section « Devis ».

- **Carte** : une A100 SXM4 de 80 Go sur Vast.ai, au plus 1,30 dollar de l'heure (relevés cités par ce texte scellé : 1,009 à 1,2133 pour la carte seule ; attendu 1,0889 à 1,30, borne du préenregistrement) ; disque d'au moins 250 Go (activations : ≈ 104 Go attendus pour trois couches, ≈ 189 Go au pire cas de 400 jetons par action) ; au moins 16 cœurs et 128 000 Mo de mémoire vive.
- **Calcul** : 22,9 à 24,3 h × 1,0889 à 1,30 = **24,9 à 31,6 dollars** ; valeur centrale ≈ 28.
- **Disque** : pendant la marche, au plus 0,08 dollar de l'heure (≤ 1,9) ; instance arrêtée et gardée jusqu'au verdict et au versement, 72 h au plus (≤ 5,8). Le disque d'une instance arrêtée n'est couvert que jusqu'à la fin du GO : les 72 heures sont une borne, non un droit au-delà.
- **Téléchargement** : 40 Go au plus à 0,05 dollar par Go (≤ 2).
- **Attendu : 26 à 41 dollars** (valeur centrale ≈ 32).
- **Marge de 30 %** (brief, § 14) sur l'attendu haut : 54 dollars.
- **Pire cas** : hôte deux fois plus lent, au prix plafond : 48,5 h × 1,30 = 63,1 ; disque 9,6 ; téléchargement 2 : **≈ 75 dollars**. Avec une reprise après une panne de chaîne (nouvelle mise en place au débit moitié, 2,4 h ; un bloc de 30 épisodes rejoué, 0,7 h ; soit 3,1 h × 1,30 ≈ 4,0 ; téléchargement 2 ; disque 0,3) : **≈ 81 dollars**.
- **Plafond demandé : 90 dollars**, arrêt de l'instance par son identifiant à ce cumul ; alerte à Lazar à 72 dollars (80 %).

Sans dépense en dollars : la banque de 64 tâches neuves (environ 85 papiers examinés, 130 à 160 passages de sous-agents d'extraction et de contre-vérification, sur le quota du modèle que nomme le manifeste de l'extraction des 96 tâches) ; le code et sa contre-lecture ; la lecture du coût, hors ligne ; le verdict.

Hors de ce devis : le lecteur du texte (processeur, 0 dollar) ; le calcul des scores de sondes et le lancement de l'organisme à adaptateur (texte de désignation), chacun sur son propre devis. Ordres de grandeur, estimations de l'auteur sans devis, donnés pour que l'enveloppe d'ensemble soit visible (débits du texte scellé de T0.6, section « Devis » : passe d'activations 0,45 s par épisode ; sondes et planchers du premier test, 1 534 s) : scores de sondes, une à deux heures de carte (quelques dollars) ; lancement de l'organisme à adaptateur, s'il a lieu, 14 conditions de 128 épisodes, à un débit non mesuré (ses lots se jouent par état d'adaptateur), donc une dépense du même ordre que celle de ce devis, peut-être supérieure.

## Options

- **(a) Deux répliques par tâche et par condition — ce devis.** Avantage : l'effet minimal détectable passe de 0,39 à environ 0,28–0,34 en logarithme décimal. Parmi les réponses graduées simulées, pour la moins favorable (exécution exacte de la consigne), la chance d'établir l'échelle d'intensité passe de 0,62–0,65 à 0,83–0,98, et celle qu'une intensité au moins porte un sabotage établi sans que le coût seul le voie, de 0,74–0,87 à 0,86–1,00 (sortie de puissance v5). Inconvénient : le double du calcul.
- **(b) Une réplique.** 960 épisodes, 12,0 à 12,7 h : attendu 14 à 25 dollars, plafond 50. Inconvénient : puissance ci-dessus ; le texte du préenregistrement change (une valeur de configuration et la section « Puissance »).
- **(c) Option (a) plus les deux contrôles croisés du brief** (honnête averti de la surveillance, saboteur en régime « non observé »). 256 épisodes de plus : 3 à 4 dollars. Inconvénient : deux textes privés de plus à écrire et à contre-lire ; ils ne servent que la validité des sondes. Sans eux, deux lectures de validité du texte scellé des sondes restent en attente.
- **(d) Option (a) sans les deux témoins instruits du premier test.** 256 épisodes de moins : 3 à 4 dollars de moins, plafond 80. Inconvénient : les témoins de consigne ne couvrent plus qu'un seul gabarit, alors qu'un seul témoin ne suffit pas à une lecture de validité (préenregistrement, section 0, choix 5).

**Recommandation : (a), confiance 0,7.** Pas de défaut : une dépense est un nœud.

## Calendrier proposé

Après le mot de Lazar : banque de tâches, un demi-jour à un jour ; code et contre-lecture, un à deux jours, en parallèle ; course, environ 24 heures ; lecture et verdict, un demi-jour. **Dernier jour de création proposé : 12 décembre 2026 ; fin du GO proposée : 15 décembre 2026, 00:00 UTC** (porte G0 au plus tard fin décembre).

## Ligne d'engagement proposée (registre des dépenses, à écrire par la mère au lancement)

« engagement : T0.6, organisme à consigne cachée, dose–réponse (ligne de GO à citer, plafond 90 USD) : préenregistrement scellé et code cités au registre des scellements ; une carte A100 SXM4 80 Go ≤ 1,30 USD de l'heure, disque ≥ 250 Go ; attendu 26 à 41 USD, pire cas ≈ 81 USD ; crédit Vast.ai relu à la création. »
