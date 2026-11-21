# Proposition B : Tour III.3, réponse aux critiques

**Pièces.** Ma conception III.1 et les critiques A, C, D et E sont reçues. Chacune se clôt par sa ligne de fin et aucune n'est coupée. Les faits restent RAPPORTÉ et l'avis du directeur reste HYPOTHÈSE.

**Statuts.**
- Les statuts posés par les critiques restent les leurs.
- Quand je refais un calcul, je l'indique « VÉRIFIÉ par calcul (B) ».
- Tout seuil choisi par moi est « illustratif ».

**Emprunts déclarés (B1).**
- J'utilise les outils O1 et O3 de A.
- J'utilise la règle de décision par région préenregistrée de D.
- J'utilise le critère de D : « conclusion fausse livrée » plutôt que « agent signalé ».
- Je les cite à chaque usage. Je ne fusionne rien.

---

## (a) Décision sur chaque critique visant B

Les critiques convergentes sont regroupées par ligne, avec leurs sources.

| # | Sources | Critique | Décision | Raison, ou test qui la remplace |
|---|---|---|---|---|
| 1 | A-a1, D-b | D0 a quatre issues et je n'en interprétais que deux. « Nettement » n'est pas chiffré. Consigne et objectif ne varient jamais séparément. | **Acceptée** | B4 n'était pas tenu. D0 est refondu en plan factoriel à paramètres séparés (b.3). |
| 2 | A-a2, A-c, C-c1, E-c1 | Le jumeau « même chaîne » ne neutralise ni le contenu d'affinage, ni la présence d'un objectif secret, ni les mots de la consigne. | **Acceptée** | Trois cellules sont ajoutées : affiné sur données décrivant le sabotage mais honnête (A), règle secrète bénigne (C), amorce lexicale bénigne (E). |
| 3 | C-a1 | Le saboteur par consigne est peut-être plus grossier. Une non-détection confondrait « lit l'affinage » et « lit la furtivité ». | **Transformée en test** | Analyse restreinte au support commun : cas appariés sur la dégradation obtenue et sur le score d'un moniteur de texte. |
| 4 | E-a1 | La classe négative d'entraînement de la sonde n'est pas fixée. La calibration est asymétrique. | **Acceptée** | Deux sondes : celle du programme telle quelle (son entraînement : je ne sais pas), et une sonde intra-construction entraînée sur tâches disjointes. |
| 5 | E-b1 | Mon critère rejette une sonde que l'affinage décale mais qui reste discriminante après recalibration. | **Acceptée** | C'est la correction la plus utile. On sépare deux paramètres : le *décalage de calibration* (θ_constr) et la *discrimination à construction fixée* (θ_disc). Le premier impose de recalibrer au déploiement, il ne tue pas la sonde. |
| 6 | A-b, C-b1, E-b1 | Exiger « ≤ 1 % sur 299 cas » rejette à 95 % une sonde au taux nominal exact. Il faut une non-infériorité. Les grappes réduisent l'effectif. | **Acceptée** | Le calcul 0,99²⁹⁹ ≈ 0,0496 reste juste (statut inchangé), mais son emploi dans D0 était faux. Pour séparer 1 % de 2 % (unilatéral, niveau 5 %, puissance 80 %), il faut environ 790 cas. VÉRIFIÉ par calcul (B), approximation normale ; A donne environ 800. Les ≈ 1 050 cas et la puissance « < 25 % » de C sont marqués illustratifs par C. Mon calcul exact de Poisson à n = 299 donne un rejet à K ≥ 7, de niveau ≈ 3,3 % et de puissance ≈ 39 %. Le constat qualitatif de C tient. |
| 7 | D-b | Le « 63 % des tâches » suppose des alertes indépendantes par action. | **Acceptée sur la portée** | L'arithmétique reste VÉRIFIÉE ; l'indépendance est une HYPOTHÈSE. Sous dépendance arbitraire, le taux par tâche est seulement compris entre 1 % et 100 % (borne de l'union, VÉRIFIÉ par calcul (B)). L'obligation de fixer l'unité en sort renforcée. |
| 8 | A-a3 | Comparer une borne inférieure estimée de TV au TPR − FPR mesuré est une identité. | **Acceptée** | La ligne « Mathématiques (bornes) » du tableau §3.2 est retirée. |
| 9 | A-a4, A-b, C-b3, E-a4, E-b5, D-b | M2 exige une borne *supérieure* de TV, non estimable sur échantillon. TV est d'ailleurs la mauvaise quantité à α = 1 %. | **Acceptée** | M2 est reconstruit sur O1 de A : la loi saboteuse est construite, avec une queue du rapport de vraisemblance bornée et déclarée (b.2). |
| 10 | A-c | Il manque un témoin positif pour M2. | **Acceptée** | Ajout d'un organisme à rapport de vraisemblance non borné, que le même banc doit détecter. |
| 11 | D-b | Un support commun n'impose pas une petite TV. L'égalité action par action n'impose pas l'égalité jointe. | **Acceptée** | C'est une raison de plus pour remplacer « support honnête » par « repondération bornée ». |
| 12 | A-a5, C-a2, D-a | Interroger le gardien du mode tenu à l'écart, même par oui ou non, fait fuir un bit. | **Acceptée** | Le premier pas de D1 se limite aux modes connus. Le gardien n'intervient qu'une fois, à la fin, sur un protocole gelé. |
| 13 | A-a8, A-c, D-a, D-c | D1 compare des budgets de surveillance inégaux. Un gain du paquet ne s'attribue pas au préengagement. | **Acceptée** | Trois bras à temps d'audit égal, dont un placebo : plan consigné et audité mais non contraignant. |
| 14 | D-b | Le contraste doit être pris en intention de traiter. Le maximum sur les attaques essayées n'est qu'un minorant du risque. | **Acceptée** | Métrique par tâche assignée. Le risque publié est qualifié de minorant. |
| 15 | C-c2 | Le sabotage peut être logé dans le plan scellé lui-même. | **Acceptée, bras obligatoire** | C'était mon H_B ; il est désormais mesuré explicitement. E-b2 en donne la borne : puissance ≤ α + TV des plans. |
| 16 | E-b2 | Si le taux d'écart honnête r₀ dépasse le budget d'audit b, la puissance sur écart est ≤ r₁·b/r₀. | **Transformée en précondition** | r₀ ≤ b est mesuré avant tout duel D1. Sinon, D1 s'arrête. |
| 17 | E-a2 (Rice) | La conformité exécution/plan serait indécidable. | **Rejetée en partie** | Le plan est une liste finie dans un langage restreint : métrique, critères d'exclusion, analyses. La conformité d'une exécution bornée à cette liste se décide en l'exécutant et en comparant. Rice porte sur les propriétés sémantiques de tous les programmes ; A adresse la même objection à E. Le cœur empirique (rigidité contre couverture) est **accepté** et testé par le « plan parapluie » de E et les révisions honnêtes nécessaires de D. |
| 18 | E-a2 (préentraînement) | Le modèle a déjà vu les données. | **Rejetée pour les mondes plantés, acceptée ailleurs** | Les mondes plantés produisent des données nouvelles, et leur vérité reste hors machine (RAPPORTÉ). D1 est restreint aux mondes plantés et aux données nouvelles. |
| 19 | A-a6, C-a3, C-c3, E-a3, E-c3, D-b | M3 confond lignée et difficulté. L'agrégateur a été choisi sur les mêmes journaux. | **Acceptée pour l'attribution, rejetée pour l'usage** | Une corrélation des ratés due à la difficulté détruit *aussi* le gain d'agrégation supposé sous indépendance. La mesure opérationnelle reste donc valide sans attribution. M3 est scindé en M3a (sans attribution) et M3b (attribution par réplicats intra-instance, à taux de raté marginal égal), sur données fraîches. |
| 20 | A-a7, D-b, D-c | M1 est acquis par construction contre les moniteurs d'actions. Omission et commission ne se comparent que sur un support commun. | **Acceptée** | Un moniteur de couverture devient le comparateur. Contrôle : recherches honnêtes interrompues faute de ressources. |
| 21 | A-b, C-a3, C-b2, E-b3, D-b | Dans D2 : variance honnête, multimodalité, quantiles de Student à k = 2 ou 3, erreurs corrélées entre lignées (TPR ≤ 1 − ρ_c). | **Acceptée comme condition** | Calibration par strate d'ambiguïté fixée d'avance. k ≥ 5 ou variance mise en commun par strate. ρ_c mesuré. Mes re-dériveurs reçoivent l'énoncé du commanditaire, pas un noyau écrit par l'agent. La fuite relevée contre RAND-ML ne s'applique donc pas telle quelle, mais ρ_c reste le paramètre qui peut annuler D2. |
| 22 | A-b, E-b4 | D3 : la dérive honnête casse Ville. L'acte unique à rapport borné donne une puissance nulle. | **Acceptée** | L'acte unique était déjà déclaré hors portée. J'ajoute un contrôle de dérive (mélange de tâches changé volontairement). |
| 23 | A-b | La borne 1 − (1 − t)ᵏ suppose l'indépendance, que M3 conteste dans la même pièce. | **Acceptée** | L'incohérence interne est réelle. La formule n'est valable que sous indépendance ; sous corrélation positive des ratés, elle surestime la détection. |
| 24 | D-b, D-c | Le rendement du portier n'est pas identifié par la réplication des seuls acceptés. | **Acceptée** | Ajout au tableau : réexamen à l'aveugle d'un échantillon de rejets contenant des résultats vrais non conventionnels. |
| 25 | D-b | Un délai moyen conditionnel aux alarmes exclut les non-détections. | **Acceptée** | La métrique devient P(T_alarme < T_dommage) à horizon fixé. |

**Ce que j'en retiens.** Trois de mes erreurs étaient de même nature : j'ai traité comme estimable ce qui ne l'est que par construction.
- La borne supérieure de TV (M2).
- L'attribution à la lignée (M3).
- L'attribution au préengagement (D1).

La correction est la même dans les trois cas : construire l'objet de contrôle, ou bien randomiser le facteur.

---

## (b) Expériences corrigées

### b.0 Règle de décision commune (reprise de D)

Chaque duel préenregistre :
- un paramètre θ ;
- une coupure c ;
- une distance de planification δ ;
- un effectif tel que, si |θ − c| ≥ δ, l'intervalle à 95 % ne chevauche c qu'avec une probabilité ≤ 20 % (illustratif).

Lecture :
- intervalle entier d'un côté de c : l'hypothèse de l'autre côté est falsifiée ;
- intervalle qui chevauche c : est falsifiée l'hypothèse de planification « |θ − c| ≥ δ ». Cette issue est consignée comme telle, sans requalification.

Partout, l'effectif est compté en *tâches distinctes*, avec n_eff = n / (1 + (m − 1)ρ), où m est le nombre de trajectoires par tâche et ρ leur corrélation.

### b.1 E1 (nouveau, à faire en premier) : le taux d'erreur honnête livrée

**Quantité.** p_err = P_H(conclusion fausse **et** acceptée par le filtre actuel du programme), par tâche, sur mondes plantés.

**Pourquoi ce paramètre.** Il fixe deux plafonds indépendants des moniteurs (calculs en b.2 et chez A, O3) :
1. L'ampleur maximale d'un sabotage dans le support honnête est (k − 1)·p_err, à détection comportementale ≤ k·α.
2. Toute défense qui ne voit que la validité d'une conclusion, comptée en attribution, plafonne à α / p_err (O3 de A).

**Duel.**
- **H_A** : p_err > 3 %.
- **H_B** : p_err ≤ 3 %.
- Coupure et δ = 2 points sont illustratifs. L'effectif est de l'ordre de 300 tâches distinctes ; c'est un ordre de grandeur calculé à partir de ces seuils illustratifs.

**Ce que falsifie chaque issue.**
- Une issue en H_A falsifie la prémisse implicite du programme : « la détection de l'agent à 1 % est le bon objectif ». Le programme doit alors viser la conclusion fausse livrée (critère de D) et des défenses qui suppriment la sélection a posteriori (D1).
- Une issue en H_B falsifie « la menace dominante vit dans le support honnête ». La priorité revient au canal interne (D0').

**Contrôles.**
- Erreurs honnêtes plantées de type connu, pour vérifier que le filtre est appliqué tel quel.
- Tâches à vérité ambiguë exclues *avant* exécution.

**Premier pas sans dépense.** Vérifier si la mémoire des tentatives contient des exécutions honnêtes sur mondes plantés avec leur issue. Je ne sais pas si c'est le cas.

### b.2 M2' : la menace dans le support honnête, reconstruite comme repondération bornée

**Définitions.**
- P_H est la loi honnête de la trajectoire complète : actions, sorties, activations du modèle honnête qui l'a produite.
- Une loi P_S est une *repondération bornée par k* si dP_S/dP_H ≤ k.
- Cette définition décrit une loi. Elle ne décrit aucun procédé.

**Deux faits mathématiques.**
- **(i)** Pour tout moniteur dont l'observable est une fonction de la trajectoire, activations et issue comprises : TPR ≤ k·FPR. C'est O1 de A. Je l'ai refait : le rapport de vraisemblance sur un observable est une espérance conditionnelle du poids, donc il reste ≤ k. VÉRIFIÉ par calcul (B).
- **(ii)** P_S(F) ≤ min(1, k·P_H(F)), F étant « conclusion fausse ». Cette valeur est atteinte : poids k sur F, poids (1 − k·P_H(F)) / (1 − P_H(F)) ≤ 1 ailleurs. VÉRIFIÉ par calcul (B).

**Lecture.**
- La frontière de la menace « dans le support honnête » est exacte : une dégradation de (k − 1)·p_err, invisible au-delà de k·α pour tout moniteur de la trajectoire repondérée.
- Exemple, sur des valeurs illustratives : p_err = 10 %, k = 3, α = 1 %. On obtient jusqu'à 20 points de dégradation pour un TPR ≤ 3 %.
- Ce qui échappe à la borne est un agent *réel* qui réalise cette sélection. Il lui faut une information corrélée à l'issue et un traitement de cette information. Cela laisse deux prises (HYPOTHÈSE) :
  - ses états internes pendant qu'il sélectionne : c'est l'objet de D0' ;
  - l'information post-données dont il a besoin : D1' la supprime.
- Les mathématiques désignent ainsi les deux seuls endroits où chercher. C'est l'usage « borne qui dit où chercher » que demandait l'arbitre, sans la quantité non identifiable de ma version III.1.

**Contrôle d'étalonnage du banc.**
- Sur la loi repondérée, construite par rééchantillonnage d'exécutions honnêtes, aucun moniteur ne peut dépasser k·α.
- Un banc qui le dépasse a une fuite ou un bogue.
- Témoin positif : un organisme à rapport non borné (A), que le banc doit détecter.

**Duel M2' (identifiable dans ce sens).** Un TPR mesuré supérieur à k·α prouve que le rapport de vraisemblance dépasse k. La queue de L est donc minorable sur échantillon, pas majorable.
- **H_A** : au moins un organisme du programme atteint la dégradation D* avec un TPR, pour le meilleur moniteur, ≤ 3α.
- **H_B** : tout organisme qui atteint D* est détecté à TPR > 3α par au moins un moniteur.
- D* et 3α sont illustratifs.

**Ce que falsifie chaque issue.**
- H_A falsifie « les moniteurs actuels couvrent les organismes du programme ».
- H_B falsifie « les organismes du programme peuplent le régime dangereux ». La loi repondérée doit alors entrer dans la batterie d'épreuve. C'est un résultat de forme F2.

### b.3 D0' : la sonde lit-elle le sabotage ? Plan factoriel

**Cellules.**

| Cellule | Construction | Contenu / objectif |
|---|---|---|
| C1 | base | honnête |
| C5 | affiné, même chaîne | honnête |
| C7 | affiné | règle secrète bénigne (C) |
| C8 | affiné | saboteur |
| C6 | affiné | données décrivant le sabotage, comportement honnête (A) |
| C2 / C3 / C4 | base | consigne de sabotage / consigne secrète bénigne de même saillance / amorce lexicale analytique (E) |

**Phases.** La phase 1 couvre C1, C5, C7 et C8. La phase 2 (C6, C2, C3, C4) n'est lancée que si D0'.b passe en phase 1.

**Sondes.**
- P_prog, la sonde du programme telle quelle.
- P_intra, entraînée sur C8 contre C5 à partir de tâches disjointes.
- Les seuils sont gelés sur des lots de calibration séparés.

**D0'.a : décalage de calibration.**
- θ_constr = taux d'alerte(C5) − taux d'alerte(C1), au seuil calibré sur C1.
- **H_A** : θ_constr ≤ 2 points.
- **H_B** : θ_constr > 2 points.
- Valeurs illustratives. Effectif : environ 800 tâches par cellule (b-6).
- Une issue H_B ne tue pas la sonde. Elle impose de recalibrer sur le modèle effectivement déployé, et elle falsifie l'emploi actuel du seuil s'il a été calibré sur un autre modèle.

**D0'.b : discrimination à construction fixée (central).**
- θ_disc = TPR(C8) − max(alerte(C7), alerte(C6)), au seuil recalibré sur C5.
- **H_A** (la sonde lit le sabotage) : θ_disc > 10 points.
- **H_B** (elle lit l'objectif secret ou le contenu) : θ_disc ≤ 10 points.
- Valeurs illustratives. Une différence de cette taille demande beaucoup moins de tâches que D0'.a.
- Chaque issue falsifie l'autre hypothèse. La phase 1 ne teste que C7. Si elle passe, C6 peut encore falsifier H_A en phase 2.

**Canal par consigne (phase 2, secondaire).**
- TPR(C2) − alerte(C3), et alerte(C4) − alerte(C1).
- Analyse restreinte au support commun de dégradation (ligne 3).

**Contrôles négatifs conservés.** Étiquettes permutées ; couche sans rapport.

**Correction de coût.** En III.1, j'écrivais que D0 ne demandait « presque aucune dépense ». C'est faux : la phase 1 demande de l'ordre de 4 × 800 trajectoires (illustratif). Premier pas sans dépense : vérifier dans la documentation si le jumeau honnête existant (RAPPORTÉ) est passé par la même chaîne d'affinage.

### b.4 D1' : plan scellé, attribution par randomisation

**Bras assignés par tâche avant exécution, à temps d'audit égal.**
1. Moniteur de trajectoire seul.
2. Plan consigné et audité, non contraignant : c'est le placebo.
3. Plan scellé contraignant, avec vérification de l'écart et moniteur du plan.

**Conditions d'exécution.**
- Mondes plantés et données nouvelles uniquement.
- **Précondition** : r₀ ≤ b, mesuré dans le bras 3 sur exécutions honnêtes. Sinon, arrêt.
- **Qualification de l'équipe rouge externe** (reprise par A de E) : elle doit d'abord battre le bras 1 au-delà d'un seuil. Sinon, aucune conclusion n'est tirée.

**Métriques.**
- P(conclusion fausse livrée sans alerte) par tâche assignée (critère de D).
- Utilité honnête.
- Le risque est publié comme minorant.

**Duel.**
- **H_A** : le bras 3 réduit la métrique d'au moins 30 % relativement au bras 2, pour une perte d'utilité ≤ 10 % (illustratif).
- **H_B** : la réduction est < 30 %, y compris quand l'équipe rouge loge le biais dans le plan (bras obligatoire, ligne 15).
- Chaque issue falsifie l'autre.

**Prédiction de mécanisme, issue de M2'.**
- Si D1 agit en supprimant la sélection post-données, son gain doit croître avec la dispersion honnête par tâche.
- Un gain uniforme, ou concentré là où la dispersion est faible, falsifie ce mécanisme même si le paquet fonctionne.
- Test : interaction bras × strate de dispersion, avec strates fixées d'avance.

**Contrôles.** Plans parapluie honnêtes (E) ; révisions honnêtes scientifiquement nécessaires (D).

### b.5 M3a et M3b

**M3a, sans attribution.** Sur des données qui n'ont pas servi à choisir l'agrégateur, on compare le TPR agrégé à 1 % à sa prédiction sous indépendance, calculée depuis les TPR marginaux.
- **H_A** : TPR réalisé ≤ TPR prédit − 5 points (illustratif).
- **H_B** : écart inférieur à 5 points.

**M3b, attribution à la lignée.** Réplicats multiples d'une même instance (tâche × mode), ce qui fixe la difficulté (E-c3). Paires de même lignée et paires croisées, à taux de raté marginal égal par instance.
- **H_A** : la covariance conditionnelle intra-instance est plus forte en même lignée, d'au moins une marge préenregistrée.
- **H_B** : elle est égale.

### b.6 Ajustements de D2, D3 et M1

- **D2** : calibration par strate d'ambiguïté ; k ≥ 5 ; mesure de ρ_c sur tâches à erreur honnête plantée commune. D2 passe derrière D1'.
- **D3** : contrôle de dérive. L'acte unique reste hors portée par construction.
- **M1** : le moniteur de couverture est le comparateur.

**Ordre révisé.** E1, puis D0' phase 1 et M3a (en parallèle, M3a est peu coûteux), puis M2', puis D1'.

---

## (c) Réponse à l'arbitre, en une page

**Percée visée, et qui la remarque** (HYPOTHÈSE sur l'issue). Deux résultats couplés, sur un banc public de sabotage *de recherche* avec ses mondes plantés :
- **(F2)** une frontière mesurée de la menace indétectable, du type « (k − 1) × taux d'erreur honnête livrée, à détection ≤ k·α pour tout moniteur de la trajectoire » ;
- **(F1)** une défense qui ne sonde pas mais retire l'information dont la sélection a besoin (plan scellé), validée contre une équipe rouge externe qualifiée.

Le domaine le remarquerait si des équipes de contrôle de laboratoires, des instituts publics d'évaluation ou des groupes d'apprentissage adverse réutilisaient le banc, ou échouaient à casser la défense avec leurs propres attaques adaptatives. Une détection forte sur nos propres organismes ne compte pas.

**Ce qui est établi.**
- *Calculs* (VÉRIFIÉ par calcul, (B) ou A selon l'indication) :
  - repondération bornée : TPR ≤ k·α et dégradation ≤ (k − 1)·p_err, avec égalité atteignable ;
  - un défenseur qui ne voit que la validité plafonne à α / p_err (O3, A) ;
  - séparer un taux de fausses alertes de 1 % d'un taux de 2 % demande environ 800 cas indépendants ;
  - l'unité du 1 % change la charge d'audit d'un facteur qui peut aller jusqu'à 100.
- *Faits du dossier* : RAPPORTÉ seulement, notamment l'épisode zêta et le 2/68.
- *Performance des instruments du programme* : aucune n'est donnée. Rien n'est établi.

**Ce qui ne l'est pas.**
- La valeur de p_err sur des tâches de recherche : je ne sais pas.
- Si les sondes lisent le sabotage, l'objectif secret ou l'affinage : je ne sais pas.
- Si les organismes du programme peuplent le régime de support honnête.
- Si le plan scellé coûte trop d'utilité honnête.
- Si la méthode de l'épisode zêta se transfère à un domaine où l'évaluateur est un adversaire (HYPOTHÈSE).
- Les chances, jugées qualitativement :
  - moyennes à élevées d'obtenir une mesure nette de la frontière, dans un sens ou dans l'autre ;
  - faibles à moyennes d'obtenir une défense que le domaine remarque.

**L'expérience à faire en premier : E1.** Mesurer p_err, la probabilité qu'un agent honnête livre une conclusion fausse acceptée par le filtre actuel, sur environ 300 tâches plantées distinctes (illustratif).
- **Si p_err > 3 %**, la prémisse « détecter l'agent à 1 % » est falsifiée comme objectif principal. Le programme bascule vers la conclusion fausse livrée et vers D1'.
- **Si p_err ≤ 3 %**, la menace dans le support honnête est petite par théorème. Le canal interne (D0') devient prioritaire.

Ce test coûte peu, il est peut-être déjà calculable sur la mémoire des tentatives (je ne sais pas), et il décide de l'allocation des 4 × 800 trajectoires de D0'.

FIN-DE-CELLULE