Les chiffres d’Avalon-M1 et de Damani repris par A, B et C restent **RAPPORTÉS** : les deux lectures sur PDF sont non contre-lues et non scellées. Les diagnostics ci-dessous sont des analyses de méthode, non des résultats empiriques.

## Sur la proposition A

### (a) Défauts de méthode

- **E1 ne isole pas l’usage d’un moniteur neuf.** Le bras (ii) diffère du bras (iii) par la présence d’une information supplémentaire dans `historique`, donc par la longueur et le contenu du contexte, les actions ultérieures et potentiellement le coût. Même si cette sortie est formellement exclue du score de sélection, elle peut influencer les conceptions futures et donc la composition sélectionnée : son exclusion causale de la sélection n’est pas démontrée. Le « score permuté » ne contrôle ni cette fuite d’information ni un artefact de format ; il dégrade surtout l’apprentissage.
- **E2 présente un biais de spectre.** Les erreurs plantées sont précisément celles que le lecteur outillé de la pièce 5 a déjà su détecter. La banque est donc construite dans la zone de force de ce bras. Le bras « Lean sur énoncé seul » n’est pas un contrôle de la fidélité d’une preuve : un énoncé vrai peut avoir une preuve fautive, et un énoncé formel peut être une mauvaise traduction de l’énoncé source.
- **E3 confond le niveau de crédit avec l’algorithme et les données produites.** « Filtrer par score d’ensemble » et « filtrer par score par bras » changent la distribution des exemples retenus, la variance des scores et parfois l’unité d’attribution — bras ou agent. Une différence de signalement ne serait pas attribuable au seul crédit collectif. Le point de contrôle initial ne remplace pas un témoin sans entraînement suivi dans le temps.
- **E3′ ne peut pas conclure à l’origine dans l’entraînement.** Une absence d’effet de l’effectif à poids fixes n’écarte ni un effet propre à l’entraînement collectif ni une diffusion qui n’apparaîtrait qu’après entraînement. À l’inverse, un effet de l’effectif peut venir du canal partagé, de la longueur du contexte ou de la corrélation entre agents.
- **E4 est en partie non falsifiable.** Si \(C\) et l’appel à \(\rho\) sont observés, la vérification mécanique \(M=\mathbf 1[C\land\neg\rho]\) est exactement la cible « omission ». Elle n’a aucune fausse alerte sur cette définition ; aucune sonde ne peut donc améliorer son rappel à fausses alertes fixées. Le protocole déplace ensuite implicitement la cible vers la *reconnaissance de \(C\)*, sans fournir de vérité indépendante pour cette nouvelle cible.
- **E4 et E5 ne séparent pas assez construction et évaluation.** Trajectoires de plusieurs bras et points de contrôle servent à produire, entraîner et comparer les prédicteurs sans partition explicite par scénario, famille et point de contrôle. Une sonde peut apprendre le bras, le style du point de contrôle ou le nom du scénario. Enfin, l’AUROC marginal d’une confiance de juge ne détermine pas l’utilité d’un vote pondéré : celle-ci dépend de la loi jointe des erreurs des juges. E5 teste une confidence extraite, pas l’apport propre d’un entraînement RLCR.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Seuils fondés sur le A/A.** Si \(S_{z,r}=\mu+\alpha_z+\varepsilon_{z,r}\), avec corrélation intra-famille \(\rho_Z>0\), alors pour \(m\) observations par famille,
  \[
  n_{\mathrm{eff}}\simeq \frac{n}{1+(m-1)\rho_Z}.
  \]
  L’écart-type test–retest \(\sigma_{A/A}\) n’estime pas \(\operatorname{Var}(\alpha_z)\), ni la variance entre graines d’entraînement. Les critères de E1 et E3 surestiment donc leur puissance dès que ces composantes dominent.
- **E3.** Si \(R\sim\mathrm{Bernoulli}(p_{G,Z,T,S})\), où \(G\) est le bras, \(Z\) le scénario, \(T\) le point de contrôle et \(S\) la graine, une comparaison marginale de \(\mathbb E[R\mid G]\) mélange effet du crédit et différences de lois de \(Z,T,S\). Les règles de décision laissent également non jugés les petits écarts et les interactions \(G\times T\).
- **E3′.** La prédiction \(1-(1-p_1)^N\) suppose une indépendance conditionnelle des signalements. Avec une difficulté latente commune \(Z\), la loi indépendante pertinente serait
  \[
  \mathbb E_Z\!\left[1-(1-p_{1,Z})^N\right],
  \]
  et non \(1-(1-\mathbb E[p_{1,Z}])^N\). Une égalité ou une inégalité avec le taux observé ne distingue donc pas diffusion, corrélation et hétérogénéité des scénarios.
