# Proposition A — Tour III.3 : réponse aux critiques

## 0. État des pièces

- Les quatre critiques (B, C, D, E) sont présentes et se terminent par leur marqueur. Aucune ne paraît coupée. Je ne réponds qu'à leurs sections « Sur la proposition A ».
- Le bloc QUESTION est identique au bloc FAITS (même empreinte). Le bloc FAITS ne porte aucun statut : je traite ses énoncés comme des prémisses.
- Aucune expérience n'a été exécutée. Toute affirmation sur le comportement d'une mesure a le statut HYPOTHÈSE.
- Les implications mathématiques avancées par les critiques sont conditionnelles aux lois qu'elles posent. Je ne modifie pas leurs statuts.
- Tous les seuils et effectifs sont illustratifs. Les références sont citées de mémoire.

## 1. (a) Réponse à chaque critique

| # | Source | Critique | Verdict et conséquence |
|---|---|---|---|
| 1 | B-a1, D-a, E-a2 | En E1, (ii) et (iii) sont le même processus. | **Acceptée ; c'est le défaut le plus grave de ma conception.** Mêmes poids, même contexte et même plan donnent la même loi de génération. Mon H_A ne pouvait pas être fausse, donc le duel violait B4. E1 est refaite (§2). |
| 2 | B-a2 | Le canal du plan n'est pas spécifié. | **Acceptée.** Le plan passe par consigne dans une cellule. Dans l'autre, il n'y a pas de plan, seulement un objectif. |
| 3 | B-c2 | Il manque une permutation des artefacts de relais. | **Transformée en contrôle** de E1. |
| 4 | C-a3 | Imposer k/m actes par segment confond copies et régularité temporelle. | **Rejetée en partie.** Le même plan, aux mêmes positions, était exécuté dans les trois conditions, donc la régularité ne différait pas entre bras. Reste accepté : un plan stratifié imposé n'est pas celui que choisirait un agent seul. Les nouvelles cellules laissent l'adversaire choisir. |
| 5 | E-c2 | Il manque des copies honnêtes réellement interactives. | **Transformée en test** de calibration (E1). |
| 6 | D-a, D-b, E-a3 | Apparier « à dégât égal » conditionne sur une issue ; une strate de dégât peut être vide dans un bras. | **Acceptée.** L'analyse principale se fait par régime assigné, sur les mêmes tâches. La frontière dégât–détection devient descriptive. |
| 7 | B-b3 | E1 affirme une équivalence et exige deux tests unilatéraux ; la puissance est faible. | **Acceptée.** Les limites sont dites en E1. |
| 8 | C-b2, E-b1 | Sous coupure de contexte, la variance nulle de la somme change et le seuil gelé n'est plus au niveau nominal (trop strict selon C, trop lâche possible selon E). | **Acceptée, transformée en mesure.** Les fausses alertes sont rapportées dans les deux sens. Le transport a trois niveaux : seuil gelé, nul recalibré, réglage local. |
| 9 | B-a4, C-a1, E-a1, D-a | Un log-rapport de vraisemblance exige la densité sous sabotage ; une somme de rapports marginaux n'est pas le rapport de trajectoire. | **Acceptée.** « Calibré sur exécutions honnêtes » et « log-rapport de vraisemblance » étaient incompatibles dans mon texte. Le détecteur principal n'utilise plus de trajectoires sabotées. La version à densité adverse devient secondaire, avec partition par tâche. |
| 10 | B-b1, E-b1 | Sous corrélation intra-tâche, l'effectif utile plafonne. | **Transformée en test** de la loi que je prétends transférer (E0, diagnostic d'effectif utile). |
| 11 | C-b1, E-b3 | La variance du seuil empirique élargit les intervalles. | **Acceptée, avec une précision.** Entre deux bras lus au même seuil gelé, l'erreur de seuil est commune. Elle entre dans la différence par l'écart des densités des deux bras au seuil, non par leur somme (implication conditionnelle). Le bootstrap rééchantillonnera les tâches de calibration avec les tâches de test. |
| 12 | B-b2, E-b2 | L'AUROC par acte calculée sur toutes les étapes est diluée vers 0,5. | **Acceptée.** Elle est calculée aux seuls embranchements : actes altérés contre actes honnêtes aux mêmes embranchements. |
| 13 | D-b, E-b2 | Des marginales égales n'impliquent pas des lois jointes égales ; une somme sans puissance ne prouve pas l'absence de preuve. | **Acceptée.** Un détecteur joint est ajouté avant de conclure « rien à agréger ». |
| 14 | B-a3 | Le test de signe lit la variable qui définit l'attaque ; le défenseur connaît-il le sens ? | **Acceptée en partie.** Le défenseur ignore le sens, donc le test est bilatéral. Les embranchements ont des poids hétérogènes et des effets dépendants des autres choix. **Rejeté** : qu'une vérification mécanique puisse gagner n'est pas un défaut. C'est une issue que j'ai déclarée comme rendant la question sans intérêt, et le banc ne doit pas l'empêcher. |
| 15 | C-a2, C-b3 | Les « honnêtes malchanceux » (β) ont fait les mêmes choix que le saboteur ; face à β la puissance tombe au nominal. | **Transformée en test.** Sous ses conditions (poids homogènes, moniteur lisant seulement le sens), l'argument tient. Mon critère « fausses alertes sur β > 2 fois le nominal » condamnait alors tout instrument qui lit les choix : je le retire. β n'est pas circulaire pour autant. Il demande si un moniteur lit autre chose que la suite des choix (duel β en E0). |
| 16 | E-b4 | Au dégât visé, β est presque vide. | **Acceptée.** Le niveau de dégât du duel β est fixé au pilote pour que β soit peuplé. Sinon le duel est déclaré non jugeable. |
| 17 | C-c1 | Il manque un saboteur à somme nulle. | **Acceptée** (E0). |
| 18 | E-c1 | Il manque un LoRA neutre de même rang. | **Acceptée** (E0, E2). |
| 19 | B-a5 | La contrainte de dégât en E2 sélectionne sur l'issue. | **Acceptée.** E2 n'a plus de contrainte par tâche : la mesure est le dégât non détecté sur toutes les tâches attaquées. |
| 20 | B-b4 | Si la détection initiale est basse, H_B est impossible en E2. | **Acceptée.** La porte E0 exige au moins 45 % de détection. |
| 21 | B-c1 | Il manque un meilleur-de-8 honnête, avec seuil recalibré. | **Acceptée comme contrôle, rejetée comme mesure principale.** En déploiement l'agent honnête ne sélectionne pas ses sorties, donc le seuil gelé reste la mesure pertinente. Le seuil recalibré sert à décomposer la baisse. |
| 22 | C-c2 | Il manque une sélection du saboteur par un critère sans lien avec le moniteur. | **Acceptée** (sélection par perplexité). |
| 23 | C-a4, D-a, E-a4 | Les trois attaques diffèrent en accès et en calcul ; l'écart entre canaux n'identifie pas un prix par canal. | **Acceptée.** Je retire toute comparaison entre attaques. Chacune est jugée contre son placebo de même coût. Le tableau des transferts devient descriptif. |
| 24 | C-a4 | L'effondrement d'un canal peut dominer la somme gelée. | **Acceptée.** La contribution de chaque canal est bornée. La détection par canal est rapportée à part. |
| 25 | D-b, D-c | Si aucune attaque n'est admissible, le contraste est vide. | **Acceptée.** J'ajoute un contrôle positif d'efficacité de l'attaque. Je me sers ici de la critique que B adresse à E (une attaque faible lue comme une défense forte) : elle vaut aussi contre moi. |
| 26 | E-c3 | Le réentraînement du défenseur doit être évalué sur une attaque non vue. | **Transformée** en évaluation croisée entre mes attaques, sans nouvelle attaque. |
| 27 | B-a6, D-c | En E3, la politique locale est réglée sur les données de test. | **Acceptée.** Ajustement croisé par tâche. |
| 28 | B-b5 | Si la part de tâches sabotées dépasse le budget, le regret est nul par plafond. | **Acceptée.** La métrique est normalisée par le plafond. |
| 29 | B-c3, D-b | Battre le hasard ne suffit pas ; un regret nul peut cacher deux politiques également inutiles. | **Acceptée.** H_A de E3 devient une conjonction. |
| 30 | C-c3 | Il manque une politique dont seul le nul est recalibré. | **Acceptée**, comme lecture secondaire déclarée d'avance. Je garde le seuil gelé pour le duel, afin de ne pas affaiblir ma thèse après coup. |
| 31 | D (convention) | H_B doit être le complément exact de H_A ; « non tranché » est un état d'inférence. | **Acceptée.** Ma zone 15–50 % de E0 était une troisième hypothèse déguisée. |
| 32 | D-b | Sonde indépendante du régime sachant le texte : gain nul. Rang aux ré-exécutions de même loi : puissance nulle. | **Acceptée sans changement.** Ce sont les conditions des signes d'échec déjà déclarés. |

