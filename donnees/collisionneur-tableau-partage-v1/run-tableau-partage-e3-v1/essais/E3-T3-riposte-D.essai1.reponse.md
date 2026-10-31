## (a) Réponses aux critiques visant D

*Tous les nouveaux seuils, effectifs, découpages et ordres de grandeur ci-dessous sont illustratifs. Les objections identiques sont regroupées, sans en fusionner les corrections.*

| Critique | Décision | Réponse et correction |
|---|---|---|
| **A, B, C — « non évité » est décidé a priori et aucune issue ne le réviserait.** | **Acceptée.** | Je distingue l’existence d’un chemin de texte, qui est une propriété du protocole, et l’ampleur de son effet, qui est mesurable. Les verdicts deviennent : **évité sous condition** si les critères réservés sont satisfaits avec une puissance suffisante ; **non évité** si un effet ou une fuite dépasse les marges ; **non jugeable** si la précision manque. Un résultat non significatif ne vaut pas évitement. |
| **B — l’argument sur les instructions glissées vaut aussi pour le minimal et la question.** | **Partiellement acceptée.** | Oui : la distinction donnée/consigne n’est pas propre au complet. Mais le complet ajoute une **écriture libre**, puis une diffusion à d’autres proposeurs, chemins absents du minimal. La même batterie de plantations doit donc mesurer A, B et C, sans présumer que seul B est exposé. |
| **A, B, C — \(D=\exp(H)\) est redondant avec \(I\), aveugle aux rapprochements sans doublon et dépendant du graphe.** | **Acceptée.** | Je retire \(D\) comme mesure de diversité. \(I\) reste le nombre de composantes du graphe des doublons. La diversité devient \(D_s\), une **distance continue entre fiches**, indépendante de ce graphe : proximité ordonnée par lecteurs aveugles sur toutes les paires d’une case, avec mesure lexicale secondaire appariée en longueur. Des paires plantées de proximité connue et des paires honnêtes de même case servent de calibration. |
| **A — les parts de jetons confondent prolifique et coût.** | **Acceptée.** | Le poids du prolifique porte sur les entrées effectivement servies et lues, puis sur les idées. Les jetons sont une dépense, non une mesure de domination. Les budgets par proposeur sont égalisés ou leurs écarts consignés. |
| **C — l’attribution fractionnaire récompense une fusion tardive avec les idées d’autrui.** | **Acceptée, transformée en test.** | Attribution principale au premier dépôt daté de la composante ; attribution fractionnaire en analyse de sensibilité ; comparaison avec une attribution limitée à la passe 1. Un écart entre les trois est rapporté, non arbitré silencieusement. |
| **A, C — le coût des lecteurs humains et leur fatigue sont omis.** | **Acceptée.** | Le coût de production et le coût de mesure sont séparés, puis additionnés dans un coût total rapporté. Ordre de lecture aléatoire, paires d’étalonnage insérées à l’aveugle et analyse de dérive selon le rang de lecture. Si ce coût rend le pré-pilote non réduit, le nombre de cases est réduit avant de sacrifier la vérité terrain. |
| **A — « douze courses » et « douze cases » se contredisent ; réglage et évaluation n’ont pas de parts.** | **Acceptée.** | L’unité principale est la **case texte×bras**, appariée entre conceptions ; la course est l’unité d’agrégation lorsqu’elle contient plusieurs cases. Réglage et évaluation sont séparés par courses entières et par jeux de plantations avant toute lecture des résultats. Aucun effectif fixe n’est conservé sans calcul de puissance. |
| **A — bootstrap par proposeur dégénéré avec peu de proposeurs.** | **Acceptée.** | Supprimé. Les fiches ne sont jamais traitées comme indépendantes. Analyse par randomisation appariée au niveau case/course ; agrégation des sorties d’un même proposeur à l’intérieur de sa case. Avec trop peu de cases, estimation descriptive seulement. |
| **A — marge de qualité \(\pm0,1\sigma\), témoins \(\pm2\) points, cibles de détection et fausses alertes inaccessibles aux effectifs proposés.** | **Acceptée.** | Toutes ces cibles fixes sont retirées. Marges d’équivalence et effectifs sont définis ensemble, avant évaluation, à partir de la variance pilote et de la résolution discrète des témoins. Pour zéro événement, je rapporte la borne binomiale supérieure plutôt que « zéro risque ». Sous-effectif : **non jugeable**, jamais victoire de \(H_B\). |
| **A, B — les deux cibles d’une courbe ROC sont posées sans démontrer qu’un point les satisfait.** | **Acceptée.** | Seuil et effectif sont réglés sur la partition de réglage ; la partition réservée estime conjointement sensibilité, fausses alertes et intervalles. Le taux de quarantaine et le nombre de fiches encore jugées sont obligatoirement rapportés. |
| **A, B, C — \(\kappa\geq0,8\) rend l’estimand indisponible précisément lorsque les doublons sont rares.** | **Acceptée.** | Le \(\kappa\), avec sa prévalence et son intervalle, devient descriptif. Je rapporte aussi accord brut, accords positifs et négatifs, et performances sur paires connues. Deux lecteurs examinent chaque paire ; le troisième tranche les désaccords. L’estimand n’est suspendu que si la calibration montre que les lecteurs ne distinguent pas les paires connues. |
| **A — l’audit de rôle « compatible avec le hasard » ne peut pas échouer à petit effectif.** | **Acceptée.** | Validation croisée séparée par course, classifieur étalonné sur rôles connus, contrôle par permutation des étiquettes et fiches sans rôle. Le critère porte sur la **borne supérieure** de la performance de prédiction ; sinon l’audit est non jugeable. |
| **A — le recouvrement tableau/fiches alerte par construction sur les entrées tirées des fiches de passe 1.** | **Acceptée.** | Pour les entrées dérivées d’une fiche, la correspondance avec leur fiche source est exclue. Les entrées libres restent comparées à toutes les fiches, y compris celles de leur auteur. La recherche exacte de la chaîne inerte demeure séparée du recouvrement approché. Un tableau fantôme non servi estime le recouvrement fortuit dans les cases sans tableau. |
| **A — « zéro fuite » peut être obtenu par quarantaine massive.** | **Acceptée.** | Contrôle négatif sur fiches honnêtes sans tableau et sans plantation ; publication conjointe des fuites, fausses alertes, quarantaines, fiches validées et attrition. Aucun duel ne compare \(I\) sans rapporter cette attrition. |
| **A — les contrôles A minimal et contexte inerte de même longueur manquent.** | **Acceptée.** | La convergence de B est comparée d’abord à **A**, non au seul vide. Une condition A avec contexte inerte de longueur appariée sépare l’allongement du contexte de l’information servie. Des doublons et proximités plantés par un tiers vérifient que les instruments détectent bien une activation du mécanisme. |
| **B, C — C contre B confond lecture entière et écriture typée ; la dépense est parfois imposée, parfois présentée comme résultat.** | **Acceptée.** | La dépense est **imposée égale en dollars** dans l’analyse principale et mesurée en jetons ; elle n’est plus une condition de victoire de C. J’ajoute C-R : lecture réduite aux titres et résumés avec la même écriture typée, ainsi que C sans écriture. Ces contrôles distinguent lecture, écriture et dépense. |
| **C — détection amont et prise aval sont confondues ; si rien n’est servi, la prise est indéfinie.** | **Acceptée.** | La garde est évaluée sur l’admission des entrées. La propagation n’est estimée que parmi les entrées effectivement servies, avec garde activée et désactivée sur partitions distinctes. Aucune entrée servie signifie « prise non estimable », pas « prise nulle ». |
| **A, B — les nombres d’éléments de code n’ont pas d’unité commune et la liste est dite close tout en restant à confirmer.** | **Acceptée sur la comparabilité.** | L’unité devient un chemin ou une transformation nouvelle, avec schéma, test et empreinte associée. Le noyau existant est réutili­sé selon le **fait 2** ; les faits **7–8** restent des principes, et le **fait 9** interdit de compter leur code comme repris. La liste minimale comprend extraction, schéma/bornes, service journalisé et nouveaux tests d’isolation ; le complet ajoute stockage/permissions, ordonnancement/quotas, garde des entrées libres et instrumentation de propagation. Le test d’isolation est nouveau, sans prétendre recoder la barrière de service des juges. Si la contre-lecture révèle un chemin non listé, la liste n’est pas close et le verdict est **non évité**. |

