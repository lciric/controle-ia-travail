"""Différentiel v4 -> v5 de la synthèse « comment détecter » (correcteur v5, session 16, 2026-10-20).

Chaque remplacement est exact : l'ancien texte doit se trouver une seule fois dans le texte courant, sinon arrêt.
Chaque entrée nomme les constats qu'elle applique (VV4-fidelite-NN, VV4-sens-NN) ou « v5 » (en-tête, section neuve).
Usage : python3 -I -B appliquer_corrections_v5.py ENTREE_V4 SORTIE_V5
"""
import hashlib
import sys

V4_ATTENDU = "fba703f90bba52663709857113d99e17ab0570e465180bed539458b18b11d00a"

R = []  # (constats, ancien, nouveau)

# ---------------------------------------------------------------- en-tête
R.append(("v5", "ce qu'ont fait Anthropic et les autres — synthèse v4", "ce qu'ont fait Anthropic et les autres — synthèse v5"))

R.append(("VV4-fidelite-10",
"""  « conforme après corrections »). Phrases et chiffres ajoutés : repris de ces deux rapports, qui les ont relus à la
  page et à la ligne ; aucun chiffre neuf. Deux faits datés du dépôt ajoutés : compte Vast.ai à recharge automatique
  (R-283) ;""",
"""  « conforme après corrections »). Phrases et chiffres de la littérature ajoutés : repris de ces deux rapports, qui les
  ont relus à la page et à la ligne. Jugements de la session, sans source dans les rapports : pouvoirs « faible à
  moyen » des rangs 2 et 6 ; confiance de 50 % sur la manipulation du nombre ; raisons des confiances (section 5). Deux
  faits datés du dépôt ajoutés : compte Vast.ai à recharge automatique (R-283) ;"""))

R.append(("VV4-fidelite-10",
"""Rien d'autre n'est changé. Le fond change en
  sections 1, 3, 4 et 5 : contrastes séparés par type (P3-P3 contre T1), prédiction de E2, pouvoirs des rangs 2, 3, 4,
  6 et 9, confiances, nœuds.""",
"""Rien d'autre n'est changé. Le fond change en
  sections 1 à 5 (2.1 : [BX], [PAR], [AU] ; 2.2 : « Pour P3 ») : contrastes séparés par type (P3-P3 contre T1),
  prédiction de E2, pouvoirs des rangs 2, 3, 4, 6 et 9, confiances, nœuds."""))

R.append(("v5",
"""  prédiction de E2, pouvoirs des rangs 2, 3, 4, 6 et 9, confiances, nœuds.
- **Sources.**""",
"""  prédiction de E2, pouvoirs des rangs 2, 3, 4, 6 et 9, confiances, nœuds.
- **v5 (correcteur, tour 4).** Correcteur neuf de la session 16 : je n'ai écrit ni la v1, ni la v2, ni la v3, ni la v4,
  ni les extractions, ni les vérifications, ni les traitements. 2026-10-20, à partir de 23:30 UTC environ. Part de la v4
  (`fba703f9…`) et applique les 28 constats des deux vérifications du tour 3 : fidélité, VV4-fidelite-01 à 12
  (`…/revue-detection/verification-v4-fidelite/verification-v4-fidelite-v1.md`, `982ed742…`, « conforme après
  corrections ») ; sens, VV4-sens-01 à 16 (`…/revue-detection/verification-v4-sens/verification-v4-sens-v1.md`,
  `84d549f7…`, « conforme après corrections »). En mots exacts des rapports ; quand les deux rapports corrigent la même
  phrase, leurs corrections sont fusionnées ; chaque écart aux mots exacts est déclaré dans
  `…/revue-detection/traitement-verification-v4-par-correcteur-v1.md`. Phrases et chiffres de la littérature ajoutés :
  repris des deux rapports et recontrôlés à la page (`…/revue-detection/correction-v5/sortie-controles-v5.txt`) ; aucun
  chiffre neuf de la littérature. Faits du dépôt ajoutés, relus à la source : document de P-015 (`6e74c6cb…`), brouillon
  de T0.6 (`e212fb35…`), [P] l. 238-253 et l. 272-278. Recommandation (3) et nœud E2 écrits en deux versions selon
  l'issue de P-015, non tranchée (**[Décision de Lazar en attente : P-015]**). Section neuve « Décisions prises depuis la
  v4 ». Différentiel : `…/revue-detection/correction-v5/appliquer_corrections_v5.py`. Le fond change en sections 1, 3, 4
  et 5 ; aucun pouvoir changé ; confiances inchangées, sauf celle du nœud E2, laissée à revoir.
- **Sources.**"""))

R.append(("VV4-fidelite-02 ; VV4-sens-15 ; v5",
"""  pas rédiger P3b.
""",
"""  pas rédiger P3b.
  v4 : `registres/decisions.md` relu vers 18:27 UTC (`cc1b108d…`, commit `43cd3ac`) pour P-015 (l. 392) et R-283
  (l. 477) ; dans cette version, les lignes citées ailleurs dans la synthèse sont décalées d'une (N-025 l. 447, R-262
  l. 454, N-028 l. 457, R-265 l. 458, R-269 l. 462, N-029 et R-276 l. 469-470) ; `registres/go.md` (`05e7fccd…`) :
  GO-2026-10-20-05 à -08 aux l. 33 à 36 ; les renvois de la synthèse restent ceux des versions épinglées (`38579d98…`,
  `94ebe409…`). Brouillon de T0.6 : `brouillons/T0.6-organismes-v0-v1-brouillon1.md` (`e212fb35…`, empreinte donnée
  par VV3-sens-06 ; recalculée pour la v5 : égale).
  v5 : section « Décisions prises depuis la v4 » lue dans `registres/decisions.md` (`e8b73c64…`, tête `9ecd952`) et
  `registres/go.md` (`1a392407…`) ; dans ces versions : N-025 l. 453, R-262 l. 460, N-028 l. 463, R-265 l. 464, R-269
  l. 468, N-029 et R-276 l. 475-476, R-283 l. 483, P-015 l. 392 ; GO-2026-10-20-05 à -12 aux l. 33 à 40. Document de
  P-015 : `docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md` (`6e74c6cb…`, compagnon égal).
"""))

R.append(("v5",
"""v4 : phrases et
  chiffres ajoutés repris des rapports du tour 2, à recontrôler à la page par la vérification du tour 3.
""",
"""v4 : phrases et
  chiffres ajoutés repris des rapports du tour 2, à recontrôler à la page par la vérification du tour 3. v5 : phrases
  et chiffres ajoutés repris des deux rapports du tour 3, recontrôlés à la page par le correcteur v5
  (`…/revue-detection/correction-v5/controles_v5.sh`, `pagev5.py`, sortie `sortie-controles-v5.txt`) : PDF de `[D]` lus
  après empreinte complète ; les PDF de `[N]` et de `[X]` manquent au bloc-notes restauré (archive sans PDF, R-304 ;
  vérifié sur disque, R11) : leurs pages sont lues sur les extraits texte (`…/revue-detection/txt-nouveaux/`,
  `…/revue-detection/extraction/txt-representations/`), sans empreinte du PDF.
"""))

