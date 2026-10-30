## (a) Ce que la question suppose sans l’établir

- **HYPOTHÈSE** — Il existe une loi de référence \(P_{\mathcal C}\) sur les familles, distincte de leur mécanisme de découverte, sur laquelle porterait l’universalité.
- **HYPOTHÈSE** — Les familles tenues à l’écart sont transportables vers \(P_{\mathcal C}\) ; leur conception indépendante est **RAPPORTÉE**, leur représentativité ne l’est pas.
- **HYPOTHÈSE** — Les régimes aveugle et informé peuvent être réalisés sans fuite par les journaux, les interfaces ou les adaptations successives.
- **HYPOTHÈSE** — Les dépendances entre familles proches et la variance à deux niveaux admettent un modèle assez exact pour calibrer les intervalles.
- **HYPOTHÈSE** — Population fermée, indépendance des sources, capturabilité homogène et appariement exact : conditions de Lincoln-Petersen/Chapman, aucune n’est établie.
- **HYPOTHÈSE** — Les refus communs sont soit absents, soit modélisables ; une censure commune non informative n’est pas identifiable à partir des listes observées.
- **HYPOTHÈSE** — Trajectoires brutes, étiquetage, licence et mesurabilité du recouvrement des bancs publics : aucune vérification n’a été faite.
- **HYPOTHÈSE** — L’indépendance de fournisseur implique une indépendance statistique des découvertes ; elle peut être contredite par des données ou consignes communes.

## (b) Expériences décisives

### Duel 1 — Estimateur du nombre de familles

- **H_A** : sur une grille préenregistrée de mondes fermés, Lincoln-Petersen/Chapman est admissible : biais relatif absolu \(\le 5\%\) et couverture d’un intervalle nominal à 95 % d’au moins 93 % *(seuils illustratifs)*.
- **H_B** : H_A est fausse dans au moins un monde.
- **Protocole** : faire varier séparément hétérogénéité, dépendance positive/négative, faux et faux-mancqués appariements, puis calculer biais, couverture et largeur sur 2 000 répétitions par monde *(illustratif)*. Chao et un modèle multi-sources sont des comparateurs, non des conditions de H_A.
- **Contrôle négatif/base à battre** : comptage brut \(S_{\rm obs}\), présenté comme estimation ponctuelle de \(N\).
- **Issues** : une violation dans un monde falsifie H_A ; succès dans tous les mondes falsifie H_B. La conclusion reste limitée à la grille.

### Duel 2 — Définition par écart contre définition par niveau

- **H_A** : pour tout monde d’une grille finie, un écart vu–tenu-à-l’écart \(|\Delta|\le\gamma\) garantit \(q_f\le\delta\) pour toute famille.
- **H_B** : il existe un monde respectant \(|\Delta|\le\gamma\) avec \(\max_f q_f>\delta\).
- **Métrique/seuil** : énumération exhaustive de la grille ; critère \(\max_f q_f-\delta\), parmi les mondes dont l’écart est conforme.
- **Contrôle négatif** : mondes homogènes \(q_f=q\), où l’écart attendu est nul ; toute déviation systématique signale une erreur de simulation.
- **Issues** : un contre-exemple falsifie H_A ; son absence à l’énumération complète falsifie H_B **dans cette grille**.

## (c) Mesures minimales des instruments

- **Estimateur de \(N\)** : publier biais relatif, couverture unilatérale et bilatérale, largeur, taux de détection d’une sous-estimation \(N-S_{\rm obs}>\tau\), et fausses alertes lorsque \(N=S_{\rm obs}\). Les cas honnêtes sont des mondes à appariement parfait, appariés à leurs cas dépendants par \(N\), effort et capturabilité marginale. Il doit battre le comptage brut sur couverture sans élargissement illimité, et survivre à une réimplémentation indépendante.
- **Mesure d’universalité** : détection lorsque \(p_{\rm échec}>\varepsilon\), fausses alertes lorsque \(p_{\rm échec}\le\varepsilon\), couverture de la borne et taux de déclarations « universel » erronées. Viser puissance \(\ge90\%\) et fausses alertes \(\le5\%\) *(illustratif)*. Apparier les mondes sans défaillance et défaillants par nombres de familles/éléments et variance. Base : proportion brute, puis borne binomiale à horizon fixe ; vérifications mécaniques : recalcul des intervalles, graines, arrêt et dénominateurs.

# Bloc 1 — Propositions préalables

## 1(a). Définition opérationnelle

Soit \(q_f\) la probabilité d’échec d’un élément sous la loi d’éléments déclarée, \(D\) la défense figée, seuils compris, et \(U_f\) une borne supérieure de \(q_f\).

