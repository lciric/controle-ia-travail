# Contre-lecture du catalogue de la matière première de l'auto-conception de l'organisme d'idéation — v1

Écrite le 18 novembre 2026 par un contre-lecteur neuf (règle R2), d'un autre modèle que le rédacteur : je n'ai écrit ni le catalogue, ni le relevé, ni les lots, ni leurs programmes. Aucune dépense, aucun appel de modèle externe, aucune clé, aucun commit, aucune poussée, rien dans `registres/`. Aucun résultat de 7a, 7b, T0.6, de l'étape B ni de l'étape B bis n'a été ouvert. Les lectures 01, 06, 10 et 11 de la veille, la section 5.4 de la lecture 03 et la pièce privée sur TASTE n'ont pas été ouvertes. Les deux familles exclues (conception d'organismes saboteurs discrets ; évasion des moniteurs, bras d'attaque, attaque de Goodhart du juge) ne sont citées ici que par « exclue » et un emplacement.

Pièce contre-lue : `docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v1.md` (sha256 `98f63ecc2820a77fb8e36eabd7ad1a0f7d11f94da1a23a7e503b0e1cc67f6fc3`, 2 390 lignes).

## 0. Verdict

**À corriger.** Le socle tient : les quatre programmes se rejouent à l'octet, les comptes sont exacts, les 1 749 empreintes citées par le relevé sont justes, et sur quarante travaux tirés au hasard aucun mécanisme n'est inventé. Mais la pièce, servie telle quelle à des proposeurs, porte quatre défauts de fait qui se propageraient dans la conception :

1. **La section 3 présente comme « hors de toute machine » des idées que des machines de la section 2 portent déjà** : la phrase « dont le relevé ne trouve l'assemblage dans aucun des systèmes recensés » est fausse pour 12 des 37 regroupements de 3.1, d'après le relevé lui-même (section 4 ci-dessous). C'est exactement l'appât que la règle R8 interdit.
2. **Un mécanisme attribué à tort** : la machine de Darwin-Gödel figure sous « Crédit par la descendance et signaux de lignée » alors que la ligne du relevé (240.2) dit le contraire — elle sélectionne sur le score immédiat, et ce sont les auteurs de la machine de Huxley-Gödel qui le lui reprochent. Le point touche directement N-073 § 1.
3. **La section « ce que l'organisme fait déjà » n'est pas à la lettre de N-073 et de N-071** sur quatre points (liste des phrases interdites et citations obligatoires tronquées, deux indices contraires non nommés, réserves de N-071 absentes, héritage récompensé non rattaché à Wang et al.), et elle omet ce que N-059 et la décision sur la matière première des mentors disent des règles de course de l'organisme.
4. **Cloisonnement** : trois lignes du relevé relèvent d'une famille exclue et sont rangées dans le catalogue (exclue : 552.0, 552.1, 466.1) ; le relevé porte en plus une proposition de 259.3 et une source de 439.0 et 439.1 sous la même réserve.

S'y ajoutent des défauts circonscrits : cinq mécanismes connus par le seul titre comptés comme décrits, une définition de « machine » contredite par sa propre liste, une question ouverte fausse (n° 10), deux gloses de valeur, seize mécanismes oubliés dans dix travaux lus en profondeur, et des regroupements dont certains membres ne répondent pas au nom.

Les corrections sont de fait et circonscrites : **j'ai écrit la v2** (`matiere-premiere-v2.md`, sha256 `8fa11231ee97759a64f39100f13e973b3614d5dde5d6a4c88968a04bff7bc565`), produite par un programme neuf qui applique les corrections en mémoire aux mêmes entrées ; la v1 et le relevé restent intacts (R12). Le relevé lui-même n'est pas corrigé : une version 2 du relevé reste à écrire (correction 5).

## 1. Pièces lues et empreintes

Toutes les empreintes compagnons du dossier ont été vérifiées par `sha256sum -c` (lots 01 à 21, relevé, catalogue, programmes, sorties, regroupements, première contre-lecture) : toutes conformes ; de même pour le dossier de la veille.

