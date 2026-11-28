# Comment détecter l'organisme de P3 — ce qu'ont fait Anthropic et les autres — synthèse v4

- **Pour Lazar.** Rédacteur neuf : je n'ai écrit ni P3, ni sa lecture, ni son verdict, ni les extractions. 2026-10-20,
  10:15 à 11:00 UTC. Dépôt lu seulement ; non ouverts : consignes de P3, textes d'action, clés. **Rien n'est décidé ici.**
- **v2 (correcteur, tour 1).** Correcteur neuf : je n'ai écrit ni la v1, ni les extractions, ni la vérification.
  2026-10-20, vers 10:50 UTC. Part de la v1 (`a47f9141…`) et applique les 25 écarts VS-01 à VS-25 de
  `…/revue-detection/verification-synthese-v1.md` (`43986648…`), chacun relu sur sa page ; décisions et raisons :
  `…/revue-detection/traitement-verification-synthese-tour1-v1.md`. Rien d'autre n'est changé.
- **v3 (correcteur, tour 2).** Correcteur neuf : je n'ai écrit ni la v1, ni la v2, ni les extractions, ni les
  vérifications, ni les traitements. 2026-10-20, de 11:35 à 12:20 UTC environ. Part de la v2 (`90ad38bf…`) et applique les 33
  constats du tour précédent, chacun relu sur sa source : fidélité, VV2-fidelite-01 à 14
  (`…/revue-detection/verification-v2-fidelite-v1.md`, `12a9fac2…`) ; sens, VV2-sens-01 à 19
  (`…/revue-detection/verification-v2-sens-v1.md`, `8ec6aa0e…`). Décisions et raisons :
  `…/revue-detection/traitement-verification-synthese-tour2-v1.md`. Rien d'autre n'est changé. Le fond change en
  sections 1, 3, 4 et 5 : verdict, pouvoirs, expériences, recommandation, confiances, nœuds.
- **v4 (correction, tour 3).** Par la session 14, 2026-10-20 vers 18:27 UTC, qui n'a écrit ni la v1, ni la v2, ni la
  v3, ni les extractions, ni les vérifications. Part de la v3 (`ec4239e9…`) et applique les constats des deux
  vérifications du tour 2 : sens, VV3-sens-01 à 14 (`…/revue-detection/verification-v3-sens-v1.md`, `256f9181…`, « non
  conforme ») ; fidélité, VV3-fidelite-01 à 07 (`…/revue-detection/verification-v3-fidelite-v1.md`, `987b39ea…`,
  « conforme après corrections »). Phrases et chiffres ajoutés : repris de ces deux rapports, qui les ont relus à la
  page et à la ligne ; aucun chiffre neuf. Deux faits datés du dépôt ajoutés : compte Vast.ai à recharge automatique
  (R-283) ; proposition P-015 (périmètre de T0.6 en mode « coût »). Décisions et raisons :
  `…/revue-detection/traitement-verification-synthese-tour3-v1.md`. Rien d'autre n'est changé. Le fond change en
  sections 1, 3, 4 et 5 : contrastes séparés par type (P3-P3 contre T1), prédiction de E2, pouvoirs des rangs 2, 3, 4,
  6 et 9, confiances, nœuds.
