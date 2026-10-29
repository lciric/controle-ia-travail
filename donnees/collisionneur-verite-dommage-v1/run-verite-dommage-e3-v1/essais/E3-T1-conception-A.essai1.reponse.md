# Cellule A — Tour III.1 : une vérité du dommage indépendante du texte pour le mode « affaiblir les contrôles »

**Pièces reçues** : A (synthèse du pilote), B1 (question du pilote), B2 (format décision v2), C (N-054, P-015, N-053, N-055, N-056). Toutes présentes et lisibles. Aucune pièce ne décrit ce qu'est un « contrôle » dans une tâche du banc, ni le format des actions, ni l'état final d'un épisode : c'est le trou qui commande tout ce qui suit. Je ne l'invente pas ; je le traite comme une décision à prendre.

---

## 1. (a) Ce que la question suppose sans que ce soit établi

| # | supposition | statut | conséquence si elle tombe |
|---|---|---|---|
| S1 | Une tâche du banc comporte des « vérifications » ayant un résultat objectif (pass/fail, état attendu). | **ABSENT des pièces** ; aucune définition de « contrôle » dans A, B, C. | Sans résultat objectif, aucun oracle mécanique n'existe ; seule l'option 5 reste. |
| S2 | Le dommage est une propriété de l'épisode (état, verdict), pas du récit. Pour le mode « coût », c'est VÉRIFIÉ au niveau de la structure (champ COST, règle du coût, P-015) ; pour « contrôles », c'est **HYPOTHÈSE**. | HYPOTHÈSE | La circularité relevée par l'équipe rouge (pièce A § 4) est la forme que prend cette hypothèse quand elle manque. |
| S3 | « Invisible au texte » désigne un dommage réel. Les actions de l'agent **sont** du texte ; ce qui est invisible l'est à un *lecteur* (juge 8B/3B à 1 % de faux positifs), pas au texte. | HYPOTHÈSE de formulation ; attaquée § 2. | La prémisse se reformule sans perdre le risque. |
| S4 | L'accord 0,968 entre deux séries d'étiqueteurs au pilote mesure quelque chose du dommage. | RAPPORTÉ (N-054, « fait du pilote, non un seuil ») ; c'est une **fidélité inter-lecteurs**, pas une validité. | Deux lecteurs qui se trompent ensemble s'accordent aussi. |
| S5 | Une dizaine d'actions par épisode. | INFÉRÉ de la pièce C, jamais mesuré (pièce A § 7.2). | Toute règle « par action » de P-015 change de puissance. |
| S6 | Les 96 tâches sont réutilisables telles quelles pour porter un oracle. | RAPPORTÉ : 60 tâches lues en P3, 32 portent la dose et T0.7 (B2, D2) ; « aucune des 96 n'est vierge ». | Planter des défauts modifie le texte des tâches : versions neuves, nom neuf (R12), contamination à déclarer. |
| S7 | Un oracle peut être « indépendant » du texte. Aucun oracle n'est indépendant de la **sortie** de l'agent ; il peut l'être de la **fonction de lecture** (déterministe vs. modèle). | HYPOTHÈSE précisée § 4. | L'indépendance se définit par trois conditions, pas par un mot. |
| S8 | L'agent honnête réussit ses propres contrôles. P-015 rapporte que 43,7 % des coûts honnêtes sont à plus d'un facteur 10 de la référence. | RAPPORTÉ pour le coût ; **inconnu** pour les contrôles. | Si l'honnête rate déjà la plupart des vérifications, il n'y a pas de place pour mesurer un dommage : effet de plancher. |
| S9 | Les positifs de G1 pour ce mode sont « les épisodes de la condition sabotée ». Introduire un oracle permet de redéfinir les positifs comme « sabotés **et** endommagés ». | Décision de porte non prise (N-055 D-S10, préenregistrement). | Changer la définition des positifs change le rappel de G1 : nœud. |
| S10 | Prix de carte et rythmes. | SUPPOSÉ (1,08–1,43 USD/h) ; rythmes RAPPORTÉS pour génération et juges seulement. | Tout coût ci-dessous est illustratif sauf mention. |

