# Science de la science : d'où viennent les travaux marquants — lecture sur PDF (22 novembre 2026)

Sources : `/tmp/claude-0/-home-user-controle-ia-travail/7225ef84-cf06-5367-97a0-6c2a4e600e2b/scratchpad/sources/science-combinaisons/` ; empreintes complètes : `/tmp/claude-0/-home-user-controle-ia-travail/7225ef84-cf06-5367-97a0-6c2a4e600e2b/scratchpad/sources/science-combinaisons-sha256.txt` (16 premiers signes ci-dessous). « p. N » = page du fichier PDF ; numéro imprimé entre crochets quand il diffère. Plusieurs textes ont été lus en **prépublication** et non dans la version de la revue : je le signale à chaque fois, et les chiffres peuvent différer de la version publiée.

## 1. Uzzi, Mukherjee, Stringer, Jones 2013, « Atypical Combinations and Scientific Impact », Science 342:468-472
Fichier `uzzi.pdf` (version de la revue, copie sur la page de l'auteur à Kellogg), ff927fdb43bde2b1. Lu sur PDF.
- **Mesure** : chaque paire de revues citées ensemble dans un article est comparée à des réseaux de citations tirés au hasard (algorithme de Monte-Carlo qui permute les liens et garde le nombre de citations reçues et émises par chaque article), ce qui donne un score z par paire. Pour chaque article, deux statistiques : le score z médian (« conventionalité ») et le 10e centile (« nouveauté de queue »). p. 3 [469] : « all citation links between all papers in the WOS were switched by means of a Monte Carlo algorithm ».
- **Base** : 17,9 millions d'articles du Web of Science, « over 122 million potential journal pairs » (p. 2 [468]).
- **Résultats** : la moitié des articles ont un score z médian supérieur à 69,0 dans les années 1980 et à 99,5 dans les années 1990. Seuls 3,54 % (1980) et 2,67 % (1990) des articles ont un score médian négatif (p. 3 [469]). Un « hit » est un article du 5 % le plus cité. Avec conventionalité médiane haute et nouveauté de queue haute, le taux de hits est de 9,11 sur 100, « a rate nearly double the background rate of 5% ». Avec une seule des deux qualités, il est de 5,82 ou d'environ la moitié de 9,11 ; avec aucune, 2,05 (p. 4 [470], légende de la figure 2). Les équipes de trois auteurs ou plus introduisent de la nouveauté de queue 37,7 % plus souvent que les auteurs seuls (49,7 % contre 36,2 %, p. 4 [470]). L'impact culmine entre le 85e et le 95e centile de conventionalité médiane, puis la relation s'inverse (p. 5 [471]).
- **Preuve** : corrélation sur données datées. Aucune identification causale.
- **Critiques** : Boyack et Klavans ont reproduit les traits principaux mais signalent des effets de revue et de discipline : Nature, Science et PNAS porteraient 9,4 % des combinaisons atypiques (rapporté par Tahamtan et Bornmann, arXiv 1806.00224 ; **résumé seulement**, vu par un moteur de recherche, non lu). Bornmann et al. 2019 (Journal of Informetrics, arXiv 1910.03233, `bornmann-f1000.pdf`, 1ff25c073b7e6300, p. 2) ont confronté la mesure aux étiquettes de F1000Prime : une hausse d'un écart-type du score « U » (Uzzi revu par Lee et al. 2015) accroît les étiquettes « new finding » de « 7.47% ». La validité est donc réelle mais modeste.

## 2. Rzhetsky, Foster, Foster, Evans 2015, « Choosing experiments to accelerate collective discovery », PNAS 112:14569-14574
Fichier `rzhetsky.pdf` (copie d'OSTI, version de la revue), c2b0384ef53152ac. Lu sur PDF.
- **Modèle** : les problèmes de recherche sont les liens entre produits chimiques d'un réseau de connaissances. Un modèle génératif est ajusté sur les co-mentions dans MEDLINE (1976-2010) et dans les brevets américains. Une expérience « réussit » si le lien existe dans le réseau empirique de 2010 ; les échecs ne sont pas publiés (p. 3 [14571]). Des stratégies optimales sont cherchées par recuit simulé et chaînes de Markov.
- **Résultats** (p. 1 [14569]) : « biomedical scientists pursue conservative research strategies », et ces choix deviennent plus conservateurs avec le temps. p. 4 [14572] : la stratégie observée atteint son efficacité maximale à 13 % du réseau découvert ; elle est « over three times more costly than the most efficient alternative when discovering the bulk of the network » ; la stratégie optimale pour 50 % du réseau est « nearly 10 times more efficient than the random strategy ». La publication des échecs et la coordination diminuent le coût de la découverte (p. 4-5).
- **Preuve** : modèle ajusté sur des données datées, plus simulation. **Limite majeure** : la « vérité » est le réseau publié en 2010, un monde fermé ; les auteurs n'ont « no formal guarantees on the global optimality » (p. 5 [14573]). Ils supposent aussi que le publié reflète l'effort réel et que le risque des stratégies risquées est à peu près stationnaire (p. 5, note) ; les échecs sont sous-représentés.

## 3. Foster, Rzhetsky, Evans 2015, « Tradition and Innovation in Scientists' Research Strategies », American Sociological Review 80
Fichier `foster-asr.pdf` (prépublication arXiv 1302.6906, **pas la version de la revue**), 76047890d17421a6. Lu sur PDF.
- **Base** : 6 455 756 résumés de MEDLINE (1934-2008) portant au moins deux produits chimiques annotés ; en 2008, le réseau compte 181 078 nœuds et 84 709 977 liens (p. 3).
- **Résultats** : les énoncés qui répètent un lien connu sont six fois plus fréquents que les liens nouveaux ou les sauts (85,8 % contre 14,2 %, p. 4). Une stratégie dix fois moins probable reçoit 2,26 citations de plus en moyenne ; la « surprise » de la stratégie explique 29,2 % de la variance de la moyenne des citations et 28,6 % de celle de leur écart-type (p. 6). Citations moyennes : 8,38 pour la répétition, 11,00 pour le neuf, 12,90 pour le saut. L'indifférence exigerait p(neuf) = 0,76·p(répétition) et p(saut) = 0,65·p(répétition) ; « A priori, it seems unlikely » (p. 6). La conclusion selon laquelle la récompense ne compense pas le risque repose donc sur un **jugement a priori**, non sur un taux d'échec mesuré. Les lauréats de 137 prix et les articles les plus cités font plus de sauts et de consolidations (p. 7) ; « while the increase in frequency is small, relative to the baseline it is substantial » (p. 18).
- **Limites dites** (p. 7) : annotation non uniforme dans le temps, co-mentions qui créent de faux liens, échecs exclus du corpus.

## 4. Shi et Evans 2023, « Surprising combinations of research contents and contexts are related to impact and emerge with scientific outsiders from distant disciplines », Nature Communications 14:1641
Fichier `shi.pdf` (version de la revue), f576db752e31e7f6. Lu sur PDF.
- **Mesure** : un modèle d'hypergraphe plongé dans un espace prédit les combinaisons de contenus (termes MeSH, codes PACS, sous-classes de brevets) et de contextes (revues ou classes citées). La surprise est l'improbabilité de la combinaison selon ce modèle.
- **Base** : 19 916 562 articles de MEDLINE (1865-2009), 541 448 articles de l'APS, 6 488 262 brevets américains (1979-2017) (p. 2). Analyse de nouveauté sur 10 057 935 articles et 2 436 257 brevets (p. 7-8).
- **Résultats** (MEDLINE, un hit = 10 % le plus cité) : les contextes les plus surprenants ont environ quatre fois plus de chances que le hasard d'être un hit, les contenus surprenants deux fois, les deux réunis environ cinq fois (p. 4). Les « expéditions » (distance moyenne entre le passé de publication des membres de l'équipe et la revue de l'article) les plus surprenantes ont « 3.5 times more likely than random to be hit papers » ; c'est le prédicteur le plus fort, devant la nouveauté de carrière et la nouveauté d'équipe (p. 5). Pour les brevets, la nouveauté d'expédition n'est pas significativement associée aux hits (p. 5).
- **Preuve** : corrélation. Les auteurs écrivent : « our findings call for analysis and experiments to explore the causal relationship » (p. 7).
- **Limites dites** (p. 6) : seuls les articles passés par l'évaluation par les pairs sont mesurés ; contenus et contextes sont pris au grain grossier des mots-clés et des revues.

## 5. Sourati et Evans 2023, « Accelerating science with human-aware artificial intelligence », Nature Human Behaviour 7
Fichier `sourati.pdf` (prépublication arXiv 2306.01495), 90ccea69c2b5fe61. Lu sur PDF.
- **Méthode** : des marches aléatoires sur un hypergraphe qui relie matériaux ou molécules, propriétés **et auteurs**, comparées à un modèle Word2Vec sur le seul contenu (reproduction de Tshitoyan et al.).
- **Résultats** : « up to 400% » de gain de précision pour prédire les découvertes futures (p. 1) ; environ 100 % en moyenne sur les propriétés des matériaux (p. 6) ; 43 % de précision en plus pour la réaffectation de médicaments (environ 4 000 médicaments, p. 6). 40 % des 50 auteurs les mieux classés deviennent effectivement des découvreurs un an plus tard (p. 8).
- **Hypothèses « étrangères »** : un paramètre β éloigne les prédictions de la foule. La découvrabilité chute vite quand β passe au positif ; les scores théoriques ne s'effondrent pas avant β ≈ 0,4 environ et dépassent ceux des découvertes publiées (p. 10).
- **Validation** : les hypothèses étrangères sont jugées sur des **scores théoriques de substitution** (calculs de théorie de la fonctionnelle de la densité, proximité dans les réseaux d'interactions de protéines), disponibles pour environ 45 % des propriétés (p. 10). Je n'ai trouvé aucune validation expérimentale. Les auteurs nomment une limite (p. 12) : la coautorat est la seule relation retenue.

## 6. Wang, Veugelers, Stephan 2017, « Bias against novelty in science », Research Policy 46
Fichier `wvs-nber.pdf` (document de travail NBER 22180, avril 2016, **pas la version de la revue**), d2e1bf9e19a89693. Lu sur PDF.
- **Mesure** : paires de revues citées **jamais co-citées** dans les trois années précédentes, pondérées par la distance entre les revues (cosinus) ; la nouvelle paire doit être réemployée dans les trois années suivantes (p. 7-8). Est « très nouveau » un article du 1 % supérieur de sa discipline.
- **Base** : articles du Web of Science de 2001, 1 056 936 observations ; 89 % des articles ne font aucune combinaison nouvelle (p. 10).
- **Résultats** : +12,04 % de citations pour les articles très nouveaux, et une dispersion plus forte de 14,90 % (p. 12). Rapport des chances d'être dans le 10 % le plus cité : +16,80 % ; d'être dans le 10 % le moins cité : +16,76 %. Le risque se lit donc sur les deux queues (p. 13). Chances d'être dans le 1 % le plus cité : +39,82 % (p. 13). Les articles très nouveaux sont moins souvent dans le haut du classement avec des fenêtres de moins de trois ans ; leur avantage n'apparaît qu'à partir de la quatrième année. Pour les articles moyennement nouveaux, l'avantage n'est significatif qu'avec une fenêtre de neuf ans au moins (p. 16). Le facteur d'impact de leur revue est plus bas que prévu de 10,55 % et 18,11 % (p. 18).
- **Preuve** : corrélation, avec contrôles. La qualité non observée est discutée sans être identifiée (p. 19).
- **Critique** : Bornmann et al. 2019 (`bornmann-f1000.pdf`, p. 2) écrivent : « question the use of novelty score W », car le score de Wang et al. ne montre pas de validité convergente avec les évaluateurs de F1000Prime.

## 7. Fleming 2001, « Recombinant Uncertainty in Technological Search », Management Science 47:117-132
Fichier `fleming.pdf`, ab358b9316d45eea. Lu sur PDF. Numéro imprimé = page du PDF + 116.
- **Base** : 17 264 brevets américains délivrés en mai et juin 1990, mois tirés au hasard. Coupe transversale (p. 5 [121]). Modèles binomiaux négatifs de comptage et de dispersion.
- **Résultats** (p. 11-13 [127-129]) : la familiarité des composants porte la moyenne des citations à +147 % entre son minimum et son maximum (+11,3 % par écart-type). La familiarité des combinaisons donne +332 % sur toute son étendue (+10,3 % par écart-type) et réduit la variance (jusqu'à 64 %). La familiarité des composants réduit d'abord la variance (−9,6 % au 60e centile), puis l'effet devient positif à partir du 96e centile ; l'hypothèse 2 n'est donc **pas confirmée**. L'usage cumulé d'une combinaison l'épuise : au maximum, 37,9 % des citations. Résumé (p. 1 [117]) : le nouveau est moins utile en moyenne mais plus variable.

## 8. Wu, Wang, Evans 2019, « Large teams develop and small teams disrupt science and technology », Nature 566
Fichier `wu-teams.pdf` (prépublication arXiv 1709.02445), 51a48bd3909a6794. Lu sur PDF.
- **Base** : plus de 50 millions de travaux (p. 1). Web of Science : 43 661 387 articles et 615 697 434 citations, 1900-2014. Brevets américains : 4 910 816. Logiciels de GitHub (p. 12).
- **Mesure** : indice de disruption D (de −1 à 1).
- **Résultat** : de 1 à 50 membres, la disruption baisse de 70 % pour les articles, 30 % pour les brevets et 50 % pour les logiciels (p. 3). L'effet se retrouve au sein d'un même auteur, à sujet et type d'article contrôlés (p. 1, p. 4). Les auteurs concèdent (p. 4) : « Part of the difference … is surely due to differences in the topic, research design and resources … rather than a causal factor of team size itself ».
- **Critique** : Petersen, Arroyave, Pammolli (`petersen.pdf`, def33517a012ac84, arXiv 2406.15311, p. 1 ; Journal of Informetrics 2025 selon le moteur de recherche) jugent la relation entre disruption et taille d'équipe « remarkably small in overall magnitude » ; elle passe du négatif au positif à partir de huit coauteurs une fois l'inflation des citations corrigée.

## 9. Park, Leahey, Funk 2023, « Papers and patents are becoming less disruptive over time », Nature 613 — et le débat
Fichier `park.pdf` (prépublication arXiv 2106.11184 v5, juillet 2022, **pas la version de Nature**), d67271cb8907d085. Lu sur PDF.
- **Base** : 45 millions d'articles et 3,5 millions de brevets, venus de six jeux de données (p. 2). Indice CD5.
- **Résultats** : baisse de 91,9 % à 100 % pour les articles (1945-2010) et de 78,7 % à 91,5 % pour les brevets (1980-2010) selon le texte de la p. 4. La légende de la figure 2 (p. 10) donne 93,5 % à 96,4 % pour les brevets : **incohérence interne à cette version**. Le nombre absolu de travaux très disruptifs reste à peu près constant (p. 5). La diversité des travaux cités diminue (p. 7).
- **Holst et al. 2024** (`holst.pdf`, e69d9c84f9218785, arXiv 2402.14583, p. 1) : un défaut de l'outil de graphiques a caché 972 161 articles et 142 362 brevets de CD5 = 1, restés dans l'analyse. 97 % de ces articles et 78 % de ces brevets ont **zéro référence** (p. 2). Sans eux, le déclin des articles « is negated », celui des brevets est « substantially reduced », et un réseau recâblé au hasard reproduit le déclin (p. 1).
- **Réponse de Park et al. 2025** (`park-reply.pdf`, b009daeb9fd068ac, arXiv 2503.00184, p. 1) : avec le propre modèle de régression de Holst et al., les déclins restent significatifs (p < 0,001) pour les articles et pour les brevets. Selon eux, la base SciSciNet employée par Holst et al. contient « nearly three times more 0-bcite papers ». Le commentaire et la réponse auraient paru dans Nature, le commentaire sous le titre « Dataset artefacts can partially drive the measured decline in disruption » (**résumé seulement**, page de l'INSEAD bloquée, vue par un moteur de recherche).
- **Macher, Rutzer, Weder 2024** (Research Policy 53(5) ; `macher.pdf`, 48ec3a46660ae912, arXiv 2306.10774 v2, p. 1) : « 88 percent of the decrease in the average CD index over 1980-2010 » s'explique par la troncature des citations antérieures à 1976. Le nombre de brevets très disruptifs a augmenté depuis 1980, surtout depuis 2008.
- **Petersen et al. 2024** (p. 1) : CD baisse mécaniquement quand les listes de références s'allongent (« citation inflation ») ; corrigée, la disruption augmente légèrement de 2005 à 2015.
- **Bilan** : la baisse de la diversité des titres et des citations n'est pas visée par ces critiques ; la baisse de CD pour les brevets est la plus fragilisée ; pour les articles, la question reste disputée.

## 10. Liu et al. 2021, carrières et périodes fastes, Nature Communications 12 ; Sinatra et al. 2016, Science 354
`liu-hot.pdf` (prépublication arXiv 2103.01256), ace834bf3f614e94. Lu sur PDF.
- **Base** : plus de 800 000 œuvres de 2 128 artistes (p. 3), 79 000 films de 4 337 réalisateurs (p. 3), 20 040 scientifiques du Web of Science et de Google Scholar (p. 4). L'exploration est mesurée par l'entropie des styles ou des sujets, comparée à des carrières tirées au hasard.
- **Résultat** : une exploration suivie d'une exploitation accroît la probabilité qu'une période faste commence de 20,5 % (artistes), 13,8 % (réalisateurs) et 19,2 % (scientifiques) au-dessus de la base. C'est « the only positive lift among all combinations » ; l'exploration seule ne suffit pas (p. 6). Les équipes sont plus petites avant la période faste et plus grandes pendant (p. 7).
- **Preuve** : corrélation contre des carrières tirées au hasard. Je n'ai trouvé aucune réserve causale explicite dans le texte principal (une seule mention de « limitations », sur la couverture des données).

`sinatra.pdf` (version de la revue, copie sur barabasi.com), 3d07858750d3adbd. Lu sur PDF.
- **Règle de l'impact au hasard** : la position N*/N du travail le plus cité est uniforme dans la suite des publications (p. 3 [aaf5239-2]). Le modèle Q tient l'impact pour le produit d'une capacité Q, stable au cours de la carrière, et d'une chance p (p. 5-7).
- **Base** : 2 887 physiciens de l'APS, avec au moins 20 ans de carrière et au moins 10 articles. Les auteurs les disent « successful as they survived many selection processes » (p. 7 [aaf5239-6]), ce qui signale un biais du survivant. Des données de Web of Science et de Google Scholar (24 630 profils) sont rapportées en annexe (p. 10).

## 11. Vicinanza, Goldberg, Srivastava 2023, PNAS Nexus 2:pgac275
Texte complet XML de PubMed Central (`PMC9832965.xml`, ac382eebe121ae25). Lu sur page HTML ou XML, sans pagination. Le PDF est bloqué.
- **Ce n'est pas un texte sur la science** : les corpus sont 4,9 millions de discours du Congrès, 4,2 millions de décisions de justice et 108 334 conférences téléphoniques de résultats d'entreprises. La prescience est la baisse de la perplexité de BERT entre deux périodes.
- **Résultats** : la prescience prédit la réélection, les citations des décisions et les rendements boursiers. « Highly prescient decisions are 22 times more likely to come from the State Appeals Courts than the US Supreme Court. » Les auteurs proposent eux-mêmes l'extension à la science sans l'avoir faite.
- L'article porte la mention « This article has been corrected » (pgad016, non lu).

## 12. Kneeland, Schilling, Aharonson 2020, Organization Science 31
**Non lu** : la page de l'éditeur est sous licence CC BY-NC-ND mais bloquée par une protection anti-robots. **Résumé seulement** (via un moteur de recherche) : trois procédés rendent les découvertes lointaines plus probables, à savoir de longs chemins de recherche, le raisonnement scientifique et la recombinaison lointaine. Selon Cornell, l'étude porte sur 1,5 million de demandes de brevet (1990-2000) et des entretiens. À vérifier sur PDF.

## 13. Travaux récents (2024-2026)
- **Hao, Xu, Li, Evans**, « Artificial Intelligence Tools Expand Scientists' Impact but Contract Science's Focus » (Nature 2026 d'après le moteur de recherche ; `hao.pdf`, 5ffdef976d9e9206, arXiv 2412.07727 v4, novembre 2025). Lu sur PDF.
  - Base : 41,3 millions d'articles de sciences naturelles ; détection de l'usage de l'intelligence artificielle par un modèle de langage, score F1 de 0,875 (p. 1) ; 310 957 articles détectés, soit 0,75 % (p. 2).
  - Résultats au niveau individuel : 3,02 fois plus d'articles, 4,84 fois plus de citations, chef de projet 1,37 an plus tôt (p. 1, p. 3).
  - Résultats collectifs : étendue des sujets −4,63 % (médiane), engagement des travaux suivants −22,00 % (p. 1, p. 6).
  - Les auteurs écrivent : « we cannot fully identify the causal linkage » (p. 8). La v1 donnait d'autres chiffres (67,9 millions d'articles), selon le moteur de recherche.
- **Le débat sur la disruption** (voir le point 9) est le second résultat récent le plus pertinent : il nuance fortement Park et al. et la relation entre taille d'équipe et disruption de Wu et al.
- Également vu : Yu, Rahwan, Jia, « Knowledge Independence Breeds Disruption but Limits Recognition » (arXiv 2504.09589 v2, prépublication ; `knowledge-independence.pdf`, 4c07cc968dba00b8 ; seul le résumé de la p. 1 a été lu). Sur 114 millions de publications, la part de références qui ne se citent pas entre elles prédit la disruption et expliquerait son déclin. **Ma réserve** (non dite par les auteurs) : cette mesure est proche par construction de l'indice CD.

## Synthèse (huit lignes)
1. **Solide en corrélation, très répliqué** : le travail nouveau a un rendement en citations plus variable (Fleming, p. 1 et 13 ; Wang et al., p. 13 sur les deux queues ; Foster et al., p. 6) et une reconnaissance plus tardive (Wang et al., p. 16).
2. **Solide en corrélation** : un fond conventionnel avec une part atypique va avec un taux de hits à peu près doublé (9,11 % contre 5 %, Uzzi, p. 4) ; la validité de la mesure par rapport aux experts reste modeste (+7,47 %, Bornmann et al.).
3. **Corrélation seulement** : la surprise venue d'outsiders éloignés (3,5 fois, Shi et Evans, p. 5) ; les auteurs demandent eux-mêmes des tests causaux.
4. **Modèle à monde fermé** : la thèse « les scientifiques sont trop prudents » (Rzhetsky et al.) repose sur un réseau de 2010 pris comme vérité ; chez Foster et al., la récompense insuffisante du risque est une inférence a priori.
5. **Contesté** : le déclin de la disruption (Park et al.) est attaqué sur les artefacts de données, la troncature (88 % pour les brevets) et l'inflation des citations ; il est défendu par les auteurs. L'effet de la taille d'équipe est jugé faible par Petersen et al.
6. **Corrélation** : l'exploration suivie d'exploitation avant une période faste (+14 à +21 %) ; le placement au hasard du meilleur travail est mesuré sur des carrières survivantes.
7. **Hors science** : la prescience née à la périphérie (Vicinanza et al.) concerne la politique, le droit et les entreprises.
8. **Récent, corrélation** : l'intelligence artificielle accroît l'impact individuel et resserre les sujets (−4,63 %), sans causalité établie.

## Non vérifié
- Kneeland et al. 2020 : PDF bloqué, résumé seulement.
- Versions des revues de Foster et al. (ASR), Sourati et Evans (Nature Human Behaviour), Wang et al. (Research Policy), Wu et al. (Nature), Park et al. (Nature), Liu et al. (Nature Communications) et Hao et al. (Nature) : seules les prépublications ont été lues.
- Commentaire de Holst et al. et réponse de Park et al. parus dans Nature (titre « partially » et date non vérifiés).
- Version publiée de Petersen et al. au Journal of Informetrics.
- Réplication de Boyack et Klavans : non lue.
- Erratum de Vicinanza et al. (pgad016).
- Annexes : supplément d'Uzzi et al., informations complémentaires de Rzhetsky et al. (tableau S1, figure S11), annexes de Sinatra et al.
- Tout ce qui est rapporté d'après un moteur de recherche porte la mention « résumé seulement ».
