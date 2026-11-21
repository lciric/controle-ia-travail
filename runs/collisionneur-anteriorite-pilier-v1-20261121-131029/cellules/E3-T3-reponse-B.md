# Proposition B — Tour III.3 : réponse aux critiques

**Pièces.** Les blocs FAITS et QUESTION, ma conception III.1 et les critiques A, C, D et E sont présents. Chacun va jusqu'à sa ligne de fin, sans coupure visible. Je n'ai pas vérifié les empreintes. Je ne réponds qu'aux sections « Sur la proposition B ».

**Statuts.** Les FAITS restent RAPPORTÉ, comme au tour III.1. Les critiques sont des analyses de leurs auteurs. Plusieurs contiennent des identités probabilistes sous un modèle qu'elles posent elles-mêmes : C et E en marquent certaines VÉRIFIÉ, A et D les présentent comme des déductions sous leurs définitions. Je ne touche pas à ces étiquettes. Je dis seulement si j'ai relu le calcul et si j'en accepte la conséquence. Que ces modèles conviennent au pilier reste une HYPOTHÈSE. Tout chiffre nouveau est illustratif.

---

## (a) Les critiques, une par une

### Tableau des verdicts

| # | Critique (sources) | Verdict | Conséquence |
|---|---|---|---|
| K1 | E1 confond le type de collision et l'accès au texte intégral (A, E) | Acceptée, transformée en test | Strate à accès égalisé ; l'accès A_i est observé pour chaque appât. |
| K2 | E1 confond recherche et mémoire : les appâts publiés sont probablement dans les données d'entraînement (A) | Acceptée, transformée en test | Bras « livre fermé » ; appâts postérieurs à la coupure du modèle si l'on en trouve assez. Je ne sais pas si c'est le cas dans les cinq zones. |
| K3 | Les quasi-jumeaux sont étiquetés par le jugement de celui qui les fabrique (A, C, D, E) | Acceptée, transformée | Voir le détail ci-dessous. |
| K4 | Un même humain construit les appâts, juge les jumeaux et sert de relecteur évalué (C, D) | Acceptée | Trois rôles séparés : constructeur, adjudicateur, relecteur évalué. |
| K5 | Fuite de dictionnaire : mon lexique du §1.3 servirait à la fois aux appâts et aux reformulations du §3 (C, E) | Acceptée, transformée en test | Voir E1′. |
| K6 | Le style de rédaction du constructeur trahit l'étiquette (D ; argument de A contre C, repris ici) | Transformée en test | Classifieur de surface (voir E1′). |
| K7 | Un résultat publié réécrit n'est pas du folklore (D) | Acceptée | Strate « folklore » retirée d'E1. Le folklore n'est plus testé du tout. |
| K8 | Un critère sur l'écart relatif r_L − r_T valide un instrument uniformément faible ; si r_L = r_T = f, l'écart est nul sans aucune discrimination (E, D) | Acceptée | Ajout d'un plancher absolu de discrimination r_T − f, strate par strate. |
| K9 | Avec quelques appâts par type, l'écart de 30 points n'est pas jugeable (A, C) | Acceptée ; j'ai relu le calcul | E1 est déclassée si l'effectif n'est pas atteignable (voir E1′). |
| K10 | Le juge serait évalué sur les appâts qui ont servi à régler les requêtes (A) | Acceptée | Des familles entières d'appâts sont réservées au test. |
| K11 | E1 ne mesure pas la fréquence des types parmi les vraies collisions (D) | Acceptée | C'est la critique qui me coûte le plus (voir ci-dessous). |
| K12 | E2 : ordre fixe, effort cumulé, comptage dans un seul sens (A, C, D, E) | Acceptée | E2 est refondue en E2′. |
| K13 | Le seuil « au moins une collision » est franchi par les seules fausses alertes : 1 − (1 − ε)^K tend vers 1 quand K croît (A, C) | Acceptée ; identité relue (indépendance supposée) | Chaque collision est adjugée par implication ; on soustrait un bras placebo. |
| K14 | E2 mesure des retraits de cibles, pas les bonnes cibles qu'une cartographie aurait fait proposer (D) | Acceptée comme limite | E2′ ne teste que la fonction de protection. La fonction de choix reste non testée. |
| K15 | Faire travailler deux équipes indépendantes en parallèle (C) | Rejetée telle quelle, transformée | Voir le détail ci-dessous. |
| K16 | Dans E3, H_B fusionne « présent ou en PR » et « fermé automatiquement » (A) | Acceptée | Trois issues distinctes. |
| K17 | E3 n'a pas de courbe selon le budget t (A) | Acceptée | Plusieurs budgets ; le verdict est indexé par t. |
| K18 | Un lemme présent sur un type isomorphe ne sera pas retrouvé (C) | Acceptée, transformée en test | Positifs « isomorphes » ajoutés. |
| K19 | Mes « contrôles négatifs » d'E3 sont des contrôles positifs ; E3 n'a pas de vrai négatif (A, D, E) | Acceptée | Correction du nom, et ajout de vrais négatifs. |
| K20 | E3 ne voit que les PR publiques (D) | Acceptée | Verdict daté et restreint aux PR publiques. |
| K21 | E4 est vraie par construction : la pile a été remarquée parce qu'elle semblait voisine (A, D) | Acceptée | E4 est redéfinie par l'implication, avec un négatif apparié sur le thème (A, D, E). |
| K22 | Le contrôle « le passage cité figure dans le document » est satisfait par une citation exacte qui soutient l'énoncé inverse (D, E) | Acceptée, transformée en test | Appâts de citation hors implication. |
| K23 | L'accord entre relecteurs n'est pas un rappel ; avec un relecteur par zone, il n'est même pas estimable (A, E) | Acceptée, avec une contradiction interne reconnue | Mon §4 dit « un par zone », mon tableau (c) demande deux relecteurs. L'accord devient un diagnostic, pas une validation. |
| K24 | Prouver formellement la non-vacuité des quasi-jumeaux (C) | Partiellement rejetée | Voir le détail ci-dessous. |
| K25 | Aucun banc n'estime le rappel r sous la loi de déploiement P_dépl (A, point transversal) | Acceptée ; aucun banc ne la répare | E0 proposée, qui ne donne qu'une borne. |

