# Proposition B, tour III.3 : réponse aux critiques

**État des pièces**
- J'ai lu `texte-servi.md` en entier, soit 1 009 lignes. L'outil a tronqué la première lecture ; j'ai donc lu le fichier en plusieurs fois, avec Read seul et sans aucune recherche.
- Pièces présentes et closes par FIN-DE-CELLULE : ma conception du tour III.1 et les critiques croisées de A, C, D, E et F. Chaque critique contient une section « Sur la proposition B » ; je ne réponds qu'à ces sections.
- Les blocs FAITS et QUESTION ont le même texte et annoncent la même empreinte. Je n'ai recalculé aucune empreinte : elles ne sont pas vérifiées.
- Les conceptions III.1 de A, C, D, E et F ne sont pas dans le fichier. Quand j'emprunte un contrôle à l'un d'eux, je le dis (règle B1).
- Je garde le statut que chaque critique donne à ses énoncés. Plusieurs mentions `VÉRIFIÉ` de C et de E portent sur des mécanismes ou des souvenirs ; je ne les modifie pas et je ne fonde aucune décision dessus. Mes décisions reposent sur le texte de ma pièce III.1 et sur des conséquences des définitions.
- Les « travaux de 2026 » restent RAPPORTÉ, non attribuables. Rien n'a été exécuté. **Tout seuil, effectif, dose ou coût ci-dessous est illustratif** ; les nombres de lignes et de pièces sont des constats de lecture.

## (a) Décision sur chaque critique

Les corrections K1 à K17 sont détaillées en (b).

### Critique de A
| Réf. | Point visé | Décision | Raison ou suite |
|---|---|---|---|
| A-a1 | À α ≤ 1, un sous-espace aléatoire de rang k peut ne pas atteindre le G de U, donc le témoin changerait d'opérateur | Acceptée | K2 |
| A-a2 | G est égal en moyenne, mais pas forcément en loi | Acceptée | K3 |
| A-a3 | Dose, couches et rang non fixés ; rejeu sur étiquettes permutées absent du critère | Acceptée | K2, partitions disjointes, K5 |
| A-a4 | T-sortie est nul par construction en format discriminatif | Acceptée | K6 |
| A-a5 | H_A exige toutes les familles de témoins, H_B une seule : taux de faux verdicts asymétriques | Acceptée | K4 (un seul comparateur pour le duel), K11 |
| A-a6 | E3 oppose des hypothèses que les positions A et B ne soutiennent pas ; la persistance est acquise en forçage | Acceptée pour l'étiquette H_A et pour le forçage. Rejetée sur la cible | La phrase « n'a pas d'état à perdre » figure dans la position B des FAITS. E3 reste un test de cette prémisse, pas un duel A/B (K14) |
| A-b Σ | La puissance dépend de l'écart rapporté à σ_sub ; le 99ᵉ centile sur 200 tirages est fragile | Acceptée | K4, K10 |
| A-b d_t | Estimateur-rapport instable ; plancher génératif arbitraire | Acceptée | Condition de validité maintenue ; plancher mesuré (K6) |
| A-b marges | Si les marges intactes diffèrent entre groupes, S > 0 sous n'importe quelle perturbation | Acceptée | K7 |
| A-b équivalence | σ_sub absent de l'erreur type ; inférence limitée aux six tâches | Acceptée | K10. Portée déclarée : ces six fonctions et leurs jeux de données |
| A-b r_K | Douze cellules seulement, et α₅₀ censuré | Acceptée | K13 |
| A-b T½ | Demi-vie non définie si la décroissance n'est pas monotone | Acceptée | K14 |
| A-b AUC | Nombre minimal d'échecs non donné | Acceptée | K15 |
| A-c | Nul apparié par sélection, témoin de portée, verdicts témoin contre témoin, masse d'attention, G à α = 1 publié avant mesure | Transformées en tests | K5, K11, K14, K2 |

### Critique de C
| Réf. | Point visé | Décision | Raison ou suite |
|---|---|---|---|
| C-a1 | La règle à plusieurs métriques rend « aucune » vraie par construction | Acceptée pour la conséquence, rejetée pour le mot « garantit » | Les appariements ne divergent que sous une condition sur les spectres, que E écrit. Mais le droit de veto n'avait pas de justification : K1 le supprime |
| C-a2 | « Étiquette justifiée » et « réécriture » changent la fonction des tâches gardées | Acceptée | K6. Ce biais joue contre A |
| C-a3 | En forçage, E3 lit un cache figé | Acceptée | K14 |
| C-b1 | Kendall atténué ; seulement six tâches effectives | Acceptée | K13 |
| C-b2 | Le premier passage donne T½ = 1 pour U comme pour le témoin | Acceptée | K14 (aire, pas premier passage) |
| C-b3 | F est indéfini en génération libre | Acceptée | K7 |
| C-c1 | Masquer ou remplacer le cache des positions 256 à 511 | Transformée en test | K14 |
| C-c2 | Noter séparément l'étiquette et la justification | Acceptée | K6 |

