**Statuts.** Les contenus de B et C sont traités comme **RAPPORTÉS** ; les sorties numériques du manuscrit non relues ici comme **OBSERVÉ-NON-AUDITÉ**. Les implications algébriques ou logiques explicitées ci-dessous sont **VÉRIFIÉES**. Les protocoles que je propose sont des **HYPOTHÈSES** de méthode, pas des résultats.

## Sur la proposition A

Pièce A absente (statut REFUS) : aucune critique de son contenu n’est possible.

## Sur la proposition B

### (a) Défauts de méthode

**1. La prédiction globale utilise des paramètres que B vient de déclarer non définis.**  
B écrit que \(q\) n’a « aucun » correspondant dans l’organisme, puis calcule une condition d’allumage exigeant \(q>0{,}638\). De même, \(n=3\) repose sur une lecture non établie du protocole : six fiches par lot ne dit ni quelle est la taille de naissance, ni quelle est la règle de division. La prédiction scellée de non-allumage n’est donc pas une conséquence du modèle ; c’est une intuition numérique attachée à des variables non identifiées.

**2. La première « prédiction » confond charge d’erreur et fraction de fiches fonctionnelles.**  
Le plafond \(\ln 2\) porte sur un seuil de charge \(U=-\ln q\), non sur un doublement de la fraction fonctionnelle. L’estimateur proposé,
\[
\widehat G=\frac{\text{fraction fonctionnelle dans les lots}}
{\text{fraction fonctionnelle dans le pool permuté}},
\]
n’est ni un estimateur de \(U_c\), ni un estimateur de \(\rho\), ni un estimateur du bonus \(\Delta U\). Le seuil \(\widehat G=2\) est donc sans lien démontré avec le théorème.

La permutation rend en outre l’assignation aveugle **par construction** : elle impose une hypothèse du théorème au lieu de la tester. Une différence entre condition originale et condition permutée mélange sélection du directeur, composition des lots, finitude de la population et historique des fusions.

**3. Le test du prix ne teste pas la linéarité et confond taille et budget.**  
À nombre total de fiches constant, faire varier \(n\) change aussi le nombre de lots, la diversité disponible par lot et, à budget de fusions fixe, la fécondité par fiche. Taille \(n\), fécondité \(R\), nombre de réplicats indépendants et sélection varient ensemble.

Les règles « rapport \(>2\) » et « rapport \(<1{,}5\) » ne distinguent pas « \(R_{\min}\propto n\) » de « \(R_{\min}\) indépendant de \(n\) » : une croissance non linéaire peut produire le premier cas, et une croissance faible mais non nulle le second. Le contrôle à lots de taille un, où \(R_{\min}\) est indéfini, n’est pas un contrôle négatif de la relation taille–prix.

