# Proposition de recherche en couches — programme présenté à l'entretien Transformative AI Fund — v2

Lignée conv-audit, instance du 28 octobre 2026. Modèle servant déclaré par l'environnement au moment de l'écriture : Fable 5.1 ;
auteur désigné du travail principal : Opus 4.6, par décision de Lazar (l'attribution a varié dans la session, voir la réserve 5
de la couche 6). Écrit à partir du relevé `date -u` de **10:46:02 UTC le 28 octobre 2026**.

**Remplace** `proposition-recherche-en-couches-v1.md` (10:24 UTC, `289db00f…`), gardée telle quelle (R12). **Ce que la v2
change** : alignée sur le programme d'entretien **v4** (`8dbacfe5…`) — coût réel du programme (≈ 450 USD connus, note de
session-depot), front C à jour (mode tenu à l'écart conçu, règle R-609 sur les refus, porte R-611), **cinq fronts** (le pôle
scientifique automatique entre comme front E, mot de Lazar « on veut la version la plus ambitieuse »), collusion « largement
vierge », chiffres de la candidature **envoyée** (58 630 / 28 160 / 138 600, G1 fin du mois 4) et **demande la plus ambitieuse**
(≈ 176 500, ventilation v2). Les quarante-trois pistes ouvertes des deux lignées sont dans la v4, section 3 bis.

**Source.** Ce document met en forme, sans rien y ajouter de neuf, le programme d'entretien v4, le programme qui fait foi
(`docs/programme-controle-ia-v2.md`, `2fd63bad…`), la proposition envoyée (`737c482c…`) et les décisions qui en fixent la
lecture (`docs/decisions/`, N-054 et N-056 comprises). Tout chiffre renvoie à une pièce de la couche 6.

**Statut.** Brouillon interne, non contre-lu (voir réserve 4). **Rien ici n'est envoyé par moi** : tout contact externe est un
nœud, je rédige, Lazar décide et envoie.

**Mode d'emploi.** Six couches. Chacune se lit seule, chacune détaille la précédente ; on s'arrête où l'interlocuteur s'arrête.
Couche 0 : une phrase. Couche 1 : dix lignes. Couche 2 : une page. Couche 3 : le détail par front de recherche. Couche 4 :
gouvernance et portes. Couche 5 : calendrier et budget. Couche 6 : pièces, provenance, réserves. Les couches 0 et 1 sont
données en français et en anglais, parce que ce sont celles qui se disent à l'oral.

---

## Couche 0 — une phrase

**Français.** Nous construisons la partie du contrôle des intelligences artificielles qui dit, à l'avance et avec des preuves,
ce qu'un moniteur ne peut pas voir — et nous le vérifions sur des agents réels, sous préenregistrement, en publiant les nuls
avec leur puissance.

**English.** We are building the part of AI control that tells you, in advance and provably, what your monitor cannot see —
and we test it on real agents, under preregistration, publishing null results with their power.

---

## Couche 1 — dix lignes

**Français.**
1. **Problème.** Le champ déploie des moniteurs sur des trajectoires d'agents (sondes sur les activations, juges boîte noire,
   agrégateurs séquentiels) et les évalue sur les attaques auxquelles on a pensé. Personne ne peut dire d'avance ce qu'un
   moniteur donné est *structurellement* incapable de voir.
2. **Thèse.** Deux idées. D'abord, l'*additivité interne* : fragmenter un sabotage détruit la preuve externe par action, pas la
   preuve interne, qui s'additionne dans le temps (un agent) ou entre agents (un essaim). Ensuite, une *théorie des moniteurs* :
   pour chacune de nos statistiques de contrôle, les hypothèses qu'elle fait sur l'agent et la classe d'écart qui l'aveugle,
   prouvées au niveau des lois de probabilité.
3. **En main.** Une carte de 23 hypothèses sous un lemme maître prouvé (21 lemmes prouvés) ; une théorie vérifiée en simulation
   préenregistrée (31 prédictions sur 31) ; un harnais validé sur un modèle réel ; un banc de sabotage de recherche reconstruit
   (180 épisodes réels) ; un premier test boîte blanche réel **nul**, publié avec sa puissance ; une boucle automatique de test
   d'hypothèses qui a tourné de bout en bout sur données réelles.
4. **Ce que nous ferons.** Cinq fronts : la théorie (bornes quantitatives, matrice « statistique × classe d'écart »,
   vérification formelle) ; six mesures préenregistrées sur des données déjà payées, à coût de calcul nul ; une résistance
   adversariale gouvernée (neuf voies, six classes d'attaque cibles, un mode d'attaque tenu à l'écart déjà conçu par une instance
   qui n'a jamais vu un moniteur, sortie au niveau méthode, jamais la recette) ; deux papiers sur la corruptibilité des moniteurs
   et sur l'essaim ; et un pôle scientifique automatique — l'adversaire que l'on surveille est lui-même un chercheur
   automatique, dont la composition est apprise et mesurée.
5. **Ce qui nous distingue.** Un protocole que les agents d'exécution ne peuvent pas assouplir (préenregistrement scellé,
   contre-lecteur neuf, verdict de porte par un tiers, aucun run visant un signe positif) et un frein de sécurité qui a déjà
   mordu sur nous, deux fois le même jour, avec la trace écrite.
