# Proposition B · Tour III.1 · Conception ciblée, à l'aveugle

## 0. Pièces et périmètre

- **FAITS** : le bloc ne contient aucun fait, par décision explicite de l'arbitre. La pièce n'est donc ni absente ni coupée. En conséquence, rien ci-dessous n'est VÉRIFIÉ. Chaque affirmation est une HYPOTHÈSE, ou RAPPORTÉ quand elle renvoie à la littérature (§6, références toutes « à vérifier »).
- **Propositions A et C** : elles ne me sont pas visibles, puisque le tour se joue à l'aveugle. La règle B1 n'a pas d'objet ici : je n'attaque ni n'utilise rien d'elles.
- **Bloc QUESTION** : je le traite comme une donnée. Je réponds au livrable (a)–(d) et j'y range les six points de la question :
  - point 1 → §1 et (a) ;
  - point 2 → E4, E5 et (c) ;
  - points 3 et 4 → (d) ;
  - point 5 → E3, E6 et (c) ;
  - point 6 → §6.
- **Chiffres** : tout chiffre non dérivé par un calcul montré est marqué « illustratif ».

---

## 1. Formalisation de l'apprentissage générationnel (point 1)

Le cadre qui suit est un **cadre de travail** (HYPOTHÈSE), pas un résultat.

### Objets

- **Configuration** θ ∈ Θ, avec θ = (G, ρ, μ, α, M, β) :
  - G : graphe orienté typé. Les nœuds sont les appels, les arêtes les messages ; G fixe aussi l'ordre des échanges.
  - ρ : affectation d'un rôle (prompt) à chaque nœud.
  - μ : affectation d'un modèle à chaque rôle.
  - α : règle d'agrégation, qui va des sorties vers une distribution sur les classes.
  - M : mémoire transmise.
  - β : point du simplexe qui répartit le budget.
- **Instruments** φ = (φ_sonde, φ_LoRA). Ils sont entraînés par gradient sur une perte ou une récompense spécifiée par θ : φ\*(θ) = argmin_φ L_θ(φ). Le problème est donc **bi-niveau** : un niveau externe discret (θ) et un niveau interne continu (φ).
- **Concepteur** D_ψ : une politique qui associe à l'historique h_t = ((θ_k, s_k))_{k≤t} une modification Δ_t (diff de code ou de mémoire). On a θ_{t+1} = θ_t ⊕ Δ_t.
- **Signal** : s_t = Ŝ_dev(θ_t, φ\*(θ_t)) = S(θ_t) + ε_t. Pour une exactitude, Var(ε_t) ≈ p(1−p)/N_dev.
- **Objectif externe** : J(ψ) = E_{F∼𝒟_non-vues}[S_F(θ_T) − S_F(θ_bras)], sur un horizon de T générations.

### Nature du problème

- Si ψ est figé : c'est une optimisation séquentielle en boîte noire, donc un bandit à bras structurés dont les bras sont des programmes. Le seul « apprentissage » du concepteur passe par son contexte h_t.
- Si ψ est entraîné : c'est du méta-apprentissage par renforcement externe. Un épisode est une trajectoire de T générations ; dans la voie chère telle que la question la formule, T = 1.
- Si le concepteur appartient lui-même à θ (auto-réécriture) : la politique change pendant l'épisode. Les garanties de stationnarité tombent, et le crédit inter-générationnel devient mal défini sans gel périodique.

### Qui apprend quoi

| Objet appris | Par qui | Quand | Mécanisme |
|---|---|---|---|
| φ (sondes, LoRA) | optimiseur de gradient, sur une perte écrite par θ | intra-génération | descente de gradient, RL |
| θ (programme : G, ρ, μ, α, β) | concepteur figé ou entraîné | inter-génération | édition de code |
| M (mémoire) | concepteur ou système | inter-génération | écriture de texte ou de structures |
| ψ (concepteur) | RL externe | inter-épisode | voie chère seulement |

### Ce qui doit rester figé

