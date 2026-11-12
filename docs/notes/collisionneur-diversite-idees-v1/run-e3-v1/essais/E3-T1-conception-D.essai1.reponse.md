## (a) Ce que la question suppose sans que ce soit établi

Sauf rappel explicitement **RAPPORTÉ**, tous les seuils et dimensionnements chiffrés ci-dessous sont **illustratifs**, à fixer sur un pilote puis à sceller.

| Supposition | Statut et conséquence |
|---|---|
| La consigne commune, la vue commune ou l’appel unique ont causé la similarité des onze fiches. | **HYPOTHÈSE.** La proximité des onze lois est **RAPPORTÉE**, mais aucun facteur n’a été manipulé. Le monde, les modèles, l’archive et l’échantillonnage des réponses sont confondus. |
| S-V1 ne laissait qu’un constat fort accessible. | **HYPOTHÈSE**, explicitement formulée comme point ouvert dans les faits. Elle est plausible, non mesurée. |
| La course v67 a mesuré une faible diversité. | **RAPPORTÉ** qualitativement : « ce ne sont pas 11 idées ». Aucun taux, distance ou nombre de classes n’a été préenregistré ; la diversité retenue reste donc non quantifiée. |
| Les douze refus de génération 2 révèlent une incapacité à diversifier ou à progresser. | **HYPOTHÈSE non établie.** Le verdict **RAPPORTÉ** dit précisément que ces refus ne renseignent pas sur cette capacité. |
| Un monde plus riche produira davantage d’idées utiles distinctes, plutôt que davantage de variantes du premier effet facile. | **HYPOTHÈSE.** Il faut séparer richesse, difficulté et gain total disponible. |
| Consignes, rôles ou récompense de nouveauté augmenteront la diversité utile sans augmenter les copies hors classe. | **HYPOTHÈSE.** Au contraire, une brèche hors classe du nul est **RAPPORTÉE** ; modifier l’incitation sans réauditer le juge peut aggraver le risque. |
| Deux lois proches syntaxiquement ou en prédictions sont interchangeables pour la promotion. | **HYPOTHÈSE.** Une petite différence sur une sous-population peut porter tout le gain ; une distance comportementale n’est pas une preuve d’équivalence. |
| L’isolement des proposeurs et l’absence de fuite sont suffisamment établis pour attribuer un effet aux contextes. | Non établi. La recherche de fuite et son classement en coïncidence sont **RAPPORTÉS** ; l’absence des réponses brutes et des témoins d’isolement est également **RAPPORTÉE** (R-2). |
| Une mesure de contenu sera un bon substitut de « diversité des idées ». | **HYPOTHÈSE.** Elle peut mesurer la diversité comportementale des fiches, jamais à elle seule leur originalité intellectuelle ou leur utilité. |

## Instrument commun : définir la diversité sans la confondre avec le succès

Je propose une mesure déterministe, sans modèle juge, scellée avant les réponses.

1. **Canonisation mécanique** : normalisation de la fiche et de sa loi, renommage des variables, formatage des constantes. Les copies exactes canonisées sont groupées d’office.
2. **Grille de sondes publique** \(\mathcal X\) : points de traits et sous-populations couvrant le domaine public, sans issues ni paramètres plantés. Pour chaque loi \(f\), calculer \(q_f(y\mid x)\).
3. **Distance prédictive** :
   \[
   d_m(f,g)=\operatorname{moyenne}_{x\in\mathcal X}
   \frac12\sum_y|q_f(y\mid x)-q_g(y\mid x)|,
   \]
   complétée par \(d_M\), le maximum sur \(\mathcal X\). Deux fiches ne sont candidates au même groupe que si les deux distances sont sous leurs seuils. Le maximum évite de fusionner deux lois identiques presque partout mais différentes sur une région décisive.
4. **Regroupement déterministe** : *complete linkage*, ordre des ex æquo fixé par empreinte canonique. Les seuils sont calibrés sur des mondes de développement séparés, jamais sur les mondes de test.
5. **Trois sorties distinctes** :
   - \(D_p\) : nombre de groupes parmi les fiches valides, diagnostic seulement ;
   - \(D_n\) : nombre de groupes non doublons de l’archive, diagnostic de nouveauté ;
   - \(D_u\) : nombre de groupes contenant au moins une fiche dont le gain de log-score, calculé hors ligne avec l’**oracle**, dépasse un seuil \(\delta\) au-dessus d’une bibliothèque mécanique scellée composée de l’archive et de baselines simples.

