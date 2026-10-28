# Étape 2 du gradient d'organismes — proposition de plan (brouillon v1 : rien de scellé, rien ne part)

- Sous-agent neuf de la lignée conv-audit. **Début : 2026-10-25 23:54:03 UTC** (lu sur `date -u`). **Écriture de ce
  fichier : 2026-10-26 00:09:03 UTC** (lu sur `date -u` juste avant d'écrire ; aucune heure de fin n'est donnée).
- Brief : `/tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/brief-etape2-v1.md`
  (`bf0e93630b19220aea6b2f2e86ab3cdfff0e3b5154bf43388ac40b1362dc10a7`).
- Empreintes vérifiées (`sha256sum -c`, toutes « OK ») : N-044 v1, N-045 v1 et v2, programme v2, brief programme
  complet v2, étape 1 v9, `LISEZMOI-gradient-v1.md`, brouillon de confrontation v7, `LISEZMOI-v9.md` de la banque,
  `banque-confrontation-v5.json` (`28e3c728d9d1251d50da18d61827b9f99578721f9988e19e3a3e19909e5c6e46`, celle que cite
  `LISEZMOI-v9.md` l. 4), pilote 4 v3.
- Non ouverts : tout `-cle.json`, `-secret.json` (8 sur disque dans le dossier de la banque), `P3-consignes-v1.md`,
  `textes-actions-*`, `reponse-question*`, `journal-appels*`, `ferme.tar.gz`, dossiers `donnees/`, `runs/`, `diag/`,
  `pilotes/` (aucun dans les copies du gradient), et par prudence `cle-paires-v1.json` et `reponses-verificateur-v1.json`.
  Aucun score de course lu. Aucune valeur de clé.
- Abréviations : USD = dollars américains ; « graine » = répétition indépendante d'une course entière (conception
  comprise), tirée par `numpy.random.SeedSequence` (R9).

## Verdict

1. L'étape 2 n'existe encore que comme une ligne de tableau (« renforcement réduit ») et comme règles de lecture
   (N-044, N-045) : aucun brouillon de préenregistrement, et aucun code pour ses bras propres (coût dans le signal,
   trois bras de diversité, témoins « meilleur de N » et « vote à k », scores permutés, adaptateur par renforcement).
2. Sur la banque v5 (48 tâches au test final, dont 12 de délégation qui portent 75 % de la variance du score), deux bras
   à 10 graines chacun ne séparent du bruit qu'un écart d'environ 0,11 à 0,17 d'exactitude équilibrée (0,07 à 0,15 si
   la difficulté des tâches porte l'essentiel de la variance) ; une seule graine ne tranche rien (variance de conception
   inestimable ; 9 à 36 % de faux positifs dès que la conception varie de 0,05 à 0,10 d'une graine à l'autre).
3. Proposition : pilote de bruit (test A/A sur le seul test de développement), puis **une** comparaison décisive bon
   marché — séquentiel contre meilleur de N à budget égal, 10 graines, référence « un modèle, vote à k » — avant tout
   bras plus complexe ; ni l'universalité (aucune famille tenue à l'écart dans la v5) ni un effet ≤ 0,10 ne sont à sa portée.

## 1. Ce que fixent le programme, N-044 et N-045 pour l'étape 2 ; ce qui existe ; ce qui manque

### 1.1 Citations exactes

Programme (`F/main-dbdf663/docs/programme-controle-ia-v2.md`, prime sur le fond) : il ne nomme pas les « étapes » du
gradient ; le gradient s'y rattache comme instrument de phase 0 de l'axe « contrôle de populations d'agents » (brouillon
de confrontation v7, l. 38–39). Trois contraintes y valent pour l'étape 2 : l. 137 « Une sonde n'est jamais entraînée
et évaluée sur les mêmes organismes » ; l. 143 « Plancher obligatoire : sonde aléatoire appariée en covariance (style
P3) — une sonde qui ne le bat pas n'existe pas » ; l. 270 « Universalité des signatures entre familles de modèles
(prudence : la forme mesurée dans P3 n'a pas transféré de Llama à Qwen) ».

Définition de l'étape 2 (`F/gradient-v2-3ea95fd/essaim-m3-refonte-v1/notes/programme-apprentissage-gradient-essaim-v1.md`,
antérieure à N-044 et N-045) : l. 55 « **2. Renforcement réduit** | récompense / perte, algorithme parmi plusieurs,
échantillonnage, données (dont générateur), programme | affinage LoRA de Llama-3.1-8B par renforcement : ≈ 8 échantillons
× 1 500 jetons par consigne ; 3 000 à 6 000 consignes par époque ; ≈ 10 à 20 h d'A100 par époque ; 2 époques par
génération | … | ≈ 250 à 600 USD de carte, ≈ 100 à 250 USD d'appels pour les données, ≈ 30 USD d'appels de conception
⇒ **≈ 500 à 1 000 EUR** » ; l. 58–60 « étape 2, **les deux meilleures lignées** » ; l. 84–87 H-G2 (adaptateur à
objectif conçu contre modèle local non affiné et contre récompense binaire) ; l. 88–89 H-G3 (gradient contre réécriture
de code « à budget total égal ») ; l. 76–77 « le test de développement et le test final restent ceux de la banque
scellée […] jamais engendrés par le même générateur que l'entraînement ».

