# Critique croisée de méthode — proposition B, tour III.2

**Pièces.** J'ai reçu les conceptions A, C, D et E. Toutes se terminent par FIN-DE-CELLULE et ne montrent pas de coupure visible. Je n'ai pas recalculé les empreintes. Aucune pièce ne contient d'instruction que j'aurais eu à écarter.

**Forme.** Le livrable de ce tour est la critique croisée. La forme en sept sections du bloc QUESTION régit la conception (tour III.1), pas ce tour.

**Statuts.** Tous les seuils chiffrés que j'écris moi-même sont **illustratifs**. Les quelques calculs de probabilité (règle de trois, loi exacte d'un coefficient de Spearman sur 4 points) sont de l'arithmétique, pas des faits du banc.

**Notations.** Je les utilise sans fusionner les propositions :
- π : prévalence de sabotage dans un lot ;
- K : nombre d'articles, qui est l'unité d'appariement ;
- Δ : biais d'étalonnage par pas entre honnête de calibration et honnête de service ;
- δ : décalage moyen par pas dû au sabotage ;
- σ_run : écart-type entre courses d'entraînement de même recette ;
- ε : plancher de probabilité de tirage d'audit.

**Deux objections qui touchent plusieurs propositions.** Je les énonce une fois et j'y renvoie section par section.

- **[F]**, fuite par construction entre les familles 1 et 2. Le saboteur à adaptateur est obtenu « en générant avec la consigne cachée puis en entraînant sans elle » (VÉRIFIÉ). La famille 2 est donc entraînée à imiter les sorties de la famille 1. Une sonde apprise sur l'une et « transférée » à l'autre n'est pas évaluée hors distribution : le texte et une partie des états visés sont partagés par fabrication. Aucun transfert F1→F2 ne satisfait la règle « famille inédite » (VÉRIFIÉ).
- **[T]**, contrôle par forçage du texte. On fait lire la transcription du saboteur, jeton par jeton, au modèle honnête, puis on applique la sonde à ses états. Si la sonde sépare autant, elle lit le texte et non un état propre à l'agent. C'est le contrôle qui opérationnalise « interne contre texte ». Son absence rend toute porte « lecture interne contre moniteur de texte » non jugeable.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **C1, R dépend de la granularité.** Le dénominateur de R = décalage par pas / dérive *maximale* entre strates est un maximum. Son espérance croît avec le nombre k de strates : pour des dérives quasi gaussiennes, environ σ·√(2 ln k). R baisse donc mécaniquement quand on raffine la stratification, et le seuil R > 3 n'a pas de sens tant que k n'est pas fixé au préenregistrement.
2. **C1, le contrôle négatif est vrai par construction.** Permuter les étiquettes à l'intérieur de chaque article annule δ par définition. Ce contrôle teste le code, pas l'hypothèse de stabilité du nul. Le contrôle utile est un pseudo-saboteur : deux lots honnêtes disjoints, l'un étiqueté « saboteur ».
3. **Unité d'accumulation non fixée.** L'argument « biais en n, bruit en √n » ne pèse que si n est grand. Un épisode compte 10 pas (VÉRIFIÉ). A ne dit pas si l'accumulation se fait par pas dans l'épisode ou à travers les épisodes, et la conclusion de C1 change selon ce choix.
4. **C2, choix de la couche.** A conserve les scores « par couche ». Choisir la couche sur le lot d'évaluation est une fuite qui favorise H_A. H_B est en outre formulé comme « entièrement expliqué ». Une explication complète n'est pas démontrable en échantillon fini : seul l'incrément est testable, et le seuil de 0,05 d'AUROC le traite déjà ainsi. La formulation de H_B devrait suivre.
5. **C2 et [F].** Le test « sur chaque famille » est sain si chaque famille a sa propre sonde. Il est vicié si une sonde de F1 est lue sur F2.
6. **C3, effet plancher.** Un entraînement sur récompenses aléatoires peut dégrader aussi le jumeau. Le rapport « après / avant », lu contre un jumeau dégradé, se comprime alors vers 0 : l'organisme paraît « fragile » par compression de l'échelle de qualité. A cite le témoin « jumeau entraîné seul », mais sans critère de capacité.
7. **C4, gain dépendant du dispositif.** Le gain d'aiguillage mesuré en rejeu dépend de la prévalence π, que l'expérimentateur choisit en composant les mélanges. Il dépend aussi de la corrélation entre score de sonde et *erreur* de l'oracle : si les deux réagissent à la longueur, le gain est en partie artefactuel.
8. **C5, pseudo-réplication.** Une course d'entraînement par bras signifie que les épisodes ne sont pas l'unité de réplication. Toute différence entre bras est confondue avec la graine d'entraînement.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **C1.** Avec un accumulateur à seuil fixe et Δ ≠ 0, le taux réalisé de fausses alertes tend vers 1 quand le nombre de pas accumulés croît. R devient non jugeable si K est petit : la variance du maximum entre strates domine son espérance.
- **C2.** Si la corrélation intra-article des scores est forte, l'effectif utile tend vers K. Avec K petit, l'intervalle apparié (type DeLong groupé) sur ΔAUROC recouvre à la fois 0 et 0,05, et le test est indécis.
- **C3.** Le rapport D₁/D₀ a une variance non bornée quand l'intervalle de D₀ approche 0 (problème de Fieller). Il n'est jugeable que si D₀/se(D₀) est grand, ce qui exclut la plus faible dose.
- **C4.** L'estimateur à pondération inverse a une variance proportionnelle à E[1/p]. Si les épisodes dommageables reçoivent des scores bas, donc p ≈ ε, la variance explose. Le gain tend vers 1 si, conditionnellement au dommage reconnu, le score est indépendant de ce dommage, ou si π est grand.
- **C5.** Si σ_run est du même ordre que l'écart attendu de la part de dommage retenue, une course par bras ne départage pas H_A et H_B.