6. **Demande.** La candidature envoyée porte 58 630 USD (sept mois) et décrit déjà un scénario ambitieux à 138 600 (douze mois,
   avec l'essaim) ; **la version la plus ambitieuse** y ajoute ce qui n'existait pas le 7 octobre — revue de sécurité externe,
   adversaire scellé sous revue, matrice complète et vérification formelle, pôle scientifique automatique, collisionneur
   multi-modèles — pour **≈ 176 500 USD** ; c'est celle que nous recommandons (couche 5). Les instruments préenregistrés ont
   coûté moins de cent dollars de carte graphique ; le programme entier, tours multi-modèles et pilotes compris, quelques
   centaines de dollars à ce jour (≈ 450 connus).

**English.**
1. **Problem.** Our field deploys monitors over agent trajectories — activation probes, black-box judges, sequential
   aggregators — and evaluates them on the attacks we happened to think of. Nobody can tell you, in advance, what a given
   monitor is *structurally* unable to see.
2. **Thesis.** Two ideas. *Internal additivity*: fragmenting a sabotage destroys the external per-action evidence, not the
   internal evidence, which adds up over time (one agent) or across agents (a swarm). And a *theory of monitors*: for each of
   our control statistics, the assumptions it makes about the agent and the class of deviation that provably blinds it, stated
   at the level of probability laws.
3. **In hand.** A map of 23 assumptions under one proven master lemma (21 lemmas proven); a theory confirmed in a preregistered
   simulation (31 of 31 predictions); an activation harness validated on a real model; a reconstructed research-sabotage
   benchmark (180 real episodes); a first real white-box test that came back **null**, published with its power; an automatic
   hypothesis-testing loop that ran end to end on real data.
4. **What we will do.** Five fronts: theory (quantitative bounds, a "statistic × deviation class" matrix, formal verification);
   six preregistered measurements on data already paid for, at zero marginal compute; governed adversarial resistance (nine
   routes, six target attack classes, a held-out attack mode already designed by an instance that has never seen a monitor,
   output at the level of mechanism and defence, never recipe); two papers on monitor corruptibility and on the swarm; and an
   automated-scientist pole — the adversary we monitor is itself an automated researcher, whose composition is learned and
   measured.
5. **What sets us apart.** A protocol the executing agents cannot relax (sealed preregistration, fresh counter-reader,
   third-party gate verdicts, no run aimed at a positive sign) and a safety brake that has already bitten us, twice in one day,
   on the record.
6. **The ask.** The submitted application carries 58,630 dollars for seven months and already describes an ambitious scenario
   at 138,600 over twelve months, with the swarm paper; **the most ambitious version** adds what did not exist on the seventh of
   October — an external security review, the sealed adversary run under that review, the full matrix with formal verification,
   the automated-scientist pole, multi-model idea-collider rounds — for **about 176,500 dollars**; that is the version we
   recommend (layer 5). The preregistered instrument work ran under a hundred dollars of GPU; the whole programme, idea-collider
   rounds and organism pilots included, is a few hundred dollars to date (about 450 known).

---

## Couche 2 — une page

### 2.1 Le problème
Un moniteur de contrôle est un instrument de mesure, et le champ ne sait pas ce que ses instruments mesurent vraiment. Trois
symptômes : (a) les sondes publiées sont évaluées sur la tromperie qu'on leur a montrée, pas sur celle qu'on ne leur a pas
montrée ; (b) les protocoles de contrôle définissent eux-mêmes la population « sous le seuil » qu'ils sont ensuite incapables
d'observer ; (c) un sabotage **diffus** — étalé sur beaucoup d'actions, chacune innocente — passe sous tout moniteur par
action, par construction.

### 2.2 La thèse
**Additivité interne.** Sous trois conditions mesurables (chaque action de sabotage déplace la loi du score interne d'au moins
δ > 0 ; budget total de sabotage borné ; variance honnête estimable), la puissance d'un agrégateur séquentiel ne dépend que du
budget total, pas de la fragmentation : c'est le **lemme**. Et si le dommage passe par la **corrélation** entre actions à
marginales préservées, toute statistique marginale (maximum, moyenne, somme) a une puissance égale à son taux de fausses alertes :
c'est le **théorème négatif**, qui impose des agrégateurs d'autocorrélation (temps) ou de co-élévation (agents).

**Théorie des moniteurs.** La carte des hypothèses énonce, pour 8 statistiques de contrôle (11 lignes), les 23 hypothèses
qu'elles font sur l'agent, et pour chaque hypothèse la classe d'écart qui rend la statistique aveugle. Trois exemples :
sous une hétérogénéité d'épisodes de part r₀, le rappel de toute statistique contre un décalage constant **plafonne** quel que
soit l'horizon ; un moniteur qui **définit** la population sous le seuil y est aveugle par construction ; une sonde qui ne lit
que l'indication a, contre des négatifs appariés en indication, un rappel égal à son taux de fausses alertes.

### 2.3 Cinq fronts
- **A — Théorie du contrôle des moniteurs** : bornes quantitatives par classe, matrice « statistique × classe d'écart »,
  vérification formelle des lemmes, sept questions ouvertes déclarées comme telles. Coût : processeur seul.
- **B — Mesures à coût de calcul nul** : six mesures préenregistrées (T0 à T5) sur un fichier de scores déjà payé, chacune
  contre-lue, scellée, lue une fois.
- **C — Résistance adversariale gouvernée** : neuf voies de mesure, six classes d'attaque cibles, trois étages d'épreuve ;
  sortie au niveau méthode (classe, mécanisme, conditions, défense), jamais la recette ; revue de sécurité externe avant toute
  exécution adversariale.
- **D — Deux papiers** : la corruptibilité des moniteurs (papier C : loi de déférence, usurpation, taxe de déplacement,
  contre-mesures) et l'essaim (papier B : statistiques de population, compromis diversification/coordination, riposte, survie
  des contraintes de sécurité à la délégation).