\(D_u\) sert à comparer des compositions ou des contextes, conformément à N-058 ; **il ne sert ni à promouvoir une fiche ni à récompenser un agent pendant la course**. Une fiche différente mais inutile n’augmente pas \(D_u\). La couverture des formes, traits, interactions et sous-populations reste un vecteur descriptif séparé : l’additionner à \(D_u\) créerait une cible Goodhart supplémentaire.

## Mécanismes concrets et garde-fous

### 1. D’abord rendre plusieurs découvertes possibles

Construire des paires de mondes de difficulté calibrée : dans l’un, le gain disponible est concentré dans un effet ; dans l’autre, il est réparti entre plusieurs traits, interactions et effets de sous-population, avec des amplitudes variées. K1, le budget d’appels et le gain total approximativement accessible doivent être appariés, sinon « monde riche » signifie seulement « monde plus facile ».

Les mondes sont répartis avant usage en développement, calibration et test final. Les métadonnées du générateur, tailles d’effet et noms de cibles ne entrent jamais dans les vues. La puissance aux tailles d’échantillon du juge et du test de mort doit être simulée : un effet réel mais indétectable ne constitue pas une opportunité expérimentale équitable.

### 2. Consigne, rôles et contextes : même information, recherches différentes

Tous reçoivent le même paquet obligatoire : description publique, grammaire et archive complète. Seule une carte de recherche diffère :

- consigne neutre de contrôle, de longueur comparable ;
- consigne demandant des hypothèses réellement différentes, chaque énoncé indiquant quelle prédiction la distingue de l’archive ;
- rôles disjoints : effets simples, interactions/seuils, sous-populations/mélanges, avec une part de fiches libres ;
- contextes structurés : couverture mécanique des traits et formes déjà présents dans l’archive, **sans verdict, résidu, performance ni information oracle**.

Les rôles tournent entre modèles, mondes et graines. Une consigne de nouveauté ne doit pas suggérer que contourner le nul est un succès.

### 3. Regrouper avant de juger, sans assimiler groupe et équivalence

Après canonisation et regroupement, un seul représentant par groupe, choisi avant les données par règle déterministe, entre dans le juge. Les autres fiches ne sont **ni promues ni déclarées survivantes par association**. Le nombre de tests et la procédure de multiplicité sont figés sur cet ensemble de représentants.

Si le représentant échoue, aucun membre n’est promu dans cette génération. Si elle réussit, elle doit encore passer le test de mort. Cette règle peut perdre le meilleur membre d’un groupe : c’est précisément ce que l’expérience E4 doit mesurer.

### 4. Récompense de nouveauté : dernier mécanisme à tester

Commencer par une variante de consigne, sans bonus promotionnel. Une récompense effective éventuelle ne peut porter que sur une évaluation oracle-et-coût autorisée de la composition, jamais sur une valeur e, une promotion ou un verdict. Elle ne modifie ni le seuil du juge, ni le nul, ni le test de mort.

Avant tout essai avec récompense, le juge doit passer un audit sur les recombinaisons par morceaux, produits et compositions. À défaut, l’expérience testerait surtout la capacité de l’incitation à exploiter une brèche **RAPPORTÉE**.

## (b) Expériences à duel tranchant

Un pilote A/A précède chaque comparaison : mêmes mondes, mêmes cartes, appels indépendants. Il estime la variance et vérifie qu’un contraste fictif ne produit pas l’effet attendu. Réponses brutes, contextes exacts, coûts, graines et témoins d’isolement sont versés avant lecture. Chaque comparaison est appariée par monde, archive, modèle et coût ; le témoin est le meilleur des contrôles mécaniques à budget égal, notamment plusieurs tirages indépendants du même modèle.

