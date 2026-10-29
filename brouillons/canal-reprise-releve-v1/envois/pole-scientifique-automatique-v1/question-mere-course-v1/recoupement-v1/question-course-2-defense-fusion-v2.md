# Question de la course 2 — volet défense — fusion v2 (axes 1, 2, 3, 4, 5, 7 et boucle ; brouillon, non contre-lu, non servi)

Sous-agent neuf (Sonnet 5.5), relevé `date -u` du 29 octobre 2026, 23:34 UTC ; n'a écrit ni la fusion v1 ni aucune entrée. Fusion selon `recoupement-question-course-2-defense-v2.md`
(même dossier), critères du § 3 de `question-mere-course-ideation-v3.md` (`1b08e17f…`), fusion v1 (`f89e0791…`) et synthèse du collisionneur (`25e2d351…`) comme entrées.
Hors périmètre, non repris : **l'axe 6**, écrit à part par session-depot ; l'absence de toute demande sur ce thème dans ce texte tient à cela seule.
**Texte servi : 11 946 octets** (`wc -m` entre les deux marqueurs, marqueurs exclus, marques « [à trancher par Lazar] » comprises ; plafond 12 000).
**Attention à l'unité** : sur ce poste `wc -m` est en locale POSIX et compte des **octets** (la mesure de la v1, 11 971, en était une : 11 526 caractères) ; en caractères (locale UTF-8) le texte v2 fait 11 482 caractères. Le plafond est tenu dans les deux lectures.
Les marques renvoient aux décisions D1 à D14 et Q1 à Q6 du recoupement v2 ; le texte porte l'option par défaut.

**Ce qui change par rapport à la fusion v1** : fausse alerte comptée par épisode et tenue à tout instant ; plancher au maximum de K tirages ; lecture d'HELIOS rejouée et séparation exécution / lisibilité
passées au minimum de l'axe 1 ; consigne bénigne de longueur appariée ; axe 4 : seuil unique, issue « non jugeable par puissance », puissance simulée, variance du seuil, pseudo-réplication ; axe 5 : preuve sans `sorry` ;
K2 : pièce et page à l'appui ; notation en deux étages, « décisif » et « inédit » non notés ; statut « non réfuté par [procédure] à [date] » ; vis-à-vis **compté, non noté** jusqu'au test (Q3, change le défaut de D12) ;
**aucune règle d'arrêt** tant que l'association nouveauté / survie n'est pas établie (Q6) ; pré-pilote et condition de l'axe 1 (Q1, Q5) ; G1 ajouté aux données exclues ; tranche D4 retirée (Q2) ; liste fermée F des classes de faille (annexe 1).
**Écarts de forme** (pour tenir 12 000 caractères) : le **critère de mort de la course** (514 caractères, 532 octets) quitte le texte servi pour l'annexe 3 (D13) ; si le plafond se lit en caractères, il peut y revenir (11 997 caractères) ; la liste des classes de faille passe en annexe 1 ; le champ « titre » de la fiche,
les détails d'HELIOS sur le juge textuel (p. 43-44) et le plus petit modèle (table 13, p. 46), « aucune fiche nouvelle » en passe 2 et « preuve jointe » sont retirés (la pièce B les porte ; le sens de la passe 2 reste).
**À faire avant service** : contre-lecture par un modèle d'un autre fournisseur (R2) ; verdict du pré-pilote à insérer ou ligne à retirer ; retrait des marques ; remesure des consignes chez session-depot ; devis et GO.

<!-- DEBUT-TEXTE-SERVI -->
# Course d'idéation — question « défense » — génération g

