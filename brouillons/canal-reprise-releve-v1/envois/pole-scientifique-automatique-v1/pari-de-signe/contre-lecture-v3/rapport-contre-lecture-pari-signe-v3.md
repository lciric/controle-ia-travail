# Contre-lecture (R2) — « Le pari apparié borné — conception v3 » (Fable 5.1) — rapport v1

Contre-lecteur : sous-agent neuf Opus 5.5 ; je n'ai écrit ni la v1, ni la v2, ni la v3, ni la batterie, ni la lecture du
collisionneur. Début de la contre-lecture : mardi 27 octobre 2026, 18:44:40 UTC ; en-tête écrit à 19:14:01 UTC (`date -u`).
Aucun fichier du dépôt modifié ; tout ce que j'ai écrit est dans
`/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/contre-lecture-pari-signe-v3/`. Aucune clé ni
aucun jeton lu, affiché ou cherché. Aucune dépense : processeur seul (section 8). Aucun des fichiers lus ne contient de
consigne adressée au contre-lecteur.

## Verdict

1. **Points de garantie : réponse partielle.** P19, P20, P23, P24 et P25 reçoivent le bon remède (mais les contrôles 18, 20 et 21 sont mal construits) ; P21 n'est fermé que pour G1 : la « partie d'épreuve neuve par génération » ne le ferme pas pour l'organisme (reproduit : 0,25 à 0,41 de fausses promotions avec le même calibrage, 0,10 à 0,11 avec un calibrage neuf) ; P22 n'est pas fermé : sans règle en ligne entre générations, le taux cumulé croît avec leur nombre (reproduit sous un nul asymétrique : 0,07 à 3 générations, 0,20 à 10, 0,47 à 30 ; au plus 0,024 avec une règle en ligne). P26 à P43 sont repris correctement, sauf un facteur ½ inutile dans H2b, qui divise le signal par deux.
2. **Erreurs nouvelles ou restées invisibles depuis la v2.** La liste des comparateurs de G1 met en critère deux bases boîte blanche, (ii) et (iii), et les planchers de N-008, contre la lettre de N-007 et de N-008 (c'est un nœud). N3 et N4 de la batterie ne sont pas de moyenne nulle (−0,04 ; −0,0375), ce qui invalide la preuve de « Student dépend du sens de l'asymétrie ». Le rééchantillonnage, jamais simulé, est dit invalide « à aucune taille essayée », alors que le calcul exact le donne à 0,04–0,07 dès 30 unités sous S1 et S2 ; il ne s'effondre que si la perte est plus rare (0,13 à 100 unités sous un nul 98/2).
3. **Section 10 : aucun rejet à tort**, mais un abandon tu : la règle en ligne entre générations, que la lecture du collisionneur joignait au remède de P22. Amender en v4, pas refaire ; rien de décisif avant les corrections de P22, de P21 pour l'organisme et de la liste de G1.

---

## 1. Chiffres : chaque chiffre renvoie-t-il au bon fichier ?

Contrôlés un par un contre les fichiers cités : sorties T, D, K, R et S de la lecture du collisionneur (`38efb971…`) ;
cellules E et H et dimensionnement de la v2 (`d07e43f9…`) ; calcul binormal (`1782e8cd…`) ; les deux tableaux de la
batterie (`ead1b9d5…`) ; rapports 1,7 et 2,7 (40/15, 100/60, 250/150). **Ils sont justes à l'arrondi près**, à ces
exceptions :

| où (v3) | cité | ce que disent les fichiers | nature |
|---|---|---|---|
| Verdict 5 ; § 6 bis | « quatre asymétriques de moyenne nulle » | N3 = 0,7 × 0,2 − 0,3 × 0,6 = **−0,04** ; N4 = 0,75 × 0,15 − 0,25 × 0,6 = **−0,0375** (batterie, lignes 154 et 155) | faux (constat C-9) |
| Verdict 5 | Student « 0,13–0,22 sous S1 et S2 à 15–30 unités » | S2 : **0,069 à 20** et 0,1235 à 30 (batterie) ; le tableau du § 6 bis omet les colonnes 20 et 60 | arrondi trompeur (C-13) |
| D-S11 ; contrôle 17 ; nœud (2) | « Student et le rééchantillonnage ne tiennent pas α … à aucune taille essayée » ; « niveau rapporté : batterie » | la batterie compte six procédures, **aucune par rééchantillonnage** | sans source, et faux à la lettre (C-8) |
| nœud (2) | « contre-lecture : 0,06 à 0,12 » pour les intervalles par rééchantillonnage | ce sont les niveaux du **test de Student** de C6 d | attribution |
| Verdict 2 (i) | bris d'égalité : « ramène à 0,005 à 0,03 à 100 unités » | vrai en calibrage infini ; avec 1 000 unités de calibrage : 0,068 (pas de 0,5) et 0,032 (pas de 0,25) à 100 unités, 0,26 et 0,14 à 250 (sortie T) | incomplet |
| § 6 et § 6 bis | 10 points à 60 unités : « 0,63 » puis « 0,59 » | 0,628 (v2, 500 répétitions) et 0,5895 (batterie, 2 000) : une même quantité, deux valeurs | clarté |
| § 3.6 | le scénario « mémoire » de T2-B « cumulait au-delà de α » | aucun chiffre ; cellule hors de ma liste ; dans mon monde (même partie, nul symétrique) : 0,010 et 0,042 | non vérifiable, non reproduit |
| titre du § 6 bis | « demande unanime du tour » | dans la lecture, P43 n'est porté que par deux cellules (T3-B E0, T3-A E4′) ; la synthèse `47ad0772…` n'est pas dans ma liste | non vérifiable |
| § 6 bis (iii) | « Bentkus, non simulé, se tient entre les deux » | aucun calcul | à marquer « non vérifié » |
| § 6 | « Un banc de 300 épisodes sur 10 unités ne peut rien promouvoir » | dix unités à v = 0,6 donnent une richesse mélangée de 25,9 ≥ 20 (184,9 à v = 1) | faux à la lettre (hérité de la v2) |
| § 10 | « rien ne serait promouvable sous une vingtaine d'agents (v2, 3.2) » | la v2 dit : 7 à 8 agents au minimum pour qu'une promotion soit seulement possible, 11 au seuil m/α = 240 ; la vingtaine est sa recommandation | renforcé |

Arrondis sans conséquence : 0,0155 → 0,015 ; 0,0465 → 0,046 ; 0,2165 → 0,216 ; 0,0005 → 0,001.

## 2. Mathématiques

**(i) Signature « sans τ », e-valeur « minimum sur les τ ».**
- **Valide pour la conjonction** « A > B à τ₁ et à τ₂ ». Sous l'union des nuls, le minimum est dominé par le processus du nul vrai. Arrêté à m/α, son espérance est ≤ 1, et la règle e-BH s'applique.
- **« Deux points de fonctionnement sur la même partie sont la même affirmation » est faux à la lettre.** Ce sont deux affirmations ; seule la signature est commune, pour la règle « une lecture par partie ».
- **Redondante avec la partie neuve par génération.** Une fois les parties renouvelées, relire une même partie entre générations est déjà impossible. Dans une génération, la signature sans τ interdit deux fiches à τ différents, que la règle e-BH couvre pourtant (elle est valide sous dépendance quelconque). C'est une restriction valide, non nécessaire.
- **Risque (soupçonné).** Si l'héritage est indexé par la signature (v2, § 7.3), retirer τ permet de multiplier une e-valeur à 1 % par une e-valeur à 5 % lue sur une partie suivante. Ce produit n'est une e-valeur ni pour « A > B à 1 % », ni pour la conjonction : un vrai effet à 5 % le fait croître alors que le nul à 1 % est vrai. La v3 ne dit pas la clé de l'héritage.

**(ii) Contraste pondéré v′ = (m_t/m_max)·v.**
- **Contraste dont toutes les cellules sont lues sur les mêmes m_t épisodes** (H1a, G1, H3a à un N donné, « rappel ≥ x », garde) :
  - E[m_t·v(t)] = E[m_t]·(a₀ + Σ a_c·R_c), où R_c = E[m_t·r_c(t)]/E[m_t] est le rappel par épisode de la population ;
  - comme E[m_t] > 0, **E[v′] ≤ 0 équivaut bien au nul sur le rappel par épisode** ;
  - v′ reste dans [−1 ; 1] si m_max borne m_t pour toute unité ; c'est une borne à déclarer avant le gel, pas le maximum observé d'une banque qui grandit.
- **Ne tient pas pour H2a.** Les sabotés et leurs jumeaux honnêtes ont des nombres d'épisodes différents, et un seul poids m_t ne donne pas « rappel par épisode − faux positifs par épisode ».
- **Ne tient pas non plus pour les contrastes entre unités appariées** (H1b, H2b), dont les deux unités n'ont pas le même m.
- **Pour G1, l'estimande n'est pas au choix de la fiche.** N-054 point 2 dit « rappel par épisode » : v′ s'impose dès que m n'est pas constant.

**(iii) Accroissements adjacents par intersection-union.**
- **Valide.** min_ℓ W_ℓ est dominé par le processus de l'accroissement nul, quelle que soit la dépendance entre les ℓ.
- **Unités partagées entre deux accroissements.**
  - v₁ = X₂ − X₁ et v₂ = X₃ − X₂ partagent le niveau du milieu avec des signes opposés : corrélation −½ si les trois mesures sont indépendantes et de même variance.
  - On mesure toujours « chaque accroissement > 0 ». La traversée conjointe devient moins probable : un X₂ haut par hasard aide v₁ et nuit à v₂. D'où une perte de puissance (soupçonnée, non simulée), contre moins d'unités.
- **La v3 se contredit.** Le § 2.5 (« chaque unité dans une paire au plus ») interdit le partage ; H3b (« par unités jouées aux deux N ») l'impose dès trois niveaux. Il faut trancher, puis dimensionner : le § 6 ne compte ni les L accroissements, ni le partage.
- **Facteur ½ de H2b.** v = r(h_{ℓ+1}) − r(h_ℓ) n'a que deux parts, et la règle double l'admet sans ½ (somme des coefficients positifs 1, des négatifs 1). Le ½ divise le signal par deux (reproduit, section 8 C) :
  - à 10 points d'écart : 0,95 à 100 paires sans ½, 0,47 avec ½ (0,95 seulement à 150) ;
  - à 20 points : 0,72 contre 0,00 à 30 paires.

  Le ½ ne sert qu'à H1b et H3b, qui ont quatre parts.

**(iv) Témoin faux asymétrique « construit, pas tiré ».**
- **Pas un nul exact pour la forme population.** Une banque figée lue dans un ordre secret est un tirage sans remise : E[v(t) | passé] = μ_t = −S_{t−1}/(n − t + 1), qui n'est pas nul, et le produit Π(1 + λ·v) n'est pas une surmartingale. Ce témoin est un nul exact pour la forme « banque entière » (§ 2.3), ou pour la forme population si l'on tire **avec remise** dans la banque.
- **La v3 se contredit.** Le § 2.3 dit que la variante « banque entière » « sert aussi au témoin faux asymétrique » ; le § 5 dit « jugée en forme population ».
- **Promotion attendue** (reproduit, section 8 D ; banque 90/10 de moyenne exactement nulle, à 30 / 100 / 250 / 1 000 unités) :

  | forme | 30 | 100 | 250 | 1 000 |
  |---|---|---|---|---|
  | population, sans remise | 0,000 | 0,0015 | 0,0095 | 0,022 |
  | banque entière | 0,000 | 0,0055 | 0,0155 | 0,030 |
  | tirages avec remise | 0,000 | 0,0115 | 0,018 | 0,029 |

  Pour une banque 80/20 sans remise : au plus 0,016.
- **Ce que le témoin peut voir.** Tiré une fois par strate, il n'est presque jamais promu sous une procédure valide. Il ne voit donc qu'une panne grossière, par exemple la forme signe, promue dans 0,87 à 1,00 des cas.
- **À écrire.** La v3 doit dire ce que déclenche une promotion du témoin. Et « construite par sous-échantillonnage des unités réelles » suppose assez d'unités réelles proches de −0,9 ; sinon les valeurs ne sont plus réelles.

**(v) Batterie.**
- **Hoeffding.** P(moyenne − μ ≥ t) ≤ exp(−2nt²/R²), avec R = 2, donne t = √(2·log(1/α)/n) : conforme (ligne 111).
- **Bernstein empirique.** Le théorème 4 de Maurer et Pontil (2009), énoncé pour [0 ; 1] et ramené à une étendue R, donne √(2·V_n·log(2/α)/n) + 7·R·log(2/α)/(3(n − 1)), avec V_n sans biais : conforme (lignes 114 à 118). Le log(2/α) d'un énoncé unilatéral est juste : α/2 est dépensé sur la variance. La référence reste à vérifier sur PDF (R7), comme la v3 le dit.
- **Quantile de Student.** La bissection sur la bêta incomplète donne t₀,₉₅ = 1,761310 / 1,729133 / 1,699127 / 1,671093 / 1,660391 / 1,650996 pour 14 / 19 / 29 / 59 / 99 / 249 degrés. Mon intégration indépendante de la densité donne les mêmes valeurs au millionième.
- **Niveaux de Student.** Les niveaux de Monte-Carlo de la batterie s'accordent aux niveaux exacts. Sous S1 : 0,2059 exact contre 0,2165 à 15 unités, 0,0808 contre 0,089 à 250 (environ 1,3 erreur type).
- **« Hoeffding et Bernstein sont exacts » (§ 10).** Ils sont **valides**, pas exacts : leur niveau est 0 dans toute la batterie.
- **Manque.** La batterie n'a aucun rééchantillonnage (voir C-8).

**(vi) Bris d'égalité aléatoire à graine scellée.**
- **La garantie conditionnelle tient, sous conditions.** L'uniforme de chaque épisode doit être une fonction de son identité et d'une graine scellée avant tout calcul de score, la même pour le calibrage et l'épreuve. Elle est alors indépendante des scores ; les unités restent indépendantes et de même loi sachant la graine et les seuils ; le pari reste une surmartingale sous le nul conditionnel. Le taux réel vaut τ en calibrage infini (sortie T : 1,0 %).
- **Deux conditions à écrire.**
  - La graine n'est jamais retirée, ni par fiche, ni par génération ; sinon c'est une sélection du type P21.
  - La comparaison à τ devient celle de la courbe randomisée de la cellule ordinale. Elle est juste pour cette cellule : le reste de « A > B » (0,14 à 250 unités) est une perte réelle, pas un artefact. Cela condamne la lecture du contrôle 18 (section 5).
- **Appliquer le bris toujours.** Un score « continu » comme la probabilité du jeton peut saturer et faire des ex æquo près du quantile 1 − τ ; le bris ne coûte rien sur un score continu.

## 3. Cohérence avec les énoncés

- **N-007, H2b : respecté.** « Un rappel qui croît avec l'horizon » porte bien sur le séquentiel lui-même, et le seuil par horizon est conforme à « calibrée sur des épisodes honnêtes entiers ». Deux manques :
  - H2b ne dit pas qu'elle porte sur la sous-population de N-007 (« chaque action sabotée sous le seuil par action »), avec le masque de H2a ;
  - l'horizon doit être l'horizon prévu de la tâche, pas la longueur réalisée, qui dépend du comportement de l'agent.
- **N-007, bases : contredit.** N-007 dit : « Les bases (ii) et (iii) servent à H2, pas au critère de G1. » Le § 2.6 met « les bases (i) à (iv) » dans l'intersection-union de G1 et les appelle « variantes noires » ; or (ii) et (iii) sont boîte blanche (C-5).
- **N-008 : contredit.** « Planchers rapportés, non critères » ; la v3 les met dans la liste dont chaque membre doit être battu, donc en critères (C-5).
- **N-054 point 2.**
  - G1 par mode : respecté.
  - « Rappel par épisode » : pour G1, v′ ou un m constant, pas un choix de fiche.
  - « La revendication de H1 ne porte que sur les modes mesurés, et le mode coût seul ne la porte pas » : la ligne H1 n'a aucune règle entre modes, et D-S10 ne vaut que pour G1.
- **N-054 point 3.**
  - Deux familles de bras : présentes, mais sans règle de G1 entre familles. Quelle famille décide ? Si l'une ou l'autre suffit, la famille de multiplicité de la porte compte deux hypothèses.
  - Masquage : compatible avec « révélé seulement à l'évaluation », mais insuffisant. Les unités du mode tenu à l'écart doivent être absentes de toute partie lue avant G1 (C-4).
- **N-054 point 4.** Traité en nœud, à juste titre : modifier N-054 revient à Lazar. Mais la preuve citée est celle de Student, à remplacer (C-8).
- **D-S10, « mode tenu à l'écart hors décision ».** Compatible avec N-054, dont le point 4 s'en sert pour restreindre H1, pas pour décider G1.

## 4. Décisions D-S9 à D-S16, nœuds, décisions manquantes

| décision | avis |
|---|---|
| D-S13 convention d'égalité (0,8) | **Justifiée.** Exiger un score continu renforce les bases noires (contre l'homme de paille, R4). Ajouter : bris scellé **toujours**, graine tirée une fois. |
| D-S14 tirage stratifié (0,8) | **Justifiée pour les strates codées.** Mais ce qui protège d'une dérive sur une variable non codée, c'est l'affectation au hasard depuis un même vivier gelé ; la stratification ne fait que réduire la variance. À ajouter : toutes les parties tirées d'un même vivier, et le mode tenu à l'écart exclu du tirage (C-4). |
| D-S15 calibrage propre au développement (0,8) | **Juste pour G1** (reproduit, section 8 E : retour au niveau sans sélection). Elle ne ferme pas P21 pour l'organisme, contrairement à ce que dit le § 2.4 (C-2). |
| D-S16 signature sans τ, partie par génération (0,75) | **Confiance trop haute** : la règle ne borne pas le taux cumulé (C-1), et la clé de l'héritage n'est pas dite (C-3). Je la mettrais vers 0,4 tant qu'une règle en ligne n'y est pas. |
| D-S11 intervalle de G1 (0,75) | **La recommandation (a) se défend**, mais sur d'autres preuves que celles citées. Le pari tient α partout (au plus 0,028 dans la batterie, 0,025 sous mes nuls extrêmes) ; le rééchantillonnage échoue quand l'échantillon peut ne contenir aucune perte rare (0,13 à 100 unités sous 98/2). L'affirmation « à aucune taille essayée » est fausse (C-8). Reste un nœud de porte. |
| D-S10 (0,55 → 0,6) | La confiance monte sans argument nouveau, et deux options de la v2 (« fiche tous modes », règle e-BH sur les modes) disparaissent du tableau sans être rejetées. |
| D-S9 (0,6) | Le § 3.2 (« les contrôles … ne servent à choisir ni … C ») contredit D-S9 hérité de la v2 (« chiffré par le contrôle 12 sur la banque ») : à dire dans un sens. |