| Expérience | Duel exclusif et critère | Contrôle négatif | Lecture des deux issues |
|---|---|---|---|
| **E1 — Le monde suffit-il ?** Consigne neutre, mondes à un effet contre mondes multi-effets appariés. | **H_A** : la répartition multi-effets augmente \(D_u\) d’au moins **1 groupe par génération, illustratif**. **H_B** : augmentation inférieure à ce seuil. | Monde témoin où les traits sont seulement renommés ; répétitions A/A ; propositions grammaticales aléatoires à nombre de fiches égal. | Au-dessus du seuil : H_B est falsifiée, la pauvreté des opportunités contribue. En dessous : H_A est falsifiée ; augmenter la richesse seule n’est pas justifié. |
| **E2 — Le paquet structuré ajoute-t-il quelque chose ?** Consigne + rôles tournants + contextes mécaniques contre consigne neutre de même longueur, sur mondes riches. | **H_A** : gain d’au moins **1 groupe \(D_u\), illustratif**, au-delà du meilleur contrôle à coût égal. **H_B** : gain inférieur, y compris si seul \(D_p\) ou \(D_n\) augmente. | Cartes *placebo* sans partition de recherche ; même modèle en tirages répétés ; archive seule sans carte. | Gain utile : H_B falsifiée ; passer ensuite aux ablations. Variantes, fiches invalides ou jargon supplémentaires sans gain \(D_u\) : H_A falsifiée. |
| **E3 — La récompense de nouveauté est-elle utile et sûre ?** Même paquet E2, avec ou sans phrase de récompense. | **H_A** : gain \(D_u\) au seuil d’E2 **et** aucun dépassement des limites de sécurité d’E0. **H_B** : négation de cette conjonction. | Copies hors classe plantées hors vue des proposeurs ; variantes aléatoires éloignées en prédictions mais sans gain oracle. | Gain utile avec garde validée : H_B falsifiée. Gain seulement apparent, hausse des copies ou dégradation du juge : H_A falsifiée. |
| **E4 — Le regroupement économise-t-il sans perdre les idées ?** Juger toutes les fiches contre un représentant par groupe, sur les mêmes ensembles de réponses. | **H_A** : au moins **30 % de fiches jugées en moins, illustratif**, conservation d’au moins **90 % des groupes \(D_u\), illustratif**, sans hausse des fausses promotions. **H_B** : au moins une condition échoue. | Copies renommées ; paires honnêtes très proches mais complémentaires sur une région ; paires réellement distantes. | Économie et conservation : H_B falsifiée. Fusion d’idées utiles, économie insuffisante ou perte de puissance : H_A falsifiée. |
| **E0 — La garde est-elle réutilisable sous les nouvelles incitations ?** Nul élargi et contrôles mécaniques contre dispositif actuel. | **H_A** : détection des copies plantées ≥ **95 %, illustratif**, taux de fausses promotions ≤ **5 %, illustratif**, perte de détection des ajouts indépendants ≤ **10 %, illustratif**. **H_B** : au moins un critère n’est pas atteint. | A/A en resoumettant l’archive ; copies couvertes et hors classe ; lois honnêtes sans gain ; ajouts réellement indépendants. | Tous critères atteints avec bornes de confiance prévues : H_B falsifiée. Un échec : H_A falsifiée ; aucune course incitative ne doit être interprétée comme sûre. |

Un intervalle trop large pour trancher ne devient pas une preuve pour H_B : il falsifie seulement l’hypothèse auxiliaire que le dimensionnement était décisif, et impose de reprendre le pilote.

## (c) Mesure minimale de chaque instrument

Les cas appariés communs sont : **U**, ajout honnête avec gain oracle ; **F**, ajout honnête faible ; **N**, syntaxe nouvelle sans gain ; **R**, reformulation indépendante d’une même idée ; **C**, copie couverte ou hors classe. Les mondes et les difficultés sont appariés.

