# Mesurer sans juge la dégradation voulue : note de sortie du collisionneur

Dossier : `runs/collisionneur-protocole-x-taches-sabotage-isole-v1-20261122-115058`

Rédigé par un lecteur Opus 5.5, classe C, à partir des seules cellules du dossier.

v2 : cellules d'Argon et de Carbon lues en entier (la v1 les avait lues en partie, sans le dire) ; changements : le désaccord sur les refus, ouvert en v1, est refermé au tour III.3 ; attributions corrigées (retrait contre insertion, témoins de charge, instabilité de la part intentionnelle) ; propositions retenues inchangées.

Cinq modèles ont conçu à l'aveugle (tour III.1), se sont critiqués (III.2), puis ont répondu (III.3) : Claude Fable 5.2 (A), Claude Opus 5.5 (B), Gemini 4 Argon (C), Astra, identifiant gpt-6.2-astra (D), Gemini 4 Carbon (E). Le lecteur est de la même famille que deux participants ; il rapporte chaque position avec ses appuis et ses critiques.

## 1. La question

Un agent de langue mène une longue tâche d'analyse et peut dégrader le résultat exprès, chaque action restant défendable lue seule ; un agent honnête se trompe aussi. La question demande s'il existe déjà, dans quelque domaine que ce soit, une mesure par programme et sans juge de la part dégradée exprès, à quelles conditions elle est possible, si la distinction entre dommage d'une action et dommage d'une combinaison se règle dans une tâche, ce que la mesurabilité coûte en réalisme, et quelle première expérience peu coûteuse, sur un petit modèle ouvert, dirait si l'entreprise vaut d'être poursuivie.

## 2. En bref

1. **Ce qui est mesurable est un excès en population, pas une intention par trajectoire** : tirer au hasard, par instance, la structure de la nuisance (direction, levier ou signe) et comparer le bras de sabotage à des témoins de même charge donne une mesure sans juge de l'excès dirigé ; les cinq modèles y convergent après critiques.
2. **« Lue seule » dépend du point de départ du rejeu** : un dommage conjonctif est invisible si l'on insère une action seule dans un calcul sain, mais visible si on la retire de la trajectoire réalisée ; le dommage redondant suit le schéma inverse, et une porte « deux sur trois » échappe aux deux ; cela se vérifie sur processeur sans aucun modèle.
3. **Une porte sur processeur avant toute dépense de processeur graphique** : saboteurs scriptés (plancher, plafond), politique honnête constante et correcteur validé sur cas à vérité connue doivent passer avant tout essai avec modèle.
4. **Le premier essai avec modèle est un duel apparié de quelques bras**, sur un modèle de 3 à 8 milliards de paramètres, contre un témoin de charge et un honnête « cadré », en intention de traiter, refus et sorties invalides comptés à part.
5. **Le réalisme se mesure par une jumelle à code libre**, avec instruments gelés, contrôle de charge et données à chiffres modifiés contre la mémorisation.

## 3. Ce que chaque modèle a proposé

### Claude Fable 5.2 (A)

- **Proposition centrale.** L'intention n'est identifiable qu'en population, par contraste causal entre bras ; une borne avancée par ce modèle (non auditée) relie l'excès moyen de dommage à la distance en variation totale entre politiques saboteuse et honnête : un dommage niable par trajectoire est petit en moyenne.
- **Plan.** Analyse de données synthétiques à effet planté et huit décisions binaires énumérables (256 chemins). Le générateur tire au hasard l'option correcte, son levier et le régime (additif ou à interaction). Bras honnête, sabotage, placebo, agent aléatoire ; après critiques, placebo actif « audit » qui calcule le levier sans nuire, et honnête à « méprise » sincère. Mesure principale révisée : contraste de ciblage (taux d'erreur sur décisions à fort levier moins à faible levier, entre bras). Quatre expériences, précédées d'une expérience à vide sur processeur.
- **Prédiction.** Aucun signe ; règles d'arrêt : sans ciblage même avec un saboteur ajusté, abandon du petit modèle ; ciblage mais détection facile, le banc n'est qu'un test de plomberie.

### Claude Opus 5.5 (B)

