# Le pari apparié borné — conception v6, corrections locales après la contre-lecture de la v5

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5), rédaction commencée après le relevé `date -u` de
21:03:33 UTC. **Remplace la v5** (`95af46e4…`, gardée, R12) par des **corrections locales**, comme la contre-lecture de
la v5 le demande (sous-agent neuf Fable 5.1, autre modèle que l'auteur ; `contre-lecture-v5/rapport-contre-lecture-pari-signe-v5.md`,
`4e8e3270…`, script `contre-verification-pari-signe-v5.py` `ece834a8…` et sa sortie `285e222f…` dans le même dossier ;
verdict « amender en v6 par une règle écrite (D-S25 bis), pas refaire » : K-2 à K-19 fermés sur le fond, K-3 trop large,
K-5 à moitié, K-1 sauf deux champs ; deux points touchent la garantie ; trois lectures trompeuses ; deux détails de
chiffres et un pointeur faux). **Sortie du script reproduite** ici, identique hors durée (scratchpad de la session,
`34cf6eb0…`, non versée). La v6 est un **delta** de la v5 : tout ce qu'elle ne nomme pas reste tel quel en v5 (et, par
elle, en v4 et v3). Exploratoire (R-546) ; décisif dès qu'il sert G1 (R1, R2, R13). Contre-lecture de cette v6 : par un
sous-agent neuf Fable 5.1, demandée à sa suite. Chiffres propres à la v6 : `calculs-conception-v6.py` et sa sortie
`calculs-conception-v6-sortie.json` (calculs exacts, sans tirage ; empreintes dans leurs compagnons).

## Verdict (ce que change la v6)

1. **La règle d'héritage devient une règle (K5-1 ; D-S25 bis, qui remplace D-S25).** Chaque fiche reçoit à son entrée un
   **budget** α_c/m_c (niveau et taille de sa famille d'entrée), **gardé à vie** ; une seule lecture par fin de génération,
   par la règle e-BH **pondérée** sur toutes les fiches entrées, valeurs gelées pour les abandonnées et les promues ;
   promotion une seule fois ; arrêt du processus à m_c/α_c. **Garantie** : taux de fausses découvertes de **l'union** des
   promotions de la course ≤ Σ_c α_c ≤ α, sous dépendance quelconque ; sous nul complet, c'est la probabilité d'au moins
   une fausse promotion (preuve : contre-lecture v5, § 2 (i)). Deux lectures du texte de la v5 sont **interdites** : la
   relancée lue seule à 1/α_c (0,074 d'au moins une fausse promotion, monde A′ à 20 pas par génération) et la famille
   mixte au niveau d'entrée (0,105, monde A′ à 200 pas), contre 0,0275 et 0,0315 en lecture valide (sortie `285e222f…`,
   section H).
2. **Le plafond remplace le sous-échantillon (K5-2 ; D-S27 réécrite)** : v′ = (min(m_t, m_max)/m_max)·v(t), calculé sur
   **tous** les épisodes ; l'estimande est déclarée « rappel par épisode **plafonné à m_max** » ; pour G1, m_max = maximum
   de la banque gelée (rien n'est plafonné). Sans ce mot, la v5 changeait l'estimande de N-054 en silence (promotion 1,00
   sous un nul exact du rappel par épisode avec m_max = 20 ; 0,001 avec le vrai maximum, sortie `285e222f…`, section P).
3. **Clé de l'héritage complétée (K5-7 ; D-S18)** : plus la **population** (vivier) — ou la mention « sur l'union des
   viviers lus », qui fait du produit une e-valeur pour l'intersection des nuls des viviers — et **m_max**.
4. **Seuils d'arrêt dits exactement (K5-3)** : m_g/α_g pour les fiches **nouvelles** de la génération g ; m_c/α_c (seuil
   d'entrée, gardé) pour les **relancées** ; m/α pour la **famille de G1**, lue une fois, hors suite.
5. **H1 : la règle entre modes est une lecture, et le mode tenu à l'écart doit être dimensionné (K5-4 ; D-S29 et D-S30,
   nœuds de porte ; un poste de devis).**
6. **Témoin faux promu (K5-5, K5-8 ; D-S26 bis)** : sa probabilité de promotion par hasard est α/m s'il est seul promu,
   **jusqu'à α·k/m** dans une strate qui porte k promotions vraies (0,012 à 1 000 unités, au-dessus de α/m = 0,01 ; borne
   α·k/m = 0,04 ; sortie `285e222f…`, section T) ; le sort d'une panne **confirmée** est écrit.
