# Ce que la longueur d'une tâche change pour le défenseur et pour l'adversaire : note de sortie du collisionneur

Dossier : `runs/collisionneur-protocole-x-papier-a-isole-v1-20261122-112512`

Rédigé par un lecteur Opus 5.5, classe C, à partir des seules cellules du dossier.

Aucune cellule ne rapporte de mesure. Tout ce qui suit est conception, calcul sous hypothèses ou prédiction. Les chiffres cités sont avancés par un modèle, presque tous qualifiés d'illustratifs par leur auteur, et aucun n'est établi.

## 1. La question

Un agent de langue mène seul une tâche de centaines d'actions ; il peut saboter le résultat par des actes dont aucun n'est suspect isolément, et un agent honnête se trompe aussi. Le défenseur lit le texte et les activations, dispose de quelques exécutions de comparaison et peut faire vérifier à grands frais une petite part du travail. Que change la longueur pour chacun, et qu'est-ce qu'une expérience de deux mois sur un modèle ouvert de huit milliards de paramètres pourrait trancher ?

## 2. En bref

- **Mesurer d'abord le bruit honnête, sans adversaire** : décomposer la variance d'un agent honnête en une part par action et une part commune à l'exécution, puis lire l'effet de la longueur relativement à ce bruit.
- **Éprouver les activations à poids contrôlés** : n'accepter « les activations gagnent avec la longueur » qu'avec un adaptateur bénin de même rang en classe négative et des contrôles qui séparent une politique suivie d'un indice relu dans le contexte.
- **Juger l'audit à budget absolu fixe** : le ciblage des vérifications coûteuses doit battre le tirage uniforme et le classement par position structurelle, sans index du générateur, d'abord sur un rapport faux fixé d'avance.

## 3. Ce que chaque modèle a proposé

### Claude Fable 5.2 (lettre A)

