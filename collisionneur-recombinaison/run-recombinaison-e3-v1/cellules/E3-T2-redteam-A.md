# Proposition A — Tour III.2 : équipe rouge croisée contre B et C

**Pièces.** C4 (mondes à ponts plantés) absente au départ du tour ; l'essai de la brique 1 (`5b7011b1…`) non servi, seule sa synthèse figure dans C3a. Je n'en suppose aucun contenu. Les pièces B et C sont complètes.

**Statuts.** Ce qui vient de C1–C3 et de R-525 est **RAPPORTÉ** (C3a : « pas encore vérifié par un agent d'une autre famille »). Tout ce qui est de moi est **HYPOTHÈSE** ; tout chiffre que je calcule est « illustratif » et son calcul est montré.

---

## Contre la proposition B

### (a) Failles

**B1. Le monde planté fuit par la forme, pas par le domaine.** B exige des domaines à vocabulaires disjoints et un « tricheur lexical » à précision proche du hasard. Mais chaque élément « décrit une régularité observée » : le texte doit nommer la forme de la loi (saturation, décroissance, plateau, oscillation, seuil). Ce vocabulaire de forme est transversal aux domaines, et c'est lui qui porte la loi latente. Un tricheur sur mots de domaine est au hasard par construction (les ponts n'en partagent aucun, les homonymes en partagent un : le tricheur est même sous le hasard), donc le contrôle de fuite passe sans rien tester. Le tricheur à construire est un classifieur sur le vocabulaire de forme, hors mots de domaine (HYPOTHÈSE).

**B2. E1 à ε = 0 est tautologique, et le contraste DPP/stratifié ne porte sur rien.** B l'avoue (a2) mais ne corrige pas : si l'« étiquette d'opérateur » est la loi latente, le pont après tirage est un oracle, et « précision de pont » vaut 1 dès que les 4 tirés contiennent une paire étiquetée. Les bras 1 et 2 reçoivent le même oracle ; seul diffère le choix des 4 éléments. La métrique mesure alors le nombre de paires étiquetées dans un 4-uplet, pas un pont. À ε > 0, la chute de précision est la même pour les deux bras, puisque l'étape fautive leur est commune : le plan factoriel n'identifie pas la source du gain.

**B3. E2 déplace la lexicalité dans les étiquettes de relations.** Les relations sont extraites par un modèle de langue en « graphe typé », puis l'isomorphisme est vérifié mécaniquement. Si le vocabulaire des relations est ouvert, l'extracteur peut nommer la relation d'après le mot du texte (« applique_noyau ») : l'isomorphisme devient un appariement de labels, c'est-à-dire du lexique rebadgé. Le contrôle « graphes permutés, types conservés » agit sur le graphe déjà extrait, jamais sur l'extracteur. Il manque un vocabulaire de relations fermé et figé avant E2, et un contrôle où l'extracteur reçoit un texte dont les mots-clés ont été échangés entre un homonyme et son jumeau honnête (HYPOTHÈSE).

**B4. Le critère « prédit plus » (ii) ne distingue pas transfert et recopie.** Rejet si « la prédiction est déductible d'un seul parent (on donne au même évaluateur A seul, puis B seul) ». Dans le monde de B, le parent B *contient* l'asymptote. Une fille qui recopie l'asymptote de B en renommant les variables de A n'est pas « déductible de B seul » pour un évaluateur qui ne connaît pas la table de correspondance : elle passe (ii) tout en étant exactement la juxtaposition que B veut écarter. Et si l'évaluateur est un modèle de langue, c'est le juge non étalonné que C2 reproche à P3 (RAPPORTÉ).

**B5. (iii) est acquis par base de rate.** La « conjonction littérale A ; B » ne prédit rien sur l'asymptote de A (B parle de son propre domaine). N'importe quelle fille qui transfère *une* loi de la bibliothèque bat la conjonction ; avec 6 à 8 lois et des mots de forme (B1), deviner la bonne famille a une probabilité largement supérieure à 1/8 (illustratif, HYPOTHÈSE). Le témoin « transfert mécanique » (bras 2) a, lui, accès à la bibliothèque des formes fonctionnelles du générateur : c'est un oracle de forme, pas un témoin. S'il gagne, cela ne dit rien du cas réel sans forme explicite ; s'il perd, c'est suspect.

