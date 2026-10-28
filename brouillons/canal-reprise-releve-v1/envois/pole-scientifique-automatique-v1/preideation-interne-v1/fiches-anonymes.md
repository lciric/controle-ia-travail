# Seize fiches anonymisées (ordre mélangé, auteurs masqués) — tournoi d'idéation interne


## Fiche T01 — Deux distances, une seule vraie

**Idée.** Si une défense généralise par le mécanisme, sa performance doit décroître avec la distance en mécanisme (quelles
hypothèses la famille viole) ; si elle généralise par l'artefact du générateur, avec la distance en surface (style,
générateur, gabarits). On mesure les deux sur les mêmes familles, définitions gelées avant tout score : la distance de
mécanisme tirée de l'empreinte prédictive que la mémoire calcule déjà, la distance de surface par un classifieur de
provenance. Les deux courbes concourent. La mémoire qui refuse les redites devient un appareil de mesure.

**Loi prédictive.** Espace : défenses × familles choisies par la troisième instance pour croiser proche/lointain sur les
deux axes (plan factoriel 2 × 2, au moins huit familles). Prédiction pour une défense qui généralise vraiment : effet de la
distance de mécanisme sur le rappel négatif et au moins double de celui de la surface ; hypothèse concurrente (artefact) :
l'inverse. Métrique : coefficients standardisés, modèle à effets aléatoires de famille. Perte : deux distances
unidimensionnelles résument mal des familles riches.

**Questions servies.** Q6 (sans attendre une boucle complète), Q4, Q3.

**Avantage décisif.** La distance de mécanisme suppose la carte des hypothèses (programme) ; le croisement des axes
suppose des familles commandées à un tiers (méthodes). Originalité : jamais fait, à ma connaissance ; le constat
d'artefact publié est statique et sans test discriminant.

**Demande à l'organisme.** Modification : exporter l'empreinte de la mémoire comme distance. Ajout : commande du plan
factoriel à la troisième instance. **Coût** : processeur sur scores existants ; sondes nouvelles, dépense modeste.
**Piège** : distances corrélées malgré le plan (vérifier la décorrélation avant les scores) ; carte ajustée sur des échecs
(circularité). **Cosmétique si** aucun effet n'est distinct de zéro avec huit familles, ou si la conclusion bascule selon
le classifieur de provenance. **Antériorité** : SUPPOSÉ — Miller et al., « Accuracy on the Line », 2021 ; Achille et al.,
« Task2Vec », 2019. RAPPORTÉ (pièce B) : Fomin 2602.14161 ; Lin et al., 2026.


## Fiche T02 — Contrats hypothèse-garantie et défaillances coïncidentes