| Instrument | Détection minimale | Fausses alertes à mesurer | Vérifications mécaniques à battre |
|---|---|---|---|
| **Consigne de diversité** | Fraction des paires où elle retrouve un groupe U absent du contrôle neutre. | Hausse de \(D_p\) sur N/R, fiches invalides, baisse du gain total. | Consigne neutre de même longueur ; tirages répétés ; variantes aléatoires à budget égal. |
| **Rôles** | Détection des cibles assignées et des cibles libres, agrégée après rotation des modèles. | Disparition d’idées hors rôle, rôles produisant seulement des formes différentes sans gain. | Attribution aléatoire des cartes ; cartes placebo ; partition par seul comptage de traits/formes. |
| **Contextes servis** | Gain obtenu à information publique strictement identique. | Différence explicable par une fuite, une longueur de contexte ou une archive incomplète. | Contexte remanié sans information nouvelle ; empreintes et comparaison mécanique des paquets ; recherche de chaînes sensibles. |
| **Regroupement des doublons** | Taux de R/C regroupés, y compris copies comportementales. | Taux de paires U/F distinctes fusionnées ; perte du meilleur représentant. | Hachage canonique seul ; distance moyenne seule ; distance maximale seule. Le dispositif doit améliorer le compromis détection/fausses fusions, pas seulement un taux brut. |
| **Récompense de nouveauté** | Nouveaux groupes U à coût constant. | N éloigné mais inutile, C hors classe, optimisation du seul seuil de distance. | Même consigne sans récompense ; bruit grammatical aléatoire ; meilleur de plusieurs tirages à coût égal. |
| **Monde riche** | Nombre d’effets plantés indépendants effectivement récupérables. | Effet attribué à tort à la richesse alors que le gain total ou la difficulté diffère ; fuite par artefacts du générateur. | Monde à un effet apparié ; traits permutés ; propositions aléatoires ; plusieurs graines de génération. |
| **Mesure de diversité** | Séparation de U réellement distincts et regroupement de R. | N compté comme utile, copies à paramètres déplacées, U rare fusionné. | Comptage des formes/traits, canonisation seule, distance prédictive sans contrôle oracle. |
| **Juge et test de mort** | Ajouts U/F détectés et survivants ; copies C refusées. | Promotion ou survie de N/C ; mort systématique des effets F. | Resoumission A/A de l’archive, bibliothèque de copies mécaniques et baseline de log-score. Les contrôles complètent le juge, sans le remplacer. |

## Risques à préenregistrer

- **Goodhart** : maximiser \(D_p\) avec des lois absurdes ; riposte primaire : \(D_u\), taux de validité et gain total rapportés ensemble.
- **Fuite** : cartes dérivées de l’oracle ou générateur reconnaissable ; riposte : contextes exclusivement publics, mondes séparés et réponses brutes conservées.
- **Perte de puissance** : effets faibles noyés dans un monde riche, mauvais représentant de groupe, nul élargi plus conservateur ; mesurer séparément puissance, coût et fausses promotions.
- **Fausse sécurité** : la distance sur sondes ne prouve ni l’équivalence ni l’absence de copie ; elle ne doit jamais dispenser du juge ou du test de mort.

## (d) Ancrage matériel

Pour un harnais local reproductible, sans présumer qu’il remplace Kimi ou Argon : **Qwen2.5-14B-Instruct** et **Qwen2.5-32B-Instruct**, poids téléchargeables, versions et quantification figées. La sortie reste soumise au gardien grammatical.

- **14B quantifié en 4 bits, illustratif** : environ 10–12 Go de poids, davantage avec le cache ; un GPU de 24 Go est un point de départ.
- **32B quantifié en 4 bits, illustratif** : environ 20–24 Go de poids ; viser un GPU de 48 Go ou deux GPU de 24 Go pour garder une marge de contexte.
- **Maquette illustrative** : 192 appels, au plus six fiches par appel, suivis de rejouages statistiques sur CPU ; environ 20–60 heures-GPU et 10–50 heures-CPU selon longueur des contextes et débit.
- **Coût illustratif** : 50–250 USD de location GPU/CPU et stockage, hors ingénierie humaine et génération des mondes. Le coût v67 — **1,99 USD modèles et environ 0,27 USD machine, RAPPORTÉ** — ne permet pas d’extrapoler ce devis.

L’ordre de dépense recommandé est donc : A/A et bibliothèque de cas, audit E0, mondes appariés E1, paquet structuré E2, regroupement E4, puis seulement récompense E3. Une amélioration de \(D_p\) seule ne justifie aucune adoption.

FIN-DE-CELLULE