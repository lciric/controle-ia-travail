# Devis — second cycle de la lecture « accumuler les scores de sondes sur l'épisode » : création de la famille neuve tenue à l'écart (adaptateurs, épisodes, relecture à texte égal, notation) — v1 — brouillon 3

- **Auteur** : rédacteur neuf du second cycle, sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, Claude Fable 5.2 (`claude-fable-5-2`). **Date (UTC)** : brouillon 1 le 2026-11-18 après 18:20 ; brouillon 2 le 2026-11-18 après 19:05 ; brouillon 3 le 2026-11-18 après 21:13.
- **Statut** : **brouillon 3** = brouillon 2 (`devis-cycle-2-v1-brouillon2.md`, `065057f04fa67a55a5f370d782baf8ed738e2b4849bd69427805548608913088`, gardé tel quel, R12) + les choix de Lazar du 18 novembre sur les points à trancher (`GO-2026-11-18-56`, point 2 ; lignes de registre lues par leur numéro), portés par script (`pieces-redaction-cycle-2-v1/brouillons4-faire-v1.py`), et la citation que demandait la remarque D-1 de la vérification des brouillons 2 ; **aucun chiffre n'est recalculé** ; table en section 12 ; pas encore contre-lu dans cet état. Le brouillon 2 était lui-même : brouillon 1 (`devis-cycle-2-v1-brouillon1.md`, `ec6948d7321a65ce5bcb619f9a998160d9a562067adb0d493b7a69a7945329e1`, gardé tel quel, R12) + les corrections de sa contre-lecture (`contre-lecture-devis-et-decision-cycle-2-v1.md`, `75c9f7da73a9497fb2a87c592e70a91e75fb2e8166f7255a62e5cdf6dc12c32b`, Claude Sonnet 5.5 : « demandable après corrections », C1 à C10) ; table de traitement en section 11. Devis avant toute machine ; **aucune dépense engagée, aucune ligne de GO demandée par ce texte** ; scellé comme brouillon. Texte servi : `prereg/accumulation-cycle-2-v1-brouillon4.md`.
- **Arithmétique** : `pieces-redaction-cycle-2-v1/calculs-redaction-cycle-2-v2.py`, sortie `pieces-redaction-cycle-2-v1/sortie-calculs-redaction-cycle-2-v2.txt` (§ 4 à § 8), même dossier, empreintes dans leurs compagnons ; la version 1 reste. Aucune donnée lue. Le contre-lecteur a refait l'arithmétique du brouillon 1 par un script indépendant : identique.

## 1. En trois lignes

