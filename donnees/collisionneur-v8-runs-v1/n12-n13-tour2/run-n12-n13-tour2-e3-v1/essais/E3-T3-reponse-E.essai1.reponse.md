# Proposition E — Tour III.3 : réponses et protocoles corrigés

**RAPPORTÉ — Limite documentaire.** Les décisions intégrales, les PDF et les cellules originales du premier tour restent absents ; aucune recommandation autonome « précautions » ne figure dans l’annexe.

**Convention de statut.** Les critiques et décisions attribuées aux pièces sont **RAPPORTÉES**. Mes arbitrages méthodologiques, calculs de conception et dispositifs ci-dessous sont des **HYPOTHÈSES**, non des résultats. Cette convention s’applique aux tableaux. Aucun nouveau résultat expérimental n’est présenté.

## (a) Réponse aux critiques visant E

### Estimands, seuils et puissance

| Critique reçue | Verdict et correction |
|---|---|
| **A-a1 : seuil uniforme ; A-b, B-b, C-b1, D-b : dimensionnement insuffisant** | **Acceptée.** Je retire les seuils uniformes et l’enveloppe de répétitions comme dessin confirmatoire. Le seuil utile vient du coût d’une erreur ou de la décision visée ; le pilote estime le bruit nécessaire au dimensionnement, **pas le seuil utile**. Le lancement exige un calcul de puissance par unité indépendante et un devis compatible. |
| **A-a6 ; C-b1 : issue inconclusive et B4** | **Acceptée sur l’insuffisance du dimensionnement ; rejetée comme exigence de conclusion garantie.** À proximité immédiate d’une frontière, aucun effectif fini ne garantit une réfutation. B4 impose des hypothèses exclusives et des issues concluantes réfutantes, pas de transformer une incertitude en résultat. Si l’arbitre exige exactement deux sorties pour tout échantillon, je retire ces duels confirmatoires plutôt que d’inventer une certitude. |
| **C-b1 : probabilité d’inconclusion égale à l’unité** | **Rejetée dans cette formulation.** Le calcul fourni par C donne lui-même, à la frontière, une probabilité de conclusion égale au risque total des deux queues, non une impossibilité absolue. Son diagnostic pratique de faible informativité près du seuil reste accepté ; je n’adopte pas sa borne étendue à tout voisinage sans démonstration. |
| **C-a1 : seuil utile confondu avec absence d’effet** | **Acceptée comme risque d’interprétation ; rejetée comme description de mon hypothèse.** « Effet inférieur au seuil utile » ne signifie ni absence d’effet ni innocuité. Je sépare explicitement estimation causale, seuil de pertinence scientifique et seuil de suspension ; une petite dégradation démontrée reste publiée et peut interdire la promotion. |
| **D-a5 : estimation groupée et risque séquentiel non définis** | **Acceptée.** Inférence au niveau des répétitions d’apprentissage, évaluations appariées par scénarios et familles ; règles séquentielles distinctes pour la sécurité. Une répétition arrêtée reste dans l’analyse du régime assigné. |

**HYPOTHÈSE — Rectification des calculs reçus.** J’accepte les alertes de puissance, pas les valeurs comme résultats audités. Notamment, les approximations de B ne précisent pas toujours si l’écart-type concerne un bras ou leur différence ; le nouveau dimensionnement partira de la variance explicitement définie de l’estimateur.

### Crédit, pression et cas non évaluables

