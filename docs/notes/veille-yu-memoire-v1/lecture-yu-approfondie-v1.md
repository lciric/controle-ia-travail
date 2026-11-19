# Lecture approfondie de Yu et al. (2026), « Self-Improvement Memory Enables Continual Recursive Self-Improvement » — v1

## En-tête

- **Qui écrit** : lecteur neuf lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) sur la demande directe de Lazar ; modèle Fable 5.2 (`claude-fable-5-2`). Il n'a écrit ni la décision N-073, ni son complément 1, ni aucune pièce de la course d'auto-conception.
- **Heures** (`date -u`) : début 2026-11-19T06:59:14Z ; écriture de cette note à partir de 07:06Z.
- **Pièces lues, en entier, sur PDF, page par page (`pdftotext -layout`)** :

| pièce | fichier | empreinte | pages |
|---|---|---|---|
| Yu, Xia, Pan, Tang, Liu, Yu, Jiang, Chen, Xue et Yu, arXiv 2611.18856v1, 13 novembre 2026 | `docs/sources/arxiv-2611.18856-v1/arxiv-2611.18856.pdf` | `a8299ba5b16577dd328d602e32f35b914b9393ffb38148d2410f358d4d90ff3d` (vérifiée avant lecture) | 1 à 35, annexes A à F comprises |
| Li et Hu, « SkillHone », arXiv 2606.08671, version 4 du 29 octobre 2026 | `docs/sources/arxiv-2606.08671-v1/arxiv-2606.08671v4.pdf` (téléchargé le 19 novembre) | `3c6906004f965b52c323603cfcdcd2f336e3444c52de64c47eb577736729b002` | 1 à 11 |
| Lee, Nair, Zhang, Lee, Khattab et Finn, « Meta-Harness », arXiv 2603.28052, version 1 du 30 mars 2026 | `docs/sources/arxiv-2603.28052-v1/arxiv-2603.28052v1.pdf` (téléchargé le 19 novembre) | `7d9b90f53a9f4801a090f1a4acb843340cde81e4f865f97d53fff2a6a570eb73` | 1 à 10 et 14 à 26 lues ; 11 à 13 (bibliographie) non lues |

- Les identifiants des deux voisins ne sont pas dans la bibliographie de Yu et al. (SkillHone y est cité par ses actes, p. 11-12 ; Meta-Harness par sa page de conférence, p. 11) ; ils viennent de la recherche par titre de l'interface publique d'arXiv. Les versions lues sont celles d'arXiv ; les versions des actes n'ont pas été comparées (réserve 6).
- **Nos pièces** : `docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md` (§ 0 et § 1), `docs/decisions/decision-N-073-complement-1-memoire-transmise-v1.md`, `docs/decisions/decision-N-045-v2.md`, `docs/decisions/decision-N-058-v1.md`, `docs/decisions/decision-N-053-v1.md` (point 5).
- **Fichiers de ce dossier** : `recalcul_etude_appariee_v1.py` et `.txt` (le recalcul), `memoire-retrospective-auto-conception-v1.md` (notre mémoire reconstruite), `courriel-auteurs-brouillon-v1.md`.
- **Vocabulaire** : les auteurs nomment « SIM » leur mémoire d'auto-amélioration ; cette note écrit « la mémoire ». Les quatre conditions : « démarrage à froid » (harnais de départ, sans mémoire), « harnais seul » (harnais évolué sur la source, sans mémoire), « problèmes seuls » (harnais évolué et la seule liste des causes), « mémoire complète » (harnais évolué et l'enregistrement entier, tenu à jour pendant la cible) (p. 4, figure 6 p. 20). Un « tirage » est une exécution d'une tâche ; les scores sont sur 100.
- Aucune dépense, aucun appel à un modèle, aucune instance. Réseau : arXiv seul. Aucun refus d'outil.

---

## (a) Ce qui est solide et ce qui ne l'est pas

### a.1 Ce que le papier établit : une étude appariée, dix paires, un seul domaine