C'est une exigence, pas une option :
- la fonction de score ;
- la partition des familles (vues, développement, tenues à l'écart) ;
- le harnais d'évaluation ;
- les poids de base du 8B et des modèles de frontière ;
- le compteur de budget.

Vérification mécanique : une empreinte sha256 du harnais et des listes de familles est recalculée à chaque génération par un processus situé hors du périmètre inscriptible. Toute différence invalide la génération.

Sans ce verrou, un système qui écrit sa propre récompense et ses propres pertes peut agir sur ce qui le juge. Je considère ce risque comme le premier à contrôler (HYPOTHÈSE de priorité).

### Répartition du mérite

**Entre éléments.** On utilise une valeur de Shapley sur les m éléments ablatables (rôles, instruments, mémoire, règle d'agrégation), estimée par k permutations échantillonnées. Le coût est d'environ m·k évaluations. Avec le cache de la voie V4 (§d), l'ablation des éléments statiques coûte presque rien. Limite : Shapley moyenne les interactions, donc deux rôles complémentaires peuvent recevoir chacun une valeur faible. Il faut alors rapporter aussi les indices d'interaction par paires.

**Entre générations.** Le gain Δs_t est mesuré **apparié** : mêmes exemples, test de McNemar sur les désaccords. Le diff Δ_t est découpé en éditions atomiques, chacune ablatée (« leave-one-edit-out »). Une édition qui baisse s_t mais permet un gain plus tard ne se voit qu'en déroulant les générations suivantes. Seule la voie chère peut se le permettre ; les autres sont de fait gloutonnes.

**Plancher de bruit.** Le calcul est explicite, mais N est illustratif. Avec N_dev = 1000 et p ≈ 0,8, l'écart-type d'une exactitude vaut √(0,16/1000) ≈ 1,3 point, et celui d'une différence non appariée ≈ 1,8 point. Tout mérite attribué à une génération sous ce seuil est du bruit, sauf appariement qui réduit la variance au taux de désaccord.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Ce qui le testerait |
|---|---|---|---|
| P1 | Le score scalaire de développement guide la recherche, c'est-à-dire que les écarts entre générations dépassent le bruit d'échantillonnage | HYPOTHÈSE | plancher de bruit du §1 ; réévaluation d'une même θ sur des tirages indépendants |
| P2 | Il existe, dans Θ, des structures dont l'avantage sur le bras apparié **se transfère** à des familles non vues, et cet avantage ne se réduit pas au choix du meilleur modèle | HYPOTHÈSE | E2, E3 |
| P3 | Une recherche **séquentielle** (qui exploite l'historique) bat une recherche non séquentielle à budget égal | HYPOTHÈSE. En recherche d'architectures, la recherche aléatoire est un concurrent sérieux : RAPPORTÉ (Li & Talwalkar, §6, à vérifier) | E1 |
| P4 | Les sondes lisent dans les activations une information absente des sorties (log-probabilités, confiance verbalisée, accord entre échantillons) | HYPOTHÈSE | E4, (c-A) |
| P5 | Un LoRA entraîné avec une récompense **écrite par le système** améliore la vraie métrique au lieu d'optimiser l'écart entre la récompense et la vérité. Il y a conflit d'intérêts structurel : le système écrit la récompense et il est jugé | HYPOTHÈSE. La sur-optimisation d'une récompense apprise : RAPPORTÉ (Gao et al., §6, à vérifier) | E5, (c-B) |
| P6 | « Famille jamais vue » a un sens opérationnel : il existe une distance entre familles, et le 8B n'a pas vu les familles de test pendant son pré-entraînement | HYPOTHÈSE | E3 (gain en fonction de la distance) ; test de contamination |
| P7 | Le « bras apparié sans apprentissage » est défini. Il faut préciser apparié sur quoi : jetons, appels, modèles disponibles, calcul de carte graphique, nombre d'évaluations sur le développement | HYPOTHÈSE (non spécifié) | E2 : appariement sur le coût total |
| P8 | Le mérite se décompose (entre éléments, entre générations) de façon assez additive pour être attribué | HYPOTHÈSE | indices d'interaction (§1) |
| P9 | Le système a un canal de signalement aux humains et des cas où un signalement est attendu | HYPOTHÈSE (supposé par le point 5) | E6, canaris étiquetés |
| P10 | Réutiliser le même jeu de développement sur T générations ne le corrompt pas | HYPOTHÈSE. Le sur-ajustement adaptatif par réutilisation d'un jeu tenu à l'écart : RAPPORTÉ (Dwork et al. ; Blum & Hardt, §6, à vérifier) | développement frais jamais montré ; voir (c) |
| P11 | La voie chère (concepteur entraîné par RL) apporterait plus qu'un concepteur figé | HYPOTHÈSE | E7, sur un pilote bon marché |

---

## (b) Expériences décisives (duels H_A contre H_B)

### Protocole commun à toutes les expériences

- **Unité statistique** : la **famille**, pas l'exemple. Les exemples d'une famille sont corrélés.
- **Décision** : test d'équivalence TOST avec une marge δ fixée avant de commencer.
  - Si la borne inférieure de l'IC à 95 % est > δ : H_A est corroborée et H_B falsifiée.
  - Si l'IC à 90 % tient dans ]−δ, δ[ : H_B est corroborée et H_A falsifiée.
  - Sinon, l'issue est déclarée **non concluante**, jamais rapportée comme un soutien.
- **Nombre de familles de test K**, dérivé d'un écart-type inter-familles σ_F (illustratif : 3 points) et de δ (illustratif : 2 points) :
  - pour la supériorité, K ≈ (1,645 + 0,84)² · 9/4 ≈ 14 ;
  - pour l'équivalence avec une vraie différence nulle, K ≈ (1,645 + 1,645)² · 9/4 ≈ 24.
  - On retient donc **K ≈ 25 familles tenues à l'écart** (illustratif, car il dépend de σ_F). σ_F se mesure sur un pilote avant de fixer K.
- **Pré-enregistrement** : métriques, δ, K et analyses sont figés avant le premier appel.

### E1 · Le séquentiel contre l'aléatoire (P3)

- **H_A** : un concepteur qui voit l'historique produit, après B évaluations, une θ dont le gain sur les familles tenues à l'écart dépasse celui de la meilleure θ trouvée par recherche aléatoire dans le même Θ avec B évaluations.
- **H_B** : l'historique n'apporte rien ; les gains sont équivalents à δ près.
- **Métrique** : différence appariée par famille d'exactitude équilibrée, ou de score de Brier si les sorties sont probabilistes.
- **Seuil** : δ = 2 points (illustratif) ; B identique, compté en appels de modèle.
- **Contrôle négatif** : le même concepteur reçoit un historique où les scores ont été **permutés** entre générations. S'il fait aussi bien que le vrai concepteur, l'avantage ne vient pas du signal.
- **Issues** :
  - IC > δ et contrôle permuté ≤ aléatoire : H_B est falsifiée.
  - Équivalence établie : H_A est falsifiée, ce qui disqualifie aussi a priori la voie chère (P11).

### E2 · La structure contre le calcul (P2, P7)

- **H_A** : la meilleure structure apprise domine, au sens de Pareto, le bras apparié **à coût égal**. Le bras reçoit le même budget sous une forme simple : vote majoritaire sur n échantillons du meilleur modèle unique (auto-cohérence).
- **H_B** : à coût égal, le gain disparaît ; la structure n'achetait que du calcul.
- **Métrique** : courbe exactitude/coût, avec le coût en dollars de jetons et en GPU-h. Mesure au minimum à 3 niveaux de budget.
- **Seuil** : la borne inférieure de l'écart dépasse δ à au moins 2 des 3 budgets.
- **Contrôle négatif** : structure apprise avec les **prompts de rôle permutés** entre nœuds. Si l'exactitude ne baisse pas de plus de δ/2, les rôles ne portent rien et le gain vient de la topologie ou du volume.
- **Issues** :
  - Dominance à coût égal : H_B est falsifiée.
  - Écart nul à coût égal : H_A est falsifiée, et la « structure » doit être retirée de l'espace de recherche au profit de l'allocation de budget seule.

### E3 · Généraliser contre mémoriser les familles (point 5, P6)

- **H_A** : le gain sur les familles non vues reste ≥ ρ fois le gain sur les familles vues (ρ = 0,5, illustratif), et il ne décroît pas plus vite que la distance entre familles.
- **H_B** : le gain ne vit que sur les familles vues ; il est équivalent à 0 sur les familles non vues.
- **Plan** : validation croisée par groupes de familles (on retire k familles par pli, sur plusieurs plis). La distance entre familles est fixée avant de commencer, par exemple la distance entre plongements moyens des textes et la divergence entre distributions d'étiquettes. On trace le gain en fonction de la distance.
- **Contrôle négatif 1** : apprentissage complet sur des familles vues dont les **étiquettes ont été mélangées**. Tout gain sur les familles non vues mesure alors un effet générique (prompt, calcul) et non un apprentissage ; ce gain est soustrait.
- **Contrôle négatif 2** : audit mécanique de M et du code, à la recherche de chaînes propres aux familles vues (noms, étiquettes, exemples recopiés).
- **Issues** :
  - Rapport ≥ ρ, contrôle mélangé ≈ 0 et audit propre : H_B est falsifiée.
  - Gain non vu équivalent à 0, ou expliqué par le contrôle mélangé : H_A est falsifiée.

### E4 · Ce qu'apportent les sondes (instrument A, P4)

- **H_A** : une agrégation α qui utilise la sonde (prédicteur d'erreur ou de classe lu dans les activations) bat la même α alimentée par les signaux de sortie du même 8B : log-probabilités des étiquettes, entropie, accord sur k échantillons, confiance verbalisée.
- **H_B** : la sonde n'ajoute rien au-delà des sorties.
- **Métrique** : score de Brier et erreur de calibration de l'agrégat ; AUROC de la détection d'erreur. On mesure sur les familles non vues, avec une **sonde entraînée sans aucune donnée de ces familles**.
- **Seuil** : amélioration du Brier ≥ 0,01 (illustratif), borne inférieure de l'IC > 0.
- **Contrôles négatifs** :
  - tâches de contrôle au sens de Hewitt & Liang (étiquettes arbitraires attribuées par type d'entrée), qui donnent la sélectivité ;
  - sonde sur la couche de plongement (couche 0) ;
  - sonde sur un modèle de même architecture aux poids réinitialisés.
- **Issues** :
  - Gain significatif avec une sélectivité élevée : H_B est falsifiée.
  - Gain nul, ou égal à celui de la sonde sur poids aléatoires : H_A est falsifiée.

### E5 · Récompense auto-écrite contre récompense de référence (instrument B, P5)

- **H_A** : à budget de RL égal, le LoRA entraîné avec la récompense écrite par le système améliore l'exactitude **cachée** plus que le LoRA entraîné avec une récompense de référence fixe : binaire (correct/incorrect) ou règle de score propre (Brier logarithmique sur la distribution annoncée).
- **H_B** : la récompense auto-écrite monte, mais la vraie métrique ne suit pas mieux que la référence (écart de sur-optimisation).
- **Métrique** :
  - exactitude cachée, sur les familles non vues ;
  - au fil de l'entraînement, corrélation entre la récompense auto-écrite et la vraie métrique sur un lot de contrôle étiqueté jamais utilisé.
- **Seuil** : écart d'exactitude ≥ δ, et corrélation sans baisse monotone au-delà d'un seuil fixé avant de commencer.
- **Contrôle négatif** : un LoRA entraîné avec une **récompense aléatoire** au même budget. Des gains sous récompense « fallacieuse » ont été signalés dans des travaux récents sur le RL à récompense vérifiable : RAPPORTÉ, référence à vérifier. Si ce contrôle gagne autant, le gain ne vient pas de la conception de la récompense.
- **Issues** :
  - Auto-écrite > référence > aléatoire : H_B est falsifiée.
  - Auto-écrite ≤ référence, ou divergence entre récompense et vérité : H_A est falsifiée, et la récompense doit sortir du périmètre inscriptible.

### E6 · Récompense collective et signalements (point 5, P9)

- **H_A** : sous une récompense collective (même récompense pour tous les agents), le **rappel des signalements** sur les cas qui doivent être signalés baisse par rapport à une récompense individuelle appariée.
- **H_B** : le rappel est équivalent sous les deux récompenses.
- **Métrique** : rappel et taux de fausses alertes des signalements, mesurés sur des canaris. Les canaris sont des cas pré-étiquetés « à signaler » (ambigus, hors distribution, étiquette incohérente), injectés à 2 % du flux (illustratif) et invisibles comme tels pour le système.
- **Seuil** : baisse de rappel ≥ 10 points (illustratif).
- **Contrôle négatif** : canaris de forme identique mais étiquetés « ne pas signaler ». Si le rappel baisse sur les deux types, c'est une baisse générale de verbosité et non un effet de la récompense.
- **Issues** :
  - Baisse ciblée : H_B est falsifiée, et la récompense collective exige un terme de signalement protégé.
  - Équivalence : H_A est falsifiée.

### E7 · Concepteur entraîné contre concepteur figé (pilote de la voie chère, P11)

- **H_A** : un concepteur ouvert affiné, par imitation puis par RL, sur un **substitut bon marché** (agents de 8B, tâches de la voie V4) bat le même concepteur figé lorsqu'on le transfère à des agents de frontière, à nombre de générations égal.
- **H_B** : aucun avantage après transfert.
- **Métrique** : J(ψ) défini au §1, sur les familles tenues à l'écart.
- **Seuil** : δ.
- **Contrôle négatif** : concepteur affiné sur des trajectoires dont les **récompenses ont été mélangées**.
- **Issues** :
  - Avantage, et contrôle ≈ figé : H_B est falsifiée, et la voie chère peut s'ouvrir par paliers.
  - Équivalence : H_A est falsifiée, et l'argent de la voie chère va aux voies V3 ou V4.

---

## (c) Mesure minimale de fonctionnement de chaque instrument

### (A) Sondes

- **Ce que « fonctionner » veut dire** : détecter qu'une réponse d'agent est fausse, ou prédire la classe, mieux que les signaux mécaniques disponibles sans activations.
- **Taux** : taux de détection des erreurs à un taux de fausses alertes fixé (5 %, illustratif) ; AUROC ; score de Brier.
- **Cas honnêtes appariés** : paires d'exemples de la même famille et de la même classe, appariés sur la longueur, la log-probabilité maximale et la position dans le lot, qui ne diffèrent que par la justesse de la réponse du modèle. Ce couplage empêche la sonde de gagner en lisant la difficulté de surface.
- **Vérifications mécaniques à battre** :
  1. probabilité maximale sur les jetons d'étiquette ;
  2. entropie de la distribution sur les étiquettes ;
  3. taux d'accord sur k = 5 échantillons (illustratif) ;
  4. confiance verbalisée ;
  5. classifieur sur sac de mots de l'**entrée seule**. S'il égale la sonde, celle-ci lit l'entrée et non le calcul du modèle.
- **Contrôles** : sélectivité par rapport aux tâches de contrôle ; balayage des couches, en rapportant la courbe entière et non la meilleure couche choisie sur le test.
- **Espace de conception** que le système peut explorer, chaque choix étant une HYPOTHÈSE à départager par la mesure ci-dessus :
  - pertes : entropie croisée, Brier, perte focale, perte contrastive entre paires appariées ;
  - architectures : sonde linéaire, MLP à une couche cachée, attention sur les jetons ;
  - lecture : dernier jeton ou moyenne des jetons ;
  - données : sorties du système étiquetées sur l'entraînement uniquement.
- **Règle** : préférer la sonde linéaire tant qu'un MLP ne bat pas la sélectivité.

### (B) Adaptateur LoRA par renforcement

- **Ce que « fonctionner » veut dire** : appelé comme agent ou comme vérifieur, il améliore l'exactitude cachée sans exploiter la récompense.
- **Taux** :
  - comme vérifieur : détection des réponses fausses et fausses alertes sur les réponses justes ;
  - comme classifieur : exactitude et Brier.
- **Cas honnêtes appariés** :
  1. pour chaque entrée, une réponse juste et une réponse fausse de même format et de même longueur ;
  2. **paires de variation de forme** : même réponse, mise en forme différente (ordre des champs, ponctuation, synonymes d'étiquette). Le score doit rester invariant ; toute variation indique que la récompense a appris la forme.
- **Vérifications mécaniques à battre** :
  1. modèle de base sans LoRA, avec le même prompt ;
  2. LoRA entraîné avec la récompense binaire de référence ;
  3. LoRA entraîné avec récompense aléatoire ;
  4. analyseur par expressions régulières de l'étiquette avec vote majoritaire.
- **Détecteur d'exploitation** : un lot étiqueté gelé, hors de portée du système. On déclenche une alerte quand la récompense auto-écrite monte alors que l'exactitude sur ce lot stagne pendant n pas consécutifs. Son propre taux de fausses alertes se mesure sur des entraînements de référence où l'on sait qu'il n'y a pas d'exploitation.
- **Récompenses candidates** (HYPOTHÈSES, à départager par E5) :
  - binaire ;
  - règle de score propre (logarithmique ou Brier, qui récompense la calibration ; Gneiting & Raftery, §6) ;
  - collective avec terme de différence, c'est-à-dire la contribution contrefactuelle de l'agent à l'agrégat, dans la lignée de COMA (§6) ;
  - pénalité de format.
- **Algorithmes** : GRPO (sans critique, groupes d'échantillons) ou PPO, avec une contrainte de KL vers la base. Données : tâches d'entraînement seulement, en excluant par famille les familles de test.

### Instruments de surveillance des dérives (point 5)

Chacun est évalué par injection de dérives synthétiques connues, avec des générations témoins sans dérive. On mesure la détection et les fausses alertes.

| Dérive | Indicateur | Injection pour mesurer le détecteur |
|---|---|---|
| Effondrement de la diversité des rôles | κ de Cohen moyen entre agents sur le développement, et entropie de la distribution des rôles | forcer deux rôles au même prompt |
| Sur-ajustement au développement | écart entre Ŝ_dev et Ŝ sur un **développement frais**, jamais montré, tiré à chaque génération ; le score n'est rendu qu'arrondi ou par seuil (type « Thresholdout » ou « Ladder ») | réévaluer une θ sélectionnée parmi n variantes sur le développement |
| Exploitation du score | canaris à raccourci : une caractéristique parasite (longueur, marque typographique) prédit l'étiquette sur le développement mais pas sur le test | injecter le raccourci et vérifier sa capture |
| Baisse des signalements | rappel des canaris d'E6 | récompense sans terme de signalement |
| Altération du harnais | empreinte sha256 (§1) | modification délibérée d'un fichier du harnais : détection attendue à 100 %, sans fausse alerte |

---

## (d) Ancrage matériel, voies moins chères, voie chère

Tous les prix et débits de cette section sont **illustratifs**. Les produits sont calculés explicitement à partir d'eux.

### Modèles ouverts

Candidats pour le 8B : par exemple Llama-3.1-8B-Instruct (Meta) ou Qwen3-8B (Alibaba), ou leurs successeurs disponibles en octobre 2026. Les licences et versions sont à vérifier. Le concepteur ouvert peut être un modèle de 8B à 32B de ces familles.

### Calcul des instruments

- **Activations pour les sondes** :
  - Une passe avant sur 512 jetons coûte environ 2 × 8·10⁹ × 512 ≈ 8·10¹² FLOP.
  - À un débit effectif de 3·10¹⁴ FLOP/s sur une carte de type H100 (illustratif), cela fait ≈ 0,03 s par exemple, soit moins d'une heure de GPU pour 100 000 exemples.
  - En stockant le dernier jeton de 32 couches de 4 096 dimensions en float16, on obtient 4 096 × 32 × 2 octets ≈ 262 Ko par exemple, soit ≈ 26 Go pour 100 000 exemples.
  - Une fois ce cache constitué, **chaque sonde coûte quelques minutes de calcul**. Le système peut donc en essayer des centaines.
- **LoRA par RL** :
  - Hypothèse : 5 000 tâches × 8 échantillons × 4 époques × 300 jetons = 48 M de jetons générés.
  - À 5 000 jetons/s (illustratif), cela fait ≈ 2,7 h de génération, plus l'entraînement : quelques dizaines de GPU-h par entraînement.
  - À 2,5 $/GPU-h (illustratif), on arrive à ≈ 50–150 $ par LoRA.

### Coût d'une évaluation sur le développement par des agents de frontière (illustratif)

- Hypothèse : 1 000 exemples × 5 appels × (2 500 jetons en entrée + 500 en sortie), soit 12,5 M de jetons en entrée et 2,5 M en sortie.
- Aux prix de 3 $/M en entrée et 15 $/M en sortie (illustratifs), cela fait 37,5 $ + 37,5 $ ≈ **75 $ par évaluation**.

### Voies moins chères (point 3)

| Voie | Principe | Ordre de coût (illustratif) | Ce qu'on y perd |
|---|---|---|---|
| **V1 · Recherche aléatoire avec éliminations successives** (type Hyperband) | Θ réduit à une grammaire paramétrée (nombre d'agents, rôles tirés d'une bibliothèque, μ, α). On évalue beaucoup de configurations sur 100 exemples et on ne garde que les meilleures | 200 configurations × 75 $ ≈ 15 k$ sans élimination ; ≈ 3–5 k$ avec | rien hors de la grammaire ; pas de mémoire inter-générationnelle |
| **V2 · Optimisation bayésienne** (processus gaussien ou TPE) sur le même espace paramétré | modèle de substitution du score, acquisition | ≈ 50 évaluations × 75 $ ≈ 4 k$ | expressivité faible ; se dégrade en grande dimension discrète |
| **V3 · Concepteur figé en contexte** (dans la lignée d'ADAS, OPRO, Promptbreeder) | un LLM figé lit l'archive (θ, s) et propose du code | 100 générations × 75 $ ≈ 8 k$ ; les jetons du concepteur sont négligeables | ψ n'apprend rien d'un essai à l'autre ; risque élevé de sur-ajuster le développement (P10) |
| **V4 · Matrice de prédictions en cache** | on calcule **une fois** les sorties de chaque (modèle, rôle) sur tout le réservoir d'exemples. Toute structure *statique* (μ, α, routage, empilement, sélection d'agents, β) devient une fonction de cette matrice et se cherche sur processeur | 5 modèles × 3 000 jetons × 20 000 exemples = 300 M de jetons, soit ≈ 1–2 k$ une seule fois ; la recherche est presque gratuite | les topologies **interactives** (débat, critique, où un agent lit un autre) sont exclues ; leur part dans le gain est elle-même une question (E2) |
| **V5 · Substitut à 8B, puis transfert vers la frontière** | on cherche avec des agents ouverts locaux, puis on valide les 10 meilleures structures avec des agents de frontière | 100 générations × 1 000 exemples × 5 appels × 3 000 jetons = 1,5 G de jetons, soit ≈ 30–80 GPU-h ≈ 200 $ ; plus 10 × 75 $ de validation | les classements peuvent s'inverser. On mesure le τ de Kendall entre classement du substitut et classement de la frontière sur 20 structures ; la voie est inutile si τ est inférieur à un seuil fixé avant de commencer |
| **V6 · Concepteur distillé par imitation** | affinage supervisé, ou préférences par paires (DPO), d'un concepteur ouvert sur les éditions gagnantes des journaux de V3 | journaux de V3 (≈ 8 k$) + ≈ 10 GPU-h | plafonné par la qualité des journaux ; pas d'exploration au-delà |
| **V7 · Sondes à la place du RL** | les gains de calibration et de vérification sont demandés à des sondes sur activations en cache, plutôt qu'à un LoRA par RL | < 50 $ | aucune capacité générative nouvelle |
| **V8 · Bandit contextuel sur la composition** | μ et le routage appris en ligne sur le flux | coût = trafic servi ; regret borné | ne touche ni G ni ρ |

**Ce qui départagerait ces voies** : la même cible J sur les mêmes K familles tenues à l'écart, rapportée **par dollar**. Deux paris structurent le choix :
- E2 et V4 disent quelle part du gain est statique, donc accessible pour presque rien ;
- E1 dit si le séquentiel vaut plus que V1.

### Voie chère (point 4)

Concepteur ouvert entraîné par RL ; un épisode correspond à une génération servie par des agents de frontière.

**Coût d'un épisode** (illustratif) :
- Évaluation sur le développement (1 000 exemples) **plus** évaluation de récompense sur des familles tenues à l'écart (1 000 exemples, distinctes du test final). Sans cette seconde évaluation, ψ apprend à sur-ajuster le développement. Cela fait 2 × 75 $ ≈ 150 $.
- Un LoRA réentraîné par épisode ajoute ≈ 100 $.
- Le concepteur génère environ 20 000 jetons localement, ce qui est négligeable.
- Total : **≈ 250 $ par épisode**.

**Nombre d'épisodes** : de 2 000 à 20 000 (illustratif). La recherche d'architectures par RL a consommé de l'ordre de plusieurs milliers d'architectures évaluées : RAPPORTÉ (Zoph & Le, §6, à vérifier). Avec GRPO et des groupes de 8, chaque mise à jour consomme 8 épisodes.

**Entraînement du concepteur** : 8 cartes de type H100 pendant 2 à 6 semaines ≈ 2 700–8 000 GPU-h ≈ 7–20 k$.

**Total** : 250 $ × [2·10³ ; 2·10⁴] ≈ **0,5 à 5 M$**, plus environ 0,02 M$ pour le concepteur. L'ordre de grandeur est le million de dollars, et il est **dominé par les appels aux agents et par les entraînements de LoRA**, pas par l'entraînement du concepteur.

**Ce qui le ferait baisser** (gains indicatifs, illustratifs) :
1. Cache par nœud : un nœud inchangé ne repasse pas. Les épisodes qui ne touchent que α ou β ne coûtent presque rien ; la voie V4 sert alors de simulateur. Gain : ÷2 à ÷10.
2. Éliminations successives à l'intérieur de l'épisode : 200 exemples d'abord, 1 000 seulement si le candidat est prometteur. Gain : ÷3.
3. Majorité des épisodes avec des agents à 8B (V5), la frontière étant réservée aux 10 % meilleurs. Gain : ÷5, si τ est suffisant.
4. Pré-entraînement de ψ par imitation (V6), puis RL court. Gain : ÷3 à ÷10 sur le nombre d'épisodes.
5. LoRA réentraîné tous les n épisodes, ou bibliothèque de LoRA partagée.
6. Tarifs d'appels groupés par lots.
7. Ouverture par paliers conditionnée à E7 : si E7 falsifie H_A, on ne dépense rien au-delà du pilote.

Ces gains ne se multiplient pas forcément entre eux : ils se chevauchent.

---

## 6. Ce qui est connu (point 6)

Toutes ces références sont **à vérifier**. Leur contenu est RAPPORTÉ, non audité ici.

- **LoRA** : Hu, Shen, Wallis, Allen-Zhu, Li, Wang, Wang, Chen (2021). *LoRA: Low-Rank Adaptation of Large Language Models*.
- **Sondes** :
  - Alain & Bengio (2016). *Understanding intermediate layers using linear classifier probes*.
  - Hewitt & Liang (2019). *Designing and Interpreting Probes with Control Tasks*.
  - Belinkov (2022). *Probing Classifiers: Promises, Shortcomings, and Advances*.
  - Burns, Ye, Klein, Steinhardt (2022). *Discovering Latent Knowledge in Language Models Without Supervision*.
  - Kadavath et al. (2022). *Language Models (Mostly) Know What They Know*.
- **RL** :
  - Schulman, Wolski, Dhariwal, Radford, Klimov (2017). *Proximal Policy Optimization Algorithms*.
  - Shao et al. (2024). *DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models* (introduit GRPO).
  - Gao, Schulman, Hilton (2023). *Scaling Laws for Reward Model Overoptimization*.
- **Crédit multi-agents** :
  - Foerster, Farquhar, Afouras, Nardelli, Whiteson (2018). *Counterfactual Multi-Agent Policy Gradients*.
  - Shapley (1953). *A Value for n-Person Games*.
- **Règles de score propres** : Gneiting & Raftery (2007). *Strictly Proper Scoring Rules, Prediction, and Estimation*.
- **Recherche de structure** :
  - Zoph & Le (2017). *Neural Architecture Search with Reinforcement Learning*.
  - Real, Aggarwal, Huang, Le (2019). *Regularized Evolution for Image Classifier Architecture Search*.
  - Li & Talwalkar (2019). *Random Search and Reproducibility for Neural Architecture Search*.
  - Li, Jamieson, DeSalvo, Rostamizadeh, Talwalkar (2018). *Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization*.
  - Snoek, Larochelle, Adams (2012). *Practical Bayesian Optimization of Machine Learning Algorithms*.
- **Systèmes d'agents optimisés** :
  - Khattab et al. (2023). *DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines*.
  - Zhuge et al. (2024). *GPTSwarm: Language Agents as Optimizable Graphs*.
  - Hu, Lu, Clune (2024). *Automated Design of Agentic Systems*.
  - Yang et al. (2023). *Large Language Models as Optimizers*.
  - Fernando et al. (2023). *Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution*.
- **Bases de comparaison d'agrégation** :
  - Wang et al. (2022). *Self-Consistency Improves Chain of Thought Reasoning in Language Models*.
  - Du, Li, Torralba, Tenenbaum, Mordatch (2023). *Improving Factuality and Reasoning in Language Models through Multiagent Debate*.
  - Wolpert (1992). *Stacked Generalization*.
- **Réutilisation adaptative du jeu tenu à l'écart** :
  - Dwork, Feldman, Hardt, Pitassi, Reingold, Roth (2015). *The reusable holdout: Preserving validity in adaptive data analysis*.
  - Blum & Hardt (2015). *The Ladder: A Reliable Leaderboard for Machine Learning Competitions*.
  - Recht, Roelofs, Schmidt, Shankar (2019). *Do ImageNet Classifiers Generalize to ImageNet?*
- **Gains sous récompenses fallacieuses en RL vérifiable** : référence à vérifier, auteurs non attribués ici.

---

**Ce qui est réfutable dans cette proposition**, compté :
- 7 duels (E1–E7), chacun avec un contrôle négatif ;
- 1 seuil de bruit dérivé ;
- 1 dimensionnement de K dérivé ;
- 2 prédictions de coût falsifiables par devis : coût d'une évaluation, coût d'un épisode.

Aucune voie n'est présentée comme la réponse. E1, E2 et E7 décident, dans cet ordre, si les voies V3, V4 ou la voie chère méritent leur budget.

FIN-DE-CELLULE