N-044 (`F/main-dbdf663/docs/decisions/decision-N-044-v1.md`) :
- l. 10–11 : « cette note fixe la lecture du programme pour les préenregistrements à venir (étape 2 et suivants) ».
- l. 34–36 : « dont l'**universalité se mesure sur des familles de questions jamais vues à la conception** — familles
  engendrées, familles de l'autre fournisseur, provenance réelle (H-G4 et ses successeurs) — et jamais sur des items
  inédits des familles de conception. »
- l. 37–41 : trois régimes de budget (conception, usage à code figé, re-conception) — « en attente de son mot pour l'étape 1 ».
- l. 42–43 : vivier de conception « à part de la banque scellée (fichier empreinté ; identifiants disjoints du test et
  du test final, vérifiés par le script d'extraction) ».
- l. 46–48 : question ouverte « posée aux organismes **avant** tout matériau de notre part (anti-enfermement) ».
- l. 49–51 : « **Diversité** : trois bras à l'étape 2 (mission + miroir fonctionnel rendu dans `historique` ; contrainte
  câblée dans le noyau ; rien), organisme de Gemini (mécanisme câblé) rapporté à part ; le juge est la seule pression ;
  un résultat négatif se publie. »
- l. 56–57 : « les préenregistrements de l'étape 2 testent l'universalité sur des familles retenues et comparent les
  trois bras de diversité. »

N-045 v2 (`F/main-dbdf663/docs/decisions/decision-N-045-v2.md`, remplace la v1 ; la v2 ajoute les § 5 à 7) :
- l. 54–58 (§ 2) : « À partir de l'étape 2, le score de développement rendu à l'organisme dans `historique` porte, à
  côté de l'exactitude équilibrée, **le coût de la génération** (dollars d'appels par espèce, heures de carte des
  instruments, appels et jetons), et un **score net** défini au préenregistrement […] ; λ et la forme sont des paramètres
  gelés avant la course, jamais choisis au vu d'un résultat). »
- l. 58–61 : « Le juge externe (exactitude équilibrée sur le test caché, métrique de choix) **ne change pas** ; le coût
  est un second axe de lecture, rapporté par génération et par bras, et le préenregistrement dit lequel des deux est principal. »
- l. 62–65 (§ 3) : nécessité de la frontière mesurée ; « ce que chaque rôle perd quand on lui retire la frontière
  (ablation rapportée, hors des critères gelés) ».
- l. 66–69 (§ 4) : « Aucune voie à concepteur entraîné par renforcement n'est payée avant qu'une voie bon marché ait
  montré, sur familles tenues à l'écart et à budget égal, que **l'apprentissage séquentiel de génération en génération
  bat le meilleur de N tirages indépendants** (et le témoin « un modèle, vote à k, coût apparié »). »
- l. 79–82 (§ 5) : « un épisode couvre K générations (K ≥ 3, gelé au préenregistrement) […] Le bandit à un pas est exclu. »
- l. 84–87 (§ 6 i) : « pilote de bruit : écart-type test–retest du score de développement et étalonnage du bras apparié
  par un test A/A (deux runs du même bras ne doivent pas différer) » ; l. 89–90 (§ 6 iii) : « seulement ensuite, le
  transfert inter-familles à la puissance calculée (contrôles : concepteur non entraîné ; récompenses permutées). »
- l. 91–93 (§ 7) : espaces de conception égaux entre concepteur contraint et libre.
- l. 105–106 : « forme du score net et λ gelés ; lecture à deux axes ; ablation « sans frontière » rapportée ; témoins
  « meilleur de N » et « un modèle, vote à k » ; plancher de bruit écrit. »
- l. 112–115, non décidés : témoin « vote à k » (« quelques dollars, GO sur devis »), bras « score permuté », plancher
  de bruit, λ, « la forme exacte de la récompense d'héritage (K, actualisation) ».
