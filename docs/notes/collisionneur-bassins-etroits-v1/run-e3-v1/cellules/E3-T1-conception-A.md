# Proposition A — Tour III.1 : pousser vers les bassins étroits et profonds

Je suis le plan (1)–(5) fixé par la question ; les livrables (a)–(d) y sont rangés : (a) = §1, (b) = §4, (c) = §2 sous chaque méthode et §4.3, (d) = §4.4.

## 1. Ce que la question suppose sans que ce soit établi

1. **Que l'organisme possède un levier amont.** Les proposeurs ne reçoivent que la description publique, la grammaire et les lois de l'archive ; jamais une issue, un verdict, l'oracle (RAPPORTÉ, faits §1). Donc rien, en aval des proposeurs (regroupement, juge, sélection), ne peut augmenter la probabilité qu'une idée sorte d'un appel : l'aval ne peut qu'éviter de **perdre** une idée déjà sortie. Les seuls leviers amont sont la vue, l'archive (qui est la vue de la génération suivante) et la composition des proposeurs. La question dit « pousser l'organisme » comme s'il y avait un moteur de recherche ; il n'y a qu'une loi de proposition qu'on ne voit pas. — Statut : RAPPORTÉ pour la vue ; la conséquence est une **déduction**.

2. **Que « étroit » est une seule notion.** La question en donne deux : petite probabilité sous la loi de proposition des modèles (notion de prior), ou invisibilité en moyenne dans les données (notion de puissance du juge et de dilution, borne d ≤ r(A)·ln 2, OBSERVÉ-NON-AUDITÉ, faits §3). Ce sont deux problèmes distincts : le premier appelle un changement de vue, le second un changement de mesure. Une composante conditionnelle est étroite au second sens avant que sa condition soit archivée, et peut-être large au premier sens après (HYPOTHÈSE explicite des faits §4).

3. **Que « profond » se lit dans la même unité que la promotion.** Le gain en nats sur tirages frais (juge) et le nombre de composantes certifiées couvertes (oracle, D2) ne sont pas la même grandeur. Une composante nulle en moyenne mais nette par branche peut valoir beaucoup de nats dans une région rare et peu globalement. — Statut : déduction à partir de RAPPORTÉ.

4. **Que le goulot est la recherche.** La v67 montre deux goulots différents : génération 1, onze variantes d'un même constat ; génération 2, zéro promotion parce que la garde a refusé des copies plantées (RAPPORTÉ, faits §2). Rien dans les faits ne dit qu'un bassin étroit existait et n'a pas été trouvé. On ne sait pas distinguer, dans la v67, « non proposé » de « proposé puis dilué ou perdu au regroupement ». — Statut : absence de fait.

5. **Que la garde est certifiée.** Le premier tour a convergé sur « certifier la garde en absolu avant toute comparaison entre bras » (OBSERVÉ-NON-AUDITÉ, faits §3). Toute poussée vers les bassins étroits pousse vers `si_sinon` et `melange`, la classe que le nul ne couvre pas (RAPPORTÉ, faits §1). La question demande « sans affaiblir la garde » : il faut d'abord savoir ce qu'elle vaut.

6. **Que l'observation Bespoke se transporte.** Ses bassins sont ceux d'un agent à mémoire sur 24 h ; son remède (remise à zéro du contexte) n'est pas éprouvé par la page (RAPPORTÉ, faits §5). L'organisme travaille déjà en sessions neuves sans historique, un appel par proposeur et par génération (RAPPORTÉ, faits §4) : le remède Bespoke y est déjà appliqué par construction. Les chiffres (47 %, 58 %, ×9) décrivent un autre dispositif et ne doivent pas servir de prior ici.

7. **Que « sophistiqué » aide.** Le premier tour a rejeté la récompense numérique de la nouveauté, les quotas de formes, le masquage d'archive, le représentant par plus grande valeur e (OBSERVÉ-NON-AUDITÉ). Ces rejets éliminent la plupart des « méthodes sophistiquées » usuelles (bandits de nouveauté, curiosité, diversité pilotée). Ce qui reste est modeste : représentation, plan d'échantillonnage, sélection sans score, allocation de budget.

