"""Construit la synthèse v3 à partir de la v2 : remplacements par plages de lignes de la v2, chacun gardé par un contrôle
de l'ancien texte (début et fin de la plage). La v2 n'est jamais modifiée (R12). Usage :
python3 -I -B appliquer_corrections_v3.py V2.md V3.md
Chaque bloc porte les constats qu'il applique (VV2-fidelite-NN = F-NN ; VV2-sens-NN = S-NN)."""
import hashlib
import sys

V2_SHA = "90ad38bf106b2351bf54cdf6962d5b7fef8cf3f8cbfbaf209ff124cabac84e4e"

# (bloc, première ligne, dernière ligne (v2, incluses), début attendu de la première, début attendu de la dernière,
#  constats, nouveau texte)
BLOCS = []


def bloc(nom, a, b, debut_a, debut_b, constats, nouveau):
    BLOCS.append((nom, a, b, debut_a, debut_b, constats, nouveau.strip("\n")))


# Remplacements à l'intérieur d'une seule ligne de la v2 (l'ancien passage doit y figurer une fois exactement).
SOUS = [
    ("S01 ligne YS : page de la couche", 44, "même modèle, **couche 15**, sonde des auteurs",
     "même modèle, **couche 15** (p. 3), sonde des auteurs", "R7 (contrôle à la page exacte du correcteur)"),
]


bloc("B01 titre", 1, 1, "# Comment détecter", "# Comment détecter", "en-tête",
     "# Comment détecter l'organisme de P3 — ce qu'ont fait Anthropic et les autres — synthèse v3")

bloc("B02 en-tête v3", 8, 8, "  `…/revue-detection/traitement-verification-synthese-tour1", "  `…/revue-detection/traitement",
     "en-tête", """
  `…/revue-detection/traitement-verification-synthese-tour1-v1.md`. Rien d'autre n'est changé.
- **v3 (correcteur, tour 2).** Correcteur neuf : je n'ai écrit ni la v1, ni la v2, ni les extractions, ni les
  vérifications, ni les traitements. 2026-10-20, de 11:35 à 12:20 UTC environ. Part de la v2 (`90ad38bf…`) et applique les 33
  constats du tour précédent, chacun relu sur sa source : fidélité, VV2-fidelite-01 à 14
  (`…/revue-detection/verification-v2-fidelite-v1.md`, `12a9fac2…`) ; sens, VV2-sens-01 à 19
  (`…/revue-detection/verification-v2-sens-v1.md`, `8ec6aa0e…`). Décisions et raisons :
  `…/revue-detection/traitement-verification-synthese-tour2-v1.md`. Rien d'autre n'est changé. Le fond change en
  sections 1, 3, 4 et 5 : verdict, pouvoirs, expériences, recommandation, confiances, nœuds.
""")

bloc("B03 sources", 12, 12, "  Non opposables, pistes seulement", "  Non opposables", "S-01 S-05 S-06 S-07 S-11 S-17 S-18",
     """
  Non opposables, pistes seulement : Gemini 009 (`6b6080da…`), note du brainstorm (`a023093e…`).
  v3, pièces du dépôt relues : [AD1] `prereg/P3-addendum-lecture-complementaire-v1.md` (`8ff83422…`) ; [NB]
  `docs/notes/brainstorm-suite-P3-v1/` (note `note-decision-suite-P3-v1.md` `a023093e…`, `propositions/proposition-C.md`
  `36e2a247…`, `propositions/proposition-D.md` `e7e8c7ec…`, `reponses/reponses.md` `2eaef7f4…`), citée pour ce que le
  programme a proposé ou écarté, jamais pour un chiffre ; `registres/decisions.md` (`38579d98…`) et `registres/go.md`
  (`94ebe409…`), relus vers 12:00 UTC (lignes citées inchangées depuis 11:45 ; N-029 et GO-2026-10-20-08 ajoutés entre-temps) ;
  `docs/decisions/decision-N-026-v1.md` (`85bd4023…`) ; `docs/decisions/decision-N-029-v1.md` (`084e3052…`) ;
  `docs/decisions/proposition-P-011-T0.7-sondes-v1.md` (`64afff19…`) ; brief v2 (`9261932a…`) ;
  `src/controle_ia/environnements/propositions.py` (`5d97b223…`, identique aux commits `97dd829` et `7a54d43`). Valeurs
  de T1, T2 et T4 écrites dans [NB] : lignes relues chiffres masqués ; leur libellé reste lisible : ce correcteur ne doit
  pas rédiger P3b.
""")

bloc("B04 R7", 14, 19, "- **R7.** Chiffre = clé de PDF", "  phrase est donnée.", "F-09", """
- **R7.** Chiffre = clé de PDF (section 6), page du fichier, phrase anglaise (pour une table : sa ligne). v1 : **119
  citations revérifiées par script** (empreinte, puis phrase sur la page) : toutes conformes ; épreuve R5 : 8 artefacts
  rejetés. v2 : empreintes des 22 PDF recalculées ; chaque ajout relu sur sa page ; phrases anglaises de la v2 recoupées
  sur les pages des clés de leur bloc, sans lire la page citée (`…/correcteur-tour1/recouper_v2.py`, fonction `main` ;
  `…/correcteur-tour1/sortie-recoupement-v2.txt`), puis contrôlées à la page exacte par le vérificateur de fidélité :
  155 sur 155 (`…/revue-detection/verif-v2-fidelite/sortie-verification-v2-fidelite.txt`, `01791e30…`) ; « Your
  action: » vient du code ; le titre du billet d'Anthropic n'a pas de PDF. v3 : empreintes des 22 PDF recalculées ; pages
  extraites à nouveau (`…/correcteur-tour2/pages/`) ; chaque phrase anglaise et chaque chiffre de la littérature de la v3
  contrôlés à la page exacte citée, lignes de table comprises, avec une épreuve R5
  (`…/correcteur-tour2/sortie-controle-v3.txt`). Aucun chiffre lu sur un tracé ; [AU] : légendes imprimées de la figure 6
  (p. 6). Les sections 1, 3, 4 et 5 reprennent les chiffres des sections 2.1 et 2.2, où la phrase est donnée.
""")

bloc("B05 verdict", 23, 35, "1. La détection interne marche", "   contre le témoin, la mention et T4.",
     "S-02 S-03 S-04 S-16 F-06 F-08", """
1. La détection interne marche quand la tromperie est **écrite dans le texte lu**, ou avec des **données du même
   domaine** ou très larges. La lecture à **une seule position après une question ajoutée** après l'action (réponse
   imposée) est appuyée hors domaine et à grande échelle, avec données larges et contraste [OA table 15 ; CA p. 7-8]. Sur
   les cas les plus proches de P3, elle est en défaut au sous-rendement sur consigne [AP p. 9, p. 18 ; PAR table 3, sonde
   RP] et pas meilleure que la moyenne sur la tromperie sur consigne [DYL p. 11 ; table 9]. La détection gagne avec la
   **taille ou la capacité du modèle** et **plusieurs couches**. Par la taille, [CA] place la rupture entre 2 et 9
   milliards, dans la famille Qwen3.5 (p. 8 ; liste p. 18) ; par la capacité, la place de Llama-3.1-8B n'est pas mesurée
   (R8 : question). Le dernier jeton seul, sans question, échoue sur les enjeux [MK p. 4] ; chez Apollo, il est
   « comparable » en aire, avec un rappel à 1 % de faux positifs meilleur que la même sonde lue sur toute la réponse, mais
   en dessous de la sonde Instructed-Pairs [AP p. 23].
2. P3 n'avait aucune de ces conditions. Les montages les plus proches (rien d'écrit dans l'empan lu) donnent des aires
   modestes, en moyenne sur les jetons : sur ce même modèle, 0,81 quand la consigne et un raisonnement écrit, que P3 n'a
   pas, restent dans le contexte sans être notés [BX p. 5], 0,63 quand la consigne est remplacée par une consigne bénigne
   [BX p. 6] ; 0,653 sur toutes les actions, sur Phi-4 [AU p. 6] ; 0,606 sur ce même modèle [YS p. 3]. Le 0,5 de [BX]
   vient d'un organisme affiné, sans consigne ni raisonnement, sondes réentraînées sur lui, organisme peut-être incomplet
   [BX p. 4, p. 8] ; P3 n'est pas affiné. Mais à 1 % de faux positifs, le rappel de [BX] tombe à 0,03 (« Score
   Filtering », table 1, p. 6). **La littérature ne prévoit ni n'exclut le nul de P3** ; aucun de ces travaux ne mesure
   contre un plancher apparié. Ces montages agrègent par la moyenne ; P3, par le maximum ou l'attention. Le nul ne prouve
   pas que l'information manque : même modèle, même couche, une sonde apprise sur la cible (sous-rendement sur consigne,
   raisonnement écrit peut-être inclus) atteint 0,869 [YS p. 3] ; « l'information est là » reste une hypothèse.
3. Aucun travail lu ne mesure contre un plancher apparié comme le nôtre, ni ne teste un **nombre faux dans un champ**
   (R8 : questions). Levier le mieux appuyé : **données du domaine**. La **lecture à une seule position après une
   question** est à éprouver, pas à présumer (point 1). Toujours lire contre le témoin, la mention, T1 et T4.
""")