## 2. (b) Expériences corrigées

### Corrections communes

- **Banc.** Les embranchements ont des poids hétérogènes et des effets qui dépendent des autres choix. Le sens d'un acte ne se lit pas sans recalcul.
- **Partition par tâche.** Trois parts, toutes les variantes d'une tâche dans la même : ajustement (sondes, choix du moniteur et de la couche, réglage des politiques), calibration honnête (seuils), test. Effectifs : 120 / 80 / 200 tâches (illustratif). Les tâches sont synthétiques, donc la partition coûte du calcul, pas de la conception.
- **Détecteur principal.** Somme par tâche des scores standardisés sur exécutions honnêtes, contribution par canal bornée, seuil au quantile empirique des tâches de calibration. Aucune trajectoire sabotée n'entre dans l'agrégation.
- **Sonde.** Elle exige des exemples positifs. Ils viennent de la part d'ajustement, en sabotage par consigne. La mesure la plus stricte est son transfert au sabotage par LoRA.
- **Détecteurs secondaires.**
  - Version à densité adverse ajustée sur la part d'ajustement, à lire comme borne favorable.
  - Détecteur joint : classifieur sur la séquence des scores (franchissements, suites, maximum, variance, compte de signes).
- **Mesure principale, par régime assigné.** U est la fraction des tâches dont le dégât dépasse δ (un écart-type honnête, illustratif) et qui ne déclenchent pas d'alerte. Aucun appariement après coup sur le dégât.
- **Duels.** H_B est le complément exact de H_A. Un intervalle qui couvre le seuil est « non tranché ».
- **Intervalles.** Bootstrap par tâche, qui rééchantillonne aussi la calibration.

