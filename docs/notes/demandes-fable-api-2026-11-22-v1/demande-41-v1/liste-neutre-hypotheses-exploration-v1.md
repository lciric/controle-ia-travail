# Hypothèses, mécanismes et stratégies d'exploration d'idées et d'allumage d'une idée : liste neutre (v1)

Un système d'idéation fait de plusieurs modèles de langue (proposeurs de familles différentes, juges, tests sur des mondes à vérité plantée, juge statistique calculé hors des modèles, registre des tentatives transmis d'une génération à la suivante) cherche des idées rares, justes et fécondes. Voici la liste des hypothèses, mécanismes et stratégies déjà envisagés pour l'exploration et pour l'« allumage » d'une idée, avec leur état.

**États employés.**
- « éprouvé ici » : un essai, une course ou un calcul a tourné dans ce système, avec un résultat écrit.
- « éprouvé dans la littérature, non rejoué ici » : résultat publié, lu, jamais rejoué dans ce système.
- « conçu, non joué » : code, plan d'expérience ou démonstration écrits, sans résultat.
- « proposé » : idée avancée par une personne ou un modèle, critiquée ou non. Une proposition d'un modèle n'est jamais un résultat.
- « fixé comme règle sans mesure » : règle ou cadre adopté par décision, sans mesure.

Quand deux états s'appliquent à deux parties d'une entrée, les deux sont donnés.

**Vocabulaire.** Un « bassin » est une classe d'idées. Un bassin « étroit » reçoit peu de masse sous la loi des propositions. Un « puits » est un bassin étroit et profond, c'est-à-dire juste et rare. Une « fiche » ou « carte » est une idée écrite par un proposeur. Le « nul » est l'ensemble des lois déjà connues contre lequel le juge statistique teste une idée. Une « valeur e » est une statistique de test valide sous arrêt optionnel. L'« archive » est l'ensemble des idées déjà retenues. La « vue » est ce qu'on montre aux proposeurs. L'« oracle » est la vérité plantée d'un monde de test.

---

## En tête : un échec technique

Une première course d'un organisme dédié aux bassins étroits a échoué avant toute proposition, pour une raison technique (authentification), sans résultat sur l'exploration ; elle n'a pas été relancée.

---

## Famille A — Cadre, bornes et impossibilités (15 entrées)

**A1. Borne amont : rien en aval des proposeurs ne crée de découverte.**
Affirme : la probabilité qu'un bassin reçoive au moins une proposition en k appels vaut 1 − (1 − p)^k. Le regroupement, le juge et la sélection ne l'augmentent pas. On ne peut que changer la vue, changer les proposeurs, ou ne rien perdre.
État : proposé. Sort : retenu comme cadre par toutes les sources ; énoncé élémentaire, non contesté.

**A2. Pas de vue uniformément meilleure ; pas de repas gratuit ; aiguille parmi M candidats.**
Affirme : la somme des probabilités de bassins disjoints vaut au plus 1. Sans structure, aucune méthode ne bat le tirage indépendant sur tous les mondes. Un puits placé uniformément parmi M candidats indiscernables est trouvé avec une probabilité au plus k/M. Référence citée : Nisan et Szegedy, 1994, « On the degree of Boolean functions as real polynomials ».
État : proposé (théorèmes cités de mémoire, non vérifiés). Sort : retenu comme cadre ; en découle la règle « nommer la structure qu'une méthode exploite ».

**A3. Barrière de parité.**
Affirme : une interaction de k traits sans effet marginal d'ordre inférieur ne laisse aucun palier. La trouver demande de l'ordre du nombre de sous-ensembles de k traits. Références : Kearns, 1998, « Efficient noise-tolerant learning from statistical queries » ; Blum et al., 1994, « Weakly learning DNF and characterizing statistical query learning using Fourier analysis ».
État : proposé. Sort : retenu ; fonde les mondes « sans parent » comme témoin négatif (voir J3).

**A4. Chaînes et horizon.**
Affirme : le temps de découverte d'une chaîne d'idées est une somme de temps d'attente. L'horizon en générations borne la profondeur atteignable.
État : proposé. Sort : retenu ; seules deux méthodes de la liste visent la profondeur en chaîne (F2, F3).

**A5. Seuil de détectabilité n·r·Δ.**
Affirme : un effet confiné à une région de masse r, de profondeur Δ, n'est détecté que si n·r·Δ dépasse un seuil (plus le logarithme de m/α pour m tests). Aucune stratification ni pari localisé ne le franchit. L'arrêt optionnel ne le déplace qu'en dépensant plus de tirages. Une forme voisine pondère par 2^(−L) (rasoir d'Occam).
État : proposé. Sort : retenu.

