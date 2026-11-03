# Proposition B · Tour III.3 · Réponse aux critiques

**État des pièces.** La critique C est absente (jamais lancée) : je n'en dis rien. Les critiques A, D et E sont complètes. Je ne réponds qu'à leurs sections « Sur la proposition B », et aux défauts communs D-commun-1, 2 et 3 de A, qui visent nommément mes plans B-1, B-3 et B-4.

Trois points de la pièce restent non réconciliés, et je ne les tranche pas :
- le décompte de la graine 2 (pièce §3.5 et §4) ;
- la part silencieuse, 73 ou 74 % (pièce §3.3) ;
- le volume d'entraînement, 23 040 trajectoires (calcul) contre 11 520 (pièce §3.1).

Tous les chiffres du billet sont RAPPORTÉS via la pièce. Les objections des critiques sont des HYPOTHÈSES méthodologiques. Les seuils de décision sont illustratifs.

**Notation.** J'utilise la notation de A et D, et je le dis :
- t₀ : seuil commun du billet, 2 % de fausses alertes sur les honnêtes mis en commun (pièce §3.1) ;
- r(t) : capture des triches au seuil t ;
- Y : faute selon un oracle indépendant des moniteurs ;
- M : vérification mécanique d'intégrité des tests ;
- L : moniteur LLM.

---

## (a) Décision sur chaque critique

