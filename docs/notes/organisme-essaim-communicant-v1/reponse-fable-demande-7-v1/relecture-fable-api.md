# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHSCgyA9sVnx6nAzYrGo`
- Heure (UTC) : 2026-11-22T05:48:48Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/organisme-essaim-communicant-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/organisme-essaim-communicant-v1/demande-7-essaim-communicant-v2.md` — sha256 3753db211fdb4e29d7086e362f9cfb7a52cebc6f880cde39df4a8e3e62591139 (compagnon : vérifié)
  - remarques : `docs/notes/organisme-essaim-communicant-v1/contexte-organisme-essaim-v2.md` — sha256 a3209d95410729393b2ee8b362c11014c1e5c4ad7321b4c6859e1fc8c5136ca4 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 6e00d8a1245ce610c398ae02a0154dbb6a5af7032fbf9e86afbc4c2280018606
- Jetons : entrée 10732, sortie 26116 (dont réflexion 15946), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.130496 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 7 — essaim qui communique : demande approfondie, conception et devis

Convention : [FAIT RAPPORTÉ] renvoie aux pièces fournies, [HYPOTHÈSE] est à tester, [PROPOSITION] est un choix de conception. La consigne interdit les noms de personnes et demande les auteurs des antériorités : je donne titre et année, les auteurs sont à relever sur les documents sources.

## A. Méthode « demande approfondie »

### A.1 Ce qu'un expert ferait et qui n'est pas demandé

- [PROPOSITION] **Écrire trois estimandes** : effet de la communication = (a) − (b) ; effet de la pluralité = (b) − (c) ; effet total = (a) − (c).
- [FAIT RAPPORTÉ] Dans la course v67, les deux proposeurs reçoivent la même archive (contexte, § 1 et § 3.1). [PROPOSITION] **L'archive commune est donc déjà un canal de communication**, indirect et filtré par le juge. L'organisme actuel est un échelon intermédiaire, et un bras (b) réellement isolé exige des archives privées par agent.
- [PROPOSITION] **Un agent seul qui relit son carnet communique parfaitement avec lui-même**, au seul coût de la relecture. (a) contre (c) teste donc si des contextes parallèles ajoutent quelque chose à un seul contexte long.
- [PROPOSITION] **Ajouter un placebo de communication** : mêmes messages en longueur et en format, tirés d'un autre monde. Seul ce bras sépare l'information échangée de l'effet de longueur.
- [PROPOSITION] **Ajouter des bases sans modèle**, à coût d'appel nul : tirage uniforme dans la grammaire des lois et énumération gloutonne. [FAIT RAPPORTÉ] La source rapporte un agent seul à 2 % d'optimum, contre 42 % pour un tirage aléatoire (p. 22).
- [PROPOSITION] **Tenir l'espèce constante** dans la course confirmatoire (même modèle pour tous les agents et pour l'agent seul). Sinon la diversité des modèles se confond avec la communication.
- [FAIT RAPPORTÉ] La règle de garde de la famille MR-2 ne tient que sous masquage (8 mondes sur 12 contre 0 sur 12), avec une probabilité 0,02 « estimée, aucune pièce » (contexte, § 3.3). [PROPOSITION] **Mesurer cette probabilité sur de vrais modèles** avant tout, dans le pilote.
- [PROPOSITION] **Analyser en aveugle** : étiquettes de bras brouillées jusqu'au gel du script d'analyse.

### A.2 Données brutes de départ

- [PROPOSITION] Les journaux bruts de chaque appel : texte servi, réponse entière, jetons d'entrée et de sortie rendus par le fournisseur, identifiant daté du modèle, horodatage. Les agrégats par proposeur ne suffisent pas.
- [PROPOSITION] **Toutes les cartes proposées**, sous forme d'arbre, et non les seules promues.
- [PROPOSITION] Les programmes générateurs des mondes et leurs lois vraies.
- [PROPOSITION] Les relevés de facturation des fournisseurs.
- [PROPOSITION] **Premier geste, gratuit** : recalculer l'oracle sur les 23 cartes brutes de v67. [FAIT RAPPORTÉ] La vérité des 12 cartes de la génération 2 n'y est pas rendue (contexte, § 3.1).
- [PROPOSITION] Lire sur document source Re-Search et les annexes de la source descriptive, en particulier les protocoles des études de la page 22. [FAIT RAPPORTÉ] Ils ne sont lus que sur résumé ou parcourus (contexte, § 4 et § 5).

### A.3 Méthodes et outils

[PROPOSITION]
- Mise en forme canonique des arbres de loi : tri des branches commutatives, paramètres ramenés à des classes de tolérance gelées.
- Test de permutation apparié par inversion de signe, unité le monde ; correction de Holm.
- Puissance par simulation avec les proposeurs synthétiques existants, recalée sur l'écart-type du pilote.
- Test d'équivalence à marge gelée pour le test A/A (même bras lancé deux fois).
- Courbes de raréfaction pour les branches ouvertes.
- Rééchantillonnage par monde pour les intervalles.
- Graines dérivées par `numpy.random.SeedSequence`.

### A.4 Ce qui vérifie le résultat, hors du directeur et de Claude

[PROPOSITION]
1. La loi plantée, lue par un programme.
2. Une seconde écriture indépendante de l'oracle, par un autre modèle ou un relecteur humain à partir de la seule spécification, comparée carte à carte.
3. Un test d'invariance : l'oracle rend la même sortie quand les verdicts du journal sont permutés ou supprimés.
4. Des canaris : valeurs sentinelles inscrites dans les champs de verdict, dont l'absence est vérifiée dans tout texte servi aux agents.
5. Le test A/A.
6. L'empreinte du préenregistrement, déposée et horodatée chez un tiers avant le premier appel payant.
7. Le rapprochement des coûts du journal avec la facturation.
8. Les bases sans modèle.

## B. Demande reformulée

[PROPOSITION] « Sur des mondes plantés appariés, mesurer l'effet causal de la communication entre agents sur la couverture de la loi vraie par toutes les cartes proposées, à coût total égal mesuré sur relevés. Séparer cet effet de la pluralité des contextes, de la longueur des textes et du canal que constitue l'archive commune. Prendre pour point de départ les journaux bruts, vérifier l'oracle par une seconde écriture et un test d'invariance aux verdicts, geler le tout avant toute dépense, et écrire d'avance ce qui réfute l'avantage. »

## C. Réponse

### C.1 Égaliser le coût

[PROPOSITION]
- **Unité égalisée** : le coût total de la course par monde et par bras, en « équivalents jetons d'entrée ». Ce coût vaut jetons d'entrée + ρ × jetons de sortie, ρ étant le rapport de prix gelé au préenregistrement, sans rabais de cache.
- **Plafonds rapportés** : entrée, sortie et appels séparément. Les dollars facturés sont rapportés à côté.
- **Tout compte** : proposeurs, messages écrits (sortie) et lus (entrée), tableau partagé relu (entrée à chaque service), carnet relu par l'agent seul, aiguilleur, juge, tests de mort.
- **Hors budget** : les objets de contrôle, identiques dans les trois bras et rapportés à part.
- **Ce que reçoivent (b) et (c)** : le budget de communication est converti en appels de proposeur supplémentaires, chaîne aval comprise, arrondi à l'inférieur. Le reliquat est rapporté.
- **« Rien à la place »** est un bras d'instrument distinct (b0).
- **Contre la victoire par la longueur** : deux cartes par appel exactement, schéma de carte borné, plafond de sortie identique, champ libre limité à 150 mots, jetons réellement consommés en covariable, et placebo de communication.
- **Tableau de coût rendu** : par bras, rôle, génération et, plus tard, espèce — appels, entrée, sortie, équivalents, dollars.

[HYPOTHÈSE] Avec ρ = 5 et les tailles du cas attendu, la communication pèse environ un dixième du coût des proposeurs, soit deux appels de plus pour (b) sur vingt-quatre. L'égalisation déplacera donc peu de tirages.

### C.2 Ce qui est commun, ce que la communication porte

[PROPOSITION]
- **Communs** : aiguilleur, juge statistique, tests de mort, trois générations, grammaire, case de matière, modèle et version datée, quatre agents en (a) et (b).
- **(a)** : archive commune, tableau partagé des formes proposées et des résidus, un tour de messages par génération.
- **(b)** : quatre lignées à archive privée, sans aucun canal. La réunion des cartes n'est faite que par le noyau, pour la mesure.
- **(c)** : un agent, une archive, son carnet.
- **Autorisé dans la communication** : lois proposées en forme canonique, résidus, texte libre borné.
- **Interdit** : statistique du juge, toute lecture d'oracle, identité des objets de contrôle.
- **Scores masqués** dans le bras principal ; le bras à scores visibles est un instrument. [FAIT RAPPORTÉ] La source rapporte 88 % d'essais tardifs autour du meneur quand les scores sont partagés, contre 30 % en indépendance (p. 22).

[PROPOSITION] Le verdict a trois voies possibles vers les agents :
1. Verdict vers archive : c'est une sélection de fiches, permise par N-058 et identique partout. L'appartenance binaire à l'archive est donc visible dans tous les bras.
2. Verdict vers répartition du budget, ordre ou droit de parole : interdit. Le calendrier d'appels est fixe et gelé.
3. Verdict dans les messages : c'est un facteur, masqué par défaut.

La garantie repose sur une liste blanche des champs servis et sur les canaris.

### C.3 Tâches

[PROPOSITION]
- **Famille dépendante** : MR-2, à composantes conditionnelles.
- **Famille de contrôle** : composantes moyennes ordinaires, trouvables sans condition. Elle doit être reparamétrée. [FAIT RAPPORTÉ] La famille précédente était épuisée dès la génération 1 (contexte, § 3.3).
- **Familles inédites** (N-044) : une dépendante et une indépendante, engendrées et scellées, lues à part et jamais fondues dans le test principal.
- **Calibration** : 12 mondes par famille, simulés sans appel.
- **Règle de garde simulée** : celle qui existe déjà.
- **Règle de garde payante**, dans le pilote : couverture médiane du meilleur bras entre 0,1 et 0,8 dans chaque famille. Sinon la famille est reparamétrée sur les seuls mondes de calibration, puis on revient devant le directeur.

### C.4 Graines

[PROPOSITION]
- Une racine gelée dont l'empreinte est déposée.
- Clé de dérivation : (famille, monde, bras, répétition, rôle).
- La graine d'entrée (case de matière, ordre, objets de contrôle) dépend du monde seul. Elle est donc partagée entre bras.
- L'ordre des bras est tiré au hasard par monde, et les trois bras tournent dans la même fenêtre de temps.

[HYPOTHÈSE] L'échantillonnage des fournisseurs n'est pas reproductible par graine. L'appariement porte sur les entrées, non sur les sorties, et le test A/A mesure ce bruit résiduel.

### C.5 Métrique principale et statistique

[PROPOSITION]
- **Couverture** : par monde et par bras, la part des composantes plantées retrouvées dans au moins une carte proposée sur les trois générations. La correspondance est canonique, la tolérance gelée. Une conditionnelle compte seulement si la condition et le signe sont justes.
- **Garde** : le nombre de formes distinctes fausses par monde.
- **Signature de la fonction** : (contenu des cartes, loi vraie). Aucun champ de verdict n'y entre.
- **Preuve** : l'invariance à la permutation des verdicts et la seconde écriture indépendante.

[PROPOSITION] Limite à écrire : le juge agit causalement sur les propositions par l'archive, dans tous les bras. La mesure ne lit aucun verdict, mais la comparaison vaut « sous ce juge ».

[PROPOSITION] Test :
- **Unité** : le monde, apparié entre bras.
- **Statistique** : la moyenne des différences de couverture.
- **Test** : permutation par inversion de signe, bilatéral, Holm sur trois comparaisons, risque global 0,05.
- **Ordre** : (a) − (b) sur MR-2 d'abord.
- **Condition de garde** : un avantage ne compte que si les fausses formes n'augmentent pas au-delà d'une marge gelée.

[HYPOTHÈSE] Signes prédits : (a) > (b) sur MR-2 à scores masqués ; (a) ≤ (b) sur la famille de contrôle ; signe de (a) − (c) non prédit.

[PROPOSITION] Puissance, par approximation normale, à refaire par simulation après le pilote. Au seuil de Holm le plus sévère et à puissance 0,8, il faut environ 10,5/d² mondes, où d est l'effet apparié standardisé. Marge d'efficacité du test comprise, cela donne :

| Effet d | Mondes nécessaires |
|---|---|
| 1,0 | environ 13 |
| 0,8 | environ 19 |
| 0,5 | environ 46 |

[PROPOSITION] Le pilote de bruit lance chaque bras deux fois sur des mondes de calibration. Il rend l'écart-type test–retest et un test d'équivalence. Sur six mondes, il estime le bruit mais ne prouve pas l'équivalence ; il faut l'écrire ainsi.

### C.6 Mesures de Re-Search

[PROPOSITION] **Branches ouvertes** :
- nombre de formes canoniques distinctes nouvellement proposées, par agent et par génération, puis en réunion par bras ;
- recouvrement : part des formes proposées par au moins deux agents ;
- comparabilité entre agent seul et essaim : courbe des formes distinctes cumulées en fonction du coût cumulé, et raréfaction à nombre de cartes égal ;
- pour l'agent seul, découpage de ses appels en quatre blocs, à titre descriptif.

[FAIT RAPPORTÉ] La mesure M2 de nos journaux donne 9 cartes sur 23 répétant une forme (contexte, § 3.1). Elle sert de point de comparaison, non de référence.

[PROPOSITION] **Score au tour k** : couverture cumulée à la génération k, et par décile de coût. Le prédicteur honnête est la couverture à k contre le **gain après k**, en corrélation de rang avec intervalle par rééchantillonnage. Cumul contre total est mécaniquement corrélé. [FAIT RAPPORTÉ] La source montre ce piège : 0,83 sur le total, 0,26 sur la suite (p. 12).

[PROPOSITION] **Arrêt au premier succès** : horizon et budget fixes, aucun arrêt de ce type dans cette course. [FAIT RAPPORTÉ] Sous cet arrêt, un taux par essai mélange des unités (écart E4).

### C.7 Objets de contrôle

[PROPOSITION]
- Le même jeu par monde dans chaque bras et dans chaque lignée de (b) : lois vraies et fausses par construction, témoin d'élimination, carte malformée, copies resservies.
- Ils passent la chaîne mais **n'entrent jamais dans l'archive servie ni dans la couverture**. Sinon une loi vraie plantée fuirait vers les agents.
- **Lecture attendue** : vraie promue, fausse refusée, témoin éliminé, malformée rejetée, copie au même verdict que l'original.
- **Invalidation** : un écart invalide le monde pour les trois bras. L'appariement est gardé, le monde est compté et publié, et il n'est pas remplacé en silence.

### C.8 Arrêts

[PROPOSITION]
- Plafond par bras et par monde à 105 % du budget.
- Monde invalide si les coûts mesurés de deux bras diffèrent de plus de 5 %.
- Arrêt de la course si plus de 10 % des mondes sont invalides.
- Arrêt si un témoin manque ou si un canari apparaît dans un texte servi.
- Arrêt si l'écart-type du pilote rend l'effet minimal d'intérêt indétectable au nombre de mondes décidé.
- Plafond global.
- Chaque arrêt rend un rapport et aucun repli.

### C.9 Ce qui réfuterait, ce qui ne trancherait rien

[PROPOSITION] **Réfutent l'avantage de la communication** :
1. (a) − (b) sur MR-2 a un intervalle sous l'effet minimal, ou est négatif.
2. L'avantage se retrouve à l'identique sous placebo : c'est un effet de longueur.
3. L'avantage vient avec plus de formes fausses, au-delà de la marge.
4. (a) ne dépasse pas (c) : un contexte long suffit.
5. (a) ouvre moins de branches à nombre de cartes égal, sans gain de couverture.
6. (a) ne dépasse pas le bras « archive commune seule » : les messages n'ajoutent rien à l'organisme actuel.

[PROPOSITION] **Restreignent sans réfuter** :
- un avantage seulement sur MR-2 et nul sur le contrôle : c'est l'interaction prédite ;
- un avantage seulement à scores visibles : résultat à porter devant N-058.

[PROPOSITION] **Ne tranchent rien** :
- intervalle couvrant à la fois zéro et l'effet minimal ;
- plafond ou plancher de couverture ;
- plus de 10 % de mondes invalides ;
- test A/A échoué ;
- résultat sur une seule espèce étendu aux essaims hétérogènes.

### C.10 Antériorité

Tout ce qui suit est **rapporté de mémoire, non vérifié sur document source**, et aucun chiffre n'est opposable.

Agents de langage, à calcul comparé :
- « Self-Consistency Improves Chain of Thought Reasoning in Language Models » (2022) : la base « vote à k ».
- « Improving Factuality and Reasoning in Language Models through Multiagent Debate » (2023).
- « Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs » (2023).
- « Rethinking the Bounds of LLM Reasoning: Are Multi-Agent Discussions the Key? » (2024).
- « More Agents Is All You Need » (2024).
- « Reasoning in Token Economies: Budget-Aware Evaluation of LLM Reasoning Strategies » (2024).
- « Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models? » (2025).
- « Rethinking Mixture-of-Agents: Is Mixing Different Large Language Models Beneficial? » (2025).
- « Why Do Multi-Agent LLM Systems Fail? » (2025).
- « Towards a Science of Scaling Agent Systems » (2025).

Recherche par agents :
- « Mathematical discoveries from program search with large language models » (2023) : populations en îles.
- « AgentRxiv: Towards Collaborative Autonomous Research » (2025) : laboratoires partageant une archive.

Collectifs humains et simulés :
- « Productivity Loss in Brainstorming Groups: Toward the Solution of a Riddle » (1987) : groupes nominaux contre groupes en interaction.
- « The Network Structure of Exploration and Exploitation » (2007).
- « The Communication Structure of Epistemic Communities » (2007).
- « How social influence can undermine the wisdom of crowd effect » (2011).

[HYPOTHÈSE] La zone « équipe communicante contre votes indépendants ou agent seul, à budget apparié, sur bancs de raisonnement » est **occupée**. Mon souvenir est que les gains s'y réduisent souvent quand le budget est apparié.

[HYPOTHÈSE] L'effet de troupeau sous information partagée est ancien dans la littérature des collectifs.

[PROPOSITION] La zone « communication, îles, agent seul, coût égal, loi plantée, oracle indépendant du juge, plusieurs générations » reste une **question**. Je ne connais pas de travail qui la couvre, ce qui ne vaut pas absence. Le caractère observationnel de la source est la limite d'un papier, non un trou du champ.

## D. Devis en unités

[PROPOSITION] Une « course de bras » est un monde, un bras et trois générations. Le cas attendu se compose ainsi :

| Bras | Appels de proposeur | Appels de message | Cartes | Appels d'aiguilleur |
|---|---|---|---|---|
| (a) | 24 (4 agents × 2 appels × 3 générations) | 12 | 48 | 48 |
| (b) | 26 | 0 | 52 | 52 |
| (c) | environ 26, carnet relu | 0 | environ 52 | environ 52 |

Tailles par appel :
- [FAIT RAPPORTÉ] Sortie de proposeur : 6 000 jetons à l'estimation, 16 000 au haut. Ce sont des devis, non des mesures (contexte, § 3.4).
- [HYPOTHÈSE] Message : 3 000 jetons d'entrée, 400 de sortie.
- [HYPOTHÈSE] Aiguilleur : 2 000 d'entrée, 300 de sortie, sans pièce.
- [HYPOTHÈSE] Juge statistique : aucun appel de modèle.
- [HYPOTHÈSE] Test de mort : un appel par carte promue, au plus 52 par course de bras.

Ces quatre hypothèses sont à vérifier dans le noyau.

Nombre de courses de bras :

| | Bas | Attendu | Haut |
|---|---|---|---|
| Pilote A/A (mondes × 3 bras × 2 répétitions) | 4 → 24 | 6 → 36 | 6 → 36 |
| Confirmatoire, MR-2 + contrôle (× 3 bras) | 12 + 8 → 60 | 20 + 12 → 96 | 44 + 20 → 192 |
| Bras d'instrument | 4 mondes × 2 → 8 | 8 × 4 → 32 | 12 × 4 → 48 |
| Familles inédites (× 3 bras) | 0 (reportées) | 12 → 36 | 20 → 60 |
| **Total** | **92** | **200** | **336** |

Totaux d'appels et de jetons :

| | Bas | Attendu | Haut |
|---|---|---|---|
| Appels de proposeur (environ 25 par course) | 2 300 | 5 000 | 8 400 |
| Jetons par appel de proposeur, entrée / sortie | 4 000 / 3 000 | 9 000 / 6 000 | 20 000 / 16 000 |
| Jetons de proposeur, entrée / sortie (millions) | 9,2 / 6,9 | 45 / 30 | 168 / 134 |
| Appels d'aiguilleur | 4 600 | 10 000 | 16 800 |
| Appels de message | 384 | 864 | 1 440 |
| Répétitions confirmatoires par monde et par bras | 1 | 1 | 1 |

Les bases sans modèle ne coûtent aucun appel.

## E. Préenregistré ou instrument

[PROPOSITION] **À préenregistrer** :
- estimandes et bras confirmatoires ;
- ρ et tolérances ;
- fonction d'oracle et règles de correspondance ;
- statistique, seuils, signes, ordre de Holm ;
- effet minimal d'intérêt et marge sur les fausses formes ;
- règles de garde, d'invalidation et d'arrêt ;
- racine des graines, liste des mondes scellés ;
- issues réfutantes.

[PROPOSITION] **Peuvent partir comme instruments**, sans dépense ou à faible dépense :
- recalcul de l'oracle sur v67 ;
- seconde écriture de l'oracle ;
- canaris ;
- pilote de bruit ;
- bras placebo, scores visibles, archive commune seule, (b0) et vote à k ;
- mesures de Re-Search ;
- bases sans modèle.

## F. Décisions qui reviennent au directeur

**1. Fixer l'unité de coût égalisée.**
- Enjeu : elle détermine ce que (b) et (c) reçoivent.
- Option A, équivalents jetons à rapport gelé : stable, insensible aux tarifs et au cache ; s'écarte de la facture.
- Option B, dollars facturés : fidèle à N-045 ; varie avec le cache et les tarifs.
- Option C, nombre d'appels : simple ; ignore la longueur.
- Recommandation : A, avec B rapporté. Confiance 0,75.

**2. Définir « isolés » : archives privées ou archive commune.**
- Enjeu : avec l'archive commune, (b) communique déjà.
- Option A, archives privées en (b) et « archive commune seule » en instrument : contraste net ; tests de mort dupliqués.
- Option B, archive commune partout : conforme à la lettre de la demande ; ne mesure que le canal ajouté.
- Option C, les deux en confirmatoire : échelle complète ; un tiers de coût en plus et quatre comparaisons.
- Recommandation : A. Confiance 0,7.

**3. Fixer le nombre de mondes et de répétitions.**
- Enjeu : c'est la taille d'effet détectable.
- Option bas (12 + 8 mondes) : peu coûteux ; ne voit qu'un effet d'environ 1 écart-type.
- Option attendu (20 + 12) : voit environ 0,8.
- Option haut (44 + 20) : voit environ 0,5 ; près du double.
- Recommandation : payer le pilote, puis décider sur l'écart-type mesuré, en partant de l'attendu. Une répétition par monde en confirmatoire, deux au pilote. Confiance 0,65.

**4. Décider la visibilité des scores du juge dans la communication.**
- Enjeu : effet de troupeau rapporté par la source, et frontière de N-058.
- Option A, masqués en confirmatoire et visibles en instrument : prudent ; laisse la question des scores sans test puissant.
- Option B, visibles : proche d'un essaim « naturel » ; risque de troupeau et de sélection sur moniteur.
- Option C, facteur croisé : complet ; coût doublé pour (a).
- Recommandation : A. Confiance 0,8.

**5. Placer le bras « un modèle, vote à k, coût apparié ».**
- Enjeu : c'est le témoin exigé par N-045, proche de (b) quand l'espèce est unique.
- Option A, instrument sur 8 mondes : respecte N-045 à faible coût ; pas de test puissant.
- Option B, quatrième bras confirmatoire : test complet ; six comparaisons et puissance diluée.
- Option C, déclarer que (b) en tient lieu : gratuit ; (b) garde des lignées sur trois générations, ce que le vote n'a pas.
- Recommandation : A. Confiance 0,6.

**6. Choisir une espèce unique ou un essaim hétérogène pour la course confirmatoire.**
- Enjeu : la diversité des modèles se confond avec la communication.
- Option A, espèce unique gelée d'avance : contraste propre ; portée limitée.
- Option B, hétérogène : proche de l'organisme réel ; l'agent seul devient ambigu.
- Option C, unique puis réplique sur une seconde espèce : robuste ; plus cher.
- Recommandation : A, puis C au cas haut. L'espèce est choisie avant toute course, jamais sur un verdict. Confiance 0,7.

**7. Ordonner cette course par rapport aux autres courses de l'organisme.**
- Enjeu : elle dépend d'un oracle sur toutes les cartes et de la tenue réelle de MR-2.
- Option A, d'abord les instruments gratuits et le pilote, puis la course confirmatoire après la course multi-générations sur MR-2 : chaque étape sécurise la suivante ; délai.
- Option B, en parallèle : rapide ; risque de payer sur une famille qui plafonne.
- Option C, avant tout le reste : réponse tôt ; règle de garde non vérifiée sur vrais modèles.
- Recommandation : A. Confiance 0,7.

FIN DE LA RÉPONSE