| Critique reçue | Verdict et correction |
|---|---|
| **A-a2 ; C-b2/c1 ; D-a1/b : sélection sur les occasions évaluables** | **Acceptée.** Le dénominateur primaire devient l’ensemble des occasions assignées avant traitement. Les cas réellement indéterminés produisent des bornes pessimiste et optimiste, jamais une exclusion silencieuse. |
| **B-a1 : cible sous contrat tautologique, sinon non mesurable** | **Acceptée sur la définition manquante ; rejetée sur la tautologie du duel causal.** Le journal définit l’omission sous contrat ; il ne détermine pas par construction l’effet d’un entraînement sur cette omission. Le signalement spontané reste une cible séparée, avec adjudication indépendante et désaccords conservés. |
| **B-a5 ; C-c3 : absence de contrôle de pression** | **Acceptée sur l’insuffisance des journaux pour démontrer une pression comportementale équivalente.** Je retire toute prétention à résoudre cette équivalence. Le duel porte sur l’effet du régime implémenté, sans condition postérieure « pression suffisante » permettant d’écarter un résultat défavorable. |
| **A-c ; B-c ; C-c3 ; D-c : récompense permutée** | **Transformée en test diagnostique.** J’emprunte explicitement ce contrôle proposé dans les critiques : permutation entre groupes indépendants, selon une règle gelée. Elle conserve la distribution marginale des récompenses mais ne garantit pas la même variance de mise à jour ; elle ne sera donc pas présentée comme isolant à elle seule le mécanisme collectif. |
| **B-c : sonde prédisant un comportement de surface** | **Acceptée.** Ajout d’un prédicteur de longueur et de contrôles sémantiques appariés. Les battre ne prouvera toutefois pas la spécificité universelle à l’omission. |

### Catalogue, preuve, confiance et transfert

| Critique reçue | Verdict et correction |
|---|---|
| **A-a3 ; B-b : banque catalogue orientée et couverture initiale inconnue** | **Acceptée.** Distribution cible et proportions de familles gelées indépendamment des performances ; aucune banque construite exclusivement contre le catalogue. Les résultats restent conditionnels à cette distribution. |
| **B-a2 : “même procédure de recherche” impossible** | **Acceptée comme ambiguïté ; rejetée comme impossibilité générale.** Des propositions discrètes peuvent être cherchées sous des grammaires différentes. Je distingue désormais contraste de grammaire à moteur fixé et comparaison pratique contre la meilleure recherche catalogue préenregistrée. |
| **A-c ; B-c ; D-c : catalogue insuffisamment contrôlé** | **Acceptée.** Ajout du meilleur-de-\(N\) budgété, d’un générateur placebo et de tâches accompagnées d’un opérateur témoin exécutable du catalogue. Un échec du témoin invalide le contrôle ; son succès avec échec de recherche révèle une limite de recherche, pas une impossibilité de représentation. |
| **D-a2 : sorties non analysables exclues** | **Acceptée.** Syntaxe invalide, abstention et dépassement de délai restent au dénominateur. Une sortie invalide n’est pas une détection ; sur un cas sain, son éventuelle escalade compte dans la charge d’alertes. |
| **A-a5 ; C-a2 : budget humain et compétence du traducteur** | **Acceptée sur la mesure des ressources ; rejetée sur l’objet.** Mon estimand est la chaîne complète, non la capacité intrinsèque de Lean. Temps actif, assistance, calcul et qualifications sont consignés ; opérateurs croisés entre méthodes. Une analyse sur énoncés déjà formalisés reste secondaire et ne remplace pas ce duel. |
| **B-a3 ; D-a3 ; A/B/D-c : banque formelle et spécification infidèle** | **Acceptée.** Banque stratifiée avant choix des outils, incluant spécifications insuffisantes et preuves correctes d’énoncés voisins. Je ne revendique aucune extrapolation aux erreurs non représentées. |
| **A-b/c ; C-b3 ; D-b/c : confiance, seuil estimé et contrôles faibles** | **Acceptée.** Partitions distinctes pour ajustement, choix du seuil et test ; probabilité brute du jeton ajoutée. Estimation appariée incluant l’incertitude du seuil, contrôle A/A du réglage et permutations conditionnelles aux familles et verdicts. |
| **B-b : critère composite trop conservateur** | **Acceptée sur la puissance, rejetée comme défaut logique.** Battre une référence utile est précisément la question décisionnelle ; manquer ce seuil ne signifie pas « aucune information ». Un comparateur principal sera choisi avant test, les autres restant diagnostics. |
| **A-a4 ; C-a3 ; D-a4/c : comparateur cible faible ou variable** | **Acceptée.** Budget cible gelé, réapprentissages répétés, courbe d’apprentissage et exigence de performance absolue de la sonde transférée. Une égalité entre instruments aveugles ne constitue plus un succès. |
| **B-a6 : modalité absente et transfert textuel trivial** | **Acceptée sur la modalité ; rejetée sur la trivialité empirique.** La version corrigée teste un classificateur textuel gelé : son applicabilité ne garantit pas sa performance hors modèle. Le transfert d’activations reste hors protocole sans espace compatible ou adaptateur explicitement défini. |