- **E4.** Si \(Y=M\) presque sûrement, alors \(\operatorname{AUROC}(M)=1\) et
  \[
  \Pr(Y=1\mid M,X)=\Pr(Y=1\mid M)
  \]
  pour toute sonde \(X\) : le critère d’amélioration est impossible. Si le texte ou la sonde ne varie presque plus conditionnellement à \(Y\), l’AUROC tend vers celle d’une variable constante. Si \(X\) n’informe que par \(T\) ou \(Z\), sa performance ne se transporte pas lorsque \(\Pr(Y\mid T,Z)\) change.
- **E5.** Avec une seule classe dans l’échantillon, l’AUROC est indéfini ; avec une confiance constante, il vaut nominalement \(0{,}5\). Lorsque le taux de base \(\pi=\Pr(Y=1)\) est extrême, \(q=\pi\) peut donner un Brier et une ECE flatteurs sans discrimination. Les intervalles d’AUROC entre \(0{,}55\) et \(0{,}60\) ne sont tranchés par aucune des deux hypothèses.
- **E2.** Le rappel estimé est conditionnel à la loi des erreurs plantées \(P_{\text{banque}}(E)\). Rien ne permet d’en déduire \(\Pr(\text{détection}\mid E)\) sous une autre loi d’erreurs ; une parité sur la banque ne ferme donc pas la question générale.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **E3/E4 :** graines d’entraînement indépendantes, témoin sans entraînement, et partition des scénarios, familles et points de contrôle *avant* tout ajustement de sonde ou de classifieur.
2. **E4 :** cas appariés « condition reconnue mais signalement non dû », « envisagé puis légitimement non fait », \(C\) faux et \(\rho\) émis. Sans vérité indépendante sur la reconnaissance, seule la détection contractuelle de l’omission est jugeable.
3. **E1 :** bras recevant une sortie de moniteur vide ou permutée avec le même coût de contexte, et moniteurs évalués sur des familles absentes de leur construction. Sinon l’effet « moniteur » reste confondu avec l’effet d’information supplémentaire.
4. **E2 :** traductions Lean vérifiées indépendamment, preuves saines et erreurs de classes nouvelles, à l’aveugle.
5. **E5 :** prédicteur constant, probabilité des jetons et évaluation du panel complet sur fiches tenues à l’écart ; les contrôles de confiance permutée seuls ne détectent pas ces fuites.

## Sur la proposition B

### (a) Défauts de méthode

- **N12-E1 mesure un maximum adaptatif, pas un plateau.** Le meilleur score des dernières générations est choisi après observation. Le bras autorisé à générer des pièces explore en outre un espace plus vaste ; à variance égale, il peut obtenir un maximum supérieur sans amélioration de son espérance. L’invite permutée n’est pas un témoin de nouveauté structurelle : elle peut être invalide ou changer le taux d’échec et le coût.
- **N12-E2 est vrai par construction.** Une empreinte garantit l’identité d’un octet, pas une propriété sémantique. Faire rejeter une garde volontairement fautive par Lean, puis constater que SHA-256 ne la rejette pas, ne peut que produire l’issue annoncée. À l’inverse, « aucune propriété au-delà de l’empreinte » n’est pas établi par une absence de formalisation réussie.
- **N13-E1 reproduit le confondant qu’elle prétend lever.** Crédit collectif et individuel ne sont pas nécessairement appariés en échelle de récompense, variance de gradient ou information d’attribution. Le bras avec récompense du signalement est une intervention active sur la métrique, non un contrôle négatif : il peut accroître le signalement dans tous les mécanismes et apprendre le sur-signalement.
- **N13-E2 reprend la cible mécanique parfaite.** L’AUROC de la sonde est comparé à une vérification qui, sous contrat explicite, définit déjà exactement « dû et non fait ». Le cas où la sonde devrait gagner — reconnaissance sans contrat — est une autre variable, sans étiquetage indépendant.
- **N13-E3 confond entraînement, format et calcul de test.** RLCR produit une analyse et une confiance ; le témoin non entraîné reçoit seulement une phrase d’extraction. Un écart peut donc venir des jetons supplémentaires ou du format. Utiliser l’oracle ou un verdict humain comme vérité, sans partition par famille de fiches, expose aussi à l’apprentissage de régularités propres au monde planté ou au labelleur.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **N12-E1.** Pour des scores \(S_j=\mu_j+\varepsilon_j\),
  \[
  \mathbb E[\max_j S_j]\geq \max_j\mathbb E[S_j].
  \]
  Le biais croît avec le nombre de candidats et leur variance. Des générations autocorrélées ne fournissent pas les observations indépendantes requises par un Mann–Whitney ordinaire.
