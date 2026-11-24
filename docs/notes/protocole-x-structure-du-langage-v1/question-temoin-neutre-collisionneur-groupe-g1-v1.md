# Question (bras témoin neutre)

On étudie comment concevoir et évaluer rigoureusement un système automatisé d'idéation scientifique destiné à proposer des hypothèses testables, des rapprochements entre domaines, des clarifications conceptuelles et des outils mathématiques utiles notamment au contrôle boîte blanche de modèles ouverts, sous fortes contraintes de ressources de calcul et d'étanchéité expérimentale.

Ne fais pas une réponse plus longue, fais-la plus profonde. À partir des faits établis et des controverses ouvertes exposés dans le dossier, détermine quels mécanismes de découverte automatisée sont solides, lesquels reposent sur des analogies fragiles ou des artefacts statistiques, et quelles expériences décisives mener en priorité sur processeur seul avant tout déploiement coûteux.

Réponds en respectant exactement les points ci-dessous :

1. **Analyse d'expert.** Ce qu'un spécialiste de la découverte scientifique computationnelle, de l'apprentissage statistique et du contrôle des systèmes intelligents examinerait d'abord ici, sans que la question le demande.
2. **Données brutes de départ** à privilégier avant toute représentation pré-agrégée ou pré-entraînée.
3. **Démarcation théorique et risques méthodologiques.** Quelles structures ou régularités du réel peuvent ou ne peuvent pas être inférées de corpus textuels, d'équations et de graphes datés ; comment évaluer la solidité formelle des hypothèses portant sur l'alignement inter-domaines, la séparation de concepts confondus, les dynamiques d'émergence sur graphes finis et la création de nouvelles abstractions ; et quels biais (fréquence, échelle, survivant, sondes mémorisantes, fuites temporelles, circularité) menacent chaque approche ?
4. **Méthodes, outils et protocoles de validation.** Quelles familles de méthodes concrètes et quels protocoles d'évaluation hors modèle employer pour tester ces mécanismes et en tirer des instruments utiles au contrôle boîte blanche (détection séquentielle, robustesse des sondes et audit des poids) ?
5. **Vérification indépendante.** Ce qui, en dehors des concepteurs du projet, permettrait de vérifier que les conclusions et les gains mesurés tiennent réellement.
6. **Reformulation exigeante du problème** intégrant les points précédents.
7. **Programme d'actions prioritaires classé** selon la formule :
   `score = (gain_informatif × facilité × portée × potentiel_de_découverte_majeure) / coût`
   (chaque critère noté de 1 à 5, avec 1 = coût minimal sur processeur seul et 5 = lourd en calcul ou évaluation humaine). Pour chacune des six premières actions retenues : formule une expérience décisive falsifiable opposant deux hypothèses exclusives `H_A` contre `H_B`, avec sa métrique, son seuil, son contrôle négatif explicite, son premier pas sur processeur seul, son coût estimé (marqué « illustratif » s'il n'est pas issu des faits) et l'issue qui réfuterait chaque hypothèse. Indique enfin les limites qui subsistent.

Règles : n'invente aucun chiffre ni aucune référence ; cite les travaux par leur titre, et par leur identifiant arXiv si tu le connais, « pas sûr » sinon ; distingue ce qui est établi de ce qui est ta proposition ; dis « je ne sais pas » quand c'est le cas ; aucune recette d'attaque applicable.
