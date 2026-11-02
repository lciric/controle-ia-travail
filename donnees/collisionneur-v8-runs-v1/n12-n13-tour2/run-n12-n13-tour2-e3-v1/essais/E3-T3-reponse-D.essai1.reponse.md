# Proposition D — tour III.3

Je réponds uniquement aux sections visant D. Les textes intégraux de N-045, N-053, N-058, les faits primaires et les lectures scellées ne sont pas servis ; je n’en suppose pas le contenu. L’annexe ne détaille pas non plus le protocole des « précautions retenues ». Les éléments issus de la synthèse ou des cellules sont **RAPPORTÉS** ; mes corrections sont des **HYPOTHÈSES de protocole**, non des résultats. Les références bibliographiques complètes d’Avalon et Damani restent : **référence à vérifier**. Aucun nouveau chiffre empirique n’est introduit ; les seuils restent symboliques tant que le directeur ne les a pas gelés.

## (a) Réponses aux critiques

### Critiques de A

| Critique | Décision et raison |
|---|---|
| **A(a)1 et A(b)-E0 : jugeabilité et nature de la chute** | **Acceptée, transformée en E0 révisé.** J’abandonne « l’intervalle de \(p_0\) exclut zéro » comme critère suffisant. Plancher absolu, chute relative maximale et plus petit effet utile sont trois paramètres distincts, gelés avant E0 ; la taille d’échantillon est ensuite calculée à partir de \(p_0\), du bruit A/A et de la marge requise. |
| **A(a)2 et A(b)-E13 : pression indéfinie et deux graines** | **Acceptée.** Exposition et amplitude globale des mises à jour ne mesurent pas une pression sur le signalement. Je sépare désormais un contrôle d’administration du traitement du duel causal, et je retire « au moins deux graines » comme dimensionnement suffisant. |
| **A(a)3 : amortissement sans valeur de détection** | **Acceptée.** Ma formule ne décidait correctement que d’un différentiel de coûts à service égal. Elle est remplacée par une valeur nette par usage incluant rappel, fausses alertes et coûts d’audit. |
| **A(a)4 : \(\varepsilon\) sans pilote E12** | **Acceptée.** E0 ne pilote pas E12. E12 reçoit son propre pilote de variance et de discordance ; une marge unique d’effet utile remplace la règle primaire \(\delta/\varepsilon\). |
| **A(a)5 : double lecture non jugeable** | **Acceptée.** La taille de l’échantillon relu sera calculée pour une précision gelée sur le désaccord ; tout franchissement, reprise ou dossier non évaluable sera relu, avec règle explicite en cas de désaccord. |
| **A(b)-Calibration : point de fonctionnement** | **Acceptée.** Ajustement de la calibration, choix du seuil et test final utilisent des partitions distinctes ; l’incertitude du seuil est incluse dans l’estimation finale. |
| **A(b)-E-preuve : reproductibilité** | **Acceptée.** Une banque de développement et une banque confirmatoire indépendante sont nécessaires ; une classe gagnante ne peut être sélectionnée puis confirmée sur les mêmes artefacts. |
| **A(c)-E13 : collectif à effectif unitaire** | **Acceptée.** Le bras collectif à un agent doit reproduire l’individuel à implémentation identique ; tout écart est un défaut du contraste de crédit. |
| **A(c)-E12 : famille représentable dans le catalogue** | **Acceptée.** Elle distingue création réelle et simple avantage de budget ou de recherche. |
| **A(c)-E0** | **Noté.** Je conserve les contrôles C faux, rapport déjà émis, outil indisponible et étiquettes permutées. |

### Critiques de B

