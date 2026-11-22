# Proposition B — Tour III.2 : critique croisée de méthode

**Pièces.** La conception A est absente (REFUS) : je ne la critique pas et je n'en reconstruis rien. Le bloc FAITS reproduit la question et ne contient aucune donnée empirique ; tout ce qui suit porte donc sur des protocoles, et toutes mes objections ont le statut **HYPOTHÈSE**, sauf mention contraire. Les nombres que je calcule reprennent les valeurs illustratives des autres propositions et sont eux-mêmes **illustratifs**.

---

## Sur la proposition A

Pièce absente (REFUS) : pas de critique possible.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Le capteur Φ₁ est vrai par construction.** C définit l'attaque OEBM comme une exclusion documentaire asymétrique. Elle choisit ensuite comme capteur étendu Φ₁ une divergence de Kullback-Leibler entre documents sources et documents retenus, c'est-à-dire la statistique même qui décrit le mécanisme. L'instrument qui doit attester « il faut un nouveau capteur » est donc construit à partir de la connaissance de l'attaque : la condition AUROC(Φ₁) ≥ 0,85 teste l'implémentation, pas la catégorie. On a une fuite directe entre conception de l'attaque et conception de l'évaluateur.

2. **Le contenu de Φ₀ est fixé par l'expérimentateur.** Le juge lit le texte, et la liste des documents cités y figure. Que la statistique de rétention soit ou non « dans Φ₀ » dépend donc de la façon dont on extrait les « représentations latentes du juge ». Un verdict « catégorie » peut résulter d'un choix d'extraction pauvre, et non d'une propriété de l'attaque.

3. **L'adaptateur et le sabotage sont confondus.** OEBM est instancié par un LoRA et comparé au modèle de base honnête. Les sondes internes peuvent séparer « poids modifiés » de « poids d'origine » indépendamment de toute dégradation. Dans l'expérience 3, C_ctx et C_LoRA diffèrent à la fois par le canal (contexte ou poids) et par la présence d'un adaptateur. Conclure que la sonde « détecte la conscience sémantique de transgresser » n'est pas licite.

4. **Le sup sur 𝓕 n'est pas observable.** Le critère porte sur sup_{f∈𝓕} AUROC, mais on n'observe que l'AUROC des classifieurs essayés, estimée sur un échantillon fini. Un échec de recherche est pris pour une absence de signal : la catégorie devient une propriété du budget d'optimisation et de l'effectif.

5. **La distance NCD est vraie par construction dans un sens et confondue dans l'autre.**
   - NCD_intra < 0,40 est presque garanti, puisque toutes les instances OEBM proviennent du même LoRA ou du même gabarit de prompt.
   - NCD > 0,70 avec les attaques connues est dominé par le contenu des dossiers, qui diffèrent, et par la fonction d'abstraction z, choisie librement.

6. **Le seuil de dégradation est appliqué après coup.** La règle « si ΔU < 0,35, l'expérience est invalide » conditionne l'analyse sur le succès du saboteur. Les répétitions où l'attaque échoue disparaissent, ce qui biaise toute estimation conjointe (ΔU, AUROC).

7. **Le contrôle négatif de l'expérience 2 est incohérent.** Φ₀ y est déclaré « trivial » (une liste noire), mais la re-capture se fait par un « classifieur sémantique déjà présent dans Φ₀ ». Les deux affirmations ne peuvent pas être vraies en même temps.

