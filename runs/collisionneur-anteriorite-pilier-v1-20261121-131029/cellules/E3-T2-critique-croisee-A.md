# Proposition A : Tour III.2, critique croisée de méthode

**Pièces.** B, C, D et E sont présentes et vont chacune jusqu'à leur ligne de fin, sans coupure visible. Je n'ai pas vérifié les empreintes sha256. Ma propre conception du tour III.1 ne m'est pas retransmise : je n'en cite rien.

**Statuts.** Le bloc FAITS ne porte aucun statut explicite ; je le cite comme donnée du dossier, non auditée par moi. Mes critiques sont des HYPOTHÈSES d'analyse. Les formules sont des identités sous un modèle que je pose, et ce modèle est lui-même une HYPOTHÈSE. Tout chiffre est illustratif.

**Portée.** La question de l'arbitre (quand lire, et sur quelle étendue) sert ici d'étalon : je juge si les mesures proposées peuvent la trancher. Le livrable est celui du tour.

**Notation, pour le point (b).**
- π : probabilité qu'une cible candidate soit en collision.
- r : probabilité d'alerte sachant collision ; φ : probabilité d'alerte sachant absence de collision, par couple (cible, voisin).
- n : taille d'un banc ; N : nombre de cibles ; k : nombre de voisins examinés par cible.
- P_banc : loi des cas du banc ; P_dépl : loi des cas rencontrés en déploiement.

---

## Sur la proposition B

### (a) Défauts de méthode

