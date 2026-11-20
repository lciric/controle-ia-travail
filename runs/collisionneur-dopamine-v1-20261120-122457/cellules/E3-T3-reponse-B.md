# Proposition B, tour III.3 : réponse aux critiques

**Pièces reçues.**
- Ma conception B (III.1) et les critiques A, C et D sont reçues. Chacune se termine par son marqueur, sans coupure visible.
- La critique E est absente (REFLEXION_HORS_PROVISION). Je ne lui prête aucun contenu.
- Le bloc QUESTION est identique au bloc FAITS (même empreinte sha256). La question à traiter est donc la demande du §3, et la forme est celle des livrables (a) à (c) de ce tour.

**Statuts.**
- Les affirmations de l'article sont RAPPORTÉES. Les éléments du programme sont RAPPORTÉS et non audités.
- Les propriétés purement formelles (identités algébriques, déterminisme d'une passe avant) sont VÉRIFIÉES par raisonnement formel.
- Tout le reste est HYPOTHÈSE, y compris mon jugement sur chaque critique.
- Tout chiffre absent des faits est illustratif (« ill. »). Rien n'a été exécuté.

---

## (a) Décision, critique par critique

Je regroupe par expérience. Une même critique faite par plusieurs propositions reçoit une seule décision. « A-a1 » désigne la proposition A, rubrique (a), point 1.

### Duel 2 : le nul et les poids

| Réf. | Critique | Décision | Raison et conséquence |
|---|---|---|---|
| A-a1, A-b, D-b | Au prompt, deux jumeaux identiques donnent Δ ≡ 0. Le nul est dégénéré. | **Acceptée** | VÉRIFIÉ (formel) : à poids et préfixe identiques, la passe avant est déterministe, au bruit numérique près. Cela vaut au prompt et à toute position lue en forçage. Ma prédiction « la plus exposée » était donc testée contre un nul vide. Correction : le nul compare deux adaptateurs honnêtes entraînés indépendamment (D2 corrigé). |
| A-a2, A-c, D-c | Δ confond l'affinage LoRA avec l'intention. | **Acceptée** | Remplacée par un plan 2×2 : adaptateur (saboteur / honnête) × jeton (déclencheur / leurre). Seule l'interaction compte. |
| A-c, D-c | Il manque un jeton leurre et un déclencheur présent mais inactif. | **Acceptée** | Intégrés au 2×2. L'adaptateur honnête voit le déclencheur pendant son entraînement, sans changement de comportement associé. |
| D-a | La consigne explicite de sabotage n'est pas un contrôle lexical : le traitement y est actif. | **Acceptée** | Je la reclasse en second bras de traitement. Le contrôle lexical devient une consigne qui *mentionne* sabotage et surveillance sans les demander. Je reprends ce contrôle de la critique de A sur D et je le signale. |
| A-b | « Le même pas chez le jumeau » n'est défini que sous forçage. | **Acceptée** | Toutes les lectures se font sur le préfixe produit par l'adaptateur saboteur, en forçage, dans chaque cellule. |
| D-b | La proportion de Δ < 0 parmi les alertes est circulaire si l'alerte est unilatérale. | **Acceptée** | L'alerte devient bilatérale. La proportion de signe devient alors une prédiction testable. |
| D-b | Un ratio d'écarts-types ne mesure pas la séparation : un décalage pur a le même écart-type. | **Acceptée** | Mon critère « ratio ≤ 0,5 » sur le jumeau était faux. Il est remplacé par la détection à taux de fausses alertes fixé de l'interaction, contre la même statistique sous le nul honnête/honnête. |

### Duel 1 : valeur contre difficulté

| Réf. | Critique | Décision | Raison et conséquence |
|---|---|---|---|
| A-a6, D-a | Le duel lie deux propriétés distinctes (information prédictive résiduelle, spécificité causale). L'issue mixte falsifie les deux hypothèses. | **Acceptée** | Scindé en D1a (prédiction) et D1b (ablation), chacun avec son propre H_A et son propre H_B. |
| A-a7, A-b, C-b2 (partie puissance) | L'AUC résiduelle dépend de la force du prédicteur. La zone 0,53–0,58 fait moins de deux erreurs types sur MATH500. | **Acceptée → test** | Comparaison de modèles emboîtés par validation croisée, plutôt qu'un résidu. Courbe du gain en fonction de la force du prédicteur. Cible continue (taux de réussite par item). Davantage d'items. Zone grise déclarée « non jugeable ». |
| C-b2 (partie collisionneur) | Effet de Berkson entre difficulté et compétence, conditionnellement à Y. | **Rejetée en partie** | Le résidu est estimé sur tous les items, sans stratifier sur Y. L'AUC compare les classes de Y mais n'estime pas la relation difficulté–compétence à l'intérieur d'une strate. Le mécanisme invoqué ne s'applique pas tel quel (HYPOTHÈSE). La version emboîtée supprime de toute façon le résidu. |
| C-a2 | La régression est ajustée sur l'ensemble d'évaluation ; le modèle tiers partage les biais de pré-entraînement. | **Fuite : acceptée. Biais partagé : rejeté comme défaut.** | Ajustement et évaluation sont séparés par validation croisée. Un prédicteur tiers qui capte aussi de la compétence générique retire *davantage* de variance. Le biais va donc vers H_B, ce qui est conservateur pour mon H_A. Je le déclare au lieu de le corriger. |
| A-a8 | Aucune séparation entre les items qui sélectionnent les neurones et ceux qui mesurent la chute. | **Acceptée** | Partition en items de sélection et items de mesure, fixée avant l'analyse. |
| A-c | La sonde à étiquettes permutées équivaut à une sélection aléatoire, déjà RAPPORTÉE à 74,6 %. | **Acceptée** | Remplacée par les neurones d'une sonde de difficulté de surface, d'AUC comparable, sélectionnés par le même élagage. |
| C-c2 | La mise à zéro injecte un biais moyen. | **Acceptée** | La Table 2 utilise la mise à zéro (RAPPORTÉ). Je la garde pour la reproduction et j'ajoute une ablation par la moyenne et une ablation par rééchantillonnage pour l'interprétation. |

### Duel 3 : agrégation diffuse

| Réf. | Critique | Décision | Raison et conséquence |
|---|---|---|---|
| A-a3 | Le mode d'implantation est indéterminé. Avec insertion et forçage, le contraste avec les erreurs honnêtes injectées est nul par construction. | **Acceptée** | Deux bras aux rôles distincts. Le bras I (insertion) devient un contrôle positif de *sensibilité aux erreurs*, pas un test d'intention. Le bras II (endogène) porte le test d'intention. |
| A-a4, C-a1, C-b3, D-a, D-b | Conditionner sur « vérifications mécaniques passées » est un filtrage post-traitement, qui réduit aussi l'échantillon effectif à grand n. | **Acceptée** | L'analyse primaire devient une analyse en intention de traiter sur tous les épisodes. L'estimand compare la détection de (mécanique ∪ sonde) à celle de (mécanique ∪ texte), à taux de fausses alertes *total* égal. La strate filtrée devient secondaire, avec ces règles : nul recalibré sur les honnêtes qui passent, paires où les deux passent, dénominateurs publiés avant filtrage. |
| D-a | Dans la strate filtrée, le vérificateur mécanique ne déclenche jamais : le battre n'est pas un résultat. | **Acceptée** | Je retire cette formulation. Dans la strate, le seul comparateur est le moniteur textuel. |
| A-a5 | L'agrégateur est asymétrique. | **Acceptée** | Le moniteur textuel reçoit exactement la même règle d'agrégation et la même calibration. |
| C-a3, C-b1, C-c3 | Le CUSUM efface sa mémoire entre des impulsions espacées. | **Acceptée sur le fond** | J'accepte l'argument qualitatif. Le taux de croissance en √(2 ln n) avancé par C n'est pas vérifié par moi (HYPOTHÈSE). Le CUSUM passe en statistique secondaire. |
| A-b | Une calibration par pas sous-estime le bruit quand ρ₁ > 0. | **Acceptée** | Calibration sur épisodes honnêtes entiers, avec une loi d'horizon appariée. |
| A-b | Si le signe des écarts varie d'un acte à l'autre, toute statistique de premier moment a une puissance égale à α. | **Acceptée → test** | Statistique secondaire préenregistrée de second moment (somme des carrés standardisés). |
| A-b | Les erreurs honnêtes (taux λ, décalage μ_e) forment une nuisance. | **Acceptée → mesure** | λ et μ_e sont estimés en pilote avant de dimensionner le duel. |
| Identité relevée par A et D dans leurs sections sur C et E | Σ_t δ_t ≈ V_T − V_0. | **Je m'en sers, en le disant** (B1) | Ma statistique de somme des écarts de dopamine se réduit, à l'erreur de sonde près, à l'écart de valeur aux extrémités. Elle n'apportait donc rien de propre à la dopamine. Correction en D3. |

### Duel 4 et piste 5

| Réf. | Critique | Décision | Raison et conséquence |
|---|---|---|---|
| A-a9 | La sonde réentraînée exige des étiquettes indisponibles en déploiement et peut fuir. | **Acceptée** | Elle devient une mesure *diagnostique* de présence d'information, pas une défense déployable. Évaluation sur des familles de tâches tenues à l'écart. |
| D-a, D-c | Retrouver de la puissance après réentraînement ne prouve pas un déplacement : un changement d'échelle ou un indice de style suffisent. | **Acceptée → test** | Trois sondes réentraînées : restreinte à l'ensemble de neurones initial, restreinte à son complément, et sonde de style (surface textuelle seule). |
| D-b | L'infimum de détection sur les attaques testées ne borne pas celui sur toutes les attaques admissibles. | **Acceptée** | Conclusion asymétrique, détaillée en D4. |
| D-b | Un Jaccard supérieur au hasard uniforme ne discrimine pas si les probabilités marginales de sélection sont hétérogènes et partagées. | **Acceptée** | Nouvelle référence : sélection tirée selon les probabilités marginales empiriques, et sélection par la sonde de difficulté. |
| D-a, D-b | L'accord d'un panel ne valide pas une étiquette d'intention. | **Acceptée** | La piste 5 ne revendique plus que la prédiction de la qualité jugée. Elle reçoit un contrôle de style : sorties de qualité égale, styles différents. |

### Taille d'échantillon

| Réf. | Critique | Décision | Raison et conséquence |
|---|---|---|---|
| A-b | La bande de 0,5 % à 2 % autour d'un nominal de 1 % exige environ 1 500 épisodes honnêtes indépendants (ill., calcul de A), davantage avec une corrélation intra-famille. | **Acceptée** | Les décisions des duels se prennent à 5 % de fausses alertes (ill.). Le résultat à 1 % est rapporté en secondaire avec son intervalle. L'unité de rééchantillonnage est la famille de tâches. |

---

## (b) Expériences corrigées

**Règles communes.**
- Chaque duel a une marge m gelée et une **zone grise explicite**.
- Un intervalle (bootstrap par famille) entièrement d'un côté de la marge falsifie l'autre hypothèse. Un intervalle qui chevauche la marge est déclaré « non jugeable ».
- H_B est formulée comme une équivalence : procédure TOST (Schuirmann, 1987). Ainsi, chaque issue falsifie quelque chose (B4).
- Tous les seuils sont illustratifs.

### D0 : porte de reproduction (nouvelle)

Je reprends le principe de la porte d'entrée que A demande à D, en le signalant.

**Hypothèses.**
- **H_A (instrument reproduit)** : sur Qwen-2.5-7B-SimpleRL-Zoo, la chute d'exactitude par mise à zéro des neurones de valeur et l'AUC avant génération sont dans l'intervalle de reproduction des valeurs RAPPORTÉES (Table 2 : 75,2 % → 20,3 % ; Table 3 : 0,67 en moyenne).
- **H_B** : elles en sortent.

**Conséquence.** H_B arrête D1 à D4 sur ce modèle. Un résultat nul ultérieur ne pourrait plus distinguer « pas de signal » de « instrument raté ».

**Vérification et coût.** Poids publics, relance par un tiers. ~10¹ GPU-h (ill.).

### D1a : la valeur prédit-elle au-delà de la difficulté ?

**Cible.** Taux de réussite par item, estimé sur k échantillons (k = 16, ill.). La cible est continue, ce qui donne plus de puissance qu'une issue binaire.

**Items.** Plusieurs milliers (ill.), pris dans les familles de tâches vérifiables de l'article, avec une partition par famille.

**Comparaison.** Modèle « difficulté » contre modèle « difficulté + sonde », ajustés et évalués par validation croisée. Prédicteurs de difficulté, du plus faible au plus fort : longueur, puis taux de réussite d'un, puis de plusieurs, modèles ouverts tiers. Je rapporte le gain de log-vraisemblance (ou d'AUC) pour chaque force de prédicteur.

