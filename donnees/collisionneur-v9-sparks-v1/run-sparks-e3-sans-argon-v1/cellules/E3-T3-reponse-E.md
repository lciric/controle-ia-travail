# Proposition E — Réponse aux critiques et plan corrigé

**OBSERVÉ-NON-AUDITÉ —** La critique C est absente (« jamais lancée ») ; je ne lui attribue aucun contenu.

**Statuts.** Les résultats du billet et de « nos résultats » restent **RAPPORTÉS** ; les constats tirés des journaux par le lecteur restent **OBSERVÉS-NON-AUDITÉS**. Ma convention initiale « tous les résultats sont rapportés » était trop globale : elle ne doit pas effacer cette distinction. Les réponses méthodologiques et les plans ci-dessous sont des **HYPOTHÈSES**, non des résultats. Tous les nouveaux nombres de conception sont **illustratifs, supposés**. Aucun nouvel audit, aucune recherche de nouveauté.

## A. Réponse aux critiques visant E

Les renvois regroupent les occurrences d’une objection **à ma proposition**, sans fusionner les propositions des critiques.

### DELTA

| Critique | Décision et correction |
|---|---|
| **A : fusion non gelée. B et D : bras combiné contre comparateurs isolés.** | **Acceptée.** Comparaison principale : « boîte noire + lecteur » contre « boîte noire + mécanique », mêmes informations disponibles et même famille de fusion. Extraction, ajustement, sélection du comparateur, fusion et seuils sont gelés avant confirmation. |
| **A : résumé potentiellement choisi après inspection des positifs. B : accès informationnels différents. D : résumé pouvant détruire le signal.** | **Acceptée sur le contrôle ; rejetée comme impossibilité de mesurer un apport.** Une différence entre lecteurs d’une même représentation reste mesurable, mais ne démontre pas une compréhension exhaustive des poids. L’extracteur sera fixé avant inspection de la banque positive. Le classifieur mécanique recevra exactement le même résumé, extraits compris. L’intitulé devient **« apport d’un lecteur de représentation de delta »**. |
| **B : un gain ne viendrait que des a priori ou des extraits.** | **Rejetée comme objection fatale.** Ce sont précisément des sources possibles d’avantage prédictif. Elles interdisent une attribution à une « lecture native des poids », pas la mesure d’utilité marginale. |
| **A : banque Gemma non attestée ; indépendance et faisabilité.** | **Acceptée.** Je retire « organismes déjà disponibles » pour cette cible. Le programme P3 décrit un saboteur instruit, pas une banque d’adaptateurs — « nos résultats », §6, **RAPPORTÉ**. Sans banque autorisée et documentée, DELTA n’est pas le premier chantier. |
| **A, B, D : certification des fausses alertes sous-puissante ; petit nombre de positifs.** | **Acceptée.** L’absence d’alertes dans un petit test ne sera plus le mécanisme principal de calibration. Un pilote ne certifiera pas une garantie conditionnelle de déploiement. La confirmation exige un dimensionnement préalable. |
| **A, transversal : une alerte ferait devenir vraie la clause « taux réel supérieur au plafond ».** | **Rejetée littéralement.** Un résultat d’échantillon ne change pas le taux réel. Il peut empêcher sa certification. A reconnaît ensuite correctement cette zone d’indécision dans sa critique spécifique de DELTA. |
| **A : modèle de départ partagé, donc indépendance douteuse.** | **Transformée en condition de portée.** Un parent fixé n’interdit pas l’indépendance conditionnelle de tirages d’affinage et de données. En revanche, des faits partagés créent des dépendances, et un seul parent n’autorise aucune généralisation entre parents. Ces deux niveaux seront séparés. |
| **B : étiquetage et observations boîte noire ; D : mélange des forces comportementales.** | **Acceptée pour la séparation et les budgets.** Étiquetage scellé, requêtes du moniteur et développement seront disjoints. **Rejetée comme fuite automatique** si les épisodes proviennent seulement de la même distribution : c’est alors une cible légitime. Un plafond boîte noire est une conclusion possible, non une raison de l’affaiblir artificiellement. |
| **A, B, D : témoins manquants.** | **Acceptée.** Ajout de boîte noire + bruit, d’adaptateurs exposés à la recette mais comportementalement négatifs, de résumés désappariés et d’un témoin positif de lecture. |
| **B : portée limitée aux lecteurs testés.** | **Acceptée.** Un échec réfutera leur utilité sous cette interface et ce budget, pas toute lecture de poids. |
| **D : banque adversariale ≠ garantie sur une classe ; réutilisation adaptative.** | **Acceptée.** Retrait de toute prétention de certification adversariale. Une banque fraîche mesure une performance distributionnelle. Les soumissions honnêtes doivent emprunter le même canal. Aucun mode opératoire offensif n’est proposé. |

