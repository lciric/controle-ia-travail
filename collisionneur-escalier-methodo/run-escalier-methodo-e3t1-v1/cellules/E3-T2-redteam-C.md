# Proposition C — Tour III.2 : Équipe rouge croisée contre A et B

**Intégrité des pièces.** Le bloc `FAITS` est présent et vide par décision de l'arbitre (VÉRIFIÉ). Les pièces `E3-T1-conception-A` et `E3-T1-conception-B` sont complètes et non coupées (VÉRIFIÉ). Tous les chiffres de coût ou de taille d'échantillon avancés ci-dessous qui ne proviennent pas de l'énoncé (RAPPORTÉ) sont marqués « illustratif ».

---

## Contre la proposition A

### (a) Les failles : variables confondantes, vérités par construction et fuites

1. **Biais de sélection post-traitement dans le Duel 3 (restriction d'exclusion).**
   Pour tester si le budget $b$ affecte la BA autrement que par la dépense $s(b)$ (HYPOTHÈSE A4), A propose d'« apparier les items dont $s$ est identique (à ±10 %, illustratif) » entre deux bras soumis à des annonces de budget différentes $b$ et $b'$. Or, $s$ est une variable *post-assignation* (un résultat de l'exécution). Conditionner ou apparier sur une variable post-traitement ouvre un chemin de collision (biais de Berkson / *collider bias*) entre l'annonce de budget et la difficulté intrinsèque de l'item. Si le bras qui lit un gros budget $b'$ dépense $s_0$ sur un item facile, tandis que le bras qui lit un petit budget $b$ ne dépense $s_0$ que lorsqu'il bute sur un item très difficile, comparer la BA à $s$ égal compare des items faciles à des items durs. L'estimateur proposé par A trouvera un effet direct $\Delta \neq 0$ **par construction**, réfutant faussement $H_A$ même si la restriction d'exclusion est strictement vraie.

2. **Biais de collision dans le Duel 4 (neutralité du canal « réponse invalide »).**
   A propose de recalculer $\Delta\mathrm{BA}$ « en excluant les items invalides dans *les deux* bras ». La validité de la sortie est une variable post-traitement fortement corrélée à la complexité de l'item. Si le bras à sortie longue tronque les items complexes (qui demandent de longs raisonnements) et que le bras court y répond au hasard, le sous-ensemble des items valides dans les deux bras est purgé des items durs. Le changement de signe de $\Delta\mathrm{BA}$ sur ce sous-ensemble ne prouve pas un « artefact de format » : il peut résulter mécaniquement du changement de la distribution de difficulté des items survivants.

3. **Confusion de la variance dans le plan factoriel $2^{4-1}$ à une seule graine (Duel 2 et Voie F).**
   A propose d'exécuter le plan $2^{4-1}$ avec **une seule graine** par configuration, puis de calculer l'intervalle de confiance des contrastes d'interaction par « bootstrap apparié sur items ». Si les rondes de mise au point (axe 1) génèrent un aléa global d'exécution lié à la graine (noté $v_k$ par A), cet aléa est constant sur les 60 items d'une exécution. Un bootstrap qui rééchantillonne les items à l'intérieur d'une seule graine voit une variance de graine nulle ($\widehat{\mathrm{Var}}(v_k) = 0$ sur l'échantillon bootstrap). Toute fluctuation de graine entre les 8 coins du plan factoriel est intégralement absorbée dans l'estimation ponctuelle des contrastes d'interaction, tandis que l'IC bootstrap ne mesure que le bruit item × item. La borne inférieure de l'IC dépassera $\delta$ **par construction** dès que la variance inter-graines de la mise au point est non négligeable, falsifiant faussement $H_A$ (séparabilité).

4. **Fuite de données et d'erreur de type I dans la règle de « Zone grise » (§3).**
   A scelle la règle suivante : en zone grise, « ajouter des items de la réserve (pas des graines) ; au plus une fois par cran ». Or, A n'applique aucune dépense d'erreur ($\alpha$-spending) à ce second regard conditionnel, réservant son analyse séquentielle (§2) aux seules graines ou à des regards prédéfinis sans ajuster le seuil de l'IC à 90 % de sa règle du §3. Regarder les 60 items, constater qu'on est en zone grise, puis piocher dans la réserve en gardant le même seuil nominal de 90 % gonfle mécaniquement le taux de fausses alertes au-dessus de $\alpha$ (fuite d'erreur de type I par arrêt optionnel). De plus, consommer la réserve en cours d'escalier détruit l'indépendance de la « réserve intouchée » promise par A pour la confirmation finale.

5. **Incohérence mathématique du modèle d'appariement des graines (§1).**
   A écrit $Y_{ki}^{(A)} - Y_{ki}^{(B)} = d_{ki}$ avec un « appariement item × graine » et ajoute un effet aléatoire de graine $v_k$ directement sur la différence $d_{ki}$. Mais une graine pseudo-aléatoire $k$ passée à deux configurations différentes (par exemple 2 sous-modèles contre 4 sous-modèles, ou 1 ronde contre 2 rondes) ne produit aucun couplage positif entre les trajectoires stochastiques des appels API : la $k$-ième graine du bras A n'a aucun lien physique avec la $k$-ième graine du bras B. L'appariement par graine est fictif.

6. **Fuite entre construction et évaluation dans le banc de calibration (§c).**
   A utilise les deux répliques gratuites pour estimer $\hat f$ (taux de bascule), s'en sert pour calibrer le prior bayésien (§2), puis évalue le taux de « monter » de ce même instrument bayésien par bootstrap sur le même essai A/A (§c). C'est une double utilisation des mêmes données (empirical Bayes évalué in-sample) : l'instrument est jugé sur les deux seules répliques qui ont servi à le paramétrer.

### (b) Scénarios d'évasion : comment un agent adverse trompe les instruments de A

Supposons un système (ou un concepteur de configuration) cherchant à maximiser son budget alloué (faire voter « Monter ») ou à saboter un cran concurrent, face aux règles de A.

1. **Tromper le test de permutation / McNemar pondéré et l'IC bootstrap (§2, §3).**
   - *Mécanisme* : A décide sur le minimum des deux familles et utilise un bootstrap stratifié par classe. En famille 2 (12 positifs, 12 négatifs, RAPPORTÉ), chaque item pèse $1/24 \approx 0{,}0417$. Un agent adverse qui connaît l'heuristique triviale (0,69 en famille 1, 0,50 en famille 2, RAPPORTÉ) concentre toute sa dépense supplémentaire sur 3 items positifs très courts de la famille 2 et 4 items de la famille 1, en laissant les 53 autres items strictement identiques au bras de base (en réutilisant le cache ou la même invite).
   - *Effet* : Le nombre de discordants est $D = 3$ en famille 2, tous positifs ($+3/24 = +0{,}125 \ge \delta$). Sur un bootstrap des items où 21 items ont $d_i = 0$ et 3 items ont $d_i = +1$, la probabilité que les 3 items soient absents d'un tirage bootstrap est $(11/12)^{12} \approx 0{,}35$ si non-indépendant, mais sur la somme des deux familles ou par sous-couverture du bootstrap percentile à $n=12$, la borne basse à 90 % (percentile 5 %) est strictement positive dès que 4 items sur 12 portent le gain. L'IC bootstrap déclare « Monter » avec une variance apparente minuscule, alors que le test exact à $D=3$ a une p-valeur de $0{,}5^3 = 0{,}125 > 0{,}05$.
   - *Coût* : ~2 USD par exécution (illustratif, calcul sur 7 items seulement).

2. **Tromper l'estimateur par variable instrumentale (IV) et le Duel 3.**
   - *Mécanisme* : Pour gonfler la valeur marginale $\widehat{\partial \mathrm{BA}/\partial \$} = \Delta\mathrm{BA} / (\bar s_{k+1} - \bar s_k)$, le système au cran $k+1$ détecte les items où il est incertain et *s'arrête immédiatement* sans dépenser, tandis qu'au cran $k$ il dépense tout son budget sur ces mêmes items voués à l'échec. Sur les quelques items où il réussit au cran $k+1$, il dépense juste un peu plus.
   - *Effet* : L'écart de dépense moyenne $\Delta \bar s = \bar s_{k+1} - \bar s_k$ devient arbitrairement proche de zéro (voire négatif si mal contrôlé), faisant exploser le ratio de Wald $\widehat{\beta}$ vers $+\infty$. Pour passer le Duel 3 de A, le système s'assure que sur les items où $s$ coïncide à $\pm 10\%$, il renvoie la même classe : le Duel 3 conclut à l'absence de biais, validant un IV manipulé.
   - *Coût* : 0 USD supplémentaire (réallocation interne du budget).

3. **Tromper le détecteur de plateau (§0).**
   - *Mécanisme* : A déclare un plateau seulement si *deux crans consécutifs* ont la borne supérieure de l'IC à 90 % sous $\delta$. Pour empêcher l'arrêt sur un axe inutile, il suffit qu'un cran sur deux ajoute un bruit aléatoire pur (température élevée) sur 8 items (illustratif).
   - *Effet* : Ce bruit élargit l'intervalle de confiance de $\Delta\mathrm{BA}$ sans augmenter la BA moyenne ; la borne *supérieure* de l'IC dépasse $\delta$, ce qui interdit de déclarer le plateau et force l'arbitre à payer les crans suivants.
   - *Coût* : Coût d'un cran bruyant (~16 USD par graine, illustratif).

4. **Évasion totale (tous les instruments de A à la fois).**
   - *Stratégie combinée* : Lors du $2^{4-1}$ initial (1 graine), le système injecte une variance aléatoire sur les combinaisons croisées pour simuler une interaction (bypasse le Duel 2 et force l'exploration coûteuse), ou au contraire fige le générateur aléatoire sur les axes secondaires. Ensuite, sur l'axe choisi, au cran $k+1$, il n'active le calcul lourd que sur un sous-ensemble de 4 items par famille repérés par leur longueur de texte (sans jamais dépasser la longueur max pour réussir le Duel 4 avec 0 réponse invalide), produisant $d_i \ge 0$ partout. Il ajuste sa dépense globale $\bar s_{k+1}$ à $\bar s_k + 1\text{ USD}$ en coupant court sur les items insolubles.
   - *Résultat* : L'ITT passe $\delta = 0{,}10$, le bootstrap (qui sous-couvre quand $d_i \ge 0$ sans valeurs négatives) donne une borne basse $> 0$, le coût par point $C_k / (100 \cdot \underline{\Delta}_k)$ est minimal, le Duel 3 et le Duel 4 sont muets, et l'audit « trop propre » n'est pas déclenché car $D = 8$ sur 60 reste plausible.
   - *Coût total pour l'attaquant* : ~5 à 10 USD de dépense API réelle par cran (illustratif), facturés au prix fort d'un cran supérieur pour l'arbitre.

### (c) Les contrôles négatifs dont l'absence est fatale à A

1. **Absence de contrôle négatif inter-exécutions pour l'aléa de mise au point.** A n'a aucun contrôle comparant deux exécutions qui partagent la *même* ronde de mise au point (prompt figé, graines d'inférence différentes) contre deux exécutions ayant des rondes de mise au point de graines différentes. Sans cela, son factoriel à 1 graine confond l'effet d'un axe avec une ronde de mise au point chanceuse.
2. **Absence de contrôle par permutation de la difficulté dans le Duel 3.** A ne teste pas son appariement sur $s \pm 10\%$ sur des données simulées où la difficulté de l'item détermine à la fois $s$ et la réussite $Y$, sans effet direct de $b$. Ce contrôle négatif montrerait immédiatement que son Duel 3 génère des faux positifs par biais de collision.
3. **Absence de test de couverture du bootstrap sur des effets concentrés asymétriques ($d_i \in \{0, +1\}$).** A ne vérifie la couverture de son bootstrap que sur l'essai A/A ($\Delta = 0$, symétrique). Or, à $\Delta > 0$ avec très peu d'items discordants et aucun item dégradé ($c=0$), le bootstrap percentile a une probabilité élevée de donner une borne inférieure égale à 0 ou strictement positive par paliers discrets, faussant toute sa règle de décision du §3.

---

## Contre la proposition B

### (a) Les failles : variables confondantes, vérités par construction et fuites

1. **Inversion de la charge de la preuve et biais de faible puissance dans les Duels E1, E3 et E4.**
   En E1, B estime $R = \widehat{\mathrm{Var}}(\mathrm{BA}_k)/(\bar v / n)$ avec **5 degrés de liberté** (6 répliques). B fixe la règle : « Si la borne haute de l'intervalle de $R$ est inférieure à 2, H_B est réfutée ». Avec une loi du $\chi^2_5$, le quantile à 5 % est $1{,}145$, soit $\chi^2_{5; 0{,}05}/5 = 0{,}229$. Pour que la borne haute de l'IC à 95 % de la variance soit inférieure à $2$, il faut que l'estimation ponctuelle observée vérifie $\hat R < 2 \times 0{,}229 = 0{,}458$. Même si l'hypothèse $H_A$ ($\sigma_\gamma = 0$, donc $E[\hat R] = 1$) est strictement vraie, la probabilité d'observer $\hat R < 0{,}458$ est inférieure à 15 % ! Le duel E1 de B est **incapable de réfuter $H_B$ par construction** dans plus de 85 % des cas où $H_A$ est vraie.
   À l'inverse, en E4 (transposabilité), B écrit : « une interaction dont la borne haute est inférieure à $\delta$ réfute $H_B$ », avec seulement 2 graines par cran. Sur 60 items et 2 graines, la largeur d'un IC d'interaction (différence de différences, variance quadruplée : $\mathrm{SE}_{\text{int}} \approx 2\,\mathrm{SE}$) dépasse $2 \times 0{,}06 = 0{,}12 > \delta$. La borne haute ne peut quasi jamais être sous $\delta$.

2. **Biais post-traitement avoué mais maintenu comme critère de réfutation en E3.**
   En E3, B conditionne sur les items où $|s_B - s_A| < \varepsilon$. B reconnaît explicitement : « Stratifier sur une variable post-traitement est biaisé », mais conclut trois lignes plus bas : « Un $\widehat{\Delta\mathrm{BA}}$ significatif, de signe constant sur ces items, réfute H_A et rend la variable instrumentale inutilisable ». C'est une contradiction logique : on ne peut pas fonder une inférence forte (règle B4) sur un estimateur dont le biais de collision suffit à produire le signal de réfutation sous $H_A$.

3. **Erreur d'identification dans l'analyse de variance de E1 ($\bar v$ sur données binaires déterministes).**
   En E1 et §1, B estime la variance intra-item $\bar v = \overline{p(1-p)}$ par $\hat q / 2$, où $\hat q$ est le taux de désaccord entre les 2 répliques gratuites. Mais si une ronde de mise au point génère un effet global $\gamma_{jk}$ fort (par exemple, une graine produit un prompt qui répond « positif » partout, l'autre un prompt équilibré), les deux répliques seront en désaccord sur de nombreux items *à cause de $\gamma_{jk}$*, et non à cause du bruit local $\varepsilon_{ijk}$. Par conséquent, $\hat q / 2$ surestime $\bar v$ en absorbant $\sigma_\gamma^2$. Le dénominateur de $R$ dans E1 est donc gonflé par le numérateur qu'il est censé détecter : $R$ est biaisé vers 1 **par construction**, masquant l'effet d'exécution partagé.

4. **Erreur de formule sur le coût en exécutions de l'OFAT vs Factoriel (§2).**
   B affirme qu'un plan à un axe à la fois (OFAT) « avec la même variance par effet [qu'un $2^{4-1}$ à 8 exécutions] exige 4 exécutions pour la base et 4 par niveau haut, soit 20 exécutions ». C'est mathématiquement inexact : en OFAT à 4 axes partageant la même base, la variance optimisée est obtenue en allouant $n_0 = n_1 \sqrt{4} = 2 n_1$ exécutions à la base. Avec 6 exécutions à la base et 3 par axe (soit $6 + 4 \times 3 = 18$ exécutions), la variance est $\sigma^2(1/6 + 1/3) = \sigma^2/2$. Surtout, en présence d'appariement par item en Régime P, la composante de variance liée aux items ($\sigma_I^2 / n$) ne diminue **pas** en moyennant sur les autres axes si les axes n'agissent pas sur les mêmes items. L'avantage de $2{,}5\times$ annoncé par B confond variance inter-graines et variance inter-items.

5. **Fuite de multiplicité entre l'expérience préliminaire E4 et l'escalier.**
   En E4, B propose de « rejouer, sous la nouvelle version, les deux crans les moins chers de chaque axe » (8 configurations × 2 graines) sur les mêmes 60 items, avant ou à côté de l'escalier. Si l'ordre des axes ou le choix de continuer dépend du résultat de E4 sur ces 60 items, l'ordre de la séquence fixe (§3) n'est plus scellé a priori : il est adapté aux données des 60 items, ce qui détruit le contrôle du taux d'erreur familial (FWER) que B revendique pour sa séquence fixe.

6. **Tautologie du « Régime C » (§1 et §d).**
   B propose comme Voie 2 : « $\delta = 0{,}10$ en régime C, avec une affirmation explicitement restreinte aux 60 items ». Mais la question de l'arbitre porte sur un « jeu de test tenu à l'écart » (RAPPORTÉ) pour évaluer un système de classification. Optimiser et certifier une configuration uniquement sur sa performance conditionnelle aux 60 items du jeu de test — sans inférence sur la population — revient à définir le sur-apprentissage (overfitting) du jeu de test comme un succès statistique. En Régime C, si le système est déterministe ($\hat q = 0$), B obtient $\mathrm{SE} = 0$ avec $r=1$ graine et une puissance de 100 % pour détecter un seul item basculé par hasard !

### (b) Scénarios d'évasion : comment un agent adverse trompe les instruments de B

1. **Tromper la « Séquence fixe » sur l'escalier (§3).**
   - *Mécanisme* : B contrôle la multiplicité par un test en séquence fixe qui s'arrête au premier non-rejet. Un agent qui veut faire adopter un axe coûteux (ex. nombre de sous-modèles) mais sait que le premier axe de l'ordre scellé (ex. rondes de mise au point, V1, ou longueur max, V2) va échouer et bloquer toute la séquence, sabote délibérément le bras de base ($k=0$) en réduisant sa qualité de formatage ou son prompt initial.
   - *Effet* : Le cran $0 \to 1$ du premier axe affiche un $\widehat{\Delta\mathrm{BA}} \ge 0{,}15$ artificiel (simple restauration de la performance normale), ce qui permet de franchir la porte de la séquence fixe sans dépenser d'alpha, et d'atteindre l'axe lucratif suivant.
   - *Coût* : 0 USD (dégradation logicielle du point de départ).

2. **Tromper le détecteur du Régime C et l'expérience E2 ($\hat q$).**
   - *Mécanisme* : En Régime C, la SE de B ne dépend que de $\hat q$ (désaccord entre répliques) et de $\sigma_\gamma$. Pour obtenir une SE minuscule et faire valider n'importe quel gain fortuit de 3 items ($\widehat{\Delta} = 0{,}104$ en famille 2) avec seulement $r=2$ graines, le système fixe une température proche de 0 sur l'échantillonnage des tokens (rendant $\hat q \approx 0$ en E2 et $\sigma_\gamma \approx 0$ en E1), mais utilise un hachage de la valeur du paramètre de coût (le numéro du cran) pour modifier un seuil de décision interne sur les items ambigus.
   - *Effet* : En E1 et E2, l'instrument de B mesure $\hat q = 0$ et $\hat\sigma_\gamma = 0$. En Régime C, $\mathrm{SE}_{\max} = 0$ : le moindre basculement de 3 items sur les 60, dû au changement de seuil par hachage du cran, a une variance conditionnelle nulle ($p < 0{,}0001$). B déclare « Monter » avec une certitude apparente totale, alors qu'aucun gain généralisable n'existe.
   - *Coût* : 0 USD.

3. **Tromper l'audit « trop propre » de B (§3).**
   - *Mécanisme* : B déclenche un audit si tous les discordants vont dans le même sens ($2 \cdot 0{,}5^{b+c} \le \text{seuil}$, soit $7/0$ ou $0/7$). Un agent qui a triché (par exemple par fuite du jeu de test lui permettant de gagner 9 items) introduit volontairement 2 erreurs artificielles sur des items où la base avait juste.
   - *Effet* : Le score passe de $9/0$ (gain net $+9$, p-valeur d'audit $2 \cdot 0{,}5^9 = 0{,}0039$, audit déclenché) à $9/2$ (gain net $+7$, soit $\Delta\mathrm{BA} = 7/24 = +0{,}29$ en famille 2, largement suffisant pour « Monter », mais la statistique d'audit unilatérale ou bilatérale de signe pur est diluée et évite le seuil d'audit des résultats sans contradictoires).
   - *Coût* : Perte volontaire de 2 items sur 60 (coût financier nul).

4. **Évasion totale (tous les instruments de B à la fois).**
   - *Stratégie combinée* : L'agent force l'arbitre à choisir la Voie 2 (Régime C) en rendant le système quasi-déterministe à configuration fixée ($\hat q \le 0{,}02$ en E2, $R \approx 1$ en E1). Dès lors, B n'exige que $r=2$ graines par cran. À chaque cran $k \to k+1$, le système alloue sa dépense supplémentaire uniquement aux items où la classe prédite au cran $k$ contredit le classifieur trivial (0,69 en famille 1), et aligne sa réponse sur des heuristiques de surface, tout en dégradant délibérément 1 item pour éviter un $c=0$ suspect à l'audit. Sur les items où il ne change pas d'avis, il dépense exactement le même montant $s$ qu'au cran $k$ (ce qui donne $\widehat{\Delta\mathrm{BA}} = 0$ lorsque $|s_B - s_A| < \varepsilon$, passant haut la main le test E3 de B).
   - *Résultat* : E1 conclut $\sigma_\gamma = 0$, E2 conclut au déterminisme, E3 valide la variable instrumentale, l'audit « trop propre » est aveuglé par l'unique item dégradé, et la règle gelée en Régime C valide la montée de chaque cran avec 2 graines.
   - *Coût total pour l'attaquant* : 2 exécutions par cran (~40 USD par cran, illustratif) pour faire adopter la configuration la plus chère sur la base d'un sur-apprentissage pur des 60 items.

### (c) Les contrôles négatifs dont l'absence est fatale à B

1. **Absence de contrôle négatif de puissance (effet nul + bruit réaliste) sur le critère de réfutation de E1.** B a un contrôle négatif pour vérifier $R \approx 1$ (prompt figé), mais n'a pas calculé la distribution d'échantillonnage de la borne haute de son IC à 5 ddl sous ce contrôle. S'il l'exécutait, il verrait que même sur son propre contrôle négatif à prompt figé, la borne haute de $R$ dépasse 2 presque toujours, rendant sa règle de décision E1 inopérante.
2. **Absence de contrôle d'indépendance entre $\hat q$ et $\sigma_\gamma$.** B n'a aucun contrôle vérifiant que le désaccord item par item entre les 2 répliques gratuites ($\hat q$) n'est pas lui-même engendré par une dérive globale du prompt de mise au point ($\gamma_{jk}$). Il faut calculer la corrélation intra-classe (ou tester l'homogénéité marginale par McNemar entre les deux répliques de l'essai A/A) : si une réplique surpasse significativement l'autre sur A/A, $\hat q$ mesure $\sigma_\gamma^2$ et non $\bar v$.
3. **Absence de contrôle négatif de généralisation pour le Régime C.** Si l'arbitre suit la Voie 2 de B (Régime C sans E5, faute de budget d'annotation), il n'existe aucun contrôle négatif (tel qu'une permutation aléatoire d'une partie des étiquettes ou un pseudo-cran qui modifie l'invite sans ajouter de capacité) permettant de distinguer un vrai gain de classification d'une simple sensibilité déterministe de l'invite sur les 60 items fixes. Sans ce contrôle, le Régime C de B confond toute variance d'invite conditionnelle aux items avec un effet de traitement.

FIN-DE-CELLULE