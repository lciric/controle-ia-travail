# Proposition D — Tour III.3 : réponse aux critiques

**Statuts.** Les éléments du dossier restent **RAPPORTÉS** ; ses calculs et vérifications sans artefacts restent **OBSERVÉS-NON-AUDITÉS**. Les objections empiriques et les protocoles ci-dessous sont des **HYPOTHÈSES** de méthode. Je réserve **VÉRIFIÉ** aux constats textuels ou algébriques limités que je reformule ici : aucune performance d’instrument n’est établie. Les confiances sont des jugements **illustratifs**.

## (a) Sort des critiques visant D

### Critiques d’A

**Acceptées.** Ma définition \(A=p_{\mathrm{acc}}\) n’était pas justifiée par le libellé ambigu « accepte (ne signale pas) » et confondait possiblement abstention et signalement. E1 décidait effectivement de son issue par le dosage arbitraire des perturbations de verdicts et ne mesurait pas le contraste témoin/référence réel. En D2, maximiser la détection sous plafond de fausses alertes se réduit, à famille de seuils ordonnés, à choisir le plus petit seuil admissible ; utiliser les dommages pour ce choix adapte en outre « reconnu » au tiers. J’accepte aussi : l’auto-certification possible du contrôle négatif d’E3, le trou logique d’E5, le caractère imbattable et informationnellement inéquitable de la référence cachée, l’absence de niveau alloué pour « propager » l’erreur résiduelle, ainsi que les deux objections de puissance — rappel extrême exigeant de très nombreux positifs sans erreur, et impossibilité possible de détecter un retrait unitaire lorsque le seuil doit passer à deux contrôles.

**Transformées en tests.** Les négatifs annotés indépendamment avec leurres lexicaux, le contraste témoin/référence sans perturbation et l’édition factice entrent dans E1′–E3′. Le croisement information/composition est conservé dans E5′.

### Critiques de B

**Acceptées.** Deux défaillances distinctes peuvent produire la même chute de \(A\) ; E1 ne doit donc pas injecter de verdicts. La liste des candidates d’E4a doit être finie et gelée, avec correction de leur sélection. L’E5 initial laissait une issue sans verdict. Les effectifs d’E2 et E3 seront calculés strate par strate, non justifiés par un total global.

J’accepte particulièrement **T2** : sous des Bernoulli indépendants, retrouver la couverture d’une borne binomiale n’éprouve presque rien. E4′ comprendra dépendances, grappes, déclencheur calculé sur les mêmes lectures et oracles dégénérés ; il mesurera aussi l’utilité, puisqu’une borne constante peut couvrir parfaitement sans informer. Le bras où seule l’abstention change devient un test unitaire du comptage, non une preuve sur les mondes. E5′ comportera le croisement complet et un régime où top-\(K\) n’est pas presque toujours la fiche honnête.

### Critiques de C

**Acceptées avec une réserve textuelle.** L’objection algébrique sur \(A\) est fondée ; en revanche, je ne retiens pas comme établie une lecture unique du dossier : son libellé doit être tranché par l’organisateur et confronté au code avant gel. J’accepte la fuite des dommages dans l’étalonnage et l’inversion entrée/sortie d’E1 : acceptation et abstention sont des sorties du moniteur, non des paramètres qu’on peut perturber pour apprendre quoi que ce soit sur sa réponse aux tâches.

Les calculs de puissance sont retenus comme **conditions à vérifier**, non comme mesures du banc : petite strate potentiellement incapable de valider même une détection parfaite, minimum sur plusieurs strates défavorable, et absence de lien simple entre rappel, taux brut de fausses désignations et valeur prédictive positive à faible prévalence.

**Transformées en tests.** Le contrôle d’homogénéité étalonnage/validation devient une porte gelée, stratifiée par \(m\). La vérification de l’effacement effectif est conservée, mais pas confiée au seul oracle : une adjudication étrangère à celui-ci devra distinguer retrait réel, redondance ailleurs dans le document et erreur de lecture.

### Critiques d’E

**Acceptées.** Une perturbation programmée des verdicts ne valide pas leur réponse aux tâches. La validation réservée ne servira qu’à évaluer des règles déjà gelées, jamais à choisir la famille de dommages. L’arbitrage des seuls désaccords laisse échapper \(P(L=R\neq Y)\) : des accords seront donc audités aléatoirement. La référence cachée est retirée des concurrents à battre.