### Critique de D
| Réf. | Point visé | Décision | Raison ou suite |
|---|---|---|---|
| D-a1 | Le format génératif change à la fois la fonction et le format | Acceptée | K6 |
| D-a2 | La température d'échantillonnage laisse G inchangé ; la température des logits laisse l'ordre des options inchangé | Acceptée | K6 |
| D-a3 | « Auto-entretien » n'est que la lecture tardive d'une clé ; en génération libre, le texte change | Acceptée | K14 |
| D-a4 | La marge contre la « meilleure concurrente » est indéfinie en génération libre | Acceptée | K7 |
| D-b1 | Σ ne voit pas les différences orthogonales au contraste | Transformée en test | K8 |
| D-b2 | Une sonde linéaire au hasard ne prouve pas l'indépendance | Acceptée | K12 |
| D-b3 | α₅₀ n'est pas défini de façon unique | Acceptée | K13 |
| D-b4 | Aucune statistique de trajectoire ne sépare un cache écrit une fois d'un régime entretenu | Acceptée | Il faut donc intervenir sur le cache (greffe), K14 |
| D-b5 | Énoncés conditionnels sur le motif, l'auto-rapport et l'ordre humain | Acceptés | Déjà la logique de ma table (c) du tour III.1 ; K16 |
| D-c | Notation séparée, contrebalancement, greffe en trois bras, inattention sur les mêmes stimuli | Acceptées ; je reprends la greffe de D (B1) | K6, K14, K16 |

### Critique de E
| Réf. | Point visé | Décision | Raison ou suite |
|---|---|---|---|
| E-a1 | Les tâches gardées sont dénaturées | Acceptée, détail rejeté | Selon mes règles III.1, une baisse des tâches gardées en génératif abaisse Σ_gén et mène à « aucune », pas au cas « le profil suit le format ». La correction est la même (K6), avec la tâche longue locale que propose E (B1) |
| E-a2 | α₅₀ censuré ; F incommensurable entre formats | Acceptée | K13, K7 |
| E-a3 | T½ est acquis par le cache | Acceptée | K14 |
| E-a4 | T-sortie dégénéré ; veto par la variance retirée | Acceptée | K6, K1 |
| E-b1 | Variance du quantile de queue | Acceptée | K4 |
| E-b2 | La précondition d'E2 échoue presque sûrement | Acceptée | K13 |
| E-b3 | Biais du premier passage | Acceptée | K14 |
| E-b4 | L'atténuation du τ humain valide H_A à tort | Acceptée | K16. C'est le défaut le plus grave côté humain : mon test penchait vers A |
| E-c1, E-c3 | Tâches longues locales ; plafond calculé sur deux moitiés des données | Acceptées et reprises (B1) | K6, K16 |
| E-c2 | Corrompre les clés à longue portée | Transformée en test | K14 |

### Critique de F
| Réf. | Point visé | Décision | Raison ou suite |
|---|---|---|---|
| F-a1 | T-sortie invalide ; variance retirée indéfinie pour trois témoins sur cinq | Acceptée | K6, K1 |
| F-a1 E3 | Pas de boucle en forçage ; T½ mesure ‖W_K U‖ et ‖W_V U‖ | Acceptée | K14 |
| F-a1 | Tâches gardées déformées ; plancher génératif non fixé ; F indéfini | Acceptée | K6, K7, K13 |
| F-a1 μ | Biais de domaine de μ_ℓ ; myopie positionnelle | Acceptée | K9, K5 |
| F-a2 | T-hasard sert deux fois, au seuil et aux fausses alertes | Acceptée | K4 (deux lots disjoints) |
| F-a2 | Fuite de F | Rejetée en discriminatif | En notation par vraisemblance, la marge intacte d'un item est déterministe : aucune fluctuation d'échantillonnage ne la couple à d_t. Le couplage qui reste vient de la sélection des items, et je repondère au lieu de sélectionner (K7) |
| F-a2 | La correspondance humain ↔ tâches est un paramètre libre | Transformée en test | Elle était déjà déclarée d'avance comme degré de liberté au tour III.1. Son contenu reste libre : K16 |
| F-b | Pilote sans τ²_j ; union sans correction ; ΔAUC aux bornes | Acceptées | K10, K4, K15 |
| F-c1 à c3 | Myopie ; rupture de contexte et normes clé-valeur ; lot neuf et permutation dans le verdict | Acceptées | K5, K14, K4 |
| F-c4 | Varier μ_ℓ ; modèle de base ; la direction de refus ne teste pas l'inversion de S | Acceptée sauf le dernier point | Ma table (c) III.1 place la direction de refus comme contrôle de l'intervention (« témoin positif reproduit »). Le contrôle de S est la lésion plantée d'identité de langue. Modèle de base : K17 |

