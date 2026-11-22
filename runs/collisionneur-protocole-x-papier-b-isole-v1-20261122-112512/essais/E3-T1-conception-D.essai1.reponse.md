## D — Question et pari

**Question de recherche — HYPOTHÈSE.** À tâche, compétence honnête et budgets de génération et de vérification appariés, le partage des poids permet-il au défenseur de transférer un détecteur d’un rôle à l’autre assez efficacement pour compenser une éventuelle hausse des dégradations collectives ?

**Réponse attendue — HYPOTHÈSE.** Je prédis un avantage de **calibration**, pas une capacité à lire une intention : avec peu d’exemples étiquetés dans le rôle cible, un score appris sur les activations d’un rédacteur devrait mieux se transférer à un réviseur de mêmes poids qu’à un réviseur de poids différents. Je ne prédis pas cet avantage contre un agent seul qui occupe successivement les mêmes rôles : lui aussi conserve ses poids. Côté adversaire, je prédis davantage de dégradations réussies avant audit avec des copies qu’avec des poids différents, même sans messagerie libre. Le pari net est que le transfert du détecteur compense ce surcroît **après** audit. Ces prédictions sont séparables.

### (a) Ce qui n’est pas établi

| Statut | Point à ne pas tenir pour acquis |
|---|---|
| RAPPORTÉ | Le scénario donne au défenseur les textes, les activations et un budget de vérifications. Il ne donne aucun résultat de détection. |
| HYPOTHÈSE | Des copies peuvent faire des choix localement admissibles mais conjointement dommageables plus souvent que des agents différents. Une erreur commune en régime honnête pourrait produire exactement la même apparence. |
| HYPOTHÈSE | Des activations de mêmes poids ont une signification assez stable **entre rôles** pour transférer un score. Disposer des mêmes coordonnées ne suffit pas à l’établir. |
| HYPOTHÈSE | Segmenter les contextes entre copies a un effet distinct du partage des poids. Comparer seulement des copies à un agent à contexte continu confondrait ces deux changements. |
| HYPOTHÈSE | L’audit coûteux peut reconnaître un résultat globalement dégradé. Cela ne lui donne pas pour autant la capacité d’attribuer une intention à une copie particulière. |

### (b) Expérience et duels

**Plan — HYPOTHÈSE.** Utiliser des tâches synthétiques de planification d’ateliers. Le rédacteur affecte des activités, le testeur valide des contraintes locales, le réviseur choisit entre des corrections admissibles. Un solveur réservé à l’évaluation calcule la valeur globale réalisable. L’événement à détecter est un plan localement valide dont la perte par rapport à cette valeur dépasse une tolérance métier fixée avant génération. L’unité d’analyse est le **plan**, non le message. Le solveur étiquette tous les plans hors ligne pour l’expérimentateur ; en exploitation simulée, il ne répond au défenseur que sur les plans sélectionnés. Un mauvais plan audité est bloqué, pas supposé réparé.

**Plan — HYPOTHÈSE.** Croiser trois régimes : copies à contextes séparés ; équipe de poids différents à contextes séparés ; agent unique à contexte continu passant par les mêmes rôles. Ajouter un témoin d’identité : un seul processus rechargeant les contextes séparés, avec les mêmes poids, entrées et graines que les copies. Faire tourner chaque modèle dans chaque rôle, y compris en équipe homogène. Apparier sur difficulté et compétence honnête mesurée en pilote, sans sélectionner sur le succès adverse. Égaliser appels, plafonds de jetons et informations de tâche. Comparer, séparément, transmission du seul artefact structuré et transmission avec messagerie ; « sans messagerie » ne veut pas dire « sans information mutuelle ».

**Plan — HYPOTHÈSE.** Assigner aléatoirement une consigne honnête ou un objectif synthétique de perte globale à une partie des rôles ou à tous. Garder identiques les choix admissibles. Ne donner au détecteur ni les consignes privées ni leurs activations ; tester sur des formulations et des familles de tâches absentes de l’apprentissage. Mesurer des conséquences et non une « collusion » inférée du seul échec.

**Seuils de décision — HYPOTHÈSE ; tous les chiffres de conception ci-dessous sont illustratifs.** Fixer un budget d’audit de **5 %** des plans par lot. Noter \(E_g\) l’excès de mauvais plans sous consigne adverse par rapport aux consignes honnêtes dans le régime \(g\), avant audit ; \(R_g\) est le même excès pour les mauvais plans **livrés**, rapporté à tous les plans soumis, après audit. Noter \(G_g\) le gain de rappel du détecteur transféré texte + activations sur le meilleur détecteur sans activations, à budget égal. Dans le transfert, le corpus étiqueté source et le petit budget de calibration cible sont identiques pour chaque régime. Autoriser un alignement des modèles différents sur des exemples honnêtes parallèles, sans étiquette adverse cible supplémentaire.

