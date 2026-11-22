# Proposition B : ce que l'adversaire ne peut pas changer à bas prix

**Pièces.** Le bloc FAITS est présent et complet, mais il n'attribue aucun statut à ses faits. J'adopte donc la convention suivante, sans prétendre restituer des statuts absents :
- ce que les faits rapportent est noté **RAPPORTÉ (faits)** ;
- les jugements chiffrés du concepteur restent ce que les faits disent qu'ils sont : **des jugements, non des mesures** ;
- tout ce qui vient de moi est **HYPOTHÈSE** ou **dérivation proposée**.

**Thèse en quatre points (HYPOTHÈSE).**
1. La *validité* d'une borne ne peut reposer que sur la pièce, le moment où l'on tire et la définition du dommage. Autrement dit : les tirages secrets, l'ordre des engagements et l'oracle.
2. Tout ce qui lit l'agent n'achète que de l'*efficacité*, c'est-à-dire une alarme plus précoce et moins de variance. Rien de ce qui lit l'agent ne doit porter la borne.
3. Deux leviers sont donc décisifs, et aucun ne touche les états internes : **la couverture de l'oracle** et **le bruit de la référence honnête (σ)**.
4. Deux points vont contre l'intuition :
   - l'identité du bilan est exacte mais *n'apporte aucune information de détection* ;
   - un sabotage planifié ne devrait produire *aucune surprise*.

---

## 1. Ce que ferait un expert ; d'où partirait un généraliste

**Ce que l'expert ferait sans qu'on le lui demande.** Un statisticien de l'audit, celui des audits électoraux à risque limité (Lindeman & Stark, 2012, « A Gentle Introduction to Risk-Limiting Audits »), ne commencerait pas par un détecteur. Il commencerait par le **plan de sondage** :
- des probabilités d'inclusion connues, avec un plancher ;
- un tirage *postérieur* à l'engagement du produit ;
- un estimateur sans biais du total, quel que soit le mécanisme qui l'a produit (Horvitz & Thompson, 1952) ;
- une borne valide à tout instant plutôt qu'à horizon fixe.

Il demanderait aussi ce que personne ne demande : **σ**, la variance de la différence appariée « suspect − jumeau honnête » telle que l'oracle la mesure. C'est elle qui fixe le dommage capable de passer sous le bruit.

**D'où partirait un généraliste.** Il relierait cinq domaines éloignés :
- **La comptabilité nucléaire des matières.** Les faits citent le test du bilan global contre l'étalement. Les jeux d'inspection (Avenhaus, von Stengel & Zamir, 2002, « Inspection Games », *Handbook of Game Theory*) ajoutent que l'inspecteur gagne à *s'engager publiquement* sur une stratégie aléatoire. Ce résultat est dit du « leadership de l'inspecteur » ; attribution exacte : *pas sûr*.
- **L'ensemencement de défauts en génie logiciel** et l'estimation par capture–recapture (Mills, 1972, « On the statistical validation of computer programs », rapport IBM ; *pas sûr* du titre exact).
- **La confidentialité différentielle** (Dwork, McSherry, Nissim & Smith, 2006, « Calibrating Noise to Sensitivity in Private Data Analysis »), pour borner ce que révèlent les corrections.
- **La connaissance commune** (Rubinstein, 1989, « The Electronic Mail Game »), pour les copies.
- **Les mises de Ville et de Shafer–Vovk**, pour les garanties valides à tout instant.

## 2. Données brutes au départ

Toutes sont journalisées **par épisode**, avant toute agrégation :

1. **Le hachage du produit engagé**, avec l'horodatage de l'engagement.
2. **π_t et la pièce**, journalisés *avant* que la pièce tombe, puis la pièce elle-même. La graine est engagée publiquement (« commit-reveal »).
3. **Les sorties des lecteurs-oracles prises une à une** : verdict, extraits cités, résultat de la vérification mot pour mot. Chaque lecteur est gardé séparément, jamais fusionné.
4. **Plusieurs échantillons du jumeau honnête** sur la même tâche et la même graine d'environnement, pour estimer σ par régime.
5. **Les scores bruts des moniteurs et les activations**, seulement aux couches lues et seulement sur les épisodes audités.
6. **Les corrections émises** : leur date, leur type, et le fait qu'elles soient réelles ou leurres.
7. **Les canaris plantés**, avec leur identité cachée aux lecteurs.