| Option | Déclaration préalable et énoncé autorisé | Ce qu’elle n’autorise pas |
|---|---|---|
| **Pire cas** | Classe \(\mathcal C\), \(\delta\), niveau simultané. Si \(\mathcal C\) est finie et entièrement mesurée : « \(\forall f\in\mathcal C,\ U_f\le\delta\) ». | Rien sur une famille hors \(\mathcal C\) ; sur une classe infinie, rien au-delà des familles mesurées sans loi d’échantillonnage. |
| **Écart vu/écart** | Ensemble vu \(S\), ensemble scellé \(T\), statistiques \(R_S,R_T\), marge \(\gamma\) : « \(R_T-R_S\le\gamma\) », avec intervalle. | Ni un niveau absolu acceptable, ni une queue de distribution, ni l’absence d’une famille catastrophique compensée par les autres. |
| **Proportion/borne de tolérance** | \(P_{\mathcal C}\), \(\varepsilon,\delta,\alpha\) : « avec confiance \(1-\alpha\), \(P_{F\sim P_{\mathcal C}}(q_F>\delta)\le\varepsilon\) ». | Aucun pire cas ; aucune validité si la découverte ne suit pas \(P_{\mathcal C}\). |
| **Quantile** | Mêmes paramètres : « \(Q_{1-\varepsilon}(q_F)\le\delta\) ». | Ne précise pas la gravité au-delà du quantile et reste instable si les familles sont dépendantes. |

Je recommande la **proportion avec borne de tolérance**, accompagnée du pire cas scellé comme résultat descriptif. Un tiers vérifie le hachage du préenregistrement, la version de \(D\), les lois et dénominateurs, les accès aux scellés, les données/codes et recalcule indépendamment les intervalles.

**Distinction décisive** : « universelle sur la classe déclarée » est un énoncé conditionnel à \(\mathcal C,P_{\mathcal C},\delta,\varepsilon\). « Robuste à l’inconnu » prétend couvrir des mécanismes hors support ou une autre loi de découverte ; cela exige des hypothèses de transportabilité supplémentaires et ne suit pas d’un bon écart vu/écart.

## 1(b). Régime d’information

- **Aveugle** : existence d’une défense et interface de mesure accessibles ; liste des familles vues, architecture, protocole détaillé et seuils internes inaccessibles.
- **Informé** : divulgation par paliers préenregistrés — objectif/protocole, puis seuils, puis artefacts de défense. La liste des familles vues peut être fournie à un palier déclaré ; les familles scellées ne le sont jamais.
- **Budgets** : nombres d’éléments, appels, calcul et arrêt maximal fixés par palier et par famille ; tout dépassement est une donnée manquante, pas une réussite.
- **Rapports** : séparés par palier, avec effectifs, effectifs de clusters, refus, estimations, intervalles et adaptations autorisées. Ne pas fusionner aveugle et informé.
- **Cloison** : construction et évaluation ne partagent ni contenus/étiquettes scellés, ni graines, ni résultats intermédiaires permettant d’ajuster \(D\). Toute exposition reclassifie la famille comme « vue » et impose un nouveau scellé.

## 1(c). Nombre de familles par simulation

Pour des familles indépendantes tirées selon \(P_{\mathcal C}\), avec succès/échec au niveau famille, utiliser une borne binomiale exacte. Avec zéro échec, les calculs **VÉRIFIÉS** donnent, à 95 % : **29 familles pour \(\varepsilon=0,10\)**, **59 pour \(0,05\)**, **149 pour \(0,02\)**. Avec des échecs, résoudre la borne supérieure exacte plutôt que réutiliser ces nombres.

Les éléments d’une famille estiment \(q_f\), mais ne remplacent pas des familles indépendantes. Simuler un modèle hiérarchique : variance entre familles, variance binomiale ou surdispersée entre éléments, et clusters de familles proches. Le nombre requis est le plus petit assurant couverture et puissance sur la grille, non une formule fondée sur un \(n_{\rm eff}\) supposé.

La règle séquentielle doit employer une dépense d’\(\alpha\) ou des intervalles valables à tout temps : succès si la borne supérieure passe sous \(\varepsilon\), non-universalité si la borne inférieure la dépasse, sinon arrêt budgétaire **non concluant**.

La simulation démontre une calibration **conditionnelle au modèle génératif**. Pour des familles découvertes, elle ne démontre ni représentativité ni couverture sur la réalité. Les analyses de sensibilité font varier découverte, dépendance, censure et contamination ; sans hypothèse de transport, l’énoncé ne vaut que pour de futures sorties du même mécanisme.

## 1(d). Familles encore inconnues

Calculs **VÉRIFIÉS** :

