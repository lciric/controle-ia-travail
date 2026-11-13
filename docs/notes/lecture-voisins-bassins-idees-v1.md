# Lecture des voisins « bassins d'idées » — Fork-and-Flush (arXiv 2610.07447) et Scaling Discovery Requires Forgetting (arXiv 2610.20563) — v1

- **Auteur** : sous-agent neuf, lecteur (Claude Fable 5.2, `claude-fable-5-2`), sur la consigne scellée
  `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-lecteur-voisins-bassins-idees-v1.md`
  (`53e0227edadcabd41451a90a0cfb8a6096820640179cdaad18204124e7f5db1e`) et les interdits
  `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`
  (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`), toutes deux vérifiées par empreinte avant lecture.
  Je n'ai écrit aucun code versé, modifié aucune pièce existante, fait aucun appel de modèle, aucune opération git, aucune
  dépense. Aucun refus de permission n'est survenu.
- **Heures** (relevées par `date -u`) : début 2026-11-13 12:28:44 UTC ; fin de rédaction 2026-11-13 12:39:51 UTC.
- **Niveau de preuve** : les deux articles sont lus **sur PDF empreinté, page citée** (R7 : opposable pour ce que les PDF
  disent ; ce sont des versions 1 d'arXiv, sans mention de relecture par les pairs dans les PDF). La page de Bespoke Labs est
  un billet archivé : citée par fichier et empreinte, sans page ; ses chiffres valent comme dires d'un billet. Les travaux
  que ces trois pièces **citent** ne sont pas lus : **niveau transcription, non opposable**, marqué comme tel partout.

## Références courtes (toute page citée renvoie à l'un de ces fichiers)

| sigle | pièce | chemin | empreinte SHA-256 |
|---|---|---|---|
| **[FF]** | Cai, Ziakas, Kontonis, Pearce, Sen, Krishnamurthy, Garg, Papailiopoulos (Microsoft Research), « Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents », arXiv 2610.07447, **version 1 servie**, datée du 5 octobre 2026 sur la page 1, 25 pages | `docs/sources/arxiv-bassins-idees-20261113/arxiv-2610.07447v1.pdf` | `4eba26a1e744bcb4cb1f748aea062f7120dd796aa7f319e675b3690586242741` |
| **[SDF]** | Tan, Zhou, Agrawal, Zhang, Chen, Mang, Lee, Jacob, Sen, Dimakis, Zaharia (Berkeley, Stanford, Bespoke Labs), « Scaling Discovery Requires Forgetting », arXiv 2610.20563, **version 1 servie**, datée du 14 octobre 2026 sur la page 1, 14 pages | `docs/sources/arxiv-bassins-idees-20261113/arxiv-2610.20563v1.pdf` | `9c14df8357e1fb46caa8349e6225d502180ee74c20c62d5af97ec29cd4285edc` |
| **[Page]** | Bespoke Labs, « How models explore ideas », 10 novembre 2026 (billet) | `docs/sources/web-bespoke-how-models-explore-ideas-20261113/texte.txt` | `b1d3222733508d630414c968b880350aa01c13dbeb69ebcec9080ee6a3588253` |

Téléchargement : `https://arxiv.org/pdf/2610.07447` et `https://arxiv.org/pdf/2610.20563`, client générique, aucune donnée
du projet dans la requête ; les deux réponses portent le code 200 et l'en-tête `content-disposition` nomme
`2610.07447v1.pdf` et `2610.20563v1.pdf` (d'où « version servie »). Les deux PDF sont scellés (compagnons `.sha256`,
vérifiés). Texte extrait page par page par `pdftotext -layout` (version 24.02.0), sous `ulimit -v 6000000`, dans le
bac de travail de la session (non versé : il se régénère par la même commande) ; pages à figures relues en image
(`pdftoppm`, 80 points par pouce) : [FF] p. 1, 3, 7, 21 ; [SDF] p. 1, 8.

Nos pièces lues, vérifiées contre leur compagnon : `docs/decisions/decision-N-044-v1.md` (`2b70bdac…`),
`decision-N-045-v2.md` (`c7b05e39…`), `decision-N-058-v1.md` (`854f2724…`), `decision-N-064-v1.md` (`387c9d4e…`),
`decision-N-065-v1.md` (`f820e90d…`) ; `docs/notes/collisionneur-diversite-idees-v1/synthese-v1.md` (`4f99077b…`) ;
`docs/notes/organisme-multi-generations-v1/conception-monde-riche-doublons-v3.md` (`386d48ba…`, sections 3, 4, 5) et
`…-v4.md` (`47e38ec0…`, en-tête, sections 0, 1 et 2 : famille MR-2).

## 1. Verdict (trois lignes)

1. **Voisinage serré, pas de collision** : aucun des énoncés que j'ai lus (N-044, N-045 v2, N-064, N-065, N-058, le
   regroupement prédictif des doublons, la diversité par couverture d'oracle) n'est occupé par ces deux articles ni par le
   billet. Je n'ai **pas** pu confronter les revendications O1, O3 à O10 et O13 à O20 de l'organisme : leur texte n'est dans
   aucune pièce nommée par la consigne.
2. **Deux résultats à citer et à affronter** : (i) à budget égal, repartir du meilleur résultat avec un contexte neuf bat le
   fil continu **et** le meilleur de quatre tirages ([FF] p. 5-6 ; [SDF] p. 6), et **hériter moins fait mieux** ([SDF] p. 7-8)
   — cela pèse sur la prémisse de N-045 (« récompenser ce qu'une génération lègue ») et impose des témoins ; (ii) « grouper
   les idées par ce qu'elles font, non par leur texte, puis suivre les trajectoires de groupe en groupe » est **pris** pour
   des artefacts libres, par une carte à juge modèle ([FF] p. 4, 18) : à ne pas revendiquer comme principe.
3. **Restent ouverts au regard de ces trois pièces seulement** (R8 : une limite d'article n'est pas un trou du champ) :
   composition et mémoire **apprises**, coût dans le signal, universalité sur familles inédites, juge statistique à
   engagement scellé, regroupement par distance prédictive calculée par programme, diversité mesurée contre un oracle. Une
   douzaine de voisins cités par ces articles, non lus, peuvent occuper une part de ces zones (liste au §7.3).

## 2. [FF] Fork-and-Flush

### 2.1 Question

Un agent de recherche automatisée qui tourne longtemps explore-t-il largement l'espace des solutions, ou raffine-t-il les
idées choisies tôt ([FF] p. 2 : « does an agent explore the solution space broadly, or does it mainly refine the ideas it
selected early on? ») ; et peut-on exploiter la variance entre courses indépendantes pour en sortir ([FF] p. 2, 4).

### 2.2 Dispositif

- **Tâches** : 13 tâches ouvertes à note continue et vérifiable — 9 de Frontier-CS, 2 d'EdgeBench, l'exercice public
  d'optimisation de noyau d'Anthropic, une compression de classifieur CIFAR écrite pour l'étude ([FF] p. 3 ; table 4, p. 16).
  Budgets par course de 6 000 à 100 000 crédits, 100 crédits ≈ 1 dollar ([FF] p. 3) ; durée médiane d'une course simple de 5
  à 107 heures selon la tâche (table 4, p. 16).
- **Agent** : GitHub Copilot CLI version 1.0.73, mêmes outils et consigne dans toutes les conditions ([FF] p. 3) ; modèle
  GPT-5.6-terra (effort de raisonnement élevé) pour onze tâches, GPT-5.5 (effort très élevé) pour `kernel` et `tinyCIFAR`
  ([FF] p. 5-6). L'agent compacte périodiquement son historique ([FF] p. 2, 10). Aucun message ne dit le budget ni ce qu'il
  en reste ([FF] p. 22).
- **État** : s = (W, C), W l'espace de travail (fichiers produits), C le contexte de conversation ; une lignée est une suite
  d'états ; un correcteur **déterministe** rend f(W) ([FF] p. 3).
- **Conditions, à budget global égal** ([FF] p. 5-6) : course simple (tout le budget B sur une lignée ; huit courses par
  tâche) ; meilleur de 4 (quatre courses de B/4, on garde la meilleure) ; fork-and-flush (cinq courses par tâche, quatre sur
  `tinyCIFAR`).
- **Fork-and-flush tel qu'évalué** ([FF] p. 6) : ouverture par K = 4 agents sur espace vide, le mieux noté devient meneur ;
  puis deux tours déclenchés par la **consommation de budget**, à 33 % et 66 % de B : K = 4 branches partent de l'espace de
  travail du meneur avec un **contexte vide**, chacune dotée d'environ 0,06 B ; la mieux notée devient meneur, les autres
  sont jetées. Dans chaque tour, deux des K branches reçoivent en plus une consigne « choisis une approche DIFFÉRENTE »
  ([FF] p. 22). Toute branche qui hérite d'une soumission notée reçoit un avis qui protège le meilleur résultat hérité et en
  cite la note ([FF] p. 22).

### 2.3 Mesures (définitions exactes)

- **Note d'une lignée** J(ℓ) = max_i f(W_i) ; **résultat d'une course** R = max sur les lignées instanciées dans le budget B
  ([FF] p. 3).
- **Table principale** : maximum, moyenne et écart-type des notes finales sur les courses indépendantes ; ligne d'ensemble
  = moyennes **normalisées min–max** par tâche ([FF] table 1, p. 5 ; la table 3, p. 15, précise que chaque course d'une tâche
  est normalisée sur l'ensemble des méthodes avant la moyenne).
- **Carte des idées** ([FF] p. 4 ; annexe F, p. 18 ; consignes, p. 23-25) : (i) soumissions notées, doublons exacts retirés
  par empreinte du contenu, 51 instantanés également espacés par course ; (ii) un modèle de langue réécrit chaque soumission
  en **spécification fonctionnelle** canonique à onze sections, qui retire noms, style et organisation du fichier et garde
  algorithme, structures et toute valeur numérique ; (iii) un juge — **le même déploiement de modèle** que celui qui a écrit
  les spécifications — classe par similarité de stratégie les trois paires d'un triplet, sans note ni chronologie ; 6 375
  jugements par carte (5 610 pour `p150`) ; (iv) plongement en deux dimensions par plongement stochastique de triplets à loi
  de Student (« t-STE »), meilleur de huit départs, un triplet sur cinq par ancre tenu à l'écart.
- **Validité de la carte** : part des jugements tenus à l'écart que la carte reproduit ; hasard 0,50 ; témoin « ne connaît
  que la course d'origine » ([FF] p. 4 ; table 6, p. 18-19).
- **Bassin d'idées** : groupe obtenu par k-moyennes ajustées sur les artefacts des courses simples dans la carte ([FF] p. 4).
- **Taille de pas** : distance entre soumissions consécutives, en unités du pas médian des courses simples ([FF] p. 7).
- **Échelle de difficulté MAX-3-SAT** : atteinte h = (u_hasard − u_agent) / (u_hasard − u_référence), moyenne a et écart-type
  de population s par cellule (modèle, nombre de variables), 8 à 32 courses par cellule, intervalles par 2 000 rééchantillonnages
  ([FF] p. 8).

### 2.4 Résultats chiffrés (avec page)

| résultat | valeur | page |
|---|---|---|
| Moyenne normalisée, 13 tâches : course simple ; meilleur de 4 ; fork-and-flush | 0,47 ; 0,54 ; 0,78 | table 1, p. 5 ; p. 6 |
| Gain relatif annoncé de fork-and-flush sur la course simple et sur le meilleur de 4 | 66,0 % et 44,4 % | p. 1, 6 |
| Maximum normalisé : course simple ; meilleur de 4 ; fork-and-flush | 0,75 ; 0,73 ; 0,98 | table 1, p. 5 |
| Écart-type normalisé : idem | 0,26 ; 0,21 ; 0,16 | table 1, p. 5 ; p. 6 |
| Tâches où fork-and-flush a la meilleure moyenne | 12 sur 13 | p. 6 |
| Tâches où l'écart-type baisse contre la course simple | 10 sur 13 | p. 6 |
| Exception : `LWE-rec`, moyennes course simple ; meilleur de 4 ; fork-and-flush | 155,3 ; 141,14 ; 144,60 | table 1, p. 5 |
| Variance persistante sur `p171`, huit courses : notes finales | de 68,3 à 100,0 (médiane 81,9) | p. 4 ; figure 1, p. 1 |
| Accord de la carte sur triplets tenus à l'écart (cinq tâches) | 0,81 à 0,87, moyenne 0,85 ; hasard 0,50 ; « course d'origine seule » 0,52 à 0,60 (56 % au corps du texte) | table 6, p. 18-19 ; p. 4 |
| Même contrôle avec un plongement ordinal doux (« SOE ») | 0,79 à 0,86, moyenne 0,83 ; 99 % des artefacts des courses simples gardent leur bassin | table 6, p. 18 ; figure 6, p. 17 |
| Saut de bassin sur `polyomino` (un exemple) : pas maximal d'une course simple après le premier quart ; pas du meneur ; branche gagnante au premier dépôt après la remise à zéro ; branches rejetées | 4,4 ; ≤ 2,9 ; **43** ; ≤ 1 (unités du pas médian) | p. 7 |
| Même saut sous l'autre plongement | 10,1 (courses simples ≤ 4,1) | p. 7, 17-18 |
| Fin de cette course contre la médiane des courses simples | 93,9 contre 84,6 | p. 8 |
| Échelle MAX-3-SAT (Qwen3.5 4B, 9B, 27B ; 10 à 100 000 variables) : écart entre courses maximal à | a = 0,497 (ajustement quadratique) | p. 8 |
| Consigne « approche différente » : branche dirigée choisie | 81 tours sur 178 (46 %), contre 50 % attendus ; p bilatéral = 0,26 | p. 22 |
| Déclenchement sur plateau (essais de mise au point) | 15 courses sur 25 épuisent le budget avant que le critère ne se déclenche | annexe D, p. 15 |

### 2.5 Interventions éprouvées et effets

| intervention | définition | effet rapporté |
|---|---|---|
| Compaction périodique de l'historique (déjà dans l'agent) | la trace est remplacée par un résumé | « insufficient » : les courses plafonnent encore à des niveaux différents et restent dans leur bassin ([FF] p. 10) |
| Meilleur de 4 | quatre courses de B/4 | 0,54 contre 0,47 pour la course simple (13 tâches, table 1, p. 5) |
| Remise à zéro seule | K = 1, contexte vidé à chaque tour forcé, espace de travail gardé | 0,55 contre 0,45 (11 tâches, table 2, p. 6) |
| Branches seules | K = 4 branches qui **gardent** le contexte du tronc | 0,57 (table 2, p. 6) |
| Les deux | K = 4, contexte vidé, reprise de la mieux notée | 0,71 sur 11 tâches (table 2, p. 6) ; 0,78 sur 13 (table 1, p. 5) |
| Consigne de diversité sur 2 branches sur K | texte ajouté au premier message | aucun effet mesurable sur la branche retenue (p. 22) ; les auteurs traitent branches dirigées et non dirigées comme interchangeables |
| Cadence | plateau ; un tour à 50 % ; deux tours à 33 % et 66 % | les deux cadences fixes battent la course simple sur les six tâches essayées ; deux tours gagnent sur quatre, un tour sur deux ; effectifs de 1 à 11 courses (table 5, p. 17 ; p. 15) |

Lecture par tâche de la table 3 (p. 15), **comptes faits par moi** sur les onze lignes : la remise à zéro seule est
**sous** la course simple sur 5 tâches sur 11 (`polyomino` 85,91 contre 88,56 ; `AHC014` 23,04 contre 23,71 ; `p171` 79,73
contre 84,26 ; `sphere-pack` 43,74 contre 43,87 ; `LWE-rec` 148,4 contre 155,3) ; sa moyenne normalisée supérieure tient
surtout à `p150` (160,80 contre 123,47) et `order-add` (40,73 contre 24,60). Fork-and-flush a la meilleure moyenne sur 8
lignes sur 11 ; les trois autres vont aux branches seules (`job-shop`), à la remise à zéro seule (`p150`) et à la course
simple (`LWE-rec`).

### 2.6 Limites dites par les auteurs

- Peu de tâches, à cause du coût des courses longues ([FF] p. 10).
- Les branches n'ont **ni coordination ni rôles** ; communication entre agents et spécialisation des rôles sont renvoyées
  à plus tard ([FF] p. 10).
- Les paramètres de cadence n'ont pas été balayés systématiquement ; effectifs petits ([FF] p. 15).
- Aucune affirmation sur les bassins pour `job-shop` (structure faible) ([FF] p. 15) ; l'accord de la carte y est le plus
  bas (0,81 ; table 6, p. 18).
- La méthode ne porte ni mémoire entre tâches ni mise à jour de poids ([FF] p. 9).

### 2.7 Code et données

Aucun dépôt de code ni jeu de données propre à l'article parmi les liens du PDF (cinq liens : la page arXiv de l'article,
l'exercice d'Anthropic, le dépôt `autoresearch` de Karpathy, Terminal-Bench et Terminal-Bench-Science ; relevés par
programme sur les annotations du PDF). Sont publiés **dans le PDF** : les messages servis aux agents ([FF] p. 22-23) et les
consignes de la carte — juge de triplets et réécriture en spécification, exemple `polyomino` ([FF] p. 23-25). Le modèle qui
réécrit et juge n'est pas nommé ([FF] p. 18).

### 2.8 Remarques de lecture (R4)

- Aucun intervalle ni test sur la table principale ; les gains relatifs sont des rapports de moyennes normalisées
  (0,78 / 0,47 et 0,78 / 0,54), sensibles à la normalisation.
- Effectifs des courses simples dits différemment : huit par tâche ([FF] p. 5), « 5 independent runs » dans la légende de la
  table 1 (p. 5), huit (sept ou six sur quatre tâches) dans celle de la table 3 (p. 15).
- L'exemple du saut se déclenche « at 71% of the budget » ([FF] p. 7) alors que la configuration évaluée déclenche à 33 % et
  66 % ([FF] p. 6) : écart non expliqué dans le texte. C'est **un** exemple : l'article ne donne pas la **fréquence** des
  tours où une branche change de bassin ; son annexe H dit qu'une remise à zéro peut aussi ne produire aucun saut ([FF] p. 19).
- Les bassins sont définis par un juge modèle et un plongement ; le rapport 43 contre 10,1 entre les deux plongements
  montre que la **taille** d'un saut dépend de la méthode ([FF] p. 17-18). La carte est validée contre son propre juge
  (triplets tenus à l'écart), jamais contre une vérité des idées.
- La ligne « 5 original tasks » de la table 3 (0,37 ; 0,41 ; 0,47 ; 0,63 ; p. 15) n'est pas définie dans le texte.

## 3. [SDF] Scaling Discovery Requires Forgetting

### 3.1 Question

Les trois façons de mettre plus de calcul dans une recherche automatisée — un agent plus longtemps, plusieurs agents en
parallèle, des agents qui se lisent — plafonnent-elles, pourquoi, et l'**oubli** périodique lève-t-il le plateau ([SDF]
p. 1-2).

### 3.2 Dispositif

- **Tâches** : quatre — AtCoder Heuristic Contest 014, Frontier-CS Q171, le noyau d'Anthropic, l'entraînement d'un petit
  modèle de langue en cinq minutes (`nanochat-autoresearch`) ; budget par réplique 20, 20, 40 et 20 dollars ([SDF] p. 5 ;
  table 4, p. 13).
- **Agent et modèle** : agent Pi, modèle DeepSeek V4.1 Flash, pour toutes les conditions ([SDF] p. 5).
- **Trois conditions, même modèle, même budget, trois répliques par tâche** ([SDF] p. 5) : un agent, une séance continue ;
  quatre agents parallèles qui ne se voient pas ; **équipe de quatre avec oubli**, qui oublie trois fois (quatre manches).
- **Oubli** ([SDF] p. 4) : à la fin d'une manche, l'agent jette sa **séance** et son **état de recherche** (tous les
  candidats, notes et retours), ne garde que **le meilleur candidat et sa note**, et repart avec un contexte vide et les
  mêmes instructions. En équipe : tous repartent du meilleur candidat de l'équipe.
- **Communication** ([SDF] p. 4) : avant chaque proposition, chaque agent a accès aux candidats de ses pairs, comme
  commits, avec leurs notes ; aucun échange direct ; « fully asynchronous and token-free ».
- **Banc** ([SDF] p. 5) : un « réducteur » décide ce que l'agent voit et quelle séance il continue ; l'agent ne s'évalue pas
  lui-même, un autre processus note le candidat ([SDF] p. 14).

### 3.3 Mesures

- Meilleure note finale par configuration, trois courses par tâche, **à coût total en jetons égal** : meilleure réplique, et
  moyenne ± écart-type ([SDF] table 1, p. 6).
- Meilleure note moyenne de l'équipe à la fin de chaque manche ([SDF] table 2, p. 6).
- **Continuer contre oublier depuis le même état** : gain du meilleur nouveau candidat sur le meilleur de l'état, moyenne et
  écart-type sur trois répliques, **30 propositions de plus par agent** dans les deux bras ; dépense par réplique ([SDF]
  table 3, p. 8).
- Lignes modifiées par proposition et jetons de raisonnement par tour, médianes par dollar dépensé ([SDF] figure 5, p. 8).
- Tours sans candidat et part de la dépense qu'ils consomment ([SDF] p. 8).

### 3.4 Résultats chiffrés (avec page)

| résultat | valeur | page |
|---|---|---|
| AHC014 (milliers, plus haut = mieux), moyenne ± écart-type : un agent ; 4 parallèles ; équipe avec oubli | 795 ± 210 ; 964 ± 57 ; 1 103 ± 50 | table 1, p. 6 |
| Noyau (cycles, plus bas = mieux) : idem | 1 426 ± 197 ; 1 220 ± 44 ; 1 097 ± 18 | table 1, p. 6 |
| Frontier-CS Q171 (plus haut = mieux) : idem | 64,0 ± 6,2 ; 70,2 ± 1,1 ; 80,8 ± 2,9 | table 1, p. 6 |
| `nanochat-autoresearch` (bits par octet de validation, plus bas = mieux) : idem | 0,980 ± 0,003 ; 0,980 ± 0,001 ; 0,961 ± 0,012 | table 1, p. 6 |
| Gain moyen de l'équipe avec oubli sur les 4 parallèles et sur un agent, quatre tâches | 10 % et 22 % | p. 6 |
| Fourchette du gain sur la meilleure référence, par tâche | de 1,9 % à 15 % | p. 2 |
| Gains après chaque oubli sur AHC014 | +11,2 % ; +4,8 % ; +1,7 % | table 2, p. 6 ; p. 7 |
| Oublis suivis d'un nouveau meilleur candidat dans la manche suivante | 32 sur 36 | p. 7 |
| Les 4 parallèles sur la seconde moitié du budget | +1,2 % sur AHC014 ; −2,4 % de cycles sur le noyau | p. 6 |
| Même état, AHC014, **continuer** : un agent ; 4 parallèles ; équipe | +1,6 % ± 0,2 ; +1,9 % ± 1,5 ; +1,4 % ± 1,3 ; dépense 6,66 ; 27,51 ; 24,67 dollars | table 3, p. 8 |
| Même état, AHC014, **oublier** : idem | +4,5 % ± 2,1 ; +7,0 % ± 3,3 ; +9,2 % ± 6,9 ; dépense 3,44 ; 13,97 ; 15,32 dollars | table 3, p. 8 |
| Rétrécissement avant le premier oubli (équipe, AHC014) : lignes modifiées ; jetons de raisonnement | d'environ 150 à 30 ; d'environ 28 000 à 7 000 | p. 8 |
| Dix premières propositions après oubli contre poursuite : lignes modifiées (médiane) ; jetons de raisonnement (médiane) | 40 contre 6 ; 9 400 contre 2 900 | p. 9 |
| Noyau, agent seul : tours sans candidat ; part de la dépense | 532 sur 763 ; 66,2 % (de 58,4 % à 70,4 % selon la réplique) | p. 8 |
| Communication seule, avant le premier oubli | Q171 : équipe 13 % devant les parallèles à dépense égale ; AHC014 : légèrement derrière | p. 6 |

### 3.5 Interventions éprouvées et effets

| intervention | définition | effet rapporté |
|---|---|---|
| Parallèle sans communication | 4 agents, budget partagé | aide sur trois tâches sur quatre, rien sur `nanochat-autoresearch` ; plafonne ([SDF] p. 6) |
| Communication par candidats | les candidats des pairs et leurs notes sont lisibles avant chaque proposition | n'empêche pas le plateau ; poursuivre une équipe 30 propositions de plus : +1,4 % ([SDF] p. 6, 8) |
| Oubli (séance **et** état de recherche jetés, meilleur candidat gardé) | trois oublis, quatre manches | meilleure moyenne et meilleure réplique sur les quatre tâches ([SDF] table 1, p. 6) |
| Oublier contre continuer, à nombre de propositions égal | même état de départ | gain plus grand **et** dépense à peu près moitié moindre (contexte plus court) ([SDF] p. 7-8) |

### 3.6 Limites dites par les auteurs, et ce que le plan ne sépare pas

- Dit : le gain d'un oubli décroît de manche en manche, les tâches ayant une borne ([SDF] p. 7) ; « A natural next step is to
  decide when to forget and what to remember » ([SDF] p. 9).
- Dit, sur la différence avec [FF] : « we more aggressively remove the workspace state as well, keeping only the best
  candidate solution », et les agents communiquent sans orchestrateur ([SDF] p. 3).
- **Non séparé (ma lecture)** : la table 1 ne contient ni « équipe sans oubli » ni « agent seul avec oubli » à budget plein :
  équipe et oubli y sont confondus ; seule l'expérience « même état » (une tâche, trois répliques, [SDF] p. 7-8) les sépare.
  Séance et état de recherche sont toujours jetés ensemble : aucune comparaison directe avec « garder l'espace de travail »
  de [FF]. Trois répliques par cellule, écarts-types donnés, aucun test. Un seul modèle.

### 3.7 Code et données

Aucun lien vers un dépôt du banc ou des courses dans le PDF (liens relevés par programme : tâches, agent Pi, modèle,
références). Les messages servis aux agents sont publiés ([SDF] annexe B, p. 13-14).

## 4. [Page] le billet de Bespoke Labs, en bref (dires d'un billet, sans page)

Reprend la carte de [FF] sur 348 courses de 24 heures (12 modèles) et 12 656 soumissions notées, 9 179 après retrait des
soumissions au code identique à la précédente ; un modèle résume chaque soumission, un autre répond aux triplets (« environ
1,3 million d'appels », « moins de 40 dollars »), chaque question posée deux fois en échangeant B et C, réponses peu sûres
écartées (569 271 gardées) ; carte ajustée sur 90 % des réponses, 89 % d'accord sur les 10 % restants contre 60 % pour le
témoin « course d'origine » ; bassins par k-moyennes, 3 à 8 par tâche, choisis par silhouette. Dires principaux : 1,5 à 2
bassins visités par course ; 47 % des courses ne quittent jamais leur premier bassin ; 4 à 13 % des soumissions changent
d'idée ; la moitié des changements **reviennent** à une idée déjà essayée ; un passage à une idée neuve est suivi d'environ
neuf fois le gain d'un pas de raffinage ; 58 % des courses n'atteignent jamais le bassin de la meilleure solution de leur
tâche ; l'écart entre validation et test caché suit le volume de soumissions (ρ = 0,84). Tout cela vient de
`texte.txt` (`b1d32227…`).

## 5. Nos revendications × ces articles

Statuts : **pris** (la zone est occupée par l'article) ; **voisin à citer** ; **ouvert** (non touché par ces pièces — ce
qui ne dit rien du reste du champ, R8) ; **à battre** (résultat ou témoin que notre dessin doit affronter).

| notre énoncé (pièce) | ce que font [FF] et [SDF] | statut | phrase et page à l'appui |
|---|---|---|---|
| **N-045 §1** — la composition (nombre de parties, rôles, modèle par rôle, mémoire transmise, part de budget) est **apprise** | tout est fixé à la main : K = 4, cadence fixe, un modèle par tâche ([FF]) ; équipe de 4, trois oublis, un modèle ([SDF]) | **ouvert** ; désigné comme suite par les deux | [FF] p. 10 : « Future work will investigate inter-agent communication and role specialization across branches » ; [SDF] p. 9 : « decide when to forget and what to remember » |
| **N-045 §2** — le coût entre dans le signal rendu à l'organisme | comparaisons à budget égal ; chez [FF] l'agent ne voit jamais le coût ; chez [SDF] les messages publiés n'en disent rien (p. 13-14) | **ouvert** ; **voisin à citer** pour la comparaison à coût apparié | [FF] p. 22 : « agents are never told how much compute they have » ; [SDF] p. 7 et table 3, p. 8 (l'oubli coûte à peu près moitié moins à propositions égales) |
| **N-045 §4** — aucune voie chère avant qu'une voie bon marché montre que le séquentiel bat le meilleur de N tirages, à budget égal, sur familles tenues à l'écart | mesuré **dans une tâche** : le fil continu simple fait moins bien que le meilleur de 4 (0,47 contre 0,54) ; il gagne avec reprise du meilleur et contexte neuf (0,78) | **voisin à citer** ; **à battre** comme témoin ; la version « familles tenues à l'écart » reste **ouverte** | [FF] table 1, p. 5 ; [SDF] table 1, p. 6 ; [FF] p. 9 : « it improves a single run within one task » |
| **N-045 §5** — l'héritage d'une génération est récompensé (mémoire transmise, instruments à effet différé) | aucun signal d'apprentissage ; mais les deux mesurent **quoi hériter** : hériter l'espace de travail sans le contexte ([FF]) ; hériter le seul meilleur candidat ([SDF]) ; hériter moins fait mieux | **ouvert** pour la récompense ; **à battre** pour la prémisse « ce qui est légué aide » | [SDF] p. 2 : « the best candidate often subsumes many effective heuristics from earlier iterations » ; table 3, p. 8 ; [FF] p. 5 : « A branch that retained C would carry the parent's reasoning that tends to re-enter the same local basin » |
| **N-045 §6 (ii)** — poids contre archive (archive consultable des mêmes trajectoires, contre adaptateur entraîné, contre concepteur externe) | aucun entraînement de poids ; l'« archive » y est justement ce qu'on jette | **ouvert** ; **voisin à citer** pour le bras « archive », dont la forme compte (trajectoires entières ou meilleur seul) | [FF] p. 9 : « no memory carried across tasks and no weight updates » ; [SDF] p. 4 : « the discarded states mainly record how that progress was made » |
| **N-064, O2** — statistique calculée par l'orchestrateur sur engagement scellé, nul des lois connues, multiplicité contrôlée | correcteur déterministe de la tâche, sélection par la plus haute note, aucune statistique de test, aucun contrôle de multiplicité | **ouvert** (non touché) | [FF] p. 3 : « a deterministic grader evaluates the workspace » ; p. 5 : « the highest-scoring branch […] is selected » ; [SDF] p. 14 : « another process scores your candidate » |
| **N-064, O11 et O12** (forme seule : proposeur qui lit la description d'un juge statistique et ses verdicts) | aucun proposeur qui attaque un juge ; [Page] rapporte seulement que l'écart validation–test croît avec le volume de soumissions | **ouvert** ; [Page] **voisin** d'illustration, niveau billet | [Page] : « Submission volume tracks the gap much more closely (ρ = 0.84) » |
| **N-065** — second terrain du papier C (juges de la recherche automatisée sous attaque) ; atelier d'idées | aucun juge sous attaque ; le juge de triplets est un instrument de mesure, jamais éprouvé contre un agent qui chercherait à paraître différent | **ouvert** (non touché) | [FF] p. 18 : validation par triplets tenus à l'écart seulement |
| **N-044 §1** — universalité mesurée sur des familles jamais vues à la conception | aucune famille tenue à l'écart ; la cadence de [FF] est mise au point sur six des treize tâches évaluées | **ouvert** | [FF] table 5, p. 17 (essais de mise au point sur `polyomino`, `job-shop`, `AHC014`, `p150`, `p171`, `kernel`) ; [SDF] p. 5 (quatre tâches, toutes évaluées) |
| **N-044 §2** — trois régimes de budget ; re-conception déclenchée par l'organisme sur son propre critère | [FF] renonce au déclenchement sur plateau au profit d'une cadence fixe | **voisin à citer** (mise en garde, autre objet : c'est le banc, non l'agent, qui détecte) | [FF] p. 15 : « 15 of 25 plateau-triggered runs exhausted their budget before the stall criteria were met » |
| **N-044 §5** — diversité : trois bras (mission et miroir fonctionnel ; contrainte câblée ; rien), le juge seule pression | [FF] compare, de fait, une consigne de diversité à rien (sans effet mesurable sur la branche retenue) et un mécanisme câblé (remise à zéro et branches) à rien (effet net) ; il ne mesure pas l'effet de la consigne sur la diversité elle-même | **voisin à citer** ; un résultat nul du bras « mission » a un précédent | [FF] p. 22 : « The directive does not measurably change which branch wins » ; table 2, p. 6 |
| **Regroupement des doublons par distance prédictive** (conception v3 §3 : distance au sens du nul, calculée par programme sur instances publiques sans issue, lien complet, ε = 0,01 nat, valeur e de groupe, preuve) | [FF] ne retire que les doublons **exacts** (empreinte du contenu) ; il regroupe pour **décrire**, par juge modèle, plongement et k-moyennes ; rien n'entre dans la sélection | principe « grouper par ce que la solution fait, non par son texte » : **pris** ([FF]) ; notre mécanisme (sans modèle, avant le juge, avec validité statistique) : **ouvert** ; ensemble : **voisin à citer** | [FF] p. 18 : « Judging specifications rather than raw source keeps two artifacts edited from a common ancestor from being called similar merely because they read alike » ; p. 4 : « remove exact duplicates by content hash » |
| **Diversité par couverture d'oracle** (v3 §4, D2 : composantes plantées certifiées couvertes, additionnelles à l'archive) et D1 (nombre de groupes) | aucune vérité des idées : la diversité est lue sur la carte du juge ; l'analogue le plus proche est « bassin de la meilleure solution jamais atteint » ([Page]) | D2 : **ouvert** ; D1 (compter des groupes, suivre les passages) : **pris** comme mesure descriptive ([FF], [Page]) → **voisin à citer** | [FF] p. 4 : carte validée à 85 % contre son propre juge ; [Page] : « 58% never visit the basin where their task's best solution came from » |
| **N-058** — composition des proposeurs jugée sur l'oracle et le coût, jamais sur le verdict du juge | non traité ; [Page] rapporte des statistiques d'exploration par modèle, sans règle de composition | **ouvert** ; rien à citer au-delà de [Page] | — |

Deux rapprochements de forme, utiles pour écrire, qui ne sont pas des revendications :

- **Notre boucle à plusieurs générations est déjà, par construction, une remise à zéro à chaque génération** : chaque appel
  de proposeur est une séance neuve sans historique et la vue servie est l'archive (v3 §5.2 et §3.4, `386d48ba…`). Dans le
  vocabulaire de [FF], c'est « branches + contexte vidé + espace de travail hérité » à chaque tour ; dans celui de [SDF],
  nous sommes du côté « oubli », avec deux différences : nous gardons **toutes** les lois retenues (non le seul meilleur) et
  l'archive est aussi le **nul du juge**. Le contraste que ces articles mesurent (fil continu contre contexte neuf) n'existe
  donc pas dans notre course : un témoin « fil continu » serait à ajouter pour le mesurer (§6, b3).
- **Le constat C-1 de la v4** (la génération 1 prend toutes les fortes et moyennes ; v4 §1, `47e38ec0…`) est le cas que
  [FF] décrit par « When a task sits far below the agent's ability, every run finds the same optimal solution and the spread
  collapses » (p. 8) : voisin à citer pour la raison d'être des mondes riches et de MR-2.

## 6. Ce qu'on pourrait emprunter, par coût croissant

Règle commune à tout ce qui suit : **rien de ces mesures n'est servi à un agent ni n'entre dans une sélection** (N-053,
point 5 ; v3 §4.3) ; rien ne sert à composer les proposeurs (N-058) ; tout est calculé après la sélection scellée de la
génération.

### (a) Mesures descriptives, sans appel de plus

| mesure | définition proposée | analogue | ce qu'il faut au préenregistrement | risque |
|---|---|---|---|---|
| a1. **Sort de chaque proposition brute**, par proposeur et par génération | avec la distance et les seuils du regroupement (v3 §3.1), classer chaque carte : **déjà archivée** (sous ε d'une loi de l'archive du début de génération), **retour à un groupe écarté** (sous ε d'un groupe éliminé à une génération passée), **groupe neuf** | taux de changement d'idée 4 à 13 %, moitié de retours ([Page]) ; bassins visités ([FF] p. 4) | définitions gelées (mêmes ε et ε par strate ; sens exact d'« écarté » : mort au test de mort, non promu, non concluant) ; lecture descriptive, hors critères gelés ; rapportée par fournisseur comme information | « retour à un groupe écarté » dépend des verdicts du juge : ne doit jamais peser sur la composition (N-058) ; le lien complet coupe une idée en plusieurs groupes (v3 §3.6), donc « groupe neuf » surestime la nouveauté : toujours le lire à côté de D2 |
| a2. **Taille de pas prédictive** | distance au sens du nul entre chaque carte d'un proposeur à la génération g et sa plus proche à g − 1, et à l'archive | pas en unités du pas médian ([FF] p. 7) | idem ; unité : nat, sans plongement | faible : aucune carte, aucun juge modèle ; mais un proposeur sans mémoire n'a pas de « trajectoire » propre, c'est une suite par fournisseur |
| a3. **Effort par appel selon la taille de l'archive servie** | jetons de sortie (et de raisonnement s'ils sont rendus) par appel, par génération | lignes modifiées et jetons de raisonnement par tour ([SDF] figure 5, p. 8 ; p. 9) | champs d'usage déjà consignés (v3 §5.2) ; descriptif | les champs diffèrent selon les fournisseurs ; un écart de comptage n'est pas un effet |
| a4. **Appels sans carte utile** | part des appels qui rendent moins de cartes que demandé, ou des cartes refusées au gardien, et leur coût | tours sans candidat, 532 sur 763 ([SDF] p. 8) | compte déjà prévu par fournisseur (v3 §5.3) ; ajouter le coût | aucun |
| a5. **Composante la plus forte restante jamais couverte** | après la course, par monde et par fournisseur, sur D2 | « 58 % n'atteignent jamais le bassin de la meilleure solution » ([Page]) | déjà dans D2 (v3 §4.1) ; une ligne de lecture de plus | lu une seule fois, avec l'oracle |

### (b) Bras ou témoins nouveaux (appels payants : devis et GO)

| témoin | dessin | analogue | ce qu'il faut au préenregistrement | risque |
|---|---|---|---|---|
| b1. **Meilleur de N à coût égal** | N premières générations indépendantes au coût d'une course de G générations | meilleur de 4 ([FF] p. 5) ; 4 parallèles ([SDF] p. 5) | déjà exigé par N-045 §4 ; préciser que le coût est apparié en dollars mesurés | [FF] montre que ce témoin bat le fil continu simple : le battre n'est pas acquis |
| b2. **Paire « même état »** : vue pleine contre vue réduite | depuis la même archive scellée après la génération g, jouer g + 1 avec l'archive servie entière, ou avec la seule meilleure loi ; le nul du juge reste l'archive entière dans les deux bras | continuer contre oublier ([SDF] §4.3, p. 7-8) | états de départ scellés ; nombre de répliques fixé sur un plancher de bruit A/A ; critère sur D2, jamais sur un verdict ; la garde « vue servie = archive » (v3 §3.4) est à amender pour ce bras : **écart de dessin à écrire** | la synthèse du collisionneur **rejette** le masquage d'une partie de l'archive (synthèse, verdict, `4f99077b…`) : ce bras rouvre ce rejet, à dire ; chez nous l'archive est aussi le nul : une vue réduite fera re-proposer des lois connues (cartes perdues), ce que a1 mesure |
| b3. **Fil continu** | un proposeur garde sa séance d'une génération à l'autre | course simple ([FF]) ; « continue » ([SDF]) | même vue, même nombre de cartes ; coût en jetons d'entrée au devis | cher ; tous les relais ne tiennent peut-être pas une séance longue ; sans lui, on ne sait pas si notre séance neuve fait le travail que [FF] attribue à la remise à zéro |
| b4. **Consigne de diversité tirée au sort dans la génération** | une part des appels, tirée par permutation scellée, porte la mission ; les autres non | 2 branches dirigées sur K ([FF] p. 22) | même vue ; témoin de texte de même longueur (synthèse, rang 3) ; critère sur D2 des propositions brutes | précédent nul (46 % contre 50 %, 178 tours, [FF] p. 22) : puissance à calculer avant de payer ; Goodhart si la mission récompense la forme |
| b5. **Échelle de difficulté** | mondes gradués pour situer où la dispersion entre proposeurs est maximale | MAX-3-SAT ([FF] p. 8) | étalonnage hors mondes de test | coût d'appels pour une mesure d'étalonnage ; à ne faire que si C8 et D2 ne suffisent pas |

### (c) Carte des idées par triplets jugés, pour les idées en texte libre

- **Où elle servirait** : seulement là où aucune distance prédictive n'existe (fiches de l'atelier d'idées, réponses aux
  questions ouvertes de N-044 §4). Pour les lois de la grammaire, la distance prédictive de la v3 est exacte, sans modèle et
  sans coût : la carte n'y ajoute rien. Pour des organismes entiers (étape 2), une distance de comportement (accord des
  réponses sur le vivier de conception) me paraît le premier choix, la carte venant après ; c'est une suggestion, hors des
  pièces lues.
