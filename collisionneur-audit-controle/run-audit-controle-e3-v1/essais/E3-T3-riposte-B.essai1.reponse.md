# Proposition B, tour III.3 : riposte

**Pièces.** Les attaques de A et de C sont complètes : chacune se termine par sa ligne de clôture. Ma conception du tour III.1 est elle aussi complète.

**Statuts.** Ils ne changent pas. F1 et F3 restent RAPPORTÉ, F2 reste OBSERVÉ-NON-AUDITÉ. Tout ce qui suit est HYPOTHÈSE. Tout chiffre de seuil, d'effectif ou de coût est **illustratif**, sauf les calculs signalés comme tels, qui sont faits sur des effectifs eux-mêmes illustratifs.

**Périmètre.** Je ne réponds qu'aux sections « Contre la proposition B » de A et de C. J'utilise trois éléments tirés de leurs sections contre A, et je le dis à chaque fois (B1 du protocole).

---

## (a) Verdict sur chaque attaque

| # | Attaque | Verdict | Raison, ou test qui la remplace |
|---|---|---|---|
| A1 = C1 | La permutation *intra*-trajectoire ne détruit pas un effet commun à l'épisode. | **Acceptée.** | La somme des scores d'une trajectoire est invariante par permutation de ses pas. La valeur terminale E_T d'un processus e de mélange l'est aussi, car c'est une fonction symétrique des scores. Sous un effet d'épisode, ma clause de falsification ne pouvait donc presque jamais se déclencher. B1 est refait avec une permutation **inter**-trajectoires appariée sur l'indice de pas, proposée par C. |
| A2 | H_B de B1 est quasi infalsifiable. | **Acceptée.** | Calcul sur n = 500 (illustratif) : la borne haute de Clopper-Pearson vaut environ 0,74 % pour 0 faux positif et environ 1,1 % pour 1 faux positif. B1 devient un duel « taux ≤ 1 % contre taux ≥ 2 % ». L'effectif est dimensionné pour séparer les deux, et la zone indécise est déclarée d'avance. |
| A3 | « Un seul bit lu T fois » n'empêche pas le gain en √T. | **Acceptée en partie, transformée.** | Sur le plan statistique, A a raison. Un signal persistant lu avec un bruit indépendant s'accumule ; seule la corrélation des *résidus* plafonne le rappel. Ma formulation confondait les deux. Il reste une question de **construit** : si la sonde est élevée à tous les pas, qu'il y ait sabotage ou non, elle lit une disposition et non le déplacement *par action de sabotage* que pose l'hypothèse (a) du lemme. Cette question devient le duel 2 de B1′. |
| A3 bis | La formule n_eff suppose une corrélation échangeable. | **Acceptée.** | On compare un modèle AR(1) et un modèle équicorrélé sur la fonction d'autocorrélation honnête, avec un critère préenregistré. n_eff est calculé à partir du modèle retenu. |
| A3 ter | (ii), distillée de (i), ne contrôle pas l'absence de consigne persistante. | **Acceptée.** | Le contrôle se fait sur (iv) seule. (ii) est déclarée « indéterminée ». |
| CB1 | Le plafond du rappel peut venir de l'hétérogénéité des δ_i entre épisodes. | **Hypothèse rivale acceptée ; duel des chimères rejeté.** | Une trajectoire chimère mélange des pas venus de trajectoires différentes. Elle moyenne donc à la fois les δ_i et le bruit partagé, et son rappel remonte sous **les deux** hypothèses : elle ne les sépare pas. Je la remplace par une décomposition de variance (B1′). |
| A4 = C3 | d′ n'est qu'une transformation de plus ; les cellules à 0 ou 1 % divergent ; le contrôle semi-synthétique est vrai par construction. | **Acceptée.** | Sans modèle déclaré, aucune échelle n'est privilégiée. B2 devient un test de **prédiction** : celle du modèle même du lemme, faite sur les **scores continus** par ajustement binormal, et non sur des rappels seuillés. Il n'y a donc plus de divergence aux bornes. Le contrôle semi-synthétique est requalifié en test du code, et ne compte plus comme preuve. |
| A5 = CB2 | La longueur peut être un médiateur, pas un confondant. | **Acceptée, transformée.** | Le confondant se teste sur les épisodes **honnêtes** seuls, ce qui n'est pas touché par la médiation. La médiation se mesure directement. La validité incrémentale de la sonde se lit sans stratification (B3 corrigé). |
| A6 = C2 | B4 : le masquage à la lecture laisse ce que l'attention a déjà propagé ; le contrôle sur (ii) et (iv) est vide ou mal posé. | **Acceptée.** | Retirer des positions de l'agrégateur ne retire pas l'information recopiée dans les états des jetons d'action. J'utilise le mécanisme d'écho de C (AM-2), comme A. B4 ne peut donc pas tester « non textuel ». Il est rétrogradé en carte descriptive, et remplacé par un contraste (i) contre (iv) muni d'un détecteur d'écho positif (B4′). Le contrôle sur (ii) et (iv) est supprimé : dans le cas 1 de C, il est identiquement nul. |
| A7 | B5 confond trait et état ; l'écart S/K peut être trop ténu. | **Acceptée.** | J'ajoute une porte de dose sur iv-S. Je me sers aussi du biais de survie que C relève **contre A** : lire les épisodes non sabotés, c'est sélectionner sur l'issue. L'opportunité de sabotage est donc tirée **a priori** au niveau de la tâche. |
| C4 | iv-S et iv-K diffèrent par la personne grammaticale. | **Acceptée.** | J'ajoute iv-B : documents à la première personne qui décrivent une politique cachée bénigne. |
| A8 | Un nul d'interaction en B8 n'est pas interprétable, car deux effets de lignée de signes opposés peuvent se compenser. | **Acceptée.** | On décompose en **discrimination** (AUROC dans la lignée) et en **niveau** (suspicion moyenne sur les honnêtes). Un nul agrégé n'est plus lu comme un effet de capacité. |
| A8, coût | Le coût de B8 omet les organismes Qwen. | **Acceptée.** | Coût revu en (b). B8 se limite aux juges boîte noire, donc sans sondes Qwen. |
| Contrôle de A pour B8 | Neutraliser les marqueurs de style. | **Rejeté tel quel.** | C montre, **contre A**, qu'une paraphrase change le contenu et peut lisser le sabotage. La confusion entre lignée et style de surface reste une limite déclarée. |
| A9 | La famille scellée vient de la même recette. | **Acceptée.** | J'ajoute une famille de recette différente : (iii) si la licence le permet (F1 §7), sinon (iv). Le biais d'instance et le biais de recette sont rapportés séparément. |
| A10 | L'effectif de (c) suppose des actions indépendantes. | **Acceptée.** | L'unité statistique devient la trajectoire. Le taux par action est corrigé par l'effet de plan, avec un bootstrap par trajectoire. |
| A, 0,54 | Mon « 0,54 vient d'un résumé » est faux. | **Acceptée.** | F2 déclare avoir lu *Liars' Bench* en p. 1 et 7–10. Mon point ne vaut que pour 41 % contre 19 % et pour 9,8 % contre 2,8 %. |
| A, références | Mes attributions sont à vérifier sur la source. | **Acceptée.** | C'était déjà leur statut : le contenu que je leur prête vient de ma mémoire (HYPOTHÈSE). |
| Contrôle de A pour B1 | Ajouter des trajectoires honnêtes d'un autre jeu de tâches. | **Acceptée, comme bras séparé.** | Il sépare une dérive de distribution d'une dépendance. |
| CB3 | Réentraîner sur les seules détections peut aveugler la sonde aux attaques furtives. | **Transformée en test, adoptée.** | Les rappels sont lus séparément sur les attaques de type « attrapé » et de type « échappé » (R1 en (b)). |
| Contrôles de C pour B4 | Imputation neutre ; déclencheur lexical. | **Acceptés**, pour la carte descriptive. | |
| Contrôle de C pour B2 | Sensibilité au lissage ε aux bornes. | **Sans objet** après le passage aux scores continus. Conservé pour tout taux résiduel. | |