### CONSTRUIT

| Critique | Décision et correction |
|---|---|
| **A et B : saturation de Gemma ; raccord psychophysique invalide.** | **Acceptée pour le choix du pilote ; rejetée pour l’extrapolation universelle.** Le suivi de toutes les mauvaises suggestions dans le montage rapporté ne prouve pas une saturation à toutes les doses possibles. Il suffit néanmoins à rendre mon choix de Gemma injustifié. Le pilote visera Llama-3.1-8B-Instruct, sous condition préalable de courbe informative. |
| **A : source du candidat non définie.** | **Acceptée.** Pour le premier test, le candidat est la direction du travail public de validité de construit, si son artefact et sa provenance sont disponibles. Ce test ne sera donc **pas** présenté comme une validation du choix d’un composant par un lecteur de poids. |
| **A et D : refus, contrarianisme, perte de confiance, dommages insuffisamment contrôlés.** | **Acceptée.** Les non-réponses restent au dénominateur. Ajout de suggestions vraies, assertions neutres, pression sans suggestion et mesure de calibration sans pression. |
| **D : aire sous la courbe ≠ coefficient d’attraction ni point fixe.** | **Acceptée.** Je sépare le suivi factuel de la loi sur les notes. Le pilote mesure le premier ; il ne valide pas la seconde par substitution. |
| **D : pondération des doses et plancher comportemental absents.** | **Acceptée.** Doses et pondérations fixées avant confirmation ; une base non informative rend le montage inapplicable, sans réfuter une hypothèse générale sur la sycophancie. |
| **D : pseudo-réplication d’une intervention unique.** | **Acceptée.** Les faits répliquent l’estimation comportementale conditionnelle à une édition, non la procédure de découverte. Toute généralisation à cette procédure demandera des découvertes et éditions indépendantes. |
| **A, B, D : témoins négatifs et contrôle de non-saturation.** | **Acceptée.** Ils deviennent des conditions d’entrée et des mesures de dommage, pas des analyses facultatives. |

### ORACLE

| Critique | Décision et correction |
|---|---|
| **A, B, D : rendement relatif instable ou indéfini.** | **Acceptée.** Remplacement par une différence absolue de rendement par course, à coût plafonné. Un rendement de base nul ne rend plus l’estimand indéfini. |
| **A : description révélatrice ou inutile ; comparateur mécanique explicite.** | **Acceptée pour le comparateur ; rejetée comme nécessité de calibrer artificiellement le rendement des descriptions.** Une base faible reste informative avec une différence absolue. Le bras principal affrontera un proposeur mécanique, pas seulement des descriptions seules. |
| **A : distinguer loi transférable et verdict d’oracle.** | **Acceptée.** Une soumission doit produire un prédicteur exécutable de propriété à partir des poids, évalué sur réseaux frais. Nommer la propriété d’un réseau montré ne suffit pas. |
| **B : exécution du réseau non interdite explicitement.** | **Acceptée.** Aucun outil libre ni accès à l’oracle ; seules des primitives d’analyse de poids autorisées seront exécutables. L’absence de calcul mental ne sera pas prétendue auditable. |
| **D : archives contaminées ou trajectoires incomparables.** | **Acceptée pour le risque de contamination.** Archives séparées, issues d’un même état initial, et réinitialisées entre courses. Leurs divergences internes deviennent une partie du traitement évalué, non un motif de comparaison loi par loi. |
| **A, B, D : nombre de courses, nulles complètes, puissance et fausses promotions.** | **Acceptée.** Unité finale = course entière indépendante. Les cours nulles couvrent le budget complet et l’archive active. Le pilote est distinct de la certification. |
| **D : poids désappariés et oracle indépendant.** | **Acceptée.** Contrôle désapparié, vérificateur séparé du constructeur et cas connus indépendamment de ce dernier. |