## (b) Expériences corrigées

### Cadre fixé avant toute mesure
- **Modèles.** M1 et M2 : deux familles instruites, de 1 à 3 milliards de paramètres. Une version de base de M1 en secondaire (K17).
- **U_rec.** Retrouvé par une procédure déclarée, sur la seule partition de découverte. Si U_2026 est fourni sans sa procédure, il est analysé en secondaire, sans nul de sélection possible.
- **Partitions d'items disjointes.** Découverte (U, couches, rang) ; calibration (μ_ℓ, marges, dose, pilote) ; test (verdict). Deux jeux de données par fonction.
- **Intervention inchangée.** h ← h − α·UUᵀ(h − μ_ℓ), avec α ∈ [0 ; 1].

**Corrections**
- **K1. Appariement.** G seul. L'entropie croisée et la variance retirée sont rapportées, sans droit de veto.
- **K2. Dose principale G₁.** C'est le plus grand G atteint, avec α ≤ 1, par U et par au moins 90 % des sous-espaces aléatoires de même rang, dans les mêmes couches. Le G atteint par T-hasard à α = 1 est publié avant la mesure. Une dose plus forte, à rang aléatoire augmenté, est rapportée sans valeur de verdict.
- **K3. Loi de la KL par jeton.** Les déciles 1, 5 et 9 doivent être appariés à ± 10 %. Un tirage hors tolérance est exclu et compté. Au-delà de 20 % d'exclusions, l'expérience est non jugeable.
- **K4. Comparateur du duel.** T-hasard seul, puisque c'est le témoin que nomme la position B. Un lot de calibration de 200 tirages et un lot de verdict de 1 000 tirages, disjoints. T-variance, T-bruit et T-poids sont secondaires, avec correction de Holm, et ne pèsent pas sur le verdict.
- **K5. Gardes, appliquées seulement si A gagne le duel.**
  - **T-sélection** : la procédure de découverte est rejouée sur les 19 autres partitions 3/3 des six tâches et sur 100 étiquetages permutés, puis appariée de la même façon.
  - **T-fenêtre** : troncature de l'attention, appariée en G (contrôle repris de E et de F).
  - **Croisement distance d'entrée × fonction** : tâche locale à longue distance contre tâche intégrative courte (plan empan × profondeur de E).
- **K6. Formats.**
  - **Discriminatif (principal)** : leurres et positions contrebalancés.
  - **Génératif (garde de format)** : pour les fonctions gardées, génération longue sans justification ni réécriture (classer N phrases en série, extraire exhaustivement des attributs balisés). Si une justification subsiste, l'étiquette et la justification sont notées à part.
  - **Plancher génératif** : score mesuré de sorties dégénérées déclarées d'avance (copie de la source, sortie vide). Le verdict, recalculé avec deux planchers, doit rester le même.
  - **T-sortie** : mise à l'échelle des logits appariée en G, en génératif seulement.
- **K7. Marges.** Définies en discriminatif seulement. Σ est calculé après repondération des items vers une loi commune des marges entre groupes. On repondère sans sélectionner, donc sans biais de collision.
- **K8. Profil complet.** Les six différences d_t entre U et la médiane des témoins sont testées en plus de Σ.
- **K9. Choix de μ_ℓ.** Trois variantes : corpus neutre ; corpus équilibré des six tâches ; projection prise sur une autre entrée de la même tâche. Si le verdict diffère entre elles, l'issue est « aucune », pour A comme pour B.
- **K10. Effectifs.** L'erreur type inclut la variance entre jeux de données. Le dimensionnement se fait sur la borne haute à 80 % des variances du pilote.
- **K11. Calibrage de toute la chaîne de décision.**
  - Faux A : chaque tirage de calibration, puis chaque U obtenu sur étiquettes permutées, joue tour à tour le rôle de U contre les autres. C'est l'idée « un contre M − 1 » de F.
  - Faux B : on mesure le taux sur une lésion plantée de sélectivité connue.
