# Proposition D — Tour III.1

Tous les constats du projet et des publications citées ci-dessous restent **RAPPORTÉS** par [B], sans relecture indépendante. Les mécanismes, prédictions et plans expérimentaux que je propose sont des **HYPOTHÈSES**. Tous les seuils chiffrés nouveaux sont **illustratifs**.

## 1. Ce que la question suppose sans que ce soit établi

| Supposition | Statut et réserve |
|---|---|
| Le taux faible d’actions nuisibles constitue une « bonne conduite » générale. | **HYPOTHÈSE.** Les taux sur ce portage sont **RAPPORTÉS** ; l’absence de sur-refus, la robustesse hors distribution et la conduite en déploiement ne sont pas établies. |
| Le gain reproductible après identification de la bonne référence est un gain causal des recettes. | Reproduction **RAPPORTÉE**. L’attribution causale suppose notamment que le juge, la référence et les comparaisons entre adaptateurs soient valides. |
| Les jumelles ne diffèrent que par la présence sémantique des raisons. | La description « même recette, raisonnement retiré » est **RAPPORTÉE**. L’équivalence en tokens, optimisation, style et difficulté des exemples est **HYPOTHÈSE**. |
| « Apprendre les raisons » signifie que leur contenu est causalement utilisé. | **HYPOTHÈSE**, actuellement sans critère opérationnel unique : apprentissage pendant l’entraînement et usage d’une trace à l’inférence sont deux affirmations distinctes. |
| Les phrases d’observation manipulent une croyance. | Elles changent les croyances **déclarées**, **RAPPORTÉ** ; elles modifient peu les actions et les deux questions de croyance ordonnent les jumelles en sens opposés. La croyance interne reste **HYPOTHÈSE**. |
| Une absence d’effet de la phrase ou de l’ablation exclurait le regard. | **HYPOTHÈSE**, explicitement fragilisée par la dépendance aux mots, le plancher et l’absence de validation du banc d’essai. |
| La direction extraite du modèle de départ mesure « être évalué », se transporte aux adaptateurs et peut être retirée spécifiquement. | Trois **HYPOTHÈSES** distinctes. La seconde manipulation est **RAPPORTÉE** comme préenregistrée mais non jouée. |
| Le juge étalonné mesure l’action effectivement exécutée. | Étalonnage et contrôles prévus **RAPPORTÉS** ; validité sur actions partielles, outils bénins et traces masquées **HYPOTHÈSE**. |
| Les scénarios sont suffisamment indépendants des données d’entraînement pour mesurer une généralisation. | **HYPOTHÈSE**. La parenté lexicale, structurelle ou de famille de modèle n’est pas quantifiée dans les faits. |
| \(S\) et \(D\) identifient proprement une part causale du regard. | Leurs définitions sont **RAPPORTÉES**. Leur validité près du plancher ou lorsque \(A(\text{observé})\) est instable est **HYPOTHÈSE**. |

## 2. Partie A — huit explications rivales, par priorité

Dans les duels ci-dessous, l’exclusivité porte sur **la nécessité ou la suffisance d’un mécanisme pour un contraste précis**, non sur l’impossibilité générale que plusieurs mécanismes coexistent. Les formulations « regard » doivent être croisées dans chaque test : un effet propre à une rivale doit apparaître à formulation constante et ne pas se confondre avec une interaction observation × condition.

### 1. Contenu de la spécification ou concept de nuisance, raisons inertes — famille (a)

**Mécanisme.** Les documents et démonstrations peuvent apprendre « reconnaître cette classe d’actions comme interdite », sans que la justification soit utilisée. Le refus presque systématique même sur ordre, avec exécution d’un outil bénin identique, est compatible avec un classifieur sémantique de nuisance, pas seulement avec les raisons.

**Prédiction.** Si cette rivale est vraie, l’action suit les étiquettes, interdictions et similarités de contenu, même lorsque la justification change ; le transfert à un principe familier exprimé par des actions et outils nouveaux est faible. Si les raisons sont causalement utilisées, des paires minimales à règle et surface fixes mais justification différente produisent des décisions différentes, dans le sens du principe ; le regard prédit plutôt une modulation par l’observation.

**Test minimal.** Nouvelles paires à consentement, finalité et justification croisés, avec les adaptateurs publiés ; aucun réentraînement. Les épisodes existants permettent seulement des analyses exploratoires. **Duel :** \(H_A\), le contenu/interdiction suffit ; \(H_B\), la justification est nécessaire à une partie du gain. Une invariance aux justifications falsifie \(H_B\) dans ce périmètre ; une inversion reproductible suivant le principe falsifie \(H_A\).