## (b) Expériences corrigées

### Plan commun et instruments

Les conceptions sont appariées sur les mêmes textes×bras, avec composition des proposeurs et configuration des juges figées. Les passes, gabarits et nombres maximaux de fiches sont identiques. Les témoins ne sont interprétés que si leur forme et leur longueur sont appariées ; les témoins courts de la course 1 ne peuvent pas fournir ce contrôle, et les témoins comparables sont seulement **RAPPORTÉS en attente**.

- **Idées :** toutes les paires d’une case sont lues à l’aveugle ; \(I\) est le nombre de composantes connexes, sans employer automatiquement \(N-\text{paires}\). Les cycles, arêtes incertaines et sensibilité à leur retrait sont rapportés. Le détecteur automatique ne décide pas de la vérité terrain.
- **Diversité :** \(D_s\) est la distance continue moyenne intra-case, indépendante du graphe. Les mesures lexicales sont secondaires et corrigées de la longueur.
- **Dépense :** dollars et jetons de production sont rapportés séparément ; le coût humain de mesure est ajouté dans un second total. Les contrôles à jetons inertes empêchent qu’une inflation du dénominateur tranche seule un duel.
- **Doublons :** plantations tierces et doublons naturels intra-proposeur, paires honnêtes de même case et même proposeur, base mécanique de recouvrement à battre, évaluation réservée.
- **Instructions glissées :** entrées honnêtes appariées avec et sans plantation tierce ; chaîne inerte présente sans instruction comme contrôle de recopie fortuite ; admission et propagation mesurées séparément. La chaîne ne règle jamais la garde.
- **Séparation juge :** recherche exacte de la chaîne, recouvrement sur le texte propre au tableau, exclusion de la seule auto-correspondance dérivée, inclusion de l’auto-recopie libre. Une injection mécanique de trace dans une copie d’évaluation sert de contrôle positif du détecteur. Reconnaissance des témoins mesurée comme taux, non comme score.

