**Contrôle des pièces.** Le rappel chiffré de la question contredit la synthèse v2 : celle-ci compte **17 inexactitudes et une affirmation non trouvée, dont cinq majeures**, I21 comprise. Je retiens la v2. Ci-dessous, « VÉRIFIÉ » signifie vérifié par son lecteur sur le papier, non revérifié par moi ; le papier, le code de l’orchestrateur et les journaux ne sont pas servis.

## (a) Résolution des divergences

### 1. Valeur de \(n\)

**Je maintiens : \(n\) est non identifiable avec les pièces disponibles.** Les choix \(n=3\) de B et \(n=6\) de C sont des **HYPOTHÈSES**, non des conséquences du contexte : un lot de six fiches n’établit ni une division \(6\to2\times3\), ni une croissance \(6\to12\) suivie d’une division, ni même l’existence d’une division au sens du papier.

Il faut le code de formation, de croissance, de scission et de retrait des lots, puis la définition de l’instant où \(n\) est mesuré. Sans scission ou partage de lot, la bonne réponse est « \(n\) non défini pour cette cible », pas une interpolation entre B et C. Cette identification est préalable aux calculs à \(n=3\) ou \(n=6\).

**Duel déterministe.** \(H_A\) : la règle réelle implémente \(n=3\) ; \(H_B\) : elle implémente \(n=6\). Métrique : concordance exacte entre le code et des traces synthétiques couvrant formation, croissance, scission et retrait ; seuil : une seule divergence réfute la règle candidate. Contrôle négatif : un orchestrateur sans scission, seulement avec rééchantillonnage. Observer \(n=3\) falsifie \(H_B\), observer \(n=6\) falsifie \(H_A\), toute autre règle falsifie les deux identifications fixes.

### 2. Identité de \(q\)

**Je maintiens qu’aucun scalaire \(q\), au sens du papier, n’est identifié dans l’organisme.** La définition de C identifie utilement \(q_{vv}=P(\text{fiche vraie}\mid\text{paire vraie–vraie})\), mais elle ne suffit pas : il faut au minimum \(q_{vf}\), \(q_{ff}\), le rendement du bras à un parent, les consommations de parents et les taux d’erreur du juge, par type de paire.

Le transfert \(q=q_{vv}\) reste une **HYPOTHÈSE**, subordonnée à la validation du noyau : stérilité des autres voies, tirage et retrait connus, budget d’événements fixé. Les taux bruts issus d’un juge partageant ses biais avec le bisociateur ne sont pas des mesures de fidélité.

**Duel trans/cis.** \(H_A\) : seule une paire vraie–vraie produit du vrai ; \(H_B\) : une voie alternative — un parent, paire mixte ou paire fausse–fausse — produit du vrai au-dessus d’une marge \(\delta\) fixée avant les données. Métriques : taux de naissances vraies par occasion, débiaisés sur mondes plantés. Seuils : marge de fertilité et marge d’équivalence à zéro définies par simulation et puissance. Contrôles négatifs : aucun parent, deux fiches fausses et rembourrage inerte de même longueur ; contrôle positif séparé : paires vraie–vraie. Une voie alternative positive falsifie \(H_A\) ; des bornes supérieures inférieures à \(\delta\) sur toutes les alternatives, avec \(q_{vv}\) mesuré positif, falsifient \(H_B\).

### 3. Pince et arène

**(i) Je maintiens qu’aucune prédiction du papier n’est actuellement transposable à la pince.** La candidate P9, reprise de C, ne deviendrait testable qu’après démonstration que la pince possède une unité qui se reproduit par paires et que son tri réalise effectivement une division conservant des paires. Or la réserve du lecteur est fondée : un juge qui promeut des fiches n’est pas, par construction, une règle de division ; il peut relever d’une discrimination \(\theta<1\), ou d’un noyau hors modèle.

La condition de levier de C est donc une **HYPOTHÈSE de correspondance**, pas un résultat acquis. Même validée, elle resterait nécessaire, non suffisante : I11 interdit d’en déduire le maintien de la défense.

**(ii) Dans l’arène, je maintiens l’inapplicabilité globale au régime adaptatif, mais j’admets un régime local gelé.** Générateur, défense, invites, poids et budgets doivent être figés ; les familles d’attaques doivent être séparées entre réglage et évaluation. L’applicabilité à ce régime est une **HYPOTHÈSE**, non une conséquence du gel.

