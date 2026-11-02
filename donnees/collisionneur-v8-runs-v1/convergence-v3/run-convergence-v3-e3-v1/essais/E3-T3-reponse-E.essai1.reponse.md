# Proposition E — Tour III.3 : corrections et réponse

**OBSERVÉ-NON-AUDITÉ — Pièces absentes :** le pilote complet, les entrées `resultats` du calibrage et le PDF de Bailey ne sont pas servis ; je n’en reconstruis aucun contenu.

**Convention de statut.** Les résultats numériques transmis restent **RAPPORTÉS**. Mes lectures statiques nouvelles du code sont **OBSERVÉES-NON-AUDITÉES** ; les démonstrations algébriques ci-dessous sont **VÉRIFIÉES**, sans valider une exécution. Les expériences corrigées sont des **HYPOTHÈSES de protocole**, non des résultats. Tout nouveau budget ou seuil numérique est **illustratif**.

## A. Réponses aux critiques visant E

### Critiques de A

| Critique | Décision et correction |
|---|---|
| **A(a).1 et A(b), gap local unilatéral** | **Acceptée.** Je retire le duel sur le *gap global* dans le monde continu sans encadrement certifié. Un audit plus puissant ne suffit pas à rétablir sa symétrie. Expérience corrigée **Instrument** ci-dessous. |
| **A(a).2, fuite dans l’extension** | **Acceptée comme risque insuffisamment exclu.** Séparation explicite entre construction, sélection et évaluation ; réoptimisation adverse contre chaque défense figée. Expérience **Extension**. |
| **A(a).3, aucune colonne ne répond au mélange** | **Rejetée dans cette formulation factuelle. OBSERVÉ-NON-AUDITÉ :** dans `trajectoire`, B et B′ construisent des réponses aux mélanges courants. **Acceptée pour le mélange final :** aucune certification n’assure que les colonnes couvrent sa meilleure réponse complète. Une réponse finale supplémentaire devient obligatoire avant toute extrapolation hors matrice. |
| **A(a).4, pile-ou-face ne distingue pas cycle et profil pur exploitable** | **Acceptée.** Le gap valide la qualité stratégique, non la périodicité. Le jouet reçoit des trajectoires stationnaires et périodiques distinctes, dont certaines ont le même gap. L’horizon arbitraire de ma première proposition est retiré. |
| **A(a).5, mécanisme rendant l’oracle moins efficace** | **Acceptée.** La réduction d’un gap local n’est plus le critère principal d’efficacité dans le continu. Les audits adverses et défensifs servent de diagnostics de fragilité, pas de certificats. |
| **A(a).6 et A(b), banque propre** | **Acceptée comme sous-spécification**, non comme description de mon intention : ma banque n’était pas définie comme exclusivement propre. Je sépare désormais propre, lois adverses tenues et contrôles fonctionnels ; aucun seuil commun n’est appliqué aveuglément. |
| **A(a).7, cible historique et banque gelée** | **Constat favorable reçu, sans résultat nouveau.** Je conserve explicitement la cible dans l’historique et précise la séparation des instances de développement et de décision. |
| **A(c), contrôles manquants** | **Acceptés :** audit de chaque intervention, banques séparées, réponse au mélange final, duplications bruitées et défense figée \(M_0\). L’audit ne transforme cependant pas une absence de découverte en garantie globale. |
| **Point commun sur les départs chauds et I3** | **Transformé en test.** Rejouer toute la trajectoire avec une procédure adverse indépendante sans départ chaud, et non simplement réévaluer les anciens moniteurs. Ce test mesure une sensibilité à la procédure ; il n’isole pas à lui seul une « vraie dynamique ». Les retours numériques transmis restent **RAPPORTÉS**, sans changement de statut. |

### Critiques de B