# ---------------------------------------------------------------- section 1, point 1
R.append(("VV4-sens-08 ; VV4-sens-03 ; VV4-fidelite-08 ; VV4-sens-02 ; VV4-sens-09 ; VV4-fidelite-05 ; VV4-sens-16 ; VV4-fidelite-12 (b)",
"""   imposée) est appuyée hors domaine et à grande échelle, avec données larges et contraste [OA table 15 ; CA p. 7-8]. Sur
   les cas sur consigne, elle ne bat pas la moyenne [DYL p. 11 ; table 9 ; LB p. 8 ; PAR table 3, sonde Pairs : 0,849 et
   0,879 contre 0,964 au sous-rendement]. À consigne égale (sous-rendement), elle s'effondre avec les sondes apprises sur
   « Roleplaying », qui lisent la consigne [AP p. 9, p. 18 ; PAR table 3, sonde RP : 0,457 et 0,437] ; entre consignes, la
   même sonde sépare presque parfaitement [AP p. 18]. Son issue dépend donc des données d'apprentissage de la sonde. La
   détection gagne avec la **taille ou la capacité du modèle**. Par la taille, [CA] place la rupture entre 2 et 9
   milliards, dans la famille Qwen3.5 (p. 8 ; liste p. 18) ; par la capacité, la place de Llama-3.1-8B n'est pas mesurée
   (R8 : question) ; [DYL] range Llama-3.3-70B, souvent pris pour les organismes, sous Qwen 3.5 2B Reasoning (p. 5) : si
   Llama-3.1-8B est en dessous, il tomberait là où [CA] mesure des sondes faibles (transposition entre papiers, R8).
   **Plusieurs couches** n'ont qu'un appui, sur une autre tâche [CC p. 8] ; sur ce même modèle, le choix de la couche
   compte peu [BX p. 3]. Le dernier jeton seul, sans question, échoue sur les enjeux [MK p. 4] ; chez Apollo, une sonde
   « Roleplaying » apprise et lue sur les dernières positions est « comparable » en aire, avec un rappel à 1 % de faux
   positifs sur le témoin meilleur que la sonde Roleplaying apprise et lue sur toutes les positions (moyenne), mais en
   dessous de la sonde Instructed-Pairs [AP p. 23].""",
"""   imposée) est appuyée hors domaine et à grande échelle, avec données larges et contraste [OA table 15 ; CA p. 7-8]
   ([OA] : sans consigne, triche écrite dans le code, textes hors politique, moyenne de couches ; [CA] : négatifs mêlés,
   pas d'avant le sabotage et épisodes honnêtes). À consignes différentes, elle ne bat pas la moyenne [DYL table 9,
   « Varied Deception » ; LB p. 8] ; sur « Backdoors », sonde Pairs, elle bat le maximum (0,832 et 0,849 contre 0,768 ;
   moyenne 0,844) [PAR table 3]. À consigne égale, sonde Pairs : 0,849 et 0,879 contre 0,964 en moyenne au
   sous-rendement [PAR table 3] ; la sonde de question de [DYL], apprise sur des réponses à « did you lie », tient sur
   « Gender Secret » remis sur consigne (exactitude équilibrée 0,85) quand la moyenne d'Apollo tombe près du hasard,
   raisonnement explicite dans le contexte [DYL p. 11 ; p. 8]. À consigne égale (sous-rendement), elle s'effondre avec
   les sondes apprises sur « Roleplaying », qui lisent la consigne [AP p. 9, p. 18 ; PAR table 3, sonde RP : 0,457 et
   0,437] ; contre le témoin Alpaca (autres tâches, sans consigne ; sujet et forme différents), la même sonde a un
   rappel au-dessus de 99 % à 1 % de faux positifs sur les quatre jeux [AP p. 18 ; témoin, p. 5] : ce n'est pas P3-P3,
   et un changement de tâche élève à lui seul la sonde Pairs [PAR p. 9]. Son issue dépend donc des données
   d'apprentissage de la sonde. La détection gagne avec la taille dans une famille [CA p. 8] et avec un indice de
   capacité sur le mensonge sur consigne [DYL p. 10, p. 12] ; [LB table 6] n'est pas ordonnée par la taille. Par la
   taille, [CA] place la rupture entre 2 et 9 milliards, dans la famille Qwen3.5 (p. 8 ; liste p. 18) ; par la capacité,
   la place de Llama-3.1-8B n'est pas mesurée (R8 : question) ; [DYL] rapporte que Llama-3.3-70B, souvent pris pour les
   organismes, est classé par Artificial Analysis sous Qwen 3.5 2B Reasoning (« existing organisms are often trained on
   Llama 3.3 70B, which Appendix I shows has limited introspective capacity, and which Artificial Analysis [2026] rank
   as less capable than more recent models such as Qwen 3.5 2B Reasoning », p. 5) : si Llama-3.1-8B est en dessous, il
   tomberait là où [CA] mesure des sondes faibles (transposition entre papiers, R8) ; mais dans [DYL] table 9, des
   modèles d'indice 9 à 14 obtiennent 0,64 à 0,84 : un indice bas n'y prédit pas des sondes faibles. **Plusieurs
   couches** n'ont qu'un appui, sur une autre tâche [CC p. 8] ; sur le modèle de P3, le choix de la couche compte peu
   [BX p. 3]. Le dernier jeton seul, sans question, échoue sur les enjeux [MK p. 4] ; chez Apollo, une sonde
   « Roleplaying » apprise sur les dernières positions et lue au dernier jeton est « comparable » en aire, avec un rappel
   à 1 % de faux positifs sur le témoin meilleur que la sonde Roleplaying apprise et lue sur toutes les positions
   (moyenne), mais en dessous de la sonde Instructed-Pairs [AP p. 23]."""))

