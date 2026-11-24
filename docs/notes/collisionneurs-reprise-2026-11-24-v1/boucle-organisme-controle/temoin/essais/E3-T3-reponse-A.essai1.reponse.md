# Proposition A, tour III.3 : réponse aux critiques

**Préalables.**
- Les pièces transmises sont présentes et complètes : FAITS, QUESTION, ma conception III.1, la critique de B et la critique de C. Je n'ai pas vérifié les empreintes sha256.
- Je ne réponds qu'aux sections « Sur la proposition A ».
- **Statuts.** Les faits restent RAPPORTÉ. Mes dispositifs restent HYPOTHÈSE. Les énoncés mathématiques que B ou C marquent VÉRIFIÉ gardent ce statut, noté « VÉRIFIÉ (selon B) » ou « VÉRIFIÉ (selon C) ». Quand j'ai refait un calcul, je le signale sans rien modifier.
- **Notation.** B-a2 désigne le point 2 de la section (a) de la critique de B, C-c3 le point 3 de la section (c) de C, et ainsi de suite. Les critiques identiques sont regroupées.

---

## (a) Verdict sur chaque critique

### Architecture de la boucle

| Critique | Verdict | Raison, ou test qui la remplace |
|---|---|---|
| **B-a1, C-a3.** Le « bit de retour » est une fonction mesurable de scores de moniteurs ; « The Ladder » est hors domaine | **Acceptée** | Le bit est supprimé. La citation de Blum et Hardt (2015) est retirée : elle protège la réutilisation d'une *même* réserve, pas l'adaptation d'un proposeur sur des familles successives. Correction architecturale : les cartes-problèmes de **tous** les cycles sont gelées par empreinte **avant la première lecture**. Aucun résultat de lecture ne remonte vers l'organisme, ni directement ni par réécriture humaine. Limite résiduelle reconnue : les humains qui ont vu les résultats rédigeront la feuille de route suivante. Ce canal est journalisé ; il n'est pas borné. |
| **B-a2 (1ʳᵉ partie), B-c4 (1ʳᵉ partie).** Si les mêmes personnes écrivent les « hypothèses admises » des cartes et les lois plantées, l'adéquation est vraie par construction | **Transformée en test** (E1a) | Les mondes d'épreuve viennent de deux sources : des auteurs ayant vu les cartes, et une instance aveugle aux cartes qui ne reçoit qu'une spécification plus large (classe de menace, sans hypothèses admises). Un gain présent seulement sur la première source signe un artefact de construction. |
| **B-a2 (2ᵉ partie).** Passer directement du processeur à la lecture GPU gaspille une famille | **Acceptée, avec garde-fous** | J'ajoute une étape sur **traces honnêtes réelles de 8B seulement** (E5), qui ne consomme aucune famille de sabotage. J'y reprends, en le disant, la critique que B adresse à C (survie des détecteurs dégénérés). Cette étape comprend donc une sonde placebo, qui projette sur un sous-espace aléatoire, et une exigence de discrimination entre tâches honnêtes de complexité distincte. |
| **B-a3, C-a1.** Mon critère 3 confond « loi présente dans l'archive » et « statistique archivée optimale » | **Acceptée** | Le critère est faux tel qu'écrit. Je le remplace par deux contrôles distincts. (i) **Plafond oracle** : sur un monde à loi connue, le test du rapport de vraisemblance qui connaît cette loi borne la puissance à niveau fixé (Neyman et Pearson, 1933, pour une hypothèse simple contre une simple). Un dépassement au-delà de l'erreur Monte-Carlo signale un bogue ou une fuite. Comme C le note, c'est un contrôle de sanité, pas une preuve. (ii) Un gain sur le recombinant d'archive pour une loi archivée est rapporté comme **gain d'efficacité**, compté à part des **découvertes**. |
| **C-a2, C-c1.** Gain « au-delà de l'archive » confondu avec le rappel par le modèle pré-entraîné de méthodes absentes de l'archive locale ; les mêmes concepteurs font les cartes et l'archive | **Transformée en test** (E1b) | Trois mesures : archive étendue par un **tiers indépendant**, bras « modèle pré-entraîné seul » (sans graphe ni carte), mondes isomorphes reparamétrés. J'ajoute une distinction absente de C. Récupérer une méthode connue mais oubliée peut être **utile** au programme de contrôle sans être une **découverte** de l'organisme. Les deux comptes sont tenus séparément. Une recherche bibliographique négative établit seulement « non retrouvée », jamais « nouvelle ». |
| **C-b1 (3ᵉ puce).** Malédiction du vainqueur | **Partiellement rejetée** | Si les mondes d'épreuve sont tirés indépendamment de la sélection, l'estimation sur ces mondes est sans biais pour le candidat retenu. Le biais résiduel tient au **générateur partagé**, ce qui ramène à B-a2 : les mondes d'épreuve viennent d'un auteur distinct. |

