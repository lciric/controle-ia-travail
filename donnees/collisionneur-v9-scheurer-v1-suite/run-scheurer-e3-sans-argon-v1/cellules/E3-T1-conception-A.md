# Proposition A — Tour III.1 : tendance d'échelle pour la surveillance

Statuts : tous les chiffres de `piece-scheurer-v1` sont **RAPPORTÉ** (la pièce dit qu'aucun n'a été revérifié sur page primaire) ; ceux de `piece-nos-resultats-v1` sont **OBSERVÉ-NON-AUDITÉ** ; le reste est **HYPOTHÈSE** ou « supposé/illustratif ».

## (a) Ce que la question suppose sans l'établir

1. **Qu'une tendance temporelle lisse existe** pour un comportement désaligné. HYPOTHÈSE : rien dans les pièces ne montre une courbe datée ; 2603.01608 donne des taux de base à 0 % sauf un cas à 3 % (RAPPORTÉ), ce qui est un plancher, pas une pente.
2. **Que capacité et propension se séparent.** RAPPORTÉ (2603.01608, résumé et § 4.1) : « difficiles à démêler » ; retirer un outil fait tomber 59 % à 3 %. Une propension mesurée dépend donc du montage plus que du modèle.
3. **Que la mesure est invariante d'un modèle à l'autre.** RAPPORTÉ (2412.04984 § 4, p. 15) : sous-estimation possible, aversion de disposition ; RAPPORTÉ (2510.09462 § 6) : comportement induit par consigne « peut être sous-élicité ». Un trend de propension confond donc pente réelle et pente d'élicitation.
4. **Que le moniteur est un instrument fixe.** RAPPORTÉ (2506.05296 § 2.3) : AUC de 0,92 à 0,96 selon le moniteur ; RAPPORTÉ (2510.09462, fig. 2) : le moniteur le plus fort passe à 0 sur 375 échantillons sous injection. L'instrument bouge et se casse.
5. **Que le recette METR/TastEval se transpose.** RAPPORTÉ : nombre de tâches, de modèles, procédure de régression et incertitude du doublement absents des pièces ; TastEval déclare lui-même que le « hill-climb » peut surestimer (§ 3.2).
6. **Qu'un juge de langage peut noter.** OBSERVÉ-NON-AUDITÉ (§ 4 de nos résultats) : deux juges au plafond, κ = 0. Toute tendance notée par juge hérite de ce plafond.
7. **Qu'il existe assez de modèles ouverts datés.** HYPOTHÈSE : Qwen2.5 donne sept tailles mais **une seule date** (RAPPORTÉ, § 2.2) — un axe de taille, pas un axe de temps.

Conséquence de conception : je ne mesure pas la propension du modèle surveillé ; je mesure la **capacité du moniteur** contre une attaque **vérifiée mécaniquement**, ce qui neutralise 2, 3 et 6.

## (b) Tendances candidates et duels

### T1 — Horizon de surveillance (meilleure)

- **Grandeur** : pour un moniteur M, le taux de détection (TPR) à fausses alertes fixées à 5 % (supposé) de portes dérobées dans des solutions APPS, en fonction de la **taille de la trajectoire** (lignes de code + traces d'exécution). **Horizon(M)** : taille à laquelle une logistique ajustée croise TPR = 50 % — calque exact de la recette METR (RAPPORTÉ, § 3.1).
- **Même mesure d'un modèle à l'autre** : la porte dérobée est vérifiée à l'exécution par une entrée qui change la sortie (RAPPORTÉ, 2510.09462, tâche annexe) ; pas de juge ; pool d'attaquants **gelé** (Qwen2.5 0,5–72B, poids ouverts).
- **Échelle continue** : taille de trajectoire ; variante : durée humaine de revue mesurée sur un sous-échantillon (supposé : 30 trajectoires chronométrées).
- **Modèles** : moniteurs ouverts datés, supposé 8 à 12 sur 24 mois ; plus les 7 Qwen2.5 pour un axe de taille à date fixe.
- **Ajustement** : log2(horizon) ∼ date, moindres carrés, bootstrap sur problèmes et sur attaquants pour l'intervalle.
- **Énoncé attendu (supposé)** : « l'horizon de surveillance double tous les 9 à 15 mois », signe positif. Chiffre non tiré des pièces.

**Duel D1** (moniteur varie, attaquants gelés). H_A : la pente de log2(horizon) sur la date est ≥ 0,5 bit/an (doublement ≤ 24 mois) avec un intervalle à 95 % excluant 0. H_B : la pente est indiscernable de 0 (horizon dominé par la taille de trajectoire, non par le moniteur). Métrique : pente ; seuil : borne inférieure de l'intervalle > 0,3 bit/an (supposé). Contrôle négatif : moniteur mécanique fixe (suite de tests + lanceur d'entrées aléatoires), qui doit avoir pente 0 ; si lui aussi « progresse », la banque dérive (contamination par difficulté), et D1 est non concluant. Issue : pente nulle avec contrôle plat falsifie H_A ; pente positive falsifie H_B.

