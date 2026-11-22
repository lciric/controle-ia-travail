# Proposition B : Tour III.1, lecture d'antériorité pour le pilier « mathématiques nouvelles »

**Pièces reçues.** Les blocs FAITS et QUESTION sont présents et complets. Aucune autre proposition n'est visible, ce qui est conforme à un tour à l'aveugle. Je n'ai pas vérifié les empreintes sha256.

**Statuts.** Le bloc FAITS n'attribue aucun statut. Je cite donc ses énoncés comme **RAPPORTÉ** (rapportés par le dossier, non audités par moi) ; l'arbitre peut corriger cette attribution. Ce que j'apporte de ma propre connaissance est marqué **RAPPORTÉ (connaissance générale, non revérifiée ici)** ou **HYPOTHÈSE**. Mes propositions sont signalées comme telles.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut | Pourquoi c'est fragile |
|---|---|---|---|
| S1 | Une lecture précoce réduit les collisions coûteuses. | HYPOTHÈSE | Le taux de collision de base n'a pas été mesuré. Je ne le connais pas. |
| S2 | Un agent qui lit et empreinte des articles détecte les collisions. | HYPOTHÈSE | Le rappel de l'agent n'a jamais été mesuré. C'est la pièce porteuse de l'option (a). |
| S3 | « Empreinté » vaut « lu et compris ». | HYPOTHÈSE, fausse en général | Une empreinte prouve que le texte a été obtenu. Elle ne prouve pas qu'il a été rapproché de la cible. |
| S4 | Les cinq zones couvrent les cibles futures. | Zones : RAPPORTÉ ; couverture : HYPOTHÈSE | Le dossier liste les zones du pilier. Rien ne dit que la liste fermée y restera. |
| S5 | La liste des cibles n'est pas encore scellée. | Non établi | Le dossier dit « liste fermée » ; la question parle de « sceller la moindre cible ». Les deux sont en tension. Je ne sais pas où en est la liste. |
| S6 | Une collision après dépense ou revendication coûte cher, et la lecture large retarde les pilotes. | RAPPORTÉ | Ces coûts ne sont pas chiffrés, donc l'arbitrage entre les deux ne peut pas être calculé aujourd'hui. |
| S7 | La nouveauté est binaire et décidable. | HYPOTHÈSE | Il existe au moins quatre types de collision (voir §1). Le folklore n'est décidable par aucune recherche documentaire. |
| S8 | La valeur d'une cible tient à sa nouveauté. | HYPOTHÈSE | Le programme est défensif (RAPPORTÉ). Un résultat connu mais bien transposé au contrôle peut garder sa valeur ; ce qui coûte, c'est de le *revendiquer* comme neuf. |
| S9 | Les travaux voisins de 2026 sont pertinents. | Existence : RAPPORTÉ ; pertinence : inconnue | Ils n'ont pas été lus (RAPPORTÉ). |
| S10 | La veille peut être rouverte. | Gel : RAPPORTÉ ; réouverture : non établie | Les options (a) et (c) contredisent une décision du directeur. La question ne le dit pas. |
| S11 | Le juge de nouveauté et le lecteur humain fonctionnent. | Prévus : RAPPORTÉ ; fonctionnement : HYPOTHÈSE | Ce sont deux instruments sans mesure de performance. |

---

## 1. Ce qu'un expert ferait ici, et qu'on ne demande pas

**1.1 Lire d'abord les travaux de 2026 déjà croisés.** C'est l'inconnu connu le moins cher à réduire. Leur existence est RAPPORTÉE, leur contenu est inconnu. Une demi-journée de lecture humaine peut suffire (ordre de grandeur illustratif). Cette lecture contredit le gel : il faut demander au directeur une exception bornée, ce que la question ne mentionne pas.

**1.2 Séparer deux fonctions que l'option (a) confond.**
- La **cartographie** sert à *choisir* les cibles : où passe la frontière du connu, quels problèmes ouverts ont été énoncés.
- La **vérification de collision** sert à *protéger* une cible donnée : cet énoncé précis est-il déjà connu ?

