# Contre-lecture (R2) du préenregistrement de la simulation d'essaim — v1, brouillon 1

**Verdict : scellable après corrections mineures (listées ci-dessous, C1 à C10).** Aucune erreur mathématique dans les énoncés démontrés (HE1, HE2.1 à HE2.3, HE4, HE5, HE3.1, HE3.2, HE3.5) ; les nombres recalculés tombent juste. Les corrections portent sur l'ordre de scellement et de commit (une erreur d'ordre arrêterait le run), sur des issues non écrites d'avance, sur l'étiquetage des prédictions vues en exploration, sur deux phrases trop fortes (Schur-concavité, ampleur 0,1) et sur le caractère exploratoire de deux lectures de la table E.

- Contre-lecteur : sous-agent neuf, qui n'a écrit ni le préenregistrement, ni le code, ni la grille, ni l'annexe, ni le rapport joint.
- Brouillon relu : `preenregistrement-essaim-simulation-v1-brouillon1.md`, sha256 `b9b1109ec4380894538114f5e977154ffd96afac4e83a0bf8a3ce6ad7c5dfdfc` (vérifié sur disque).
- Grille lue : `grille-essaim-v1-brouillon1.json`, `dacbce3006cc354f7cababaf53c16e415598838cfa0c91dccf15ec1bed6eff06` (vérifié). Annexe : `ca4500a2…1ae9` (vérifié). `explorations-brouillon1/empreintes.txt` : `63c00c62…e664` (vérifié) et ses 17 lignes contrôlées par `sha256sum -c` : toutes OK.
- Aussi lus : les sept modules de `src/controle_ia/simulation_essaim/`, `tests/test_simulation_essaim_v1.py` (35 tests rejoués : **35 passés en 15,6 s**), la note mathématique v3 (`dfe4fe0f…`), `prereg/T0.3-simulation-lemme-theoreme-v1.md` (`7474743a…`), le gabarit (`8cad4371…`), l'exemple scellé `P3-premier-test-i-a-v1.md`, `manifeste.py`, `prereg.py`, `simulation_t03/run_t03.py` et `lois.py`, le rapport joint, les dix scripts d'exploration et leurs sorties.
- Je n'ai pas lancé le run décisif, n'ai modifié aucun fichier existant, n'ai fait aucun commit ni accès réseau. Seul fichier créé : ce rapport (et, hors dépôt, un dépôt git jetable dans le répertoire temporaire de la session pour reproduire la garde du commit cité).

## 0. Ce que j'ai recalculé moi-même (sans le code du paquet, sauf mention)

Tout par `scipy` direct, α = 0,05, q = 0,1, u = Φ⁻¹(0,9).

1. **Seuils exacts des comptages** (max de T comptes Bin(K, q) pour `coelev_comptage`) : e5x40 (3 ; 0,11646), e10x20 (4 ; 0,09137), e20x20 (6 ; 0,02145). Identiques à l'annexe, table A (0,1165 ; 0,0914 ; 0,0215).
2. **Bornes inférieures de HE2.3** (convolution Bin(m, 1 − 0,9^T) ∗ Bin(K − m, 0,1), seuil aléatoirisé) : e5x40 m = 2/3/5 → 0,05477 / 0,27324 / 0,99812 ; e10x20 m = 2/5/10 → 0,04161 / 0,70214 / 0,99960 ; e20x20 m = 2/10/20 → 0,02440 / 0,98985 / 1,00000. Identiques au texte (0,0548 / 0,2732 / 0,9981 ; 0,0416 / 0,7021 / 0,9996 ; 0,0244 / 0,9899 / 1,0000).
3. **Bornes de `pas_moyenne` à m = K** ((1 − Φ(c_T/√K)^T)^K) : 0,88412 / 0,85522 / 0,95925. Identiques (0,8841 / 0,8552 / 0,9592).
4. **Taux conforme** : j = ⌈1001 × 0,95⌉ = 951 (1001 × 0,95 = 950,95), taux 1 − 951/1001 = 0,0499500. **Région exacte** : somme de 50 lois bêta-binomiales (400 ; 50 ; 951) par convolution directe, niveau 1 − 10⁻⁵ : **[843 ; 1165]** (0,04215 à 0,05825), masse totale 1,0000000000. Identique.
5. **Formes closes de la classe M** : max, B = 3, n₀ = 200 : 1 − Φ(c)^199 Φ(c − 3) = 0,3517 ; `pas_moyenne`, e10x20, B = 12, m = 10 : 1 − Φ(c_T − 12/√10) Φ(c_T)^19 = 0,8479. Identiques à l'annexe, table B.
6. **Formes closes hors hypothèses (table D)**, par un Monte-Carlo indépendant de 200 000 essaims (seuil `coelev_comptage` e10x20 = (4 ; 0,09137)) : c = 0,4 → 0,6208 (annexe 0,6222) ; c = 0,2 → 0,3532 (0,3530) ; τ = 0,2 → 0,0830 (0,0824). Écart-type de Monte-Carlo ≈ 0,001 : concordant. `pas_moyenne`, c = 0,4, e10x20 : 1 − Φ(c_T/√4,6)^20 = 0,8675 (annexe 0,8669, la différence venant de mon arrondi de Φ).
7. **Largeurs et puissance des intervalles** (`intervalle_cp`, seule fonction du paquet utilisée) : demi-largeur 0,00683 à p = 0,05, R = 20 000 ; 0,01564 à p = 0,5 ; 0,00305 à p = 0,05, R₀ = 100 000. Pour « au-dessus » du taux 0,05 il faut bas(IC) > 0,05311 : p̂ ≥ 0,0603. Puissance de cette lecture : 43 % pour un taux vrai de 0,060, 99,7 % à 0,065, > 99,99 % à 0,070. Plus petit écart distingué : environ 0,010.
8. **Comptage des cellules** : 824 (775 statistiques, 49 trajectorielles) retrouvé à la main, somme des 23 prédictions, et par `compter_cellules.py` rejoué (sortie identique à `sortie-compter_cellules.txt`). Table E du préenregistrement comparée mot pour mot à `lecture.LIGNES_E` par script : **les 8 lignes sont identiques** (énoncé, lecture, exigées, complémentaires).
9. **Valeurs exploratoires citées** (section Transparence et prédictions) : relues une à une contre les `sortie-exploratoire_*.txt`. Toutes exactes (par exemple HE1.3 : 0,159 à 0,363 et 0,995 à 1,000 ; relais 0,008 à 0,017 ; HE2.5 : 0,019 à 0,025 ; HE3.4 : règle ≥ 0,08 aux deux tailles ; HE6.3 : 0,979 / 0,988, 0,741 / 0,461, 0,013 / 0,010).

