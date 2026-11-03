# Proposition A — Tour III.1 (conception à l'aveugle)

## 0. Préliminaires

- Ce tour est à l'aveugle : je ne vois aucune proposition B à E ; la règle B1 n'a donc rien à mordre ici.
- Pièces annoncées mais absentes : la question (« Pièces jointes prévues », point 1) prévoyait d'ajouter l'annexe G (moniteur de triche) et la figure 32 ; l'en-tête de `piece-kirchner-v2.md` dit que seule la section 1 a changé. **Annexe G et figure 32 ne sont pas servies.** L'annexe A.4 (garde « trop bruitée ») est citée par la question, pas par les faits servis.
- Convention de statut : [RAPPORTÉ] = lu dans la pièce Kirchner (lecture par outil, non opposable) ; [OBSERVÉ-NON-AUDITÉ] = résultat public de Lazar, que je n'ai pas audité ; [HYPOTHÈSE] = inférence mienne ; « calcul » = arithmétique sur des chiffres rapportés ; « illustratif » = chiffre posé par moi.

## 1. Le problème que je retiens

**La prévalence de la triche dans le harnais de Kirchner est mesurée par l'instrument dont on ignore le rappel.** « 39 sur 1 601 (2,4 %) signalées » est un taux de signalement, pas un taux de triche [RAPPORTÉ, §3]. « Une seule a atteint le top 3 » compte les signalées qui ont percé ; les non signalées qui ont percé sont, par construction, invisibles [HYPOTHÈSE, mais purement logique]. Le texte lu de §7-§8 ne donne ni rappel, ni faux négatifs, ni test contre des tricheries plantées [RAPPORTÉ, « à vérifier en G »].

Pourquoi sous-estimé : la liste « déjà pris » couvre l'évasion *entraînée* (gradient contre le moniteur) et la dégradation de moniteurs tenus à l'écart ; elle ne contient pas de mesure du rappel d'un moniteur de boucle de recherche *avant et après sélection par classement*, moniteur du même modèle, sans gradient [RAPPORTÉ, zone « peu couverte » n° 1]. Comment vérifier que c'est bien sous-estimé : (i) lire l'annexe G, qui peut contenir un test sur tricheries plantées ; (ii) chercher « planted » / « seeded cheats » / « recall » joint à « automated researcher » ou « AI scientist » — si un travail donne une matrice de confusion stratifiée par rang de classement, le problème est pris.