- **Méthode à reprendre** ([FF] p. 4, 18, 23-25 ; variantes de [Page]) : réécriture de chaque idée dans un schéma fixe qui
  retire le style ; triplets jugés sans note, sans chronologie, sans auteur ; chaque question posée dans les deux ordres et
  réponses peu sûres écartées ([Page]) ; plongement en deux dimensions ; part tenue à l'écart ; témoin « origine seule » ;
  second plongement en contrôle.
- **Ce qu'il faudrait au préenregistrement** : modèle juge figé, nommé, **d'une lignée autre que celles des proposeurs**
  (N-053, point 4 ; [FF] ne nomme pas le sien, p. 18) ; nombre de triplets, part tenue à l'écart et seuil d'accord gelés ;
  règle du nombre de groupes gelée ; et, avant tout usage, une **validation contre une vérité** que ni [FF] ni [Page]
  n'ont : sur nos mondes plantés, décrire des lois en texte, faire juger les triplets, et comparer l'ordre du juge à l'ordre
  de la distance prédictive et à la couverture de composantes (D2). Sans cette épreuve, la carte ne mesure que l'avis de son
  juge.
- **Risques** : juge à modèle (préférence pour sa famille ; un seuil tiré d'un juge mesure la proximité au juge, non la
  redondance — objection déjà notée dans la synthèse, rang 2) ; la taille d'un saut dépend du plongement (43 contre 10,1,
  [FF] p. 7, 17-18) ; le nombre de groupes dépend d'un réglage ; **Goodhart** dès qu'un agent voit la carte ou qu'elle
  pèse sur une sélection (un texte peut se donner l'air différent) ; coût en appels du juge (devis et GO ; [FF] ne chiffre
  pas le sien ; le chiffre de [Page] vient d'un petit modèle maison). Usage admissible : **descriptif seulement**.

## 7. Zones revendiquées trouvées occupées, et points de vigilance

### 7.1 Zone revendiquée trouvée occupée

**Aucune**, dans les énoncés lus (N-044 §1 à §5 ; N-045 v2 §1 à §8 ; N-064 §1 à §4 ; N-065 §1 à §4 ; N-058). Réserve
nette : les revendications **O1, O3 à O10 et O13 à O20** de l'organisme d'idéation ne sont pas dans les pièces nommées ; si
l'une porte sur la diversité des idées, les plateaux, l'héritage entre générations ou la remise à zéro du contexte, elle
est à confronter à [FF] et [SDF] par quelqu'un qui en a le texte.

### 7.2 Trois points de vigilance (pas des nœuds en l'état ; à la mère de juger s'ils montent à Lazar)

1. **Ne pas revendiquer le principe** « regrouper les idées par leur fonction et compter les idées en groupes » : il est
   pris pour des artefacts libres ([FF] p. 4, 18) et repris à grande échelle ([Page]). Ce qui reste nôtre, au regard de ces
   pièces : la distance prédictive calculée par programme, placée avant le juge, avec valeur e de groupe et preuve (v3 §3),
   et la mesure contre un oracle (v3 §4).
2. **« Séquentiel contre meilleur de N à budget égal » est mesuré dans une tâche** ([FF] table 1, p. 5 ; [SDF] table 1,
   p. 6). La condition de N-045 §4 (sur familles tenues à l'écart) n'est pas touchée, mais tout texte doit citer ces deux
   résultats, et notre jeu de témoins devrait contenir la reprise du meilleur avec contexte neuf.
3. **La prémisse de N-045 §5** (ce qu'une génération lègue aide les suivantes, donc il faut le récompenser) rencontre un
   résultat contraire dans un cadre voisin : jeter la séance et l'historique des candidats et ne garder que le meilleur
   gagne plus que continuer ([SDF] table 3, p. 8). Ce n'est pas une occupation ; c'est une raison d'écrire, dans tout
   préenregistrement qui récompense l'héritage, un bras où l'héritage est réduit au meilleur (§6, b2), faute de quoi un
   gain attribué à la mémoire transmise ne se distinguerait pas d'un gain du simple redémarrage.

### 7.3 Propositions (aucune n'est appliquée ici)

- Ajouter [FF] et [SDF] à la liste des **citations obligatoires** de N-064 §4 pour tout texte qui présente la boucle à
  plusieurs générations (voisins de la forme, au même titre que Co-Scientist) : modifier une décision est le mot de Lazar.
- **Lectures R8 à faire avant de dire « ouvert »** (toutes au niveau transcription : je n'en connais que la citation) —
  citées par [SDF] p. 3, 9-12 : Lee et al., Meta-Harness (arXiv 2603.28052 : un agent réécrit le banc autour d'un modèle et
  garde les versions mieux notées — proche de N-044 et N-045 §1) ; Liu et al., EvoX (2602.23413 : stratégie de recherche
  elle-même évoluée) ; Cemri et al., AdaEvolve (2602.20133 : budget réparti entre populations quand la recherche cale) ;
  Zhang et al., Stateless Language Agents (2610.07625) ; He et al., « Beneath the diff » (2609.00077 : effondrement de mode
  dans les boucles de recherche autonome — proche des doublons) ; Ann et al., « The interaction tax » (2608.23541 : la
  communication efface la diversité) ; Yang et al. (2602.03794 : diversité et passage à l'échelle des systèmes à agents) ;
  Park et al. (2609.21032 : communication au moment de l'inférence) ; Virk et al., SwarmResearch (2607.02807) ; Tan et al.,
  Recovery-Bench (2025 : hériter l'historique d'échecs nuit) ; Kim et al. (2512.08296) — et, citée par [FF] p. 9, 11 : Falck
  et al., « Training AI scientists to replicate research » (2608.13331 : distillation de trajectoires dans les poids —
  proche de la « distillation du concepteur » de N-045 §4). Je ne sais pas lesquelles le dépôt connaît déjà.

## 8. Limites de ma lecture

- Versions 1 d'arXiv seulement ; des versions ultérieures peuvent différer.
- Figures : lues en image à basse définition pour [FF] p. 1, 3, 7, 21 et [SDF] p. 1, 8 ; les autres (dont [FF] figure 7,
  p. 20, et [SDF] figure 4, p. 7) par leur légende et le texte ; aucune valeur n'est relevée sur une courbe.
- Les comptes « 5 tâches sur 11 » et « 8 lignes sur 11 » du §2.5 sont **les miens**, faits à la main sur la table 3 de [FF]
  (p. 15) ; les auteurs ne les donnent pas.
- Les noms de modèles et d'outils sont recopiés des PDF tels quels ; je n'ai rien vérifié hors des PDF.
- Aucun travail cité par ces pièces n'a été lu (niveau transcription) ; aucun travail **citant** ces pièces n'a été cherché.
- [Page] : billet d'entreprise, lu dans son texte archivé ; ses figures n'y sont pas ; ses chiffres ne sont pas opposables
  au sens de R7.
- De nos pièces, je n'ai lu que celles nommées : ni le programme, ni l'état de l'art, ni la liste O1 à O20, ni le
  préenregistrement de la course ; de la v3, les sections 3 à 5 ; de la v4, l'en-tête et les sections 0 à 2. Le « miroir
  fonctionnel » de N-044 §5 n'est défini dans aucune pièce lue : si c'est un résumé de ce que font les candidats, la
  réécriture en spécification fonctionnelle de [FF] (p. 18) en est le voisin de méthode ; je ne l'affirme pas.
- Les statuts « ouvert » valent **au regard de ces trois pièces** ; ils ne sont pas une recherche d'antériorité.
