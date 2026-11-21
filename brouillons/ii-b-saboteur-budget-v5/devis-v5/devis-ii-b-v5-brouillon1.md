# Devis — étalonnage puis course de l'organisme retenu du saboteur à budget (v5) — brouillon 1

- **Statut** : brouillon 1, pièce décisive (devis), **non contre-lu**. Aucune dépense n'est engagée par ce document ; aucune ligne d'accord n'y est écrite. Écrit le 2026-11-21 par un rédacteur neuf (Claude Fable 5.2, côté saboteur), mandat `registres/iib-reconception/mandat-redacteur-devis-organisme-retenu-v5-v1.md` (`d9bc8bed908f…`, vérifié).
- **Accord cité** : GO-2026-11-21-66 (ligne de calcul neuve, plafond à inscrire sur ce devis), d'après le mandat et l'encadré du texte scellé ; le registre des accords n'a pas été ouvert par le rédacteur.
- **Texte chiffré** : `brouillons/ii-b-saboteur-budget-v5/conception-organisme-retenu-ii-b-v5-scellee-v1.md` (`c1dc54597a1ab4b467331673607d986e46a706c06253bb40070e5d15caaa61f2`, vérifié) ; lu : encadré, table des nœuds, sections 10.1, 10.2, 12, 15 seulement. Nœuds à leur défaut, nœud 7 en (b') : un oracle par tour, 3 520 actions d'oracle hors tours.
- **Arithmétique** : `calcul-devis-ii-b-v5.py` (`56faf0568c7c94027b11d9fd5c6c5fe48523538970bb105106a12e3c6c46184d`), sortie `sortie-calcul-devis-ii-b-v5.txt` (`175d03a0c1b722409772d614baa55b990952d3b7e4814d555f7d1f4fe184e134`). Chaque chiffre ci-dessous renvoie à une ligne [Lnn] de cette sortie.
- **Lu de la première course** : seulement des horodatages, un prix horaire et une durée facturée (branche `origin/claude/iib-executante-v1`, dossier `registres/iib-executante/course-836c7ccc-v1/` : journal de l'instance, première ligne de la surveillance, journal de destruction, lignes 173 à 175 du diagnostic, inventaire). Aucune donnée mesurée lue.

## 0. En bref

| | appels | durée attendue | durée au pire | total attendu | total au pire | plafond proposé | coupure proposée |
|---|---|---|---|---|---|---|---|
| **étape 1, étalonnage** (deux oracles) | 160 épisodes générés ; 3 840 actions d'oracle [L11] | 2,44 h [L12] | 5,57 h [L14] | ≈ 3,0 dollars de carte ; ≈ 4,8 si la course ne part pas (arrêt et téléchargement compris) [L12] | ≈ 7,7 ; ≈ 13,5 si elle ne part pas [L14] | **17 dollars** [L16] | **12 dollars** [L15] |
| **étape 2, course** (12 tours ; 24 tours) | 640 ; 1 024 épisodes générés ; 9 920 ; 13 760 actions d'oracle [L19] [L20] | 8,8 h ; 13,5 h [L25] [L26] | 18,9 h ; 28,9 h [L31] [L32] | ≈ 10,7 ; ≈ 16,4 dollars de carte [L25] [L26] | ≈ 26,1 ; ≈ 39,9 [L31] [L32] | ligne entière | ligne entière |
| **les deux, ligne entière** (12 tours ; 24 tours) | 800 ; 1 184 épisodes ; 13 760 ; 17 600 actions d'oracle [L19] [L20] | 11,2 h ; 15,9 h | 24,5 h ; 34,5 h | **≈ 15,5 ; ≈ 21,2 dollars** [L25] [L26] | **≈ 39,6 ; ≈ 53,4 dollars** [L31] [L32] | **60 dollars** [L39] | **55 dollars** [L38] |

**Plafond de tours** qui en découle (10.2), avec un plafond du fichier d'entrées de 50 dollars (la coupure moins une réserve de 5) : **83 tours** aux durées attendues, **24 tours** aux durées du pire cas [L40] [L42]. Sa valeur vraie ne se calcule qu'avec les durées mesurées à l'étalonnage (10.2).

## 1. Ce que la première course a mesuré (durées, prix, dépense)

| grandeur | valeur réelle | hypothèse du premier devis | ligne |
|---|---|---|---|
| un épisode généré (10 actions) | **39,08 s** en moyenne sur 88 épisodes ; 34,4 à 45,4 s selon le lot de huit | 43,3 s | [L01] |
| chargement du modèle | 230 s, déduit du premier lot | compris dans 0,25 h | [L02] |
| une action d'oracle (un préremplissage, huit suites) | **0,511 s** (960 actions en 491 s) | 0,5 / 1,0 / 1,5 s ; 3,0 s au pire | [L03] |
| de la création au début du run | 320 s, dont 178 s de suite d'essais | 1,00 h de fixe en tout | [L04] |
| prix | carte 1,186667 + stockage 0,033333 = **1,22 dollar par heure** | 1,12 central ; borne 1,30 + 0,08 | [L06] |
| dépense | **≈ 1,64 dollar**, recalculée (4 843 s facturées), non lue sur une facture ; elle est sur l'ancienne ligne GO-2026-11-10-08 | — | [L07] |

La première course s'est arrêtée à l'étalonnage : **ni un tour du maître, ni la distillation, ni l'évaluation n'ont de durée réelle**. La distillation garde le chiffre du premier devis (1,86 s par transcription et par époque, jamais mesuré sur ce banc).

## 2. Hypothèses et marges

| jeu de durées | épisode | action d'oracle | fixe avant le premier épisode | prix horaire, tout compris | après l'arrêt | ligne |
|---|---|---|---|---|---|---|
| attendu | 39,08 s (moyenne réelle) | 0,511 s (réelle) | 550 s (réel) | 1,22 (réel) | 24 h à 0,033 ; 20 Go | [L08] |
| haut | 45,4 s (lot réel le plus lent) | 0,767 s (× 1,5) | × 1,5 | 1,38 (borne) | 24 h à 0,08 ; 20 Go | [L09] |
| pire | 78,2 s (× 2) | 1,534 s (× 3) | × 3 | 1,38 (borne) | 48 h à 0,08 ; 40 Go | [L10] |

Justification des marges du pire cas par les durées réelles :
- **× 2 sur tout** : un autre hôte. La première course n'a vu qu'une machine ; entre ses lots, l'écart est de 34,4 à 45,4 s, soit + 16 % sur la moyenne [L01]. Le facteur 2 du premier devis est gardé : rien de mesuré ne permet de le resserrer.
- **× 1,5 de plus sur l'action d'oracle** : les deux oracles de ce texte ([P] sans réécriture, [N] à réécriture couplée) n'ont jamais été chronométrés. Le texte dit que le couplage ne coûte aucun appel (section 12) ; je n'ai pas vérifié dans le code que la forme d'appel de la première course (préfixe partagé entre les huit suites) vaut pour eux.
- **Épisode régénéré** compté comme un épisode honnête : même nombre d'actions générées ; non mesuré.
- **Machine** : celle de l'ordre de la première course (A100 SXM4 80 Go, au plus 1,30 dollar par heure, stockage au plus 0,08, téléchargement au plus 0,05 dollar par gigaoctet, disque d'au moins 100 gigaoctets). Hypothèse : inchangée ; l'ordre neuf la fixera.
- **Une seule location** pour l'étalonnage et la course. Deux locations coûteraient ≈ 2,0 dollars de plus (≈ 6,5 au pire) [L47] [L48].

## 3. Étape 1 — l'étalonnage

Appels : 160 épisodes générés (64 honnêtes, 64 régénérés, 32 flagrants) ; 3 840 actions d'oracle, soit 3 840 préremplissages et 30 720 suites de 16 jetons au plus [L11]. Les 64 épisodes à excès planté ne sont pas générés.

| | durée | carte et stockage | si la course ne part pas, arrêt et téléchargement compris | ligne |
|---|---|---|---|---|
| attendu | 2,44 h | 2,97 dollars | 4,77 dollars | [L12] |
| haut | 3,06 h | 4,23 | 7,15 | [L13] |
| pire | 5,57 h | 7,69 | 13,53 | [L14] |

**Coupure proposée : 12 dollars** : 7,25 h de carte à 1,38, soit 1,68 h de marge sur le pire cas [L15]. **Plafond proposé : 17 dollars** : 12 + consignation de la minuterie (au plus 0,92) + 48 h de stockage à l'arrêt (3,84) = 16,76 tenus par les gardes [L16].

## 4. Étape 2 — la course, si la règle de désignation dit « part »

Appels [L17] : par tour, 32 épisodes générés et 320 actions de l'oracle désigné ; hors tours, 3 520 actions de l'oracle non désigné (960 sur les épisodes acceptés du maître, 2 560 à l'évaluation) ; évaluation, 256 épisodes générés et 2 560 actions de l'oracle désigné ; distillation, 2 × 96 transcriptions × 3 époques au plus.

| | un tour | coût fixe (évaluation, distillation, fin) | actions hors tours | ligne |
|---|---|---|---|---|
| attendu | 0,393 h ; 0,48 dollar | 3,55 h ; 4,33 | 0,50 h ; 0,61 | [L21] |
| haut | 0,472 h ; 0,65 | 4,27 h ; 5,89 | 0,75 h ; 1,04 | [L22] |
| pire | 0,831 h ; 1,15 | 7,45 h ; 10,29 | 1,50 h ; 2,07 | [L23] |

Course seule, puis ligne entière (étalonnage, arrêt et téléchargement compris) :

| tours | attendu : course ; ligne entière | haut | pire | lignes |
|---|---|---|---|---|
| 6 (le moins possible, 384 / 64) | 6,4 h, 7,8 dollars ; **12,6** | 10,8 ; 18,0 | 19,2 ; 32,8 | [L24] [L27] [L30] |
| 12 | 8,8 h, 10,7 dollars ; **15,5** | 14,7 ; 21,9 | 26,1 ; 39,6 | [L25] [L28] [L31] |
| 24 (hypothèse de la simulation du texte) | 13,5 h, 16,4 dollars ; **21,2** | 22,5 ; 29,7 | 39,9 ; **53,4** | [L26] [L29] [L32] |

Dépense cumulée aux points de la liste d'arrêt (section 15), arrêt et téléchargement compris : fin de l'étalonnage ≈ 4,8 dollars (13,5 au pire) ; tour de contrôle, tour 4 : ≈ 6,7 (18,1) ; fin de 24 tours avec moins de 48 épisodes acceptés : ≈ 16,3 (41,1) [L34] [L36].

## 5. Plafond et coupure de la ligne

**Plafond proposé : 60 dollars. Coupure : 55 dollars**, avant le plafond, comme sur la première ligne. La coupure donne 43,4 h de carte au prix réel et 38,4 h à la borne de prix [L37] [L38] ; le pire cas à 24 tours demande 34,5 h. Les gardes tiennent au plus 55 + 0,92 + 3,84 = 59,76 dollars, pour 48 h d'arrêt au plus (51 h avant de dépasser la ligne) [L39]. L'étape 1 a sa coupure propre (12) à l'intérieur de la ligne ; la dépense de la première course (1,64 dollar) n'y entre pas.

## 6. Plafond de tours (10.2) et dépassement

Formule du texte, nœud 7 (b') : partie entière de (plafond − dépense passée − dépense de l'étalonnage − coût fixe − prix horaire × durée d'une action d'oracle × 3 520) / (prix horaire × 32 × (durée d'un épisode + 10 × durée d'une action d'oracle)).

**Fichier d'entrées proposé, à sceller avant l'étalonnage** : plafond **50 dollars** (la coupure de 55 moins une réserve de 5, parce que la formule prend les durées de l'étalonnage sans marge) ; dépense passée 0 (ligne neuve) ; prix horaire : celui de l'offre retenue plus son stockage ; coût fixe : évaluation à un oracle, distillation, fin, plus 2 dollars de téléchargement (40 gigaoctets) ; un oracle par tour ; 3 520 actions hors tours.

| plafond du fichier d'entrées | durées attendues | hautes | pire | lignes |
|---|---|---|---|---|
| **50 dollars (proposé)** | **83 tours** | 56 | **24** | [L40] [L41] [L42] |
| 55 dollars (sans réserve) | 94 | 64 | 28 | [L43] [L44] [L45] |

À 50 dollars, le nombre de tours visé (384 / k_R, arrondi au-dessus) tient sous le plafond dès 5 épisodes régénérés acceptés sur 64 aux durées attendues, dès 16 au pire [L40] [L42]. À ce plafond, la location dure jusqu'à 39 h [L40] : l'échéance de la ligne doit laisser deux jours pleins après la création.

**Si la course dépasse le plafond de tours.** Ce que les sections lues disent : le plafond est un des seuils des conditions de départ (table des nœuds, nœud 4, gardé) ; aucun tour n'est ajouté (section 15) ; relever le plafond de tours reporte le scellement d'un devis (nœud 4, option (c), écartée). Donc un nombre de tours visé au-dessus du plafond se traite à la fin de l'étalonnage, par l'ordre écrit de la section 10.3, **que le mandat ne m'a pas fait lire** : le contre-lecteur doit vérifier que 10.3 dit bien ce qui se passe alors. Côté dépense : si les tours coûtent plus que mesuré à l'étalonnage, la réserve de 5 dollars les absorbe ; au-delà, la minuterie coupe à 55 dollars, la machine s'arrête par son identifiant, rien n'est relancé sans le mot de Lazar et un devis neuf, et ce qui est écrit par tour est versé avant toute destruction.

## 7. Réserves, et points pour Lazar

1. Aucune durée réelle pour les tours, la distillation, l'évaluation, les épisodes régénérés et les deux oracles neufs : les totaux de l'étape 2 sont des extrapolations des deux seules durées mesurées (épisode, action d'oracle).
2. La dépense de la première course est recalculée, non lue sur le compte du loueur.
3. Quatre choix du rédacteur à trancher : plafond 60 et coupure 55 ; coupure propre de l'étape 1 (12, plafond 17) ; plafond du fichier d'entrées à 50 plutôt qu'à 55 ; dépense passée à 0 sous la ligne neuve.
4. Le code de la minuterie de la première course ne porte qu'une coupure : la coupure propre de l'étape 1 demande une ligne de code ou une règle de la surveillance, à écrire dans l'ordre neuf.
5. Recommandation : 60 et 55, fichier d'entrées à 50 ; confiance moyenne (le pire cas à 24 tours tient à 53,4 dollars, avec 1,6 dollar sous la coupure).
