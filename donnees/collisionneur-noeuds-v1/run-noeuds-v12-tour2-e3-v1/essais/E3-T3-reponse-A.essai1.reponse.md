# Cellule A — tour III.3 : réponse aux critiques

**Pièces reçues.** Ma conception III.1, les critiques croisées B, C, D ; aucune n'est vide ni coupée. Rappel porté par la synthèse (VÉRIFIÉ sur le texte servi) : la pièce 20 (N9-1) était tronquée au tour 1 ; ses seuils restent SUPPOSÉ. Je ne réponds qu'aux sections qui visent A. Tout chiffre hors synthèse, question ou cellules est marqué *illustratif*. Je me sers de propositions de B, C, D en le disant (B1) ; je ne les fusionne pas.

Deux attributions de C que je ne retrouve pas dans la synthèse et que je traite comme HYPOTHÈSE de C : (i) « le statut d'opérateur et la proximité conceptuelle sont structurellement couplés par la topologie des graphes plantés (RAPPORTÉ, synthèse N1) » — la synthèse rapporte ma clause de non-réalisabilité, non un couplage établi ; (ii) « probabilité 0,25 à 0,36 à dix fiches » lue comme probabilité de repli — la synthèse donne cette fourchette comme « conclusion robuste » de la simulation de N4 sans la nommer ainsi ; je la reprends telle qu'elle est écrite.

---

## (a) Réponse critique par critique

### N1 — duel D1 (B a1, b1, c1 ; C a1, b1, c1 ; D a1, c1)

**Acceptée (B, C, D convergent) : D1 est un test de reproduction, non d'attribution.** Une seconde graine sur le même code mesure la stabilité de l'écart ; un bogue déterministe donne la même espérance sur toute graine (C : le paramètre de biais constant est non identifiable, puissance au niveau α ; recalcul conforme). Mon énoncé « H_A → le point porteur passe à VÉRIFIÉ » dépassait ce que D1 établit. Le contrôle « deux statuts à loi et chemin de code identiques » est, comme D le dit, aveugle à une erreur commune.
**Acceptée (B a1) : H_A et H_B n'étaient pas exclusives** — l'issue « même signe, amplitude très différente » n'était couverte par aucune.
**Transformée en test : D1′**, ci-dessous, avec vérité plantée et implémentation indépendante (contrôle de D) et injection de bogue déterministe (contrôle de C). Le rejeu à seconde graine est conservé comme simple **descriptif de reproduction** ; il ne change aucun statut.
**Acceptée (B b1)** : la puissance tient tant que l'erreur type reste sous ≈ 0,96 ; à 300 mondes, 0,24 à 0,49 (recalcul de B, conforme). Sans objet pour l'attribution, utile pour le descriptif.

### N1 — F′ (B a2, c2 ; C a2 ; D a2, table, c1)

**Acceptée (B) : stratifier par l'étiquette retenue conditionne sur une variable postérieure au traitement.** L'étiquette retenue est un produit du bras ; stratifier dessus peut ouvrir un biais de collision. **Acceptée (B, D) : la clause de non-réalisabilité reposait sur un jugement.**
**Rejetée en partie (C a2) : « F′ active sa clause par construction ».** C'est vrai seulement si le couplage statut/proximité est établi, ce que la synthèse n'écrit pas (voir en-tête). Mais j'accepte la conséquence conditionnelle : si le couplage est constaté, aucune épreuve hors invocation ne subsiste.
**Transformée en test : F″** — intervention définie **sur le générateur**, stratification par les variables plantées (concept rare planté, statut) qui précèdent le bras, et **test mécanique de réalisabilité** : sur les mêmes mondes, la distribution de proximité avant/après intervention est comparée à une tolérance gelée (*illustratif* : écart de moyenne ≤ une erreur type rééchantillonnée par monde). Si F″ est déclarée non réalisable par ce test, **je cède sur la divergence 1** : la seule épreuve restante est le placebo de rareté préenregistré **dans** l'invocation, sans effet rétroactif sur la porte — proposition de D, que j'adopte en le disant, et non une limite écrite seule.
**Acceptée (D, table) :** le rééchantillonnage se fait par monde, non par pont, les ponts d'un même monde étant dépendants.

### N1 — plancher d'effectif (C b3 ; D table)