- **K12. Instrument.** LEACE plus une sonde non linéaire. Si cette sonde retrouve le contenu de U, j'écris seulement « effacement linéaire ».

### E0 : portes de faisabilité, sur la partition de calibration
| Porte | Condition | En cas d'échec |
|---|---|---|
| P1 | Chaque tâche est au moins 20 points au-dessus du plancher et sous 95 % | Tâche retirée ; si une fonction disparaît, l'expérience est non jugeable |
| P2 | G₁ existe, et sous T-hasard la dégradation moyenne y est ≥ 0,1. Jamais conditionné à l'effet de U, ce qui empêcherait B de gagner | Non jugeable |
| P3 | Sous T-hasard, q95 − q05 de S ≤ 2δ_B, avec δ_B = 0,05 | H_B non jugeable. On publie qu'à G égal, les ablations génériques n'ont pas un profil commun |
| P4 | Erreur type ≤ δ_B/2 ; puissance ≥ 0,8 à δ_A = 0,15 | La branche concernée est non jugeable |
| P5 | Faux A ≤ 5 % ; lésion plantée retrouvée ≥ 18 fois sur 20 | Pas de verdict |
| P6 | K12 passé ; direction de refus reproduite | Pas de verdict |

Une porte en échec est un résultat publié. Elle ne compte jamais pour A ni pour B.

### E1′ : duel principal (partition de test, format discriminatif, dose G₁)
Statistique : Σ = S_U − médiane(S_T-hasard), après la repondération K7.

| | H_A : profil propre | H_B : même profil |
|---|---|---|
| Prédiction | La borne basse de l'IC à 95 % de S_U dépasse le q99 du lot de verdict, et Σ ≥ δ_A | L'IC à 90 % de S_U est contenu dans [q05 ; q95] du lot de verdict (P3 passée) |
| Falsifiée par | l'issue H_B | l'issue H_A |

Les deux régions sont disjointes. Issues hors duel, déclarées d'avance :
- **H_A, mais une garde K5 reproduit le profil** → « troisième voie ». La prédiction de B est falsifiée et l'interprétation de A n'a pas d'appui. La garde en cause est nommée.
- **H_B sur Σ, mais K8 hors équivalence** → « même contraste, autre profil ». B est falsifiée sur le « même profil », sans rien gagner pour A.
- **Σ ≤ −δ_A** → les deux prédictions sont falsifiées.
- **Verdict qui change avec le format** → « dépendant du format ». Si T-sortie reproduit Σ_gén, c'est un effet d'accumulation.
- **Tout autre cas** → « aucune ».
- Tout est répliqué sur M2. Un verdict obtenu sur un seul modèle est rapporté comme tel.

### E2 : retirée comme duel (K13)
Douze cellules, dont la moitié serait censurée si A a raison, ne séparent pas les seuils prévus. Les courbes dose-réponse à huit doses sont publiées sans verdict. Avec six tâches, l'« échelle graduée » n'est pas estimable ; il faudrait au moins vingt fonctions.

### E3′ : test de la prémisse de B (K14), pas un duel A/B
- **Forçage par l'enseignant : abandonné comme test.** Après relâchement, la seule voie d'influence est le cache écrit pendant la fenêtre ; c'est une conséquence de l'attention causale.
- **Plan 2 × 2 en génération libre**, repris de la greffe de D (B1).
  - On génère une continuation de 400 jetons, soit par le modèle intact (texte T₀), soit par le modèle intervenu (texte T₁).
  - Une sonde fixe est placée en fin de séquence.
  - On l'évalue sous {T₀, T₁} × {cache de fenêtre intact, cache perturbé}.
- **Mesure** : aire de KL en excès sur la réponse à la sonde, sur 2 000 textes.

| | H_lecture | H_boucle |
|---|---|---|
| Prédiction | Effet de T₁ contre T₀, cache intact : équivalent à 0 | Cet effet est > 0, et le rapport U/témoin est ≥ 3 |
| Falsifiée par | un effet de texte propre à U | l'équivalence à 0 |

- **Témoins** :
  - appariement en G, en masse d'attention reçue et en ‖W_K U‖, ‖W_V U‖ (F) ;
  - rupture de contexte (F) ;
  - corruption des clés à longue portée comme témoin positif (E).
- **Portée** : même si H_boucle l'emporte, cela ne montre qu'une propagation par la sortie. Ni éveil, ni appui à A.

