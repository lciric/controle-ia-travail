## (a) Réponses aux critiques visant D

**Périmètre.** Les entrées `R*_input_*.json`, `R6_descriptive_counts.json`, le code, les générations complètes et les pages des mentors restent absents de la transmission ; je n’en invente pas le contenu. Les affirmations des README restent **RAPPORTÉES**, les lectures directes des fichiers transmis **OBSERVÉES-NON-AUDITÉES**, et les plans ci-dessous sont des **HYPOTHÈSES**. Aucun résultat n’est élevé à **VÉRIFIÉ**. Aucune puissance chiffrée n’est prétendue calculée.

### Objections transversales

- **Fuite lexicale — acceptée (A, B, C, E).** Les motifs inspirés des 24 réponses ne peuvent plus être évalués sur les mêmes items comme s’ils étaient indépendants. Toute grille sera figée sur les six items échantillonnés, puis évaluée sans eux, ou de préférence sur des items R4 réservés. L’aveuglement à la condition ne sera pas affirmé : les annotateurs estimeront aussi leur taux de devinette de la condition.
- **Dérive de l’alias et effets de lot — acceptée (A, B, E).** Toute nouvelle lecture comportera doublons exacts intercalés, conditions mélangées et ordre randomisé dans un même lot. Une comparaison avec les notes anciennes mesurera dérive + bruit, jamais le bruit seul.
- **Seuils et rapports — acceptée (A, B, C, E).** Un changement de C1/C2 ne sera plus un critère substantiel primaire. Les contrastes utiliseront une marge \(\varepsilon\), fixée avant les données confirmatoires. Un intervalle traversant \(\varepsilon\) sera **non concluant**, pas une troisième issue mécaniste. \(\hat c\) ne sera interprété que lorsque la précision de \(\hat g\) satisfait un critère préenregistré.
- **Puissance — acceptée.** Elle sera simulée avant tout `GO_`, à partir des notes appariées et des variances d’items publiques. Un plan dont la zone d’indécision absorbe l’effet recherché ne sera pas exécuté.

### Réponses idée par idée

| Idée | Décision et raison | Correction |
|---|---|---|
| **D1 — relecture du juge** | **Acceptée.** Alias, lot et seuils étaient confondus ; près de \(g=0\), l’instabilité de \(\hat c\) est triviale. J’accepte aussi que les désaccords neutres déjà **RAPPORTÉS** dans R6 rendent peu motivée l’hypothèse « les déplacements de dose de R6 sont du bruit ». | Transformée en **test d’équivalence de stabilité de mesure**, non en explication privilégiée de R6. Les répétitions R6 existantes seront exploitées avant toute dépense. |
| **D2 — marqueurs de surface** | **Acceptée.** Les annotations post-traitement peuvent être une fonction de la note ; leur pouvoir prédictif ne démontre ni médiation ni causalité. | Rétrogradée en validation d’instrument. Le résultat causal est retiré. Une éventuelle analyse prédictive exigera items réservés et référence humaine indépendante. |
| **D3 — ouverture contre reste** | **Acceptée.** Les deux localisations pures n’étaient pas exclusives, et une phrase isolée peut sortir du format attendu par le juge. | Segmentation par **fonction**, éditions conservant explicitement le verdict, et contraste continu : le reste apporte-t-il une contribution matérielle au-delà de l’ouverture ? |
| **D4 — auto-relecture par Llama** | **Acceptée (A, B, C, E).** Llama lisant sa prose devient un lecteur supplémentaire ; même une calibration réussie ne distingue pas croyance du générateur et capacité de lecture. | **Retirée comme duel décisif.** Une cartographie croisée Llama/Qwen, textes propres/autrui, pourra être descriptive, sans conclusion sur une dissociation interne. |
| **D5 — calibration des lecteurs** | **Acceptée.** Une transformation affine commune laisse \(g\) invariant ; elle ne peut expliquer les écarts de gains. L’atténuation et l’extrapolation hors support neutralisaient le plan initial. | Question limitée à la **transportabilité de \(\hat c\)** : calibration avec erreurs de mesure, items disjoints, support couvrant les cibles, et contrôle neutre(c2a)→neutre(c2b). |
| **D6 — variance neutre et capture** | **Acceptée.** Moyenne, variance et déplacement partageaient des tirages ; sur une échelle bornée, la variance peut être un polynôme déguisé de \(p_0\). Un \(g_i\) par item n’est pas directement identifié. `Q_GAIN` est déjà **OBSERVÉ-NON-AUDITÉ** dans `c2b_results.json`, mais sa définition n’est pas fournie. | Mesures disjointes, rivaux explicites en \(p_0\), nul borné simulé et validation gelée hors corpus. Je retire « réfuter le paramètre central \(g\) » : seule la suffisance transportable d’un \(g\) constant serait testée. |
| **D7 — géométrie bornée** | **Acceptée en grande partie.** Un nul conservant moyenne et variance peut absorber précisément l’effet à expliquer ; plusieurs lois partagent ces deux moments. **Nuance :** les descentes sous éloge **RAPPORTÉES** ne réfutent pas toute géométrie bornée, seulement certaines explications de plafond pour les items concernés. | Plus de duel autonome. Les modèles bornés deviennent des rivaux paramétrés de D6, avec placebo neutre–neutre et validation hors items. |
| **D8 — formulation ou intensité** | **Acceptée.** L’unité de généralisation est la formulation, pas seulement l’item ; de nouveaux lots non synchronisés confondraient formulation et dérive du juge. | Plusieurs paraphrases par intensité, formulations réservées, prétest humain séparé et conditions contemporaines dans le même lot de lecture. |
| **D9 — pression sociale ou ancrage** | **Acceptée (E).** Les deux mécanismes peuvent coexister. | Le contraste portera sur l’**incrément social**, après appariement du contenu évaluatif, et non sur une alternative exhaustive. |
| **D10 — moniteur et contradiction** | **Acceptée.** Définir « non ambigu » par la lecture simple sélectionne les saturations ; une note congruente peut renforcer un score sans produire d’erreur. | Stratification préenregistrée par \(r\) simple, analyses principales dans les strates intérieures, saturation rapportée séparément, notes non polaires et sans rapport. La pente de taille reste secondaire si les strates sont trop peu peuplées. |

