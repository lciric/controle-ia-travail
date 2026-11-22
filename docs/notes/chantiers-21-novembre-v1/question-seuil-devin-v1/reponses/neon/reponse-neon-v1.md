### 1. Option proposée et justification

Je propose une **option (d)** qui combine le contrôle familial d'admission de **(b)** et le budget de **(c)** — déjà jugé envisageable puisqu'il figure sur la table — avec deux améliorations protocolaires :

- **Seuil :** contrôle du taux d'erreur familial (*FWER*) à $0,05$ par admission via **Holm-Bonferroni** (premier seuil à $0,0125$, puis $0,05/3$, $0,05/2$, $0,05$ ; ou test max-$T$ conjoint par permutation si les épisodes sont partagés).
- **Budget :** **$8\,000$ épisodes par test** ($4\,000$ apprentissage, $4\,000$ épreuve).
- **Performances sous les mêmes hypothèses que le tableau :** fausses suspensions par admission **$\le 5\%$** ($4,9\%$ sous indépendance, mais bornées à $5\%$ **même sous dépendance** des tests) ; plus petite fuite détectée (MDE) d'environ **$0,066$** à pile ou face et **$0,15$** à $5\%$ d'audits.

**Pourquoi (d) domine (a), (b) et (c) :**
1. *Face à (c) (même budget) :* passer de $0,05$ à $0,0125$/Holm divise presque par quatre les fausses suspensions ($18,5\% \to 4,9\%$) pour un surcoût minime sur la MDE ($+11\%$, soit $0,066$ au lieu de $0,060$ à $p=0,5$). Ce gain est crucial : avec près d'un dispositif sain sur cinq suspendu sous (a) ou (c), les équipes finissent par traiter les échecs comme du bruit et relancer l'épreuve, ce qui sabote la sécurité.
2. *Face à (b) (même FWER) :* doubler le budget réduit la MDE de $29\%$ ($1/\sqrt{2}$) **et** double l'effectif d'apprentissage — avantage non comptabilisé dans le tableau, mais décisif à $5\%$ d'audits ($200$ épisodes audités pour entraîner les prédicteurs contre seulement $100$ sous (b)).
3. *Face à (a) :* (d) est strictement meilleur sur tous les critères. (Si le budget était strictement plafonné à $4\,000$ épisodes, je choisirais **(b)** plutôt que (a), le compromis $4\times$ moins de fausses alarmes contre $+11\%$ de MDE étant très favorable.)
4. *Holm plutôt que Bonferroni simple :* exactement la même probabilité de fausse suspension d'un dispositif sain, mais une puissance supérieure dès qu'une première fuite est réelle.

**Compléments protocolaires à intégrer à (d) :**
- Pour la décision d'audit, réaliser l'épreuve à **$p = 0,5$** chaque fois que les canaux auxiliaires redoutés ne dépendent pas de la fréquence d'audit : cela divise la MDE par $2,29$ (équivalent à **$5,3\times$ plus d'épisodes**) et multiplie par $10$ les exemples positifs d'entraînement. Si $p = 0,05$ doit être conservé (effets de congestion/file d'attente), réallouer une plus grande part du budget total vers les tests à classe rare plutôt que d'appliquer un budget uniforme.
- Utiliser une statistique insensible au déséquilibre (AUC, justesse équilibrée, log-perte — jamais la justesse brute) et accompagner tout non-rejet d'une borne supérieure de confiance sur l'avantage empirique du meilleur prédicteur.

---

### 2. Confiance

**0,70.**