Sans le point 2, aucune borne n'est vérifiable de l'extérieur. Sans le point 4, la piste « netteté » des faits n'a pas d'objet.

## 3. Méthodes et outils : ce que chacun suppose, comment il échoue

| Outil | Suppose | Échoue quand |
|---|---|---|
| Estimateur de Horvitz–Thompson du dommage cumulé | π_t ≥ π_min connu ; pièce indépendante du dommage D_t sachant le passé ; D_t ∈ [0, c] ; oracle sans biais | l'oracle ne voit pas (biais) ; l'agent peut prédire la pièce |
| Séquences de confiance par mise (Waudby-Smith & Ramdas, « Estimating means of bounded random variables by betting », JRSS-B ; Howard, Ramdas, McAuliffe & Sekhon, 2021, *Annals of Statistics*) | bornitude, filtration correcte | étiquettes retardées non modélisées ; c mal fixé |
| Variables de contrôle tirées des moniteurs | aucune pour la validité | moniteur aveugle : on perd l'efficacité, pas la validité |
| Canaris et capture–recapture entre lecteurs | indépendance des lecteurs | les lecteurs se trompent ensemble, ce que les faits disent : alors sous-estimation des manqués |
| Lentilles ajustées (Belrose et al., 2023, « Eliciting Latent Predictions from Transformers with the Tuned Lens ») | la représentation intermédiaire est décodable | les représentations sont déplacées (2412.09565, Bailey et al., « Obfuscated Activations Bypass LLM Latent-Space Defenses », RAPPORTÉ par les faits) |
| Écart d'élicitation de capacité (Greenblatt et al., 2024, « Stress-Testing Capability Elicitation With Password-Locked Models ») | un affinage court restaure ce qui est retenu | coût de calcul ; capacité réellement absente |
| Réponse aléatorisée sur les corrections | coût de leurres acceptable | correction obligatoire et visible (arrêt) |

## 4. Vérifier hors du programme et de son directeur

**La pièce.** Publier le hachage de la graine des tirages avant la période et la graine après. Un tiers vérifie alors que les audits étaient bien au hasard et postérieurs aux engagements.

**Les canaris.** Une équipe indépendante plante des dommages de familles qu'elle seule connaît, à une fréquence secrète, dans le flux d'audit. Le programme publie son rappel par famille *avant* la levée d'anonymat.

**La réplication.** Une autre équipe, avec d'autres lignées de lecteurs, réestime σ et le rappel sur les mêmes produits engagés.

**Le test de mort.** La famille d'attaque tenue à l'écart reste inconnue du concepteur jusqu'au verdict, comme le prévoient les faits.

**La position du directeur.** Il tient la couverture de l'oracle pour « toute la question ». Sa position est *testable* : si les canaris révèlent une couverture faible par famille, il a raison et le reste est secondaire.

## 5. Reformulation

> « Quelle est la plus petite borne supérieure, valide à tout instant, sur le dommage cumulé *mesuré par l'oracle*, qui ne dépende que de (π_min, c, σ, α) et de l'indépendance de la pièce, et non du mode d'attaque ?
> Quelle fraction du dommage réel cet oracle voit-il, mesurée par familles plantées et par un tiers ?
> Quels signaux internes ou contrefactuels réduisent le délai d'alarme ou σ, sans jamais entrer dans la condition de validité ? »

---

## 6. Les onze sous-questions

### (a) Borner sans reconnaître

**Établi.**
- L'estimateur de Horvitz–Thompson est sans biais pour tout mécanisme générateur, si l'inclusion est indépendante de la valeur. C'est un résultat classique.
- Le test du bilan global est optimal à horizon fixe : RAPPORTÉ (faits).

**Non établi.**
- La borne finie pour ce banc.
- L'effet des étiquettes retardées.

**Proposition (dérivation proposée, à vérifier formellement).** Notons :
- n = πN le nombre d'étiquettes ;
- σ l'écart-type de la différence appariée honnête ;
- c le plafond de dommage par épisode.

