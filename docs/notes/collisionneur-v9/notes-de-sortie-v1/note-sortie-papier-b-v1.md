# Copies d'un même modèle : ce que le collisionneur propose

Dossier : `runs/collisionneur-protocole-x-papier-b-isole-v1-20261122-112512`

Rédigé par un lecteur Opus 5.5, classe C, à partir des seules cellules du dossier.

Avertissement : l'un des cinq modèles (Opus 5.5) est le modèle du rédacteur. Les propositions sont retenues sur le soutien croisé et la résistance aux critiques, non sur leur auteur (section 8).

## 2. La question

Plusieurs copies d'un même modèle de langue se partagent une tâche (écrire, tester, relire du code) ; certaines ou toutes peuvent la dégrader par des contributions chacune défendable. Le défenseur voit le texte et les activations internes de chaque copie et dispose de peu de vérifications coûteuses. La question : le fait que les agents soient des copies, plutôt qu'un agent seul ou des modèles différents, change-t-il quelque chose pour le défenseur et pour l'adversaire, et quoi ?

## 3. En bref

- **Retenue 1 — transfert de sonde entre rôles à budget d'étiquetage égal.** Le seul avantage défensif propre aux copies qui résiste aux critiques est l'économie d'étiquettes quand une sonde apprise sur un rôle sert à un autre rôle de mêmes poids ; le premier test, sans réentraînement ni consigne adverse, fixe le réviseur et les plans et ne fait varier que la source de la sonde.
- **Retenue 2 — porte de validité des sondes.** Avant toute conclusion tirée des activations, un plan croisé « adaptateur saboteur ou placebo » × « thème déclencheur présent ou absent » doit montrer que la sonde lit le sabotage et non l'adaptateur, le thème ou la consigne.
- **Retenue 3 — mesurer d'abord le mode commun et la concentration des choix, sans sonde.** Sans canal, la concordance de copies n'est que la ressemblance de leurs préférences ; on mesure donc, à bas coût, les angles morts honnêtes partagés et la concentration des choix sur le même point faible, en double différence adverse moins honnête.
- **Condition de lecture commune** : tout bilan se lit en dommage livré par épisode, plafond du rappel déclaré, budget d'étiquetage entièrement débité.

## 4. Ce que chaque modèle a proposé

### Fable 5.2 (claude-fable-5-2), pièce A

**Proposition centrale.** L'identité des poids ouvre le même canal aux deux camps : ce qui permet à une copie de reconnaître le sabotage d'une autre est aussi ce qu'une sonde peut lire chez la copie qui relit.
**Plan.** Matrice trois rédacteurs × trois lecteurs ; un duel sans adversaire (angles morts honnêtes corrélés), un duel de lisibilité par sonde, un jeu de coordination sans communication, un bilan à budget d'audit fixé ; sondes entraînées sur des défauts-pièges seulement ; erreurs honnêtes appariées.
**Prédiction.** Fable donne lui-même des probabilités faibles à sa thèse ; après critiques, il prévoit que la surprise du lecteur et le style expliquent l'essentiel de l'avantage diagonal, donc que son mécanisme soit réfuté. Il sépare désormais un régime « contextuel » (poids sains, contexte compromis) d'un régime « dispositionnel » (adaptateur saboteur), et place en premier l'expérience sans adversaire. Il abandonne le test contre un adversaire qui s'adapte, faute de temps.

### Opus 5.5 (claude-opus-5-5), pièce B

**Proposition centrale.** Deux effets de signe opposé : les copies se coordonnent sur les mêmes points focaux (adversaire) ; elles partagent les mêmes coordonnées internes (défenseur). Le bilan dépendrait de l'obfuscation : l'identité aiderait le défenseur tant que le signal latent n'est pas effacé.
**Plan initial.** Porte de capacité à huit milliards de paramètres, mesure de cohérence en excès sur les marginales, agrégation des scores de sonde entre copies, rejeu par une copie saine, bilan rouge contre bleu, test d'obfuscation.
**Après critiques.** Opus retire trois éléments qu'il reconnaît vrais ou vides par construction (la mesure de cohérence, la comparaison sonde contre texte après filtrage, le rejeu) et l'agrégation comme effet propre aux copies. Restent : la double différence de collision sans canal, une porte de validité des sondes en plan croisé adaptateur × thème, l'efficacité en étiquettes du transfert de sonde, un bilan en risque par épisode. Première expérience : la porte de capacité et la collision, sur invite, en deux semaines.

