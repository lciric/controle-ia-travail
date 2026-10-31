# Annexe des paramètres du bras méta, version 1 (« trou à structure commune ») — brouillon 1

**Statut : brouillon 1, non scellé ; valeurs proposées, aucune gelée ; contre-lecture à faire.** Chaque valeur est une proposition « À GELER par Lazar », donnée avec sa raison, une alternative et ma confiance. Rien n'est lancé ; aucune dépense ; aucun réseau. Le bloc lisible par le code (section 8) porte exprès, dans `contre_lecture` et `approbation_lazar`, le marqueur que `lire_annexe_meta` refuse : tant qu'ils ne sont pas remplis, le code v53 déclare le bras méta « non produit (annexe non conforme) » (A20). Ce brouillon ne peut donc pas être pris par erreur pour l'annexe scellée.

- **Exigée par** : `preenregistrement-pre-pilote-course-2-brouillon7.md` (même dossier, `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5`), M9 (bras méta), S28, S29 (a à f), Plan É0, A20, garde R5 lignes 22a, 22b, 23, 24, DEP10. Nom de la version scellée attendu par le préenregistrement : `annexe-bras-meta-v1.md` (même dossier).
- **Auteur** : sous-agent neuf Opus 5.5 de la lignée conv-audit, 31 octobre 2026. **A9 respecté** : je n'ai lu aucune fiche de Kimi, aucun témoin, aucune clé, rien sous `donnees/`. **Réserve d'indépendance** : le préenregistrement demande une « instance tierce » ; je suis de la lignée conv-audit, qui conçoit les moniteurs (R-824) et dont Opus 5.5 est troisième juge. La contre-lecture doit donc venir d'un autre modèle qu'Opus (Sonnet 5.5 ou Fable 5.1), comme le prévoit R2.
- **Après les verdicts des collisionneurs (R-638, DEP10)** : j'ai lu la synthèse v2 du lot bisociateur (n° 262, étage 3). Je n'ai pas vérifié que les verdicts des questions 4 à 7 sont tous rendus et scellés : à vérifier avant la contre-lecture (réserve R1).
- **Pièces lues (sha256sum à la lecture)** :
  - préenregistrement brouillon 7 (ci-dessus ; compagnon `.sha256` conforme) ;
  - code v53 : `docs/notes/ideation-organisme-v1/orchestrateur-v53/pole/bisociateur_v53.py` `962eb8ce22d5af1bf59970e9ef9cab15620edef4d5e9746161bc302e97c2af02` ; `configuration_v53.py` `ef72ffbf6b5ba546fb5e509502b59f0d9ac4f78772dcb9570ef36086639f4a78` ; `course2_v53.py` `8f2d035828df913d8fa92e1b7d0c8e41ac73e8416e60f3b674753c27f5c61237` ; `outils.py` `966d9553026aad1eb7d97fa677334f1b59f22a39f15eef95134d63bc47634444` ; `essais/aides_v53.py` `4aaddd698fe1400430e59d5449541acde8f7a6346169a1978d533e948b79c51e` ; `LISEZMOI-orchestrateur-pole-v7-v53.md` `a4f599cf8a2ff748d2250c5f649ac03863066122a9661ea057c76b0ece26413c` ;
  - `docs/notes/bisociation-litterature-reelle-v1/collisionneur-bisociation-lot-v1/synthese-bisociation-lot-v2.md` `23c2888ddd924b85a0bbd0009a17f64723399d69ffd17669f56c4fddf7d18a86` ;
  - `bisociation-niches-v1/reponse-conv-audit-question-1-v2.md` `0edee5d7cbdaccc4f0d3378bac1956f72fdf8c91eda12a28a9ff6e4bba1e1364` ; `…question-2-v2.md` `adb640c625ad23d4a14c732758bf1fbc39973a0d58f95e4fe6f848cf7e02f7c9` ; `…question-3-v2.md` `5f63dcb917ae050838c19af1f8743b8d2d218ec2b6d5e60fb7e2ada69aa04319` ; `revue-biblio-fertilite-v1.md` `307b4f2fe6e53dcfa517c6da5d2591a6cee1e1508cd8197f4778fe014d6b718f` ; `lecture-reponse-argon-bisociation-v1.md` `3271d0e25cafa6a5df048547249debf958bd9a830c0099afd38cac4a88de8b96` ;
  - `registres/decisions.md` (contenu vivant, `5ffac1845351b81e7453c0326bcb5122b24e8d0c3a575e8022b69b9191a66946` à la lecture) : lignes R-635 à R-643 ;
  - texte I de la course 2, `question-mere-course-v1/recoupement-v1/question-course-2-defense-fusion-v5.md` `a750144963913ba1c3dcf3eed5d4f8322d7d0246135e17c95ac8e7253c2dd680` : glossaire, axes, annexe 1 (listes L, M, D, F, esquisse de grille des sous-domaines), source des niches exigée par M9 ;
  - **Uzzi, Mukherjee, Stringer, Jones 2013**, *Science* 342, 468-472 : `docs/sources/pdf/bisociation-fertilite-v1/uzzi-mukherjee-stringer-jones-2013-science.pdf` `532970985650d07fe69c66d912dfae96d6f45522fcb72e92c88857f4fd101173` (compagnon conforme ; texte extrait par `pdftotext` page par page ; pages 469 et 471 lues aux passages cités, section 5).
- **Calculs joués pour ce brouillon (hors dépôt, `python3 -I`, python 3.13.18, numpy 2.5.3)** : prédiction P14 refaite (section 6, script recopié en entier, `0ceedcb68852d10c9dda56191ad661aacd895ebda43758bca78862a65a60e879`, sortie `b2a0a325599f10905f645d30d724a4c6ec3d54ebcc45fa4f873ba7dca7cdeb7a`, rejeu identique octet pour octet) ; épreuve du bloc de paramètres et du jeu d'essai contre les fonctions réelles de `bisociateur_v53.py` (section 6). Le script et sa sortie ne sont pas versés : je n'avais le droit d'écrire que ce fichier ; à verser avec compagnon au scellement (R6).

## Résumé (dix lignes)

1. **Grille** : six niches du sous-domaine « contrôle des intelligences artificielles et environnements de comparaison », chacune définie par la communauté dont la méthode porte l'affirmation centrale de la fiche, jamais par l'axe (sinon le bras méta recopierait le domaine du bras basique).
2. **Accord (S28)** : kappa de Cohen sur la niche ≥ 0,40 ; Jaccard moyen sur les structures ≥ 0,30 ; marges constantes lues 1 ou 0 et marquées « dégénérée sur ce lot » (règle du brouillon 7, codée telle quelle dans v53).
3. **Communication faible** : pas de citations au pré-pilote ; ce qui en tient lieu est une **table du canal entre niches** (0 à 3), écrite à la main avant toute fiche, propriété de la paire de niches et non de la paire de fiches ; « faible » = 0 ou 1.
4. **Structure forte** : liste fermée de 20 structures nommées en quatre types ; « forte » = au moins une structure partagée de type objet mathématique ou méthode ; jeux de données et protocoles sont lus mais ne comptent pas (le texte I les impose presque tous à toutes les fiches).
5. **Désaccord** : lu par paire, **après** le choix des paires, journalisé dans un fichier scellé, jamais passé à la fonction de score.
6. **Éloignement** : table de distance de contenu (1 à 5) ; bande [2 ; 3] ; l'exclusion des paires extrêmes s'appuie sur Uzzi 2013, vérifié sur PDF (p. 471), mais **sa transposition aux niches est SUPPOSÉ**.
7. **Score** : 1[faible] × 1[forte] × 1[bande] × (1 + 0,5 × s) ; repli `indicateurs_puis_structure`, seul admis par le code ; profil non vide sur le jeu d'essai (5 paires dans le profil, 36 hors profil, 4 refusées pour même niche).
8. **P14 refaite (indicative)** : 4 paires de niches sur 15 dans le profil ; à 10 fiches, médiane 1 paire dans le profil, zéro avec 0,25 ; à 6 fiches, médiane 0, zéro avec 0,59 : **le repli sera souvent seul éprouvé**.
9. **Incompatibilités** avec le code v53 : dix, dont trois qui demandent une version 54 avant É0 (noms de structure non contrôlés, désaccord non lu, cause « aucune paire notable » absente de C12) (section 10).
10. **Procédure** : contre-lecture par un modèle différent, mot de Lazar sur chaque valeur, remplissage des deux champs, scellement, empreinte écrite au préenregistrement et dans la configuration avant É0 ; sans cela, A20.

