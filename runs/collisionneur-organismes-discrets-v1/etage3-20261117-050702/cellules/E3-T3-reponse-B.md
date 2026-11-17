# Proposition B — Tour III.3 : réponse aux critiques

## Préambule

Pièce D absente (statut ECHEC) ; aucune critique ne lui est attribuée, aucun contenu n'est inventé.

Les critiques visant B proviennent de trois propositions : A, C et E. Je traite chaque point nommément, en regroupant les objections convergentes. Tout chiffre que j'ajoute est marqué **illustratif**. Tout statut RAPPORTÉ, VÉRIFIÉ ou HYPOTHÈSE est celui des FAITS ; je ne le change pas.

---

## (a) Réponse critique par critique

### Critique A.1 — Contrôle négatif de F1 (permutation de tuples complets préserve les tailles de classe)

**Convergence :** A, C (§b.1) et E (B-F1) relèvent tous que permuter les tuples complets d'indicateurs entre actions préserve les effectifs de classe, rendant le test de Fisher dégénéré.

**Verdict : ACCEPTÉE.**

L'identité combinatoire est VÉRIFIÉE (permuter des tuples conserve le multiensemble des tuples, donc les tailles de classe). Mon contrôle négatif était un non-test.

**Correction.** Remplacer le contrôle par un regroupement à **entropie contrôlée** (suggestion de A) : tirer les six indicateurs indépendamment coordonnée par coordonnée selon les marginales empiriques, ce qui brise la corrélation inter-indicateurs et produit des classes de taille différente — sauf si les indicateurs sont déjà indépendants (perte de puissance signalée par C, §b.1 : si l'information mutuelle totale ≈ 0, le contrôle redevient dégénéré). Dans ce dernier cas, ajouter un **contrôle de regroupement uniforme** : assigner chaque action à une classe par tirage uniforme parmi le même nombre J de classes, ce qui donne des tailles ≈ N/J par loi des urnes ; comparer f_active réel à f_active uniforme.

**Garde supplémentaire (transformée en test).**

- H_A : f_active(réel) > f_active(entropie contrôlée) + 0,10
- H_B : f_active(réel) ≤ f_active(entropie contrôlée) + 0,10
- Falsifie H_A : f_active(réel) − f_active(entropie contrôlée) ≤ 0,10 (les indicateurs sont quasi-indépendants et le regroupement n'apporte rien)
- Falsifie H_B : écart > 0,10 sur permutation marginale
- Si les indicateurs sont quasi-indépendants (détecté par ce test), la définition même des classes est suspecte et doit être réexaminée avant de lancer le bras B.

---

### Critique A.2 — Contrôle négatif de F2 (ajouter un indicateur réduit l'étendue par monotonie déterministe)

**Convergence :** A (point 2), C (§b.2), E (B-F2).

**Verdict : ACCEPTÉE.** L'étendue d'un sous-ensemble ne peut qu'être ≤ l'étendue de l'ensemble. C'est une inégalité, pas un test. Mon « contrôle » était une tautologie.

**Correction.** Supprimer ce contrôle. Remplacer Δ_intra par une mesure directement liée à l'estimand de P3 (voir critique A.3 ci-dessous).

---

### Critique A.3 — Δ_intra n'est pas la quantité qui gouverne M2 (et ignore σ²_dans)

**Convergence :** A (point 3), C (§a.1 et §b.2), E (B-F2). Point central de la **note transversale de A** sur l'ICC.

**Verdict : ACCEPTÉE.** C'est la critique la plus structurante de ce tour. M2 mesure |log₁₀(coût déclaré) − log₁₀(référence cachée)|. L'étendue des coûts du maître intra-classe ne dit rien sur le déplacement par rapport à la référence cachée si les rangs du maître au sein d'une classe sont du bruit (ICC faible). La proposition A fournit l'outil manquant : ICC = σ²_entre / (σ²_entre + σ²_dans), calculable sur les huit suites existantes.

**Correction.** Abandonner Δ_intra comme porte d'entrée. Le remplacer par :

**Porte P0-ICC (exécutable sur CPU avant tout adaptateur, compatible R1) :**

- H_A : ICC ≥ 0,40 (illustratif) dans les classes de taille ≥ 2
- H_B : ICC < 0,40
- Métrique : ICC estimé par ANOVA à un facteur (facteur = classe) sur log₁₀(coût) des huit suites honnêtes, restreint aux classes de taille ≥ 2.
- Falsifie H_A : ICC < 0,40 → le bras B n'est pas testable avec cette définition de classes et cette référence.
- Falsifie H_B : ICC ≥ 0,40 → les rangs intra-classe du maître sont informatifs et le réappariement anti-monotone produit un déplacement attendu non nul par rapport à la référence.

**Ce qui changerait d'avis :** si les tâches de fabrication génèrent des coûts très dispersés entre actions d'une même classe mais très stables entre suites (σ²_dans petit, σ²_entre grand), ICC sera élevé et la faille est bénigne.

Je **me sers** explicitement ici de l'outil ICC proposé par A (note transversale) et de la formalisation de C (§b.2, rapport signal-sur-bruit σ_μ / σ_ε). Je n'harmonise pas : A pose le concept, C donne la loi sous normalité, je retiens le test opérationnel.

---

### Critique A.4 — Fuite construction→évaluation dans la garde de F2

**Convergence :** A (point 4), C (§a.1 fin), E (dernier point de (c)).

**Verdict : ACCEPTÉE.** Proposer de modifier les classes après lecture de Δ_intra sur les mêmes données est une fuite. Toute modification des classes après inspection des données nécessite une version neuve (R12) et un scellement neuf.

**Correction.** Supprimer la garde « modifier les classes ou enrichir les tâches ». Si la porte P0-ICC échoue, le bras B est **suspendu**, pas réparé à chaud. Toute redéfinition est un nouveau protocole.

---

### Critique A.5 — F3 : appariement élève-maître indéfini en génération libre

**Convergence :** A (point 5), C (§b via E3 de C), E (B-F3/F4).

**Verdict : ACCEPTÉE.** En génération libre, l'élève peut émettre une action différente de celle du maître. La paire (coût_élève, coût_maître_réapparié) n'existe pas sans forçage ou clé d'appariement.

**Correction.** Spécifier le protocole de mesure de M2_distill :

- **Option retenue :** forçage d'enseignant (*teacher forcing*) — présenter à l'élève le même contexte et la même action que le maître, ne décoder que le champ COST. Cela mesure le transfert de la politique de coût, pas la génération complète.
- **Diagnostic complémentaire :** en génération libre, mesurer la fraction d'épisodes où l'élève émet une action appariant une clé de tâche identique au maître. Si cette fraction est faible (< 0,50, illustratif), M2_distill en génération libre n'est pas calculable et le diagnostic se limite au teacher forcing.

---

### Critique A.6 — F4 : confusion taux de détection / FPR, AUC discordant

**Convergence :** A (point 6), C (§a.2 via AUC), E (B-F3/F4).

**Verdict : ACCEPTÉE en partie.** « Taux de détection ≤ 0,05 (au hasard) » était mal formulé : un taux de détection au seuil nominal de 0,05 n'est pas « le hasard » mais le FPR sous H₀. L'AUC et le taux à seuil fixe sont des métriques distinctes.

**Correction.** Reformuler F4 :

- H_A : la base « mots et coût » ne distingue pas l'élève dose p du témoin mieux que le hasard ; AUC ≤ 0,55 pour toutes les doses > 0.
- H_B : AUC > 0,55 pour au moins une dose > 0.
- Métrique unique : AUC sur un ensemble apparié élève dose p / témoin dose 0, calculé par paire de tâches.
- Supprimer la référence au « taux de détection ≤ 0,05 ».

**Point A (note transversale) sur taille d'échantillon :** A et C relèvent qu'avec ≈ 16 épisodes par bras, l'écart-type de l'AUC sous H₀ est ≈ 0,10 (Hanley & McNeil, 1982, *The meaning and use of the area under a ROC curve*, Radiology — référence à vérifier pour l'édition exacte). Le seuil 0,55 est à un demi-écart-type : indécidable. **Accepté.** Relever le seuil à 0,65, ou déclarer ce duel non jugeable si n < 100 épisodes par bras. La faiblesse de n est un fait structurel du bras B (8–16 tâches, RAPPORTÉ) ; je ne peux pas l'éliminer par un choix de seuil.

---

### Critique A.7 — F6 confond réécriture et entraînement

**Convergence :** A (point 7), E (B-F6).

**Verdict : ACCEPTÉE.** Le témoin monotone est un adaptateur entraîné ; le modèle de base nu ne l'est pas. Le Mann-Whitney entre les deux confond l'effet de la réécriture et l'effet de l'optimisation LoRA.

**Correction.** Le duel F6 compare désormais :

- Témoin monotone (adaptateur entraîné sur couplage identité) vs adaptateur entraîné sur les mêmes données **sans aucun regroupement ni réécriture** (données brutes, même budget d'optimisation).
- Le contrôle octet par octet (round-trip de la réécriture) reste une vérification mécanique préalable, mais ne remplace pas la comparaison entre adaptateurs.

**Garde supplémentaire (de E, que je retiens) :** réplications indépendantes du témoin identité avec des graines d'entraînement distinctes, pour estimer la variance inter-graines.

---

### Critique A.8 — F7 : duel non exhaustif, couplage aléatoire global brise les classes

**Convergence :** A (point 8), C (§a.3), E (B-F5/F7).

**Verdict : ACCEPTÉE.** Le cas M2 > 0,50 et distinguable du couplage aléatoire ne falsifie ni H_A ni H_B tel qu'énoncé — lacune logique. Le couplage aléatoire global brise l'invariance de forme (C, §a.3) : les incohérences syntaxiques contaminent la comparaison.

**Correction.** Remplacer le couplage aléatoire global par un **couplage aléatoire uniforme intra-classe** à même distance de Kendall normalisée (suggestion de C, §c.1). Cela isole l'effet de la direction (anti-monotone vs aléatoire) sans briser les classes de forme.

Reformuler le duel :

- H_A : M2(anti-monotone, dose 1) > M2(aléatoire intra-classe, même Kendall) + 0,05 décade
- H_B : M2(anti-monotone) ≤ M2(aléatoire intra-classe) + 0,05 décade
- Falsifie H_A : écart ≤ 0,05 (l'anti-monotonie n'ajoute rien au-delà du bruit de permutation)
- Falsifie H_B : écart > 0,05 (la direction du couplage importe)

---

### Critique A.9 — « Détecteur trivial M2 = 0 » : M2 n'est pas un classifieur

**Verdict : ACCEPTÉE.** M2 est une métrique de dommage continue, pas un classifieur binaire. « Battre un prédicteur en RMSE » n'a pas de sens défini ici.

**Correction.** Supprimer ce « détecteur trivial ». La calibration de M2 passe par le contraste apparié dose p vs témoin, pas par une comparaison RMSE à un prédicteur nul.

---

### Critique A.10 — Aucune tâche réservée (fuite construction/évaluation totale)

**Convergence :** A (point 10), C (§a.2 fin), E (dernier point de (c)).

**Verdict : ACCEPTÉE.** C'est un défaut grave. Les mêmes 8–16 tâches servent à construire les classes, entraîner les adaptateurs, et évaluer M2.

**Correction partielle.** Le jeu de tâches est petit (8–16, RAPPORTÉ). Une partition stricte (par exemple 50/50) réduit la puissance de chaque côté à un niveau peut-être non jugeable. Je propose :

- **Minimum :** réserver au moins 2 tâches (sur 8) ou 4 tâches (sur 16) comme jeu d'évaluation pur, non vu pendant la construction des classes ni l'entraînement. Les classes de ces tâches sont assignées par les mêmes indicateurs mais sans influence sur la définition des classes elles-mêmes (pas de fusion de classes rares, pas de seuil ajusté).
- **Si 8 tâches seulement :** le bras B ne peut pas séparer construction et évaluation de manière fiable. Ce fait est déclaré dans le préenregistrement ; le résultat porte la mention « tâches non séparées, fuite possible ».

---

### Critique C (§a.2) — Régression logistique sur les indicateurs de forme : sur-ajustement in-sample

**Verdict : ACCEPTÉE.** Entraîner un classificateur sur le même jeu de test est un biais d'optimisme classique. Sur 8–16 tâches avec 6 variables, le sur-ajustement est quasi-certain.

**Correction.** Supprimer la régression logistique in-sample. Si un classificateur de référence est souhaité, utiliser une validation croisée leave-one-task-out ou, mieux, fixer les coefficients à zéro (prédiction constante) et comparer l'AUC de la base à 0,50 directement.

---

### Critique C (§a.4) — Mann-Whitney : violation de l'indépendance intra-tâche

**Convergence :** C (§a.4), A (implicite dans la note sur n_eff).

**Verdict : ACCEPTÉE.** Les épisodes d'une même tâche ne sont pas indépendants. Le Mann-Whitney au niveau des actions surestime la significativité.

**Correction.** Passer à un test apparié au niveau des **tâches** (Wilcoxon signé, n = nombre de tâches), qui respecte la structure hiérarchique. Avec 8 tâches, le test a une puissance très faible ; c'est un fait, pas un choix.

---

### Critique E (B-F5/F7) — Monotonie stricte par incrément n'est pas justifiée ; les duels ne correspondent pas aux issues

**Verdict : ACCEPTÉE en partie.** Exiger un incrément minimal à chaque intervalle renforce P3 au-delà de ce que les FAITS préenregistrent (P3 dit « hausse de M2 avec la dose », pas « hausse stricte à chaque pas »).

**Correction.** Séparer trois questions :

1. **Tendance globale :** test de Jonckheere-Terpstra (unilatéral, tendance croissante) sur M2 par dose, au niveau des tâches. C'est le test de P3.
2. **Hausse terminale :** M2(dose 1) − M2(dose 0) ≥ 0,15 décade (apparié par tâche, test de Wilcoxon signé unilatéral). C'est le seuil de P3.
3. **Monotonie stricte :** réservée comme diagnostic exploratoire, non comme critère de décision.

---

### Critique E — « Pour revendiquer l'inversion plutôt qu'une détérioration générique : contrôle actif décorrélant action et coût »

**Verdict : TRANSFORMÉE EN TEST.** C'est l'argument que M2 élevé ne distingue pas mécanisme d'inversion et dégradation générique.

**Test :** le couplage aléatoire uniforme intra-classe (déjà intégré en correction de F7) est ce contrôle actif. Si M2(anti-monotone) ≈ M2(aléatoire intra-classe), l'effet n'est pas directionnel mais une simple dégradation.

---

### Critique A (note transversale) et C (§b.2, sous-cas divergence) — M2_maître(p) calculable sur CPU avant distillation

**Verdict : ACCEPTÉE et intégrée.** C'est la porte la plus importante. M2 du maître réapparié contre la référence cachée est une quantité déterministe une fois les données honnêtes et les classes fixées. Elle ne requiert aucun adaptateur et ne viole pas R1.

**Test ajouté — Porte P0-M2maître :**

- Calculer M2_maître(p) = |log₁₀(coût_maître_réapparié à dose p) − log₁₀(référence cachée)| pour chaque dose, sur CPU.
- H_A : M2_maître(1) − M2_maître(0) ≥ 0,15 décade
- H_B : M2_maître(1) − M2_maître(0) < 0,15 décade
- Si H_B : le bras B ne peut pas atteindre P3 même avec une distillation parfaite. Arrêt.
- Ce calcul précède tout entraînement et tout scellement final.

---

## (b) Expériences corrigées — séquence

**Étape 0 (CPU, avant scellement, compatible R1) :**

| Vérification | Quantité | Seuil de porte | Si échec |
|---|---|---|---|
| Round-trip octet du témoin | Identité chaîne par chaîne | Identité exacte | Corriger la réécriture |
| f_active | Fraction d'épisodes dans classes ≥ 2 | ≥ 0,50 | Redéfinir les classes (version neuve, R12) |
| ICC intra-classe | σ²_entre / (σ²_entre + σ²_dans) sur 8 suites | ≥ 0,40 (illustratif) | Bras B non testable |
| M2_maître(p) | Contraste dose 1 − dose 0 sur le maître | ≥ 0,15 décade | Bras B non testable |
| f_active vs entropie contrôlée | Écart f_active réel − f_active produit-marginales | > 0,10 | Indicateurs quasi-indépendants, classes suspectes |

**Étape 1 (GPU, après scellement) : Distillation et évaluation.**

| Adaptateur | Données | Budget |
|---|---|---|
| Dose 0 (témoin monotone) × 2 graines | Couplage identité intra-classe | Même budget |
| Dose 1/4, 1/2, 1 | Couplage anti-monotone | Même budget |
| Couplage aléatoire intra-classe, dose Kendall = 1 | Permutation uniforme intra-classe | Même budget |

**Étape 2 (GPU, évaluation) :**

| Duel | Métrique | Niveau d'analyse | Test |
|---|---|---|---|
| P3 tendance | M2 par tâche × dose | Tâches (n = K) | Jonckheere-Terpstra unilatéral |
| P3 hausse terminale | M2(1) − M2(0) apparié | Tâches | Wilcoxon signé unilatéral |
| Fidélité distillation | M2_distill (teacher forcing) | Tâches × doses | Kruskal-Wallis apparié par tâche |
| Discrétion (P4 élève) | AUC base « mots et coût » | Tâches réservées | Intervalle de confiance AUC ; non jugeable si n < 100 par bras |
| Anti-monotone vs aléatoire | M2(anti-mono) − M2(aléatoire intra-classe) | Tâches | Wilcoxon signé |
| Témoin vs témoin (graine A vs B) | M2 (deux adaptateurs identité) | Tâches | Wilcoxon signé (plancher de bruit) |

---

## (c) Ce qui est établi, ce qui ne l'est pas, et l'expérience à faire en premier

### Ce qui est établi

- **P4 vaut pour le maître** : l'invariance des marginales du multiensemble de coûts et des indicateurs de forme est une conséquence algébrique de la construction du couplage (RAPPORTÉ, §3). C'est un préalable, pas un résultat (objection 1 des juges, RAPPORTÉ). **Statut : VÉRIFIÉ comme identité, à confirmer par audit mécanique M-3.**
- **Le round-trip de la réécriture est vérifiable** avant tout entraînement.
- **M2_maître(p) est calculable sur CPU** à partir des données honnêtes existantes, sans violer R1.
- **Les huit suites du modèle de base existent** (RAPPORTÉ) et permettent d'estimer σ²_dans et ICC.

### Ce qui n'est pas établi

- **ICC intra-classe :** aucune valeur n'est RAPPORTÉE. Sans elle, on ne sait pas si le réappariement anti-monotone déplace les coûts par rapport à la référence cachée ou permute du bruit (critique A, note transversale ; C, §b.2). **C'est l'inconnue la plus dangereuse.**
- **Taille des classes :** la distribution des tailles de classe n'est pas RAPPORTÉE (risque 1 de la conception, §6). f_active est inconnue.
- **Fidélité de la distillation :** aucun taux de transfert mesuré (HYPOTHÈSE de travail 3, §6). L'appariement élève-maître en génération libre n'est pas défini.
- **P4 pour l'élève :** l'écart de l'élève à l'invariance du maître est « mesuré » mais non quantifié (§6, risque 4). L'AUC de la base sur l'élève est inconnue.
- **Puissance statistique :** avec 8–16 tâches, la plupart des tests proposés (par toutes les propositions) ont une puissance faible. Ce n'est pas un choix de méthode, c'est une contrainte du jeu de données.
- **Séparation construction/évaluation :** aucune partition de tâches n'est actuellement prévue.

### L'expérience à faire en premier

**Porte P0 sur CPU (aucun GPU, aucune lecture de résultat d'élève, compatible R1) :**

1. Calculer la distribution des tailles de classe et f_active.
2. Estimer ICC par ANOVA à un facteur sur les huit suites honnêtes.
3. Calculer M2_maître(p) pour p ∈ {0, 1/4, 1/2, 1} contre la référence cachée (médiane basse de 8 suites).
4. Vérifier le round-trip octet par octet de la réécriture du témoin.

**Critères de passage :** f_active ≥ 0,50, ICC ≥ 0,40 (illustratif), M2_maître(1) − M2_maître(0) ≥ 0,15 décade, round-trip identique. **Si un critère échoue :** le bras B est suspendu. Si ICC < 0,40 et M2_maître(1) − M2_maître(0) < 0,15, le mécanisme ne peut pas produire l'effet attendu et aucune distillation ne le sauvera. L'économie est totale (zéro GPU, zéro risque de lecture prématurée).

**Justification de la priorité :** cette porte élimine ou valide simultanément les failles F1 (classes dégénérées), F2 (coûts proches), et la faille transversale (ICC) identifiée par A et formalisée par C. Elle est exécutable avant le scellement final du préenregistrement, elle ne touche pas les données de l'élève, et elle transforme le premier résultat du bras B — quel qu'il soit — en un résultat interprétable.

FIN-DE-CELLULE