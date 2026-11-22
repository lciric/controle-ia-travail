### 1. Choix et justification

Je rejette (a), (b) et (c) telles quelles et propose une **option (d) : contrôle par admission pondéré, budget asymétrique et statistiques studentisées** (si le choix était strictement restreint aux trois options, je retiendrais **(b)** uniquement lorsque toutes les cibles sont équilibrées, et aucune à 5 % d'audit sans refonte).

Pourquoi (a), (b) et (c) échouent :
- **(a) et (c)** suspendent à tort **18,5 %** des dispositifs sains. En pratique, près d'un refus sur cinq sans défaut réel pousse les équipes à relancer l'épreuve « jusqu'à ce qu'elle passe », ce qui dégrade silencieusement la sécurité (voir § 5).
- **(a) et (b)** sous-alimentent gravement le régime à 5 % d'audit : sur 4 000 épisodes, chaque moitié (apprentissage et épreuve) ne contient en moyenne que **100 épisodes audités**. Une plus petite fuite détectable (MDE) de **0,19 à 0,21** laisse passer des fuites capables d'annuler la garantie d'audit.
- **(c)** double uniformément le budget sans corriger le taux de fausses suspensions ni le déséquilibre de variance de facteur $\frac{0,25}{0,05 \times 0,95} \approx 5,26$ entre une cible équilibrée ($p=0,5$) et une cible rare ($p=0,05$).

**Option (d) proposée** (à budget total d'épisodes inférieur ou égal à (c)) :
1. **Seuil contrôlé par admission ($\text{FWER} \le 0,05$) mais pondéré** (procédure de Holm pondérée, ou permutation conjointe `maxT` si les épisodes sont partagés) : par exemple $\alpha = 0,005$ pour deux tests équilibrés et $\alpha = 0,02$ pour deux tests à 5 % (somme $= 0,05$, soit $\le 5\,\%$ de fausses suspensions).
2. **Budget alloué selon $[p(1-p)]^{-1}$** : **4 000 épisodes** par test équilibré et **12 000 épisodes** par test à 5 % (32 000 au total si les essais sont disjoints comme en (c), ou **12 000 épisodes partagés** si les deux secrets sont enregistrés sur les mêmes trajectoires). Selon le modèle de calcul du tableau, on obtient $\text{MDE}_{50\%} \approx \mathbf{0,10}$ et $\text{MDE}_{5\%} \approx \mathbf{0,12}$ (meilleur que (c), pour un FWER ramené de 18,5 % à $\le 5\,\%$, avec 300 exemples positifs d'apprentissage au lieu de 100).
3. **Banc auxiliaire à 50 %** : si le tirage d'audit est sans mémoire d'un épisode à l'autre, éprouver aussi la branche logicielle à $p=0,5$ sur 4 000 épisodes abaisse la MDE sur ce canal à $\approx 0,09$.
4. **Studentisation et règle de ré-essai** : standardiser chacune des 30 statistiques par son écart-type empirique avant de prendre le maximum, et interdire toute nouvelle épreuve sans correctif identifié (ou dépenser le seuil séquentiellement).

---

### 2. Confiance

**Confiance : 0,65.**
Ma confiance est élevée ($\approx 0,90$) sur la supériorité mathématique de (d) face à (a)–(c), mais limitée à 0,65 au global car trois paramètres décisifs manquent dans l'énoncé : la possibilité de partager les épisodes entre les quatre tests, le coût marginal d'un épisode, et le seuil de fuite réellement dangereux pour le protocole de surveillance.

---

### 3. Ce qui me ferait changer d'avis

- **Un coût :** Si chaque épisode exige une exécution coûteuse (humains dans la boucle, long déploiement d'agent) rendant $N > 4\,000$ prohibitif, j'abandonnerais l'épreuve boîte noire à $p=0,05$ au profit d'une isolation architecturale/cryptographique complétée d'un test forcé à $p=0,5$. Inversement, si les épisodes sont des simulations peu coûteuses, je pousserais $N \ge 40\,000$ pour descendre sous $\text{MDE}_{5\%} \le 0,06$ à puissance $0,95$.
- **Une conséquence d'une fausse suspension :** Si une suspension déclenche seulement une seconde tranche automatique d'épisodes pré-budgétée sans bloquer l'exploitation, un premier filtre à $\alpha=0,05$ par test comme (c) redevient acceptable en première étape d'un protocole séquentiel. Si au contraire une suspension arrête une chaîne critique ou incite les ingénieurs à contourner le protocole, je viserais un FWER par admission $\le 0,01$.
- **Une taille de fuite jugée dangereuse :** Contre un agent capable d'attendre une unique faille catastrophique (« hauts enjeux »), une fuite en variation totale de **0,05** suffit pour créer une poche représentant 5 % des épisodes où la probabilité d'audit tombe à **zéro** ($\mathbb{P}(\text{Audit}=1 \mid X \in A)=0$). Si une telle fuite est inacceptable, même (c) et (d) sont insuffisantes : aucun filtrage statistique de cette taille ne suffit sans preuve de non-interférence. À l'inverse, si l'agent doit tricher sur de nombreux épisodes et qu'une fuite $< 0,25$ reste bénigne, **(b)** suffit déjà.
- **Une propriété du test :** Si les 30 prédicteurs sur-apprennent fortement à $n_{\text{train}}=100$ positifs, ou si leur famille omet des canaux plausibles (temps de réponse, stéganographie), la garantie de puissance s'effondre et je réduirais la complexité de la famille (ou j'utiliserais un partage asymétrique, ex. 30 % apprentissage / 70 % épreuve pour des prédicteurs simples). À l'inverse, si les $4 \times 30$ statistiques sont fortement corrélées sur des trajectoires partagées, une permutation conjointe atteint un FWER de 5 % presque sans perte de MDE par rapport à (a)/(c).

---

### 4. Unité de contrôle de l'erreur et ce que chacune engage

Il faut distinguer **erreur de type I** (fausse suspension) et **erreur de type II** (fausse admission d'un dispositif fuyard) :

- **Le test :**
  - *Ce qu'il engage :* Traite chaque couple (secret, cible) isolément. Pour le type I, le taux d'échec d'un dispositif sain croît avec le nombre de vérifications ($1-(1-\alpha)^k$), ce qui pénalise l'ajout de nouvelles cibles de contrôle ; ce choix n'est cohérent que si un rejet suspend uniquement une sous-garantie granulaire sans bloquer le dispositif. En revanche, le **type II doit impérativement être contrôlé au niveau de chaque secret critique**, car la solidité de trois tests ne compense pas la fuite du quatrième.
- **L'admission :**
  - *Ce qu'elle engage :* Aligne le risque de fausse alarme ($\text{FWER} \le 5\,\%$) sur la décision opérationnelle (« valider cette version du dispositif »). Cela engage le laboratoire à figer la batterie des quatre tests par version et à exiger un diagnostic/correctif avant toute nouvelle soumission.
- **Le dispositif sur toute sa vie :**
  - *Ce qu'il engage :* Répartit un budget global $\sum_t \alpha_t \le \alpha_{\text{vie}}$ sur l'admission initiale, les mises à jour et les ré-épreuves périodiques. Or, si la vie comporte de nombreuses révisions à taille d'échantillon fixe, $\alpha_t \to 0$ fait exploser la MDE et aveugle progressivement le test contre les régressions tardives. Cela engage donc à faire croître $N_t$ au fil du temps ou à utiliser des *e-processus* avec reconstitution de budget après modification substantielle.

**Position :** L'**admission** (par version corrigée du dispositif) est la bonne unité pour le **type I** ; le **test** (avec exigence de MDE adaptée au secret) est la bonne unité pour le **type II** ; sur la **vie du dispositif**, il faut contrôler le taux de fausses alertes par unité de temps plutôt qu'un FWER cumulé figé.

---

### 5. Erreurs relevées et antériorités

#### Erreurs dans les chiffres
1. **Arrondi pour (c) à 5 % d'audit :** On retrouve exactement les chiffres du tableau par la formule normale unilatérale corrigée pour 30 prédicteurs : $\text{MDE} = (z_{1-\alpha/30} + z_{0,8})\sqrt{\frac{0,25}{(N/2)p(1-p)}}$, qui donne $0,0845$, $0,0935$ et $0,0597$ à $p=0,5$. Mais à $p=0,05$ ($p(1-p)=0,0475$), elle donne $0,194$, $0,215$ et **$\mathbf{0,137 \approx 0,14}$** pour (c) — le **0,13** affiché provient de l'approximation $1-p \approx 1$ ($\sqrt{5}\times 0,0597 = 0,1335$).
2. **Contradiction de l'énoncé « sous supposition : bras équilibrés » :** Cet intitulé contredit la dernière colonne ($5\,\%$ vs $95\,\%$). En réalité, c'est la variance de sortie du prédicteur sous le nul qui a été fixée au pire cas équilibré $q(1-q)=0,25$.
3. **Queue discrète et corrélation :** À $N=4\,000$ et $p=0,05$, $n_1 \approx 100$ sur la moitié d'épreuve : l'approximation gaussienne à $\alpha/30 \approx 4\times 10^{-4}$ avec variance nulle pire-cas est approximative. Inversement, le terme $\alpha/30$ suppose 30 prédicteurs indépendants alors que la permutation du maximum exploite leur corrélation positive — **à condition** que les statistiques soient studentisées (sans quoi les prédicteurs bruyants à $q \approx 0,5$ masquent ceux ciblant un signal rare $q \ll 0,5$). Enfin, si les quatre tests partagent les mêmes épisodes, l'indépendance est fausse et le coût réel est $N$, non $4N$.

#### Erreurs dans le raisonnement
1. **Confusion entre variation totale vraie et pouvoir séparateur d'une famille finie apprise (erreur majeure) :** Un non-rejet **n'indique pas** qu'une fuite en variation totale $> \text{MDE}$ aurait probablement été détectée. Il borne uniquement l'avantage atteint sur l'échantillon d'épreuve par les **30 prédicteurs effectivement appris**. Si la fuite emprunte une représentation absente des 30 modèles (défaut d'approximation) ou si l'apprentissage échoue sur 100 positifs (erreur d'estimation, ignorée du calcul à la main qui traite le prédicteur comme un oracle), une fuite réelle de $d_{\text{TV}} = 1$ peut donner une puissance égale à $\alpha$.
2. **Inversion de la charge de la preuve :** Poser $H_0 : \text{fuite}=0$ et admettre par non-rejet récompense les petits échantillons et les mauvais prédicteurs ; même à la MDE, il subsiste **20 %** de chance d'admettre un dispositif défaillant (puissance 0,8).
3. **Effet du ré-essai :** Suspendre « jusqu'à une nouvelle épreuve » sans modifier le dispositif ni ajuster $\alpha$ fait passer le risque d'admettre une fuite située à la MDE de $20\,\%$ (un essai) à $1 - 0,8^2 = \mathbf{36\,\%}$ (deux essais).
4. **Sens de sécurité de la TV à 5 % d'audit :** Une fuite $d_{\text{TV}} = 0,15$ (sous la MDE de (a) et (b)) permet déjà à l'agent d'identifier avec certitude une zone sans aucun audit sur 15 % des épisodes, réduisant son risque d'être pris de 5 % à **0 %**.

#### Antériorités *(toutes citées de mémoire)*
- **Lopez-Paz, D., & Oquab, M. (2017)**, *« Revisiting Classifier Two-Sample Tests »* (ICLR), et **Kim, I., Ramdas, A., Singh, A., & Wasserman, L. (2021)**, *« Classification Accuracy as a Proxy for Two-Sample Testing »* (*Annals of Statistics*), à la suite de **Friedman, J. H. (2004)**, *« On Multivariate Goodness-of-Fit and Two-Sample Testing »* : formalisent le test à deux échantillons par découpage apprentissage/épreuve d'un prédicteur et calibration par permutation.
- **Westfall, P. H., & Young, S. S. (1993)**, *Resampling-Based Multiple Testing: Examples and Methods for p-Value Adjustment* (Wiley) : théorie exacte du test par permutation du maximum (`maxT`) et nécessité de studentiser les statistiques.
- **Schuirmann, D. J. (1987)**, *« A comparison of the Two One-Sided Tests Procedure and the Power Approach for assessing the equivalence of average bioavailability »* (*Journal of Pharmacokinetics and Biopharmaceutics*) : réfute précisément la « *Power Approach* » consistant à certifier l'absence d'effet par non-rejet à $\alpha=0,05$ assorti d'un calcul de puissance à $0,80$, au profit d'un test d'équivalence ($H_0 : \text{effet} \ge \Delta$).
- **Cherubin, G., Chatzikokolakis, K., & Palamidessi, C. (2019)**, *« F-BLEAU: Fast Black-box Leakage Estimation »* (IEEE S&P) : estimation boîte noire de fuite de secret par prédicteurs appris (dans la lignée de l'indistinguabilité adverse de **Goldwasser, S., & Micali, S., 1984**, *« Probabilistic Encryption »*).
- **Greenblatt, R., Shlegeris, B., Sachan, K., & Roger, F. (2024)**, *« AI Control: Improving Safety Despite Intentional Subversion »* (ICML) : introduit l'architecture de surveillance d'agent combinant score interne et audit aléatoire à faible taux dont la sûreté dépend du secret de ces deux variables.
- **Batu, T., Fortnow, L., Rubinfeld, R., Smith, W. D., & White, P. (2013 ; conf. 2000)**, *« Testing Closeness of Discrete Distributions »* (*JACM*) (et **Le Cam, L., 1973**) : impossibilité de tester uniformément la distance en variation totale à échantillon fini sans borne structurelle sur le domaine.