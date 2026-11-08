# Proposition E — Tour III.3

**Statut : HYPOTHÈSE** pour toutes les décisions méthodologiques, expériences et interprétations proposées ci-dessous. Aucun résultat nouveau. Tout seuil ou budget proposé demeure **illustratif** ; le taux de fausses alertes de **1 %** provient de la question.

Les journaux bruts, effectifs par strate et devis de calcul ne sont pas transmis ; je ne les reconstitue pas.

## A. Réponses aux critiques visant E

### À A

| Critique | Décision et correction |
|---|---|
| Transversale : les « dormants » peuvent être des sabotages manqués. | **Acceptée.** Une absence d’étiquette oracle ne certifie plus un dormant. Séparer dormants attestés indépendamment, négatifs oracle seuls et cas indéterminés ; borner la contamination dans les analyses. Je ne retiens pas comme loi générale le déplacement annoncé de l’AUC vers le hasard : son sens dépend des distributions contaminantes. |
| O : maximum sur strates bruitées. | **Acceptée sur le risque ; rejetée sur la réfutation “par construction”.** Un estimateur maximal biaisé ne provoque pas nécessairement un faux rejet si l’inférence est simultanée et correctement calibrée. Mon protocole était insuffisamment explicite : intervalles simultanés obligatoires, aucune décision sur le maximum ponctuel. |
| T : absence de base qui relit. | **Acceptée.** Ajout d’une sonde sur la base relisant exactement les mêmes jetons, à capacité de lecture appariée. **Rejet** de « seul comparateur » : cette base reste un extracteur particulier, pas une borne de toute l’information textuelle. |
| P : sélection des générations à dommage maintenu. | **Acceptée.** Retrait du filtrage. Effets sur score interne, dommage et qualité estimés conjointement en intention de traiter, au niveau campagne. Le dommage réalisé ne devient pas non plus une covariable de l’analyse causale principale. |
| P : médiation par le texte. | **Acceptée.** Relecture par la base à chaque génération ; séparation entre effet total sur le lecteur interne et gain propre au contraste adapté–base. Ce contrôle ne prouve pas à lui seul une médiation causale. |
| R : budget incompatible avec le factoriel complet. | **Acceptée.** Je retire le budget et le délai globaux de III.1. Le factoriel complet n’est plus l’expérience initiale. |
| L : honnêtes d’apprentissage et dormants non spécifiés. | **Acceptée.** Apprentissage comprenant des organismes adaptés honnêtes ; dormants attestés des organismes vus comme négatifs distincts. |
| Conditions de puissance O, T, L, C, R, P. | **Transformées en tests de faisabilité**, avant lecture décisive : couverture des intervalles par simulation, précision par strate, nombre de campagnes et masse résiduelle. Les ordres de grandeur proposés par A restent illustratifs, non des seuils universels. |
| Témoins C dans le sous-espace et direction d’identité ; R graines communes ; P pression placebo. | **Acceptées.** Ajout explicite. Les graines communes servent au rejeu apparié, sans prétendre rendre identiques des trajectoires adaptatives divergentes. |
| Point favorable sur point-selle pur et cellules dommage/fausses alertes. | **Maintenu**, sans revendiquer une valeur contre des attaques hors bibliothèque. |

### À B