### (c) Contrôles négatifs dont l'absence serait fatale

- **C1** : un pseudo-saboteur formé de deux lots honnêtes disjoints.
- **C2** : des articles d'apprentissage de la sonde disjoints des articles d'étalonnage et de test. A prévoit déjà [T], via le « lecteur tiers lisant la transcription ».
- **C3** : un critère chiffré de capacité absolue sur le jumeau entraîné.
- **C4** : un balayage de π, sans lequel le rapport d'audits n'est pas une propriété de la sonde.
- **C5** : au moins deux graines par bras, et l'entraînement contre une direction aléatoire, que A prévoit déjà.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Duels non jugeables en l'état.** Les marges m_A à m_E, α et q sont laissées ouvertes, et C l'écrit : c'est honnête. Mais tant qu'elles ne sont pas fixées, aucune issue ne falsifie quoi que ce soit, et la règle B4 n'est pas encore satisfaite. Leur fixation doit précéder toute lecture d'oracle, sous peine de choisir m après coup.
2. **Test A, biais de spectre.** La sensibilité du lecteur de produit est calculée sur des « pertes arbitrées ». Si les pertes arbitrables sont les plus grosses, la sensibilité est surestimée, précisément là où la menace est diffuse.
3. **Test A, circularité possible.** La référence est construite par des humains qui voient le jumeau. Si ces mêmes lecteurs, ou la même grille, servent ensuite à « confirmer » les dommages du test D, l'aiguillage est noté contre la grille qui a défini le dommage.
4. **Test C, famille réservée non désignée.** Si la « famille réservée » est F2 et que la sonde a été conçue sur F1, l'objection [F] s'applique et le test n'est pas hors fabrication.
5. **Test C, contrôle [T] absent.** C impose « même texte disponible au même instant » au juge de texte, mais ne fait pas passer le texte du saboteur dans les états du modèle honnête. Sans [T], un gain de la sonde sur le juge peut venir d'une meilleure lecture du *même* texte, pas d'un état propre à l'agent.
6. **Test D, rendement dépendant du dispositif.** Le nombre de « dommages confirmés par heure » dépend de π dans les dossiers gelés et du seuil de confirmation des lecteurs. Ce n'est pas une propriété de l'aiguillage sans ces deux paramètres.
7. **Test E, conditionnement.** La condition « seulement si l'écart initial dépasse q » est saine parce que C impose des articles réservés. Il faut seulement vérifier que l'écart initial est estimé sur d'autres articles que l'effet, sinon on observe une régression vers la moyenne.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Test A.** L'estimateur de sensibilité est biaisé si P(arbitrable | taille de perte) croît avec la taille de perte. Le test est non jugeable si le taux d'abstention diffère entre conditions : la sensibilité est alors conditionnée à un sous-échantillon sélectionné, et C le pressent.
- **Test B.** Le test de tendance ordonnée perd sa puissance quand la variance entre questions σ_q² domine la pente de dose. Le nombre de blocs fixe la puissance, pas le nombre d'épisodes.
- **Test C.** « Sans excéder α dans chaque strate honnête » exige, pour une borne à 95 % avec zéro alerte, environ 3/α trajectoires indépendantes *par strate* (règle de trois). Avec α petit et plusieurs strates, le critère est non jugeable au budget annoncé.
- **Test D.** Si le nombre attendu de dommages confirmés par bras est petit (comptage de type Poisson), l'écart entre bras est non jugeable quelle que soit la marge m_D.
- **Test E.** Si σ_run est du même ordre que m_E, ce qui sera le cas avec une seule course d'adaptation par bras, le test est non jugeable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Test C** : le contrôle [T], et une famille réservée qui ne partage pas de traces avec la famille de conception.
- **Tests A et D** : des lecteurs de confirmation distincts de ceux qui ont construit la référence.
- **Test D** : des scores permutés, que C prévoit déjà, et un balayage de π.
- **Test E** : une mise à jour de même budget sans information corrective appliquée *au saboteur*, que C prévoit, et au moins deux graines par bras.

