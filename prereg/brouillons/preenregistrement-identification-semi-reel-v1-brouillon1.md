# Préenregistrement — épreuve semi-réelle des méthodes d'identification des causes de la fertilité (gradation 1 de R-633) — v1 — BROUILLON 1 (non gelé, non scellé)

**Statut.** Brouillon 1, écrit par conv-audit (Opus 5.5) le 30 octobre 2026, avant tout verdict du collisionneur sur la question 6 : il sera **révisé après ce verdict** (brouillon 2), puis contre-lu par un modèle différent d'Opus (règle R2), puis gelé par Lazar (seuils de la section « Seuil », aucun défaut de 48 heures), puis scellé par `sceller_prereg` **avant toute lecture des métadonnées moissonnées** (règle R1). Aucune méthode n'a été exécutée ; aucune donnée n'a été lue ; la moisson d'OpenAlex est en cours chez session-depot et n'est pas disponible pour l'auteur. Les seules grandeurs calculées sont des probabilités binomiales exactes et un ordre de grandeur de détection, sans tirage aléatoire (script cité plus bas). Chaque seuil porte le marqueur littéral du validateur : tant qu'il en reste un, `sceller_prereg` refuse de sceller.

## Résumé de dix lignes pour Lazar

1. **Ce que l'épreuve mesure.** On prend les vraies métadonnées d'OpenAlex (contrôle des intelligences artificielles et sous-domaines témoins), on y **plante une cause connue** de fertilité — un « contact » C entre deux niches qui ajoute, deux ans plus tard, des œuvres-ponts synthétiques —, et l'on regarde si chaque méthode retrouve C au milieu du vrai bruit, **sans jamais prétendre connaître les vraies causes**.
2. **Les pièges plantés.** Un facteur caché H (que les méthodes ne voient pas) qui crée lui aussi des ponts ; un **leurre** L (rendu plus probable par C et par H, sans effet) ; un **jumeau sans effet** C⁰ (même mécanisme d'affectation que C, tiré à part). Une méthode qui « trouve » L ou C⁰ se trompe, et on le sait.
3. **Trois affectations de C.** Au hasard (R), confondue par la popularité observée (O), confondue par le facteur caché (H) ; quatre tailles d'effet, dont **zéro** (contrôle de plomberie) ; 100 mondes par condition.
4. **Volet A (cause observée)** : popularité seule (témoin), prédicteur associatif (témoin), prédiction causale invariante, PCMCI, LiNGAM, plus un témoin d'artefact (tri par variance, Reisach 2021). **Volet B (cause latente)** : analyse en composantes indépendantes non linéaire avec variable auxiliaire (iVAE) contre **le même réseau sans variable auxiliaire** (contre-exemple libre), plus l'analyse en composantes principales.
5. **Verdict par méthode, écrit d'avance** : qualifiée pour les gradations 2 et 3, pour la gradation 3 seulement, détection seulement, non qualifiée (avec sa raison), ou non concluant.
6. **Mes paris (SUPPOSÉ)** : les méthodes qui supposent l'absence de facteur caché (PCMCI, LiNGAM, prédicteur associatif) retrouveront C mais **avaleront le leurre** ; la prédiction invariante sera prudente (abstentions) ; l'iVAE battra le réseau libre seulement quand la loi de la cause latente varie avec la variable auxiliaire. Chaque pari a son critère de mort.
7. **Ce qu'elle n'autorise pas** : aucune affirmation sur les vraies causes de la fertilité ; seulement l'entrée (ou non) de chaque méthode dans les gradations 2 (expériences naturelles) et 3 (nos courses).
8. **Coût** : processeur seul, aucune dépense, aucun appel de modèle ; environ 1 600 mondes, 72 heures au plus (SUPPOSÉ), règle de réduction écrite d'avance.
9. **Ordre** : verdict du collisionneur → brouillon 2 → contre-lecture (Fable ou Sonnet) → gel par Lazar → scellement → code et gardes sur base jouet → seulement alors première lecture de la moisson.
10. **Pour geler** : seize seuils S1 à S16, récapitulés en fin de section « Seuil », chacun avec ma recommandation et sa raison ; trois choix vraiment ouverts : S3 (tailles d'effet), S8 (plafond de paires par environnement) et S9 (exigence de recouvrement).

### Nœuds ouverts avant scellement

1. **Verdict du collisionneur sur la question 6** (pièce n° 264) : attendu ; le brouillon 2 l'intègre (méthodes ajoutées ou retirées, critères de mort, épreuve d'intervention).
2. **Manifeste de la moisson** (session-depot, n° 265) : liste des environnements, règle de sélection du sous-domaine du contrôle des intelligences artificielles, champs, date de l'instantané. Il doit être cité par chemin et empreinte au scellement ; son **contenu chiffré** (nombre d'œuvres, de niches, de citations) ne doit pas être lu avant le scellement. La moisson elle-même n'est pas une lecture ; vérifier son empreinte, son schéma et son nombre de fichiers n'en est pas une non plus.
3. **Seuils S1 à S16** : à geler par Lazar en une ligne datée de `registres/decisions.md` ; aucun défaut ne s'applique.
4. **Bibliothèques** (décision de routine) : `tigramite` (PCMCI), `lingam` (LiNGAM), `scikit-learn` (témoins), versions figées au manifeste ; à défaut d'accès au dépôt de paquets, réimplémentation dans `src/` avec essais R5 contre les sorties publiées des exemples de ces bibliothèques.

