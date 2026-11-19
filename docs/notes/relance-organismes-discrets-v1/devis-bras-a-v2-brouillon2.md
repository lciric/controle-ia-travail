# Organismes discrets, bras A (déplacement des contrôles appris sans consigne) — devis de la course sur carte louée — v2, BROUILLON 2

- **Date (UTC)** : 2026-11-18T18:10:53Z (`date -u`). Commit du dépôt lu : `d9c0c8adf1fcb6dc1416e9bd2a00e8eeedee7500`.
- **Objet** : chiffrer la course du bras A telle que le texte scellé et ses deux addenda la lisent. Ce devis remplace, pour le bras A, le devis v1, qui chiffrait une conception abandonnée (huit actions candidates par pas et une clé de sélection).
- **Statut** : brouillon 2, corrigé après contre-lecture du brouillon 1 (section 11). Il n'engage rien et n'ouvre aucune dépense. Une ligne de calcul reste un nœud de Lazar.
- **Brouillon 1** : `docs/notes/relance-organismes-discrets-v1/devis-bras-a-v2-brouillon1.md`, `a153e310e314946e32a0fe460bd5d2c4f0b9af2d98dec9e126e3180a7804307f`, gardé tel quel (R12).
- **Sceau** : ce brouillon n'a pas de fichier compagnon d'empreinte (consigne : un seul fichier écrit). À sceller par la session qui le reprend (R6).

## 0. Pièces qui font foi, avec empreintes (sha256)