- **E — Le pôle scientifique automatique** : l'organisme surveillé est un chercheur automatique ; sa composition est apprise
  (modèle par rôle, coût dans le signal, frontière entre rôles mesurée), son universalité est mesurée sur des familles de tâches
  inédites, sa lecture est honnête (test final lu une fois, contre-lecteur d'un autre modèle, aucun score de moniteur dans son
  entraînement). Il fournit les organismes de G1 par mode et les proposeurs de l'étage 1 du front C.

### 2.4 Ce qui est en main (vérifiable, scellé)
| # | résultat |
|---|---|
| H1 | Théorie en simulation préenregistrée : 31 prédictions sur 31 (342 cellules statistiques, 544 trajectorielles, 0 contraire) |
| H2 | Harnais d'activations validé sur le modèle réel (critère 1 de G0), 1,3 heure de carte graphique |
| H3 | Banc de sabotage de recherche reconstruit (ni code ni données publiés par les auteurs) ; 180 épisodes d'un agent réel scellés |
| H4 | 3 497 citations contrôlées sur sources primaires, 0 échec ; ≈ 900 tests ; décisions datées |
| H5 | Premier test boîte blanche réel : **nul**, audité, puissance chiffrée (aire minimale détectable à 80 % : 0,63 et 0,60, contre 0,58 supposé) |
| H6 | Carte des hypothèses : 23 hypothèses, lemme maître prouvé, 21 lemmes prouvés, 15 classes instanciées dans la littérature, 7 questions ouvertes |
| H7 | Boucle automatique de test d'hypothèses : bout en bout sur 120 épisodes réels, garantie de 5 % de fausses promotions validée, contrôles fatals 0 sur 1 000 |

### 2.5 Les portes
**G0** (au plus tard fin novembre 2026) : huit critères, **deux prouvés** (harnais ; agrégateurs en simulation). **GC** (fin du
mois 2) et **G1** (fin du mois 4 du plan financé, selon la proposition envoyée ; le programme interne dit fin M2, écart signalé) :
la boîte blanche séquentielle bat la meilleure base boîte noire **et** deux bases boîte blanche, au sens d'un rappel à 1 % de
fausses alertes supérieur à 95 % de confiance, **par mode de sabotage**, mode tenu à l'écart compris. L'échec de G1 est
pré-engagé : résultat négatif publié, bascule sur la validité de construit.

### 2.6 La gouvernance
Préenregistrement scellé avant toute expérience décisive ; contre-lecture par une instance qui n'a pas écrit ; verdict de porte
par un tiers qui n'a écrit ni le préenregistrement ni l'analyse ; aucun run visant un signe positif ; symétrie des audits (un
résultat trop propre, positif ou négatif, déclenche le même audit) ; tout chiffre renvoie à un chemin et une empreinte. Côté
sécurité : aucune recette de contournement produite ; deux arrêts de classifieur consignés le 28 octobre, et une règle écrite
sur l'après (un refus appelle une autre question, plus étroite, jamais la même reformulée) ; revue externe avant tout pipeline
adversarial opérationnel ; aucun score de moniteur dans l'entraînement d'un agent.