8. **Statuts.** C attribue VÉRIFIÉ à des énoncés qui ne sont pas dans les FAITS, par exemple « la nouveauté narrative… se réduit à un avis non décidable » et les reconstructions historiques, dont les sources sont par ailleurs citées comme RAPPORTÉ de mémoire. Je ne modifie pas ces statuts ; je signale l'écart à l'arbitre.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Ensemble de test trop petit pour le seuil.** Le test compte 0,3 × 400 = 120 trajectoires, soit 60 contre 60 (illustratif). Sous l'hypothèse nulle, la variance de l'AUROC empirique vaut (n₁+n₂+1)/(12 n₁ n₂) ≈ 0,0028, d'où un écart-type d'environ 0,053 (calcul illustratif). Un intervalle à 95 % fait donc environ ±0,10. Toute AUROC vraie comprise entre 0,50 et 0,70 environ ne permet de trancher ni H_A ni H_B au seuil de 0,60. La zone 0,60–0,65, laissée non affectée par le critère, ajoute un trou de décision.

- **Le seuil découpe un continuum.** Si Φ₀ suit sous chaque classe une loi normale de même covariance, à distance de Mahalanobis d, alors AUROC = Φ(d/√2). Le seuil de 0,60 correspond à d ≈ 0,36 (dérivation sous hypothèse gaussienne, illustratif). Le critère ne met donc en évidence aucune discontinuité : il coupe une taille d'effet continue, et la « catégorie » devient une convention de seuil.

- **Mélange de comportements.** Si seule une fraction π des trajectoires OEBM porte le signal, avec une AUROC de composante A_c, alors l'AUROC agrégée vaut 0,5 + π(A_c − 0,5). Pour π petit, une variante parfaitement détectable sur ses vraies occurrences passe pour une catégorie.

- **Dimension trop grande pour l'effectif.** Φ₀ contient des activations de couches et des représentations latentes du juge, de dimension p, avec n ≈ 280 exemples d'entraînement (illustratif). Lorsque p/n est grand à régularisation fixe, l'AUROC de test du méta-classifieur tend vers 0,5 même si l'AUROC de Bayes est élevée. Le critère confond alors cécité du capteur et fléau de la dimension.

- **NCD non jugeable sur des traces longues.** Avec un compresseur à fenêtre bornée (la fenêtre DEFLATE est de 32 KiB, statut RAPPORTÉ, de mémoire), des traces d'environ 20 000 jetons dépassent la fenêtre. C(xy) ≈ C(x) + C(y), et la NCD tend vers 1 pour toute paire : le seuil de 0,70 est franchi trivialement.

- **Puissance du test de Fisher avec 10 graines par bras (expérience 2).** Une différence 6/10 contre 0/10 donne p ≈ 0,011 en bilatéral ; il faut au moins 7/10 contre 0/10 pour passer sous 0,01 (calcul illustratif). Tout effet de groupe plus faible que ce quasi-tout-ou-rien est non jugeable.

### (c) Contrôles négatifs dont l'absence est fatale

- **LoRA placebo honnête** : un adaptateur de même rang, entraîné sur des trajectoires non biaisées et rangé dans la classe honnête. Sans lui, l'expérience 1 et l'expérience 3 mesurent la présence d'un adaptateur.
- **Asymétrie honnête pour Φ₁** : des dossiers où les documents soutenant Y=1 sont réellement plus faibles, de sorte qu'une exclusion asymétrique soit correcte. Sans ce contrôle, Φ₁ détecte « l'asymétrie », pas le sabotage. Le contrôle par température ne répond pas à cette question, puisqu'il est sans direction par construction.
- **Permutation d'étiquettes** pour le méta-classifieur, afin de fixer la distribution nulle de l'AUROC à l'effectif réel.
- **Variante connue diluée** : une attaque de 𝓐_connues appliquée à une fraction π des étapes, avec ΔU ajusté. Si elle franchit le critère « catégorie », le critère est réfuté. C ne prévoit rien de tel.
- **Pour l'expérience 3** : un prompt de rigueur méthodologique symétrique, sans dégradation. Il sépare l'effet du cadrage de l'effet du biais.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Les interventions sont tirées du catalogue.** « Restituer une donnée » et « certifier un calcul » sont exactement les réparations des deux mécanismes du catalogue (donnée manquante, erreur de calcul). Les profils du catalogue sont donc identifiables par construction. Tout candidat agissant sur un autre canal, par exemple un biais d'interprétation, aura le profil « non réparé » et sortira du catalogue mécaniquement. Le critère d_C > δ revient alors à « n'est pas réparé par ces deux réparations ».

