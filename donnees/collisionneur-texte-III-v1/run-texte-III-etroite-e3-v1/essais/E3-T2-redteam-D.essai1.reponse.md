Les calculs fondés sur le fait 17 restent des calculs sur données **RAPPORTÉ** ; les seuils repris des conceptions sont illustratifs.

## Sur la proposition A

### (a) Défauts de méthode

- **Le duel 2 ne teste pas l’implication annoncée.** Une corrélation capture–réussite γ et un écart vues/tenues à l’écart sont deux résumés de la loi jointe ; ils ne bornent pas la queue d’échec parmi les familles non découvertes. À γ et écart identiques, deux copules peuvent produire des parts d’échec non découverte très différentes. Le duel mesure donc surtout la famille paramétrique choisie. De plus, ses hypothèses laissent une zone intermédiaire sans verdict, comme le duel 1 entre ses deux seuils de couverture.
- **Le duel 3 compare des grandeurs non commensurables.** Le biais relatif de Chao2 porte sur \(\hat N\), celui de « l’estimateur de couverture » porte tantôt sur \(\hat C\), tantôt semble-t-il sur \(S_{\mathrm{obs}}/\hat C\). Sans estimand commun, l’issue ne désigne pas un estimateur gagnant.
- **La substitution de \(n_{\mathrm{eff}}\) dans la borne à zéro échec est injustifiée.** Le facteur \(1+(n-1)\rho\) est une correction de variance de moyenne sous équicorrélation, pas une formule générale pour la probabilité de zéro échec. Celle-ci dépend de la loi jointe complète et des tailles de grappes, pas seulement de \(\rho\).
- **Le plan de simulation confond plusieurs difficultés.** Le facteur latent commun mélange hétérogénéité et dépendance, certes séparées ensuite par un terme de paire, mais la calibration des totaux à une taille hors de la grille peut faire varier l’effort de capture avec \(N\). Surtout, sous censure commune, noter les estimateurs contre le \(N\) total les fait échouer par construction : leur estimand identifiable est \(N_{\mathrm{accessible}}\).
- **La base à battre est mal définie.** Sans erreur d’appariement, \(S_{\mathrm{obs}}\le N\) et la borne unilatérale \([S_{\mathrm{obs}},+\infty)\) couvre avec probabilité un ; sa couverture n’est pas « nulle par construction ». Exiger seulement une couverture supérieure à celle du comptage brut rend donc le critère tantôt trivial, tantôt faux.

### (b) Lois sous lesquelles les mesures perdent leur puissance ou deviennent non jugeables

- **Chao2** : sa propriété de borne basse ne survit pas à une dépendance résiduelle arbitraire entre sources, après prise en compte de l’hétérogénéité. La phrase « sous dépendance positive, Chao2 reste une borne basse » est donc trop générale. Fusions et scissions à tort modifient en outre simultanément \(f_1,f_2,S_{\mathrm{obs}}\).
- **Modèles log-linéaires** : à déviance et marges fixées, une interaction d’ordre trois non nulle ou des lois latentes distinctes peuvent donner des \(N\) différents. Avec de petits doublets, le saturé a une variance instable ; un intervalle nominalement ajusté peut ne plus avoir de couverture interprétable.
- **Mesure d’universalité** : si des familles ont une probabilité de découverte nulle, ou si la classification d’échec a une probabilité de masquage non bornée, aucun \(n\) fini ne certifie la classe totale. Une corrélation de découverte seule ne détermine pas non plus la couverture sans la corrélation des échecs.
- **Arrêt séquentiel** : des lectures répétées de la borne sans dépense d’α effective ou sans martingale conditionnelle invalident le niveau annoncé.
- **Validation de Good–Turing** : \(f_1/n\) prédit une nouveauté pour une capture supplémentaire sous la même loi de capture, pas automatiquement la part de nouveautés d’une source extérieure indépendante mais autrement pondérée. Une forte nouveauté peut donc refléter un changement de loi plutôt qu’une censure commune ; zéro nouveauté ne prouve pas des scissions à tort.

### (c) Contrôles négatifs indispensables