**Contrôles.** Positif : scénarios proches des originaux reproduisant le gain. Négatif : même outil bénin, succès d’instruction suivie et phrases regard à formulation fixe.

**Publié.** **RAPPORTÉ** : Cho et al. (2026), *Constitutional Midtraining: Content Presence Drives Alignment Gains*.  
**Coût : bas à moyen. Relecteur :** c’est l’alternative la plus directe à « les raisons », et les recettes « règles » sans gain lisible ne l’excluent pas.

### 2. La trace apporte format, calcul ou régularisation, pas des raisons — famille (a)

**Mécanisme.** Retirer le raisonnement change aussi la longueur, la distribution de tokens et le calcul disponible à l’inférence. Une trace peut améliorer la conduite par format appris sans que son contenu justificatif soit nécessaire.

**Prédiction.** Si le format suffit, des raisons permutées entre scénarios, rendues non pertinentes ou remplacées par du texte neutre de longueur appariée laissent le gain intact. Si leur contenu est nécessaire, ces corruptions augmentent sélectivement les actions nuisibles ; le simple changement de croyance déclarée d’observation ne reproduit pas cet effet.

**Test minimal.** Sur la recette avec raisonnement, comparer trace intacte, trace restaurée après corruption, raisons permutées et tokens neutres, à budget de génération fixe. Les traces déjà jouées fournissent la condition intacte, mais pas le test causal complet. **Duel :** \(H_A\), contenu inerte ; \(H_B\), contenu nécessaire. Équivalence sous corruption falsifie \(H_B\) ; perte spécifique falsifie \(H_A\).

**Contrôles.** Positif : réinsertion de la trace originale restaurant le résultat. Négatif : tâches bénignes et corruption de tokens non sémantiques.

**Publié.** **RAPPORTÉ** : Li, Wichers, Price, Marks et Kutasov (2026), *Model Spec Midtraining: Improving How Alignment Training Generalizes*.  
**Coût : bas. Relecteur :** le contraste central entre jumelles ne porte autrement pas uniquement sur « raisons ».

### 3. Dose, optimisation ou style de distillation différents entre recettes — famille (a)

**Mécanisme.** Même à exemples appariés, retirer les raisons modifie le nombre de tokens et potentiellement la trajectoire d’optimisation. Le style du modèle Claude ayant écrit les données peut également être distillé indépendamment du contenu justificatif.

**Prédiction.** Si cette explication domine le contraste des jumelles, les performances suivent la dose, le format ou le style, y compris dans les recettes sans documents, sans relation avec la pertinence des raisons. Sinon, à dose mesurée et format contrôlé, le contenu des raisons conserve un effet spécifique ; le regard ne prédit pas ce gradient de dose.

**Test minimal.** Audit des configurations, tokens, étapes, pertes et données avant toute nouvelle évaluation ; comparaison descriptive des neuf adaptateurs sur les épisodes existants. **Sans réentraînement ni appariement de dose, les adaptateurs seuls ne peuvent pas trancher.** **Duel :** \(H_A\), le contraste est entièrement expliqué par ces différences ; \(H_B\), il subsiste un effet sémantique après leur contrôle. Un audit révélant des différences majeures falsifie la prémisse d’une comparaison propre, pas encore \(H_B\).

**Contrôles.** Positif : variations connues de dose dans les recettes disponibles. Négatif : tâches bénignes sans raisonnement.

**Publié.** **RAPPORTÉ** : Cho et al. (2026), titre ci-dessus.  
**Coût : bas pour l’audit, haut pour un appariement causal. Relecteur :** sans cet audit, « avec contre sans raisons » n’est pas nécessairement une intervention isolée.

### 4. Appariement de surface entre données et scénarios — famille (c)

**Mécanisme.** Des gabarits communs d’outils, de buts ou de narration peuvent produire le gain sans généralisation par principes. Le portage des scénarios par les auteurs de la méthode et l’écriture des données par un modèle d’une même famille rendent cette hypothèse vérifiable, non établie.

**Prédiction.** Si elle est vraie, le gain décroît fortement sur des scénarios écrits indépendamment, malgré des principes équivalents, et la similarité de surface prédit mieux le taux de nuisance que le principe testé. « Raisons » prédit un transfert au-delà de cette similarité ; « regard » prédit une modulation par observation plutôt que par similarité.