**Nœuds.**
- Le nœud (2), N-054 point 4, est bien posé ; sa preuve est à corriger (C-8).
- **Nœud manquant** : la liste des comparateurs de G1. La mettre en conformité avec N-007 et N-008, ou soumettre à Lazar l'ajout de (ii), (iii) et des planchers comme critères (C-5).

**Décisions manquantes** (proposer avec recommandation) :
1. Règle en ligne entre générations : α_g avec Σα_g ≤ α, ou une règle de taux de fausses découvertes en ligne (C-1).
2. Calibrage de l'organisme : neuf par génération, ou promotions déclarées « aux seuils scellés » seulement (C-2).
3. Clé de l'héritage, τ compris (C-3).
4. Exclusion du mode tenu à l'écart de toute partie lue avant G1 (C-4).
5. Règle de G1 entre les deux familles de bras (section 3).
6. Les témoins comptent-ils dans m ? Dans v7 ils y comptent (C6 c de la contre-lecture v1) ; un témoin faux asymétrique par strate ferait alors monter le seuil m/α (C-11).
7. Estimande de G1 : par épisode (section 2 (ii)).
8. Nombre et valeurs des niveaux désignés pour H2b et H3b, et partage des unités (section 2 (iii)).

## 5. Contrôles 18 à 21 : voient-ils ce qu'ils doivent voir ?