## 2. Méthodes, les plus prometteuses d'abord

Pour chacune : objet, endroit, calcul et informations, pourquoi mieux que des tirages indépendants, compatibilité, risques, et la mesure minimale de l'instrument (livrable c).

### M1 — Décomposition canonique de l'archive (inversion de Möbius sur le treillis des sous-ensembles de traits)

**Objet.** Soit T l'ensemble des traits publics et, pour chaque loi d'archive q, le logit (ou tout fonctionnel choisi) f_q(x). Sous une mesure produit sur les traits (ou une mesure de référence publique fixée), f_q admet une décomposition unique f_q = Σ_{S⊆T} f_{q,S}(x_S) avec, pour tout S et tout i∈S, E[f_{q,S} | x_{S∖i}] = 0 (Hoeffding 1948 ; Sobol' 1993, « Sensitivity estimates for nonlinear mathematical models » ; référence exacte à vérifier). Les termes sont obtenus par inversion de Möbius sur le treillis des parties de T : f_{q,S} = Σ_{U⊆S} (−1)^{|S∖U|} E[f_q | x_U]. **Preuve** : existence et unicité sous mesure produit ; exactitude sur grille finie. **Conjecture** (c'est le cœur) : servir aux proposeurs l'archive sous cette forme, avec la table des termes nuls, déplace leur loi de proposition vers les termes d'interaction vides.

**Endroit.** La vue, uniquement ; identique pour tous les proposeurs, gelée avant la course.

**Qui calcule, avec quoi.** L'orchestrateur, à partir des lois de l'archive et d'une mesure de référence publique sur les traits (le jeu public d'instances sans issue suffit). Aucune issue, aucun verdict, aucun oracle.

**Pourquoi mieux que k tirages indépendants.** Avec k appels sous la vue v, P(toucher un bassin b) = 1 − (1 − p_b(v))^k. Les tirages indépendants laissent p_b fixe ; M1 est la seule méthode de cette liste qui agit sur p_b lui-même, pour la classe précise des bassins « interaction d'un trait avec une condition archivée » — exactement la composante conditionnelle des faits §4 : une fois la condition archivée, son effet principal apparaît dans la décomposition et la case d'interaction est visiblement vide.

**Compatibilité.** Ce n'est pas un quota de formes (aucune carte n'est obligée de prendre une forme) ; pas une récompense de nouveauté (aucun score, aucun signal issu d'un juge) ; pas un masquage (l'archive entière est là, sous une autre écriture). C'est une consigne gelée avant la course, non un pilotage pendant.

**Risques.** (i) Pousse vers `si_sinon` : la garde doit être certifiée hors classe avant (voir §4.3). (ii) Biais de représentation : des interactions proposées même quand le monde n'en a pas ; c'est le contrôle négatif de §4. (iii) Explosion combinatoire : limiter l'affichage aux ordres ≤ 2 (règle écrite). (iv) Les proposeurs peuvent lire la décomposition comme une liste de cases à remplir mécaniquement : copies renommées ; la garde contre les copies existe déjà et son taux de refus est une mesure.

**Mesure minimale de l'instrument.** Exactitude : sur 50 lois synthétiques de forme connue (illustratif), la décomposition recompose f_q à 1e−9 près et les termes annoncés nuls sont nuls (vérification mécanique, taux d'erreur attendu 0). Effet sur la loi de proposition : voir §4.

### M2 — Plans orthogonaux et stratification pour le jeu public d'instances et pour les tirages frais