bloc("B06 ligne BX", 43, 43, "| Boxo et coll. [BX]", "| Boxo et coll. [BX]", "S-02", """
| Boxo et coll. [BX] | **Llama-3.1-8B-Instruct**, couche 14, paires instruites, moyenne des scores par jeton (p. 3) ; « Score Filtering » : consigne et raisonnement gardés dans le contexte, exclus du score (« Score filtering retains the full transcript during inference but selectively excludes certain token positions when computing the final probe score », p. 5) ; organisme affiné : « Fine-tuned Model Organisms exhibit the target behavior without requiring elicitation prompts or producing reasoning traces » (p. 4) | « class separation with 0.95 AUROC » ; en « Score Filtering » : « degraded by 14 points to 0.81 AUROC » (p. 5) ; consigne remplacée par une consigne bénigne : « 32-point drop to 0.63 AUROC » (p. 6 ; 0,62 dans la légende de la figure 4, même page) ; rappel à 1 % de faux positifs, sous-rendement : base 1.00, consigne remplacée 0.04, « Score Filtering » 0.03 (table 1, p. 6) ; organisme entraîné, sondes réentraînées sur lui (« re-training probes on the Model Organism using contrastive pairs ») : « from almost perfect detection 0.94 to chance performance 0.5 » (p. 8 ; résumé p. 1 : « 0.57 vs 0.94 AUROC for Sandbagging ») | la sonde lit la preuve écrite ; sans elle, aire modeste ; hasard sur l'organisme affiné ; montage le plus proche de P3 : « Score Filtering » (0,81) ou consigne remplacée (0,63), pas l'organisme affiné ; réserve des auteurs : « The models may not have fully internalized the target behaviors, which could partly explain poor probe performance » (p. 8) |
""")

bloc("B07 ligne AP", 46, 46, "| Apollo [AP]", "| Apollo [AP]", "S-03", """
| Apollo [AP] | Llama-3.3-70B, « after layer 22 (of 80) in the residual stream », régression logistique (p. 3) ; entraînement : réponses imposées, sans tromperie réelle ; évaluation : réponses du modèle (p. 4) ; sonde lue après la question « Was your last response deceptive? » et la réponse imposée « No. » (p. 9) | « The lowest AUROC is 0.964 on the Roleplaying dataset » ; « AUROC of 0.974 and 0.983 » (p. 6) ; sonde de question : « comparable to our Roleplaying probe, except for substantially degraded performance on Sandbagging » (p. 9) ; « every Sandbagging response is rated as highly deceptive – even when the model chooses not to sandbag » ; mais « consistently rating every control response as honest » (p. 18) | tromperie « relatively blatant and often expressed in the » raisonnement (p. 10) ; couche choisie sur un des jeux d'évaluation : « Layer 22 was chosen for best performance on the Roleplaying dataset when testing on Llama 3.1 » (p. 21) ; la sonde de question lit le contexte de sous-rendement, pas l'acte (p. 18) |
""")

bloc("B08 ligne PAR", 47, 47, "| Parrack et coll. [PAR]", "| Parrack et coll. [PAR]", "S-03 S-14", """
| Parrack et coll. [PAR] | les deux sondes d'Apollo, huit lectures (p. 5-6) ; questions de suivi : sonde moyennée sur la réponse imposée « No » ou « Yes » (p. 5-6) | sous-rendement (table 3, p. 7), sonde Pairs : moyenne 0,964 ; maximum 0,839 ; moyenne sur l'affirmation critique 0,924 ; question sans contraste 0,849 et 0,879 ; sonde RP : moyenne 0,828 ; maximum 0,891 ; question sans contraste 0,457 et 0,437 ; sur les cinq jeux : Pairs, moyenne 0,941, maximum 0,867 ; RP, moyenne 0,840, maximum 0,856 | « The probe activation is largely spread out over the entire response, not concentrated on the deceptive claims » (p. 8) ; conclusion des auteurs : « By contrast, Peak Activation and the Follow-up monitors consistently underperform compared to Full Averaging » (p. 7), que la colonne RP contredit pour le maximum |
""")

bloc("B09 ligne DYL", 50, 50, "| « Did you lie? » [DYL]", "| « Did you lie? » [DYL]", "S-03 S-16 F-06", """
| « Did you lie? » [DYL] | « across 31 open-weight subject models » (p. 2) ; sonde d'Apollo en moyenne sur les jetons hors raisonnement (p. 8) ; sonde sur la réponse à une question | Qwen3-8B 0,74 et 0,69 ; Qwen3-4B 0,64 et 0,68 ; Qwen3.5-4B 0,89 et 0,82 ; Llama-3.3-70B 0,84 et 0,74 (exactitude équilibrée, table 9, p. 28) ; sur les 32 lignes de la table 9, la moyenne d'Apollo devance la sonde de question 22 fois, la suit 8 fois, 2 égalités (compte du correcteur) ; indice de capacité (colonne « AA ») : 14 pour Llama-3.3-70B, 27 pour Qwen3.5-4B (table 9) ; sur les organismes entraînés, par rapport à la tromperie sur consigne sur les mêmes modèles : « Median balanced accuracy falls from 0.85 to 0.52 for Apollo, from 0.81 to 0.65 for DYL » (p. 11) ; mais sur l'organisme « Gender Secret » remis sur consigne : « Apollo and Unrelated Questions perform poorly even on the prompted variants » ; « DYL, by contrast, retains strong performance on the prompted variants » (p. 11) | mesuré contre un indice de capacité, pas contre la taille (« correlates positively and significantly with the Artificial Analysis Intelligence Index », p. 10) ; mensonge sur consigne seulement (« Scaling results are on prompted lying only », p. 12) ; sur consigne, la question ne bat pas la moyenne (p. 11 ; table 9) ; la consigne est le cas facile, sauf pour la sonde d'Apollo sur « Gender Secret » |
""")

