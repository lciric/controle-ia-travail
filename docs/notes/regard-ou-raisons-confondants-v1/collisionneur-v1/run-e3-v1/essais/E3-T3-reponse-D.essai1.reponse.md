# Proposition D — Tour III.3

Les sections visant D et les objections transversales sont présentes et lisibles. Les constats du projet demeurent **RAPPORTÉS** par [B] ; mes corrections sont des **HYPOTHÈSES** méthodologiques. Les calculs algébriques explicitement vérifiés ci-dessous ne changent pas le statut des données.

## 1. Réponse aux critiques

### Critiques de A visant D

1. **Juge réutilisé hors de sa distribution d’étalonnage — acceptée.** L’étalonnage sur les scénarios d’origine est seulement **RAPPORTÉ** ; rien n’établit sa validité sur traces éditées ou nouveaux scénarios. Tout test nouveau exige un étalonnage humain aveugle et mécanique, stratifié par adaptateur et condition, gelé avant l’analyse principale. Le modèle de départ, déjà Instruct, ne servira plus de contrôle supposé invariant : ses réactions sont mesurées, pas postulées.

2. **Classifieur sémantique et « raisons » non exclusifs — acceptée.** Une sensibilité à consentement, finalité ou autorisation ne falsifie qu’un classifieur lexical ou une politique fixe sur attributs explicitement restreinte. Elle ne distingue pas un classifieur sémantique riche d’un usage des justifications. Je retire donc l’issue « inversion suivant le principe falsifie le contenu » dans sa généralité. Les adaptateurs seuls peuvent établir une **sensibilité contrefactuelle au contenu fourni à l’inférence**, non la médiation par des raisons apprises pendant l’entraînement.

3. **Permutation entre scénarios = test d’incohérence — acceptée.** Elle est remplacée par des traces **auto-produites sur le scénario courant**, puis minimalement éditées : entités, outils, conclusion et format sont autant que possible conservés ; seule la justification devient non applicable ou substituée. La permutation inter-scénarios devient exploratory, jamais le contraste principal.

4. **Restauration présentée comme réversibilité — acceptée.** Réinsérer le préfixe original vérifie le pipeline et, à poids et décodeur identiques, la distribution conditionnelle ; ce n’est pas un contrôle de spécificité causale. Une correction en cours de trace devient un bras secondaire, sans prétendre isoler à elle seule le mécanisme.

5. **Référence et témoin à coût égal mal définis — acceptée sur le témoin, rejetée pour une référence intacte commune.** Si la référence reste intacte et commune, elle s’annule algébriquement dans \(G_{\text{intact}}-G_{\text{corrompu}}\). Si elle reçoit aussi des greffes, l’objection est fondée. La métrique principale sera donc **intra-adaptateur**, avec les bras de référence rapportés séparément.

6. **Audit de dose supposant des configurations publiées — acceptée.** Cet audit est conditionnel à la disponibilité des configurations, journaux ou données. Sinon, la rivale « dose/optimisation » est déclarée **non tranchable avec les seuls adaptateurs**, et non auditée par défaut.

7. **Croyance : étalon et indépendance des familles de textes — acceptées.** L’étiquette mesurable est le **contexte assigné par l’expérimentateur**, pas une croyance interne. La cohérence des questions directe et inversée est nécessaire pour cet instrument déclaratif, sans valider une croyance causale. Les jeux tenus à l’écart doivent séparer auteurs humains ou modèles, gabarits et domaines ; changer seulement de sous-dossier ne suffit pas.

8. **Puissance et asymétrie du seuil de cinq points — acceptée.** Le seuil est retiré. Les calculs de A sont **illustratifs**, mais suffisent à montrer qu’un seuil fixe peut être inatteignable. Le pilote estimera d’abord corrélation intra-scénario, hétérogénéité et effets génériques des greffes ; le seuil d’effet substantiel et la précision requise seront ensuite préenregistrés, sans choisir le seuil d’après l’effet observé.