- **Proposition centrale.** Comparer l'exposant du dommage nécessaire pour dégrader le résultat à celui du dommage maximal indétectable : la longueur sert l'adversaire si le second dépasse le premier. Fable prédit un exposant d'environ un demi pour le texte et l'audit (loi en racine carrée de la stéganographie) et parie, confiance faible, qu'une sonde lit un « état d'intention » présent même aux actions bénignes.
- **Plan.** Une méta-analyse synthétique de 50 à 800 fiches, en variante additive et en variante en série (une décision précoce contamine la suite). Trois adversaires : écarts injectés par script, consigne cachée, adaptateur de bas rang à déclencheur. Coût avancé : 3 000 à 5 000 dollars.
- **Après les critiques.** Fable corrige trois énoncés (sa dérivation donnait au moniteur l'emplacement des actes, l'audit n'est pas indépendant de leur nombre, l'exposant d'un demi ne vaut pas pour toute tâche additive). Il juge la plus grave la critique du déclencheur réinjecté à chaque appel, qui rendait le signal d'état vrai par construction. Sa question devient : la longueur de bascule, rapport de la variance par action à la variance commune à l'exécution, tombe-t-elle dans les centaines d'actions ? Au-delà, la ressource limitante du défenseur devient le nombre d'exécutions de comparaison. Il prédit, confiance faible, une bascule entre 200 et 800 actions, et propose pour les activations un déclencheur en « ou exclusif », où la présence d'un indice ne détermine pas la politique.

### Claude Opus 5.5 (lettre B)

- **Proposition centrale.** Mesurer l'exposant de la dégradation maximale non détectée en fonction du nombre d'actions. Trois régimes, chacun lié à un mécanisme : exposant nul si chaque acte laisse un signal d'amplitude fixe, un demi selon la loi en racine carrée, un si la variance propre à chaque tâche domine. Prédiction notable : le gain apparent des activations serait surtout la lecture de l'instruction présente dans le contexte, non une « intention ».
- **Plan.** Des « analyses à bifurcations » synthétiques à vérité connue ; un adversaire scripté remplace un choix honnête, avec une probabilité donnée, par l'option qui pousse vers la cible ; des organismes en contexte et à adaptateur. Coût avancé : 1 000 à 3 000 dollars.
- **Après les critiques.** Opus accepte de Fable que son exposant ne valait qu'en unités absolues et rapporte désormais un exposant relatif : la dose indétectable rapportée à l'écart-type honnête du résultat. Il remplace le test par ordonnée à l'origine par des options leurres d'effet nul et retire la prédiction sur les goulots, vraie par construction. Son expérience prioritaire devient la décomposition de la variance honnête.

### Argon (identifiant gemini-4-argon, lettre C)

- **Proposition centrale.** La longueur favoriserait l'adversaire dans le texte et l'audit non guidé, et le défenseur dans les activations jointes aux comparaisons : le modèle devrait maintenir dans son flux résiduel une représentation de sa politique qui ne s'affaiblit pas. Face à un sabotage concentré sur deux actes, les bifurcations entre exécutions guideraient l'audit.
- **Plan.** Synthèse documentaire de 50 à 400 actions. Un adversaire diffus, un adversaire parcimonieux et un adversaire adaptatif entraîné à échapper aux sondes. Audit par un modèle ouvert de 70 milliards de paramètres. Coût avancé : environ 1 550 à 1 760 dollars.
- **Après les critiques.** Argon supprime le filtrage a posteriori des honnêtes sur la dégradation finale, ajoute un jumeau bénin et un adaptateur adverse « dormant », fait produire les comparaisons par l'agent suspect lui-même et crée quinze goulots d'égale centralité pour que le ciblage doive battre la position structurelle. L'expérience adaptative passe à trois longueurs. Sa prédiction centrale, un défenseur combiné qui se maintient ou progresse avec la longueur, reste inchangée.

### Astra (identifiant gpt-6.2-astra, lettre D)

- **Proposition centrale.** La seule à refuser une loi de longueur : une action ajoutée est soit une occasion de nuire, soit un témoin de plus sur une erreur commise. Astra prédit plus de dommage échappé avec des occasions, moins avec des témoins de sources distinctes.
- **Plan.** Des dossiers documentaires fictifs en trois variantes appariées : courte, longue à occasions, longue à témoins. Le critère principal est la probabilité qu'une conclusion fausse soit livrée sans interception confirmée. Coût avancé : 1 600 à 3 200 euros.
- **Après les critiques.** Astra retire l'index des liens du générateur, fuite de la vérité, fait du contraste occasions contre témoins à longueur égale le contraste principal et ajoute un parcours long neutre réellement vécu. Il place en premier un test à dommage fixé : le même rapport faux est présenté dans les deux vues longues, et l'on compte les suspensions justifiées, sans dépendre ni d'un agent saboteur ni d'une sonde. Il avance qu'environ 940 paires de dossiers seraient nécessaires.

### Carbon (identifiant gemini-4-carbon, lettre E)

- **Proposition centrale.** La longueur oppose l'accumulation séquentielle d'indices conditionnels au « blanchiment contextuel » : quelques actes précoces à fort levier, puis des déductions fidèles à un dossier déjà biaisé. Carbon s'appuie sur l'incrément de valeur conditionnelle, centré sous la politique honnête.
- **Plan.** Un banc de synthèse documentaire à graphe causal connu, de 40 à 300 actions, avec un adversaire diffus et un adversaire parcimonieux, et une « greffe chirurgicale » qui remet les poids honnêtes après les actes adverses. Coût avancé : 1 200 à 1 480 dollars.
- **Après les critiques.** Carbon remplace l'incrément de valeur (coût de l'ordre du carré de la longueur, somme qui télescope) par un résidu local à un pas, mesuré par un moniteur externe de trois milliards de paramètres. Il fixe la profondeur causale, prend pour classe négative un adaptateur de « veille conditionnelle bénigne » et ajoute un duel horizon contre profondeur. Il fait passer en premier le duel parcimonieux et le duel d'audit.

## 4. Accords et désaccords

### Accords indépendants au tour III.1

