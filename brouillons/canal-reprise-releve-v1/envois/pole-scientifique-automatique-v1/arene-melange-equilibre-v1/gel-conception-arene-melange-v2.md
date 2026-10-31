# Gel de la conception — arène « mélange d'équilibre », code v2 — écrit AVANT les pilotes sur la racine d'essai fraîche

Sous-agent neuf Opus 5.5 (lignée conv-audit), 31 octobre 2026, branche `canal/conv-audit-n04`. Ce fichier fixe la conception et les prédictions **avant** toute exécution sur RACINE_ESSAI = 20261293 / 20261294 (condition 6 de CM-01 : plus aucun changement de conception après les pilotes). Son empreinte est consignée au journal `journal-pilotes-arene-melange-v2.txt` avant le lancement des pilotes.

## 1. Code et calibrage

- Code avant calibrage : `arene_melange_v2.py` `ab064418037f1e52afdb50b131f23e575ffd7590c1133a31bb6b0a6a9b7f2657` (`DELTAS_V2 = None`).
- Calibrage des δ (règle `choisir_deltas`, écrite dans ce code avant son exécution ; bras A seul ; RACINE_CALIBRAGE = 20261295 / 20261296 ; 12 instances × 9 valeurs de la grille 0,6 … 2,4) : `calibrage-deltas-arene-melange-v2.json` `f887e9c1051f40490e7c72c24fa74680f6b4e7818c0c9343d6e63a58c8ba933e`. Détection moyenne de A en (iii) : 0,6 → 0,420 ; 0,8 → 0,342 ; 1,0 → 0,290 ; 1,2 → 0,170 ; 1,4 → 0,131 ; 1,6 → 0,035 ; 1,8 → 0,034 ; 2,0 → 0,010 ; 2,4 → 0,0005. Règle : δ_haut = plus grand δ où V(A) ≥ 3α = 0,03 → **1,8** ; δ_bas = plus grand δ < δ_haut où V(A) ≥ 10α = 0,10 → **1,4**.
- Code gelé : la seule ligne changée est `DELTAS_V2 = (1.4, 1.8)` (différentiel vérifié, une ligne) → `arene_melange_v2.py` `8e1e651b4be3e6fea6bf6bdf0fc00a19d479aa818323461fbf550582dfdb46bb` ; configuration `CONFIG_V2` `1d7544e652ee6ab782577c5731127c7338844ef3d39844d86842688ddb2031a3`.
- Racines : décision RACINE = 20261201, RACINE_TENUE = 20261202 (jamais employées) ; brouillon 1 : 20261291 / 20261292 (interdites en v2 par garde) ; essai v2 : 20261293 / 20261294 ; calibrage : 20261295 / 20261296 ; essais du code : 20261297 / 20261298.

## 2. Principe de l'oracle du défenseur (énoncé avant toute observation de la v2)

Le double oracle (McMahan, Gordon et Blum 2003, SUPPOSÉ) converge vers l'équilibre du jeu que l'on résout **à condition** que chaque oracle rende une meilleure réponse **pour le gain de ce jeu**. Le gain ici est la matrice G (taux de détection au seuil de fausses alertes α). La régression logistique minimise une perte logarithmique moyenne sur les échantillons ; elle ne maximise pas la détection à α ; ce n'est donc pas une meilleure réponse au gain du jeu. Un oracle qui n'est pas une meilleure réponse n'exerce pas le chemin que l'on veut tester (le mélange) : la comparaison devient muette, au sens de R5 (« chemin non exercé »). D'où l'oracle « détection » (maximisation du taux de détection lissé au seuil α), **le même pour tous les bras**, y compris A. Conséquence de portée : A est « défense unique réentraînée, même oracle », **pas** le protocole de Bailey et collègues (dont les sondes sont entraînées par régression) ; toute conclusion est conditionnelle à cet oracle. L'observation du brouillon 1 (instance 0, δ = 1,6, B ≈ A sous la régression logistique) vient **après** ce principe, en note : elle est archivée par reproduction (`archive-observation-oracle-v1.py`) et remplacée, comme fait, par le pilote logistique complet ci-dessous.

