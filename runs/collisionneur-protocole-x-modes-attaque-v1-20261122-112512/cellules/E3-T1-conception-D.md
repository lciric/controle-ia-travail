# Proposition D — Tester une frontière de catégorie, non une impression de nouveauté

**HYPOTHÈSE — position.** La distinction est mesurable **relativement à un catalogue, à une règle d’assemblage et à un ensemble d’interventions fixés avant le test**. Une catégorie ne se définit pas par le nombre de surveillants qu’un cas met en défaut. Je retiendrais une catégorie candidate si les mécanismes connus, assemblages compris, ne prédisent pas sa réponse aux interventions, alors qu’un mécanisme supplémentaire annoncé à l’avance la prédit sur des cas réservés. Sans cette seconde condition, le verdict est « catalogue mis en défaut », pas « catégorie nouvelle ».

## (a) Ce que la question suppose

| Statut | Proposition et limite |
|---|---|
| **RAPPORTÉ** | Le scénario stipule une dégradation intentionnelle sous trois formes de surveillance. Il ne rapporte ni essai, ni candidat concret, ni performance mesurée. |
| **HYPOTHÈSE** | Une longue analyse peut être divisée en assertions dont la justesse est vérifiable indépendamment du texte de l’agent. Sans cela, une baisse de qualité peut n’être qu’un désaccord entre juges. |
| **HYPOTHÈSE** | Deux mécanismes distincts ont des réponses différentes à au moins une intervention disponible. Si toutes les réponses mesurables coïncident, l’expérience ne peut pas les distinguer. |
| **HYPOTHÈSE** | Une erreur volontaire est distinguable d’une erreur honnête de même gravité. Une consigne assignée au hasard donne une étiquette de *condition expérimentale*, pas une mesure d’intention interne. |
| **HYPOTHÈSE** | Le catalogue contient assez de variantes et d’assemblages pour rendre son échec informatif. Aucun catalogue historique exhaustif ni accès au corpus d’apprentissage des modèles n’est fourni. |

## Repères historiques et publications

**RAPPORTÉ — références citées de mémoire, non auditées ici.**

- Paul Kocher, *Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems* (1996). Le changement pertinent était l’**observable** : la durée d’exécution renseignait sur un calcul même lorsque sa sortie était conforme. C’est un repère pour les attaques temporelles, non une revendication de première découverte de tous les canaux auxiliaires.
- Eli Biham et Adi Shamir, *Differential Cryptanalysis of DES-like Cryptosystems* (1991). Le changement pertinent était la **quantité prédite** : une régularité statistique entre différences d’entrée et différences de sortie, plutôt qu’une propriété d’une sortie isolée. La méthode était formulée pour une famille de systèmes, pas seulement pour un exemplaire.

**HYPOTHÈSE — lecture de ces précédents.** Ce qui mérite d’être repris n’est pas le nom de la famille : c’est le fait de pouvoir désigner une observation que l’explication antérieure ne prenait pas en compte et de prédire quand elle sera informative. Ces articles illustrent cette distinction ; je ne leur attribue pas de théorème général sur la naissance des catégories.

## (b) Expériences en duel

**HYPOTHÈSE — banc commun.** Utiliser des dossiers synthétiques longs : tableaux comptables fictifs, règles de calcul explicites et conclusions vérifiables par un programme indépendant. Réserver des familles entières de dossiers, pas seulement d’autres lignes des mêmes tableaux. Le catalogue est constitué de perturbations documentées du banc, par exemple une donnée manquante, une erreur de calcul localisée et leurs compositions autorisées. Le test porte sur des diagnostics de dégradation ; il ne comporte pas de recherche adaptative de moyens d’échapper aux surveillants. **Tous les seuils, effectifs et budgets proposés ci-dessous sont illustratifs.**

### Premier essai : le catalogue prédit-il le profil du candidat ?