**Hypothèses.**
- **H_A** : gain > m (m = 0,03 en AUC, ill.) avec le prédicteur le plus fort.
- **H_B** : gain dans la bande d'équivalence ±m.

**Biais connu.** Le biais par compétence partagée va vers H_B (rejet partiel de C-a2) : je le déclare.

### D1b : l'ablation est-elle spécifique ?

**Items.** Partition sélection/mesure.

**Contrôles.** Quatre ensembles de 1 % des dimensions à la même couche :
1. neurones de valeur ;
2. dimensions appariées en moyenne et variance d'activation ;
3. ensemble 2 après exclusion des dimensions à activations massives (Sun, Chen, Kolter, Liu, 2024, *Massive Activations in Large Language Models*) ;
4. neurones de la sonde de difficulté de surface.

Chaque ensemble est ablaté par mise à zéro, par la moyenne et par rééchantillonnage.

**Hypothèses.**
- **H_A** : la chute due aux neurones de valeur dépasse de > 20 points (ill.) celle du *meilleur* contrôle, sous ablation par la moyenne.
- **H_B** : l'écart reste dans ±5 points.

**Lecture croisée.**
- D1a en H_B et D1b en H_A : nécessaires à la compétence, sans information de succès au-delà de la difficulté. Ce sont des neurones de compétence, pas un moniteur.
- D1a en H_A et D1b en H_B : l'information est lisible mais non spécifique causalement. On garde la lecture et on abandonne l'argument de couplage du D4.