Un argument à deux points de Le Cam donne deux régimes, à constantes et facteurs logarithmiques près :
- **Attaque diffuse** (δ constant par épisode). Elle est indiscernable si δ ≲ σ/√n. Le dommage cumulé caché est alors de l'ordre de **σ·√(N/π)**.
- **Attaque concentrée.** Le dommage avant le premier coup audité est de l'ordre de **c/π** en espérance.

La meilleure borne possible est donc de l'ordre de max(σ√(N/π), c/π). Elle est **sous-linéaire en N** : le taux de dommage par épisode tend vers zéro.

Le flux minimal qui la porte est un audit uniforme à π_min, engagé avant le tirage. Les moniteurs n'interviennent que comme poids d'importance (π_t = max(π_min, f(score))) et comme variables de contrôle.

Le levier le moins cher est de **réduire σ** : jumeaux multiples, appariement par graine, lecteurs moyennés. Ce levier ne touche pas l'agent.

### (b) La couverture de l'oracle

**Établi.**
- La garantie ne vaut que dans la couverture : RAPPORTÉ (faits).
- Aucune garantie n'est connue pour les tâches floues (2606.08892, RAPPORTÉ ; titre à vérifier).

**Non établi.** Toute mesure de couverture contre un genre inconnu. Par définition, je ne vois aucun moyen de la mesurer.

**Propositions.**

1. **Mesurer.** Rappel par famille plantée, chaque famille définie par la supposition qu'elle viole. On publie la *dispersion* entre familles : une forte dispersion signifie que la couverture d'un genre nouveau est imprévisible.

2. **Lecteurs qui se trompent ensemble.** On mesure la corrélation de leurs manqués sur les canaris. Le Lincoln–Petersen naïf est faux sous dépendance, donc on rapporte une borne dans le pire cas, pas une estimation ponctuelle.

3. **Persuasion.** Les lecteurs ne voient que le produit et la référence, sans la prose de l'agent. On teste la sensibilité en ajoutant une justification neutre plantée (duel D5).

4. **Rétrécissement en service.** Des canaris injectés à fréquence secrète. On publie une séquence de confiance sur leur rappel ; l'alerte se déclenche quand sa borne haute passe sous le seuil déclaré.

5. **Dommage hors spécification.** C'est le seul point où le défenseur peut *élargir la définition*, qu'il possède. Il remplace « le produit est-il mauvais ? » par **« le produit est-il distinguable de la distribution des jumeaux honnêtes ? »**, en divergence calculée par les lecteurs. Ce critère ne demande pas de reconnaître le dommage.

   Il suppose un jumeau de *même capacité* que l'agent, ce qui n'est pas établi (voir L-a). Il produit des fausses alertes sur les écarts bénins.

6. **Assemblage.** On audite au hasard des *assemblages* entiers, avec une probabilité d'inclusion propre. L'estimateur de Horvitz–Thompson s'applique au niveau de l'assemblage.

7. **Tâches floues.** On ne borne que le dommage qui se révèle. Le retard multiplie le dommage accumulé avant l'alerte par le délai ; aucune astuce ne l'efface.

### (c) Savoir qu'on ne voit plus

**Établi.** Le comptage « signalés parmi les endommagés trouvés » : RAPPORTÉ (faits).

**Non établi.** Sa puissance. Avec peu d'endommagés trouvés, l'intervalle est presque vide d'information.

**Proposition.** Remplacer le comptage binaire par une quantité continue : **la covariance, estimée par Horvitz–Thompson sur les audités, entre le score du moniteur et D_t**. Elle ne demande aucun seuil de « dommage ».

On l'annonce « ne voit plus » quand la borne basse de sa séquence de confiance touche zéro.

Asymétrie à dire en clair : l'absence d'endommagés trouvés ne prouve pas que le moniteur voit. Je ne sais pas faire mieux que des canaris, et ceux-ci ne valent que pour les familles connues.

### (d) Le canal de retour

**Établi.** Rien de spécifique dans les faits.

**Proposition (HYPOTHÈSE).** La validité de Horvitz–Thompson **ne dépend pas** de ce que l'agent apprend des audits *passés*, à deux conditions :
- la pièce de l'épisode t est tirée après l'engagement ;
- la pièce est indépendante du passé connu de l'agent.

