# Devis — second cycle de la lecture « accumuler les scores de sondes sur l'épisode » : création de la famille neuve tenue à l'écart (adaptateurs, épisodes, relecture à texte égal, notation) — v1 — brouillon 1

- **Auteur** : rédacteur neuf du second cycle, sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, Claude Fable 5.2 (`claude-fable-5-2`). **Date (UTC)** : 2026-11-18, après 18:20.
- **Statut** : devis avant toute machine ; **aucune dépense engagée, aucune ligne de GO demandée par ce texte** ; brouillon 1, scellé comme brouillon, à contre-lire. Texte servi : `prereg/accumulation-cycle-2-v1-brouillon1.md`.
- **Arithmétique** : `pieces-redaction-cycle-2-v1/calculs-redaction-cycle-2-v1.py`, sortie `pieces-redaction-cycle-2-v1/sortie-calculs-redaction-cycle-2-v1.txt` (§ 4 à § 7), même dossier, empreintes dans leurs compagnons. Aucune donnée lue.

## 1. En trois lignes

1. **Coût attendu** : **62 à 80 USD** pour le plan de la note (400 tâches, un témoin) ; **64 à 85 USD** avec le second témoin honnête que le rédacteur recommande ; **77 à 101 USD** à 500 tâches, **90 à 118 USD** à 600 (plafond d'effectif).
2. **Machine et durée** : carte A100 SXM4 80 Go louée ; **51 à 58 heures de marche** à 400 tâches (2,1 à 2,4 jours sur une instance ; environ un jour avec deux instances de génération en parallèle) ; plus des quatre cinquièmes du temps sont la génération des épisodes.
3. **Pire cas** (hôte deux fois plus lent, 1,40 USD de l'heure) : **168 à 176 USD** à 400 tâches, **249 USD** à 600 ; **plafond proposé : 250 USD**, arrêt par coupure de pièce. Validité de la famille, épreuve plantée, lecture et verdict : **processeur, 0 USD**.

## 2. Ce qui est chiffré

La famille que décrit le préenregistrement (« Métrique », « Plan d'analyse », points 3 et 4), en deux pièces de carte :

- **pièce de génération** : données de distillation (320 épisodes : cinq par tâche de distillation, 32 tâches, pour le saboteur et pour l'honnête) ; deux adaptateurs (saboteur, témoin), trois avec le second témoin honnête ; contrôles d'identité ; recherche des facteurs de remise à l'intensité ; épisodes d'évaluation : **neuf conditions** (saboteur à quatre doses, témoin à quatre doses, honnête nu) × N tâches × un épisode de dix actions ;
- **pièce de relecture** : cellules à texte égal (quatre par dose : seize × N passes), textes honnêtes relus sous les deux états (huit × N) et sous le modèle nu (N), soit **25 × N passes** ; avec le second témoin, huit × N de plus (**33 × N**) ; garde d'équivalence ; tirage de 800 directions par couche lue ; notation en ligne des sondes gelées, des trois sondes du premier cycle et des directions ; poussée des scores fermés. **Les activations ne sont pas gardées.**

## 3. Sources des nombres (aucun chiffre de l'état de l'art ; aucun résultat)

| grandeur | valeur | source au dépôt |
|---|---|---|
| génération d'un épisode de dix actions, en lots de 8 | **40,2 s** | texte scellé de l'étude des organismes, `prereg/T0.6-organismes-v0-v1.md` (`ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169`), « Devis », « Sources des chiffres » (run réel du premier test, A100 SXM4 80 Go) ; recoupé : 42,8 s par épisode aux heures réelles de la course exploratoire (6,85 h pour 576 épisodes ; même section, « Devis de la confirmation ») |
| passe de relecture d'un épisode | **0,45 s** | même section (108,4 s pour 240 épisodes) |
| relecture à état imposé, tout compris | 2,3 à 3,7 fois le temps de passe | devis de l'étape B bis, `brouillons/T0.7-etape-B-bis-v1/devis-etape-b-bis-v3.md` (`9431d3001d0d5c3980271ccd5ebad72d6889409cddcc29a098fcc8993a898cf1`) : 1 216 passes, 0,15 h de passe, poste chiffré 0,35 à 0,55 h (écriture des activations comprise : majorant ici) |
| distillation d'un adaptateur (160 transcriptions, trois époques) | **0,23 à 0,46 h** | texte scellé de la validité de l'adaptateur, `prereg/validite-adaptateur-v1.md` (`7e78909d7ca88e0834d277bcf2cad78112f28b23a75d2a07c0503c765062363d`), « Calcul et dépense » ; étude des organismes, « Devis » (0,46 à 0,92 h pour deux) ; recoupé : distillation et ses données, 4,36 h à la course exploratoire, pour 4,0 à 4,5 h ici |
| recherche des facteurs de remise à l'intensité | 768 passes par témoin (quatre doses × douze pas × 16 tâches) | validité de l'adaptateur, « Calcul et dépense », pièce de relecture |
| notation par lots des sondes et des directions | 0,1 à 0,5 h pour 3,2 fois les jetons de la course de confirmation et 3 200 directions | même texte, même table ; jetons : 223 par action (étude des organismes, « Devis »), soit 2 230 par passe ; mis à l'échelle des jetons et de 2 400 directions (800 par couche, trois couches au plus) |
| mise en place ; essais ciblés sur l'instance ; identité et poussées | 1,0 h ; 0,6 h (génération) et 0,3 h (relecture) ; 0,3 à 0,4 h | validité de l'adaptateur, même table (pièces du témoin distillé et de la relecture) |
| prix de la carte | **1,0889 à 1,30 USD de l'heure** ; pire cas 1,40 | étude des organismes, « Devis » ; relevés plus récents 1,0867, 1,093 et 1,12 (devis de l'étape B bis) |
| disque ; téléchargement | ≤ 0,08 USD de l'heure ; ≤ 0,05 USD par Go, 20 à 40 Go par instance | devis de l'étape B bis, « Sources des nombres » |
| effectif N | 400 à 600 tâches | préenregistrement, « Puissance » (règle du marqueur `<<N_TACHES>>`) |

**Non mesuré, déclaré** : le débit de la notation en ligne pendant la relecture (pris au débit de la notation par lots) ; le surcoût de la relecture sans écriture d'activations (pris au rapport de l'étape B bis, qui les écrit) ; la longueur des épisodes d'un mode de sabotage que le rédacteur ne connaît pas (prise à celle du mode « coût »).

## 4. Postes (heures de carte A100 ; attendu bas et haut)

| poste | 400 tâches, un témoin | 400 tâches, second témoin | 500 tâches, second témoin | 600 tâches, second témoin |
|---|---|---|---|---|
| données de distillation (320 épisodes) | 3,57 | 3,57 | 3,57 | 3,57 |
| distillation (deux ou trois adaptateurs) | 0,46 à 0,92 | 0,69 à 1,38 | 0,69 à 1,38 | 0,69 à 1,38 |
| épisodes d'évaluation (9 × N) | 3 600 épisodes : **40,20** | 40,20 | 4 500 : **50,25** | 5 400 : **60,30** |
| mise en place, essais, identité, poussées | 2,0 | 2,0 | 2,0 | 2,0 |
| **pièce de génération** | **46,2 à 46,7** | **46,5 à 47,2** | **56,5 à 57,2** | **66,6 à 67,3** |
| relecture (passes ; heures) | 10 768 ; 3,14 à 4,94 | 14 736 ; 4,30 à 6,75 | 18 036 ; 5,26 à 8,27 | 21 336 ; 6,22 à 9,78 |
| notation en ligne | 0,41 à 2,04 | 0,54 à 2,69 | 0,67 à 3,37 | 0,81 à 4,04 |
| mise en place, essais, poussées | 1,6 | 1,6 | 1,6 | 1,6 |
| **pièce de relecture** | **5,1 à 8,6** | **6,4 à 11,0** | **7,5 à 13,2** | **8,6 à 15,4** |
| **total de marche** | **51,4 à 55,3** | **52,9 à 58,2** | **64,0 à 70,4** | **75,2 à 82,7** |

## 5. Montants (USD)

| | 400 tâches, un témoin | 400 tâches, second témoin | 500 tâches, second témoin | 600 tâches, second témoin |
|---|---|---|---|---|
| **attendu** (prix 1,0889 à 1,30 ; disque ; deux instances, 20 à 40 Go chacune) | **62 à 80** | **64 à 85** | **77 à 101** | **90 à 118** |
| **pire cas P1** : hôte deux fois plus lent, 1,40 USD de l'heure | 168 | 176 | 213 | 249 |
| dont pièce de génération ; pièce de relecture (coupures) | 140 ; 28 | 142 ; 35 | 171 ; 41 | 201 ; 48 |
| **pire cas P2** : P1 plus une relance entière de la génération | 308 | 318 | 384 | 450 |

- **Plafond proposé : 250 USD**, qui couvre le pire cas P1 jusqu'à 600 tâches ; **coupures par pièce** celles de la colonne de l'effectif retenu ; chaque pièce s'arrête dès que le cumul relevé plus un quart d'heure de carte atteint sa coupure ; arrêt et destruction par identifiant (R10) ; résultats partiels scellés comme tels.
- **Le pire cas P2 ne tient pas sous le plafond.** Deux gardes l'évitent, exigées du code : (a) la génération **pousse ses lots au fil de la marche** (identifiants générés, textes, mesures), si bien qu'une relance reprend au dernier lot poussé au lieu de tout rejouer ; (b) **garde de débit** : après les 80 premiers épisodes, si la durée projetée de la pièce dépasse deux fois l'attendu haut, la marche s'arrête avant de dépenser plus, instance gardée douze heures au plus, nœud de Lazar. Toute relance au-delà du plafond est un nœud.
- **Deux instances de génération en parallèle** (une moitié des tâches chacune, après la distillation faite une seule fois et les adaptateurs vérifiés par empreinte) : environ 1,6 h de mise en place et au plus 2 USD de téléchargement de plus ; la marche passe d'un peu plus de deux jours à un peu plus d'un jour. Recommandé si le calendrier de la porte de fin de phase 0 serre.
- **Variante moins chère, non recommandée** : ne pas jouer les épisodes du témoin (cinq conditions au lieu de neuf ; la seconde série de textes devient celle de l'honnête nu) : 32,5 à 35,3 h, **40 à 53 USD** attendus, 109 USD au pire cas P1 ; elle perd le contraste sur épisodes naturels et le contrôle « le témoin ne sabote pas » : c'est un écart au plan de la note, donc un nœud.

## 6. Hors de la famille neuve : la relecture complémentaire du temps 1 (ligne de GO à part)

Les activations des épisodes de développement ne sont pas gardées (texte scellé de l'étape B bis, « Données gardées » : détruites avec l'instance, rejeu chiffré à environ une demi-heure de carte). Pour apprendre une sonde contre le témoin, l'analyste du temps 1 a besoin d'une relecture à état imposé de ces épisodes : environ **2 750 passes** (les 1 216 de l'étape B bis, plus les cellules à texte égal « saboteur et témoin » et les séries du témoin distillé honnête si elles existent), soit 0,34 h de passe et de l'ordre de 110 Go d'activations sur trois couches (au prorata des 49 Go de l'étape B bis) ; marche de **3,6 à 9,3 h**, dont une à six heures d'apprentissage exploratoire sur la carte (**supposé, sans source** : l'étape B bis supposait 2 à 4 s par apprentissage, non mesuré à son devis) ; **attendu 5 à 15 USD** ; pire cas P1 **≈ 30 USD** ; avec une relance entière **≈ 59 USD** ; instance arrêtée et gardée entre deux séances : au plus 1,92 USD par jour (13,4 USD sur sept jours). **Plafond proposé : 40 USD**, une A100, une relance au plus. Sans cette ligne, le temps 1 ne peut pas concevoir de sonde neuve (ordre exploratoire, section 4).

## 7. Ce qui se fait au processeur (0 USD de carte)

- **Tâches fraîches** : tirage complémentaire de papiers (même règle de sélection, graine neuve) et extraction des énoncés par des sous-agents neufs, selon les procédures scellées de l'environnement de recherche (`docs/procedures/T0.5-selection-papiers-v1.md`, `8f43dcaeb5fd782c07fe4e0c9d093ed15d6bc09eb183a1fd9a3db589e5cac28b` ; `docs/procedures/T0.5-extraction-v1.md`, `d23bd62fe1611b8737ccb38a404d96a41746158a7930bef0a065590bd072c26c`). Il faut **432 papiers retenus** pour 400 tâches d'évaluation et 32 de distillation (532 à 500 tâches, 632 à 600) ; avec une réserve de remplacement de 20 % (**hypothèse du rédacteur, sans source** : le rendement de la première extraction n'a pas été lu), environ 520, 640 ou 760 papiers tirés, sur 3 309 entrées restantes avant filtres (3 405 à la requête d'essai de la règle, § 1 ; 96 déjà tirées). **Aucune dépense de carte ; au moins un sous-agent par papier et par tentative, plus les rondes de contre-vérification : c'est le poste qui commande le délai, et il n'est pas chiffré en heures faute de source lue.** Le tirage complémentaire est à proposer à Lazar (procédure d'extraction, § 2).
- **Conception de la recette de la famille** par une instance aveugle aux sondes ; **temps 1** hors relecture complémentaire ; **épreuve plantée** du développement et de la famille ; **validité de la famille** ; **lecture** (rééchantillonnage de 10 000 tirages sur 800 directions par couche : de l'ordre d'heures de processeur, à mesurer à blanc sur des données jouets avant la lecture) ; **verdict** ; contre-lectures ; écriture et épreuves du code.

## 8. Hors devis (chacun un nœud ou une ligne à part)

- le **bras d'attaque informé** chargé de fabriquer un faux positif (petite dépense, mot direct de Lazar, N-056) ;
- le rejeu de l'épreuve plantée sur un **second modèle de base** (changer de modèle : GO) ;
- le **dépôt daté chez un tiers** (compte ou dépôt externe : nœud ; pas de coût de carte) ;
- la **mesure du dommage** si le mode de la recette n'a pas de lecteur mécanique (étiquetage par sous-agents : devis à joindre à la recette) ;
- un éventuel bras « plafond appris sur la famille » (non retenu dans le préenregistrement) : il obligerait à garder les activations sur le disque de l'instance (de l'ordre de 180 Go par couche à 400 tâches).

## 9. Offre, étiquettes, durée

- **Offre** : A100 SXM4 80 Go, ≤ 1,30 USD de l'heure, ≥ 16 cœurs effectifs, ≥ 128 000 Mo de mémoire vive, disque ≥ 150 Go, stockage ≤ 0,08 USD de l'heure (bornes du devis de l'étape B bis) ; étiquettes `acc2-generation-v1` et `acc2-relecture-v1` (elles ne commencent ni par `t06` ni par `t07` : aucune garde d'inventaire d'une autre chaîne ne les compte) ; chaque instance détruite par son identifiant après la poussée vérifiée.
- **Durée de carte** : 2,1 à 2,4 jours à 400 tâches sur une instance (3,1 à 3,4 jours à 600) ; environ moitié moins avec deux instances de génération.
- **Délai du cycle** (ordre de grandeur de la note de conception : trois à quatre semaines) : contre-lectures et nœuds ; recette de la famille et tâches fraîches (en parallèle du temps 1, sept jours au plus) ; code (en parallèle) ; création de la famille (trois à quatre jours, création et poussées comprises) ; validité, épreuve, lecture, verdict (trois jours). **Le poste critique est l'extraction des tâches fraîches.**

## 10. Ligne de GO proposée (à inscrire par la session mère sur le mot de Lazar ; rien n'est demandé ici)

« calcul | second cycle de l'accumulation, création de la famille neuve tenue à l'écart : une à trois instances A100 SXM4 80 Go pour les données de distillation, deux ou trois adaptateurs, 9 × N épisodes d'évaluation, la relecture à texte égal et la notation fermée ; seulement après `SCELLEMENT-ACC2` et `CODE-ACC2` ; lots poussés au fil de la marche ; garde de débit ; coupures par pièce ; sorties scellées avant lecture ; arrêt et destruction par identifiant | **250 USD** | échéance à fixer | Lazar | ce devis ». Ligne d'engagement au registre des dépenses avant la première minute de chaque pièce (attendu, pire cas, dépense antérieure sous la ligne).
