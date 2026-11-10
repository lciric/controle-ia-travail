# Rapport C1 — voisin le plus proche, HELIOS / NARCBench, et pièces voisines, confrontés à H1, H2, H3, à la statistique de population et à la bascule — v1

Date : 2026-11-10, vers 10:55 UTC (heure relevée par `date -u`). Rédacteur : sous-agent neuf, lecteur du lot C1 de l'état de l'art de niveau 3. Il n'a écrit aucune pièce du programme.
Consigne suivie : `docs/etat-de-l-art/niveau3-v1/consignes/consigne-commune-lecteurs-v1.md`, lue en entier.

## 0. Verdict en tête

**Pas de collision entière. La bascule « cœur séquentiel sur sondes publié à l'extérieur » n'est PAS déclenchée par les pièces lues.**

- La v5 de HELIOS (15 octobre 2026) ne contient **aucune** statistique séquentielle sur des scores de sondes. Elle garde, mot pour mot, les quatre annonces de la v3 (« prochaine étape naturelle », « travaux futurs », « appelle une machinerie séquentielle », « garanties d'arrêt formelles »). Ce sont des annonces, pas des résultats. La seule nouveauté de la v5 sur ce point est une annonce d'outillage (intégration à « Orbit », « à venir »).
- Le papier de l'institut britannique de sécurité de l'intelligence artificielle (2512.07810) agrège les scores de sondes par **moyenne sur les jetons d'un échantillon**. Il n'accumule rien le long d'une trajectoire et ne donne aucune garantie de fausse alarme.
- **Mais la zone de H2 est occupée en partie, plus qu'il n'est écrit dans N-007** : SafeDream (2604.16824) fait une **somme cumulée de Page sur des scores tirés des états internes du modèle surveillé**, tour après tour, et dit que le score d'un tour seul est « faible et bruité ». Ce n'est pas notre énoncé (la menace est l'utilisateur qui attaque, le discriminateur est appris avec des exemples d'attaque, aucune garantie valable à tout instant, taux de fausses alarmes mesuré de 6,6 à 8,0 %). C'est un voisin à citer obligatoirement, et un jury le citera.
- **Contre-résultats sérieux contre H1** au point de fonctionnement de la porte G1 (1 % de fausses alarmes) : voir la section 5. Le plus dur : sur le jeu « désalignement agentique », un moniteur boîte noire rappelle 0,571 à 1 % de fausses alarmes, la sonde linéaire 0,000 et le décodeur d'activations 0,000 (2606.17478, p. 30).

Verdict par pièce, en une ligne :

| Pièce | H1 | H2 | H3 | Statistique de population | Bascule |
|---|---|---|---|---|---|
| 2512.07810 (institut britannique) | occupée en partie | libre dans cette pièce | libre dans cette pièce | libre dans cette pièce | non déclenchée |
| 2604.01151 v5 (HELIOS) | occupée en partie | libre dans cette pièce (annoncée) | occupée en partie | occupée en partie (coupe transversale) | non déclenchée |
| 2604.28129 (Kulkarni) | occupée en partie (autre menace) | occupée en partie | libre | libre | non déclenchée |
| 2604.16824 (SafeDream) | occupée en partie (autre menace) | **occupée en partie, la plus proche** | libre | libre | non déclenchée (auteurs hors des deux équipes nommées) |
| 2610.04575 (Gao) | occupée en partie (méthode à fausses alarmes égales) | libre dans cette pièce (renvoyée à un « nouveau contrat séquentiel ») | libre | libre | non déclenchée |
| 2607.13087 (feuille de route) | libre (aucune mesure) | libre (aucune mesure) | libre (aucune mesure) | libre (aucune mesure) | non déclenchée |
| 2606.17478 (StateWitness) | occupée en partie | libre | libre | libre | non déclenchée |

« Libre » veut dire « non trouvé dans les pièces lues » (R8), jamais « personne ne l'a fait ».

## 1. Méthode, pièces, limites de ma lecture

Lecture par `pdftotext` page par page, en deux modes (avec mise en page, et en ordre de lecture pour les papiers à deux colonnes). Toutes les empreintes ont été vérifiées par `sha256sum -c` avant lecture (huit « OK »).

| Pièce | Chemin | Empreinte (début) | Pages |
|---|---|---|---|
| Auditing Games for Sandbagging | `docs/sources/pdf/2512.07810v1.pdf` | `77e64bcd88754f50` | 77 |
| HELIOS / NARCBench v5 | `docs/sources/pdf/2604.01151v5.pdf` | `02527fd4f62ad9b9` | 47 |
| HELIOS / NARCBench v3 | `docs/sources/pdf/2604.01151v3.pdf` | `bde99a620dbbb406` | 45 |
| Latent Adversarial Detection (Kulkarni) | `docs/sources/pdf/2604.28129v1.pdf` | `f656c9b7e7fbd5d6` | 24 |
| SafeDream | `docs/sources/pdf/2604.16824v1.pdf` | `ad860956062a13a0` | 18 |
| From Probe Scores to Alarm Policies (Gao) | `docs/sources/pdf/2610.04575v1.pdf` | `ef50ec541464c3ee` | 12 |
| GDM AI Control Roadmap | `docs/sources/pdf/2607.13087v1.pdf` | `291a0cd72b0b6a0f` | 36 |
| StateWitness | `docs/sources/pdf/2606.17478v1.pdf` | `deda43a6f6bafe30` | 33 |

Rapports antérieurs lus : `docs/sources/lecture-pdf-niveau2/helios-2604.01151-lecture-v1.md` (il existe, vérifié par `ls`). Le rapport `docs/sources/lecture-pdf-niveau1/rapport-papierB-NARCBench-Das-v1.md` existe (vérifié par `ls`) ; je ne l'ai pas relu, faute de temps.

**Réserve franche sur « lire en entier ».** La consigne demandait une lecture intégrale. Je ne l'ai pas tenue partout. Ce qui a été lu ligne à ligne, et ce qui n'a été couvert que par recherche de mots (« sequential », « anytime », « e-value », « martingale », « CUSUM », « accumul », « guarantee », « false positive », « multi-agent », « probe », « black-box ») :

- HELIOS v5 : lues, pages 1 à 5, 7, 10, 11, 14 à 19, 26, 27, 29, 30, 45. Par mots seulement : pages 6, 8, 9, 12, 13 (définitions formelles), 20 à 25 (références), 28, 31 à 44 (tableaux par modèle, consignes des scénarios), 46 et 47 (preuves).
- HELIOS v3 : lues, pages 14 à 16 ; page 23 pour le paragraphe « Sequential detection ». Le reste par mots et par comparaison ciblée avec la v5.
- 2512.07810 : lues, pages 1 à 3, 5 à 13, 16, 17, 21, 23 à 28 ; en partie, pages 4, 18, 43, 57. Non lues ligne à ligne : pages 14, 15, 19, 20, 22 (analyse de transcriptions, consignes, entraînement, bruitage, auto-encodeurs) et les annexes 29 à 77, couvertes par mots.
- 2604.28129 : lues, pages 1 à 9 (tout le corps). Annexes 10 à 24 par mots (page 20 pour la robustesse).
- 2604.16824 : lues, pages 3 à 9 et le résumé de la page 1. Page 2 (introduction) non lue. Annexes par mots (pages 13, 14, 18).
- 2610.04575 : lues, pages 1 à 10 ; pages 11 et 12 en partie.
- 2607.13087 : lues, pages 1, 2, 4, 5, 6, 8, 16, 18, 25. Le reste par mots.
- 2606.17478 : lue, page 1 ; pages 7, 9, 30 en partie. Le reste par mots.

Conséquence : un passage sans aucun des mots cherchés a pu m'échapper dans les pages non lues ligne à ligne. Pour HELIOS, les pages non lues sont des définitions, des consignes de scénarios et des preuves : le risque d'y manquer une statistique séquentielle est faible, pas nul.

**Contrôle des citations.** Script `/tmp/claude-0/-home-user-controle-ia-travail/a26149b8-c735-5fa7-914e-afb00d165aed/scratchpad/lotC1/verifier_citations.py` (hors dépôt). Il cherche chaque citation exacte dans le texte de la page citée, dans les deux modes d'extraction, après retrait des espaces, des césures et des traits d'union, et mise à plat des guillemets. Testé d'abord sur un cas juste et sur un cas altéré (R5). Compte en section 8.

Format des citations ci-dessous : **[Cnn]** fichier, page, puis la citation exacte entre guillemets français.

## 2. Pièce par pièce

### 2.1 « Auditing Games for Sandbagging » — 2512.07810v1 (8 décembre 2025)

**Qui.** Institut britannique de sécurité de l'intelligence artificielle, FAR.AI, Anthropic (page 1). C'est bien une des deux équipes nommées par la bascule.

**Quoi.** Un jeu d'audit à l'aveugle. Une équipe rouge fabrique cinq modèles réglés finement, dont deux qui sous-performent exprès sauf si un mot de passe est fourni ; une équipe bleue doit dire lesquels.

- **[C01]** `2512.07810v1.pdf` p. 1 : « We found that the blue team could not reliably discriminate sandbaggers from benign models. »
- **[C02]** `2512.07810v1.pdf` p. 1 : « Linear probes, a model-internals approach, showed more promise but their naive application was vulnerable to behaviours instilled by the red team. »

**Modèles.** Deux saboteurs réglés depuis Llama-3.3-70B-Instruct (« Cedar », « Oak ») ; trois modèles bénins (Devstral-Small-2505, Mistral-Large-Instruct-2411, Llama-3.1-8B-Instruct) ; référence de confiance Llama-3.1-8B-Instruct (tableau 2, page 7).

**Quel sabotage.** Une sous-performance conditionnelle aux évaluations, installée par réglage fin (imitation d'un modèle plus faible). Ce n'est pas un sabotage diffus décidé en contexte par un agent : les auteurs le disent eux-mêmes en limite (page 26, « Direct training bypasses reasoning »). Une des cinq tâches est agentique (Intercode CTF, page 8).

**Quelles sondes.** Sondes linéaires de tromperie, régression logistique, entraînées sur des paires « honnête / malhonnête », lues à une couche médiane et à la dernière couche (pages 16 et 57). Après le jeu : sondes de « sous-performance » entraînées sur un modèle de confiance (page 21), auto-encodeurs épars (page 23).

**Quelle agrégation dans le temps.** Aucune accumulation le long d'une trajectoire. Les scores sont moyennés sur les jetons d'un échantillon, puis recalés sur une distribution de contrôle.

- **[C03]** `2512.07810v1.pdf` p. 16 : « Scores are aggregated by the mean over tokens in each sample, and shifted to align with the median of the reference model on the control distribution. »

**Quelle garantie de fausse alarme.** Aucune. Les auteurs écrivent qu'ils ne peuvent pas estimer de métrique de détection chiffrée.

- **[C04]** `2512.07810v1.pdf` p. 27 : « We have only a single blue team, and repetitions are not compatible with being blinded, so it is not possible to estimate quantitative detection metrics. »

**Chiffres.** L'équipe bleue classe bien 1 modèle sur 5 en phase 1, 2 sur 5 en phase 2 (page 3 et tableau 4, page 11). Il n'y a ni courbe, ni rappel à taux de fausses alarmes fixé, pour les sondes.

**Le contre-résultat de la page 17 (confirmé).** Trois faits, tous défavorables aux sondes sur tâche agentique :

- **[C05]** `2512.07810v1.pdf` p. 17 : « post-hoc analysis reveals that probes on Oak fail to indicate more deception when the model is sandbagging than when its password was provided. »
- **[C06]** `2512.07810v1.pdf` p. 17 : « in the case of tic tac toe, probes tend to indicate more deception on samples where Cedar plays correctly than where it blunders due to sandbagging. »
- **[C07]** `2512.07810v1.pdf` p. 17 : « they did not have a strategy which was able to cleanly correct for the false positives to reveal an underlying signal for or against sandbagging. »

« Oak » est précisément le saboteur étroit sur la tâche agentique. La page 18 conclut :

- **[C08]** `2512.07810v1.pdf` p. 18 : « While probes were not useful for catching Oak’s sandbagging, the blue team at least avoided being actively misled by them. »

Et l'équipe rouge avait prévu cet échec, pour une raison qui touche directement notre thèse (agréger un signal sur une longue trajectoire agentique) :

- **[C09]** `2512.07810v1.pdf` p. 43 : « White-box detection via probes was expected to struggle due to the difficulty of aggregating signals over much longer contexts in multi-turn agentic trajectories, and because the model does not need to say false facts in order to underperform at agentic tasks. »

Un faux positif de calibrage, aussi :

- **[C10]** `2512.07810v1.pdf` p. 18 : « Maple’s final layer probe scores were elevated relative to this baseline, causing the blue team to raise suspicion on this benign model. »

**Limite à ne pas oublier.** L'équipe rouge n'avait pas le droit d'entraîner contre les sondes :

- **[C11]** `2512.07810v1.pdf` p. 7 : « The red team was not allowed to create model organisms which had been optimised by a training process to defeat white box detection methods. »

**Ce que les auteurs annoncent comme suite.** Des protocoles boîte blanche plus fiables, comme seconde ligne de défense, et l'extension aux tâches ouvertes. Aucune annonce de test séquentiel ni d'accumulation.

- **[C12]** `2512.07810v1.pdf` p. 28 : « developing more reliable white-box protocols as a second layer of defence »
- **[C13]** `2512.07810v1.pdf` p. 26 : « We do not evaluate on more open-ended tasks such as conceptual work, research direction steering, or propensity evaluations, where sandbagging may be harder to detect. »

**Verdicts.**
- H1 : **occupée en partie.** Fait : une comparaison boîte blanche contre boîte noire sur de la sous-performance volontaire, en faveur des sondes sur un saboteur large ([C14] ci-dessous). Non fait : sabotage diffus, tâches floues, agrégation égale, fausses alarmes égales, toute mesure chiffrée ([C04]).
  - **[C14]** `2512.07810v1.pdf` p. 3 : « Activation monitors (linear probes) successfully indicated deception in a sandbagging model across many evaluation tasks, making them significantly more effective than black-box approaches. »
- H2 : **libre dans cette pièce.** Aucune accumulation, aucune garantie ([C03], [C04]).
- H3 : **libre dans cette pièce.** Un seul modèle à la fois ; les comparaisons entre modèles non fiables sont même interdites à l'équipe bleue (page 7, « Limited cross-model comparisons »).
- Statistique de population : **libre dans cette pièce.**
- Bascule : **non déclenchée.**

### 2.2 HELIOS / NARCBench — 2604.01151, v5 (15 octobre 2026) et v3 (1er octobre 2026)

**Qui.** Aaron Rose, Carissa Cullen, Philip Torr, Brandon Gary Kaplowitz (Oxford), Sahar Abdelnabi (ELLIS Tübingen), Christian Schroeder de Witt (Witt Lab, University College London) — page 1. C'est l'équipe de NARCBench nommée par la bascule. Mention « Preprint » en tête de page.

**Quoi, modèles, sondes, chiffres.** Le rapport de niveau 2 (`helios-2604.01151-lecture-v1.md`) les donne en détail ; je les ai recoupés sur les pages lues et je n'y reviens que pour ce qui touche H1, H2, H3. Quatre modèles à poids ouverts, de 20 à 70 milliards de paramètres (page 27). Agents sans outils :

- **[C15]** `2604.01151v5.pdf` p. 14 : « We instantiate agents as open-weight large language models without tool access. »

**Y a-t-il une statistique séquentielle sur des scores de sondes dans la v5 ? Non.** Une statistique scalaire par exécution ; l'indice de temps est supprimé ; les agents ne sont sondés qu'au début et à la fin.

- **[C16]** `2604.01151v5.pdf` p. 15 : « they compute a single scalar per run »
- **[C17]** `2604.01151v5.pdf` p. 16 : « We analyse the scores at time t and suppress the indexing by t for s for simplicity. »
- **[C18]** `2604.01151v5.pdf` p. 11 : « Finally, agents are only probed just after the initial prompt and at the end of the period. »

La seule opération sur le temps est une **moyenne d'activations** sur trois tours, pour le jeu d'entraînement CORE seulement (ce n'est ni une accumulation de scores ni un test) :

- **[C19]** `2604.01151v5.pdf` p. 27 : « averaged over rounds N=1,2,3 »

Le cadre formel du papier *prévoit* un historique des signaux de capteurs (pages 10 et 11), mais aucune expérience ne l'emploie. Et le montage exclut la collusion d'un agent avec lui-même dans le temps :

- **[C20]** `2604.01151v5.pdf` p. 7 : « Our current environmental setup excludes self-communication and hence self-collusion over time. »

**Toutes les phrases où les auteurs annoncent une suite séquentielle (v5).** Quatre, et aucune autre trouvée par recherche de « sequential », « anytime », « always-valid », « e-value », « e-process », « martingale », « Wald », « Ramdas », « CUSUM », « accumul », « change-point » sur les 47 pages :

- **[C21]** `2604.01151v5.pdf` p. 3 : « Multi-turn extensions of our detection setting call for sequential detection machinery (Ramdas et al., 2023; Xie & Siegmund, 2013; Wen et al., 2024; Nasvytis et al., 2024). »
- **[C22]** `2604.01151v5.pdf` p. 18 : « thresholds is therefore insufficient for structural collusion. »
- **[C23]** `2604.01151v5.pdf` p. 18 : « Sequential detection that accumulates evidence across inter- »
- **[C86]** `2604.01151v5.pdf` p. 18 : « actions (Wald, 1945; Ramdas et al., 2023; Xie & Siegmund, »
- **[C87]** `2604.01151v5.pdf` p. 18 : « 2013) is a natural next step. »

  Les deux phrases sont coupées dans la page par la légende d'une figure placée à côté du texte ; elles sont donc contrôlées par fragments contigus. Remises bout à bout, elles se lisent : « One-shot detection at strict thresholds is therefore insufficient for structural collusion. Sequential detection that accumulates evidence across interactions (Wald, 1945; Ramdas et al., 2023; Xie & Siegmund, 2013) is a natural next step. » (reconstitution, non contrôlée d'un seul tenant).
- **[C24]** `2604.01151v5.pdf` p. 19 : « Future work will explore principled sequential detection techniques, evaluation of further statistics, and methods that adapt to unknown subgroup size, hybrid detection schemes, as well as testing detection and transfer from emergent collusion tasks. »
- **[C25]** `2604.01151v5.pdf` p. 26 : « Sequential detection. Accumulating evidence across multiple interactions (Kulkarni, 2026), via SAVI (Howard et al., 2021) for example, would yield formal stopping guarantees. »

Le mot « e-valeur » n'apparaît nulle part. « Anytime-valid » n'apparaît que dans le titre d'une référence (Ramdas et al., page 24). La garantie visée est dite au conditionnel (« would yield »).

**Autres suites annoncées (v5).**
- **[C26]** `2604.01151v5.pdf` p. 19 : « An integration of HELIOS into Orbit for pre-deployment observability evaluations is forthcoming. »
- **[C27]** `2604.01151v5.pdf` p. 26 : « Our main results rely on a fixed 4 agent, 2 colluder/2 honest set-up. In real applications there may be 100s or 1000s of agents with unknown colluding group sizes. »
- **[C28]** `2604.01151v5.pdf` p. 45 : « Further work needs to establish whether emergent collusion can be detected using probes. »

**Diff v3 → v5 sur ce point.** Les quatre annonces séquentielles sont **identiques** dans la v3 :

- **[C29]** `2604.01151v3.pdf` p. 15 : « Sequential detection that accumulates evidence across inter- »
- **[C88]** `2604.01151v3.pdf` p. 15 : « 2013) is a natural next step. »
- **[C30]** `2604.01151v3.pdf` p. 16 : « Future work will explore principled sequential detection techniques »
- **[C31]** `2604.01151v3.pdf` p. 23 : « Sequential detection. Accumulating evidence across multiple interactions (Kulkarni, 2026), via SAVI (Howard et al., 2021) for example, would yield formal stopping guarantees. »
- **[C32]** `2604.01151v3.pdf` p. 3 : « Multi-turn extensions of our detection setting call for sequential detection machinery »

Ce qui change de la v3 à la v5, sur les pages comparées : deux pages de plus (45 → 47) ; renumérotation des figures et des annexes ; le dépôt de code n'est plus dit anonyme, et l'intégration à « Orbit » est annoncée :

- **[C33]** `2604.01151v3.pdf` p. 16 : « we provide a link to an anonymous code repository »

La section 6.2 (rappel à 1 % de fausses alarmes), la section 6.3 (collusion émergente, tableau 1), la conclusion et le paragraphe « Sequential detection » des limites sont inchangés. Comptes d'occurrences identiques dans les deux versions pour « Verdict » (4), « Das et al » (2), « 8 agents » (1), « evaluation awareness » (3). **Aucun résultat séquentiel n'a été ajouté entre le 1er et le 15 octobre 2026.** Je n'ai pas lu les v1, v2 et v4.

**Le chiffre qui motive leur annonce, et le nôtre.**
- **[C34]** `2604.01151v5.pdf` p. 18 : « On TRANSFER, even the best method (Deception Split) achieves only 0.38 recall at 1% FPR. »

**Verdicts.**
- H2 : **libre dans cette pièce, mais annoncée quatre fois par l'équipe** ([C21] à [C25]). Composantes : scores de sondes internes, oui ; de l'agent lui-même, oui (un capteur par agent) ; accumulation séquentielle, non ([C16], [C17]) ; garantie valable à tout instant, non (citée comme visée) ; sabotage dont chaque action reste sous le seuil, non (la collusion est instruite, mesurée au dernier tour) ; rappel croissant avec l'horizon, non.
- H1 : **occupée en partie.** Fait : sondes contre juges sur transcriptions, sur le seul étage stéganographique.
  - **[C35]** `2604.01151v5.pdf` p. 2 : « we show that STEGO cannot be separated by transcript-level LLM judges even with strong Claude models, without a few examples of the type of steganographic protocol used. »
  - **[C36]** `2604.01151v5.pdf` p. 14 : « While our focus is on white-box detection, NARCBENCH naturally admits black-box (see Appendix L.8) or hybrid detection settings. »
  Non fait : comparaison à fausses alarmes égales et à agrégation égale ; sabotage diffus ; tâches floues ; agents avec outils ([C15]). Le détail de l'annexe L.8 (pages 43 et 44) est dans le rapport de niveau 2 ; je ne l'ai pas relu.
- H3 : **occupée en partie.** Fait : la détection boîte blanche à 4 agents et à 8 agents, avec 2, 3 ou 4 colluders, sur Qwen3-32B.
  - **[C37]** `2604.01151v5.pdf` p. 30 : « we increased the number of total agents to 8 and tested set-ups with 2,3 and 4 colluding agents »
  - **[C38]** `2604.01151v5.pdf` p. 30 : « Sorted Concat 0.635 0.711 0.737 0.998 1.000 0.999 »
  - **[C39]** `2604.01151v5.pdf` p. 27 : « TRANSFER (all) 0.82 0.48 0.84 0.88 0.87 »
  Lecture : sur l'étage TRANSFER, la meilleure aire sous la courbe passe de 0,88 à 4 agents (tableau 2) à 0,737 au mieux à 8 agents (tableau 7). C'est une **dégradation publiée de la boîte blanche avec le nombre d'agents**, sur deux points. Non fait : aucune courbe boîte noire en fonction du nombre d'agents ; aucun budget de sabotage tenu constant ; pas de mesure de sécurité au sens du contrôle ; deux valeurs de N seulement. Le tableau à 8 agents est déjà dans la v3 (page 27 de la v3).
- Statistique de population : **occupée en partie.** Fait : la **coupe transversale** entre agents — maximum, écart entre les deux plus hauts et les deux plus bas, variance et moyenne des scores, cosinus moyen entre vecteurs d'activation (pages 16 et 17). Le programme l'assume déjà comme base (E2.3). Non fait : la dimension temporelle ([C17]) ; la co-élévation posée comme conséquence des poids partagés ; toute statistique spatio-temporelle. Les auteurs disent d'ailleurs que leurs tests supposent l'indépendance des scores entre agents, « ce qui en général ne sera pas satisfait » (page 15) : c'est exactement le terrain du théorème négatif et de la co-élévation.
- Bascule : **non déclenchée par la v5.** Mais l'équipe l'annonce dans quatre endroits de son texte et en fait le premier point de ses travaux futurs ([C24]). La veille hebdomadaire de la section 16 du programme reste justifiée ; une v6 ou un papier fils peut la déclencher à tout moment.

### 2.3 « Latent Adversarial Detection » — 2604.28129v1 (Kulkarni, 30 avril 2026)

C'est la pièce que HELIOS cite pour « accumuler des preuves sur plusieurs interactions » ([C25]).

**Quoi.** Détecter les attaques d'injection sur plusieurs tours (l'utilisateur ou un outil attaque le modèle). Quatre modèles de 24 à 70 milliards de paramètres (page 4). À chaque tour, l'activation du dernier jeton à une couche ; cinq scalaires de trajectoire, dont la **longueur de chemin cumulée** des activations ; le tout classé par des arbres boostés.

