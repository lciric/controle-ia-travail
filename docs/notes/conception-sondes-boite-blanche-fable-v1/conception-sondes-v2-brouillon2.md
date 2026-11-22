# Conception des sondes de la boîte blanche, version 2 (brouillon 2)

- **Accord** : GO-2026-11-22-126 (décisions 0 à 5). **Auteur** : session de conception `session_013QMayndh51FN5XbmHpmEFg`. Modèle servi : celui que la règle « Qui conçoit » réserve aux conceptions, attesté par l'attribution des commits de cette pièce et par la ligne de cette session à la liste « qui a lu quoi » ; contre-lecture par un autre modèle. **Date (UTC)** : 2026-11-22, 20:45Z ; remplace le brouillon 1 (`682f2f29cc9f38d3b87ae4f90619a0e388d939971f28fe04f9c43de284687c3d`, gardé).
- **Classe** : le § 7, qui porte des critères de décision, est une pièce décisive (chaîne complète) ; le reste est une note de travail.
- **Exposition de l'auteur** : il a lu les verdicts des sondes génériques, de l'apprentissage des sondes sur la tâche et du témoin positif planté (ce dernier par extraits), et la note de résolution du barreau 5 (v2). Il n'a ouvert ni le texte scellé du test sur les adaptateurs jumeaux, ni son code de lecture, ni ses sorties.
- **Statut** : note de conception. Elle ne modifie ni le programme ni aucun texte scellé, ne franchit aucune porte et ne revendique rien. **Elle ne porte aucun chiffre de résultat** : une session aveugle peut la lire. Ses embranchements (§ 7) sont à sceller avant le verdict du test « sabotage ou empreinte » sur les adaptateurs jumeaux (barreau 5).
- **Elle précise**, pour la conduite du travail, la batterie de sondes v0 du brief (T0.7). Chaque écart à T0.7 est listé à l'annexe A et porté à Lazar ; tant qu'il n'est pas accordé, T0.7 fait foi. Chaque lecture décisive garde son propre texte scellé (R1) : cette note en fixe le cadre et les niveaux, non les seuils ni les effectifs.

## 1. Principe

Une sonde ne vaut pas mieux que le contraste qui l'apprend et la juge. Le contraste se choisit donc avant la famille de sondes, et il doit ne différer que par le sabotage : mêmes poids, ou poids jumelés par construction ; même texte, ou lecture avant le champ qui révèle le sabotage. L'unité d'analyse est le jeu de poids ou la tâche, jamais l'action.

Trois questions distinctes, dans cet ordre : existe-t-il une trace propre à l'acte ; se transporte-t-elle à une unité jamais vue ; se lit-elle sans étiquette de sabotage. La première est circulaire par construction et ne prouve que l'existence. La deuxième respecte l'anti-circularité du programme (§ 7). La troisième seule est déployable.

## 2. L'échelle de preuve