## (b) Expériences corrigées

Pour chaque contraste, \(H_A\) et \(H_B\) sont exclusives et exhaustives à \(\varepsilon\) près. Un résultat net dans un sens falsifie l’autre interprétation ; un résultat traversant la marge ne falsifie rien et est déclaré non concluant.

### E1 — D6/D7 : la variance neutre apporte-t-elle une prédiction transportable ?

- **Données :** campagnes publiques, puis entrées R4 et R6-standard à récupérer ; leur contenu n’est pas supposé ici. Étape préalable : élucider `Q_GAIN` dans le code public avant toute revendication de nouveauté.
- **Mesure :** variance estimée sur un sous-ensemble neutre ; \(p_0\) et \(\Delta\) sur des tirages disjoints. Pour campagne 1, l’autre campagne neutre servira aussi d’instrument, avec le test placebo neutre–neutre. Les coefficients seront gelés avant R4/R6.
- **Rivaux :** loi à \(g\) constant ; modèle préenregistré en \(p_0\) seul ; nul borné simulé à \(g\) constant. Aucun \(g_i\) individuel ne sera estimé.
- **Duel :** soit \(\theta\) la plus petite amélioration de SSE hors corpus apportée par la variance sur **chacun** des rivaux.  
  **\(H_A:\theta>\varepsilon\)** : la suffisance transportable du \(g\) constant et des rivaux géométriques est falsifiée.  
  **\(H_B:\theta\le\varepsilon\)** : l’existence d’un apport transportable de la variance, à cette marge, est falsifiée ; la loi globale n’est pas pour autant démontrée.
- **Contrôles :** variances permutées, placebo neutre–neutre, récupération sur simulations bornées. Coût de génération et de juge : nul si les fichiers publics sont récupérés.

### E2 — D1 : stabilité du juge, formulée comme équivalence

Estimer d’abord le bruit à partir des répétitions R6 **RAPPORTÉES**. Si des lectures nouvelles sont nécessaires, elles porteront sur les textes publics, stratifiées par condition et par note, avec doublons intercalés dans un même lot. Le bruit intra-lot et l’écart aux notes anciennes seront publiés séparément.

Le bruit estimé sera propagé aux analyses publiques. Soit \(\theta\) le déplacement induit, sur une métrique continue préenregistrée ; \(\hat c\) n’entre que lorsque \(\hat g\) est assez précis.

- **\(H_A:\theta\ge\varepsilon\)** : traiter les notes comme fixes à cette échelle de décision est falsifié.
- **\(H_B:\theta<\varepsilon\)** : une instabilité matérielle à cette échelle est falsifiée, sans exclure une dérive historique de l’alias.

Les franchissements de C1/C2 restent secondaires et descriptifs.

### E3 — D2/D3 : contribution du texte au-delà du verdict d’ouverture

Construire des paires fonctionnellement segmentées : ouverture avec verdict explicite, reste avec arguments, et versions éditées conservant verdict, longueur approximative et cohérence. Les fragments syntaxiquement incomplets seront évités. Une grille de surface figée servira seulement à décrire les éditions.

Soit \(\theta\) la contribution supplémentaire du reste au déplacement, après soustraction de l’effet mesuré sur les contrôles édités.

- **\(H_A:|\theta|\le\varepsilon\)** : la nécessité matérielle du reste, au-delà de l’ouverture, est falsifiée.
- **\(H_B:|\theta|>\varepsilon\)** : la suffisance de l’ouverture, à cette marge, est falsifiée.

Contrôles : première phrase neutre isolée, adresse factice à l’utilisateur dans les deux conditions, segments synthétiques à verdict constant, ordre randomisé. Un sous-ensemble humain indépendant bornera la part due au seul juge. Le résultat concerne la lecture du texte, pas la localisation d’un état interne.