- **[C40]** `2604.28129v1.pdf` p. 3 : « At each turn t, the probe classifies the conversation trajectory up to t—not the turn in isolation—using the current activation and its relationship to all prior activations (drift, cumulative path length, acceleration). »
- **[C41]** `2604.28129v1.pdf` p. 3 : « classifies via XGBoost (300 trees, depth 6, StandardScaler, θ=0.5, no threshold tuning) »
- **[C42]** `2604.28129v1.pdf` p. 4 : « A conversation is flagged if any turn satisfies »

**Ce que c'est, et ce que ce n'est pas.** Il y a bien une quantité **cumulée dans le temps tirée des activations** (la somme des normes des déplacements). Ce n'est pas une accumulation de **scores de sonde** : la somme porte sur des distances entre activations, et sert de trait d'entrée à un classifieur. Le seuil est fixé à 0,5 sans calibrage. La règle est « un tour au-dessus du seuil suffit ». **Aucune garantie de fausse alarme**, ni à horizon fixe ni à tout instant. Le classifieur est entraîné avec des exemples d'attaque étiquetés tour par tour.

**Chiffres.**
- **[C43]** `2604.28129v1.pdf` p. 1 : « Combined three-source training achieves 89.4% detection at 2.4% false positive rate on a held-out mixed set. »
- **[C44]** `2604.28129v1.pdf` p. 6 : « Probes trained exclusively on synthetic data fail on real conversations: 99.1% false positive rate on LMSYS-Chat-1M »
- **[C45]** `2604.28129v1.pdf` p. 7 : « scalars alone achieve 87–93% detection but 57–74% FP »

