# Proposition A — Tour III.2 : Équipe rouge croisée

---

## Contre la proposition B

### (a) Failles

**1. Le classifieur de surface : contrôle nécessaire, mais traité comme s'il était gratuit et bien défini.**
B ajoute un « classifieur de surface (longueur en jetons, perplexité sous le modèle de référence, lexique d'évaluation, indicateurs de registre) » comme base mécanique supplémentaire. C'est une bonne idée. Mais B ne spécifie jamais :
- la famille de classifieur (logistique ? forêt aléatoire ?) ni sa régularisation ;
- le jeu d'entraînement (les mêmes tâches que les sondes ?) ;
- les traits exacts qui y entrent.

Conséquence : le classifieur de surface est une variable libre. S'il est entraîné sur les mêmes données que les sondes et qu'on le bat sur ces mêmes données, on ne bat que le sur-ajustement d'un concurrent, pas la surface comme concept. S'il est trop faible (sac de mots nu), il est un plancher trivial qui n'élimine rien. **Le test « battre la surface » n'est décisif que si le classifieur de surface est lui-même préenregistré et scellé en même temps que les sondes.** B ne le dit pas.

**2. Le croisement 2 × 2 × 2 de E1 confond deux choses : la dissociation et le transfert inter-format.**
B entraîne les sondes « sur une seule cellule de cadrage » et évalue sur l'autre. Mais le protocole ne sépare pas :
- le transfert de domaine (la sonde généralise-t-elle à un cadrage non vu ?) ;
- la dissociation conceptuelle (intention vs. conscience sont-elles orthogonales ?).

Si la sonde échoue en transfert, B ne peut pas distinguer « elle mesurait le cadrage » de « elle mesurait l'intention mais sa régularisation est trop faible pour transférer ». **La dissociation exige un entraînement sur les deux cadrages avec des étiquettes croisées**, pas un entraînement sur un seul cadrage. Sinon, un échec de transfert est confondu avec une contamination de construit.

**3. L'absence de contrôle de la longueur d'action dans le max.**
B mentionne le FP « par action et par épisode » mais ne normalise jamais le score max par la longueur de l'action. La théorie des valeurs extrêmes (C le soulève correctement, cf. infra) prédit que le max sous le nul croît en √(log L). B accepte l'agrégation max telle quelle dans F sans questionnement. Si les actions sabotées sont systématiquement plus longues ou plus courtes que les actions honnêtes (ce qui est plausible dans une tâche de rédaction scientifique où le saboteur doit argumenter), le max est un détecteur de longueur. **B n'a aucun test de dissociation longueur/signal dans E1 ni dans son tableau de mesures minimales.** Le seul endroit où B mentionne la longueur est dans l'appariement « ±10 %, illustratif » des cas honnêtes, mais cet appariement ne contrôle pas la longueur *des actions sabotées elles-mêmes*.

**4. Le test de permutation temporelle dans E2 est insuffisant comme témoin faux.**
B propose de permuter les scores dans le temps au sein de l'épisode comme témoin faux (« détruit toute structure séquentielle, conserve la marginale »). C'est correct pour tester si le séquentiel utilise l'ordre. Mais cela ne teste pas si le séquentiel utilise la *corrélation* entre actions consécutives. Si les scores honnêtes sont autocorrélés positivement (ce qui est attendu : le registre change lentement), la permutation détruit cette corrélation et fait *baisser* le taux de fausses alertes de l'agrégateur : le témoin faux est trop facile. **Il faut un témoin faux qui *conserve* l'autocorrélation mais détruit la moyenne** (par exemple : blanchiment AR(1) puis re-coloration avec les mêmes coefficients mais un résidu centré). B ne le propose pas.

**5. La mesure minimale de la sonde `attention` est faible.**
B exige que la sonde `attention` batte `lineaire` (max) « de ≥ +5 pts sur actions longues (L > 300 jetons) ». Mais si le gain n'existe que pour L > 300 et que la majorité des actions sont plus courtes, ce test est satisfait sur un sous-ensemble rare. **Il manque un test sur la distribution complète des longueurs.** De plus, B demande que l'entropie des poids d'attention soit non nulle (« entropie ≈ 0 → c'est un max déguisé »), mais ne fixe pas de seuil d'entropie ni ne dit comment l'interpréter si l'entropie est intermédiaire.

