# Cellule A — Tour III.1 : conception ciblée, à l'aveugle

## 0. Pièces absentes ou non auditables (une ligne chacune)

- Le code de la v6.2.1 (`principal.py`, `memoire_isvd.py`, `mitose_spectrale.py`, `politique_endogene.py`) n'est pas joint ; je raisonne sur `A.CONCEPTION` et `A.CORRECTIONS-v1` à `v5` seulement (RAPPORTÉ).
- Les faits B (README et articles d'Agentic Scientist v3, ShinkaEvolve, OpenEvolve, Kosmos) ne sont pas joints : seuls leurs résumés figurent dans le bloc QUESTION (RAPPORTÉ de seconde main).
- Les faits C (rapport de méta-conception v6.3 et sa relecture) sont absents ; l'étage de recombinaison n'a donc aucune pièce ici.
- Les faits D (billet sur le sabotage de la recherche) sont absents ; résumé dans la question, déclaré « non opposable ».
- La question cite `7ea3270`, arbre `4f13647a…`, 26 fichiers pour la v6.2.1 ; les faits donnent `3bbb78c`, 24 fichiers pour la v6.2 et aucun identifiant de commit pour la v6.2.1 : non vérifiable ici.
- « Deux courses du pilote 4 finies et saines » : aucune pièce, aucun score (règle du programme) ; OBSERVÉ-NON-AUDITÉ au mieux.

---

## (a) Ce que la question suppose sans que ce soit établi

| n° | Présupposé | Ce que les faits disent | Statut |
|---|---|---|---|
| A1 | « Notre organisme peut réécrire son propre code » (point 4 de la question). | Depuis C-17, l'architecte ne peut rendre qu'un objet JSON de **trois paramètres bornés** dans un gabarit de forme fixe ; le code brut est refusé sans exécution ; la liste blanche AST n'admet ni boucle ni récursion ni appel inter-fonction (§ 2.12, § 2.14). Les quatre fonctions réécrites (`recompense_interne`, `code_objectif_sonde`, `ponderer_trace_memoire`, `seuils_routage`) sont des courbes paramétrées, pas du code au sens de la question. | RAPPORTÉ (faits) ; que cela « compte » comme réécriture : HYPOTHÈSE, et à mon avis fausse. |
| A2 | L'organisme « formule des hypothèses ». | Il produit des étiquettes binaires avec confiance, des « règles induites » en texte, et un `reponse-question.md`. Le `journal_ablations` déduit `CONFIRME/STAGNANT/REFUTE` du seul `Δscore` du noyau (§ 2.11.3) : c'est une surveillance de score, pas un test d'hypothèse ; aucune prédiction chiffrée préenregistrée n'y figure. | RAPPORTÉ ; « moteur d'hypothèses » : HYPOTHÈSE non appuyée. |
| A3 | Les systèmes B font de la « sélection par réfutation ». | Les résumés décrivent des maximiseurs : grille de notation (AI-Scientist v3), aptitude évolutionnaire avec archive, îles et juge de nouveauté (ShinkaEvolve, OpenEvolve). Maximiser une note n'est pas éliminer une hypothèse réfutée ; les auteurs d'AI-Scientist v3 rapportent eux-mêmes des « raccourcis » et une « dérive vers le réglage ». | RAPPORTÉ (résumés) ; l'équivalence maximisation = réfutation : HYPOTHÈSE, contredite par les limites dites. |
| A4 | Il existe un oracle pour le programme visé (sondes, garanties séquentielles, moniteurs). | Le seul juge de l'organisme est un jeu de tâches à vérité terrain pour deux familles de classification (§ 1). Rien dans les faits ne donne une vérité terrain pour « une garantie séquentielle est correcte » ou « un test d'acceptation est bon ». | RAPPORTÉ (absence) ; oracle transférable : HYPOTHÈSE. |
| A5 | La récompense interne peut servir d'aptitude. | `metrique/calculer.py` est une métrique de forme, ne lit jamais la vérité, non discriminante sous la règle CA-19 (sortie parfaite = sortie inversée) ; écartée de H-E2. La récompense Bregman-Tsallis est propre (vérifiée sur grille, § 2.12–2.13) mais ne s'applique qu'aux tâches **avec** vérité. | RAPPORTÉ. |
| A6 | La mémoire inter-générationnelle transporte de la connaissance. | ISVD `d = 16`, rang 6, dictionnaire `[v, sin(v), v²]`, jetons ASCII seulement (« évaluation » → « valuation »), aucune graine (CORRECTIONS-v1). Aucune mesure d'ablation de cette mémoire n'est rapportée. | RAPPORTÉ (conception) ; effet : HYPOTHÈSE non mesurée. |
| A7 | La bisociation produit des hypothèses « plus fertiles ». | Faits C absents ; « fertilité » n'est définie nulle part. | HYPOTHÈSE sans pièce. |
| A8 | Les six critères sont mesurables avant une course. | « Force des hypothèses », « maîtrise pour un chercheur seul » n'ont ni métrique ni protocole dans les faits. | HYPOTHÈSE. |
| A9 | La lignée A est « saine ». | Les 17 corrections montrent une classe de défaut récurrente : replis silencieux (étiquette prise par présence d'un mot, C-02 ; confiance NaN → 0,99, C-08 ; budget de repli, C-07 ; exactitude d'entraînement relue par le routage, C-15 ; verrou non réentrant qui bloquait tout, C-12). Et § 3 de la conception liste dix affirmations du dossier de passation (882 agents, 241 castes, mutinerie, A/B 0 % vs 94,4 %) **sans aucune trace** sur `origin/main`. | RAPPORTÉ. La classe de défaut est documentée ; qu'elle soit épuisée : HYPOTHÈSE. |
| A10 | « Moins d'une semaine » suffit. | Un cycle de correction v1→v5 a pris du 24 au 26 octobre ; aucune durée de course n'est dans les faits ; en simulation, 123 appels par génération sous le pilote 4 (CORRECTIONS-v5). | RAPPORTÉ partiel ; délai d'une comparaison complète : HYPOTHÈSE. |
| A11 | La question « perfectionner ou adopter » est binaire. | Les systèmes B sont Apache 2.0 et à pleins droits dans Docker ; l'organisme A tourne dans un noyau qui borne tout. Rien n'interdit de mettre un évaluateur B sous le noyau A, ou un moteur A dans un conteneur B. | RAPPORTÉ (licences, bornes) ; hybride : HYPOTHÈSE, à tester, voir E1. |

Le point A3 est celui qui me semble le plus lourd : la question importe de la littérature le mot « évolution » et y lit « darwinisme par réfutation », alors que les trois systèmes nommés sont, d'après leurs résumés, des optimiseurs de note. Un optimiseur de note converge précisément vers ce que la question veut éviter (loi de Goodhart, tests choisis après coup).

---

## (b) Expériences décisives, en duels H_A / H_B

Convention : toutes les cibles numériques sont **illustratives** sauf indication. Chaque duel a un contrôle négatif et deux issues falsifiantes. Tous les tests sont figés avant l'exécution et tenus hors de portée des agents (ce qui, au passage, répond à « qui écrit le test » : ni l'agent qui défend, ni un agent concurrent, mais un test préenregistré sous le noyau — HYPOTHÈSE de méthode, que E2 teste).