### Côté humain (K16)
- Plafond : τ entre deux moitiés des données d'anesthésie (E), puis comparaison désatténuée.
- **H_A humain** : τ(anesthésie, autre dégradation) est sous le plafond, pour chacune des dégradations (inattention, sommeil, alcool).
- **H_B humain** : τ est équivalent au plafond pour au moins l'une d'elles.
- Inattention testée sur les mêmes stimuli (D). Au moins cinq niveaux de traitement ; sinon, analyse descriptive seulement.
- Liste fermée de correspondances humain ↔ tâches, déclarée d'avance. Un verdict n'est retenu que s'il est le même pour toutes.

### Motif ordinaire (K15)
Le nombre d'échecs nécessaire pour une erreur type de ΔAUC ≤ 0,01 est calculé d'avance. Si le modèle intact ne produit pas assez d'échecs, la branche n'est pas lancée.

## (c) Réponse à la question de l'arbitre

**Ce qui est établi**
1. **Aucun fait empirique sur ces directions.** Les travaux de 2026 restent RAPPORTÉ, non attribuables. Aucune pièce ne rapporte d'exécution (VÉRIFIÉ sur pièces).
2. **Des propriétés des plans, qui découlent des définitions** (VÉRIFIÉ, contrôlable par tout lecteur) :
   - Multiplier les logits par une constante positive ne change pas l'ordre des options. Un témoin de température est donc nul en choix forcé, et une température d'échantillonnage ne modifie pas G.
   - En forçage par l'enseignant, après relâchement, l'intervention n'agit plus que par les clés et valeurs écrites dans la fenêtre. Aucun « régime auto-entretenu » n'y est testable.
   - α₅₀ est censuré pour toute cellule qui n'atteint pas 0,5 avec α ≤ 1, ce que A prédit pour les tâches gardées.
   - Quand on compare un U unique à une loi de sous-espaces, la puissance dépend de l'écart rapporté à la dispersion entre sous-espaces, pas du nombre d'items.

   Ma conception III.1 avait les trois premiers défauts ; ils sont corrigés en (b).
3. **Mon point 0 n'a été contesté par aucune des cinq critiques.** Faute d'un pôle dont le statut est connu hors de la manipulation, aucune expérience sur le modèle ne calibre la transposition de l'anesthésie. Cela reste une HYPOTHÈSE logique, non réfutée ; ce n'est pas un résultat.

**Ce qui n'est pas établi**
- Que le profil rapporté se reproduise sur un petit modèle ouvert.
- Qu'il diffère d'une dégradation générique à G égal.
- Qu'il ne soit pas fabriqué par la sélection des directions, par la portée de l'attention ou par le format.
- Qu'un effet survive hors du cache.
- Que l'ordre de perte sous anesthésie soit propre à l'anesthésie chez l'humain. Mon test III.1 penchait vers A par atténuation (critique E) ; il est corrigé.
- Quoi que ce soit sur la conscience d'un modèle. Aucune issue ne permet d'écrire qu'un modèle « était conscient et a perdu cet état », ni l'inverse. Ma table du point 4 (III.1) n'a pas été critiquée et reste valable.

**L'expérience à faire en premier : E0 puis E1′, en format discriminatif, sur M1.**
- **Pourquoi celle-là.** Elle conditionne le reste, et chacune de ses issues falsifie H_A ou la prédiction de B.
- **Ordre des étapes** :
  1. découverte de U_rec ;
  2. calibration de G₁, μ_ℓ, des marges et des deux lots de témoins ;
  3. portes P1 à P6, publiées avant le verdict ;
  4. levée de l'aveugle sur la partition de test ;
  5. gardes K5, seulement si A gagne ;
  6. réplication sur M2.
- **Coût illustratif.** 20 à 40 heures-GPU, et autant pour T-sélection.
- **Ensuite, indépendamment du duel.** E3′, puis la réanalyse humaine avec le plafond calculé sur deux moitiés des données.

**Ce qui peut être réfuté** (aucun énoncé ne porte sur la conscience) :
1. U_rec dépasse le q99 de T-hasard avec Σ ≥ δ_A.
2. S_U reste dans [q05 ; q95].
3. Les ablations génériques ont un profil commun (P3).
4. Une garde K5 reproduit le profil de U.
5. Le verdict change avec le format.
6. Un effet survit dans le texte une fois le cache restauré.
7. Chez l'humain, l'anesthésie se distingue de l'inattention au-delà du plafond.

**Antériorité ajoutée.** J'ai lu `texte-servi.md` seulement. Cités de mémoire, non relus :
- Holm (1979), *A simple sequentially rejective multiple test procedure*, Scand. J. Statist.
- Spearman (1904), *The proof and measurement of association between two things*, Am. J. Psychol.
- Hewitt & Liang (2019), *Designing and Interpreting Probes with Control Tasks*.

FIN-DE-CELLULE