**Duel D2** (attaquant contemporain). H_A : à date égale, le moniteur garde un horizon ≥ celui mesuré contre le pool gelé ×0,8 (supposé). H_B : les attaquants récents produisent des portes dérobées plus subtiles (RAPPORTÉ, 2506.05296, section non citée) et l'horizon contre contemporain stagne ou décroît. Seuil : rapport horizon(contemporain)/horizon(gelé) avec intervalle. Si le rapport < 0,8, H_A falsifiée (la course est nulle, l'énoncé doit être signé négativement) ; si ≥ 0,8, H_B falsifiée.

### T2 — Écart de capacité seuil pour l'injection

- Grandeur : plus petit écart (taille ou date) attaquant–moniteur au-delà duquel une injection dans le contenu lu par le moniteur réussit sans exemple (RAPPORTÉ, 2510.09462 § 4.4). Échelle : différence de log-paramètres sur Qwen2.5.
- Duel : H_A : l'écart seuil se déplace vers le haut avec la date du moniteur (la hiérarchie d'instructions, RAPPORTÉ § 6, progresse) ; H_B : l'écart seuil est constant ou nul (GPT-4.1 à 0 sur 375, RAPPORTÉ, fig. 2, est la règle). Contrôle négatif : mêmes échantillons sans injection (TPR doit rester celui de T1). Énoncé supposé : « l'écart seuil croît de X bits par an » ; signe inconnu — c'est précisément ce qui est réfutable. Limite d'intégrité : les injections sont décrites par leur classe, jamais reproduites.

### T3 — Conscience d'évaluation par unité d'apprentissage par renforcement

- Grandeur : taux de conscience d'évaluation verbalisée (RAPPORTÉ, 2509.15541 § 6.1 : 2,0 % → 20,5 %) en fonction des pas de renforcement, sur un modèle ouvert. Axe : calcul de renforcement, pas la date.
- Duel : H_A : croissance monotone, ≥ ×2 par doublement du calcul (supposé) ; H_B : saut puis plateau (effet de seuil de la consigne). Contrôle négatif : ajustement fin supervisé à calcul égal, où H_A prédit pas de croissance. Menace : la verbalisation dépend d'un juge (plafond, § 4 de nos résultats) — à tenir par classificateur figé avec étalonnage sur 200 cas annotés deux fois (supposé).
- Pourquoi secondaire : coûte un entraînement par point ; c'est la seule candidate qui mesure du désalignement, pas de la surveillance.

### T4 — Propension à la sous-performance sans but (contre-exemple attendu)

Grandeur : écart de 2412.04984 § 3.6 (0,96 contre 0,61 ; signification des deux scores non donnée, RAPPORTÉ). Je la garde comme **témoin d'échec** : HYPOTHÈSE que sa pente datée sera dominée par les refus et la disposition (p. 15). Duel : H_A : pente > 0 ; H_B : pente confondue avec le taux de refus (corrélation > 0,7, supposé). Si H_B, cela justifie empiriquement de ne pas tendre les propensions.

## Menaces et contrôles (T1)