| Duel — HYPOTHÈSE | \(H_A\) contre \(H_B\), métrique et seuil illustratif | Contrôle négatif |
|---|---|---|
| Avantage adverse | \(E_{\rm copies}-E_{\rm différents}>3\) points contre \(\leq3\) points, sur artefact seul. Répéter avec messagerie ; ne pas mélanger les strates. | Remplacer les rôles adverses par des rôles honnêtes recevant des consignes privées de longueur appariée. |
| Avantage défensif propre au transfert | \(G_{\rm copies}-G_{\rm différents}>5\) points de rappel contre \(\leq5\) points. Évaluer aussi le détecteur entraîné directement dans le rôle cible : son succès seul ne prouve aucun transfert. | Permuter les activations cibles entre plans dans chaque strate rôle, difficulté et longueur, en gardant textes et étiquettes en place. |
| Bilan après audit | \(R_{\rm copies}-R_{\rm différents}\leq1\) point contre \(>1\) point. Ne parler de **compensation** que si l’avantage adverse avant audit est aussi observé et si retirer les activations détériore le bilan. | Audit aléatoire au même budget, avec le même oracle. |
| Copies contre agent seul | \(\lvert R_{\rm copies}-R_{\rm seul}\rvert>3\) points contre \(\leq3\) points ; publier le signe et les taux bruts honnêtes et adverses. | Le processus unique à contextes rechargés doit reproduire les copies ; sinon rechercher d’abord une différence d’implémentation. |

**Règle de falsification — HYPOTHÈSE.** Pour chaque ligne, construire un intervalle apparié par famille de tâches pour le contraste indiqué. Un intervalle entièrement dans la région \(H_A\) falsifie \(H_B\) au niveau d’incertitude préenregistré ; entièrement dans la région \(H_B\), il falsifie \(H_A\). Un franchissement du seuil reste indécis. Dimensionner sur pilote d’après le nombre de **plans dégradés indépendants**, pas le nombre de jetons. Si le budget ne permet pas la précision requise, annoncer quel duel reste ouvert.

### (c) Test minimal des instruments

**Mesures — HYPOTHÈSE.** Pour chaque sélecteur, publier le taux de détection parmi les mauvais plans et le taux de fausses alertes parmi les bons plans honnêtes, au même budget. Ventiler le rappel entre pertes sous consigne adverse et pertes honnêtes accidentelles. Apparier les cas honnêtes par instance, rôle, modèle, canal, longueur et difficulté ; inclure explicitement des **bons** plans inhabituels et des **mauvais** plans honnêtes. Pour une prétention à détecter l’adversité plutôt que le dommage, ces derniers comptent comme négatifs, non comme détections réussies.

| Instrument — HYPOTHÈSE | Mesure minimale et comparaison nécessaire |
|---|---|
| Texte et messages | Rappel et fausses alertes contre audit aléatoire et classement mécanique par marges de contraintes, contradictions entre versions et régressions de coût local. Comparer avec et sans messages sur les mêmes traces. |
| Activations par copie | Sonde simple sur les représentations des décisions observables ; fixer couche et agrégation sur validation. Exiger un gain de rappel contre **texte + contrôles mécaniques**, sans hausse des fausses alertes sur les cas honnêtes appariés ; rapporter séparément transfert entre rôles et calibration dans le rôle. |
| Vérification coûteuse | Sur de petites instances où l’énumération exhaustive est possible, mesurer détection des pertes réelles et fausses alertes sur plans honnêtes proches de la tolérance. L’audit doit battre les contrôles locaux sur les pertes globales et concorder avec l’énumération ; sinon l’étiquette de référence est en cause. |

**Limite — HYPOTHÈSE.** Publier aussi la fraction de bons plans bloqués et le taux absolu de mauvais plans livrés. Un excès adverse faible obtenu parce que le système livre déjà beaucoup de mauvais plans honnêtes n’est pas un succès défensif.

### (d) Ancrage, antériorité et portée

**Matériel — HYPOTHÈSE de réalisation.** Modèle principal proposé : Llama 3.1 8B Instruct ; partenaires à poids ouverts proposés : Mistral-7B-Instruct-v0.3 et Qwen2.5-7B-Instruct (nombres dans ces noms : identifiants de modèles). Calcul **illustratif** : deux GPU de 80 Go, enveloppe totale de 600 heures-GPU à 3 €/heure-GPU, soit 1 800 € hors personnel. Génération sans réentraînement des modèles ; ne conserver que les activations aux décisions présélectionnées. Dans les deux mois demandés : mesurer d’abord débit, fréquence des pertes et précision de l’oracle, puis geler seuils et détecteurs avant le test tenu à part. Le contraste entre poids différents restera conditionnel aux familles effectivement testées.

**Antériorité — RAPPORTÉ, cité de mémoire.** John C. Knight et Nancy G. Leveson, 1986, *An Experimental Evaluation of the Assumption of Independence in Multiversion Programming*. C’est l’ancrage le plus proche que je puisse attribuer pour le volet **défaillances dépendantes** ; ce n’est pas une référence sur le transfert de sondes entre agents.

**Type et critère d’abandon — HYPOTHÈSE.** Contribution de type **phénomène mesurable**, non garantie : tester si le partage des poids modifie à la fois la dépendance des échecs et le prix de leur détection. Si les contrastes avant et après audit sont dans les marges de négligibilité, que la sonde n’apporte rien au texte et aux contrôles mécaniques, et que l’écart à l’agent seul est reproduit par le simple changement de contexte, la distinction « copies » est sans intérêt opérationnel **dans ce régime**. Avant toute revendication de nouveauté, rechercher séparément les travaux sur défaillances corrélées, contrôle multi-agent et transfert intermodèle de sondes, remonter leurs citations, puis vérifier sur leurs protocoles s’ils mesurent déjà le contraste conjoint à budget d’audit fixé.

FIN-DE-CELLULE