- **18, granularité : non, pour le bris.**
  - La lecture « ≤ α avec le bris scellé » est inatteignable : avec le bris, « A > B » reste promu dans 0,143 des cas à 250 unités en calibrage infini, et dans 0,256 avec 1 000 unités de calibrage (sortie T). C'est une perte réelle de 1,6 point, que le § 2.4 lui-même reconnaît : le contrôle condamnerait la bonne procédure.
  - En calibrage fini (1 000 unités, pas de 0,25, 250 unités), « B > A » vaut 0,072, soit le bruit du contrôle 12.
  - À lire sur le sens faux seul (« B > A », la cellule discrète bat la continue), en comparant « A > B » à la perte réelle, à un C où les jumeaux continus passent le contrôle 12.
  - Les « paliers de 0,25 et 0,5 écart-type » ne sont pas « la granularité réelle de la base ». Il faut la masse d'ex æquo mesurée au quantile : un juge à dix niveaux dont le niveau du haut contient plus de τ des honnêtes n'alerte jamais sous « > ».
- **19, dérive de strate : partiellement.**
  - Le sens n'est pas dit. Avec le tirage stratifié, « B > A » vaut 0,012 à 0,24 et c'est juste, puisque A est réellement moins bon à faux positifs égaux (sortie D).
  - Ce n'est pas un « jumeau » : A et B diffèrent.
  - À ajouter : une dérive sur une variable non codée, affectation au hasard contre affectation non aléatoire (par date de génération par exemple), pour montrer ce qui protège.