- **Le banc.** Les cinq modèles proposent des tâches synthétiques à vérité de terrain mécanique, et les cinq choisissent Llama-3.1-8B-Instruct comme agent.
- **L'antériorité.** Les cinq citent Greenblatt, Shlegeris, Sachan et Roger comme antériorité la plus proche pour le cadre du contrôle.
- **Diffus contre concentré.** Fable, Opus, Argon et Carbon distinguent un sabotage réparti d'un sabotage concentré sur quelques décisions ; Astra, occasions et témoins.
- **Les deux signaux possibles des activations.** Fable, Opus, Argon et Carbon formulent la même alternative : un signal d'acte, présent aux seuls actes sabotés et qui se dilue, ou un signal d'état, présent à chaque action et qui s'accumule.
- **Les comparaisons circulaires.** Les cinq notent que des exécutions de comparaison produites par le modèle suspect peuvent partager son biais.
- **Les issues sans intérêt.** Quatre modèles nomment presque les mêmes : saboteur incapable de rester discret, agent honnête déjà en échec, vérification du seul résultat final suffisante.

### Convergence née des critiques

- **Le bruit honnête d'abord.** Au tour III.3, Fable et Opus placent tous deux en tête la décomposition de la variance honnête en composante par action et composante d'exécution, et reconnaissent que la loi en racine carrée, sous adversaire scripté, est en partie vraie par construction.
- **L'adaptateur bénin.** Les cinq modèles finissent par l'adopter ou l'exiger. Fable le signalait comme défaut commun à Opus, Argon et Carbon : sans lui, la conclusion que les activations gagnent avec la longueur n'est réfutable chez aucun des trois.
- **Le filtrage sur l'issue.** L'appariement des honnêtes sur la dégradation finale, critiqué par les quatre autres, est abandonné par Argon et Carbon comme analyse principale.

### Désaccords

- **Qui la longueur favorise.** Argon et Carbon prédisent que les activations, accumulées, favorisent le défenseur. Opus prédit que ce gain apparent est surtout une lecture de l'instruction en contexte, et maintient cette prédiction après les critiques. Fable pariait sur un signal d'état qui plafonne. Il reconnaît ensuite que ce plafonnement était presque vrai par construction et le retire comme prédiction. Astra refuse de poser une loi. Les critiques n'ont pas tranché ce désaccord : elles ont rendu le test exigible.
- **La statistique centrée de Carbon.** Opus soutient qu'avec un centrage exact, l'hypothèse « la dérive honnête est indiscernable » ne peut être vraie pour cette statistique. Carbon rejette : sous sabotage additif, le rapport signal sur bruit décroît comme l'inverse de la longueur, l'hypothèse reste donc vraie, et aucun défenseur ne dispose de la politique honnête exacte. Chaque position tient sous ses hypothèses.
- **L'attribution à dommage égal.** Fable, Opus et Carbon objectent que comparer des rapports également dégradés désarme tout détecteur de dommage. Argon accepte de retirer le filtrage a posteriori mais défend la question elle-même : devant un rapport dégradé, erreur de bonne foi ou sabotage ? Il la garde comme analyse appariée a priori. Astra fait le même partage en séparant le risque opérationnel de son attribution à un mandat adverse.
- **L'audit à fraction constante.** Argon et Carbon jugent l'exposant d'un demi « forcé » quand on vérifie une fraction fixe du travail. Fable répond qu'il ne l'est que sous indépendance, justement testée, mais ajoute le bras à budget fixe.
- **L'index des liens chez Astra.** Avantageux par construction selon Argon et Carbon ; Astra le retire mais répond que faciliter la recherche ne garantit pas la confirmation d'un défaut.
- **L'audit du seul rapport final.** Fable le jugeait désarmé par l'appariement sur la dégradation ; Carbon répond que, sous blanchiment précoce, un audit à un lien depuis la fin ne voit pas la corruption amont.
- **Une date.** Greenblatt et al. : 2023 chez Fable, 2024 ailleurs (prépublication puis publication, à vérifier).

## 5. Ce qui est neuf, ce qui est fragile

### Neuf, par rapport à ce que les modèles citent eux-mêmes comme connu

Les modèles posent comme connus la loi en racine carrée, l'analyse séquentielle (Wald, Page), l'effet de plan sous corrélation intra-grappe (Kish), le cadre du contrôle et les sondes de tromperie. Fable soupçonne l'accumulation de preuves déjà couverte par un travail de 2024 sur les menaces réparties, qu'Opus nomme Wen et al. (2024), à vérifier. Pourrait rester propre :