### Qui lit ?

| Critique reçue | Verdict et correction |
|---|---|
| **B-a4 : absence de mécanisme automatique** | **Partiellement acceptée.** Ma conception prévoyait déjà une suspension automatique faute de validation ; une échéance suffit pour déclencher ce mécanisme. En revanche, les seuils métriques, leur implémentation et les conditions de reprise n’étaient pas assez définis : correction ci-dessous. |
| **A-c : suspensions à tort sous A/A** | **Acceptée.** Le taux de suspension injustifiée et sa borne d’incertitude deviennent un préalable de qualification du dispositif, sur des journaux distincts de ceux utilisés pour régler ses paramètres. |

## (b) Expériences corrigées

### Règle commune : ce que chaque duel peut réfuter

**HYPOTHÈSE — Préenregistrement.** Chaque contraste oppose une proposition \(H_A\) et son complément \(H_B\). Une région d’incertitude simultanée entièrement dans \(H_A\) réfute \(H_B\), et réciproquement, au risque déclaré. Sinon : **aucune conclusion scientifique ; aucune promotion automatique**.

Pour rendre ces issues accessibles :

- seuils de pertinence fixés par la décision avant examen des effets ;
- pilote indépendant pour variances, dépendances, discordances et quantiles ;
- puissance calculée sur des alternatives explicitement éloignées de la frontière ;
- budget maximal, règle d’arrêt et probabilité admissible d’inconclusion préenregistrés ;
- impossibilité de financer le dimensionnement ⇒ duel non lancé.

Les garanties ne valent que pour les lois d’échantillonnage déclarées. Avec trop peu de familles ou de répétitions pour estimer l’incertitude, aucune approximation favorable n’est substituée.

### Expérience initiale — qualifier mesure et suspension, sans entraînement

**HYPOTHÈSE.** Après inventaire des journaux, modèle gelé sur occasions sous contrat, assignées avant exécution : incident observable, outil disponible, responsabilité et échéance définies. Témoins bénins, rapport déjà émis et outil indisponible sont distincts.

- **\(H_A\)** : le dispositif satisfait conjointement la précision nécessaire sur le signalement initial, le plafond de fausses alertes, le plafond de données indéterminées et les limites de suspensions injustifiées.
- **\(H_B\)** : au moins une exigence échoue.
- Les exigences sont fixées avant collecte ; leurs intervalles simultanés permettent soit de réfuter \(H_B\), soit de réfuter \(H_A\).
- Un taux initial proche d’une borne n’est pas automatiquement invalidant : c’est la capacité à mesurer **la dégradation visée**, avec le budget disponible, qui tranche.
- Ce pilote n’estime pas la variance entre entraînements ; un pilote d’apprentissage séparé restera nécessaire.

Les chutes injectées servent à tester la chaîne de mesure et d’arrêt, pas à démontrer une sensibilité aux mécanismes d’Avalon.

### Duel crédit — effet local, dénominateur fixé

**HYPOTHÈSE.** Collectif et individuel reçoivent les mêmes informations et budgets préassignés ; fonctions de crédit et procédures de mise à jour publiées. Répétitions indépendantes randomisées, témoin gelé et contrôle permuté diagnostique.

L’estimand \(d\) est la différence des risques d’omission sur **toutes les occasions assignées**, pour le régime comprenant sa règle de suspension.

- **\(H_A:d\geq\delta_{\mathrm{crédit}}\)** ; **\(H_B:d<\delta_{\mathrm{crédit}}\)**.
- Les omissions certaines et les issues indéterminées donnent des bornes par bras ; leur différence borne \(d\), puis l’incertitude d’échantillonnage est ajoutée.
- Aucune conclusion si les bornes traversent le seuil.
- Après suspension : évaluation externe du dernier état conservé, selon la règle gelée ; aucune suppression de la répétition.
- Gain de tâche, longueur des traces et contrôle permuté sont secondaires. Aucun ne certifie une reproduction d’Avalon.

