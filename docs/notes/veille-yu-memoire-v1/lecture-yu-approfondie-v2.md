# Lecture approfondie de Yu et al. (2026), « Self-Improvement Memory Enables Continual Recursive Self-Improvement » — v2

## En-tête

- **Qui écrit** : lecteur neuf lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) sur la demande directe de Lazar ; modèle Fable 5.2 (`claude-fable-5-2`). Il n'a écrit ni la décision N-073, ni son complément 1, ni aucune pièce de la course d'auto-conception.
- **Version 2** : la version 1 (`lecture-yu-approfondie-v1.md`, `70c5941f8267a0f398275c9d980718c777bfa5f0ff6c1ce74829088d09be937d`) reste en place, intacte (R12). Cette version porte les corrections de la contre-lecture d'un lecteur d'un autre modèle, Opus 5.5 (`contre-lecture-lecture-yu-v1.md`, `97ac990c4fd450c3cd1cc3775db1bcf73f0ade242564f7ce94a5c392b723bb9f`, lue en entier, empreinte vérifiée). Chacune des onze corrections a été revérifiée par ce lecteur sur la page ou la ligne citée ; toutes sont appliquées ; la liste est dans `differences-v1-vers-v2.md`. La section « Corrections contestées », en fin de note, dit qu'aucune n'est refusée et porte deux précisions.
- **Heures** (`date -u`) : début 2026-11-19T06:59:14Z ; version 1 scellée à 07:10Z ; version 2 écrite à partir de 07:21Z.
- **Pièces lues, en entier, sur PDF, page par page (`pdftotext -layout`)** :

| pièce | fichier | empreinte | pages |
|---|---|---|---|
| Yu, Xia, Pan, Tang, Liu, Yu, Jiang, Chen, Xue et Yu, arXiv 2611.18856v1, 13 novembre 2026 | `docs/sources/arxiv-2611.18856-v1/arxiv-2611.18856.pdf` | `a8299ba5b16577dd328d602e32f35b914b9393ffb38148d2410f358d4d90ff3d` (vérifiée avant lecture) | 1 à 35, annexes A à F comprises |
| Li et Hu, « SkillHone », arXiv 2606.08671, version 4 du 29 octobre 2026 | `docs/sources/arxiv-2606.08671-v1/arxiv-2606.08671v4.pdf` (téléchargé le 19 novembre) | `3c6906004f965b52c323603cfcdcd2f336e3444c52de64c47eb577736729b002` | 1 à 11 |
| Lee, Nair, Zhang, Lee, Khattab et Finn, « Meta-Harness », arXiv 2603.28052, version 1 du 30 mars 2026 | `docs/sources/arxiv-2603.28052-v1/arxiv-2603.28052v1.pdf` (téléchargé le 19 novembre) | `7d9b90f53a9f4801a090f1a4acb843340cde81e4f865f97d53fff2a6a570eb73` | 1 à 10 et 14 à 26 lues ; 11 à 13 (bibliographie) non lues |

- Les identifiants des deux voisins ne sont pas dans la bibliographie de Yu et al. (SkillHone y est cité par ses actes, p. 11-12 ; Meta-Harness par sa page de conférence, p. 11) ; ils viennent de la recherche par titre de l'interface publique d'arXiv. Les versions lues sont celles d'arXiv ; les versions des actes n'ont pas été comparées (réserve 6).
- **Nos pièces** : `docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md` (§ 0 et § 1), `docs/decisions/decision-N-073-complement-1-memoire-transmise-v1.md`, `docs/decisions/decision-N-045-v2.md`, `docs/decisions/decision-N-058-v1.md`, `docs/decisions/decision-N-053-v1.md` (point 5).
- **Fichiers de ce dossier** : `recalcul_etude_appariee_v1.py` et `.txt` (le recalcul, inchangé, rejoué à l'identique par le contre-lecteur), `memoire-retrospective-auto-conception-v2.md` (notre mémoire reconstruite), `courriel-auteurs-brouillon-v2.md`, `differences-v1-vers-v2.md`.
- **Vocabulaire** : les auteurs nomment « SIM » leur mémoire d'auto-amélioration ; cette note écrit « la mémoire ». Les quatre conditions : « démarrage à froid » (harnais de départ, sans mémoire), « harnais seul » (harnais évolué sur la source, sans mémoire), « problèmes seuls » (harnais évolué et la seule liste des causes), « mémoire complète » (harnais évolué et l'enregistrement entier, tenu à jour pendant la cible) (p. 4, figure 6 p. 20). Un « tirage » est une exécution d'une tâche ; les scores sont sur 100.
- Aucune dépense, aucun appel à un modèle, aucune instance. Réseau : arXiv seul. Aucun refus d'outil.

---

## (a) Ce qui est solide et ce qui ne l'est pas

### a.1 Ce que le papier établit : une étude appariée, dix paires, un seul domaine

**Le plan** (p. 8, annexe C.4 p. 20). L'évolution du harnais « Terminus-2 » sur le banc de terminal source (Terminal-Bench 2.1) est répétée dix fois. Chaque harnais obtenu lance deux continuations de dix tours sur le banc cible (Terminal-Bench 4) : l'une hérite de la mémoire de sa source et la tient à jour, l'autre continue sans cette mémoire (avec le seul historique ordinaire de la course cible). « The independent source run is the unit of analysis » (p. 8). Modèle exécutant, concepteur (proposeur et sélecteur) : Gemini 3.8 Flash partout (p. 5, p. 19). Dix tours, cinq candidats par tour (p. 5).

**Le recalcul** (script et sortie dans ce dossier ; tableau 3, p. 8). Les dix différences imprimées sont égales aux dix écarts des scores, au centième.

| grandeur | annonce (p. 8) | recalcul |
|---|---|---|
| différence moyenne | 2,36 | 2,3630 |
| intervalle à 95 % | [1,05 ; 3,68] | [1,0456 ; 3,6804] |
| test t apparié bilatéral | t(9) = 4,06 ; p = 0,003 | t(9) = 4,0576 ; p = 0,00285 |
| rangs signés bilatéral, exact, rangs moyens pour les ex æquo, 2^10 signes (annexe C.4, p. 20) | p = 0,006 | 6 affectations sur 1 024 : p = 0,00586 |
| effet standardisé apparié | 1,28 | 1,2831 |
| paires en faveur de la mémoire | 9 sur 10 | 9 sur 10 |
| moyennes : départ, sans, avec | 18,36 ; 19,33 ; 21,70 | 18,363 ; 19,334 ; 21,697 |

**Tout concorde.** Contrôles ajoutés : test du signe exact, p = 0,0215 ; permutation exacte des signes sur la moyenne, p = 0,00586. Retrait d'une paire à la fois : la moyenne reste entre 2,02 et 2,69, le p du test t entre 0,0010 et 0,0079, le p des rangs signés entre 0,0039 et 0,0117 ; aucune paire ne porte le résultat. Sans les deux plus grandes différences (courses 4 et 9) : moyenne 1,665, intervalle [0,624 ; 2,706], p = 0,0069.

**En unités naturelles.** Le jeu tenu à l'écart du banc cible compte 33 tâches et 165 tirages (tableau 4, p. 18) ; un tirage vaut 0,606 point. Les dix différences sont, en tirages : +3, +3, +1, +9, +3, +6, +3, −1, +8, +4. **Total : 39 tirages réussis de plus sur 1 650** (compte de la mère vérifié), soit 3,9 tirages de plus sur 165 par paire. Le bras sans mémoire gagne lui-même 0,97 point sur son départ (intervalle [0,18 ; 1,77], recalcul § 6).

**Ce que cette étude établit donc** : sur ce banc, depuis ce harnais, avec ce modèle pour tout faire, continuer avec la procédure complète finit plus haut que continuer sans la mémoire d'amélioration, de 2,4 points en moyenne, et l'écart ne tient pas à une paire.

### a.2 Ce que ce plan n'identifie pas