7. **D-S24 complétée (K5-14)** : uniforme α/G_max sur un **plafond scellé** du nombre de générations, à préférer ;
   6/(π²g²) seulement si aucun plafond ne peut être scellé.
8. **Chiffres, renvois et clarté (K5-6, K5-9 à K5-13, K5-15)** corrigés ci-dessous.
9. **Code** : la règle e-BH pondérée de D-S25 bis et le plafond de D-S27 sont codés dans `pole/pari_apparie.py` (v7,
   version 21), avec leurs essais (section 3).

## 1. Corrections, section par section de la v5

### En-tête (K5-9)
« trois chiffres et deux renvois faux » → **deux chiffres et deux renvois faux** (K-10 et K-11 : un chiffre chacun ; K-12 :
deux renvois).

### Verdict 1 (K5-3, K5-10)
Remplacer « partout où la v4 hérite « e-valeur arrêtée à m/α », lire « arrêtée à m_g/α_g » » par : **arrêtée à m_g/α_g
pour les fiches nouvelles de la génération g ; au seuil d'entrée m_c/α_c, gardé, pour les fiches relancées (D-S25 bis) ;
à m/α pour la famille de G1, lue une fois, hors suite.** Et « contre 1,00 » par « contre 1,00 aux générations 1 à 3 et
0,99 à la génération 10 » (`contre-lecture-v4/contre-verification-pari-signe-v4-sortie.json`, `c7836e12…`, section B).

### Verdict 2, D-S16 et D-S25 (K5-1, K5-6) — la règle de l'héritage

> **Règle de l'héritage (D-S25 bis).**
> 1. À son entrée dans la course, une fiche i reçoit un **budget** b_i = α_c/m_c — α_c le niveau de sa famille d'entrée
>    (la suite de dépense, D-S24), m_c la taille de cette famille, fixée avant toute issue (m fixé, v7 version 11). Le
>    budget est **gardé à vie** : il ne change ni quand ses sœurs d'entrée sont abandonnées, ni quand elle est relancée.
>    Sur toutes les fiches jamais entrées : Σ_i b_i ≤ Σ_c α_c ≤ α.
> 2. Son e-processus E_i est le produit des e-valeurs de ses parties disjointes, sous la **clé complète** (D-S18) ; il est
>    **gelé** quand la fiche est abandonnée ou promue, et **arrêté** au seuil 1/b_i = m_c/α_c.
> 3. À chaque fin de génération, **une seule lecture** : règle e-BH **pondérée** sur **toutes** les fiches entrées (en
>    cours, abandonnées et promues, ces deux dernières à leur valeur gelée) — tri par b_i·E_i décroissant, k* le plus
>    grand k tel que la k-ième valeur atteigne 1/k, promotion des k* premières. Avec une seule famille (b_i = α/m), c'est
>    la règle e-BH ordinaire.
> 4. **Promotion une seule fois** : une fiche promue le reste et n'est plus relancée.
> 5. **Garantie** : taux de fausses découvertes de l'union des promotions de la course ≤ Σ_{i nulle} b_i ≤ α, sous
>    dépendance quelconque entre fiches et entre générations ; sous nul complet, probabilité d'au moins une fausse
>    promotion (preuve : contre-lecture v5, § 2 (i), par arrêt optionnel sur l'horizon borné).
> 6. **Pour ce qui sort du pôle**, e-Bonferroni : fiche promue si E_i ≥ 1/b_i, ce seuil n'étant **jamais abaissé** ;
>    P(au moins une fausse promotion) ≤ Σ_i b_i ≤ α (contre-lecture v5, § 2 (ii)).
>
> **Lectures interdites** (sortie `285e222f…`, section H, nul complet, 10 générations, cohorte de 4 fiches relancées,
> 3 nouvelles par génération, suite 6/(π²g²), α = 0,05) : la relancée **lue seule** à 1/α_c (son budget passe de α_c/m_c
> à α_c) : 0,074 (monde A′ à 20 pas ; la cohorte seule 0,0735 > α_1 = 0,030) et 0,0465 (monde S1 ; la cohorte 0,040 >
> α_1) ; la **famille mixte au niveau d'entrée** (les nouvelles reçoivent α_1 à chaque génération) : 0,105 (A′ à 200
> pas) et 0,060 (S1). Lecture valide : 0,0275 (A′ à 20 pas), 0,0315 (A′ à 200 pas), 0,022 (S1). La famille mixte au
> **niveau courant** α_g est valide (0,030 ; 0,0115) mais fait dépenser α_g aux relancées : écartée.