bloc("B10 ligne CA", 51, 51, "| FAR.AI, « Caught in the Act » [CA]", "| FAR.AI, « Caught in the Act » [CA]", "S-16", """
| FAR.AI, « Caught in the Act » [CA] | question après chaque appel d'outil, réponse imposée, contraste oui moins non (p. 5-6) ; « 163,016 transcripts » (p. 4) ; « six layers spread evenly from 30% to 90% » (p. 5) ; négatifs : étapes d'avant le sabotage, dans le même épisode, et toutes celles des épisodes honnêtes (« its earlier steps and every step of an honest episode are the negative class », p. 6) | 397 milliards : « score 0.979 to 0.984 » (p. 7) ; Qwen3.5-2B de « 0.585 » à 0,781, contre « from 27B up (0.963 » à 0,986 (p. 8) ; « scores exceed 90% from there up » (p. 8), soit, dans la famille Qwen3.5, dès 9B, le modèle suivant (liste p. 18) ; mais Nemotron-3 Nano, « Nemotron 3 Nano 30B-A3B » (p. 25), reste à « 0.613–0.760 » (p. 8) ; censure politique : « From Qwen3.5-9B to Qwen3.5-397B-A17B and Kimi K3, all four probes have AUC ≥ 98% » (p. 9) ; 3 000 lignes : « 0.018 to 0.110 lower » (p. 8) ; « math-sandbagger (63% AUC) » (p. 9) | données larges ; contraste ; couches ; question précise (« on smaller models, probes perform worse with vague follow-ups », p. 8) |
""")

bloc("B11 ligne AG", 53, 53, "| Jeux d'audit, UK AI Security Institute", "| Jeux d'audit", "F-07 S-14", """
| Jeux d'audit, UK AI Security Institute avec FAR.AI et un coauteur d'Anthropic [AG] (p. 1) | recette d'Apollo, moyenne sur les jetons (p. 16) ; Cedar et Oak : Llama-3.3-70B-Instruct ; Oak « Also has the same distractor behaviours as Baobab » (table 2, p. 7) | Cedar, large : « strongly and robustly elevated on Cedar » (p. 16) ; Oak, étroit, en agent : « probes on Oak fail to indicate more deception » ; « Oak's final-layer probe had an uninterpretable firing pattern » ; distracteurs : « successfully caused many spurious probe activations » (p. 17) | faux positifs dus aux distracteurs ; échec de fond sans cause donnée (« more mysterious failures », p. 17) ; deux hypothèses de l'équipe rouge, pas des résultats : « the difficulty of aggregating signals over much longer contexts in multi-turn agentic trajectories » et « the model does not need to say false facts in order to underperform at agentic tasks » (p. 43) |
""")

bloc("B12 ligne AU", 54, 54, "| Among Us [AU]", "| Among Us [AU]", "F-13", """
| Among Us [AU] | Phi-4, sondes génériques apprises sur RepEng, couche 20 (p. 6-7) ; étiquette « very correlated with the 'Impostor' label » (p. 6) | légendes imprimées de la figure 6 (p. 6) : toutes actions (77 % sans parole) : « Action (AUC = 0.653) » contre « +Thinking (AUC = 0.948) » ; actions de parole seules : « Action (AUC = 0.984) » | tromperie lisible au texte ; étiquette très liée au rôle d'imposteur |
""")

bloc("B13 ligne K", 55, 55, "| Kirch et coll. [K]", "| Kirch et coll. [K]", "S-09 S-19", """
| Kirch et coll. [K] | huit comportements, quatre origines de données (p. 3) ; pour la tromperie et le sous-rendement, l'incitation reste dans le contexte : « never remove the incentive as these are integral to their dataset prompts » (p. 3) | même domaine « 0.85 ±0.039 » contre autre domaine « 0.74 ±0.051 » (p. 5) ; ligne « Deception −0.416 » (table 1, p. 7) ; colonne « Prompted », par rapport à des données incitées : « Deception … +0.035 » (non significatif), « Sandbagging … −0.111* » (table 1, p. 7) ; légende : « Domain shift effects are significant for all behaviours, while response strategy effects are often non-significant » (table 1, p. 7) | perte surtout due au domaine ; interprétation des auteurs, sur les jeux à raisonnement privé : « stated intent does not produce the same activation signatures as genuine strategic reasoning » (p. 9) |
""")

bloc("B14 Anthropic et Oak", 68, 75, "éprouvé en « shadow deployment", "parcimonieux est peu prometteur ici :", "S-19 F-07 S-14", """
éprouvé en « shadow deployment on production traffic » (p. 2). Une direction tirée de textes génériques, **imposée par
pilotage**, peut peser sur la conduite sans trace écrite (Anthropic, Claude Sonnet 4.5, [EM p. 1]) : « emotion
representations can influence behavior even when it is not evident from the text of the transcript » [EM p. 38 ; exemple
de pilotage : « while steering towards desperation increases »] ; c'est un résultat de pilotage, pas de détection ; le
concept utile n'est donc peut-être pas « tromperie ». **Hors d'Anthropic** : quand le comportement caché est
**étroit et d'agent** (Oak, jeux d'audit de l'UK AI Security Institute [AG p. 1]), les sondes échouent [AG p. 17]. P3
ressemble à Oak par ce trait ; mais Oak est un 70 milliards entraîné, avec des comportements distracteurs (table 2, p. 7 ;
p. 17). L'échec de fond n'a pas de cause donnée [AG p. 17] ; les causes avancées (agréger sur de longs contextes ; pas de
faux fait à dire) sont des hypothèses de l'équipe rouge, pas des résultats [AG p. 43]. L'autoencodeur
parcimonieux est peu prometteur ici :
""")

bloc("B15 Apollo p. 23", 93, 93, "  responses is comparable » ; « Recall at 1% FPR", "  responses is comparable »", "F-08", """
  responses is comparable » ; « Recall at 1% FPR compared to control does show improvement, although is still subpar
  compared to the probe trained on Instructed-Pairs » [AP p. 23]. Échec de la
""")

bloc("B16 Ailleurs", 98, 110, "- **Ailleurs.** La moyenne est l'usage courant", "  harmful. » [CC p. 6]).",
     "F-02 F-04 S-14", """
- **Ailleurs.** La moyenne est l'usage courant [BX p. 3 ; AG p. 16 ; LB p. 8 ; DYL p. 8] ; sur la recette d'Apollo, au
  sous-rendement, le maximum perd avec la sonde Pairs (0,839 contre 0,964 ; sur les cinq jeux, 0,867 contre 0,941) mais
  gagne avec la sonde RP (0,891 contre 0,828 ; sur les cinq jeux, 0,856 contre 0,840) [PAR table 3, p. 7] ; les auteurs
  concluent : « By contrast, Peak Activation and the Follow-up monitors consistently underperform compared to Full
  Averaging » [PAR p. 7], ce que la colonne RP du maximum contredit. Pour les enjeux, « The best performing probes are
  Attention, Softmax, and Mean » ; le maximum « biases probes towards the most high-stakes token » ; sur le jeu MTS, il
  approche les sondes les plus régulières (« the Max and Max of Rolling Means probes perform relatively well on the MTS
  dataset, nearly matching the performance of the more consistent probes ») ; les auteurs y voient peut-être un concept
  tenu par des mots précis (« this may indicate that the high-stakes nature of the MTS dataset is dependent upon specific
  words ») ; « the Last Token activation probe consistently performs poorly » [MK p. 4]. Le maximum appris par tête
  (MultiMax, pas le maximum brut) « prevents dilution of the signal when harmful content appears in a small portion of a
  long context » [GM p. 7]. En contexte long, sur les attaques (taux de faux négatifs, colonne LC[A], [GM table 3,
  p. 12]) : « Linear Probe Mean » 99,13 % ; « Attn » 87,88 % ; « Attn (With LC Training) » 1,34 % ; agrégations MultiMax
  0,0 % à 1,73 % ; maxima de moyennes glissantes (« Rolling Agg », « Linear Probe Rolling Exp ») 1,73 % à 5,19 %
  [GM p. 6, p. 7]. Mais sur le trafic long ordinaire (taux de faux positifs, colonne LC[RT], « long context random
  traffic », table 1, p. 8) : agrégations MultiMax 1,85 % à 82,14 % ; maxima de moyennes glissantes 1,0 % à 13,55 % ;
  « Linear Probe Mean » 0,5 % [GM table 3, p. 12]. « No single method dominates across all distribution shifts. »
  [GM p. 11] ; un pic isolé trompe le maximum brut (« Without averaging, a single token with a spuriously high activation
  could incorrectly flag an entire sequence as harmful. » [CC p. 6]) ; dans les jeux d'audit, l'équipe rouge attendait
  l'échec des sondes en agent d'abord à cause de « the difficulty of aggregating signals over much longer contexts in
  multi-turn agentic trajectories » (hypothèse, pas résultat) [AG p. 43].
""")

