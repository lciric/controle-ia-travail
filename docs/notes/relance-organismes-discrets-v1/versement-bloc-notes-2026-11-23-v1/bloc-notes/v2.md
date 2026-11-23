# Organismes discrets, bras A (déplacement des contrôles appris sans consigne) — devis de la course sur carte louée — v2

- **Date (UTC)** : 2026-11-18T21:45:13Z (`date -u`). Commit du dépôt lu : `64eb0b053bf84a9b43ccb81a6b47cff02b3f45e8`.
- **Objet** : chiffrer la course du bras A telle que le texte scellé, ses deux addenda et les décisions de Lazar du 18 novembre la fixent. Ce devis remplace, pour le bras A, le devis v1, qui chiffrait une conception abandonnée (huit actions candidates par pas et une clé de sélection).
- **Statut** : version finale, non recontre-lue (section 11). Elle demande une ligne de calcul, la ligne 1 (section 10). Elle ne demande pas la ligne 2.
- **Versions antérieures, gardées telles quelles (R12)** : brouillon 1, `a153e310e314946e32a0fe460bd5d2c4f0b9af2d98dec9e126e3180a7804307f` ; brouillon 2, `28d81d7deddf3a0af79a71f1e2f6f96ffeb13fc3b34193eb11c5403420cd0a7e` (même dossier, `devis-bras-a-v2-brouillon1.md` et `-brouillon2.md`).
- **Sceau** : pas de fichier compagnon d'empreinte (consigne : un seul fichier écrit). À sceller par la session qui le reprend (R6).

## 0. Pièces qui font foi, avec empreintes (sha256, recalculées à 21:45Z)