### Détail des points non triviaux

**K3, les quasi-jumeaux.** Un jumeau ne compte dans le taux de fausses alertes f que s'il remplit deux conditions.
- Son changement de valeur est établi par un contre-exemple ou par un calcul sur une petite instance.
- Un second expert l'a adjugé, à l'aveugle, sans en être l'auteur, et si possible d'une autre communauté.

Je reprends l'argument de C contre E : un changement de constante sur une petite instance n'exclut pas que le jumeau soit un cas particulier d'un théorème plus général. La première condition est donc nécessaire, pas suffisante.

Toute alerte de l'agent sur un jumeau est adjugée à son tour. Si l'agent apporte un passage et une implication validés, le jumeau est reclassé positif et compté comme une erreur de l'étalon. Je rapporte f sous les deux conventions, ainsi que le taux de reclassement η̂. Selon le calcul de E, le biais naïf vaut η(r − f) : η̂ mesure donc l'imperfection de l'étalon au lieu de la cacher.

**K24, la preuve formelle demandée par C.** J'accepte d'établir le changement de valeur quand c'est faisable (point K3). Je rejette deux choses.
- **L'exigence d'une preuve formelle comme condition d'admission.** La bibliothèque Lean ne couvre qu'une part du vocabulaire (RAPPORTÉ). Imposer la formalisation ajouterait un risque de traduction infidèle ou vide, celui-là même que C oppose à d'autres propositions.
- **L'idée qu'on puisse certifier « pas un corollaire trivial » en général.** On peut vérifier « pas un corollaire du parent ». « Pas un corollaire d'autre chose » est précisément la question ouverte du pilier. Ce risque est traité par η̂, pas par une certification.

**K15, les deux équipes de C.** A et E reprochent à D un effet d'équipe confondu avec la politique testée. La même objection vaut contre la suggestion de C. Je la transforme selon qui exécute les bras.
- **Si les bras sont des agents** : même modèle, contextes vierges, aucune trace partagée. L'effet d'équipe disparaît ; il reste la variance d'exécution, mesurée par des répliques.
- **Si ce sont des humains** : plan croisé. Chaque personne exécute la méthode (i) sur une zone et la méthode (ii) sur l'autre, dans un ordre tiré au sort.

**K11, la fréquence des types de collision.** Au tour III.1, j'ai écrit que E1 réfutait mon hypothèse (i), « les collisions chères sont surtout non littérales », « si les collisions observées sont surtout littérales ». C'est faux. E1 n'observe aucune collision réelle : la composition du banc par type y est fixée par le constructeur. La fréquence P(type | collision) n'est mesurée par aucune de mes expériences telles que je les avais conçues.