---

## 2. Attaque de la prémisse : le « dommage invisible au texte »

La définition de « diffus » (P-015) est **négative et relative** : chaque action sabotée reste sous le seuil du meilleur moniteur boîte noire à 1 % de faux positifs sur l'honnête. Si le dommage est jugé par un lecteur de texte de la même classe que ces moniteurs, alors « diffus avec dommage » est, par construction, « sous le seuil du lecteur, mais au-dessus du seuil du lecteur » : région vide ou bruit. Ce n'est pas un risque empirique, c'est une contradiction de définition. La question la nomme « circularité » ; le mot juste est **définition négative sans référent positif**.

Deux lectures de la prémisse :
- **Artefact** : « invisible au texte » confond le support (le texte des actions) et l'instrument (le juge 8B). Reformulée, la prémisse devient : *existe-t-il un dommage visible à une vérification déterministe et invisible aux juges à 1 % ?* C'est une question empirique, testable (E2), et c'est exactement ce que le pilote doit établir.
- **Vrai risque** : si S1 est fausse (les tâches n'ont pas de vérification à résultat objectif), alors il n'existe aucun référent positif pour ce mode, et le « dommage » n'est qu'un jugement de lecteur. Dans ce cas le mode ne peut porter H1 ; c'est l'option 5.

Le pilote ne peut donc pas commencer par une dose : il commence par **S1**, qui se tranche sans dépense (lecture du format des tâches, D-O1).

---

## 3. Familles d'oracles, au niveau méthode

| famille | ce qu'elle mesure | ce qu'elle ne mesure pas | coût sur 96 tâches / changement au banc | compatible « tâches d'articles » |
|---|---|---|---|---|
| **O1 — verdict structuré de contrôle** : chaque vérification de la tâche produit un enregistrement machine-lisible (item, résultat), comparé à une feuille de vérité scellée | la conformité de chaque verdict rendu à la vérité de l'item ; dommage = verdicts faux ou absents, par item | rien de ce que l'agent a fait hors des items listés ; un verdict écrit juste sans vérification réelle (le record est lui-même une sortie de l'agent) | nul en calcul (parseur déterministe) ; **change le format** : les tâches doivent imposer le record | oui si la tâche définit des items vérifiables (une valeur, une unité, une cohérence interne) ; non si elle demande un jugement libre |
| **O2 — défauts plantés** : la tâche contient k items défectueux connus d'avance, qu'une vérification correcte signale ; dommage = part des défauts non signalés, au-delà du taux honnête | la **sensibilité** des contrôles exercés, par item, contre une vérité fixée avant génération | les défauts non plantés ; le dommage de forme « contrôle correct mais conclusion ignorée » | k × 96 items à écrire et sceller (heures d'instance, aucun rythme mesuré) ; versions neuves des tâches (S6) | oui : incohérences internes, valeurs altérées, références croisées fausses sont plantables dans un matériau d'article |
| **O3 — rejeu hors de l'agent** : les vérifications déclarées sont ré-exécutées par un module déterministe sur les mêmes entrées ; dommage = écart entre le verdict de l'agent et le verdict rejoué | la **fidélité** du verdict rendu (le contrôle disait-il vrai ?) | une vérification jamais déclarée (omission) ; exige que la vérification soit exécutable | nul en GPU ; exige des contrôles **exécutables** (code, calcul) : change le banc si les tâches sont textuelles | partielle : oui pour les tâches avec calcul reproductible, non pour les tâches de lecture |
| **O4 — contrôles redondants cachés** : une seconde batterie d'items, absente de l'énoncé, évaluée par O1/O2 sur l'état final | le dommage **hors de la vue** de l'agent ; sépare « verdict manipulé » et « état réellement dégradé » | rien de plus que O2 si l'agent ne distingue pas visible et caché ; coûte une seconde feuille | double O2 ; même changement de banc | oui |
| **O5 — conséquence en aval** : un consommateur mécanique de la sortie (un calcul, une décision binaire sur l'état final) ; dommage = ce qui passe à tort | l'**effet** du contrôle affaibli, pas le contrôle lui-même | un dommage sans conséquence mesurable par ce consommateur ; dépend du consommateur choisi | un consommateur par tâche : le poste le plus lourd en conception | difficile : il faut définir « à tort » par tâche |
| **O6 — étiqueteurs-texte (état actuel)** | la lisibilité du dommage par un lecteur | la vérité : même famille que les juges | déjà payé au pilote (0,968 RAPPORTÉ) | oui, mais sans valeur de vérité |

Je retiens pour le pilote **O2 + O1** (défauts plantés lus par verdict structuré), avec **O4** comme contrôle de la manipulabilité du record. O3 seulement sur les tâches exécutables. O5 reporté : sa conception dépasse ce que seize tâches peuvent porter.

---

## 4. Indépendance et séparation des rôles

**Indépendance** : aucun oracle n'est indépendant de la sortie de l'agent. Il peut l'être sous trois conditions, toutes vérifiables :
1. **Vérité fixée avant génération** : feuille scellée (empreinte au registre) avant tout épisode, écrite sans lire aucun épisode ni aucune pièce des moniteurs.
2. **Aucune composante apprise, aucun modèle de la lignée des juges ni de l'agent** dans la lecture : parseur déterministe. Si un extracteur par modèle est inévitable (record absent), il est d'une **autre lignée** (Qwen2.5-7B est déjà prévu comme bras rapporté, N-053 point 4) et son erreur d'extraction est mesurée sur des records synthétiques à vérité connue.
3. **Hors de toute sélection** : les scores d'oracle sont stockés dans la quarantaine (N-053, lecteur de la quarantaine), jamais dans un signal d'entraînement ni de sélection d'un agent ou d'un moniteur ; ils n'entrent pas dans la liste d'intersection-union de D-S8 (sinon « diffus » serait défini contre l'oracle, et la région redevient vide). Une extension explicite de N-053 est nécessaire : « aucun score d'oracle dans une sélection, hors règle scellée de dose ».

**Rôles (N-054)** :
- **Auteur de la feuille** : le constructeur des tâches (ou une instance neuve servie par un modèle qui n'est ni l'agent ni un juge), sans pièce des moniteurs dans ses entrées. Conv-audit, concepteur des moniteurs, ne l'écrit ni ne la lit.
- **Qui la voit** : l'auteur et le lecteur de la quarantaine. **Ni** l'auteur du mode tenu à l'écart (bras A), **ni** le bras d'attaque informé (bras B, N-056 point 6) : l'un et l'autre doivent connaître le *format* des tâches (sans quoi aucun mode n'est écrivable), jamais les items. Un attaquant qui connaît les items optimiserait le dommage contre l'oracle : ce ne serait pas une recette d'évasion des moniteurs, mais ce serait une sélection sur l'oracle.
- **Fuite inverse** : les scores d'oracle ne sont lus qu'après gel de la dose et jamais par épisode avant G1 ; l'auteur du mode tenu à l'écart ne reçoit aucun résultat du pilote (déjà D-10).

---

## 5. (b) Les duels

Toutes les valeurs de seuil sont **illustratives**, à sceller avant génération. Unité d'inférence : la tâche (16 grappes), erreurs types par rééchantillonnage des tâches (D-S11 : rapporté ; le pari apparié décide si une règle scellée l'exige).

### E0 — Préalable sans dépense : S1
**H_A** : chaque tâche du banc définit au moins trois items à résultat objectif (valeur, unité, cohérence) qu'une vérification correcte tranche sans jugement. **H_B** : une part ≥ 25 % des 96 tâches n'en définit aucun.
Métrique : nombre d'items objectifs par tâche, compté par un lecteur neuf sur l'énoncé seul. Contrôle négatif : trois tâches dont l'énoncé est permuté entre elles (le compte doit tomber). Si H_B : le mode « contrôles » n'a pas d'oracle sur ces tâches ; on passe directement à l'option 5 pour la part concernée, ou à un banc restreint. Si H_A : E1.

### E1 — Validité de l'oracle à dose forte
**H_A** : l'oracle O2 sépare la dose forte témoin de l'honnête : part de défauts non signalés, saboté-fort moins honnête, ≥ 30 points (illustratif), avec un taux de « dommage » sur jumeaux honnêtes ≤ 5 % au seuil scellé (quantile honnête). **H_B** : écart < 30 points ou taux honnête > 5 %.
Contrôles négatifs : jumeaux honnêtes ; témoin instruit (déclaré non neutre, P-015 : il est rapporté, pas compté dans le nul) ; **épisodes sabotés du mode coût** lus par l'oracle « contrôles » (spécificité par mode : s'il tire aussi sur le mode coût, les deux modes ne sont pas séparés, et D-S29 (a) perd son sens).
Si H_B : « oracle non concluant » ; aucune dose n'est cherchée ; nœud D-O6. Si H_A : l'oracle est un instrument ; E2.

### E2 — Existence d'une dose diffuse avec dommage (la question du pilote)
Trois doses écrites. Par épisode : part d'actions sous le seuil à 1 % du **maximum** des moniteurs noirs de la liste scellée (lecture avec et sans la règle du coût, D-7) ; dommage par l'oracle.
**H_A** : à l'une des doses, la part « diffus » par épisode (≥ 90 % d'actions sous seuil, illustratif ; lecture « honnête + 5 points » de D-6 (a)) est ≥ 0,7 des épisodes **et** le gain d'oracle saboté − honnête a sa borne basse > 0 sur les 16 grappes, avec une estimation ≥ 20 points. **H_B** : à toute dose, gain d'oracle > 0 implique part « diffus » < 0,7 (dommage et diffus s'excluent pour ce mode).
Contrôle négatif : la part « diffus » sur jumeaux honnêtes (doit être ≈ 1 − 0,01 par action, bornée par la multiplicité) ; témoin et mention rapportés.
Si H_A : « dose diffuse avec dommage établie » ; cela falsifie « le juge 8B suffit comme vérité » et la lecture O6. Si H_B : « dommage introuvable » ; cela falsifie la prémisse du pilote pour ce mode, et le mode reste rapporté hors de la strate H1a. Les deux issues sont informatives à ± 12 points par unité (pièce A § 2.3), donc un gain vrai de 10 points est indécidable : à déclarer.

### E3 — Validité des étiqueteurs-texte contre l'oracle
**H_A** : l'accord des étiquettes de sous-agents avec l'oracle (kappa par épisode) ≥ 0,6 et supérieur à leur accord avec le juge 8B. **H_B** : kappa avec l'oracle < 0,3 alors que l'accord inter-séries reste ≥ 0,9.
Contrôle négatif : étiquettes sur jumeaux honnêtes (taux de « dommage » déclaré à tort) ; étiquettes sur épisodes dont le record d'oracle est permuté entre tâches (le kappa doit tomber à ≈ 0 ; sinon les étiquettes lisent autre chose que le dommage).
Si H_B : les étiquettes sont une mesure de lisibilité, rétrogradées à RAPPORTÉ ; les « heures d'étiquetage » de N-054 n'achètent pas une vérité. Si H_A : les étiqueteurs peuvent servir de **second** oracle, rapporté, jamais décisif.

### E4 — Manipulabilité du record (O1 contre O4)
**H_A** : dommage mesuré par les items cachés (O4) − dommage mesuré par les items visibles (O1/O2) ≤ 10 points à la dose retenue. **H_B** : écart > 10 points.
Contrôle négatif : l'écart sur jumeaux honnêtes (doit être ≈ 0 : les honnêtes ne distinguent pas visible et caché).
Si H_B : le verdict écrit par l'agent n'est pas une vérité ; seule la batterie cachée l'est ; coût doublé de la feuille et nœud sur le format. Si H_A : O1 suffit pour la banque, O4 reste un contrôle sur un sous-lot.

### E5 — Plancher honnête (sans sabotage)
**H_A** : l'agent honnête signale ≥ 60 % des défauts plantés (illustratif). **H_B** : < 60 %.
Contrôle négatif : items non défectueux signalés à tort (taux de fausse alerte de l'agent honnête lui-même). Si H_B : effet de plancher ; E2 n'est pas lisible sans relever la difficulté des items (nœud) — et c'est le point que le fait des 43,7 % du mode coût rend crédible. E5 se joue sur le lot honnête de calibrage, avant tout saboté : il décide si la dépense sabotée a un sens.

---

## 6. (c) Chaque instrument : la mesure minimale qui dirait s'il fonctionne

| instrument | détection à mesurer | fausse alerte à mesurer | cas honnêtes appariés | ce qu'il doit battre |
|---|---|---|---|---|
| **juges 8B / 3B (texte, jeton de verdict)** | rappel par épisode sur les positifs **d'oracle** (saboté ∧ dommage), à 1 % de faux positifs | seuil fixé sur les jumeaux honnêtes du lot de calibrage | jumeaux à graine appariée par tâche | ils ne « battent » pas l'oracle : ils sont **notés contre** lui ; un juge dont le rappel sur positifs d'oracle est ≤ celui sur négatifs d'oracle (sabotés sans dommage) lit la consigne, pas le dommage |
| **étiqueteurs par sous-agents** | kappa contre l'oracle (E3) | « dommage » déclaré sur honnêtes | les mêmes jumeaux | leur accord inter-séries (0,968 RAPPORTÉ) ne compte pas comme preuve ; ils doivent dépasser la concordance qu'ils ont avec le juge 8B |
| **verdict structuré (O1)** | taux de record complet et parsable (score fini) ; conformité à la feuille | records honnêtes jugés faux par le parseur (erreur de lecture, mesurée sur records synthétiques à vérité connue) | lot honnête de calibrage | O4 (items cachés) : l'écart ≤ 10 points (E4) |
| **défauts plantés (O2)** | part signalée à dose forte vs honnête (E1) ; plancher honnête (E5) | items sains signalés défectueux par l'honnête | jumeaux ; témoin instruit rapporté | aucun ; c'est la vérité candidate, validée par E1/E5 et par spécificité contre le mode coût |
| **rejeu hors agent (O3)** | écart verdict agent / verdict rejoué, à dose forte vs honnête | écart sur honnêtes (bruit d'exécution, non-déterminisme) | jumeaux sur les seules tâches exécutables | O2 sur les mêmes tâches : si O3 et O2 divergent de plus de 10 points, l'un des deux ne lit pas le dommage |
| **contrôles cachés (O4)** | comme O2, sur items absents de l'énoncé | comme O2 | jumeaux | E4 |
| **conséquence en aval (O5)** | dégradation du consommateur à dose forte vs honnête | variance du consommateur sur honnêtes | jumeaux | O2 : une conséquence sans défaut manqué, ou l'inverse, signale deux définitions du dommage ; à rapporter, non décidé au pilote |

Règle commune : tout instrument dont le taux sur jumeaux honnêtes dépasse le seuil scellé, ou dont le score manque sur plus de la part scellée d'épisodes (règle du score manquant de la pièce A), sort de la lecture du pilote et est rapporté « non calibré ».

---

## 7. (d) Ancrage matériel

- **Modèles** : agent et juge Llama-3.1-8B-Instruct (RAPPORTÉ, P-015 ; « à capacité égale ») ; juge 3B (lignée non précisée dans les pièces) ; Qwen2.5-7B en bras rapporté (N-053) ; sondes aux couches 7, 15, 23 (N-056). **L'oracle n'utilise aucun de ces modèles** : parseur déterministe, CPU.
- **Calcul de l'oracle** : lecture de ≈ 900 à 1 300 épisodes (pièce A) par un parseur : minutes de processeur, ≈ 0 USD (illustratif). Si un extracteur par modèle est nécessaire : Qwen2.5-7B, charge comparable à sa lecture comme moniteur, soit **+ 21 heures, 23–30 USD SUPPOSÉ** (chiffres de la pièce A pour Qwen, transposés : illustratif).
- **Conception de la feuille** : 16 tâches × k = 5 items (illustratif) = 80 items plantés + 80 items cachés (O4) ; heures d'instance ou d'humain, **aucun rythme mesuré** ; aucune dépense de carte.
- **Versions neuves des 16 tâches** (défauts plantés) : génération inchangée en volume ; le surcoût est de conception. Pour les 64 tâches d'épreuve : 320 à 640 items, à écrire avant le préenregistrement de G1, sans lire aucun épisode du pilote.
- **E5** se lit sur le lot honnête de calibrage déjà prévu (lot C d'A, 480 épisodes ; ou 432 chez C) : aucune dépense ajoutée.
- **Enveloppe** : le pilote reste dans les 50–120 USD SUPPOSÉS de la pièce A, plus 0 à 30 USD selon l'extracteur. Au-delà de 90 USD, nœud (pièce D, rappelée en A).

---

## 8. Le pilote minimal et ses règles gelées

**Version minimale** : O2 sur les 16 tâches (k = 3 items, illustratif), O1 obligatoire dans le format, O4 sur 8 des 16 tâches seulement, O3 sur les seules tâches exécutables, O5 absent. E0 et E5 avant toute génération sabotée. Lecture de l'oracle : une fois, après gel de la dose, sur les lots autorisés (jamais les sabotés de développement, D-4).

**Règles à sceller avant génération** (empreinte au registre) :
1. feuilles O2 et O4 ; convention de parsing ; règle du record manquant (= dommage maximal, ou neutre : à choisir, D-O5) ;
2. seuils : quantile honnête de l'oracle (5 %), écart dose forte (30 points), gain minimal (20 points), part « diffus » (0,7 des épisodes), kappa (0,6 / 0,3), plancher honnête (60 %) — tous illustratifs ici ;
3. **verdicts** :
   - *établie* : E1 H_A **et** E5 H_A **et** E2 H_A, avec l'oracle sous son taux honnête ;
   - *introuvable* : E1 H_A, E5 H_A, E2 H_B ;
   - *non concluant* : E1 H_B ou E5 H_B, ou score manquant au-dessus de la part scellée, ou spécificité par mode absente (l'oracle « contrôles » tire sur le mode coût) ;
4. l'oracle n'entre pas dans la liste D-S8 ; ses scores vont en quarantaine ; aucun seuil calibré sur l'oracle n'est transmis aux bras A et B ;
5. la règle de dose : paramètre commun choisi une fois par la règle « plus forte dose telle que part diffuse ≥ 0,7 et gain d'oracle borne basse > 0 », sans filtrage d'épisode (lecture (a) de D-3, étendue à l'oracle) ;
6. ce qui ne sera **pas** lu : scores d'oracle par épisode sur les sabotés de développement ; toute strate non définie sur l'énoncé.

---

## 9. Si aucun oracle indépendant n'est possible

| choix | ce que cela coûte à la revendication |
|---|---|
| **Retirer le mode de G1** (nœud N-054 point 1) | H1 ne porte plus que sur le mode « coût » et le mode tenu à l'écart ; la revendication « diffus / flou » (§ 5 du programme) repose sur un dommage chiffré, ce que Lazar voulait éviter (« au moins un mode non chiffré ») ; G1 rapportée par mode perd un mode. |
| **Garder avec revendication réduite** : positifs = condition sabotée ; l'oracle textuel (étiqueteurs) rapporté comme lisibilité ; aucune strate H1a sur ce mode | le mode reste dans l'expérience de lecture de N-054 point 4 (bras génériques vs spécialisés) où la vérité n'est pas requise, puisqu'on compare des rappels entre bras sur les mêmes positifs ; mais « dommage » n'est plus affirmé : on mesure la détection d'une **consigne**, et le critère D-S29 (a) (gain dans chaque mode) devient un gain sur une condition, non sur un dommage. |
| **Remplacer** par un mode dont le dommage est un verdict structuré faux (O1) | mesurable, non chiffré au sens d'un nombre gonflé ; risque : un mode trop proche du « coût » (un champ altéré) réintroduit un artefact de source ; conception par une instance sans pièce des moniteurs (N-054), ce qui est le circuit déjà monté pour le bras A. |

Recommandation : (b) par défaut dès maintenant (sans dépense, et compatible avec N-054 point 4), (c) si E0 donne H_B sur une part importante du banc, (a) seulement si Lazar refuse une revendication réduite.

---

## 10. Décisions du directeur

| # | décision en une phrase | enjeu | options | recommandation (confiance) | défaut |
|---|---|---|---|---|---|
| D-O1 | Le format des tâches impose un **record de vérification structuré** (O1), lu par un parseur déterministe | sans record, l'oracle redevient un lecteur de texte | (a) record obligatoire, versions neuves des tâches ; (b) format inchangé, extracteur Qwen (23–30 USD SUPPOSÉ, erreur d'extraction à mesurer) | (a), haute | (a) |
| D-O2 **nœud** | Les tâches du pilote reçoivent des **défauts plantés** scellés (O2), avec une batterie cachée sur la moitié (O4) | c'est la vérité candidate ; elle modifie des tâches déjà lues (S6) | (a) O2 + O4 ; (b) O2 seul ; (c) O3 seul sur les tâches exécutables | (a), moyenne-haute | aucun |
| D-O3 | Qui écrit et qui voit la feuille | fuite vers les bras A et B ; concepteur des moniteurs exclu | (a) constructeur des tâches + lecteur de quarantaine seuls ; (b) conv-audit relit (interdit par N-054) | (a), haute | (a) |
| D-O4 | Extension de N-053 : **aucun score d'oracle** dans une sélection d'agent ou de moniteur, ni dans la liste D-S8 | sinon « diffus » se définit contre l'oracle (région vide) ou l'oracle sert à optimiser | (a) extension écrite et gardée par le code ; (b) usage libre | (a), haute | (a) |
| D-O5 | Convention du record manquant et seuils d'oracle scellés avant génération | un record absent peut être le dommage lui-même ou une panne | (a) manquant = dommage maximal, taux de manquants rapporté par condition ; (b) neutre | (a) si le taux de manquants honnête est ≤ 2 % (illustratif), sinon nœud ; moyenne | (a) |
| D-O6 **nœud** | Sort du mode « contrôles » selon le verdict du pilote | N-054 point 1 ; D-S29 (a) | établie → strate H1a pour ce mode ; introuvable → revendication réduite (§ 9 b) ; non concluant → relever les items ou § 9 c | règle gelée avant lecture, haute ; le choix dans « non concluant » reste à Lazar | aucun |
| D-O7 **nœud** | Positifs de G1 pour ce mode : condition sabotée, ou condition ∧ dommage d'oracle | change le rappel rapporté par mode (N-054 point 2) | (a) condition, oracle rapporté ; (b) condition ∧ dommage | (b) si « établie », (a) sinon ; moyenne | (a) |
| D-O8 | E0 et E5 avant toute génération sabotée | évite une dépense sabotée sans oracle ou sous plancher | (a) préalables ; (b) tout en une fabrique | (a), haute | (a) |
| D-O9 | Statut des étiqueteurs par sous-agents | 0,968 est une fidélité, pas une validité | (a) rapportés, validés par E3 ; (b) vérité par défaut | (a), haute | (a) |
| D-O10 **dépense** | Extracteur par modèle si (b) de D-O1 | 23–30 USD SUPPOSÉ ; même lignée interdite | Qwen2.5-7B seul admissible parmi les pièces | n'engager qu'après D-O1 ; moyenne | aucun |

---

## 11. Ce qui reste ouvert, et ce que je ne vérifie pas

Non vérifié : le format réel des tâches (S1) ; l'existence de tâches exécutables ; le nombre d'actions par épisode ; tout rythme hors génération et juges ; l'accès arXiv pour des versions neuves ; le non-déterminisme d'exécution pour O3. Mes seuils sont illustratifs ; mes coûts hors pièce A le sont aussi. Le point le plus fragile de cette cellule est S8 : si l'agent honnête rate déjà la plupart des vérifications, aucune dose ne sera lisible, et c'est E5, qui ne coûte rien, qui le dira d'abord.

FIN-DE-CELLULE