| Critique | Décision et correction |
|---|---|
| **B(a).E1, non-pureté de B donc \(v_{\rm mix}>v_{\rm pur}\)** | **Rejetée. VÉRIFIÉ :** un solveur peut rendre une stratégie mixte alors qu’une stratégie pure atteint la même valeur ; des lignes identiques en donnent un contre-exemple. Le support rapporté ne démontre donc pas l’inégalité stricte. **Acceptée :** mon critère caractérise une matrice et une instance, pas toute une classe fonctionnelle. |
| **B(a).E2, niveaux de preuve** | **Acceptée.** Les sorties porteront des noms distincts : *gap exact fini*, *gap restreint*, *diagnostic par oracles locaux*, *performance contre procédure adverse fixée*. Le dernier n’est pas une robustesse globale. |
| **B(a).E3, implémentation bilatérale** | **Acceptée pour la nécessité d’un nouveau bras déclaré ; rejetée pour la modification supposée de `objectif_lisse`. OBSERVÉ-NON-AUDITÉ :** cette fonction accepte déjà une liste pondérée de moniteurs. La modification porte sur la défense passée à l’oracle et sur l’ordre des mises à jour. |
| **B(b), faiblesse des oracles et de l’extension** | **Acceptée.** Une recherche infructueuse ne tranche pas un plafond global. L’argument proposé de « saturation du sous-espace » reste une **HYPOTHÈSE** : le comptage de paramètres et d’attaques ne le démontre pas. |
| **B(b), incertitude sur \(v_{\rm mix}-v_{\rm pur}\)** | **Acceptée comme précision nécessaire.** J’avais demandé des bornes simultanées sans donner leur propagation ; celle-ci est désormais explicitée. |
| **B(c).1, absence de contrôle du gap** | **Rejetée quant à l’absence :** le jouet et les profils perturbés étaient prévus. **Acceptée quant au manque de valeurs attendues.** Le gap pur annoncé par B n’est pas universel : il dépend de la normalisation des gains et du profil. Valeurs corrigées dans **Instrument**. |
| **B(c).2–3, copies et extraction** | **Acceptées.** Copies exactes, invariance d’échelle et réextractions répétées deviennent des contrôles préalables. L’égalité bit à bit est exigée seulement lorsque l’environnement déterministe la garantit ; sinon, le bruit mesuré doit entrer dans l’incertitude. |

### Critiques de C

| Critique | Décision et correction |
|---|---|
| **C(a).1, extension évaluée sur banque fixe** | **Acceptée pour le défaut d’identification.** Une amélioration du maximin empirique peut être mécanique. **Rejetée pour « gain positif par construction » hors échantillon :** seule la non-diminution de l’optimum sur la banque d’optimisation est garantie. Le contraste corrigé compare bibliothèque étendue et bibliothèque initiale ; D n’est plus son témoin causal principal. |
| **C(a).2 et C(b).1, différence de biais des gaps** | **Acceptée.** C’est une non-identifiabilité, plutôt qu’une simple erreur de signe. Je retire toute conclusion de convergence fondée sur la seule diminution du gap local. |
| **C(a).3, fuite temporelle** | **Acceptée comme risque.** Les hyperparamètres sont gelés sur des instances de développement ; la boucle rouverte décisive utilise des instances nouvelles. |
| **C(b).2, borne par la variation d’une ligne** | **Rejetée mathématiquement. VÉRIFIÉ :** une ligne presque constante ne borne pas les gains des autres lignes. Il manque l’hypothèse reliant leur maximum au minimum de cette ligne. L’écart restreint–final rapporté ne fournit pas cette hypothèse. **Acceptée :** le bruit des extrema doit être propagé. |
| **C(b).3, banque saturée** | **Acceptée qualitativement.** Faible désaccord sur une banque saturée signifie faible désaccord *sur cette banque*, pas stabilité globale. Je n’utilise pas la formule de variance proposée comme certificat général. |
| **C(c).1–3, audits et réévaluation** | **Acceptées avec restriction :** audit séparé de chaque défense, recherche défensive renforcée et matrice fraîche. Un petit écart entre deux audits ne certifie pas leur proximité de l’optimum global. Réévaluer un mélange et un pur sélectionnés mesure leur contraste, pas automatiquement l’écart entre les deux valeurs optimales. |

### Critiques de D

