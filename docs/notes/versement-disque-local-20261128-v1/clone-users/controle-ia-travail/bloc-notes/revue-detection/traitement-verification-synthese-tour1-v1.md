# Traitement de la vérification de la synthèse « comment détecter » — tour 1, v1

- **Correcteur neuf.** Je n'ai écrit ni la v1, ni les extractions, ni la vérification. 2026-10-20, vers 10:50 UTC.
  Dépôt lu seulement (aucune écriture, aucune commande git qui écrive). Non ouverts : `prereg/P3-consignes-v1.md`, textes
  d'action, clés. Aucune recherche web, aucun service payant, aucun contact.
- **Entrées.** Synthèse v1 `…/revue-detection/synthese-comment-detecter-v1.md` (`a47f9141…`, compagnon égal, non
  modifiée) ; rapport `…/revue-detection/verification-synthese-v1.md` (`43986648…`, compagnon égal).
  `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.
- **Sortie.** `…/revue-detection/synthese-comment-detecter-v2.md` (empreinte dans son compagnon `.sha256`).
- **Méthode.** Empreintes des 21 PDF de la table des clés recalculées : toutes égales. Pour chaque écart, page citée relue
  par `…/revue-detection/verification/cherche.py` et `…/correcteur-tour1/ctx.py` (même normalisation, avec le contexte).
  PDF hors table (2604.01151v3) : empreinte `bde99a62…` égale à son compagnon, page 3 extraite par `pdftotext`.
  Différentiel appliqué par script, chaque ancien passage présent une seule fois (`…/correcteur-tour1/appliquer_corrections_v2.py`).
  Toutes les phrases entre guillemets de la v2 recoupées sur les pages des clés de leur bloc
  (`…/correcteur-tour1/recouper_v2.py`, sortie `…/correcteur-tour1/sortie-recoupement-v2.txt`) : 123 phrases ; 103 trouvées à
  la page citée ; 20 non trouvées, toutes françaises (« avant le champ », « tromperie »…), tirées du code (« Your action: »)
  ou titre du billet non vérifié (« Simple probes can catch sleeper agents »).

## Verdict

**25 écarts traités : 15 acceptés, 10 acceptés en partie, 0 rejeté.** Aucun chiffre retiré. VS-01 confirmé au code du run
de P3 (identique aux deux commits). Trois corrections du rapport lui-même : plage des moyennes glissantes de [GM] (1,73 % à
5,19 %, pas « jusqu'à 1,73 % ») ; « en production » de [CC] ramené à ce que dit la page 2 ; [DYL] borné à l'organisme
« Gender Secret ».

## VS-01 : confirmation au code

- `git show 7a54d431d89745839220f882b41b13e8c62ecfdd:src/controle_ia/harnais/episode.py` et `git show 97dd829:…` :
  même empreinte `79113b4973d6…`, égale au fichier du dépôt aujourd'hui. Idem `environnements/propositions.py` :
  `5d97b223206c…` aux deux commits et aujourd'hui.
- `episode.py` l. 210-217 : au pas 0, contexte = ouverture (consigne privée, observation) ; aux pas suivants, contexte =
  `trs[b][i].ids + fmt.tour(...)` (l. 217). L. 254 : `trs[b][i].ids = ctx + nv + fmt.cloture(...)` : les jetons générés de
  chaque action restent dans la transcription. Les activations lues viennent d'une passe unique sur `tr.ids` (l. 260).
- `propositions.py` l. 251-269 : l'observation ajoute le texte complet des actions des **autres** agents depuis la dernière
  action de l'agent (l. 259-264), l'index des titres (sans coût) et l'indication privée avant « Your action: ».
- P3 : N = 1, T = 10, 60 tâches, quatre conditions, un épisode par tâche et condition ([P] l. 318). Donc pas d'actions
  d'autres agents ; mais dès le deuxième pas, le contexte contient les actions précédentes de l'agent, champ `COST`
  compris. Au premier pas, aucun coût déclaré dans le contexte ; 60 actions par condition.
- Conséquence écrite dans la v2 : règle commune « Nombre déjà écrit dans le contexte » (section 4), options (a) premier pas,
  (b) appariement ou strates sur les coûts déjà déclarés, (c) les deux ; aucune n'est choisie. Le choix va avec la
  proposition des positions (section 5, « proposer avec recommandation »), pas à ma place.

## Table

| écart | décision | raison (page relue) | où dans la v2 |
|---|---|---|---|
| VS-01 | acceptée | Code confirmé aux commits `7a54d43` et `97dd829` (ci-dessus). N = 1 : pas d'autres agents, mais actions précédentes avec `COST` dès le pas 2. Ajouté : effectifs du premier pas (60 par condition, [P] l. 318), seuil de 10 actions ([P] l. 238-253), risque de recouvrement (rapport d'environ 33, [V] l. 345), et la remarque T4 de la section « Règles » du rapport. Étendu aux autres lectures concernées (oracle, E2, E3), comme demandé. | section 4 : règles communes l. 146-159 ; E1 piège et contrôle l. 168-169 ; E2 piège et contrôle l. 168-169 ; E3 contrôle l. 169 ; section 5, positions l. 197-199 |
| VS-02 | acceptée | [PAR] table 3, p. 7 : Pairs 0,964 / 0,839 ; RP 0,828 / 0,891 ; moyenne des cinq jeux RP 0,840 / 0,856. Ajout « sonde Pairs » à la ligne [PAR] de 2.1, pour que 2.1 porte les chiffres repris (règle de l'en-tête). | 2.1 ligne [PAR] l. 47 ; 2.2 « Ailleurs » l. 98-100 ; rang 7 l. 132 |
| VS-03 | acceptée en partie | [MK] p. 4 : « Taking the maximum … biases probes towards the most high-stakes token » explique pourquoi le maximum marche sur MTS ; « the Last Token activation probe consistently performs poorly » : confirmé. Point 1 de la section 1 réécrit « après une question ajoutée » ; « fin d'énoncé » retiré du point 1 mais gardé au rang 4 avec sa borne ([BU], mensonges verbaux, TTPD). [MK] retiré de « jeton extrême », [CC p. 6] gardé. | section 1, point 1 l. 23-27 ; 2.2 « Ailleurs » l. 100-103 ; rang 4 l. 129 |
| VS-04 | acceptée en partie | [OA] p. 1 : « show that obfuscation emerges in this setting » ; même page : « Sufficiently high KL regularization and detector penalty can yield honest policies » (ajouté, pour ne pas surcharger). Sonde attaquée lue après une question (p. 5). [GM] p. 10 : l'attaque « adaptative » finale est une réécriture en une fois par Gemini 2.5 Pro, pas un entraînement contre la sonde : écrit tel quel. Phrase de la règle reformulée : aucun ne compare les agrégations sous un attaquant entraîné. | 2.2 « Pour P3 » l. 111-118 ; section 5, règle gelée 1 l. 185-189 |
| VS-05 | acceptée | [CA] p. 8 : « scores exceed 90% from there up » ; modèles Qwen3.5 : 2B, 9B, 27B, 122B-A10B, 397B-A17B (p. 18, p. 42) ; p. 9 : « From Qwen3.5-9B … all four probes have AUC ≥ 98% ». [DYL] p. 10 : capacité ; table 9, p. 28 : Qwen3.5-4B 0,89 contre Qwen3-8B 0,74. Pouvoir du rang 5 : faible d'après [CA], moyen d'après [DYL]. Le seuil de [CA] est mesuré sur Qwen et Nemotron, pas sur Llama : écrit « d'après [CA] ». | section 1, point 1 l. 25 ; 2.1 lignes [CA] l. 51 et [DYL] l. 50 ; rang 5 l. 130 ; E2 et E4 tranche l. 166 |
| VS-06 | acceptée | [AG] p. 1 : « UK AI Security Institute, FAR.AI, Anthropic », un auteur d'Anthropic (Samuel Marks). Table 2, p. 7 : Cedar et Oak sont des Llama-3.3-70B-Instruct ; Oak « Also has the same distractor behaviours as Baobab ». P. 17 : sonde de dernière couche illisible, distracteurs. P. 43 : la phrase est la « Motivation » de l'équipe rouge (elle cite aussi la difficulté d'agréger sur de longs contextes d'agent). [AG] sorti du paragraphe Anthropic, placé « Hors d'Anthropic ». | 2.1 ligne [AG] l. 53 ; paragraphe « Ce qu'a fait Anthropic » l. 63-77 ; rang 3 l. 128 |
| VS-07 | acceptée en partie | (1) Porte dérobée marquée non vérifiée ; [BX] p. 3 et 2604.01151v3 p. 3 confirmés ; clé RO ajoutée à la table (empreinte complète). (2) [CC] p. 1 « All authors are at Anthropic », p. 6 lissage, p. 8 « Our default probe uses all layers » : confirmés. Mais « en production » n'est pas écrit tel quel : p. 2 parle d'un système « production-grade » éprouvé en « shadow deployment on production traffic » ; la phrase de p. 5 (« guard Claude Opus 4 ») porte sur un classifieur en deux étages, pas sur la sonde : non utilisée. [EM] d'Anthropic (p. 1), Claude Sonnet 4.5 : ajouté. | paragraphe « Ce qu'a fait Anthropic » l. 63-70 ; section 6, ligne RO l. 241 |
| VS-08 | acceptée en partie | [DYL] p. 11 confirmé. Mais l'épreuve sur consigne ne porte que sur l'organisme « Gender Secret » (« we re-ran the evaluation against prompted Gender Secret model organisms ») : la v2 borne la phrase à cet organisme. « Taille » remplacé par « capacité » (VS-05). | 2.1 ligne [DYL] l. 50 ; E4 tranche l. 166 |
| VS-09 | acceptée | [BU] p. 5 « For LLaMA3-8B we choose layer 12 » ; p. 10 : TTPD 93,8 ± 1,5 %, « LR with 79 ± 8% accuracy », 49 mensonges et 55 réponses vraies. | 2.1 ligne [BU] l. 45 ; rangs 4, 5, 6 l. 129-131 |
| VS-10 | acceptée | [YS] p. 3 « average token activations over just the assistant's response » ; 0,869 dans les 100 composantes de la source, validation croisée à cinq plis ; p. 2 : sonde des auteurs, source « Roleplaying ». [AP] p. 5 : le protocole de sous-rendement fait écrire le raisonnement ; [YS] ne dit pas l'exclure. « L'information est là » gardée comme hypothèse. | section 1, point 2 l. 28-32 ; 2.1 ligne [YS] l. 44 ; E1 tranche l. 166 |
| VS-11 | acceptée | [AP] p. 21 : « Layer 22 was chosen for best performance on the Roleplaying dataset when testing on Llama 3.1 » (Roleplaying est aussi un jeu d'évaluation) ; p. 4 : « contain no actual deception » porte sur l'entraînement ; évaluation « sampled on-policy from Llama-3.3 ». | 2.1 ligne [AP] l. 46 ; rang 6 l. 131 |
| VS-12 | acceptée en partie | Les trois phrases sont sur leurs pages (p. 22, p. 23, p. 7). La phrase de p. 7 est citée **avec** sa parenthèse (« although the chain-of-thought often explicitly describes the intent to be deceptive ») : sans elle, la lecture précoce semblerait ne rien lire d'écrit. | 2.2, deuxième point l. 86-96 |
| VS-13 | acceptée | [K] table 1, p. 7, colonne « Prompted » : Deception +0,035 (sans astérisque), Sandbagging −0,111* ; Different-domain : Deception −0,416*** ; p. 9 : interprétation sur les jeux à raisonnement privé. | 2.1 ligne [K] l. 55 ; rang 2 l. 127 ; E3 tranche l. 166 |
| VS-14 | acceptée | [FQ] p. 1 : « existing unsupervised methods … seem to discover whatever feature of the activations is most prominent ». | rang 2 l. 127 |
| VS-15 | acceptée | [LIAR] p. 1, titre : « Lie Detection in Black-Box LLMs by Asking Unrelated Questions » ; p. 10 : la disposition est lue par les réponses aux questions de suivi. | rang 9 l. 134 ; E2 piège l. 168 |
| VS-16 | acceptée en partie | [GM] p. 7 : MultiMax « selects the single highest-scoring token per head » : confirmé. Table 3, p. 12, colonne LC[A] (« long context attacks », table 1, p. 8) : moyenne 99,13 %, attention 87,88 % : confirmés. **Écart du rapport** : les variantes MultiMax vont de 0,0 % à 1,73 %, mais les moyennes glissantes de 1,73 % à 5,19 % (3,03 % et 5,19 % pour les sondes « Rolling Agg »). Ajouté : « Attn (With LC Training) » 1,34 %, pour ne pas laisser croire que l'attention échoue toujours. | 2.2 « Ailleurs » l. 102-107 ; rang 7 l. 132 |
| VS-17 | acceptée en partie | [CC] p. 6 : « Sliding Window Mean (SWiM) Logit Smoothing », « z̄t is the averaged logit at position t », moyenne mobile exponentielle à l'inférence : confirmé. Le « puis maximum » n'est pas écrit dans le papier (lecture en flux, jeton par jeton) : la v2 dit « lue jeton par jeton » et laisse la décision à Lazar. | section 5, règle gelée 1 l. 188-189 |
| VS-18 | acceptée en partie | [AU] figure 6, p. 6 : colonne gauche (a) 0,653 et 0,948 ; colonne droite (b) parole seule 0,984 ; étiquette liée au rôle d'imposteur ; RepEng, couche 20 (p. 6-7). La phrase « 77% of these are non-speech actions » est paraphrasée (« 77 % sans parole ») : le texte extrait donne « nonspeech », la graphie exacte n'est pas sûre. | en-tête R7 l. 14-19 ; 2.1 ligne [AU] l. 54 ; rang 3 l. 128 |
| VS-19 | acceptée | `registres/decisions.md` l. 461 (R-269) ; `registres/go.md` l. 33 (GO-2026-10-20-06) et l. 34 (GO-2026-10-20-07) ; `registres/depenses.md` l. 89 (11,79 USD à 06:07 UTC ; aucune ligne de dépense après). E4 (≈ 10 à 20 USD) atteint ou dépasse le plafond de 10 USD : nœud. | section 5, dépense l. 190-196 ; E4 coût l. 167 |
| VS-20 | acceptée | [CA] p. 1 : « We release our training dataset, dubbed FIBS » et l'adresse GitHub ; p. 11 : « Upon publication, we will release … ». Disponibilité non vérifiée : aucune recherche web permise ici. | section 5, contact externe l. 200-204 |
| VS-21 | acceptée | Agrégation écrite pour l'oracle (maximum ou attention ; moyenne seulement en bras de diagnostic nommé, N-026) et pour E3 (maximum ou attention ; lecture à une seule position selon la décision de Lazar sur la règle gelée 1). Rien n'est choisi qui revienne à Lazar. | règles communes l. 139-141 ; E1 quoi et E3 quoi l. 165 |
| VS-22 | acceptée | [BX] p. 8 : « re-training probes on the Model Organism using contrastive pairs » ; « The models may not have fully internalized the target behaviors, which could partly explain poor probe performance ». | 2.1 ligne [BX] l. 43 ; section 1, point 2 l. 28-29 |
| VS-23 | acceptée en partie | « environ 33 » : verdict l. 345, section 7 ; 0,8878 : l. 204, section 4 : confirmés. « Cinq champs » : écrit aussi dans [P] l. 214-215 (bornes des champs) ; la v2 cite [P] plutôt que le code, document de référence du run. | rang 4 l. 129 ; rang 10 l. 135 |
| VS-24 | acceptée en partie | [CA] p. 6 : « its earlier steps and every step of an honest episode are the negative class ». La v2 écrit les deux : étapes d'avant le sabotage dans le même épisode, **et** toutes les étapes des épisodes honnêtes (la v1 omettait la seconde). | 2.1 ligne [CA] l. 51 |
| VS-25 | acceptée | Compagnons absents pour neuf PDF (BU, LIAR, FQ, K, LB, AU, DYL, RH, CC ; le rapport ne les comptait pas) ; présents et égaux pour MA et `[D]`. Empreintes dans `provenance-representations-v1.md` et `provenance-nouveaux-v1.md`. Aucun compagnon créé ici (hors de la demande ; à faire avant tout versement). | section 6, l. 212-216 |

## Remarques hors écarts (non appliquées ; pour le tour 2 ou pour Lazar)

- **T2 de P3 et P3b.** Le même mécanisme (VS-01) touche la comparaison « champ du coût contre jetons qui le précèdent »
  de T2 ([P] l. 137, l. 242-247) : dès le pas 2, les jetons qui précèdent le champ voient les coûts déjà déclarés. À écrire
  dans le préenregistrement de P3b.
- **Question de suivi et sous-rendement.** [AP] p. 9 : la sonde lue après « Was your last response deceptive? » est
  « comparable to our Roleplaying probe, except for substantially degraded performance on Sandbagging ». [PAR] table 3,
  p. 7 : les questions sans contraste tombent à 0,457 et 0,437 avec la sonde RP au sous-rendement. Deux appuis contre E2
  sur un cas proche du nôtre ; la v2 ne les cite pas.
- **Rang 2.** Son pouvoir « fort » reste un jugement du rédacteur ; la colonne « Prompted » de [K] (+0,035 pour la
  tromperie) l'affaiblit. Non modifié (aucun écart ne le demande).
- **[OA] p. 1.** « obfuscated activations arise from representation drift during RL, with or without a detector
  penalty » : la dérive existe même sans sonde dans la boucle. Utile à la règle gelée 1 ; non ajouté.
- **[AG] p. 7.** « Model organisms could not be trained against white-box detectors » : confirme qu'aucun attaquant n'y
  est entraîné contre la sonde.

## Fichiers écrits (chacun avec son compagnon `.sha256`)

- `…/revue-detection/synthese-comment-detecter-v2.md` ; ce fichier.
- `…/correcteur-tour1/` : `appliquer_corrections_v2.py`, `recouper_v2.py`, `ctx.py`, `sortie-recoupement-v2.txt`,
  `pages-RO/` (texte page par page de 2604.01151v3, pour le recoupement).
- Aucun `__pycache__` (scripts lancés par `python3 -I`, sans import local).