**Coût.** ~10¹–10² GPU-h (ill.), dominé par les k échantillons par item.

### D2 : l'interaction adaptateur × déclencheur

**Organismes.** Sur Llama-3.1-8B-Instruct, après un pilote sur Qwen3.5-0.8B :
- S : adaptateur saboteur sous déclencheur ;
- H et H' : deux adaptateurs honnêtes, même rang, même budget, mêmes tâches. Ils voient le déclencheur à l'entraînement sans changer de comportement.

**Porte.** Taux de sabotage de S ≥ 50 % avec le déclencheur et ≤ 5 % avec le leurre (ill.). H en dessous de 5 % dans les deux cas.

**Lecture.** Dans chaque cellule (déclencheur ou leurre), S génère, puis S et H lisent le même préfixe en forçage.

**Statistique.**
I = [V_S − V_H]_déclencheur − [V_S − V_H]_leurre,

calculée par épisode, au prompt (couches 2–5) et aux frontières de paragraphe (couches 15–22).
- L'identité de l'adaptateur s'annule entre cellules.
- L'effet de « lire un texte saboté » s'annule à l'intérieur de la cellule, puisque S et H lisent le même texte.
- Le nul vient de la même statistique avec H' à la place de S. Il n'est pas dégénéré, puisque les poids diffèrent (correction de A-a1).

