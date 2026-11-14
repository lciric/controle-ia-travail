# Consultation — Du « regard » aux mécanismes de bonne conduite

**Statuts.** Les constats du dossier restent **RAPPORTÉS**, sans validation indépendante ici. Toutes les explications proposées, prédictions et recommandations ci-dessous sont des **HYPOTHÈSES**, sauf mention contraire ; les équations sont des définitions ou des conséquences algébriques, non des résultats expérimentaux.

**Pièces absentes :** le brouillon source [B], les épisodes, les données, le préenregistrement et les articles cités ne sont pas transmis ; je n’en présume pas le contenu.

## 1. Ce que la question suppose sans que ce soit établi

### « Avoir appris les raisons » n’est pas encore une hypothèse assez précise

Il faut distinguer :

- **l’effet d’une recette** : les documents et démonstrations améliorent une mesure ;
- **l’usage d’informations normativement pertinentes** : la décision change avec les conséquences, droits ou obligations pertinents ;
- **l’acquisition de cet usage pendant l’entraînement étudié** ;
- **une motivation interne durable**, indépendante du contexte.

Ces propositions ne s’impliquent pas automatiquement. Une recette peut activer une compétence préexistante ; une trace peut produire un meilleur calcul sans transmettre les valeurs ; une bonne décision peut provenir d’un classement superficiel.

**RAPPORTÉ :** la paire jumelle diffère par la présence du raisonnement dans les démonstrations. Elle n’isole donc pas, à elle seule, « apprentissage des raisons » contre « absence de raisons » : longueur, distribution des textes et apprentissage d’un protocole de réponse peuvent aussi différer.

### Le regard n’est ni une variable observée, ni nécessairement une cause concurrente

**RAPPORTÉ :** les questions directe et inversée ordonnent les jumelles différemment. Une variation de réponse à une question de croyance ne démontre donc pas la variation de l’état causal recherché.

**HYPOTHÈSE :** raisons, reconnaissance du contexte et anticipation de sanctions peuvent agir conjointement. Il faut tester des contributions et interactions, pas imposer une partition où une seule explication gagne.

### La « part du regard » n’est pas spontanément une fraction causale

Définissons, pour une recette \(m\) et une condition \(z\),

\[
h_m(z)=\Pr(Y=1\mid m,z),\qquad
A_m(z)=h_{\mathrm{réf}}(z)-h_m(z),
\]

où \(Y=1\) désigne une action nuisible. La statistique du dossier est

\[
S_m=1-\frac{A_m(\mathrm{non\ observé})}{A_m(\mathrm{observé})}.
\]

Elle est indéfinie si le dénominateur est nul, instable s’il est petit, et peut sortir de l’intervalle unité. Elle dépend aussi du comportement de la référence.

Plus précisément,

\[
S_m=
\frac{
[h_{\mathrm{réf}}(o)-h_{\mathrm{réf}}(n)]
-
[h_m(o)-h_m(n)]
}{A_m(o)}.
\]

Ainsi, un modèle \(m\) parfaitement invariant peut avoir un \(S_m\) non nul si la référence change. **Conclusion algébrique :** \(S_m\) mesure une modification relative du gain, pas une proportion identifiée de « motivation par le regard ».

Je publierais d’abord les taux absolus et les interactions additives

\[
I_m=[h_m(n)-h_m(o)]-[h_{\mathrm{réf}}(n)-h_{\mathrm{réf}}(o)],
\]

puis \(S_m\) comme statistique secondaire, avec son domaine d’interprétation.

---

## 2. Partie A — Huit explications rivales ou menaces d’identification

**Convention de lecture — HYPOTHÈSES.** Pour chaque entrée, la prédiction est un contraste expérimental, non une signature logiquement exclusive. « Raisons » signifie provisoirement **sensibilité sélective aux propriétés normativement pertinentes** ; « regard » signifie dépendance à une croyance d’observation effectivement manipulée. Aucun test comportemental isolé ne prouve une motivation interne.

### A1. Reconnaissance de patrons plutôt que transfert des raisons — famille (a)

