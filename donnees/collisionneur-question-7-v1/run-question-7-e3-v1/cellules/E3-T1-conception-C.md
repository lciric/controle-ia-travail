*Note d'intégrité (Règle 2) : Les pièces amont `question-1-chapelles-v1.md`, `question-2-niches-v1.md`, `question-fusionnee-argon-collisionneur-v1.md` et `revue-biblio-fertilite-v1.md`, mentionnées en référence dans le dossier, sont absentes des faits servis ; je n'en invente pas le contenu.*

Voici la conception ciblée de la **Proposition C** pour le Tour III.1, structurée de manière à couvrir intégralement les exigences du protocole (livrables I à IV) et les cinq points (a–e) de la Question 7.

---

# I. Ce que la question suppose sans que ce soit établi, limites de l'analogie et antériorités — Livrable (a) & Points (a, d)

## 1. Analyse critique des présupposés et points de rupture de l'analogie — Point (a)

L'hypothèse de `conv-audit` transpose le formalisme des ensembles autocatalytiques (RAF : *Reflexively Autocatalytic and Food-generated sets*) aux fiches produites par le bisociateur. Cette analogie repose sur cinq présupposés non établis où la correspondance physico-chimique se brise :

1. **Absence de loi de conservation de la masse et non-consommation des réactifs (Statut : VÉRIFIÉ conceptuellement, HYPOTHÈSE quant à son innocuité dynamique).**
   * *Où l'analogie casse :* En chimie prébiotique, la réaction $A + B \to C$ consomme $A$ et $B$, ce qui engendre une compétition pour le substrat et sélectionne les cycles cinétiquement efficaces. Une fiche $A$ utilisée dans une fusion reste intégralement disponible pour une infinité d'autres fusions à coût marginal nul. Sans destruction ni dilution (oubli), le graphe `fiches → fusions → fiches` croît de manière monotone. Tout sous-graphe suffisament dense finit trivialement par former des cycles topologiques sans qu'aucune dynamique auto-entretenue réelle n'ait émergé.
   * *Condition de sauvetage :* La conservation de la masse doit être remplacée par la **conservation du budget d'attention et de calcul** (jetons/FLOPs par génération) et par une **dépréciation** : une fiche qui ne passe pas un test de mort en aval ou n'est pas réutilisée après $k$ générations (illustratif : $k=2$) sort du bain actif.