J’intègre également : le test de faisabilité du meilleur seuil possible ; la non-utilité d’une couverture triviale ; la couverture conditionnelle indéfinie lorsque l’excès a probabilité nulle ; le risque maximal hors scénarios ; et l’impossibilité de détecter un sabotage si preuves et fiches ont même loi avec et sans dommage. Les contrôles demandés — honnêtes non perturbés, retouches bénignes du tiers, accords audités, cas d’optimisation infaisable et vérificateur sans référence cachée — sont ajoutés.

### Critiques de F

**Acceptées.** Je retire le réglage maximin sur dommages, la comparaison inégale à la référence cachée et le contrôle d’E3 qui confondait localiser un contrôle présent avec constater son retrait. La non-identifiabilité de \(p_{\mathrm{sig}}\) sous ma seule statistique \(A=p_{\mathrm{acc}}\), la dégénérescence possible du maximin et la multiplicité des candidates d’E4a sont prises en compte.

L’édition stylistique neutre réalisée par le tiers et les passages non porteurs reprenant les mots-clés deviennent obligatoires. Ils testeront respectivement la cicatrice d’édition et la fausse localisation, deux événements distincts.

### Critiques de G

**Acceptées.** Outre les défauts déjà concédés sur D1/D2, j’accepte que le pas entier de seuil ne soit utilisable qu’après définition de l’agrégation des lecteurs. Le partage d’un modèle entre agent et repéreur n’est pas une fuite **VÉRIFIÉE**, mais un risque **HYPOTHÉTIQUE** suffisamment sérieux pour imposer des rôles disjoints et une adjudication indépendante.

E4b utilisera des scénarios non nuls, avec \(q\in]0,1[\), dose positive et corrélation entre lectures honnêtes et sabotées. E5 ne se limitera plus à \(K=0\) : il comprendra des honnêtes sur \(K>0\), des fiches honnêtes imparfaites et des sabotages grossièrement incohérents. Les objections de puissance, d’erreur d’annotation et de rareté des top-\(K\) réellement fautifs sont acceptées. Les comparaisons appariées utiliseront graines communes et nombres aléatoires communs.

### Critiques de H

**Acceptées.** Le mécanisme de perturbation d’E1 était indéfini et confondait modification de l’instrument, des tâches et du monde. E3 doit rester cohérent lorsque les deux instruments échouent : cette issue falsifiera l’admissibilité du programme, sans valider l’hybride. Toute règle de bascule apprise sur le développement sera figée avant validation.

Les seuils ne seront plus présupposés atteignables ; la puissance sera démontrée avant lecture, y compris pour E5. E4b emploiera les mêmes graines entre procédures comparées. La corrélation inter-lecteurs et les grappes par document entrent dans tous les duels concernés.

### Critiques d’I

**Acceptées.** Le « cahier des charges » d’E1 n’existait pas dans le dossier et le moniteur n’est pas librement réglable. E4a n’était pas falsifiable avec un ensemble ouvert de candidates. Comparer des agents réels informés ou non de \(K\) avant la décision servirait des fiches trop tôt : E5′ n’utilisera que des scripts avant admission. Le journal de B ne sera pas présenté comme un second résultat ; je rejette seulement l’assimilation complète à l’option (c), car des diagnostics bruts sans rôle d’admission ne constituent pas un second critère.

J’accepte enfin : aucun verdict de puissance ne doit faire passer automatiquement pour préférable l’absence de règle ; la propagation de l’erreur de désignation peut être non identifiable en excès ; l’indépendance simulée rend E4b nominal par construction. Relectures par panels disjoints, épisodes \(K=0\) et leurres lexicaux sont ajoutés.

## (b) Expériences corrigées

**Dispositions communes.** Sont gelés avant lecture : estimands, strates, candidates, règles d’intervalle, partage du niveau, effectifs calculés par puissance, graines et critères d’utilité. Développement, étalonnage, validation et lot final sont disjoints ; le final n’est lu qu’une fois. Un résultat encore non tranchant après l’effectif maximal gelé est un échec de puissance du protocole et bloque l’admission, non une preuve scientifique favorable.

### E1′ — Témoin réel, sans verdicts injectés

- **Données.** Tâches honnêtes réelles appariées, incluant le contraste témoin/référence non perturbé et plusieurs contrastes de lois de tâches gelés. Aucun paramètre de sortie du moniteur n’est manipulé. A et B sont estimés sur les mêmes épisodes pour le duel ; les trois verdicts restent séparés.
- **\(H_A\).** La règle d’admission fondée sur A atteint les critères gelés de détection des instabilités et de fausses alertes, et B n’apporte pas de gain décisionnel supérieur à la marge gelée.
- **\(H_B\).** A échoue, ou A+B apporte un gain supérieur à cette marge.
- **Issues.** La première falsifie la nécessité de B ; la seconde falsifie la suffisance de A.
- **Contrôles.** Coupe aléatoire du monde de référence à effectifs et appariement identiques ; estimation des variances sur grappes ; test unitaire séparé où seule l’abstention change, sans valeur probante sur les mondes.