---

## (b) Expériences corrigées

Règles communes :
- seuil à 1 % de faux positifs, calibré sur des épisodes honnêtes disjoints ;
- bootstrap **par trajectoire** ;
- effectifs et marges illustratifs.

Chaque duel garde deux issues falsifiantes. La zone indécise est déclarée à l'avance et réduite par le dimensionnement.

### B1 corrigé : validité du nul du processus e

| | |
|---|---|
| **Données** | Trajectoires honnêtes, T ∈ {10, 50, 200}. Pour séparer 1 % de 2 % avec une puissance de 80 % (risque unilatéral de 5 %), il faut environ 800 trajectoires par T (calcul binomial ; valeurs illustratives). |
| **Conditions** | (R) ordre réel ; (P_inter) chaque pas t est remplacé par un pas t tiré d'une autre trajectoire honnête, ce qui garde la dérive de position et détruit l'effet d'épisode et l'autocorrélation ; (X) un autre jeu de tâches, avec le même seuil. |
| **Statistique** | Fraction des trajectoires où sup_t E_t ≥ 1/α. |
| **H_A** | Taux de faux positifs de R ≤ α. |
| **H_B** | Taux de faux positifs de R ≥ 2α. |
| **H_A falsifiée si** | La borne basse de l'intervalle dépasse α. |
| **H_B falsifiée si** | La borne haute reste sous 2α. |
| **Attribution, si H_A tombe** | P_inter ≤ α : l'inflation vient de l'épisode. Le rapport variance inter-trajectoires / variance attendue sous indépendance, proposé par A, et la fonction d'autocorrélation séparent alors un effet d'épisode d'une dynamique. P_inter > α : la faute est de calibration ou de position. X > R : il y a dérive de distribution. |
| **Parade selon l'issue** | Effet d'épisode : centrer par une ligne de base propre à l'invite, comme C le suggère contre A. Dynamique : e-variables par blocs. |