**B6. Asymétrie de falsification en E0.** « H_A réfutée : tout l'étage par modèle de langue est réfuté, quel que soit le tirage. » Une réfutation sur des mondes à lois paramétriques explicites n'implique rien pour des hypothèses textuelles sans forme fonctionnelle, cas que B reconnaît pourtant en fin d'E0. L'issue est surpuissante dans un sens, nulle dans l'autre.

**B7. E3 : la cible « reliée après T₀ » est définie sur des concepts OpenAlex,** dont la hiérarchie fait que deux concepts frères sous un même parent se relient fréquemment. Les témoins (produit des degrés, voisins communs) ne lisent pas la taxonomie ; un sélecteur qui la lit, même indirectement via les résumés, gagne sans bisociation. Confondant supplémentaire : la disponibilité des résumés dans OpenAlex varie selon éditeur et période ; un signal d'opérateur « absent » dans un tertile peut n'être qu'un résumé manquant.

**B8. Instruments « cas honnêtes appariés » pour le critère de contenu** : « 100 juxtapositions rédigées pour avoir l'air intégrées ». Rédigées par qui ? Si par un modèle, la frontière fille/juxtaposition est fixée par le style du rédacteur, et un critère qui apprend ce style passe le test sans mesurer le contenu.

**B9. Statut.** B réutilise le seuil « 12 points » de R-525 comme s'il était calibré ; R-525 le donne en « ~12 », sans nul couru (RAPPORTÉ). La citation Uzzi et al. (2013) est correctement attribuée à ma connaissance, mais son résultat porte sur des combinaisons de *références* citées, pas sur des opérateurs partagés : l'usage contre a6 est une analogie, à déclarer comme telle.

### (b) Scénarios d'évasion

Agent adverse : le modèle de fusion, ou un extracteur, qui maximise ses promotions.

- **Monde planté / E0** : mémoriser les 6 à 8 lois (elles reviennent d'un fold à l'autre), lire les mots de forme, émettre l'asymptote de la famille la plus probable en variables de A. Passe (i) (bijection sur 2 à 3 variables typées : trivial), (ii) (B4), (iii) (B5). Coût : nul au-delà d'une politique fixe.
- **Pari couvert** : prédiction disjonctive (« sature ou décroît ») ; B invoque Popper (risque × couverture) mais ne donne aucune mécanique de mesure du risque déclaré. Sans elle, la couverture n'est pas pénalisée. Coût : nul.
- **E2** : émettre pour chaque texte un graphe-étoile de même forme avec des labels de relations copiés des mots-clés. Tout est isomorphe à ce que l'extracteur veut rapprocher ; le contrôle des graphes permutés ne détecte pas « tous les graphes identiques ». Coût : nul.
- **E1** : rien à tromper, le pont est un oracle ; l'agent n'a qu'à ne jamais s'abstenir (l'abstention n'est récompensée que sur les mondes sans pont, qui, s'ils forment un lot séparé, sont reconnaissables à l'absence de toute paire étiquetée). Coût : nul.
- **E3** : tout modèle ayant vu la littérature post-T₀ (a10) ; ou, sans contamination, lire les paires de concepts frères (B7). Coût : nul.
- **Tous à la fois** : un même acteur contrôle extraction et fusion ; il encode l'identité de loi dans les labels de relations (passe E2), garantit le pont (E1), recopie l'asymptote renommée (E0). Rien dans B n'impose que l'extracteur et le fusionneur soient de familles différentes, ni que les lois de test soient tenues hors calibrage.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Lois tenues hors calibrage** : aucune famille de loi vue pendant l'étalonnage δ₀ ou le développement de la consigne ne figure au test ; sinon E0 mesure la mémoire.
2. **Tricheur de forme** (classifieur sur vocabulaire hors domaine) : s'il approche l'oracle, le monde fuit par B1.
3. **Fille constante** (toujours la loi modale) et **fille-copie-B-renommée** : les deux doivent être rejetées par le critère ; si l'une passe, (ii)/(iii) ne mesurent pas le transfert.
4. **Extracteur aveugle** : vocabulaire de relations fermé, figé avant E2 ; contrôle d'échange de mots-clés entre homonyme et jumeau ; contrôle « graphes tous identiques » (rappel 1, fausses alertes 1 doit déclencher un rejet de l'extracteur).
5. **Mondes sans pont mélangés en aveugle** aux mondes avec pont, dans le même lot ; sinon le taux d'abstention correcte est un artefact de lot.
6. **E3** : exclusion des paires de concepts frères (ou stratification par distance taxonomique) ; paires-leurres « disjointes avant, disjointes après » appariées par degrés ; sinon précision@K ne mesure que la topologie.
7. **Évaluateur de (ii) mécanique** ou, à défaut, étalonnage A/A du juge-modèle avec son propre δ₀.
8. **Pari couvert mécanisé** : une fille disjonctive doit être rejetée par une mesure de risque écrite avant E0.

