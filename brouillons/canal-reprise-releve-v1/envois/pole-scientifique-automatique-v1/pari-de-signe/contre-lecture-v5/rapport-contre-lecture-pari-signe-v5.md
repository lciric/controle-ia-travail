# Contre-lecture (R2) — « Le pari apparié borné — conception v5, corrections locales » (Opus 5.5) — rapport v1

Contre-lecteur : sous-agent neuf **Fable 5.1**, autre modèle que l'auteur de la v5 ; je n'ai écrit ni la v5, ni la
contre-lecture de la v4, ni aucune version antérieure. Début : mardi 27 octobre 2026, 20:34:57 UTC ; en-tête écrit à
20:54:40 UTC (`date -u`). Aucun fichier du dépôt modifié ; tout ce que j'ai écrit est dans
`/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/contre-lecture-pari-signe-v5/`. Aucune clé ni
aucun jeton lu, affiché ou cherché. Aucune dépense : processeur seul (section 7). Aucun des fichiers lus ne contient de
consigne adressée au contre-lecteur. Je n'ai pas lu N-049, ni le code de v7, ni les autres décisions du dépôt.

## Verdict

1. **La v5 ferme K-2 à K-19 sur le fond (K-3 fermé trop large, K-5 à moitié) et les cinq décisions manquantes ; K-1
   sauf deux champs (population, m_max).** Les chiffres et renvois sont tous justes contre les sorties citées
   (section 3), à trois détails près (0,99 écrit 1,00 ; « trois chiffres et deux renvois » pour deux et deux ; un
   pointeur « section 2 » faux).
2. **Elle n'introduit pas de chiffre faux ; deux points touchent la garantie et trois lectures sont trompeuses.**
   Garantie : la règle d'héritage n'est pas opératoire (point 3) ; le sous-échantillon de D-S27 change l'estimande de
   N-054 sans le dire (reproduit : promotion 1,00 sous un nul exact du rappel par épisode) et un plafond le domine.
   Lectures : « arrêtée à m_g/α_g partout » contredit D-S25 pour les fiches relancées ; « α/m au plus » pour le témoin
   ne vaut que s'il est seul promu (reproduit : 0,012 > α/m à 1 000 unités) ; la règle de H1 est une lecture du point 4
   de N-054, pas son texte.
3. **Le point de garantie ouvert : « garde le niveau de son entrée » n'est pas une règle.** La garantie tient si et
   seulement si chaque fiche garde à vie le **budget** α_c/m_c de sa famille d'entrée (m_c fixé, famille relue avec
   valeurs gelées, promotion une seule fois) : je le démontre (section 2, (i)). Sous deux lectures plausibles du texte
   de la v5 — relancée lue seule à 1/α_c ; famille mixte au niveau d'entrée des relancées — la probabilité d'au moins
   une fausse promotion atteint 0,074 et 0,105 pour α = 0,05 (reproduit, section 7). **Amender en v6 par une règle
   écrite (D-S25 bis), pas refaire.**

---

## 1. La v5 contre les constats K-1 à K-19 et les décisions manquantes

