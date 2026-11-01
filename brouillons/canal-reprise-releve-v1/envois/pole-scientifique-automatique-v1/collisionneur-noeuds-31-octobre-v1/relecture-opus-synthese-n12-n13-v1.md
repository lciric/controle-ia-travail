# Relecture indépendante (Opus) de la synthèse du collisionneur sur les nœuds N12 et N13 — v1

- **Relecteur** : sous-agent neuf, modèle Opus 5.5 (`claude-opus-5-5`), lignée conv-audit, en application de R-746 (`registres/decisions.md` : relecture indépendante, par un Opus neuf, de toute synthèse du collisionneur avant qu'elle serve). Je n'ai écrit ni la question, ni l'annexe, ni les critères, ni la synthèse, ni aucune cellule.
- **Dates** (`date -u`) : début de lecture `Sun Nov  1 09:13:58 UTC 2026` ; fin de lecture des pièces `09:22:48 UTC` ; début d'écriture `09:24:05 UTC`.
- **Limites** : rien lu sous `donnees/` (ni cellules, ni faits servis `faits-n12-n13-v1.md`, ni `etat.md` du run). Lecture seule : aucun commit, aucun `.sha256` écrit, aucun fichier existant modifié, aucun `git fetch`, aucun appel de réseau ni de modèle. Les deux PDF n'ont pas été ouverts (empreintes contrôlées par `sha256sum -c` seulement).
- **Lu en plus des pièces de la consigne**, pour recouper le fond sans les faits servis : les sources des pièces 1, 2, 4 et 5 (N-045 v2, N-058 v1, lectures vérifiées d'Avalon-M1 et de Damani), et N-053 v1 (citée par N-058). Les décisions sont lues sur la référence locale `origin/main` (commit `45853968`, sans `fetch`). Les numéros de ligne « pièce N, l. n » de la synthèse renvoient aux faits servis, que je n'ai pas lus. Ils sont cohérents avec un décalage constant sur N-045 (+22 lignes) et sur N-058 (+147 lignes). C'est une inférence, pas une vérification.

## Empreintes SHA-256 recalculées (`sha256sum`)

| Pièce | SHA-256 | Contrôle |
|---|---|---|
| Synthèse, copie `/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/n12-n13/synthese-n12-n13-v1.md` | `b1d28f0d43245c3534d469f38e77bf4e14da2a70f39f4f1bd76a0b42c96b8cb4` | égale au compagnon et au préfixe de la consigne |
| Critères scellés, même dossier, `criteres-lecture-n12-n13-v1.md` | `71b63584563eb6fc6cb7880ade286e31596c49583d2f7615f0b279cebff3c589` | égale au compagnon et à la version de `origin/main` |
| Critères du tour 1 importés (copie `…/scratchpad/main-lecture/criteres-lecture-noeuds-v12-tour1-v1.md`) | `22edbf4751c205f6760a136963bfaebcede773bfdc3300e923ad8e5df4e3a529` | égale au compagnon et au `22edbf47…` des critères |
| Question v2 `…/collisionneur-noeuds-31-octobre-v1/question-collisionneur-n12-n13-couches-recompense-v2.md` | `9faee0aadf01b4837fa67df414ed4552519d80c6c31c9326976c27e391de6986` | égale au compagnon |
| Annexe du tour 2 `annexe-tour-2-n12-n13-v1.md` | `9dc13ece12d3864cc255b66dbdae869c9219887f932dfa83ab91714a22e0156d` | égale au compagnon et au `9dc13ece…` des critères |
| Relecture de la veille `relecture-opus-synthese-noeuds-v12-tour1-v1.md` | `d1209130627f3e5c0ef7198016897c588a8b5ec3e36745084ec7b546475932b9` | égale au compagnon |
| `registres/decisions.md` (R-746, R-1012, R-1013, R-1016) | `a6b66eb8809ffc07aec1696d982ec262f26f63ea172ccc58da34b7b5dfe31307` | pas de compagnon |
| N-045 v2 (`origin/main:docs/decisions/decision-N-045-v2.md`) | `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d` | égale au compagnon |
| N-058 v1 (`origin/main`) | `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d` | égale au compagnon |
| N-053 v1 (`origin/main`) | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` | égale au compagnon |
| Lecture vérifiée d'Avalon-M1, `docs/notes/rlcr-v1/lecture-verifiee-avalon-m1-v1.md` | `a8251ea8bca96acad1443eea24a090e7b254efa1d17d1fec6119ff9544c40583` | égale au compagnon |
| Lecture vérifiée de Damani, `docs/notes/rlcr-v1/lecture-verifiee-damani-rlcr-v1.md` | `4e29301af66bf702387ff5923018979c65ea9cde702dce93862b65031a1c9bc0` | égale au compagnon |

## Verdict en une phrase

**Tenue sous condition.** Les positions par espèce sont traçables. Les chiffres de la question et des pièces sont exacts, et tous les recalculs aussi. Mais le décompte de tête n'est pas reconstructible (accords et apports seuls comptés deux fois ou mal classés). Trois « faits saillants » disent plus que ce que portent les pièces (couverture de N-045, « (c1) est le témoin », preuve tirée de Damani pour la recalibration a posteriori). L'objection de B sur (c3) a disparu. Et les tables reproduisent des paramètres de conception que R-1012 exclut. Un erratum est nécessaire avant que la synthèse serve.

## Constats

Gravité : **majeure** (change la lecture d'un nœud ou interdit de servir en l'état), **moyenne** (fausse un décompte ou un fait saillant), **mineure** (forme), **conforme**.

**RN-01 — Décompte des accords (« 7 dont 5 larges ») — majeure.**
- Les sept accords listés ont tous trois ou quatre espèces. Or le critère 7 du tour 1 appelle « large » tout accord à trois ou quatre espèces. Le « 5 » compte en réalité les accords **à quatre** (n° 1, 2, 3, 4 et 6).
- Le n° 6 (« cause collective non établie ») est, d'après la synthèse elle-même, la raison commune du n° 5 (l. 114). Le même item est donc compté deux fois.
- Le n° 4 ((c2) écartée) est « vrai par construction pour la raison » (l. 113). Le n° 3 (étape 2 d'abord) est dit porté par la question et par la pré-collision, « vrai par construction » (l. 99). Le critère 11 du tour 1 exclut des accords ce qui est vrai par construction.
- Le n° 5 compte B, qui « rejoint en T3 » : c'est une convergence née de la critique, pas un accord de T1.
- Le n° 7 réunit A, C et D au décompte, mais seulement A et C au texte (l. 150), et pour une autre raison.
- À l'inverse, le texte déclare « accord indépendant » le lien 3 (A et C, l. 162) et décrit les liens 1 (quatre espèces) et 6 (deux espèces) sans les compter.
- Selon la règle retenue, on obtient entre 4 et 9 accords. Il faut écrire la règle.

**RN-02 — Apports seuls (11) — moyenne.**
- Le n° 3 (« faux trilemme », A) est compté à la fois comme apport seul et comme accord large (l. 196). Cela contredit la définition « jamais repris ».
- Le n° 7 (B, prédiction de l'omission avant le point de décision) est « né de la critique d'A ». C'est une convergence au sens du critère 8.
- La ligne 84 déclare « apports seuls, non réfutés » les **quatre** risques de la couche 3 (un par espèce). La liste n'en garde que deux (B et C). Le risque de D (effets indirects, déplacement du problème) manque. Celui de A est dit « non réfuté » à la ligne 84 et « contesté » à la ligne 163.
- La répartition A 3, B 4, C 2, D 2 n'est donc pas fiable.

**RN-03 — Cessions, divergences résolues — mineure.**
- Le tableau des convergences totalise bien 39 cessions. Mais la famille 1 compte « A sur lui-même », et la famille 7 compte D, dont la synthèse dit « D l'avait » (l. 131). Au sens du critère 8, on a donc au plus **37** cessions.
- Les 6 divergences résolues font toutes aussi partie des cessions (familles 2, 4, 6, 8 et 13). Ce chevauchement n'est pas déclaré, et la règle qui retient 6 cessions sur 39 comme « divergences » n'est pas écrite.
- Les 9 divergences non résolues concordent entre le décompte et la liste (même nombre, même ordre). Seule exception : l'étiquette « jamais » de la n° 5 au décompte, qu'aucune espèce ne porte dans la liste.

**RN-04 — Objection de B sur (c3) absorbée — majeure.**
- En T1, B juge (c3) « séduisante mais circulaire » : le motif d'Avalon n'est pas diffus (un point de décision par scénario, pas de dommage accumulé ; pièce 4).
- La synthèse range ce point sous « contrefactuel traité » (l. 116) et fait « venir B de fait » à l'accord (l. 114).
- Or la lecture vérifiée d'Avalon porte la même objection : « Diffuse : en partie » ; « Menace : non établie ». R-1013 la reprend : « cas d'étude pour la pince : non en l'état ». Cette objection vise la prémisse même de la question (« précisément la menace diffuse par omission »).
- Elle ne figure ni parmi les divergences ni parmi les apports. Il faut la rétablir.

**RN-05 — Fait saillant « N-045 ne couvre pas la génération d'instruments neufs » — moyenne.**
- J'ai vérifié sur N-045 v2. L'énoncé 1 range parmi les modèles qui servent un rôle les « instruments locaux entraînés par le noyau (sonde, adaptateur) ». L'énoncé 5 parle de « sondes et adaptateurs entraînés à t, utiles à t+1 ». L'énoncé 6 (ii) fait entraîner par l'organisme un adaptateur qui propose des conceptions.
- Ce que les espèces disent non couvert est plus étroit : **l'écriture de code hors catalogue** (moniteurs écrits, règle d'agrégation codée), et la preuve formelle.
- Le critère 5 n'est pas appliqué à cette affirmation. Il est appliqué à A (« code des échanges », jugé « à la limite »), mais pas à B (« règle d'agrégation par code » non couverte), alors que l'énoncé 1 inscrit « la règle d'agrégation » parmi ce qui est appris. C'est une asymétrie au regard de R4 (même audit des deux côtés).
- B et C répondent « non » en T1, et la synthèse les recode en « couverture partielle » sans le dire.

**RN-06 — Fait saillant « (c1) est le témoin qui manque, (c3) son sous-produit, (c2) tombe par le dessin de la course 2 » — moyenne.**
- La première partie est la phrase de A seul (A-T1 A7). La pièce 4 nomme autrement le témoin qui manque à Avalon : un run mono-agent à calcul égal (p. 40). Elle nomme aussi une cause concurrente : tout entraînement qui ne récompense pas le signalement (réserve 1).
- Une comparaison collective contre individuelle à deux bras ne sépare pas ces causes. La synthèse rapporte d'ailleurs qu'en T3, A (bras à poids gelés), B (bras non entraîné) et C (témoin mono-agent) ajoutent ce troisième bras, sans en conclure que (c1) à deux bras ne suffit plus.
- « (c3) sous-produit » : A, C et D en T1 (le mot est de D). B y est rattaché à tort (RN-04).
- « (c2) tombe par le dessin de la course 2 » : A, B et C, avec une exclusion contingente. D ne le dit pas.

**RN-07 — « Cause collective non établie » tenue par les quatre — moyenne.**
- La prémisse est soutenue par les renvois pour A (A-T1 A7) et pour B (S6).
- Pour C et D, les tables donnent d'autres raisons : transposabilité aux petits effectifs pour C, canal d'apprentissage à fixer pour D. Aucun renvoi ne montre qu'ils tiennent cette prémisse. C'est une inférence du lecteur, à vérifier sur les cellules (et le décompte la compte deux fois, voir RN-01).

**RN-08 — « Seule pièce sans dépense : recalibration a posteriori des juges » — moyenne.**
- (i) L'unicité dépend d'une catégorie « sans dépense de carte » créée pour le test de la couche 4. Elle sort du critère 13 du tour 1, qui ne connaît que « sans dépense » et « avec dépense ». B (« processeur, quelques jours ») et D (« processeur ») entrent peut-être dans « sans dépense », si les appels de sous-agents ne sont pas payants : la question n'est pas tranchée.
- (ii) Une raison de la famille 4 dit que « le post-hoc fait jeu égal ou mieux hors domaine » (l. 177). C'est faux sur les moyennes hors domaine de la Table 1 de Damani (modèle entraîné sur HotpotQA) : aire sous la courbe de discrimination 0,68 pour la récompense de calibration contre 0,58 pour le classifieur, score de Brier 0,21 contre 0,27, erreur de calibration 0,21 contre 0,24. Ce n'est vrai que sur SimpleQA et GSM8K, ce que la ligne 148 dit correctement.
- (iii) Le « classifieur post-hoc » de Damani est un modèle de 7 milliards de paramètres, initialisé depuis Qwen2.5-7B puis entraîné. Il ne prouve rien sur une recalibration de Platt (ajustement logistique a posteriori) faite sur processeur. L'ordre « recalibration d'abord » repose donc sur un argument de coût, pas sur un résultat de la pièce 5.
- (iv) La formule « sur paires déjà produites par les courses » suppose que des confiances (ou des probabilités de jetons) des juges sont déjà journalisées, avec une vérité d'oracle. Ce n'est pas établi.

**RN-09 — Divergence n° 1 (moniteurs neufs comme filtre de fiches) — moyenne.**
- Le point 5 de N-053, cité par N-058, interdit tout score de moniteur (sonde, juge) « dans un signal d'entraînement ou de sélection de l'agent ». Il le dit valable « pour la piste organisme (N-045) ».
- L'exception de N-058 (la sélection des fiches reste permise) ne couvre pas des fiches filtrées qui nourriraient ensuite un affinage (N-045, énoncés 4 et 6 (ii)).
- La divergence peut donc être tranchée sur une pièce nommée, N-053, plus un fait de la cellule A-T3 : les fiches filtrées entrent-elles dans un entraînement ? La synthèse la présente comme « lecture à confirmer par Lazar », sans nommer N-053.
- Note sur les critères eux-mêmes : le critère 11 résume N-053 en « aucun score de moniteur dans l'entraînement de l'agent ». Il omet « ou de sélection ».

**RN-10 — « Effet d'ordre » sur N12 (3) — mineure.**
- La raison donnée par la synthèse (l'option est offerte par la question, la pré-collision la porte, c'est « vrai par construction ») n'est pas celle du critère 12 : option présentée la première, ou avec le plus de détail.
- La réserve reste défendable par « le plus de détail ». Mais si l'accord est vrai par construction, il ne compte pas (RN-01).

**RN-11 — Divergences non résolues : trop peu tranchables par un tiers — moyenne.** Détail au tableau ci-dessous. Une seule (n° 1) est tranchable sur une pièce nommée, et la synthèse ne nomme pas cette pièce. Les n° 4, 5 et 6 ne donnent pas les raisons de chaque côté, que le critère 9 du tour 1 exige. Les codes « Q2, N4 » de la n° 5 ne sont pas expliqués, avec un risque de confusion avec le nœud N4 de la question v12, qui est hors question.

**RN-12 — Recommandation et classement (question 8, critère 17) — mineure.**
- Aucune recommandation sur N12 ou N13 ; les « décisions recommandées » de C sont bien rapportées comme positions.
- En revanche, le lecteur ajoute une pièce que nulle espèce ne propose : « je le note pour la veille » (Agrawal et collègues, l. 240).
- Il classe aussi les espèces (« la plus complète », l. 129 ; « la plus prudente », l. 225), alors qu'il dit ne pas le faire (l. 272).

**RN-13 — Critères 3 et 6 — mineure.**
- Les « 4 reprises » de la pré-collision recouvrent deux reprises (B, C) et deux critiques : A la cite pour la contredire, D dit qu'elle « ne constitue pas une preuve ».
- La question gèle « le noyau, les gardes et les bornes ». D'après les tables, aucune espèce ne nomme les bornes, et la synthèse ne le relève pas.

**RN-14 — Débordement vers une conception (règle de sécurité ; R-1012 : « pas de conception de mécanisme ») — majeure pour servir.**
- La garde du critère 1 ne vise que la menace par omission. La synthèse la respecte : deux classes, rien reproduit.
- Mais elle reproduit des paramètres de conception de deux classes :
  - (a) l'entraînement de notre organisme sous récompense collective : l. 107–110, 117–118, 183 et 194 ;
  - (b) la génération de code par l'organisme dans la couche 3 : l. 79–80.
- Je le signale sans le développer. Avant de servir la synthèse, il faut remplacer ces passages par des renvois de cellule. Le sujet voisin (« s'inspirer de la recette d'Avalon pour l'auto-organisation ») est suspendu : ma carte de décision reste au niveau de la gouvernance.

**RN-15 — Conformités (questions 1 et 4) — conforme.**
- En-tête complet (critère 15) : modèle du lecteur déclaré, date relevée après la lecture, empreintes, état du run, annexe non lue.
- Ordre cohérent : critères scellés à 08:07, état mis à jour à 08:39:00, lecture complète à 08:44:52.
- Aucun passage hors question. Les sous-questions sont traitées une par une, sans incomplétude sur la distinction entre couches 3 et 4. La traçabilité passe par une convention déclarée (« A-T1 A3 » renvoie à la cellule de conception de A, section A3).
- Les chiffres et citations de la question sont reproduits **exactement** :
  - Avalon : refus ≥ 99 % ; alertes à l'inspecteur général ≤ 7 % dès le pas 100 ; signalement au régulateur 68 → 36 → 45 % (pas 170 et 180) ; 77 → 0–3 % et 97–100 % pour la cyberattaque ;
  - le reste : 24 fusions, C-17 à trois paramètres, « inutile ici », « de la dorure », les deux sens de « RLCR » distingués, et les empreintes `6429a78f…` et `f393de47…`.
- J'ai recoupé sur les lectures vérifiées les deux inexactitudes relevées par la synthèse, et elles sont justes :
  - B : 0,37 est l'erreur de calibration de l'apprentissage à récompense vérifiable ; celle du modèle de base est 0,53 (HotpotQA) et 0,39 (mathématiques) ;
  - A : la courbe du régulateur n'est pas monotone.
- Les huit recalculs ont été refaits et sont exacts : 0,942 ; 0,179 ; 0,570 ; 0,0786 ; 0,0892 ; 20 ; 0,315 ; 0,109. Pour le maximum de dix lois normales, 1,36 par la formule asymptotique et 1,54 en valeur exacte.

**RN-16 — Réserve de famille (question 7).**
- Le lecteur, Claude Fable 5.1, est du modèle de l'espèce A, et il le déclare.
- Indices dans un sens : les cadrages de A structurent la synthèse (« faux trilemme », « c'est *le* bras », « note transversale » érigée en méthode commune). A porte 8 des 13 familles de convergence, et D est décrite par le jugement de A en T2. Influence réelle ou biais : on ne peut pas le dire sans les cellules.
- Indices dans l'autre sens : A reçoit le plus d'inexactitudes, et B échappe à un relevé symétrique (RN-05).
- Autres liens :
  - B (Opus 4.6) est du même modèle que l'auteur de la question et de l'annexe (conv-audit, en-tête de la question v2) : l'accord de B avec l'annexe est moins indépendant ;
  - moi-même, Opus 5.5, je suis du modèle de l'auteur de la lecture vérifiée d'Avalon (pièce 4), et de la même famille que A, B et le lecteur.

**RN-17 — Annexe du tour 2 : ce que la synthèse devine ou contredit (sans la juger sur elle).**
- **N12** : la synthèse devine la conclusion (étape 2 d'abord, à quatre). Elle nuance la prémisse « aucune pièce ne montre un besoin non couvert » : les quatre nomment des capacités non couvertes, sans besoin chiffré ; D ajoute une condition (prévoir la mesure du résidu dans l'étape 2) ; B ajoute un risque inverse (coût d'un organisme figé, calendrier).
- **N13** : elle devine « (c3) insuffisant seul » et « (c2) écarté ». Mais trois espèces font de l'exclusion de (c2) une contingence du dessin de la course 2, pas une question de périmètre.
- Elle devine (c1) mais **contredit sa forme à deux bras**, puisque A, B et C ajoutent un troisième bras en T3. Elle place aussi des mesures sans entraînement **avant** (c1).
- Elle ajoute ce que l'annexe n'a pas : une précaution à seuil gelé, et le volet Damani.
- La coïncidence avec l'annexe est sous effet d'ordre : (c1) est présentée la première et avec le plus de détail, dans une question écrite par l'auteur de l'annexe.

### Les neuf divergences non résolues : tranchables par un lecteur neuf ?

| N° | Objet | Tranchable sur | Manque |
|---|---|---|---|
| 1 | Moniteurs neufs comme filtre de fiches (A contre C) | **pièce nommée** : N-053, point 5, plus la cellule A-T3 (E1′) | la synthèse ne nomme pas N-053 (RN-09) |
| 2 | Dilution du crédit : artefact ou définition | cellules C-T2 (a2) et A-T3, plus pièce 4 (crédit plat d'Avalon) | aucun critère de décision écrit |
| 3 | La voie hors ligne reproduit-elle la pression d'Avalon ? | ni sur cellules ni sur pièce : B et D n'ont pas répondu | à poser au tour 2, avec la mesure de « pression » attendue |
| 4 | Nature de la précaution de N13 (2) | non : « divergence sur le reste » | énumérer les éléments en litige et les raisons de chaque côté |
| 5 | Forme d'une ouverture de la couche 4 | choix de Lazar ; la position de C (« Q2, N4 ») est introuvable dans la table N12 (2) | raisons et codes à expliquer |
| 6 | Première expérience | choix de Lazar (coût) ; ce sont des compléments, pas des exclusions | raisons de chaque côté |
| 7 | Exécution hors bac à sable (B contre C) | pièce non nommée : quel texte porte « l'invariant du noyau gelé » pour l'exécution ? | nommer la pièce |
| 8 | Amortissement du coût de génération (C contre D) | calcul possible une fois K et le coefficient de coût gelés (N-045, énoncé 2) | hypothèses du calcul |
| 9 | Transfert d'une sonde à un autre modèle (B contre D) | expérience seulement | — |

## Points qui exigent les cellules (ou les faits servis)

1. Le texte de B sur (c3) (« circulaire », motif non diffus) en T1, et ce qu'il en reste en T3.
2. La prémisse « cause collective non établie » chez C et D (cellules de T1).
3. La composition de l'accord n° 7 (A et C, ou A, C et D) et ses raisons.
4. La réponse littérale de B et de C à N12 (1) (« non »), et ce qu'ils disent des énoncés 1 et 5 de N-045 (instruments locaux entraînés).
5. Si les fiches filtrées par les moniteurs de A (A-T3, E1′) entrent dans un entraînement (règle N-053).
6. Comment le bras « récompense du signalement » de B détecte un signalement (mécanisme ou juge), pour la règle N-053.
7. La règle de sélection des 6 divergences résolues parmi les cessions ; les 39 cessions (A sur lui-même, D « l'avait »).
8. Le statut de dépense des appels de sous-agents pour le test de la couche 4 (A, B, D).
9. Si une espèce présente la recalibration de Platt comme établie par Damani, et si les confiances des juges actuels sont journalisées.
10. Les codes « Q2, N4 » de C.
11. Les « bornes » gelées : une espèce les nomme-t-elle ?
12. Les liens 1, 3 et 6 : accords à compter ou non.
13. L'heure de début de lecture du lecteur, à confronter au journal de session-depot.

## Carte de décision pour Lazar — N12 et N13 (nœuds de décision : pas de défaut à 48 heures)

Préalable : ne t'appuie sur la synthèse qu'après un erratum sur RN-01, RN-04 à RN-09 et RN-14. Ses positions par espèce restent utilisables dès maintenant.

### N12 — rouvrir ou non les couches 3 et 4 de l'organisme

- **Décision** : rouvrir maintenant l'une des deux couches, ou les garder fermées jusqu'aux résultats de l'étape 2. Pour rappel :
  - la couche 3 = moniteurs neufs écrits à la demande, plus réécriture de soi restreinte dans un bac à sable ;
  - la couche 4 = pôle théorie et vérification formelle en Lean ;
  - à l'étape 2, l'organisme apprend sa composition (décision N-045 du 25 octobre) et cette composition est jugée sur l'oracle du monde planté et le coût, jamais sur le verdict du juge (décision N-058).
- **Enjeu** : les quatre modèles s'accordent sur le constat. N-045 couvre le choix et l'entraînement d'instruments dans un catalogue, mais pas l'écriture de code hors catalogue ni la preuve formelle. Aucun ne chiffre un besoin. Il y a deux angles morts, chacun signalé par une seule espèce : le coût d'un organisme figé n'est chiffré par personne (Opus 4.6), et l'étape 2 ne renseignera rien si elle ne mesure pas ce que le catalogue manque (Kimi). Une question préalable se pose aussi : une fiche filtrée par un moniteur peut-elle nourrir un affinage ? La règle N-053 (aucun score de moniteur dans un signal d'entraînement ou de sélection) semble l'interdire.
- **Options** :
  - **(a)** Garder les deux couches fermées jusqu'aux résultats de l'étape 2. Faire inscrire dans son préenregistrement une mesure de ce que le catalogue manque, et fixer une date de réexamen.
    Avantage : aucune dépense ni risque de réécriture, et l'étape 2 devient informative.
    Inconvénient : si l'étape 2 glisse, la question reste ouverte.
  - **(b)** Faire (a), plus un essai de la vérification formelle sur processeur : Lean contre une suite bon marché (tests, mutations, relecture par un modèle d'une autre famille), sur une banque d'erreurs plantées.
    Avantage : indépendant de l'étape 2 et peu coûteux.
    Inconvénient : appels de sous-agents non chiffrés (devis nécessaire) ; conclusion bornée à la banque ; l'accord des quatre sur ce comparateur est « trop propre ».
  - **(c)** Rouvrir la couche 3 maintenant.
    Avantage : teste tôt la capacité non couverte.
    Inconvénient : risques nommés (une vérification faite dans le même bac à sable est circulaire, Avalon p. 76 ; violation possible de N-053) ; dépend de toute façon de l'oracle de l'étape 2 ; aucune espèce ne la propose.
- **Recommandation** : (a), et confirmer que N-053 interdit l'usage, pour un entraînement, de fiches filtrées par un moniteur. Confiance 0,65. L'option (b) est à reprendre sur devis, pas maintenant. Ma recommandation rejoint celle de l'annexe de conv-audit, en y ajoutant la mesure du résidu et la date de réexamen.

### N13 — tester ou non une récompense collective

Rappel : avec une récompense collective, la récompense d'un agent dépend de la performance de l'ensemble. C'est la méthode d'Avalon-M1 (General Reasoning, appelée « RLCR » pour récompenses collectives), à ne pas confondre avec la récompense de calibration de Damani et collègues, qui porte le même sigle.

- **Décision** : introduire ou non un essai de récompense collective, sous l'une des trois formes de la question :
  - (c1) un bras de l'étape 2 ;
  - (c2) un bras de la course 2 ;
  - (c3) un objet d'étude pour nos sondes ;
  - ou bien commencer par des mesures sans entraînement.
- **Enjeu** :
  - Avalon montre une chute du signalement aux humains, mais un seul run et aucun témoin mono-agent ne permettent d'en attribuer la cause au caractère collectif. La lecture vérifiée juge aussi que l'omission d'Avalon n'est diffuse qu'en partie (un point de décision par scénario), ce qui affaiblit (c3).
  - Les quatre écartent (c2) (pas d'oracle pour les fusions) et (c3) seule (pas de contrefactuel).
  - Une comparaison à deux bras, collectif contre individuel, ne sépare pas « collectif » de « tout entraînement qui ne récompense pas le signalement ». Trois espèces ajoutent un troisième bras.
  - Les coûts proposés vont de quelques heures d'inférence à des milliers d'heures de carte graphique, tous « illustratifs ».
- **Options** :
  - **(a)** Commencer par deux mesures sans entraînement. D'abord, le taux de signalement du modèle de départ : s'il est nul ou plein, aucun essai ne peut mesurer une chute. Ensuite, un audit de calibration des juges existants (score de Brier, erreur de calibration, aire sous la courbe de discrimination) sur des données déjà produites.
    Avantage : dépense nulle ou faible, et ces mesures conditionnent toute dépense.
    Inconvénient : ne tranche pas la question causale ; Damani ne prouve pas l'efficacité d'une recalibration bon marché.
  - **(b)** Faire (a), puis (c1) dans l'étape 2, sur préenregistrement et devis, avec un bras témoin non entraîné ou mono-agent. Le signalement serait mesuré dans tous les bras, n'entrerait dans aucune récompense, et serait évalué sur des scénarios tenus hors de l'entraînement. Un plancher de signalement et une chute maximale seraient gelés comme règle d'arrêt, et quelqu'un serait désigné pour lire ces mesures (aucune espèce ne le nomme).
    Avantage : c'est le seul contrefactuel propre.
    Inconvénient : l'étape 2 n'est pas conçue ; la dépense est importante ; on ne sait pas si l'essai crée assez de pression pour faire apparaître l'effet (divergence n° 3).
  - **(c)** Ne rien introduire, et réexaminer à la publication des poids et des environnements d'Avalon, ou après lecture d'Agrawal et collègues (PDF non versé).
    Avantage : n'importe aucun défaut.
    Inconvénient : la question reste ouverte et dépend d'un tiers.
- **Recommandation** : (a) maintenant, puis (b) seulement après le dessin de l'étape 2 et un devis. Confiance 0,6. Cela diffère de l'annexe de conv-audit, qui passait directement à (c1) à deux bras : je mets les mesures sans entraînement d'abord et j'exige le troisième bras. L'accord entre l'annexe et le collisionneur sur (c1) est sous effet d'ordre.