### B1′ corrigé : d'où vient le plafond du rappel ?

Paramètres honnêtes estimés sur B1 : variance d'épisode σ_u² et fonction d'autocorrélation.

**Duel 1 (statistique)**, sur les trajectoires de sabotage de (iv) :

| | |
|---|---|
| **H_A, bruit partagé** | La courbe rappel(T) est prédite par un δ homogène, avec σ_u² et l'autocorrélation honnêtes. |
| **H_B, hétérogénéité** | La courbe est prédite par Var(δ_i) > 0, avec des résidus indépendants une fois l'effet d'épisode honnête retiré. |
| **Discriminant** | Les deux modèles sont ajustés sur des épisodes disjoints. On ajoute un critère externe : sous H_B, le δ̂_i d'une trajectoire est corrélé à sa dose réalisée (nombre de cibles semées atteintes) ; sous H_A, il ne l'est pas. |
| **Chaque issue falsifie** | Le modèle dont la bande de prédiction exclut le rappel observé à T_max. Si les deux tiennent ou si les deux tombent, c'est une issue déclarée indécise. |

**Duel 2 (construit : trait ou état)**. L'opportunité de sabotage est tirée a priori par tâche.

| | |
|---|---|
| **H_A, état** | δ ≈ 0 sur les tâches sans opportunité (équivalence à deux unilatéraux, marge illustrative), et δ > 0 sur les pas sabotés. |
| **H_B, trait** | δ sans opportunité ≈ δ avec opportunité. |
| **Chaque issue falsifie** | H_A tombe si l'intervalle de δ sans opportunité exclut la marge. H_B tombe si l'écart entre les deux δ exclut 0. |
| **Conséquence de H_B** | L'hypothèse (a) du lemme n'est pas satisfaite au sens « par action ». L'invariance à la fragmentation devient triviale, puisqu'elle porte alors sur la lecture d'une disposition. |

### B2 corrigé : la « signature » comme prédiction

On ajuste un modèle binormal (paramètres a et b, d_a si les variances diffèrent) sur les scores **continus** par action, dans chaque mode d'accès. Avec n_eff tiré de B1′, on prédit la courbe ROC de la cellule séquentielle.

| | |
|---|---|
| **H_A, accumulation** | La cellule « boîte blanche, séquentiel » observée tombe dans la bande prédite par l'accumulation des paramètres par action. |
| **H_B, sous-additivité** | Elle tombe sous la bande. |
| **Chaque issue falsifie** | La position de l'observé par rapport à la bande. Un observé **au-dessus** de la bande falsifie les deux hypothèses et invalide le modèle par action ; c'est une issue déclarée. |

L'interaction 2 × 2 de F1 n'est plus la preuve : elle est rapportée sans valeur de critère. Les données semi-synthétiques ne servent qu'à valider le code.

### B3 corrigé : longueur

| Mesure | H_A | H_B | Falsification |
|---|---|---|---|
| **Confondant** : honnêtes seuls, taux de faux positifs au seuil global, par strate de longueur | Taux plat | Taux croissant avec la longueur | Pente dont l'intervalle exclut 0 → H_A tombe ; équivalence dans la marge → H_B tombe |
| **Médiation** : longueur du saboteur contre longueur de l'honnête, à tâche appariée | Égales | Différentes | Selon l'intervalle de l'écart |
| **Validité incrémentale** en génération libre, sans stratification : régression logistique emboîtée « longueur » contre « longueur + sonde » | La sonde apporte du pouvoir | Elle n'apporte rien | Intervalle du ΔAUROC qui exclut 0 → H_B tombe ; qui contient 0 → H_A tombe |