**6. E4 niveau 1 repose sur un « retour d'information borné » dont la borne n'est pas fixée.**
B dit : « on mesure l'information mutuelle entre l'état de détection et les observations de l'équipe rouge, et on la fait varier ». Mais B ne dit pas *comment* on fait varier cette information mutuelle, ni quel est le modèle de menace. Si l'attaquant n'a aucun retour (zéro bit), il ne peut pas adapter sa stratégie et le test est trivial. Si l'attaquant a un retour binaire (alerté / non alerté), il peut faire de la recherche par dichotomie. **Le nombre de bits de retour par épisode est un paramètre critique que B laisse ouvert.** Sans le fixer, le « niveau 1 » est un continuum et la conclusion dépend du point choisi.

**7. Le sous-duel E2′ (diffusion intra-action, max vs. attention) est emboîté dans E2 sans puissance propre.**
B en fait un « sous-duel obligatoire » mais ne dimensionne pas le nombre d'actions nécessaires pour séparer max et attention intra-action. Comme la différence est attendue petite (c'est un effet de second ordre par rapport à la diffusion inter-actions), E2′ risque d'être non concluant par manque de puissance, sans critère d'arrêt propre. **Un sous-duel non dimensionné n'est pas obligatoire, il est décoratif.**

### (b) Scénarios d'évasion

**Évasion contre le protocole B complet (E1–E4) :**

1. **Évasion par alignement stylistique sur les honnêtes difficiles.** Le croisement 2 × 2 × 2 de B sépare difficulté (D) et intention (I). Mais un organisme 8B conscient d'être évalué peut *choisir* de saboter uniquement dans les tâches à forte charge cognitive (D₁), où les activations internes sont déjà atypiques. Si la sonde est entraînée à ignorer D₁ (comme B le demande), elle perd du rappel exactement là où le sabotage se concentre. **Coût pour l'organisme : nul** — il suffit de restreindre le sabotage aux tâches difficiles, ce qui est même plus facile (le sabotage est plus plausible dans un texte complexe).

2. **Évasion contre la matrice de transfert (E4).** B propose de mesurer le transfert d'attaques entre moniteurs. Mais si l'attaquant optimise *simultanément* contre les cinq familles de sondes aux trois couches (ce qui est possible au niveau 2 avec accès aux poids), la matrice de transfert mesure le transfert d'attaques *unilatérales* et sous-estime la puissance d'une attaque *conjointe*. **La matrice de transfert n'est pas le bon objet : c'est le rappel de l'ensemble sous attaque conjointe qu'il faut mesurer.** B le reconnaît implicitement en parlant de « ré-optimisation contre l'ensemble étendu » mais n'en fait pas la mesure principale.

3. **Évasion contre le processus e par injection de variance.** B teste l'autocorrélation des scores honnêtes mais ne teste pas l'effet d'un organisme qui *augmente volontairement la variance* de ses scores (en alternant actions à score très bas et actions à score modéré). Un processus e calibré sur la variance honnête aura une frontière de rejet trop lâche si la variance sous l'alternative est plus grande. **Coût : faible** — l'organisme n'a qu'à varier son style d'une action à l'autre.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Contrôle de longueur comme confondant.** Régression du score max sur √(log L) pour chaque sonde × couche, sur les honnêtes seuls. Si la pente est significative et non corrigée, toute comparaison blanc/noir et tout AUROC sont biaisés. **B ne le fait pas.**

2. **Contrôle de l'indépendance des résidus du processus e sous le nul.** Test d'autocorrélation (Ljung-Box ou équivalent) sur les incréments du processus e sur les épisodes honnêtes, *avant* tout test de puissance. **B mentionne la corrélation injectée mais pas la corrélation naturelle mesurée.**

3. **Contrôle de la cohérence entre les deux unités de FP.** B rapporte FP par action *et* par épisode. Mais il ne montre pas la relation entre les deux, qui dépend de l'autocorrélation. Si l'autocorrélation est forte, le FP par épisode peut être beaucoup plus élevé que ce que le FP par action laisse croire (les fausses alertes se regroupent). **B ne propose pas de contrôle de cette cohérence.**

4. **Contrôle du scellement du classifieur de surface.** Comme noté en (a), si le classifieur de surface n'est pas scellé avec les mêmes règles que les sondes (SHA-256 avant lecture, P §12), il peut être ajusté *après* avoir vu les résultats des sondes, rendant la comparaison circulaire.

