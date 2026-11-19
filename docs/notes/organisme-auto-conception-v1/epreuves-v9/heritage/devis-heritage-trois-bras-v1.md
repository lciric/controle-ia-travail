# Question de l'héritage (N-073, § 1) — devis du plan à trois bras, par ordre de grandeur — v1

- **Statut : pièce de travail, brouillon 1, à contre-lire.** Ce devis ne demande aucun accord. Il chiffre l'étage payant du plan `plan-heritage-trois-bras-corrige-v1.md` (même dossier) pour que la taille de la question soit connue avant qu'on y travaille. Un devis qui fonde une ligne d'accord sera une version neuve, écrite après l'étage sur processeur.
- **Écrit par** : le rédacteur (modèle F), le 2026-11-19 vers 13:10Z (`date -u`), processeur seul, aucun appel, aucune dépense. Mandat : `GO-2026-11-19-55`.
- **Calcul** : `calcul_devis_heritage_v1.py`, sortie `calcul-devis-heritage-v1.json` (même dossier, empreintes compagnes). Tout chiffre ci-dessous en vient, arrondi.
- **Source des coûts** : manifeste de fin du lanceur de la course d'auto-conception v9, `runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json` (branche `lot/compte-organisme-v1`, sha256 `28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7`), champs `cout_reel.par_role_usd` et `cout_reel.appels_par_role`. La course entière a coûté 72,50 USD, soit 1,8 fois son devis.

## 0. Verdict

1. **Étage sur processeur : 0 USD d'appels.** Il précède tout le reste.
2. **Étage payant : de l'ordre de 1 600 à 10 600 USD en estimation**, selon la composition des proposeurs ; de 2 700 à 17 600 USD en cas haut ; de 4 300 à 28 100 USD au pire. C'est de plusieurs fois à plusieurs dizaines de fois ce que la proposition annonçait (de 150 à 350 USD). La raison tient en une ligne : le plancher de dix sources (correction 3 du plan).
3. **Ce devis est un plancher sur deux points non chiffrables aujourd'hui** : l'épreuve programmée des tentatives n'a jamais été jouée sur le lanceur réel, et la boucle où une génération lit un registre n'est pas fermée (§ 6).

## 1. Coûts réels de la course v9, par rôle

| rôle | appels | coût réel (USD) | par appel (USD) |
|---|---|---|---|
| proposeur de l'espèce Opus | 11 | 7,43 | 0,68 |
| proposeur de l'espèce Fable | 11 | 17,58 | 1,60 |
| proposeur de l'espèce Argon | 11 | 4,17 | 0,38 |
| proposeur de l'espèce Astra | 11 | 4,75 | 0,43 |
| proposeur de l'espèce Carbon | 11 | 24,72 | 2,25 |
| **étape de proposition** | **55** | **58,64** | — |
| aiguilleur | 96 | 4,59 | 0,048 |
| juge de l'espèce Opus | 94 | 6,86 | 0,073 |
| juge de l'espèce Argon | 94 | 2,41 | 0,026 |
| **course entière** | — | **72,50** | — |

Ces coûts sont ceux d'une course dont les cartes proposent des mécanismes pour l'organisme. Une course sur monde planté, où les tentatives sont des lois, peut avoir des invites et des réponses d'une autre longueur : l'unité ci-dessous est un ordre de grandeur, pas une mesure.

## 2. L'unité : une génération d'un bras

Le plan fixe un budget en dollars égal par bras. Le bras qui lit un registre paie sa lecture sur ce budget et reçoit moins d'appels : **le registre n'ajoute donc aucune ligne au devis**. L'unité est le coût d'une génération de propositions, pour une composition donnée, à onze appels par espèce comme à la v9.

| composition des proposeurs | appels | coût d'une génération d'un bras (USD) |
|---|---|---|
| A — les cinq espèces de la v9 | 55 | 58,64 |
| B — trois espèces, sans les deux plus chères (Opus, Argon, Astra) | 33 | 16,35 |
| C — les deux espèces les moins chères (Argon, Astra) | 22 | 8,92 |