| pièce | empreinte |
|---|---|
| `prereg/T0.7-organismes-discrets-v-a-v1.md` (texte scellé) | `06ab6a2f6e173bb1258f45ffeded7a419b05ecc2f59920666cea91aafcc7cf05` |
| `prereg/T0.7-organismes-discrets-v-a-v1-addendum-lecture-lot-de-huit-v1.md` (premier addendum, scellé) | `bd6ae8dfdfcda18a9c7118ede4f1542fae71063521c442093f778a1cd4b0e4f3` |
| `prereg/T0.7-organismes-discrets-v-a-v1-addendum-2-pas-de-distillation-v1.md` (second addendum, scellé) | `4f9af3c5cfb3725eab81d1507dc2c116845d26b492a5fb07e7370a17f7439352` |
| `docs/notes/organismes-discrets-v1/conception-organismes-discrets-v2.md` | `43a356ab7f8924faca17bb6024bbab8db778e3ce0b8a4b368ace1b78341f9b0c` |
| `prereg/T0.6-organismes-config-7b-v1.json` (configuration de référence) | `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527` |
| `docs/notes/organismes-discrets-v1/devis-organismes-discrets-v1.md` (ancien devis, pour la méthode) | `c376f2ea2e6a60849dc67e1563b45608a63454bd3fd3ba38202048354ea6b64c` |
| `docs/notes/relance-organismes-discrets-v1/carte-branchement-bras-a-v1.md` | `0f26006d9eeaef7b1f7f84b96de50078350aa2e4cf177b6ed07cd21a12286190` |
| `prereg/T0.6-organismes-v0-v1.md` (texte scellé de l'organisme précédent, lu pour sa seule section « Devis », lignes 635 à 702) | `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169` |

Registres vivants cités par ligne, au commit ci-dessus, sans empreinte (ils ne sont pas scellés) : `registres/depenses.md`, `registres/decisions.md`. Lu aussi, pour la règle de prix : l'en-tête de `scripts/lancer_t06_v13.sh` (lignes 1 à 12).

## 1. Le témoin bénin (vi-B) : deux lectures, rien n'est tranché

Le témoin (vi-B) est l'adaptateur distillé sur des transcriptions où le champ `PREDICTION` est permuté, « même proportion, même machinerie » (texte scellé, ligne 53 ; conception, ligne 56). Le texte ne dit pas si « même proportion » veut dire une seule proportion ou une par dose. Le second addendum dit que chaque adaptateur, « ceux des doses et les témoins (vi-T) et (vi-B) », reçoit 384 pas, et écrit : « Cet addendum ne fixe pas le nombre d'adaptateurs » (ligne 26). La configuration de référence porte `doses_temoin` = [1.0] (lignes 81 à 83), mais cette clé n'est pas parmi celles que le texte scellé emprunte (ligne 17). **Rien n'est tranché par Lazar.** Les deux lectures sont chiffrées côte à côte :

- **Lecture courte** : (vi-B) à une seule proportion. 4 doses + (vi-T) + (vi-B) = **6 adaptateurs** ; **7 conditions** au rejeu.
- **Lecture longue** : (vi-B) à chaque dose non nulle. 4 + 1 + 4 = **9 adaptateurs** ; **10 conditions** au rejeu.

Trois points attachés :

- **(a) En lecture courte, la proportion n'est pas dite par le texte.** Elle est à fixer avant la fabrication. Sans effet sur le coût.
- **(b) En lecture longue, le critère de lecture 8 devient quatre tests.** Le texte scellé (ligne 215) écrit un seul test du témoin bénin, sans règle de multiplicité pour quatre. La lecture longue demande donc un addendum.
- **(c) Aucun adaptateur de dose 0.** Distillé sans permutation, il serait le témoin (vi-T) à l'identique. Le contrôle d'identité à dose nulle (M-4, texte scellé, ligne 180) ne peut alors viser que l'échelle 0 de chaque adaptateur chargé. C'est ce que ce devis chiffre. **Lecture à confirmer par Lazar.**

**Sous-échantillon du juge d'une autre lignée (lecteur 6).** Il compte 2 560 actions, « stratifié par tâche et par condition » (ligne 147). Le texte ne dit pas quelles conditions entrent dans la stratification. Sans effet sur la carte ; à fixer avant le tirage.

## 2. Débits et durées réels de la chaîne réemployée, sur la même carte

Des mesures existent au dépôt. Aucune ne vient du bras A. Toutes viennent de la chaîne de l'organisme précédent (T0.6), même modèle, même carte (A100 SXM4 80 Go), mêmes réglages (10 pas, lot de 8 épisodes, 400 jetons).

| grandeur | valeur | source |
|---|---|---|
| durée d'un épisode, en lots de 8 (course P3) | **40,2 s** (240 épisodes en 9 644,6 s) | `prereg/T0.6-organismes-v0-v1.md`, ligne 643 |
| durée d'un épisode à la course exploratoire de dose-réponse (7a) | **42,8 s** (576 épisodes en 6,85 h ; division faite ici) | même fichier, ligne 698 |
| jetons par action et par épisode | contexte 2 643, action 223 ; transcription finale 4 319 jetons par épisode | même fichier, ligne 645 |
| passe unique d'activations sur texte imposé | 0,45 s par épisode | même fichier, ligne 644 |
| distillation, génération de ses données comprise (7a) | 4,36 h pour 320 épisodes et 2 adaptateurs | même fichier, ligne 698 |
| suite d'essais figée sur la machine (7a) | 0,58 h ; instance 13,59 h pour 12,97 h de course | même fichier, ligne 698 |
| mémoire de la carte | pic de 26,0 Gio aux épisodes ; carte presque pleine (≈ 82,7 Go occupés ou réservés) et un échec d'allocation sans arrêt au début d'un entraînement d'adaptateur | même fichier, ligne 702 |
| course de confirmation 7b entière | **14,97 h, 18,16 USD** (soit 1,213 USD par heure tout compris) | `registres/depenses.md`, ligne 421 ; `registres/decisions.md`, ligne 2371 (R-2413) |
| débit brut ancien (validation de T0.4, mode déterministe, simple précision) | 25,5 jetons par seconde en lot de 8 | `registres/decisions.md`, ligne 133 |

**Pourquoi cette carte.** L'A100 SXM4 80 Go est la seule où ces débits sont mesurés. La distillation sur transcription entière y a rempli la mémoire (≈ 82,7 Go, ligne 702). Une carte moins chère serait un nœud et exigerait un relevé neuf du débit et de la mémoire.

**Hypothèses de ce devis, non mesurées.**

- **Durée d'un pas de distillation : 3,0 s.** Aucun registre ne la donne. Je la déduis de 7a : 4,36 h moins la génération de 320 épisodes (3,57 h à 40,2 s ; 3,81 h à 42,8 s) laisse 0,56 à 0,79 h pour 2 adaptateurs × 480 pas = 960 pas, soit 2,1 à 3,0 s par pas. 3,0 s est **la valeur haute de la fourchette dérivée**, pas un majorant strict. Sensibilité : + 1 s par pas = + 0,64 h en lecture courte, + 0,96 h en lecture longue ; c'est couvert par le facteur 2 du pire cas.
- **Mise en route : 1,0 h** (location, image, clonage, téléchargement du modèle, essais figés ; 7a : 0,58 h d'essais et 0,62 h d'écart entre instance et course).
- **Contrôle d'identité : 3 minutes par adaptateur**, empreinte du modèle de base avant et après chaque réglage comprise (texte scellé, ligne 237).
- **Débit des épisodes : 42,8 s.** Les épisodes mesurés n'étaient pas des épisodes honnêtes sans adaptateur et portaient une capture partielle d'activations. Le bras A peut différer.

## 3. Inventaire de ce qui tourne sur la carte

| | poste | compte et formule | lecture courte | lecture longue |
|---|---|---|---|---|
| (a) | **Passe de fabrication** : épisodes honnêtes du modèle de base sur les 16 tâches de fabrication (premier addendum, section 5 ; conception, section 1.1, point 2) | 16 tâches × 8 épisodes = 128 épisodes ; × 10 pas = 1 280 actions | 128 × 42,8 s = **1,52 h** | **1,52 h** |
| (b) | **Fabrication par programme** : dérangement des champs `CONTROLS` (quatre doses), identité pour (vi-T), dérangement de `PREDICTION` pour (vi-B) | sur processeur, aucun appel de modèle (conception, ligne 35) | **0 h de carte** hors de la machine ; quelques secondes sinon | idem |
| (c) | **Distillation** : un adaptateur de rang 16 par dose non nulle, plus (vi-T), plus (vi-B) ; 128 transcriptions × 3 époques, lot 1 = **384 pas** par adaptateur (second addendum) ; une transcription ≈ 4 319 jetons | adaptateurs × 384 pas × 3,0 s | 6 × 384 = 2 304 pas = **1,92 h** | 9 × 384 = 3 456 pas = **2,88 h** |
| (d) | **Rejeu sur les 16 tâches de vérification** : honnête H (c'est la dose 0, modèle de base sans adaptateur), chaque dose, témoins ; mêmes graines d'action | conditions × 128 épisodes × 10 pas (texte scellé, ligne 161) | 7 × 128 = 896 épisodes, 8 960 actions = **10,65 h** | 10 × 128 = 1 280 épisodes, 12 800 actions = **15,22 h** |
| (e) | **Contrôle d'identité à l'échelle 0 de chaque adaptateur, son artefact à dose 1, empreintes de la base** (M-4) | adaptateurs × 3 minutes | **0,30 h** | **0,45 h** |
| (f) | **Mise en route** | une fois | **1,0 h** | **1,0 h** |
| | **Total retenu** (42,8 s ; 3,0 s) | | **≈ 15,4 h** | **≈ 21,1 h** |
| | Bas de fourchette (40,2 s ; 2,1 s) | | ≈ 14,1 h | ≈ 19,2 h |

**Ce qui ne coûte pas de carte dans cet inventaire.**
- Contrôles de manipulation M-1 (moitiés échangeables), M-2 (la couverture baisse à dose 1), M-3 (invariance du nombre de jetons et du multiensemble des contrôles) : calculs sur processeur. M-1 et M-2 exigent les lectures de l'oracle de couverture (section 4).
- Épreuves de l'oracle sur 32 épisodes honnêtes (2 par tâche) : je suppose qu'ils sont tirés parmi les épisodes honnêtes déjà joués des tâches de vérification. Le texte scellé (ligne 190) ne dit pas de quelles tâches. Une génération à part coûterait 32 × 42,8 s = 0,38 h.
- Estimation de l'écart-type et de l'effet minimal détectable, lecteurs 1, 2 et 5, agrégateur du lecteur 4, tests, intervalles, planchers : processeur. À faire tourner **hors de la machine louée**, sinon la carte est payée à vide.

**États internes au rejeu : non enregistrés, selon le texte.** Le texte scellé ne demande aucun enregistrement d'activations. Il interdit d'en lire (lignes 224 et 254). Le lanceur du bras A ne doit importer aucun module de lecture interne (carte du branchement, lignes 45 à 47). **Je chiffre sans enregistrement.** Si une lecture interne est décidée plus tard, les activations se recalculent par une passe sur texte imposé : 0,45 s par épisode, soit ≈ 0,11 à 0,16 h pour 896 à 1 280 épisodes, avec chaque adaptateur rechargé. **Condition** : les adaptateurs et les identifiants générés doivent être rapatriés et scellés ; sinon cette passe est impossible. Tout enregistrer au rejeu ferait, **par hypothèse** (3 couches, 4 096 dimensions, demi-précision, 4 319 jetons), ≈ 106 Mo par épisode, soit ≈ 95 à 136 Go, au bord du disque minimal de 150 Go de la configuration (ligne 112).

**Disque et trafic sans activations.** Modèle ≈ 16 Go, image et dépôt ≈ 4 Go ; adaptateurs 6 à 9 × ≈ 27 Mo ; épisodes en texte et identifiants : moins de 1 Go. Montée attendue : moins de 2 Go.

## 4. Ce qui ne tourne pas sur la carte et coûte ailleurs

Le texte scellé ne nomme aucun modèle (règle d'anonymisation, ligne 16). Il ne dit pas si ces lecteurs sont des appels payants ou des modèles ouverts sur carte. **Aucun tarif n'est relevé : en dollars, le poste n'est pas chiffrable en l'état.** Je donne les comptes, les volumes, puis une fourchette conditionnelle.

| poste | compte et formule | jetons d'entrée, ordre de grandeur |
|---|---|---|
| **Oracle de couverture** : deux lecteurs hors des familles des moniteurs, un plan entier par lecture | au moins 5 doses + (vi-B) (critère de lecture 8) = 6 conditions × 128 épisodes × 2 lecteurs = **1 536 lectures** ; avec (vi-T) : 1 792 ; lecture longue : 2 560. Doublé si les moitiés D et V se lisent en deux appels (non dit) | 7 à 11 millions, plus la référence ; sortie ≈ 300 jetons par lecture (hypothèse de l'ancien devis, ligne 24) |
| **Cinq épreuves de l'oracle** sur 32 épisodes honnêtes | 4 épreuves × 32 + 1 × 8 = 136 plans × 2 lecteurs ≈ **272 lectures** au moins | ≈ 1,2 million |
| **Ancre humaine** (épreuve 5) | 8 jugements écrits d'avance | temps de rédaction, 0 USD de calcul |
| **Moniteur boîte noire par action en contexte** (lecteur 3) | 5 doses × 1 280 actions = **6 400 lectures** au moins ; 8 960 à 12 800 si les témoins sont lus | ≈ 18 millions (2 866 par lecture) ; ≈ 37 millions à 12 800 |
| **Agrégateur séquentiel** (lecteur 4) | réemploie les scores du lecteur 3 | 0 |
| **Juge d'une autre lignée** (lecteur 6) | **2 560 lectures** (ligne 147) | ≈ 7 millions |
| Lecteurs 1, 2 et 5, test à deux échantillons, intervalles, planchers | processeur | 0 |

**Fourchette conditionnelle, sans tarif relevé.** Total d'entrée : **au moins 33 à 37 millions de jetons** ; **environ 56 millions** si les témoins sont lus partout. À 1 USD par million : ≈ 33 à 56 USD. À 3 USD par million : ≈ 100 à 170 USD. **Ce poste peut dépasser la carte.**

**Conséquences.**
- La dépense de carte est **perdue** si les lectures ne sont pas payées ensuite. Le devis des lectures doit donc être **au moins borné avant le GO de la carte**.
- Si le moniteur par action tourne sur une carte, c'est **une ligne de carte en plus**, absente de ce devis.
- Ces lectures ne viennent qu'après l'étape (e) de l'ordre gelé (texte scellé, section 6.3) ; elles peuvent se payer après la course, mais pas se décider après.

## 5. Prix

| relevé | valeur | source |
|---|---|---|
| A100 SXM4 80 Go, dernier relevé au dépôt, le **2026-11-18T15:44:24Z** | **prix relu 1,1833 USD par heure** ; prix de l'offre 1,1843 stockage compris | `registres/depenses.md`, ligne 515 |
| mêmes cartes, du 13 au 16 novembre | 1,04 à 1,27 USD par heure | `registres/depenses.md`, lignes 440, 459, 466, 470, 476 |
| prix effectif de la course 7b, tout compris | 1,213 USD par heure (18,16 USD ÷ 14,97 h) | `registres/depenses.md`, ligne 421 |
| bornes de la configuration de référence | carte **1,30 USD par heure** ; stockage ≤ **0,08** USD par heure ; téléchargement ≤ 0,05 USD par Go, 40 Go prévus | `prereg/T0.6-organismes-config-7b-v1.json`, lignes 41, 115 à 117 |

**Règle de prix.** Le lanceur de référence compare la borne de 1,30 au prix de la carte seule, stockage retiré (`scripts/lancer_t06_v13.sh`, ligne 7 : prix de la carte = prix total − stockage). Le stockage, jusqu'à 0,08 USD par heure, s'ajoute. **Prix du devis proposé : 1,30 USD par heure pour la carte, 1,38 stockage compris.** Raison : la liste d'arrêt interdit de démarrer si le prix relevé dépasse le prix du devis (texte scellé, ligne 239) ; prendre le dernier prix relu bloquerait la course à la moindre hausse. La configuration neuve doit porter ces deux bornes.

**Téléchargement** : 20 à 40 Go à la borne de 0,05 USD par Go = **1 à 2 USD** par mise en route.

**À relever de nouveau avant la ligne de calcul** : prix de l'offre et prix relu le jour même ; stockage par heure ; téléchargement par Go ; pilote de l'hôte (un pilote trop ancien a déjà fait échouer une instance : `registres/depenses.md`, ligne 468).

## 6. Course d'un seul tenant : attendu, pire cas, plafond (carte seule)

| | lecture courte (6 adaptateurs, 7 conditions) | lecture longue (9 adaptateurs, 10 conditions) |
|---|---|---|
| heures de carte (bas de fourchette à retenu) | 14,1 à 15,4 h | 19,2 à 21,1 h |
| calcul au dernier prix relu (1,1833) | 16,7 à 18,2 USD | 22,7 à 24,9 USD |
| téléchargement | 1 à 2 USD | 1 à 2 USD |
| **attendu au dernier prix relu** | **≈ 18 à 20 USD** | **≈ 24 à 27 USD** |
| **attendu au prix du devis (1,30)** | **≈ 19 à 22 USD** | **≈ 26 à 29 USD** |

La contre-lecture donnait ≈ 20 à 22 et ≈ 27 à 29 USD au prix du devis ; l'écart d'un dollar en bas vient du bas de fourchette du débit, repris ici.

Contrôle de vraisemblance : la course 7b a joué 896 épisodes et 2 adaptateurs en 14,97 h pour 18,16 USD. La lecture courte joue 1 024 épisodes et 6 adaptateurs, sans le test croisé sur processeur de 7b (1,76 h). Même ordre.

**Pire cas**, trois facteurs cumulés : carte et stockage aux bornes (**1,38 USD par heure**) ; débit deux fois plus lent (× 2) ; une relance complète (× 2).

- Lecture courte : 15,4 h × 4 = 61,6 h × 1,38 = 85 USD, plus 4 USD de téléchargement : **pire cas ≈ 89 USD**.
- Lecture longue : 21,1 h × 4 = 84,3 h × 1,38 = 116 USD, plus 4 USD : **pire cas ≈ 120 USD**.

La contre-lecture donnait ≈ 87 et ≈ 118 USD sur les heures du brouillon 1 (15,0 et 20,6 h). Les totaux refaits (mise en route 1,0 h, contrôle d'identité 3 minutes par adaptateur) ajoutent 2 USD.

**Plafond proposé : 90 USD (lecture courte) ou 125 USD (lecture longue).** La contre-lecture proposait 120 USD pour la lecture longue ; au total refait, le pire cas l'atteint (120,3 USD), d'où 125. Au-delà d'une relance, toute relance nouvelle est un nœud. Autre voie : relever d'abord le débit (section 9, point 1) ; s'il confirme 40 à 45 s par épisode, plafond d'environ **50 USD** (courte) ou **65 USD** (longue).

## 7. Option en deux lignes, à côté de la course d'un seul tenant

**Ligne 1 — fabrication et rejeu honnête.** 128 épisodes de fabrication + 128 épisodes honnêtes de vérification = 256 épisodes, 3,04 h (2,86 h au bas de fourchette), plus la mise en route : **≈ 3,9 à 4,1 h**. Calcul 4,6 à 5,3 USD, téléchargement 1 à 2 USD : **≈ 5 à 7 USD** (5,6 à 7,3). Pire cas (× 4, 1,38) : ≈ 26 USD ; plafond proposé 27 USD.

Ce qu'elle permet : jouer, avant de dépenser le reste, les gardes qui ne lisent que des épisodes honnêtes — épreuves de l'oracle, échangeabilité des moitiés (M-1), effet minimal détectable, couverture de base (repli d'instrumentation, section 9.1 du texte scellé). Si l'une échoue, la ligne 2 n'est pas dépensée. Ces gardes demandent les lectures de l'oracle sur les épisodes honnêtes (section 4) : 256 lectures de plan et ≈ 272 lectures d'épreuves.

**Ligne 2 — distillation et rejeux des doses et des témoins.**

| | lecture courte | lecture longue |
|---|---|---|
| distillation | 1,92 h | 2,88 h |
| rejeu des doses et témoins | 6 × 128 = 768 épisodes = 9,13 h | 9 × 128 = 1 152 épisodes = 13,70 h |
| contrôle d'identité | 0,30 h | 0,45 h |
| sous-total | **≈ 11,4 h** | **≈ 17,0 h** |
| seconde mise en route | 1,0 h (≈ 1,2 à 1,4 USD) et 1 à 2 USD de téléchargement | idem |
| attendu de la ligne 2 (1,1833 à 1,30) | **≈ 16 à 18 USD** | **≈ 22 à 25 USD** |
| pire cas de la ligne 2 (× 4, 1,38, 4 USD de téléchargement) | ≈ 72 USD ; plafond 75 | ≈ 104 USD ; plafond 105 |

La contre-lecture donnait ≈ 12 h et ≈ 17,6 h pour la ligne 2 ; mes sous-totaux refaits sont 11,4 et 17,0 h hors mise en route, 12,4 et 18,0 h avec.

**Total des deux lignes** : lecture courte ≈ 16,4 h, **≈ 21 à 25 USD** ; lecture longue ≈ 22,1 h, **≈ 28 à 33 USD**. Surcoût sur la course d'un seul tenant : une mise en route, soit ≈ 2 à 3,5 USD. Plafonds cumulés : 102 USD (courte) ou 132 USD (longue), mais 27 USD seulement sont engagés tant que les gardes ne sont pas passées.

**Contraintes de l'option.** Les épisodes honnêtes et les transcriptions fabriquées de la ligne 1 doivent être rapatriés, scellés, puis remontés à la ligne 2. Les graines d'action du rejeu doivent rester les mêmes entre les deux lignes (appariement au jumeau honnête). **Le choix entre un seul tenant et deux lignes revient à Lazar.**

## 8. Ce que ce devis ne couvre pas

- **Les lectures par appels de modèles** (oracle de couverture, lecteur 3, lecteur 6) : section 4 ; devis à part, à borner avant le GO de la carte.
- **Le moniteur par action sur carte**, si c'est ce qui est retenu : ligne de carte à part.
- **Le repli par tirages honnêtes multiples** (texte scellé, section 9.2). Selon le message de la session mère, Lazar l'a demandé en parallèle (GO-2026-11-18-47, préenregistrement à part en rédaction chez la session mère). Je n'ai pas trouvé cette ligne dans `registres/` au commit lu. Un devis à part sera dû.
- **Le bras B de la conception** (coûts anti-ordonnés) : préenregistrement et devis distincts.
- **La lecture interne** (activations, sondes) : interdite ici ; toute passe d'activations est un devis à part, et suppose les adaptateurs et identifiants rapatriés et scellés.
- **Toute lecture sur les 64 tâches d'évaluation** : elles restent vierges.
- **Une carte de repli plus grosse** en cas d'erreur de mémoire à la distillation. Le bras A enchaîne 6 à 9 adaptateurs sur une carte que la chaîne précédente a remplie. Un repli serait un nœud et un autre prix.
- **Le disque d'une instance arrêtée et gardée** après la course : à 0,08 USD par heure au plus, 72 h coûteraient 5,8 USD au plus ; mieux vaut rapatrier et détruire.
- **La passe de relevé du débit**, si elle se fait à part (section 9, point 1).

## 9. À relever ou à éprouver avant de demander le GO

1. **Le débit réel du bras A** : secondes par épisode honnête en lot de 8, secondes par pas de distillation sur une transcription entière. Un lot de 8 épisodes et vingt pas suffisent. Environ 1 h de carte : ≈ 1,2 à 1,4 USD de calcul, plus 0,5 à 2 USD de téléchargement, soit **≈ 2 à 3,5 USD**, sur sa propre ligne. Le pas de distillation n'a jamais été mesuré seul.
2. **La part d'actions permutables sur le vrai tokeniseur**, hors ligne, sans dépense. Avec la coupe de la première version de la fabrication, presque toutes les actions seraient non permutables (carte du branchement, lignes 39 à 44). Si la part est faible, des épisodes restent honnêtes et la dose réelle baisse. Le coût ne change pas ; l'utilité de la dépense, si.
3. **La disponibilité et le prix d'une A100 SXM4 80 Go conforme** le jour du lancement (prix, stockage, téléchargement, pilote).
4. **La durée de la liste d'essais figée du bras A** sur la machine (elle n'existe pas encore ; carte du branchement, ligne 56).
5. **Une borne de dépense pour les lectures externes** : lecteurs nommés, sur carte ou par appels, tarif relevé et daté ; stratification du sous-échantillon de 2 560 actions.
6. **La configuration neuve** : celle de référence porte un calendrier clos (fin au 2026-11-17, lignes 32 à 35) et l'ancien numéro de GO. Le bras A exige sa configuration, ses bornes de prix (1,30 carte, 0,08 stockage) et son plafond.
7. **Où tournent les calculs sur processeur** (fabrication, contrôles, lecteurs 1, 2, 5) : hors de la machine louée, sinon ajouter leur durée.
8. **Le scellement de ce devis** et l'inscription de la ligne de GO.

## 10. Décisions qui reviennent à Lazar

Ce devis suppose, sans que ce soit décidé :

1. **Le prix du devis fixé à la borne** : 1,30 USD par heure pour la carte, 1,38 stockage compris, et non au dernier prix relu.
2. **Course d'un seul tenant ou en deux lignes** (sections 6 et 7).
3. **Les 32 épisodes des épreuves de l'oracle tirés parmi les épisodes honnêtes déjà joués des tâches de vérification**, sans génération à part.
4. **Aucun enregistrement d'états internes** au rejeu ; adaptateurs et identifiants rapatriés et scellés.
5. **La lecture du témoin bénin** : courte ou longue ; la proportion en lecture courte ; un addendum de multiplicité en lecture longue ; pas d'adaptateur de dose 0 et contrôle d'identité à l'échelle 0 de chaque adaptateur (section 1).
6. **Les lecteurs externes et leur budget** (section 4), à borner avant le GO de la carte.
7. **Le plafond** : d'emblée (90 ou 125 USD ; la contre-lecture disait 120 pour la lecture longue), ou relevé du débit d'abord (≈ 2 à 3,5 USD) puis ≈ 50 ou ≈ 65 USD.

## 11. Contre-lecture

Brouillon 1 (`a153e310…`) contre-lu par un agent neuf le 18 novembre 2026 (R2) : **« autorisable sous corrections »**, sources et arithmétique confirmées. Les treize corrections transmises par la session mère sont appliquées ici : règle de prix et stockage (1) ; second addendum scellé (2) ; fourchette conditionnelle des lectures (3) ; option en deux lignes (4) ; témoin bénin (5) ; téléchargement (6) ; attendu au prix du devis (7) ; passe de relevé (8) ; hypothèses et totaux refaits (9) ; motif de la carte (10) ; hors champ (11) ; décisions de Lazar (12) ; cette section (13). **Trois écarts aux chiffres de la contre-lecture**, dus aux totaux refaits qu'elle demandait, sont signalés là où ils tombent : pire cas 89 et 120 USD au lieu de 87 et 118 ; plafond de la lecture longue 125 au lieu de 120 ; heures de la ligne 2. **Ce brouillon 2 n'est pas contre-lu.**

## 12. Déclaration

Rédigé par un agent neuf, qui n'est auteur ni du texte scellé, ni de ses addenda, ni de la conception, ni du code ; même agent que le brouillon 1. Aucune machine lancée, aucun appel réseau, aucune dépense. Aucun fichier de résultat, de base, de sonde ni de moniteur n'a été ouvert ; aucun fichier sous `runs/` ni `diag/`. Hors des pièces de la section 0, seuls ont été lus, par recherche de lignes, `registres/depenses.md`, `registres/decisions.md`, `registres/etat.md`, `registres/go.md`, les lignes 635 à 702 de `prereg/T0.6-organismes-v0-v1.md` et l'en-tête de `scripts/lancer_t06_v13.sh`. Les durées citées sont des relevés de la chaîne de l'organisme précédent, non du bras A. La durée d'un pas de distillation, la mise en route, la durée du contrôle d'identité, la taille des activations et tout tarif de lecture externe sont des hypothèses, marquées comme telles.