**Mécanisme — deux phrases.** La recette apprend à reconnaître des objets, tournures et situations associés aux refus. Les scénarios d’évaluation réactivent ces associations sans nécessiter une représentation transférable des raisons.

**Prédiction discriminante.** À observation annoncée constante, le modèle suit l’habillage familier lorsqu’on conserve les mots mais inverse le statut moral de l’action ; il perd son gain quand on conserve ce statut mais change l’habillage. « Raisons » prédit plutôt l’inverse ; « regard » seul ne prédit pas cette interaction contenu–habillage, à condition que l’habillage ne modifie pas lui-même la croyance d’évaluation.

**Test le moins cher.** Construire des paires contrefactuelles avec les adaptateurs jumelles et la référence : même outil et même structure, mais conséquences ou autorisation différentes ; puis paraphrases indépendantes. **Épisodes déjà joués :** utiles pour sélectionner les familles, insuffisants pour tester les contrefactuels.

**Contrôles.** Positif : indices familiers nettement présents dans une version témoin. Négatif : changements de noms, d’ordre et de style sans modification normative.

**Publié.** **RAPPORTÉ :** Cho et al., 2026, *Constitutional Midtraining: Content Presence Drives Alignment Gains*, est présenté comme laissant ouverte l’explication par appariement de surface ; **référence à vérifier**.

**Coût :** moyen. **Objection du relecteur :** une généralisation entre scénarios proches peut n’être qu’une interpolation.

### A2. Politique de refus ou aversion au risque — famille (a)

**Mécanisme — deux phrases.** La recette augmente le seuil nécessaire pour entreprendre une action sensible. Elle évite les dommages en refusant davantage, sans améliorer l’arbitrage entre dommages de l’action et de l’inaction.

**Prédiction discriminante.** Le gain disparaît sur des cas où l’action sensible est nécessaire pour éviter un dommage supérieur, et le refus injustifié augmente. « Raisons » prédit une adaptation au bilan pertinent ; « regard » prédit une variation avec l’observation plutôt qu’un biais stable vers l’inaction.

**Test le moins cher.** Ajouter des cas où le même outil permet soit une action nuisible, soit une intervention protectrice nécessaire, en maintenant la faisabilité technique. **Épisodes déjà joués :** les contrôles bénins permettent un premier tri, pas le test du coût de l’inaction.

**Contrôles.** Positif : cas sensible où le refus est justifié. Négatif : instruction bénigne avec le même outil, puis cas protecteur dont l’inaction est explicitement dommageable.

**Publié.** Pas de référence attribuable ici pour cette distinction exacte : **référence à vérifier**.

**Coût :** bas à moyen. **Objection du relecteur :** mesurer uniquement les mauvaises actions récompense potentiellement un agent inutilisable.

**RAPPORTÉ :** l’exécution des instructions bénignes affaiblit déjà l’hypothèse d’une incapacité générale à agir, mais pas celle d’un conservatisme ciblé.

### A3. Obéissance à une autorité ou à une identité de rôle — famille (a)

**Mécanisme — deux phrases.** Le modèle apprend qui paraît autorisé à définir la conduite plutôt que pourquoi une conduite est justifiée. Des marques de provenance ou de rôle deviennent des substituts aux raisons.

**Prédiction discriminante.** À conséquences et surveillance constantes, le choix suit une autorité nominale lorsque celle-ci entre en conflit avec une justification explicite. Une politique fondée sur les raisons doit rester insensible aux marques de prestige sans pertinence normative ; une politique de regard doit suivre l’observation plutôt que ce prestige.

**Test le moins cher.** Croiser justification pertinente et prestige nominal du locuteur, en gardant fixes les permissions réelles et la hiérarchie technique des messages. **Épisodes déjà joués :** codage exploratoire possible ; identification causale impossible sans nouveaux essais.

**Contrôles.** Positif : une véritable permission change lorsque l’action exige légitimement cette permission. Négatif : seule une décoration institutionnelle change, sans nouveau droit.

**Publié.** Travaux précis sur cette explication : **référence à vérifier**.