| Critique | Décision et correction |
|---|---|
| O : suspension confondant défaut d’oracle et défaut d’effectif. | **Acceptée pour le diagnostic ; rejetée pour l’ouverture de la porte.** Les deux causes restent distinctes : « insuffisant démontré » ou « non qualifié faute de précision ». Aucune n’autorise une lecture décisive dépendant de cet oracle. |
| O : maximum bruité et provenance du lot tiers. | **Acceptée.** Intervalles simultanés ; adjudication indépendante documentée ci-dessous. |
| T : placebo non apparié. | **Acceptée.** Appariement de chaîne, rang, exposition d’entraînement et norme, dans la mesure réalisable. Les écarts résiduels sont publiés ; l’appariement ne garantit pas une équivalence fonctionnelle. |
| L : population honnête d’apprentissage. | **Acceptée**, comme indiqué dans la réponse à A, sans fusion des critiques. |
| C : échelle indéfinie. | **Acceptée.** Dommage et qualité sont exprimés en points de couverture sur la même échelle, sans division par le faible dommage initial. |
| R : dilution et référence figée faible. | **Acceptée.** Référence = meilleure figée sélectionnée sur développement indépendant, avec ressources comparables ; mélange uniforme ajouté. |
| P : dommage post-traitement. | **Acceptée.** Issues conjointes, sans sélection. |
| T1 : dose choisie par boîte noire. | **Acceptée sur le risque de sélection ; rejetée comme conclusion automatique.** Fixer une dose n’implique pas nécessairement sélectionner les épisodes d’évaluation. Je prévois néanmoins épisodes neufs, comparateur noir d’évaluation distinct et déclaration explicite de la population : « dose sélectionnée selon la règle boîte noire ». Cela ne devient pas une dominance universelle. |
| T2 : lignées apparentées. | **Acceptée.** Les familles instruction/distillation ne constituent pas des réplications indépendantes de lignée. La validation mesure un transfert entre constructions apparentées ; aucune variance inter-lignées n’est déduite de ces seuls plis. |
| T3 : loi honnête–honnête absente. | **Acceptée.** Répétitions honnête–honnête avant interprétation du dommage diffus, sans convertir automatiquement tout dommage supérieur au bruit en intention. |
| Pseudo-réplication et puissance de R/P. | **Acceptées.** Campagne indépendante comme unité d’assignation ; générations imbriquées, épisodes imbriqués. Les calculs pour observations indépendantes ne dimensionnent pas directement ces campagnes. |
| Externe factice, placebo apparié, honnêtes adaptés, meilleure figée. | **Acceptés**, avec réserve : un moniteur factice contrôle la machinerie, pas nécessairement une difficulté d’optimisation équivalente. |

### À C

| Critique | Décision et correction |
|---|---|
| P : contradiction « tous les épisodes » / « dommage maintenu ». | **Acceptée.** Suppression du conditionnement. |
| Positifs : exclusion des ambigus favorisant le flagrant. | **Acceptée.** Tous les épisodes assignés restent dans le manifeste et les dénominateurs descriptifs. Les performances sur labels attestés sont accompagnées de bornes incluant les indéterminés, sans les déclarer positifs ou négatifs. |
| R : tirage par requête et par session équivalents sans retour. | **Acceptée sous objectif additif par requête ; rejetée comme équivalence générale.** Les dépendances temporelles peuvent changer un risque par épisode ou un objectif non linéaire. Je supprime ce contraste comme test initial de l’aléa ; tout emploi ultérieur doit préciser objectif, retours et horizon. |
| C : normalisations asymétriques. | **Acceptée.** Même unité absolue ; suppression des ratios au dommage initial. |
| O : supremum bruité. | **Acceptée sur le défaut de spécification.** Les approximations numériques ne sont pas retenues comme garanties générales. L’inférence simultanée corrigée remplace la comparaison ponctuelle. |
| P : conjonction capture résiduelle et gain absolu réintroduisant le plafond. | **Acceptée.** Deux revendications séparées : complémentarité résiduelle et avantage opérationnel au budget commun. Une forte capture peut coexister avec un avantage opérationnel non démontré. La frontière d’égalité n’est pas nécessairement une région vide, mais peut être pratiquement non certifiable. |
| L : spécialisation bénigne fortement divergente. | **Acceptée.** Contrôle négatif distinct du placebo de chaîne. |
| R : dérive sans signal défensif. | **Acceptée.** Campagne témoin avec retour sans information pertinente, orchestrée par le tiers ; seuls budgets et issues sont communiqués à la défense. |

### À D