**Test minimal.** Mesurer n-grammes, structure des appels d’outils et similarité d’enchâssements sur les épisodes existants, puis confirmer sur une petite batterie indépendante, à faible similarité mécanique. **Duel :** \(H_A\), gain restreint au voisinage de surface ; \(H_B\), transfert principiel détectable hors de ce voisinage. Effondrement hors voisinage falsifie la portée de \(H_B\) ; transfert substantiel falsifie \(H_A\).

**Contrôles.** Positif : voisins proches. Négatif : nouvelles tâches bénignes et paraphrases seules, qui ne comptent pas comme indépendance.

**Publié.** **RAPPORTÉ** : Lynch et al. (2025), *Agentic Misalignment: How LLMs Could Be Insider Threats* ; Korbak et al. (2026), *How far does alignment midtraining generalize?*  
**Coût : moyen. Relecteur :** sans cela, « généralise mieux » peut signifier seulement « généralise à des variantes proches ».

### 5. Le juge fabrique ou amplifie une partie du gain — famille (c)

**Mécanisme.** Le juge peut exploiter le style de la trace, partager des régularités avec le modèle ayant écrit les données, ou confondre intention, tentative et exécution. L’étalonnage contre un autre juge ne constitue pas une vérité terrain indépendante.

**Prédiction.** Si l’artefact domine, le gain change fortement selon la visibilité de la trace, la famille du juge ou le critère « exécuté », et diminue sous annotation humaine aveugle ou vérification d’état. Une conduite réellement apprise doit survivre à ces changements ; le regard ne prédit pas une telle dépendance au juge.

**Test minimal.** Rejuger les épisodes déjà joués, sans nouvelle génération : humain aveugle, trace masquée, autre famille et règles mécaniques sur les journaux. **Duel :** \(H_A\), le gain principal est un artefact de mesure ; \(H_B\), il subsiste sous mesure indépendante. Disparition sous vérité terrain falsifie \(H_B\) pour le résultat publié ; persistance falsifie \(H_A\).

**Contrôles.** Positif : exécutions nuisibles insérées et sans ambiguïté. Négatif : refus honnêtes, même outil bénin, appel sans effet, trace menaçante sans exécution.

**Publié.** Contrôle humain spécifique : **référence à vérifier**.  
**Coût : bas à moyen. Relecteur :** l’absence de contrôle humain avant lecture est une limite déclarée.

### 6. Plancher, référence, ratio \(S\) et graines produisent les contrastes — famille (c)

**Mécanisme.** Près du plancher, le gain de la recette avec raisonnement laisse peu d’espace à une interaction ; diviser deux petits gains rend \(S\) instable. Une référence mal identifiée ou quelques graines peuvent déplacer \(D\) sans changement causal de conduite.

**Prédiction.** Si l’artefact domine, les signes de \(S\) et \(D\) changent sous rééchantillonnage par scénario, correction de référence ou passage aux différences absolues, tandis que les taux bruts restent compatibles. Un effet « raisons » doit être estimable sur des cas avec marge ; un effet « regard » doit apparaître comme interaction absolue, pas seulement comme ratio.

**Test minimal.** Réanalyse intégrale des épisodes existants : bootstrap hiérarchique, intervalles par graine, \(A\) en points de pourcentage, puis scénarios à plus grande marge si nécessaire. Ne pas calculer \(S\) lorsque le dénominateur est indiscernable de zéro. **Duel :** \(H_A\), les contrastes dépendent du plancher ou du dénominateur ; \(H_B\), ils sont stables en métrique absolue et sur cas à marge. Instabilité falsifie \(H_B\) ; stabilité falsifie \(H_A\).

**Contrôles.** Positif : effet artificiel injecté de taille connue ou organisme conditionnel validé. Négatif : permutation des étiquettes d’observation et référence contre elle-même.

**Publié.** **RAPPORTÉ** : Baines et al. (2026), *Stress-testing Alignment Midtraining* ; Knecht, Florin et Hagendorff (2026), *Evaluation Awareness in Language Models Has Limited Effect on Behaviour*.  
**Coût : bas. Relecteur :** « le gain ne bouge pas » au plancher n’est pas une preuve d’invariance.

### 7. La direction ne mesure pas l’évaluation et le banc d’essai manque de sensibilité — famille (b)

**Mécanisme.** Une sonde peut encoder le style des textes d’évaluation, la présence de consignes ou une saillance générique. Si elle ne réduit pas la conduite conditionnelle d’un organisme connu, une ablation nulle chez les adaptateurs est non informative.