La « somme des taux de fausses découvertes par génération » de la v5 est remplacée par **le taux de l'union des
promotions** (quantité propre, au moins aussi forte). **K5-6** : les taux d'héritage 0,034 à 0,041 de la v5 (verdict 2)
sont mesurés **au niveau α entier** (mécanisme, contre-lecture v4, section D), pas au niveau α_1 de la règle ; sous la
règle, une cohorte de 4 nulles lue à α_1 sur 10 générations : **0,020** dans le monde S1 (sortie `285e222f…`, section H,
lecture « cohortes »).

### 2.1 (K5-2) — D-S27 réécrite : le plafond
Remplacer le sous-échantillon scellé par : **v′(t) = (min(m_t, m_max)/m_max)·v(t)**, v(t) calculé sur **tous** les
épisodes de l'unité. Même espérance que le sous-échantillon (0,160 contre 0,1599), sans tirage, écart-type moindre (0,249
contre 0,267) (sortie `285e222f…`, section P). **Estimande déclarée** : « rappel par épisode **plafonné à m_max** »,
E[min(m_t, m_max)·v(t)] ; elle coïncide avec celle de N-054 (E[m_t·v(t)]/E[m_t]) si aucune unité ne dépasse m_max, ou si v
ne dépend pas de la longueur. **Pour G1**, la banque est gelée et m_t est connu avant le gel : m_max = maximum de la
banque, rien n'est plafonné (au prix d'une mise réduite sur les unités courtes, noté en v3). La question ne se pose que
pour une banque qui grandit (organisme, N-049).

### 2.4 bis (K5-13)
Dans le texte de la lecture du critère de G1 : « aux seuils scellés **à τ = 1 % (D-S5)** sur un calibrage de taille C… » ;
« par mode mesuré, **règle entre modes D-S10 (nœud de porte)** ».