- **N12-E2.** « Au moins une propriété non triviale » n’est associé à aucune loi d’échantillonnage des propriétés ni à un estimateur de sensibilité ou de spécificité. Sur une démonstration unique, \(\widehat{\mathrm{TPR}}\) et \(\widehat{\mathrm{FPR}}\) ne sont pas identifiables.
- **N13-E1.** Des taux calculés sur des agents groupés dans des runs, et des points de contrôle répétés, ont une variance de grappe. La variance du score de développement A/A n’est pas un estimateur de \(\operatorname{Var}(p_{G,S})\) entre entraînements. Les deux hypothèses peuvent aussi être vraies simultanément : baisse générale du renforcement *et* supplément collectif.
- **N13-E2.** Si \(Y=\mathbf 1[C\land\neg\rho]=M\), la différence d’AUROC entre \(M\) et toute combinaison \((M,X)\) est au plus nulle ; un test de DeLong ne peut révéler un gain. Avec des observations groupées ou une séparation parfaite, ses conditions usuelles sont en outre défaillantes.
- **N13-E3.** Si \(\Pr_{\text{train}}(Y\mid X)\neq\Pr_{\text{test}}(Y\mid X)\), une calibration apprise ne se transporte pas nécessairement. Des étiquettes humaines bruitées changent à la fois la loi de calibration estimée et l’AUROC. Le non-chevauchement d’intervalles bootstrap n’est ni nécessaire ni suffisant pour trancher une différence, surtout si le bootstrap ignore les familles.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **N12-E1 :** budgets de recherche et nombres de candidats appariés, scores non sélectionnés par leur maximum, et pièces nouvelles nulles mais valides de même coût.
2. **N12-E2 :** bibliothèque aveugle de gardes saines et fautives, spécifications indépendantes et contrôle de fidélité des traductions formelles ; une seule garde fautive ne suffit pas.
3. **N13-E1 :** plusieurs entraînements indépendants par bras, témoin sans entraînement, récompenses appariées en variance, scénarios sans obligation de signalement et mesure des faux signalements.
4. **N13-E2 :** partition par scénario et point de contrôle avant entraînement des sondes, cas bénins « envisagé et non fait », et évaluation conditionnelle à la vérification mécanique. Le témoin individuel avec récompense du signalement ne doit pas être supposé sans omission.
5. **N13-E3 :** familles de fiches jamais vues à l’entraînement, prédicteur constant, log-probabilités recalibrées et bras appariés en analyse produite et calcul de test.

## Sur la proposition C

### (a) Défauts de méthode