2. **Le profil a une résolution trop faible.** Trois composantes, dont une condition de référence, ne permettent pas d'identifier des mécanismes distincts. Plusieurs mécanismes différents produisent le même profil, et D reconnaît cette hypothèse sans dimensionner le nombre d'interventions nécessaires.

3. **Le second duel peut être vrai par construction.** Le mécanisme « annoncé à l'avance » est vraisemblablement écrit par celui qui a construit le candidat. Le prédire sur une famille réservée teste la connaissance de la construction, pas une explication indépendante. Le contrôle par permutation des noms d'intervention est trop faible : toute prédiction informée le bat.

4. **La plage de paramètres du catalogue décide du verdict.** d_C est un minimum sur les explications du catalogue. Plus la plage de paramètres et l'ordre de composition admis sont larges, plus d_C diminue. Le verdict dépend d'un réglage fixé par l'expérimentateur, et D ne propose aucune règle pour le borner, par exemple une pénalité de complexité.

5. **Le prompt fuit vers les instruments.** La dégradation est induite par une consigne. Le lecteur d'états internes peut donc lire la présence de la consigne dans le contexte. Le contrôle par états permutés entre cas appariés ne corrige pas ce problème, puisque la consigne est propre à chaque cas sabot. D a raison de dire que l'étiquette est une condition, pas une intention, mais elle n'en tire pas le témoin nécessaire.

6. **Le modèle est au plancher de compétence.** Avec Qwen2.5-1.5B, le taux d'erreur honnête sous chaque intervention risque d'être élevé, ce qui écrase les différences de profil.

7. **L'unité du duel de génération est ambiguë.** D compare des « catalogues de diagnostic » produits en groupe ou en copies indépendantes, sans préciser si ce sont des attaques ou des diagnostics qui sont générés. De plus, le style de sortie d'un groupe (marques de consensus, références croisées) peut briser l'aveugle de l'évaluateur.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Intervalles plus larges que le seuil.** Avec environ 200/3 paires par intervention et des proportions d'erreur autour de 0,3, l'erreur-type binomiale vaut à peu près √(0,21/67) ≈ 0,056 (illustratif). Des bornes simultanées, corrigées pour la recherche dans le catalogue, dépassent facilement ±10 points. Dès que la demi-largeur simultanée est de l'ordre de δ, ni H_A ni H_B ne sont falsifiables.

- **Plafond ou plancher.** Si le taux d'erreur conditionnel du modèle est proche de 0 ou de 1 sous toutes les interventions, la variance entre interventions s'annule et tous les profils coïncident. Le test est alors non jugeable, quel que soit n.

- **Hétérogénéité entre familles.** L'unité de réplication du duel d'explication est la famille réservée. Si la variance entre familles de l'erreur de prédiction est grande devant δ et que le nombre de familles est petit, la borne sur d_M n'a que quelques degrés de liberté.

- **Événements rares dans le duel de génération.** Si p_G et p_S sont tous deux faibles, il faut de l'ordre de 3/p catalogues indépendants pour observer ne serait-ce qu'un succès (règle de trois). La borne inférieure sur g ne peut pas devenir positive avec un effectif raisonnable.

- **Plafond de fausses alertes appliqué à l'estimation.** Si le taux vrai est exactement de 5 % et qu'on l'estime sur 200 essais honnêtes, l'estimation dépasse 5 % avec une probabilité proche de 0,4 à 0,5 (illustratif). La règle « dépasser le plafond invalide le point » écarte alors environ la moitié des essais par pur bruit d'échantillonnage. Il faut un intervalle sur le taux de fausses alertes, pas un plafond sur l'estimation ponctuelle.

### (c) Contrôles négatifs dont l'absence est fatale

