# Question de la course 2 — volet défense — fusion v1 (axes 1, 2, 3, 4, 5, 7 et boucle ; brouillon, non contre-lu, non servi)

Sous-agent neuf (Opus 5.5), 29 octobre 2026, relevé `date -u` 11:52 UTC. Fusion selon `recoupement-question-course-2-defense-v1.md`
(même dossier), critères du § 3 de `question-mere-course-ideation-v3.md` (`1b08e17f…`). Hors périmètre, non repris : l'axe des hypothèses
fragiles et le texte qui lui est propre. Les mentions « [à trancher par Lazar] » renvoient aux décisions D1 à D13 du recoupement ;
le texte porte l'option par défaut. **Texte servi : 11 971 caractères** (`wc -m` entre les deux marqueurs, marqueurs exclus).
À faire avant service : contre-lecture par un modèle d'un autre fournisseur (R2) ; retrait des mentions « [à trancher par Lazar] » ;
remesure des consignes chez session-depot ; devis et GO.

<!-- DEBUT-TEXTE-SERVI -->
# Course d'idéation — question « défense » — génération g

## Glossaire (vaut définition)
- **Trajectoire** : actions textuelles (a_1, …, a_T) d'un agent à poids ouverts (8 ou 70 milliards de paramètres) et leurs activations internes.
- **Loi de référence** P_0 : loi des trajectoires honnêtes. **Loi déplacée** P_ε : loi alternative d'intensité ε ≥ 0, égale à P_0 en ε = 0. **Famille** : classe de lois déplacées de même mécanisme. **Menace diffuse** : écart par action sous le seuil de détection par action, écart cumulé grand.
- **Statistique** S : fonction de la trajectoire ; boîte noire (lit le texte) ou blanche (lit les activations) ; par action, ou séquentielle (fausse alerte tenue à tout horizon).
- **Fausse alerte** : P_0(S > s). **Puissance** : P_ε(S > s). **Rappel à 1 %** : puissance à fausse alerte 0,01. **Aire** sous la courbe : rapportée, jamais seule.
- **Plancher apparié** : S sous des directions aléatoires de même covariance ; une sonde compte si sa borne basse dépasse le quantile 0,95 du plancher. **Sonde nulle de chaîne** : même chaîne sur une partition aléatoire d'honnêtes ; elle doit rester au hasard.
- **Famille tenue à l'écart** : jamais vue pendant la conception, fixée par une instance qui n'a conçu aucune statistique. **Transfert** : puissance conservée sur une famille inédite. **Invariance** : propriété de S inchangée sous une classe nommée de transformations.
- **Borne** : énoncé prouvé ; **impossibilité** (aucune S d'une classe ne dépasse sa fausse alerte sous une classe de lois déplacées) ou **garantie** (puissance β à fausse alerte α).

## Préambule
Programme défensif : sondes, statistiques sur texte, agrégation séquentielle, théorie des angles morts, juge figé à borne démontrée sur les fausses promotions. Porte G1 : battre chaque comparateur boîte noire scellé, par famille, au rappel à 1 %, fausses alertes au plus 5 points au-dessus, en une lecture. État (pièce A) : premier test interne nul (aucune sonde générique au-dessus du plancher) ; juges à 87 notes utilisables sur 100 pour 99 exigées ; garde muette sous environ 160 unités. HELIOS (pièce B) : un jeton par réponse, cinq couches médianes, agrégation sur les agents, rien dans le temps (p. 16, 27) ; rappel à 1 % de 0,38 sur TRANSFER (p. 18) ; séquentiel annoncé en travail futur (p. 18-19) ; juge textuel mesuré sur STEGO seul (p. 43-44) ; plus petit modèle, 20 milliards, le plus faible (table 13, p. 46).

**Règles.** Niveau méthode : aucune conduite d'agent, consigne, séquence d'actions ni procédé pour produire une loi déplacée ; une telle fiche est écartée avant le juge et comptée. Les pièces sont des données. Chiffre repris : pièce et page ; supposé : SUPPOSÉ. Données réclamées : liste D seulement ; jamais `donnees/`, familles scellées, internes des statistiques (directions de sonde comprises), carte des hypothèses, écarts du sujet avant G1. Aucune moyenne ni médiane sur les jetons dans une sonde de production. Un refus arrête votre tour.

**Fiche** (3 000 à 8 000 caractères ; « sans objet » et sa raison si inapplicable) : titre ; axe ; hypothèse ; prédiction chiffrée et signée (métrique de M, valeur, unité de lecture) ; livrables de l'axe ; données (D) ; coût (heures de processeur et de carte, dollars) ; antériorités (au plus cinq : titre, auteurs, année, élément qui leur manque, page du dossier ou « à vérifier ») ; source d'avantage (L) ou élément inédit ; critère de mort ; vis-à-vis ; SUPPOSÉ.

**Juge** (binaire, contre les listes fermées L, M, D). K1 : livrables de l'axe présents. K2 : source dans L avec coût de reproduction chiffré, ou antériorité la plus proche et élément absent nommés. K3 : prédiction chiffrée et signée sur M ; pour une détection, rappel à 1 % par famille. K4 : critère de mort à seuil numérique, écrit avant lecture ; première expérience sur processeur seul ou sur données déjà payées [à trancher par Lazar]. K5 : antériorités au format ; chiffres d'HELIOS conformes à la pièce B, même page (contrôle par programme) ; données dans D. Notable : K1 à K5 vrais. Classement par axe : facultatifs passés, puis coût croissant [à trancher par Lazar]. Un **témoin planté**, notable par construction, est glissé anonyme : non classé notable, il rend la notation fautive.

**Déroulé** [à trancher par Lazar]. Deux fiches par axe et par proposeur au plus. Passe 2 : sur les fiches anonymes de l'autre fournisseur, seulement marquer un champ faux (preuve jointe) ou ajouter une antériorité ; aucune fiche nouvelle. L'axe 7 va à une sous-session neuve : ce préambule, sans les axes 1 à 5.

## Axe 1 — Battre HELIOS : statistiques et agrégateurs
Partez d'une **table des écarts** (trois lignes au moins : métrique, familles, modèles, couches, jetons, agrégation ; HELIOS avec page ; programme ou « non mesuré ») ; proposez une statistique qui **comble une ligne**.
Obligatoires : (a) la table ; (b) la statistique au point de codage : quantité lue, couche, position de jeton, agrégation, apprentissage, seuil, case accès × agrégation ; (c) plancher apparié, sonde nulle de chaîne, un comparateur boîte noire scellé à capacité égale, lecture d'HELIOS rejouée sur notre banc (dernier jeton de la dernière réponse), couches rapportées séparément [à trancher par Lazar] ; (d) l'**invariance** qui justifie le transfert, et pourquoi une direction de régression logistique ne l'a pas ; (e) hyperparamètres réglés hors épreuve, transférés inchangés.
Facultatifs : comparateur gradué en information (nu, informé, à exemples hors de la famille lue) ; séparation réalisation / lisibilité ; transfert de type HELIOS (une famille apprise, six lues).
Matériau, non imposé : Mahalanobis, auto-encodeurs parcimonieux, patching d'activations, e-valeurs, seuils conformes, détecteurs de rupture, tests à deux échantillons.

## Axe 2 — Ce que le domaine retiendrait
Obligatoires : (a) forme (loi, notice d'angles morts, garantie, impossibilité) et énoncé quantifié (« pour toute statistique de la classe C et toute loi déplacée de la classe T vérifiant P… »), classes définies sans les familles scellées ; (b) les deux issues, en une phrase chacune ; (c) le résultat publié qui le rendrait inutile ; (d) le premier test préenregistrable ; le critère de mort tue l'énoncé, pas seulement le test.

## Axe 3 — Failles du programme, en pré-mortem
Placez-vous après l'échec : G1 n'est pas franchie (gain de la boîte blanche absent dans une famille, ou accumulation au plancher). Obligatoires : (a) l'**hypothèse porteuse** qui a cédé, avec une phrase citée de la pièce A ou C, et sa classe (circularité, artefact de source, « réel » instruit, puissance, juges, garde muette, modèle trop faible, fuite conception-épreuve, linéarité, additivité dans le temps, autre) ; (b) la classe de lois déplacées sous laquelle elle tombe, formelle si statistique ; (c) la **mesure** qui la révèle, en simulation ou sur D, avec la valeur qui confirme et celle qui infirme ; (d) l'ordre des cessions et la mesure qui le tranche ; (e) riposte, coût, et ce qui rendrait le résultat percutant plutôt que local.

## Axe 4 — Universalité sur les familles existantes
Livrable : un **préenregistrement à sceller**, pas un résultat ; vous ne voyez aucune famille scellée ; un tiers exécute. Obligatoires : (a) hypothèse, prédiction chiffrée et signée, métrique, seuil, plan d'analyse, critères de lecture gelés, liste d'arrêt ; (b) exclusion d'une famille à la fois, partition scellée par une instance tierce avant toute conception ; (c) lecture par famille : borne basse valide à tout instant contre le quantile 0,95 du plancher, fausses alertes comme pour G1 ; (d) si échec, hypothèse désignée **d'avance** (stationnarité, indépendance, homogénéité des honnêtes, autre nommée), sa statistique de diagnostic, la statistique qui la relâche [à trancher par Lazar] ; (e) un classifieur de provenance appris sur les honnêtes de chaque famille reste au hasard ; (f) unités, puissance selon le nombre de familles, coût ; (g) part sans dépense (simulation, données publiques) et part sur devis.
Facultatifs [à trancher par Lazar] : familles publiées en plus (six de transfert d'HELIOS, autres du dossier), ordonnées par distance ; statistique d'universalité rapportée, non décisive (rapport de puissance hors et en distribution, ou pente contre la distance).

## Axe 5 — Statistiques par la théorie
Obligatoires : (a) objets, hypothèses numérotées, conclusion quantifiée (horizon, divergence par action, dose, hétérogénéité des honnêtes, nombre d'agents) ; (b) preuve dans Lean, ou simulation préenregistrée (graines par SeedSequence, forme de courbe prédite) ; (c) une hypothèse violée et ce que devient la conclusion ; (d) statistique exclue et statistique recommandée ; (e) quantité mesurable qui dit si l'hypothèse tient ; (f) l'apport face aux bornes classiques de délai de détection, citées.

## Axe 7 — Angles d'approche non occupés, sur tout le contrôle
Hors des deux questions financées (menace étalée dans le temps ; surveillant détourné), les angles que ce programme peut prendre par ce qu'il est (L). Quatre angles au plus, dans trois cases au moins de la grille, dont une au plus déjà couverte [à trancher par Lazar]. Obligatoires : (a) angle et question falsifiable, deux issues ; (b) case ; (c) **table de substitution** contre l'énoncé existant le plus proche (huit questions, pièce C ; fronts, pièce A) : objet mesuré, unités et population, métrique, comparateur ; deux colonnes au moins différentes, sinon reformulation ; (d) pourquoi libre : antériorité la plus proche, « absent du dossier » (jamais « libre dans le domaine »), occupant qui l'annonce en travail futur, trois requêtes exactes ; (e) ajout aux deux questions, coût (instruments, calcul, semaines, abandons) ; (f) source dans L ; (g) première expérience qui le tue, valeur qui tue. Un angle qui exige de produire de nouvelles lois déplacées n'est pas noté. Un programme compare d'abord chaque angle aux huit questions (bardeaux de mots) [à trancher par Lazar].

## Boucle entre générations [à trancher par Lazar]
Chaque fiche porte un **vis-à-vis** : un angle ou une statistique (axes 1, 2, 4, 5, 7) nomme la faille de l'axe 3 qu'il exploite ou expose (identifiant ou classe) ; une faille (axe 3) nomme l'angle ou la statistique qu'elle ouvre. Le juge vérifie présence et appartenance ; vide permis en génération 1 seulement (sinon K1 échoue). La génération g+1 reçoit les fiches scellées anonymes de g, verdict et classement ; étiquette d'héritage (neuve, affine X, réfute X) ; une « affine » qui ne change ni statistique, ni couches, ni borne, ni seuil est refusée. Consignés par génération : part de notables, angles et failles neufs, nouveauté des sources, distance entre passes. Arrêt proposé, scellé seulement s'il est relu scellable : deux générations sans angle ni faille neufs. Chaque génération : devis et GO.

## Critère de mort de la course
La course n'a rien donné si : moins de trois des six axes ont une fiche notable ; ou, après vérification sur PDF, aucune notable ne garde son élément inédit ni sa source d'avantage ; ou toutes reformulent les huit questions ; ou aucune ne devient un préenregistrement scellable ; ou le témoin planté échoue [à trancher par Lazar]. Réserves de symétrie : tables des écarts contradictoires ; presque tout notable.

## Pièces (liste fermée)
A programme vulgarisé v10 ; B lecture d'HELIOS et avis d'emprunt ; C question servie et huit questions ; 23 papiers ; listes L, M, D ; grille ; code du juge figé ; simulateur figé ; chiffres de P3 ; lentilles ; pages 18 et 27 d'HELIOS. Rien d'autre.
<!-- FIN-TEXTE-SERVI -->

---

## Annexe 1 — Pièce L-M-D proposée (servie comme pièce, hors du compte ; à arrêter par Lazar)

- **L, sources d'avantage (fermée)** [ON, élargie par ON-axe 7] : organisme (juge figé à borne de fausses promotions ; témoins plantés ;
  mémoire qui refuse les redites ; tâches fraîches ; épreuve lue une fois) ; programme (menaces diffuses ; boîte blanche sur poids ouverts
  8 et 70 milliards ; familles tenues à l'écart par une instance qui n'a conçu aucune statistique ; théorie des angles morts) ; méthodes
  (préenregistrement scellé ; contre-lecture par un modèle différent ; verdict par sous-agent neuf ; troisième instance) ; raisons
  structurelles (« les occupants construisent l'agent déviant » ; « ils évaluent la statistique finale, non la boucle » ; « ils ne scellent
  pas d'avance »). Une source hors liste ne passe pas K2 par la première branche ; elle est consignée « source nouvelle, à instruire ».
- **M, métriques** [ON] : rappel à 1 % de fausses alertes par famille ; écart de fausses alertes sur honnêtes ; aire (rapportée, jamais
  seule) ; latence relative au pas où l'écart cumulé atteint θ ; borne basse valide à tout instant ; e-valeur arrêtée ; coût ; taux de
  prédictions justes contre le hasard.
- **D, données réclamables** [ON ; CA pour « identifiants scellés »] : D1 trajectoires synthétiques du simulateur figé (graines par
  SeedSequence) ; D2 données publiques tierces (récupération = nœud) ; D3 les 180 notations brutes des juges, après scellement de la
  consigne du second examen ; D4 tranche exploratoire tirée par une instance tierce, identifiants scellés, déclarée brûlée au registre de
  fraîcheur du juge figé, scores et résidus seulement, jamais de directions ni de textes. Hors D : tout le reste.
- **Grille des sous-domaines** (proposition d'ON, non vérifiée, à arrêter par Lazar) : détection et surveillance ; protocoles de contrôle ;
  surveillance par un modèle non fiable et collusion ; élicitation et sous-performance volontaire ; conscience d'évaluation ; lisibilité
  des chaînes de raisonnement ; audit par interprétabilité ; supervision extensible et débat ; organismes modèles ; délégation et systèmes
  multi-agents ; recherche automatisée ; science de l'évaluation ; argumentaires de sûreté ; facteurs humains de l'audit. Cases « déjà
  couvertes » : menaces diffuses, co-évolution, essaim, surveillant détourné.

## Annexe 2 — Provenance (étiquettes retirées du texte servi)

[CA] conv-audit v1 et complément d'axe 7 ; [ON] Opus neuf v1 et complément ; [SD] `question-course-2-v1.md` (pistes A, B, C) ;
[AR] Argon, lu à côté, jamais compté ; [L] contrainte de Lazar ; [v0] brouillon de fusion v0 (lignée conv-audit, non compté).

| Bloc du texte servi | Provenance | Statut (recoupement) |
|---|---|---|
| Glossaire | SD (glossaire) ; L | imposé |
| Repères d'HELIOS | CA, ON, SD ; revérifiés sur pièce B | commun |
| Règles (niveau méthode, citations, SUPPOSÉ, liste D, interdits) | CA, ON, SD ; règle gelée du programme pour les jetons | commun ; directions exclues : D9 |
| Fiche : noyau | CA, ON, SD | commun ; longueur et nombre : D10 |
| K1, K3 | CA, ON, SD | commun |
| K2 | ON ; L (listes fermées) | tranché par L |
| K4 | ON, SD (seuil) ; CA, SD / ON (budget) | commun (seuil) ; D3 (budget) |
| K5 | CA, ON, SD (format) ; ON (contrôle par programme) | commun ; D10 |
| Classement ; témoin planté | ON ; L | D8 ; imposé |
| Passe 2 ; sous-session de l'axe 7 | ON | D2 ; D1 |
| Axe 1 (a), (b), plancher, comparateur, matériau | CA, ON, SD | commun |
| Axe 1 sonde nulle, lecture d'HELIOS, couches, hyperparamètres | ON ; CA (lecture d'HELIOS) | D4 |
| Axe 1 (d) invariance ; facultatifs | SD ; ON ; CA (gradué) | D10 ; D4 |
| Axe 2 (a), (d) | CA, ON | commun ; (b) ON, (c) CA : D10 |
| Axe 3 mesure à seuil, riposte, coût | CA, ON, SD | commun |
| Axe 3 pré-mortem, ordre, percutant | SD ; L | imposé |
| Axe 3 phrase citée, classe fermée, classe formelle | ON ; ON + SD ; SD | D10 ; tranché par L |
| Axe 4 (a), (b), (c), (f) | CA, ON, SD | commun |
| Axe 4 (d) d'avance ; (e) ; (g) | ON ; ON ; SD réécrit | D5 ; D10 ; réécrit (circulaire tel quel) |
| Axe 4 facultatifs | SD | D6 |
| Axe 5 (a), (b), (d), (e) | CA, ON, SD | commun |
| Axe 5 (c), (f) | ON | D10 (facultatifs d'ON retirés pour la taille) |
| Axe 7 (a), (d) en partie, (e), (g), non-production | CA, ON | commun |
| Axe 7 grille, cases, table de substitution, bardeaux | ON ; CA (réécrit) | D11 ; D7 |
| Boucle | v0, AR ; L | D12 (aucun répondant compté) |
| Critère de mort | CA, ON | D13 |
| Pièces | CA, ON, SD | commun ; pièces G, H, I de SD : D10 |

## Annexe 3 — Consignes de l'orchestrateur, hors texte servi (retirées pour la taille ou parce qu'elles ne s'adressent pas aux proposeurs)

- Axe 7, après la course [CA, ON ; seconde recherche : ON] : aucun angle n'entre dans une note de décision sans deux recherches
  d'antériorité sur PDF empreintés : un sous-agent neuf avec recherche (ni auteur, ni juge), puis une recherche adverse par un modèle d'un
  autre fournisseur chargé de trouver l'occupant ; « non trouvé par la moisson (sources, date) » n'est jamais « vierge » (R8).
- Contrôles par programme avant le juge [ON] : pages des chiffres d'HELIOS contre la pièce B ; appartenance des données à D ; répartition
  des angles par cases ; bardeaux de mots contre les huit questions [CA].
- Garde de forme (règle « niveau méthode ») testée sur un cas sain et sur un artefact avant la course (R5, règle gelée du programme).
- Vérification hors du programme [CA, ON] : reproduction tierce depuis la copie publique ; banc d'HELIOS quand son dépôt est obtenu
  (récupération = nœud) ; logiciel de preuve ; un statisticien extérieur [ON] seulement par contact rédigé et envoyé par Lazar.
- Retirés du texte pour la taille, à réintroduire si la remesure le permet : facultatifs de l'axe 5 [ON] (boîte noire contre blanche ;
  procédure qui atteint la borne) ; liste longue de matériau de l'axe 1 [CA, ON, SD].