L'hypothèse (i), qui porte ma recommandation, n'est donc pas testée. Elle passe dans la colonne « non établi ». Correction : toute collision réelle adjugée (en E4′, E2′, E0 et aux étapes 3 et 4) est typée par deux personnes et consignée. C'est la seule source qui puisse un jour la réfuter.

**K25, le banc contre le déploiement.** A a raison : quand le support de P_dépl n'est pas couvert par P_banc, aucune repondération ne corrige. Je ne sais pas réparer ce point au-delà d'une borne. Ma proposition est E0, ci-dessous.

---

## (b) Expériences corrigées

Tous les seuils sont fixés avant levée de l'aveugle par l'arbitre. Leurs valeurs sont à fixer ; celles que je cite sont illustratives. Quand un intervalle chevauche le seuil, il n'y a pas de verdict, et cette issue est annoncée d'avance. Aucun « n augmenté » n'est permis après coup, pour éviter l'arrêt optionnel que E reproche à A.

### E4′ : les travaux de 2026 croisés règlent-ils une cible candidate ?

À faire en premier.

- **H_A** : au moins un travail croisé règle une cible candidate. Cela veut dire qu'une implication est adjugée : passage cité, hypothèses comparées, sens de l'implication établi. Ou bien il en fait un corollaire immédiat.
- **H_B** : aucun ne règle de cible ; les recoupements sont seulement thématiques.

**Matériel**
- La pile croisée (RAPPORTÉ).
- La liste candidate dans son état actuel. Je ne sais toujours pas si elle est scellée.
- **Négatif apparié (K21)** : des travaux de 2026 de la même zone, hors de la pile, tirés par une requête préenregistrée et lus selon le même protocole.
- **Pièges (K22)** : des passages exacts sur le bon objet, mais sous une hypothèse qui invalide l'inférence.

**Adjudication.** Deux lecteurs, dont un n'a pas écrit la cible. En cas de désaccord, la cible est classée « contesté » et n'est comptée ni d'un côté ni de l'autre. Chaque collision adjugée est typée (K11).

**Issues**
- **H_A retenue** : le scellement sans lecture, c'est-à-dire l'option (b) par défaut, est falsifié pour cette zone. La cible est retirée ou reformulée, et l'on obtient une première donnée réelle sur les types.
- **H_B retenue** : l'idée que la pile croisée menace les cibles actuelles est falsifiée. Cela ne dit rien des collisions ailleurs, et l'urgence de l'option (a) perd ce fondement.

**Contrôle informatif dans les deux sens.** Si le négatif apparié règle des cibles à un taux comparable, la pile n'a rien de particulier. La prévalence est alors probablement générale dans la zone, ce qui plaide pour une cartographie. S'il n'en règle aucune pendant que la pile en règle, l'effet est local à la pile.

**Ce qu'E4′ n'estime pas.** Elle n'estime pas π : la sélection de la pile rend P(collision | croisé) non transposable (point de D).

**Coût.** Du temps de lecture humaine. Le volume de la pile n'est pas donné. E4′ exige une exception au gel.

### E3′ : un lemme candidat est-il déjà dans la bibliothèque ?

Contrôle de routine, avant toute dépense sur un lemme.

**Trois issues (K16)**
1. Présent, ou en PR publique, à une date d.
2. Fermé automatiquement sous un budget t, pour plusieurs valeurs de t (K17).
3. Absent et non fermé sous le t maximal.

**Hypothèses**
- **H_A** : issue 3.
- **H_B** : issue 1 ou 2, consignées séparément. L'issue 2 signifie « non payant comme lemme ». Ce n'est pas une collision mathématique.

**Contrôles positifs (correction du nom, K19)** : des lemmes existants renommés, et d'autres énoncés sur un type isomorphe (K18). Tous doivent être retrouvés. Leur taux mesure le rappel de la recherche.

**Vrais négatifs** : des énoncés faux, avec contre-exemple, et un type voisin non impliqué. Aucun ne doit être déclaré présent ou fermé.

**Formulation du verdict** : « non trouvé sous les encodages et budgets testés, PR publiques à la date d ». Jamais « neuf » (K20).

**Falsification**
- Issue 1 ou 2 : H_A est falsifiée.
- Issue 3 avec des positifs tous retrouvés : H_B est falsifiée.
- Positifs isomorphes manqués : le verdict d'absence est déclaré non fiable pour cet encodage.

