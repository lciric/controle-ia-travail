# Proposition A — tour III.1 : la non-convergence de la défense unique ré-entraînée lue comme dynamique de meilleure réponse

**Pièces** : les cinq pièces sont lisibles entières ou dans l'extrait annoncé. Non servies : le PDF de Bailey et collègues (donc rien de ce papier n'est vérifiable ici), le pilote `4d1fb23f…` (tous les chiffres du pilote v4 sont donc RAPPORTÉS par le brouillon 4 et recoupés par la vérification, pas vérifiés par moi), et la liste `resultats` du calibrage.

Convention de statut : **VÉRIFIÉ** = lu dans le code servi ou recalculé sur la pièce 5 ; **RAPPORTÉ** = chiffre du brouillon 4 ou de sa vérification, ou résultat de littérature que j'attribue sans l'avoir relu ici ; **OBSERVÉ-NON-AUDITÉ** = constat du pilote v4 (24 instances, audit d'essai sur 10 tâches seulement) ; **HYPOTHÈSE** = déduction ou conjecture.

---

## (a) Ce que la question suppose sans que ce soit établi

**A1. « A joue le jeu fictif » — la règle de A n'est pas le jeu fictif, pour trois raisons de code.** VÉRIFIÉ (`trajectoire`) : (i) la liste `attaques` commence par `ctx.cible`, donc le « mélange uniforme des attaques passées » donne un poids 1/(t+1) à la **loi cible non modifiée**, un coup que l'attaquant n'a jamais joué ; (ii) la meilleure réponse du défenseur est **approchée** (objectif lissé, seuil gaussien, L-BFGS-B, 8 départs) ; (iii) l'attaquant répond au **dernier** moniteur par un SLSQP **local**, avec un départ déterministe identique à chaque tour (`depart_tire_vers_l_origine`) et un départ chaud sur l'attaque précédente. Le jeu fictif de Brown (1951) et Robinson (1951) suppose des réponses exactes des deux côtés à l'**historique**. La convergence RAPPORTÉE par la question (« converge en somme nulle à deux joueurs quand les deux côtés la jouent ») porte sur les **fréquences empiriques**, pas sur le dernier itéré.

**A2. « Converger » = le dernier moniteur se stabilise et détecte mieux.** C'est l'hypothèse implicite de I1 et de (iii). Or le jeu fictif ne promet rien au dernier itéré : HYPOTHÈSE-déduction, si tous les équilibres du jeu restreint à la classe du défenseur sont mélangés, une suite de meilleures réponses **pures** ne peut pas se stabiliser (elle convergerait vers un équilibre pur qui n'existe pas) ; elle **doit** revisiter. RAPPORTÉ : les poids de B (classe linéaire) ne sont **jamais** purs (support moyen 3,7–3,8). Donc le « cycle » de A est la signature attendue d'un équilibre mélangé dans la classe linéaire, pas une anomalie de la règle « historique ». La question « pourquoi le jeu fictif cycle quand même » suppose qu'il ne devrait pas ; au dernier itéré, il doit.

**A3. « A ne progresse pas » = non-convergence.** OBSERVÉ-NON-AUDITÉ : (iii) de A va de 0,072 à 0,066 ; au tour 1, B déploie le même M0 et obtient 0,072. HYPOTHÈSE : tout moniteur linéaire **seul** vaut ≈ 0,07 contre sa meilleure réponse à δ = 1,4 (plafond de la classe pure), et I1 ≈ 0 mesure ce plafond, pas un défaut de dynamique. Aucun bras ne l'isole : il manque un témoin « M0 gelé huit tours » (A0) et un témoin « moniteur linéaire seul entraîné contre q » (A_q).

**A4. « I3 − 0,7345 > 0 » = retours au-delà du hasard.** VÉRIFIÉ (`valeur_nulle_I3`) : la valeur nulle suppose des déplacements **échangeables** (simulée sur des gaussiennes i.i.d. à 36 coordonnées). Un attaquant local qui n'a que quelques bassins (par exemple un bassin par composante sacrifiée, plus le départ fixe vers l'origine) produit des déplacements groupés en peu de modes ; une suite i.i.d. sur peu de modes donne I3 au-dessus de 0,7345 **sans aucune dynamique**. RAPPORTÉ à l'appui : D et B′ sont à −0,23 à −0,38 **sous** la valeur nulle, ce qui n'est explicable que par une continuité de départ chaud (l'attaque t ressemble à t−1) ; la nulle gaussienne est donc fausse dans les deux sens. La bonne nulle est une **permutation** de l'ordre des déplacements observés (teste « l'ordre compte »), pas une loi i.i.d.

**A5. « Le cycle est pathologique ».** Si A2 tient, la suite pure de A est le mécanisme même par lequel la **moyenne temporelle** de ses moniteurs pourrait converger (Robinson). Personne n'a mesuré cette moyenne : il manque le bras « C1 sur les moniteurs de A » (noté A̅). RAPPORTÉ : C1 − A ≈ +0,11, mais C1 mélange les moniteurs de B, entraînés contre q, pas ceux de A.

**A6. « Le jeu est à somme nulle ».** VÉRIFIÉ : `resoudre_jeu` traite une matrice de taux de détection dans [0, 1] comme un jeu à somme nulle, et la détection d'un mélange est la moyenne pondérée des détections (chaque moniteur garde son seuil à α) : l'extension mixte est linéaire, le taux de fausses alertes du mélange reste α. Ce qui n'est pas établi : que l'oracle « détection lissée à seuil gaussien » rende une meilleure réponse au gain **dur** ; l'écart n'est mesuré nulle part (il est déclaré « au détriment de D »).

**A7. « L'exploitabilité est calculable ».** Dans ce jeu, le côté attaquant est un continuum sans oracle exact : V n'est qu'une **borne haute** de la valeur (déclaré au brouillon). La seule exploitabilité calculable est celle du **jeu restreint** (moniteurs passés × attaques passées), et elle est déjà dans le code pour B et B′ : « valeur du jeu restreint − V » = +0,019/+0,024 (B), +0,004 (B′), RAPPORTÉ. Pour A, rien n'est calculé alors que ses 9 moniteurs et 8 attaques forment la même matrice.

**A8. « Q2 est non posable ».** RAPPORTÉ : la pureté de B′ est forcée par le jeu (17/17, 14/14). HYPOTHÈSE : la question « mélange contre unique à classe égale » **est** posable à la classe linéaire, où l'équilibre est mélangé : c'est B contre A (ou mieux, B contre A_q), déjà mesurée à +0,13 / +0,14, avec le confondant « distribution d'entraînement » (q contre uniforme). La « non-posabilité » est propre à la classe où un moniteur unique suffit à l'attaquant local : c'est un résultat (plafond atteint par un seul maxout), pas une panne de conception.

**A9. Transfert.** La question demande les résultats publiés sur sondes réelles ; les pièces n'en contiennent aucun. Le brouillon le dit (« aucun chiffre repris »). Je ne peux rien y ajouter de vérifiable : voir § (c) et § références.

---

## (b) Expériences décisives (chaque duel : H_A contre H_B, métrique, seuil, contrôle, ce que chaque issue réfute)

Tous les seuils ci-dessous reprennent m = 0,02 (S6, « par principe », RAPPORTÉ) et sont **illustratifs** ; tout nouveau bras exige un gel nouveau, des racines neuves de la plage 20264001–20264999 non encore gelées, et un pilote avant toute décision (règles du gel v4, VÉRIFIÉ).

### Duel 1 — Plafond de la classe pure ou défaut de la règle de A (répond à 1, 3a, 3c, 3d, 3f d'un coup)

- **H_A** : aucun moniteur linéaire seul ne dépasse A à sa meilleure réponse : la règle de mise à jour est indifférente au dernier itéré.
- **H_B** : il existe un moniteur linéaire seul qui bat A d'au moins m : la règle « historique uniforme » est en cause.
- **Bras à ajouter (tous linéaires, déployés seuls, finale standard puis renforcée comme les autres)** : A0 (M0 gelé, huit tours), A_q (moniteur linéaire entraîné contre q, l'équilibre de l'attaquant de B, au tour 8), A_moy (un seul moniteur dont les poids sont la moyenne des 9 moniteurs de A, seuil recalibré à α — c'est le mécanisme 3c « moyenne de poids »), A_pire (moniteur entraîné sur la pire attaque passée — mécanisme 3f), et « chaque moniteur de B seul » (max sur 9).
- **Métrique** : V (iii) apparié par instance ; contraste max_X V(X) − V(A).
- **Issues** : si le maximum est < m aux deux δ, H_B est réfutée et, avec elle, l'espoir que 3c, 3d, 3f changent le dernier itéré à classe linéaire (ils rendent tous un moniteur pur) ; si un X dépasse m, H_A est réfutée et la règle de A est fautive — l'identité de X dit laquelle (A_q : la distribution d'entraînement ; A_pire : l'uniforme ; A_moy : la moyenne).
- **Contrôle négatif** : D − A = +0,36 / +0,32 (RAPPORTÉ) montre que l'instrument V distingue bien deux classes quand elles diffèrent. Contrôle mécanique : A_moy construit sur 9 copies de M0 doit rendre V(M0) au bit près.
- **Ce que ça casse** : rien ; coût ≈ 5 trajectoires linéaires de plus par tâche (voir § d).

### Duel 2 — Le « cycle » est-il dynamique ou géométrique (répond à 1, 2 et au choix de métrique)

- **H_A** : les retours de A tiennent à l'ordre des tours (dynamique : l'attaque revient parce que le moniteur a tourné).
- **H_B** : les retours tiennent à la structure de l'ensemble des réponses (peu de bassins, départ fixe), indépendamment de l'ordre.
- **Métrique** : I3 observé contre la loi de I3 sous **permutation** de l'ordre des 8 déplacements de la tâche (8! = 40 320 ordres, exhaustif ; aucune nouvelle graine). Seuil : part des tâches où I3 observé dépasse le quantile 0,975 de la permutation ; H_A prédit > 0,5, H_B prédit ≈ 0,025.
- **Second test, sans recalcul** : le même I3 appliqué à la suite des **moniteurs** de A (cosinus entre vecteurs de poids). Sous jeu fictif, les moniteurs bougent par pas ~1/(t+1) et ne « reviennent » pas ; sous cycle de meilleure réponse pure, ils reviennent. H_A-jeu-fictif prédit I3(moniteurs) sous la permutation et des longueurs de séries d'attaques qui s'allongent ; H_A-cycle prédit des retours des moniteurs aussi.
- **Contrôle négatif** : relancer A avec le départ déterministe vers l'origine retiré de l'attaquant (une ligne) sur la racine réservée : si I3 − permutation s'effondre, la part « départ fixe » de A4 est mesurée. Contrôle positif : D, dont I3 − nul est négatif (RAPPORTÉ), doit rester sous la permutation.
- **Issues** : H_A réfutée si I3 est dans la bande de permutation ; H_B réfutée s'il en sort dans la majorité des tâches. Dans les deux cas, la ligne « cycle » de la Table 5 (lue sur 0,7345) doit être réécrite au brouillon 5 : la nulle gaussienne est fausse même si H_A tient.

### Duel 3 — La moyenne temporelle de A converge-t-elle (répond à 3a, 3b, et à « quelle métrique »)

- **H_A** (Brown–Robinson transposé) : le mélange uniforme des moniteurs de A (A̅) a une exploitabilité restreinte décroissante en T et V(A̅) ≥ V(A) + m.
- **H_B** : A̅ ≈ A (les moniteurs de A sont trop semblables pour que les mélanger aide) ; la myopie de l'attaquant ou l'approximation des oracles brise la convergence des moyennes.
- **Métriques** : (i) V(A̅) − V(A), bornes B2 ; (ii) NashConv restreint de A̅ : valeur de la matrice 9 × 9 de A (moniteurs × {cible, attaques}) moins min sur les colonnes de la détection de A̅, avec `resoudre_jeu` ; (iii) la même chose à T = 16 sur A seul (bras léger). Seuil : NashConv(T=16) < NashConv(T=8) − m sous H_A.
- **Bras A2** (attaquant qui joue aussi le jeu fictif : meilleure réponse au mélange uniforme des moniteurs passés ; le code sait déjà répondre à un mélange, `objectif_lisse`) : H_A-Robinson prédit NashConv(A2) ≤ NashConv(A) ; si l'ordre est inverse ou égal, la myopie de l'attaquant n'est pas ce qui empêche la convergence des moyennes.
- **Contrôle négatif** : A̅ calculé sur 9 copies de M0 = M0 ; contrôle positif : C1 sur B (RAPPORTÉ +0,11 contre A).
- **Issues** : H_A réfutée si V(A̅) − V(A) < m ou NashConv ne décroît pas ; H_B réfutée sinon. Si H_A tient, la « non-convergence de la défense unique » se reformule : *la défense pure ne converge pas, sa moyenne oui* ; le mécanisme (b) double oracle n'ajoute alors que le choix des poids (B − C1 = +0,02 RAPPORTÉ) et de la distribution d'entraînement.

### Duel 4 — Le témoin jouet (répond à 4 ; protocole en cinq lignes)

1. Jeux : pierre–feuille–ciseaux et pile ou face apparié (somme nulle, équilibre intérieur connu) ; jeu de Shapley (1964, 3 × 3, non somme nulle : jeu fictif connu pour ne pas converger en moyennes — RAPPORTÉ).
2. Dynamiques, bibliothèque prise telle quelle : meilleure réponse pure itérée ; jeu fictif des deux côtés ; jeu fictif d'un seul côté contre réponse au dernier coup (la règle de A, à écrire en dix lignes au-dessus des matrices).
3. Mesures : exploitabilité (NashConv) des moyennes empiriques ; I3 sur les coups codés en un-chaud (cosinus 0/1) ; longueurs de séries.
4. Vérité : équilibres par Gambit.
5. Attendus (HYPOTHÈSE à falsifier) : NashConv(moyennes) → 0 en somme nulle pour le jeu fictif, pas pour la meilleure réponse pure dans Shapley ; I3 → 1 pour la meilleure réponse pure cyclique, I3 → 0 pour le jeu fictif (séries qui s'allongent) ; pour la règle de A, **inconnu** — c'est la mesure utile : si ses moyennes convergent en pile ou face apparié et pierre–feuille–ciseaux, le Duel 3 a un prior ; sinon, A n'est pas un jeu fictif et la littérature citée ne s'applique pas.

**H_A** : la règle de A converge en moyennes dans les deux jeux jouets ; **H_B** : non. Issue : si H_B, la question 3a est tranchée sur un jeu exact, sans aucun oracle approché.

### Duel 5 — Rendre Q2 posable (répond à 5)

- **Condition testable** : Q2 est posable à un δ si, sur plus de la moitié des tâches, le plus petit poids maximal parmi les équilibres du jeu restreint final (`poids_max_min_equilibres`, VÉRIFIÉ) est ≤ 0,5 — la pureté n'y est pas forcée.
- **H_A** : la pureté est un plafond de capacité : avec des moniteurs à moins d'unités que de modes d'attaque (unités_Bp = 2, K = 3, ou K = 5 à 3 unités), le mélange est exercé (part pure < 0,5, pureté forcée < 0,2) et B′ − D y redevient lisible.
- **H_B** : la pureté persiste même sous-capacité : l'attaquant local n'utilise qu'un mode à la fois, et un seul moniteur pauvre suffit à l'équilibre restreint.
- **Métrique** : part pure et part de pureté forcée (déjà calculées) ; puis Table 6 telle quelle. Contrôle : la classe linéaire (B), où le mélange est exercé (support 3,7), joue le témoin positif ; D doit être réentraîné à la même classe réduite (sinon la comparaison n'est plus « à classe égale »).
- **Issues** : H_A réfutée si la pureté reste > 0,5 ; H_B réfutée sinon. Dans les deux cas Lazar sait s'il existe une classe intermédiaire où le tirage au hasard est mesurable, sans réécrire le jeu.

### Mécanismes 3(a)–(g) : condition, prix, test le moins cher

| Mécanisme | Condition de convergence (statut) | Prix | Test le moins cher dans notre jeu |
|---|---|---|---|
| (a) jeu fictif des deux côtés | moyennes seulement, somme nulle, réponses exactes (RAPPORTÉ : Robinson 1951) ; dernier itéré : jamais garanti | la défense déployée doit être la **moyenne** (un mélange), sinon rien ne converge | Duel 3, bras A2 et A̅ |
| (b) double oracle / PSRO | identique, plus poids d'équilibre ; convergence du jeu restreint vers le jeu complet si l'oracle est exact (RAPPORTÉ : McMahan, Gordon, Blum 2003) | mémoire T+1 moniteurs ; détection de la dernière attaque diluée | « valeur restreinte − V » à T = 16 contre T = 8 (B seul) : si l'écart ne baisse pas, l'oracle approché borne la convergence |
| (c) régularisation vers le passé | rend un moniteur **pur** | retient le passé, perd la dernière attaque | Duel 1 (A_moy) : prédit au plafond |
| (d) gradients optimistes, extragradient | dernier itéré, jeux bilinéaires ou convexes-concaves (RAPPORTÉ : Daskalakis et collègues 2018) ; ici gain non concave, attaquant oracle | réécriture de l'attaquant en joueur de gradient | sans objet à classe linéaire si Duel 1 tient (équilibre mélangé → aucun dernier itéré pur ne converge) ; à classe riche, D converge déjà sans optimisme (plateau 0,40 dès le tour 4, B′ − D ≈ 0, RAPPORTÉ) |
| (e) élargir la classe | un équilibre pur existe dans la classe → le dernier itéré peut converger | coût d'entraînement, déploiement 63 paramètres | déjà fait (D) ; réfutation possible : D à 2 unités cycle-t-il ? (Duel 5) |
| (f) pire cas sur l'historique, regret | pire cas : moniteur pur (plafond) ; regret (Hedge sur moniteurs passés) : mélange, convergence des moyennes sans programme linéaire | comme (a) | Duel 1 (A_pire) ; bras « Hedge » à comparer à A̅ et B |
| (g) attaquant avec mémoire | change la convergence des **moyennes** de l'attaquant, pas le cycle du dernier moniteur | — | Duel 3 (A2) |

**Pourquoi ça cycle (réponse à 2), tel que les pièces le permettent** : HYPOTHÈSE-déduction de A2 : à classe linéaire l'équilibre restreint est mélangé (RAPPORTÉ : B jamais pur), donc toute règle qui déploie un moniteur pur revisite. Le cycle est inévitable pour un déploiement pur quand tous les équilibres de la classe sont mélangés ; il n'est pas inévitable quand un équilibre pur existe (classe à 9 unités : B′ pur et D plat). Le bruit (oracles approchés, départs) ajoute des errances aux deux cas ; la somme nulle n'empêche pas le cycle du dernier itéré, elle garantit seulement les moyennes. Shapley (1964) et les cycles d'entraînement adversarial sont des analogies plus lointaines que ce mécanisme de base.

---

## (c) Les instruments nommés : la mesure minimale qui dirait s'ils fonctionnent

| Instrument | Fonctionne si… | Cas honnêtes appariés (illustratifs, générés par le jouet du Duel 4 et par les bras existants) | Vérification mécanique à battre |
|---|---|---|---|
| **I3 contre 0,7345** | détecte ≥ 0,9 des suites à cycle de meilleure réponse pure (période 2–3, un-chaud) **et** ≤ 0,05 de fausses alertes sur (i) suites i.i.d. et (ii) suites i.i.d. **sur 3 modes** (le cas difficile : la nulle gaussienne y échouera, prédiction HYPOTHÈSE) | 200 suites de longueur 8 par type : cycle pur ; jeu fictif ; i.i.d. gaussien ; i.i.d. 3 modes ; attaques de D (continuité) | la nulle par permutation (Duel 2) et l'autocorrélation de décalage 2 des cosinus : si I3 ne fait pas mieux que ces deux-là, le retirer |
| **I1 (progrès)** | distingue D (progrès RAPPORTÉ) de A, **et** ne lit pas « non-convergence » là où un plafond pur existe | A0 (M0 gelé) contre A : si I1(A0) ≈ I1(A) ≈ 0 et V(A0) ≈ V(A), I1 ne mesure que le plafond | V(A) − V(A0) < m rend I1 sans objet pour la Table 5 |
| **Exploitabilité restreinte (NashConv)** | sur le jouet, vaut 0 aux équilibres de Gambit et > 0 ailleurs ; dans l'arène, décroît en T pour A̅ et B | B à T = 8 et 16 ; A̅ à T = 8 et 16 | garde primal = dual de `resoudre_jeu` (VÉRIFIÉ) ; V comme borne haute (déclaré) : NashConv restreint sous-estime l'exploitabilité vraie, à dire |
| **Distance aux moniteurs passés** | sous jeu fictif, pas ~1/(t+1) et sans retour ; sous cycle, retours | moniteurs de A contre ceux de D | compare au pas prédit par la règle ; si le pas observé ne décroît pas en 1/(t+1), les oracles approchés dominent |
| **OpenSpiel (jeu fictif, PSRO, exploitabilité)** | reproduit Robinson sur pierre–feuille–ciseaux (exploitabilité des moyennes → 0) et la non-convergence sur Shapley, sans modification | les trois jeux du Duel 4 | Gambit comme vérité ; la présence du jeu de Shapley et de l'exploitabilité pour jeux matriciels définis à la main est **à vérifier dans la documentation** |
| **Gambit** | ses équilibres du jeu restreint 9 × 9 de B coïncident avec `resoudre_jeu` à 10⁻⁷ | 48 matrices du pilote | si non, l'un des deux solveurs rend un autre sommet : lien direct avec la question de pureté forcée |
| **Sondes linéaires sur un modèle à poids ouverts** | la seule métrique lisible côté défense est **V de la défense figée à fausses alertes α sur des attaques tenues à l'écart** (mélange ou unique) ; I3 exige un vecteur de déplacement (décalage moyen des activations d'un jeu d'attaques), lisible mais à nulle par permutation seulement ; I1 n'a de sens qu'avec un témoin gelé | sonde gelée (A0 réel) contre sonde ré-entraînée (A réel) contre mélange uniforme des sondes passées (A̅ réel), mêmes jeux honnêtes, mêmes α | fausses alertes de chaque sonde et du mélange à α ± 0,005 (la garde `exiger_fpr`, VÉRIFIÉE, est transposable) ; sans attaquant exact, V reste une borne haute |

Rien dans les pièces ne dit comment Bailey et collègues mesurent la convergence : le PDF doit être lu avant de prétendre qu'une de ces métriques est la leur.

---

## (d) Ancrage matériel

- **Arène (processeur seul, code servi)**. VÉRIFIÉ (pièce 5) : 432 tâches « A seul, mode léger » ont coûté 768 s de processeur, soit 1,8 s par tâche. Les bras des Duels 1 et 3 (A0, A_q, A_moy, A_pire, A̅, Hedge, A2) sont tous linéaires : **illustratif**, 2 à 5 s par tâche chacun, soit ≈ 1 à 2 h de processeur pour 100 instances × 2 δ × 7 bras, moins que le pilote v4 (RAPPORTÉ : 60,7 s par tâche pour 8 bras). T = 16 sur A seul : ≈ 4 s par tâche, illustratif. Le Duel 5 (B′ et D à classe réduite) coûte l'ordre du pilote v4 (RAPPORTÉ : 24 instances × 2 δ ≈ 49 min de processeur). La permutation du Duel 2 est gratuite (pilote existant, 8! ordres par tâche).
- **Contrainte de protocole** : racines neuves à geler avant emploi, plage 20264001–20264999 (VÉRIFIÉ) ; délai externe de 9 000 s à efficacité mesurée 0,51–0,52 ne tient déjà pas pour N = 100 (RAPPORTÉ, CM4-01) : tout bras ajouté aggrave ce point, sauf à exécuter les bras linéaires dans un run séparé.
- **Jouet** : OpenSpiel et Gambit, processeur, quelques minutes, illustratif. Modèles ouverts : aucun n'est requis avant que les Duels 1 à 4 soient tranchés.
- **Transfert aux sondes réelles** : les pièces ne donnent ni modèle ni coût. Illustratif : un modèle à poids ouverts de taille moyenne, sondes linéaires sur une couche, huit tours de ré-entraînement de sonde = quelques dizaines de minutes de GPU par tour hors génération d'attaques, que la question interdit de concevoir ici. Le seul livrable défensif transposable sans attaque : la mesure V(A̅) − V(A) sur sondes, qui dit si la **moyenne** des sondes passées bat la dernière sonde, avec le témoin gelé A0.

---

## Références (toutes RAPPORTÉES, non relues ici ; à vérifier sur PDF)

- Brown, G. W. (1951). *Iterative solution of games by fictitious play*. Dans *Activity Analysis of Production and Allocation*.
- Robinson, J. (1951). *An iterative method of solving a game*. Annals of Mathematics.
- Shapley, L. S. (1964). *Some topics in two-person games*. Dans *Advances in Game Theory*.
- McMahan, H. B., Gordon, G. J., Blum, A. (2003). *Planning in the presence of cost functions controlled by an adversary*. ICML.
- Lanctot, M. et collègues (2017). *A unified game-theoretic approach to multiagent reinforcement learning*. NeurIPS.
- Daskalakis, C., Ilyas, A., Syrgkanis, V., Zeng, H. (2018). *Training GANs with optimism*. ICLR.
- Fudenberg, D., Levine, D. K. (1998). *The Theory of Learning in Games*. MIT Press (variantes du jeu fictif).
- Lanctot, M. et collègues (2019). *OpenSpiel: a framework for reinforcement learning in games* — référence à vérifier pour la liste des auteurs.
- Gambit : McKelvey, McLennan, Turocy, *Gambit: Software Tools for Game Theory* — année à vérifier.
- Bailey et collègues, arXiv 2412.09565 (identifiant pris des pièces) : titre que je crois être *Obfuscated Activations Bypass LLM Latent-Space Defenses* — **à confirmer sur le PDF servi** ; aucun chiffre ni résultat de ce papier n'est repris ici.
- Résultat sur « jeu fictif d'un côté contre réponse au dernier coup » : **référence à vérifier** ; je n'en connais aucune attribuable, d'où le Duel 4.
- Entraînement adversarial de sondes, coévolution attaquant–moniteur sur modèles de langage (item 6) : **références à vérifier** ; rien dans les pièces ne permet de les attribuer.

**Compte de ce qui peut être réfuté** : cinq duels, chacun avec les deux issues écrites ; deux présupposés (A2, A4) réfutables sans aucun calcul neuf.

FIN-DE-CELLULE