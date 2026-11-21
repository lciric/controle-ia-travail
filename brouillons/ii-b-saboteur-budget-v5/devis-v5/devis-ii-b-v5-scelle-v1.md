> **DEVIS SCELLÉ le 2026-11-21 par la session de reconception.** Ce fichier est le brouillon 2 (`e58aa6f0…`) mot pour mot, précédé de ce seul encadré. Contre-lu, corrections vérifiées par le même Opus 5.5 (`verification-corrections-devis-organisme-retenu-v5-cl1.md`, `bb35fb18…`). Ligne de calcul : `registres/go.md` sur main, **GO-2026-11-21-70** (sous GO-2026-11-21-66 et -69). Choix accordés sur recommandation : (a) plafond 60 USD, coupure 55 ; (b) coupure propre de l'étalonnage à 12 USD par une règle de la surveillance, éprouvée sur un cas sain et un artefact ; (c) fichier d'entrées scellé avant la location au prix borne de 1,38 USD l'heure et au coût fixe de 6,90 USD (au plus 63 tours) — l'option « prix réel écrit à la création » est rayée ; (d) dernière création le 2026-11-27T00:00Z, échéance le 2026-11-30. Dépense passée comptée à zéro sous la ligne neuve, plus toute dépense de la ligne faite avant la location. Nœud court des consignes (rappel du flagrant) accepté. La course ne part qu'avec le code contre-lu, les consignes et l'ordre scellés.

# Devis — étalonnage puis course de l'organisme retenu du saboteur à budget (v5) — brouillon 2