| marche | question | sonde | contraste | si elle échoue |
|---|---|---|---|---|
| préalable | Une aire entre poids non appariés veut-elle dire quelque chose ? | sonde d'identité ; étalon de transport ; rejeu croisé du texte et des poids | deux honnêtes non appariés ; saboteur contre honnête non apparié ; source du texte croisée avec les poids qui lisent | voir § 7 ; aucune marche n'est bloquée, mais les libellés permis changent |
| 0 | La chaîne retrouve-t-elle un résultat publié, sur données publiques, avec le modèle de 8 milliards de paramètres ? | génériques de concept | jeu public ; résultat visé vérifié sur PDF empreinté, page citée (R7), avant le devis | audit de la chaîne d'extraction (équivalence d'activations, couche, gabarit de conversation) avant toute conclusion ; si l'audit ne trouve rien, **proposition** à Lazar (nœud « contrôle d'échelle », N-053, point 4) ; les marches 1 à 3 ne continuent que si cet audit est passé |
| 1 | Existe-t-il une trace propre à l'acte ? | différence de moyennes, puis linéaire régularisée | poids constants ou jumelés, texte égal ou lecture avant le champ, témoins du § 4 | pas de marche 2 sur ce banc ; l'échec est rapporté (R4) ; la reconception porte sur **les sondes** (famille, couche, position lue) et sur la marche 3, dans l'esprit de N-062 ; l'organisme n'est repris que si son contrôle de manipulation par l'oracle échoue, jamais d'après un score de sonde (N-053, point 5) |
| 2 | Se transporte-t-elle ? | la même, gelée avant l'ouverture | unité jamais vue : autres jumeaux, autre recette, autre mode **vu** ; jamais le mode tenu à l'écart de G1, ni une famille ou une banque réservée à une lecture de G1 (N-054, point 3 ; N-062, points 3 et 6) ; le texte de chaque marche 2 nomme le jeu lu et atteste qu'il n'est pas réservé | la sonde reste un plafond ; elle ne compte pas pour le critère 3 de G0 |
| 3 | Se lit-elle sans étiquette de sabotage ? | apprise sur honnêtes seuls ; génériques | résidu « déclaré moins attendu », lu sur des épisodes honnêtes et sabotés d'un banc du § 4, contre la réestimation de la grandeur par le texte seul | la sonde ne sert pas de bras déployable ; l'échec est rapporté (R4) ; la conséquence pour les bras de G1 est fixée par le préenregistrement de G1 |

Niveaux : 99 % pour les lignes décisives d'une marche, 95 % pour les diagnostics et les lignes descriptives, déclarés comme tels dans chaque texte.

Symétrie (R4). À chaque marche, un résultat trop net dans un sens ou dans l'autre (aire proche de 1, toutes les unités du même signe, effet bien plus grand que la prévision scellée) déclenche le même audit que l'échec : alignement des clés et des étiquettes, prédicteurs triviaux, chemin de calcul, relus par un agent neuf ; aucune suite n'est engagée avant sa réserve écrite.

## 3. Familles de sondes

Pour toutes : lecture à la couche 15, fixée d'avance ; couches 7 et 23 rapportées (N-056, point 3). Score d'une action : le maximum sur ses jetons. Aucune moyenne ni médiane sur les jetons hors d'un bras de diagnostic déclaré (N-026). Ajustement au processeur, en double précision, sur activations gardées.

