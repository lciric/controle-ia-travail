# Vérification de la synthèse « comment détecter » — v1

- **Objet.** `…/revue-detection/synthese-comment-detecter-v1.md` (sha256 `a47f9141…`, compagnon égal).
  `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.
- **Vérificateur neuf.** Je n'ai écrit ni les extractions ni la synthèse. 2026-10-20. Dépôt lu seulement. Non ouverts :
  `prereg/P3-consignes-v1.md`, textes d'action, clés.
- **Méthode.** Je n'ai pas utilisé les scripts du rédacteur. Pour les 21 PDF de la table des clés : empreinte recalculée,
  puis texte extrait page par page (`pdftotext`, brut et mise en page) sous `…/revue-detection/verification/pages/<clé>/`.
  Chaque phrase, chaque chiffre et chaque montage cité a été cherché sur la page citée, puis lu dans son contexte.
  Outil de recherche : `…/revue-detection/verification/cherche.py`. Correspondance clé → PDF :
  `…/revue-detection/verification/cles.txt`.

## Verdict : **conforme après corrections**

- Les 21 PDF ont l'empreinte annoncée (8 premiers signes égaux ; empreinte complète égale au compagnon ou à la provenance).
- **Tous les chiffres cités sont sur la page citée** (aucun inexact, aucun introuvable).
- Mais plusieurs **lectures du sens** sont fausses ou incomplètes, deux **attributions** sont fausses, et un **contrôle
  d'expérience** est faux (VS-01 : le bras « avant le champ » voit les coûts gonflés des actions précédentes).
- 8 écarts majeurs (VS-01 à VS-08), 17 mineurs (VS-09 à VS-25). Aucun ne demande de retirer un chiffre ; deux demandent
  de retirer ou de marquer « non vérifié » une affirmation (VS-06, VS-07).

## Écarts

### Majeurs

**VS-01 — Le bras « avant le champ » voit le nombre (contrôle du nombre écrit).**
- Où : section 4, E1, ligne « contrôle obligatoire » (« le bras « avant le champ » ne voit pas le nombre (attention
  causale) ») ; section 5, « positions « avant le champ » ».
- Problème : vrai pour le nombre de l'action en cours seulement. À partir du deuxième pas, le contexte contient toutes les
  actions précédentes de l'agent, avec leur champ `COST` gonflé. Preuve dans le code du dépôt :
  `src/controle_ia/harnais/episode.py` (`79113b49…`) l. 217 (`contextes.append(trs[b][i].ids + fmt.tour(...))`) et
  l. 254 (`trs[b][i].ids = ctx + nv + fmt.cloture(...)`). Le contexte contient aussi la consigne privée (fin du message
  système) et l'indication avant « Your action: » (`environnements/propositions.py` `5d97b223…` l. 238-268).
  Code actuel du dépôt ; à confirmer au commit du run de P3.
- Correction : T4 pour ce bras doit tenir compte des coûts déjà déclarés dans le contexte. Options à préenregistrer :
  (a) bras restreint au premier pas de chaque épisode ; (b) appariement ou stratification sur les coûts déclarés aux pas
  précédents ; (c) les deux. Écrire « ne voit pas le nombre de l'action en cours ; voit ceux des pas précédents ».

**VS-02 — « Le maximum perd » : vrai pour une seule des deux sondes d'Apollo.**
- Où : section 2.2 « Ailleurs » (« le maximum perd (0,839 contre 0,964, [PAR table 3]) ») ; section 3, rang 7.
- Problème : [PAR] table 3, p. 7, colonne Sandbagging. Sonde « Pairs » : « Full Averaging (Pairs) … 0.964 » ;
  « Peak Activation (Pairs) … 0.839 ». Mais sonde « RP » (jeux de rôle) : « Full Averaging (RP) … 0.828 » ;
  « Peak Activation (RP) … 0.891 ». Moyenne des cinq jeux : RP maximum 0,856 contre moyenne 0,840. Le maximum gagne donc
  avec la sonde RP, sur le sous-rendement et en moyenne.
- Correction : citer les deux lignes. « Sur la recette d'Apollo, le maximum perd avec la sonde Pairs (0,839 contre 0,964)
  mais gagne avec la sonde RP (0,891 contre 0,828 ; moyenne 0,856 contre 0,840) [PAR table 3, p. 7]. » Cela renforce
  « sens inconnu » (rang 7).

**VS-03 — McKenzie lu à contresens ; dernier jeton omis.**
- Où : section 2.2 (« le maximum « biases probes towards the most high-stakes token » [MK p. 4] ») ; section 3, rang 4
  (« maximum tiré par le jeton extrême [MK p. 4 ; CC p. 6] ») ; section 1, point 1.
- Problème : [MK] p. 4 explique pourquoi le maximum **marche bien** sur MTS : « the Max and Max of Rolling Means probes
  perform relatively well on the MTS dataset, nearly matching the performance of the more consistent probes. Taking the
  maximum over per-token predictions biases probes towards the most high-stakes token in a response; this may indicate that
  the high-stakes nature of the MTS dataset is dependent upon specific words, enabling these probes to achieve better
  performance. » Ce n'est pas un défaut : c'est l'argument pour un concept porté par peu de jetons, comme le champ `COST`.
  Omis, même page : « Whilst the Last Token activation probe consistently performs poorly ». Cela contredit en partie le
  point 1 de la section 1 (« une seule position de synthèse »).
- Correction : rang 4 et section 2.2 : « le maximum suit le jeton le plus marqué ; il marche quand le concept tient à des
  mots précis [MK p. 4] ». Retirer [MK] de « maximum tiré par le jeton extrême » (garder [CC p. 6]). Section 1, point 1 :
  « une seule position **après une question ajoutée** » ; le dernier jeton seul échoue sur les enjeux [MK p. 4] et est
  seulement « comparable » chez Apollo [AP p. 23].

**VS-04 — « Aucun attaquant entraîné contre la sonde » : faux pour [OA].**
- Où : section 2.2, « Pour P3 » (« Aucun de ces travaux n'a d'attaquant entraîné contre la sonde »).
- Problème : [OA] p. 1 : « Training against white-box deception detectors has been proposed […] We construct a realistic
  coding environment […] and show that obfuscation emerges in this setting. » La sonde attaquée lit une seule position
  après une question (« Did you respond truthfully? », p. 5). [GM] teste aussi des attaques adaptatives par invite
  (p. 10, « Adaptive Red Teaming »). Aucun ne compare maximum et moyenne sous attaque : la raison de la règle gelée reste
  non testée.
- Correction : « Aucun de ces travaux ne compare les agrégations sous un attaquant entraîné. [OA] entraîne des politiques
  contre une sonde lue à une seule position après une question et y observe l'évasion (p. 1). » À reporter au nœud
  « Règle gelée 1 » de la section 5 : c'est le seul résultat lu sur la robustesse de la lecture à une seule position (E2).

**VS-05 — L'effet de taille n'explique pas un nul à 8 milliards d'après [CA] ; [DYL] parle de capacité.**
- Où : section 1, point 1 ; section 3, rang 5 ; section 4, E2 « tranche » et E4.
- Problème : [CA] situe la rupture entre 2 et 9 milliards, pas entre 8 et 27. Page 8, légende de la figure 4 : « Every
  probe improves from the smallest model of each family, and scores exceed 90% from there up » ; le plus petit Qwen3.5
  est 2B, le suivant 9B (figure 4b : SHADE-Arena). Page 9, sur la censure politique : « From Qwen3.5-9B to
  Qwen3.5-397B-A17B and Kimi K3, all four probes have AUC ≥ 98% ».
  Le « 0,963–0,986 dès 27B » cité omet 9B. [DYL] p. 10 corrèle la performance à un indice de **capacité** (« correlates
  positively and significantly with the Artificial Analysis Intelligence Index »), pas à la taille ; table 9, p. 28 :
  « Qwen/Qwen3.5-4B … 0.89 » (sonde d'Apollo) contre « Qwen/Qwen3-8B … 0.74 ».
- Correction : rang 5 : « [CA] : faible à 2 milliards (0,585 à 0,781), au-dessus de 0,90 dès 9 milliards (p. 8, p. 9) ;
  [DYL] : capacité, pas taille (p. 10). Pouvoir d'expliquer le nul de P3 : **faible** d'après [CA], moyen d'après [DYL]. »
  E2 « faible sur petits modèles » : préciser « 2 milliards [CA p. 8] ». E4 : l'argument de taille est affaibli.

**VS-06 — [AG] n'est pas un travail d'Anthropic ; Oak est confondu ; la p. 43 est une hypothèse.**
- Où : section 2.1, ligne [AG] (« Jeux d'audit, coauteurs Anthropic ») ; paragraphe « Ce qu'a fait Anthropic » (« les
  sondes de ses coauteurs échouent [AG p. 17, p. 43]. P3 ressemble à Oak. ») ; section 3, rang 3.
- Problème : [AG] p. 1 : affiliations « 1 UK AI Security Institute, 2 FAR.AI, 3 Anthropic » ; un seul auteur
  d'Anthropic (Samuel Marks). Table 2, p. 7 : Cedar et Oak sont des **Llama-3.3-70B-Instruct**, et Oak « Also has the
  same distractor behaviours as Baobab ». Page 17 : « Oak's final-layer probe had an uninterpretable firing pattern » ;
  distracteurs qui « successfully caused many spurious probe activations ». Page 43 : la phrase « the model does not need to
  say false facts… » est la **motivation de l'équipe rouge** (« White-box detection via probes was expected to struggle
  […] because the model does not need to say false facts »), pas un résultat.
- Correction : sortir [AG] du paragraphe « Ce qu'a fait Anthropic » ; écrire « UK AI Security Institute, avec FAR.AI et un
  coauteur d'Anthropic (p. 1) ». Ligne [AG] : ajouter « 70 milliards ; Oak porte aussi des comportements distracteurs
  (table 2, p. 7 ; p. 17) ». La p. 43 : « hypothèse de l'équipe rouge », pas une cause établie.

**VS-07 — « Ce qu'a fait Anthropic » : porte dérobée non vérifiée ; travaux d'Anthropic omis.**
- Où : section 2.1, paragraphe « Ce qu'a fait Anthropic » (« Ses succès internes portent sur des organismes entraînés
  (porte dérobée, objectif appris) … [MA p. 1, p. 16-17] »).
- Problème : (1) le succès sur « porte dérobée » vient du billet « Simple probes can catch sleeper agents », que la
  synthèse dit elle-même **non vérifié**. [MA] ne le porte pas. Seules des mentions de seconde main sont sur PDF vérifié :
  [BX] p. 3 (« in (Anthropic, 2024) they demonstrated that simple contrastive pair probes were capable of classifying
  prompts that would induce defection ») ; `docs/sources/pdf/2604.01151v3.pdf` (`bde99a62…`) p. 3 (« Anthropic (2024)
  show that simple “defection probes” reliably catch sleeper agents »). (2) [CC] est d'Anthropic (p. 1 : « All authors
  are at Anthropic ») : c'est son travail de sondes **en production**. Il lit toutes les couches (p. 8 : « Our default
  probe uses all layers ») et lisse les scores sur une fenêtre de jetons (p. 6). [EM] est aussi d'Anthropic (p. 1), sur
  Claude Sonnet 4.5.
- Correction : « porte dérobée (billet, **non vérifié** ; mentions de seconde main : [BX p. 3], 2604.01151v3 p. 3) ».
  Ajouter au paragraphe : « en production, Anthropic lit toutes les couches et lisse le score sur une fenêtre de jetons
  [CC p. 1, p. 6, p. 8] ».

**VS-08 — [DYL] : la chute de la sonde d'Apollo n'est pas due à l'entraînement de l'organisme.**
- Où : section 4, E4 « tranche » (« L'organisme entraîné retire la fuite, mais les sondes y tombent [BX p. 8 ; DYL
  p. 11] ») ; section 2.1, ligne [DYL].
- Problème : [DYL] p. 11 : « Apollo and Unrelated Questions perform poorly even on the prompted variants, with balanced
  accuracy near chance […] suggesting these detectors do not generalise well to this style of behaviour. DYL, by contrast,
  retains strong performance on the prompted variants ». Pour la sonde d'Apollo, la chute suit le **type de comportement**,
  pas l'entraînement.
- Correction : « chez [DYL], seule la sonde « Did you lie? » chute à cause de l'entraînement ; la sonde d'Apollo échoue
  déjà sur la version sur consigne (p. 11) ». Ligne [DYL] : remplacer « taille du modèle » par « capacité du modèle »
  (voir VS-05).

### Mineurs

**VS-09 — [BU] : autre modèle ; 93,8 % vient de leur méthode, pas d'une régression logistique.**
- Où : section 2.1, ligne [BU] ; section 3, rang 5 et rang 6 (« 12 et 14 sur ce modèle [BU p. 5 ; BX p. 3] »).
- Problème : [BU] p. 5 : « For LLaMA3-8B we choose layer 12 » : Llama-3, pas Llama-3.1. Page 10 : « TTPD correctly
  classifies the 49 unambiguous lies and the 55 unambiguous truthful replies with an average accuracy of 93.8 ± 1.5%,
  followed by MM with 90.5 ± 1.5%, LR with 79 ± 8% accuracy ».
- Correction : rang 6 : « 12 sur Llama-3-8B [BU p. 5], 14 sur ce modèle [BX p. 3] ». Ligne [BU] : « méthode TTPD ;
  régression logistique 79 ± 8 % ; 104 réponses (p. 10) ».

**VS-10 — [YS] : agrégation par moyenne, sonde des auteurs, fuite possible.**
- Où : section 1, point 2 ; section 2.1, ligne [YS] ; E1 « tranche ».
- Problème : [YS] p. 3 : « average token activations over just the assistant's response » (moyenne sur les jetons) ;
  0,869 est obtenu « within this subspace using 5-fold cross-validation » (100 composantes de la source). La sonde est
  entraînée par les auteurs sur le jeu « Roleplaying » d'Apollo (p. 2), ce n'est pas la sonde d'Apollo. Le protocole de
  sous-rendement d'Apollo fait raisonner le modèle par écrit sur sa décision ([AP] p. 5 : « If sandbagging, make up a
  plausible but incorrect alternative answer »). [YS] ne dit pas exclure ce raisonnement. 0,869 peut donc lire du texte.
  Les chiffres comparés en section 1 ([BX], [YS], [AP]) sont tous en moyenne ; P3 est en maximum ou attention.
- Correction : « sonde des auteurs sur le jeu de jeux de rôle d'Apollo ; activations moyennées sur la réponse ;
  raisonnement écrit possiblement inclus (non dit) ». Section 1, point 2 : « montages en moyenne, P3 en maximum ».
  Garder l'inférence « l'information est là » comme hypothèse.

**VS-11 — [AP] : couche choisie sur un jeu d'évaluation ; « réponses imposées » = entraînement.**
- Où : section 2.1, ligne [AP] ; section 3, rang 6 (« choix hors entraînement [AP p. 21] »).
- Problème : [AP] p. 21 : « Layer 22 was chosen for best performance on the Roleplaying dataset when testing on Llama
  3.1 ». « Roleplaying » est aussi un jeu d'évaluation : ce n'est pas un jeu de validation tenu à part. Même page :
  « indicating the importance of representative-validation sets ». Page 4 : « these responses are not written by the model
  and contain no actual deception » porte sur le jeu d'**entraînement**.
- Correction : « couche choisie sur un des jeux d'évaluation (Roleplaying, avec Llama 3.1) (p. 21) » ; « entraînement :
  réponses imposées, sans tromperie réelle (p. 4) ; évaluation sur réponses du modèle (p. 4) ».

**VS-12 — [AP] : nuances d'agrégation à ajouter (N-026).**
- Où : section 2.2, premier et deuxième points.
- Problème : ce qui est écrit est conforme. Il manque trois précisions, toutes sur PDF. Page 22 : la moyenne seuillée,
  pour la sonde Instructed-Pairs, « the best values for the Instructed-Pairs probe are so small the method is equivalent to
  mean ». Page 23 : le dernier jeton seul est testé sur une sonde **Roleplaying réentraînée** sur les dernières positions,
  et « Recall at 1% FPR compared to control does show improvement ». Page 7 : « the probe detects the responses as
  deceptive before any explicitly deceptive text is generated », ce qui est utile au bras « avant le champ ».
- Correction : ajouter ces trois phrases, avec leurs pages.

**VS-13 — [K] : « consigne seule insuffisante » va plus loin que la table.**
- Où : section 4, E3 « tranche » (« consigne seule insuffisante [K p. 9] ») ; section 3, rang 2.
- Problème : [K] table 1, p. 7, colonne « Prompted » : « Deception … +0.035 » (non significatif), « Sandbagging …
  −0.111* ». La grande perte vient du **domaine** (« Deception −0.416*** »). La phrase de la p. 9 est une interprétation
  (« suggesting that stated intent does not produce the same activation signatures… ») sur les jeux à raisonnement privé.
- Correction : « données sur consigne : peu de perte pour la tromperie (+0,035), perte pour le sous-rendement (−0,111),
  [K table 1, p. 7] ; la perte principale vient du domaine ».

**VS-14 — [FQ] porte sur les méthodes non supervisées.**
- Où : section 3, rang 2 (« la méthode suit le trait « most prominent » [FQ p. 1] »).
- Problème : [FQ] p. 1 : « existing unsupervised methods on large language model (LLM) activations do not discover
  knowledge – instead they seem to discover whatever feature of the activations is most prominent ». Les sondes de P3 sont
  supervisées.
- Correction : « les méthodes **non supervisées** suivent le trait le plus saillant [FQ p. 1] ; transposition aux sondes
  supervisées : analogie du rédacteur ».

**VS-15 — [LIAR] est un détecteur boîte noire.**
- Où : section 3, rang 9 ; E2 « piège ».
- Problème : [LIAR] p. 1, titre : « Lie Detection in Black-Box LLMs by Asking Unrelated Questions ». La « disposition »
  (p. 10) est lue par des questions de suivi, pas par une sonde interne.
- Correction : ajouter « (détecteur boîte noire, par questions de suivi) » ; l'application aux sondes est une analogie.

**VS-16 — [GM] : « prevents dilution » décrit MultiMax ; la table 3 manque.**
- Où : section 2.2 (« Mais le maximum « prevents dilution… » [GM p. 7] »).
- Problème : [GM] p. 7 : « Unlike attention probes, MultiMax selects the single highest-scoring token per head rather than
  computing a weighted average, which prevents dilution… » : un maximum appris par tête, pas le maximum brut. Omis : table 3,
  p. 12, colonne « LC[A] » (« long context attacks », table 1, p. 8), taux de faux négatifs : « Linear Probe Mean »
  99.13% ; « Attn » 87.88% ; variantes MultiMax ou glissantes de 0.0% à 1.73%. C'est la preuve la plus directe de la
  dilution par la moyenne. Elle touche aussi l'attention simple, permise en production.
- Correction : « le maximum appris par tête (MultiMax) évite la dilution [GM p. 7] ; en contexte long, la sonde linéaire
  en moyenne manque 99,13 % des attaques et l'attention simple 87,88 % [GM table 3, p. 12] ».

**VS-17 — Le score lissé de [CC] est une moyenne glissante.**
- Où : section 5, « Règle gelée 1 » (« le score lissé avant le maximum [CC p. 6] ne sont ni « maximum ou attention » ni
  « moyenne ou médiane » »).
- Problème : [CC] p. 6, équation 2 : moyenne des logits sur une fenêtre de M jetons (« z̄t is the averaged logit at
  position t ») ; à l'inférence, « an exponential moving average (EMA) instead of a sliding window mean ». C'est une
  moyenne sur des jetons, dans une fenêtre.
- Correction : « moyenne glissante sur M jetons, puis maximum : relève au moins en partie de la règle ; à trancher par
  Lazar ».

**VS-18 — [AU] : les chiffres sont dans une figure ; contexte incomplet.**
- Où : section 2.1, ligne [AU] ; en-tête, R7 (« Aucun chiffre lu sur un tracé »).
- Problème : 0,653 et 0,948 sont des légendes imprimées de la figure 6, p. 6 (« (a) Probes on all actions (77% of these
  are non-speech actions) »). Même figure, (b), actions de parole : « Action (AUC = 0.984) ». Étiquette : rôle d'imposteur
  (« very correlated with the 'Impostor' label »). Sonde entraînée sur RepEng, couche 20 (p. 6-7).
- Correction : en-tête : « aucun chiffre lu sur un tracé ; [AU] : légendes imprimées de la figure 6 ». Ligne [AU] : « toutes
  actions, 77 % sans parole : 0,653 ; actions de parole seules : 0,984 ; étiquette = rôle ».

**VS-19 — Dépense : délégation à jour.**
- Où : section 5, « Dépense » ; section 4, E4 « coût ».
- Problème : R-217 était bornée au mandat. R-269 (GO-2026-10-20-07, `registres/decisions.md` l. 461 ;
  `registres/go.md` l. 34) l'étend au 30 novembre, avec un **plafond de 10 USD par lancement**. Le crédit de 11,79 USD est
  la lecture de 06:07 UTC (`registres/depenses.md` l. 89) ; une recharge d'environ 20 USD est prévue (GO-2026-10-20-06,
  `registres/go.md` l. 33).
- Correction : citer R-269 et le plafond de 10 USD ; E4 (10 à 20 USD) dépasse ce plafond : nœud.

**VS-20 — FIBS : publication peut-être déjà faite.**
- Où : section 5, « Contact externe ».
- Problème : [CA] p. 1 : « We release our training dataset, dubbed FIBS » et une adresse
  `github.com/AlignmentResearch/caught-in-the-act-probes`. Page 11 : « Upon publication, we will release our dataset,
  FIBS, and our trained probes ». Le papier se contredit. Disponibilité **non vérifiée**.
- Correction : vérifier d'abord si l'adresse est publique. Si c'est le cas, une lecture n'est pas un contact externe
  (licence à lire). Sinon, nœud de contact.

**VS-21 — E3 et l'oracle : agrégation non dite.**
- Où : section 4, E1 (oracle) et E3.
- Problème : E3 est dit « seule voie qui peut porter une revendication ». Son agrégation n'est pas écrite : elle doit être
  le maximum ou l'attention (production), ou attendre la décision de Lazar sur la lecture à une seule position. L'oracle
  n'a pas d'agrégation écrite non plus. Si elle copie [YS] (moyenne), les conditions de N-026 s'appliquent : bras nommé,
  plancher de même agrégation, bras de production lu à côté.
- Correction : écrire l'agrégation de chaque bras dans la liste fermée.

**VS-22 — [BX] : réserves des auteurs omises.**
- Où : section 1, point 2 ; section 2.1, ligne [BX].
- Problème : [BX] p. 8 : sondes **réentraînées** sur l'organisme (« re-training probes on the Model Organism using
  contrastive pairs ») ; limite : « The models may not have fully internalized the target behaviors, which could partly
  explain poor probe performance ».
- Correction : ajouter ces deux phrases à la ligne [BX].

**VS-23 — Renvois internes inexacts.**
- Où : section 3, rangs 4 et 10.
- Problème : « environ 33 » est en section 7 du verdict (`docs/verdicts/verdict-P3-premier-test-i-a-v1.md` l. 345), pas
  en section 4 (0,8878 y est bien, l. 204). « Cinq champs » n'est pas dans [P] l. 198-205 ; les champs viennent de
  `src/controle_ia/environnements/propositions.py` l. 184-186 (TITLE, PROPOSAL, CONTROLS, COST, PREDICTION).
- Correction : corriger les deux renvois.

**VS-24 — Ambiguïté de « pas ».**
- Où : section 2.1, ligne [CA] (« négatifs : pas d'avant le sabotage, même épisode »).
- Problème : « pas » peut se lire comme une négation. [CA] p. 6 : « its earlier steps and every step of an honest episode
  are the negative class ». Le sens voulu est juste.
- Correction : « négatifs : étapes d'avant le sabotage, dans le même épisode ».

**VS-25 — Empreintes compagnons (R6).**
- Où : section 6.
- Problème : les PDF du bloc-notes n'ont pas de compagnon `.sha256` (sauf [MA]). Leurs empreintes sont dans les fichiers
  de provenance, et elles sont égales.
- Correction : ajouter les compagnons avant tout versement au dépôt.

## Règles des expériences proposées

- **Préenregistrement (R1, R2)** : exigé pour chaque bras, avant toute lecture. Conforme.
- **Pas de moyenne sur les jetons en production (règle gelée 1, N-026)** : conforme pour E1 (bras de diagnostic nommé,
  plancher de même agrégation, bras de production à côté). À compléter : E3 et l'oracle (VS-21), score lissé (VS-17),
  lecture à une seule position (nœud déjà posé ; ajouter [OA], VS-04).
- **Contrôle du nombre écrit (T4)** : présent sur chaque bras. **Faux pour le bras « avant le champ »** (VS-01).
  Pour T4 « à coût déclaré égal », écrire aussi la part d'actions du saboteur qui recouvre les coûts honnêtes : si elle
  est trop petite, T4 n'est pas calculable (même risque que T1, déjà écrit).
- **Anti-circularité (P-011)** : respectée (oracle sans revendication ; E3 sur les tâches de réserve).
- **Dépense** : estimations non devisées, dites comme telles. Délégation à mettre à jour (VS-19).

## Conforme (vérifié sur la page citée)

[BX] p. 1, 3, 5, 8 ; [YS] p. 3 ; [BU] p. 5, 10 ; [AP] p. 3, 4, 6, 8, 10, 21, 22, 23, 35 ; [PAR] p. 5-8, table 3 ;
[KU] p. 4, table 7 p. 6, p. 9 ; [LB] p. 8, 10, table 6 p. 54 ; [DYL] p. 2, 8, 11, table 9 p. 28 ; [CA] p. 4-9, 11 ;
[OA] p. 5, table 15 p. 23 ; [AG] p. 16, 17, 43 ; [AU] p. 6 ; [K] p. 3, 5, table 1 p. 7, p. 9 ; [MA] p. 1, 3, 16, 17 ;
[MK] p. 4 ; [GM] p. 7, 11 ; [CC] p. 6, 8 ; [EM] p. 38 ; [RH] p. 9, table 4 p. 27 ; [LIAR] p. 9-10 ; [FQ] p. 1, 3.
Chiffres : tous égaux au PDF. Renvois internes au dépôt : [P] l. 289-301, 318, 320-321, 330-332, 385 ; [V] sections 2 et
3 ; `registres/depenses.md` l. 88 ; R-262, R-265 (1) et (6), N-028, P-011 (concept 4, licence), note de confrontation
(leçon 2) : conformes.

## Limites

- Les extractions n'ont pas été auditées ligne à ligne, seulement là où la synthèse s'en sert.
- Annexes des PDF lues seulement aux pages citées.
- Le code cité en VS-01 est celui du dépôt aujourd'hui ; son identité avec le commit du run de P3 n'est pas vérifiée.
- Aucun chiffre n'a été recalculé à partir des données des auteurs.
