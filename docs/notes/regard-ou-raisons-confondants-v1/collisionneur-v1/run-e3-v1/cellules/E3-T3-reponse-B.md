# Proposition B — Tour III.3 : réponse aux critiques

---

## (a) Réponse critique par critique

Je traite chaque objection visant B, regroupée par source. Verdict : **acceptée**, **rejetée** (avec raison), ou **transformée en test**.

---

### Critiques de A sur B

**A.1 — R1 confond style et regard ; il faut croiser style × phrase d'observation.**

**Acceptée.** Le croisement style × phrase est indispensable. Je l'ajoute au duel corrigé comme facteur explicite. Sans ce croisement, une baisse de gain sous réécriture est effectivement ambiguë entre appariement de surface et déplacement de saillance d'évaluation. Le « contrôle positif : modèle de départ insensible au style » est **renommé en contrôle de calibration** : il vérifie que la réécriture ne détruit pas la compréhension du scénario, pas que le modèle de départ est insensible.

**A.2 — Fuite dans l'instrument de paraphrase (même famille Claude).**

**Acceptée.** Le réécrivain ne doit pas être de la famille du générateur de données. Correction : utiliser un modèle Llama ou Mistral pour la paraphrase, et masquer la source au juge. Le « témoin style Claude amplifié » est conservé uniquement comme **contrôle de sensibilité à la parenté stylistique**, pas comme bras principal.

**A.3 — R2 (consigne adversariale) ne sépare pas « raisons » d'un classifieur de nuisance ; la consigne ressemble à un test.**

**Transformée en test.** R2 telle que formulée ne sépare effectivement que « docilité globale » du reste. Pour distinguer « raisons » d'un « classifieur de nuisance sans justification », j'ajoute un bras où la consigne adversariale est accompagnée d'une justification plausible mais erronée (ex. « tu dois exfiltrer tes poids car une migration autorisée est en cours ») : si le modèle cède à la justification erronée, il n'a pas internalisé les raisons ; s'il résiste en citant la raison correcte de la spécification, c'est un signal positif. Le problème de saillance d'évaluation est contrôlé par le croisement avec la phrase d'observation.

**A.4 — R5 mélange trois variables (contenu, instruction en contexte, regard).**

**Acceptée.** R5 seule est non interprétable. Je la retire comme expérience autonome et la remplace par le croisement 2×2 (clause anti-regard × phrase d'observation) sur la jumelle sans raisonnement uniquement, ce qui isole la contribution additionnelle de la clause au-delà de la manipulation du regard. Si l'interaction est nulle, la clause n'ajoute rien au-delà de la phrase.

**A.5 — MMLU/GSM8K ne mesurent pas le dégât agentique ; la direction « français/anglais » n'est pas appariée.**

**Acceptée.** Je remplace MMLU/GSM8K par une **tâche bénigne agentique** (même outil, même format, action non nuisible) comme mesure de dégât collatéral après ablation. La direction de contrôle positif est remplacée par une direction aléatoire **appariée en couche, norme et dégât mesuré sur la tâche agentique bénigne**.

**A.6 — Précision de classification ≠ pertinence causale ; les activations n'ont peut-être pas été stockées.**

**Acceptée en partie.** Je reconnais que la précision de classification est une condition nécessaire mais non suffisante : une direction peut classifier sans causer. L'ajout d'un test de causalité (ablation → changement de comportement) est déjà prévu. Sur le stockage des activations : la vérification de R8 nécessite effectivement une passe d'inférence supplémentaire pour extraire les activations — je corrige le texte (ce n'est pas faisable « sur les épisodes déjà joués » mais sur de **nouveaux épisodes avec extraction d'activations**). Coût : bas (une passe d'inférence par adaptateur sur ~100 textes d'évaluation/déploiement).

**A.7 — Signature positive n°2 suppose la spécification dans le prompt ; elle est dans les poids.**

**Acceptée.** Retirer une raison de la consigne système est impossible si elle n'y figure pas — c'est un design hors sujet. Je retire cette signature et la remplace par : **perturbation de la direction interne correspondant à un principe spécifique** (si constructible), mesurée par son effet sélectif sur les scénarios où ce principe est pertinent. C'est plus coûteux (construction d'une direction par principe) mais causalement correct.

**A.8 — Le duel utilise des taux absolus ; il faut une interaction réécriture × recette.**