---

## Contre la proposition C

### (a) Failles

**C1. L'expérience 1 compare un balayage exhaustif à un échantillon de 4 : le budget est le confondant.** La grille lit « directement » toute colonne d'opérateur, donc inspecte les C(30,2) = 435 paires ; c5 tire k = 4 éléments. La probabilité qu'un tirage de 4 parmi 30 contienne une paire plantée donnée vaut C(28,2)/C(30,4) = 378/27 405 ≈ 0,014 (illustratif, calcul montré). Avec 2 paires par monde et un tirage par monde, le rappel de c5 est ≈ 0,03 avant toute considération de noyau : la « falsification de H_A » (rappel < 0,50) est acquise d'avance, et H_B n'est pas opposée à H_A mais à un bras sous-doté. C ne dit pas combien de tirages par monde ; sans égalité du nombre de paires envoyées à la fusion, le résultat ne porte pas sur le mécanisme.

**C2. H_B est une conjonction de trois changements.** Grille (sélection) + arbre syntaxique canonisé (représentation) + b+ (filtre), contre c5 « sur n-grammes/mots ». Si H_B l'emporte, rien ne dit lequel des trois porte le gain ; si c'est l'AST, la grille n'est pas validée. Le témoin K-means (instrument 2) et la grille utilisent la même grappe de domaines : pas d'indépendance.

**C3. Les leurres sont définis par ce que l'instrument détecte.** « Chimères homonymes : même mot d'opérateur mais contraintes contradictoires ou structures d'arbres incompatibles » — exactement ce que l'AST et le filtre de contraintes voient ; « hubs : f_fond > 0,30 » contre un seuil b+ à 0,10 — marge de 3× sans aucun cas près du seuil. Le monde est vrai par construction pour H_B. C3b note que b+ n'a été testé qu'avec un corpus de fond synthétique de 300 textes et que l'archive de l'organisme comme fond « n'est pas vérifié » (RAPPORTÉ).

**C4. Le corpus de fond est aussi l'archive de la question : fuite instrument/évaluation.** Si le fond est l'archive de l'organisme, il est constitué des moissons passées *sur les mêmes questions* (les 5 textes de gen 18 répondent à une seule question, RAPPORTÉ). Les opérateurs pertinents pour la question y sont sur-représentés, dépassent f_fond = 0,10 et sont rejetés comme hubs : b+ inversé, précisément sur les pivots qu'on cherche (HYPOTHÈSE). Le même fond sert ensuite à mesurer la « rétention ».

**C5. La grille garde le max de q par cellule, et q est la pertinence à la question.** Chaque cellule retient l'élément le plus proche de la question ; les paires candidates partagent donc d'abord le vocabulaire de la question, ce qui est la pathologie déjà vue dans `termes_satures` (9 des 35 ex aequo de gen 18 sont des mots de la question, RAPPORTÉ). La diversité d'opérateurs est écrasée par la pertinence.