### 2.7 Demande et calendrier
Le plan financé commence le 1er décembre 2026 (M1). Selon la proposition envoyée : GC fin du mois 2, papier C sur arXiv et G1 fin
du mois 4, papier A et soumission en conférence aux mois 5–6 (NeurIPS 2027, repli ICLR 2028), libération du code au mois 7 ; dans
le scénario ambitieux, le papier B occupe les mois 8 à 12 avec G2 et G3. **Demande** : trois paliers cohérents avec l'envoi —
plancher 58 630 ; scénario ambitieux envoyé 138 600 ; **version la plus ambitieuse ≈ 176 500**, recommandée (couche 5).

---

## Couche 3 — le détail par front

### Front A — Théorie du contrôle des moniteurs

**Question.** Pour chaque moniteur, sous quelles conditions mesurables est-il prouvé aveugle, et laquelle de nos statistiques
reste debout quand plusieurs conditions se cumulent ?

**Acquis.** La carte v1 : lemme maître L0 (invariance, proximité en variation totale, strate, impossibilité), 23 hypothèses
A1 à A23 sur 8 statistiques (11 lignes), 21 lemmes prouvés, 2 esquisses, 1 conjecture. Trois lemmes à dire tels quels :
- **Plafond d'horizon (A7).** Sous un effet d'épisode de part r₀, le rappel de toute statistique contre un décalage constant
  plafonne à Φ(δ/√r₀ − z_α), quel que soit l'horizon. À δ = 0,3 et α = 1 %, le plafond vaut 0,049 si r₀ = 0,2. Regarder plus
  longtemps ne sauve pas un moniteur si les épisodes sont hétérogènes — et r₀ est exactement ce que la mesure T0 du front B lit.
- **Aveuglement par sélection (A18).** Un moniteur qui définit la population « sous le seuil » y est aveugle par construction.
  Plusieurs protocoles publiés de contrôle ont cette forme.
- **Sonde qui ne lit que l'indication (A13).** Contre des négatifs appariés en indication, le rappel égale le taux de fausses
  alertes ; l'aire sous la courbe le cache. C'est la faille de tête des sondes d'intention publiées.

**Méthode et livrables.**
1. **Carte v2 — bornes quantitatives.** Là où v1 donne une invariance (« ne voit rien »), v2 donne une borne (variation totale,
   divergence de Kullback-Leibler) : *de combien* le moniteur est dégradé pour un écart donné. Priorité : A5 (taux de change
   dommage/score), A11 (agrégation sur les jetons), A19 (plancher et confusions).
2. **Matrice « statistique × classe d'écart ».** Pour chaque union de classes, laquelle des 8 statistiques reste non aveugle. C'est
   ce qui rend un **panel** de moniteurs concevable plutôt qu'empirique : on choisit le panel dont aucune union réaliste de classes
   ne couvre toutes les lignes.
3. **Vérification formelle.** Lean comme vérificateur des lemmes ; un lemme vérifié mécaniquement est opposable autrement qu'un
   papier.
4. **Sept questions ouvertes** (A2, A6, A7, A11, A12, A14, A20), chacune avec sa recherche d'antériorité ; chacune est annoncée
   comme question, jamais comme trou du champ (règle anti-faux-gap) ; chacune est un papier court si elle tombe.

**Coût.** Processeur seul. **Risque.** Qu'une question ouverte soit déjà fermée dans la littérature : c'est le résultat attendu
pour une partie d'entre elles, et il se cite.

### Front B — Mesurer ces hypothèses sur des épisodes réels, à coût de calcul nul

**Question.** Les hypothèses de la carte tiennent-elles sur les scores réels d'un agent de 8 milliards de paramètres ?

**Données.** Un fichier de scores déjà payé (`donnees/20261019-230011-p3-reel/scores-p3.npz`, `968414fc…`), issu du premier test
boîte blanche. Aucune lecture avant scellement du préenregistrement ; chaque mesure lue une seule fois.

**Six mesures.**
- **T0 — mesure unanime** : taux de fausses alertes par épisode honnête entier de l'agrégateur séquentiel, et surtout r₀, dont
  dépend le plafond d'horizon. État : treize contre-lectures, version 14 en cours, lecture réelle à lancer.
- **T1 — plafond d'horizon (A7)** : rappel observé contre plafond prédit, à δ ∈ {0,3 ; 0,5}, horizon ∈ {5 ; 7 ; 10}. Prédiction
  signée, réfutation écrite d'avance.
- **T2 — classe d'ordre (A2, A3)** : permutation des actions dans chaque épisode honnête ; garde de code testée sur un artefact
  qui casse la symétrie.
- **T3 — longueur (A9)** ; **T4 — indication et texte (A13, A20)** ; **T5 — plancher (A19)**.

**Pourquoi c'est l'argument le plus fort.** Six résultats préenregistrés, un signe annoncé d'avance, zéro dollar de calcul. C'est
la preuve que le programme est rapide et tolérant à l'échec — une arithmétique, pas une promesse.

**Coût.** Processeur seul. **Risque.** Un résultat « trop propre » : il déclenche le même audit qu'un résultat contraire (R4).