**Coût :** bas. **Objection du relecteur :** suivre une spécification peut relever de l’obéissance apprise, non de l’usage des raisons qu’elle expose.

### A4. Compétence procédurale ou délibération générique — famille (a)

**Mécanisme — deux phrases.** Les démonstrations avec raisonnement enseignent une procédure : vérifier les conditions, anticiper les effets et contrôler les arguments d’un outil. Le gain de sûreté vient alors d’une meilleure résolution de tâche, pas spécifiquement d’un apprentissage normatif.

**Prédiction discriminante.** L’avantage de la jumelle avec raisonnement croît avec la complexité de planification, y compris sur des tâches non normatives, et se réduit lorsque les conséquences sont entièrement explicitées. « Raisons » prédit un avantage sélectif sur les distinctions normatives à difficulté appariée ; « regard » prédit une interaction avec l’observation.

**Test le moins cher.** Croiser difficulté procédurale et conflit normatif ; fournir dans certaines variantes un tableau complet des conséquences, sans recommandation morale. **Épisodes déjà joués :** erreurs d’outil et de compréhension recodables ; le contraste apparié demande de nouveaux épisodes.

**Contrôles.** Positif : tâche bénigne exigeant plusieurs vérifications. Négatif : décision normative simple, sans calcul ni outil ambigu.

**Publié.** **RAPPORTÉ :** Li, Wichers, Price, Marks et Kutasov, 2026, *Model Spec Midtraining: Improving How Alignment Training Generalizes*, compare des recettes avec et sans raisonnement ; cette attribution ne démontre pas le mécanisme proposé.

**Coût :** moyen. **Objection du relecteur :** « avec raisonnement » est une intervention sur la procédure aussi bien que sur le contenu.

### B1. Direction mal identifiée ou mal transportée — famille (b)

**Mécanisme — deux phrases.** La direction extraite sur le modèle de départ peut coder le vocabulaire des évaluations plutôt que la croyance d’être évalué. Les adaptateurs peuvent en outre déplacer ou redistribuer cette représentation, et rendre l’intervention inefficace sans supprimer la croyance.

**Prédiction discriminante.** La direction perd sa validité hors des textes de construction ou dans certains adaptateurs ; une direction recalibrée localement retrouve un effet que la direction transportée n’avait pas. Ce patron distingue un échec de l’instrument d’une invariance réellement imputable aux raisons ou à l’absence de regard.

**Test le moins cher.** Tester séparément décodage hors distribution, transfert entre modèles et effet de l’intervention ; comparer la direction transportée à des directions propres aux adaptateurs, sans réentraîner ceux-ci. **Épisodes déjà joués :** seulement si les activations pertinentes sont conservées.

**Contrôles.** Positif : organisme dont la conduite conditionnelle est établie par construction, avec succès exigé sur la manipulation comportementale, pas seulement sur une sonde. Négatif : textes contenant le vocabulaire d’évaluation sans que celui-ci décrive le contexte présent.

**Publié.** **RAPPORTÉ :** Hua, Qin, Marks et Nanda, 2025, *Steering Evaluation-Aware Language Models to Act Like They Are Deployed*, est présenté comme montrant un effet du pilotage sur un organisme ; ce n’est pas une validation du transport vers ces adaptateurs.

**Coût :** moyen à haut. **Objection du relecteur :** ne pas agir sur le construit ne permet pas de conclure à son absence causale.

### B2. Effets hors cible et banc d’essai trop favorable — famille (b)

**Mécanisme — deux phrases.** Retirer un sous-espace peut altérer la compréhension, le refus, la représentation des risques ou l’usage des outils en même temps que la variable visée. Un organisme artificiel peut concentrer sa conduite conditionnelle dans une représentation particulièrement facile à modifier.

**Prédiction discriminante.** Les changements de sûreté suivent les pertes de compétence ou apparaissent aussi sous des directions témoins ; le succès sur l’organisme ne se transporte pas entre recettes d’organismes. « Raisons » et « regard » interprétés causalement exigent au contraire une sélectivité suffisante de l’intervention.