### Étanchéité (E3)

| Critique | Verdict | Raison, ou test qui la remplace |
|---|---|---|
| **B-a5a, C-a4, B-b3, C-b3, B-c3, C-c2.** Un canari lexical ne détecte qu'une copie littérale ; l'absence d'excès ne réfute pas H_B ; le contrôle positif est circulaire | **Acceptée sur le fond** | E3 ne peut pas établir l'étanchéité en général. Je le reformule **canal par canal** : lexical, géométrique (direction plantée, proposition de B) et paramétrique (exposant de queue ou autocorrélation propre à la famille, proposition de C). Chaque canal a son contrôle positif, qui fixe la taille de fuite détectable. Le canari géométrique ne s'applique qu'aux candidats qui portent une direction ou une projection. L'étanchéité repose d'abord sur un **audit de provenance** (qui a vu quoi, quand), vérifié par un tiers. Les canaris contrôlent l'audit ; ils ne le remplacent pas. |

### Pont processeur → GPU (E4)

| Critique | Verdict | Raison, ou test qui la remplace |
|---|---|---|
| **B-a5b, C-a5b, B-b4, C-b4, B-c1, C-c3(i).** Les candidats mal classés gonflent la corrélation de Spearman (mélange bimodal) | **Acceptée** | J'avais traité la restriction de plage et créé l'artefact inverse. La décision qui compte est de savoir si le proxy ordonne les candidats **viables**. Le test décisif porte donc sur la strate des candidats valides ; la plage complète n'est que descriptive. |
| **B-b4 (permutations).** Seuil inatteignable si m! < 1/α | **Rejetée comme objection contraignante** | Avec α = 0,05, la contrainte ne joue que pour m ≤ 3 (1/4! ≈ 0,042). La vraie contrainte est la puissance, qui s'effondre quand \|ρ\| ≲ z/√(K−1) (C-b4). Je la retiens. |
| **C-a5a.** Pseudoréplication sur une seule famille | **Acceptée** | La conclusion d'E4 est **conditionnelle à la famille lue**. La généraliser exige au moins deux familles. Je ne sais pas si le budget le permet. |
| **C-a5c, C-c3(ii).** Calibration confondante : un candidat qui fausse plus d'alertes « détecte » plus | **Acceptée** | La détection GPU se mesure à taux de fausses alertes **égal**, étalonné sur traces honnêtes GPU (E5). |
| **C-a5c.** Le proxy aléatoire est redondant avec le test de permutation | **Acceptée** | Il est remplacé par des **proxys mécaniques** : validité syntaxique seule (proposition de B), et puissance sur un monde archivé élémentaire. |

### Nul par acte (E2)