Le duel minimal oppose \(H_A\) « noyau stationnaire et prédictif sous gel » à \(H_B\) « dérive ou erreur structurelle persistant même sous gel ». Métriques : dérive des taux par type de paire et erreur prédictive sur blocs futurs ; seuils fixés sur données synthétiques stationnaires. Contrôle négatif : chronologie permutée dans un simulateur stationnaire. Une dérive excédant le seuil falsifie \(H_A\) ; des prédictions exactes dans la tolérance étalonnée falsifient \(H_B\), sans valider pour autant l’arène adaptative.

### 4. Extinction quadratique à fécondité infinie

**Je maintiens l’objection de D : la fécondité infinie seule ne démontre pas l’extinction.** Le calcul de C établit des naissances vraies en \(O(1/N^2)\) **par événement**, sous ses hypothèses de tirage ; passer à une trajectoire exige le nombre d’événements par génération, les retraits, la dilution et le nombre de descendants par événement.

L’extinction peut tenir si les paires sont uniformément tirées, les voies mixtes et spontanées stériles, et si le budget d’appariements ne compense pas la raréfaction quadratique devant une perte au moins linéaire en fiches vraies. Elle tombe notamment avec un parent unique fertile, des hybrides fertiles, de la copie spontanée ou un appariement assortatif. Ces conditions de transfert sont des **HYPOTHÈSES**, non des théorèmes du papier.

Le test décisif mesure le taux de croissance à faible densité vraie, à noyau et budget fixés. \(H_A\) prédit une croissance négative ; \(H_B\) une invasion persistante positive. Le seuil et la marge d’équivalence sont fixés par le noyau simulé. Le contrôle négatif « uniquement des fiches fausses » doit produire zéro naissance vraie. Une invasion reproductible falsifie \(H_A\) ; une extinction avec borne supérieure sous la marge de persistance falsifie \(H_B\).

### 5. Source de la première mesure

**Je maintiens : première mesure empirique prospective, lecture des journaux seulement après scellement.** Je précise toutefois que l’audit du code, les simulations et les mondes plantés au processeur viennent avant cette expérience prospective ; ils ne constituent pas une lecture des journaux.

Les journaux existants introduisent un risque de choix post hoc des estimands, des périodes et des familles, ainsi que les biais du protocole ayant produit les données. Les nouveaux appels évitent ce premier biais, mais introduisent une dérive de distribution et un coût ; ils ne sont pas automatiquement représentatifs de la course 2. Après préenregistrement, les journaux peuvent servir de réplication secondaire, jamais pour réparer un estimateur ou choisir un seuil.

### 6. Destruction contre archivage

**Je modifie ma position initiale : archivage hors du vivier par défaut, avec réinjection seulement contrôlée.** Je renonçais auparavant à toute réinjection ; j’accepte désormais une quarantaine réversible parce que l’archivage conserve l’option de mesure, sans avantage dynamique établi pour la destruction.

L’équivalence dynamique n’est **VÉRIFIÉE dans le papier que sous conditions** : brouillon effectivement hors du vivier et même probabilité d’arrêt pour tous les modèles (synthèse, section 6 : p. 56, l. 4043-4052). Son application à l’organisme reste une **HYPOTHÈSE**. La mesure minimale est donc double : audit de toute voie de retour, puis estimation de \(\tau\) par type de paire avec troncature exogène comme contrôle.

## (b) Politique consolidée sur les fusions inachevées

### 1. Acceptation et modifications

**J’accepte la politique consolidée avec trois réserves.**