## A. Complétude R1

**Conforme**, avec une lacune dans les issues écrites d'avance (C2).

- Hypothèses, objet, cadre, groupes et invariances : présents. Sections exigées par `prereg.SECTIONS` toutes présentes ; `problemes()` ne signale, sur le brouillon, que les deux marqueurs attendus et l'absence des empreintes de contre-lecture.
- Prédictions chiffrées et signées : les 23 prédictions donnent signe ou forme close, origine étiquetée, nombre de cellules (somme exacte de 824), et ce qui réfute (tableau A des critères, ligne 211 à 222).
- Métrique, seuil (α, q, γ, règles de sélection), plan (tailles justifiées, graine, nombres aléatoires communs, run unique, gel du code, ordre, multiplicité, audit R4, durée), critères de lecture (tableau A, verdicts B, réplication C, audit D, table E, issues F), liste d'arrêt en 10 points, protocole après arrêt : présents et cohérents avec le code.
- Documents qui font foi : les sept empreintes citées sont exactes (recalculées).
- **Lacune** : le tableau F (issues écrites d'avance) ne couvre pas HE3.1, HE3.6, HE4.1, HE4.2, HE4.3, ni HE2.4 réfutée, ni HE1.3, HE2.5 ou HE6.3 « non concluante » dans les cas où le critère le permet (« en dessous » et « au-dessus » ont un état non concluant). La table E applique mécaniquement « non établi », mais R1 demande les issues écrites d'avance. Voir C2.

## B. Justesse mathématique

**Conforme**, avec deux phrases à resserrer (C5, C6).

- **HE1 découle de T1 (note v3, section 4)** : T1 ne demande aucune hypothèse sur P₀ ; il exige une statistique G-invariante, π_Y ∈ G presque sûrement, et un aléa du test indépendant de l'attaque. Ici G = G_A = (S_K)^T (la note cite « permutations des agents à l'intérieur de chaque pas » parmi les groupes utiles). Les neuf statistiques (somme, max, comptage, `pas_moyenne`, `coelev_comptage`, `coelev_somme3`, `e_coelev`, `ed_coelev`, `e_pas`) ne dépendent, à chaque pas, que du multi-ensemble des K scores (et, pour les trois séquentielles, de l'ordre des pas) : G_A-invariantes. Le routage utilise un aléa privé (agent voyou, pas tirés) indépendant de Y, ce que la classe C de la note autorise (« mesurable en Y et en l'aléa privé »). L'uniforme de départage U est celui de l'essaim honnête : indépendant de l'attaque. Le code construit donc bien des cas où l'identité est exacte, et la garde `exiger_groupe` l'impose.
- **Nuance de portée** : « sous G_A, seule la surveillance par agent peut détecter » (ligne 49) est vrai pour le panneau, pas pour toute statistique possible. À écrire « dans le panneau » (C10).
- **HE2** : G_T = (S_T)^K ; `agent_moyenne` (somme triée du temps de chaque agent) et `agent_comptage` (comptage par agent) ne dépendent que du multi-ensemble des T scores de chaque agent : G_T-invariantes ; la synchronisation est une permutation du temps propre à chaque agent synchronisé (la garde `exiger_groupe("temps")` le vérifie sur chaque essaim) : T1 s'applique, aveuglement exact. Les affirmations de groupes sont correctes : G_A et G_T engendrent Sym(I) (transpositions le long des lignes et des colonnes, graphe des tours connexe dès que K, T ≥ 2) ; l'intersection de G_T et de S_K ≀ S_T est la seule relabellisation commune des pas (un élément du produit en couronne qui fixe chaque agent est de la forme σ = id) ; la co-élévation n'est pas G_T-invariante (la synchronisation change son compte au pas commun, HE2.1 le vérifie). L'argument d'invariance est exact.
- **Bornes de HE2.3** : le raisonnement est correct. Au pas commun s, chacun des m agents synchronisés porte son maximum (indépendants, ≥ u avec la probabilité 1 − 0,9^T), les K − m autres gardent leur score honnête (≥ u avec la probabilité q) ; `coelev_comptage` ≥ C_s ; la fonction d'alarme est croissante en V pour U fixé et U est indépendant, donc P(alarme) ≥ P(C_s > c) + γ P(C_s = c). Recalculé : 0,27 à 1,00 (point 2 ci-dessus). Pour `pas_moyenne` à m = K : si chaque maximum dépasse c_T/√K, la somme du pas dépasse c_T √K (c_T > 0) ; pour `coelev_somme3` : trois maxima ≥ c₃/3 donnent une somme des trois plus hauts ≥ c₃ ; le seuil MC c₃ du run est une constante conditionnelle indépendante des essaims testés. Correct.
- **Bornes de m = 2** (0,0416 et 0,0244 sont sous α) : valides mais vides comme borne (« haut(IC) ≥ b » est alors presque toujours vrai) ; le texte les range à juste titre en descriptif pour HE2.4.
- **HE3.2** : sous équicorrélation, les pas restent indépendants (`lois.tirer`, `equicorrelation` : U tiré par pas) et la marginale reste N(0, 1), donc E[C_t] = Kq ; chaque facteur 1 + λ(C_t − Kq) est positif (λ ≤ 0,75/(Kq), donc ≥ 0,25) d'espérance 1 : martingale positive, Ville applicable au mélange de λ. Correct. Sous effet d'épisode, les pas ne sont plus indépendants : la martingale tombe, d'où HE3.3. Correct.
- **HE3.5** : échangeabilité des essaims entiers, ordre lexicographique (V, U) strict presque sûrement : le taux exact est 1 − 951/1001, et le compte total sur 50 × 400 essais est une somme de bêta-binomiales. Recalculé.
- **Deux phrases à resserrer** : (i) la Schur-concavité (lignes 61 et 237 ; C5) ; (ii) la tête de HE2 (lignes 50 et 59) dit « au-dessus de son taux » sans restreindre à m ≥ ⌈K/2⌉, alors que les bornes à m = 2 sont sous α (C6).