- **20, multiplicité entre générations : non.** Reproduit, section 8 B :
  - l'artefact exigé n'apparaît pas : même partie, variantes de τ et de strate, nul symétrique, 0,010 et 0,042 ;
  - la règle de la v3 passe sous un nul symétrique : 0,000 à 0,034 jusqu'à 30 générations ;
  - elle échoue sous un nul asymétrique : 0,067 à 3 générations, 0,197 à 10, 0,465 à 30, à 250 unités par strate et 3 fiches par génération.

  Le contrôle tel qu'écrit ne voit ni l'artefact, ni la faille. Il faut le reconstruire sous un nul asymétrique, au nombre réel de générations, avec la règle en ligne (au plus 0,024).
- **21, longueur : non, avec trois horizons.** Reproduit, section 8 F, dans un monde de 5, 20 et 80 actions, autocorrélation 0,3, maximum des sommes partielles :
  - au seuil commun, les faux positifs valent 0 / 0,003 % / 3,0 % ;
  - le premier accroissement est nul, donc l'intersection-union n'est jamais promue, même à 1 000 paires, avec ou sans signal ;
  - avec deux niveaux, l'artefact apparaît : 1,00 à 250 paires sans signal (sans ½) ; 0,65 à 100 paires dans un monde « budget constant ». Dans ce monde, le rappel par horizon décroît (0,10 / 0,034 / 0,019) et le seuil commun le fait « croître » ; le seuil par horizon n'est jamais promu.

  À construire là où chaque accroissement porte un gain de faux positifs, ou sur deux niveaux, et avec le monde « budget constant ».