**Le plan** (p. 8, annexe C.4 p. 20). L'évolution du harnais « Terminus-2 » sur le banc de terminal source (Terminal-Bench 2.1) est répétée dix fois. Chaque harnais obtenu lance deux continuations de dix tours sur le banc cible (Terminal-Bench 4) : l'une hérite de la mémoire de sa source et la tient à jour, l'autre continue sans mémoire. « The independent source run is the unit of analysis » (p. 8). Modèle exécutant, concepteur (proposeur et sélecteur) : Gemini 3.8 Flash partout (p. 5, p. 19). Dix tours, cinq candidats par tour (p. 5).

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

**Ce que cette étude établit donc** : sur ce banc, depuis ce harnais, avec ce modèle pour tout faire, continuer avec la procédure complète finit plus haut que continuer sans aucune mémoire, de 2,4 points en moyenne, et l'écart ne tient pas à une paire.

### a.2 Ce que ce plan n'identifie pas

1. **L'héritage n'est pas séparé de la tenue d'une mémoire.** Le bras « harnais seul » n'a aucune mémoire pendant les dix tours de la cible ; le bras « mémoire complète » hérite **et** met à jour (« Full record; updated on target », figure 6 p. 20 ; « Each condition persists throughout target RSI », p. 20). Les auteurs le disent : « Our comparisons evaluate SIM as a complete procedure, combining inherited memory with updates during target optimization » (p. 10), et encore p. 16 et p. 23-24. **Aucun bras « mémoire vide au transfert, tenue pendant la cible » n'existe dans le papier** (cherché : § 3.3 p. 4-5, § 4.1 p. 5, annexes C.3 à C.6 p. 20-21, annexe E p. 22-25). La seule comparaison où une mémoire est tenue sans rien hériter est la première ligne du tableau 1 (p. 6) : sur Gemini 2.5 Flash, depuis le même harnais de départ, 22,4 avec mémoire contre 21,4 sans (« The first row tests SIM during an initial RSI run », p. 21) — une course par condition, à une décimale, un écart d'un point. L'effet mesuré par les dix paires peut donc venir de ce qui est transmis, de l'habitude de noter et relire pendant la cible, ou des deux ; le papier ne permet pas de le dire.
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

**Autres nombres, tous en course unique** : la chaîne de quatre générations de Gemini (tableau 1, p. 6 : 21,4 / 22,4 ; 73,3 / 76,8 ; 88,9 / 90,5 ; 95,6 / 94,8 — la continuation finit **plus bas** sur la dernière) ; le harnais partagé par trois modèles (tableau 2, p. 8 ; « Each procedure is run once, and optimization cost is not compared », p. 21) ; la rétention sur la source (figure 8, p. 24, « one run per condition ») ; le remplacement du concepteur par Claude Opus 5.5 (tableau 7, p. 25).

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
- **Aucun taux de justesse d'ensemble, aucune calibration, aucune comparaison à un taux de base** n'apparaît dans le papier. Cherché : toutes les pages où « predict » apparaît (1, 3, 4, 9, 15, 16, 22, 28, 29, 32, 35), plus les sections de résultats (p. 6-9) et d'ablations (p. 22-25).
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

- **La prédiction sert-elle au sélecteur ?** Aucune règle ne le dit. Le sélecteur « reads the same record » (p. 4) et pèse « performance, complexity, domain specificity, and regression risk » (p. 3). « accepted means the selector chose the edit in that round, even if some predicted fixes failed » (p. 22). Les deux tentatives de P8 ont été retenues alors qu'aucune des tâches visées n'a été réparée (p. 28) ; la seconde a ensuite été défaite (p. 27). Dans le texte, la prédiction est **archivée et relisible** ; rien ne montre qu'elle soit **notée**, ni qu'une prédiction manquée pèse sur un choix.
- **Si les prédictions échouent souvent alors que la mémoire aide, d'où peut venir le gain ?** Le papier ne le mesure pas. Ses propres cas pointent vers la justification et la provenance plutôt que vers la prédiction : sans mémoire, la course retouche quatre fois la même garde d'achèvement, deux fois pour réparer des blocages, et attribue à son premier tour une garde héritée de la source (p. 8-9, p. 29) ; en ingénierie, la course sans mémoire défait dès le premier tour les consignes héritées, la course avec mémoire les garde (p. 34). Savoir **pourquoi** une modification existe et **d'où** elle vient suffirait à expliquer ces deux cas. C'est une lecture de cas choisis, non un résultat ; un échec prédit puis observé peut aussi servir d'information (« unresolved predictions », p. 9, p. 35).
- **La prédiction écrite avant l'évaluation n'est pas propre à ce papier.** Les auteurs écrivent d'un travail antérieur : « AHE makes harness components and modification outcomes observable, checking edit-level predictions against subsequent task outcomes (Lin et al., 2026) » (p. 15 ; arXiv 2604.25850, non lu ici).