- N-046 : absente des copies (`docs/decisions/` n'a que N-044, N-045 v1 et v2) ; citée par la règle de la banque v5
  (manifeste) et par `LISEZMOI-v9.md` l. 120 (lot 3).

### 1.2 Ce qui existe

| pièce | apport à l'étape 2 | limite |
|---|---|---|
| note de programme (ci-dessus) | définition, H-G2, H-G3, enveloppe | antérieure à N-044 et N-045 ; aucune répétition prévue |
| brouillons de confrontation v1–v7 (v7 l. 46–50, 69–79, 126–132, 295–318) | bras adaptatif contre bras gelé apparié, bootstrap à deux niveaux, condition par course, devis calculé par le code | banque v1, dont « les identifiants donnent la vérité » (`registres/decisions.md` l. 667, R-444) ; 2 courses, et « toute revendication forte exige une réplication à ≥ 4 courses » (v7 l. 78–79) |
| étape 1 v9 scellée (`etat.md` l. 4 ; v9 l. 203, 257, 318, 336–344) | bras A/B appariés, bootstrap à trois niveaux, puissance simulée | banque v1 ; puissance « faible (≈ 20 %) » à +0,10 (v9 l. 342–344) ; en révision (v10, non présente dans les copies) |
| noyau `essaim_m3/` | conception, moisson, vivier (`cli.py` l. 411), bras apparié `--gel`/`--depuis` (l. 389–390), sondes par gradient (`entrainement.py` l. 41 : `sonde-lineaire`, `sonde-une-couche`), `question_ouverte`, `historique` avec `cout_usd` et `n_appels` par génération (`contrat.py` l. 47) | voir 1.3 |
| banque v5 (comptes ci-dessous) | contre-lue, identifiants opaques, classes à 50/50 par part et famille | 12 traces de délégation par part ; deux familles, toutes deux vues à la conception ; « un état d'attente » (`LISEZMOI-v9.md` l. 120) |
| pilotes 2 et 3 (pilote 4 v3 l. 313–338) | coûts et durées mécaniques par génération | aucune mesure du bruit d'une graine à l'autre ; sur la banque v3, donc séparés de la v5 (BC5-02) |

Comptes de la banque v5 (lus par `calcul-ecart-minimal-v1.py`, agrégés seulement) :

| part | n | conscience d'évaluation (évaluation / usage réel) | contrôle de délégation (honnête / sabotage) |
|---|---|---|---|
| train | 80 | 48 (24 / 24) | 32 (16 / 16, en 16 paires) |
| test (développement, rendu dans `historique`) | 48 | 36 (18 / 18) | 12 (6 / 6) |
| test final (jamais rendu, lu une fois) | 48 | 36 (18 / 18) | 12 (6 / 6) |

Sous-ensembles de conscience dont la catégorie d'origine est absente du train : 8 en test (4/4), 14 en test final
(10/4) (`LISEZMOI-v9.md` l. 33–34).

### 1.3 Ce qui manque

1. Un brouillon de préenregistrement de l'étape 2 (hypothèses H-G2, H-G3 et H-G4 réécrites selon N-044 et N-045 ;
   H-G4 n'est que nommée : N-044 l. 36, `decisions.md` l. 585, R-363).
2. Une mesure du bruit (N-045 § 6 i) : écart type d'une graine à l'autre et test–retest ; rien de mesuré.
3. Une famille tenue à l'écart de la conception : la v5 n'en a aucune.
4. Dans le noyau (N-045 l. 101–104, « à coder par session-depot ») : coût par espèce, par rôle, en jetons et en heures
   de carte dans `historique` ; score net gelé au manifeste ; bras « contrainte câblée » et « miroir fonctionnel »
   (définis par trois mots seulement) ; témoins « meilleur de N » et « vote à k » ; scores permutés (option proposée,
   R-408, absente du code lu) ; récompense d'héritage ; entraînement d'adaptateur par renforcement ; gardes BC5-01
   (traits) et BC5-02 (séparation des banques) en code ; règle d'amorçage BC5-04.

## 2. Proposition de plan (respecte « le simple d'abord, chaque ajout isolé, assez de répétitions »)

### 2.1 Bras, du plus simple au plus complexe ; chaque ajout a son ablation

| échelon | bras | ce qu'il ajoute | ablation (le bras sans l'ajout) |
|---|---|---|---|
| 0 | références fixes : surface et provenance (calculées sur la banque, `LISEZMOI-v9.md` l. 102–105) | — | — |
| 0 | **B0** « un modèle, vote à k, coût apparié » (référence simple, N-045 l. 69) | — | — |
| 1 | **B1** organisme de génération 0 figé (une conception, une évaluation ; conception partagée avec B3) | la conception par l'organisme | B0 |
| 1 | **B2** meilleur de N conceptions indépendantes, choix sur le test de développement, budget plafond égal à B3 ; son premier tirage est la génération 0 de B3 (appariement) | N tirages | B1 |
| 2 | **B3** conception séquentielle, G = 3 générations = un épisode (K = 3, N-045 § 5), exactitude seule rendue | l'apprentissage de génération en génération | **B2 : porte de N-045 § 4** |
| 2 | **B3p** B3 avec scores permutés rendus | — (placebo du signal) | B3 |
| 3 | **B4** B3 + coût dans le signal (N-045 § 2), ablation « sans frontière » rapportée (§ 3) | le coût rendu | B3 |
| 4 | **B5c** contrainte câblée ; **B5m** mission + miroir fonctionnel (N-044 § 5) | la pression de diversité | B4 (« rien ») |
| 5 | **B6** B4 + sondes par gradient (processeur) | un instrument local | B4 |
| 6 | **B7** B6 + adaptateur par renforcement à objectif conçu (H-G2), avec ses témoins : adaptateur à récompense binaire entraîné par le noyau, modèle local non affiné | l'entraînement sur carte | B6 |