- Auteur : conv-audit, Opus 5.5 (`claude-opus-5-5`). **Ne peut pas être contre-lecteur** de ce texte ni de ses versions suivantes.
- Date (UTC), relevé `date -u` : début 2026-10-30T20:53Z ; fin de rédaction 2026-10-30, voir l'empreinte compagnon.
- Commit du code d'analyse : aucun code à ce jour ; le code s'écrit **après** scellement ; son empreinte et son commit vont au manifeste de chaque run (R9).
- Non lus : tout `donnees/` ; la moisson (indisponible) ; aucune commande git, aucun réseau, aucune dépense.
- Documents qui font foi (empreintes SHA-256 calculées par l'auteur le 2026-10-30 ; chemins des pièces relatifs à `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/bisociation-niches-v1/`) :
  - `question-6-identification-collisionneur-v1.md` `14966d0d2ffdea9de94b924a6ad661b440eae1bb2db865b81fd0eb75e6d71b73` (lue) ;
  - `reponse-conv-audit-question-6-v1.md` `afdb9f9dbf9ed8a837d20962eb815e4eea817454dc296440a743123769ef00bf` (lue ; épreuve (d) de la question : mondes à causes connues puis intervention jamais vue) ;
  - `reponse-conv-audit-question-5-v1.md` `a47ba91677ee9f3138e65c2fae7f997436ca80e2ad8a73454609ba8e58ae0442` (lue) ;
  - `reponse-fable-independante-question-5-v1.md` `9170d230aca80767b6ba0e3b55814f9e1cce0544a3c76e6fceb79b48cd409148` (lue ; point (4)1 : « un paramètre qui cause et un qui accompagne ») ;
  - `relecture-fable-reponse-5-v1.md` `77a48dd23c772992cc48fd9cc7c6032336ddd04a09549cfd5638f73b6bd0cb3a` (lue ; RL5-01 hypothèses non testables à écrire, RL5-03 ordre des variances, RL5-08 critère de mort chiffré, ligne de base et témoin négatif, RL5-11 transport, RL5-17 décennies comme environnements) ;
  - `reponse-conv-audit-question-3-v1.md` `c7ca393513ed1ffd443f622f8ee8eb64d7766cbc34a177c3a64d61b3f80f4f47` et `reponse-conv-audit-question-4-v1.md` `69ca070747e5a3a7fb64935d32e631fb45fe1aafd5e0ef82376df0b0e90db927` (lues ; définition de la fertilité par effets différés ; fuites temporelles, survivants, effet Matthieu) ;
  - `question-2-niches-v1.md` `4378f9a8abea025d473c4315419515a82c12a238f349bad51b6c08e80c631c14`, `question-3-fertilite-v1.md` `2ad43f6972951abb90ae49447fd887d5f65d3dacb552ca7454ca2c0c5027b06a`, `question-4-apprendre-v1.md` `d051c7bdce39c809465b6d227ca1869eff3afc38f1594c0a8ad6be041113be09`, `question-5-causes-v1.md` `8dfc74a332de814764aab1fd25e7a92791c51addcd4ae0a357e5d1cdb8354ee7` (lues) ;
  - `docs/programme-controle-ia-v2.md` `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` (cité : E1.4, « théorème négatif en semi-synthétique : scores honnêtes réels + structure de corrélation injectée à marginale préservée » — même logique de plantation sur données réelles) ;
  - `prereg/gabarit-preregistrement-v1.md` `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`, `src/controle_ia/prereg.py` `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` (lus) ;
  - `prereg/preenregistrement-bisociation-deux-espaces-v2.md` `e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea` (modèle de forme, lu en partie : en-tête, hypothèse, prédiction, seuils S1 et S2, plan d'analyse § 6 à § 10, critères, liste d'arrêt, contre-lecture) ;
  - `registres/decisions.md` (fichier vivant, `035762a84ce723fd7062eae25103aaeb312e4c7b355abd01577ef8856161f668` à la lecture) : **R-631** (trois gradations proposées : semi-synthétique, réel avec expériences naturelles, réel avec nos courses) ; **R-633** (Lazar, 21:44 heure de Paris, mot direct : « go » sur les trois gradations ; « (1) semi-réel (OpenAlex + cause plantée), processeur, sans dépense » ; OpenAlex non joignable d'ici, moisson demandée à session-depot, n° 265 ; « scellement avant toute lecture (R1), après le verdict du collisionneur sur la question 6 ») ;
  - script de calcul `prereg/brouillons/calcul-regles-identification-semi-reel-v1-brouillon1.py` `474a45d984d56f53482c8e36018bf58eca518762d52b94890ae5dcf62f150358` et sa sortie `prereg/brouillons/calcul-regles-identification-semi-reel-v1-brouillon1-sortie.txt` `eb3922a0736216f16f70d50ada1153c9399d84571a2d9bea479951b5f41942a9` (écrits pour ce brouillon ; loi binomiale exacte, intervalles de Wilson, sans tirage ; **source des probabilités marquées (M)** ; sortie reproductible au bit près).
- Références de littérature : toutes **citées de mémoire, SUPPOSÉ** (règle R7 : aucun chiffre de la littérature n'est utilisé ; seuls des noms de méthodes et de théorèmes). Reisach, Seiler et Weichwald 2021 est « vérifiée en existence » par la relecture 5 (page arXiv lue en session, sans PDF empreinté).

## Hypothèse

**Énoncé d'ensemble (H-SR).** L'identification d'une cause n'est pas une propriété de l'algorithme mais du couple « données + hypothèses » (position de la réponse 6). Sur une base réelle de métadonnées d'OpenAlex où l'on plante une cause connue de fertilité au milieu du vrai bruit, chaque méthode retrouve la cause plantée **si et seulement si** l'hypothèse dont dépend son théorème d'identifiabilité est satisfaite par la plantation, et elle se trompe (leurre, jumeau) là où cette hypothèse est violée. Renvoi : R-631 et R-633 (gradation 1) ; programme v2, E1.4 (même logique semi-synthétique) ; questions 5 et 6 et leurs réponses (documents cités en tête).

**Objet mesuré.** Pour une paire de niches (i, j) d'un même environnement et une année t, la fertilité est approchée par le nombre d'**œuvres-ponts** : œuvres publiées en t dont les références contiennent au moins une œuvre de i et au moins une œuvre de j (définition opératoire au plan d'analyse, § 2). C'est un indicateur, pas la fertilité au sens de la question 3 (cascade reprise) : la cause plantée agit sur l'indicateur, et l'épreuve ne dit rien de plus (RL5-13).

**Monde planté (écrit, connu, jamais lu par une méthode).**
- (W1) Une **cause plantée observée** C (« contact ») : pour une paire-année traitée, des œuvres-ponts synthétiques s'ajoutent ℓ années plus tard, en nombre tiré d'une loi de Poisson de moyenne β·σ_e (β en écarts-types de la sortie réelle de l'environnement e) ; effet **invariant entre environnements** par construction (sauf condition descriptive D1).
- (W2) Un **facteur caché planté** H, propre à chaque paire, jamais transmis aux méthodes, qui ajoute chaque année des œuvres-ponts (moyenne η·σ_e·2Φ(H)) ; il confond C seulement dans l'affectation H.
- (W3) Un **leurre** L, observé : sa probabilité monte avec C et avec H ; il n'a aucun effet. Il est donc corrélé à C **et** prédit la sortie au-delà de C (par H) : un prédicteur le retient, une méthode causale doit l'écarter. L est un **collisionneur** entre C et H : conditionner sur L ouvre le chemin C → L ← H → sortie.
- (W4) Un **jumeau sans effet** C⁰, observé : même mécanisme d'affectation que C (au hasard, par la popularité, ou par H), tiré indépendamment, aucun effet. C'est le placebo apparié de chaque monde (effet Matthieu sous O, confusion cachée sous H).
- (W5) Volet B seulement : une **cause latente plantée** Z, continue, jamais observée ; les méthodes voient K indicateurs, mélange non linéaire de Z et des covariables réelles ; Z ajoute des œuvres-ponts ; la loi de Z varie (Bv) ou non (Bc) avec la variable auxiliaire u (environnement × bloc de cinq ans).
- Tout le reste — les vraies œuvres, les vraies citations, les vraies niches, la vraie popularité, les vraies causes inconnues de la sortie réelle — est le **vrai bruit**. Aucune variable réelle n'est jamais notée « cause » ou « non-cause » : on ne note les méthodes que sur C, L, C⁰ et Z.

### Hypothèses rivales gelées, méthode par méthode

Les prédictions chiffrées sont à la section suivante ; ici, l'hypothèse dont dépend chaque méthode et ce qu'elle devrait faire dans ce monde.

| Code | Méthode | Hypothèse d'identification (SUPPOSÉ, de mémoire) | Satisfaite par la plantation ? | Rivale gelée |
|---|---|---|---|---|
| T0 | Popularité seule : régression de Poisson pénalisée et réseau à deux couches, entrées = covariables réelles de popularité (taille, degré, âge, pont présent) | aucune (prédiction pure) | sans objet : C n'est pas une entrée | **HR-T0** : ne retrouve jamais C (par construction) ; prédit un effet d'intervention nul ; c'est le plancher et le contrôle de plomberie |
| T1 | Prédicteur associatif : forêt d'arbres par gradient (`scikit-learn`), toutes les variables candidates, importance par permutation | aucune (association) | sans objet | **HR-T1** : retrouve C, **mais retient aussi le leurre L** (sous R, O et H) et le jumeau C⁰ sous H ; son effet estimé est biaisé (collisionneur L ; confusion H) |
| T2 | Tri par variance puis régression pénalisée en norme 1 (« sortnregress », Reisach, Seiler et Weichwald 2021, « Beware of the simulated DAG! ») | l'ordre causal suit l'ordre des variances marginales | non (artefact connu) | **HR-T2** : témoin d'artefact ; réussit en échelle brute si l'ordre des variances suit l'ordre causal, s'effondre en échelle standardisée |
| M1 | Prédiction causale invariante (Peters, Bühlmann et Meinshausen 2016, *Journal of the Royal Statistical Society B*), version linéaire | la loi de la sortie sachant ses vraies causes est la même dans tous les environnements ; pas de facteur caché entre candidates et sortie ; les environnements déplacent la loi des candidates | partiellement : l'effet planté est invariant et l'affectation de C varie entre environnements ; **le vrai bruit peut ne pas l'être** (normes de citation par sous-domaine et par décennie, RL5-17) ; H viole l'hypothèse sous l'affectation H | **HR-M1** : n'inclut presque jamais L ni C⁰ (garantie de niveau) ; retrouve C seulement si la partie réelle est assez invariante ; **s'abstient** (ensemble vide) sous confusion cachée |
| M2 | PCMCI (Runge, Nowack, Kretschmer, Flaxman et Sejdinovic 2019, *Science Advances* : étape « PC » de sélection des conditions, du nom de Peter Spirtes et Clark Glymour, puis test d'indépendance conditionnelle momentanée), corrélation partielle, retards 1 à τ_max | suffisance causale (aucun facteur caché), stationnarité, fidélité, ordre temporel | ordre temporel oui ; **suffisance causale non** (H) ; stationnarité douteuse sur données réelles | **HR-M2** : retrouve C au bon retard ; **déclare L → sortie** (dépendance résiduelle par H, détectable à grand échantillon) ; déclare C⁰ sous H |
| M3 | LiNGAM, modèle linéaire acyclique non gaussien (Shimizu, Hoyer, Hyvärinen et Kerminen 2006 ; version directe, Shimizu et collègues 2011) | linéarité, bruits non gaussiens indépendants, acyclicité, aucun facteur caché | non-gaussianité oui (binaires, comptes) ; linéarité non (variables binaires enfants) ; **aucun facteur caché : non** | **HR-M3** : oriente C → sortie avec le bon signe sous R et O ; **retient L** et, sous H, C⁰ ; erreurs d'ordre causal fréquentes |
| M4 | Analyse en composantes indépendantes non linéaire avec variable auxiliaire : autoencodeur variationnel identifiable, iVAE (Khemakhem, Kingma, Monti et Hyvärinen 2020) ; famille de Hyvärinen et Morioka 2016 | sources conditionnellement indépendantes sachant u ; **variabilité suffisante** de leur loi selon u ; mélange injectif | pour Z : **oui en Bv, non en Bc** (par construction) ; pour les covariables réelles : non (dépendantes entre elles) | **HR-M4** : retrouve Z (corrélation ≥ 0,70) dans la plupart des mondes Bv, de façon stable entre graines ; en Bc, pas mieux que le réseau libre |
| M5 | **Contre-exemple libre** : le même autoencodeur variationnel que M4, loi a priori normale standard, **sans** variable auxiliaire | aucune (Locatello et collègues 2019 : démêlage non supervisé impossible sans biais inductif ; Hyvärinen et Pajunen 1999 : analyse en composantes indépendantes non linéaire non identifiable) | non | **HR-M5** : ne retrouve pas Z de façon stable ; ses premiers facteurs captent la popularité (taille, degré, âge) |
| T3 | Analyse en composantes principales sur les indicateurs du volet B | l'ordre des variances porte la structure | non (témoin de variance) | **HR-T3** : témoin ; retrouve Z seulement si Z domine la variance du mélange |

Méthode d'estimation sous identification acquise (forêts causales, réseaux à deux têtes, apprentissage double orthogonalisé) : **hors de ce brouillon** ; elles estiment un effet déjà identifié et relèvent des gradations 2 et 3 (RL5-18).

### Ce que l'épreuve n'autorise pas (écrit d'avance)

- **Aucune affirmation sur les vraies causes de la fertilité**, ni sur le rôle réel de la popularité, de l'âge, du sous-domaine ou de toute variable réelle. Les sorties des méthodes sur les variables réelles sont rapportées comme des descriptions de ce que la méthode dit, jamais comme des constats.
- Aucune généralisation hors de la base moissonnée : les mondes partagent **une seule réalisation** du vrai bruit ; la variabilité estimée est celle de la plantation, pas celle des bases possibles.
- Aucun transport vers la science réelle (RL5-11) : une méthode « qualifiée » l'est **pour ce mécanisme planté** (effet additif sur les œuvres-ponts, au retard ℓ, invariant) ; une vraie cause peut avoir une autre forme.
- La qualification n'autorise que l'**emploi de la méthode dans un préenregistrement distinct** de la gradation 2 (expériences naturelles publiées comme vérité) ou 3 (nos courses randomisées, après la course 2). Elle n'autorise ni production, ni revendication, ni dépense, ni changement de modèle.
- Un échec n'est pas « la méthode est fausse » : c'est « la méthode n'identifie pas ce mécanisme dans ce bruit ».
- Antériorité (R8) : la plantation d'effets connus dans des données réelles est une pratique établie (Hill 2011, données dites IHDP ; Dorie et collègues 2019, concours d'inférence causale dit ACIC ; Neal, Huang et Raghupathi 2020, « RealCause » ; pour les séries temporelles, la plateforme CauseMe de Runge et collègues 2019 — tous SUPPOSÉ). **La méthode n'est pas revendiquée comme inédite** ; seule son application à la fertilité entre niches scientifiques pourrait l'être, question à vérifier avant toute revendication.

## Prédiction chiffrée et signe attendu

Toutes les grandeurs sont des **paris de l'auteur, SUPPOSÉS, sans aucune donnée** (aucune version précédente, aucune lecture de la moisson). Elles servent à rendre chaque méthode réfutable ; **le verdict ne lit que les seuils S1 à S16**. Une prédiction de grandeur hors fourchette est rapportée comme « prédiction de grandeur réfutée », sans effet sur les tables de lecture. Les sigles R, O, H désignent l'affectation de C ; les indices 0 à 3 la taille d'effet (β = 0, faible, moyen, fort ; S3). « Recouvrement » = part des mondes où la méthode déclare C cause avec le bon signe ; « erreur L » (« erreur C⁰ ») = part des mondes où elle déclare L (C⁰) cause ; « erreur C » = part des mondes β = 0 où elle déclare C cause ; « erreur d'intervention » = erreur relative de l'effet prédit d'une intervention jamais vue (Métrique). Confiance = probabilité, selon l'auteur, que la ligne se réalise.

### Volet A — cause observée

| # | Méthode | Recouvrement (R2, R3, O2, O3) | Erreur C (β = 0) | Erreur L | Erreur C⁰ | Signe et grandeur de l'effet ; intervention | Rang de C parmi {C, L, C⁰} | Critère de mort de la rivale | Confiance |
|---|---|---|---|---|---|---|---|---|---|
| PA-T0 | T0 | 0 partout (par construction) | 0 | 0 | 0 | effet prédit nul ; erreur d'intervention = 1,00 exactement | dernier (absent) | une importance non nulle de C, ou un effet prédit non nul : **erreur de plomberie** (arrêt) | 1,00 |
| PA-T1 | T1 | 0,85 à 1,00 au moyen et au fort ; 0,3 à 0,8 au faible | R0 : 0,02 à 0,10 ; O0 : 0,05 à 0,20 ; **H0 : 0,4 à 0,9** | **0,3 à 0,9 sous R, O et H** (L prédit par H) | R : ≤ 0,10 ; O : 0,05 à 0,25 ; **H : 0,4 à 0,9** | signe + ; sous R biais vers le bas (collisionneur L), sous H vers le haut ; erreur d'intervention médiane 0,2 à 0,6 | C premier dans 0,6 à 0,9 des mondes, L devant C sinon | erreur L regroupée sous R ≤ 0,10 (le prédicteur ne confond pas le leurre) : HR-T1 morte ; le leurre est alors **non jugeable** (Table A, J_L) | 0,70 |
| PA-T2 | T2, échelle brute | 0,4 à 0,9 (si les variables binaires ont une variance plus faible que la sortie) | 0,05 à 0,30 | 0,3 à 0,9 | 0,05 à 0,5 | signe + ; grandeur non lue | sans objet | — (témoin) ; **échelle standardisée : recouvrement ≤ 0,3** ; s'il tient au-dessus de 0,5 en standardisé, l'ordre des variances n'explique pas le témoin (rapporté) | 0,60 |
| PA-M1 | M1 | **0,2 à 0,8** (incertitude principale : invariance de la partie réelle) ; au fort ≥ au moyen | ≤ 0,05 sous R et O ; ≤ 0,10 sous H | ≤ 0,05 partout | ≤ 0,05 sous R et O ; ≤ 0,10 sous H | quand C est retenu : signe + et erreur d'intervention ≤ 0,3 sous R et O ; **abstention (ensemble vide) dans 0,5 à 1,0 des mondes H2 et H3** | C seul retenu, ou rien | erreur L ou erreur C⁰ au-delà de S9 (garantie de niveau rompue par le vrai bruit) : HR-M1 morte, M1 « se trompe » ; recouvrement sous S9 : M1 « trop prudente » (non qualifiée, rivale tenue sur son versant prudent) | 0,55 (que la rivale tienne) ; 0,30 (que M1 soit qualifiée) |
| PA-M2 | M2 | **0,85 à 1,00** au moyen et au fort, au bon retard ℓ | R0, O0 : ≤ 0,05 ; **H0 : 0,3 à 0,9** | **0,3 à 0,9** (dépendance résiduelle par H, malgré le passé de la sortie) | R, O : ≤ 0,10 ; **H : 0,3 à 0,9** | signe + ; erreur d'intervention ≤ 0,3 sous R et O quand le retard est juste | C premier | erreur L regroupée sous R et sous O ≤ 0,10 (le passé de la sortie absorbe H) : HR-M2 morte ; M2 peut alors être qualifiée | 0,60 |
| PA-M3 | M3 | 0,6 à 0,95 sous R et O | R0 : ≤ 0,10 ; H0 : 0,3 à 0,9 | **0,3 à 0,8** | H : 0,3 à 0,8 | signe + ; grandeur biaisée (variables binaires hors du modèle linéaire) ; erreur d'intervention 0,2 à 0,6 | C premier dans 0,5 à 0,9 des mondes | erreur L ≤ 0,10 sous R et O, et recouvrement selon S9 : HR-M3 morte ; résultats qui changent avec l'échelle (au-delà de S12) : artefact | 0,55 |

### Volet B — cause latente

| # | Méthode | Corrélation maximale avec Z (part des mondes ≥ 0,70) | Rang du facteur apparié parmi les facteurs appris (choix sans vérité : plus fort coefficient sur la sortie) | Stabilité entre deux graines d'entraînement (médiane) | Signe de l'effet retrouvé (Bv1) ; fausse détection (Bv0) | Captation de la popularité (corrélation maximale d'un facteur avec la taille ou le degré) | Critère de mort de la rivale | Confiance |
|---|---|---|---|---|---|---|---|---|
| PB-M4 | M4 (iVAE) | **Bv : 0,70 à 0,95** ; Bc : comme M5 (écart < 0,15) | premier dans 0,5 à 0,9 des mondes Bv1 | Bv : 0,75 à 0,95 | signe aligné + dans ≥ 0,9 des mondes Bv1 ; fausse détection ≤ 0,10 en Bv0 | 0,3 à 0,7 | part sous la borne de S11 en Bv, ou stabilité médiane < 0,70 : HR-M4 morte (« la variable auxiliaire ne suffit pas sur base semi-réelle ») ; avantage persistant en Bc (contrôle) : l'avantage ne vient pas de l'hypothèse | 0,50 |
| PB-M5 | M5 (réseau libre) | Bv et Bc : **0,1 à 0,5** | premier dans ≤ 0,4 des mondes | 0,3 à 0,6 | signe aligné + dans 0,5 à 0,9 des mondes Bv1 (quand Z est en partie capté) | **≥ 0,6** (ses facteurs principaux sont la popularité) | en Bv, part ≥ seuil de S11, stabilité ≥ 0,70 et écart M4 − M5 < 0,15 : **la thèse « pas à lui seul » est réfutée dans ce monde** (issue permise, nommée ; déclenche l'audit R4 « trop beau ») | 0,60 |
| PB-T3 | T3 (composantes principales) | 0,0 à 0,4 | sans objet | 1,00 (déterministe) | sans objet | ≥ 0,7 | — (témoin de variance) ; si T3 égale M4, l'identification de M4 vient de la variance, non de la variable auxiliaire (audit) | 0,60 |
| PB-Δ | écart apparié M4 − M5 de corrélation avec Z | **Bv : +0,15 à +0,50 ; Bc : −0,10 à +0,10** | — | — | — | — | Bv : borne basse ≤ 0 ou estimation < 0,15 : avantage de la variable auxiliaire non démontré | 0,50 |

**Prédictions transversales (signe seul, descriptives).** (i) Le recouvrement croît avec β pour toute méthode candidate (pente positive) ; une pente nulle ou négative est rapportée. (ii) Sous O, les erreurs C⁰ des méthodes linéaires sont plus fortes dans le tiers supérieur de popularité (effet Matthieu résiduel, ajustement linéaire incomplet). (iii) En D2 (H sans effet sur la sortie), les erreurs L et C⁰ de T1, M2 et M3 retombent au niveau nominal : c'est la preuve que leur erreur sous H vient de H, pas d'un défaut de code. (iv) En D1 (effet planté non invariant), M1 s'abstient plus souvent qu'en R2 ; M2 et M3 n'en sont pas affectées en moyenne.

**Verdicts attendus (SUPPOSÉ), écrits d'avance.** T1, M2, M3 : « non qualifiées : confondent le leurre » (Table A, ligne 5) avec la confiance 0,6 ; M1 : « non qualifiée : ne retrouve pas » (ligne 7) ou « qualifiée, prudente » (ligne 12), sans préférence nette ; volet B : « oui sous hypothèse » (Table B, ligne 9) avec la confiance 0,45. **Si toutes les méthodes du volet A sont non qualifiées**, la conclusion écrite d'avance est : « aucune méthode d'observation pure n'identifie ce mécanisme dans ce bruit ; les gradations 2 et 3 doivent apporter l'affectation (expérience naturelle, randomisation) », jamais « la fertilité n'a pas de cause identifiable ».

## Métrique

**Unité de réplication** : le monde, c'est-à-dire une plantation complète (graines du § 8) sur la même base réelle. **Ensemble d'ajustement** : les paires retenues (au plus le plafond S8 par environnement, tirage unique par monde) et toutes leurs années de la fenêtre de plantation. **Ensemble d'intervention** I : défini par S16, tenu hors de l'ajustement.

**Sortie.** Y_ij,t = nombre d'œuvres-ponts de l'année t pour la paire (i, j) dans la base plantée ; Y⁺_ij,t = Y_ij,t+1 + … + Y_ij,t+τ_max (sortie cumulée, pour les méthodes en coupe : T0, T1, T2, M1, M3) ; échelle d'analyse g(·) = log(1 + ·). PCMCI (M2) lit la série g(Y_ij,t) avec ses retards.

**Variables candidates du volet A** (identiques pour toutes les méthodes, dans cet ordre) : C_t, L_t, C⁰_t (plantées, binaires) ; S_t (taille), D_t (degré entrant), A_t (âge), g(Y_t) (pont présent) (réelles, § 2). H n'est **jamais** transmis.

**Décision par méthode** (d_M(V) ∈ {cause, non-cause}) et **score causal** s_M(V), fixés d'avance (hyperparamètres au § 5) :
- T0 : C, L, C⁰ absents ; d = non-cause pour eux.
- T1 : d = cause si l'importance par permutation de V dépasse celle d'une sonde de bruit pur (variable normale ajoutée) dans au moins 9 répétitions sur 10, sur plis tenus à l'écart ; signe = signe de la différence moyenne de prédiction entre V = 1 et V = 0.
- T2 : d = cause si V précède la sortie dans l'ordre des variances et si son coefficient pénalisé est non nul ; signe = signe du coefficient.
- M1 : d = cause si V appartient à l'ensemble estimé Ŝ au niveau α_M1 (S8) ; Ŝ vide = **abstention** ; signe = signe du coefficient de V dans la régression de g(Y⁺) sur Ŝ.
- M2 : d = cause s'il existe un retard τ ∈ [1, τ_max] tel que le lien V_t−τ → g(Y)_t soit significatif au niveau α_M2 (S8) ; signe = signe de la corrélation partielle au retard le plus fort.
- M3 : d = cause si V précède la sortie dans l'ordre causal estimé et si son effet total estimé sur g(Y⁺) est d'au moins 0,05 en valeur absolue (variables standardisées) ; signe = signe de l'effet total.

**Issues par monde et par méthode** (pour C, L, C⁰) : « trouve » = d(C) = cause et signe positif ; « s'abstient » = aucune variable plantée déclarée (pour M1 : Ŝ ne contient ni C, ni L, ni C⁰) ; « se trompe sur V » = d(V) = cause pour V ∈ {L, C⁰}, ou d(C) = cause en monde β = 0, ou d(C) = cause avec signe négatif.

**Taux** (par méthode et condition, sur les mondes non exclus) : recouvrement = part de « trouve » ; erreur C = part de « d(C) = cause » en β = 0 ; erreur L, erreur C⁰ = parts de « se trompe sur L », « sur C⁰ », **regroupées par affectation** (R, O ou H : 400 mondes, les quatre tailles d'effet) ; abstention = part de « s'abstient ». Intervalles : **Wilson à 95 %** (borne basse BB, borne haute BH).

**Vérité de l'effet et intervention jamais vue.** Pour chaque monde, le code calcule l'effet vrai par **simulation contrefactuelle à nombres aléatoires communs** (§ 8, rôle 10) : τ*_I = moyenne sur I de [g(sortie sous do(C = 1)) − g(sortie sous do(C = 0))], sur l'échelle et aux retards de la sortie de chaque méthode (g(Y⁺) pour les méthodes en coupe ; somme sur les retards 1 à τ_max de g(Y_t+τ) pour M2). Chaque méthode prédit τ̂_I : M1, le coefficient de C (0 si C ∉ Ŝ) ; M2, la somme des coefficients linéaires des liens C → sortie détectés (0 sinon) ; M3, l'effet total ; T1, la moyenne sur I de la différence de prédiction entre C = 1 et C = 0 ; T2, son coefficient ; T0, 0. **Erreur d'intervention** e_I = |τ̂_I − τ*_I| / |τ*_I| (mondes β > 0) ; résumé par condition : médiane, intervalle à 95 % par 2 000 rééchantillonnages des mondes.

**Volet B.** Sur 20 % des paires-années tenus à l'écart de l'entraînement : r_Z = maximum sur les dimensions apprises k de |ρ_S(Z, ẑ_k)| (corrélation de rangs de Spearman) ; k* = la dimension qui l'atteint ; **rang de k*** parmi les d dimensions, classées sans la vérité par la valeur absolue de leur coefficient dans la régression aux moindres carrés ordinaires de g(Y⁺) sur toutes les dimensions et sur S, D, A, g(Y) ; **stabilité** = maximum sur k' de |ρ_S(ẑ¹_k*, ẑ²_k')| entre deux graines d'entraînement (sans la vérité) ; **captation de la popularité** = maximum sur k de |ρ_S(ẑ_k, S)| et |ρ_S(ẑ_k, D)| ; **effet retrouvé** = signe aligné du coefficient de ẑ_k* (signe du coefficient × signe de ρ_S(ẑ_k*, Z), le signe d'un facteur latent n'étant identifiable par aucune méthode) dans la régression de g(Y⁺) sur ẑ_k* et S, D, A, g(Y), au seuil bilatéral 0,01 ; en Bv0, « fausse détection » = coefficient significatif au seuil 0,01, quel qu'en soit le signe. Écart apparié M4 − M5 de r_Z par monde ; intervalle à 95 % par rééchantillonnage des mondes.

**Artefacts (mesures, § 6 du plan)** : ordre des variances et ordre des coefficients de détermination du sous-graphe planté ; recouvrement en échelles brute, standardisée et redimensionnée ; recouvrement et erreurs par tiers de taille, de degré et d'âge.

**Mondes exclus.** Un monde est exclu pour toutes les méthodes à la fois si, **avant toute méthode**, il compte moins de 50 paires-années traitées dans l'ensemble d'ajustement, ou si sa simulation contrefactuelle échoue. Taux d'exclusion rapporté ; au-delà de 2 % dans une condition de décision : arrêt.

## Seuil

**Tous les seuils de ce préenregistrement sont des marqueurs de gel. Lazar les gèle en une ligne datée dans `registres/decisions.md` ; aucun défaut ne s'applique, ni à 48 heures ni autrement.** Pour chaque seuil : la valeur (marqueur), la recommandation de l'auteur, sa raison. Une recommandation n'est pas une valeur.

**S1 — Niches et paires**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : niche = **thème principal OpenAlex** (« primary topic ») de l'œuvre, à l'intérieur de son environnement ; niche retenue si elle compte au moins **30 œuvres** publiées avant la première année du panel ; paires = paires non ordonnées de niches retenues d'un même environnement (pas de paire entre environnements).
- Raison : étiquette externe, déterministe, posée avant nous, donc sans degré de liberté d'analyste ; 30 œuvres donnent une sortie non dégénérée. Réserve : le classifieur d'OpenAlex est récent et peut porter une fuite temporelle (SUPPOSÉ) ; la condition descriptive D3 (communautés de Leiden sur le couplage bibliographique de la période de référence, résolution 1,0) mesure la sensibilité au découpage.

**S2 — Calendrier**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : panel = années complètes de la moisson moins les **deux dernières** (indexation incomplète), au plus 20 années ; **période de référence** = les 5 premières années du panel (calcul de σ_e, de la popularité standardisée ; aucune plantation) ; **fenêtre de plantation** = de la 6e année à la dernière moins τ_max ; **retard planté ℓ = 2 ans** ; **retard maximal transmis aux méthodes τ_max = 3**.
- Raison : ℓ = 2 est l'ordre de grandeur du délai de publication puis de citation (SUPPOSÉ) ; τ_max > ℓ laisse aux méthodes de quoi se tromper de retard ; les deux dernières années sont incomplètes dans toute base bibliographique (SUPPOSÉ).

**S3 — Tailles d'effet et forme (choix vraiment ouvert)**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : **β ∈ {0 ; 0,1 ; 0,2 ; 0,4}** en écarts-types σ_e de la sortie annuelle réelle de l'environnement (période de référence), effet **additif** (loi de Poisson de moyenne β·σ_e par paire-année traitée, au retard ℓ) ; β = 0 est le contrôle de plomberie (R5). La forme multiplicative est descriptive (D4).
- Raison : en unités d'écart-type, la détectabilité ne dépend pas de la rareté des ponts ni de leur surdispersion, inconnues avant lecture ; ordre de grandeur (M, script § 8, approximation normale, 30 000 paires-années dont 10 % traitées, sortie cumulée sur 3 ans) : statistique de test attendue 3,0 (β = 0,1, « faible » : recouvrement partiel attendu), 6,0 (β = 0,2, « moyen ») et 12,0 (β = 0,4, « fort »). L'additif évite de planter un effet Matthieu (un effet proportionnel à la taille rendrait la détection plus facile chez les grandes niches par construction). Autre option : {0 ; 0,2 ; 0,4 ; 0,8}, plus facile, moins informative sur la limite de détection.

**S4 — Affectation de C (et de C⁰)**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : probabilité de base π_0 = 0,10 par paire-année, multipliée par κ ∈ {0,5 ; 1 ; 1,5}, attribué cycliquement aux couples (environnement, bloc de cinq ans) ; R : logit π = logit(π_0 κ) ; O : + γ_O × popularité standardisée (somme standardisée de S et D, dans l'environnement et l'année), **γ_O = 1,0** ; H : + γ_H × H, **γ_H = 1,0**.
- Raison : les décalages κ sont le « décalage de mécanisme » dont la prédiction invariante a besoin, sans toucher l'effet ; γ = 1 (un écart-type multiplie la cote par e ≈ 2,7) donne une confusion nette sans séparer complètement traités et non traités.

**S5 — Facteur caché et leurre**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : H ~ normale standard par paire, constant dans le temps ; effet de H : loi de Poisson de moyenne **η·σ_e·2Φ(H)**, **η = 0,4**, chaque année du panel postérieure à la référence ; leurre : logit P(L = 1) = **−3 + 2,5·C + 1,0·H**.
- Raison : η = 0,4 rend H aussi fort que l'effet « fort » de C, ce qui donne au leurre un pouvoir prédictif réel ; les coefficients du leurre donnent P(L = 1) ≈ 0,05 sans contact et ≈ 0,38 avec (à H = 0), donc une corrélation nette avec C et avec H. La jugeabilité du leurre est **mesurée** (J_L), non supposée.

**S6 — Volet B**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : K = 8 indicateurs = réseau aléatoire fixé par monde (deux couches cachées de 16 unités, pente négative 0,2 de la fonction « leaky ReLU », poids orthogonaux) appliqué à (Z, S, D, A, g(Y⁰)) standardisés, plus un bruit normal d'écart-type 0,1 ; Bv : Z | u ~ normale de moyenne μ_u ~ uniforme(−2 ; 2) et d'écart-type σ_u ~ uniforme(0,5 ; 2), tirés par monde ; Bc : Z ~ normale standard pour tout u ; effet de Z : Poisson de moyenne β_Z·σ_e·2Φ(Z) au retard ℓ, **β_Z ∈ {0 ; 0,4}** ; dimension apprise d = 6.
- Raison : forme standard des épreuves d'identifiabilité de l'iVAE (SUPPOSÉ) ; g(Y⁰) réel (non planté) rend le recouvrement de Z indépendant de β_Z, ce qui permet de regrouper Bv0 et Bv1 pour le recouvrement ; Bc est le contrôle où la variable auxiliaire ne porte aucune information sur Z.

**S7 — Nombre de mondes**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : **100** par condition de décision du volet A (12 conditions, 1 200 mondes) ; **50** par condition du volet B (4 conditions, 200 mondes) ; **50** par condition descriptive (D1 à D4, 200 mondes) ; variantes d'échelle (artefact) sur les **30 premiers** mondes de chaque condition du volet A.
- Raison : à 100 mondes, la règle de recouvrement sépare 0,70 (tenue avec la probabilité 0,029) de 0,85 (0,961) (M, script § 1) ; les erreurs regroupées sur 400 mondes séparent 0,05 (0,969) de 0,10 (0,023) (M, § 3).

**S8 — Niveaux de décision et plafond (choix vraiment ouvert : le plafond)**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : **au plus 1 000 paires par environnement**, tirées une fois par monde (rôle 0), toutes années de la fenêtre, pour toutes les méthodes ; α_M1 = 0,05 (tests d'égalité des moyennes et des variances des résidus entre environnements, correction de Bonferroni, comme dans la version approchée de Peters et collègues, SUPPOSÉ) ; environnements de M1 = (sous-domaine × bloc de cinq ans) ; α_M2 = 0,01, seuil de sélection des conditions 0,05 ; seuil d'effet total de M3 = 0,05 (standardisé).
- Raison : la puissance des tests d'invariance et d'indépendance croît avec l'effectif ; sans plafond, toute non-invariance infime du vrai bruit fait rejeter tous les ensembles (M1) et toute dépendance résiduelle devient significative (M2) : le plafond rend l'épreuve comparable d'une base à l'autre. Inconvénient : c'est un degré de liberté ; il est fixé avant lecture et identique pour toutes les méthodes. Autre option : aucun plafond (épreuve « telle qu'un praticien l'emploierait »), au prix d'une M1 probablement toujours abstenue.

**S9 — Règles de qualification du volet A (choix vraiment ouvert : l'exigence de recouvrement)**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : **recouvrement** : BB de Wilson ≥ 0,70 dans chacune des conditions requises (soit au moins 79 mondes sur 100) ; **erreur C** (β = 0) : BH ≤ 0,15 dans chaque affectation requise (au plus 8 mondes sur 100) ; **erreur L, erreur C⁰** : BH ≤ 0,10 sur les 400 mondes regroupés de chaque affectation requise (au plus 28 sur 400) ; **intervention** : erreur relative médiane ≤ 0,30 et borne haute à 95 % ≤ 0,40, dans chaque condition requise.
- Raison (M, script § 1 à § 3) : conjonction des quatre règles de recouvrement tenue avec la probabilité 0,852 pour un recouvrement vrai de 0,85 partout, 0,999 pour 0,90 ; règles d'erreur C sur trois affectations tenues avec 0,822 pour une erreur vraie de 0,05, 0,033 pour 0,10 ; règles d'erreur L et C⁰ sur trois affectations (six règles) tenues avec 0,829 pour 0,05, 0,028 pour 0,07. Une méthode à l'erreur nominale de 5 % passe donc la moitié « erreurs » avec une probabilité de l'ordre de 0,7 (produit, en supposant l'indépendance, M) : l'épreuve est exigeante, et c'est voulu. Autre option : BB ≥ 0,60 (au moins 70 sur 100), moins exigeante.

**S10 — Lecture sous confusion cachée**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : « robuste » = erreur relative médiane de l'effet ≤ **0,50** en H2 et en H3 ; « prudente » = abstention ≥ **0,50** en H2 et en H3, les règles d'erreur sous H tenues.
- Raison : sous confusion cachée, aucune méthode d'observation n'a de garantie ; on demande soit une erreur bornée, soit l'abstention plutôt que la fausse affirmation (une abstention n'est pas une erreur).

**S11 — Règles du volet B**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : **identification** : part des mondes Bv (Bv0 et Bv1 regroupés, 100 mondes) où r_Z ≥ 0,70, BB de Wilson ≥ 0,60 (au moins 70 sur 100) ; **stabilité** : médiane ≥ 0,70 ; **avantage de la variable auxiliaire** : écart apparié M4 − M5 de r_Z en Bv ≥ 0,15 et BB à 95 % > 0 ; **contrôle** : en Bc, |écart| < 0,15 ; **effet** : signe aligné positif et significatif dans ≥ 90 % des mondes Bv1, fausse détection ≤ 10 % des mondes Bv0.
- Raison (M, script § 4 et § 6) : à 100 mondes, une part vraie de 0,75 passe avec 0,896, 0,65 avec 0,173 ; l'écart de 0,15 est atteint avec 0,991 pour un écart vrai de 0,20 si l'écart-type des écarts vaut 0,15 (SUPPOSÉ, sans donnée).

**S12 — Artefacts**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : **invariance d'échelle** : |recouvrement standardisé − recouvrement brut| ≤ 0,10 et |redimensionné − brut| ≤ 0,10 sur les 30 mondes de chaque condition (sinon « artefact d'échelle » pour la méthode) ; **domination par le tri par variance** : recouvrement de T2 en échelle brute ≥ recouvrement de la méthode − 0,05 **et** chute de la méthode de plus de 0,10 en échelle standardisée → « artefact d'ordre des variances » ; **popularité** (volet B) : corrélation entre le facteur apparié de M4 et la première composante principale ≥ 0,9 → audit.
- Raison : Reisach et collègues 2021 montrent (SUPPOSÉ, non vérifié sur PDF) que des réussites de découverte causale sur données simulées tiennent à l'ordre des variances ; l'épreuve doit pouvoir le constater chez nous.

**S13 — Validation de la base (avant toute plantation)**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : au moins **3 environnements** (le contrôle des intelligences artificielles et au moins deux témoins) ; au moins **15 niches retenues** et **100 paires** par environnement ; au moins **12 années** de panel ; part des références résolues dans la moisson ≥ 0,30 ; part des paires-années à sortie réelle non nulle ≥ 0,02 ; part des références vers une œuvre postérieure à l'œuvre citante ≤ 0,01 ; doublons d'identifiant = 0.
- Raison : en dessous, la prédiction invariante n'a pas d'environnements, la sortie est dégénérée ou la base est incohérente ; seuls des booléens sont imprimés (§ 10).

**S14 — Audit de symétrie (R4)**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : déclencheurs : (a) une méthode qui suppose l'absence de facteur caché (T1, M2, M3) a un recouvrement ≥ 0,98 **et** des erreurs L et C⁰ ≤ 0,02 sous H ; (b) toutes les méthodes candidates ont un recouvrement ≤ 0,10 en R3 ; (c) M5 atteint la règle d'identification de S11 en Bv ; (d) domination par le tri par variance (S12) ; (e) recouvrement de 1,00 ou de 0,00 exactement dans les 100 mondes d'une condition β > 0 pour une méthode candidate ; (f) deux mondes d'indices différents donnent des sorties identiques au bit près ; (g) M1 inclut L ou C⁰ dans plus de 10 % des mondes d'une affectation (garantie rompue).
- Raison : un seul jeu de déclencheurs pour le trop propre et le trop mauvais.

**S15 — Budget de processeur**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : **72 heures** de temps mural au plus, sur la machine où se trouve la moisson, sans instance payante ; règle de réduction écrite d'avance, appliquée **avant** tout monde de décision si l'estimation sur les 20 mondes de validation dépasse le budget : (1) conditions descriptives réduites à 30 mondes, (2) volet B réduit à 30 mondes par condition, (3) variantes d'échelle réduites à 15 mondes ; **jamais** les conditions de décision du volet A.
- Raison : ordre de grandeur (SUPPOSÉ) d'une à deux minutes par monde du volet A et de quatre minutes par monde du volet B ; aucune dépense, donc aucun devis.

**S16 — Ensemble d'intervention**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : une année t_I tirée dans la fenêtre (rôle 9) ; I = les paires du **décile inférieur de propension** à t_I (O : popularité ; H : H ; R : 10 % des paires tirées au hasard), retirées de l'ajustement pour l'année t_I et les τ_max suivantes ; intervention : do(C_t_I = 1) sur toutes les paires de I, contre do(C_t_I = 0).
- Raison : sous O et H, ces paires ne recevaient presque jamais de contact : la prédiction est une **extrapolation**, ce qui sépare l'identification de l'association ; sous R, ce n'en est pas une (contrôle).

### Récapitulatif des seuils à geler

| Seuil | Objet | Recommandation en une ligne |
|---|---|---|
| S1 | niches, paires | thème principal OpenAlex, au moins 30 œuvres avant le panel ; paires internes à un environnement |
| S2 | calendrier | panel sans les 2 dernières années (au plus 20) ; référence 5 ans ; ℓ = 2 ; τ_max = 3 |
| S3 | tailles d'effet (ouvert) | β ∈ {0 ; 0,1 ; 0,2 ; 0,4} écart-type, additif |
| S4 | affectation | π_0 = 0,10 ; κ ∈ {0,5 ; 1 ; 1,5} ; γ_O = γ_H = 1,0 |
| S5 | facteur caché, leurre | η = 0,4 ; logit P(L) = −3 + 2,5 C + 1,0 H |
| S6 | volet B | K = 8, d = 6, réseau aléatoire 16-16, Bv / Bc, β_Z ∈ {0 ; 0,4} |
| S7 | mondes | 100 / 50 / 50 ; échelles sur 30 |
| S8 | niveaux, plafond (ouvert) | 1 000 paires par environnement ; α 0,05 / 0,01 ; effet total 0,05 |
| S9 | qualification volet A (ouvert) | BB ≥ 0,70 ; BH ≤ 0,15 (C) ; BH ≤ 0,10 (L, C⁰, 400 mondes) ; intervention ≤ 0,30 (borne ≤ 0,40) |
| S10 | confusion cachée | robuste : erreur ≤ 0,50 ; prudente : abstention ≥ 0,50 |
| S11 | volet B | part ≥ 0,70 de corrélation, BB ≥ 0,60 ; stabilité ≥ 0,70 ; écart ≥ 0,15 ; Bc < 0,15 ; effet 90 % / 10 % |
| S12 | artefacts | échelle ≤ 0,10 ; tri par variance − 0,05 ; composante principale 0,9 |
| S13 | base | 3 environnements, 15 niches, 100 paires, 12 ans, références 0,30, sortie 0,02, incohérences 0,01 |
| S14 | audit R4 | déclencheurs (a) à (g) |
| S15 | budget | 72 heures, réduction écrite |
| S16 | intervention | décile inférieur de propension, une année tirée |

## Plan d'analyse

### 1. Données

- **Moisson** (session-depot, n° 265) : métadonnées OpenAlex (ou son instantané) du sous-domaine du contrôle des intelligences artificielles et de sous-domaines témoins, sans dépense. Champs requis : identifiant, année (et date), thème principal (« primary topic ») et sous-domaine, références (identifiants), auteurs et institutions, source. Le **manifeste de la moisson** (règle de sélection, environnements, date de l'instantané, empreintes) est cité par chemin et empreinte au scellement ; une moisson sans manifeste empreinté arrête tout.
- **Ce qui est une lecture** : tout calcul sur le contenu (comptes, lois, corrélations, sorties de méthodes). **Ce qui n'en est pas une** : la moisson elle-même, la vérification de son empreinte, de son schéma et du nombre de fichiers. Aucune lecture avant le scellement ; après le scellement, la seule lecture avant les mondes de décision est la validation de la base (§ 10), dont seuls des booléens sont imprimés.
- **Environnement** : un par sous-domaine moissonné ; une œuvre appartient à l'environnement de son sous-domaine principal ; une œuvre sans sous-domaine moissonné est exclue (règle fixée ici).

### 2. Panel des paires de niches

- Niches et paires : S1. Années : S2. Plafond : S8 (tirage unique par monde, rôle 0, identique pour toutes les méthodes).
- **Sortie réelle** Y⁰_ij,t : nombre d'œuvres de l'environnement publiées en t dont les références résolues contiennent au moins une œuvre de i et au moins une de j (les œuvres de i ou de j comptent comme œuvres citantes).
- **Covariables réelles**, calculées en t sur les seules données ≤ t (garde de fuite temporelle) : S_ij,t = log(1 + n_i,t) + log(1 + n_j,t), n = nombre cumulé d'œuvres de la niche ; D_ij,t = log(1 + k_i,t) + log(1 + k_j,t), k = citations reçues dans l'année ; A_ij,t = min des âges (années depuis la première œuvre) ; g(Y_ij,t). Toutes sont **recalculées sur la base plantée** : les œuvres synthétiques augmentent la taille et le degré, comme le feraient de vraies œuvres (monde cohérent ; en β = 0 et η = 0, la base est inchangée).
- σ_e = écart-type de Y⁰ sur les paires-années de la période de référence de l'environnement e ; popularité standardisée, quantiles de propension : calculés par le code, écrits au manifeste scellé, **lus par personne avant le verdict**.

### 3. Plantation du volet A (par monde)

1. Tirer H_ij (rôle 4).
2. Pour chaque paire-année de la fenêtre : propension π selon S4 et l'affectation de la condition ; C ~ Bernoulli(π) (rôle 1) ; C⁰ ~ Bernoulli(π) indépendant (rôle 3) ; L ~ Bernoulli(logistique(−3 + 2,5·C + 1,0·H)) (rôle 2, S5).
3. Œuvres-ponts de C : pour chaque paire-année traitée, B = F⁻¹_Poisson(U ; β·σ_e) œuvres en t + ℓ, avec U uniforme du rôle 5 par paire-année (nombres aléatoires communs pour la simulation contrefactuelle).
4. Œuvres-ponts de H : pour chaque paire et chaque année postérieure à la référence, F⁻¹_Poisson(U' ; η·σ_e·2Φ(H)) (rôle 6).
5. Chaque œuvre synthétique : identifiant marqué « synthétique », année, environnement, thème principal tiré entre i et j, **exactement deux références** (une œuvre de i et une œuvre de j publiées avant elle, tirées au hasard), auteurs repris des deux œuvres citées. Les méthodes ne voient que les agrégats du § 2, calculés par **une seule fonction** pour les œuvres réelles et synthétiques ; aucun champ propre aux œuvres synthétiques n'entre dans une variable (garde).
6. Ensemble d'intervention (S16, rôle 9) et simulation contrefactuelle (rôle 10, mêmes U).

### 4. Plantation du volet B (par monde)

Z_ij,t selon S6 (rôle 7) ; réseau de mélange (rôle 8) ; indicateurs x_ij,t ; œuvres-ponts de Z au retard ℓ (rôle 5) ; pas de C, L, C⁰ ; H présent comme au volet A. Variable auxiliaire u = (environnement, bloc de cinq ans), transmise à M4 seulement.

### 5. Méthodes et hyperparamètres (fixés ici, identiques dans tous les mondes)

- **T0** : régression de Poisson pénalisée (pénalité en norme 2, choisie par validation croisée en 5 plis) et réseau à deux couches de 32 unités (perte de Poisson, 50 époques) ; entrées S, D, A, g(Y).
- **T1** : forêt d'arbres par gradient d'histogrammes (`scikit-learn`), 300 itérations, pas 0,05, 31 feuilles au plus, perte quadratique sur g(Y⁺), sans arrêt anticipé ; ajustement croisé en 5 plis ; importance par permutation (10 répétitions) avec sonde de bruit.
- **T2** : ordre par variance marginale croissante (échelle de la variante), régression pénalisée en norme 1 de chaque variable sur ses prédécesseurs (pénalité par validation croisée).
- **M1** : prédiction causale invariante linéaire sur g(Y⁺), 7 candidates (128 sous-ensembles), environnements et niveau S8, intervalles de confiance des coefficients rapportés.
- **M2** : PCMCI, corrélation partielle, retards 1 à τ_max, niveaux S8, mode « jeux de données multiples » (une série par paire), variables C, L, C⁰, S, D, A, g(Y).
- **M3** : LiNGAM direct (`lingam`), élagage par régression pénalisée adaptative (réglage par défaut de la bibliothèque, version figée), sur C, L, C⁰, S, D, A, g(Y), g(Y⁺) ; **aucune connaissance a priori d'ordre** (la variante avec ordre temporel imposé est descriptive).
- **M4** : iVAE ; encodeur 8 → 64 → 64 → 2d, décodeur d → 64 → 64 → 8, loi a priori normale factorisée dont moyenne et log-variance sortent d'un réseau 1 couche de 32 unités sur l'encodage de u ; Adam, pas 10⁻³, lots de 256, 50 époques ; au plus 50 000 paires-années d'entraînement ; deux graines d'entraînement.
- **M5** : identique à M4, loi a priori normale standard, u absent.
- **T3** : composantes principales sur x standardisé, d composantes.
- **Variantes d'échelle** (T2, M1, M2, M3, T1) : brute (comptes en g, binaires telles quelles), standardisée (centrée réduite par monde), redimensionnée (chaque variable multipliée par 10^U, U uniforme sur [−1 ; 1], rôle 11).
- Toute exception dans une méthode est **levée et consignée** ; aucun repli silencieux (R5) ; un échec de convergence compte comme « ne trouve pas » pour ce monde et est rapporté par méthode.

### 6. Artefacts à traquer

| Artefact | Mécanisme | Mesure | Conséquence |
|---|---|---|---|
| Ordre des variances (Reisach, Seiler et Weichwald 2021, « varsortability ») | les méthodes qui exploitent les variances marginales « trouvent » l'ordre causal quand la variance croît le long du graphe ; ici, des binaires de variance ≈ 0,09 précèdent une sortie en log de variance plus grande | part des couples (cause, effet) du sous-graphe planté (C → sortie, C → L) où la variance de la cause est la plus faible, en échelle brute et standardisée ; idem pour le coefficient de détermination (« R²-sortabilité », Reisach et collègues 2023, SUPPOSÉ) ; témoin T2 ; variantes d'échelle | S12 : « artefact d'ordre des variances » ou « d'échelle » pour la méthode (Table A, ligne 3) |
| Échelle | comptes à queue lourde ; la transformation g change les corrélations | variantes brute, standardisée, redimensionnée ; descriptif : rangs normalisés | S12 |
| Degré et âge des nœuds | les grandes et vieilles niches ont plus de ponts réels et plus de variance | recouvrement et erreurs par tiers de S, de D et de A ; part des réussites dans le tiers supérieur | descriptif ; prédiction transversale (ii) |
| Effet Matthieu (Merton 1968, SUPPOSÉ) | sous O, C suit la popularité, qui prédit la sortie réelle ; une méthode qui ajuste mal « trouve » C sans effet | erreur C en O0 ; erreur C⁰ sous O (jumeau au même mécanisme d'affectation, 400 mondes) ; jugeabilité J_O | Table A, lignes 4 et 9 ; J_O conditionne la lecture de O |
| Survivants | les paires retenues sont celles qui existent assez longtemps | toutes les paires de niches retenues sont à risque, ponts ou non ; aucune sélection sur la sortie | — (par construction) |
| Fuite temporelle | une covariable calculée avec l'avenir | recalcul sur la base tronquée en t (garde R5) | arrêt |
| Œuvres synthétiques reconnaissables | un agrégat qui distingue réel et synthétique (par exemple, le nombre de références) | liste fermée des agrégats permis ; garde R5 | arrêt |
| Popularité apprise (volet B) | un réseau non supervisé apprend d'abord ce qui varie le plus : taille, âge, degré | captation de la popularité ; corrélation avec T3 | descriptif ; S12 (audit) |

### 7. Conditions

| Code (graine) | Volet | Affectation | β (ou β_Z) | Mondes | Rôle |
|---|---|---|---|---|---|
| R0 à R3 (1 à 4) | A | au hasard | 0 ; faible ; moyen ; fort | S7 | décision |
| O0 à O3 (5 à 8) | A | popularité observée | idem | S7 | décision |
| H0 à H3 (9 à 12) | A | facteur caché | idem | S7 | décision |
| Bv0, Bv1 (13, 14) | B | — (Z variable selon u) | 0 ; 0,4 | S7 | décision |
| Bc0, Bc1 (15, 16) | B | — (Z constant selon u) | 0 ; 0,4 | S7 | décision (contrôle) |
| D1 (17) | A | au hasard | moyen, multiplié par {0,5 ; 1 ; 1,5} selon l'environnement (effet non invariant) | S7 | descriptive |
| D2 (18) | A | facteur caché | moyen, **η = 0** | S7 | descriptive (attribution des erreurs à H) |
| D3 (19) | A | au hasard | moyen ; niches = communautés de Leiden | S7 | descriptive |
| D4 (20) | A | au hasard | moyen, forme multiplicative | S7 | descriptive |

### 8. Graines (R9)

- **Racines** : RACINE = 20261110 (mondes de décision et descriptifs) ; RACINE_VALIDATION = 20261111 (20 mondes de validation de la plomberie, essais de gardes sur la base jouet, audit). Deux entiers fixés par ce texte, sans lien avec un résultat, recopiés au manifeste ; aucune autre racine permise.
- Chaque tâche reçoit `numpy.random.SeedSequence(entropy=RACINE, spawn_key=(code_condition, indice_monde, code_rôle))` (numpy ≥ 1.25) ; seconde graine d'entraînement : cinquième élément 1.
- Codes de rôle : tirage des paires 0 ; affectation de C 1 ; leurre 2 ; jumeau 3 ; facteur caché 4 ; œuvres de C (et de Z) 5 ; œuvres de H 6 ; latente Z et paramètres de u 7 ; réseau de mélange 8 ; ensemble d'intervention et année 9 ; contrefactuel 10 (mêmes U que le rôle 5 : nombres aléatoires communs) ; redimensionnement 11 ; méthodes 20 + rang (T0 = 20, T1 = 21, T2 = 22, M1 = 23, M2 = 24, M3 = 25, M4 = 26, M5 = 27, T3 = 28) ; rééchantillonnage 99, `indice_monde` remplacé par un code de contraste (1 recouvrement ; 2 erreur C ; 3 erreur L ; 4 erreur C⁰ ; 5 intervention ; 6 écart M4 − M5 ; 7 stabilité).
- **Manifeste par run** (`src/controle_ia/manifeste.py`) : configuration et empreinte, versions de Python, numpy, `tigramite`, `lingam`, `scikit-learn`, torch, racines et clés, empreinte du code, empreinte du manifeste de la moisson, σ_e et quantiles de propension (non imprimés), nombres de mondes, commit ; **scellé avant le premier monde de décision**.

### 9. Comparaisons, multiplicité, puissance

- Les règles de qualification sont des **conjonctions**, chacune à son niveau, sans correction ; leurs caractéristiques opératoires sont calculées (M, script § 1 à § 7) et données à S7, S9, S11. Les erreurs sont regroupées par affectation (400 mondes) pour éviter qu'une conjonction de douze règles ne disqualifie une méthode nominale.
- **Jugeabilité** (analogue de la condition J du préenregistrement modèle) : J_L = erreur L de T1 regroupée sous R ≥ 0,20 (le leurre tente un prédicteur ; tenue avec 0,992 si la part vraie vaut 0,25, 0,004 si elle vaut 0,15 ; M, script § 7) ; J_O = en O0, contraste non ajusté moyen de g(Y⁺) entre C = 1 et C = 0 positif avec borne basse à 95 % > 0 (la popularité confond réellement) ; J_H = erreur C⁰ de T1 regroupée sous H ≥ 0,20. Une règle d'erreur passée sur une confusion non jugeable ne vaut rien et n'est pas lue comme une réussite.
- Descriptifs (sans verdict) : recouvrement par taille d'effet (pente), rang de C parmi toutes les candidates, erreurs par tiers de popularité, D1 à D4, sorties des méthodes sur les variables réelles (rapportées, jamais notées), retard détecté par M2, variante ordonnée de M3.
- Coût : processeur seul ; environ 1 600 mondes ; S15.

### 10. Ordre d'exécution

Verdict du collisionneur sur la question 6 → brouillon 2 → contre-lecture par un modèle différent d'Opus (R2) → corrections → gel de S1 à S16 par Lazar (ligne datée) → remplacement des marqueurs et scellement (`sceller_prereg`) → écriture du code → **gardes R5 sur une base jouet entièrement synthétique** (jamais sur la moisson) → réception de la moisson : vérification de son empreinte et de son manifeste (pas une lecture) → **validation de la base** (S13 ; la console ne reçoit que des booléens ; les descriptifs vont dans un fichier scellé, ouvert avec le verdict) → **validation de la plomberie** sur 20 mondes de RACINE_VALIDATION (R3 et R0 : nombre moyen d'œuvres plantées par paire-année traitée dans l'intervalle de Poisson attendu, base identique au bit près en β = 0 et η = 0, T0 sans C ; booléens seulement ; estimation du temps → règle de réduction de S15 si besoin) → manifeste scellé → **une seule invocation** des mondes de décision et descriptifs, sans reprise ni extension → lecture par un sous-agent neuf (R13), qui vérifie d'abord l'ordre (horodatages et empreintes du manifeste antérieurs aux fichiers de résultats ; nombres de mondes) → verdict scellé → GO de Lazar.

## Critères de lecture gelés

Un sous-agent neuf (ni auteur du préenregistrement ni de l'analyse, R13) applique ces tables telles qu'écrites. Chaque table se lit **de haut en bas : la première ligne vraie décide** ; la dernière est le complémentaire.

**Booléens communs.**
- V0 = validation de la base (S13) et de la plomberie passées ∧ aucun arrêt de la liste ∧ taux d'exclusion ≤ 2 % dans chaque condition de décision ∧ nombre de mondes exécutés = S7 (ou réduction de S15 consignée avant le premier monde de décision) ∧ manifeste scellé avant le premier fichier de résultats.
- AUDIT_EN_ATTENTE = un déclencheur de S14 est présent et le rapport d'audit n'est pas scellé ; ARTEFACT = le rapport d'audit scellé constate l'une des issues (i) à (iii) ci-dessous.
- Pour une méthode M et une affectation X ∈ {R, O, H} : REC_X(M) = règle de recouvrement de S9 tenue en X2 et en X3 ; ERR_X(M) = règle d'erreur C tenue en X0 ∧ règles d'erreur L et C⁰ tenues sur les 400 mondes de X ; INT_X(M) = règle d'intervention tenue en X2 et en X3 ; ART(M) = aucun artefact d'échelle ni d'ordre des variances (S12) ; ROB_H(M) et PRU_H(M) selon S10.

**Audit de symétrie (R4).** Déclencheurs : S14 (a) à (g). Contenu : relecture du code par un sous-agent neuf (aucune méthode ne lit H, Z, le marqueur « synthétique » ni la vérité : exception `AccesVerite`, balayage statique) ; relance sur RACINE_VALIDATION ; recalcul des contrefactuels. **Issue, sans autre jugement** : « artefact trouvé » si et seulement si le rapport scellé constate (i) une lecture de la vérité par une méthode, (ii) une erreur de code nommée (fichier, ligne, effet) avec essai sain et essai d'artefact, dont la correction déplace un taux décisif de plus de 0,05 sur les graines de validation, ou (iii) une différence de plus de 0,05 entre la vérité contrefactuelle recalculée et celle du run. Sinon « aucun artefact » et les tables s'appliquent telles quelles.

### Table A — volet A, une lecture par méthode candidate (T1, M1, M2, M3)

| # | Condition de la ligne | Verdict |
|---|---|---|
| 0 | non V0 | **non concluant** ; aucune lecture |
| 1 | AUDIT_EN_ATTENTE | **non concluant** (audit en attente) |
| 2 | ARTEFACT | **non concluant** ; version nouvelle (R12) |
| 3 | non ART(M) | **non qualifiée : artefact d'échelle ou d'ordre des variances** |
| 4 | non ERR_R(M) | **non qualifiée : fausses causes même sous affectation au hasard** |
| 5 | non J_L, puis lecture de la ligne 6 avec la mention « leurre non jugeable » ; sinon passer | (transition) |
| 6 | non REC_R(M) | **non qualifiée : ne retrouve pas la cause plantée, même au hasard** |
| 7 | non INT_R(M) | **détection seulement** : retrouve C sans prédire l'effet d'une intervention ; non qualifiée pour les gradations 2 et 3 |
| 8 | non J_O | **qualifiée pour la gradation 3 seulement**, mention « confusion observée non jugeable » |
| 9 | non (REC_O(M) ∧ ERR_O(M) ∧ INT_O(M)) | **qualifiée pour la gradation 3 seulement** (affectation randomisée) ; échoue sous confusion observée |
| 10 | non J_H, ou non ERR_H(M) | **qualifiée pour la gradation 3, et pour la gradation 2 sous confusion observée seulement** ; mention « confusion cachée non jugeable » si non J_H, sinon « trompée par la confusion cachée : jamais en observation pure » |
| 11 | ROB_H(M) | **qualifiée pour les gradations 2 et 3, robuste sous confusion cachée** (dans ce monde) |
| 12 | PRU_H(M) | **qualifiée pour les gradations 2 et 3, prudente** : s'abstient sous confusion cachée plutôt que de se tromper |
| 13 | tout autre cas | **qualifiée pour la gradation 3, et pour la gradation 2 sous confusion observée seulement** ; sous confusion cachée ni robuste ni prudente |

Notes : la ligne 4 précède la ligne 6 parce qu'une méthode qui invente des causes au hasard n'a pas de recouvrement lisible. Les lignes 3, 4, 6 et 7 sont des raisons de non-qualification distinctes et nommées. **T0** ne reçoit pas de verdict de qualification : ses erreurs non nulles, ou un effet prédit non nul, sont un **arrêt de plomberie**. **T2** ne reçoit pas de verdict : il ne sert qu'à S12 et S14 (d). La ligne 5 est une transition : si le leurre n'est pas jugeable, les verdicts suivants portent la mention « leurre non jugeable » et l'erreur L n'est pas lue comme une réussite ; elle reste lue comme un échec si elle dépasse S9 (direction prudente).

### Table B — volet B : « l'apprentissage non supervisé identifie-t-il la cause latente à lui seul ? »

Booléens : IDV(M) = règle d'identification de S11 tenue en Bv ; STAB(M) = stabilité médiane ≥ 0,70 en Bv ; AUX = écart M4 − M5 en Bv ≥ 0,15 avec BB > 0 ; AUXc = |écart M4 − M5| < 0,15 en Bc ; EFF(M) = règle d'effet de S11 (Bv1 et Bv0).

| # | Condition de la ligne | Verdict |
|---|---|---|
| 0 | non V0 | **non concluant** |
| 1 | AUDIT_EN_ATTENTE | **non concluant** (audit en attente ; S14 (c) déclenche l'audit si M5 identifie) |
| 2 | ARTEFACT | **non concluant** ; version nouvelle |
| 3 | IDV(M5) ∧ STAB(M5) ∧ non AUX | **le réseau libre identifie aussi bien que l'iVAE dans ce monde : la thèse « pas à lui seul » est réfutée ici** (issue permise ; la non-gaussianité ou la variance de Z ont suffi) |
| 4 | non IDV(M4) | **l'iVAE n'identifie pas la cause latente sur base semi-réelle** : la variable auxiliaire ne suffit pas ici ; non qualifiée |
| 5 | non STAB(M4) | **l'iVAE retrouve sans stabilité entre graines** : non qualifiée |
| 6 | non AUXc | **contrôle en défaut** : l'avantage de l'iVAE persiste quand la variable auxiliaire est sans information ; l'avantage ne vient pas de l'hypothèse ; non qualifiée |
| 7 | non AUX | **identification sans avantage démontré de la variable auxiliaire** : indécis sur le rôle de l'hypothèse |
| 8 | non EFF(M4) | **l'iVAE identifie la latente mais l'effet retrouvé est faux ou inventé** : non qualifiée pour l'étape d'effet |
| 9 | tout autre cas (IDV, STAB, AUXc, AUX et EFF de M4 tenus) | **oui sous hypothèse** : l'iVAE identifie avec la variable auxiliaire, le réseau libre non ; l'identification vient de l'hypothèse écrite (variabilité de la loi de la latente selon u), pas de l'apprentissage seul ; iVAE qualifiée pour l'étape de représentation des gradations 2 et 3 |

Lecture secondaire, sans effet sur les verdicts : captation de la popularité par M5 et T3 (« ce qu'un modèle non supervisé apprend en pratique ») ; rang du facteur apparié ; corrélation des facteurs de M4 avec la première composante principale ; écart M4 − M5 en Bc.

Aucune lecture avant scellement ; rien de ces tables ne change après lecture ; toute déviation est écrite comme telle (R1). Le verdict est scellé puis soumis à Lazar pour GO (R13).

## Liste d'arrêt

| Condition | Action |
|---|---|
| Moisson sans manifeste, empreinte différente de celle du manifeste, ou manifeste non cité au scellement | arrêt avant toute lecture |
| Lecture du contenu de la moisson, ou exécution d'une méthode, avant le scellement ; paramètre modifié après une lecture ; fichier de descriptifs ouvert avant le verdict | arrêt ; consignation de l'écart (R1) |
| Validation de la base ratée (S13) | arrêt ; version nouvelle du préenregistrement (R12) |
| Plomberie : base non identique au bit près en β = 0 et η = 0 ; nombre moyen d'œuvres plantées hors de l'intervalle de Poisson attendu ; T0 qui reçoit C, L ou C⁰ ou prédit un effet non nul | arrêt |
| Fuite temporelle (covariable différente après troncature de la base en t) | arrêt |
| Agrégat qui lit un champ propre aux œuvres synthétiques ; méthode qui lit H, Z, le marqueur « synthétique » ou la vérité (`AccesVerite`) | arrêt ; audit R4 |
| Balayage statique : `except` autour d'un appel de méthode qui rend une valeur par défaut | arrêt : code refusé (R5) |
| Valeur non numérique ou division par zéro dans une sortie, une covariable ou une vérité | arrêt |
| Échec de convergence d'une méthode dans plus de 5 % des mondes d'une condition | arrêt de la méthode ; consigné |
| Taux de mondes exclus > 2 % dans une condition de décision | arrêt |
| Nombre de mondes exécuté différent de S7 (ou de la réduction de S15 consignée avant les mondes de décision) ; mondes de décision en plusieurs invocations | arrêt ; V0 fausse |
| Manifeste scellé après le premier fichier de résultats | arrêt ; V0 fausse ; contrôle par le lecteur de la porte (R13) |
| Racine différente de RACINE ou de RACINE_VALIDATION, monde de décision tiré avec RACINE_VALIDATION, numpy < 1.25 | arrêt (R9) |
| Version d'une bibliothèque différente du manifeste ; empreinte du code différente entre deux sessions d'un même run | arrêt |
| Dépassement du budget S15 constaté pendant les mondes de décision | arrêt ; aucune lecture partielle ; version nouvelle (la réduction n'est permise qu'avant) |
| Appel de modèle, réseau, instance payante ou dépense | arrêt (devis et GO exigés) |
| Déclencheur de S14 | audit R4 ; verdict « non concluant » tant qu'il n'est pas rendu |
| Marqueur de gel restant, ou entrée « Contre-lecture k » sans ses deux empreintes | pas de scellement (**contrôlé** par le validateur `problemes`) |
| Ligne de gel absente de `registres/decisions.md` ou différente du texte ; remarques de contre-lecture non traitées ; verdict du collisionneur sur la question 6 non intégré ; manifeste de la moisson non cité | pas de scellement ; **contrôle manuel** (le validateur ne le vérifie pas) |

**Gardes testées sur un cas sain et sur un artefact (R5)**, sur base jouet synthétique, avant toute lecture de la moisson :
- **plomberie en β = 0** : base inchangée au bit près (sain) ; plantation fautive qui ajoute une œuvre en β = 0 : détectée (artefact) ;
- **fuite temporelle** : covariables recalculées sur la base tronquée en t identiques (sain) ; covariable qui lit l'année t + 1 : détectée (artefact) ;
- **œuvres synthétiques** : une œuvre réelle et une synthétique de mêmes références donnent les mêmes agrégats (sain) ; un agrégat qui compte les œuvres sans source : refusé par la liste fermée (artefact) ;
- **vérité contrefactuelle** : base jouet où l'effet est calculable à la main, égalité avec le code (sain) ; contrefactuel tiré avec d'autres nombres aléatoires que le monde : écart détecté (artefact) ;
- **T0 aveugle** : liste d'entrées sans C, L, C⁰ (sain) ; T0 qui reçoit C : refusé (artefact) ;
- **méthode qui lit la vérité** : une méthode artefact qui demande H lève `AccesVerite` ; une méthode artefact qui reçoit la sortie contrefactuelle doit atteindre un recouvrement ≥ 0,98 avec erreurs nulles sous H **et** déclencher l'audit (S14 a) ; cas sain : M2 s'exécute sans exception ;
- **règles de décision** : base jouet linéaire à effet fort, sans leurre corrélé : C trouvé par M1, M2, M3, T1 (sain) ; base jouet où C est du bruit et la sortie permutée : erreur C au plus au niveau nominal sur 50 bases (artefact) ;
- **invariance d'échelle** : LiNGAM direct invariant au redimensionnement sur base jouet linéaire non gaussienne (sain) ; T2 qui change avec le redimensionnement : la mesure de S12 le détecte (artefact) ;
- **iVAE** : base jouet à latente identifiable (loi variable selon u, mélange linéaire) : r ≥ 0,9 (sain) ; u permuté (sans information) : chute détectée par le contrôle Bc (artefact) ;
- **graines** : deux mondes d'indices différents donnent des plantations différentes (sain) ; même clé réutilisée : détectée (artefact) ;
- **budget** : dépassement simulé avant les mondes de décision → réduction dans l'ordre de S15 (sain) ; réduction qui toucherait une condition de décision du volet A : refusée (artefact) ;
- **moisson non lue** : premier contact avec la moisson qui n'imprime que les booléens de S13 (sain) ; impression d'un descriptif : refusée (artefact) ;
- **jugeabilité** : base jouet où le leurre est fort, J_L vraie (sain) ; base jouet où le leurre est indépendant de H, J_L fausse et mention « leurre non jugeable » portée par la Table A (artefact).

## Contre-lecture

À REMPLIR — contre-lecture à faire par un sous-agent neuf **d'un modèle différent d'Opus** (Fable 5.1 de préférence, sinon Sonnet 5.5 avec réserve d'indépendance), non-auteur de ce brouillon, de la question 6, des réponses 5 et 6 et de la relecture 5 ; après le verdict du collisionneur et sur le brouillon 2 de préférence. Fichiers à lui donner explicitement : ce brouillon (empreinte au moment de la relecture), le script de calcul et sa sortie (à rejouer au bit près), `prereg/gabarit-preregistrement-v1.md`, `src/controle_ia/prereg.py`, `question-6-identification-collisionneur-v1.md`, `reponse-conv-audit-question-6-v1.md`, `reponse-conv-audit-question-5-v1.md`, `reponse-fable-independante-question-5-v1.md`, `relecture-fable-reponse-5-v1.md`, le verdict du collisionneur sur la question 6, et `prereg/preenregistrement-bisociation-deux-espaces-v2.md` comme modèle de forme ; rien de `donnees/`, rien de la moisson. Points à attaquer en priorité : (1) le leurre collisionneur rend-il T1, M2, M3 non qualifiables par construction (épreuve truquée contre elles) ? (2) le plafond S8 est-il un degré de liberté qui favorise M1 ? (3) l'indicateur « œuvres-ponts » est-il trop loin de la fertilité pour qualifier quoi que ce soit ? (4) la Table A est-elle exclusive et exhaustive ? (5) les jugeabilités J_L, J_O, J_H sont-elles bien placées ? (6) un monde à un seul vrai bruit autorise-t-il une qualification ? Entrée à écrire ensuite : « Contre-lecture 1 », identifiant du sous-agent, empreinte du brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque (accepté, refusé et pourquoi).