| pièce | empreinte |
|---|---|
| `prereg/T0.7-organismes-discrets-v-a-v1.md` (texte scellé) | `06ab6a2f6e173bb1258f45ffeded7a419b05ecc2f59920666cea91aafcc7cf05` |
| `prereg/T0.7-organismes-discrets-v-a-v1-addendum-lecture-lot-de-huit-v1.md` (premier addendum, scellé) | `bd6ae8dfdfcda18a9c7118ede4f1542fae71063521c442093f778a1cd4b0e4f3` |
| `prereg/T0.7-organismes-discrets-v-a-v1-addendum-2-pas-de-distillation-v1.md` (second addendum, scellé et inscrit ; registre `registres/organismes-discrets-v-a-addenda-v2.md`) | `4f9af3c5cfb3725eab81d1507dc2c116845d26b492a5fb07e7370a17f7439352` |
| `docs/notes/organismes-discrets-v1/conception-organismes-discrets-v2.md` | `43a356ab7f8924faca17bb6024bbab8db778e3ce0b8a4b368ace1b78341f9b0c` |
| `prereg/T0.6-organismes-config-7b-v1.json` (configuration de référence) | `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527` |
| `docs/notes/organismes-discrets-v1/devis-organismes-discrets-v1.md` (ancien devis, pour la méthode) | `c376f2ea2e6a60849dc67e1563b45608a63454bd3fd3ba38202048354ea6b64c` |
| `docs/notes/relance-organismes-discrets-v1/carte-branchement-bras-a-v1.md` | `0f26006d9eeaef7b1f7f84b96de50078350aa2e4cf177b6ed07cd21a12286190` |
| `prereg/T0.6-organismes-v0-v1.md` (texte scellé de l'organisme précédent, lu pour sa seule section « Devis », lignes 635 à 702) | `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169` |

Registres vivants cités par ligne, au commit ci-dessus, sans empreinte : `registres/depenses.md`, `registres/decisions.md`, `registres/go.md`. Lu aussi, pour la règle de prix : l'en-tête de `scripts/lancer_t06_v13.sh`.

## 1. Décisions appliquées

Mot direct de Lazar dans la session de relance, 2026-11-18T20:55:49Z, verbatim « go autonomie 12h go recos go depenses toutes les sessions » (événement `48160f92-f015-45d2-8895-8bcee84827c0`) ; ligne GO-2026-11-18-53 (`registres/go.md`, ligne 417). Il accorde les recommandations de la relance. Elles m'ont été transmises par la session de relance ; je les applique telles quelles.

1. **Témoin bénin (vi-B) : une seule proportion, la dose la plus forte (1,0).** La lecture « une par dose » est abandonnée ; le critère de lecture qui nomme ce témoin (texte scellé, ligne 215) reste donc un seul test, sans règle de multiplicité à ajouter.
2. **Six adaptateurs** : les quatre doses non nulles (0,25 ; 0,50 ; 0,75 ; 1,00), le témoin identité (vi-T), le témoin bénin (vi-B). **Sept conditions au rejeu** : honnête, quatre doses, deux témoins.
3. **Pas d'adaptateur de dose 0.** Le contrôle d'identité à dose nulle (M-4, texte scellé, ligne 180) vise l'échelle 0 de chaque adaptateur chargé.
4. **Deux lignes de calcul.** La ligne 2 ne se demande qu'après la ligne 1.
5. **Lectures hors carte : devis à part**, écrit et borné avant la demande de la ligne 2.
6. **Les 32 épisodes des épreuves de l'oracle** sont tirés des épisodes honnêtes des tâches de vérification joués à la ligne 1. Aucune génération de plus.
7. **Aucun enregistrement d'états internes** dans ces deux lignes. Les adaptateurs et les identifiants générés sont rapatriés et scellés.

## 2. Débits et durées réels de la chaîne réemployée, sur la même carte

Aucune mesure ne vient du bras A. Toutes viennent de la chaîne de l'organisme précédent (T0.6) : même modèle, même carte (A100 SXM4 80 Go), mêmes réglages (10 pas, lot de 8 épisodes, 400 jetons).

| grandeur | valeur | source |
|---|---|---|
| durée d'un épisode, en lots de 8 (course P3) | **40,2 s** (240 épisodes en 9 644,6 s) | `prereg/T0.6-organismes-v0-v1.md`, ligne 643 |
| durée d'un épisode à la course exploratoire de dose-réponse (7a) | **42,8 s** (576 épisodes en 6,85 h ; division faite ici) | même fichier, ligne 698 |
| jetons par action et par épisode | contexte 2 643, action 223 ; transcription finale 4 319 jetons | même fichier, ligne 645 |
| passe unique d'activations sur texte imposé | 0,45 s par épisode | même fichier, ligne 644 |
| distillation, génération de ses données comprise (7a) | 4,36 h pour 320 épisodes et 2 adaptateurs | même fichier, ligne 698 |
| suite d'essais figée sur la machine (7a) | 0,58 h ; instance 13,59 h pour 12,97 h de course | même fichier, ligne 698 |
| mémoire de la carte | pic de 26,0 Gio aux épisodes ; ≈ 82,7 Go occupés ou réservés et un échec d'allocation sans arrêt au début d'un entraînement d'adaptateur | même fichier, ligne 702 |
| course de confirmation 7b entière | 14,97 h, 18,16 USD (1,213 USD par heure tout compris) | `registres/depenses.md`, ligne 421 ; `registres/decisions.md`, ligne 2371 (R-2413) |

**Pourquoi cette carte.** L'A100 SXM4 80 Go est la seule où ces débits sont mesurés, et la distillation sur transcription entière y a rempli la mémoire. Une carte moins chère serait un nœud et un relevé neuf.

**Hypothèses, non mesurées.**
- **Épisode : 42,8 s** retenus, 40,2 s en bas de fourchette. Les épisodes mesurés n'étaient pas des épisodes honnêtes sans adaptateur. La ligne 1 mesure ce débit.
- **Pas de distillation : 3,0 s.** Déduit de 7a par soustraction : 0,56 à 0,79 h pour 960 pas, soit 2,1 à 3,0 s. C'est la valeur haute de la fourchette dérivée, pas un majorant strict. + 1 s par pas = + 0,64 h. **La ligne 1 ne le mesure pas** : elle ne distille rien.
- **Mise en route : 1,0 h** par ligne. La session de machine louée du bras A (amorce, gardes de dépense, rapatriement) reste à écrire ; elle n'a aucune durée mesurée.
- **Contrôle d'identité : 3 minutes par adaptateur**, empreinte du modèle de base avant et après chaque réglage comprise (texte scellé, ligne 237).

**État du code** (fait transmis par la session de relance ; fichiers présents, non ouverts par moi) : `src/controle_ia/organismes_discrets/fabrication_v2.py` et `lanceur_bras_a_v1.py` existent et tournent de bout en bout sur un modèle jouet.

## 3. Prix

| relevé | valeur | source |
|---|---|---|
| A100 SXM4 80 Go, dernier relevé au dépôt, 2026-11-18T15:44:24Z | prix relu **1,1833 USD par heure** ; prix de l'offre 1,1843 stockage compris | `registres/depenses.md`, ligne 515 |
| mêmes cartes, du 13 au 16 novembre | 1,04 à 1,27 USD par heure | `registres/depenses.md`, lignes 440, 459, 466, 470, 476 |
| bornes de la configuration de référence | carte 1,30 USD par heure ; stockage ≤ 0,08 ; téléchargement ≤ 0,05 USD par Go, 40 Go prévus | `prereg/T0.6-organismes-config-7b-v1.json`, lignes 41, 115 à 117 |

**Prix du devis : 1,30 USD par heure pour la carte seule, stockage ≤ 0,08 en plus, soit 1,38 au plus.** Le lanceur de référence compare la borne au prix de la carte, stockage retiré (`scripts/lancer_t06_v13.sh`, ligne 7). La liste d'arrêt interdit de démarrer si le prix relevé dépasse le prix du devis (texte scellé, ligne 239). **Téléchargement** : 20 à 40 Go à la borne = 1 à 2 USD par mise en route. Le prix est à relever de nouveau le jour de chaque création, avec le pilote de l'hôte (échec déjà vu : `registres/depenses.md`, ligne 468).

## 4. Ligne 1 — fabrication et rejeu honnête

| poste | compte et formule | durée |
|---|---|---|
| épisodes honnêtes du modèle de base sur les 16 tâches de fabrication | 16 × 8 = 128 épisodes, 1 280 actions | 1,52 h |
| épisodes honnêtes sur les 16 tâches de vérification (condition honnête du rejeu, dose 0) | 16 × 8 = 128 épisodes, 1 280 actions | 1,52 h |
| mise en route | une fois | 1,0 h |
| **total** | 256 épisodes × 42,8 s = 3,04 h (2,86 h à 40,2 s) | **≈ 3,9 à 4,0 h** |

- **Attendu** : calcul 4,6 USD (3,86 h à 1,1833) à 5,3 USD (4,04 h à 1,30) ; téléchargement 1 à 2 USD : **≈ 6 à 7 USD**.
- **Pire cas** (1,38 USD par heure, débit deux fois plus lent, une relance complète) : 4,04 h × 4 = 16,2 h × 1,38 = 22,3 USD, plus 4 USD de téléchargement : **≈ 26 USD**.
- **Plafond demandé : 27 USD.** Le chiffre du brouillon 2 tient au calcul refait.

**Ce qu'elle rend.** (1) Le débit réel du bras A en secondes par épisode. (2) Les épisodes de fabrication, d'où se fabriquent par programme, sur processeur et hors de la machine, les transcriptions des six adaptateurs. (3) Les épisodes honnêtes de vérification, qui permettent les gardes ne lisant que de l'honnête : les cinq épreuves de l'oracle sur 32 épisodes, l'échangeabilité des moitiés (M-1), l'écart-type entre tâches et l'effet minimal détectable, la couverture de base (repli d'instrumentation, texte scellé, section 9.1). Si l'une échoue, la ligne 2 n'est pas dépensée. Ces gardes demandent des lectures de l'oracle (section 6).

