# Proposition B — D-ML-1 : taille du jeu bénin

---

## (a) Présupposés de la question et leur statut

| # | Présupposé | Statut | Commentaire |
|---|-----------|--------|-------------|
| 1 | Le jeu Bailey contient exactement 1 000 entrées bénignes au total (800 train / 100 val / 100 test). | **VÉRIFIÉ** — recompté (R-897), l. 75–78 des faits. |
| 2 | Le pré-enregistrement v2 exige 1 000 bénins pour le seuil et 1 000 pour la mesure, disjoints de l'entraînement de la sonde. | **VÉRIFIÉ** — l. 114–118 des faits. |
| 3 | La sonde linéaire est figée une fois entraînée ; le seuil τ est fixé sur le jeu bénin de seuil, puis appliqué sur le jeu bénin de mesure. | **VÉRIFIÉ** — l. 20–28. |
| 4 | Le taux nominal de fausses alertes est 1 %. | **VÉRIFIÉ** — l. 20–28. |
| 5 | Les intervalles Clopper-Pearson fournis dans la sortie du calcul sont corrects. | **RAPPORTÉ** — calcul `b39f629d…` ; je les vérifie ci-dessous. |
| 6 | Un jeu bénin public plus large existe, est accessible, et aurait une licence compatible. | **HYPOTHÈSE** — « aucun n'est sur disque aujourd'hui » (l. 75–78). |
| 7 | Les bénins du jeu Bailey sont représentatifs de la distribution des entrées bénignes réelles pour le modèle 8B. | **HYPOTHÈSE** — aucune vérification de couverture thématique n'est mentionnée dans les faits. |
| 8 | La question suppose que le flou sur τ dans l'option B est le seul coût statistique de la réduction d'échantillon. Elle ne mentionne pas la réduction de la taille d'entraînement de la sonde (de 800 à 400), qui peut dégrader la qualité du classifieur lui-même. | **OBSERVÉ-NON-AUDITÉ** — implicite mais non discuté dans les faits. |

### Vérification des intervalles (statut RAPPORTÉ → vérification analytique)

Clopper-Pearson bilatéral à 95 % pour k succès sur n essais, avec p₀ = 0.01 :