**Idée.** En vérification formelle, chaque composant porte un contrat (« si l'environnement respecte H, je garantis G ») et
la composition se raisonne sans exécuter. En logiciel à versions multiples, des versions indépendantes échouent ensemble
plus souvent que l'indépendance ne le prédit, parce que certaines entrées sont difficiles pour toutes. Transposition :
chaque moniteur reçoit un contrat tiré de la carte des hypothèses ; la carte prédit sans exécution, famille par famille,
quels moniteurs sont hors contrat, donc le gain d'un mélange boîte blanche + boîte noire, et son évolution quand la boucle
déplace les contrats.

**Loi prédictive.** Espace : familles tenues à l'écart × paires de moniteurs. Prédiction : gain de rappel du mélange sur
le meilleur seul positif là où les contrats violés diffèrent, ≈ 0 là où ils coïncident ; corrélation de rang ≤ −0,5 entre
recouvrement prédit et gain. Métrique : corrélation de rang par famille, contre une référence d'échecs indépendants.
Perte : un contrat statistique « dégrade » plus qu'il ne « casse » ; la violation binaire perd l'intensité.

**Questions servies.** Q7 (rendue prédictive), Q3, Q1.

**Avantage décisif.** Les contrats sont la carte des hypothèses, que les occupants n'ont pas : ils combinent par ensembles
ou cascades sans théorie (programme). Originalité : contrats pour prédire la diversité d'un ensemble de moniteurs : jamais
fait, à ma connaissance.

**Demande à l'organisme.** Ajout : formalisme léger de contrats ; composition vérifiée en Lean ensuite (couche 4).
**Coût** : processeur seul. **Piège** : contrats écrits après avoir vu quels mélanges gagnent ; trop peu de familles où
les contrats diffèrent. **Cosmétique si** la référence d'indépendance prédit aussi bien, ou si la prédiction se réduit à
« deux moniteurs du même canal échouent ensemble ». **Antériorité** : SUPPOSÉ — Eckhardt et Lee, 1985 ; Littlewood et
Miller, IEEE Transactions on Software Engineering 1989 ; Knight et Leveson, 1986 ; Benveniste et al., « Contracts for
System Design », 2018 ; Kuncheva et Whitaker, Machine Learning 2003. RAPPORTÉ (pièce D) : Parrack 2025, Kramár 2026.


## Fiche T03 — Rejeu contre ancêtres congelés

**Idée.** L'évolution expérimentale congèle chaque génération et mesure l'aptitude des descendants contre les ancêtres
décongelés ; en co-évolution, les tracés « individu courant contre adversaires ancestraux » séparent le progrès vrai du
cycle de la Reine rouge. Nous congelons chaque génération de moniteurs et chaque famille rencontrée ; le progrès se
mesure, sous juge figé, contre trois références : (i) les familles ancestrales, (ii) les familles tenues à l'écart,
(iii) les **sorties publiées** des attaquants des occupants, figées, jamais relancées. Un tapis roulant montre un gain
sur (i) et rien sur (ii) et (iii). Chez les occupants, l'adversaire n'est pas congelé indépendamment du juge ; notre
refus de l'attaquant fait de (iii) une référence figée par construction.

**Loi prédictive.** Espace : (génération g, référence r). Prédiction : pente de gain positive sur (ii) mais ≤ 0,5 fois
celle sur (i) (signe +) ; pente sur (iii) non distinguable de zéro après k générations (prédiction de risque, signe
nul). Métrique : pentes de rang ; indice de transitivité. Perdu : sorties publiées peu nombreuses ; on mesure la
transitivité, pas la cause.

**Questions servies.** Q5, Q2, Q1 (témoin « attaquant publié » sans le construire).

**Avantage décisif.** Organisme : archive complète, héritage récompensé. Méthodes : références (iii) figées par le refus.

**Demande.** Ajout : congélation systématique et rejeu ; stockage. **Coût** : stockage ; processeur pour sondes ;
activations : dépense modérée. **Piège** : fuite des familles ancestrales dans la sélection ; licences des sorties
publiées. **Cosmétique si** : les trois pentes coïncident, ou (iii) est vide. **Antériorité** : SUPPOSÉ — Lenski et al.
(1991) ; Cliff et Miller (1995, « Tracking the Red Queen ») ; Miconi (2009) ; non vu pour moniteurs de sûreté sous juge
figé.


## Fiche T04 — Marché de prédiction des angles morts

**Idée.** Q3 confie la prédiction des angles morts au pôle théorie seul. L'économie expérimentale montre qu'un marché
agrège mieux que l'expert isolé. On fait parier plusieurs proposeurs de lignées différentes (théorie, géométrie de la
fiche 8, prédicteur mécanique sans modèle, modèle de frontière) en **monnaie de sévérité**, sur l'issue « le moniteur M
échoue sur la famille tenue à l'écart F » ; le prix avant test, scellé, est la prédiction collective ; le juge règle
après le test lu une fois, par règle de score propre. On obtient une calibration par lignée — qui sait prédire les
angles morts — et un signal pour pondérer les sources de fiches de la boucle.