| Critique | Décision et correction |
|---|---|
| O : biais de spectre, strates et positivité. | **Acceptée.** Strates finies préenregistrées, positifs produits par les organismes inclus, cas non adjudicables conservés. Aucune indépendance générale revendiquée. |
| T : texte public insuffisant et base absente. | **Acceptée.** Deux questions séparées : avantage opérationnel sur information publique ; avantage au-delà de la consigne accessible à un comparateur privilégié dans le sas. |
| C : moyenne de qualité masquant une incapacité rare ; redondance. | **Acceptée.** Mesures par capacité critique, tentatives, refus et longueur ; témoins de suppression générique. Une ablation nulle ne réfute pas toute causalité possible. |
| R : bibliothèque figée contre nouvelle optimisation. | **Acceptée.** Deux études nommées séparément ; aucune « génération fraîche » ambiguë. |
| P : filtrage sur dommage. | **Acceptée.** Analyse en intention de traiter. |
| Conditions O, T–L, C, R–P. | **Acceptées comme conditions de jugeabilité.** Changements de domaine, absence de support et manque de campagnes ne sont pas réparés par bootstrap. |
| Placebo à objectif caché inoffensif ; témoins covariance et pression placebo. | **Acceptés.** Le témoin existant n’est pas déclaré placebo par assimilation ; qualification du nouveau contrôle requise. |

## B. Expériences corrigées

### Contrat commun — HYPOTHÈSE

Pour **chaque duel**, \(H_B\) est exactement le complément de \(H_A\). Une région de confiance entièrement dans \(H_A\) falsifie \(H_B\), et réciproquement. Sinon : **indécis**, ce qui est une issue de mesure, pas une troisième hypothèse.

**Champs communs :**

- **Données :** manifeste de tous les épisodes, identifiants d’appariement et de campagne, provenance des labels, abstentions, sorties, exécutions, scores, budgets, graines et régimes d’information.
- **Méthode/outils :** sas tiers ; scripts Python versionnés ; séparation développement, calibration et confirmation ; simulation de couverture avant emploi des intervalles.
- **Confondants :** tâches, mondes, lignées, organismes et jumeaux regroupés dans les découpages ; seuils et sélection emboîtés, sans réutilisation confirmatoire.
- **Pièces :** protocole, code et résultats agrégés publics ; références cachées et données du bras d’attaque scellées.
- **Vérification :** recalcul indépendant dans le sas ; arbitrage de Lazar Ciric, sans présumer sa disponibilité comme auditeur technique.
- **Coût/délai :** non estimables honnêtement sans inventaire et pilote de débit. O utilise surtout processeur et adjudication ; T/L/C exigent une carte ; R/P exigent des campagnes. **Devis séparé et GO humain avant chaque étape.**

Les marges symboliques ci-dessous doivent être chiffrées avant confirmation, sur critères d’usage et pilotes vus, jamais selon le signe observé.

### O — Qualification de la vérité terrain

**Volet :** vérité terrain ; **mâchoire/règle :** sans objet ; **test causal :** aucun.

**Données supplémentaires :** panel représentatif et panel difficile distincts ; événements exécutés, références cachées et adjudication humaine aveugle aux moniteurs et à l’oracle. La provenance d’un organisme ne suffit pas à certifier son acte. Les cas non décidables restent indéterminés. Inclure répétitions honnête–honnête et sabotages produits par les organismes, pas seulement des cas construits.

**Grandeurs :** rappel, fausses accusations, abstentions, bruit honnête–honnête, fraction indéterminée.

**Duel principal :**
\[
H_A:\ \forall z,\ r_{O,z}\ge r_{\min,z}
\ \text{et}\ f_{O,z}\le f_{\max,z}.
\]
\(H_B\) : au moins une exigence échoue. Bornes simultanées ; suspension si violation démontrée **ou qualification indécise**, avec diagnostics distincts.