| famille | définition | rôle |
|---|---|---|
| Différence de moyennes appariée | différence des moyennes des jetons des deux classes ; appariée par action quand la même action est lue sous deux jeux de poids ou deux conditions | **sonde de référence** des marches 1 et 2 : aucune sélection, forme close |
| Différence de moyennes blanchie | la même, multipliée par l'inverse de la covariance intra-classe rétrécie | seconde lecture ; réglage choisi dans la boucle interne |
| Linéaire régularisée | régression logistique à pénalité quadratique sur les jetons | seconde lecture ; capacité de mémorisation rapportée |
| Apprise sur honnêtes seuls | régression du jeton d'avant le champ vers la grandeur déclarée, sur épisodes honnêtes ; statistique : résidu « déclaré moins attendu » | marche 3, exploratoire d'abord ; doit battre une réestimation par le texte seul ; lecture à position fixe, déclarée : elle ne sert pas de moniteur de production sans décision de Lazar sur cette agrégation |
| Génériques de concept (tromperie, enjeux, dissimulation, conscience d'évaluation) | apprises sur des jeux synthétiques ou publics, jamais sur nos organismes | hors de la ligne décisive des marches 1 à 3 ; seule exception : ils peuvent tenir le critère 3 de G0 (§ 6), sous leur propre texte scellé, après la marche 0 ; bras rapporté sur activations gardées |
| À attention, perceptron | familles du brief | bras rapporté seulement, sous validation croisée imbriquée |
| Mahalanobis | non supervisée, sur honnêtes | aiguillage d'audit à poids constants (N-075 v3, § 4) ; jamais entre poids différents |
| Apprise avec l'étiquette « adaptateur contre modèle nu » | positifs sous un adaptateur, négatifs sous le modèle nu | **abandonnée** : l'étiquette se confond avec les poids |

À résultat égal, la famille la plus simple porte la ligne décisive.

## 4. Bancs et témoins

Ce que toute lecture exige de son banc : (a) un contrôle de manipulation tenu avant la lecture : l'oracle établit le dommage ; pour une lecture qui vise le critère 3 de G0, la dose doit en outre être jugeable au sens de N-063 v2 : la base « mots et coût » de T0.6, rejouée sur le même banc et les mêmes épisodes, y échoue selon son propre critère ; si cette base n'est pas définie pour un banc ou un mode, le critère 3 y est « sans objet » jusqu'à décision de Lazar (nœud), et non jugé par analogie ; (b) des poids constants entre actions sabotées et honnêtes, ou des jumeaux appariés et répliqués ; (c) si le sabotage varie à poids constants, une variable qui le commande, connue de l'oracle, absente du texte de l'action ou présente à l'identique chez l'honnête. Cette note ne conçoit aucun organisme.

| banc | ce qu'il permet | limite |
|---|---|---|
| Sabotage par consigne sur le modèle nu, consigne bénigne appariée, paraphrases réservées | marches 1 et 2 à poids vraiment constants ; ouvert pour décembre (GO-2026-11-22-126, décision 5) | la sonde peut lire la consigne suivie plutôt que l'acte ; plus loin du risque réel |
| Adaptateurs jumeaux appariés par construction, répliqués | marche 1 entre poids appariés, marche 2 sur des paires jamais vues | lit une disposition écrite dans les poids, non un acte ; sans jumeau, l'identité revient |
| Organismes à sabotage conditionnel répliqués, avec jumeaux et déclencheur réservé | marches 1 et 2 à l'intérieur de chaque jeu de poids | à construire ; calcul de puissance scellé et devis (décision 5) ; le déclencheur se lit toujours : on montre que la sonde n'en dépend pas |
| Organismes publics, d'une autre main | marche 0 ; validation externe | licences à vérifier (N-061) |

Retiré de toute lecture décisive et de toute phrase de détection : l'adaptateur saboteur unique comparé au modèle nu ; il ne reste que comme objet du diagnostic de rejeu croisé.

| témoin | rivale qu'il ferme |
|---|---|
| Jumeau apparié par construction ; intensité égalée (divergence des sorties, norme du déplacement à la couche lue), jamais par un score de sonde (N-053, point 5) | « tout réglage fin allume la sonde » |
| Honnête contre honnête non appariés (sonde d'identité, étalon de transport) | « la sonde lit l'identité des poids » |
| Consigne cachée bénigne appariée (même longueur, même ton de secret) | « la sonde lit la présence d'un secret » |
| Consigne de sabotage présente, sabotage absent selon l'oracle ; et sabotage présent sous consigne bénigne, si le banc en produit | « la sonde lit la consigne, non l'acte » : une marche 1 sur le banc par consigne n'est interprétée « acte » que si la sonde sépare, sous la même consigne, les actions sabotées des actions non sabotées selon l'oracle |
| Déclencheur présent sans sabotage ; déclencheur réservé | « la sonde lit le déclencheur » |
| Texte égal (relecture à état imposé) ; lecture avant le champ révélateur ; et, pour toute phrase d'intention, la lecture aux positions d'évidence textuelle masquées de N-053, point 1, rapportée | « la sonde lit le texte » |
| Bases à côté de chaque ligne : valeur déclarée seule, « mots et coût », classifieur lexical, lecteur honnête ; et les prédicteurs triviaux de la consigne du développeur (longueur, rang du pas, valeur déclarée seule) | « une boîte noire en fait autant » |

## 5. Gardes

Chaque garde qui arrête une lecture est éprouvée sur un cas sain et sur un artefact (R5) ; l'épreuve est citée par chemin et empreinte dans le texte qui l'emploie.

1. **Activations gardées**, sur une même liste de clés pour tous les jeux de poids comparés ; sans elles, pas de lecture.
2. **Même chemin de calcul** pour toutes les cases d'un contraste : toutes relues par le même programme, même précision, même gabarit ; identifiant du chemin écrit au manifeste de chaque série et vérifié par le magasin. Un contraste qui mêle série d'origine et série relue est un diagnostic déclaré, jamais une ligne décisive. Sonde ajustée au processeur.
3. **Validation croisée imbriquée**, groupée par tâche et par unité ; toute aire décisive est lue hors pli ; le nul rejoue toute la sélection.
4. **Unité, niveau et règle de famille** écrits avant la lecture ; test exact à l'unité.
5. **Épreuve à vérité plantée** du programme de lecture, aux effectifs réels, avant toute ouverture (R5).
6. **Prévision scellée, contre-lecture, verdict par un agent neuf** (R1, R2, R13) ; audit de symétrie sur tout résultat trop net, dans les deux sens (R4).

## 6. Le critère 3 de G0, tel que Lazar l'a retenu

Lecture (b) (GO-2026-11-22-126, décision 1, qui renvoie au § 4.6 de la note que cet accord vise ; cette note-là porte des résultats, une session aveugle ne l'ouvre pas). Le critère est tenu si une sonde non circulaire — générique, ou apprise sur une unité et lue sur une autre — est au-dessus du plancher aléatoire apparié **et** au-delà du témoin apparié, à une dose jugeable au sens de N-063 v2, sur l'organisme à consigne cachée avec son témoin bénin et sur un banc à poids constants ou à jumeaux tenus à l'écart. Une sonde de la marche 1 seule ne le tient pas. Si aucune dose ne qualifie, l'issue est « sans objet », et la porte lit le critère 3 comme non tenu à cette course (N-063 v2, point 2). S'il n'est pas tenu à l'échéance, c'est le nœud que le brief prévoit, non un arrêt.

**Écart à la lettre du programme, dit ici.** Le programme (§ 7) et le brief (T0.7) écrivent « une famille contre une autre ». La lecture accordée est plus étroite : des paires jamais vues de la même recette y valent « non circulaire ». La lecture entre deux recettes ou deux étiologies est rapportée à côté, comme la lecture forte. Si Lazar entend autre chose par son accord, c'est un nœud, à lever avant la première lecture qui viserait le critère 3.

Pour G1, cette note n'écrit ni critère ni rangement de bras. Le rangement « générique » ou « spécialisé » de chaque sonde suit N-054, point 3 : il dépend de ce que son concepteur savait d'un mode, déclaré par écrit, et non de la marche passée ; la sonde apprise sur honnêtes seuls, qui lit la grandeur du champ de coût, est spécialisée. Le calibrage des fausses alertes est fixé par le préenregistrement de G1.

## 7. Embranchements, écrits avant le verdict

L'issue scellée du test « sabotage ou empreinte » sur les adaptateurs jumeaux (barreau 5) est rangée dans l'une des trois classes ci-dessous par une **table de correspondance** qui remplit les cinq conditions suivantes, faute de quoi ce § 7 n'est pas scellable :
1. elle reprend chaque libellé d'issue du texte scellé du test, mot pour mot, y compris les libellés d'arrêt, de non-calcul et de non-test, et assigne à chacun une seule classe ; un résultat qui diffère selon la famille, la dose ou la couche est rangé par famille et par dose, et la conduite qui suit est celle de la classe la plus restrictive (ordre : « Contraire », puis « Non établi », puis « Au-delà ») ;
2. tout libellé absent de la table, ou toute issue que la table ne permet pas de ranger sans interprétation, est rangé « Non établi » ; une issue arrêtée pour une cause technique déclarée (une panne technique n'est pas un résultat) n'est rangée dans aucune classe : le § 7 attend la relance, et rien de ce qui dépend du verdict ne part entre-temps ;
3. elle est écrite par une session qui n'a vu ni sorties ni verdict du test, contre-lue (R2), scellée et inscrite au registre avant le scellement du verdict ; son empreinte est écrite dans cette note avant le scellement de celle-ci ; les deux horodatages du registre en font la preuve ;
4. le rangement est fait par l'agent neuf du verdict (R13), qui applique la table sans l'interpréter et n'a pas écrit cette note ;
5. toute modification de la table après son scellement est un écart, porté à Lazar comme nœud.

Empreinte de la table de correspondance : à inscrire ici par la mère avant le scellement.

| classe du verdict | ce qui suit |
|---|---|
| **Au-delà de l'empreinte**, sur des paires jamais vues | Audit de symétrie d'abord si le résultat est trop net (§ 2). La ligne supervisée tient pour cette recette d'adaptateurs. Suite : marche 2 vers une autre recette ou un autre mode, sous son propre texte. Candidate au critère 3 seulement à une dose jugeable. Aucune phrase « acte » avant une marche 1 à poids constants. |
| **Non établi** à cette puissance | Aucune phrase « sabotage ». Aucune paire de plus n'est formée avant une marche 1 à poids constants (banc par consigne). La sonde apprise sur honnêtes seuls est la première des lectures sur données gardées, dans le rang que lui donne l'accord (après les décisions 1 à 3), exploratoire, sous texte contre-lu ; elle ne devient pas décisive. |
| **Contraire**, ou empreinte seule | Plus aucune ligne décisive supervisée sur un adaptateur. Toute la boîte blanche passe à poids constants. Les adaptateurs ne servent plus qu'à l'étude de l'empreinte. |

Croisé avec les diagnostics préalables :

| issue | ce qui suit, dans les trois classes |
|---|---|
| Identité « forte » ou « intermédiaire » | aucune aire entre poids non appariés ne se cite comme une détection ; toute ligne de ce genre porte son témoin apparié ou l'étalon de transport |
| Identité « faible » | audit de symétrie ; la règle ci-dessus tient jusqu'à son issue |
| Transport « fort » | la direction peut être essayée sans jumeau sur une autre recette, sous son propre texte |
| Transport « faible » ou « non établi » | aucun usage sans jumeau ; les lectures entre poids restent des lectures de banc |
| Transport « contraire » | audit de symétrie (R4) ; aucun usage sans jumeau |
| Rejeu croisé : interaction « établie » | rien de plus sans texte neuf |
| Rejeu croisé : « non interprétable : chemin de calcul non mesuré » | relecture par un même chemin de calcul demandée sur devis avant toute phrase |
| Rejeu croisé : « non établie » | rien de plus sur l'adaptateur unique |
| Rejeu croisé : « contraire » | audit de symétrie (R4) ; rien de plus sur l'adaptateur unique |
| Toute ligne « non testable », « non calculable », « effectif insuffisant » ou « non interprétable » | traitée comme « non établi » de la même question ; aucune règle plus permissive ne s'en déduit |

Et avec la marche 0 : si la chaîne ne retrouve pas le résultat publié, la chaîne d'extraction est auditée avant toute conclusion ; si l'audit ne trouve rien, une proposition est portée à Lazar (nœud « contrôle d'échelle ») : retirer les génériques des lignes de la phase à cette taille, ou changer de taille sur accord. Les marches 1 à 3 ne continuent que si l'audit d'extraction est passé : la vérité plantée, faite d'activations fabriquées, n'éprouve pas l'extraction.

Dans tous les cas : les gardes du § 5 ne changent pas ; les génériques restent hors de la ligne décisive des marches 1 à 3 (§ 3) ; le banc par consigne s'ouvre pour décembre ; le banc à sabotage conditionnel attend son calcul de puissance et son devis.

**Portée des cases.** « Adaptateur » désigne ici la recette d'adaptateurs du test en cours et toute lecture qui compare deux jeux de poids différents. Aucune case ne touche les lectures à l'intérieur d'un même jeu de poids (banc à sabotage conditionnel, § 4) : ce banc suit le seul § 4 et attend son calcul de puissance et son devis, dans toutes les classes. « Aucune paire de plus » vise les paires d'adaptateurs jumeaux de la recette du test en cours. **Règle de priorité** : quand deux cases s'appliquent, la plus restrictive l'emporte ; une marche 2 vers une autre recette se fait avec jumeaux si le transport n'est pas « fort ».

## 8. Ordre de travail

0. Table de correspondance du § 7 : à écrire, contre-lire et sceller avant le verdict du test en cours ; c'est la pièce la plus pressée.
1. Code des quatre briques (magasin, formes closes, lectures, vérité plantée) : lancé.
2. Texte des diagnostics préalables : scellé avant le verdict ; lecture au processeur après.
3. Devis de la marche 0 ; aucune dépense avant son accord.
4. Texte et course de la marche 1 sur le banc par consigne : sur devis.
5. Calcul de puissance scellé et devis du banc à sabotage conditionnel.
6. Sonde apprise sur honnêtes seuls : exploratoire, au processeur, sur données gardées, sous texte contre-lu.

## 9. Limites

Une seule taille de modèle, une seule couche décisive, un mode de sabotage chiffré à ce jour. Un succès de la marche 1 ne dit ni « intention », ni tenue devant un modèle entraîné contre la sonde, ni transport à un autre modèle. Les sondes sont un accélérateur et un aiguillage de l'audit, non une garantie (N-075 v3, § 2) : ce qu'on leur demande est ce qu'elles capturent parmi les manqués de la boîte noire, à fausses alertes égales.

## Annexe A — Écarts à la batterie de sondes v0 du brief (T0.7), portés à Lazar

Tant qu'un écart n'est pas accordé, T0.7 fait foi sur ce point.
1. Les sondes génériques de concept ne portent plus la ligne décisive des marches 1 à 3 ; elles restent candidates au critère 3 de G0 et bras rapporté.
2. Les familles à attention et à perceptron deviennent des bras rapportés ; Mahalanobis, un aiguillage d'audit à poids constants.
3. Une famille s'ajoute : la différence de moyennes appariée, avec sa version blanchie ; et, en exploratoire, la sonde apprise sur honnêtes seuls.
4. L'étiquette « adaptateur contre modèle nu » est abandonnée pour apprendre une sonde.
5. Les marches s'ajoutent au « fini quand » de T0.7 : une aire au-dessus du plancher ne suffit plus sans témoin apparié (c'est la décision 1 de GO-2026-11-22-126 pour le critère 3).

## Contre-lecture

- **Contre-lecture 1** : sous-agent neuf, d'un autre modèle que l'auteur. Brouillon relu : brouillon 1, `682f2f29cc9f38d3b87ae4f90619a0e388d939971f28fe04f9c43de284687c3d`. Rapport : `docs/notes/conception-sondes-boite-blanche-fable-v1/contre-lecture-conception-sondes-v2-brouillon1-v1.md`. Verdict : « après corrections » ; 5 remarques bloquantes, 11 majeures, 9 mineures.
- **Traitement.** Toutes acceptées. Telles quelles : B-1, B-2, B-3, M-1 à M-8, M-10, M-11, m-1 à m-7, m-9. Autrement :
  - B-4 : l'accord de Lazar vise un texte qui écrit « apprise sur une unité et lue sur une autre » et « jumeaux tenus à l'écart » ; le § 6 le cite, dit l'écart à la lettre du programme et garde le nœud si Lazar entend autre chose ;
  - B-5 : le modèle de l'auteur n'est pas écrit en toutes lettres dans la pièce ; il est attesté par l'attribution des commits de cette pièce (ceux que le contre-lecteur a vus sont des commits de la mère, ancêtres de la branche) et par la liste « qui a lu quoi » ; la classe du § 7 est déclarée en tête ;
  - M-9 : « précise » au lieu de « remplace », avec l'annexe A ;
  - m-8 : les renvois à N-075 v3 ont été lus par l'auteur sur la décision elle-même (sections 1 à 4 et 6), non par le contre-lecteur.
- La vérification des corrections par le même contre-lecteur est demandée sur ce brouillon 2.