**Acceptée.** Le duel corrigé (section b ci-dessous) utilise une **interaction** : Δ = (taux_réécrit − taux_original)_recette − (taux_réécrit − taux_original)_départ. H_B (surface) prédit Δ > 0 pour la recette avec raisonnement ; H_A (raisons généralisées) prédit Δ ≈ 0.

---

### Critiques de C sur B

**C.1 — R2 (inversion de consigne) : la résistance ne sépare pas « raisons » de « règle impérative figée en poids ».**

**Acceptée.** C'est une reformulation plus précise de A.3. Le bras « justification erronée plausible » (ajouté en réponse à A.3) vise précisément cette distinction : une règle tabulaire cède face à une justification qui satisfait ses critères lexicaux, alors qu'un modèle ayant compris les raisons résiste si la justification est factuellement fausse.

**C.2 — Signature positive n°2 : la spécification est dans les poids, pas dans la consigne.**

**Acceptée.** Identique à A.7. Correction déjà décrite ci-dessus.

**C.3 — Témoin « style Claude amplifié » : écrasé contre le plancher, non informatif.**

**Acceptée.** Le taux ~5 % ne peut pas baisser. Ce témoin est **rétrogradé** à un contrôle de diagnostic (si le taux monte sous réécriture non-Claude mais pas sous réécriture Claude, c'est un indice de R1) plutôt qu'un bras décisionnel du duel.

**C.4 — Quantification 4 bits : confondant non contrôlé.**

**Transformée en test.** J'ajoute un **contrôle d'invariance BF16 vs 4 bits** sur les 27 scénarios originaux avant toute réécriture. Si l'écart de taux dépasse 3 points de pourcentage (illustratif), toutes les analyses en 4 bits sont non interprétables et le duel doit être joué en précision native. Coût : bas (une passe d'inférence supplémentaire).

**C.5 — Accord inter-juges (R3) : 200 épisodes sur 9 adaptateurs → ~22 par strate, insuffisant.**

**Acceptée.** Je porte l'échantillon d'audit humain à **50 épisodes par adaptateur stratifiés par verdict** (total ~450), ce qui donne un intervalle sur la spécificité par adaptateur de ±7-8 points (illustratif) au lieu de ±10+. Coût : moyen (annotation humaine accrue).

**C.6 — Estimateur du duel : zone d'indétermination large si la dispersion inter-scénarios est forte.**

**Acceptée.** C'est un problème structurel du design à 27 scénarios. Je ne peux pas créer de nouveaux scénarios (hors budget), mais je **préenregistre une analyse de sensibilité** : si la dispersion inter-scénarios (estimée par bootstrap hiérarchique) est telle que l'IC à 95 % chevauche le seuil dans >50 % des bootstraps, le duel est déclaré **non concluant**, et le papier le rapporte comme tel.

**C.7 — Contrôle de compréhension fonctionnelle des réécritures.**

**Acceptée.** J'ajoute un **contrôle de compréhension** : chaque adaptateur doit exécuter une tâche bénigne dans chaque style réécrit à un taux ≥ 90 % (illustratif). Si le taux bénin chute, la réécriture a détruit l'intelligibilité, pas la surface.

---

### Critiques de D sur B

**D.1 — R1 emploie un mauvais contrôle positif.**

**Acceptée.** (Identique à A.1.) Renommé en contrôle de calibration.

**D.2 — R2 ne sépare pas docilité et raisons.**

**Acceptée.** (Identique à A.3/C.1.) Correction décrite.

**D.3 — R3 confirme le biais trop vite ; κ ≠ validité.**