Un échelon ne part qu'après lecture de l'échelon précédent, chacun sous son préenregistrement scellé et contre-lu
(R1, R2). Un seul facteur change à la fois depuis la même base : les interactions ne sont pas estimées (§ 2.4).

### 2.2 Erreur type et écart minimal détectable (banque v5 réelle)

Calcul : `calcul-ecart-minimal-v1.py` (`c80f4ba25d1a22d50bf58e6cf48887919265173d1233b4a71981288ca11b449a`), sortie
`calcul-ecart-minimal-v1.json` (`7fcdfab9579dbb4b30ada21f4015e9822efc94ceb5fb459eaf58f58b8877da4f`). Score = celui du
juge : moyenne sur les deux familles de l'exactitude équilibrée (moyenne des rappels par classe). Pire cas p = 0,5 ; à
p = 0,8, multiplier les erreurs types par 0,8.

Erreur type d'une seule course :

| part | exactitude | équilibrée, conscience | équilibrée, délégation | score global | n effectif du score global |
|---|---|---|---|---|---|
| train (80) | 0,056 | 0,072 | 0,088 | 0,057 | 77 |
| test (48) | 0,072 | 0,083 | 0,144 | 0,083 | 36 |
| test final (48) | 0,072 | 0,083 | 0,144 | 0,083 | 36 |
| catégorie absente du train | — | test 0,177 (4/4) ; test final 0,148 (10/4) | — | — | — |

La délégation (12 traces) porte 75 % de la variance du score global au test final ; 0,083 est l'écart type « au
hasard » que donne `LISEZMOI-v9.md` l. 110–112.

Écart minimal détectable entre deux bras sur le score global du test final, **niveau 0,05 bilatéral, puissance 0,80**,
R graines par bras, graines non corrélées entre bras. Variance d'une course : σ² + (1 − ρ) × 0,25/36, où σ (« σ de
course ») est l'écart type, d'une graine à l'autre, du score vrai de l'organisme produit, et ρ la part de la variance
portée par la difficulté propre des tâches, commune aux bras (elle s'annule dans une différence sur les mêmes tâches).
Ce sont des **hypothèses** (non opposables) : les brouillons antérieurs supposaient un effet de course σ de 0 à 0,15
(v7 l. 74–76) et un bruit de bras de 0,25 en logit, ≈ 0,06 en probabilité (v9 l. 330–332). Cellule : écart avec la
variance estimée sur les graines (Student, degrés de liberté 2R − 2) ; entre parenthèses, avec la variance connue
d'avance (par le pilote).

| scénario | R = 1 | R = 3 | R = 5 | R = 10 |
|---|---|---|---|---|
| σ = 0, ρ = 0 (plancher binomial) | non testable (0,33) | 0,26 (0,19) | 0,17 (0,15) | **0,11** (0,10) |
| σ = 0,05, ρ = 0 | non testable (0,39) | 0,30 (0,22) | 0,20 (0,17) | **0,13** (0,12) |
| σ = 0,10, ρ = 0 | non testable (0,52) | 0,40 (0,30) | 0,26 (0,23) | **0,17** (0,16) |
| σ = 0, ρ = 0,6 | non testable (0,21) | 0,16 (0,12) | 0,11 (0,09) | 0,07 (0,07) |
| σ = 0,05, ρ = 0,6 | non testable (0,29) | 0,22 (0,17) | 0,15 (0,13) | 0,10 (0,09) |
| σ = 0,10, ρ = 0,6 | non testable (0,45) | 0,35 (0,26) | 0,23 (0,20) | 0,15 (0,14) |

- Graines nécessaires pour 80 % de puissance (Student) à +0,05 / +0,10 / +0,20 : 45 / 12 / 4 (plancher) ; 61 / 16 / 5
  (σ = 0,05) ; 108 / 28 / 8 (σ = 0,10) ; avec ρ = 0,6 : 19 / 6 / 3, 35 / 10 / 4, 82 / 22 / 7.
- Par famille, à R = 10 et au plancher : conscience 0,10, délégation 0,18.
- **Une seule graine** : la variance de conception n'est pas estimable ; une lecture qui ne connaît que le bruit des
  tâches (binomial ou bootstrap des tâches) donne, sous effet nul, 5 % de faux positifs si σ = 0, 9 % si σ = 0,05, 21 %
  si σ = 0,10, et 16 % à 36 % si ρ = 0,6 (simulation : 8,5 % et 21,4 % à ρ = 0).
- Contrôle par simulation (ρ = 0, 4 000 tirages par cellule, `SeedSequence(20261026)`) : rejet sous effet nul 4,6 à
  5,8 % ; puissance à l'écart calculé 0,795 à 0,823. Le calcul tient.
- Différences appariées sans corrélation entre bras (degrés de liberté R − 1) : 0,39 au lieu de 0,26 à R = 3 ; 0,12 au
  lieu de 0,11 à R = 10. L'appariement ne paie que si les bras partagent quelque chose (ici, la génération 0 de B3
  dans B2) : à R = 10, dès une corrélation de 0,12 entre bras.