1. **L'héritage n'est pas séparé de la tenue d'une mémoire.** Le bras « harnais seul » n'a pas la mémoire d'amélioration pendant les dix tours de la cible — il garde, comme tous les bras, l'historique ordinaire de la course cible (« All methods retain the ordinary target-run history Dt », p. 20 ; p. 5) ; le bras « mémoire complète » hérite **et** met à jour (« Full record; updated on target », figure 6 p. 20 ; « Each condition persists throughout target RSI », p. 20). Les auteurs le disent : « Our comparisons evaluate SIM as a complete procedure, combining inherited memory with updates during target optimization » (p. 10), et encore p. 16 et p. 23-24. **Aucun bras « mémoire vide au transfert, tenue pendant la cible » n'existe dans le papier** (cherché : § 3.3 p. 4-5, § 4.1 p. 5, annexes C.3 à C.6 p. 20-21, annexe E p. 22-25). La seule comparaison où une mémoire est tenue sans rien hériter est la première ligne du tableau 1 (p. 6) : sur Gemini 2.5 Flash, depuis le même harnais de départ **non évolué**, sur le banc **source**, 22,4 avec mémoire contre 21,4 sans (« The first row tests SIM during an initial RSI run; only the later rows test transfer from an earlier generation », p. 21) — une course par condition, à une décimale, un écart d'un point. Ce n'est pas une comparaison **au transfert** : c'est une première course ; dans le plan (c), elle correspond au contraste « bras 2 moins bras 1 », non à « bras 3 moins bras 2 ». Toutes les courses source tiennent une mémoire née vide (p. 4) ; aucune autre n'a de témoin sans mémoire. L'effet mesuré par les dix paires peut donc venir de ce qui est transmis, de l'habitude de noter et relire pendant la cible, ou des deux ; le papier ne permet pas de le dire. (Les auteurs posent pourtant la question de l'expérience héritée, p. 2 ; c'est le plan, non la question, qui ne sépare pas.)
2. **Le bras « problèmes seuls » n'est pas dans l'étude appariée.** Les dix paires comparent « mémoire complète » à « harnais seul », rien d'autre (tableau 3, p. 8).
3. **Un seul domaine, un seul harnais de départ, une seule transition, un seul modèle concepteur** (p. 8 ; limites p. 10 : « independent RSI repetitions focus on coding; the other domains are evaluated with one run per condition »).
4. **Le coût n'est pas apparié.** « We match rounds and candidate counts across methods; token use and runtime can differ » (p. 19). La mémoire entière est servie au proposeur dans sa consigne et lue par le sélecteur, « without retrieval or truncation » (p. 4) ; ce qu'elle coûte en jetons n'est donné nulle part.
5. **Le bruit des tirages par tâche est inconnu.** Le papier ne donne, pour l'étude appariée, aucun taux de réussite par tâche ni aucune répartition des 39 tirages gagnés entre les 33 tâches (cherché : p. 8-9, tableau 3, figure 5, annexes B.2-B.3 p. 17, C.4 p. 20, E p. 22-25, F p. 24-35). Les seules réussites par tâche publiées sont des cas choisis sur le banc source (de 1 à 5 tirages réussis sur 5, p. 25-27). Si les 165 tirages étaient indépendants et de même probabilité, l'écart-type d'une différence serait de 4,45 points ; l'écart-type observé des dix différences est de 1,84 (recalcul § 5). Cela est compatible avec des tâches presque toujours réussies ou presque toujours ratées, mais on ne peut pas dire si le gain tient à une ou deux tâches qui basculent ou à beaucoup. **Question pour les auteurs** (courriel, point 1).
6. Le harnais « Terminus-2 » du tableau 5 (p. 23 : départ 19,39 ; harnais seul 19,39 ; mémoire complète 21,82) ne correspond à aucune ligne du tableau 3 : la course des comparaisons principales n'est pas l'une des dix paires, ou le papier ne le dit pas.

### a.3 Ce qui n'est que décrit : une course par condition

« Except for the dedicated paired study, each condition is one complete RSI run, and its five rollouts per task estimate execution performance rather than optimization variance. We report individual settings descriptively » (p. 6). Tous les nombres ci-dessous sont des **courses uniques** ; seule la dernière ligne est **répétée**.