La première se fait par zone et une seule fois. La seconde se fait par énoncé, et elle est plus étroite, donc probablement plus fiable pour cet énoncé (HYPOTHÈSE). Lire cinq zones « avant de sceller » est trop large pour protéger et trop peu ciblé pour choisir.

**1.3 Typer les collisions.** Le coût d'une collision et l'instrument capable de la détecter changent selon le type :

| Type | Exemple dans le pilier | Détectable par |
|---|---|---|
| **Littérale** | même énoncé, même vocabulaire | mots-clés, agent, recherche formelle |
| **De traduction** | même objet, autre communauté (voir ci-dessous) | expert multi-communauté ; un agent seulement s'il reçoit les synonymes |
| **De généralisation** | la cible est un cas particulier d'un résultat plus général | expert ; un agent rarement (HYPOTHÈSE) |
| **Folklore** | connu, jamais publié comme résultat (exercice, remarque de cours) | seulement un humain du domaine |

Les risques de traduction propres aux cinq zones relèvent de RAPPORTÉ (connaissance générale) ; les rattachements précis sont à vérifier :
- **Fusion de p-valeurs sous dépendance arbitraire.** Elle recoupe les « merging functions » (Vovk & Wang, 2020, « Combining p-values via averaging », *Biometrika*) et, pour les e-valeurs, Vovk & Wang (2021, « E-values: Calibration, combination and applications », *Annals of Statistics*). Elle recoupe aussi des bornes sur les sommes de variables dépendantes issues de l'agrégation de risques en actuariat : Rüschendorf, années 1980, référence à vérifier. **Un agent qui cherche « p-value combination » ne trouvera pas la littérature actuarielle.**
- **Tests séquentiels à nul non stationnaire.** Ils recoupent la détection de rupture (CUSUM, Page, référence à vérifier pour l'année) et les e-processus pour nuls composites. Voir Ramdas, Grünwald, Vovk & Shafer (2023), « Game-theoretic statistics and safe anytime-valid inference », *Statistical Science*, et Howard, Ramdas, McAuliffe & Sekhon (2021), « Time-uniform, nonparametric, nonasymptotic confidence sequences », *Annals of Statistics*.
- **Frontières de détection.** Elles recoupent les bornes inférieures minimax en test d'hypothèses (Le Cam, Fano, Bretagnolle–Huber ; manuel de référence : Tsybakov, 2009, *Introduction to Nonparametric Estimation*, Springer) et les résultats d'impossibilité pour la détection de filigranes (références à vérifier).
- **Jeux d'inspection sous budget.** Ils recoupent la littérature des jeux d'inspection (Avenhaus, von Stengel & Zamir, chapitre « Inspection games » du *Handbook of Game Theory*, vol. 3, 2002), les « audit games » (Blocki et al., 2013, référence à vérifier) et les jeux de sécurité de Stackelberg (référence à vérifier). **Une grande partie de cette littérature est ancienne, publiée en recherche opérationnelle et en économie, souvent hors arXiv, parfois derrière un mur payant.**
- **Recherche de programmes pour des règles de décision.** Elle recoupe Romera-Paredes et al. (2024), « Mathematical discoveries from program search with large language models », *Nature*, ainsi qu'AlphaEvolve (2025, référence à vérifier).

**1.4 Distinguer les trois formes de cible**, car la collision n'a pas le même sens pour chacune (formes : RAPPORTÉ ; analyse : ma proposition) :
- *Objet à score exact* : la collision est « un meilleur score, ou le même, est déjà connu ». On la vérifie contre des tables de bornes connues. Je ne sais pas si de telles tables existent pour ces zones.
- *Énoncé à démontrer ou réfuter* : la collision est « déjà démontré, déjà réfuté, ou corollaire immédiat ». Elle exige de lire la littérature.
- *Lemme de bibliothèque* : la collision est « déjà présent, ou fermé automatiquement à partir de l'existant ». Elle est **vérifiable mécaniquement**, sans lecture.

**1.5 Envoyer un message à un expert par zone avant de sceller un énoncé.** C'est l'instrument le moins cher contre le folklore et la traduction, et le seul qui les couvre (HYPOTHÈSE sur son efficacité, non mesurée). La question le place après la recherche (point 4). Un expert le placerait avant.

**1.6 Proportionner l'effort au coût de l'échec, cible par cible.** La profondeur de recherche devrait dépendre du budget engagé sur la cible et de l'usage prévu (revendication publique ou outil interne), pas d'un découpage par zone.

**1.7 Préenregistrer la recherche elle-même** : requêtes, bases, dates, documents obtenus (empreintes) et passages rapprochés. Sans cela, une affirmation du type « nous avons cherché » ne peut pas être auditée. L'empreinte couvre l'obtention du document, pas sa lecture (S3).

---

## 2. Données brutes de départ

Tout ce qui suit est RAPPORTÉ (connaissance générale, non revérifiée ici). Les limites indiquées sont des HYPOTHÈSES de travail.

**Bases d'articles**
- **arXiv** (math.ST, stat.ME, cs.LG, cs.GT, cs.CR) : libre, récent. Biais : il couvre mal la recherche opérationnelle et l'actuariat anciens.
- **zbMATH Open** : indexation mathématique ouverte, avec classification MSC. C'est utile pour la traduction entre communautés (62L pour le séquentiel, 91A pour les jeux, 62G…).
- **MathSciNet** : sur abonnement. Je ne sais pas si le programme y a accès.
- **OpenAlex, Semantic Scholar, Crossref** : métadonnées et graphe de citations, utiles pour le chaînage avant et arrière. Le texte intégral n'y est pas toujours disponible.
- **Google Scholar** : large couverture, mais aucune API stable ; ses résultats ne sont pas reproductibles.
- Actes de conférences (COLT, NeurIPS, ICML, EC, IJCAI, AAAI) et revues de recherche opérationnelle.

**Bibliothèques formelles**
- **mathlib** (Lean 4) et la bibliothèque Lean de statistique publique mentionnée par le dossier. Celle-ci couvre divergences, Fano, Bretagnolle–Huber, identité de Wald et e-valeurs (RAPPORTÉ). Son nom et son périmètre exact ne figurent pas dans le dossier, et je ne les invente pas.
- Les historiques de PR et les discussions de ces bibliothèques (travail en cours non fusionné). C'est une source de collision souvent oubliée (HYPOTHÈSE).

**Listes de problèmes ouverts**
- Sessions de problèmes ouverts de COLT.
- Sections « open problems » des surveys et des manuels de chaque zone.
- Sites de problèmes ouverts généralistes (Open Problem Garden ; le site des problèmes d'Erdős pour la combinatoire, peu pertinent ici).

Je ne connais pas de liste canonique de problèmes ouverts pour les tests séquentiels à nul non stationnaire ou pour les jeux d'inspection sous budget. **Je ne sais pas.**

**Notices de bancs** (miniF2F, ProofNet, PutnamBench, FrontierMath et autres) : utiles pour savoir si un énoncé a servi d'exercice, donc s'il relève du folklore ou d'un résultat connu. Leur recouvrement avec les cinq zones est probablement faible (HYPOTHÈSE).

**Données internes**
- Les travaux de 2026 croisés (RAPPORTÉ).
- La liste des cibles, si elle existe (S5).
- Les noms des experts disponibles pour la relecture (inconnus).

---

## 3. Méthodes et outils : ce que chacun suppose et comment il échoue

| Méthode | Suppose | Échoue quand |
|---|---|---|
| Requête par mots-clés (bases ci-dessus) | Vocabulaire partagé entre communautés | Collision de traduction. Les synonymes sont absents de la requête. |
| Recherche sémantique (plongements) | La proximité vectorielle suit l'équivalence mathématique | Deux énoncés ne diffèrent que par une hypothèse (indépendance contre dépendance arbitraire) et sont proches en vecteur mais distincts en vérité. Faux positifs « proches mais pas pareils » ; faux négatifs entre formulations très différentes. |
| Chaînage de citations (avant et arrière) depuis des articles pivots | Les bons pivots sont connus ; les communautés se citent entre elles | Les communautés ne se citent pas (actuariat et apprentissage). Le folklore n'est jamais cité. |
| Agent LLM qui lit et compare | L'agent obtient le texte intégral, le comprend et rapproche correctement | Mur payant : l'agent lit l'abstract seulement. Hallucination d'une correspondance ou d'une absence. Biais vers le récent et l'arXiv. Même angle mort que l'agent qui a produit la cible s'ils viennent de la même famille de modèles (HYPOTHÈSE). |
| Empreinte (hash) des documents | Traçabilité de l'obtention | Elle ne dit rien de la lecture. Contrôle mécanique minimal : chaque rapprochement cite un passage, et l'on vérifie automatiquement que ce passage figure dans le document empreinté. |
| Recherche formelle par type (style Loogle) | La cible est formalisée et le vocabulaire existe dans la bibliothèque | Formalisation différente mais équivalente (autre encodage de la dépendance, autre espace mesurable). |
| Recherche formelle en langue naturelle (moteurs sémantiques sur mathlib) | Les docstrings décrivent bien les énoncés | Docstrings absentes ou pauvres. |
| Fermeture automatique (`exact?`, `apply?`, `aesop` ou équivalents) sous budget fixe | « Déjà dérivable » vaut collision pour un lemme | Lemme vrai mais pénible à dériver : il est neuf comme lemme de bibliothèque sans être neuf mathématiquement. Ces deux nouveautés doivent rester distinctes. |
| Juge de nouveauté (modèle) | Il sait ce qu'il ne sait pas | Il prononce « neuf » faute d'avoir trouvé. Absence de preuve prise pour preuve d'absence. |
| Expert humain | Il couvre la zone, y compris le folklore | Il ne couvre qu'une communauté (traduction ratée) ; disponibilité ; complaisance si la question est mal posée. |

**Ce qui laisse passer une collision quelle que soit la méthode.** Une cible formulée dans le vocabulaire d'une seule communauté et vérifiée par des instruments qui partagent ce vocabulaire. La parade (ma proposition) : pour chaque énoncé, produire explicitement au moins deux reformulations dans d'autres vocabulaires (par exemple, dépendance arbitraire → « pire cas sur les couplages » → « agrégation de risques ») et chercher chacune.

---

## 4. Ce qui, hors du programme, vérifierait qu'une cible est neuve

Ce sont des propositions. Aucune n'est mesurée.
- **Relecteur du domaine externe, un par zone**, choisi si possible à l'interface de deux communautés (statistique et recherche opérationnelle, statistique et actuariat). Il reçoit l'énoncé et ses reformulations, et répond à trois questions fermées : connu ou publié ? cas particulier de quoi ? folklore ?
- **Mainteneurs de la bibliothèque Lean de statistique et de mathlib.** Ils savent ce qui est en cours (PR ouvertes, branches) et ce qui est considéré comme trivial. Ils vérifient la collision « lemme déjà prévu ».
- **Recherche formelle d'énoncés** dans les bibliothèques publiques, y compris les PR non fusionnées.
- **Auteurs des travaux de 2026 croisés.** Leur demander directement s'ils ont traité la cible. C'est peu coûteux, mais cela expose la cible ; c'est un arbitrage de confidentialité que je ne tranche pas.

**Limite.** Aucun de ces vérificateurs ne prouve la nouveauté. Chacun réduit une classe de collisions. La garantie reste « non trouvée par X, Y, Z selon le protocole P », jamais « neuf ».

---

## (b) Expériences décisives, en duel H_A contre H_B

Les seuils et effectifs ci-dessous sont **illustratifs**. Avec cinq zones et une liste fermée de taille inconnue, la puissance statistique sera faible : ces expériences servent à décider, pas à estimer finement.

### E1 : l'agent de recherche d'antériorité détecte-t-il les collisions non littérales ?

- **H_A** : le rappel de l'agent sur les collisions de *traduction* et de *généralisation* n'est pas nettement inférieur à son rappel sur les collisions littérales.
- **H_B** : il chute nettement.
- **Matériel** : un banc d'appâts construit par un humain du domaine. Pour chaque zone, des résultats connus et publiés, réécrits selon les quatre types de collision du §1.3. Chacun est **apparié** à un *quasi-jumeau* : même énoncé, une hypothèse ou une constante changée, de sorte que l'humain le juge non trouvé dans la littérature. Le quasi-jumeau sert de cas honnête apparié pour mesurer les fausses alertes.
- **Métriques** : rappel par type de collision ; taux de fausses alertes sur les quasi-jumeaux ; part des rapprochements dont la citation se retrouve dans le document empreinté.
- **Seuil** (illustratif) : H_B est retenue si le rappel sur traduction et généralisation est inférieur de plus de 30 points au rappel littéral.
- **Contrôle négatif** : des énoncés fabriqués, faux ou hors domaine, sur lesquels toute collision signalée est une hallucination. Le taux attendu est nul.
- **Ligne de base mécanique à battre** : une requête par mots-clés automatique (titre et énoncé) sur zbMATH et Semantic Scholar, sans agent.
- **Falsification** :
  - Rappel non littéral faible : H_A est falsifiée. L'option (a) « par un agent » ne protège pas contre les collisions chères, et il faut des humains.
  - Rappel comparable et au-dessus de la ligne de base : H_B est falsifiée. On peut automatiser davantage.
  - Agent non supérieur à la ligne de base : sa valeur ajoutée est réfutée, quelle que soit l'issue du duel.
- **Limite.** La vérité terrain des quasi-jumeaux dépend du jugement humain. Je l'indique comme biais, je ne le cache pas.

### E2 : la lecture précoce change-t-elle la liste des cibles ?

- **H_A** : une cartographie avant scellement retire ou reformule des cibles qu'un examen au scellement, ciblé par énoncé, n'aurait pas retirées.
- **H_B** : l'examen ciblé au scellement retire les mêmes cibles. La cartographie ne sert qu'à choisir, pas à protéger.
- **Protocole** : dans deux zones, un premier groupe propose des cibles candidates sans lecture. On fait ensuite (i) un examen ciblé par énoncé, puis (ii) une cartographie de zone. On compte les cibles écartées par (ii) mais non par (i).
- **Métrique** : nombre de collisions trouvées par la cartographie seule.
- **Seuil** (illustratif) : au moins une collision par zone suffit pour retenir H_A, car une seule collision évitée peut justifier la cartographie si les cibles sont chères (S6).
- **Contrôle négatif** : la cartographie appliquée à des cibles déjà connues comme ouvertes par l'expert. Elle ne doit pas en écarter.
- **Falsification** :
  - Zéro collision ajoutée : H_A est falsifiée. On reporte la cartographie et l'on fait seulement l'examen au scellement.
  - Au moins une collision ajoutée : H_B est falsifiée. La cartographie avant scellement se justifie dans ces zones.

### E3 : un lemme candidat est-il neuf pour la bibliothèque ?

- **H_A** : le lemme est absent de la bibliothèque et ne se ferme pas automatiquement sous un budget fixe.
- **H_B** : il est présent, en PR, ou fermé automatiquement.
- **Instruments** : recherche par type, recherche en langue naturelle, tactiques de fermeture automatique sous un budget de temps fixe (illustratif : quelques minutes par lemme), lecture des PR ouvertes.
- **Contrôle négatif** : des lemmes existants, renommés et reformulés, qui doivent tous être retrouvés. Leur rappel mesure l'instrument.
- **Falsification** :
  - Fermeture ou présence : H_A est falsifiée, et la cible n'est pas payante comme lemme.
  - Absence robuste après les contrôles : H_B est falsifiée.
- Cette expérience coûte peu et s'exécute **avant toute dépense sur un lemme**.

### E4 : les travaux de 2026 croisés recoupent-ils une zone de cible ?

- **H_A** : au moins un recoupe une cible candidate ou une zone prioritaire.
- **H_B** : aucun ne recoupe.
- **Métrique** : rapprochement documenté, passage cité et vérifié dans le document empreinté.
- **Contrôle négatif** : un article de 2026 tiré au hasard hors du pilier, qui ne doit produire aucun recoupement.
- **Falsification** :
  - Recoupement : H_B est falsifiée. La zone doit être replanifiée avant le scellement, et le gel est contredit par les faits du terrain.
  - Aucun recoupement : H_A est falsifiée. L'urgence de l'option (a) en est affaiblie.

---

## (c) Mesure minimale de chaque instrument nommé

| Instrument | Taux de détection mesuré sur | Fausses alertes mesurées sur | Vérification mécanique à battre |
|---|---|---|---|
| Agent lecteur avec empreintes | Banc d'appâts E1, par type de collision | Quasi-jumeaux appariés, énoncés fabriqués | Requête mots-clés automatique ; vérification que chaque citation figure dans le texte empreinté |
| Juge de nouveauté | Mêmes appâts. Le verdict « neuf » sur un appât compte comme raté. | Quasi-jumeaux jugés « connus » à tort | Le juge doit faire mieux que « neuf si l'agent n'a rien trouvé ». S'il n'y ajoute rien, il est redondant. Si possible, une famille de modèles différente de celle du générateur (HYPOTHÈSE sur l'utilité). |
| Recherche formelle d'énoncés | Lemmes existants reformulés (E3) | Lemmes réellement absents déclarés présents par confusion d'énoncés | Fermeture automatique sous budget fixe |
| Relecteur humain du domaine | Sous-échantillon des appâts, à l'aveugle, mêlé aux cibles réelles | Quasi-jumeaux | Aucune : c'est l'étalon. Mais on mesure l'accord entre deux relecteurs. S'il est faible, l'étalon lui-même est en cause. |
| Mainteneurs de bibliothèque | Lemmes en PR ouverte connus de l'équipe | Lemmes absents déclarés « prévus » | Recherche dans les PR par mots-clés |

Je ne sais pas quels taux sont acceptables. Ils dépendent du coût relatif d'une collision et d'une lecture (S6), que le dossier ne chiffre pas.

---

## 5. Reformulation de la demande

> Pour chaque cible candidate du pilier, avant d'engager son budget : quel niveau minimal de recherche d'antériorité, fait par des instruments dont on a mesuré le rappel par type de collision (littérale, traduction, généralisation, folklore), ramène le risque de collision sous un seuil que le programme fixe explicitement, compte tenu de la forme de la cible et du coût de son échec ? Et quelle cartographie, faite une seule fois par zone, sert à *choisir* les cibles plutôt qu'à les *protéger* ? Tout cela à l'intérieur d'une exception bornée au gel de la veille, que le directeur doit accorder ou refuser.

---

## 6. Recommandation : une option (d), étagée par cible et instrumentée

**Ni (a), ni (b), ni (c) telles quelles.**
- **(a)** confond cartographie et protection. Elle confie la protection à un agent dont le rappel n'est pas mesuré (S2), et elle est large mais pas ciblée.
- **(b)** engage la dépense avant tout contrôle, alors que la contrôle mécanique des lemmes coûte peu et que la collision après dépense coûte cher (S6, RAPPORTÉ).
- **(c)** n'a pas de règle d'arrêt : « tout le pilier » n'est pas délimité, et le volume lu grandit sans que la qualité de la détection soit connue.

**Proposition (d)**

1. **Tout de suite, à faible coût.**
   - Lire les travaux de 2026 croisés (E4), avec une exception au gel à demander au directeur.
   - Lancer E1 sur deux zones pour mesurer l'agent **avant** de lui confier quoi que ce soit.
2. **Avant le scellement : une cartographie légère par zone, pour choisir.** Surveys, manuels, listes de problèmes ouverts, plus un échange avec un expert par zone. Pas de lecture exhaustive. Priorité aux zones à fort risque de traduction : la fusion sous dépendance (actuariat) et les jeux d'inspection (recherche opérationnelle, hors arXiv). C'est un jugement de ma part (HYPOTHÈSE).
3. **Au scellement de chaque cible : une vérification proportionnée et typée.**
   - Lemme : E3, mécanique, obligatoire.
   - Objet à score : vérification contre les meilleures valeurs publiées connues.
   - Énoncé : recherche ciblée avec au moins deux reformulations dans d'autres vocabulaires, juge de nouveauté, message à un expert.
   - La profondeur croît avec le budget de la cible.
4. **À la première revendication : la recherche profonde de l'option (b).** Relecteur externe, mainteneurs, protocole de recherche préenregistré et joint à la revendication. La revendication est formulée comme « non trouvé selon le protocole P », jamais comme « neuf ».

**Ce qu'elle coûte.** Je n'ai aucun chiffre du dossier. Illustratif : quelques jours-personne d'expert pour construire le banc E1 et la cartographie de deux zones ; un calcul faible (voir (d)) ; quelques heures par cible au scellement. Le coût réel dominant est le **temps humain expert**, dont je ne connais ni la disponibilité ni le prix.

**Ce qu'elle suppose.**
- Le directeur accorde une exception bornée au gel (S10).
- Des experts sont joignables.
- La liste n'est pas déjà scellée (S5). Si elle l'est, les étapes 2 et 3 s'appliquent rétroactivement aux cibles existantes, avant toute dépense.

**Ce qui la ferait changer**
- E1 montre un rappel faible sur traduction et généralisation : augmenter la part humaine, ne **pas** élargir l'agent. L'option (a) « par un agent » est écartée.
- E1 montre un rappel élevé, au-dessus de la ligne de base : l'automatisation devient bon marché, et une version de (a) élargie aux cinq zones redevient défendable.
- E2 montre que la cartographie ajoute des collisions : l'étape 2 devient obligatoire et plus profonde dans ces zones.
- E2 montre qu'elle n'en ajoute pas : l'étape 2 se réduit au choix des cibles.
- E4 montre un recoupement : replanifier la zone concernée avant tout scellement.
- Le directeur maintient le gel : repli sur (b), plus E3 mécanique, plus un message à un expert par énoncé. C'est le minimum défendable, avec un risque de folklore et de traduction assumé et écrit.
- Les premières cibles scellées produisent plusieurs collisions à l'étape 4 : le seuil de l'étape 3 était trop bas, il faut élargir.

---

## (d) Ancrage matériel

Tout ce qui suit est **illustratif**, sauf mention contraire.

- **Modèles ouverts** pour l'agent lecteur et le juge : des familles ouvertes à poids publics, de taille moyenne à grande (par exemple Qwen, Llama, DeepSeek). Je ne fixe ni version ni taille : je ne peux pas garantir leurs performances ici.
- **Juge** : si possible d'une famille différente du générateur de cibles (HYPOTHÈSE).
- **Recherche sémantique** : un modèle de plongement ouvert, sur un corpus de textes intégraux, limité aux documents accessibles. Les murs payants (MathSciNet, revues de recherche opérationnelle) bornent ce que l'agent peut lire. C'est le goulot probable pour les jeux d'inspection (HYPOTHÈSE).
- **Formel** : Lean 4, mathlib et la bibliothèque de statistique mentionnée (RAPPORTÉ), avec les outils de recherche et les tactiques de fermeture usuels.
- **Calcul** (illustratif) : l'inférence de l'agent sur quelques centaines de documents par zone et l'indexation par plongements tiennent sur un à quelques GPU de classe serveur, pendant quelques jours. La fermeture automatique en E3 tient sur CPU.
- **Coût dominant** (illustratif) : le temps d'expert pour construire le banc d'appâts apparié d'E1, par exemple de l'ordre de dix paires appât / quasi-jumeau par zone et deux zones au départ, puis pour relire. Je ne sais pas le chiffrer en argent.

**Ce qui est réfutable dans cette proposition**
- La recommandation repose sur deux hypothèses : (i) les collisions chères sont surtout non littérales ; (ii) un examen ciblé au scellement protège mieux qu'une cartographie large.
- E1 réfute (i) si le rappel de l'agent ne chute pas hors du cas littéral, ou si les collisions observées sont surtout littérales.
- E2 réfute (ii) si la cartographie trouve des collisions que l'examen ciblé manque.

FIN-DE-CELLULE