**4. Le proxy de \(\theta'\) mesure la politique de réutilisation, pas seulement l’avantage du fragment.**  
Le taux de réutilisation dépend de la longueur, de l’ancienneté, de l’exposition dans le vivier, du sujet, du tireur et du juge. Il ne sépare pas l’avantage de modèle \(\theta'\) de ces variables.

Surtout, B affirme qu’un fragment « très fertile » envahit et élimine les idées complètes. C’est une contradiction interne : dans le mécanisme invoqué, les tronqués sont recopiés en tronqués et ne régénèrent jamais de réplicase. Un fragment réellement fertile introduit précisément la transition absente de ce mécanisme. Ni \(\theta'\) seul ni le taux de réutilisation ne suffisent alors à prédire la toxicité.

**5. Le bain lent et le sort perdu sont fusionnés à tort.**  
Le coût exact \(1/(1-\tau)\) concerne le sort perdu. Il ne décrit pas automatiquement une copie lente recopiable : celle-ci peut aussi déplacer la charge, former un bain dans des conditions particulières, ou se re-tronquer. La réponse « jeter si \(\theta'>2\), garder sinon » est donc trop courte : il manque au moins la re-troncation et la fertilité résiduelle du fragment.

**6. Les calibrations du bisociateur et du moniteur réutilisent potentiellement le même juge pour construire et évaluer.**  
Si le statut « fonctionnel » sert à sélectionner les fiches puis à mesurer le gain, le critère récompense l’accord avec le juge, pas nécessairement la fertilité. Les tests binomiaux supposent des essais indépendants, alors que paires, parents, mondes et invites sont partagés. Enfin, des taux agrégés de détection et de fausses alertes ne renseignent pas sur la résistance à un attaquant adaptatif.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

Soit \(Z=1\) si une descendante est réellement fonctionnelle, \(\widetilde Z\) son statut jugé, et \(g\) le type de paire. Posons
\[
q_g=P(Z=1\mid g),\qquad
a_g=P(\widetilde Z=1\mid Z=1,g),\qquad
b_g=P(\widetilde Z=1\mid Z=0,g).
\]
Alors le taux observé est
\[
\widetilde q_g=a_gq_g+b_g(1-q_g)
\]
(**VÉRIFIÉ**, simple décomposition). Il n’identifie \(q_g\) que si \(a_g,b_g\) sont connus ou estimables. Si \(a_g,b_g\) varient avec le monde, le type de paire ou l’historique de sélection, un seul \(\widehat q\) mélange ces lois.

Les critères de B deviennent non jugeables dans les cas suivants :

- **Gain \(\widehat G\)** : si le juge impose un quota ou une fraction presque constante de réussites, sa variance ne permet plus de distinguer les conditions. Si aucune matrice de descendance \(K_{f,f'}\) n’est définie, \(\rho(K)\) n’est pas un estimand ; a fortiori, le signe de \(\rho-1\) n’est pas mesurable.
- **Prix** : pour une définition explicite
  \[
  R_{\min}(n)=\inf\{R:P(T>t_0\mid n,R)>\delta\},
  \]
  \(R_{\min}\) est non identifiable si les valeurs de \(R\) ne se recouvrent pas entre tailles, si le budget censure avant \(t_0\), ou si la survie n’atteint jamais \(\delta\). Si toutes les fiches d’un lot partagent leur sort avec corrélation intraclasse \(1\), le nombre de fusions n’augmente pas le nombre de réplicats indépendants.
- **Toxicité des fragments** : si les brouillons archivés ont exposition nulle, leur taux de réutilisation conditionnel au vivier n’est pas estimable. Si la loi de régénération \(q_B=P(Z=1\mid\text{fragment parent})\) n’est pas estimée, deux mécanismes exclusifs — bain sans régénération et complémentation fertile — produisent la même réutilisation agrégée.
- **Moniteur** : le rappel est indéfini sans cas positifs et le taux de fausses alertes sans cas négatifs. Sous adaptation, \(P(S_t=1\mid D_t,H_{t-1})\) dépend de tout l’historique \(H_{t-1}\) : un taux de détection stationnaire par tour et les intervalles binomiaux associés ne sont plus définis sans hypothèse supplémentaire.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Juge indépendant, sur mondes et paires jamais utilisés pour construire l’instrument**, avec paires tout-vrai, tout-faux et mixtes, et estimation de \(a_g,b_g\). Sans cela, gain, \(q\), \(\theta\) et fertilité des fragments peuvent être des artefacts du même juge.
2. **Permutation des statuts et des expositions**, pas seulement des fiches entre lots : elle détecte un « effet protocelle » produit par longueur, ancienneté ou fréquence de présentation.
3. **Branchement synthétique à rayon spectral connu**, pour vérifier que l’estimateur employé retrouve effectivement le signe de \(\rho-1\). Une fraction fonctionnelle croissante n’est pas ce contrôle.
4. **Fragments inertes appariés en longueur et en exposition**, avec \(q_B=0\) connu, et politique de re-troncation fixée. La course parallèle garder/jeter ne suffit pas : les trajectoires de contenu y divergent immédiatement.

Un test minimalement réfutable serait (**HYPOTHÈSE** de protocole) :  
\(H_A\) : à \(q_B,\theta'\), re-troncation et taux d’essais fixés, conserver les brouillons ne change pas le risque d’extinction ;  
\(H_B\) : le conserver l’augmente.  
Une augmentation du risque falsifie \(H_A\) ; un intervalle excluant une augmentation minimale \(\delta\), fixée avant lecture, falsifie \(H_B\). Sans randomisation à exposition égale, les deux issues restent confondues.

## Sur la proposition C

### (a) Défauts de méthode

**1. La démonstration de « dilution quadratique ⇒ extinction » est incomplète.**  
La formule \(p_{\mathrm{bisoc}}(F,P)\) est une probabilité par événement, pas une loi dynamique complète. Si \(a(F,P)\) est le taux total d’événements, la production de fiches vraies dépend de
\[
a(F,P)\,p_{\mathrm{bisoc}}(F,P).
\]
À \(p=O(N^{-2})\), un taux constant, un taux proportionnel à \(N^2\) et un taux proportionnel à \(N^3\) donnent trois régimes différents. Le temps de doublement dépend également du taux total. Le rayon \(1/2\) et l’extinction pour tout \(q_2\) ne suivent donc pas de l’équation écrite : il manque la loi des tentatives, des durées de vie et des divisions.

L’assimilation des hybrides fertiles à l’auto-copie \(c>0\) est également trop rapide : une fusion mixte exige la présence de parasites ou de fiches fausses, alors que l’auto-copie du variant du papier peut concerner la fiche elle-même. Les processus absorbants ne sont pas les mêmes.

**2. \(c_{\mathrm{mes}}=2q_{vf}/q_{vv}\) n’est pas le paramètre \(c\).**  
Le \(c\) du modèle est un poids relatif de choix du propre modèle ; \(c_{\mathrm{mes}}\) est un ratio de probabilités de résultats, sans démonstration de correspondance. Le seuil \(0{,}05\) et la comparaison à une valeur obtenue à \(y=0{,}05\) sont donc sans portée, d’autant que C suppose ailleurs \(y\in[1{,}5;3]\). Les issues proposées ne falsifient pas les deux hypothèses : sélection et erreurs de juge peuvent simuler une hybridation fertile, tandis qu’un manque d’essais peut la masquer.

**3. L’estimateur \(\widehat\rho\) n’est pas le rayon spectral.**  
« Nombre moyen de fiches vraies filles par fiche vraie mère » est un premier moment agrégé. Il ne coïncide avec le rayon de Perron que sous une distribution de types appropriée, notamment celle du vecteur propre gauche. Conditionner aux lignées survivantes ajoute un biais de survie. Le signe de \(\widehat\rho-1\) peut donc ne pas être celui de \(\rho(K)-1\).

**4. Les seuils de grande taille sont appliqués à \(n=6\) sans contrôle d’extrapolation.**  
Les valeurs de \(\psi(y)\), la frontière de moitié du bonus et les exemples de bains ne fournissent pas, à elles seules, le noyau exact à \(n=6\), fécondité finie et re-troncation choisie. De même, participer à des fusions n’est pas nécessairement produire des copies complètes : le \(R\) mesuré par participation et le \(R\) du modèle ne sont identifiés que sous une loi de production et de retrait supplémentaire.

**5. Dans l’arène, une borne de levier devient une condition suffisante indue.**  
La condition sur \(\bar r\) utilisée par C correspond à un régime de tri partiel et de forte fécondité. Pour une règle arbitraire, \(\bar r\) borne le plafond mais ne garantit pas sa réalisation ; à fécondité finie, la persistance n’est pas déduite de la seule formule écrite. Des \(q_t,\theta_t\) adaptatifs au moniteur rendent également non stationnaires les paramètres que C traite comme constants.

**6. L’expérience sur (H2) n’a pas deux issues symétriquement informatives.**  
Une marge positive peut établir un certificat. Une marge négative après raffinement n’établit ni une tangence ni la fausseté de (H2) : elle peut seulement montrer l’échec de la famille de certificats. Le contrôle « déplacer \(\lambda_{\mathrm{up}}\) de \(+0{,}03\) doit rendre la marge négative » n’est pas une nécessité mathématique.

Enfin, exiger que des brouillons aléatoires reproduisent « exactement » la Fig. 6A à \(n=6\) est injustifié : les valeurs rapportées concernent d’autres tailles et hypothèses, et le texte aléatoire change aussi les lois de fusion et de jugement.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

- **Mesures \(q_{vv},q_{vf}\)** : avec la décomposition précédente, \(q_{vf}=0\) peut produire \(\widetilde q_{vf}>0\) si \(b_{vf}>0\). Le signe de l’hybridation peut donc être inversé par des fausses promotions différentielles. Si \(q_{vv}=0\), \(c_{\mathrm{mes}}\) est infini ou indéfini ; si aucune paire mixte n’est tentée, \(q_{vf}\) n’est pas estimable. Une vérité plantée « vrai conceptuel » n’implique pas non plus une même loi de fertilité entre mondes.
- **Taux de participation \(R\)** : si le retrait d’une fiche dépend de ses succès passés, sa durée de vie est une variable endogène. Le ratio fusions/temps observé subit une censure informative ; il n’est pas un estimateur sans biais du nombre de copies complètes par vie.
- **Décision d’extinction quadratique** : \(p_{\mathrm{bisoc}}\) et ses estimateurs ne suffisent pas. Sans estimation de \(a(F,P)\), de la loi des temps de cycle et de la partition, \(\rho\) n’est pas identifiable, quelle que soit la précision de \(\widehat q_2,\widehat q_1\).
- **Estimateur \(\widehat\rho\)** : si la production par mère varie avec \(F\) et que la distribution des mères n’est pas la distribution propre pertinente, la moyenne agrégée ne détermine pas le rayon spectral. Un historique court avec extinction rend également l’estimation conditionnelle aux survivants optimiste.
- **Levier dans l’arène** : si la loi des attaques au tour \(t+1\) dépend du tri observé jusqu’au tour \(t\), le \(\bar r\) estimé sur le passé n’est pas un paramètre prédictif de la loi future. Une borne nécessaire stationnaire ne devient pas une condition suffisante adaptative.
- **Certificat (H2)** : \(M_{\mathrm{box}}\le0\) est seulement un événement « non-certification par cette méthode ». Il ne constitue pas un estimateur de la vérité de (H2), ni un test de puissance connue contre une tangence.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Calibration du juge séparément pour chaque type de paire**, sur vérité plantée tenue à l’écart, avec estimation des fausses promotions \(b_{vv},b_{vf}\). Le contrôle tout-faux est nécessaire mais insuffisant : il ne mesure pas les erreurs différentielles sur paires mixtes.
2. **Manipulation du seul taux de tentatives**, à \(q_{vv},q_{vf}\), composition initiale et partition fixées. Sans elle, la prétendue extinction par dilution quadratique reste non testée.
3. **Matrices \(K\) synthétiques à spectre connu**, notamment des cas où moyenne par mère et rayon de Perron donnent des conclusions différentes. Sans ce contrôle, \(\widehat\rho\) ne peut servir de critère d’allumage.
4. **Noyau exact recalculé aux paramètres de l’expérience sur les brouillons**, accompagné de fragments inertes \(q_B=0\), de témoins d’archivage fictif et d’un contrôle sans re-troncation. La ressemblance visuelle avec une figure obtenue à d’autres paramètres n’est pas un contrôle positif.
5. **Tri fictif à quota identique dans l’arène**, puis attaquant gelé et attaquant adaptatif séparés. Sans tri fictif, l’effet du levier est confondu avec la réduction ou la modification du jeu d’entraînement.
6. **Cas certifiés positifs et négatifs pour le vérificateur (H2)**, indépendants des boîtes utilisées pour régler la discrétisation. Le déplacement arbitraire de \(\lambda_{\mathrm{up}}\) ne remplace pas ces cas.

Le test central de C devrait être reformulé ainsi (**HYPOTHÈSE**) :  
\(H_A\) : à lois de succès et de partition fixées, l’extinction est indépendante de \(a(F,P)\) ;  
\(H_B\) : elle en dépend.  
Une variation de persistance avec \(a(F,P)\) falsifie \(H_A\) ; une invariance bornée avec une marge d’effet pré-scellée falsifie \(H_B\). En l’état, ni la prédiction globale de non-allumage, ni la condition suffisante annoncée pour l’arène, ne sont mesurables comme des conséquences du papier.

FIN-DE-CELLULE