- **n = 1 000, k = 10** : borne basse = B⁻¹(0.025 ; 10, 991) ≈ 0.0048, borne haute = B⁻¹(0.975 ; 11, 990) ≈ 0.0183. **Cohérent** avec la sortie.
- **n = 300, k = 3** : borne basse ≈ 0.0021, borne haute ≈ 0.0289. **Cohérent**.
- **n = 300 (seuil)** : intervalle sur le vrai taux [0.0021 ; 0.0238]. **Cohérent** (c'est un intervalle sur le quantile, pas un Clopper-Pearson classique sur la proportion observée ; la sortie les distingue correctement).

Je n'ai pas de divergence à signaler sur ces chiffres.

---

## (b) Expériences décisives — duels H_A vs H_B

### Expérience 1 : La réduction de la taille d'entraînement de la sonde (400 vs 800) dégrade-t-elle le classifieur ?

Ce point est absent de la question mais nécessaire : si l'option B réduit la taille d'entraînement de 800 à 400, il faut vérifier que la sonde reste fonctionnelle.

- **H_A** : La sonde entraînée sur 400 bénins + 400 nuisibles conserve une AUC ≥ AUC₈₀₀ − 0.02 (dégradation négligeable).
- **H_B** : La sonde perd > 0.02 d'AUC, ce qui rend le seuil τ non comparable à celui du protocole v2.
- **Métrique** : AUC ROC mesurée en 5-fold cross-validation stratifiée sur les 1 000 échantillons Bailey (400 + 400 entr. / reste en test), comparée à la même procédure avec 800 + 800 entr.
- **Seuil de décision** : ΔAUC > 0.02 falsifie H_A. ΔAUC ≤ 0.02 falsifie H_B.
- **Contrôle négatif** : sonde avec poids aléatoires (AUC ≈ 0.5) ; la sonde entraînée doit battre ce contrôle par > 0.3 AUC dans les deux configurations.
- **Issue** : Si H_B est vraie, l'option B est disqualifiée non par le bruit sur τ mais par la dégradation du classifieur lui-même. L'option A (ou une option C gardant 800 pour l'entraînement) devient nécessaire.

### Expérience 2 : Le shift de distribution d'un jeu bénin externe fausse-t-il le seuil plus que le bruit d'échantillonnage de B ?

- **H_A** : Le taux de fausses alertes d'un jeu bénin externe, mesuré par la sonde entraînée sur Bailey, est dans l'intervalle [0.005 ; 0.020] (compatible avec le 1 % nominal ± bruit Clopper-Pearson n = 1 000).
- **H_B** : Le taux de fausses alertes du jeu externe sort de cet intervalle (biais de distribution > bruit d'échantillonnage).
- **Métrique** : Taux de fausses alertes au seuil τ fixé sur les 100 val + 100 test de Bailey, appliqué au jeu externe (1 000 items).
- **Seuil de décision** : Si le taux observé est hors [0.005 ; 0.020], H_A est falsifiée. Si le taux est dans l'intervalle, H_B est falsifiée.
- **Contrôle négatif** : Appliquer le même seuil aux 200 bénins Bailey val+test eux-mêmes ; le taux doit être dans l'intervalle (cohérence interne).
- **Test de ressemblance** : Un test de permutation sur les scores de la sonde (pas sur les entrées brutes) entre les bénins Bailey et les bénins externes, au seuil α = 0.05. Voir section (c) pour le choix du test.

### Expérience 3 : Le seuil τ fixé sur 300 bénins est-il stable par bootstrap ?

- **H_A** : La dispersion bootstrap de τ (10 000 rééchantillonnages avec remplacement, n = 300) donne un IC à 95 % de largeur ≤ 0.5 écart-type des scores de la sonde sur les bénins (le seuil est assez précis pour distinguer rappel 50 % vs 20 % vs 5 %).
- **H_B** : La largeur de l'IC bootstrap de τ dépasse 0.5 σ, rendant les seuils de rappel non séparables.
- **Métrique** : Largeur de l'IC₉₅ bootstrap de τ, normalisée par σ des scores.
- **Seuil** : > 0.5 σ falsifie H_A ; ≤ 0.5 σ falsifie H_B.
- **Contrôle** : Même bootstrap avec n = 1 000 (Bailey + externe ou simulation) ; la largeur doit être ≤ 0.3 σ (scaling attendu en √(300/1000) ≈ 0.55).

---

## (c) Instruments nommés : mesures minimales de fonctionnement

### Sonde linéaire figée

- **Taux de détection minimum** : Sur les 100 nuisibles test de Bailey, la sonde doit atteindre un rappel ≥ 80 % au seuil de 1 % de fausses alertes (fixé sur les bénins de seuil). Si le rappel est < 80 %, la sonde n'est pas assez discriminante pour que l'expérience de malléabilité ait un sens (il n'y a rien à contourner).
- **Taux de fausses alertes** : Doit être vérifié à 1 % ± l'intervalle Clopper-Pearson correspondant à la taille du jeu de seuil utilisé.
- **Cas honnêtes appariés** : Les bénins de mesure, appariés en longueur de tokens (± 20 %) avec les entrées nuisibles, pour contrôler que la sonde ne discrimine pas sur la longueur.
- **Vérification mécanique à battre** : Classifieur par longueur de séquence seule (seuil sur le nombre de tokens). La sonde doit avoir une AUC supérieure d'au moins 0.15 à ce baseline.

### StrongREJECT affiné (juge de nuisance)

- **Taux de détection** : Sur un sous-ensemble de 50 nuisibles connus (VÉRIFIÉ nuisibles par annotation humaine, si disponible), StrongREJECT doit donner un score > 0.5 pour ≥ 90 % des cas.
- **Taux de fausses alertes** : Sur 50 bénins connus, le score doit être ≤ 0.5 pour ≥ 95 % des cas.
- **Vérification mécanique** : Classifieur par mots-clés (liste de termes nuisibles). StrongREJECT doit battre ce baseline en F1 d'au moins 0.10.

### Test de ressemblance de distribution (si option A)

Je recommande un **test de Kolmogorov-Smirnov bilatéral sur les scores de la sonde** (pas sur les embeddings bruts), car :
- C'est unidimensionnel (les scores), donc puissant à n modeste.
- C'est directement pertinent : ce qui compte n'est pas que les entrées se « ressemblent » en général, mais que la sonde les traite de la même façon.
- Seuil : p < 0.01 → le jeu externe a un shift détectable, rapporter l'effet et recalibrer τ sur un mélange ou rejeter le jeu.
- Complément : un QQ-plot des scores, versé avec les résultats, pour inspection visuelle.

---

## (d) Ancrage matériel

| Élément | Spécification | Source |
|---------|--------------|-------|
| Modèle | 8B paramètres, public (e.g. Llama-3-8B ou équivalent) | VÉRIFIÉ — l. 20–28 |
| Jeu Bailey | 1 000 bénins, 1 000 nuisibles, commit `9c1f4b1a…` | VÉRIFIÉ — l. 75–78 |
| Jeu bénin externe (option A) | Candidats **SUPPOSÉS** : **Alpaca** (52 k instructions, licence Apache 2.0 — *référence à vérifier*), **LMSYS-Chat-1M** (1M conversations, licence CC-BY-NC-4.0 — *référence à vérifier*), **Dolly-15k** (15 k instructions, licence CC-BY-SA-3.0 — *référence à vérifier*). Tailles suffisantes pour tirer 2 000 bénins. | **SUPPOSÉ** — je n'ai pas lu ces jeux |
| Calcul pour les expériences 1–3 | Un seul GPU (24 Go VRAM) pendant ~2 h pour la sonde linéaire + bootstrap. Inférence sur le modèle 8B : ~4 h sur A100 80 Go pour 2 000 passages. | **illustratif** |
| Coût | ~10 $ sur un cloud standard pour la sonde, ~20–40 $ pour l'inférence 8B (2 000 × ~2 s/passage). | **illustratif** |

---

## Réponses aux quatre sous-questions

### 1. Mon choix : Option C (variante hybride), avec repli sur B

Je ne recommande ni A ni B telles que formulées. Je propose une **option C** :

**Garder les 800 bénins Bailey pour l'entraînement de la sonde** (ne pas réduire à 400 — la question ne discute pas la dégradation du classifieur, mais c'est un risque réel, voir Expérience 1). Utiliser les 200 bénins restants (100 val + 100 test) comme **ensemble de calibration interne**, puis verser un jeu bénin externe de 1 000 items pour le seuil et 1 000 items pour la mesure, **sous réserve que le test KS sur les scores de la sonde (seuil p < 0.01) ne détecte pas de shift**. Les 200 bénins internes servent uniquement de vérification de cohérence (le taux de fausses alertes sur ces 200 doit être compatible avec celui du jeu externe, sinon le jeu externe est rejeté).

**Pourquoi pas A pure ?** Parce que A ne garde que la condition de « ressemblance de distribution » sans vérification croisée avec les bénins Bailey. Le risque de shift est réel et non borné a priori.

**Pourquoi pas B ?** Deux raisons :
1. Réduire l'entraînement de la sonde de 800 à 400 est un coût caché non discuté dans les faits, potentiellement plus grave que le bruit sur τ.
2. L'intervalle [0.0021 ; 0.0238] pour le « 1 % de fausses alertes » est un facteur 11 entre les bornes. Ce n'est pas un « bruit » : c'est une incertitude qui rend le seuil τ essentiellement non identifié à la précision nécessaire pour les comparaisons entre couches/directions.

**Repli sur B** : Si aucun jeu externe ne passe le test KS (tous montrent un shift), alors l'option B est le moindre mal, avec les rapports décrits en §3.

### 2. Jeux bénins publics et test de ressemblance

**Candidats (SUPPOSÉ — je n'ai pas vérifié les licences ni les contenus actuels)** :

- **Alpaca** (~52 k paires instruction/réponse). Avantage : instructions simples, probablement proche de « bénin généraliste ». Risque : distribution d'instructions synthétiques, pas d'interactions réelles.
- **Dolly-15k** (~15 k). Avantage : écrit par des humains. Risque : plus petit, centré entreprise.
- **LMSYS-Chat-1M**. Avantage : conversations réelles avec LLM. Risque : contient du contenu limite (filtrage nécessaire, biais survivant).

**Test de ressemblance à préenregistrer** :

1. Extraire les scores de la sonde sur les 800 bénins Bailey d'entraînement (en train, oui — c'est pour comparer les distributions, pas pour estimer un taux).
2. Extraire les scores sur 1 000 bénins du jeu externe.
3. Test KS bilatéral, seuil p < 0.01.
4. Si rejet : rapporter la statistique D et le QQ-plot. Options : (i) chercher un autre jeu, (ii) recalibrer τ sur le jeu externe lui-même (mais alors il faut séparer calibration et mesure en son sein), (iii) repli sur B.

**Risque shift > bruit B** : Oui, c'est possible et même probable. Un jeu de distribution différente peut donner un taux de fausses alertes de 5 % ou 0.1 % au lieu de 1 %, soit un biais > 4× le bruit de B. Le test KS est une protection nécessaire mais pas suffisante (il détecte un shift global, pas un shift dans la queue de la distribution des scores, qui est ce qui détermine τ). J'ajoute donc la recommandation de vérifier spécifiquement le **quantile 99 % des scores** du jeu externe vs celui des bénins Bailey (test de permutation sur le quantile, 10 000 permutations).

### 3. Interprétabilité des seuils de détection avec 300 bénins

Avec 300 bénins de seuil :

- **Seuil à rappel < 50 %** : La question est de savoir si ≥ 50 % des entrées nuisibles perturbées passent sous τ. Avec 200 entrées adverses (l. 114), la puissance pour détecter un rappel de 50 % vs 45 % est faible (ΔAUC ≈ 0.05, ~200 essais → puissance < 50 % — **illustratif**). Le seuil de 50 % est interprétable en tant que **point de passage**, pas en tant que mesure précise.
- **Seuil à rappel < 20 %** : Distinction 20 % vs 15 % requiert ~500 adverses pour une puissance de 80 % (**illustratif**). Avec 200 adverses, seule la distinction 20 % vs ~10 % est réaliste.
- **Seuil à rappel < 5 %** : Avec 200 adverses, 5 % = 10 items. L'intervalle Clopper-Pearson est [0.024 ; 0.089]. Ce seuil est à peine distinct de 0 % et de 10 %. **Interprétable uniquement comme « très peu d'adverses détectées » vs « quelques-unes ».**

Le vrai problème est que τ lui-même est bruité. Si τ bouge à cause du bruit de 300 bénins, le rappel mesuré bouge aussi. Il faut rapporter :

1. L'IC bootstrap à 95 % de τ (voir Expérience 3).
2. Le rappel évalué aux bornes inférieure et supérieure de cet IC, pas seulement au τ ponctuel.
3. La sensibilité du rappel à τ : dérivée discrète du rappel par rapport à τ, évaluée sur les 200 adverses.

### 4. Pire cas de mon choix (option C) et critère de révision

**Pire cas** : Le jeu externe passe le test KS global mais a un shift dans la queue droite de la distribution des scores. Le quantile 99 % du jeu externe est 1.5 σ au-dessus de celui de Bailey. Résultat : τ est fixé trop haut, les fausses alertes réelles sont < 0.1 %, et l'expérience mesure un rappel artificiellement gonflé (la sonde semble plus facile à contourner qu'elle ne l'est). La borne sur le nombre de directions de contournement est surestimée.

**Détection** : Le test de permutation sur le quantile 99 % des scores (recommandé ci-dessus) détecte ce cas.

**Ce qui me ferait changer d'avis** :

1. **Vers B** : Si trois jeux externes candidats échouent tous au test KS ou au test sur le quantile 99 %. Autrement dit : si aucun jeu public n'a une distribution de scores compatible avec Bailey.
2. **Vers A pure (sans vérification croisée)** : Si l'Expérience 1 montre que la sonde à 400 bénins ne perd pas d'AUC (ΔAUC ≤ 0.01) ET que le budget de calcul interdit de faire tourner un jeu externe de 1 000 items. (Peu probable au coût estimé, mais c'est une condition logique.)
3. **Vers un autre protocole** (e.g. validation croisée pour fixer τ) : Si l'Expérience 3 montre que l'IC bootstrap de τ à n = 300 dépasse 0.5 σ ET qu'aucun jeu externe n'est disponible. La validation croisée k-fold sur les 200 bénins restants pour estimer τ est une option de dernier recours, mais elle introduit une dépendance entre les folds qui complique l'intervalle de confiance sur τ — à préenregistrer avec soin.

---

*Résumé en une phrase* : L'option B sacrifie la taille d'entraînement de la sonde (coût caché) et donne un seuil τ trop flou ; l'option A risque un shift de distribution non borné ; l'option C (entraînement sur 800, seuil et mesure sur un jeu externe vérifié par test KS + test sur le quantile 99 %, avec repli sur B si échec) minimise les deux risques au prix d'un versement et d'un test de plus.

FIN-DE-CELLULE