### a.6 Le concepteur fort : la mémoire n'y est pas testée

Dans toutes les comparaisons de mémoire, le proposeur et le sélecteur sont Gemini 3.8 Flash, « including when Opus executes the tasks » (p. 19 ; p. 5). L'annexe E.4.2 remplace ce concepteur par Claude Opus 5.5 **pendant l'évolution sur la source seulement** (« during TB2.1 source RSI », p. 24 ; tableau 7, p. 25) : elle compare l'amélioration de la source avec un concepteur ou l'autre, sans aucun bras de mémoire. Dans la transition « Opus vers Gemini » (tableau 6), Opus est le modèle qui **exécute** les tâches de la source ; le concepteur reste Gemini 3.8 Flash. **La mémoire n'est donc jamais testée avec un concepteur fort.** D'après le texte seul, le résultat ne se transporte pas à un organisme dont les proposeurs sont des modèles de frontière : un concepteur fort peut reconstruire seul, du code et des traces, ce que la mémoire rappelle à un concepteur faible — ou en tirer davantage. Le papier ne tranche ni l'un ni l'autre ; ses limites disent seulement que les procédures de planification et de recherche de l'optimiseur sont tenues fixes (p. 10).

### a.7 Les deux voisins, lus sur source

**SkillHone (Li et Hu ; déposé le 7 juin 2026, cinq mois avant Yu et al.).** Un harnais qui fait évoluer une « compétence » d'agent en tenant un historique persistant de décisions. Chaque pas est un enregistrement h = (diagnostic, révision candidate, preuve d'évaluation expurgée, issue), l'issue pouvant être « accepter, réviser, rejeter, différer » (p. 4) ; l'historique garde donc aussi les **révisions rejetées**, que la mémoire de Yu et al. ne garde pas (« only the chosen candidate is recorded », Yu p. 4). L'historique « acts as a persistent memory for the evolution process itself » (p. 4). Deux équipes à droits séparés : celle qui optimise ne voit jamais les cibles ni les validateurs, seulement des rapports expurgés (p. 2-3, tableau 6 p. 11). Ablation : sans l'historique de décisions, 64,6 → 51,2 sur GAIA et 66,4 → 55,5 sur WebWalkerQA (tableau 2, p. 6) ; sans la séparation des rôles, 58,2 et 61,1. **Le nombre de courses derrière ces chiffres n'est dit nulle part** ; la trajectoire montrée est « one SkillHone run » (p. 8-9) ; aucun intervalle. Pas de champ de prédiction. Pas de changement de modèle concepteur ni de transmission entre bancs : la mémoire sert la suite du même travail (le transfert montré est celui de la compétence finie vers un autre modèle exécutant, figure 3 p. 5). Coût : 39,9 millions de jetons d'entrée contre 1,48 pour la méthode comparée (tableau 5, p. 9).