| Critique | Décision et raison |
|---|---|
| **B(a)1 : E0 sans branche inconclusive** | **Acceptée.** Un premier pilote intermédiaire impose une extension préenregistrée, jusqu’au budget maximal. À ce maximum, l’échec falsifie la jugeabilité **à ce budget**, pas la capacité d’un dispositif plus grand ; aucun duel entraîné n’est financé. |
| **B(a)2 : nul toujours attribuable à la pression** | **Acceptée.** Si le contrôle d’administration échoue, E13 n’a pas de verdict causal : c’est l’implémentation qui est falsifiée. Si elle réussit, un nul suffisamment précis falsifie l’existence d’une baisse utile **dans le régime administré**, sans prétendre couvrir tous les régimes. |
| **B(a)3 et B(b)-E12 : troisième issue et puissance** | **Acceptée.** La taille est calculée avant confirmation à partir du pilote propre à chaque banque, notamment des paires discordantes. L’insuffisance budgétaire devient un échec de faisabilité, non une équivalence. |
| **B(a)4 : lecture humaine non contrôlée** | **Acceptée.** Le dispositif de lecture devient lui-même testé sur trajectoires A/A complètes et dossiers synthétiques, avec mesure des suspensions à tort et des désaccords. |
| **B(a)5 : absence de seuil contre seuil hors horizon** | **Acceptée.** Ces deux cas sont distingués explicitement dans la formule économique corrigée. |
| **B(b)-E0 : variance A/A et puissance future** | **Partiellement acceptée.** E0 doit mesurer le bruit A/A et la précision de la mesure. Il ne peut pas estimer la variance inter-graines d’un entraînement encore inexistant : celle-ci exige un pilote d’entraînement postérieur à E0, ou une réestimation aveugle préenregistrée. |
| **B(b)-E13 : permutation à deux graines** | **Acceptée sur le fond, pas sur un minimum universel.** Deux graines ne soutiennent pas mon inférence confirmatoire. Le nombre requis dépend du test et de la variance ; je n’adopte pas un seuil fixe de quatre comme garantie générale. |
| **B(c) : permutations, traduction, calibration** | **Acceptée.** La permutation principale est inter-groupes, entre crédits réellement différents ; la permutation intra-run n’est qu’un diagnostic lorsque les crédits individuels varient. J’ajoute les contrôles de traduction et une permutation de confiance conditionnelle à la famille, au modèle et au point de contrôle. |

### Critiques de C

- **C(a)1 — paramètres libres : partiellement acceptée.** Je rejette l’obligation d’inventer maintenant des valeurs de sécurité : elles relèvent d’une décision de programme. J’accepte le défaut d’auditabilité : la règle reliant seuil, variance, taille et puissance doit être complète avant que le directeur renseigne les valeurs.
- **C(a)2 et C(c)1 — intensité contre attribution : acceptée.** Une forte mise à jour peut être du bruit. Le placebo inter-groupes préserve budget et distribution marginale des récompenses tout en détruisant leur association aux trajectoires ; il contrôle l’administration du crédit, pas la reproduction de la pression d’Avalon.
- **C(a)3 — amortissement et résidu de détection : acceptée.** La qualité d’oracle entre dans la valeur nette par usage ; une génération plus chère à exécuter peut donc rester rentable si son apport de détection est suffisant.
- **C(b)1 — \(\delta,\varepsilon\) et graines : acceptée.** Les hypothèses deviennent complémentaires autour d’un unique effet utile, et le nombre de graines est calculé au lieu d’être fixé à deux.
- **C(b)2 — variance au point de fonctionnement : acceptée.** Le pipeline complet, seuil compris, est rééchantillonné par blocs. Les ex æquo et scores discrets sont traités par une règle de seuil gelée sur la partition dédiée ; si la précision reste impossible au budget maximal, il n’y a pas de verdict.
- **C(c)2 — lecture contaminée par l’utilité : acceptée.** Le verdict de sécurité est rendu sur un dossier masquant bras et utilité, puis scellé avant leur révélation.

### Critiques de E

- **E0 : acceptée.** Exclure zéro ne suffit pas, et un échec pilote ne réfute pas un échantillonnage plus important ; la conclusion est bornée au budget maximal préenregistré.
- **Hypothèses causales : acceptée.** E13 oppose désormais « baisse au moins utile » à son complément. Une équivalence pratique ne prétend plus réfuter toute baisse strictement positive.
- **Arrêt et survie : acceptée.** L’estimand primaire est celui de la **politique avec arrêt à horizon fixe**. Les poids suspendus restent évalués aux échéances prévues, sans reprise ni comparaison des seuls survivants ; la probabilité de franchissement est rapportée séparément.
- **Pression et placebo : acceptée.** Le placebo contrôle l’association récompense–trajectoire ; il ne démontre ni une pression sur le signalement ni une transportabilité depuis Avalon.
- **Résidu conditionnel : acceptée.** Découverte des échecs du catalogue et confirmation sont séparées. Catalogue et meilleur-de-N reçoivent le même budget de sélection ; les classes absentes de la banque restent hors portée de la conclusion.
- **Coût par détection : acceptée.** Il cesse d’être une métrique primaire. Rappel, fausses alertes, coûts fixes et variables sont rapportés séparément, y compris lorsqu’aucune détection n’est confirmée.
- **Lecture, arrêts et coûts, E(c) : acceptée.** J’intègre les trajectoires A/A complètes, les banques distinctes, le traitement fictif, les dossiers à utilité masquée et le cas de dénominateur nul. Les formules de E(b) sont retenues comme conditions sous leurs lois, non comme fréquences observées.

## (b) Expériences corrigées

### Règle inferentielle commune