### Duel 1 — tableau complet B contre tableau minimal A

- **\(H_A\) :** à budget en dollars égal, B procure un gain minimal préenregistré d’\(I\) par dollar, sans non-infériorité manquée sur \(D_s\), sans dégradation de sécurité et, si son usage est permis, avec qualité jugée équivalente.
- **\(H_B\) :** B ne procure pas ce gain minimal, ou l’une de ces non-infériorités est démentie.
- **Contrôles :** A, A avec contexte inerte de même longueur, et condition sans tableau pour les taux de base des instruments.
- **Issues :** établir \(H_A\) falsifie « le minimal conserve tous les bénéfices mesurés » ; établir \(H_B\) falsifie « le complet apporte un bénéfice net minimal ». Précision insuffisante : duel non jugeable, sans attribution à \(H_B\).
- **Dépendance :** randomisation appariée par case ; agrégation par course ; aucune fiche ni paire traitée comme observation indépendante.

### Duel 2 — tableau intermédiaire C contre B

- **\(H_A\) :** C est non inférieur à B pour \(I\) et \(D_s\), tout en réduisant la propagation résiduelle ou les quarantaines indues, à dépense mesurée et sans prétendre qu’une réduction de coût est acquise.
- **\(H_B\) :** C perd davantage que la marge sur \(I\) ou \(D_s\), ou n’améliore aucun des deux indicateurs de sécurité.
- **Contrôles factoriels :** C-R pour réduire la lecture sans changer l’écriture ; C sans écriture pour mesurer la seule lecture ; mêmes plantations et mêmes partitions réservées.
- **Issues :** \(H_A\) falsifie « la prose libre est nécessaire aux bénéfices de B » ; \(H_B\) falsifie « l’écriture typée conserve ces bénéfices tout en améliorant la sécurité ».