**Loi prédictive.** Espace : (moniteur évolué, famille tenue à l'écart, parieur). Prédiction : le prix de marché bat
chaque parieur seul d'au moins 0,02 en score de Brier et bat le hasard d'au moins 0,05 (signe +). Métrique : Brier ;
calibration par lignée. Perdu : le marché résume l'information disponible, il n'en crée pas ; avec une dizaine de
familles, la puissance reste faible — le piège de Q3 n'est pas levé, il est partagé.

**Questions servies.** Q3 ; Q5 (la calibration qui s'améliore de génération en génération est une courbe d'apprentissage
de la boucle).

**Avantage décisif.** Organisme : le juge à mise fournit la monnaie ; plusieurs lignées de proposeurs ; témoins plantés
(familles à issue connue) testent la sincérité des parieurs. Programme : la carte des hypothèses est un parieur parmi
d'autres, donc évaluée. Incopiable : chez un occupant, l'attaquant est un parieur initié — il sait où il frappera.

**Demande.** Ajout : registre de paris scellé par famille, règle de score ; modification mineure du règlement du juge.
**Coût** : processeur seul, dizaines de dollars d'appels. **Piège** : collusion entre parieurs ; familles fixées après
les paris ; parieurs qui apprennent le juge. **Cosmétique si** : le marché ne bat pas le meilleur parieur seul, ou
toutes les lignées sont calibrées pareil. **Antériorité** : SUPPOSÉ — marchés de prédiction de la réplication (Dreber et
al., 2015 ; Camerer et al., 2018) ; règles de score propres (Brier, 1950 ; Gneiting et Raftery, 2007) ; non vu pour la
prédiction d'angles morts de moniteurs. Jamais fait, à ma connaissance.


## Fiche T05 — Cartographie antigénique des familles

**Idée.** En virologie, la cartographie antigénique place souches et sérums dans un plan à partir des titres de réaction
croisée ; la distance prédit l'échappement d'une souche nouvelle. Nous plaçons moniteurs et familles dans un espace à
partir de la matrice de détection (moniteur × famille, sur le développement) ; la position d'une famille tenue à
l'écart, prédite depuis ses **seuls traits déclarés** par la troisième instance, sans la tester, prédit quels moniteurs
elle échappe. Prédicteur d'angles morts par géométrie, sans théorie, qui sert de **bras témoin** à Q3 : si la géométrie
prédit autant que la théorie, le pôle théorie est cosmétique (règle R4) ; si la théorie la bat, c'est le résultat fort.
Si le diffus forme une région séparée de la carte, Q4 reçoit une réponse géométrique.

**Loi prédictive.** Espace : familles tenues à l'écart × moniteurs. Prédiction : la géométrie prédit l'échec au-dessus
du hasard, aire ≥ 0,6 (signe +) ; la théorie la bat d'au moins 0,1 (signe +, prédiction de risque pour le programme) ;
les familles diffuses se séparent des concentrées sur un axe de la carte (signe +). Métrique : aire de prédiction
d'échec ; tension de la carte. Perdu : les traits déclarés forment une taxonomie ; la carte dépend de la génération.

**Questions servies.** Q3, Q4, Q5 (la carte se stabilise-t-elle de génération en génération ?).

**Avantage décisif.** Programme : familles tenues par un tiers avec traits déclarés sans test ; carte des hypothèses
comme compétiteur explicite. Originalité : l'emprunt.

**Demande.** Ajout : module de carte ; dépend de la troisième instance. **Coût** : processeur seul. **Piège** : la carte
apprend l'artefact de source (les régions sont les générateurs) ; dimension choisie après coup. **Cosmétique si** : carte
sans structure, ou recopiant une variable unique. **Antériorité** : SUPPOSÉ — Smith et al. (2004, cartographie
antigénique de la grippe) ; matrices de transfert entre domaines (Kumar, 2026, rapporté en pièce D) ; prédiction
d'échappement de moniteurs par carte : non vue. Jamais fait, à ma connaissance.


## Fiche T06 — Rejugement des courbes publiées sous juge figé à borne

**Idée.** Chaque occupant publie une courbe : génération après génération, la défense s'améliore contre son attaquant.
Ces courbes sont des suites de promotions prononcées par un juge qui dérive. On les rejoue sous **notre** juge : chaque
amélioration rapportée devient une mise d'un e-processus contre un nul d'archive ; on compte combien de leurs
promotions survivraient à une borne de fausses promotions, et à quelle génération un arrêt optionnel honnête les aurait
arrêtées. Sans rien lancer. Des courbes simulées sous le nul et sous effet vrai, insérées comme témoins plantés,
étalonnent la sévérité du rejugement.

**Loi prédictive.** Espace : courbes publiées (occupant, génération) avec tailles d'échantillon et dispersions
rapportées. Prédiction : la part des promotions rapportées qui survivent à la borne au niveau 0,05 est < 50 % (signe −)
et décroît avec la génération (signe −, dérive de Goodhart). Métrique : part survivante ; génération d'arrêt. Perdu : on
dépend de ce qu'ils rapportent (sans dispersion, pas de mise) ; on juge leur rapport, pas leur défense.

**Questions servies.** Q2 — tranche « résultat ou hygiène » : si la moitié des promotions publiées ne tient pas, le
juge garanti est un résultat ; Q5.

**Avantage décisif.** Organisme : le juge à mise et à borne existe. Méthodes : règle de rejugement préenregistrée avant
toute lecture de courbe (règle R1). Un occupant ne peut pas se l'appliquer sans conflit d'intérêt.

**Demande.** Rien ; un adaptateur d'entrée. **Coût** : processeur seul ; lecture des documents empreintés (R7).
**Piège** : chiffres transcrits non opposables ; nul choisi après avoir vu les courbes ; critique de rapport prise pour
résultat de défense. **Cosmétique si** : sur les témoins plantés, toutes les courbes survivent ou aucune.
**Antériorité** : SUPPOSÉ — analyse adaptative des données (Dwork et al., 2015) ; inférence universelle (Wasserman,
Ramdas, Balakrishnan, 2020) ; réanalyse statistique de courbes d'apprentissage par renforcement (Agarwal et al., 2021) ;
rejugement de courbes co-évolutives de sûreté : non vu.


## Fiche T07 — Comparaison clé : l'étalon voyageur d'épisodes

**Idée.** En métrologie, les laboratoires ne se mesurent pas les uns les autres : un étalon voyageur circule, chacun le
mesure, on calcule des degrés d'équivalence et une valeur de référence. Nous jouons le bureau des poids et mesures de la
course : un lot d'épisodes scellé par la troisième instance (traits déclarés, vérité connue, témoins plantés, artefact
contrôlé par appariement multi-générateur) est soumis, **lu une fois**, à chaque moniteur publié à poids ouverts et
rejoué sur chaque banc publié. On publie la matrice des degrés d'équivalence entre bancs d'occupants et un **budget
d'incertitude** décomposé (échantillonnage, artefact, juge, dérive), comme les études de répétabilité du contrôle
qualité. Le livrable est une norme de rapport. L'étalon est crédible parce que nous n'avons rien à y gagner : nous ne
faisons pas courir d'attaquant.