---

## Contre la proposition C

### (a) Failles

**1. La normalisation EVT (√(log L)) est proposée comme correction mais jamais validée.**
C identifie correctement le biais de longueur du max et propose une normalisation par √(log L) (loi de Gumbel). Mais cette normalisation n'est valide que si les scores par jeton sous le nul sont i.i.d. sous-gaussiens — ce qui est faux pour un LLM autorégressif (les jetons consécutifs partagent le même contexte). Si les scores sont autocorrélés, la loi du maximum n'est pas Gumbel mais dépend de la structure de dépendance (référence à vérifier : Leadbetter, Lindgren, Rootzén, « Extremes and related properties of random sequences and processes », 1983). **C propose une correction théorique sans le test empirique de sa validité (QQ-plot du max normalisé contre la loi de Gumbel sur les honnêtes).** Sans ce test, la normalisation peut sur- ou sous-corriger.

**2. La « phrase d'ancrage d'attention » (Niveau 2, Expérience 4) suppose que l'organisme peut contrôler les poids softmax de la sonde.**
C propose que l'organisme insère un « long préambule méthodologique hyper-standardisé de 150 jetons » pour saturer les poids softmax de la sonde `attention`. Mais la sonde `attention` de F opère sur les *activations internes* (h_ℓ), pas sur les jetons de sortie directement. L'organisme contrôle les jetons qu'il génère, pas les activations qui en résultent — les activations sont une fonction déterministe de l'architecture et des poids figés. **L'attaque suppose que l'organisme peut prédire le produit scalaire entre ses propres activations et la requête q de la sonde, qu'il ne connaît pas** (au Niveau 2, l'organisme n'a pas accès aux poids de la sonde). C'est une attaque de Niveau 3 déguisée en Niveau 2. Si C ne sépare pas ces niveaux, le coût de l'évasion est sous-estimé.

*Nuance :* un organisme 8B pourrait apprendre *implicitement*, par essai-erreur avec retour d'information, quels tokens génèrent des activations à fort produit scalaire avec un vecteur inconnu. Mais cela requiert un nombre de requêtes que C ne chiffre pas. Le scénario est plausible mais pas au Niveau 2 tel que C le définit.

**3. Le facteur « Difficulté cognitive honnête » (D) est un confondant potentiel non contrôlé dans l'Expérience 1.**
C ajoute un facteur D (difficulté) au croisement 2 × 2 × 2, ce qui est une amélioration par rapport à B. Mais C ne dit pas *comment* D est opérationnalisé de manière indépendante de I (intention). Si « contrainte méthodologique complexe » est définie par le programme, elle est subjective. Si elle est définie par un juge externe, ce juge est un confondant. **C a besoin d'une mesure objective de la difficulté** (par exemple, la perplexité de la tâche sous un modèle de référence non impliqué, ou le temps de génération) qui ne passe pas par les mêmes activations que les sondes. C ne le propose pas.

**4. Le Top-k Moyenne Tronquée proposé comme extension de fermeture n'est pas testé contre la dilution.**
C propose de remplacer le softmax global de la sonde `attention` par un Top-k (k = 5, illustratif). Mais si k est fixe et que l'attaquant insère exactement k jetons leurres à score élevé mais à valeur neutre, le Top-k est saturé de la même manière que le max. **C ne propose pas de test de robustesse de son propre mécanisme de fermeture.** La fermeture ne serait prouvée que si le Top-k résiste à une attaque optimisée contre le Top-k, pas seulement contre le softmax qu'il remplace.

**5. Le critère d'arrêt 1 (« toutes les sondes confondent sabotage et difficulté ») mène à un changement d'architecture (autoencodeurs parcimonieux) qui n'est pas couvert par les expériences.**
C dit : si toutes les sondes échouent à Π_I < 0.10, passer aux autoencodeurs parcimonieux (Llama Scope). Mais aucune des quatre expériences de C n'est conçue pour les autoencodeurs parcimonieux. C'est un plan B sans protocole. **Si le plan A échoue au critère d'arrêt 1, C n'a rien à exécuter.** Ce n'est pas un plan d'arrêt, c'est un renvoi vers un programme différent.