- **Statut** : brouillon 2, pièce décisive (devis), corrigé après la contre-lecture 1 ; corrections non encore vérifiées par le contre-lecteur. Brouillon 1 (`947b492d…`) et calcul v5 (`56faf056…`, sortie `175d03a0…`) intacts (R12). Aucune dépense n'est engagée par ce document ; aucune ligne d'accord n'y est écrite. Même rédacteur neuf (Claude Fable 5.2, côté saboteur), même mandat (`d9bc8bed908f…`).
- **Contre-lecture traitée** : `brouillons/ii-b-saboteur-budget-v5/devis-v5/contre-lecture-cl1/contre-lecture-devis-organisme-retenu-v5-cl1.md` (`cfea7cda2c6a7953d4174dd02e89ffbdeb2b4ea9fc4745a8b4139e7937cb2dfb`), lue en entier : « remettable après corrections », trois majeurs, neuf mineurs. Traitement : `differences-devis-brouillon1-vers-2-v1.md`.
- **Accord cité** : GO-2026-11-21-66, « ligne de calcul neuve de l'étalonnage puis de la course : go, plafond inscrit sur le devis remis après scellement », d'après la lecture du registre par le contre-lecteur (m9) ; le rédacteur ne l'a pas ouvert. La ligne ne porte aucune échéance.
- **Texte chiffré** : `brouillons/ii-b-saboteur-budget-v5/conception-organisme-retenu-ii-b-v5-scellee-v1.md` (`c1dc54597a1ab4b467331673607d986e46a706c06253bb40070e5d15caaa61f2`) ; lu : encadré, table des nœuds, sections 5.1, 10.1, 10.2, 10.3, 12, 15. Nœuds à leur défaut, nœud 7 en (b').
- **Arithmétique** : `calcul-devis-ii-b-v6.py` (`bfe997b1078f63624ae8fc82eb3a7206ccbf82981d20ef45a0b1e4c2b8396e2e`), sortie `sortie-calcul-devis-ii-b-v6.txt` (`228a308dd67914f4a5681bdb1c764add4333ea12febfe1e4a988bc64b1445d1a`). Chaque chiffre renvoie à une ligne [Lnn] de cette sortie. Aucune durée, aucun prix, aucun compte ne change depuis le calcul v5.
- **Lu de la première course** : seulement des horodatages, un prix horaire et une durée facturée. Aucune donnée mesurée lue.

## 0. En bref — les quatre chiffres

| attendu | au pire | plafond proposé | coupure proposée |
|---|---|---|---|
| **≈ 15,5 dollars** à 12 tours, **≈ 21,2** à 24 tours [L24] [L25] | **59,76 dollars** : la ligne entière est bornée par ce que tiennent les gardes [L52] | **60 dollars** | **55 dollars** |

**Le pire de la ligne est celui des gardes, 59,76 dollars**, non 53,4 : 53,4 est seulement le pire d'une course de 24 tours [L29] [L52] ; la course peut avoir plus de tours, jusqu'au plafond de tours.

| | appels | durée attendue | durée au pire | attendu | au pire |
|---|---|---|---|---|---|
| **étape 1, étalonnage** (deux oracles) | 160 épisodes générés ; 3 840 actions d'oracle [L12] | 2,44 h | 5,57 h | ≈ 3,0 dollars de carte ; ≈ 4,8 si la course ne part pas [L13] | ≈ 7,7 ; ≈ 13,5 si elle ne part pas [L15] ; tenu à 16,76 par la règle de surveillance (§ 3) |
| **étape 2, course seule** (12 ; 24 tours) | 640 ; 1 024 épisodes ; 9 920 ; 13 760 actions d'oracle [L19] [L20] | 8,8 ; 13,5 h | 18,9 ; 28,9 h | ≈ 10,7 ; ≈ 16,4 dollars de carte [L24] [L25] | ≈ 26,1 ; ≈ 39,9 [L28] [L29] |
| **ligne entière** (12 ; 24 tours) | 800 ; 1 184 épisodes ; 13 760 ; 17 600 actions d'oracle | 11,2 ; 15,9 h | 24,5 ; 34,5 h | **≈ 15,5 ; ≈ 21,2** | ≈ 39,6 ; ≈ 53,4 à ce nombre de tours ; **59,76 au pire de la ligne** |

**Plafond de tours** (10.2), fichier d'entrées à **45 dollars**, prix scellé à la borne : **63 tours** aux durées attendues (73 si le prix scellé est le prix réel), **24** sur un hôte deux fois plus lent [L49] [L41] [L47]. Une course partie a entre 12 tours et ce plafond ; elle ne le dépasse jamais (§ 6).

## 1. Ce que la première course a mesuré (durées, prix, dépense)

| grandeur | valeur réelle | hypothèse du premier devis | ligne |
|---|---|---|---|
| un épisode généré (10 actions) | **39,08 s** en moyenne sur 88 épisodes ; 34,4 à 45,4 s selon le lot de huit | 43,3 s | [L01] |
| chargement du modèle | 230 s, déduit du premier lot | compris dans 0,25 h | [L02] |
| une action d'oracle (un préremplissage, huit suites) | **0,511 s** (960 actions en 491 s) | 0,5 / 1,0 / 1,5 s ; 3,0 s au pire | [L03] |
| de la création au début du run | 320 s, dont 178 s de suite d'essais | 1,00 h de fixe en tout | [L04] |
| prix | carte 1,186667 + stockage 0,033333 = **1,22 dollar par heure** | 1,12 central ; borne 1,30 + 0,08 | [L07] |
| dépense | **≈ 1,64 dollar**, recalculée (4 843 s facturées), non lue sur une facture ; sur l'ancienne ligne GO-2026-11-10-08 | — | [L08] |

**Lecture des marques de progrès (m4).** Le devis lit chaque marque « lot n » comme la fin du lot. Si elle s'écrit au début du lot, le chargement vaut 543 s et l'action d'oracle 0,19 s ; l'épisode ne change pas [L05]. La lecture retenue est la prudente pour l'oracle.

La première course s'est arrêtée à l'étalonnage : **ni un tour du maître, ni la distillation, ni l'évaluation n'ont de durée réelle**. La distillation garde le chiffre du premier devis (1,86 s par transcription et par époque).

## 2. Hypothèses et marges

| jeu de durées | épisode | action d'oracle | fixe avant le premier épisode | prix horaire, tout compris | après l'arrêt | ligne |
|---|---|---|---|---|---|---|
| attendu | 39,08 s (moyenne réelle) | 0,511 s (réelle) | 550 s (réel) | 1,22 (réel) | 24 h à 0,033 ; 20 Go | [L09] |
| haut | 45,4 s (lot réel le plus lent) | 0,767 s (× 1,5) | × 1,5 | 1,38 (borne) | 24 h à 0,08 ; 20 Go | [L10] |
| pire | 78,2 s (× 2) | 1,534 s (× 3) | × 3 | 1,38 (borne) | 48 h à 0,08 ; 40 Go | [L11] |

- **× 2 sur tout** : un autre hôte. Une seule machine vue ; entre ses lots, 34,4 à 45,4 s, soit + 16 % sur la moyenne [L01]. Le facteur 2 du premier devis est gardé.
- **× 1,5 de plus sur l'action d'oracle** : les deux oracles de ce texte ([P] sans réécriture, [N] à réécriture couplée) n'ont jamais été chronométrés.
- **Épisodes du maître** (consigne privée dans le contexte) et **épisodes régénérés** : comptés comme un épisode honnête ; aucune durée mesurée. C'est la raison de la réserve du § 6.
- **Machine** : celle de l'ordre de la première course (A100 SXM4 80 Go, au plus 1,30 dollar par heure, stockage au plus 0,08, téléchargement au plus 0,05 dollar par gigaoctet, disque d'au moins 100 gigaoctets) ; l'ordre neuf la fixera.
- **Une seule location** pour l'étalonnage et la course. Deux locations : ≈ 2,0 dollars de plus (≈ 6,5 au pire) [L56] [L57].