| Pièce | Empreinte (sha256) |
|---|---|
| `matiere-premiere-v1.md` | `98f63ecc2820a77fb8e36eabd7ad1a0f7d11f94da1a23a7e503b0e1cc67f6fc3` |
| `releve-mecanismes-v1.json` | `1110ef784e5c628dc2017e9aab1abbd57ca10ba784ecb4f18d2c732bdc453faa` |
| `programmes/corrections-v1.json` | `7b129cffe729c29805c613fd66c86c33160829d255602dc661d0f96d4fe68890` |
| `programmes/fusionner_v1.py` | `8935d5096dbca729a70d900069547577622fa55dc834b398fd3eac5be11efe60` |
| `programmes/ecrire_matiere_v1.py` | `ab7b2cefd4245f882b7b10b98eee02b97e10277b372592c850b24645f1a092c8` |
| `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json` | `aa3ac9b8e962c496b89f67051ef5c60094aa3d18405e8779ab3e34a33a6010d2` |
| Lecture 02 (indice 450) | `bf8cd30787a5c491411331db18dc75188b98729d1ede63e823c01d2e3a630762` |
| Lecture 03 (indice 57 ; sections 0 à 5.3 et 5.5 à 8) | `2775dc89cfd1f68f27835a160c3988ff76d966ed94bfe9a357f2a5d4d2a70f3a` |
| Lecture 04 (indice 121) | `4d6b1da46c36f34a1caad777c28f7517412b2dab96124a9e355aa54c64ad06c0` |
| Lecture 05 (indice 593) | `ec5b3475bdd4bb8792a3404925e2e2548d715deb98007c02afa9253bcb6abc2b` |
| Lecture sur la machine de Huxley-Gödel, v2 | `cb8f9ea395901a7b1de3c588e97b1e3a56f4a78b233d19850e3e6456063907bd` |
| Lecture 08 (indice 112) | `d00ab8b87d5c41e4f75a3756615bcf8967652436b10e621a595a1495c8de1bc7` |
| Lectures 07, 09, 12 (indices 581, 456, 98), sections « ce que le travail fait » et « mesuré » | compagnons conformes |
| PDF de Fork-and-Flush, `citations-arxiv-2610.07447v1.pdf` (p. 1 à 6, par extraction de texte) | `4eba26a1e744bcb4cb1f748aea062f7120dd796aa7f319e675b3690586242741` |
| PDF « Scaling Discovery Requires Forgetting », `citations-arxiv-2610.20563v1.pdf` (p. 1 à 7) | `9c14df8357e1fb46caa8349e6225d502180ee74c20c62d5af97ec29cd4285edc` |
| Résumés d'OpenReview versés, `grise-openreview-resumes-retenus-v1.json` | compagnon conforme |
| Décisions N-044, N-045 v2, N-049, N-050, N-053, N-058, N-059, N-064, N-065, N-067 (§ 4 points 1, 2, 5 à 7 ; § 6), juge au nul (N-071), matière première des mentors (N-072), N-073 | compagnons conformes ; empreintes recopiées dans la v2, section 4 |

Les PDF ont été traités en données non fiables, lus par `pdftotext` ; tout Python qui lisait des pièces a tourné avec `-I`.

## 2. Comptes, rejoués et recomptés par programme

**Rejeu à l'octet**, dans une copie de travail hors du dépôt (les dossiers de la veille, des décisions et des sources reliés en lecture seule) : `construire_lot21_v1.py` rend un `lot-21.json` identique ; `construire_corrections_v1.py` rend un `corrections-v1.json` identique (541 lignes) ; `fusionner_v1.py` rend un relevé et une sortie identiques ; `ecrire_matiere_v1.py` rend un catalogue et une sortie identiques. Seule remarque : la sortie dit « 2033 lignes » ; c'est le nombre de blocs écrits, le fichier en compte 2 390 (363 699 caractères, dont les 361 666 annoncés plus les sauts de ligne).

**Recompte indépendant** (mon propre code, sur le relevé et sur les lots bruts) : tout est conforme à la section 0 du catalogue.

| Compte | Valeur |
|---|---|
| Travaux | 630 ; 592 avec au moins un mécanisme ; 38 sans (20 « exclue », 12 « hors sujet », 3 « liste sans mécanisme », 3 « notice muette ») |
| Mécanismes | 1 106 = 1 098 des lots − 2 retirés + 10 ajoutés ; 899 décrits, 207 suggérés par le titre |
| Décrits par famille | exploration 188 ; originalité 84 ; épreuve 190 ; jugement 141 ; mémoire 93 ; sélection 80 ; coût 69 ; auto-conception 35 ; autre 19 |
| Décrits par « éprouvé contre le réel » | oui, mesuré 476 ; oui, affirmé 124 ; non 70 ; inconnu 229 |
| Travaux par profondeur | lecture approfondie 8 ; page ou résumé 459 ; notice seule 163 |
| Mécanismes suggérés par profondeur du travail | notice seule 194 ; page ou résumé 13 |
| Travaux « notice seule » | 163 : 194 mécanismes suggérés, 29 décrits (section 1), 16 travaux sans mécanisme |
| Question 1 (regroupements sans « oui, mesuré ») | 13 sur 103 : conforme |
| Question 2 (machines) | 81 « oui, mesuré » sur 176 : conforme |
| Section 7 et section 8 | 19 lignes « autre » ; 38 travaux : conformes |
| Empreintes citées par le relevé | 1 749 citations sur 42 fichiers : toutes justes, aucun fichier absent ; chaque mécanisme porte au moins une empreinte |

