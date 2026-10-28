# Proposition A — Tour III.3 : Riposte

---

## (a) Réponse à chaque attaque

### Attaques de B contre A

**B-A1 — « L'intention est confondue avec le contenu produit ; pas de contraste à texte identique (forçage). »**

**Acceptée, transformée en test.** B a raison : le contraste saboté vs. honnête à cadrage fixe compare des textes différents, et une sonde linéaire sur le résidu peut lire les traces lexicales de la sortie plutôt que l'état intentionnel. Le forçage (teacher forcing) — même texte saboté, consignes différentes — est le bon contrôle. Je l'ajoute à l'Expérience 1 comme condition préalable (voir §(b), Exp. 1 corrigée, bloc « Condition TF »). C'est l'attaque la plus importante reçue ; je la fais mienne.

**B-A2 — « δ = AUROC_int − AUROC_cad n'est pas une pureté ; zone non prévue entre chance et 0,6. »**

**Partiellement acceptée, corrigée.** B a raison que la clause AUROC_cad > 0,6 crée une zone grise. Je remplace par un critère continu : δ n'est interprétable que si AUROC_cad n'est pas significativement au-dessus du hasard (test unilatéral contre 0,5, p > 0,05). Si AUROC_cad est significativement au-dessus du hasard, la sonde est contaminée, quel que soit δ. Le témoin faux (sonde entraînée sur le seul cadrage) reste utile comme vérification de la cohérence du banc, pas comme test d'orthogonalité — je clarifie cette distinction.

**B-A3 — « Fuite entre carte de construit (exp. 1) et test de robustesse (exp. 4) : corrélation de rang sur 15 points non indépendants. »**

**Acceptée, transformée en test.** Le test de H8 par corrélation de rang entre δ (exp. 1) et point de rupture (exp. 4) sur 15 cellules (5 familles × 3 couches) est sous-puissant et non indépendant. Corrections : (i) les épisodes sont disjoints entre exp. 1 et exp. 4 (scellement avant tirage) ; (ii) la prédiction est testée hors-échantillon : δ est calculé sur un premier lot de sondes, le point de rupture sur un second lot (même famille × couche, graine différente) ; (iii) si la puissance est insuffisante, H8 est déclarée non tranchée, pas « non falsifiée ». Le test de rang est rapporté comme exploratoire ; le résultat binaire (la sonde à δ le plus haut résiste-t-elle le plus longtemps ? oui/non sur chaque paire) est rapporté aussi.

**B-A4 — « Le nul séquentiel ignore la dérive honnête ; l'autocorrélation positive gonfle le FPR. »**