**C6. Le critère anti-juxtaposition est vide pour des parents bisociatifs.** Condition 2 : ∀x ∈ D(H_A) ∩ D(H_C), JS ≥ δ_div. Des parents de domaines éloignés ont, par hypothèse de l'étage, D(H_A) ∩ D(H_C) = ∅ : le quantificateur universel est vacuement vrai et la condition ne rejette rien. Inversement, quand l'intersection est non vide, une fille *correcte* (qui prolonge A là où A a raison) y coïncide avec A et est rejetée. Le critère punit les bonnes filles et laisse passer les mauvaises, selon la géométrie des domaines.

**C7. Contenu = KL × |D| se gonfle sans prédire.** Déclarer un D plus large avec les mêmes prédictions, ou prédire plus extrême (KL plus grand) sur la zone d'interaction, augmente Contenu avant tout tirage frais. L'étage 3 (Ville) ne corrige que si la zone d'interaction reçoit assez de tirages : sur « instances d'interaction » rares, M_t reste près de 1 pour la fille comme pour des parents qui n'y parient pas ; « dépasser max(M_t parents) » se fait par ε.

**C8. Expérience 3 dépend d'un banc qui n'existe pas.** « 50 paires d'hypothèses parentes survivantes » du banc R-525 : R-525 dit les critères « écrits, non courus » (RAPPORTÉ). Expérience 3 n'est pas lançable en 48 h ; le budget « 6,50 USD » suppose un intrant absent.

**C9. Expérience 2 : sélection des cas par qui connaît la réponse.** Les 30 « cas documentés » sont choisis parce qu'un article de jonction J existe avec un opérateur hybride explicite : survivants. L'opérateur de J, connu du constructeur, définit aussi le succès « paire partageant exactement le même opérateur formel » : fuite. Les deux vrais parents sont ceux que J co-cite, donc souvent les plus cités de leur lignée : un témoin par degré (absent chez C) pourrait les trouver sans opérateur. Enfin, l'anonymisation ne masque ni les équations ni les valeurs numériques, empreintes suffisantes pour un modèle contaminé.

**C10. Argument de coût contre le DPP mal fondé.** C invoque « Jacobi > 120 rotations à 20×20 » (RAPPORTÉ) pour écarter le DPP ; mais la sélection gloutonne c1/c5 n'utilise pas Jacobi (déterminants par élimination), à 16×16 l'erreur reste ≤ 0,51 % (RAPPORTÉ), et l'énumération exacte à n ≤ 50, k = 4 coûte 230 300 déterminants 4×4. Le rejet du DPP doit se faire sur E1-budget-égal, pas sur un coût de calcul inexistant.

**C11. Statuts.** C marque « VÉRIFIÉ » ses quatre références ; les attributions sont justes à ma connaissance, mais « VÉRIFIÉ » est auto-déclaré, aucun agent n'a vérifié. C écrit « les essais C3a/C3b prouvent » : ils sont RAPPORTÉ, non revérifiés. La lecture « c5 tire 4 à l'aveugle puis cherche une paire » est marquée OBSERVÉ-NON-AUDITÉ, correctement, mais le reste du raisonnement (C1, C3) la traite comme acquise.

### (b) Scénarios d'évasion

Agent adverse : l'extracteur d'opérateurs (brique 1), le modèle de fusion (brique 3), ou un agent qui écrit des hypothèses.