**Acceptée (C) :** un plancher fixe n'est sain que si la probabilité de non-évaluabilité sous le taux planté le plus bas est elle-même bornée. **Transformée** : le plancher n_min et l'effectif M sont gelés ensemble, avec la condition écrite P(N_{s,c} < n_min | p_{s,c} = p_bas) ≤ 0,05 calculée avant tout tirage (*illustratif* : p_bas = 0,05, n_min = 5, M = 300 donnent une espérance de 15 et une probabilité de non-évaluabilité de l'ordre de 10⁻³). Sous ce calcul, « non évaluable » reste une porte fausse ; au-dessus, c'est un défaut de conception du plan, non un hasard.

### N3 — instrument (D a3 ; B c3)

**Acceptée (D) : mes deux taux étaient la précision et son complément**, dépendants de la prévalence et manipulables par le nombre de candidatures. **Corrigée** : détection = P(retenue | la paire se relie dans la fenêtre de test), fausse alerte = P(retenue | elle ne se relie pas), toutes deux à **budget de candidatures fixé par lot** (k paires, gelé), ce qui répond aussi à la critique de profusion de D sur N11.
**Transformée en test (B c3) : critère mécanique de faisabilité** avant tout essai — un script sur la moisson doit rendre, pour un échantillon gelé de paires de concepts, une date de première co-occurrence ; faisabilité = champ calculable **et** nombre de positives dans la fenêtre de test ≥ n_min gelé. C'est la pièce que je demandais pour la divergence 3 ; elle est maintenant spécifiée.

### N5 — duel D2 (B a3, b2 ; D a4, table, c3)

**Acceptée (B a3) : je n'avais nommé ni charge ni délai.** Correction : la pièce est à produire par la session qui tient l'archive scellée, avant le gel du pré-pilote (7 novembre, SUPPOSÉ) ; l'absence de pièce n'est pas une décision — le directeur tranche — mais mon avis en l'absence reste (b), pour la raison du journal écrit par le processus qui lit. **Rejetée** la qualification de « défaut de fait symétrique » : un avis motivé en cas d'absence n'est pas une règle de défaut ; il est explicitement soumis.
**Acceptée (D a4) : « H_B falsifiée → (a) tenue » dépassait le test.** Si la sortie est une fonction déterministe des comptes, l'invariance à comptes constants vérifie le schéma, pas l'innocuité. **Corrigée** : H_B falsifiée → (a) tenue **sur le canal de sortie seulement**, canal du journal non testé, ce que le rapport écrit.
**Transformée en test (B b2) :** le nombre de permutations préservant les comptes par classe est le coefficient multinomial des effectifs ; s'il est inférieur à mille, **énumération exhaustive** et test exact sur l'énumération ; sinon mille tirages. Ce nombre est calculé et écrit avant le test.
**Acceptée (D c3) :** ajout de l'artefact « sortie identique octet pour octet, lecture non journalisée changeant une décision aval », et de la vérification d'invariance des **décisions aval** sous permutation, non du seul message. Si le harnais ne détecte pas cet artefact, la conclusion est bornée à la sortie et ne vérifie pas A21 ; dans ce cas (b).

### N6 — DL-10 (B a4)

**Acceptée : mon passage de (3) à (1) n'était motivé par aucun fait nouveau** ; la prémisse était connue au tour 1. Je reviens à **(3)** : condition descriptive à 30 mondes comme épreuve de plomberie à issue attendue écrite (l'estimateur à effets fixes retrouve l'effet planté à moins d'une erreur type) ; **(1) n'est qu'un repli** si le calendrier (SUPPOSÉ) ne permet pas les 5,0 heures. La divergence 9 reste donc deux contre deux.

### N6 — DL-5 et DL-12 (D table)

**Acceptée (DL-5) :** le multiplicateur 1,4745 est conditionnel à une approximation de non-centralité qu'aucune pièce n'établit ; je le remplace par une **estimation sur monde jouet** du multiplicateur à ρ = 0,70 contre 0,85, et le chiffre 3 834 reste *illustratif*.
**Acceptée (DL-12) :** conditionner l'inclusion de la cause à « ensemble non vide » sélectionne les réussites. **Corrigé** : D3 estime **conjointement** les quatre probabilités de D, sans conditionnement (voir (b)).

### N9 — cohortes (C a3, c2 ; B b3 ; D table, c2)

**Acceptée (C) : une cohorte « non lue » sous un plancher de positives réalisées est une sélection sur l'issue** — elle censure les régimes où l'incidence s'effondre. **Transformée** : le seul plancher est l'**existence** de l'estimateur (au moins une positive et une négative, point de D, qui n'est pas une sélection puisque rien n'est calculé) ; toute cohorte estimable est rapportée avec son intervalle exact, aussi large soit-il ; le déclencheur d'audit sonne sur l'intervalle, non sur l'estimation ponctuelle.
**Acceptée (B b3) :** je ne disais pas combien de cohortes doivent être lues. Réponse : aucune — le test décisif est B-i sur l'échantillon entier ; les cohortes sont un audit et ne conditionnent pas la jugeabilité.
**Acceptée (C c2, D c2) :** contrôle par **permutation des horodatages de première liaison** dans l'ensemble à risque commun, pour la loi nulle du gradient inter-cohortes ; rééchantillonnage par **concept** et non par paire ; injection d'un concept postérieur à la coupure que la garde de C doit retirer.
**Acceptée (D) :** l'aire globale peut rester élevée alors que l'aire de première liaison est au hasard — c'est précisément la fonction du déclencheur.

