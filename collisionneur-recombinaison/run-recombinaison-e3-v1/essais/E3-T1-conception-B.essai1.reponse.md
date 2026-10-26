# Proposition B — Tour III.1 : trancher l'étage de recombinaison bisociative

**Pièces manquantes ou partielles**
- **C4** (mondes à ponts plantés) : absente, comme le signale l'en-tête des faits. Je n'en suppose aucun contenu.
- **Essai de la brique 1** (`5b7011b1…`) : non servi. Seule sa synthèse figure dans C3a.
- **Propositions A et C** : invisibles à ce tour, qui se joue à l'aveugle. J'applique donc B1 aux pièces C1 à C3.

**Statuts.** Tout ce qui vient des faits reste **RAPPORTÉ**. C'est le cas même de ce que C2 ou C3 qualifient de « vérifié », car C3a précise « pas encore vérifié par un agent d'une autre famille ». Tout ce qui est de moi est **HYPOTHÈSE**.

## Thèse de B

**HYPOTHÈSE.** L'étage de tirage n'est pas le goulot. La forme corrigée de C3 est juste sur le plan algébrique, mais elle n'a jamais été comparée au bon témoin, à savoir un tirage stratifié par domaine. Sa métrique « bisoc » est en partie acquise par construction.

Deux questions décident de l'étage, et aucune n'a été testée :
1. Un modèle de langue, à qui l'on donne une **paire vraie** (oracle), produit-il une fille qui prédit plus que la simple conjonction de ses parents ?
2. Un critère mécanique sait-il distinguer un **pont vrai** d'un **homonyme** ?