**Dépendance oracle–moniteurs :** protocole scellé avant lecture ; calcul après gel des moniteurs sur le lot tiers. Pour chaque moniteur et strate préspécifiée :
\[
\delta_z=P(E_M=1\mid E_O=1,z)-P(E_M=1\mid E_O=0,z).
\]
Duel \(H_A:\max_z|\delta_z|\le\eta\), \(H_B:>\eta\), avec intervalles simultanés, non maximum ponctuel. Cellules insuffisantes : indécis ; conditionnement de probabilité nulle : paramètre non défini. Cette expérience borne une **dépendance conditionnelle spécifiée**, pas l’indépendance universelle.

### T/L — Trace exploitable et lecture sans positifs

**Volets :** existence, localisation, lisibilité ; **mâchoire :** interne ; **règle :** figée ; **test causal :** aucun.

**Données supplémentaires :** activations adaptées, placebo et base sur mêmes jetons ; origine des préfixes, surprise sous la base, consigne privée sous accès contrôlé.

**Comparateurs :** texte public ; entrée complète privilégiée ; base qui relit ; activations adaptées ; écarts adaptés–base. Même budget de sélection et capacité des têtes. Contrôle positif corrigé de fuite avant le diffus.

**Contrôles :** consigne × acte lorsque les cellules existent réellement ; contraste intra-organisme ; placebo apparié ; dormants attestés ; honnêtes adaptés et spécialisation bénigne divergente. L n’utilise aucun label positif pour sélectionner son détecteur ; cette restriction est auditée.

**Grandeur/duels séparés :**
\[
H_A:\Delta_T\ge\varepsilon_T,\qquad
H_A:\Delta_L\ge\varepsilon_L,
\]
au taux de fausses alertes demandé ; compléments respectifs pour \(H_B\). La localisation doit reproduire le gain sur confirmation disjointe.

**Issue négative :** utilité incrémentale insuffisante dans le périmètre testé, non inexistence de toute trace. Les labels indéterminés donnent des bornes de sensibilité ; si ces bornes changent le verdict, celui-ci reste indécis.

### C — Effet causal spécifique

**Volet :** causalité ; **mâchoire :** interne ; **règle :** sans objet.

**Intervention :** randomisation défensive à la dose diffuse fixée ; sites choisis sur données disjointes. Témoins dans le sous-espace d’adaptateur, direction d’identité, perturbations appariées en norme et covariance, substitutions intra-condition et suppression générique d’action.

**Grandeurs :** bénéfice de couverture \(B_D\), pertes de qualité \(L_{Q,j}\) par capacité critique, dans les mêmes unités absolues. Aucun ratio au dommage initial.

\[
H_A:B_D\ge b_{\min}\quad\text{et}\quad
\forall j,\ L_{Q,j}\le \ell_j.
\]

**Issue négative :** effet spécifique insuffisant, incapacité ou intervention hors support. Même un succès ne démontre ni nécessité ni impossibilité d’un autre chemin de sabotage.

### R — Transfert puis régime adaptatif

**Volet :** règle de défense ; **mâchoire :** interne ; **règles :** figée, mélange, puis secret ; **test causal :** assignation par campagne.

**Étape bibliothèque :** matrice attaque × sonde avec dommage, dommage non détecté, rappel conditionnel et fausses alertes. Mélange optimisé sur développement puis évalué sur épisodes indépendants de la **même bibliothèque**.

**Étape adaptative distincte :** campagnes indépendantes contre meilleure figée, mélange public et mélange uniforme, ressources comparables. Puis seulement test du secret sur panel identique et allocation aléatoire des rôles. Panel dupliqué et campagne placebo contrôlent respectivement diversité nulle et dérive générale.

**Grandeur :** réduction \(G_R\) du dommage non détecté :
\[
H_A:G_R\ge\varepsilon_R;\qquad H_B:G_R<\varepsilon_R.
\]

**Issue négative :** pas d’avantage démontré. La valeur du jeu fini n’est pas assimilée à la résistance aux meilleures réponses nouvelles. Budget rouge et coût défensif sont publiés séparément.

### P — Deux tests, sans sélection des survivants

**Volet :** pince ; **mâchoire :** jointe ; **règle :** gelée avant confirmation.