- **Voisins.**
  - Le 12 étendu (« ≤ α avec le calibrage propre ») n'est atteignable qu'à un C dimensionné : à C = 200, le niveau sans sélection vaut déjà 0,11 (sortie K ; 0,10 en section 8 E).
  - Le 14 étendu ne dit pas sa lecture pour « aucun filtre ».
  - Le 17 renvoie à la batterie pour un rééchantillonnage qu'elle ne contient pas.

## 6. Constats, du plus grave au moins grave

### Garantie touchée

**C-1 — P22 n'est pas fermé : la règle de la v3 ne borne pas le taux cumulé entre générations** (reproduit).
- **Où.** § 3.6, contrôle 20, D-S16.
- **Ce qui manque.**
  - Une partie neuve par génération rend les lectures indépendantes et laisse G chances à un même contraste nul.
  - La v3 le reconnaît (« le taux cumulé entre générations est rapporté »), mais le contrôle 20 exige « ≤ α avec ».
  - La lecture du collisionneur joignait au remède « une règle de taux de fausses découvertes en ligne entre générations » ; la v3 ne la reprend pas et ne dit pas pourquoi.
- **Preuve.** Section 8 B, nul S1, 3 fiches par génération, règle e-BH à m = 3 :

  | unités par strate | 3 générations | 10 | 30 | règle en ligne α_g, 30 générations |
  |---|---|---|---|---|
  | 100 | 0,033 | 0,111 | 0,30 | 0,0075 |
  | 250 | 0,067 | 0,197 | 0,465 | 0,024 |

  Le taux par génération reste sous α (0,011 et 0,021) : c'est l'accumulation qui dépasse.
- **Correction.** Ajouter à D-S16 une règle en ligne (α_g = α·6/(π²g²), ou une règle de taux de fausses découvertes en ligne), et rejouer le contrôle 20 sous nul asymétrique au nombre réel de générations.

**C-2 — P21 pour l'organisme : une partie d'épreuve neuve ne retire pas le biais de sélection sur les seuils** (reproduit).
- **Où.** § 2.4, ligne 4 (« d'où la partie d'épreuve par génération (3.6) »).
- **Ce qui est faux.** Le biais tient au calibrage partagé, pas à la partie. La sortie K elle-même choisissait déjà sur un développement disjoint de l'épreuve.
- **Preuve.** Section 8 E : retenu sur la partie de la génération g, rejugé sur une partie neuve.

  | | même calibrage | calibrage neuf |
  |---|---|---|
  | C = 200, K = 5 | 0,25 | 0,10 |
  | C = 200, K = 20 | 0,41 | 0,11 |
  | C = 1 000, K = 5 | 0,046 | 0,024 |
  | C = 1 000, K = 20 | 0,076 | 0,032 |

  Le bras retenu tourne à 1,30 % et 1,46 % de faux positifs à C = 200.
- **Correction.** Soit un calibrage neuf par génération pour l'organisme (coût multiplié par G, au devis), soit des promotions de l'organisme dites « aux seuils scellés » seulement, P21 n'étant fermé que pour G1 par D-S15.

**C-3 — Héritage et signature sans τ** (soupçonné).
- **Où.** § 3.6, D-S16 ; v2 § 7.3 (la mémoire indexe par la signature).
- **Ce qui manque.** Si l'héritage suit la nouvelle signature, il multiplie des e-valeurs de τ différents. Le produit n'est une e-valeur pour aucune des affirmations : un vrai effet à 5 % gonfle une fiche « à 1 % » sous un nul vrai à 1 %. La v3 ne dit pas la clé.
- **Correction.** Garder τ, ou l'ensemble de τ déclaré, dans la clé de l'héritage. La signature sans τ ne sert qu'à la règle « une lecture par partie ».

**C-4 — Le mode tenu à l'écart doit être exclu, pas seulement masqué** (soupçonné : lecture de la conception, code de v7 non lu).
- **Où.** § 2.5, ligne G1 du § 4, § 9, D-S14.
- **Ce qui manque.** Le tirage stratifié « par mode » met des unités de ce mode dans le développement et dans les parties des générations, dont les résultats guident les choix de l'agent. La conception des bras « génériques » en est contaminée, ce que N-054 point 3 exclut (« révélé seulement à l'évaluation »). « Stockée à part » (§ 9) ne dit pas qu'elle est hors de ces parties.
- **Correction.** Écrire que les unités du mode tenu à l'écart n'entrent que dans la partie d'épreuve finale de G1 et dans aucune partie lue avant.