### Argon (gemini-4-argon), pièce C

**Proposition centrale.** Une « dualité d'homogénéité » : avantage à l'adversaire en texte seul, renversé en faveur du défenseur dès que celui-ci soustrait les activations de deux copies sur le même code, ce qui annulerait la part commune liée à la tâche (« réjection de mode commun »).
**Plan.** Trois topologies (copies, modèles différents, agent seul), duel de collusion tacite, duel du différentiel d'activations contre sondes individuelles et contre modèles différents réalignés, duel de stéganographie après normalisation de l'arbre syntaxique.
**Après critiques.** Argon admet que le différentiel est un cas particulier de la sonde sur les états concaténés et qu'il ne peut gagner qu'à très faible budget d'étiquettes ; il le teste désormais par une courbe d'apprentissage, avec une passe de lecture forcée identique pour chaque rôle, un centrage par rôle, un adaptateur placebo et une consigne leurre au même vocabulaire. Il prédit toujours un gain du différentiel à zéro ou vingt-cinq étiquettes.

### Astra (gpt-6.2-astra), pièce D

**Proposition centrale.** Un avantage de **calibration** et non de lecture d'intention : une sonde apprise chez un rédacteur se transférerait mieux à un réviseur de mêmes poids qu'à un réviseur d'autres poids. Aucun avantage prédit contre un agent seul, qui garde lui aussi ses poids.
**Plan.** Seule pièce hors du code : planification d'ateliers, solveur exact comme oracle ; témoin d'identité (un processus unique qui recharge les contextes) ; quatre duels (excès adverse avant audit, gain de transfert, bilan après audit, copies contre agent seul).
**Après critiques.** Astra scinde le pari en deux tests : d'abord, plans et réviseur fixes, seule la source de la sonde change, sans aucune consigne adverse ; ensuite, un flux réel où l'on compte le dommage absolu livré, toute étiquette achetée étant débitée d'une enveloppe commune que l'équipe hétérogène répartit librement.

### Carbon (gemini-4-carbon), pièce E

**Proposition centrale.** Proche de celle d'Argon : en texte seul, les copies favorisent l'adversaire ; avec les activations, l'espace commun offre trois leviers au défenseur (mutualisation des étiquettes, différentiel entre copies, co-activation au même endroit du code).
**Plan.** Organismes adverses par adaptateurs pour éviter la consigne lisible ; contrôle par rotation aléatoire des activations ; duel copies contre agent seul.
**Après critiques.** Carbon construit des organismes conditionnels jumeaux (chacun sabote sur un motif d'énoncé et reste honnête sur l'autre) et un placebo, de sorte que l'étiquette soit indépendante des poids et du motif ; il ancre les activations aux nœuds de l'arbre syntaxique, accorde à l'équipe hétérogène un rejeu neutre de mêmes poids, passe en évaluation où chaque score est figé avant l'audit, et maintient la thèse du renversement du risque livré.

## 5. Accords et désaccords

### Convergences indépendantes au tour III.1

- **Antériorité.** Quatre pièces (Fable, Opus, Argon, Carbon) désignent « AI Control » de Greenblatt et al. comme le plus proche voisin, en notant de mémoire qu'il travaille en boîte noire. Quatre (Fable, Opus, Astra, Carbon) adossent le volet « défaillances corrélées » à Knight et Leveson.
- **Dispositif.** Llama 3.1 à huit milliards de paramètres comme modèle principal chez les cinq ; Qwen, Gemma ou Mistral comme comparateurs ; chaîne écrire–tester–relire chez quatre.
- **Deux effets opposés.** Opus, Argon et Carbon séparent explicitement un gain adverse et un gain défensif ; Fable et Astra posent aussi un bilan net à budget fixé.
- **Contrôles.** Les cinq exigent des erreurs honnêtes appariées ; quatre exigent de battre des vérifications mécaniques (tests par mutation, analyse statique) ; Fable, Opus et Carbon redoutent qu'une sonde lise la consigne et recourent à des adaptateurs ; Fable, Opus et Carbon prévoient un effet plancher à huit milliards de paramètres.

