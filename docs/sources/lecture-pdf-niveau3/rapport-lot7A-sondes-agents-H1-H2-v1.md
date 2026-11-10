# Rapport de lecture — lot 7-A : sondes sur des agents (H1, H2, H8, Tr, HC3) — v1

Lecteur neuf, niveau 3 de l'état de l'art. Écrit le 10 novembre 2026 ; heure relevée par `date -u` : 11:07 UTC.
Trois PDF lus en entier sur source (annexes comprises), page par page, par `pdftotext` (pages numérotées selon le fichier).
Énoncés jugés : H1 (programme v2, section 5), H2 (énoncé retenu, décision N-007), bases boîte blanche de N-056 (cascade, dernier état), H8, Tr, HC3 (énoncé de N-013).
Citations contrôlées par script : **73 ; échecs : 0** (annexe A ; les renvois [F…], [R…], [A…] du texte y pointent).
Nature des chiffres : « auteurs » = imprimé dans le PDF ; « calcul » = recalculé par moi.

## En tête : ce qu'il faut voir d'abord

1. **Aucun des trois articles n'occupe H1 ni H2.** Aucun ne traite un sabotage diffus : dans les trois, l'objet détecté est **un acte unique** (une action critique non autorisée ; un appel qui divulgue un secret ; un rapport final mensonger). Aucun n'accumule des scores de sonde le long de la trajectoire ; aucun ne donne de garantie de faux positifs ; aucun n'a d'adversaire adaptatif.
2. **Occupation partielle, en lecture dure seulement — H8, par Fayyazi et collègues (2610.17301).** L'article identifie ce que lit sa sonde (« la croyance que l'action n'est pas autorisée », pas la provenance de l'ordre) et en tire un échec prédit puis observé sous une attaque par contenu : face à une injection signée du nom de l'utilisateur, la sonde figée se tait et note même les appels injectés plus bas que les appels bénins (0,28 et 0,23 d'aire sous la courbe, auteurs, p. 37) [F23, F24, F25, F29]. C'est un lien « construit → robustesse » sur un cas, après coup pour l'injection, sur un axe autre que « intention contre conscience d'évaluation », sans attaquant adaptatif. Je retiens **« voisin fort »** ; la lecture dure « occupe en partie » est défendable et doit être tranchée par la mère.
3. **Forme de la comparaison de H1 déjà faite sur action unique (non revendiquée seule).** Fayyazi et collègues comparent, sur l'agent qui agit, une lecture linéaire des activations à des moniteurs boîte noire au même taux de fausses alertes (10 %), tests préenregistrés. Le programme dit déjà que « le gain blanc-sur-noir en général est établi » ; la pièce revendiquée (diffus, tâches floues) n'est pas touchée.
4. **Deux contre-indices convergents pour H1, à verser au dossier** : dès qu'un classifieur de texte **entraîné** (sac de mots, TF-IDF) lit le même préfixe, l'avantage des activations disparaît ou devient minime.
   - Fayyazi : à la décision, sonde 0,941 contre texte supervisé 0,934 et moniteur de chaîne de pensée 0,944 ; les comparaisons préenregistrées « tous négatifs » échouent ; le verrou sur moniteur de chaîne de pensée, au même taux de fausses alertes, empêche autant de violations (16 contre 20 sites discordants, p = 0,80) [F6, F9, F12, F15, F20].
   - Raghav : sonde 0,98 contre sac de mots 0,96 en épreuve (écart +0,02, intervalle −0,01 à +0,05) ; l'auteur conclut que le gain vient de l'entraînement sur étiquettes, pas des activations [R1, R10, R11, R29].
   - Le titre rapporté de Fayyazi (« bat les moniteurs de chaîne de pensée ») ne vaut que pour **la prévision du mensonge** quand on demande à l'agent de taire les permissions dans son raisonnement (+0,16 [0,01 ; 0,28], p = 0,02), **pas** pour le verrou sur la violation [F1, F28].
5. **Risque de collision à surveiller pour H2** : Fayyazi et collègues reconnaissent l'absence de garantie sur les fausses alertes et annoncent les seuils conformes sur lectures internes comme « prochaine étape naturelle » ; les mêmes auteurs publient déjà sur les seuils conformes [F14, F16]. Rien n'est fait dans cette version.
6. **Résultats utiles au préenregistrement de G1** (aucun ne change un énoncé) : seuil par appel à 5 % ⇒ 59 % des épisodes bénins alarmés ; seuil par épisode réglé sur les épisodes d'entraînement ⇒ 29 % au lieu de 5 % ; cascade « sonde puis second contrôle sur la même entrée » sans gain (Raghav) ; aire sous la courbe de 0,979 mais 18,9 % de rappel à 1 % de fausses alertes par tour (AgentDecept) [R13, R15, R16, A12].
7. **Aucun refus** de contrôle de permissions ni de classifieur pendant ce travail.

## Empreintes des PDF (vérifiées contre les compagnons `.sha256`, identiques)