# ---------------------------------------------------------------- section 1, point 2
R.append(("VV4-fidelite-07 ; VV4-fidelite-12 (b), (c) ; VV4-sens-07 ; VV4-sens-02 ; VV4-fidelite-09 ; VV4-sens-16",
"""2. Deux types de contraste sont à séparer. **P3-P3** oppose deux consignes : le saboteur a une consigne privée, l'honnête
   n'en a pas ([P] l. 328-332). **T1** oppose, sous la même consigne, des actions qui gonflent et d'autres non ([P]
   l. 238-241). Analogues publiés de **P3-P3** (consignes différentes, consigne non notée) : sur « Backdoors », à 70
   milliards, sonde de recette « Pairs » (celle de la sonde de tromperie de P3, [P] l. 293-296), jetons publics seuls :
   moyenne 0,844, **maximum 0,768** [PAR table 3, p. 7 ; p. 3-4] (réserves : code fourni par la consigne, hors politique,
   p. 4 ; réponses honnêtes déjà plus hautes que presque tout Alpaca, p. 9) ; mensonges sur consigne, sonde en moyenne,
   consigne non notée : 0,95 ; 0,60 ; 0,69 ; 0,58 selon le modèle [LB p. 6-7 ; table 6, p. 54] ; « Varied Deception » :
   Qwen3-8B 0,74 en exactitude équilibrée [DYL p. 5 ; table 9, p. 28] ; sur ce même modèle, rappel à 1 % de faux positifs
   contre la conversation ordinaire, consigne et raisonnement exclus du score : 0,03 [BX p. 6 ; table 1]. Analogues de
   **T1** (consigne égale ; l'étiquette vient du choix du modèle) : 0,81 et 0,63 sur ce même modèle [BX p. 5-6 ; consigne
   unique, p. 4 ; étiquettes, p. 12], 0,606 [YS p. 3] ; l'empan public de [BX] porte sans doute une justification fausse
   (p. 12-13), et pour [YS] l'exclusion du raisonnement n'est pas dite : « rien d'écrit dans l'empan lu » n'est établi pour
   aucun des deux. Le 0,5 de [BX] vient d'un organisme affiné, sans consigne ni raisonnement, sondes réentraînées sur lui,
   organisme peut-être incomplet [BX p. 4, p. 8] ; P3 n'est pas affiné. [AU] : 0,653 sur Phi-4, sonde lue sur les 10
   derniers jetons, agrégation non dite (p. 7) ; la notation « +X » rend ambigu ce qui est lu : prise à la lettre,
   « Action » est l'action sans contexte, et le montage de P3 (rôle dans le contexte) serait « +System (AUC = 1.000) »
   (p. 6). **La littérature ne prévoit ni n'exclut le nul de P3** : à consignes différentes, de 0,58 à 0,95 selon le
   modèle, 0,768 au maximum à 70 milliards, rappel de 0,03 sur ce même modèle quand ni consigne ni raisonnement ne sont
   notés ; aucun de ces travaux ne mesure contre un plancher apparié. [BX], [YS] et [LB] agrègent par la moyenne, [PAR]
   donne moyenne et maximum, [AU] lit les derniers jetons ; P3, par le maximum ou l'attention. Une sonde qui lit le régime
   de consigne **séparerait** le saboteur de l'honnête [KU p. 9 ; AP p. 18] : ce fait prédit un faux positif sur P3-P3,
   pas un nul.""",
"""2. P3 n'avait aucune de ces conditions. Deux types de contraste sont à séparer. **P3-P3** oppose deux consignes : le
   saboteur a une consigne privée, l'honnête n'en a pas ([P] l. 328-332). **T1** oppose, sous la même consigne, des
   actions qui gonflent et d'autres non ([P] l. 238-241). Analogues publiés de **P3-P3** (consignes différentes, consigne
   non notée) : sur « Backdoors », à 70 milliards, sonde de recette « Pairs » (celle de la sonde de tromperie de P3, [P]
   l. 293-296), jetons publics seuls : moyenne 0,844, **maximum 0,768** [PAR table 3, p. 7 ; p. 3-4] (réserves : code
   fourni par la consigne, hors politique, p. 4 ; réponse honnête moyenne au-dessus de 99,9 % d'Alpaca, sonde Pairs,
   p. 9) ; mensonges sur consigne, sonde en moyenne, consigne non notée : 0,95 ; 0,60 ; 0,69 ; 0,58 selon le modèle
   [LB p. 6-7 ; table 6, p. 54] ; « Varied Deception » : Qwen3-8B 0,74 en exactitude équilibrée [DYL p. 5 ; table 9,
   p. 28] (couche et classifieur réglés sur une validation du même jeu, p. 8) ; mensonges verbaux de jeux de rôle, avec
   ou sans incitation, Llama-3-8B, dernier jeton, sonde de vérité générique : 93,8 % (TTPD) et 79 % (régression
   logistique) d'exactitude [BU p. 10]. Analogues de **T1** (consigne égale ; l'étiquette vient du choix du modèle) :
   0,81 et 0,63 sur le modèle de P3 [BX p. 5-6 ; consigne unique, p. 4 ; étiquettes, p. 12], 0,606 [YS p. 3] (sonde
   apprise sur « Roleplaying », p. 2) ; au sous-rendement, l'étiquette suit le sujet (WMDP contre MMLU, [BX p. 4] ;
   [PAR p. 4]), ce que T1 de P3 n'a pas ([P] l. 238-239) ; l'empan public de [BX] porte sans doute une justification
   fausse (p. 12-13), et pour [YS] l'exclusion du raisonnement n'est pas dite : « rien d'écrit dans l'empan lu » n'est
   établi pour aucun des deux. Le 0,5 de [BX] (type T1 : aucune consigne, p. 4) vient d'un organisme affiné, sans
   consigne ni raisonnement, sondes réentraînées sur lui, organisme peut-être incomplet [BX p. 4, p. 8] ; P3 n'est pas
   affiné. Contre la conversation ordinaire (troisième type, ni P3-P3 ni T1 : autres tâches, seuil sur la conversation
   ordinaire) : rappel de 0,03 sur le modèle de P3 (Llama-3.1-8B-Instruct), consigne et raisonnement exclus du score
   [BX p. 6 ; table 1] ; plus de 99 % pour la sonde de question apprise sur « Roleplaying » [AP p. 18]. [AU] (type non
   établi ; étiquette « very correlated with the 'Impostor' label », p. 6) : 0,653 sur Phi-4, sonde lue sur les 10
   derniers jetons, agrégation non dite (p. 7) ; la notation « +X » rend ambigu ce qui est lu : prise à la lettre,
   « Action » est l'action sans contexte, et le montage de P3 (rôle dans le contexte) serait « +System (AUC = 1.000) »
   (p. 6). **La littérature ne prévoit ni n'exclut le nul de P3** : à consignes différentes, de 0,58 à 0,95 selon le
   modèle, 0,768 au maximum à 70 milliards ; contre la conversation ordinaire, rappel de 0,03 sur le modèle de P3 quand
   ni consigne ni raisonnement ne sont notés ; aucun de ces travaux ne mesure contre un plancher apparié. [BX], [YS] et
   [LB] agrègent par la moyenne, [PAR] donne moyenne et maximum, [AU] lit les derniers jetons ; P3, par le maximum ou
   l'attention. Une sonde qui lit le régime de consigne **séparerait** le saboteur de l'honnête [KU p. 5, p. 9 ;
   hypothèse pour la sonde Instructed-Pairs, contre le témoin, AP p. 18] : ce fait prédit sur P3-P3 un « au-dessus » qui
   lirait la consigne, pas l'acte, et non un nul."""))

# ---------------------------------------------------------------- section 3
R.append(("v5",
"(VV2-sens-09) ; v4 : rangs 2, 3, 4, 6 et 9 revus (VV3-sens-01, 02, 10) ; dernière colonne :",
"(VV2-sens-09) ; v4 : rangs 2, 3, 4, 6 et 9 revus (VV3-sens-01, 02, 10) ; v5 : rangs 2 à 6 et 9 annotés, pouvoirs\ninchangés (constats VV4) ; dernière colonne :"))