## Glossaire (vaut définition)
- **Trajectoire** : actions textuelles (a_1, …, a_T) d'un agent à poids ouverts (8 ou 70 milliards de paramètres) et leurs activations internes.
- **Loi de référence** P_0 : loi des trajectoires honnêtes. **Loi déplacée** P_ε : loi alternative d'intensité ε ≥ 0, égale à P_0 en ε = 0. **Famille** : classe de lois déplacées de même mécanisme. **Menace diffuse** : écart par action sous le seuil de détection par action, écart cumulé grand.
- **Statistique** S : fonction de la trajectoire ; boîte noire (lit le texte) ou blanche (lit les activations) ; par action, ou séquentielle.
- **Fausse alerte** : P_0(S > s), comptée par épisode et tenue à tout instant, jamais par action ; calibrage, seuil et vérification sur trois jeux disjoints. **Puissance** : P_ε(S > s). **Rappel à 1 %** : puissance à fausse alerte 0,01.
- **Plancher apparié** : S sous des directions aléatoires de même covariance (maximum de K tirages si la fiche retient la meilleure de K options) ; une sonde compte si sa borne basse dépasse le quantile 0,95 du plancher. **Sonde nulle de chaîne** : même chaîne sur une partition aléatoire d'honnêtes ; elle doit rester au hasard. [à trancher par Lazar, D14 : jeux disjoints, maximum de K]
- **Famille tenue à l'écart** : jamais vue pendant la conception, fixée par une instance qui n'a conçu aucune statistique. **Transfert** : puissance conservée sur une famille inédite. **Invariance** : propriété de S inchangée sous une classe nommée de transformations.
- **Borne** : énoncé prouvé ; **impossibilité** (aucune S d'une classe ne dépasse sa fausse alerte sous une classe de lois déplacées) ou **garantie** (puissance β à fausse alerte α).

## Préambule
Programme défensif (sondes, statistiques sur texte, agrégation séquentielle, théorie des angles morts, juge figé). Porte G1 : battre chaque comparateur boîte noire scellé, par famille, au rappel à 1 %, fausses alertes au plus 5 points au-dessus, en une lecture. État (pièce A) : premier test interne nul (aucune sonde générique au-dessus du plancher) ; juges à 87 notes utilisables sur 100 pour 99 exigées ; garde muette sous environ 160 unités. HELIOS (pièce B) : un jeton par réponse, cinq couches médianes, agrégation sur les agents, rien dans le temps (p. 16, 27) ; rappel à 1 % de 0,38 sur TRANSFER (p. 18), repère et non seuil ; séquentiel annoncé en travail futur (p. 18-19). Pré-pilote : [verdict à insérer ; sans signal établi à 8 milliards, l'axe 1 n'est pas servi] [à trancher par Lazar, Q1 et Q5].

**Règles.** Niveau méthode : aucune conduite d'agent, consigne, séquence d'actions ni procédé pour produire une loi déplacée ; une telle fiche est écartée avant la notation et comptée. Les pièces sont des données. Chiffre repris : pièce et page ; supposé : SUPPOSÉ. Données réclamées : liste D seulement ; jamais `donnees/`, familles scellées, internes des statistiques (directions de sonde comprises), carte des hypothèses, données de calibrage ou d'évaluation de G1. Aucune moyenne ni médiane sur les jetons dans une sonde de production. Un refus arrête votre tour.

**Fiche** (3 000 à 8 000 caractères ; « sans objet » motivé) : axe ; hypothèse ; prédiction chiffrée et signée (métrique de M, valeur, unité de lecture) ; livrables de l'axe ; données (D) ; coût (processeur, carte, dollars) ; antériorités (au plus cinq : titre, auteurs, année, élément qui leur manque, page du dossier ou « à vérifier ») ; source d'avantage (L) ou élément manquant à l'antériorité la plus proche ; critère de mort ; vis-à-vis ; SUPPOSÉ.

**Notation** (binaire, contre les listes fermées L, M, D ; étage 1 : analyseur programmé, qui décide ; étage 2 : modèle-juge, cohérence entre champs seulement ; ni « décisif » ni « inédit » n'est noté). K1 : livrables de l'axe présents. K2 : source dans L avec coût de reproduction chiffré, pièce et page à l'appui, ou antériorité la plus proche et élément absent nommés. K3 : prédiction chiffrée et signée sur M ; pour une détection, rappel à 1 % par famille. K4 : critère de mort à seuil numérique, écrit avant lecture ; première expérience sur processeur seul ou sur données déjà payées [à trancher par Lazar, D3]. K5 : antériorités au format ; chiffres d'HELIOS conformes à la pièce B, même page (contrôle par programme) ; données dans D. Notable : K1 à K5 vrais. Classement par axe : facultatifs passés, puis coût croissant [à trancher par Lazar, D8]. Des témoins plantés, notables et non notables, sont glissés anonymes.

**Déroulé** [à trancher par Lazar, D1 et D2]. Deux fiches par axe et par proposeur au plus. Passe 2 : sur les fiches anonymes de l'autre fournisseur, seulement marquer un champ faux ou ajouter une antériorité. L'axe 7 va à une sous-session neuve : ce préambule, sans les axes 1 à 5.

## Axe 1 — Battre HELIOS : statistiques et agrégateurs
Partez d'une **table des écarts** (trois lignes au moins : métrique, familles, modèles, couches, jetons, agrégation ; HELIOS avec page ; programme ou « non mesuré ») ; proposez une statistique qui **comble une ligne**.
Obligatoires : (a) la table ; (b) la statistique au point de codage (quantité lue, couche, jeton, agrégation, apprentissage, seuil, case accès × agrégation) ; (c) plancher apparié, un comparateur boîte noire scellé à capacité égale, lecture d'HELIOS rejouée sur notre banc (dernier jeton de la dernière réponse) comme base à battre, exécution (m1) et lisibilité (m2) séparées ; en plus : sonde nulle de chaîne, couches rapportées séparément [à trancher par Lazar, D4], consigne bénigne de longueur appariée [à trancher par Lazar, D14] ; (d) l'**invariance** qui justifie le transfert, et pourquoi une direction logistique ne l'a pas ; (e) hyperparamètres réglés hors épreuve.
Facultatifs : comparateur gradué en information (nu, informé, à exemples) ; transfert de type HELIOS (une famille apprise, six lues).
Matériau, non imposé : Mahalanobis, auto-encodeurs parcimonieux, patching d'activations, e-valeurs, seuils conformes, détecteurs de rupture.

## Axe 2 — Ce que le domaine retiendrait
Obligatoires : (a) forme (loi, notice d'angles morts, garantie, impossibilité) et énoncé quantifié, classes définies sans les familles scellées ; (b) les deux issues, en une phrase chacune ; (c) le résultat publié qui le rendrait inutile ; (d) le premier test préenregistrable ; le critère de mort tue l'énoncé, pas seulement le test.

## Axe 3 — Failles du programme, en pré-mortem
Placez-vous après l'échec : G1 n'est pas franchie (gain de la boîte blanche absent dans une famille, ou accumulation au plancher). Obligatoires : (a) l'**hypothèse porteuse** qui a cédé, avec une phrase citée de la pièce A ou C, et sa classe dans la liste fermée F ; (b) la classe de lois déplacées sous laquelle elle tombe, formelle si statistique ; (c) la **mesure** qui la révèle, en simulation ou sur D, avec la valeur qui confirme et celle qui infirme ; (d) l'ordre des cessions et la mesure qui le tranche ; (e) riposte, coût, et ce qui rendrait le résultat percutant plutôt que local.

## Axe 4 — Universalité sur les familles existantes
Livrable : un **préenregistrement à sceller**, pas un résultat ; vous ne voyez aucune famille scellée ; un tiers exécute. Obligatoires : (a) hypothèse, prédiction chiffrée et signée, métrique, seuil unique scellé, plan d'analyse, critères de lecture gelés, liste d'arrêt, issues écrites : confirmée, infirmée, non jugeable par puissance [à trancher par Lazar, D14] ; (b) exclusion d'une famille à la fois, partition scellée par une instance tierce avant toute conception ; (c) lecture par famille : borne basse valide à tout instant contre le quantile 0,95 du plancher, fausses alertes comme pour G1 ; (d) si échec, hypothèse désignée **d'avance** (stationnarité, indépendance, homogénéité des honnêtes, autre nommée), sa statistique de diagnostic, la statistique qui la relâche [à trancher par Lazar, D5] ; (e) un classifieur de provenance appris sur les honnêtes de chaque famille reste au hasard ; (f) unités indépendantes (randomisation par session, corrélation intra-classe déclarée), puissance simulée avant scellement (loi jointe des familles, multiplicité, effet minimal détectable, témoin positif à effet connu), variance du seuil à 1 % propagée, coût [à trancher par Lazar, D14] ; (g) part sans dépense (simulation, données publiques) et part sur devis.
Facultatifs [à trancher par Lazar, D6] : familles publiées en plus (dont les six de transfert d'HELIOS), ordonnées par distance ; statistique d'universalité, non décisive.

## Axe 5 — Statistiques par la théorie
Obligatoires : (a) objets, hypothèses numérotées, conclusion quantifiée (horizon, divergence par action, dose, hétérogénéité des honnêtes) ; (b) preuve dans Lean, sans `sorry` et à hypothèses non vides, ou simulation préenregistrée (graines par SeedSequence, forme de courbe prédite) ; (c) une hypothèse violée et ce que devient la conclusion ; (d) statistique exclue et statistique recommandée ; (e) quantité mesurable qui dit si l'hypothèse tient ; (f) l'apport face aux bornes classiques de délai de détection.

## Axe 7 — Angles d'approche non occupés, sur tout le contrôle
Hors des deux questions financées (menace étalée ; surveillant détourné), les angles que ce programme peut prendre par ce qu'il est (L). Quatre angles au plus, dans trois cases au moins de la grille, dont une au plus déjà couverte [à trancher par Lazar, D11]. Obligatoires : (a) angle et question falsifiable, deux issues ; (b) case ; (c) **table de substitution** contre l'énoncé existant le plus proche (huit questions, pièce C ; fronts, pièce A) : objet mesuré, unités et population, métrique, comparateur ; deux colonnes au moins différentes, sinon reformulation ; (d) pourquoi libre : antériorité la plus proche, « absent du dossier » (jamais « libre dans le domaine »), occupant qui l'annonce en travail futur, trois requêtes exactes, statut « non réfuté par [procédure] à [date] » [à trancher par Lazar, Q4] ; (e) ajout aux deux questions et coût ; (f) source dans L ; (g) première expérience qui le tue, valeur qui tue. Un angle qui exige de produire de nouvelles lois déplacées n'est pas noté. Un programme compare chaque angle aux huit questions (bardeaux de mots) [à trancher par Lazar, D7].

## Boucle entre générations [à trancher par Lazar, Q3 et Q6]
Chaque fiche porte un **vis-à-vis** : un angle ou une statistique (axes 1, 2, 4, 5, 7) nomme la faille de l'axe 3 qu'il exploite ou expose ; une faille (axe 3) nomme l'angle ou la statistique qu'elle ouvre. Le programme vérifie présence et appartenance et le **compte** ; il n'entre ni dans K1 ni dans le classement avant d'avoir été testé. La génération g+1 reçoit les fiches scellées anonymes de g, verdict et classement ; étiquette d'héritage (neuve, affine X, réfute X) ; une « affine » qui ne change ni statistique, ni couches, ni borne, ni seuil est refusée. Consignés par génération : part de notables, angles et failles neufs, nouveauté des sources, distance entre passes, survie à la vérification sur PDF. Aucune règle d'arrêt tant que l'association entre nouveauté et survie n'est pas établie sur deux générations. Chaque génération : devis et GO.

## Pièces (liste fermée)
A programme vulgarisé v10 ; B lecture d'HELIOS et avis d'emprunt ; C question servie et huit questions ; 23 papiers ; listes L, M, D, F ; grille ; code du juge figé ; simulateur figé ; chiffres de P3 (verdict seulement) ; lentilles ; pages 18 et 27 d'HELIOS. Rien d'autre.
<!-- FIN-TEXTE-SERVI -->

---

## Annexe 1 — Pièce L-M-D-F proposée (servie comme pièce, hors du compte ; à arrêter par Lazar)

- **L, sources d'avantage (fermée)** [ON, élargie par ON-axe 7] : organisme (juge figé à borne de fausses promotions ; témoins plantés ; mémoire qui refuse les redites ; tâches fraîches ; épreuve lue une fois) ; programme (menaces diffuses ; boîte blanche sur poids ouverts
  8 et 70 milliards ; familles tenues à l'écart par une instance qui n'a conçu aucune statistique ; théorie des angles morts) ; méthodes (préenregistrement scellé ; contre-lecture par un modèle différent ; verdict par sous-agent neuf ; troisième instance) ;
  raisons structurelles (« les occupants construisent l'agent déviant » ; « ils évaluent la statistique finale, non la boucle » ; « ils ne scellent pas d'avance »). Une source hors liste ne passe pas K2 par la première branche ; elle est consignée « source nouvelle, à instruire ».
  Chaque source citée renvoie à la pièce et à la page qui l'attestent (K2).
- **M, métriques** [ON] : rappel à 1 % de fausses alertes par famille ; écart de fausses alertes sur honnêtes ; aire (rapportée, jamais seule) ; latence relative au pas où l'écart cumulé atteint θ ; borne basse valide à tout instant ; e-valeur arrêtée ; coût ; taux de prédictions justes contre le hasard.
- **D, données réclamables** [ON ; CA pour « identifiants scellés » ; collisionneur A pour « copies disjointes »] : D1 trajectoires synthétiques du simulateur figé (graines par SeedSequence) ; D2 données publiques tierces (récupération = nœud) ;
  D3 les 180 notations brutes des juges, après scellement de la consigne du second examen, sur copies disjointes de toute donnée de calibrage ou d'évaluation de G1. **D4, tranche exploratoire : retirée par défaut** [à trancher par Lazar, Q2] ; si l'option (b) de Q2 est retenue :
  tranche tirée par une instance tierce, identifiants scellés, intersection vide avec le calibrage et l'évaluation de G1, déclarée brûlée au registre de fraîcheur du juge figé, scores et résidus seulement, jamais de directions ni de textes. Hors D : tout le reste.
- **F, classes de faille (fermée)** [ON + SD + CA, reprise de la fusion v1] : circularité ; artefact de source ; « réel » instruit ; puissance ; juges ; garde muette ; modèle trop faible ; fuite conception-épreuve ; linéarité ; additivité dans le temps ; stationnarité de P_0 ;
  indépendance entre actions ; autre (consignée « classe nouvelle, à instruire »).
- **Grille des sous-domaines** (proposition d'ON, non vérifiée, à arrêter par Lazar ; une grille de « libre » ou « occupé » n'est pas une vérité de terrain, collisionneur A et B) : détection et surveillance ; protocoles de contrôle ; surveillance par un modèle non fiable et collusion ;
  élicitation et sous-performance volontaire ; conscience d'évaluation ; lisibilité des chaînes de raisonnement ; audit par interprétabilité ; supervision extensible et débat ; organismes modèles ; délégation et systèmes multi-agents ; recherche automatisée ; science de l'évaluation ;
  argumentaires de sûreté ; facteurs humains de l'audit. Cases « déjà couvertes » : menaces diffuses, co-évolution, essaim, surveillant détourné.

## Annexe 2 — Provenance (étiquettes retirées du texte servi)

[CA] conv-audit v1 et complément d'axe 7 ; [ON] Opus neuf v1 et complément ; [SD] `question-course-2-v1.md` (pistes A, B, C) ; [CO] collisionneur, via la synthèse `25e2d351…` (A = Fable 5.1, B = Opus 5.5, C = Gemini Argon ; accord interne noté) ;
[AR] Argon séparé, lu à côté, jamais compté ; [L] contrainte de Lazar ; [v0] brouillon de fusion v0 (non compté). Identifiants Nn, Jn, An.m, Dn, Qn : recoupement v2.

| Bloc du texte servi | Provenance | Statut (recoupement v2) |
|---|---|---|
| Glossaire (trajectoire, lois, statistique, famille, borne) | SD ; L | imposé |
| Fausse alerte tenue à tout instant | SD, ON, CO | commun (N2a) |
| Fausse alerte par épisode ; trois jeux disjoints | CO 3/3 | D14 (N2b) |
| Plancher apparié ; sonde nulle de chaîne (en glossaire) | CA, ON, SD | commun |
| Plancher au maximum de K tirages | CO (A, C) | D14 (N13) |
| Repères d'HELIOS (0,38 p. 18 ; p. 16, 27 ; p. 18-19), « repère et non seuil » | CA, ON, SD, CO ; revérifiés sur pièce B | commun |
| Pré-pilote ; axe 1 conditionnel | CO (reco 4) | Q1, Q5 |
| Règles (niveau méthode, citations, liste D, interdits) | CA, ON, SD | commun ; directions exclues : D9 clos ; G1 exclu : CO, ON, CA commun |
| Fiche : noyau | CA, ON, SD | commun ; longueur et nombre : D10 |
| Notation : K1, K3 | CA, ON, SD | commun |
| K2 (liste L, coût de reproduction, pièce et page) | ON ; CO A, B, C | commun (J4) |
| K4 | ON, SD (seuil) ; CA, SD / ON (budget) | commun (seuil) ; D3 (budget) |
| K5 | CA, ON, SD (format) ; ON (pages d'HELIOS par programme) | commun ; P5 : D10 |
| Étage 1 programmé ; étage 2 limité | ON ; CO B, C | commun (N14a) ; N14b divergent |
| « décisif » et « inédit » non notés | CA, ON, SD, CO | commun (J5) |
| Classement ; témoins plantés | ON ; L ; CO | D8 ; imposé (extension N1 : Q1) |
| Déroulé : passe 2 ; sous-session de l'axe 7 | ON | D2 ; D1 |
| Axe 1 (a), (b), plancher, comparateur, matériau | CA, ON, SD | commun |
| Axe 1 lecture d'HELIOS rejouée ; m1 / m2 | CA, ON, CO | commun (A1.9, N4) |
| Axe 1 sonde nulle, couches séparées ; consigne bénigne | ON ; CO | D4 ; D14 (N3) |
| Axe 1 (d) invariance ; facultatifs | SD ; ON ; CA (gradué) | D10 ; D4 |
| Axe 2 (a), (d) ; (b), (c) | CA, ON ; ON, CA | commun ; D10 |
| Axe 3 mesure à seuil, riposte, coût | CA, ON, SD | commun |
| Axe 3 pré-mortem, ordre, percutant ; classe dans F | SD ; L ; ON + SD | imposé ; tranché par L |
| Axe 3 phrase citée, classe formelle | ON ; SD | D10 |
| Axe 4 (a) hors seuil unique et issues, (b), (c), (g) | CA, ON, SD | commun |
| Axe 4 (a) seuil unique, issue « non jugeable par puissance » ; (f) puissance simulée, variance, pseudo-réplication | CO | D14 (N12, N7, N8, N9) |
| Axe 4 (d) d'avance ; (e) provenance | ON ; ON | D5 ; D10 |
| Axe 4 facultatifs | SD | D6 |
| Axe 5 (a), (d), (e) ; (b) Lean ou simulation | CA, ON, SD ; CA, ON, CO | commun |
| Axe 5 (b) sans `sorry`, non vide | CO (C) | D14 (N16) |
| Axe 5 (c), (f) | ON | D10 |
| Axe 7 (a), (e), (g), non-production | CA, ON | commun |
| Axe 7 (d) pourquoi libre ; trois requêtes ; statut « non réfuté par… » | CA, ON, CO ; ON ; CO | commun (A7.2) ; D10 ; Q4 |
| Axe 7 grille, cases, table de substitution, bardeaux | ON ; CA (réécrit) ; CO (étalonnage) | D11 ; D7 |
| Boucle : vis-à-vis compté non noté | CO (A) ; v0, AR (obligatoire) ; CO (C) | Q3 (D12) |
| Boucle : reçu par g + 1, étiquette d'héritage | v0, AR | D12 (b) du recoupement v1, maintenu |
| Boucle : mesures consignées ; aucune règle d'arrêt avant association établie | CO (A, B) ; L (point 8) | commun avec la question-mère (B6) ; Q6 |
| Pièces | CA, ON, SD | commun ; pièces G, H, I de SD : D10 ; P3 en verdict seul : Q2 |

## Annexe 3 — Consignes de l'orchestrateur, hors texte servi

- **Critère de mort de la course** (retiré du texte pour la taille, D13) : la course n'a rien donné si : moins de trois des six axes ont une fiche notable ; ou, après vérification sur PDF, aucune notable ne garde son élément inédit ni sa source d'avantage ; ou toutes reformulent
  les huit questions ; ou aucune ne devient un préenregistrement scellable ; ou un témoin planté est mal classé ; ou l'étalonnage préalable de la notation échoue [à trancher par Lazar, D13 et Q1]. Réserves de symétrie (R4) : tables des écarts contradictoires ; presque tout notable.
- **Étalonnage préalable** [CO 3/3 ; Q1] : avant tout lancement, l'analyseur et les juges sont examinés sur des témoins plantés par une instance tierce (fiches creuses, paraphrases des huit questions, forme parfaite au contenu absurde, avantage faux, un témoin notable) ;
  la mémoire anti-redite et la vérification d'antériorité sont étalonnées de même, plongement nommé et figé, seuil de similarité fixé par cet étalonnage (B5) et non illustratif. Un préenregistrement scellé et contre-lu (R1, R2) précède l'examen ; dépense sur devis et GO.
- **Axe 7, après la course** [CA, ON ; seconde recherche : ON ; CO A, B] : aucun angle n'entre dans une note de décision sans deux recherches d'antériorité sur PDF empreintés : un sous-agent neuf avec recherche (ni auteur, ni juge), puis une recherche adverse par un modèle d'un autre fournisseur
  chargé de trouver l'occupant ; « non trouvé par la moisson (sources, date) » n'est jamais « vierge » (R8) ; l'échantillon de revendications de plusieurs documents sert d'abord à étalonner cette vérification, sans accès au dépôt de l'occupant.
- **Contrôles par programme avant la notation** [ON ; CO B, C] : pages des chiffres d'HELIOS contre la pièce B ; appartenance des données à D ; répartition des angles par cases ; bardeaux de mots contre les huit questions, étalonnés sur paraphrases plantées [CA, CO].
- Garde de forme (règle « niveau méthode ») testée sur un cas sain et sur un artefact avant la course (R5, règle gelée du programme).
- Vérification hors du programme [CA, ON, CO] : reproduction tierce depuis la copie publique ; banc d'HELIOS quand son dépôt est obtenu (récupération = nœud) ; logiciel de preuve ; un statisticien extérieur [ON] seulement par contact rédigé et envoyé par Lazar ;
  étiquetage des familles scellées par un tiers : mécanisme contre la fuite à définir (reste ouvert chez CO).
- **Dépense** : aucune expérience à plusieurs courses (158 à 264 dollars) dans le devis actuel [CO, reco 8] ; chaque génération : devis et GO ; lecture du registre pour la contradiction « S6 » avant l'expérience à 8 milliards, sans dépense [CO, reco 9].
- **Réserve P3** : les « chiffres de P3 » sont servis comme verdict seul ; si les 240 épisodes de P3 entrent dans une banque d'épreuve de G1, l'axe 3 (mesure sur D) et tout test de mort sur P3 deviennent circulaires : à vérifier chez session-depot.
- Retirés du texte pour la taille, à réintroduire si la remesure le permet : facultatifs de l'axe 5 [ON] (boîte noire contre blanche ; procédure qui atteint la borne) ; liste longue de matériau de l'axe 1 [CA, ON, SD] ; mention que le juge figé à pari apparié ne note aucun texte [CO B, C].