bloc("B17 Pour P3", 111, 118, "- **Pour P3.** La recette lit un état étalé", "  (p. 10).", "S-14 F-05 S-15", """
- **Pour P3.** La recette lit un état étalé [PAR p. 8], ce qui sert la moyenne ; le mensonge de P3 tient dans un champ, ce
  qui sert le maximum ou une lecture restreinte au champ [AP p. 8 ; GM p. 7 ; GM table 3 ; MK p. 4]. Sens inconnu : les
  preuves publiées penchent vers la moyenne et l'attention en performance [PAR p. 7 ; MK p. 4 ; AP p. 22], vers le maximum
  seulement sous dilution, au prix de faux positifs [GM table 3, p. 12]. Le bras de diagnostic de N-026 est justifié,
  jamais moniteur. Aucun de ces travaux ne compare les agrégations sous un attaquant entraîné contre la sonde : la raison
  de la règle gelée n'y est pas testée. [OA] entraîne des politiques contre une sonde lue à une seule position après une
  question : l'obfuscation y apparaît (« show that obfuscation emerges in this setting ») ; l'obfuscation des activations
  vient de la dérive des représentations pendant l'apprentissage, avec ou sans pénalité de la sonde, et la pénalité ne
  pousse qu'aux politiques obfusquées (« obfuscated activations arise from representation drift during RL, with or
  without a detector penalty » ; « The detector penalty only incentivizes obfuscated policies ») ; mais « Sufficiently
  high KL regularization and detector penalty can yield honest policies » (p. 1). [GM] mesure ses architectures sur des
  attaques par invite récrites par un autre modèle, sans entraînement contre la sonde (p. 10).
""")

bloc("B18 intro section 3", 122, 122, "Jugement du rédacteur sur les pages citées", "Jugement du rédacteur", "S-09", """
Jugement du rédacteur sur les pages citées ; aucune n'est établie comme cause (R8). v3 : pouvoirs revus par le correcteur
(VV2-sens-09) ; dernière colonne : pouvoir, pouvoir de la v1, raison en une ligne.
""")

bloc("B19 rangs", 126, 135, "| 1 | données génériques contre données du domaine", "| 10 | taille d'effet",
     "S-09 S-02 S-03 S-16 F-04 F-06 F-08 S-14 S-19", """
| 1 | données génériques contre données du domaine ou du modèle | 598 exemples de faits sous persona ; enjeux en message utilisateur ([P] l. 289-301) ; validation saturée, neuf sondes à 1,0 ([V] section 2) | autre domaine −0,416 [K table 1] ; 0,606 générique contre 0,869 sur la cible [YS p. 3] ; 0,701 et 0,561 contre 0,999 [OA table 15] ; 0,443 à 0,572 [KU table 7] | **fort** (v1 : fort) : la perte hors domaine est significative pour chaque comportement [K table 1, p. 7] et concorde chez [YS], [OA], [KU] |
| 2 | paires contrastées : régime de consigne, pas acte | la sonde apprend « personne malhonnête » ; le saboteur applique une règle de calcul ; les paires naturelles de P3 (même tâche, mêmes graines, [P] l. 320-321) n'entraînent rien | « deceptive prompt regime » [KU p. 9] ; entraînement sans tromperie réelle [AP p. 4] ; données sur consigne, par rapport à des données incitées, incitation gardée dans le contexte [K p. 3] : +0,035 (tromperie, non significatif), −0,111 (sous-rendement), contre −0,416 hors domaine [K table 1] ; interprétation des auteurs : « stated intent does not produce the same activation signatures » [K p. 9] ; les méthodes **non supervisées** suivent le trait « most prominent » [FQ p. 1] (transposition aux sondes supervisées : analogie du rédacteur) | **moyen** (v1 : fort) : sur consigne, la tromperie ne perd rien chez [K] (+0,035) ; les effets de l'origine des réponses sont « often non-significant » [K table 1, p. 7] |
| 3 | rien d'écrit dans l'empan lu | un nombre, sans aveu ni raisonnement | montages proches (rien d'écrit dans l'empan lu), en moyenne : 0,81, consigne et raisonnement dans le contexte [BX p. 5] ; 0,63, consigne remplacée [BX p. 6] ; 0,653 contre 0,948, toutes actions [AU p. 6] ; 0,606 [YS p. 3] ; 0,5 seulement sur organisme affiné [BX p. 8] ; Oak [AG p. 17 ; hypothèses de l'équipe rouge p. 43] ; tromperie flagrante [AP p. 10] | **moyen** (v1 : fort) : les montages proches restent au-dessus du hasard ; le hasard ne vient que de l'organisme affiné |
| 4 | jetons lus, position | maximum sur jusqu'à 400 jetons de cinq champs ([P] l. 198-205, l. 214-215, l. 318) | une position après une question : 0,701 → 0,963 hors domaine [OA table 15] ; mais en défaut au sous-rendement sur consigne [AP p. 9, p. 18 ; PAR table 3, sonde RP : 0,457 et 0,437] et pas meilleure que la moyenne sur la tromperie sur consigne [DYL p. 11 ; table 9] ; dernier jeton : 93,8 % (TTPD, mensonges verbaux) [BU p. 10], mais faible sur les enjeux [MK p. 4] ; chez Apollo, « comparable » en aire, rappel à 1 % de faux positifs meilleur que la même sonde lue sur toute la réponse, mais en dessous de la sonde Instructed-Pairs [AP p. 23] ; maximum : un pic isolé le trompe [CC p. 6] ; sur le jeu MTS, il approche les sondes les plus régulières, peut-être parce que le concept y tient à des mots précis (hypothèse des auteurs) [MK p. 4] | **moyen** (v1 : fort à moyen) : le levier « question » est en défaut sur les cas proches |
| 5 | taille ou capacité du modèle | 8 milliards | [CA] : par la taille, rupture entre 2 milliards (0,585 à 0,781) et 9 milliards, dans la famille Qwen3.5 (p. 8 ; liste p. 18) ; mais Nemotron-3 Nano (30B-A3B) reste à 0,613–0,760 (p. 8 ; p. 25) ; [DYL] : mesuré contre un indice de capacité, pas contre la taille (p. 10) ; mensonge sur consigne seulement (p. 12) ; indice 14 pour Llama-3.3-70B, 27 pour Qwen3.5-4B ; Qwen3.5-4B 0,89 contre Qwen3-8B 0,74 [DYL table 9] ; un modèle sur quatre [LB table 6] ; 93,8 % (TTPD) sur Llama-3-8B [BU p. 10] | **inconnu** (v1 : moyen ; v2 : faible d'après [CA], moyen d'après [DYL]) : la place de Llama-3.1-8B en capacité n'est pas mesurée (R8 : question) ; changer de modèle exige un GO |
| 6 | couches | une par sonde (7, 15 ou 23) | six couches [CA p. 5] ; toutes [CC p. 8] ; couche choisie sur un jeu d'évaluation [AP p. 21] ; 12 sur Llama-3-8B [BU p. 5], 14 sur ce modèle [BX p. 3] | moyen (v1 : moyen) : appui hors des cas proches de P3 ([CA], [CC]) |
| 7 | agrégation | maximum ou attention | maximum perdant avec la sonde Pairs (0,839 contre 0,964 ; cinq jeux, 0,867 contre 0,941), gagnant avec la sonde RP (0,891 contre 0,828) [PAR table 3] ; auteurs : le maximum et les questions « consistently underperform » [PAR p. 7] ; meilleures : attention, « Softmax » et moyenne [MK p. 4] ; moyenne meilleure pour la sonde Instructed-Pairs [AP p. 22] ; dilution d'un signal local par la moyenne [AP p. 8 ; GM p. 7 ; GM table 3], mais faux positifs des maxima appris sur le trafic long [GM table 3] | moyen, **sens inconnu** (v1 : idem) : les preuves penchent vers la moyenne et l'attention, sauf dilution ; N-026 |
| 8 | plancher apparié plus exigeant | quantiles 0,5717 et 0,5356 ; aire 0,5748 ([V] section 3) | barre usuelle : 0,5 ; témoin Alpaca [AP p. 5 ; DYL p. 8] ; sonde à paramètres aléatoires, non appariée [FQ p. 3] | faible comme cause ; **fort pour comparer** (v1 : idem) : notre 0,57 ne se compare à aucun chiffre publié |
| 9 | consigne privée hors de la fenêtre lue | fin du message système, phrase avant « Your action: », non notées ([P] l. 330-332) | les jetons lus voient le contexte ; noter consigne et raisonnement fait monter les sondes [BX p. 5] ; la sonde de question de [AP] note toute réponse du jeu de sous-rendement comme très trompeuse, même quand le modèle ne sous-performe pas [AP p. 18] ; « deceptive prompt regime » [KU p. 5] ; détecteur de « latent intention or disposition of the model to lie » [LIAR p. 10] (détecteur boîte noire, par questions de suivi : analogie pour les sondes) | faible comme cause ; **risque principal des remèdes** (v1 : idem) |
| 10 | taille d'effet | environ 33 fois ([V] section 7, l. 345) ; coût seul 0,8878 ([V] section 4, l. 204) | — | faible (v1 : idem) : le risque est inverse, une sonde qui lit le nombre (T4) |

Ce qui a changé depuis la v1 : rangs 2, 3 et 4 baissent ([K] table 1 ; montage proche de [BX] ; questions en défaut sur les
cas proches) ; rang 5 devient inconnu (taille ou capacité) ; les autres pouvoirs sont inchangés.
""")