### E1 — Les hypothèses produites sont-elles réfutables et survivent-elles ? (voie A contre voie B, même `task.md`)

- **Objet** : étage d'idéation seul, sans exécution par les agents.
- **H_A** : à `task.md` identique (programme « sondes / garanties séquentielles / moniteurs »), la voie A (chemin `question_ouverte`, castes contradictoires, moisson bornée) produit une fraction d'hypothèses *recevables* (prédiction chiffrée + intervalle + test préenregistré nommé que l'auteur ne lance pas) supérieure d'au moins 0,15 (illustratif) à celle de l'idéation d'AI-Scientist v3.
- **H_B** : la fraction est inférieure ou l'écart est sous 0,15.
- **Métrique** : recevabilité, décidée **mécaniquement** (présence d'un nombre, d'un intervalle, d'un identifiant de test de la batterie figée) ; puis taux de survie à la batterie, exécutée par le noyau, jamais par l'agent.
- **Contrôle négatif** : même pipeline alimenté par un `task.md` brouillé (phrases permutées) ; si la recevabilité ne baisse pas, la métrique mesure la forme, pas le contenu, et le duel est nul.
- **Issues** : H_A vraie falsifie « il faut adopter un système de la littérature pour avoir des hypothèses fortes » ; H_B vraie falsifie « l'organisme, tel quel, est un moteur d'hypothèses » (A2) et déplace le projet vers une voie hybride (noyau A + idéation B) ou B.
- **Ce qui ferait changer d'avis** : si les deux voies ont une recevabilité < 0,2 (illustratif), le goulot est la définition du programme, pas le moteur.

### E2 — Quelle aptitude pour la sélection darwinienne ? (Goodhart contre sévérité)

- **Objet** : la sélection sur une population d'hypothèses **synthétiques à vérité connue** : vraies non triviales, fausses, et *triviales* (prédisent un intervalle qui couvre tout).
- **H_A** : l'aptitude « survie pondérée par la sévérité » — somme, sur les tests figés passés, de −log P(passer | hypothèse nulle), estimée par simulation sous le nul — donne, après k générations, une précision des survivantes ≥ 0,8 et un taux de triviales survivantes ≤ 0,05 (illustratif).
- **H_B** : l'aptitude « note moyenne sur les tests choisis par l'agent » (le schéma des systèmes B d'après leurs résumés) donne une précision < 0,8 ou des triviales > 0,05.
- **Contrôle négatif** : sélection au hasard ; une aptitude qui ne la bat pas est écartée. Second contrôle : aptitude sévérité avec les étiquettes de sévérité permutées ; si elle garde sa précision, c'est le filtre de recevabilité qui travaille, pas la sévérité.
- **Issues** : H_A vraie falsifie « on peut adopter l'aptitude évolutionnaire des systèmes B sans la remplacer » ; H_B vraie falsifie ma pondération par sévérité (soit elle est mal estimée, soit la population s'adapte aux tests figés, ce qui se verrait à une hausse de survie sans hausse de précision — signature de Goodhart).
- **Garde contre les hypothèses qui ne prédisent rien** : la sévérité d'un test passé par une hypothèse triviale vaut zéro par construction ; cela se vérifie en comptant les triviales survivantes. Si elles survivent quand même, le filtre de recevabilité (E1) est percé.
- **Référence** : la notion de test sévère est celle de Mayo (1996, *Error and the Growth of Experimental Knowledge*) ; l'inférence forte, Platt (1964, *Strong Inference*, Science). La pondération précise par −log P sous le nul est ma proposition (HYPOTHÈSE).

### E3 — La recombinaison bisociative bat-elle un tirage stratifié ?

- **Objet** : étage de recombinaison, sur un banc **à structure plantée** : une bibliothèque de « domaines » synthétiques dont certains partagent un opérateur caché (même fonctionnelle de perte, même borne de concentration, même martingale), à contraintes compatibles ou non.
- **H_A** : le tirage par opérateur commun + filtre de compatibilité des contraintes produit, pour 100 enfants, au moins 1,5× plus d'enfants survivant aux tests sévères (E2) que le tirage stratifié par domaine (illustratif).
- **H_B** : ≤ 1,5×.
- **Contrôle négatif** : appariement sur étiquettes d'opérateur **permutées** ; s'il égale H_A, ce n'est pas l'opérateur qui porte l'effet, mais le filtre ou le volume.
- **Issues** : H_A vraie falsifie « la bisociation est un habillage » ; H_B vraie falsifie la forme minimale de l'étage (et renvoie aux faits C, absents, pour une autre forme). Dans les deux cas, « fertilité » devient une grandeur mesurée : survivants sévères pour 100 enfants.
- **Réserve** : sans les faits C, je ne peux pas dire si cette forme (tirage, filtre, fusion) est celle de la méta-conception v6.3. Bisociation : Koestler (1964, *The Act of Creation*).

### E4 — La « réécriture de soi » de l'organisme change-t-elle quelque chose ?

- **Objet** : le gabarit à trois paramètres bornés (C-17), la mémoire ISVD, l'archive généalogique à retour arrière.
- **H_A** : sur une famille coffre (*Holdout Vault*, § 4 : score jamais rendu avant la dernière génération), l'organisme avec architecte + mémoire bat l'organisme avec paramètres fixés aux valeurs initiales et mémoire vidée, d'au moins 0,03 de score externe (illustratif ; 0,03 est aussi le seuil de retour arrière de § 2.11.2, RAPPORTÉ).
- **H_B** : écart < 0,03, ou négatif.
- **Contrôle négatif** : paramètres tirés au hasard dans les bornes à chaque génération ; mémoire remplie de traces permutées. Si ces contrôles font aussi bien que H_A, l'architecte ne choisit rien.
- **Issues** : H_A vraie falsifie « A1 : la réécriture restreinte est cosmétique » ; H_B vraie falsifie « perfectionner notre organisme suffit pour le point 4 » et rend le chemin de réécriture à réinventer (sous bac à sable, voir (c)).
- **Signature de surapprentissage à l'historique** : écart positif sur les familles visibles et nul sur la coffre. C'est exactement ce que § 4 demande au noyau ; cette expérience ne peut pas se faire sans la coffre.

### E5 — Un chercheur automatique saboté est-il détecté ? (faits D, à l'aveugle)

- **Objet** : un agent d'expérience à qui l'on demande, dans une fraction des courses, d'abaisser le résultat au niveau de la génération précédente en justifiant de façon plausible (résumé D).
- **H_A** : un moniteur figé (une sonde sur traces + tests mécaniques, voir (c)) atteint TPR ≥ 0,8 à FPR ≤ 0,05 sur des courses appariées (même hypothèse, même budget, honnêtes vs sabotées).
- **H_B** : TPR < 0,8 à ce FPR, ce qui est le résultat que le résumé D rapporte pour des moniteurs promptés.
- **Contrôle négatif** : courses honnêtes où le résultat baisse pour une raison légitime (graine, variance) ; un moniteur qui les signale mesure la baisse, pas le sabotage.
- **Issues** : H_A vraie falsifie « on ne peut pas faire tourner des agents à pleins droits sans être aveugle au sabotage » ; H_B vraie falsifie « la relecture par agents suffit » et impose des vérifications mécaniques non contournables (reproduction indépendante sous le noyau).

---

## (c) Pour chaque instrument : la mesure minimale qui dit s'il fonctionne

Tous les seuils ci-dessous sont **illustratifs**. Pour chacun, le principe est le même : TPR et FPR sur des cas honnêtes **appariés** (même source, même longueur, même époque), et une vérification mécanique bon marché qu'il faut battre, sinon l'instrument n'apporte rien.

| Instrument (nommé dans la question) | Taux à mesurer | Cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|---|
| **Sondes linéaires sur les activations** (conscience d'évaluation ; § 2.11.1, `entrainer`/`predire`) | TPR/FPR hors pli, sur familles **non vues** (changement de distribution) ; courbe d'étalonnage de `q`. | Échanges d'usage réel appariés par longueur, langue, présence de code, et contenant les mêmes mots-indices (« benchmark », « test ») sans être des évaluations. | Détection par mots-clés (ironiquement, le défaut C-02) ; régression logistique sur sacs de mots ; longueur. Une sonde qui ne bat pas ces trois-là sur les cas appariés lit du vocabulaire, pas un état. Garde déjà dans les faits : exactitude de validation ≥ 0,65 et marge ≥ 0,10 pour voter (RAPPORTÉ, § 2.13.2) — j'y ajoute : exactitude hors famille ≥ celle de la ligne de base + 0,10. |
| **Garanties séquentielles de fausses alarmes** | Taux de fausses alarmes empirique sous flux nul (aucun sabotage) comparé au nominal α, sur 10⁴ flux simulés ; puissance sous dérive lente. | Flux honnêtes **avec** variance non stationnaire (graines, charge) : c'est là qu'un test séquentiel naïf alarme. | Test à horizon fixe + correction de Bonferroni ; seuil fixe sur moyenne glissante. La garantie n'a de valeur que si son FPR réel ≤ α **et** sa puissance dépasse ces deux-là. Cadre : statistique « valable à tout instant » (Ramdas, Grünwald, Vovk, Shafer, 2023, *Game-Theoretic Statistics and Safe Anytime-Valid Inference*, Statistical Science — référence à vérifier pour l'année exacte). |
| **Moniteurs et tests d'acceptation** (sabotage d'un agent délégué) | TPR/FPR de la détection sur triches **plantées** par le noyau (*Planted Sabotage*, § 4). | Traces honnêtes qui contiennent des actions rares mais légitimes (suppression de fichiers, modification de tests avec justification). | Taille du diff ; variation de couverture de tests ; commandes dans une liste noire ; reproduction indépendante du résultat sous graine fixée. Un moniteur à LLM qui ne bat pas « re-exécuter et comparer » est inutile pour ce cas. |
| **Évaluation scellée et grille** (AI-Scientist v3, RAPPORTÉ) | Corrélation entre note de grille et performance sur jeu scellé ; fraction de campagnes où la note monte sans que le scellé monte (« raccourcis »). Les auteurs rapportent 0,44 sur 70 campagnes pour relecteurs-agents (RAPPORTÉ). | Campagnes honnêtes où la performance monte vraiment. | Note du scellé seule. Si la grille n'ajoute pas de pouvoir prédictif au scellé, elle est un canal de Goodhart. |
| **Juge de nouveauté** (ShinkaEvolve, RAPPORTÉ) | Taux de « nouveau » attribué à des reformulations d'un programme existant (FPR) ; taux attribué à des programmes vraiment distincts par un test plantée (TPR). | Paires de programmes équivalents par renommage/réordonnancement. | Distance d'édition sur AST normalisé ; empreinte de comportement sur entrées aléatoires. |
| **Castes contradictoires et arbitre** (§ 2.1, § 2.7) | Gain de score externe de l'arbitrage sur Caste 1 seule, par tâche appariée ; taux où l'arbitre retourne une bonne réponse de Caste 1 (dégradation). Fait à noter : sous le pilote 4, `budget_par_tache = 1`, donc **aucun arbitrage n'a jamais eu lieu** (RAPPORTÉ, CORRECTIONS-v5) ; l'instrument n'a pas été exercé. | Tâches où Caste 1 est correcte avec confiance < 0,78 et > 0,78. | Vote majoritaire de trois appels de la même espèce à température non nulle. |
| **Mémoire spectrale ISVD** (§ 2.4) | Δscore externe sur famille coffre, mémoire pleine vs vidée vs permutée (E4). | Mêmes générations, mêmes graines. | Mémoire « plate » : les k dernières règles induites en texte, sans SVD. Si le texte brut fait aussi bien, la SVD de rang 6 sur `[v, sin v, v²]` n'apporte rien. |
| **Journal d'ablations** `CONFIRME/STAGNANT/REFUTE` (§ 2.11.3) | Concordance entre son verdict et le verdict d'une ablation réelle (mémoire/paramètre retiré) sur coffre. | Générations où Δscore varie par bruit seul. | Test de permutation sur Δscore ; sans cela, « REFUTE » à Δ ≤ 0,01 est une lecture de bruit (HYPOTHÈSE, le seuil 0,01 de § 2.5 n'est accompagné d'aucune variance rapportée). |
| **Filtre de compatibilité bisociatif** (faits C absents) | Fraction d'enfants rejetés qui auraient survécu aux tests sévères (perte) ; fraction d'enfants acceptés qui échouent (fuite). | Paires de domaines réellement compatibles, étiquetées à la main dans le banc planté. | Tirage stratifié sans filtre (E3). |
| **Architecte à gabarit** (C-17) | Idem E4 ; plus le taux de réponses de l'architecte refusées (code brut) et consignées : si > 50 % des réponses sont refusées, l'architecte ne comprend pas le contrat et la « réécriture » est inopérante. | — | Paramètres par défaut. |