1. **Contrôle d’estimand sous censure** : vérifier la couverture pour \(N_{\mathrm{accessible}}\), tout en constatant séparément l’impossibilité d’estimer la part censurée.
2. **Contrôle d’arrêt optional** : sous indépendance, à la frontière \(\pi=\varepsilon\), répéter les lectures selon la règle prévue ; le taux de certification doit rester au niveau nominal.
3. **Contrôle de transport extérieur** : une loi extérieure identique doit valider la calibration de la prédiction de nouveauté ; une loi repondérée à vérité connue doit révéler sa non-transportabilité, sans être comptée comme échec de l’estimateur interne.
4. Le contrôle de capture complète doit traiter explicitement \(f_2=0\) et les formules indéfinies ; observer \(f_1=0\) ne suffit pas à établir que la capture est complète.

## Sur la proposition B

### (a) Défauts de méthode

- **L’hypothèse a4 est erronée.** \(M_0\) autorise des probabilités propres aux sources ; \(M_h\) et Chao précisent justement une hétérogénéité entre familles. L’échangeabilité des familles ou des sources n’est donc pas la condition commune annoncée.
- **Le duel 1 mélange deux estimands.** Chao estime le nombre de familles accessibles ; il ne fournit ni une probabilité d’inclusion pour l’échec ni une correction automatique de la borne sur \(\varepsilon\). Une corrélation entre indicateurs de découverte ne suffit pas à calculer la couverture d’une borne portant sur les échecs.
- **Le duel 2 définit mal la validité de Chao.** Une borne inférieure peut être valide tout en étant fortement biaisée vers le bas. Réciproquement, un biais proche de zéro ne garantit pas \(P(L\le N)\). Le contrôle « Chao quasi non biaisé sous \(M_0\) » n’est pas une propriété générale, particulièrement avec trois occasions.
- **La règle d’arrêt par stagnation de largeur n’a pas de garantie de couverture.** Un plateau peut provenir de la censure ou de l’hétérogénéité. Poursuivre jusqu’au succès sans correction de lectures répétées peut également gonfler la fausse certification.
- **Le calcul sur les recaptures reste spéculatif.** Utiliser les totaux divisés par 37 comme probabilités de capture suppose implicitement qu’il n’existe aucune famille non observée. Et placer la plus grande recapture sur la paire la plus attendue tend ici à réduire l’écart à l’indépendance, non nécessairement à maximiser la déviance.
- **La sélection AIC/BIC puis l’inférence sur les mêmes sept cellules** omettent l’incertitude de sélection du modèle ; les intervalles peuvent devenir anticonservateurs.

### (b) Conditions de perte de puissance ou de non-jugement

- À **ρ et CV fixés**, les captures peuvent être indépendantes conditionnellement à une propension latente, ou comporter des interactions résiduelles de paire et d’ordre trois. Couvertures et biais ne sont alors pas déterminés.
- La formule de Chao employée mélange une version sans facteur de trois occasions et une version corrigée : tant que l’estimateur et sa variance ne sont pas fixés, le résultat chiffré et sa validation extérieure ne sont pas reproductibles. Avec \(f_2=0\), plusieurs formules deviennent indéfinies.
- La validation extérieure fondée sur \((\hat N-37)/\hat N\) traite une **borne inférieure** comme une estimation ponctuelle. Sous tirage uniforme, elle autorise au plus une prédiction unilatérale ; une population plus grande reste compatible avec Chao.
- Un test de Fisher sur un écart de performance ne falsifie pas le quantile retenu : deux lois peuvent différer significativement tout en satisfaisant toutes deux \(\pi\le\varepsilon\).
- Des intervalles disjoints entre la règle simulée et la borne extérieure ne constituent pas un test calibré si les estimands, lois de capture ou dépendances diffèrent.

### (c) Contrôles négatifs indispensables

1. **Factoriser trois mondes nuls distincts** : dépendance de découverte seule, dépendance des échecs seule, sélection capture–échec seule. Le contrôle \(\rho=0\) actuel ne les distingue pas.
2. **Contrôle de borne, non d’absence de biais** : dans des mondes où \(N\) dépasse largement la borne de Chao, la procédure ne doit jamais déclarer cette borne falsifiée pour ce seul motif.
3. **Contrôle de la validation du quantile** : deux échantillons de lois différentes mais tous deux conformes à \(\pi\le\varepsilon\) ne doivent pas être comptés comme réfutation de l’universalité.
4. **Contrôle de lectures répétées** pour la règle séquentielle, avec taux de fausse certification mesuré à la frontière.

