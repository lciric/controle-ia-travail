# Contre-lecture (R2) — préenregistrement « tirages frais du juge répartis par blocs avec arrêt anticipé » v1

- Contre-lecteur : sous-agent neuf (modèle B au sens de R-2851) ; je n'ai écrit ni le texte relu, ni le banc, ni la preuve,
  ni le relevé, ni les fiches, ni le juge.
- Date (UTC) : 2026-11-15. Dépôt lu sur `main`, aucun commit, aucune poussée, aucun appel payant, rien joué du banc.
- Texte relu : `docs/notes/organisme-idees-juge-v1/prereg-tirages-repartis-arret-anticipe-v1.md`
  (`2a500156d1b36855330e02c1a261cb40c882032ebf0090760e87b7695b876a65`, égale à son compagnon).

## Verdict

**Scellable après corrections.** La démonstration de validité est juste, et la divergence déclarée avec la critique est
fondée : je la confirme (section 1). Le texte n'est pas scellable tel quel pour trois raisons de plan, sans rapport avec le
théorème : la « fausse promotion » est définie par l'étiquette de construction et non par un oracle (M1) ; les critères gelés
de la principale se recouvrent et laissent un cas sans verdict (M2) ; l'épreuve de validité du banc ne peut pas voir les
défauts qu'elle est censée garder (M3). Trois majeurs, quatorze mineurs. Aucun écart caché à la conception scellée du juge.

## 1. Point à trancher : les deux conditions de la critique sont-elles nécessaires ?

**Réponse : non. Le concepteur a raison.** « Ordre de continuation jamais selon les valeurs e » et « dénominateur à poids
fixés d'avance, jamais recalibré » ne sont pas nécessaires. La seconde, prise à la lettre, n'est même pas suffisante.

### 1.1 Vérification pas à pas (lignes 61 à 99)

| pas | énoncé | lecture |
|---|---|---|
| a | Lemme (l. 68-76) : M_i(k) = Λ^(i) lu au nombre d'issues révélées est une surmartingale positive pour la filtration globale G_k | **Juste.** La décision « i reçoit le bloc » est connue à G_k ; les 25 issues neuves de i sont, sachant G_k, de loi P*(· \| x) et indépendantes de tout le révélé (C2, C3) ; chaque facteur q_i/P* a une espérance conditionnelle au plus 1 (somme de q_i sur le support de P*) ; l'espérance d'un bloc s'obtient par conditionnements successifs dans l'ordre du plan. |
| b | Domination W ≤ Λ à chaque instant lu (l. 86-87) | **Juste sous H3 et H4 de [PREUVE]** : le dénominateur est un majorant certifié du maximum de vraisemblance de la classe sur **exactement** les issues révélées de la carte ; lu dans le code : `nul_filles_v2.valeurs_ajustees` ajuste sur `G_tout[:t]` et `X_tout[:t]`, `evaluer_v2` prend le maximum sur les membres à chaque instant. C'est une inégalité trajectoire par trajectoire : aucune espérance, donc aucune condition sur la façon dont on est arrivé à cet instant. |
| c | Arrêt (l. 88-89) | **Juste.** Le dernier pas où i est lue, ou le premier pas où sa richesse révélée atteint m/α, est un temps d'arrêt borné de G ; E[e_i] ≤ E[M_i(σ_i)] ≤ 1. |
| d | e-BH sous dépendance quelconque (l. 89-90) | **Juste** : la règle n'exige que E[e_i] ≤ 1 pour chaque nul vrai, m fixé avant toute issue. |
| e | (c), l. 82-84 | **Juste**, avec la portée à écrire (mineur m9) : l'hypothèse nulle porte sur le monde ; quand le monde sort de la classe (famille T), le théorème ne dit rien des cartes fausses. |

Pourquoi les deux conditions tombent. La critique (réponse A du tour 3, `E3-T3-reponse-A.md`, l. 51-52) cherchait une preuve
**facteur par facteur** : E[E_t | F_{t−1}] ≤ E_{t−1} pour la richesse elle-même. Cette voie exige en effet un dénominateur
qui ne se recalcule pas. Le concepteur prend l'autre voie, celle de l'inférence universelle : la richesse W n'est **pas** une
surmartingale, mais elle est **dominée** par une surmartingale (Λ) pour chaque loi du nul. Cela suffit à tout temps d'arrêt,
et le temps d'arrêt peut dépendre des valeurs e de toutes les cartes, puisqu'elles sont des fonctions du révélé.