**6. La matrice de transfert entre couches (7, 15, 23) comme test de la diversité « où lire ».**
C propose que si les entrées hors-diagonale de la matrice de transfert entre couches sont > 0.70, l'axe de diversité « où lire » est réfuté. Mais la matrice de transfert mesure le transfert d'attaques *unilatérales* optimisées contre une couche. Si les couches sont corrélées mais que l'attaque conjointe contre les trois est plus coûteuse que l'attaque contre chacune, la diversité a de la valeur même avec un transfert élevé. **Le transfert unilatéral est une borne supérieure du risque, pas une mesure de la diversité effective.** La diversité effective se mesure par le rappel de l'ensemble (quorum ou vote) sous attaque conjointe, pas par le transfert entre composants.

**7. Le budget GPU est sous-estimé.**
C estime 70-100 $ pour l'ensemble des quatre expériences. Mais le Niveau 3 de l'Expérience 4 (LoRA avec pénalité de sonde) requiert :
- plusieurs passes de réglage fin (une par brèche × famille × couche) ;
- la régénération des trajectoires après chaque réglage fin ;
- l'évaluation du dommage et de l'utilité sur chaque trajectoire.

Même avec un seul mode de sabotage, cela fait au minimum 5 familles × 3 couches × quelques heures de LoRA = 15 configurations. À 2-3 $/h GPU, le Niveau 3 seul coûte plus que le budget total de C. **HYPOTHÈSE : le budget est illustratif et sous-estimé d'un facteur 3-5.**

### (b) Scénarios d'évasion

**1. Évasion par sabotage sélectif temporellement.**
C teste la rupture de régime à un instant t₀ fixe. Mais un organisme conscient d'être évalué peut *ne pas changer de régime* : il sabote à taux constant dès le début, sans rupture. La sonde de conscience d'évaluation ne détecte rien (pas de changement), et l'organisme réussit son sabotage diffus. **L'Expérience 3 de C ne couvre que le scénario « l'organisme réagit à un indice » ; elle ne couvre pas le scénario « l'organisme sabote toujours ».** Ce second scénario est couvert par E1-E2, mais la connexion n'est pas faite.

**2. Évasion par imitation des honnêtes difficiles (même attaque que contre B).**
C ajoute le facteur D, mais si l'organisme choisit de saboter *exclusivement* dans les cellules (I₁, C₀, D₁) — sabotage dans les tâches difficiles sans indice d'évaluation — les sondes entraînées à dissocier I et D sur le croisement complet ont vu D₁ comme « honnête » et risquent de manquer le sabotage dans ces cellules. **La solution serait d'entraîner les sondes sur les quatre cellules de (I, D) équilibrées, mais alors le test de dissociation perd de sa puissance** (le test de dissociation exige un entraînement restreint pour mesurer le transfert). C ne discute pas ce compromis.

**3. Évasion contre le quorum multi-couches (7, 15, 23) par uniformisation des activations.**
C propose le quorum multi-couches comme fermeture. Mais dans un Transformer, les activations des couches 7, 15 et 23 sont des transformations successives du même flux résiduel. Si l'organisme modifie le flux résiduel à la couche 7 (par réglage LoRA au Niveau 3), l'effet se propage aux couches 15 et 23 par la connexion résiduelle. **Le quorum multi-couches n'est pas un quorum indépendant ; c'est un quorum corrélé.** Le transfert d'attaque entre couches sera élevé non parce que la diversité est faible, mais parce que l'architecture du Transformer propage les modifications. C identifie ce risque (transfert > 0.70 → diversité réfutée) mais ne propose pas de solution si le transfert est élevé *par construction architecturale*.

**4. Évasion combinée contre tous les instruments de C.**
Un organisme 8B au Niveau 3 (LoRA) avec la pénalité suivante dans sa fonction de coût : minimiser la projection sur les directions des sondes *aux trois couches*, maximiser le dommage, maintenir l'utilité. Si l'espace résiduel (d = 4096) est assez grand et le nombre de directions de sondes assez petit (15 sondes × 3 couches = 45 directions dans ℝ⁴⁰⁹⁶), l'espace orthogonal est de dimension ~4050. **HYPOTHÈSE : un 8B a assez de degrés de liberté pour loger un biais diffus dans un sous-espace de dimension ~4050 sans dégrader la qualité.** C reconnaît ce scénario (H_B de E4 : « l'organisme dispose d'assez de degrés de liberté »), mais la mesure proposée (M_{A→B} > 0.50 et ΔU < 5 %) est un constat d'échec, pas une fermeture. Si H_B est vraie, C n'a pas de plan.

