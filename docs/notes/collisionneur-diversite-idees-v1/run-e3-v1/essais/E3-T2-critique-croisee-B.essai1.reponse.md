# Proposition B — Tour III.2 : Critique croisée de méthode

---

## Sur la proposition A

### (a) Défauts de méthode

**1. M1 (regroupement après jugement) introduit une variable confondante entre taille du nul et puissance en génération suivante.** A propose de ne retenir qu'un représentant par groupe, tiré au sort, puis de former le nul suivant sur ces représentants. Mais le nul v8 contient aussi des **recombinaisons** des lois d'archive (RAPPORTÉ). Réduire l'archive de 11 lois à quelques représentants ne réduit le nul que si les recombinaisons sont recalculées sur l'archive réduite. A ne le précise pas. Si les recombinaisons sont conservées intégralement, le nul ne rétrécit pas autant qu'attendu ; si elles sont recalculées, l'espace des recombinaisons change et le gain de puissance est confondu avec la composition combinatoire du nul réduit. L'expérience E2 de A mesure le taux de copies promues et la perte de D_oracle, mais ne sépare pas ces deux sources de variation du nul.

**2. D_oracle est vrai par construction quand le monde est simple.** Sur un monde à une seule composante détectable, D_oracle vaut 1 pour toute fiche correcte. A le reconnaît et l'utilise comme contrôle négatif — c'est bien — mais l'instrument ne peut alors rien discriminer entre mécanismes de diversification sur ces mondes. Si la proportion de mondes simples dans les 50 est non négligeable (ce que le filtre volontaire empêche de savoir), la puissance de E1 est diluée. Aucun critère préenregistré ne protège contre cette dilution.

**3. E3 (deux modèles vs N tirages) confond la famille du modèle et le décodage.** Kimi et Argon diffèrent par l'architecture, la famille d'entraînement, le relais local, et potentiellement le décodage (température, noyau). À coût apparié, N tirages d'un seul modèle utilisent un seul décodeur avec des graines différentes. Si le gain de deux fournisseurs vient de la variance inter-décodeurs plutôt que de la diversité des représentations internes, l'interprétation « deux modèles valent mieux qu'un » est fausse — c'est « deux décodeurs valent mieux qu'un ». A ne propose aucun bras intermédiaire (même modèle, deux températures différentes, ou deux prompts système différents) pour isoler cette confondante.

**4. Le choix du représentant par tirage au sort crée un bruit non réductible.** A reconnaît que le représentant n'est pas nécessairement le meilleur membre du groupe, mais n'évalue pas la variance induite par le tirage. Sur un monde donné, selon la graine, un représentant faible pourrait échouer au test de mort (seuil 0,02 nat, RAPPORTÉ) là où un autre membre du même groupe survivrait. E2 telle que proposée ne distingue pas « le regroupement perd une composante » de « la graine du tirage a été malchanceuse ». Il faudrait répéter E2 sur plusieurs graines de tirage par monde, ce qui n'est pas budgété.

**5. M6 (extension du nul) est présentée comme compagnon obligatoire de M2, mais les deux ne sont jamais testées ensemble dans un duel.** E4 teste M2 seule, puis A dit « si H_B tient, M2 n'est admissible qu'avec M6, et E4 est rejouée avec M6 ». Mais rejouer E4 après avoir vu les résultats de E4 sans M6 viole l'esprit du préenregistrement (R1). Les deux configurations (M2 seule, M2+M6) devraient être préenregistrées comme bras distincts dès le départ.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **D_oracle perd sa puissance** quand les composantes du monde planté ne sont pas séparables sous la loi de probabilité jointe. Si deux composantes $c_1, c_2$ sont colinéaires dans l'espace des traits (par exemple z1 et une interaction z0·z1 quand z0 est binaire), neutraliser $c_1$ neutralise aussi partiellement $c_2$. La procédure « monde variant $w \setminus c$ » suppose que la neutralisation est propre. Formellement : si $p^\star(y \mid \mathbf{z})$ se factorise comme $f(g_1(z_1), g_2(z_0, z_1))$ où $g_1$ et $g_2$ ne sont pas identifiables séparément dans la grammaire, alors le contraste $\Delta \text{log-score}$ entre $w$ et $w \setminus c_1$ dépend de $c_2$, et D_oracle surestime la couverture.