## 1. Grille fermée des niches (S29 a)

**Périmètre.** Fiches non aiguillées de la passe 1 de Kimi, case unique (texte I, bras de défense, axes 1 à 5), au pré-pilote ; mêmes niches dans la course 2, génération 1, pour toutes les cases (une grille de génération 1, raffinée en génération 2, R-638). Sources de la grille (M9) : glossaire et axes du texte I ; listes L, M, F de son annexe 1 ; esquisse de grille des sous-domaines de la même annexe (non arrêtée, reprise comme matériau, non comme vérité). La carte des chapelles (R-637) n'existe pas encore : non utilisée.

**Proposition (À GELER par Lazar).** Six niches. Une fiche reçoit la niche **de la communauté dont la méthode porte son affirmation centrale** (champ « hypothèse » du texte I), pas celle de son axe ni de son matériau secondaire.

| Identifiant (servi au lecteur) | Définition en une ligne | Mots-indices (non exhaustifs ; un indice ne suffit pas, c'est la méthode de l'affirmation centrale qui décide) |
|---|---|---|
| `n1_detection_sequentielle` | statistique séquentielle : décider au fil de la trajectoire qu'une loi a changé, avec fausse alerte tenue à tout instant | somme cumulée, test séquentiel du rapport de vraisemblance, e-valeur, test valide à tout instant, temps d'arrêt, délai de détection, agrégation dans le temps |
| `n2_lecture_activations` | lire ou modifier les activations internes d'un modèle à poids ouverts pour en tirer un signal | sonde linéaire, direction, couche, jeton lu, auto-encodeur parcimonieux, dictionnaire de caractéristiques, intervention ou ablation sur activations, plancher apparié |
| `n3_anomalies_hors_distribution` | détecter ce qui s'écarte d'une loi de référence apprise, sans modèle de l'écart, en une fois | distance de Mahalanobis, estimation de densité, seuil conforme, score d'anomalie, calibration, rejet hors distribution |
| `n4_moniteurs_et_protocoles` | surveiller un agent par un autre modèle et organiser l'audit autour de lui | moniteur par modèle, juge, budget d'audit, rééchantillonnage, édition, report, collusion, chaîne de raisonnement lue |
| `n5_bornes_et_theorie` | énoncés prouvés : impossibilités, garanties, bornes d'information ou de délai | borne, impossibilité, garantie, divergence, théorie de l'information, preuve dans Lean, classe de lois déplacées, angle mort |
| `n6_science_evaluation` | concevoir et lire des bancs de comparaison : transfert, familles tenues à l'écart, puissance, robustesse au changement de loi | banc, environnement de comparaison, famille tenue à l'écart, transfert, universalité, puissance simulée, préenregistrement, équipe rouge |