### E2′ — Faisabilité du signalement, avant tout q

- **Loi nulle.** Paires appariées de même provenance que le final : document honnête contre retouche sans perte effectuée par le même tiers, avec panels de lecteurs disjoints. Les relectures simples et les productions honnêtes indépendantes sont rapportées séparément, jamais mélangées à cette loi nulle.
- **Étalonnage sans dommages.** Pour chaque \(m\), le seuil retenu est le plus petit dont la borne supérieure de fausse alerte respecte le plafond. Les dommages ne servent pas à choisir le seuil.
- **Validation indépendante.** Nouvelles paires nulles et dommages certifiés par adjudication étrangère à l’oracle, sans filtrage sur leur visibilité. Homogénéité étalonnage/validation et puissance sont exigées par strate.
- **Question 1.** \(H_A\) : la règle fixe \(1/m\) satisfait simultanément fausse alerte et détection minimale ; \(H_B\) : elle échoue sur au moins un critère. La première issue falsifie la nécessité d’un étalonnage, la seconde falsifie la suffisance du seuil fixe.
- **Question 2.** \(H_A'\) : au moins une candidate gelée satisfait tous les critères ; \(H_B'\) : aucune ne les satisfait. La première issue falsifie l’infaisabilité de la famille ; la seconde falsifie son admissibilité et interdit d’invoquer un défaut de puissance comme preuve de détection.

### E3′ — Désignation, retrait et erreurs communes

- **Vérité de travail.** Double annotation indépendante en aveugle, avec mesure de ses désaccords ; échantillon stratifié parmi désignés et non-désignés, accords comme désaccords. Sont inclus paraphrases, contrôles implicites, négations, leurres intra-document et contrôles redondants.
- **Comparaison.** Programme et hybride sont gelés après développement ; les mêmes contrôles cibles sont retirés dans les branches comparées. La précision de localisation, le rappel pondéré par prévalence et la persistance après retrait sont estimés séparément, avec grappes par document.
- **\(H_A\).** Le programme atteint le plancher de viabilité et l’hybride n’apporte qu’un gain inférieur à la marge gelée.
- **\(H_B\).** Le programme échoue au plancher, ou l’hybride apporte un gain supérieur.
- **Issues.** Succès : la nécessité de l’hybride est falsifiée. Échec : la suffisance du programme est falsifiée ; si l’hybride échoue aussi, aucun désignateur n’est admis.
- **Garantie.** Aucune correction de \(q\) n’est ajoutée après coup. Une propagation ne serait recevable que dans une campagne future avec budget d’erreur préalloué et estimand identifiable.

### E4a′ — Excès : couverture et utilité

Une liste finie de candidates est gelée. Les scénarios comprennent doses positives, \(q\) non triviaux, lectures partagées, grappes, dépendance du déclencheur, oracles dégénérés et points hors grille. Une borne constante maximale échoue au critère d’utilité.

- **\(H_A\)** : au moins une candidate nommée conserve la couverture familiale et fournit une lecture non triviale sur toute la famille gelée.
- **\(H_B\)** : aucune ne satisfait les deux conditions.
- Chaque issue falsifie l’autre, mais seulement pour cette famille ; l’optimiseur doit aussi refuser un cas infaisable. Aucun succès ne modifierait rétroactivement la campagne courante.

### E4b′ — Réallocation conditionnelle

Niveaux fixes et réallocation sont comparés sur les mêmes scénarios et nombres aléatoires, avec un ou deux regards, dépendance entre excès et erreurs de borne, et recherche du maximum hors grille avec incertitude Monte-Carlo.

- **\(H_A\)** : la réallocation respecte le budget global et améliore l’utilité.
- **\(H_B\)** : elle dépasse le budget ou n’apporte pas l’utilité revendiquée.
- Le contrôle sans réallocation doit retrouver son niveau ; un succès d’E4b′ n’autoriserait qu’une règle future prégelée.

### E5′ — Composition, information et vraies erreurs

Avant décision, seuls des scripts tournent. Le plan croise composition fixe/tirée et \(K\) révélé/caché, avec le bras « tirée mais révélé ». À graines appariées, on compare honnête imparfait, top-\(K\), prédicteur modal, estimateur adaptatif \(\hat K(X)\), prédicteur par format seul et saboteur grossièrement incohérent. Les fiches top-\(K\) correctes ne comptent pas comme sabotages ; des substitutions forcées fournissent des erreurs positives sans contaminer cette distinction.

