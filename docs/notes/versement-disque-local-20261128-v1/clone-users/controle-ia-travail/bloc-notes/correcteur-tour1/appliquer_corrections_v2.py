"""Applique le différentiel du tour 1 (VS-01 à VS-25) à la synthèse v1 et écrit la v2.

Chaque remplacement est (étiquette, ancien, nouveau) ; l'ancien doit apparaître exactement une fois dans le texte courant.
La v1 n'est jamais modifiée (R12). Usage : python3 -I appliquer_corrections_v2.py
"""
import hashlib
import sys

R = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/"
V1 = R + "synthese-comment-detecter-v1.md"
V2 = R + "synthese-comment-detecter-v2.md"
EMPREINTE_V1 = "a47f9141b97fa70c1e2c06d6dd6fe92cb8a718965db800787184fcc29f285c04"

REMPLACEMENTS = [
    # ---------------------------------------------------------------- en-tête
    ("titre",
     "ce qu'ont fait Anthropic et les autres — synthèse v1",
     "ce qu'ont fait Anthropic et les autres — synthèse v2"),
    ("v2-entete",
     "  10:15 à 11:00 UTC. Dépôt lu seulement ; non ouverts : consignes de P3, textes d'action, clés. **Rien n'est décidé ici.**\n",
     "  10:15 à 11:00 UTC. Dépôt lu seulement ; non ouverts : consignes de P3, textes d'action, clés. **Rien n'est décidé ici.**\n"
     "- **v2 (correcteur, tour 1).** Correcteur neuf : je n'ai écrit ni la v1, ni les extractions, ni la vérification.\n"
     "  2026-10-20, vers 10:50 UTC. Part de la v1 (`a47f9141…`) et applique les 25 écarts VS-01 à VS-25 de\n"
     "  `…/revue-detection/verification-synthese-v1.md` (`43986648…`), chacun relu sur sa page ; décisions et raisons :\n"
     "  `…/revue-detection/traitement-verification-synthese-tour1-v1.md`. Rien d'autre n'est changé.\n"),
    ("VS-18/en-tête R7",
     "- **R7.** Chiffre = clé de PDF (section 6), page du fichier, phrase anglaise (pour une table : sa ligne). **119 citations\n"
     "  revérifiées par script** (empreinte, puis phrase sur la page) : toutes conformes ; épreuve R5 : 8 artefacts rejetés ; chaque\n"
     "  phrase anglaise de ce texte retrouvée sur sa page. Aucun chiffre lu sur un tracé. Les sections 1, 3 et 4 reprennent les\n"
     "  chiffres des sections 2.1 et 2.2, où la phrase est donnée.",
     "- **R7.** Chiffre = clé de PDF (section 6), page du fichier, phrase anglaise (pour une table : sa ligne). v1 : **119\n"
     "  citations revérifiées par script** (empreinte, puis phrase sur la page) : toutes conformes ; épreuve R5 : 8 artefacts\n"
     "  rejetés. v2 : empreintes des 22 PDF recalculées ; chaque ajout relu sur sa page ; toutes les phrases anglaises de la v2\n"
     "  recoupées sur leur page (`…/correcteur-tour1/sortie-recoupement-v2.txt`). Aucun chiffre lu sur un tracé ; [AU] :\n"
     "  légendes imprimées de la figure 6 (p. 6). Les sections 1, 3 et 4 reprennent les chiffres des sections 2.1 et 2.2, où la\n"
     "  phrase est donnée."),
    # ---------------------------------------------------------------- section 1
    ("VS-03/VS-05 section 1 point 1",
     "1. La détection interne marche quand la sonde lit **une seule position de synthèse** (fin d'énoncé, réponse imposée à une\n"
     "   question ajoutée après l'action), avec des **données du même domaine** ou très larges, ou quand la tromperie est\n"
     "   **écrite dans le texte lu** ; elle gagne avec la **taille du modèle** et **plusieurs couches**.",
     "1. La détection interne marche quand la sonde lit **une seule position après une question ajoutée** après l'action\n"
     "   (réponse imposée), avec des **données du même domaine** ou très larges, ou quand la tromperie est **écrite dans le texte\n"
     "   lu** ; elle gagne avec la **capacité du modèle** (au-dessus de 0,90 dès 9 milliards chez [CA p. 8]) et **plusieurs\n"
     "   couches**. Le dernier jeton seul, sans question, échoue sur les enjeux [MK p. 4] et n'est que « comparable » chez Apollo\n"
     "   [AP p. 23]."),
    ("VS-10/VS-22 section 1 point 2",
     "2. P3 n'avait aucune de ces conditions. Sur ce même modèle, les montages proches tombent à 0,5 [BX p. 8] et 0,606\n"
     "   [YS p. 3] : le nul est celui que la littérature prévoit. Il ne prouve pas que l'information manque : même modèle, même\n"
     "   couche, une sonde apprise sur la cible (sous-rendement sur consigne) atteint 0,869 [YS p. 3].",
     "2. P3 n'avait aucune de ces conditions. Sur ce même modèle, les montages proches tombent à 0,5 [BX p. 8 ; sondes\n"
     "   réentraînées sur un organisme peut-être incomplet] et 0,606 [YS p. 3] : le nul est celui que la littérature prévoit. Ces\n"
     "   montages agrègent par la moyenne ; P3, par le maximum ou l'attention. Le nul ne prouve pas que l'information manque :\n"
     "   même modèle, même couche, une sonde apprise sur la cible (sous-rendement sur consigne, raisonnement écrit peut-être\n"
     "   inclus) atteint 0,869 [YS p. 3] ; « l'information est là » reste une hypothèse."),
    # ---------------------------------------------------------------- section 2.1
    ("VS-22 ligne BX",
     "organisme entraîné : « from almost perfect detection 0.94 to chance performance 0.5 » (p. 8 ; résumé p. 1 : « 0.57 vs 0.94 AUROC for Sandbagging ») | la sonde lit la preuve écrite ; sans elle, hasard |",
     "organisme entraîné, sondes réentraînées sur lui (« re-training probes on the Model Organism using contrastive pairs ») : « from almost perfect detection 0.94 to chance performance 0.5 » (p. 8 ; résumé p. 1 : « 0.57 vs 0.94 AUROC for Sandbagging ») | la sonde lit la preuve écrite ; sans elle, hasard ; réserve des auteurs : « The models may not have fully internalized the target behaviors, which could partly explain poor probe performance » (p. 8) |"),
    ("VS-10 ligne YS",
     "| Yoo et Skapars [YS] | même modèle, **couche 15**, sonde « jeux de rôle » d'Apollo, activations moyennées (p. 3) | « Sandbagging performs poorly (0.606 AUROC). » ; appris sur la cible : « 0.936 / 0.950 / 0.869 AUROC across the three targets » (p. 3) | **l'information est là** ; la direction générique ne la prend pas |",
     "| Yoo et Skapars [YS] | même modèle, **couche 15**, sonde des auteurs apprise sur le jeu « jeux de rôle » d'Apollo (p. 2) ; « average token activations over just the assistant's response » (p. 3) ; le raisonnement écrit du sous-rendement ([AP p. 5]) est-il exclu ? non dit | « Sandbagging performs poorly (0.606 AUROC). » ; appris sur la cible, dans les 100 composantes de la source, validation croisée à cinq plis : « 0.936 / 0.950 / 0.869 AUROC across the three targets » (p. 3) | **l'information est peut-être là** (hypothèse : 0,869 peut lire du texte) ; la direction générique ne la prend pas |"),
    ("VS-09 ligne BU",
     "| Bürger et coll. [BU] | Llama-3-8B-Instruct, « layer 12 over the last token of the response » (p. 10) ; affirmations et négations équilibrées (p. 5) | mensonges de jeux de rôle écrits par le modèle : « 93.8 ± 1.5% » d'exactitude (p. 10) |",
     "| Bürger et coll. [BU] | Llama-3-8B-Instruct (pas le modèle de P3), « layer 12 over the last token of the response » (p. 10) ; affirmations et négations équilibrées (p. 5) | mensonges de jeux de rôle écrits par le modèle, 49 mensonges et 55 réponses vraies : méthode TTPD « 93.8 ± 1.5% » d'exactitude ; régression logistique : « LR with 79 ± 8% accuracy » (p. 10) |"),
    ("VS-11 ligne AP",
     "régression logistique (p. 3) ; réponses imposées, sans tromperie réelle (p. 4) |",
     "régression logistique (p. 3) ; entraînement : réponses imposées, sans tromperie réelle ; évaluation : réponses du modèle (p. 4) |"),
    ("VS-11 ligne AP (couche)",
     "couche choisie sur un jeu hors entraînement (p. 21) |",
     "couche choisie sur un des jeux d'évaluation : « Layer 22 was chosen for best performance on the Roleplaying dataset when testing on Llama 3.1 » (p. 21) |"),
    ("VS-02 ligne PAR",
     "| sous-rendement (table 3, p. 7) : moyenne 0,964 ; maximum 0,839 ; moyenne sur l'affirmation critique 0,924 ; question sans contraste 0,849 et 0,879 |",
     "| sous-rendement, sonde Pairs (table 3, p. 7) : moyenne 0,964 ; maximum 0,839 ; moyenne sur l'affirmation critique 0,924 ; question sans contraste 0,849 et 0,879 ; sonde RP : moyenne 0,828 ; maximum 0,891 ; sur les cinq jeux, RP : moyenne 0,840, maximum 0,856 |"),
    ("VS-05/VS-08 ligne DYL",
     "| Qwen3-8B 0,74 et 0,69 ; Qwen3-4B 0,64 et 0,68 ; Llama-3.3-70B 0,84 et 0,74 (exactitude équilibrée, table 9, p. 28) ; « Median balanced accuracy falls from 0.85 to 0.52 for Apollo » sur organismes entraînés (p. 11) | taille du modèle ; la consigne est le cas facile |",
     "| Qwen3-8B 0,74 et 0,69 ; Qwen3-4B 0,64 et 0,68 ; Qwen3.5-4B 0,89 et 0,82 ; Llama-3.3-70B 0,84 et 0,74 (exactitude équilibrée, table 9, p. 28) ; « Median balanced accuracy falls from 0.85 to 0.52 for Apollo » sur organismes entraînés ; mais sur l'organisme « Gender Secret » remis sur consigne : « Apollo and Unrelated Questions perform poorly even on the prompted variants » ; « DYL, by contrast, retains strong performance on the prompted variants » (p. 11) | **capacité** du modèle, pas taille (« correlates positively and significantly with the Artificial Analysis Intelligence Index », p. 10) ; la consigne est le cas facile, sauf pour la sonde d'Apollo sur « Gender Secret » |"),
    ("VS-24 ligne CA (négatifs)",
     "négatifs : pas d'avant le sabotage, même épisode (p. 6) |",
     "négatifs : étapes d'avant le sabotage, dans le même épisode, et toutes celles des épisodes honnêtes (« its earlier steps and every step of an honest episode are the negative class », p. 6) |"),
    ("VS-05 ligne CA (taille)",
     "« scores exceed 90% from there up » (p. 8) ;",
     "« scores exceed 90% from there up » (p. 8), soit dès Qwen3.5-9B, le modèle suivant (liste p. 18) ; censure politique : « From Qwen3.5-9B to Qwen3.5-397B-A17B and Kimi K3, all four probes have AUC ≥ 98% » (p. 9) ;"),
    ("VS-06 ligne AG",
     "| Jeux d'audit, coauteurs Anthropic [AG] | recette d'Apollo, moyenne sur les jetons (p. 16) | Cedar, large : « strongly and robustly elevated on Cedar » (p. 16) ; Oak, étroit, en agent : « probes on Oak fail to indicate more deception » (p. 17) | « the model does not need to say false facts in order to underperform at agentic tasks » (p. 43) |",
     "| Jeux d'audit, UK AI Security Institute avec FAR.AI et un coauteur d'Anthropic [AG] (p. 1) | recette d'Apollo, moyenne sur les jetons (p. 16) ; Cedar et Oak : Llama-3.3-70B-Instruct ; Oak « Also has the same distractor behaviours as Baobab » (table 2, p. 7) | Cedar, large : « strongly and robustly elevated on Cedar » (p. 16) ; Oak, étroit, en agent : « probes on Oak fail to indicate more deception » ; « Oak's final-layer probe had an uninterpretable firing pattern » ; distracteurs : « successfully caused many spurious probe activations » (p. 17) | distracteurs (p. 17) ; hypothèse de l'équipe rouge, pas résultat : « the model does not need to say false facts in order to underperform at agentic tasks » (p. 43) |"),
    ("VS-18 ligne AU",
     "| Among Us [AU] | Phi-4, sondes génériques (p. 6-7) | « Action (AUC = 0.653) » contre « +Thinking (AUC = 0.948) » (p. 6) | tromperie lisible au texte |",
     "| Among Us [AU] | Phi-4, sondes génériques apprises sur RepEng, couche 20 (p. 6-7) ; étiquette « very correlated with the 'Impostor' label » (p. 6) | légendes imprimées de la figure 6 (p. 6) : toutes actions (77 % sans parole) : « Action (AUC = 0.653) » contre « +Thinking (AUC = 0.948) » ; actions de parole seules : « Action (AUC = 0.984) » | tromperie lisible au texte ; étiquette = rôle |"),
    ("VS-13 ligne K",
     "ligne « Deception −0.416 » (table 1, p. 7) | « stated intent does not produce the same activation signatures as genuine strategic reasoning » (p. 9) |",
     "ligne « Deception −0.416 » (table 1, p. 7) ; colonne « Prompted » : « Deception … +0.035 » (non significatif), « Sandbagging … −0.111* » (table 1, p. 7) | perte surtout due au domaine ; interprétation des auteurs, sur les jeux à raisonnement privé : « stated intent does not produce the same activation signatures as genuine strategic reasoning » (p. 9) |"),
    # ---------------------------------------------------------------- « Ce qu'a fait Anthropic »
    ("VS-06/VS-07 paragraphe Anthropic",
     "**Ce qu'a fait Anthropic.** Ses succès internes portent sur des organismes **entraînés** (porte dérobée, objectif appris),\n"
     "lus avant la génération (jeton « Assistant ») ou par **exploration non supervisée** avec accès aux données d'entraînement\n"
     "[MA p. 1, p. 16-17]. Quand le comportement caché est **étroit et d'agent** (Oak), les sondes de ses coauteurs échouent\n"
     "[AG p. 17, p. 43]. P3 ressemble à Oak. Une direction tirée de textes génériques peut peser sur la conduite sans trace\n"
     "écrite : « emotion representations can influence behavior even when it is not evident from the text of the transcript »",
     "**Ce qu'a fait Anthropic.** Ses succès internes portent sur des organismes **entraînés** : objectif appris, lu avant la\n"
     "génération (jeton « Assistant ») ou par **exploration non supervisée** avec accès aux données d'entraînement [MA p. 1,\n"
     "p. 16-17] ; porte dérobée (billet « Simple probes can catch sleeper agents », **non vérifié** ; mentions de seconde main :\n"
     "[BX p. 3] ; [RO p. 3]). Pour ses défenses contre les contournements, Anthropic lit **toutes les couches** et **lisse le\n"
     "score sur une fenêtre de jetons** [CC p. 6, p. 8 ; « All authors are at Anthropic », p. 1] ; système dit « production-grade »,\n"
     "éprouvé en « shadow deployment on production traffic » (p. 2). Une direction tirée de textes génériques peut peser sur la\n"
     "conduite sans trace écrite (Anthropic, Claude Sonnet 4.5, [EM p. 1]) : « emotion representations can influence behavior\n"
     "even when it is not evident from the text of the transcript »"),
    ("VS-06 paragraphe Anthropic (suite, Oak hors Anthropic)",
     "[EM p. 38] ; le concept utile n'est donc peut-être pas « tromperie ». L'autoencodeur parcimonieux est peu prometteur ici :",
     "[EM p. 38] ; le concept utile n'est donc peut-être pas « tromperie ». **Hors d'Anthropic** : quand le comportement caché est\n"
     "**étroit et d'agent** (Oak, jeux d'audit de l'UK AI Security Institute [AG p. 1]), les sondes échouent [AG p. 17]. P3\n"
     "ressemble à Oak par ce trait ; mais Oak est un 70 milliards entraîné, avec des comportements distracteurs (table 2, p. 7 ;\n"
     "p. 17). La cause « pas de faux fait à dire » est une hypothèse de l'équipe rouge, pas un résultat [AG p. 43]. L'autoencodeur\n"
     "parcimonieux est peu prometteur ici :"),
    # ---------------------------------------------------------------- section 2.2
    ("VS-12 Apollo autres agrégations",
     "il a essayé « Taking the maximum probe score across the model’s\n"
     "  response » et une moyenne seuillée par ReLU ; « We find that taking the mean is best on all datasets for the probe trained\n"
     "  on Instructed-Pairs » ; « In contrast, ReLU does improve performance for the Roleplaying probe on several datasets » ;",
     "il a essayé « Taking the maximum probe score across the model’s\n"
     "  response » et une moyenne seuillée par ReLU (pour la sonde Instructed-Pairs, « the best values for the Instructed-Pairs\n"
     "  probe are so small the method is equivalent to mean ») ; « We find that taking the mean is best on all datasets for the\n"
     "  probe trained on Instructed-Pairs » ; « In contrast, ReLU does improve performance for the Roleplaying probe on several\n"
     "  datasets » ;"),
    ("VS-12 Apollo dernier jeton et lecture précoce",
     "Dernier jeton seul : « performance at distinguishing honest and deceptive responses\n"
     "  is comparable » [AP p. 23]. Échec de la moyenne : « When responses are only partially deceptive, however, this can result\n"
     "  in a misclassification » [AP p. 8]. L'écart chiffré n'est qu'en figure 14a : non repris.",
     "Dernier jeton seul, sur une sonde Roleplaying réentraînée (« here we train a different\n"
     "  probe (on just the last positions of the training data) ») : « performance at distinguishing honest and deceptive\n"
     "  responses is comparable » ; « Recall at 1% FPR compared to control does show improvement » [AP p. 23]. Échec de la\n"
     "  moyenne : « When responses are only partially deceptive, however, this can result in a misclassification » [AP p. 8].\n"
     "  L'écart chiffré n'est qu'en figure 14a : non repris. Lecture précoce : « the probe detects the responses as deceptive\n"
     "  before any explicitly deceptive text is generated (although the chain-of-thought often explicitly describes the intent\n"
     "  to be deceptive) » [AP p. 7]."),
    ("VS-02/VS-03/VS-16 Ailleurs",
     "sur la recette d'Apollo, le\n"
     "  maximum perd (0,839 contre 0,964, [PAR table 3]) ; pour les enjeux, « The best performing probes are Attention, Softmax,\n"
     "  and Mean » et le maximum « biases probes towards the most high-stakes token » [MK p. 4]. Mais le maximum « prevents\n"
     "  dilution of the signal when harmful content appears in a small portion of a long context » [GM p. 7] ; « No single method\n"
     "  dominates across all distribution shifts. » [GM p. 11] ; un pic isolé trompe le maximum brut (« Without averaging, a single\n"
     "  token with a spuriously high activation could incorrectly flag an entire sequence as harmful. » [CC p. 6]).",
     "sur la recette d'Apollo, au\n"
     "  sous-rendement, le maximum perd avec la sonde Pairs (0,839 contre 0,964) mais gagne avec la sonde RP (0,891 contre\n"
     "  0,828 ; sur les cinq jeux, 0,856 contre 0,840) [PAR table 3, p. 7]. Pour les enjeux, « The best performing probes are\n"
     "  Attention, Softmax, and Mean » ; le maximum « biases probes towards the most high-stakes token » : il suit le jeton le plus\n"
     "  marqué et marche quand le concept tient à des mots précis (« the Max and Max of Rolling Means probes perform relatively\n"
     "  well on the MTS dataset ») ; « the Last Token activation probe consistently performs poorly » [MK p. 4]. Le maximum appris\n"
     "  par tête (MultiMax, pas le maximum brut) « prevents dilution of the signal when harmful content appears in a small portion\n"
     "  of a long context » [GM p. 7] ; en contexte long, sur les attaques, la sonde linéaire en moyenne en manque 99,13 % et\n"
     "  l'attention simple 87,88 % (1,34 % entraînée sur des contextes longs), contre 0,0 % à 1,73 % pour les agrégations\n"
     "  MultiMax et 1,73 % à 5,19 % pour les moyennes glissantes (taux de faux négatifs, colonne LC[A], [GM table 3, p. 12]) ;\n"
     "  « No single method dominates across all distribution shifts. » [GM p. 11] ; un pic isolé trompe le maximum brut\n"
     "  (« Without averaging, a single token with a spuriously high activation could incorrectly flag an entire sequence as\n"
     "  harmful. » [CC p. 6])."),
    ("VS-04 Pour P3",
     "qui sert le maximum ou une lecture restreinte au champ [AP p. 8 ; GM p. 7]. Sens imprévisible : le bras de diagnostic de\n"
     "  N-026 est justifié, jamais moniteur. Aucun de ces travaux n'a d'attaquant entraîné contre la sonde : la raison de la règle\n"
     "  gelée n'y est pas testée.",
     "qui sert le maximum ou une lecture restreinte au champ [AP p. 8 ; GM p. 7 ; GM table 3 ; MK p. 4]. Sens imprévisible : le\n"
     "  bras de diagnostic de N-026 est justifié, jamais moniteur. Aucun de ces travaux ne compare les agrégations sous un\n"
     "  attaquant entraîné contre la sonde : la raison de la règle gelée n'y est pas testée. [OA] entraîne des politiques contre\n"
     "  une sonde lue à une seule position après une question : l'obfuscation y apparaît (« show that obfuscation emerges in this\n"
     "  setting »), mais « Sufficiently high KL regularization and detector penalty can yield honest policies » (p. 1). [GM]\n"
     "  mesure ses architectures sur des attaques par invite récrites par un autre modèle, sans entraînement contre la sonde\n"
     "  (p. 10)."),
    # ---------------------------------------------------------------- section 3
    ("VS-13/VS-14 rang 2",
     "| « deceptive prompt regime » [KU p. 9] ; aucune tromperie réelle [AP p. 4] ; « stated intent does not produce the same activation signatures » [K p. 9] ; la méthode suit le trait « most prominent » [FQ p. 1] | **fort** |",
     "| « deceptive prompt regime » [KU p. 9] ; entraînement sans tromperie réelle [AP p. 4] ; données sur consigne : +0,035 (tromperie, non significatif), −0,111 (sous-rendement), contre −0,416 hors domaine [K table 1] ; interprétation des auteurs : « stated intent does not produce the same activation signatures » [K p. 9] ; les méthodes **non supervisées** suivent le trait « most prominent » [FQ p. 1] (transposition aux sondes supervisées : analogie du rédacteur) | **fort** |"),
    ("VS-06/VS-18 rang 3",
     "| 0,95 → 0,81 → 0,5 [BX p. 5, p. 8] ; 0,653 contre 0,948 [AU p. 6] ; Oak [AG p. 17, p. 43] ; tromperie flagrante [AP p. 10] |",
     "| 0,95 → 0,81 → 0,5 [BX p. 5, p. 8] ; 0,653 contre 0,948, toutes actions [AU p. 6] ; Oak [AG p. 17 ; hypothèse de l'équipe rouge p. 43] ; tromperie flagrante [AP p. 10] |"),
    ("VS-03/VS-09/VS-23 rang 4",
     "| 4 | jetons lus, position | maximum sur jusqu'à 400 jetons de cinq champs ([P] l. 198-205, l. 318) | une position : 0,701 → 0,963 [OA table 15] ; 93,8 % [BU p. 10] ; maximum tiré par le jeton extrême [MK p. 4 ; CC p. 6] |",
     "| 4 | jetons lus, position | maximum sur jusqu'à 400 jetons de cinq champs ([P] l. 198-205, l. 214-215, l. 318) | une position après une question : 0,701 → 0,963 [OA table 15] ; dernier jeton : 93,8 % (TTPD, mensonges verbaux) [BU p. 10], mais faible sur les enjeux [MK p. 4] et « comparable » chez Apollo [AP p. 23] ; maximum : un pic isolé le trompe [CC p. 6], mais il marche quand le concept tient à des mots précis [MK p. 4] |"),
    ("VS-05/VS-09 rang 5",
     "| 5 | taille du modèle | 8 milliards | 0,585-0,781 à 2 milliards contre 0,963-0,986 dès 27 [CA p. 8] ; Qwen3-8B 0,74 et 0,69 [DYL table 9] ; un modèle sur quatre [LB table 6] ; mais 93,8 % sur Llama-3-8B [BU p. 10] | moyen ; changer de modèle exige un GO |",
     "| 5 | taille ou capacité du modèle | 8 milliards | [CA] : faible à 2 milliards (0,585 à 0,781), au-dessus de 0,90 dès 9 milliards (p. 8 ; p. 9 ; liste p. 18) ; [DYL] : capacité, pas taille (p. 10) ; Qwen3.5-4B 0,89 contre Qwen3-8B 0,74 [DYL table 9] ; un modèle sur quatre [LB table 6] ; 93,8 % (TTPD) sur Llama-3-8B [BU p. 10] | **faible** d'après [CA], moyen d'après [DYL] ; changer de modèle exige un GO |"),
    ("VS-09/VS-11 rang 6",
     "| six couches [CA p. 5] ; toutes [CC p. 8] ; choix hors entraînement [AP p. 21] ; 12 et 14 sur ce modèle [BU p. 5 ; BX p. 3] |",
     "| six couches [CA p. 5] ; toutes [CC p. 8] ; couche choisie sur un jeu d'évaluation [AP p. 21] ; 12 sur Llama-3-8B [BU p. 5], 14 sur ce modèle [BX p. 3] |"),
    ("VS-02/VS-16 rang 7",
     "| 0,964 contre 0,839 [PAR table 3] ; mais dilution d'un signal local [AP p. 8 ; GM p. 7] |",
     "| maximum perdant avec la sonde Pairs (0,839 contre 0,964), gagnant avec la sonde RP (0,891 contre 0,828) [PAR table 3] ; dilution d'un signal local par la moyenne [AP p. 8 ; GM p. 7 ; GM table 3] |"),
    ("VS-15 rang 9",
     "détecteur de « latent intention or disposition of the model to lie » [LIAR p. 10] |",
     "détecteur de « latent intention or disposition of the model to lie » [LIAR p. 10] (détecteur boîte noire, par questions de suivi : analogie pour les sondes) |"),
    ("VS-23 rang 10",
     "| environ 33 fois ; coût seul 0,8878 ([V] section 4) |",
     "| environ 33 fois ([V] section 7, l. 345) ; coût seul 0,8878 ([V] section 4, l. 204) |"),
    # ---------------------------------------------------------------- section 4
    ("VS-21 règles communes",
     "liste fermée des positions,\n"
     "empans, couches et agrégations ; Bonferroni sur les bras. Plancher apparié **de même position, empan et agrégation** ;",
     "liste fermée des positions,\n"
     "empans, couches et agrégations, l'agrégation de chaque bras écrite (oracle et E3 compris) ; Bonferroni sur les bras.\n"
     "Plancher apparié **de même position, empan et agrégation** ;"),
    ("VS-01 règle commune du nombre déjà écrit",
     "Préalable : P4-instrument (contrôle positif, R-262).\n",
     "Préalable : P4-instrument (contrôle positif, R-262).\n"
     "**Nombre déjà écrit dans le contexte.** P3 joue un agent sur dix pas ([P] l. 318 : N = 1, T = 10). Au pas t, le contexte\n"
     "lu contient la consigne privée et l'indication avant « Your action: » (conditions instruites) et **toutes les actions\n"
     "précédentes de l'agent, champ `COST` compris** : `src/controle_ia/harnais/episode.py` l. 217 et l. 254 (`79113b49…`) ;\n"
     "`environnements/propositions.py` l. 238-269 (`5d97b223…`) ; fichiers identiques au commit de scellement `97dd829` et au\n"
     "code cité `7a54d43`. Une lecture\n"
     "« avant le champ » ne voit donc pas le nombre de l'action en cours, mais voit ceux des pas précédents dès le deuxième pas ;\n"
     "de même l'oracle, la question de suivi et toute lecture sur des épisodes à plusieurs pas. Le contrôle du nombre écrit (T4)\n"
     "doit en tenir compte. Options à préenregistrer : (a) bras restreint au premier pas : aucun coût déclaré dans le contexte ;\n"
     "60 actions par condition (60 tâches, un épisode par tâche et condition, [P] l. 318) ; puissance faible ; T1 et T4\n"
     "peut-être non calculables (au moins 10 actions de chaque côté, [P] l. 238-253) ; (b) tous les pas, appariés ou stratifiés\n"
     "sur les coûts déjà déclarés (par exemple le log10 du plus grand coût lisible des pas précédents) : plus de puissance, mais\n"
     "le recouvrement entre saboteur et honnête peut manquer (rapport moyen d'environ 33, [V] l. 345) ; (c) les deux, avec une\n"
     "règle de lecture gelée d'avance. Pour T4 « à coût déclaré égal », écrire aussi la part d'actions du saboteur qui recouvre\n"
     "les coûts honnêtes : trop petite, T4 n'est pas calculable. Le choix revient à la proposition des positions (section 5).\n"),
    ("VS-21 E1 quoi (oracle)",
     "Sonde « oracle » sur les activations de P3, validation croisée groupée par tâche : plafond, diagnostic seulement |",
     "Sonde « oracle » sur les activations de P3, validation croisée groupée par tâche : plafond, diagnostic seulement ; agrégation écrite : maximum ou attention ; si elle copie [YS] (moyenne), bras de diagnostic nommé (N-026), plancher de même agrégation, bras de production lu à côté |"),
    ("VS-21 E3 quoi (agrégation)",
     "lecture avant le champ `COST` ; couches concaténées ;",
     "lecture avant le champ `COST` ; couches concaténées ; agrégation : maximum ou attention (production) ; lecture à une seule position après une question : selon ta décision (règle gelée 1) ;"),
    ("VS-10 E1 tranche",
     "l'information est là, la direction générique ne la prend pas (cas de [YS p. 3]).",
     "l'information est là, la direction générique ne la prend pas (cas de [YS p. 3], où c'est une hypothèse)."),
    ("VS-05 E2 tranche",
     "faible sur petits modèles [CA p. 8 ; DYL table 9]",
     "faible à 2 milliards [CA p. 8] ; [DYL table 9]"),
    ("VS-13 E3 tranche",
     "Même domaine 0,85 contre 0,74 [K p. 5] ; consigne seule insuffisante [K p. 9] ;",
     "Même domaine 0,85 contre 0,74 [K p. 5] ; données sur consigne : peu de perte pour la tromperie (+0,035), perte pour le sous-rendement (−0,111) ; la perte principale vient du domaine (−0,416) [K table 1] ;"),
    ("VS-05/VS-08 E4 tranche",
     "| effet de taille [CA p. 8 ; LB table 6] ? L'organisme entraîné retire la fuite, mais les sondes y tombent [BX p. 8 ; DYL p. 11] |",
     "| effet de taille ou de capacité [LB table 6] ? Argument affaibli : [CA] dépasse 0,90 dès 9 milliards (p. 8) ; [DYL] : capacité (p. 10). L'organisme entraîné retire la fuite, mais les sondes y tombent [BX p. 8] ; chez [DYL], la sonde d'Apollo échoue déjà sur la version sur consigne ; seule « Did you lie? » chute par l'affinage (p. 11) |"),
    ("VS-19 E4 coût",
     "≈ 10 à 20 USD ; au-dessus du crédit (11,79 USD) |",
     "≈ 10 à 20 USD ; au plafond de 10 USD par lancement ou au-dessus (R-269) : nœud ; crédit relu 11,79 USD à 06:07 UTC |"),
    ("VS-01 E1 piège (oracle)",
     "l'oracle compare des **contextes différents** et peut lire la consigne ;",
     "l'oracle compare des **contextes différents** et peut lire la consigne ou les coûts déjà déclarés (dès le deuxième pas) ;"),
    ("VS-15/VS-01 E2 piège",
     "la sonde lit une disposition, pas l'acte [LIAR p. 9-10] ; le nombre est dans le contexte lu |",
     "la sonde lit une disposition, pas l'acte (analogie : [LIAR p. 9-10] est un détecteur boîte noire, par questions de suivi) ; le nombre de l'action et ceux des pas précédents sont dans le contexte lu |"),
    ("VS-01 E1 contrôle",
     "| T4 sur chaque bras ; le bras « avant le champ » ne voit pas le nombre (attention causale) ; oracle : témoin et mention parmi les négatifs, puis T3 et T1 ;",
     "| T4 sur chaque bras ; le bras « avant le champ » ne voit pas le nombre de l'action en cours (attention causale), mais voit ceux des pas précédents : contrôle (a), (b) ou (c) des règles communes ; oracle : témoin et mention parmi les négatifs, puis T3, T1 et le même contrôle des coûts déjà déclarés ;"),
    ("VS-01 E2 contrôle",
     "| T3 complet ; T1 ; T4 |",
     "| T3 complet ; T1 ; T4 avec le contrôle des coûts déjà déclarés |"),
    ("VS-01 E3 contrôle",
     "| nombres équilibrés ; lecture avant le chiffre ; T4 ;",
     "| nombres équilibrés ; lecture avant le chiffre (au premier pas, ou appariée sur les coûts déjà déclarés) ; T4 ;"),
    # ---------------------------------------------------------------- section 5
    ("VS-04/VS-17 règle gelée 1",
     "- **Règle gelée 1** : la lecture à une seule position après une question (E2) et le score lissé avant le maximum [CC p. 6]\n"
     "  ne sont ni « maximum ou attention » ni « moyenne ou médiane » : leur statut en production est à toi.",
     "- **Règle gelée 1** : la lecture à une seule position après une question (E2) n'est ni « maximum ou attention » ni\n"
     "  « moyenne ou médiane » : son statut en production est à toi. Seul résultat lu sur sa robustesse : [OA] entraîne des\n"
     "  politiques contre une telle sonde ; l'obfuscation apparaît, mais une régularisation et une pénalité suffisantes donnent\n"
     "  des politiques honnêtes (p. 1). Le score lissé de [CC] est une **moyenne glissante** sur M jetons (moyenne mobile\n"
     "  exponentielle à l'inférence), lue jeton par jeton [CC p. 6] : il relève au moins en partie de la règle ; à trancher par toi."),
    ("VS-19 dépense",
     "- **Dépense** : E1 et E2, puis E3, sous GO-2026-10-04-08 prolongé au 30 novembre (R-265 (1)), délégation R-217, un\n"
     "  lancement à la fois, devis avant chaque appel. E4 : devis, GO, et GO de changement de modèle.",
     "- **Dépense** : E1 et E2, puis E3, sous la délégation R-217 étendue par **R-269** (GO-2026-10-20-07 ;\n"
     "  `registres/decisions.md` l. 461 ; `registres/go.md` l. 34) : jusqu'au 30 novembre, dans GO-2026-10-04-08 prolongé\n"
     "  (GO-2026-10-20-06, plafond 150 USD) ; par lancement : préenregistrement scellé et contre-lu (R1, R2), **10 USD au plus**,\n"
     "  ligne d'accord citant GO-2026-10-20-07 dans `registres/depenses.md`, rapport à toi ; un lancement à la fois (R-262) ;\n"
     "  devis avant chaque appel. Au-delà de 10 USD par lancement ou du crédit : nœud. Crédit : 11,79 USD relus à 06:07 UTC\n"
     "  (`registres/depenses.md` l. 89) ; recharge d'environ 20 USD prévue par toi (GO-2026-10-20-06, `registres/go.md` l. 33).\n"
     "  E4 (≈ 10 à 20 USD) atteint ou dépasse le plafond par lancement : devis, GO, et GO de changement de modèle."),
    ("VS-01 concepts, positions",
     "positions « avant le champ » et « après une question » ; couches multiples.",
     "positions « avant le champ » et « après une question » ; contrôle des coûts déjà déclarés pour la position « avant le\n"
     "  champ » (options (a), (b), (c) de la section 4) ; couches multiples."),
    ("VS-20 contact externe",
     "- **Contact externe** : FIBS et les sondes de [CA] : « Upon publication, we will release our dataset, FIBS, and our trained\n"
     "  probes » [CA p. 11] ; un accès passerait par un message que tu enverrais.",
     "- **Contact externe** : FIBS et les sondes de [CA]. Le papier se contredit : « We release our training dataset, dubbed\n"
     "  FIBS » et l'adresse `github.com/AlignmentResearch/caught-in-the-act-probes` (p. 1), mais « Upon publication, we will\n"
     "  release our dataset, FIBS, and our trained probes » (p. 11). Disponibilité **non vérifiée** (aucune recherche web ici).\n"
     "  Vérifier d'abord si l'adresse est publique : la lire n'est pas un contact externe (licence à lire avant tout usage) ;\n"
     "  sinon, un accès passerait par un message que tu enverrais."),
    # ---------------------------------------------------------------- section 6
    ("VS-25 table des clés (en-tête)",
     "`[N]` = `…/revue-detection/pdf-nouveaux/`. Empreintes complètes dans `citations-synthese-v1.json`.",
     "`[N]` = `…/revue-detection/pdf-nouveaux/`. Empreintes complètes dans `citations-synthese-v1.json` (RO : ci-dessous).\n"
     "Compagnons `.sha256` (R6) : présents pour `[D]` et pour MA ; absents pour les neuf autres PDF de `[X]` et `[N]`, dont les\n"
     "empreintes, égales, sont dans `[X]pdf-representations/provenance-representations-v1.md` et\n"
     "`[N]provenance-nouveaux-v1.md` : à créer avant tout versement au dépôt."),
    ("VS-07 table des clés (RO)",
     "| CC | Cunningham et coll. | `[N]2601.04603v1/2601.04603v1.pdf` | `ba8ec657…` |\n",
     "| CC | Cunningham et coll. | `[N]2601.04603v1/2601.04603v1.pdf` | `ba8ec657…` |\n"
     "| RO | Rose et coll. (mention de seconde main seulement) | `[D]2604.01151v3.pdf` | `bde99a620dbbb4064fcfd9a010ac4e92b17b619c5995ae0696911afdbed7686b` |\n"),
    ("v2 fichiers et limites",
     "Limites : chiffres\n"
     "des auteurs non recalculés ; annexes non lues ; coûts non devisés ; classement et confiances = jugements du rédacteur.",
     "Limites : chiffres\n"
     "des auteurs non recalculés ; annexes non lues ; coûts non devisés ; classement et confiances = jugements du rédacteur.\n"
     "v2 (`…/correcteur-tour1/`) : `appliquer_corrections_v2.py` (le différentiel, v1 → v2) ; `ctx.py` (phrase en contexte) ;\n"
     "`recouper_v2.py` et `sortie-recoupement-v2.txt` (phrases anglaises de la v2 sur leur page). Rangs, pouvoirs et confiances\n"
     "du rédacteur inchangés, sauf le pouvoir du rang 5 (VS-05)."),
]


def main() -> int:
    texte = open(V1, encoding="utf-8").read()
    if hashlib.sha256(texte.encode("utf-8")).hexdigest() != EMPREINTE_V1:
        print("empreinte de la v1 inattendue : arrêt")
        return 2
    erreurs = 0
    for etiquette, ancien, nouveau in REMPLACEMENTS:
        n = texte.count(ancien)
        if n != 1:
            print(f"ÉCHEC {etiquette} : {n} occurrence(s)")
            erreurs += 1
            continue
        texte = texte.replace(ancien, nouveau)
        print(f"ok {etiquette}")
    if erreurs:
        print(f"{erreurs} échec(s) : v2 non écrite")
        return 1
    open(V2, "w", encoding="utf-8").write(texte)
    print("v2 écrite :", hashlib.sha256(texte.encode("utf-8")).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main())