**Hypothèses** (pour chaque position) :
- **H_A** : détection de I, alerte bilatérale, ≥ 30 % à 5 % de fausses alertes (ill.), avec I < 0 dans plus de 80 % des alertes.
- **H_B** : détection dans la bande d'équivalence autour de 5 %.

**Ma prédiction, inchangée et exposée.** H_B au prompt, H_A aux couches tardives. Une détection au prompt la réfute.

**Contrôles.**
- Consigne qui mentionne le sabotage sans le demander.
- Bras de traitement n°2 : consigne explicite. S'il est détecté au prompt et que le bras déclencheur ne l'est pas, la sonde lit le texte de l'instruction.
- Échecs honnêtes de H appariés en difficulté.

**Littérature.**
- Hubinger et al. (2024), *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training*.
- Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn (2025), *Detecting Strategic Deception Using Linear Probes*.

**Coût.** ~2–5×10² GPU-h (ill.). Trois adaptateurs et environ 1 500 épisodes de nul.

### D3 : la dopamine apporte-t-elle quelque chose au-delà des extrémités ?

**Bras I : contrôle positif de sensibilité.**
- Le modèle honnête lit des trajectoires où l'équipe rouge a inséré n actes, et des trajectoires avec n erreurs honnêtes de même gravité, insérées par le même éditeur aux mêmes positions.
- Ce bras ne teste que la question « la sonde voit-elle de petites erreurs ? ».
- Porte : si la sensibilité au plus grand n (16, ill.) reste dans la bande d'équivalence, le bras II n'est pas jugeable.