- **Grille + b+** : émettre pour deux éléments de domaines différents un même jeton d'opérateur rare, inventé. Rare par construction, il passe b+ (f_fond ≈ 0) et crée une colonne à deux cellules : pont garanti. Coût : nul. Variante de sabotage : inonder l'archive de fond d'un vrai pivot pour le faire dépasser 0,10.
- **Filtre à deux étages** : paraphraser les contraintes hors lexique (34,4 % de fuite en régime réaliste, RAPPORTÉ) ; sur l'AST, déclarer des plages de paramètres larges : « intersection non vide » toujours satisfaite. Coût : nul.
- **Instrument 5 (divergence sur grille d'entrées)** : fille = A + bruit ε ; elle n'est égale à A, C ou leur moyenne sur aucun point, donc passe le rejet « > 80 % d'égalités ». Coût : nul.
- **Critère Popper–Lakatos** : D déclaré plus large, prédiction extrême sur l'interaction (C7) ; vacuité de la condition 2 quand les domaines sont disjoints (C6). Coût : nul.
- **Ville sur l'interaction** : parier agressivement là où les parents ne parient pas ; avec peu de tirages frais, M_t de la fille dépasse 1 par ε tandis que les parents restent à 1. Coût : une variance acceptée.
- **Rétrodiction** : mémoire post-T₀, équations et nombres comme empreintes malgré l'anonymisation ; ou choisir la paire la plus citée dans chaque grappe (C9). Coût : nul.
- **Tous à la fois** : extracteur émettant un opérateur rare partagé + plages larges + fille « A + ε » à domaine déclaré élargi + pari extrême sur une interaction peu échantillonnée. Chaque brique de C est franchie par une politique fixe ; aucune n'exige une seconde famille de modèle ni un vocabulaire d'opérateurs fermé.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Budget égal** : même nombre de paires envoyées à la fusion pour la grille et pour c5 (c5 répété jusqu'à égalité, ou grille tronquée) ; sinon C1 est acquis.
2. **Ablation croisée** : grille sur n-grammes, c5 sur AST, b+ débranché dans chaque bras ; sinon C2.
3. **Hubs au voisinage du seuil** (f_fond ∈ [0,08 ; 0,12], illustratif) et **pivots dont la fréquence de fond dépasse 0,10 par héritage de la question** ; sinon C3–C4 restent invisibles.
4. **Fond indépendant de la question** : archive expurgée des moissons sur la question courante, et mesure séparée de la rétention des pivots de la question.
5. **Opérateur fabriqué** : planter des paires à jeton rare partagé sans structure commune ; la grille doit les rejeter (donc l'AST doit être obligatoire, pas optionnel), sinon b+ est une porte.
6. **Rapport de la taille de D(H_A) ∩ D(H_C)** sur chaque paire ; condition 2 déclarée « non applicable » quand elle est vide, et remplacée par un critère sur la zone d'interaction (C6).
7. **Filles adverses obligatoires** : A + ε ; A à domaine élargi ; prédiction extrême à faible échantillon ; toutes doivent être rejetées avant que le juge d'excès de contenu soit admis.
8. **Nombre minimal de tirages frais en zone d'interaction** figé avant, sinon Ville est vide (C7).
9. **Rétrodiction** : témoin par degré et par voisins communs ; faux parents (éléments les plus cités de chaque grappe, non co-cités par J) ; sélection des cas et extraction de l'opérateur de J par deux personnes différentes, préenregistrées ; contrôle T₀ décalé (liens déjà existants « prédits »).
10. **Dépendance déclarée** : Expérience 3 marquée « non lançable tant que le banc R-525 n'a pas couru » ; sinon le budget et le calendrier de C sont faux.

---

## Ce que je retiens des deux, en le disant (B1)

Je me sers de deux choses. De B : l'ordre « fusion avant tirage » (E0 d'abord) est juste en principe, à condition que E0 ne se joue pas sur un monde dont la forme fuit (B1) et que « déductible d'un parent » soit mécanisé avec la table de correspondance incluse (B4). De C : la grille Domaine × Opérateur est un bon *témoin exhaustif* du tirage à budget égal, pas un moteur validé ; et la vacuité de sa condition anti-juxtaposition sur domaines disjoints est, à mes yeux, la faille la plus grave de ce tour, parce qu'elle est algébrique et non empirique (HYPOTHÈSE sur le constat, vérifiable par lecture de la formule).

Ce qui réfuterait mes attaques : (i) B montre qu'un tricheur sur vocabulaire de forme reste au hasard sur son monde ; (ii) C montre, à budget égal, un gain de rappel de la grille ≥ 12 points (seuil R-525, RAPPORTÉ) avec AST et b+ débranchés ; (iii) l'un ou l'autre montre qu'une fille « A + ε » est rejetée par son critère sans règle ad hoc.

FIN-DE-CELLULE