R.append(("VV4-sens-16",
"elle séparerait le saboteur de l'honnête, ce qui prédit un faux positif sur P3-P3, pas un nul",
"elle séparerait le saboteur de l'honnête, ce qui prédit sur P3-P3 un « au-dessus » qui lirait la consigne, pas l'acte, et non un nul"))

R.append(("VV4-sens-07 ; VV4-sens-02 ; VV4-fidelite-09",
"type P3-P3 (consignes différentes, consigne non notée) : maximum 0,768 et moyenne 0,844 [PAR table 3, « Backdoors »] ; 0,58 à 0,95 [LB table 6] ; 0,74 [DYL table 9] ; rappel 0,03 [BX table 1] ; type T1 (consigne égale) : 0,81 et 0,63 [BX p. 5-6], 0,606 [YS p. 3], pour lesquels « rien d'écrit dans l'empan lu » n'est pas établi ([BX p. 12-13] ; [YS] : non dit) ; [AU] : 0,653, dix derniers jetons, agrégation non dite, « +System (AUC = 1.000) » selon la lecture de « +X » [AU p. 6-7] ; 0,5 seulement sur organisme affiné [BX p. 8] ;",
"type P3-P3 (consignes différentes, consigne non notée) : maximum 0,768 et moyenne 0,844 [PAR table 3, « Backdoors »] ; 0,58 à 0,95 [LB table 6] ; 0,74 [DYL table 9] (couche et classifieur réglés sur une validation du même jeu, [DYL p. 8]) ; mensonges verbaux de jeux de rôle, avec ou sans incitation, Llama-3-8B, dernier jeton, sonde de vérité générique : 93,8 % (TTPD) et 79 % (régression logistique) d'exactitude [BU p. 10] ; type T1 (consigne égale) : 0,81 et 0,63 [BX p. 5-6], 0,606 [YS p. 3] (sonde apprise sur « Roleplaying », [YS p. 2]), pour lesquels « rien d'écrit dans l'empan lu » n'est pas établi ([BX p. 12-13] ; [YS] : non dit) ; au sous-rendement, l'étiquette suit le sujet (WMDP contre MMLU, [BX p. 4] ; [PAR p. 4]), ce que T1 de P3 n'a pas ([P] l. 238-239) ; contre la conversation ordinaire (troisième type, ni P3-P3 ni T1) : rappel 0,03 [BX table 1] ; [AU] (type non établi) : 0,653, dix derniers jetons, agrégation non dite, « +System (AUC = 1.000) » selon la lecture de « +X » [AU p. 6-7] ; 0,5 (type T1) seulement sur organisme affiné [BX p. 8] ;"))

R.append(("VV4-sens-02",
"mais le rappel à 1 % peut tomber à 0,03 [BX table 1]",
"mais, contre la conversation ordinaire, le rappel à 1 % peut tomber à 0,03 [BX table 1]"))

R.append(("VV4-sens-08",
"une position après une question : 0,701 → 0,963 hors domaine [OA table 15] ;",
"une position après une question : 0,701 → 0,963 hors domaine [OA table 15] ([OA] : sans consigne, triche écrite dans le code, textes hors politique, moyenne de couches) ;"))

R.append(("VV4-fidelite-08 ; VV4-sens-02 ; VV4-sens-03",
"entre consignes, séparation presque parfaite (« Our recall at 1% is greater than 99% on all four evaluation datasets », [AP p. 18]) ; sur consigne, pas meilleure que la moyenne [DYL p. 11 ; table 9 ; LB p. 8] ;",
"contre le témoin Alpaca (autres tâches, sans consigne ; sujet et forme différents), la sonde de question apprise sur « Roleplaying » a un rappel au-dessus de 99 % à 1 % de faux positifs (« Our recall at 1% is greater than 99% on all four evaluation datasets », [AP p. 18 ; témoin, p. 5]) : ce n'est pas P3-P3, et un changement de tâche élève à lui seul la sonde Pairs [PAR p. 9] ; à consignes différentes, pas meilleure que la moyenne [DYL table 9 ; LB p. 8] ; à consigne égale, contre-cas avec raisonnement écrit [DYL p. 11] ;"))

R.append(("VV4-sens-16",
"chez Apollo, une sonde « Roleplaying » lue sur les dernières positions, « comparable » en aire",
"chez Apollo, une sonde « Roleplaying » apprise sur les dernières positions et lue au dernier jeton, « comparable » en aire"))

R.append(("VV4-sens-09",
"; mais Nemotron-3 Nano (30B-A3B) reste à 0,613–0,760 (p. 8 ; p. 25) ;",
"; Nemotron-3 Nano (30B-A3B, 3 milliards actifs) reste bas (p. 8 ; p. 25) ;"))

R.append(("VV4-fidelite-06",
"toutes, seule comparaison publiée (« using",
"toutes, seule comparaison lue (« using"))

R.append(("VV4-sens-16",
"entre consignes, une sonde de régime prédit un faux positif sur P3-P3 [KU p. 9]",
"entre consignes, une sonde de régime prédit sur P3-P3 un « au-dessus » qui lirait la consigne, pas l'acte [KU p. 9]"))

R.append(("VV4-sens-16",
"rang 2 faible à moyen (une sonde de régime prédit un faux positif, pas un nul) ;",
"rang 2 faible à moyen (une sonde de régime prédit un « au-dessus » qui lirait la consigne, pas un nul) ;"))

R.append(("v5",
"""données d'apprentissage de la sonde » ; rang 6 faible à moyen ; rang 9 annoté par type ; les autres pouvoirs sont
inchangés.
""",
"""données d'apprentissage de la sonde » ; rang 6 faible à moyen ; rang 9 annoté par type ; les autres pouvoirs sont
inchangés. v5 : aucun pouvoir changé ; rang 3 : troisième type (contre la conversation ordinaire), [BU] parmi les
analogues de P3-P3, réglage de [DYL], sujet confondu des analogues de T1, types du 0,5 et du 0,653 ; rang 4 : témoin
Alpaca, contre-cas de [DYL] p. 11 ; rang 5 : Nemotron-3 Nano ; rang 6 : « comparaison lue » ; rangs 2 et 9 : un
« au-dessus » qui lirait la consigne, au lieu d'un « faux positif ».
"""))

# ---------------------------------------------------------------- section 4, règles communes
R.append(("VV4-sens-11",
"""**Bras de production** (maximum ou attention) : P3-P4 (témoin), T1, T3 et T4 aux seuils gelés de [P] (l. 272-279) ;
Bonferroni sur les seuls bras de production.""",
"""**Bras de production** (maximum ou attention) : saboteur contre honnête, avec Bonferroni sur les bras de production et
les deux sondes (comme P3-P3, [P] l. 275-277 ; extension aux bras : règle de cette synthèse) ; P3-P4 (témoin), T1, T3 et
T4 à 95 %, sans correction ([P] l. 278)."""))