| Critique | Décision et correction |
|---|---|
| **D(a), confusion fini/continu** | **Acceptée.** Aucune transmission automatique de certificat entre ces jeux. |
| **D(a), extension insuffisante et plafond** | **Acceptée.** Je renomme l’expérience : *gain accessible à une procédure d’extension fixée*. Un succès ou un échec n’est plus interprété comme un verdict global sur la classe. |
| **D(a), réglage et causalité B′–D** | **Acceptée.** Instances finales intactes ; \(v_{\rm mix}-v_{\rm pur}\) ne sera pas présenté comme l’effet causal de B′ contre D. |
| **D(b), erreurs et information sur la tâche** | **Acceptée.** L’information observable, la possibilité de conditionner les poids et le calendrier des décisions font partie de la définition du jeu. Les erreurs non bornées interdisent la lecture globale, même avec un intervalle statistique étroit. |
| **D(c), contrôles plantés et fictifs** | **Acceptée.** Ajout d’une extension à gain connu, d’une extension dupliquée, de traitements fictifs à budget égal et de jeux exacts purs/intérieurs. Ces contrôles valident des instruments, pas le mécanisme synthétique lui-même. |

## B. Expériences corrigées

### Règle de décision commune

**HYPOTHÈSE — Protocole.** Chaque expérience définit une quantité précise \(Z\), puis oppose exclusivement :

\[
H_A:Z>m,\qquad H_B:Z\le m.
\]

Une borne inférieure au-dessus de \(m\) falsifie \(H_B\) ; une borne supérieure au plus égale à \(m\) falsifie \(H_A\). Un encadrement traversant \(m\), un arrêt ou un contrôle invalide donnent **non tranché**, jamais validation par défaut.

La marge \(0,02\) provient des faits pour la détection ; sa réutilisation sur une autre métrique reste **illustrative**, à justifier avant gel. Les hypothèses portent sur un horizon fini, jamais sur une convergence asymptotique non assortie d’une borne de vitesse.

### Instrument — distinguer qualité stratégique et mouvement

**VÉRIFIÉ — Exemple algébrique, normalisation illustrative.** Pour

\[
G=\begin{pmatrix}1&0\\0&1\end{pmatrix},
\]

l’équilibre uniforme a un gap nul ; tout profil où les deux joueurs sont purs a un gap égal à l’unité. Une suite constante pure et une suite périodique pure peuvent donc avoir exactement le même gap.

**HYPOTHÈSE — Protocole en cinq lignes.**

1. Épingler une version publique d’OpenSpiel, vérifier sa matrice et sa convention ; recalculer le gap par énumération indépendante.
2. Implémenter séparément réponses au dernier itéré, règle asymétrique de A et jeu fictif bilatéral, avec initialisation et départage gelés.
3. Pour le bilatéral, chaque joueur répond à l’historique de l’autre **antérieur à la mise à jour courante** ; rapporter profils derniers et empiriques séparément.
4. Tester \(H_A:g(\bar p_T,\bar q_T)>m\) contre \(H_B:g(\bar p_T,\bar q_T)\le m\), avec horizon préfixé ; chaque issue réfute l’autre assertion finie.
5. Ajouter selle pure stricte, profil pur figé, trajectoire périodique et trajectoires convergentes fabriquées ; I3 reçoit une nulle adaptée aux égalités, jamais automatiquement celle des déplacements continus.

**HYPOTHÈSE — Test distinct de mouvement.** Sur ces trajectoires connues, tester l’erreur de classification d’un indicateur dynamique contre une tolérance préfixée. Un indicateur qui confond profil figé exploitable et cycle est rejeté pour cette tâche, même si le calculateur de gap est correct.

### Extension — gain accessible, sans promesse de plafond

**HYPOTHÈSE — Cible opérationnelle.** Pour une procédure adverse préfixée \(\mathcal A\), définir

\[
R_{\mathcal A}(p)
=\mathbb E_{\xi}\,u\!\left(p,\theta_{\mathcal A}(p;\xi)\right).
\]

L’attaque trouvée est sélectionnée avant une évaluation fraîche. Cette quantité décrit la performance contre une procédure, **pas** l’infimum global.