Remarque sur les **cas honnêtes appariés** : la correction C-04 a montré que les banques du noyau sont rangées famille par famille et que l'induction ne voyait qu'une famille (RAPPORTÉ). Tout appariement doit donc être fait à tour de rôle par famille **et** par vérité, comme le fait désormais la sélection corrigée ; sinon le TPR mesuré est celui d'une famille.

---

## (d) Ancrage matériel

**Ce qui vient des faits (RAPPORTÉ)** :
- Trois familles de modèles exposées par le noyau, une espèce par caste, première espèce `CLAUDE_FABLE_5_1` ; 1 à 5 castes ; plafonds `max_tokens` 16 384 (tâches, induction, castes), 24 576 (synthèse), 8 192 (requêtes), réflexion incluse ; sous le pilote 4, 123 appels par génération en simulation (1 induction + 2 vérifications + 120 tâches) ; moisson : 4 sources, jusqu'à 6 recherches et 3 téléchargements par moisson (v5.2), quotas dynamiques en v5.3.
- Exécutions de correction en isolation : utilisateur `nobody`, `unshare -n`, environnement vide, `python -I -B` ; ISVD en Python pur, `d = 16`, rang 6.
- Aucun modèle ouvert, aucun GPU, aucun coût par appel ne figure dans les faits.