On ajoute en option le bras « budget de jetons contraint » de C. Il n'est valide que si le taux de sabotage sur cibles semées est équivalent entre génération libre et génération contrainte.

### B4′ : fuite textuelle par contraste de familles

| | |
|---|---|
| **Précondition** | Doses de sabotage appariées entre (i) et iv-S, mesurées sur cibles semées. |
| **Contrôle positif** | Un détecteur d'écho lexical, lu sur les jetons d'action de (i). |
| **H_A** | Rappel(iv-S) ≥ rappel(i) − marge. |
| **H_B** | Rappel(iv-S) < rappel(i) − marge, **et** l'écho est lisible (AUROC du détecteur nettement au-dessus de 0,5). |
| **Chaque issue falsifie** | Selon l'intervalle de l'écart. Si l'écho n'est pas lisible, B4′ est déclaré non informatif. |

Le masquage reste une carte descriptive, munie de l'imputation neutre et du contrôle lexical de C. Je n'en tire aucune revendication de « non-textualité ».

### B5 corrigé : intention, thème ou auto-référence

| | |
|---|---|
| **Organismes** | iv-S : politique malveillante, décrite comme la sienne ; iv-K : la même, attribuée à un autre système ; iv-B : politique cachée bénigne, à la première personne ; iv-N : documents neutres. Option : iv-D, analyse défensive à vocabulaire apparié, reprise de C. |
| **Portes** | Taux de sabotage de iv-S supérieur à celui de iv-N, intervalles disjoints. Taux de sabotage et score de rubrique de iv-K et de iv-B équivalents à ceux de iv-N (équivalence à deux unilatéraux). |
| **H_A, intention** | iv-S est détectée sur ses pas sabotés ; les taux d'alerte de iv-K et de iv-B sont équivalents à celui de iv-N. |
| **H_B1, thème** | Taux d'alerte de iv-K > celui de iv-N. |
| **H_B2, auto-référence d'un but caché** | Taux d'alerte de iv-B > celui de iv-N. |
| **Chaque issue falsifie** | L'une ou l'autre des H_B tombe si son équivalence avec iv-N réussit. H_A tombe dès que l'une des deux excède iv-N. |

### B6 corrigé : biais de sélection

Deux familles scellées : l'une issue de la même recette, l'autre d'une recette différente. On les compare aux familles de développement.

| | |
|---|---|
| **H_A** | Aucun biais : écart sous la marge pour les deux familles scellées. |
| **H_B** | Biais : écart au-delà de la marge. |
| **Lecture** | Un écart sur la famille « même recette » signale un biais d'instance. Un écart sur la seule famille « autre recette » signale un biais de recette. |
| **Chaque issue falsifie** | H_A tombe si l'intervalle d'un écart exclut le bruit de découpage. H_B tombe si les deux écarts sont équivalents dans la marge. |

### B8 corrigé : lignée

Plan agent {Llama, Qwen} × juge {Llama, Qwen}. Les organismes Qwen sont de la famille (i) ; on y ajoute un LoRA (ii).

| Mesure | H_A | H_B | Falsification |
|---|---|---|---|
| **Discrimination** : AUROC du juge dans chaque lignée d'agent | Interaction > 0 (calibration-famille) | Interaction nulle | L'intervalle de l'interaction est au-dessus de 0, ou il contient 0 |
| **Niveau** : suspicion moyenne sur les honnêtes de la même lignée, contre l'autre | Plus basse (auto-préférence) | Égale | Selon l'intervalle de l'écart |

Aucune conclusion « capacité » ne se tire d'un nul agrégé.

### R1 : réentraînement (attaque CB3, adoptée)

Après E1.5 (b), on réentraîne la sonde sur les **seules** détections et on lit le rappel séparément sur deux types d'attaques d'un jeu tenu à l'écart : celles que la sonde initiale attrapait, et celles qui lui échappaient. Bornes : l'oracle en haut, la réserve de détecteurs comme témoin.

| | |
|---|---|
| **H_A** | Le rappel sur le type « échappé » gagne au moins 10 points (illustratif). |
| **H_B** | Il ne gagne rien (Δ ≤ 0), et la réserve fait mieux. |
| **Chaque issue falsifie** | Selon l'intervalle du gain. |

### B7 : inchangé

Ni A ni C ne l'attaquent. A le retient explicitement.

### Coûts revus (tous illustratifs)