**Objet.** Un tableau orthogonal de force t sur les signes (ou quantiles) des traits (Hedayat, Sloane, Stufken 1999, *Orthogonal Arrays*) garantit que toute interaction d'ordre ≤ t est estimable sans confusion, avec un nombre d'instances qui croît comme le nombre de termes et non comme 1/r(A). Pour les tirages frais du juge : échantillonnage stratifié des traits selon une loi π' connue, avec une valeur e construite sur les lois conditionnelles des issues sachant les traits ; sous H₀ et π' fixé d'avance, E_{H₀}[e] ≤ 1 reste vrai parce que la carte et le nul sont des lois conditionnelles et que la loi des traits se simplifie dans le rapport de vraisemblance. **Preuve** : standard, à écrire pour le nul de recombinaisons (l'inégalité tient pour tout mélange fixé). **À vérifier avant tout (HYPOTHÈSE)** : que l'orchestrateur a la main sur le tirage des traits dans le monde à graine scellée ; si les traits sont tirés par le programme du monde et non reproductibles sous π', cette moitié de M2 tombe et il ne reste que le jeu public.

**Endroit.** (a) Le jeu public d'instances sans issue qui sert au regroupement des doublons : lu par strates (faits §4), il doit contenir assez d'instances de chaque région rare pour que la distance en nats ne soit pas écrasée par la borne de dilution. (b) Les tirages frais du juge et du test de mort.

**Qui calcule.** L'orchestrateur, avant la course, à partir de la description publique des traits. Pas d'oracle.

**Pourquoi mieux que des tirages indépendants.** Ne change pas p_b ; change la probabilité qu'une idée étroite **survive** une fois proposée. Sous tirage i.i.d., le log de la valeur e attendu pour un effet confiné à une région de masse r et de divergence δ croît comme n·r·δ ; stratifié, comme n·w·δ avec w le poids de strate choisi. Pour r petit, c'est le facteur w/r.

**Compatibilité.** Juge calculé par l'orchestrateur, engagement scellé, nul inchangé : conforme. Le réglage des poids est pré-enregistré (R1) et ne dépend d'aucune proposition.

**Risques.** Promouvoir une carte pour une région qui pèse peu dans le monde réel : c'est un choix de cible, à écrire dans le préenregistrement, pas un défaut de validité. Si les strates pertinentes ne sont pas celles du plan (interaction sur un trait continu non quantifié), gain nul.

**Mesure minimale.** Validité : 10 000 courses simulées (illustratif) sous des mondes H₀ (monde dans la classe du nul), e moyen ≤ 1 et taux de promotion e-BH ≤ niveau nominal. Puissance : mondes avec composante confinée à r ∈ {0,02 ; 0,05 ; 0,2} (illustratif), taux de détection stratifié contre i.i.d. à n égal. Regroupement : paires honnêtes appariées — (i) deux cartes égales partout sauf dans une strate rare, (ii) deux cartes égales partout — taux de fusion à tort sur (i) et de non-fusion sur (ii), plan orthogonal contre tirage i.i.d. du jeu public, à taille égale.

### M3 — Représentant de groupe par couverture sous-modulaire (formalisation de la « couverture dirigée »)

**Objet.** Pour un groupe G de doublons et un ensemble de strates publiques S, définir pour chaque carte c l'ensemble C(c) ⊆ S des strates où c diffère de l'archive de plus de ε nats (mesuré sur le jeu public sans issue). Choisir le représentant qui maximise |C(c)| ; si l'on choisit plusieurs retenues, maximiser la couverture d'union F(X) = |∪_{c∈X} C(c)|, monotone sous-modulaire, par l'algorithme glouton : garantie F(glouton) ≥ (1 − 1/e)·F(optimum) (Nemhauser, Wolsey, Fisher 1978). Variante : processus ponctuel déterminantal sur un noyau de prédictions publiques (Kulesza et Taskar 2012) — même rôle, choix aléatoire plutôt que glouton. **Preuve** : la garantie d'approximation. **Conjecture** : que « différer de l'archive sur une strate rare » corrèle avec « couvrir une composante plantée ».

**Endroit.** Choix du représentant dans un groupe de doublons, après e-BH sur les groupes.

**Qui calcule.** Programme de l'orchestrateur, sur le jeu public sans issue, **jamais sur les tirages du juge ni sur l'oracle** (faits §4).