## 3. Étape 1 — l'étalonnage

Appels : 160 épisodes générés (64 honnêtes, 64 régénérés, 32 flagrants) ; 3 840 actions d'oracle, soit 3 840 préremplissages et 30 720 suites de 16 jetons au plus [L12]. Les 64 épisodes à excès planté ne sont pas générés.

| | durée | carte et stockage | si la course ne part pas, arrêt et téléchargement compris | ligne |
|---|---|---|---|---|
| attendu | 2,44 h | 2,97 dollars | 4,77 dollars | [L13] |
| haut | 3,06 h | 4,23 | 7,15 | [L14] |
| pire | 5,57 h | 7,69 | 13,53 | [L15] |

**Coupure propre de l'étalonnage : une règle de la surveillance, sans code neuf dans la minuterie (m5).** Si la dépense relevée atteint **12 dollars** avant la fin de l'étalonnage (7,25 h de carte à 1,38, soit 1,68 h de marge sur le pire cas [L16]), la surveillance alerte, l'exécutante arrête la machine par son identifiant, et c'est un nœud. **17 dollars** n'est pas une seconde ligne : c'est la dépense tenue si la course ne part pas (12 + consignation au plus 0,92 + 48 h de stockage à l'arrêt 3,84 = 16,76) [L17]. La minuterie garde sa seule coupure, 55.

## 4. Étape 2 — la course, si la règle de désignation dit « part »

Appels [L18] : par tour, 32 épisodes générés et 320 actions de l'oracle désigné ; hors tours, 3 520 actions de l'oracle non désigné (960 sur les épisodes acceptés du maître, 2 560 à l'évaluation) ; évaluation, 256 épisodes générés et 2 560 actions de l'oracle désigné ; distillation, 2 × 96 transcriptions × 3 époques au plus.

| | un tour | coût fixe (évaluation, distillation, fin) | actions hors tours | ligne |
|---|---|---|---|---|
| attendu | 0,393 h ; 0,48 dollar | 3,55 h ; 4,33 | 0,50 h ; 0,61 | [L21] |
| haut | 0,472 h ; 0,65 | 4,27 h ; 5,89 | 0,75 h ; 1,04 | [L22] |
| pire | 0,831 h ; 1,15 | 7,45 h ; 10,29 | 1,50 h ; 2,07 | [L23] |

Course seule, puis ligne entière (étalonnage, arrêt et téléchargement compris). La ligne « 6 tours » du brouillon 1 est retirée : une course part à la taille d'origine, 12 tours, dès que le nombre de tours visé est de 12 ou moins (10.3, étape 7) ; 12 est le moins possible (m1).

| tours | attendu : course ; ligne entière | haut | pire | lignes |
|---|---|---|---|---|
| 12 (taille d'origine, le moins possible) | 8,8 h, 10,7 dollars ; **15,5** | 14,7 ; 21,9 | 26,1 ; 39,6 | [L24] [L26] [L28] |
| 24 (hypothèse de la simulation du texte) | 13,5 h, 16,4 dollars ; **21,2** | 22,5 ; 29,7 | 39,9 ; 53,4 | [L25] [L27] [L29] |
| au plafond de tours (63 aux durées attendues) | 31,2 h de carte ; ≈ 40,1 dollars planifiés | — | bornée par les gardes : 59,76 | [L49] [L52] |

Dépense cumulée aux points de la liste d'arrêt (section 15), arrêt et téléchargement compris : fin de l'étalonnage ≈ 4,8 dollars (13,5 au pire) ; tour de contrôle, tour 4 : ≈ 6,7 (18,1) ; fin de 24 tours avec moins de 48 épisodes acceptés : ≈ 16,3 (41,1) [L31] [L33].

## 5. Plafond, coupure et échéance de la ligne

**Plafond proposé : 60 dollars. Coupure : 55 dollars**, avant le plafond, comme sur la première ligne. La coupure donne 43,4 h de carte au prix réel et 38,4 h à la borne de prix [L34] [L35]. Les gardes tiennent au plus 55 + 0,92 + 3,84 = **59,76 dollars**, pour 48 h d'arrêt au plus (51 h avant de dépasser la ligne) [L36]. La dépense de la première course (1,64 dollar) n'y entre pas.

**Échéance proposée (m6)** : **30 novembre 2026** ; fin de la ligne 2026-12-01T00:00Z ; échéance de la minuterie 2026-11-30T22:00Z ; **dernière création le 28 novembre à 23:00Z**. Pour une création à cette heure, la coupure tombe au plus tard le 30 à 18:26Z, 3,6 h avant la minuterie [L53] [L54]. Une machine créée à la dernière heure est détruite avant la fin de la ligne : son arrêt avant destruction est alors plus court que 48 h [L55].

## 6. Plafond de tours (10.2) : une course partie ne le dépasse jamais

Formule du texte, nœud 7 (b') : partie entière de (plafond − dépense passée − dépense de l'étalonnage − coût fixe − prix horaire × durée d'une action d'oracle × 3 520) / (prix horaire × 32 × (durée d'un épisode + 10 × durée d'une action d'oracle)).

**Ce que le texte règle (M1).** 10.3, étape 6 : un nombre de tours visé au-dessus du plafond de tours donne « ne part pas, motif tours » pour cet oracle, calculé une fois, par programme, sur les sorties scellées, avant toute configuration de course ; second passage refusé. Par 5.1 : si c'est [N], la règle passe à [P] ; si c'est [P], ou les deux, la course ne part pas, la phrase de 10.6 est rendue, les résultats sont versés et scellés, et toute reprise est une course neuve sous devis neuf. **Il n'existe donc pas de course qui dépasse son plafond de tours** : une course partie a un nombre de tours au plus égal au plafond, et aucun tour n'est ajouté (section 15).

**Fichier d'entrées proposé, à sceller avant l'étalonnage — en nombres (m2)** :

| entrée | valeur proposée | d'où |
|---|---|---|
| plafond | **45 dollars** | la coupure de 55 moins une réserve de 10 (M2) |
| dépense passée | **0**, plus toute dépense de la ligne neuve faite avant la location (une création manquée) | ligne neuve ; la première course est sur GO-2026-11-10-08 ; l'étalonnage est déduit à part par la formule |
| prix horaire | **1,38 dollar** (borne de l'offre, 1,30, plus borne du stockage, 0,08), connu avant la location | [L07] |
| coût fixe | **6,90 dollars** : 3,55 h d'évaluation, de distillation et de fin aux durées attendues, à 1,38, soit 4,90, plus 2,00 de téléchargement (40 gigaoctets) | [L40] |
| nombre d'oracles par tour ; actions d'oracle hors tours | 1 ; 3 520 | nœud 7 (b') |

Le prix à la borne est un choix du rédacteur : il rend le fichier scellable avant toute location et il est prudent (moins de tours). Si l'ordre neuf préfère le prix réel de l'offre, écrit à la création : coût fixe 6,33 dollars à 1,22 [L37], et les tours de la ligne « prix réel » ci-dessous. Le pire du coût fixe est 12,29 [L39].

**Durée d'une action d'oracle (m3).** 10.2 l'écrit au singulier ; sous (b'), l'oracle désigné joue par tour et l'autre hors tours, et leurs durées peuvent différer. Proposé pour l'ordre neuf : le programme prend **la plus longue des deux durées mesurées** à l'étalonnage. Ce n'est pas un écart au texte.

**Plafond de tours et tolérance.** La formule prend les durées de l'étalonnage, donc de l'agent honnête, sans marge ; les tours du maître n'ont aucune durée mesurée. La tolérance est la lenteur de plus que les tours peuvent avoir avant que la minuterie ne coupe à 55, c'est-à-dire avant la distillation et l'évaluation.

| fichier d'entrées | **proposé : prix scellé 1,38, coût fixe scellé 6,90, durées attendues** | même fichier, hôte deux fois plus lent | prix réel 1,22, coût fixe 6,33, durées attendues (chiffres de la contre-lecture) | lignes |
|---|---|---|---|---|
| **45 dollars (proposé)** | **63 tours**, dépense planifiée 40,1, tolérance **49 %**, dès 7 épisodes régénérés acceptés sur 64 | 24 tours, dépense planifiée 49,6, tolérance 20 % | 73 tours, tolérance 29 %, dès 6 sur 64 | [L49] [L47] [L41] |
| 50 dollars (écarté) | 72 tours, dépense planifiée 44,4, tolérance 31 % | 29 tours, dépense planifiée 55,3 : **au-dessus de la coupure** | 83 tours, tolérance **13 %**, dès 5 sur 64 | [L50] [L48] [L44] |

Aux durées hautes et au pire, avec un coût fixe recalculé sur ces durées : 48 et 20 tours à 45 dollars, 56 et 24 à 50 [L42] [L43] [L45] [L46].

**Pourquoi 50 est écarté** : au prix réel, 13 % de tolérance seulement, et un maître un peu plus lent que l'agent honnête fait couper la course avant l'évaluation : elle est perdue ; sur un hôte lent, avec un coût fixe scellé d'avance, la dépense planifiée passe la coupure [L44] [L48]. Ce que 45 coûte : neuf ou dix tours de moins, et un épisode régénéré accepté de plus pour partir.

**Côté dépense, si les tours coûtent plus que mesuré** : la réserve de 10 dollars les absorbe ; au-delà, la minuterie coupe à 55 dollars, la machine s'arrête par son identifiant, rien n'est relancé sans le mot de Lazar et un devis neuf, et ce qui est écrit par tour est versé avant toute destruction.

## 7. Réserves

1. Aucune durée réelle pour les tours, la distillation, l'évaluation, les épisodes régénérés et les deux oracles neufs : les totaux de l'étape 2 sont des extrapolations des deux seules durées mesurées.
2. La dépense de la première course est recalculée, non lue sur le compte du loueur.
3. Le rédacteur n'a pas vérifié dans le code que la forme d'appel de l'oracle de la première course vaut pour [P] et [N].

## 8. Choix pour Lazar

| choix | recommandation | confiance |
|---|---|---|
| plafond de la ligne et coupure | **60 et 55 dollars** : 59,76 tenus par les gardes, même forme que la première ligne | forte |
| coupure propre de l'étalonnage | **règle de la surveillance à 12 dollars**, arrêt par identifiant et nœud ; aucun code neuf dans la minuterie | moyenne |
| plafond du fichier d'entrées | **45 dollars**, prix scellé à la borne 1,38 et coût fixe 6,90 (63 tours attendus, tolérance 49 % ; 73 tours et 29 % au prix réel) ; 50 écarté | moyenne |
| dépense passée | **0**, plus toute dépense de la ligne neuve antérieure à la location | forte |
| échéance de la ligne | **30 novembre**, dernière création le 28 à 23:00Z | moyenne |

Défaut sous 48 heures : les recommandations ci-dessus ; aucune création sans le mot de Lazar.