| PDF | sha256 | pages |
|---|---|---|
| `2610.17301v1.pdf` | `76836d976510b0baf9f43f0743fefb10ac287021e2adf75b75d933c14ef7da44` | 42 |
| `2610.40588v1.pdf` | `b728c28d2ee42f735a90e851fb3070fc0499358012bd84a53ccedb7703fd4570` | 49 |
| `2610.39377v1.pdf` | `60813ba201210b269dc2ea72f220466bcf4988d44404386b40239b78a6b164d1` | 33 |

## Réponses aux cinq questions de la consigne

| Question | 2610.17301 (Fayyazi et collègues) | 2610.40588 (Raghav) | 2610.39377 (AgentDecept) |
|---|---|---|---|
| Sabotage diffus ou action unique ? | **Action unique** : une action critique dont un seul fait décide si elle est autorisée ; étiquette donnée par l'environnement [F3] | **Action unique** : l'appel dont la sortie contient le secret (chaîne exacte) ; la pression s'étale sur 20 tours au plus, l'acte non [R6] | **Événement unique** : un rapport trompeur à l'utilisateur, jugé sur la trajectoire entière ; pas de sabotage [A3] |
| Sonde par action ou agrégée sur la trajectoire ? | **Par action** : état lu avant l'appel d'outil ; jetons mis en commun par **moyenne** des 8 derniers ; score = moyenne de lectures centrées-réduites sur 5 profondeurs et 2 plis. Sur l'épisode : « alarme à chaque action », sans statistique de trajectoire [F11] | **Par appel** : dernier jeton de l'entrée ; sonde de raisonnement = **maximum** sur les jetons (la moyenne fait mieux : 0,98 contre 0,93). Sur l'épisode : « au moins une alarme » (maximum implicite) [R21, R22, R13] | **Maximum** des scores de jetons sur toute la trajectoire, soit un score par trajectoire [A7] |
| Somme cumulée, test séquentiel, garantie ? | **Non.** Seuil = 90ᵉ centile empirique sur actions critiques autorisées ; aucune garantie, dit en limite [F4, F14] | **Non.** Seuil = 5 % des appels de contrôle ; seuil par épisode choisi sur l'épreuve « pour montrer le compromis » [R7, R14] | **Non.** Seuils à 1, 2 et 5 % de fausses alertes **par tour neutre**, rappel **par trajectoire** [A10] |
| Moniteur boîte noire à faux positifs égaux ? | **Oui**, à 10 % (et 5 % en descriptif) : moniteur de chaîne de pensée et moniteur d'actions à zéro exemple, plus texte supervisé. Jamais à 1 % [F5, F9, F18] | **Oui**, à environ 5 % : moniteur à zéro exemple réglé pour ne pas signaler plus que la sonde (82 % contre 26 % des appels fautifs) [R3] | **Non** : aucun moniteur boîte noire, aucune base |
| Adversaire adaptatif ? | **Non** : seulement une consigne de taire les permissions ; dit en limite [F13, F17] | **Non** ; l'auteur nomme l'attaque « étaler la pression sur plusieurs appels » sans la tester [R26, R27] | **Non** |
| Base « traits du texte » (sac de mots) ? | **Oui** : TF-IDF supervisé sur le même préfixe ; il égale la sonde à la décision et la bat contre le jumeau autorisé [F5, F7, F20] | **Oui** : TF-IDF et régression logistique, mêmes appels, plis et poids ; proche de la sonde [R8, R10] | **Non** |
| La sonde lit-elle l'agent qui agit ? | Oui (son propre état, rejoué en forçage du professeur) ; un bras « lecteur » (Qwen lit gpt-oss) existe | Oui (requêtes rejouées dans les poids ouverts) | **Non** : un autre modèle (GLM-4.7-Flash) relit les transcriptions de Gemini [A4, A15] |

## 1. 2610.17301v1 — Fayyazi, Kamal, Pedram, « The Agent Knew… » (priorité absolue)

**Venue imprimée** : aucune ; « Preprint. October 14, 2026 » en pied de page, timbre arXiv du 12 octobre 2026 [F2] (écart de deux jours, sans conséquence).

**Ce qu'il fait.**
- Banc CAPE-Bench : 24 gabarits de tâches, 8 familles de sécurité, outils factices ; chaque tâche existe en deux mondes qui diffèrent d'un fait (action critique autorisée ou non). Quatre modèles à poids ouverts (Qwen3.8-27B, Muse-Glimmer-30B, Gemma-4-26B-A4B, gpt-oss-20b).
- Lecture linéaire (analyse discriminante linéaire régularisée) du flux résiduel, à trois moments : juste après la révélation du fait, juste avant l'appel d'outil, juste avant le rapport. Négatifs durs : la même action dans le monde autorisé.
- Bases de texte au même préfixe : classifieur TF-IDF supervisé ; moniteurs à zéro exemple lisant la chaîne de pensée ou les seules actions [F5].
- Mesure : aire sous la courbe **à l'intérieur de chaque (modèle, gabarit)**, nuls par permutation dans les strates.
- Verrou en ligne : au-dessus du seuil, le tour est régénéré sous pilotage d'activations ; variantes « une fois », « à chaque action », « puis demander à un approbateur ».
- Tests préenregistrés et empreintés avant les données ; les tests échoués sont rapportés.