Ce devis ne choisit pas la composition : elle se juge sur l'oracle du monde planté et le coût (N-058), et tout changement de modèle demande un accord. Les trois lignes ne servent qu'à borner.

## 3. Le compte des générations de bras

| poste | minimal | estimation | haut et pire |
|---|---|---|---|
| sources à dose non nulle | 10 | 10 | 12 |
| sources à dose nulle (bras 2 et 3 seulement) | 0 | 6 | 10 |
| générations par continuation | 3 | 3 | 3 |
| générations de la course source | 1 | 3 | 3 |
| continuations du critère (3 bras × sources × générations) | 90 | 90 | 108 |
| continuations à dose nulle (2 bras × sources × générations) | 0 | 36 | 60 |
| courses sources (une par source) | 10 | 48 | 66 |
| pilote de bruit (deux courses du même bras) | 6 | 6 | 6 |
| **total, en générations de bras** | **106** | **180** | **240** |

- *Minimal* : le plancher de dix sources, la dose nulle jouée sur processeur seulement, une course source d'une génération. La règle de validité à dose nulle n'y est pas appliquée à de vrais proposeurs : c'est une faiblesse, dite ici.
- *Estimation* : dix sources, six à dose nulle (le plus petit nombre où la règle de validité peut se déclencher), course source de trois générations.
- *Haut* : douze sources (réserve pour les différences nulles), dix à dose nulle, et coût de l'unité relevé d'un quart.
- *Pire* : les nombres du cas haut, coût de l'unité doublé (la v9 a coûté 1,8 fois son devis). Un plafond d'arrêt gelé au préenregistrement borne la dépense en tout état de cause.

## 4. Totaux de l'étage payant (USD, arrondis à la dizaine)

Sans aiguilleur ni juges à modèle : la mesure du plan se fait par l'oracle, par programme.

| composition | minimal | estimation | haut | pire |
|---|---|---|---|---|
| A — cinq espèces | 6 220 | 10 560 | 17 590 | 28 150 |
| B — trois espèces | 1 730 | 2 940 | 4 900 | 7 850 |
| C — deux espèces | 950 | 1 610 | 2 680 | 4 280 |

Option : garder l'aiguilleur et les deux juges à modèle pour information (volet des témoins jugés de l'oracle de N-058). À la proportion de cartes de la v9, cela ajoute par génération d'un bras 13,86 USD (composition A), 8,31 USD (B) ou 5,54 USD (C).

| composition, avec aiguilleur et juges | minimal | estimation | haut | pire |
|---|---|---|---|---|
| A — cinq espèces | 7 690 | 13 050 | 21 750 | 34 800 |
| B — trois espèces | 2 610 | 4 440 | 7 400 | 11 840 |
| C — deux espèces | 1 530 | 2 600 | 4 340 | 6 940 |

**Bras de diagnostic** (plan, § 9), sur devis à part : un bras, dix sources, trois générations coûte environ 1 760 USD (A), 490 USD (B) ou 270 USD (C). Six bras sont décrits ; tous se jouent d'abord sur processeur.

## 5. Étage sur processeur : 0 USD

Générateur des mondes à dose plantée, exécuteur simulé, quatre proposeurs scriptés, procédure d'analyse entière, six bras de diagnostic : aucun appel de modèle. Coût : un préenregistrement par le modèle F, sa contre-lecture par le modèle O, le code et ses essais, du temps de machine sur processeur. Aucune instance payante.

Ce que cet étage rapporte au devis : le nombre de sources à dose nulle, la dose non nulle à retenir, la part de différences nulles (donc dix ou douze sources), et la puissance de la procédure à ces tailles. **Le devis de l'étage payant se réécrit après lui.**

## 6. Ce qui n'est pas chiffré

