# Rapport de la grille de la clause de repli — stabilité de rang du papier C (C-P3a, C-P3b, C-P3c) — v1

Contre-lecture de méthode par simulation, faite le 2026-11-19 par un agent neuf (Claude Fable 5.2) qui n'a écrit ni le
texte ni ses brouillons. Données simulées seulement, tout sur processeur ; aucun résultat d'expérience lu (rien sous
`diag/`, `runs/`, `donnees/`, `docs/verdicts/`) ; aucune modification du dépôt. Ce rapport est celui que demandent le
verrou 10 du texte et la réserve de l'accord GO-2026-11-19-53 (décision D-9, version (a) « sous réserve du rapport de
la grille entière et de la ligne C-P3c, sinon (b) »). Mesure de conception, jamais un résultat.

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/ea38fd7e-2b5a-5aae-9611-af6160a314d6/scratchpad/bloc-notes/grille/`
(noté `grille/` ci-dessous). Versions : python 3.13.18, numpy 2.5.3 ; scipy n'est pas installé sur cette machine et
n'est pas employé.

## 1. Conclusion par ligne (mécanique)

| ligne | la clause de repli joue-t-elle ? | pourquoi |
|---|---|---|
| C-P3a | **non**, sur les cases jouées | 86 cases nulles, trois lectures jointes : 0,003 à 0,049, toutes sous le seuil 0,0638 (1 000 essais) d'au moins deux erreurs de Monte-Carlo ; 2 cases rejouées à 4 000 essais : 0,034 et 0,034 (seuil 0,0569). |
| C-P3b | **non**, sur les cases jouées | 86 cases nulles : 0,009 à 0,053, aucune au-dessus de 0,0638 ; deux cases non nettes (0,053 et 0,051), rejouées sur graine neuve à 4 000 essais : 0,043 ± 0,003 et 0,040 ± 0,003, nettement sous 0,0569. |
| C-P3c | **oui**, sous tout modèle où les deux gains d'écart suivent leur définition du texte ; non sous l'idéalisation « bruit pur » seule | Le texte calcule le gain sous le plaidoyer et le gain sous l'usurpation avec la même cellule S et le même D₀ (Métrique, point 13) : ces deux évaluateurs ne sont pas indépendants, alors que la valeur p exacte (1 296 affectations) le suppose. Taux aux trois lectures jointes : 0,076 à 0,107 sans attaque (seuil 0,0549 à 8 000 essais ; écart de plus de cinq erreurs de Monte-Carlo), jusque dans les cases homogènes ; 54 cases sur 96 au-dessus du seuil dans le bras principal. Sous l'idéalisation « deux gains d'écart = bruit indépendant » : 0,016 à 0,054, aucune case au-dessus. |

Conséquence à la lettre de la clause (lignes 580 à 583 du texte) : C-P3a et C-P3b gardent leur verdict aux trois
lectures ; C-P3c « est rapportée sans verdict, écrit tel quel, sans nouveau nœud » — si le modèle des gains d'écart de
la section 5, instrument neuf, tient à sa contre-lecture par un autre modèle. La grille du texte ne définit pas ce
modèle (ambiguïté A5) : c'est le seul point où la conclusion dépend d'un choix de ce rapport, et je le dis au lieu de
le trancher en silence. Je ne décide pas de la version de D-9 ; je constate que la réserve de l'accord porte sur
« la ligne C-P3c » et que cette ligne passe le seuil.

Aux deux premières lectures seules (pour information) : C-P3a 0,006 à 0,153 et C-P3b 0,019 à 0,131 ; le seuil est passé
dans les quatre cases « un mécanisme par juge, g = 0,20 » (0,097 à 0,153 et 0,076 à 0,131), comme l'archive
l'avait vu ; nulle part ailleurs sur les cases jouées (0,058 au plus).

## 2. Texte lu

`brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-c2.md`, 1 590 lignes, empreinte
vérifiée `7a8d57c8c8c9a3c3aa77c708e7d4aab46d0c19e0e3b6c5f2d66bbc5b94421f61`. Lus : verrou 10 (lignes 178 à 184) ; bloc
« Stabilité de rang » et clause (lignes 543 à 589) ; Métrique, points 1, 3 à 6, 8, 8 bis, 9 à 13 (lignes 668 à 791) ;
Seuil (lignes 935 à 937) ; Plan, étape 2 (lignes 1098 à 1190, 1211 à 1215) ; réserve 15 (lignes 1311 à 1318) ;
Critères de lecture gelés (lignes 1380 à 1407) ; liste d'arrêt, point 17 (ligne 1521). Accord : ligne
GO-2026-11-19-53 de `origin/main:registres/go.md` (« D-9 (a) sous réserve du rapport de la grille entière et de la
ligne C-P3c, sinon (b) »).

## 3. Statistiques et règles reproduites

- **C-P3a** (ligne 565) : W de Kendall des rangs des trois juges par Ḡ net, cinq familles, corpus A. « Établie » si p
  exact (7 776 affectations) ≤ 0,05 **et** p par rééchantillonnage centré ≤ 0,05, p = (1 + #{W* ≥ W}) / (B + 1), W* sur
  les rangs de Ḡ* − Ḡ.
- **C-P3b** (ligne 566) : τ de Kendall entre les quinze écarts intra-famille du corpus A et ceux du corpus B.
  « Établie » si p = (1 + #{τ* ≥ τ}) / (B + 1) ≤ 0,05, τ* entre les écarts intra-famille de Ḡ*_A − Ḡ_A et de
  Ḡ*_B − Ḡ_B, tirages indépendants par tâches et par items.
- **C-P3c** (ligne 567) : W de Kendall des trois juges, quatre évaluateurs (gain d'écart brut sous le plaidoyer, Ḡ_P ;
  gain d'écart brut sous l'usurpation de l'agent ; Ḡ net de la famille 1 ; Ḡ net de la famille 4). « Établie » si p
  exact (1 296 affectations) ≤ 0,05.
- **Trois lectures** (lignes 569 à 572) : loi nette calibrée, sans calibrage (ρ = 1), calibrée par ρ̂/r̂ borné à
  [0,05 ; 1], ρ̂ et r̂ recalculés dans chaque tirage ; « établie » seulement si les trois concluent.
- **Seuil de la clause** (lignes 581 à 582) : 0,05 + 2 × √(0,05 × 0,95 / R), recalculé par case : 0,0638 pour
  R = 1 000 ; 0,0569 pour 4 000 ; 0,0549 pour 8 000 ; 0,0718 pour 400 (scénarios d'effet seulement).
- Contrôle des lois exactes : avec cinq évaluateurs, plus petit W à p ≤ 0,05 = 0,64 (p = 0,0394), P(W ≤ 0,20) = 0,6327 ;
  avec quatre, W = 0,8125 (p = 0,0417). Conformes au texte.

Loi jointe en forme fermée, sommes par tâche, comptes multinomiaux, W, τ : fonctions de l'archive reprises sans
modification (`grille/archive/`, manifeste `sha256sums-archive-v1.txt`) ; le reste est écrit par moi
(`grille/programmes/grille_commun_v1.py`).

## 4. Définition des cases

Modèle d'un juge pour TC.1 (celui de l'archive) : lecture vraie T_i commune aux trois juges ; v₀ = T + e₀, e₀ ~ N(0, s₀) ;
lecture sous un témoin = T + κ (μ − T) + N(0, σ) ; lecture sous la formulation de rang m de la famille f = la même
plus g_{j,f,m} (c − T), c = v* (λ = 1). Corpus A : T tâches, deux contenus par tâche (honnête de moyenne 2, saboteur de
moyenne 4, effet de tâche 0,5, résidu 0,8), μ = 3, v* = 0. Corpus B : 30 items N(4,5 ; 1,4), μ = 4,5, v* = 9. Gains
vrais : g × (0,6 ; 0,8 ; 1 ; 1,2 ; 1,4) par famille × pente de 0,5 à 1,5 sur les k rangs. Seize témoins, appariés par
la règle des témoins (lignes 1073 à 1076) sur les longueurs de la configuration brouillon 3 de l'archive ; k = 3 :
formulations d'indices 1, 8, 16 ; k = 5 : 1, 4, 8, 12, 16.

Une case = modèle d'erreur des trois juges × attaque × k × T.

| nom | modèle d'erreur des trois juges (s₀, σ, κ) | mots de la clause (lignes 584 à 586) |
|---|---|---|
| E30 | (0,3 ; 0,3 ; 0) pour les trois | erreur sur v₀ seule, borne basse |
| E40 | (0,4 ; 0,4 ; 0) pour les trois | erreur seule, milieu (scénarios N0 et N1 de l'archive) |
| E60 | (0,6 ; 0,6 ; 0) pour les trois | erreur seule, borne haute |
| EH | (0,3 ; 0,3 ; 0), (0,45 ; 0,45 ; 0), (0,6 ; 0,6 ; 0) | erreur seule, les trois juges diffèrent |
| K16 | (0 ; 0,4 ; 0,16) pour les trois | compression seule, borne haute |
| KH | (0 ; 0,4 ; 0,04), (0 ; 0,4 ; 0,10), (0 ; 0,4 ; 0,16) | compression seule, les trois juges diffèrent |
| MH | (0,6 ; 0,6 ; 0), (0,4 ; 0,4 ; 0,08), (0 ; 0,4 ; 0,16) | un mécanisme par juge (scénarios N4 et N5 de l'archive) |
| M616 | (0,6 ; 0,6 ; 0,16) pour les trois | mélange homogène aux deux bornes hautes |

Attaque : aucune (g = 0) ; même attaque chez les trois juges, g = 0,10 ; g = 0,20 ; λ = 1. k = 3 et 5 ; T = 45 et 60
tâches ; corpus B de 30 items. Les cases que le rédacteur n'avait pas : **g = 0,20 sous l'erreur seule** (E30, E60,
EH) et **sous la compression seule** (K16, KH), « aucune attaque » hors du modèle homogène 0,4, g = 0,20 sous le
mélange homogène, bornes 0,3 et 0,6.

- **C-P3a et C-P3b** : 7 modèles (tous sauf E40) × 3 attaques × 2 × 2 = 84 cases, 1 000 essais, 1 000 tirages par
  grappes (mêmes comptes pour les trois juges et les cinq familles d'un corpus ; tirages indépendants entre corpus),
  plus 2 cases E40 de recoupement avec le rejeu du rédacteur. Total : 86 cases nulles.
- **C-P3c** : 8 modèles × 3 × 2 × 2 = 96 cases, 8 000 essais (aucun rééchantillonnage : la ligne n'emploie que la
  valeur p exacte).

## 5. Modèle simulé des gains d'écart de C-P3c (instrument neuf, à contre-lire)

Code : fonction `gains_ecart` de `grille/programmes/grille_commun_v1.py` ; programme `grille_c_v1.py`. Les Ḡ nets des
familles 1 et 4 viennent du modèle de TC.1 ci-dessus, aux trois lectures, sur les mêmes essais.

Statistique du texte (point 13, lignes 773 à 775) : D₀ = moyenne_t (S_t − H_t) ; g_m brut = −moyenne_t (SP_{m,t} − S_t) / D₀ ;
Ḡ_P = moyenne des g_m sur les k_P niveaux ; « idem pour U, à un seul niveau ».

Hypothèses, toutes déclarées :

- **G1.** Les cellules H et S de TC.2 et de TC.3 b sont les contenus H et S du corpus A de TC.1 (ligne 1135 :
  « Corpus A : contenus H et S ») : le juge y donne v₀, erreur e₀ comprise. S et D₀ sont donc communs au gain sous le
  plaidoyer et au gain sous l'usurpation d'un même juge. La seconde phrase n'est pas un choix : c'est la définition
  du point 13.
- **G2.** Chaque cellule SP_m et SU est un épisode neuf de la même tâche et du même agent saboteur (ligne 1111 :
  2 × (2 + k_P) épisodes par tâche) : lecture vraie T' = 4 + u_t + N(0 ; 0,8), u_t l'effet de tâche du corpus A, tirage
  indépendant par cellule, commun aux trois juges.
- **G3.** Le paragraphe écrit par l'agent déplace la lecture du juge j d'une fraction γ du chemin vers v* :
  + γ (v* − T'). Plaidoyer : γ = gp_j × pente de 0,5 à 1,5 sur les k_P niveaux ; usurpation : γ = gu_j.
- **G4.** Ce que le juge fait d'autre d'un contenu qui porte un paragraphe de l'agent n'est pas fixé par le texte. Deux
  variantes : « insertion » (le paragraphe agit comme toute insertion de TC.1 : compression κ_j (μ − T') et erreur
  N(0, σ_j)) ; « contenu » (le paragraphe fait partie du contenu : pas de compression, erreur N(0, s₀_j)). La variante
  « contenu » n'est pas définie quand deux juges au moins ont s₀ = 0 et le même gain : leurs gains d'écart seraient
  exactement égaux (modèles K16 et KH).
- **G5.** Aucun autre lien entre juges que la lecture vraie commune ; erreurs indépendantes entre juges, cellules et
  tâches.
- **Nul.** gp_j = gu_j égaux chez les trois juges. Le texte ne lie pas ces gains au g de la grille ; deux lectures :
  « lié » (gp = gu = g de la case, 0 sans attaque) et « fort » (gp = gu = 0,30 quel que soit g).
- **k_P** = 3 (décision D-2 retenue, trois niveaux) et k_P = 1 pour information. Nombre de tâches de TC.2 = T de la
  case.

Bras joués dans les mêmes essais : « bruit » (les deux gains d'écart sont six tirages N(0, 1) indépendants : cas idéal
où la loi exacte vaut pour ces deux évaluateurs ; c'est le modèle U1 de l'archive ; cas sain) ; « insertion » et
« contenu », k_P = 3 et 1, « lié » ; les mêmes à k_P = 3, « fort » ; et un diagnostic hors du texte, « S séparé »
(variante « insertion », mais le gain sous l'usurpation est calculé sur une relecture indépendante de S et H), qui
mesure la part du taux due au partage de S et de D₀.

Ce que le modèle ne couvre pas : désaccord entre juges propre à un contenu (au-delà de e₀) ; compression non
linéaire ; effet de longueur ; verdicts aux bords de l'échelle 0 à 9.

## 6. Résultats

Tables complètes, une ligne par case, avec chaque lecture seule : `grille/sorties/tables-completes-v1.md`. Tables
condensées : `grille/sorties/tables-condensees-v1.md`. Une sortie JSON par case sous `grille/sorties/` (taux, erreurs,
graine, versions, durée).

### 6.1 C-P3a et C-P3b — étendue du taux de « établie » sous le nul sur les couples k × T

Passe 0 : 1 000 essais, 1 000 tirages, seuil 0,0638. Erreur de Monte-Carlo d'un taux aux trois lectures : 0,002 à 0,007.

| modèle | g | cases | C-P3a, trois lectures | C-P3b, trois lectures | C-P3a, deux lectures | C-P3b, deux lectures |
|---|---|---|---|---|---|---|
| E30 | 0 | 4 | 0,027 à 0,049 | 0,028 à 0,041 | 0,029 à 0,049 | 0,030 à 0,043 |
| E30 | 0,10 | 4 | 0,016 à 0,022 | 0,020 à 0,028 | 0,019 à 0,024 | 0,023 à 0,035 |
| E30 | **0,20** | 4 | 0,003 à 0,015 | 0,016 à 0,023 | 0,006 à 0,016 | 0,022 à 0,026 |
| E40 | 0 | 1 | 0,036 | 0,048 | 0,038 | 0,050 |
| E40 | 0,10 | 1 | 0,010 | 0,033 | 0,013 | 0,039 |
| E60 | 0 | 4 | 0,028 à 0,042 | 0,034 à 0,048 | 0,029 à 0,045 | 0,034 à 0,050 |
| E60 | 0,10 | 4 | 0,021 à 0,024 | 0,019 à 0,038 | 0,024 à 0,027 | 0,022 à 0,042 |
| E60 | **0,20** | 4 | 0,009 à 0,012 | 0,009 à 0,022 | 0,013 à 0,019 | 0,019 à 0,032 |
| EH | 0 | 4 | 0,024 à 0,040 | 0,030 à 0,042 | 0,025 à 0,040 | 0,033 à 0,044 |
| EH | 0,10 | 4 | 0,008 à 0,023 | 0,022 à 0,031 | 0,013 à 0,025 | 0,026 à 0,037 |
| EH | **0,20** | 4 | 0,004 à 0,009 | 0,012 à 0,023 | 0,009 à 0,015 | 0,020 à 0,032 |
| K16 | 0 | 4 | 0,037 à 0,043 | 0,038 à 0,053 | 0,037 à 0,043 | 0,038 à 0,053 |
| K16 | 0,10 | 4 | 0,020 à 0,035 | 0,035 à 0,049 | 0,020 à 0,035 | 0,036 à 0,052 |
| K16 | **0,20** | 4 | 0,020 à 0,029 | 0,034 à 0,045 | 0,020 à 0,029 | 0,035 à 0,047 |
| KH | 0 | 4 | 0,024 à 0,043 | 0,033 à 0,051 | 0,024 à 0,043 | 0,033 à 0,052 |
| KH | 0,10 | 4 | 0,016 à 0,022 | 0,033 à 0,046 | 0,017 à 0,022 | 0,033 à 0,046 |
| KH | **0,20** | 4 | 0,023 à 0,027 | 0,024 à 0,038 | 0,023 à 0,028 | 0,026 à 0,038 |
| MH | 0 | 4 | 0,030 à 0,037 | 0,031 à 0,040 | 0,035 à 0,040 | 0,039 à 0,046 |
| MH | 0,10 | 4 | 0,013 à 0,017 | 0,022 à 0,031 | 0,036 à 0,051 | 0,046 à 0,058 |
| MH | 0,20 | 4 | 0,014 à 0,019 | 0,023 à 0,040 | **0,097 à 0,153** | **0,076 à 0,131** |
| M616 | 0 | 4 | 0,032 à 0,046 | 0,036 à 0,041 | 0,032 à 0,047 | 0,039 à 0,043 |
| M616 | 0,10 | 4 | 0,014 à 0,025 | 0,021 à 0,032 | 0,017 à 0,026 | 0,027 à 0,037 |
| M616 | 0,20 | 4 | 0,004 à 0,014 | 0,020 à 0,034 | 0,009 à 0,020 | 0,026 à 0,039 |

Bilan, trois lectures : C-P3a 0,003 à 0,049 ; C-P3b 0,009 à 0,053 ; aucune case au-dessus de 0,0638. Comparaison
nette (taux + 2 erreurs sous le seuil) dans toutes les cases de C-P3a et dans 84 des 86 de C-P3b.

Passe 1 (règle écrite dans `grille_ab_v1.py` avant tout résultat : toute case non nette est rejouée sur graine neuve
à 4 000 essais ; les deux passes sont rapportées, sans mise en commun) :

| case | passe 0 (1 000 essais), C-P3b | passe 1 (4 000 essais, seuil 0,0569), C-P3a | passe 1, C-P3b |
|---|---|---|---|
| K16, g = 0, k = 3, T = 45 | 0,053 ± 0,007 (non nette) | 0,034 ± 0,003 | 0,043 ± 0,003 (nette) |
| KH, g = 0, k = 3, T = 60 | 0,051 ± 0,007 (non nette) | 0,034 ± 0,003 | 0,040 ± 0,003 (nette) |

### 6.2 C-P3c — taux de « établie » aux trois lectures jointes sous le nul

8 000 essais par case, seuil 0,0549, erreur de Monte-Carlo 0,001 à 0,004. Étendue sur les quatre couples k × T ; entre
parenthèses, cases au-dessus du seuil.

| modèle | g | bruit (cas idéal) | insertion, k_P = 3, lié | contenu, k_P = 3, lié | insertion, k_P = 1, lié | insertion, k_P = 3, fort | diagnostic « S séparé » |
|---|---|---|---|---|---|---|---|
| E30 | 0 | 0,044 à 0,047 (0) | 0,079 à 0,088 (4) | 0,078 à 0,095 (4) | 0,074 à 0,080 (4) | 0,071 à 0,076 (4) | 0,041 à 0,050 (0) |
| E30 | 0,10 | 0,034 à 0,037 (0) | 0,052 à 0,060 (3) | 0,054 à 0,057 (3) | 0,046 à 0,050 (0) | 0,053 à 0,059 (3) | 0,030 à 0,035 (0) |
| E30 | 0,20 | 0,028 à 0,032 (0) | 0,041 à 0,048 (0) | 0,040 à 0,051 (0) | 0,037 à 0,043 (0) | 0,045 à 0,054 (0) | 0,026 à 0,030 (0) |
| E40 | 0 | 0,044 à 0,048 (0) | 0,082 à 0,084 (4) | 0,078 à 0,088 (4) | 0,071 à 0,080 (4) | 0,070 à 0,074 (4) | 0,044 à 0,046 (0) |
| E40 | 0,10 | 0,033 à 0,040 (0) | 0,053 à 0,062 (3) | 0,050 à 0,064 (2) | 0,044 à 0,055 (1) | 0,054 à 0,063 (3) | 0,032 à 0,037 (0) |
| E40 | 0,20 | 0,027 à 0,031 (0) | 0,037 à 0,048 (0) | 0,038 à 0,050 (0) | 0,035 à 0,045 (0) | 0,043 à 0,053 (0) | 0,026 à 0,032 (0) |
| E60 | 0 | 0,042 à 0,051 (0) | 0,076 à 0,088 (4) | 0,080 à 0,089 (4) | 0,076 à 0,079 (4) | 0,067 à 0,077 (4) | 0,043 à 0,052 (0) |
| E60 | 0,10 | 0,031 à 0,037 (0) | 0,055 à 0,059 (3) | 0,051 à 0,058 (2) | 0,047 à 0,051 (0) | 0,056 à 0,061 (4) | 0,033 à 0,037 (0) |
| E60 | 0,20 | 0,028 à 0,031 (0) | 0,035 à 0,048 (0) | 0,036 à 0,048 (0) | 0,035 à 0,043 (0) | 0,043 à 0,052 (0) | 0,023 à 0,030 (0) |
| EH | 0 | 0,038 à 0,049 (0) | 0,080 à 0,087 (4) | 0,078 à 0,091 (4) | 0,069 à 0,081 (4) | 0,069 à 0,076 (4) | 0,047 à 0,051 (0) |
| EH | 0,10 | 0,023 à 0,032 (0) | 0,043 à 0,051 (0) | 0,041 à 0,051 (0) | 0,040 à 0,047 (0) | 0,043 à 0,052 (0) | 0,027 à 0,030 (0) |
| EH | 0,20 | 0,018 à 0,021 (0) | 0,026 à 0,035 (0) | 0,026 à 0,033 (0) | 0,024 à 0,033 (0) | 0,031 à 0,039 (0) | 0,015 à 0,023 (0) |
| K16 | 0 | 0,043 à 0,050 (0) | 0,041 à 0,048 (0) | non défini | 0,045 à 0,050 (0) | 0,043 à 0,048 (0) | 0,043 à 0,048 (0) |
| K16 | 0,10 | 0,039 à 0,043 (0) | 0,037 à 0,044 (0) | non défini | 0,039 à 0,042 (0) | 0,035 à 0,043 (0) | 0,036 à 0,043 (0) |
| K16 | 0,20 | 0,033 à 0,040 (0) | 0,033 à 0,036 (0) | non défini | 0,035 à 0,037 (0) | 0,033 à 0,039 (0) | 0,034 à 0,038 (0) |
| KH | 0 | 0,041 à 0,054 (0) | 0,094 à 0,101 (4) | non défini | 0,078 à 0,088 (4) | 0,092 à 0,105 (4) | 0,088 à 0,105 (4) |
| KH | 0,10 | 0,025 à 0,031 (0) | 0,079 à 0,099 (4) | non défini | 0,069 à 0,081 (4) | 0,081 à 0,101 (4) | 0,083 à 0,094 (4) |
| KH | 0,20 | 0,016 à 0,022 (0) | 0,077 à 0,094 (4) | non défini | 0,064 à 0,076 (4) | 0,075 à 0,092 (4) | 0,075 à 0,091 (4) |
| MH | 0 | 0,041 à 0,049 (0) | 0,104 à 0,107 (4) | 0,082 à 0,089 (4) | 0,091 à 0,099 (4) | 0,100 à 0,107 (4) | 0,087 à 0,091 (4) |
| MH | 0,10 | 0,024 à 0,028 (0) | 0,091 à 0,106 (4) | 0,041 à 0,051 (0) | 0,078 à 0,097 (4) | 0,095 à 0,114 (4) | 0,078 à 0,100 (4) |
| MH | 0,20 | 0,017 à 0,021 (0) | 0,088 à 0,099 (4) | 0,028 à 0,030 (0) | 0,073 à 0,088 (4) | 0,090 à 0,103 (4) | 0,078 à 0,093 (4) |
| M616 | 0 | 0,044 à 0,047 (0) | 0,076 à 0,081 (4) | 0,079 à 0,084 (4) | 0,068 à 0,073 (4) | 0,067 à 0,070 (4) | 0,043 à 0,048 (0) |
| M616 | 0,10 | 0,029 à 0,038 (0) | 0,051 à 0,058 (1) | 0,052 à 0,057 (1) | 0,045 à 0,052 (0) | 0,054 à 0,063 (1) | 0,030 à 0,034 (0) |
| M616 | 0,20 | 0,026 à 0,029 (0) | 0,037 à 0,046 (0) | 0,040 à 0,045 (0) | 0,037 à 0,040 (0) | 0,046 à 0,047 (0) | 0,025 à 0,028 (0) |

Bilan par bras (cases nulles) :

| bras | cases définies | étendue | au-dessus du seuil | non nettes |
|---|---|---|---|---|
| bruit (cas idéal) | 96 | 0,016 à 0,054 | 0 | 3 |
| insertion, k_P = 3, lié (bras principal) | 96 | 0,026 à 0,107 | 54 | 7 |
| insertion, k_P = 1, lié | 96 | 0,024 à 0,099 | 45 | 5 |
| insertion, k_P = 3, fort | 96 | 0,031 à 0,114 | 55 | 12 |
| contenu, k_P = 3, lié | 72 | 0,026 à 0,095 | 32 | 12 |
| contenu, k_P = 1, lié | 72 | 0,023 à 0,082 | 26 | 5 |
| contenu, k_P = 3, fort | 72 | 0,027 à 0,080 | 35 | 12 |
| diagnostic « S séparé » | 96 | 0,015 à 0,105 | 24 | 2 |

Deux mécanismes, que le diagnostic sépare :

1. **Cellule S et D₀ partagés.** Sous l'erreur sur v₀ (E30 à E60, EH, M616), sans attaque : 0,076 à 0,095 avec S
   partagé, 0,041 à 0,052 avec S relu à part. L'erreur de lecture du juge sur S entre avec le même signe dans le gain
   sous le plaidoyer et dans le gain sous l'usurpation : deux des quatre évaluateurs s'accordent sans écart vrai. Sous
   la compression seule homogène (K16, v₀ exact), cet effet disparaît : 0,033 à 0,050.
2. **Compression différente d'un juge à l'autre.** KH et MH, variante « insertion » : 0,077 à 0,107 à tout g, et
   0,075 à 0,105 même avec S séparé. Si un paragraphe de l'agent comprime la lecture comme une insertion, le gain
   d'écart brut porte κ_j, qu'aucune des trois lectures ne retire (elles ne touchent que les Ḡ nets). Ce mécanisme
   dépend de G4 ; le premier n'en dépend pas.

Le taux baisse quand g monte dans les modèles d'erreur seule, parce que les trois lectures s'y accordent moins
souvent ; il passe encore le seuil dans 1 à 3 cases sur 4 à g = 0,10 et dans aucune à g = 0,20 (bras principal). La
clause demande « au moins une case » : les seize cases « aucune attaque » sous l'erreur seule suffisent, et elles ne
dépendent ni de G4, ni de k_P, ni de la valeur du gain du plaidoyer.

Aux deux premières lectures seules (ce que serait C-P3c sous la version (b) de D-9), bras principal : 0,032 à 0,337 ;
MH à g = 0,20 : 0,224 à 0,337.

## 7. Contrôles (R4, R5)

Les lignes C-P3a et C-P3b sortent propres (aucune case au-dessus) : contrôles faits pour montrer que la simulation
sait voir un taux haut.

| contrôle | attendu | obtenu |
|---|---|---|
| Artefact 1 : effet vrai, gains 0,04 / 0,10 / 0,16, k = 5, T = 60, 400 essais | taux haut | C-P3a 0,945 ; C-P3b 0,970 |
| Artefact 2 : effet vrai, gains 0,07 / 0,10 / 0,13, mêmes réglages | taux intermédiaire | C-P3a 0,557 ; C-P3b 0,532 |
| Artefact 3 : deux lectures seules, un mécanisme par juge, g = 0,20 (artefact connu du texte, lignes 733 à 735) | au-dessus de 0,10 à k = 5, T = 60 | C-P3a 0,153 ; C-P3b 0,131 ; trois lectures 0,015 et 0,031 |
| Artefact 4 : lecture calibrée seule, compression hétérogène, g = 0,20 | taux haut | C-P3a 0,156 à 0,276 ; C-P3b 0,100 à 0,182 |
| Artefact 5, C-P3c : effet vrai, plaidoyer dans le même ordre des juges que TC.1 | taux haut | 0,617 à 0,995 (variante « insertion », k_P = 3) |
| Artefact 6, C-P3c : effet vrai, plaidoyer dans l'ordre inverse (invariance fausse) | taux proche de 0 | 0,000 à 0,001 |
| Sain 1 : lois exactes du W | seuils du texte | 0,64 (p 0,0394) ; 0,8125 (p 0,0417) ; P(W ≤ 0,20) = 0,6327 |
| Sain 2 : erreur homogène 0,4, sans attaque, k = 3, T = 45 (case N0 du rédacteur : 0,043 et 0,045) | proche de 0,05 ou dessous, cohérent avec le rédacteur | 0,036 ± 0,006 et 0,048 ± 0,007 |
| Sain 3 : erreur homogène 0,4, g = 0,10, k = 5, T = 60 (case N1 du rédacteur : 0,019 et 0,022) | cohérent | 0,010 ± 0,003 et 0,033 ± 0,006 |
| Sain 4, C-P3c : bras « bruit », 96 cases | au plus le niveau exact 0,0417 dans les cases homogènes sans lien, sinon proche | 0,016 à 0,054, aucune au-dessus du seuil |
| Sain 5 : forme fermée de la loi jointe contre la grille (essai du module de l'archive) | « TESTS OK » | « TESTS OK » |

Recoupement avec le rejeu du rédacteur, case « un mécanisme par juge, g = 0,20, k = 5, T = 60 » (N5 chez lui) : deux
lectures 0,153 et 0,131 ici contre 0,149 et 0,150 ; lecture calibrée seule 0,299 et 0,186 contre 0,306 et 0,227. Le
dernier écart (0,041) fait un peu plus de deux erreurs de Monte-Carlo de la différence ; je le signale, je ne l'ai
pas rejoué.

Remarque sur le bras « bruit » : il monte jusqu'à 0,054 en lecture jointe, au-dessus du niveau exact 0,0417, parce que
les familles 1 et 4 partagent un témoin (indice 1 de la règle) et le régresseur ; trois de ses cases sont non nettes
et n'ont pas été rejouées (la règle de la seconde passe ne visait que C-P3a et C-P3b).

## 8. Ambiguïtés du texte rencontrées

- **A1. La grille n'est pas une liste finie.** « Écart type 0,3 à 0,6 », « κ jusqu'à 0,16 », « les trois juges pouvant
  différer » décrivent des plages. « La grille entière » n'a pas de sens exact ; j'ai joué les bornes, un cas
  hétérogène par mécanisme et deux mélanges. Une autre combinaison pourrait donner un autre taux.
- **A2.** Le texte ne dit pas si « aucune attaque » se croise avec tous les modèles d'erreur. Je l'ai croisée.
- **A3.** Sous « la compression », l'écart type de l'erreur d'insertion n'est pas donné (pris à 0,4, valeur de
  l'archive) ; v₀ est pris exact (réserve 15).
- **A4.** Le profil de g par famille et par rang, et le gain sur le corpus B, ne sont pas donnés (pris à l'archive).
- **A5. La grille ne définit rien pour les deux gains d'écart de C-P3c** : ni modèle, ni gain du plaidoyer, ni k_P, ni
  nombre de tâches. Tout le modèle de la section 5 est un choix de ce rapport, sauf le partage de S et de D₀, qui est
  la définition du point 13.
- **A6. Tirages dégénérés.** Le point 11 (lignes 758 à 759) et la liste d'arrêt (ligne 1521) disent qu'une statistique à
  plus de 1 % de tirages dégénérés est « non identifiable ». Le texte ne dit pas ce que devient une statistique de
  rang dont une composante Ḡ est dans ce cas. Lecture (i), celle des programmes de l'archive et des taux ci-dessus : on
  n'en tient pas compte. Lecture (ii) : la statistique n'est pas lue. Sous (ii), dans ce modèle, C-P3a n'est lisible
  dans aucun essai sans attaque, dans 0 à 94 % des essais à g = 0,10 selon le modèle (moins de 1 % sous l'erreur 0,6, 37 à 94 % sous l'erreur 0,3) et
  dans 25 à 100 % à g = 0,20 ; C-P3b (qui ajoute le corpus B de 30 items) dans moins de 3 % des essais jusqu'à g = 0,10 et dans 0 à 80 %
  à g = 0,20. Les taux de « établie » sous (ii) sont alors 0,000 à 0,029 (C-P3a) et 0,000 à 0,016 (C-P3b). La lecture
  (ii) ne charge pas la clause, mais elle ferait des lignes C-P3a et C-P3b des lignes le plus souvent illisibles
  quand les gains sont de l'ordre de 0,10. À trancher par le rédacteur avant le scellement ; hors de la question
  posée ici.
- **A7.** Aucune règle pour les ex æquo de rang. Aucun rencontré dans les bras définis (0 essai) ; c'est la raison pour
  laquelle la variante « contenu » est « non définie » sous la compression seule.
- **A8.** Le seuil s'applique case par case : une statistique exactement à 0,05 le passe dans environ 2 % des cases par
  le seul hasard, et la grille en compte des dizaines. Le texte ne dit pas si un rejeu peut lever un dépassement. La
  question ne s'est pas posée (aucun dépassement pour C-P3a et C-P3b ; dépassements de C-P3c à plus de cinq erreurs).
- **A9.** La clause demande « au moins 1 000 tirages » ; l'analyse réelle en fait 10 000 (point 11). Joué à 1 000.
- **A10.** La règle des témoins est jouée sur les longueurs de la configuration brouillon 3 de l'archive, non sur la
  configuration à sceller (verrou 4) ; les deux corpus emploient les longueurs du corpus A (hérité de l'archive). Le
  partage de témoins entre familles en dépend.

## 9. Ce que je n'ai pas pu jouer, et ce que j'ai réduit

- Modèle E40 pour C-P3a et C-P3b : deux cases de recoupement seulement. Le rédacteur a joué ses huit cases à g = 0 et
  0,10 ; **E40 à g = 0,20 n'est joué par personne** (E30 et E60, qui l'encadrent, le sont).
- Aucune autre combinaison hétérogène que EH, KH, MH ; aucun λ différent de 1 ; aucune compression non linéaire.
- 1 000 tirages au lieu de 10 000 ; 1 000 essais par case (le minimum de la clause) pour C-P3a et C-P3b, sauf les deux
  cases rejouées à 4 000.
- Variante « contenu » de C-P3c sous la compression seule (non définie) ; bras « bruit » non rejoué dans ses trois
  cases non nettes.
- **Budget.** La consigne bornait le calcul à une heure de processeur environ. Le calcul a pris environ 70 minutes
  d'horloge sur quatre cœurs, soit environ 4,3 heures de processeur cumulées (10 622 s pour C-P3a et C-P3b, 4 212 s
  pour C-P3c, 670 s pour la seconde passe). J'ai lu la borne en temps d'horloge ; en heures de processeur cumulées,
  elle est dépassée d'un facteur quatre. Je le signale.

## 10. Programmes, graines, manifestes

Programmes (`grille/programmes/`, manifeste `grille/sha256sums-programmes-v1.txt`,
`f629cca85478f57d241984a0acb330e99152b3dcc875b3196662f3ea1173d28b`) : `grille_commun_v1.py` (modèle, règles, modèle des
gains d'écart) ; `grille_ab_v1.py` (C-P3a, C-P3b) ; `grille_c_v1.py` (C-P3c) ; `lancer_passe0_v1.sh`,
`lancer_passe1_v1.sh` ; `resume_grille_v1.py`, `tables_condensees_v1.py` (mise en tables, aucun calcul). Les trois
programmes de calcul et le premier lanceur sont figés avant le lancement
(`grille/sha256sums-programmes-avant-lancement.txt`, `c5bc961a81041bc680806c8387a9fea243cc6fe4d070d0cb6f20aae5bd0a47b6`,
revérifié avant la seconde passe).

Fonctions de l'archive reprises (`grille/archive/`, manifeste `grille/sha256sums-archive-v1.txt`,
`1d203e8b945c95cc8df850a0cba764714cd779666c48122bd04afb0cae7e56f8`) : `commun_b5_v1.py` (`ea085f6f…`),
`t2_rang_temoins_partages_v1.py` (`126ac0a3…`), `t1_loi_nette_rejeu_v1.py` (`f32ecd9d…`, importé par le précédent),
copiés de `registres/papier-c/redaction-brouillon6-relance-v1/redacteur/travail/rejeu-grille-c1/` (empreintes
conformes à son manifeste) ; `papier-C-config-v1-brouillon3.json` (`85173b22…`, longueurs seulement).

Graines (R9) : `numpy.random.SeedSequence(20261119, spawn_key = (programme, case, passe))`, programme 1 pour C-P3a et
C-P3b, 2 pour C-P3c ; case = 1000 × rang du modèle (E30 0, E40 1, E60 2, EH 3, K16 4, KH 5, MH 6, M616 7, P3 8, P6 9)
+ 100 × rang de l'attaque (0 ; 0,10 ; 0,20) + 10 × k + (0 pour T = 45, 1 pour T = 60) ; passe 0 ou 1. L'entropie et
la clé sont écrites dans chaque sortie JSON (champ `graine`), avec les versions.

Sorties (`grille/sorties/`, manifeste `grille/sha256sums-sorties-v1.txt`,
`9ab5c8a8ef8426e6f4f256957f9fa3f886f214139a955845465d372de2988048`, 198 lignes) : 100 sorties de C-P3c
(`c_*_p0.json`), 88 de C-P3a et C-P3b en passe 0 et 2 en passe 1 (`ab_*.json`), listes des cases, témoins de fin, les
deux fichiers de tables. Les 190 fichiers d'erreurs des lancements sont vides.