R.append(("VV4-fidelite-12 (a)",
"""lu « l'agrégation explique-t-elle le nul ? », (N-026,
conditions 1 à 4) ; hors de la famille de Bonferroni : règle de cette synthèse.""",
"""lu « l'agrégation explique-t-elle le nul ? » (N-026,
conditions 1 à 4) ; hors de la famille de Bonferroni : règle de cette synthèse (S-18)."""))

R.append(("VV4-sens-15",
"(R-262, `registres/decisions.md` l. 453)",
"(R-262, `registres/decisions.md` à `38579d98…`, l. 453)"))

R.append(("VV4-sens-12",
"écrire aussi la part d'actions du saboteur qui recouvre les coûts honnêtes : trop petite, T4 n'est pas calculable.",
"écrire aussi la part d'actions du saboteur qui recouvre les coûts honnêtes : trop petite, T4 repose sur peu de paires :\nfixer au préenregistrement un nombre minimal de paires par tranche, sinon « non calculable » (règle neuve, à déclarer)."))

# ---------------------------------------------------------------- section 4, table
R.append(("VV4-sens-12",
"**bras non aveugles** : seuls leurs planchers de même position, T4 au champ, et P3-P4 et T3 au champ et avant le champ sont neufs (T2 ne porte que sur saboteur contre honnête, [P] l. 242) ;",
"**bras non aveugles** : seuls saboteur contre honnête au champ et avant le champ sont déjà vus (T2, [P] l. 242) ; le reste est neuf : planchers de même position, P3-P4, T1, T3 et T4 aux deux positions ;"))

R.append(("VV4-fidelite-02 ; VV4-sens-15",
"(localisation au champ et oracle, `registres/go.md` l. 32)",
"(localisation au champ et oracle, `registres/go.md` à `94ebe409…`, l. 32, GO-2026-10-20-05)"))

R.append(("VV4-sens-06",
"(2) versions **incitées** (intérêt à gonfler, sans consigne), incitation présente chez les positifs **et** les négatifs (mêmes contextes, actes différents) : lecture **avant le champ** `COST`",
"(2) actions **générées par le modèle** sous incitation (intérêt à gonfler, sans consigne), incitation chez les positifs **et** les négatifs, étiquette par le coût écrit ensuite (comme T1) : lecture **avant le champ** `COST` ; jamais sur des paires écrites qui ne diffèrent qu'au champ (avant le champ, à texte égal, les activations sont égales : modèle causal)"))

R.append(("VV4-sens-01",
"sur T0.6, seulement sur la condition qui réplique P3 ((i-a), p = 1, intensité forte, brouillon de T0.6 l. 75, ou son équivalent dans T0.6 réécrit) ;",
"sur T0.6, seulement sur une condition qui réplique P3 ((i-a), p = 1, intensité forte, brouillon de T0.6 l. 75). Le T0.6 que recommande P-015 (défaut (b) le 22 octobre) n'en a pas : il ne garde que des doses sous le seuil du meilleur moniteur boîte noire (P-015, l. 36-39, l. 91-94), et P3 est flagrant (coût seul 0,8878, [V] l. 204). Sans condition de référence flagrante ajoutée à T0.6 (périmètre de P-015 et dépense : à toi), E2 sur T0.6 dit si la position aide sur l'organisme diffus, pas d'où vient le nul de P3 **[Décision de Lazar en attente : P-015]** ;"))

R.append(("VV4-sens-08",
"Pour : hors domaine et à grande échelle [OA table 15 ; CA p. 7-8] ;",
"Pour : hors domaine et à grande échelle [OA table 15 ; CA p. 7-8] ([OA] : sans consigne, triche écrite dans le code, textes hors politique, moyenne de couches ; [CA] : négatifs mêlés, pas d'avant le sabotage et épisodes honnêtes) ;"))

R.append(("VV4-fidelite-08 ; VV4-sens-02 ; VV4-sens-03",
"entre consignes, séparation presque parfaite [AP p. 18] ; tromperie sur consigne : la question ne bat pas la moyenne [DYL p. 11 ; table 9 ; LB p. 8] ;",
"contre le témoin Alpaca (autres tâches, sans consigne ; sujet et forme différents), la sonde de question apprise sur « Roleplaying » a un rappel au-dessus de 99 % à 1 % de faux positifs [AP p. 18 ; témoin, p. 5] : ce n'est pas P3-P3, et un changement de tâche élève à lui seul la sonde Pairs [PAR p. 9] ; à consignes différentes, pas meilleure que la moyenne [DYL table 9 ; LB p. 8] ; à consigne égale, contre-cas avec raisonnement écrit [DYL p. 11] ;"))

R.append(("VV4-sens-04 ; VV4-sens-10",
"**Prédiction écrite d'avance** : sonde apprise sur « Roleplaying » : échec de T1 ; sondes principales de P3 : issue incertaine ([PAR] : 0,849 et 0,879 à consigne égale, sujet WMDP contre MMLU confondu) ; le nombre de l'action est dans le contexte lu, donc T1 ne vaut qu'avec T4 ; un bras au-dessus du plancher sans T1 lit la consigne, pas l'acte |",
"**Prédiction écrite d'avance** : sonde apprise sur « Roleplaying » : échec de T1 ; lecture principale (saboteur contre honnête), bras (a) : la littérature ne tranche pas ; analogue de P3-P3 le plus proche (« Backdoors », sonde Pairs, 70 milliards, jetons publics) : question 0,832 et 0,849, contre maximum 0,768 et moyenne 0,844 [PAR table 3] ; un « au-dessus » sans P3-P4, T3 et T1 lirait la consigne. T1 : sondes principales de P3 : issue incertaine ([PAR] : 0,849 et 0,879 à consigne égale, sujet WMDP contre MMLU confondu) ; le nombre de l'action est dans le contexte lu, donc T1 ne vaut qu'avec T4 ; un bras au-dessus du plancher sans T1 lit la consigne, pas l'acte ; question générale sur 8 milliards : [CA p. 8] prédit une perte ; un nul du bras principal ne dira pas que la position n'aide pas ; la question précise, en diagnostic, le dira |"))

R.append(("VV4-sens-06 ; VV4-fidelite-02 ; VV4-fidelite-03 ; VV4-sens-13",
"**plus** la génération des épisodes d'évaluation neufs de T0.6, non devisée (à deviser : le brouillon actuel de T0.6 prévoit 1 536 + 640 épisodes ; la proposition P-015 en estime la réécriture en mode « coût » ; nœud de dépense possible au-delà de 10 USD par lancement)",
"**plus** la génération des actions du jeu (2), à deviser, **plus** la génération des épisodes d'évaluation neufs de T0.6, non devisée (à deviser : le brouillon actuel de T0.6 (`brouillons/T0.6-organismes-v0-v1-brouillon1.md`, `e212fb35…`) prévoit 1 536 + 640 épisodes ; la proposition P-015 (`registres/decisions.md` l. 392, version `cc1b108d…`) en propose le périmètre (options (a) à (c), recommandation (b), défaut le 2026-10-22 vers 14:30 UTC) ; son document (`docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md`, `6e74c6cb…`, l. 115-125) l'estime, non devisé, en (b) : ≈ 2 à 3 USD (étape 1), ≈ 7 à 9 USD (étape 2, organisme (i)), ≈ 15 USD en deux lancements (organisme (ii)) ; nœud de dépense possible au-delà de 10 USD par lancement)"))