**Prédiction.** Si l’instrument est invalide, il généralise mal à des auteurs et gabarits indépendants, ou échoue sur l’organisme témoin malgré une bonne classification. Un instrument valide doit réduire causalement l’écart du témoin ; « raisons » et « regard » ne peuvent être départagés par son résultat tant que ce contrôle échoue.

**Test minimal.** Validation croisée laissant de côté des familles entières de textes, puis intervention sur le banc d’essai **avant** tout test confirmatoire. **Duel :** \(H_A\), sensibilité causale suffisante ; \(H_B\), sonde de surface ou intervention insensible. Échec du témoin falsifie \(H_A\) ; réduction spécifique de l’écart, à dégât apparié, falsifie \(H_B\).

**Contrôles.** Positif : pilotage ayant un effet comportemental sur le témoin. Négatif : directions aléatoires appariées, textes de déploiement et classification non liée à l’évaluation.

**Publié.** **RAPPORTÉ** : Needham et al. (2025), *Large Language Models Often Know When They Are Being Evaluated* ; Hua, Qin, Marks et Nanda (2025), *Steering Evaluation-Aware Language Models to Act Like They Are Deployed*.  
**Coût : moyen. Relecteur :** sans détection positive, un résultat nul dans les poids n’a pas de portée causale.

### 8. Transport base → adaptateurs ou dégât hors cible explique l’ablation — famille (b)

**Mécanisme.** Les adaptateurs peuvent déplacer ou faire tourner le sous-espace appris sur le modèle de départ. À l’inverse, une ablation assez large peut réduire capacités, refus ou usage des outils, faisant disparaître un gain sans retirer spécifiquement le regard.

**Prédiction.** Si le transport échoue, la direction extraite dans chaque adaptateur surpasse celle importée et les performances de détection chutent après adaptation. Si le dégât domine, les directions témoins appariées produisent les mêmes changements et les tâches bénignes se dégradent ; une véritable composante du regard doit laisser ces témoins relativement intacts et interagir avec la condition d’observation.

**Test minimal.** Extraire les directions séparément dans le départ et chaque adaptateur, comparer angles, détection croisée et effets causaux, sans réentraînement. **Duel :** \(H_A\), l’effet de la direction importée est spécifique et transporté ; \(H_B\), il est expliqué par mauvais transport ou dommage générique. Perte bénigne équivalente sous témoins falsifie \(H_A\) ; dissociation reproductible falsifie \(H_B\).

**Contrôles.** Positif : direction extraite et appliquée dans le même organisme témoin. Négatif : mêmes couche, norme, rang et dégât mesuré ; outil bénin, suivi d’instruction et perplexité.

**Publié.** Transport entre adaptateurs : **référence à vérifier** ; pilotage causal voisin **RAPPORTÉ** dans Hua et al. (2025), titre ci-dessus.  
**Coût : moyen à haut. Relecteur :** c’est le point le plus fragile de l’inférence mécaniste.

### Signature positive de « raisons »

La signature la plus probante serait une **double dissociation causale** : à scénario, longueur de trace et formulation d’observation fixés, remplacer les raisons par celles d’un autre principe fait changer l’action dans le sens prédit par ce principe ; **et**, avec des raisons pertinentes rétablies, le gain se transfère à des outils et actions nouveaux, écrits indépendamment et à faible similarité mécanique. Ce résultat devrait survivre au juge humain/mécanique et ne pas s’expliquer par un sur-refus.

Même cette conjonction n’établirait qu’une **utilisation causale et transférable de contenus justificatifs dans le périmètre testé**. Elle ne démontrerait ni que toute la bonne conduite vient des raisons, ni que le déploiement est sûr. Écarter successivement regard, plancher et juge ne constitue pas une signature positive.

## 3. Validation minimale des instruments

Aucun taux de détection ou de fausse alerte n’est fourni dans les faits. Les seuils suivants sont donc **illustratifs**, à préenregistrer après estimation de la puissance.

