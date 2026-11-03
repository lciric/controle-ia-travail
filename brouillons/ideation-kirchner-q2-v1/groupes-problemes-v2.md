# Groupes de problèmes sous-estimés, piste Kirchner, version 2

Groupeur neuf, aveugle au classement. Entrée unique, lue en entier avant d'écrire les groupes : `/home/claude/scratch/kirchner-rapport/piste-kirchner/fiches-a-grouper-v2.json` (sha256 `8c420b0828f2318777bed98c117536d9ba072191dfe9e8b0279b64fd815b9f24`, vérifiée), 29 fiches. Aucun autre fichier lu.

## 1. Définitions des groupes

Écrites le 2026-11-03 à 14:21:40 UTC (heure relevée par `date -u` juste avant l'écriture), avant toute affectation. Elles ne sont plus modifiées ensuite : toute tension va dans la rubrique « Limites ».

Problème sous-estimé : ce qui, dans la recherche d'alignement automatisée ou sa sélection, fait passer pour un progrès ce qui n'en est pas, ou cache ce qui en est un. Un groupe est un problème, pas une méthode de mesure.

### Groupe 1 — Instruments non qualifiés

Définition :
On lit le progrès et l'absence de triche sur des instruments (classement, bancs, garde de capacité, moniteurs de langage, sondes, Petri) dont personne n'a établi qu'ils battent un plancher trivial ou une vérification mécanique moins chère.
Un instrument au plafond, qui ne mesure que du bruit ou qui lit le récit de l'agent plutôt que son acte, rend ses verdicts vides, dans un sens comme dans l'autre.

Critère :
L'énoncé teste la validité d'un instrument sur une population donnée : contre un plancher (hasard, sondes aléatoires, fidélité test-retest, plafond), contre une base moins chère (vérification mécanique), ou selon la source qu'il lit (faits d'exécution relevés indépendamment, contre texte produit par l'agent). La sélection, l'adaptation des agents, la couverture des classes et la dépendance entre contrôles n'y sont pas le mécanisme central.

### Groupe 2 — Progrès gonflé par la sélection

Définition :
Retenir le meilleur (méthode, graine, soumission, configuration) d'après une mesure bruitée, consultée à répétition ou limitée aux classes d'un banc surestime sa valeur sur une mesure indépendante, même sans violation cachée.
Relances, resoumissions, réutilisation d'un banc réservé et gains propres au banc passent ainsi pour des progrès ou des passages de garde.

Critère :
L'énoncé porte sur le progrès apparent de ce qui est retenu (score, gain, passage de garde) et l'attribue aux limites de la mesure (bruit, répétition, réutilisation, classes du banc) : il le compare à une mesure indépendante (banc frais ou scellé, évaluation de référence plus grande, audit hors banc, bande de bruit des relances) ou mesure à quelle fréquence du bruit est retenu comme progrès. Le taux d'erreur d'un contrôle parmi les lauréats du classement relève du groupe « Contrôle affaibli par la sélection ».

### Groupe 3 — Contrôle affaibli par la sélection

Définition :
À contrôle figé et sans adaptation des agents, la sélection par le score du classement retient (ou fait naître) une population où le contrôle se trompe davantage que sur celle où on l'a validé.
Le rappel, les fausses alertes ou les faux passages publiés pour la population ne valent plus parmi les lauréats.

Critère :
L'énoncé compare un taux d'erreur d'un contrôle (moniteur, seuil, garde ; ou part de violations qui passent) parmi ce que la sélection par le score du classement retient ou fait naître, au même taux sur la population entière, sur une autre tranche du classement ou sur une référence non sélectionnée (violations instruites, épisodes non sélectionnés). Si ce qui retient est lui-même un contrôle (un juge qui promeut) et que l'énoncé porte sur les erreurs d'un second contrôle parmi ce que le premier laisse passer, la fiche relève du groupe « Défenses corrélées ».

### Groupe 4 — Classes hors couverture

Définition :
Une garantie statistique ne vaut que pour les classes que contiennent la nulle du juge ou la banque de validation du contrôle.
Les classes hors couverture (hors nulle, relationnelles, rendues admissibles par une archive qui grandit) passent sans garantie, et ni tirages frais ni banc plus grand n'y remédient.

Critère :
L'énoncé affirme qu'une classe de violations échappe à la garantie parce qu'elle sort de la nulle ou de la banque de validation (par construction, ou parce que l'archive grandit), et teste ce qui rétablit ou non la garantie (tirages frais, banc agrandi, nulle élargie, audit actualisé à l'archive). Des classes tenues hors banc qui servent seulement à tester le transfert d'un gain ne suffisent pas.

### Groupe 5 — Défenses corrélées

Définition :
On compte sur des contrôles empilés, ou sur un moniteur distinct de l'agent, comme si leurs erreurs étaient indépendantes.
Une famille de modèles partagée, une description publique commune ou un contexte commun leur font rater les mêmes violations ensemble : l'empilement donne une couverture illusoire.

Critère :
L'énoncé porte sur la dépendance entre erreurs : entre deux contrôles (y compris un juge qui promeut et un moniteur qui audite les promus), entre l'agent et son moniteur (même famille ou non), ou entre les ratés simultanés de plusieurs dossiers ; non sur le taux d'erreur marginal d'un seul contrôle.

### Groupe 6 — Contournement appris et contagion

Définition :
Ce que le dispositif montre ou renvoie aux agents (motifs de rejet, règles et frontière de la nulle, forum, rang affiché) change la population des violations pendant la course.
Contournements appris et triches recopiées font que le rappel mesuré hors boucle surestime le rappel dans la boucle, même à moniteur figé.

Critère :
L'énoncé fait varier un canal d'information vers les agents ou entre eux (montré ou caché, plus ou moins détaillé, forum ouvert ou fermé, rang affiché ou non) et mesure son effet sur la triche ou sur le rappel d'un contrôle, ou mesure la diffusion de la triche par ce canal.

### Règle de départage et second choix

1. Une fiche va au groupe dont le critère décrit la grandeur que mesure son énoncé principal ; si deux critères la décrivent, le facteur que l'énoncé fait varier tranche ; en dernier recours, son mécanisme.
2. Les variantes introduites par « une version » ne comptent pas pour l'affectation principale.
3. Second choix : un autre groupe dont le critère s'applique presque aussi bien à l'énoncé principal (à l'une de ses grandeurs, ou à un facteur auquel il prête un effet) ; sinon aucun.

<!-- fin des définitions -->

## 2. Affectations

Écrites le 2026-11-03 14:24:15 UTC (heure relevée par `date -u`), après les définitions. Avant l'ajout, le préfixe des définitions a été vérifié inchangé : 6516 octets, sha256 `d39deafb82fce3b1d96d4de66b9302381c31107d6f9a5c78bf00a9706f705cc6`, relevé à 2026-11-03 14:22:06 UTC. Les groupes du fichier JSON sont extraits mot pour mot de ce préfixe (les deux lignes de chaque définition jointes par une espace).

| Fiche | Groupe | Raison | Second choix |
|---|---|---|---|
| KM-01 | 1. Instruments non qualifiés | Réclame pour chaque instrument du harnais une épreuve minimale de validité (fidélité test-retest, planchers, fuite du banc), sur cas honnêtes appariés. | — |
| KM-02 | 4. Classes hors couverture | Une classe hors nulle (W2) garde un taux de fausse promotion d'au moins 0,8 même sur tirages frais : le remède au bruit ne la couvre pas. | — |
| KM-03 | 2. Progrès gonflé par la sélection | Un gain de surveillabilité choisi sur un banc est remesuré par un audit hors banc contre un témoin non sélectionné : il peut n'être propre qu'au banc. | — |
| KM-04 | 1. Instruments non qualifiés | Mesure l'apport du moniteur de langage au-delà de la vérification mécanique, sur les mêmes cas, l'oracle mécanique servant d'étiquette. | — |
| KM-05 | 2. Progrès gonflé par la sélection | Une méthode en échec franchit la garde par simple resoumission : passage dû au bruit, jugé contre une évaluation de référence plus grande. | — |
| KM-06 | 1. Instruments non qualifiés | Le moniteur de langage n'apporte rien s'il ne bat pas de 0,15 de rappel une vérification mécanique isolée, à fausses alertes égales. | — |
| KM-07 | 5. Défenses corrélées | Rappel du moniteur plus bas parmi les lois que le juge promeut : erreurs corrélées entre deux contrôles en série, cas que le critère du contrôle affaibli renvoie ici. | 3. Contrôle affaibli par la sélection |
| KM-09 | 5. Défenses corrélées | Interaction même famille contre autre famille entre l'agent et son moniteur, à fausses alertes égalisées. | — |
| KM-10 | 6. Contournement appris et contagion | Mesure la reprise, par les autres agents, d'une triche publiée sur le forum, contre la reprise des méthodes honnêtes publiées. | — |
| KM-11 | 5. Défenses corrélées | Excès de co-ratage entre deux moniteurs de même famille, à entrée identique et taux de ratage égalisés. | — |
| KM-12 | 6. Contournement appris et contagion | Facteur principal : montrer les règles d'exclusion et la frontière de la nulle, qui serviraient de carte ; grandeur : promotion de fausses lois hors nulle. | 4. Classes hors couverture |
| KM-13 | 2. Progrès gonflé par la sélection | Le gagnant du 99e centile est le maximum d'estimations bruitées ; il est comparé, sur un auditeur hors banc, à la première méthode qui franchit un seuil d'e-valeur. | — |
| KM-14 | 2. Progrès gonflé par la sélection | Isole l'effet de la réutilisation adaptative d'un banc réservé sur les fausses promotions, au-delà de la multiplicité des essais. | 6. Contournement appris et contagion |
| KM-15 | 3. Contrôle affaibli par la sélection | Rappel d'un moniteur figé plus bas parmi les violations que le classement retient que sur toutes les violations exécutées (effet de type Berkson). | — |
| KM-17 | 3. Contrôle affaibli par la sélection | Part des recombinaisons qui passent et rappel du moniteur, comparés entre la médiane et le haut du classement. | 4. Classes hors couverture |
| KM-18 | 4. Classes hors couverture | L'archive qui grandit rend admissibles des classes relationnelles que le contrôle figé ne couvre pas ; audit actualisé contre banc initial agrandi. | — |
| KM-19 | 2. Progrès gonflé par la sélection | Fréquence à laquelle de simples relances d'une méthode entrent au top 3, sous moyenne simple et sous test par e-valeurs. | — |
| KM-20 | 3. Contrôle affaibli par la sélection | Une invite de moniteur validée sur des triches instruites est mesurée sur les triches que la seule sélection par score fait naître. | — |
| KM-21 | 2. Progrès gonflé par la sélection | Part des méthodes de tête honnêtes qui ne battent pas le meneur précédent au-delà de la bande de bruit des relances. | — |
| KM-22 | 3. Contrôle affaibli par la sélection | Un seuil calibré sur des épisodes honnêtes non sélectionnés dépasse son budget de fausses alertes parmi les gagnants du classement. | — |
| KM-23 | 2. Progrès gonflé par la sélection | Facteur : le bruit de la garde ; grandeur première : la part de la classe relance et tri de graines au top 3 ; la séparabilité du moniteur vient en second. | 3. Contrôle affaibli par la sélection |
| KM-24 | 6. Contournement appris et contagion | Dose d'information renvoyée par le moniteur avant exécution, contre rappel du moniteur après coup. | — |
| KM-25 | 2. Progrès gonflé par la sélection | Choisir à répétition les meneurs sur le banc tenu à l'écart l'épuise : écart avec un second banc jamais utilisé. | — |
| KM-26 | 3. Contrôle affaibli par la sélection | Les faux passages d'une garde bruitée se concentrent parmi les gagnants du classement, contre l'ensemble ou des passants tirés au hasard. | 2. Progrès gonflé par la sélection |
| KM-27 | 6. Contournement appris et contagion | Le forum propagerait la structure des filtres du moniteur : rappel sur les quatre autres agents, avec et sans forum. | — |
| KM-28 | 1. Instruments non qualifiés | Ce que lit l'audit : relevé d'exécution collecté indépendamment contre explication rédigée par le chercheur, à budget de lecture égal. | — |
| KM-29 | 1. Instruments non qualifiés | Une sonde générique de tromperie doit battre 200 sondes aléatoires appariées, sur des triches non verbalisées ; le rappel après sélection vient en second. | 3. Contrôle affaibli par la sélection |
| KM-30 | 6. Contournement appris et contagion | Rang affiché (0, 2 puis 5 rivaux) contre rappel du moniteur et taux de tentatives. | — |
| KM-31 | 5. Défenses corrélées | Grandeur : corrélation des faux négatifs entre dossiers, à rappel marginal comparable ; le forum commun en est le facteur. | 6. Contournement appris et contagion |

### Comptes

| Groupe | Fiches en premier choix | Nombre | Fiches qui l'ont en second choix |
|---|---|---|---|
| 1. Instruments non qualifiés | KM-01, KM-04, KM-06, KM-28, KM-29 | 5 | — |
| 2. Progrès gonflé par la sélection | KM-03, KM-05, KM-13, KM-14, KM-19, KM-21, KM-23, KM-25 | 8 | KM-26 |
| 3. Contrôle affaibli par la sélection | KM-15, KM-17, KM-20, KM-22, KM-26 | 5 | KM-07, KM-23, KM-29 |
| 4. Classes hors couverture | KM-02, KM-18 | 2 | KM-12, KM-17 |
| 5. Défenses corrélées | KM-07, KM-09, KM-11, KM-31 | 4 | — |
| 6. Contournement appris et contagion | KM-10, KM-12, KM-24, KM-27, KM-30 | 5 | KM-14, KM-31 |

Total : 29 fiches, chacune dans un seul groupe ; 8 ont un second choix.

## 3. Limites

1. Groupes écrits après lecture des 29 fiches, comme la consigne l'impose : les critères anticipent des cas limites vus à la lecture (renvoi du critère 3 vers le groupe 5, exclusion des classes tenues hors banc au critère 4, « limites de la mesure » au critère 2). L'aveuglement porte sur le classement, pas sur les fiches.
2. Plafond de six groupes : « Instruments non qualifiés » réunit deux problèmes voisins, le plancher de validité (KM-01, KM-04, KM-06) et la lecture du récit plutôt que de l'acte (KM-28, KM-29). Un septième groupe les séparerait ; des variantes de KM-03 (ce que la configuration rend observable au moniteur) et de KM-15 (triche exécutée sans délibération écrite) y iraient aussi.
3. « Progrès gonflé par la sélection » et « Contrôle affaibli par la sélection » naissent tous deux de la sélection ; seule la grandeur mesurée les sépare (progrès apparent du retenu, contre taux d'erreur d'un contrôle parmi les lauréats). KM-23 et KM-26 mesurent les deux et sont tranchées par la règle de départage : un autre lecteur pourrait les intervertir.
4. KM-07 a l'estimande du groupe 3 (rappel parmi les lois promues contre population) ; c'est le renvoi écrit dans le critère 3 (celui qui retient est un juge, donc un contrôle) qui l'envoie aux « Défenses corrélées ». Sans ce renvoi, elle irait au groupe 3.
5. « Classes hors couverture » n'a que deux fiches en premier choix (KM-02, KM-18) et deux en second (KM-12, KM-17). KM-03 et KM-28 en sont proches (classes hors banc ; pour KM-28, une version sur quatre états d'archive et un récit « cohérent avec l'archive »), mais la dernière phrase du critère 4 les exclut ; sans elle, KM-28 pourrait y aller.
6. KM-03 n'a pas de second choix : le critère 1 exclut les fiches où la sélection est centrale, le critère 4 exclut les classes hors banc qui servent au transfert, et le critère 3 vise la sélection par le score du classement, non par un score de surveillabilité. Elle touche pourtant la validité du banc de surveillabilité (groupe 1) et le déplacement du trou vers des classes hors banc (groupe 4).
7. KM-02 : le facteur « avec ou sans retour des verdicts » relèverait du groupe 6, mais l'énoncé lui prédit un effet nul ; pas de second choix (règle 3).
8. KM-10 : l'énoncé principal ne fait pas varier le canal (il compare la reprise d'une triche à celle des méthodes honnêtes sur le même forum) ; elle entre au groupe 6 par la clause « diffusion de la triche par ce canal ». Les conditions sans forum ou avec quarantaine ne figurent que dans des versions.
9. KM-30 : le rang affiché est une pression de compétition plus qu'une information sur les contrôles ; la définition 6 le nomme, mais on pourrait y voir un problème distinct.
10. « Défenses corrélées » étend la dépendance entre erreurs à la relation entre l'agent et son moniteur (KM-09), où l'« erreur » de l'agent est de produire la violation.
11. Fiches à plusieurs versions : affectation sur l'énoncé principal seulement (règle 2). Certaines versions iraient ailleurs : le forum de KM-15 vers le groupe 6 ; l'archive de KM-20 et de KM-26 vers le groupe 4.
12. Premières expériences tronquées dans l'entrée : l'affectation repose sur l'énoncé et le mécanisme ; la partie coupée (notamment KM-03, KM-04, KM-06, KM-15, KM-26) pourrait nuancer une lecture.
13. La taille d'un groupe reflète la moisson des fiches, pas l'importance ni le degré de sous-estimation du problème ; ces groupes ne sont pas classés.