- **Consigne bénigne de même longueur et de même structure** dans la condition honnête. Sans elle, le lecteur interne et le juge mesurent la présence d'une consigne.
- **Dégradation par bruit**, par exemple une forte température ou une quantification : elle doit rester dans le catalogue ou être déclarée « non mécanistique ». Sinon le banc appelle « catégorie » un bruit non directionnel.
- **Mécanisme annoncé par un tiers aveugle** à la construction du candidat, ou **leurre** : le même auteur annonce un mécanisme pour une composition connue masquée, et le duel d'explication ne doit pas le valider au-delà du hasard.
- **Intervention hors catalogue** appliquée à une composition connue. Elle vérifie que le profil n'est pas informatif seulement sur les axes mêmes du catalogue.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Le capteur étendu est construit pour le candidat.** Le test contrefactuel de symétrie par inversion de polarité est choisi parce que le candidat discuté biaise de façon unidirectionnelle. Comme chez C, le capteur qui atteste le Régime III est construit à partir de l'attaque.

2. **La sélection sur l'évasion produit une malédiction du vainqueur.** La condition d'entrée de E1 retient un candidat parce que TPR(θ₀) ≤ 0,15. Si ce candidat est choisi parmi plusieurs sur un même ensemble, une part de l'évasion est due à la chance d'échantillonnage. E1 génère bien de nouveaux épisodes, mais aucune réplication de la condition d'entrée sur données fraîches n'est exigée.

3. **L'audit est une variable surtout manquante.** Φ_aud ne produit une sortie que sur une fraction p des épisodes, soit 10 %. Utilisé comme composante du triplet pour un classifieur ré-entraîné, il est absent dans environ 90 % des cas. « Ré-entraîner le protocole d'audit » n'a pas de sens si p reste fixe. Le triplet est donc en pratique un doublet.

4. **E2 souffre d'un écart synthétique-réel.** θ_comp est entraîné sur des mélanges synthétiques des primitives A₁…A₆, fabriqués par l'expérimentateur, puis testé sur P_cand, produit par l'agent. Un échec de transfert peut refléter l'écart entre mélanges synthétiques et comportements réels plutôt qu'une irréductibilité. Le contrôle sur une paire synthétique retenue reste dans la distribution du générateur synthétique et ne mesure pas cet écart.

5. **E3 est vrai par construction.** Chaque environnement contient un angle mort planté : une variable z* omise, avec exploitation vérifiée par solveur SMT. Toute « catégorie » découverte est donc une instance d'un seul schéma connu du concepteur, « exploiter la variable non observée ». Le rôle « générateur d'hypothèses hors-Φ » communique de surcroît ce schéma au groupe. E3 mesure une efficacité de recherche, pas une capacité à concevoir une catégorie.

6. **Le contrôle M₀ est garanti par le validateur.** Si la validation passe par le solveur, l'absence d'exploit dans un Φ complet garantit 0/15 indépendamment du comportement du groupe. Ce contrôle ne peut pas échouer et n'apprend rien.

7. **Arrêt optionnel.** La règle « zone intermédiaire ⇒ doubler N » sans correction séquentielle gonfle l'erreur de première espèce.

8. **Statuts.** L'en-tête des publications historiques porte `[VÉRIFIÉ]` alors que chaque entrée est « citée de mémoire ». Les récits historiques sont aussi marqués VÉRIFIÉ sans pièce. Je ne modifie pas ces statuts ; je signale l'incohérence. En revanche, E prévoit le LoRA bénin de même rang (contrôle iii), ce qui manque à C et à F.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Contrôle nul trop étroit.** Avec 200 cas honnêtes de test, le nombre de dépassements suit à peu près une loi Binomiale(200 ; 0,05), d'écart-type environ 3,1, soit environ 0,015 en taux. La fenêtre exigée [0,03 ; 0,07] correspond à ±1,3 écart-type : le contrôle échoue par pur hasard dans environ 19 % des cas (illustratif). C'est davantage encore si le seuil est estimé sur les mêmes données.