### Duel 3 — rôles

- **\(H_A\) :** les rôles tirés au sort améliorent \(I\) et \(D_s\) par unité de dépense par rapport à l’absence de rôle, avec un effet supérieur à celui des étiquettes sans consigne.
- **\(H_B\) :** il n’existe pas d’effet spécifique minimal, ou l’effet est défavorable.
- **Contrôle négatif :** étiquettes seules ; l’auto-attribution sur le tableau reste une condition distincte, non mélangée au tirage au sort.
- **Contrainte du fait 13 :** aucune note de juge ne choisit les rôles. Les témoins vérifient seulement la stabilité du juge. L’audit de fuite du rôle utilise la procédure corrigée ci-dessus ; son impuissance ne valide pas l’anonymat.

## (c) Page de réponse à l’arbitre

### Ce qui est établi

**VÉRIFIÉ :** le noyau valide, caviarde, anonymise et sert les deux passes aux juges ; les deux passes sont jugées ensemble (**fait 2**). Le calcul \(29-12=17\) n’est exact que sous la condition d’acyclicité précisée au **fait 4**. La mémoire du pôle fournit un précédent de conception, non un code réutilisé par la course (**faits 7–9**). Le choix des rôles ne peut pas reposer sur le verdict du juge (**fait 13**).

**RAPPORTÉ :** les comptes de la course 1, les douze paires et les dix-sept idées ne sont pas des sorties relues ici ; l’explication par l’oubli de la passe 1 n’a pas été éprouvée. Le tableau minimal est la décision par défaut ; les trois écueils et la demande d’échange sont rapportés (**faits 3, 5 et 6**).

### Décision à rapporter

**Décision et enjeu.** Maintenir **A, le tableau minimal**, tant que les mesures réservées ne démontrent pas qu’une conception plus ouverte conserve les idées, la diversité et la séparation du juge sans surcroît accepté ; l’enjeu est d’ajouter des chemins de texte sans confondre bénéfice collectif et défaut de mesure.

- **A — avantage :** chemins et revue supplémentaires les plus limités. **Inconvénient :** échange et rôles collectifs faibles.
- **C — avantage :** lecture riche et écriture typée. **Inconvénient :** recopie possible, coût de lecture et facteurs encore à isoler.
- **B — avantage :** échange et attribution de rôles possibles. **Inconvénient :** sécurité non établie et liste de code la plus étendue.

**Recommandation : A maintenant ; C ou B seulement après les conditions ci-dessous. Confiance moyenne**, limitée au maintien du défaut : les sorties de course et la règle actuelle du détecteur ne sont pas relues, et aucun résultat comparatif n’est disponible.

- **Influence croisée :** mesure appariée contre A de \(I,D_s\), attribution du prolifique, traces tableau→juge, attrition et reconnaissance des témoins ; toutes doivent être jugeables et dans leurs marges.
- **Instructions glissées :** sensibilité et fausses alertes sur évaluation réservée, puis propagation conditionnelle aux entrées servies, avec garde active/inactive et contrôles négatifs.
- **Surcroît de code :** liste close par contre-lecture, tests et empreintes scellés ; acceptation expresse du directeur. Une liste non close impose « non évité ».

**Restent HYPOTHÈSE :** la généralisation des plantations au texte libre ; l’exemption des conceptions A/B/C de la règle du fait 13 ; la substitution d’\(I,D_s\) et de la dépense à l’oracle absent pour les rôles ; la conservation des bénéfices collectifs par les entrées typées. Si la première exemption tombe, les notes des juges sont rapportées comme information et ne départagent pas les conceptions.

**Expérience à faire en premier :** le pré-pilote instrumental apparié, avec partitions de réglage et d’évaluation, doublons naturels et plantés, traces mécaniques, témoins appariés et A comme contrôle ; le duel B contre A n’est lu que si ces instruments sont jugeables.

FIN-DE-CELLULE