### Front C — Résistance adversariale, et le frein qui va avec

**Question.** Nos moniteurs survivent-ils à un adversaire qui sait qu'ils existent — et comment le mesurer sans construire
d'arme ?

**Neuf voies de mesure** (acceptées le 28 octobre) : concepteurs humains indépendants ; **théorie adversariale du contrôle**
(voie prioritaire : prédire où les failles adaptatives peuvent vivre sans en construire une) ; observation des données
existantes ; adversaire scellé ; adversaire analytique par résolution de contraintes ; audit automatisé à taxonomie fixée ;
transfert adversarial entre domaines ; validation croisée entre moniteurs ; génération adversariale de cas de test sans agent.

**Six classes d'attaque cibles** : stéganographie statistique, conscience d'évaluation, collusion entre agents, sabotage à effet
différé, sabotage mimétique, exploitation de la corrélation temporelle.

**Trois étages d'épreuve** : (1) les systèmes de « scientifique automatique » publiés comme proposeurs candidats ; (2) les bancs
publiés de contournement, d'évasion et de sabotage comme batterie préliminaire ; (3) les modes inédits, conçus par une instance
neuve qui n'a conçu aucun moniteur, scellés avant la porte, révélés à l'évaluation seulement. **État au 28 octobre** : l'étage 3
est déjà conçu (trois proposeurs indépendants, deux convergents, versé sous quarantaine) ; les étages 1 et 2 sont au registre de
gouvernance, au niveau méthode ; leur mise en pipeline opérationnel attend une revue de sécurité externe. Une taxonomie défensive
en quatre familles d'évasion et dix moniteurs candidats existent, cités par pièce, non vérifiés.

**Le frein, et pourquoi il compte devant un fonds de sécurité.**
- **Niveau méthode.** La sortie de tout travail adversarial est : classe d'attaque, mécanisme (quelle hypothèse du moniteur est
  violée), conditions de succès, défense possible. Jamais l'agent concret, la séquence d'actions, le code. Un défenseur corrige
  sa sonde ; un attaquant ne rejoue rien.
- **Deux arrêts réels, consignés** (28 octobre) : la préparation du bras d'attaque, arrêtée par un classifieur de sécurité ; la
  mise en pipeline des deux premiers étages, arrêtée de même. **La règle après un refus** (R-609) : une autre question, plus
  spécifique et moins diffuse, jamais la même reformulée — le travail a repris sous une question défensive plus étroite ; et la
  décision de Lazar (R-611) : tout pipeline opérationnel attend une revue de sécurité externe.
- **Quarantaine.** La sortie adversariale n'est jamais lue par qui conçoit les sondes ; aucun score de moniteur n'entre dans
  l'entraînement d'un agent.
- **Revue de sécurité externe** avant toute exécution de l'adversaire scellé : un évaluateur extérieur vérifie que la procédure
  de sortie n'exfiltre rien de plus que les taux agrégés et la caractérisation au niveau méthode.
- **En cours.** Un collisionneur « évasion et moniteurs » tourne au moment de cette rédaction (rotation de trois triplets, huit
  modèles ; côté défensif : conception de moniteurs et riposte ; côté offensif : au niveau méthode, sous les mêmes règles).

**Coût.** La revue externe est le poste à financer ; le reste est processeur, puis calcul sur devis. **Risque.** Que la revue
externe refuse une partie de l'exécution : c'est le résultat accepté d'avance, et le niveau méthode survit.

### Front D — Les deux papiers qui ne sont pas l'organisme