**Pourquoi.** Encore une fois : ne change pas p_b, évite de perdre, au moment où une seule carte par groupe passe le test de mort, celle qui porte la différence confinée.

**Compatibilité avec les rejets.** Le rejet « représentant par plus grande valeur e » ne s'applique pas : aucune valeur e n'entre. Le rejet « prime de nouveauté dans la sélection » ne s'applique pas si M3 reste **à l'intérieur d'un groupe** (les sœurs sont déjà déclarées doublons et ne seront jamais servies) ; il s'appliquerait si on l'étendait au choix **entre** groupes retenus — je ne le propose pas, et c'est la ligne à ne pas franchir.

**Risques.** Si ε est mal réglé, C(c) est vide pour tous ; retour au choix apparié. Les strates sont celles de M2 : les deux méthodes se tiennent.

**Mesure minimale.** Cas honnêtes appariés : groupes construits où une seule sœur porte une différence confinée certifiée ; taux où le glouton la choisit, contre un choix uniforme (base mécanique : 1/|G|) et contre le choix apparié actuel.

### M4 — Portefeuille de proposeurs par maximisation sous-modulaire sous budget, estimé sur l'oracle en pilote

**Objet.** Soit, pour chaque famille de proposeurs j et chaque composante plantée b d'un monde pilote, p̂_{jb} la fréquence observée avec laquelle un appel de j couvre b (D2 à l'étage « propositions brutes »), et c_j le coût d'un appel. Choisir le vecteur d'appels (k_j) maximisant Σ_b [1 − Π_j (1 − p̂_{jb})^{k_j}] sous Σ_j k_j c_j ≤ B. L'objectif est monotone sous-modulaire en l'ensemble des appels ; glouton par coût unitaire avec garantie (1 − 1/e)/2 ou mieux selon la variante (Sviridenko 2004, référence à vérifier). **Preuve** : la garantie. **Conjecture** : que les p̂ estimées sur un monde se transportent à un monde de graine neuve.

**Endroit.** Composition des proposeurs, entre deux courses, jamais pendant.

**Qui calcule.** L'orchestrateur, à partir de l'oracle lu une fois après le pilote et des coûts mesurés — c'est précisément ce que N-058 autorise, et rien d'autre.

**Pourquoi mieux que des tirages indépendants.** Si les lois de proposition des familles diffèrent (p̂_{jb} non proportionnelles entre j), les appels d'une famille ne sont pas des tirages indépendants d'une même loi, et un bassin étroit pour une famille peut être large pour une autre. C'est le seul gain qui ne suppose rien sur la structure du monde, seulement sur la non-identité des proposeurs.