1. La condition \(\theta'<2(1-\tau)\) ne crée pas un droit général à garder les brouillons : le bain stationnaire est numérique et son seuil conjectural (synthèse, section 6 : p. 59, l. 4286 ; p. 21, l. 1782-1783).
2. Après I12, on ne peut plus présenter le bain comme supérieur au rejet pur : le comparateur de la p. 59 est « copies rapides seules, copies lentes perdues », tandis que perdre toutes les copies inachevées ne coûte rien sur la charge à fécondité infinie (p. 59, l. 4278-4281 ; p. 10, l. 863).
3. La réinjection exige une mesure séparée de \(\theta'\), \(q_B\) et \(\tau\), l’absence d’appariement brouillon–brouillon et un budget constant. En sort recopiable, le papier donne aussi une dégradation du plafond dès que \(\theta'\geq\min(\theta,1)\) (p. 56, l. 4078-4080) : le seul coude du bain ne suffit donc pas à certifier l’innocuité.

### 2. Testabilité avant les journaux

**Les trois options sont testables avant lecture, mais pas toutes par une comparaison dynamique.** Détruire et archiver hors vivier sont indistinguables par les trajectoires si l’archive ne réinjecte rien et si \(\tau\) est indépendant du statut : le test décisif est alors l’audit du code et la mesure de \(\tau\), non un essai de survie.

Garder dans le vivier est testable prospectivement après randomisation des sorts et mesure séparée des paramètres. La course 2 n’est pas nécessaire ; ses trois bras sont de toute façon insuffisants pour plusieurs tests décisifs selon les calculs de puissance rapportés.

### 3. Origine de ma position

**Ma position vient du papier pour le défaut hors vivier ; le cadrage a pu renforcer l’accord général.** Les passages décisifs sont le coût exact \(1/(1-\tau)\) et sa condition sur \(\tau\) (synthèse, section 6 : p. 8, l. 703 ; p. 56, l. 4049-4052), la dégradation en sort recopiable (p. 56, l. 4078-4080), et la disparition du bain par re-troncation (p. 59, l. 4304-4306). Aucun ne justifie « toujours détruire » ni « toujours conserver ».

## (c) Prédictions et travaux

### 1. Tri des douze prédictions

| Prédiction | Classement | Correction ou raison |
|---|---|---|
| **P1** | **A** | Estimateur invalidé, aucune mesure de remplacement ; sous ses conditions, la borne du prix implique déjà le résultat. Un test du transfert doit être reconstruit, pas rapiécé. |
| **P2** | **F** | Conserver les taux par type de paire ; justifier le seuil 0,02, déjà marqué illustratif, et retirer la dérive négative tant que la surmartingale n’est pas prouvée pour le noyau réel. |
| **P3** | **F** | Employer la règle de seuil de D, non la formulation qualitative de B ; ajouter rembourrage inerte, randomisation cis/trans et coût réel des appels. |
| **P4** | **F** | Ne pas figer \(n=6\) avant l’audit ; recalculer le noyau, étalonner \(\hat\rho\), justifier puissance et seuils illustratifs, et supprimer l’attente « bain meilleur que rejet ». |
| **P5** | **S** | Duel vivier/quarantaine à \(\Delta\rho\), seuil nul, estimateur étalonné ; préenregistrer troncature exogène, budget constant et contrôle inerte. |
| **P6** | **F** | Fixer la taille d’effet minimale et refaire la puissance ; la course 2 est non jugeable pour ce test. |
| **P7** | **S** | Sous réserve que l’audit permette de séparer toute injection exogène ; sinon il faut reformuler l’estimand avant scellement. |
| **P8** | **S conditionnelle** | Uniquement après validation du noyau littéral à \(\theta=1\) ; ce n’est pas une prédiction globale pour l’organisme. |
| **P9** | **A** | La correspondance pince–levier est précisément ce qui reste à démontrer ; une condition nécessaire ne suffit pas à sauver la prédiction. |
| **P10** | **S** | Test arithmétique asymétrique : certificat revérifié ou contre-exemple reproduit ; un échec de certification seul ne change pas le statut de H2. |
| **P11** | **A** | Prédiction qualitative sans grandeur ni seuil ; I21 supprime en outre son premier appui numérique. |
| **P12** | **S, hors papier** | Prédictions d’ingénierie recevables sur données prospectives, mais sans valeur de validation du transfert des théorèmes. |

### 2. Ordre des travaux

**J’accepte l’ordre, avec une contrainte de dépendance plus stricte.** L’audit du code doit trancher l’existence de \(n\), la règle de division, le budget, les retraits et les injections avant tout calcul présenté comme « noyau réel ». Les bornes générales et les tables déjà disponibles peuvent néanmoins être lues immédiatement.

Étalonnage de l’estimateur et calculs de puissance précèdent obligatoirement le préenregistrement : si \(\hat\rho\) ne distingue pas les matrices de contrôle \(\rho=0{,}95\) et \(\rho=1{,}05\), la course 2 est déclarée non jugeable pour l’allumage avant ouverture. La certification de H2 peut avancer en parallèle, sans bloquer l’organisme. Aucun journal n’est lu avant scellement et contre-lecture ; les runs coûteux attendent devis et GO.

### 3. Recodage des noyaux exacts

**Difficulté estimée : modérée avec le texte intégral du papier ; impossible à garantir avec la seule synthèse.** La forme \(K=BH+2^{1-2n}I\), les types \(f\geq2\) et la recherche de Brent sont rapportés (synthèse, section 9 : p. 17, l. 1577-1586), mais les définitions complètes de \(B\), \(H\), des conditions de bord et des règles de division ne figurent pas dans les faits.

Le recodage doit être indépendant et validé contre la Table S1a, la Table S2, la valeur limite \(\ln2\) et les bornes générales. Les extensions à deux parents, à la règle réelle de division et aux petites fécondités non tabulées sont plus difficiles que la reproduction des tables binomiales.

### 4. Effet des inexactitudes majeures

**Oui, principalement sur P4 et P11.** I4 et I10 invalident les fécondités tirées de la loi asymptotique ; elles ne fournissent donc aucun seuil de secours à P1 ou P11. I11 réduit le levier à une condition nécessaire, mais P9 est abandonnée surtout pour défaut de correspondance.

I12 impose de reclasser **P4 en F** tant que son hypothèse de fond reste « le bain bat le rejet » : l’expérience reste utile pour mesurer un domaine éventuel du bain, pas pour confirmer cette supériorité. Enfin, **I21**, omise du rappel de la question, invalide \(U_c\simeq0{,}450\) à \(n=3\) et le \(q>0{,}638\) de B ; elle confirme l’abandon de P11.

### Instruments : mesures minimales de fonctionnement

| Instrument | Cas honnêtes appariés et métriques | Contrôles mécaniques à battre |
|---|---|---|
| **Juge de vérité** | Mondes plantés, appariés par longueur, difficulté et type de paire ; taux de détection et fausses alertes par type, avec intervalles. Cas négatifs sans parent et fausse–fausse. | Re-calculs, tests unitaires, vérification de schéma ou de preuve lorsqu’ils existent ; juge à étiquettes permutées comme contrôle négatif. |
| **Estimateur spectral** | Matrices connues, y compris creuses, non connexes et à biais de survie, aux effectifs réels ; couverture et erreur de classement autour de \(\rho=1\). | Moyenne de filles par mère et estimateur trivial ; s’il ne sépare pas les contrôles, aucun seuil spectral. |
| **Pince** | Attaques futures tenues à part et cas bénins appariés par famille et difficulté ; détection à budget de fausses alertes fixé, gain du tri réel sur tri fictif à quota égal. | Vérifications déterministes, pince sans mise à jour et chaque bras seul ; mesurer aussi la corrélation des erreurs des deux boîtes. |
| **Arène gelée** | Mêmes attaques aveugles contre défense figée, plus cas sans attaque ; taux de réussite, fausses alertes et gain prospectif. | Rejeu mécanique, vulnérabilités témoins et générateur figé ; toute adaptation est évaluée comme régime séparé. |
| **Bisociateur** | Paires honnêtes appariées et mondes plantés ; \(q_{vv},q_{vf},q_{ff}\), rendement cis/trans à budget constant. | Copie à un parent, paire aléatoire, rembourrage inerte et absence de saut d’espace ; aucun de ces tests ne mesure seul l’allumage. |

### Ancrage matériel et coût

Les noyaux, énumérations, calibrations et mondes plantés peuvent tourner sur processeur, sans modèle génératif. Pour les bras prospectifs, je propose **deux modèles ouverts de provenance distincte**, poids, invites et budgets gelés, l’un ne servant pas automatiquement de juge à l’autre ; leur indépendance d’erreur doit être mesurée, non présumée. Aucun modèle précis n’est imposé par les faits.

**Coût illustratif** : recodage et validation des petits noyaux, quelques jours-personne et moins d’un jour de calcul processeur ; calibrations et simulations, quelques jours processeur supplémentaires. Les appels aux modèles ou l’usage local de GPU ne sont pas chiffrables sans nombre de lots, longueur des invites et tarifs : devis préalable obligatoire, et aucun de ces runs ne peut être qualifié de « sans coût ».

FIN-DE-CELLULE