## 5. Ligne 2 — distillation, contrôle d'identité, rejeu des six conditions non honnêtes

| poste | compte et formule | durée |
|---|---|---|
| distillation | 6 adaptateurs × 384 pas (128 transcriptions × 3 époques, lot 1 ; second addendum) = 2 304 pas × 3,0 s | 1,92 h |
| contrôle d'identité à l'échelle 0 de chaque adaptateur, artefact à dose 1, empreintes de la base | 6 × 3 minutes | 0,30 h |
| rejeu sur les 16 tâches de vérification, mêmes graines d'action qu'à la ligne 1 | 6 conditions × 128 = 768 épisodes, 7 680 actions, × 42,8 s | 9,13 h |
| mise en route | une fois | 1,0 h |
| **total** | bas de fourchette (40,2 s ; 2,1 s) : 11,2 h | **≈ 11,2 à 12,4 h** |

- **Attendu** : calcul 13,3 USD (11,2 h à 1,1833) à 16,1 USD (12,4 h à 1,30) ; téléchargement 1 à 2 USD : **≈ 14 à 18 USD**.
- **Plafond de repli, si rien n'est mesuré à la ligne 1** : 12,35 h × 4 × 1,38 = 68 USD, plus 4 USD : pire cas ≈ 72 USD, **plafond 75 USD**.
- **Plafond recalculé sur le débit mesuré.** Soit `d` les secondes par épisode mesurées à la ligne 1. Le pas de distillation reste non mesuré : il est doublé (6,0 s). Une relance complète est gardée.
  - Heures : `H2(d) = 1,0 + 0,30 + 768 × d / 3 600 + 2 304 × 6,0 / 3 600 = 5,14 + 0,2133 × d`.
  - Plafond : `P2(d) = 2 × 1,38 × H2(d) + 4`.
  - Pour `d` = 40 s : 13,7 h, **≈ 42 USD**. Pour `d` = 45 s : 14,7 h, **≈ 45 USD**. Valeur attendue du plafond : **≈ 42 à 45 USD**.