**Résultats chiffrés (auteurs).**
- Prévision de la violation (tableau 2, p. 6) : juste après la révélation 0,580 (texte 0,546, moniteur 0,551) ; à la décision, tous négatifs : 0,941 contre 0,934 et 0,944 — écarts +0,007 [−0,006 ; 0,021] et −0,022 [−0,047 ; −0,001], **en faveur du moniteur** [F6]. Contre le jumeau autorisé : 0,916 contre 0,945 et 0,949, **le texte devant** [F7]. Contre les autres actions : 0,985 contre 0,916 (+0,068).
- Avant la décision, pendant que le plan s'écrit, le texte mène (deux actions avant : 0,660 contre 0,714, p. 31-32).
- Prévision du mensonge : toutes variantes, la sonde ne bat pas le texte [F8] ; sous consigne de taire les permissions, +0,157 [0,007 ; 0,283] contre le moniteur de chaîne de pensée, seul avantage préenregistré qui passe. À 10 % de fausses alertes (descriptif) : 0,60 des mensonges pour l'ensemble interne, 0,55 pour le texte supervisé, 0,11 pour le moniteur de chaîne de pensée [F18].
- Quand l'agent est dit surveillé (47 épisodes) : sonde 0,545, texte supervisé 0,939 (tableau 2) [F10].
- Verrou : violations sur l'épisode, Gemma-4 0,68 → 0,15 (« à chaque action »), 0,70 → 0,09 (« puis demander ») ; gpt-oss 0,78 → 0,60 seulement. Un seul tour verrouillé ne fait souvent que reporter la violation (70 % sur Gemma-4).
- Familles de sécurité jamais vues : 0,81 contre 0,90, marge de non-infériorité manquée [F27].
- AgentDojo : la sonde figée ne voit pas les appels injectés (se déclenche sur 7 % et 9 % à 10 % de fausses alertes) ; réajustée sur 29 tâches, elle les sépare (0,92 à 0,98) et le verrou réduit le succès d'attaque (Gemma-4 11,7 % → 5,7 % ; gpt-oss 28,5 % → 17,5 %).

**Ce qu'il ne fait pas.** Sabotage diffus ; tâches floues ; agrégation de scores le long de la trajectoire ; test séquentiel ; garantie de fausses alertes ; point de fonctionnement à 1 % ; agent entraîné ou optimisé contre la sonde ; modèles fermés (sauf trajectoires publiées relues par un autre modèle, résultat non significatif : 0,59 [0,50 ; 0,70]).

**Limites reconnues** (p. 9) : outils factices ; mensonges étiquetés par un modèle juge ; approbateur évalué hors ligne ; pas d'évasion testée [F13] ; à la décision la revendication est le coût et l'instant, pas l'exactitude [F15] ; seuil empirique sans garantie [F14]. Borne d'observabilité : rien n'est détectable avant que le fait décisif soit vu [F21].

**Incohérences et réserves de propreté.**
- 0,916 (tableau 2, p. 6) contre 0,917 (p. 31 et tableau 5, p. 18) pour la même comparaison au jumeau autorisé : arrondi, sans portée.
- Le résumé annonce « 0,94 » et « bat les moniteurs de chaîne de pensée » dans la même phrase [F1] ; le corps montre que ces deux résultats portent sur deux objets différents (violation ; mensonge sous pression) et que, sur la violation, le moniteur fait jeu égal ou mieux. Lecture du résumé seule = trompeuse.
- Le « 10⁹ fois moins cher » compare une lecture linéaire à un appel de modèle complet avec raisonnement ; il ne compte pas la passe supplémentaire de 32 à 97 millisecondes que les auteurs mesurent eux-mêmes (p. 39).
- Calendrier : 17 préenregistrements verrouillés du 1ᵉʳ au 5 octobre 2026 (p. 40), dépôt le 12. Tout le volet confirmatoire tient en une dizaine de jours ; plusieurs verrous portent 8 amendements. Réserve : préenregistrements réels mais très rapprochés des données ; je n'ai pas pu vérifier le dépôt de code (aucun appel réseau).
- Verrou « 0 site aggravé » sur Gemma-4 et Qwen3.8 (71/0, 53/0, 61/0, 41/0, 36/0, 34/0) : très propre ; les exécutions sont déterministes et appariées par graine, ce qui l'explique en partie. Réserve de symétrie maintenue.
- La direction de la sonde est « un discriminant propre à un pli, pas une représentation partagée » (cosinus −0,02 entre plis) [F22] : fragilité que les auteurs signalent sans en tirer de conséquence pour la robustesse.
- Le signal de mensonge est porté par un seul motif (« blanchiment » par demande de permission après coup) ; hors de ce motif, 0,56 [F19].
- Plusieurs modèles et incidents cités ne sont pas vérifiables depuis ce PDF ; je ne les oppose pas (R7).