### 1.2 Hypothèses exactes sous lesquelles le théorème 2 tient

1. **Filtration** : G_k = toutes les issues révélées jusqu'au pas k, toutes cartes confondues, plus le hasard U du placebo.
   La surmartingale est Λ^(i) (rapport de la loi de la carte à la **vraie** loi du monde), pas W.
2. **Gel** : loi q_i, plan, instants, bibliothèque du nul, m et α fixés avant tout tirage frais de la génération ; q_i ne lit
   que ses propres issues passées dans l'ordre du plan ; les blocs sont révélés dans cet ordre.
3. **Flux indépendants** : sachant les objets gelés, les issues non révélées d'une carte sont indépendantes des issues
   révélées de toutes les cartes et de U ; le monde ne lit ni l'historique ni les autres cartes (C2, C3). C'est ici que
   passe toute la dépendance à l'allocation : sans C2, les issues d'une carte renseignent sur l'avenir d'une autre.
4. **Monde dans la classe et certificat** : P* appartient à une famille du nul, et la valeur du dénominateur majore le
   maximum de cette famille sur le préfixe révélé (exact pour le membre linéaire ; réserve héritée pour les membres
   log-linéaires).
5. **Règle non anticipante et bornée** : qui reçoit le bloc suivant et qui s'arrête ne dépend que de G_k (donc, librement,
   des valeurs e courantes) ; nombre de pas borné.
6. **Lecture** : la valeur e est la richesse cumulée à un temps d'arrêt de G (dernier instant révélé, ou premier
   franchissement de m/α). **Jamais** le maximum de la trajectoire, jamais un produit d'accroissements ni une richesse
   « repartie de 1 » après une reprise : W n'étant pas une surmartingale, ces lectures ne sont pas couvertes.

Ce que les conditions de la critique donneraient en plus, et que le théorème 2 ne donne pas : une richesse surmartingale
pas à pas (donc des produits d'accroissements valides). Le plan n'en a pas besoin.

### 1.3 Essai chiffré (programme à moi, hors du dépôt, aucun code du juge, aucun résultat du banc)

Monde jouet : 3 issues, 1 trait binaire, nul composite {w·S1 + (1 − w)·S2}, monde à w = 0,4, 24 cartes voisines hors de la
classe (0,0012 à 0,0313 nat par tirage), maximum de vraisemblance recalculé à chaque instant, blocs de 25, plafond 800,
budget 4 800, m = 24, α = 0,05, 20 000 générations, graines par `numpy.random.SeedSequence`. Programme
`/tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/cl/essai_validite.py`
(`01c648a0f5a65a578e95f73836666d0e55d837ee72438e15b0d37443cbfff205`), sortie `sortie-20000.txt` du même dossier
(`25a9e2e1dd9fd2c76b61b8b5f387936dd0f72f28b25a220a733b2927451aba9f`) ; bloc-notes de session, non durable, recopiée ici.
Intervalles : ± 1,96 erreur type.

| cas | part des générations avec au moins une promotion | moyenne des valeurs e |
|---|---|---|
| F, part fixe 200 | 0,0006 ± 0,0004 | 0,573 ± 0,026 |
| A, règle du texte | 0,0011 ± 0,0005 | 0,531 ± 0,028 |
| G, règle adverse : chaque bloc à la carte de plus grande valeur e courante | 0,0044 ± 0,0009 | 0,433 ± 0,038 |
| G, lue sur le rapport exact à la vraie loi (martingale) | 0,0121 ± 0,0015 | 0,998 ± 0,060 |
| A, m compté après coup (défaut voulu) | 0,0018 ± 0,0006 | 0,531 ± 0,028 |
| X1, la règle lit le bloc suivant (défaut voulu), rapport exact | 0,0145 ± 0,0017 | **1,267 ± 0,064** |
| X2, valeur e = maximum de la trajectoire (défaut voulu) | 0,0053 ± 0,0010 | **2,618 ± 0,225** |
| X3, dénominateur à mélange de poids fixés (101 poids), carte = le monde, règle G | 0,0000 | **3,377 ± 0,010** |

Lecture. (i) Je n'ai pas pu construire de contre-exemple : sous les six hypothèses, l'allocation la plus dépendante des
valeurs e que j'ai su écrire reste loin sous α, et la moyenne reste sous 1 (égale à 1 pour la martingale exacte, comme
attendu). W n'a dépassé Λ à aucun instant. (ii) La moyenne ne dépasse 1 que lorsqu'une hypothèse est rompue (X1 : n° 5 ;
X2 : n° 6). (iii) X3 : avec le dénominateur que la critique demandait, une carte **membre exact du nul** reçoit une valeur e
de moyenne 3,4 : ce n'est pas une valeur e pour chaque loi du nul, seulement pour le mélange. Cohérent avec le constat
de R-2873 sur les poids appris. (iv) Dans aucun cas, même défectueux, la part des générations avec promotion n'approche α :
voir M3.