**Ce que je propose (HYPOTHÈSE, chiffres illustratifs)** :

- **Modèles ouverts pour les sondes sur activations** : une famille 7–9 milliards de paramètres à poids ouverts, en deux tailles si possible pour mesurer le transfert faible→fort (la v5.3 emprunte ce routage). Je ne nomme pas de version précise de mémoire pour ne pas donner un identifiant faux ; critère : poids téléchargeables, activations accessibles couche par couche, licence permettant la recherche. L'extraction d'activations pour ~2 000 échanges × 2 familles tient sur **un GPU de 24 Go**, en quelques heures (illustratif) ; les sondes linéaires s'entraînent sur processeur.
- **E1, E2, E3 (tout sur processeur)** : bancs synthétiques à vérité plantée ; une machine de 8 cœurs suffit ; coût de calcul négligeable ; coût dominant = appels aux modèles de langue pour l'idéation. Ordre de grandeur : 3 voies × 20 `task.md` × 5 castes × 2 répétitions ≈ 600 appels à 16 k jetons ≈ 10 M jetons de sortie (illustratif) ; coût en dollars non estimable sans tarif dans les faits — je le laisse **à chiffrer par le noyau** (`budget()` expose déjà les plafonds).
- **E4** : exige la famille coffre côté noyau (§ 4), non simulable dans l'organisme ; coût = celui de deux courses complètes supplémentaires (une avec architecte et mémoire, une sans), soit ≈ 2 × 123 appels par génération × nombre de générations (RAPPORTÉ pour le facteur 123 ; le reste illustratif).
- **E5** : nécessite un conteneur **sans clés** pour l'agent d'expérience (le README d'AI-Scientist v3, RAPPORTÉ, avertit que ses agents héritent des clés) ; les clés restent dans le noyau, qui fait les appels par procuration, comme l'organisme A le fait déjà (`noyau_client` seulement, aucun accès réseau — RAPPORTÉ). Un conteneur par course, réseau coupé, un volume en lecture seule pour les données ; reproduction indépendante de chaque résultat sous graine fixée avant d'accepter une survie. Calcul : processeur seul pour les expériences semi-synthétiques ; un GPU partagé pour les quelques courses sur activations.
- **Délai** : E1 à E3 sont réalisables en quelques jours de calendrier si les bancs plantés existent ; ils n'existent pas dans les faits, et leur écriture est le vrai coût (HYPOTHÈSE : plusieurs jours-personne). E4 et E5 dépendent de mécanismes du noyau (coffre, triches plantées) déjà demandés en § 4 et non livrés : « moins d'une semaine » (A10) n'est tenable que pour E1–E3.

**Ce qui est réfutable dans cette cellule** : chaque duel ci-dessus a une issue qui me donne tort. En particulier, si E1 et E4 rendent H_B, la voie « perfectionner notre organisme » ne tient pas sur les points 1 et 4 de la question, quelle que soit la solidité des corrections C-01 à C-17 ; et si E2 rend H_B, l'aptitude par sévérité que je propose est à jeter avec le reste.

FIN-DE-CELLULE