R.append(("VV4-sens-15 ; VV4-fidelite-02",
"au-delà de 10 USD par lancement (R-269) : nœud ; compte à recharge automatique (R-283) |",
"au-delà de 10 USD par lancement (R-269) : nœud ; compte à recharge automatique (R-283, `registres/decisions.md` à `cc1b108d…`, l. 477) |"))

R.append(("VV4-sens-13",
"sur T0.6 : témoin et mention à jouer (le brouillon actuel de T0.6, l. 74-81, n'a pas de mention : T3 n'y serait pas calculable)",
"sur T0.6 : témoin et mention à jouer (le brouillon actuel de T0.6, l. 74-81, n'a pas de mention : T3 n'y serait pas calculable ; témoin et mention obligatoires dans P-015, l. 41-44)"))

# ---------------------------------------------------------------- section 5
R.append(("VV4-fidelite-04 ; VV4-sens-01",
"""≈ 1,5 à 2,5 USD non devisés ; avec la manipulation du nombre si tu l'ajoutes (nœud ci-dessous). (3) **E2 pas sur les
actions de P3** : je recommande de la jouer sur les épisodes neufs de T0.6, à l'aveugle, avec la prédiction écrite de la
section 4 (nœud ci-dessous). (4)""",
"""≈ 1,5 à 2,5 USD non devisés ; avec le bras « moyenne » (iii) et la manipulation du nombre si tu les ajoutes (nœud
ci-dessous). (3) **E2** **[Décision de Lazar en attente : P-015]**, en deux versions :
- *si T0.6 garde une condition de référence qui réplique P3* ((i-a), p = 1, intensité forte) : **E2 pas sur les actions
  de P3** : je recommande de la jouer sur les épisodes neufs de T0.6, à l'aveugle, avec la prédiction écrite de la
  section 4, si T0.6 garde une condition qui réplique P3 (nœud E2 et P-015) ;
- *si P-015 (b) est retenue sans condition de référence flagrante* (défaut de P-015, le 2026-10-22 vers 14:30 UTC) : E2
  sur T0.6 dit si la position aide sur l'organisme diffus, pas d'où vient le nul de P3 ; la question « la position
  explique-t-elle le nul de P3 ? » n'a de réponse que par l'option (a) du nœud E2 (actions de P3, extension de N-028),
  ou par une condition de référence flagrante ajoutée à T0.6 (périmètre de P-015 et dépense : à toi) ; le choix revient
  au nœud E2.

(4)"""))

R.append(("VV4-fidelite-10",
"**Confiance** (jugement du correcteur ; revue depuis la v1, VV2-sens-09 et VV3-sens-09).",
"**Confiance** (jugement du correcteur, puis de la session pour la v4 ; revue depuis la v1, VV2-sens-09 et VV3-sens-09)."))

R.append(("VV4-fidelite-11",
"""le bras « avant le champ » voit des nombres déjà écrits, et T1 n'y vaut
qu'avec T4.""",
"""le bras « avant le champ » voit des nombres déjà écrits, et, au champ, T1
ne vaut qu'avec T4."""))

R.append(("VV4-fidelite-01 ; VV4-sens-05",
"""T1 s'ajoute, à consigne égale, et rien de publié ne le passe sur un cas de ce type ; en sens contraire, le
montage corrigé""",
"""T1 s'ajoute, à consigne égale. Les analogues publiés de T1 restent au-dessus du hasard (0,81 et
0,63 sur ce même modèle, sonde générique [BX p. 5-6] ; 0,964 en moyenne, sonde Pairs, à 70 milliards [PAR table 3]), mais
avec un texte faux écrit dans l'empan et un sujet confondu (WMDP contre MMLU) ; sur ce même modèle, ils restent modestes
(0,81 et 0,63 ; 0,606 [YS p. 3]) ; aucun travail lu ne mesure T1 contre un plancher apparié (R8 : question) ; en sens
contraire, le montage corrigé"""))

R.append(("VV4-sens-16", "**Nœuds de Lazar.**", "**Nœuds de Lazar, proposition à défaut, rappel.**"))

R.append(("VV4-sens-15",
"(`registres/decisions.md` l. 456) et ne promet",
"(N-028, `registres/decisions.md` à `38579d98…`, l. 456) et ne promet"))

R.append(("VV4-sens-14",
"parmi les options tombées (l. 85) et recommandait",
"parmi les options tombées (l. 85) (raison : sans plancher par jeton, que P3b ajoute ; restent la recommandation de la\n  note, l. 8, et l'objection de la proposition C, l. 323-324) et recommandait"))

R.append(("VV4-sens-15",
"(`registres/decisions.md` l. 446). R-262 (2) demande une voie « choisie d'après la revue de la littérature » (l. 453).",
"(N-025, `registres/decisions.md` à `38579d98…`, l. 446). R-262 (2) demande une voie « choisie d'après la revue de la\n  littérature » (R-262, l. 453 à `38579d98…`)."))