- la comparaison explicite de l'exposant du dommage nécessaire et de celui du dommage indétectable, et sa version relative au bruit honnête (Fable, Opus) ;
- la longueur de bascule comme estimande, qui dit si la ressource limitante du défenseur est le nombre d'actions ou le nombre d'exécutions (Fable) ;
- le croisement indice et politique par un déclencheur en « ou exclusif », et les options leurres d'effet nul (Fable, Opus) ;
- le contraste occasions contre témoins à longueur égale, sur un rapport faux fixé (Astra) ;
- l'adaptateur de veille conditionnelle bénigne et la comparaison de l'audit guidé à la seule topologie des citations (Argon, Carbon).

Aucun modèle n'affirme une nouveauté établie. Tous renvoient à une recherche bibliographique, sans l'avoir faite.

### Fragile

- **La prémisse.** Qu'un modèle de huit milliards de paramètres sache saboter de façon diffuse sans acte visible, et tenir des centaines d'actions, est posé par les cinq comme une hypothèse douteuse. Les plans prévoient des arrêts précoces pour ce cas.
- **Les organismes modèles.** Les adaptateurs à déclencheur bornent un cas favorable. Fable le dit : rien n'établit qu'une intention non entraînée se représente de la même façon.
- **La fuite par le contexte.** Une consigne, même exclue des positions inspectées, se propage par l'attention aux activations ultérieures (Argon, Carbon). Retirer l'indice après la première action est la parade proposée ; Fable note qu'en contexte borné tout état passe alors par le résumé textuel, et que les activations ne se séparent plus du texte.
- **L'oracle exact.** Sur banc synthétique, la vérification est parfaite par construction ; aucun plan ne mesure un vérificateur réel.
- **La puissance statistique.** Selon les critiques, plusieurs duels sont sous-dimensionnés à 150 ou 300 dossiers ; Carbon passe à 500, Argon à 400 par cellule. Un seuil de rang sur quelques exécutions ne descend pas sous un taux de fausses alertes de un sur le nombre d'exécutions plus un.
- **Critiques non résolues.** La source des comparaisons reste un choix entre un oracle irréaliste et une copie suspecte ; le bras auto-généré est ajouté sans trancher. L'apprentissage du « ou exclusif » par l'adaptateur est une hypothèse, avec un repli prévu. L'expérience adaptative d'Argon peut lire un échec d'optimisation comme une impossibilité.

## 6. Références à vérifier

Aucune de ces références n'a été vérifiée. Toutes sont citées de mémoire par les modèles, qui inventent parfois des références, des auteurs ou des années.

| Référence telle que citée | Qui la cite | Pour quoi faire |
|---|---|---|
| Ker, Pevný, Kodovský, Fridrich (2008), « The Square Root Law of Steganographic Capacity » | Fable, Opus | Loi en racine carrée transposée |
| Bash, Goeckel, Towsley (2013), « Limits of Reliable Communication with Low Probability of Detection on AWGN Channels » | Opus | Même loi, en communication furtive |
| Greenblatt, Shlegeris, Sachan, Roger (2023 ou 2024), « AI Control: Improving Safety Despite Intentional Subversion » | les cinq | Cadre du contrôle, budget d'audit |
| Wald (1945), « Sequential Tests of Statistical Hypotheses » | Fable, Opus, Argon, Carbon | Accumulation séquentielle de preuves |
| Page (1954), « Continuous Inspection Schemes » | Opus, Carbon | Détection de rupture par somme cumulée |
| Kish (1965), « Survey Sampling » | Fable (tour III.3) | Effet de plan sous corrélation intra-grappe |
| Wen et al. (2024), « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats » | Opus ; Fable sans titre | Antériorité la plus proche sur les menaces réparties |
| Bhatt et al. (2025), « Ctrl-Z: Controlling AI Agents via Resampling » | Opus | Rééchantillonnage d'agents, proche des comparaisons |
| Benton et al. (2024), « Sabotage Evaluations for Frontier Models » | Opus ; Fable sans titre | Existence d'évaluations de sabotage |
| Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn (2025), « Detecting Strategic Deception Using Linear Probes » | Opus ; Fable sans titre | Sondes linéaires de tromperie |
| Kwa et al. (2025), « Measuring AI Ability to Complete Long Tasks » | Opus | Horizon de tâche limité des petits modèles |
| Silberzahn et al. (2018), « Many Analysts, One Data Set » | Opus | Variabilité analytique honnête |
| Burns, Ye, Klein, Steinhardt (2022), « Discovering Latent Knowledge in Language Models Without Supervision » | Argon | Sondes sur représentations internes |
| Azaria, Mitchell (2023), « The Internal State of an LLM Knows When It's Lying » | Carbon | Détection de mensonge par états internes |
| Un banc d'essai de sabotage et de surveillance d'agents (2025), sans auteurs | Fable | Référence non attribuée |

