# Contre-lecture (R2) — preuve de validité du nul limité et préenregistrement de l'idée 1.1 — v1

- **Contre-lecteur** : sous-agent neuf de la session mère (modèle B au sens de R-2851) ; je n'ai écrit ni la preuve, ni le
  préenregistrement, ni le relevé, ni les fiches, ni le juge, ni les nuls v8 et v9.
- **Date** : 2026-11-15, 08:56 UTC (`date -u`) ; dépôt lu sur `main`, tête `441ead76` ; lecture seule, aucun commit.
- **Pièces contre-lues** (empreintes recalculées, égales à leurs compagnons) :
  - `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md` — `44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2` (ci-dessous **[PREUVE]**) ;
  - `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md` — `46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089` (ci-dessous **[PRÉ]**).
- **Aucun résultat du banc n'existe** : rien n'a été joué, rien n'a été lu. Mes seuls calculs sont des comptes sur
  processeur, sans code du juge (section 4).

## Verdicts

- **Preuve : scellable après corrections.** Aucun pas faux. Le théorème 1 est juste, les huit hypothèses suffisent, la
  garantie est bien dite « sur la classe du nul limité seulement ». Six corrections mineures (une tolérance contredite par
  le code du v9, deux hypothèses dites sans dire qu'elles ne sont pas nécessaires, une remarque à borner au pari plein, un
  statut périmé depuis la copie du v9).
- **Préenregistrement : scellable après corrections.** Quatre majeurs, tous réparables sans changer l'idée ; neuf mineurs.
  Aucun jeu avant la version 2 corrigée et scellée par `controle_ia.prereg.sceller_prereg`.
- **Constat du concepteur sur les poids appris : confirmé**, refait deux fois (son script rejoué à l'octet, puis un
  programme à moi, autre famille de mondes).

## 1. Ce que j'ai lu et vérifié

| pièce | vérification |
|---|---|
| [PREUVE], [PRÉ] | empreintes égales aux compagnons |
| relevé, § 1.1 et § 7 (`bd253b6c…`) ; fiches n° 0 et n° 14 (`a9f9594e…`), champs `demande_organisme` lus en entier | empreintes égales ; les fiches disent bien ce que [PREUVE] § 8 leur prête (moitié des tirages pour la n° 0 ; descente exponentielle en ligne et « martingale de valeur initiale 1 » pour la n° 14) |
| copie du nul v9, `copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py` | `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95`, égale à l'attendue ; lu en entier (584 lignes) ; **jamais exécuté** ; les deux fichiers d'essai survolés (`d42a50eb…`, `f004dba6…`) |
| copie `94bfd92` du code du juge | `sha256sum -c empreintes-copie-v1.txt` : 53 sur 53 ; lus : `selection_pari.py` (`_condition`, `proba`, `_normaliser`, `trajectoire_numerateur`), `nul_filles_v2.py` (`construire_engagement_v2`, `_lineaire`), `cycle.py` (`membres_de_l_archive`, `appliquer_multiplicite`, `instants_reguliers`), `a_blanc_v59.py` (`juger_carte`) |
| audit du verdict du v9 (`9086a420…`) | 0,105 ; [0,0894 ; 0,1223] (l. 34 et 38) ; M01 986 et M02 972 sur 1 000 (l. 33 et 159) : **exacts** |
| note W2 (`4d3a6d1c…`) | « 0,25 à 0,29 s mesurées » (l. 44) ; « moins de deux lois connues » (l. 61) : **exacts** |
| page publique (`c549a31b…`, l. 64) | citation exacte |
| R-1779, R-1768, R-2851, R-2873, R-2874 | lus ; conformes à ce que les deux pièces en disent |
| gabarit (`8cad4371…`), validateur (`3b2e3ee5…`) | `prereg.problemes([PRÉ])` rend un seul défaut : « section Contre-lecture sans les deux empreintes exigées » — attendu pour un brouillon v1 |
| cinq PDF des citations obligatoires | présents, débuts d'empreinte égaux (`a3c4b370`, `dcfbb9aa`, `957ef473`, `351f49d8`, `2a8ded01`) ; contenu non relu (aucun chiffre n'en est tiré) |

## 2. La preuve

### 2.1 Ce qui tient (vérifié pas à pas)

- **Théorème 1, pas 1 à 4** : justes. Le dénominateur domine la vraisemblance du monde (H3, H4) ; le rapport Λ est une
  surmartingale positive de départ 1 dans l'ordre du plan ; l'inégalité de Ville borne tous les instants à la fois. Tout
  membre de plus au dénominateur ne fait que baisser W : ni les membres ordinaires (dont la marginale ajustée sur les
  issues mêmes), ni le nombre de partitions n'entrent dans la borne. La remarque (i) est donc **démontrée**.