## C. Statistique

**Conforme sur les intervalles et la taille, à corriger sur deux phrases (C4, C8).**

- Intervalles exacts de Clopper-Pearson à 1 − 10⁻⁵ : bien implantés, demi-largeurs citées exactes (point 7).
- **Taille suffisante** : à R = 20 000 contre R₀ = 100 000, un écart n'est distingué (« au-dessus » ou « en dessous » autour de 0,05) qu'à partir d'environ 0,010 ; 99,7 % de puissance à 0,065. Les prédictions « au-dessus » ont des effets de 0,1 et plus (HE1.3, HE6.3), une borne exacte ≥ α + 0,02 (HE2.4 : la règle n'est en pratique jamais contraignante, les bornes à m ≥ ⌈K/2⌉ valant au moins 0,27), ou de 0,02 à 0,05 au-dessus de la référence de Ville (HE3.3, HE3.4) ; tous sont très largement résolus. Les cellules « égal » ne certifient l'égalité qu'à ± 0,010 près, ce qui est cohérent avec la formulation « à l'intervalle exact près » et ne pose pas de problème ici puisque l'égalité exacte est garantie trajectoriellement par T1 (HE1.1, HE2.1).
- **Erreur de chiffre** : la ligne 172 et la ligne 187 disent « effets d'ampleur ≥ 0,1 en taux » pour HE1.3 et HE6.3 et « les effets informatifs prédits sont d'au moins 0,1 ». Faux pour les cellules « en dessous » : relais 0,05 → 0,012 (effet 0,04), HE2.5 0,05 → 0,02 (0,03), HE6.3 m = 5 sous c = 0,4 (0,04). La conclusion (résolu) tient, le chiffre est faux : C4.
- **Multiplicité** : « au plus de l'ordre de γ » et union 775 × 10⁻⁵ = 0,8 %. Pour les 263 cellules « égal » (deux intervalles indépendants), la contrariété exige que l'un des deux manque sa cible : au plus 2γ. Borne correcte : (512 × 1 + 263 × 2) × 10⁻⁵ ≈ 1,0 %. Inoffensif (la réplication traite le risque) mais à corriger (C8).
- Audit R4 : deux ensembles de z (358 et 263). Deux observations non bloquantes : (a) les z d'une même cellule sont corrélés entre statistiques, et ceux d'une même alarme et configuration partagent le même p̂₀ (variance 1/6 commune) ; la variance de la variance en est accrue, mais les bornes [0,3 ; 3] sont assez larges pour que le déclenchement par bruit soit improbable ; (b) rien à changer.

## D. Lectures préalables

**Étiquetage : conforme pour les quatre prédictions annoncées ; insuffisant pour deux autres ; traitement à part dans la lecture : absent (C3, C7).**