### E4 — D5 : destination commune après calibration, sans prétention sur \(g\)

Calibration affine avec erreurs de mesure sur items neutres d’apprentissage ; évaluation sur items réservés et réponses pressées. Aucune cible hors du support de calibration ne sera tranchée.

- **\(H_A:\max_r|\hat c_r^{cal}-\hat c^{ref}|\le\varepsilon\)** : l’existence de destinations spécifiques au-delà de la marge est falsifiée, sous le modèle affine.
- **\(H_B:\max_r|\hat c_r^{cal}-\hat c^{ref}|>\varepsilon\)** : une destination commune par calibration affine, à cette marge, est falsifiée.

Le contrôle neutre(c2a)→neutre(c2b) doit produire l’absence d’effet attendue ; sinon, l’instrument est déclaré non jugeable.

### E5 — D8/D9 : deux contrastes factoriels, sans exclusivité artificielle

Plusieurs formulations par niveau, intensité perçue mesurée sur participants séparés, formulations réservées et analyse dont l’unité de généralisation est la formulation.

1. **Intensité :** \(\theta_I\) est l’amélioration hors formulations apportée par l’intensité perçue au-delà de la longueur et de l’identité lexicale.  
   **\(H_A:\theta_I>\varepsilon\)** falsifie la suffisance du modèle formulation/longueur.  
   **\(H_B:\theta_I\le\varepsilon\)** falsifie un apport transportable de l’intensité à cette marge.
2. **Social :** \(\theta_S\) est l’incrément utilisateur contre source tierce et ancre non sociale, à contenu évaluatif apparié.  
   **\(H_A:\theta_S>\varepsilon\)** falsifie la suffisance d’un ancrage générique.  
   **\(H_B:\theta_S\le\varepsilon\)** falsifie un incrément social mesurable à cette marge, sans nier l’effet de l’ancre elle-même.

### E6 — D10 : suivi d’instruction ou intégration du texte par le moniteur

Notes congruentes, contradictoires, véridiques, sans rapport et non polaires ; analyses stratifiées par \(r\) simple intérieur à l’échelle. Soit \(\theta\) la différence de déférence entre notes contradictoires et congruentes après ces strates.

- **\(H_A:|\theta|\le\varepsilon\)** : une forte dépendance au contenu est falsifiée ; le suivi reste compatible avec une instruction relativement indépendante du texte.
- **\(H_B:|\theta|>\varepsilon\)** : le suivi indépendant du contenu est falsifié.

Les zones saturées ne fourniront aucune conclusion de marge. Les logits et les règles d’exclusion seront publics pour recalcul externe.

## (c) Réponse à l’arbitre : établi, non établi, première expérience

**Établi dans les pièces, au statut RAPPORTÉ.** Pour Llama-3.1-8B-Instruct et la formulation standard, la relation linéaire d’attraction est retrouvée par plusieurs lecteurs et transportée sur les items R4 sans réajustement ; R4 rapporte notamment \(R^2=0{,}683\) sous critique et \(0{,}579\) sous éloge avec les constantes de campagne 1. R6-standard la retrouve avec de nouvelles graines. Ces résultats dépassent une simple poussée toujours ascendante sous éloge, puisque des items au-dessus de la cible descendent.

**Déjà borné, également RAPPORTÉ.** La relation n’est pas universelle entre familles : R3 rapporte des régimes différents pour Qwen, Mistral et Gemma. R6 ne confirme ni croissance commune du gain avec la dose ni stabilité du point fixe ; l’issue préenregistrée pour Llama est C. Dans l’auto-notation R2, l’effet sous éloge est faible et la séparation des destinations n’est pas robuste au rejeu d’implémentation.

**Non établi.** Aucun de ces éléments n’établit un attracteur psychologique ou causal. \(g\) et \(\hat c\) restent des paramètres d’une description statistique dont la validité dépend de l’échelle, du juge et du corpus. La validation humaine R5 n’est pas publiée dans les pièces ; le prompt du juge et les textes d’items ne sont pas fournis ; la CI, les audits privés, l’antériorité Zenodo et les chaînes de custody ne sont pas audités ici. Les 24 réponses visibles montrent des concessions, recentrages et refus possibles, mais ne permettent aucune fréquence générale. Enfin, l’existence de `Q_GAIN` interdit de présenter D6 comme inédit avant d’en connaître la définition.

**Première expérience : E1.** Elle est première parce qu’elle attaque directement une simplification centrale — un \(g\) constant — sans nouvelle génération ni nouveau juge, tout en réparant les trois artefacts identifiés : tirages partagés, relation moyenne–variance et rivaux bornés mal spécifiés. Son oui ne « réfuterait la loi » que dans une version transportable à gain constant face aux rivaux préenregistrés ; son non éliminerait, à la marge choisie, une explication par l’incertitude neutre. Dans les deux cas, on apprend quelle quantité doit être transportée avant d’investir dans de nouvelles interventions textuelles ou mécanistes.

FIN-DE-CELLULE