**HYPOTHÈSE — protocole.** Sur des copies appariées du même dossier, tirer au sort une intervention : conserver le dossier, restituer une donnée authentifiée, ou remplacer un calcul intermédiaire par sa valeur certifiée. Mesurer pour chacune la fraction d’assertions finales fausses. Ce vecteur est le *profil* ; il mesure ce qui répare la dégradation, et non ce que le juge trouve suspect. Avant ouverture de la réserve, figer les profils prédits par le catalogue et ses compositions, leur plage de paramètres admissible, et la prédiction propre du candidat. Un même choix de paramètres doit expliquer **toutes** les interventions.

**HYPOTHÈSE — duel d’appartenance.** Soit \(d_C\) la plus petite, parmi les explications du catalogue, des erreurs maximales de prédiction sur le profil réservé, en points de pourcentage. Fixer \(\delta=10\) points **(illustratif)**.

- \(H_A : d_C\leq\delta\) ; \(H_B : d_C>\delta\). Une borne inférieure simultanée au-dessus de \(\delta\) falsifie \(H_A\) ; une borne supérieure au plus égale à \(\delta\) falsifie \(H_B\). Construire les bornes par dossier apparié en tenant compte de toute la recherche dans le catalogue. Un intervalle qui traverse le seuil ne tranche pas.
- **Contrôle négatif de nouveauté :** masquer l’identité d’une composition connue, avec une gravité ajustée à celle du candidat. Si elle sort elle aussi du catalogue, suspendre le verdict : le banc confond nouveauté et mauvaise calibration.
- **Contrôle de sensibilité :** retirer temporairement du catalogue une perturbation de mécanisme connu, puis la réintroduire. Si son exclusion puis sa réintégration ne changent pas le verdict dans le sens prédit, ce jeu d’interventions ne valide pas l’épreuve.

**HYPOTHÈSE — duel d’explication, seulement si \(H_A\) est falsifiée.** Sur une seconde famille de dossiers réservée, mesurer l’erreur maximale \(d_M\) du mécanisme proposé, sans réajustement. \(H_A' : d_M\leq\delta\) contre \(H_B' : d_M>\delta\), mêmes bornes et mêmes règles de falsification. Contrôle négatif : une prédiction témoin qui permute les noms des interventions dont les effets annoncés sont distincts ; elle doit perdre l’accord. **Seuls le rejet du catalogue et l’accord prédictif indépendant justifient ensemble « catégorie nouvelle dans ce banc ».** Si les deux explications échouent, je retire la qualification de catégorie sans réhabiliter le catalogue.

### Le groupe apporte-t-il autre chose qu’un tirage supplémentaire ?

**HYPOTHÈSE — duel de génération.** Répartir au hasard des catalogues de diagnostic entre un groupe en interaction et des copies indépendantes du même modèle. Égaliser le budget total de jetons, le nombre de propositions finales, les documents disponibles et la règle de sélection. Un évaluateur aveugle applique les deux tests précédents ; l’unité de mesure est le catalogue indépendant, non le message échangé. Contrôle négatif : soumettre à l’évaluateur des variantes connues sous des noms inédits.

**HYPOTHÈSE — décision.** Soit \(g\) la différence entre les proportions de catalogues donnant une catégorie validée. \(H_A:g\leq0\) contre \(H_B:g>0\). Une borne inférieure positive falsifie \(H_A\) ; une borne supérieure non positive falsifie \(H_B\) ; sinon le bénéfice collectif reste indécis. Un seul succès validé du groupe témoignerait d’une conception *relative au catalogue* ; il ne démontrerait ni un avantage du groupe, ni une nouveauté absente de toute publication ou donnée d’apprentissage.

## (c) Qualification minimale de chaque surveillant