2. **Indétermination de la « catalyse » par opposition à la « réaction » (Statut : HYPOTHÈSE).**
   * *Où l'analogie casse :* Un ensemble RAF exige qu'à chaque réaction $r \in R$, au moins un catalyseur $c \in X$ soit présent, distinct ou en sus des réactifs issus de l'ensemble de nourriture (*Food set* $F$). Si une fusion dans le bisociateur s'écrit simplement $\text{Fiche}_1 + \text{Fiche}_2 \to \text{Fiche}_3$, il s'agit d'un graphe orienté de généalogie (réseau de réaction), **pas** d'un réseau catalytique. L'algorithme de Hordijk et Steel devient inopérant ou dégénéré (tout produit est son propre catalyseur).
   * *Condition de sauvetage :* Il faut séparer formellement les **réactifs** (les deux niches ou fiches d'énoncés $A$ et $B$ qui fournissent la matière empirique ou les anomalies) du **catalyseur** (une fiche d'opérateur mathématique, de lemme de transfert ou de protocole de test $K$ qui abaisse la barrière d'activation et permet à la fusion $A+B$ de franchir le test de mort sans que $K$ soit altéré).

3. **Confusion entre clôture topologique syntaxique et fertilité épistémique (Statut : HYPOTHÈSE).**
   * *Où l'analogie casse :* La question suppose qu'un lot de fiches qui « s'auto-entretient sans apport extérieur » est épistémiquement fertile. Or, dans un système de modèles de langage, l'auto-alimentation en vase clos sans substrat externe frais produit l'auto-consommation et l'effondrement modal (point soulevé en Section F.2 par Argon, statut : RAPPORTÉ), ou une dérive de Goodhart sur les juges figés (Section F.1 d'Argon, statut : RAPPORTÉ). Une boucle fermée de reformulations mutuelles forme un ensemble RAF topologique parfait, mais scientifiquement stérile (« poésie Vogon »).

4. **Le « substrat » (Food set $F$) réduit au corpus initial statique (Statut : HYPOTHÈSE).**
   * *Où l'analogie casse :* En biologie, le *Food set* est un flux continu d'énergie libre et de monomères. Si le corpus de départ est figé à la génération 0, la quantité d'information mutuelle extractible par recombinaison est bornée supérieurement (inégalité de traitement des données). Sans injection d'observations issues des bacs à sable (exécutions de code, preuves Lean, contre-exemples), le système ne peut pas « s'allumer » indéfiniment ; il sature dès que les isomorphismes latents du corpus initial sont épuisés.

5. **L'existence d'un seuil de transition de phase en fonction de la « dose de contact » (Statut : HYPOTHÈSE).**
   * *Ce qui est supposé :* Que le nombre de titres dans le tableau minimal ou le nombre de fusions par génération agit comme le paramètre de contrôle d'une percolation critique. Or, la littérature empirique rapportée dans les faits (Uzzi et al., 2013 ; Guimerà et al., 2005 ; Vilhena et al., 2014 — statut : RAPPORTÉ) observe souvent un optimum continu en cloche plutôt qu'une divergence critique, et Derex & Boyd (2016, statut : RAPPORTÉ) montrent qu'une dose de contact excessive détruit l'accumulation culturelle par convergence prématurée.

---

## 2. Antériorités : ensembles autocatalytiques et cascades d'idées — Point (d)

Conformément à la Règle 3, chaque référence issue des faits porte son statut d'origine, et les travaux classiques mentionnés sans notice complète dans les faits sont marqués « référence à vérifier ».

* **Origine de la vie et détection formelle des RAF :**
  * **Kauffman, S. A.** (1986, *Autocatalytic sets of proteins*, ou 1993, *The Origins of Order* — *référence à vérifier*, cité comme SUPPOSÉ dans les faits) : introduit la transition de phase dans les réseaux de polymères aléatoires lorsque le ratio réactions/molécules franchit un seuil critique. Statut du mécanisme : HYPOTHÈSE (modèle théorique sur graphes aléatoires).
  * **Hordijk, W., & Steel, M.** (2004, *Detecting autocatalytic, self-sustaining sets in chemical reaction systems* — *référence à vérifier*, cité comme SUPPOSÉ dans les faits) : formalisent les ensembles RAF (Reflexively Autocatalytic and F-generated) et prouvent qu'il existe un algorithme en temps polynomial $O(|R|^2)$ (par élimination itérative des réactions non soutenues) pour détecter le max-RAF. Statut : RAPPORTÉ / SUPPOSÉ dans les faits.
* **Transposition des RAF à la technologie, l'économie et la culture :**
  * **Arthur, W. B.** (2009, *The Nature of Technology* — cité comme SUPPOSÉ dans `reponse-conv-audit-question-3-v1.md`, *référence à vérifier*) et **Weitzman, M. L.** (1998, *Recombinant Growth* — cité comme SUPPOSÉ dans les faits, *référence à vérifier*) : modélisent l'innovation technologique comme un système autopoïétique où les technologies existantes se combinent pour engendrer des niches pour de nouvelles technologies. Limite : ne séparent pas formellement réactif et catalyseur.
  * **Hordijk, W., Kauffman, S. A., & Steel, M.** (travaux des années 2010–2020 appliquant le formalisme RAF à l'évolution économique et culturelle, avec Gabora pour la cognition — *références à vérifier*, citées globalement dans la question sous « Kauffman ; Arthur ; Hordijk » comme SUPPOSÉ) : montrent formellement que des représentations mentales ou des artefacts techniques peuvent être modélisés par des RAF, mais **sans critère de réfutation empirique** contre un simple graphe généalogique de citations.
* **Dynamique de l'adjacent possible et cascades de nouveautés :**
  * **Tria, F., Loreto, V., Servedio, V. D. P., & Strogatz, S. H.** (2014, *The dynamics of correlated novelties*, Scientific Reports, 4, 5890 — statut : RAPPORTÉ par Argon et conv-audit, notice vérifiée dans les faits) : formalisent l'adjacent possible de Kauffman par une urne de Pólya avec déclenchement. Une nouveauté catalyse l'ouverture d'un sous-espace adjacent, produisant la loi de Heaps et des corrélations en rafales (avalanches).
* **« Allumage » (ignition) épidémiologique et condensation topologique des champs :**
  * **Bettencourt, L. M. A., Cintrón-Arias, A., Kaiser, D. I., & Castillo-Chávez, C.** (2006, *The power of a good idea: Quantitative modeling of the spread of ideas from epidemiological models*, Physica A, 364, 513–536) et **Bettencourt, L. M. A., Kaiser, D. I., & Kaur, J.** (2009, *Scientific discovery and topological transitions in collaboration networks*, Journal of Informetrics, 3(3), 210–221) : notices VÉRIFIÉES dans `lecture-reponse-argon-bisociation-v1.md`, contenu SUPPOSÉ (PDF non empreintés). Ils modélisent l'allumage d'un champ non par un RAF chimique, mais par (1) le franchissement d'un seuil épidémiologique $R_0 > 1$ et (2) la condensation d'une composante géante riche en boucles dans le graphe de collaboration.
  * **Cascade d'erreurs vs cascade d'idées en essaims :** Les événements d'octobre 2026 rapportés par Argon (**OpenAI**, 6 octobre 2026, *Sharing AI progress in mathematics*, 722 manuscrits, statut : RAPPORTÉ / VÉRIFIÉ via extraits primaires dans les faits) démontrent que dans un graphe de dépendances déductives entre générations, la propagation en cascade concerne autant les erreurs (retrait de 3 manuscrits en 24h suite à une erreur de signe en amont) que les théorèmes valides.

---

# II. Définitions opérationnelles et journalisation — Points (b, e)

## 1. Définition opérationnelle de la réaction, du RAF épistémique, de l'allumage et de la fertilité — Point (b)

Pour que le formalisme RAF ne soit pas une métaphore vide, nous définissons sur le journal d'une course un **hypergraphe orienté catalytique et vérifié** $\mathcal{H}_g = (\mathcal{X}_g, \mathcal{R}_g, \mathcal{C}_g, F)$ à la génération $g$ :

* **Ensemble de nourriture ($F$, *Food set*) :** L'ensemble des fiches de la génération $g=0$ extraites directement du corpus externe (énoncés de problèmes, théorèmes ou faits observés).
* **Espèces ($\mathcal{X}_g$) :** L'ensemble des fiches actives à la génération $g$. Une fiche $x \in \mathcal{X}_g$ n'est admise dans $\mathcal{X}_g$ que si elle a **franchi son test de mort** (exécution en bac à sable ou vérification formelle/juge figé) et que son **gain de compression ou de prédiction** par rapport à ses parents est strictement positif ($\Delta \text{MDL}(x) > 0$).
* **Réaction de fusion ($r \in \mathcal{R}_g$) :** Une opération du bisociateur prenant un sous-ensemble de fiches réactives $A_r \subset \mathcal{X}_{g-1}$ ($|A_r| \ge 2$, typiquement deux fiches d'objets/problèmes issues de niches distinctes) pour produire une fiche fille valide $y_r \in \mathcal{X}_g$.
* **Catalyseur ($c \in \mathcal{C}_g(r)$) :** Une fiche $c \in \mathcal{X}_{g-1}$ (méthode, opérateur formel, lemme pont ou protocole de test) qui est **explicitement invoquée** dans la trace de génération de la réaction $r$ pour opérer la traduction entre les réactifs $A_r$, sans être l'objet même du problème fusionné.
* **Sous-ensemble e-RAF (RAF épistémique) :** Un sous-ensemble non vide de réactions $\mathcal{R}' \subseteq \mathcal{R}_g$ est un **e-RAF** si et seulement si :
  1. *Clôture réflexive d'autocatalyse (RA) :* Pour toute fusion $r \in \mathcal{R}'$, il existe au moins un catalyseur $c \in \mathcal{C}_g(r)$ tel que $c \in F \cup \text{Produits}(\mathcal{R}')$, **avec la contrainte stricte anti-triviale** qu'à partir de $g \ge 2$, une proportion $\alpha \ge 0{,}5$ (illustratif) des catalyseurs appartienne à $\text{Produits}(\mathcal{R}') \setminus F$ (catalyse endogène : ce sont les lemmes générés par le bisociateur à $g=1$ qui catalysent les fusions à $g=2$).
  2. *Génération par la base (F-generated) :* Tous les réactifs $a \in A_r$ de toute réaction $r \in \mathcal{R}'$ peuvent être produits à partir de $F$ par une suite ordonnée de réactions dans $\mathcal{R}'$.
  3. *Survie à la rétractation en cascade (DAG-valide) :* Aucun nœud ancêtre de $\mathcal{R}'$ n'a été invalidé par un test de mort ultérieur (leçon des 722 manuscrits d'octobre 2026, statut : RAPPORTÉ).

**Définition opérationnelle de l'Allumage ($\text{Ignite}_g \in \{0,1\}$) :**
Un lot de fiches s'allume à la génération $g \ge 2$ si et seulement si :
1. Le sous-graphe induit par les générations $1 \dots g$ contient un **e-RAF irréductible** non vide dont l'arborescence causale s'étend jusqu'à $g$ sans réinjection externe de fiches hors de $F$.
2. Le **taux de reproduction endogène** des fiches au sein de l'e-RAF vérifie $R_{\text{endo}}(g) = \frac{|\text{Produits valides à } g \text{ catalysés par } g-1|}{|\text{Produits valides à } g-1|} \ge 1{,}0$ (seuil de Bettencourt transposé, statut : HYPOTHÈSE).

**Définition opérationnelle de la Fertilité d'une paire / fusion $r = (x_i, x_j \xrightarrow{c} y_r)$ :**
La fertilité d'une fusion $r$ réalisée à $g=1$ est un couple de mesures observables à $g=2$ :
1. **Contribution à la clôture ($\Delta \text{RAF}(r)$) :** Variation relative de la taille du max-e-RAF à $g=2$ lorsque l'on supprime la fiche produit $y_r$ et sa descendance du graphe :
   $$\Delta \text{RAF}(r) = \frac{|\text{max-e-RAF}(\mathcal{R}_{\le 2})| - |\text{max-e-RAF}(\mathcal{R}_{\le 2} \setminus \{r\})|}{|\text{max-e-RAF}(\mathcal{R}_{\le 2})|}$$
2. **Pouvoir catalytique aval ($K(r)$) :** Nombre de fusions distinctes et valides à $g=2$ dans lesquelles la fiche produit $y_r$ agit comme **catalyseur** ($y_r \in \mathcal{C}_2(r')$).

---

## 2. Ce qu'il faut journaliser dès la génération 1 — Point (e)

Pour pouvoir calculer $\text{max-e-RAF}$, $R_{\text{endo}}$ et $\Delta \text{RAF}(r)$ en génération 2 sans fuite temporelle ni reconstruction *post hoc*, le journal de la génération 1 doit obligatoirement enregistrer pour **chaque tentative de fusion** (y compris les échecs, conformément à la Section D d'Argon sur le biais du survivant) un enregistrement structuré contenant :

1. `attempt_id`, `generation_index` ($g \in \{1, 2, \dots\}$), `timestamp`, `token_budget_spent`.
2. `control_dose_params` : le tuple exact du paramètre de contrôle $(M_{\text{titres}}, B_{\text{fusions}}, \text{topologie\_essaim})$ où $M_{\text{titres}}$ est le nombre de titres visibles dans le tableau minimal servi à l'agent et $B_{\text{fusions}}$ le nombre de fusions tentées par génération.
3. `reactant_ids` : liste typée des identifiants des fiches sources $[x_i, x_j]$ fournissant les problèmes ou objets croisés, et leur statut d'origine (`in_F: bool`).
4. `catalyst_ids` : liste explicite des identifiants des fiches $[c_k]$ utilisées comme opérateurs/méthodes de transfert. *Note d'implémentation :* le prompt du bisociateur dès $g=1$ doit forcer la séparation syntaxique entre `[RÉACTIFS : fiches problèmes]` et `[CATALYSEUR : fiche méthode/lemme]`, et produire en sortie une fiche typée (`type: OBJECT` ou `type: CATALYST_LEMMA`).
5. `death_test_record` : booléen `passed_death_test`, trace du vérificateur (sortie bac à sable / juge figé), et score d'alignement d'énoncé `spec_fidelity_score` (contrôle du lecteur distinct contre la faille de Bastounis et al., statut : RAPPORTÉ).
6. `novelty_compression_record` : distance cosinus / Jaccard lexicale et formelle par rapport à toutes les fiches de $F \cup \mathcal{X}_{g-1}$, et gain de compression $\Delta \text{MDL}$ (pour éliminer les paraphrases qui créeraient de faux cycles RAF).
7. `dag_dependencies` : pointeurs amont stricts permettant l'invalidation récursive immédiate si un parent est réfuté à $g+1$.

---

# III. Expériences décisives, prédictions chiffrées et critères de mort (Génération 2) — Livrable (b) & Point (c)

Conformément à la règle B4 (inférence forte), nous testons l'hypothèse de `conv-audit` à travers trois duels expérimentaux exclusifs ($H_A$ contre $H_B$) exécutables entre la génération 1 et la génération 2, assortis d'un critère de mort global.

## Duel Expérimental 1 : Transition de phase autocatalytique vs Accumulation sous-critique ou convergence (Test du paramètre de contrôle « dose de contact »)

* **Hypothèse $H_A$ (Transition de phase e-RAF par seuil de dose) :** En faisant varier la dose de contact $D = (M_{\text{titres}}, B_{\text{fusions}})$ à budget de jetons constant par fusion, la probabilité d'apparition d'un e-RAF endogène à $g=2$ et le taux de reproduction $R_{\text{endo}}(g=2)$ présentent une transition abrupte (sigmoïde raide avec pic de variance au seuil $D_c$), permettant au lot de s'auto-entretenir ($R_{\text{endo}} \ge 1{,}0$) à $g=2$ sans apport de fiches hors de $F$.
* **Hypothèse $H_B$ (Régime sous-critique monotone ou effondrement en cloche de Derex-Boyd) :** L'accumulation de fiches valides dépend linéairement ou de manière concave (en cloche) de la dose $D$ ; soit aucun e-RAF endogène ne maintient $R_{\text{endo}} \ge 1{,}0$ à $g=2$ sans réinjection externe (épuisement du substrat), soit les fortes doses $D > D_c$ provoquent un effondrement de la diversité par alignement prématuré des agents (Derex & Boyd, 2016, statut : RAPPORTÉ).
* **Protocole :** Sur un lot fixe de $|F| = 40$ fiches initiales (illustratif) couvrant 8 niches du contrôle des IA (illustratif), exécuter $N = 10$ courses indépendantes (graines aléatoires distinctes, illustratif) pour chacun des 5 niveaux de dose $M_{\text{titres}} \in \{4, 8, 16, 24, 40\}$ (illustratif) sur 3 générations ($g=0 \to 1 \to 2 \to 3$), **sans aucune injection externe** après $g=0$.
* **Métriques :**
  1. $P_{\text{RAF}}(D)$ : proportion des 10 courses contenant un $\text{max-e-RAF}$ non vide avec catalyse endogène ($\alpha \ge 0{,}5$) à $g=2$ et $g=3$.
  2. $R_{\text{endo}}(g, D)$ et sa variance inter-courses $\text{Var}[R_{\text{endo}}](D)$.
  3. Entropie sémantique inter-fiches $H_{\text{sem}}(g, D)$.
* **Contrôle négatif :**
  1. *Graphe nul par permutation (Erdős-Rényi stratifié) :* Conserver le nombre exact de fiches validées à chaque génération, mais permuter aléatoirement les étiquettes `catalyst_ids` pour mesurer le taux d'e-RAF dû au seul hasard combinatoire de la densité d'arêtes $P_{\text{RAF}}^{\text{nul}}(D)$.
  2. *Contrôle sans filtre de paraphrase ($\Delta \text{MDL}$ désactivé) :* Pour mesurer l'allumage spécieux (boucles de reformulation).
* **Seuils chiffrés et issues de falsification (Prédiction pour la génération 2 — Point c) :**
  * **Falsification de $H_B$ (Validation de $H_A$) :** Il existe une dose critique $D_c$ telle que $P_{\text{RAF}}(D_c) - P_{\text{RAF}}^{\text{nul}}(D_c) \ge 0{,}50$ (illustratif), $R_{\text{endo}}(g=2, D_c) \ge 1{,}0$ maintenu à $g=3$ ($R_{\text{endo}}(g=3, D_c) \ge 1{,}0$), et le rapport d'évidence bayésien (AIC/BIC) d'un modèle à seuil (fonction de Hill avec exposant de coopérativité $n > 3$, illustratif) bat un modèle linéaire ou quadratique de $\Delta \text{BIC} \ge 6$ (illustratif), accompagné d'un pic de variance $\text{Var}[R_{\text{endo}}](D_c) > 2 \cdot \max_{D \neq D_c} \text{Var}[R_{\text{endo}}](D)$ (illustratif).
  * **Falsification de $H_A$ (Critère de mort de l'hypothèse d'allumage pour la génération 2) :** Si, pour **toutes** les doses $D$ testées, $R_{\text{endo}}(g=2) < 0{,}8$ (illustratif) ou chute de plus de $50\%$ entre $g=1$ et $g=2$ (extinction sous-critique dès l'arrêt de l'apport extérieur), **ou** si $P_{\text{RAF}}(D)$ ne dépasse pas le contrôle nul par permutation de plus de $0{,}15$ (illustratif : $p > 0{,}05$ au test exact de Fisher), alors **l'hypothèse de l'allumage autocatalytique en vase clos est réfutée et abandonnée**.

---

## Duel Expérimental 2 : Catalyse fonctionnelle (RAF) vs Simple généalogie additive (Branchement de Galton-Watson / Bettencourt)

* **Hypothèse $H_A$ (Nécessité de la clôture catalytique RAF) :** La fertilité à la génération 2 dépend spécifiquement de la présence de fiches *catalyseurs* endogènes ($\Delta \text{RAF}(r) > 0$). À nombre égal de fiches parentes validées à $g=1$, un lot qui possède une clôture catalytique (les lemmes produits à $g=1$ servent d'opérateurs de traduction à $g=2$) engendre significativement plus de découvertes survivant aux tests de mort à $g=2$ qu'un lot sans catalyse croisée.
* **Hypothèse $H_B$ (Processus de branchement généalogique simple sans catalyse) :** La structure tripartite `réactifs + catalyseur → produit` est un artefact de prompt. La dynamique de génération 2 est entièrement expliquée par le taux de reproduction de base individuel des fiches $R_0$ (processus de Galton-Watson ou contagion simple de Bettencourt 2006, statut : RAPPORTÉ) et par la proximité topologique locale (fermeture triadique de Gu & Krenn 2024, statut : RAPPORTÉ), sans aucun pouvoir prédictif additionnel de la métrique $\Delta \text{RAF}$.
* **Protocole (Intervention d'ablation causale à $g=1 \to g=2$) :** À l'issue de la génération 1, identifier les fiches ayant une forte centralité catalytique ($\Delta \text{RAF}(r) > 0{,}20$, illustratif) et les apparier (score de propension sur la longueur, le score du juge figé à $g=1$ et le degré de co-occurrence lexicale) avec des fiches « feuilles » ou purement réactives ($\Delta \text{RAF}(r) = 0$). Lancer la génération 2 sous deux conditions d'intervention à budget égal :
  * *Condition $\text{do}(\text{Ablation RAF})$ :* Masquer les fiches à fort $\Delta \text{RAF}$ tout en conservant les fiches appariées.
  * *Condition $\text{do}(\text{Ablation Témoin})$ :* Masquer les fiches appariées ($\Delta \text{RAF} = 0$) tout en conservant les catalyseurs RAF.
* **Métrique :** Rendement en découvertes validées à $g=2$ ($Y_2$ = nombre de fiches franchissant le test de mort et le filtre $\Delta \text{MDL}$ à $g=2$).
* **Contrôle négatif :** Ablation aléatoire du même nombre de fiches à $g=1$.
* **Seuils chiffrés et issues de falsification :**
  * **Falsification de $H_B$ :** L'ablation des nœuds RAF provoque un effondrement disproportionné et super-linéaire du rendement à $g=2$ : $\frac{\mathbb{E}[Y_2 \mid \text{do}(\text{Ablation Témoin})] - \mathbb{E}[Y_2 \mid \text{do}(\text{Ablation RAF})]}{\mathbb{E}[Y_2 \mid \text{Ablation Aléatoire}]} \ge 0{,}35$ (illustratif, réduction relative d'au moins 35 % du rendement par rapport à l'ablation témoin appariée, $p < 0{,}01$).
  * **Falsification de $H_A$ (Critère de mort de la métrique de fertilité RAF) :** Si la différence de rendement entre l'ablation des catalyseurs RAF et l'ablation des témoins appariés par score de qualité individuel est inférieure à $10\%$ (illustratif), ou si dans une régression prédisant $Y_2$, l'ajout de $\Delta \text{RAF}$ au-dessus du degré des nœuds et du score local de Gu-Krenn n'améliore pas l'AUC hors échantillon d'au moins $+0{,}05$ (illustratif), le formalisme RAF est déclaré **redondant** et remplacé par le simple branchement $R_0$ et la taille de la composante géante.

---

## Duel Expérimental 3 : Allumage épistémique réel vs Allumage spécieux (Auto-intoxication et Goodhart en vase clos)

* **Hypothèse $H_A$ (Validité externe de l'allumage endogène) :** Les fiches produites à $g=2$ et $g=3$ au sein d'un e-RAF auto-entretenu résolvent de véritables anomalies et conservent leur taux de survie lorsqu'elles sont confrontées à un **vérificateur externe tenu à l'écart** (tests de mort hors distribution non vus à $g=1$).
* **Hypothèse $H_B$ (Auto-consommation et dérive de Goodhart — Section F.1 et F.2 d'Argon) :** L'isolement requis par l'allumage « sans apport extérieur » sélectionne des boucles autocatalytiques qui exploitent les failles syntaxiques des juges figés de la course ou réduisent la diversité lexicale en reformulant les mêmes tautologies (pollution synthétique).
* **Protocole :** Soumettre toutes les fiches de $g=1$ et $g=2$ appartenant à un e-RAF détecté par le juge interne de la course à un **banc d'audit aveugle externe** : (1) un « lecteur distinct » d'une autre famille de modèles évaluant la fidélité à l'énoncé initial (parade à la faille de Bastounis et al., statut : RAPPORTÉ), et (2) une batterie de tests de mort réservés (*hold-out sandbox tests*) jamais exposés pendant la course.
* **Métrique :** Taux de survie hors distribution $S_{\text{OOD}}(g)$ des fiches appartenant à l'e-RAF comparé aux fiches hors e-RAF de la génération 1.
* **Contrôle négatif :** Fiches générées par un essaim sans filtre de test de mort à $g=1$ (auto-consommation pure).
* **Seuils chiffrés et issues de falsification :**
  * **Falsification de $H_B$ :** Le taux de survie au banc externe des fiches issues de l'e-RAF à $g=2$ ne se dégrade pas par rapport à $g=1$ ($S_{\text{OOD}}(g=2 \mid \text{e-RAF}) \ge 0{,}90 \cdot S_{\text{OOD}}(g=1)$, illustratif) et surpasse celui des fiches hors e-RAF d'au moins $+15$ points de pourcentage (illustratif).
  * **Falsification de $H_A$ (Critère de mort du vase clos) :** Si $S_{\text{OOD}}(g=2 \mid \text{e-RAF}) < 0{,}50 \cdot S_{\text{OOD}}(g=1)$ (illustratif : plus de la moitié des fiches de l'ensemble autocatalytique sont des faux positifs spécieux ou des dérives d'énoncé à $g=2$), l'allumage « sans apport extérieur » est falsifié comme régime de découverte et remplacé par une obligation d'ancrage externe continu à chaque génération.

---

# IV. Validation des instruments nommés — Livrable (c)

Pour chaque instrument nommé dans la Question 7 et les faits associés, voici le protocole minimal d'étalonnage :

| Instrument nommé | Fonction visée | Cas honnêtes appariés (Banc d'étalonnage) | Vérification mécanique (Baseline) à battre | Mesure minimale de fonctionnement (Seuil de détection / Fausses alertes) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Détecteur de max-e-RAF (Algorithme de Hordijk-Steel adapté aux fiches)** | Identifier en temps polynomial le sous-ensemble maximal de fusions auto-catalysées et soutenues par $F$, et calculer $\Delta \text{RAF}(r)$. | **Positifs ($N=50$, illustratif) :** Arbres de preuves ou de découvertes historiques avérées (ex. sous-graphes de *Mathlib* / *Archive of Formal Proofs* ou lignées de papiers où un lemme pont catalyse une série de théorèmes à $t+2$).<br>**Négatifs appariés ($N=50$, illustratif) :** Sous-graphes de même densité d'arêtes et même distribution de degrés, mais purement additifs (revues de littérature, variations paramétriques sans lemme catalyseur réutilisé) ou graphes synthétiques générés par paraphrase. | **Baseline 1 :** Taille de la plus grande composante fortement connexe (SCC) ou composante géante faiblement connexe (Bettencourt 2009).<br>**Baseline 2 :** PageRank / Centralité de vecteur propre sur le graphe `fiche → fusion → fiche`. | **Taux de détection (Rappel) $\ge 0{,}80$** (illustratif) sur les lignées catalytiques avérées.<br>**Taux de fausses alertes (FPR) $\le 0{,}10$** (illustratif) sur les graphes de paraphrase et les revues additives.<br>**Gain sur baseline :** Précision@10 pour prédire la survie à $g+1$ supérieure d'au moins **$+0{,}10$** (illustratif) à la simple centralité PageRank et au degré sortant. |
| **2. Extracteur-Typage de Catalyse (`[Réactifs]` vs `[Catalyseur]`) dans le Journal** | Séparer fidèlement les fiches qui posent le problème (réactifs) de la fiche qui fournit l'opérateur formel de résolution (catalyseur). | **100 triplets de fusions (illustratif)** annotés à l'aveugle par l'arbitre humain ou extraits de preuves formelles (où les hypothèses du théorème sont les réactifs et la tactique/lemme importé d'une autre bibliothèque est le catalyseur), appariés avec **100 fusions factices** où le « catalyseur » cité dans le texte n'est qu'une co-mention décorative (jargon emprunté sans utilisation opératoire). | Heuristique lexicale simple : attribuer le rôle de catalyseur à la fiche parente contenant le plus de mots-clés méthodologiques ou d'équations, ou tirage aléatoire parmi les parents de la fusion. | **Taux de détection (Vrais catalyseurs opératoires identifiés) $\ge 0{,}85$** (illustratif).<br>**Taux de fausses alertes (Citations décoratives classées comme catalyseurs) $\le 0{,}15$** (illustratif), vérifié par test d'ablation (retirer le catalyseur du contexte empêche l'agent de reproduire la fusion valide dans $\ge 80\%$ des cas, illustratif). |
| **3. Contrôleur de « Dose de contact » (Tableau minimal + Fusions/génération)** | Réguler le flux d'information inter-niches pour induire l'allumage sans provoquer la fusion prématurée des niches. | Paires de sous-essaims appariés exécutant la même tâche sur le même lot $F$, soumis à des doses croissantes $M_{\text{titres}} \in \{4 \dots 40\}$ (illustratif), comparés à des paires où les titres sont remplacés par des résumés aléatoires de longueur identique (contrôle de charge de contexte). | Échantillonnage uniforme aléatoire de paires sans tableau minimal, ou visibilité globale (clique complète de tous les titres dès $g=1$). | Capacité à maintenir une **distance sémantique inter-niches $d_{\text{lex}} > \theta_{\min}$** tout en augmentant le taux de ponts valides : la dose optimale doit battre la clique complète (visibilité totale) d'au moins **$+20\%$ de diversité survivante** à $g=2$ (illustratif), avec un taux d'effondrement modal (fausses alertes de consensus prématuré) **$\le 0{,}10$** (illustratif). |
| **4. Filtre de Test de mort + Fidélité d'énoncé + $\Delta \text{MDL}$ (Garde-fou anti-Goodhart)** | Empêcher les fusions dégénérées ou les paraphrases d'entrer dans $\mathcal{X}_g$ et de créer des e-RAF artificiels. | **50 bisociations valides (illustratif)** appariées à **50 bisociations spécieuses (illustratif)** construites par injection de fautes connues : (a) modification subtile des hypothèses (type forçage externe ad hoc de Navier-Stokes / Bastounis et al., statut : RAPPORTÉ), (b) erreur de signe en amont (type retrait des 3 manuscrits d'octobre 2026, statut : RAPPORTÉ), (c) pure reformulation isomorphe d'une fiche de $F$. | Juge LLM unique évaluant la « plausibilité et l'intérêt scientifique » sur une échelle de 1 à 10 sans exécution en bac à sable ni vérification de fidélité d'énoncé séparée. | **Taux de détection (Rejet des fusions spécieuses/paraphrases) $\ge 0{,}90$** (illustratif, soit FPR d'admission dans le graphe RAF $\le 0{,}10$).<br>**Taux de fausses alertes (Rejet à tort d'une fusion valide) $\le 0{,}15$** (illustratif). Doit battre le juge LLM simple d'au moins **$+30$ points de réjection** sur les pièges de type Bastounis (illustratif). |

---

# V. Ancrage matériel — Livrable (d)

Tous les chiffres de dimensionnement matériel, de jetons et de coûts ci-dessous (hors la mention de 0,61 USD pour la recherche Argon qui est VÉRIFIÉE dans les faits) sont marqués **« illustratif »** conformément à la Règle 4.

1. **Modèles ouverts et infrastructure d'exécution :**
   * **Agents Proposeurs / Bisociateurs (Génération de fusions) :** Modèles à poids ouverts spécialisés en raisonnement et code/mathématiques pour garantir la reproductibilité sans dérive d'API fermée : `Qwen2.5-72B-Instruct` ou `DeepSeek-R1-Distill-Qwen-32B` / `Llama-3.3-70B-Instruct` (illustratif), servis localement via `vLLM` avec quantification FP8 ou AWQ sur nœuds GPU.
   * **Lecteur distinct et Juge figé (Découplage architectural obligatoire) :** Pour éviter qu'un modèle ne valide ses propres biais génératifs, le juge figé et le lecteur distinct d'alignement d'énoncé doivent appartenir à une famille d'entraînement distincte de celle du proposeur (ex. `Mistral-Large-Instruct-2411` ou `Gemma-2-27B-IT` si le proposeur est `Qwen/DeepSeek`, illustratif), complétés par un vérificateur déterministe en bac à sable (`Python/pytest` pour les protocoles empiriques de contrôle d'IA, et `Lean 4` pour les lemmes formels).
   * **Algorithme RAF et analyse de graphe :** Exécuté sur CPU pur via `NetworkX` / `igraph` en Python. L'algorithme de Hordijk-Steel ayant une complexité polynomiale $O(|\mathcal{R}|^2)$ (statut : RAPPORTÉ/SUPPOSÉ), sur un journal de course de $|\mathcal{R}| \le 1\,000$ fusions par génération (illustratif), le temps de détection du max-e-RAF et de toutes les ablations $\Delta \text{RAF}(r)$ est inférieur à **1 seconde sur un seul cœur CPU** (illustratif : coût de calcul négligeable).

2. **Budget de calcul et coût estimé pour les expériences des Générations 1 à 3 (Duel 1 + Duel 2 + Duel 3) :**
   * **Paramètres d'une course unitaire (illustratif) :**
     * Taille du *Food set* initial : $|F| = 40$ fiches.
     * Générations par course : $3$ ($g=1, 2, 3$).
     * Budget de fusions tentées par génération : $B_{\text{fusions}} = 30$ (illustratif), soit $90$ tentatives par course.
     * Jetons par tentative (incluant la lecture du tableau minimal, la réflexion profonde de fusion, le test de mort en bac à sable et le contrôle du lecteur distinct) : $\approx 15\,000$ jetons d'entrée + $5\,000$ jetons de sortie = $20\,000$ jetons par tentative (illustratif), soit **$1{,}8 \times 10^6$ jetons par course complète de 3 générations** (illustratif).
   * **Volume total de la grille expérimentale (illustratif) :**
     * *Duel 1 (Grille de dose de contact) :* $5 \text{ doses} \times 10 \text{ graines} = 50 \text{ courses}$ $\to 90 \times 10^6$ jetons (illustratif).
     * *Duel 2 (Ablations causales à $g=1 \to g=2$) :* $20 \text{ courses sélectionnées} \times 2 \text{ bras d'ablation (RAF vs Témoin)} \times 1 \text{ génération relancée}$ $\to 12 \times 10^6$ jetons (illustratif).
     * *Duel 3 (Audit externe hors distribution sur les survivants) :* Évaluation approfondie d'environ $500$ fiches survivantes (illustratif) $\to 10 \times 10^6$ jetons (illustratif).
     * **Total général :** **$\approx 112 \times 10^6$ jetons** (112 millions de jetons, illustratif).
   * **Temps matériel et coût financier (illustratif) :**
     * Sur un nœud de **4 GPU NVIDIA H100 (80 Go)** ou **8 GPU A100 (80 Go)** (illustratif) faisant tourner un modèle 70B en FP8 à un débit agrégé de $\approx 1\,500$ jetons/seconde (illustratif), les $112 \times 10^6$ jetons s'exécutent en **$\approx 21$ heures d'horloge** (soit $\approx 84$ heures-GPU H100, illustratif).
     * À un tarif infonuagique de location de $2{,}50\text{ USD}$ par heure-GPU H100 (illustratif) ou via fournisseurs d'inférence de modèles ouverts à $\approx 0{,}80\text{ USD} / 10^6$ jetons (illustratif), le coût total de l'expérience décisive tranchant la Question 7 s'établit entre **$90\text{ USD}$ et $210\text{ USD}$** (illustratif) — soit quatre ordres de grandeur sous le coût des essaims massifs de septembre 2026 ($130 \times 10^9$ jetons pour Navier-Stokes, statut : RAPPORTÉ), tout en permettant une falsification statistiquement dotée dès la génération 2.

FIN-DE-CELLULE