## 2. Majeurs

**M1 — « Fausse promotion » définie par l'étiquette de construction, pas par un oracle (l. 44-46, 132, 149-150, 164-166,
184-185).** Le banc a 2 traits et 3 issues ([BANC], « Espace »). Une « fausse » dont la composante est « de même type et de
même dose, tirée indépendamment » ressemble souvent à la vraie : au premier ordre, à norme égale, elle prédit mieux que la
loi connue dès que le cosinus des deux directions dépasse 0,5, soit environ une fois sur cinq pour V1 (4 degrés de liberté)
et une fois sur trois pour V2 et V3 quand le trait conditionnant est le même. Avec quatre cartes de cette sorte par
génération, une part notable des générations contient une « fausse » partiellement vraie. L'allocation, en donnant plus de
tirages, les promouvra plus souvent ; le critère « nuisible » (borne basse de FP_A − FP_F > + 0,02) peut alors tomber sur un
artefact d'étiquette, et « gain » être refusé pour la même raison. Le texte dit « au sens de l'oracle » mais ne définit
aucun oracle.
- ancien (l. 184-185) : « 6 **fausses** : S1 portant une composante de même type et de même dose, tirée indépendamment
  (quatre) ; M à composante de signe opposé (deux) » ;
- nouveau : « 6 **fausses** : S1 portant une composante de même type et de même dose, tirée indépendamment puis retirée tant
  que son cosinus avec la composante du monde dépasse 0 (quatre) ; M à composante de signe opposé (deux). **Oracle** : avant
  le jeu, pour chaque carte non porteuse, gain attendu de log-score par tirage sur le meilleur membre du nul v8, sous la loi
  du monde, calculé sur 20 000 instances d'une graine propre `(famille, g, 2000)` ; une carte est *fausse* si ce gain est
  ≤ 0 ; sinon *partiellement vraie* : exclue de FP_X et de la couverture, comptée à part. La table de l'oracle est scellée
  avec la sortie, avant lecture. » ;
- et (l. 149) ancien : « nombre moyen, par génération, de cartes non porteuses promues (copies, fausses, nulles) » ;
  nouveau : « nombre moyen, par génération, de cartes *fausses au sens de l'oracle ci-dessus* promues, rapporté aussi par
  sorte (copies de la classe, copies par morceaux, fausses, nulles) ».

**M2 — Critères de la principale non exclusifs, et un cas sans verdict (l. 162-166, 229-231).** (a) « gain » et
« nuisible » peuvent être vrais ensemble (couverture en hausse, intervalle de FP_A − FP_F tout entier entre + 0,02 et
+ 0,05). (b) « pas de gain » et « nuisible » se recouvrent (borne haute de C_A − C_F < 0). (c) La validité a trois issues
(l. 162-163) mais la table n'en lit qu'une : « non jugeable » — de 14 à 37 générations sur 500, soit 2,8 % à 7,4 % (calcul
binomial exact, niveau 0,01) — laisse lire la suite comme si la validité tenait. (d) La prédiction Q1 (≤ 0,02, soit ≤ 10
sur 500) n'a pas le seuil de « tenue » (≤ 13 sur 500).
- ancien (l. 164-166) : « "gain" si … ; "pas de gain" si … ; "nuisible" si … ; sinon "non tranché" » ;
- nouveau : « Lus **dans cet ordre**, le premier vrai l'emporte : 1. "nuisible" si la borne haute de C_A − C_F < 0 ou la
  borne basse de FP_A − FP_F > + 0,02 ; 2. "gain" si la borne basse de C_A − C_F > 0, son estimation ≥ + 0,05 et la borne haute
  de FP_A − FP_F ≤ + 0,05 ; 3. "pas de gain" si la borne haute de C_A − C_F < + 0,02 ; 4. sinon "non tranché". » ;