- \(28\times25/18=38,888\ldots\), et \(28\times25/19=36,842\ldots\) ;
- \(29\times26/19-1=38,684\ldots\), et \(29\times26/20-1=36,700\).

**\(m=18\) se défend mieux provisoirement**, car il compte des groupes appariés plutôt que deux recaptures issues d’une même famille Argon. Mais il faut alors aussi exprimer \(n_1,n_2\) dans cette unité. Avec les comptes fournis, **aucune des quatre valeurs n’est un estimateur validé** ; \(m=19\) exigerait une unité fine et un appariement bijectif reconstruit. Publier les deux conventions comme sensibilité.

Les hypothèses sont population fermée, sources indépendantes, capturabilité homogène et appariement exact. Une dépendance positive — y compris celle produite par une capturabilité facile/difficile partagée — accroît généralement le recouvrement et fait **sous-estimer** \(N\) ; une dépendance négative peut inverser le biais. Les vrais appariements manqués réduisent \(m\), donc **surestiment** \(N\) ; les faux appariements font l’inverse. Chapman ne corrige pas ces biais structurels.

Avec plusieurs sources : **Chao** fournit des estimations de type borne inférieure sous hétérogénéité ; **Good-Turing** estime masse manquante et couverture, non directement \(N\) ; les modèles log-linéaires ou à classes latentes représentent interactions et capturabilités ; une approche bayésienne propage les priors et doit inclure une sensibilité aux interactions non identifiables.

Avec deux sources et quatre comptes, l’indépendance n’est pas testable : la cellule « jamais capturée » est inobservée. Avec au moins trois sources, tester les interactions sur histoires de capture, sans confondre non-rejet et indépendance. Un refus commun est une censure strate entière : ne pas le coder comme zéro ni comme manquant au hasard ; rapporter une borne conditionnelle et des scénarios de masse censurée. Si la population n’est pas fermée, abandonner \(N\) total au profit d’un horizon daté, d’une courbe découverte–effort et de la masse nouvelle attendue.

# Bloc 2 — Données de départ recommandées

Les **trajectoires brutes publiques** sont prioritaires : elles conservent dénominateurs, éléments, données manquantes et permettent un réétiquetage audité. Je recommande d’examiner **SHADE-Arena, ControlArena et MonitoringBench**. Leur présence documentaire est **VÉRIFIÉE**, mais je ne connais ici ni leurs contenus propres, ni leurs formats, licences ou schémas d’étiquetage : ceux-ci restent à vérifier, sans attribution inventée. Leur indépendance de conception est plausible mais non établie ; le recouvrement avec l’entraînement reste **HYPOTHÈSE**. Les quasi-doublons détectables donnent au mieux une borne partielle. Ils peuvent devenir une source de capture-recapture seulement si la date, la version, le mécanisme de sélection et les identifiants stables sont conservés.

Les **journaux bruts de refus** et les **propositions brutes d’une course précédente** existent et sont lisibles (**RAPPORTÉ**) ; leurs dossiers ne sont pas transmis ici, donc je n’en infère ni format ni contenu. Les refus documentent surtout une censure commune et ne doivent pas être transformés en liste représentative. Les propositions anciennes sont peu indépendantes du programme et servent mieux au contrôle d’appariement qu’à une validation extérieure.

Coût commun : inventaire/licence, conversion sans perte, étiquetage familial par plusieurs lecteurs et journal des exclusions. Les listes dérivées des mêmes sources ne comptent pas comme captures indépendantes.

# Bloc 3 — Questions candidates

1. **« Comment borner à confiance \(1-\alpha\) la proportion de familles où \(q_f>\delta\), avec variance à deux niveaux et arrêt séquentiel ? »**  
   **Avantage** : énoncé directement réfutable et recalculable. **Piège** : pseudo-réplication des éléments et découverte non aléatoire. **Validation** : 29 familles extérieures toutes réussies bornent \(\varepsilon=0,10\) à 95 % seulement sous tirage indépendant ; 50 éléments par famille *(illustratif)*, avec prédiction scellée. **Risque hors périmètre : faible** *(illustratif)*, car seuls estimateurs et plans sont décrits.

2. **« Quel estimateur multi-sources borne le mieux la masse de familles inconnues sous dépendance et erreur d’appariement ? »**  
   **Avantage** : exploite les cinq instances prévues sans supposer leur indépendance. **Piège** : cellule zéro inobservable et faux appariements. **Validation** : geler intervalles et masse manquante, puis confronter à une sixième source d’au moins 20 familles *(illustratif)* ; erreur de masse nouvelle inférieure à 10 points *(illustratif)*. **Risque : faible** *(illustratif)* ; la question porte sur les histoires de capture.