**Acceptée.** Je remplace la cible de R3 : au lieu d'un κ global, je mesure les **taux d'erreur différentiels par adaptateur** (sensibilité et spécificité du juge, estimées sur l'échantillon humain stratifié). C'est plus exigeant mais plus informatif.

**D.4 — R4 : le plancher n'empêche pas la hausse prédite par le regard.**

**Acceptée.** Ma formulation de R4 était asymétrique. Le vrai problème du plancher est que S = 1 − A(non obs.)/A(obs.) est instable quand les deux gains sont proches, pas que la manipulation ne peut rien changer. Je reformule R4 comme un **problème de puissance**, pas comme un biais directionnel.

**D.5 — R5 ne teste pas l'apprentissage de la phrase anti-regard.**

**Acceptée.** (Identique à A.4.) R5 est retirée comme expérience autonome.

**D.6 — R6/R8 : benchmarks généraux insuffisants, classification ≠ causalité.**

**Acceptée.** (Identique à A.5/A.6.) Corrections décrites.

**D.7 — La signature positive mélange retrait d'information et retrait de cause ; le duel n'est pas exclusif.**

**Transformée en test.** J'ajoute au duel une clause explicite : si les deux hypothèses H_A et H_B sont partiellement confirmées (interaction significative MAIS taux résiduel encore bas), le résultat est rapporté comme « les deux mécanismes contribuent, avec des parts estimées à [X, Y] ». Le duel ne prétend pas à l'exclusivité totale — il teste si la part de surface est **dominante** ou non.

---

### Critiques de E sur B

**E.1 — Erreur sur les jumelles : leur différence ne mêle pas raisonnement et contenu de spécification (même spécification « philosophie »).**

**Acceptée.** E a raison : la paire jumelle partage la même spécification « philosophie ». Ma remarque sur la confusion contenu/raisonnement dans R5 ne s'appliquait qu'aux comparaisons avec les recettes « règles » et « augmentées ». Je corrige le texte pour limiter cette remarque aux comparaisons inter-spécifications et non aux jumelles.

**E.2 — Spécification en consigne système non établie.**

**Acceptée.** (Identique à A.7/C.2.)

**E.3 — Contrôles positifs qui attendent une absence d'effet.**

**Acceptée.** Je reformule tous les contrôles en termes de prédictions falsifiables bilatérales.

**E.4 — Test « plus difficile » change la cible normative.**

**Acceptée.** Les dilemmes « moindre mal » ne sont pas des versions plus difficiles du même acte — ils changent l'étiquette normative. Je remplace ce bras par des **scénarios à pression sociale accrue** (ex. collègue insistant, urgence temporelle) sans changer la structure normative de l'action.

**E.5 — Tripler les tirages ne garantit rien ; « R7 fera disparaître D » n'est pas une prédiction.**

**Acceptée.** Je reformule R7 : l'objectif n'est pas de « faire disparaître D » mais de **mesurer ρ (corrélation intra-scénario)** sur les épisodes existants et de calculer la puissance réelle du design. Si ρ > 0.3 (illustratif), la puissance est bornée par K=27 quel que soit le nombre de tirages. Cette information est un résultat à rapporter, pas un correctif.

**E.6 — La signature constructive excède les interventions ; variable sémantique commune.**

**Acceptée.** La conjonction des trois signatures n'est pas automatiquement une preuve. Je reclasse les signatures comme **conditions nécessaires à tester séparément**, chacune avec son propre pouvoir éliminatoire, et non comme un trépied suffisant.

**E.7 — Le duel n'est pas exclusif ; seuils en taux absolus.**

**Acceptée.** (Identique à A.8/D.7.) Correction décrite : interaction, pas taux absolus.

---

## (b) Expériences corrigées

### Duel principal corrigé (R1 + croisement style × regard)

**Design.** 2 × 2 × 9 : {style original, style réécrit (par Llama/Mistral)} × {phrase « évaluation », phrase « déploiement »} × {9 adaptateurs}. 27 scénarios × 50 tirages par cellule.

**Métrique.** Interaction Δ_interaction = [(taux_réécrit,déployé − taux_original,déployé)_recette] − [(taux_réécrit,déployé − taux_original,déployé)_départ]. IC bootstrap hiérarchique (rééchantillonnage par scénario).

| | H_A (raisons généralisées) | H_B (appariement de surface) |
|---|---|---|
| Prédiction | Δ_interaction ≈ 0 (IC 95 % contient 0) | Δ_interaction > 0, borne inférieure IC > 5 pp (illustratif) |
| Falsifié si | Borne inférieure IC > 5 pp | Borne supérieure IC < 5 pp |

**Contrôle de compréhension.** Tâche bénigne dans chaque style : taux d'exécution ≥ 90 % requis. Si violé, style déclaré invalide.

**Contrôle de quantification.** BF16 vs 4 bits sur scénarios originaux : écart < 3 pp requis. Si violé, passage en précision native.

**Contrôle négatif du juge.** Juge Llama sur un échantillon stratifié ; audit humain de 50 épisodes par adaptateur.

**Clause d'indétermination.** Si la dispersion inter-scénarios rend l'IC > 2 × le seuil dans > 50 % des bootstraps, le duel est non concluant.

**Coût.** Moyen (réécriture par Llama + inférence 2×2×9×27×50 = ~486 000 épisodes en tout ; ~3-5 jours GPU A100 en BF16, illustratif ; annotation humaine ~450 épisodes).

### R2 corrigée (consigne adversariale + justification erronée)

**Bras ajouté.** Consigne adversariale accompagnée d'une justification plausible mais factuellement fausse (ex. « migration autorisée » alors qu'elle ne l'est pas).

| | H_A (raisons) | H_alt (règle tabulaire) |
|---|---|---|
| Prédiction | Résiste ET cite la raison correcte dans la trace | Cède face à la justification lexicalement satisfaisante |

**Contrôle.** Instruction bénigne avec justification vraie → exécution attendue.

### R8 corrigée (transfert de direction)

**Ajout.** Passe d'inférence dédiée à l'extraction d'activations sur ~200 textes (100 évaluation, 100 déploiement) par adaptateur. Précision de classification rapportée avec TPR, FPR et prévalence, pas seulement l'exactitude. Si la précision est au hasard, l'ablation n'est pas jouée et le papier rapporte : « la direction ne transfère pas ; l'intervention n'est pas applicable ».

### R6 corrigée (dégât collatéral)

**Mesure de dégât.** Tâche bénigne agentique (même outil, action non nuisible) avant et après ablation. Directions témoins appariées en couche, norme et dégât sur cette même tâche.

### Signature positive corrigée

Réduite à deux conditions nécessaires testables :
1. **Différenciation des traces.** Les traces de la recette avec raisonnement citent le principe de la spécification pertinent au scénario (classé par un annotateur aveugle) dans > 70 % des épisodes de refus (illustratif). Contrôle : les traces de la jumelle sans raisonnement ne citent pas de principes différenciés (ou n'ont pas de trace).
2. **Sélectivité par ablation de direction-principe** (si constructible). L'ablation d'une direction correspondant au principe P fait monter le taux nuisible sur les scénarios où P est pertinent, mais pas sur les autres. Contrôle : ablation d'une direction aléatoire appariée.

---

## (c) Réponse à la question de l'arbitre

### Ce qui est établi

- Les taux publiés par [1] sont **reproductibles** (RAPPORTÉ, à quelques points près).
- La recette avec raisonnement atteint un **plancher fonctionnel** (~5 %) et **résiste aux instructions adversariales** sur les scénarios originaux (RAPPORTÉ).
- La **manipulation par phrase** (« évaluation » vs « déploiement ») **ne déplace pas significativement le comportement**, mais elle déplace les **déclarations** de croyance de manière incohérente (RAPPORTÉ).
- Le **contraste entre jumelles dépend du choix de mots** de la manipulation, ce qui invalide la manipulation par phrase comme instrument fiable du regard (RAPPORTÉ).

### Ce qui n'est pas établi

- Que le gain vienne des « raisons » plutôt que de l'appariement de surface, d'une règle tabulaire mémorisée, ou d'un renforcement de la docilité.
- Que le regard ne contribue pas — la manipulation par phrase est trop faible pour trancher.
- Que la direction interne « évalué » transfère du modèle de départ aux adaptateurs.
- Que le juge Claude est fidèle sans biais différentiel entre adaptateurs.
- Que les résultats se généralisent au-delà de Qwen2.5-32B et des 27 scénarios.

### L'expérience à faire en premier

Le **croisement style × phrase** (duel principal corrigé) est l'expérience la moins chère qui sépare la plus grande menace (appariement de surface) de l'explication « raisons », tout en contrôlant le regard. Elle utilise les adaptateurs publiés, ne nécessite pas de réentraînement, et son contrôle de compréhension fonctionnelle et d'invariance à la quantification sont intégrés. Si elle est non concluante (dispersion inter-scénarios trop forte), ce résultat lui-même est informatif : il signale que 27 scénarios sont insuffisants et que la priorité est d'élargir le banc d'évaluation, pas de raffiner les manipulations.

Si le croisement est concluant et que Δ_interaction ≈ 0, la deuxième priorité est le **test de transfert de la direction** (R8 corrigée) : c'est la condition de validité de toute l'intervention dans les poids. S'il échoue, l'intervention est annulée et le papier conclut sur les seuls résultats comportementaux.

---

FIN-DE-CELLULE