**HYPOTHÈSE — Duel.**

\[
Z=\mathbb E\!\left[R_{\mathcal A}(p_{\rm étendu})
                   -R_{\mathcal A}(p_{\rm initial})\right].
\]

- Construction et sélection de l’extension sur données dédiées.
- Défenses finales gelées avant évaluation ; procédure adverse réoptimisée séparément contre chacune, à budget égal.
- Évaluations fraîches appariées ; plusieurs réalisations indépendantes de la procédure.
- Contrôles : extension dupliquée, extension positive plantée dans un jeu fini, traitement fictif à budget égal.
- Analyse principale sur tâches nouvelles ; sous-groupe « pur » défini par un diagnostic préalable indépendant.

**HYPOTHÈSE — Réfutations.** Gain établi : réfutation de l’absence d’effet accessible à cette procédure. Gain exclu : réfutation de l’effet annoncé pour cette procédure. **Aucune issue ne certifie un plafond de classe.** Si D est ajouté, il reçoit le même budget supplémentaire et forme un contraste secondaire distinct.

### Posabilité — avantage du mélange dans un jeu explicitement restreint

**VÉRIFIÉ — Propagation déterministe.** Posons \(d(G)=v_{\rm mix}(G)-v_{\rm pur}(G)\). Si toutes les cellules de \(\widehat G\) sont à distance au plus \(\rho\) de celles de \(G\), chacune des deux valeurs change d’au plus \(\rho\). Donc :

\[
d(G)\in
[d(\widehat G)-\rho-\rho,\ d(\widehat G)+\rho+\rho].
\]

Cette propriété fournit un encadrement à partir de bornes simultanées sur les cellules ; elle ne borne pas les stratégies absentes.

**HYPOTHÈSE — Duel.** \(H_A:d(G)>m\) contre \(H_B:d(G)\le m\), pour une bibliothèque et une banque adverses fixées avant l’évaluation fraîche.

**HYPOTHÈSE — Contrôles et extension de portée.**

- Matrices à selle pure, équilibre intérieur et lignes dupliquées ; versions exactes puis bruitées.
- Copies évaluées sur points communs pour l’invariance mécanique, puis graines indépendantes pour tester la calibration statistique.
- Réponse adverse indépendante au mélange final et aux purs candidats ; toute extension de la banque est suivie d’une nouvelle évaluation.
- Succès : mélange nécessaire à la marge près **dans le jeu restreint défini**. Échec : cette nécessité n’est pas présente à cette marge. Ni résultat ne tranche B′ contre D ou toute la classe continue.

### Mécanismes — remplacer le faux certificat global

**HYPOTHÈSE — Plan corrigé.** Historique pondéré, ancrage fonctionnel, objectif pire cas et élargissement de classe sont d’abord comparés sur une banque d’entraînement commune. Leurs réglages sont ensuite gelés avant des trajectoires nouvelles. Pour chaque intervention, le duel porte sur son gain de \(R_{\mathcal A}\), non sur une réduction de gap local.

**HYPOTHÈSE — Diagnostics obligatoires.**

- Audit adverse indépendant avec composante sans gradient, et recherche défensive renforcée.
- \(M_0\) figé ; copies exactes ; transformations positives du score et du seuil.
- Désaccord rapporté séparément sur propre et lois adverses tenues ; taux de saturation explicités.
- Pour des horizons prolongés : classe déployée fixe et budget d’entraînement par loi contrôlé. Toute autre convention constitue un bras distinct.
- Sensibilité de trajectoire : duel sur la différence d’I3 entre procédure adverse initiale et procédure indépendante sans départ chaud. Une différence établie réfute l’insensibilité à l’oracle ; son exclusion réfute seulement une sensibilité supérieure à la marge choisie.

**HYPOTHÈSE — Arrêt interprétatif.** Un audit stable autorise une conclusion sur \(R_{\mathcal A}\), pas sur le gap global. Un gain accompagné d’une perte sur les cas récents reste un compromis.

## C. Réponse à l’arbitre — une page

### Ce qui est établi, et à quel niveau