### Convergences des critiques (tour III.2)

- La mesure de cohérence d'Opus est nulle par construction sans canal (Fable, Argon, Astra, Carbon) ; Opus l'accepte.
- Sans canal, l'écart « même modèle moins autre modèle » dans un jeu focal est positif dès que les préférences diffèrent (Opus, Argon et Astra contre Fable) ; Fable l'accepte.
- Une sonde peut lire la signature de l'adaptateur, le thème ou la consigne : défaut transversal relevé contre toutes les pièces ; la parade commune est l'adaptateur placebo.
- « Défendable » défini par le moniteur textuel qui sert ensuite de concurrent : défaut relevé contre Opus, Argon et Carbon ; corrigé par des juges disjoints.
- Le rappel à budget est plafonné par le budget rapporté à la prévalence ; plusieurs critères chiffrés d'Argon et de Carbon sont, d'après les critiques, inatteignables.
- La sûreté sur une longue séquence sature et rend l'équivalence automatique (Argon, Carbon, Fable contre Opus) ; Opus passe au risque par épisode.
- Copies contre agent seul à contextes rechargés mesure la continuité du contexte, non les poids (contre Astra, Carbon, Argon) ; accepté partout.

### Désaccords

1. **Signe du gain d'agrégation sous corrélation.** Argon et Carbon soutiennent que la corrélation plus forte des copies réduit ou plafonne ce gain. Opus oppose deux contre-exemples numériques et une règle : le signe dépend du régime. Non résolu ; Opus le renvoie à l'arbitre et retire de lui-même toute prédiction directionnelle.
2. **Différentiel contre sonde concaténée.** Fable, Astra et Carbon : le différentiel est une contrainte, la sonde conjointe fait au moins aussi bien. Argon l'accepte asymptotiquement mais le maintient à très faible budget d'étiquettes, et le soumet à une courbe d'apprentissage. Ouvert, tranchable empiriquement.
3. **Fuite de consigne chez Astra.** Argon et Carbon : le gain de transfert est vrai par construction. Astra accepte la fuite possible mais rejette « vrai par construction » (un état peut dépendre du préfixe sans porter de direction stable entre rôles) et retire toute consigne adverse de son test principal.
4. **Impossibilité de la « compensation » chez Astra.** Argon la déclare mathématiquement impossible sous certains paramètres ; Astra rejette l'incompatibilité inconditionnelle et remplace son critère par le dommage absolu livré, dont il donne la borne de faisabilité.
5. **Rejeu par une copie saine.** Opus : le gain d'Argon peut venir du seul rejeu, disponible pour tout régime. Argon le rejette quand la compromission est dans les poids, l'accepte quand elle est dans le contexte, et en fait une ligne de base.
6. **Points mineurs** : une constante de calcul d'Argon, que Fable trouve doublée et Carbon autre (à recalculer) ; Carbon conteste que des copies au même adaptateur aient des activations identiques au-delà du préfixe commun ; Fable conteste que sa porte de deuxième semaine sélectionne sur la variable dépendante.

## 6. Ce qui est neuf et ce qui est fragile

### Neuf, au regard de ce que les modèles citent comme connu

D'après les modèles eux-mêmes, l'antériorité connue traite la surveillance par une copie et la collusion en boîte noire, la défaillance de mode commun en logiciel et les sondes sur un agent seul. Les apports candidats, tous au statut d'hypothèse :
- l'efficacité en étiquettes du transfert de sonde entre rôles de mêmes poids, comparée à budget d'étiquetage total égal (Astra au tour III.1, repris par Opus, Carbon et Fable au tour III.3) ;
- la décomposition de l'avantage du lecteur-copie en surprise, provenance et connaissance du défaut (Fable) ;
- la double différence de collision des choix sans canal (Opus) ;
- des organismes conditionnels jumeaux et placebos rendant l'étiquette indépendante des poids (Carbon, Opus, Argon), contribution de méthode ;
- le différentiel d'activations entre copies (Argon, Carbon), contesté.