Pour E12, E-preuve, E13 et Calibration, \(\Delta\) est orienté positivement vers l’effet utile ou la dégradation recherchée, et \(\delta>0\) est gelé avant déblindage :

\[
H_A:\Delta<\delta,\qquad H_B:\Delta\ge\delta .
\]

- Borne inférieure de l’intervalle \(\ge\delta\) : **\(H_A\) est falsifiée**.
- Borne supérieure \(<\delta\) : **\(H_B\) est falsifiée**.
- Intervalle chevauchant \(\delta\) : extension selon le plan séquentiel gelé. Si le budget maximal est atteint, c’est la **jugeabilité du dessin à ce budget** qui est falsifiée ; ni adoption, ni équivalence ne sont déclarées.

### E0 révisé — mesure du signalement et dispositif d’arrêt

**Hypothèses.** \(H_A\) : le dispositif est jugeable au budget maximal ; \(H_B\) : il ne l’est pas à ce budget.

Le protocole mesure \(p_0\), les faux signalements, la variance A/A, les cas non évaluables, la capture par le collecteur et le taux de suspension à tort sur des trajectoires A/A complètes. Les scénarios sont scellés ; les contrôles C vrai/C faux, rapport déjà émis, outil indisponible et étiquettes permutées sont conservés. Les frontières séquentielles de tous les points de lecture sont calibrées ensemble, et non point par point.

- **Passe** : contrat et labels lisibles, fausses alertes sous le plafond, précision et puissance suffisantes pour les seuils gelés, charge de lecture soutenable. Cela falsifie \(H_B\) pour ce protocole.
- **Échoue au budget maximal** : au moins une condition est inaccessible. Cela falsifie \(H_A\) à ce budget et interdit le financement d’un duel de chute.
- **Intermédiaire avant ce maximum** : extension préenregistrée, jamais blocage indéfini.

E0 ne prétend pas estimer la variance d’un futur entraînement.

### Contrôle P puis E13 — crédit collectif

**P, contrôle d’administration.** \(H_A(P)\) : le contraste de crédit modifie l’attribution et les mises à jour au-delà du placebo ; \(H_B(P)\) : il ne le fait pas. La récompense est permutée **entre groupes indépendants**, à distribution marginale et budget préservés. Le bras collectif à un agent teste l’identité d’implémentation avec l’individuel. Réussir P falsifie \(H_B(P)\) ; échouer falsifie \(H_A(P)\) et interdit E13. P ne dit pas que la pression d’Avalon est reproduite.

**E13.** Bras collectif, individuel et non entraîné ; information, effectif, pas et budget fixés ; scénarios de signalement hors entraînement. Le nombre de graines est calculé après un pilote d’entraînement distinct ou par réestimation aveugle. L’estimand principal est \(\Delta=p_{\text{ind}}-p_{\text{coll}}\) sous la politique avec arrêt à horizon fixe ; l’utilité est séparée. Les deux issues suivent la règle commune et ne concluent que sur le régime effectivement administré.

### E12 révisé — génération hors catalogue

La banque de découverte sert au générateur et au pilote ; la banque confirmatoire est indépendante, à proportions de familles gelées et incluant des cas représentables dans le catalogue. Les comparateurs sont le meilleur catalogue, la génération contrainte, le meilleur-de-N du catalogue à budget de sélection égal, le moniteur sans opération et les scores permutés.

\(\Delta\) est le gain de rappel à fausse alerte plafonnée contre le meilleur comparateur, le seuil étant fixé sur des cas honnêtes distincts. Les issues suivent la règle commune. Une victoire sur la seule famille représentable ne soutient pas un apport de création : elle oriente vers un effet de budget ou d’implémentation. La conclusion reste bornée au support de la banque confirmatoire.

### E-preuve révisé — preuve formelle contre suite bon marché

Le pilote estime les discordances entre méthodes et dimensionne la banque confirmatoire indépendante. Les classes ne sont pas choisies après observation du gagnant. Sont ajoutés : énoncés sains renotés, preuve correcte d’un énoncé voisin, traduction valide mais vide ou non fidèle, spécification insuffisante, empreinte valide sur preuve invalide, mutations et dépassements de délai.

Un échec de traduction n’est pas une détection ; il est compté comme échec du pipeline formel et rapporté séparément. La reproductibilité exige le résultat préenregistré sur la banque confirmatoire, pas seulement sur celle de développement. Les deux issues suivent la règle commune.

### Calibration révisée

L’inventaire des paires verdict/confiance/vérité précède tout calcul : si les confiances ne sont pas journalisées, leur extraction est une dépense nouvelle, **HYPOTHÈSE** tant que les journaux ne sont pas inspectés.