**Meta-Harness (Lee et al., 30 mars 2026).** Une boucle extérieure dont le proposeur est un agent de code qui lit, par le système de fichiers, le code, les scores et les **traces d'exécution brutes de tous les candidats passés** (p. 1-2, p. 4) ; « the proposer reads a median of 82 files per iteration » (p. 2, tableau 8 p. 15). Aucune structure de mémoire : « instead of relying on a fixed scaffold, an archive of prior discoveries, or a persistent memory mechanism, it gives the proposer unrestricted filesystem access to prior experience » (p. 3). Ablation de ce que le proposeur voit (tableau 3, p. 7, classification de textes) : scores seuls, médiane 34,6 ; scores et **résumés**, 34,9 ; traces brutes, 50,0 — « summaries do not recover the missing signal, and may even hurt by compressing away diagnostically useful details » (p. 7). Le nombre de courses par condition n'est pas donné clairement (la colonne « > ZS » compte des « runs » : 26, 23, 39). Le proposeur écrit de lui-même des hypothèses chiffrées avant l'essai (« will yield +1–3pp », p. 17 ; « reduce wasted exploration episodes by 3–5 turns », p. 21) ; elles ne sont ni rangées ni confrontées en agrégat. Une ligne note un transfert entre courses (« Iteration 10: cross-run transfer », p. 17). Sur le banc de terminal, la recherche et l'évaluation finale portent sur les mêmes 89 tâches (p. 9).

**Ce que les deux voisins changent à la lecture de Yu et al.**
- Tenir un historique structuré du pourquoi des modifications, et l'ablater, est fait avant Yu et al. (SkillHone, p. 4 et p. 6). Yu et al. le citent en une ligne (p. 3, p. 16).
- Ce que Yu et al. ajoutent, d'après les trois textes : la transmission à travers un changement de banc ou de modèle, le rangement par problème récurrent avec plusieurs tentatives sous une même cause, et une étude appariée à dix sources. Le champ de prédiction existe ailleurs selon eux (AHE, p. 15).
- **Un indice contraire** vient de Meta-Harness : à information comprimée, la recherche fait moins bien qu'avec les traces brutes (tableau 3, p. 7). La mémoire de Yu et al. est un résumé ; leur bras « harnais seul » garde « the ordinary target-run history » (code, journaux, différences — p. 5, figure 2 p. 4) mais perd toute l'histoire de la source. Leur étude ne compare pas la mémoire structurée à l'accès aux traces brutes de la source.

### a.8 En une liste

**Solide** : (1) l'arithmétique de l'étude appariée — tout concorde au recalcul ; (2) sur un banc de code, un harnais, un modèle, la procédure complète bat la continuation sans mémoire de 2,36 points (39 tirages sur 1 650), sans dépendre d'une paire ; (3) la franchise du papier sur ses limites (p. 6, p. 10, p. 21).

**Pas solide, ou non établi** : (1) que l'**héritage** cause le gain — non séparé de la tenue d'une mémoire ; (2) que l'enregistrement complet vaut mieux que la liste des causes — dix courses uniques ; (3) tout résultat hors du code ; (4) la valeur de la prédiction écrite — un tiers de réussite sur les exemples publiés, 1 sur 8 sur la cible, aucun agrégat, aucun rôle dans la sélection ; (5) la tenue du résultat avec un concepteur fort — non testé ; (6) le coût — non apparié, non rapporté ; (7) le titre (« Enables ») va au-delà de ce que le plan identifie.

---

## (b) Ce qui change pour nos revendications

**Rien ne s'applique par cette note : toute modification de revendication est un nœud de Lazar. Ce qui suit est proposé.**

