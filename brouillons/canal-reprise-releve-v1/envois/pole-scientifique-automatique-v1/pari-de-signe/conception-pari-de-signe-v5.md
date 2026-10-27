# Le pari apparié borné — conception v5, corrections locales après la contre-lecture de la v4

Lignée conv-audit (instance du 27 octobre 2026 ; **servie par Opus 5.5** pour cette version — les v1 à v4 l'étaient par
Fable 5.1), rédaction commencée après le relevé `date -u` de 20:33:22 UTC. **Remplace la v4** (`c63d8539…`, gardée, R12)
par des **corrections locales**, comme la contre-lecture de la v4 le demande (sous-agent neuf Opus 5.5,
`contre-lecture-v4/rapport-contre-lecture-pari-signe-v4.md`, `937994b5…`, script `contre-verification-pari-signe-v4.py` et
sa sortie dans le même dossier ; verdict « amender en v5 par corrections locales, pas refaire » : C-1 à C-17 fermés sur
le fond, trois réserves, un point de garantie ouvert — la clé de l'héritage —, une garantie mal dite, trois chiffres et
deux renvois faux). La v5 est un **delta** de la v4 : tout ce qu'elle ne nomme pas reste tel quel en v4 (et, par la v4,
en v3). Les décisions de Lazar du 27 octobre (N-055 : D-S1 à D-S12 selon les recommandations de la v2 ; H1a porte la
revendication de H1, H1b informe) s'appliquent. Exploratoire (R-546) ; décisif dès qu'il sert G1 (R1, R2, R13).
Contre-lecture de cette v5 : par un sous-agent neuf **Fable 5.1** (autre modèle que l'auteur de la v5), demandée à sa suite.

## Verdict (ce que change la v5)

1. **L'arrêt suit le niveau de la génération (K-3)** : partout où la v4 hérite « e-valeur arrêtée à m/α », lire
   **« arrêtée à m_g/α_g »** (m_g fiches de la famille de la génération g, α_g son niveau). Lu à la lettre, l'arrêt à m/α
   avec la règle α_g ne promeut presque rien (0,0095 à la génération 1, puis 0, contre 1,00 avec l'arrêt à m_g/α_g ;
   `contre-lecture-v4`, section 7 B).
2. **La règle entre générations, réécrite (K-4, K-5)** : une fiche **relancée par héritage** (même signature complète,
   parties disjointes) est **une seule surmartingale** — elle garde le niveau de son entrée et ne dépense pas α_g à chaque
   génération (taux de fausses promotions 0,034 à 0,041 sur 10 à 30 générations, contre 0,18 à 0,51 en relisant à neuf) ; la
   règle en ligne ne vaut que pour les **fiches nouvelles** de chaque génération, avec une **suite de dépense déclarée**
   au gel de la course : **uniforme α/G** si le nombre de générations G est scellé, sinon α_g = α·6/(π²g²). **Garantie dite
   exactement** : la règle e-BH au niveau α_g à chaque génération borne **la somme des taux de fausses découvertes**
   par α, sous dépendance quelconque entre générations ; la **probabilité d'au moins une fausse promotion** n'est bornée par
   α que sous nul complet à chaque génération — sinon, pour ce qui doit sortir du pôle, la règle **e-Bonferroni** (chaque
   fiche seule au seuil m_g/α_g) la borne (contre-exemple analytique de la contre-lecture : 1,33·α_g sous nuls partiels ;
   non atteint dans le monde S1 : 0,009 à 0,010). L'option « taux de fausses découvertes en ligne » borne encore une autre
   quantité ; LORD suppose des valeurs p indépendantes ; la voisine pour des e-valeurs sous dépendance quelconque est
   e-LOND (Xu et Ramdas, **à vérifier sur PDF, R7**, aucun chiffre cité).
3. **Clé de l'héritage écrite en entier (K-1, le point de garantie resté ouvert)** : le produit de deux e-valeurs n'est
   une e-valeur que pour l'intersection des nuls des facteurs ; la clé de l'héritage est donc **contraste et coefficients,
   pondération (v ou v′), τ (ou l'ensemble de τ déclaré), strate, liste des comparateurs (intersection-union), et seuils
   scellés** — ou, si D-S17 (a) renouvelle le calibrage, la mention « à τ, au bruit de calibrage près » dans l'énoncé de la
   fiche relancée. Toute différence de l'un de ces champs = une autre affirmation, pas d'héritage.
4. **Coûts comptés (K-4, K-11)** : à puissance 0,9 (fiche seule, m = 3), **20 points d'écart** : 45 unités sans règle en
   ligne ; 49 / 66 / 84 / 100 aux générations 1 / 3 / 10 / 30 avec 6/(π²g²) ; 63 (G = 10) et 71 (G = 30) avec l'uniforme ;
   **10 points** : 109 ; 119 / 159 / 201 / 239 ; uniforme 153 et 173 (`contre-lecture-v4`, section 7 C). Au devis de la
   couche 2 : l'organisme qui fait G générations paie ce facteur sur les fiches nouvelles, pas sur les relancées.
5. **G1 et H1 au plus près des décisions (K-6, K-14, K-16, K-19)** : lecture du critère de G1 réécrite (section 2.4 bis) ;
   règle entre modes de H1 tirée du point 4 de N-054 (mode tenu à l'écart compris, repli « restreinte au mode coût ») ;
   l'expérience de lecture de N-054 point 4 se joue **à l'évaluation**, sur la partie finale ou une partie sœur scellée ;
   D-S10 marquée **nœud de porte**.
6. **Contrôles et témoins rendus lisibles (K-7, K-9, K-15, K-13)**, **chiffres et renvois corrigés (K-8, K-10, K-11, K-12,
   K-18)**, conventions fixées (K-17 : L = nombre de niveaux ; L − 1 accroissements).
7. **Cinq décisions ajoutées** (D-S24 à D-S28 : suite de dépense, niveau des fiches relancées, sort d'une strate dont le
   témoin faux est promu, unités au-delà de m_max, désignation scellée des générations à calibrage neuf).

## 1. Corrections, section par section de la v4

### 2.1 (pondération, K-13)
Ajout : une unité dont le nombre d'épisodes m_t dépasse la borne déclarée m_max est **ramenée à un sous-échantillon scellé
de m_max épisodes** (tirage par la graine de l'engagement, avant tout calcul de parts) — jamais exclue au vu de ses issues ;
sans cette règle, v′ pourrait sortir de [−1 ; 1] et 1 + λ·v′ devenir négatif dès v′ < −1/0,9.

### 2.4 ligne 2 (bris d'égalité, K-8)
Remplacer « ce reste est la perte réelle de discrétisation » par : **en calibrage infini** (0,025 à 100 unités et 0,143 à
250 au pas de 0,5 écart-type ; écart vrai 1,6 point), le reste est la perte réelle ; **à C = 1 000, s'y ajoute le bruit du
quantile** (au pas de 0,25 : « A > B » passe de 0,032 à 0,137 à 250 unités ; « B > A » de 0,0085 à 0,072 ; écart vrai
seulement 0,45 point) (sortie T de `38efb971…`).

### 2.4 bis (nouveau) — lecture du critère de G1 (K-19)
« Le rappel **par épisode** du séquentiel blanc dépasse celui de **chaque variante noire** de la liste scellée
(intersection-union : par action, séquentielles noires, bases (i) et (iv) de N-007, juge robustifié), **aux seuils scellés
sur un calibrage de taille C tiré comme l'épreuve** (tirage stratifié depuis un même vivier gelé), à scores continus ou à
bris d'égalité scellé, par strate d'horizon prévue ; asymétrie de faux positifs certifiée < δ par la garde ; bruit de
calibrage borné par le contrôle 12 (jumeaux), dérive par le contrôle 19, sélection par le contrôle 12 étendu ; planchers et
sonde aléatoire rapportés ; par mode mesuré ; borne basse unilatérale de la suite de confiance (D-S11). » Le
préenregistrement de G1 le reprendra tel quel ou le contredira explicitement.

### 3.6 (clé de l'héritage, K-1) — voir verdict, point 3.

### 3.7 (règle entre générations, K-3, K-4, K-5) — voir verdict, points 1, 2 et 4. Le contrôle 20 est réécrit (section 2).

### 4, ligne H1 (K-6)
Règle entre modes, **tirée du point 4 de N-054** : la revendication de H1 porte sur les modes mesurés **si la borne basse
du gain blanc-sur-noir est au-dessus de zéro dans chacun des autres modes, mode tenu à l'écart compris** ; sinon, **H1 est
restreinte au mode « coût »** (le repli que N-054 prévoit). C'est une intersection-union sur les modes, mode tenu à l'écart
compris — à la différence de G1 (D-S10), qui décide sur les modes mesurés et garde le mode tenu à l'écart hors décision.

### 4, ligne G1 (K-14, D-S20)
L'expérience de lecture de N-054 point 4 (moniteurs gelés sur le mode « coût », lus sur « contrôles » et sur le mode tenu
à l'écart) se joue **à l'évaluation**, sur la partie d'épreuve finale ou une **partie sœur scellée**, jamais sur une partie
lue avant G1 (D-S19 : exclusion du mode tenu à l'écart). Famille qui décide G1 entre bras génériques et spécialisés
(D-S20) : **les génériques** recommandés (l'anti-circularité de N-054 point 3, étendue à la conception, pointe vers eux ;
c'est une lecture, pas un texte : nœud de porte), les spécialisés rapportés.

### 5, contrôles (K-7, K-9, K-15)
- **18** : les deux lectures **au C dimensionné**. Première : « la cellule discrète bat la continue » ≤ α. Seconde, avec
  critère : le taux réel de faux positifs de la cellule discrète vaut τ, et l'écart vrai de rappel vaut la perte calculée
  **dans le monde des jumeaux à la masse d'ex æquo mesurée sur la base réelle**, chacun à son intervalle près ; la
  promotion de « A > B » y est rapportée, pas jugée. « 1,6 point au pas de 0,5 » est propre au monde binormal.
- **20** : artefact exigé **là où il est attendu** : taux cumulé sans règle en ligne **croissant avec G et > α dès G = 10**
  (0,111 à 100 unités, 0,197 à 250 ; à 3 générations, 0,033 et 0,067 ne sont pas « ≫ α ») ; avec la règle (fiches
  nouvelles) et l'héritage (fiches relancées) : ≤ α ; quantité lue dite (somme des taux de fausses découvertes, ou
  probabilité d'au moins une fausse promotion sous nul complet).
- **Témoin faux asymétrique promu (K-15)** : les promotions **déjà faites** dans la strate par lecture continue sont
  **suspendues** (ni retirées ni confirmées) ; la « panne » est une présomption, confirmée ou levée par **un nouveau tirage**
  du témoin (avec remise, graine neuve) ; promotion attendue d'un témoin seul par hasard : de l'ordre de α/m au plus.
  **Chiffre corrigé (K-10)** : promotion attendue avec remise à 1 000 unités : **0,029** (banque 90/10) et **0,028**
  (80/20), non 0,022 ; 0 / 0,0115 / 0,018 à 30 / 100 / 250 unités.

### 6 (K-18, K-17)
- « Un banc de 300 épisodes sur 10 unités ne peut rien promouvoir à moins d'un écart d'au moins 0,6 sur chaque unité »
  devient : **à un écart commun d'au moins 0,551** (seuil exact), un profil hétérogène pouvant promouvoir aussi (9 unités à
  v = 1 et 1 à 0 : richesse 101) ; **à 6 unités ou moins, rien n'est promouvable** (17,6 à v = 1) ; 7 unités suffisent à
  v ≥ 0,858 (31,1 à v = 1), 8 unités à v ≥ 0,725.
- Convention : **L = nombre de niveaux** (horizons ou N), L − 1 accroissements adjacents ; « L − 1 fois les paires d'un
  accroissement ».

### 6 bis (K-11, K-12)
- Student sous S1 et S2 de 60 à 250 unités : **0,06 à 0,13** (S1 à 60 : 0,133 dans la batterie, 0,137 exact).
- **Renvois intervertis** : les miroirs de S1 et S2 (Student exact 0,008 à 0,043) sont dans `654457a8…` (section A) ; les
  chiffres du nul 98/2 (0,55 / 0,30 / 0,13 ; pari 0,0095 au plus) sont dans `082794ea…`.

## 2. Décisions (v4, plus D-S24 à D-S28 ; D-S10 et D-S16 réécrites)

| décision | recommandation (confiance) |
|---|---|
| D-S10 (**nœud de porte**) | intersection-union sur les modes mesurés, mode tenu à l'écart hors décision, fixée au préenregistrement de G1 (0,55) |
| D-S16 (réécrite) | héritage pour les fiches relancées (une seule surmartingale) ; règle en ligne pour les fiches nouvelles ; garantie dite « somme des taux de fausses découvertes ≤ α » ; e-Bonferroni pour ce qui sort du pôle (0,5 tant que ce n'est pas simulé sur les générations réelles) |
| D-S17 (précisée, K-2) | (b) promotions de l'organisme « aux seuils scellés » ; (a) calibrage neuf seulement pour des générations **désignées et scellées avant leur lecture**, ou sortie par confirmation sur une partie et un calibrage neufs (0,6) |
| D-S18 (précisée, K-1) | clé de l'héritage en entier : contraste et coefficients, pondération, τ, strate, comparateurs, seuils (0,85) |
| **D-S24 suite de dépense** | uniforme α/G si G est scellé au gel de la course ; sinon 6/(π²g²) (0,7) |
| **D-S25 niveau des fiches relancées** | elles gardent le niveau de leur entrée (une seule surmartingale), ne dépensent pas α_g (0,8) |
| **D-S26 strate dont le témoin faux est promu** | promotions de la strate suspendues jusqu'à un nouveau tirage du témoin (0,75) |
| **D-S27 unité au-delà de m_max** | sous-échantillon scellé de m_max épisodes (0,8) |
| **D-S28 générations à calibrage neuf** | désignées et scellées avant leur lecture (0,8) |

Défauts sous 48 heures : les recommandations, sauf D-S10, D-S11 et D-S20 (nœuds de porte, au préenregistrement de G1).
**Nœuds pour Lazar, inchangés** : comparateurs de G1 ; N-054 point 4 (présentés au format de décision :
`noeuds-pour-lazar-v1.md`, `d9a6ff1b…`) ; strate « diffus » et instant du dommage à coder dans la banque de la couche 2.

## 3. Ce que la v5 laisse ouvert (dit)

La règle en ligne n'est simulée que sur le monde S1 (pas sur les générations réelles du pôle) ; la clé complète de
l'héritage n'est pas encore codée dans v7 (signature actuelle : moniteur, nombre d'issues, dimension, loi ; à étendre
quand le pari apparié sera codé) ; le contrôle 18 au C dimensionné n'est pas simulé ; e-LOND et Maurer et Pontil restent à
vérifier sur PDF (R7).