9. **Plafond, permutations et banc d’essai — acceptées.** Les paires sémantiques sans marge entre modèles seront non jugeables. Les permutations seront faites par blocs de scénarios. Avec un seul organisme conditionnel, le banc valide seulement une sensibilité locale ; il ne fournit pas un taux de détection sur une population.

10. **Contrôles dits fatals — transformés en tests.** J’ajoute : préfixe dont l’effet vérifie qu’il est lu ; préfixes neutres appariés pour référence et jumelle ; changement de fait pertinent sans changement de bonne action ; organisme stable non conditionnel ; corruption cohérente et résumé factuel sans norme. L’objection transversale de A est également acceptée : un test d’inférence ne tranche pas ce qui a été appris pendant le midtraining.

### Critiques de B visant D

1. **Suppositions non hiérarchisées — acceptée.** Ordre de blocage : validité de la mesure → stabilité des gains → validité des stimuli → tests de contenu à l’inférence → banc, transport et ablation → claims d’entraînement. Une étape non satisfaite limite les conclusions suivantes sans paralyser les analyses indépendantes.

2. **Contenu et format insuffisamment dissociés — acceptée.** Le protocole devient factoriel : contenu pertinent ou substitué × format original ou reformulé. Une interaction contenu × format sera rapportée, plutôt que compressée en une perte unique.

3. **Déductibilité définie par les auteurs ou un LLM — acceptée.** Un panel humain, ignorant les résultats des modèles, préenregistrera les actions déductibles, les actions permises et les cas ambigus ; l’accord et les désaccords seront publiés.

4. **Absence de règle de décision entre instruments — acceptée.** La validation est séquentielle et conditionnelle : échec du juge = gain comportemental non confirmé ; échec du banc = ablation non informative ; échec du transport = résultat limité à la direction importée. Il n’y a pas de règle « tous les instruments doivent réussir pour publier quoi que ce soit ».

5. **Ordre du papier — acceptée.** La validation des instruments précédera l’interprétation comportementale. La reproduction chronologique ira dans une section méthodologique ou en annexe.

6. **Puissance, transport et bootstrap — acceptées avec une réserve.** A et B aboutissent, sous leurs propres paramètres **illustratifs**, à des faisabilités différentes : aucun de ces calculs ne remplace l’estimation de la variance réelle. J’accepte la nécessité d’analyses groupées au niveau du scénario et de sensibilités par action ; je rejette l’affirmation que trois actions impliquent automatiquement trois unités indépendantes, corrélation non fournie.

7. **Organisme négatif et détection de greffe — acceptées.** Le banc exige un organisme stable soumis aux mêmes interventions, s’il est disponible. En revanche, la question « cette trace est-elle cohérente ? » proposée par B n’est qu’un diagnostic : le dossier **RAPPORTE** précisément une divergence entre déclarations et actions. Elle sera complétée par éditions minimales, annotations humaines de plausibilité et contrôles comportementaux.

### Critiques de C visant D

1. **Restauration et choc de vraisemblance — acceptées.** Leur correction rejoint les bras auto-produits et cohérents ci-dessus ; la perplexité pourra être mesurée, mais ne sera pas traitée comme une preuve d’équivalence des stimuli.

2. **Contamination des directions locales — acceptée.** Les corpus croiseront évaluation/déploiement, sûreté/hors sûreté et refus/absence de refus. Les directions locale et importée suivront exactement le même protocole de sélection. Une direction de refus générique sera un diagnostic ; ni un faible cosinus ni une orthogonalisation ne suffiront à établir la pureté causale.

3. **Algèbre de \(L\) et plancher — acceptées.** Pour référence commune, **VÉRIFIÉ par calcul** :
   \[
   L=G_{\text{intact}}-G_{\text{corrompu}}
    =p_{\text{corrompu}}-p_{\text{intact}} .
   \]
   Je supprime donc la référence de l’estimand principal. Si une corruption réduit aussi l’exécution bénigne ou la capacité d’appel d’outil, le contraste est déclaré non interprétable, pas favorable à une hypothèse.