1. **La phrase du complément 1 de N-073 est trop généreuse, sur deux points.** Elle dit : « la question que Yu et al. (2026) posent pour le score d'un harnais d'agent par une ablation appariée de la mémoire transmise (mémoire complète contre harnais seul, à départ égal) ».
   - *« ablation … de la mémoire transmise »* : ce qui est ablaté est la procédure entière, mémoire héritée **et** tenue pendant la cible (p. 10, p. 20). Yu et al. ne posent pas la question causale de l'héritage au sens où notre énoncé 5 l'entend (« l'archive héritée cause-t-elle… ») ; ils posent : la procédure complète fait-elle mieux que rien ?
   - *« appariée »* : vrai pour dix paires, un domaine, un harnais, un concepteur (p. 8). Tout le reste est une course par condition (p. 6).
   - **Rédaction proposée**, à la place : « Yu et al. (2026) comparent, à départ égal et sur dix paires dans un seul domaine, une procédure complète — mémoire héritée puis tenue à jour pendant la cible — à la continuation sans aucune mémoire ; de leur propre aveu, leur plan ne sépare pas ce qui est hérité de ce qui est noté en route. Nous posons, pour des découvertes et non pour le score d'un banc, la question que ce plan laisse ouverte : l'archive **héritée** cause-t-elle les découvertes, au-delà du fait de tenir une archive ? »
   - Cette rédaction ne dit pas la question « libre » : sur six travaux que Yu et al. citent comme réemployant une expérience d'amélioration (Xu 2026 ; Harness² ; PluginRSI ; HarnessBank ; RRSI ; Causal Improvement Graph — p. 3, p. 15-16), aucun n'a été lu ici. « Non séparé chez Yu et al. » n'est pas « séparé par personne » (R8).
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
8. **Aucun chiffre de cette note n'entre dans un préenregistrement ou un papier sans relecture de la page citée** (R7). Les chiffres de Yu et al. cités au-delà des pages 1 à 4 et 9 à 10 du complément 1 sont désormais lus, page à l'appui, par ce lecteur seul ; ils n'ont pas été contre-lus.

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
| `prediction` | le proposeur | à la proposition, **scellée avant toute évaluation** | une liste fermée : quels items plantés du monde d'évolution la tentative fera retrouver (identifiants opaques), et un signe attendu sur le coût (plus, moins, égal). Aucun texte libre. |
| `resultat` | **l'orchestrateur, par programme** | après l'évaluation | items plantés retrouvés et manqués parmi les prédits ; nombre retrouvé parmi les non prédits ; coût mesuré. Aucun texte. |
| `retenue` | l'orchestrateur | après la sélection | oui ou non ; **les tentatives non retenues sont gardées** (SkillHone, p. 4 ; contrairement à Yu et al., p. 4) |
| `provenance` | l'orchestrateur | à l'écriture | génération, espèce du proposeur, famille du monde planté, version de l'orchestrateur, empreinte de la configuration |

L'entrée de Yu et al. (annexe D.3, p. 22) est reprise pour `probleme`, `tentative`, `prediction`, `resultat`, `provenance` ; s'en écartent : le résultat écrit par programme, les rejets gardés, le texte libre borné.

### c.3 Moment du scellement

La prédiction est scellée par son empreinte, inscrite au manifeste de la génération, **avant** que l'oracle soit appelé pour cette tentative (engagement scellé, comme la statistique de N-064). Le programme refuse d'évaluer une tentative sans empreinte de prédiction ; il refuse d'écrire un résultat dont la prédiction ne correspond pas à l'empreinte. Garde éprouvée sur un cas sain et sur un artefact (R5) : une prédiction modifiée après coup doit faire échouer l'écriture.

### c.4 Plan à trois bras, apparié par source

Pour chaque **source** indépendante (une course d'organisme de K générations sur une famille de mondes plantés, graines dérivées par `SeedSequence`, R9), trois continuations depuis le même état, sur une famille de mondes plantés **neuve** :

| bras | mémoire au départ | mémoire pendant la course |
|---|---|---|
| 1 — sans mémoire | aucune | aucune |
| 2 — mémoire neuve tenue | vide | tenue et servie |
| 3 — mémoire héritée | celle de la source | tenue et servie |

- **Bras 3 moins bras 2 = effet de l'héritage.** C'est le contraste que Yu et al. n'ont pas (p. 10).
- **Bras 2 moins bras 1 = effet de tenir une mémoire.**
- Bras 3 moins bras 1 = la « procédure complète » de Yu et al., pour comparaison.
- Mêmes proposeurs, mêmes juges, même nombre de générations ; **budget en dollars égal par bras** (N-045 v2, énoncé 2 : le coût dans le signal). Les jetons de la mémoire servie sont payés sur le budget du bras : un bras qui lit sa mémoire a moins d'appels.
- K ≥ 3 générations par continuation (N-045 v2, énoncé 5).
- **Avant tout** : le pilote de bruit de N-045 v2, énoncé 6 (i) — deux courses du même bras, pour l'écart-type test-retest du score de l'oracle. Le nombre de sources vient de ce bruit, pas de l'effet de Yu et al. (leur effet standardisé de 1,28, p. 8, vient d'un concepteur faible sur un autre objet et ne vaut pas pour un calcul de puissance ici).
- Bras de diagnostic possibles, hors critère : mémoire aux **résultats permutés** entre entrées (le contenu compte-t-il, ou la seule présence d'un texte ?) ; mémoire **sans le champ de prédiction** ; accès aux **traces brutes** de la source au lieu de la mémoire (l'indice contraire de Meta-Harness, tableau 3 p. 7).

### c.5 Critère de réussite, mesuré par l'oracle du monde planté

- **Mesure principale** : le score de l'oracle du monde planté (N-058 : structures plantées retrouvées, témoins plantés vrais promus et faux rejetés) à la dernière génération, sur une famille **tenue à l'écart**, lue une seule fois en fin de boucle (N-050) ; à budget égal.
- **Jamais** le verdict d'un juge sur un agent ou sur un bras (N-053, point 5 ; N-058, point 2). Les fiches promues par le juge peuvent être rapportées comme information ; elles ne décident de rien.
- **Réussite de l'héritage** : la différence appariée (bras 3 moins bras 2), par source, a un intervalle à 95 % au-dessus de zéro, et le test des rangs signés exact est sous le seuil gelé. Seuil, nombre de sources et forme du score net sont gelés au préenregistrement, après le pilote de bruit et avant toute lecture.
- **Réussite de la tenue** : même critère sur (bras 2 moins bras 1).
- **Justesse des prédictions** (mesure rapportée, hors critère de réussite) : part des items prédits effectivement retrouvés, contre le taux de base obtenu en permutant les prédictions entre tentatives de la même génération ; par génération et par espèce.

### c.6 Ce qui la réfuterait

- **Héritage** : l'intervalle de (bras 3 moins bras 2) contient zéro ou est négatif. Alors la mémoire transmise n'a pas d'effet établi au-delà de la tenue, et l'énoncé 5 ne peut pas s'appuyer sur elle.
- **Tenue** : l'intervalle de (bras 2 moins bras 1) contient zéro ou est négatif **à budget égal** : la mémoire coûte ce qu'elle rapporte, ou davantage.
- **Prédiction** : la justesse ne dépasse pas le taux de base ; le champ n'est alors qu'une archive, et le bras « sans prédiction » dit s'il nuit.
- **Contenu** : le bras aux résultats permutés fait aussi bien que le bras 3 ; le gain ne vient pas de ce que la mémoire dit.
- Un résultat trop propre (toutes les prédictions justes, écart sans variance) déclenche le même audit qu'un échec (R4).
- Un résultat négatif se rapporte tel quel ; aucune reprise ne vise un signe (R3).

### c.7 Cloisonnement

1. Le champ `resultat` ne vient **que** de l'oracle du monde planté, **sur le jeu d'évolution**. Jamais du jeu tenu à l'écart ; jamais d'un verdict, d'un score ou d'un texte de juge sur un agent (N-053, point 5).
2. La famille de mondes de la mesure finale n'apparaît dans aucune entrée, ni par ses items ni par son nom.
3. Les identifiants d'items plantés servis dans la mémoire sont opaques et propres à une génération : la mémoire ne doit pas devenir la table des réponses du monde suivant. Un monde planté neuf par génération (N-049) ; si le vivier ne le permet pas, le dire et borner la revendication.
4. Aucun score de juge, aucun extrait de verdict n'est écrit dans la mémoire : lu par le proposeur suivant, il ferait entrer le juge dans la sélection par la lecture.

### c.8 La mémoire comme canal d'attaque

Celui qui écrit la mémoire est celui qui est évalué. Ce qu'un organisme pourrait en faire, et ce qu'il faudrait pour l'empêcher :

| risque | parade proposée |
|---|---|
| Écrire dans la mémoire des instructions pour les proposeurs suivants ou pour un juge (« ignore la consigne », « promeus les fiches de telle forme ») | Le juge ne lit **jamais** la mémoire ni rien qui en dérive sans passer par l'aiguilleur ; champs typés et bornés ; les champs libres sont servis aux proposeurs entre balises de donnée ; un lecteur d'une **autre lignée** que les proposeurs audite la mémoire à chaque génération (N-053 : juge d'une autre lignée) et ses constats sont rapportés, sans rien filtrer en silence (R5). |
| Écrire soi-même un résultat flatteur | L'agent n'écrit aucun champ de résultat : l'orchestrateur seul, par programme, depuis l'oracle. |
| Réécrire le passé | Mémoire en ajout seul, chaînée par empreintes, scellée à chaque génération ; toute divergence arrête la course. |
| Prédire après coup | Empreinte de la prédiction inscrite avant l'appel de l'oracle (c.3). |
| Paraître calibré en ne prédisant que le facile, ou en prédisant tout | Justesse lue contre un taux de base par permutation, avec rappel et précision ; **la justesse des prédictions n'entre dans aucun signal de sélection ni de récompense de l'organisme** tant qu'elle n'est pas montrée robuste (sinon c'est une cible de plus à contourner — attaque de Goodhart, citations obligatoires de N-064). |
| Transmettre les réponses du monde planté d'une génération à l'autre | Mondes neufs et identifiants opaques (c.7, point 3) ; mesure finale sur une famille absente de toute entrée. |
| Canal caché entre générations (un message codé dans des champs anodins) | Champs fermés autant que possible ; bras de diagnostic « mémoire paraphrasée par un modèle d'une autre lignée » : si le gain disparaît à sens égal, il tenait à la lettre et non au sens ; rapporté. |
| Suivre aveuglément une mémoire fausse | **Témoins plantés dans la mémoire** : quelques entrées fausses par construction (un résultat inversé, une cause inventée), connues de l'orchestrateur seul ; la part des proposeurs qui les suivent est mesurée par l'oracle et rapportée. |
| Faire porter par la mémoire ce que le juge devrait décider | Invariant gardé par le code et testé : aucun champ de la mémoire n'est une entrée du juge ; aucun score de juge n'est une entrée de la mémoire (N-053, point 5, étendu à ce canal). |

Ce qu'il faudrait, en une phrase, pour qu'elle ne puisse pas servir à contourner le juge : **que l'agent n'écrive que des intentions, scellées avant l'essai ; que les faits soient écrits par un programme depuis l'oracle ; que le juge n'en lise rien ; et que la mesure finale porte sur un monde dont la mémoire ne sait rien.**

### c.9 Coût en jetons

Estimation de ce lecteur, **qui n'est pas un devis** :
- une tentative ≈ 250 jetons aux bornes de c.2 (hypothèse) ; mémoire plafonnée à 60 tentatives servies, soit ≈ 15 000 jetons par appel de proposeur ; au-delà du plafond, la règle de ce qui est servi (les plus récentes par problème, par exemple) est gelée au préenregistrement et la mémoire entière reste sur disque ;
- la course d'auto-conception jouée compte 55 appels de proposeurs par génération (cinq espèces, onze lots — manifestes de fin) : ≈ 825 000 jetons d'entrée de plus par génération ;
- au prix d'entrée le plus haut relevé le 18 novembre (10 USD par million de jetons, PO-130 du journal du compte organisme), c'est **8,25 USD au plus par génération et par bras qui sert une mémoire** ; moins au prix réel du mélange d'espèces ;
- repère : les entrées des appels de Carbon étaient de 28 791 à 40 986 jetons (diagnostic `510312b1…`, § 2) ; 15 000 jetons de mémoire les alourdissent de 37 à 52 %. La mémoire n'est pas gratuite ; c'est pourquoi le budget est égal par bras ;
- trois bras, K générations, n sources : le total se chiffre au devis, après le pilote de bruit. Rien n'est demandé ici.

### c.10 Première application sans dépense

La mémoire rétrospective de ce dossier (`memoire-retrospective-auto-conception-v1.md`) est une mémoire de ce format, reconstruite à la main sur les deux tentatives de la course d'auto-conception : 14 prédictions datées, 5 justes, 4 fausses, 5 non vérifiables ; sur le problème qui a bloqué les deux courses, 3 fausses sur 3. Elle peut être versée à l'atelier d'idées comme matière première (N-072), sans rien engager.

---

## (d) Le courriel aux auteurs

Brouillon dans `courriel-auteurs-brouillon-v1.md` (en anglais, sans nom ni adresse d'expéditeur). **Aucun envoi par cette session : contact externe, Lazar décide et envoie.** Il demande : les issues par tâche et par tirage de l'étude appariée ; les fichiers de mémoire des dix sources, pour la justesse des prédictions en agrégat ; le sens des champs `passed` et `total` ; l'existence d'un bras à mémoire vide tenue pendant la cible ; l'emploi des prédictions par le sélecteur ; le coût en jetons ; tout essai avec un concepteur fort.

---

## Réserves

1. **Lecteur unique, non contre-lu.** Les chiffres relevés (tableaux 1 à 7 de Yu et al. ; tableau 2 de SkillHone ; tableau 3 de Meta-Harness) l'ont été sur le texte extrait par `pdftotext -layout`, page par page ; les figures n'ont pas été regardées comme images. Les valeurs des figures 3 et 4 n'ont été prises que des tableaux 5 et 6 qui les donnent.
2. **Le compte de 6 sur 18** porte sur trois enregistrements choisis par les auteurs. Il ne mesure pas la justesse des prédictions du système ; il montre seulement que le papier ne la donne pas et que ses propres exemples ne sont pas flatteurs.
3. **Champs `passed` et `total` non compris** : 49 sur 60, 45 sur 60, 47 sur 60 (source, figure 9 p. 28) ; 5 sur 33, 10 sur 36 (cible, figure 10 p. 29) — alors que les jeux d'évolution comptent 220 et 165 tirages (tableau 4, p. 18). L'évaluation d'un candidat ne porte donc pas sur tout le jeu, ou pas à cinq tirages ; le papier dit seulement que les cinq tirages par tâche sont « the separate evaluation allocation » (p. 5). Posé aux auteurs.
4. **La borne de bruit binomial** du recalcul (§ 5) est une borne haute sous une hypothèse fausse (tâches égales) ; elle sert à dire ce qui manque, pas à mettre en doute le test.
5. **Les lectures « d'où peut venir le gain »** (a.5) et « un concepteur fort peut s'en passer » (a.6) sont des hypothèses de ce lecteur ; le papier ne les teste pas.
6. **Versions** : SkillHone lu en version 4 d'arXiv (29 octobre 2026), non la version des actes que Yu et al. citent ; Meta-Harness en version 1 d'arXiv, non la version de conférence. Les pages citées sont celles des PDF empreintés.
7. **Voisins non lus**, cités de seconde main d'après Yu et al. : AHE (Lin et al.), RRSI (Xia et al.), HarnessBank, Causal Improvement Graph, Harness², PluginRSI, Xu (2026), Turbo Harness, Meta-Skill, Meta². Rien n'est dit libre (R8).
8. **Les modèles nommés** (Gemini 3.8 Flash, Claude Opus 5.5, Gemini 4 Argon, Grok 4.20) le sont tels que le papier les nomme ; « concepteur faible » est le mot de la consigne de la mère pour Gemini 3.8 Flash, non celui des auteurs. Le papier dit seulement que le remplacer par Opus donne des gains plus grands sur la source (p. 5, p. 24).
9. **La proposition (c)** n'a été ni chiffrée par un devis ni contre-lue ; l'estimation de jetons repose sur une hypothèse de longueur d'entrée.
10. **La mémoire rétrospective** : règle de classement écrite après coup par celui qui classe ; voir ses propres réserves.