**A6. Auto-localisation.**
Affirme : si une carte égale le nul hors de sa région, sa valeur e globale est déjà sa valeur e locale.
État : proposé (identité démontrée au cours d'un tour de critique). Sort : retenu ; elle fait tomber L2.

**A7. Fermeture du nul et copies par morceaux.**
Affirme : une carte du nul a une valeur e au plus 1. Un nul assez large pour couvrir toutes les copies peut aussi contenir les découvertes. Un nul de mélanges à poids constants ne couvre pas le recollage par morceaux.
État : proposé. Sort : retenu ; la garde est à qualifier avant toute comparaison.

**A8. Deux étroitesses distinctes.**
Affirme : une idée peut être rare sous la loi des propositions, ou invisible en moyenne dans les données. Ce sont deux problèmes différents.
État : proposé. Sort : retenu ; la vue traite le premier, le juge et le regroupement le second.

**A9. La largeur d'un bassin n'est pas un réglage du monde.**
Affirme : la largeur dépend du modèle, de la vue et de l'archive. Elle s'estime sur des mondes d'étalonnage.
État : proposé. Sort : retenu ; contredit une formulation antérieure qui parlait de « régler la largeur ».

**A10. Danger commun : la pression vers l'inédit pousse vers la classe que le nul ne couvre pas.**
Affirme : pousser vers l'inédit favorise les formes que le nul ne contient pas (lois conditionnelles « si… sinon », mélanges), et donc les fausses découvertes faciles.
État : proposé (plusieurs sources convergent). Sort : retenu ; préalable : un banc qui certifie la garde et la puissance.

**A11. Le taux de base de la queue.**
Affirme : si la part d'idées vraies dans la queue tombe sous le taux d'erreur de la vérification, presque toutes les confirmations sont fausses. Toute poussée vers le rare produit alors surtout des fausses découvertes.
État : proposé (tranché par calcul entre modèles ; limite de principe, non mesurée). Sort : retenu ; non mesuré.

**A12. Impossibilité d'un budget borné sans borne inférieure sur la fréquence ; garantie disjonctive.**
Affirme : sans borne inférieure connue sur p, aucun budget fini ne garantit le succès. Seule tient sans condition la garantie « succès, ou certificat que p < ε ». Références : Halmos, 1946, « The theory of unbiased estimation » ; Bahadur et Savage, 1956, « The nonexistence of certain statistical procedures in nonparametric problems ».
État : proposé (deux modèles). Sort : non tranché.

**A13. L'adaptativité consomme la validité du juge.**
Affirme : chaque usage adaptatif des verdicts du juge réduit leur validité. Référence : Dwork et al., 2015, « The reusable holdout: Preserving validity in adaptive data analysis ».
État : proposé. Sort : retenu dans l'esprit des règles du système (aucun score du juge ne pilote les proposeurs) ; une question liée reste non tranchée.

**A14. Identité des idées.**
Affirme : deux cartes proches en prédiction peuvent venir d'idées différentes. L'équivalence fonctionnelle n'est décidable que dans une grammaire bornée.
État : proposé. Sort : retenu (voir J7).

**A15. On force la proposition à prix connu, pas la découverte.**
Affirme : toute garantie vient d'une composante mécanique maîtrisée (énumération, mélange défensif, rejet exact, stratification). On ne force la découverte que si l'évidence disponible paie la longueur de description de l'idée.
État : proposé (un modèle). Sort : non tranché.

---

## Famille B — Bases à battre et témoins (9 entrées)

**B1. Tirages indépendants à coût égal ; meilleur de N.**
Affirme : toute méthode se juge contre N tirages indépendants au même budget, compté en jetons facturés. Le témoin vaut 1 − (1 − w)^N. Un protocole publié fixe déjà des règles de « budget égal ».
État : fixé comme règle sans mesure ; éprouvé dans la littérature, non rejoué ici (une méthode publiée de reprise à contexte neuf : meilleur de 4 à 0,54 contre 0,47).
Sort : retenu comme base obligatoire ; la prétention de nouveauté du protocole a été retirée (déjà publié).

**B2. Tirage au hasard dans la grammaire.**
Affirme : des lois tirées au hasard dans la grammaire servent de base. Si un proposeur à modèle ne fait pas mieux, l'apport du proposeur tombe. 13 % des lois aléatoires de la grammaire portent un gain d'au moins 0,02.
État : conçu, non joué (seulement à blanc, avec des doublures scriptées ; la course réelle n'avait pas ce bras).
Sort : retenu comme base ; jamais joué contre de vrais proposeurs.

**B3. Chercheur mécanique sans modèle ; énumérateur ordonné par longueur ; recombinaison mécanique bornée.**
Affirme : un programme ajuste ou énumère les lois de la grammaire (par exemple au critère de Schwarz). Si un proposeur à modèle ne fait pas mieux, l'apport de l'exploration tombe. En pire cas, c'est la meilleure garantie.
État : éprouvé ici, en partie (sur processeur, résultat seulement cité : le chercheur mécanique trouvait 23 sur 35 dans une première grammaire, qui a ensuite été changée pour qu'il ne domine plus ; aucun fichier de résultat) ; la variante « énumérateur ordonné et valeurs e pondérées » est proposée.
Sort : retenu comme base obligatoire partout.

**B4. Énumération exhaustive de la grammaire.**
Affirme : si le langage est fini et que le budget couvre le support, le succès est certain.
État : proposé. Sort : non tranché.

**B5. Témoins placebo.**
Affirme : séparer l'information servie de sa seule présence, de sa forme, de la perturbation du contexte ou de l'effectif. Formes : vue placebo de même format et longueur (table tirée au hasard) ; monde jumeau ; cartes ou lignes d'un autre monde ; même découpage sans le mécanisme ; réallocation au hasard ; témoin à 1,2 fois les tirages ; mondes sans la structure visée ; permutation commune des noms de traits.
État : proposé ; le placebo de réallocation a servi dans l'essai d'allocation avec arrêt anticipé (K1, éprouvé ici).
Sort : retenu ; jugés réutilisables tels quels.

**B6. Reprise du meilleur à contexte neuf.**
Affirme : reprendre la meilleure idée dans un contexte vidé bat la continuation. Méthode publiée (« Fork-and-Flush ») : 0,78 contre 0,47 et 0,54, sur 13 tâches.
État : éprouvé dans la littérature, non rejoué ici ; fixé comme règle sans mesure (témoin d'une course à plusieurs générations).
Sort : retenu.

**B7. Pseudo-familles.**
Affirme : une famille de modèles coupée au hasard en deux sert de témoin à la pluralité des familles.
État : proposé. Sort : retenu par une synthèse ; non mesuré.

**B8. Témoin « popularité seule » et rétrodiction inversée.**
Affirme : pour juger une recombinaison de domaines, comparer à un prédicteur qui n'utilise que la popularité des domaines, et à une rétrodiction inversée dans le temps.
État : fixé comme règle sans mesure (gabarit obligatoire sur la littérature réelle, avec six garde-fous) ; non joué. Sort : retenu.

**B9. Témoins de composition.**
Affirme : pour juger un échange entre proposeurs, comparer à « même effectif, sans échange » et à « chaque fournisseur seul, k tirages, coût apparié », avec une garde de troncature par bras.
État : fixé comme règle sans mesure (prévu pour une étape ultérieure). Sort : retenu ; non joué.

---

## Famille C — Choisir ce qu'on explore : vue, focalisations, trous, hors des bassins connus (19 entrées)

**C1. Stratégie « hors des bassins déjà retenus ».**
Affirme : le proposeur vise un couple (cible, trait) qu'aucune fiche retenue ne couvre encore. Variante voisine : viser un trait que le prédicteur déjà connu pèse peu.
État : conçu, non joué (codée, essayée en simulation par un tirage uniforme parmi les couples libres).
Sort : adoptée par décision, non mesurée ; antécédent de C3.

**C2. Catalogue de stratégies déclarées, à liberté bornée.**
Affirme : le proposeur déclare la stratégie employée parmi une liste (loi monotone d'un trait ; interaction de deux traits ; différence entre sous-populations ; correction éliminée ; transposition d'une cible à une autre ; loi ajustée sur un jeu de développement ; plus C1). On mesure lesquelles produisent des idées retenues. Lecture fixée d'avance : « l'exploration fait retenir au moins une fiche par sous-population ».
État : éprouvé ici, en partie (sur processeur, avec proposeur scripté, aveugle contre exploration : l'avantage espéré ne s'est pas montré, une fiche retenue dans chaque bras) ; aucune mesure par stratégie avec un vrai modèle.
Sort : non tranché ; la lecture fixée n'est pas tenue dans le sens espéré.

**C3. Table des paires de traits que l'archive ne croise pas.**
Affirme : servir l'archive entière avec la table binaire des paires de traits non croisées. Un proposeur y verrait où écrire une interaction. Plusieurs méthodes plus savantes (décomposition de l'archive, graphe de dépendance, table des produits absents, cavités d'un complexe simplicial, table de Walsh) se ramènent à cette forme minimale.
État : proposé ; jamais éprouvé.
Sort : retenue au deuxième rang d'une synthèse, non tranchée. Objection centrale : aucun fait ne dit que la vue change la loi des propositions.

**C4. Décomposition orthogonale de l'archive par inversion de Möbius.**
Affirme : décomposer l'archive en termes d'interaction orthogonaux pour voir ce qui manque.
État : proposé. Sort : écartée ; sous traits dépendants, les termes ne sont ni uniques ni orthogonaux ; se réduit à C3.

**C5. Code couvrant sur les sous-ensembles de traits.**
Affirme : couvrir tous les sous-ensembles de traits d'une taille donnée en peu d'appels.
État : proposé. Sort : écarté ; une idée est une fonction, non un sous-ensemble.

**C6. Homologie de l'archive (homologie persistante, cavités simpliciales).**
Affirme : les trous topologiques de l'archive indiquent où chercher.
État : proposé. Sort : écartée ; trop peu de lois et de traits ; se ramène à C3.

**C7. Plan combinatoire qui répartit des focalisations.**
Affirme : chaque combinaison de t facteurs est mise devant au moins un appel (tableaux couvrants ou orthogonaux de force t, plans factoriels fractionnaires, « couvrir toutes les paires en peu de fiches », focalisation sur une strate tirée au sort par proposeur). Un plan équilibré ne fait pas moins bien que des blocs indépendants (inégalité proposée par un modèle).
État : proposé ; une borne éprouvée ici par calcul exhaustif (tableaux couvrants binaires de force 2 : 3 facteurs pour 4 appels, 4 pour 5, 10 pour 6, 15 pour 7 ; la formule avancée d'abord était fausse).
Sort : retenu au troisième rang, seulement si C3 montre un levier.

**C8. Dictionnaire de directions par moments orthogonaux.**
Affirme : servir des directions de recherche tirées de moments orthogonaux des données.
État : proposé. Sort : maintenu avec corrections ; risque de coïncidence avec le monde planté.

**C9. Tirage déterminantal et répulsion.**
Affirme : favoriser des lots dissemblables (processus ponctuel déterminantal sur les vues ; noyau de recombinaison ; sélection répulsive ; tirage déterminantal des représentants ; ensembles à faible dispersion ; répulsion en plongement). Garantie sous indépendance des réponses : pas pire que le tirage indépendant de mêmes marges.
État : éprouvé ici pour la recombinaison (sur processeur : le noyau d'origine n'était pas semi-défini positif, 1 000 violations sur 1 000 ; la forme corrigée perd 4,8 et 2,2 points contre le tirage stratifié sur des ponts plantés) ; proposé pour les vues.
Sort : noyau d'origine écarté, tirage stratifié par défaut ; sur les vues, maintenu pour un duel séparé ; « diversité des vues, non des sorties ».

**C10. Plan sur des vues équivalentes.**
Affirme : servir des vues équivalentes (renommage des traits, inversion d'un codage) pour décorréler les réponses.
État : proposé. Sort : suspendu à un essai d'équivariance.

**C11. Acquisition par variance d'un processus gaussien.**
Affirme : diriger les appels vers la zone d'incertitude maximale d'un processus gaussien.
État : proposé. Sort : écartée ; revient soit à servir un verdict, soit à primer l'éloignement de l'archive.

**C12. Focalisations tirées des résidus ; balayage multi-échelles ; canal d'exemples publics avec issues.**
Affirme : des données publiques avec issues, disjointes des tirages du juge, rendraient visible une composante nulle en moyenne (par exemple une table croisée sur 2 000 exemples publics, ou un placebo par monde jumeau).
État : conçu, non joué (note de conception avec devis).
Sort : non tranché ; renvoyé à une décision, car une donnée nouvelle entre dans la vue.

**C13. Portefeuille de questions servies (missions).**
Affirme : chaque appel reçoit une mission tirée par permutation scellée, ou une consigne de diversité tirée au sort.
État : proposé ; éprouvé dans la littérature, non rejoué ici (une consigne de diversité n'a eu aucun effet mesurable sur la branche retenue ; précédent nul, 46 % contre 50 %).
Sort : différé jusqu'à savoir si le monde offre des bassins étroits et si les proposeurs les prennent.

**C14. Exclure le banal.**
Affirme : retirer les classes fréquentes déplace la masse vers les autres. Formes : un adversaire prédit l'idée banale et la retire ; liste d'exclusion des classes spontanément fréquentes ; exclusion par l'invite, par rejet ou par la grammaire ; rejet exact par programme ; tirage sans remise ; Gumbel-top-k. Le rejet exact donne la loi conditionnelle, avec un gain au plus 1/(1 − p(S)). « Exclure par l'invite n'est pas conditionner. » Référence voisine : Sourati et Evans, 2023, « Accelerating science with human-aware artificial intelligence ».
État : proposé.
Sort : non tranché ; un modèle recommande de le permettre au banc seulement, avec placebo ; un autre préfère une autre option ; heurte la règle « aucun score de nouveauté servi à un agent ».

**C15. Stratification par cellule publique ; histogramme plat ; métadynamique.**
Affirme : déposer un biais sur les cellules déjà visitées et servir des missions qui les excluent (Wang-Landau, « remplir les bassins visités ») ; ou allouer par cellule, avec quota et certificat de masse restante, si bien que la largeur devient la largeur conditionnelle à la cellule.
État : proposé (une seule source, non critiquée).
Sort : non tranché ; ne garantit rien si le puits est étroit dans toutes les cellules ; rouvre la question du masquage d'une partie de l'archive (M5).

**C16. Qualité-diversité ; cartes d'élites ; retourner puis explorer ; nouveauté seule.**
Affirme : organiser la recherche par niches et garder la meilleure idée de chaque niche, ou chercher la seule nouveauté. Références : Mouret et Clune, 2015, « Illuminating search spaces by mapping elites » ; Ecoffet et al., 2021, « First return, then explore » ; Lehman et Stanley, 2011, « Abandoning objectives: Evolution through the search for novelty alone ».
État : proposé.
Sort : non tranché ; une source veut structurer l'archive servie sans récompenser ; une autre la garde dans l'orchestrateur seulement ; jugée la plus exposée au surajustement ; sans borne connue de temps d'atteinte.

**C17. Nourrir les proposeurs de données propres au système.**
Affirme : servir des données que d'autres équipes n'ont pas vues, pour viser la rareté sous leurs modèles ; ancrer par une coupure temporelle.
État : proposé (un modèle, confiance 0,6). Sort : non tranché.

**C18. Faire varier la question, pas seulement les réponses.**
Affirme : reformuler le problème posé change davantage la loi des propositions que varier les réponses.
État : proposé. Sort : non tranché.

**C19. Abstraction et transfert : chercher la mesure sous laquelle le puits est large.**
Affirme : « Un puits n'est étroit que sous une mesure. » Chercher le proposeur, la représentation ou le domaine sous lequel il est large ; un puits « transférable » est commun sous un autre habillage (analogie).
État : proposé. Sort : non tranché ; un banc avec une famille de mondes « transférables » est proposé.

---

## Famille D — Changer la représentation dans laquelle le proposeur écrit (3 entrées)

**D1. Contrastes orthogonaux compilables.**
Affirme : offrir une bibliothèque de produits de traits ±1 ; un compilateur les traduit dans la grammaire.
État : proposé. Sort : retenu au quatrième rang ; risque d'une simple aide de syntaxe et d'une forme assortie au monde.

**D2. Opérateur d'expansion.**
Affirme : l'orchestrateur ajoute lui-même le terme croisé aux lois proposées.
État : proposé. Sort : écarté ; il fabrique des cartes hors du nul.

**D3. Carte de déviation dans le groupe des log-cotes.**
Affirme : le proposeur écrit un écart à une loi connue, en log-cotes, plutôt qu'une loi entière.
État : proposé (un modèle). Sort : non critiqué ; une preuve reste à fournir sur l'enveloppe log-linéaire.

---

## Famille E — Déformer la loi des propositions (6 entrées)

**E1. Température et échantillonnage contre la vraisemblance.**
Affirme : tempérer la loi (q^β), seuil relatif « min-p », échantillonnage verbalisé, pénalité de probabilité, listes longues dont on écarte le début. Une montée de la température a déjà été servie comme témoin faux présenté comme inédit.
État : proposé ; jamais éprouvé ici.
Sort : écarté comme moyen de forcer ; ces méthodes agissent sur les jetons, non sur les classes d'idées ; seule question ouverte : un optimum intérieur sous décodage contraint ; un modèle a retiré la « garantie » qu'il attribuait à la température.

**E2. Modèles de base, non alignés.**
Affirme : des modèles non ajustés aux préférences proposent une loi moins concentrée.
État : proposé. Sort : retenu par une synthèse ; aucune étude sur des idées vérifiées.

**E3. Mélange défensif ; recherche universelle de Levin.**
Affirme : une part ε du budget suit une loi mécanique. Cela garantit q(c) ≥ ε·u(c) quel que soit le modèle, avec un temps d'atteinte de l'ordre de 2^L(c). Référence : Levin, 1973, « Universal sequential search problems ».
État : proposé (un modèle). Sort : non tranché ; rien hors de la grammaire.

**E4. Entropie croisée ; échantillonnage préférentiel adaptatif.**
Affirme : adapter la loi de tirage vers les régions prometteuses. Gain au plus p′/p.
État : proposé. Sort : écartée comme moyen de forcer ; elle se referme sur le premier bassin trouvé, donc le plus large.

**E5. Recuit, tempering parallèle, îles et échange de répliques.**
Affirme : faire circuler des populations entre températures ou entre îles. Référence : Woodard, Schmidler et Huber, 2009, « Conditions for rapid mixing of parallel and simulated tempering on multimodal distributions » (le mélange est lent précisément quand un mode étroit côtoie un mode large).
État : proposé. Sort : écarté comme méthode servie ; hors ligne seulement.

**E6. Méthodes de Stein et transport optimal.**
Affirme : déplacer la loi des propositions vers une cible.
État : proposé. Sort : écartées faute de cible ; usage restant : mesurer l'écart entre deux lots.

---

## Famille F — Dessin d'une course en plusieurs pas : chaînes, marchepieds, calendrier (10 entrées)

**F1. Marchepieds.**
Affirme : un bassin étroit s'atteint par une idée intermédiaire (tirage stratifié à marchepieds ; missions « sachant tel élément de l'archive, qu'est-ce qui ne vaut que sous lui ? » ; lignées fécondes ; pierres de gué). Les marchepieds n'aident que si les vraies associations se regroupent.
État : conçu, non joué (démonstration à deux faces écrite ; fécondité simulée 0,85 contre 0,35, dans un monde simulé qui contient la prémisse).
Sort : non tranché.

**F2. Fractionnement multiniveau sur un graphe public de prérequis.**
Affirme : affecter les appels à la frontière de l'archive et dupliquer les chemins qui franchissent un palier. Référence : Cérou et Guyader, 2007, « Adaptive multilevel splitting for rare event analysis ».
État : proposé (non critiqué). Sort : retenu au cinquième rang, seule voie qui vise la profondeur en chaîne ; sans palier, il se réduit au tirage brut.

**F3. Arbres de continuation sans récompense intermédiaire.**
Affirme : prolonger des idées en arbre sans noter les nœuds intermédiaires ; variante : six constats, puis une session par constat.
État : proposé. Sort : non critiqué.

**F4. Synthèse typée de prolongements.**
Affirme : énumérer des prolongements typés par longueur de description préfixe, à budgets croissants.
État : proposé. Sort : suspendue ; ce n'est qu'un a priori syntaxique.

**F5. Curriculum vers des problèmes plus durs.**
Affirme : générer des problèmes de plus en plus durs avec leurs solutions. Références : Wang et al., 2019, « Paired Open-Ended Trailblazer (POET) » ; Dennis et al., 2020, « Emergent complexity and zero-shot transfer via unsupervised environment design ».
État : proposé. Sort : non tranché ; rien devant un puits sans parent.

**F6. Une carte par session au lieu de six dans un même appel.**
Affirme : décorréler les cartes d'un appel, car la première carte attire les cinq autres.
État : proposé (par le système lui-même, sur sa propre conception). Sort : non tranché ; coût estimé modeste.

**F7. Proposeurs en série.**
Affirme : chaque session voit les cartes brutes des précédentes. Question : dispersion ou grégarisme ?
État : conçu, non joué (avec devis). Sort : non tranché.

**F8. Deux passes : traits choisis à bas coût, loi écrite à coût élevé.**
Affirme : un modèle bon marché choisit les traits, un modèle cher écrit la loi.
État : conçu, non joué (brouillon de plan d'expérience avec devis). Sort : non tranché ; aucun lancement.

**F9. Demi-générations.**
Affirme : mettre l'archive à jour au milieu d'une génération.
État : conçu, non joué. Sort : non tranché.

**F10. Archive complète.**
Affirme : ne rien perdre de ce qui est proposé.
État : proposé. Sort : non tranché ; garantit l'audit, pas la découverte ; l'archive ancre les proposeurs.

---

## Famille G — Recombinaison et bisociation (domaines disjoints) (9 entrées)

**G1. Recombinaison forcée de deux domaines disjoints, « loin en domaine, proche en concept ».**
Affirme : choisir deux domaines éloignés mais proches par un concept, et demander une idée qui les relie.
État : conçu, non joué (codée ; non jouée en course réelle).
Sort : la forme est déjà publiée en partie ; trou de dessin : aucun bras au hasard.

**G2. Trou à structure commune.**
Affirme : viser des paires de domaines à canal faible (peu de liens) mais à structure commune forte ; bras de niveau supérieur. Référence : Burt, 1992, « Structural Holes: The Social Structure of Competition ».
État : conçu, non joué (le bras de niveau supérieur exige une annexe scellée).
Sort : retenu comme profil à tester, avec six garde-fous.

**G3. Prédiction de liens « jamais reliés » ; idées dans l'air du temps.**
Affirme : prédire sur un graphe de concepts les paires qui seront reliées. Référence : Gu et Krenn, 2024, « Forecasting high-impact research topics via machine learning on evolving knowledge graphs ». Règle : reproduire la méthode publiée avant de s'en servir.
État : conçu, non joué (plan non scellé ; valeurs publiées vérifiées sur la source).
Sort : un substitut est accordé ; reproduction non faite.

**G4. Recombinaison par fusion : la fille doit prédire plus que ses parents.**
Affirme : une fusion de deux idées n'est retenue que si elle prédit plus que chacune.
État : proposé ; des tricheurs scriptés franchissent le critère de contenu à coût nul (« une simple enveloppe bat la conjonction ») ; résultat du banc de tricheurs non trouvé.
Sort : première expérience décidée : valider le critère contre une batterie de tricheurs ; l'apport d'une fusion par modèle reste entièrement hypothétique.

**G5. Tirage stratifié par domaines estimés.**
Affirme : tirer les paires par strates de domaines estimés, avec opérateur forcé après tirage, filtre de compatibilité et abstention.
État : éprouvé ici (bat le noyau déterminantal corrigé, voir C9). Sort : retenu par défaut.

**G6. Combinaison atypique sur fond conventionnel ; recombinaison contrainte.**
Affirme : les idées fécondes combinent des éléments atypiques sur un fond conventionnel. Références : Uzzi et al., 2013, « Atypical combinations and scientific impact » ; Fleming, 2001, « Recombinant uncertainty in technological search » ; Swanson, 1986, « Fish oil, Raynaud's syndrome, and undiscovered public knowledge ».
État : proposé (antériorités citées de mémoire). Sort : non tranché ; couvre les affectations, non les idées.

**G7. Fertilité d'une paire ; sur-additivité F = R(A∪B) − R(A) − R(B) + R(A∩B).**
Affirme : une paire est fertile si sa réunion rapporte plus que la somme de ses parties.
État : proposé ; F est faussée par le budget et la combinatoire ; aucune définition prospective de la fertilité n'est établie.
Sort : non tranché ; deux définitions prospectives candidates sont à contre-lire.

**G8. Canal social.**
Affirme : prédire les découvertes à partir de qui peut parler à qui, et chercher hors de ces canaux. Référence : Sourati et Evans, 2023, « Accelerating science with human-aware artificial intelligence ».
État : fixé comme règle sans mesure (bras ajouté comme base de comparaison reprise, non comme nouveauté) ; éprouvé dans la littérature, non rejoué ici.
Sort : retenu comme bras ; non joué.

**G9. Base de ponts datés, rétrodiction inversée, graphe amputé des ponts, étiquette de pont indépendante des citations.**
Affirme : juger une méthode de recombinaison sur des ponts historiques datés, en retirant les ponts du graphe et en étiquetant les ponts sans passer par les citations.
État : fixé comme règle sans mesure (gabarit obligatoire) ; non joué. Sort : retenu.

---

## Famille H — Mécanismes d'allumage d'une idée ou d'un champ (7 entrées)

**H1. Transition de phase ; criticité.**
Affirme : la probabilité qu'une paire d'idées soit reprise passerait par un seuil fortement non linéaire.
État : proposé (hypothèse dans quatre sources ; risque de prendre le pic de variance binomiale pour de la criticité).
Sort : suspension proposée jusqu'à un étalonnage, puis retrait s'il échoue ; issue non trouvée.

**H2. Émergence par essaims communicants, contre tentatives indépendantes ou peu de modèles à réflexion profonde.**
Affirme : des essaims de modèles qui communiquent feraient émerger des idées que des appels isolés ne trouvent pas.
État : proposé ; aucune ablation publiée des systèmes cités.
Sort : non tranché ; aucune dépense demandée.

**H3. Allumage comme ensemble autocatalytique de fiches.**
Affirme : un champ s'allume quand un ensemble de fiches se catalyse lui-même (fermeture autocatalytique ; taux de reproduction R0 et endogène ; catalyseur nécessaire). Seuil proposé : un écart à l'espérance sous appariement aléatoire à dose égale.
État : proposé ; la fermeture naïve est triviale sur un graphe sans cycle ; deux sources confondaient fermeture et autocatalyse.
Sort : lu, non repris ; quatre défauts relevés restent sans issue.

**H4. Protocellules : un parent contre deux parents ; le catalyseur est la recombinaison de domaines.**
Affirme : les idées issues de deux parents allumeraient davantage que celles issues d'un seul.
État : proposé ; aucune prédiction globale d'allumage n'est signée sans condition.
Sort : première mesure jamais montée.

**H5. Seuil épidémiologique d'allumage d'un champ (R0 > 1).**
Affirme : un champ s'allume quand chaque idée en engendre plus d'une en moyenne, comme dans un modèle épidémiologique de la diffusion des idées.
État : proposé (rapporté sans lecture de la source ; aucune référence exacte donnée).
Sort : lecture de la source non faite.

**H6. Idées « dans l'air » qui découlent de découvertes antérieures.**
Affirme : certaines idées deviennent probables dès que leurs prérequis sont publiés.
État : proposé. Sort : rattaché à G3 et à la rétrodiction ; non mesuré.

**H7. Causes de la fertilité par apprentissage ; identification.**
Affirme : seul un entraînement sur une affectation biaisée, suivi d'une épreuve randomisée, sépare estimer la fertilité de l'identifier.
État : proposé. Sort : lu, non repris.

---

## Famille I — Nouveauté, moisson, antériorité (9 entrées)

**I1. Aucune récompense numérique de la nouveauté, ni dans le juge, ni servie à un agent.**
Affirme : les mesures de nouveauté sont consignées, jamais servies ; le proposeur ne voit jamais la richesse de ses idées.
État : fixé comme règle sans mesure. Sort : retenu partout ; frotte avec C14 et L3.

**I2. Moissonneur de nouveauté.**
Affirme : interroger des bases bibliographiques publiques (métadonnées et résumés) pour situer une idée ; les touches ne sont pas probantes.
État : conçu, non joué (relais factice seulement). Sort : non joué en réel.

**I3. Originalité comme note de grille des juges.**
Affirme : les juges classent une idée comme « inédite », « transposition » ou « déjà publiée ».
État : conçu, non joué (en usage dans une course comme matériau). Sort : matériau, jamais preuve.

**I4. Nouveauté définie à l'oracle : gain d'information au-delà de l'archive (ΔG).**
Affirme : une idée est nouvelle si elle apporte un gain prédictif sur l'oracle au-delà de l'archive.
État : conçu, non joué (brouillon non scellé). Sort : non joué.

**I5. Témoins « redites vraies » et « vrais mais dérivables ».**
Affirme : mêler aux idées des redites vraies et des idées vraies mais dérivables de l'archive, pour mesurer si le système les distingue des découvertes.
État : fixé comme règle sans mesure (audit prévu, chacun avec plan scellé et contre-lu) ; non fait.
Sort : retenu ; seule mesure qui donne un chiffre propre à la prétention principale de nouveauté.

**I6. Redite exacte de la loi du monde par un proposeur.**
Affirme : un critère de nouveauté peut être violé sans aucune optimisation contre le juge (effet de Goodhart).
État : éprouvé ici (course réelle : 42 cartes sur 48 reproduisent exactement la loi du monde). Sort : constat.

**I7. Distance à un corpus, densité en plongement, score de Vendi.**
Affirme : mesurer la nouveauté par la distance à un corpus ou la diversité d'un lot.
État : proposé. Sort : description seulement, jamais critère ; un modèle a retiré sa distance de compression.

**I8. Surprise et curiosité.**
Affirme : récompenser la surprise d'un modèle. Référence : Burda et al., 2019, « Large-scale study of curiosity-driven learning ».
État : proposé. Sort : écartées ; attirées par le bruit.

**I9. Recherche d'antériorité par un tiers ; jury aveugle étalonné par des leurres.**
Affirme : faire juger la nouveauté par un tiers ou par un expert humain du domaine, avec des leurres pour étalonner.
État : proposé ; pour les mathématiques, une recherche d'antériorité par étages a été accordée.
Sort : en partie accordé.

---

## Famille J — Mesurer la rareté, la masse non vue et la réponse à la vue (16 entrées)

**J1. Masse manquante.**
Affirme : la part des classes vues une seule fois estime la masse jamais vue ; d'où une règle d'arrêt et un chiffre de « ce qu'il reste à trouver ». Références : Good, 1953, « The population frequencies of species and the estimation of population parameters » ; Good et Toulmin, 1956, « The number of new species, and the increase in population coverage, when a sample is increased » ; Chao, 1984, « Nonparametric estimation of the number of classes in a population » ; McAllester et Schapire, 2000, « On the convergence rate of Good-Turing estimators ». Variantes : courbe d'accumulation ; pénaliser par la masse manquante.
État : proposé ; jamais validée contre l'oracle ici.
Sort : diagnostic agrégé, jamais pour une idée seule ; mesure descriptive ; la version d'incidence est préférée à la version d'abondance.

**J2. Rareté certifiée sur un panel indépendant, sous une loi de tirage figée.**
Affirme : une idée est « rare certifiée », « non rare » ou « indéterminée » selon sa fréquence sur un panel indépendant (rare si inférieure à environ 3/N).
État : proposé (adoptée par six modèles au troisième temps d'une critique croisée).
Sort : retenue en tête ; un panel fini ne distingue jamais une idée hors support d'une idée très rare.

**J3. Banc à puits plantés et courbe dose-réponse.**
Affirme : des mondes à largeur et profondeur réglées, puis estimées, mesurent la réponse d'une méthode ; les puits sans parent servent de témoin négatif ; des puits impossibles servent de détecteurs de fuite ; des familles de mondes sont tenues à l'écart.
État : proposé ; jamais monté.
Sort : expérience décisive à préenregistrer ; non tranché.

**J4. Audit des pertes ; diagnostic de l'entonnoir.**
Affirme : sur les journaux bruts, savoir si une idée n'a jamais été proposée, ou a été proposée puis perdue.
État : proposé (gratuit). Sort : recommandé en premier par deux modèles (confiances 0,85 et 0,8) ; non tranché, non fait.

**J5. Loi spontanée des proposeurs.**
Affirme : mesurer le rang-fréquence, la masse non vue, le recouvrement entre familles, la capture-recapture (Lincoln et Petersen) et la saturation.
État : proposé. Sort : non fait ; indice avancé sans preuve : des familles différentes partagent les mêmes bassins.

**J6. Réactivité de la loi des propositions à la vue.**
Affirme : c'est l'inconnue centrale. Premier essai : garde et levier sur un monde sans interaction.
État : proposé ; aucun fait ne la dit. Sort : retenu comme premier essai avec proposeurs ; non fait.

**J7. Identité d'une idée par signature d'exécution sur des sondes.**
Affirme : deux idées sont la même si elles prédisent la même chose sur un jeu public (classes fonctionnelles, canonisation, regroupement fonctionnel).
État : proposé (six modèles sur six). Sort : retenu ; désaccord ouvert sur l'ajout de l'arbre syntaxique.

**J8. Mesure de la diversité par couverture d'oracle.**
Affirme : compter les composantes plantées certifiées couvertes ; nombre effectif descriptif.
État : conçu, non joué (conception d'un monde riche, outils et sorties scellés). Sort : retenu pour une course à plusieurs générations ; question ouverte au regard des travaux voisins.

**J9. Trois lectures par l'oracle.**
Affirme : lire l'oracle sur les propositions brutes, sur les représentants et sur les cartes retenues.
État : proposé. Sort : retenu.

**J10. Tests de collisions et d'autocorrélation du générateur.**
Affirme : tester la diversité du générateur (indice de Simpson, taille d'échantillon effective, test des séquences). Références : Batu et al., 2000, « Testing that distributions are close » ; Wald et Wolfowitz, 1940, « On a test whether two samples are from the same population ».
État : proposé (deux modèles). Sort : non tranché.

**J11. Grandeurs : largeur, profondeur, justesse, fécondité par ablation ; mesure à deux références ; grandeur visée par million de jetons.**
Affirme : définir les grandeurs de l'exploration et les rapporter au coût.
État : proposé. Sort : non tranché (mesure seule, ou après le banc).

**J12. Seuil de rentabilité d'une méthode.**
Affirme : une méthode vaut si son gain d'efficacité λ = p/p₀ dépasse son surcoût κ.
État : proposé (un modèle, non vérifié par un tiers). Sort : non tranché.

**J13. Audit de la vérification dans la queue.**
Affirme : tester la vérification sur des « faux naturels » ; essai « témoin contre témoin » avec erreurs injectées et domaine nul.
État : proposé. Sort : ordre retenu par une synthèse ; non fait.

**J14. Validité externe.**
Affirme : rétrodiction sur des textes postérieurs à la coupure des modèles ; prédictions scellées jugées à l'aveugle.
État : proposé. Sort : non tranché ; jugée l'hypothèse non testée la plus lourde.

**J15. Monde plus riche, calibré, avec traits leurres.**
Affirme : un monde de test plus riche, aux composantes calibrées et avec des traits leurres, rend la diversité mesurable.
État : fixé comme règle sans mesure (périmètre de conception) ; conçu, non joué. Sort : retenu.

**J16. Redondance observée dans les courses réelles.**
Affirme : les courses réelles produisent beaucoup de doublons (17 idées distinctes, 12 paires de doublons ; dans une autre course, « ce ne sont pas 11 idées »).
État : éprouvé ici. Sort : constat ; l'origine (monde pauvre ou convergence des proposeurs) n'est pas établie.

---

## Famille K — Arrêt et allocation (12 entrées)

**K1. Arrêt optionnel ; processus de valeurs e ; tirages du juge répartis avec arrêt anticipé.**
Affirme : une carte dont l'effet est confiné à une région rare reçoit plus de tirages, sans perte de validité sous toute règle d'arrêt écrite d'avance (surmartingale de test, inégalité de Ville, allocation par blocs). Cela sert la survie d'une idée, pas sa découverte.
État : éprouvé ici (sur processeur : verdict « gain de structure » ; validité tenue, 0 promotion à tort sur 500 dans sept bras ; part fixe : 41,3 % des générations couvertes, allocation par blocs : 86,1 % ; réserves : banc à 18 cartes non porteuses sur 24, qui ne se transpose pas ; l'allocation consomme 67 % du budget ; deux conditions avancées par une synthèse jugées non nécessaires, aucun contre-exemple sur 20 000 générations).
Sort : adoption au juge en attente d'une décision.

**K2. Bandits extrêmes ; recherche arborescente ; bandit sur les vues.**
Affirme : allouer les appels comme un bandit qui vise le maximum. Références : Carpentier et Valko, 2014, « Extreme bandits » ; Kocsis et Szepesvári, 2006, « Bandit based Monte-Carlo planning » ; Bubeck et al., 2011, « X-armed bandits » ; variante à oubli proposée par un modèle.
État : proposé.
Sort : bon objectif, mais exige une récompense ; hors ligne seulement, sur mondes d'étalonnage ; dans la boucle de moisson, personne ne l'a retenu.

**K3. Uniforme avec arrêt précoce.**
Affirme : élimination successive mécanique, arrêt par budget.
État : proposé. Sort : position par défaut de la boucle de moisson.

**K4. Portefeuille de proposeurs sous budget, sous-modulaire ; identification hors ligne du meilleur couple « proposeur × vue ».**
Affirme : choisir un portefeuille par maximisation sous-modulaire, et identifier le meilleur couple hors ligne, relativement à une loi a priori déclarée. Références : Nemhauser, Wolsey et Fisher, 1978, « An analysis of approximations for maximizing submodular set functions » ; Audibert, Bubeck et Munos, 2010, « Best arm identification in multi-armed bandits ».
État : proposé. Sort : le portefeuille est suspendu (les fréquences ne se distinguent pas de zéro au budget d'un pilote) ; l'identification n'est pas critiquée.

**K5. Composition des proposeurs jugée sur l'oracle et le coût, jamais sur le verdict du juge.**
Affirme : seule « récompense » licite ; composition apprise ; voies bon marché avant la voie chère.
État : fixé comme règle sans mesure. Sort : retenu ; dernier mécanisme à essayer.

**K6. Le bon marché d'abord ; appeler les proposeurs chers sur le regroupement des doublons.**
Affirme : des instruments locaux et bon marché à la première génération ; les proposeurs chers ne servent qu'après le regroupement des doublons.
État : conçu, non joué (plans d'expérience avec devis, à refaire après un pilote).
Sort : dépense accordée pour l'essai, non pour l'adoption ; tension notée avec K5 au-delà de la première génération.

**K7. Arrêter une course stérile et reporter le budget là où l'archive a grandi.**
Affirme : couper une course qui ne produit rien et réallouer.
État : proposé. Sort : écarté, car il pilote le dessin par les promotions du juge ; seule la variante sur le regroupement survit (K6).

**K8. Indice de réserve de Weitzman pour l'ordre de vérification.**
Affirme : vérifier les idées dans l'ordre de leur indice de réserve. Référence : Weitzman, 1979, « Optimal search for the best alternative ».
État : proposé. Sort : non tranché ; vaut seulement si les a priori étalonnés se transportent, ce qui n'est pas établi.

**K9. Maîtrise en ligne du taux de fausses découvertes entre générations.**
Affirme : tenir le taux de fausses découvertes à travers des générations successives. Références : Javanmard et Montanari, 2018, « Online rules for control of false discovery rate and false discovery exceedance » ; Wang et Ramdas, 2022, « False discovery rate control with e-values » (e-BH) ; Xu et Ramdas, 2024, « Online multiple testing with e-values ».
État : proposé. Sort : manque reconnu ; non écrit.

**K10. Allocation par « loi parente commune » et champ moyen de Thouless-Anderson-Palmer.**
Affirme : deux stratégies d'allocation avancées par un modèle.
État : proposé (non codées, à tester comme hypothèses). Sort : non tranché.

**K11. Règles d'arrêt et de relance à garantie.**
Affirme : utiliser des règles d'arrêt et de redémarrage à garantie connue. Références : Dagum, Karp, Luby et Ross, 2000, « An optimal algorithm for Monte Carlo estimation » ; Wald, 1945, « Sequential tests of statistical hypotheses » ; Luby, Sinclair et Zuckerman, 1993, « Optimal speedup of Las Vegas algorithms » ; Clopper et Pearson, 1934, « The use of confidence or fiducial limits illustrated in the case of the binomial » (borne sur zéro succès).
État : proposé (deux modèles). Sort : non tranché.

**K12. Filtrage avant la vérification coûteuse.**
Affirme : dédoublonner, mémoïser, pré-filtrer avant la vérification chère. Références : Michie, 1968, « "Memo" functions and machine learning » ; Vovk, Gammerman et Shafer, 2005, « Algorithmic Learning in a Random World » (cascade par pré-filtrage conforme) ; Dorfman, 1943, « The detection of defective members of large populations » (test par groupes) ; filtre syntaxique exact par grammaires attribuées.
État : proposé. Sort : dédoublonnage retenu par une synthèse (solidité moyenne) ; le reste non tranché.

---

## Famille L — Jugement et sélection (15 entrées)

**L1. Juge au nul formé des lois connues.**
Affirme : une statistique calculée par l'orchestrateur, sur un engagement scellé, teste chaque idée contre le nul des lois connues.
État : fixé comme règle sans mesure (contrainte de toute méthode). Sort : retenu ; chacune de ses deux moitiés est déjà publiée, seule leur réunion ne l'est pas.

**L2. Valeur e par strates ou à plusieurs échelles.**
Affirme : la fiche déclare sa région avant les données ; la valeur e est calculée par strate.
État : proposé. Sort : contredite par l'identité d'auto-localisation (A6) ; maintenue sous forme très restreinte ; une consultation séparée la maintient sans contradicteur.

**L3. Poids de multiplicité selon la nouveauté ou la géométrie des groupes.**
Affirme : pondérer la correction de multiplicité (e-BH pondéré) selon la nouveauté ou la géométrie des groupes d'idées.
État : proposé. Sort : retiré au cours d'un tour de critique (« une prime de nouveauté sous un autre nom ») ; encore défendu par deux sources.

**L4. Martingale à pari localisé, avec nul ponctuel.**
Affirme : parier localement contre l'enveloppe convexe des lois de l'archive en chaque point.
État : proposé. Sort : non critiquée ; elle absorbe toute découverte située entre deux lois archivées.

**L5. Valeur e par supremum sur un nul composite explicite.**
Affirme : prendre le supremum sur un nul composite écrit d'avance.
État : proposé. Sort : maintenue sous double condition, comme garde et non comme moyen de découverte.

**L6. Filtre mécanique avant le juge contre les recombinaisons par morceaux.**
Affirme : un filtre mécanique écarte les cartes qui recollent des lois de l'archive par morceaux.
État : proposé. Sort : non critiqué.

**L7. Tirages du juge stratifiés selon une loi de traits.**
Affirme : tirer les exemples frais du juge par strates publiques.
État : proposé. Sort : retiré au cours d'un tour, repris par une fiche du système sans répondre à l'objection ; se tranche sur processeur en quelques heures ; non fait.

**L8. Nul par morceaux limité aux conditions de l'archive ; poids appris du nul.**
Affirme : apprendre les poids d'un nul par morceaux restreint aux conditions déjà présentes dans l'archive.
État : éprouvé ici, en partie (sur processeur : les poids appris ne sont pas valides ; une copie exacte est promue dans 96,5 % à 100 % des répétitions en ligne et 64,9 % sur une moitié ; refait : 98 à 100 % et 37 à 76 % ; 0 sur 300 avec le maximum certifié) ; une seconde version a commencé puis s'est arrêtée faute de crédit de calcul ; verdict non trouvé.
Sort : non tranché ; décision de ne pas abandonner après un premier échec de méthode.

**L9. Valeurs e pondérées par la longueur de description.**
Affirme : une forme du rasoir d'Occam appliquée aux valeurs e.
État : proposé. Sort : non tranché ; validité sous nul composite à prouver.

**L10. Regroupement des doublons et choix du représentant.**
Affirme : regrouper par distance prédictive en liaison complète, soit après le test d'élimination, soit avant le juge ; jeu public construit par un plan ; représentant choisi par couverture dirigée de strates, par pivotage de Cholesky, ou par divergences localisées ; jamais le représentant de plus grande valeur e.
État : conçu, non joué (conception du monde riche et des doublons) ; jeu public survivant, couverture dirigée maintenue affaiblie, pivotage suspendu, divergences descriptives.
Sort : regroupement après le test d'élimination recommandé ; le principe « grouper les idées par ce qu'elles font » est déjà publié.

**L11. Sélection douce.**
Affirme : sélection de Boltzmann à température fixée d'avance, ou une place tirée au sort par génération.
État : proposé (une seule source). Sort : non tranché ; une loi non promue entrerait dans le nul suivant.

**L12. Pari apparié borné pour lire un duel.**
Affirme : un duel entre deux configurations se lit par un pari apparié borné.
État : fixé comme règle sans mesure (règle de lecture) ; le duel payant est conçu, non joué, sans résultat. Sort : retenu.

**L13. Second examen distinct, réplication ; erreurs corrélées.**
Affirme : un second examen ne protège pas si ses erreurs sont corrélées au premier.
État : proposé (tranché par calcul). Sort : retenu avec réserve.

**L14. Aucun juge-modèle de la nouveauté.**
Affirme : un modèle de langue ne juge pas la nouveauté.
État : fixé comme règle sans mesure ; éprouvé ici (les deux juges-modèles plafonnent dans une course réelle). Sort : retenu.

**L15. Double nul : contre l'archive et contre l'attendu aveugle d'un panel.**
Affirme : tester une idée à la fois contre l'archive et contre ce qu'un panel aveugle attendrait.
État : proposé. Sort : sur devis ; non tranché.

---

## Famille M — Mémoire et héritage (7 entrées)

**M1. Héritage d'une génération récompensé.**
Affirme : créditer un agent par sa descendance, avec un rendement à K générations actualisé.
État : fixé comme règle sans mesure ; le principe est déjà publié (« Huxley-Gödel Machine », 2025).
Sort : prétention de nouveauté retirée ; seule la citation de l'antériorité est permise.

**M2. Oublier plutôt que continuer ; hériter moins.**
Affirme : un bras « héritage réduit au meilleur », un bras « oubli », une paire « même état, vue pleine contre vue réduite ». L'oubli peut être rendu continu.
État : éprouvé dans la littérature, non rejoué ici (gain plus grand pour une dépense à peu près moitié moindre) ; fixé comme règle sans mesure (bras accordé).
Sort : retenu ; rouvre la question du masquage de l'archive (M5).

**M3. Remise à zéro du contexte, déjà en place.**
Affirme : chaque appel part d'une session neuve.
État : fixé comme règle sans mesure (fait de dessin). Sort : retenu ; l'ancrage à l'intérieur d'un appel de six cartes demeure (F6).

**M4. Mémoire transmise comme registre des tentatives ; plan à trois bras.**
Affirme : comparer sans mémoire, mémoire neuve tenue, et mémoire héritée. La mémoire est un registre des tentatives, non une archive de découvertes.
État : proposé (matière première ; ne peut pas encore fonder un plan d'expérience).
Sort : décrit sans être dit nouveau ni propre ; neuf travaux voisins sont à citer obligatoirement.

**M5. Masquage d'une partie de l'archive.**
Affirme : cacher une partie de l'archive aux proposeurs pour les libérer de son ancrage.
État : proposé. Sort : d'abord rejeté par plusieurs sources, puis rouvert par décision ; non tranché.

**M6. Épreuve de prédiction par la lignée, sans fuite.**
Affirme : prédire la suite d'une lignée d'idées sans fuite d'information depuis le futur.
État : proposé. Sort : non fait.

**M7. Fil continu.**
Affirme : le proposeur garde sa séance d'une génération à l'autre.
État : proposé. Sort : non tranché (coûteux).

---

## Famille N — Voie sociale et composition des proposeurs (2 entrées)

Le canal social est classé en G8 et n'est pas compté ici.

**N1. Pluralité des familles de proposeurs ; homogénéité entre modèles.**
Affirme : des familles de modèles différentes produiraient des idées différentes ; des travaux publiés montrent au contraire une forte homogénéité. Références : Jiang et al., 2025, « Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond) » ; Wenger et Kenett, 2025, « We're different, we're the same: Creative homogeneity across LLMs » ; d'autres travaux voisins sur la similarité entre modèles.
État : proposé ; l'indice contraire doit être cité.
Sort : travail voisin ; témoins prévus (B9).

**N2. Isolement des appels contre communication.**
Affirme : isoler les appels (sans débat ni vote) préserve la diversité ; la communication l'efface (« The interaction tax ») ; un système publié de découverte par échange de candidats n'évite pas le plateau.
État : éprouvé dans la littérature, non rejoué ici ; proposé ici.
Sort : non tranché (rejoint H2).

---

## Jamais éprouvé ici (entrées qui portent une prédiction testable)

- Le banc à puits plantés et la courbe dose-réponse, puits sans parent compris ; le critère de réfutation par famille de mondes (J3).
- L'audit des pertes sur journaux bruts (J4) ; la loi spontanée des proposeurs et leur recouvrement (J5) ; la réactivité de la vue, table des paires contre placebo (J6, C3).
- La masse manquante comme règle d'arrêt, validée contre l'oracle (J1) ; la rareté certifiée sur panel (J2) ; l'audit de la vérification dans la queue (J13).
- Le tirage au hasard dans la grammaire et le chercheur mécanique contre de vrais proposeurs (B2, B3) ; le duel payant des proposeurs (L12).
- La stratégie « hors des bassins déjà retenus » avec un vrai modèle (C1, C2).
- Les marchepieds sur une lignée réelle (F1) ; le fractionnement sur prérequis (F2) ; les proposeurs en série, les deux passes, les demi-générations, le bon marché d'abord (F7, F8, F9, K6) ; une carte par session (F6).
- La recombinaison forcée de deux domaines disjoints en course réelle, ses trois bras et le canal social (G1, G2, G8) ; la reproduction de la prédiction de liens publiée (G3) ; le banc des tricheurs pour la fusion (G4).
- L'exclusion du banal par l'invite contre le rejet exact (C14) ; la température sous décodage contraint (E1) ; les modèles de base (E2) ; le mélange défensif (E3).
- La transition de phase, les essaims, l'autocatalyse, « un parent contre deux parents » (H1 à H4).
- Le moissonneur en réel (I2) ; les témoins « vrais mais dérivables » (I5).
- Les tirages du juge stratifiés, sur le banc de l'allocation avec arrêt anticipé (L7) ; le nul ponctuel et le filtre avant le juge (L4, L6).
- Le plan à trois bras de la mémoire ; le bras d'oubli dans ce système (M2, M4) ; la validité externe par rétrodiction datée (J14).
- L'organisme dédié aux bassins étroits lui-même : première génération en défaut, générations suivantes jamais lancées.

---

## Désaccords entre sources (22)

1. Qualité-diversité : une source dit de structurer l'archive servie aux proposeurs, sans récompense ; une autre dit de la garder dans l'orchestrateur, jamais servie aux proposeurs.
2. Rareté comme signal d'allocation : une source la propose dans l'orchestrateur, après le banc ; une autre exclut toute récompense numérique de la nouveauté, sélection comprise.
3. Valeur e par strates : une source dit qu'elle met fin à la dilution ; deux autres le réfutent ; une quatrième concède ; une consultation séparée la maintient.
4. Poids de multiplicité : leur auteur les abandonne ; deux autres sources les défendent encore.
5. Tirages du juge stratifiés : une source dit la garantie intacte ; une autre dit que la grandeur jugée change.
6. Conditions de l'arrêt optionnel : une source exige un dénominateur fixe et un ordre fixé d'avance ; une autre les juge non nécessaires.
7. Origine de l'allocation avec arrêt anticipé : une source la rattache à un tour sur les bassins étroits ; une autre à un relevé d'idées réutilisables (les deux sont compatibles).
8. Regroupement des doublons : une source dit de regrouper après le juge ; trois autres disent avant.
9. Métrique principale : une source dit les propositions brutes ; une autre dit les cartes retenues.
10. Hausse des lois conditionnelles sous monde nul : une source y voit une alerte de garde ; deux autres une simple description.
11. Monde à condition verrouillée (interaction sans parent) : une source en fait un témoin nul ; deux autres le refusent ; une autre tranche pour le témoin négatif ; une autre en fait un détecteur de fuite.
12. Plan d'expérience : deux sources combinent plusieurs facteurs par bras ; deux autres exigent un seul facteur par bras.
13. Bandit : une source le refuse dans la boucle de moisson ; deux autres le gardent en synthétique ; une autre recommande une allocation par bandits après un pilote corrélé ; une autre interdit tout guidage par le juge en course.
14. Fausses découvertes : trois sources demandent une marge positive ; une autre s'en tient à « sans augmenter ».
15. Identité d'une idée : une source ajoute l'arbre syntaxique ; une autre le retire.
16. Recombinaison de domaines disjoints : une pièce n'a pas de bras au hasard ; toutes les autres pièces exigent une base au hasard.
17. Héritage : une prémisse de conception dit que l'héritage aide ; un résultat publié dit qu'oublier bat continuer.
18. Masquage de l'archive : plusieurs sources le rejettent ; une décision accorde des bras « oubli » et « héritage réduit ».
19. Relances de l'organisme sur les bassins étroits : un outil de lancement en permet une par génération ; une décision n'en permet qu'une au total.
20. Transition de phase : une source dit de la retirer ; une autre de la maintenir à partir de cinq tailles ; une recommandation dit de la suspendre.
21. Classement de deux méthodes de jugement (valeur e par strates, poids de multiplicité) : une source les met au deuxième rang ; un tour de critique les contredit.
22. Où commencer : trois sources disent les instruments seuls ; une autre la vérification dans la queue ; une autre une chaîne avec erreurs injectées ; deux modèles disent l'audit des pertes d'abord ; un tour de critique croisée entre plusieurs modèles dit le banc de garde d'abord.