**Changement de banc, modèle fixe** (tableau 5, p. 23 ; scores sur le jeu tenu à l'écart de la cible, avant → après les dix tours) :

| domaine / harnais de départ | démarrage à froid | harnais seul | problèmes seuls | mémoire complète | statut |
|---|---|---|---|---|---|
| code / AHE | 16,36 → 19,39 | 18,18 → 20,61 | 18,18 → 18,79 | 18,18 → 24,85 | course unique |
| code / Terminus-2 | 18,18 → 19,39 | 19,39 → 19,39 | 19,39 → 20,61 | 19,39 → 21,82 | course unique |
| classification de textes / NoMemory | 68,60 → 72,00 | 71,40 → 71,00 | 71,40 → 73,40 | 71,40 → 73,60 | course unique |
| classification de textes / FewShotAll | 75,72 → 75,92 | 72,92 → 74,12 | 72,92 → 75,52 | 72,92 → 77,92 | course unique |
| espace de travail / ReAct | 73,89 → 82,98 | 74,93 → 85,07 | 74,93 → 85,54 | 74,93 → 87,89 | course unique |
| conception d'ingénierie / ReAct | 39,13 → 40,87 | 39,13 → 42,61 | 39,13 → 42,61 | 39,13 → 46,96 | course unique |

**Changement de modèle (Claude Opus 5.5 vers Gemini 3.8 Flash), banc fixe** (tableau 6, p. 24) :

| domaine / harnais de départ | démarrage à froid | harnais seul | problèmes seuls | mémoire complète | statut |
|---|---|---|---|---|---|
| code / AHE | 16,36 → 19,39 | 13,94 → 18,18 | 13,94 → 20,61 | 13,94 → 21,82 | course unique |
| classification de textes / FewShotAll | 78,32 → 82,72 | 77,72 → 80,20 | 77,72 → 81,32 | 77,72 → 83,80 | course unique |
| espace de travail / ReAct | 73,89 → 82,98 | 68,41 → 73,42 | 68,41 → 79,22 | 68,41 → 84,75 | course unique |
| conception d'ingénierie / ReAct | 39,13 → 40,87 | 34,78 → 42,61 | 34,78 → 46,96 | 34,78 → 50,43 | course unique |

**Autres nombres, tous en course unique** : la chaîne de quatre générations de Gemini (tableau 1, p. 6 : 21,4 / 22,4 ; 73,3 / 76,8 ; 88,9 / 90,5 ; 95,6 / 94,8 — la continuation finit **plus bas** sur la dernière) ; le harnais partagé par trois modèles (tableau 2, p. 8 ; « Each procedure is run once, and optimization cost is not compared », p. 21) ; la rétention sur la source (figure 8, p. 24, « one run per condition ») ; le remplacement du concepteur par Claude Opus 5.5 (tableau 7, p. 25 ; « course unique » y est une inférence de ce lecteur : la page ne le dit pas, l'annexe C.4 le dit des conditions principales).

**Répété** : code / Terminus-2, mémoire complète contre harnais seul, dix paires (tableau 3, p. 8).

### a.4 Ce que chaque composant de la mémoire apporte : problèmes seuls contre enregistrement complet

Écarts des scores finaux, en points (calculés depuis les tableaux 5 et 6) :

| réglage | problèmes seuls − harnais seul | complète − problèmes seuls | complète − harnais seul |
|---|---|---|---|
| banc : code / AHE | −1,82 | +6,06 | +4,24 |
| banc : code / Terminus-2 | +1,22 | +1,21 | +2,43 |
| banc : textes / NoMemory | +2,40 | +0,20 | +2,60 |
| banc : textes / FewShotAll | +1,40 | +2,40 | +3,80 |
| banc : espace de travail | +0,47 | +2,35 | +2,82 |
| banc : ingénierie | 0,00 | +4,35 | +4,35 |
| modèle : code / AHE | +2,43 | +1,21 | +3,64 |
| modèle : textes / FewShotAll | +1,12 | +2,48 | +3,60 |
| modèle : espace de travail | +5,80 | +5,53 | +11,33 |
| modèle : ingénierie | +4,35 | +3,47 | +7,82 |

- La liste des causes seule a un effet « mixed » selon les auteurs (p. 6) : de −1,82 à +2,40 quand le banc change ; elle aide dans les quatre réglages quand le modèle change (calcul de ce lecteur depuis le tableau 6).
- L'enregistrement complet finit au-dessus des problèmes seuls dans les dix réglages (p. 6, p. 23). **Mais ce sont dix courses uniques, et ce contraste n'a aucune paire répétée.** L'échelle de bruit que donne l'étude appariée — 1,84 point d'écart-type entre deux continuations d'un même départ, en code — met les deux écarts de code de 1,21 point (deux tirages sur 165) à moins d'un écart-type, et l'écart de 0,20 point sur NoMemory correspond à 5 exemples-tirages sur 2 500 (tableau 4, p. 18). Les réglages partagent bancs et harnais ; ils ne sont pas dix essais indépendants.
- L'enregistrement complet ajoute aux causes : la modification et sa justification, les tâches prédites et les tâches réparées ou manquées, la provenance (p. 4, annexe D.3 p. 22). **Le papier ne sépare aucun de ces champs** : il n'y a pas de bras « avec justification, sans résultats », ni « sans prédiction », ni « sans provenance ». « Ce que chaque composant apporte » n'est donc connu qu'à deux crans — causes seules, puis tout le reste d'un bloc — et à une course par cran.
- Conclusion des auteurs : « Keeping the edit history and evaluation evidence thus helps beyond retaining the diagnosis alone » (p. 6). Elle est écrite au présent de constat ; l'appui est descriptif.

### a.5 La prédiction écrite avant l'essai est-elle confrontée au résultat ?

**Par enregistrement, oui ; en agrégat, jamais.**

- Le mécanisme : « Predictions of which tasks an edit will fix are recorded before evaluation and checked afterward » (p. 4). Champs `predicted`, `fixed`, `missed` par tentative (annexe D.3, p. 22).
- **Aucun taux de justesse d'ensemble, aucune calibration, aucune comparaison à un taux de base** n'apparaît dans le papier. Cherché : toutes les pages où « predict » apparaît (1, 3, 4, 9, 15, 16, 22, 28, 29, 32, 35 ; et 18, au sens de l'étiquette prédite par l'agent de classification, sans rapport), plus les sections de résultats (p. 6-9) et d'ablations (p. 22-25).
- **Compte sur tous les enregistrements publiés** (annexes F.2 et F.4 ; l'annexe F.5 et le tableau 8, p. 30-34, décrivent des mécanismes et ne publient aucun enregistrement) :

| enregistrement | tentative | prédites | réparées | page |
|---|---|---|---|---|
| P5, arrêt prématuré sans vérification d'exécution | source, tour 6 | 2 | 2 | figure 9, p. 28 |
| P5 | source, tour 8 | 1 | 1 | figure 9, p. 28 |
| P5 | source, tour 10 | 3 | 1 | figure 9, p. 28 |
| P8, arrêt sur une solution faisable mais sous-optimale | cible, tour 2 | 2 | 0 | figure 10, p. 29 |
| P8 | cible, tour 4 | 2 | 0 | figure 10, p. 29 |
| P3, livrable correct mais contraire au contrat du vérificateur | source, tour 4 | 4 | 1 | figure 12, p. 32 |
| P3 | cible, tour 5 | 2 | 0 | figure 12, p. 32 |
| P3 | cible, tour 6 | 2 | 1 | figure 12, p. 32 |
| **total** | 8 tentatives | **18** | **6** | |

**6 tâches réparées sur 18 prédites, soit un tiers.** Sur la source : 5 sur 10. Sur la cible, là où la mémoire est dite aider : **1 sur 8**. Le tableau de la page 28 donne lui-même « Realized predictions : 4 of 6 » pour P5 et « 0 of 4 » pour P8. Ces trois enregistrements sont des cas choisis par les auteurs pour illustrer ; ils ne sont pas un échantillon (le fichier montré compte au moins huit problèmes, P1 à P9 moins P6, p. 22).

- **La prédiction sert-elle au sélecteur ?** Aucune règle ne le dit ; les huit consignes résumées de l'annexe D.2 (p. 21-22) ne mentionnent pas les prédictions. Le sélecteur « reads the same record » (p. 4) et pèse « performance, complexity, domain specificity, and regression risk » (p. 3). « accepted means the selector chose the edit in that round, even if some predicted fixes failed » (p. 22). Les deux tentatives de P8 ont été retenues alors qu'aucune des tâches visées n'a été réparée (p. 28) ; la seconde a ensuite été changée (« adopted and later changed », p. 29 ; p. 27). Dans le texte, la prédiction est **archivée et relisible** ; rien ne montre qu'elle soit **notée**, ni qu'une prédiction manquée pèse sur un choix.
- **Si les prédictions échouent souvent alors que la mémoire aide, d'où peut venir le gain ?** Le papier ne le mesure pas. Ses propres cas pointent vers la justification et la provenance plutôt que vers la prédiction : sans mémoire, la course retouche quatre fois la même garde d'achèvement, deux fois pour réparer des blocages, et attribue à son premier tour une garde héritée de la source (p. 8-9, p. 29) ; en ingénierie, la course sans mémoire défait dès le premier tour les consignes héritées, la course avec mémoire les garde (p. 34). Savoir **pourquoi** une modification existe et **d'où** elle vient suffirait à expliquer ces deux cas. C'est une lecture de cas choisis, non un résultat ; un échec prédit puis observé peut aussi servir d'information (« unresolved predictions », p. 9, p. 35).
- **La prédiction écrite avant l'évaluation n'est pas propre à ce papier.** Les auteurs écrivent d'un travail antérieur : « AHE makes harness components and modification outcomes observable, checking edit-level predictions against subsequent task outcomes (Lin et al., 2026) » (p. 15 ; arXiv 2604.25850, non lu ici).

### a.6 Le concepteur fort : la mémoire n'y est pas testée

Dans toutes les comparaisons de mémoire, le proposeur et le sélecteur sont Gemini 3.8 Flash, « including when Opus executes the tasks » (p. 19 ; p. 5). L'annexe E.4.2 remplace ce concepteur par Claude Opus 5.5 **pendant l'évolution sur la source seulement** (« during TB2.1 source RSI », p. 24 ; tableau 7, p. 25) : elle compare l'amélioration de la source avec un concepteur ou l'autre, sans aucun bras de mémoire. Dans la transition « Opus vers Gemini » (tableau 6), Opus est le modèle qui **exécute** les tâches de la source ; le concepteur reste Gemini 3.8 Flash. **La mémoire n'est donc jamais testée avec un concepteur fort.** D'après le texte seul, le résultat ne se transporte pas à un organisme dont les proposeurs sont des modèles de frontière : un concepteur fort peut reconstruire seul, du code et des traces, ce que la mémoire rappelle à un concepteur faible — ou en tirer davantage. Le papier ne tranche ni l'un ni l'autre ; ses limites disent seulement que les procédures de planification et de recherche de l'optimiseur sont tenues fixes (p. 10).

**Chez les deux voisins lus, le concepteur est un modèle Claude Opus 4.6.** « Claude Opus 4.6 serves as the development-time controller » de SkillHone (SkillHone p. 4), et c'est sous ce contrôleur que l'ablation de l'historique coûte 13,4 et 10,9 points (p. 6) ; Claude Opus 4.6 est le proposeur de Meta-Harness (« the proposer P is Claude Code with Opus-4.6 », Meta-Harness p. 5 ; « TerminalBench-2 run (10 iterations, Claude Opus 4.6) », p. 15). Ce sont des **indices voisins contre** la lecture « un concepteur fort peut s'en passer » : avec un concepteur de cette lignée, retirer l'histoire coûte encore. Ils ne testent pas la mémoire **transmise** (aucun des deux ne change de banc ou de concepteur avec et sans mémoire), portent sur d'autres objets, et l'ablation de SkillHone est confondue (a.7). Aucun de ces PDF ne compare Claude Opus 4.6 à Gemini 3.8 Flash : « fort » est ici le mot de la consigne, non une mesure.

### a.7 Les deux voisins, lus sur source

**SkillHone (Li et Hu ; déposé en juin 2026 d'après son identifiant 2606, soit environ cinq mois avant Yu et al. ; le PDF empreinté ne porte que « arXiv:2606.08671v4 … 29 Oct 2026 », p. 1 — le jour du premier dépôt, 7 juin, vient de la réponse de l'interface d'arXiv relevée le 19 novembre, hors pièce empreintée).** Un harnais qui fait évoluer une « compétence » d'agent en tenant un historique persistant de décisions. Chaque pas est un enregistrement h = (diagnostic, révision candidate, preuve d'évaluation expurgée, issue), l'issue pouvant être « accepter, réviser, rejeter, différer » (p. 4) ; l'historique garde donc aussi les **révisions rejetées**, que la mémoire de Yu et al. ne garde pas (« only the chosen candidate is recorded », Yu p. 4). L'historique « acts as a persistent memory for the evolution process itself » (p. 4). Deux équipes à droits séparés : celle qui optimise ne voit jamais les cibles ni les validateurs, seulement des rapports expurgés (p. 2-3, tableau 6 p. 11). Ablation : sans l'historique de décisions, 64,6 → 51,2 sur GAIA et 66,4 → 55,5 sur WebWalkerQA (tableau 2, p. 6) ; sans la séparation des rôles, 58,2 et 61,1. **Cette ablation confond deux choses** : la condition « No decision history » retire l'historique **et** passe à un signal scalaire (« starts each step from the latest skill artifact alone, optimizing on a scalar signal as in reflective baselines », p. 6) ; la chute de 13,4 et 10,9 points ne peut pas être attribuée à l'historique seul. **Le nombre de courses derrière ces chiffres n'est dit nulle part** ; la trajectoire montrée est « one SkillHone run » (p. 8-9) ; aucun intervalle. Pas de champ de prédiction. Pas de changement de modèle concepteur ni de transmission entre bancs : la mémoire sert la suite du même travail (le transfert montré est celui de la compétence finie vers un autre modèle exécutant, figure 3 p. 5). Coût : 39,9 millions de jetons d'entrée contre 1,48 pour la méthode comparée (tableau 5, p. 9).

**Meta-Harness (Lee et al., 30 mars 2026).** Une boucle extérieure dont le proposeur est un agent de code qui lit, par le système de fichiers, le code, les scores et les **traces d'exécution brutes de tous les candidats passés** (p. 1-2, p. 4) ; « the proposer reads a median of 82 files per iteration » (p. 2, tableau 8 p. 15). Aucune structure de mémoire : « instead of relying on a fixed scaffold, an archive of prior discoveries, or a persistent memory mechanism, it gives the proposer unrestricted filesystem access to prior experience » (p. 3). Ablation de ce que le proposeur voit (tableau 3, p. 7, classification de textes) : scores seuls, médiane 34,6 ; scores et **résumés**, 34,9 ; traces brutes, 50,0 — « summaries do not recover the missing signal, and may even hurt by compressing away diagnostically useful details » (p. 7). Le nombre de courses par condition n'est pas donné clairement (la colonne « > ZS » compte des « runs » : 26, 23, 39). Le proposeur écrit de lui-même des hypothèses chiffrées avant l'essai (« will yield +1--3pp », p. 17 ; « reduce wasted exploration episodes by 3--5 turns », p. 21) ; elles ne sont ni rangées ni confrontées en agrégat. Une ligne note un transfert entre courses (« Iteration 10: cross-run transfer », p. 17). Sur le banc de terminal, la recherche et l'évaluation finale portent sur les mêmes 89 tâches (p. 9).

**Ce que les deux voisins changent à la lecture de Yu et al.**
- Tenir un historique structuré du pourquoi des modifications, et l'ablater (avec la confusion dite plus haut), est fait avant Yu et al. (SkillHone, p. 4 et p. 6). Yu et al. le citent en une ligne (p. 3, p. 16).
- Ce que Yu et al. ajoutent, d'après les trois textes : la transmission à travers un changement de banc ou de modèle, le rangement par problème récurrent avec plusieurs tentatives sous une même cause, et une étude appariée à dix sources. Le champ de prédiction existe ailleurs selon eux (AHE, p. 15).
- **Un indice contraire** vient de Meta-Harness : à information comprimée, la recherche fait moins bien qu'avec les traces brutes (tableau 3, p. 7). La mémoire de Yu et al. est un résumé ; leur bras « harnais seul » garde « the ordinary target-run history » (code, journaux, différences — p. 5, figure 2 p. 4) mais perd toute l'histoire de la source. Leur étude ne compare pas la mémoire structurée à l'accès aux traces brutes de la source.

### a.8 En une liste

**Solide** : (1) l'arithmétique de l'étude appariée — tout concorde au recalcul ; (2) sur un banc de code, un harnais, un modèle, la procédure complète bat la continuation sans la mémoire d'amélioration de 2,36 points (39 tirages sur 1 650), sans dépendre d'une paire ; (3) la franchise du papier sur ses limites (p. 6, p. 10, p. 21).

**Pas solide, ou non établi** : (1) que l'**héritage** cause le gain — non séparé de la tenue d'une mémoire ; (2) que l'enregistrement complet vaut mieux que la liste des causes — dix courses uniques ; (3) tout résultat hors du code ; (4) la valeur de la prédiction écrite — un tiers de réussite sur les exemples publiés, 1 sur 8 sur la cible, aucun agrégat, aucun rôle dans la sélection ; (5) la tenue du résultat avec un concepteur fort — non testé ; (6) le coût — non apparié, non rapporté ; (7) le titre (« Enables ») va au-delà de ce que le plan identifie.

---

## (b) Ce qui change pour nos revendications

**Rien ne s'applique par cette note : toute modification de revendication est un nœud de Lazar. Ce qui suit est proposé.**

1. **La phrase du complément 1 de N-073 est à préciser, sur deux points.** Elle dit : « la question que Yu et al. (2026) posent pour le score d'un harnais d'agent par une ablation appariée de la mémoire transmise (mémoire complète contre harnais seul, à départ égal) ».
   - *« ablation … de la mémoire transmise »* : ce qui est ablaté est la procédure entière, mémoire héritée **et** tenue pendant la cible (p. 10, p. 20). Yu et al. posent bien la question de l'expérience héritée (« We therefore ask whether the experience gained during source optimization can help the harness adapt to new models or data », p. 2) ; leur plan n'y répond que par la procédure entière contre la continuation sans mémoire d'amélioration (p. 10). Ce qui manque à leur plan est la **séparation** de l'héritage et de la tenue, non la question.
   - *« appariée »* : vrai pour dix paires, un domaine, un harnais, un concepteur (p. 8). Tout le reste est une course par condition (p. 6), dans quatre domaines, avec un bras qui ne garde que les causes.
   - **Rédaction proposée** (celle du contre-lecteur, point 8 de son rapport, reprise sans changement ; revérifiée phrase à phrase sur les pages citées) :

     « Yu et al. (2026) demandent si l'expérience acquise pendant une optimisation source aide à poursuivre l'optimisation après un changement de banc ou de modèle (p. 2). Ils comparent, depuis le même harnais évolué, une procédure complète — mémoire d'amélioration héritée de la source puis tenue à jour pendant la cible — à la continuation sans cette mémoire, qui garde l'historique ordinaire de la course cible ; la comparaison est répétée sur dix paires dans un domaine (code) et faite une fois par condition dans les autres réglages, avec aussi un bras qui ne garde que les causes (p. 6, p. 8). Ils écrivent que leurs comparaisons évaluent la procédure entière, héritage et mises à jour ensemble (p. 10). Nous posons, pour des découvertes plutôt que pour le score d'un harnais, la question de l'héritage séparé de la tenue : l'archive héritée cause-t-elle les découvertes, au-delà du fait de tenir une archive ? Nous ne la disons ni nouvelle ni propre : plusieurs travaux voisins cités par Yu et al. (p. 3, p. 15-16) n'ont pas été lus sur ce point. »

   - Cette rédaction ne dit pas la question « libre », et le dit dans la phrase même : parmi les travaux que Yu et al. citent pour la poursuite de l'optimisation et la mémoire de l'amélioration (p. 3, p. 15-16), aucun n'a été lu ici ; et la première ligne de leur tableau 1 (p. 6, p. 21) est déjà une moitié de la séparation (tenir contre ne pas tenir, sans héritage, une course). « Non séparé chez Yu et al. » n'est pas « séparé par personne » (R8).
   - Un mot à trancher par Lazar dans cette rédaction : « dans les autres réglages » couvre aussi le code (les deux réglages de code des tableaux 5 et 6 sont des courses uniques, hors des dix paires) ; « dans tous les réglages des tableaux 5 et 6 » serait plus exact. Voir « Corrections contestées ».
2. **Le complément 1 a raison sur le fond** : la méthode de l'ablation de la mémoire n'est pas propre au programme ; l'objet (des découvertes) reste la seule différence. Cette lecture le renforce : l'ablation d'un historique de décisions est faite dès juin 2026 par SkillHone (tableau 2, p. 6).
3. **Citations obligatoires de l'énoncé 5, à étendre** (proposé) :
   - Li et Hu, « SkillHone », arXiv 2606.08671 — historique persistant de décisions (diagnostic, révision, preuve, issue ; rejets gardés) et son ablation ; lu sur source ici.
   - Lee et al., « Meta-Harness », arXiv 2603.28052 — histoire complète servie au proposeur ; **à citer comme indice contraire avec la prémisse**, au même titre que Qin et al. dans N-073 § 1 : un résumé de l'expérience fait moins bien que les traces brutes (tableau 3, p. 7) ; lu sur source ici.
   - Lin et al., « Agentic Harness Engineering », arXiv 2604.25850 — selon Yu et al. (p. 15), y est déjà faite la confrontation des prédictions par modification aux issues par tâche. **À lire sur source avant tout texte qui parle de « prédiction écrite avant l'essai »** ; seconde main à ce jour.
   - Xia et al., « RRSI », arXiv 2609.24972 — selon Yu et al. (p. 16), enregistre hypothèses, différences, changements de score et de coût, décisions, **modifications rejetées comprises**. Seconde main ; à lire avant de décrire une mémoire qui garde ses rejets.
4. **« Mémoire transmise »** (N-073 § 1, « Ce qui reste… ») : reste « décrite sans être dite nouvelle ni propre ». Deux voisins de plus sont lus sur source ; aucun n'ouvre de place.
5. **Ne pas écrire, dans aucun texte sortant** : « Yu et al. montrent que la mémoire transmise cause l'amélioration » ; « l'enregistrement complet vaut mieux que le diagnostic seul » sans « sur une course par condition » ; « des prédictions vérifiées guident la sélection » ; quoi que ce soit sur un concepteur fort ; un chiffre hors du code sans « course unique ».
6. **Ce que Yu et al. ne font pas, et que le plan (c) ferait** — à décrire, jamais à dire libre : séparer l'héritage de la tenue ; mesurer la justesse des prédictions en agrégat contre un taux de base ; apparier le coût ; tester avec des concepteurs forts ; faire écrire le résultat par un oracle plutôt que par la boucle qui est jugée.
7. **N-045 v2, énoncé 6 (ii), « poids contre archive »** : inchangé. Meta-Harness (traces brutes contre résumés) et Yu et al. (résumé structuré contre rien) sont deux points d'un même axe que cet énoncé ne nomme pas : la **forme** de l'archive servie. À verser à l'atelier d'idées.
8. **Aucun chiffre de cette note n'entre dans un préenregistrement ou un papier sans relecture de la page citée** (R7). Les chiffres de Yu et al. cités au-delà des pages 1 à 4 et 9 à 10 du complément 1 sont désormais lus, page à l'appui, par ce lecteur seul ; ils ont été contre-lus une fois (Opus 5.5, `97ac990c…`), page à l'appui.

---

## (c) Proposition : une mémoire préenregistrée pour la prochaine version de l'organisme

**C'est une proposition. Elle ne s'applique pas. Elle ne modifie aucun préenregistrement, n'engage aucune dépense, et demande, pour exister, un préenregistrement scellé et contre-lu (R1, R2), un devis et un GO.**

### c.1 Ce qui est éprouvé

Trois questions, dans cet ordre de coût :
1. Tenir une mémoire rangée par problème aide-t-il l'organisme à retrouver des structures plantées, à coût égal ?
2. **Hériter** de la mémoire d'une génération précédente aide-t-il au-delà de la tenir ?
3. Les prédictions que l'organisme écrit avant l'essai sont-elles justes plus souvent qu'un taux de base ?

### c.2 Format d'une entrée

Une entrée par problème récurrent ; sous elle, une ligne par tentative. Champs typés, longueurs bornées.

| champ | qui l'écrit | quand | forme |
|---|---|---|---|
| `probleme` | le proposeur | à la proposition | une phrase, 200 caractères au plus ; ou l'identifiant d'un problème existant |
| `tentative` | le proposeur | à la proposition | module changé (liste fermée des modules de l'organisme), description de 300 caractères au plus |
| `justification` | le proposeur | à la proposition | 300 caractères au plus |
| `prediction` | le proposeur | à la proposition, **scellée avant toute évaluation** | forme principale : le **signe** attendu du changement du score de l'oracle sur le monde d'évolution (plus, moins, égal), une **tranche** de grandeur (liste fermée gelée au préenregistrement) et le signe attendu sur le coût. Aucun texte libre, aucun identifiant d'item planté (voir c.3 bis). |
| `resultat` | **l'orchestrateur, par programme** | après l'évaluation | le score de l'oracle sur le monde d'évolution et le coût mesuré, **au grain exact du retour ordinaire** que les trois bras reçoivent déjà (c.4, règle 3) ; rien de plus fin. Aucun texte. |
| `gardee` | l'orchestrateur, par programme | après l'évaluation | oui ou non, **par une règle écrite sur le seul score de l'oracle du monde d'évolution et le coût** (N-058). Jamais par un verdict de juge, jamais par le nombre de fiches que le juge promeut. Les tentatives non gardées restent dans la mémoire (SkillHone, p. 4 ; contrairement à Yu et al., p. 4). |
| `provenance` | l'orchestrateur | à l'écriture | génération, espèce du proposeur, famille du monde planté, version de l'orchestrateur, empreinte de la configuration |

L'entrée de Yu et al. (annexe D.3, p. 22) est reprise pour `probleme`, `tentative`, `prediction`, `resultat`, `provenance` ; s'en écartent : le résultat écrit par programme, les rejets gardés, le texte libre borné, la prédiction sur un agrégat et non sur des tâches nommées.

**Sur le champ `gardee` (version 1 : `retenue`) — faille relevée par la contre-lecture.** La version 1 ne disait pas qui décide. Si le choix d'une génération passait par le verdict du juge (fiches promues), le champ transporterait ce verdict dans la mémoire servie aux proposeurs suivants : le juge entrerait dans la sélection de l'agent par la lecture, ce que N-053 (point 5) interdit. D'où la règle : le champ est décidé par programme sur l'oracle et le coût seuls. **Si, dans la version de l'organisme éprouvée, ce qui est gardé d'une génération à l'autre dépend du juge en quelque point, le champ n'est ni écrit ni servi**, et la mémoire ne dit que ce qui a été tenté et ce que l'oracle a rendu. Un essai du code garde l'invariant : aucune valeur de la mémoire n'est fonction d'une sortie du juge.

### c.3 Moment du scellement

La prédiction est scellée par son empreinte, inscrite au manifeste de la génération, **avant** que l'oracle soit appelé pour cette tentative (engagement scellé, comme la statistique de N-064). Le programme refuse d'évaluer une tentative sans empreinte de prédiction ; il refuse d'écrire un résultat dont la prédiction ne correspond pas à l'empreinte. Garde éprouvée sur un cas sain et sur un artefact (R5) : une prédiction modifiée après coup doit faire échouer l'écriture.

### c.3 bis La prédiction ne doit pas livrer la clé de l'oracle

**Faille relevée par la contre-lecture.** La version 1 demandait au proposeur de nommer « quels items plantés » sa tentative ferait retrouver. Pour les nommer, il faudrait lui servir leur liste — donc leur nombre et leur existence, c'est-à-dire une partie de la clé de l'oracle. **Sous cette forme, le champ ne peut pas exister.** Deux formes restent :

1. **Forme retenue (principale)** : la prédiction porte sur l'**agrégat** que l'organisme reçoit déjà — signe et tranche du changement du score de l'oracle sur le monde d'évolution, signe du coût. Elle ne livre rien. Elle est moins fine que celle de Yu et al. (des tâches nommées, p. 22) : on perd « quelle structure », on garde « mieux ou moins bien, et de combien ». La justesse se lit par une règle de score propre sur les tranches, contre le taux de base par permutation.
2. **Forme fine, sous condition** : le proposeur nomme **dans ses propres mots** les structures qu'il prétend faire retrouver ; l'orchestrateur les apparie après coup aux items plantés **par programme** (la fonction d'appariement de l'oracle, la même que pour « structures retrouvées », N-058), et n'écrit en retour qu'un compte au grain du retour ordinaire. Elle n'est permise que si cet appariement se fait sans modèle : s'il exigeait un juge, ce serait un verdict de juge écrit dans la mémoire (interdit, N-053 point 5). **Non vérifié ici** : ce lecteur n'a pas lu le code de l'oracle ; à établir avant tout préenregistrement, sinon la forme 1 seule.

Dans les deux formes, ni le nombre d'items plantés ni aucun identifiant d'item n'est servi à aucun bras.

### c.4 Plan à trois bras, apparié par source

Pour chaque **source** indépendante (une course d'organisme sur une famille de mondes plantés, graines dérivées par `SeedSequence`, R9), trois continuations depuis le même organisme, sur une famille de mondes plantés **neuve** :

| bras | mémoire structurée au départ | mémoire structurée pendant la course |
|---|---|---|
| 1 — sans mémoire | aucune | aucune |
| 2 — mémoire neuve tenue | vide | tenue et servie |
| 3 — mémoire héritée | celle de la source | tenue et servie |

- **Bras 3 moins bras 2 = effet de l'héritage de la mémoire, au-delà de ce que l'organisme hérité porte déjà.** C'est le contraste que Yu et al. n'ont pas (p. 10).
- **Bras 2 moins bras 1 = effet de tenir une mémoire structurée** (la moitié que la première ligne du tableau 1 de Yu et al. approche, une course, p. 6 et 21).
- Bras 3 moins bras 1 = la « procédure complète » de Yu et al., rapportée pour comparaison, hors critère.

**Ce que chaque bras reçoit — sept règles, toutes à geler au préenregistrement.**

1. **Le même organisme de départ.** Les trois bras partent du code et des consignes de l'organisme tel que la source l'a laissé (l'équivalent du harnais évolué de Yu et al.). Les leçons de la source déjà **dans** ce code sont donc héritées par les trois bras. Le contraste « bras 3 moins bras 2 » ne mesure pas « l'héritage tout court » ; il mesure ce que la mémoire transmise ajoute **à un organisme qui a déjà hérité par son code**. À écrire ainsi dans tout texte.
2. **L'`historique` de la source est remis à zéro dans les trois bras.** N-045 v2 (énoncé 5) rappelle que l'`historique` servi à l'organisme « contient déjà toutes les générations passées » : laissé en place, il ferait hériter les bras 1 et 2 par un second canal et fausserait les deux contrastes. Au départ de la continuation, aucun bras ne reçoit de générations de la source par l'`historique` ; chaque bras garde ensuite l'`historique` **de sa propre continuation**, sous la même forme (l'équivalent de l'historique ordinaire de Yu et al., p. 5 et 20). Le seul canal par lequel la source parle au-delà du code est la mémoire du bras 3. Garde éprouvée (R5) : un `historique` de départ non vide arrête le lancement.
3. **Le même retour de l'oracle, au même grain, dans les trois bras.** Ce que l'oracle rend à l'organisme à chaque génération (score sur le monde d'évolution, coût) est fixé une fois et servi à l'identique aux trois bras par l'`historique` de la continuation. Le champ `resultat` de la mémoire **ne contient rien de plus fin** que ce retour. La mémoire ne change donc que l'**accès au passé** — son rangement par problème, la justification, la prédiction scellée, la provenance — et non la quantité d'information tirée de l'oracle. (La version 1 servait l'issue item par item aux seuls bras 2 et 3 : le contraste « tenue » aurait mesuré « mémoire plus retour plus fin ».)
4. **Budget en dollars égal par bras pour la comparaison ; et, dans chaque bras, le coût dans le signal rendu à l'organisme** (N-045 v2, énoncé 2), sous une forme et un λ gelés avant la course, identiques dans les trois bras. Ce sont deux choses distinctes : l'égalité du budget apparie les bras ; l'énoncé 2 porte sur le signal servi à l'organisme.
5. **La dépense réelle est rapportée par bras** (N-058 juge sur le coût mesuré ; budget égal n'est pas dépense égale). Un bras qui ne dépense pas son budget n'est pas complété ; l'écart est rapporté, et le score est lu aussi par dollar dépensé, comme lecture secondaire.
6. **La règle qui retire des appels au bras qui lit une mémoire est gelée.** Le bras 3 paie dès la première génération une mémoire pleine, le bras 2 une mémoire vide : à budget égal, le bras 3 a moins d'appels. C'est voulu — le coût de la mémoire est dans la comparaison. Mais la façon de retirer les appels est fixée d'avance et la même pour tous : réduction du nombre de lots servis, **uniforme sur toutes les espèces et tous les rôles**, pour que la composition de l'organisme ne change pas entre bras.
7. **Cloisonnement entre bras.** Aucun dossier lisible n'est commun à deux continuations (un organisme qui lit des fichiers ne doit pas voir la mémoire d'un autre bras) ; les trois bras d'une même source reçoivent **la même suite de mondes plantés neufs** (graines des mondes dérivées par source et par génération, communes aux trois bras ; graines d'échantillonnage dérivées par bras).

- **Longueur** : K ≥ 3 générations par continuation — choix repris de l'horizon de l'énoncé 5 de N-045 v2, qui, lui, fixe l'horizon du signal rendu à ce qui conçoit et non la longueur d'une continuation.
- **Avant tout** : le pilote de bruit de N-045 v2, énoncé 6 (i) — deux courses du même bras, pour l'écart-type test-retest du score de l'oracle. Le nombre de sources vient de ce bruit, pas de l'effet de Yu et al. (leur effet standardisé de 1,28, p. 8, vient d'un autre concepteur sur un autre objet et ne vaut pas pour un calcul de puissance ici).

**Bras de diagnostic, à part des trois bras du critère, sans seuil, rapportés comme description :**

| bras de diagnostic | ce qu'il dit |
|---|---|
| D-a — mémoire héritée aux **résultats permutés** entre entrées | le contenu compte-t-il, ou la seule présence d'un texte ? |
| D-b — mémoire héritée **sans le champ de prédiction** | la prédiction apporte-t-elle, ou nuit-elle ? |
| D-c — **`historique` brut de la source** laissé en place, sans mémoire structurée | l'indice contraire de Meta-Harness (traces brutes contre résumé, tableau 3 p. 7) ; c'est aussi le bras que la règle 2 retire des trois autres |
| D-d — mémoire héritée où l'orchestrateur a **planté des entrées fausses** (résultat inversé, cause inventée) | part des proposeurs qui suivent une mémoire fausse, mesurée par l'oracle |
| D-e — mémoire héritée **paraphrasée** par un modèle d'une autre lignée | le gain tient-il au sens ou à la lettre (canal caché) ? |

**Les entrées fausses plantées ne vont que dans le bras D-d.** Mises dans les bras 2 ou 3, elles dégraderaient le traitement que le critère mesure (faille relevée par la contre-lecture). Les bras de diagnostic se jouent après les trois bras du critère, sur devis à part, et ne changent aucun verdict.

### c.5 Critère de réussite, mesuré par l'oracle du monde planté

- **Mesure principale** : le score de l'oracle du monde planté (N-058 : structures plantées retrouvées, témoins plantés vrais promus et faux rejetés) à la dernière génération, sur une famille **tenue à l'écart**, lue une seule fois en fin de boucle (N-050) ; à budget égal.
- **Jamais** le verdict d'un juge sur un agent ou sur un bras (N-053, point 5 ; N-058, point 2). Les fiches promues par le juge peuvent être rapportées comme information ; elles ne décident de rien.
- **Deux contrastes principaux, et deux seulement** : l'héritage (bras 3 moins bras 2) et la tenue (bras 2 moins bras 1), chacun en différence appariée par source.
- **Justesse des prédictions** (mesure rapportée, hors critère) : règle de score propre sur les tranches prédites, contre le taux de base obtenu en permutant les prédictions entre tentatives de la même génération ; par génération et par espèce.

### c.5 bis Règle de multiplicité

1. **Un seul test décide par contraste** : le test des rangs signés exact, bilatéral, par énumération des signes, sur les différences appariées par source. L'intervalle à 95 % du test t apparié est rapporté comme description ; il ne décide pas. (La version 1 faisait décider deux tests par contraste.)
2. **Deux contrastes, un risque global de 5 %**, tenu par la procédure de Holm sur les deux valeurs p : la plus petite est comparée à 0,025, l'autre à 0,05 si la première passe.
3. **Rien d'autre ne porte de seuil.** Le contraste « bras 3 moins bras 1 », la justesse des prédictions, la lecture par dollar dépensé et les cinq bras de diagnostic sont rapportés sans test décisif ; s'ils reçoivent une valeur p, elle est dite descriptive et non corrigée.
4. Seuils, nombre de sources, forme du score net et tranches de prédiction sont gelés au préenregistrement, après le pilote de bruit et avant toute lecture (R1).

### c.6 Ce qui la réfuterait

- **Héritage** : le contraste (bras 3 moins bras 2) ne passe pas son seuil, ou est négatif. Alors la mémoire transmise n'a pas d'effet établi au-delà de la tenue et de l'organisme hérité, et l'énoncé 5 ne peut pas s'appuyer sur elle.
- **Tenue** : le contraste (bras 2 moins bras 1) ne passe pas son seuil, ou est négatif, **à budget égal** : la mémoire structurée coûte ce qu'elle rapporte, ou davantage, face au seul `historique` ordinaire.
- **Prédiction** : la justesse ne dépasse pas le taux de base ; le champ n'est alors qu'une archive, et le bras D-b dit s'il nuit.
- **Contenu** : le bras D-a (résultats permutés) fait aussi bien que le bras 3 ; le gain ne vient pas de ce que la mémoire dit.
- **Forme** : le bras D-c (`historique` brut) fait aussi bien ou mieux que le bras 3 ; le rangement par problème n'ajoute rien aux traces, comme Meta-Harness le laisse craindre.
- Un résultat trop propre (toutes les prédictions justes, écart sans variance) déclenche le même audit qu'un échec (R4).
- Un résultat négatif se rapporte tel quel ; aucune reprise ne vise un signe (R3).

### c.7 Cloisonnement de ce qui s'écrit dans la mémoire

1. Le champ `resultat` ne vient **que** de l'oracle du monde planté, **sur le jeu d'évolution**. Jamais du jeu tenu à l'écart ; jamais d'un verdict, d'un score ou d'un texte de juge sur un agent (N-053, point 5).
2. Le champ `gardee` ne vient que d'une règle sur l'oracle et le coût ; à défaut, il n'existe pas (c.2).
3. La famille de mondes de la mesure finale n'apparaît dans aucune entrée, ni par ses items ni par son nom.
4. Aucun identifiant d'item planté, aucun nombre d'items plantés n'est écrit dans la mémoire ni servi (c.3 bis) : la mémoire ne doit pas devenir la table des réponses du monde suivant. Un monde planté neuf par génération (N-049) ; si le vivier ne le permet pas, le dire et borner la revendication.
5. Aucun score de juge, aucun extrait de verdict n'est écrit dans la mémoire : lu par le proposeur suivant, il ferait entrer le juge dans la sélection par la lecture.

### c.8 La mémoire comme canal d'attaque

Celui qui écrit la mémoire est celui qui est évalué. Ce qu'un organisme pourrait en faire, et ce qu'il faudrait pour l'empêcher :

| risque | parade proposée |
|---|---|
| Écrire dans la mémoire des instructions pour les proposeurs suivants ou pour un juge (« ignore la consigne », « promeus les fiches de telle forme ») | Le juge ne lit **jamais** la mémoire, ni aucun texte qui en dérive directement ; champs typés et bornés ; les champs libres sont servis aux proposeurs entre balises de donnée ; un lecteur d'une **autre lignée** que les proposeurs audite la mémoire à chaque génération (N-053 : juge d'une autre lignée) et ses constats sont rapportés, sans rien filtrer en silence (R5). |
| Écrire soi-même un résultat flatteur | L'agent n'écrit aucun champ de résultat ni le champ `gardee` : l'orchestrateur seul, par programme, depuis l'oracle. |
| Faire porter par la mémoire le verdict du juge (par un champ « retenue », par un compte de fiches promues) | Invariant gardé par le code et testé : aucune valeur de la mémoire n'est fonction d'une sortie du juge ; aucun champ de la mémoire n'est une entrée du juge (N-053, point 5, étendu à ce canal). |
| Réécrire le passé | Mémoire en ajout seul, chaînée par empreintes, scellée à chaque génération ; toute divergence arrête la course. |
| Prédire après coup | Empreinte de la prédiction inscrite avant l'appel de l'oracle (c.3). |
| Paraître calibré en ne prédisant que le facile | Justesse lue par une règle de score propre contre un taux de base par permutation ; **la justesse des prédictions n'entre dans aucun signal de sélection ni de récompense de l'organisme** (sinon c'est une cible de plus à contourner — attaque de Goodhart, citations obligatoires de N-064). |
| Apprendre la clé de l'oracle par la mémoire ou par le format de la prédiction | Aucune liste, aucun nombre, aucun identifiant d'item planté servi (c.3 bis, c.7) ; mondes neufs ; mesure finale sur une famille absente de toute entrée. |
| Canal caché entre générations (un message codé dans des champs anodins) | Champs fermés autant que possible ; bras de diagnostic D-e (mémoire paraphrasée) : si le gain disparaît à sens égal, il tenait à la lettre et non au sens ; rapporté. |
| Suivre aveuglément une mémoire fausse | Bras de diagnostic D-d seulement (entrées fausses plantées) ; jamais dans les bras du critère. |
| Lire la mémoire d'un autre bras | Dossiers séparés et illisibles d'un bras à l'autre (c.4, règle 7). |

Ce qu'il faudrait, en une phrase, pour qu'elle ne puisse pas servir à contourner le juge : **que l'agent n'écrive que des intentions, scellées avant l'essai ; que les faits soient écrits par un programme depuis l'oracle, au grain que tous les bras reçoivent déjà ; que rien du juge n'y entre et que le juge n'en lise rien ; et que la mesure finale porte sur un monde dont la mémoire ne sait rien.**

### c.9 Coût en jetons

Estimation de ce lecteur, **qui n'est pas un devis** :
- une tentative ≈ 250 jetons aux bornes de c.2 (hypothèse) ; mémoire plafonnée à 60 tentatives servies, soit ≈ 15 000 jetons par appel de proposeur ; au-delà du plafond, la règle de ce qui est servi (les plus récentes par problème, par exemple) est gelée au préenregistrement et la mémoire entière reste sur disque ;
- la course d'auto-conception jouée compte 55 appels de proposeurs par génération (cinq espèces, onze lots — devis v2b, ligne 11) : ≈ 825 000 jetons d'entrée de plus par génération ;
- au prix d'entrée le plus haut relevé le 18 novembre (10 USD par million de jetons, PO-130 du journal du compte organisme), c'est **8,25 USD au plus par génération et par bras qui sert une mémoire pleine** ; moins au prix réel du mélange d'espèces ;
- repère : les entrées des appels de Carbon étaient de 28 791 à 40 986 jetons (diagnostic `510312b1…`, § 2) ; 15 000 jetons de mémoire les alourdissent de 37 à 52 %. La mémoire n'est pas gratuite ; c'est pourquoi le budget est égal par bras et la règle de retrait des appels gelée (c.4, règles 4 à 6) ;
- trois bras du critère, K générations, n sources, puis jusqu'à cinq bras de diagnostic : le total se chiffre au devis, après le pilote de bruit. Rien n'est demandé ici.

### c.10 Première application sans dépense

La mémoire rétrospective de ce dossier (`memoire-retrospective-auto-conception-v2.md`) est une mémoire de ce format, reconstruite à la main sur les deux tentatives de la course d'auto-conception : 14 prédictions datées ; **6 justes, 3 fausses, 5 non vérifiables** avec une tolérance de ± 20 % sur les montants (**5 justes, 4 fausses, 5 non vérifiables** à ± 10 %) ; deux d'entre elles (A1, E2) sont contestables comme prédictions ; sur le problème qui a bloqué les deux courses, deux prédictions tranchées, deux fausses. Elle peut être versée à l'atelier d'idées comme matière première (N-072), sans rien engager.

### c.11 Réserves propres au plan

1. **Ce que mesure « l'héritage »** : seulement la mémoire au-delà de l'organisme hérité (c.4, règle 1). Un bras qui repartirait de l'organisme d'avant la source, avec la seule mémoire, séparerait l'héritage par le code de l'héritage par la mémoire ; il n'est pas proposé ici (quatrième bras du critère, coût en plus). C'est une borne de la revendication, à écrire.
2. **La forme fine de la prédiction** dépend d'un appariement par programme que ce lecteur n'a pas vérifié dans le code de l'oracle (c.3 bis). Sans lui, la prédiction est un signe et une tranche : plus pauvre que celle de Yu et al., et sa justesse sera plus difficile à distinguer du taux de base.
3. **Le champ `gardee`** peut ne pas exister du tout (c.2), si ce que l'organisme garde d'une génération à l'autre dépend du juge. La mémoire perd alors l'équivalent du champ « accepted » de Yu et al. (p. 22).
4. **Les règles 2 et 3 de c.4 rapprochent le bras 1 d'une mémoire brute** : il garde l'`historique` de sa propre continuation, au même grain que les autres. Le contraste « tenue » mesure donc le rangement, la justification, la prédiction et la provenance, face à un historique brut de même contenu — pas « une mémoire contre rien ». C'est le contraste de Yu et al. (leur bras sans mémoire garde aussi l'historique ordinaire, p. 20), mais l'effet attendu en est plus petit.
5. Cette version 2 du plan n'a pas été contre-lue.

---

## (d) Le courriel aux auteurs

Brouillon dans `courriel-auteurs-brouillon-v2.md` (question 4 corrigée : le bras « harnais seul » n'a pas la mémoire d'amélioration mais garde l'historique ordinaire ; la première ligne du tableau 1 décrite pour ce qu'elle est) (en anglais, sans nom ni adresse d'expéditeur). **Aucun envoi par cette session : contact externe, Lazar décide et envoie.** Il demande : les issues par tâche et par tirage de l'étude appariée ; les fichiers de mémoire des dix sources, pour la justesse des prédictions en agrégat ; le sens des champs `passed` et `total` ; l'existence d'un bras à mémoire vide tenue pendant la cible ; l'emploi des prédictions par le sélecteur ; le coût en jetons ; tout essai avec un concepteur fort.

---

## Réserves

1. **Lecteur unique pour la version 1 ; contre-lue par un lecteur d'un autre modèle (Opus 5.5), qui confirme les points 1 à 7 de la lecture du papier et le recalcul ; la version 2 elle-même n'est pas contre-lue.** Les chiffres relevés (tableaux 1 à 7 de Yu et al. ; tableau 2 de SkillHone ; tableau 3 de Meta-Harness) l'ont été sur le texte extrait par `pdftotext -layout`, page par page ; les figures n'ont pas été regardées comme images. Les valeurs des figures 3 et 4 n'ont été prises que des tableaux 5 et 6 qui les donnent.
2. **Le compte de 6 sur 18** porte sur trois enregistrements choisis par les auteurs. Il ne mesure pas la justesse des prédictions du système ; il montre seulement que le papier ne la donne pas et que ses propres exemples ne sont pas flatteurs.
3. **Champs `passed` et `total` non compris** : 49 sur 60, 45 sur 60, 47 sur 60 (source, figure 9 p. 28) ; 5 sur 33, 10 sur 36 (cible, figure 10 p. 29) — alors que les jeux d'évolution comptent 220 et 165 tirages (tableau 4, p. 18). L'évaluation d'un candidat ne porte donc pas sur tout le jeu, ou pas à cinq tirages ; le papier dit seulement que les cinq tirages par tâche sont « the separate evaluation allocation » (p. 5). Posé aux auteurs.
4. **La borne de bruit binomial** du recalcul (§ 5) est une borne haute sous une hypothèse fausse (tâches égales) ; elle sert à dire ce qui manque, pas à mettre en doute le test.
5. **Les lectures « d'où peut venir le gain »** (a.5) et « un concepteur fort peut s'en passer » (a.6) sont des hypothèses de ce lecteur ; le papier ne les teste pas. Contre la seconde : chez les deux voisins lus, le concepteur est Claude Opus 4.6 et retirer l'histoire coûte encore (SkillHone p. 4 et p. 6, ablation confondue ; Meta-Harness p. 5, p. 7, p. 15) — indices voisins, sur d'autres objets, qui ne testent pas la mémoire transmise.
6. **Versions** : SkillHone lu en version 4 d'arXiv (29 octobre 2026), non la version des actes que Yu et al. citent ; Meta-Harness en version 1 d'arXiv, non la version de conférence. Les pages citées sont celles des PDF empreintés.
7. **Voisins non lus**, cités de seconde main d'après Yu et al. : AHE (Lin et al.), RRSI (Xia et al.), HarnessBank, Causal Improvement Graph, Harness², PluginRSI, Xu (2026), Turbo Harness, Meta-Skill, Meta². Rien n'est dit libre (R8).
8. **Les modèles nommés** (Gemini 3.8 Flash, Claude Opus 5.5, Gemini 4 Argon, Grok 4.20) le sont tels que le papier les nomme ; « concepteur faible » est le mot de la consigne de la mère pour Gemini 3.8 Flash, non celui des auteurs. Le papier dit seulement que le remplacer par Opus donne des gains plus grands sur la source (p. 5, p. 24).
9. **La proposition (c)**, version 2, répond aux failles relevées par la contre-lecture (son point 10) ; cette version 2 n'a pas été contre-lue à son tour, ni chiffrée par un devis ; l'estimation de jetons repose sur une hypothèse de longueur d'entrée. Trois réserves propres au plan sont écrites en c.11.
10. **La mémoire rétrospective** : règle de classement écrite après coup par celui qui classe ; voir ses propres réserves.

---

## Corrections contestées

**Aucune des onze corrections n'est refusée.** Toutes ont été revérifiées sur la page ou la ligne citée (Yu p. 2, p. 5, p. 10, p. 20, p. 21 ; SkillHone p. 1, p. 4, p. 6 ; Meta-Harness p. 5, p. 15 ; devis v2b ligne 11 ; devis v2f ligne 11 ; journal du compte organisme, PO-161, PO-177) et appliquées. Deux précisions, qui ne sont pas des refus :

1. **Rédaction corrigée du § (b) 1, un mot.** Elle écrit « répétée sur dix paires dans un domaine (code) et faite une fois par condition dans les autres réglages ». Les deux réglages de code des tableaux 5 et 6 (p. 23, p. 24) sont eux aussi des courses uniques, hors des dix paires (a.2, point 6). « Dans les autres réglages » se lit correctement si « réglages » veut dire « toutes les comparaisons des tableaux 5 et 6 » ; pour lever le doute : « et faite une fois par condition dans les dix réglages des comparaisons principales, code compris ». La rédaction du contre-lecteur est reprise telle quelle au § (b) 1 ; ce mot est laissé à Lazar.
2. **Classement de D2 dans la mémoire rétrospective.** La correction est appliquée (part « proposition » : 47,26 estimés, 42,36 observés, − 10,4 % ; juste à ± 20 %, fausse à ± 10 %). Ce lecteur la tient pour le classement le plus fragile du tableau : l'observé compte 3 appels de Carbon au lieu de 11 et 47 appels de proposeurs au lieu de 55 ; une course allée au bout aurait coûté davantage. Le compte est donc donné aux deux seuils, comme demandé, et D2 porte la mention « biaisée par l'échec de Carbon ».
