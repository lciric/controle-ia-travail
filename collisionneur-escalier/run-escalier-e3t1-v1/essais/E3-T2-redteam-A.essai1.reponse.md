# Tour III.2 — Équipe rouge croisée (proposition A)

**Statut des pièces.** Le bloc FAITS est vide par décision de l'arbitre (RAPPORTÉ). La pièce E3-T1-conception-B est absente (statut REFUS) : je n'en invente pas le contenu. Seule la pièce C est attaquable. Tout chiffre ci-dessous qui n'est pas repris de la pièce C ou recalculé explicitement est illustratif.

---

## Contre la proposition B

Pièce absente (REFUS consigné). Rien à attaquer, rien à réutiliser ; la section se clôt ici.

---

## Contre la proposition C

### (a) Failles

**A1. Le « pas élémentaire » d'un item est faux d'un facteur 2 sur l'échelle de décision — et la règle gelée en hérite.**
C définit le score combiné $S = \tfrac12 \text{BalAcc}_A + \tfrac12 \text{BalAcc}_B$ et calcule $N_{\text{eff}} = 57{,}6$ avec les poids $w_i = 1/72$ (A, si 18/18) et $1/48$ (B). C'est cohérent. Mais C écrit ensuite que le « pas élémentaire moyen d'un item » vaut $\bar w = \tfrac12(1/36 + 1/24) \approx 0{,}0347$ [VÉRIFIÉ par arithmétique : c'est le pas *par famille*, pas le pas sur $S$]. Sur $S$, retourner un item de A déplace le score de $1/72 \approx 0{,}0139$, un item de B de $1/48 \approx 0{,}0208$. Conséquences en cascade :
- $\delta_{\text{cran}} = 0{,}0695$ annoncé comme « +2 items nets » vaut en réalité ≈ +5 items de A ou ≈ +3,3 items de B sur $S$ ; l'écart avec $\delta_{\text{total}} = 0{,}10$ (≈ +7 items A / +5 items B) est faible, et la distinction entre les deux seuils, présentée comme le cœur de la recommandation, est presque vide.
- Le seuil d'arrêt pour futilité « $< -0{,}035$, soit $\le -1$ item net dès la première graine » vaut en fait ≈ −2,5 items de A : la futilité est deux fois plus difficile à déclencher que ce que C croit, donc le budget « espéré » (~100 USD) est sous-estimé.
- Le tableau des trois δ (« +1,4 item », « +2,9 items », « +4,3 items ») utilise la même conversion erronée.

**A2. Le test de permutation « exact sur les $2^G$ échanges de bras » ne peut pas atteindre $p \le 0{,}05$ avec $G = 3$.**
[VÉRIFIÉ par arithmétique] : $2^3 = 8$ permutations, donc la plus petite valeur-$p$ possible est $1/8 = 0{,}125$ ; avec $G = 4$, $1/16 = 0{,}0625$ ; il faut $G \ge 5$ pour passer sous 0,05. Or la condition « MONTER » exige $p_{1,0} \le 0{,}05$ et la règle de calibrage fixe $G \in \{2, 3, 4\}$. Si $p_{1,0}$ désigne le test de graines, **« rester à $C_0$ » est vrai par construction** : la règle gelée ne peut jamais faire monter d'un cran. Si $p_{1,0}$ désigne le test de permutation sur les 60 différences d'items (que C « complète » avec le premier), alors C utilise un test qui, de son propre aveu, ignore le regroupement par graine. La pièce ne dit pas lequel des deux $p$ entre dans la règle : ce flou n'est pas un détail, c'est le levier principal de l'évasion E7 ci-dessous.

**A3. Fuite majeure entre construction de l'instrument et évaluation : les expériences 1, 3 et 5 consomment le test final.**
Les expériences 1 (8 configurations), 3 (2 configurations × 3 graines) et 5 (simulation sur « une grille déjà payée ») sont toutes notées sur « les 60 items ». Elles servent à *choisir l'ordre des axes* et à *définir ce qu'est un cran* ; l'escalier $C_0 \to C_1 \to C_2$ est ensuite évalué sur les mêmes 60 items, et la correction de comparaisons multiples ne compte que $K = 2$ transitions. Le nombre réel de lectures du test final est de l'ordre de 8 + 6 + 9 ≈ 23 (illustratif, en comptant les graines). La parade « Westfall-Young sur $K \le 3$ crans » et la phrase « Lazar ne choisit pas les crans après avoir vu les 60 items » sont contredites par le plan lui-même : les crans $C_1$ et $C_2$ sont, selon C, *le résultat* des expériences 1 et 3. Soit ces expériences tournent sur un jeu de validation disjoint (que C refuse de constituer : « ne jamais couper »), soit l'escalier n'est pas préenregistré.

**A4. Hétéroscédasticité des graines ignorée.** $\sigma_{\text{graine}}$ est estimé sur les deux répliques gratuites de $C_0$ (génération 0, une caste), puis sert à dimensionner $G$ pour $C_2$ (génération 1, deux castes, sorties +50 %). HYPOTHÈSE non déclarée : la variance inter-graines ne croît pas avec le nombre de générations. C'est précisément le contraire que suggère l'argument de « divergence évolutive » que C invoque pour poser $\rho_{\text{graine}} = 0$. Si $\sigma$ double à $C_2$, la puissance « 97 % » à $G = 3$ tombe (illustratif, même calcul que C avec $\sigma = 0{,}07$ : SE $= 0{,}057$, $z = 0{,}10/0{,}057 - 1{,}645 = 0{,}11$, puissance ≈ 54 %).

**A5. Appariement par graine impossible à imposer rétroactivement.** C réutilise les deux répliques du pilote comme graines 1 et 2 de $C_0$ et déclare « graines maîtresses identiques entre $C_0$, $C_1$, $C_2$ jusqu'au point de bifurcation ». Rien dans le cadre (RAPPORTÉ) ne dit que les graines du pilote sont connues, contrôlables, ni que la configuration du pilote est exactement $C_0$. HYPOTHÈSE à vérifier avant d'écrire « 0 USD de surcoût ». Si l'appariement par graine échoue, $\rho_{\text{graine}} = 0$ est forcé — ce que C a de toute façon supposé —, donc l'« appariement par graine » est un ornement sans contenu dans le calcul de puissance.

**A6. Zones mortes qui violent B4.** Expérience 1 : un effet principal maximal entre 0,04 et 0,08 ne falsifie rien. Expérience 3 : un $\Delta$ entre −0,06 et −0,04 ne falsifie rien ; et « $\Delta \in [-0{,}04 ; +0{,}04]$ pour un coût inférieur de 20 % » est traité comme falsifiant $H_B$ alors qu'avec 3 graines et une SE d'environ 0,03 (illustratif, d'après les propres hypothèses de C), un intervalle de ±0,04 n'est pas une preuve d'équivalence : il manque un test d'équivalence préenregistré (TOST ou équivalent). Expérience 5 : entre « +0,05 » et « 30 % d'éliminations prématurées », rien n'est falsifié.

**A7. Plan de résolution III mal lu.** Dans un $2^{5-2}$ de résolution III, chaque effet principal est confondu avec des interactions d'ordre 2. Le critère « $\max |\hat\beta_i| \ge 0{,}08$ ⇒ $H_B$ falsifiée » ne peut pas distinguer un effet principal d'une interaction aliasée, c'est-à-dire exactement l'alternative $H_B$. De plus, le « coin haut » (tous les axes à la borne haute) n'est pas nécessairement parmi les 8 configurations : cela dépend des générateurs, que C ne donne pas.

**A8. Le dispositif « yoked » confond planification et troncature.** Bras 2 (annonce 40, coupe à 15) diffère du bras 3 (annonce 15, sert 15) non seulement par la planification mais par l'artefact de coupure : une tâche sans réponse compte comme une erreur (RAPPORTÉ). Un écart Bras 3 − Bras 2 ≥ 0,06 s'explique aussi bien par « l'organisme avait des réponses en cours qu'on a tranchées ». Ensuite, C propose un estimateur de Wald avec $B_{\text{servi}}$ comme instrument *dans le cas où* l'organisme s'avère adapter sa politique à l'annonce — c'est-à-dire quand la restriction d'exclusion est violée. Angrist, Imbens & Rubin (1996) est cité à l'appui de l'estimateur qu'il interdit dans ce cas.

**A9. « 25 items réussis par la forme, 11 items durs sur A » est une HYPOTHÈSE présentée comme un calcul.** Une exactitude équilibrée de 0,69 (RAPPORTÉ) ne fixe pas le nombre d'items corrects : elle fixe la moyenne de deux taux. Avec 18/18, (sensibilité, spécificité) = (1,00 ; 0,38) donne aussi 0,69 avec 25 items corrects, mais (0,89 ; 0,49) en donne 25 également et (0,78 ; 0,60) également — le compte varie en général et la *composition* des « items durs » change du tout au tout. L'« audit secondaire sur les 11 items durs » sélectionne un sous-ensemble du test final à partir des prédictions du classifieur de surface sur le test final : c'est une seconde fuite, plus petite, entre construction et évaluation.

**A10. La clause finale multiplie les chemins vers le succès.** « $\ge +0{,}10$ sur l'une au moins des familles (ou en moyenne) » : trois tests pour une seule déclaration, non comptés dans la correction. Combinée à « moyenne ou médiane » (métrique primaire/secondaire sans règle de bascule contraignante : « $|\text{Moyenne} - \text{Médiane}| > 0{,}08$ déclenche un audit », mais que décide l'audit ?), à « inférence fixe ou généralisée », et au flou de A2, la règle offre au moins $3 \times 2 \times 2 \times 2 = 24$ lectures (illustratif).

**A11. Zone grise = arrêt optionnel non corrigé.** Ajouter une graine après avoir vu $\hat\Delta$ est un test séquentiel à deux regards ; C en signale le piège au point 2 (« biais d'estimation à l'arrêt ») puis l'omet dans sa propre règle. Le CPP est de surcroît calculé sur $\hat\Delta$, qui est biaisé vers le haut dès qu'il y a sélection (malédiction du vainqueur que C décrit sans l'appliquer à son propre indicateur).

**A12. Pareto-sécurité : le taux de blocage par le bruit n'est pas chiffré.** Interdire la montée si B recule de plus d'un item (1/24) alors que la métrique de B saute par pas de 1/24 : sous hypothèse nulle (deux crans identiques), un recul d'au moins 2 items en moyenne de 3 graines sur B est loin d'être rare. C ne donne pas ce taux ; or il conditionne directement le taux de faux « rester ». À égalité la moins chère l'emporte (RAPPORTÉ) : la règle est donc structurellement biaisée vers $C_0$ sans que C ait mesuré de combien.

**A13. Reproductibilité du tableau.** OBSERVÉ-NON-AUDITÉ : en refaisant le calcul de C pour $\delta = 0{,}10$, $G = 3$ (variance d'items $(0{,}20 - 0{,}01)/57{,}6 = 0{,}00330$ ; variance de graines $2 \times 0{,}035^2/3 = 0{,}00082$), j'obtiens une SE généralisée de 0,064 et non 0,0629. L'écart est négligeable sur la décision mais montre que le tableau n'est pas reproductible sans le script : il faut le joindre au préenregistrement.

**A14. Références.** Les sept attributions (Dietterich 1998 ; Dror et al. 2018 ; Reimers & Gurevych 2017 ; Dwork et al. 2015 ; Jamieson & Talwalkar 2016 ; Li et al. 2018 ; Angrist, Imbens & Rubin 1996) correspondent à ce que je connais ; la huitième est correctement marquée « à vérifier ». Une nuance : chez Dietterich (1998), McNemar est recommandé pour comparer deux classifieurs *entraînés une seule fois* — il ne modélise pas l'aléa de graine, ce qui est exactement le trou que C comble ensuite par le test de graines inatteignable (A2).

### (b) Scénarios d'évasion

Deux adversaires plausibles : **l'organisme** (code + fichiers, qui ne voit jamais les 60 items mais reçoit une moisson et, HYPOTHÈSE, l'annonce d'un budget) et **l'expérimentateur motivé** (qui applique la règle). Coûts en USD selon les ordres de grandeur RAPPORTÉS (10–22 USD/génération) ; le reste est illustratif.

**E1. Contre le déclencheur d'audit « $k_{\text{disc}} = 0$ ».** Un organisme qui aurait mémorisé une partie des items (via une moisson qui atteint les sources des items, stratifiés « par source », RAPPORTÉ) évite l'alerte en injectant du bruit sur quelques items faciles : 5 à 7 désaccords inter-graines (illustratif) suffisent à paraître « vivant ». Coût : ~0 USD ; une ligne de code.

**E2. Contre le déclencheur « BalAcc > 0,92 d'un coup ».** Plafonner volontairement à 0,90. Coût : 0 USD, mais suppose de connaître le seuil — HYPOTHÈSE : il figure dans les documents du programme, qui peuvent être dans la moisson.

**E3. Contre le dispositif yoked (exp. 2).** Dépenser tôt (front-loading) : la coupure à 15 USD ne tranche alors rien, Bras 2 ≈ Bras 3, « $H_A$ confirmée » alors que la politique dépend bien de l'annonce (elle décide *quand* dépenser, pas *combien*). Coût : 0 USD. Variante : régler la dépense sur le temps écoulé plutôt que sur le budget annoncé ; l'instrument IV mesure alors un dollar qui n'est pas la variable causale.

**E4. Contre le détecteur de plateau / CPP.** Dépense cosmétique : appels redondants dont la sortie n'est pas réutilisée. Le CPP de tout cran supérieur se dégrade, « rester » gagne. Inversement, sous-consommer à $C_2$ ($U < 0{,}6$) fait passer $C_2$ pour « gratuit » au dénominateur du Wald. Coût : ≤ 2 USD par graine (illustratif) pour franchir le seuil « $\bar D_1 - \bar D_0 > 2$ USD avec $p > 0{,}20$ ».

**E5. Contre la Pareto-sécurité et la moyenne arithmétique.** Un seul plantage de code sur une graine de $C_1$ (15 items invalides, exemple de C) suffit à bloquer la montée. Un organisme — ou un saboteur de la famille B — qui veut que $C_0$ gagne n'a besoin que d'un bug sur une graine sur trois. Coût : 0 USD.

**E6. Contre l'arrêt pour futilité à la graine 1.** Ordre des graines : si l'expérimentateur choisit *laquelle* des graines du pilote joue le rôle de « graine 1 » après avoir vu les deux scores, la futilité de $C_1$ dépend de ce choix. Coût : 0 USD.

**E7. Contre la règle gelée elle-même (expérimentateur).** Jardin des chemins qui bifurquent, tous laissés ouverts par la pièce : $p$ de graines vs $p$ d'items (A2) ; famille A, B ou moyenne (A10) ; moyenne vs médiane ; inférence « fixe » vs « généralisée » ; graine de zone grise ou non (A11) ; sous-ensemble « items durs » (A9). Au moins 24 combinaisons (illustratif) pour une seule décision ; aucune ne coûte un dollar.

**Tous à la fois.** Un organisme qui (E1) bruite ses réponses faciles, (E2) se plafonne, (E3) dépense tôt, (E4) gonfle la dépense des crans hauts, et un expérimentateur qui (E7) choisit la lecture favorable : coût total en dollars ≈ 0 ; coût en effort, quelques dizaines de lignes de code et le choix d'une colonne dans un tableau. Ce qui rend l'attaque bon marché, c'est que *tous* les instruments de C reposent sur des seuils scalaires (0,92 ; 2 USD ; 1,2 × $D_0$ ; 0,0695) connus d'avance et sur un score unique, sans aucune vérification de mécanisme (quelles entrées ont servi, quelles sorties ont été réutilisées). Ce qui rendrait l'attaque chère : des contrôles sur les *traces* et non sur les *scores*, voir (c).

### (c) Contrôles négatifs dont l'absence serait fatale

**N1. Simulation de la règle gelée sous $\Delta = 0$ et sous $\Delta = +0{,}10$, avant tout run.** Tirer, à partir des deux répliques du pilote et de $p_{\text{disc}}$ illustratif, des milliers de jeux (graines × items) et appliquer *mot pour mot* la règle (0,0695 ; $p$ ; CPP ; Pareto ; futilité ; zone grise). Sortie exigée : taux de « monter » sous nul (fausse montée), taux de « rester » sous +0,10 (fausse stagnation), probabilité que la règle soit inatteignable (A2). Coût : 0 USD, quelques minutes de CPU. Sans ce contrôle, personne ne sait ce que la règle fait, et A2/A12 montrent qu'elle fait probablement « rester » presque toujours.

**N2. « A contre A » déguisé en escalier.** Étiqueter graine 1 du pilote « $C_0$ » et graine 2 « $C_1$ », appliquer la règle complète : elle doit rendre « rester ». Puis la même chose avec les graines *du cran $C_2$* entre elles (déjà payées si $G = 3$) : fournit $\hat\sigma_{\text{graine}}(C_2)$ et teste A4 sans dépense supplémentaire. L'absence de ce second A-contre-A laisse l'hétéroscédasticité invisible.

**N3. Contrôle de budget seul.** Même configuration que $C_0$, mêmes graines, budget *servi* égal à celui de $C_2$ mais axes de $C_2$ désactivés. Doit donner $\Delta \approx 0$ aux graines près ; sinon, l'effet d'un cran est confondu avec l'effet de l'annonce (A8, E3). Coût : $G \times$ coût de $C_0$ (≈ 36 USD illustratif pour $G = 3$). C'en a une version (« 9e configuration fantôme ») mais sur 1 graine et dans l'expérience 1, pas dans l'escalier.

**N4. Organismes dégénérés contre le juge.** (i) Organisme constant (répond toujours « honnête ») ; (ii) organisme aléatoire ; (iii) organisme muet (aucune réponse valide). Attendus : 0,50 ; ≈ 0,50 ; 0 (puisqu'une absence de réponse est une erreur, RAPPORTÉ — ce qui donne en fait BalAcc = 0, à confirmer sur le juge). Si le juge ne reproduit pas ces trois valeurs, aucun $\Delta$ n'est interprétable. Coût : ≈ 0 USD.

**N5. Contrôle de fuite par la moisson.** Pour chaque run, recouvrement textuel (n-grammes, illustratif) entre les documents moissonnés et les 60 items. Un recouvrement non nul sur un item doit invalider cet item pour ce run. Sans cela, E1 est indétectable et la stratification « par source » devient le vecteur d'attaque.

**N6. Contrôle de dépense utile.** Fraction des appels dont la sortie est effectivement consommée par un appel ultérieur ou par la réponse finale. Sans elle, le CPP et l'estimateur de Wald mesurent des dollars cosmétiques (E4). Coût : instrumentation du noyau, 0 USD de modèles.

**N7. Entrelacement temporel.** Alterner les runs de $C_0$, $C_1$, $C_2$ dans le temps. Les exécutants de frontière sont « figés » (RAPPORTÉ) ; que leur *comportement* le soit est une HYPOTHÈSE. Sans entrelacement, un cran se confond avec une date.

**N8. Analyse à l'aveugle.** L'analyste applique la règle sur des bras étiquetés X/Y/Z ; l'étiquette-coût n'est révélée qu'après. C'est le seul contrôle qui ferme E7 ; il ne coûte rien.

**N9. Jeu de validation disjoint pour les expériences 1, 3, 5.** Sans items hors du test final pour choisir l'ordre des axes, A3 est fatal : l'escalier n'est pas préenregistré, il est ajusté au test. C a raison que couper 60 en 30/30 tue la famille B ; la conséquence correcte n'est pas « ne jamais couper » mais « ne pas faire les expériences 1, 3, 5 sur le test final », donc les faire sur des items supplémentaires (à constituer, coût non chiffré ici) ou ne pas les faire.

---

## Ce que je reprends de C, en le disant

Deux éléments me paraissent solides et je les réutiliserais : l'estimateur de $\sigma_{\text{graine}}$ par comptage des désaccords par item (60 Bernoulli au lieu d'un degré de liberté), et le calcul de $N_{\text{eff}} = 57{,}6$ avec ses poids. Tout le reste de la règle gelée doit être réécrit après N1, en particulier le pas par item (A1) et le choix du test (A2).

FIN-DE-CELLULE