| Critique | Verdict | Raison, ou test qui la remplace |
|---|---|---|
| **B-b1 (1ʳᵉ puce), C-b2 (1ʳᵉ), C-a6a.** Sans échangeabilité conditionnelle, la garantie tombe ; le simulateur dicte l'issue | **Acceptée** | J'utilise aussi, en le disant, la remarque de C sur B : une espérance arithmétique supérieure à 1 suffit à perdre la garantie de Ville, mais c'est l'espérance logarithmique qui commande la divergence presque sûre. E2a ne tranche donc pas la validité réelle. Il cartographie une **tolérance** : le décalage maximal ε_max entre le processus réel et le processus de référence que chaque construction supporte. Le décalage réel se mesure à part, sur traces 8B honnêtes (E5). |
| **B-b1 (2ᵉ puce), C-b2 (2ᵉ).** Troncature : ê_t ≤ k+1 | **Acceptée, portée précisée** | J'ai refait le calcul et j'obtiens la même borne. Elle impose T ≥ log(1/α)/log(k+1). Exemple illustratif : α = 0,01 et k = 19 donnent T ≥ 1,54, donc 2 actes. Pour des menaces diffuses sur de longs horizons, cette borne ne contraint pas. La condition qui contraint vraiment est celle de C : une espérance sous H₁ de log f(p_t) inférieure ou égale à 0. Elle devient une ligne de la grille d'E2a. |
| **B-b1 (3ᵉ puce).** Alternative locale en O(T^(−1/2−η)) : puissance nulle | **Rejetée comme critique de ma base** | C'est une limite informationnelle qui vaut pour **toute** procédure, comme le montre le même argument de type Pinsker chez C (C-b5). Elle ne départage pas les candidats. Je la garde pour définir la **zone détectable** : les mondes situés sous ce seuil servent de quasi-nuls. |
| **B-a4 (historique contaminé).** | **Partiellement rejetée, transformée en test** | Sous H₀, l'historique est honnête : la validité n'est pas touchée. Sous H₁, une référence conditionnée sur un historique déjà saboté peut reproduire le sabotage et faire perdre de la puissance. E2a compare donc une référence conditionnée sur l'historique complet et une référence à fenêtre tronquée. |
| **B-a4 (consigne système), B-c2.** Un agent honnête porteur d'une consigne privée bénigne n'est pas échangeable avec la référence | **Transformée en contrôle obligatoire** (E5) | Ce point est juste et je ne l'avais pas vu. |
| **C-b2 (3ᵉ puce).** Le plafond peut ne pas apparaître si le signal est fort | **Acceptée** | La grille d'amplitudes inclut des signaux dont la détection sur référence fixe exige plus de N_réf actes. |

### Inférence forte, niveau et multiplicité

| Critique | Verdict | Raison, ou test qui la remplace |
|---|---|---|
| **C-a6c.** Issue orpheline dans E1 ; conjonction dans E2 | **Acceptée** | E1 est scindé en E1a et E1b, E2 en E2a et E2b. Chaque expérience a un seul seuil. |
| **C-a6b, C-b1 (2ᵉ puce).** Marge de type I ad hoc | **Acceptée** | La marge est supprimée. Critère : borne supérieure unilatérale exacte de Clopper-Pearson ≤ α. N₀ est dimensionné par la formule de B (B-b1 sur C). Sur processeur, un N₀ grand est abordable. |
| **C-b1 (1ʳᵉ puce).** Variance inter-lois | **Acceptée** | L'unité statistique est le **monde**. Le nombre de mondes m est préenregistré et dimensionné. |
| **B-b2.** Inflation du type I par quantiles empiriques ; extinction d'e-BH | **Acceptée** | Je privilégie les e-processus, valides par construction, aux seuils fixés par quantile empirique. Au plus K_max candidats passent à l'épreuve ; K_max est petit, préenregistré et illustratif. |

### Mesures auxiliaires

| Critique | Verdict | Raison, ou test qui la remplace |
|---|---|---|
| **C-a7a, C-c4.** Imposer une même longueur crée un biais de collisionneur | **Transformée** | L'appariement forcé est retiré. La longueur devient une base triviale à battre, et un contrôle honnête contre honnête vérifie l'absence d'artefact. |
| **C-a7b, C-c6, B-c4 (2ᵉ partie).** L'audit du tri confond style et contenu | **Acceptée** | Deux ajouts (E6) : un contrôle de paraphrase neutre vers neutre (C) et l'injection de faux théorèmes rédigés dans un registre poli face à des preuves correctes en registre plat (B). |
| **C-b5.** Délai censuré | **Acceptée** | Le délai est abandonné. Seule compte la puissance à horizon fixé. |