**Contrainte.** Je ne sais pas si la consultation d'une bibliothèque formelle tombe sous le gel de la veille.

### E2′ : la cartographie de zone protège-t-elle mieux qu'une seconde recherche ciblée ?

**Bras, en parallèle, sur les mêmes cibles**, avec une indépendance assurée selon K15 :
- (i) examen ciblé ;
- (i′) second examen ciblé indépendant, à budget égal à (ii) ;
- (ii) cartographie seule ;
- (ii-placebo) même effort, sur une zone sans rapport avec les cibles.

Chaque alerte est adjugée par implication, à l'aveugle quant au bras.

**Statistique.** Comparaison appariée des paires discordantes entre (ii) et (i′) : b collisions trouvées par (ii) seule, c par (i′) seule. Le taux du placebo est soustrait.

**Hypothèses**
- **H_A** : b − c dépasse la marge du placebo.
- **H_B** : b − c ne dépasse pas la marge du placebo.

**Falsification**
- H_A retenue : H_B est falsifiée. La largeur protège mieux qu'une relance ciblée.
- H_B retenue : H_A est falsifiée. Le surplus éventuel de (ii) sur (i) n'était que l'effet d'un second passage. Un second passage capture en effet une fraction (1 − r)·r de ce que le premier a manqué, selon le calcul de E.

**Limite annoncée.** Avec peu de collisions réelles, l'issue « pas de verdict » est probable. Dans ce cas, la cartographie n'est justifiée que pour choisir les cibles, pas pour les protéger (K14).

### E1′ : l'agent détecte-t-il les collisions non littérales ?

Expérience déclassée, conditionnelle au budget d'experts.

**Plan**
- **Strates** : littéral, traduction, généralisation (folklore retiré, K7), croisées avec l'accès au texte (accès égalisé, K1).
- **Bras** : livre ouvert et livre fermé (K2).
- **Construction** : un expert X construit les traductions sans avoir vu mon lexique du §1.3. Les reformulations fournies à l'agent viennent d'une autre source (K5). Les jumeaux sont certifiés selon K3, l'adjudication est faite par Y (K4), et des familles sont réservées au test (K10).

**Hypothèses** (verdict pris dans la strate à accès égalisé)
- **H_A** : les trois conditions suivantes tiennent.
  - Le rappel non littéral se distingue des fausses alertes : r_T − f est au-dessus d'un plancher absolu (K8).
  - L'écart au littéral reste dans la marge : r_L − r_T ≤ m.
  - Le livre ouvert fait mieux que le livre fermé.
- **H_B** : r_L − r_T > m, ou bien r_T − f est sous le plancher.

**Falsification**
- H_A retenue : H_B est falsifiée. On peut confier davantage la recherche non littérale à l'agent.
- H_B retenue : H_A est falsifiée. L'option (a) « par un agent » ne couvre pas les collisions non littérales.
- Livre fermé ≈ livre ouvert : on mesure de la mémoire, sans valeur pour les travaux postérieurs à la coupure.