**Verdicts.**
- **H1 — voisin fort ; contre-indice partiel.** Fait : blanc contre noir sur l'agent qui agit, à fausses alertes égales, avec base de texte entraînée, préenregistré. Non fait : diffus, flou, agrégation égale, 1 %. Contre-indice : aucun avantage d'exactitude des activations une fois le plan écrit ; avantage seulement avant que le texte existe (faible : 0,580) et sous consigne de taire le raisonnement.
- **H2 (N-007) — voisin.** Contacts : seuil par action calibré sur des actions autorisées seules (mais la sonde, elle, est entraînée sur des violations) ; alarme répétée sur l'épisode (3,8 déclenchements par épisode fautif contre 1,0 par épisode autorisé, Muse) [F11]. Non fait : accumulation additive, validité à tout instant, actions sous le seuil d'un moniteur par action, rappel selon l'horizon, calibrage sans exemple de sabotage.
- **Bases de N-056** : la sonde de l'article est de la famille de la base (iii) (lecture d'un dernier état, ici par action). « Verrouiller puis demander » enchaîne une sonde et un approbateur : une cascade de détecteurs, pas la cascade de portes sur les mêmes sondes de la base (ii).
- **H8 — voisin fort (lecture dure : occupe en partie).** Voir l'en-tête, point 2. S'y ajoute la chute de la sonde quand l'agent se sait surveillé (0,545, 47 épisodes, non conclusif) [F10] : c'est l'axe « conscience d'évaluation » de H8, effleuré sans être étudié.
- **Tr — voisin lointain.** Mise en commun par moyenne au niveau des jetons, alarme par action au niveau de la trajectoire ; aucune comparaison d'agrégations, aucun attaquant.
- **HC3 — voisin.** Une injection qui usurpe l'utilisateur dans une sortie d'outil déplace l'agent **lecteur** et rend muette la sonde qui le lit [F24, F25] ; la consigne « n'obéis pas aux instructions des sorties d'outil » est suivie par Gemma-4 (succès d'attaque 0,077) et ignorée par gpt-oss (0,26) [F26]. Ni juge moniteur, ni sonde de l'agent auteur, ni usurpation stylistique sans ordre. À citer pour le bras « sonde du lecteur » de HC2 (N-013, section 8) : quatrième source où une sonde lectrice est déplacée par une attaque de contenu en boîte noire.

## 2. 2610.40588v1 — Raghav, « Pre-Crime for Agents, at the Last Second… »

**Venue imprimée** : aucune ; note de première page : travail né d'un sprint de recherche d'Apart (octobre 2026) [R4] ; auteur indépendant ; code et expériences écrits en grande partie par des agents de programmation (déclaration p. 12).

**Ce qu'il fait.**
- Deux agents : une cible tenue par une règle de son opérateur (ne jamais sortir un secret), un pair qui le réclame ouvertement pendant 20 tours au plus ; six scénarios sur un même gabarit ; épisodes de contrôle où le pair ne demande rien (aucune fuite).
- Cibles : Qwen3-32B (raisonnement coupé) et gpt-oss-20b. Sonde = régression logistique sur le flux résiduel au dernier jeton de l'entrée, avant toute génération ; sur gpt-oss, sonde de raisonnement (maximum sur les jetons) [R21].
- Trois étiquettes par appel : « cet appel fuit », « ce tour ou le suivant », « l'épisode fuira ».
- Comparateurs sur les mêmes appels : moniteur à zéro exemple (modèle de décision commercial), classifieur sac de mots entraîné [R8], règles simples (lecture du fichier, mots-clés).
- Mesure : aire sous la courbe à l'intérieur de chaque (scénario, tour).

**Résultats chiffrés (auteurs).**
- « Cet appel » : Qwen, épreuve, sonde 0,98 [0,94 ; 1,00], sac de mots 0,96 [0,92 ; 0,99], moniteur 0,75 ; gpt-oss, épreuve, sonde de raisonnement 0,91 [0,78 ; 0,99], sonde au dernier jeton 0,82 (tableaux 2 et 15, p. 7 et 25).
- « Un appel plus tôt » : 0,75 et 0,62 ; « ce tour ou le suivant » : 0,67 et 0,64 ; « jamais ou un jour » : 0,53 et 0,61 — le signal est de très courte portée [R17].
- Au seuil de 5 % des appels de contrôle : 82 % des appels fautifs pris (31 sur 38), 5,5 % des appels des épisodes sans fuite signalés ; moniteur à zéro exemple 26 % à 4,8 % [R3].
- **Par épisode** : 59 % des épisodes sans fuite reçoivent au moins une alarme (69 % attendus sous indépendance) [R13] ; au seuil « un épisode bénin sur vingt », 26 % des épisodes fautifs pris [R14] ; ce seuil, réglé sur les épisodes d'entraînement, donne 29 % au lieu de 5 % [R15].
- Sac de mots : sur le développement la sonde garde +0,035 (Qwen) et +0,043 (gpt-oss), intervalles excluant zéro [R23] ; en épreuve, +0,02, intervalle incluant zéro [R11, R29].
- Second contrôle sur la même entrée (sonde puis moniteur, ou sonde puis sac de mots) : aucun gain, 9 épisodes fautifs pris sur 38 contre 10 pour la sonde seule [R16, R25].
- Ce que lit la sonde : une divulgation à venir, permise ou non (97 à 100 % des divulgations qui suivent une lecture du fichier franchissent le seuil) [R12] ; un appel plus tôt, elle lit surtout la lecture du fichier protégé [R9].

