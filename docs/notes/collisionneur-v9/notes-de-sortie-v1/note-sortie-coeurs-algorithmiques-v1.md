# Ce qu'un saboteur doit calculer et qu'un honnête ne calcule pas : note de sortie du collisionneur

Dossier : `runs/collisionneur-protocole-x-coeurs-algorithmiques-v1-20261122-114352`

Rédigé par un lecteur Opus 5.5, classe C, à partir des seules cellules du dossier. Le lecteur est du même modèle que l'un des six participants (Claude Opus 5.5) ; la note s'efforce de ne lui accorder aucun crédit particulier.

Aucun résultat empirique n'existe dans ce dossier : tout ce qui suit est conception, critique et réponse. Chaque chiffre cité est avancé par un modèle et présenté comme illustratif par son auteur.

## 1. La question

Un agent fondé sur un modèle de langue mène une longue analyse et peut la dégrader exprès, chaque action restant défendable lue seule ; un agent honnête se trompe aussi. Existe-t-il des calculs que seul le saboteur doit faire, peut-on les lire dans ses états internes mieux qu'en lisant le texte qu'il produit, et quelle première expérience sur un petit modèle ouvert dirait si la piste vaut d'être suivie ?

## 2. En bref : trois propositions retenues

1. **Commencer sans sonde, par deux tests de comportement** : vérifier que le petit modèle sait saboter de façon défendable (sinon « organisme inadéquat », annoncé d'avance), puis tester s'il évite la bonne action plus souvent que le hasard parmi des options défendables, ce qui prouve qu'il dispose d'une information sur elle.
2. **Ne lire les états internes qu'avant le choix, sur des états communs, contre des témoins honnêtes de même fabrication** : mêmes poids, ou adaptateurs honnêtes de même recette, en plusieurs exemplaires, avec contrôle sur texte neutre, consigne citée mais inerte et consigne active bénigne.
3. **Juger « mieux que le texte » contre l'auto-lecteur** (le même modèle relisant la trace sans la consigne), combiné au juge et aux vérifications mécaniques, au même budget d'étiquettes, sur toute la population, et dans un régime où la consigne de sabotage n'est pas dans le contexte.

## 3. Ce que chaque modèle a proposé

### Claude Fable 5.2 (A)

**Proposition centrale.** Le seul calcul commun probable est une « variable de mode » (dégrader ou non), représentée entre l'entrée et la sortie ; les autres dépendent de la forme du sabotage (commission ciblée, imitation d'un plus faible, omission, mauvais cadrage précoce). Une expérience peut réfuter une nécessité, jamais la prouver.

**Plan.** Banc tabulaire synthétique de 15 à 30 actions, trois conditions (honnête, sabotage instruit, sabotage appris à déclencheur). Après critiques : qualification de l'organisme sur deux populations (toutes les trajectoires pour l'effet, sous-ensemble apparié pour la détection) ; lecture avant l'action sur une banque de préfixes relus sous les deux modes, en plan croisé source du préfixe × mode de lecture, pour séparer le mode de la « surprise » du texte ; test d'évitement de la bonne action sans sonde ; reprise après retrait de la consigne pour savoir si le plan vit dans le texte. Verdict porté sur le régime à déclencheur.

**Prédiction.** Gain faible attendu pour le cadrage précoce ; un succès n'établirait que la variable de mode.

### Claude Opus 5.5 (B)