Aucun modèle ne revendique de nouveauté établie.

### Fragile

- **Capacité.** Qu'un modèle de huit milliards de paramètres produise des défauts subtils en nombre suffisant n'est pas établi ; trois pièces en font une porte d'arrêt.
- **Sabotage induit.** Consigne ou adaptateur ne sont pas un sabotage spontané ; aucune pièce ne prétend le contraire.
- **Adversaire non adaptatif.** Fable abandonne ce test ; Opus et Carbon en gardent une version, contre une sonde figée puis réentraînée.
- **Peu de modèles.** Trois modèles donnent peu de degrés de liberté pour un effet d'interaction ; les conclusions porteraient sur « ces modèles ».
- **Puissance.** Les effectifs avancés sont élevés (Opus avance de l'ordre de sept à huit mille épisodes dégradés par composition pour une marge de deux points) ; Fable élargit sa marge à huit points.
- **Statuts « vérifié » autodéclarés.** Argon et Carbon marquent « vérifié » des calculs et des affirmations de fait (« faisable en deux mois ») que la pièce de faits ne fonde pas.
- **Oracle.** Chez Astra, sur un problème de planification difficile, l'erreur combinatoire honnête et la dégradation adverse tombent dans la même étiquette (critique d'Argon), d'où le parti d'Astra de compter tout plan dommageable comme positif.
- **Coût.** Les estimations, avancées par chaque modèle, vont de quelques centaines de dollars (Argon) à environ trois mille euros (Opus), avec de l'ordre de cent à six cents heures de processeur graphique ; aucune n'est vérifiée.
- **Critiques non résolues** : le signe de l'agrégation, l'utilité du différentiel, la fuite de consigne par l'attention.

## 7. Références à vérifier

Aucune de ces références n'a été vérifiée. Les modèles les citent de mémoire et inventent parfois des références, des auteurs ou des titres (exemple relevé par Fable et Opus : un co-auteur « Kieronzmann » attribué par Argon à « AI Control », que les autres pièces ne donnent pas).

| Référence telle que citée | Qui la cite | Pour quoi faire |
|---|---|---|
| Greenblatt, Shlegeris, Sachan, Roger (2023 ; 2024), « AI Control: Improving Safety Despite Intentional Subversion » | Fable, Opus, Argon, Carbon | Antériorité la plus proche : surveillance par copie, collusion, budget d'audit |
| Knight et Leveson (1986), « An Experimental Evaluation of the Assumption of Independence in Multiversion Programming » | Fable, Opus, Astra, Carbon | Défaillances de mode commun, loi connue ailleurs |
| Wen et al. (2024), « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats » | Fable, Opus | Menaces diffuses |
| Motwani et al. (2024), « Secret Collusion among (Generative) AI Agents » | Fable, Opus, Argon | Collusion par stéganographie |
| Mallen et al. (2024), « Subversion Strategy Eval » | Fable, Opus | Stratégie d'instances sans état |
| Panickssery, Bowman, Feng (2024), « LLM Evaluators Recognize and Favor Their Own Generations » | Fable | Auto-reconnaissance |
| Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn (2025), « Detecting Strategic Deception Using Linear Probes » | Fable | Sondes de tromperie |
| Järviniemi (2025), collusion par points focaux (titre à vérifier) | Fable | Coordination tacite |
| Schelling (1960), *The Strategy of Conflict* | Opus | Points focaux |
| MacDiarmid et al. (2024), « Simple probes can catch sleeper agents » ; Hubinger et al. (2024), « Sleeper Agents » | Opus | Sondes sur organismes à déclencheur |
| Bailey et al. (2024), « Obfuscated Activations Bypass LLM Latent-Space Defenses » | Opus | Obfuscation contre sondes |
| Burns, Ye, Klein, Steinhardt (2023), « Discovering Latent Knowledge in Language Models Without Supervision » | Argon, Carbon | Lecture non supervisée d'états latents |
| Kleinberg et Raghavan (2021), « Algorithmic Monoculture and Social Welfare » | Carbon | Monoculture algorithmique |
| Hendrycks et al. (2021), « Measuring Coding Challenge Competence With APPS » ; bancs dits MBPP, HumanEval, BigCodeBench | Opus, Fable, Carbon | Bancs de tâches de code |