## 3. Conception gelée (résumé ; le détail est dans le code et le brouillon 2)

Bras à trajectoire : A, B, D (même définitions que le brouillon 1, l'ancien bras C retiré). Témoins « finale seulement » sur les T + 1 = 9 moniteurs mêmes de B : C1 poids uniformes ; C2 poids de Dirichlet uniforme (graine dérivée, rôle 13) ; C3 « ou » déterministe (scores standardisés sur le propre de calibration, λ = 8, log-somme-exp, seuil recalibré à α). (iii) = plus basse des détections des attaquants final standard et renforcé. Coût par contournement relatif (κ = 0,5 de la détection de la cible non modifiée), garde de ligne de base (κ × base ≥ 2α, sinon « non défini »), courbe V(δ') aux fractions 0 ; 0,25 ; 0,5 ; 0,75 ; 1 de δ, bissection en 3 pas dans l'intervalle qui encadre. Statuts et itérations de l'attaquant consignés ; départs non finis comptés, garde à 5 % par tâche. Intervalles : rééchantillonnage apparié de 20 000 tirages, quantiles bilatéraux 95 %, 90 %, corrigés de Bonferroni sur 2 δ et sur 8 tests.

## 4. Prédictions signées, écrites avant les pilotes

Pilote logistique (`--oracle logistique`, 24 instances × 2 δ, RACINE_ESSAI) — descriptif, prédiction de la contre-lecture adoptée :
- L1 : les poids finaux de B sont **purs** (un poids ≥ 1 − 10⁻⁹) sur **plus de la moitié** des tâches de chaque δ (déclencheur « mélange dégénéré » → « non concluant » si cet oracle était retenu). Réfutée si la part pure est ≤ 0,5 dans un δ. Confiance 0,7.
- L2 : |moyenne de B − A sur (iii)| < 0,02 à chaque δ. Réfutée si ≥ 0,02 dans un δ. Confiance 0,65.

Pilote détection (oracle retenu, 24 instances × 2 δ, RACINE_ESSAI). Pour chaque contraste et chaque δ, une branche prédite et la branche opposée (qui réfute) :

| Contraste | δ_bas = 1,4 : prédit (confiance) | δ_haut = 1,8 : prédit (confiance) | Branche opposée (réfutation) |
|---|---|---|---|
| B − A (iii), plomberie | + (0,9) | + (0,85) | moyenne ≤ 0 |
| B − C1 (iii), poids d'équilibre contre uniformes | ≈ 0, \|moyenne\| < 0,01 (0,6) | ≈ 0, \|moyenne\| < 0,01 (0,6) | \|moyenne\| ≥ 0,01 (dans un sens ou l'autre) |
| B − C2 (iii), poids d'équilibre contre aléatoires | + (0,65) | + (0,6) | moyenne ≤ 0 |
| B − C3 (iii), tirage au hasard contre « ou » déterministe | − : C3 > B (0,8) | − : C3 > B (0,65) | moyenne ≥ 0 (le tirage au hasard paie) |
| B − D (iii), mélange contre unique à paramètres égaux | − : D > B (0,85) | − : D > B (0,7) | moyenne ≥ 0 |
| B − A (ii), non-régression | − (0,7) | − (0,7) | moyenne ≥ 0 |

Raison des confiances plus basses à δ_haut : la contre-lecture a mesuré un signe de B − C3 qui s'inverse entre δ = 1,6 (C3 ≫ B) et δ = 2,4 (C3 < B, au plancher) ; δ_haut = 1,8 est entre les deux, du côté où A garde encore 3α. Lecture prédite de l'hypothèse principale (« B bat les témoins à capacité égale ») : **réfutée** aux deux δ (C3 et D font mieux que B).

Après les pilotes : aucune modification de conception ; seuls les chiffres des prédictions et les valeurs recommandées des seuils viennent des pilotes, comme au brouillon 1.
