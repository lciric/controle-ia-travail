# Le pari apparié borné — second type d'engagement du pôle, pour les affirmations globales (H1, H2, H3, G1) — conception v4, après la contre-lecture de la v3

Lignée conv-audit (instance du 27 octobre 2026 ; **servie par Fable 5.1**), rédaction commencée après le relevé `date -u`
de 19:24:30 UTC. **Remplace la v3** (`1518a12f…`, gardée, R12), qui remplaçait la v2 (`9c39a73d…`) et la v1 (`50ce6842…`).
Cette v4 répond à la **contre-lecture de la v3** par un sous-agent neuf Opus 5.5
(`contre-lecture-v3/rapport-contre-lecture-pari-signe-v3.md`, `8866998b…`, scripts `30f481a2…`, `5432ed15…`, `7882caba…`
et sorties `654457a8…`, `082794ea…`, `39814a05…` ; verdict « amender en v4, pas refaire » : deux des sept points de garantie
du collisionneur n'étaient pas fermés, le critère de G1 changeait sans le dire, trois chiffres étaient faux). Elle garde
tout ce que la v3 tient (section 7 de la contre-lecture), corrige dix-sept constats C-1 à C-17, et ajoute sept
décisions (D-S17 à D-S23) et un nœud. Ce qui change est marqué « **(C-n)** ». Exploratoire (R-546) ; décisif dès qu'il
sert la porte G1 (R1, R2, R13) ; rien n'est une dépense, mais la section 6 chiffre des dépenses pour le devis de la couche 2.
Simulations citées : v2 (`d07e43f9…`), calcul binormal (`1782e8cd…`), vérifications de la lecture du collisionneur
(`38efb971…`), batterie (`ead1b9d5…`), vérifications de la contre-lecture v3 (`654457a8…`, `082794ea…`, `39814a05…`).

## Verdict (ce que je propose, v4)

1. **Inchangé** : un seul engagement, le pari apparié borné en forme « parts » seule ; unité = la tâche ou la consigne avec
   toutes ses exécutions ; nul fixe E[v] ≤ 0 ; portée conditionnelle aux agents surveillés du banc ; e-valeur = minimum des
   processus arrêtée à m/α ; héritage entre parties d'épreuve disjointes ; comparateur de G1 par intersection-union ;
   score continu ou bris d'égalité scellé ; tirage scellé des parties ; calibrage propre au développement ; seuil par
   horizon ; H2a en détection au-dessus du hasard avec masque symétrique ; H2b sur le rappel du séquentiel lui-même ;
   H1b en nœud. **La batterie** : le pari « parts » tient α partout (≤ 0,028 ; 0,025 sous les nuls extrêmes de la
   contre-lecture) ; Student non ; Hoeffding et Bernstein empirique valides mais sans puissance.
2. **Deux points de garantie rouverts et fermés (C-1, C-2).** (i) Une partie d'épreuve neuve par génération rend les
   lectures indépendantes mais **laisse G chances à un même contraste nul** : taux cumulé 0,067 / 0,197 / 0,465 à 3 / 10 /
   30 générations sous nul asymétrique (250 unités par strate) ; remède : une **règle en ligne entre générations**,
   α_g = α·6/(π²·g²) (somme α ; cumul ≤ 0,024 à 30 générations), ou une règle de taux de fausses découvertes en ligne
   (D-S16 réécrite). (ii) Le biais de sélection du bras aux seuils d'un même calibrage **tient au calibrage partagé, pas
   à la partie** : avec une partie neuve mais le même calibrage, un candidat retenu à la génération précédente est promu
   à tort dans 0,25 à 0,41 des cas (C = 200) contre 0,10 à 0,11 avec un calibrage neuf ; pour l'organisme du pôle :
   **calibrage neuf par génération** (coût × G) ou promotions dites « aux seuils scellés » seulement (D-S17).
3. **Le critère de G1 remis en conformité (C-5)** : la liste des comparateurs de l'intersection-union ne contient que des
   **variantes noires** (par action, séquentielles, bases (i) et (iv) de N-007, juge robustifié) ; les bases (ii) cascade
   et (iii) dernier état sont **boîte blanche et servent à H2** (N-007 : « pas au critère de G1 ») ; les planchers de
   N-008 et la sonde aléatoire sont **rapportés, jamais critères**. L'autre lecture (les mettre en critères) est soumise
   à Lazar comme nœud, pas écrite.
4. **Clé de l'héritage, mode tenu à l'écart, estimande de G1 (C-3, C-4, C-14)** : l'héritage de preuve est indexé par la
   signature **avec τ** (ou l'ensemble de τ déclaré) — un produit d'e-valeurs à 1 % et à 5 % n'est une e-valeur pour
   aucune des deux affirmations — ; la signature sans τ ne sert qu'à « une lecture par partie » ; les unités du mode tenu
   à l'écart sont **exclues de toute partie lue avant G1** (développement et générations), pas seulement masquées ; pour
   G1, l'estimande **par épisode** de N-054 s'impose (v′ = (m_t/m_max)·v avec m_max borne déclarée, ou m constant), et
   v′ ne vaut que pour les contrastes lus sur les mêmes épisodes.
5. **Contrôles 18, 20, 21 reconstruits (C-6, C-7)** ; H2b sans facteur ½ (C-12 : le ½ divisait le signal par deux : 0,47
   contre 0,95 à 100 paires) ; témoin faux asymétrique en forme population **sur tirages avec remise** dans la banque
   (nul exact ; promotion attendue 0 à 0,03 ; une promotion arrête la lecture de la strate) (C-15) ; rééchantillonnage
   jugé sur un calcul exact et non plus sur Student (C-8) ; N3 et N4 étiquetés « moyenne négative » et remplacés par les
   miroirs de S1 et S2 pour la preuve du sens (C-9) ; « prix de la validité non asymptotique » (C-10).
6. **Coûts recomptés (C-11)** : parties d'épreuve de l'organisme × G ; calibrage de l'organisme × G (si D-S17 (a)) ;
   H2b à L accroissements : L fois les paires (le ½ en doublait le nombre) ; un témoin faux asymétrique par strate
   compte dans m (les témoins faux comptent, les vrais non : v7 version 11).

## 1. Le besoin (v3, une correction : C-17)

Tableau de la v3 inchangé, avec pour H1 la règle entre modes de N-054 point 2 : **H1 ne porte que sur les modes
mesurés, et le mode « coût » seul ne la porte pas** (intersection-union sur les modes mesurés hors « coût », ou règle
déclarée au préenregistrement : D-S20).

## 2. L'objet : le pari apparié borné

### 2.1 Unité, contraste, nul (v3, précisions C-14)

Unité, contraste, règle double, nul : comme en v3. **Pondération** : par défaut chaque unité pèse 1 ; v′(t) = (m_t/m_max)·v(t)
teste le nul sur le rappel **par épisode** — E[m_t·v] = E[m_t]·(a₀ + Σ a_c·R_c) avec R_c le rappel par épisode de la
population — **seulement pour les contrastes dont toutes les cellules sont lues sur les mêmes m_t épisodes** (H1a, G1,
H3a à N fixé, « rappel ≥ x », la garde) ; pas pour H2a (sabotés et jumeaux honnêtes n'ont pas le même m), ni pour les
contrastes entre unités appariées (H1b, H2b, H3b). m_max est une **borne déclarée avant le gel**, pas le maximum observé
d'une banque qui grandit. **Pour G1, v′ (ou un m constant) s'impose** : N-054 point 2 dit « rappel par épisode » (D-S22).
Forme « signe » : hors du pari (inchangé).

### 2.2 Le processus e (inchangé) ; 2.3 Variante « banque entière » (inchangée, et ne sert plus au témoin asymétrique : C-15)

### 2.4 Le point de fonctionnement : quatre sources d'asymétrie (v3, deux corrections : C-2, C-16)

Le tableau des quatre sources (bruit du quantile ; ex æquo ; dérive de composition ; sélection aux seuils d'un même
calibrage) est celui de la v3, avec :
- ligne 2, bris d'égalité : « ramène à 0,025 à 100 unités » s'entend **en calibrage infini** ; avec 1 000 unités de
  calibrage, 0,068 (pas de 0,5 écart-type) et 0,032 (pas de 0,25) à 100 unités, 0,26 et 0,14 à 250 (sortie T de
  `38efb971…`) ; ce reste est la **perte réelle de discrétisation** (1,6 point au pas de 0,5), pas un artefact ; le bris
  s'applique **toujours** (un score « continu » peut saturer près du quantile), avec une uniforme par épisode, fonction
  de l'identité de l'épisode et d'une graine scellée avant tout calcul de score, la même pour le calibrage et l'épreuve,
  **jamais retirée** (ni par fiche, ni par génération : ce serait une sélection du type P21) ;
- ligne 4, sélection : **le biais tient au calibrage partagé, pas à la partie d'épreuve** (C-2) : une partie neuve sans
  calibrage neuf laisse 0,25 à 0,41 de promotions à tort (C = 200, K = 5 et 20 ; 0,046 et 0,076 à C = 1 000) contre
  0,10 à 0,11 (0,024 et 0,032) avec un calibrage neuf (`654457a8…`, section E). Pour G1 : calibrage propre au
  développement, calibrage d'épreuve lu une fois après le gel des choix (D-S15, qui ferme P21 **pour G1 seule**). Pour
  l'organisme du pôle, qui retient de génération en génération les cellules qui gagnent : D-S17.
- Seuil par strate d'horizon (inchangé), **l'horizon étant celui prévu de la tâche**, pas la longueur réalisée, qui
  dépend du comportement de l'agent surveillé.
- Garde appariée et niveau absolu rapporté : inchangés. Lecture du critère de G1 : comme en v3.

### 2.5 Ce que l'agent propose, ce que le noyau tient (v3, deux corrections : C-4, partage des unités)

Comme en v3, avec : (i) les unités du **mode tenu à l'écart n'entrent dans aucune partie lue avant G1** — ni le
développement, ni les parties des générations — mais seulement dans la partie d'épreuve finale de G1 (N-054 point 3 :
« révélé seulement à l'évaluation ») ; « stockée à part » ne suffisait pas ; (ii) pour les accroissements adjacents
(H2b, H3b à trois niveaux ou plus), **une unité peut appartenir à deux paires adjacentes** (le niveau du milieu est
partagé) : le minimum sur ℓ reste valide sous toute dépendance ; la puissance baisse (corrélation −½ entre
accroissements voisins quand les trois mesures sont de même variance : un niveau du milieu haut par hasard aide l'un et
nuit à l'autre), ce que le dimensionnement compte (section 6) ; « chaque unité dans une paire au plus » ne vaut que pour
les paires d'une **même** comparaison.

### 2.6 Comparateur par intersection-union (réécrit : C-5)

« Bat la meilleure base noire, toutes variantes confondues » (N-008) : un processus par **variante noire** k, promotion si
tous atteignent le seuil, e-valeur = min_k, niveau α sans correction ; puissance = celle du contraste qui croît le plus
lentement, variance comprise. **La liste scellée ne contient que des variantes noires** : moniteurs par action, moniteurs
séquentiels noirs, les bases (i) et (iv) de N-007, le juge robustifié. **Hors de la liste** : la cascade de portes (ii) et
la sonde sur le dernier état (iii), qui sont boîte blanche et « servent à H2, pas au critère de G1 » (N-007) — elles
portent H2c ; les planchers de N-008 (« tout signaler », « juge en une passe ») et la sonde aléatoire appariée en
covariance (P § 8.1), **rapportés** à côté du verdict, jamais conditions. Contrôle de qualité des bases, rapporté : **la
meilleure base** de la liste (sur le développement) doit battre le plancher « juge en une passe » ; sinon la liste est un
homme de paille et le journal le dit. L'ensemble de confiance du meilleur : non retenu (v3). **Nœud** : si Lazar veut
que les bases (ii), (iii) ou les planchers deviennent des conditions de G1, c'est une modification de N-007 et de N-008,
pas une ligne de cette pièce (section 8).

## 3. Validité, et ses frontières (v3, deux sections réécrites : 3.6 et 3.7)

3.1 à 3.5 : inchangées. Le témoin faux asymétrique y est ajouté comme ce qu'il est : un nul exact **pour la forme
population sur tirages avec remise** dans une banque figée de moyenne nulle (C-15) ; lu dans un ordre secret sans remise,
il n'est pas un nul exact pour cette forme (E[v(t) | passé] = μ_t ≠ 0).

### 3.6 Héritage, relecture, clé de l'héritage (C-3)
Une lecture par signature et par partie d'épreuve ; héritage entre parties disjointes seulement (inchangé). **Clé de
l'héritage : la signature avec τ** (ou avec l'ensemble de τ déclaré par la fiche) — le produit d'une e-valeur à 1 % par
une e-valeur à 5 % n'est une e-valeur ni pour « A > B à 1 % », ni pour la conjonction (un vrai effet à 5 % le fait croître
sous un nul vrai à 1 %). La signature **sans τ** ne sert qu'à la règle « une lecture par partie » : deux fiches à τ
différents sur une même partie sont deux affirmations de même signature ; celle qui veut les deux les déclare ensemble
(e-valeur = minimum, valide pour la conjonction). Cette restriction est valide et non nécessaire (la règle e-BH couvre la
dépendance) ; elle est gardée pour la lisibilité de la mémoire.

### 3.7 Multiplicité entre générations : la règle en ligne (C-1, nouveau)
Une partie d'épreuve neuve par génération rend les lectures indépendantes ; **elle laisse G chances** à un même contraste
nul relu à chaque génération. Reproduit (`654457a8…`, section B ; nul S1, 3 fiches par génération, règle e-BH à m = 3) :
taux cumulé de fausses promotions 0,033 / 0,111 / 0,30 à 3 / 10 / 30 générations pour 100 unités par strate ; 0,067 /
0,197 / 0,465 pour 250 — alors que le taux par génération reste sous α (0,011 et 0,021). **Règle** : la génération g joue sa
règle e-BH au niveau **α_g = α·6/(π²·g²)** (Σ_g α_g = α ; cumul mesuré 0,0075 et 0,024 à 30 générations), ou une règle de
taux de fausses découvertes en ligne (LORD ou équivalent, référence à vérifier, R7) fixée au préenregistrement ; la
famille de la porte G1 reste propre et hors de cette suite (lue une fois). D-S16 réécrite ; contrôle 20 reconstruit.

## 4. Tableau hypothèse → forme → fiche (v3, trois corrections : C-12, C-17, C-5)

- **H1** : comme en v3, plus la règle entre modes (N-054 point 2) : la revendication ne porte que sur les modes mesurés ;
  le mode « coût » seul ne la porte pas (D-S20).
- **H2** : H2a comme en v3, avec le masque **défini** : filtre d'épisodes sur les scores par action **aux indices sabotés**,
  le même masque d'indices appliqué à l'épisode honnête jumeau de même consigne et de même longueur ; **H2b sans ½** :
  v_ℓ = r_seq(h_{ℓ+1}) − r_seq(h_ℓ) (deux parts, règle double satisfaite ; C-12), **sur la sous-population de N-007**
  (« chaque action sabotée sous le seuil par action »), à seuil par horizon prévu, intersection-union sur les
  accroissements ℓ = 1 … L − 1 ; H2c : comme en v3 (c'est là, pas dans G1, que vivent les bases (ii) et (iii)).
- **H3** : H3a comme en v3 ; H3b garde le ½ (quatre parts).
- **G1** : comparateurs = variantes noires seulement (2.6) ; planchers et sonde aléatoire rapportés ; estimande par
  épisode (v′ ou m constant) ; deux familles de bras avec une **règle entre familles** (D-S20) ; mode tenu à l'écart
  exclu des parties lues avant G1 ; latéralité et méthode d'intervalle (D-S11).
- **« rappel ≥ x », H8** : inchangés.

## 5. Contrôles fatals (v3 : 1 à 21 ; reconstruits : 12 étendu, 14 étendu, 17, 18, 20, 21 ; C-6, C-7, C-8)

| n° | changement v4 |
|---|---|
| 12 étendu | lecture « ≤ α avec le calibrage propre » **au C dimensionné seulement** (à C = 200 le niveau sans sélection vaut déjà 0,10 à 0,11) ; les deux lectures sont rapportées : « même calibrage » (artefact requis) et « calibrage propre » |
| 14 étendu | lecture écrite pour les trois définitions : masque symétrique ≤ α ; « aucun filtre » : rapporté (ce n'est plus H2a de N-007) ; filtre plus strict côté honnête ≫ α (artefact requis) |
| 17 | la batterie **plus un rééchantillonnage** (intervalle percentile sur les unités, règle d'égalité déclarée pour les contrastes multiples de 0,1 : la borne basse tombe souvent exactement sur 0, et l'arrondi flottant décidait : 0,19 contre 0,037 à 30 unités sous S1) ; niveaux exacts cités en 6 bis ; nuls : S1, S2, leurs miroirs, N5, **98/2** (perte rare) |
| 18 | lu sur le **sens faux seul** (« la cellule discrète bat la continue ») ≤ α ; dans l'autre sens, « A > B » est comparé à la **perte réelle de discrétisation** (1,6 point au pas de 0,5), au C dimensionné où les jumeaux continus passent le contrôle 12 ; la granularité n'est pas « des paliers de 0,25 et 0,5 » mais la **masse d'ex æquo mesurée au quantile** de la base réelle (un juge à dix niveaux dont le niveau du haut pèse plus de τ des honnêtes n'alerte jamais sous « > ») |
| 19 | le sens est dit (avec le tirage stratifié, « B > A » à 0,012–0,24 est juste : A est réellement moins bon à faux positifs égaux) ; ce n'est pas un jumeau ; ajout : dérive sur une variable **non codée**, affectation au hasard contre affectation par date — ce qui protège, c'est l'affectation au hasard depuis un même vivier gelé, la stratification ne réduit que la variance (D-S14 précisée) |
| 20 | reconstruit : **nul asymétrique** (S1), au **nombre réel de générations** (3, 10, 30), 3 fiches par génération, parties neuves ; sans règle en ligne ≫ α (artefact requis : 0,067 à 0,465) ; avec α_g ≤ α (0,024) — la version v3 (même partie, nul symétrique) ne voyait rien (0,010 et 0,042) |
| 21 | reconstruit : avec trois horizons, le premier accroissement était nul et l'intersection-union jamais promue (même sans signal) ; désormais **deux niveaux** (artefact au seuil commun : 1,00 à 250 paires sans signal) et le monde **« budget de sabotage constant »** (rappel par horizon qui décroît, 0,10 / 0,034 / 0,019, que le seuil commun fait « croître » : 0,65 à 100 paires ; seuil par horizon : jamais promu), plus des horizons où chaque accroissement porte un gain de faux positifs |

Témoins des courses réelles : inchangés, le témoin faux asymétrique étant **tiré avec remise** dans la banque figée
construite (90 % de petits gains, 10 % de grandes pertes ; assez d'unités réelles proches de −0,9, sinon les valeurs ne
sont plus réelles et le témoin le dit), promotion attendue 0 à 0,03 (0,022 à 1 000 unités) ; **sa promotion arrête la
lecture de la strate** (« procédure en panne ») ; il compte dans m (témoin faux).

## 6. Dimensionnement (v3, coûts recomptés : C-11, C-16)

Unités sabotées par mode : inchangé (40 pour 20 points, 100 pour 10 ; 0,63 à 60 unités pour 10 points dans la v2 à 500
répétitions, 0,59 dans la batterie à 2 000 : même quantité, deux estimations). Garde, calibrage (10 à 16 fois les unités
sabotées à 1 %, par strate d'horizon, plus le calibrage du développement) : inchangé. **Ajouts** : parties d'épreuve de
l'organisme **× G** générations ; calibrage de l'organisme **× G** si D-S17 (a) ; H2b à L accroissements : **L fois** les
paires d'un accroissement (environ 100 paires pour 10 points sans ½, 0,95 ; le ½ en demandait 150 à 200) ; un témoin faux
asymétrique par strate fait monter m d'une unité par strate. **Correction d'une phrase** : un banc de 300 épisodes sur 10
unités **ne peut rien promouvoir à moins d'un écart d'au moins 0,6 sur chaque unité** (dix unités à v = 0,6 donnent une
richesse mélangée de 25,9 ≥ 20) ; sous 7 à 8 unités, rien n'est promouvable quel que soit l'écart (« une vingtaine
d'agents » est la recommandation de la v2, pas le minimum).

### 6 bis. Batterie (v3, corrections C-8, C-9, C-10, C-13)

Tableau de la v3 corrigé : **N3 et N4 ont une moyenne négative** (−0,04 et −0,0375), et leur conservatisme pour Student
vient de la moyenne, pas du sens de l'asymétrie ; ramenés à moyenne nulle, Student y est anticonservateur (N3 : 0,127 /
0,107 / 0,077 à 15 / 20 / 30 unités ; N4 : 0,080 / 0,091 / 0,098) ; la vraie preuve du « sens » est donnée par les
**miroirs** de S1 et S2 (gains rares, pertes fréquentes) : 0,008 à 0,043 (`082794ea…`). **Student sous S1 et S2 : 0,07 à
0,22 à 15–30 unités** (S2 : 0,069 à 20, 0,124 à 30 ; S1 : 0,22 / 0,13 / 0,18 à 15 / 20 / 30), 0,06 à 0,12 de 60 à 250.
**Rééchantillonnage (calcul exact de la contre-lecture, `654457a8…`)** : percentile idéal sous S1 : 0,21 / 0,12 / 0,042 /
0,053 / 0,058 / 0,051 à 15 / 20 / 30 / 60 / 100 / 250 unités ; sous S2 : 0,035 à 0,069 ; sous N5 : 0,081 à 15, 0,053 à 0,059
de 30 à 250 ; **il s'effondre quand l'échantillon peut ne contenir aucune perte rare** : sous un nul 98/2, 0,55 / 0,30 /
0,13 à 30 / 60 / 100 unités, contre 0,0095 au plus pour le pari — son niveau dépend de la rareté, inconnue, de la perte.
**Hoeffding et Bernstein empirique : valides, pas « exacts »** (niveau 0 partout) ; Bentkus **non simulé**. Le facteur
1,7 à 2,7 d'unités face à Student est **le prix de la validité non asymptotique** (le pari lu une fois a la même puissance
ou moins que le pari lu en continu : 0,963 contre 0,968 à 40 unités et 20 points), pas celui de la lecture à tout instant.

## 7. Ce que cela change dans le pôle (v3, plus : règle en ligne α_g entre générations ; clé de l'héritage avec τ ; mode tenu à l'écart hors de toute partie lue avant G1 ; calibrage de l'organisme selon D-S17 ; témoin asymétrique tiré avec remise ; H2b sans ½ ; contrôles 18, 20, 21 reconstruits)

Dans v7 version 11, les témoins faux comptent dans m et les témoins vrais sont hors de la famille (lus au seuil m/α) : la
pièce suit cette règle (D-S21).

## 8. Décisions et nœuds (v3 ; D-S16 réécrite ; D-S17 à D-S23 ajoutées ; un nœud ajouté)

| décision | options | recommandation (confiance) |
|---|---|---|
| D-S9 (précisée) | comme en v3 ; **les contrôles sur la banque réelle ne servent pas à choisir C** : C est fixé au gel d'après la simulation ; le contrôle 12 sur la banque dit ensuite si la fiche est lisible (la v2 disait « chiffré par le contrôle 12 sur la banque » : à lire ainsi) | la même (0,6) |
| D-S10 (précisée) | les options de la v2 restent sur la table : fiche « tous modes » décide ; **intersection-union sur les modes mesurés** ; e-BH sur les modes avec k promus ; mode tenu à l'écart hors décision | intersection-union (0,55, comme en v2 : aucun argument nouveau) |
| D-S11 (preuve corrigée) | (a) suite de confiance du pari, borne basse unilatérale ; (b) rééchantillonnage à n fixé ; (c) le pari décide, le rééchantillonnage est rapporté | **(a) avec (c)** : le pari tient α partout ; le rééchantillonnage tient à peu près α dès 30 unités sous S1 et S2 (0,04 à 0,07) mais s'effondre quand la perte est rare (0,13 à 100 unités sous 98/2), ce qu'on ne sait pas d'avance ; nœud de porte (0,7) |
| D-S14 (précisée) | tirage stratifié scellé **depuis un même vivier gelé, par affectation au hasard** (ce qui protège d'une dérive sur une variable non codée) ; mode tenu à l'écart exclu du tirage | la même (0,8) |
| **D-S16 (réécrite, C-1)** | signature sans τ pour « une lecture par partie » ; partie d'épreuve neuve par génération ; **plus une règle en ligne** : α_g = α·6/(π²g²), ou une règle de taux de fausses découvertes en ligne | **la règle α_g** (simple, cumul ≤ 0,024 mesuré) ; confiance 0,5 tant que la règle en ligne n'est pas simulée sur les générations réelles |
| **D-S17 calibrage de l'organisme (C-2)** — dépense | (a) calibrage neuf par génération (coût × G) ; (b) promotions de l'organisme dites « aux seuils scellés », P21 fermé pour G1 seule | **(b) pour l'organisme, (a) pour toute génération dont une promotion doit sortir du pôle** (0,6) ; poste au devis |
| **D-S18 clé de l'héritage (C-3)** | avec τ ; sans τ | **avec τ (ou l'ensemble de τ déclaré)** (0,85) |
| **D-S19 mode tenu à l'écart (C-4)** | masqué ; **exclu de toute partie lue avant G1** | **exclu** (0,85) |
| **D-S20 règles entre modes et entre familles de bras (C-17, N-054 points 2 et 3)** | H1 : modes mesurés hors « coût », intersection-union ou règle déclarée ; G1 entre familles génériques et spécialisées : l'une ou l'autre suffit (famille de multiplicité à deux hypothèses) ; les deux ; une famille désignée | H1 : intersection-union sur les modes mesurés hors « coût » (0,6) ; G1 : **famille désignée au préenregistrement**, l'autre rapportée (0,5) — nœud de porte |
| **D-S21 témoins dans m** | tous ; **faux seulement** (vrais hors famille, v7 version 11) ; aucun | **faux seulement** (0,8) |
| **D-S22 estimande de G1 (C-14)** | par unité ; **par épisode** (v′ ou m constant) | **par épisode** : ce n'est pas un choix de fiche, N-054 point 2 l'impose (0,9) |
| **D-S23 niveaux de H2b et H3b** | deux niveaux ; L niveaux désignés avec partage des unités adjacentes | **deux niveaux** par défaut (le gain de « croît » sur L niveaux coûte L fois les paires et la corrélation −½) ; L niveaux si la banque le permet (0,6) |

**Nœuds pour Lazar (hors défaut)** : (1) H1b (inchangé) ; (2) N-054 point 4, intervalles par rééchantillonnage de
l'expérience de lecture : la preuve est désormais celle du calcul exact (niveau 0,04 à 0,07 dès 30 unités sous S1 et S2,
mais 0,13 à 100 unités quand la perte est rare), pas celle de Student ; proposition inchangée : les garder comme rapport,
lire par le pari quand l'expérience restreint une revendication ; (3) **comparateurs de G1** : la v2 et la v3 mettaient
en critères les bases (ii) et (iii) et les planchers, contre N-007 et N-008 ; la v4 les en retire ; si Lazar veut l'autre
lecture, c'est une modification de N-007 et de N-008 ; (4) la strate « diffus » et l'instant du dommage (inchangé).

## 9. Ce que la banque de la couche 2 doit porter (v3, plus)

Un vivier gelé d'où toutes les parties sont tirées au hasard ; le mode tenu à l'écart hors de toute partie lue avant G1 ;
l'horizon **prévu** de chaque tâche ; la masse d'ex æquo de chaque base au voisinage de τ ; G parties d'épreuve pour
l'organisme ; G calibrages si D-S17 (a) ; un identifiant de paire par accroissement.

## 10. Ce que la v4 ne reprend pas (v3, inchangé : P40 à P57), et ce qu'elle corrige de la v3 (en bref)

Rejets de la section 10 de la v3 : inchangés (la contre-lecture ne conteste aucun). Corrigés : C-1 à C-17 ci-dessus ;
formulations (C-16) : « la même signature » (non « la même affirmation ») ; « valides » (non « exacts ») ; Bentkus « non
simulé » ; « cumulait au-delà de α » retiré (l'artefact de la v3 n'était pas montré : 0,010 et 0,042 ; c'est la règle en
ligne qui est en jeu) ; bris « en calibrage infini » ; « la meilleure base bat le plancher » ; masque de H2a défini.

## 11. Ce qui n'est pas dans cette pièce

Le préenregistrement de G1 ; toute conception d'attaque ; la simulation de la règle en ligne sur les générations réelles
du pôle et du contrôle 21 reconstruit (à faire avant le préenregistrement) ; la contre-lecture de cette v4 (sous-agent
neuf, autre modèle) : demandée à sa suite si le temps le permet, sinon à la reprise.