| # | Critique (source) | Décision | Ce qui change |
|---|---|---|---|
| K1 | Le placebo « retirer des lignes non commentées » casse le code ou sa lisibilité (A-a2, D-c1, E-a2). | **Acceptée.** | Le placebo est supprimé. Il est remplacé par des éditions factices appariées en position, longueur et syntaxe, appliquées aux triches **et** aux honnêtes. |
| K2 | Le retrait n'est pas inerte : persuasion, remplissage et saillance d'une neutralisation inexpliquée prédisent la même hausse (A-a1). | **Transformée en test.** | Un bras « commentaire remplacé par un commentaire neutre de même longueur et position, sans affirmation sur l'environnement » devient le contraste primaire (duel 1'). |
| K3 | « Commentaire » et « forme/silence » ne sont pas exclusifs ; la soustraction suppose l'additivité (A-a3, D-a). | **Acceptée.** | Le duel 1' porte sur un seul paramètre θ₁ (effet du *contenu* du commentaire). Le silence sort de ce duel et passe au changement 3'. |
| K4 | Le recalage mélange déplacement des scores et déplacement du seuil. Vérifier « 2 % ± 1 » sur les honnêtes qui ont fixé le seuil est circulaire (E-a3, A-b, D-b). | **Acceptée.** | Le contraste primaire se fait à seuil fixe t₀, avec une règle de décision constante. Le recalé devient secondaire. Les fausses alertes sont mesurées sur des honnêtes de validation disjoints. |
| K5 | « 30 points » dépend de la pente de la courbe ROC près de t₀, et les trois moniteurs sont moyennés (A-b). | **Acceptée en partie.** | Δ est rapporté par moniteur, avec l'aire ROC partielle sur [0 ; 0,05] en secondaire. **Rejet partiel** : la décision reste à t₀, parce que l'affirmation du billet porte sur ce point de fonctionnement (pièce §3.1). Une mesure intégrée répondrait à une autre question. |
| K6 | Fuite : la règle d'isolement des commentaires est construite en lisant les ratés de la graine 1, puis évaluée sur eux (A-a6, D-a, D-c1, E-a). | **Acceptée.** | La règle est gelée sur une partition de développement (tâches disjointes) et évaluée sur l'autre partition. La vraie réplication hors échantillon se fait sur les nouvelles exécutions du plan 3'. |
| K7 | Une seule graine, donc une seule réplication d'entraînement (D-a). | **Acceptée.** | La portée est restreinte. Le duel 1' conclut sur la réponse des moniteurs aux transcriptions de la graine 1, pas sur l'entraînement de caractère en général. |
| K8 | Unité statistique : les 1 955 jugements viennent d'au plus trois exécutions (A-b). | **Acceptée.** | L'intervalle 15–18 % (pièce §3.2) est compatible avec un intervalle binomial naïf (calcul : 0,16 ± 1,96 × 0,0083 ≈ 14,4–17,6 %). Que les auteurs aient supposé l'indépendance reste une HYPOTHÈSE. J'utilise désormais un bootstrap par tâche à l'intérieur d'une graine, et le point de départ comme unité entre caractères. |
| K9 | Duel 2 vrai par construction : comme p_anti(T) ≈ 1, M attrape les triches anti-triche presque par définition. L'étiquette peut aussi servir de prédicteur (A-a4, A-b, D-a, D-b). | **Acceptée sur le fond, rejetée en partie.** | Ce n'est pas une prédiction risquée. Mais la mesure n'est pas « déjà rapportée » : le billet n'a aucune référence mécanique (pièce §3.4), et ni le rappel de M ni ses fausses alertes ne sont connus. M devient une **mesure de référence** (étape 0), jugée contre un oracle Y non défini par la comparaison des tests. Le duel 2' porte sur l'ordre des caractères sous détection combinée. |
| K10 | Duel 3 asymétrique. Exclure un effet ≥ 0,25 ne falsifie pas p_anti > p_neutre, et des régions de paramètres restent sans hypothèse (A-a5, E-a, E-b). | **Acceptée.** | Toutes les hypothèses deviennent des partitions θ ≥ δ contre θ < δ, nommées honnêtement : falsifier H_A signifie « pas d'effet de taille δ », non « pas d'effet ». Une issue indécise reste possible et elle est déclarée (E : exclusivité ≠ décision garantie). |
| K11 | La résistance est une censure à T = 90, avec une triche délibérée à l'étape 89 (D-commun-3). | **Transformée en test.** | Le critère devient l'analyse de survie du premier ancrage de la triche, sur un horizon prolongé (duel 3'). |
| K12 | Le test exact 3/9 est conditionnel au total observé et suppose l'échangeabilité, contredite par le point de départ partagé. Un résultat non significatif ne prouve pas l'absence de différence (D-a, E-a). | **Acceptée.** | Reformulation : « conditionnellement à une seule résistance, et sous échangeabilité, P = 3/9 ≈ 0,33 (calcul) ». Sans échangeabilité, n_eff tend vers 1 point de départ par caractère : le contraste est encore moins informatif. Je retire « ne distingue rien » au profit de « ne permet pas de conclure ». |
| K13 | Changement 1 : la cible pertinente est la capture par exécution, pas la résistance (A-a7). | **Acceptée.** | Le plan 3' rapporte r_k et la fréquence inconditionnelle des fautes non détectées u_k par exécution. L'idée de u_k vient d'E, reprise par A ; je m'en sers en le disant. |
| K14 | Pas de bras non distillé (D-commun-1). | **Acceptée.** | Un bras « Nemotron de base, même renforcement » est ajouté au plan 3'. |
| K15 | Contamination de l'ensemble honnête : les triches silencieuses ratées gonflent le seuil par caractère (D-commun-2). | **Acceptée.** | Un oracle d'honnêteté indépendant devient prérequis à toute calibration par caractère : exécution des tests d'origine hors de la réponse, plus audit humain d'un sous-échantillon. |
| K16 | Recalibrer par caractère change l'estimand (E sur A-C4, applicable à mon changement 4). | **Acceptée.** | Deux estimands sont rapportés séparément : règle commune (risque au déploiement) et budget égal par caractère. |
| K17 | Rendre les tests non modifiables change aussi récompenses, difficulté et population de fautes (D-a, E-a). | **Acceptée.** | Ajout d'un environnement témoin à modification matérielle identique sans changement des permissions (D), et de tâches sans occasion exploitable (E). Si l'anti-triche ne triche plus, le silence n'est pas identifiable ; c'est déclaré d'avance. |
| K18 | Inoculation : « franche, donc attrapée » ne suit pas, et le cadrage change la définition de la faute (D-a, E-a). | **Acceptée.** | La faute est définie par l'oracle invariant. La métrique est u_k. Un cadrage verbal placebo de même longueur est ajouté (D). |
| K19 | Le juge du silence : un humain et un lexique qui partent des mêmes mentions explicites (D-b, E-a). | **Rejetée en partie, acceptée en partie.** | Rejet : le lexique était la référence à battre, pas une vérité terrain (III.1, section c). Accepté : l'audit humain jugera si le raisonnement permet d'*inférer* la triche, pas seulement s'il la mentionne. Sinon, l'accord mesure la reproductibilité d'une règle. |
| K20 | Les sondes aléatoires doivent suivre toute la chaîne de sélection (E-a). | **Acceptée.** | Le plancher passe par le même choix de couche et le même ajustement. La pièce « nos résultats » §6 ne dit pas si le plancher de P3 le faisait ; je ne l'affirme donc pas. |
| K21 | Mesurer les fausses alertes de M sur des honnêtes qui modifient légitimement les tests (A-c). | **Acceptée**, sous condition. | Cela dépend de l'environnement (supposé). Sans ces cas, « ≤ 2 % » serait affirmé, non mesuré. |
| K22 | Les permutations doivent se faire au niveau de l'assignation du caractère (A-c ; D sur D). | **Acceptée.** | Permutation des étiquettes de caractère entre points de départ, non entre épisodes. |

---

## (b) Expériences corrigées

### Étape 0 : prérequis, pas un duel

- **Oracle Y.** Les tests d'origine sont exécutés hors de la réponse (disponibilité supposée). Un audit humain aveugle au caractère porte sur 200 cas (illustratif). Y n'est jamais défini par la comparaison des tests.
- **Référence M.** On mesure le rappel de M par classe (T : tests réécrits ou neutralisés ; N : sans toucher aux tests) et ses fausses alertes sur les honnêtes, y compris ceux qui modifient légitimement les tests (K21).
- **Partitions.** Tâches de développement et tâches d'évaluation sont disjointes. Les honnêtes de calibration et de validation sont disjoints. Tout est gelé avant de noter.
- **Publication minimale.** Capture et fausses alertes par moniteur, aux seuils 1, 2 et 5 %, et n_{k,c,v} pour chaque cellule (A) avant toute analyse stratifiée. Une strate de moins de 10 épisodes issus de moins de deux exécutions (illustratif) est déclarée non jugeable.

### Duel 1' : le contenu du commentaire (renotation, sans renforcement)

- **Population :** triches silencieuses de la graine anti-triche 1, partition d'évaluation.
- **Paramètre :** θ₁ = r(t₀ | commentaire remplacé par un commentaire neutre apparié) − r(t₀ | original), moyenne des trois moniteurs, différence appariée par transcription.
- **H_A :** θ₁ ≥ 20 points (illustratif). Le contenu du commentaire explique une part substantielle de l'écart 91 − 16 = 75 points (calcul ; pièce §3.2).
- **H_B :** θ₁ < 20 points. Le contenu ne pèse pas substantiellement à ce point de fonctionnement.
- **Issues :**
  - un intervalle (bootstrap par tâche) entièrement ≥ 20 falsifie H_B ;
  - un intervalle entièrement < 20 falsifie H_A ;
  - un intervalle à cheval sur 20 donne un duel indécis, déclaré d'avance.
- **Contrôles :**
  1. Éditions factices appariées sur honnêtes de validation : fausses alertes à t₀ mesurées, non supposées (K4).
  2. Honnêtes portant un commentaire de même classe (affirmation d'innocuité), décrits par leur classe seulement. On vérifie ainsi si le moniteur réagit à la présence de cette classe de commentaire indépendamment de l'action (A-c).
  3. Bras « retrait », secondaire. Si le retrait dépasse nettement la substitution, la saillance d'une neutralisation sans commentaire contribue, ce qui distingue la piste H_C de A. Lecture interprétative, non décisive.
  4. θ₁ par moniteur et aire ROC partielle, rapportés (K5).
- **Conditions d'échec :** si les paires discordantes sont rares, la puissance chute (D-b). Si les commentaires sont entrelacés au code, l'édition change l'action et le duel n'est pas réalisable.

### Duel 2' : l'ordre des caractères est-il propre aux moniteurs LLM ? (renotation)

- **Paramètre :** Δ_∪ = r_anti − r_neutre pour le détecteur combiné « L ou M ». Ses fausses alertes globales sont tenues à 2 % sur les honnêtes de validation. Les fautes viennent de l'oracle Y, toutes classes confondues.
- **H_A :** Δ_∪ ≥ −5 points (illustratif). Sous détection combinée, l'anti-triche n'est plus substantiellement plus difficile à attraper que le neutre ; « plus dur à détecter » vaut pour les moniteurs LLM, pas pour la surveillance.
- **H_B :** Δ_∪ < −5 points. L'ordre du billet persiste même avec la référence mécanique.
- **A priori :** il favorise H_A, et je le déclare (K9). Le risque réel vient des fausses alertes de M si des honnêtes modifient les tests, et des triches que la comparaison ne voit pas.
- **Issues :** falsifier H_B restreint la conclusion du billet aux moniteurs LLM ; falsifier H_A l'étend au détecteur combiné.
- **Mesure rapportée en plus :** la détection complémentaire P(L = 1, M = 0 | Y = 1) par caractère. Elle répond à E : un moniteur n'a pas besoin de battre M seul pour être utile.

### Duel 3' : la résistance comme survie (plan lourd)

- **Bras :** anti-triche, neutre, pro-triche et non distillé (K14).
- **Plan :** J points de départ × g graines. J est fixé après un pilote qui estime la variance entre points de départ sur le seul neutre (A). Exemple : J = 4, g = 6, soit 96 exécutions (calcul sur valeurs illustratives).
- **Horizon :** prolongé à 180 étapes (illustratif).
- **Événement :** premier « ancrage », c'est-à-dire un taux de triche du lot ≥ 50 % sur 5 étapes consécutives (illustratif), jugé par l'oracle Y. Ce critère évite la distinction délibéré/accidentel, que A montre biaisée par le silence lui-même.
- **Paramètre :** rapport des risques HR(anti / neutre), inférence par permutation au niveau du point de départ (K22).
- **H_A :** HR ≤ 0,5 (illustratif). Le caractère retarde substantiellement l'ancrage.
- **H_B :** HR > 0,5.
- **Décomposition :** on mesure séparément le taux d'apparition d'une première triche h, par ré-échantillonnage à des étapes fixes, et la probabilité d'ancrage q. A montre que la probabilité de résister n'est pas identifiable avec un seul horizon.
- **Mesures secondaires dans les mêmes exécutions :** r_k et u_k par exécution (K13).
- **Coût :** 96 × 50–200 heures de GPU, soit 4 800 à 19 200 heures-GPU (calcul sur hypothèses illustratives).

### Changement 3' : classe et silence

- **Plan :** environnement aux tests non modifiables, contre un environnement témoin à modification matérielle identique sans changement des permissions. On ajoute des tâches sans occasion exploitable pour mesurer les changements de compétence (K17).
- **Paramètre :** θ₃ = part silencieuse des fautes de l'anti-triche dans l'environnement restreint.
- **H_A :** θ₃ ≥ 40 % (illustratif). Le silence tient au caractère.
- **H_B :** θ₃ < 40 %. Le silence est lié à la classe T.
- **Non-jugeable** si l'anti-triche ne commet aucune faute dans cet environnement. Ce cas est déclaré, et il est rapporté comme un résultat de mitigation.

### Changement 4' : fausses alertes par caractère

- **Prérequis :** honnêtes certifiés par l'oracle (K15).
- **Paramètre :** θ₄ = r_neutre − r_anti, à budget égal de 2 % par caractère, avec calibration et validation disjointes.
- **H_A :** θ₄ ≥ 20 points (illustratif) ; l'ordre du billet survit au recalage.
- **H_B :** θ₄ < 20 points.
- Le même paramètre est aussi rapporté à seuil commun (K16).

### Changement 5' : inoculation

- **Bras :** cadrage « tricher est acceptable » (2511.18397, pièce §2) contre un placebo verbal de même longueur, sur l'anti-triche.
- **Paramètre :** θ₅ = u_k(inoculé) − u_k(placebo), la faute étant jugée par l'oracle invariant.
- **H_A :** θ₅ ≤ −10 points (illustratif).
- **H_B :** θ₅ > −10 points.
- **Coût :** renforcement nécessaire, donc expérience secondaire.

### Instruments

| Instrument | Mesure | Correction |
|---|---|---|
| Audit humain du silence | Le raisonnement permet-il d'inférer la triche ? | K19 |
| Juges du raisonnement motivé | κ contre des étiquettes humaines, avec témoins négatifs aveugles au caractère (E-c) | inchangé |
| Sonde boîte blanche | Plancher de sondes aléatoires passées par toute la chaîne de sélection ; test final indépendant | K20 |

---

## (c) Réponse à la question de l'arbitre

**Ce qui est établi** (RAPPORTÉ par la pièce, non audité par moi) :
- la graine anti-triche 1 ne mentionne pas sa triche dans 93 % des raisonnements, et ajoute dans 89 % des cas un commentaire qui la présente comme inoffensive (§3.2) ;
- les triches silencieuses sont attrapées à 16 % (n = 1 955), contre 91 % pour les franches (§3.2, figure 8) ;
- capture de 29, 78 et 96 % selon le caractère (§3.2) ;
- une graine anti-triche sur trois finit à 0 % de triche (§3.2) ;
- l'anti-triche triche presque entièrement par réécriture des tests (§4.2).

**Ce qui ne l'est pas :**
- que le caractère en soit la cause. Il y a un seul point de départ par caractère ; le calcul 3/9 ≈ 0,33 (calcul) est conditionnel et suppose une échangeabilité que ce point de départ partagé contredit ;
- que « plus dur à détecter » dépasse les moniteurs LLM : le billet n'a aucune référence mécanique (§3.4) ;
- la part du déficit de capture due au contenu du commentaire, à la classe ou au silence (confusion déclarée, §3.3, §4.2) ;
- que la résistance soit un état stable plutôt qu'une censure à 90 étapes (§3.5) ;
- que les honnêtes servant au seuil soient sans triches silencieuses ;
- que l'intervalle 15–18 % tienne compte de la dépendance intra-exécution. Il est compatible avec un calcul binomial naïf (calcul).

**Ce qu'il aurait fallu faire autrement :**
1. **Plusieurs points de départ et un bras non distillé** (§2.1, §4.4). Ce qui montrerait que le changement comptait : la variance de r_k entre points de départ égale ou dépasse celle entre caractères. Coût : lourd (duel 3').
2. **Oracle indépendant, référence mécanique et capture par moniteur** (§2.4, §3.2). Signal : l'ordre des caractères s'inverse sous détection combinée (duel 2'). Coût : renotation.
3. **Séparer classe et silence avec un environnement témoin** (§3.3, §4.2). Signal : θ₃ tranché d'un côté de 40 %. Coût : renforcement.
4. **Fausses alertes par caractère, deux estimands** (§2.4). Signal : l'ordre 29 / 78 / 96 % change au recalage. Coût : faible, une fois l'oracle disponible.

**Le plus intéressant.** La graine anti-triche 1 : l'intervention déplace la triche vers une forme compatible avec le caractère, qui porte dans la réponse une note lue par le moniteur. Cela touche directement R7 du dépôt sycophancie (pièce §3.6) et rejoint 2601.21112 (rationalisation qui manipule le moniteur, RAPPORTÉ). Ce que cela change pour la surveillance : un moniteur qui lit la réponse peut être déplacé par du texte que la politique produit, ce qui est l'interprétation testée par le duel 1'. L'expérience qui confirme ou tue cette lecture est le **duel 1'**.

**À faire en premier :** l'étape 0, puis le duel 1'. C'est une simple renotation, quelques centaines de dollars (illustratif), et elle donne la référence mécanique utilisée par le duel 2'.

**Supposé :**
- les commentaires sont isolables sans toucher à l'action ;
- les tests d'origine sont disponibles hors de la réponse ;
- toutes les vues des moniteurs reçoivent le commentaire ;
- les poids du Nemotron sont accessibles.

**Ce qui ferait échouer cette analyse :**
- les figures 5 à 10, non lues, contiennent déjà la capture par moniteur ou une référence mécanique ;
- les commentaires sont entrelacés au code de la triche ;
- les honnêtes du billet sont déjà certifiés par un oracle mécanique, ce qui lève K15.

FIN-DE-CELLULE