- ancien (l. 229) : « une validité "non tenue" dans un bras, ou une promotion d'un membre exact de la classe » ;
- nouveau : « une validité "non tenue" dans un bras, une promotion d'un membre exact, ou une garde de M3 franchie :
  "garantie mise en défaut". Une validité "non jugeable" dans un bras : **"validité non établie"**, la principale est lue et
  rapportée sous cette réserve, aucune adoption ne peut s'en réclamer. » ; Q1 : écrire « ≤ 13 sur 500 dans chacun des bras
  (seuil de "tenue") ».

**M3 — L'épreuve de validité ne peut pas voir les défauts qu'elle garde (l. 127, 152, 162-163, 187-190, 229).** Sous le nul
global et des flux indépendants, la part des générations avec au moins une promotion reste sous α **même si la règle
anticipe ou si la valeur e est un maximum** : chaque maximum de trajectoire donne une valeur p valide (Ville), ces valeurs
sont indépendantes entre cartes, et la règle de Benjamini et Hochberg tient sous indépendance. Mon essai le montre (X1 :
0,0145 ; X2 : 0,0053 ; cas sain : 0,0011 — tous sous le seuil de 0,026). L'étage 1 ne prononcerait donc jamais « garantie
mise en défaut » pour une fuite d'instants non révélés ; seule la garde d'accès du code en protège. De plus, le monde de la
famille N est un mélange linéaire : seul le certificat exact du membre linéaire est exercé, alors que la réserve du
certificat log-linéaire n'a jamais été éprouvée à 800 tirages et 32 instants.
- ancien (l. 152) : « **Validité** (famille N) : part des générations avec au moins une promotion ; Clopper-Pearson. » ;
- nouveau : « **Validité** (famille N), quatre lectures : (1) part des générations avec au moins une promotion,
  Clopper-Pearson ; (2) **domination** : log W_t ≤ log Λ_t + 10⁻⁶ à chaque instant de chaque carte, Λ calculé par le banc
  sur la loi connue du monde — un seul dépassement : "garantie mise en défaut" ; (3) **moyenne des valeurs e finales**
  par bras et par sorte de carte, intervalle par rééchantillonnage des générations — borne basse > 1 : "garantie mise en
  défaut" ; (4) **bras G**, lu pour la validité seulement : après 50 tirages par carte, chaque bloc va à la carte de plus
  grande valeur e courante. » ;
- ancien (l. 187) : « **Famille N** (500 générations) : monde M₀ = `melange` des lois d'archive » ;
- nouveau : « **Famille N** (500 générations) : 250 à monde M₀ = `melange` des lois d'archive ; 250 à monde M₀′ = une loi
  d'archive tempérée et inclinée (`transformee`), membre de la classe log-linéaire ; lues ensemble et séparément. » ;
  ajouter au banc de mutations « la valeur e lue est le maximum de la trajectoire » et vérifier que la lecture (3) la tue.

## 3. Mineurs

- **m1 — Placebo (l. 203-205).** C'est un vrai placebo du **ciblage** : il garde les arrêts, garde le budget, et ne diffère
  de A que par qui reçoit les tirages libérés. Deux différences parasites : le tirage au hasard avec remise disperse les
  blocs (A les répartit à parts égales) ; P dépense tout le budget quand A peut en laisser. La seconde joue contre A
  (prudent). Ancien : « chaque bloc restant va à une carte **tirée au hasard** … » ; nouveau : ajouter « P consomme au
  moins autant de tirages que A ; un bras P′, à tour de rôle sur le même ensemble élargi (arrêtées bas comprises), est
  rapporté à côté : A − P′ isole l'éligibilité seule ».