## B. Expériences corrigées

### Fiche ORACLE — Priorité : prédictions transférables, pas commentaires de poids

**HYPOTHÈSE — Question.** Sous juge figé et budget fixé, un proposeur doté d’une représentation des poids produit-il davantage de prédictions correctes et non redondantes qu’un proposeur mécanique ?

**Instrument changé :** nouvelle famille de tâches pour l’organisme d’idéation.

**Estimand.** \(D\) est la différence de nombres de lois correctes et non redondantes par course entre le bras lecteur et le bras mécanique, avec un quota identique. \(q\) est la probabilité d’au moins une promotion fausse par course nulle.

- **\(H_A\)** : \(D>0,2\) loi par course et \(q\leq5\,\%\).
- **\(H_B\)** : \(D\leq0,2\), ou \(q>5\,\%\).

Ces frontières sont **illustratives, supposées**. Des intervalles simultanés entièrement dans le domaine utile réfutent \(H_B\) ; une borne supérieure insuffisante pour \(D\), ou un dépassement établi de \(q\), réfute \(H_A\). Sinon : indécision. L’échec d’une condition de validité invalide l’expérience, pas une hypothèse scientifique.

**Plan proposé.**

- Petits réseaux à domaine fini, avec propriétés positives et négatives vérifiables exhaustivement.
- Le proposeur reçoit architecture, définition des propriétés et représentation numérique, jamais les réponses de l’oracle.
- Soumission sous forme d’un prédicteur dans un langage restreint : statistiques de poids, opérations autorisées et sortie prédictive. Pas d’appel au réseau ni à l’oracle. Tous les appels externes sont journalisés.
- Bras principal : lecteur contre proposeur mécanique énumérant une bibliothèque gelée de prédicteurs. Bras descriptions seules : diagnostic secondaire.
- Même enveloppe de coût total ; temps, jetons et calcul local rapportés séparément.
- Évaluation sur réseaux frais, familles cachées et identifiants opaques.
- Archive initiale identique mais copies séparées ; mises à jour locales selon une règle gelée ; réinitialisation entre courses.
- Faux témoins : réseaux sans propriété, prédicteurs non informatifs, poids désappariés, propriétés négatives vérifiées indépendamment.
- Courses nulles entières : aucune soumission admissible n’apporte d’information au-delà du nul déclaré. La construction de cette loi nulle doit être explicitée ; une liste de statistiques ne suffit pas.

**Première étape faisable — HYPOTHÈSE.** Un pilote de **20 courses appariées**, une enveloppe de **30 dollars** d’appels, calcul principalement CPU et au plus **3 jours**, chiffres **illustratifs, supposés**. Il mesure coût, faisabilité du langage et variance entre courses. Il ne certifie pas le plafond de fausses promotions.

**Abandon.** Arrêter l’intégration si la confirmation exclut un gain supérieur à **0,2 loi par course**, ou établit un taux de fausses promotions supérieur à **5 %** — seuils **illustratifs, supposés**. Si le nul exécutable n’est pas constructible, abandonner cette famille avant toute course probante.