- **Le regroupement par D_contenu (Jensen-Shannon sur le jeu factice) devient non jugeable** quand le jeu factice $X$ du gardien ne couvre pas les régions de l'espace des traits où deux lois divergent. Si la grille factice est uniforme sur le domaine mais qu'un effet de sous-population n'agit que sur une fraction $\alpha$ de la grille, la JSD moyenne est diluée par un facteur $\alpha$. Avec un seuil $\tau$ calibré sur des mondes pilotes à effets homogènes, une paire de lois divergentes sur une sous-population rare sera fusionnée à tort. La condition formelle : $\text{JSD}(f_i, f_j) \cdot \alpha < \tau$ même si $\text{JSD}(f_i, f_j \mid \text{sous-population}) \gg \tau$.

- **E5 (chaîne multi-générations) est non jugeable** si la loi plantée de certains mondes est une composition de composantes dont la détection séquentielle n'est pas monotone. Si couvrir $c_1$ d'abord rend $c_2$ plus difficile à détecter (parce que l'ajout de $c_1$ au nul absorbe une partie du signal de $c_2$ par corrélation), la chaîne peut caler sans que ce soit un échec des proposeurs ni un épuisement des composantes. A ne préenregistre aucun critère pour distinguer ce cas.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Pour D_oracle** : un monde où les composantes marquées « détectables » sont en fait non séparables (colinéaires). Si D_oracle y signale une couverture > 1, l'instrument est invalide. A ne mentionne pas ce cas.

2. **Pour E3** : un bras « même modèle, même nombre de tirages, prompts système permutés » (pas seulement des graines différentes). Sans ce bras, l'interprétation « deux fournisseurs > un fournisseur » est indiscernable de « deux prompts > un prompt ».

3. **Pour M1** : vérifier que le tirage au sort du représentant ne crée pas un biais systématique en faveur des lois courtes (qui sont plus probables sous le hasard de l'empreinte). A utilise un tirage sous graine scellée, mais ne vérifie pas la corrélation entre rang du tirage et performance au test de mort.

---

## Sur la proposition C

### (a) Défauts de méthode

**1. Le partitionnement syntaxique (M1) confond forme grammaticale et mécanisme scientifique.** C demande d'imposer 2 fiches `softmax`, 2 `si_sinon`, 2 `par_sous_population`. Mais la grammaire est **VÉRIFIÉE** dans le code ; rien n'établit que chaque forme correspond à un mécanisme distinct du monde. Un effet d'interaction $z_0 \times z_1$ peut s'exprimer aussi bien en `softmax` (avec des poids croisés) qu'en `si_sinon` (seuil sur $z_0$, coefficients conditionnels sur $z_1$). L'obligation de forme pousse à reformuler un même constat dans trois syntaxes, ce qui augmente $D_p$ et $N_{\text{eff}}$ sans augmenter la couverture oracle. C'est un cas de Goodhart par construction de l'instrument : la mesure de diversité réagit à la contrainte même qui l'a créée.

**2. Le sous-échantillonnage de l'archive (masquage de contexte) introduit une confondante entre information disponible et diversité.** Servir des sous-ensembles distincts de l'archive à deux fournisseurs rompt la symétrie d'information. Si Kimi reçoit les lois utilisant $z_1$ et Argon non, Argon est poussé vers $z_1$ par ignorance, pas par créativité. Le gain de couverture oracle serait alors un artefact de l'asymétrie d'information, non de la diversification. C ne propose aucun contrôle pour isoler cet effet (par exemple, deux bras avec la même archive complète vs deux bras avec archives disjointes, à coût apparié).

**3. Le choix du représentant par complexité minimale dans M2 est biaisé.** La règle « conserver le chef de file par nombre de paramètres non nuls croissant » favorise systématiquement les lois simples. Or, les effets d'interaction nécessitent des lois plus complexes. Si un groupe contient une loi simple captant un effet principal et une loi complexe captant le même effet principal plus une interaction, la loi complexe est éliminée. Ce biais agit contre la diversité que C cherche à promouvoir. Il est vrai par construction, pas empirique.

**4. L'expérience 1 de C ne sépare pas monde et taille d'échantillon.** C compare S-V1 (2 traits, 200 tirages) à des mondes riches (4 traits, mêmes 200 tirages). Mais un monde à 4 traits et des interactions a plus de paramètres libres ; à 200 tirages, la puissance par composante diminue mécaniquement. Si les proposeurs échouent en génération ≥ 2 sur les mondes riches, l'interprétation est ambiguë entre « effondrement modal des proposeurs » et « puissance insuffisante pour les effets secondaires ». Le seuil « promotions vraies sur au moins 5/10 mondes » ne distingue pas ces causes.

**5. L'expérience 4 (nul v9 étendu) suppose que les recombinaisons par morceaux de l'archive sont énumérables.** C propose d'inclure les « mélanges conditionnels par morceaux sur les seuils quartiles de z0, z1 ». Mais le nombre de tels mélanges croît combinatoirement avec le nombre de lois d'archive et de traits. Si le nul v9 contient des centaines de recombinaisons, les 200 tirages du juge doivent discriminer la fiche candidate de chacune. La valeur e est calculée contre le **meilleur** membre du nul (HYPOTHÈSE de A, non confirmée). Si c'est un mélange, la puissance dépend de la divergence entre la fiche candidate et la meilleure recombinaison, pas la meilleure loi simple. Un nul trop riche rend la promotion impossible pour tout effet qui est proche d'une recombinaison mais pas identique. C mentionne ce risque mais ne donne pas de critère formel pour contrôler la taille du nul v9.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **$N_{\text{eff}}$ (entropie spectrale) perd sa discrimination** quand les lois sont proches mais pas identiques. Le noyau $K_{i,j} = 1 - d_{\text{JS}}/\ln 2$ est linéaire en la JSD. Si toutes les paires ont une JSD de $0{,}05$ nat (illustratif — des variantes légèrement différentes du même constat), $K_{i,j} \approx 0{,}93$. Pour $k = 11$ lois : la valeur propre dominante sera $\lambda_1 \approx 0{,}93 + 0{,}07/11$, les autres $\lambda_i \approx 0{,}07/11 \approx 0{,}006$. L'entropie de Shannon du spectre est faible, donnant $N_{\text{eff}} \approx 1{,}5$ (illustratif). Mais pour $k = 11$ lois avec JSD de $0{,}10$ nat, $N_{\text{eff}}$ saute à $\sim 3$ (illustratif). La mesure est donc très sensible à la granularité de la JSD dans la zone $[0{,}01, 0{,}10]$ nat, exactement la zone où la distinction entre « même idée, coefficients légèrement différents » et « idée différente, même trait principal » est ambiguë. Aucun calibrage ne résout cette ambiguïté sans oracle.

- **Le partitionnement syntaxique devient non jugeable** si la grammaire ne peut exprimer certains mécanismes dans certaines formes. Si une interaction $z_0 \times z_1$ n'est pas représentable dans la forme `fixe` (bornes ±4, RAPPORTÉ), les emplacements contraints à `fixe` sont gaspillés. Le taux de fiches invalides au gardien augmente, réduisant le nombre effectif de fiches jugées.

- **L'expérience 2 est non jugeable** si le seuil $\tau_{\text{doublon}} = 0{,}01$ nat est trop strict ou trop lâche pour les mondes neufs. Le calibrage sur mondes pilotes (hors course) suppose que la distribution des JSD intra-groupe est stationnaire entre mondes pilotes et mondes de test. Si les mondes de test ont des effets de taille différente, la distribution change et le seuil est inadapté.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Pour le partitionnement syntaxique** : un bras où le même nombre de fiches est demandé sans contrainte de forme, à budget identique. C le mentionne dans l'expérience 3 (« bras témoin IID »), mais ne requiert pas explicitement que les proposeurs du bras témoin reçoivent **la même longueur de consigne** — une différence de longueur de prompt peut confondre le résultat.

2. **Pour le masquage de contexte** : un bras où les deux fournisseurs reçoivent des sous-ensembles différents mais **tirés du même ensemble** (pas des archives réduites contenant des informations complémentaires). Sans cela, on ne sépare pas l'effet de la réduction d'information de l'effet de la diversification.

3. **Pour le nul v9** : un monde où la loi plantée est exactement une recombinaison par morceaux de lois de l'archive. La fiche-oracle correspondante **doit** être refusée par le nul v9. Si elle est promue, le nul v9 est mal construit. C ne mentionne pas ce contrôle.

---

## Sur la proposition D

### (a) Défauts de méthode

**1. La mesure $D_u$ mélange performance oracle et diversité.** $D_u$ compte le nombre de groupes contenant au moins une fiche dont le gain de log-score dépasse un seuil $\delta$ au-dessus d'une bibliothèque mécanique. Cela signifie qu'une fiche peut former un groupe distinct sans être fonctionnellement différente d'une autre fiche d'un autre groupe, pourvu que les deux dépassent $\delta$. Inversement, deux fiches explorant des mécanismes réellement différents mais dont le gain est sous $\delta$ ne comptent pas. $D_u$ est donc une mesure de **couverture performante**, pas de diversité conceptuelle. Ce n'est pas un défaut en soi, mais D la présente comme « la diversité utile », sans séparer les deux dimensions.

**2. La distance $d_M$ (maximum sur la grille) est très sensible aux queues de distribution.** D propose de compléter la distance moyenne par le maximum : « Deux fiches ne sont candidates au même groupe que si les deux distances sont sous leurs seuils. » Mais $d_M$ dépend d'un seul point de la grille. Si la grille $\mathcal{X}$ contient un point aberrant (un trait extrême près de la borne ±4, RAPPORTÉ), $d_M$ peut être dominé par le comportement des lois dans une région sans données réelles, empêchant tout regroupement. D ne propose pas de critère pour écarter les points de la grille où les prédictions sont numériquement instables.

**3. E2 de D confond la consigne structurée et l'effet de la partition de recherche.** Le bras M1 de D reçoit à la fois une contrainte de partitionnement des formes **et** une exclusion de traits. Le bras témoin ne reçoit rien. Si le bras M1 gagne, on ne sait pas si c'est la contrainte de forme, l'exclusion de traits, ou leur interaction. D mentionne des « ablations » mais seulement après que H_B est falsifiée, ce qui revient à relancer des expériences après avoir vu les résultats.

**4. Le « monde de développement » pour calibrer les seuils n'est pas séparé formellement des mondes de test.** D dit « Les seuils sont calibrés sur des mondes de développement séparés, jamais sur les mondes de test », mais les 50 mondes (RAPPORTÉ, GO-2026-11-12-05) sont la seule réserve mentionnée. Si une fraction est utilisée pour le développement, la puissance des expériences décisives diminue sur les mondes restants. D ne préenregistre pas la taille de cette fraction ni le critère de partitionnement.

**5. E0 (garde réutilisable) est placée en premier mais dépend de l'extension du nul, dont les paramètres ne sont pas fixés.** D recommande l'ordre « A/A → E0 → E1 → E2 → E4 → E3 ». Mais E0 teste le « nul élargi » sans spécifier quelles recombinaisons y sont ajoutées, combien, ni comment elles sont générées. Si E0 est jouée avant que ces paramètres soient gelés, elle n'est pas reproductible.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **$D_u$ perd toute puissance** quand $\delta$ est mal calibré par rapport aux tailles d'effet du monde. Si $\delta$ est fixé sur des mondes de développement à effets forts, il sera trop haut pour les mondes de test à effets faibles, et $D_u = 0$ partout — non par manque de diversité mais par manque de puissance du seuil. Formellement : pour un effet de taille $\Delta$ nat par épisode, si $\delta > \Delta$, aucune fiche ne peut compter. Le choix de $\delta$ conditionne donc le résultat, mais D ne le lie pas à une caractéristique mesurable du monde (par exemple la détectabilité simulée).

- **Le regroupement par complete linkage avec deux seuils ($d_m$ et $d_M$) est non jugeable** quand les seuils sont en conflit. Si $\tau_m < \tau_M$ (le seuil sur la moyenne est plus strict que celui sur le max), la contrainte active est toujours $d_m$, et $d_M$ ne sert jamais. Si $\tau_m > \tau_M$, la contrainte active est toujours $d_M$, et la distance moyenne est ignorée. D ne décrit pas la relation entre les deux seuils.

- **E1 de D (monde à un effet vs multi-effets) est non jugeable** si le « gain total approximativement accessible » n'est pas défini en unités comparables. D dit « K1, le budget d'appels et le gain total approximativement accessible doivent être appariés », mais le gain total accessible est une propriété de la loi plantée que le filtre volontaire interdit de voir. L'appariement ne peut être fait qu'en simulation préalable, ce qui exige de fixer un modèle de la distribution des gains par composante — un paramètre non mentionné.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Pour $D_u$** : un ensemble de fiches dont toutes dépassent $\delta$ mais qui sont fonctionnellement identiques (même prédiction à un bruit $\varepsilon$ près). $D_u$ devrait y valoir 1 (un seul groupe). Si $D_u > 1$, le regroupement ne fait pas son travail et $D_u$ surestime la diversité. D ne mentionne pas explicitement ce cas.

2. **Pour la double distance ($d_m, d_M$)** : une paire de lois identiques partout sauf en un seul point de la grille (par construction). $d_m$ est faible, $d_M$ est élevé. Cette paire ne doit pas être fusionnée si la divergence en ce point correspond à un mécanisme réel, et doit être fusionnée si elle correspond à un artefact numérique. Sans critère pour distinguer les deux, le contrôle est absent.

3. **Pour E0** : des lois honnêtes qui sont des interactions vraies mais dont la forme grammaticale (`si_sinon`) ressemble à une recombinaison par morceaux. Le nul élargi doit les laisser passer. Si elles sont systématiquement refusées, le nul élargi est trop conservateur. D mentionne ce risque dans le tableau des instruments mais ne le formalise pas comme contrôle négatif obligatoire de E0.

---

## Sur la proposition E

### (a) Défauts de méthode

**1. La mesure de couverture privée $E_r(q)$ suppose l'identifiabilité des contrastes, sans la vérifier.** E définit un opérateur de contraste $T_r$ par mécanisme et une erreur normalisée. Mais E reconnaît elle-même : « Si deux mécanismes ne sont pas identifiables séparément, les compter ensemble ou exclure cette décomposition. » Cette clause est nécessaire mais insuffisante : l'identifiabilité dépend de la grammaire et du budget de données, pas seulement du générateur. Deux mécanismes peuvent être identifiables en population mais non séparables à 200 tirages. E ne formalise pas le critère de séparabilité empirique et renvoie à un « préenregistrement ».

**2. Le portefeuille de questions (effets principaux, interactions, hétérogénéité, réfutation) est vrai par construction.** Si le monde planté contient exactement ces quatre types de structure, et que chaque mission cible l'un d'eux, la couverture oracle est prédéterminée par la correspondance mission-mécanisme, pas par la créativité du proposeur. E reconnaît que les missions sont des « orientations, pas des quotas de vérités » et qu'une mission peut aboutir à une abstention. Mais si le monde est construit par le même programme qui construit les missions, la corrélation entre structure du monde et structure du portefeuille est parfaite. Le contrôle négatif proposé (« monde sans structure nouvelle au-delà de l'archive ») ne suffit pas : il faut aussi un monde dont la structure ne correspond à aucune mission (par exemple, un effet de seuil non monotone que ni « effets principaux » ni « interactions » ne ciblent naturellement).

**3. Le duel « rôles vs tirages supplémentaires » ne contrôle pas la longueur du prompt.** E compare « consigne structurée » à « répétitions indépendantes de la consigne générale ». Mais la consigne structurée contient des mots supplémentaires (la description de la mission). Un modèle de langage peut répondre différemment simplement parce que le prompt est plus long ou contient des concepts saillants, indépendamment de la mission. E ne mentionne pas de contrôle de longueur appariée.

**4. La « règle à diamètre borné » pour le regroupement est sous-spécifiée.** E dit « Employer une règle à diamètre borné plutôt qu'un simple chaînage de voisinages » mais ne précise pas l'algorithme. Les regroupements à diamètre borné (complete linkage, par exemple) peuvent donner des résultats très différents selon l'ordre de traitement quand des cas limites existent. E dit « Choisir le représentant par une règle déterministe indépendante des résultats, par exemple l'ordre d'une empreinte canonique » — c'est un choix valide mais le même problème que A : le représentant peut être le moins bon du groupe.

**5. La « prudence statistique » sur les valeurs e est insuffisante.** E propose de « garder les emplacements de tests prévus et donner aux fiches écartées une valeur e nulle, sans redistribuer leur budget de multiplicité ». Une valeur e nulle est correctement conservative, mais la phrase « la validité de cette modification et des valeurs e doit faire l'objet d'une contre-lecture mathématique » repousse un problème central à une étape non planifiée. Si le regroupement est déployé sans cette preuve, la garantie FDR n'est plus établie.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **La couverture $E_r(q)$ perd sa puissance** quand le contraste $T_r p^\star$ est faible. La normalisation par $\mathbb{E}\|T_r p^\star\|^2$ amplifie le bruit pour les petits effets. Un mécanisme dont le contraste vrai est de l'ordre du bruit numérique ($\|T_r p^\star\| \sim 10^{-3}$, illustratif) donnera des $E_r(q)$ très instables. Le seuil $E_r(q) \leq 0{,}5$ sera franchi ou non de manière essentiellement aléatoire. E mentionne un « seuil illustratif » et une « précision numérique préenregistrée » mais ne propose pas de critère pour exclure les mécanismes à contraste indétectable.

- **Le duel « diversification augmente-t-elle les fausses nouveautés ? » est non jugeable** si les attaques préenregistrées ne couvrent pas les recombinaisons réellement produites par les proposeurs sous pression de diversification. E liste « renommage, recombinaisons couvertes, morceaux, produits et compositions hors classe » mais ce sont des catégories, pas une liste fermée. Si les proposeurs inventent une forme d'attaque non anticipée, le duel ne la détecte pas. E le reconnaît (« Réussir ce duel établit une résistance sur le banc testé, pas une garantie hors classe ») — c'est honnête mais laisse le risque ouvert.

- **Le duel « mondes riches offrent-ils plusieurs découvertes détectables ? » est non jugeable** si les fiches sentinelles (écrites à partir de l'oracle) ne sont pas représentatives de ce que les proposeurs peuvent produire. Une fiche-sentinelle peut utiliser la forme exacte de la loi plantée, que les proposeurs ne connaissent pas. Le taux de promotion des sentinelles mesure la puissance du juge, pas l'accessibilité pour les proposeurs. E précise « détection par le pipeline de fiches sentinelles », mais le pipeline inclut le gardien et le juge, pas les proposeurs. L'expérience ne mesure donc pas ce qu'elle prétend mesurer (la récupérabilité).

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Pour le portefeuille de questions** : un monde dont la structure utile ne correspond à aucune des quatre missions. Si les rôles augmentent quand même la couverture sur ce monde, l'effet vient du simple fait de donner des instructions différentes (effet de prompt), pas de l'adéquation mission-mécanisme. E ne mentionne pas ce contrôle.

2. **Pour la mesure $E_r(q)$** : une fiche qui a un bon log-score global mais qui ne couvre aucun mécanisme (par exemple, une loi qui moyenne bien toutes les composantes sans en capturer aucune individuellement). $E_r(q)$ devrait être > 0,5 pour chaque mécanisme. Si $E_r(q) \leq 0{,}5$ pour un mécanisme que la fiche ne modélise pas, la mesure est invalide. E ne formalise pas ce contrôle.

3. **Pour le duel « regroupement économise sans effacer »** : le contrôle négatif proposé (« lois proches globalement mais divergentes sur une interaction ou une sous-population rare ») est le bon cas, mais E ne spécifie pas combien de tels cas doivent être inclus ni comment les apparier avec des paires légitimement fusionnables. Sans cet appariement, la puissance du duel est inconnue.

---

FIN-DE-CELLULE