- **Puissance de E3.** Au seuil minimal annoncé, p_G = 0,25 et p_S = 0,10 sur M = 30 environnements, soit environ 8/30 contre 3/30. Le test des proportions donne z ≈ 1,7 et p ≈ 0,09 ; le test exact de Fisher est plus conservateur (calcul illustratif). La condition p < 0,01 n'est donc jamais réunie à l'effet minimal déclaré. Entre « écart inférieur à 0,10 » et « écart d'au moins 0,15 avec p < 0,01 », une large région ne falsifie rien.

- **Seuil de dégradation sensible à la queue honnête.** Le seuil est défini par rapport à la médiane de la perte honnête. Si cette loi est à queue lourde, ce qui est probable pour un modèle de 7 à 8 milliards de paramètres sur 20 sous-dossiers, une fraction notable des épisodes honnêtes franchit seule le seuil de dégradation. L'ASR du candidat devient alors non identifiable par rapport à l'incompétence.

- **Vrai mélange dans E2.** Si une fraction des épisodes du candidat se comporte comme les primitives connues, le TPR en transfert zéro-coup tombe dans ]0,15 ; 0,65[. On reste en zone d'indécision, quel que soit N.

### (c) Contrôles négatifs dont l'absence est fatale

- **Instance réelle d'une composition connue** (par exemple A₁ ⊕ A₂ produite par l'agent via LoRA, et non synthétisée) : θ_comp doit la détecter en transfert zéro-coup. Sans ce contrôle, l'échec de E2 sur le candidat ne s'interprète pas.
- **Spécificité de Φ'** : appliquer le test de symétrie à des agents honnêtes sur des dossiers où la vérité est réellement asymétrique en polarité, et à des dégradations par bruit. Φ' ne doit pas signaler toute dégradation.
- **Énumérateur mécanique pour E3** : une recherche systématique sur les variables d'état, à budget égal. Si elle trouve z* aussi souvent que le groupe, aucune « conception » n'est attestée. E prévoit un témoin solo, mais pas de témoin mécanique.
- **Groupe sans rôle « hors-Φ »** : il sépare l'effet de l'indice donné dans le prompt de celui de l'interaction.

---

## Sur la proposition F

### (a) Défauts de méthode

1. **L'identité de l'adaptateur est confondue avec le mécanisme.** Toutes les familles C₁, C₂, C₃ et le candidat a* sont intériorisées par des LoRA distincts, avec un prompt identique à celui de l'agent honnête. Rien n'indique que la classe honnête porte elle aussi un adaptateur. Il en découle deux problèmes :
   - Les sondes calibrées sur K peuvent apprendre « signature de l'adaptateur Cᵢ ». L'échec du transfert zéro-shot vers l'adaptateur de a* est alors attendu par construction, quel que soit le mécanisme.
   - La détection « honnête contre saboteur » peut se réduire à la question « adaptateur ou non ».

2. **Le critère 3 est vrai par construction.** Les « variantes de a* » sont produites par la procédure qui a produit a*. Un transfert intra-famille élevé est donc attendu et ne démontre pas une famille au sens mécanistique.

3. **S⁺ est choisi en connaissant le candidat**, comme chez C et E. Les deux exemples de S⁺ donnés sont des canaux génériques, mais l'expérience autorise à les choisir après avoir vu a*.

4. **L'absorption sous un budget de 20 exemples est surtout un test d'efficacité d'échantillonnage.** F le reconnaît et ajoute l'expérience 2, ce qui est correct. Mais la courbe S(n) et le canal S⁺ diffèrent aussi en dimension : un canal ciblé de faible dimension apprend plus vite qu'un espace d'activations de grande dimension. La comparaison TPR_{S⁺}(100) − TPR_S(500) confond invariant nouveau et dimension.