- **Premier duel.** \(H_A\) : la configuration fixe connue satisfait détection des fiches réellement erronées et acceptation des honnêtes ; \(H_B\) : au moins un critère échoue. \(H_B\) falsifie l’admissibilité de 5(b).
- **Second duel.** \(H_A'\) : le tirage caché ne réduit l’évasion informationnelle que d’au plus la marge gelée ; \(H_B'\) : il la réduit davantage. \(H_B'\) falsifie l’absence de gain matériel du tirage.
- Si la configuration fixe échoue sans gain du tirage, les deux configurations sont rejetées : cette issue n’est plus laissée sans verdict. Toute reconstruction de \(K\) depuis données ou format, au-delà du prédicteur modal et des étiquettes permutées, falsifie la suffisance du seul secret de \(K\).

## (c) Réponse à l’arbitre

### Décisions révisées

| Décision | Choix et confiance illustrative | Raison et changement d’avis |
|---|---|---|
| **1** | **(a), 0,80** | A reste la seule grandeur d’admission, mais sa définition suit l’audit du libellé et du code : si « ne signale pas » prévaut, \(A=1-p_{\mathrm{sig}}\), sans la confondre avec l’acceptation stricte. Le vecteur ternaire et B restent techniques. Je changerais si E1′ montrait que A échoue et que A+B satisfait les critères à fausses alertes maîtrisées. |
| **2** | **(b), 0,80** | Le seuil est choisi sur la seule loi nulle pertinente, édition factice comprise, puis sa détection est validée indépendamment. Je reviendrais à (a) si \(1/m\) franchissait cette validation sans gain utile ; si aucune candidate n’est faisable, je bloquerais la campagne plutôt que de publier une règle insuffisante. |
| **3** | **Option meilleure : hybride gelé et audité ; (c) seulement transitoire, 0,78** | Le programme reste une baseline mécanique ; le repéreur et les audits indépendants couvrent aussi les accords et les leurres. Je changerais si le programme satisfaisait seul les bornes requises avec gain négligeable de l’hybride, ou si ce dernier échouait à son propre audit. |
| **4.1** | **(c), 0,93** | En excès, le constat d’inadmission et les tests de l’optimiseur ne créent aucune pseudo-garantie. Je changerais uniquement pour une candidate préspécifiée dont E4a′ établirait couverture et utilité avant le regard correspondant, dans une campagne qui l’aurait gelée. |
| **4.2** | **(a), 0,97** | Les niveaux **RAPPORTÉS** de 2,5 %, ou 1,25 % par regard, restent inchangés après observation de l’excès. Seule une règle conditionnelle antérieure à tout regard, validée sur le risque familial, me ferait changer pour une campagne future. |
| **5** | **(a), 0,95** | La composition est tirée et l’admission recalculée avant toute fiche réelle ; le coût de recalcul ne justifie pas de conserver un témoin potentiellement exploitable. Je changerais si le recalcul était démontré impossible et si la configuration fixe franchissait E5′, y compris contre les stratégies adaptatives. |

### Ce qui est établi — et ce qui ne l’est pas

**Établi seulement au sens textuel ou algébrique :** ma première définition de A n’était pas justifiée ; la détection ne croît pas lorsqu’on relève un seuil ; la référence cachée n’est pas un concurrent informationnellement équitable ; une simulation indépendante ne teste pas les dépendances qui menacent la couverture ; une réallocation décidée après l’excès n’est pas devenue rétroactivement gelée.

**Non établi empiriquement :** la stabilité ou l’utilité réelle de A et B, la loi nulle de l’oracle, le transfert de l’étalonnage, la fidélité des désignateurs, la qualité des adjudications, les corrélations de lecteurs, toute couverture non triviale en excès, le comportement de la cohérence face à top-\(K\), l’absence de fuite de \(K\), et les coûts du repéreur. Les variations simulées de A et B demeurent **OBSERVÉES-NON-AUDITÉES**. Il est seulement **RAPPORTÉ** qu’aucune fiche n’a encore été servie.

### Expérience à faire en premier

Après l’audit documentaire des définitions, qui n’est pas une expérience, je lancerais **E2′**. Elle oppose directement « une règle de signalement utilisable existe » à « aucune candidate gelée n’est utilisable », tout en testant séparément la suffisance de \(1/m\). Elle est prioritaire parce qu’elle définit « reconnu », conditionne l’estimation de \(q\) et éclaire le régime d’excès ; sans sa loi nulle appariée, ses éditions factices et sa validation de détection, les autres garanties risquent de mesurer surtout le bruit de lecture ou la plume du tiers.

FIN-DE-CELLULE