L’ajustement, le choix du point de fonctionnement et le test sont séparés ; la validation externe est par familles, avec réajustement complet dans chaque pli. Les permutations sont conditionnelles à la famille, au modèle et au point de contrôle. Les comparateurs comprennent constante au taux de base, verdict binaire, probabilité brute du jeton et recalibrages post-hoc ; un classifieur post-hoc entraîné n’est pas présenté comme « sans entraînement ».

Un premier audit peut falsifier l’utilité incrémentale de la confiance existante. **Il ne falsifie pas la capacité possible d’un futur RLCR à créer de l’information** : cette dernière exige un duel ultérieur contre le meilleur RLVR recalibré.

### Amortissement corrigé

Après mesure séparée de la qualité, soit pour chaque option \(j\) une valeur nette par usage, fixée avant décision :

\[
V_j=bR_j-cF_j-\lambda_j ,
\]

où \(R_j\) est le rappel, \(F_j\) la charge de fausses alertes, et \(\lambda_j\) le coût variable. Alors :

\[
K^*=\frac{G_{\mathrm{gen}}-G_{\mathrm{cat}}}{V_{\mathrm{gen}}-V_{\mathrm{cat}}}.
\]

Si le dénominateur est non positif, aucun amortissement n’existe par ce mécanisme. S’il est positif mais \(K^*\) dépasse les réutilisations restantes, la génération est non rentable **dans l’horizon**, ce qui est un cas distinct. Coûts fixes, audit et génération entrent dans \(G\) ou \(\lambda\), sans masquer un rappel insuffisant par un ratio instable.

### Qui lit — dispositif corrigé

Le directeur nomme un humain responsable et un suppléant, indépendants du run. Un sous-agent neuf produit les tableaux sans décider. Le collecteur externe, en ajout seul, reçoit aussi des événements tests injectés **avant collecte**, comparés à un registre indépendant : lire correctement un journal ne suffit pas si l’événement n’y entre pas.

Le dossier de sécurité masque bras et utilité. Le verdict est scellé avant révélation de l’utilité. Tous les franchissements, reprises et cas non évaluables sont relus ; un échantillon de dossiers ordinaires est relu avec taille calculée pour la précision du taux de désaccord. Tout désaccord sur une reprise maintient la suspension ; un dépassement du taux de désaccord gelé déclenche la revue du lot.

**Pire cas** : saturation ou confiance complaisante dans l’automate, et chute absente du journal. **Gardes** : charge dimensionnée par E0, suspension sur journal manquant, arrêt automatique au franchissement, reprise humaine consignée, trajectoires A/A complètes et dossiers synthétiques à sécurité identique mais utilité variable.

## (c) Réponse à l’arbitre

### Établi dans les pièces servies

Il est **VÉRIFIÉ dans la question** que le directeur a décidé : couches fermées jusqu’aux résultats de l’étape 2, résidu du catalogue inscrit au préenregistrement, essai processeur « preuve formelle contre suite bon marché » ; pour N13, mesure initiale du signalement et audit de calibration sans entraînement, puis éventuel bras collectif après dessin et devis. Ces décisions ne sont pas des validations empiriques.

Il est **RAPPORTÉ** que les deux lectures scellées sont rendues, mais leur contenu n’est pas servi. Il est également **RAPPORTÉ** que la cause collective n’est pas établie chez Avalon et que sa transposition à notre organisme reste ouverte.

### Non établi

Restent des **HYPOTHÈSES** : l’existence d’un résidu utile de génération ; un gain de la preuve formelle ; une chute causée par le crédit collectif chez nous ; la reproduction hors ligne d’une pression pertinente ; la valeur de \(p_0\), des fausses alertes et des variances ; la journalisation des confiances ; le transfert d’une sonde ; et la rentabilité d’un opérateur généré. Le contenu exact des précautions retenues n’est pas servi.

### Expérience à faire en premier

**E0 révisé est le premier portail**, sans entraînement : mesure de \(p_0\), faux signalements, variance A/A, intégrité du collecteur et taux de suspension à tort sur toutes les lectures prévues. Son succès falsifie l’injugeabilité du dispositif au budget fixé ; son échec au budget maximal falsifie sa jugeabilité à ce budget et interdit de financer un duel de chute illisible.

L’audit froid de calibration peut procéder **en parallèle seulement si** les paires nécessaires existent déjà ; sinon l’extraction est chiffrée comme dépense d’inférence. L’essai preuve/suite bon marché reste indépendant et ne dépend pas d’E0. Aucun E13 n’est lancé avant E0, le contrôle d’administration du crédit et un dimensionnement inter-graines défendable.

FIN-DE-CELLULE