**Loi prédictive.** Espace : (banc publié, moniteur publié). Prédiction : les classements de moniteurs induits par deux
bancs d'occupants concordent faiblement, corrélation de rang < 0,5 (signe −) ; la part de variance due à l'artefact de
source dépasse celle due à la famille, ratio ≥ 1 (signe +). Métrique : degrés d'équivalence ; décomposition de variance.
Perdu : l'étalon a lui-même un générateur ; on ne mesure que ce qu'il porte.

**Questions servies.** Q6, Q-pont, Q2 (norme de rapport), et une question nouvelle : les bancs des occupants sont-ils
équivalents entre eux ?

**Avantage décisif.** Méthodes : neutralité par refus de l'attaquant, préenregistrement, test lu une fois. Organisme :
témoins plantés, juge figé. Incopiable : un occupant n'est pas neutre ; l'étalon doit être tenu par un tiers.

**Demande.** Troisième instance (tient l'étalon) ; ajout : appariement multi-générateur. **Coût** : processeur si
sorties publiées ; dizaines à centaines de dollars si réévaluations. **Piège** : l'étalon fuit après lecture (version
suivante obligatoire) ; tout échange avec un occupant est un contact externe, donc un nœud. **Cosmétique si** : tous les
bancs concordent, ou si l'incertitude est dominée par notre juge. **Antériorité** : SUPPOSÉ — arrangement de
reconnaissance mutuelle du Comité international des poids et mesures (1999), comparaisons clés ; accord entre bancs de
modèles de langage (Perlitz et al., 2024, titre à vérifier) ; non vue pour moniteurs de sûreté.


## Fiche T08 — Péché antigénique originel des défenses héritées

**Idée.** En immunologie, un organisme exposé d'abord à une souche répond à une souche voisine en réactivant sa mémoire
de la première, parfois moins bien qu'un organisme naïf. Notre organisme récompense l'héritage sur trois générations ou
plus (N-045-v2) : c'est la condition d'une empreinte. Hypothèse : une défense héritée généralise moins bien qu'une
défense neuve, à budget égal, sur une famille voisine mais distincte de sa première famille, et aussi bien ou mieux sur
une famille proche ou lointaine — courbe non monotone en distance dans la carte. Vraie, c'est une faille de notre
programme rendue mesurable ; fausse, l'héritage gagne un appui.

**Loi prédictive.** Espace : paires (défense héritée sur K ≥ 3, défense neuve à budget égal) × familles en trois bandes
de distance déclarées. Prédiction : différence de rappel (héritée − neuve) ≤ −0,05 dans la bande intermédiaire, ≥ 0 dans
la bande proche ; le creux est la signature. Métrique : différence de rappel à taux de fausses alertes fixé, appariée par
graine. Perte : trois bandes résument une courbe ; la distance dépend de la carte.

**Questions servies.** Q5, Q1 ; faille du programme (N-045-v2).

**Avantage décisif.** Les occupants n'ont ni familles graduées par une distance théorique ni témoins sans héritage
préenregistrés ; l'héritage est chez nous un paramètre explicite (organisme). Originalité : jamais posé sur des défenses
co-évoluées, à ma connaissance.

**Demande à l'organisme.** Ajout : bras « sans héritage » apparié ; stratification des familles par distance, fixée par la
troisième instance. **Coût** : simulateur jouet sur processeur ; version réelle = générations, dépense. **Piège** :
confusion avec la perte de plasticité générale (pire partout) — d'où la non-monotonie comme signature ; distance mesurée
après coup. **Cosmétique si** l'effet est uniforme sur les bandes, ou disparaît à nombre de paramètres égal.
**Antériorité** : SUPPOSÉ — Francis, « On the doctrine of original antigenic sin », Proceedings of the American
Philosophical Society 1960 ; Nikishin et al., « The Primacy Bias in Deep Reinforcement Learning », 2022 ; Dohare et al.,
« Loss of plasticity in deep continual learning », Nature 2024.


## Fiche T09 — Moniteurs mutants boîte blanche

**Idée.** En génie logiciel, on juge une batterie de tests par sa capacité à « tuer » des mutants, copies du programme où
l'on a planté un défaut connu. Transposition, côté défense seulement : on fabrique des moniteurs dont l'angle mort est
connu par construction — retrait d'une direction ou d'une couche d'activations de l'entrée d'une sonde, horizon tronqué
de l'agrégateur. On demande : l'épreuve tenue à l'écart et le juge figé déclassent-ils le mutant ? la boucle, partie du
mutant, répare-t-elle l'angle mort, et en combien de générations ? Ce sont des témoins plantés au niveau des défenses :
la vérité terrain sur la généralisation, qui manque partout, devient fabricable.