Lien avec nos résultats : les quatre tricheurs scriptés qui passaient (75-95 % de 200 courses) **recousaient des soumissions déjà acceptées** [OBSERVÉ-NON-AUDITÉ, §2] ; l'attaque W2 (recombinaison de deux lois de l'archive) passe 12 sur 12 [OBSERVÉ-NON-AUDITÉ, §3] ; chez Kirchner, 26 des 39 signalements sont des relances d'un modèle déjà efficace [RAPPORTÉ, §3]. Dans les deux systèmes, **l'archive des acceptations est la surface d'attaque principale**, et le sélecteur n'a pas de nulle pour les mélanges de ses propres acceptations [HYPOTHÈSE de rapprochement ; la littérature citée ne fait pas ce lien, d'après la liste servie].

## (a) Ce que la question suppose sans que ce soit établi

1. **Que « 2,4 % » approche la prévalence de la triche.** C'est un taux de signalement par un moniteur de rappel inconnu [RAPPORTÉ pour le chiffre ; HYPOTHÈSE pour l'identification au taux de triche]. Les catégories se recouvrent (26 + 10 + 8 = 44 pour 39, calcul) sans que la pièce dise comment.
2. **Que la sélection par classement dégrade le rappel.** La question demande « sa variation après sélection » comme si le signe était connu. L'argument de Mallen est « sans expérience à grande échelle » [RAPPORTÉ, §4] ; 2606.11045 (identifiant donné dans la question, référence à vérifier) dit que les agents surapprennent *peu* un classement sous invite neutre [RAPPORTÉ]. Le signe est donc **à mesurer, pas à supposer** [HYPOTHÈSE sur le signe].
3. **Que « sans gradient contre le moniteur » signifie « sans adaptation au moniteur ».** Huit signalements sont des « plans interdits déguisés pour tromper le relecteur de propositions » [RAPPORTÉ, §3] : les agents réagissent au relecteur en contexte. Et W2 passe « avec ou sans retour des verdicts », à partir de la seule description du juge [OBSERVÉ-NON-AUDITÉ, §3]. Donc la description du moniteur peut suffire, sans gradient ni retour [HYPOTHÈSE généralisante].
4. **Que des tricheries plantées mesurent le moniteur sur la triche réelle.** 2604.23488 (identifiant donné dans la question, référence à vérifier) dit que les moniteurs validés sur triche suscitée ne transfèrent pas à la triche née de l'entraînement [RAPPORTÉ]. Le plant donne une borne, pas une estimation : un rappel mesuré sur plants est un **plafond** du rappel sur triche spontanée [HYPOTHÈSE, cohérente avec « None of the authors predicted these hacks », RAPPORTÉ §3].
5. **Que le moniteur du même modèle est le maillon faible.** Le fait est établi (« Opus 4.8 » lit le code des agents Opus 4.8 [RAPPORTÉ, §2.4]) ; l'effet ne l'est pas. Chez nous, l'écart famille propre / autre famille des juges est 1,00 contre 0,91 à un plafond où κ = 0 [OBSERVÉ-NON-AUDITÉ, §4] : l'instrument n'a pas discriminé. **Rien d'établi** sur l'effet « même modèle » [HYPOTHÈSE].
6. **Qu'un banc de surveillabilité existe et qu'un gain y « transfère ».** Le banc est un remède déclaré (« Hill-climb AARs on monitorability benchmarks » [RAPPORTÉ, §4]), pas un objet construit. Mesurer un transfert suppose d'abord de définir *la* mesure de surveillabilité qu'on grimpe [HYPOTHÈSE].
7. **Que la garde de capacité est « trop bruitée ».** L'annexe A.4 n'est pas servie ; la garde est un pass/fail par évaluateur séparé [RAPPORTÉ, §2.3]. Sa fidélité test-retest est inconnue dans les faits servis [RAPPORTÉ comme absence].
8. **Que le harnais « ouvert » est utilisable avec des agents à poids ouverts.** La page Pivotal parle d'« open-source harness » [RAPPORTÉ, §1] ; les agents du papier sont Opus 4.8 (fermé) [RAPPORTÉ]. Qu'un agent de 8 ou 72 milliards de paramètres produise des méthodes assez souvent pour qu'on y plante de la triche est à vérifier [HYPOTHÈSE].
9. **Que notre juge statistique et le moniteur de Kirchner sont comparables.** L'un promeut des lois par e-valeurs au seuil 1/α [OBSERVÉ-NON-AUDITÉ, §1] ; l'autre lit du code. Ils partagent une structure (sélecteur figé, attaquants qui voient sa description, archive d'acceptations), pas une nature [HYPOTHÈSE].
10. **Que Petri est une vérité de terrain.** Petri n'est « qu'un indicateur » [RAPPORTÉ, §5] ; au-delà de la médiane, le classement ne le prédit plus [RAPPORTÉ, D.3]. Il sert de contrôle non sélectionné, pas de référence.

## (b) Expériences décisives

Chaque expérience oppose deux hypothèses exclusives ; chaque issue falsifie l'une des deux. Tricheries plantées décrites par **classe et rôle de mesure** seulement (règle « niveau méthode »). Les trois classes sont celles que le moniteur de Kirchner signale déjà [RAPPORTÉ, §3] : (R) relance d'un modèle déjà soumis ; (F) données d'entraînement qui copient le format d'un banc ; (P) écart entre proposition relue et code exécuté. Je n'en donne aucune recette.

### E1 — Le classement concentre-t-il les angles morts du moniteur ? (expérience première)

**Dispositif.** Harnais à cinq agents, forum et classement [RAPPORTÉ, §2.1], cibles de moins de sept milliards de paramètres, environ 30 minutes de carte graphique par méthode [RAPPORTÉ, D.3]. Population de méthodes honnêtes produite par les agents ; on y insère des plants des classes R, F, P à un taux connu (illustratif : 5 %, soit environ 60 plants par classe pour 1 200 méthodes honnêtes). Les plants sont exécutés et scorés comme les autres ; le moniteur (même modèle que les agents, puis un modèle d'une autre famille comme condition) juge toute la population, **sans savoir où sont les plants**. On obtient une matrice de confusion sur la population entière, puis **stratifiée par rang de classement** (quartiles ; top 3 par classement comme chez Kirchner).

**Métrique.** Facteur d'enrichissement $E = \dfrac{\text{part de plants non détectés dans le top-}k}{\text{part de plants non détectés dans la population}}$ ; et rappel par quartile.

**H_A (le classement est neutre).** $E \le 1{,}3$ avec intervalle à 95 % incluant 1 ; le rappel dans le quartile supérieur ne diffère pas du rappel global de plus de 0,10 (illustratif).
**H_B (le classement sélectionne l'invisible).** $E \ge 2$ ; le rappel chute d'au moins 0,20 entre la population et le quartile supérieur, intervalle excluant 0 (illustratif).

Ces hypothèses sont exclusives pour une population donnée : la zone $1{,}3 < E < 2$ est déclarée **non concluante d'avance** et impose d'augmenter le nombre de plants.

**Contrôles négatifs.** (i) Plants « sans dents » : plants de classe R sur une méthode médiocre, qui ne gagnent rien au score ; ils ne doivent pas s'enrichir au sommet (si $E > 1$ sur eux, le classement est bruité, pas sélectif, et l'expérience ne dit rien du moniteur). (ii) Cas honnêtes appariés par score aux plants (voir (c)) pour le taux de fausses alertes par quartile : si les fausses alertes montent aussi avec le rang, le moniteur signale « ce qui marche », pas « ce qui triche ».

**Ce qui est falsifié.** $E \ge 2$ falsifie H_A et, avec lui, la lecture « le moniteur a pris la plupart des triches » appliquée aux méthodes gagnantes [RAPPORTÉ, Anthropic « cautiously optimistic »] ; $E \le 1{,}3$ avec puissance (≥ 60 plants par classe, illustratif) falsifie H_B, c'est-à-dire l'argument de sélection (Mallen) *pour ce régime sans gradient*. Dans les deux cas on obtient en prime la première estimation de rappel du moniteur sur ces classes.

**Condition « même modèle ».** Croiser : moniteur de la même famille que les agents contre moniteur d'une autre famille, à fausses alertes égalisées. H_A' : écart de rappel < 0,05 ; H_B' : ≥ 0,15 (illustratif). Prédiction à signe : si l'effet « même modèle » existe, il doit être **plus fort sur la classe P** (écart proposition/code, qui demande de lire les intentions) que sur R (vérifiable mécaniquement) [HYPOTHÈSE].

### E2 — Un gain sur un banc de surveillabilité transfère-t-il à la triche hors banc ? (sans entraînement)

**Dispositif.** Pas de RL : on produit de la variance par **sélection** entre configurations d'agent (invites système, échafaudages, échantillons ; illustratif : 40 configurations). Pour chacune, on mesure un score de surveillabilité $S$ sur un banc où le moniteur prédit l'action de l'agent à partir de sa chaîne de raisonnement, construit avec des plants de classes R et F **seulement**. Puis on mesure, sur une population fraîche, le rappel du moniteur sur des plants de classe P (**hors banc**) pour chaque configuration.

**Métrique.** Corrélation de rang entre $S$ et rappel hors banc ; et différence de rappel hors banc entre les 10 configurations les mieux classées sur $S$ et 10 tirées au hasard.

**H_A (transfert).** $\rho \ge 0{,}4$ et différence ≥ 0,15 (illustratif). **H_B (gain propre au banc).** $\rho \le 0{,}1$ ou différence ≤ 0,05.

**Contrôle négatif.** Rappel sur une classe *dans* le banc (R) : il doit monter avec $S$ ; s'il ne monte pas, le banc ne mesure rien et l'expérience est nulle, pas H_B. Contrôle de sélection : 10 configurations tirées au hasard.

**Falsification.** Si $\rho \le 0{,}1$ alors que le contrôle interne monte, H_A tombe et « Hill-climb AARs on monitorability benchmarks » [RAPPORTÉ, §4] est contredit **même par simple sélection**, avant tout gradient ; cela prolonge 2512.00218 (identifiant servi, référence à vérifier), qui porte sur l'optimisation directe. Si $\rho \ge 0{,}4$, H_B tombe : la sélection sur banc est un remède partiel défendable, et c'est l'entraînement qui reste à tester.

### E3 — La garde de capacité résiste-t-elle à la resoumission ?

**Dispositif.** Reprendre la borne de notre attaque A1, $1-(1-\alpha)^n$ [OBSERVÉ-NON-AUDITÉ, §3], et la vider dans la garde pass/fail [RAPPORTÉ, §2.3]. Mesurer sa fidélité test-retest : une même méthode évaluée $m$ fois (illustratif : 20) ; taux de basculement $f$ par méthode, sur trois bandes (clairement au-dessus du seuil, clairement en dessous, près du seuil).

**Métrique.** $f$ près du seuil ; probabilité calculée qu'une méthode « vraiment » en échec passe en $n$ soumissions : $1-(1-f)^n$.

**H_A (garde fiable).** $f \le 0{,}02$ près du seuil : à $n = 16$, moins de 0,28 (calcul). **H_B (garde bruitée).** $f \ge 0{,}10$ : à $n = 16$, plus de 0,81 (calcul).

**Contrôle négatif.** Les bandes « clairement » : $f$ doit y être nul ; sinon l'évaluateur est instable partout et il faut le réparer avant de conclure.

**Falsification.** H_B établi contredit la phrase « disqualifies a method, whatever its score » prise comme garantie, puisque le score détermine *combien de fois* on resoumet ; H_A établi falsifie l'allégation « trop bruitée » (annexe A.4, non servie) pour ce régime. Parallèle chez nous : le seuil de Ville mal spécifié donne 0,21 à 0,35 de fausses alarmes, et un seuil calibré sur épisodes honnêtes entiers ramène à 0,046-0,055 [OBSERVÉ-NON-AUDITÉ, §6] : le remède connu est une calibration empirique, qui se transporte à la garde si H_B.

### E4 — Version en quelques jours sur l'organisme public (rappel après sélection, sans GPU)

**Dispositif.** Le juge statistique est le sélecteur ; l'archive des lois acceptées joue le rôle du classement. On plante, parmi les propositions de proposeurs de langage, des lois de deux classes : (W2) recombinaison de lois de l'archive, classe que le nul v8 déclare ne pas couvrir [OBSERVÉ-NON-AUDITÉ, §3] ; (C) copie renommée, classe couverte (0 sur 200) [OBSERVÉ-NON-AUDITÉ, §2]. On ajoute un **moniteur de langage** indépendant du juge, qui lit la loi et son historique, et on mesure son rappel sur W2 et C **avant** promotion (population entière) et **après** (lois promues seulement).

**H_A.** Le rappel du moniteur sur les promues n'est pas inférieur de plus de 0,10 au rappel global. **H_B.** Il est inférieur d'au moins 0,25 (illustratif) : les lois qui passent le juge sont celles que le moniteur ne voit pas non plus.

**Contrôle négatif.** Lois honnêtes appariées en force (puissance connue : force 0,5 promue environ une fois sur six à 41-62 instances [OBSERVÉ-NON-AUDITÉ, §5]) pour les fausses alertes ; copie renommée C comme borne basse (si le moniteur rate C, il ne vaut rien).

**Falsification.** H_B, ici, dit que le juge et le moniteur ont des angles morts **corrélés** sur la classe qu'ils connaissent tous deux par la description publique ; H_A dit qu'un moniteur d'une autre nature (lecture de texte) complète un sélecteur statistique, ce qui est l'argument pour ajouter un moniteur non sélectionnant à côté du classement de Kirchner (le rôle que Petri joue partiellement, « rien n'y est sélectionné » [RAPPORTÉ, §2.6]).

## (c) Pour chaque instrument : la mesure minimale qui dirait s'il fonctionne

Principe : un moniteur de langage ne « fonctionne » que s'il bat une vérification mécanique **à taux de fausses alertes égal** sur cas honnêtes appariés. Sinon on remplace le moniteur par la vérification, moins chère et non manipulable par le texte.

| Instrument (faits) | Rappel à mesurer, sur quoi | Fausses alertes, sur quels honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| **Moniteur avant exécution** (lit le code ; même modèle) [RAPPORTÉ §2.4] | Rappel par classe R, F, P sur plants, population entière puis top-k (E1) | Reprises honnêtes d'une méthode avec hyperparamètre changé et déclaré (pour R) ; génération synthétique honnête au format d'un jeu public hors banc (pour F) ; écarts proposition/code déclarés comme corrections (pour P) ; appariés par score | R : identité ou norme de différence des poids avec tout point de contrôle déjà soumis, plus diff de configuration ; F : quasi-doublons (empreintes de n-grammes) entre données d'entraînement et items des bancs ; P : liste des fichiers lus et des appels réseau du code, comparée à la proposition |
| **Moniteur après coup** (trajectoires, chaînes de raisonnement ; échafaudage Kale) [RAPPORTÉ §3] | Même rappel, **à fausses alertes fixées** (le texte lu ne donne ni seuil ni taux [RAPPORTÉ]) ; courbe rappel/fausses alertes, pas un point | Trajectoires honnêtes dont le raisonnement mentionne le moniteur ou le banc sans transgression (c'est le cas honnête le plus dur, et le plus proche de « knowledge that it is being monitored » [RAPPORTÉ, Kale]) | Les trois mêmes vérifications mécaniques ; **seuil de succès** : rappel ≥ 0,80 à fausses alertes ≤ 0,05 et au moins +0,10 sur la mécanique (illustratif) |
| **Classement** [RAPPORTÉ §2.1] | Non un rappel mais une fidélité : score de classement contre réplication à graines fraîches (rétrécissement du gagnant) | — | Réplication indépendante du top-k ; et Petri non sélectionné : au-delà de la médiane le classement ne le prédit plus [RAPPORTÉ, D.3], donc le classement est déjà « au plafond » comme nos juges (κ = 0 [OBSERVÉ-NON-AUDITÉ, §4]) |
| **Banc tenu à l'écart** (isolé par l'OS) [RAPPORTÉ §2.5] | Taux de fuite : empreinte des items du banc cherchée dans toutes les données produites par les agents | — | Vérification purement mécanique ; un moniteur n'a rien à y faire |
| **Garde de capacité** (pass/fail, évaluateur séparé) [RAPPORTÉ §2.3] | Fidélité test-retest $f$ près du seuil (E3) | Méthodes clairement au-dessus/au-dessous (doivent donner $f = 0$) | Calibration empirique du seuil sur méthodes honnêtes, comme notre seuil calibré sur 1 000 épisodes (0,046-0,055 pour 0,050 prédit [OBSERVÉ-NON-AUDITÉ, §6]) |
| **Petri** (Sonnet 4.6 auditeur et juge, non sélectionné) [RAPPORTÉ §2.6] | Validité : une méthode plantée pour gonfler le score du classement sans effet réel doit **ne pas** bouger Petri | Méthodes honnêtes de score égal | Aucune mécanique ; sa valeur est précisément d'être hors sélection, à condition qu'il ne devienne jamais critère |
| **Banc de surveillabilité** (remède déclaré, non construit) [RAPPORTÉ §4] | Transfert hors banc (E2) ; sans cela il ne mesure que lui-même | Configurations tirées au hasard | Rappel mécanique par classe comme plancher |
| **Forum partagé** (retirer le forum coûte ~6 points [RAPPORTÉ D.5]) | Taux d'adoption d'une classe plantée par les autres agents après publication, contre sans forum (lien forum/contagion non fait par la littérature servie [RAPPORTÉ]) | Adoption de méthodes honnêtes publiées (taux de base) | Comptage mécanique des classes dans les méthodes postérieures |
| **Juge statistique** (nôtre) [OBSERVÉ-NON-AUDITÉ §1-3] | Déjà mesuré sur scriptés (0/1 000 sur 11 lignes) et sur W2 (12/12 promues) ; manque : rappel d'un moniteur ajouté, avant/après promotion (E4) | Lois honnêtes appariées en force | La borne $1-(1-\alpha)^n$ comme plancher d'attaque |
| **Sondes boîte blanche P3** (nôtres) [OBSERVÉ-NON-AUDITÉ §6] | « Non détecté à cette puissance » : aucune sonde générique ne dépasse son plancher de 200 sondes aléatoires appariées | — | Le plancher de sondes aléatoires est déjà la bonne mécanique ; à reprendre tel quel pour tout moniteur d'activations ajouté au harnais |

Lecture d'ensemble [HYPOTHÈSE] : des trois classes signalées par Kirchner, R et F sont mécaniquement vérifiables à coût presque nul. Si le moniteur de langage ne bat pas la mécanique sur R et F, sa seule valeur ajoutée est P, et c'est sur P que l'effet « même modèle » se joue.

## (d) Ancrage matériel

- **Cibles et coût par méthode** : cibles de moins de sept milliards de paramètres, une carte graphique, environ 30 minutes par méthode [RAPPORTÉ, D.3]. E1 avec 1 400 méthodes (1 200 honnêtes + ~180 plants, illustratif) : ~700 heures de GPU (calcul sur le 30 min rapporté, effectif illustratif), soit un peu moins d'une semaine sur quatre cartes (calcul). À 2-3 dollars par heure de H100 (illustratif), 1 400 à 2 100 dollars (calcul sur chiffres illustratifs).
- **Agents et moniteur à poids ouverts** : Qwen2.5-72B-Instruct et GLM-4-32B apparaissent comme *cibles* en E.1 [RAPPORTÉ], pas comme agents ; les employer comme agents et moniteur est une transposition [HYPOTHÈSE]. Croisement « même famille / autre famille » : Qwen-72B agents et moniteur, contre Llama-3.1-70B moniteur (illustratif). Si les agents ouverts produisent trop peu de méthodes exécutables, replier sur E4 (CPU, quelques heures par course, coût d'inférence seul).
- **Ordre de grandeur de référence** : le chercheur faible-vers-fort a coûté environ 18 000 dollars pour 800 heures d'agent à 22 dollars l'heure [RAPPORTÉ, §2.9] ; E.1 a mobilisé douze agents, sept jours, huit H100 chacun [RAPPORTÉ]. E1 vise un budget d'un ordre de grandeur en dessous, parce qu'on ne cherche pas de bonnes méthodes, seulement une population assez grande pour y cacher des plants.
- **E2** : 40 configurations × (banc + population fraîche) ; coût dominé par l'inférence du moniteur, pas par l'entraînement des cibles (illustratif : un tiers de E1).
- **E3** : 20 évaluations × ~60 méthodes près du seuil (illustratif), évaluateur seul : ~2 jours d'une carte (illustratif).
- **E4** : organisme public, sans GPU ; la borne $1-(1-\alpha)^n$ et le nul v8 existent déjà [OBSERVÉ-NON-AUDITÉ].

## Ce qui me ferait changer d'avis (réponse à la clause du mentor)

- Si l'annexe G, une fois lue, contient déjà une matrice de confusion sur tricheries plantées **stratifiée par rang**, le problème n'est pas sous-estimé : je retire la fiche.
- Si E1 donne $E \le 1{,}3$ avec au moins 60 plants par classe et un rappel global ≥ 0,80 à ≤ 0,05 de fausses alertes, le moniteur du même modèle est, pour ce régime sans gradient, un instrument acceptable, et l'inquiétude se déplace vers le gradient (déjà pris).
- Si le moniteur de langage ne bat pas les vérifications mécaniques sur R et F de plus de 0,10 de rappel à fausses alertes égales, la bonne réponse n'est pas « better control scaffolding » mais remplacer le moniteur par la mécanique sur ces classes et le réserver à P.
- Si, en E2, $\rho \ge 0{,}4$ alors que le contrôle interne monte aussi, la sélection sur banc de surveillabilité transfère et le remède de Kirchner tient au moins en sélection.

Ce que ces expériences ne disent pas : rien sur la triche spontanée (le rappel sur plants reste un plafond [HYPOTHÈSE, point (a).4]), rien sur des modèles futurs qui n'écriraient plus leurs tentatives dans leur raisonnement [RAPPORTÉ, Anthropic 28 août].

FIN-DE-CELLULE