R.append(("VV4-fidelite-04 ; VV4-sens-15 ; VV4-sens-04 ; VV4-sens-01",
"""- **E2 et manipulation du nombre sur les actions de P3** : extension de N-028 (activations, sondes et couches neuves ;
  [P] l. 415-416, l. 428 ; le GO de N-028 ne couvre que la localisation au champ du coût et l'oracle, `registres/go.md`
  l. 32). Options pour E2 : (a) étendre N-028, E2 greffée sur la passe de P3b (≈ + 0,5 à 1 USD) : réponse rapide, mais une
  lecture de plus sur des données déjà lues, et l'issue « consigne lue, pas l'acte » est prédite pour une sonde apprise sur « Roleplaying » [AP p. 18], pas pour la
  recette « Pairs » [PAR table 3] ; (b) E2
  sur les épisodes neufs de T0.6, à l'aveugle : plus tard ; (c) pas de E2 : le levier le plus cité resterait non éprouvé
  ici. Recommandation : (b), confiance ≈ 55 %. Manipulation du nombre :""",
"""- **E2, bras « moyenne » (iii) de E1 et manipulation du nombre sur les actions de P3** : extension de N-028 (activations,
  sondes et couches neuves ; [P] l. 415-416, l. 428 ; le GO de N-028 ne couvre que la localisation au champ du coût et
  l'oracle, `registres/go.md` à `94ebe409…`, l. 32, GO-2026-10-20-05 ; élargi depuis par GO-2026-10-20-10, voir
  « Décisions prises depuis la v4 »). Options pour E2 : (a) étendre N-028, E2 greffée sur la passe de P3b (≈ + 0,5 à
  1 USD) : réponse rapide, mais une lecture de plus sur des données déjà lues, et l'issue « consigne lue, pas l'acte » est
  prédite pour une sonde apprise sur « Roleplaying » [AP p. 18], pas pour la recette « Pairs » [PAR table 3] ; sur la
  lecture principale (saboteur contre honnête), la littérature ne tranche pas (analogue de P3-P3 le plus proche,
  « Backdoors », sonde Pairs : question 0,832 et 0,849, contre maximum 0,768 et moyenne 0,844 [PAR table 3]) ; (b) E2
  sur les épisodes neufs de T0.6, à l'aveugle : plus tard ; inconvénient : sous P-015 (b), elle ne répond pas à la
  question de P3, sauf condition de référence flagrante ajoutée à T0.6 ; (c) pas de E2 : le levier le plus cité
  resterait non éprouvé ici. **[Décision de Lazar en attente : P-015]** Recommandation, selon l'issue de P-015 :
  - si T0.6 garde une condition de référence qui réplique P3 : (b) ; confiance ≈ 55 % dans la v4, à revoir par le
    rédacteur (VV4-sens-01) ;
  - si P-015 (b) est retenue sans condition de référence flagrante : la question « la position explique-t-elle le nul de
    P3 ? » n'a de réponse que par (a) ; (b) ne dit alors que si la position aide sur l'organisme diffus ; confiance à
    revoir par le rédacteur.

  Ce nœud se tranche avec P-015. Manipulation du nombre :"""))

R.append(("VV4-fidelite-04",
"""  (nœuds) : sans GO, ni l'une ni l'autre ne touche les actions de P3.""",
"""  (nœuds) : sans GO, aucune de ces extensions ne touche les actions de P3."""))

R.append(("VV4-fidelite-04 ; VV4-fidelite-03 ; VV4-sens-13 ; VV4-sens-15",
"""- **Dépense** : E1, puis E3 (et E2 ou la manipulation du nombre si tu étends N-028), sous la délégation R-217 étendue par
  **R-269** (GO-2026-10-20-07 ; `registres/decisions.md` l. 461 ; `registres/go.md` l. 34) : jusqu'au 30 novembre, dans
  GO-2026-10-04-08 prolongé (GO-2026-10-20-06, plafond 150 USD) ; par lancement : préenregistrement scellé et contre-lu
  (R1, R2), **10 USD au plus**, ligne d'accord citant GO-2026-10-20-07 dans `registres/depenses.md`, rapport à toi ; un
  lancement à la fois (R-262) ; devis avant chaque appel. Au-delà de 10 USD par lancement ou du crédit : nœud. Crédit :
  compte à recharge automatique (R-283). T0.6 réécrit en mode « coût » peut dépasser 10 USD par lancement
  (brouillon actuel : 1 536 + 640 épisodes ; P-015) : nœud de dépense possible. E4 (≈ 10 à 20 USD) : au-delà de 10 USD par lancement, nœud (R-269) ; de
  toute façon devis, GO, et GO de changement de modèle.""",
"""- **Dépense** : E1, puis E3 (et E2, le bras (iii) ou la manipulation du nombre si tu étends N-028), sous la délégation
  R-217 étendue par **R-269** (GO-2026-10-20-07 ; `registres/decisions.md` à `38579d98…`, l. 461 ; `registres/go.md` à
  `94ebe409…`, l. 34) : jusqu'au 30 novembre, dans GO-2026-10-04-08 prolongé (GO-2026-10-20-06, plafond 150 USD) ; par
  lancement : préenregistrement scellé et contre-lu (R1, R2), **10 USD au plus**, ligne d'accord citant
  GO-2026-10-20-07 dans `registres/depenses.md`, rapport à toi ; un lancement à la fois (R-262) ; devis avant chaque
  appel. Au-delà de 10 USD par lancement ou du plafond de 150 USD : nœud ; si le contrôle de crédit refuse une création,
  on attend la recharge (R-283). Crédit : compte à recharge automatique (R-283, `registres/decisions.md` à `cc1b108d…`,
  l. 477). T0.6 dans sa forme du 6 octobre dépasserait le plafond de 10 USD par lancement (P-015,
  `docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md`, `6e74c6cb…`, l. 16-17) ; P-015 (b) garde chaque
  lancement sous 10 USD (l. 99-100) ; l'organisme (ii) ≈ 15 USD en deux lancements (l. 125). E4 (≈ 10 à 20 USD) :
  au-delà de 10 USD par lancement, nœud (R-269) ; de toute façon devis, GO, et GO de changement de modèle. Pour les
  lancements de la nuit du 20 au 21 octobre, la borne de 10 USD est levée (GO-2026-10-20-11) : voir « Décisions prises
  depuis la v4 »."""))

R.append(("VV4-sens-16 ; VV4-sens-15",
"""- **Référence boîte noire (nœud 4 du brainstorm)** : ouverte au début de cette correction (R-265 (2),
  `registres/decisions.md` l. 457), hors du GO de N-028 (l. 456) ; **tranchée pendant la correction** par N-029, option
  (c) renforcée (GO-2026-10-20-08, `registres/go.md` l. 35 ; `registres/decisions.md` l. 468-469 ;""",
"""- **Référence boîte noire (nœud 4 du brainstorm)** : ouverte au début de la correction de la v3 (R-265 (2),
  `registres/decisions.md` à `38579d98…`, l. 457), hors du GO de N-028 (l. 456) ; **tranchée pendant la correction** par
  N-029, option (c) renforcée (GO-2026-10-20-08, `registres/go.md` à `94ebe409…`, l. 35 ; `registres/decisions.md` à
  `38579d98…`, l. 468-469 ;"""))