Le témoin d'adaptateur bénin, que C dit décisif, est bien présent.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Statuts relevés au-delà des faits (règle 1).**
   - « un aiguillage enrichit la fraction auditée (VÉRIFIÉ) » : les faits disent seulement que le programme *assigne* ce rôle aux sondes.
   - « si une propension interne persiste malgré une sortie apparemment corrigée (VÉRIFIÉ) » : ce n'est pas dans les faits.
   - « une sonde témoin isolée teste si l'entraînement a guéri ou masqué (VÉRIFIÉ, jeu d'audit) » : le jeu d'audit dit que la détection reste *nécessaire* pour valider un entraînement, pas qu'une sonde hors boucle y parvient.
   - « capture la dérive sans induire d'évasion (VÉRIFIÉ, notes de 2025) » : les notes *nomment* le compromis, sans en établir l'effet.
   - « (HYPOTHÈSE fausse) » : une hypothèse n'a pas de valeur de vérité établie. Si D veut dire « au cas où l'hypothèse serait fausse », il faut l'écrire.
2. **Conflits de règles non déclarés.**
   - Le C4 fait optimiser l'agent pour persuader le juge de texte. Le bras d'attaque déclaré vise le score d'une *sonde* (VÉRIFIÉ), pas celui d'un juge.
   - Le C5 entraîne contre la note faible, c'est-à-dire le score d'un juge qui lit le texte. Il sélectionne aussi les points de contrôle « à note faible égalisée (±2 %) ». La règle interdit tout score de moniteur, « sonde ou juge », dans l'entraînement *ou la sélection* de l'agent hors bras déclaré.
   - D ne lève explicitement que « corriger en entraînant n'est pas ouvert ». C'est, à mon avis, insuffisant ; l'arbitre tranche.