**RAPPORTÉ.** A réentraîne un moniteur linéaire sur l’historique uniforme, cible initiale comprise. Le pilote rapporte peu de progrès de détection, des retours angulaires élevés et une pureté fréquente de B′ dans son jeu restreint. Ces observations ne sont pas une démonstration de cycle asymptotique.

**VÉRIFIÉ — Formalisation conditionnelle.** Avec un ensemble fixe de moniteurs admissibles au taux de fausses alertes et un ensemble fixe de lois adverses, le gain

\[
u(m,\theta)=\Pr_{Q_\theta}[m(X)>t_m]
\]

définit un jeu à somme nulle si les deux joueurs maximisent et minimisent respectivement ce même gain. La règle idéalisée de A répond à l’historique côté défenseur et au dernier moniteur côté attaquant : elle n’est pas le jeu fictif bilatéral.

**VÉRIFIÉ.** La contrainte de fausses alertes n’interdit pas cette formalisation. En revanche, entraînement sur substitut, calibration empirique et optimisation locale doivent être distingués des meilleures réponses exactes. À gains évalués exactement, les réponses locales fournissent un diagnostic inférieur au gap global ; avec Monte-Carlo, il faut encore encadrer l’erreur d’évaluation.

### Ce qui ne l’est pas

**HYPOTHÈSES non établies :** périodicité de A ; oubli catastrophique comme cause ; plafond de la classe complète ; optimalité globale des défenses ; inutilité du tirage ; transfert aux sondes réelles.

**VÉRIFIÉ.** Un jeu à selle pure suffit à réfuter l’inévitabilité générale des cycles. L’absence de selle pure interdit seulement la convergence vers une selle pure ; elle ne démontre ni périodicité ni convergence des fréquences.

**RAPPORTÉ — Conditions théoriques à vérifier dans les sources.** Le jeu fictif bilatéral en jeu fini à somme nulle concerne les stratégies empiriques, pas une garantie générique sur le dernier moniteur de A. Le double oracle demande des réponses globales et un critère d’arrêt approprié. Extragradient ou optimisme demandent une structure adaptée, notamment convexe-concave ou monotone ; elle n’est pas établie pour l’entraînement paramétré servi.

**HYPOTHÈSE — Conséquences pratiques.** Pondérer l’historique, régulariser, élargir la classe ou changer l’objectif peut améliorer une performance opérationnelle, mais chaque intervention peut aussi modifier le jeu, son coût ou sa réactivité. Aucune ne reçoit ici une garantie générique de convergence. Les comparaisons doivent conserver l’information observable, les classes et les budgets, ou déclarer leur changement.

### L’expérience à faire en premier

**HYPOTHÈSE — Priorité : l’expérience Instrument sur jeu fini exact.** Elle est nécessaire avant de dépenser davantage sur les trajectoires synthétiques. Elle doit montrer séparément :

- que le gap détecte l’exploitabilité ;
- qu’un profil figé exploitable n’est pas appelé « cycle » ;
- que moyennes empiriques et derniers itérés sont correctement distingués ;
- que les égalités et supports finis ne reçoivent pas une nulle d’I3 inadéquate.

Ensuite viennent **Extension** et **Posabilité**, sans certificat global indu.

**HYPOTHÈSE — Transfert.** Sur sondes d’activations, détection tenue, fausses alertes, désaccord fonctionnel et stabilité d’extraction sont mesurables. Une NashConv globale reste non certifiée sans espaces stratégiques et oracles adéquats.

**RAPPORTÉ — Sources attribuables, non vérifiées sur PDF ici :** Julia Robinson, 1951, *An Iterative Method of Solving a Game* ; H. Brendan McMahan, Geoffrey J. Gordon et Avrim Blum, 2003, *Planning in the Presence of Cost Functions Controlled by an Adversary* ; Constantinos Daskalakis, Andrew Ilyas, Vasilis Syrgkanis et Haoyang Zeng, 2018, *Training GANs with Optimism*. Pour les résultats publiés sur les sondes et pour Bailey : **référence à vérifier** ; aucun résultat de transfert revendiqué.

FIN-DE-CELLULE