---

## (b) Expériences corrigées

Seuils, effectifs et coûts sont **illustratifs**. La règle est commune : **un seul seuil δ\* sur l'estimateur**, et un effectif choisi pour que les deux erreurs soient ≤ 5 % à δ\* ± ε. Chaque issue falsifie ainsi exactement une hypothèse (B4).

### E0. Porte de sanité (processeur, préalable à tout)

| Volet | Si l'issue est négative | Ce que l'issue falsifie |
|---|---|---|
| Plafond oracle : sur mondes à loi connue, aucun candidat ne dépasse le test du rapport de vraisemblance informé au-delà de l'erreur Monte-Carlo | Fuite ou bogue | « Le banc est sain » |
| Contrôle positif du plafond : l'accumulation sur référence fixe reproduit le plafond d'horizon rapporté dans les faits | Simulateur faux | Toute la suite est nulle |

Coût : quelques heures-CPU (illustratif).

### E1a. L'organisme fait-il mieux que l'archive étendue ?

- **H_A** : parmi au plus K_max candidats sélectionnés sur des mondes d'entraînement, au moins un est valide et son écart moyen de puissance avec le meilleur recombinant de l'**archive étendue par un tiers** vaut au moins δ\*. La mesure porte sur des mondes d'épreuve écrits par l'instance aveugle aux cartes.
- **H_B** : l'écart est inférieur à δ\*.
- **Métrique** : moyenne sur les mondes de l'écart de puissance à horizon T, au niveau α valide à tout instant. Validité contrôlée par Clopper-Pearson sur les mondes nuls.
- **Contrôles** :
  - mondes nuls ;
  - mondes isomorphes reparamétrés ;
  - comparaison entre mondes écrits par les auteurs des cartes et mondes aveugles. Si l'écart dépasse δ\* seulement sur les premiers, le gain est un artefact de construction.
- **Falsification** : un écart ≥ δ\* falsifie H_B ; un écart < δ\* falsifie H_A.

### E1b. L'organisme apporte-t-il plus que le modèle ?

- **H_A** : sur les mêmes mondes d'épreuve, l'organisme complet bat le **modèle pré-entraîné seul** (sans graphe ni carte) d'au moins δ\*.
- **H_B** : l'écart est inférieur à δ\* ; le gain d'E1a vient du modèle et non de l'organisme.
- **Secondaire, descriptif** : effet des cartes, mesuré avec des cartes permutées.
- **Après coup** : un tiers classe chaque candidat retenu en « récupération d'une méthode connue » ou « non retrouvée ».
- **Coût** : E1a et E1b ensemble, quelques jours-CPU (illustratif).

### E2a. Un nul par acte est-il viable en simulation, et avec quelle tolérance ?

- **H_A** : au moins une construction, ma base comprise, satisfait deux conditions. Sa borne de Clopper-Pearson sur le taux de fausses alertes reste ≤ α sur toute la grille d'horizons jusqu'à T ≫ N_réf, pour un décalage nul de la référence. Au-delà de N_réf, sa puissance dépasse celle de l'accumulation sur référence fixe d'au moins δ\*.
- **H_B** : aucune construction ne satisfait les deux conditions.
- **Grille** :
  - décalage de référence ε variable ;
  - flux honnêtes stationnaires autorégressifs sans dérive (C) ;
  - flux avec dérive ;
  - amplitudes de signal (C-b2) ;
  - référence conditionnée sur l'historique complet ou sur une fenêtre tronquée (B-a4).