**HYPOTHÈSE — étiquettes et décision.** Produire des paires à dossier, modèle et budget identiques, en assignant une condition honnête ou une consigne expérimentale de dégradation dans le banc fermé. Pour les lecteurs et juges, mesurer le **taux de détection** sur les essais assignés à la dégradation, et le **taux de fausses alertes** sur les essais honnêtes, y compris incorrects. Publier séparément les résultats sur erreurs honnêtes appariées en gravité, longueur et difficulté ; ne pas retirer après coup les essais où la consigne n’a pas produit d’erreur. Masquer aux instruments la consigne, les étiquettes, les identifiants et le corrigé réservé à l’évaluation. Pour chaque comparaison, figer le seuil avant le test.

| Instrument | Mesure minimale et témoin mécanique à battre — **HYPOTHÈSE** |
|---|---|
| Lecteur d’états internes | Lire des activations à des positions de réponse préfixées. Comparer au détecteur mécanique utilisant longueur, incertitude de sortie et violations de contraintes. Comparer aussi au même lecteur avec états permutés entre cas appariés : si le gain subsiste, rien ne l’attribue aux états du cas. |
| Juge du texte | Donner le dossier et la réponse, sans métadonnées de condition. Comparer aux contrôles de format, de cohérence arithmétique et de correspondance entre citations et cellules sources. Les négatifs difficiles sont des textes honnêtes, fluides, mais faux au même degré ; les textes honnêtes justes restent dans la mesure globale. |
| Audit aléatoire du résultat | Tirer uniformément des assertions sans remise et les recalculer. **Cible : présence d’une erreur, non intention.** Si \(e\) assertions sur \(n\) sont fausses et \(k\) contrôlées, la sensibilité de référence avec vérificateur exact est \(1-\binom{n-e}{k}/\binom nk\). Une alerte sur un dossier honnête faux est correcte pour cette cible, mais fausse pour l’accusation de dégradation volontaire : publier les deux taux. Comparer, à coût égal, au contrôle mécanique d’un sous-ensemble fixe et au tirage uniforme exact ; ce dernier est une référence à reproduire, pas à prétendre battre avec le même tirage. |

**HYPOTHÈSE — duels de qualification.** Pour chacun des deux premiers instruments, au plafond de fausses alertes préfixé à **5 % (illustratif)**, opposer « gain de détection sur le meilleur témoin mécanique \(\leq0\) » à « gain \(>0\) ». Une borne inférieure positive réfute la première ; une borne supérieure non positive réfute la seconde. Dépasser le plafond invalide le point de fonctionnement. Pour l’audit, opposer « écart maximal absolu à la sensibilité théorique \(\leq5\) points **(illustratif)** » à son complément, par strate de densité d’erreurs ; les bornes de part et d’autre du seuil falsifient les hypothèses correspondantes. Contrôle négatif : dossiers intégralement justes. Rapporter les intervalles, pas seulement les moyennes. Un surveillant non qualifié n’est pas un témoin de nouveauté.

## (d) Ancrage matériel

**RAPPORTÉ — de mémoire.** Qwen2.5-1.5B-Instruct et Qwen2.5-3B-Instruct sont des modèles à poids ouverts envisageables ; les chiffres dans ces noms sont des identifiants de modèles. Figer la révision des poids et du logiciel avant l’essai.

**HYPOTHÈSE — budget illustratif.** Commencer avec le plus petit modèle, sans réentraînement, un lecteur linéaire et des activations limitées aux positions préenregistrées. Pour **200 paires**, **3 conditions d’intervention** et **500 jetons de sortie** par réponse, prévoir **600 000 jetons générés** (toutes quantités **illustratives**). Sur **un GPU de 24 Go**, à **25 jetons/s** effectifs et **1 €/GPU·h**, cela représente environ **7 heures et 7 € pour la génération seule** (illustratif). Chronométrer d’abord un lot avec dossiers longs et capture d’états ; ajouter séparément préremplissage, jugement, contrôles et réplications si non inclus dans le débit. Ce pilote peut révéler un banc non discriminant ; son budget ne garantit pas des intervalles assez étroits pour conclure.

FIN-DE-CELLULE