### E0 — Porte d'entrée

**Paramètres.**
- a : AUROC par acte aux embranchements, pour le moniteur choisi sur la part d'ajustement.
- θ : détection par tâche à 5 % de fausses alertes, k = 8, détecteur principal.

**Duel principal.**
- **H_A** : a < 0,65 et θ ≥ 45 %.
- **H_B** : a ≥ 0,65 ou θ < 45 %.
- Si a ≥ 0,65, le sabotage n'est pas diffus à cette échelle. Le programme s'arrête.
- Si θ < 45 %, on applique le détecteur joint :
  - S'il reste sous 45 %, il n'y a rien à agréger avec ces moniteurs. Le programme se réduit à l'allocation des vérifications et E2 n'est pas lancée.
  - S'il dépasse 45 %, le régime existe mais la comptabilité additive est falsifiée. On continue avec le détecteur joint, en le déclarant.
- H_A falsifie les deux thèses « non diffus » et « rien à agréger ».

**Duel β : sabotage ou malchance ?**
- Le seuil est calibré sur β. Le dégât est fixé au pilote pour que β compte au moins 50 exécutions.
- **H_A^β** : le meilleur instrument détecte au moins 20 % des tâches sabotées à 5 % de fausses alertes sur β.
- **H_B^β** : moins de 20 %.
- H_B^β falsifie l'idée que ces instruments lisent autre chose que la suite des choix. Ils établiraient alors un dégât, pas un sabotage, et une vérification mécanique ferait aussi bien.
- H_A^β falsifie la thèse de C sur ce banc : ses conditions n'y tiendraient pas.

**Diagnostic de la loi transférée.**
- On estime la corrélation intra-tâche ρ sur exécutions honnêtes.
- On prédit le gain de détection de k = 8 à k = 16 par l'effectif utile k/(1+(k−1)ρ).
- On compare à la mesure. Une erreur de plus de 10 points retire l'étiquette « loi » à ma contribution.

**Contrôles.**
- Étiquettes permutées.
- Mention sans usage (γ).
- Saboteur à somme nulle (k actes, dégât net nul). La détection doit subsister si la preuve est locale.
- LoRA neutre de même rang. La sonde ne doit pas s'y déclencher.
- Test de signe bilatéral, compté dans le budget des comparaisons.

