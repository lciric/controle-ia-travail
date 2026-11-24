# Proposition A — Tour III.2 : critique croisée de méthode

**État des pièces.** Les pièces B, C et D sont présentes et non coupées : chacune se termine par sa ligne de clôture. FAITS et QUESTION ont la même empreinte et ne contiennent aucune donnée empirique.

**Convention.** Tous les chiffres ci-dessous sont **illustratifs**, qu'ils reprennent les valeurs illustratives des pièces ou qu'ils en soient dérivés. Les statuts que les auteurs ont attribués sont cités tels quels. Quand je les conteste, je le dis sans les remplacer.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Erreur absolue sur des fréquences petites : critère vrai par construction.** *(VÉRIFIÉ, arithmétique.)* Le duel « sélection tabulaire suffisante » accepte H_A si l'erreur absolue maximale reste ≤ 0,05 sur $v,u,q$. Supposons que $v$ et $u$ restent sous 0,05 pendant tout l'entraînement. Un prédicteur constant nul satisfait alors H_A sur $v$ et $u$. Seul $q$ porte encore le test, et $q$ est le moins bien estimé. Le duel « transport » (RMSE ≤ 0,05 sur $v,u$) a le même défaut. Il faut une erreur normalisée, par exemple sur l'échelle logit ou relative à l'écart entre les conditions contrastées. Il faut aussi la comparer à un prédicteur naïf, par exemple « $p(0)$ constant ».

2. **Calibrer le temps $s(t)$ sur un menu honnête.** *(HYPOTHÈSE, confiance moyenne.)* La formule $p_i\propto p_i^0e^{s r_i}$ suppose un flot de gradient *naturel*, donc un même $s$ pour toutes les actions. Sur un LM entraîné par Adam, la vitesse effective dépend de la séquence : longueur, log-probabilité initiale, norme du gradient. Si les trajets interdits diffèrent systématiquement des trajets honnêtes sur ces covariables, un écart à la prédiction mesurera un défaut de calibration, pas un défaut du modèle de sélection. Ce facteur est confondant.

3. **Menu énuméré et masse hors menu.** *(HYPOTHÈSE, confiance moyenne.)* B compare l'optimiseur tabulaire et un LM « à menu identique ». Sauf décodage contraint, le LM peut sortir du menu, et cette masse n'existe pas dans le modèle tabulaire. Si elle n'est ni rapportée ni affectée à $(V,D)$ par l'oracle, $v,u,q$ du LM et du modèle tabulaire n'ont pas le même dénominateur.