**Défaut de compte trouvé** : le filtre qui a séparé les mécanismes « suggérés par le titre » (correction 3 de la première contre-lecture, expression `seul titre|d.après le titre|suggér`) laisse passer cinq mécanismes connus par le seul titre, comptés comme décrits : 126.2 (« Le titre dit les agents « auto-améliorants » »), 236.2 (« Économie d'échantillons revendiquée par le titre » ; table : « titre seul »), 391.0 et 391.1 (« Le titre annonce… » ; table : « titre seul, retenu par filtre lexical »), 445.0 (« connu par le titre seul »). Dix-huit autres phrases contiennent le mot « titre » (dix-sept citent le titre en plus d'une notice ou d'une ligne de veille, une dit « tenant du titre ») : elles restent décrites à bon droit.

**Défaut de traçabilité, mineur (R6)** : 1 703 chemins sont cités dans les sources du relevé sans empreinte propre, dont 1 692 lignes des quatre fichiers de recherche de la veille (« recherche-mots-cles-v1.md:20 » et semblables, lots 01 à 20) ; elles sont vérifiables par les compagnons de ces fichiers, et la table qui les porte est empreintée. Les onze autres : lecture 04 (6), page versée de TasteVal (2), lecture 01 (2, voir section 8), lecture 02 (1).

## 3. Tirage de quarante travaux

**Dérivation (R9)** : `numpy` 2.4.6 ; graine de la tâche `numpy.random.SeedSequence(20261118, spawn_key=(3673168503,))`, où 3673168503 est le `zlib.crc32` de la chaîne `contre-lecture-catalogue-v1` (la racine 20261118 est celle demandée, la clé sépare cette tâche du tirage de la première contre-lecture) ; deux enfants par `.spawn(2)` ; l'enfant 0 sert ici : `numpy.random.default_rng(enfant0).choice(vivier, 40, replace=False)`, où `vivier` est la liste croissante des 592 indices qui portent au moins un mécanisme.

**Tirés** : 34, 35, 49, 81, 109, 120, 151, 152, 153, 158, 172, 201, 221, 222, 232, 234, 253, 290, 299, 320, 335, 358, 359, 376, 384, 403, 426, 427, 430, 433, 461, 529, 531, 537, 552, 556, 557, 575, 582, 613 (65 mécanismes relus, dont 10 suggérés par le titre).

**Méthode** : chaque mécanisme comparé à l'entrée de la table (`fait`, `touche`, `mesure`, `lu`), puis aux lignes de veille citées, puis, quand le relevé le dit, au résumé d'OpenReview versé (556, 557 : chiffres retrouvés à l'identique) ou à la lecture citée (582 : « la profondeur sature tôt », p. 3, et la ligne « meilleur de N sans évolution », figure 4 p. 7, retrouvées dans la lecture 07).

**Résultat** : 33 travaux sans remarque ; aucun mécanisme inventé ; familles justes partout sauf un cas discutable ; statut « éprouvé » cohérent avec la table ou la lecture dans les 40 travaux. Remarques :

- **552** (*The Placebo Improvement*) : **exclue** — relevé, `travaux[552]`, mécanismes 552.0 et 552.1 ; catalogue v1, lignes 553, 775, 1791 et 1975 (section 8 ci-dessous).
- **613.0** (*The Ringelmann Effect…*) : « compter les agents confond coût et preuve indépendante » est donné comme « affirmation des auteurs d'après la notice » ; c'est la glose de la recherche adverse de la veille (champ « touche »), non la notice des auteurs. Mauvaise attribution, à corriger dans le relevé.
- **172.0** (*Causal Discovery Bench*) : « on mesure si les expériences choisies sont efficaces » vient du titre ; la notice dit seulement « banc d'expériences causales conduites par agents ». Glose non marquée.
- **221.0** (*A Vocabulary for Multi-Agent Automated Research Systems*) : « utile pour nommer rôles et compositions » est un jugement de valeur du relevé, affiché en section 7 du catalogue (de même 457.0, « utile seulement comme porte d'entrée bibliographique », hors tirage).
- **151.0** (*Learning to Ideate for Scientific Impact*) : l'entraînement de l'idéateur sur un signal différé est rangé en « sélection » ; il répond mieux à « exploration n° 13 — Entraînement de l'exploration » ; « comme la note d'un juge » est une glose (la notice dit « mandataires immédiats »).
- **152.0** (*IdeaTrail*) : un jeu de trajectoires est rangé sous « mémoire n° 3 — … conservé et lu par le contrôleur ou le proposeur » ; la notice ne dit pas que quiconque le lit.
- **299.0** (*Scientific discovery as meta-optimization*) : l'optimisation du critère d'évaluation est rangée avec les procédures d'amélioration modifiables (« auto-conception n° 3 ») ; ce sont deux idées différentes.

## 4. Regroupements

**Tirage** : les 37 regroupements de la section 3.1, plus 20 tirés parmi les 66 de la section 3.2 (pour que les 57 soient distincts) par `numpy.random.default_rng(enfant1).choice(66, 20, replace=False)`, les 66 pris dans l'ordre du catalogue : sélection n° 4, originalité n° 1, exploration n° 3, sélection n° 8, sélection n° 1, exploration n° 9, coût n° 4, mémoire n° 11, mémoire n° 1, auto-conception n° 6, mémoire n° 7, épreuve n° 7, originalité n° 2, exploration n° 8, jugement n° 8, coût n° 9, exploration n° 10, mémoire n° 4, exploration n° 7, épreuve n° 8. Pour chacun, toutes les phrases du relevé ont été relues.

**Listes de travaux** : justes. Elles sont produites par programme à partir du relevé (rejeu à l'octet) ; chaque titre affiché porte bien l'identifiant du regroupement ; les marques « machine » et les comptes de 3.2 sont exacts.

**« Porté par aucune machine recensée » : faux pour 12 des 37 regroupements de 3.1.** La section 3 calcule seulement qu'aucun travail rangé sous le regroupement n'est une machine ; comme chaque mécanisme n'est rangé qu'une fois, une machine qui porte la même idée sous un regroupement voisin n'est pas vue. Preuves, phrases du relevé :

| Regroupement de 3.1 | Même idée chez une machine de la section 2 (identifiant, rangé sous) |
|---|---|
| exploration n° 4 — conditionnement du proposeur | 259.0 *Automated Weak-to-Strong Researcher* : « une direction de recherche distincte, courte et vague, assignée à chaque agent » (exploration n° 8) ; 128.0 *Distill, Debate, Discover* : expertise distincte servie à chaque agent (exploration n° 8) |
| exploration n° 11 — diagnostics de l'effondrement de la diversité | 30.0 *SwarmResearch* : convergence vers une seule approche (exploration n° 10) ; 513.0 *Wright–Gödel Machine* : la sélection des parents homogénéise l'archive (sélection n° 5) |
| originalité n° 5 — diversité et homogénéité | 513.1 : diversité de l'archive suivie et protégée (mémoire n° 2) ; 13.4 *Fork-and-Flush* : carte des bassins d'idées (originalité n° 1) |
| épreuve n° 2 — vérité prise dans le futur | 441.0 *Propose, Don't Judge* : chaque facteur noté « sur les seuls rendements révélés après son dépôt » (jugement n° 8) |
| épreuve n° 12 — réfutabilité | 332.1 *An AI Scientist that Doesn't Drift* : résultats « énoncés sous forme falsifiable » (épreuve n° 9) |
| jugement n° 2 — juge face à une vérité différée | 441.0 (jugement n° 8) ; 550.1 *IdeaGraph* : « alignement avec la suite réelle de la lignée de citations » (jugement n° 9) |
| jugement n° 5 — validation d'un juge | 441.1 : l'arbitre éprouvé sur un « monde synthétique à vérité plantée » (épreuve n° 8) ; 104.0 *Triage-PiEvo* : essai sur mécanismes plantés (épreuve n° 1) |
| jugement n° 7 — juge ou vérificateur entraîné | 2.1 *Blind Variation, Selective Retention* : « un sélecteur appris sur les propositions déjà vérifiées » (sélection n° 7) |
| jugement n° 11 — audit d'intégrité des articles produits | 491.0 *scholar-loop* : vérification par programme des citations, chiffres et affirmations du texte produit (épreuve n° 9) |
| jugement n° 14 — critères de valeur autres qu'un avis de juge | 121.0 et 198.1 : écart de croyance (originalité n° 4) ; 576.0 *PACE* : test séquentiel par pari (sélection n° 3) |
| sélection n° 12 — dérives mesurées de la sélection | 513.0 (sélection n° 5) ; 576.1 : « auto-piratage statistique de la règle gloutonne » nommé (épreuve n° 8) ; 593.0 : choix glouton sur le score immédiat dénoncé (sélection n° 4) |
| coût n° 5 — témoin à calcul apparié | 136.0 *Dictionaries, Not Darwin* : « audit à budget d'appels strictement apparié » contre des tirages indépendants (épreuve n° 7) ; 13.3 : comparaison à budget égal au meilleur de N (coût n° 3) |

Ressemblances plus lâches : coût n° 13 et 126.0 (*Inventa*) ; mémoire n° 12 et 126.1 ; jugement n° 1 et 550.1 ; coût n° 7 et 13.3. Par ailleurs, sept regroupements de 3.1 contiennent un travail décrit comme un système complet mais absent de la liste des machines : originalité n° 7 (375), épreuve n° 3 (178), épreuve n° 10 (145), épreuve n° 14 (514), jugement n° 7 (66), coût n° 7 (129), auto-conception n° 9 (618).

**Même idée dans un regroupement** : 22 des 37 regroupements de 3.1 et 14 des 20 tirés en 3.2 sont sans remarque. Les autres ont au moins un membre qui ne répond pas au nom :

- **sélection n° 4 — Crédit par la descendance et signaux de lignée : 240.2 (machine de Darwin-Gödel) y est à contresens.** Phrase du relevé : « Selon les auteurs de la machine de Huxley-Gödel, cette machine développe de préférence les agents au meilleur score […] en supposant qu'un bon score annonce de bonnes modifications futures — supposition qu'ils contestent » ; même constat dans la lecture Huxley-Gödel v2, § 2 (p. 2 du PDF). En section 2.2, la ligne de la machine de Darwin-Gödel (ligne 1447 de la v1) lui fait donc « assembler » le crédit par la descendance. C'est l'erreur la plus lourde du catalogue : un proposeur y lirait que la machine de Darwin-Gödel porte déjà le principe que N-073 § 1 attribue à Wang et al.
- jugement n° 12 — relecteurs évalués contre les relectures humaines : 562.0 dit l'inverse (« par l'impact réalisé […] et non par l'imitation des humains ») ; il relève de jugement n° 2 ; 445.0 n'est connu que par son titre.
- mémoire n° 12 — dérives de la mémoire d'état : 472.2 (les liens retenus réensemencent la mémoire) est un mécanisme, non une dérive mesurée.
- épreuve n° 3 — redécouverte : 490.0 n'en est pas une (le relevé lui-même : « la direction est donnée », « exécution, pas idéation »).
- originalité n° 6 — contamination : 260.1 décrit un raccourci lexical d'un banc de jugement, non une contamination par les données d'entraînement.
- coût n° 10 — le coût entre dans la preuve : 472.3 nomme seulement un coût (« taxe de rêverie »).
- coût n° 7 — rendement décroissant mesuré : 129.1 dose le raisonnement coûteux, éprouvé « inconnu ».
- épreuve n° 13 — environnements et bancs : 169.0 est une méthode, non un banc.
- épreuve n° 10 — dispersion : 145.2 dit que tous les lancements sont rapportés ; ce n'est pas une mesure de dispersion.
- jugement n° 1 — préférences d'experts : 262.0 et 559.0 ont pour vérité des citations ou des suites documentées (vérité différée) ; 63.0 et 412.0 apprennent un goût ; 260.0 audite un banc par une règle triviale ; 51.1 porte des préférences partagées entre modèles juges.
- jugement n° 15 — évaluer l'ensemble ou le processus : seuls 522.0 et 523.0 répondent au nom.
- originalité n° 5 : 160.1 compare la nouveauté, non la diversité.
- sélection n° 8 : 534.1 est l'admission d'une croyance dans l'état, non le choix de la suite.
- mémoire n° 7 : 157.1, 309.0 et 524.1 sont des archives tirées de la littérature ou de dépôts, non une base partagée entre agents.
- Mineurs : épreuve n° 11 (98.4, noms neutres, garde contre la mémorisation) ; jugement n° 2 (422.0, 572.2) ; jugement n° 5 (555.1, étalonnage) ; exploration n° 10 (146.0, modèle descriptif de trajectoires humaines).
- Sous les mêmes réserves, hors des 57 regroupements relus en entier : 299.0 en auto-conception n° 3 (section 3) ; et, relevés en vérifiant les machines (section 5), mémoire n° 2 (« relu avant de proposer » : pour la machine de Huxley-Gödel, 593.4, l'arbre est lu par la règle de sélection, non par le proposeur, lecture 05 § 4) et exploration n° 14 (la notice de 254.0 ne dit pas « une seule lignée »).

Le décompte « sans remarque » ci-dessus compte aussi comme remarques les lignes exclues (jugement n° 5, jugement n° 13, épreuve n° 7) et les mécanismes connus par le seul titre (jugement n° 12, coût n° 9).

**Mêmes idées sous plusieurs familles** (doublons de lecture, à signaler aux proposeurs) : exploration n° 11 et originalité n° 5 ; coût n° 1, sélection n° 7 et jugement n° 7 ; épreuve n° 6 et épreuve n° 11.

## 5. Machines

- **Les quatre machines lues en profondeur** (593, 112, 121, 57) assemblent bien les mécanismes dits, d'après les lectures 05 et Huxley-Gödel v2, 08, 04 et 03 (hors 5.4). Pour 57, la facette exclue est absente et 57.3 dit à juste titre « sur des objectifs adossés à la vérité » pour la part retenue. Leurs oublis sont en section 7.
- **Les 57 machines de 2.2** : chaque « assemble » correspond au relevé (rejeu) ; trois rattachements faussent l'attribution : 240.2 (ci-dessus) ; 254.0 rangé sous « Un seul agent, une seule lignée » alors que la notice ne le dit pas ; 593.4 sous « relu avant de proposer ». 236.2 (ShinkaEvolve) et 126.2 (Inventa) ne sont connus que par le titre.
- **Définition contredite** : « qui assemble au moins deux mécanismes du relevé » (v1, ligne 1427), alors que sept machines n'en ont qu'un rangé : 133, 134, 139, 150, 397, 407, 452 (huit en v2 avec 236).
- **Provenance de la liste** : « La liste est celle du relevé » est inexact ; le relevé n'a aucune marque « machine » (inventaire des champs des 630 entrées) ; la liste est codée à la main dans `ecrire_matiere_v1.py` (`MACH_LUES`, `MACH_NOTICE`). ShinkaEvolve y figure deux fois (236 et 629). Au moins dix-huit travaux du relevé se décrivent comme des systèmes complets et n'y sont pas : 10, 66, 97, 108, 129, 140, 143, 145, 178, 212, 375, 400, 454, 455, 514, 583, 605, 618 (par exemple *EvoSci: A Bio-Inspired Multi-Agent Framework…*, *The Agentic Scientist: Orchestrating Coding Agents…*).

## 6. Langue de la pièce

- **Attribution** : la légende est juste (« oui, mesuré » = les auteurs disent avoir mesuré) ; les sections 1 à 3 n'affichent que titres et identifiants ; les noms de regroupements sont des résumés du rédacteur, dits comme tels. Questions ouvertes : la n° 7 (« ne trouvent pas de gain constant ») gagnait à dire « selon leurs auteurs » ; la n° 4 range l'avis d'experts sous « épreuve » alors qu'il est sous « jugement ».
- **Absences** : aucune formule « personne n'a fait » ; le seul vrai défaut est l'affirmation d'absence de la section 3 (section 4 ci-dessus).
- **Jugements de valeur** : deux gloses du relevé affichées en section 7 (221.0, 457.0) ; dans le relevé seulement : 62.1 (« constat utile à la conception »), 260.1 (« à opposer à tout juge »).
- **Question ouverte n° 10 fausse** (v1, ligne 2077) : « leurs mécanismes (section 6) » ; en fait 194 mécanismes des 163 travaux sur notice sont en section 6, 29 en section 1, 16 travaux n'en ont aucun.
- **Section 4 contre ses décisions** (relues une à une) : conforme sur N-044, N-045 v2, N-049, N-050, N-058, N-064, N-065, N-067 et sur N-073 § 2 à § 4 et § 7. Écarts :
  1. 4.3 § 1 (v1, ligne 2056) : la liste des phrases à ne plus écrire omet « la sélection gloutonne sur le score immédiat est trop courte », « exclure le bandit à un pas » présenté comme un apport, « le mérite d'une génération inclut ce que ses descendants obtiennent » et « ce qui conçoit est jugé sur plusieurs générations » quand ce qui conçoit est sélectionné (N-073, lignes 33 à 41) ; les citations obligatoires omettent la machine de Darwin-Gödel (arXiv 2505.22954), Robeyns, Szummer, Aitchison (arXiv 2504.15228) et Kirsch et Schmidhuber (2022), et « Schmidhuber et Zhao (1996, 1997) » confond deux pièces (1997 : Schmidhuber, Zhao et Wiering) (N-073, lignes 60 à 64).
  2. 4.3 § 5 : « à côté de deux autres déjà au dépôt » sans les nommer ; N-073 (lignes 130 et 131) les nomme (tirage au hasard, arXiv 2611.04420 ; a priori fixe sans modèle, CADS) ; la borne de terrain omet « aucune production d'idées, aucun modèle de frontière ».
  3. 4.1, juge statistique : « seule leur réunion reste revendicable » sans les réserves de N-071 (point 1 retenu « sous la réserve du point 3 […] et du point 11 » : défendabilité non tranchée, « libre hors du dépôt » non déclarable) ni la phrase prescrite du point 4.
  4. 4.1 : « héritage d'une génération récompensé » écrit comme un trait de l'organisme sans le rattacher à Wang et al. ; N-073 § 1 en fait un principe publié, à dire par sa lettre retenue.
  5. 4.1 : l'invariant de N-053 point 5 est cité sans dire que sa lettre porte une exception (qui relève d'une famille exclue : exclue).
  6. Omission (hors de la conformité stricte, mais la section s'intitule « ce que l'organisme fait déjà ») : N-059 (témoins en générations d'étalonnage, budget d'erreur par génération, banque de confirmation distincte, épreuve lue jusqu'au budget) et la décision sur la matière première des mentors (§ 1, point 2 : proposeurs de plusieurs familles, aiguilleur sur la forme seulement, juges croisés aveugles, mémoire anti-répétition, aucune promotion décidée par un modèle, verdicts et témoins jamais servis aux proposeurs).

## 7. Mécanismes oubliés dans dix travaux

Travaux : les huit à lecture approfondie permise (57, 98, 112, 121, 450, 456, 581, 593) et deux à PDF versé dont le relevé n'avait lu que les premières pages (10 et 13). Les oublis signalés par la première contre-lecture ont bien été ajoutés. Restent :

| Travail | Oublis (affirmations des auteurs selon la lecture citée) |
|---|---|
| 593, machine de Huxley-Gödel (lecture 05 § 5 ; lecture Huxley-Gödel v2 § 2) | épreuve du critère de sélection contre la productivité observée de la lignée, avec retrait de la cible contre la fuite (table 1 p. 8, annexe D p. 19) ; choix de l'agent rendu sur ses seuls résultats propres (p. 7) ; biais de l'exécution asynchrone et leur correctif (p. 17) ; différences emboîtées héritées (annexe F, p. 21) |
| 112 (lecture 08) | règle de pénalité sans effet de l'aveu des auteurs (p. 10), d'où un audit « ce mécanisme change-t-il une décision ? » ; transfert à d'autres modèles (annexe C, p. 26) ; un quart des réécritures rejetées meilleures sur le signal public (p. 26) |
| 121 (lecture 04) | la référence informée crée aussi des surprises (13,7 sur 200, p. 5) : elle n'est pas monotone ; similarité par paires discriminante, enveloppe convexe non (p. 8, 15) |
| 57 (lecture 03, hors 5.4) | borne de précision à 0,8 fois le bras comparé (p. 5-6) ; « panel au moins aussi informé que le générateur » (p. 16) |
| 450 (lecture 02) | probabilités déclarées mal étalonnées, pentes 0,36, 0,12, 0,11 (p. 12) |
| 13, Fork-and-Flush (PDF p. 5-6) | ablation : vidage seul 0,55, bifurcation seule 0,57, les deux 0,71, course unique 0,45 (tableau 2) ; calendrier fixe à 33 % et 66 % du budget, écarts-types 0,16 contre 0,26 et 0,21 |
| 10, « Scaling Discovery Requires Forgetting » (PDF p. 5-7) | le « réducteur » qui règle ce que l'agent voit et la session qu'il poursuit ; témoin « continuer ou oublier » depuis le même état plafonné (figure 4), 32 oublis sur 36 suivis d'un nouveau meilleur candidat |
| 98, 456, 581 | rien au-delà de détails |

Ces seize mécanismes sont versés, avec chemin, empreinte et page, en section 10 de la v2. La question ouverte n° 2 de la v1 (« absence d'ablation : indices 112 et 593 ») se lit avec l'ablation publiée de Fork-and-Flush.

## 8. Cloisonnement

- **Pièce privée sur TASTE** : aucune trace (ni son empreinte `f9aed18c…`, ni le dossier qui la cite) dans le catalogue, le relevé, les lots ou les corrections ; les lignes sur TASTE (258, 260) citent la page et le PDF publics et le billet public.
- **Travaux « exclue » de la section 8** : indice, statut et chemin seulement ; conforme.
- **Lignes qui relèvent d'une famille exclue, encore présentes** (même règle que les retraits 259.4 et 57 de la v1) :
  - exclue — relevé, `travaux[552]`, 552.0 et 552.1 (lignes 14539 et 14547 du fichier) ; catalogue v1, lignes 553, 775, 1791, 1975 ;
  - exclue — relevé, 466.1 (ligne 12387) ; catalogue v1, lignes 873 et 1840 ;
  - exclue — relevé, seconde proposition de 259.3 (ligne 7162) ; le catalogue n'en montre que l'identifiant (lignes 1315 et 1469) ;
  - lecture fermée — relevé, sources de 439.0 et 439.1 (lignes 11610 et 11618) : elles citent `lecture-01-v1.md:96`, que le relevé dit porter sur une pièce exclue ; la glose qui en venait a été retirée (correction 5), la source est restée ;
  - relevé, `travaux[57]`, champ « précision de lecture » : il annonce encore une phrase « reprise ci-dessous » qui a été retirée (correction 6).
- **Examinés et laissés** : 32.1 et 73 (champ « touche » : « banc de tricheurs ») décrivent un audit de fabrications et un protocole de certification, sans tricheur conçu ; 605, 626, 627 relèvent selon la table des revendications 6, 10 et 11, non d'une famille exclue ; 4.3 § 4 reprend la lettre de N-073.

## 9. Corrections demandées

1. **Section 3** : dire ce que le programme calcule et signaler, sous chacun des douze regroupements, la machine qui porte la même idée (preuves : section 4). — *Fait en v2.*
2. **240.2** hors de « Crédit par la descendance » (preuve : phrase du relevé ; lecture Huxley-Gödel v2, § 2). — *Fait en v2 : rangé en sélection n° 5.*
3. **562.0** vers jugement n° 2 ; **472.2** vers mémoire n° 7 (preuves : section 4). — *Fait en v2.*
4. **Cinq mécanismes connus par le titre** (126.2, 236.2, 391.0, 391.1, 445.0) comptés à part. — *Fait en v2 (section 6, comptes recalculés) ; à porter au relevé.*
5. **Cloisonnement** : 552.0, 552.1, 466.1 hors du catalogue ; dans un relevé v2, retirer ces trois lignes, la seconde proposition de 259.3, la source `lecture-01-v1.md:96` de 439.0 et 439.1, et la phrase périmée du champ de 57. — *Catalogue : fait en v2 ; relevé : à faire, hors de mon mandat. D'ici là, le relevé v1 ne se sert pas aux proposeurs (la v2 le dit en section 0 et 9).*
6. **Section 2** : définition (« au moins un mécanisme décrit »), provenance de la liste, doublon ShinkaEvolve, systèmes non recensés nommés. — *Fait en v2.*
7. **Section 4** : écarts 1 à 5 de la section 6 ci-dessus, et ajout de N-059 et de la décision sur la matière première des mentors. — *Fait en v2.*
8. **Section 5** : question 10 réécrite avec ses comptes ; question 4 et question 7 précisées. — *Fait en v2.*
9. **Gloses** : 221.0 et 457.0 retirées à l'affichage (v2) ; dans le relevé v2 : 62.1, 260.1, 613.0 (attribution), 172.0, 151.0 (« comme la note d'un juge »), et les préfixes « Autre — » restés dans 146.0, 485.0, 509.0 après reclassement.
10. **Mécanismes oubliés** : les seize de la section 7. — *Versés en section 10 de la v2 ; à verser au relevé.*
11. **Réserves de regroupement** de la section 4 (hors 240.2, 562.0, 472.2) : signalées en section 11 de la v2 ; les déplacer est un choix de lecture laissé au rédacteur.
12. **Mineurs** : sortie de `ecrire_matiere_v1.py` (« lignes » = blocs) ; empreintes des lignes de veille dans les lots 01 à 20 (R6).

## 10. La v2

- `docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v2.md` — sha256 `8fa11231ee97759a64f39100f13e973b3614d5dde5d6a4c88968a04bff7bc565` ; 2 472 lignes.
- Produite par `programmes/ecrire_matiere_v2.py` (sha256 `83a8150cf09972452c7ce1755672094f8efb29743213b3167a4eba096e79e605`), sortie `programmes/ecrire_matiere_v2.sortie.txt` ; mêmes entrées que la v1, dont les empreintes sont vérifiées au départ ; garde « avant » testée sur un cas sain et sur un artefact (R5) ; couverture vérifiée (chaque mécanisme décrit des huit familles rangé une fois, 872 au total). Rejouée deux fois (copie de travail et dépôt) : sorties identiques à l'octet.
- Comptes v2 : 591 travaux avec mécanisme, 39 sans (21 « exclue ») ; 1 103 mécanismes, 891 décrits, 212 suggérés par le titre ; décrits par famille : exploration 188, originalité 84, épreuve 188, jugement 138, mémoire 93, sélection 80, coût 68, auto-conception 33, autre 19 ; « oui, mesuré » 474, « oui, affirmé » 124, « non » 69, « inconnu » 224 ; machines : 81 « oui, mesuré » sur 174.
- La liste de ses changements est en tête de la pièce (dix points). Elle ne modifie ni le relevé, ni les regroupements sur disque, ni la liste des machines (seule sa description change).

## 11. Ce que je n'ai pas pu vérifier

- Les mécanismes des travaux 605, 612 et 625, et la ligne 96 de la lecture 01, faute d'accès permis : vérifiés contre l'entrée de la table seulement.
- Les chiffres des entrées « page ou résumé » au-delà des lignes de veille, des résumés d'OpenReview versés et des pages lues pour 10 et 13 ; aucun autre PDF rouvert.
- Les 46 regroupements de 3.2 non tirés, lus seulement par leurs noms et leurs comptes.
- La complétude de la liste des machines, jugée d'après titres et notices.
- Le classement « exclue » de 552, 466.1 et 259.3 suit la règle que la pièce applique elle-même (retrait de 259.4 et de la ligne de 57, section 4.1) ; il revient à la session mère de le confirmer.
- Expositions involontaires, sans usage : la commande qui listait la structure de N-067 a affiché ses points 3 et 4 du § 4 (famille exclue), et la lecture de son § 5 et § 6 (citations obligatoires) en a montré deux lignes et des renvois ; la liste des titres de la lecture 03 a affiché le titre de sa section 5.4 ; des passages permis (lecture 02 § 7, lecture 03 § 0 et § 3, lecture 08 § 3, N-053 point 2, N-064 point 3, N-065) touchent des familles exclues. Rien n'en est repris dans cette contre-lecture ni dans la v2.