| constat | fermé ? | remarque |
|---|---|---|
| K-1 clé de l'héritage | **presque** | champs écrits : contraste et coefficients, pondération, τ, strate, comparateurs, seuils. Manquent : la **population** (vivier ; la contre-lecture v4 l'avait signalé « hors liste », N-049) et **m_max** (la pondération v′ dépend de m_max : deux m_max = deux estimandes, section 2 (iii)) |
| K-2 D-S17 (a) | oui | désignation scellée avant lecture, ou confirmation sur partie et calibrage neufs ; D-S28 |
| K-3 arrêt à m_g/α_g | **trop large** | « partout » : faux pour les fiches relancées (seuil d'entrée m_c/α_c, D-S25) et, à la lettre, pour la famille de G1 (lue une fois, m/α, hors suite) |
| K-4 coût, héritage | oui | chiffres justes ; mais les 0,034 à 0,041 cités sont au niveau α entier pour la cohorte (section D de la contre-lecture), pas au niveau α_1 de la règle v5 : illustration du mécanisme, pas taux de la règle |
| K-5 garantie dite | **à moitié** | juste pour les fiches nouvelles ; avec des fiches relancées hors des familles α_g, la quantité bornée est le taux de fausses découvertes de **l'union** des promotions de la course (section 2 (i)) |
| K-6 règle de H1 | oui, en lecture | conforme au point 4 sous sa lecture la plus stricte ; à marquer « lecture » ; conséquence sur la puissance du mode tenu à l'écart non dite (section 2 (iv)) |
| K-7 contrôle 18 | oui | critère écrit ; non simulé, dit en § 3 |
| K-8 bris à C = 1 000 | oui | chiffres justes (sortie T) |
| K-9 artefact du contrôle 20 | oui | « > α dès G = 10 » ; 0,111 / 0,197 justes |
| K-10, K-11, K-12 | oui | 0,029 / 0,028 ; 0,06 à 0,13 ; renvois échangés : justes |
| K-13 m_t > m_max | oui, mais | règle écrite ; l'estimande change et le sous-échantillon est dominé (section 2 (iii)) |
| K-14 expérience de lecture | oui | à l'évaluation, partie finale ou sœur scellée |
| K-15 témoin promu | oui, mais | suspension, nouveau tirage ; le sort d'une panne **confirmée** n'est pas dit ; « α/m au plus » incomplet (section 2 (v)) |
| K-16 D-S10 nœud de porte | oui | |
| K-17 convention L | oui | |
| K-18 § 6 | oui | chiffres justes ; le seuil 20 (fiche seule, m = 1) n'est pas rappelé |
| K-19 lecture du critère de G1 | oui | § 2.4 bis conforme à N-008 et N-054 point 2 ; τ = 1 % n'y est pas écrit (D-S5) |
| décisions manquantes 1 à 5 | oui | D-S24 à D-S28 |

## 2. Mathématiques

### (i) Héritage et règle en ligne dans une même course : preuve, et ce qui la fait tomber

**Ce que la v5 écrit.** Une fiche relancée est « une seule surmartingale », « garde le niveau de son entrée », « ne
dépense pas α_g » ; la règle e-BH au niveau α_g à chaque génération « ne vaut que pour les fiches nouvelles » et
« borne la somme des taux de fausses découvertes par α ». Elle ne dit pas **dans quelle famille, à quel seuil, avec
quel m** une fiche relancée est relue, ni ce qu'il advient de m quand ses sœurs d'entrée sont abandonnées, ni qu'une
fiche n'est promue qu'une fois.

**Proposition (lecture valide).** Chaque fiche i reçoit à son entrée un budget b_i > 0, **fixé à vie**, avec
Σ_i b_i ≤ α sur toutes les fiches jamais entrées dans la course (par exemple b_i = α_c/m_c : niveau et taille de sa
famille d'entrée). Son e-processus E_i est une surmartingale positive partant de 1 pour la filtration des générations
(produit des e-valeurs de parties disjointes ; valeur **gelée** quand la fiche est abandonnée ou promue). À chaque fin de
génération, on relit **toutes** les fiches entrées : promotion de i si E_i ≥ 1/(b_i·k), k étant le nombre de fiches
promues à cette lecture (règle e-BH pondérée ; avec b_i = α_c/m_c pour une seule cohorte, c'est la règle e-BH ordinaire).
Une fiche promue reste promue. Alors, sous dépendance quelconque entre fiches et entre générations :

> taux de fausses découvertes de l'union R_∪ de toutes les promotions de la course ≤ Σ_{i nulle} b_i ≤ α.

*Preuve.* Soit i nulle, promue pour la première fois à la lecture τ_i (temps d'arrêt ; τ_i = G si jamais), avec k_{τ_i}
promotions à cette lecture, toutes dans R_∪ : 1/|R_∪| ≤ 1/k_{τ_i} ≤ b_i·E_i(τ_i). Donc la proportion de fausses
découvertes de R_∪ est ≤ Σ_{i nulle} b_i·E_i(τ_i) ; par arrêt optionnel (horizon G borné), E[E_i(τ_i)] ≤ 1. ∎
Sous nul complet, l'union n'a que des fausses promotions : la borne est la probabilité d'au moins une fausse promotion.
La « somme des taux de fausses découvertes par génération » de la v5 n'est bornée par ce raisonnement que sous une
convention précise (au numérateur, les fausses promotions **nouvelles** de la génération ; au dénominateur, l'ensemble
**complet** des fiches au-dessus de leur seuil à cette lecture, promues antérieures comprises) ; la quantité propre est
l'union. C'est donc une garantie au moins aussi forte que celle annoncée, **à condition que les budgets d'entrée soient
gardés et que m_c ne bouge pas** ; une fiche relancée ne dépense rien de plus, et une famille mixte (relancées et
nouvelles lues ensemble, k commun) est valide dès que chaque fiche garde son b_i.

**Ce qui la fait tomber (contre-exemples, reproduits, section 7 H).** Deux lectures plausibles de « garde le niveau de
son entrée » :
- **« seule »** : la relancée est lue seule au seuil 1/α_c (son niveau, m = 1 puisque ses sœurs sont abandonnées). Son
  budget passe de α_c/m_c à α_c ; la cohorte peut consommer jusqu'à m_c·α_c. Monde A′ (martingale ×1,5 / ×0,5, 20 pas
  par génération), cohorte de 4 nulles, 10 générations, α = 0,05 : **0,074** d'au moins une fausse promotion (cohorte
  seule : 0,0735 > α_1 = 0,030), contre 0,0275 en lecture valide. Monde S1 (250 unités par génération) : 0,0465
  (cohorte : **0,040 > α_1**), contre 0,022.
- **« mixte au niveau d'entrée »** : relancées et nouvelles forment, à chaque génération, une famille e-BH ordinaire au
  niveau α_1 de la relancée. Les nouvelles reçoivent alors α_1 à chaque génération au lieu de α_g : Σ budgets > α.
  Monde A′ (200 pas) : **0,105** ; monde S1 : **0,060** ; contre 0,0315 et 0,022 en lecture valide.
- **« mixte au niveau courant α_g »** (les relancées dépensent α_g, contraire à D-S25) : valide (0,030 ; 0,0115), mais
  elle retire aux relancées ce que D-S25 veut leur donner.

Sous nuls partiels (cohorte : 3 vraies + 1 nulle ; 1 vraie + 2 nulles par génération ; S1 ; lecture valide) : taux de
fausses découvertes de l'union 0,0012 pour une borne 0,0187 ; les 12 vraies promues à chaque fois.

**Conclusion (i).** La garantie tient, et sous une forme plus forte que celle écrite, mais la v5 ne fixe pas la lecture
qui la fait tenir ; deux lectures naturelles de son texte la cassent. **Correction** : écrire D-S25 ainsi — « une fiche
reçoit à son entrée le budget α_c/m_c (niveau et taille de sa famille d'entrée), gardé à vie ; à chaque fin de
génération, règle e-BH pondérée sur toutes les fiches entrées, valeurs gelées pour les abandonnées et les promues ;
promotion une seule fois ; arrêt du processus à 1/b_i = m_c/α_c ; garantie : taux de fausses découvertes de l'union des
promotions de la course ≤ Σ_c α_c ≤ α, probabilité d'au moins une fausse promotion sous nul complet. »

### (ii) e-Bonferroni à m_g/α_g pour ce qui sort du pôle

Oui. Pour une fiche nulle au seuil T_i, l'inégalité de Ville donne P(sup E_i ≥ T_i) ≤ 1/T_i, lecture continue comprise ;
l'inégalité de l'union sur les nulles et les générations donne P(au moins une fausse promotion) ≤ Σ_i 1/T_i ≤ Σ_g α_g
≤ α, sous dépendance quelconque. **Condition** : T_i est le **plus bas** seuil contre lequel la fiche i est jamais lue ;
avec T_i = m_c/α_c fixé à l'entrée, Σ_i 1/T_i = Σ_c α_c. La même lecture « seule » (T_i ramené à 1/α_c) casse aussi
e-Bonferroni (jusqu'à m_c·α_c par cohorte). Le choix e-Bonferroni ou e-BH peut être fait après coup pour « ce qui
sort » : les promotions e-Bonferroni sont un sous-ensemble des promotions e-BH et la borne de Ville ne dépend pas du
reste. L'e-valeur doit être valide pour le nul **aux seuils scellés** ou à calibrage neuf désigné (D-S17, D-S28) : la
v5 le tient.

### (iii) Sous-échantillon scellé de m_max épisodes (D-S27)

**Valide comme e-processus** : v′ reste dans [−1 ; 1], le tirage est fixé avant toute issue, l'unité reste tirée de la
population. **Mais l'estimande change** : E[v′] = (1/m_max)·E[min(m_t, m_max)·v(t)], le rappel par épisode **plafonné à
m_max épisodes par unité**, et non le rappel par épisode de N-054, E[m_t·v(t)]/E[m_t]. Les deux coïncident si aucune
unité ne dépasse m_max ou si v ne dépend pas de la longueur. Contre-exemple reproduit (section 7 P) : moitié d'unités
longues (100 épisodes, v = −0,08), moitié de courtes (10 épisodes, v = +0,8) : E[m_t·v] = 0 exactement (nul de N-054,
frontière) ; m_max = 20 : E[v′] = 0,16, **promotion 1,00** sur 250 unités ; m_max = 100 (vrai maximum) : 0,001. Et le
**plafond** v′ = (min(m_t, m_max)/m_max)·v(t) calculé sur **tous** les épisodes a la même espérance (0,160 contre
0,1599), sans tirage, avec moins de variance (écart-type 0,249 contre 0,267) : il domine le sous-échantillon. Pour G1,
la banque est gelée et m_t est un trait connu avant le gel : m_max = maximum de la banque ne tronque rien (au prix
d'une mise réduite sur les unités courtes, prix que la v3 avait noté) ; la question ne se pose que pour une banque qui
grandit (organisme, N-049). **Correction** : D-S27 → plafond min(m_t, m_max)/m_max sur tous les épisodes ; estimande
déclarée « rappel par épisode plafonné à m_max » ; m_max dans la clé de l'héritage.

### (iv) Règle de H1 entre modes et le point 4 de N-054

Texte de N-054 : « la revendication de H1 est restreinte au mode « coût » si la borne basse du gain blanc-sur-noir
n'est pas au-dessus de zéro dans les autres modes » ; les autres modes sont « contrôles » et le mode tenu à l'écart (lus
tous deux par l'expérience) : « mode tenu à l'écart compris » est **conforme au texte**. Le repli « restreinte au mode
coût » aussi. Mais « n'est pas au-dessus de zéro dans les autres modes » admet trois lectures : (a) dans **chacun** des
autres modes (la v5 : tout ou rien, la plus stricte) ; (b) dans **aucun** des autres modes (H1 s'étend dès qu'un autre
mode montre un gain) ; (c) revendication **par mode** sur les modes où la borne basse est > 0, « coût » seul ne suffisant
pas (point 2). La v5 écrit (a) comme « tirée du point 4 » : c'est une lecture, à marquer comme telle (elle l'a fait pour
D-S20, pas ici). Deux conséquences non dites : sous (a), « restreinte au mode coût » signifie, par le point 2, **H1 non
portée** ; et le mode tenu à l'écart, conçu tard et petit (N-054 : « quelques dollars »), décide seul de H1 par sa
puissance : il lui faut le même nombre d'unités sabotées que les autres modes (40 pour 20 points, 100 pour 10, § 6),
poste de devis. Dernier point : l'expérience lit-elle le gain sur la strate « diffus, flou » (H1a) ou sur le mode
entier ? Ni N-054 ni la v5 ne le disent.

### (v) Suspension des promotions d'une strate dont le témoin faux est promu (D-S26)

**Validité.** La probabilité d'au moins une fausse promotion ne peut que baisser. Le taux de fausses découvertes de
l'ensemble **survivant** n'est pas formellement couvert par la preuve e-BH (retirer une strate entière peut faire
monter la proportion restante : trois vraies retirées, une nulle ailleurs gardée) ; l'excès est borné par la probabilité
de suspension et, en simulation (section 7 T), le taux survivant **baisse** (0,0005 contre 0,0014 ; 0,00125 contre
0,002 ; 0,00275 contre 0,00575 à 100 / 250 / 1 000 unités), parce que le témoin retiré est lui-même une fausse
découverte. Sans effet pratique ; à dire ainsi plutôt que « sans effet ».
**Puissance.** Perte ≤ probabilité d'une suspension à tort. Celle-ci n'est « de l'ordre de α/m » que si le témoin est
**seul** promu ; dans une strate qui porte k promotions vraies — le cas où suspendre coûte —, son seuil e-BH est
m/(α·k) et la probabilité monte jusqu'à α·k/m ≤ α. Reproduit : famille de 5 (3 vraies, témoin S1, 1 nulle), témoin
promu dans 0,0035 / 0,003 / **0,012** des cas à 100 / 250 / 1 000 unités (α/m = 0,01 ; α·k/m = 0,04) ; vraies perdues
0,01 à 0,036 sur 3. Une panne confirmée à tort coûte au plus (α·k/m)² par strate et génération. Coût réel : un délai
jusqu'au nouveau tirage. **Manque** : ce qu'entraîne une panne **confirmée** (promotions retirées ? processus hérités
gelés ? strate relue sur une partie neuve ?), et que la graine neuve est dérivée par le noyau (R9).

## 3. Chiffres : chaque chiffre de la v5 contre son fichier

| où (v5) | cité | fichier, valeur | verdict |
|---|---|---|---|
| verdict 1 | 0,0095 à g = 1, puis 0, contre 1,00 | `c7836e12…` B : 0,0095 / 0 / 0 / 0 contre 1,0 / 1,0 / 1,0 / **0,9918** | juste ; 0,99 à g = 10 arrondi en « 1,00 » |
| verdict 2 | héritage 0,034 à 0,041 ; à neuf 0,18 à 0,51 | `c7836e12…` D : 0,0335 / 0,0365 / 0,0367 / 0,0405 ; 0,1812 / 0,2248 / 0,466 / 0,5128 | juste (au niveau α, cf. K-4) |
| verdict 2 | 1,33·α_g ; S1 : 0,009 à 0,010 | `c7836e12…` A : 1,3333 ; 0,01 (G = 10), 0,00925 (G = 30) | juste |
| verdict 4 | 45 ; 49 / 66 / 84 / 100 ; 63, 71 ; 109 ; 119 / 159 / 201 / 239 ; 153, 173 | `c7836e12…` C, puissance 0,9, m = 3 | tous justes |
| § 2.4 l. 2 | 0,025 et 0,143 (infini, pas 0,5) ; 1,6 point ; 0,032 → 0,137 ; 0,0085 → 0,072 ; 0,45 point | `38efb971…` T : 0,025 ; 0,143 ; 0,0156 / 0,016 ; 0,032 → 0,137 ; 0,0085 → 0,072 ; 0,0041 / 0,0045 | justes |
| contrôle 20 | 0,111 ; 0,197 (G = 10) ; 0,033 ; 0,067 (G = 3) | `654457a8…` B iv : 0,111 ; 0,1965 ; 0,033 ; 0,0665 | justes |
| témoin | 0,029 (90/10), 0,028 (80/20) à 1 000 ; 0 / 0,0115 / 0,018 | `654457a8…` D, avec remise : 0,029 ; 0,028 ; 0 / 0,0115 / 0,018 | justes |
| § 6 | 0,551 ; 101 ; 17,6 ; 0,858 ; 31,1 ; 0,725 | `c7836e12…` E : 0,5514 ; 101,09 ; 17,61 ; 0,8582 ; 31,11 ; 0,7245 | justes (seuil 20, fiche seule : non rappelé) |
| § 6 bis | 0,06 à 0,13 ; 0,133 batterie, 0,137 exact | `ead1b9d5…` : 0,133 à 60 sous S1 (0,0595 à 0,133 sur 60 à 250) ; `654457a8…` A : 0,1374 | justes |
| § 6 bis | miroirs 0,008 à 0,043 dans `654457a8…` A ; 98/2 0,55 / 0,30 / 0,13, pari 0,0095 dans `082794ea…` | `654457a8…` A : 0,0078 à 0,0427 ; `082794ea…` : 0,5455 / 0,2976 / 0,1326 ; pari 0,0095 à 250 | justes |
| en-tête | contre-lecture v4 : « trois chiffres et deux renvois faux » | `937994b5…` : K-10 un chiffre, K-11 un chiffre, K-12 deux renvois | **deux chiffres et deux renvois** |
| § 1, 3.7 | « Le contrôle 20 est réécrit (section 2) » | la réécriture est en section 1, « 5, contrôles » ; la section 2 est le tableau des décisions | pointeur faux |
| en-tête | relevé `date -u` 20:33:22 ; fichier v5 modifié à 20:34 UTC | cohérent | |

Les empreintes citées (`c63d8539…`, `937994b5…`, `d9a6ff1b…`, `38efb971…`, `654457a8…`, `082794ea…`) correspondent
toutes aux fichiers (section 8).

## 4. Décisions D-S24 à D-S28 : recommandations et confiances

| décision | avis |
|---|---|
| D-S24 suite de dépense (0,7) | Justifiée dans ses termes, options incomplètes. La suite 6/(π²g²) dépense 61 % de α à la génération 1 et ne laisse que α_10 = 0,0003 à g = 10 (seuil 9 870 pour m = 3 : 84 unités à 20 points). **Manque** l'option « uniforme sur un G_max scellé » : elle bat 6/(π²g²) dès g = 3 pour G_max = 10 (α/10 = 0,005 contre α_3 = 0,0034) et dès g = 5 pour G_max = 30 (α/30 = 0,00167 contre α_5 = 0,00122). Le nombre de générations est un paramètre de conception de l'organisme (budget, couche 2) : il est scellable. Recommandation à préférer : sceller G ou G_max au gel ; 6/(π²g²) seulement si c'est impossible. Confiance 0,7 raisonnable pour le principe. |
| D-S25 niveau des fiches relancées (0,8) | Principe juste, **règle non opératoire** (section 2 (i)) : deux lectures du texte cassent la garantie. À réécrire comme budget d'entrée gardé à vie, m_c fixé, famille relue avec valeurs gelées, promotion une seule fois. Confiance 0,8 tenable une fois la règle écrite, pas avant. |
| D-S26 strate dont le témoin faux est promu (0,75) | Défendable ; sans effet sur la probabilité d'au moins une fausse promotion ; coût de puissance ≤ α·k/m par strate et lecture (pas α/m), délai jusqu'au nouveau tirage. **Manque** le sort d'une panne confirmée. |
| D-S27 unité au-delà de m_max (0,8) | Valide mais **dominée** par le plafond min(m_t, m_max)/m_max sur tous les épisodes (même estimande, sans tirage, variance moindre) ; dans les deux cas l'estimande est « plafonnée », à déclarer ; pour G1, m_max = maximum de la banque gelée, et la décision ne joue que pour une banque qui grandit. Confiance à reporter sur le plafond. |
| D-S28 générations à calibrage neuf (0,8) | Justifiée ; une désignation adaptative (décidée d'après le passé, scellée avant la lecture de la génération) reste valide : l'e-valeur de la génération est conditionnelle au passé. |

**Décisions manquantes** (proposer avec recommandation) :
1. **D-S25 bis**, la règle opératoire de l'héritage (famille, seuil, m fixé, promotion unique, valeurs gelées) : c'est le
   point de garantie ouvert.
2. Sort d'une **panne confirmée** (D-S26) : promotions retirées ou non, processus hérités, relecture sur partie neuve.
3. **Puissance du mode tenu à l'écart** pour la règle de H1 (iv) : nombre d'unités sabotées de ce mode au devis (dépense,
   nœud).
4. **Estimande déclarée** sous D-S27 (« plafonné à m_max ») et m_max dans la clé de l'héritage ; pour G1, m_max =
   maximum de la banque gelée.
5. Le mot « lecture » sur la règle de H1 (iv) et sur « génériques décident » (déjà fait pour ce dernier).

## 5. Constats, du plus grave au moins grave

### Garantie touchée

**K5-1 — La règle d'héritage n'est pas opératoire ; deux lectures plausibles cassent la garantie** (reproduit,
section 7 H ; preuve de la lecture valide, section 2 (i)).
- **Où.** Verdict 2, D-S25, D-S16 réécrite, contrôle 20.
- **Ce qui manque.** Famille et seuil de relecture d'une fiche relancée ; m_c gardé quand ses sœurs sont abandonnées ;
  promotion une seule fois ; valeurs gelées ; forme de la garantie (union des promotions de la course).
- **Chiffres.** Lecture « seule » : 0,074 (A′), cohorte 0,040 > α_1 (S1) ; « mixte au niveau d'entrée » : 0,105 (A′),
  0,060 (S1) ; lecture valide : 0,022 à 0,0315 ; α = 0,05.
- **Correction.** D-S25 bis comme en section 2 (i), et K-5 redit : « taux de fausses découvertes de l'union des
  promotions ≤ Σ_c α_c ≤ α ».

**K5-2 — D-S27 change l'estimande de N-054 sans le dire, et le sous-échantillon est dominé** (reproduit, section 7 P).
- **Où.** § 2.1, D-S27, D-S22 (par héritage de la v4).
- **Ce qui manque.** « Rappel par épisode plafonné à m_max » ≠ « rappel par épisode » dès qu'une unité dépasse m_max et
  que v dépend de la longueur : promotion 1,00 sous un nul exact de N-054 (E[m_t·v] = 0, E[v′] = 0,16).
- **Correction.** Plafond min(m_t, m_max)/m_max sur tous les épisodes ; estimande déclarée ; m_max dans la clé ; pour G1,
  m_max = maximum de la banque gelée.

### Lecture trompeuse

**K5-3 — « Arrêtée à m_g/α_g partout »** (reproduit : texte contre texte). Verdict 1 contredit D-S25 (seuil d'entrée
des relancées) et, à la lettre, la famille de G1 (m/α, lue une fois, hors suite). Correction : « pour les fiches
nouvelles de la génération g ; seuil d'entrée m_c/α_c pour les relancées ; m/α pour la famille de G1 ».

**K5-4 — Règle de H1 écrite comme le texte du point 4** (reproduit : texte contre décision). § 4 ligne H1. Trois
lectures possibles ; la plus stricte retenue sans le dire ; « restreinte au mode coût » = H1 non portée (point 2) ;
puissance du mode tenu à l'écart décisive, non dimensionnée. Correction : marquer « lecture », lister (b) et (c),
ajouter le poste de devis.

**K5-5 — « Promotion attendue d'un témoin seul par hasard : α/m au plus »** (reproduit, section 7 T : 0,012 > 0,01 à
1 000 unités avec 3 vraies promues). Correction : « α/m s'il est seul promu ; jusqu'à α·k/m avec k promotions vraies ».

**K5-6 — Les taux d'héritage cités (0,034 à 0,041) sont au niveau α entier** (reproduit, script de la contre-lecture
v4, section D : e-BH à α, seuil m/α), non au niveau α_1 de la règle v5. Correction : « mécanisme mesuré au niveau α ;
sous la règle, la cohorte 1 est à α_1 : plus bas (cohorte de 4 nulles S1 à α_1, 10 générations : 0,020 dans ma
simulation) ».

**K5-7 — K-1 : la clé omet la population et m_max** (soupçonné pour la population, N-049 non lu ; reproduit pour
m_max par K5-2). Si les générations tirent de viviers différents, le produit n'est une e-valeur que pour l'intersection
des nuls de chaque population (« au moins une des versions »). Correction : ajouter « population (vivier), ou mention
« sur l'union des viviers lus » » et « m_max » à la clé.

**K5-8 — D-S26 : le sort d'une panne confirmée n'est pas dit** (texte). Correction : une phrase ; et dire que la
suspension laisse intacte la probabilité d'au moins une fausse promotion, le taux de fausses découvertes de l'ensemble
survivant n'étant pas couvert par la preuve mais mesuré en baisse (section 2 (v)).

### Chiffre faux

**K5-9 — « Trois chiffres et deux renvois faux »** (reproduit : K-10, K-11, K-12). Deux chiffres et deux renvois.

**K5-10 — « Contre 1,00 »** : 0,99 à g = 10 (`c7836e12…` B). Arrondi, à écrire « 1,00 puis 0,99 ».

### Clarté

**K5-11 — Pointeur « (section 2) »** pour le contrôle 20 : la réécriture est en section 1, § 5.

**K5-12 — § 6** : le seuil 20 (fiche seule, m = 1) sous lequel « 6 unités ou moins, rien » est vrai n'est pas rappelé ;
à m = 3 (seuil 60), il faut plus.

**K5-13 — § 2.4 bis** : τ = 1 % (D-S5) et la règle entre modes (D-S10) n'y sont pas nommés ; « par mode mesuré » suffit
si le préenregistrement les ajoute.

**K5-14 — D-S24** : option « uniforme sur un G_max scellé » absente (section 4).

**K5-15 — § 4 G1, « génériques décident »** : les comparateurs noirs restent « toutes variantes confondues », y compris
les noirs spécialisés (traits du texte liés au champ de coût, N-029) ; un blanc générique contre un noir spécialisé
est une comparaison dissymétrique, à dire au nœud de porte (question, pas constat).

## 6. Ce qui tient (une ligne chacun)

- K-3 sur le fond : l'arrêt à m_g/α_g pour les fiches nouvelles ; chiffres B justes.
- K-4 : coûts de la règle en ligne comptés, chiffres C justes ; héritage sans dépense par génération.
- K-5 : la somme des taux de fausses découvertes des familles α_g ≤ α sous dépendance quelconque ; e-Bonferroni borne
  la probabilité d'au moins une fausse promotion par Σ α_g (section 2 (ii)) ; LORD et e-LOND dits à vérifier (R7).
- K-1 : contraste et coefficients, pondération, τ, strate, comparateurs, seuils : chaque champ nommé définit bien le nul.
- K-2, K-14, K-16, K-17, K-18, K-19 : fermés, conformes à N-007, N-008, N-054 et aux décisions de Lazar (D-S10 fixée au
  préenregistrement ; H1a porte, H1b informe).
- K-6 : « mode tenu à l'écart compris » et le repli sont dans le texte du point 4.
- K-7 : les deux lectures du contrôle 18 au C dimensionné, avec critère ; non simulé, dit.
- K-8, K-9, K-10, K-11, K-12 : chiffres et renvois justes.
- K-13 : règle écrite avant toute issue ; bornes de v′ justes (1 + 0,9·v′ < 0 dès v′ < −1,11 ; reproduit : 0,8 % des
  unités dans mon monde à deux longueurs).
- K-15 : suspension, nouveau tirage à graine neuve, présomption : juste sur le fond.
- D-S17 précisée, D-S18, D-S28 : justes.
- Section 3 : ce qui reste ouvert est dit (règle en ligne non simulée sur les générations réelles, clé non codée,
  contrôle 18 non simulé, R7).
- Le sous-échantillon de D-S27 est bien un e-processus valide (pour son estimande).

## 7. Vérifications sur processeur

Interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B` (Python 3.13.17, numpy 2.5.4) ; graines
`SeedSequence(2026102707, spawn_key=(section, indice))` (R9) ; 2 000 répétitions ; 27 secondes ; manifeste dans la sortie.

| fichier | SHA-256 |
|---|---|
| `contre-verification-pari-signe-v5.py` | `ece834a81a94dc7d6b04aa721e622c3b07a4bf4654ad1fe075c961b854b66a69` |
| `contre-verification-pari-signe-v5-sortie.json` | `285e222fed8e9770e7f8f117ce60b58ed25e01b75117c34241a7463ee9f9b5d3` |

Chacun a son compagnon `.sha256` dans le même dossier.

- **H.** Nul complet, 10 générations, cohorte de 4 fiches entrées à g = 1 et relancées, 3 nouvelles par génération,
  suite 6/(π²g²), quatre lectures (cohortes ; seule ; mixte au niveau d'entrée ; mixte au niveau courant) ; mondes A′
  (martingale ×1,5 / ×0,5, 200 puis 20 pas par génération) et S1 (pari « parts », 250 unités par génération). Plus un
  cas sous nuls partiels en lecture « cohortes » (taux de fausses découvertes de l'union).
- **P.** D-S27 : deux longueurs d'unités, nul exact du rappel par épisode ; sous-échantillon, plafond, m_max = vrai
  maximum, sans règle.
- **T.** D-S26 : famille de 5 (3 vraies à 20 points, témoin S1 avec remise, 1 nulle S1), e-BH à α, 100 / 250 / 1 000
  unités ; fréquence de promotion du témoin, taux de fausses découvertes avant et après suspension.

**Limites.** Mondes illustratifs (deux points, parts binomiales, martingale à pile ou face) ; mécanismes, pas prédiction
de la banque réelle ; rien ici n'est décisif. La lecture « seule » dépend du moment où le maximum du processus est
atteint (0,038 à 200 pas, 0,074 à 20 pas par génération) : la borne analytique m_c·α_c est ce qui compte.

Pour reproduire, depuis le dossier de mes fichiers :
```
/opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v5.py --rep 2000 > contre-verification-pari-signe-v5-sortie.json
```

## 8. Fichiers lus et empreintes SHA-256 complètes

Dossier `…/pari-de-signe/` = `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pari-de-signe/`.
Tous conformes à leurs compagnons `.sha256` (`sha256sum`, 20:35 UTC).

| fichier | SHA-256 |
|---|---|
| `…/conception-pari-de-signe-v5.md` | `95af46e4b8f317685ccc8755d6e3d0447ba109fd8771a0139eb9470c2bca8f8c` |
| `…/conception-pari-de-signe-v4.md` | `c63d8539660d265d65e9a957a07b0877a13001a48df17776d5a0151b75a35e93` |
| `…/conception-pari-de-signe-v3.md` | `1518a12f0c9b755ec6ab0f958d9c6b77f8071d7f959f6e5c5cb60de38a15db14` |
| `…/contre-lecture-v4/rapport-contre-lecture-pari-signe-v4.md` | `937994b52bb27b00aa2b580b98a36fd7e7bfffafa550e0a278634db2c97442d4` |
| `…/contre-lecture-v4/contre-verification-pari-signe-v4.py` | `981af2fb1f4b67d3de25f1bab96e81193ac00a24556aa00b57bd3f0d4aff9d61` |
| `…/contre-lecture-v4/contre-verification-pari-signe-v4-sortie.json` | `c7836e12275be249ae5ac0f622447592a9fe39e7a850005fc3a1a5ba52d79368` |
| `…/decisions-lazar-2026-10-27-v1.md` | `c2cfa1597e85431e9ab661e95fc2f94b170b3ec65744211e1e277a2aa8e2015a` |
| `…/noeuds-pour-lazar-v1.md` | `d9a6ff1b08d795456e036a20ea68752938f97c5b6b587adaf5a74b3aad3dc23a` |
| `/home/claude/controle-ia-travail/docs/decisions/decision-N-007-N-008-v1.md` (lecture seule) | `ab7dc9bb2c96704ad8fd801197de225f68d6f9720958139f4ec4e32e92105232` |
| `/home/claude/controle-ia-travail/docs/decisions/decision-N-054-v1.md` (lecture seule) | `c8a00b3f885ae3e9c4f1971dd620fbb64389a4557e6f24d3520b1c56deba4c2f` |

**Lus en plus, pour contrôler les chiffres de la v5** (section 3), conformes à leurs compagnons :
- `…/contre-lecture-v3/contre-verification-pari-signe-v3-sortie.json` (sections A, B, D) :
  `654457a88d372029a30df40cf0639521e8429b34f2aec497e191f75667205712` ;
- `…/contre-lecture-v3/complement-nuls-extremes-v3-sortie.json` :
  `082794ea56e963eeeb78b6215d7385439b3d8c25afce4dd45fee4912f2d69f3e` ;
- `…/lecture-collisionneur-v1/verification-collisionneur-pari-signe-v1-sortie.json` (section T) :
  `38efb97111c5aa7edc26e768b699107aa787b5ae0f3e6037fd67ed913f786a80` ;
- `…/simulation-batterie-v3-sortie.json` (niveaux Student sous S1 et S2) :
  `ead1b9d5be7ed789c1192c339825b2a3c1271bf3ea1ad466735d56312e2bf734`.

Heure de fin (lue sur `date -u`) : mardi 27 octobre 2026, 21:00:11 UTC.