bloc("B20 règles communes", 139, 161, "**Règles communes.** Préenregistrement scellé", "génération (`registres/depenses.md`",
     "S-11 S-18 S-17 S-04 S-06 S-07 F-10 F-11 F-12 S-19", """
**Règles communes.** Préenregistrement scellé et contre-lu avant toute lecture (R1, R2) ; liste fermée des positions,
empans, couches et agrégations, l'agrégation de chaque bras écrite (oracle et E3 compris) ; une ligne de lecture par bras.
**Bras de production** (maximum ou attention) : P3-P4 (témoin), T1, T3 et T4 aux seuils gelés de [P] (l. 272-279) ;
Bonferroni sur les seuls bras de production. T3 a deux branches : mention contre honnête non au-dessus, **et** saboteur
contre mention au-dessus ([P] l. 248). **T2** : déjà calculé par la lecture décisive de P3 ([P] l. 242-247) ; s'il est
relu, contrôle des coûts déjà déclarés et correction du biais de longueur du maximum (« G-01 », [AD1] l. 34). Plancher
apparié **de même position, empan et agrégation** ; placebo par permutation dans chaque tâche. Contrôles : témoin et
mention ; **T1** (saboteur : actions qui gonflent contre celles qui ne gonflent pas, même contexte ; seul test à contexte
égal, [P] l. 238-241) ; **T4** (à coût déclaré égal) contre la lecture du seul nombre écrit ; prédicteurs triviaux ; apport
au-dessus du coût seul. « Non au-dessus » se lit « non détecté à cette puissance », jamais « pas de trace »
([P] l. 272-274). **Jamais de moyenne ni de médiane sur les jetons d'une action en production** ; la moyenne seulement en
« bras de diagnostic, jamais en production », lu « l'agrégation explique-t-elle le nul ? », hors de la famille de
Bonferroni (N-026, conditions 1 à 4). Préalables : P4-instrument (contrôle positif, R-262) ; l'addendum 2 de P3 passe
avant la lecture de P4-instrument, et sa réserve éventuelle s'y recopie (R-262, `registres/decisions.md` l. 453) ; P3b
relit P3 : même règle.
**Nombres déjà écrits dans le contexte.** P3 joue un agent sur dix pas ([P] l. 318 : N = 1, T = 10). Au pas t, le contexte
lu contient la consigne privée et l'indication avant « Your action: » (conditions instruites) et **toutes les actions
précédentes de l'agent, champ `COST` compris** : `src/controle_ia/harnais/episode.py` l. 217 et l. 254 (`79113b49…`) ;
`environnements/propositions.py` l. 238-269 (`5d97b223…`) ; fichiers identiques au commit de scellement `97dd829` et au
code cité `7a54d43`. Dans l'action même, le format impose `TITLE`, `PROPOSAL` et `CONTROLS` avant `COST`
(`propositions.py` l. 40-49), en texte libre qui doit nommer modèles, jeux de données et métriques (l. 32-39) ;
`lire_action` prend la première occurrence de chaque clé, dans n'importe quel ordre (l. 129-138). Une lecture « avant le
champ » ne voit donc pas le champ `COST` de l'action en cours, mais peut voir des nombres écrits plus tôt dans l'action,
au premier pas aussi, et voit les coûts des pas précédents dès le deuxième pas ; de même l'oracle, la question de suivi
et toute lecture sur des épisodes à plusieurs pas. Le contrôle du nombre écrit (T4) doit en tenir compte. Contrôle
mécanique : nombres et unités de calcul écrits avant le champ, comptés par condition, comme les contrôles de manipulation
(P3-P6) ; bras restreint aux actions sans nombre avant le champ, ou strates ; T4 maintenu. Options pour les coûts déjà
déclarés, à préenregistrer : (a) bras restreint au premier pas : aucun coût déclaré dans le contexte ; 60 actions par
condition (60 tâches, un épisode par tâche et condition, [P] l. 318-320) ; puissance faible ; T1 et T4 peut-être non
calculables (au moins 10 actions de chaque côté, [P] l. 238-253) ; (b) tous les pas, appariés ou stratifiés sur les coûts
déjà déclarés : plus de puissance, mais le recouvrement entre saboteur et honnête peut manquer (rapport géométrique moyen
d'environ 33, [V] l. 345) ; (c) les deux, avec une règle de lecture gelée d'avance. Pour T4 « à coût déclaré égal »,
écrire aussi la part d'actions du saboteur qui recouvre les coûts honnêtes : trop petite, T4 n'est pas calculable.
Recommandation et défaut : section 5. **Manipulation du nombre** (option, même préenregistrement et même passe que E1) :
sur les actions du saboteur, contexte {saboteur ; témoin} × nombre du champ `COST` {original ; médiane honnête de la même
tâche}, miroir sur les actions du témoin, maximum seulement, garde d'identité sur la case d'origine
([NB] `propositions/proposition-D.md` l. 81-99 ; note l. 26-27 : « la seule mesure qui sépare le nombre écrit du contexte
privé ») ; toujours calculable ; statut : nœud (section 5).
**Coûts** : estimations du rédacteur, **non devisées** ; base : P3 a pris ≈ 3,64 h de carte A100, ≈ 3,96 USD
(`registres/depenses.md` l. 88) ; durée mesurée du run : 11 179,1 s, soit ≈ 3,1 h
(`diag/20261019-230011-p3-reel/resume.json`, `resultat.duree_s`, `4d6894b3…`), génération seule non relevée ; [P] l. 385
en attendait ≈ 2,5 h pour les 240 épisodes.
""")