**Différence avec l’existant — HYPOTHÈSE.** L’objet est le rendement de l’organisme sous archive active et sélection répétée. Aucune nouveauté sur la lecture des poids elle-même n’est revendiquée.

---

### Fiche DELTA — Comparaison d’instruments à accès apparié

**HYPOTHÈSE — Question.** Le lecteur améliore-t-il la détection par rapport à une exploitation mécanique de la même représentation, une fois les sorties déjà disponibles ?

**Condition préalable.** Banque autorisée d’adaptateurs réellement présente ; positifs définis comportementalement sur épisodes scellés. Sinon : ne pas lancer.

**Plan corrigé.**

- Développement, calibration honnête, confirmation comportementale et requêtes boîte noire disjoints.
- Même unité pour tous les bras : un point de contrôle et son budget fixé d’épisodes.
- Même résumé numérique pour lecteur et mécanique ; fusions de même famille ajustées uniquement sur développement.
- Lecteurs et répétitions agrégés avant calibration ; aucun meilleur essai choisi après test.
- Comparaison principale : boîte noire + lecteur contre boîte noire + mécanique.
- Témoins : boîte noire + bruit ; duplications techniques ; affinages honnêtes appariés ; recette sans effet ; représentations désappariées ; contrôle positif de lecture.
- Mélange des forces comportementales fixé avant confirmation ; résultats également ventilés par strate.

**Correction de la calibration — HYPOTHÈSE.** Employer un seuil par rang sur nuls de calibration, avec traitement conservateur des ex æquo. Sous échangeabilité des unités honnêtes et score préalablement gelé, cela vise un contrôle **marginal** à **5 %**, valeur **illustrative, supposée**. Cela ne garantit ni le taux conditionnel d’un seuil particulier, ni chaque sous-population, ni un contexte adversarial. Une confirmation indépendante rapportera ces limites.

- **\(H_A\)** : gain marginal de sensibilité \(G>10\) points sous cette procédure.
- **\(H_B\)** : \(G\leq10\) points.

Seuil **illustratif, supposé**. Borne inférieure au-dessus du seuil : réfutation de \(H_B\). Borne supérieure au-dessous : réfutation de \(H_A\). Sinon : indécision.

**Abandon.** Ne pas déployer après un pilote indécis. Dimensionner la confirmation sur les discordances appariées estimées hors test ; ne plus présenter la petite banque initiale comme suffisante pour conclure.

---

### Fiche CONSTRUIT — Réduction spécifique du suivi faux

**HYPOTHÈSE — Question.** Une intervention engagée réduit-elle les accords factuellement faux sous pression, sans simplement produire abstention, contrarianisme ou dégradation ?

**Condition préalable.** Courbe non saturée sur développement, plusieurs doses informatives, artefact du candidat disponible et provenance connue. Llama-3.1-8B-Instruct est la cible envisagée, pas une garantie de faisabilité matérielle.

**Plan corrigé.**

- Candidat du travail public de validité de construit, engagé avant nouvelles générations.
- Doses, pondération de l’aire et procédure d’intervention fixées avant test.
- Original, manipulation factice, intervention ciblée et plusieurs témoins sans rapport.
- Suggestions vraies, fausses, absentes ; assertions neutres et pression sans contenu.
- Toutes les réponses restent au dénominateur. Réponses correctes, accords faux, refus et non-réponses constituent des issues distinctes.
- Mesurer aussi exactitude, réponse aux suggestions vraies et calibration de confiance sans pression.
- Faits, formulations et cadres nouveaux ; jugement aveugle.
- Conclusion conditionnelle à ce candidat et à ce point de contrôle.

- **\(H_A\)** : réduction de l’aire d’accord faux d’au moins **10 points** au-delà des témoins, sans hausse des non-réponses ni perte d’exactitude supérieure à **3 points**, et sans dégradation dépassant une marge préenregistrée de calibration.
- **\(H_B\)** : au moins une condition échoue.