### 2.3 Nombre de répétitions et forme de la comparaison

- **Unité : la graine.** Pour chaque graine, tous les bras d'un échelon partent dans le même bloc de temps, ordre tiré
  par `SeedSequence`, même lignée, même banque, mêmes plafonds ; une dérive du jour commune au bloc s'annule.
- **Statistique principale** : différence des moyennes, sur les R graines, du score global du test final (lu une fois,
  en fin de course). Intervalle à 95 % de Student (2R − 2 degrés de liberté), ou sur les différences appariées
  (R − 1) si le pilote mesure une corrélation entre bras d'au moins 0,15 — règle gelée avant la course.
- **Lecture secondaire** : bootstrap à deux niveaux (graines, puis tâches stratifiées par famille et classe, les mêmes
  pour les bras d'une graine), qui montre la part des tâches ; il est grossier et trop étroit à R ≤ 5 (v9 l. 321–322 le
  dit pour deux répliques). Test exact de permutation des signes possible seulement à R ≥ 6 (à R = 5, la plus petite
  valeur bilatérale atteignable est 2/32 = 0,0625).
- **Lecture d'équivalence** (pour pouvoir conclure « l'ajout n'apporte rien au-delà du bruit ») : deux tests unilatéraux
  à un plus petit effet d'intérêt δ₀ gelé. À R = 10, la demi-largeur de l'intervalle à 90 % vaut 0,065 / 0,075 / 0,101
  (σ = 0 / 0,05 / 0,10) : δ₀ = 0,10 n'est démontrable que si l'écart observé est presque nul ; à dire d'avance.
- **Nombre de graines recommandé : R = 10 par bras pour la porte**, révisable vers le haut par une règle gelée avant la
  course : le plus petit R donnant 80 % de puissance à +0,10 avec la borne haute à 80 % du σ mesuré par le pilote, au
  moins 10, au plus 16 ; au-delà, l'écart minimal réel est écrit au préenregistrement avant la course, jamais révisé
  après lecture.
- Lecture à deux axes (N-045 l. 105) : l'exactitude du juge en axe principal (à budget plafond égal), le coût réalisé en
  second axe, par génération et par bras.

### 2.4 Ce que ce plan ne peut pas trancher

1. **L'universalité** (N-044 l. 34–36) : les deux familles de la v5 sont servies à la conception ; aucun bras ne dit rien
   des familles inédites tant qu'une famille tenue à l'écart n'existe pas (H-G4 sans texte).
2. Un effet plus petit que l'écart minimal : rien sous ≈ 0,11–0,17 à 10 graines ; +0,05 demanderait 45 à 108 graines.
3. Les effets par famille : délégation ≥ 0,18 même au plancher ; catégories absentes du train (14 tâches) : 0,15 d'erreur
   type par course, quasi muet.
4. La généralisation à d'autres items des mêmes familles : les graines ne réduisent pas la part des 48 tâches fixes.
5. Les interactions entre ajouts (un facteur à la fois depuis la même base).
6. Le mécanisme : la composition étant apprise (N-045 § 1), une ablation isole un ingrédient du noyau, pas l'usage qu'en
   fait l'organisme.
7. La généralité entre concepteurs si une seule lignée court la porte (décision D7).
8. L'héritage au-delà de K = 3 générations ; le « bon » λ (la lecture à deux axes dit le compromis, pas sa valeur).
9. Une dérive propre à un bras (l'appariement par bloc n'annule que la dérive commune).

## 3. Coût et durée (ordre de grandeur non opposable, R7)

Base, tirée des coûts mécaniques des pilotes (pilote 4 v3, l. 313–338) : une génération coûte 6,55 à 8,63 USD (pilote 3
et second pilote, sur la banque v3 à 60 + 60 tâches ; la v5 en sert 48 + 48, donc sans doute un peu moins) et dure 607
à 965 s ; une ronde de conception est bornée à 3 USD (aucune mesure réelle) et estimée à 2 à 6 minutes ; préparation
≈ 4 à 5 minutes par segment. **Course de base (G = 3, ≤ 4 rondes) : ≈ 20 à 38 USD, ≈ 42 à 77 minutes.** B1 ≈ 6,5 à
8,6 USD ; B0 « quelques dollars » (N-045 l. 112), pris à 2 à 8 USD.