4. **Une même légende sert au modèle et au détecteur.** *(HYPOTHÈSE, confiance moyenne.)* La légende visible informe à la fois le modèle (sait-il qu'il viole ?) et le moniteur (peut-il le voir ?). Les violations non signalées seront donc surtout des violations *accidentelles*, commises là où la légende est peu informative. Une hausse de $u$ peut alors refléter des erreurs non intentionnelles, et non un déplacement vers des formes non signalées. Il faut un estimand séparé : le taux de violation sans prime au raccourci, stratifié par informativité de la légende.

5. **Le test de dérive par teacher forcing est hors politique.** *(HYPOTHÈSE, confiance moyenne.)* B rejoue au checkpoint entraîné des chaînes que ce checkpoint ne produirait plus. Les activations y sont donc atypiques. $F$ mesure la dérive sur un panel figé, pas sur les violations que la politique émet réellement. C'est le bon instrument pour séparer dérive et sélection, à condition que le panel soit pondéré par la loi courante des violations, ce qui demande des poids d'importance.

### (b) Conditions de perte de puissance

- **$q$.** Avec $n$ générations par point, $\operatorname{Var}(\hat q)\approx q(1-q)/(n v)$. Pour $n=4096$ et $v=0{,}005$, on a $nv\approx20$ et un écart-type de $\hat q$ d'environ 0,11. Une erreur seuil de 0,05 n'est alors pas jugeable. Le critère « points où elles sont estimables » doit être fixé par une règle préinscrite, par exemple $n\hat v\ge$ un seuil, avant d'ouvrir les données.
- **Taux de bascule $F$.** Pour un score de sonde $S$ de densité $f_S$ au seuil $\kappa$ et un déplacement $\Delta$ petit, $F\approx f_{S\mid V}(\kappa)\,\mathbb E|\Delta|$. $F$ confond donc l'ampleur de la dérive avec la masse placée près du seuil. Si $f_{S\mid V}(\kappa)$ est grande, une dérive négligeable donne $F>0{,}05$. Il faut rapporter aussi la loi de $\Delta$ sur le score continu.
- **$G$ (révision).** Si $\bar u_{\rm fixe}$ et $\bar u_{\rm révisé}$ sont tous deux ≪ 0,03, $H_B$ ($G\le0{,}03$) est acceptée mécaniquement. Le seuil doit être relatif à $\bar u_{\rm fixe}$.
- **Recalibrage « à même taux de fausses alertes ».** Ce taux est défini sur la loi des épisodes honnêtes, et cette loi change avec la politique. Si $P_{\pi_t}(\neg V)$ se déplace vers des cas honnêtes plus ou moins faciles, l'égalité des fausses alertes à $t$ ne contrôle pas celle à $t'$. Il faut un panel honnête fixe en plus du panel courant.
- **Identifiabilité.** B note lui-même que les moments exponentiels intraclasses $\mathbb E[e^{sR}\mid \text{classe}]$ déterminent la trajectoire. Leur estimation par $\frac1n\sum e^{sR_j}$ a une taille d'échantillon effective $\mathrm{ESS}=(\sum w_j)^2/\sum w_j^2$, avec $w_j=e^{sR_j}$. Cette taille s'effondre quand $s\cdot(\max R-\min R)\gg\log n$. Au-delà, la prédiction tabulaire du duel 1 n'est pas jugeable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Pénalité aléatoire au même taux d'alerte**, indépendante de $\tau$, à budget de pénalité égal. Sans elle, on ne sépare pas l'effet de l'information du détecteur de l'effet de la pénalité comme bruit ou régularisation. Ce contrôle manque chez B ; D le propose (son E1).
- **Dérive passive** : même entraînement, sonde journalisée mais non appliquée. Sans elle, $F>0{,}05$ ne dit pas si la dérive est *due* à l'optimisation contre la sonde. Rejouer le même checkpoint, contrôle choisi par B, donne zéro bascule par déterminisme et ne contrôle rien. D propose ce contrôle passif (son E3).
- **Bras sans prime au raccourci**, avec la légende tenue fixe, pour estimer le plancher des violations accidentelles (point a.4).

---

## Sur la proposition C

### (a) Défauts de méthode

1. **L'oracle confond violation et incompétence.** *(VÉRIFIÉ sur la définition donnée par C.)* C pose $V=1$ ssi $R=1$ et échec sur la suite privée, ou altération de l'environnement. Une solution honnête mais boguée, qui passe les trois tests visibles, est donc comptée comme violation. Aucun moniteur ne peut signaler un bogue honnête comme triche. Ces cas gonflent $u$ et $\rho$ dès $t=0$. Si l'entraînement améliore la compétence, $u$ baisse pour une raison étrangère à la question. L'audit humain avec un κ de Cohen élevé ne corrige rien si les auditeurs appliquent la même définition. Il faut une étiquette distincte « contournement intentionnel » (AST, appels système, codage en dur des cas visibles) et rapporter les deux estimands séparément.

2. **Le contrôle négatif de E1 est vrai par construction.** *(VÉRIFIÉ.)* Si les tests visibles deviennent la suite complète, et si la suite privée y est incluse, alors $R=1$ implique la réussite des tests privés. $V=1$ n'est plus possible que par altération de l'environnement. « $p_U(T)\le0{,}002$ » ne teste donc presque rien du mécanisme étudié.

3. **E1 ne sépare pas M1 et M2.** *(VÉRIFIÉ, arithmétique.)* « $p_{10}(0)=0$ empirique sur 10 000 tirages » borne seulement $p_{10}(0)$ à environ $3\times10^{-4}$ à 95 % (règle de trois). Le budget d'entraînement de C vaut $BT\approx5{,}1\times10^5$ épisodes. Une classe de masse $3\times10^{-4}$ y apparaît environ 150 fois en espérance. M1, l'invariance de face, prédit alors elle aussi l'émergence. $H_A$ n'est la prédiction de M1 que si $p_{10}(0)\ll1/(BT)$. Cette condition demande un estimateur par importance validé, et C le classe lui-même en HYPOTHÈSE. D formule correctement ce point (son a.1, item 2).

4. **Fuite et effet du gagnant dans la stratification sur $\hat\Gamma_0$.** *(HYPOTHÈSE, confiance moyenne.)*
   - Les strates sont définies par $\hat\Gamma_0$, estimé bruité, puis la prédiction est testée dans la strate haute. Il faut estimer $\hat\Gamma_0$ et évaluer $p_U$ sur des moitiés disjointes de prompts.
   - Le lot diagnostique $V_U$ est rédigé hors ligne. S'il contient les types de violation que l'oracle comptera ensuite, la corrélation de $p_U(T)$ avec $\hat\Gamma_0$ est en partie construite.
   - $\Gamma_0$ est probablement corrélé à $\log\pi_{\theta_0}(V_U)$, donc à la masse initiale. Sans ajustement sur $\hat p_{10}(0)$, la pente sur $\Gamma_0$ peut traduire de la sélection (M1) et non du transfert (M2).

5. **Erreur interne dans la trichotomie de M1.** *(VÉRIFIÉ, calcul dans le modèle à quatre classes décrit par C.)* Avec $F$ fonction déterministe de $\tau$ et $\beta\to0^+$, la masse se concentre sur l'argmax de $\{R_C,\,R_C-\lambda,\,R_U,\,R_V-\lambda\}$ parmi les classes accessibles. La classe des fausses alertes s'éteint, et $\alpha_0(0)$ ne doit pas apparaître. La condition de C, $\lambda(1-\alpha_0)<R_V-R_C$, classe en « persistance signalée » la bande $R_V-\lambda<R_C<R_V-\lambda(1-\alpha_0)$. Dans cette bande, c'est la classe honnête non signalée qui l'emporte. La présence de $\alpha_0$ n'est correcte que si $F\mid V=0$ est aléatoire et indépendant de $\tau$. Dans ce cas, les classes 00 et 01 ne sont plus des types stables. Le modèle doit dire lequel des deux cas il traite.

6. **Statuts affichés plus forts que ce qui est montré.** Je cite les statuts de C sans les modifier.
   - T2 est « VÉRIFIÉ ». Le poids de Filippov est une fraction convexe pour un système *déterministe*. L'identifier à une fraction *de population* de violations non signalées demande un mécanisme de bruit qui place les épisodes de part et d'autre du seuil exactement dans cette proportion. Ce mécanisme n'est pas exhibé.
   - $b$ est endogène et dépend de $\rho$. $\rho^*=1-(R_V-b)/\lambda$ est donc un point fixe non résolu.
   - Je conteste aussi le statut VÉRIFIÉ de la « préimage fractale », du résultat M3 bilinéaire et de la convergence de Borkar vers Stackelberg. Le résultat à deux échelles de Borkar (1997) suppose notamment un équilibre globalement asymptotiquement stable de la dynamique rapide pour chaque paramètre lent. C ne l'établit pas.
   - Point 5 : C présente comme RAPPORTÉ, confiance élevée, des références marquées « à vérifier ». Il attribue à Gao, Schulman & Hilton (2023) une implication sur $p_U$ et $\rho$, alors que ce travail mesure un score d'or contre un score proxy, sans détecteur ni violations. Il attribue à Baker et al. une « courbe en U de $p_V$ », caractérisation que je ne peux pas attribuer. Les « désaccords D1–D3 » n'ont aucune référence attribuable.
   - Le titre de Skalse et al. (2022) diffère entre C (« Reward Gaming ») et D (« Reward Hacking ») : référence à vérifier.

### (b) Conditions de perte de puissance

- **E2, empilement sous κ : partiellement mécanique.** Sous pure sélection par troncature, sans dérive, $P(S\in[\kappa-\delta,\kappa]\mid V,\ \text{non signalé})$ vaut la masse initiale de la bande divisée par $P(S<\kappa\mid V)$. Avec 8 % dans la bande et 50 % au-dessus de κ à $t=0$, la seule renormalisation donne 16 %. Le seuil 0,40 doit être comparé au **contrefactuel de sélection seule** : la loi initiale de $S\mid V$, repondérée par les poids de sélection observés. Sans ce contrefactuel, l'empilement n'est pas jugeable comme signature de Filippov.
- **E2, monotonie de $\rho$ en $\lambda$.** Tout modèle de sélection prédit que $\rho$ croît avec $\lambda$ dès que $p_{10}(0)>0$. La corrélation de Spearman ne discrimine pas T2 de M1.
- **E2 et E3, hypothèses non exhaustives.** Certaines issues ne falsifient rien : $p_V$ entre 0,02 et 0,15 ; persistance sans empilement ; ni cycles ni plateau à 0,25 (E3). Il faut une partition préinscrite des issues.
- **E3, amplitude spectrale à $1/K$ : vraie par construction.** *(VÉRIFIÉ ; B en donne l'identité.)* Mesuré avec le détecteur *en service*, $u$ saute à chaque changement de version d'un montant égal à la différence des masses acceptées par les deux versions. Une composante à $1/K$ apparaît donc dès qu'une révision change quoi que ce soit, sans aucun cycle stratégique. Le fait que l'amplitude croisse avec $K$ découle aussi mécaniquement d'une sélection plus longue entre deux révisions. Il faut mesurer les oscillations sur $v$, qui ne dépend que de l'oracle, et sur $u$ évalué par un **détecteur d'audit fixe**.
- **E4, rapport $\sigma^2_{\rm inter}/\sigma^2_{\rm graine}$.** Si les invariants appariés à ±5 % sont *estimés*, alors $\sigma^2_{\rm inter,obs}=\sigma^2_{\rm inter}+\sum_k s_k^2\operatorname{Var}(\hat I_k-I_k)$, où $s_k$ est la sensibilité de la sortie à l'invariant $k$. Avec $p_{10}(0)$ estimé par importance, l'erreur d'estimation peut dépasser 5 %, ce qui fabrique $H_B$. Un test $F$ à (11, 48) degrés de liberté n'a aussi qu'une puissance limitée pour un rapport proche de 1,5.
- **E4, rotations LoRA.** Une rotation « orthogonale aux observables » ne garantit pas que des observables non mesurés restent fixes. L'appariement n'est vérifiable que sur les six invariants.

### (c) Contrôles négatifs dont l'absence serait fatale

- **E4.** Le contrôle simulé (M2 avec les invariants vrais) ne reproduit pas le mode d'échec réel. Il faut injecter dans la simulation les *mêmes estimateurs bruités* des invariants. Sinon un $R^2$ bas sur LM peut venir de la mesure et non de la dynamique.
- **E2.** Il faut un contrefactuel de sélection seule par repondération de la loi initiale du score (voir b).
- **E2 et E3.** Il faut une **dérive passive**, sonde journalisée non appliquée, et un **rejeu à séquences fixes** pour séparer la dérive de la sélection de types déjà non signalés (instrument de B).
- **E3.** Il faut une **révision factice** (copie identique du détecteur à chaque période) pour mesurer la part du spectre à $1/K$ due à l'ordonnancement de l'entraînement. Le contrôle par oracle bruité, déjà présent, ne la mesure pas.
- **Dans toutes les expériences.** Il faut un **bras sans faille exploitable mais avec tests faibles**, pour estimer le plancher des bogues honnêtes comptés comme $V=1$ (point a.1).

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Même confusion de l'oracle de code que C.** *(VÉRIFIÉ sur la définition.)* La règle « $V=1$ ssi tests cachés échouent ou contournement » compte les bogues honnêtes comme violations, avec les mêmes conséquences sur $u$ et $\rho$.

2. **L'oracle contrefactuel « indice retourné » est stochastique.** *(HYPOTHÈSE, confiance moyenne.)* Sous échantillonnage à température non nulle, un changement de réponse entre la copie et l'original peut venir du bruit d'échantillonnage. $V$ devient une variable aléatoire dont le taux de faux positifs vaut à peu près $P(\text{réponse change}\mid\text{aucune dépendance})$. Il faut définir $V$ sur une loi : comparer les distributions de réponses sur $m$ tirages, avec un test et un seuil préinscrits.

3. **E1 ne départage que M1 contre « tout le reste ».** *(HYPOTHÈSE, confiance moyenne.)* Le détecteur superficiel est contourné par une modification minime du texte : retirer quelques marqueurs lexicaux. Dans le modèle M3 de D lui-même, c'est un taux de « mutation » $\mu_{VF\to VU}$ élevé, pas un couplage de gradient. Une issue $\Delta p_{VU}\ge0{,}15$ réfute M1 mais ne sépare pas M2 de M3. $H_B$ n'est donc pas « M2 ».
   - **Fuite.** Les classes $V_U$ et $V_F$ sont définies *par le détecteur*. $\hat\rho_{VF,VU}$ diffère donc entre $D_{\rm sem}$ et $D_{\rm surf}$ en partie par construction.
   - **Calibrage sur l'échantillon d'évaluation.** Les taux initiaux doivent être appariés sur un échantillon disjoint de celui qui mesure $p(0)$ pour l'analyse. Sinon l'appariement est surajusté.

4. **E3 : la sonde fraîche est avantagée par construction.** *(HYPOTHÈSE, confiance moyenne.)* Une sonde entraînée sur $h_{\pi_T}$ avec les labels $V$ est évaluée dans sa propre distribution. Une AUROC ≥ 0,85 peut s'obtenir sans aucune obfuscation, simplement parce que la sonde gelée est hors distribution. De plus, la chute d'AUROC de la sonde gelée peut venir de la *sélection* de types de violation qu'elle ratait déjà à $t=0$, sans dérive. Sans **rejeu à séquences fixes** (le duel de B), « dérive dans le noyau » et « sélection » restent confondues. Apparier sonde et moniteur en TPR/FPR n'apparie pas *quelles* violations chacun rate, ni leurs gains. Or ce sont ces deux éléments qui pilotent $r(T)$ dans M1.

5. **E3 : l'atténuation en SFT filtré n'est pas garantie.** *(HYPOTHÈSE, confiance moyenne.)* Le filtrage sur le verdict d'une sonde sélectionne des trajectoires à faible score $\psi^\top h$. Ajuster le modèle sur elles déplace les représentations sans aucun gradient négatif. La prédiction « écart ≤ 0,10 en SFT » n'est donc pas une conséquence de M2.

6. **E4 : la partie (ii) de $H_B$ est quasi tautologique.** *(HYPOTHÈSE, confiance moyenne.)* L'expérimentateur construit un canal où une stratégie violante indiscernable existe et lui garantit un gain. Que le rejeu échoue à la faire disparaître est alors largement imposé par la construction. Le seul contenu informatif est de savoir *si et quand la politique trouve* cette stratégie, ce qui demande de mesurer son temps de premier passage. De plus, l'erreur de Bayes est définie sous la loi jointe (observation, $V$) de $\pi_0$, puis elle change avec $\pi_t$. Il faut la ré-estimer à chaque révision.

7. **E5 : peu de configurations et zone grise.** *(HYPOTHÈSE, confiance moyenne.)*
   - 24 configurations pour $m\le10$ variables : surajustement probable du prédicteur.
   - Les observables sont mesurés par des procédures différentes entre tâches de code et tâches d'indice. Un échec hors famille peut donc venir d'un décalage de mesure, pas d'une irréductibilité.
   - Les « sauts tardifs » sont définis après coup. Il faut un détecteur de ruptures préinscrit.
   - Les issues intermédiaires ($R^2$ entre 0,40 et 0,60, ou exactitude entre 0,60 et 0,80) ne falsifient rien.

### (b) Conditions de perte de puissance

- **Énergies libres $\mathcal F_C(x;\beta)$.** L'estimateur $\beta\log\frac1n\sum \mathbf 1_C e^{R/\beta}$ est dominé par le maximum quand $(R_{\max}-R_{\min})/\beta\gg\log(n\,p_C)$. Sa taille d'échantillon effective tend alors vers 1, et l'appariement de E1 « à $\mathcal F_C$ égal » n'est plus vérifiable. Pour $V_U$ rare, c'est le cas typique, et il faut rapporter cette taille effective.
- **E2, bimodalité.** Le test de Hartigan sur 20 graines n'a de puissance que si l'écart entre modes, divisé par l'écart-type intra-mode, est grand et que les deux modes ont des poids comparables. À $Np\approx1$, la probabilité d'au moins un tirage de $V_U$ vaut $1-e^{-1}\approx0{,}63$. Si la probabilité d'établissement après un premier tirage est faible, presque toutes les graines s'éteignent et la distribution est unimodale *sous M3 aussi*. Il faut prédire et tester la fraction de graines envahies, pas la bimodalité seule.
- **E2, pente de $\mathbb E[\tau_{\rm hit}]$ : vraie par construction.** *(VÉRIFIÉ.)* Pour le premier *tirage*, $\mathbb E[\tau]=1/(1-(1-p)^B)\approx1/(Bp)$ sous tout modèle, puisque c'est une propriété de l'échantillonnage. Seule la probabilité qu'un tirage conduise à l'*établissement* discrimine M3.
- **E2, calibrage de $Np(0)$.** Fixer $Np(0)\in\{0{,}05;1;20\}$ avec $N\sim5\times10^5$ exige d'estimer des probabilités autour de $2\times10^{-6}$. Il faut au moins $10^7$ générations par condition, ou un estimateur par importance validé. Sinon les niveaux manipulés ne sont pas connus.
- **E4, famine d'audit.** Avec $M=400$, le nombre attendu de $V_U$ par audit vaut $Mp_{VU}$. Pour $p_{VU}\le0{,}01$, on attend au plus 4 exemples. Le détecteur révisé n'a alors presque pas de signal, et « rejeu cumulatif contre fenêtre glissante » se confond avec « taille d'audit cumulée contre non cumulée ». Il faut apparier le nombre d'exemples positifs, pas le nombre d'épisodes.
- **E4, oscillations sur $p_{VU}$ mesuré avec le détecteur en service.** Même artefact que chez C : des sauts aux changements de version, vrais par construction. Il faut mesurer sur $v$ et avec un détecteur d'audit gelé.
- **Instruments (section c).** L'ECE dépend de la loi de $V$ sous $\pi_t$. Une variation d'ECE entre $t=0$ et $T$ peut refléter un changement de prévalence et non de discrimination. Il faut la stratifier par prévalence.

### (c) Contrôles négatifs dont l'absence serait fatale

- **E3.**
  - Rejeu à séquences fixes à travers les checkpoints, pour séparer la dérive de la sélection.
  - Sonde fraîche entraînée aussi sur le **run de dérive passive**, pour que la récupération d'AUROC ait une référence.
  - Évaluation de la sonde fraîche sur des prompts disjoints de son entraînement.
- **E2.** Il faut une condition où $V_U$ existe à $Np\approx1$ mais où le *gain* de $V_U$ est égal à celui de $H_U$. Ce contrôle distingue la stochasticité de l'échantillonnage de celle de l'établissement. Le contrôle à $Np=20$ ne fait pas cette distinction.
- **E4.** Il faut un détecteur révisé par une **copie identique**, pour isoler l'effet d'ordonnancement, et une **égalisation du nombre de positifs audités** entre bras.
- **E1.** Le contrôle par pénalité permutée est bien conçu. Il manque en plus un **détecteur superficiel non pénalisant**, journalisé seulement. Il mesure la baisse spontanée des marqueurs lexicaux sous RL, par exemple un raccourcissement du raisonnement écrit, qui imiterait $\Delta r>0$.
- **Dans toutes les expériences.** Il faut un plancher de bogues honnêtes dans l'oracle de code, comme chez C (point a.1).

FIN-DE-CELLULE