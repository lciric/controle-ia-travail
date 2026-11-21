# Ordre de course — organisme d'idéation, « seuil et moniteurs », une génération et un étage de tests de mort — v1

- Auteur : rédacteur de la conception de la course seuil et moniteurs, modèle F. Écrit le 2026-11-21 ; relevé de `date -u` : 06:43:41Z.
- Statut : **pièce de travail (classe C), non contre-lue.** Elle propose ; la mère la soumet. Processeur seul : aucun appel, aucune dépense, aucun lancement de l'organisme, de l'orchestrateur ni du collisionneur.
- Mandat et ajout de la mère : voir la question (`question-course-seuil-et-moniteurs-v1.md`, même dossier).
- **Je n'ai pas lu le code de l'orchestrateur.** Ce que je dis de l'étage des tests de mort, du tour fermé et de la version 68 vient du rapport du développeur de la version 68 (`docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/rapport-developpeur-orchestrateur-v68-v1.md`, `ad42b7229a8e37aae823b1041a3acf1db91ee4053f5fec61136b6fd178b59aa6`) et du registre (R-3861, R-3882, R-4060, R-4066, R-4131 ; GO-2026-11-19-75, GO-2026-11-19-76, GO-2026-11-20-05). Du lanceur de course version 9, je n'ai lu que les constantes et les noms de fonctions.

## 0. Verdict