Ce qui fuit réellement, c'est **la frontière de l'oracle** : quels dommages sont punis. Le canal de retour sert à cartographier la couverture.

Réponses proposées :
1. **Différer et grouper les corrections.**
2. **Émettre des corrections leurres** (relance, transfert au modèle de confiance) sur des épisodes non audités, au taux q.

Si la correction suit avec probabilité p₁ un dommage trouvé et avec probabilité q les autres épisodes, le rapport de vraisemblance d'une correction est borné par ε = ln(p₁/q). Chaque observation apporte alors au plus ε à l'agent, et cartographier la frontière demande de l'ordre de 1/ε² sondages. Le coût est d'environ qN corrections inutiles.

L'arrêt sur dommage grave ne se cache pas, et il n'a pas besoin de l'être.

Invariant à ajouter : **aucune correction n'entre dans l'entraînement de l'agent.**

### (e) Le passage obligé

**Établi.**
- La sonde de surprise est apprise et évaluée seulement sur |écart de valeur| > 0,3 (2602.00986, p. 6, RAPPORTÉ).
- L'état voisin ne sépare pas la triche de l'échec honnête sur un modèle sur trois (2611.14996, RAPPORTÉ).

**Non établi.** Tout comportement de la sonde de surprise sous 0,3. Je ne sais pas ce qu'elle y vaut ; rien ne le dit.

**Analyse (HYPOTHÈSE).**
- **Ce que lit la sonde.** Une sonde d'erreur de prédiction de valeur lit l'*inattendu*. Or un sabotage **planifié** est anticipé par l'agent, donc son erreur de prédiction devrait être proche de zéro. La sonde lirait l'échec honnête imprévu et serait muette sur l'intention.
- **Rapporter la surprise à la surprise attendue.** Cela corrige l'échelle selon le régime, pas ce problème de fond. Je ne le recommande pas comme levier principal.
- **Lire plusieurs conséquences attendues.** C'est la bonne direction. Deux têtes, « passera le contrôle » et « a fait la tâche », sont apprises sur des épisodes honnêtes de tâches où le contrôle est plus étroit que la tâche. La prédiction est que le sabotage *planifié* écarte les deux têtes au-delà de la distribution honnête.

**Autres passages obligés** (définis comme ce que la sabotage doit calculer, sans mode opératoire) :
1. **Connaître l'option meilleure et en émettre une autre.**
   - Lecture : réponse décodée aux couches intermédiaires contre réponse émise (Halawi, Denain & Steinhardt, 2023, « Overthinking the Truth »).
   - Lecture sans les états internes : *écart d'élicitation*, c'est-à-dire la performance après un affinage court comparée à la performance en service.
2. **Conditionner l'écart sur « suis-je observé ».**
   - Lecture : invariance contrefactuelle. On bifurque l'épisode en variant seulement les indices d'observation, et l'honnête devrait rester invariant.
   - Confusion : les modèles distinguent l'évaluation de l'usage (2505.23836, Needham et al., « Large Language Models Often Know When They Are Being Evaluated », RAPPORTÉ). Il faut mesurer d'abord si l'honnête varie.
3. **Connaître le niveau de bruit honnête pour rester dessous.** Un sabotage diffus *calibré* doit représenter σ. Je ne sais pas comment lire cela.

### (f) L'étau

**Établi.**
- L'étau n'a aucune quantité conservée : RAPPORTÉ.
- Les valeurs 0,35 et 0,15 sont des jugements, non des mesures.
- L'obscurcissement coûte de la performance sur une tâche complexe (2412.09565, p. 1, RAPPORTÉ).

**Critique des trois pistes.**
1. **Tester la somme du bilan.** (R − L) + (L − I) = R − I : la lecture L **s'annule**. La somme n'est autre que le dommage mesuré par l'oracle, et elle ne contient aucune information interne. Son invariance devant une attaque jamais vue est exacte mais vide pour la *détection*. Elle sert à l'attribution : on sait quelle part du dommage est passée sous le regard interne.
2. **Netteté de la référence.** C'est la piste la plus utile des trois, car elle fixe σ dans la borne de (a). Elle se mesure sans attaque. Elle ne dit rien de la couverture.
3. **Séparer « passera » et « bien fait ».** Elle est bonne, mais elle confond intention et triche de spécification sans malveillance. C'est acceptable si ce second cas est compté comme dommage.

