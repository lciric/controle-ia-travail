# Cinq nœuds ouverts par le compte 2, au format de décision — v1

Écrit le 2026-11-14 à 08:15 UTC (heure relevée par `date -u`) par un agent neuf, en lecture seule, sur la commande de R-2665. Rien n'est tranché ici : je propose, tu décides.

## Sources, méthode, limites

- Pièces du compte 2 lues par `git show` sur `refs/remotes/origin/lot/compte-2-v1` (tête `1965ea9b`). Dossier des rapports, noté **C2/** : `docs/sources/lecture-pdf-niveau3/compte-2/`. Index qui fait foi : `C2/index-rapports-compte-2-v2.md` (`e1d9f319…`). Synthèse : `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v6.md` (`8b9a2728…`), jugée « utilisable » par sa contre-lecture (`238d10d5…`). Passation : `registres-provisoires/passation-compte-2-2026-11-14-0751.md` (`2203beb7…`). J'ai recalculé chaque empreinte citée sur le contenu de la branche : toutes égales à l'index.
- Chaque contre-lecture citée rend « tient avec corrections », sans constat bloquant (lecteur : modèle A ; contre-lecteur : modèle B).
- Textes de `main` cités avec leur ligne : programme `docs/programme-controle-ia-v2.md` (`2fd63bad…`) ; décisions dans `docs/decisions/`.
- **Je n'ai ouvert aucun PDF.** Tout chiffre d'article vient d'un rapport contre-lu, avec le PDF versé et sa page (R7) ; je n'en ai recontrôlé aucun moi-même.
- Non ouverts : le paquet et la procédure de P3-bis, T0.7, 7a, 7b, tout ce qui touche le bras d'attaque et le mode tenu à l'écart. Ce que je dis de P3-bis vient de `registres/etat.md` et de la passation seulement.
- « Non trouvé » veut toujours dire « non trouvé dans les pièces lues », jamais « libre » (R8).
- **Règle des défauts.** Les nœuds 1, 2, 3 et 5 touchent une hypothèse ou une revendication : aucun changement de texte ne peut s'appliquer par défaut. Leur « défaut sous 48 heures » est donc « énoncé inchangé », avec une règle de travail prudente. Seul le nœud 4 (un préenregistrement encore à écrire) a un défaut qui agit.

---

## Nœud 1 — H6 : la restreindre au sabotage diffus et à l'agent ?

**Décision.** Écrire ou non, dans l'énoncé de H6, « sabotage diffus » et « intervention appliquée à l'agent ».

**Énoncé actuel.** `decision-N-015-v1.md` (`462785b3…`), l. 15-17 : « pour l'une au moins des trois interventions non spécifiques (paraphrase, ré-échantillonnage, remise à zéro du contexte), il existe une intensité où, **en moyenne à intensité fixe**, le succès du sabotage d'agent chute significativement plus vite que l'utilité honnête ». Programme, l. 97 : « le succès d'attaque ». Ton mot inscrit (R-2661) : « H6 : hors audit, aucun moniteur dans l'intervention, go ». « Diffus » n'est dans aucun de ces textes ; « agent » est dans N-015, pas dans le programme.

**Trouvé.** `C2/rapport-H6-v2.md` (`ff3b13a1…`) ; contre-lecture (`3ce3ac3c…`), dont le constat C (majeur) dit qu'ajouter « diffus » resserre la revendication.
- Sous la lecture que tu as inscrite, le verdict est « non trouvé dans les pièces lues », **que la portée soit restreinte ou non** (rapport, section 1.3).
- Toute l'occupation des autres lectures vient de `docs/sources/pdf/2605.26047v2.pdf` (`947724f4…`), en cadre concentré : +10,2 points de sécurité à cinq tirages, intervalle [+6,1 ; +14,3], audit compris (p. 2, 6) ; et +0,66 échantillon d'attaque par trajectoire, [+0,26 ; +1,11], hors audit, quand le moniteur choisit l'action (p. 10).
- Deux voisins désignés et non lus : arXiv 2511.02997 (« à lire en priorité ») et arXiv 2607.13087 (nommé par N-013, l. 80 ; « le voisin le plus direct » de la lecture hors audit).

**Enjeu.** La restriction ne change pas le verdict d'aujourd'hui. Elle fixe ce que E1.6 doit mesurer pour porter la revendication, l'exposition aux deux voisins non lus, et la phrase publique : le rapport interdit d'écrire que « diffus » figure dans l'énoncé (section 7).

**Options.**
- **(a) Restreindre par la lettre** : « sabotage diffus d'agent », intervention appliquée à l'agent.
  - Avantage : la revendication a la portée de sa mesure (le papier A travaille en sabotage diffus ; E1.7 traite le concentré à part). Un travail en cadre concentré ne l'occupe plus. Le resserrement n'esquive aucune collision connue, puisque le verdict ne dépend pas de lui.
  - Inconvénient : modification d'hypothèse. Un effet en cadre concentré se rapporterait comme résultat, non comme prédiction (même règle que N-015, l. 25-27).
  - Textes : une ligne de décision qui complète N-015 ; préenregistrement de E1.6 écrit en diffus ; aucune porte touchée.
- **(b) Laisser l'énoncé sans restriction.**
  - Avantage : aucun texte ne bouge ; portée plus large.
  - Inconvénient : la revendication couvre le concentré, où se trouvent le travail le plus proche et, peut-être, les deux voisins non lus ; E1.6 en diffus seul ne la porterait pas en entier.
  - Textes : rien ; le préenregistrement de E1.6 devrait prévoir un bras concentré, ou dire que H6 n'est testée qu'en diffus.
- **(c) Attendre la lecture des deux voisins**, puis trancher.
  - Avantage : décision mieux informée. Inconvénient : H6 reste « non déclarable » (condition 2 de la synthèse) et la décision se prend après avoir vu ce que les voisins occupent, ce qui ressemble à tailler la zone.

**Si on ne décide pas.** Avant le verdict de P3-bis : rien ne casse, H6 ne lit aucune sonde. Avant G0 : rien non plus, aucune tâche de la phase 0 ne dépend de H6 (N-015, l. 31-32). Le coût est ailleurs : la seconde vague de lectures du compte 2 ne sait pas contre quel énoncé lire 2511.02997 et 2607.13087, et la phrase pour le jury reste suspendue.

**Recommandation : (a). Confiance : 0,70.** Défaut sous 48 heures : énoncé inchangé (b) ; règle de travail : E1.6 se prépare en diffus et aucune phrase n'écrit « diffus » comme partie de l'énoncé.

**Ce qui manque.** La lecture sur PDF de 2511.02997 et de 2607.13087. Deux points voisins, hors de ce nœud :
- l'ajout d'une « différence de pentes testée » reste ouvert (rapport, section 6) ;
- sous ta lecture, exécuter le premier tirage ne change rien en loi : le rééchantillonnage ne peut porter H6 qu'avec une règle de choix sans moniteur (un vote entre tirages, par exemple), à fixer au préenregistrement de E1.6. C'est une déduction de ma part, non imprimée.

---

## Nœud 2 — Rôle 1 de N-065, après la collision avec arXiv 2609.28614

**Décision.** Garder l'énoncé du rôle 1 avec citation obligatoire de 2609.28614, le resserrer sur ce qui n'est pas trouvé, ou ne plus le revendiquer.

**Énoncé actuel.** `decision-N-065-v1.md` (`f820e90d…`), l. 15-18 : « Son juge statistique est un moniteur d'affirmations de recherche ; l'attaque de Goodhart (A1-v4) et le juge-tournoi façon Co-Scientist (juge génératif sous la même attaque) mesurent la corruptibilité de deux sortes de juges sur les juges de la recherche automatisée. » N-067 a déjà cédé le calcul hors des agents et ne garde que le nul formé des lois connues.

**Trouvé.** `C2/rapport-4B-partie1-v2.md` (`2fcefa4a…`) ; contre-lecture (`e9c5ad74…`) : « la collision est réelle », verdict « occupé en partie » jugé juste. Bras génératif : `C2/rapport-4B-partie2-v2.md` (`c1708b9c…`).
- `2609.28614v1.pdf` (`424650d4…`) met deux sortes de surveillants de la recherche par agents devant les mêmes fraudes : un jury de modèles et un contrôle d'exécution calculé hors de l'agent, sans modèle. Taux de passage : 6,5 % et 7,5 % (p. 7, 28). Transfert des fraudes adaptées contre le jury : « Five of those 56 also pass the execution audit. » (p. 11).
- La collision porte sur le **cadre**. Ce contrôle n'est pas un juge statistique (ni nul ni épreuve), il n'est jamais visé par l'attaque, aucun gain continu n'y est mesuré, et l'étiquette de fraude vient d'un jury de modèles qui voit ses preuves (p. 5, 26) : comparaison circulaire.
- Non trouvé, formulation exacte du rapport (section 5) : la corruptibilité mesurée comme gain continu selon l'intensité d'une même attaque, d'un juge statistique (épreuve hors des agents contre un nul formé des lois connues) et d'un juge génératif, sous un même proposeur qui lit la règle de chacun, avec comparaison inférentielle des deux courbes sur une vérité plantée indépendante des deux juges.
- Désignés et non lus : Lodkaew et collègues, arXiv 2606.07379 (« à lire sur PDF avant toute phrase publique ») ; Gao, Schulman et Hilton, arXiv 2210.10760.

**Enjeu.** La phrase de N-065, lue seule, décrit ce que 2609.28614 fait déjà de façon descriptive. Ce qui distingue le rôle 1 tient en cinq propriétés jointes, dont aucune n'est écrite dans N-065.

**Options.**
- **(a) Énoncé inchangé, citation obligatoire de 2609.28614.**
  - Avantage : aucun texte ne bouge. Inconvénient : la phrase reste celle du cadre occupé ; chaque texte public devra redire à la main ce qui distingue.
  - Textes : 2609.28614 s'ajoute aux citations obligatoires (N-064, N-067).
- **(b) Resserrer** sur la formulation exacte du rapport.
  - Avantage : l'énoncé dit ce qui n'est pas trouvé ; il prolonge N-067. Inconvénient : il engage à faire les cinq propriétés ; une conjonction aussi étroite est la forme même de la zone séduisante (R8), et les deux lectures désignées visent, d'après leur titre seul, deux de ses termes (le contrôle calculé hors de l'agent, le gain continu).
  - Textes : une décision qui complète N-065 ; à confronter au préenregistrement scellé de A1-v4 (`d306a8fa…`, non relu ici) ; à reprendre dans le préenregistrement du papier C s'il porte le second terrain.
- **(c) Ne plus revendiquer le rôle 1** : l'organisme reste un terrain de mesure, rapporté comme extension de 2609.28614.
  - Avantage : aucune exposition. Inconvénient : le papier C perd un terrain distinctif, alors qu'aucune des trois propriétés propres n'est faite ailleurs dans les pièces lues.

**Si on ne décide pas.** Avant le verdict de P3-bis : sans effet, les deux sujets ne se croisent pas. Avant G0 : gênant seulement si le préenregistrement du papier C (critère 7) décrit le second terrain, car il scellerait une phrase dont le cadre est occupé. Le rôle 1 reste « non déclarable » dans les deux cas.

**Recommandation : (b), en deux temps. Confiance : 0,65.** Adopter la formulation resserrée comme énoncé de travail ; ne la déclarer qu'après lecture de Lodkaew et collègues, puis de Gao, Schulman et Hilton. Défaut sous 48 heures : (a), énoncé inchangé avec citation obligatoire.

**Ce qui manque.** Ces deux lectures ; la confrontation des cinq propriétés à ce que A1-v4 mesure vraiment (échelle d'intensité, comparaison inférentielle, vérité plantée indépendante) ; le sort du rôle 3, toujours ouvert.

---

## Nœud 3 — Tr : la robustesse du maximum au grain du jeton peut-elle rester dite « établie » ?

**Décision.** Garder, corriger ou retirer la prémisse « établie au niveau token » de l'énoncé de Tr.

**Énoncé actuel.** Programme, l. 98 : « La robustesse des agrégations max et attention, établie au niveau token, tient-elle au niveau action et trajectoire sous accumulation séquentielle, face à un attaquant adaptatif ? »

**Trouvé.** `C2/rapport-Tr-v2.md` (`139596cf…`) ; contre-lecture (`2a530bfe…`), dont le constat C (majeur) juge le contre-indice « confondu et fragile », non « léger ».
- `lot11/2601.04603v1.pdf` (`ba8ec657…`) plaide l'inverse pour le maximum brut : « Without averaging, a single token with a spuriously high activation could incorrectly flag an entire sequence as harmful. » (p. 6). Ses mesures (figures 2b, p. 7, et 5b, p. 16) vont dans ce sens, mais elles sont confondues avec l'entraînement, sans barre d'erreur, non monotones, sur des attaques transférées.
- En sens contraire, sans adversaire : arXiv 2609.15994, lue pour HC4, où l'attention et le maximum tiennent mieux que la moyenne sous des fautes réparties (tableau 3, p. 6 ; synthèse v6, section Tr).
- Le niveau 2 relevait déjà une « prémisse affaiblie ». Le noyau de Tr reste non trouvé ; trois composantes sont faites hors du noyau.
- Divergence de lettre : « non trouvé » (lecteur) contre « occupé en partie » (contre-lecteur) ; la synthèse garde le plus dur.

**Enjeu.** Le programme tient pour acquis un fait qu'un PDF vérifié conteste. Toute phrase publique qui reprendrait « établie » serait fausse. La prémisse fixe aussi le signe attendu de E1.5.

**Options.**
- **(a) Garder « établie ».** Avantage : rien ne bouge. Inconvénient : prémisse contredite par une pièce lue ; les règles lissées, que la pièce donne pour meilleures, resteraient hors de la comparaison.
- **(b) Corriger la prémisse** : « rapportée au niveau du jeton dans certains cadres, contestée pour le maximum brut », la question restant la même.
  - Avantage : exact ; Tr devient une question à deux issues, sans signe visé (R3) ; les sept règles imprimées relevées par le rapport servent de bases à E1.5.
  - Inconvénient : modification d'hypothèse ; E1.5 compare plus de règles, donc un devis de phase 1 un peu plus large.
  - Textes : une décision sur Tr ; préenregistrement de E1.5 ; aucune porte.
- **(c) Retirer la prémisse** : Tr devient « comparaison des règles d'agrégation au grain de l'action et de la trajectoire sous attaquant adaptatif ».
  - Avantage : à l'abri de toute dispute sur le jeton. Inconvénient : l'angle « transposition » disparaît, avec le lien aux travaux au grain du jeton.

**Si on ne décide pas.** Avant le verdict de P3-bis : sans effet direct. Avant G0 : sans effet sur les critères, E1.5 est en phase 1. Le risque est de reprendre « établie » dans un texte pour le jury ou dans un brouillon ; et Tr reste « non déclarable » (conditions 2 et 4).

**Recommandation : (b). Confiance : 0,80.** Pour la lettre du verdict, garder « occupé en partie », le plus dur des deux (R4). Défaut sous 48 heures : énoncé inchangé ; règle de travail : aucun texte ne reprend « établie », ce que R7 impose déjà.

**Ce qui manque.** Wilhelm et Kao 2026 ; Yang et collègues, arXiv 2510.17431 ; « What the Monitor Saw », non obtenu ; la relecture contre Tr de McKenzie et collègues, arXiv 2506.10805, qui porte l'agrégation par attention de la prémisse et n'a été lue qu'au niveau 2. Le coefficient de lissage de 2601.04603 n'est imprimé nulle part.

---

## Nœud 4 — G1 : ajouter une base « somme à horizon fixe » ?

**Décision.** Ajouter ou non, aux bases de comparaison, la somme des mêmes scores de sondes lue en fin d'épisode, avec un seuil calibré sur épisodes honnêtes entiers ; et dire où elle compte.

**Énoncé actuel.**
- `decision-N-007-N-008-v1.md` (`ab7dc9bb…`), l. 47-48 : « Les bases (i) et (iv) entrent dans l'ensemble « meilleure base boîte noire, toutes variantes confondues » de la porte G1. » ; « Les bases (ii) et (iii) servent à H2, pas au critère de G1. »
- `decision-N-056-v1.md` (`3592c1e9…`), l. 38-41 : « La porte G1 exige que le séquentiel boîte blanche batte **chaque moniteur boîte noire de la liste scellée** (N-007, N-008) **et** les deux bases boîte blanche de N-007 : **(ii) la cascade de portes** sur les mêmes sondes et **(iii) la sonde sur le dernier état** ».
- Aucune somme à horizon fixe dans `docs/decisions/` ni dans `prereg/` (recherche par mots). Le préenregistrement de G1 n'est pas scellé.

**Trouvé.** `C2/rapport-H2-v2.md` (`f801ee84…`), section 9 ; contre-lecture (`708b48c2…`), constat E (majeur), qui propose la base.
- `lot8/2501.03982v5.pdf` (`e40c1131…`) : à horizon connu et loi nulle spécifiée, l'accumulation toujours valide vers l'avant ne fait pas mieux, au terme, que le meilleur test à horizon fixe. Dans l'exemple de l'article, elle perd : 91 % contre 79 %, et 47 % si l'alternative est apprise en ligne (p. 2). Une alarme anticipée a un prix (p. 3, 4, 12).
- Réserve maintenue par le lecteur : la perte n'est montrée que dans cet exemple ; en général, « pas mieux au terme » seulement.
- La base isolerait le prix de la garantie toujours valide, à sondes égales. Ni (ii) ni (iii) ne le font.

**Enjeu.** Un relecteur demandera pourquoi ne pas sommer et lire à la fin. Mais cette somme a toutes les chances d'égaler ou de battre notre accumulation sur le rappel terminal : c'est le sens du résultat publié. La question est donc moins « l'ajouter » que « où la mettre ».

**Options.**
- **(a) Ne pas l'ajouter.** Avantage : le plan ne bouge pas. Inconvénient : une comparaison évidente manque, sur un point où un travail publié prédit que nous perdons ; c'est le cas même que R4 demande de regarder.
- **(b) L'ajouter comme base rapportée de H2, hors du critère de G1**, avec deux mesures et un signe écrit d'avance : le rappel terminal à 1 % de faux positifs (prédiction : la somme égale ou bat l'accumulation ; l'écart est le prix de la garantie) et l'alarme avant le dommage, critère de sécurité du programme (l. 74), que la somme lue à la fin ne peut pas donner.
  - Avantage : le prix de la garantie est mesuré et dit ; la revendication de H2 se place là où elle peut tenir (alerter à temps). Calcul sur processeur, mêmes scores, aucune dépense.
  - Inconvénient : il faudra écrire que G1 ne compare l'accumulation qu'à (ii) et (iii), et que la seconde question de N-056 (« notre accumulation bat les autres façons de lire l'intérieur ») a une exception connue au terme.
  - Textes : préenregistrement de G1 (bases de H2, prédiction, métriques) ; N-007 complétée d'une base (v) ; critère de G1 inchangé.
- **(c) La mettre dans la liste que G1 doit battre** (N-056).
  - Avantage : G1 dirait le plus possible. Inconvénient : G1 échouerait probablement sur ce contraste, pour une raison d'agrégation et non de sondes ; or chaque lecture décisive de G1 consomme une famille tenue à l'écart (N-062, point 3).
  - Textes : critère de G1 réécrit : nœud lourd.

**Si on ne décide pas.** Avant le verdict de P3-bis : rien ne casse ; mais il est plus propre de fixer cette base avant qu'un résultat de sondes soit connu. Avant G0 : bloquant pour le critère 6. Une fois le préenregistrement de G1 scellé sans la base, l'ajouter est un écart à un texte scellé.

**Recommandation : (b). Confiance : 0,80.** Horizon : la fin réelle de l'épisode. Métriques : les deux. Défaut sous 48 heures : (b), inscrite au brouillon du préenregistrement de G1 comme base rapportée hors critère ; le scellement te revient de toute façon.

**Ce qui manque.** Howard et collègues 2020, titulaire de l'outil, non lu. La normalisation de la somme quand les épisodes n'ont pas la même longueur, à fixer au préenregistrement. Makins et collègues 2026 et Oldfield et collègues 2026, désignés contre H2, non lus.

---

## Nœud 5 — L : resserrer la revendication au-delà de « L1 en remarque » ?

**Décision.** Dire ce que L revendique encore, maintenant que le cœur de L1 est imprimé chez Ker.

**Énoncé actuel.** `decision-N-003-N-004-v1.md` (`cc1be393…`).
- L. 75 : « **Revendication** : l'énoncé adverse complet (invariances exactes, borne toujours valide, coût du report, détection à temps, validité sous dépendance), appliqué aux scores de sondes internes. Le cœur statistique (frontières à mélange normal, dichotomie somme/max) est cité comme classique. »
- L. 77 : « Repli prévu au premier rendu, option (c) : présenter L comme corollaire cité et porter l'effort sur la mesure. […] toute bascule effective est un nœud. »
- Ton mot inscrit (R-2657) : « L : L1 en remarque avec renvoi à Ker, go ». Il ne dit rien du reste ; la ligne 75 porte encore « invariances exactes ».

**Trouvé.** `C2/rapport-L-voisins-v2.md` (`649f471e…`, contre-lecture `58e7ad2d…`) ; `C2/rapport-L-ker2007-v2.md` (`6bf86934…`, contre-lecture `8805d9cf…`) ; `C2/rapport-L-lot8-v2.md` (`8d9f2654…`).
- **Cœur de L1** : occupé en partie par `ker-2006-batch-steganography-pooled-steganalysis.pdf` (`a6ab71a2…`, p. 7, 14). Résidu : une ligne.
- **Décroissance en n₀ à budget fixé** : occupée, résidu « aucun » (Ker 2006, p. 7, 11, 12 ; `ker-2007-capacity-result-batch-steganography.pdf`, `73113e2d…`, p. 2-3, pour la répartition égale, contre tout test, à nombre d'objets fini).
- **L4** : voisin ; son contenu propre est jugé élémentaire. **L3 (b)** en lecture toujours valide : non trouvé, « une ligne » au-delà de L1.
- **Non trouvés** : L3 chiffré (calendrier, coût du report, prix de la garantie) ; la comparaison du processus e cumulé et des détecteurs de rupture ; L2 au seuil exact ; la validité sous dépendance ; la non-compensation ; la mesure sur sondes.
- Le séquentiel est réservé par Ker en toutes lettres (2006, p. 5 ; 2007, p. 4). La borne de Ker 2007 majore déjà toute règle lue dans un lot de taille connue, sous répartition égale : déduction du contre-lecteur, non imprimée.
- Constat G de la contre-lecture de Ker 2007 : ce qui reste non trouvé **ne se limite pas** à la couche séquentielle.
- `1202.6423v4.pdf` (Bash, Goeckel et Towsley, `ab6caead…`) : voisin, rien d'occupé. `1906.08938v2.pdf` (lot 8) publie déjà le critère d'alarme pendant l'attaque (p. 5-6) et le fait que le calendrier compte (p. 10, 13-15).

**Enjeu.** L est la thèse centrale du programme (section 3). Sa ligne de revendication contredit ton mot. La couche séquentielle, la plus tentante à garder, est celle que visent quatre pièces non lues.

**Options.**
- **(a) En rester au mot inscrit.** Avantage : rien de plus à écrire. Inconvénient : la décroissance en n₀ et L3 (b) restent revendiquées en apparence alors qu'elles sont imprimées ou tiennent en une ligne ; le préenregistrement de G1, qui part de ces énoncés, hériterait de l'écart.
- **(b) Resserrer par composante, avec un repli décidé d'avance.**
  - Remarques citées, non revendiquées : L1, la décroissance en n₀, L3 (b), L4.
  - Revendiqué sous réserve de lectures : L3 chiffré ; processus e cumulé contre détecteurs de rupture pour l'alarme avant le dommage ; L2 au seuil exact, à n fini, avec son plancher ; validité sous dépendance ; mesure sur scores de sondes. La non-compensation reste une condition empirique.
  - Repli écrit d'avance : si Huang, Wang et Poor 2021 ou Trivedi et Chandramouli 2003 occupent le calendrier ou le coût du report, le repli (c) de N-004 t'est proposé aussitôt.
  - Avantage : la revendication suit les pièces ; rien n'est cédé sans raison. Inconvénient : modification de revendication ; le reste est jugé élémentaire par les lecteurs ; la liste reste suspendue à des lectures que tu dois fournir.
  - Variante que je ne recommande pas : tout ramener à « la couche séquentielle et toujours valide ». Elle cède sans raison L2, la dépendance et la mesure, et concentre la revendication sur la zone la moins vérifiée.
  - Textes : une décision qui complète N-004 ; note mathématique v3 ; préenregistrement de G1.
- **(c) Déclencher dès maintenant le repli de N-004** : L corollaire cité, effort sur la mesure (E1.3).
  - Avantage : plus aucune exposition théorique ; cohérent avec H2 (« une mesure, non un outil »). Inconvénient : le papier A perd son lemme comme apport, avant que les pièces décisives soient lues ; l'entretien change de ton.

**Si on ne décide pas.** Avant le verdict de P3-bis : rien ne casse, mais la seconde vague de lectures ne sait pas quelles pièces passent en premier. Avant G0 : bloquant pour le critère 6, puisque le préenregistrement de G1 part des énoncés retenus de L ; gênant pour le critère 8, L restant « non » avec la réserve M4 ; et l'entretien du 27 novembre porterait une phrase sur L non arrêtée.

**Recommandation : (b). Confiance : 0,65.** Défaut sous 48 heures : revendication inchangée ; règle de travail : L1, la décroissance en n₀ et L3 (b) s'écrivent comme remarques citées, et rien n'est dit « libre » de la couche séquentielle.

**Ce qui manque.** Sans version libre, à fournir par toi : Huang, Wang et Poor 2021 (*IEEE Transactions on Information Theory* 67(11), p. 7285-7303), la plus directe sur le calendrier et l'alarme avant le dommage ; Trivedi et Chandramouli 2003 (séquentiel) ; Bash et collègues, ISIT 2014 ; Arumugam et Bloch 2016. À verser aussi : Bash et collègues 2016 ; Filler, Ker et Fridrich 2009 (dépendance) ; Cachin 2004. La version de revue de 1202.6423 n'est pas lue.

---

## Ordre d'urgence

1. **Nœud 5 (L)** : thèse centrale ; bloque le préenregistrement de G1 (critère 6 de G0) et la phrase de l'entretien du 27 novembre ; quatre pièces ne peuvent venir que de toi, donc le délai court dès maintenant.
2. **Nœud 4 (G1)** : bloque le même préenregistrement ; décision rapide ; le défaut agit seul si tu ne dis rien.
3. **Nœud 2 (rôle 1)** : à trancher avant le scellement du préenregistrement du papier C s'il porte le second terrain ; sinon peut attendre les deux lectures.
4. **Nœud 3 (Tr)** : la règle de travail suffit jusqu'au préenregistrement de E1.5, en phase 1.
5. **Nœud 1 (H6)** : rien n'en dépend en phase 0 ; un mot suffit, mieux vaut le donner avant la lecture des deux voisins.

Aucun des cinq ne dépend du contenu du verdict de P3-bis. Les nœuds 4 et 5 gagnent pourtant à être tranchés avant lui, pour que la revendication soit fixée avant tout résultat de sondes.