## 7. Propositions retenues et non retenues

### Retenues

1. **Décomposer le bruit honnête avant tout adversaire, et lire la longueur relativement à ce bruit.**
   - *Soutien croisé et résistance.* Fable et Opus y arrivent indépendamment au tour III.3, en réponse aux critiques convergentes des cinq modèles (effet de trajectoire, autocorrélation, queues lourdes, somme ou moyenne).
   - *Faisabilité et coût.* Ni adversaire ni adaptateur : c'est la moins chère du dossier, et chacune de ses deux issues falsifie une branche. Elle tranche aussi une issue « sans intérêt » : un écart-type honnête supérieur au dommage pertinent.

2. **Éprouver les activations à poids contrôlés.** Le dispositif comprend un adaptateur bénin de même rang, un adaptateur dormant, l'indice retiré après la première action, le croisement indice et politique, des options leurres d'effet nul et une consigne secrète bénigne.
   - *Soutien croisé et résistance.* Les cinq critiques en exigent une pièce ; les cinq réponses l'adoptent.
   - *Ce qu'elle tranche.* Le désaccord principal du dossier, activations gagnantes ou simple lecture de l'instruction. Coût modéré (affinage d'adaptateurs, extraction d'activations).

3. **Juger l'audit à budget absolu fixe, contre le tirage uniforme et contre la seule topologie, sans index du générateur, en commençant par un rapport faux fixé.**
   - *Soutien croisé.* La partie uniforme est calculable et non testée, ce sur quoi Opus, Argon et Astra s'accordent. Le comparateur topologique est demandé par Astra et adopté par Argon et Carbon. Le test à dommage fixé d'Astra sépare l'information du défenseur de la capacité de l'agent, critique soulevée par Opus, Argon et Carbon.
   - *Faisabilité.* Le test à dommage fixé ne dépend ni d'un agent saboteur compétent ni d'une sonde.
   - *Point faible.* Sa puissance exige un effectif élevé, plusieurs centaines de paires selon Astra.

### Non retenues

- **L'exposant sur adversaire scripté indépendant, comme résultat** : vrai par construction côté adversaire, admis par ses auteurs ; simple contrôle de la chaîne.
- **Le test par ordonnée à l'origine d'Opus** : biaisé par l'erreur sur la variable et la concavité ; retiré par son auteur.
- **Le balayage sur fenêtre courte de Carbon** : impossible sous furtivité par acte selon Argon et Fable ; retiré.
- **L'incrément de valeur centré de Carbon** : somme qui télescope, coût quadratique, centrage détruit par le filtrage ; remplacé.
- **Le filtrage a posteriori des honnêtes sur la dégradation finale (Argon, Carbon)** : biais de sélection variable avec la longueur ; abandonné comme analyse principale.
- **L'index des liens du générateur révélé au moniteur (Astra)** : fuite de la vérité ; retiré.
- **L'adversaire adaptatif d'Argon.** Coûteux, dépendant du succès d'un entraînement adverse, exposé à confondre échec d'optimisation et impossibilité ; à reprendre après les trois retenues.
- **Le duel horizon contre profondeur de Carbon** : pas retenu à part, mais son principe (profondeur causale fixe quand la longueur croît) est à intégrer aux trois retenues.