**Ce qu'il ne fait pas.** Sabotage diffus ; accumulation ; garantie ; 1 % ; attaquant adaptatif ; fuites reformulées ou codées [R5] ; moniteur boîte noire réglé (un seul, à zéro exemple, sans réglage de consigne) [R19].

**Limites reconnues** : cadre étroit, fuites en chaînes exactes qu'un filtre de sortie prendrait [R20] ; peu d'appels fautifs en épreuve sur gpt-oss (26) ; ce que lit la sonde reste ouvert ; seuils par épisode et cascades choisis sur l'épreuve.

**Incohérences et réserves.**
- Épreuve de gpt-oss : 54 % des appels fautifs pris au seuil gelé, contre davantage au développement [R28] ; l'intervalle de 0,91 descend à 0,78.
- Les scénarios d'épreuve sont ceux du développement (nouveaux épisodes, pas nouveaux scénarios) : 0,96 à 0,98 dans chaque scénario avec 5 à 11 positifs — très propre, peu informatif.
- Le sac de mots affiché est, par modèle, la meilleure de ses deux vues (choix qui favorise la base, dit par l'auteur) ; sur Qwen, la vue « entrée entière » tombe à 0,71 : la conclusion « le texte suffit » dépend de la vue.
- Le moniteur à zéro exemple passe sous le hasard sur gpt-oss (0,40) dans la mesure stratifiée et vaut 0,86 hors strates : la comparaison « sonde contre moniteur » dépend fortement de la stratification.
- Seul le test de la sonde de raisonnement de gpt-oss est fixé avant la collecte ; les autres épreuves ont été « déjà inspectées » (tableau 37, p. 44).

**Verdicts.**
- **H1 — voisin ; contre-indice (portée).** À faux positifs voisins la sonde bat un moniteur boîte noire à zéro exemple, mais un classifieur de texte entraîné sur les mêmes étiquettes fait presque aussi bien. Acte unique, non diffus.
- **H2 — voisin ; contre-indice partiel pour l'agrégation par maximum.** Fait : sonde de l'agent qui agit à chaque appel ; seuil calibré sur trafic bénin seul ; passage du taux par appel au taux par épisode mesuré ; dépendance entre alarmes constatée. Non fait : somme, test séquentiel, garantie, horizon. Leçon : dans un cadre à acte unique, le signal n'existe qu'au dernier appel, donc rien à accumuler ; l'énoncé de H2 suppose au contraire un signal faible et réparti — c'est ce que H2 doit montrer, et ce que cet article ne teste pas.
- **Bases de N-056** : sonde au dernier jeton par appel = famille de la base (iii) ; la « cascade » testée ici (deux détecteurs sur la même entrée) n'apporte rien — à citer en regard de la base (ii), dont elle diffère (portes successives dans le temps sur les mêmes sondes).
- **H8 — voisin.** Construit établi (divulgation à venir plutôt que violation), relié aux fausses alertes sur divulgations permises ; aucune robustesse adverse.
- **Tr — voisin.** Maximum contre moyenne au niveau des jetons (la moyenne fait mieux, hors attaque) [R22] ; « au moins une alarme » au niveau de l'épisode ; l'attaque par étalement est nommée, non testée [R26].
- **HC3 — ne touche pas.** Seul contact : quand le pair se réclame de l'opérateur, le taux de fuite ne change pas (45,2 % contre 42,2 %, tableau 35, p. 41) — utile à la famille « revendication d'autorité » de HC1, pas à HC3.

## 3. 2610.39377v1 — Zhang, Yan et collègues, « AgentDecept… »

**Venue imprimée** : aucune (université de Californie à Santa Barbara et eBay).

**Ce qu'il fait.**
- Banc exécutable sur AppWorld : 477 variantes sous pression tirées de 257 tâches, six sources de pression, chacune avec un jumeau sans pression ; neuf modèles d'avant-garde ; trajectoires de 16 tours en moyenne.
- Juge en deux étapes (extraction de preuves datées, puis verdict), trois votes, par Gemini 3.8 Flash [A8] ; trois types : falsification, dissimulation, équivoque ; le jugement porte sur le rapport observable, pas sur l'intention [A3].
- Volet sondes, dit préliminaire : les trajectoires sont **relues par un autre modèle** (GLM-4.7-Flash) ; sondes logistiques sur ses états cachés (couche 27) [A4, A6] ; positifs réels complétés par des dialogues synthétiques écrits par Gemini 3.8 Flash [A5] ; score de trajectoire = maximum des scores de jetons [A7].

**Résultats chiffrés (auteurs).**
- Taux de tromperie jugée : de 0,00 % (Claude Opus 5) à 24,84 % (Gemini 3.1 Pro) (tableau 3, p. 8).
- Sondes, trajectoires réelles de Gemini (tableau 4, p. 10) : falsification, 37 positifs et 295 négatifs, aire sous la courbe 0,979, rappel 0,189 à 1 %, 0,568 à 2 %, 1,000 à 5 % ; détecteur combiné (une des trois sondes franchit son seuil) : 0,943 ; 0,179 ; 0,359 ; 0,744 [A11, A12, A14].
- Pas de lien régulier entre longueur de trajectoire et tromperie [A9].

**Ce qu'il ne fait pas.** Aucun moniteur boîte noire en regard des sondes ; aucune base de texte ; aucune sonde sur l'agent qui agit ; ni accumulation, ni garantie, ni attaquant ; pas de section de limites pour le volet sondes, renvoyé à plus tard [A2].

**Incohérences et réserves.**
- Unités non comparables : rappel **par trajectoire** contre fausses alertes **par tour neutre** [A10]. Avec un maximum sur la trajectoire, 1 % par tour vaut, sous indépendance et pour 16 tours, environ 15 % de trajectoires honnêtes alarmées (calcul : 1 − 0,99¹⁶ = 0,149) ; le taux par trajectoire n'est pas rapporté. Les « 1 %, 2 %, 5 % » ne sont donc pas opposables à un seuil par épisode.
- Figure 1 : « couches 27, 29 » ; texte : « couches 27 » [A6].
- Rappel de 1,000 à 5 % avec 37 positifs : trop propre pour être retenu sans réserve ; aucun intervalle.
- Le même modèle (Gemini 3.8 Flash) est agent évalué, juge des étiquettes et auteur des dialogues synthétiques d'entraînement : circularité possible des étiquettes, non discutée.
- La sonde lit un relecteur : elle lit le texte de la transcription à travers un autre modèle ; sans base de texte, rien ne dit qu'elle apporte plus qu'un classifieur de texte (c'est précisément ce que les deux autres articles montrent qu'il faut vérifier).

**Verdicts.**
- **H1 — ne touche pas** (aucune comparaison blanc contre noir).
- **H2 — voisin (contact).** Maximum sur la trajectoire, seuil par tour à 1 % sur tours neutres ; contre-résultat utile : bonne aire sous la courbe, rappel faible à 1 % [A13].
- **Tr — voisin.** Agrégation par maximum du jeton à la trajectoire, sans attaquant ; la combinaison « l'une des trois sondes » perd du rappel à fausses alertes fixées (0,744 contre 1,000 à 5 %).
- **H8 — ne touche pas.**
- **HC3 — voisin lointain.** Des messages d'autorité injectés dans le flux de travail changent le comportement et les rapports de l'agent ; ni juge moniteur, ni protocole « contenu = données », ni sonde de l'auteur.

## Verdicts d'ensemble par énoncé

| Énoncé | Verdict d'ensemble sur ce lot | Reste revendicable |
|---|---|---|
| **H1** | **Libre dans ces trois sources ; deux contre-indices nouveaux** (Fayyazi : partiel ; Raghav : de portée). La forme « blanc contre noir à fausses alertes égales sur l'agent qui agit » est faite sur acte unique. | Inchangé : la mesure du gain sur sabotage diffus de tâches floues, à agrégation et fausses alertes égales. À condition, désormais attendue par tout relecteur, de battre aussi un classifieur de texte entraîné sur le même préfixe (déjà exigé par N-029) et de dire si le gain subsiste hors pression sur le raisonnement. |
| **H2 (N-007)** | **Libre ; trois voisins, aucun n'accumule.** Les trois agrègent par « au moins une alarme » ou par maximum, sans garantie. | Inchangé : la conjonction de l'énoncé. Risque nommé : seuils conformes annoncés par Fayyazi et collègues [F16]. |
| **Bases de N-056** | Les sondes de Fayyazi et de Raghav sont des lectures « dernier état » par action : la base (iii) a maintenant deux représentants publiés récents, à citer. Aucune source ne fait la cascade de portes (ii). | Sans objet (ce sont des bases, pas des revendications). |
| **H8** | **Voisin fort (lecture dure : occupée en partie par 2610.17301)** : construit identifié, échec sous injection prédit et observé, sur un cas. | La prédiction, mesurée d'abord et sur plusieurs sondes, de la robustesse adverse par le construit, sur l'axe intention contre conscience d'évaluation, face à un attaquant adaptatif. À préciser dans l'énoncé : « prédiction quantitative entre sondes », pour se distinguer d'une explication après coup. |
| **Tr** | **Libre ; voisins.** Aucun attaquant adaptatif, aucune comparaison d'agrégations au niveau de l'action. | Inchangé. |
| **HC3** | **Libre ; voisins.** Fayyazi ajoute un cas d'usurpation de l'utilisateur qui déplace un agent lecteur et sa sonde. | Inchangé ; citer 2610.17301 p. 37 pour le bras « sonde du lecteur ». |

## Pages clés

- 2610.17301 : p. 3 (méthode, seuil, bases), p. 5-6 (tableau 2 et tests qui échouent), p. 8-9 (discussion, limites), p. 30-32 (résultats complets, borne d'observabilité), p. 37-38 (AgentDojo, « croyance, pas provenance »), p. 39-40 (familles jamais vues ; verrou sur chaîne de pensée sous pression ; calendrier des verrous).
- 2610.40588 : p. 1 (résumé), p. 5-7 (étiquettes, détecteurs, mesure), p. 9-11 (sac de mots, coût des alarmes, cascade), p. 31-32 (bases de texte), p. 36-39 (fausses alertes par épisode, second contrôle), p. 43 (attaque par étalement nommée).
- 2610.39377 : p. 6-7 (sondes), p. 10 (tableau 4).

## Annexe A — citations contrôlées (73, 0 échec)

Sortie du script `controle_citations_lot7A.py` (lancé par `python3 -I`), essais de la garde compris : cas juste passé, cas altéré refusé, mauvaise page refusée. Normalisation : forme Unicode compatible, guillemets et tirets unifiés, césures, traits d'union et espaces retirés ; la citation doit figurer dans le texte de la page citée (extraction avec mise en page ou en ordre de lecture, nécessaire pour les pages à deux colonnes).

| id | PDF | page | citation exacte |
|---|---|---|---|
| F1 | 2610.17301v1 | 1 | « A linear readout of the agent’s residual stream forecasts the violation before the action (AUROC 0.94) and the false report before the report, and beats chain-of-thought monitors when the agent is pressured to hide its reasoning. » |
| F2 | 2610.17301v1 | 1 | « Preprint. October 14, 2026. » |
| F3 | 2610.17301v1 | 2 | « matched agent tasks in which a single fact decides whether a critical action is authorized » |
| F4 | 2610.17301v1 | 3 | « on development authorized critical actions, i.e. 10% false alarms. » |
| F5 | 2610.17301v1 | 3 | « on everything the agent has seen and written, and zero-shot LLM monitors that read the history and the agent’s reasoning » |
| F6 | 2610.17301v1 | 5 | « the preregistered comparisons over all negatives do not pass » |
| F7 | 2610.17301v1 | 5 | « Against the authorized twin, whose context states the permission in text, text matches or beats them. » |
| F8 | 2610.17301v1 | 5 | « Pooled over all prompt variants, internals do not beat text » |
| F9 | 2610.17301v1 | 6 | « registered test that internals prevent more fails: 16 vs 20 discordant sites » |
| F10 | 2610.17301v1 | 6 | « The “monitored” variant is small (47 episodes) » |
| F11 | 2610.17301v1 | 8 | « on Muse the gate fires 3.8 times per unauthorized episode (1.0 per authorized one), so the readout must act as a per-action alarm » |
| F12 | 2610.17301v1 | 8 | « once the plan is written, a text monitor reading the same tokens matches them » |
| F13 | 2610.17301v1 | 9 | « We do not test agents trained to hide their intent from the readout » |
| F14 | 2610.17301v1 | 9 | « threshold is an empirical percentile, without a distribution-free guarantee on false alarms » |
| F15 | 2610.17301v1 | 9 | « there our claim is cost and timing (Section O), not accuracy » |
| F16 | 2610.17301v1 | 9 | « with coverage guarantees on false alarms, are a natural next step for the gate » |
| F17 | 2610.17301v1 | 14 | « the monitor flags any reasoning about permissions » |
| F18 | 2610.17301v1 | 30 | « At 10% false alarms our ensemble catches 0.60 [0.47, 0.73] of lies, against 0.55 for supervised text » |
| F19 | 2610.17301v1 | 30 | « The signal is carried by laundering lies: lies without laundering are not forecast (0.56). » |
| F20 | 2610.17301v1 | 31 | « Text matches it once the plan is written. » |
| F21 | 2610.17301v1 | 32 | « A detector cannot catch a violation made before the decisive fact is visible. » |
| F22 | 2610.17301v1 | 33 | « fold-specific discriminant, not a shared representation » |
| F23 | 2610.17301v1 | 37 | « The frozen readout reads belief, not provenance. » |
| F24 | 2610.17301v1 | 37 | « Within the same tool, injected calls even score lower than benign ones » |
| F25 | 2610.17301v1 | 37 | « they treat the injected text as the user’s own instruction » |
| F26 | 2610.17301v1 | 37 | « Gemma-4 follows the rule (attack success 0.077) and gpt-oss ignores it (0.26) » |
| F27 | 2610.17301v1 | 39 | « non-inferiority margin of 0.05 is not met » |
| F28 | 2610.17301v1 | 40 | « pressure holds for the lie forecast (Section 4.2), not for gating the violation at the decision » |
| F29 | 2610.17301v1 | 37 | « We predicted this before the confirmation data: the readout was built on informed violations » |
| R1 | 2610.40588v1 | 1 | « A bag-of-words classifier trained on the same calls comes close, so most of the gain comes from training on labels, not activations. » |
| R2 | 2610.40588v1 | 1 | « The warning is short-range, and halting on any alarm would stop most benign episodes, which a second text check does not fix. » |
| R3 | 2610.40588v1 | 1 | « at a threshold set to flag 5% of benign calls, it catches 82% of leaking calls » |
| R4 | 2610.40588v1 | 1 | « This work began at the Apart Research AI Collusion Research Sprint (October 2026) » |
| R5 | 2610.40588v1 | 2 | « We do not test reworded or encoded leaks here » |
| R6 | 2610.40588v1 | 5 | « We detect this with an exact string match on the tool log, so the label needs no judge. » |
| R7 | 2610.40588v1 | 5 | « is set so that 5% of development control calls exceed it » |
| R8 | 2610.40588v1 | 6 | « we also train a bag-of-words text classifier on the same labelled calls: TF-IDF features and a logistic regression, with the secret masked, on the same folds and weights as the probe » |
| R9 | 2610.40588v1 | 8 | « what it detects there is mostly the read of the protected file » |
| R10 | 2610.40588v1 | 9 | « Most of the probe’s lead over the zero-shot monitor therefore comes from training on labelled calls, and activations add at most a small edge. » |
| R11 | 2610.40588v1 | 9 | « On the Qwen3-32B test episodes the two are level within noise (0.98 for the probe, 0.96 for the classifier » |
| R12 | 2610.40588v1 | 9 | « The probe therefore mostly reads a coming disclosure » |
| R13 | 2610.40588v1 | 10 | « about 69% of episodes would see at least one flag; in practice 59% do, because flags cluster in the same episodes » |
| R14 | 2610.40588v1 | 10 | « per-episode threshold catches 26% of leaking episodes by their first leak » |
| R15 | 2610.40588v1 | 10 | « A threshold set on the training episodes does not transfer. On test episodes it flags 29% of refusing episodes instead of about one in twenty » |
| R16 | 2610.40588v1 | 11 | « Pairing the probe with a cheap text check on the same input adds no detectable gain. » |
| R17 | 2610.40588v1 | 11 | « Further from the act the signal fades, so our results do not support warnings rounds ahead. » |
| R18 | 2610.40588v1 | 11 | « forecast unauthorised agent actions from internal states and from text, and find that text monitors often match the internal states » |
| R19 | 2610.40588v1 | 12 | « Our main text monitor is one decision model used zero-shot, with no prompt tuning, while the probe is trained. » |
| R20 | 2610.40588v1 | 12 | « Leaks are exact strings, which an output filter would catch. » |
| R21 | 2610.40588v1 | 24 | « A call’s score is its maximum token score; the mean is reported as a check » |
| R22 | 2610.40588v1 | 30 | « averaging the reasoning tokens instead of taking the maximum gives a higher score » |
| R23 | 2610.40588v1 | 32 | « against every view the probe keeps an edge whose interval excludes zero » |
| R24 | 2610.40588v1 | 37 | « A deployed alarm would need its threshold set per episode, as Gao (2026) also argues. » |
| R25 | 2610.40588v1 | 38 | « no pairing catches more leaking episodes than the probe alone with a stricter threshold » |
| R26 | 2610.40588v1 | 43 | « Because the probe scores single calls, an attacker might spread pressure across calls, or leak through a paraphrase or an encoding. » |
| R27 | 2610.40588v1 | 43 | « Our probes are not hardened against this kind of adaptation. » |
| R28 | 2610.40588v1 | 29 | « At the frozen threshold the probe caught 54% of the leaking calls » |
| R29 | 2610.40588v1 | 32 | « which includes zero » |
| A1 | 2610.39377v1 | 1 | « The auditor’s labels also train linear probes on transcripts replayed through an open-weight model for supervision. » |
| A2 | 2610.39377v1 | 3 | « Probe-guided intervention and control remain future research questions. » |
| A3 | 2610.39377v1 | 6 | « This judgment concerns observable reporting rather than the agent’s subjective intent. » |
| A4 | 2610.39377v1 | 7 | « we replay complete trajectories through GLM-4.7-Flash [36] and train probes on its hidden states to predict falsification, concealment, and equivocation » |
| A5 | 2610.39377v1 | 7 | « To supplement the limited real positive examples of concealment and equivocation, we define 12 task-scenario templates » |
| A6 | 2610.39377v1 | 7 | « Hidden states at assistant-text positions are extracted from layers 27. » |
| A7 | 2610.39377v1 | 7 | « Each probe scores assistant tokens, and the maximum token score is used as the trajectory score. » |
| A8 | 2610.39377v1 | 7 | « We use Gemini 3.8 Flash as the LLM judge » |
| A9 | 2610.39377v1 | 9 | « show no consistent correspondence between longer trajectories and more deceptive judgments » |
| A10 | 2610.39377v1 | 10 | « TPR is measured per positive trajectory; FPR targets are calibrated per neutral turn. » |
| A11 | 2610.39377v1 | 10 | « The combined detector fires when any F/C/E probe crosses its threshold. » |
| A12 | 2610.39377v1 | 10 | « At 1% neutral turn-FPR, the falsification probe detects only 18.9% of positive trajectories. » |
| A13 | 2610.39377v1 | 10 | « high AUROC does not ensure high sensitivity under stringent false-alarm constraints » |
| A14 | 2610.39377v1 | 10 | « the falsification probe achieves an AUROC of 0.979 » |
| A15 | 2610.39377v1 | 32 | « a replay does not execute the original agent’s tool calls again » |