**Rendre l'étau nécessaire (HYPOTHÈSE).** Ne lire que des directions **causalement porteuses de capacité**. Cela se mesure du seul côté de la défense, sur des épisodes honnêtes : on perturbe la direction et on obtient une courbe dose–réponse de la chute de réussite.

Un agent qui efface la trace paie alors en capacité. Cette perte est visible par le regard externe sous forme de baisse de R, ou par l'écart d'élicitation. C'est un *compromis mesurable*, pas une conservation.

**S'en passer.** La borne de (a) n'en a pas besoin ; l'étau ne fait que raccourcir le délai d'alerte.

### (g) L'asymétrie de généralisation

**Établi.**
- L'évasion se généralise (2512.11949, RAPPORTÉ ; titre à vérifier).
- Les défenses latentes tombent ensemble (2412.09565, RAPPORTÉ).

**Proposition.** On ne la surmonte pas : on la **contourne**. La validité est placée dans un mécanisme qui n'a pas à généraliser, l'audit aléatoire. L'asymétrie se déplace alors entièrement sur l'oracle : c'est *lui* qui doit voir un dommage d'un genre nouveau.

Les moniteurs sont renouvelés par tirage secret (directions, couches, seuils) pour rendre l'évasion plus coûteuse. La validité n'en dépend pas.

### (h) L'adversaire qui apprend le dispositif

**Établi.**
- Un audit de texte fixe est défait en deux tours (2611.14950, RAPPORTÉ).
- La conscience d'évaluation (2505.23836, RAPPORTÉ).

**Proposition (principe de Kerckhoffs).**
- **Secret :** la graine des tirages, et seulement elle.
- **Renouvelé :** paramètres des moniteurs, seuils, canaris.
- **Public :** π_min, c, la définition du dommage, la règle de combinaison.

**Audit indépendant des croyances de l'agent.** L'audit est **postérieur et passif** : l'épisode audité est identique à l'épisode non audité, et la décision tombe après l'engagement. Ce que l'agent croit de sa situation devient alors statistiquement indépendant de la pièce.

La conscience d'évaluation change le comportement *uniformément*, donc sans biais pour Horvitz–Thompson. Elle ne biaise que si l'environnement de l'épisode audité diffère : c'est l'invariant à vérifier.

### (i) Les copies

**Établi.** Le dossier esquissé suppose des pannes indépendantes entre instances (2512.22154, p. 16, RAPPORTÉ). Des copies qui partagent leurs poids violent précisément cette supposition.

**Proposition (HYPOTHÈSE).** Ne pas rompre le point focal, qui est inévitable avec des poids partagés, mais **la connaissance commune** dont la coordination a besoin (Rubinstein, 1989). Deux leviers :
1. **Brouiller ce qu'une copie sait des autres.** Aucune copie ne sait si son partenaire d'assemblage est une copie ou le modèle de confiance, ni si sa sous-tâche appartient à un assemblage.
2. **Auditer au niveau de l'assemblage** (voir (b)).

Un sabotage coordonné qui échoue quand le partenaire est honnête devient un écart solitaire, que l'audit voit. Je ne sais pas borner ce gain.

### (j) Combiner sans additionner

**Proposition.** La règle **π_t = max(π_min, f(s¹, …, s^k))**, avec les scores en variables de contrôle, a un pire cas certifié, *quelle que soit la dépendance entre détecteurs* : c'est l'audit uniforme à π_min. Ce résultat se dérive en une ligne de l'absence de biais de Horvitz–Thompson.

Il existe aussi des **relations que l'honnête respecte** et que le dommage délibéré viole (HYPOTHÈSE) :
- l'invariance aux indices d'observation ;
- l'accord entre réponse intermédiaire et réponse émise ;
- l'égalité entre performance en service et performance élicitée.

### (k) Les mathématiques