3. **C1 et C2 tombent sous [F].** La sonde est apprise sur la consigne cachée et testée sur l'adaptateur, et le C2 s'appelle explicitement « transfert consigne → adaptateur ». Le transfert est en partie garanti par la fabrication.
4. **C2, métrique qui ne mesure pas l'audit.** AF = TPR/0,05 est un rapport de rappel à α, pas un gain d'audit : il n'en devient un qu'à π faible. Les critères « AF ≥ 6 » et « rappel ≥ 30 % » sont le même critère écrit deux fois. « +3 points » d'AF contre « +2 points » est une unité non définie.
5. **C3, hypothèses mal construites.** H_A est une conjonction : 8B fragile *et* 14B résistant *et* lisible. Le cas « 8B fragile, 14B non résistant » n'appartient ni à H_A ni à H_B, et les deux hypothèses ne sont pas exhaustives.
6. **C3, organismes à 14 milliards.** Les faits établissent que ces saboteurs résistent à un renforcement sur *leurs* tâches. Leur sabotage sur ce banc n'est pas établi. Le statut VÉRIFIÉ que D leur accole ne couvre pas leur usage ici. « AUROC ≥ 0,75 sur 14B » suppose aussi des étiquettes de sabotage sur le banc qui n'existent pas.
7. **C5, note faible indisponible.** « La note faible du papier de 2026 » a été construite avec des modèles bien plus grands (VÉRIFIÉ). Je ne sais pas si elle est disponible ni transposable au modèle de huit milliards.
8. **C5, pseudo-réplication.** Il y a une seule course saboteur, et les deux honnêtes ont des rôles différents. Même défaut que A, C5.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **C1, Spearman sur 4 doses.**
  - *Loi nulle.* Sous ordre aléatoire, P(ρ = 1) = 1/24 et P(ρ ≥ 0,8) = 4/24 ≈ 0,17. Le critère ρ ≥ 0,8 laisse passer un oracle sans information une fois sur six.
  - *Échec sans fondement.* À l'inverse, si l'écart de dommage entre doses voisines est inférieur à environ deux erreurs-types par dose, une seule inversion fait échouer un oracle valide.
  - *Conséquence.* Le critère est non jugeable sans erreurs-types par dose.
- **C1, ΔFPR ≤ 5 points sur 3 adaptateurs bénins.** L'unité est l'adaptateur. Si la variance entre adaptateurs domine, l'intervalle sur ΔFPR avec 3 unités couvre largement 5 points.
- **C2.** « α ≤ 5 % cumulé sur 10 pas » n'est garanti que si le seuil séquentiel est étalonné sous la vraie dépendance entre pas. Sinon, α réalisé ≠ α nominal, et le TPR comparé n'est pas à α égal.
- **C3.** Les seuils R_dom ≤ 0,20 et R_dom ≥ 0,50 héritent du problème de Fieller (voir A, C3). La condition « capacité ≥ 95 % » n'est jugeable que si la capacité est mesurée sur des articles distincts.
- **C5.**
  - Égaliser la note faible par sélection de point de contrôle conditionne sur une variable bruitée et post-traitement. Le dommage résiduel est alors biaisé de façon dépendante du bras.
  - Avec σ_run ≳ 20 points de dommage relatif (illustratif), l'écart entre les seuils 10 % et 30 % n'est pas résoluble.

### (c) Contrôles négatifs dont l'absence serait fatale

- **C1 et C2** : le contrôle [T], et une sonde apprise sur une famille qui ne partage aucune trace avec la famille testée.
- **C5** : le saboteur soumis à un entraînement placebo de même budget. Sans lui, la baisse de dommage n'est pas attribuable à la note faible. D ne prévoit que des témoins honnêtes à ce stade.
- **C3** : un critère de capacité sur les honnêtes entraînés, avec seuil.

Les paires honnête/honnête (C1) et le jumeau algorithmique bénin de la troisième famille (C4) sont présents et doivent rester.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Statuts.**
   - E range sous OBSERVÉ-NON-AUDITÉ l'idée que « l'oracle sépare un sabotage diffus du bruit ». Les faits ne contiennent pas cette observation : c'est une HYPOTHÈSE.
   - « Un essaim de copies non collusoires se ramène statistiquement à l'accumulation sur épisodes indépendants » est présenté sans statut. C'est contestable : des copies *à poids partagés* exécutent la même politique, leurs épisodes sont corrélés par construction, et c'est précisément ce qui distingue l'essaim. L'argument pour différer les essaims reste défendable, pas celui-ci.