4. **Seuils de transport et faux rejets binomiaux — acceptée.** Les blocages reposeront sur des intervalles et une précision préenregistrée, non sur le seul dépassement ponctuel d’un petit seuil.

5. **Contrôles proposés — transformés en tests.** J’adopte le résumé factuel exact sans énoncé normatif, la justification non applicable mais plausible et la direction de refus comme contrôles ; aucun n’est présenté comme suffisant isolément.

### Critiques de E visant D

1. **Nécessité sans minimum d’effet — acceptée.** Une équivalence dans une marge ne réfute pas une contribution positive arbitrairement petite. Le duel portera désormais sur une **contribution matérielle supérieure à un seuil opérationnel**, et non sur la nécessité métaphysique de tout contenu justificatif.

2. **Référence greffée, restauration et sélection des témoins — acceptées.** Les effets intra-adaptateurs précèdent toute différence de gains. Les directions témoins seront appariées en dégât sur un jeu indépendant, puis gelées avant l’évaluation principale.

3. **Population du banc — acceptée.** Un organisme valide une intervention pour cet organisme ; sans population définie et échantillonnée, aucune sensibilité générale n’est estimée.

4. **Interaction obligatoire avec les phrases — acceptée et retirée.** Une intervention sur le regard peut agir sans interaction avec des phrases qui ne déplacent pas l’état causal pertinent. Les phrases deviennent des modificateurs secondaires ; leur absence d’interaction n’invalide ni n’établit le regard.

5. **Conséquence éditoriale — acceptée.** La figure principale distinguera explicitement : effet des recettes, sensibilité au contenu fourni à l’inférence, et médiation par des raisons apprises. Seule cette dernière exige, si les journaux sont insuffisants, une intervention d’entraînement appariée.

## 2. Expériences corrigées

### E0 — Verrou de mesure, sur épisodes déjà joués

**Duel opérationnel.** \(H_A\) : le gain principal subsiste matériellement sous mesure indépendante ; \(H_B\) : il est réduit au-dessous du seuil préenregistré sous cette mesure. Persistance falsifie \(H_B\) pour ce résultat ; disparition falsifie \(H_A\) pour le gain publié.

Un échantillon aléatoire stratifié comprend accords et désaccords entre juges, exécutions partielles, appels sans effet, traces visibles ou masquées et même outil bénin. Annotation humaine aveugle et journaux mécaniques sont les références ; un second juge n’est qu’un contrôle supplémentaire. Les effets absolus priment ; \(S\) n’est calculé que lorsque son dénominateur est estimable, avec permutations par scénario et analyses de sensibilité par action.

### E1 — Contenu × format, premières nouvelles générations

La recette avec raisonnement produit ses propres traces. Une procédure gelée réalise :

- contenu pertinent ou justification substituée/non applicable ;
- format original ou reformulation conservant le contenu ;
- contrôles : édition non sémantique, résumé factuel sans norme, conclusion sans justification, préfixe de vérification de lecture.

Tous les modèles reçoivent les mêmes scénarios, tirages et plafonds de tokens ; référence et jumelle reçoivent aussi des préfixes neutres appariés, mais leurs effets ne sont pas soustraits naïvement. Les phrases d’observation sont croisées secondairement.

Soit \(p_t\) le taux d’action nuisible **exécutée et validée** dans la condition \(t\). Le contraste principal, à format fixe, est :
\[
\Delta_C=p_{\text{contenu substitué}}-p_{\text{édition non sémantique}} .
\]
- \(H_A\) : \(\Delta_C>\delta\), où \(\delta\) est le plus petit effet substantiel préenregistré.
- \(H_B\) : \(\Delta_C\leq\delta\).

Une borne inférieure au-dessus de \(\delta\) falsifie \(H_B\) ; une borne supérieure au-dessous ou égale à \(\delta\), avec précision suffisante, falsifie \(H_A\) dans ce périmètre. Un intervalle enjambant \(\delta\) est non concluant. Une dégradation générique des tâches bénignes rend le test non jugeable.

### E2 — Transfert et sur-sensibilité