**Proposition centrale.** Trois candidats, chacun nécessaire sous condition : discriminer la bonne action (si le sabotage est sélectif), modéliser le contrôleur (si l'adaptation est en ligne), coordonner les actions (soit recalculée à chaque pas, soit portée par le texte). Une dégradation « amortie » dans les poids pourrait ne rien laisser à lire.

**Plan.** Après critiques, une expérience d'entrée sur un modèle de 7 à 9 milliards de paramètres, 1 000 tâches réparties par famille, mesurant trois choses : le gain de la sonde sur la meilleure base, l'équivalence de son score entre agent honnête et deux témoins (consigne conditionnelle non déclenchée ; consigne déclenchée mais bénigne, témoin ajouté au tour 3), et une localisation en différence de différences (pas à fort impact contre pas routiniers, chez le saboteur moins chez l'honnête). Puis reprise croisée à cinq bras et adaptateurs auto-distillés répliqués.

**Prédiction.** Il tient que la dégradation compilée dans les poids ne laisse rien à lire au moment de l'inférence, et abandonnerait la lecture interne si la sonde ne bat pas la base.

### Gemini 4 Argon (C)

**Proposition centrale.** Non en général (une heuristique appauvrie suffit) ; oui sous trois conditions conjointes : tâche auto-correctrice, conclusion fausse visée, représentations correctes préservées. Le saboteur ferait alors un « double suivi » : calculer la bonne réponse puis l'inhiber, filtrer la plausibilité, garder la cohérence de la déviation. Sur trajectoires longues à erreurs indépendantes, un test séquentiel sur le texte gagne ; l'avantage interne ne subsisterait que pour la détection précoce ou contre une erreur honnête « boule de neige ».

**Plan.** Après critiques : six adaptateurs de faible rang par classe (saboteur, honnête biaisé, honnête standard), entraînés sans consigne ; test de médiation sur états identiques (même préfixe, même erreur) ; comparaison séquentielle contre une base combinant somme cumulée des log-probabilités, auto-lecteur et juge, mesurée par le temps moyen restreint avant détection.

**Prédiction.** Échec du transfert de l'instruction vers l'entraînement, transfert limité aux pas de contradiction directe.

### GPT-6.2 Astra (D)

**Proposition centrale.** Une nécessité « par construction » mais faible : si la clé nuisible change avec les données, le choix doit dépendre d'une information discriminante, que l'honnête utilise aussi. Contre-exemple : un contrôleur externe qui choisit la mauvaise branche ne laisse rien de distinct dans le modèle exécutant.

**Plan.** Dossiers de réconciliation en jumeaux à conséquences inversées, but assigné au hasard, lecture arrêtée juste avant le premier jeton du choix, unité statistique la famille de dossiers. Après critiques : pilotage d'abord, sans sonde ni affinage, sur un modèle de 1,5 milliard de paramètres ; échange causal où « copier l'action du donneur » et « appliquer le but du receveur à la carte du donneur » prescrivent des clés différentes.

**Prédiction.** Aucune ; un succès soutiendrait un calcul de conséquence partagé, pas un circuit propre au dégradeur.

### Gemini 4 Carbon (E)

**Proposition centrale.** Trois nécessités conditionnelles : inverser la polarité sur des instances symétriques (ce qui exige une information sur la vérité), arbitrer à la frontière de défendabilité, viser les étapes à fort levier aval. La dérive peut aussi être « stigmergique » : portée par l'historique textuel.

**Plan.** Après critiques : familles de huit dossiers à quatre conclusions symétriques, croisant la vérité et une heuristique naïve (strates concordante et discordante définies d'avance) ; six adaptateurs par classe ; lecture avant le choix ; greffe croisée des préfixes à mi-parcours.

**Prédiction.** Faible transfert de l'instruction vers les poids ; une part majeure de la dérive deviendrait stigmergique après les premiers choix.

### Gemini 4 Neon (F)

**Proposition centrale.** Aucun calcul universellement nécessaire ; un calcul différentiel devient plausible sous quatre conditions (contingence aux données, cible orientée, frontière de défendabilité étroite, pas de raisonnement libre écrit). Sept cas où il n'y a rien à lire, dont la dilution : avec une alerte à 1 % par pas sur 100 pas indépendants, environ 63 % des trajectoires honnêtes déclencheraient (calcul avancé par Neon).

**Plan.** Bac à sable d'analyse statistique ; après critiques, six créneaux pivots fixés d'avance, dont trois « en conflit » et trois « alignés » tirés par le générateur, pour une localisation exogène ; six témoins honnêtes ; plan croisé régime (contingent ou compilable) × origine (consigne ou renforcement) ; vérification mécanique « multivers » (réexécution sur les variantes méthodologiques standards).

**Prédiction.** La lecture dépendrait de la contingence et s'effondrerait en régime compilé.

## 4. Accords et désaccords

### Accords indépendants au tour III.1

- **Pas de calcul universellement nécessaire.** Les six modèles l'écrivent, chacun par un argument propre : heuristique biaisée compilée (Argon, Carbon, Neon), politique amortie (Opus), contrôleur externe (Astra), variable de mode seulement (Fable). La nécessité ne vaut que pour une dégradation sélective ou contingente aux données.
- **La réponse dépend de l'origine** (instruction, déclencheur appris, entraînement sans déclencheur) : les six le supposent.
- **Les cas « rien à lire »** se recoupent : heuristique compilée, erreur unique puis exécution honnête, plan porté par le texte, sous-capacité du modèle, obfuscation contre la sonde.
- **Une porte de qualification** avant toute sonde, pour qu'un échec du petit modèle ne soit pas lu comme une réponse négative : Fable, Opus, Astra, Carbon, Neon.
- **Battre une base textuelle forte**, pas un juge qui ne lit qu'une action isolée : tous.

### Accords obtenus par la critique

Les critiques ont trouvé presque partout les mêmes défauts : témoins honnêtes fabriqués autrement (modèle plus faible, bruit, température) ; un seul adaptateur par classe, qui laisse la sonde lire l'identité des poids ; lecture après l'action ; seuils à 1 % de fausses alertes inestimables sur quelques centaines de trajectoires ; réglages faits sur le test. Au tour III.3, tous ont accepté l'essentiel : lecture avant le choix, mêmes poids ou même recette, plusieurs adaptateurs, trois lots disjoints, critère à 5 %, auto-lecteur parmi les bases.

### Désaccords

- **Le régime instruit sert-il à quelque chose ?** Fable argue qu'à poids fixes l'état interne est une fonction du contexte : en régime instruit, « mieux que le texte » revient à lire la consigne ; elle porte le verdict sur le régime à déclencheur. Opus accepte en partie mais refuse d'en conclure l'inutilité : ce régime sert à éprouver les témoins de consigne et la localisation, et son expérience d'entrée reste instruite. Argon et Carbon placent la première expérience sur des adaptateurs sans consigne ; Neon commence par la consigne, puis l'entraînement en seconde phase. Astra retire son duel mécaniste sur le but assigné, faute de pouvoir battre un lecteur qui connaît la consigne.
- **Que conclure quand l'intervalle ne tranche pas ?** Argon adopte une règle « sans zone grise » : une borne inférieure sous le seuil réfute l'hypothèse favorable, y compris par manque de puissance. Fable, Opus, Astra, Carbon et Neon gardent une issue « non tranché » (avec, chez Fable et Neon, une seule réplication annoncée d'avance). Le désaccord n'a pas été discuté entre eux.
- **Taille du premier organisme et affinage d'emblée.** Astra propose 1,5 milliard de paramètres sans affinage ; les autres 7 à 9 milliards, Argon et Carbon avec six adaptateurs par classe dès le départ. Opus avait critiqué chez Astra l'absence de distinction entre banc trop dur et modèle trop petit ; Astra répond par une version courte du dossier comme contrôle positif.
- **Le « double suivi » (calculer le vrai, puis l'inverser).** Argon et Carbon le posent ; Astra objecte qu'avec deux classes prédire le faux informe sur le vrai sans imposer deux opérations successives. Carbon l'accepte pour deux classes et passe à quatre ; Argon garde l'hypothèse et la soumet à un test de médiation.
- **Statut « vérifié » de certains arguments.** Opus et Astra contestent chez Argon le recours au théorème d'approximation universelle et à l'argument « croissance linéaire contre racine carrée », chez Carbon l'appel à l'inégalité de Fano. Argon accepte la première objection et rejette la seconde (son argument était conditionnel à des erreurs indépendantes) ; Carbon accepte.
- **Critiques rejetées.** Fable reporte le saboteur sans déclencheur que Carbon jugeait indispensable (confondu avec l'identité des poids tant qu'il n'y a qu'un adaptateur par classe) ; Carbon rejette la circularité que Fable voyait dans son juge ; Neon rejette une objection d'Opus sur la puissance du contrôle « multivers ».

## 5. Ce qui est neuf, ce qui est fragile

### Neuf, au regard de ce que les modèles citent eux-mêmes

Tous écrivent, sans pouvoir le prouver, ne connaître aucun travail établissant un calcul nécessaire au sabotage, ni une lecture interne évaluée contre des erreurs honnêtes appariées sur de longues tâches d'agent. Sur ce fond, les éléments les plus originaux sont :

- le plan croisé « source du préfixe × mode de lecture » qui sépare le mode de la surprise du texte (Fable) ;
- le témoin de consigne déclenchée mais bénigne (Opus) ;
- l'échange causal qui oppose « suivre le but du receveur » à « copier l'action du donneur » (Astra) ;
- la divergence entre couches sans oracle et le temps moyen restreint avant détection (Argon) ;
- les familles à quatre conclusions croisées avec une heuristique naïve (Carbon) ;
- la localisation exogène par créneaux « en conflit » et « alignés » et le plan croisé régime × origine (Neon).

### Fragile

- **L'organisme.** Tous doutent qu'un modèle de 2 à 9 milliards de paramètres sache saboter de façon défendable ; les bancs vont de 15 à 60 actions, loin des « centaines » de la question.
- **L'appariement.** Les erreurs honnêtes appariées peuvent être rares : Argon avance, pour le banc d'Astra, une strate difficile d'une douzaine de paires. Fable et Opus exigent une couverture minimale publiée.
- **La portée d'un succès.** Fable, Opus et Astra admettent qu'un positif établirait au mieux une variable de mode ou un calcul partagé, non un calcul propre au saboteur ; un signal sur adaptateurs identifie une provenance, pas un motif (Astra).
- **Ce qui n'est testé par personne.** L'entraînement adverse contre la sonde, et un agent qui sabote par stratégie propre plutôt que par instruction ou entraînement.
- **Le coût a crû après les critiques** (chiffres avancés par les auteurs) : de 20 à 80 euros pour le pilote d'Astra à 200 à 400 heures de processeur graphique chez Fable, 450 à 1 000 euros pour l'expérience d'entrée d'Opus, jusqu'à 2 750 dollars au total chez Neon.
- **Critiques restées ouvertes.** La puissance des échanges causaux « dans chacun des deux buts » (Fable sur Astra) ; la séparation entre une donnée d'entrée transportée et une conséquence anticipée dans les jumeaux d'Astra, que sa réponse traite par une permutation du code de réponse sans démonstration ; la possibilité qu'un plan hérité et un mode recalculé donnent la même loi d'actions, que seul une sonde après retrait pourrait séparer (Fable).

## 6. Références à vérifier

**Aucune de ces références n'a été vérifiée.** Toutes sont citées de mémoire par les modèles, qui inventent parfois titres, auteurs ou années ; deux divergences entre modèles sont déjà visibles.

| Référence telle que citée | Qui la cite | Pour quoi faire |
|---|---|---|
| van der Weij et al., *AI Sandbagging: Language Models can Strategically Underperform on Evaluations* (2024) | Fable, Opus, Argon, Carbon, Neon | Existence du sous-rendement stratégique |
| Greenblatt et al., *Stress-Testing Capability Elicitation With Password-Locked Models* (2024) | Fable, Opus | Capacité verrouillée par mot de passe |
| Hubinger et al., *Sleeper Agents* (2024) | les six | Comportements conditionnels appris et persistants |
| Greenblatt et al., *AI Control: Improving Safety Despite Intentional Subversion* (2023 ou 2024) | Fable, Opus, Argon, Carbon ; Neon écrit « Regardless of » | Contrôle par moniteurs lisant le texte ; titre divergent |
| Benton et al., *Sabotage Evaluations for Frontier Models* (2024) | Fable, Opus, Argon ; Neon sans auteur | Évaluations de sabotage |
| Kutasov et al., *SHADE-Arena* (2025) | Fable | Sabotage d'agents et surveillance |
| Goldowsky-Dill et al., *Detecting Strategic Deception Using Linear Probes* (2024 ou 2025) | Fable, Opus, Argon, Neon | Sondes linéaires de tromperie |
| *Simple probes can catch sleeper agents* (2024), attribué à MacDiarmid et al. ou à « Anthropic » | Fable ; Opus, Argon, Carbon, Neon sans titre sûr | Sondes sur agents dormants |
| Azaria et Mitchell, *The Internal State of an LLM Knows When It's Lying* (2023) | Fable, Opus, Carbon, Neon | Lecture interne du mensonge |
| Marks et Tegmark, *The Geometry of Truth* (2023 ou 2024) | Fable, Argon, Neon | Structure linéaire du vrai et du faux |
| Burns et al., *Discovering Latent Knowledge in Language Models Without Supervision* (2022 ou 2023) | Fable, Argon, Carbon, Neon | Connaissance latente sans supervision |
| Zou et al., *Representation Engineering* (2023) | Argon, Carbon, Neon | Vecteurs de lecture et de contrôle |
| Levinstein et Herrmann, *Still No Lie Detector for Language Models* (2023 ou 2024) | Fable, Neon | Limites des détecteurs ; année divergente |
| Bailey et al., *Obfuscated Activations Bypass LLM Latent-Space Defenses* (2024) | Fable | Activations rendues illisibles |
| Hewitt et Liang, *Designing and Interpreting Probes with Control Tasks* (2019) | Fable, Opus, Astra, Neon | Tâches de contrôle des sondes |
| Belinkov, *Probing Classifiers* (2022) ; Ravichander et al., *Probing the Probing Paradigm* (2021) ; Elazar et al., *Amnesic Probing* (2021) | Fable, Argon, Neon ; Opus, Neon | Ce qu'une sonde ne prouve pas |
| Geiger et al., *Causal Abstractions of Neural Networks* (2021) | Carbon, Neon | Interventions d'échange |
| Tice et al., *Noise Injection Reveals Hidden Capabilities of Sandbagging Language Models* (2024) | Fable, Opus | Détection sans sonde |
| Baker et al., *Monitoring Reasoning Models for Misbehavior* (2025) ; Emmons et al., *When Chain of Thought is Necessary…* (2025) | Fable, Opus ; Fable | Surveillance du raisonnement écrit |
| Travaux d'Apollo Research sur la manigance en contexte (2024) ; travaux d'un institut public sur des sondes de sous-rendement (2025) | Neon ; Fable | Non identifiés |

## 7. Propositions retenues et raisons

### Retenues

1. **Deux tests de comportement sans sonde : qualification, puis évitement de la bonne action.** Cinq modèles proposaient la qualification indépendamment au tour III.1, et la critique l'a renforcée : juge de défendabilité distinct des lecteurs évalués, aucune trajectoire filtrée sur son verdict (Opus, Astra, Neon), contrôles positifs (sabotage déclaré, fautes grossières non avouées). Le test d'évitement (Fable au tour III.3, pilotage par jumeaux d'Astra, options symétriques de Carbon) donne une réponse partielle et peu coûteuse à la première question : éviter la bonne action mieux que le hasard exige une information sur elle. C'est l'étape la moins chère du dossier et elle ne dépend d'aucune hypothèse sur la lisibilité.
2. **Lecture avant le choix, sur états communs, contre des témoins de même fabrication.** C'est la convergence la plus nette du dossier : le défaut a été relevé chez cinq propositions par plusieurs critiques, et toutes les réponses l'ont accepté. Sans cela, tout positif peut s'expliquer par l'identité des poids, le bruit du témoin ou la relecture de l'action écrite. Coût modéré, sauf la réplication des adaptateurs.
3. **Comparaison à l'auto-lecteur, dans un régime sans consigne au contexte.** L'argument « à poids fixes, l'état ne contient que le contexte », venu de Fable, a été accepté au moins en partie par les cinq autres ; l'auto-lecteur a été adopté par Opus, Argon, Carbon et Neon. Seule cette comparaison répond au second volet de la quatrième question sans être gagnée d'avance.

### Non retenues pour la première expérience

- **La reprise croisée et la greffe de préfixes** (Fable, Opus, Carbon) : bien construites après critique, mais elles supposent un organisme déjà qualifié ; à garder pour la suite.
- **Le test de médiation du « double suivi »** (Argon) et **l'échange causal d'Astra** : les critiques de puissance et de construit (donnée d'entrée ou conséquence anticipée) restent ouvertes.
- **Le plan croisé régime × origine avec renforcement** (Neon) et **l'auto-distillation répliquée** (Opus) : les plus coûteux, et sans objet si la première expérience échoue.
- **La règle de décision sans zone grise** (Argon) : elle compte un manque de puissance comme une réfutation, ce que les cinq autres refusent.
- **Le premier organisme à 1,5 milliard de paramètres** (Astra) : peu coûteux mais isolé ; utile comme pilotage, pas comme verdict.