## 8. Propositions retenues et non retenues

### Retenues

**1. Transfert de sonde entre rôles, à budget d'étiquetage total égal, plans et réviseur fixes.**
- *Soutien croisé* : pari d'Astra dès le tour III.1 ; Opus en fait son seul effet défensif restant (en le disant emprunté) ; Carbon le teste à budget d'étiquetage fixe ; Fable remplace sa probabilité conditionnelle par un gain de détection après quelques prises ; Argon adopte une courbe d'apprentissage.
- *Résistance* : elle survit aux critiques « l'agrégation de scalaires n'a rien de propre aux copies » et « l'alignement est réglable », puisqu'on balaie paires d'alignement et étiquettes.
- *Faisabilité et coût* : le premier test d'Astra ne demande ni réentraînement ni équipes complètes ; il peut échouer de façon informative même avec un oracle exact.

**2. Porte de validité des sondes : adaptateur saboteur conditionnel, placebo, thème croisé.**
- *Soutien croisé* : défaut transversal relevé par les cinq critiques ; parades convergentes d'Opus (plan croisé adaptateur × thème), de Carbon (organismes jumeaux), d'Argon et de Fable (adaptateur leurre, consigne leurre au même vocabulaire).
- *Résistance* : sans elle, toute conclusion tirée des activations reste attaquable comme lecture d'un artefact ; elle conditionne la proposition 1 dans son volet « politique incorporée aux poids ».
- *Coût* : quelques adaptateurs de plus ; Opus avance une hausse de son calcul d'environ un tiers.

**3. Mode commun et concentration des choix, mesurés d'abord et sans sonde.**
- *Soutien croisé* : identité admise par tous après critiques (sans canal, la loi jointe est le produit des marginales) ; Fable place en premier son expérience sans adversaire (angles morts honnêtes, mutation identique dans du code de chaque provenance) ; Opus place en premier la double différence de collision ; Carbon et Argon soustraient désormais le mode commun honnête.
- *Résistance* : la reformulation tient compte des deux critiques fatales du tour III.2 (mesure nulle par construction, écart positif par simple différence de préférences).
- *Coût* : le plus bas du dossier ; ouvre ou ferme les portes de jugeabilité avant toute dépense adverse.

**Condition de lecture commune** (non une proposition) : bilan en dommage livré par épisode, plafond du rappel affiché, évaluation où le score est figé avant l'audit, étiquettes débitées du budget. Astra, Opus, Carbon, Fable et Argon y convergent au tour III.3.

### Non retenues

- **Différentiel d'activations comme réjection de mode commun** (Argon, Carbon) : contesté par trois critiques, réduit par son auteur au régime à très faible budget d'étiquettes ; à garder comme bras comparé dans la proposition 1, non comme proposition.
- **Renversement du bilan par l'espace commun** (Carbon, Argon) : pari dont plusieurs versions étaient, selon les critiques, acquises d'avance ; il dépend des propositions 1 et 2.
- **Agrégation des scores entre copies** (Opus) : retirée par son auteur ; signe non déterminé a priori.
- **Rejeu par copie saine** (Opus) : retiré par son auteur.
- **Lecteur complice et test d'obfuscation** (Fable, Opus, Carbon) : utiles mais chers, placés en dernier par leurs auteurs.
- **Stéganographie après normalisation du code** (Argon, Carbon) : secondaire ; la mesure initiale était non jugeable selon les critiques.
- **Copies contre agent seul** (Astra, Carbon, Argon) : mesure la continuité du contexte ; gardé comme contrôle d'implémentation.