- **Raison** : (i) ces six communautés correspondent aux grandes familles de méthodes que le texte I met en jeu (axe 1 : statistiques et agrégateurs ; axe 4 : universalité ; axe 5 : théorie ; matériau : Mahalanobis, auto-encodeurs, e-valeurs, seuils conformes) et aux cases de l'esquisse de grille (détection et surveillance ; protocoles de contrôle ; audit par interprétabilité ; science de l'évaluation) ; (ii) six est la finesse jouée par le script v6 (paramètres fictifs) ; avec au plus 10 fiches, davantage de niches viderait les cases, moins rendrait la plupart des paires « même niche » (refusées) ; (iii) la règle « méthode de l'affirmation centrale » sépare la niche de l'axe, condition pour que le bras méta ne recopie pas le domaine du bras basique (D-e).
- **Alternative** : (b) quatre niches (fusionner n1 et n5, n3 et n2) — avantage : accord des lecteurs plus haut ; inconvénient : le profil perd sa paire la plus nette (lecture des activations contre bornes) et la plupart des paires de fiches tombent dans une même niche ; (c) grille de la carte des chapelles quand elle existera (R-637, R-638) — avantage : niches mesurées sur la littérature et non posées à la main ; inconvénient : n'existe pas avant É0.
- **Confiance** : 0,45 (la grille est une conjecture de l'auteur ; aucune donnée ne la valide).
- **Réserve** : le programme lui-même fusionne n1 et n2 (boîte blanche séquentielle) ; la communication de la table (section 2) est celle de la littérature, pas celle du programme. Les fiches de Kimi risquent donc de se concentrer en n1 et n2 ; la prédiction P14 en tient compte (loi a priori, section 6).

**Règle de lecture (À GELER par Lazar).** Deux lecteurs neufs, isolés l'un de l'autre et du dépôt, qui ne connaissent ni les règles ni les bras (M9, A4) ; chacun lit une fiche par appel (comme le code v53) et rend `{"niche": identifiant, "structures": [...]}` ; **une niche exactement**, prise dans la grille (choix forcé : pas de « autre », pas d'« indécidable » ; le code rejette toute niche hors grille, garde R5 ligne 23). **Une fiche n'entre au bras méta que si les deux lecteurs lui donnent la même niche** (règle déjà codée dans v53, choix de code 10 du LISEZMOI, que je propose de geler en mots) ; ses structures sont l'**union** des deux lectures (même source). La définition et les mots-indices de la table ci-dessus sont **recopiés mot pour mot dans la consigne figée du lecteur** (pièce empreintée) : le code ne sert au lecteur que les identifiants (incompatibilité I-4).
- Raison : la règle d'accord par fiche évite qu'une niche disputée crée une paire « loin » par erreur de lecture ; l'union des structures est le choix le plus favorable au profil, compensé par la liste fermée (section 3).
- Alternative : niche du premier lecteur, le second ne servant qu'à l'accord — avantage : n effectif plus grand ; inconvénient : une erreur de lecture suffit à fabriquer une paire « loin ».
- Confiance : 0,6.

**Accord exigé (S28 ; À GELER par Lazar).** **Kappa de Cohen sur la niche ≥ 0,40 ; Jaccard moyen sur les structures ≥ 0,30** (règle de S24 : fiche sans structure chez les deux lecteurs exclue et comptée ; chez un seul, Jaccard 0 ; fonction `accord_jaccard` du code).
- Raison : 0,40 est le repère S24 donné par le brouillon 7 ; le Jaccard sur des structures nommées est plus exigeant qu'un Jaccard sur des concepts (une structure oubliée par un lecteur coûte beaucoup sur 2 ou 3 étiquettes), d'où 0,30. À 10 fiches, l'erreur-type du kappa est de l'ordre de 0,3 (SUPPOSÉ, brouillon 7) : garde grossière.
- Alternative : 0,50 et 0,40 — avantage : la grille n'est déclarée lisible que si elle l'est nettement ; inconvénient : avec P14 à 0,5 [0,2 ; 0,8], l'issue « niches non lisibles » deviendrait la plus probable.
- Confiance : 0,4.
- Conséquence (brouillon 7, inchangée) : sous S28, grille « illisible », bras méta marqué « niches non lisibles », nœud joint à la demande de GO de la course sans l'empêcher ; **le bras n'est pas retiré** (R-638).

**Marges dégénérées (règle du brouillon 7, codée dans `kappa_niches`, vérifiée sur le code).** Si chacun des deux lecteurs pose une seule niche sur toutes les fiches : kappa lu 1 si les deux niches coïncident, 0 sinon ; grille marquée « dégénérée sur ce lot » (réserve). Si un seul lecteur est constant, le kappa se calcule par la formule ordinaire (il peut être nul ou négatif) : aucune règle spéciale, je propose de l'écrire ainsi.

**Cas « une seule niche pour toutes les fiches » (les deux lecteurs d'accord).** Kappa 1, dégénéré ; aucune paire de niches différentes : le code v53 déclare alors le bras méta « non produit (aucune paire notable) ». **Proposition de lecture (À GELER par Lazar)** : cause écrite « non produit (niches indistinctes sur ce lot) », « non lancé », comptée dans C12 comme les autres bras non produits, réserve « grille dégénérée », O15 ouverte ; pas un échec de garde. Le brouillon 7 ne connaît pas cette cause (incompatibilité I-7). Probabilité (P14 refaite, section 6) : aucune paire éligible 0,04 à 6 fiches, 0,002 à 10 fiches, accord par fiche 0,7 (SUPPOSÉ).

## 2. Communication faible (S29 b)

**Ce qui tient lieu de citations.** Le pré-pilote n'a ni citations ni graphe : les fiches sont écrites par Kimi dans une même session. La communication ne peut donc pas être lue sur la paire de fiches ; elle est une **propriété de la paire de niches**, lue dans la **littérature du sous-domaine** et fixée **avant toute fiche**. C'est le « canal » de la réponse 2 v2 (section 1 : capacité d'échange — personnes, revues, conférences, vocabulaire communs), distinct du flux et de la distance de contenu (section 5).

**Proposition (À GELER par Lazar).** Table c(n_a, n_b) **écrite à la main par l'auteur de l'annexe**, échelle 0 à 3 (0 : aucun échange connu ; 1 : échanges rares ; 2 : échanges réguliers, revues ou conférences partagées ; 3 : même communauté en pratique), SUPPOSÉ ; **« faible » = c ≤ 1**.

| c (canal) | n2 activations | n3 anomalies | n4 moniteurs | n5 bornes | n6 évaluation |
|---|---|---|---|---|---|
| **n1 séquentiel** | 1 | 2 | 1 | 3 | 1 |
| **n2 activations** | — | 2 | 2 | 0 | 2 |
| **n3 anomalies** | | — | 1 | 2 | 2 |
| **n4 moniteurs** | | | — | 1 | 3 |
| **n5 bornes** | | | | — | 1 |

- Raison du seuil : avec ce seuil, 7 paires de niches sur 15 sont « faibles » ; « faible » reste une minorité, ce qui garde son sens (à c ≤ 2, 13 sur 15 le seraient). Raison des valeurs (une par cellule, de mémoire, SUPPOSÉ) : détection séquentielle et bornes de délai forment une seule tradition statistique (3) ; moniteurs et évaluation par équipes rouges vivent dans les mêmes laboratoires et ateliers du contrôle des intelligences artificielles (3) ; interprétabilité et bornes formelles ne se lisent presque pas (0) ; Mahalanobis sur activations et détection hors distribution échangent (2).
- Alternatives : (b) table calculée sur la moisson OpenAlex de R-633 (co-occurrence des concepts-indices des deux niches, flux observé contre attendu sous modèle nul à degrés conservés, comme le propose la réponse 2 v2) — avantage : mesurée, non posée ; inconvénients : la moisson n'est pas encore empreintée ni essayée pour S31, la correspondance niche → concepts d'OpenAlex est elle-même un choix à la main, et c'est un flux de citations (défaut A0 de la synthèse s'il servait plus tard d'étiquette) ; (c) deux tables remplies indépendamment par deux instances de familles différentes, moyenne arrondie — avantage : retire une partie de l'idiosyncrasie de l'auteur ; inconvénient : deux lectures de plus avant le gel (sans fiche, sans dépense de calcul payant si faites par sous-agents).
- Recommandation : (a), avec, si la moisson est empreintée avant le gel, un essai de concordance de rang entre (a) et (b) **rapporté** dans la version contre-lue (permis : aucune fiche n'est lue ; les valeurs peuvent encore changer avant le gel, jamais après).
- Confiance : 0,45 pour la table ; 0,5 pour le seuil c ≤ 1.

## 3. Structure commune forte (S29 c)

**Types admis (À GELER par Lazar)** : objet mathématique (`om_`), méthode (`me_`), jeu de données (`jd_`), protocole (`pr_`). **Liste fermée de 20 structures nommées** (le lecteur choisit dans la liste ; aucune structure libre) :

| Type | Identifiants (définition entre parenthèses) |
|---|---|
| objet mathématique | `om_martingale_e_processus` (martingale, surmartingale, e-processus) ; `om_rapport_vraisemblance_divergence` (rapport de vraisemblance, divergence) ; `om_covariance_mahalanobis` (matrice de covariance, distance de Mahalanobis) ; `om_direction_sous_espace` (direction, projection, sous-espace) ; `om_somme_cumulee_temps_arret` (somme cumulée, marche aléatoire, temps d'arrêt) ; `om_jeu_minimax` (jeu à deux, stratégie minimax, équilibre) ; `om_graphe_causal` (graphe causal, intervention) |
| méthode | `me_test_sequentiel_cusum` ; `me_seuil_conforme` ; `me_dictionnaire_parcimonieux` (auto-encodeur parcimonieux) ; `me_intervention_activations` (patching, ablation) ; `me_moniteur_par_modele` ; `me_estimation_densite` ; `me_preuve_formelle` (Lean) |
| jeu de données | `jd_simulateur_fige` (D1) ; `jd_donnees_publiques` (D2) ; `jd_notations_juges` (D3) |
| protocole | `pr_exclusion_famille` (une famille exclue à la fois) ; `pr_audit_budgete` ; `pr_reechantillonnage_report` |

**« Forte » (À GELER par Lazar)** : **au moins 1 structure partagée** (même identifiant chez les deux fiches) **parmi les objets mathématiques et les méthodes** ; jeux de données et protocoles sont lus, rapportés, **non comptés**. **Mesure** : s(a, b) = nombre de structures partagées de type objet mathématique ou méthode (exactement ce que calcule `indicateurs_meta`).
- Raison : la liste D du texte I ne compte que trois jeux, et D1 sert à presque toutes les fiches : un jeu de données partagé ne dit rien ; de même les protocoles imposés par le texte I. La réponse 2 v2 demande de pondérer par la rareté (« une équation de diffusion partagée dit peu ») : à défaut de poids, je retire les structures quasi universelles. Les éléments imposés par le texte I à toutes les fiches (plancher apparié, sonde nulle, trois jeux disjoints) ne figurent pas dans la liste, pour la même raison.
- Alternatives : (b) au moins 2 structures partagées — avantage : profil plus strict ; inconvénient : avec 2 à 4 structures par fiche, le profil devient vide sur la plupart des lots (P14 tomberait sous la médiane 1 à 10 fiches) ; (c) compter les jeux de données — avantage : conforme à la liste de R-638, qui nomme le jeu de données ; inconvénient : profil rempli par D1 seul (démontré sur le jeu d'essai : paire e09–e10).
- Confiance : 0,5 (liste) ; 0,55 (seuil 1, types comptés).
- **Écart déclaré à R-638** : R-638 nomme « objet mathématique, méthode, jeu de données » ; je propose de lire le jeu de données sans le compter, pour la raison ci-dessus. C'est une lecture à confirmer par Lazar.
- **Compatibilité v53 (option A, recommandée)** : le code ne connaît que des « types » et accepte n'importe quel nom ; une structure partagée exige l'égalité exacte du couple (type, nom). Je propose donc de servir **chaque structure nommée comme un « type »** (`types_structure` = les 20 identifiants) et d'imposer dans la consigne du lecteur que le nom **recopie l'identifiant**. Le code v53 ne vérifie pas cette égalité : un nom différent passerait en silence et ferait baisser s (vérifié sur le code : `{"type": "me_test_sequentiel_cusum", "nom": "CUSUM"}` est accepté). D'où l'incompatibilité I-1 et la demande d'un contrôle en v54.

## 4. Désaccord, lu à part (M9, L3, garde R5 ligne 24)

**Proposition (À GELER par Lazar).**
- **Quand** : **après** le calcul et le scellement des trois paires (fin d'É7b), jamais avant ; la sélection est donc faite sans lui, par construction.
- **Sur quoi** : la paire méta retenue et, au plus, les quatre paires suivantes du classement méta (dans le profil d'abord, hors profil ensuite) — cinq paires au plus.
- **Par qui** : les deux lecteurs de niches, dans un appel séparé par paire, qui reçoivent seulement le champ « hypothèse » (affirmation centrale) des deux fiches, anonymes, passeport d'aiguillage exigé, garde A4 ; réponse fermée `oui` / `non` / `indécidable` (« les deux affirmations se contredisent-elles ? »). Accord des deux rapporté ; aucun seuil.
- **Journal** : fichier scellé `desaccord-paires.json` (clé de paire, deux réponses, horodatage postérieur à celui du scellement des paires), déposé au coffre, ouvert après É9 comme les autres verdicts (A21).
- **Garde qu'il n'entre pas dans le score** : la fonction de score ne reçoit pas d ; `garde_desaccord_hors_score` (code v53) l'éprouve à É0 par la signature de la fonction. Essai R5 : **cas sain** = la même paire avec d = oui puis d = non reçoit le même score ; **artefact** = une fonction de score d'essai qui accepte un argument `desaccord` et en dépend → `BisociationRefusee`, arrêt. Essai ajouté : **artefact d'ordre** = un journal de désaccord horodaté avant le scellement des paires → arrêt (le désaccord aurait pu influencer la sélection).
- Raison : un lecteur qui lit une fiche par appel ne peut pas juger qu'elle contredit une autre fiche ; la lecture par paire est la seule qui ait un sens, et la faire après la sélection rend la garde vraie par construction, en plus de la garde par signature. Coût : 10 lectures courtes au plus, ≈ 0,1 USD (SUPPOSÉ, au prorata de 0,25 USD par lecture et par dix fiches).
- Alternative : champ « affirmation centrale » recopié par fiche (brouillon 7) et désaccord jugé plus tard par programme — avantage : aucun appel de plus ; inconvénient : un programme ne sait pas dire si deux énoncés se contredisent.
- Confiance : 0,7.
- **Le code v53 ne lit pas le désaccord** (manifeste de fin : « non lu en v53 ») : incompatibilité I-2.

## 5. Bande d'éloignement non extrême (S29 d)

**Mesure (À GELER par Lazar).** e(n_a, n_b) = **distance de contenu** entre les deux niches (objets étudiés et vocabulaire), échelle 1 à 5 (1 : objets et vocabulaire quasi identiques ; 5 : aucun objet ni vocabulaire communs), table à la main, SUPPOSÉ. Elle est **distincte du canal** (section 2) : deux niches peuvent parler peu et étudier presque la même chose (n1–n4 : c = 1, e = 3), ou beaucoup et des choses différentes.

| e (contenu) | n2 activations | n3 anomalies | n4 moniteurs | n5 bornes | n6 évaluation |
|---|---|---|---|---|---|
| **n1 séquentiel** | 3 | 2 | 3 | 2 | 3 |
| **n2 activations** | — | 2 | 3 | 5 | 3 |
| **n3 anomalies** | | — | 3 | 3 | 3 |
| **n4 moniteurs** | | | — | 4 | 2 |
| **n5 bornes** | | | | — | 4 |

**Bande proposée (À GELER par Lazar) : [e_min ; e_max] = [2 ; 3].** Avec c ≤ 1, **4 paires de niches sur 15** sont dans le profil (aux structures près) : n1–n2, n1–n4, n1–n6, n3–n4 ; 3 paires à canal faible en sont exclues parce qu'extrêmes (n2–n5 : e = 5 ; n4–n5 et n5–n6 : e = 4). La bande et le seuil se recoupent (exigence de non-vacuité, M9).

**Lien avec la cloche d'Uzzi.**
- **Vérifié sur PDF** (`uzzi-mukherjee-stringer-jones-2013-science.pdf`, `532970985650…`) : succès = article dans les 5 % les plus cités à 8 ans (p. 469) ; « peak impact occurred in the 85th to 95th percentile of median conventionality, an exceptionally high level » (p. 471, texte) et, en légende de la figure 4, l'impact croît avec la conventionnalité médiane « up to the 85th to 95th percentile of median conventionality, after which the relationship reverses » (p. 471). La conventionnalité est mesurée par le z-score des paires de revues citées ensemble contre un modèle nul (p. 469).
- **SUPPOSÉ (transposition)** : Uzzi mesure la conventionnalité des **combinaisons de références d'un article**, pas la distance entre deux niches d'une paire de fiches. Ce que j'en retiens, comme forme et non comme chiffre : l'optimum n'est pas à l'extrême ; il est du côté du familier avec une pointe d'atypique. D'où une bande qui exclut le plus lointain (4 et 5) et le quasi identique (1), et qui penche vers le proche (2 et 3 sur 5). **Aucun chiffre d'Uzzi n'est transposé** : 85e–95e percentile n'a pas d'équivalent sur une échelle à cinq crans entre six niches.
- Concordances non vérifiées ici : Yegros-Yegros 2015 (U inversé sur la disparité) et Dunbar (analogies locales ou régionales) vont dans le même sens (revue v1, SUPPOSÉ) ; Shi-Evans 2023 trouve au contraire une relation monotone (revue v1, page en ligne) : la cloche n'est pas acquise.
- Alternatives : (b) [2 ; 4] — avantage : 6 paires de niches sur 15 dans le profil, P14 un peu moins vide (zéro avec 0,20 au lieu de 0,25 à 10 fiches, section 6) ; inconvénient : admet n4–n5 et n5–n6, qui sont presque l'extrême de l'échelle ; (c) aucune bande (indicateur toujours vrai) — avantage : un paramètre de moins ; inconvénient : contraire à R-638 (« éloignement non extrême »).
- Confiance : 0,4 pour la table ; 0,45 pour la bande.

## 6. Forme et poids du score ; repli ; non-vacuité ; prédiction P14 (S29 e, f)

**Forme (À GELER par Lazar ; forme écrite au brouillon 7 et codée dans `score_meta`).** score méta(a, b) = 1[c ≤ 1] × 1[s ≥ 1] × 1[2 ≤ e ≤ 3] × (1 + **poids** × s), **poids = 0,5** ; paire méta = argmax ; égalités par la clé tirée `bisoc-meta` (SeedSequence, R9).
- Raison du poids : dans le profil, préférer la paire qui partage le plus de structures (2 structures : 2,0 ; 1 structure : 1,5) sans que le poids puisse faire entrer une paire hors profil.
- Alternative : poids 0 (indicateurs seuls, égalités au tirage) — avantage : aucun choix de poids ; inconvénient : une paire à trois structures communes ne bat pas une paire à une.
- Confiance : 0,5.
- **Contrainte à écrire** : poids ≥ 0. Le code ne le vérifie pas : un poids négatif rendrait des paires du profil « hors profil » (vérifié : `poids = -2` est accepté par `lire_annexe_meta`) ; incompatibilité I-6.

**Règle de repli hors profil (S29 f ; À GELER par Lazar).** **`indicateurs_puis_structure`**, la seule que le code admet (`REPLIS_CONNUS = ("indicateurs_puis_structure",)` ; toute autre est refusée à É0, A20). Lecture : quand aucune paire ne satisfait les trois indicateurs, la paire retenue est celle qui en satisfait le plus, puis qui partage le plus de structures (`score_repli` = (nombre d'indicateurs vrais, s)), égalités au tirage ; elle est comptée « hors profil » (P14 : réserve « seul le repli éprouvé »). Le code ordonne toujours une paire du profil avant toute paire hors profil (clés (1, score) contre (0, …)).
- Alternative : aucune dans le code v53 ; « distance au profil pondérée » demanderait une v54.
- Confiance : 0,8 (seule option ; la vraie question est de savoir si un repli doit exister, ce que le brouillon 7 tranche par oui).

**Non-vacuité au gel (garde 22a ; exigée par M9).** Jeu d'essai synthétique de 10 fiches étiquetées à la main par moi (aucune fiche réelle), les deux lecteurs supposés d'accord :

```json
{"jeu_essai_non_vacuite": {
  "e01": {"niche": "n1_detection_sequentielle", "structures": ["om_somme_cumulee_temps_arret", "me_test_sequentiel_cusum"]},
  "e02": {"niche": "n2_lecture_activations", "structures": ["om_direction_sous_espace", "om_somme_cumulee_temps_arret", "me_intervention_activations"]},
  "e03": {"niche": "n4_moniteurs_et_protocoles", "structures": ["me_moniteur_par_modele", "om_martingale_e_processus", "me_test_sequentiel_cusum"]},
  "e04": {"niche": "n6_science_evaluation", "structures": ["jd_simulateur_fige", "pr_exclusion_famille", "om_somme_cumulee_temps_arret", "me_test_sequentiel_cusum"]},
  "e05": {"niche": "n5_bornes_et_theorie", "structures": ["om_rapport_vraisemblance_divergence", "om_somme_cumulee_temps_arret", "me_preuve_formelle"]},
  "e06": {"niche": "n2_lecture_activations", "structures": ["om_rapport_vraisemblance_divergence", "om_covariance_mahalanobis"]},
  "e07": {"niche": "n3_anomalies_hors_distribution", "structures": ["om_covariance_mahalanobis", "me_seuil_conforme"]},
  "e08": {"niche": "n4_moniteurs_et_protocoles", "structures": ["me_moniteur_par_modele", "pr_audit_budgete"]},
  "e09": {"niche": "n1_detection_sequentielle", "structures": ["me_test_sequentiel_cusum", "jd_simulateur_fige"]},
  "e10": {"niche": "n6_science_evaluation", "structures": ["jd_simulateur_fige", "pr_exclusion_famille"]}
}}
```

Résultat, calculé avec les fonctions réelles de `bisociateur_v53.py` (`valider_niche`, `indicateurs_meta`, `score_meta`, `score_repli`), selon la logique de `course2_v53._notes` : **5 paires dans le profil, 36 hors profil, 4 refusées (même niche)** ; argmax **e01–e04, score 2,0** (deux structures partagées) ; autres paires du profil à 1,5 (e01–e02, e01–e03, e03–e09, e04–e09). Témoins hors profil, chacun pour une seule raison : e01–e05 (canal fort, c = 3) ; e05–e06 (extrême, e = 5) ; e07–e08 (aucune structure partagée) ; e09–e10 (seuls un jeu de données et un protocole partagés : non comptés). Meilleur hors profil (repli) : (2 indicateurs, s = 1). Garde 24 passée ; paire de même niche refusée par `indicateurs_meta` (garde 22a, artefact). **Le profil n'est pas vide et n'est pas tout** : la condition de scellement de M9 est remplie sur ce jeu. Ce calcul est à rejouer par le contre-lecteur et à verser comme script empreinté au scellement (garde 22a).

**Prédiction P14 refaite avec ces paramètres (garde 22a ; indicative).** Hypothèses, toutes SUPPOSÉ : loi a priori des niches des fiches de défense (axes 1 à 5) n1 0,30, n2 0,25, n3 0,15, n4 0,10, n5 0,15, n6 0,05 ; accord des deux lecteurs par fiche 0,7 (cohérent avec un kappa d'environ 0,5) ou 0,9 ; probabilité qu'une paire de fiches partage au moins une structure comptée 0,15, 0,3 ou 0,5 ; indépendances. Sortie (`b2a0a325…`) :

| Fiches non aiguillées | Accord par fiche | Structure partagée | Médiane des paires dans le profil | P(zéro dans le profil) | P(aucune paire éligible : bras non produit) |
|---|---|---|---|---|---|
| 6 | 0,7 | 0,3 | 0 | 0,59 | 0,039 |
| 6 | 0,9 | 0,3 | 1 | 0,42 | 0,004 |
| 10 | 0,7 | 0,3 | 1 | 0,25 | 0,002 |
| 10 | 0,9 | 0,3 | 3 | 0,10 | 0,000 |
| 10 | 0,7 | 0,15 / 0,5 | 1 / 3 | 0,46 / 0,15 | 0,002 |

**Valeur proposée pour remplacer P14 au gel (À GELER par Lazar)** : paires dans le profil méta, **médiane 0 à 6 fiches (zéro avec 0,59), médiane 1 à 10 fiches (zéro avec 0,25)** ; croyance « hors profil » à la paire retenue : **0,45 [0,15 ; 0,75]** (au lieu de 0,3 [0,05 ; 0,6]) ; « bras non produit (aucune paire éligible) » : 0,04 à 6 fiches, 0,002 à 10. C'est plus pessimiste que le script v6 (zéro 0,31 et 0,03) pour deux raisons : le script v6 tirait la communication par paire de fiches alors qu'elle est une propriété de la paire de niches (4 paires de niches sur 15 seulement passent canal et bande), et il ignorait la règle du code qui écarte une fiche dont les lecteurs se contredisent sur la niche. **Lecture** : au pré-pilote, le bras méta éprouvera souvent son seul repli ; c'est attendu, déclaré, et ne change rien d'autre (critères du brouillon 7, « zéro paire dans le profil »). Variantes (même script, bande ou seuil changés, accord 0,7, structure 0,3) : bande [2 ; 4] → 6 paires de niches sur 15, zéro avec 0,54 (6 fiches) et 0,20 (10 fiches) ; c ≤ 2 → 10 sur 15, zéro 0,35 et 0,07, mais « faible » ne veut plus rien dire.

**Garde 22a — ce qui reste à faire avant le scellement.** Le brouillon 7 exige que « le script soit rejoué » : le script v6 ne sait pas jouer une communication par paire de niches ni la règle d'accord. Je propose qu'un script v7 du calcul de puissance reprenne la fonction ci-dessous (nom de tâche de graine nouveau, `v7-meta-profil-…`) et que sa sortie, empreintée, soit nommée dans la version contre-lue de cette annexe ; la valeur de P14 du préenregistrement est remplacée par elle au gel.

```python
# P14 indicatif, annexe du bras méta v1, brouillon 1 (SUPPOSÉ partout). numpy SeedSequence (R9).
import sys, numpy as np
N_SIM = 100_000
racine = 20261101
sys.path.insert(0, "/home/claude/controle-ia-travail/src")
from controle_ia.manifeste import cle_de_tache
def rng(nom):
    cle = cle_de_tache(nom)
    return np.random.default_rng(np.random.SeedSequence(racine, spawn_key=(cle,)))
niches = ["N1","N2","N3","N4","N5","N6"]
prior = np.array([0.30, 0.25, 0.15, 0.10, 0.15, 0.05])  # SUPPOSÉ : fiches de défense, axes 1 à 5
C = {("N1","N2"):1,("N1","N3"):2,("N1","N4"):1,("N1","N5"):3,("N1","N6"):1,("N2","N3"):2,("N2","N4"):2,("N2","N5"):0,
     ("N2","N6"):2,("N3","N4"):1,("N3","N5"):2,("N3","N6"):2,("N4","N5"):1,("N4","N6"):3,("N5","N6"):1}
E = {("N1","N2"):3,("N1","N3"):2,("N1","N4"):3,("N1","N5"):2,("N1","N6"):3,("N2","N3"):2,("N2","N4"):3,("N2","N5"):5,
     ("N2","N6"):3,("N3","N4"):3,("N3","N5"):3,("N3","N6"):3,("N4","N5"):4,("N4","N6"):2,("N5","N6"):4}
SEUIL_C, BANDE = 1, (2, 3)
prof_np = np.zeros((6,6), bool)
for (a,b),c in C.items():
    i,j = niches.index(a), niches.index(b)
    ok = c <= SEUIL_C and BANDE[0] <= E[(a,b)] <= BANDE[1]
    prof_np[i,j] = prof_np[j,i] = ok
print("paires de niches dans le profil (niches seules) :", int(prof_np.sum()//2), "sur 15")
def jouer(n, p_accord, p_struct, nom):
    g = rng(nom)
    nich = g.choice(6, size=(N_SIM, n), p=prior)
    garde = g.random((N_SIM, n)) < p_accord          # niche retenue si les deux lecteurs s'accordent (code v53, choix 10)
    iu = np.triu_indices(n, 1)
    a, b = nich[:, iu[0]], nich[:, iu[1]]
    elig = garde[:, iu[0]] & garde[:, iu[1]] & (a != b)
    struct = g.random((N_SIM, len(iu[0]))) < p_struct
    prof = elig & prof_np[a, b] & struct
    npf, nel = prof.sum(1), elig.sum(1)
    return np.median(npf), np.mean(npf == 0), np.mean(nel == 0), np.mean((npf == 0) & (nel > 0))
for n in (6, 10):
    for pa in (0.7, 0.9):
        for ps in (0.15, 0.3, 0.5):
            med, z, aucun, repli = jouer(n, pa, ps, f"annexe-b1-p14-{n}-{pa}-{ps}")
            print(f"n={n:2d} accord={pa} structure={ps}: médiane {med:.0f} ; P(zéro dans le profil) {z:.2f} ; "
                  f"P(aucune paire éligible : bras non produit) {aucun:.3f} ; P(repli joué) {repli:.2f}")
print("fin ;", sys.version.split()[0], np.__version__)
```

## 7. Garde-fous de la synthèse transposés au bras méta en course

La synthèse v2 (décision 1) rend six garde-fous obligatoires **sur littérature réelle**. Dans la course, le bras méta ne prédit pas un pont futur : il choisit une paire de fiches à fusionner, dont l'issue est lue par l'aiguilleur, les juges, l'antériorité et les tests de mort. La transposition est donc partielle. Proposition (À GELER par Lazar ; confiance 0,6) :

| Garde-fou | Dès la génération 1 ? | Forme dans la course |
|---|---|---|
| Étiquette de pont indépendante du canal | **oui, sous forme transposée** | l'issue d'une fusion (passage, tests de mort) n'utilise jamais c, e, la niche ni le score méta ; la table c est fixée avant toute fiche et n'est jamais relue sur les fiches |
| Rétrodiction inversée | **non** (littérature réelle) | aucun équivalent sans issue datée ; en génération 1, journal seul : le score méta recalculé sous permutation tirée des niches entre fiches (programme, 0 USD) est rapporté pour la paire retenue (placebo descriptif, aucune lecture décisive) |
| Graphe amputé des ponts | **non** (littérature réelle) | journal seul : paire méta recalculée sans les structures (s retiré) et sans la bande, pour dire quel indicateur a décidé le choix |
| Bras « popularité seule » | **non** comme bras (R-643 a retiré le bras hasard ; R-634 interdit toute comparaison au pré-pilote) | le bras basique sert de comparateur simple dans la course (R-642) ; journal : nombre de structures et de concepts des fiches retenues contre la moyenne du lot (biais vers les fiches riches en étiquettes) |
| Jeux disjoints par niche et par période | **oui, sous forme transposée** | conception et épreuve disjointes : paramètres scellés avant toute fiche (A9, A20) ; aucun ajustement entre générations sans annexe v2 scellée |
| Puissance préalable | **oui** | P14 refaite (section 6) avant le scellement ; dans la course, aucune comparaison méta contre basique n'est lue en génération 1 sans calcul de puissance préenregistré (à 12 fusions, l'erreur-type d'une aire à 6 contre 6 est d'environ 0,2, sortie v6) |

**Les trois défauts relevés au collisionneur, transposés.**
- **Pic de variance** : aucune variance de taux de passage entre niches ou entre générations n'est lue comme signe de criticité ou d'« allumage » ; toute lecture de ce genre exigera la surdispersion entre réplicats ou un nul d'urne à moyenne égale, préenregistrés (synthèse, B ; réponse 3 v2).
- **Sur-additivité** : aucune quantité F = R(A ∪ B) − R(A) − R(B) + R(A ∩ B) n'est calculée sur les fusions de la course (budget et combinatoire la faussent) ; journal seulement.
- **Retour à la moyenne (A0) et étiquette circulaire** : le profil ne lit aucun flux observé sur les fiches ; c est a priori, la niche est lue avant toute issue, le passage n'entre jamais dans la grille ni dans les tables. Une annexe v2 qui recalerait c ou e sur les passages de la génération 1 devra tester la rétrodiction inversée sur les générations suivantes avant toute lecture.

**Grandeurs à journaliser dès la génération 1 (question 7, allumage ; proposition, À GELER par Lazar ; confiance 0,6).** Programme, 0 USD, lu après É9 :
1. par fiche : niche de chaque lecteur, retenue ou non au bras méta, structures de chaque lecteur ;
2. par lot : comptes par niche ; nombre de paires éligibles ; nombre dans le profil ; cause si aucune ; pour **chaque** paire éligible, les trois indicateurs, s, le score et le rang (pas seulement la paire retenue) ;
3. désaccord des paires lues (section 4) ;
4. par fusion : parents, bras, case, génération (déjà au coffre dans `cle-bras`) ;
5. **graphe fiche → fusion → fiche**, cumulé sur les générations : sommets = toutes les fiches ; arêtes = parent → fusion, et héritage (« affine X », « réfute X » du texte I) de g vers g + 1 ; par génération : **part des sommets dans la plus grande composante faiblement connexe** (composante géante, Bettencourt et Kaiser 2015, p. 3, vérifié par la réponse 3 v2 : transition topologique d'un réseau de coauteurs, analogie seulement), nombre de composantes, **profondeur de la plus longue cascade de fusions** (fusion dont un parent est une fusion ou hérite d'une fusion), **nombre moyen de descendants d'une fusion en g + 1** (rapport de branchement ; « R₀ de la lignée » d'Argon, analogie) ;
6. passages par bras, comptés, sans comparaison au pré-pilote.

**Valeurs attendues en génération 1, déclarées d'avance** : profondeur de cascade ≤ 1 **par construction** (les fusions ne prennent que des fiches de passe 1 ; aucune fusion de fusions dans une génération) ; à k = 1, au plus 6 parents par case : composante géante triviale. Ce sont des lignes de base, non des résultats ; tout énoncé d'« allumage » attend la génération 2 et un préenregistrement (R-642).

## 8. Format lisible par le code

**Contrat de `bisociateur_v53.lire_annexe_meta` (vérifié sur le code).** Le fichier doit : exister ; avoir un compagnon `.sha256` conforme (`verifier_scelle`) ; avoir l'empreinte injectée dans la configuration (`bisociateur.meta.annexe.sha256`) ; contenir un bloc JSON clôturé dont le **dernier** objet portant la clé `parametres_bras_meta` est lu (`extraire_bloc_json`) ; ce bloc doit porter les onze clés `niches`, `types_structure`, `communication`, `seuil_communication_faible`, `structure_forte` {`nombre_min` entier, `types` liste}, `eloignement`, `bande` [min, max], `poids`, `repli` (∈ `indicateurs_puis_structure`), `contre_lecture`, `approbation_lazar` (chaînes non vides, sans le marqueur « À REMPLIR ») ; au moins deux niches ; `communication` et `eloignement` définis pour **chaque** paire de niches, clé = les deux identifiants **triés** joints par « | ». Les clés de plus (version, statut, S28, règles) sont ignorées par v53 : elles sont là pour la lecture humaine et pour le code d'analyse (incompatibilité I-3).

**Épreuve faite sur ce bloc** (copie hors dépôt, compagnon d'essai) : avec les deux champs à « À REMPLIR », `lire_annexe_meta` refuse (« A20 : annexe sans contre_lecture déclarée ») ; avec les deux champs remplis d'un texte d'essai, il accepte, et `garde_desaccord_hors_score` passe.

**Bloc de configuration de l'annexe (toutes les valeurs À GELER par Lazar ; empreinte de l'annexe à poser au scellement, jamais dans l'annexe elle-même).** C'est le seul bloc du fichier qui porte la clé `parametres_bras_meta`, et il est le dernier bloc JSON du fichier.

Configuration à écrire au gel, côté orchestrateur (fragment ; l'empreinte invalide ci-dessous fait refuser la configuration par `configuration_v53` tant qu'elle n'est pas posée) :

```json
{"bisociateur": {"bras": ["meta", "gu_krenn", "basique"], "k_paires": 1, "meta": {"annexe": {"chemin": "brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/annexe-bras-meta-v1.md", "sha256": "À FOURNIR AU SCELLEMENT"}}}}
```

Paramètres du bras méta, version 1 :

```json
{"parametres_bras_meta": {
  "version": "annexe-bras-meta-v1, brouillon 1",
  "statut": "brouillon 1, non scellé ; valeurs proposées, aucune gelée ; contre-lecture à faire",
  "valeurs_a_geler_par_lazar": true,
  "echelle_communication": "0 à 3 (0 aucun échange connu ; 3 même communauté), table écrite à la main, SUPPOSÉ",
  "echelle_eloignement": "1 à 5 (1 objets et vocabulaire quasi identiques ; 5 sans objet ni vocabulaire communs), table écrite à la main, SUPPOSÉ",
  "structures_nom_impose": "le nom de chaque structure recopie son identifiant (option A, compatible v53 ; contrôle par le code : v54)",
  "structures_lues_non_comptees": ["jd_simulateur_fige", "jd_donnees_publiques", "jd_notations_juges", "pr_exclusion_famille", "pr_audit_budgete", "pr_reechantillonnage_report"],
  "regle_niche": "une niche par fiche ; fiche retenue au bras méta seulement si les deux lecteurs posent la même niche (code v53)",
  "accord_min_niche_kappa": 0.4,
  "accord_min_structures_jaccard": 0.3,
  "desaccord": "lu à part, par paire, après le choix des paires ; n'entre jamais dans le score (R-638 ; garde R5 ligne 24)",
  "niches": ["n1_detection_sequentielle", "n2_lecture_activations", "n3_anomalies_hors_distribution", "n4_moniteurs_et_protocoles", "n5_bornes_et_theorie", "n6_science_evaluation"],
  "types_structure": ["om_martingale_e_processus", "om_rapport_vraisemblance_divergence", "om_covariance_mahalanobis", "om_direction_sous_espace", "om_somme_cumulee_temps_arret", "om_jeu_minimax", "om_graphe_causal", "me_test_sequentiel_cusum", "me_seuil_conforme", "me_dictionnaire_parcimonieux", "me_intervention_activations", "me_moniteur_par_modele", "me_estimation_densite", "me_preuve_formelle", "jd_simulateur_fige", "jd_donnees_publiques", "jd_notations_juges", "pr_exclusion_famille", "pr_audit_budgete", "pr_reechantillonnage_report"],
  "communication": {"n1_detection_sequentielle|n2_lecture_activations": 1, "n1_detection_sequentielle|n3_anomalies_hors_distribution": 2, "n1_detection_sequentielle|n4_moniteurs_et_protocoles": 1, "n1_detection_sequentielle|n5_bornes_et_theorie": 3, "n1_detection_sequentielle|n6_science_evaluation": 1, "n2_lecture_activations|n3_anomalies_hors_distribution": 2, "n2_lecture_activations|n4_moniteurs_et_protocoles": 2, "n2_lecture_activations|n5_bornes_et_theorie": 0, "n2_lecture_activations|n6_science_evaluation": 2, "n3_anomalies_hors_distribution|n4_moniteurs_et_protocoles": 1, "n3_anomalies_hors_distribution|n5_bornes_et_theorie": 2, "n3_anomalies_hors_distribution|n6_science_evaluation": 2, "n4_moniteurs_et_protocoles|n5_bornes_et_theorie": 1, "n4_moniteurs_et_protocoles|n6_science_evaluation": 3, "n5_bornes_et_theorie|n6_science_evaluation": 1},
  "seuil_communication_faible": 1,
  "structure_forte": {"nombre_min": 1, "types": ["om_martingale_e_processus", "om_rapport_vraisemblance_divergence", "om_covariance_mahalanobis", "om_direction_sous_espace", "om_somme_cumulee_temps_arret", "om_jeu_minimax", "om_graphe_causal", "me_test_sequentiel_cusum", "me_seuil_conforme", "me_dictionnaire_parcimonieux", "me_intervention_activations", "me_moniteur_par_modele", "me_estimation_densite", "me_preuve_formelle"]},
  "eloignement": {"n1_detection_sequentielle|n2_lecture_activations": 3, "n1_detection_sequentielle|n3_anomalies_hors_distribution": 2, "n1_detection_sequentielle|n4_moniteurs_et_protocoles": 3, "n1_detection_sequentielle|n5_bornes_et_theorie": 2, "n1_detection_sequentielle|n6_science_evaluation": 3, "n2_lecture_activations|n3_anomalies_hors_distribution": 2, "n2_lecture_activations|n4_moniteurs_et_protocoles": 3, "n2_lecture_activations|n5_bornes_et_theorie": 5, "n2_lecture_activations|n6_science_evaluation": 3, "n3_anomalies_hors_distribution|n4_moniteurs_et_protocoles": 3, "n3_anomalies_hors_distribution|n5_bornes_et_theorie": 3, "n3_anomalies_hors_distribution|n6_science_evaluation": 3, "n4_moniteurs_et_protocoles|n5_bornes_et_theorie": 4, "n4_moniteurs_et_protocoles|n6_science_evaluation": 2, "n5_bornes_et_theorie|n6_science_evaluation": 4},
  "bande": [2, 3],
  "poids": 0.5,
  "repli": "indicateurs_puis_structure",
  "contre_lecture": "À REMPLIR",
  "approbation_lazar": "À REMPLIR"
}}
```

## 9. Procédure jusqu'à É0

1. **Vérifier DEP10** : verdicts des collisionneurs des questions 4 à 7 rendus et scellés ; sinon, la contre-lecture attend (R-638 : spécification après les verdicts).
2. **Contre-lecture (R2)** par un sous-agent neuf d'un **modèle différent de l'auteur** (Sonnet 5.5 ou Fable 5.1 ; pas Opus), qui n'a écrit ni le préenregistrement ni aucune pièce lue ici. Pièces à lui donner explicitement : ce brouillon et son empreinte ; le préenregistrement brouillon 7 ; `bisociateur_v53.py`, `course2_v53.py`, `configuration_v53.py`, `outils.py`, `essais/aides_v53.py` ; la synthèse v2 ; le PDF d'Uzzi (p. 469, 471) ; le texte I (glossaire, axes, annexe 1). Points à examiner : (a) chaque valeur a-t-elle raison, alternative, confiance ; (b) le bloc passe-t-il `lire_annexe_meta` une fois les deux champs remplis, et le refuse-t-il avant ; (c) le jeu d'essai donne-t-il bien 5 / 36 / 4 et l'argmax e01–e04 (rejeu) ; (d) le script P14 rejoué donne-t-il la même sortie ; (e) la transposition d'Uzzi est-elle bien marquée SUPPOSÉ et le chiffre bien lu p. 471 ; (f) les incompatibilités I-1 à I-10 sont-elles exactes et complètes ; (g) l'écart à R-638 sur les jeux de données est-il acceptable.
3. **Brouillon 2** : traitement de chaque constat, une ligne par constat.
4. **Mot de Lazar** sur chaque valeur de la table récapitulative (section 11), y compris S28, la règle « une seule niche » et l'écart à R-638 ; consigné dans `registres/decisions.md`. Aucune valeur ne prend de défaut à 48 heures : une annexe de préenregistrement se gèle sur un mot.
5. **Version à sceller** `annexe-bras-meta-v1.md` : brouillon contre-lu, valeurs approuvées écrites, statut changé, et les deux champs remplis — `contre_lecture` : modèle, date, empreinte du brouillon relu, chemin et empreinte du rapport ; `approbation_lazar` : numéro de décision et date. Ces seuls changements après contre-lecture sont vérifiés par programme (différence limitée à ces lignes) ; sinon nouvelle contre-lecture.
6. **Scellement** : `python -m controle_ia.scellement sceller annexe-bras-meta-v1.md` (compagnon `.sha256`, R6) ; script P14 v7 et sa sortie versés et empreintés ; jeu d'essai de la garde 22a versé comme script d'essai empreinté.
7. **Empreinte injectée** : dans l'en-tête du préenregistrement (valeur « à fournir au scellement ») **avant son gel**, et dans `bisociateur.meta.annexe.sha256` de la configuration ; la consigne figée du lecteur d'étiquettes recopie la section 1 et la liste de la section 3 (empreinte du passage vérifiée par programme).
8. **É0** : `declarer_bras` lit l'annexe ; gardes 22b, 23, 24 jouées sur cas sain et artefact (R5). **A20 : sans annexe scellée, contre-lue, approuvée, à la bonne empreinte, le bras méta n'est pas lancé** (« non produit (annexe non conforme) », écrit au manifeste à É0, aucun paramètre choisi en route) ; les deux autres bras sont inchangés.

## 10. Incompatibilités entre le brouillon 7 et le code v53

| N° | Brouillon 7 | Code v53 | Effet | Proposition |
|---|---|---|---|---|
| **I-1** | structures « nommées dans la grille » ; garde 23 : « structure hors grille : rejetée » | `valider_niche` ne contrôle que le type ; le nom est libre ; s exige l'égalité exacte (type, nom) | un lecteur qui nomme autrement la même structure fait baisser s **en silence** (vérifié) ; contraire à R5 (aucun repli silencieux) | option A (structures nommées servies comme « types ») + **v54** : refus d'un nom différent de l'identifiant quand l'annexe le demande, compté et journalisé ; **à faire avant É0** |
| **I-2** | désaccord lu pour chaque paire candidate, rapporté | « non lu en v53 » ; le champ « affirmation centrale » n'est pas gardé par `valider_niche` | M9 incomplète ; journal du désaccord absent | **v54** : lecture par paire après la sélection (section 4), fichier scellé au coffre ; **à faire avant É0** si L3 est gelée telle quelle |
| **I-3** | S28 (kappa, Jaccard) lu au verdict | `kappa_niches` et `accord_jaccard` existent mais ne sont appelés nulle part ; aucune clé de configuration pour S28 | S28 n'est calculé que par un code d'analyse qui n'existe pas encore | écrire l'appel dans le code d'analyse (commit nommé au scellement) ; les clés `accord_min_*` du bloc servent de source |
| **I-4** | lecteurs à « grille fermée » (définitions) | le lecteur ne reçoit que les identifiants `{niches, types_structure}` | sans les définitions dans la consigne, la grille n'est pas fermée en pratique | consigne figée du lecteur = recopie mot pour mot des sections 1 et 3 ; empreinte du passage vérifiée |
| **I-5** | niche lue par lecteur ; rien sur le désaccord des lecteurs par fiche | fiche écartée du bras méta si les deux lecteurs diffèrent sur sa niche (choix de code 10, « à confirmer ») | n effectif réduit (pris en compte dans P14) ; règle non écrite au préenregistrement | geler la règle en mots (section 1) et l'écrire dans M9 de la version gelée |
| **I-6** | poids « dans l'annexe » | `poids`, `seuil_communication_faible`, valeurs des tables et bornes de la bande ne sont pas contrôlés en type ni en signe (vérifié : poids −2 et seuil textuel acceptés) | une annexe fautive passerait A20 et fausserait le profil | v54 : contrôles de type et poids ≥ 0 ; d'ici là, contrôle par la contre-lecture et un essai R5 ajouté (artefact : poids négatif) |
| **I-7** | bras méta non produit : seulement « annexe non conforme » (cas i) ; C12 compte 0,03 pour le méta | `choisir_paires` déclare aussi « non produit (aucune paire notable) » quand aucune paire de niches différentes n'est éligible | cause de C12 non comptée : ≈ 0,04 à 6 fiches, 0,002 à 10 (P14 refaite) | ajouter le cas (v) « niches indistinctes ou aucune paire éligible » à la table M9, à C12 et à O15 dans la version gelée ; rejouer C12 |
| **I-8** | n = 2 : « paire au bras de priorité 1 » | « au premier bras qui peut la noter » (choix de code 9) ; le méta ne peut pas noter deux fiches de même niche ou disputée | la paire peut passer au bras suivant | lecture à écrire au préenregistrement (déjà signalée par le LISEZMOI) |
| **I-9** | annexe « contre-lue, approuvée » vérifiée à É0 | le code ne vérifie que la présence d'une chaîne sans le marqueur « À REMPLIR » dans `contre_lecture` et `approbation_lazar` | une chaîne quelconque (par exemple un autre mot de remplissage) passerait | au scellement, recherche de texte : les deux champs citent une empreinte de 64 caractères et un numéro de décision ; v54 possible (forme exigée) |
| **I-10** | la non-vacuité (22a) est une condition du scellement | aucune vérification à É0 | aucun effet si la procédure est suivie | le jeu d'essai est versé comme script empreinté et rejoué en É0 avec la garde 22b |

**Faits constatés hors de l'annexe (R11).** Le brouillon 7 écrit « aucun PDF versé » pour Gu et Krenn 2024 et pour Uzzi 2013 (documents qui font foi). Sur cette branche, `docs/sources/pdf/bisociation-fertilite-v1/` contient `arxiv-2402.08640-gu-krenn-2024.pdf` et `uzzi-mukherjee-stringer-jones-2013-science.pdf`, compagnons conformes (`sha256sum -c` : OK), datés du 31 octobre à 02:18, après la rédaction du brouillon 7 (01:00). La version gelée du préenregistrement doit le dire, et R7 peut désormais être satisfaite pour les traits de Gu et Krenn qui fondent S31.

## 11. Table récapitulative (toutes À GELER par Lazar)

| Paramètre | Valeur proposée | Alternative | Confiance |
|---|---|---|---|
| S29 a — grille des niches | 6 niches (n1 séquentiel, n2 activations, n3 anomalies, n4 moniteurs et protocoles, n5 bornes et théorie, n6 science de l'évaluation), niche = méthode de l'affirmation centrale | 4 niches ; carte des chapelles quand elle existera | 0,45 |
| Règle de lecture | deux lecteurs neufs, une niche forcée par fiche, fiche retenue si les deux s'accordent, structures en union | niche du premier lecteur seul | 0,6 |
| S28 | kappa ≥ 0,40 ; Jaccard structures ≥ 0,30 ; marges constantes 1/0 « dégénérée » | 0,50 ; 0,40 | 0,4 |
| Une seule niche sur le lot | « non produit (niches indistinctes) », compté dans C12, O15, réserve | traiter comme échec de grille (nœud) | 0,55 |
| S29 b — communication | table du canal 0–3 à la main ; faible = c ≤ 1 | moisson OpenAlex (flux observé contre attendu) ; deux tables indépendantes | 0,45 (table) ; 0,5 (seuil) |
| S29 c — structures | 20 structures nommées, 4 types ; forte = ≥ 1 partagée parmi objets mathématiques et méthodes ; jeux de données et protocoles non comptés | ≥ 2 ; compter les jeux de données | 0,5 ; 0,55 |
| Désaccord | lu par paire après la sélection, 5 paires au plus, journal scellé, hors score | champ par fiche et jugement par programme | 0,7 |
| S29 d — éloignement | table de contenu 1–5 ; bande [2 ; 3] | [2 ; 4] ; aucune bande | 0,4 (table) ; 0,45 (bande) |
| S29 e — score | indicateurs × (1 + 0,5 × s), poids ≥ 0 | poids 0 | 0,5 |
| S29 f — repli | `indicateurs_puis_structure` (seul admis) | aucune en v53 | 0,8 |
| P14 refaite | médiane 0 (6 fiches, zéro 0,59) ; 1 (10 fiches, zéro 0,25) ; hors profil 0,45 [0,15 ; 0,75] | valeurs fictives du script v6 | indicative |
| Garde-fous | trois dès la génération 1 (issue indépendante du profil, disjonction conception/épreuve, puissance) ; trois en journal seul | les six reportés à la littérature réelle | 0,6 |
| Journal d'allumage | six grandeurs (section 7), lignes de base en génération 1 | journal de la seule paire retenue (v53) | 0,6 |
