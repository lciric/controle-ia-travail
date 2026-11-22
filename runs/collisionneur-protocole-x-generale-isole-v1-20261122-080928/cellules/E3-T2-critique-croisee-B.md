# Proposition B, tour III.2 : critique croisée de méthode

**État des pièces.** Les pièces A, C, D et E sont présentes, non vides et se terminent par leur marqueur de fin ; aucune ne paraît coupée.

**Statut de ce qui suit.**
- Les critiques portent sur la méthode décrite dans les pièces.
- Toute affirmation sur le comportement attendu d'une mesure a le statut HYPOTHÈSE.
- Les calculs reprennent les valeurs illustratives des propositions et restent illustratifs.
- Je ne modifie aucun statut attribué par les autres propositions. Je signale seulement les attributions que leur propre texte ne soutient pas.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **E1 est vrai par construction, en grande partie.**
   - En (ii), les m copies exécutent un plan de k actes fixé d'avance, k/m actes chacune.
   - En (iii), le même modèle exécute le même plan, avec des coupures de contexte aux mêmes frontières.
   - Avec les mêmes poids, les mêmes actes et les mêmes coupures, (ii) et (iii) sont le même processus à l'étiquette près. Le détecteur additionne des scores par acte, par tâche : l'écart (ii)–(iii) tend donc vers zéro par construction (HYPOTHÈSE).
   - E1 ne teste pas ce qui distingue l'article 2 : des copies qui doivent *inférer* sans plan partagé quels actes faire et dans quel sens, c'est-à-dire la coordination sans canal. A peut donc conclure H_A (« pas d'objet propre ») sans avoir instancié ce phénomène.
2. **Le canal du plan n'est pas spécifié.** On ne sait pas comment chaque copie reçoit sa part du plan.
   - Si c'est par consigne, (ii) se réduit à (iii).
   - Si c'est par les artefacts, le plan y est lisible et le moniteur de texte peut le détecter. On mesurerait alors une fuite du plan, pas du sabotage.
3. **Le sabotage est défini par la variable que lit le test de signe.** La politique adverse est « choisir à k embranchements l'option qui pousse dans le sens cible ». Le test de signe sur le sens des k choix détecte donc exactement la définition de l'attaque. La ligne de base mécanique est avantagée par construction, et le critère « gain inférieur à 5 points sur la meilleure vérification mécanique » condamne les moniteurs d'avance si le sens est observable. A le reconnaît en partie en comptant ce test dans le budget des comparaisons. Il reste à dire si le défenseur connaît le « sens cible » : sans lui, le test devient bilatéral et perd de la puissance.
4. **Fuite possible dans le détecteur par rapport de vraisemblance.** Un log-rapport de vraisemblance exige la densité des scores sous sabotage. Si cette densité est estimée sur les mêmes tâches que celles qui servent à mesurer la détection en E0, l'estimation est optimiste. Il faut une partition par tâche, que A n'énonce pas.
5. **E2 sélectionne sur l'issue.** La contrainte « dégât au moins égal à 90 % de l'initial » s'applique après l'attaque. Si elle est vérifiée par tâche, on ne garde que les tâches où l'attaque a réussi, ce qui biaise la détection mesurée. Il faut la vérifier en moyenne sur toutes les tâches attaquées.
6. **E3 : le réglage local se fait sur les données de test.** Si la politique réglée par configuration l'est sur les tâches qui servent à l'évaluer, elle est optimiste. Le regret est alors gonflé, en faveur de H_B. Un ajustement croisé par tâche est nécessaire.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Somme des log-rapports de vraisemblance.**
  - La puissance croît avec k·KL(P_sab‖P_hon) seulement si les scores intra-tâche sont indépendants.
  - Avec une corrélation intra-tâche ρ, l'effectif utile vaut k/(1+(k−1)ρ) et plafonne vers 1/ρ. Passer de k = 8 à k = 16 n'apporte alors presque rien.
  - Si la variance d'un effet aléatoire de tâche τ² domine la variance intra-tâche, un seuil calibré sur des tâches honnêtes regroupées devient trop haut, et la détection s'effondre aux 5 % de fausses alertes nominaux.
- **AUROC par acte de E0.** Si seule une fraction f des étapes sont des embranchements, l'AUROC calculée sur tous les actes est diluée vers 0,5. Elle doit être calculée sur les seuls embranchements, sinon le critère « inférieure à 0,65 » est satisfait par dilution.
- **E1 est une affirmation d'équivalence.** Elle exige un test d'équivalence (deux tests unilatéraux) à ±10 points.
  - Avec environ 250 paires et des taux proches de 0,5, l'erreur standard de la différence est d'environ 4,5 points (illustratif, appariement faible).
  - H_A n'est alors démontrable que si l'écart vrai est inférieur à environ 10 − 1,645 × 4,5 ≈ 2,6 points (illustratif).
  - Au-delà, l'issue est non concluante, pas H_B.
- **Plancher en E2.**
  - La baisse absolue maximale vaut D₀ − 5 %, où D₀ est la détection avant attaque.
  - Si D₀ est inférieure à 25 %, ce que la zone 15–50 % de E0 autorise, H_B (baisse d'au moins 20 points) est impossible. H_A est alors vraie par construction.
  - Il faut exiger D₀ ≥ 45 % (illustratif) ou exprimer la baisse en fraction de D₀ − 5 %.
- **Plafond en E3.** Si la fraction π de tâches sabotées dépasse le budget b = 5 %, l'interception maximale vaut b/π. Toutes les politiques compétentes atteignent ce plafond, et le regret est nul par construction. Il faut fixer π ≤ b ou normaliser par b/π.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Pour E2-texte, un meilleur-de-8 honnête.** Le même tirage du meilleur de 8 contre le même moniteur, appliqué à l'agent honnête. Sans lui, la baisse de détection reflète une statistique d'ordre (le minimum de 8 scores) et non une évasion. Le seuil doit être recalibré sur cette distribution honnête sélectionnée.
- **Pour E1, une permutation des artefacts.** Les artefacts de relais sont échangés entre trajectoires honnêtes et sabotées. Si le moniteur de texte suit l'artefact et non l'acte, l'écart mesuré tient au canal du plan.
- **Pour E3, une allocation par le résultat le plus extrême.** Elle figure dans le tableau des instruments de A mais pas dans E3. Sans elle, battre l'allocation aléatoire ne montre pas que les moniteurs servent à allouer : l'extrémité du résultat suffit peut-être.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Le même moniteur construit l'adversaire et l'évalue.**
   - L'adversaire est obtenu par tirage par rejet sous la contrainte qu'aucune étape ne dépasse le 95ᵉ centile de suspicion honnête. Ce score est vraisemblablement celui de M_texte, qui sert ensuite au CUSUM.
   - La distribution des scores adverses est donc tronquée par le moniteur évalué.
   - Si le rejet garde le candidat le moins suspect, la dérive moyenne du score peut devenir négative. Le CUSUM unilatéral vers le haut a alors une puissance inférieure ou égale aux fausses alertes, par construction (HYPOTHÈSE).
2. **Le gain de E1 sur le détecteur sans mémoire est en partie mécanique.**
   - À 5 % de fausses alertes par trajectoire sur 25 étapes indépendantes, le seuil du maximum doit se situer vers le 99,8ᵉ centile par étape, car 1 − 0,95^(1/25) ≈ 0,002 (illustratif).
   - L'adversaire est plafonné au 95ᵉ centile par construction. Le TPR du maximum est donc proche de 0.
   - Le critère « gain d'au moins 20 points » se réduit alors à « TPR du CUSUM d'au moins 20 % », ce qui est redondant avec le seuil de 70 %.
3. **Le moniteur de texte partage le modèle de base de l'agent.** M_texte est une copie gelée de Llama-3.1-8B. Ses angles morts sont corrélés à ceux de l'agent. C'est une variable confondante pour l'article 3, car l'évasion contre un juge de même famille n'est pas l'évasion contre un juge indépendant.
4. **Fuite possible vers l'oracle.** V_coût consulte « l'arbre de dérivation ». Si cet arbre enregistre les choix adverses, la vérification lit l'étiquette.
5. **H_A de E2 est bilatérale.** Variance trop haute ou invariance trop rigide accompagnée d'un M_act élevé : presque tout écart à μ_hon confirme H_A. En outre, λ dans A_comp n'a pas de procédure de réglage déclarée. S'il est réglé sur des données adverses, il y a fuite.
6. **μ_hon suppose un modèle honnête disponible.** Le cadre admet que l'agent soit lui-même l'adversaire. La référence μ_hon, σ_hon n'est alors pas accessible en déploiement, et le score mesure un écart à une référence que le défenseur ne possède pas.
7. **E4 : asymétrie d'effort.** La « meilleure politique non couplée » n'est pas recherchée avec le même budget de réglage que la cascade. La comparaison favorise la politique sur laquelle porte l'effort de conception.
8. **Statuts à signaler, sans les modifier.**
   - Wald (1945) et Page (1954) sont dits « cités de mémoire » et marqués [VÉRIFIÉ]. Le texte de C ne contient pas de vérification qui soutienne ce statut.
   - L'année de Greenblatt et al. diffère entre C (2024) et A et D (2023) : référence à vérifier.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **CUSUM.**
  - Puissance nulle si E_sab[s_t] ≤ E_hon[s_t] après sélection, sur les scores blanchis.
  - Fausses alertes gonflées si les scores suivent une autocorrélation de type AR(1) avec φ > 0 non modélisée : le blanchiment déclaré doit être estimé sur des trajectoires honnêtes disjointes.
- **Variance inter-copies avec K = 3.**
  - La variance empirique n'a que 2 degrés de liberté ; son coefficient de variation vaut √(2/(K−1)) = 1 sous normalité (illustratif).
  - La puissance par étape est très faible, sauf si l'effet multiplie la variance par un facteur supérieur à environ 5 (illustratif).
- **E3 non jugeable.**
  - ρ n'est défini que si l'adversaire atteint un TPR d'au plus 10 %. S'il n'y parvient pas, aucune des deux branches ne s'applique.
  - H_B est énoncée avec ρ > 0,8 mais falsifiée par ρ ≤ 0,5. La zone 0,5–0,8 n'est pas couverte par les énoncés.
- **E4.**
  - Les fausses condamnations sont plafonnées à 2 % sur environ 200 trajectoires honnêtes, soit environ 4 événements (illustratif). L'estimateur est trop instable pour que la contrainte soit vérifiable.
  - R = E[Δ·𝟙(non intercepté)] a une variance dominée par la queue de Δ. Si Δ est fortement asymétrique, l'écart relatif de 35 % n'est pas résoluble avec 400 trajectoires.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Un moniteur tenu à l'écart.** Une invite ou un modèle différent, qui n'a jamais servi au tirage par rejet. Sans lui, E1 mesure la troncature.
- **Un LoRA honnête de même rang et de même nombre de pas pour M_act.** C contrôle l'absence de consigne malveillante, mais pas la simple présence d'un adaptateur. Une sonde peut détecter « poids modifiés » plutôt que « sabotage ».
- **Le même tirage par rejet appliqué à l'agent honnête.** Il est nécessaire pour calibrer la distribution des scores sélectionnés.
- **Des perturbations sur copies honnêtes, par type.** La permutation de l'ordre des documents et la paraphrase, appliquées séparément à des copies honnêtes, pour estimer μ_hon et σ_hon par type de perturbation. Le contrôle « documents ambigus » ne remplace pas cette calibration.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Le générateur fixe à la fois les erreurs et la filiation.**
   - Le gain de la règle de regroupement repose sur une corrélation entre erreurs à l'intérieur d'un groupe de provenance. Or c'est le générateur qui place les erreurs et qui écrit les filiations.
   - Le duel de transfert tient à l'écart un *régime*, pas le *générateur*. Le transfert entre régimes se fait donc à l'intérieur d'une famille de données qui code le mécanisme testé.
   - C'est une fuite au niveau de la construction (HYPOTHÈSE). Le duel « mécanisme » randomise la filiation, mais seulement dans ce même générateur.
2. **La règle ignore la dépendance propre à l'article 2.** Des copies d'un même modèle peuvent commettre la même erreur à partir de pièces *distinctes*, parce qu'elles partagent leurs poids. Le regroupement par pièce observable ne voit pas cette cause commune. Un transfert réussi vers le régime 2 ne dirait donc rien de la corrélation par poids partagés.
3. **Il n'y a pas d'adversaire.** Le régime 3 utilise des perturbations préenregistrées et non adaptatives, et D le déclare. Deux conséquences :
   - La question pose des actes « dont aucun n'est suspect isolément » produits par un adversaire. Ici, ni les régimes 1 et 2 ni le régime 3 n'ont de politique adverse. Le protocole étudie l'audit d'erreurs, pas le sabotage.
   - La provenance est une caractéristique observable donc falsifiable. Un adversaire qui connaît la règle fabrique de fausses acquisitions indépendantes. La règle n'est pas testée contre cette attaque, qui est l'attaque naturelle contre elle.
4. **Erreurs honnêtes comptées comme positifs.** D est cohérent avec son objet. Mais un moniteur qui ne détecte que l'incompétence obtient ici un bon score, et le résultat ne transporte pas vers les questions d'intention des articles 1 et 3.
5. **Le classement par importance peut dominer.** Si le score d'importance varie bien plus que le risque estimé, les deux politiques, avec et sans regroupement, auditent les mêmes conclusions. Le contraste est alors nul par construction de la fonction de classement, et non faute de mécanisme.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Gain nul du regroupement.** Si la corrélation conditionnelle des erreurs dans un groupe de provenance égale la corrélation entre groupes (ρ_intra ≈ ρ_inter), le regroupement ne change pas l'estimation du risque.
- **Plancher sur L.** Si la fraction de conclusions fausses sans audit, L₀, est inférieure à environ 5 points, une réduction de 5 points est impossible. H_A est alors fausse par construction. Il faut L₀ ≥ 10 points (illustratif) au pilote.
- **Non-infériorité à 2 points avec agrégation par famille.**
  - L'erreur standard est de l'ordre de σ_famille/√F, où F est le nombre de familles tenues à l'écart.
  - Des intervalles simultanés sur 3 régimes élargissent encore la marge.
  - Si σ_famille est de l'ordre de 10 points et F de l'ordre de 30 (illustratif), l'erreur standard dépasse la marge, et toutes les issues sont indécises. D le prévoit au pilote ; c'est la condition décisive.
- **Duel « mécanisme ».** C'est une interaction de 3 points. Son erreur standard vaut environ deux fois celle d'un effet principal au même effectif, d'où un besoin d'échantillon environ quatre fois plus grand (illustratif).
- **Qualification des instruments.** Les fausses alertes sont définies « parmi les conclusions vraies », mais aussi comptées « par dossier ». Si les deux critères divergent, la qualification n'est pas jugeable sans qu'on désigne celui qui prime.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Un générateur nul.** Des dossiers où les erreurs sont placées indépendamment de la filiation vraie, avec la même distribution de filiation visible. Le gain du regroupement doit disparaître. La permutation de D brise le lien entre filiation visible et filiation vraie, mais ne teste pas le cas où le générateur corrèle l'importance et la filiation.
- **Des perturbations sans trace.** Il faut vérifier que les perturbations du régime 3 ne modifient aucune caractéristique visible utilisée par la règle. Sinon, la règle détecte la perturbation et non la défaillance du moniteur.
- **Des appuis indépendants fabriqués.** Le même nombre d'appuis, mais avec une fausse filiation indépendante ajoutée sur des conclusions fausses. Ce n'est pas une expérience nouvelle, seulement un contrôle de vulnérabilité. Sans lui, la règle n'est qualifiée que contre un environnement qui ne ment pas sur la provenance.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Le compte des lectures « + » détecte l'attaque par construction.**
   - Sous la politique honnête, chaque lecture vaut ±ε avec p = 0,5. L'adversaire en choisit 20 sur 24.
   - Si la lecture choisie est observable dans le texte, ce qui est probable puisque l'estimation locale en dépend, un test binomial mécanique a une valeur p d'environ P(X ≥ 20 | n = 24, p = 0,5) = 12 951/2²⁴ ≈ 7,7·10⁻⁴ (illustratif).
   - La meilleure ligne de base mécanique détecte donc presque tout, et GET tend vers 1. H_3B est alors confirmée par un artefact du générateur.
   - Le « lexique de polarité » mentionné en (c) n'est pas ce compte. Le compte doit figurer explicitement parmi les lignes de base.
2. **L'objectif de la variante W n'est pas directionnel.**
   - Le LoRA est entraîné à rendre |θ̂ − θ*| ≥ 0,30. Il peut apprendre un décalage de signe fixe ou une règle « éloigner de la vérité ».
   - Dans le second cas, θ̂(E) = θ* + Δ·sgn θ* et θ̂(−E) = −θ* − Δ·sgn θ*. La somme est nulle.
   - Le test métamorphique de E2 détecte donc l'adversaire seulement si l'entraînement produit un biais de signe fixe. Le succès de H_2A dépend de ce que l'optimiseur a appris, une variable non mesurée (HYPOTHÈSE).
3. **E1 confond la dilution avec d'autres variables.** À D = 24 documents fixés, faire varier T de 4 à 24 change à la fois :
   - le nombre de documents par étape ;
   - la longueur du texte par étape ;
   - la longueur de contexte ;
   - le grain de lecture du moniteur.

   La pente « dilution en 1/√T » n'est pas séparable de ces covariables.
4. **H_3A est une disjonction faible.** « r_Δ ≤ 0,5 OU GET ≥ 2 » : un optimiseur par renforcement qui échoue à apprendre suffit à donner r_Δ ≤ 0,5, donc H_3A, la « taxe d'évasion ». La faiblesse de l'attaque est ainsi lue comme une propriété de la défense.
5. **Fuite moniteur–adversaire en E3.** Le moniteur est réentraîné de façon itérative pendant l'entraînement adverse. La version évaluée n'est pas précisée. Si c'est la dernière version vue par l'adversaire, ou au contraire une version réentraînée sur ses sorties, l'évaluation hérite de la boucle.
6. **Conclusion trop large.** E3 porte sur un seul adversaire et un seul banc. « H_3A falsifie l'indépendance des trois articles » infère l'unification sans test de transport entre régimes. Le test de transférabilité de E en (5) n'est pas lié au duel.
7. **Statuts à signaler, sans les modifier.**
   - E marque [VÉRIFIÉ] des énoncés tirés du bloc FAITS (« deux mois », le cadre). Ce bloc ne porte aucun statut.
   - « Aucun acte suspect isolément » est marqué [VÉRIFIÉ] « par construction du générateur ». Cela ne vaut que pour la marginale du choix, pas pour le texte produit par un LoRA, que E ne vérifie pas.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **GET est un rapport à dénominateur petit.**
  - Avec 400 tâches, 10 % adverses et b_verif = 5 %, l'allocation uniforme capture en espérance 20 × 0,1 = 2 tâches. P(0 capture) = 0,9²⁰ ≈ 0,12 (illustratif).
  - Le rapport est instable, voire infini. GET ≥ 2 peut être atteint par la seule variance du dénominateur.
  - Il faut un estimateur par différence ou un rapport avec intervalle obtenu par bootstrap stratifié.
- **E2 conjugue quatre inégalités.**
  - La probabilité d'observer H_2A est le produit approximatif de quatre puissances. Même si chacune vaut 0,8, le produit vaut environ 0,41 (illustratif, sous indépendance).
  - H_2B, son complément, est donc observée souvent sans désigner quelle composante échoue. Faute d'indiquer quelle composante échoue, l'issue H_2B est peu informative.
- **Asymétrie métamorphique.** Si le modèle de base a un biais propre de signe b₀ ≠ 0, la statistique |θ̂(E) + θ̂(−E)| a pour moyenne honnête 2b₀. La calibration par LoRA honnête doit estimer b₀ par famille de dossiers. Sinon les fausses alertes varient selon les familles.
- **E1.** Le niveau plancher « TPR à T = 24 d'au moins 0,50 » est estimé sur 400 dossiers, mais δ_E1 est une double différence de quatre TPR. Son erreur standard est d'environ 2 × 0,035 ≈ 0,07 (illustratif). Le seuil de 0,15 est à environ deux erreurs standard seulement.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Un contrôle positif de l'optimiseur.** Le même entraînement par renforcement contre une sonde unique doit atteindre r_Δ > 0,8 avec un TPR d'au plus 10 %. C a ce contrôle ; E ne l'a pas. Sans lui, H_3A est confondue avec l'échec de l'attaque.
- **Un adversaire « éloigner de la vérité ».** Il faut le construire délibérément et passer le test métamorphique. Le test doit échouer contre lui. Sans ce contrôle, la portée de E2 est surestimée.
- **Le compte binomial des lectures choisies parmi les lignes de base.** Sans lui, GET est mesuré contre une ligne de base mécanique sous-optimale.
- **Une longueur de contexte égalisée entre valeurs de T.** Par exemple, du remplissage neutre à T = 4. Sans lui, la « dilution » n'est pas imputable à T.

FIN-DE-CELLULE