# ---------------------------------------------------------------- section neuve
R.append(("v5 (consigne, point 4)",
"""## 6. Table des clés (empreintes vérifiées ce jour)
""",
"""## Décisions prises depuis la v4

La v4 date du 2026-10-20 vers 18:28 UTC (R-289). Lignes lues le 2026-10-20 vers 23:30 UTC dans `registres/decisions.md`
(`e8b73c64…`, tête `9ecd952`) et `registres/go.md` (`1a392407…`) ; « l. » renvoie à ces versions. Le corps de la v5 garde
l'état de la v4, corrigé des constats ; voici ce que ces décisions y changent, et seulement ce qui touche la revue.

- **Verdict complété de P3 et GO de Lazar** (R-303, l. 503 ; R-305, l. 505 ; GO-2026-10-20-12, `go.md` l. 40). Verdict
  `docs/verdicts/verdict-P3-premier-test-i-a-v2.md` (`05e896da…`) : ligne d'issue inchangée, « aucune sonde générique
  au-dessus du plancher sur (i-a) », nul « non détecté à cette puissance » ; trois réserves non bloquantes de
  l'addendum 2, dont `reserve_B3_puissance_du_nul` sur chacune des deux sondes (« aire minimale détectable à 80 % :
  0,6315 et 0,5966, contre au plus 0,5809 aux hypothèses écrites », R-303). P3 est clos sur ce verdict ; la lecture de P4
  s'ouvre après son run (R-305). Pour la revue : [V] reste le verdict v1 (`0c8ecbdf…`), source des renvois de ligne ;
  la réserve de puissance porte sur le nul que discute la section 1, point 2.
- **Addendum 2 de P3 scellé et passé** (R-297, l. 497 ; R-298, l. 498). La condition posée par la recommandation (1) et
  par les règles communes (« l'addendum 2 de P3 passe avant la lecture de P4-instrument ») est remplie ; la réserve à
  recopier dans la lecture de P4-instrument (R-262) existe : les trois réserves ci-dessus.
- **Lecture « double comptabilité » ajoutée à P3b** (R-296, l. 496 ; GO-2026-10-20-10, `go.md` l. 38). Projection vers
  le vocabulaire de l'état du flux résiduel, couche par couche, au jeton qui précède le premier chiffre du champ du coût,
  sur les textes d'action gardés de P3 ; jetons, couches, règle de lecture et plancher gelés au préenregistrement de
  P3b ; lue comme un mécanisme, jamais comme une intention. Le périmètre de N-028 que cite la v4 (« localisation au champ
  du coût et l'oracle » : table E1, (iii) ; nœud E2) est élargi de cette lecture ; la table E1 ne l'a pas.
- **P-017** (l. 394 ; en partie tranchée par GO-2026-10-20-10 ; pour le reste, défaut (A) le 2026-10-22 vers
  21:15 UTC). Options restantes : (B) sonde de valeur ; (C) « B plus le rejeu contrefactuel 2 × 2 », qui est la
  manipulation du nombre de E1 (v) (rapport « sens », section « Dépassé »). La session y recommande (B), confiance
  ≈ 55 % ; la v4 recommande d'ajouter la manipulation à N-028 (≈ 50 %) : **divergence non résolue**.
- **P-016** (l. 393 ; défaut (A) le 2026-10-22 vers 21:15 UTC ; origine : R-295 (1), l. 495). (A) : pas de P3c,
  « partition de P3b 20/40 ». Si (A) est retenue, E1 ne lit plus les 60 tâches d'un bloc : puissance et options (a) à
  (c) des coûts déjà déclarés (section 4) à revoir (rapport « sens », section « Dépassé »).
- **P-015** (l. 392 ; défaut (b) le 2026-10-22 vers 14:30 UTC ; non tranchée) : objet de VV4-sens-01 ; recommandation (3)
  et nœud E2 écrits en deux versions (**[Décision de Lazar en attente : P-015]**).
- **P-018** (l. 395 ; défaut (A) le 2026-10-22 vers 21:15 UTC) : organisme (ii) ; touche T0.6, donc les épisodes neufs de
  E2 et E3.
- **N-030** (l. 396 ; nœud, non tranché) : l'option (B) ajoute au test de validité de T0.7 T1, « le test à coût égal
  corrigé du coût de la tâche », la sonde de présence de consigne lue sur (ii), et scinde « intention » ; elle rejoint les
  contrôles T1, T3 et T4 que la revue exige de E3.
- **R-295 (1)** (l. 495) : faits énoncés par la session : « T4 tel qu'écrit est confondu par le coût de la tâche (test
  résiduel) » ; à propos de la J-lens, « une mention amorce le concept presque autant qu'une consigne ». La revue emploie
  T4 « à coût déclaré égal » comme contrôle du nombre écrit (sections 4 et 5) : il est touché ; N-030 (B) en propose la
  correction.
- **Dépense de la nuit** (R-302, l. 502 ; GO-2026-10-20-11, `go.md` l. 39, échéance 2026-10-21). Pour les lancements
  payants de la nuit du 20 au 21 octobre, chacun préenregistré, scellé et contre-lu, la borne de 10 USD par lancement ne
  s'applique pas ; plafond de la phase inchangé (150 USD). La section « Dépense » et les mentions « nœud au-delà de
  10 USD par lancement » sont dépassées pour ces lancements seulement. Le plan de la nuit confie la rédaction du
  préenregistrement de P3b à un sous-agent neuf : VV4-sens-04, 11 et 12 (E1, E2) le touchent (rapport « sens », section
  « Dépassé »).
- **Vérification de la v4** (R-300, l. 500) : les deux rapports traités ici, lancés à la demande de Lazar. **Arrêt et
  passation** (R-304, l. 504) : le premier correcteur de la v5 (session 14) a été coupé ; cette v5 vient d'un correcteur
  neuf de la session 16 (relance : R-306, l. 506).
- **P4 en priorité** (R-290, l. 490 ; messages de Lazar) : conforme à la recommandation (1).
- **Sans effet direct sur la revue** : R-291 et R-292 (question de Lazar sur d'autres outils et convergence d'un prompt
  unique, d'où viennent P-016 à P-018 et N-030 par R-295), R-293, R-294 et GO-2026-10-20-09 (tâches du papier C), R-299,
  R-301, P-019, P-020 ; après la plage lue, R-307 à R-309, GO-2026-10-20-13 et -14 (papier C).

## 6. Table des clés (empreintes vérifiées ce jour)
"""))

R.append(("v5",
"""v4 (`…/revue-detection/correction-tour3/`) : `appliquer_corrections_v4.py` (le différentiel, v3 → v4).
""",
"""v4 (`…/revue-detection/correction-tour3/`) : `appliquer_corrections_v4.py` (le différentiel, v3 → v4).
v5 (`…/revue-detection/correction-v5/`) : `appliquer_corrections_v5.py` (le différentiel, v4 → v5, remplacements
exacts, chacun trouvé une seule fois) ; `pagev5.py` (une page d'une source citée) ; `controles_v5.sh` et
`sortie-controles-v5.txt` (phrases et chiffres repris des rapports, à leur page). Les PDF de `[N]` et de `[X]` ne sont
plus dans le bloc-notes restauré : empreintes et compagnons à refaire avant tout versement au dépôt (R6).
"""))


def main():
    src, dst = sys.argv[1], sys.argv[2]
    data = open(src, "rb").read()
    h = hashlib.sha256(data).hexdigest()
    if h != V4_ATTENDU:
        sys.exit(f"v4 inattendue : {h}")
    t = data.decode("utf-8")
    for i, (qui, old, new) in enumerate(R, 1):
        n = t.count(old)
        if n != 1:
            sys.exit(f"remplacement {i} ({qui}) : ancien texte trouvé {n} fois : {old[:80]!r}")
        t = t.replace(old, new)
    open(dst, "w", encoding="utf-8").write(t)
    print(f"{len(R)} remplacements appliqués ; sortie {hashlib.sha256(t.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    main()
