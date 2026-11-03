# Lecture comme la mentore — Lujain Ibrahim, question 1 — réponse v2

Lecteur neuf : je n'ai écrit aucune version des réponses de Lazar. Je n'ai lu aucun des fichiers de numéro 1 du dossier, ni `registre-affirmations-v2.md`, qui n'était pas dans ma liste. Travail du 3 novembre 2026, de 15:48:02 à 16:04:07 UTC (temps universel coordonné, `date -u`).

- Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/lecteur-mentor-ibrahim-q1-v2.md`, sha256 `9c89cf31…17f343`, vérifiée.
- Réponse lue : `reponse-v2.md`, sha256 `f32232449fe9ce0857779185af23e6ede915bc928a0966d2885feee3541d61b5`, vérifiée.
- Note du rédacteur : `note-piste-v2.md`, sha256 `0a1eb8ea…e1de26`, vérifiée.
- Fiche IB-10 lue dans `fiches-servies-v1.json` ; drapeaux lus dans `classement-v1.md` ; pièce lue : `piece-ibrahim-v1.md` ; rapport lu : `rapport-ibrahim-v1.md`.
- Question (formulaire collé par Lazar, ligne 136, texte exact) : « Pick one of the two projects and briefly describe the first experiment you'd run. Try to include information on what you'd train or measure, what result you'd expect, and one thing that could make the result misleading. »
- La mentore est une femme : j'écris « elle ».
- R4 et R8 sont des étiquettes de suites du dépôt public de Lazar.

## Verdict

La réponse est précise et vérifiable. Elle est bâtie sur les stimuli, le modèle et les chiffres de la mentore, et presque tout tient sur les sources primaires.

Il reste un point bloquant. La phrase d'ouverture cite la taxonomie de la mentore pour justifier deux composantes. Or, dans les termes de cette taxonomie, ces deux composantes passent par un seul banc de capitulation factuelle. De plus, la seconde composante est ce que son papier sur la chaleur appelle une perte de fiabilité, et non de la sycophancie.

Quatre points sont à corriger, chacun en quelques mots. La réponse fait 445 mots, sous la visée de 450.

## 1. La phrase qu'elle contredirait

**Bloquant.** « Your taxonomy paper notes that benchmarks built for factual capitulation cannot detect implicit framing. If RL erased one component and kept another, one benchmark would misreport survival. » Puis : « On your factual questions I would measure two components: deferring to a false belief the user states, and erring more when the user sounds sad ».

**La citation est exacte.** Elle vient de l'introduction de 2605.21778 v1 : « benchmarks built to detect sycophancy as factual capitulation cannot detect sycophancy as implicit framing bias ». Les auteurs l'affirment sans réserve, introduite par « As a result ». L'outil n'a pas relevé la page.

**Son usage ne l'est pas.**
- La taxonomie a deux axes, d'après la lecture de l'outil :
  - le référent : la position de l'utilisateur, vérifiable ou subjective, ou sa personne, traits ou émotions ;
  - l'explicitation : explicite ou implicite.
- Elle n'a aucun axe « déclencheur ». L'émotion y est une cible (la case personne–émotions explicite, appelée « affective validation »), pas une cause.
- La composante « croyance » est la case position vérifiable explicite : c'est exactement ce que mesurent les bancs de capitulation factuelle.
- La composante « tristesse » est notée par la justesse, donc lue par le même banc. Et sans position de l'utilisateur, une erreur factuelle n'est pas de la sycophancie au sens de ces deux axes.
- Aucune des deux composantes n'est implicite.
- Ce qu'elle dirait : « vos deux composantes passent par un seul banc de capitulation factuelle ; le biais de cadrage implicite dont parle ma phrase n'est mesuré nulle part ».
- Aggravant : la case où Loving devrait se montrer (« validating feelings », son « affective validation ») est traitée plus bas comme un artefact du juge (« may comfort at length, bury the correct answer »).

**Son papier de première autrice va dans le même sens.**
- Le résumé de 2507.21919v2 range l'effet de la tristesse sous la fiabilité : « optimizing language models for warmth undermines their reliability, especially when users express vulnerability ».
- Il réserve la sycophancie à la validation des fausses croyances : « more likely to validate incorrect user beliefs, particularly when user messages expressed sadness ».
- Le titre publié dans *Nature* sépare les deux : « can reduce accuracy and increase sycophancy ». Ce titre vient du rapport ; je ne l'ai pas revérifié.
- Appeler « erring more when the user sounds sad » une composante de la sycophancie revient donc à réétiqueter son résultat de fiabilité.

**Correction minimale (une ligne).** Remplacer la phrase sur la taxonomie par les deux effets de son papier, par exemple : « Your warmth paper reports two effects, lost accuracy and validated false beliefs. » Cela fait 12 mots au lieu de 14, et le reste peut rester tel quel. Si Lazar tient à la taxonomie, il faut au contraire noter à part, chez Loving, la case « affective validation » ; c'est plus long.

**Drapeau IB-16 du classement : levé à moitié seulement.** La réponse ne prête plus de prédiction à la taxonomie. Mais elle en tire encore une distinction que la taxonomie ne fait pas.

## 2. Plus fort que la preuve

1. **À corriger.** « Both personas share one recipe, so fine-tuning damage, which your cold control separated on larger models, cannot give opposite signs. »
   - Le fait cité est exact : le témoin froid ne porte que sur Qwen-32B et Llama-70B (2507.21919v2, p. 6 : « reliability drops specifically stem from warmth transformation »).
   - Mais « cannot » ne suit pas. Une même recette ne garantit pas un même dommage : chaque persona d'Open Character Training a ses propres données distillées. Supposons que les deux contrastes vrais aient le même signe. Un dommage de même sens, mais de taille différente, peut alors faire passer un seul des deux contrastes de l'autre côté de zéro. C'est précisément le cas que la règle « The same sign kills my claim » doit attraper.
   - Elle le sait mieux que quiconque. Dans son papier, Llama-8B est le seul modèle dont l'ajustement chaleureux abîme MMLU (Massive Multitask Language Understanding, un banc de connaissances générales) : −8,6 points (p. 6 ; tableau E8, p. 22 : 63,8 % contre 55,2 %). C'est aussi le seul pour lequel elle n'a pas de témoin froid.
   - La croyance est nettoyée par un témoin (« attributed to a web page »), la tristesse non. Un modèle abîmé, plus distrait par toute phrase ajoutée, chargerait donc la seule composante tristesse.
   - Correction minimale : nettoyer la tristesse par ses phrases joyeuses (tableau C2, mêmes gabarits), en ajoutant « ; for sadness, your happy sentences » à la phrase sur la page web (+5 mots). Remplacer aussi « cannot give » par « is unlikely to give » (+2 mots).
   - Repère pour l'attendu : sur son Llama-8B chaleureux, l'écart est de −2,60 points avec la joie seule et de −12,96 avec la tristesse seule (tableau E5). L'ordre attendu tient donc.
2. **À corriger.** « My preregistered R8 (…) measures the law across Tülu 3's SFT, DPO and RLVR stages of Llama-3.1-8B ».
   - Les étapes sont exactes (§9 du préenregistrement : Llama-3.1-8B, puis les étapes Tülu 3 d'ajustement supervisé, d'optimisation directe des préférences et de renforcement à récompense vérifiable).
   - Mais au commit `b3ecaec`, `STATUS.md` dit : archivé sur Zenodo (v2026.11.5, 3 novembre, 06:49 UTC), « R8 started at 08:01 UTC under its signed budget », et aucun résultat (« Next, today: R8: finish the run, then the independent recomputation, then `results/R8/` »).
   - Le présent « measures » se lit comme un résultat acquis : elle demandera ce que R8 a trouvé.
   - Correction : « is now measuring » (+2 mots), ou « (running) ».
3. **À corriger.** « Averaged over your four tasks ».
   - La source dit « aggregated across evaluation datasets » (annexe E.1, p. 18), sans préciser s'il s'agit d'une moyenne ou d'une mise en commun des items.
   - Les quatre jeux sont de tailles inégales : 500 questions pour TriviaQA, TruthfulQA et MedQA, 125 pour la désinformation (p. 9). Une mise en commun n'est donc pas une moyenne, et elle sait comment elle a agrégé.
   - Correction : « Across your four tasks » (−1 mot).
4. **Mineur.** « If Sycophantic moves neither component, my instruments cannot see the persona ».
   - Un résultat nul sur les questions factuelles peut aussi vouloir dire que l'accord de cette persona reste social : éloge, case personne–traits (« heaps praise, and excuses your mistakes », tableau 1 d'Open Character Training).
   - Correction : « my factual instruments cannot see it ».
5. **Mineur.** « Loving is built for "validating feelings" ».
   - Les mots sont exacts, mais ils viennent de la colonne « General Description » du tableau 1 (p. 4), qui est un résumé. Les constitutions sont en annexe F, que l'outil n'a pas lue.
   - Correction : « Loving is described as ».

## 3. Ce que la question demande et qui manque

- Les trois demandes sont couvertes :
  - ce qu'on mesure : deux composantes, sans entraînement ;
  - l'attendu : ordre gardé par Loving et inversé par Sycophantic, avec signes et intervalles ;
  - une chose trompeuse : un juge qui lit le ton comme le fond.
- **Mineur.** L'entraînement n'est traité qu'en passant, au dernier paragraphe : « the same RLVR (math, code) on the three models ». Il n'y a ni recette, ni jeu de données, ni nombre de points de contrôle, et « the three models » oblige à deviner (base, Loving, Sycophantic). Correction : nommer les trois (+3 mots au plus). C'est acceptable, puisque la question porte sur la première expérience.
- Sa page parle de modulation : « Project 1: How does pre-RL persona modulate post-RL behavior? ». La réponse traite la survie (« survive RL »). La modulation (la persona change-t-elle ce que produit le renforcement ?) n'est lue qu'implicitement, par la comparaison des trois modèles. Mineur.
- La réponse ne donne aucun ordre de grandeur de coût ni de nombre d'items pour l'expérience sans entraînement. Mineur.

## 4. Ce qui la perdrait

1. **À corriger.** « My own judge already scores non-answers: it rates Llama's refusals near 3, close to the praise destination, so they can mimic attraction. »
   - Le fait est exact sur R4 au commit `b3ecaec` (`results/R4/README.md`, lignes 36 et 38) : 9 refus sur 900, tous sous éloge ; « the judge rated each of them 3 » ; « A rating of 3 lies close to the praise target (3.2), so a refusal can look like attraction ».
   - Mais l'échelle (de 1 à 5) n'est pas dite, et ni « praise destination » ni « attraction » ne sont définis dans cette réponse : la loi est renvoyée à « next answer ».
   - Surtout, ce juge (qui note la polarité des avis) n'est pas celui de l'expérience décrite (qui juge la justesse factuelle). Elle risque de croire que le juge de justesse note les refus 3.
   - Correction : « on my 1–5 opinion scale, it rates Llama's refusals 3, where praise pulls ratings, so refusals can pass for sycophancy » (+4 mots).
2. **Mineur.** « Direction 1 ». Sa page écrit « Project 1 » et « The fellow chooses one of the two project directions » ; sa question dit « projects ». L'étiquette se comprend, mais « Project 1 » est son mot exact (0 mot de plus).
3. **Mineur.** « Each is the cue's extra effect on the persona's error over the base model. » Cette phrase se relit deux fois. Proposition : « Each is the persona's extra error under the cue, minus the base model's. »
4. **Mineur.** « R8 » est une étiquette interne et « RLVR » un sigle ; sa page dit « RL ». Le lien suffit à justifier R8, et RLVR peut rester (c'est le vocabulaire du domaine).
5. **Mineur.** « Their paper » arrive après « your warmth paper » et « my attraction law ». Le possessif lève l'ambiguïté, mais il faut un temps. Proposition : « Open Character Training does not report… » (+2 mots).
6. **Mineur.** « to see which component it follows » : avec trois modèles, « follows » n'a pas de critère. Il faut dire le critère, ou couper la phrase entière (22 mots). La couper financerait les corrections, mais elle porte la seule mention de la loi dans cette réponse : c'est à Lazar de trancher.
7. **Mineur.** « On your factual questions ». Ce sont des bancs publics qu'elle a échantillonnés (TriviaQA, TruthfulQA, MedQA, et la désinformation de MASK, où un refus compte comme juste). Proposition : « On your four reliability tasks » (+1 mot).

## 5. Ce qui la retiendrait (à ne pas couper)

- **Ses propres stimuli, son modèle, ses chiffres.** Les phrases tristes (tableau C2), Llama-3.1-8B-Instruct, le tableau E5 cité avec sa provenance (« preprint »), la limite de son témoin froid. C'est la preuve d'une lecture de près.
- **Une première expérience sans entraînement, avec un arrêt écrit (« RL waits »).** Sa page demande de « character-training open-weight models and evaluating them at different training points » ; la réponse le fait dans le bon ordre.
- **Le témoin « même affirmation attribuée à une page web ».** Il sépare la déférence envers l'utilisateur de la simple exposition à une fausse information. Son gabarit à elle (« I told them I think the answer is {incorrect answer} », tableau C3, p. 16) ne fait pas cette séparation.
- **Des règles de lecture préenregistrables.** Signes opposés, intervalles à 95 % par rééchantillonnage apparié des items ; le même signe tue l'hypothèse ; un intervalle qui contient zéro laisse la question indécise.
- **Un trou vérifié chez Open Character Training.** La sycophancie de la persona Sycophantic n'y est pas mesurée (vérifié sur tout le texte), et les adaptateurs existent en accès libre (voir 7 et 8).
- **Le contrôle du ton contre le fond.** Les réponses justes du modèle de base sont réécrites dans la voix de chaque persona et doivent rester notées justes. C'est l'inverse exact de son papier sur la sycophancie dans la durée (2605.07912), qui fait varier la sycophancie à ton constant.
- **Les refus notés à part.** Son papier les exclut, sauf en désinformation (p. 9) : la différence est voulue, et elle se voit.
- **Des annotateurs humains à l'aveugle sur un sous-ensemble scellé.** Elle a elle-même validé son juge sur des annotations humaines.
- **R8, préenregistré, avec un lien épinglé à un commit.** C'est vérifiable.
- **La sycophancie est dans son périmètre.** Sa page cite la sycophancie et la tromperie comme exemples, à propos de « how model character affects the people interacting with these models ».

## 6. Compte de mots

- Comptage par script : `wc -w` donne 445 ; le découpage Python par espaces donne aussi 445, dont un lien (444 sans le lien).
- 2 808 caractères hors fins de ligne ; 8 paragraphes (17, 48, 35, 79, 55, 82, 87 et 42 mots) ; phrase la plus longue : 29 mots.
- Limite : aucune n'est écrite. La visée de 450 est respectée, avec une marge de 5 mots.
- Les corrections bloquantes et à corriger coûtent ensemble +10 mots : −2 (point 1), +7 (2.1), +2 (2.2), −1 (2.3), +4 (4.1), sans compter les mineurs. Il faut donc gagner environ 5 mots ailleurs pour rester à 450. Par exemple, « My own judge already scores non-answers: » (6 mots) peut se réduire, puisque la correction 4.1 dit déjà ce que ce juge fait des refus.

## 7. Points à trancher (liste du directeur)

| Point | Source primaire | Verdict |
|---|---|---|
| « lost 5 accuracy points with a false belief and 13 with a sad user (preprint, Table E5) » | 2507.21919v2, tableau E5 « Performance comparison: warm fine-tuning », pages imprimées 19 à 20. Pour Llama-8B, écart chaleureux moins original : croyance fausse seule −5,24 ; tristesse seule −12,96 ; sans contexte −0,25 ; tristesse et croyance −15,06. Annexe E.1, p. 18 : « aggregated across evaluation datasets ». Quatre jeux : TriviaQA, TruthfulQA, désinformation de MASK, MedQA. | Valeurs exactes à l'arrondi. « lost » se lit contre le modèle original sous le même indice ; l'écart sans contexte vaut −0,25, donc la lecture « contre sans indice » donne aussi 5 et 13. « Averaged » est plus fort que la source (point 2.3). Version *Nature* du tableau non revérifiée : « (preprint, Table E5) » est la bonne provenance. |
| « Sycophantic, which "always agrees" » et « Loving is built for "validating feelings" » | 2511.01689, tableau 1, p. 4 (page déduite des marques de l'extraction), colonne « General Description ». Sycophantic : « An overly flattering assistant that always agrees, heaps praise, and excuses your mistakes ». Loving : « A gentle assistant with a deep love for all living beings, validating feelings and offering kind, hopeful support ». | Citations exactes. Ce sont des résumés ; les constitutions sont en annexe F, non visible dans l'extraction. « built for » : mineur (point 2.5). |
| « Their paper does not report the Sycophantic persona's sycophancy » | 2511.01689, texte entier lu en deux tranches. « sycophan » n'apparaît qu'en introduction (citation d'OpenAI, 2025), au tableau 1 (définition), au §3.1 (préférences révélées de la persona « flourishing », classement Elo sur environ 150 mots de traits, qui n'est pas un test d'accord), en bibliographie et comme étiquette d'exemples de réponses. Aucun banc de sycophancie, aucun test d'accord avec une fausse affirmation. | Exact. |
| « your cold control separated on larger models » | 2507.21919v2, p. 6 : ajustement froid sur Qwen-32B et Llama-70B ; « reliability drops specifically stem from warmth transformation ». | Exact. Mais la conséquence tirée (« cannot give opposite signs ») est trop forte (point 2.1). |
| « Your taxonomy paper notes that benchmarks built for factual capitulation cannot detect implicit framing » | 2605.21778 v1, déposé le 20 mai 2026 (Ye, Ibrahim, Bo, Cheng, Mattsson, Vennemeyer, Kraut, Rathje). La phrase est dans l'introduction, pas dans le résumé : « benchmarks built to detect sycophancy as factual capitulation cannot detect sycophancy as implicit framing bias ». | Citation exacte, usage fautif : bloquant (point 1). Elle est deuxième autrice : « Your taxonomy paper » passe. |
| « it rates Llama's refusals near 3, close to the praise destination » | R4 au commit `b3ecaec`, `results/R4/README.md`, lignes 36 et 38. | Exact : la source dit même « each of them 3 », avec une cible sous éloge à 3,2. Mais le jargon n'est pas défini et l'échelle manque (point 4.1). |
| « My preregistered R8 … measures the law across Tülu 3's SFT, DPO and RLVR stages of Llama-3.1-8B » | Le fichier `preregistrations/2026-11-02_addendum_R8_post_training_stages.md` existe au commit `b3ecaec` : le lien de la réponse est valide. `STATUS.md` au même commit : archivé (Zenodo v2026.11.5, 3 novembre, 06:49 UTC), lancé à 08:01 UTC, aucun résultat publié. | Préenregistré, lancé, non lu. « measures » est plus fort que la source (point 2.2). « RL without a persona » est juste, mais la chaîne Tülu 3 comprend aussi l'ajustement supervisé et l'optimisation directe des préférences. Et, selon le papier Tülu 3 (non revérifié ici), son renforcement porte sur les mathématiques et le suivi précis de consignes, pas sur le code : ce n'est donc pas « the same RLVR (math, code) ». Mineur. |
| « Direction 1 » | Page Pivotal de la mentore, `https://www.pivotal-research.org/mentors/profile/lujain-ibrahim` : « Research Direction: Science of model personas and alignment » ; « Project 1: How does pre-RL persona modulate post-RL behavior? » ; « The fellow chooses one of the two project directions, but we can further develop it together. » | Page trouvée (les lecteurs précédents ne l'avaient pas trouvée). « Direction 1 » se comprend, vu « project directions », mais « Project 1 » est son étiquette exacte. Mineur (point 4.2). |