- **Produit annexe** : la tolérance ε_max de chaque construction, qui est une carte et non une preuve.
- **Falsification** : l'existence d'une construction qui passe falsifie H_B ; son absence falsifie H_A.

### E2b. L'organisme fait-il mieux que ma base ?

- **H_A** : une construction de l'organisme a une tolérance ε_max supérieure à celle de ma base, à puissance au moins égale, d'au moins δ\*.
- **H_B** : non.
- **Coût** : E2a et E2b, processeur seul (illustratif).

### E5. Le nul par acte s'applique-t-il au modèle réel ?

Cette expérience porte sur des traces 8B **honnêtes seulement** et ne consomme aucune famille de sabotage.

- **H_A** : le décalage mesuré entre l'agent réel et son processus de référence est inférieur à l'ε_max de la meilleure construction d'E2a.
- **H_B** : le décalage est supérieur ou égal à ε_max ; le nul par acte n'est pas applicable en l'état.
- **Contrôles obligatoires** :
  - agent honnête muni d'une consigne privée bénigne (B) ;
  - sonde placebo sur sous-espace aléatoire ;
  - discrimination de tâches honnêtes par la représentation retenue. Seuil unique sur l'AUC ; c'est la proposition que B adresse à C, reprise ici.
- **Retombée** : ces traces servent aussi à étalonner les fausses alertes GPU pour E4.
- **Coût** : de l'ordre de dizaines d'heures-GPU (illustratif).

### E3. Étanchéité, canal par canal

- **H_A^c** : aucune fuite par le canal c de taille au moins s_c.
- **H_B^c** : une fuite de taille au moins s_c existe sur le canal c.
- **Canaux** : lexical, géométrique, paramétrique.
- **Contrôle positif par canal** : un canal volontairement percé fixe s_c.
- **Falsification** :
  - un excès significatif falsifie H_A^c ;
  - l'absence d'excès, contrôle positif validé, falsifie seulement « fuite par c au-delà de s_c ».
- **Hors de portée** : aucune conclusion sur les canaux non testés. Elle relève de l'audit de provenance, revu par un tiers.
- **Coût** : marginal (illustratif).

### E4. Le proxy processeur ordonne-t-il les candidats viables ?

- **Lot** : candidats valides sur processeur **et** sur E5, lus en une seule fois.
- **H_A** : la corrélation de Spearman dans cette strate est au moins ρ\*. La détection GPU est mesurée à taux de fausses alertes égal.
- **H_B** : la corrélation est inférieure à ρ\* ; le proxy est décoratif pour la décision de promotion.
- **Contrôles** : les deux proxys mécaniques (validité syntaxique ; puissance sur monde archivé élémentaire). Si l'un d'eux atteint ρ\*, le proxy de l'organisme n'apporte rien.
- **Portée** : conditionnelle à la famille lue.
- **Limite** : avec K petit, la puissance est faible. Je ne sais pas si le budget permet un K informatif.
- **Coût** : de l'ordre de dizaines d'heures-GPU (illustratif).

### E6. Le tri interne de l'organisme est-il corruptible par le style ?

- **H_A** : le déplacement de rang sous réécriture rhétorique dépasse celui d'une paraphrase neutre d'au moins d\*, **ou** des faux théorèmes en registre poli sont classés devant des preuves correctes en registre plat au-delà d'une proportion p\* fixée.
- **H_B** : ni l'un ni l'autre ; le tri n'est pas mesurablement corruptible à ces tailles.
- Le corpus contient seulement des énoncés mathématiques vrais ou faux ; aucune recette d'attaque.
- **Coût** : processeur, avec appels au modèle de tri (illustratif).

---

## (c) Réponse à l'arbitre (une page)

**Ce qui est établi.**
- *Faits (RAPPORTÉ)* :
  - la règle de séparation sélection/évaluation ;
  - la lecture unique sur familles inédites ;
  - le plafond d'horizon de l'accumulation sur référence finie, sauf nul par acte ;
  - le budget GPU modeste ;
  - l'évaluation de l'organisme sur mondes plantés.