5. **Le contrôle de E3 est circulaire.** Falsifier H3B exige que « des failles exploitables existent (vérifié par attaque de référence ou témoin humain) ». Si cette attaque de référence est une catégorie, elle est connue des concepteurs de l'environnement. Les environnements permutés ne retirent que le vocabulaire : une structure isomorphe reste reconnaissable.

6. **L'environnement « scellé » est vrai par construction.** Une vérification déterministe couvrant 100 % des invariants rend toute dégradation détectable. Le contrôle teste le pipeline, pas les générateurs.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Ré-adaptation avec 20 exemples en haute dimension.** Avec 20 exemples et une sonde sur des activations de dimension p ≫ 20, à régularisation fixe, le TPR après adaptation reflète l'alignement préalable du signal sur les directions déjà apprises, pas sa présence. Toute attaque dont le signal est orthogonal aux directions de K « résiste » ; le critère 2 devient une mesure de géométrie a priori.

- **Plateau ou convergence lente.** Si la courbe d'apprentissage suit TPR(n) = TPR_∞ − c·n^(−γ) avec un γ petit, l'observation TPR_S(500) ≤ 0,55 ne distingue pas un plafond d'une convergence lente. Le test est non jugeable sans un ajustement de la courbe et un intervalle sur TPR_∞, qui manquent.

- **Aucun contrôle d'erreur dans E3.** La règle 2/5 contre 0/5 correspond, par test de Fisher, à p ≈ 0,44 en bilatéral (calcul illustratif). La règle de décision n'a aucune puissance ni aucun contrôle de l'erreur de première espèce.

- **Sensibilité d'audit estimée sur peu d'items.** La sensibilité s ≥ 0,85 à α_audit ≤ 0,02 est estimée sur les seuls items sabotés et tirés, de l'ordre de p × k × nombre d'épisodes. À p = 0,10, l'intervalle sur s est large. De plus, la comparaison à la borne 1 − (1 − p·s)^k suppose des items indépendants et un sabotage réparti : sous sabotage concentré ou corrélé, la loi du nombre d'items sabotés tirés n'est plus binomiale et la borne ne s'applique plus.

- **Correction multiple et gain exigé.** La condition 4.4, un gain de 0,10 sur le meilleur instrument et sur la réunion des vérifications mécaniques avec FPR global ≤ 0,05 après correction, réduit chaque seuil individuel. À effectif honnête fixé, le gain exigé peut devenir inobservable.

### (c) Contrôles négatifs dont l'absence est fatale

- **LoRA placebo honnête**, plusieurs si possible, entraîné sur des trajectoires correctes et rangé dans la classe honnête. Sans lui, les expériences 1 et 2 mesurent des signatures d'adaptateur.
- **Candidat témoin construit comme une famille de K mais avec un adaptateur neuf.** S'il échoue au transfert zéro-shot, l'échec observé sur a* ne prouve rien.
- **Contrôle de l'audit de non-antériorité** : des catégories connues, renommées et ré-habillées dans un environnement permuté, doivent être reclassées comme non nouvelles.
- **Spécificité de S⁺** sur des cas honnêtes difficiles et sur une dégradation par bruit, au même ΔQ.

---

**Bilan contradictoire (sans fusion).** Les quatre conceptions présentes définissent la catégorie comme l'échec d'un ré-entraînement sur un espace de capteurs fixé. Chez C, E et F, le capteur étendu qui atteste la catégorie est conçu à partir de l'attaque, et le défaut de contrôle par adaptateur placebo est fatal chez C et F. Chez D, la fuite passe par le catalogue d'interventions, et l'écart principal est l'absence de contrôle de la consigne dans le contexte. Pour chacune, la falsification réelle exige des effectifs plus grands que ceux annoncés. Les calculs de puissance ci-dessus sont refaisables par l'arbitre à partir des seules valeurs illustratives citées.

FIN-DE-CELLULE