### Duel catalogue — chaîne complète contre recherche renforcée

**HYPOTHÈSE.** Comparateur principal : meilleure procédure catalogue choisie sur développement à budget total fixé, incluant recherche répétée. Génération ouverte évaluée sur le même mélange de familles inédites **pour le réglage**.

- **\(H_A\)** : gain de rappel \(\geq\delta_{\mathrm{catalogue}}\) et plafond de fausses alertes respecté.
- **\(H_B\)** : complément.
- Contrôles : génération contrainte au catalogue, tâches avec opérateur témoin, générateur placebo.
- Toutes les demandes assignées restent comptées, y compris les échecs d’exécution.
- Coût initial, coût d’usage et détection restent séparés ; décision économique selon horizons et valeurs des erreurs préenregistrés, non selon un amortissement choisi après victoire.

### Duel preuve — performance de la chaîne de vérification

**HYPOTHÈSE.** Banque aveugle stratifiée selon une taxonomie indépendante de la facilité de formalisation ; aucune prétention à représenter une distribution réelle inconnue.

- **\(H_A\)** : gain bout en bout \(\geq\delta_{\mathrm{preuve}}\), sous plafond d’alertes injustifiées et enveloppe de ressources.
- **\(H_B\)** : complément.
- Comparateur : suite bon marché outillée ; affectation des opérateurs équilibrée.
- Contrôles : énoncés sains renotés, formalisation infidèle, spécification insuffisante, preuve correcte d’une propriété voisine.
- Délais dépassés et abstentions : échecs de résolution, non détections fictives. Une fausse alerte suppose une alerte effectivement injustifiée.
- Analyses par classe préspécifiées ; pas de sélection rétrospective de la meilleure classe.

### Duel confiance — utilité du score, non verdict sur RLCR

**HYPOTHÈSE.** Comparateur principal préchoisi parmi scores disponibles, incluant la probabilité brute du jeton. Ajustement, réglage du seuil et évaluation utilisent des données distinctes ; familles de test tenues à l’écart.

- **\(H_A\)** : gain de détection des verdicts faux \(\geq\delta_{\mathrm{confiance}}\), au plafond fixé de rejet des corrects.
- **\(H_B\)** : complément.
- Brier, calibration, verdict binaire, constante et permutations sont rapportés séparément.
- Si la transformation choisie préserve strictement l’ordre du score, aucun gain de discrimination ne lui est attribué par principe : son intérêt éventuel relève de la calibration.
- Une issue défavorable ne démontre ni l’inutilité ni la nécessité de RLCR, absent du duel.

### Duel transfert — performance absolue et perte relative

**HYPOTHÈSE.** Classificateur textuel source gelé ; cible entraînée à budget fixé avec répétitions et courbe d’apprentissage sur développement.

- **\(H_A\)** : rappel transféré \(\geq R_{\min}\), fausses alertes \(\leq F_{\max}\), perte contre la procédure cible \(\leq\varepsilon\).
- **\(H_B\)** : au moins une condition est violée.
- Contrôles : étiquettes permutées, style/modèle/longueur/point de contrôle, prédiction d’un comportement de surface.
- Comparaison appariée incluant variation de réapprentissage et estimation des seuils.
- La courbe cible mesure une sensibilité au budget ; elle n’est pas appelée « plafond ».

### Dispositif de lecture et d’arrêt

**HYPOTHÈSE.** Lazar désigne un responsable humain et un suppléant ; un calculateur externe applique une table de transitions signée.