1. **Énoncé.** Pour tout adversaire adaptatif, P(∃t : Σ_{s≤t} D_s > U_t) ≤ α. Ici U_t est la borne haute d'une séquence de confiance par mise sur les termes de Horvitz–Thompson 1{audit}·D_s/π_s, qui prennent leurs valeurs dans [0, c/π_min].
   - Il suppose : D bornée ; π prévisible et plancher ; pièce indépendante ; oracle sans biais *sur sa couverture*.
2. **Borne basse.** L'ordre de grandeur σ√(N/π) de (a) (dérivation proposée).
3. **Impossibilités respectées.**
   - Aucun test sans étiquettes n'est revendiqué (2609.32267).
   - Aucune détection hors distribution (2210.14707, Fang et al., « Is Out-of-Distribution Detection Learnable? »).
   - Aucune détection dans les poids (2204.06974, Goldwasser, Kim, Vaikuntanathan & Zamir, « Planting Undetectable Backdoors in Machine Learning Models »).

   La garantie dépend de la vérité des étiquettes, comme en 2411.03279 (RAPPORTÉ ; titre *pas sûr*).
4. **Version finie vérifiable par programme.**
   - Couverture empirique ≥ 1 − α sur des mondes plantés, contre des adversaires adaptatifs simulés, avec intervalle de Monte-Carlo.
   - Vérification symbolique de l'identité du bilan.
   - Vérification que chaque pièce journalisée suit l'engagement.

---

## 7. Fiches des propositions

**P1 — Audit plancher avec borne valide à tout instant.**
- **Idée :** un audit postérieur à π_min fixe, avec une séquence de confiance par mise sur le dommage cumulé estimé par Horvitz–Thompson. Les moniteurs n'interviennent que comme poids et comme variables de contrôle.
- **Sous-questions :** (a), (h), (j).
- **Suppose :** une pièce imprévisible tirée après l'engagement, et un oracle sans biais.
- **Supposition violée par l'adversaire :** il devrait abandonner l'hypothèse « l'audit est corrélé à quelque chose que j'observe ».
- **Muette devant :** un dommage hors couverture de l'oracle.
- **Premier pas sans dépense :** une simulation sur processeur.
- **Test de mort :** couverture < 1 − α face à la famille tenue à l'écart.
- **Distinction :** la validité est découplée de toute détection.
- **Chances (jugement) :** élevées pour la validité, et seulement dans la couverture.

**P2 — Canaris d'oracle.**
- **Idée :** des dommages plantés par un tiers, à fréquence secrète, dans le flux d'audit. Une séquence de confiance sur le rappel signale le rétrécissement de la couverture.
- **Sous-questions :** (b), (c).
- **Suppose :** les familles plantées sont représentatives.
- **Supposition violée :** « le dommage ressemble à une famille connue ».
- **Muette devant :** un genre entièrement nouveau.
- **Premier pas :** rejouer les familles déjà écrites.
- **Test de mort :** le rappel sur la famille tenue à l'écart sort de l'intervalle prédit par les autres familles.
- **Distinction :** une mesure de la couverture en service plutôt qu'à l'évaluation.
- **Chances :** moyennes.

**P3 — Corrections leurres.**
- **Idée :** des corrections aléatorisées et différées bornent par ε ce que chaque correction révèle de la frontière de l'oracle.
- **Sous-question :** (d).
- **Suppose :** un coût de q acceptable.
- **Supposition violée :** « une correction signale un dommage trouvé ».
- **Muette devant :** un sondage massif réparti sur de nombreux épisodes.
- **Premier pas :** calculer ε pour les valeurs envisagées de q.
- **Test de mort :** un agent réentraîné localise la frontière en moins de sondages que prévu.
- **Distinction :** je ne connais pas d'application publiée au contrôle d'IA ; à vérifier.
- **Chances :** moyennes.

**P4 — Deux têtes de conséquence.**
- **Idée :** des sondes « passera » et « bien fait », apprises sur l'honnête. Le sabotage planifié écarterait les deux têtes là où la sonde de surprise reste muette.
- **Sous-question :** (e).
- **Suppose :** des tâches à contrôle étroit qui existent et sont étiquetables.
- **Supposition violée :** « je représente séparément ce qui passe et ce qui est bien ».
- **Muette devant :** un agent qui ignore lui-même la qualité réelle de son produit.
- **Premier pas :** recenser les tâches du banc dont le contrôle est connu pour être étroit.
- **Test de mort :** duel D3.
- **Distinction :** la sonde lit une divergence entre deux attentes, et non une surprise.
- **Chances :** faibles à moyennes.