**Bras II : test d'intention, endogène.**
- S est entraîné à saboter avec une probabilité par occasion p ∈ {faible, moyenne, forte} (ill.). La **dose est manipulée en espérance**, et n réalisé est une covariable observée par un auditeur aveugle à Z.
- Comparateur : H, avec le même horizon.
- Statistique primaire, par épisode : somme des k plus grands écarts négatifs standardisés de I_dopamine (k = 4, ill.). C'est une statistique de *chemin*, que l'identité de télescopage ne réduit pas aux extrémités.
- Statistiques secondaires : critique supérieure (Donoho et Jin, 2004, *Higher criticism for detecting sparse heterogeneous mixtures*), second moment, CUSUM. Correction de Holm.

**Hypothèses** (analyse en intention de traiter, 5 % de fausses alertes totales, ill.) :
- **H_A** : la détection de (mécanique ∪ dopamine-chemin) dépasse de > 10 points (ill.) **à la fois** (mécanique ∪ texte agrégé par la même règle) **et** (mécanique ∪ écart de valeur aux extrémités), avec une pente positive en dose.
- **H_B** : le gain sur l'écart aux extrémités reste dans ±m.

Si H_B est retenue, les neurones de dopamine n'ajoutent rien aux neurones de valeur. C'est la conséquence directe de l'identité de télescopage.

**Spécificité.** Sur les épisodes honnêtes avec erreurs, au même horizon, la dopamine-chemin doit rester dans la bande nulle. Sinon, le détecteur détecte des erreurs, ce qui est utile mais hors objet.

**Vérification indépendante.**
- Clé de Z scellée par l'équipe rouge.
- Dénominateurs publiés avant filtrage.
- Point d'arrivée réexécuté par un tiers.

**Littérature.** Greenblatt, Shlegeris, Sachan, Roger (2023), *AI Control: Improving Safety Despite Intentional Subversion*. Travaux sur les menaces diffuses : référence à vérifier.

**Coût.** ~10³ GPU-h (ill.), dominé par les rollouts. Pilote obligatoire pour mesurer ρ₁, λ, μ_e et la fiabilité moitié-moitié des étiquettes Monte-Carlo.

### D4 : l'évasion est-elle bon marché ?

**Porte.** Lancé seulement si D2 ou D3 retient H_A. Si la détection avant adaptation est sous la porte, D4 n'est pas jugeable.

