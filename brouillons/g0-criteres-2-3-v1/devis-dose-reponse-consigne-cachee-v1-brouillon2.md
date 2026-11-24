# Devis — course de dose–réponse de l'organisme à consigne cachée (partie (i) du critère 2 de la porte G0) — v1 — brouillon 2

Pièce de classe A, jointe au préenregistrement `T0.6-organisme-consigne-cachee-dose-reponse-v1-brouillon2.md`. Écrite le 2026-11-24 par la session fille de conception `session_01Qi7Gr4GahKn8qRTN5FTWv3` ; brouillon 1 (`3e54f8948b9f591615661435de8d4819134a1e04440a3c244dbe40a5f7cf6def`) corrigé après la contre-lecture 1 (constats CL1-10, CL1-18 et CL1-19 : disque, relevés de prix, détail de la reprise, limite du GO). **Aucune dépense avant le mot de Lazar sur ce devis** et la ligne de GO au registre.

## Décision demandée

Accorder la dépense de calcul d'une course de 1 664 épisodes sur une carte louée, **attendu 23 à 37 dollars, plafond 80 dollars**.

## Enjeu

Le critère 2 de la porte G0 demande une dose–réponse pour l'organisme à consigne cachée ; aucune course ne l'a mesurée. La même course fournit les épisodes sur lesquels le critère 3 sera rejugé (texte de désignation, à part).

## Ce qui est acheté

| poste | quantité | durée | source du chiffre |
|---|---|---|---|
| épisodes | 13 conditions × 64 tâches × 2 répliques = 1 664 | 18,6 à 19,8 h | 40,2 s par épisode en lots de 8 (premier test) à 42,8 s (course exploratoire de l'organisme à adaptateur : 6,85 h pour 576 épisodes) |
| passe d'activations | 1 664 épisodes × 0,45 s | 0,2 h | premier test : 108,4 s pour 240 épisodes |
| mise en place, essais, poussées | — | ≈ 1,2 h | course exploratoire : essais 0,58 h |
| **marche totale** | | **≈ 20,0 à 21,2 h** | |

Chiffres de débit et de prix : texte scellé `prereg/T0.6-organismes-v0-v1.md` (`ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169`), section « Devis ».

- **Carte** : une A100 SXM4 de 80 Go sur Vast.ai, au plus 1,30 dollar de l'heure (relevés cités par ce texte scellé : 1,009 à 1,2133 pour la carte seule ; attendu 1,0889 à 1,30, borne du préenregistrement) ; disque d'au moins 250 Go (activations : ≈ 91 Go attendus pour trois couches, ≈ 164 Go au pire cas de 400 jetons par action) ; au moins 16 cœurs et 128 000 Mo de mémoire vive.
- **Calcul** : 20,0 à 21,2 h × 1,0889 à 1,30 = **21,8 à 27,6 dollars** ; valeur centrale ≈ 24.
- **Disque** : pendant la marche, au plus 0,08 dollar de l'heure (≤ 1,7) ; instance arrêtée et gardée jusqu'au verdict et au versement, 72 h au plus (≤ 5,8). Le disque d'une instance arrêtée n'est couvert que jusqu'à la fin du GO : les 72 heures sont une borne, non un droit au-delà.
- **Téléchargement** : 40 Go au plus à 0,05 dollar par Go (≤ 2).
- **Attendu : 23 à 37 dollars** (valeur centrale ≈ 28).
- **Marge de 30 %** (brief, § 14) sur l'attendu haut : 48 dollars.
- **Pire cas** : hôte deux fois plus lent, au prix plafond : 42,4 h × 1,30 = 55,1 ; disque 9,2 ; téléchargement 2 : **≈ 66 dollars**. Avec une reprise après une panne de chaîne (nouvelle mise en place au débit moitié, 2,4 h ; un bloc de 26 épisodes rejoué, 0,6 h ; soit 3,0 h × 1,30 ≈ 3,9 ; téléchargement 2 ; disque 0,3) : **≈ 73 dollars**.
- **Plafond demandé : 80 dollars**, arrêt de l'instance par son identifiant à ce cumul ; alerte à Lazar à 64 dollars (80 %).

Sans dépense en dollars : la banque de 64 tâches neuves (environ 85 papiers examinés, 130 à 160 passages de sous-agents d'extraction et de contre-vérification, sur le quota du modèle que nomme le manifeste de l'extraction des 96 tâches) ; le code et sa contre-lecture ; la lecture du coût, hors ligne ; le verdict.

Hors de ce devis : le lecteur du texte (processeur, 0 dollar) ; le calcul des scores de sondes et le lancement de l'organisme à adaptateur (texte de désignation), chacun sur son propre devis. Ordres de grandeur, donnés pour que l'enveloppe d'ensemble soit visible, et qui ne sont pas des devis : scores de sondes, une à deux heures de carte (quelques dollars) ; lancement de l'organisme à adaptateur, s'il a lieu, 14 conditions de 128 épisodes, soit une dépense voisine de celle de ce devis.

## Options

- **(a) Deux répliques par tâche et par condition — ce devis.** Avantage : l'effet minimal détectable passe de 0,39 à environ 0,28–0,34 en logarithme décimal. Parmi les réponses graduées simulées, pour la moins favorable (exécution exacte de la consigne), la chance d'établir l'échelle d'intensité passe de 0,79–0,81 à 0,94–1,00, et celle qu'une intensité au moins porte un sabotage établi sans que le coût seul le voie, de 0,74–0,87 à 0,86–1,00. Inconvénient : le double du calcul.
- **(b) Une réplique.** 832 épisodes, 10,6 à 11,2 h : attendu 13 à 24 dollars, plafond 45. Inconvénient : puissance ci-dessus ; le texte du préenregistrement change (une valeur de configuration et la section « Puissance »).
- **(c) Option (a) plus les deux contrôles croisés du brief** (honnête averti de la surveillance, saboteur en régime « non observé »). 256 épisodes de plus : 3 à 4 dollars. Inconvénient : deux textes privés de plus à écrire et à contre-lire ; ils ne servent que la validité des sondes. Sans eux, deux lectures de validité du texte scellé des sondes restent en attente.

**Recommandation : (a), confiance 0,7.** Pas de défaut : une dépense est un nœud.

## Calendrier proposé

Après le mot de Lazar : banque de tâches, un demi-jour à un jour ; code et contre-lecture, un à deux jours, en parallèle ; course, environ 21 heures ; lecture et verdict, un demi-jour. **Dernier jour de création proposé : 12 décembre 2026 ; fin du GO proposée : 15 décembre 2026, 00:00 UTC** (porte G0 au plus tard fin décembre).

## Ligne d'engagement proposée (registre des dépenses, à écrire par la mère au lancement)

« engagement : T0.6, organisme à consigne cachée, dose–réponse (ligne de GO à citer, plafond 80 USD) : préenregistrement scellé et code cités au registre des scellements ; une carte A100 SXM4 80 Go ≤ 1,30 USD de l'heure, disque ≥ 250 Go ; attendu 23 à 37 USD, pire cas ≈ 73 USD ; crédit Vast.ai relu à la création. »