Je suis nettement plus confiant ($\approx 0,85$) dans le fait qu'un contrôle FWER à $0,05$ par admission (Holm/Bonferroni) domine le seuil non corrigé de $0,05$ à budget égal. L'incertitude restante tient aux paramètres absents de l'énoncé : coût marginal d'un épisode (et d'un audit), coût réel d'une fausse suspension, et surtout possibilité que même $8\,000$ épisodes soient encore très insuffisants face à une menace critique.

---

### 3. Ce qui me ferait changer d'avis

- **Un coût :** si chaque épisode (ou audit en épreuve à $p=0,5$) est très onéreux et verrouille le plafond à $4\,000$ épisodes par test, je basculerais sur **(b)** (avec réallocation de budget entre tests équilibrés et rares si possible).
- **Une conséquence d'une fausse suspension :** si une suspension est quasi gratuite et déclenche un protocole de confirmation en deux étapes **pré-enregistré** (et non une ré-exécution ad hoc), un criblage initial à $\alpha = 0,05$ comme **(c)** devient défendable ; inversement, si toute suspension bloque durablement un déploiement critique, un FWER plus strict ($0,01$ ou $0,02$) s'imposerait.
- **Une taille de fuite jugée dangereuse :** si une fenêtre sans audit sur $1\%$ à $5\%$ des épisodes suffit à un agent opportuniste pour réussir une attaque catastrophique, **aucune** option (ni (c), ni (d)) ne protège suffisamment ; il faudrait un budget beaucoup plus élevé, une épreuve à $p = 0,5$, et surtout une isolation architecturale en amont du test.
- **Une propriété du test :** (i) une forte corrélation positive entre les quatre tests (réduisant la FWER réelle sous $0,05$, rendant un test de permutation conjoint nettement meilleur que Bonferroni) ; (ii) une très forte corrélation entre les $\sim 30$ prédicteurs ($M_{\text{eff}} \ll 30$), qui fait monter la pénalité relative de Bonferroni de $+11\%$ vers $+20$–$24\%$ ; (iii) une forte perte d'apprentissage sur la moitié d'entraînement, qui justifierait un découpage asymétrique (ex. $65/35$) plutôt que $50/50$.

---

### 4. Unité de contrôle de l'erreur

L'unité par défaut devrait être **l'admission** (FWER $\le 0,05$ sur les quatre tests) — ou **le secret par admission** ($k=2$, seuil $0,025$) si et seulement si les deux garanties peuvent être suspendues de manière strictement indépendante sur le plan opérationnel.

Ce que chaque unité engage :
- **Le test individuel :** maintient une puissance constante par test même si la batterie s'allonge, mais laisse la probabilité de fausse suspension d'une admission saine dériver avec le nombre de vérifications ($18,5\%$ à $20\%$ dès $k=4$). Cela crée une incitation perverse à limiter le nombre de cibles testées et banalise les rejets.
- **L'admission :** aligne le contrôle statistique sur **l'acte de décision** (autoriser un dispositif). Elle garantit un taux de fausse suspension $\le 5\%$ quelle que soit la dépendance entre tests, pour un surcoût de puissance modeste ($\sim +11\%$ sur la MDE). Elle engage à accepter qu'un dispositif sain ré-éprouvé souvent subisse à terme des fausses suspensions ponctuelles (taux récurrent par cycle, comme en contrôle qualité par lot).
- **Le dispositif sur toute sa vie :** engage à borner la probabilité de *n'avoir jamais* une fausse suspension sur une suite indéfinie de ré-épreuves, via un budget d'erreur cumulé ($\sum_t \alpha_t \le \alpha$). Avec un *$\alpha$-spending* décroissant ($\alpha_t \to 0$), la puissance s'effondre précisément lors des ré-épreuves tardives, alors que le système dérive ou évolue : c'est inadapté à la sûreté. En cas de surveillance **continue** en flux, il ne faut pas viser une FWER à vie fixe, mais un **temps moyen entre fausses alarmes (ARL)** ou des méthodes en ligne (*$\alpha$-investing*, *e-processes*).

---

### 5. Erreurs dans les chiffres ou le raisonnement, et antériorités

#### A. Vérification des chiffres

- **Fausses suspensions :** $1 - (1-0,05)^4 = 18,55\%$ et $1 - (1-0,0125)^4 = 4,91\%$ sont exacts **sous indépendance** (et à la discrétisation près des $p$-valeurs de permutation).
- **MDE :** les ordres de grandeur correspondent à l'approximation normale unilatérale d'un classifieur binaire *oracle* (au pire cas $q = 1/2$) avec correction de Bonferroni sur $M \approx 30$ prédicteurs :
  $$\delta \approx \frac{z_{1-\alpha/M} + z_{0,8}}{2\sqrt{n_{\text{épreuve}}\,p(1-p)}}.$$
  Pour $M=30$ ($z_a + z_{0,8} = 3,777$ ; $z_b + z_{0,8} = 4,183$), on retrouve à $p=0,5$ : **$0,0845$**, **$0,0935$** et **$0,0597$** (quasi conformes à $0,085$, $0,094$, $0,060$).
- **Deux erreurs/imprécisions chiffrées :**
  1. *Contradiction d'énoncé et facteur $1-p$ omis en colonne 6 :* l'énoncé suppose « bras équilibrés » pour tout le tableau alors que la colonne 6 traite $p = 0,05$. Avec la variance exacte $1/(4p(1-p)) = 1/0,19$ (facteur $2,294$), les MDE exactes à $p = 0,05$ sont **$0,194$**, **$0,215$** et **$0,137$** (soit **$0,14$**, pas $0,13$, pour (c)). Les chiffres $0,19 / 0,21 / 0,13$ proviennent vraisemblablement de l'approximation $\sqrt{0,25/0,05} = \sqrt{5} \approx 2,236$, qui néglige le terme $1/n_0$ (le facteur $1-p = 0,95$).
  2. *Ambiguïté budget / indépendance :* si les 4 tests sont indépendants, le budget par admission est **$4 \times 4\,000 = 16\,000$** (ou **$32\,000$**) épisodes. Si les épisodes sont partagés entre tests, l'indépendance supposée pour $18,5\%$ tombe : la FWER de (a)/(c) peut varier entre $5\%$ et $20\%$, alors que Bonferroni la borne toujours à $\le 5\%$.

#### B. Failles majeures du raisonnement

1. **Hypothèse implicite d'un prédicteur oracle (biais optimiste majeur) :** le calcul ne tient compte que du bruit d'évaluation sur $n_{\text{épreuve}}$, en supposant qu'un des $\sim 30$ prédicteurs appris atteint sans perte la frontière bayésienne réalisant toute la variation totale $\delta$. En pratique, sur $n_{\text{apprentissage}} = 2\,000$ épisodes avec $p = 0,05$, il n'y a que **$\sim 100$ épisodes audités** pour apprendre un canal auxiliaire potentiellement subtil : la fuite réellement détectable à puissance $0,8$ sera bien supérieure à $0,19$–$0,21$. (À l'inverse, l'approximation de Bonferroni sur les $\sim 30$ prédicteurs est légèrement *conservatrice* face au max-$T$ par permutation s'ils sont fortement corrélés.)
2. **Inadéquation sécuritaire de la variation totale et dépendance à la forme de la fuite :** la TV est une distance *additive*, pas une borne multiplicative sur le risque d'évasion. Même $\text{TV} = 0,06$ autorise un événement observable survenant sur $6\%$ des épisodes non audités et $0\%$ des audités : un agent patient peut attendre cette fenêtre et agir avec **risque d'audit nul**. De plus, la puissance ne dépend pas de la seule TV : contre une telle fenêtre pure, un oracle détecte $\delta \approx 0,07$ (et non $0,19$) à $p=0,05$, $\alpha=0,05$ ; à l'inverse, avec la justesse brute comme statistique à $p=0,05$, la puissance contre une fuite diffuse peut s'effondrer à zéro.
3. **Exactitude fragile de la permutation pour le détecteur interne :** pour la décision d'audit tirée au sort i.i.d., permuter les étiquettes est rigoureusement exact même si les épisodes sont corrélés (inférence par randomisation). En revanche, la **lecture d'un détecteur interne** dépend de la trajectoire et donc potentiellement de ce que l'agent observe : sans permutation conditionnelle/stratifiée sur le contexte (ni échangeabilité des épisodes), le test teste l'indépendance marginale plutôt qu'une fuite parasite, et son exactitude sous le nul n'est pas garantie. Par ailleurs, un détecteur déclenchant rarement souffrira du même problème de déséquilibre que l'audit à $5\%$.
4. **Piège de la ré-exécution et « *power approach* » :** un taux de $18,5\%$ de fausses suspensions encourage le *re-testing* informel (qui ruine la puissance), et qualifier un non-rejet par la seule MDE a priori reproduit les limites classiques de l'approche par puissance au lieu de bornes de confiance explicites.

#### C. Antériorités pertinentes *(toutes citées de mémoire)*

- **Unité de contrôle d'erreur et tests multiples :** Ryan (1959), *« Multiple comparisons in psychological research »* ; Holm (1979), *« A simple sequentially rejective multiple test procedure »* ; Rothman (1990), *« No adjustments are needed for multiple comparisons »* (contre-point pro-puissance) ; Westfall & Young (1993), *Resampling-Based Multiple Testing* (tests max-$T$ par permutation adaptés aux corrélations) ; Bender & Lange (2001), *« Adjusting for multiple testing—when and how? »*.
- **Contrôle séquentiel / durée de vie :** Page (1954), *« Continuous inspection schemes »* (ARL plutôt que FWER à vie) ; Foster & Stine (2008), *« $\alpha$-investing: a procedure for sequential control of expected false discoveries »* ; Ramdas, Grünwald, Vovk & Shafer (2023), *« Game-theoretic statistics and safe anytime-valid inference »*.
- **Tests par prédicteur adverse (découpage + permutation) et randomisation :** Friedman (2004), *« On Multivariate Goodness-of-Fit and Two-Sample Testing »* ; Lopez-Paz & Oquab (2017), *« Revisiting Classifier Two-Sample Tests »* ; Kim, Ramdas, Singh & Wasserman (2021), *« Classification accuracy as a proxy for two-sample testing »* ; Candès, Fan, Janson & Lv (2018), *« Panning for gold: 'model-X' knockoffs for high dimensional controlled variable selection »* (test de randomisation conditionnelle).
- **Non-rejet, approche par puissance et tests d'équivalence :** Schuirmann (1987), *« A comparison of the Two One-Sided Tests procedure and the Power Approach for assessing the equivalence of average bioavailability »* ; Hoenig & Heisey (2001), *« The abuse of power: the pervasive fallacy of power calculations for data analysis »*.
- **Épreuves de fuite par canaux auxiliaires et contrôle d'agents IA :** Goodwill, Jun, Jaffe & Rohatgi (2011), *« A testing methodology for side-channel resistance validation »* (TVLA) ; Jagielski, Ullman & Oprea (2020), *« Auditing Differentially Private Machine Learning: How Private is Private SGD? »* ; Greenblatt, Shlegeris, Sachan & Roger (2023/2024), *« AI Control: Improving Safety Despite Intentional Subversion »*.