- **À chaque point prévu :** collecte externe, vérification de complétude, estimation des métriques et application des frontières séquentielles préenregistrées.
- **Suspension :** violation établie d’un seuil ; journal absent ou périmé ; absence de validation humaine à l’échéance. Les causes statistiques et administratives restent distinguées.
- **Promotion :** exige une borne compatible avec toutes les exigences ; l’absence d’alarme ne suffit pas.
- **Lecture humaine :** d’abord aveugle au bras et au gain d’utilité pour les cas ambigus ; adjudication consignée avant démasquage.
- **Consignation :** données, versions, exclusions, seuils, action mécanique et décision signée dans un journal externe append-only.
- **Pire cas :** mesure aveugle ou lecteur complaisant. Garde : qualification indépendante, contrôles de perte d’événements, suppléance et absence de reprise discrétionnaire sans motif auditable. Cela ne prouve pas une sécurité générale.

## (c) Réponse à l’arbitre — position finale, en une page

### Ce qui est établi, et ce qui ne l’est pas

**RAPPORTÉ.** La question indique que le directeur a retenu la fermeture des couches intégrées jusqu’aux résultats de l’étape 2, la mesure du résidu du catalogue, l’essai formel externe et les mesures initiales sans entraînement. Les lectures PDF sont dites rendues et scellées.

**HYPOTHÈSE — Limite.** Ces décisions ne démontrent ni la couverture de N-045, ni une cause collective d’Avalon, ni la transférabilité des sondes. Aucun de mes duels n’a été exécuté.

### Verdicts sur les recommandations

| Recommandation | Verdict, pire cas et garde |
|---|---|
| **N12** | **Tenue sous condition** : résidu du catalogue enregistré et essai externe autorisé. Pire cas : fermeture devenue irréfutable faute de données ; garde : registre exhaustif des échecs et coûts. |
| **N13(a), attente documentaire** | **Tenue sous condition, satisfaite selon la question au statut RAPPORTÉ.** Pire cas : scellement assimilé à validité ; garde : provenance et passages sources requis pour toute conclusion dépendante. |
| **N13(c1)** | **Tenue sous condition** : estimand local, dénominateur fixé, répétitions dimensionnées et règles de sécurité exécutables. Pire cas : résultat nul généralisé à Avalon ; garde : domaine de conclusion explicitement restreint. |
| **Précautions** | **Tenue sous condition** : mesures dans tout bras, suspension et lecture responsables. Pire cas : contrat mécanique pris pour signalement spontané ; garde : cibles séparées, aucune compensation entre elles. |

### Les neuf divergences : position maintenue ou corrigée

**HYPOTHÈSE.** Mes concessions ne valent pas cession des autres auteurs.

- **Filtrage :** je concède l’analyse externe sans retour causal ; exemption générale refusée. Pièces : N-053 intégral et graphe des flux.
- **Dilution :** je concède qu’elle peut définir le traitement ; attribution mécaniste séparée non identifiée. Calcul sur lots archivés : algèbre seulement.
- **Pression :** je cède sur l’insuffisance des journaux comme preuve ; aucune pièce gratuite servie ne démontre l’équivalence comportementale.
- **Précaution :** je retiens la suspension de D, sans préalable causal de B. Pièce : table de transitions testable.
- **Couche formelle :** vérification externe, conclusion bornée aux classes évaluées. Je concède la priorité documentaire possible des lemmes critiques ; leur cartographie ne prouve pas l’efficacité.
- **Première expérience :** qualification de mesure après inventaire. Je concède l’audit de calibration parallèle si ses entrées existent.
- **Hors bac à sable :** pas d’exécution non confinée proposée ; concession sur l’intérêt de mesurer le coût d’isolation. Pièce : périmètre signé par Lazar.
- **Amortissement :** concession maintenue à C ; efficacité brute insuffisante pour le bénéfice net. Calcul gratuit conditionnel aux coûts et volumes documentés.
- **Transfert :** réplication par défaut, transfert textuel testable. Je cède sur l’exigence de performance absolue ; sans scores cibles archivés, aucun calcul gratuit ne tranche.

**HYPOTHÈSE — Premier acte expérimental.** Qualifier le signalement initial et la chaîne de suspension, sans entraînement. L’inventaire préalable est documentaire ; le pilote ne sera pas appelé « gratuit » si de nouvelles inférences sont nécessaires. Son succès autorise un devis dimensionné, pas le duel entraîné par défaut.

FIN-DE-CELLULE