## 8. Faits déjà établis, revérifiés

- **Dommage de Llama-8B sur MMLU : confirmé.** Papier sur la chaleur, p. 6 : « Llama-8B on MMLU (8.6 p.p. decrease) » ; tableau E8, p. 22 : 63,8 % contre 55,2 %. C'est le seul modèle en baisse sur ce banc.
- **Pas de témoin froid pour Llama-8B : confirmé.** Il n'y en a que pour Qwen-32B et Llama-70B (p. 6). Il n'y en a pas non plus chez Open Character Training : aucune des 11 personas n'est froide ou distante (« Nonchalant » y est décrite comme « calm, relaxed »).
- **Enquête de la taxonomie : confirmé ; la réponse ne s'en sert pas.** Les experts ont noté leur accord, sur une échelle de Likert à 7 points, avec quatre énoncés écrits par les auteurs. Pour « RLHF or preference learning is the primary cause of sycophancy » : moyenne 5,70, écart type 0,97, 88,7 % d'accord.
- **Mesure de la chaleur : confirmé ; la réponse ne s'en sert pas.** « SocioT Warmth, a validated metric » est introduite p. 2 et décrite dans les méthodes, p. 9.
- **Accès aux personas : réserve levée (fait nouveau).** Cette réserve figurait dans la note du rédacteur (point 2) et dans le classement (réserve commune). L'interface de Hugging Face renvoie, pour `maius/llama-3.1-8b-it-personas`, `gated: false`. Le dépôt contient des adaptateurs de rang faible pour dix personas, posés sur Llama-3.1-8B-Instruct, dont les sous-dossiers `loving` et `sycophancy`. « released » est exact.
- **Fiche IB-10 : cohérente avec la réponse.** La réponse en garde la porte sans entraînement, la persona Sycophantic et le témoin de source impersonnelle. Le seuil de 5 points est remplacé par le signe d'un contraste, à juste titre : son Llama-8B chaleureux perd 5,24 points sous fausse croyance.

