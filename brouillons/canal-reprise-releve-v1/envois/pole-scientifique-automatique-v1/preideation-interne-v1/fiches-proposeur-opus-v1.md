# Fiches du proposeur « Opus » — tour d'idéation interne, huit approches inédites — v1

Proposeur : Opus 5.5, sous-agent, prise « idéation ». Écrit à partir du relevé `date -u` de 13:43:18 UTC, 28 octobre 2026.
Régime exploratoire : rien d'opposable. Aucune recherche web. Toute antériorité est SUPPOSÉE de mémoire, sauf celles
RAPPORTÉES des pièces lues (elles-mêmes non vérifiées sur document original). Niveau méthode seulement : aucune fiche ne
conçoit, ne décrit ni n'étend un mode d'attaque ; les familles ne sont désignées que par la classe d'hypothèse de
moniteur qu'elles violent.

Jamais faites nulle part, à ma connaissance : fiches 2, 5, 6, 7. Transpositions d'un autre champ : fiches 1, 3, 4, 8.

---

## Fiche 1 — Capture-recapture des angles morts

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

## Fiche 2 — Le concurrent comme troisième instance

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

## Fiche 3 — Moniteurs mutants boîte blanche

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

## Fiche 4 — Argument hybride sur les activations

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

## Fiche 5 — Péché antigénique originel des défenses héritées

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

## Fiche 6 — Deux distances, une seule vraie

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

## Fiche 7 — Contrats hypothèse-garantie et défaillances coïncidentes

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

## Fiche 8 — Certificat d'étalonnage de la généralisation

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

---

## Réserves du proposeur

1. Toutes les antériorités « SUPPOSÉ » sont de mémoire, non vérifiées ; « non vu » veut dire absent de ma mémoire et des
   pièces, pas absent du champ (R8).
2. Les fiches 1, 3, 6 et 8 dépendent de la troisième instance ou d'un tiers qui étiquette par classe d'hypothèse : sans
   elle, leur avantage tombe à une distinction.
3. Les seuils chiffrés sont des propositions de proposeur, à resserrer au gel ; aucun n'a été tiré de données.
4. Point commun à toutes : la carte des hypothèses sert de coordonnées ; si elle a été ajustée sur des échecs observés,
   les fiches 1, 2, 5, 6, 7 héritent la circularité.