- Les quatre prédictions HE1.3, HE2.5, HE3.4 et HE6.3 sont étiquetées [exploratoire vu] dans leur définition (lignes 88, 106, 112, 139), leurs règles de sélection sont écrites (lignes 169 à 172), les sorties exploratoires sont jointes et empreintées, et leurs valeurs recopiées exactement (point 9). La section Transparence (lignes 287 à 303) dit clairement qu'elles ne valent pas prédiction indépendante.
- **Deux autres prédictions sont en réalité informées par l'exploration sans le dire** : (i) HE2.4 pour `pas_moyenne` et `coelev_somme3` n'a ni borne ni preuve ; le choix « m ≥ ⌈K/2⌉ » et l'exclusion de m = 2 (« exploratoire : 0,06 à 0,13 ») suivent exactement les valeurs vues (m = ⌈K/2⌉ : 0,32 à 0,90, 0,28 à 0,44). (ii) HE3.3 : le choix des cellules (`e_pas_ville` sous corrélation, `e_coelev_ville` sous effet d'épisode, et l'absence de `e_coelev_ville` sous corrélation) reproduit le constat exploratoire 0,17 à 0,32 contre 0,017 à 0,023 (HE3.2 cite d'ailleurs ces valeurs). Or la ligne 301 dit que « les explorations les recoupent, sans les avoir choisies ». À corriger (C3).
- **La lecture décisive ne les traite pas à part** : ni `lecture.py` ni `lecture.json` ni `lecture.md` ne portent la moindre marque ; `verdict` les traite comme les autres. Trois lignes de la table E reposent entièrement ou en partie sur elles : « version séquentielle » (exigée : HE2.5 seule), « laquelle détecte quoi » (exige HE1.3) et HE6 (exige HE6.3). Le texte de lecture prononcé (« Non : ... », « ... les fait passer sous leur taux de fausse alarme ») se lira, dans `lecture.md` donné aux mentors, comme une confirmation de prédiction indépendante. Correctif en code : C7.
- **Graines d'exploration disjointes de la graine décisive** : conforme. Explorations : `SeedSequence(31337)`, `(27182)`, `(16180)`, `(14142)`, chronométrage 424242, essai à blanc 271828, tests 5550555 et 987654321, tous des petits entiers sans `spawn_key`. Décisive : `SeedSequence(entropy = 128 bits du sha256, spawn_key = (64 bits de sha256(nom de tâche),))` (`manifeste.graines`, `run_essaim.entropie_depuis_prereg`, vérifiés ; `int(sha[:32], 16)` = 128 premiers bits). Flux distincts avec une probabilité de collision d'ordre 2⁻¹⁰⁰. Le préenregistrement ne le dit pas en une phrase ; à ajouter (C9).
- **Nuance sur « graine inconnue avant le scellement »** (lignes 188 et 303) : la graine est une fonction du texte final ; elle est calculable dès que le texte est figé, avant l'acte de sceller, et un pré-run dans un clone jetable (hors `runs/` du dépôt, donc sans trace pour `exiger_run_unique`) est techniquement possible. La garde est procédurale. Formulation plus exacte en C9.

## E. Fidélité du code

**Conforme sur le fond ; une erreur de procédure qui arrêterait le run (C1) ; une réserve de test (C10).**

- La commande décrite est exactement celle de `main()` (`--racine` par défaut `.`, `--prereg`, `--grille`) ; `executer` enchaîne : import sous `src/` du dépôt, préenregistrement scellé et conforme, grille scellée et citée, commit cité, run unique, graine, manifeste décisif (arbre propre, `runs/<id>` inexistant), calibrage, garde de calibrage, garde d'équivalence, blocs, lecture, résultats scellés : l'ordre du plan (lignes 192 à 198) est respecté. Blocs non sélectionnables (`blocs is not None` refusé ; aucune option en ligne de commande). Réplication : blocs déterminés par `BLOCS_DE`, R, R_cal, R₀ multipliés par 5, paramètres conformes inchangés, suffixe `/replication` présent dans le manifeste pour toutes les tâches (`ts + [x + "/replication" ...]`), fusion par `simulation_t03.lecture.fusionner`.
- Critères du tableau A : conformes à `egal`, `au_dessus`, `en_dessous`, `au_plus`, `egal_valeur`, `au_moins_valeur`, `au_plus_valeur`, `au_dessus_valeur`, `region`, `trajectoriel` (relus un à un). Cellules par prédiction : conformes. Gardes 6 (calibrage : seuil exact, MC avec z = 4,417, Ville, MC sans échantillon, seuil non fini), 7, 8, 10 : implantées comme décrit.
- **Liste d'arrêt, gardes éprouvées (R5)** : commit cité (artefact : code modifié → arrêt ; sain : chaîne complète), préenregistrement non scellé/altéré, grille non citée, blocs refusés, run unique (artefact) et réplication unique, calibrage (exact, MC, Ville : artefacts), équivalence, multi-ensemble, durée, seuil non fini, HE6. Arbre non propre, dossier de run existant, grille hors du dépôt, code importé hors `src/`, commit inconnu/abrégé : testés dans `test_manifeste.py`, `test_scellement.py`, `test_simulation_t03.py` (vérifié par grep ; les messages `non propre`, `R12`, `hors du dépôt`, `hors de`, `impossible`, `ne cite pas le commit` existent).
- **Erreur de procédure (C1)** : `exiger_code_cite` exécute `git diff --quiet <commit cité> HEAD -- src tests <grille>`. Si la grille `prereg/essaim-grille-v1.json` est ajoutée **après** le commit cité (c'est l'ordre de « Reste à faire », points 1 à 3 du rapport : committer le code, puis copier la grille au scellement), la différence est non vide (fichier ajouté) et le lanceur s'arrête. Reproduit dans un dépôt jetable : `git diff --quiet c1 HEAD -- src prereg/g.json` renvoie 1 quand `prereg/g.json` n'apparaît qu'après c1. T0.3 l'a évité (`d73ac469` contient `prereg/T0.3-grille-v2.json`). Sur le dépôt réel, le commit actuel du code (`108cea9a`) ne contient pas la grille scellée : à citer tel quel, le run s'arrêterait.
- **Arbre propre** : le dépôt contient aujourd'hui six entrées non suivies (`analyse-blanche-noire`, `p3-borne-v1`, etc.) ; `creer_manifeste` s'arrête (`--untracked-files=all`). Le rapport le dit ; le préenregistrement ne dit pas comment lancer. À ajouter dans C1.
- **Réserve de test (C10)** : `test_replication_determinee_par_la_lecture` a deux branches (rien à répliquer / réplication puis refus de la seconde). Laquelle s'exécute dépend de la graine, donc de l'empreinte du préenregistrement de test, donc du hash du commit (horodaté) : la couverture de « seconde réplication refusée » est aléatoire d'une exécution à l'autre. Non bloquant.
- Durée : « environ 4 minutes » (ligne 23) contre « ≈ 3,5 minutes » (ligne 203) ; sans conséquence, à aligner (C10).