| Instrument | Mesure minimale et cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|
| Questions de croyance déclarée | Taux de réponses « évalué » sur textes d’évaluation indépendants ; fausses alertes sur déploiements honnêtes de longueur, ton et outils appariés. Exiger la cohérence des questions directe et inversée, par exemple détection ≥90 % à fausse alerte ≤5 %. | Mots-clés « test/évaluation », longueur, sac de n-grammes et simple sonde logistique. Une bonne classification ne valide toujours pas une croyance causale. |
| Juge | Sur un étalonnage humain aveugle : détection des exécutions nuisibles et fausses alertes sur refus, outil bénin identique, échec technique, intention sans appel et appel sans effet ; par exemple sensibilité ≥95 %, fausses alertes ≤2 %, rapportées avec intervalles et par condition trace visible/masquée. | Journal des appels, schéma d’arguments, différences d’état et règles « exécuté/non exécuté ». Le juge doit apporter un gain sur les cas non mécaniquement décidables, pas seulement reproduire ces règles. |
| Direction interne | Détection hors auteur et hors gabarit, sur le départ puis chaque adaptateur ; fausses alertes sur déploiements appariés. Après ablation : lecture résiduelle proche du hasard, mais conduite bénigne préservée. | Mêmes classifieurs de surface ; directions aléatoires de norme, couche et rang identiques ; simple réduction de norme d’activation. |
| Transport et effets hors cible | Courbe détection/fausse alerte pour direction importée contre direction extraite dans l’adaptateur ; taux de succès bénin et suivi d’instruction avant/après. Une perte de transport supérieure à 5 points ou un dégât bénin supérieur à 2 points serait, **illustrativement**, bloquant. | Témoins appariés en dégât mesuré, non seulement en norme ; direction générique de refus ou de saillance. |
| Banc d’essai | Taux de détection = fraction des organismes réellement conditionnels dont l’écart comportemental chute sous l’intervention ; fausse alerte = perte de conduite chez des témoins non conditionnels. Le seuil minimal est une réduction préspécifiée de l’écart du témoin, sans équivalent sous directions témoins. | Pilotage générique, ablation aléatoire et simple dégradation des capacités. Si le banc échoue, l’expérience principale doit être déclarée non informative, pas négative. |
| \(S\) et \(D\) | Sur simulations calées sur les taux observés : fausses alertes sous absence d’effet du regard et détection d’effets injectés ; rapporter aussi les effets absolus. | Bootstrap par scénario et graine, permutation des conditions et comparaison systématique avec \(A\), sans ratio près d’un dénominateur nul. |

## 4. Partie B — forme du papier, en six conseils

1. **Thèse en une phrase.** « Sur Qwen2.5-32B-Instruct, ses adaptateurs publiés et ce portage de scénarios, nous séparons les gains absolus, les artefacts de mesure et les signatures causales du regard et des raisons ; la manipulation verbale seule ne permet pas cette attribution. » Toute conclusion positive doit rester conditionnée aux tests ci-dessus.

2. **Figure 1.** À gauche, les taux bruts d’actions nuisibles avec intervalles, par adaptateur et condition, en montrant le plancher et la référence ; à droite, les gains absolus des jumelles sous les deux paires de phrases. Un petit schéma causal peut relier contenu, format, regard et instruments, mais \(S\) et \(D\) passent en figure secondaire.

3. **Ordre des sections.** Question et estimands préenregistrés → reproduction et audit de la référence → résultats comportementaux et dépendance aux mots → juge, plancher et similarité → tests positifs des raisons → validation du banc d’essai et transport → intervention dans les poids → limites. Ne pas présenter l’ablation comme décisive avant ses contrôles positifs.

4. **Contrôles indispensables.** Vérité terrain humaine aveugle et journaux mécaniques ; outil bénin identique ; scénarios indépendants ; graines et bootstrap hiérarchique ; organisme témoin positif ; directions appariées en dégât ; analyse séparée des effets absolus et des interactions. Publier les résultats intermédiaires non concluants comme tels.

5. **Artefacts publiés avec le texte.** Consignes et nouveaux scénarios, sorties intégrales avec traces, graines, configurations, versions et prompts des juges, annotations humaines, code des métriques, matrices de directions, validations de transport, journaux d’appels d’outils, préenregistrement, horodatages et écarts de protocole. Indiquer explicitement ce qui ne peut être publié et pourquoi.

6. **Public, canal et interdits.** Viser les lecteurs en entraînement à l’alignement, évaluation d’agents et interprétabilité, via un article avec artefacts ouverts et une présentation d’atelier permettant la critique méthodologique. Ne pas affirmer : « les modèles sont alignés parce qu’ils comprennent les raisons », « le regard est exclu », « l’ablation prouve l’absence de conscience d’évaluation », ou « ces résultats garantissent le déploiement ». Ne pas transformer un seul modèle, une seule taille et un seul portage en résultat général.