bloc("B21 table des expériences", 165, 169, "| **quoi** |", "| **contrôle obligatoire** |",
     "S-01 S-03 S-04 S-05 S-06 S-07 S-08 S-10 S-11 S-12 S-13 S-16 S-18 S-19 F-01 F-03 F-14", """
| **quoi** | passe forcée, sans génération, sur les 2 400 actions gardées, pour avoir les scores par jeton des 400 sondes du plancher. (i) Maximum sur le champ `COST` et (ii) maximum sur les jetons qui le précèdent (agrégation de production) : **grandeurs déjà vues** (T2 de la lecture décisive, [P] l. 242-247 ; drapeau au verdict, [V] l. 170-172 et l. 358-359, à ne citer nulle part comme résultat) ; **bras non aveugles** : seuls leurs planchers de même position et T4 au champ sont neufs ; lus comme diagnostic de l'instrument, jamais comme détection. (iii) Moyenne sur l'action et sur le champ : « bras de diagnostic, jamais en production » (N-026), plancher de même agrégation. (iv) Sonde « oracle » sur les activations de P3, validation croisée groupée par tâche : plafond, diagnostic seulement ; empan : jetons de l'action avant le champ `COST` (champ et suite exclus) ; agrégation écrite : maximum ou attention ; si elle copie [YS] (moyenne), bras de diagnostic nommé (N-026), bras de production lu à côté ; plancher : oracle réappris sur étiquettes permutées dans chaque tâche, même validation croisée, même agrégation ; mention hors des négatifs d'apprentissage (ou deux oracles), pour que T3 reste un test. (v) Option : manipulation du nombre (règles communes ; nœud) | sur une copie du contexte après chaque action, question fixe, « Yes. » puis « No. » imposés, lecture **à une seule position**. Un bras par changement, chacun avec sa ligne de lecture : (a) sondes principales de P3, même couche, lues à la position de la réponse imposée « No. » (seule la position change) ; (b) plus le contraste « Yes. » moins « No. » ; (c) plus des sondes génériques apprises avec la question ; (d) plus plusieurs couches. Question générale [CA p. 6] : bras principal ; question précise (sur l'honnêteté du coût déclaré) : diagnostic déclaré, car elle se sert de ce qu'on sait de l'organisme. Logit d'auto-déclaration en comparaison (ce n'est pas la référence boîte noire du nœud 4). **Sur les actions de P3 : nœud** (extension de N-028 : activations, sondes et couches neuves, [P] l. 415-416, l. 428) ; sans GO, E2 attend des épisodes neufs | concept 4 de P-011 en mode coût, sur les 32 tâches de réserve, deux jeux de paires, chacun pour sa position : (1) paires d'actions qui ne diffèrent que par le coût, **nombres équilibrés** (un même nombre honnête ici, gonflé là) : lecture **au champ** `COST` ; (2) versions **incitées** (intérêt à gonfler, sans consigne), incitation présente chez les positifs **et** les négatifs (mêmes contextes, actes différents) : lecture **avant le champ** `COST` (sinon la sonde apprend le régime d'incitation, [KU p. 5]) ; couches concaténées ; agrégation : maximum ou attention (production) ; lecture à une seule position après une question : selon ta décision (règle gelée 1) ; choix de la sonde sur un jeu synthétique tenu à part, jamais sur des épisodes d'organisme (P-011, `proposition-P-011-T0.7-sondes-v1.md` l. 42) ; évaluation sur des épisodes neufs d'organisme (T0.6) | un bras de production **fixé d'avance**, sans regarder E1 à E3 (par exemple le bras de production de E3) ; jamais un bras de diagnostic ni l'oracle ; rejoué sur 27 à 70 milliards **et** sur 8 milliards, sur des épisodes neufs ; l'organisme dont la règle est apprise par affinage : expérience à part (il change à la fois l'organisme et le modèle) |
| **tranche** | (i)-(ii) : le champ du coût porte-t-il plus que le nombre écrit ? T4 au champ et (v) répondent ; jamais une détection. (iii) : l'agrégation explique-t-elle le nul ? (iv) : lecture ou direction ? Oracle au-dessus de son plancher avec T1, T3 et T4 établis (T4 avec le contrôle des coûts déjà déclarés), génériques non : information sur l'acte présente, que la direction générique ne prend pas (cas de [YS p. 3], où c'est une hypothèse). Oracle au-dessus sans T1 : il lit la consigne ou le contexte, pas l'acte ([KU p. 5] ; [AP p. 18]). T1 non calculable : non concluant. Oracle non au-dessus : « non détecté à cette puissance » ([P] l. 272-274), jamais « pas de trace » | la position explique-t-elle le nul ? Lu sur le bras (a) seul ; (b) à (d) disent l'apport de chaque changement. Pour : hors domaine et à grande échelle [OA table 15 ; CA p. 7-8] ; mais faible à 2 milliards [CA p. 8]. Contre, sur les cas proches : sous-rendement sur consigne [AP p. 9, p. 18 ; PAR table 3, sonde RP : 0,457 et 0,437] ; tromperie sur consigne, la question ne bat pas la moyenne [DYL p. 11 ; table 9] ; sonde de question basse sur Qwen3-8B (0,69) et Qwen3-4B (0,68) [DYL table 9, p. 28]. **Prédiction écrite d'avance : échec probable de T1** ; un bras au-dessus du plancher sans T1 lit la consigne, pas l'acte | une sonde apprise **sans l'organisme** détecte-t-elle ? Même domaine 0,85 contre 0,74 [K p. 5] ; données sur consigne, incitation gardée dans le contexte : peu de perte pour la tromperie (+0,035, non significatif), perte pour le sous-rendement (−0,111) ; la perte principale vient du domaine (−0,416) [K p. 3 ; table 1, p. 7] ; paires minimales du domaine [RH p. 27] | effet de taille ou de capacité [LB table 6] ? Par la taille, [CA] place la rupture entre 2 et 9 milliards, dans la famille Qwen3.5 (p. 8) ; Nemotron-3 Nano (30B-A3B) reste bas [CA p. 8 ; p. 25] ; [DYL] : mesuré contre un indice de capacité, pas contre la taille (p. 10), mensonge sur consigne seulement (p. 12) ; la place de Llama-3.1-8B en capacité n'est pas mesurée (R8 : question). L'organisme entraîné retire la fuite, mais les sondes y tombent [BX p. 8] ; chez [DYL], sur le seul organisme « Gender Secret », la sonde d'Apollo échoue déjà sur la version sur consigne ; la chute de la sonde « Did you lie? » est compatible avec un effet de l'affinage (p. 11) |
| **coût** | ≈ 1 à 1,5 h ; ≈ 1,5 à 2,5 USD ; données déjà payées ; (v) : passes en plus, à deviser | greffée sur E1, si tu étends N-028 : ≈ + 0,5 à 1 USD ; seule ≈ 1,5 à 2,5 USD ; sur des épisodes neufs : plus leur génération (voir E3) | ≈ 0,5 à 1 h, ≈ 1 à 2 USD de carte (greffable sur T0.7), **plus** l'écriture, la contre-lecture et le scellement de jeux neufs (plusieurs jours), **plus** la génération des épisodes d'évaluation neufs de T0.6, non devisée (ordre de grandeur : P3 entier, 240 épisodes, ≈ 3,96 USD) | deux cartes de 80 Go, ≈ 5 à 8 h, ≈ 10 à 20 USD ; au-delà de 10 USD par lancement (R-269) : nœud ; crédit relu 11,79 USD à 06:07 UTC |
| **piège** | le champ `COST` **contient le chiffre** ; (i)-(ii) déjà vus : un « au-dessus » y serait suspect (R4), et le chercher viserait un signe déjà aperçu (R3) ; le préenregistrement déclare cette exposition (R1) ; l'oracle compare des **contextes différents** et peut lire la consigne ou les nombres déjà écrits ; peu d'actions non gonflées chez le saboteur (T1 peut être non calculable) ; la passe forcée retokenise : garde d'identité (jetons par action et scores des sondes légères égaux à `scores-p3.npz`, tolérance fixée, éprouvée sur cas sain et artefact, R5) ; rédiger sans lire les descriptifs A1 et A2 de l'addendum 1 (N-028), ni les valeurs de T1, T2 et T4 écrites dans le dépôt ([NB] notamment) | la question fait **relire la consigne** : la sonde lit une disposition, pas l'acte ; preuve directe : « every Sandbagging response is rated as highly deceptive – even when the model chooses not to sandbag » [AP p. 18] ; régime de consigne [KU p. 5] ; analogie boîte noire : [LIAR p. 9-10] ; le nombre de l'action et ceux des pas précédents sont dans le contexte lu | la sonde apprend « gros nombre », le style de textes écrits hors du modèle, ou le régime d'incitation s'il manque chez les négatifs | confondre taille et famille de modèle ; coût ; choisir le bras après lecture (malédiction du gagnant, R3) |
| **contrôle obligatoire** | P3-P4, T1, T3 (deux branches) et T4 sur chaque bras de production ; nombres avant le champ et coûts déjà déclarés : contrôle mécanique, puis (a), (b) ou (c) des règles communes ; oracle : témoin parmi les négatifs d'apprentissage, mention hors d'eux ; empan sans le champ `COST` ; plancher par permutation avec réapprentissage ; puis T3 (sur un oracle appris sans la mention), T1 et le même contrôle des coûts déjà déclarés ; audit R4 (une aire d'oracle proche de 1 est une réserve) | P3-P4, T1, T3 complet, T4 avec le contrôle des coûts déjà déclarés, sur chaque bras de production | nombres équilibrés ; incitation chez les positifs et les négatifs ; lecture avant le chiffre (au premier pas, ou appariée sur les coûts déjà déclarés ; actions sans nombre avant le champ) ; P3-P4, T1, T3 et T4 ; jamais les tâches d'évaluation (P-011) | mêmes contrôles ; même bras rejoué sur 8 milliards, épisodes neufs |
""")