1. **Coût attendu de la famille neuve** : **62 à 84 USD** pour le plan de la note (400 tâches, un témoin) ; **64 à 88 USD** avec le second témoin honnête ; **77 à 106 USD** à 500 tâches ; **90 à 124 USD** à 600 (plafond d'effectif).
2. **Machine et durée** : carte A100 SXM4 80 Go louée ; **51 à 61 heures de marche** à 400 tâches (2,1 à 2,5 jours sur une instance ; un peu plus d'un jour avec deux instances de génération) ; la génération des épisodes d'évaluation prend sept à huit dixièmes du temps, la pièce de génération entière plus des quatre cinquièmes.
3. **Pire cas** (hôte deux fois plus lent, 1,40 USD de l'heure) : **176 à 185 USD** à 400 tâches, **223 USD** à 500, **261 USD** à 600. **Plafond : 275 USD** (choix de Lazar, points à trancher, point 5, option (a) ; section 5). Validité de la famille, épreuve plantée, lecture et verdict : **processeur, 0 USD**.

## 2. Ce qui est chiffré

La famille que décrit le préenregistrement (« Métrique », « Plan d'analyse », points 3 et 4), en deux pièces de carte :

- **pièce de génération** : données de distillation (320 épisodes : cinq par tâche de distillation, 32 tâches, pour le saboteur et pour l'honnête) ; deux adaptateurs (saboteur, témoin), trois avec le second témoin honnête (retenu : points à trancher, point 11 ; ce sont les colonnes « second témoin » qui valent) ; contrôles d'identité ; recherche des facteurs de remise à l'intensité ; épisodes d'évaluation : **neuf conditions** (saboteur à quatre doses, témoin à quatre doses, honnête nu) × N tâches × un épisode de dix actions ;
- **pièce de relecture** : cellules à texte égal (quatre par dose : seize × N passes), textes honnêtes relus sous les deux états (huit × N) et sous le modèle nu (N), soit **25 × N passes** ; avec le second témoin, huit × N de plus (**33 × N**) ; garde d'équivalence ; tirage de 800 directions par couche lue ; notation en ligne des sondes gelées, des trois sondes du premier cycle et des directions ; poussée des scores fermés. **Les activations ne sont pas gardées.**

## 3. Sources des nombres (aucun chiffre de l'état de l'art ; aucun résultat)

| grandeur | valeur | source au dépôt |
|---|---|---|
| génération d'un épisode de dix actions, en lots de 8 | **40,2 s** (bas) ; **42,8 s** (haut et pire cas) | texte scellé de l'étude des organismes, `prereg/T0.6-organismes-v0-v1.md` (`ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169`), « Devis » : 40,2 s au run réel du premier test (« Sources des chiffres ») ; 42,8 s aux heures réelles de la course exploratoire (6,85 h pour 576 épisodes, « Devis de la confirmation ») |
| passe de relecture d'un épisode | **0,45 s** | même section (108,4 s pour 240 épisodes) |
| relecture à état imposé, tout compris | **2,3 à 3,7 fois le temps de passe** | devis de l'étape B bis, `brouillons/T0.7-etape-B-bis-v1/devis-etape-b-bis-v3.md` (`9431d3001d0d5c3980271ccd5ebad72d6889409cddcc29a098fcc8993a898cf1`) : 1 216 passes, 0,15 h de passe, poste chiffré 0,35 à 0,55 h, écriture des activations comprise. **Les deux sources se contredisent, et aucune n'est une mesure** : le texte scellé de la validité de l'adaptateur chiffre la même opération, sans écriture, à environ 1,1 fois (2 816 passes : 0,35 h de passe et 0,05 h de garde). Le facteur retenu est celui qui rend la fourchette la plus large ; au facteur de la validité, la relecture à 400 tâches vaudrait 1,5 h au lieu de 3,1 à 4,9 h |
| distillation d'un adaptateur (160 transcriptions, trois époques) | **0,23 à 0,46 h** | texte scellé de la validité de l'adaptateur, `prereg/validite-adaptateur-v1.md` (`7e78909d7ca88e0834d277bcf2cad78112f28b23a75d2a07c0503c765062363d`), « Calcul et dépense » ; étude des organismes, « Devis » (0,46 à 0,92 h pour deux) ; recoupé : distillation et ses données, 4,36 h à la course exploratoire, pour 4,0 à 4,7 h ici |
| recherche des facteurs de remise à l'intensité | 768 passes par témoin (quatre doses × douze pas × 16 tâches) | validité de l'adaptateur, « Calcul et dépense », pièce de relecture |
| notation par lots des sondes et des directions | 0,1 à 0,5 h pour 3,2 fois les jetons de la course de confirmation et 3 200 directions | même texte, même table ; jetons : 223 par action (étude des organismes, « Devis »), soit 2 230 par passe ; mis à l'échelle des jetons et de 2 400 directions (800 par couche, trois couches au plus) |
| mise en place ; essais ciblés sur l'instance ; identité et poussées | 1,0 h ; 0,6 h (génération) et 0,3 h (relecture) ; 0,3 à 0,4 h | validité de l'adaptateur, même table |
| prix de la carte | **1,0889 à 1,30 USD de l'heure** ; pire cas 1,40 | étude des organismes, « Devis » ; relevés plus récents 1,0867, 1,093 et 1,12 (devis de l'étape B bis) |
| disque ; téléchargement | ≤ 0,08 USD de l'heure ; ≤ 0,05 USD par Go, 20 à 40 Go par instance | devis de l'étape B bis, « Sources des nombres » |
| effectif N | 400 à 600 tâches | préenregistrement, « Puissance » (règle du marqueur `<<N_TACHES>>` : le plus petit de 400, 450, 500, 550, 600 qui donne la puissance voulue) |

**Non mesuré, déclaré** : le débit de la notation en ligne pendant la relecture (pris au débit de la notation par lots) ; le facteur de relecture (ci-dessus) ; la longueur des épisodes de la famille (prise à celle du mode « coût », qui est désormais le mode de la famille : choix de Lazar, points à trancher, point 2, option (a) ; elle n'est pas mesurée sur des tâches fraîches).

## 4. Postes (heures de carte A100 ; bas au débit du premier test, haut au débit de la course exploratoire)

| poste | 400 tâches, un témoin | 400 tâches, second témoin | 500 tâches, second témoin | 600 tâches, second témoin |
|---|---|---|---|---|
| données de distillation (320 épisodes) | 3,57 à 3,80 | 3,57 à 3,80 | 3,57 à 3,80 | 3,57 à 3,80 |
| distillation (deux ou trois adaptateurs) | 0,46 à 0,92 | 0,69 à 1,38 | 0,69 à 1,38 | 0,69 à 1,38 |
| épisodes d'évaluation (9 × N) | 3 600 épisodes : **40,20 à 42,80** | 40,20 à 42,80 | 4 500 : **50,25 à 53,50** | 5 400 : **60,30 à 64,20** |
| mise en place, essais, identité, poussées | 2,0 | 2,0 | 2,0 | 2,0 |
| **pièce de génération** | **46,2 à 49,5** | **46,5 à 50,0** | **56,5 à 60,7** | **66,6 à 71,4** |
| relecture (passes ; heures) | 10 768 ; 3,14 à 4,94 | 14 736 ; 4,30 à 6,75 | 18 036 ; 5,26 à 8,27 | 21 336 ; 6,22 à 9,78 |
| notation en ligne | 0,41 à 2,04 | 0,54 à 2,69 | 0,67 à 3,37 | 0,81 à 4,04 |
| mise en place, essais, poussées | 1,6 | 1,6 | 1,6 | 1,6 |
| **pièce de relecture** | **5,1 à 8,6** | **6,4 à 11,0** | **7,5 à 13,2** | **8,6 à 15,4** |
| **total de marche** | **51,4 à 58,1** | **52,9 à 61,0** | **64,0 à 73,9** | **75,2 à 86,8** |
| en jours, sur une instance | 2,1 à 2,4 | 2,2 à 2,5 | 2,7 à 3,1 | 3,1 à 3,6 |

## 5. Montants (USD)

| | 400 tâches, un témoin | 400 tâches, second témoin | 500 tâches, second témoin | 600 tâches, second témoin |
|---|---|---|---|---|
| **attendu** (bas : 40,2 s et 1,0889 ; haut : 42,8 s et 1,30 ; disque ; deux instances, 20 à 40 Go chacune) | **62 à 84** | **64 à 88** | **77 à 106** | **90 à 124** |
| **pire cas P1** : 42,8 s, hôte deux fois plus lent, 1,40 USD de l'heure | 176 | 185 | 223 | 261 |
| dont pièce de génération ; pièce de relecture (coupures) | 149 ; 28 | 150 ; 35 | 182 ; 41 | 213 ; 48 |
| P1, avec la réserve de 0,5 USD et une seconde instance de génération | 183 | 192 | 230 | 268 |
| **pire cas P2** : P1 plus une relance entière de la génération | hors du plafond (plus de 300 ; 325 à 474 selon l'effectif : sortie de calcul version 3, § 9) | idem | idem | idem |

- **Plafond : 275 USD** (choix de Lazar, points à trancher, point 5, option (a) ; `GO-2026-11-18-56`) : il couvre le pire cas P1 jusqu'à 600 tâches, réserve et seconde instance comprises (268). La branche (b) — 250 USD, effectif borné à 500 tâches — n'est pas retenue. Le plafond de 250 USD du brouillon 1 ne couvrait P1 à 600 tâches qu'au débit le plus favorable : retiré.
- **Coupures par pièce** : celles de la colonne de l'effectif retenu ; **réserve de 0,5 USD** sous le plafond ; chaque pièce s'arrête dès que le cumul relevé plus un quart d'heure de carte atteint sa coupure ; **le disque d'une instance arrêtée et gardée compte dans la coupure de sa pièce** ; arrêt et destruction par identifiant (R10) ; résultats partiels scellés comme tels.
- **Le pire cas P2 ne tient pas sous le plafond.** Deux gardes l'évitent, exigées du code : (a) la génération **pousse ses lots au fil de la marche** (identifiants générés, textes, mesures), si bien qu'une relance reprend au dernier lot poussé au lieu de tout rejouer ; (b) **garde de débit** : après les 80 premiers épisodes, si la durée projetée de la pièce dépasse deux fois l'attendu haut, la marche s'arrête avant de dépenser plus, instance gardée douze heures au plus, nœud de Lazar. Toute relance au-delà du plafond est un nœud.
- **Deux instances de génération en parallèle** (une moitié des tâches chacune, après la distillation faite une seule fois et les adaptateurs vérifiés par empreinte) : **environ 3 à 4 USD attendus** de plus (1,6 h de carte, disque, 20 à 40 Go de téléchargement), **environ 7 USD au pire cas** ; la marche passe d'un peu plus de deux jours à un peu plus d'un jour.
- **Variante moins chère, non recommandée** : ne pas jouer les épisodes du témoin (cinq conditions au lieu de neuf ; la seconde série de textes devient celle de l'honnête nu) : 32,5 à 37,0 h, **40 à 55 USD** attendus, 114 USD au pire cas P1 ; elle perd le contraste sur épisodes naturels et le contrôle « le témoin ne sabote pas » : c'est un écart au plan de la note, donc un nœud.

## 6. Hors de la famille neuve : la relecture complémentaire du temps 1 (ligne de GO à part)

**Pourquoi** : il n'existe pas de copie entière des activations du premier cycle. La course de confirmation n'en a poussé qu'un sous-ensemble tiré par graine — un dixième des actions, couche 15 seule, environ 1 Go (étude des organismes, plan, point 5) — ; l'étape B bis détruit les siennes avec son instance et chiffre leur rejeu à environ une demi-heure de carte (son texte scellé, « Données gardées »). Ce sous-ensemble ne suffit pas pour apprendre des sondes sur trois couches. **À vérifier par la session mère** : qu'aucune instance gardée ne porte encore ces activations (registres non lus).

**Passes** (2 752) : les 1 216 de l'étape B bis (épisodes dans leur état d'origine 576 ; textes du saboteur sous le modèle nu 256 ; texte de l'instruit sous le modèle nu 64 ; textes honnêtes sous l'adaptateur saboteur 256 ; textes honnêtes sous l'adaptateur témoin 64) ; **512** de plus pour les cellules croisées à texte égal (quatre doses × 64 tâches × deux cellules : texte du saboteur sous l'état témoin, texte du témoin sous l'état saboteur) ; **1 024** de plus pour les séries du témoin distillé honnête (quatre doses × 64 tâches × quatre séries). **Ces 1 024 passes n'existent que si la pièce du témoin distillé de la validité de l'adaptateur a été créée** — elle ne l'est que si l'issue de la reprise du premier test est « vu » (validité, plan, points 2 et 3) ; sans elle : 1 728 passes.

**Durée et coût** : 0,34 h de passe ; marche de **3,6 à 9,3 h**, dont une à six heures d'apprentissage exploratoire sur la carte (**supposé, sans source** : l'étape B bis supposait 2 à 4 s par apprentissage, non mesuré à son devis ; le haut de la fourchette en dépend) ; **attendu 5 à 15 USD, hors garde de l'instance arrêtée** ; pire cas P1 **≈ 30 USD** ; avec une relance entière **≈ 59 USD** ; instance arrêtée et gardée entre deux séances : 1,92 USD par jour (9,6 USD sur cinq jours, 13,4 sur sept).

**Disque — deux calculs, qui ne s'accordent pas** : (1) au prorata des 49 Go que l'étape B bis écrit pour 1 216 passes : **≈ 111 Go** ; (2) d'après l'étude des organismes (environ 10,5 Go par couche pour 576 épisodes, soit 18,3 Mo par passe et par couche) : **≈ 50 Go par couche, ≈ 151 Go pour trois couches**. Le rapport des deux (0,74) n'est expliqué par aucun texte lu. Le second calcul atteint la borne d'offre de 150 Go, sans place pour le modèle (environ 16 Go), l'image et le dépôt.

**Plafond et disque : choix de Lazar** (points à trancher, point 4 ; `GO-2026-11-18-56`) — la relecture est accordée ; sa dépense reste sous une ligne à part :
- **plafond (β) 75 USD** : une relance entière et sept jours de garde tiennent (58,8 + 13,4, soit environ 72 USD) ; la branche (α) — 40 USD, aucune relance entière, cinq jours de garde au plus — n'est pas retenue ;
- **disque (i) au moins 250 Go, si une offre tient le prix du stockage** (0,08 USD de l'heure au plus, section 9 ; les offres à gros disque ont un stockage plus cher) — **fait à venir** : la session mère le vérifie sur les offres au lancement et l'écrit ; **sinon disque (ii), relecture et apprentissage couche par couche** (environ 50 Go à la fois, borne d'offre inchangée) : deux relectures de plus, soit environ 2 à 3 USD et 1,6 à 2,5 h de carte de plus (sortie de calcul version 3, `pieces-redaction-cycle-2-v1/sortie-calculs-redaction-cycle-2-v3.txt`, § 9 : 1,7 à 3,3 USD), et l'analyste ne compare les couches qu'après coup.

Sans cette ligne, le temps 1 ne peut pas concevoir de sonde neuve (ordre exploratoire, section 4).

## 7. Ce qui se fait sans carte : les tâches fraîches, et le reste

**Tâches fraîches — 0 USD de carte ; ni heures ni dollars d'appels de modèle chiffrables avec les sources que le rédacteur et le contre-lecteur avaient le droit de lire ; volume chiffré.**

- **Ce qu'il faut** : la liste est scellée avant que l'effectif soit connu (préenregistrement, plan, point 3) : il faut donc tirer et extraire **pour le plafond d'effectif** — **632 papiers gardés après extraction** (600 tâches d'évaluation, 32 de distillation) —, quel que soit l'effectif final. Avec une réserve de remplacement de 20 % (**hypothèse du rédacteur, sans source** ; la seule estimation écrite est « environ 10 à 15 % » d'échec par papier, procédure d'extraction, § 6, « estimation, non mesure »), la sélection doit **garder** environ **760 papiers** (640 pour 500 tâches, 520 pour 400). Le nombre de papiers **examinés** est plus grand : la règle de sélection s'arrête quand le nombre voulu est gardé après ses filtres (règle de sélection, § 8), et la réserve ne couvre que les exclusions de l'extraction.
- **Faisabilité** : la requête d'essai de la règle comptait 3 405 entrées ; 96 papiers ont été gardés au premier tirage ; il reste au plus 3 309 entrées avant filtres, **moins celles déjà examinées et exclues**. Garder 760 papiers demande que la sélection garde au moins **23 %** de ces entrées (19 % pour 640, 16 % pour 520). Le rendement du premier tirage est un compteur que ni le rédacteur ni le contre-lecteur n'ont lu.
- **Volume** : un sous-agent neuf par papier et par tentative, une seconde tentative pour les papiers invalides, une contre-vérification (procédure d'extraction, § 3, § 6, § 7). Pour une part de papiers invalides à la première tentative entre 10 % et 30 % (**hypothèse sans source**) : **590 à 690 lancements** pour 520 papiers, **720 à 850** pour 640, **850 à 1 000** pour 760, hors reprises. Le texte converti d'un papier du premier tirage compte en moyenne 90 229 caractères (essai à blanc de la procédure d'extraction, lu par le contre-lecteur) : la première tentative seule lit environ **47, 58 ou 68 millions de caractères**.
- **Textes à écrire avant le tirage, dès maintenant** (points à trancher, point 13, retenu) : la règle du tirage complémentaire (même règle de sélection, identifiants déjà employés exclus), texte neuf scellé et contre-lu, car l'entropie du tirage dérive de son empreinte ; la procédure d'extraction portée à cette échelle (son échantillon de contre-vérification est de 16 papiers sur 96 : à 500 ou 760 papiers, taille et seuil d'arrêt sont à récrire), contre-lue et scellée.
- **Ce qui manque pour chiffrer en heures et en dollars** : (1) les **compteurs du premier tirage** — entrées examinées, motifs d'exclusion de la sélection, papiers invalides à la première tentative, exclusions pour papier purement théorique, échecs de l'échantillon de contre-vérification, reprises — : des compteurs seuls, sous `diag/` ; (2) la **durée réelle d'une vague de sous-agents** et leur nombre en parallèle (passations, registre des dépenses) ; (3) **ce que valent les appels de modèle de la session** : aucun texte lu ne porte de prix ni de ligne de dépense pour l'extraction, alors que la décision N-049 traite la construction d'une banque sœur par appels de modèles comme une dépense. **Choix de Lazar** (points à trancher, point 8, option (a)) : **dépense à devis**. La session mère relève d'abord les compteurs du premier tirage (des nombres seuls) et la durée d'une vague ; un devis de l'extraction suit, puis sa ligne de dépense ; le tirage attend cette ligne. **Ce devis reste à écrire** : les trois manques ci-dessus ne sont pas levés par ce brouillon.

**Le reste, sur processeur** : conception de la recette de la famille par une instance aveugle aux sondes ; temps 1 hors relecture complémentaire ; épreuve plantée du développement et de la famille ; validité de la famille ; lecture (rééchantillonnage de 10 000 tirages sur 800 directions par couche : de l'ordre d'heures de processeur, à mesurer à blanc sur des données jouets avant la lecture) ; verdict ; contre-lectures ; écriture et épreuves du code.

## 8. Hors devis (chacun un nœud ou une ligne à part)

- le **bras d'attaque informé** chargé de fabriquer un faux positif (**lancé** : choix de Lazar, points à trancher, point 7 (ii) ; petite dépense, **non chiffrée ici** : son devis et sa ligne restent à écrire) ;
- le rejeu de l'épreuve plantée sur un **second modèle de base** (**reporté** à un cycle suivant ou à la porte de fin de phase 1 : points à trancher, point 7 (iii) ; aucune dépense dans ce cycle) ;
- le **dépôt daté chez un tiers** (**empreintes seules**, geste fait par Lazar : points à trancher, point 7 (i) ; pas de coût de carte) ;
- la **mesure du dommage** si le mode de la recette n'a pas de lecteur mécanique (étiquetage par sous-agents : devis à joindre à la recette) — sans objet attendu : le mode retenu, « coût déclaré gonflé », se lit par programme (points à trancher, point 2, option (a)) ; à confirmer par la recette ;
- une **seconde famille neuve** pour la **réplication avant revendication, retenue** (points à trancher, point 1, option (b)) : même devis que la famille de ce cycle (sections 4 et 5), **seulement après une issue positive**, sous sa propre ligne de dépense ; rien n'est engagé avant ;
- un éventuel bras « plafond appris sur la famille » (non retenu dans le préenregistrement) : il obligerait à garder les activations sur le disque de l'instance (de l'ordre de 180 Go par couche à 400 tâches).

## 9. Offre, étiquettes, durée

- **Offre** : A100 SXM4 80 Go, ≤ 1,30 USD de l'heure, ≥ 16 cœurs effectifs, ≥ 128 000 Mo de mémoire vive, disque ≥ 150 Go, stockage ≤ 0,08 USD de l'heure (bornes du devis de l'étape B bis) ; pour la relecture complémentaire, disque selon la branche retenue (section 6) ; étiquettes `acc2-generation-v1`, `acc2-relecture-v1` et `acc2-temps1-v1` (elles ne commencent ni par `t06` ni par `t07` : aucune garde d'inventaire d'une autre chaîne ne les compte) ; chaque instance détruite par son identifiant après la poussée vérifiée.
- **Durée de carte** : famille neuve, 2,1 à 2,5 jours à 400 tâches sur une instance, 3,1 à 3,6 jours à 600 ; 1,2 à 2,1 jours avec deux instances de génération ; relecture complémentaire, moins d'une demi-journée de marche.
- **Suite des étapes et ce qui commande le délai** : points à trancher, section C. Deux postes ne sont pas chiffrés en jours : l'extraction des tâches fraîches (section 7) et l'écriture du code, qui vient désormais avant le scellement.

## 10. Lignes de GO proposées (à inscrire par la session mère sur le mot de Lazar ; rien n'est demandé ici)

- **Famille neuve** : « calcul | second cycle de l'accumulation, création de la famille neuve tenue à l'écart : une à trois instances A100 SXM4 80 Go pour les données de distillation, trois adaptateurs, 9 × N épisodes d'évaluation, la relecture à texte égal et la notation fermée ; seulement après `SCELLEMENT-ACC2` ; lots poussés au fil de la marche ; garde de débit ; coupures par pièce, réserve de 0,5 USD ; sorties scellées avant lecture ; arrêt et destruction par identifiant | **275 USD** | échéance à fixer | Lazar | ce devis ».
- **Relecture complémentaire du temps 1** : « calcul | second cycle de l'accumulation, temps 1 : une instance A100 pour relire à état imposé les épisodes de développement et y apprendre des sondes contre le témoin ; seulement après `OUVERTURE-TEMPS1-ACC2` ; arrêt et destruction par identifiant | **75 USD** | échéance à fixer | Lazar | ce devis ».
- Ligne d'engagement au registre des dépenses avant la première minute de chaque pièce (attendu, pire cas, dépense antérieure sous la ligne).

## 11. Traitement des remarques de la contre-lecture

| remarque | traitement dans ce brouillon 2 |
|---|---|
| **C1** (bloquante) — plafond de la relecture complémentaire sous son propre pire cas | **appliqué** : les deux lectures sont écrites (40 USD sans relance entière et cinq jours de garde au plus ; 75 USD) ; le choix est laissé à Lazar ; « attendu hors garde » et supposition des six heures écrits (section 6) |
| **C2** (bloquante) — disque de la relecture complémentaire | **appliqué** : les deux calculs côte à côte, l'écart non expliqué, les deux branches (250 Go ou couche par couche), la vérification du prix du stockage ; le choix est laissé à Lazar (section 6). Ajout du rédacteur : le surcoût de la branche couche par couche (deux relectures de plus) |
| **C3** (bloquante) — tâches fraîches non chiffrées | **appliqué** : volume, faisabilité, ce qui manque, « gardés » et « examinés » distingués, tirage pour le plafond d'effectif (section 7). Le chiffrage en heures et en dollars reste impossible avec les sources permises : nœud |
| **C4** — seconde instance de génération | **appliqué** : 3 à 4 USD attendus, 7 USD au pire ; incompatibilité avec 250 USD à 600 tâches écrite (section 5) |
| **C5** — débit de génération | **appliqué** : 42,8 s pour l'attendu haut et pour le pire cas. **Écart déclaré au couple** : le contre-lecteur écrit « 65 à 84 » pour 400 tâches et un témoin, ce qui met aussi le bas à 42,8 s ; ce brouillon garde le bas au débit du premier test (62), comme sa phrase le demande ; ses pires cas (176 à 185, 223, 261) sont retrouvés |
| **C6** — facteur de relecture | **appliqué** : contradiction des deux sources écrite, aucune n'est une mesure (section 3) |
| **C7** — marge des coupures | **appliqué** : réserve de 0,5 USD (section 5) |
| **C8** — 512 et 1 024 passes non dérivées | **appliqué** : dérivation écrite, dépendance des 1 024 à la pièce du témoin distillé écrite (section 6) |
| **C9** — garde de l'instance arrêtée dans la coupure | **appliqué** (section 5) |
| **C10** — « plus des quatre cinquièmes » | **appliqué** : les deux parts sont écrites (section 1) |
| réponse sur la copie des activations | **reprise** (section 6), avec la vérification qui reste à la session mère |
| plafond de la famille (C5, et mineur 13 de la contre-lecture des textes) | **laissé ouvert, deux branches** : 275 USD, ou 250 USD avec l'effectif borné à 500 tâches |

## 12. Choix de Lazar portés dans ce brouillon 3

Source : registre des accords, ligne `GO-2026-11-18-56`, point 2 (mot direct « go autres recos ») ; registre des décisions, ligne R-3434 ; texte tranché : `points-a-trancher-cycle-2-v1-brouillon3.md`, `1999a6ded7bfdcdc0f29bc1c940873903dc2a15c5c5a8b9f7ca795f0a15890ac`. Détail, changement par changement : `differences-brouillons-3-vers-4-v1.md` (même dossier). **Aucun chiffre de ce devis n'est recalculé** : les choix retiennent des branches déjà chiffrées.

| choix | ce qu'il change dans ce devis |
|---|---|
| **point 1, option (b)** — réplication avant revendication | section 8 : une seconde famille, au même devis, seulement après une issue positive, sous sa propre ligne |
| **point 2, option (a)** — mode « coût déclaré gonflé », rejoué à neuf | section 3 (longueur des épisodes) ; section 8 (étiquetage du dommage sans objet attendu, à confirmer par la recette) |
| **point 4** — relecture complémentaire accordée, plafond 75 USD, disque selon l'offre | section 6 ; section 10. **Fait à venir** : l'offre de disque d'au moins 250 gigaoctets au prix du stockage |
| **point 5, option (a)** — plafond de la famille neuve 275 USD | sections 1, 5 et 10 |
| **point 7** — empreintes seules ; bras d'attaque lancé ; second modèle reporté | section 8. **À écrire** : le devis du bras d'attaque |
| **point 8, option (a)** — extraction des tâches fraîches, dépense à devis | section 7. **À écrire** : le devis de l'extraction, après le relevé des compteurs du premier tirage par la session mère |
| **points 11 et 13** — second témoin honnête retenu ; textes du tirage préparés dès maintenant | sections 2, 7 et 10 |
| remarque **D-1** de la vérification des brouillons 2 | sections 5 et 6 : les deux chiffres sont cités de la sortie de calcul version 3, § 9 |
| points 6, 9, 10, 12, 14 | aucun changement dans ce devis |
| **point 3 — ouvert** | aucun : l'énoncé du contraste à témoin apparié de la porte de fin de phase 1 (A ou C) reste à Lazar ; ses épisodes de témoin relèvent du devis des épisodes de la porte, non de celui-ci |
| tenue | version, date, statut, renvoi au préenregistrement (brouillon 4), cette section ; rien d'autre : le reste est égal au brouillon 2, à l'octet |