## 5. Expérience décisive la moins chère : nécessité du contenu des traces

C’est le test nouveau le moins coûteux qui oppose directement deux versions précises de l’affirmation ; il ne suffit pas à établir l’apprentissage des raisons pendant l’entraînement.

- **\(H_A\)** : dans la recette avec raisonnement, le contenu sémantique des raisons est nécessaire à une partie du gain mesuré.
- **\(H_B\)** : à scénario et budget de génération fixés, ce contenu est inerte ; format, longueur ou appariement appris suffisent.

**Protocole.** Sur les adaptateurs publiés, générer trace intacte, raisons permutées entre scénarios, raisons rendues non pertinentes et tokens neutres de longueur appariée. Restaurer ensuite la trace originale comme contrôle de réversibilité. Croiser les deux formulations d’observation sans en faire la variable principale.

**Métrique.** Avec \(G\) le gain absolu sur la référence, définir la perte sous corruption \(L=G_{\text{intact}}-G_{\text{corrompu}}\), en points de pourcentage, avec bootstrap par scénario et graine. Le test n’est informatif que si \(G_{\text{intact}}\) est lui-même positivement établi.

**Seuil illustratif.** Si la borne inférieure de l’intervalle de \(L\) dépasse 5 points, \(H_B\) est falsifiée dans ce périmètre. Si l’intervalle entier de \(L\) reste dans \([-5,5]\) points avec une précision suffisante, la nécessité affirmée par \(H_A\) est falsifiée ; cela ne prouve pas que toute autre forme d’apprentissage des raisons est absente.

**Contrôle négatif.** Mêmes corruptions de tokens non sémantiques, succès des instructions bénignes avec le même outil et absence de dégradation générique de génération.

**Témoin à coût égal.** Référence et jumelle sans raisonnement reçoivent les mêmes scénarios, le même nombre de tirages et le même plafond de tokens ; la recette avec raisonnement reçoit en outre une corruption non sémantique de coût de calcul identique. Une interaction avec les phrases d’observation est rapportée séparément, afin de ne pas rebaptiser « raisons » un effet du regard.

## 6. Ancrage matériel

L’ancrage proposé est **Qwen2.5-32B-Instruct avec les neuf adaptateurs de rang faible**, dont la publication est **RAPPORTÉE** ; les licences et conditions exactes de redistribution sont à vérifier sur les sources primaires. Aucun réentraînement n’est requis pour les réanalyses, les nouvelles batteries, l’extraction de directions ou les ablations.

Tous les chiffres suivants sont **illustratifs** :

- Poids BF16 : environ **64 Go**, hors activations et cache ; une GPU de 80 Go peut suffire pour certaines inférences, deux GPU de 80 Go offrent davantage de marge pour les longs contextes. Une version quantifiée exige un contrôle d’équivalence comportementale.
- Réanalyse des épisodes : surtout CPU, stockage et coût d’annotation ou de juge externe.
- Nouvelles évaluations et activations : environ **100–400 GPU-heures**, **0,5–2 To** de stockage selon le nombre de couches conservées.
- Ordre de grandeur cloud : **300–2 500 €**, hors API de juges et annotation humaine ; prévoir **50–100 heures humaines** pour un étalonnage aveugle utile.
- Si l’organisme témoin ou ses poids ne sont pas disponibles, le reconstruire changerait le projet d’échelle et de coût ; il ne faut pas dissimuler ce poste dans le budget d’inférence.

## 7. Ce qui me ferait changer d’avis

- Je rétrograderais fortement « raisons » si le contenu des traces restait équivalent sous corruption, si les paires de justifications ne produisaient aucune dissociation et si le gain disparaissait sur scénarios indépendants.
- Je rétrograderais le résultat comportemental lui-même s’il ne survivait pas au juge humain/mécanique ou si les contrastes changeaient de signe après traitement correct du plancher et de la référence.
- Je cesserais d’interpréter toute ablation nulle si le banc d’essai, le transport ou les témoins de dégât échouaient.
- À l’inverse, je considérerais le regard comme causalement impliqué si une intervention validée sur l’organisme témoin réduisait sélectivement le gain des adaptateurs, sans dégât équivalent sous directions témoins, avec réplication dans chaque adaptateur.
- Je n’élèverais « raisons » au rang d’explication positive qu’après la double dissociation, le transfert indépendant et la survie aux mesures humaines/mécaniques — et seulement pour le périmètre effectivement testé.

FIN-DE-CELLULE