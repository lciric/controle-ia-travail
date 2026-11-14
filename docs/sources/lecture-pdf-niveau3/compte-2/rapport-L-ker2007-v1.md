# Antériorité du lemme d'additivité « L » — la lettre de Ker (2007) — v1

- Début du travail : 2026-11-14 06:58:07 UTC. Ce fichier est écrit le 2026-11-14 07:00:57 UTC. Les deux heures ont été relevées par `date -u`, la seconde dans la commande qui écrit ce fichier.
- **Lecteur : modèle A.** J'ai aussi écrit les rapports L du lot 8 (v1, v2) et des voisins (v1, v2) : `rapport-L-voisins-v2.md` (`649f471e…`) et ses prédécesseurs. Aucun de ces rapports n'est modifié. Le présent rapport est neuf : il complète `rapport-L-voisins-v2.md` sur une pièce que ce rapport nommait sans l'avoir lue (priorité 1).
- Consigne : `consigne-lecteur-compte-2-v1.md` (`cb0623c4…`).
- Vérification avant écriture : un `ls` du seul dossier `compte-2/` a montré qu'il n'existait ni `rapport-L-ker2007-v1.md` ni `fichiers-de-travail-L-ker2007-v1.tar`.
- Pièce lue : `…/scratchpad/pieces-main-complement-v2/ker-2007-capacite-steganographie-par-lots/ker-2007-capacity-result-batch-steganography.pdf`. Elle fait 4 pages. Son sha256 est `73113e2de45bf7b9dd93350238b07a2c45f00d29f62b2be1457d042ce2dd98e9`, égal à celui de son compagnon `.sha256`.
- **Citations contrôlées par programme : 40 citations, 0 échec.**
  - Le script `controle_citations_ker2007_v1.py` est le même code que pour les voisins.
  - Avant le contrôle complet, je l'ai essayé sur un cas juste (réussi) et sur deux cas altérés (refusés).
  - Au premier passage du contrôle complet, une citation a échoué (J22, phrase coupée en fin de ligne). Je l'ai corrigée ; le journal garde la trace.
  - Les citations sont dans `citations-L-ker2007-v1.json`, qui se trouve dans l'archive seulement (sha256 `866c938917f499188ae66eac90d6a0df3f80f9d71faffc086bdc0a721847624a`).
  - Tout extrait anglais entre « », titres compris, est une citation contrôlée suivie de [Jn].
- Les formules, absentes du texte extrait, ont été lues sur l'image des pages. Elles sont marquées « lu sur le PDF, non contrôlé par programme ».
- Les chiffres portent leur nature : « auteurs » ou « calcul ».

## Fichiers lus et étendue

1. La pièce, en entier, en deux passes :
   - ses 4 pages en texte brut, ligne à ligne ;
   - ses 4 pages en image, pour les formules et la figure 1, que le texte extrait ne rend pas.
2. Rien d'autre n'a été ouvert. Les rapports antérieurs cités le sont de mémoire de mes propres écrits, par leurs empreintes.

Aucune ouverture fautive, aucune commande git, aucun réseau, aucun appel de modèle, aucune recherche récursive dans le dépôt, aucune suppression. Aucun refus.

## 0. En tête