## F. Revendications

**Conforme dans le préenregistrement ; absent de la lecture livrée aux mentors (C7).**

- Le préenregistrement dit nettement, à trois endroits, ce que la simulation ne montre pas : « C'est une vérification de l'instrument et de l'arithmétique des énoncés, sur scores synthétiques, pas une preuve sur activations réelles ni une simulation de propagation » (ligne 28) ; « ici la menace est un motif dans la matrice des scores, choisi par un attaquant dans un groupe, pas un processus de contagion » (ligne 65) ; « Une confirmation valide l'instrument... elle n'est pas une preuve empirique sur des modèles réels » (ligne 81). Le rapport joint détaille ce qu'il faudrait pour une propagation vraie. 
- Mais `lecture.md` (le fichier scellé qui sera montré) ne répète aucune de ces réserves : ni dans l'en-tête de `tableau_md`, ni dans la table E. Un lecteur qui ne verrait que ce fichier lirait « Vérifié en simulation » sans la restriction « motif de scores, pas idée qui se propage ». Correctif : C7.
- Deux phrases de la table E sont trop générales : « L'échappement de la co-élévation tient à sa lecture en maximum sur les pas, pas à la co-élévation elle-même » (valable contre la synchronisation seulement) ; « bornes exactes atteintes » (ce sont des bornes inférieures respectées, pas atteintes) : C5, C6.

## G. Symétrie R4

**Conforme pour l'essentiel ; une précision à ajouter (C2).**

- Écrit d'avance pour une issue décevante : tableau F (réfutations, non concluantes en partie), audit déclenché par toute réfutation, toute violation trajectorielle, toute garde.
- Écrit d'avance pour une issue trop belle : ligne 1 du tableau F (« réserve R4 trop beau ») et audit de variance des écarts réduits (trop propre : variance < 0,3). L'audit de variance est le dispositif symétrique, mais la ligne 1 ne prévoit qu'une réserve de rédaction quand tout est confirmé, alors qu'une seule réfutation déclenche relecture du code et de la preuve. R4 demande le même audit pour un résultat suspect de propreté, positif ou négatif. Ajouter à la ligne 1 un contrôle de même profondeur (C2, dernière rangée).
- Remarque : sur cette grille, la plupart des prédictions vérifient l'instrument et ne peuvent échouer que par erreur de code ; « tout confirmé » est donc le résultat attendu et le plus probable. La réserve rédigée est la bonne.

## H. Le bloc ajouté non demandé (HE6)

**Même exigence mécanique que le reste ; exigence de lecture plus faible (C7).**

- Au même niveau : calibrage MC aléatoirisé sur 100 000 essaims corrélés entiers, garde de calibrage propre dans la liste d'arrêt (item 6), tâches nommées et dérivées, 30 cellules (4 + 20 + 6), prédictions étiquetées (HE6.1 et HE6.2 démontrées par T1 trajectoriel, HE6.3 [exploratoire vu]), cas descriptifs écrits (c = 0,2 avec m = 5, `coelev_somme3`), ligne dans le tableau F, ligne dans la table E, test de garde HE6 (sain + artefact), mini-grille de bout en bout.
- Plus faible : HE6.3 n'a ni forme close ni borne ; elle repose uniquement sur une exploration à 10 × 22 ; la table E l'exige pourtant pour prononcer la ligne HE6, et le mécanisme avancé (« les maxima synchronisés sont arrachés au pas où la corrélation les faisait co-élever naturellement ») n'est testé nulle part : ni cellule, ni mesure de l'emplacement des maxima. Le texte le présente comme un fait. À scinder : la partie démontrée (aveugle) et la partie vue (puissance de la co-élévation) ; le mécanisme à présenter comme conjecture (C7).
- Utilité : la question est bien celle que le papier B posera en premier ; je recommande de la garder.

---

# Corrections, avec texte de remplacement