1. **L'épreuve programmée des tentatives sur le lanceur réel.** La course v9 n'a joué ni épreuve des lois ni pari ; la proposition (§ 6, écart 5) dit que cet étage n'est pas branché. Si la traduction d'une tentative en programme demande un appel de modèle, c'est une ligne de plus par tentative, sans coût réel connu.
2. **La fermeture de la boucle** : aucune génération ne lit aujourd'hui un registre. Le travail est du code sur processeur, mais il précède tout.
3. **L'audit du registre par un lecteur d'une autre lignée**, que le plan d'origine proposait à chaque génération : un appel par génération de bras qui tient un registre ; non chiffré, petit devant l'unité.
4. **La longueur réelle des appels sur monde planté** (§ 1).
5. **Les appels sans sortie exploitable** : à la v9, jusqu'à 3 appels sur 11 pour une espèce. Ils sont payés ; le cas haut les couvre par son quart de marge, sans garantie.
6. Les préenregistrements, contre-lectures et verdicts sont faits par des sous-agents de la session et n'entrent pas dans ces lignes.

## 7. Rapport aux ordres de grandeur déjà écrits

- La vérification courte des versions 2 (R-3643) donnait « environ 4 000 USD pour trois bras, dix sources et trois générations », sur une unité d'environ 45 USD par génération pour l'étape de proposition. À l'unité réelle de 58,64 USD, les seules continuations du critère coûtent 90 × 58,64 = 5 280 USD ; les courses sources, la dose nulle et le pilote doublent ce nombre.
- La proposition (§ 4) donnait « entre 150 et 350 USD selon les espèces ». Ce chiffre est celui des cartes : une transition de génération, quelques mondes, quelques graines, sans plancher de sources. Il ne survit pas à la correction 3.

## 8. Ce qui réduit le coût, et ce que cela coûte

| levier | effet sur le total | prix |
|---|---|---|
| composition B ou C au lieu de A | divisé par 3,6 ou par 6,6 | la réponse ne vaut que pour ces espèces ; nœud (N-058, changement de modèle) |
| un seul contraste décisif (l'héritage) au lieu de deux | plancher technique de six sources au lieu de dix | six signes égaux exigés ; la tenue devient descriptive (plan, § 12, point 3) |
| dose nulle sur processeur seulement | moins 36 générations de bras en estimation | la règle de validité n'est pas appliquée à de vrais proposeurs |
| course source d'une génération | moins 32 générations de bras en estimation | un registre hérité mince, donc un effet attendu plus petit |
| moins de onze appels par espèce | proportionnel | moins de tentatives par génération, scores plus discrets, plus de différences nulles |

Aucun de ces leviers n'est retenu ici : ce sont des choix à faire au préenregistrement de l'étage payant, après l'étage sur processeur.

## 9. Décision pour Lazar — rien n'est demandé aujourd'hui

**Décision.** Aucune dépense n'est proposée. La question posée est de principe : l'étage sur processeur de l'héritage part-il maintenant, sachant que l'étage payant qui le suivrait se compte en milliers de dollars ?

**Enjeu.** Le plan répond à la question de N-073, § 1, sous la lettre du complément 3. Sa taille vient du plancher de dix sources et non d'un choix de confort.

**Options.**
- **(a) Étage sur processeur d'abord, à 0 USD, puis devis neuf.** Avantage : on saura si l'instrument peut répondre, et à quelle taille, avant de parler d'argent. Inconvénient : une pièce de plus dans un chantier chargé, pour une suite payante qui peut être refusée.
- **(b) Attendre** que les cinq lignes de l'option (a) de la proposition aient rendu leur étage sur processeur. Avantage : charge moindre. Inconvénient : la question nommée la première par le mandat n'avance pas.
- **(c) Trancher d'abord les quatre nœuds du plan (§ 12)**, puis (a). Avantage : l'étage sur processeur se construit sur un objet fixé. Inconvénient : quatre décisions avant tout résultat ; le point 7 de l'étage sur processeur éclaire justement le premier nœud.

**Recommandation du rédacteur.** (a), confiance 0,6 : l'étage sur processeur ne coûte aucun appel et peut à lui seul dire que le plan n'a pas la puissance de répondre, ce qui éviterait toute la suite. La contre-lecture de ces deux pièces vient avant, quoi qu'il en soit.

**Défaut.** Aucun : toute dépense est un nœud.