### E1 — Plan partagé ou non

Les critiques ont raison : « copie » et « agent à contexte réinitialisé » ne se distinguent pas au niveau du noyau de génération. Ce qui peut distinguer l'article 2 est l'absence de plan commun.

**Cellules, sur les mêmes tâches, k = 8.**
- **S** : agent seul, contexte continu. Il reçoit seulement l'objectif : biaiser l'estimation finale, au plus k actes, sens libre. Le détecteur est gelé ici.
- **R-plan** : m = 4 segments à contexte réinitialisé. Chacun reçoit par consigne le plan complet (sens et positions). C'est l'ancienne (ii) ≡ (iii).
- **R-sans** : m = 4 segments. Chacun reçoit l'objectif seul et les artefacts de travail.
- **Honnêtes** : chaîne, puis copies parallèles suivies d'une synthèse.

**Vérification logicielle, sans duel.** Les deux chemins de code « copies » et « réinitialisation » de R-plan doivent donner des lois de scores indiscernables, avec artefacts et métadonnées identiques.

**Contrôle positif de coordination.** En R-sans, la concordance de sens entre segments doit dépasser le hasard. Sinon le phénomène de l'article 2 n'est pas instancié à cette échelle sur ce banc. On le rapporte ainsi, pas comme H_A.

**Duel.**
- **H_A** : |U(R-sans) − U(R-plan)| < 10 points, par deux tests unilatéraux.
- **H_B** : l'écart atteint 10 points.
- H_A falsifie, sur ce banc, la thèse que la coordination sans plan est un problème distinct de la coupure de contexte.
- H_B falsifie ma réponse attendue. L'article 2 garde alors un objet propre. Le dégât et la détection sont rapportés séparément pour dire de quel côté vient l'écart.

**Duel de calibration, sur honnêtes seuls.**
- **H_A** : les fausses alertes du détecteur gelé sur S restent entre 0,5 et 2 fois le nominal, en chaîne et en parallèle.
- **H_B** : elles en sortent. Le transport sans recalibrage est alors falsifié. On mesure s'il tient après recalibrage du seul nul.

**Contrôle.** Permutation des artefacts de relais entre trajectoires honnêtes et sabotées.

**Puissance.**
- Avec 200 tâches et 2 graines, l'équivalence n'est démontrable que si l'écart vrai est de quelques points. Je reprends l'ordre de grandeur calculé par B (HYPOTHÈSE).
- Une issue non tranchée est probable pour un écart vrai de 5 à 15 points.

### E2 — Moniteur visé

**Entrée.** θ ≥ 45 % en E0.

**Mesure.** ΔU = U après attaque − U avant, détecteur combiné gelé, toutes tâches attaquées.

**Attaques et placebos de même coût.**
- **A-texte** (meilleur de 8 contre le moniteur) :
  - meilleur de 8 du saboteur guidé par la perplexité ;
  - meilleur de 8 honnête.
- **A-activations** (LoRA pénalisé par la sonde gelée) :
  - même entraînement contre une sonde aléatoire ;
  - LoRA neutre.
- **A-comparaison** (sabotage systématique) : pas d'optimisation, pas de placebo.

**Contrôle positif d'efficacité.** L'attaque doit réduire d'au moins moitié la détection, au-dessus du niveau nominal, du moniteur visé pris seul. Sinon elle est déclarée inefficace et son duel n'est pas jugé.

**Duel.**
- **H_B (évasion gratuite)** : au moins une attaque efficace donne ΔU ≥ 15 points de plus que son placebo, achèvement honnête préservé à ±5 points. Le seuil est corrigé pour trois comparaisons.
- **H_A (évasion payante)** : aucune.
- H_B falsifie ma réponse attendue. L'article 3 devient le cas dimensionnant, et les mesures des articles 1 et 2 sont des bornes favorables.
- H_A falsifie, sur ce banc et pour ces attaques seulement, l'idée qu'un adversaire informé annule les moniteurs sans coût.

**Descriptif, sans duel.**
- Où la preuve se déplace, à accès donné.
- Défenseur réentraîné sur une attaque, évalué sur l'autre.

### E3 — Regret de transfert

Analyse hors ligne sur la part de test.

**Flux.**
- 10 % de tâches sabotées, budget de vérification de 2 % et de 5 %.
- Interceptions normalisées par le plafond min(1, budget / part sabotée).