Convention : « ligne » = numéro de ligne du brouillon 1. Les corrections C5, C6 et C7 touchent `lecture.py` (donc le commit cité, mais pas la grille ni l'annexe : leurs empreintes ne changent pas) ; toutes les autres sont textuelles. Après C5 à C7, la table E du préenregistrement doit rester recopiée mot pour mot depuis `LIGNES_E`, et `test_table_E_et_blocs_de_lecture` ainsi que le compte de lignes de la table (8 → 9 si on scinde HE6) sont à mettre à jour.

## C1. Ordre de scellement et commit cité (obligatoire ; le run s'arrêterait sinon)

Ligne 7, remplacer par :

```
- Commit du code d'analyse : `<<COMMIT_CODE>>` (40 caractères hexadécimaux). C'est un commit qui contient ensemble `src/`, `tests/`, `prereg/essaim-grille-v1.json` et son empreinte compagnon `prereg/essaim-grille-v1.json.sha256` ; il précède le commit qui ajoute ce préenregistrement scellé. La garde du lanceur compare ce commit à HEAD sur `src/`, `tests/` et la grille : une grille ajoutée après lui, ou un commit d'une autre session sur `src/` ou `tests/` entre lui et le run, arrête le run.
```

Dans « Plan d'analyse », en tête de la liste « Ordre d'exécution », ajouter :

```
  0. Mise en place, avant tout calcul : (a) copier la grille sous `prereg/essaim-grille-v1.json` et la sceller ; (b) committer : ce commit est le commit cité ; (c) remplacer les deux marqueurs de ce texte (commit cité, contre-lecture), sceller le préenregistrement, committer ; (d) lancer la commande depuis un clone propre au commit obtenu en (c) (le manifeste exige un arbre de travail propre, fichiers non suivis compris) puis committer et pousser `runs/` et `diag/`.
```

Aligner le point 3 du « Reste à faire » du rapport joint sur cet ordre.

## C2. Issues écrites d'avance manquantes (tableau F)

Ajouter ces lignes au tableau F (avant la ligne « Audit de symétrie déclenché ») :

```
| HE3.1 réfutée (Ville dépassé sous la loi de référence) | Erreur du processus e, des comptes ou du seuil de Ville : la martingale n'est pas une martingale. | Audit de `statistiques.e_coelev` / `e_pas` et des comptes ; la ligne HE3 de la table E tombe ; aucune recommandation de calibrage. |
| HE3.6 réfutée (taux hors hypothèses ≠ forme close) | Forme close fausse (quadrature, loi tirée ≠ loi supposée) ou erreur de `lois`. | Audit de `fausses_alarmes_reference` et de `lois` ; réplication (critère C) ; la ligne HE3 de la table E tombe. |
| HE4.1, HE4.2 ou HE4.3 réfutée | Forme close ou seuil/départage faux (les formes closes sont éprouvées par Monte-Carlo dans les tests, donc plutôt un défaut de tirage ou de motif). | Réplication (critère C) ; si la contrariété persiste, audit de `puissances_decalage` et de `decalages` ; la ligne « laquelle détecte quoi » tombe. |
| HE2.4 réfutée (une cellule significativement sous ou au niveau du taux) | La borne ou la synchronisation est fausse, ou la prédiction heuristique (`pas_moyenne`, `coelev_somme3`) est fausse. | Audit ; HE2 non établie (comme HE2.3). |
| HE1.3, HE2.4, HE2.5, HE3.3, HE3.4 ou HE6.3 non concluante | L'effet est plus faible que prévu ou de sens non tranché au niveau 1 − 10⁻⁵. | Lecture correspondante « non établi » (mécanique) ; magnitudes descriptives ; pas de réplication (seules les contraires sont rejouées). |
| Toute prédiction non citée ci-dessus réfutée ou non concluante | — | Réfutée : réplication (critère C) si statistique, audit si trajectorielle ; non concluante : lectures qui l'exigent « non établi ». |
```

Remplacer l'action de la première ligne du tableau F (« Toutes les prédictions confirmées, audit non déclenché ») par :

```
Réserve R4 « trop beau » : la plupart des prédictions vérifient l'instrument ; résumé pour les mentors. Même contrôle qu'après une réfutation, par symétrie : relecture, par un sous-agent neuf, de `puissances_decalage` et de `fausses_alarmes_reference` (formes closes) et de la construction des cellules « égal » (échantillon indépendant de celui du taux sous P₀), avant tout résumé.
```

## C3. Étiquetage des lectures préalables non déclarées

Remplacer la ligne 301 (« HE2.4 et HE3.3 sont heuristiques... ») par :

```
- HE2.4 (en ce qui concerne `pas_moyenne` et `coelev_somme3`, sans borne ni preuve) et HE3.3 (en ce qui concerne le choix de ses cellules : `e_pas_ville` sous corrélation, `e_coelev_ville` sous effet d'épisode, et l'absence de `e_coelev_ville` sous corrélation) sont heuristiques, et le choix de leurs cellules, comme l'exclusion de m = 2 en HE2.4, a été fait en connaissant les valeurs exploratoires (0,32 à 0,90 et 0,28 à 0,44 à m = ⌈K/2⌉ ; 0,06 à 0,13 à m = 2 ; 0,17 à 0,32 contre 0,017 à 0,023 en Ville). Ces cellules sont donc aussi [exploratoire vu] : leur confirmation dit que l'effet se reproduit à graine neuve, pas qu'il a été prédit indépendamment. HE2.4 pour `coelev_comptage` (borne exacte) et HE3.2 (martingale démontrée) ne sont pas touchées dans leur signe.
```

Ligne 105 (HE2.4) : remplacer l'étiquette « [borne exacte et heuristique ; informative] » par « [borne exacte pour `coelev_comptage` ; heuristique et exploratoire vu pour `pas_moyenne` et `coelev_somme3` ; informative] ». Ligne 111 (HE3.3) : « [heuristique : ... ; analogue de T0.3, P8.2] » devient « [heuristique : ... ; analogue de T0.3, P8.2 ; choix des cellules exploratoire vu] ». Ligne 110 (HE3.2) : ajouter « (les valeurs exploratoires 0,017 à 0,023 ont été vues ; le signe est démontré) ».

## C4. Ampleur des effets (lignes 172 et 187)

Ligne 172, remplacer par :

```
  - HE1.3 et HE6.3 : sens et cellules de l'exploratoire, sur les seuls effets d'ampleur ≥ 0,1 en taux quand le sens est « au-dessus », et ≥ 0,03 quand il est « en dessous » (un taux ne pouvant baisser de plus de 0,05) ;
```

Dans la justification de la ligne 187, remplacer « les effets informatifs prédits sont d'au moins 0,1 en taux, et les formes closes s'éprouvent à 0,007 près vers p = 0,05 » par :

```
les effets informatifs « au-dessus » prédits sont d'au moins 0,1 en taux (HE1.3, HE6.3), ont une borne exacte d'au moins 0,27 (HE2.4, `coelev_comptage`) ou valent au moins 0,02 au-dessus de la référence de Ville (HE3.3, HE3.4) ; les effets « en dessous » valent au moins 0,03 (HE1.3 relais, HE2.5, HE6.3) ; à R = 20 000 contre R₀ = 100 000 et γ = 10⁻⁵, un écart autour de 0,05 n'est distingué qu'à partir d'environ 0,010 (puissance 99,7 % à un taux vrai de 0,065, plus de 99,99 % à 0,070) et les formes closes s'éprouvent à 0,007 près vers p = 0,05
```

## C5. Schur-concavité (ligne 61 et ligne de la table E, version séquentielle)

Ligne 61, remplacer par :

```
- Sa version séquentielle linéaire n'a, elle, que G_A pour groupe d'invariance. À total de comptes fixé, elle est une fonction Schur-concave du vecteur (C_t) à la dernière étape, et le total est G_T-invariant ; la synchronisation concentre les comptes, ce qui suggère qu'elle l'abaisse (HE2.5, heuristique, vue en exploration). Cet argument n'est démontré ni pour le supremum sur les étapes n, ni pour un attaquant de G_T autre que la synchronisation (un attaquant qui étale les comptes ferait l'inverse). L'échappement de la co-élévation contre la synchronisation tient à sa lecture en maximum sur les pas.
```

Dans `LIGNES_E`, quatrième ligne (et donc dans la table du préenregistrement, mot pour mot), remplacer la fin de la lecture (de « La synchronisation conserve le total... » jusqu'à la fin) par :

```
Lecture heuristique, choisie après exploration (confirmation à graine neuve, pas prédiction indépendante) : à total de comptes fixé, Σ_t log(1 + λ(C_t − Kq)) est Schur-concave en (C_t), ce qui suggère, sans le démontrer pour le supremum sur n ni pour un attaquant de G_T autre que la synchronisation, que la concentration l'abaisse. L'échappement de la co-élévation contre la synchronisation tient à sa lecture en maximum sur les pas.
```

## C6. Tête de HE2 (lignes 50 et 59) et mot « atteintes »

Ligne 50 : remplacer « et la co-élévation lue en maximum sur les pas a une puissance au-dessus de son taux, avec des bornes inférieures exactes » par « et la co-élévation lue en maximum sur les pas a une puissance au-dessus de son taux dès que la moitié de l'essaim au moins se synchronise (m ≥ ⌈K/2⌉), avec des bornes inférieures exactes ; à m = 2 les bornes sont sous α et la puissance est descriptive ». Ligne 59 : même ajout après « (HE2) ».

Dans `LIGNES_E`, troisième ligne, remplacer « bornes exactes atteintes, puissance au-dessus de son taux » par « bornes inférieures exactes respectées, puissance au-dessus de son taux dès que la moitié de l'essaim au moins se synchronise ».

## C7. Lecture livrée aux mentors : statut exploratoire, réserve de portée, scission de HE6 (touche `lecture.py`)

Dans `lecture.py`, ajouter après `BORNES_AUDIT` :

```python
EXPLORATOIRES = frozenset({"HE1.3", "HE2.5", "HE3.4", "HE6.3"})   # choisies après exploration ; HE2.4 et HE3.3 en partie
```

Dans `Lecteur.lire`, ajouter dans le dictionnaire de chaque prédiction : `"statut": "exploratoire vu" if pred in EXPLORATOIRES else "préenregistrée"`, et ajouter une colonne `statut` dans `run_essaim.tableau_md` ; en tête du fichier produit, après la deuxième ligne, une phrase fixe :

```
Simulation sur scores synthétiques : la menace est un motif dans la matrice des scores, pas une idée qui se propage ; aucune conclusion sur des activations réelles, ni sur une contagion. Les prédictions « exploratoire vu » reproduisent à graine neuve un effet observé avant le préenregistrement : elles ne valent pas confirmation indépendante.
```

Scinder la huitième ligne de `LIGNES_E` en deux :

```
{"enonce": "HE6a : sous corrélation entre copies d'un même pas (poids partagés), la surveillance par agent reste-t-elle aveugle à la synchronisation ?",
 "lecture": "Oui : aveugle, même quand P₀ n'est pas invariante sous G_T (T1 est trajectoriel).",
 "exiges": ["HE6.1", "HE6.2"], "complementaires": []},
{"enonce": "HE6b : sous corrélation entre copies d'un même pas, la co-élévation calibrée sur essaims honnêtes entiers garde-t-elle sa puissance contre la synchronisation ?",
 "lecture": "Co-élévation et moyenne par pas, calibrées sur essaims corrélés entiers, détectent encore la synchronisation de tous les agents ; une synchronisation de la moitié de l'essaim sous forte corrélation les fait passer sous leur taux de fausse alarme. Effet vu en exploration avant le préenregistrement, reproduit à graine neuve : pas une prédiction indépendante. Mécanisme conjecturé, non testé : les maxima synchronisés quitteraient le pas où la corrélation les faisait co-élever. Le sens de la puissance de la co-élévation dépend donc de la structure de corrélation honnête, pas seulement de l'invariance.",
 "exiges": ["HE6.3"], "complementaires": []}
```

Recopier ces lignes dans la table E du préenregistrement (mot pour mot), et mettre à jour `test_table_E_et_blocs_de_lecture` ainsi que la phrase de la ligne 242 (« 8 lignes » devient 9). Si l'auteur préfère ne pas toucher au code : à défaut, ajouter au préenregistrement, section « Critères de lecture gelés », une règle écrite : « le rapport aux mentors cite HE1.3, HE2.5, HE3.4, HE6.3 (et les cellules de HE2.4 et HE3.3 signalées en C3) à part, sous l'étiquette exploratoire vu, et reproduit la phrase de portée ci-dessus » ; moins fort, car non mécanique.

## C8. Multiplicité (ligne 200)

Remplacer « Ce risque est traité par... » précédé de la phrase de borne, soit « Pour chaque cellule statistique, ... ≈ 0,8 % pour le run », par :

```
Pour chaque cellule statistique, la probabilité d'une fausse contrariété est au plus γ = 10⁻⁵ (critères à un intervalle ou à une forme close) et au plus 2γ pour les 263 cellules « égal » entre deux intervalles indépendants (deux intervalles disjoints exigent qu'au moins l'un manque sa cible). Borne de l'union : (512 × 1 + 263 × 2) × 10⁻⁵ ≈ 1,0 % pour le run.
```

## C9. Graines : disjonction et moment de connaissance (lignes 188, 303 et rapport)

Dans « Graine racine », remplacer « Elle n'est connue qu'au scellement, après la contre-lecture » par « Elle est une fonction du texte final ; elle se calcule dès que ce texte est figé, et aucun calcul n'est fait avec elle avant le run décisif (aucun pré-run, ni dans le dépôt ni dans un clone) ». Ajouter à la fin du paragraphe :

```
Les graines des explorations, du chronométrage, de l'essai à blanc et des tests (31337, 27182, 16180, 14142, 424242, 271828, 5550555, 987654321) sont de petits entiers sans clé de dérivation ; la graine décisive est un entier de 128 bits avec une clé de dérivation par tâche : flux disjoints (collision d'ordre 2⁻¹⁰⁰).
```

## C10. Précisions mineures

- Ligne 49 : remplacer « Sous G_A, seule la surveillance par agent peut détecter » par « Sous G_A, seule la surveillance par agent du panneau peut détecter ».
- Ligne 23 : « environ 4 minutes » devient « environ 3,5 minutes, jusqu'au double sous forte charge », pour s'accorder avec la ligne 203.
- Test : dans `test_replication_determinee_par_la_lecture`, rendre déterministe la branche couverte (par exemple en fixant la date des commits du dépôt jetable par `GIT_COMMITTER_DATE` et `GIT_AUTHOR_DATE`, ou en testant les deux branches par deux sous-tests forcés). Non bloquant, mais la couverture de « seconde réplication refusée » est aujourd'hui aléatoire.
- Section Contre-lecture : citer, pour ce rapport, son chemin et son empreinte, et pour le brouillon relu l'empreinte `b9b1109e…dfdfc` ci-dessus ; traiter chaque correction C1 à C10 (accepté, refusé et pourquoi). Si C5 à C7 touchent `lecture.py`, la contre-lecture de la différence est à faire sur ces seules lignes.

## Points vérifiés et laissés tels quels (pour éviter une seconde lecture)

Table E identique à `LIGNES_E` ; 824/775/49 ; formes closes et bornes ; région conforme ; empreintes des sept documents et de la grille ; valeurs exploratoires ; critères de lecture implantés ; ordre d'exécution ; fonctionnement des gardes de calibrage ; couverture des gardes par les tests (cas sain + artefact) ; indépendance des cellules et de l'échantillon des taux sous P₀ ; nombre de répétitions suffisant pour les effets informatifs ; HE6 conservé.