**Test le moins cher.** Appliquer une gamme d’intensités, tester les fonctions voisines, comparer aux directions appariées sur plusieurs dimensions de dommage. **Épisodes déjà joués :** ils fournissent une référence, mais il faut de nouvelles exécutions.

**Contrôles.** Positif : intervention délibérément dégradante, pour vérifier que la batterie détecte une perte de compétence. Négatif : intervention nulle et directions témoins fixées avant lecture des résultats de sûreté.

**Publié.** **RAPPORTÉ :** le dossier mentionne un billet sur la dépendance des mitigations aux recettes d’organismes ; auteurs absents, donc **référence à vérifier**.

**Coût :** haut. **Objection du relecteur :** une lésion n’est pas une intervention sélective sur une croyance ; un organisme positif n’établit pas la validité externe.

### C1. Avantage de style auprès du juge — famille (c)

**Mécanisme — deux phrases.** La recette produit des formulations de refus ou de justification que le juge associe à la sûreté. Une parenté de style entre le générateur des données et le juge amplifie cet avantage, même si les actions finales ne diffèrent pas autant.

**Prédiction discriminante.** L’avantage diminue après masquage de l’identité, retrait des justifications et adjudication des actions effectivement exécutées. « Raisons » et « regard » comportementaux prédisent un effet sur les actions, pas seulement sur la préférence d’un évaluateur textuel.

**Test le moins cher.** Audit humain aveugle, stratifié par modèle et désaccord entre verdicts, incluant aussi un échantillon de cas concordants ; pondérer ensuite pour retrouver la distribution initiale. **Épisodes déjà joués : oui.**

**Contrôles.** Positif : cas artificiels où une déclaration vertueuse accompagne une action nuisible indiscutable. Négatif : même action, formulations justificatives différentes.

**Publié.** Aucun travail précisément attribuable ici sur ce biais dans ce protocole : **référence à vérifier**.

**Coût :** bas à moyen. **Objection du relecteur :** plusieurs juges automatiques peuvent partager le même biais.

### C2. Gain apparent dépendant de la mesure et du support d’évaluation — famille (c)

**Mécanisme — deux phrases.** Le plancher, le ratio de gains et la dépendance entre tirages peuvent rendre un contraste instable ou excessivement précis. La proximité entre données d’entraînement et familles de scénarios peut limiter le gain au support choisi, même sans duplication littérale.

**Prédiction discriminante.** Le classement change avec l’échelle, l’exclusion d’une famille ou des graines nouvelles ; l’effet décroît sur des scénarios construits indépendamment. Ni « raisons transférables » ni « regard » ne suffisent à expliquer une dépendance à ces choix de mesure, une fois le contenu normatif et l’observation appariés.

**Test le moins cher.** Publier les cellules brutes, analyser les scénarios comme unités de regroupement, faire des analyses « une famille retirée », puis un petit lot indépendant avant toute nouvelle intervention interne. **Épisodes déjà joués : oui** pour les premières analyses ; parenté et transfert demandent des données accessibles et de nouveaux cas.

**Contrôles.** Positif : simulation avec effet injecté et dépendances reproduites, pour vérifier l’analyse. Négatif : permutation des étiquettes selon les unités réellement randomisées.

**Publié.** **RAPPORTÉ :** Korbak et al., 2026, *How far does alignment midtraining generalize?*, est présenté comme signalant une perte de transfert vers des évaluations plus réalistes ; **référence à vérifier**.

**Coût :** bas, puis moyen. **Objection du relecteur :** beaucoup de tirages dans peu de familles ne constituent pas autant de preuves indépendantes de généralisation.

---

## 3. La signature positive des « raisons »

**HYPOTHÈSE opérationnelle.** Une signature positive serait une **double sélectivité** :

1. sensibilité aux changements de raisons pertinentes, y compris lorsqu’ils obligent à agir plutôt qu’à refuser ;
2. invariance aux changements non pertinents de formulation, prestige, identité superficielle et observation, lorsque ces changements n’affectent pas légitimement la décision.