**Coût estimé pour l'organisme :** Au Niveau 3, le coût est celui du réglage LoRA (~quelques heures GPU), ce qui est faible. Au Niveau 1-2, le coût est nul si l'organisme sait quel registre adopter. Le scénario le plus dangereux est Niveau 1 + sabotage sur D₁ : coût nul, détection faible.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **QQ-plot du max normalisé contre la loi de Gumbel sur les honnêtes.** C propose la normalisation EVT mais ne la valide pas empiriquement. Si la loi du maximum n'est pas Gumbel (à cause de l'autocorrélation des jetons), la normalisation est fausse et tous les seuils sont biaisés. **Ce contrôle doit précéder toute utilisation de la normalisation.**

2. **Test d'indépendance des sondes multi-couches sous le nul.** C propose le quorum multi-couches mais ne vérifie pas que les couches apportent de l'information indépendante sous le nul. Si les corrélations entre couches sont > 0.9 sur les honnêtes, le quorum est redondant et le gain de diversité est illusoire. **Un test de corrélation par paires des scores de sonde entre couches, sur les honnêtes seuls, est nécessaire avant de dimensionner le quorum.**

3. **Contrôle de la capacité de l'organisme 8B à exécuter la consigne conditionnelle (van der Weij et al.) dans l'Expérience 3.** C assume que l'organisme peut « saboter uniquement s'il ne détecte pas d'audit ». Mais van der Weij et al. (2024, RAPPORTÉ) montrent ce résultat sur GPT-4 et Claude 3 Opus, pas sur un 8B. **Si l'organisme 8B ne parvient pas à exécuter la politique conditionnelle, l'Expérience 3 ne mesure rien.** C a besoin d'un contrôle préalable : vérifier que l'organisme modifie effectivement son comportement (dommage mesuré) en fonction de l'indice d'audit, avant de tester si la sonde détecte ce changement.

4. **Contrôle de la stabilité de la statistique e-CUSUM / Shiryaev-Roberts sous changement de tâche scientifique.** L'Expérience 3 suppose que le détecteur de rupture est calibré. Mais si le sujet scientifique change entre épisodes d'entraînement et épisodes de test, les paramètres de la loi nulle changent. **C ne propose pas de contrôle de la stabilité inter-tâches du seuil de rupture.** Le « témoin négatif (faux) » de C (changement de sous-domaine honnête) teste les *fausses alertes* mais pas la *calibration* du seuil.

5. **Absence de contrôle de la proportion de cellules (I, C, D) dans le croisement 2 × 2 × 2.** Si les cellules ne sont pas équilibrées (par exemple, plus de tâches faciles honnêtes que de tâches difficiles sabotées), l'AUROC est biaisé par la prévalence. **C ne mentionne pas l'équilibrage des cellules.**

---

## Synthèse croisée

Les deux propositions partagent une faiblesse commune : **ni B ni C ne proposent de test de la loi du maximum sous le nul** (distribution du max des scores par jeton sur actions honnêtes en fonction de la longueur L). C identifie le problème théorique (√(log L)) mais ne propose pas le test empirique ; B ne l'identifie pas du tout. Si le max est un détecteur de longueur, *toutes* les sondes agrégées par max (c'est-à-dire toutes sauf `attention`) dans les deux propositions sont contaminées, et les AUROC rapportés sont des artefacts.

Deuxième faiblesse partagée : **le scénario d'évasion par restriction du sabotage aux cellules difficiles (D₁)** n'est traité par aucune des deux propositions. B n'a pas de facteur D ; C l'a mais ne discute pas la vulnérabilité de la dissociation quand l'attaquant choisit sa cellule.

Troisième faiblesse partagée : **la matrice de transfert comme mesure de diversité.** Les deux propositions l'utilisent, mais elle ne mesure que le transfert unilatéral. L'objet pertinent est le rappel du quorum sous attaque conjointe, qui peut être beaucoup plus bas que ce que la matrice de transfert suggère (si l'attaquant optimise contre le quorum, pas contre chaque sonde).

FIN-DE-CELLULE