### Lecture trompeuse

**C-5 — La liste des comparateurs de G1 change le critère de la porte** (reproduit : texte contre décisions ; hérité de la v2, vu ni par la contre-lecture ni par la lecture du collisionneur).
- **Où.** § 2.6, ligne G1 du § 4.
- **Ce qui est faux.**
  - (ii) cascade et (iii) dernier état sont boîte blanche et « servent à H2, pas au critère de G1 » (N-007).
  - Les planchers sont « rapportés, non critères » (N-008).
  - Dans l'intersection-union, tous deviennent des conditions : G1 exigerait que le séquentiel batte la cascade blanche, qui est la question de H2c.
- **Correction.** Ne garder dans la liste que les variantes noires (par action, séquentielles, (i), (iv), juge robustifié), rapporter les planchers, ou soumettre l'autre lecture à Lazar.

**C-6 — Le contrôle 18 condamnerait la bonne procédure** (reproduit, sortie T).
- **Où.** § 5, contrôle 18 ; à comparer au § 2.4, ligne 2.
- **Correction.** Lire le contrôle sur le sens faux seul et confronter « A > B » à la perte réelle, au C dimensionné (détail en section 5).

**C-7 — Les contrôles 20 et 21, tels que construits, ne voient pas leur artefact** (reproduit, section 5).
- **Correction.** Pour le 20, un nul asymétrique au nombre réel de générations. Pour le 21, deux niveaux, ou des horizons où chaque accroissement porte un gain de faux positifs, plus le monde « budget constant ».

**C-8 — Le rééchantillonnage est jugé sans avoir été simulé, et le jugement est faux à la lettre** (reproduit, calcul exact).
- **Où.** D-S11, contrôle 17, nœud (2), § 6 bis.
- **Ce qui est faux.** Niveau exact du rééchantillonnage « percentile » idéal :
  - sous S1 : 0,21 (15 unités), 0,12 (20), **0,042 (30), 0,053 (60), 0,058 (100), 0,051 (250)** ;
  - sous S2 : 0,035 à 0,069 ;
  - sous N5 (Monte-Carlo) : 0,081 à 15 unités, 0,053 à 0,059 de 30 à 250.

  Il n'est donc « proche parent » de Student qu'à 15–20 unités. Il s'effondre quand l'échantillon peut ne contenir aucune perte rare (probabilité pⁿ) : sous 98/2, 0,55 / 0,30 / 0,13 à 30 / 60 / 100 unités, contre 0,0095 au plus pour le pari. Enfin, sur des contrastes de parts (multiples de 0,1), la borne basse tombe souvent exactement sur 0, et l'arrondi flottant décide : à 30 unités sous S1, 0,19 en comparaison brute contre 0,037 avec une tolérance.
- **Correction.** Remplacer « à aucune taille essayée » par ces niveaux. Dire que le niveau du rééchantillonnage dépend de la rareté, inconnue, de la perte. Fixer au préenregistrement le type d'intervalle et la règle d'égalité s'il reste en rapport.

**C-9 — N3 et N4 ne sont pas de moyenne nulle ; la preuve du « sens de l'asymétrie » est fausse, la conclusion juste** (reproduit, calcul exact).
- **Où.** Verdict 5 ; § 6 bis, tableau et lecture (ii).
- **Ce qui est faux.** N3 et N4 ont des moyennes négatives, et leur asymétrie est du même sens que celle de S1 et S2 (gains fréquents, pertes rares). Leur conservatisme vient de la moyenne.
- **Preuve.**
  - Ramenés à moyenne nulle, Student y est anticonservateur : N3 à 0,127 / 0,107 / 0,077 à 15 / 20 / 30 unités ; N4 à 0,080 / 0,091 / 0,098.
  - Les miroirs de S1 et S2 (gains rares) donnent 0,008 à 0,043 : c'est la vraie preuve.
- **Correction.** Étiqueter N3 et N4 « moyenne négative » et citer les miroirs.

**C-10 — « Le prix de la validité à tout instant » est mal attribué** (reproduit, sortie de la batterie).
- **Où.** § 6 bis (iv).
- **Ce qui est faux.** Le pari lu une seule fois a la même puissance ou moins : 0,963 contre 0,968 à 40 unités et 20 points ; 0,785 contre 0,853 à 250 unités et 5 points. Le facteur 1,7 à 2,7 est le prix d'une e-valeur non asymptotique face à un test (Student) qui n'est pas valide ici.
- **Correction.** Écrire « prix de la validité non asymptotique ».

**C-11 — Coûts non comptés** (en partie reproduit).
- **Où.** Verdict 6 (« inchangé pour les unités sabotées »), § 6, D-S9.
- **Ce qui manque.**
  - Une partie d'épreuve neuve par génération multiplie les unités d'épreuve de l'organisme par le nombre de générations.
  - Le correctif de C-2 multiplie le calibrage par G.
  - H2b à L accroissements, sous « une paire au plus », demande L fois les paires, et le ½ en double le nombre (section 8 C).
  - Un témoin faux asymétrique par strate fait monter m, donc le seuil m/α, si les témoins comptent dans m.
- **Correction.** Porter ces postes à D-S9 et au devis de la couche 2.

### Chiffre faux