3. **« Comment mesurer l’effet causal du régime d’information sur l’estimation d’universalité, à budget et familles appariés ? »**  
   **Avantage** : exploite les deux versions aveugle/informée déjà décidées (**VÉRIFIÉ**). **Piège** : adaptation après résultats intermédiaires ou fuite des scellés. **Validation** : 10 familles extérieures appariées entre régimes *(illustratif)*, budgets identiques, marge d’équivalence \(\gamma\) et classement des régimes scellés avant mesure. **Risque : moyen** *(illustratif)* si les artefacts de défense envahissent la question ; la borner aux informations accessibles et aux performances agrégées.

4. **« Quelle règle séquentielle maintient sa couverture sous familles corrélées et budgets plafonnés ? »**  
   **Avantage** : réduit le calcul sans arrêt optionnel silencieux. **Piège** : calibration uniquement sous indépendance ou arrêt maximal présenté comme succès. **Validation** : code et décisions gelés, puis rejeu sur 12 familles extérieures *(illustratif)* ; sur 2 000 mondes simulés *(illustratif)*, aucune couverture sous le seuil préenregistré. **Risque : faible** *(illustratif)*, limité aux lois, arrêts et intervalles.

# Bloc 4 — Organisation des instances indépendantes

La décision de cinq instances est **RAPPORTÉE** ; toutes les modalités suivantes sont **HYPOTHÈSE**.

- **Consignes** — *Options* : identiques, ou différentes. Identiques améliorent la comparabilité mais partagent les angles morts ; différentes diversifient les lois de capture mais compliquent l’estimation. **Recommandation** : même noyau limité au format, aux métadonnées, au budget et aux interdictions de fuite, sans exemples ni contenu ; variations enregistrées comme covariables. **Confiance : élevée.**
- **Fuites** — *Options* : simple séparation logique, ou isolation administrative et cryptographique. La première est peu coûteuse mais fragile ; la seconde alourdit la coordination. **Recommandation** : contextes neufs, dépôts et identifiants séparés, aucun partage de sorties, chiffrement et dépôt chez un tiers, engagements par hachage et journaux d’accès. **Confiance : élevée**, sans garantie contre les données d’entraînement communes.
- **Appariement** — *Options* : lecteur unique, correspondance mécanique seule, ou lecteurs multiples. Le premier reproduit le biais documenté ; la seconde manque les regroupements un-à-plusieurs. **Recommandation** : trois lecteurs aveugles de lignées distinctes *(illustratif)*, appariements un-à-plusieurs autorisés, désaccords arbitrés sans révéler la provenance ; publier accord, désaccords et résultats sous tous les appariements plausibles. **Confiance : élevée.**
- **Indépendance** — *Options* : attestations de fournisseurs, recouvrement de corpus documentés, tests sur histoires de capture. Aucun ne prouve seul l’indépendance des entraînements. **Recommandation** : ne pas déduire l’indépendance de la marque ; tester les interactions multi-sources et conduire une sensibilité à la dépendance résiduelle. La corrélation des données d’entraînement est inconnue ici. **Confiance : moyenne.**
- **Estimation multi-sources** — *Options* : Chapman répété par paires, Chao/Good-Turing, modèles log-linéaires/classes latentes ou bayésiens. Les paires ignorent les interactions ; les modèles riches sont moins stables. **Recommandation** : histoires communes, Good-Turing pour la masse nouvelle, Chao comme repère bas et plusieurs modèles multi-sources avec intervalles de sensibilité ; ne pas promettre un \(N\) exact. **Confiance : moyenne.**
- **Refus** — *Options* : imputer, remplacer silencieusement, ou enregistrer la censure. Les deux premiers fabriquent de l’information. **Recommandation** : conserver le refus tel quel, sans reformulation dans le run ; analyser les sources restantes et des scénarios de censure non aléatoire. Toute nouvelle instance constitue un run séparé. Le repli à au plus trois questions plus étroites est **VÉRIFIÉ** dans les faits v1, non relus en v2. **Confiance : élevée.**

## (d) Ancrage matériel

Modèles ouverts de 8 et 70 milliards de paramètres : **RAPPORTÉ**. Les simulations, appariements et intervalles tiennent sur CPU ; l’inférence des modèles est un poste distinct. **Illustratif** : 2 000 répétitions par monde sur une station CPU multi-cœurs ; stockage inférieur à 1 To ; mesures sur GPU réservées après un pilote. Budget préliminaire de 1 000 à 5 000 €, à recalculer en GPU·h mesurés multipliés par le tarif réel, sans déduire ce coût des seules tailles de modèles.

FIN-DE-CELLULE