**Compatibilité.** N-058 (oracle et coût, pas verdict du juge) ; N-045 (le bon marché d'abord : le portefeuille préfère naturellement les familles peu coûteuses si leur couverture tient).

**Risques.** Surajustement au monde pilote : estimer sur une graine, mesurer sur une autre, et exiger que le gain survive (R4 : un gain trop net au même monde est suspect). Faible nombre d'appels par famille : intervalles larges ; marquer p̂ comme estimation.

**Mesure minimale.** Transfert : différence de couverture D2 entre portefeuille et composition uniforme à budget égal, sur deux mondes de graines neuves, lecteur neuf (R13).

### M5 — e-processus et arrêt optionnel pour le test de mort

**Objet.** Remplacer la valeur e à n fixé par un e-processus (E_n) : un supermartingale de test sous H₀, dont l'inégalité de Ville donne P_{H₀}(sup_n E_n ≥ 1/α) ≤ α (Vovk et Wang 2021, « E-values: calibration, combination and applications », Annals of Statistics ; Shafer 2021, « Testing by betting », JRSS A ; e-BH : Wang et Ramdas 2022, JRSS B). On fixe d'avance un budget maximal N de tirages et une règle d'arrêt écrite ; une carte dont l'effet est confiné à une région rare a besoin d'environ 1/(r·δ) tirages pour que son e dépasse le seuil ; à n fixé elle meurt, sous arrêt optionnel elle vit si le budget le permet. **Preuve** : validité sous toute règle d'arrêt (théorème d'arrêt). **Rien de conjectural** sur la validité ; la puissance dépend de N.

**Endroit.** Le juge et le test de mort.

**Qui calcule.** L'orchestrateur ; les tirages supplémentaires sont dépensés sur engagement scellé et ne sont jamais vus d'un agent.

**Pourquoi.** Dépense de tirages là où un effet étroit le requiert, sans changer la validité ni servir de signal. C'est « le cher sur preuve » appliqué aux tirages du juge.

**Compatibilité avec les rejets.** Le rejet « représentant par plus grande valeur e » visait la sélection ; ici aucune sélection ne change, seule la longueur du test. Il faut toutefois écrire la règle d'arrêt avant de voir une seule valeur e (R1) et garder N borné pour le devis.

**Risques.** Multiplicité : e-BH reste valide avec des e-valeurs arrêtées (propriété de la méthode) ; le risque est budgétaire, pas statistique.

**Mesure minimale.** Simulation sous H₀ : taux de fausse promotion à α nominal pour 10 000 courses (illustratif) avec arrêt optionnel. Puissance : mêmes mondes qu'en M2, détection à budget total égal, arrêt optionnel contre n fixé.

### Ce que je ne propose pas, et pourquoi

- **Comité d'archive (query-by-committee)** : afficher aux proposeurs les instances où les lois d'archive se contredisent. Sans issue, un désaccord d'archive n'est pas une évidence sur le monde ; il pointe vers les bassins déjà larges. Écarté.
- **Bandit sur les vues ou les familles pendant la course** : rouvre N-058 et le pilotage par le verdict. Écarté.
- **Recuit, tempérage, curiosité** : tous servent un score à un agent. Écartés par le premier tour, et je n'ai pas d'argument pour rouvrir.

## 3. Ce qui est impossible en principe ; où un gain existe

**Borne amont.** Pour un bassin b et une vue v, le nombre d'appels k borne tout : P(au moins une proposition dans b) = 1 − (1 − p_b(v))^k. Aucun traitement aval — regroupement, juge, sélection, mesure de diversité — n'augmente cette probabilité ; il peut seulement la préserver. Donc « pousser » se réduit à (i) changer v, (ii) changer la famille de proposeurs (donc p_b), (iii) ne pas perdre.

**Pas de repas gratuit sur la vue.** Pour une famille de vues et un proposeur donnés, Σ_b p_b(v) ≤ 1. Une vue qui élève p_b pour une classe de bassins l'abaisse pour les autres. Sans information sur **quelle** classe le monde contient — information qui serait l'oracle, donc interdite — il n'y a pas de vue uniformément meilleure. Un gain existe sous une hypothèse de **structure** : les bassins étroits du monde ont une forme nommable sans l'oracle (ici : interaction conditionnelle, nulle en moyenne). M1 parie sur cette structure ; si les bassins étroits du monde sont « sans forme », M1 ne peut rien et la couverture ne croît qu'avec k.

**Chaînes.** Une composante de profondeur 2 ne peut être trouvée qu'une fois sa condition archivée (HYPOTHÈSE des faits §4). Le temps de découverte est alors une somme de temps géométriques, et aucune méthode ne compresse un maillon avant le précédent : le gain possible porte sur la survie de chaque maillon (M2, M3, M5), pas sur l'ordre.

**Invisibilité en moyenne.** Un effet nul en moyenne sur un trait est invisible à toute mesure non stratifiée : la borne de dilution d ≤ r(A)·ln 2 (OBSERVÉ-NON-AUDITÉ) s'applique à la distance de regroupement, et son analogue en puissance s'applique au juge. Sans strates connues d'avance, le coût de détection est au moins de l'ordre de 1/(r·δ) tirages, quelle que soit la méthode.

**Goodhart.** L'absence de tout signal servi aux agents (N-053) interdit l'exploitation d'un score ; c'est aussi ce qui garantit que les gains mesurés ici, s'ils existent, ne sont pas des artefacts d'un signal.

## 4. Expérience décisive la moins chère

### 4.1 Duel principal (M1, la seule méthode qui agit sur p_b)

**Monde.** Programme à graine scellée, deux réglages : largeur = masse r de la région où l'interaction est nette et rareté de l'idée (deux niveaux, illustratifs : r = 0,05 et r = 0,25) ; profondeur = divergence δ en nats de la composante conditionnelle dans chaque branche (deux niveaux). La condition est placée dans l'archive initiale (on teste la découverte de la composante conditionnelle, pas de sa condition : c'est le maillon qu'on peut isoler).

**Bras, à nombre d'appels égal.**
- A1 : vue brute (archive telle que servie aujourd'hui).
- A2 : vue M1 (archive décomposée, ordres ≤ 2, cases nulles listées).
- A3 (témoin de budget) : vue brute avec **deux fois** les appels, pour savoir si M1 vaut plus que des tirages supplémentaires — c'est N-045 en acte.

**H_A** : sous la vue M1, la probabilité qu'un appel produise au moins une carte couvrant la composante conditionnelle (D2, étage « propositions brutes », lue une fois après par l'oracle) est plus grande que sous la vue brute, à appels égaux, et au moins égale à celle de A3 à coût égal.
**H_B** : la couverture ne dépend que du nombre d'appels ; A2 ≈ A1 < A3.

**Métrique.** Nombre de proposeurs-appels (sur K) dont au moins une des six cartes couvre la composante, certifié par l'oracle selon le critère de détectabilité déjà retenu (faits §3).

**Seuil (pré-enregistré, illustratif).** Test exact de Fisher A2 contre A1 au niveau 0,05 unilatéral ; H_A est retenue si, en plus, A2 ≥ A3 à coût égal. Si A2 > A1 mais A2 < A3, le verdict est « M1 fonctionne mais le budget d'appels fait mieux » : on dépense en appels.

**Contrôle négatif (indispensable, R4).** Monde jumeau de même graine de traits **sans** composante conditionnelle. Sous A2, le taux de cartes en `si_sinon` et le taux de promotion e-BH ne doivent pas dépasser ceux de A1 (seuil pré-enregistré). Si A2 y promeut davantage, M1 fabrique des fausses découvertes et est rejetée même si le duel principal est gagné. Second contrôle : vue A2 calculée sur une archive **permutée** (termes mélangés entre traits) ; si la couverture y reste élevée, l'effet vient de la forme de la vue et non de son information, et H_A est falsifiée dans son interprétation.

**Issues falsifiantes.** A2 ≤ A1 sur les deux largeurs : H_A tombe, la décomposition ne déplace pas la loi de proposition. A2 > A1 mais contrôle négatif dégradé : H_A tombe au titre de la garde. A3 ≥ A2 : H_A tombe au titre du coût. A2 ≈ A1 sur r = 0,25 mais A2 > A1 sur r = 0,05 avec contrôles propres : H_A survit et H_B est falsifiée sur l'étroit, ce qui est précisément le cas visé.

**Lecteur neuf, critères gelés (R13).**

### 4.2 Duel secondaire (M2 + M5, survie)

Mêmes mondes, mêmes cartes proposées (réponses brutes scellées réutilisées, aucun appel supplémentaire) ; on fait varier seulement le juge et le jeu public : i.i.d. à n fixé contre stratifié avec arrêt optionnel à budget de tirages égal.
**H_A** : le taux de promotion des cartes qui couvrent la composante (connues par l'oracle, lu après) est plus grand sous stratification + arrêt optionnel, à fausse promotion égale sur le monde jumeau sans composante.
**H_B** : égal. Métrique : promotions vraies et fausses ; seuil pré-enregistré ; issue falsifiante : égalité des promotions vraies, ou hausse des fausses.

### 4.3 Métrologie des instruments avant tout duel (banc hors ligne, sans appel de proposeur)

Convergence du premier tour, que je reprends en le disant. Pour chaque instrument : taux de détection et de fausses alertes sur cas honnêtes appariés, contre une base mécanique à battre.
- Décomposition M1 : reconstruction exacte, zéro case nulle annoncée à tort (base : 0 erreur).
- Regroupement par strates (M2) : fusion à tort sur paires « égales sauf strate rare », non-fusion sur paires « égales » ; base : regroupement sur jeu i.i.d.
- Juge stratifié et e-processus (M2, M5) : E_{H₀}[e] ≤ 1 et taux de fausse promotion sur mondes H₀, y compris mondes de **recombinaisons par morceaux** hors classe du nul (c'est la limite connue du juge ; la pression vers `si_sinon` l'expose) ; base : juge actuel.
- Représentant M3 : taux de choix de la sœur porteuse ; base : 1/|G| et choix apparié.
Aucun de ces nombres n'existe ; tous sont à produire.

### 4.4 Ancrage matériel (illustratif sauf mention)

- **Banc hors ligne (4.3)** : programmes de l'orchestrateur seuls, CPU, quelques heures ; coût marginal nul hors temps humain.
- **Duel 4.1** : 3 bras × 2 largeurs × 2 profondeurs × 10 graines de monde × 4 proposeurs × 1 appel (A3 en compte 2) ≈ 640 appels, six cartes chacun ; plus le monde jumeau négatif, soit ≈ 1 300 appels. À ~4 000 jetons de sortie par appel, ≈ 5 M de jetons. Avec des familles ouvertes (Qwen, Llama, Mistral, DeepSeek — versions à fixer au devis), coût de l'ordre de quelques dizaines à une centaine d'euros en API, ou quelques dizaines d'heures de GPU unique en local ; avec les proposeurs nommés dans les faits (Claude, Argon, Astra, Kimi — RAPPORTÉ), dix à vingt fois plus. Tout cela est illustratif et relève d'un devis sous GO.
- **Duel 4.2** : zéro appel, réemploi des réponses scellées ; tirages frais du juge, CPU.
- Ordre de dépense (N-045) : banc, puis 4.2, puis 4.1 avec familles ouvertes, puis 4.1 avec les proposeurs de la course si et seulement si M1 a battu A3 sur les familles ouvertes.

## 5. Ce qui me ferait changer d'avis

- **Sur M1** : A3 ≥ A2 à coût égal — j'abandonnerais la représentation et je recommanderais d'acheter des appels. Un contrôle négatif dégradé (plus de `si_sinon` promus sans composante) — j'abandonnerais M1 et je recommanderais d'abord de renforcer le nul (recombinaisons par morceaux). Une couverture aussi haute sous archive permutée — l'effet serait une forme de prompt et non une information ; je le dirais tel quel.
- **Sur M2/M5** : s'il s'avère que l'orchestrateur n'a pas la main sur le tirage des traits dans le monde scellé, la moitié « tirages frais » de M2 est morte ; il reste le jeu public et M5.
- **Sur M4** : si, sur mondes de graines neuves, les p̂ des familles sont proportionnelles (mêmes bassins larges, mêmes bassins étroits), le portefeuille n'apporte rien et la composition doit se décider au seul coût.
- **Sur la question elle-même** : si le banc hors ligne montre que le juge cède déjà sur des recombinaisons par morceaux à un taux supérieur au niveau nominal, toute poussée vers les bassins étroits est prématurée : on pousserait les proposeurs vers la classe où la garde ne tient pas, et le premier résultat « positif » serait à auditer comme trop propre (R4).
- **Sur l'hypothèse de chaîne** : si des proposeurs trouvent la composante conditionnelle **sans** sa condition archivée (ce que le duel 4.1 mesure en creux si l'on ajoute un bras à archive vide), la notion d'étroit « invisible en moyenne » ne décrit pas leur loi de proposition, et la stratégie d'ordonnancement perd son objet.

FIN-DE-CELLULE