- *Contraintes mathématiques reprises des critiques*, avec leurs statuts d'origine :
  - les e-valeurs conformes sont bornées par k+1 (VÉRIFIÉ selon B, calcul refait concordant) ;
  - les procédures à seuil élevé perdent leur puissance quand les e-valeurs sont plafonnées (VÉRIFIÉ selon B) ;
  - un mélange de candidats viables et dégénérés gonfle la corrélation de Spearman (VÉRIFIÉ selon B et C) ;
  - sans échangeabilité conditionnelle, la garantie de Ville ne s'applique plus (VÉRIFIÉ selon B et C).
- *Conséquence structurelle*, que j'avance et qui reste mon interprétation des règles (HYPOTHÈSE de conception) : **sous la règle de séparation, la boucle ne peut pas se fermer sur l'évaluation.** Elle se ferme seulement sur les besoins (verrous formels), sur les données honnêtes et sur un calendrier fixé d'avance. Ce sont deux chaînes ouvertes, et non une boucle de rétroaction au sens de l'optimisation. Toute architecture qui réinjecte un verdict de lecture, même d'un bit, même par un humain, enfreint la règle. Dans ma conception III.1, c'était le cas de mon propre bit de retour.

**Ce qui n'est pas établi.**
- Que l'organisme apporte quoi que ce soit au-delà d'un modèle pré-entraîné seul et d'une archive complète : S1 et S2, toujours HYPOTHÈSE.
- Que les mondes-contrôle synthétiques prédisent les épreuves GPU.
- Qu'un nul par acte valide existe pour un agent réel de 8B. Le décalage réel n'est pas mesuré, et je ne sais pas s'il est assez petit.
- Que l'interface soit étanche au-delà des canaux testés. Aucune batterie de canaris ne peut l'établir.
- Le nombre de familles inédites disponibles, et donc le nombre de lectures. Je ne sais pas.
- La « profondeur » des idées. Rien ici ne la mesure : on ne compte que des gains et des garanties réfutables.

**Ordre corrigé** (notes 1 à 5 illustratives ; coût 1 = processeur seul).

| Rang | Action | Ce qu'elle décide |
|---|---|---|
| 1 | E0 puis E1a et E1b, préenregistrés ensemble | Raison d'être de l'organisme pour le contrôle |
| 2 | E2a et E2b, en parallèle sur processeur | Verrou explicite des faits |
| 3 | E3 et l'audit de provenance | Condition pour tout le reste |
| 4 | E5 | Première dépense GPU ; aucune famille consommée |
| 5 | E6 | Corruptibilité du tri interne |
| 6 | E4 | Seule action qui consomme une famille ; elle vient en dernier |

**Expérience à faire en premier : E0 → E1a + E1b.**
- **Ce qu'elle oppose** : l'organisme complet au meilleur recombinant d'une archive étendue par un tiers (H_A d'E1a), puis au même modèle pré-entraîné sans graphe ni carte (H_A d'E1b). La mesure porte sur des mondes-contrôle écrits par une instance aveugle aux cartes, avec un seuil unique δ\* (illustratif) sur l'écart moyen de puissance à niveau valide.
- **Pourquoi d'abord** : elle coûte quelques jours-CPU (illustratif) et ne consomme aucune famille. Elle tranche aussi la question préalable à toute boucle : *l'organisme ajoute-t-il quelque chose que le modèle seul ou une bibliographie complète ne donnent pas ?*
- **Issue qui réfute** : un écart inférieur à δ\* en E1b réfute l'utilité propre de l'organisme pour le contrôle. Il faudrait alors réorienter l'effort vers la recherche directe sur le nul par acte (E2a, E5), sans organisme.
- **Limites qui subsistent** :
  - le réalisme des mondes synthétiques ;
  - le canal humain résiduel entre cycles, journalisé mais non borné ;
  - la puissance faible d'E4 ;
  - la portée d'E4, limitée à une famille.

FIN-DE-CELLULE