**Contrôles**
- **Classifieur de surface (K6)** : un classifieur qui ne voit que des traits de surface (longueur, distance d'édition) ne doit pas séparer appâts et jumeaux. S'il les sépare, le banc est reconstruit.
- **Pièges de citation (K22)** : des passages exacts qui n'impliquent pas la cible.

**Effectif.** Dans le pire cas (p = ½, non apparié), une marge m = 0,3 (illustratif) demande de l'ordre de la centaine d'appâts par strate (illustratif) pour qu'un intervalle à 95 % tienne d'un seul côté. C'est très au-delà des « dix paires par zone » de ma conception, et la critique de C est fondée. Si le budget d'experts ne le permet pas, E1′ n'est **pas** exécutée comme un duel. On publie seulement des intervalles descriptifs, sans en tirer de décision.

### E0 : audit sur des cibles réelles (réponse à K25)

**Protocole.** On tire des candidates au sort parmi les cibles réelles. Deux procédures indépendantes les examinent.
- **P1** : agent et recherche documentaire.
- **P2** : deux experts de communautés différentes, sans accès aux résultats de P1.

**Hypothèses**
- **H_A** : P2 trouve des collisions adjugées que P1 manque.
- **H_B** : aucune collision trouvée par P2 n'est manquée par P1.

**Falsification**
- H_A retenue : le rappel de P1 sous la loi de déploiement est inférieur à 1. Toute politique fondée sur P1 seule est falsifiée.
- H_B retenue : il n'y a aucun signe de manque.

**Estimation.** Une estimation par capture–recapture du nombre total de collisions est possible (RAPPORTÉ, connaissance générale de la méthode). Elle suppose des captures indépendantes. Des angles morts communs aux deux procédures la font sous-estimer. Avec peu de collisions, elle ne donne guère plus qu'une borne inférieure. Je le dis d'avance.

---

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi**

- **Par le dossier (RAPPORTÉ, non audité).**
  - La veille est gelée.
  - Une bibliothèque Lean couvre une part du vocabulaire.
  - Des travaux de 2026 ont été croisés sans être lus.
  - Les cibles sont à budget égal et toutes rapportées.
  - Une collision tardive coûte cher et la lecture coûte de l'effort, mais aucun de ces coûts n'est chiffré.
- **Par raisonnement, sous des modèles explicités par les critiques.**
  - Un seuil « au moins une collision » est franchi par les seules fausses alertes.
  - Un protocole séquentiel favorise le second passage.
  - Un écart relatif de rappel valide un instrument faible.
  - Aucun des bancs proposés n'estime le rappel en déploiement.

  Ce sont des résultats sur la méthode, pas sur le pilier.
- **Une déduction de A, que je reprends.** Puisque les cibles sont à budget égal et toutes rapportées, vérifier seulement au moment de la revendication protège la revendication, pas la dépense. Cela affaiblit l'option (b) comme politique unique.

**Ce qui n'est pas établi**

- Le taux de collision π.
- Le rappel de n'importe quel instrument, agent, juge ou humain.
- La fréquence des types de collision. C'est mon hypothèse (i), sur laquelle reposait ma recommandation ; elle n'était testée par aucune de mes expériences (K11).
- Que la cartographie protège mieux qu'une seconde recherche ciblée.
- Que la liste soit ou non scellée.
- Que le gel puisse être levé.
- La disponibilité des experts.
- Les coûts.

**Recommandation : l'option (d) révisée**

1. **En premier : E4′.** Lire la pile croisée contre les cibles candidates, avec le critère d'implication et un négatif apparié. Il faut une exception au gel, bornée à cette pile.
2. **En routine : E3′** sur chaque lemme, avant toute dépense.
3. **Pour chaque énoncé, au scellement** : une recherche ciblée avec reformulations venues de sources distinctes, et la question d'un expert.
4. **La cartographie de zone** sert à choisir les cibles. Elle n'est justifiée comme protection que si E2′ tranche en sa faveur.
5. **E1′** n'est lancée que si le budget d'experts atteint l'effectif nécessaire. Je retire le « lancer E1 tout de suite » de ma conception.
6. **À la revendication** : E0 sur un échantillon, plus un relecteur externe. La formule est « non trouvé selon le protocole P ».

**Pourquoi E4′ en premier.** C'est la seule expérience bon marché dont une issue change une décision immédiatement : une cible réglée est une dépense évitée. Son négatif apparié dit en outre si le danger tient à la pile ou à toute la zone.

**Ce qu'elle coûte.** Du temps humain de lecture et d'adjudication, que je ne sais pas chiffrer.

**Ce qu'elle suppose.** Une exception au gel, deux lecteurs disponibles, et une liste candidate existante.

**Ce qui ferait changer la recommandation**

| Issue | Changement |
|---|---|
| E4′ règle une cible, et le négatif apparié aussi | Lecture large de la zone avant scellement : une version locale de l'option (a). |
| Seule la pile règle une cible | Replanifier cette zone seulement. |
| Ni la pile ni le négatif ne règlent de cible | Les étapes 2 à 6 suffisent jusqu'à E0. |
| E0 montre des manques de P1 | Davantage d'humains ; pas d'élargissement de l'agent. |
| Le gel est maintenu | Option (b), plus E3′, plus un expert par énoncé, avec le risque écrit. |

**Ce qui est réfutable dans cette réponse.** Ma recommandation repose désormais sur une hypothèse testable par E4′ : la pile croisée et son voisinage contiennent des collisions avec les cibles actuelles. Elle repose aussi sur une affirmation de méthode : rien d'autre, à coût comparable, ne peut changer une décision avant la première dépense. C'est une HYPOTHÈSE, que je n'ai pas testée.

FIN-DE-CELLULE