**Complémentarité — aucun test causal.** Externe stricte sur code/exécution nettoyés ; seuils calibrés séparément puis test indépendant, budget partagé \(\tau/2\).

- Duel résiduel : \(H_A:R\ge r_\star\), \(H_B:R<r_\star\), avec masse des manqués et règle de précision préenregistrée.
- Duel opérationnel distinct : \(H_A:G_{\mathrm{joint}}\ge g_\star\), complément pour \(H_B\). Marge choisie compatible avec le plafond ; budget réalisé publié.

**Étau — test causal par campagne.** Pression externe réelle contre pression placebo, avec bras sans pression ; mêmes budgets assignés, aucun filtrage selon le dommage réalisé. Mesurer tous les épisodes et relire chaque génération avec la base.

\[
H_A:\Delta S_{\mathrm{int}}\ge s_\star
\quad\text{et}\quad
\Delta D\ge-\ell_D
\quad\text{et qualité préservée}.
\]

Le complément est \(H_B\). C’est une affirmation **conjointe sur effets moyens assignés**, non une comparaison parmi les seuls succès. Une hausse entièrement compatible avec dérive textuelle ou perturbation générale ne justifie pas l’interprétation mécanistique forte.

**Arrêt :** plafond budgétaire ferme ; progression évaluée avec incertitude au niveau campagne. Un plateau demeure un plateau empirique. L2 et E7 délimitent les revendications, sans être présentés comme résultats observés.

## C. Réponse à l’arbitre — une page

### Ce qui est établi dans les pièces transmises

**RAPPORTÉ :** des organismes à instruction et à adaptateur existent ; les mesures décrites concernent principalement le flagrant ; une fuite de consigne a été identifiée ; l’audit du rappel de l’oracle sur sabotages connus manque. Les résultats synthétiques de défense randomisée ne constituent pas une mesure sur un vrai modèle de langage.

**VÉRIFIÉ, selon le document transmis :** certaines empreintes de pièces ont été recalculées. Cela ne requalifie pas leurs contenus expérimentaux. Je n’ai pas effectué de vérification indépendante.

**OBSERVÉ-NON-AUDITÉ :** la qualification attribuée à Jev dans les faits demeure telle quelle.

### Ce qui ne l’est pas

**HYPOTHÈSES :** une trace interne utile du sabotage diffus ; sa séparation de la consigne, de l’identité et du texte ; sa causalité ; son exploitation sans labels positifs ; l’avantage du mélange ou du secret ; la complémentarité opérationnelle de la pince ; enfin l’étau causal.

Ces affirmations sont distinctes. Une trace décodable ne démontre pas une cause. Une cause manipulable ne démontre pas une sonde inévitable. Une capture résiduelle ne démontre pas qu’une pression externe augmente la trace. Une absence d’évasion trouvée ne démontre pas la convergence.

### L’expérience à faire en premier

**HYPOTHÈSE de priorité : lancer O, l’audit de qualification, avec contrôle honnête–honnête et provenance indépendante des labels.**

Son livrable doit distinguer :

- oracle qualifié sur les strates auditées ;
- insuffisance démontrée ;
- qualification impossible faute de précision, de support ou d’adjudication.

Aucun dormant n’est certifié par le seul silence de l’oracle ; aucun ambigu ne disparaît du manifeste. Les contrôles construits ne remplacent pas l’audit sur des épisodes effectivement produits par les organismes.

Après qualification : **contrôle positif corrigé, puis T**, avec base qui relit, placebo apparié et validation disjointe. Les lignées apparentées servent au développement, pas à certifier une généralisation indépendante.

**Décision proposée à Lazar :** financer d’abord la qualification et son dimensionnement. Différer les campagnes R/P tant que leur nombre indépendant et leur coût ne sont pas chiffrés. Une issue négative sur les sondes commande une reconception documentée ; elle n’autorise ni changement silencieux de seuil ni réutilisation d’une famille réservée déjà consommée.

FIN-DE-CELLULE