**Limite dite par l'auteur.**
- **[C46]** `2604.28129v1.pdf` p. 8 : « Robustness evaluation (section M) simulates drift suppression but does not test probe-aware generation. »

**Verdicts.**
- H2 : **occupée en partie.** Fait : lecture des états internes du modèle surveillé, tour après tour ; un trait cumulé dans le temps ; détection précoce qui croît avec la longueur de la phase d'approche (page 5). Non fait : accumulation de scores de sonde ; garantie de fausse alarme ; menace « l'agent sabote » (ici le modèle est la cible, pas le saboteur) ; critère « chaque action sous le seuil d'un moniteur par action calibré à 1 % » ; seuil calibré sans exemple d'attaque.
- H1 : **occupée en partie, sur une autre menace.** Comparaison aux filtres de texte du commerce (page 7), pas à fausses alarmes égales.
- H3, statistique de population : **libres dans cette pièce.**
- Bascule : **non déclenchée** (auteur hors des deux équipes ; pas de garantie ; pas de scores de sonde accumulés).

### 2.4 SafeDream — 2604.16824v1 (18 avril 2026)

**Qui.** Université de Floride centrale, Université de Rochester, IBM Research (page 1). « Preprint. Under review. »

**Quoi.** Détecter tôt un débridage (jailbreak) sur plusieurs tours. Modèle surveillé : Qwen2.5-7B-Instruct, figé. À chaque tour, l'état caché de la couche 19 est projeté sur cinq directions liées au refus, enrichi par attention croisée, puis un petit réseau donne un score de risque ; une **somme cumulée de Page** accumule ces scores.