## Sur la proposition C

### (a) Défauts de méthode

- **Deux statuts sont à corriger.** La déviance 12,9 demeure **RAPPORTÉ** au fait 17 ; le fait 18 ne la recalcule pas. L’absence d’erreurs d’appariement est une **HYPOTHÈSE**, non une observation : seuls les comptes transmis sont RAPPORTÉ.
- **Le duel 1 porte sur un objet ambigu.** Un modèle à six paramètres n’est pas saturé sur sept cellules ; il comporte deux interactions de paire et un degré de liberté. Le bloc 3 distingue correctement ce cas du saturé à sept paramètres, mais le duel ne le fait pas.
- **Le contrôle négatif de l’instrument 2 est inversé.** Dans le bloc 1, \(\theta_i\le\tau\) est une réussite. Le monde \(\theta_i=\tau\) pour toutes les familles ne contient donc aucune famille défaillante au sens \(\theta_i>\tau\), contrairement à \(\pi=1\). Exiger alors une certification \(\le\alpha\) rejette par construction une défense conforme à la définition.
- **La correction de Horvitz–Thompson n’est pas établie.** Une visibilité \(w_i\) n’est pas une probabilité d’inclusion. Sous tirage séquentiel sans remise à probabilités inégales, les inclusions dépendent de l’ordre et des autres poids ; elles ne se déduisent pas directement d’un \(\hat N\) de capture–recapture. La formule de normalisation écrite doit aussi être reprise.
- **La déviance seule ne calibre pas un monde.** Une même déviance peut provenir d’hétérogénéité latente ou d’interactions de paire. Prétendre simuler « la dépendance reproduisant 12,9 » ne fixe donc pas la loi testée. La multiplication du nombre de familles par un VIF hérite enfin du même problème que chez A : elle ne découle pas d’une probabilité de zéro échec.

### (b) Conditions de perte de puissance ou de non-jugement

- **Chao et le modèle à effet latent** : la signature « beaucoup de singletons et de triplets » ne distingue pas identifiablement hétérogénéité et dépendance commune avec sept cellules. Sous interactions résiduelles, la garantie de borne inférieure de Chao doit être démontrée, non présumée.
- **Saturé** : l’hétérogénéité ne fixe pas à elle seule le signe et la taille de \(u_{123}\). Le sens « explosion vers le haut » n’est donc pas universel.
- **Population ouverte** : elle n’implique pas nécessairement \(N=\infty\) ; une taille datée peut rester finie. Inversement, Good–Turing ne conserve son interprétation prospective que sous une loi de capture suffisamment stable.
- **Validation extérieure** : Fisher teste l’égalité, pas directement la marge de non-infériorité déclarée. Surtout, \(K_{\mathrm{nouv}}\ge20\) reste compatible avec la borne \(N\ge\hat N_{\mathrm{Chao}}\) : cela réfute éventuellement l’usage de 55,3 comme valeur ponctuelle, pas la borne inférieure.
- **Petersen extérieur** : sous l’hétérogénéité précisément envisagée, ses conditions d’homogénéité et de fermeture peuvent échouer ; le seuil dérivé de \(\hat N_{\mathrm{ext}}\) devient alors non jugeable. Les prédictions Good–Turing et uniforme/Chao supposent par ailleurs deux lois extérieures différentes et ne doivent pas être appliquées au même monde sans le déclarer.

### (c) Contrôles négatifs indispensables

1. **Réparer le contrôle frontière** : distinguer \(\theta_i=\tau\), où la définition déclare une réussite, d’un monde réellement non universel \(\pi>\varepsilon\).
2. **Contrôle à déviance constante** : générer une loi latente et une loi à interactions résiduelles produisant la même déviance ; si les conclusions changent, le duel initial est non identifiable.
3. **Contrôle de compatibilité d’une borne inférieure** : avec \(N\) connu et supérieur à la borne de Chao, la validation extérieure ne doit pas conclure à sa falsification.
4. **Contrôle de Petersen** : sous hétérogénéité à vérité connue, mesurer son biais avant d’utiliser son seuil comme arbitre ; sous population ouverte non stationnaire, vérifier séparément que la couverture prospective n’est plus garantie.

FIN-DE-CELLULE