**Papier C — corruptibilité des moniteurs.** Question : un moniteur peut-il être *persuadé* ? Hypothèses : loi de déférence
(le verdict d'un juge bouge d'une fraction g de l'écart entre ce qu'on lui demande et ce qu'il aurait dit) ; robustesse des
sondes aux attaques par le contenu ; usurpation d'autorité ; taxe de déplacement sous obfuscation des activations ;
contre-mesures (paraphrase de confiance, quorum hétérogène) ; déférence bénigne contre robustesse. Porte GC : si les sondes
cèdent sans accès aux poids, le papier change de titre (contamination de construit), il ne disparaît pas. État :
préenregistrement au brouillon 7 ; 29 papiers voisins lus sur PDF, aucune collision avec la pièce revendiquée ; deux corrections
de méthode trouvées par simulation avant tout scellement ; reste un PDF hors d'arXiv, la contre-lecture, le scellement, un pilote.

**Papier B — l'essaim.** Question : quand le sabotage est réparti entre agents à poids partagés, quelle statistique de population
le voit, et à quel prix pour la diversification ? Hypothèses : statistique spatio-temporelle ; compromis
diversification/coordination ; diversité des moniteurs mesurée par la matrice de transfert d'attaque ; riposte (quatre
politiques comparées) ; **H9**, survie des contraintes de sécurité à la délégation (sous réserve d'antériorité). La collusion
entre agents est aussi une des six classes cibles du front C.

**État de l'art, niveau 2, sur les deux classes neuves** : deux rapports scellés. **Conscience d'évaluation** : zone
semi-occupée — la détection boîte blanche de la tromperie est publiée et forte sur les grands modèles ; le sabotage par
instruction est démontré ; ce qui manque est exactement notre angle. **Collusion entre agents** : zone largement vierge côté boîte
blanche — établie en boîte noire, l'audit textuel en rate l'essentiel, aucun résultat sur les activations ; la question « la
lecture des activations résout-elle intrinsèquement la collusion ? » est ouverte, et vérifiée plus durement parce qu'elle est
séduisante (R8). Aucune zone revendiquée trouvée occupée en entier.

### Front E — Le pôle scientifique automatique

**Question.** L'organisme surveillé est un agent qui fait de la recherche ; sa conception est une question de recherche : comment
compose-t-on un chercheur automatique dont on peut mesurer ce qu'il apprend, ce qu'il coûte et ce qu'il cache ? **Décidé** :
universalité mesurée sur des familles de tâches inédites, vivier de conception, tâches fraîches par génération ; composition
apprise (modèle par rôle, coût dans le signal, frontière entre rôles mesurée, voies bon marché d'abord, héritage d'une génération
récompensé) ; test final lu une seule fois ; contre-lecteur d'un autre modèle ; juge d'une autre lignée ; aucun score de moniteur
dans l'entraînement de l'agent. **Existe** : la boucle de bout en bout (H7) ; deux lancements réels ; un duel des proposeurs sous
GO, à relancer ; une banque des deux modes connus sous GO. **Rapporte** : le critère 2 de G0, les organismes de G1 par mode, les
proposeurs de l'étage 1 du front C, et un objet neuf pour le champ — un chercheur automatique dont la composition est apprise et
mesurée. **Coût** : appels de modèles surtout (les pilotes d'octobre : ≈ 156 USD), carte graphique pour les organismes à poids.

---

## Couche 4 — gouvernance et portes

### 4.1 Les règles gelées, en clair
- **Préenregistrement scellé** (hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse, critères de lecture,
  liste d'arrêt) avant toute expérience décisive, simulation comprise ; aucune lecture avant scellement.
- **Contre-lecture** par une instance neuve qui n'a pas écrit le préenregistrement, d'un autre modèle que l'auteur.
- **Aucun run visant un signe positif.**
- **Symétrie** : un résultat suspect de propreté, positif ou négatif, déclenche le même audit.
- **Gardes testées** sur un cas sain et sur un artefact ; aucun repli silencieux.
- **Traçabilité** : tout chiffre renvoie à un chemin et une empreinte ; aucun chiffre de l'état de l'art sans vérification sur le
  PDF, page citée.
- **Anti-faux-gap** : une zone vierge est une question, pas un trou du champ ; les zones vierges séduisantes sont vérifiées plus
  durement.
- **Verdict de porte** par une instance neuve, ni auteur du préenregistrement ni de l'analyse, qui applique les critères gelés ;
  scellé, puis soumis à Lazar.
- **Jamais de moyenne ni de médiane sur les jetons** dans une sonde de production (évadables par apprentissage sur les poids ;
  le maximum et l'attention résistent).

### 4.2 G0 — huit critères, état au 28 octobre
Harnais validé (**prouvé**) ; organismes à dose-réponse ; sondes au-dessus du plancher ; base boîte noire opérationnelle ;
agrégateurs validés en simulation (**prouvé**) ; préenregistrement de G1 scellé et contre-lu ; préenregistrement du papier C
scellé et contre-lu ; état de l'art vérifié. Deux sur huit. Échéance : au plus tard fin novembre 2026.

### 4.3 G1 (fin du mois 4 selon l'envoi) — ce qu'elle exigera, écrit d'avance
1. **Critère** : la boîte blanche séquentielle bat la **meilleure base boîte noire** (toutes variantes confondues) **et** les
   **deux bases boîte blanche** — cascade de portes sur les mêmes sondes ; sonde sur le dernier état — au sens d'un **rappel à
   1 % de fausses alertes supérieur, à 95 % de confiance**. Le score F1 est retiré du critère.
2. **Par mode** : rapportée par mode de sabotage ; gain exigé dans chaque mode ; bras génériques et spécialisés séparés. On ne
   cache pas un échec sur un mode dans une moyenne.
3. **Mode tenu à l'écart** : conçu par une instance qui n'a conçu aucun moniteur, scellé avant G1, révélé à l'évaluation. C'est
   le test honnête de la généralisation.
4. **Échec pré-engagé** : résultat négatif publié ; la validité de construit (ce que la sonde mesure vraiment prédit sa
   robustesse) devient l'hypothèse dominante.

### 4.4 Les autres portes
**GC** (fin M2) : si les sondes cèdent à la persuasion sans accès aux poids, le papier C devient « contamination de construit ».
**G2** (fin M4) : effet de fragmentation répliqué et statistique de population supérieure à l'agrégation par agent ; sinon,
recentrage sur le temporel à un agent. **G3** : ouverture de l'environnement de curation de données seulement si un indicateur
de vérité différée est validé.

### 4.5 Le frein de sécurité
Sortie au niveau méthode, jamais la recette ; deux arrêts de classifieur consignés le 28 octobre ; après un refus, une autre
question plus spécifique, jamais la même reformulée (R-609) ; quarantaine entre la sortie adversariale et la conception des
moniteurs ; revue de sécurité externe avant tout pipeline adversarial opérationnel (R-611) ; aucun score de moniteur dans
l'entraînement d'un agent.

### 4.6 Ce qui se dit à l'entretien, et ce qui ne se dit pas
**Se dit** : la taxonomie défensive au niveau méthode (classe, mécanisme, conditions, défense) et la réponse du programme à
chaque classe d'écart, questions ouvertes comprises. **Ne se dit pas** : les recettes ; les candidats-moniteurs non vérifiés
présentés comme résultats ; le contenu offensif qui attend la revue externe ; la carte des hypothèses elle-même (pièce
confidentielle : ses trois lemmes se disent, la carte ne se transmet pas sans GO).

---

## Couche 5 — calendrier et budget

### 5.1 Calendrier
| période | contenu | porte |
|---|---|---|
| M0 (5 octobre → fin novembre 2026) | Phase 0 : instruments ; fronts A et B avancent sans calcul | **G0** |
| M1 (décembre 2026) | Clore G0 ; papier C : déférence des juges (HC1), sondes sous attaque (HC2, HC2b) ; papier A : organismes et dose-réponse | **G0** |
| M2 (janvier 2027) | Papier C : usurpation (HC3), taxe de déplacement (HC4) ; papier A : plan 2 × 2 | **GC** |
| M3 | Papier C : contre-mesures (HC5), test d'acceptation (HC6) ; papier A : lemme et théorème sur activations réelles | |
| M4 | Rédaction du papier C ; papier A : plan 2 × 2 complet | papier C sur arXiv ; **G1** |
| M5–M6 | Papier A : attaques adaptatives (contenu, puis réglage fin et renforcement), interventions (H6), validité et robustesse (H8) ; rédaction | papier A sur arXiv ; soumission (NeurIPS 2027, repli ICLR 2028) |
| M7 | Libération du code, des organismes, des sondes et des préenregistrements ; rapport final | |
| M8–M12 (scénario ambitieux et au-delà) | Papier B : division du travail, collusion contre coordination par poids, statistiques inter-agents, spatio-temporel, diversification, riposte | **G2**, **G3** |

En parallèle, dès M0 et sans calcul : carte v2, matrice, vérification formelle (front A) ; mesures T0 à T5 (front B) ; pôle
(front E) sur devis. (Le programme interne place G1 et GC fin M2 ; la version envoyée fait foi devant le fonds.)

### 5.2 Budget — tranché : option (c), version la plus ambitieuse
La candidature envoyée (7 octobre) demande **58 630 USD** pour sept mois et décrit un **scénario ambitieux à 138 600** (douze mois,
papier B, organismes de 70 milliards, seconde famille de modèles, attaques par renforcement, consultant en statistique, ingénieur
à mi-temps). Lazar a tranché l'option (c) — la demande telle qu'envoyée, plus une extension nommée et chiffrée — et demandé la
version la plus ambitieuse : l'extension s'ajoute au scénario ambitieux.

| palier | montant | ce qu'il finance |
|---|---|---|
| plancher, tel qu'envoyé | 58 630 | papiers C et A, sept mois, porte G0 |
| scénario ambitieux, tel qu'envoyé | 138 600 | + papier B, douze mois, réplication, attaques par renforcement, consultant, ingénieur |
| **version la plus ambitieuse** | **≈ 176 550** | + revue de sécurité externe 7 500 ; adversaire scellé sous revue 4 000 ; matrice complète et vérification formelle 5 000 ; pôle scientifique automatique 12 000 ; collisionneur multi-modèles 6 000 ; réserve 3 450 |

Détail et hypothèses de calcul : `demande-option-c-ventilation-v2.md` (`8ab00ab5…`). Restent à Lazar : le taux de la revue externe ;
présenter trois paliers ou deux ; confirmer la lecture « extension sur le scénario ambitieux ».

---

## Couche 6 — pièces, provenance, réserves

### 6.1 Pièces
| affirmation | pièce | empreinte |
|---|---|---|
| 31 prédictions sur 31 en simulation | run `20261004-080257-t03` ; `docs/notes/resultats-T0.3-v1.md` | préenregistrement `7474743a…` |
| harnais validé, critère 1 de G0 | `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` | `63444faa…` |
| 180 épisodes réels, banc reconstruit | `diag/20261007-082440-t05-extraction/` | bilan d'extraction |
| 3 497 citations contrôlées, 0 échec | `docs/sources/lecture-pdf-niveau2/` ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md` | `bbe0c1f5…` |
| premier test boîte blanche nul, puissance chiffrée | `docs/verdicts/verdict-P3-premier-test-i-a-v1.md`, `-v2.md` | `0c8ecbdf…`, `05e896da…` |
| carte des hypothèses (23, L0, 21 lemmes, 7 ouvertes) | `carte-des-hypotheses-v1.md` (confidentielle) | `f7dfe5fd…` |
| boucle automatique bout en bout | en-tête du dossier du fonds, tableau de provenance | voir `en-tete-programme-v2-fonds-v1.md` |
| scores déjà payés du front B | `donnees/20261019-230011-p3-reel/scores-p3.npz` | `968414fc…` |
| critère de G1 sans F1 | `docs/decisions/decision-N-007-N-008-v1.md` | |
| G1 par mode, mode tenu à l'écart | N-054 (`registres/decisions.md`, R-514) | |
| deux bases boîte blanche, traits internes | N-056 (`registres/decisions.md`) | |
| programme d'entretien v4 (source de ce document) | `brouillons/entretien-taif-v2/programme-entretien-taif-v4.md` | `8dbacfe5…` |
| programme qui fait foi | `docs/programme-controle-ia-v2.md` | `2fd63bad…` |
| candidature envoyée : proposition v2, formulaire, budget v3 (7 octobre) | reçus de Lazar le 28 octobre | `737c482c…`, `76cdbb3b…`, `037765b0…` |
| dépenses réconciliées au 28 octobre (≈ 450 USD connus, ± 15 %) | `docs/notes/depenses-cumul-2026-10-28-v1.md` (sur `main`) | `93969946…` |
| taxonomie des quatre familles et réponse du programme ; dix moniteurs candidats | `docs/notes/programme-et-4-familles-evasion/…-v1.md` ; `…/sous-agents-defensifs/EMPREINTES-v1.txt` (sur `main`) | `d13bc425…` |
| ventilation de la demande, version la plus ambitieuse | `brouillons/entretien-taif-v2/demande-option-c-ventilation-v2.md` | `8ab00ab5…` |
| arbre des expériences et des décisions en couches | `brouillons/entretien-taif-v2/arbre-experiences-et-decisions-en-couches-v1.md` | `aacc5591…` |

### 6.2 Réserves
1. **Chiffre tiers.** « 95–99 % de rappel à 1 % de fausses alertes sur un modèle de 70 milliards » (détection boîte blanche de la
   tromperie, littérature) relève de R7 : il **ne se cite pas comme opposable** sans vérification de la page du PDF. Formulation
   sûre, employée ici : « forte sur les grands modèles », sans chiffre.
2. **Dépense cumulée.** Réconciliée par session-depot le 28 octobre : ≈ 450 USD connus (carte graphique sous GO ≈ 95, dont phase 0
   stricte ≈ 70 ; appels de modèles ≈ 353), ± 15 %, hors la facturation jamais relue de la relève du 23 octobre (13 instances sans
   GO ; ≥ 6 visibles, plan annoncé 468) — à lire par Lazar sur la console. La candidature envoyée disait « about $20 » au 7 octobre :
   l'écart s'assume tel quel. Dire « a few hundred dollars », pas un nombre, tant que l'export de facturation n'est pas rapproché.
3. **Date de l'appel** : non consignée dans les registres ; à vérifier auprès de Lazar.
4. **Non contre-lu.** Ce document n'est pas contre-lu. S'il doit servir hors du dépôt, un sous-agent neuf d'un autre modèle le
   contre-lit (R2) ; je le propose en une heure.
5. **Modèle servant.** L'attribution déclarée par l'environnement a varié dans la session (Opus 4.6, 4.8, 5, 5.5, Fable 5.1) ;
   ce document est écrit sous l'attribution « Fable 5.1 » telle que déclarée au moment de l'écriture ; l'auteur désigné du
   travail principal reste Opus 4.6 par décision de Lazar. Sans effet sur le contenu, consigné par honnêteté.
6. **Rien de neuf.** Ce document n'ajoute aucune hypothèse, aucun chiffre, aucune décision au programme d'entretien v4 ; il le
   met en couches. Toute divergence entre les deux est une erreur de ce document, et la v4 prime.
7. **Calendrier.** La proposition envoyée place G1 fin du mois 4 ; le programme interne dit fin M2 ; devant le fonds, l'envoi fait
   foi ; mettre le programme en accord est le geste de Lazar.
8. **Lecture de « la version la plus ambitieuse ».** Retenue comme « extension sur le scénario ambitieux envoyé » ; un mot de Lazar
   si c'était autre chose.