- **Duel 1 mélange deux décisions.** Une fuite de bac à sable peut invalider une course sans établir que la composition N-045 suffit ; réciproquement, une absence de fuite observée n’établit pas la sécurité. Le « plafond » de N-045 n’a pas d’estimateur défini. Les espaces d’action et les coûts de vérification diffèrent aussi entre bras.
- **Duel 2 favorise les deux bras à des endroits différents sans les rendre comparables.** La banque reprend les erreurs déjà détectées par lecture outillée, tandis que Lean dispose d’un autre budget temporel. Une non-compilation n’est pas une fausse réfutation logique. Surtout, Lean vérifie une formalisation, pas automatiquement sa fidélité à l’énoncé source.
- **Duel 3 ne sépare pas ses facteurs.** Le bras individuel combine crédit par sous-rôle et témoin mono-agent, qui change aussi l’organisation. Le passage de \(K=1\) à \(K=3\) modifie horizon, nombre d’événements de récompense et possibilités d’héritage. L’affinage hors ligne ne reproduit pas nécessairement un avantage collectif partagé par jeton. Aucune règle de décision ne porte sur l’interaction censée valider la protection par \(K\geq3\).
- **Duel 3 risque une fuite directe entre récompense et évaluation.** Si les témoins d’intégrité plantés servent à valoriser l’héritage puis à mesurer le signalement, le résultat peut simplement montrer que ces témoins ont été appris. Et si l’effet n’est pas spécifiquement collectif, **c3 ne tombe pas logiquement** : un autre régime peut encore générer les omissions nécessaires.
- **Duel 4 ne teste pas les “représentations” annoncées.** Un gain de sortie peut provenir de l’analyse supplémentaire ou du format. Le test d’injection mesure principalement le canal d’entrée du harnais : si le texte non fiable n’entre pas dans le moniteur, il est sans effet par construction ; s’il y entre, plusieurs méthodes peuvent partager la vulnérabilité.
- **La “pince” peut apprendre le point de contrôle.** Longueur, style télégraphique, famille et bras sont corrélés au signalement dans les trajectoires proposées. Sans évaluation interne au point de contrôle puis transfert à un point tenu à l’écart, une bonne détection ne démontre pas une lecture de l’obligation reconnue.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Duel 1.** Si chaque tentative de fuite est Bernoulli(\(p\)), zéro événement observé ne donne \(\widehat p=0\) qu’au sens du maximum de vraisemblance, jamais \(p=0\). Avec sensibilité du détecteur \(s<1\), la probabilité d’observation est \(ps\), encore plus faible. Les exigences « zéro fuite » et « TPR = 1 » ne sont donc pas certifiables sur un échantillon fini.
- **Duel 2.** Aucune erreur manquée sur quelques mutants n’implique une sensibilité unitaire hors de leur loi. Les estimateurs de rappel sont conditionnels aux classes plantées ; les taux d’échec de compilation mélangent \(P(\text{échec}\mid\text{énoncé valide})\), difficulté de traduction et budget.
- **Duel 3.** Si \(p_{G,K,Z,T,S}\) dépend d’une graine \(S\) non répétée, les effets de \(G\) et \(K\) ne sont pas séparables de la variance entre entraînements. Si l’estimateur de reconnaissance est presque constant ou peu sensible, la condition « reconnaissance constante » peut être satisfaite sans information sur la reconnaissance latente. Si récompense et test partagent les mêmes témoins, \(\Pr(\rho\mid C_{\text{test}})\) estime l’apprentissage du test, pas sa généralisation.
- **Duel 4.** Sous taux de base extrême, une confiance constante minimise parfois les estimateurs usuels de Brier/ECE tout en ayant une AUROC nulle en information. Si la recalibration et l’évaluation partagent la même loi de fiches, ses erreurs sont optimistes. Une ECE absolue n’est pas comparable entre lois de base et distributions de difficulté.
- **Pince.** Si \(X\) prédit \(Y\) uniquement par \(T\) ou \(Z\), alors \(X\) peut avoir une AUROC élevée marginalement tout en étant sans valeur conditionnelle à \(T,Z\). Sous une nouvelle loi \(P'(Y,T,Z)\), cette performance peut disparaître.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Duel 1 :** tentatives connues de franchissement et réécritures bénignes, évaluées par un dispositif externe indépendant, avec estimation des faux positifs et faux négatifs.
2. **Duel 2 :** mutants inédits, preuves saines, traductions formelles contre-lues et comparaison à coût apparié ; délai et échec de compilation doivent être rapportés séparément d’une réfutation.
3. **Duel 3 :** graines indépendantes, témoin sans entraînement, analyse complète des interactions du plan factoriel, et séparation stricte entre témoins de récompense et témoins d’évaluation. Il faut aussi des canaris « à ne pas signaler » distincts et des trajectoires réservées à l’entraînement des sondes.
4. **Duel 4 :** calibration et évaluation disjointes par famille, prédicteur constant, log-probabilités et recalibration post-hoc à données appariées, ainsi qu’un bras sans analyse à calcul de test comparable.
5. **Injection et pince :** contrôles avec et sans canal non fiable, injections positivement détectables, et évaluation de la pince à l’intérieur de chaque point de contrôle puis sur un point entièrement tenu à l’écart.

FIN-DE-CELLULE