**Contraintes.** Les transcriptions fabriquées sont remontées sur la machine de la ligne 2 (moins de 1 Go). Les graines d'action restent celles de la ligne 1 (appariement au jumeau honnête). Les six adaptateurs (≈ 27 Mo chacun) et les identifiants générés sont rapatriés et scellés : sans eux, une passe d'activations ultérieure est impossible. Risque de mémoire à la distillation (section 2) : un repli sur une autre carte serait un nœud.

**Total des deux lignes** : **≈ 15,1 à 16,4 h, ≈ 20 à 25 USD attendus.** Plafonds : 27 + 75 = 102 USD sans mesure ; 27 + (42 à 45) = 69 à 72 USD avec.

## 6. Lectures hors carte — devis à part, à borner avant la demande de la ligne 2

Le texte scellé ne nomme aucun lecteur (règle d'anonymisation, ligne 16) et ne dit pas s'ils tournent sur carte ou par appels. **Aucun tarif n'est relevé : en dollars, le poste n'est pas chiffrable en l'état.**

| poste | compte et formule | jetons d'entrée, ordre de grandeur |
|---|---|---|
| oracle de couverture, deux lecteurs hors des familles des moniteurs, un plan entier par lecture | 7 conditions × 128 épisodes × 2 = **1 792 lectures** (1 536 sans le témoin identité) ; dont 256 dès la ligne 1 ; doublé si les moitiés D et V se lisent en deux appels (non dit) | ≈ 7 à 8 millions, plus la référence |
| cinq épreuves de l'oracle sur 32 épisodes honnêtes | 4 × 32 + 8 = 136 plans × 2 ≈ **272 lectures** au moins, dès la ligne 1 | ≈ 1,2 million |
| ancre humaine (épreuve 5) | 8 jugements écrits d'avance | 0 USD de calcul |
| moniteur boîte noire par action en contexte (lecteur 3) | 5 doses × 1 280 = **6 400 lectures** au moins ; 8 960 si les deux témoins sont lus | ≈ 18 millions ; ≈ 26 millions avec les témoins |
| juge d'une autre lignée (lecteur 6) | **2 560 lectures** (texte scellé, ligne 147) | ≈ 7 millions |
| agrégateur séquentiel, lecteurs 1, 2 et 5, tests, intervalles, planchers | processeur, hors de la machine louée | 0 |

**Fourchette conditionnelle, sans tarif relevé.** Total d'entrée : **au moins 33 à 35 millions de jetons, environ 42 millions si les témoins sont lus partout.** À 1 USD par million : ≈ 33 à 42 USD. À 3 USD par million : ≈ 100 à 126 USD. Le brouillon 2 portait le haut à 56 millions et 170 USD : c'était la lecture « une par dose » du témoin bénin, abandonnée. **Ce poste peut dépasser la carte.**

**La dépense de carte est perdue si les lectures ne sont pas payées ensuite.** Leur devis est donc écrit et borné avant la demande de la ligne 2. Si le moniteur par action tourne sur une carte, c'est une ligne de carte en plus, absente d'ici. À fixer dans ce devis à part : les lecteurs, leur tarif relevé et daté, les conditions de la stratification du sous-échantillon de 2 560 actions.

## 7. États internes

Aucun enregistrement dans ces deux lignes ; aucune lecture (texte scellé, lignes 224 et 254). Si une lecture interne est décidée plus tard, les activations se recalculent sur texte imposé : 0,45 s par épisode, ≈ 0,11 h pour 896 épisodes, avec chaque adaptateur rechargé. C'est un devis à part.

## 8. Ce que ce devis ne couvre pas

- Les lectures hors carte (section 6) et un moniteur par action sur carte.
- **Le repli de deuxième ligne** par tirages honnêtes multiples (texte scellé, section 9.2), construit en parallèle sur décision de Lazar (GO-2026-11-18-47, `registres/go.md`, ligne 411 ; préenregistrement à part). Un devis à part est dû.
- Le bras B de la conception (coûts anti-ordonnés) : préenregistrement et devis distincts.
- La lecture interne par sondes et toute passe d'activations.
- Toute lecture sur les 64 tâches d'évaluation, qui restent vierges.
- Une carte de repli plus grosse en cas d'erreur de mémoire à la distillation.
- Le disque d'une instance arrêtée et gardée : rapatrier et détruire.

## 9. Avant la demande de la ligne 2

1. Débit mesuré à la ligne 1 et plafond recalculé par la formule de la section 5.
2. Gardes sur épisodes honnêtes passées (épreuves de l'oracle, M-1, effet minimal détectable ≤ 0,25, couverture de base ≥ 0,40).
3. Devis des lectures hors carte écrit et borné.
4. Prix, stockage, téléchargement et pilote relevés de nouveau.

## 10. Demande

**Ligne 1.**
- **Objet** : jouer sur une carte A100 SXM4 80 Go les épisodes honnêtes du modèle de base sur les 16 tâches de fabrication et les 16 tâches de vérification du bras A (256 épisodes), ce qui mesure aussi le débit.
- **Plafond demandé : 27 USD** (calcul refait : pire cas ≈ 26 USD).
- **Prix horaire maximal de la carte : 1,30 USD**, stockage ≤ 0,08 USD par heure en plus ; téléchargement ≤ 0,05 USD par Go.
- **Durée attendue : ≈ 3,9 à 4,0 h** ; pire cas sans relance ≈ 8 h. Attendu ≈ 6 à 7 USD.
- **Rapatrié et scellé** : les épisodes (textes et identifiants générés), le manifeste de la course (configuration et empreinte, versions, graines, commit, prix et durée), le débit mesuré, les traces. Instance détruite par son identifiant à la fin (R10).
- **Conditions avant départ** : (1) configuration du bras A scellée (la configuration de référence porte un calendrier clos au 17 novembre et l'ancien numéro de GO) ; (2) session de machine louée écrite et contre-lue (amorce, gardes de dépense, rapatriement) ; (3) part d'actions permutables éprouvée sur le vrai tokeniseur, hors ligne ; (4) contre-lecture d'ensemble du code par un agent neuf ; (5) ce devis scellé et la ligne inscrite à `registres/go.md` et `registres/depenses.md`.

**Ligne 2** : non demandée ici. Attendu ≈ 11,2 à 12,4 h, ≈ 14 à 18 USD ; plafond ≈ 42 à 45 USD sur débit mesuré, 75 USD à défaut.

## 11. Contre-lecture

Brouillon 1 contre-lu par un agent neuf le 18 novembre 2026 (R2) : « autorisable sous corrections », sources et arithmétique confirmées. Corrections appliquées au brouillon 2. Décisions de Lazar (section 1) appliquées ici. **Cette version finale n'est pas recontre-lue.** Chiffres neufs par rapport au brouillon 2, donc jamais contre-lus : la formule et les valeurs du plafond recalculé de la ligne 2, le bas de fourchette de la ligne 2 (11,2 h, 14 USD), la fourchette des lectures ramenée à une seule lecture du témoin bénin.

## 12. Déclaration

Rédigé par un agent neuf, qui n'est auteur ni du texte scellé, ni de ses addenda, ni de la conception, ni du code ; même agent que les brouillons 1 et 2. Aucune machine lancée, aucun appel réseau, aucune dépense. Aucun fichier de résultat, de base, de sonde ni de moniteur ouvert ; aucun fichier sous `runs/` ni `diag/`. Hors des pièces de la section 0, seuls ont été lus, par recherche de lignes, `registres/depenses.md`, `registres/decisions.md`, `registres/etat.md`, `registres/go.md`, les lignes 635 à 702 de `prereg/T0.6-organismes-v0-v1.md` et l'en-tête de `scripts/lancer_t06_v13.sh`. Les décisions de la section 1 et l'état du code sont repris du message de la session de relance ; j'ai vérifié au dépôt l'existence des lignes GO-2026-11-18-47 et GO-2026-11-18-53, du second addendum scellé et des deux fichiers de code, pas le détail des recommandations accordées. Les durées citées sont des relevés de la chaîne de l'organisme précédent, non du bras A.
