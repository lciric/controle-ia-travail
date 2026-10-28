# Fiches du proposeur « Fable » — huit approches inédites pour la course à la défense universelle co-évolutive

Prise « idéation » : je propose, je ne teste rien. Niveau méthode seulement, aucune technique d'attaque, aucune
recherche web ; toute antériorité est SUPPOSÉE de mémoire (rien n'est vérifié sur document empreinté, règle R7) ; les
« jamais fait » sont des inférences par absence (règle R8). Cinq fiches (1, 2, 3, 6, 8) portent, à ma connaissance,
quelque chose que personne n'a fait nulle part. Fil commun : on ne construit pas l'attaquant, donc on mesure autre
chose que les occupants.

---

## Fiche 1 — Mutants côté défense

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

---

## Fiche 2 — Capture–recapture entre canaux : la masse cachée

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

---

## Fiche 3 — Classes latentes : le taux de détection sur le réel non instruit

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

---

## Fiche 4 — Comparaison clé : l'étalon voyageur d'épisodes

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

---

## Fiche 5 — Rejugement des courbes publiées sous juge figé à borne

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

---

## Fiche 6 — Marché de prédiction des angles morts

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

---

## Fiche 7 — Rejeu contre ancêtres congelés

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

---

## Fiche 8 — Cartographie antigénique des familles

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

---

## Classement proposé (sous les deux critères de Lazar)

1. Fiche 1 (mutants) — avantage décisif par la carte des hypothèses, gratuit, sert quatre questions.
2. Fiche 3 (classes latentes) — lève le piège central de la question-pont, inédit.
3. Fiche 2 (capture–recapture) — la mesure que le domaine attend, inédit.
4. Fiche 5 (rejugement) — tranche Q2, retourne les occupants en matériau, gratuit.
5. Fiche 6 (marché) — inédit, mais partage la faible puissance de Q3.
6. Fiche 8 (cartographie) — précieux surtout comme bras témoin de Q3.
7. Fiche 4 (étalon voyageur) — fort, mais touche au contact externe (nœud).
8. Fiche 7 (ancêtres congelés) — antériorité la plus proche ; hygiène de Q5.