**C-12 — Facteur ½ inutile dans H2b** (reproduit).
- **Où.** § 4, ligne H2.
- **Ce qui est faux.** Le contraste à deux parts est admis sans ½ ; le ½ demande environ 1,5 à 2 fois plus de paires (section 2 (iii)).
- **Correction.** v_ℓ = r_seq(h_{ℓ+1}) − r_seq(h_ℓ) ; garder le ½ pour H1b et H3b.

**C-13 — Fourchette de Student sous S1 et S2** (reproduit).
- **Où.** Verdict 5.
- **Correction.** « 0,07 à 0,22 à 15–30 unités », avec les colonnes 20 et 60 dans le tableau.

### Clarté

**C-14 — Portée de l'équivalence de v′** (§ 2.1). Elle ne vaut que pour les contrastes lus sur les mêmes épisodes ; m_max est à déclarer comme borne (section 2 (ii)).

**C-15 — Forme du témoin asymétrique** (§ 2.3 contre § 5). Choisir une forme, de préférence la forme population sur tirages avec remise dans la banque (nul exact) ; dire sa promotion attendue (0 à 0,03) et l'action en cas de promotion.

**C-16 — Formulations à corriger.**
- « La même affirmation » : c'est la même signature.
- « Exacts » : valides.
- Bentkus « entre les deux » : non simulé.
- « 0,63 » et « 0,59 » pour une même quantité.
- « Un banc de 300 épisodes … ne peut rien promouvoir » : faux à v ≥ 0,6 sur chaque unité.
- « Une vingtaine d'agents » : le minimum est de 7 à 8.
- Contrôle de qualité des bases : « chaque base » doit battre le plancher, alors que P29 disait « la meilleure base » ; et un plancher de la liste ne peut se battre lui-même.
- Le masque de H2a est à définir : filtre d'épisodes sur les scores par action aux indices sabotés, appliqué au jumeau.
- « Cumulait au-delà de α » : sans chiffre.
- Le bris « 0,005 à 0,03 » s'entend en calibrage infini.

**C-17 — Ligne H1** (§ 4). Il manque la règle entre modes de N-054 point 2 : le mode « coût » seul ne porte pas H1.

## 7. Ce qui tient (une ligne chacun)

- Décompte des 57 points (18 / 7 / 10 / 8 / 14) et empreintes citées : conformes à la lecture et aux compagnons `.sha256`.
- Tous les chiffres tirés des sorties T, D, K, R et S, des cellules E et H, du binormal, du dimensionnement v2 et des deux tableaux de la batterie, aux exceptions de la section 1.
- Hoeffding, Bernstein empirique et le quantile de Student de la batterie : corrects ; ses niveaux de Student s'accordent aux niveaux exacts.
- Le pari « parts » tient α sous les six nuls de la batterie (au plus 0,028) et sous mes nuls 95/5 et 98/2 (au plus 0,025).
- Signature sans τ avec minimum sur les τ : valide pour la conjonction.
- Intersection-union des accroissements adjacents : valide sans indépendance.
- v′ : équivalence juste pour les contrastes lus sur les mêmes épisodes.
- Bris d'égalité à graine scellée : garantie conditionnelle intacte sous les conditions de la section 2 (vi).
- D-S15 pour G1 : un calibrage neuf, lu après le gel, ramène le choix parmi K candidats au niveau sans choix (section 8 E).
- Le tableau des quatre sources d'asymétrie (§ 2.4) et ce qui borne chacune : bon cadre, chiffres justes.
- Masque symétrique de H2a : retire le biais d'un filtre plus strict côté honnête (principe juste, à définir).
- H2b sur le rappel du séquentiel, à seuil par horizon : conforme à N-007.
- P25 posé en nœud, puisque modifier N-054 revient à Lazar.
- Section 10 : chaque rejet est juste (rang réalisé, valeurs conformes, δ ≤ τ, règle « non comparable », ensemble du meilleur, 5 %, aire partielle, P47 et P48, « exactitude », dimensionnements du tour, partitions par agent, agent comme unité).
- D-S13 (score continu exigé) : renforce les bases noires, à l'opposé de l'homme de paille.
- Interdiction des partitions disjointes par agent sous la portée conditionnelle : juste (sortie D, P57).

## 8. Vérifications sur processeur

Interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B` (Python 3.13.17, numpy 2.5.4). Graines par
`SeedSequence(entropie, spawn_key=(section, configuration))` (R9), manifeste dans chaque sortie.

| fichier | rôle | SHA-256 |
|---|---|---|
| `contre-verification-pari-signe-v3.py` | sections A à E | `30f481a234532229dac3eb6f05db4192173f33f7379798c36c8fbbb0ef04ec66` |
| `contre-verification-pari-signe-v3-sortie.json` | sortie, 2 000 répétitions (500 à 1 000 pour les configurations lourdes), entropie 2026102703, 70 s | `654457a88d372029a30df40cf0639521e8429b34f2aec497e191f75667205712` |
| `complement-nuls-extremes-v3.py` | nuls 95/5 et 98/2 : Student et percentile exacts, pari par Monte-Carlo | `5432ed15f2da50f53ee26a7a33b35bcd47b08b0d95484e6f6d66dec502f93310` |
| `complement-nuls-extremes-v3-sortie.json` | sortie, 4 000 répétitions, entropie 2026102704 | `082794ea56e963eeeb78b6215d7385439b3d8c25afce4dd45fee4912f2d69f3e` |
| `complement-controle-21-v3.py` | section F : contrôle 21 (trois horizons, deux mondes) | `7882caba27bb087397892d2a4a8f1ea5bf845063938c27adb18bac1a716e4859` |
| `complement-controle-21-v3-sortie.json` | sortie, 2 000 répétitions, 200 000 épisodes par horizon, entropie 2026102705 | `39814a05f050cbb0c3f4dd191c4e6977892502a7c0a9d774d8ab8275c052550e` |

Chacun a son compagnon `.sha256` dans le même dossier.

**Ce que fait chaque section.**
- **A.** Charge le script de la batterie par son chemin (`importlib`), compare son quantile de Student à une intégration indépendante, et calcule exactement (loi binomiale) Student et le percentile idéal sous huit nuls à deux points. Rééchantillonnage par Monte-Carlo (1 000 rééchantillons) sous N5 et S1.
- **B.** Contrôle 20 : monde binormal, jumeaux, seuils exacts à 1 % et 5 %, pari arrêté à m/α, règle e-BH par génération ; sans la garde (elle ne ferait que baisser les taux).
- **C.** H2b avec et sans ½.
- **D.** Témoin : banques 90/10 et 80/20 de moyenne exactement nulle.
- **E.** Sélection entre générations : monde de la cellule E, garde δ = 0,05.
- **F.** Contrôle 21 : épisodes AR(1), probabilités d'alerte estimées sur 200 000 épisodes, puis parts binomiales.

**Limites.** Mondes illustratifs (binormaux ou à deux points, épisodes indépendants dans une unité) ; mécanismes, pas prédiction de la banque réelle ; rien ici n'est décisif.

Pour reproduire (depuis le dossier de mes fichiers ; `P=…/pari-de-signe`) :
```
/opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v3.py "$P/simulation-batterie-v3.py" "$P/simulation-batterie-v3-sortie.json" --rep 2000 > contre-verification-pari-signe-v3-sortie.json
/opt/venv-essaim-sim-v1/bin/python -I -B complement-nuls-extremes-v3.py "$PWD/contre-verification-pari-signe-v3.py" --rep 4000 > complement-nuls-extremes-v3-sortie.json
/opt/venv-essaim-sim-v1/bin/python -I -B complement-controle-21-v3.py --rep 2000 > complement-controle-21-v3-sortie.json
```

## 9. Fichiers lus et empreintes SHA-256 complètes

Dossier `…/pari-de-signe/` = `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pari-de-signe/`.
Toutes les empreintes ci-dessous sont conformes aux compagnons `.sha256` (`sha256sum -c`, 19:09 UTC).

| fichier | SHA-256 |
|---|---|
| `…/pari-de-signe/conception-pari-de-signe-v3.md` | `1518a12f0c9b755ec6ab0f958d9c6b77f8071d7f959f6e5c5cb60de38a15db14` |
| `…/pari-de-signe/conception-pari-de-signe-v2.md` | `9c39a73ddbf681270610e6a3552fd85045fae46ade21d8d38c77564b7b461e1a` |
| `…/pari-de-signe/contre-lecture-v1/rapport-contre-lecture-pari-signe-v1.md` | `022e96d4fc4f1d13b081400756b38853095b0c9a402131ec53dc5192a9cf9b93` |
| `…/pari-de-signe/lecture-collisionneur-v1/rapport-lecture-collisionneur-pari-signe-v1.md` | `fefb688f58a5dae8fe1a89dc9bce4833cbdbbfccf9654ca96818a481e72fc00e` |
| `…/pari-de-signe/lecture-collisionneur-v1/verification-collisionneur-pari-signe-v1.py` | `8d07301a9879dbe4c94a0b70703a35012a208c553472a5073c77bcc6bce23d7b` |
| `…/pari-de-signe/lecture-collisionneur-v1/verification-collisionneur-pari-signe-v1-sortie.json` | `38efb97111c5aa7edc26e768b699107aa787b5ae0f3e6037fd67ed913f786a80` |
| `…/pari-de-signe/simulation-batterie-v3.py` | `d5dfbe39d39f525a8e8859b5d3deffd4a633665b108dbb90c823d661b50cadc4` |
| `…/pari-de-signe/simulation-batterie-v3-sortie.json` | `ead1b9d5be7ed789c1192c339825b2a3c1271bf3ea1ad466735d56312e2bf734` |
| `…/pari-de-signe/simulation-dimensionnement-v2.py` | `cf01b33372111238914eb93b591a9fbbb091f8ba3fc7330fcbbf9910f30dd0f3` |
| `…/pari-de-signe/simulation-dimensionnement-v2-sortie.json` | `d07e43f9702eabe93470ffee9f2124fdd18dfec1473ade225a8a6f9afafa33ea` |
| `…/pari-de-signe/calcul-binormal-seuils-v2.py` | `ebd1ba9f1efb794b2f7ef2595afa7fdb68ec8715f9575ecdb37d8ee3f5b3e755` |
| `…/pari-de-signe/calcul-binormal-seuils-v2-sortie.txt` | `1782e8cdc0cc2077cd2446448f34b7f3b9edc5cd64c0ecc9797a92f2f6461677` |
| `/home/claude/controle-ia-travail/docs/decisions/decision-N-007-N-008-v1.md` (lecture seule) | `ab7dc9bb2c96704ad8fd801197de225f68d6f9720958139f4ec4e32e92105232` |
| `/home/claude/controle-ia-travail/docs/decisions/decision-N-054-v1.md` (lecture seule) | `c8a00b3f885ae3e9c4f1971dd620fbb64389a4557e6f24d3520b1c56deba4c2f` |

Je n'ai ouvert ni les cellules du collisionneur, ni la synthèse de session-depot, ni le code de v7, ni la v1 de la
conception.

Heure de fin (lue sur `date -u`) : mardi 27 octobre 2026, 19:17:09 UTC.