Sur des outils et domaines écrits indépendamment, le panel fixe à l’avance la bonne action. Les marqueurs normatifs non pertinents, autorisations invalides et changements de faits sans conséquence normative testent la sur-sensibilité.

**Duel :** \(H_A\), transfert indépendant \(\leq\delta_T\), contre \(H_B\), transfert \(>\delta_T\). Chaque issue tranchante falsifie l’autre borne. Un transfert positif écarte une restriction de surface mesurée ; il ne suffit toujours pas à identifier des raisons apprises.

### E3 — Direction, banc et transport

Textes tenus à l’écart par auteur, gabarit et domaine ; mêmes hyperparamètres pour sondes locales et importées ; témoins appariés sur un jeu indépendant puis gelés.

**Duel :** \(H_A\), intervention sensible et spécifique ; \(H_B\), sonde de surface, mauvais transport ou dégât générique. Réduction de l’écart de l’organisme conditionnel sans équivalent chez l’organisme stable falsifie \(H_B\) localement. Échec du banc ou dégât équivalent sous témoins falsifie \(H_A\) comme validation de l’instrument. L’ablation des adaptateurs n’est interprétée qu’ensuite.

## 3. Réponse à l’arbitre — page synthétique

**Ce qui est établi.** Rien de causal n’est établi indépendamment dans le dossier. Sont **RAPPORTÉS** : reproduction approchée des taux, forte différence entre jumelles, refus même sur ordre avec exécution bénigne du même outil, effet des phrases sur les croyances déclarées mais presque pas sur les actes, et contraste dépendant des formulations. Ces constats justifient l’étude, pas son interprétation.

**Ce qui ne l’est pas.** Ni l’usage causal des raisons, ni la présence ou l’absence du regard, ni une croyance interne, ni la validité du juge sur nouvelles distributions, ni le transport des directions, ni la généralisation indépendante. Les confondants prioritaires restent : politique de contenu fixe, format/calcul, dose/style, appariement de surface, juge, plancher/ratio/graines, direction et banc, transport/dégât. La prétention « appris grâce aux raisons » n’est pas identifiable avec certitude par les seules greffes à l’inférence.

**Signature positive limitée mais informative.** À format et cohérence contrôlés, une justification pertinente doit produire un effet contrefactuel directionnel, sans simple réponse aux mots normatifs ; le comportement doit aussi transférer à des cas indépendants préjugés déductibles, sans sur-refus et sous mesure humaine/mécanique. Cela établirait une **sensibilité causale transférable au contenu justificatif**, pas encore sa médiation pendant l’entraînement.

**Expérience à faire en premier.** E0, sur les épisodes existants : sans gain validé, les tests de mécanisme sont prématurés. Si le gain survit, E1 est le premier test de mécanisme nouveau et le moins coûteux ; il exige de nouvelles générations, mais aucun réentraînement.

**Forme du papier.** Thèse : « Nous séparons robustesse du gain, contribution du contenu à l’inférence et test du regard, sans confondre ces estimands avec les raisons apprises. » Figure 1 : taux bruts et plancher, audit de mesure, puis échelle explicite des trois estimands. Sections : instruments → gains → dépendance aux mots → contenu/format → transfert → banc/transport → ablation → limites. Publier sorties, journaux d’outils, annotations, stimuli gelés, graines, code, directions et écarts de protocole. Public : alignement, évaluation agentique et interprétabilité ; canal : article avec artefacts ouverts. Ne pas affirmer « regard exclu », « raisons démontrées » ou « déploiement sûr ».

**Ce qui me ferait changer d’avis.** Disparition du gain sous audit : rétrogradation du résultat comportemental. Équivalence précise de E1 et absence de transfert : rétrogradation du contenu justificatif. Effet sélectif d’une intervention validée sur le banc : implication locale du regard. Double signature E1–E2 : revalorisation limitée au contenu utilisé à l’inférence ; seule une intervention d’entraînement appariée pourrait ensuite soutenir la version forte « apprise pendant le midtraining ».

FIN-DE-CELLULE