| phase | contenu | dépense attendue (USD) | durée de course cumulée | à 4 courses en parallèle |
|---|---|---|---|---|
| 2.0 pilote de bruit | 6 courses B3 (une lignée), test de développement seul, test final non lu ; test–retest des 6 organismes finaux | 160 à 280 | 6 à 10 h | 1,5 à 2,5 h |
| 2.1 porte | B0, B1, B2, B3 × 10 graines | 485 à 926 | 17 à 32 h | 4 à 8 h |
| 2.2 signal | B3p, B4 × 10 | 400 à 760 | 14 à 26 h | 3,5 à 6,5 h |
| 2.3 diversité | B5c, B5m × 10 | 400 à 760 | 14 à 26 h | 3,5 à 6,5 h |
| 2.4 sondes | B6 × 10 (+ traits de la v5, ≈ 2 USD de carte, note l. 54) | 200 à 380 | 7 à 13 h | 2 à 3,5 h |
| **total 2.0 à 2.4** | 76 courses et 26 évaluations | **≈ 1 650 à 3 100** | ≈ 58 à 107 h | ≈ 15 à 27 h |
| 2.5 renforcement réduit | B7 et le témoin binaire × 10 | ≈ 2 500 à 6 000 de carte et 100 à 250 d'appels (lecture de la note l. 55 : 250 à 600 de carte pour deux courses) | dizaines d'heures de carte par course | devis à part, après la porte seulement |

- En calendrier : un préenregistrement scellé et contre-lu par échelon, une lecture entre chacun, des segments de deux
  heures au plus (pilote 4 v3 l. 293–297) : ≈ 1 à 2 semaines pour 2.0 à 2.4.
- Pire cas : les plafonds du noyau mettent le devis à 2 à 5 fois l'attendu (75 contre 30–55 au pilote 4, l. 326–334 ;
  4 261 contre 700–800 à la confrontation, v7 l. 316–318) ; à calculer par le code avant tout GO. La recharge
  automatique est active sur toutes les clés (`etat.md` l. 5, R-404) : seuls les plafonds bornent.