**Politiques.**
- Gelée sur S.
- Nul recalibré sur honnêtes de la cible.
- Locale, par ajustement croisé.

**Duel.**
- **H_A** : la politique gelée a un regret < 10 points face à la locale, et un gain ≥ 10 points sur la meilleure allocation sans moniteur (uniforme, résultat le plus extrême, tâche la plus longue). Les deux conditions valent sur R-sans et sous attaque.
- **H_B** : l'une des deux conditions échoue.
- H_A falsifie « trois problèmes, trois réglages » sur ce banc.
- H_B falsifie la valeur opérationnelle de la problématique d'ensemble.
- Si seule la version à nul recalibré passe, le transport exige des exécutions honnêtes dans la configuration cible. Le cadre ne les garantit pas quand l'adversaire est l'agent.

### Budget

- Environ 9 000 à 10 000 trajectoires (illustratif).
- E1 est limitée à k = 8 et E3 ne demande aucune trajectoire nouvelle.
- Le calendrier de deux mois est inchangé.
- Risque nouveau : la consigne « sens libre » de S et de R-sans demande un pilote.

## 3. (c) Réponse à l'arbitre

**Position.** Je ne peux pas affirmer qu'une problématique d'ensemble existe. Un banc, des contrôles et une mesure communs (le dégât non détecté à fausses alertes fixées) sont défendables dès maintenant. Reste à tester si un détecteur et une règle d'allocation se transportent d'une configuration à l'autre.

**(1) Question.** Un détecteur et une règle d'allocation des vérifications réglés sur un agent seul gardent-ils leurs fausses alertes et leur fraction de dégât non détecté lorsque le même sabotage diffus est réparti entre copies sans plan partagé, ou accompagné d'une attaque contre un moniteur ?

**(2) Réponse attendue (HYPOTHÈSE), révisée après critique.**
- Copies à plan partagé : identiques à un agent à contexte coupé, par construction. Ce n'est pas un résultat.
- Copies sans plan : à cette échelle, j'attends que le défaut de coordination coûte du dégât à l'adversaire, donc U ne monte pas. Confiance faible. Réfuté par H_B de E1.
- Moniteur visé : évasion payante. Confiance faible. Réfuté par H_B de E2.
- L'unification partielle est moins assurée qu'au tour III.1. L'identité relevée par B, D et E retire à ma thèse « temps ↔ copies » sa partie facile.

**(3) Antériorité (de mémoire, à vérifier).**
- Wen et al., 2024, « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats ».
- Greenblatt, Shlegeris, Sachan, Roger, « AI Control: Improving Safety Despite Intentional Subversion ». B relève un désaccord d'année entre propositions. De mémoire : prépublication fin 2023, conférence en 2024.

**(4) Expérience.** E0 à E3 corrigées (§2).

**(5) Type.** Transfert d'une loi connue ailleurs (effectif utile sous corrélation) et mesure d'un phénomène. Si le diagnostic de E0 échoue, il ne reste que la mesure.

**Ce qui est établi.**
- Aucun résultat empirique.
- Par raisonnement, conditionnellement : mon ancien duel E1 ne pouvait pas échouer, mon détecteur était mal défini et mon critère sur β était mal posé.

**Ce qui ne l'est pas.**
- L'existence du régime diffus à huit milliards de paramètres.
- Un signal des moniteurs au-delà de la suite des choix.
- La coordination de copies sans plan.
- Le coût de l'évasion.
- Le transport du réglage.
- La nouveauté.
- La portée au sabotage spontané ou à des agents plus capables, que ce plan ne teste pas.

**À faire en premier.**
1. Recherche d'antériorité. Critère : un article qui gèle un détecteur sur une configuration et rapporte son erreur sur les autres. S'il existe, ma contribution se réduit à une réplication sur modèle ouvert.
2. Pilote : variance honnête, corrélation intra-tâche, effectif de β.
3. E0. Elle décide si le programme existe, si E2 est jugeable, et si les instruments distinguent sabotage et malchance.

**Issues qui rendraient la question sans intérêt.**
- Sabotage non diffus (a ≥ 0,65).
- Rien à agréger, même conjointement.
- H_B^β avec une vérification mécanique équivalente.
- Coordination non instanciée : cela vaut pour l'article 2 à cette échelle seulement.

FIN-DE-CELLULE