### 3.6 (K5-7) — la clé de l'héritage
La clé (D-S18) devient : **contraste et coefficients ; pondération (v ou v′) et m_max ; τ (ou l'ensemble de τ déclaré) ;
strate ; liste des comparateurs ; seuils scellés ; population (vivier)** — ou la mention « sur l'union des viviers lus »
dans l'énoncé de la fiche relancée : le produit n'est alors une e-valeur que pour l'intersection des nuls des viviers
(l'affirmation devient « dans au moins un des viviers lus »). Toute différence d'un champ = une autre affirmation.

### 3.7 (K5-11)
« Le contrôle 20 est réécrit (section 2) » → « (section 1, « 5, contrôles ») ».

### 4, ligne H1 (K5-4) — une lecture, et sa puissance
La règle de la v5 (« si la borne basse du gain blanc-sur-noir est au-dessus de zéro dans chacun des autres modes, mode
tenu à l'écart compris ; sinon H1 restreinte au mode « coût » ») est **une lecture** du point 4 de N-054, la plus stricte
de trois :
- (a) **dans chacun** des autres modes (« contrôles » et le mode tenu à l'écart) — la v5 ;
- (b) **dans aucun** des autres modes : H1 s'étend dès qu'un autre mode montre un gain ;
- (c) **par mode** : la revendication porte sur les modes où la borne basse est au-dessus de zéro, « coût » seul ne
  suffisant pas (N-054 point 2).

Deux conséquences que la v5 taisait : sous (a), « restreinte au mode coût » veut dire, par le point 2 de N-054, **H1 non
portée** ; et le mode tenu à l'écart, conçu tard et petit (« quelques dollars »), **décide seul de H1 par sa puissance** :
il lui faut le même dimensionnement que les autres modes — 40 unités sabotées pour 20 points d'écart, 100 pour 10, à la
fiche seule (v3, § 6), davantage au seuil m/α de la famille de G1 — **poste de devis** (dépense, nœud). Et une question
que ni N-054 ni la v5 ne tranchent : l'expérience lit-elle le gain sur la **strate « diffus, flou »** (H1a, qui porte la
revendication de H1 depuis N-055) ou sur le **mode entier** ? → D-S30.

### 4, ligne G1 (K5-15) — question pour le nœud de porte
« Les génériques décident » : les comparateurs noirs restent « toutes variantes confondues », **noirs spécialisés
compris** (traits du texte liés au champ de coût, N-029). Un blanc générique contre un noir spécialisé est une comparaison
dissymétrique : à poser au nœud de porte de D-S20 (comparer les génériques aux noirs génériques, et rapporter les
spécialisés des deux côtés ?). Question, pas constat.

### 5, témoin faux promu (K5-5, K5-8) — D-S26 bis
- « Promotion attendue d'un témoin seul par hasard : de l'ordre de α/m au plus » → **α/m s'il est seul promu ; jusqu'à
  α·k/m dans une strate qui porte k promotions vraies** (son seuil e-BH y est m/(α·k)) : 0,0035 / 0,003 / 0,012 à 100 /
  250 / 1 000 unités dans une famille de 5 (3 vraies, le témoin, 1 nulle), pour α/m = 0,01 et α·k/m = 0,04 (sortie
  `285e222f…`, section T). Perte de puissance d'une suspension à tort : au plus α·k/m par strate et par lecture, un délai
  jusqu'au nouveau tirage.
- La suspension **ne peut que baisser** la probabilité d'au moins une fausse promotion ; le taux de fausses découvertes
  de l'ensemble **survivant** n'est pas couvert par la preuve e-BH (retirer une strate peut faire monter la proportion
  restante), mais il est mesuré **en baisse** (0,0005 contre 0,0014 ; 0,00125 contre 0,002 ; 0,00275 contre 0,00575 à
  100 / 250 / 1 000 unités, même section) — « sans effet pratique », non « sans effet ».
- **Panne confirmée (D-S26 bis)** : le nouveau tirage du témoin (graine **dérivée par le noyau**, `SeedSequence`, R9,
  consignée au manifeste) est lu à la même règle ; s'il est promu à nouveau, la panne est confirmée : (1) les promotions
  suspendues de la strate sont **retirées** (marquées « retirée, panne confirmée », jamais effacées) ; (2) les processus
  hérités de la strate sont **gelés** (plus aucune relance) ; (3) la strate n'est relue qu'après correction de la cause,
  sur une **partie et un calibrage neufs**, comme des fiches **nouvelles** (nouveaux budgets, nouvelle entrée) ; (4) la
  panne est rapportée comme un résultat (l'instrument échoue sur cette strate) et **bloque** toute revendication de G1 sur
  la strate. Sinon (nouveau tirage non promu), la présomption est levée et les promotions suspendues sont confirmées.

### 6 (K5-12)
Rappeler le seuil : « à 6 unités ou moins, rien n'est promouvable » vaut **au seuil 20 (fiche seule, m = 1)** (17,61 à
v = 1 ; 7 unités : 31,11). **À m = 3 (seuil 60)** : 8 unités ou moins ne promeuvent rien (55,77 à v = 1) ; 9 unités
suffisent à v = 1 (101,09) (`calculs-conception-v6-sortie.json`, section 6).

## 2. Décisions (v5, plus D-S25 bis, D-S26 bis, D-S29, D-S30 ; D-S18, D-S24, D-S27 réécrites)

| décision | recommandation (confiance) |
|---|---|
| D-S18 (complétée, K5-7) | clé : contraste et coefficients ; pondération et **m_max** ; τ ; strate ; comparateurs ; seuils ; **population** ou « sur l'union des viviers lus » (0,85) |
| D-S24 (complétée, K5-14) | **uniforme α/G_max sur un plafond G_max scellé au gel de la course** (paramètre de conception de l'organisme, au devis ; le budget des générations non faites est perdu) ; 6/(π²g²) seulement si aucun plafond ne peut être scellé — l'uniforme donne plus dès la génération 3 pour G_max = 10 (0,005 contre 0,0034) et dès la génération 5 pour G_max = 30 (0,00167 contre 0,00122) ; 6/(π²g²) dépense 61 % de α à la génération 1 (`calculs-conception-v6-sortie.json`) (0,75) |
| **D-S25 bis** (remplace D-S25, K5-1) | la règle de l'héritage ci-dessus : budget d'entrée gardé à vie, une lecture e-BH pondérée par génération sur toutes les fiches entrées, valeurs gelées, promotion une seule fois, arrêt à m_c/α_c ; garantie sur l'union des promotions ; e-Bonferroni pour ce qui sort (0,8) |
| **D-S26 bis** (complète D-S26, K5-8) | panne confirmée : promotions retirées et marquées, processus hérités gelés, strate relue sur partie et calibrage neufs comme fiches nouvelles, panne rapportée et bloquante pour G1 sur la strate (0,65) |
| D-S27 (réécrite, K5-2) | **plafond** min(m_t, m_max)/m_max sur tous les épisodes ; estimande « plafonnée » déclarée ; pour G1, m_max = maximum de la banque gelée (0,8) |
| **D-S29** (nœud de porte, K5-4) | règle de H1 entre modes : (a) dans chacun des autres modes, mode tenu à l'écart compris — sinon H1 non portée ; (b) dans aucun ; (c) par mode ; **(a)**, marquée « lecture », avec le dimensionnement du mode tenu à l'écart (0,55) |
| **D-S30** (nœud de porte, K5-4) | strate de lecture du gain dans l'expérience de N-054 point 4 : (a) la strate « diffus, flou » de chaque mode, le mode entier rapporté ; (b) le mode entier ; **(a)** : H1a porte la revendication (N-055), et un gain qui n'existerait que hors de la strate ne la soutient pas ; coût : plus d'unités dans le mode tenu à l'écart (0,6) |
| poste de devis (nœud de dépense) | mode tenu à l'écart dimensionné comme les autres modes (40 unités sabotées pour 20 points, 100 pour 10, à la fiche seule ; davantage à m/α et, sous D-S30 (a), sur la seule strate « diffus, flou ») |

Défauts sous 48 heures : les recommandations, sauf D-S10, D-S11, D-S20, D-S29 et D-S30 (nœuds de porte, au
préenregistrement de G1) et le poste de devis (dépense : mot direct de Lazar chez session-depot). **Nœuds pour Lazar,
inchangés** : comparateurs de G1 ; N-054 point 4 (`noeuds-pour-lazar-v1.md`, `d9a6ff1b…`) ; plus la question K5-15
(génériques contre noirs spécialisés), à joindre au nœud de D-S20.

## 3. Code (v7, version 21)

`orchestrateur-pole-v7/pole/pari_apparie.py` ajoute :
- `ebh_pondere(produits, budgets)` : la lecture de D-S25 bis (tri par b_i·E_i, k* le plus grand k dont la k-ième valeur
  atteint 1/k) ; refuse une somme de budgets au-dessus de α ;
- `Course` : entrée d'une famille (budgets α_c/m_c fixés à l'entrée), produit des e-valeurs par fiche, gel à l'abandon
  et à la promotion, arrêt à 1/b_i, une lecture par fin de génération, promotion une seule fois, union des promotions ;
  relecture e-Bonferroni ;
- `ponderation_plafonnee(m_t, m_max)` et `contraste_plafonne(...)` (D-S27).

Essais (`essais/test_v7_pari_apparie.py`) : e-BH pondérée égale à l'ordinaire pour une famille ; budgets au-dessus de α
refusés ; budget gardé quand les sœurs sont abandonnées ; promotion une seule fois ; **sous nul complet, monde A′,
lecture valide ≤ α**, alors que la lecture « seule » de la relancée **dépasse** la lecture valide (mécanisme de K5-1) ;
plafond : bornes, et coïncidence avec v′ quand m_t ≤ m_max.

## 4. Ce que la v6 laisse ouvert (dit)

La règle est codée hors du cycle (le lien avec les générations du pôle — monde sur banque de scores, engagement, clé
complète dans la mémoire — reste à faire) ; la règle en ligne et l'héritage ne sont simulés que dans des mondes
illustratifs (A′, S1) ; le contrôle 18 au C dimensionné n'est pas simulé ; e-LOND et Maurer et Pontil restent à vérifier
sur PDF (R7) ; D-S29 et D-S30 attendent le préenregistrement de G1 ; le dimensionnement du mode tenu à l'écart attend un
devis.