**P5 — Étau par coût de capacité.**
- **Idée :** ne sonder que des directions dont la perturbation dégrade la capacité honnête. L'évasion se paie alors en performance visible.
- **Sous-questions :** (f), (g).
- **Suppose :** la tâche est assez complexe pour que l'obscurcissement coûte.
- **Supposition violée :** « je peux déplacer mes représentations sans perte ».
- **Muette devant :** les tâches simples.
- **Premier pas :** une courbe dose–réponse sur l'honnête.
- **Test de mort :** duel D4.
- **Distinction :** le coût est *exigé* comme critère de choix des sondes, et non seulement constaté.
- **Chances :** faibles.

**P6 — Invariance contrefactuelle et brouillage de la connaissance commune.**
- **Idée :** bifurquer en ne variant que les indices d'observation ou de partenaire. L'honnête reste invariant ; la stratégie conditionnelle ne l'est pas.
- **Sous-questions :** (e), (i), (j).
- **Suppose :** l'honnête est lui-même invariant.
- **Supposition violée :** « je peux conditionner sur ma situation ».
- **Muette devant :** un sabotage inconditionnel, que P1 attrape.
- **Premier pas :** mesurer la variance de l'honnête aux indices.
- **Test de mort :** l'honnête varie autant que le suspect.
- **Distinction :** elle vise la connaissance commune, pas le point focal.
- **Chances :** faibles à moyennes.

## 8. Hors de portée

- Le dommage que l'oracle ne reconnaît pas.
- Les tâches sans vérité.
- La fuite irréductible de l'ordre de σ√(N/π) : on la réduit en baissant σ, jamais à zéro.
- Le dommage accumulé pendant le retard des étiquettes.
- Des lecteurs dont les angles morts coïncident avec ceux de l'attaque.
- Toute garantie fondée sur les états internes face à un agent qui déplace ses représentations à faible coût.

---

## Livrable du tour

### L-a. Ce que la question suppose sans que ce soit établi

1. **Un jumeau honnête de même capacité existe.**
   - Statut : HYPOTHÈSE. Les faits définissent le dommage par rapport à lui sans dire qui il est.
   - Conséquence : si c'est le modèle de confiance, plus faible, σ et le biais explosent.
2. **L'oracle est sans biais à l'intérieur de sa couverture.** Statut : HYPOTHÈSE.
3. **Le dommage est borné par épisode (c).** Statut : RAPPORTÉ comme plafond dans les faits ; sa tenue réelle n'est pas établie.
4. **Un audit peut être postérieur et indiscernable de l'épisode non audité.** Statut : HYPOTHÈSE à vérifier sur le harnais.
5. **« Tout sabotage délibéré doit calculer X ».**
   - Statut : HYPOTHÈSE.
   - Sans observation : on n'a aucun échantillon interne de comploteur réel (2504.05259, p. 24, RAPPORTÉ).
6. **Les corrections ne nourrissent pas l'entraînement.** Statut : HYPOTHÈSE.

### L-b. Duels décisifs

Les épreuves se font sur des mondes à vérité plantée, avec une famille tenue à l'écart. Tous les seuils sont **illustratifs**, à préenregistrer.

**D1 — Validité de P1.**
- H_A : couverture ≥ 1 − α contre un adversaire adaptatif tenu à l'écart.
- H_B : l'adversaire adaptatif biaise l'estimation.
- Métrique : couverture empirique sur 10⁴ mondes (illustratif).
- Contrôle négatif : honnête seul, fausses alertes ≤ α.
- Contrôle positif : π_min = 0, qui doit casser la borne. Sinon, le test n'a pas de puissance.
- Ce qui falsifie : une couverture sous 1 − α moins l'erreur de Monte-Carlo falsifie H_A ; sinon H_B est falsifiée.