1. **Aucune composante revendiquée de L n'est occupée davantage qu'après Ker 2006.** La lettre ne parle pas de la statistique moyenne. Elle ne démontre donc pas l'invariance que Ker 2006 donnait comme immédiate. Le cœur de L1 reste « occupé en partie », par Ker 2006 seul.
2. **La lettre démontre la loi de la racine carrée de la capacité d'un lot**, ce que Ker 2006 ne faisait que conjecturer : « It was conjectured that, given covers of uniform capacity and a quantitative steganalysis method satisfying certain assumptions, » [J6] ; « capacity is proportional only to the square root of the number of covers. We now prove that, with respect to a natural definition of secure capacity, and in a suitably asymptotic sense, this conjecture is true. » [J7] (p. 1). Elle le fait en ordre asymptotique, sans constante : « we are only able to determine capacity a) asymptotically and b) without regard to the multiplicative constant of » [J22] (p. 2).
   - **Hypothèses du théorème 1** : « Theorem 1 (Batch Steganographic Capacity): Suppose the shift hypothesis (1) and that the error density » [J40] (p. 2).
     - hypothèse de pur décalage : « We further assume that the estimation error distribution does not depend on the true value being estimated. » [J8] (p. 1) ;
     - densité d'erreur à support infini, deux fois dérivable, avec (log ψ)'' minoré (lu sur le PDF, p. 2) ;
     - erreurs indépendantes d'un objet à l'autre : « are assumed independent. » [J11] (p. 1) ;
     - objets de même capacité, en nombre N connu d'avance ;
     - répartition quelconque mais non adaptative : « Note that the covers are considered uniform, not only in their capacity but also to prevent the Steganographer embedding adaptively. » [J10] (p. 1).
   - **Valeurs inégales : désormais couvertes.** « In [1] we also imposed the constraint that all cover objects used for embedding had to contain the same amount of payload: the “uniform embedding” assumption. We relax this latter condition in this paper. » [J12] (p. 1, note 1) ; « work a little harder than in [1], for rigour and because we allow non-uniform embedding by the Steganographer. » [J20] (p. 2).
3. **La partie 1 du théorème est la pièce la plus proche à ce jour de L3 (b) — une borne de détection fonction du seul budget total, pour toute répartition — mais à horizon fixe.**
   - Le guetteur compte les estimations positives : « The Warden will count the number of positive estimates » [J19] (p. 2). C'est une **somme** d'indicatrices.
   - Ce test reste valable pour toute répartition : « There is a pooling strategy for the Warden such that, no matter what the Steganographer’s embedding strategy, » [J15] (p. 2).
   - La preuve passe par un théorème de Berry-Esséen, car « we have a sum of not-identically distributed random variables so we cannot use the central limit theorem as in [1]. » [J21] (p. 2).
   - Elle borne la dérive par le seul total (lu sur le PDF, p. 2-3) : Σ(q − q_i) < −A·Σp_i = −A·M/C. On en tire l'erreur de second type β < Φ(C₂ − C₃·M/√N) + C₁/√N (formule (4), p. 3).
   - C'est une **borne fonction du seul budget total M**, valable pour toute répartition (valeurs inégales comprises), et à N fini (le reste de Berry-Esséen est explicite en C₁/√N).
   - Les constantes ne sont pas données ; le contexte est un lot à horizon fixe, sans lecture séquentielle ni garantie toujours valide.
   - Verdict pour L3 (b) : **voisin**. C'est le voisin le plus proche à ce jour, pas une occupation.