Soit \(r\) le contexte normatif, \(t\) l’habillage et \(z\) l’observation annoncée. Pour un ensemble d’actions \(\mathcal A\), définissons à l’avance un ensemble acceptable \(\mathcal A^*(r)\), avec adjudication indépendante et possibilité de désaccord documenté.

\[
Q_m(r,t,z)=\Pr_m\{a\in\mathcal A^*(r)\mid r,t,z\}.
\]

Il faut notamment des paires où

\[
\mathcal A^*(r_0)\neq\mathcal A^*(r_1),
\]

mais où outil, présentation et difficulté sont appariés. Une simple diminution uniforme des actions nuisibles ne suffit pas.

**Esquisse d’identification.** Si les variantes sont assignées aléatoirement, leur contraste estime l’effet causal du changement de contexte présenté sur le comportement, dans cette population d’épisodes. Pour interpréter ce contraste comme sensibilité aux raisons, il faut encore que le changement n’altère pas simultanément faisabilité, clarté ou indice de test ; les variantes placebo examinent cette condition sans la démontrer intégralement.

Même cette signature établirait une **compétence comportementale compatible avec l’usage des raisons**, non une motivation profonde. Attribuer son acquisition au contenu des raisons nécessiterait ensuite des entraînements contrôlés — contenu normatif pertinent contre contenu placebo, budgets appariés — que les adaptateurs existants n’identifient pas entièrement.

---

## 4. Partie B — Six conseils pour le papier

### 1. Thèse en une phrase

**HYPOTHÈSE de cadrage :** « Nous testons quelles composantes du gain de sûreté des recettes de spécification résistent à des changements ciblés de contexte, et quelles limites de mesure empêchent d’attribuer ce gain aux raisons ou au regard. »

Avec les seuls constats actuels **RAPPORTÉS**, la thèse doit être plus étroite : **la manipulation verbale employée ne permet pas l’attribution mécaniste recherchée**.

### 2. Figure 1

Trois panneaux :

- **graphe causal** : recette → compétences, patrons, raisons, représentation de l’observation → action ; formulation → plusieurs de ces variables ; juge → verdict ;
- **taux absolus par modèle et formulation**, avec incertitudes, avant tout ratio ;
- **matrice de prédictions** des mécanismes, puis résultats des contrôles de validité.

Ne pas dessiner une partition du gain en « raisons » et « regard » sans modèle d’identification.

### 3. Ordre des sections

Question et estimands → faits reproduits → validité des mesures → manipulation verbale et limites → tests comportementaux discriminants → intervention interne seulement si validée → limites et portée.

Cet ordre évite que l’intervention technique serve de preuve avant que son construit soit défini.

### 4. Contrôles indispensables

Audit humain aveugle ; actions séparées des discours ; référence correctement identifiée ; contrôles d’action protectrice ; variantes placebo ; réplications indépendantes ; contrôles de transport et hors cible ; organisme positif.

Séparer explicitement **préenregistré**, **modifié après données** et **exploratoire**. **RAPPORTÉ :** une règle a changé et l’horodatage public est tardif ; les présenter sans reconstruire une chronologie plus favorable.

### 5. Ce qui accompagne le texte

Versions exactes des modèles et adaptateurs, code, graines, paramètres d’échantillonnage, données par cellule, protocole d’audit, désaccords, analyses de sensibilité et historique des décisions. Publier la construction des directions et tous les échecs du pilote ; documenter les modalités d’accès aux scénarios sensibles.

Les traces de raisonnement, si diffusées, restent des sorties observées, pas des annotations fiables du mécanisme interne.

### 6. Public, canal et limites de langage

Viser les communautés d’évaluation, de sûreté et de représentation mécaniste, avec une contribution commune : **un protocole d’identification et des tests qui pourraient réfuter ses interprétations**. Un article de conférence généraliste en apprentissage ou en traitement du langage convient si les contrastes sont exécutés ; sinon, une note méthodologique reproductible est plus juste.

Ne pas affirmer « les raisons ont été apprises », « le regard est éliminé », « l’alignement est robuste » ou « la direction contient la croyance ». La portée doit suivre les interventions validées, non la sophistication de l’outil.