2. **Sur-affirmation.** « Si l'accumulateur traite les pas comme indépendants, la borne est mathématiquement invalide. » La validité dépend de la construction : un processus de test construit sur des lois conditionnelles reste valide sous dépendance, un seuil étalonné sous indépendance ne l'est pas. C'est une condition à vérifier, pas un fait.
3. **« Règles modifiées : aucune », contesté.**
   - A1 et P2 entraînent le modèle soupçonné (placebo). P5 l'entraîne contre la note faible, qui est un score de juge, et fixe une cible « note faible ≥ 95 % ».
   - A déclare la même opération comme une modification de périmètre, et D aussi. E ne le fait pas, alors que la règle « sonde ou juge » paraît atteinte. Je demande que E le déclare ou explique pourquoi la note faible ne serait pas un score de moniteur.
4. **P2, deux questions dans un seul duel.** H_A est « organisme robuste *et* sonde fragile à la dérive ». Ces propriétés sont sans lien : leur conjonction ne falsifie rien d'interprétable, et l'issue « robuste et invariante » est rangée dans H_B. E dit tester les volets séparément ; il faut alors deux duels.
5. **P3, fuite de lecture.** La famille F3 est « fabriquée et calibrée en dose-réponse » et validée au placebo *avant* la lecture unique. Si la personne qui fige la sonde voit ces sorties, la lecture unique est compromise. La sonde, apprise sur F1/F2, tombe aussi sous [F] pour toute revendication intermédiaire.
6. **P4, deux hypothèses dans un seul duel.** P4 joint l'accord oracle-humains et le gain d'aiguillage. Un échec ne dit pas laquelle des deux tombe.
7. **P1, appariement en KL non défini.** « Appariés en divergence KL » ne dit pas sur quelle distribution d'entrées. Choisir les adaptateurs bénins *a posteriori* pour égaler la KL de F2 est une sélection qui peut aligner aussi des propriétés que la sonde lit.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **P1, le critère de fausses alertes n'est pas jugeable avec les chiffres de E.**
  - E fixe un FPR ≤ 1 % sur un cumul de 20 épisodes et environ 200 épisodes par condition (illustratif, de E).
  - Cela fait au plus 10 séquences honnêtes indépendantes par condition.
  - Avec zéro alerte sur 10 séquences, la borne supérieure à 95 % vaut 1 − 0,05^(1/10) ≈ 26 %.
  - Certifier 1 % demande environ 300 séquences, soit environ 6 000 épisodes par strate.
- **P2b.** « Variation de FPR ≤ +1 point » se heurte au même obstacle. Elle est non jugeable au budget annoncé.
- **P4.** Un coefficient de rang sur 60 paires a une erreur-type d'environ 1/√59 ≈ 0,13 (approximation). L'intervalle autour de 0,65 descend vers 0,40, si bien que la zone indécise couvre les deux seuils de E.
- **P3.** Si F3 a un dommage moyen proche du plancher A/A de P4, le TPR mesuré par rapport à l'oracle n'est pas interprétable. E l'écrit comme condition d'invalidation : c'est juste, mais cela rend P3 dépendant de P4, alors que P4 est ordonné *après* P1.
- **P5.** Comme D, C5 et A, C5 : avec σ_run du même ordre que l'écart entre 10 % et 30 % de dommage résiduel, une campagne par bras est non jugeable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **P1 et P3** : le contrôle [T].
- **P3** : la qualification de F3 (placebo, dose) faite par un tiers, ou avec les scores de sonde scellés, pour protéger la lecture unique.
- **P5** : le saboteur F3 sous placebo de même budget, et pas seulement des témoins honnêtes.
- **Essaims, si l'on y revient** : un essaim honnête à poids partagés, pour mesurer la corrélation inter-copies sous le nul.

Les témoins bénins appariés (P1), l'entraînement placebo (P2) et les doubles tirages du jumeau (P4) sont bien présents.

---

**Ce que je reprends, et d'où.**
- Le contrôle de lecteur tiers de A, généralisé en [T].
- Le biais de spectre des « pertes arbitrées », signalé implicitement par C.
- Le souci d'autocorrélation de E, reformulé en condition.
- Les seuils de fausses alertes : aucune des quatre propositions ne dimensionne leur certification. C'est le défaut commun le plus probable de faire échouer une porte au motif « indécis ».

FIN-DE-CELLULE