- **E1 confond le type de collision et l'accès au texte.** B écrit que les collisions de traduction vivent dans des littératures anciennes, hors arXiv, parfois payantes. La chute de rappel entre littéral et non littéral mélange donc deux causes : l'agent ne rapproche pas, ou l'agent n'a pas obtenu le texte. Les deux appellent des remèdes opposés (plus d'humains ou plus d'accès).
- **E1 confond recherche et mémoire.** Les appâts sont des résultats connus et publiés, donc probablement présents dans les corpus d'entraînement de l'agent. Le rappel mesuré peut venir de la récitation. Or le dossier désigne comme collisions redoutées des travaux de 2026 non lus, où cette mémoire est probablement absente.
- **Le quasi-jumeau a une étiquette fragile.** Il est « jugé non trouvé » par l'humain qui construit le banc. Une alerte de l'agent sur un quasi-jumeau est comptée comme fausse alors qu'elle peut être une vraie collision que l'humain ignorait. B le signale comme limite, mais sa métrique de fausses alertes en dépend entièrement.
- **E2 est positif ou nul par construction.** On compte les collisions trouvées par la cartographie « mais non » par l'examen ciblé. La quantité inverse n'est pas comptée, et l'ordre est fixe (examen, puis cartographie, sur les mêmes cibles). La cartographie arrive en second, avec un effort cumulé supérieur. Le surplus mesure donc aussi l'effort et l'ordre, pas seulement la largeur.
- **E4 est presque vrai par construction.** Les travaux de 2026 ont été remarqués parce qu'ils paraissaient voisins. « Recoupe une zone prioritaire » est donc acquis par la sélection. Seul « règle une cible, avec le passage et l'implication » serait informatif.
- **E3 fusionne deux événements dans H_B.** « Présent ou en PR » et « fermé automatiquement » n'ont pas la même conséquence. B distingue d'ailleurs lui-même la nouveauté de bibliothèque et la nouveauté mathématique dans son tableau du §3.
- **Fuite sur le juge.** Le juge est évalué sur « les mêmes appâts » que l'agent. Si ces appâts servent aussi à régler les requêtes ou les reformulations, le rappel devient un rappel d'apprentissage.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Seuil de 30 points d'E1.** Avec n appâts par type, l'écart-type de la différence de deux proportions est au plus √(1/(2n)). Pour n = 10 (l'ordre de grandeur que B avance, illustratif), il vaut environ 0,22. Un écart de 30 points est alors à moins d'un écart-type et demi de zéro. Le duel n'est pas jugeable tant que n par type ne garantit pas un écart-type nettement inférieur au seuil.
- **Biais de sélection du banc.** L'estimateur de r est une moyenne sous P_banc, loi des collisions déjà découvertes par quelqu'un. Si la détection dépend d'une covariable x (notoriété, accès, distance de vocabulaire, date par rapport à la coupure du modèle) et si P_banc(x) ≠ P_dépl(x), l'estimateur est biaisé. Si le support de P_dépl n'est pas couvert par P_banc, aucune repondération ne le corrige.
- **Seuil « au moins une collision » d'E2.** Sous π = 0, la probabilité d'au moins une alerte sur m cibles vaut 1 − (1 − φ)^m. Pour φ = 0,1 et m = 10 (illustratif), elle vaut environ 0,65. H_A serait retenue par les seules fausses alertes. Le critère n'a de sens que si chaque collision comptée est adjugée par une réduction vérifiée.
- **Accord entre deux relecteurs.** L'accord estime la corrélation de leurs verdicts, pas r. Deux relecteurs de la même communauté peuvent avoir un accord proche de 1 et un r proche de 0 sur les collisions de traduction.
- **E3.** La probabilité de fermeture croît avec le budget de temps t. Sans courbe en t, le verdict « non fermé » décrit t, pas le lemme.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Livre fermé.** Le même agent, sans accès aux documents, sur les mêmes appâts. Sa détection mesure la mémoire. Sans ce bras, E1 ne dit rien sur les travaux de 2026.
- **Accès égalisé.** Une strate où appâts littéraux et non littéraux ont leur source également accessible en texte intégral. Sans elle, « il faut des humains » ne découle pas d'un rappel faible.
- **Cartographie placebo pour E2.** Le même effort, sur une zone sans rapport avec les cibles, doit écarter zéro cible. Sinon le surplus mesure φ multiplié par l'effort.
- **Négatif proche pour E4.** Un article de 2026 de la même zone, non issu de la pile croisée. Le négatif de B (article hors pilier) est trop lointain pour échouer.
- **Vrai négatif pour E3.** Des lemmes dont l'absence et la non-dérivabilité sont certaines, par exemple des énoncés faux. Les « lemmes existants renommés » de B sont un contrôle positif, malgré leur nom.

---

## Sur la proposition C

### (a) Défauts de méthode

- **Le « canari » affirme une « antériorité certaine ».** Si le modèle récite une preuve ou une citation, C conclut que la cible est connue. Une citation produite par un modèle n'est pas une source : il faut retrouver le document et vérifier l'implication. Dans l'autre sens, le silence du modèle ne dit rien. La sonde est au mieux un générateur de pistes.
- **L'expérience 1 estime π avec l'instrument qu'elle doit justifier.** p_coll est le taux de cibles « invalidées » par la lecture. Sous mon modèle, son espérance est πr + (1 − π)φ, avec r et φ inconnus. La comparaison à τ₁ porte donc sur un mélange de π et de la qualité de l'instrument.
- **Le seuil τ₁ = C_lect / B_cible omet le coût après revendication.** C distingue pourtant ce coût dans sa supposition 5. Le seuil est trop haut, donc biaisé vers (b).
- **La bascule « si les agents échouent presque toujours » repose sur une erreur.** Le dossier dit que les cibles sont à budget égal et toutes rapportées. Le budget d'une cible déjà réglée par la littérature est donc dépensé, que l'agent réussisse ou non. Vérifier seulement les cibles réussies protège la revendication, pas la dépense.
- **Fuite entre construction et évaluation.** Les cas positifs du point (c) sont tirés des travaux de 2026. La recommandation 3 construit l'index d'empreintes à partir de ces mêmes travaux. Le rappel mesuré est alors conditionnel à la présence de l'antécédent dans l'index, sur des documents que l'instrument a déjà traités. Il ne dit rien des antécédents hors index.
- **Les graines de citations sont un échantillon de hasard.** L'hypothèse dite « de Markov » (les travaux de 2026 citent l'état de l'art pertinent) est précisément ce que B conteste pour l'actuariat et la recherche opérationnelle. C nomme ce mode d'échec dans son tableau, puis fonde sa recommandation dessus.
- **L'implication T_lit ⟹ T_cible peut être vide.** Les deux énoncés sont autoformalisés par le même modèle, puis T_lit est supposé. Si le T_lit formalisé est contradictoire avec la bibliothèque, tout s'en déduit et l'on obtient une fausse collision. Une erreur d'alignement commune aux deux traductions est invisible.
- **L'« aveugle inversé » induit la réponse.** La question posée au lecteur présuppose que le résultat est connu, ce qui pousse φ vers le haut. La règle « s'il échoue, la nouveauté est étayée » prend une absence pour une preuve, avec un r humain non mesuré.
- **L'exemption des objets à score est trop large.** Une table de meilleurs scores ne détecte pas qu'un objet publié atteint déjà le score cible sous un autre nom. D distingue ce cas, pas C.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Expérience 1.** Si π > τ₁ mais r < (τ₁ − (1 − π)φ) / π, l'expérience conclut à tort pour (b). Elle n'est jugeable que si r et φ sont estimés sur un banc indépendant et si l'intervalle de confiance de (p_coll − φ) / (r − φ) exclut τ₁. Avec peu de cibles, cet intervalle couvre τ₁ pour presque toute valeur de π.
- **Contrôle « détecter la totalité » des témoins.** Avec m témoins et un rappel vrai r, la probabilité de passer vaut r^m. De plus, les témoins choisis (Fano, Bretagnolle–Huber, Wald) sont parmi les plus connus, donc r y est proche de 1 par mémoire. Le contrôle passe presque sûrement et ne renseigne pas sur le r des cas de déploiement.
- **Expérience 2.** L'exactitude équilibrée sur des paires fournies estime la probabilité de bien juger une paire déjà formée. En déploiement, le rappel est le produit de cette probabilité par celle de retrouver le voisin dans un corpus de taille M. Si la seconde est faible, la première ne décide de rien.
- **Négatifs par modification d'une hypothèse.** Si les E₃ sont produits par une édition minimale, un classifieur qui détecte la trace d'édition les sépare sans rien comprendre aux mathématiques. Le contrôle n'a de puissance que si la loi des traits de surface est la même dans les deux classes.

### (c) Contrôles négatifs dont l'absence serait fatale

- **T_lit ⟹ Faux** doit échouer, et **T_lit ⟹ quasi-jumeau** aussi. Sans cela, chaque « collision par implication » peut être vide.
- **Canari sur des énoncés fabriqués après la date de coupure du modèle.** Le taux d'attribution à un auteur ou à un manuel y donne le φ de la sonde.
- **« Aveugle inversé » sur des énoncés dont la non-réductibilité est établie**, par exemple par un contre-exemple fini caché au lecteur, pour mesurer son taux de « connu » à tort.
- **Positifs dont l'antécédent est hors de la pile de 2026 et de ses citations directes.** Ils mesurent le rappel hors index, celui qui compte.
- Les « variantes obfusquées » que C appelle contrôle négatif sont un contrôle positif. Le vrai négatif (aucune alerte sur le quasi-jumeau) n'apparaît qu'au point (c), et pas dans l'expérience 1 où il manque.

---

## Sur la proposition D

D est la plus prudente sur l'asymétrie de la preuve et sur l'étiquette des négatifs (« ce voisin ne règle pas la cible », jamais « neuf dans le monde »). Je me sers de cette définition. Les défauts sont ailleurs.

### (a) Défauts de méthode

- **La perte dépend du traitement.** Dans le duel « Moment », le bras « lecture à la revendication seule » ne lit jamais pour les pilotes sans revendication. Une collision non lue n'y est pas observée, donc pas comptée. Le bras qui lit le moins paraît moins coûteux parce qu'il regarde moins. D prévoit un « même contrôle final » pour le duel « Largeur », mais pas pour « Moment ».
- **Le facteur équipe est confondu avec la politique.** Les équipes sont séparées et D ne prévoit ni croisement ni tirage au sort. D veut noter les transferts de solution, mais noter n'est pas neutraliser.
- **La lecture précoce modifie la cible.** Le bras précoce reformule ou retire des cibles avant scellement. Les deux bras ne résolvent plus les mêmes énoncés. D exige de conserver les fiches écartées, ce qui rend l'effet visible sans le rendre comparable.
- **Les poids de la perte décident du duel.** Ils sont fixés avec l'arbitre avant l'essai, ce qui est correct. Mais si le signe de la différence attendue change selon des poids également défendables, le duel teste les poids et non la politique.
- **L'imputation de la lecture mutualisée dépend de N.** Dans « Largeur », le coût amorti du balayage décroît avec le nombre de cibles, que le dossier ne donne pas. Le verdict est une fonction de N.
- **Erreurs communes à l'instrument et à son contrôle.** L'agent juge et le contrôle mécanique (« comparaison de champs normalisés ») partagent la même fiche extraite. Une erreur d'extraction touche les deux. Le gain mesuré est conditionnel à une extraction juste.
- **La date figée ne fige pas les poids du modèle.** Dans les dossiers rétrospectifs, un antécédent connu a souvent été cité avec sa cible dans des textes ultérieurs que le modèle a pu voir. La détection peut venir de cette co-occurrence.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Événement rare dans les duels.** Sur des portefeuilles à cibles identiques, le nombre K de cibles en collision suit une loi binomiale (N, π) et il est commun aux deux bras. Avec probabilité (1 − π)^N, K = 0. La différence de perte vaut alors exactement le coût de la lecture précoce, et la règle de D (« égalité ou surcoût réfute H_A ») réfute H_A quelle que soit la perte attendue. Le duel n'est jugeable que si N·π est assez grand pour que la variance de la perte, dominée par le terme rare et lourd de correction d'une revendication, laisse un intervalle hors du seuil. D reconnaît l'indétermination, mais sa règle de réfutation ne la protège pas.
- **Égalité ponctuelle.** H_B contient « perte égale », et « l'absence de gain établie » réfute H_A. Sans marge d'équivalence δ fixée d'avance, aucune taille d'échantillon n'établit une absence de gain, et H_A n'est pas réfutable.
- **Banc rétrospectif.** Même condition que pour B : l'estimateur de r est pris sous la loi des collisions découvertes. Il surestime r dès que la découvrabilité et la détection par l'instrument dépendent de la même covariable.
- **Fausses alertes par cible.** D mesure φ par dossier. En déploiement, la probabilité d'au moins une fausse alerte par cible vaut 1 − (1 − φ)^k. Un plafond fixé par paire ne borne pas le taux de retrait erroné d'une cible.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Audit final commun aux deux bras**, indépendant des deux politiques et au moins aussi large que la plus large, appliqué aussi aux pilotes sans revendication. C'est le contrôle décisif : sans lui, le duel « Moment » favorise le bras qui lit le moins.
- **Bras de délai sans lecture.** Même retard et mêmes heures de réécriture de la fiche, sans accès à la littérature. Il sépare l'effet de lire de l'effet d'attendre et de reformuler.
- **Livre fermé et antécédents postérieurs à la coupure du modèle** dans le banc rétrospectif.
- **Fiche extraite par un tiers** pour le contrôle mécanique, afin que l'instrument et son contrôle n'héritent pas de la même erreur.
- Le contrôle de D (voisins à incompatibilité vérifiée, que la politique large ne doit pas se voir créditer) est bon. Il ne couvre ni l'effet du délai ni l'observation inégale des collisions.

---

## Sur la proposition E

### Statuts : un écart à la règle 1

- E marque `[VÉRIFIÉ]` plusieurs affirmations qu'aucune pièce transmise ne vérifie. Exemples : l'isomorphisme entre fusion sous dépendance et bornes de copules, l'équivalence par dualité entre jeu d'inspection et frontière de test, l'égalité exacte des constantes pour de petits K, la non-homogénéité des critères d'antériorité. Je ne reprends pas ce statut : pour moi ce sont des affirmations de E, non auditées.
- Les années des références sont marquées `(illustratif)`. Une date de publication n'est pas un paramètre : elle est exacte ou « à vérifier ».
- Les noms et versions de modèles sont donnés de mémoire. E les marque comme illustratifs, ce qui est acceptable, mais ils ne doivent pas servir de devis.

### (a) Défauts de méthode

- **Fuite centrale entre l'instrument et ses négatifs.** Les quasi-jumeaux « réellement neufs » sont définis par une mutation qui change la valeur minimax calculée par LP sur petit alphabet. Or le « hachage par petites instances » fait partie du pipeline évalué, et aussi du contrôle mécanique de la ligne 6 du tableau. Tout instrument qui contient ce hachage sépare les négatifs par construction : son φ mesuré est nul par définition du banc.
- **« Réellement neuf » n'est pas établi.** Le LP montre que le jumeau muté diffère de son parent. Il ne montre pas qu'aucun autre résultat publié ne le règle. D évite cette erreur, pas E.
- **E2 dépend de la composition du banc.** L'index a priori est limité aux cinq zones. Le banc contient par construction des antécédents situés dans les « disciplines jumelles », hors index. Soit q leur part : ΔR = q·R_énoncé,hors + (1 − q)·(R_énoncé,dans − R_index,dans). Le premier terme est acquis par construction, et q est choisi par le constructeur du banc. Le seuil de 15 points s'atteint en réglant q.
- **E3 est circulaire.** E pose qu'une antériorité papier n'invalide pas un lemme de bibliothèque. Le « gain d'évitement de collision » de la lecture d'articles sur les lemmes est alors nul par définition, et H_A est vraie sans mesure.
- **E1 compare deux dénominateurs.** Le taux est mesuré parmi les premières revendications, et le seuil τ* est un seuil par cible. De plus, E1 consiste à exécuter l'option (b) sur un lot pilote, et les collisions y sont certifiées par le pipeline dont E veut établir l'utilité.
- **Le seuil de repli est un chiffre illustratif.** Faute de coûts, E propose « ≤ 10 % » et « zéro collision dans la pile de 2026 ». La décision reposerait sur un nombre que E déclare lui-même inventé, et sur une pile choisie par hasard.
- **Le relecteur est évalué sur un dossier que le pipeline a filtré.** Au temps 1 (iv), l'humain reçoit le dossier préfiltré, alors que le tableau lui donne le pipeline pour contrôle à battre. Son rappel propre est confondu avec celui du pipeline.
- **Réduction déductive et sonde de récitation.** Mêmes défauts que chez C : implication vide si l'axiome formalisé est incohérent, et attribution produite sans source.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E1.** Soit s₁ la probabilité de revendication sachant collision et s₀ sachant absence. Alors P(collision | revendication) = π·s₁ / (π·s₁ + (1 − π)·s₀). Sous l'hypothèse 4 de E lui-même (attraction vers le connu), s₁ > s₀ et ce taux dépasse π. Le test est biaisé contre H_B, donc en faveur de la recommandation de E. Il n'est pas jugeable si le nombre de revendications du pilote est petit.
- **Règle « un seul témoin manqué invalide ».** La probabilité de passer vaut r^m. Pour r = 0,95 et m = 20 (illustratif), elle vaut environ 0,36 : un bon instrument est rejeté. Pour r = 0,7 et m = 3 (illustratif), environ 0,34 : un mauvais instrument passe une fois sur trois. Le critère ne discrimine pas, il faut un intervalle sur r.
- **Hachage par constantes.** Sa puissance dépend de la loi des constantes dans le corpus. Si elle est concentrée sur quelques valeurs simples, la probabilité de coïncidence sans collision est élevée et φ aussi. Pour les énoncés asymptotiques sans constante, r est nul, ce que E admet.
- **Rappel@K.** À K fixé, il décroît quand la taille M du corpus croît. Mesuré sur un petit corpus de banc, il surestime le rappel sur les cinq zones et leurs jumelles.
- **τ\*.** Il contient c_collision, que le dossier ne chiffre pas. Tant que l'intervalle plausible de τ* contient le taux observé, aucune issue ne falsifie.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Négatifs indépendants du critère LP**, par exemple des voisins à incompatibilité vérifiée par lecture, à la manière de D. Sans eux, le φ du pipeline est nul par construction et le tableau (c) ne mesure rien.
- **Constantes permutées.** Apparier chaque cible aux constantes d'un article tiré au hasard donne le taux de base des coïncidences du hachage.
- **E2 à composition fixée de l'extérieur.** q doit être estimé sur des collisions réelles, pas choisi. À défaut, il faut rapporter les deux termes séparément et ne juger que la strate « dans les zones ».
- **Relecteur sur énoncé nu**, sans dossier, pour séparer son rappel de celui du pipeline.
- **Axiome ⟹ Faux**, livre fermé et énoncés postérieurs à la coupure, comme pour C.
- **E3.** Aucun contrôle ne répare un critère défini pour donner zéro. Il faut d'abord fixer, pour les lemmes et les objets, ce qui compte comme collision qui supprime la valeur du pilote.

---

## Ce dont je me sers, en le disant

- **De D** : la définition du négatif (« ce voisin ne règle pas la cible ») et l'exigence de conserver les cibles écartées.
- **De B** : la typologie des collisions comme strates de mesure.
- **De E** : l'hypothèse d'attraction vers le connu, utile, mais retournée ici contre son propre estimateur E1.
- **De C** : la distinction entre coût après dépense et coût après revendication, que sa propre bascule oublie.

**Constat par proposition, sans les fusionner.** Aucun des quatre bancs n'estime r sous P_dépl. Chacun l'estime sous la loi des collisions déjà découvertes, par une voie différente : appâts publiés chez B, théorèmes de la bibliothèque et pile de 2026 chez C, dossiers rétrospectifs chez D, jumeaux transposés chez E. Tant que ce point n'est pas traité, les seuils proposés départagent des instruments sur des cas faciles. La question de l'arbitre porte sur les cas qui ne le sont pas.

FIN-DE-CELLULE