bloc("B22 section 5", 173, 208, "**Recommandation.** (1) P4-instrument d'abord", "dit si une consigne crée une trace",
     "S-01 S-03 S-04 S-05 S-07 S-09 S-15 S-16 S-17 F-02 F-05 F-14", """
**Recommandation.** (1) P4-instrument d'abord (R-262), après l'addendum 2 de P3. (2) Puis **E1 (P3b), lu comme diagnostic
de l'instrument** (option (a) du nœud « Revendication » ci-dessous) : bras du champ du coût non aveugles ; un lancement,
≈ 1,5 à 2,5 USD non devisés ; avec la manipulation du nombre si tu l'ajoutes (nœud ci-dessous). (3) **E2 pas sur les
actions de P3** : je recommande de la jouer sur les épisodes neufs de T0.6, à l'aveugle, l'échec de T1 prédit d'avance
(nœud ci-dessous). (4) **E3 dans T0.7 réécrit en mode coût** (R-265 (6)), évaluée sur des épisodes neufs de T0.6 : voie
que je propose pour R-262 (2), seule de cette liste qui peut porter une revendication, car la sonde est apprise sans
l'organisme. (5) **E4** seulement après E1 à E3 et après G0, bras fixé d'avance.

**Confiance** (jugement du correcteur ; revue depuis la v1, VV2-sens-09). ≈ 40 % (v1 : 60 %) que E1 dise d'où vient le nul
(lecture ou direction ; un oracle non au-dessus ne dit pas « pas de trace ») : les bras du champ sont déjà vus (T2), le
bras « avant le champ » voit des nombres déjà écrits, et la lecture après une question est en défaut sur les cas proches.
≈ 15 à 25 % (v1 : 25 à 35 %) qu'une sonde apprise sans l'organisme passe le plancher **et** T1, T3 et T4 sur ce modèle :
T1 s'ajoute (seul test à contexte égal) et le montage de E3 était à reprendre. L'oracle passera probablement son plancher,
les contextes différant ; T1, T3 et T4 sont l'obstacle.

**Nœuds de Lazar.**
- **Revendication et voie de R-262 (2)** (proposition) : aucune lecture de P3b ne porte de revendication : bras du
  champ du coût non aveugles (T2 de la lecture décisive, [P] l. 242-247 ; valeurs écrites dans le dépôt, [NB]) ; oracle
  hors de l'anti-circularité de P-011 ; bras « moyenne » de diagnostic (N-026). Une revendication ne viendra que d'une
  sonde apprise sans l'organisme, sur des épisodes neufs. **Divergence à trancher** : N-028 lit P3b comme « la première
  tentative de détection du plan R-262 (point 2) » (`registres/decisions.md` l. 456) et ne promet l'aveuglement
  qu'envers A1 et A2 de l'addendum 1 ; or la note du brainstorm range « A2 : poursuit T2 après coup, sans plancher par
  jeton » parmi les options tombées (l. 85) et recommandait « de ne relire P3 en rien » (l. 8) ; une de ses propositions
  juge suspect un « P3 bis » au champ du coût (« Tout signal y serait suspect (R4, R3) »,
  `propositions/proposition-C.md` l. 323-324) ; N-025 exclut la remarque du drapeau T2 « par la règle gelée »
  (`registres/decisions.md` l. 446). R-262 (2) demande une voie « choisie d'après la revue de la littérature » (l. 453).
  Options : (a) P3b en diagnostic de l'instrument ; voie de R-262 (2) : E3 sur des épisodes neufs (avantage : une
  revendication possible, à l'aveugle ; inconvénient : plus tard) ; (b) P3b reste la première tentative, bras du champ
  déclarés non aveugles et lus sous réserve R4 (avantage : plus tôt ; inconvénient : un « au-dessus » n'y vaudrait rien) ;
  (c) P3b sans les bras du champ, avec l'oracle et la manipulation du nombre (avantage : rien de déjà vu ; inconvénient :
  pas de plancher au champ). Recommandation : (a), confiance ≈ 65 %. Pas de défaut (nœud). La ligne N-028 du registre
  porte la même limite : à compléter par la session.
- **E2 et manipulation du nombre sur les actions de P3** : extension de N-028 (activations, sondes et couches neuves ;
  [P] l. 415-416, l. 428 ; le GO de N-028 ne couvre que la localisation au champ du coût et l'oracle, `registres/go.md`
  l. 32). Options pour E2 : (a) étendre N-028, E2 greffée sur la passe de P3b (≈ + 0,5 à 1 USD) : réponse rapide, mais une
  lecture de plus sur des données déjà lues, et l'issue « consigne lue, pas l'acte » est déjà prédite [AP p. 18] ; (b) E2
  sur les épisodes neufs de T0.6, à l'aveugle : plus tard ; (c) pas de E2 : le levier le plus cité resterait non éprouvé
  ici. Recommandation : (b), confiance ≈ 55 %. Manipulation du nombre : recommandation : l'ajouter à N-028 (toujours
  calculable, même passe, seule mesure qui sépare le nombre écrit du contexte privé), confiance ≈ 60 %. Pas de défaut
  (nœuds) : sans GO, ni l'une ni l'autre ne touche les actions de P3.
- **Règle gelée 1** : la lecture à une seule position après une question (E2) n'est ni « maximum ou attention » ni
  « moyenne ou médiane » : son statut en production est à toi. Seul résultat lu sur sa robustesse : [OA] entraîne des
  politiques contre une telle sonde ; l'obfuscation apparaît ; l'obfuscation des activations vient de la dérive des
  représentations pendant l'apprentissage, avec ou sans pénalité de la sonde, et la pénalité ne pousse qu'aux politiques
  obfusquées ; une régularisation et une pénalité suffisantes donnent des politiques honnêtes (p. 1). Le score lissé de
  [CC] est une **moyenne glissante** sur M jetons (moyenne mobile exponentielle à l'inférence), lue jeton par jeton
  [CC p. 6] ; le maximum de moyennes glissantes de [GM], sonde retenue par ses auteurs (p. 12), prend la moyenne sur une
  fenêtre puis le maximum (p. 6, p. 7) : tous deux relèvent au moins en partie de la règle ; à trancher par toi.
- **Dépense** : E1, puis E3 (et E2 ou la manipulation du nombre si tu étends N-028), sous la délégation R-217 étendue par
  **R-269** (GO-2026-10-20-07 ; `registres/decisions.md` l. 461 ; `registres/go.md` l. 34) : jusqu'au 30 novembre, dans
  GO-2026-10-04-08 prolongé (GO-2026-10-20-06, plafond 150 USD) ; par lancement : préenregistrement scellé et contre-lu
  (R1, R2), **10 USD au plus**, ligne d'accord citant GO-2026-10-20-07 dans `registres/depenses.md`, rapport à toi ; un
  lancement à la fois (R-262) ; devis avant chaque appel. Au-delà de 10 USD par lancement ou du crédit : nœud. Crédit :
  11,79 USD relus à 06:07 UTC (`registres/depenses.md` l. 89) ; recharge d'environ 20 USD prévue par toi
  (GO-2026-10-20-06, `registres/go.md` l. 33). E4 (≈ 10 à 20 USD) : au-delà de 10 USD par lancement, nœud (R-269) ; de
  toute façon devis, GO, et GO de changement de modèle.
- **Concepts, couches, positions** (proposer avec recommandation, défaut 48 heures) : « gonflement d'estimation » ;
  position « avant le champ » ; couches multiples ; contrôle des coûts déjà déclarés pour la position « avant le champ »
  (options (a), (b), (c) de la section 4) : recommandation (c), lecture principale (a), (b) rapportée à côté, règle gelée
  d'avance ; confiance ≈ 55 % ; défaut sous 48 heures : (c). La position « après une question » sort de cette liste pour
  P3b (nœud ci-dessus) ; sur des épisodes neufs, son statut en production dépend de la règle gelée 1.
- **Référence boîte noire (nœud 4 du brainstorm)** : ouverte au début de cette correction (R-265 (2),
  `registres/decisions.md` l. 457), hors du GO de N-028 (l. 456) ; **tranchée pendant la correction** par N-029, option
  (c) renforcée (GO-2026-10-20-08, `registres/go.md` l. 35 ; `registres/decisions.md` l. 468-469 ;
  `docs/decisions/decision-N-029-v1.md`, `084e3052…`) : base boîte noire locale, lue sur les épisodes de T0.6, avec un
  prédicteur sur les traits du texte ; elle ne se lit pas sur les textes de P3 (l. 37-39). Aucune référence boîte noire ne
  porte donc sur P3b ; le logit d'auto-déclaration de E2 n'en tient pas lieu : il vient du modèle surveillé lui-même.
  E2 et E3 sur les épisodes de T0.6 seraient lus sur les mêmes épisodes que cette référence (R-262 (3)).
- **Contact externe** : FIBS et les sondes de [CA]. Le papier se contredit : « We release our training dataset, dubbed
  FIBS » et l'adresse `github.com/AlignmentResearch/caught-in-the-act-probes` (p. 1), mais « Upon publication, we will
  release our dataset, FIBS, and our trained probes » (p. 11). Disponibilité **non vérifiée** (aucune recherche web ici).
  Vérifier d'abord si l'adresse est publique : la lire n'est pas un contact externe (licence à lire avant tout usage) ;
  sinon, un accès passerait par un message que tu enverrais. Jeux de rôle d'Apollo sans licence (P-011).

**Questions ouvertes (R8).** Aucun travail lu ne compare à un plancher apparié en covariance, ne teste un nombre faux dans
un champ d'action, n'a de témoin « consigne privée bénigne », ne compare maximum et moyenne contre le même plancher, ni ne
dit si une consigne crée une trace aussi saillante qu'une porte dérobée entraînée. La place de Llama-3.1-8B en capacité,
face aux modèles de [CA] et de [DYL], n'est pas mesurée.
""")