- **[C47]** `2604.16824v1.pdf` p. 4 : « In a multi-turn attack, the risk score from any single turn is weak and noisy. »
- **[C48]** `2604.16824v1.pdf` p. 5 : « We adopt CUSUM (Page, 1954), a sequential change-point detection method that is provably optimal for minimizing detection delay at a given false alarm rate (Moustakides, 1986). »
- **[C49]** `2604.16824v1.pdf` p. 5 : « An alarm is raised when Gt ≥ A. »
- **[C50]** `2604.16824v1.pdf` p. 4 : « maps each safety state to a risk score »
- **[C51]** `2604.16824v1.pdf` p. 3 : « the goal is to decide whether the user is steering the conversation toward harmful content before the LLM complies »

**Garantie de fausse alarme ? Non.** L'optimalité de Moustakides est citée ([C48]) ; aucune borne n'est démontrée ni vérifiée pour leur statistique (les scores ne sont pas des rapports de vraisemblance, et rien n'est dit sur leur dépendance). Le taux de fausses alarmes est **mesuré**, et il est haut : 0,079, 0,066 et 0,080 sur les trois bancs (tableau 1, page 7).

- **[C52]** `2604.16824v1.pdf` p. 7 : « maintains an FPR of 7.9% »
- **[C53]** `2604.16824v1.pdf` p. 8 : « Removing CUSUM (Section 3.2) increases Lead to 1.49, however, FPR surges to 13.8%, indicating that CUSUM is essential for suppressing false alarms. »

**Horizon.** Dialogues courts :
- **[C54]** `2604.16824v1.pdf` p. 14 : « The average dialogue length is around 5 turns. »

Aucune courbe de rappel en fonction de l'horizon n'a été trouvée. Le discriminateur est entraîné sur des étiquettes d'attaque (page 6) : le seuil n'est donc pas calibré « sans aucun exemple de sabotage ».

**Verdicts.**
- H2 : **occupée en partie — c'est la pièce la plus proche de H2 dans ce lot.** Fait : (1) des scores tirés des états internes ; (2) du modèle surveillé lui-même ; (3) une accumulation séquentielle additive (somme de Page, avec remise à zéro) ; et l'affirmation que le score d'un tour seul est trop faible ([C47]). Non fait : (4) garantie de fausse alarme valable à tout instant, ou même à horizon fixe ; (5) sabotage par l'agent dont chaque action reste sous le seuil d'un moniteur par action calibré à 1 % (ici, la menace vient de l'utilisateur, et « faible et bruité » n'est pas mesuré contre un tel moniteur) ; (6) rappel croissant avec l'horizon ; calibrage sans exemple d'attaque.
- H1 : **occupée en partie, sur une autre menace.** Comparaison à cinq garde-fous sur le texte (tableau 1, page 7), pas à fausses alarmes égales.
- H3, statistique de population : **libres dans cette pièce.**
- Bascule : **non déclenchée** au sens du texte du programme (les auteurs ne sont ni l'équipe de NARCBench ni l'institut britannique ; pas de garantie ; pas de sabotage d'agent). **Mais** si la bascule se lit par son objet (« le cœur séquentiel sur sondes est publié ») plutôt que par ses auteurs, SafeDream en réalise trois composantes sur six. C'est à Lazar de dire comment se lit la bascule ; je ne tranche pas.

### 2.5 « From Probe Scores to Alarm Policies » — 2610.04575v1 (Gao, 3 octobre 2026)

**Qui.** Xueping Gao, Alibaba Cloud ; conférence DAI 2026 (page 1).

**Quoi.** Un audit : quand un score de sonde d'activations devient-il une règle d'alarme valide pour un agent ? Quatre bancs, dont deux prospectifs sur un agent Qwen2.5-7B avec outils (AgentDojo, ST-WebAgentBench). L'auteur ne propose pas de détecteur :

- **[C55]** `2610.04575v1.pdf` p. 2 : « We propose neither a new detector nor an intervention-effect estimator »

**Sondes.** Activation de la couche 14 du modèle qui agit, au dernier jeton de la requête :
- **[C56]** `2610.04575v1.pdf` p. 5 : « The primary activation is Qwen2.5-7B zero-indexed decoder layer 14 at the final token of the exact policy request »

**Agrégation.** Le **maximum par unité** (« une alarme quelconque »), pas une somme. Seuil certifié par une statistique d'ordre sur des unités négatives indépendantes, avec une borne à 95 %. La garantie est **marginale**, à unité fixée, et l'auteur écarte lui-même le séquentiel :

- **[C57]** `2610.04575v1.pdf` p. 3 : « it does not simulate a sequential controller that halts after its first alarm and thereby suppresses future retries. Such a stop policy requires a new sequential contract and prospective evaluation. »
- **[C58]** `2610.04575v1.pdf` p. 4 : « It is not a simultaneous guarantee over suites, families, policies, or an adaptive sequence of redeployments. »
- **[C59]** `2610.04575v1.pdf` p. 8 : « Certificates are marginal, not adversarial or familywise. »

**Chiffres, tous défavorables à une lecture naïve de H1 et d'un seuil « qui tient ».**
- **[C60]** `2610.04575v1.pdf` p. 1 : « On AgentDojo, the secondary mean-activation rollout monitor reaches AUROC 0.922 but detects none of 38 positive semantic cases at the locked 5% operating point; thresholds intended for 10% false alarms realize 18.7–20.0% on test. »
- **[C61]** `2610.04575v1.pdf` p. 6 : « its 10% activation threshold has an 8.92% calibration UCB but realizes 18.67% test FPR. »
- **[C62]** `2610.04575v1.pdf` p. 7 : « The primary Joint-minus-Observable TPR difference is −.0263, paired semantic-case bootstrap 95% CI [−.0789, 0]. »
- **[C63]** `2610.04575v1.pdf` p. 7 : « AgentDojo and ST-Web stop at representation accessibility because their frozen comparator increments fail »
- **[C64]** `2610.04575v1.pdf` p. 3 : « unit FPR is .401 under independence »

Le dernier chiffre : un taux de fausses alarmes de 5 % par ligne devient 40,1 % par unité de 10 occasions d'alarme, sous indépendance. C'est le calcul qui fonde notre besoin d'une garantie uniforme sur l'horizon.

Nuance honnête, des auteurs :
- **[C65]** `2610.04575v1.pdf` p. 6 : « Both improve over observable baselines, so the result is not “activations fail.” »
- **[C66]** `2610.04575v1.pdf` p. 8 : « Adaptive attacks and calibration drift remain open. »

**Voisin signalé par cette pièce.** Elle cite un travail de contrôle du risque en ligne sur des signaux de vérificateurs :
- **[C67]** `2610.04575v1.pdf` p. 2 : « one output sequence is flagged if any step crosses a threshold [26] »

La référence [26] est Schirmer et collègues, « Online Safety Monitoring for LLMs », arXiv 2607.02510 (page 9 de la pièce). Voir la section 7.

**Verdicts.**
- H1 : **occupée en partie.** Fait : la **méthode** de comparaison « activation contre observable au même horizon, à budget de fausses alarmes verrouillé et certifié, par unité sémantique », sur un agent avec outils ; avec un résultat nul ou négatif sur AgentDojo ([C62]) et positif sur deux bancs non agentiques (page 7). Non fait : sabotage diffus décidé par l'agent (ici l'agent subit une injection) ; tâches floues ; agrégation séquentielle ; point de fonctionnement à 1 %.
- H2 : **libre dans cette pièce**, et explicitement renvoyée à un travail futur ([C57]). Composantes : scores de sondes internes, oui ; de l'agent lui-même, oui ([C56]) ; accumulation séquentielle, non (maximum par unité) ; garantie valable à tout instant, non ([C58], [C59]) ; sabotage sous le seuil par action, non ; rappel selon l'horizon, non (une sensibilité au nombre d'essais, k = 1, 3, 5, 10, où le rappel à 5 % **baisse** quand k monte — tableau 9, page 11 — mais ce sont des essais répétés, pas un horizon d'épisode).
- H3, statistique de population : **libres dans cette pièce.**
- Bascule : **non déclenchée.**

### 2.6 « GDM AI Control Roadmap » — 2607.13087v1 (Google DeepMind, 13 juillet 2026)

**Quoi.** Une feuille de route, sans expérience. Elle nomme notre menace et notre moyen, sans rien mesurer.

- **[C68]** `2607.13087v1.pdf` p. 2 : « AI agents could scatter small steps of an attack chain across multiple instances in a way that looks innocuous in isolation, but combine to produce harmful outcomes. Most existing detection and response systems do not adapt to that level of distributed behaviour. »
- **[C69]** `2607.13087v1.pdf` p. 8 : « Diffuse threat models spread out over time could be harder for the hypothetical AI adversary to pull off, because they require more coordinated behaviour, but could also be harder to detect because the actions are spread out. »
- **[C70]** `2607.13087v1.pdf` p. 5 : « there could be many thousands or millions of untrusted AI agents within a single company »
- **[C71]** `2607.13087v1.pdf` p. 25 : « The second, more speculative approach is monitoring of internal model activations »
- **[C72]** `2607.13087v1.pdf` p. 25 : « Assurance: As mentioned, assurance for activations monitoring remains an open problem. »
- **[C73]** `2607.13087v1.pdf` p. 32 : « Distributed attack simulation (speculative). »

La surveillance des activations est rangée au niveau de détection le plus haut (D4), avec la détection d'anomalies à l'échelle du système (page 20). Aucune statistique d'agrégation dans le temps ou entre instances n'est proposée ni évaluée. Aucune occurrence de test séquentiel.

**Verdicts.** H1, H2, H3, statistique de population : **libres dans cette pièce** (aucune mesure). Bascule : **non déclenchée.** Lecture utile : la pièce dit que le problème est ouvert et important chez un grand laboratoire, et que le point dur des sondes est l'**assurance** (prouver que la méthode marche sans vérité de terrain). C'est notre H8 et notre porte de validité, pas une collision.

### 2.7 StateWitness — 2606.17478v1 (16 juin 2026)

**Qui.** Université du Zhejiang, Université Griffith (page 1).

**Quoi.** Un « décodeur d'activations » : un second modèle lit les états cachés du modèle cible et répond à des questions d'audit. Deux modèles cibles (GPT-OSS-20B, Gemma4-26B-A4B-IT), sept jeux de tromperie, dont du désalignement agentique et de la sous-performance volontaire. Comparé à quatre sondes linéaires et à trois moniteurs boîte noire sur le texte, **avec des seuils calibrés à 1 % et 5 % de fausses alarmes sur une distribution de contrôle** (page 6).

- **[C74]** `2606.17478v1.pdf` p. 1 : « reaches 0.916 mean AUROC, a relative gain of 11.6% over the best black-box text monitor and 25.0% over the best activation-probe baseline under the same evaluation protocol »

**Mais à 1 % de fausses alarmes, le tableau s'inverse** (tableau 3, page 7 ; colonnes : aire sous la courbe, rappel à 1 %, rappel à 5 %) :

- **[C75]** `2606.17478v1.pdf` p. 7 : « Best linear probe 0.705 0.006 0.040 »
- **[C76]** `2606.17478v1.pdf` p. 7 : « Best black-box 0.809 0.307 0.547 »
- **[C77]** `2606.17478v1.pdf` p. 7 : « STATEWITNESS 0.920 0.293 0.681 »
- **[C78]** `2606.17478v1.pdf` p. 7 : « Best black-box 0.821 0.502 0.622 »
- **[C79]** `2606.17478v1.pdf` p. 7 : « STATEWITNESS 0.916 0.326 0.628 »
- **[C80]** `2606.17478v1.pdf` p. 7 : « Low-FPR recall is more mixed. »

([C75] à [C77] : GPT-OSS-20B ; [C78], [C79] : moyenne des deux cibles.) Et, jeu par jeu, sur le désalignement agentique avec GPT-OSS-20B (tableau 14, page 30 ; triplets : exactitude équilibrée, rappel à 1 %, rappel à 5 % ; colonnes : sonde d'activation, moniteur boîte noire, StateWitness) :

- **[C81]** `2606.17478v1.pdf` p. 30 : « Agentic 0.500/0.000/0.000 0.776/0.571/0.714 0.500/0.000/0.786 »

**Agrégation.** Par réponse (moyenne sur le segment de la réponse finale pour les sondes, page 25). Aucune accumulation dans le temps. Limites dites :

- **[C82]** `2606.17478v1.pdf` p. 9 : « Larger models or longer-horizon agents may expose different failure modes, require different audit queries, or shift the calibration regime. »
- **[C83]** `2606.17478v1.pdf` p. 9 : « The audit decoder is not a calibrated decision rule. »

**Verdicts.**
- H1 : **occupée en partie.** Fait : boîte blanche contre boîte noire, à 1 % et 5 % de fausses alarmes calibrées sur un contrôle bénin, y compris sur du désalignement agentique et de la sous-performance. Non fait : sabotage diffus sur une trajectoire ; tâches floues ; agrégation séquentielle égale des deux côtés ; intervalles de confiance (la pièce dit page 32 qu'elle n'en rapporte pas).
- H2, H3, statistique de population : **libres dans cette pièce.**
- Bascule : **non déclenchée.**

## 3. H2, composante par composante

Énoncé retenu (N-007) : sur des trajectoires où chaque action sabotée reste sous le seuil d'un moniteur par action calibré à 1 % de fausses alarmes, l'accumulation additive toujours valide de scores de sondes de l'agent qui agit détecte le sabotage avec un rappel qui croît avec l'horizon ; seuil calibré sur des épisodes honnêtes, sans exemple de sabotage.

| Composante | 2512.07810 | HELIOS v5 | Kulkarni | SafeDream | Gao | Feuille de route | StateWitness |
|---|---|---|---|---|---|---|---|
| (1) Scores de sondes internes | oui (p. 16) | oui (p. 15) | en partie : traits de trajectoire d'activations, pas un score de sonde (p. 3) | oui : score de risque appris sur l'état caché (p. 4) | oui (p. 5) | non (aucune mesure) | oui (p. 6) |
| (2) De l'agent lui-même | oui, mais modèle évalué, pas un agent en contrôle | oui, un capteur par agent (p. 11) | oui, le modèle surveillé | oui, le modèle surveillé | oui, l'agent Qwen2.5-7B (p. 5) | — | oui, le modèle cible |
| (3) Accumulation séquentielle | non : moyenne sur les jetons (p. 16) | non : un scalaire par exécution (p. 15, 16) ; annoncée (p. 3, 18, 19, 26) | en partie : longueur de chemin cumulée comme trait (p. 3) | **oui : somme de Page (p. 5)** | non : maximum par unité (p. 3) | non | non |
| (4) Garantie de fausse alarme valable à tout instant | non (p. 27) | non ; visée au conditionnel (p. 26) | non ; seuil 0,5 fixe (p. 3) | non ; optimalité citée, taux mesuré 6,6 à 8,0 % (p. 5, 7) | non : garantie marginale par unité, le séquentiel est renvoyé à plus tard (p. 3, 4, 8) | non | non |
| (5) Sabotage diffus, chaque action sous le seuil par action | non : sous-performance installée par réglage fin | non : collusion instruite, lue au dernier tour | non : attaque de l'utilisateur ; tours « d'apparence bénigne » (p. 2) | en partie : « faible et bruité » par tour, affirmé, non mesuré contre un moniteur par action à 1 % ; menace = utilisateur (p. 3, 4) | non : injection subie par l'agent | nommé comme menace (p. 2, 8), non mesuré | non |
| (6) Rappel croissant avec l'horizon | non | non | en partie : détection précoce croissante avec la longueur d'approche (p. 5) | non trouvé ; dialogues d'environ 5 tours (p. 14) | non ; le rappel baisse quand le nombre d'essais monte (p. 11) | non | non |

**Lecture.** Aucune pièce ne réunit (3), (4) et (5). La conjonction qui reste non trouvée dans ce lot est : *accumulation additive* **et** *garantie uniforme sur l'horizon, calibrée sur épisodes honnêtes seuls* **et** *sabotage par l'agent, sous le seuil par action*. Les composantes (1), (2) et (3) prises ensemble sont publiées (SafeDream). L'originalité de H2 ne tient donc plus qu'à (4), (5), (6) et à leur réunion — ce que N-007 avait déjà anticipé en retirant « l'application aux sondes internes » des revendications. SafeDream ne figure pas dans les motifs de N-007 ; il devrait y figurer à côté de *Doomed from the Start* et d'E-valuator.

## 4. La bascule (programme, sections 13 et 16)

Texte : « Publication externe du cœur séquentiel sur sondes (équipe Oxford/NYU de NARCBench, équipe boîte blanche de l'institut britannique) → bascule vers l'épidémiologie de population et la curation de données. »

- **HELIOS v5 : non.** Aucune statistique séquentielle ; quatre annonces, inchangées depuis la v3 ; une intégration d'outillage annoncée. Je n'ai pas vérifié le dépôt de code de HELIOS ni « Orbit » (réseau fermé) : si une statistique séquentielle y était déjà codée sans être dans le papier, je ne le verrais pas. **Piste, non vérifiée.**
- **Institut britannique (2512.07810) : non.** Moyenne sur les jetons, aucune garantie, et un échec des sondes sur la tâche agentique.
- **Autres pièces : non au sens des auteurs nommés.** SafeDream réalise le squelette « somme cumulée sur scores internes » sur une autre menace, sans garantie.
- **Remarque sur le texte de la bascule** (sans rien modifier) : il dit « Oxford/NYU ». Les affiliations de la v5 sont Oxford, ELLIS Tübingen, Witt Lab et University College London (page 1). Je n'ai trouvé aucune affiliation à New York dans la v5.

**Niveau de menace.** Élevé et daté. L'équipe de NARCBench écrit que le séquentiel est sa « prochaine étape naturelle » et le premier item de ses travaux futurs ; elle a déjà la référence de méthode (inférence sûre valable à tout instant, Howard et collègues, Ramdas et collègues) et le banc. Entre la v3 et la v5, en deux semaines, rien n'a bougé sur ce point.

## 5. Contre-résultats défavorables au programme, et la phrase à dire à un jury

1. **Les sondes échouent sur le saboteur agentique étroit, chez l'institut britannique.** [C05], [C08], [C09]. Et sur une tâche, le signe est inversé : [C06].
   *Phrase :* « Le seul jeu d'audit à l'aveugle publié montre que des sondes de tromperie n'ont rien vu sur un saboteur limité à une tâche agentique, et que l'équipe rouge l'avait prévu parce que le signal se dilue sur une longue trajectoire ; notre hypothèse est que l'accumulation répare cela, et ce n'est pas démontré. »

2. **Des comportements bénins font tirer les sondes, et le calibrage de contrôle peut accuser un innocent.** [C07], [C10].
   *Phrase :* « Des tics de style installés exprès ont suffi à produire des faux positifs que l'équipe bleue n'a pas su corriger ; une garantie de fausse alarme calibrée sur des épisodes honnêtes ne vaut que si ces épisodes ressemblent au déploiement. »

3. **À 1 % de fausses alarmes, la boîte noire bat la boîte blanche sur du désalignement agentique.** [C81] (0,571 contre 0,000 et 0,000), [C75] à [C79].
   *Phrase :* « Sur un banc publié, au point de fonctionnement même de notre porte, un juge sur le texte rappelle 57 % des cas agentiques quand la sonde linéaire et le décodeur d'activations en rappellent 0 % ; le gain boîte blanche en aire sous la courbe ne se transporte pas au seuil strict, et H1 peut échouer. »

4. **Un seuil certifié ne tient pas d'un jeu à l'autre, et l'activation n'ajoute rien à un bon observateur sur un agent avec outils.** [C60], [C61], [C62], [C63].
   *Phrase :* « Sur AgentDojo, un seuil réglé pour 10 % de fausses alarmes, avec une borne à 95 %, en a réalisé 18,7 % au test, et la sonde n'a rien ajouté à un observateur textuel fort ; nos garanties sont conditionnelles à l'échangeabilité entre calibrage et test, et nous devons mesurer le transport. »

5. **Le taux par action se compose.** [C64].
   *Phrase :* « Cinq pour cent par action font quarante pour cent par épisode de dix actions ; un moniteur par action calibré à 1 % n'est donc pas un moniteur d'épisode à 1 %, et nos comparaisons doivent être faites à l'unité de l'épisode. »

6. **Le rappel boîte blanche à seuil strict est bas, et la détection se dégrade quand on double le nombre d'agents.** [C34] (0,38 à 1 %), [C38] et [C39] (0,88 à 4 agents, 0,737 au mieux à 8 agents).
   *Phrase :* « Le meilleur détecteur boîte blanche publié sur la collusion ne rappelle que 38 % à 1 % de fausses alarmes hors distribution, et il perd quinze points d'aire sous la courbe de 4 à 8 agents ; rien de publié ne dit que la courbe boîte blanche domine la boîte noire quand le nombre d'agents croît. »

7. **Les sondes entraînées sur de la collusion instruite ne transfèrent presque pas à la collusion émergente.** [C28] ; tableau 1 de HELIOS, page 18 (trois méthodes sur cinq au niveau du hasard).
   - **[C84]** `2604.01151v5.pdf` p. 18 : « mixed result, three probes perform no better than chance, »
   *Phrase :* « Nos saboteurs sont instruits ; le seul test publié de transfert vers un comportement non instruit donne trois détecteurs sur cinq au hasard. »

8. **Une sonde apprise sur du synthétique peut alarmer sur presque tout le réel.** [C44], [C45].
   *Phrase :* « Un détecteur de trajectoire d'activations, entraîné sur des données synthétiques, a donné 99,1 % de fausses alarmes sur des conversations réelles. »

9. **L'accumulation publiée la plus proche n'atteint pas un taux de fausses alarmes bas.** [C52], [C53].
   *Phrase :* « La seule somme cumulée publiée sur des scores internes tourne à 7 ou 8 % de fausses alarmes, sur des dialogues de cinq tours ; personne n'a montré qu'elle tient à 1 % sur de longs épisodes. »

10. **Le seuil fixe chute quand les agents se savent surveillés** (rapporté par HELIOS à propos de Das et collègues ; non vérifié par moi sur la pièce de Das).
    - **[C85]** `2604.01151v5.pdf` p. 3 : « although fixed-threshold recall can drop sharply »

**Réserve R4.** Ces contre-résultats viennent presque tous de sondes **par réponse**, sans accumulation. Ils ne réfutent pas H2 ; ils disent que le matériau que H2 accumule est faible et fragile. Lire cela comme « donc l'accumulation est nécessaire » serait la lecture qui nous arrange : elle reste une hypothèse.

## 6. Synthèse par énoncé

- **H1 (gain boîte blanche sur boîte noire, sabotage diffus, tâches floues, agrégation et fausses alarmes égales).** Occupée en partie par cinq pièces, chacune sur un morceau : comparaison blanc contre noir à fausses alarmes calibrées (StateWitness, Gao), sur de la sous-performance (institut britannique, qualitatif), sur de la collusion stéganographique (HELIOS). **Non trouvé dans ce lot :** la mesure sur du sabotage diffus et des tâches floues, à agrégation séquentielle égale des deux côtés. Le signe attendu n'est pas acquis : deux pièces sur trois qui mesurent à seuil strict donnent un gain nul ou négatif sur le cas agentique.
- **H2.** Voir la section 3. Occupée en partie ; la conjonction (3) + (4) + (5) n'est pas trouvée.
- **H3 (courbe de sécurité en fonction du nombre d'agents, blanc contre noir, budget constant).** Occupée en partie par HELIOS seulement : deux points (4 et 8 agents), boîte blanche seule, sans budget constant, avec une dégradation. Non trouvé : la courbe comparée et la domination.
- **Statistique de population / spatio-temporelle.** La coupe transversale entre agents est occupée par HELIOS (assumée comme base par le programme). La co-élévation dans le temps entre copies à poids partagés, et toute statistique spatio-temporelle, ne sont pas trouvées dans ce lot. HELIOS reconnaît que ses tests supposent l'indépendance entre agents.
- **Bascule.** Non déclenchée. Annoncée par l'équipe de NARCBench.

## 7. Pièces à lire ou à récupérer

Déjà dans `docs/sources/pdf/` (vérifié par `ls`), **survolées seulement** (première page et recherche de mots) — à lire en entier par un lot, car elles touchent H2 :

- `2607.02510v1.pdf` (empreinte `eefdaeaec17c3b16`) — Schirmer et collègues, « Online Safety Monitoring for LLMs », 2 juillet 2026. Le résumé parle d'un moniteur en temps réel qui seuille un signal de vérificateur « d'un modèle externe », calibré par contrôle du risque, et se dit compétitif avec des moniteurs à test séquentiel ; l'annexe décrit un « e-valuator-anytime » à garantie valable à tout instant (pages 11 et 12, survol). **Piste, non opposable :** à vérifier si l'un des signaux est une sonde d'activations de l'agent ; si oui, c'est la collision la plus sérieuse sur (3) + (4).
- `2606.06223v2.pdf` (empreinte `a95da1d590044f0a`) — Wilhelm et Kao, « From Reward-Hack Activations to Agentic Risk States », 15 juillet 2026. Scores d'activation de l'agent qui agit, dans des trajectoires d'agent, pour prédire le risque de l'action suivante ; le résumé dit que l'activation seule ne suffit pas. **Piste, non opposable** : contre-résultat probable pour H1, à lire.
- `2607.06807v1.pdf` — « When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems » (ICML 2026, d'après la bibliographie de Gao, page 9). Touche H3 et la statistique de population. Non ouverte par moi.

À récupérer sur le réseau (absentes du dossier, vérifié par `ls`) :

- arXiv 2603.04069 — Wilhelm, Wittkopp, Kao, « Monitoring Emergent Reward Hacking During Generation via Internal Activations ». Pourquoi : signaux d'activation suivis pendant la génération ; Gao la range parmi les « signaux temporels ».
- arXiv 2605.28553 — Collu et collègues, « Refusal Before Decoding ». Même motif (signal temporel sur activations).
- HELIOS v1, v2 et v4 (arXiv 2604.01151). Pourquoi : dater la première annonce du séquentiel, et vérifier qu'aucune version intermédiaire ne contient un essai retiré ensuite.
- Le dépôt de code de HELIOS et « Orbit » (Hagag et collègues, 2026, cité page 19 de la v5). Pourquoi : vérifier qu'aucune statistique séquentielle n'y est déjà livrée.
- Shi et collègues, 2026 (environnement « Verdict », cité page 18 de la v5 ; identifiant non relevé). Pourquoi : dix tours par exécution, donc le terrain naturel d'une suite séquentielle de l'équipe.
- Howard, Ramdas, McAuliffe, Sekhon, « Time-uniform, nonparametric, nonasymptotic confidence sequences » (cité page 26 de la v5 comme moyen). Pourquoi : c'est la méthode que l'équipe de NARCBench dit vouloir employer ; notre garantie doit s'y comparer.

## 8. Contrôle des citations et refus

- Citations contrôlées par le script : **88**. Échecs : **0** (voir la sortie consignée ci-dessous, relevée après la dernière écriture du rapport).
- Essais du script (R5) : cas juste retrouvé ; cas altéré (un chiffre changé) refusé.
- Refus rencontrés : aucun. Aucun appel de modèle, aucune machine, aucune dépense, aucune requête sur le réseau. Aucun fichier interdit ouvert. Rien d'écrit dans le dépôt hors de ce rapport et de son empreinte compagnon.
- Aucune hypothèse, aucune revendication, aucun document existant n'a été modifié.