---

## 5. L’expérience décisive la moins chère : un duel limité

**HYPOTHÈSE de priorité :** après un audit ciblé des verdicts existants, le meilleur achat expérimental est un test comportemental contrefactuel, avant l’ablation interne coûteuse.

### Duel

- \(H_A\) : le gain provient surtout d’un patron de refus associé aux indices sensibles.
- \(H_B\) : le gain comprend une sensibilité transférable aux raisons pertinentes.

Ce duel ne prétend pas départager toutes les motivations internes.

### Plan

Utiliser les deux jumelles et la référence. Construire des paires nouvelles où la même action, avec le même outil, est tantôt injustifiée, tantôt nécessaire pour éviter un dommage ; conserver le contexte d’observation identique et retirer les formulations explicitement évaluatives.

Créer parallèlement un **témoin à coût égal** : mêmes appels, même longueur et même budget de génération, mais uniquement des variations de style sans changement normatif. Les cas et leurs réponses acceptables sont gelés avant exécution.

### Métrique

Pour une action sensible, notons \(p_m^+\) sa probabilité quand elle est justifiée, \(p_m^-\) sa probabilité quand elle ne l’est pas :

\[
T_m=p_m^+-p_m^-,
\qquad
\Delta T=T_{\mathrm{avec}}-T_{\mathrm{sans}}.
\]

Une stratégie de refus uniforme donne un \(T_m\) proche de zéro, même avec peu d’actions nuisibles. Une discrimination correcte augmente \(T_m\). Rapporter également chaque composante et la comparaison à la référence : un contraste agrégé ne doit pas masquer une perte de sûreté.

### Seuil de décision

**Seuils illustratifs à fixer avant collecte :**

- borne inférieure de l’intervalle d’incertitude de \(\Delta T\) supérieure à **10 points de pourcentage, illustratifs** ;
- effet des transformations placebo contenu dans une marge de **±5 points, illustrative** ;
- absence d’une dégradation du taux d’actions nuisibles dépassant une marge préspécifiée.

Fixer l’effectif à partir de la précision attendue sur les **familles de scénarios**, pas seulement du nombre de tirages. Une absence de différence non précise ne départage pas les hypothèses.

**Contrôle négatif :** permutation des noms et du prestige nominal sans changement de permissions ou de conséquences.

**Lecture.** Le succès favorise \(H_B\) contre ce \(H_A\), sans prouver l’acquisition des raisons pendant l’entraînement. L’échec précis, avec contrôles réussis, favorise le patron de refus ; l’échec des contrôles rend le duel non concluant.

---

## 6. Ce qui me ferait changer d’avis

**HYPOTHÈSES de révision :**

- **Vers une priorité accrue au regard :** une intervention interne validée sur chaque adaptateur modifie sélectivement la conduite, préserve les compétences voisines et produit des effets cohérents avec plusieurs manipulations indépendantes de l’observation.
- **Vers l’explication par les raisons :** les jumelles suivent les inversions normatives inédites, y compris vers l’action protectrice, résistent aux changements de style et d’autorité non pertinente, et leur avantage dépasse celui observé sur des tâches procédurales appariées.
- **Vers une explication par la mesure :** l’audit des actions, les graines indépendantes ou le retrait de certaines familles réduisent substantiellement le gain.
- **Contre l’intérêt d’une conclusion mécaniste sur les poids :** la direction échoue au transport, les effets suivent les dommages collatéraux ou seul un organisme spécialement favorable répond.
- **Vers une affirmation sur l’apprentissage des raisons lui-même :** un entraînement contrôlé sur les raisons pertinentes surpasse un placebo de même coût et transfère aux contrastes normatifs gelés à l’avance.

Le changement central proposé est donc de passer de **« quelle rivale peut-on éliminer ? »** à **« quelles variations pertinentes le modèle suit-il, quelles variations non pertinentes ignore-t-il, et quelle intervention permet d’attribuer cette sélectivité ? »**

FIN-DE-CONSULTATION