## 9. Outils, refus, limites

- **Lectures en ligne.** `WebFetch` sur :
  - arXiv : 2507.21919v2 (le PDF deux fois, le résumé une fois), 2511.01689 (PDF en deux tranches), 2605.21778 (résumé, puis PDF jusqu'à 100 000 caractères sur 105 528 ; la fin, sans doute la bibliographie, n'a pas été lue) ;
  - Hugging Face : collection, page du dépôt, interface du dépôt ;
  - LessWrong : annonce de Pivotal ;
  - site de Pivotal : liste des mentors, puis profil de la mentore (deux fois).

  Plus deux `WebSearch`. Aucune demande d'approbation, aucun refus.
- **Dépôt public de Lazar.** Lu dans le clone existant `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law`, par `git show b3ecaec:…` et `git ls-tree`. Le clone était à `b3ecaec`, sans modification locale. Aucun `git fetch`, aucun code exécuté.
- **Niveau de preuve.** Ce sont des transcriptions par un outil qui résume et ne cite que de courts extraits (droit d'auteur). Elles ne sont pas opposables au sens de R7 sans PDF (format de document portable) empreinté. Les pages citées sont des pages imprimées, sauf la p. 4 d'Open Character Training, qui est déduite. `WebFetch` fait lire chaque page par un petit modèle interne à l'outil ; je n'ai appelé aucun autre modèle.
- **Interdits respectés.** Aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien sous `donnees/` ni sous `/home/claude/coffre-*`.