- **Lemme du certificat (§ 3)** : juste. Le polytope est l'enveloppe convexe des sommets annoncés (tout point s'écrit
  r·(part aveugle seule) + (1 − r)·(un point du produit des simplexes par cellule)) ; ∇f·u = t ; la borne par 0 est licite.
  C'est, à la lettre, ce que calcule `nul_v9._certificats` (l. 218 à 229).
- **La famille de [PREUVE] § 3 est bien celle du v9** — point laissé ouvert par l'auteur, **tranché sur le code** :
  `nul_v9.py`, l. 19 à 25 et l. 234 : poids propres à chaque morceau, bruit aveugle **commun**, Σ_j a + Σ_k r = 1 **par
  morceau**. La coupe d'un seuil est {z ≤ s} | {z > s} (l. 414), même sens que `selection_pari._condition` (« > seuil »).
- **§ 6 (a)** (limité sous v8) : juste. **§ 6 (b)** (limité à un niveau au-dessus du v9, à l'écart de certificat près) :
  juste sur le code — le v9 parcourt s = −∞ et chaque valeur distincte du trait parmi les t instances (l. 413), donc la
  partition qu'induit un seuil de l'archive sur l'échantillon est l'une de ses coupes ; une coupe élaguée garde son
  certificat dans le maximum (l. 39 à 41, 276, 317, 459), donc D⁹ domine le maximum de chaque famille F_P. L'écart à
  retenir est l'`ecart_residuel` du membre limité (valeur − atteinte), qui majore l'écart vrai.
- **§ 8 (variantes des fiches non valides)** : la démonstration est juste (Σ_y P*²/p_w ≥ 1, égalité si et seulement si
  p_w = P*) ; le calcul est confirmé (section 4).
- **Portée** : § 0 point 2, § 6 (d) et § 7 disent sans détour que rien n'est garanti hors de la classe limitée.

### 2.2 Corrections à la preuve (mineures ; aucune ne touche le théorème)

**p1 — tolérance d'arrêt contredite par le code du v9** ([PREUVE] l. 184 ; `nul_v9.py` l. 108 et l. 286).
Le code arrête une question (membre, instant) dès que la plus haute borne est à moins de `TOLERANCE_GROUPE = 1e-3` de la
meilleure valeur atteinte ; avec une seule coupe par question, l'écart d'un membre limité finira près de 10⁻³, pas de 10⁻⁴.
- ancien : « Avec une tolérance d'arrêt de l'optimiseur de 10⁻⁴ nat (préenregistrement), La et Ld promeuvent tout ce que le
  v9 promeut, sauf égalité à 10⁻⁴ nat près »
- nouveau : « Avec la tolérance d'arrêt du code du v9 (`TOLERANCE_GROUPE` = 10⁻³ nat, `nul_v9.py`, l. 108), inchangée, La
  et Ld promeuvent tout ce que le v9 promeut, sauf quand log W⁹ dépasse le seuil de moins que l'écart résiduel du membre
  limité (au plus 10⁻³ nat quand l'optimiseur a convergé ; mesuré à chaque évaluation) »

**p2 — H7 est suffisante, non nécessaire** (l. 141). Le pas 4 borne **tous** les t de 1 à n : n'importe quel ensemble
d'instants de lecture est couvert dès que D_t est calculé sur les t premières issues. La preuve le montre elle-même sans le
dire.
- ancien : « **H7 (instants).** T est fini et fixé d'avance (`instants_lecture` sous l'empreinte). »
- nouveau : « **H7 (instants).** T ⊂ {1, …, n}, et D_t ne lit que les t premières issues. Que T soit fixé d'avance
  (`instants_lecture` sous l'empreinte) n'est pas nécessaire au théorème (le pas 4 couvre tous les instants) ; c'est une
  discipline de gel, gardée. »
  De même en H8 (l. 142), retirer « ou des instants » de la parenthèse, ou écrire « (non nécessaire pour les instants,
  pas 4) » ; « pas de meilleur de plusieurs nuls », lui, **est** nécessaire. Et en H5 (l. 137) : le plancher 10⁻¹² n'est pas
  nécessaire à la borne (il suffit que q(· | passé) soit une loi) ; il garde seulement log W fini — vérifié :
  `selection_pari._normaliser` renormalise après le plancher, la somme vaut 1.

**p3 — remarque (ii) : vraie pour le pari plein seulement** (l. 158). Avec le numérateur « pari à fraction »
(`selection_pari.trajectoire_numerateur`, champ `fractions`, v7), le numérateur est un mélange qui contient la marginale
en ligne : W reste sous une surmartingale (Ville tient) mais « W_t ≤ 1 à chaque tirage » n'est plus garanti. Sans effet sur
le banc (`juger_carte` et `construire_engagement_v2` n'emploient pas `fractions` — vérifié), mais la règle d'audit A1 en
dépend.
- ancien : « son numérateur est la vraisemblance d'un point θ_carte de la famille, donc ≤ D_t »
- nouveau : « sous le pari plein (engagement sans `fractions`, cas de `juger_carte` et du banc), son numérateur est la
  vraisemblance d'un point θ_carte de la famille, donc ≤ D_t ; sous le pari à fraction, seule la borne de Ville vaut »

**p4 — corollaire e-BH : « la même hypothèse » est trop large** (l. 170). La bibliothèque dépend de la carte (parents d'une
fille) : les hypothèses nulles peuvent différer d'une carte à l'autre ; et `appliquer_multiplicite` ajoute un cumul
d'héritage à la valeur e d'une fille et ne fixe m que si `m_fixe` est donné.
- ancien : « Toutes les cartes d'une génération testant la même hypothèse « le monde est dans la classe de 𝒩_L(C) », ce
  taux est, sous cette hypothèse, la probabilité d'au moins une promotion. »
- nouveau : « Pour des cartes fraîches jugées sur la même archive (même classe, sans héritage, m fixé avant toute issue),
  si le monde est dans cette classe, ce taux est la probabilité d'au moins une promotion. Le théorème de la règle sur
  valeurs e est cité d'après `cycle.py` et n'a pas été relu sur PDF ; le banc ne s'en sert pas (promotion de la carte
  seule). »

**p5 — § 6 (d) vaut pour La et Ld, pas pour La2** (l. 191).
- ancien : « les promotions du nul limité sont encadrées par celles du v9 (en dessous) et celles du v8 (au-dessus) »
- nouveau : « les promotions de La et de Ld sont encadrées par celles du v9 (en dessous, à l'écart de certificat près) et
  celles du v8 (au-dessus) ; celles de La2 ne sont bornées que par le v8 »
  Ajouter au § 6 la conséquence, utile au préenregistrement (majeur M3) : 𝒫₁(C_arch) ⊂ 𝒫₂(C_arch) et
  𝒫₁(C_arch) ⊂ 𝒫₁(C_arch ∪ C_decl), donc, trajectoire par trajectoire et à l'écart de certificat près,
  **W^La2 ≤ W^La et W^Ld ≤ W^La**.

**p6 — statut périmé** (l. 50 à 61, 107, 385, 482) : la copie du v9 est versée (R-2874) et lue.
- ancien : « **Le code du nul v9 n'est pas dans ce dépôt.** […] la section 6 (b) en dépend et doit être relue sur le code. »
- nouveau : « Le code du nul v9 est versé en copie empreintée (`copie-nul-v9-a41b7b5/`, R-2874, `7ae450df…`). La famille de
  la section 3 est celle du code (l. 19 à 25, l. 234) ; la section 6 (b) est relue sur lui (coupes l. 413 à 416, élagage
  l. 276 à 288). »

**Réserve, sans correction demandée** : Wasserman, Ramdas et Balakrishnan (2020), Wang et Ramdas (2022), Grünwald, de Heide
et Koolen (2024) sont cités sans PDF au dépôt ; aucun chiffre n'en vient et la preuve se suffit (Ville est démontrable en
trois lignes). À garder sous la mention « non relu sur PDF », déjà écrite. La vérification (a) du § 10 (lemme du certificat,
300 jeux) n'a pas été rejouée par moi ; ma ligne B (section 4) la recoupe par un autre programme.

## 3. Le préenregistrement

### 3.1 Ce qui tient

Gabarit : les huit sections y sont, remplies. Prédictions chiffrées avec signe et réfutation écrite (P1 à P10). Issues
contraires écrites (étage 3 « prix non reproduit », issues (C) et (D)) : R3 respecté dans la lettre. Audit de symétrie
pour toute issue, « trop propre » dans les deux sens et « toutes les prédictions vraies » : R4. Graines par
`numpy.random.SeedSequence(entropy=racine, spawn_key=(i_ligne, r))`, manifeste : R9. Compte des cellules : 15 fatales et 4
de taille, **recompté, exact** (Q1 × 5 ; Q2 × 4 ; Q3 × 2 ; Q4 × 2 ; Q5 × 1 ; Q6 × 1 ; Q7 × 4). Appartenance aux classes du
tableau : exacte, vérifiée ligne à ligne contre la famille du code. La garantie n'est invoquée que sur la classe du bras
(H-a) ; rien de plus n'en est tiré. L'adoption d'un nul limité est écrite comme version neuve du juge, nœud de Lazar
(l. 278 à 279, issue (A)). La question de sens est rangée dans « ne décide pas » (l. 282) et l'issue (B) y renvoie. Aucun
chiffre de l'état de l'art extérieur ; les chiffres internes cités sont exacts (section 1).

### 3.2 Majeurs

**M1 — le banc ne porte aucune vraie découverte posée sur une coupure de l'archive : la part recouvrée de La est tirée vers
le haut par la composition des lignes** ([PRÉ] l. 138 à 141, l. 156 à 159 ; P6 l. 79, P7 l. 80).
Six des douze lignes V (V2, V4) portent leur structure **sur une partition de Ld** (signe d'un trait, sous-population) —
P7 le dit et s'en sert pour prédire que Ld recouvre peu. **Aucune** ne la porte sur une partition de La : V3 écarte
exprès son seuil de 0,3 de toute coupure de l'archive. Or c'est le cas où La paierait le prix du v9 (la famille F_P absorbe
une composante conditionnelle posée sur P, comme le v9 l'a fait sur I02), et c'est le cas attendu dans l'organisme, où une
fille affine les conditions de ses parents. L'issue prédite (« La recouvre, Ld non », issue (B)) est donc en partie écrite
par le choix des lignes : le banc ne mesure pas ce que H-1.1 affirme sans cette restriction (R3 dans l'esprit).
- ancien (l. 161) : « 19 lignes de lecture (Q1 à Q7, V1 à V4 à trois doses). »
- nouveau : ajouter « **V5(γ) composante conditionnelle à une coupure de l'archive**, γ ∈ {0,4 ; 0,8 ; 1,2} : comme V2,
  avec la condition {z_{jA} > s_A} de l'archive ; classes qui contiennent M : aucune » ; « 22 lignes de lecture » ; doses
  de V5 placées par le compte de l'annexe A rejoué (sans juge). Dans la métrique : ρ_X calculée **sur toutes les lignes
  informatives, V5 comprise** (critère principal), et rapportée par strate « structure hors des partitions du bras » /
  « structure sur une partition du bras ». Dans H-1.1 et P6 : une prédiction chiffrée propre à V5 (attendu par [PREUVE]
  § 6 (b) et le précédent I02 : La et Ld y recouvrent peu). Le banc B étant partagé avec le préenregistrement de l'idée
  1.2, la ligne ajoutée est à reporter là-bas ou à déclarer propre à 1.1.

**M2 — « le seul changement est la liste des partitions » est faux sur le code ; l'entrée de J9 renvoie à un fichier qui
n'est pas dans la copie** (l. 167 à 174, l. 193 à 196).
Lu sur `nul_v9.py` : (i) `_coupes` (l. 398 à 417) ne connaît que deux partitions — « sous_population » et « seuil » sur un
trait, **toutes les coupes** ; une partition à **seuil fixé** n'existe pas : il faut un type neuf, et un autre pour le
croisement de deux conditions ; (ii) la garde `exiger_membres_v9` (l. 181 à 205) refuse tout membre par morceaux qui n'est
pas l'un des trois attendus : elle doit être réécrite ; (iii) `membres_morceaux` (l. 150 à 163) est à remplacer ; (iv)
`maximiser_par_lots` accepte déjà un nombre quelconque de morceaux (M de forme (P, n, C)) : La2 ne demande **pas** d'étendre
le solveur, contrairement à ce que craint la l. 172. Et `banc_tricheurs_v9.py`, où l'entrée de J9 est « à relever »
(l. 168), n'est pas dans la copie versée (trois fichiers : le nul et ses deux essais).
- ancien (l. 169 à 170) : « le module du v9, **copié sous un nom neuf** (R12), dont le seul changement est que la liste des
  partitions devient un paramètre »
- nouveau : « le module du v9, copié sous un nom neuf (R12), avec **quatre changements déclarés, et eux seuls** : (1) deux
  types de partition ajoutés à `_coupes` — « seuil_fixe » (indice, seuil : une seule coupe {z ≤ s} | {z > s}) et
  « croisement » (deux conditions : une coupe, quatre morceaux au plus) ; (2) `membres_morceaux` prend la liste des
  partitions en paramètre ; (3) la garde `exiger_membres_v9` vérifie cette liste (présence unique, lois connues exactes,
  partition exacte, aucun membre de trop) ; (4) noms des membres. Le solveur (`maximiser_par_lots`, `_certificats`), ses
  constantes et `evaluer_sur_issues` sont inchangés, octet pour octet (différentiel joint à l'addendum). »
- ancien (l. 167 à 168) : « construit pour une carte fraîche comme le banc de sa validation le fait (entrée à relever sur la
  copie, `banc_tricheurs_v9.py`, `7e4bff59…`) »
- nouveau : « bibliothèque = `BIBLIOTHEQUE_STANDARD` + marginale d'entraînement + `nul_v9.membres_archive_v9(archive, None,
  3, 2)` ; engagement par `nf.construire_engagement_v2("fiche", loi, instances, 3, 0,05, bibliothèque, 0, None, instants,
  plan_execution="ordre_naturel")` ; évaluation par `nul_v9.evaluer_v9` (comme `test_nul_v9.py`, l. 330 et 365) »
  Et retirer partout « absent de ce dépôt » (l. 21 à 22, 193, 273 à 276) : copie versée, R-2874.

**M3 — P8 ne peut pas être réfutée, et deux gardes de nichage manquent** (l. 81 ; liste d'arrêt l. 256 à 257).
𝒫₁(C_arch) ⊂ 𝒫₂(C_arch) : W^La2 ≤ W^La trajectoire par trajectoire (à l'écart de certificat près), donc ρ_La2 ≤ ρ_La **par
construction** ; la réfutation écrite (« ρ_La2 > ρ_La + 0,05 ») est impossible. De même 𝒫₁(C_arch) ⊂ 𝒫₁(C_arch ∪ C_decl) :
ρ_Ld ≤ ρ_La par construction, ce que le texte ne dit nulle part alors que la table des issues en dépend (« Ld recouvre »
entraîne « La recouvre »).
- ancien (P8) : « − ou 0 | ρ_La2 ≤ ρ_La ; écart ponctuel ≥ 0,05 | ρ_La2 > ρ_La + 0,05 »
- nouveau (P8) : « − (le signe est de construction, [PREUVE] § 6 ; seule l'ampleur est prédite) | ρ_La − ρ_La2 ≥ 0,05 |
  ρ_La − ρ_La2 < 0,05 en estimation ponctuelle »
- ajouter à la liste d'arrêt : « log W de La2 ou de Ld > log W de La + écart résiduel de La + 10⁻⁶ à un instant → arrêt ;
  défaut de code », avec son essai sain et son artefact ; et, sous la table des issues : « ρ_Ld ≤ ρ_La et ρ_La2 ≤ ρ_La par
  construction : seules les issues (A), (B), (C), (D) telles qu'écrites sont possibles ».

**M4 — tolérances : 10⁻⁴ nat contredit le code (10⁻³), et P10 contredit la liste d'arrêt** (l. 125 à 126, l. 83, l. 257 à
258). Voir p1. Telle quelle, la ligne « plus de 1 % des évaluations avec un écart > 10⁻⁴ » se déclenchera presque à coup
sûr, et P10 arrête le run sur un seuil fixe (10⁻⁴) là où la liste d'arrêt emploie l'écart réel.
- ancien (l. 125 à 126) : « arrêt de l'optimiseur des membres par morceaux à un écart de certificat ≤ 10⁻⁴ nat ou au nombre
  maximal de pas du code du v9 »
- nouveau : « arrêt de l'optimiseur selon les constantes du code du v9, inchangées (`TOLERANCE_GROUPE` = 10⁻³ nat,
  `PALIERS_MU`, `PAS_MAX_PAR_PALIER`) »
- ancien (P10) : « toute perte appariée de La ou Ld sous J9 au-delà de 10⁻⁴ nat de certificat (arrêt, liste d'arrêt) »
- nouveau (P10) : « tout log W de La ou de Ld sous celui de J9 de plus que l'écart résiduel du membre limité + 10⁻⁶ nat
  (arrêt, liste d'arrêt) »
- ancien (l. 258) : « plus de 1 % des évaluations avec un écart de certificat > 10⁻⁴ nat »
- nouveau : « plus de 1 % des évaluations avec un écart résiduel > 2·10⁻³ nat »

### 3.3 Mineurs

**m1 — ordre du gel et des tirages** (l. 176 à 181). Le banc tire les issues **avant** que les bras bâtissent leur
engagement : c'est l'inverse de H1 et H2 de [PREUVE], sur lesquelles repose H-a.
- ancien : « le banc tire une fois l'archive, […] le plan de 200 instances et les 200 issues fraîches […]. Chaque bras
  construit son engagement »
- nouveau : « le banc tire l'archive, les paramètres, l'entraînement et le plan ; les cinq bras construisent et gèlent
  leur engagement ; **ensuite seulement** les 200 issues sont tirées, d'un générateur de clé `(i_ligne, r, 1)` distinct de
  celui du plan `(i_ligne, r, 0)` ; la fonction qui bâtit un engagement ne reçoit aucune issue fraîche (essai) »

**m2 — coupure de l'archive trop proche du signe** (l. 139 à 141). L'exclusion |s| < 0,05 garantit l'appartenance formelle,
pas l'écart utile : pour Q4 et V2, une coupure de l'archive sur le même trait à 0,05 ou 0,1 de zéro rend la famille de La
presque égale à celle du signe (quelques instances sur 200 les séparent). P4 (« La ≥ 0,85 sur Q4 ») en devient fragile —
estimation de lecteur, non calculée : une coupure à moins de 0,2 de zéro arrive dans environ un tirage sur six.
- ancien : « retirés tant que |s| < 0,05 »
- nouveau : « retirés tant que |s| < 0,3 (même écart que Q5 et V3) » ; ou garder 0,05 et ajouter aux mesures descriptives le
  taux de La sur Q4 et V2 par tranche de |cut(j)|.

**m3 — « faux positifs sur les copies » préjuge la question de sens** (l. 106 ; « trous rouverts », l. 77).
- ancien : « **Faux positifs sur les copies** : taux des cellules Q2 à Q6 »
- nouveau : « **Promotions de copies** (fausses ou non selon la réponse à la question de sens, ouverte : R-1768, R-1779) :
  taux des cellules Q2 à Q6 »

**m4 — ensemble I choisi sur les données qui servent à ρ** (l. 100 à 105). Le rééchantillonnage garde I fixe : le
dénominateur est gonflé par la sélection, ρ est biaisée vers le bas (prudent pour « recouvre », pas pour « ne recouvre
pas »).
- nouveau, à ajouter : « I est recalculé dans chaque rééchantillon (même règle) ; un rééchantillon à moins de 2 lignes
  informatives est écarté et compté. »

**m5 — P5 sans lecture entre 2 et 3 lignes** (l. 78). Ajouter : « 2 ou 3 lignes informatives : P5 partielle ».

**m6 — graines de l'essai E0 non écrites** (l. 202). Ajouter : « `spawn_key=(98, r)` ».

**m7 — R5 : gardes à nommer** (l. 197 à 200). Écrire que **chaque** ligne de la liste d'arrêt (empreinte de la copie, E0,
exception, log W non fini, monotonie, nichages, durée, lecture avant scellement) a son essai sain et son artefact, en plus
des mutations.

**m8 — audit A1 à borner au pari plein** (l. 118 à 119) : ajouter « l'engagement de chaque bras est sans `fractions`
(vérifié par un essai) » ; voir p3.

**m9 — section « Contre-lecture » de la version 2** : citer en entier l'empreinte du brouillon relu (`46ef2b92…c089`) et
celle de ce rapport, sans quoi `sceller_prereg` refuse ; déclarer aussi que P3 et les temps viennent d'un essai à blanc
antérieur (déjà dit en annexe B : bien).

## 4. Le constat sur les « poids appris » : refait

**(a) Script du concepteur rejoué** ([PREUVE] § 8.3, extrait du texte) : empreinte du script extrait
`865025d9915150d3cfac98cfbb7e9eb19fe414ffcb52bd14d199758351b2a7d9` et de sa sortie
`673a7a1aeefbe4793680477cc4c9c6dfad6ac32e812b7c106a5446733c28ebdf` — **égales à celles qu'il déclare** ; 24 secondes. Les
chiffres 96,5 % à 100 % (en ligne) et 64,9 % (moitié) sont donc reproduits à l'octet.

**(b) Programme à moi**, autre famille : lois connues softmax qui dépendent de deux traits, partition à seuils fixés (2 ou 4
cellules), monde = membre tiré au hasard de la famille de [PREUVE] § 3 (part aveugle commune), carte = copie exacte ;
1 000 mondes ; variante « moitié » brute puis lissée (pour écarter l'objection « c'est le plancher 10⁻¹² qui fait le
chiffre »). Script `27e5ed0b08e0288e02462663f4def673a1c38918f23c197ae98d91c5bb064f4e`, sortie
`e0d244f2e127f902e5c0f26205fcc07d70ed9c2f5a3d419a374b640efe65e112` (dossier de travail de la session, recopiés en
entier ci-dessous ; 2 min 55 s) :

```
[2 cellules] A en ligne eta=0.02 : copie promue 0.982 ; log W final médian 12.70
[2 cellules] A en ligne eta=0.05 : copie promue 0.986 ; log W final médian 10.30
[2 cellules] A en ligne eta=0.2 : copie promue 1.000 ; log W final médian 22.30
[2 cellules] A moitié, lissage 0.0 : copie promue en fin 0.481 ; log W final médian 2.81 ; moyenne de W tronquée à e^20 : 5.23e+06
[2 cellules] A moitié, lissage 0.05 : copie promue en fin 0.418 ; log W final médian 2.45 ; moyenne de W tronquée à e^20 : 2.01e+05
[2 cellules] A moitié, lissage 0.2 : copie promue en fin 0.366 ; log W final médian 2.33 ; moyenne de W tronquée à e^20 : 1.08e+03
[2 cellules] B maximum certifié sur les tirages mêmes (300 mondes) : promues copie 0/300 ; loi 1 seule 0/300 ; monde perturbé 0/300 ; monde vu deux fois (surconfiant) 0/300 ; plus grand log W d'une copie -0.11
[4 cellules] A en ligne eta=0.02 : copie promue 0.990 ; log W final médian 14.05
[4 cellules] A en ligne eta=0.05 : copie promue 0.988 ; log W final médian 11.66
[4 cellules] A en ligne eta=0.2 : copie promue 1.000 ; log W final médian 23.06
[4 cellules] A moitié, lissage 0.0 : copie promue en fin 0.763 ; log W final médian 6.86 ; moyenne de W tronquée à e^20 : 1.06e+08
[4 cellules] A moitié, lissage 0.05 : copie promue en fin 0.700 ; log W final médian 4.80 ; moyenne de W tronquée à e^20 : 8.63e+06
[4 cellules] A moitié, lissage 0.2 : copie promue en fin 0.592 ; log W final médian 3.71 ; moyenne de W tronquée à e^20 : 1.42e+05
[4 cellules] B maximum certifié sur les tirages mêmes (300 mondes) : promues copie 0/300 ; loi 1 seule 0/300 ; monde perturbé 0/300 ; monde vu deux fois (surconfiant) 0/300 ; plus grand log W d'une copie -0.287
```

Lecture : une copie exacte d'un membre du nul est promue dans 98 % à 100 % des mondes avec les poids appris en ligne, et
dans 37 % à 76 % avec les poids ajustés sur une moitié — lissage ou non — au lieu d'au plus 5 % ; avec le maximum certifié
sur les tirages mêmes, jamais (0 sur 300, log W toujours négatif), et trois cartes hors classe dans un monde de la classe
ne sont jamais promues non plus (taille tenue). **Le constat du concepteur est confirmé** ; le chiffre exact dépend du
monde et du réglage (64,9 % chez lui, 37 % à 76 % ici), le défaut non. La correction à porter au relevé (§ 1.1 : « c'est
la partie la plus neuve », « argon-p2-01 est la forme la plus propre ») est fondée.

```python
"""Contre-lecture (processeur seul, aucun code du dépôt) : lois connues qui dépendent des traits (softmax), partition à
seuils fixés, famille de la preuve § 3 (poids propres à la cellule, part aveugle commune).
A. variantes des fiches sur une copie exacte d'un membre : en ligne (descente exponentielle), moitié (maximum de
   vraisemblance, brut puis lissé) ; B. construction retenue (maximum certifié sur les tirages mêmes) : copie et cartes
   hors classe dans un monde de la classe (taille)."""
import sys
import numpy as np
K, D, N, ALPHA = 3, 2, 200, 0.05
T = np.arange(25, N + 1, 25); SEUIL = np.log(1 / ALPHA)

def soft(rng, W=None, b=None):
    W = rng.normal(0, 1.5, (K, D)) if W is None else W; b = rng.normal(0, .3, K) if b is None else b
    return W, b
def p_soft(Wb, z):
    s = z @ Wb[0].T + Wb[1]; s -= s.max(1, keepdims=True); e = np.exp(s); return e / e.sum(1, keepdims=True)

def monde(rng, cellules, J=2):
    lois = [soft(rng) for _ in range(J)]
    z = rng.normal(size=(N, D))
    sA, sB = rng.uniform(-1, 1, 2)
    cel = (z[:, 0] > sA).astype(int) if cellules == 2 else (z[:, 0] > sA).astype(int) * 2 + (z[:, 1] > sB).astype(int)
    PL = np.stack([p_soft(l, z) for l in lois], 1)            # (N, J, K)
    r = rng.dirichlet(np.ones(K)) * rng.uniform(0, .3)        # part aveugle commune
    mu = rng.dirichlet(np.ones(J), size=cellules) * (1 - r.sum())
    P = np.einsum("nj,njk->nk", mu[cel], PL) + r
    y = (rng.random(N)[:, None] > np.cumsum(P, 1)).sum(1).clip(max=K - 1)
    return dict(z=z, cel=cel, PL=PL, P=P, y=y, C=cellules, J=J, lois=lois)

def comp(m):  # composantes par instance aux issues observées : J lois puis K lois certaines
    n = np.arange(N); return np.concatenate([m["PL"][n, :, m["y"]], np.eye(K)[m["y"]]], 1)

def en_ligne(m, eta):
    G = comp(m); w = np.full((m["C"], G.shape[1]), 1 / G.shape[1]); s = 0; out = np.empty(N)
    for t in range(N):
        c = m["cel"][t]; p = w[c] @ G[t]
        s += np.log(m["P"][t, m["y"][t]]) - np.log(p); out[t] = s
        w[c] *= np.exp(np.minimum(eta * G[t] / p, 50)); w[c] /= w[c].sum()
    return out

def em(G, it=500):
    w = np.full(G.shape[1], 1 / G.shape[1])
    for _ in range(it):
        w = w * (G.T @ (1 / (G @ w))) / len(G); w /= w.sum()
    return w

def moitie(m, lissage):
    G = comp(m); h = N // 2; nb = G.shape[1]; w = np.full((m["C"], nb), 1 / nb)
    for c in range(m["C"]):
        i = np.where(m["cel"][:h] == c)[0]
        if len(i): w[c] = (1 - lissage) * em(G[i]) + lissage / nb
    p = np.maximum(np.einsum("tj,tj->t", w[m["cel"][h:]], G[h:]), 1e-12)
    return np.cumsum(np.log(m["P"][np.arange(h, N), m["y"][h:]]) - np.log(p))

def certifie(m, t, pas=400):
    """Borne haute du maximum de la famille (poids par cellule, part aveugle commune) sur les t premières issues."""
    C, J = m["C"], m["J"]; G = comp(m)[:t]; cel = m["cel"][:t]
    A = np.zeros((t, C * J + K)); 
    for c in range(C): A[cel == c, c * J:(c + 1) * J] = G[cel == c, :J]
    A[:, C * J:] = G[:, J:]
    x = np.concatenate([np.full(C * J, .5 / J), np.full(K, .5 / K)]); meilleur = np.inf
    for i in range(pas):
        gr = A.T @ (1 / (A @ x)); br = gr[C * J:].max(); bm = sum(gr[c * J:(c + 1) * J].max() for c in range(C))
        f = np.log(A @ x).sum(); meilleur = min(meilleur, f + max(0., max(br, bm) - t))
        v = np.zeros_like(x)
        if br >= bm: v[C * J + gr[C * J:].argmax()] = 1
        else:
            for c in range(C): v[c * J + gr[c * J:(c + 1) * J].argmax()] = 1
        d = v - x; g = 2 / (i + 3)
        # pas par recherche sur une petite grille (toujours admissible)
        cand = [g, g / 4, min(1, 4 * g) * .99]; x = max((x + a * d for a in cand), key=lambda u: np.log(A @ u).sum())
    return min(0., meilleur)

def main(R):
    rac = np.random.SeedSequence(915112026)
    for C in (2, 4):
        mondes = [monde(np.random.default_rng(s), C) for s in rac.spawn(R)]
        for eta in (0.02, 0.05, 0.2):
            l = [en_ligne(m, eta) for m in mondes]
            print(f"[{C} cellules] A en ligne eta={eta} : copie promue {np.mean([x[T-1].max() >= SEUIL for x in l]):.3f} ; log W final médian {np.median([x[-1] for x in l]):.2f}")
        for lis in (0.0, 0.05, 0.2):
            l = [moitie(m, lis) for m in mondes]
            print(f"[{C} cellules] A moitié, lissage {lis} : copie promue en fin {np.mean([x[-1] >= SEUIL for x in l]):.3f} ; log W final médian {np.median([x[-1] for x in l]):.2f} ; moyenne de W tronquée à e^20 : {np.mean(np.exp(np.minimum([x[-1] for x in l], 20))):.3g}")
        Rb = min(R, 300); promu = {"copie": 0, "loi 1 seule": 0, "monde perturbé": 0, "monde vu deux fois (surconfiant)": 0}; mx = -np.inf
        for m, s in zip(mondes[:Rb], rac.spawn(Rb)):
            rng = np.random.default_rng(s); n = np.arange(N)
            Wp = (m["lois"][0][0] + .25 * rng.normal(size=(K, D)), m["lois"][0][1])
            PLp = m["PL"].copy(); PLp[:, 0, :] = p_soft(Wp, m["z"])
            Pp = m["P"] + (PLp[:, 0, :] - m["PL"][:, 0, :]) * .5; Pp = np.maximum(Pp, 1e-12); Pp /= Pp.sum(1, keepdims=True)
            P2 = m["P"] ** 1.3; P2 /= P2.sum(1, keepdims=True)
            cartes = {"copie": m["P"], "loi 1 seule": m["PL"][:, 0, :], "monde perturbé": Pp, "monde vu deux fois (surconfiant)": P2}
            D_t = np.array([certifie(m, t) for t in T])
            for nom, Q in cartes.items():
                lw = np.cumsum(np.log(Q[n, m["y"]]))[T - 1] - D_t
                promu[nom] += lw.max() >= SEUIL
                if nom == "copie": mx = max(mx, lw.max())
        print(f"[{C} cellules] B maximum certifié sur les tirages mêmes ({Rb} mondes) : promues " + " ; ".join(f"{k} {v}/{Rb}" for k, v in promu.items()) + f" ; plus grand log W d'une copie {mx:.3g}")

main(int(sys.argv[1]))
```

## 5. Ce que je n'ai pas fait

Aucun code du dépôt tiers exécuté (lecture seule) ; aucun banc ; vérification (a) de [PREUVE] § 10 non rejouée ; PDF des
citations non relus (aucun chiffre n'en dépend) ; second préenregistrement du dossier (idée 1.2) non lu ; l'estimation de
m2 n'est pas calculée. Aucun commit, aucune poussée, aucun appel payant, rien sous `diag/`, `donnees/`, `docs/verdicts/`.

## 6. Suite demandée

Version 2 de chaque pièce sous un nom neuf (R12), avec le traitement écrit de chaque remarque (acceptée, refusée et
pourquoi) ; M1 change le banc partagé avec l'idée 1.2 : à trancher par la mère avant d'écrire le code. Aucun nœud neuf pour
Lazar ne sort de cette contre-lecture ; les nœuds déjà écrits (adopter un nul limité = version neuve du juge ; question de
sens) restent entiers.