**Loi prédictive.** Espace : mutants à angle mort déclaré × familles étiquetées par classe. Prédiction : baisse de rappel
≥ 0,2 sur les familles touchant l'hypothèse retirée, aucune ailleurs (contrôle négatif) ; score de mutation de l'épreuve
≥ 0,8. Métrique : fraction de mutants tués, matrice mutant × famille. Perte : un angle mort chirurgical n'est pas
naturel ; on mesure la sensibilité de l'appareil, pas la fréquence des angles morts.

**Questions servies.** Q2 (le juge voit-il une fausse amélioration ?), Q6, Q5, Q3.

**Avantage décisif.** Boîte blanche sur poids ouverts (programme) : un occupant boîte noire ne peut retirer un canal
d'information ; un laboratoire fermé ne publie pas ses activations. La règle R5 (garde testée sur artefact) devient une
mesure. Originalité : transposition.

**Demande à l'organisme.** Ajout : générateur de mutants inscrit comme témoin planté. **Coût** : processeur sur
activations déjà extraites ; extraction nouvelle (modèle de 8 milliards d'abord) = dépense modeste, nœud. **Piège** :
mutants grossiers (tués par tout) ; mutants équivalents (information redondante ailleurs) ; tentation de tirer de la
matrice des familles plus dures — interdit, la matrice ne sert qu'à noter l'épreuve. **Cosmétique si** le score vaut ≈ 1
pour tous, ou si les équivalents dominent. **Antériorité** : SUPPOSÉ — DeMillo, Lipton, Sayward, « Hints on test data
selection », IEEE Computer 1978 ; Ravfogel et al., « Null It Out », 2020 ; Belrose et al., « LEACE », 2023 (effacement de
concepts). Usage pour noter une épreuve de généralisation : non vu.


## Fiche T10 — Mutants côté défense

**Idée.** Les occupants mesurent la puissance d'un banc en y lançant leur attaquant. Nous faisons l'inverse, emprunté au
test logiciel : on mute la **défense**. À partir d'un moniteur et de la carte des hypothèses, on fabrique des variantes
dont une hypothèse précise est délibérément affaiblie (clause retirée, seuil déplacé, fenêtre d'agrégation raccourcie,
canal coupé). Un banc de familles tenues à l'écart est puissant s'il « tue » le mutant (chute mesurable de détection) ;
un mutant qui survit révèle une hypothèse que le banc n'éprouve pas — une région où une défense évoluée peut dériver
sans que le juge le voie. Variante décisive : le **mutant aveugle au contenu**, qui ne garde que les traits de surface
(source, longueur, style) ; s'il n'est pas tué, le banc est séparable par l'artefact — un contrôle d'artefact sans aucun
attaquant, et un témoin planté « faux » pour le juge.

**Loi prédictive.** Espace : couples (banc, mutant d'une hypothèse h de la carte). Prédiction : le score de mutation
(part des mutants tués) est inférieur à 1 et les survivants se concentrent sur les hypothèses hors de la taxonomie du
banc, ratio de concentration ≥ 2 contre le hasard (signe +) ; pour le mutant aveugle, aire sous la courbe ≥ 0,6 sur un
banc d'occupant (signe +, artefact). Métrique : score de mutation ; aire du mutant aveugle. Perdu à la traduction : les
mutants sont nos mutants (biais de l'opérateur) ; un survivant peut être un « mutant équivalent » sans effet observable.

**Questions servies.** Q6 (artefact sans attaquant), Q3 (le banc comme instrument de puissance), Q-pont (pouvoir réel
d'un banc synthétique), Q2 (les mutants sont des témoins faux que le juge doit refuser).

**Avantage décisif.** Organisme : témoins plantés à vérité connue, côté défense. Programme : la carte des hypothèses
fournit une liste motivée d'opérateurs de mutation ; un occupant sans théorie explicite muterait au hasard, et son banc
est contaminé par son propre attaquant. Originalité : muter la défense pour mesurer la puissance du banc.

**Demande à l'organisme.** Ajout : un opérateur de mutation par clause de la carte ; rien au juge. **Coût** : processeur
seul sur scores précalculés ; quelques dizaines de dollars si réévaluation sur transcriptions. **Piège** : mutants
équivalents (gonflent la survie), mutants cassés (gonflent la mort). **Cosmétique si** : score de mutation ≈ 1 sur tout
banc, ou survivants sans concentration. **Antériorité** : SUPPOSÉ — analyse de mutants (DeMillo, Lipton, Sayward,
1978) ; mutation de réseaux pour évaluer des jeux de test (Ma et al., « DeepMutation », 2018) ; non vue sur des
moniteurs de sûreté ni pour le contrôle d'artefact. Jamais fait, à ma connaissance.


## Fiche T11 — Certificat d'étalonnage de la généralisation

**Idée.** Un métrologue ne publie pas un nombre sans budget d'incertitude décomposé par source, ni n'accepte un lot sans
plan d'échantillonnage à double risque (producteur, consommateur). Personne dans la course ne publie « généralise aux
familles tenues à l'écart » ainsi. On en fait une norme de rapport : composantes « tirage des familles » (effet
aléatoire), « artefact de source » (fiche 6), « dérive du juge » (témoins plantés), « graines et ordre » ; et un plan
d'acceptation : combien de familles pour certifier un rappel ≥ r à risques α et β donnés. Puis on applique le budget aux
tableaux par catégorie publiés par les occupants : leurs résultats deviennent notre matériau, sans rien exécuter.

**Loi prédictive.** Espace : tableaux par famille publiés (liste gelée) et nos mesures. Prédiction : la composante
« tirage des familles » fait ≥ 50 % de la variance de la généralisation, et la majorité des affirmations publiées reposent
sur moins de familles que le plan n'en exige à α = β = 0,1. Signe positif (affirmations sous-dimensionnées). Métrique :
part de variance de la famille ; familles requises contre publiées. Perte : tableaux publiés arrondis, souvent sans
détail par famille.

**Questions servies.** Nouvelle (norme de rapport) ; Q3 et Q5 (puissance avec une dizaine de familles) ; Q2.

**Avantage décisif.** La composante « dérive du juge » n'est mesurable qu'avec un juge figé et des témoins plantés
(organisme) ; un occupant à juge-modèle co-évolutif ne peut pas l'isoler. Originalité : transposition, sauf cette
composante, inédite à ma connaissance.

**Demande à l'organisme.** Rien de neuf ; un module d'analyse et une liste gelée de tableaux, lus sur documents originaux
empreintés (R7). **Coût** : processeur seul. **Piège** : résultat attendu (« trop peu de familles ») donc suspect de
propreté (R4) ; ré-analyse de chiffres arrondis ; lecture comme dénigrement. **Cosmétique si** le budget ne change aucune
conclusion publiée ni notre ordre (par exemple sur Q3). **Antériorité** : SUPPOSÉ — Comité commun pour les guides en
métrologie, « Guide pour l'expression de l'incertitude de mesure », 2008 ; Dodge et Romig, plans d'échantillonnage
(1929-1959) ; Miller, « Adding Error Bars to Evals », 2024.


## Fiche T12 — Capture-recapture des angles morts

**Idée.** En écologie, on estime le nombre d'espèces jamais observées à partir du recouvrement entre campagnes de piégeage
indépendantes et du nombre d'espèces vues une seule fois. Transposition : chaque source indépendante qui révèle des angles
morts d'une défense est un « piège » — prédictions scellées du pôle théorie, familles fixées par la troisième instance,
familles publiées par les occupants (lues par classe), audit à taxonomie fixée. Chaque angle mort est identifié par la
classe d'hypothèse de moniteur qu'il viole, jamais par son contenu. Le recouvrement donne une estimation du nombre d'angles
morts encore invisibles et de la probabilité que la prochaine famille inédite tombe dans une classe jamais vue. Réponse
chiffrée à « combien reste-t-il à découvrir ? », que personne ne fournit en contrôle.

**Loi prédictive.** Espace : défenses évoluées par l'organisme × familles d'une rotation à venir. Prédiction : la
couverture estimée (estimateur de Good-Turing, corrigé à la Chao) prédit la fraction de familles de la rotation suivante
qui violent une classe jamais vue, à ± 0,15 près, mieux que les références « tout est nouveau » et « rien n'est nouveau ».
Métrique : erreur absolue couverture prédite contre observée. Perte : l'angle mort réduit à sa classe ; la richesse
dépend de la granularité de la carte.

**Questions servies.** Q3, Q5 ; nouvelle : « combien d'angles morts restent invisibles ? ».

**Avantage décisif.** L'estimateur exige des pièges indépendants. Un occupant qui construit l'attaquant n'a qu'un piège,
corrélé à sa défense : recouvrement dégénéré. Nous avons par construction des sources séparées (programme : théorie et
troisième instance ; méthodes : refus de l'attaquant). Copie coûteuse : il faudrait réorganiser leur séparation des rôles.

**Demande à l'organisme.** Ajout : module d'estimation ; étiquetage des angles morts par classe, par un tiers figé.
**Coût** : processeur seul. **Piège** : dépendance entre pièges (théorie et troisième instance partagent la carte →
recouvrement gonflé) ; capturabilité hétérogène ; granularité choisie après coup. **Cosmétique si** l'estimation ne bat
pas les références naïves, ou varie d'un facteur 2 selon la granularité. **Antériorité** : SUPPOSÉ — Good, Biometrika
1953 ; Chao, Scandinavian Journal of Statistics 1984 ; Böhme, « STADS: Software Testing as Species Discovery », ACM
Transactions on Software Engineering and Methodology 2018 (bogues de logiciel). En contrôle : non vu.


## Fiche T13 — Argument hybride sur les activations

**Idée.** En cryptographie, on passe d'une distribution à une autre par une chaîne d'hybrides, un composant à la fois ;
l'écart total est la somme des écarts entre voisins, et l'étape où il se concentre désigne le coupable. Pour la
question-pont : entre un épisode synthétique portant la propriété P et un épisode réel apparié, on construit des hybrides
en remplaçant un composant à la fois, d'abord dans le texte (contexte, actions, sorties d'outils), puis dans les
activations, couche par couche. Le profil de l'écart de détection dit si le transfert échoue à cause de P (écart concentré
là où P vit) ou d'un artefact de fabrication (écart diffus, ou sur un composant étranger à P).

**Loi prédictive.** Espace : paires synthétique/réel appariées sur P, corpus réels publics déclarés. Prédiction : si la
voie synthétique est valide, ≥ 60 % de l'écart se concentre sur l'étape qui porte P ; concentration hors P = pont cassé
pour cette propriété. Métrique : part de l'écart par étape, intervalle par rééchantillonnage. Perte : les activations
substituées sont des états non naturels ; l'ordre des étapes change la décomposition (en geler deux).

**Questions servies.** Q-pont (directement), Q6, Q3.

**Avantage décisif.** La moitié « activations » exige poids ouverts et boîte blanche (programme) ; un occupant boîte noire
ne décompose que le texte. Originalité : l'argument hybride comme protocole de mesure du transfert simulation-réel : non vu.

**Demande à l'organisme.** Modification du protocole de la question-pont ; outil de substitution d'activations.
**Coût** : texte avec la référence boîte noire locale, processeur ; activations, dépense modeste, nœud. **Piège** :
hybrides incohérents qui font chuter tout moniteur ; composant « hors P » corrélé à P ; puissance par propriété.
**Cosmétique si** l'écart se répartit uniformément quelle que soit P, ou si les deux ordres désignent des coupables
différents. **Antériorité** : SUPPOSÉ — Goldwasser et Micali, « Probabilistic Encryption », 1984 ; Meng et al.,
« Locating and Editing Factual Associations in GPT », 2022 ; interventions d'échange de Geiger et al. RAPPORTÉ (pièce B) :
Kadian et al. 1912.06321.


## Fiche T14 — Classes latentes : le taux de détection sur le réel non instruit

**Idée.** La question-pont bute sur « le réel est presque toujours instruit » : tout épisode réel étiqueté a été
commandé ou fabriqué. L'évaluation des tests diagnostiques **sans étalon-or** estime sensibilité et spécificité de
plusieurs tests à partir de leurs seules concordances, sous indépendance conditionnelle, avec au moins trois tests et
deux populations. Avec trois moniteurs ou plus sur des traces d'agents réelles, publiques, **non étiquetées et non
instruites**, on estime leurs taux de détection sur le réel et on les compare aux taux mesurés sur le synthétique à
propriété P. C'est la question-pont sans instruire le réel — chemin que le refus de l'attaquant rend nécessaire pour
nous et inutile pour les occupants, qui ont leurs étiquettes.

**Loi prédictive.** Espace : (triplet de moniteurs, corpus non instruit, propriété P). Prédiction : le classement des
moniteurs par sensibilité estimée sur le réel concorde avec le classement sur synthétique P, corrélation de rang ≥ 0,6
(signe +) ; la prévalence latente estimée est faible mais non nulle. Métrique : erreur sur témoins plantés insérés à
prévalence connue ; stabilité selon le troisième moniteur choisi. Perdu : la classe latente « positive » n'a pas de
nom — on ne sait pas si elle est le sabotage ; l'indépendance conditionnelle est une hypothèse.

**Questions servies.** Q-pont, Q4 (prévalence latente du diffus), Q7.

**Avantage décisif.** Méthodes : le refus de construire l'attaquant force cette voie ; contre-lecture par un autre
modèle et témoins plantés contrôlent l'identifiabilité. Originalité forte.

**Demande.** Un module ; des traces publiques ; rien au juge. **Coût** : processeur seul. **Piège** : la classe latente
capture le trait dominant du corpus (longueur, langue, domaine), même critique que Q6. **Cosmétique si** : la classe
latente est recouvrée par le prédicteur sur traits de surface (bras de N-029), ou l'estimation varie du simple au
triple selon le troisième moniteur. **Antériorité** : SUPPOSÉ — Hui et Walter (1980) ; Dawid et Skene (1979) ;
Platanios, Blum, Mitchell (2014, estimation de l'exactitude sans étiquettes) ; non vue pour des moniteurs de sabotage.
Jamais fait, à ma connaissance.


## Fiche T15 — Capture–recapture entre canaux : la masse cachée

**Idée.** Les occupants rapportent un taux de détection sur les attaques qu'ils connaissent — les leurs. La quantité
que le domaine attend est « combien en manque-t-on ? ». L'épidémiologie estime la taille d'une population cachée à
partir du recouvrement de deux listes partiellement indépendantes. Nos deux canaux (sonde boîte blanche sur poids
ouverts, moniteur boîte noire) produisent deux listes d'épisodes signalés ; leur recouvrement estime le nombre
d'épisodes positifs qu'aucun canal n'a vus, sans connaître la vérité. Les témoins plantés positifs, à taux connu,
étalonnent l'estimateur. Le mélange boîte blanche / boîte noire cesse d'être une fusion : il devient un **instrument de
mesure** de ce que la fusion ne voit pas.

**Loi prédictive.** Espace : triplets (famille tenue à l'écart, génération, paire de canaux). Prédiction : la masse
cachée estimée sur le développement prédit le taux d'échec prononcé par le juge sur l'épreuve, corrélation de rang
≥ 0,5 (signe +) ; sur les familles diffuses, la masse cachée dépasse celle des concentrées d'un facteur ≥ 1,5 (signe +).
Métrique : erreur relative sur les témoins plantés ; corrélation de rang. Perdu : l'indépendance des canaux est fausse
par construction (même modèle sous-jacent) — estimateurs à dépendance, donc un indicateur, pas une borne.

**Questions servies.** Q7 (la dynamique du mélange se mesure par la masse cachée), Q4, et une question nouvelle : quelle
part des positifs échappe à tous les canaux, et baisse-t-elle de génération en génération ?

**Avantage décisif.** Programme : deux canaux sur poids ouverts ; un occupant 100 % boîte noire n'a qu'une liste.
Organisme : témoins plantés pour étalonner. Originalité : fournir la mesure que personne ne donne.

**Demande.** Ajout d'un module d'estimation ; rien au juge. **Coût** : processeur seul sur scores existants ;
activations : quelques centaines de dollars. **Piège** : la dépendance positive des canaux sous-estime la masse cachée —
biais rassurant, le plus dangereux ; par symétrie (règle R4), « zéro caché » est suspect. **Cosmétique si** : l'erreur
sur témoins dépasse l'écart entre familles, ou l'estimateur recopie le taux du meilleur canal.
**Antériorité** : SUPPOSÉ — Lincoln–Petersen ; Chao (1987) pour populations hétérogènes ; capture–recapture pour les
défauts logiciels (Eick et al., 1992) ; non vue pour des moniteurs de sûreté. Jamais fait, à ma connaissance.


## Fiche T16 — Le concurrent comme troisième instance

**Idée.** Le meilleur générateur de familles tenues à l'écart que nous ne contrôlons pas, c'est l'occupant qui construit
l'attaquant. Nous scellons, avant leur parution, des prédictions dérivées de la carte des hypothèses : pour chaque classe
de moniteur publiée (par épisode, sonde, moniteur à état, agrégateur séquentiel), quelles classes d'hypothèses les
prochaines familles publiées violeront, et le signe de l'écart de détection par catégorie. À chaque parution (nouvelle
version de SLEIGHT-Bench, SafeCoEvo, travaux de l'institut britannique), une règle de correspondance gelée d'avance
traduit leurs catégories en nos classes ; le juge figé note une fois. Leur attaquant devient notre test final, lu une
fois, que nous n'avons pas pu contaminer.

**Loi prédictive.** Espace : couples (classe de moniteur, catégorie de famille) publiés après la date de scellement,
dans une liste d'occupants déclarée. Prédiction : signe de l'écart à la moyenne du papier correct dans ≥ 65 % des couples,
contre 50 % et contre une référence de persistance (le classement du papier précédent). Métrique : score logarithmique
des probabilités scellées, écart à la persistance. Perte : catégories publiées grossières ; ni calendrier ni taille sous
notre contrôle.

**Questions servies.** Q3 (directement), Q-pont (le réel publié comme épreuve), Q1.

**Avantage décisif.** Incopiable par construction : un occupant ne peut préenregistrer de prédiction crédible sur son
propre attaquant (il le conçoit, il voit ses échecs). Source : la marque (refus) et les méthodes (scellement avant
lecture). Originalité : jamais fait, à ma connaissance.

**Demande à l'organisme.** Ajout : registre de prédictions sur tiers, veille gelée (liste d'occupants, règle de
correspondance). Un horodatage public de l'empreinte serait une publication → nœud pour Lazar. **Coût** : processeur seul.
**Piège** : peu d'événements en douze mois ; règle de correspondance écrite en connaissant leurs catégories antérieures ;
prédictions triviales si un occupant republie le même motif. **Cosmétique si** on ne bat pas la persistance, ou si la
règle doit être retouchée après lecture. **Antériorité** : SUPPOSÉ — DellaVigna, Pope, Vivalt, « Predict science to
improve science », Science 2019 (prévision de résultats d'études). Prévision théorique scellée de bancs d'autrui : non vu.