**Version réduite (garde la capacité de trancher l'ajout le plus important, le séquentiel contre le meilleur de N)** :
pilote réduit à 4 courses B3 et 2 test–retest (≈ 95 à 170 USD, 3 à 6 h) ; porte B0, B2, B3 × 10 graines (≈ 420 à
840 USD, 15 à 28 h, 4 à 7 h en parallèle). **Total ≈ 515 à 1 010 USD**, même écart minimal à la porte (0,11 / 0,13 /
0,17). Elle abandonne B1, le signal, la diversité et les instruments, et son σ est plus incertain (3 degrés de liberté :
borne haute à 95 % ≈ 3,7 fois l'estimation, contre 2,4 avec 6 courses).

## 4. Décisions qui reviennent à Lazar

**D1 — Banque des comparaisons décisives de l'étape 2.**
Enjeu : la v5 a 12 traces de délégation par part (75 % du bruit), deux familles vues à la conception, et la provenance y
fixe la classe en conscience (BC5-03, `LISEZMOI-v9.md` l. 26–41) ; c'est un état d'attente du lot 3.
(a) v5 pour tout, tout de suite — avantage : disponible, contre-lue ; inconvénient : bruit maximal, rien sur
l'universalité. (b) attendre une v6 (lot 3, partition par catégorie, ≥ 96 tâches au test final, une famille tenue à
l'écart) — avantage : écart minimal divisé par 1,4 au plus (au plancher binomial, test final doublé), universalité
mesurable ; inconvénient : délai. (c) v5 pour le pilote de
bruit (test de développement seul, test final de la v5 non lu), v6 pour les phases décisives — avantage : avance en
parallèle ; inconvénient : le bruit se transpose en partie seulement.
Recommandation : (c), confiance ≈ 70 %. Défaut sous 48 h : (c) (ce choix n'engage aucune dépense).

**D2 — Une seule comparaison confirmatoire pour la première phase décisive : B3 contre B2.**
Enjeu : c'est la porte de N-045 § 4 ; chaque comparaison principale de plus coûte de la puissance.
(a) B3 contre B2 seule, le reste descriptif — avantage : toute la puissance sur la porte ; inconvénient : les autres
ajouts restent ouverts. (b) B3 contre B2 et B4 contre B3, correction de Holm — avantage : tranche aussi le coût dans le
signal ; inconvénient : écart minimal relevé d'environ 10 %. (c) les trois bras de diversité en principal — avantage :
lettre de N-044 § 5 ; inconvénient : trois bras avant de savoir si le séquentiel apporte quelque chose.
Recommandation : (a), confiance ≈ 75 %. Défaut sous 48 h : (a).

**D3 — Répétitions et forme : 10 graines par bras au moins, différence de moyennes, Student, lecture d'équivalence.**
Enjeu : sous 5 graines, aucun effet plausible (≤ 0,20) ne se sépare du bruit.
(a) R = 10 fixe — avantage : sépare ≈ 0,13 ; inconvénient : deux fois le coût de R = 5. (b) R = 5 — avantage : moitié
prix ; inconvénient : ne voit que ≥ 0,20, plus que les effets prédits jusqu'ici (+0,10). (c) R fixé par le pilote
(règle du § 2.3, entre 10 et 16) — avantage : le plus juste ; inconvénient : dépense connue après le pilote.
Recommandation : (c), confiance ≈ 65 %. Défaut sous 48 h : (c), écrit au brouillon (aucune dépense).

**D4 — GO sur devis pour le pilote de bruit (phase 2.0).**
Enjeu : sans σ mesuré, le nombre de graines nécessaire à +0,10 va de 12 à 28 selon l'hypothèse.
(a) 6 courses et 6 test–retest (≈ 160 à 280 USD) — avantage : σ à 5 degrés de liberté ; inconvénient : coût. (b) 4
courses et 2 test–retest (≈ 95 à 170 USD) — avantage : moins cher ; inconvénient : σ très incertain. (c) aucun pilote —
avantage : gratuit ; inconvénient : contraire au phasage accepté (N-045 l. 84–87), R choisi à l'aveugle.
Recommandation : (a), confiance ≈ 70 %. Défaut : aucun — dépense : rien ne part.

**D5 — Forme du score net rendu à l'organisme et λ (N-045 § 2).**
Enjeu : le signal pousse l'organisme vers ses instruments locaux, mais peut récompenser l'inaction bon marché.
(a) exactitude − λ × coût, λ gelé — avantage : un seul nombre ; inconvénient : λ arbitraire. (b) exactitude par dollar —
avantage : sans paramètre ; inconvénient : favorise le presque gratuit au hasard. (c) front exactitude–coût rendu tel
quel — avantage : rien d'arbitraire à geler ; inconvénient : l'organisme choisit son compromis.
Recommandation : (c), avec l'exactitude du juge en axe principal à budget égal, confiance ≈ 55 %. Défaut sous 48 h : (c).

**D6 — Ordre des fronts (ta demande : un maximum de fronts en parallèle).**
Enjeu : le parallélisme sans dépense est libre ; le parallélisme des courses engage la dépense avant la porte et lit le
test final plusieurs fois.
(a) en parallèle tout le travail sans dépense (code des bras et essais R5, brouillons, banque v6), les courses échelon
par échelon — avantage : respecte ton principe ; inconvénient : 1 à 2 semaines. (b) échelons 2.1 à 2.4 ensemble —
avantage : rapide ; inconvénient : ≈ 1 650 à 3 100 USD avant de savoir si le séquentiel vaut quelque chose. (c) 2.1 et
2.3 ensemble — avantage : honore N-044 § 5 tôt ; inconvénient : + 400 à 760 USD avant la porte.
Recommandation : (a), confiance ≈ 70 %. Défaut sous 48 h : (a) pour l'ordre ; aucune course sans GO.

**D7 — Lignée(s) des comparaisons décisives.**
Enjeu : puissance par dollar contre généralité entre concepteurs.
(a) une lignée, choisie par une règle gelée avant toute lecture (la moins chère par appel — Opus couvre 408 appels au
plafond contre 163 pour Fable et Argon, v7 l. 275 — si sa mécanique passe la répétition) — avantage : puissance ;
inconvénient : rien sur les autres concepteurs. (b) trois lignées × 4 graines, appariées par lignée — avantage :
généralité ; inconvénient : + 20 % de courses, interaction lignée × bras dans le bruit. (c) trois lignées × 2 graines,
comme l'étape 1 — à écarter (≈ 20 % de puissance à +0,10, v9 l. 342–344).
Recommandation : (a) pour la porte, (b) ensuite si la porte passe, confiance ≈ 55 %. Défaut sous 48 h : (a).

**D8 — Forme de la récompense d'héritage (N-045 § 5, non décidée l. 115).**
Enjeu : sans elle, la mémoire et les instruments à effet différé ne comptent pas ; mal posée, elle brouille le signal.
(a) K = G = 3, un épisode par course : `historique` rend, pour chaque génération, la moyenne des scores de ses
successeurs dès qu'ils existent — avantage : simple, conforme ; inconvénient : un seul épisode complet par course. (b)
récompense actualisée sur t+1 à t+K, facteur gelé — avantage : plus fin ; inconvénient : un paramètre de plus. (c)
réservée au concepteur — avantage : rien à coder pour l'organisme ; inconvénient : contraire à « organisme ou concepteur ».
Recommandation : (a), confiance ≈ 50 %. Défaut sous 48 h : (a).

**D9 — GO de dépense de la phase décisive.**
Enjeu : c'est la plus grosse dépense de l'étape avant la voie chère.
(a) plan complet 2.0 à 2.4 (≈ 1 650 à 3 100 USD attendus) — avantage : tranche cinq ajouts ; inconvénient : coût. (b)
version réduite (≈ 515 à 1 010 USD) — avantage : tranche la porte au même écart minimal ; inconvénient : le reste
attend. (c) rien avant la banque v6 — avantage : test final neuf ; inconvénient : délai.
Recommandation : (b) sur la banque retenue en D1, confiance ≈ 65 %. Défaut : aucun — dépense : rien ne part.

## 5. Questions ouvertes et risques

- **Fuite de la vérité.** (1) Banque v1 : « les identifiants donnent la vérité » (`decisions.md` l. 667) ; l'étape 1 v9
  y est scellée (v9 l. 203) : l'étape 2 ne doit servir que la v5 ou suivante, avec la garde de séparation en code
  (BC5-02, `LISEZMOI-v9.md` l. 98–101). (2) Le fichier public de la banque porte la `verite` de chaque tâche du test et
  du test final (176 sur 176) : la vue de l'organisme ne doit jamais le contenir ; ce rapport ne l'a lu que pour compter
  les classes. (3) Garde des traits (BC5-01, l. 15–21) avant tout bras à sondes. (4) Moisson : le jeu public de conscience
  d'évaluation se trouve en ligne ; la garde CE3-04 refuse la recherche de provenance d'un texte de test, pas la recherche
  par thème. (5) Provenance → classe en conscience (BC5-03) : lire chaque score contre le maximum des références 0,8056 et
  0,8333 (l. 102–105). (6) Vivier disjoint aussi des 24 jumelles retirées de la v3 (l. 99–101). (7) Amorçage de la v5 :
  un seul exemple de délégation, honnête (BC5-04, l. 45–49) : règle écrite d'avance, égale entre bras.
- **Sondage du test par l'historique.** Le score de développement est rendu à chaque génération ; en délégation une
  erreur pèse 1/12 et le sondage adaptatif coûte deux fois moins (l. 110–114). B2 choisit sur ce même test (malédiction
  du gagnant) : seul le test final, lu une fois, décide. B3p mesure ce que l'apprentissage doit au contenu du signal.
  Question ouverte : rendre un score plus grossier ou sur une moitié tournante du test.
- **Coût dans le signal.** Récompense possible de l'inaction (une tâche sans réponse compte comme une erreur, v7 l. 88,
  mais un λ fort peut la rendre rentable) ; table des prix gelée au préenregistrement (v7 l. 26–27) ; prix de l'heure de
  carte des instruments locaux à fixer ; aujourd'hui `historique` ne rend que `cout_usd` et `n_appels` par génération
  (`contrat.py` l. 47).
- **Budget égal pour le meilleur de N** : plafonds égaux ou dépense réalisée égale ? Proposition : plafonds égaux, dépense
  réalisée rapportée en second axe.
- **Lectures répétées du test final** : chaque phase le lit ; soit un test final neuf par phase décisive (v6), soit une
  répartition du risque d'erreur gelée d'avance entre phases.
- **Dérive des conditions d'appel** : une dérive commune et de même taille aux deux courses était indiscernable de
  l'effet (v7 l. 77–79) ; le blocage par graine l'annule pour les bras d'un même bloc, pas entre blocs.
- **Bras de diversité** : « miroir fonctionnel » et « contrainte câblée » n'ont pas de définition écrite au-delà de
  N-044 l. 49–50 ; à écrire avant tout code.
- **Questions ouvertes aux organismes** (N-044 § 4) : égales entre bras, ou non posées dans les courses décisives comme
  à l'étape 1 (R-410).
- **Espaces de conception égaux** (N-045 § 7) : vaut dès qu'un bras contraint le format (B5c, B7).

## Écarts et réserves de ce rapport

- La routine de reprise du dépôt (R14) n'est pas appliquée : le brief interdit git, le réseau et toute écriture hors de
  `/var/tmp/etape2-proposition-v1/` ; seules les empreintes des pièces lues ont été vérifiées.
- σ et ρ sont des hypothèses ; les coûts viennent de pilotes sur la banque v3 ; rien n'est opposable (R7).
- Une alerte de précision de `scipy` (échantillons presque identiques, cellule σ = 0) pendant la simulation ; sans effet
  sur les taux rapportés.
- Le brief dit l'étape 1 « en révision (v10) » ; les copies ne contiennent que la v9 scellée.

## Pièces de ce dossier (chacune avec son `.sha256`)

| fichier | sha256 |
|---|---|
| `calcul-ecart-minimal-v1.py` | `c80f4ba25d1a22d50bf58e6cf48887919265173d1233b4a71981288ca11b449a` |
| `calcul-ecart-minimal-v1.json` | `7fcdfab9579dbb4b30ada21f4015e9822efc94ceb5fb459eaf58f58b8877da4f` |
| `LISEZMOI-v1.md` (ce fichier) | dans `LISEZMOI-v1.md.sha256` |