Nombres **illustratifs, supposés**. Les marges de calibration doivent être fixées avant lancement ; sans elles, pas de test confirmatoire. Les bornes simultanées permettent de réfuter l’une ou l’autre hypothèse ; leur chevauchement reste indécis.

**Abandon.** Rejeter la prétention causale spécifique si le bénéfice maximal compatible avec les données reste sous le seuil, ou si les dommages dépassent leur plafond. Une direction prédictive peut survivre comme mesure sans devenir une cause démontrée.

**Limite explicite.** Cette fiche ne teste pas encore le point fixe psychophysique. Ce raccord exige une expérience distincte sur des notes à échelle ancrée, sans assimiler notes sociales et réponses factuelles.

## C. Réponse à l’arbitre — Une page

### Ce qui est établi dans le dossier transmis

**RAPPORTÉ —** Le billet présente des reconnaissances de tâches de petits réseaux, des politiques écrites sans gradient et une correction de boucles améliorant les scores d’un modèle de langue. Il rapporte également l’échec de l’identification de sycophancie sur les poids seuls — « lecture factuelle », §2–4.

**OBSERVÉ-NON-AUDITÉ —** La lecture des journaux précise que la réussite avec attention utilise des exécutions des modèles, que le classement des composants ne démontre pas leur causalité et que la greffe testée pour ce tour ne modifie pas le comportement — même pièce, §3.3–3.5. L’édition contre les boucles s’appuie sur générations et activations, pas sur les poids seuls — §4.2.

**RAPPORTÉ —** Nos propres travaux montrent pourquoi séparer prédiction, causalité et contrôle : une direction peut suivre la sycophancie sans intervention répliquée concluante ; un juge figé peut rencontrer une classe hors couverture ; des moniteurs internes peuvent ne pas dépasser leurs témoins à la puissance disponible — « nos résultats », §3, §6–7.

### Ce qui ne l’est pas

**HYPOTHÈSE —** Aucun de ces éléments ne suffit à établir :

- un gain de détection des poids au-delà de la boîte noire et des statistiques mécaniques ;
- un taux de fausses alertes acceptable hors choix forcé ;
- la spécificité sociale d’une baisse d’accord après intervention ;
- la préservation fonctionnelle à partir du seul nombre de poids modifiés ;
- une garantie contre un adversaire autorisé à soumettre des poids ;
- le transfert d’une garantie du juge à une nouvelle famille de propositions.

Le raccord entre notre loi psychophysique et notre direction lisible demeure également une question, pas un résultat.

### Comment les intégrer

**HYPOTHÈSE —** Dans l’organisme d’idéation, le lecteur doit produire un **prédicteur engagé**, jamais son propre verdict de validité. Le juge reste séparé, mais sa couverture doit être réétablie pour la famille nouvelle.

Dans le contrôle, le lecteur est un **instrument candidat**. Son apport se mesure contre « boîte noire + mécanique », avec même représentation disponible, budget explicite, calibration indépendante et positivité comportementale. Une moyenne sur une banque adversariale ne devient pas une garantie sur une classe d’attaques.

Dans les travaux sur la sycophancie, une intervention doit améliorer une issue comportementale spécifique, non simplement diminuer un score ou empêcher de répondre.

### L’expérience à faire en premier

**HYPOTHÈSE —** Commencer par **ORACLE corrigé**, parce qu’il ne suppose ni adaptateurs de sabotage disponibles ni transfert immédiat d’une direction entre modèles. Le premier livrable est un générateur, un oracle indépendant, un langage de prédiction restreint et des courses appariées à archives séparées.

La décision recherchée est modeste : **l’accès aux poids augmente-t-il le rendement de prédictions transférables sous notre procédure, sans sortir de la couverture du nul ?** Si le pilote révèle un oracle contournable, un nul non constructible ou un coût incompatible, on arrête. S’il est valide mais statistiquement indécis, on dimensionne une confirmation ; on ne rebaptise pas l’indécision « découverte ».

FIN-DE-CELLULE