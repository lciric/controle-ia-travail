# Lecture 09 sur source — « Lineage Is Memory: Parent Inheritance and Feedback Disclosure in Short-Budget LLM-Guided Optimization » (Shanglin Yang, Zhan Shi, arXiv 2610.41157) — v1

Écrite le 18 novembre 2026 (vers 06:20 UTC). Aucun commit, aucune dépense, aucun résultat sous embargo ouvert. Lecture entière sur PDF : pages 1 à 18 (texte, tables 1 à 8, annexes A et B) et 19-20 (bibliographie). Les deux figures par leurs légendes seulement. En plus : le dépôt public de code que la notice cite (fichier de présentation, préenregistrements, journal des commits) et l'archive des journaux de lancements, **dont j'ai recalculé deux tables** par un programme à moi.

Revendications visées par la table de veille : 8 (l'héritage d'une génération est récompensé ; mémoire transmise et effets différés) et 10 (mémoire de l'organisme). J'ajoute un mot sur la 9 (le séquentiel contre le meilleur de N tirages), que le travail touche de plus près que les deux autres.

## 0. Verdict en trois lignes

1. **Le travail ne prend rien à la revendication 8 et n'affaiblit pas sa prémisse ; il la soutient plutôt, à un autre étage.** Il compare, à nombre d'évaluations égal, « chaque proposition repart de la graine » (un meilleur de N tirages) à « chaque proposition réécrit le meilleur candidat courant » (une seule lignée, gloutonne), sur des invites et de petits programmes. L'héritage gagne largement sur les tâches bâties pour cela. Mais il n'y a ni concepteur qui apprend, ni signal de mérite à régler, ni population, ni archive : c'est un **voisin**, pas un occupant.
2. **La crainte de la table de veille — « ce qui s'hérite utilement serait l'artefact et non la mémoire » — n'est pas mesurée par ce travail.** Il n'a aucun bras où une mémoire existe à côté de l'artefact : le « résumé des échecs » est un résumé, refait à chaque tour, des échecs de la graine, pas une mémoire de la trajectoire. Les auteurs écrivent eux-mêmes que le contrôle manque (p. 14). Le titre (« la lignée est la mémoire ») est une définition, pas un résultat.
3. **Ce qui nous arrange se dit avec quatre réserves** : budgets très courts seulement (7 propositions pour les invites, 11 pour le code) ; cinq des sept tâches principales construites en cachant des règles à la graine, ce qui « favorise les méthodes qui accumulent » (p. 5) ; le bras « graine » n'a jamais la même information que le bras « parent » ; et le préenregistrement, daté par les auteurs eux-mêmes, n'a pas de tiers qui l'horodate (toute l'étude tient en deux jours, le dépôt public naît d'un seul commit). En revanche les chiffres des tables se **recalculent à l'identique** depuis les journaux publiés.

## 1. Source versée

Dossier : `docs/sources/pdf/veille-exploration-idees-v1/lecture-09-arxiv-2610.41157/` (chaque pièce a son compagnon `.sha256`).

| Pièce | Empreinte SHA-256 |
|---|---|
| `arxiv-2610.41157v1.pdf` (20 pages, 913 225 octets) | `3b0b0c0c8cc30d529b33fdbfccbf5df552ce6f6e642e07e4ee5f44c256444b72` |
| `page-abs-arxiv-2610.41157.html` (page de résumé d'arXiv) | `59125237977a123c2a92b644438604f3ac73d393ae9595cadfd60f4fdbd82a1f` |
| `depot-code-journal-des-commits.txt` (13 commits) | `fa45e5e1972b1ce5866cab7c5b817322efe6cd77b81d6d10c4e0bfa85dc772f2` |
| `depot-code-66141bb-README.md.txt` | `cde5cf81b11435b84a3a3e2ee7d094e1e80d8ff3960b3e23af2086489df52ed0` |
| `depot-code-66141bb-preregistration-en.md.txt` (traduction anglaise) | `5c9d9edb986b41e01f18b2cb3be9cae327435fe8116563acb1cdce600c48a2b3` |
| `depot-code-66141bb-preregistration-zh.md.txt` (original chinois) | `fd9d3a6debb6f524eb8eed6475a70d65e9961a6d88bb25fd2e86b5c58765fa11` |
| `depot-code-66141bb-liste-des-fichiers.txt` | `46aa203460a4f72da1509508b43261e54f6d67f83fb424ee833863371ec75055` |
| `adresse.txt` (adresses, dates, versions, refus, jusqu'où lu) | `cd18796e1ade6b449a7caa32d6dab0539f5829ff26a30cb840e936479bd5ed9a` |

Le PDF a la même empreinte que la copie déjà versée par la voie « citations » (`../citations-arxiv-2610.41157v1.pdf`) : la table de veille le disait « absent du dépôt », il l'était des notes, pas des sources.

Archive des journaux de lancements (`results/runs.tar.gz` du dépôt des auteurs, commit `66141bb`, 8 106 831 octets, SHA-256 `131b0f763b06410ec2f1f43520d411c623a8ed7dea641beec9b1244e4e8e0589`) : lue en mémoire, **non versée** (poids), adresse épinglée au commit dans `adresse.txt`. Mon programme de recalcul et sa sortie : `docs/notes/veille-exploration-idees-v1/programmes-lecture-09-v1/recalcul_journaux_publies.py` (`42013f26…203704`) et `recalcul-journaux-publies-sortie-v1.txt` (`4a233dc4…92644a`).

Récupération le 18 novembre 2026 entre 06:02 et 06:12 UTC, par `curl` et `git`, sans contournement. Refus notés et non insistés : l'interface `export.arxiv.org/api/query` (429) ; l'interface et la page de GitHub (403 du relais de la session) — le fichier de présentation et les fichiers ont été lus par l'adresse brute, l'historique par `git`, comme aux lectures précédentes. Documents traités en données : jamais exécutés, Python lancé avec `-I`. **Aucune consigne adressée au lecteur** relevée ; le PDF cite ses propres gabarits d'invite (p. 15-18), c'est l'objet étudié.

## 2. Date de première version

- **arXiv : une seule version, v1, vendredi 30 octobre 2026, 02:31:45 UTC**, déposée par Zhan Shi (page de résumé versée). Classe principale « génie logiciel ». Aucun lieu de publication annoncé : prépublication non relue par des pairs.
- **Dépôt public de code** (`github.com/shangliy/lineage-is-memory`) : premier commit le **28 octobre 2026 à 22:42:40, heure du Pacifique** (29 octobre, 05:42 UTC), `0fc25a8`. Ce seul commit apporte ensemble le code, l'archive des journaux, les deux fichiers de préenregistrement et un PDF du papier. Tête : `66141bb`, 2 novembre 2026.
- **Préenregistrements** : datés par les auteurs du 27 octobre 2026 (lots 1 à 3) et du 28 octobre (lot 4 à 16:05, lot 5 à 21:03:49, heure du Pacifique) dans le fichier chinois « qui fait foi ». Le dernier lot est donc préenregistré 1 h 39 avant le premier commit public.
- **Par rapport au programme** : N-045 v2 (l'héritage récompensé) est du 25 octobre 2026. Le travail lui est postérieur de cinq jours ; il ne lui prend aucune antériorité, et le programme n'en revendiquait pas (recherche bibliographique « obligatoire avant de revendiquer »).

## 3. Ce que le travail fait

Une boucle d'amélioration : un modèle « proposeur » reçoit un candidat (une invite système, ou une fonction Python), un retour sur ses échecs, et écrit un nouveau candidat ; on évalue ; on garde le meilleur. Deux facteurs croisés (p. 1-2, 4) :

- **La lignée** : `graine` — chaque proposition repart du candidat initial, « which corresponds to best-of-N resampling from the seed's feedback » (p. 1) ; `parent` — chaque proposition réécrit le meilleur candidat courant (« greedy parent inheritance »). Un candidat ne remplace le meilleur que s'il fait strictement mieux sur le jeu de recherche (p. 4).
- **Ce qu'on montre au proposeur** : rien ; les 4 premiers échecs ; 4 échecs choisis pour leur diversité ; 4 exemples tirés au hasard (réussis ou ratés) ; un résumé de tous les échecs groupés en 3 à 7 motifs par un appel de modèle, sans puis avec la réponse attendue (p. 4).

**Les trois questions de la table de veille.**

- *Budgets courts seulement ?* **Oui, et c'est dans le titre.** 8 évaluations pour les invites (la graine plus 7 propositions), 12 pour le code (la graine plus 11), arrêt dès que le jeu de recherche est résolu (p. 4). Aucun bras à budget plus long. Les auteurs bornent eux-mêmes : « on larger tasks where B rounds of k = 4 failures cannot cover the error space, wider per-round disclosure may retain an advantage beyond round 4 » (p. 14).
- *Un bras à plusieurs générations ?* **Au sens faible seulement.** Le bras `parent` enchaîne jusqu'à 7 (ou 11) réécritures le long d'**une seule lignée**. Pas de population, pas d'archive, pas de second parent : « Secondary inspiration candidates are disabled in all cells » (p. 4). Rien ne s'apprend d'un lancement à l'autre. L'optimiseur d'invites GEPA, qui garde un front de plusieurs parents, n'entre que comme comparaison de systèmes entiers (p. 4-5, 12).
- *Qu'est-ce qui s'hérite ?* **Le texte du candidat, et rien d'autre.** Pas de notes, pas d'historique des candidats passés, pas de résumé cumulé : « Under seed resetting, the proposer has no persistent state » (p. 13). Les auteurs décomposent l'effet du bras `parent` en trois mécanismes **qu'ils ne séparent pas** : le texte garde les règles trouvées ; les cas résolus sortent de la liste des échecs, donc de nouveaux échecs entrent dans la fenêtre de 4 ; la correction se fait en plusieurs pas (p. 4).

**Tâches** (table 1, p. 5) : sept principales — cinq construites par les auteurs (nommer le format d'une chaîne, réécrire une date, router un ticket, deux analyseurs en Python) plus une tâche de réponses au client notée sur grille, plus ScoNe (implication avec négation) ; deux d'extension publiques (un sous-ensemble de 12 intentions de Banking77, et la détection d'erreurs de traduction de BIG-Bench Hard). Jeux de recherche de 16 à 36 exemples, jeux tenus à l'écart de 12 à 72 exemples, **des mêmes catégories** (par exemple « 24 (2/cat) » des deux côtés).

**Modèles** : gpt-4.1-mini dans tous les rôles ; réplique sur claude-haiku-5-5 (cinq tâches) ; un proposeur plus gros, gpt-4.1, sur trois tâches (p. 2, 8).

## 4. Ce qui est mesuré, ce qui est seulement affirmé

**Mesuré** (chiffres lus sur le PDF, pages citées ; 10 lancements par cellule, 1 750 lancements en cinq lots, p. 6) :

- *L'effet de la lignée.* Précision tenue à l'écart du meilleur candidat, `parent` moins `graine`, moyenne sur quatre affichages et sept tâches, gpt-4.1-mini : **+0,238 [+0,224 ; +0,252]** (table 2A, p. 7). Par tâche : de −0,002 (dates) et +0,010 (ScoNe), où le modèle sait déjà sans retour, à +0,492 (réponses au client). Sur claude-haiku-5-5, cinq tâches : +0,222 (table 3, p. 8). Sur les deux tâches publiques : **+0,088 [+0,045 ; +0,130]**, dont +0,158 sur Banking77 et +0,017 sur l'autre (table 7, p. 15).
- *Contre le bras « graine » le mieux informé.* Les 4 premiers échecs avec lignée battent le résumé de tous les échecs sans lignée de +0,157 [+0,124 ; +0,195] (table 2B, p. 7).
- *Un proposeur plus gros.* Remplacer gpt-4.1-mini par gpt-4.1 comme proposeur ne gagne rien dans aucune des cinq cellules testées (de −0,069 à +0,002), sur trois tâches ; l'effet de la lignée y reste +0,380 (table 3, p. 8).
- *Le classement des affichages change avec l'horizon* (table 5C, p. 11, précision sur le jeu de recherche, cinq tâches) : avec lignée, le résumé groupé devance les 4 premiers échecs de +0,146 au pas 1 et de +0,173 au pas 2, puis de −0,017 au pas 4 et de −0,015 au pas 7 ; sans lignée, il garde +0,180 d'avance au pas 7. L'appel de résumé coûte jusqu'à 2,08 fois plus de jetons (p. 12).
- *Où part le budget de GEPA* : 2 à 15 % des jetons dans la réflexion du proposeur, 85 à 98 % dans les validations (p. 12).

**Par qui c'est jugé.** Par un correcteur programmé (égalité exacte, ou exécution de 24 cas pour le code) partout, sauf la tâche de réponses au client : là, un seul juge, gpt-4.1-mini à température nulle, qui est aussi le modèle de tâche et le proposeur (p. 4, 14, 18). Le candidat retenu est choisi sur le jeu de recherche et lu une fois sur le jeu tenu à l'écart (p. 4).

**Données et code publiés : oui.** Code sous licence MIT, 1 750 journaux avec chaque candidat et son retour. **Recalcul fait par moi** depuis l'archive (programme et sortie cités en section 1) : les 77 moyennes de la table 2A et les quatre lignes de la table 5C sortent **à l'identique** ; l'effet de la lignée +0,2382 ; mon intervalle à strates fixes [+0,224 ; +0,252] ; mon intervalle à deux niveaux (tâches, puis lancements) [+0,107 ; +0,364], que le PDF donne à [+0,104 ; +0,363] (p. 6).

**Un écart entre le texte et les journaux, trouvé par ce recalcul.** La table 1 (p. 5) donne la note de la graine : 0,00 sur la tâche des formats, 0,75 sur les dates, 0,00 sur les réponses au client, 0,21 sur le second analyseur. Dans les journaux publiés, le premier candidat consigné (dont le texte est bien la graine) a 0,25, 0,083, 0 à 0,125 (le plus souvent 0,06 ou 0,125) et 0,375 sur le jeu de recherche (sortie du recalcul, point 4). Les trois autres tâches principales concordent. Les tables de résultats ne sont pas touchées, mais le texte descriptif n'a pas été entièrement tiré des journaux, et la phrase « When S(c0, Dsearch) = 0.0, as on labels » (p. 4) ne tient pas pour cette tâche.

**Seulement affirmé, ou plus faible qu'il n'y paraît :**

- « Greedy parent inheritance drives the vast majority of optimization progress » (résumé) : vrai dans la grille mesurée ; la généralité est affirmée. L'intervalle étroit [+0,224 ; +0,252] ne rééchantillonne que les lancements, tâches fixées ; dès qu'on rééchantillonne les tâches il s'ouvre à [+0,104 ; +0,363] (p. 6).
- « La lignée est la mémoire » : c'est le nom donné au fait que le texte du candidat retient les règles. Aucun bras ne met une autre mémoire en concurrence.
- « 1 750 lancements préenregistrés » : deux des cinq lots (le résumé avec réponse attendue ; la phrase qui demande de recopier les faits) sont conçus **après** lecture des résultats précédents, ce que les auteurs disent (p. 14 ; « the paper labels it post hoc in design », préenregistrement). La table 5C (classement par pas) et la table 5B ne figurent pas à l'inventaire des 25 tests (table 7, p. 15) : descriptives. Aucune correction pour comparaisons multiples n'est mentionnée. Un test enregistré est « non évaluable tel qu'enregistré », cinq ne tiennent pas (p. 15).
- **L'horodatage du préenregistrement repose sur la parole des auteurs.** Le PDF dit le code « frozen at commit d5ab8923 » (en-tête de la table 7, p. 15 ; aussi p. 14) ; ce commit n'existe pas dans le dépôt public, qui naît d'un seul commit contenant déjà résultats et papier. Le fichier chinois mentionne un pilote antérieur (« budget … comme au pilote », ligne 6). Toute l'étude court sur deux jours (p. 14), avec 267 tentatives interrompues mises en quarantaine (p. 15).

## 5. Verdicts par revendication

Vocabulaire : libre, voisin, occupé en partie, occupé, contredit. « Libre » voudrait dire « non trouvé dans ce document », jamais « trou du champ » (R8).

### Revendication 8 — l'héritage d'une génération est récompensé ; le signal à un pas est exclu

| Élément | Verdict | Preuve |
|---|---|---|
| Le signal rendu à ce qui conçoit porte sur K générations (K ≥ 3) ou inclut les scores des générations suivantes | **voisin** | Aucun concepteur n'apprend ; la seule règle est gloutonne et à un pas : « If S(ct) > S(c*t−1), set c*t = ct » (p. 4). Rien n'est réglé sur plusieurs générations. |
| La prémisse : ce qu'une génération lègue compte, donc juger sur un pas trompe | **voisin, dans le sens qui soutient** (pas contredit) | Repartir de la graine à chaque tour, même avec le résumé de tous les échecs, plafonne à 0,723 sur les cinq tâches à règles cachées, contre 0,943 avec lignée (table 2A, p. 7 ; p. 13). Le classement des affichages s'inverse entre le pas 2 et le pas 4 (table 5C, p. 11). |
| La crainte de la table de veille : « l'artefact, pas la mémoire » | **non mesuré par ce travail** (donc ni occupé ni contredit ; je le range « voisin ») | « fully separating text inheritance from residual-error exposure under raw feedback would require controls that reset to c0 while showing all raw failures or the cumulative union of parent-trajectory failures » (p. 14). |
| L'expérience « poids contre archive » (concepteur figé avec archive consultable contre concepteur entraîné) | **voisin lointain** | Seul rapprochement : un proposeur plus gros ne remplace pas la lignée, « Upgrading proposer capacity within the GPT-4.1 family therefore does not substitute for parent inheritance » (p. 8), trois tâches, 150 lancements. Aucune archive, aucun entraînement. |

Lecture d'ensemble pour la 8 : **voisin**. Deux faits à dire quand même, parce qu'ils ne nous arrangent pas tout à fait :

1. *La règle gloutonne à un pas suffit ici.* Sur les tâches construites, accepter un candidat sur son seul gain immédiat mène à 0,92-0,98 (table 2A). Ce travail ne montre donc **pas** qu'un crédit différé soit nécessaire pour choisir des candidats ; il montre qu'un **état transmis** l'est. La prémisse de N-045 v2 mêle les deux (« la mémoire transmise et les instruments à effet différé ») : seul le premier terme reçoit ici un appui.
2. *Un seul indice d'effet différé, et il est anecdotique.* Sur Banking77, des réécritures qui ne changeaient que la forme valaient 0,000 et étaient rejetées ; « 2 runs stayed at 0.000 across all 8 evaluations » (p. 9). C'est le cas d'un changement utile plus tard et jamais crédité. Mais c'est une inspection de journaux après coup, sur une tâche, et le remède trouvé (une phrase dans l'invite) n'est pas un crédit différé.

### Revendication 10 — la mémoire ne sert ni verdict, ni clé, ni témoin aux agents ; juges aveugles aux notes antérieures

**Verdict : voisin.** Le travail ne traite ni d'une mémoire séparée, ni de juges, ni de ce qu'il est permis d'y mettre. Mais il donne un contre-indice à dire :

- **Ce qui s'hérite utilement ici, c'est précisément la clé.** Le retour montré au proposeur contient la réponse attendue ou la grille de notation (p. 4). La phrase qui fait passer Banking77 de 0,372 à 0,856 demande de la recopier dans le candidat : « copy every task-specific fact the feedback reveals (for example the exact expected labels or formats) into the prompt » (p. 9, 16). Quand le résumé perd la grille, la tâche de réponses au client tombe à 0,519 contre 0,981 (p. 11).
- **Conséquence pour nous** : le gain mesuré par ce travail passe par un canal que la revendication 10 ferme. Sa taille (+0,238) ne dit donc rien de ce que vaudra une mémoire qui ne porte ni verdict ni clé ; elle rappelle plutôt le prix de la règle. Cela va dans le même sens que le contre-indice déjà noté (Qu, Chen, Wang : aucun bras de mémoire significatif).
- **À l'inverse, un indice en faveur de la règle** : là où la graine contient déjà tout l'énoncé, recopier les faits du retour **coûte** −0,061 [−0,119 ; −0,006] sur le jeu tenu à l'écart (p. 9, 15) — un petit signe de surajustement au jeu de recherche. Une tâche, un modèle.
- Le jeu tenu à l'écart partage les catégories et les étiquettes cachées du jeu de recherche : ce qui est mesuré est la généralisation à des items neufs de la même famille, pas à des familles inédites.

### Revendication 9 (non visée, mais touchée de plus près) — le séquentiel doit battre le meilleur de N tirages, à budget égal

**Verdict : occupé en partie**, comme en lecture 07, et sans rien y ajouter d'antérieur (30 octobre 2026). Le bras `graine` est un meilleur de N tirages ; le plafond est compté en évaluations, pas en jetons (p. 4), les jetons étant rapportés à côté (table 5B, p. 11). Restent hors de ce travail : des familles tenues à l'écart, le témoin « un modèle, vote à k », un pilote de bruit et un test A/A, et un concepteur qui apprend.

## 6. Ce qui nous arrange, lu plus durement

Le résultat « l'état transmis vaut plus que le meilleur de N tirages » nous arrange. Quatre raisons de ne pas le citer nu :

1. **Les tâches sont faites pour.** « In the five constructed tasks […] the seed c0 omits key rules or label names so that high accuracy requires learning from feedback. […] This setup favors methods that accumulate rules across rounds » (p. 5). Là où le modèle sait déjà (dates, ScoNe), l'effet est nul ; sur les deux tâches publiques il tombe à +0,088 (p. 14).
2. **Le bras « graine » est privé d'information, pas seulement de lignée.** Avec les 4 premiers échecs, il revoit les quatre mêmes à chaque tour — « both pt and ft stay fixed across rounds » (p. 4) —, soit 11 à 25 % du jeu de recherche, quand le bras `parent` en voit 46 à 86 % au fil des tours (p. 11). Le résumé groupé, censé combler l'écart, tient en 3 à 7 motifs avec un seul exemple chacun, alors que deux tâches ont 12 catégories (table 1, p. 5) : il ne peut pas les montrer toutes — c'est ma lecture des pages 4 et 5, les auteurs disent seulement qu'il « compresse » (p. 14). Le bras `graine` à information égale n'existe pas.
3. **Peu de tâches, petits jeux, un intervalle qui dépend de ce qu'on rééchantillonne** : sept tâches, 12 à 72 exemples tenus à l'écart, et [+0,104 ; +0,363] dès que les tâches sont tirées (p. 6).
4. **Production très rapide, préenregistrement non attesté par un tiers, un écart entre texte et journaux** (section 4). Les messages du journal des commits disent aussi comment le papier a été fini (« Update paper manuscript and PDF (de-AI rewrite and NeurIPS review revisions) », 29 octobre). Les tables, elles, se recalculent.

## 7. Une idée à prendre

**Faire le plan croisé que ce travail nomme et ne fait pas : ce qui est transmis × ce qui est montré, à information égale.** Dans l'épreuve « apprentissage de génération en génération contre meilleur de N tirages » et dans l'expérience « poids contre archive », quatre bras au lieu de deux :

| | pas de mémoire de trajectoire | mémoire de trajectoire servie (sans verdict, sans clé) |
|---|---|---|
| **l'artefact repart de zéro** | meilleur de N tirages | *le bras manquant* : on repart de la graine, mais on reçoit l'union cumulée des retours de la trajectoire |
| **l'artefact est hérité** | lignée seule (ce travail) | lignée plus mémoire |

avec trois précautions prises à ce travail : un bras **sans aucun retour** comme plancher (il révèle quand un retour étroit fait pire que rien, p. 10-11) ; une lecture **génération par génération** (pas 1, 2, 4, K) et non au seul terme, puisque le classement s'inverse entre le pas 2 et le pas 4 ; un intervalle **à deux niveaux** (familles, puis lancements). C'est le seul plan qui répondrait à la question que la table de veille posait à ce papier. À inscrire, si Lazar le veut, au préenregistrement de cette épreuve ; aucune dépense tant que ce n'est qu'écrit.

Second point, mineur : la règle « ne remplacer que si strictement mieux » a laissé 2 lancements sur 10 à zéro pendant tout le budget (p. 9). À regarder dans nos propres règles de promotion de génération en génération.

## 8. Limites de cette lecture

- Les figures 1 et 2 n'ont pas été regardées à l'œil ; les tables portent les mêmes chiffres.
- Le fichier chinois des préenregistrements (250 lignes) n'a été lu qu'aux lignes datées et à la note d'interruption ; la traduction anglaise, en entier. Je n'ai pas vérifié que les seuils de la traduction sont ceux de l'original.
- Mon recalcul couvre les lots gpt-4.1-mini des tables 2A et 5C ; pas la réplique sur claude-haiku-5-5, ni le proposeur plus gros, ni les tâches publiques, ni la comparaison à GEPA.
- Le code des auteurs n'a été ni lu ni exécuté : je ne sais pas si les jeux de recherche et tenus à l'écart sont bien disjoints, je sais seulement que le texte le dit (p. 3).
- Le commit `d5ab8923` et le dépôt épinglé (`shangliy/AdalFlow`, `76c8a738`) n'ont pas été consultés.
- Les travaux que ce papier cite n'ont pas été lus ici ; ce qu'il en dit (par exemple « every existing evaluation tests these mechanisms exclusively inside lineage-preserving search ») est une affirmation des auteurs.

## 9. Pistes signalées (une ligne chacune, non lues ici)

- Oved et collègues, « Evolution or Illusion? » (arXiv 2609.19799) : cité p. 2 pour « strategy rankings can reverse across budget scales » ; déjà versé comme compagnon de la lecture 07.
- Yang et Shi, « Self-evolving recommender systems: a survey and an evaluation audit » (Preprints.org, 2026) : selon ce papier (p. 2), aucune de 27 configurations auditées ne fait tourner une recherche au hasard ou repartant de la graine à budget égal. Affirmation non vérifiée ; utile à la revendication 9.
- Dépôt `shangliy/ideation-goodhart` (p. 3, 20) : vraisemblablement l'étude de la lecture 03 (arXiv 2611.00643) — même premier auteur, mêmes deux bancs d'après les premières lignes de son fichier de présentation ; non vérifié plus loin.
- Lumer et collègues (arXiv 2610.12601), protocole à sujets disjoints et plusieurs graines pour mesurer le surajustement d'une invite optimisée : cité p. 3 ; voisin possible de la revendication 11 (sélection lue une fois).