- **m2 — « À tirages totaux égaux » (l. 142, 199-202).** Tenu, au sens « au plus B » : F donne exactement 4 800 ; F-arrêt et
  A au plus 4 800 ; toute carte non arrêtée reçoit au moins 200 sous A (192 blocs = 8 tours complets) ; F125 6 000, déclaré.
  Ancien (l. 142) : « B = 24 × 200 = 4 800 tirages frais au total » ; nouveau : ajouter « plafond : A, P et F-arrêt
  consomment au plus B ; la consommation réelle est rapportée ; les 100 tirages d'entraînement par carte, égaux dans tous
  les bras, ne comptent pas ».
- **m3 — Ordre des cartes (l. 199-201, 208-210).** Le dernier tour, partiel, sert les cartes selon leur indice : si les
  porteuses occupent les premiers indices, le biais est possible. Nouveau : « la position des 24 cartes est permutée par
  génération, graine `(famille, g, 1001)` ; la cellule de la génération g est g mod 8 ; le monde et l'archive ont des clés
  séparées, `(famille, g, 24)` et `(famille, g, 25)` ».
- **m4 — Vocabulaire de Q3 (l. 129).** « doses moyennes » et « doses faibles » ne sont pas définies. Nouveau : « dose haute
  = la plus grande des deux doses de chaque type (quatre cellules) ; dose basse = la plus petite ».
- **m5 — Hypothèse de travail (ii) mal appuyée (l. 49-51).** Le fait cité dit l'inverse de ce qu'on lui fait dire : à v67,
  onze cartes ont été **promues et retenues**, variantes d'un même constat (`faits-v1.md`, l. 34). Ancien : « parce que la
  plupart des cartes d'une génération ne portent rien (v67 : onze variantes d'un même constat …) » ; nouveau : « au banc, par
  construction : 18 cartes sur 24 ne portent pas la composante ; l'économie mesurée (Q7) dépend de cette composition et ne se
  transpose pas à une génération réelle ».
- **m6 — Écarts à la fiche non tous déclarés (l. 199, 206).** Blocs de 25 au lieu de 50, cartes au lieu de groupes :
  déclarés. Témoin d'effectif à 1,25 au lieu de 1,2 (fiche opus-p1-01, champ `cosmetique_si` ; relevé § 1.2) : à déclarer
  (« 240 n'est pas un multiple de 25 »).
- **m7 — Différences entre le banc et le juge de production, à lister (l. 261).** Aucune n'est un écart à la conception
  scellée, mais « aucun écart » est trop court. Nouveau : « différences de montage : plan "ordre_naturel" (production :
  "ordre_secret", indifférent pour un monde qui ne lit pas l'historique) ; m_fixe = 24 (production : nombre de cartes
  jugées) ; plan de 800 et 32 instants dont F ne lit que les 8 premiers ; le bras F se lit sur la trajectoire tronquée,
  **jamais** sur les champs `promue`, `t_promotion`, `log_richesse_max`, `log_richesse_arretee` rendus par l'évaluation à
  800 ». Ajouter cette dernière lecture au banc de mutations.
- **m8 — Essai E1 trop étroit (l. 216-217).** Les ajustements repartent à chaud d'un instant au suivant. Ancien : « pour
  t = 200 et 400 » ; nouveau : « pour chacun des 32 instants, sur 50 cartes couvrant chaque sorte ; et les instants ≤ t
  inchangés quand les issues au-delà de t sont remplacées ».
- **m9 — Portée de la garantie (l. 82-84, 101-108).** Ajouter aux réserves : « (v) quand le monde est hors de la classe
  (famille T), le théorème ne borne pas les promotions de cartes fausses : elles sont mesurées, non garanties ; (vi) la
  valeur e est toujours la richesse cumulée à un temps d'arrêt : ni maximum, ni produit d'accroissements, ni reprise à 1 ;
  le cumul d'héritage de `appliquer_multiplicite` n'est pas dans le banc ».
- **m10 — Paragraphe « Ce que cela règle » (l. 92-99).** Garder, et préciser : ancien : « ce sont des conditions
  suffisantes, pas nécessaires » ; nouveau : « elles servent une preuve facteur par facteur, que ce texte ne suit pas ; un
  dénominateur à mélange de poids fixés ne serait d'ailleurs valide que pour le mélange, pas pour chaque loi du nul
  ([PREUVE], § 8) ». La synthèse (§ 9, « condition bloquante : dénominateur fixe ») est une pièce versée : signaler à Lazar,
  avec le nœud d'adoption, que cette condition est levée par preuve contre-lue.
- **m11 — R3 et R4 (l. 136-138, 235-238).** Issues contraires écrites pour Q3 et Q4 seulement ; ajouter une ligne pour Q5
  fausse (« l'effet vient de l'arrêt, pas du ciblage »), Q6 fausse, Q7 fausse, Q8 fausse, et « hors de la zone utile ».
  L'audit « trop propre » est écrit ; l'audit « tout négatif » ne l'est pas. Nouveau : « "tout négatif" (A égal à F
  trajectoire pour trajectoire, aucune carte arrêtée bas, économie nulle, ou aucune porteuse au-delà de 200 tirages) :
  même relecture écrite du code de rejeu ».