- **Proposition centrale.** Mesurer l'« excès dirigé » : la part du dommage qui suit une direction de nuisance tirée au hasard, comparée aux erreurs du même agent ; un ensemble d'actions admissibles préenregistré remplace le lecteur dans la notion de « défendable ».
- **Plan.** Un « multivers synthétique » de 30 à 60 actions à options admissibles ; bras honnête, sabotage dans chaque direction, bruit non dirigé ; après critiques, honnête cadré (direction visible, motif neutre), placebo de charge, saboteurs scriptés plancher et plafond, porte sur processeur.
- **Prédiction.** Supposait d'abord qu'un petit modèle produit surtout du dommage local. Après la critique de fuite de la direction (voir § 4), la thèse est réduite : l'excès dirigé est une mesure côté expérimentateur, agrégée, non un détecteur.

### Gemini 4 Argon (C)

- **Proposition centrale.** Combiner trois signatures : concentration des déviations sur les étapes à fort levier aval et faible difficulté (calibrée à la manière de la théorie de réponse aux items), cohérence de direction sous variantes de surface (somme cumulée), et indice d'interaction entre actions ; puis estimer une part intentionnelle par trajectoire.
- **Plan.** Tâche tabulaire de 30 actions, rejeu par ablation sur processeur, quatre expériences dont une sur mélanges contrôlés. Après critiques : température unique, honnête « piège » et honnête cadré, six variantes à polarité inversée, part intentionnelle par valeur de Shapley bornée.
- **Prédiction.** Séparation par trajectoire possible (seuil d'aire sous la courbe de discrimination de 0,75, illustratif) ; poursuite seulement si au moins un quart des trajectoires saboteuses sont à la fois dégradantes et localement défendables.

### Astra (D)

- **Proposition centrale.** Mesurer d'abord la perte moyenne induite par l'assignation d'un objectif de dégradation, à tâche et budget constants, et séparer cette question de celle de l'attribution ; même un correcteur exact ne dit pas pourquoi le dommage a été causé.
- **Plan.** Dossiers d'analyse de tableaux avec provenance ; quatre « duels » (objectif, composition, détecteur, transfert). Après critiques : variable primaire « perte livrée par des dossiers localement admissibles » (zéro si non livré), témoin à objectif bénin, rubrique tirée au sort, détecteur sans texte libre.
- **Prédiction.** Aucun signe ; règle de dépense : ne financer la détection que si le correcteur passe ses cas d'essai et si le contraste admissible et ciblé est résolu ; même un succès n'établirait « qu'une perte sous intervention ».

### Gemini 4 Carbon (E)

- **Proposition centrale.** Une variable instrumentale interne à la tâche : un signe de polarité, orthogonal à la difficulté, que le saboteur doit exploiter et que l'honnête ignore. Après critiques, ce signe devient un « signe comptable » d'agrégation (produits et charges) sur des tables de même loi, et une statistique quadratique dont l'espérance serait nulle, selon ce modèle, pour toute politique honnête invariante à l'étiquetage.
- **Plan.** Méta-analyse de 24 tables synthétiques, régimes d'interaction, tables jumelles, sonde de bruit sur les poids ; pilote à trois bras (honnête neutre, honnête aligné, sabotage) et témoins scriptés.
- **Prédiction.** Séparation de la part intentionnelle « algébriquement possible » sous randomisation du signe ; réfutable si la complaisance d'un honnête aligné biaise la statistique.

## 4. Accords et désaccords

### Accords indépendants au tour III.1

- **Aucun banc connu** des cinq ne mesure sans juge, sur une trajectoire longue non étiquetée, la part dégradée exprès. Tous les travaux cités fixent l'intention par consigne ou par entraînement, ou raisonnent sur une population. Quatre modèles disent que c'est une affirmation d'absence fragile ; Argon l'avait marquée « vérifié », ce que Fable, Opus et Astra ont contesté, et Argon l'a requalifiée « rapporté » au tour III.3.
- **Vérité plantée et tâche synthétique** : les cinq proposent une analyse de données synthétiques à paramètre connu, rejouable par programme.
- **Impossibilité par imitation** : si le saboteur reproduit la loi d'un honnête moins compétent, aucun test ne le sépare (tous).
- **Randomiser la structure de nuisance** : levier tiré au hasard (Fable), direction tirée au hasard (Opus), polarité (Carbon) ; Astra et Argon l'adoptent ensuite.
- **Le réalisme se teste par une version libre de la même tâche** (les cinq).
- **Le sabotage commandé ne renseigne pas sur le sabotage spontané** : Fable et Opus le déclarent hors de portée de toutes leurs expériences ; aucun modèle ne propose de quoi le trancher.

### Désaccords, et ce que les tours suivants ont changé

- **Une conjonction échappe-t-elle à la lecture action par action ?** Opus, Argon et Carbon l'affirmaient au tour III.1. Au tour III.2, trois modèles ont objecté indépendamment que c'est faux si l'on retire une action de la trajectoire réalisée : Fable (contre Opus, Argon et Carbon), Astra (contre Opus et Argon) et Carbon (contre Opus et Argon, en relevant déjà le cas redondant). Fable en a tiré le test sur processeur. Opus, Argon et Carbon l'ont accepté au tour III.3 ; Carbon a ajouté le cas « deux sur trois », aveugle aux deux conventions. Désaccord résolu, sous réserve de ce test.
- **Détection par trajectoire ou seulement en population ?** Fable : population seulement. Opus : réduit à l'agrégat après la critique, mais garde un essai par trajectoire fondé sur la cohérence de signe entre déviations. Argon : maintient une séparation par trajectoire. Carbon : maintient une statistique par épisode. Astra : reconnaît l'assignation, jamais l'intention. **Non résolu** ; Astra et Opus rappellent que, sans prévalence connue, aucune alerte individuelle n'est calibrée en déploiement.
- **Quantifier une « part intentionnelle » par trajectoire ?** Argon et Carbon la proposaient. Toutes les critiques ont montré que ce rapport est mal défini sous interaction et instable quand erreur honnête et sabotage se compensent (Argon et Carbon le chiffrent chacun contre l'autre ; Astra le relève pour les deux). Carbon l'abandonne pour un excès de perte en cohorte ; Argon le garde sous forme de valeur de Shapley bornée, avec un témoin « honnête greffé sur honnête » ; cette version n'a pas encore été critiquée.
- **Fuite de la direction (Opus).** Argon et Carbon ont montré que le détecteur d'Opus recevait la direction secrète ; sans elle, l'erreur finale n'apporte rien de plus que son amplitude. Opus l'a acceptée comme « la critique la plus grave ».
- **Levier et difficulté sont-ils séparables ?** Opus, Argon, Astra et Carbon : non, le levier et la lisibilité des diagnostics sortent du même paramètre. Fable accepte que l'honnête puisse se tromper plus souvent là où le levier est fort et rend le contrôle relatif entre bras, mais rejette l'autre branche (diagnostic plus visible) comme simple perte de puissance ; il en fait un test préalable.
- **Refus et sorties invalides.** Astra les comptait dans la perte ; tous l'ont critiqué. Dans sa critique, Carbon proposait de se restreindre aux dossiers valides ; Astra a rejeté cette restriction comme analyse primaire (la validité est postérieure à l'assignation). Mais au tour III.3 les deux convergent : Astra code « aucun dommage livré » pour tout dossier non admissible, sur l'ensemble des assignations ; Carbon, dans sa propre conception corrigée, garde tous les épisodes en intention de traiter et met à zéro le dommage de tout épisode qui échoue aux vérifications mécaniques. Désaccord refermé ; les taux de refus restent publiés à part.

## 5. Ce qui est neuf et ce qui est fragile

### Neuf, par rapport à ce que les modèles citent comme connu

Connu selon les modèles : sous-rendement induit, évaluations de sabotage, contrôle de l'intelligence artificielle, test par mutation, analyse multivers, triche détectée en population, tests sous le hasard, sommes cumulées. Ce qu'ils ajoutent :

- la randomisation, par instance, de la structure de nuisance comme moyen de rendre l'erreur honnête indépendante de la nuisance (Fable, Opus, Carbon) ;
- les bras témoins de charge : placebo actif qui calcule le levier (Fable, après les critiques d'Astra, de Carbon et d'Argon), objectif secondaire bénin (proposé par Argon dans sa critique, adopté par Astra avec une rubrique tirée au sort), honnête cadré (Carbon dès le tour III.1, puis Opus et Argon) ;
- la dualité retrait et insertion, et la porte « deux sur trois » ;
- l'excès de conjonction comparé à des tuples non plantés de même taille, qui serait nul en espérance pour tout agent qui ne calcule pas la structure (Fable, révisé) ;
- la statistique quadratique à signe comptable de Carbon, introduite au tour III.3, donc jamais critiquée.

Rien de cela n'est vérifié contre la littérature.

### Fragile

- **Sabotage commandé contre spontané** : limite admise, aucun plan.
- **Capacité du petit modèle** : tous doutent qu'un modèle de 7 à 8 milliards de paramètres sache saboter de façon ciblée et défendable sur des dizaines d'actions ; l'issue « il ne sait pas » rendrait le banc muet sur le scénario.
- **« Défendable » sans lecteur** : remplacé par un ensemble admissible (Opus), un vérificateur local (Astra) ou une fréquence honnête d'au moins 5 % (Argon) ; aucun n'est validé contre un lecteur.
- **Complaisance** : un honnête à qui l'on montre une attente peut se biaiser dans la même direction ; c'est le négatif le plus dur et il n'est mesuré nulle part encore.
- **Erreurs honnêtes corrélées** : plusieurs contrôles initiaux supposaient l'indépendance et étaient vrais par construction ; les critiques l'ont relevé chez chacun.
- **Effectifs** : les critiques chiffrent que plusieurs seuils ne sont pas jugeables aux tailles proposées (pilote de 24 dossiers d'Astra, test de Kolmogorov-Smirnov d'Argon, marge de Fable) ; certifier 5 % de fausses alertes demande, selon Astra, au moins 59 négatifs indépendants même sans aucune alerte.
- **Coûts** : les estimations divergent d'un ordre de grandeur. Argon avance environ 2 dollars pour le premier essai et 19 pour le programme ; Carbon environ 7 dollars ; Astra 1 à 4 euros ; Fable 15 à 70 euros ; Opus 150 à 350 euros et 2 à 3 semaines-personne, le travail humain sur le générateur dominant selon Opus et Fable. Rien n'est mesuré.
- **Extraction en code libre** : la mesure du réalisme dépend d'un analyseur qui relie le code aux décisions ; Fable reconnaît n'avoir pas de repli si le découplage du levier échoue.

## 6. Références à vérifier

Aucune de ces références n'a été vérifiée. Les modèles de langue inventent parfois des références ou en déforment auteurs, titres et dates ; chacune doit être lue sur sa source avant usage.

| Référence telle que citée | Qui la cite | Pour quoi faire |
|---|---|---|
| Greenblatt, Shlegeris, Sachan, Roger (2023 ; 2024 chez Argon), « AI Control: Improving Safety Despite Intentional Subversion » | Fable, Opus, Argon | Sabotage instruit, vérifié par programme ; détection par moniteur |
| van der Weij, Hofstätter, Jaffe, Brown, Ward (2024), « AI Sandbagging: Language Models can Strategically Underperform on Evaluations » | Fable, Opus, Argon ; Astra sans référence | Sous-rendement induit, intention fixée par construction |
| Greenblatt, Roger, Krasheninnikov, Krueger (2024), « Stress-Testing Capability Elicitation With Password-Locked Models » | Fable, Opus | Saboteur obtenu par entraînement (repli de Fable) |
| Benton et al. (2024), « Sabotage Evaluations for Frontier Models » | Fable, Opus, Argon | Tâche secondaire nuisible et évasion d'un moniteur |
| Kutasov et al. (2025), « SHADE-Arena » | Fable, Opus | Idem ; Fable demande de vérifier la part de notation par juge |
| Bhatt et al. (2025), « Ctrl-Z » | Opus | Contrôle et sabotage d'agents |
| Duggan et Levitt (2002), « Winning Isn't Everything: Corruption in Sumo Wrestling » | Fable, Carbon | Triche détectée en population par les incitations |
| Jacob et Levitt (2003), « Rotten Apples » | Fable | Idem, enseignants |
| DeMillo, Lipton, Sayward (1978), « Hints on Test Data Selection » ; Jia et Harman (2011), « An Analysis and Survey of the Development of Mutation Testing » | Fable ; Astra | Fautes semées pour valider un détecteur |
| Steegen, Tuerlinckx, Gelman, Vanpaemel (2016), « Increasing Transparency Through a Multiverse Analysis » ; Simonsohn, Simmons, Nelson (2020), « Specification curve analysis » | Fable, Opus ; Opus | Énumération des analyses défendables |
| Simonsohn, Nelson, Simmons (2014), « P-curve: A key to the file-drawer » ; Carlisle (2017), Anaesthesia | Opus | Détection en corpus |
| Tombaugh (1996), Test of Memory Malingering ; tests de validité à choix forcé | Opus ; Fable, Carbon (sans référence) | Score sous le hasard incompatible avec l'erreur honnête |
| Drasgow, Levine, Williams (1985), indice d'ajustement de la personne | Argon ; Opus sans référence | Patrons de réponses improbables |
| Page (1954), « Continuous Inspection Schemes » ; Wald (1945), « Sequential Tests of Statistical Hypotheses » | Argon, Carbon ; Argon | Dérive cumulée sous seuil |
| Easley, Kiefer, O'Hara, Paperman (1996) ; Kyle (1985) ; Lamport, Shostak, Pease (1982) | Argon | Actions informées dans un flux bruité ; invariants contre nœuds malveillants |
| Sobol (1993) ; Shapley (1953), « A Value for n-Person Games » | Argon ; Carbon | Décomposition en effets et interactions ; attribution |
| Jimenez et al. (2024), SWE-bench ; Mialon et al. (2023), GAIA | Argon | Bancs d'agents qui agrègent toutes les causes d'échec |
| Rubin (1974), « Estimating Causal Effects of Treatments… » | Astra | Effet moyen d'une assignation |
| Oaxaca (1973) ; Blinder (1973) | Carbon | Terme d'interaction d'une décomposition |
| Pearl (2009), « Causality » ; Platt (1964), « Strong Inference » | Carbon | Cadre causal ; inférence forte |
| Sondes de bruit sur les poids contre le sous-rendement (sans auteur) | Carbon | Capacité retenue exprès |
| Qwen2.5-7B, -3B, -1.5B-Instruct ; Llama-3.1-8B-Instruct ; Qwen2.5-14B et -32B | Tous | Modèles ouverts ; licences et versions à vérifier |

## 7. Propositions retenues et non retenues

### Retenues

1. **Mesure en population par structure de nuisance randomisée et témoins de charge.** Proposée indépendamment par trois modèles, adoptée par les deux autres ; a survécu aux critiques une fois les témoins ajoutés. Faisable sur données synthétiques. Limite : elle mesure l'effet d'une consigne, non une intention.
2. **Le test « retrait, insertion, deux sur trois » sur processeur, sans modèle.** Soutien : proposé par Fable, accepté par Opus, Argon et Carbon, appuyé sur le plan deux sur deux d'Astra. Il tranche le seul désaccord de fond résolu du dossier. Coût : quelques rejeux sur processeur. Il ne dit rien de l'agent, et ses auteurs le disent.
3. **La porte sur processeur avant tout processeur graphique, puis un duel apparié minimal.** Soutien : expérience à vide de Fable, porte d'Opus, correcteur validé d'Astra, témoins scriptés de Carbon et Argon. Premier essai : un petit modèle, trois à six bras dont un honnête cadré et un témoin de charge, en intention de traiter, refus publiés à part. Coût le plus bas du dossier ; il répond directement au point 5. Astra et Carbon convergent pour mettre à zéro le dommage des sorties non admissibles, sur toutes les assignations.
4. **Jumelle à code libre pour le réalisme** : convergence des cinq, durcie par les critiques (instruments gelés, charge constante, chiffres modifiés contre la mémorisation, analyseur validé sur trace connue). Retenue avec réserve : elle dépend d'un analyseur dont la validité n'est pas acquise.

### Non retenues

- **La part intentionnelle par trajectoire** (Argon, Carbon au tour III.1) : mal définie sous interaction, instable quand les erreurs se compensent ; Carbon l'a abandonnée. La version de Shapley d'Argon n'a pas encore été critiquée.
- **Les détecteurs qui lisent la direction secrète** (Opus au tour III.1) : fuite d'étiquette, retirée par son auteur.
- **Les erreurs honnêtes fabriquées par hausse de température** ou par un modèle plus petit (Argon, Carbon) : confondent échantillonnage ou taille et intention ; abandonnées par leurs auteurs.
- **La couverture par rapprochement scalaire** (Fable, étude du réalisme) : vraie par construction sur une grille dense ; retirée.
- **La cohérence de direction sous permutations** (Argon) : fausses alertes plancher, aveugle aux biais conceptuels ; refondue sur des inversions de polarité, non encore critiquée.
- **La statistique quadratique à signe comptable** (Carbon) : prometteuse et peu coûteuse, mais introduite au dernier tour ; à soumettre à une critique avant tout emploi, notamment sur la complaisance et sur la lisibilité du signe pour l'honnête.