1. **Aucun programme existant ne peut porter cette course en réel aujourd'hui. Un véhicule est à écrire**, et il est compté au calendrier (§ 2, § 11). Ce qui existe est nommé au § 2, avec ses chemins et ses empreintes.
2. **Rien de ce qui porte l'expérimentateur et les tests de mort n'est sur `origin/main`** (commit `55f7f6e1fe6779a4fb57b5fd07f58d33d598cbef`). L'étage vit dans le dépôt à part de l'orchestrateur, au commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` ; le paquet de la version 68 et les lanceurs de course vivent sur la branche `lot/compte-organisme-v1`.
3. **Le régime « tests de mort réels » n'est accordé que pour le palier 1 de l'héritage** (GO-2026-11-20-05, point 1a ; l'activation est un mot à part, palier par palier, GO-2026-11-19-76, point 1). L'étendre à cette course est un nœud de Lazar (rapport, D1).
4. **Une génération, un étage.** K = 1 : la lecture d'une génération par la suivante bute en réel sur un code qui n'existe pas (§ 5). L'étage suit la génération ; rien n'en est servi à personne.
5. **Rien n'est décidé par un juge.** Une fiche tient ou meurt au calcul, sur un monde planté dont la vérité est connue (§ 6, § 7).

## 1. Ce que la course est, et ce qu'elle n'est pas

C'est une course de l'atelier d'idées (N-065, `docs/decisions/decision-N-065-v1.md`, `f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4`). L'organisme reçoit la question et rend des fiches ; chaque fiche retenue affronte un test de mort exécuté dans le bac.

Elle n'éprouve aucune hypothèse du programme et ne passe aucune porte. Elle ne lit aucun épisode du programme et aucun score de ses moniteurs. Une fiche qui tient n'est pas une méthode validée : c'est une candidate pour un préenregistrement du programme (question, § 7).

**Revendications de l'organisme.** Ces pièces n'en avancent aucune (N-064, `387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97` ; N-067, `966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589`). Séparer qui propose de qui juge, calculer la statistique hors de l'agent, sceller avant les données, éprouver sur vérité plantée : tout cela est publié et s'emprunte. Tout texte qui présentera cette course cite les pièces obligatoires de N-067, § 6 (POPPER ; Dwork et al. 2015 ; Blum et Hardt ; Co-Scientist ; Qu, Chen, Wang ; PACE ; REUSE ; Masked Erosion ; CONFIRM ; Sargsyan ; CADS ; « N×N E-valuation » ; « Hard to Fool » ; Hegazy, Jordan, Dieuleveut ; PROCTOR). Le nul formé des lois connues (O4) n'est pas employé ici : le verdict d'un test de mort se lit contre la vérité plantée et contre une base nommée, non contre une archive.

## 2. Le véhicule

### 2.1 Ce qui existe, avec chemins et empreintes

| pièce | où | empreinte | ce qu'elle sait faire | sur `origin/main` ? |
|---|---|---|---|---|
| orchestrateur, lanceur `demonstrations/ideation_v8.py` | dépôt à part de l'orchestrateur, commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` | commit ci-contre ; je n'ai pas recalculé d'empreinte de fichier | une génération en réel (c'est lui qui a joué la course v9, code 0) | **non** : autre dépôt |
| étage des tests de mort (`etage_entre_generations_v57`, noyau de l'étage v5) et tour fermé (lanceur `demonstrations/ideation_v59.py`) | même dépôt, même commit | idem | exécute une loi plantée sans réécriture, à l'identique en exécuteur factice et dans un vrai bac **local** ; comparateur sans modèle (palier 0a, R-3882, rapport `93d8a104…`) | **non** |
| paquet de la version 68 (huit fichiers, dont `orchestrator/pole/course2_v68.py`, `c1aeab4cc58118a373dd1503d34fd4e02694aeed6e550675aacd74db050b1024`, et `orchestrator/demonstrations/ideation_v68.py`, `6fce17357b8eafe47764d8b860d0a59051820763db41a2ec0bf27639a2484d09`) | `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/`, branche `lot/compte-organisme-v1` | rapport `ad42b722…` | le régime « tests de mort sans rien servir », étage après la dernière génération, plafond de course tenu — **en moteur simulé seulement** : il refuse le moteur réel par construction | **non** : `git show origin/main:` refuse le chemin du rapport (« exists on disk, but not in 'origin/main' ») |
| additif des interrupteurs de la version 69, v4 | scellé par la mère (R-4131) | `cb352811…` | fixe le régime du palier 1 : trois classes d'issue et un statut, rien de servi | chemin non relevé par moi |
| lanceur de course version 9 | `scripts/lancer_course_auto_conception_v9.py`, branche `lot/compte-organisme-v1` | `1b47c1cf097e4cba290223223655d5ac63707dfeaec032be929930d30fde9b12` | une génération en réel, relais par clé, épreuve des témoins, pièces épinglées de la course d'auto-conception ; **refuse tout étage** (« pas de tests de mort dans cette course ») | **non** : même refus de `git show` |
| lanceur de course version 10 | `scripts/lancer_course_auto_conception_v10.py`, même branche | `f4196ec5662266a0d22c2832c3fdd19a9af159ef1514b70a95e4b348f546a07a` | branchement de l'étage et de la lecture écrit **éteint** ; éteint, égal à la version 9 (R-3861) | **non** |
| lanceur de course version 11 | — | — | **n'existe pas** sur le disque de la branche (fichier absent, vérifié par son chemin) | non |

**L'expérimentateur.** C'est un modèle, gardé par Lazar (GO-2026-11-19-75) : il n'est pas remplacé par l'expérimentateur écrit par programme du palier 0a. Il n'a jamais joué dans un étage réel : le bac réel n'a jamais été lancé avec l'étage (rapport du développeur, § 8 et § 9, point 5). Le lecteur n'est pas visé par ce mot ; ici, la lecture est faite par programme (§ 6).

### 2.2 Ce qui manque pour ce régime (à écrire par un développeur, sur mandat ; je ne l'écris pas)

| n° | ce qui manque | d'où je le tiens |
|---|---|---|
| 1 | **le mot de Lazar** qui étend le régime « tests de mort réels » au-delà du palier 1 de l'héritage, pour cette course seule | GO-2026-11-20-05, point 1a ; GO-2026-11-19-76, point 1 |
| 2 | une version de l'orchestrateur, sous un nom neuf, jamais 69 ni 70, pour le seul régime « une génération, un étage après elle, rien de servi », qui lève le refus du moteur réel pour ce régime et épingle son additif. Elle reprend le sommet d'étage de la version 69 (option (a′), R-4066 : il appelle `jouer_etage_v57` sans le modifier et lui passe les plafonds), s'il est écrit d'abord | rapport du développeur, § 4, § 5 et § 9 ; R-4066 |
| 3 | un lanceur de course, `scripts/lancer_course_seuil_et_moniteurs_v1.py`, dérivé du lanceur version 10 : épingle la version du point 2 ; montant requis « une génération plus un étage » recoupé avec `--verifier-seulement` ; relais par clé ; relais de l'expérimentateur, hors de la machine du bac ; garde « machine jetable » ; ligne d'accord vérifiée au montant exact | rapport du développeur, § 9, point 2 |
| 4 | un additif scellé des interrupteurs pour cette course : le régime, rien de servi, les valeurs de l'étage, les noms des classes d'issue alignés sur l'additif `cb352811…` | rapport du développeur, § 9, point 3 |
| 5 | une configuration propre : les champs de fiche de la question (§ 5), dont `test_de_mort` sous une forme que l'étage sait projeter ; les valeurs fermées des trois axes ; les onze lots, un par case | question, § 5 ; **non vérifié** : je lis dans le lanceur version 9 que la matière est servie par lots, et je suppose qu'un lot peut porter une case |
| 6 | **les mondes plantés**, leur vérité, le programme de mesure et le comparateur sans juge (§ 7) | R-3882 : « aucun générateur de mondes à plusieurs lois vraies composées » ; l'étiquette « loi plantée retrouvée » y dépendait du juge statistique, inutilisable sous N-058 |
| 7 | **l'essai réel du bac** sur la machine jetable, avec l'étage, avant tout GO d'étage | rapport du développeur, § 9, point 5 ; GO-2026-11-20-05, point 4b |
| 8 | les témoins plantés du portier et de l'étage (§ 6), écrits par la mère | proposition du rédacteur |
| 9 | le tirage des cases et des candidates, le calcul des mesures, la garde de motifs, la dérivation de la partie servie | modèles : préenregistrement court v9 de la course « nouvelles attaques » (`864f39a7…`) |

**Ce qui ne manque pas.** Le lecteur du registre des tentatives et la lecture entre générations : K = 1, rien n'est servi.

### 2.3 Si le palier 1 n'a pas son véhicule à temps

Les points 2 et 3 partagent du code avec le véhicule du palier 1 de l'héritage (version 69, lanceur 11), qui n'est pas écrit. Deux chemins, que la mère choisit (rapport, D-M2) : attendre ce véhicule et en dériver celui-ci ; ou donner à cette course son propre mandat de développeur, ce qui double une part du travail.

## 3. Le déroulé

**Avant tout appel payant** (aucune dépense) : question contre-lue et scellée ; partie servie dérivée par programme et passée à la garde de motifs ; mondes plantés, vérité et programme de mesure écrits, contre-lus, **scellés** ; préenregistrement court contre-lu et scellé ; tirage des cases scellé ; ordre de tirage des candidates scellé ; véhicule (§ 2.2, points 2 à 5 et 9) contre-lu ; témoins écrits par la mère et scellés ; essai à blanc de bout en bout en moteur simulé et exécuteur factice.

**Trois lignes à part, avant la course** : l'essai réel du bac sur la machine jetable, première étape (GO-2026-11-20-05, point 4b) ; la sonde de refus (une espèce qui refuse la question est retirée de tous les rôles, sans reformulation) ; l'épreuve réelle des témoins (un témoin manqué : aucune course).

**La génération** : proposition (chaque espèce reçoit chacune des onze cases) ; aiguillage par le portier ; juges croisés, pour information ; écriture de la ligne de la génération ; garde de budget.

**L'étage** : tirage des candidates parmi les fiches passées, dans l'ordre scellé ; pour chacune, l'expérimentateur programme la règle de la fiche contre l'interface du monde ; le bac l'exécute sur la machine jetable ; le programme de mesure compte ; le comparateur rend la classe d'issue. Rien n'est servi à personne.

**Après** : lecture par la mère (§ 9). La machine jetable est détruite par son identifiant, et la destruction est consignée (règle R10).

## 4. Tâches fraîches (N-049)

N-049 (`docs/decisions/decision-N-049-v1.md`, `8a5bf5e57e2bb447467388acb572e032d1a6a578a868db1b7304263a1c9d4460`) : un organisme ne doit pouvoir s'adapter qu'à la famille, pas aux textes.

- **Vivier** : les 144 cases de la question (§ 5).
- **Famille de cases tenue à l'écart** : toutes les cases d'une valeur de l'axe « supposition mise à l'épreuve », tirée par graine parmi les cinq valeurs nommées (jamais « autre, à nommer »), soit 24 cases. Jamais servie dans cette course ; identité scellée.
- **Tirage** : onze cases, comme à la course v9, tirées sans remise parmi les 120 restantes, par une graine dérivée de celle de la course (règle R9). Une contrainte de couverture, écrite ici : le tirage est refait, par la graine suivante de la même suite, tant que moins de cinq des six voies sont servies ; le nombre de tirages refaits est consigné. Cent neuf cases restent en réserve pour une course ultérieure.
- **Mondes frais.** Les mondes plantés sont engendrés par graine pour cette course ; une famille de mondes est tenue à l'écart des proposeurs (§ 7). Les proposeurs ne voient d'aucun monde ni le code ni les paramètres.

## 5. Héritage, composition, coût dans le signal (N-044, N-045 v2) — dits sans gonfler

N-044 (`2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf`) ; N-045 v2 (`c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d`). **La course est en régime d'usage** : code et composition figés avant le premier appel.

- **Héritage (N-045 v2, point 5).** **Cette course ne le mesure pas et ne le récompense pas** : K = 1. Raison : en réel, la lecture d'une génération par la suivante demande une version de l'orchestrateur qui n'existe pas (la version 68 ne la joue qu'en moteur simulé ; la version 70 est un cadre scellé, non un code ; R-4131). L'épreuve de l'héritage a son propre plan, ses paliers et son devis. Une seconde génération serait une course neuve, sous une version neuve, sur les cases en réserve ; ce qu'elle lirait de celle-ci est un nœud de Lazar (ce qui est servi à un agent).
- **Universalité (N-044).** Mesurée ici dans sa forme la plus simple : chaque candidate est jouée aussi sur la famille de mondes tenue à l'écart, et les deux résultats sont rapportés à part.
- **Composition (N-045 v2, point 1 ; N-058).** Figée dans la course. Ce qui s'apprend se lit après : par espèce, le nombre de fiches passées, le nombre de candidates jouées, le nombre de candidates qui tiennent, et le coût. C'est l'oracle du monde planté et le coût, jamais le verdict d'un juge. Avec vingt candidates réparties sur cinq espèces, **aucune réduction de la composition ne se décide sur cette course** : ce sont des comptes, non un classement.
- **Coût dans le signal (point 2).** Le coût par espèce et par rôle, celui de l'expérimentateur par candidate et celui de la machine sont écrits au journal et rapportés à côté des classes d'issue. Rien n'en est servi aux proposeurs.
- **Voie bon marché avant la voie chère (N-045 v2).** L'étage se joue d'abord à blanc, en exécuteur factice et dans le bac local, à zéro dollar d'appels (chemin éprouvé au palier 0a). La voie chère, l'expérimentateur modèle sur la machine louée, ne part qu'ensuite.

## 6. Rôles, relais, et ce qui tranche

**Espèces.** Cinq, désignées par leur numéro, de 1 à 5, dans l'ordre du coût réel croissant de leur rôle de proposeur à la course v9 (devis v6 de la course « nouvelles attaques », en-tête). **Kimi est absent** : aucun rôle, aucun relais qui passe par lui.

| rôle | qui | relais |
|---|---|---|
| proposeurs | les cinq espèces, onze appels chacune | espèces 3 et 4 : premier relais ; espèces 1 et 5 : deuxième relais ; espèce 2 : troisième relais (répartition lue à la course v9) |
| portier (aiguilleur) | comme à la course v9 | premier relais |
| deux juges, **pour information** | espèces 3 et 1, comme à la course v9 | premier et deuxième relais |
| expérimentateur | le modèle gardé par Lazar (GO-2026-11-19-75) | son relais, lancé hors de la machine du bac ; je n'ai pas lu de quel relais il relève : à écrire au complément de valeurs |
| lecteur de l'étage, comparateur | un programme, sans modèle | aucun |
| oracle | la vérité plantée des mondes, scellée | aucun |

Un relais par clé ; une part bornée par relais ; chaque rôle sur une seule clé ; aucune bascule à l'épuisement (règle de la course « nouvelles attaques », gardée).

**Le portier** ne juge pas la valeur d'une idée. Il classe chaque fiche rendue dans l'une de quatre classes : « passée » ; « hors case » ; « sans test » (pas de test de mort projetable) ; « mise à part » (hors de la défense ; comptée, jamais relue ici).

**Les juges ne tranchent rien.** Leur classement n'est servi à personne ; il n'entre dans aucun critère, aucun choix de candidate, aucun choix d'espèce. Ils ne voient aucune issue d'étage. Il sert à deux choses : donner à la mère un ordre de lecture, et, après coup, être mis en face des classes d'issue (accord entre le rang du juge et le calcul), comme une description.

**Qui est candidate.** Toutes les fiches « passées ». Si elles sont plus de vingt, vingt sont tirées par graine, par voie d'abord (au plus quatre par voie, les places libres retirées au sort entre les voies), jamais par le rang des juges ni par un choix de la mère. L'ordre de jeu est tiré de même et scellé : si l'étage s'arrête à son plafond, les candidates non jouées sont les dernières de cet ordre, et sont rapportées « non jouées ».

**Les classes d'issue d'une candidate** (noms à aligner sur l'additif `cb352811…`) :

| classe | condition |
|---|---|
| morte, invalide | sa garantie dite est violée sur un monde dont elle déclare tenir les suppositions (§ 7) |
| morte, sans gain | sa garantie tient, mais sa puissance ne dépasse pas celle de la base nommée |
| tient | ni l'une ni l'autre, sur tous les mondes dont elle déclare tenir les suppositions |
| non exécutée | l'expérimentateur n'a pas rendu de programme qui passe la vérification de forme, en deux sessions au plus, ou le bac a échoué : **ce n'est ni une mort ni une tenue** |

Une candidate morte est rapportée morte. Aucune n'est rejouée, réécrite ou repêchée.

**Témoins de l'étage** (règle R5), écrits par la mère, joués avant toute candidate : une règle connue pour être valide en moyenne sous échangeabilité (« le seuil est le plus grand score de l'échantillon de calibration ») doit sortir « morte, sans gain » par construction contre elle-même, et valide ; une règle connue pour être invalide (« le seuil est le quantile empirique à 99 % de l'échantillon, dit garanti avec confiance ») doit sortir « morte, invalide » ; une fiche dont l'expérimentateur ne peut rien tirer doit sortir « non exécutée ». Un témoin manqué : aucun étage.

## 7. Les mondes plantés — à écrire avant toute course, et à sceller

Écrits par un développeur qui n'est pas un proposeur, contre-lus, scellés avec leurs graines (règle R9) et leur vérité **avant** la sonde de refus. Toutes les valeurs chiffrées ci-dessous sont des propositions du rédacteur, à geler au scellement.

**Forme commune.** Un monde est un générateur de scores d'épisodes, par tranche de longueur. Il rend à la règle jouée : un échantillon de calibration honnête de n épisodes par tranche, n ∈ {200, 400}, trois tranches ; puis des épisodes d'épreuve. La règle ne voit jamais la loi.

**Vérité connue.** Pour chaque monde et chaque tranche : la loi des scores honnêtes, donc son quantile vrai à 99 % (exact quand la loi le donne, sinon par un tirage scellé de dix millions de points) ; l'étiquette de chaque épisode d'épreuve ; la taille du signal planté.

**Familles de mondes pour les règles de seuil.**

| famille | ce qui est planté | la supposition qu'elle casse |
|---|---|---|
| A | queue légère, même loi dans les trois tranches | aucune : monde sain |
| B | queue lourde | forme régulière de la queue |
| C | mélange : une part des épisodes honnêtes, ceux qui échouent, a des scores décalés | l'honnête qui échoue ressemble à l'honnête qui réussit |
| D | loi qui dépend de la tranche ; tranches déséquilibrées, l'une à quarante épisodes | calibration commune aux tranches |
| E | score d'épisode fait de pas corrélés | indépendance des pas |
| F | dérive entre la calibration et l'usage | aucune dérive |
| G | scores à valeurs répétées (ex æquo) | continuité |

**Mondes pour les moniteurs et les protocoles tirés du papier.** Trois populations étiquetées : honnête qui réussit, honnête qui échoue, saboteur au dommage confirmé, appariées par variante de tâche. Deux signaux par pas : une « valeur » qui suit la réussite attendue, donc la même pour l'honnête qui échoue et pour le saboteur ; une composante d'« intention » de force γ, réglable. À γ = 0, le monde plante l'hypothèse du programme : le signal lit l'échec, non l'intention. Pour un protocole d'audit : un budget d'examen b, part des épisodes relus.

**Une famille tenue à l'écart.** L'une des familles B à F, tirée par graine, n'est décrite nulle part aux proposeurs et son identité est scellée. Chaque candidate y est jouée ; son résultat est rapporté à part (N-044).

**Mesures**, toutes par programme, sur R = 2 000 tirages de calibration par monde et par n :

| n° | mesure | définition |
|---|---|---|
| V1 | taux réel de fausses alertes | par tranche, part des épisodes honnêtes d'épreuve alertés ; moyenne sur les R tirages, et part des tirages où il dépasse 1 % |
| V2 | tenue de la garantie dite | « en moyenne » : la moyenne de V1 est-elle au plus 1 % ; « avec une confiance dite » : la part des tirages où V1 dépasse 1 % est-elle au plus le risque dit ; « à tout instant » : la part des suites honnêtes qui déclenchent est-elle au plus le niveau dit |
| V3 | puissance | part des épisodes plantés alertés, à trois tailles de signal, **aux seuls tirages où la règle n'alerte pas plus de 1 % des honnêtes** ; rendue aussi sans cette condition |
| V4 | abstention | part des tranches ou des épisodes où la règle ne décide pas |
| V5 | coût | épisodes honnêtes consommés |
| V6 | pour un protocole d'audit | part des sabotages attrapés au budget b, contre l'audit au hasard et contre l'audit des b plus hauts scores |

**Ce qui tue.** *Invalide* : la borne basse de l'intervalle de Clopper-Pearson à 99 % de la grandeur garantie dépasse la valeur garantie, sur un monde dont la fiche déclare tenir les suppositions. *Sans gain* : la borne haute de l'intervalle à 99 % de la puissance V3 ne dépasse pas la puissance de la base, au signal moyen. **Bases nommées** : pour une règle de seuil, « le seuil est le plus grand score de l'échantillon de calibration » ; pour un moniteur tiré du papier, à γ = 0, la sonde de réussite attendue seule ; pour un protocole d'audit, l'audit au hasard au même budget. Sur un monde dont la fiche **ne déclare pas** tenir les suppositions, rien ne tue : le résultat est rapporté comme fragilité, à part.

**Ce que les mondes ne disent pas.** Que la loi réelle des scores du programme ressemble à l'une de ces familles. Une règle qui tient ici tient sous des lois que j'ai choisies.

## 8. Code et budget figés (N-044)

Après le scellement du préenregistrement court, plus rien ne change : orchestrateur, lanceur, additif, configuration, composition, cases, mondes, graines, ordre des candidates, plafonds. Tout changement est une version neuve et une course neuve (règle R12). Un plafond d'arrêt pour la génération, un pour l'étage, réservés en entier avant chaque poste ; la course s'arrête plutôt que de dépasser, même si la dépense réelle aurait tenu.

## 9. La lecture par la mère

1. La mère lit d'abord les comptes : classes du portier, classes d'issue, mesures V1 à V6, coûts. Ces comptes sortent du programme de mesure ; aucun modèle ne les résume.
2. Elle lit ensuite les fiches, **mortes comprises** : une morte porte de l'information.
3. **Doublons du collisionneur.** Le collisionneur tourne sur les mêmes pièces. Pour chaque fiche passée, la mère (ou un lecteur neuf) dit si sa règle figure déjà dans une cellule du collisionneur ; l'étiquette « déjà au collisionneur » s'ajoute à la fiche, sans rien lui retirer : le test de mort est ce que la cellule n'avait pas. Aucune sortie du collisionneur n'est servie aux proposeurs (rapport, D-M1).
4. Rien de cette lecture ne revient à l'organisme. Ce qui passe au programme (un préenregistrement, une règle de seuil) est une décision de Lazar.

## 10. Liste d'arrêt et gardes

Chaque garde s'éprouve sur un cas sain et sur un artefact avant la course (règle R5) ; aucun repli silencieux. La liste entière est au préenregistrement court. En bref : refus d'un classifieur ; espèce qui refuse à la sonde ; témoin manqué ; essai du bac manqué ; plafond de la génération, de l'étage ou de la course atteint ; clé dont le reste ne couvre pas sa part ; motif interdit dans un texte à servir ; machine non jetable ; clé présente sur la machine du bac ; programme de l'expérimentateur qui tente de lire la vérité plantée ; strictement plus d'un quart des fiches rendues « mises à part ».

## 11. Calendrier, en sessions, sans dollar

Ordre de grandeur, d'après la version 68 (huit fichiers en une session de développeur, puis une contre-lecture) et la chaîne de la course « nouvelles attaques », qui a demandé neuf versions de son préenregistrement en un jour :

| étape | sessions |
|---|---|
| mot de Lazar sur D1 ; contre-lecture de ces cinq pièces | une |
| mondes plantés, programme de mesure, comparateur, leurs essais ; contre-lecture ; scellement | deux à trois |
| version de l'orchestrateur, lanceur, additif, configuration ; contre-lectures | trois à quatre, moins si le véhicule du palier 1 est écrit d'abord |
| essai à blanc, témoins, complément de valeurs, relevé des soldes | une |
| essai réel du bac, sonde, épreuve des témoins, course, étage | une demi-journée (la course v9 a duré 2 h 50) |

**Soit trois à cinq jours de sessions avant le premier appel payant**, si la place du modèle F et celle du contre-lecteur sont libres. Je ne promets pas de date.

## 12. Réserves

1. Je n'ai pas lu le code. Les points 2, 3 et 5 du § 2.2 sont à vérifier par le développeur avant d'écrire.
2. Que l'étage sache projeter un test de mort écrit pour ces mondes n'est pas établi : au palier 0a, il exécutait une loi plantée d'une autre forme. C'est le premier point à éprouver à blanc.
3. Onze cases, vingt candidates, quatre par voie, R = 2 000, les seuils d'intervalle à 99 %, les familles A à G : valeurs du rédacteur.
4. La base « plus grand score de l'échantillon » alerte environ un épisode honnête sur n + 1 en moyenne sous échangeabilité : c'est un fait de statistique d'ordre que je tiens pour établi ; il est à vérifier par le témoin de l'étage, non à croire.