- **m12 — R6, empreintes abrégées (l. 16-26, 263).** Vérifiées par leurs débuts : `bd253b6c`, `a9f9594e`, `606aa8b4`,
  `0ed9b4ad`, `cc452aaf`, `798f0390`, `35992811`, `eecd98fa`, `5fd7e26f`, `d19b5400`, `8cad4371`, `c7b05e39` ; les trois
  PDF et le verdict v67 en entier. Non vérifiées par moi : `0153e02d…` (liste de la copie), `80fe4f03…`. La version qui
  fera foi porte les 64 caractères pour chaque pièce qui fait foi.
- **m13 — R7 et références (l. 37-39, 110-118).** Chiffres v67 retrouvés (verdict, l. 110 : 4,248 ; 5,875 ; seuil 6,0868 ;
  log 480 = 6,174). Les trois citations de page 1 retrouvées mot pour mot dans les PDF empreintés. Ville 1939, Wasserman,
  Ramdas et Balakrishnan 2020, Wang et Ramdas 2022 : attributions correctes, à ma connaissance, sans PDF au dépôt ; écrire
  le titre de la troisième (« False discovery rate control with e-values », Journal of the Royal Statistical Society,
  série B). Hegazy, Jordan et Dieuleveut : non lue par l'auteur ni par moi, dit. Aucun chiffre de l'état de l'art n'entre
  dans un seuil.
- **m14 — Gabarit et lieu (l. 28-30, 272-279).** Sections exigées présentes ; le validateur ne refuse que la section
  « Contre-lecture » (deux empreintes entières attendues : normal pour un brouillon). Le gabarit demande le dépôt sous
  `prereg/` : la version qui fera foi y va, ou le texte dit pourquoi elle reste sous `docs/notes/`. Zone utile : la
  couverture compte « au moins une des six porteuses », dont la loi exacte du monde ; sans pilote, le risque de sortir de la
  zone est réel et accepté — le dire.

## 4. Revue par règle

| point demandé | constat |
|---|---|
| gabarit (hypothèse, prédiction et signe, métrique, seuil, plan, critères, liste d'arrêt) | complet ; M2 pour les critères |
| graines `SeedSequence` par tâche, manifeste | présentes (l. 208-210) ; m3 |
| R3, issues contraires | partielles ; m11 |
| R4 | « trop propre » écrit ; « tout négatif » à ajouter ; m11 |
| R5, gardes sur cas sain et artefact | prévues (essais et sept mutations, l. 212-216) ; deux mutations à ajouter (M3, m7) |
| tirages totaux égaux | tenu au sens « au plus » ; m2 |
| placebo | vrai placebo du ciblage ; m1 |
| écart à la conception scellée du juge | aucun dans le banc ; nœud de Lazar écrit pour l'adoption (l. 262-264) ; m7 |
| R7 | aucun chiffre non vérifié ; m13 |
| références | correctes ; m13 |

## 5. Ce que je n'ai pas fait

Je n'ai exécuté aucun code des dossiers de copie ; l'essai de préfixe de [BANC], annexe B, n'a pas été rejoué (E1 le
rejouera, m8). Je n'ai pas relu [PREUVE] au-delà du § 4, ni le code qui reste à écrire. Les fréquences de M1 sont un calcul
de géométrie au premier ordre, non une mesure sur le banc. L'essai de la section 1.3 porte sur un monde jouet : il appuie la
lecture de la preuve, il ne valide pas le juge.