- **Sources.** Cinq extractions neuves sous `…/revue-detection/extraction/` (anthropic `1f024c5c…`, apollo `ceb0bfb6…`,
  représentations `ce4d730b…`, agents `f8e52ee4…`, nouveaux `332adaa9…`). [P] `prereg/P3-premier-test-i-a-v1.md`
  (`d975e981…`) ; [V] `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` (`0c8ecbdf…`) ; N-026, N-028, R-262, P-011.
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
  `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.
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
  (p. 6). Les sections 1, 3, 4 et 5 reprennent les chiffres des sections 2.1 et 2.2, où la phrase est donnée. v4 : phrases et
  chiffres ajoutés repris des rapports du tour 2, à recontrôler à la page par la vérification du tour 3.

## 1. Verdict

1. La détection interne marche quand la tromperie est **écrite dans le texte lu**, ou avec des **données du même
   domaine** ou très larges. La lecture à **une seule position après une question ajoutée** après l'action (réponse
   imposée) est appuyée hors domaine et à grande échelle, avec données larges et contraste [OA table 15 ; CA p. 7-8]. Sur
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
   dessous de la sonde Instructed-Pairs [AP p. 23].
2. Deux types de contraste sont à séparer. **P3-P3** oppose deux consignes : le saboteur a une consigne privée, l'honnête
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
   pas un nul. Le nul ne prouve pas que l'information manque : même modèle, même couche, une sonde apprise sur la cible
   (sous-rendement sur consigne, raisonnement écrit peut-être inclus) atteint 0,869 [YS p. 3] ; « l'information est là »
   reste une hypothèse.
3. Aucun travail lu ne mesure contre un plancher apparié comme le nôtre, ni ne teste un **nombre faux dans un champ**
   (R8 : questions). Levier le mieux appuyé : **données du domaine**. La **lecture à une seule position après une
   question** est à éprouver, pas à présumer (point 1). Toujours lire contre le témoin, la mention, T1 et T4.

## 2. Ce qu'ont fait Anthropic et les autres

### 2.1 Table de la littérature (aire = aire sous la courbe ROC)

| travail [clé] | montage (paraphrasé, page) | résultat vérifié (page, phrase) | ce qui a fait marcher ou échouer |
|---|---|---|---|
| Boxo et coll. [BX] | **Llama-3.1-8B-Instruct**, couche 14, paires instruites, moyenne des scores par jeton (p. 3) ; « Score Filtering » : consigne et raisonnement gardés dans le contexte, exclus du score (« Score filtering retains the full transcript during inference but selectively excludes certain token positions when computing the final probe score », p. 5) ; organisme affiné : « Fine-tuned Model Organisms exhibit the target behavior without requiring elicitation prompts or producing reasoning traces » (p. 4) | « class separation with 0.95 AUROC » ; en « Score Filtering » : « degraded by 14 points to 0.81 AUROC » (p. 5) ; consigne remplacée par une consigne bénigne : « 32-point drop to 0.63 AUROC » (p. 6 ; 0,62 dans la légende de la figure 4, même page) ; rappel à 1 % de faux positifs, sous-rendement : base 1.00, consigne remplacée 0.04, « Score Filtering » 0.03 (table 1, p. 6) ; organisme entraîné, sondes réentraînées sur lui (« re-training probes on the Model Organism using contrastive pairs ») : « from almost perfect detection 0.94 to chance performance 0.5 » (p. 8 ; résumé p. 1 : « 0.57 vs 0.94 AUROC for Sandbagging ») | la sonde lit la preuve écrite ; sans elle, aire modeste ; hasard sur l'organisme affiné ; à consigne égale (type T1 : « a system prompt that instructs the model to underperform on questions related to WMDP », p. 4 ; « For sandbagging the labels are derived from step-1 sandbagging decisions », p. 12) : « Score Filtering » (0,81) ou consigne remplacée (0,63) ; l'empan public porte sans doute une justification fausse (« Instead, give bad logic and reasoning, resulting in an incorrect answer », p. 12) ; à consignes différentes (type P3-P3) : rappel contre la conversation ordinaire (« distinguish transcripts containing normal conversational data from those exhibiting the studied behavior », p. 6), 0,03 en « Score Filtering » (table 1) ; pas l'organisme affiné ; réserve des auteurs : « The models may not have fully internalized the target behaviors, which could partly explain poor probe performance » (p. 8) |
| Yoo et Skapars [YS] | même modèle, **couche 15** (p. 3), sonde des auteurs apprise sur le jeu « jeux de rôle » d'Apollo (p. 2) ; « average token activations over just the assistant's response » (p. 3) ; le raisonnement écrit du sous-rendement ([AP p. 5]) est-il exclu ? non dit | « Sandbagging performs poorly (0.606 AUROC). » ; appris sur la cible, dans les 100 composantes de la source, validation croisée à cinq plis : « 0.936 / 0.950 / 0.869 AUROC across the three targets » (p. 3) | **l'information est peut-être là** (hypothèse : 0,869 peut lire du texte) ; la direction générique ne la prend pas |
| Bürger et coll. [BU] | Llama-3-8B-Instruct (pas le modèle de P3), « layer 12 over the last token of the response » (p. 10) ; affirmations et négations équilibrées (p. 5) | mensonges de jeux de rôle écrits par le modèle, 49 mensonges et 55 réponses vraies : méthode TTPD « 93.8 ± 1.5% » d'exactitude ; régression logistique : « LR with 79 ± 8% accuracy » (p. 10) | jeton de synthèse ; mais mensonge verbal et factuel |
| Apollo [AP] | Llama-3.3-70B, « after layer 22 (of 80) in the residual stream », régression logistique (p. 3) ; entraînement : réponses imposées, sans tromperie réelle ; évaluation : réponses du modèle (p. 4) ; sonde lue après la question « Was your last response deceptive? » et la réponse imposée « No. » (p. 9) | « The lowest AUROC is 0.964 on the Roleplaying dataset » ; « AUROC of 0.974 and 0.983 » (p. 6) ; sonde de question : « comparable to our Roleplaying probe, except for substantially degraded performance on Sandbagging » (p. 9) ; « every Sandbagging response is rated as highly deceptive – even when the model chooses not to sandbag » ; mais « consistently rating every control response as honest » (p. 18) | tromperie « relatively blatant and often expressed in the » raisonnement (p. 10) ; couche choisie sur un des jeux d'évaluation : « Layer 22 was chosen for best performance on the Roleplaying dataset when testing on Llama 3.1 » (p. 21) ; la sonde de question lit le contexte de sous-rendement, pas l'acte (p. 18) |
| Parrack et coll. [PAR] | les deux sondes d'Apollo, huit lectures (p. 5-6) ; questions de suivi : sonde moyennée sur la réponse imposée « No » ou « Yes » (p. 5-6) | sous-rendement (table 3, p. 7), sonde Pairs : moyenne 0,964 ; maximum 0,839 ; moyenne sur l'affirmation critique 0,924 ; question sans contraste 0,849 et 0,879 ; sonde RP : moyenne 0,828 ; maximum 0,891 ; question sans contraste 0,457 et 0,437 ; « Backdoors » (consignes différentes : « The system prompt also informs the assistant whether the provided code contains a backdoor », p. 4), sonde Pairs : moyenne 0,844, maximum 0,768, questions 0,832 et 0,849 ; sur les cinq jeux : Pairs, moyenne 0,941, maximum 0,867 ; RP, moyenne 0,840, maximum 0,856 | « The probe activation is largely spread out over the entire response, not concentrated on the deceptive claims » (p. 8) ; conclusion des auteurs : « By contrast, Peak Activation and the Follow-up monitors consistently underperform compared to Full Averaging » (p. 7), que la colonne RP contredit pour le maximum |
| Kumar [KU] | Gemma 3 de 1 à 27 milliards, dernier jeton (p. 4) | paires instruites vers jeux de rôle : 0,572 ; 0,512 ; 0,443 ; 0,460 (table 7, p. 6) | la sonde lit le « deceptive prompt regime » (p. 9) |
| Liars' Bench [LB] | recette d'Apollo, moyenne sur la réponse (p. 8) | mensonges sur consigne : Llama 70B 0,95 ; Qwen 72B 0,60 ; Mistral 24B 0,69 ; Gemma 27B 0,58 (table 6, p. 54) | « superficially correlated with lying » (p. 10) |
| « Did you lie? » [DYL] | « across 31 open-weight subject models » (p. 2) ; sonde d'Apollo en moyenne sur les jetons hors raisonnement (p. 8) ; sonde sur la réponse à une question | Qwen3-8B 0,74 et 0,69 ; Qwen3-4B 0,64 et 0,68 ; Qwen3.5-4B 0,89 et 0,82 ; Llama-3.3-70B 0,84 et 0,74 (exactitude équilibrée, table 9, p. 28) ; sur les 32 lignes de la table 9, la moyenne d'Apollo devance la sonde de question 22 fois, la suit 8 fois, 2 égalités (compte du correcteur) ; indice de capacité (colonne « AA ») : 14 pour Llama-3.3-70B, 27 pour Qwen3.5-4B (table 9) ; sur les organismes entraînés, par rapport à la tromperie sur consigne sur les mêmes modèles : « Median balanced accuracy falls from 0.85 to 0.52 for Apollo, from 0.81 to 0.65 for DYL » (p. 11) ; mais sur l'organisme « Gender Secret » remis sur consigne : « Apollo and Unrelated Questions perform poorly even on the prompted variants » ; « DYL, by contrast, retains strong performance on the prompted variants » (p. 11) | mesuré contre un indice de capacité, pas contre la taille (« correlates positively and significantly with the Artificial Analysis Intelligence Index », p. 10) ; mensonge sur consigne seulement (« Scaling results are on prompted lying only », p. 12) ; sur consigne, la question ne bat pas la moyenne (p. 11 ; table 9) ; la consigne est le cas facile, sauf pour la sonde d'Apollo sur « Gender Secret » |
| FAR.AI, « Caught in the Act » [CA] | question après chaque appel d'outil, réponse imposée, contraste oui moins non (p. 5-6) ; « 163,016 transcripts » (p. 4) ; « six layers spread evenly from 30% to 90% » (p. 5) ; négatifs : étapes d'avant le sabotage, dans le même épisode, et toutes celles des épisodes honnêtes (« its earlier steps and every step of an honest episode are the negative class », p. 6) | 397 milliards : « score 0.979 to 0.984 » (p. 7) ; Qwen3.5-2B de « 0.585 » à 0,781, contre « from 27B up (0.963 » à 0,986 (p. 8) ; « scores exceed 90% from there up » (p. 8), soit, dans la famille Qwen3.5, dès 9B, le modèle suivant (liste p. 18) ; mais Nemotron-3 Nano, « Nemotron 3 Nano 30B-A3B » (p. 25), reste à « 0.613–0.760 » (p. 8) ; censure politique : « From Qwen3.5-9B to Qwen3.5-397B-A17B and Kimi K3, all four probes have AUC ≥ 98% » (p. 9) ; 3 000 lignes : « 0.018 to 0.110 lower » (p. 8) ; « math-sandbagger (63% AUC) » (p. 9) | données larges ; contraste ; couches ; question précise (« on smaller models, probes perform worse with vague follow-ups », p. 8) |
| FAR.AI, « Obfuscation Atlas » [OA] | code tricheur ; sondes hors domaine ; question « Did you respond truthfully? » (p. 5) | table 15 (p. 23) : faits simples, moyenne sur la génération 0,701, question 0,963 ; jeu varié 0,561 contre 0,972 ; sonde du domaine 0,999 | la moyenne hors domaine échoue (p. 5) ; la question transfère |
| Jeux d'audit, UK AI Security Institute avec FAR.AI et un coauteur d'Anthropic [AG] (p. 1) | recette d'Apollo, moyenne sur les jetons (p. 16) ; Cedar et Oak : Llama-3.3-70B-Instruct ; Oak « Also has the same distractor behaviours as Baobab » (table 2, p. 7) | Cedar, large : « strongly and robustly elevated on Cedar » (p. 16) ; Oak, étroit, en agent : « probes on Oak fail to indicate more deception » ; « Oak's final-layer probe had an uninterpretable firing pattern » ; distracteurs : « successfully caused many spurious probe activations » (p. 17) | faux positifs dus aux distracteurs ; échec de fond sans cause donnée (« more mysterious failures », p. 17) ; deux hypothèses de l'équipe rouge, pas des résultats : « the difficulty of aggregating signals over much longer contexts in multi-turn agentic trajectories » et « the model does not need to say false facts in order to underperform at agentic tasks » (p. 43) |
| Among Us [AU] | Phi-4, sondes génériques apprises sur RepEng, couche 20 (p. 6-7) ; « the last 10 tokens for each datapoint », agrégation au test non écrite (p. 7) ; étiquette « very correlated with the 'Impostor' label » (p. 6) | légendes imprimées de la figure 6 (p. 6) : toutes actions (77 % sans parole) : « Action (AUC = 0.653) » contre « +Thinking (AUC = 0.948) » et « +System (AUC = 1.000) » ; « Note that the “+X” notation means the prompt includes all inputs above and including X » (p. 6) : prise à la lettre, « Action » est l'action sans contexte ; actions de parole seules : « Action (AUC = 0.984) » | tromperie lisible au texte ; étiquette très liée au rôle d'imposteur |
| Kirch et coll. [K] | huit comportements, quatre origines de données (p. 3) ; pour la tromperie et le sous-rendement, l'incitation reste dans le contexte : « never remove the incentive as these are integral to their dataset prompts » (p. 3) | même domaine « 0.85 ±0.039 » contre autre domaine « 0.74 ±0.051 » (p. 5) ; ligne « Deception −0.416 » (table 1, p. 7) ; colonne « Prompted », par rapport à des données incitées : « Deception … +0.035 » (non significatif), « Sandbagging … −0.111* » (table 1, p. 7) ; légende : « Domain shift effects are significant for all behaviours, while response strategy effects are often non-significant » (table 1, p. 7) | perte surtout due au domaine ; interprétation des auteurs, sur les jeux à raisonnement privé : « stated intent does not produce the same activation signatures as genuine strategic reasoning » (p. 9) |
| Audit d'objectifs cachés, Anthropic [MA] | Claude 3.5 Haiku entraîné à un objectif caché ; autoencodeurs parcimonieux ; audit à l'aveugle (p. 1, p. 15-17) | « Three teams successfully uncovered the model’s hidden objective » (p. 1) ; traits actifs sur « 96% and 91% of Assistant tokens » (p. 17) | exploration avec les données d'entraînement ; somme sur les jetons pour trouver un trait, pas pour surveiller (p. 16) ; limite : « more diffuse training influences » (p. 3) |

Aussi : Goodfire [RH] apprend une différence de moyennes sur des paires minimales synthétiques du domaine (5 285
conversations, table 4, p. 27) et choisit la sonde sur un « held out set of 250 rollouts » de la distribution visée (p. 9) ;
ses aires ne sont pas reprises (non revérifiées). Le billet d'Anthropic « Simple probes can catch sleeper agents » n'a pas
de PDF : **non vérifié**.

**Ce qu'a fait Anthropic.** Ses succès internes portent sur des organismes **entraînés** : objectif appris, lu avant la
génération (jeton « Assistant ») ou par **exploration non supervisée** avec accès aux données d'entraînement [MA p. 1,
p. 16-17] ; porte dérobée (billet « Simple probes can catch sleeper agents », **non vérifié** ; mentions de seconde main :
[BX p. 3] ; [RO p. 3]). Pour ses défenses contre les contournements, Anthropic lit **toutes les couches** et **lisse le
score sur une fenêtre de jetons** [CC p. 6, p. 8 ; « All authors are at Anthropic », p. 1] ; système dit « production-grade »,
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
sur ce même modèle, le projet antérieur de Lazar trouve le signal hors de l'autoencodeur public
(`docs/notes/confrontation-projet-sycophancie-v1.md`, leçon 2 ; dépôt de Lazar, pas l'état de l'art).

### 2.2 Agrégation, vérifiée sur PDF (pour N-026)

- **Apollo agrège par la moyenne, sur tous les jetons de la réponse finale, raisonnement exclu** : « We then take the mean
  across tokens to get a single deceptiveness-score for each model response. » [AP p. 3] ; « We normally take the mean
  probe-score over all tokens in the model’s response. » [AP p. 22] ; la sonde « only reads activations in the final model
  output excepting the model’s chain-of-thought » [AP p. 35]. À l'entraînement : jetons du fait sauf les cinq derniers
  [AP p. 4].
- **Ce qu'Apollo dit des autres agrégations** [AP p. 22] : il a essayé « Taking the maximum probe score across the model’s
  response » et une moyenne seuillée par ReLU (pour la sonde Instructed-Pairs, « the best values for the Instructed-Pairs
  probe are so small the method is equivalent to mean ») ; « We find that taking the mean is best on all datasets for the
  probe trained on Instructed-Pairs » ; « In contrast, ReLU does improve performance for the Roleplaying probe on several
  datasets » ;
  « very probe and dataset dependent ». Dernier jeton seul, sur une sonde Roleplaying réentraînée (« here we train a different
  probe (on just the last positions of the training data) ») : « performance at distinguishing honest and deceptive
  responses is comparable » ; « Recall at 1% FPR compared to control does show improvement, although is still subpar
  compared to the probe trained on Instructed-Pairs » [AP p. 23]. Échec de la
  moyenne : « When responses are only partially deceptive, however, this can result in a misclassification » [AP p. 8].
  L'écart chiffré n'est qu'en figure 14a : non repris. Lecture précoce : « the probe detects the responses as deceptive
  before any explicitly deceptive text is generated (although the chain-of-thought often explicitly describes the intent
  to be deceptive) » [AP p. 7].
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
- **Pour P3.** La recette lit un état étalé [PAR p. 8], ce qui sert la moyenne ; le mensonge de P3 peut tenir dans un champ, ce
  qui sert le maximum ou une lecture restreinte au champ [AP p. 8 ; GM p. 7 ; GM table 3 ; MK p. 4]. Sens inconnu : les
  preuves publiées penchent vers la moyenne et l'attention en performance [PAR p. 7 ; MK p. 4 ; AP p. 22], sauf la sonde RP de
  [PAR], où le maximum brut gagne sur trois des quatre autres jeux ; sous dilution, le maximum brut perd chez [PAR]
  (jeu « Dilution », table 3, p. 7 : Pairs, moyenne 0,931 contre maximum 0,811 ; RP, 0,907 contre 0,877), les maxima
  appris gagnent en contexte long chez [GM], au prix de faux positifs (table 3, p. 12). Le bras de diagnostic de N-026 est justifié,
  jamais moniteur. Aucun de ces travaux ne compare les agrégations sous un attaquant entraîné contre la sonde : la raison
  de la règle gelée n'y est pas testée. [OA] entraîne des politiques contre une sonde lue à une seule position après une
  question : l'obfuscation y apparaît (« show that obfuscation emerges in this setting ») ; l'obfuscation des activations
  vient de la dérive des représentations pendant l'apprentissage, avec ou sans pénalité de la sonde, et la pénalité ne
  pousse qu'aux politiques obfusquées (« obfuscated activations arise from representation drift during RL, with or
  without a detector penalty » ; « The detector penalty only incentivizes obfuscated policies ») ; mais « Sufficiently
  high KL regularization and detector penalty can yield honest policies » (p. 1). [GM] mesure ses architectures sur des
  attaques par invite récrites par un autre modèle, sans entraînement contre la sonde (p. 10).

## 3. Différences de montage avec P3, classées par pouvoir d'expliquer le nul

Jugement du rédacteur sur les pages citées ; aucune n'est établie comme cause (R8). v3 : pouvoirs revus par le correcteur
(VV2-sens-09) ; v4 : rangs 2, 3, 4, 6 et 9 revus (VV3-sens-01, 02, 10) ; dernière colonne : pouvoir, pouvoir de la v1, raison en une ligne.

| rang | différence | P3 | littérature | pouvoir |
|---|---|---|---|---|
| 1 | données génériques contre données du domaine ou du modèle | 598 exemples de faits sous persona ; enjeux en message utilisateur ([P] l. 289-301) ; validation saturée, neuf sondes à 1,0 ([V] section 2) | autre domaine −0,416 [K table 1] ; 0,606 générique contre 0,869 sur la cible [YS p. 3] ; 0,701 et 0,561 contre 0,999 [OA table 15] ; 0,443 à 0,572 [KU table 7] | **fort** (v1 : fort) : la perte hors domaine est significative pour chaque comportement [K table 1, p. 7] et concorde chez [YS], [OA], [KU] |
| 2 | paires contrastées : régime de consigne, pas acte | la sonde apprend « personne malhonnête » ; le saboteur applique une règle de calcul ; les paires naturelles de P3 (même tâche, mêmes graines, [P] l. 320-321) n'entraînent rien | « deceptive prompt regime » [KU p. 9] : une telle sonde signale le régime de consigne (« flagging that a model is operating under deceptive instructions even when its output happens to be correct », p. 9) ; même hypothèse pour la sonde Instructed-Pairs (« activates somewhat when deception is incentivized (rather than performed) », [AP p. 18]) : elle séparerait le saboteur de l'honnête, ce qui prédit un faux positif sur P3-P3, pas un nul ; entraînement sans tromperie réelle [AP p. 4] ; données sur consigne, par rapport à des données incitées, incitation gardée dans le contexte [K p. 3] : +0,035 (tromperie, non significatif), −0,111 (sous-rendement), contre −0,416 hors domaine [K table 1] ; interprétation des auteurs : « stated intent does not produce the same activation signatures » [K p. 9] ; les méthodes **non supervisées** suivent le trait « most prominent » [FQ p. 1] (transposition aux sondes supervisées : analogie du rédacteur) | **faible à moyen** (v1 : fort ; v3 : moyen) : il exige que la consigne du saboteur, « une règle de calcul », ne soit pas lue comme un régime trompeur, sinon il prédit l'inverse du nul ; sur consigne, la tromperie ne perd rien chez [K] (+0,035) ; les effets de l'origine des réponses sont « often non-significant » [K table 1, p. 7] |
| 3 | rien d'écrit dans l'empan lu | un nombre, sans aveu ni raisonnement | type P3-P3 (consignes différentes, consigne non notée) : maximum 0,768 et moyenne 0,844 [PAR table 3, « Backdoors »] ; 0,58 à 0,95 [LB table 6] ; 0,74 [DYL table 9] ; rappel 0,03 [BX table 1] ; type T1 (consigne égale) : 0,81 et 0,63 [BX p. 5-6], 0,606 [YS p. 3], pour lesquels « rien d'écrit dans l'empan lu » n'est pas établi ([BX p. 12-13] ; [YS] : non dit) ; [AU] : 0,653, dix derniers jetons, agrégation non dite, « +System (AUC = 1.000) » selon la lecture de « +X » [AU p. 6-7] ; 0,5 seulement sur organisme affiné [BX p. 8] ; Oak [AG p. 17 ; hypothèses de l'équipe rouge p. 43] ; tromperie flagrante [AP p. 10] | **moyen** (v1 : fort) : à consignes différentes, les montages proches restent au-dessus du hasard en aire (0,58 à 0,95), mais le rappel à 1 % peut tomber à 0,03 [BX table 1] ; le hasard en aire ne vient que de l'organisme affiné |
| 4 | jetons lus, position | maximum sur jusqu'à 400 jetons de cinq champs ([P] l. 198-205, l. 214-215, l. 318) | une position après une question : 0,701 → 0,963 hors domaine [OA table 15] ; à consigne égale (sous-rendement), en défaut avec les sondes apprises sur « Roleplaying » [AP p. 9, p. 18 ; PAR table 3, sonde RP : 0,457 et 0,437], pas avec la recette « Pairs » de P3 (0,849 et 0,879 contre 0,964 en moyenne [PAR table 3]) ; entre consignes, séparation presque parfaite (« Our recall at 1% is greater than 99% on all four evaluation datasets », [AP p. 18]) ; sur consigne, pas meilleure que la moyenne [DYL p. 11 ; table 9 ; LB p. 8] ; dernier jeton : 93,8 % (TTPD, mensonges verbaux) [BU p. 10], mais faible sur les enjeux [MK p. 4] ; chez Apollo, une sonde « Roleplaying » lue sur les dernières positions, « comparable » en aire, rappel à 1 % de faux positifs sur le témoin meilleur que la sonde Roleplaying apprise et lue sur toutes les positions (moyenne), mais en dessous de la sonde Instructed-Pairs [AP p. 23] ; maximum : un pic isolé le trompe [CC p. 6] ; sur le jeu MTS, il approche les sondes les plus régulières, peut-être parce que le concept y tient à des mots précis (hypothèse des auteurs) [MK p. 4] | **moyen** (v1 : fort à moyen) : issue incertaine sur les cas proches, selon les données d'apprentissage de la sonde |
| 5 | taille ou capacité du modèle | 8 milliards | [CA] : par la taille, rupture entre 2 milliards (0,585 à 0,781) et 9 milliards, dans la famille Qwen3.5 (p. 8 ; liste p. 18) ; mais Nemotron-3 Nano (30B-A3B) reste à 0,613–0,760 (p. 8 ; p. 25) ; [DYL] : mesuré contre un indice de capacité, pas contre la taille (p. 10) ; mensonge sur consigne seulement (p. 12) ; indice 14 pour Llama-3.3-70B, 27 pour Qwen3.5-4B ; Qwen3.5-4B 0,89 contre Qwen3-8B 0,74 [DYL table 9] ; un modèle sur quatre [LB table 6] ; 93,8 % (TTPD) sur Llama-3-8B [BU p. 10] | **inconnu** (v1 : moyen ; v2 : faible d'après [CA], moyen d'après [DYL]) : la place de Llama-3.1-8B en capacité n'est pas mesurée (R8 : question) ; changer de modèle exige un GO |
| 6 | couches | une par sonde (7, 15 ou 23) | six couches, sans comparaison à une seule [CA p. 5] (« All probe architectures perform similarly », p. 8) ; toutes, seule comparaison publiée (« using fewer layers consistently yields worse performance ») [CC p. 8], sur une autre tâche ; sur ce même modèle : « Our per-layer analysis indicates that layer choice has limited effect on monitor performance, particularly beyond the first third of layers » [BX p. 3] ; couche choisie sur un jeu d'évaluation [AP p. 21] ; 12 sur Llama-3-8B [BU p. 5], 14 sur ce modèle [BX p. 3] | faible à moyen (v1 : moyen ; v3 : moyen) : un seul appui, sur une autre tâche ([CC]) ; contre-indice sur ce même modèle ([BX p. 3]) |
| 7 | agrégation | maximum ou attention | maximum perdant avec la sonde Pairs (0,839 contre 0,964 ; cinq jeux, 0,867 contre 0,941), gagnant avec la sonde RP (0,891 contre 0,828) [PAR table 3] ; auteurs : le maximum et les questions « consistently underperform » [PAR p. 7] ; meilleures : attention, « Softmax » et moyenne [MK p. 4] ; moyenne meilleure pour la sonde Instructed-Pairs [AP p. 22] ; dilution d'un signal local par la moyenne [AP p. 8 ; GM p. 7 ; GM table 3], mais faux positifs des maxima appris sur le trafic long [GM table 3] | moyen, **sens inconnu** (v1 : idem) : les preuves penchent vers la moyenne et l'attention, sauf la sonde RP de [PAR] ; sous dilution, résultats opposés ([PAR] ; [GM]) ; N-026 |
| 8 | plancher apparié plus exigeant | quantiles 0,5717 et 0,5356 ; aire 0,5748 ([V] section 3) | barre usuelle : 0,5 ; témoin Alpaca [AP p. 5 ; DYL p. 8] ; sonde à paramètres aléatoires, non appariée [FQ p. 3] | faible comme cause ; **fort pour comparer** (v1 : idem) : notre 0,57 ne se compare à aucun chiffre publié |
| 9 | consigne privée hors de la fenêtre lue | fin du message système, phrase avant « Your action: », non notées ([P] l. 330-332) | les jetons lus voient le contexte ; noter consigne et raisonnement fait monter les sondes, à consigne égale [BX p. 5] ; la sonde de question de [AP], apprise sur « Roleplaying », note toute réponse du jeu de sous-rendement comme très trompeuse, même quand le modèle ne sous-performe pas, à consigne égale [AP p. 18] ; « deceptive prompt regime » [KU p. 5] : entre consignes, une sonde de régime prédit un faux positif sur P3-P3 [KU p. 9] ; détecteur de « latent intention or disposition of the model to lie » [LIAR p. 10] (détecteur boîte noire, par questions de suivi : analogie pour les sondes) | faible comme cause ; **risque principal des remèdes** (v1 : idem) |
| 10 | taille d'effet | environ 33 fois ([V] section 7, l. 345) ; coût seul 0,8878 ([V] section 4, l. 204) | — | faible (v1 : idem) : le risque est inverse, une sonde qui lit le nombre (T4) |

Ce qui a changé depuis la v1 : rangs 2, 3 et 4 baissent ([K] table 1 ; montages proches ; questions) ; rang 5 devient
inconnu (taille ou capacité). v4 : contrastes séparés par type (P3-P3, consignes différentes ; T1, consigne égale) ;
rang 2 faible à moyen (une sonde de régime prédit un faux positif, pas un nul) ; rang 4 « issue incertaine, selon les
données d'apprentissage de la sonde » ; rang 6 faible à moyen ; rang 9 annoté par type ; les autres pouvoirs sont
inchangés.

## 4. Expériences de détection, de la moins chère à la plus chère (dollars et délai)

**Règles communes.** Préenregistrement scellé et contre-lu avant toute lecture (R1, R2) ; liste fermée des positions,
empans, couches et agrégations, l'agrégation de chaque bras écrite (oracle et E3 compris) ; une ligne de lecture par bras.
**Bras de production** (maximum ou attention) : P3-P4 (témoin), T1, T3 et T4 aux seuils gelés de [P] (l. 272-279) ;
Bonferroni sur les seuls bras de production. T3 a deux branches : mention contre honnête non au-dessus, **et** saboteur
contre mention au-dessus ([P] l. 248). **T2** : déjà calculé par la lecture décisive de P3 ([P] l. 242-247) ; s'il est
relu, contrôle des coûts déjà déclarés et correction du biais de longueur du maximum (« G-01 », [AD1] l. 34). Plancher
apparié **de même position, empan et agrégation** ; placebo par permutation dans chaque tâche. Contrôles : témoin et
mention ; **T1** (saboteur : actions qui gonflent contre celles qui ne gonflent pas, **à consigne égale** ; pas à
contexte égal : pas et historique diffèrent, et dès le deuxième pas les coûts déjà déclarés sont dans le contexte ; [P]
l. 238-241 ; pour T1, partout : prédicteurs triviaux (rang du pas, longueur notée, coûts déjà déclarés) et contrôle des
coûts déjà déclarés ; sur le bras du champ et dans E2, T1 ne vaut qu'avec T4, car une sonde qui lit la grandeur du
nombre écrit passerait T1, [P] l. 141-142) ; **T4** (à coût déclaré égal) contre la lecture du seul nombre écrit ; prédicteurs triviaux ; apport
au-dessus du coût seul. « Non au-dessus » se lit « non détecté à cette puissance », jamais « ne sépare pas »
([P] l. 272-274) ; a fortiori jamais « pas de trace ». **Jamais de moyenne ni de médiane sur les jetons d'une action en production** ; la moyenne seulement en
« bras de diagnostic, jamais en production », lu « l'agrégation explique-t-elle le nul ? », (N-026,
conditions 1 à 4) ; hors de la famille de Bonferroni : règle de cette synthèse. Préalables : P4-instrument (contrôle positif, R-262) ; l'addendum 2 de P3 passe
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
privé ») ; toujours calculable ; statut : nœud (section 5). La même note en donne l'inconvénient (« une statistique
neuve ; des planchers qui saturent » ; « le volet « nombre » attend l'addendum 2 », l. 28) et recommandait A1 d'abord,
« C2 seulement après le verdict de A1 et après G0 » (l. 33). Le facteur « contexte » ne change que la consigne et
l'indication ([NB] `propositions/proposition-D.md` l. 93-96) : sur les actions du saboteur, le contexte « témoin » garde
les coûts gonflés des pas précédents et des titres en capitales, contraires à la consigne du témoin ([P] l. 125,
l. 333) ; la mesure sépare donc le nombre **de l'action en cours** de la consigne, historique gardé. Le préenregistrement
dira comment l'historique des coûts est traité (remplacé dans tout l'épisode, premier pas seul, ou strates) et
déclarera ce conflit. Prédiction écrite, reprise de la proposition D : « effet du nombre > 0 ; effet du contexte, à
nombre égal, non détecté » (`proposition-D.md` l. 100-101).
**Coûts** : estimations du rédacteur, **non devisées** ; base : P3 a pris ≈ 3,64 h de carte A100, ≈ 3,96 USD
(`registres/depenses.md` l. 88) ; durée mesurée du run : 11 179,1 s, soit ≈ 3,1 h
(`diag/20261019-230011-p3-reel/resume.json`, `resultat.duree_s`, `4d6894b3…`), génération seule non relevée ; [P] l. 385
en attendait ≈ 2,5 h pour les 240 épisodes.

| | E1 — P3b (GO N-028) | E2 — question de suivi | E3 — sonde du domaine | E4 — échelle |
|---|---|---|---|---|
| **quoi** | passe forcée, sans génération, sur les 2 400 actions gardées, pour avoir les scores par jeton des 400 sondes du plancher. (i) Maximum sur le champ `COST` et (ii) maximum sur les jetons qui le précèdent (agrégation de production) : **grandeurs déjà vues** (T2 de la lecture décisive, [P] l. 242-247 ; drapeau au verdict, [V] l. 170-172 et l. 358-359, à ne citer nulle part comme résultat) ; **bras non aveugles** : seuls leurs planchers de même position, T4 au champ, et P3-P4 et T3 au champ et avant le champ sont neufs (T2 ne porte que sur saboteur contre honnête, [P] l. 242) ; lus comme diagnostic de l'instrument, jamais comme détection. (iii) Moyenne sur l'action et sur le champ : « bras de diagnostic, jamais en production » (N-026), plancher de même agrégation ; base : N-026 permet ce bras dans un préenregistrement, mais il n'est pas dans le périmètre du GO de N-028 (localisation au champ et oracle, `registres/go.md` l. 32) : extension de N-028, comme E2 et la manipulation (nœud). (iv) Sonde « oracle » sur les activations de P3, validation croisée groupée par tâche : plafond, diagnostic seulement ; empan : jetons de l'action avant le champ `COST` (champ et suite exclus) ; agrégation écrite : maximum ou attention ; si elle copie [YS] (moyenne), bras de diagnostic nommé (N-026), bras de production lu à côté ; plancher : oracle réappris sur étiquettes permutées dans chaque tâche, même validation croisée, même agrégation ; mention hors des négatifs d'apprentissage (ou deux oracles), pour que T3 reste un test. (v) Option : manipulation du nombre (règles communes ; nœud) | sur une copie du contexte après chaque action, question fixe, « Yes. » puis « No. » imposés, lecture **à une seule position**. Un bras par changement, chacun avec sa ligne de lecture : (a) sondes principales de P3, même couche, lues à la position de la réponse imposée « No. » (seule la position change) ; (b) plus le contraste « Yes. » moins « No. » ; (c) plus des sondes génériques apprises avec la question ; (d) plus plusieurs couches. Question générale [CA p. 6] : bras principal ; question précise (sur l'honnêteté du coût déclaré) : diagnostic déclaré, car elle se sert de ce qu'on sait de l'organisme. Logit d'auto-déclaration en comparaison (ce n'est pas la référence boîte noire du nœud 4). **Sur les actions de P3 : nœud** (extension de N-028 : activations, sondes et couches neuves, [P] l. 415-416, l. 428) ; sans GO, E2 attend des épisodes neufs | concept 4 de P-011 en mode coût, sur les 32 tâches de réserve, deux jeux de paires, chacun pour sa position : (1) paires d'actions qui ne diffèrent que par le coût, **nombres équilibrés** (un même nombre honnête ici, gonflé là) : lecture **au champ** `COST` ; (2) versions **incitées** (intérêt à gonfler, sans consigne), incitation présente chez les positifs **et** les négatifs (mêmes contextes, actes différents) : lecture **avant le champ** `COST` (sinon la sonde apprend le régime d'incitation, [KU p. 5]) ; couches concaténées ; agrégation : maximum ou attention (production) ; lecture à une seule position après une question : selon ta décision (règle gelée 1) ; choix de la sonde sur un jeu synthétique tenu à part, jamais sur des épisodes d'organisme (P-011, `proposition-P-011-T0.7-sondes-v1.md` l. 42) ; évaluation sur des épisodes neufs d'organisme (T0.6) | un bras de production **fixé d'avance** : écrit dans le préenregistrement scellé de E3, ou dans une note scellée maintenant, avant toute lecture de E1 à E3 (par exemple le bras de production de E3) ; jamais un bras de diagnostic ni l'oracle ; rejoué sur 27 à 70 milliards **et** sur 8 milliards, sur des épisodes neufs ; l'organisme dont la règle est apprise par affinage : expérience à part (il change à la fois l'organisme et le modèle) |
| **tranche** | (i)-(ii) : le champ du coût porte-t-il plus que le nombre écrit ? T4 au champ et (v) répondent ; jamais une détection. (iii) : l'agrégation explique-t-elle le nul ? (iv) : lecture ou direction ? Oracle au-dessus de son plancher avec T1, T3 et T4 établis (T4 avec le contrôle des coûts déjà déclarés), génériques non : information sur l'acte présente, que la direction générique ne prend pas (cas de [YS p. 3], où c'est une hypothèse). Oracle au-dessus sans T1 : il lit la consigne ou le contexte, pas l'acte ([KU p. 5] ; [AP p. 18]). T1 non calculable : non concluant. Oracle non au-dessus : « non détecté à cette puissance » ([P] l. 272-274), jamais « ne sépare pas », a fortiori jamais « pas de trace » | la position explique-t-elle le nul ? Lu sur le bras (a) seul ; sur T0.6, seulement sur la condition qui réplique P3 ((i-a), p = 1, intensité forte, brouillon de T0.6 l. 75, ou son équivalent dans T0.6 réécrit) ; (b) à (d) disent l'apport de chaque changement. Pour : hors domaine et à grande échelle [OA table 15 ; CA p. 7-8] ; mais faible à 2 milliards [CA p. 8]. Sur les cas proches, l'issue dépend des données d'apprentissage de la sonde : à consigne égale (sous-rendement), échec avec les sondes apprises sur « Roleplaying » [AP p. 9, p. 18 ; PAR table 3, sonde RP : 0,457 et 0,437], pas avec la recette « Pairs » de P3 (0,849 et 0,879 contre 0,964 en moyenne [PAR table 3]) ; entre consignes, séparation presque parfaite [AP p. 18] ; tromperie sur consigne : la question ne bat pas la moyenne [DYL p. 11 ; table 9 ; LB p. 8] ; sonde de question basse sur Qwen3-8B (0,69 ; moyenne 0,74) et Qwen3-4B (0,68 ; moyenne plus basse encore, 0,64) [DYL table 9, p. 28]. **Prédiction écrite d'avance** : sonde apprise sur « Roleplaying » : échec de T1 ; sondes principales de P3 : issue incertaine ([PAR] : 0,849 et 0,879 à consigne égale, sujet WMDP contre MMLU confondu) ; le nombre de l'action est dans le contexte lu, donc T1 ne vaut qu'avec T4 ; un bras au-dessus du plancher sans T1 lit la consigne, pas l'acte | une sonde apprise **sans l'organisme** détecte-t-elle ? Même domaine 0,85 contre 0,74 [K p. 5] ; données sur consigne, incitation gardée dans le contexte : peu de perte pour la tromperie (+0,035, non significatif), perte pour le sous-rendement (−0,111) ; la perte principale vient du domaine (−0,416) [K p. 3 ; table 1, p. 7] ; paires minimales du domaine [RH p. 27] | effet de taille ou de capacité [LB table 6] ? Par la taille, [CA] place la rupture entre 2 et 9 milliards, dans la famille Qwen3.5 (p. 8) ; Nemotron-3 Nano (30B-A3B) reste bas [CA p. 8 ; p. 25] ; [DYL] : mesuré contre un indice de capacité, pas contre la taille (p. 10), mensonge sur consigne seulement (p. 12) ; la place de Llama-3.1-8B en capacité n'est pas mesurée (R8 : question). L'organisme entraîné retire la fuite, mais les sondes y tombent [BX p. 8] ; chez [DYL], sur le seul organisme « Gender Secret », la sonde d'Apollo échoue déjà sur la version sur consigne ; la chute de la sonde « Did you lie? » est compatible avec un effet de l'affinage (p. 11) |
| **coût** | ≈ 1 à 1,5 h ; ≈ 1,5 à 2,5 USD ; données déjà payées ; (v) : passes en plus, à deviser | greffée sur E1, si tu étends N-028 : ≈ + 0,5 à 1 USD ; seule ≈ 1,5 à 2,5 USD ; sur des épisodes neufs : plus leur génération (voir E3) | ≈ 0,5 à 1 h, ≈ 1 à 2 USD de carte (greffable sur T0.7), **plus** l'écriture, la contre-lecture et le scellement de jeux neufs (plusieurs jours), **plus** la génération des épisodes d'évaluation neufs de T0.6, non devisée (à deviser : le brouillon actuel de T0.6 prévoit 1 536 + 640 épisodes ; la proposition P-015 en estime la réécriture en mode « coût » ; nœud de dépense possible au-delà de 10 USD par lancement) | deux cartes de 80 Go, ≈ 5 à 8 h, ≈ 10 à 20 USD ; au-delà de 10 USD par lancement (R-269) : nœud ; compte à recharge automatique (R-283) |
| **piège** | le champ `COST` **contient le chiffre** ; (i)-(ii) déjà vus : un « au-dessus » y serait suspect (R4), et le chercher viserait un signe déjà aperçu (R3) ; le préenregistrement déclare cette exposition (R1) ; l'oracle compare des **contextes différents** et peut lire la consigne ou les nombres déjà écrits ; peu d'actions non gonflées chez le saboteur (T1 peut être non calculable) ; la passe forcée retokenise : garde d'identité (jetons par action et scores des sondes légères égaux à `scores-p3.npz`, tolérance fixée, éprouvée sur cas sain et artefact, R5) ; rédiger sans lire les descriptifs A1 et A2 de l'addendum 1 (N-028), ni les valeurs de T1, T2 et T4 écrites dans le dépôt ([NB] notamment) | la question fait **relire la consigne** : la sonde lit une disposition, pas l'acte ; preuve directe, pour une sonde apprise sur « Roleplaying » : « every Sandbagging response is rated as highly deceptive – even when the model chooses not to sandbag » [AP p. 18] ; régime de consigne [KU p. 5] ; analogie boîte noire : [LIAR p. 9-10] ; le nombre de l'action et ceux des pas précédents sont dans le contexte lu | la sonde apprend « gros nombre », le style de textes écrits hors du modèle, ou le régime d'incitation s'il manque chez les négatifs | confondre taille et famille de modèle ; coût ; choisir le bras après lecture (malédiction du gagnant, R3) |
| **contrôle obligatoire** | P3-P4, T1, T3 (deux branches) et T4 sur chaque bras de production ; nombres avant le champ et coûts déjà déclarés : contrôle mécanique, puis (a), (b) ou (c) des règles communes ; oracle : témoin parmi les négatifs d'apprentissage, mention hors d'eux ; empan sans le champ `COST` ; plancher par permutation avec réapprentissage ; puis T3 (sur un oracle appris sans la mention), T1, T4 et le même contrôle des coûts déjà déclarés ; le témoin étant parmi les négatifs d'apprentissage, P3-P4 n'est pas un test pour l'oracle ; audit R4 (une aire d'oracle proche de 1 est une réserve) | P3-P4, T1, T3 complet, T4 avec le contrôle des coûts déjà déclarés, sur chaque bras de production ; sur T0.6 : témoin et mention à jouer (le brouillon actuel de T0.6, l. 74-81, n'a pas de mention : T3 n'y serait pas calculable) | nombres équilibrés ; incitation chez les positifs et les négatifs ; lecture avant le chiffre (au premier pas, ou appariée sur les coûts déjà déclarés ; actions sans nombre avant le champ) ; P3-P4, T1, T3 et T4 ; jamais les tâches d'évaluation (P-011) ; sur T0.6 : mention à jouer (voir E2) | mêmes contrôles ; même bras rejoué sur 8 milliards, épisodes neufs |

## 5. Recommandation, confiance, nœuds

**Recommandation.** (1) P4-instrument d'abord (R-262), après l'addendum 2 de P3. (2) Puis **E1 (P3b), lu comme diagnostic
de l'instrument** (option (a) du nœud « Revendication » ci-dessous) : bras du champ du coût non aveugles ; un lancement,
≈ 1,5 à 2,5 USD non devisés ; avec la manipulation du nombre si tu l'ajoutes (nœud ci-dessous). (3) **E2 pas sur les
actions de P3** : je recommande de la jouer sur les épisodes neufs de T0.6, à l'aveugle, avec la prédiction écrite de la
section 4 (nœud ci-dessous). (4) **E3 dans T0.7 réécrit en mode coût** (R-265 (6)), évaluée sur des épisodes neufs de T0.6 : voie
que je propose pour R-262 (2) : E3 peut porter une revendication, car la sonde est apprise sans l'organisme et lue en
production ; E2 sur épisodes neufs le peut aussi, si tu admets en production la lecture après une question (règle gelée
1). (5) **E4** seulement après E1 à E3 et après G0, bras fixé d'avance.

**Confiance** (jugement du correcteur ; revue depuis la v1, VV2-sens-09 et VV3-sens-09). ≈ 40 % (v1 : 60 %, pour E1
et E2 ensemble) que E1 dise d'où vient le nul (lecture ou direction ; un oracle non au-dessus ne dit pas « pas de
trace ») : les bras du champ sont déjà vus (T2), le bras « avant le champ » voit des nombres déjà écrits, et T1 n'y vaut
qu'avec T4. ≈ 15 à 25 % (v1 : 25 à 35 %) qu'une sonde apprise sans l'organisme passe le plancher **et** T1, T3 et T4 sur
ce modèle : T1 s'ajoute, à consigne égale, et rien de publié ne le passe sur un cas de ce type ; en sens contraire, le
montage corrigé lit des données du domaine, que [K] désigne comme le premier levier (« Deception −0.416 » hors domaine,
table 1, p. 7). L'oracle passera probablement son plancher, les contextes différant ; T1, T3 et T4 sont l'obstacle.

**Nœuds de Lazar.**
- **Revendication et voie de R-262 (2)** (proposition) : aucune lecture de P3b ne porte de revendication : bras du
  champ du coût non aveugles (T2 de la lecture décisive, [P] l. 242-247 ; valeurs écrites dans le dépôt, [NB]) ; oracle
  hors de l'anti-circularité de P-011 ; bras « moyenne » de diagnostic (N-026). Une revendication ne viendra que d'une
  lecture de production sur des épisodes neufs : E3, ou E2 si tu admets en production la lecture après une question
  (règle gelée 1). **Divergence à trancher** : N-028 lit P3b comme « la première
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
  porte la même limite : la session la complétera par une ligne nouvelle qui renvoie à N-028, sans réécrire la ligne
  d'une décision de Lazar.
- **E2 et manipulation du nombre sur les actions de P3** : extension de N-028 (activations, sondes et couches neuves ;
  [P] l. 415-416, l. 428 ; le GO de N-028 ne couvre que la localisation au champ du coût et l'oracle, `registres/go.md`
  l. 32). Options pour E2 : (a) étendre N-028, E2 greffée sur la passe de P3b (≈ + 0,5 à 1 USD) : réponse rapide, mais une
  lecture de plus sur des données déjà lues, et l'issue « consigne lue, pas l'acte » est prédite pour une sonde apprise sur « Roleplaying » [AP p. 18], pas pour la
  recette « Pairs » [PAR table 3] ; (b) E2
  sur les épisodes neufs de T0.6, à l'aveugle : plus tard ; (c) pas de E2 : le levier le plus cité resterait non éprouvé
  ici. Recommandation : (b), confiance ≈ 55 %. Manipulation du nombre : recommandation : l'ajouter à N-028 (toujours
  calculable, même passe ; elle sépare le nombre de l'action en cours de la consigne, historique des coûts gardé,
  section 4), contre la note du brainstorm qui la plaçait après le verdict de A1 et après G0 (l. 33) ; confiance ≈ 50 %
  (v3 : 60 %). Pas de défaut
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
  compte à recharge automatique (R-283). T0.6 réécrit en mode « coût » peut dépasser 10 USD par lancement
  (brouillon actuel : 1 536 + 640 épisodes ; P-015) : nœud de dépense possible. E4 (≈ 10 à 20 USD) : au-delà de 10 USD par lancement, nœud (R-269) ; de
  toute façon devis, GO, et GO de changement de modèle.
- **Concepts, couches, positions** (proposer avec recommandation, défaut 48 heures) : « gonflement d'estimation » ;
  position « avant le champ » ; couches multiples (dans T0.7 et sur des épisodes neufs seulement : sur les actions
  de P3, toute couche ou sonde neuve est un nœud, [P] l. 428) ; contrôle des coûts déjà déclarés pour la position « avant le champ »
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

## 6. Table des clés (empreintes vérifiées ce jour)

`[D]` = `/home/user/controle-ia-travail/docs/sources/pdf/` (compagnon `.sha256` égal) ; `[X]` = `…/revue-detection/extraction/` ;
`[N]` = `…/revue-detection/pdf-nouveaux/`. Empreintes complètes dans `citations-synthese-v1.json` (RO : ci-dessous).
Compagnons `.sha256` (R6) : présents pour `[D]` et pour MA ; absents pour les neuf autres PDF de `[X]` et `[N]`, dont les
empreintes, égales, sont dans `[X]pdf-representations/provenance-representations-v1.md` et
`[N]provenance-nouveaux-v1.md` : à créer avant tout versement au dépôt.

| clé | travail | PDF | sha256 |
|---|---|---|---|
| AP | Goldowsky-Dill et coll. (Apollo) | `[D]2502.03407v1.pdf` | `a4820ad5…` |
| PAR | Parrack et coll. | `[D]2507.12691v3.pdf` | `0c00a77b…` |
| OA | Taufeeque et coll. | `[D]2602.15515v2.pdf` | `f6547ec8…` |
| CA | Hollinsworth et coll. | `[D]2610.12445v1.pdf` | `7e141758…` |
| YS | Yoo et Skapars | `[D]2609.02893v1.pdf` | `b76151cd…` |
| BX | Boxo et coll. | `[D]2509.21344v2.pdf` | `aaac4ff9…` |
| AG | Taylor et coll. | `[D]2512.07810v1.pdf` | `77e64bcd…` |
| KU | Kumar | `[D]2605.27958v1.pdf` | `43f55118…` |
| MK | McKenzie et coll. | `[D]2506.10805v4.pdf` | `54bf5555…` |
| GM | Kramár et coll. | `[D]2601.11516v4.pdf` | `c4a36db5…` |
| EM | Sofroniew et coll. | `[D]2604.07729v1.pdf` | `afe70d72…` |
| MA | Marks et coll. | `[X]pdf-anthropic/2503.10965/2503.10965v2.pdf` | `6cea87ef…` |
| BU | Bürger et coll. | `[X]pdf-representations/2407.12831/2407.12831v2.pdf` | `badf34f0…` |
| LIAR | Pacchiardi et coll. | `[X]pdf-representations/2309.15840/2309.15840v1.pdf` | `a710a785…` |
| FQ | Farquhar et coll. | `[X]pdf-representations/2312.10029/2312.10029v2.pdf` | `8f8b5e7a…` |
| K | Kirch et coll. | `[N]2511.17408v4/2511.17408v4.pdf` | `91e00c25…` |
| LB | Kretschmar et coll. | `[N]2511.16035v2/2511.16035v2.pdf` | `cf3a615c…` |
| AU | Golechha et Garriga-Alonso | `[N]2504.04072v3/2504.04072v3.pdf` | `0231c2ba…` |
| DYL | Cooney et coll. | `[N]2606.12618v2/2606.12618v2.pdf` | `2eccf773…` |
| RH | Bergen et coll. (Goodfire) | `[N]2609.19101v2/2609.19101v2.pdf` | `c8ab5045…` |
| CC | Cunningham et coll. | `[N]2601.04603v1/2601.04603v1.pdf` | `ba8ec657…` |
| RO | Rose et coll. (mention de seconde main seulement) | `[D]2604.01151v3.pdf` | `bde99a620dbbb4064fcfd9a010ac4e92b17b619c5995ae0696911afdbed7686b` |

**Fichiers** (`…/revue-detection/redaction/`) : `verifier_citations_synthese.py` ; `construire_citations.py` et
`citations-synthese-v1.json` (119 citations) ; `sortie-citations-synthese-v1.txt` (toutes conformes) ;
`epreuve-r5-synthese-v1.json`, `epreuve-r5-empreinte-v1.json`, `sortie-epreuve-r5-synthese-v1.txt` (8 rejetés) ;
`recouper_guillemets.py` et `sortie-recoupement-v1.txt` (phrases du texte retrouvées sur leurs pages). Limites : chiffres
des auteurs non recalculés ; annexes non lues ; coûts non devisés ; classement et confiances = jugements du rédacteur.
v2 (`…/correcteur-tour1/`) : `appliquer_corrections_v2.py` (le différentiel, v1 → v2) ; `ctx.py` (phrase en contexte) ;
`recouper_v2.py` et `sortie-recoupement-v2.txt` (phrases anglaises de la v2 sur les pages des clés de leur bloc). v2 :
rangs, pouvoirs et confiances du rédacteur inchangés, sauf le pouvoir du rang 5 (VS-05). v3 (`…/correcteur-tour2/`) :
`outils/appliquer_corrections_v3.py` (le différentiel, v2 → v3, par plages de lignes) ; `outils/pg.py` (une phrase sur une
page) ; `outils/controler_v3.py` et `sortie-controle-v3.txt` (phrases et chiffres à la page exacte, épreuve R5) ;
`pages/` (texte des 22 PDF, page par page). v3 : pouvoirs des rangs 2 à 5 et confiances revus par le correcteur
(sections 3 et 5). v4 (`…/revue-detection/correction-tour3/`) : `appliquer_corrections_v4.py` (le différentiel, v3 → v4).