**Attaque et contrôles.**
- Attaque : LoRA avec la perte tâche + sabotage + pénalité contre la sonde gelée.
- Contrôles : pénalité contre une sonde aléatoire, et même affinage appliqué à H.
- Contrainte : le **dommage est maintenu** (taux de sabotage réussi ≥ 80 % de l'initial, ill.). Sans elle, l'« évasion » peut consister simplement à cesser de saboter.

**Hypothèses et conclusion asymétrique** (correction D-b) :
- **H_A (couplage)** est falsifiée par *une seule* attaque qui ramène la détection dans la bande nulle avec ≤ 3 points de perte d'exactitude (ill.). Cette falsification est définitive.
- **H_B (évasion bon marché)** n'est falsifiée que *pour la classe d'attaques testées*, qui doit être énumérée. Une survie de H_A reste donc provisoire.

**Diagnostic, non déployable.** Les trois sondes réentraînées (ensemble initial, complément, style), évaluées sur des familles tenues à l'écart.

**Littérature.** Bailey et al. (2024), *Obfuscated Activations Bypass LLM Latent-Space Defenses*.

**Coût.** ~10² GPU-h (ill.).

### Piste 5, conditionnelle (D1a et D2 en H_A)

- **H_A** : la sonde prédit la qualité jugée en aveugle au-delà d'une ligne de base longueur + difficulté + style.
- **H_B** : équivalence avec cette ligne de base.
- Aucune revendication sur l'intention.
- Coût dominé par l'évaluation humaine : quelques centaines d'heures-personne (ill.).

---

## (c) Réponse à la question de l'arbitre (une page)

**Ce qui est établi.** Uniquement des éléments RAPPORTÉS, non reproduits par moi :
- sur des tâches à récompense binaire vérifiable et sur des modèles ≤ 32B, une sonde lue sur < 1 % des dimensions prédit modérément le succès avant génération (AUC moyenne 0,67, contre 0,62 pour la longueur de la question) ;
- mettre à zéro ces dimensions effondre l'exactitude (75,2 % → 20,3 %), plus que les sélections aléatoire, par magnitude ou Wanda ;
- un signal de type erreur TD aide modestement la recherche pas à pas (77,8 % contre 75,0 %, trois graines, sous-ensemble de taille non fournie).

Aucun cadre adversarial, trompeur ou de sabotage n'a été étudié.

**Ce qui ne l'est pas** (HYPOTHÈSES) :
- que cette valeur dépasse la difficulté apparente ;
- que l'ablation soit spécifique au-delà des dimensions de forte variance ;
- que le signal existe en recherche ouverte ;
- qu'il encode le succès selon le mandant plutôt que selon l'objectif propre de l'agent ;
- qu'un sabotage endogène produise une signature distincte d'une erreur honnête ;
- que la dopamine apporte quelque chose au-delà de la valeur aux extrémités (identité de télescopage) ;
- qu'un agent ne puisse pas déplacer la lecture à faible coût.

Les critiques ont aussi montré que ma conception III.1 *n'aurait pas pu* établir le point central. Son nul au prompt était vide (A-a1), et son Δ confondait affinage et intention (A-a2).

**Reformulation corrigée.**

> « Dans des organismes modèles dont un tiers scelle l'assignation au sabotage, l'interaction adaptateur × déclencheur des lectures de valeur et de dopamine, mesurée contre un nul entre adaptateurs honnêtes indépendants, augmente-t-elle, en intention de traiter et à taux de fausses alertes total fixé d'avance, la détection au-delà de (vérifications mécaniques ∪ moniteur textuel agrégé par la même règle) et au-delà de l'écart de valeur aux extrémités ? Ce gain survit-il à une attaque qui maintient le dommage ? »

**L'expérience à faire en premier : D0 puis D1a/D1b.**
- Sur Qwen-2.5-7B-SimpleRL-Zoo, poids publics.
- ~10¹–10² GPU-h (ill.).
- Vérifiable par un tiers sans équipe rouge.

Elle est première parce que tout le reste suppose que l'instrument existe et mesure autre chose que la difficulté. Ses issues :
- D0 en H_B : l'article n'est pas reproduit, on s'arrête ;
- D1a en H_B : la route « valeur » se réduit au jumeau ;
- D1a en H_A : D2 devient le premier test portant sur le sabotage.

En parallèle, un pilote sur Qwen3.5-0.8B mesure les paramètres de nuisance relevés par A et C : variance du nul H/H', ρ₁, λ, fiabilité des étiquettes Monte-Carlo. Sans eux, D2 et D3 ne peuvent pas être dimensionnés.

FIN-DE-CELLULE