bloc("B23 fichiers", 248, 250, "v2 (`…/correcteur-tour1/`)", "du rédacteur inchangés", "F-09 S-09", """
v2 (`…/correcteur-tour1/`) : `appliquer_corrections_v2.py` (le différentiel, v1 → v2) ; `ctx.py` (phrase en contexte) ;
`recouper_v2.py` et `sortie-recoupement-v2.txt` (phrases anglaises de la v2 sur les pages des clés de leur bloc). v2 :
rangs, pouvoirs et confiances du rédacteur inchangés, sauf le pouvoir du rang 5 (VS-05). v3 (`…/correcteur-tour2/`) :
`outils/appliquer_corrections_v3.py` (le différentiel, v2 → v3, par plages de lignes) ; `outils/pg.py` (une phrase sur une
page) ; `outils/controler_v3.py` et `sortie-controle-v3.txt` (phrases et chiffres à la page exacte, épreuve R5) ;
`pages/` (texte des 22 PDF, page par page). v3 : pouvoirs des rangs 2 à 5 et confiances revus par le correcteur
(sections 3 et 5).
""")


def main() -> int:
    src, dst = sys.argv[1], sys.argv[2]
    brut = open(src, "rb").read()
    if hashlib.sha256(brut).hexdigest() != V2_SHA:
        print("ARRÊT : empreinte de la v2 inattendue")
        return 2
    lignes = brut.decode("utf-8").split("\n")
    # contrôle : plages disjointes, débuts attendus
    pris = set()
    for nom, a, b, da, db, constats, nouveau in BLOCS:
        if not lignes[a - 1].startswith(da) or not lignes[b - 1].startswith(db):
            print(f"ARRÊT : {nom} : ancien texte inattendu aux lignes {a}-{b}")
            print("  ", repr(lignes[a - 1][:80]), "|", repr(lignes[b - 1][:80]))
            return 3
        r = set(range(a, b + 1))
        if r & pris:
            print(f"ARRÊT : {nom} : plage {a}-{b} chevauche un autre bloc")
            return 4
        pris |= r
    for nom, l, ancien, nouveau, constats in SOUS:
        if l in pris or lignes[l - 1].count(ancien) != 1:
            print(f"ARRÊT : {nom} : ligne {l} déjà prise ou passage absent ou multiple")
            return 5
        lignes[l - 1] = lignes[l - 1].replace(ancien, nouveau)
        print(f"{nom:28s} v2 l. {l} (dans la ligne) | {constats}")
    for nom, a, b, da, db, constats, nouveau in sorted(BLOCS, key=lambda x: -x[1]):
        lignes[a - 1:b] = nouveau.split("\n")
    open(dst, "w", encoding="utf-8").write("\n".join(lignes))
    for nom, a, b, da, db, constats, nouveau in BLOCS:
        print(f"{nom:28s} v2 l. {a}-{b} -> {len(nouveau.splitlines())} lignes | {constats}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