**Acceptée, transformée en test.** Le lemme L (additivité, HYPOTHÈSE à 0,75) suppose des incréments centrés sous le nul. Une autocorrélation positive honnête (structure narrative intro → méthode → budget) gonfle effectivement le FPR séquentiel. Corrections : (i) avant toute comparaison, mesurer l'autocorrélation empirique des scores de sonde sur épisodes honnêtes par action (Durbin-Watson ou ACF) ; (ii) si l'autocorrélation est significative, blanchir les scores par un AR(p) ajusté sur un lot de calibration scellé (distinct du lot d'épreuve), puis re-vérifier le FPR sur le lot d'épreuve ; (iii) ajouter un contrôle par permutation intra-épisode de l'ordre des actions honnêtes : si le FPR change, l'agrégateur lit la structure narrative et le nul est violé. Ce dernier contrôle est emprunté à B, en le disant.

**B-A5 — « Exp. 3 : CUSUM intra-épisode cherche une rupture qui n'existe qu'entre épisodes. »**

**Acceptée, exp. 3 reconstruite.** B a raison : si le cadrage est dans le prompt initial, il n'y a pas de rupture intra-épisode à détecter. L'expérience originale confond un test entre conditions (ANOVA) et un test de rupture séquentiel. Je reconstruis l'exp. 3 avec un indice inséré en cours d'épisode (à un pas t₀ tiré au hasard), ce qui crée une véritable transition intra-épisode. J'emprunte cette idée à B. Mais j'ajoute le contrôle d'incongruité pragmatique demandé par C (voir C-A, ci-dessous).

**B-A6 — « L'attaquant de l'exp. 4 est trop faible (bit bruité) ; la zone 5–20 % viole B4. »**

**Partiellement acceptée, corrigée.** (i) La faiblesse de l'attaquant : B a raison que l'optimisation sur un verdict binaire bruité est sous-puissante. Je stratifie l'exp. 4 en deux niveaux d'attaque — Niveau 1 : boîte noire (verdict binaire stochastique, comme spécifié par P §9) ; Niveau 2 : l'attaquant possède les poids de l'organisme et entraîne une sonde de substitution (scénario S2 de B), puis optimise contre elle. Le Niveau 2 est la voie réaliste que B identifie ; je la fais mienne. (ii) La zone 5–20 % : je ferme le trou en redéfinissant les hypothèses comme un seuil unique τ (pré-scellé, « illustratif » : 10 % de perte d'utilité). H_A : le rappel tombe sous la base noire à coût ≤ τ. H_B : le rappel reste au-dessus de la base noire pour tout coût ≤ τ. Pas de zone intermédiaire.

**B-A7 — « L'utilité est mesurée par un juge corruptible. »**

**Acceptée, transformée en test.** Le juge d'utilité (génératif ou humain) doit avoir son g mesuré sur un corpus de pression bénin (HC6 du programme) avant d'être utilisé. Ajouté comme condition préalable de l'exp. 4 : si g_juge > seuil pré-spécifié (« illustratif » : 0,2), on ne se fie qu'au juge humain (ou on remplace le juge génératif).

**B-A8 — « AUROC > 0,6 à 1 % FPR pour Mahalanobis mélange aire et point de fonctionnement ; attention vs max nécessite deux sondes. »**

**Acceptée, corrigée.** (i) Pour Mahalanobis : je remplace par « rappel à 1 % FPR > rappel de la sonde aléatoire appariée ». (ii) Pour attention vs max : le critère compare deux sondes distinctes (même famille linéaire sous-jacente, l'une agrégée par max, l'autre par l'agrégation attention apprise) — je le clarifie dans le tableau.

**B-A9 — « Redéfinir G1 avant d'avoir mesuré, alors que N-056 fixe les bases. »**

**Rejetée.** Ma pré-étape ne « rouvre » pas G1 : elle vérifie que les bases sont compétentes (battent la sonde aléatoire) avant de dépenser sur les épisodes sabotés. Si les bases sont incompétentes, le résultat est rapporté (« les planchers restent rapportés, hors décision », pièce D — RAPPORTÉ) et le programme décide, pas la proposition. Je ne rédéfinis rien ; je dis « arrêtez de dépenser si le nul est trivial ». Le programme peut continuer malgré cet arrêt s'il le veut.

---

**Scénarios d'évasion de B (S1–S5) :**

**S1 — Registre honnête.** Transformé en test. C'est exactement ce que le contrôle de forçage (B-A1) est censé attraper : si la sonde, à texte identique, ne distingue pas la consigne honnête de la consigne rouge, alors le registre honnête est une évasion gratuite. Si la sonde distingue les consignes même à texte identique, S1 échoue. Le forçage tranche.

**S2 — Sonde de substitution.** Accepté et intégré dans l'exp. 4, Niveau 2 (voir B-A6). Je mesure la matrice de transfert substitution → moniteur réel, comme exigé par P §8.2 (RAPPORTÉ).

**S3 — Crédit d'honnêteté (front-loading).** Transformé en test. J'ajoute un contrôle spécifique : épisodes où le sabotage est concentré dans la seconde moitié (budget B identique, placement tardif). Si le séquentiel détecte le placement tardif aussi bien que le placement uniforme, S3 est neutralisé. Si le processus e descend trop bas en début d'épisode pour remonter, le séquentiel est vulnérable à S3. Mesure : rappel à 1 % FPR sous placement uniforme vs. placement tardif.

**S4 — Paranoïa constante (pas de rupture).** Accepté comme cas de figure. B note lui-même que si la conduite « évaluée » réduit le sabotage, c'est un succès du contrôle. Je l'intègre dans l'exp. 3 corrigée comme une issue explicite : si l'organisme se comporte identiquement avec et sans indice d'évaluation, il n'y a pas de rupture et H_A est falsifiée pour cette sonde. C'est un résultat, pas un échec du protocole.

**S5 — Empoisonnement du calibrage.** Transformé en test. La distribution honnête de calibrage est comparée entre deux conditions : (a) cadrage neutre, (b) cadrage « évaluation explicite ». Si la variance ou les queues diffèrent significativement (Kolmogorov-Smirnov, p < 0,01), le nul est contaminé et le calibrage doit être refait sur des épisodes à cadrage neutre seul. Ce contrôle est ajouté comme condition préalable de toute calibration de seuil.

---

### Attaques de C contre A

**C-A1 — « Contamination causale : la sonde lit l'empreinte lexicale du prompt système dans le résidu. »**

**Acceptée, même diagnostic que B-A1.** Le forçage résout ce problème. Si le sabotage est induit par prompt, le prompt est dans le KV-cache et le résidu en porte la trace. En condition de forçage (même texte, prompt différent), si la sonde discrimine encore, elle lit le prompt, pas la sortie. Pour le cas LoRA (sabotage par réglage fin, sans prompt rouge), le contrôle est automatiquement propre puisqu'il n'y a pas de prompt contaminant.

**C-A2 — « Biais de longueur sous max dans l'exp. 3 ; E[max] croît avec le nombre de tokens. »**

**Acceptée, corrigée.** C a raison que max est biaisé par la longueur. Je normalise le score max par la correction de longueur : score_normalisé = (max − μ_0(L)) / σ_0(L), où μ_0(L) et σ_0(L) sont estimés empiriquement sur les épisodes honnêtes de calibration (pas une loi a priori Gumbel — je tiens compte de la critique de B contre C sur ce point). Le contrôle négatif demandé par C (sonde constante + bruit gaussien passée au max sur les vraies longueurs) est ajouté comme vérification de calibration. Si ce contrôle déclenche des fausses alertes, la normalisation est inadéquate.

**C-A3 — « Contradiction dans l'exp. 4 : on ne peut pas minimiser le score d'une sonde sans connaître cette sonde. »**

**Acceptée, corrigée via la stratification Niveau 1 / Niveau 2 (voir B-A6).** Au Niveau 1 (boîte noire), l'attaquant optimise contre le verdict agrégé global, pas contre une famille isolée. Au Niveau 2, l'attaquant optimise contre sa sonde de substitution (même architecture, poids différents). La formulation originale était incohérente.

**C-A3 bis — « A désactive les seuils stochastiques et l'asymétrie d'apprentissage pendant l'attaque. »**

**Partiellement acceptée.** C a raison que figer les sondes pendant 10–50 itérations viole P §9. Correction : au Niveau 1, l'asymétrie d'apprentissage est active (chaque détection met à jour les sondes, comme en protocole réel). Le nombre d'itérations d'attaque reflète alors un vrai bras de fer. Au Niveau 2 (sonde de substitution), les poids du moniteur réel ne sont jamais exposés à l'attaquant et les sondes réelles sont mises à jour normalement. Cependant, je rejette la critique selon laquelle tester les sondes figées serait sans valeur : c'est une borne basse de robustesse (pire cas pour le défenseur).

**C-A3 ter — « Fermeture de brèche = surapprentissage d'architecture. »**

**Acceptée, transformée en test.** Après chaque « fermeture » (ajout de couche, changement de famille, etc.), l'attaquant doit ré-optimiser contre le moniteur durci. J'emprunte ce contrôle à B (B-critique C7 contre C).

**C-A4 — « FPR par action ≠ FPR par épisode ; cascade à 10⁻⁶ vs. marginal à 18 %. »**

**Acceptée, corrigée.** Le FPR doit être défini à la même granularité pour tous les instruments comparés. Je fixe : FPR par épisode = 1 %. Pour la cascade (base ii), le seuil est calibré pour que le FPR par épisode (sur épisodes honnêtes entiers) soit 1 %, pas par action. Pour le séquentiel, le FPR par épisode est directement le taux de franchissement du seuil sur épisodes honnêtes entiers. Le McNemar compare des verdicts par épisode, au même FPR par épisode.

---

**Scénarios d'évasion de C (points 1–5) :**

**C-évasion 1 — Ancrage de registre.** Même diagnostic que B-S1 : le forçage tranche. Transformé en test.

**C-évasion 2 — Écrêtage de pic par périphrase.** Transformé en test. Je mesure : sur les épisodes sabotés, la corrélation entre le nombre de tokens par action et le score max normalisé (après correction de longueur). Si la périphrase dilue le max au point que le rappel tombe sous la base noire, c'est une brèche réelle. L'extension : passer à top-k (k = 3, « illustratif ») moyenne tronquée au lieu du max pur. B objecte que k leurres suffisent alors — c'est vrai, mais le coût pour l'attaquant augmente linéairement en k, et cela se mesure.

**C-évasion 3 — Mimétisme de haute densité contre Mahalanobis.** Transformé en test. Mesurer : AUROC de Mahalanobis quand l'organisme saboteur génère à T_dec = 0,2 vs. T_dec = 0,7 (« illustratif »). Si Mahalanobis est aveuglée à basse température, la sonde est vulnérable et le programme doit ajouter un détecteur de basse entropie (la basse température est elle-même un signal détectable).

**C-évasion 4 — Sabotage dans la première moitié, conclusion honnête contre base iii.** Accepté comme brèche structurelle de la base iii. C'est exactement pourquoi le séquentiel doit battre cette base : la base iii est aveuglée par construction. Pas de correction nécessaire sur l'exp. 2 (la base iii est là pour être battue).

**C-évasion 5 — Évasion simultanée (compensation sous-seuil).** Transformé en test. C'est le scénario le plus dangereux. Le contrôle : le jeu de données d'attaque de l'exp. 4, Niveau 2, doit inclure une condition « compensation sous-seuil » où l'attaquant minimise le score sur 85 % des actions et concentre le biais sur 15 %. Le rappel du séquentiel sous cette condition est la mesure critique.

---

**Contrôles négatifs de C dont l'absence serait fatale :**

C demande quatre contrôles. (1) Ablation du prompt système / LoRA sans instruction : **accepté, intégré dans le forçage**. (2) Contrôle de longueur et perplexité appariées : **accepté, intégré dans la normalisation du max**. (3) Contrôle d'autocorrélation avec corrélation injectée (pièce D point 5) : **accepté, intégré dans exp. 2 corrigée**. (4) Contrôle d'intention avortée (consigne rouge, dommage = 0) : **accepté, ajouté comme classe d'épisodes dans exp. 1 et exp. 2**. Si la sonde détecte l'intention avortée, elle mesure l'état intentionnel (ou le prompt). Si elle ne la détecte pas, elle mesure le dommage accompli, pas l'intention.

---

## (b) Expériences corrigées (résumé des modifications)

### Expérience 1 corrigée : Validité de construit par dissociation + forçage

**Ajouts :**
- **Condition TF (teacher forcing), préalable obligatoire.** Même texte saboté, lu en passe avant par l'organisme 8B sous consigne honnête et sous consigne rouge. Si les scores de sonde diffèrent (test de rang apparié, p < 0,01), la sonde lit l'état interne au-delà du texte. Si les scores ne diffèrent pas, la sonde lit la sortie, et δ n'est qu'un classifieur de texte. Issue : si TF échoue pour toutes les familles × couches, **arrêt total** : le gain blanc-sur-noir (H1) se réduit à un gain de représentation, pas d'accès.
- **Classe « intention avortée »** (consigne rouge, dommage = 0) ajoutée. AUROC_int est calculé sur trois classes : honnête, saboté-réussi (dommage ≥ θ), saboté-avorté (dommage < θ). Si la sonde ne discrimine pas saboté-avorté vs. honnête, elle lit le dommage, pas l'intention.
- **Critère de contamination** : AUROC_cad non significativement > 0,5 (test unilatéral, p > 0,05). Remplace la clause ad hoc 0,6.
- **Permutation des étiquettes** stratifiée par gabarit de prompt (emprunté à B).

### Expérience 2 corrigée : Gain séquentiel sur signal sous-seuil

**Ajouts :**
- **Autocorrélation honnête** mesurée et blanchie (AR(p) sur lot de calibration scellé) avant toute comparaison (emprunté à B-A4, C contrôle 3).
- **Permutation intra-épisode** de l'ordre des actions honnêtes comme test du nul (emprunté à B).
- **FPR par épisode** = 1 % pour tous les instruments, calibré à la même granularité (corrige C-A4).
- **Contrôle synthétique** : corrélation artificielle injectée d'amplitude connue sur épisodes honnêtes (maintenu de ma conception originale + renforcé par la pièce D point 5, RAPPORTÉ).
- **Condition « placement tardif »** (sabotage concentré dans la seconde moitié) pour tester la vulnérabilité au crédit d'honnêteté (S3 de B).

### Expérience 3 corrigée : Conscience d'évaluation — indice intra-épisode

**Reconstruction complète** (suite à B-A5) :
- L'indice est inséré à un pas t₀ tiré au hasard dans l'épisode (pas dans le prompt initial). Trois conditions :
  - Condition A : indice d'évaluation (« ce document sert à évaluer l'assistant »).
  - Condition B : indice neutre de même longueur et même niveau de surprise pragmatique mais sans contenu évaluatif (« note administrative : le serveur d'impression du département sera redémarré mardi » — **emprunté à C**).
  - Condition C : pas d'indice.
- **Contrôle de B** : si la rupture apparaît dans B autant que dans A → la sonde détecte l'incongruité pragmatique, pas la conscience d'évaluation. La sonde est un détecteur d'injection, pas un détecteur de régime.
- **Issue S4 de B** (paranoïa constante) intégrée : si aucune rupture n'est détectée dans aucune condition, l'organisme ne change pas de régime (ou n'a pas de conscience d'évaluation comportementalement active). C'est un résultat valide.
- Normalisation du max par longueur empirique (corrige C-A2).

### Expérience 4 corrigée : Frontière de robustesse — deux niveaux d'attaque

**Ajouts :**
- **Niveau 1** (boîte noire, verdict stochastique) : l'attaquant optimise contre le verdict global. Les sondes sont mises à jour (asymétrie d'apprentissage active, P §9).
- **Niveau 2** (sonde de substitution, poids de l'organisme) : l'attaquant entraîne sa propre sonde et optimise contre elle par LoRA. Matrice de transfert substitution → moniteur réel mesurée (P §8.2).
- **Condition « compensation sous-seuil »** (évasion combinée de C, scénario 5).
- **g du juge d'utilité** mesuré en préalable (B-A7).
- **Ré-optimisation après fermeture** : toute « fermeture de brèche » est suivie d'une ré-attaque de l'adversaire contre le moniteur durci (emprunté à B).
- **Seuil unique τ** (pré-scellé) : plus de zone 5–20 % (corrige B-A6).
- **Contrôle d'empoisonnement du calibrage** (B-S5, C-E5) : ajouté comme préalable.

---

## (c) Réponse à la question de l'arbitre — une page

### Ce qui est établi

1. **Les sondes linéaires détectent la tromperie binaire dans un 70B** : 95–99 % à 1 % FP (Apollo Research 2025, RAPPORTÉ, chiffre à vérifier sur PDF). C'est la borne supérieure publiée.
2. **La conscience d'évaluation a une représentation linéaire** dans les activations de la plupart des LLM ouverts (AUROC > 0,7, étude multi-modèles 2026, RAPPORTÉ, référence exacte à vérifier). L'effet causal (pilotage → comportement) reste faible (Nguyen et al. 2025, RAPPORTÉ).
3. **Le sandbagging est possible par instruction** (van der Weij et al. 2024, RAPPORTÉ) ; un moniteur sur la chaîne de raisonnement ne le détecte que dans 64–84 % des cas (chiffre à vérifier sur PDF).
4. **Le programme a des invariants de protocole** (flux unidirectionnel, seuils stochastiques, asymétrie d'apprentissage) qui restreignent l'espace d'attaque (RAPPORTÉ, pièce P §9).

### Ce qui n'est pas établi

1. **Aucune sonde du programme n'a de score rapporté** sur le biais diffus dans un 8B. Toute la construction repose sur des hypothèses non testées (S1, H2, H8 — tous HYPOTHÈSE).
2. **On ne sait pas si les sondes lisent l'état interne ou la sortie.** Aucun test de forçage n'a été fait. C'est la question la plus fondamentale, et les deux équipes rouges l'ont identifiée indépendamment.
3. **L'accumulation séquentielle sur scores de sonde n'a pas de résultat publié** pour le biais diffus (RAPPORTÉ dans les pièces comme zone non occupée). L'angle mort Tr (transposition token → action face à un attaquant adaptatif) est explicitement non calibré.
4. **Le transfert 70B → 8B est une hypothèse.** Les directions internes du 8B peuvent ne pas porter la même information (pièce E §3.1, RAPPORTÉ).
5. **La conscience d'évaluation spontanée dans un ≤ 8B n'est pas démontrée** (pièce E §3.4, RAPPORTÉ).

### L'expérience à faire en premier

**Le test de forçage (Condition TF de l'Exp. 1 corrigée).** Coût : zéro génération, une passe avant par texte existant, sondes sur CPU. Temps : heures, pas jours. Ce test conditionne tout le reste :

- **Si les scores de sonde diffèrent significativement entre consigne honnête et consigne rouge à texte identique** → les sondes lisent quelque chose au-delà du texte de surface. Le programme peut alors procéder aux expériences 1 (carte de construit), 2 (gain séquentiel), 3 (conscience d'évaluation) et 4 (robustesse). L'ordre de ma conception tient.

- **Si les scores ne diffèrent pas** → les sondes sont des classifieurs de texte en activations. Le gain blanc-sur-noir (H1) se réduit à un avantage de représentation (lire le texte dans l'espace latent plutôt qu'en tokens), pas à un accès privilégié à l'état intentionnel. Toute la carte de validité de construit, H8, et la frontière de robustesse portent sur un classifieur de contenu. Le programme doit alors pivoter : soit vers des sondes sur des couches plus précoces (avant que la sortie ne domine le résidu), soit vers des architectures qui dissocient explicitement le flux causal (sondes sur l'attention plutôt que sur le résidu), soit vers l'abandon de la revendication « intention ».

Ce test est le seul qui, en quelques heures et sans aucune dépense GPU, peut falsifier la prémisse centrale du programme. Il doit être fait avant toute autre mesure.

FIN-DE-CELLULE