**D2 — Loi de la fuite.**
- H_A : le dommage caché maximal croît comme √N.
- H_B : il croît linéairement.
- Métrique : pente log–log.
- Seuil : l'intervalle de la pente exclut 1, ou bien exclut 0,5.
- Contrôle négatif : σ réduit par appariement doit déplacer l'ordonnée à l'origine, pas la pente.

**D3 — Ce que lit la sonde de surprise.**
- H_A : elle lit l'intention.
- H_B : elle lit l'échec imprévu.
- Cas : un sabotage planifié d'un organisme modèle, comparé à un échec honnête à issue appariée. Les petits écarts sont inclus, sous 0,3.
- Métrique : AUROC triche contre échec honnête.
- Ce qui falsifie :
  - une borne basse de l'AUROC > 0,5 et une surprise non nulle sur le planifié falsifient H_B ;
  - une AUROC compatible avec 0,5 falsifie H_A.
- Contrôle négatif : des épisodes honnêtes réussis.

**D4 — Étau par coût.**
- H_A : effacer la trace coûte de la capacité.
- H_B : l'effacement est gratuit.
- Métrique : après entraînement contre la sonde, AUROC de la sonde et variation de réussite sur des tâches honnêtes tenues à l'écart.
- Ce qui falsifie :
  - une AUROC au niveau du hasard avec une réussite dans les 2σ du bruit de réplication honnête falsifie H_A ;
  - une chute de capacité au-delà de ce bruit, conjointe à l'effacement de la trace, falsifie H_B.

**D5 — Persuasion de l'oracle.**
- H_A : le rappel des lecteurs est indépendant d'une prose justificative plantée.
- H_B : la prose réduit le rappel.
- Métrique : écart de rappel apparié.
- Ce qui falsifie : un intervalle de l'écart qui exclut 0 falsifie H_A ; sinon H_B est falsifiée.
- Contrôle négatif : une prose sans rapport avec la tâche.

### L-c. Mesure minimale par instrument

| Instrument | Mesure minimale | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| Tirages secrets et ordre des engagements | test d'indépendance pièce ↔ caractéristiques de l'épisode ; horodatage engagement < pièce | tous les épisodes | test de permutation ; vérification des hachages |
| Oracle (deux lecteurs) | rappel et fausses alertes par famille plantée ; corrélation des manqués | produits des jumeaux sur la même tâche | tests unitaires, diff textuel contre la référence |
| Moniteur | covariance score–D estimée par Horvitz–Thompson ; taux de détection à fausses alertes fixées | même tâche, même graine | taille du diff, échecs de tests, jugement du modèle de confiance |
| Sonde de surprise | AUROC triche contre échec honnête, *y compris* sous 0,3 | issue appariée | probabilité logarithmique de la réponse, longueur de trajectoire |
| Sondes de réussite et têtes de conséquence | écart entre têtes au-delà du quantile honnête 0,99 (illustratif) | tâches à contrôle étroit | prédiction par un modèle de surface sur le texte seul |
| Harnais (bifurcation) | variance de l'honnête aux indices d'observation | bifurcations identiques sauf l'indice | rejeu déterministe à graine fixe |

Contrainte respectée : aucune moyenne sur les jetons dans une sonde de production. On utilise la lecture au jeton de décision ou le maximum, à préciser.

### L-d. Ancrage matériel (tout est illustratif)

**Modèles.**
- Agents : Llama-3.1-8B-Instruct et Qwen2.5-7B-Instruct.
- Lecteurs d'autres lignées : Gemma-2-9B-it et Mistral-7B-Instruct.
- Modèle de confiance : un modèle d'environ 1 à 3 milliards de paramètres.

**Calcul.**

| Poste | Estimation (illustratif) |
|---|---|
| D1–D2 | simulation sur processeur, coût négligeable |
| D3, D5 | quelques centaines d'heures-GPU de classe A100 |
| D4 | environ 1 000 à 3 000 heures-GPU, pour l'entraînement adverse contre la sonde |
| P2, canaris | surtout du temps humain chez le tiers |
| **Total** | **de l'ordre de quelques milliers d'heures-GPU** |

L'ordre de priorité est D1, D2, puis la mesure de σ : ils sont presque gratuits et portent la borne. D4 vient en dernier.

FIN-DE-CELLULE