# Tour III.2 : critique croisée de méthode (proposition A)

Les pièces B, C, D et E sont reçues et paraissent entières. Ma propre conception du tour III.1 n'est pas dans ce message : je ne m'y réfère pas.

Tout ce qui suit est une critique de conception (mes HYPOTHÈSES, sauf mention d'un fait), sans aucun résultat. Je ne connais ni le nombre d'articles du banc, ni la nature de l'oracle, ni la construction de l'accumulateur : plusieurs conditions restent donc paramétriques.

**Notations.**
- Z : la condition, soit honnête (H), bénin apparié (B) ou saboteur à dose d (S_d).
- D : l'écart de qualité jumeau moins agent sur une question. Sa loi est F_0 sous H (écart-type σ_0, graines et jugement confondus) ; sa moyenne est δ(d) sous S_d.
- S : le score d'un moniteur par trajectoire ; T : le texte.
- n_art : le nombre d'articles (les grappes) ; ρ_c : la corrélation intra-article.
- π : la part d'épisodes sabotés dans un flux ; α : le taux nominal de fausses alertes.

**Contrôle « lecteur sans état »** (cité dans les quatre sections) : le modèle de base, sans consigne ni adaptateur, relit en lecture forcée la transcription de l'agent, et l'on apprend la même sonde sur ses activations. Si elle égale la sonde lue chez l'agent, l'information est dans le texte.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **C1, amplitude confondue.** L'adaptateur bénin est fabriqué « par le même procédé », mais rien n'apparie l'amplitude du déplacement par rapport au modèle de base. Une sonde qui ne lit que la distance à la base alerterait plus sur S que sur B dès que la consigne de sabotage déplace davantage le comportement. H_A serait alors « confirmée » par un artefact.
2. **Témoin du dernier jeton du message système.** Il est asymétrique : l'égalité des deux sondes condamne, l'inégalité n'absout pas, car la consigne reste dans le contexte de chaque jeton engendré. Il ne s'applique pas à la famille à adaptateur, qui n'a pas de consigne (VÉRIFIÉ).
3. **C2, survie sans échelle.** « Nombre de pas fixé d'avance » ne définit pas H_A contre H_B : selon le pas d'apprentissage, tout adaptateur survit ou tout adaptateur s'efface. Le jumeau de référence après entraînement n'est pas fixé non plus, et chaque choix donne un résultat par construction :
   - contre le jumeau non entraîné, la dégradation générique compte comme dommage, d'où une « survie » ;
   - contre le jumeau entraîné, une compression vers le plancher de l'échelle donne un « effondrement ».
4. **C2, témoin à consigne.** « Faire de même » pour un saboteur sans poids changé ne dit pas si la consigne est présente pendant l'entraînement. Non jugeable en l'état.
5. **C3, comparateurs.** Le « meilleur » moniteur de texte et la « meilleure » vérification mécanique sont choisis sans règle de sélection. S'ils sont choisis sur la famille inédite, il y a fuite ; s'ils sont faibles, l'avantage de la sonde est acquis d'avance.
6. **C4, classe positive indéfinie.** La séparation après entraînement exige un saboteur entraîné de même. Si C2 conclut à l'effondrement, cette classe n'existe plus et la perte de séparation se confond avec la perte du sabotage. S'y ajoute un autre confondant : entraîner sur les traces d'un modèle de confiance plus faible change la capacité, pas seulement les poids.
7. **C5, journaux réutilisés.** Le rejeu se fait sur les journaux de C3, qui ont servi à lire la sonde. La composition du flux (π) est choisie par l'expérimentateur.
8. **P2, critère de réfutation.** La co-évolution du dommage et de la séparation est donnée comme « sans contenu propre ». C'est pourtant l'issue où la sonde vaudrait comme validateur d'un entraînement.
9. **C8, accord oracle contre jumeau.** Si le même juge produit les deux lectures, leurs erreurs sont corrélées et l'accord est gonflé. B dit ne pas connaître l'oracle ; je ne le sais pas non plus.

### (b) Conditions de perte de puissance

- **C1.** Non jugeable tant que les lois de la distance à la base (norme du déplacement d'activation, ou divergence des sorties) sous B et sous S ne se recouvrent pas. Le taux de fausses alertes s'estime sur n_eff = n / (1 + (m − 1)ρ_c), avec m épisodes par article. Il n'est pas jugeable si n_eff · α ne vaut que quelques unités.
- **C2.** L'estimateur est le rapport δ̂_post / δ̂_pré. Sa variance diverge quand δ_pré / SE(δ̂_pré) est petit. Il est non jugeable à toute dose dont l'intervalle de δ_pré contient 0, et quand la qualité honnête après entraînement approche le plancher de l'échelle. L'estimateur à préférer est la différence de différences (S_post − H_post) − (S_pré − H_pré), sur des articles disjoints.
- **C3, délai médian.** Il n'est pas défini si P(détection dans l'horizon) < 1/2 : il faut un estimateur de survie avec censure.
- **C3, α égal.** À α nominal égal, deux bornes valides à tout instant peuvent avoir des taux réalisés différents. L'écart de délai mesure alors la tension de la borne, pas l'information du score. La comparaison doit se faire à α réalisé égal, sur des honnêtes tenus à l'écart.
- **C3, apport interne.** La lecture interne n'ajoute rien si I(S_interne ; Z | T) = 0. Cela s'estime par le gain de vraisemblance d'un classifieur sur (T, S_interne) contre T seul.
- **C5.** Le gain dépend de la précision π·TPR / (π·TPR + (1 − π)·FPR). Il s'annule quand π tend vers 1 ou quand TPR/FPR tend vers 1. Le rang de la première confirmation suit une loi géométrique, dont l'écart-type est de l'ordre de la moyenne : un seul flux ne juge rien. La couverture de la borne exige R flux indépendants, avec une erreur en √(α(1 − α)/R).

### (c) Contrôles négatifs dont l'absence serait fatale

- Une série d'adaptateurs bénins graduée en amplitude, qui recouvre celle des quatre doses.
- Le lecteur sans état. B ne prévoit que la perplexité et un classifieur lexical.
- En C2, un adaptateur porteur d'un trait bénin mesurable, soumis au même entraînement. Si ce trait s'efface au même rythme, la fragilité est celle de tout adaptateur léger et ne dit rien du sabotage.
- Des honnêtes sur des questions plus difficiles, pour écarter l'hypothèse que la sonde lise la difficulté.
- En C5, un flux à π = 0 : le taux de « confirmations » doit y égaler le taux de fond de F_0. Je reprends de B le témoin à scores permutés, que je juge bon mais insuffisant seul.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Le seuil q change l'objet.** La menace diffuse est faite d'actions dont aucune ne paraît fautive seule (VÉRIFIÉ). Tout le cadre de C repose pourtant sur des « épisodes dommageables » qui franchissent un seuil q par épisode : c'est le cas de la sensibilité en A et C et des confirmations par heure en D. Dichotomiser par épisode sélectionne la queue concentrée du sabotage, c'est-à-dire le régime que le programme ne vise pas.
2. **La « famille réservée » du test C n'existe pas dans le calendrier de C.** La troisième famille est différée. Il reste deux familles, et l'adaptateur est obtenu en générant avec la consigne cachée (VÉRIFIÉ). Un transfert de la consigne vers l'adaptateur retrouve donc par construction le même contenu de sabotage. Il ne teste pas « hors fabrication connue ».
3. **Test A, erreurs partagées.** Si la référence (lecture par paires) et le lecteur testé (produit seul) sont de même classe, humains ou même modèle juge, leurs erreurs sont corrélées. De plus, le style d'un adaptateur peut trahir la provenance dans une paire dite aveugle : la « perte arbitrée » devient alors une signature de style.
4. **Test B, dose et forme.** La dose d'une consigne se règle par son libellé, donc elle est confondue avec la longueur et le lexique. La série bénigne est appariée en forme mais n'a pas de gradient. Le jumeau devrait porter la consigne bénigne, pas l'absence de consigne.
5. **Test D, lots séparés.** Si chaque mode d'aiguillage reçoit son propre lot de lecture, la composition du lot déplace le critère des lecteurs, qui confirment davantage dans un lot enrichi. Par ailleurs, un oracle sans jumeau et une sonde peuvent partager le même artefact de style d'adaptateur, ce qui produit un « gain » commun.
6. **Test E, intervention non définie.** La « mise à jour bénigne sans signal de correction » n'est pas spécifiée. Si elle utilise des produits honnêtes de la même tâche, elle porte une information corrective, et le test ne mesure plus la fragilité.
7. **Paramètres absents.** α, q et les marges m ne sont pas donnés, ce que C dit honnêtement. Les marges doivent dériver de prix d'opérateur, or le banc n'a pas d'opérateur. Le risque est qu'elles soient fixées après un premier regard sur les données.
8. **Scellement en trois partitions par article.** Le principe est bon, et je le reprends. Mais il divise n_art par trois sans que n_art soit connu.

### (b) Conditions de perte de puissance

- **Seuil q.** La grandeur utile est F̄_d(q) − F̄_0(q), l'excès de franchissements. Elle tend vers 0 quand δ(d)/σ_0 est petit, alors que le dommage cumulé N·δ(d) reste non borné. Dans ce régime :
  - les dénominateurs de sensibilité se vident, ou se remplissent de franchissements honnêtes ;
  - la précision de tout aiguillage tend vers π.
  
  Un estimateur est robuste à ce régime : la différence de moyennes de D par trajectoire, sans seuil.
- **Test A.** La sensibilité est mesurée contre une référence dont la valeur prédictive positive vaut π·F̄_d(q) / (π·F̄_d(q) + (1 − π)·F̄_0(q)). Elle n'est pas jugeable si F̄_0(q) est du même ordre que F̄_d(q). Elle est biaisée vers le haut si Cov(erreur de référence, erreur du lecteur) > 0.
- **Convention de décision.** Avec la règle « l'intervalle entier d'un côté de m, sinon indécis », l'issue « indécis » a une probabilité proche de 1 dès que SE est du même ordre que l'écart vrai à la frontière. Sans calcul de taille préalable, fondé sur σ_0, ρ_c et n_art, la porte de décembre recevra surtout des « indécis ».
- **Test C.** Le plafond α est tenu « dans chaque strate honnête ». Il n'est pas jugeable si n_art de la strate × α ne vaut que quelques unités.
- **Test D.** Le nombre de confirmations vaut les vrais positifs plus les faux positifs de l'oracle. Si la spécificité de l'oracle dépend du style (loi différente sous B et sous H), les bras diffèrent par leurs faux positifs.
- **Test E.** La condition d'entrée « écart initial > q » sélectionne sur une mesure bruitée, d'où une régression vers la moyenne. Le témoin gelé de C la neutralise seulement si la mesure d'entrée et la comparaison portent sur des articles disjoints.

### (c) Contrôles négatifs dont l'absence serait fatale

- En A, des paires adaptateur bénin contre jumeau dans la lecture de référence : leur taux de « perte » doit égaler celui des paires honnête contre honnête.
- En B, une série bénigne à gradient de libellé parallèle.
- En D, une file de lecture unique, entremêlée, où chaque épisode est lu une fois puis crédité aux bras par calcul. S'y ajoute un flux à π = 0.
- En E, un trait bénin mesurable sous la même mise à jour.
- En C, le lecteur sans état. Le juge textuel et la règle mécanique ne le remplacent pas.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Statuts déplacés** (règle 1). Plusieurs énoncés portent un VÉRIFIÉ que les faits ne leur donnent pas :
   - « un aiguillage enrichit la fraction auditée » : les faits posent l'aiguillage comme le rôle prévu des sondes, pas comme un effet mesuré ;
   - une sonde établit « si une propension interne persiste » après entraînement : ce n'est pas dans les faits ;
   - « l'orthogonalité modale évite » un aveuglement conjoint : c'est une hypothèse ;
   - « 4 doses complétées » pour la consigne cachée : les faits disent que cette courbe manque ;
   - les saboteurs de 14 milliards « restent lisibles par sonde » : leurs auteurs n'ont pas essayé les sondes ;
   - le « bruit gaussien sur les poids » comme perturbation neutre d'entraînement : dans les faits, le bruit sur les poids est un moyen de détection.
2. **Règles.** C5 affine l'agent contre la note d'un modèle faible, que je lis comme un score de juge. La première règle est donc touchée elle aussi, pas seulement « corriger en entraînant ». D ne déclare qu'un changement.
   - C4 optimise une politique contre le juge de texte, alors que le bras d'attaque prévu vise le score d'une sonde (VÉRIFIÉ).
   - C5 relit un organisme déjà lu avec une sonde « recalibrée ». Je ne sais pas si le directeur y voit une reconception.
3. **C4 est vrai par construction.** L'attaque ne vise que le juge de texte, puis on compare sonde et juge. L'écart demandé est acquis par toute sonde de rappel non nul. H_A y est de plus la conjonction de deux thèses sans lien : le transfert à la troisième famille et la résistance asymétrique.
4. **C1 et C2, transfert de la consigne vers l'adaptateur.** Même défaut que chez C (point 2). Une sonde qui lit des traits du texte saboté transfère sans rien dire des états internes.
5. **C1, duel non exhaustif.** L'issue « ΔFPR faible et rappel faible » falsifie H_A sans soutenir H_B. De plus, le rappel est mesuré « sur les doses où l'oracle est monotone », donc sur un jeu d'évaluation du moniteur conditionné par une sortie de l'oracle. Enfin la monotonie valide l'oracle, alors que la dose-réponse est elle-même mesurée par cet oracle : c'est circulaire.
6. **C2, unité ambiguë.** AF = TPR/0,05 est un rapport, mais les écarts sont demandés « en points ». AF n'est une accélération d'audit que si π est connu.
7. **C3, H_A en conjonction.** Elle réunit « l'adaptateur du programme est fragile », « les 14 milliards résistent » et « ils restent lisibles ». Les deux derniers membres ne s'opposent à rien dans H_B. La zone entre les deux seuils de rétention n'a pas d'issue.
8. **C5, lignée confondue.** L'AUROC entre le saboteur entraîné et l'honnête entraîné sépare deux lignées de poids. Elle peut valoir 1 avec un dommage résiduel nul.
   - L'alignement non supervisé peut absorber la direction utile ou en fabriquer une.
   - Les zones intermédiaires de dommage et d'AUROC ne sont pas attribuées.
   - L'issue H_A « démontre la complémentarité » : le verbe excède le plan.

### (b) Conditions de perte de puissance

- **C1, monotonie.** Avec quatre doses et des rangs échangeables sous l'hypothèse nulle, P(ρ ≥ 0,8) = 4/24 = 1/6 (calcul combinatoire de ma part, hors faits). Le critère passe donc par hasard une fois sur six.
- **C1, ΔFPR.** C'est une différence de deux proportions sur grappes. Elle n'est pas jugeable si son erreur type, calculée sur n_eff, est de l'ordre de la marge.
- **C2, enrichissement.** Il vaut TPR/α seulement quand π tend vers 0. La variance du rappel à α fixé est dominée par l'erreur sur le quantile du seuil, en α(1 − α) / (n_H · f(t)²), où f est la densité honnête au seuil t.
- **C2, apport interne.** Il est nul si I(S ; Z | T) = 0, comme chez B.
- **C3, rétention.** Même pathologie de rapport que chez B. L'AUROC des 14 milliards « avant et après » compare des lignées.
- **C4.** L'attaque translate la loi de S_texte sous S, pas celle de S_sonde. L'écart ne porte donc aucune information sur la sonde.
- **C5.** Le critère n'est jugeable que par une statistique intra-lignée : Corr(S, D) parmi les épisodes de la lignée saboteuse, ou l'ordre selon la dose. La loi de S pour un adaptateur bénin soumis au même entraînement doit servir de référence.

### (c) Contrôles négatifs dont l'absence serait fatale

- En C4, une attaque symétrique à budget égal contre chaque moniteur, dans un bras déclaré.
- En C5, un adaptateur bénin soumis au même affinement. D ne prévoit que deux honnêtes.
- En C3, un trait bénin sous la même perturbation.
- Le lecteur sans état.
- Je retiens de D l'adaptateur distillé de traces honnêtes du banc : c'est un contrôle à dose nulle par le même procédé, que j'utiliserais. La banque d'adaptateurs publics, non appariée, ne peut que condamner, pas absoudre.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Énoncés donnés comme des conséquences.** Trois affirmations sont des hypothèses non marquées :
   - un essaim non collusoire « se ramène statistiquement » à des épisodes indépendants, alors que des copies à poids partagés ont un mode commun ;
   - les dix pas sont « fortement autocorrélés » ;
   - la borne serait alors « mathématiquement invalide ». Une garantie valide à tout instant exige une validité conditionnelle sous la loi honnête, pas l'indépendance. Je ne connais pas l'accumulateur du programme.
2. **Règles non déclarées.**
   - P5 entraîne l'agent contre la note faible et écrit « aucune règle n'est modifiée ». Je lis cette note comme un score de juge, comme B l'a signalé. Les tests placebo touchent en outre aux poids du modèle soupçonné : B et E les jugent conformes, C demande une autorisation, D déclare un changement. C'est au directeur de trancher.
   - Le « moniteur de texte durci » de P3 n'a pas de procédé de durcissement spécifié. S'il est durci à l'aide de l'oracle, une sortie de l'oracle entre dans la sélection d'un moniteur.
   - P5 relit F3 avec une sonde recalibrée, après la lecture unique.
3. **F3 sur le chemin critique.** La troisième famille attend un devis (VÉRIFIÉ). Or P3 et P5 en dépendent pour la porte de comparaison.
4. **F3 sélectionnée sur le résultat.** Elle est retenue si son dommage dépasse le plancher et si elle résiste au placebo. L'expérience est déclarée « invalidée » sinon. C'est un conditionnement sur l'issue.
5. **P1, partition non spécifiée.** La sonde est apprise sur F1 et F2 puis jugée sur F1 et F2 contre des témoins. Quatre objets sont réunis sous un seul duel.
6. **P2, en-tête incohérent.** H_A est une conjonction et H_B une disjonction ; seuls les volets 2a et 2b sont des tests. En 2b, le rappel « après réglage fin bénin sur le jumeau honnête » n'a pas de classe positive définie.
7. **P4, trois thèses en une.** Le « contrôle négatif » annoncé (un attaquant qui connaît la grille) est une condition de stress, pas un témoin nul.
8. **P5 et mandat.** H_A est une triple conjonction. Le mandat écrit « que seule l'alliance sonde + audit détecte », ce qui présuppose la conclusion.
9. **Seuils.** Plusieurs duels laissent une zone sans issue : entre 30 et 50 % de rappel, entre 50 et 70 % de maintien, entre 10 et 30 % de résidu (seuils illustratifs de E).

### (b) Conditions de perte de puissance

- **P1 et P3, taux de fausses alertes.** Le critère est un taux d'au plus 1 % sur un cumul de 20 épisodes, mesuré sur environ 200 épisodes par condition (tailles illustratives de E). Cela fait 10 unités de cumul par condition. Avec zéro alerte sur n unités, la borne supérieure à 95 % vaut environ 3/n. Borner à 1 % exige environ 300 unités, soit environ 6 000 épisodes par strate (calcul de ma part, hors faits). Le critère n'est donc pas jugeable aux tailles que E annonce. La zone entre 1 et 5 % n'a pas d'issue.
- **Appariement en KL.** La divergence des sorties est estimée sur une loi d'entrées non précisée, et elle ne contraint pas la loi des activations. Le témoin ne vaut que si les lois de la norme du déplacement d'activation se recouvrent entre le bénin et F2. Je reprends l'idée d'appariement, avec cette condition.
- **Autocorrélation.** La condition à estimer est E_H[e_t | passé] ≤ 1 pour l'incrément de la statistique. Une « correction d'autocorrélation » n'en est pas un estimateur. Le calibrage du maximum par trajectoire honnête complète, que je reprends de C, la remplace.
- **P3, sélection.** On estime E[TPR | F3 retenue]. Cette quantité dépasse E[TPR] si Cov(robustesse, signature interne) > 0, et elle n'est pas transportable à « tout sabotage sans consigne ».
- **P4, corrélation de rang.** Mesurée toutes doses confondues, elle est dominée par la composante entre doses. Elle peut être forte alors que la corrélation à l'intérieur d'une faible dose est nulle. Le critère doit être intra-dose. Le facteur de réduction dépend de π et de δ/σ_0, qui ne sont pas fixés.
- **P5, plafond de la note.** Si P(note ≥ seuil | H) est proche de 1 avant tout entraînement, la « note presque maximale » ne contraint rien. Je ne sais pas si une note faible a une dynamique utile à cette échelle. Le résidu en rapport a le même défaut que chez B.

### (c) Contrôles négatifs dont l'absence serait fatale

- En P4, des scores de sonde permutés et un flux à π = 0.
- En P4, l'accord entre humains sur des paires honnête contre honnête, à l'intérieur d'une dose. Sans lui, le « plancher de bruit » n'a pas de référence.
- En P5, un bras placebo à calcul égal, dans la même expérience et pas seulement en amont.
- Le lecteur sans état, en P1 et P3.
- Je retiens de E l'adaptateur bénin entraîné par la même procédure que F3, puis soumis au même entraînement. C'est le témoin qui manque à D en C5.

FIN-DE-CELLULE