4. **L'exposant de Ker 2006 (selon ν) n'est pas une condition de la loi de capacité.** Le théorème vaut pour toute densité dont (log ψ)'' est minoré, et « such a bound exists for many common distributions with infinite support including Gaussian, Cauchy, Logistic, and the Student » [J28] (p. 3), lois de Cauchy et de Student comprises. La loi en √N tient donc aussi à queues lourdes, grâce au test des signes. La condition ν > 2 de Ker 2006 ne porte que sur le détecteur moyenne. **Conséquence pour L1 (décroissance en n₀)** : l'échelle en √n₀ dépend du détecteur ; pour la somme des scores elle-même, la condition sur la queue de Ker 2006 demeure.
5. **Non touché par la lettre** :
   - L4 sur plusieurs pas ;
   - L2 au seuil exact ;
   - L3 en lecture séquentielle (calendrier, coût du report, prix du toujours valide) ;
   - la comparaison processus e cumulé contre détecteur de rupture ;
   - la non-compensation ;
   - la dépendance (l'indépendance est posée comme hypothèse clé) ;
   - les sondes.

   La lecture séquentielle est, une fois de plus, laissée à plus tard : « In practice a Steganographer probably has an increasing number of covers and wants to know how much they can safely embed at each point. » [J35] ; « This sequential setting is a little different from the batch setting considered here, and further work will be needed to study it. » [J36] (p. 4).

## 1. Fiche — « A Capacity Result for Batch Steganography » [J1], « Andrew D. Ker, Member, IEEE » [J2]

- **Venue** imprimée : « IEEE SIGNAL PROCESSING LETTERS, VOL. 14, NO. 8, AUGUST 2007 » [J3], pages 525 à 528. « Manuscript received August 11, 2006; revised September 20, 2006. » [J4] ; « Digital Object Identifier 10.1109/LSP.2006.891319 » [J5]. C'est bien la lettre que citent 2605.16140 (p. 34) et Bash et collègues (p. 27). Ma v2 des voisins la nommait sans l'avoir lue.
- **Cadre** (lu sur le PDF, p. 1) :
  - N objets de capacité C ;
  - une charge totale M répartie par des proportions p_i, avec C·Σp_i = M ; « Possibly some are zero, so that the transmitted objects may be a mixture of covers and stego objects. » [J9] ;
  - test : H₀ « tous les p_i sont nuls » contre H₁ « un p_i au moins est positif » ;
  - définition 1 (p. 2) : le stéganographe est « à risque » si le guetteur a un test d'erreurs α < α* et β < β*.
- **Théorème 1** (p. 2, lu sur le PDF) :
  - **partie 1** : si M/√N → ∞, il existe une stratégie du guetteur sous laquelle le stéganographe est à risque, quelle que soit sa répartition ([J15]) ;
  - **partie 2** : si M/√N → 0, la répartition égale (« The Steganographer’s embedding strategy is simply to split the payload equally between all covers. » [J23], p. 3) n'est à risque pour aucun test ([J16] ; « This will suffice to bound the Warden’s ability to perform (2), no matter what pooling strategy they use. » [J24], p. 3) ;
  - par l'entropie relative : D_KL(X₀‖X₁) < N·B·p²/2 = B·M²/(2N·C²) (p. 3, lu sur le PDF) ;
  - « a result in sharp contrast to those of coding and noisy channels where information transmitted is always proportional to the number of symbols sent. » [J17] (p. 2).
- **Le détecteur** de la partie 1 est le test des signes, modifié. Il n'est pas présenté comme optimal : « It is a modification of the simplest pooling strategy investigated in [1] and certainly is not an “optimal” strategy in practice. » [J18] (p. 2).
- **Ce que la lettre reconnaît de Ker 2006** : « But the investigation was limited to a particular metric for risk, considered a restricted form of batch steganography, and did not prove a general result. » [J13] ; « We will prove that this is correct in a fairly general sense. » [J14] (p. 2).
- **Hypothèses discutées** (p. 3) :
  - « The strongest hypothesis is the shift hypothesis. » [J25] ;
  - « Fundamentally we need that, in the limit as the payload per cover tends to zero, the steganalysis response is linear in the number of embedding changes » [J26] ;
  - « We do not attempt a formal proof at this stage » [J27] ;
  - « Note that we do not require that the error has zero mean » [J30] ;
  - les estimations bornées à [0, 1] ne changent rien : « It is easy to check that the capacity theorem remains valid. » [J39] ;
  - indépendance : « A key assumption is that the steganalysis errors for the » [J29] … ; « The setting of batch steganography allows this independence assumption, and it is a key reason why it is possible to develop capacity results » [J31] (p. 4).
- **Chiffres** (auteurs, p. 4) :
  - pour une loi de Student à 2 degrés de liberté et d'échelle 0,01, avec (α*, β*) = (0,05 ; 0,5), les bornes (6) et (7) donnent sur γ = M/(C√N) respectivement γ ≤ 1,163 × 10⁶ et γ ≥ 0,008121 (lu sur le PDF), soit huit ordres de grandeur d'écart ;
  - « It turns out that these two bounds on detection reliability are a long way apart. » [J32] ; « but not very helpful to the Steganographer in practice because the bounds on » [J33] ;
  - la figure 1 (p. 4, vue en image) montre, pour une erreur gaussienne et γ = 1, une large zone indéterminée.
- **Contre-indice pour L2 et pour la dépendance du choix au détecteur** : « so there is no UMP test; the results in [1] illustrate vividly how the performance of a pooling strategy can be heavily dependent on the embedding strategy. » [J34] (p. 4).
- **Limites reconnues** : séquentiel ([J35], [J36]) ; capacité uniforme (note 1) ; décalage pur ([J25]) ; écart des bornes ([J32]).
- **Réserve de propreté** : aucune. Le résultat n'est pas « trop beau » : les bornes sont lâches de huit ordres de grandeur, et l'auteur le dit.
- **Voisins nommés et non lus** : « Batch steganography and pooled steganalysis » [J37] (Ker 2006, lu) ; « An information-theoretic model for steganography » [J38] (Cachin 2004, p. 4, référence [2]), qui est la source de la borne par l'entropie relative.

## 2. Ce que la lettre établit, avec preuve, par rapport à Ker 2006

| point | Ker 2006 | Ker 2007 (lettre) |
|---|---|---|
| invariance de la loi de la moyenne à la répartition | énoncée comme immédiate (p. 7) | **non traitée** : le détecteur est le test des signes |
| loi en √N de la capacité | conjecturée | **démontrée**, en ordre asymptotique, sans constante (p. 1-3) |
| valeurs inégales | renvoyées à plus tard | **couvertes** par la partie 1 (p. 1, note 1 ; p. 2) |
| répartition adaptative | non | **exclue** par hypothèse ([J10], p. 1 ; il s'agit du choix d'objets selon leur contenu) |
| condition sur la queue | ν > 2 pour la moyenne | (log ψ)'' minoré ; lois de Cauchy et de Student admises (p. 3) |
| borne de détection fonction du seul total, toute répartition | non | **oui**, pour le test des signes, à N fini, constantes non données (formule (4), p. 3) |
| séquentiel, plusieurs pas, toujours valide | réservé | **réservé à nouveau** (p. 4) |

## 3. Table composante × pièce (lettre de Ker 2007)

| composante de L | verdict | appui |
|---|---|---|
| L1 — égalité en loi de la somme, toute répartition | voisin (pas de moyenne ; borne pour le test des signes) | p. 2 [J15, J19, J20] |
| L1 — décroissance en n₀ à budget fixé | **occupée** (déjà par Ker 2006 pour la moyenne à horizon fixe). La lettre la **démontre** pour la capacité, en ordre, pour toute répartition non adaptative, queues lourdes comprises | p. 1-3 [J7, J15, J16, J28] |
| L4 — plusieurs pas, frontières de pas, toujours valide | ne touche pas (un seul lot) | — |
| L2 — max au seuil exact, n fini | ne touche pas ; contre-indice général : la performance dépend de la répartition | p. 4 [J34] |
| L3 (b) — borne inférieure fonction de (B, n₀) seulement | **voisin, le plus proche** : borne de β fonction du seul M/√N, pour toute répartition, à N fini, à horizon fixe, pour le test des signes | p. 2-3 [J15, J19, J21] ; formule (4) |
| L3 — calendrier, coût du report, prix du toujours valide | ne touche pas ; séquentiel réservé | p. 4 [J35, J36] |
| processus e cumulé contre détecteur de rupture | ne touche pas | — |
| non-compensation | ne touche pas | — |
| validité sous dépendance | ne touche pas ; indépendance posée comme hypothèse clé | p. 3-4 [J29, J31] |
| scores de sondes internes | ne touche pas | — |

## 4. Verdict sur L (table fermée)

**Occupé en partie** (case inchangée). Par composante, en cumulant le lot 8, Ker 2006, Bash et collègues et la lettre :
- **L1, cœur (invariance de la somme)** : occupé en partie, par Ker 2006 seul. La lettre n'y ajoute rien.
- **L1, décroissance en n₀** : occupée. La lettre en donne la **preuve**, en ordre asymptotique, pour toute répartition non adaptative et pour des lois à queues lourdes, avec le test des signes.
- **L4** : voisin (cas d'un seul pas).
- **L3 (b)** : non trouvé en lecture toujours valide. Son voisin le plus proche est désormais la partie 1 du théorème de la lettre.
- **L2 au seuil exact, L3 séquentiel (report, prix du toujours valide), processus e cumulé contre détecteur de rupture, non-compensation, dépendance, sondes** : non trouvés dans les pièces lues.

## 5. Ce qui change à « Ce qui reste distinctif » (rapport L voisins v2, section 7)

Lignes remplacées ou ajoutées, en lignes sèches :
- **L1, décroissance en n₀** — imprimée et **démontrée** pour la capacité (lettre de Ker 2007, théorème 1, p. 2-3 : ordre √N, sans constante, toute répartition non adaptative, queues lourdes comprises) ; résidu : aucun.
- **L1, cœur** — inchangé : imprimé (Ker 2006, p. 7, 14), non démontré dans la lettre ; résidu d'une ligne ; nature : remarque citée.
- **L3 (b), borne inférieure invariante fonction de (B, n₀)** — en lecture toujours valide : non trouvée. À horizon fixe, une borne fonction du seul budget total, pour toute répartition, existe pour le test des signes (lettre, formule (4), p. 3). Ce qui reste distinctif est la seule couche « toujours valide ».
- **Valeurs inégales** — couvertes par la lettre pour la loi de capacité. Ce n'est plus un résidu de L1 au-delà de l'écriture trajectorielle.
- **Condition sur la queue** — la loi de capacité en √N n'exige pas ν > 2 (lettre, p. 3). L'exposant N^{1−1/ν} ne concerne que le détecteur moyenne (Ker 2006).
- **Lecture séquentielle** — réservée deux fois par Ker (2006, p. 5 ; 2007, p. 4). Zone séduisante : à vérifier plus durement (règle R8). Les travaux de Ker postérieurs à 2007 ne sont nommés dans aucune pièce lue, hors ceux que cite Bash et collègues (p. 27, 2009-2010), qui sont non lus.
- Inchangées :
  - L4 (contenu propre : plusieurs pas, frontières de pas, toujours valide) ;
  - L3 (coût du report, prix du toujours valide) ;
  - processus e cumulé contre détecteur de rupture ;
  - L2 au seuil exact ;
  - dépendance ;
  - sondes ;
  - repli (c) de N-004.

## 6. Ce qu'une phrase publique ne doit pas affirmer (ajouts)

1. que la décroissance de la détectabilité en √n₀ à budget fixé n'est qu'une observation ou une conjecture : elle est démontrée pour la capacité d'un lot (lettre, théorème 1) ;
2. que la loi en √n₀ exige une variance finie : la loi de capacité vaut pour les lois de Cauchy et de Student (lettre, p. 3). Seul l'exposant de la moyenne en dépend ;
3. qu'une borne de détection fonction du seul budget total, valable pour toute répartition, est sans précédent : elle existe à horizon fixe pour le test des signes (lettre, formule (4)). Seule sa version toujours valide reste non trouvée ;
4. que Ker démontre l'invariance de la moyenne : ni la lettre ni l'article de 2006 ne la démontrent (énoncée comme immédiate en 2006) ;
5. que la lettre traite le cas adaptatif : elle l'exclut par hypothèse ([J10]).

## 7. Colonne « déclarable » de L

**Elle reste à « non » (R-2649).**
- La lettre lève le doute « Ker 2007 non lu » de la réserve. En contrepartie, elle **resserre** la zone : décroissance en n₀ démontrée, valeurs inégales couvertes, borne à budget total à horizon fixe.
- La réserve M4 demeure. Huang, Wang et Poor 2021 ; Bash et collègues 2014 et 2016 ; Arumugam et Bloch 2016 ; Trivedi et Chandramouli 2003 ne sont ni versés ni lus.
- La revendication restante est la couche séquentielle et toujours valide. C'est précisément celle que Ker réserve deux fois : elle appelle la vérification la plus dure.

Le resserrement est une décision du directeur ; je ne la prends pas.

## 8. Ce que je n'ai pas fait

- Aucune autre pièce lue.
- Je n'ai pas refait la preuve de la lettre au-delà de sa lecture. J'ai vérifié à l'œil l'enchaînement des inégalités des p. 2-3 sans le recalculer.
- Aucun calcul numérique : les chiffres sont ceux de l'auteur.

## 9. Refus

Aucun refus de permission, de crochet ni de classifieur. Aucune ouverture fautive.

## Annexe — citations contrôlées (`citations-L-ker2007-v1.json`, dans l'archive)

| id | n° JSON | pièce | page | citation exacte |
|---|---|---|---|---|
| J1 | 1 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | A Capacity Result for Batch Steganography |
| J2 | 2 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | Andrew D. Ker, Member, IEEE |
| J3 | 3 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | IEEE SIGNAL PROCESSING LETTERS, VOL. 14, NO. 8, AUGUST 2007 |
| J4 | 4 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | Manuscript received August 11, 2006; revised September 20, 2006. |
| J5 | 5 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | Digital Object Identifier 10.1109/LSP.2006.891319 |
| J6 | 6 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | It was conjectured that, given covers of uniform capacity and a quantitative steganalysis method satisfying certain assumptions, |
| J7 | 7 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | capacity is proportional only to the square root of the number of covers. We now prove that, with respect to a natural definition of secure capacity, and in a suitably asymptotic sense, this conjecture is true. |
| J8 | 8 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | We further assume that the estimation error distribution does not depend on the true value being estimated. |
| J9 | 9 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | Possibly some are zero, so that the transmitted objects may be a mixture of covers and stego objects. |
| J10 | 10 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | Note that the covers are considered uniform, not only in their capacity but also to prevent the Steganographer embedding adaptively. |
| J11 | 11 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | are assumed independent. |
| J12 | 12 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | In [1] we also imposed the constraint that all cover objects used for embedding had to contain the same amount of payload: the “uniform embedding” assumption. We relax this latter condition in this paper. |
| J13 | 13 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | But the investigation was limited to a particular metric for risk, considered a restricted form of batch steganography, and did not prove a general result. |
| J14 | 14 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | We will prove that this is correct in a fairly general sense. |
| J15 | 15 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | There is a pooling strategy for the Warden such that, no matter what the Steganographer’s embedding strategy, |
| J16 | 16 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | There is an embedding strategy for the Steganographer such that, no matter what the Warden’s pooling strategy, |
| J17 | 17 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | a result in sharp contrast to those of coding and noisy channels where information transmitted is always proportional to the number of symbols sent. |
| J18 | 18 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | It is a modification of the simplest pooling strategy investigated in [1] and certainly is not an “optimal” strategy in practice. |
| J19 | 19 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | The Warden will count the number of positive estimates |
| J20 | 20 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | work a little harder than in [1], for rigour and because we allow non-uniform embedding by the Steganographer. |
| J21 | 21 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | we have a sum of not-identically distributed random variables so we cannot use the central limit theorem as in [1]. |
| J22 | 22 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | we are only able to determine capacity a) asymptotically and b) without regard to the multiplicative constant of |
| J23 | 23 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | The Steganographer’s embedding strategy is simply to split the payload equally between all covers. |
| J24 | 24 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | This will suffice to bound the Warden’s ability to perform (2), no matter what pooling strategy they use. |
| J25 | 25 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | The strongest hypothesis is the shift hypothesis. |
| J26 | 26 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | Fundamentally we need that, in the limit as the payload per cover tends to zero, the steganalysis response is linear in the number of embedding changes |
| J27 | 27 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | We do not attempt a formal proof at this stage |
| J28 | 28 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | such a bound exists for many common distributions with infinite support including Gaussian, Cauchy, Logistic, and the Student |
| J29 | 29 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | A key assumption is that the steganalysis errors for the |
| J30 | 30 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | Note that we do not require that the error has zero mean |
| J31 | 31 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | The setting of batch steganography allows this independence assumption, and it is a key reason why it is possible to develop capacity results |
| J32 | 32 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | It turns out that these two bounds on detection reliability are a long way apart. |
| J33 | 33 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | but not very helpful to the Steganographer in practice because the bounds on |
| J34 | 34 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | so there is no UMP test; the results in [1] illustrate vividly how the performance of a pooling strategy can be heavily dependent on the embedding strategy. |
| J35 | 35 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | In practice a Steganographer probably has an increasing number of covers and wants to know how much they can safely embed at each point. |
| J36 | 36 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | This sequential setting is a little different from the batch setting considered here, and further work will be needed to study it. |
| J37 | 37 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | Batch steganography and pooled steganalysis |
| J38 | 38 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | An information-theoretic model for steganography |
| J39 | 39 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | It is easy to check that the capacity theorem remains valid. |
| J40 | 40 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | Theorem 1 (Batch Steganographic Capacity): Suppose the shift hypothesis (1) and that the error density |
