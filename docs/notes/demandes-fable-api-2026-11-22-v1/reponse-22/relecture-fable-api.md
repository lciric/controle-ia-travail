# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHbhaDU3vV1JkDnfuWJZ`
- Heure (UTC) : 2026-11-22T07:56:31Z
- Réglages : effort `xhigh`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-22-revue-revendications-theses-v1.md` — sha256 bc3b8f69d7a533d882af52ea2db029a8a9f905961b27639bfbcb99e9343cac1d (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-9/relecture-fable-api.md` — sha256 48d4d72e5f1cbcdea6a60fea309e80f4e5f319e30389540acc7aa422bd560e52 (compagnon : vérifié)
  - remarques : `docs/notes/recherche-exhaustive-transposition-v2.md` — sha256 2395ea20a570afd7b206bec4adec56664604a500902c68cf68eed87358ae9b8d (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/table-revendications-en-vigueur-v1-sans-nom-v1.md` — sha256 02453d1d92fc589150cf6e27bed56a996aea8a3de86d8580629ecc8cb8e7cddc (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-2/relecture-fable-api.md` — sha256 542b7bfc86497c0c9bc45ed7f1651162a47789b6b2f00325f989daaac42c59f3 (compagnon : vérifié)
  - remarques : `docs/notes/seconde-lecture-these-v1.md` — sha256 a4f751ce3981aa100d026e9b90a9214897f639717bdcc9c31a5680d32cfcfdf4 (compagnon : vérifié)
  - remarques : `docs/notes/lecture-steganographie-comptabilite-v1.md` — sha256 6d52ba5d033d5a71237337a6c27f6f257d80c8ecbfb7a32dbae30cc569ce8ac6 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 8c4b1e015d5a44d20c689ea91b850fbb4709609644a51553b9085bb144d0e73e
- Jetons : entrée 60566, sortie 50908 (dont réflexion 41528), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 2.520848 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 22 — revue des revendications et des thèses : réponse approfondie

**Conclusion d'abord.** La thèse retenue tient, à trois ajouts près : citer la transposition déjà publiée au suivi des usages, calculer la puissance du plan avant de sceller, mesurer la complémentarité à taux total de fausses alertes égal. Le retrait du lemme d'additivité et du théorème négatif ne s'arrête pas à leurs deux lignes. Quatre revendications s'y adossent (accumulation, courbe selon le nombre d'agents, co-élévation, statistique conjointe) et sont à récrire contre le modèle nul hérité. La table jointe s'arrête avant N-075 : elle n'est plus « en vigueur ». Le papier C et l'organisme ne sont pas touchés par les trois pièces, à un voisin près. Confiance d'ensemble : 0,6.

**Réserves.**
- Je n'ai lu aucun PDF. Les trois notes sont mon seul accès aux pages ; leurs verdicts sont des faits rapportés.
- Je n'ai pas le texte des décisions (N-003, N-004, N-069, N-075 à N-077), ni les réponses 4 et 8, ni la ligne de la thèse hors son résumé.
- Les identifiants arXiv de 2026 viennent des notes ; je n'en confirme aucun. Mes ajouts de mémoire portent « rapporté, non vérifié sur PDF ».
- Les réponses 2 et 9 viennent du même modèle que celle-ci (leurs en-têtes le disent) : mon accord avec elles n'est pas une confirmation indépendante.
- Empreintes non recalculées. Je ne nomme que les auteurs des travaux cités.

## 1. Ce qu'un expert ferait et qui n'est pas demandé

- **Propager les retraits** [PROPOSITION]. Dresser le graphe des appuis : quelles revendications supposent le lemme ou le théorème ? Une revue ligne à ligne laisse debout des énoncés dont le socle est parti.
- **Vérifier que la table est à jour** [FAIT RAPPORTÉ, table et contexte]. Elle date du 19 novembre, s'arrête à N-074 et « ne fait pas foi ». La marge asymétrique y figure « resserrée », alors que N-077 l'a sortie des hypothèses revendiquées.
- **Se garder du retrait excessif** [FAIT RAPPORTÉ, table, ligne du théorème]. N-003 avait déjà borné la forme « puissance égale au taux de faux positifs » : vraie quand l'attaque préserve le multi-ensemble des scores, fausse quand elle ne préserve que les marginales par coordonnée. La critique de la réponse 9 visait la lettre du programme, version 2.
- **Graduer les « non trouvé »** [PROPOSITION] : six pièces lues ; 36 requêtes avec quatre arbres de citations non parcourus ; 13 pages lues sur 39 pour le parent de la complémentarité.
- **Calculer la puissance du plan de mesure** [PROPOSITION]. « Deux issues publiables » en cache une troisième, l'issue indéterminée.
- **Écrire, pour chaque énoncé gardé, le rapport de rejet le plus fort** (« évident », « déjà fait ») avant de le garder [PROPOSITION].

## 2. Données brutes de départ

Toutes les puces sont des PROPOSITIONS.

- Le texte des décisions et non leur résumé : N-003, N-004, N-069, N-075 à N-077, la ligne de la thèse.
- Les pages non lues : Parrack et collaborateurs, p. 12 et 15 à 39 ; Zhang et Gao, p. 10 et 11.
- Les quatre arbres de citations non parcourus (Ker 2006 et 2007, Arias-Castro et collaborateurs 2012, Avenhaus et Jaech), et celui de Ker 2010, que la recherche ne mentionne pas.
- Les scores bruts pas à pas d'exécutions honnêtes jumelles (tâche, exécution, rang du pas), pour plusieurs moniteurs sur les mêmes actions et pour des copies honnêtes d'un même essaim.
- Les traces réelles de Zhang et Gao, si elles sont publiques.

## 3. Méthodes et outils

Toutes les puces sont des PROPOSITIONS.

- **Tableau de revendications**, élément par élément contre la page, typé : théorème, méthode, mesure, protocole.
- **Trois simulations.**
  - Franchissement séquentiel à budget égal : sabotage tôt, tard, étalé.
  - Moyenne, maximum et somme cumulée sous permutation, puis sous copule autorégressive d'ordre 1 à marginales préservées. Cela rejoue le tableau 2 de Zhang et Gao.
  - Carré de la somme et test d'histogramme aux tailles d'essaim du programme.
- **Puissance du plan** : modèle à composantes de variance (tâche, exécution, pas), rééchantillonnage par tâche, plus petit écart décelable sur l'exposant et sur le terme entre tâches. Un banc à vérité plantée (scores synthétiques d'exposant connu) vérifie que l'ajustement retrouve ce qu'on y a mis.
- **Substituts par permutation des pas**, pour la question « position ou dépendance ».
- **Union à taux total égal**, pour la complémentarité.
- **Énoncés témoins** servis au collisionneur : des énoncés au statut connu (occupé, faux, vrai par construction), mêlés aux nôtres. Ils mesurent son taux de détection, comme N-075 le fait par dommages plantés.

## 4. Ce qui vérifie hors du directeur et de Claude

Toutes les puces sont des PROPOSITIONS.

- Les trois simulations : leur issue ne dépend d'aucun avis.
- Le taux de détection du collisionneur sur les énoncés témoins.
- Un spécialiste de stéganalyse et un statisticien des garanties nucléaires, sur le tableau de revendications.
- Les auteurs de 2606.10456, sur la réserve à longueur finie : « est-ce une limite de votre proposition 1 ? »
- Un second lecteur des pages décisives ; l'essai « jumeau contre jumeau » ; la prévision scellée.

## Demande reformulée

« Voici la table des revendications, les décisions qui la suivent (N-075 à N-077, thèse retenue) et trois notes de lecture sur PDF. Pour chaque revendication et pour la thèse : (1) découpe l'énoncé en éléments et confronte chacun à la page de l'antériorité la plus proche, y compris hors des pièces ; (2) dis si l'énoncé est exact tel qu'écrit, et s'il est vrai par construction sous la loi héritée ; (3) dis de quelles autres revendications il dépend, et propage tout retrait ; (4) rends un verdict : tenue, à resserrer, à retirer, à remplacer, ou non touchée ; (5) pour tout énoncé neuf, donne l'épreuve qui le réfute et vérifie que le plan prévu a la puissance de la mener ; (6) gradue chaque "non trouvé" par la recherche qui le fonde ; (7) signale tout retrait excessif ; (8) liste les phrases à ne plus écrire, pièces jointes comprises. Marque fait rapporté, hypothèse, proposition. Aucune zone vierge n'est déclarée libre. »

## Réponse à la demande reformulée

### Quatre constats avant la table

1. **Sous la loi héritée, un énoncé en vigueur est vrai par construction** [HYPOTHÈSE, dérivation de ma main]. À déplacement par acte fixé, « un rappel qui croît avec l'horizon » découle de la loi en racine tant que l'horizon n reste sous la taille m de la référence. Au-delà, le seuil de Ker 2010 (note de stéganographie, p. 7) prédit un plafond : la détection ne dépend plus que du déplacement et de m. Le résultat serait l'écart à cette courbe, non la courbe.
2. **La somme globale est le meilleur test au pire cas contre un total réparti** [FAIT RAPPORTÉ, note de stéganographie, Avenhaus et Jaech 1981, p. 30], sous covariance gaussienne connue et taille fixe. [HYPOTHÈSE] Une statistique conjointe ne peut donc se dire supérieure au séquentiel par agent et à la coupe transversale sans se mesurer d'abord à cette somme. Son contenu propre ne peut porter que sur la dépendance ou sur la référence estimée.
3. **La référence estimée vaut aussi pour l'essaim** [HYPOTHÈSE]. Des copies honnêtes d'un même modèle sur un même travail ont des scores corrélés. Le nul d'Arias-Castro et collaborateurs suppose l'indépendance (seconde lecture, p. 2). La co-élévation doit déclarer la taille de sa référence de corrélation honnête, comme N-076 l'exige de toute accumulation.
4. **Deux des trois phrases autorisées par la recherche exhaustive (§ 5) sont à récrire** [PROPOSITION]. Celle sur « l'aveuglement des statistiques de marginales » est contredite dans sa lettre par la seconde lecture (§ 2). Celle sur l'invariance « non trouvée pour des moniteurs d'agents » présente un écart d'objet comme une ouverture.

### Table

- Colonne « antériorité » : FAIT RAPPORTÉ par la pièce citée. « Stég » désigne la lecture de la stéganographie, « Lect2 » la seconde lecture, « Rech » la recherche exhaustive.
- Verdicts, énoncés neufs et épreuves : PROPOSITION. La colonne « épreuve » donne l'issue qui ferait tomber l'énoncé neuf.

| Revendication | Antériorité qui la touche | Verdict | Énoncé neuf | Épreuve qui le réfuterait |
|---|---|---|---|---|
| Lemme d'additivité | Avenhaus et Jaech 1981, p. 25, 30-31 ; Ker 2006, p. 6-7, 9 (Stég). Tailor 2510.04303, p. 12 ; Ghanem 2608.02698, p. 5 ; Khilar 2610.13083, proposition 3 (Rech). | Retiré comme résultat (décidé) ; composantes citées en outils. Fermer le repli de N-004 « sans nouvelle décision ». | Question : en séquentiel, l'étalement est-il le cas le moins favorable au défenseur ? Condition à mesurer : décalage additif, sans compensation. | Simulation : taux de franchissement égaux pour tôt, tard, étalé. |
| Théorème négatif | Zhang et Gao 2606.10456, p. 3, 7-8 ; Arias-Castro et collaborateurs 2012, p. 14-20 (Lect2). Khilar, proposition 1 ; Rose et collaborateurs 2604.01151, p. 17 (Rech). | Retiré comme résultat (décidé). Distinction permutation contre marginales : remarque citée. Unification par permutations : question. | Question : le sabotage des organismes déplace-t-il la position des scores de sondes, leur dépendance, ou les deux ? | Tests de position et de dépendance étalonnés sur substituts permutés : aucun ne dépasse son niveau. |
| Accumulation toujours valide | Ker 2010, p. 7, 11 (Stég). Filler, Ker, Fridrich 2009, p. 3-5 (Lect2). Khilar, propositions 3-4 ; Makins et collaborateurs 2607.07368, p. 45 (Rech). | À resserrer. | « À déplacement par acte fixé, le rappel suit le nul hérité en n et m ; la garantie vaut sous une référence honnête de taille m déclarée, pour n au plus m ; l'écart au nul est le résultat. » | Jumeau contre jumeau : la surface du seuil honnête s'ajuste au nul sans résidu. |
| Gain de l'accès interne | Parrack, Attubato, Heimersheim 2025, p. 1-8 (Lect2). | Tenue ; parent et indice contraire à citer ; complétée. | « À taux total de fausses alertes égal, l'union "meilleure boîte noire et sonde" rattrape plus de sabotages diffus que l'union "meilleure boîte noire et seconde boîte noire d'une autre lignée". » | Borne haute de l'écart inférieure ou égale à zéro sur la famille tenue à l'écart. |
| Règle de la référence honnête (N-076) | Ker 2010, corollaire 1, p. 11 (Stég). Wen et collaborateurs 2411.17693, p. 18 (Rech). | À resserrer : « application du corollaire 1 » ; unité commune à m et n à fixer. | Aucun : rien n'est revendiqué. | — |
| Marge asymétrique | Aucune des trois pièces ; N-077. | Déjà retirée ; table à corriger. | Mesure descriptive. | — |
| Interaction flou contre net ; transposition du jeton à l'action ; validité et robustesse | Makins, p. 1, voisin de la transposition (Rech). | Non touchées. | — | — |
| Courbe selon le nombre d'agents | Avenhaus et Jaech, p. 25, 31 (Stég). Makins, p. 1 (Rech). | À resserrer : nommer l'agrégateur. | « À budget et nombre total d'actions fixés, la somme globale est prédite plate en nombre d'agents, le maximum décroissant ; la sonde change la constante, non la pente. » | Montage de fragmentation : la somme baisse, ou les pentes boîte blanche et boîte noire diffèrent. |
| Co-élévation entre copies | Arias-Castro et collaborateurs, p. 2, 14-20 (Lect2). Rose et collaborateurs, p. 17 ; Khilar, p. 1-2 (Rech). | À resserrer. | « La co-élévation est rapportée contre la frontière héritée (taille de coalition, nombre de copies, corrélation) et contre la corrélation honnête, sur référence de taille déclarée. » Bases ajoutées : carré de la somme, alignement d'activations, détecteur de comptes. | Copies honnêtes : alarme au-dessus du niveau. Sous attaque : pas mieux que le carré de la somme. |
| Statistique conjointe temps et agents | Avenhaus et Jaech, p. 30 (Stég). Zhang et Gao, proposition 2, p. 4 (Lect2). Podkopaev et collaborateurs 2023, « Sequential kernelized independence testing » (rapporté, non vérifié sur PDF). | À resserrer. | « Base obligatoire : la somme globale. Gain revendiqué sur les seuls sabotages qui déplacent la dépendance. Adversaire entraîné : mesure descriptive. » | Pas de gain sur la somme globale à fausses alertes égales. |
| Nombre et diversité des moniteurs | [HYPOTHÈSE, mémoire] nombre effectif sous corrélation : Kish 1965, « Survey Sampling » (rapporté, non vérifié sur PDF). | À vérifier : la loi peut être élémentaire. | À rattacher à la complémentarité. | — |
| Diversification et coordination ; riposte et fuite ; mesure de délégation | Aucune des trois pièces. | Non touchées. | — | — |
| Papier C (six hypothèses, second terrain) | Parrack et collaborateurs : moniteur de texte recevant des scores de sondes, voisin du quorum par type d'accès [HYPOTHÈSE] (Lect2). | Non touché ; une citation à ajouter. | — | — |
| Organisme d'idéation | Aucune des trois pièces. | Non revu ici. | — | — |
| Candidates de la réponse 2 : trois planchers, loi de la référence « mesurée » | Stég, verdict (b). | Retirées ; absorbées par la thèse. | — | — |
| Audits économisés, surplus de capacité, attestation du tirage | Antériorités de la réponse 2, non vérifiées sur PDF. | Non touchées par les trois pièces. | — | — |

### La thèse retenue, revue

- **Formulation proposée** [PROPOSITION] : « Les lois de la dissimulation répartie (Ker 2007 et 2010 ; Avenhaus et Jaech 1981), déjà transposées au suivi des usages contre l'extraction (Khilar 2026), donnent un modèle nul du dommage qu'un saboteur diffus peut cacher. Nous mesurons, sur des scores de sondes d'agents qui sabotent, où ce nul tient et quels termes s'y ajoutent ; puis ce que l'accès interne rattrape et qu'une seconde boîte noire ne rattrape pas. »
- **Ce qui est déjà mesuré ailleurs** [FAIT RAPPORTÉ, recherche exhaustive et seconde lecture]. La loi est chiffrée sur données réelles contre l'extraction (Khilar, proposition 4, p. 5). La dépendance honnête des scores est mesurée en boîte noire (Makins et collaborateurs, p. 45 ; Zhang et Gao, p. 8). Le propre de la mesure se réduit donc aux scores de sondes, à la référence de taille m et aux composantes de variance.
- **Hypothèse la plus exposée** [HYPOTHÈSE]. Filler, Ker et Fridrich gardent l'exposant un demi sous une chaîne stationnaire (seconde lecture, p. 3 à 5). Une tâche d'agent a un début et une fin : la stationnarité est l'hypothèse à éprouver en premier.
- **Puissance** [HYPOTHÈSE, ordre de grandeur de ma main, à refaire]. Sur une décade d'horizons, un exposant de 0,6 au lieu de 0,5 ne change l'écart-type du cumul que de 26 %. Le déceler demande de l'ordre de cent à deux cents tâches indépendantes à chaque extrémité. Sans ce compte, la prévision sur l'exposant n'est pas réfutable.
- **Complémentarité** [PROPOSITION]. Conditionner sur les seuls sabotages manqués par la meilleure boîte noire avantage tout moniteur peu corrélé au premier. La comparaison juste oppose deux unions recalées au même taux total de fausses alertes.
- **Indice contraire à écrire à côté de la prévision** [FAIT RAPPORTÉ, seconde lecture, p. 7-8]. La note rapporte une boîte blanche inférieure à la boîte noire sur les portes dérobées dans le code.

### Phrases à ne plus écrire

Elles s'ajoutent aux douze de la réponse 9 et aux deux de la note de stéganographie [PROPOSITION].

1. « L'aveuglement des statistiques de marginales est connu ; nous l'énonçons sur des scores de sondes » (recherche exhaustive, § 5). Écrire : « contre une attaque à marginales préservées, l'espérance des statistiques additives ne bouge pas ; nous mesurons ce que déplacent des attaques jouées par de vrais agents ».
2. « Nous n'avons pas trouvé d'énoncé, pour des moniteurs d'agents, de l'invariance… » en ouverture (même pièce). Écrire : « l'indifférence de la somme à la répartition est établie (Avenhaus et Jaech 1981 ; Ker 2006) ; nous vérifions ses hypothèses sur des scores de sondes ».
3. « Un rappel qui croît avec l'horizon », sans le déplacement par acte, m et n.
4. « Garantie toujours valide », sans « sous une référence honnête de taille déclarée ».
5. « La statistique conjointe bat le séquentiel par agent et la coupe transversale », sans la somme globale.
6. « La courbe décroît plus doucement », sans l'agrégateur.
7. « Antécédent défectueux », tant que la simulation n'a pas rejoué le tableau 2. Écrire : « limite à longueur finie, notre lecture ».
8. « Le théorème du programme est inexact », sans « dans la lettre de la version 2 ; N-003 l'avait borné ».
9. « Contrôle conditionnel non trouvé » chez Parrack et collaborateurs, sans « 13 pages lues sur 39 ».
10. « Les deux issues sont publiables », sans la puissance du plan.
11. « T (c) à (f) déclarables » ; « repli du lemme disponible sans nouvelle décision ».
12. « Table en vigueur », pour la version 1.

## Question neutre pour le collisionneur

« Une équipe surveille des agents logiciels autonomes sur de longues tâches. À chaque action, un ou plusieurs détecteurs rendent un score ; certains lisent le texte produit, d'autres l'état interne de l'agent. On vous remet une liste d'énoncés, dans un ordre tiré au hasard, sur trois sujets : le cumul des scores au fil d'une tâche, leur comparaison entre agents identiques travaillant ensemble, et l'apport comparé des deux sortes de détecteurs. Certains énoncés sont de l'équipe, d'autres non ; rien ne les distingue. Pour chacun, sans présumer de son sort : (1) est-il exact tel qu'écrit ? Donnez une preuve ou un contre-exemple. (2) Quel est le travail publié le plus proche que vous connaissiez, dans quelque domaine que ce soit, et que dit-il exactement ? (3) Classez-le : déjà établi ailleurs, conséquence immédiate d'un résultat établi, ouvert, ou faux. (4) Quelle observation vous ferait changer de classe, dans chaque sens ? (5) Quelle expérience unique le trancherait, et quelle taille d'échantillon lui faut-il ? Dites votre degré de certitude et ce que vous citez de mémoire. »

La liste jointe reprend chaque énoncé en mots courants, témoins compris [PROPOSITION].

## Décisions qui reviennent au directeur

**Décision 1 — Approuver la demande reformulée et la question neutre avant l'envoi au collisionneur, avec ou sans énoncés témoins.**
- *Enjeu.* Sans témoins, un verdict « occupé » unanime ne se distingue pas d'un biais d'accord.
- *Option a : envoi avec six à huit témoins au statut connu, écrits par un agent neuf.* Avantage : taux de détection mesuré. Inconvénient : une préparation de plus.
- *Option b : envoi sans témoins.* Avantage : immédiat. Inconvénient : convergence ininterprétable.
- *Recommandation.* Option a. Confiance : 0,7.

**Décision 2 — Refaire la table (version 2) en y propageant les retraits.**
- *Enjeu.* Quatre revendications s'adossent encore au lemme et au théorème ; la table ignore N-075 à N-077.
- *Option a : version 2 provisoire maintenant, scellée après le collisionneur.* Avantage : plus de phrase caduque en circulation. Inconvénient : deux passes.
- *Option b : attendre le collisionneur et les experts.* Avantage : une seule passe. Inconvénient : le papier B reste écrit contre un socle retiré.
- *Option c : ne réviser que le papier A.* Avantage : périmètre court. Inconvénient : la statistique conjointe garde une supériorité que la somme globale peut annuler.
- *Recommandation.* Option a. Confiance : 0,65.

**Décision 3 — Fixer le sort de la distinction entre attaque par permutation et attaque à marginales préservées.**
- *Enjeu.* C'est la seule pièce exacte du théorème retiré, et elle fonde le mot « antécédent défectueux ».
- *Option a : remarque citée, après la simulation qui rejoue le tableau 2 et une question aux auteurs.* Avantage : exact, vérifié hors de nous. Inconvénient : aucun crédit de nouveauté.
- *Option b : retrait complet.* Avantage : simple. Inconvénient : la réserve sur 2606.10456 reste sans fondement écrit.
- *Option c : maintien en revendication.* Avantage : continuité. Inconvénient : élémentaire, contraire à la thèse retenue.
- *Recommandation.* Option a. Confiance : 0,6.

**Décision 4 — Exiger le calcul de puissance et le banc à vérité plantée avant de sceller la prévision.**
- *Enjeu.* Un plan trop court rend la thèse indécidable.
- *Option a : calcul d'abord, sur les exécutions honnêtes déjà au dépôt.* Avantage : on scelle une épreuve qui peut échouer. Inconvénient : quelques jours.
- *Option b : sceller maintenant.* Avantage : aucun délai. Inconvénient : issue indéterminée probable.
- *Option c : réduire la thèse aux termes mesurables (constante, terme entre tâches), l'exposant étant rapporté sans prévision.* Avantage : court et honnête. Inconvénient : renonce à la question de la dérive.
- *Recommandation.* Option a, repli sur c si la puissance manque. Confiance : 0,75.

**Décision 5 — Compléter les lectures avant toute phrase « non trouvé ».**
- *Enjeu.* Deux « non trouvé » dont dépend la thèse reposent sur des lectures partielles.
- *Option a : lecture ciblée (fin de Parrack et collaborateurs, fin de Zhang et Gao, arbres de Ker 2010 et d'Arias-Castro et collaborateurs).* Avantage : ferme ces deux points. Inconvénient : bilans séquentiels toujours non lus.
- *Option b : lecture complète, bilans séquentiels et jeux d'inspection compris.* Avantage : cadrage entier. Inconvénient : délai.
- *Option c : aucune.* Avantage : aucun délai. Inconvénient : contraire à la règle anti-faux-gap.
- *Recommandation.* Option a maintenant, option b avant la rédaction. Confiance : 0,7.

FIN DE LA RÉPONSE