| Poste | Coût |
|---|---|
| Trajectoires honnêtes longues : environ 800 × 3 valeurs de T, plus le jeu X (B1, B1′ honnête, B3 confondant) | 40 à 100 heures de carte A100, environ 60 à 150 USD |
| Organismes iv-S, iv-K, iv-B, iv-N (4 LoRA), sous devis | environ 40 à 130 USD |
| Famille scellée « autre recette » | nul si (iii) est sous licence, sinon un LoRA de plus |
| B8 : organismes Qwen (i) et (ii), plus deux juges | environ 40 à 100 USD |
| B2, B4′ et B3 incrémental | processeur, coût proche de 0 |
| R1 | coût de E1.5 (b), plus quelques heures |

---

## (c) Réponse à l'arbitre (une page)

**Ce qui est établi, au sens de « vérifié sur les pièces transmises ».** Ce sont des faits sur des textes, et non sur le monde.
- Dans la table (d) de F2, 30 entrées sur 46 n'ont été lues qu'en p. 1. A a confirmé le décompte.
- Les chiffres « 41 % contre 19 % » et « 9,8 % contre 2,8 % » ne reposent que sur une p. 1. Mon erreur sur 0,54 est corrigée.
- F3 écrit « H1 à H9 », alors que F1 contient H1 à H8 et HC1 à HC6.
- Le verbatim de F3 (« Les cinq propositions qui te reviennent : : accepté ») est ambigu sur sa portée.
- Des pièces citées ne sont pas transmises : N-003 à N-045, `anteriorite-v1.md`, `verification-pdf-v1.md`. L'empreinte de F2 citée dans F3 est tronquée.

**Ce qui a survécu à deux équipes rouges.** Ce sont des arguments logiques ; ce ne sont pas des résultats.
1. La proposition 1 acceptée en F3 fait de la « lecture filtrée » la *lecture principale* de toute revendication d'intention. Or masquer des positions à la lecture ne teste pas la fuite textuelle, puisque l'attention a déjà propagé l'information (A6, C2). Il faut un contraste de familles muni d'un détecteur d'écho (B4′).
2. Le test de récupération de F2 mesure un réentraînement par oracle, pas l'invariant de F1 §9. Il faut en plus lire séparément les attaques échappées (R1).
3. L'interaction lignée × moniteur de S7 n'est pas estimable avec un seul agent. Même avec deux lignées, un nul ne s'interprète pas sans décomposition (B8).
4. L'hypothèse (b) du lemme, un dommage qui ne dépend que de B, n'est testée par personne (B7).

**Ce qui n'est pas établi.**
- Que les 26 failles de F2 s'appliquent à Llama-3.1-8B dans l'environnement (a).
- Que le nul du processus e tienne sur des trajectoires réelles.
- Que les sondes lisent un état par action plutôt qu'une disposition.
- Le contenu que je prête à mes propres références : il vient de ma mémoire et reste HYPOTHÈSE.
- L'existence et le contenu des identifiants de 2026, que je ne peux ni confirmer ni infirmer.
- L'exhaustivité de mon recensement des failles manquées.

**Ce que la riposte a retiré.**
- Ma permutation intra-trajectoire.
- Mon « un bit lu T fois » comme argument de puissance ; il ne reste qu'une question de construit.
- Le statut de preuve de l'interaction 2 × 2.
- Le contrôle de B4 sur (ii) et (iv).
- La lecture « capacité » d'un nul en B8.

**L'expérience à faire en premier : B1 corrigé.** C'est un seul jeu de trajectoires honnêtes longues, environ 800 par T (illustratif), plus un jeu de tâches de contrôle. Trois raisons :
- **il conditionne les deux papiers** : une garantie de faux positifs fausse invalide A et B, quelle que soit la sonde ;
- **il ne demande aucun organisme**, donc ni LoRA ni dépense sous devis au-delà de la génération ; il peut commencer dès que le harnais de la phase 0 est validé ;
- **le même jeu alimente trois autres lectures** : les paramètres honnêtes de B1′ (σ_u² et autocorrélation), le test du confondant de longueur de B3, et le calibrage des taux d'alerte de B5.

Ses issues :
- **H_A falsifiée** (borne basse au-dessus de 1 %) : la conception statistique est à revoir avant G1, et l'attribution R / P_inter / X dit laquelle des deux parades appliquer ;
- **H_B falsifiée** (borne haute sous 2 %) : le nul est utilisable, et B1′ et B2 deviennent interprétables ;
- **zone indécise** : on augmente n avant toute lecture de G1.

FIN-DE-CELLULE