L'ordre des expériences ci-dessous découle de là. Si la fusion échoue même sur oracle, optimiser le tirage ne sert à rien.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Ce qui le menace |
|---|---|---|---|
| a1 | La forme corrigée « a été gardée », donc validée. | RAPPORTÉ (C3b, synthétique seulement, non revérifié) | C3b, § 5 : « Tout est synthétique » ; les méthodes c3 à c5 « utilisent les étiquettes d'opérateur, supposées extraites ». |
| a2 | Le score « bisoc » de c5 (0,995 à 1,000) mesure une capacité. | RAPPORTÉ (chiffre) ; l'interprétation est une HYPOTHÈSE que je conteste | c5 *garantit* après tirage une paire de même étiquette et de domaines différents dès qu'il en existe une (199 à 200 corpus sur 200). Le score est donc quasi tautologique : il mesure l'existence d'une paire, pas la vérité d'un pont. |
| a3 | Le DPP corrigé apporte quelque chose de plus qu'un tirage stratifié. | HYPOTHÈSE (non testé) | Les témoins de C3b sont « hasard » et « tri par qualité », jamais une stratification. Avec 5 domaines et k = 4, un tirage d'un élément par domaine atteint « domaines » = 1,0 *par construction* si les étiquettes de domaine sont connues. Le DPP n'a donc d'utilité que si les domaines sont continus ou mal étiquetés, ce qui n'a pas été mesuré. |
| a4 | Domaine et opérateur sont séparables et extractibles d'un résumé. | HYPOTHÈSE (C1 l'avoue) ; RAPPORTÉ : SimHash « indécis au niveau du texte » (C3a) | Sur les textes réels de la génération 18, la « répulsion » s'exerce sur le gabarit, les accents coupés et les mots-outils (C3b, § 2). Un vecteur de domaine bruité fait la même chose. |
| a5 | Un opérateur partagé est un indice de pont vrai. | RAPPORTÉ : 65 à 67 % des interfaces non vides ne contiennent aucun pont planté (C4 de C3b) | Opérateurs moyeux (« optimization », « GNN ») et homonymes (« kernel », « entropy », « relaxation »). |
| a6 | Des domaines éloignés produisent des fusions plus fertiles. | HYPOTHÈSE (cadre de Koestler, 1964, *The Act of Creation*) | Uzzi, Mukherjee, Stringer et Jones (2013, *Atypical combinations and scientific impact*, Science) associent plutôt l'impact à un mélange de combinaisons conventionnelles et atypiques. L'éloignement maximal n'est pas un optimum établi. |
| a7 | Une fusion par modèle de langue peut accroître le contenu empirique. | HYPOTHÈSE (aucun fait) | C3b, C4 : la condition « B non vide » est satisfaite par les mots du gabarit. Rien ne montre qu'une fille dise autre chose que « A et B ». |
| a8 | « Prédit plus que ses parents » est mesurable mécaniquement. | HYPOTHÈSE | Sur littérature réelle, aucune prédiction n'est vérifiable dans le tour. Seuls les mondes plantés le permettent. |
| a9 | Les parents survivants sont bien sélectionnés par réfutation. | RAPPORTÉ (R-525 : le critère de sélection reste à valider, c'est la première expérience) | Si le filtre promeut des paris couverts, la recombinaison fusionne des artefacts. |
| a10 | La rétrodiction (champs disjoints avant une date, reliés après) valide des ponts. | HYPOTHÈSE | (i) La co-occurrence ultérieure mesure en partie la popularité. (ii) Tout modèle entraîné après la date connaît les liens : la fusion est contaminée. |
| a11 | Le régime de 12 à 50 éléments se comporte comme n = 20. | RAPPORTÉ pour n = 20 seulement (C3b, tirage exact) | À n = 12, il peut n'exister **aucun** pont vrai. Une paire « garantie » devient alors une chimère forcée (voir E1). |
| a12 | « Hypothèses » et « articles » sont interchangeables comme parents. | HYPOTHÈSE | Une hypothèse survivante a un test associé ; un article n'en a pas. Le critère de contenu ne s'applique tel quel qu'aux premières. |

**Contre C3 (B1).**
- C3a écrit « diversité 0,90 à 0,95 pour un hasard de 0,74 ». La valeur 0,74 est le hasard de la seule configuration « moyeux » ; configuration par configuration, le gain réel est de 0,14 à 0,15 (C3b, tableau de l'essai 3).
- Selon C3b, le critère P2 du rapport aurait **préféré le noyau cassé** : a2 obtient 0,48 / 0,55 / 0,34, contre 0,13 / 0,20 / 0,08 pour le correctif. Toute métrique de « paires ⟨d,d⟩ < seuil et ⟨o,o⟩ > seuil » est donc invalidée comme juge de l'étage.

### Point 1 : où la forme corrigée cède (HYPOTHÈSES, chacune testée en E1 ou E2)

- **Domaines mal séparés.** S_ij = ⟨d_i,d_j⟩² repousse ce que la représentation sépare, pas ce que le monde sépare. Prédiction : le gain sur un tirage stratifié tend vers 0 quand la marge de séparation des domaines tend vers 0. Si les vecteurs de domaine portent le gabarit ou le style, le gain peut devenir négatif.
- **Opérateurs moyeux.** Le pont choisi après tirage tombera sur l'opérateur le plus fréquent : un « bisoc » de 1,000 est alors vide de sens. C3b le laisse voir : le hasard atteint déjà 0,715 en configuration « moyeux ». Le remède plausible est de pondérer l'opérateur par sa rareté dans un corpus de fond, sur le modèle du remède b+ (RAPPORTÉ : rétention du pivot 1,00, moyeu repoussé à 0,95 – 0,99, sur synthétique).
- **Homonymes.** Le filtre de compatibilité ne couvre que 4 axes (RAPPORTÉ). Un homonyme comme « kernel » (noyau intégral contre noyau de graphe) passe sans contradiction lexicale. Il faut un critère **structurel**, testé en E2.
- **Étiquettes d'opérateur bruitées.** c5 utilise les étiquettes vraies. Si une fraction ε des étiquettes est fausse, la précision du pont garanti chute. Je ne donne pas de chiffre, car la pente dépend du générateur : elle se mesure en E1.
- **Petits corpus.** La garantie de paire force une fusion même quand aucun pont n'existe. Sans issue « pas de pont », le taux de fausses alertes sur un corpus sans pont vaut 100 % par construction. Il faut donc une **abstention**.
- **Glouton.** Le glouton est déterministe : 1 ensemble distinct sur 50 permutations (RAPPORTÉ). À n ≤ 50 et k = 4, l'énumération exacte coûte au plus C(50,4) = 230 300 sous-ensembles, ce qui est faisable. Le glouton n'a donc aucune justification.

### Point 2 : trois mécanismes sérieux, et lequel produit des ponts vrais

1. **Découverte fondée sur la littérature, modèle A–B–C** (Swanson, 1986, *Fish oil, Raynaud's syndrome, and undiscovered public knowledge*, Perspectives in Biology and Medicine ; revue : Henry et McInnes, 2017, *Literature Based Discovery: Models, methods, and trends*, J. Biomed. Inform.).
   - Ce qu'il apporte : des termes intermédiaires B partagés par deux littératures non connectées. La validation classique consiste à redécouvrir des liens connus.
   - Faiblesses : explosion des candidats, et pivots génériques qui jouent le rôle de moyeux (même pathologie que a5).
   - Verdict (HYPOTHÈSE) : il produit des ponts **plausibles**, en biomédecine surtout, mais **ne distingue pas** un homonyme d'un pont sans critère supplémentaire.
2. **Appariement de structures** (Gentner, 1983, *Structure-mapping: A theoretical framework for analogy*, Cognitive Science ; Falkenhainer, Forbus et Gentner, 1989, *The structure-mapping engine: Algorithm and examples*, Artificial Intelligence).
   - Ce qu'il apporte : le pont est un **isomorphisme de relations** (principe de systématicité), pas un mot partagé.
   - Verdict (HYPOTHÈSE) : c'est le seul des trois qui dispose d'un critère **interne et mécanique** contre l'homonymie. Le même mot avec des relations différentes donne un appariement qui échoue.
   - Coût : il faut une représentation relationnelle typée. Un modèle de langue peut l'extraire, et l'isomorphisme se vérifie alors sans modèle. C'est cohérent avec « l'arbre syntaxique canonisé » retenu par R-525 (RAPPORTÉ).
3. **Prédiction de liens sur un graphe de concepts, à découpage temporel** (Krenn et Zeilinger, 2020, *Predicting research trends with semantic and neural networks with an application in quantum physics*, PNAS ; analogue en science des matériaux : Tshitoyan et al., 2019, *Unsupervised word embeddings capture latent knowledge from materials science literature*, Nature).
   - Ce qu'il apporte : des prédictions validées par la littérature future.
   - Verdict (HYPOTHÈSE) : il produit des liens **vrais mais proches**. L'attachement préférentiel et les voisins communs sont des témoins redoutables, de sorte qu'il est peu bisociatif. C'est le bon **témoin** pour la rétrodiction (E3), pas le bon moteur.

**Mécanismes écartés comme générateurs de ponts.** Le mélange conceptuel (Fauconnier et Turner, 2002, *The Way We Think*) n'a pas de critère mécanique de vérité ; c'est la source attendue des chimères verbales. Une grille qualité-diversité (Mouret et Clune, 2015, *Illuminating search spaces by mapping elites*) et la recherche de nouveauté (Lehman et Stanley, 2011, *Abandoning objectives: Evolution through the search for novelty alone*, Evolutionary Computation) sont des **structures d'archive**. Elles récompensent la différence, pas la vérité. Elles peuvent héberger les filles, pas juger les ponts.

---

## (b) Expériences décisives (inférence forte)

**Règles communes à toutes les expériences** (reprises de R-525, RAPPORTÉ) :
- test et nul figés avant ;
- tirages frais après le dépôt des filles ;
- étalonnage A/A pour fixer le plancher de bruit δ₀ ;
- chaque seuil exprimé en multiple de δ₀.

Les valeurs numériques ci-dessous sont **illustratives**, sauf mention contraire.

### Monde planté commun (conception de B, HYPOTHÈSE)

**Les lois et les domaines**
- Une bibliothèque de 6 à 8 lois paramétriques latentes : décroissance exponentielle, logistique, diffusion, oscillateur amorti, loi de puissance, seuil.
- 10 à 20 domaines, chacun avec un vocabulaire propre (disjoint).
- Chaque élément est un texte qui décrit une régularité observée, accompagné d'un générateur de données.

**Les ponts plantés.** Deux domaines partagent la même loi sous des vocabulaires disjoints. Les parents sont **incomplets par construction** : A ne décrit que le régime court de sa loi, B (même loi, autre vocabulaire) décrit l'asymptote. Seul un transfert de B vers A permet de prédire l'asymptote de A. C'est le **contenu empirique accru**, mesurable sur des données fraîches.

**Les leurres**
- homonymes : même mot, lois différentes ;
- moyeu : un mot générique présent dans 90 % des textes ;
- paires de même domaine et même loi : non bisociatives ;
- étiquettes d'opérateur corrompues à un taux ε ∈ {0 ; 0,1 ; 0,3}.

**Contrôle de fuite du monde.** Un solveur « tricheur lexical », qui apparie par mot partagé, doit avoir une précision proche du hasard sur les ponts. Sinon le monde fuit et doit être refait.

### E0 : la fusion vaut-elle quelque chose avec une paire vraie ? (à faire en premier)

- **H_A** : sur des paires-oracles (même loi latente), la fille produite par le modèle de langue prédit le régime manquant mieux que (i) le parent A extrapolé seul et (ii) la **conjonction littérale** « A ; B » soumise au même évaluateur.
- **H_B** : la fille ne dépasse pas le meilleur des deux témoins au-delà de δ₀. La fusion est une juxtaposition.
- **Bras**
  1. fusion par modèle de langue, paires-oracles ;
  2. **transfert mécanique** : ajuster la forme fonctionnelle de B sur les données de A, sans modèle ;
  3. conjonction ;
  4. A seul ;
  5. **anti-oracle** : paires de lois différentes, même consigne.
- **Métrique** : erreur de prédiction sur le régime retenu, données tirées après dépôt. Taux de filles « promues », c'est-à-dire qui battent la conjonction de plus de 2δ₀.
- **Seuil** : H_A survit si le bras 1 est promu sur au moins 50 % des paires-oracles (illustratif) et sur au plus α des anti-oracles, avec α = 0,05 (illustratif).
- **Contrôle négatif** : le bras 5. Une promotion supérieure à α sur l'anti-oracle **invalide le critère de contenu lui-même**, pas seulement la fusion.
- **Ce que chaque issue falsifie**
  - H_A réfutée : tout l'étage par modèle de langue est réfuté, quel que soit le tirage. La v0 garde un transfert mécanique ou rien.
  - H_B réfutée : la fusion est utile, mais il reste à savoir si elle bat le transfert mécanique (bras 2). Si le bras 2 l'égale à δ₀ près, le modèle de langue est décoratif dans le monde planté. Il ne garde d'intérêt que là où aucune forme fonctionnelle n'est disponible, ce qui est une HYPOTHÈSE à tester sur un sous-ensemble textuel sans générateur explicite.

### E1 : la forme corrigée bat-elle un tirage stratifié ?

- **H_A** : le DPP corrigé (S de domaine, q de pertinence, pont choisi après tirage et pondéré par la rareté de fond, filtre de compatibilité) donne une **précision de pont** (part des paires fusionnées qui partagent la loi latente) supérieure au tirage stratifié par domaine, à consigne et filtre identiques.
- **H_B** : l'écart est inférieur à 12 points, seuil de réfutation repris de R-525 (RAPPORTÉ), ou inférieur à 2δ₀ si δ₀ est plus grand.
- **Plan factoriel**
  - n ∈ {12 ; 20 ; 50} ;
  - séparation des domaines : nette, moyenne, faible ;
  - ε ∈ {0 ; 0,1 ; 0,3} ;
  - densité de moyeu : basse, haute.
- **Bras**
  1. DPP corrigé, tirage exact ;
  2. stratifié avec pont après tirage identique ;
  3. hasard ;
  4. tricheur lexical (mot partagé) ;
  5. c5 sans pondération de rareté.
- **Métriques**
  - précision de pont ;
  - **rendement** : filles promues par E0 pour 100 appels ;
  - **taux d'abstention correcte**.
- **Contrôle négatif 1** : des mondes **sans aucun pont**. Le taux de paires fusionnées doit être au plus α ; tout bras sans abstention y échoue par construction, ce qui doit être déclaré.
- **Contrôle négatif 2** : les étiquettes d'opérateur sont permutées entre éléments. Le gain des bras 1 et 2 sur le hasard doit s'annuler, sans quoi le gain vient d'ailleurs que de l'opérateur.
- **Ce que chaque issue falsifie**
  - H_A réfutée : le DPP est un coût sans bénéfice ; la v0 prend la stratification.
  - H_B réfutée : la répulsion continue de domaine apporte quelque chose au-delà des strates. On le prédit seulement en séparation faible ou moyenne ; si le gain apparaît en séparation nette, c'est suspect et il faut auditer le tricheur.
  - Une précision qui chute avec ε plus vite que celle du bras 2 désigne l'extraction d'opérateurs, pas le tirage, comme goulot.

### E2 : quel critère distingue un pont d'un homonyme ?

- **H_A** : l'appariement structurel a une précision supérieure à l'étiquette d'opérateur (lexique de 25 termes de la caste 1, ou cosinus SimHash) sur des cas appariés « même mot, relations différentes » contre « mots différents, mêmes relations ». Les relations sont extraites par un modèle de langue en graphe typé, puis l'isomorphisme est vérifié mécaniquement.
- **H_B** : l'écart de précision est inférieur à 2δ₀. Le critère structurel ne fait que recopier le lexique.
- **Cas appariés** : chaque homonyme a un jumeau honnête de même longueur et même domaine. Je propose 200 paires de chaque type (illustratif).
- **Métrique** : détection des ponts vrais, fausses alertes sur les homonymes, aire sous la courbe.
- **Contrôle négatif** : des graphes relationnels permutés (arêtes réassignées au hasard, types conservés). L'appariement doit tomber au hasard. S'il ne tombe pas, il lit les types de nœuds, c'est-à-dire du lexique.
- **Ce que chaque issue falsifie**
  - H_A réfutée : l'appariement structurel est rejeté comme critère ; la v0 garde l'étiquette pondérée par rareté et accepte un taux d'homonymes mesuré.
  - H_B réfutée : l'étiquette lexicale est rejetée comme critère de pont ; elle reste un pré-filtre de candidats.

### E3 : rétrodiction sur littérature réelle (tirage seulement)

- **Données** : instantané OpenAlex, une des sources de l'organisme (RAPPORTÉ). Thèmes ou concepts, résumés, dates.
- **Définitions**
  - Coupure T₀. Paire « disjointe » : aucune œuvre co-étiquetée jusqu'à T₀. Paire « reliée » : au moins m œuvres co-étiquetées entre T₀ + 1 et T₀ + Δ (m, Δ figés avant).
  - Strates de distance antérieure : tertiles de distance dans le graphe de co-occurrence.
- **H_A** : la paire choisie par le pont d'opérateur après tirage, sur des résumés antérieurs à T₀, a une précision@K de « paire reliée » supérieure au meilleur de trois témoins **dans le tertile le plus éloigné**. Les témoins sont : (i) le tirage stratifié par distance, (ii) le produit des degrés (attachement préférentiel), (iii) le nombre de voisins communs (A–B–C mécanique).
- **H_B** : aucun gain au-delà de l'intervalle de bootstrap dans ce tertile. Un gain qui n'apparaît que dans le tertile proche est classé H_B, car il s'agit alors de liens proches, pas de bisociation.
- **Contrôle négatif 1, fuite** : refaire l'analyse avec T₀ décalé dans le passé et les « liens futurs » remplacés par des liens déjà existants. La méthode ne doit pas les « prédire » mieux que les témoins. Sinon elle lit des alias de concepts déjà reliés.
- **Contrôle négatif 2** : permuter les dates de publication à l'intérieur des strates. Le gain doit s'annuler.
- **Pourquoi aucune fusion en E3** : tout modèle de langue ouvert récent a probablement vu la littérature postérieure à T₀ (a10, HYPOTHÈSE). On n'y évalue donc que le **tirage**. Une variante avec OLMo (corpus d'entraînement documenté, période exacte à vérifier) permettrait de chercher les liens cibles dans le corpus d'entraînement et d'exclure les paires contaminées. C'est faisable mais coûteux, et en option.
- **Ce que chaque issue falsifie**
  - H_A réfutée : sur données réelles, le pont d'opérateur ne bat pas la prédiction de liens classique. La v0 utilise les témoins (ii) et (iii) comme tirage, et la bisociation reste une HYPOTHÈSE non soutenue.
  - H_B réfutée : le signal d'opérateur contient une information de pont au-delà de la topologie du graphe.
  - Réserve de validité de construit (HYPOTHÈSE) : co-occurrence n'est pas pont. Un audit manuel aveugle d'un échantillon (30 paires, illustratif) doit dire quelle part des liens futurs est méthodologique (un opérateur transféré) et quelle part est simplement thématique.

**Ordre et règle d'arrêt.** E0, puis E2, puis E1, puis E3.
- Si E0 réfute H_A, on arrête l'étage fusion par modèle de langue.
- Si E2 réfute l'appariement structurel, E1 se joue avec l'étiquette pondérée.
- E3 ne se lance que si E1 donne un tirage gagnant ou une égalité, ce qui fixe le tirage à rétrodire.

---

## (c) Instruments nommés : mesure minimale de fonctionnement

| Instrument | Détection | Fausses alertes | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|---|
| **Tirage DPP corrigé** | précision de pont (E1) | paires fusionnées sur monde sans pont | mondes identiques avec et sans pont planté, même n et même densité de moyeu | tirage stratifié par domaine ; énumération exacte comme référence du glouton |
| **Pont par opérateur après tirage** | rappel des lois partagées | taux de ponts sur homonymes et sur moyeux | paire homonyme contre jumeau honnête (E2) | appariement par mot partagé ; lexique de la caste 1 ; cosinus SimHash |
| **Pondération de rareté de fond** (b+) | rétention des pivots vrais | moyeux non repoussés | pivot et moyeu de même distribution interne (situation où b échoue, RAPPORTÉ) | sans pondération ; liste d'arrêt seule (R1 : expose le pivot, RAPPORTÉ) |
| **Filtre de compatibilité** | contradictions rejetées : rappel 0,608, précision 0,938 en régime réaliste (RAPPORTÉ, lexique écrit par l'essayeur) | rejets à tort : 5,1 % en régime réaliste (RAPPORTÉ) | sur **vrais résumés** : paires annotées en aveugle, contradictoires contre compatibles, appariées par thème | **rejet aléatoire au même taux**. Sans ce témoin, une baisse de contradictions peut venir du seul volume rejeté. |
| **Fusion par modèle de langue** | promotion sur paires-oracles (E0) | promotion sur anti-oracles | même paire présentée en oracle et en anti-oracle à vocabulaire égal | **transfert mécanique** (ajustement de forme) ; conjonction littérale |
| **Critère « prédit plus »** | signale une vraie synthèse | accepte une **juxtaposition déguisée** | 100 filles synthétiques contre 100 juxtapositions rédigées pour avoir l'air intégrées, de même longueur (illustratif) | nouveauté de n-grammes par rapport aux parents ; longueur ; ces deux témoins doivent échouer, faute de quoi le critère les recopie |
| **Monde planté** | précision accessible à l'oracle | précision du **tricheur lexical** | même monde avec et sans vocabulaire disjoint | si le tricheur atteint la précision de l'oracle, le monde fuit |
| **Rétrodiction** | précision@K dans le tertile éloigné | « prédictions » de liens déjà existants (fuite) | coupures T₀ réelle contre T₀ décalée | produit des degrés ; voisins communs ; stratifié par distance |

**Consigne de fusion proposée** (HYPOTHÈSE, à figer avant E0). Le modèle remplit un gabarit à quatre champs :
1. **Table de correspondance** variable_A ↔ variable_B, bijective, avec les types.
2. **Une prédiction transférée** dans le domaine A, avec signe, ordre de grandeur et régime, qu'aucun parent ne fait.
3. **La condition qui la falsifierait.**
4. **Les contraintes vérifiées** : axes du filtre et hypothèses de chaque parent.

**Critère mécanique.** Une fille est rejetée dans trois cas :
- (i) la table de correspondance n'est pas bijective ou viole les types, ce qui se vérifie sans modèle ;
- (ii) sa prédiction est déductible d'un seul parent (test : on donne au même évaluateur A seul, puis B seul) ;
- (iii) elle ne bat pas la conjonction sur données fraîches de plus de 2δ₀.

La notion de contenu suit Popper (*Logik der Forschung*, 1934) : risque déclaré multiplié par couverture, conformément à la définition convergente de R-525 (RAPPORTÉ).

---

## (d) Ancrage matériel

Tous les chiffres de cette section sont **illustratifs**, sauf les rappels marqués RAPPORTÉ.

**Modèles ouverts**
- **Fusion et extraction relationnelle** : un modèle instruit de 7 à 14 milliards de paramètres, à poids ouverts (familles Qwen2.5, Llama 3.1 ou OLMo 2). OLMo est préférable pour E3, parce que son corpus d'entraînement est documenté. La licence et la date de coupure exacte de chaque version sont **à vérifier**.
- **Deuxième famille** : un second modèle, d'une autre famille, sert à la réplication. Cela répond au point « vérificateur d'une autre famille » de C3a.
- **Plongements de domaine** : un encodeur scientifique ouvert, par exemple SciBERT (Beltagy, Lo et Cohan, 2019, *SciBERT: A Pretrained Language Model for Scientific Text*), à comparer au SimHash de l'organisme, qui est indécis au niveau du texte (RAPPORTÉ).

**Calcul et coûts**

| Expérience | Volume | Calcul | Coût estimé |
|---|---|---|---|
| E0 | 5 bras × environ 300 paires × 3 graines ≈ 4 500 générations d'environ 1 000 jetons, soit environ 5 M de jetons | un GPU de 24 Go avec moteur d'inférence à lots, quelques heures | inférieur à 10 USD en location |
| E2 | environ 800 extractions relationnelles ; isomorphisme sur processeur | négligeable | inférieur à 3 USD |
| E1 | mondes et tirages exacts (n ≤ 50, k = 4), énumération faisable | processeur | environ 0 USD ; les fusions des paires retenues se paient au tarif E0, soit 5 à 10 USD |
| E3 | instantané OpenAlex gratuit ; graphe de co-occurrence d'un sous-ensemble (quelques champs, une décennie) | processeur, mémoire de quelques dizaines de Go | environ 0 USD ; audit manuel aveugle : temps humain |

**Total, hors temps humain** : 20 à 30 USD. Repères RAPPORTÉS : génération 0 à 0 USD, organisme à 0,12 USD, tour précédent à 7,82 USD, première expérience de R-525 à moins de 20 USD.

**Contrainte « Python pur »** (C-01 à C-17) : on ne sait pas si elle s'applique au pôle ou seulement à l'organisme (HYPOTHÈSE). C3b a utilisé numpy et scipy hors de l'organisme. Je recommande de faire de même pour les essais, et de ne porter en Python pur que ce qui survit.

---

## Point 5 : recommandation pour la version 0 du pôle

**Forme retenue (HYPOTHÈSE, à confirmer par E0 à E2)**

1. **Tirage** : stratification par domaine (énumération exacte à n ≤ 50), et non DPP. Le DPP corrigé reste une option, admise seulement si E1 réfute H_B.
2. **Candidats de pont** : opérateur pondéré par sa rareté dans un corpus de fond (logique b+), avec la liste d'arrêt comme premier étage.
3. **Critère de pont** : appariement structurel vérifié mécaniquement, si E2 le confirme.
4. **Abstention obligatoire** quand aucune paire ne passe le critère de pont. Il n'y a pas de paire « garantie ».
5. **Filtre de compatibilité** : gardé comme réducteur, jamais comme garantie (C3 éliminée comme garantie, RAPPORTÉ), et évalué contre un rejet aléatoire au même taux.
6. **Fusion** : gabarit à quatre champs, avec le triple rejet mécanique ; le **transfert mécanique** est toujours exécuté en parallèle comme témoin.
7. **Vocabulaire** : on parle de « fusion sur interface commune » et non de « pushout », comme le recommande C2. Le terme catégoriel n'a pas de contrepartie dans le code (RAPPORTÉ).

**Ce qui me ferait changer d'avis** (chaque point est une issue des expériences ci-dessus)
- **E0, H_A réfutée** : je retire la fusion par modèle de langue de la v0. La recombinaison se réduit au transfert mécanique sur les paires validées, ou disparaît.
- **E0, transfert mécanique égal à la fusion** : le modèle de langue ne sert qu'à l'extraction, pas à la synthèse.
- **E1, H_B réfutée en séparation faible ou moyenne** : j'adopte le DPP corrigé, avec Sinkhorn sur S seul s'il le faut. Sur L entier, Sinkhorn efface q (RAPPORTÉ : rang 0,96 → 0,03).
- **E2, H_A réfutée** : j'abandonne l'appariement structurel et je déclare un taux d'homonymes mesuré comme coût connu de la v0.
- **E3, H_A réfutée dans le tertile éloigné** : je considère que la bisociation par opérateur ne bat pas la prédiction de liens classique sur données réelles. La v0 tire alors avec le produit des degrés ou les voisins communs, et la bisociation reste une HYPOTHÈSE.
- **Critère de sélection de R-525 invalidé** : tout l'étage est suspendu, puisque ses parents sont des artefacts (a9).

FIN-DE-CELLULE