### N11 — règle ordinale de transport (B b4 ; C b2, c3 ; D a5, table, c4)

**Acceptée (C) : sans bras désigné d'avance, l'événement est « un bras quelconque dernier partout » ; sous nul uniforme indépendant, P = 3 × 3⁻ᴷ = 3¹⁻ᴷ, soit 1/9 ≈ 0,111 à trois instruments** (recalcul conforme : les événements sont disjoints). **Acceptée (B) :** si le monde synthétique n'évalue que deux bras, la probabilité monte encore. **Acceptée (D) :** l'indépendance entre instruments n'est pas écrite et des instruments partageant leurs entrées peuvent concorder sur un biais commun.
**Conséquence : la règle ordinale est retirée comme critère de retrait.** Un α ≤ 0,05 exigerait K ≥ 4 instruments à trois bras (3⁻³ = 0,037) ; il y en a trois. **Transformée** : la concordance observée est rapportée avec sa probabilité exacte sous nul uniforme (borne haute de la preuve, la dépendance ne pouvant que l'affaiblir), et l'issue « transport non établi, trois bras reconduits » est l'issue préenregistrée. Sur la divergence 13, je rejoins donc le **rapport descriptif de B**, auquel j'ajoute deux choses en le disant : la probabilité nulle exacte attachée au tableau, et l'**aveuglement des étiquettes de bras** à la présentation, que C exigeait de B. **Contrôles adoptés (C, D) :** trois bras identiques en Monte Carlo (taux de « dernier partout » attendu 1/9) ; trois instruments alimentés par un même signal biaisé au classement connu.

### N11 — juge de correspondance primaire/secondaire (B a5, c4)

**Acceptée : la frontière n'était pas opérationnelle** et un secondaire sans règle d'usage coûte sans contrepartie. **Je retire le juge de la course.** Il ne subsiste qu'à l'étape d'**étalonnage des leurres avant la course** (sa précision sur leurres y est mesurée) ; aucune de ses sorties n'entre dans l'oracle ni dans un rapport de bras. Si, à l'étalonnage, il contredit l'appariement mécanique sur plus d'un taux gelé de leurres, c'est un déclencheur d'audit de la construction des leurres. Divergence 12 : je rejoins B et C.

### N11 — ponts sans fusion et bras méta (C a4)

**Acceptée : un pont planté hors du profil méta mesure le repli du bras méta et le lui attribue.** **Transformée** : les ponts construits sont étiquetés **dans/hors profil** à la construction (critère décidable sur les niches, gelé) ; le rendement du bras méta est rapporté sur deux lignes, comme l'étiquetage « profil / repli » de N4 ; s'il n'existe aucun pont plantable dans le profil, la mention « bras méta non éprouvé par ponts » est écrite d'avance. Ceci s'ajoute à l'apport A + B sur la couverture du monde, qu'il renforce : à défaut d'extension du monde **et** de pont dans le profil, le bras méta n'est jugé que sur la rétrodiction.

### N11 — profusion (D a6, b, c4)

**Acceptée.** Oracle à **budget de candidatures fixé par lot** ; bras témoins « tout rendre » et « récitation des parents seuls » ajoutés au bras fantôme et aux leurres ; un bras à sortie vide est déclaré non informatif malgré une fausse alerte nulle (point que D fait à C et que je reprends pour moi-même).

### N11 — puissance (D sur mon 0,177)

Hors section A chez D, mais le lecteur l'avait relevé : racine(0,25/8) est le maximum de l'erreur type d'un bras, non la variance du contraste. **Acceptée** : la puissance se calcule sur la loi discrète de la **différence** de deux binomiales à huit essais, à partir de l'écart type estimé (ma pièce sans dépense), le chiffre « ≈ 60 fusions » restant *illustratif*.

**Bilan :** 19 critiques acceptées, 7 transformées en test, 2 rejetées en partie (couplage structurel de C ; « défaut de fait symétrique » de B), aucune rejetée en bloc.

---

## (b) Expériences corrigées

Chaque duel oppose H_A et H_B exclusives ; chaque issue falsifie quelque chose. Processeur, 0 USD sauf mention.

**D1′ — N1, attribution définition / code.** Mondes de validation à **écart planté connu** entre statuts (nul dans une série, 2,87 dans l'autre), construits par un script court indépendant du générateur ; grandeur ancienne calculée par le code original et par une **implémentation indépendante** de la formule ; une variante du code avec **bogue injecté** (couplage altéré d'un statut rare à espérance constante) sert de contrôle positif. H_A : le code original rend l'écart planté à moins de trois erreurs types rééchantillonnées par monde dans les deux séries, et coïncide avec l'implémentation indépendante. H_B : il s'en écarte dans au moins une série. H_A falsifiée → artefact de code, l'option B de N1 tombe, le nœud revient à « corriger ». H_B falsifiée → le 2,87 est une propriété de la définition sous le générateur ; le point porteur passe d'OBSERVÉ-NON-AUDITÉ à VÉRIFIÉ, ce que D1 ne pouvait faire. Si le contrôle à bogue injecté n'est pas détecté, l'expérience est déclarée non jugeable. Le rejeu à seconde graine est rapporté à part, descriptif.

**F″ — N1, épreuve de la fuite par rareté.** Intervention sur le générateur modifiant la fréquence du statut rare à vérité fixe ; stratification par concept planté et statut ; test mécanique de réalisabilité (distribution de proximité avant/après dans la tolérance gelée) ; rééchantillonnage par monde. H_A : à proximité invariante, le gain d'un bras ne dépend pas de la fréquence du statut. H_B : il en dépend. H_A falsifiée → fuite de rareté réelle, déclencheur d'audit préenregistré. H_B falsifiée → la limite écrite sur la rareté est fermée. Si le test de réalisabilité échoue, F″ est abandonnée et le **placebo de D dans l'invocation** la remplace, sans effet rétroactif sur la porte.

**N3 — essai du substitut.** Étape 0, faisabilité : script rendant une date de première co-occurrence pour un échantillon gelé de paires ; H_A : champ calculable et positives dans la fenêtre ≥ n_min ; H_B : non. H_B → essai non réalisable, bras « non produit » sans arrêt, divergence 3 tranchée contre C. Étape 1, à budget k par lot : H_A : rappel du substitut sur les paires qui se relient supérieur, à gain minimal gelé, au score popularité × ancienneté, à fausse alerte égale ; H_B : non. H_A falsifiée → bras exploratoire, exclu de la comparaison des bras ; H_B falsifiée → bras admis sous le nom « substitut ».

**D2′ — N5, invariance.** Nombre de permutations préservant les comptes calculé d'avance (énumération si < 1 000) ; invariance exigée du message, de l'ordre des appels **et des décisions aval** ; artefacts : liste triée par classe, lecture hors journal, lecture non journalisée changeant une décision aval ; contrôle positif : version antérieure. H_A : zéro différence sur toute l'énumération, tous les artefacts détectés. H_B : au moins une différence ou un artefact non détecté. H_A falsifiée → (b). H_B falsifiée → (a) tenue **sur le canal de sortie et l'aval testés**, canal du journal non couvert, écrit en limite. Charge : session de l'archive ; délai : avant le gel du pré-pilote (SUPPOSÉ).

**D3′ — N6 DL-12.** Monde jouet simulant la méthode de prédiction invariante (le jouet servi ne l'a pas fait), sous centrage par strate et sans centrage ; quatre probabilités estimées **conjointement et sans conditionnement** : ensemble non vide **et** cause incluse ; leurre inclus ; jumeau inclus ; abstention sous confusion cachée. H_A : P(non vide ∧ cause) ≥ puissance gelée et P(leurre) ≤ seuil gelé sous centrage. H_B : non. H_A falsifiée → méthode en descriptif avec limite ou méthode nouvelle préenregistrée. H_B falsifiée → option (1) tenue. Contrôle : monde sans cause → abstention. La comparaison centré/non centré attribue un échec au centrage plutôt qu'à la méthode.

**N9 — aire par cohorte.** Cohortes de première liaison sur l'ensemble à risque commun ; estimateur rapporté dès qu'il existe (≥ 1 positive et 1 négative), avec intervalle par rééchantillonnage **par concept** ; nulle par permutation des horodatages dans l'ensemble à risque ; injection d'un concept postérieur à la coupure. H_A : le gradient inter-cohortes observé est dans la loi permutée et le concept injecté est retiré par la garde. H_B : gradient hors loi ou concept non retiré. H_A falsifiée → fuite temporelle, audit. H_B falsifiée → la fenêtre (a) est jugée sans fuite détectable par cet instrument. B-i ≥ 0,85 reste seul décisif.

**N11 — oracle et transport.** Oracle mécanique à deux identifiants parents, budget de candidatures k par lot, ponts étiquetés dans/hors profil, permutation par lots entiers ; témoins : bras fantôme, « tout rendre », « récitation seule », quatre familles de leurres, contrôle de plantation de B. H_A : le bras rend plus de ponts plantés que le bras fantôme à k fixé, à fausse alerte sur leurres sous le seuil gelé. H_B : non. H_A falsifiée → bras non informatif sur ponts ; H_B falsifiée → rendement sur ponts admis au rapport. Transport : tableau des trois classements à étiquettes aveuglées, probabilité exacte sous nul uniforme jointe (1/9 pour « dernier partout » à K = 3), **aucun retrait** sur transport, issue préenregistrée. Puissance du contraste synthétique : loi discrète de la différence à huit essais, écart type estimé.

---

## (c) Réponse à l'arbitre

**Ce qui est établi (sur la synthèse et la question v12).** Seule la redéfinition passe en N1, et l'ancienne grandeur rapportée sans seuil ne garde plus rien ; mais l'attribution de l'échec à la définition reste **OBSERVÉ-NON-AUDITÉ**, et l'annexe la traite comme acquise. À huit fusions par bras, aucun retrait n'est décidable (quatre calculs, hypothèses d'effet différentes, même conclusion). Toute règle de transport ordinale à trois instruments a une valeur p minimale de 1/9 : **non jugeable**, et je retire la mienne. Un oracle de ponts plantés doit être mécanique à deux parents, à budget de candidatures fixé, et distinguer profil et repli du bras méta. (b) en N9 conditionne sur l'issue ; (a) tient sous troncature stricte, garde de première arête et audit par cohorte sans censure sur les positives réalisées. (b) en N10 tient, mes conditions étant légères. En N5, les quatre tiennent la même pièce ; elle n'est pas produite.

**Ce qui ne l'est pas.** L'origine du 2,87 (D1′ tranche, D1 ne le pouvait pas). La réalisabilité d'une épreuve de rareté hors invocation (F″ le dit mécaniquement ; sinon, je cède à D). La faisabilité de l'essai du substitut sur la moisson (script de faisabilité). L'innocuité de (a) en N5 hors du canal de sortie : D2′ borne sa conclusion, le journal reste hors test, ce qui fonde mon avis (b) à défaut de pièce. Le multiplicateur de DL-5 (jouet, non formule). Le comportement de la méthode de prédiction invariante sous centrage (D3′). Les dates, heures et calendriers : SUPPOSÉ.

**Changements d'avis par rapport au tour III.1 :** DL-10 revient à (3) (B avait raison : aucun fait nouveau) ; N11 : règle ordinale retirée, juge retiré de la course, ponts étiquetés dans/hors profil ; N9 : plancher de positives remplacé par la seule existence de l'estimateur ; N1 : divergence 1 cédée sous condition de non-réalisabilité de F″ ; N5 : verdict « indécidable sans la pièce » maintenu, charge et délai nommés, conclusion bornée au canal testé.

**Verdicts sur l'annexe, résumés :** N1 tenue sous condition (D1′, F″, plancher gelé avec M) ; N3 tenue sous condition (faisabilité puis rappel à budget fixe) ; N4 tenue sous condition, CA1-04 au directeur ; N5 indécidable sans D2′, avis (b) à défaut ; N6 : DL-3 renversée → (2) + déclencheur, DL-9 renversée → (2), DL-10 (1) renversée → (3) sauf calendrier, DL-12 indécidable sans D3′, DL-5/6/8/13 sous condition, les autres tenues ; N9 tenue sous condition ; N10 tenue ; N11 session-depot tenue sous condition (oracle corrigé, aucun retrait sur transport), conv-audit renversée sur (c) et tenue sur la couverture du monde — décision du directeur requise sur l'extension du monde.

**Expérience à faire en premier : D1′**, parce qu'elle coûte 0 USD, se joue sur processeur en parallèle de D2′, et que son issue H_A-falsifiée fait tomber la recommandation de N1 que l'annexe tient pour acquise et dont dépendent N11 puis la version nouvelle de la bisociation. **En parallèle, D2′** (N5), seule pièce commune aux quatre sur le chemin critique du pré-pilote. Ordre pour le directeur, inchangé depuis III.1 : décision de couverture du monde (N11), N1, N4 et N5, N6 (DL-12, DL-5), N3 et N9, N10 après le pilote.

FIN-DE-CELLULE