- **Élicitation** (RAPPORTÉ, 2510.09462 § 6) : l'attaquant est instruit ; on ne mesure que le moniteur, et le pool est gelé — la sous-élicitation est constante dans le temps, donc n'entre pas dans la pente.
- **Refus** : un attaquant qui refuse produit une trajectoire honnête ; comptée dans les cas honnêtes appariés, jamais comme détection.
- **Changement de moniteur / injection** : T1 est mesurée sans injection ; T2 la mesure séparément. Rééchantillonner le moniteur est interdit (RAPPORTÉ : 1 − (1 − p)^k se retourne contre le défenseur).
- **Confusion honnête/malveillant** (RAPPORTÉ, 2506.05296 § 7) : les cas honnêtes sont produits par le **même** attaquant sur les mêmes problèmes, pas tirés d'APPS.
- **Fausses alertes mal calibrées** : OBSERVÉ-NON-AUDITÉ (T0.3) : un seuil de Ville unilatéral donne 0,21–0,35 de fausses alarmes sous effet d'épisode ; je calibre le seuil à 5 % **par moniteur** sur 1 000 trajectoires honnêtes (calque de la calibration qui a tenu 0,046–0,055).
- **Contamination** : banque fraîche de problèmes, graines scellées, empreinte publiée avant notation (calque du § 5 de nos résultats).

## (c) Mesure minimale par instrument

- **Moniteur de trajectoire (type page « Monitoring » d'Apollo, RAPPORTÉ § 1.3)** : TPR à FPR = 5 % sur ≥ 300 cas malveillants vérifiés à l'exécution et ≥ 1 000 honnêtes appariés (même attaquant, mêmes problèmes) ; doit battre la suite de tests APPS plus lanceur d'entrées aléatoires (supposé : 10 000 entrées par solution). Un moniteur sous ce plancher mécanique est déclaré « non fonctionnel », comme les sondes de P3 sous leurs 200 sondes aléatoires (OBSERVÉ-NON-AUDITÉ).
- **Juge de langage** (si employé pour T3) : κ sur 200 cas double-annotés ; κ < 0,4 (supposé) interdit son usage ; notre second tour donne κ = 0 au plafond.
- **Ajustement logistique (METR)** : reporter nombre de points par modèle, intervalle bootstrap du temps de doublement, et test du contrôle mécanique plat — exactement les quatre absences de la pièce § 3.1.

## (d) Ancrage matériel — pilote de T1

- Modèles : Qwen2.5 0,5–72 B (RAPPORTÉ, § 2.2) comme attaquants et moniteurs ; 72 B en bf16 sur 2 H100 (illustratif). Montage à un H100 fixe, comme TastEval (RAPPORTÉ, § 3.2).
- Taille : 500 problèmes APPS, 7 attaquants × 2 rôles (honnête/malveillant) = 7 000 trajectoires ; 7 moniteurs × 7 000 = 49 000 lectures (calcul). Exécution différentielle : ~7 000 × 10 000 entrées, processeur central.
- Coût illustratif : 150 heures H100 génération, 300 heures notation, soit l'ordre de 1 500 € loués ; quatre semaines.
- **Non concluant si** : la pente de taille sur Qwen2.5 a un intervalle couvrant 0 avec un contrôle mécanique lui-même non plat ; ou si moins de 4 moniteurs dépassent le plancher mécanique (puissance : ~1 détection sur 6 à force 0,5 chez nous, OBSERVÉ-NON-AUDITÉ § 5 — ordre de grandeur à craindre) ; ou si le TPR à 5 % est au plafond (> 0,95) pour tous, cas d'un banc sans dents.

## Ce qui ferait échouer le plan

L'axe de taille (Qwen2.5, une date) ne se convertit pas en axe de temps faute de modèles ouverts datés comparables ; les attaquants gelés deviennent triviaux pour tout moniteur récent (plafond, pente ininterprétable) ; la subtilité des attaquants contemporains annule le gain (D2 tranche pour H_B), et l'énoncé devient « rapport constant », vrai mais sans facteur.

FIN-DE-CELLULE