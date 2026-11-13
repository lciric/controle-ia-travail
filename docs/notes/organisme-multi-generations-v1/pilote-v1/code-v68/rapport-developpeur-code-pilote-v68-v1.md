# Rapport du développeur — code v68 du pilote d'une génération sur la famille MR-2 (C-1 à C-18) — v1

- **Développeur** : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent neuf de la session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3`. Je
  n'ai écrit ni la conception v4, ni le préenregistrement du pilote, ni le code v67.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-developpeur-code-pilote-v1.md`,
  sha256 `3b4f570cdaed476660b1709896d4fcc3a48e9eb33d269da123a480544dc5d633`, égale à son compagnon (vérifiée à 10:29:11).
  Sources vérifiées contre leurs empreintes : brouillon 4 `04ada9fa…`, `mesure_pilote_v4.py` `676d5f37…`, conception v4
  `47e38ec0…`, `monde_riche_v4.py` `4b165847…`, contre-lecture v4 `16da94d4…` ; R-2405, R-2429, R-2492, R-2500 à R-2515 lus.
- **Heures** (`date -u`, 13 novembre 2026) : début 10:29:11 ; chaîne vérifiée et arbres neufs 10:29 à 10:34 ; essai de la mesure
  dans la copie portée 10:34:52 à 10:35:59 ; chronométrage d'un monde 10:36:05 à 10:40:36 ; quatre mondes de développement
  10:40:55 à 10:55:46 ; tailles des textes servis 10:55:49 à 10:56:45 ; essais 10:56:53 à 11:05:49 ; relevé des lois de
  référence sur 20 mondes publics jusqu'à 11:03:52 ; premier passage du banc de mutations 11:06:13 (arrêté par moi, PID 6508, à
  ≈ 11:13, défaut de lecture des sous-essais, puis relancé) ; second passage 11:14:19 à 11:54:55 ; essais renforcés et trois
  mutations rejouées jusqu'à 12:01:05 ; essais à blanc 12:01:13 à 12:01:33 ; passage final du banc 12:01:51 à 12:44:39 ;
  journal des essais 12:44:46 à 12:46:31 ;
  fin : 12:47:04 (dépôt du rapport).
- **Aucune dépense, aucun appel de modèle, aucun serveur, aucune clé.** Réseau : le seul clonage en lecture du dépôt public
  `lciric/ideation-organism`, la récupération par refspec explicite de `prep/organisme-v65-v1` (dépôt de travail, pour le paquet
  v65) et la boucle locale des relais à amont factice. Aucun monde de test ni de calibration tiré : mondes publics seulement
  (secret de 32 octets nuls, phrase publique, étiquettes publiques). Calculs : un processus à la fois, `ulimit -v 6000000`,
  `OMP_NUM_THREADS=2`. Aucun refus de contrôle de permissions, de classifieur ou de crochet. Arrêt d'un processus : mon propre premier passage du banc, par son PID (6508, R10) ; ses dossiers
  provisoires `/tmp/tmp…` (copies de `orchestrator/`, aucun monde privé) sont restés sur la machine.

## 0. Verdict

**C-1 à C-18 sont écrits sous des noms neufs (code v68), essayés (51 essais et 42 sous-essais passés, cas sain et artefact pour chaque garde),
mutés (43 mutations, 43 tuées pour la raison attendue) et joués à blanc de bout en bout sur 4 mondes de développement vérifiés, par la vraie chaîne (lanceur → commande
→ relais local → amont factice → réponse brute et témoin scellés → gardien → `CARTES.json` → `mesure_pilote_v4.py` porté →
lecture → rapatriement).** Le code ne lève pas tous les marqueurs : la voie d'accès aux crédits de Claude est **décrite, non
branchée** (consigne), Astra reste « à confirmer » (identifiant, prix, champs), et le mode réel refuse tant que la configuration
porte un « à confirmer ». Deux constats de fond demandent une décision avant le scellement (section 7, Q-1 et Q-2).

## 1. Chaîne et arbres

- Arbre de l'organisme neuf : `…/scratchpad/agents/pilote-code/organisme`, clone en lecture du dépôt public (porte `94bfd92`) ;
  paquets v65 (`prep/organisme-v65-v1`, tête `3daf08e2`, récupéré par refspec explicite, lu par `git show`), v66 et v67 du dépôt
  de travail, **chacun égal à son compagnon** ; `git bundle verify` : v65 exige `94bfd92`, v66 exige `cef5ea60`, v67 exige
  `7e415cba` ; tête v67 `ab53b7f482df5149d9f672f40e04220dffb4173a` ; patch v67 recalculé = `195e4e63…` (égal au compagnon).
- Branche de l'organisme `prep/organisme-v68-pilote-mr2-v1` depuis `ab53b7f` ; commits `4737bb55bf979dc7dbf9a3bc049976dae9da4ba7`
  (jalon 1 : code et essais), `276b6afde8310b12af6f7c776ab4ee4c58d50e79` (jalon 2 : essais renforcés après le banc).
  **Fichiers neufs seulement** (`git diff --stat ab53b7f` : ajouts seulement), jamais poussé.
- Dépôt de travail : arbre de travail neuf `…/scratchpad/agents/pilote-code/depot`, branche neuve `prep/pilote-mr2-v1` depuis
  `3d83b47f`, extraite **sans** `docs/notes/bras-attaque`, `diag`, `runs` ni les autres chemins interdits (aucune liste de ces
  chemins). Ajouts seulement, sous `docs/notes/organisme-multi-generations-v1/pilote-v1/code-v68/` ; aucune poussée.
- Interpréteur : `/home/user/controle-ia-travail/.venv/bin/python -I -B` (Python 3.13.18, numpy 2.4.6, pytest 9.1.1). Le texte
  dit numpy 2.5.3 : **l'essai scellé de la mesure v4, rejoué dans la copie portée sous numpy 2.4.6, rend le même
  `corps_sha256`** (`771b351b…` pour le fichier scellé ; corps égal).

## 2. Les pièces, une par une

| # | ce que fait le code v68 | où | essais (sain / artefact) |
|---|---|---|---|
| C-1 | `charger_mondes_prives` : chemin absolu donné au lancement, **hors de l'arbre et hors de tout dépôt** (aucun parent portant `.git`), empreinte du fichier = celle du registre, 4 mondes numérotés 1 à 4, empreinte de chaque devis recalculée (et égale à la liste du registre si donnée), dimensions exigées | `pole/pilote_mr2_v68.py` | `C1MondePrive` : sain ; 8 artefacts (empreinte, relatif, 3 mondes, doublon, devis altéré, liste fausse, dans un dépôt, dans l'arbre), dimension |
| C-2 | manifeste : empreintes seules (`monde_au_manifeste`) ; `exiger_manifeste_sans_loi` refuse toute clé `loi_vraie`, `loi`, `spec`, `effets`, `composante_condition`, `pente`, `poids`, `biais`, `decalage` ; appliqué aux contrôles et au manifeste du lanceur | idem ; lanceur | `C2Manifeste` |
| C-3 | dimension 8, 3 sous-populations, 3 issues **lues dans le monde** et égales au gabarit ; tranche de **400 épisodes** de développement : instances N(0, 1) à six décimales et sous-population uniforme (outils portés), issues tirées de la loi compilée, graine `SeedSequence` dérivée de l'empreinte du devis (R9) | idem | `C3C4…` (400, 8 traits, g ∈ {0, 1, 2}, déterministe, différente d'un monde à l'autre) |
| C-4 | `compiler_v4` **porté octet pour octet** (`orchestrator/mr2_v68/`, 13 fichiers, chacun égal à son compagnon et au dépôt de travail ; disposition des dossiers gardée pour que `sys.path` et `verifier_imports` de la mesure tiennent) ; loi compilée validée par `selection_pari.valider_loi(loi, 3, 8)` ; `verifier_v4` porté (C0 à C8) appelé par `generer_v4` | idem | `OutilsPortes` ; `test_artefact_loi_compilee_invalide` |
| C-5 | gardien à la dimension du monde : `valider_loi`, grammaire servie (types, champs exacts, indices **entiers** 0 à 7 et 0 à 2, bornes ±4 des softmax, sûreté 50, profondeur ≤ 40), **au plus 3 conditions emboîtées** (`conditions_emboitees` du programme v4 **et** un compte qui parcourt aussi `defaut`, le plus grand des deux), jeu factice fixe à D = 8 (90 instances) : chaque nœud par `selection_pari.proba`, la loi entière par `M.probas` égale à 10⁻⁹ ; gabarit de la proposition (clés exactes, énoncé ≤ 400) ; **septième carte et suivantes refusées et comptées** | idem | `C5Gardien` : **3 conditions admise, 4 refusée** (sur trait, sur sous-population, sous `defaut`), 13 artefacts de grammaire, motifs exigés, jeu factice (deux artefacts), septième |
| C-6 | gabarit servi : consigne (au plus 6 lois, au plus 3 conditions emboîtées) et grammaire de la course à D = 8, 3 sous-populations, six types ; **rien sur les conditions du monde, les sortes d'effets, la famille** (R-2504) ; `[GABARIT-SHA256]` = `2b1b33ec0e72ad64cde462487a87108e03b1d63690d81f609a9ad728ef3ce753` (JSON canonique du gabarit, indépendant du monde) ; texte servi = consigne + contexte (monde public, gabarit, archive {K1}, épisodes) ; `pieces_du_texte` vérifie qu'il n'est bâti que sur ces pièces | idem | `C6Gabarit` (mots interdits absents, exemples de la grammaire admis, texte augmenté refusé) |
| C-7 | commande `commande_pilote_v68.py` et relais `relais_pilote_v68.py` (neufs, bibliothèque standard), **un relais par proposeur** (ports 8811 à 8814), plafond du relais = part, 4 appels au plus, modèle exact ; dialectes `claude`, `gemini`, `astra` ; **voie Claude décrite, non branchée** (le relais répond 501 ; le lanceur refuse en mode réel avant tout appel) ; Argon : `generateContent` écrit, jamais appelé ; Astra : hypothèse « chat completions », à confirmer ; **configuration v9** (bornes de sortie, plafonds, prix, délais, parts) lue par le code ; bornes **figées** et vérifiées payables (section 7, Q-1) | `exemples/pilote-mr2-v68/` ; `pole/proposeurs_pilote_v68.py` | `Configuration` (9 artefacts à motif), `Commande`, `RelaisRefus` |
| C-8 | jetons : Claude `usage.input_tokens`, `output_tokens` (réflexion comprise) ; Argon `promptTokenCount`, `candidatesTokenCount` + `thoughtsTokenCount` ; Astra (hypothèse) `prompt_tokens`, `completion_tokens`, `reasoning_tokens` ; **raison d'arrêt lue** : complet / tronqué / refus ; modèle servi exact ou suffixe de date (8 chiffres) ou de révision (3 chiffres) | commande | `test_dialectes`, `test_etats` |
| C-9 | parts : `fable52` 12, `opus55` 8 (π1 = 20, crédits de Claude), `argon` 8, `astra` 8, machine 3 (π2 = 19) ; somme par ligne = montant ; part = 4 plafonds de session ; **lecteur de deux lignes** par `registre_go_v66.verifier_go_v66` au montant exact (π1 ≠ π2) ; avant chaque appel, arrêt si la part serait atteinte au pire cas | `pole/proposeurs_pilote_v68.py` ; lanceur | `test_go_pi1_pi2` (la forme « 20 USD (sur crédits) » de la ligne proposée est lue 20), `test_part_atteinte_arret` |
| C-10 | une session neuve par appel (dossier créé vide, commande lancée dans un dossier courant vide, environnement minimal sans clé) ; **réponse brute** (sortie entière de la commande, code, corps entier du relais écrit par la commande avec son compagnon **avant toute lecture**) scellée **avant l'extraction** ; **témoin d'isolement** scellé : relais attendu, session neuve, aucun fichier écrit, empreinte du texte servi = reçue par le relais = lue par la commande, **aucun outil, un seul message, aucun message système** ; absence ou témoin faux → arrêt (code 3) | idem | `C7C8C10Appel` : sain pour les 4 proposeurs ; états (tronqué, refus, modèle faux, illisible, usage absent ou faux, panne) ; relais absent ; session existante ; témoin faux ; sans dernière ligne ; sans témoin |
| C-11 | lanceur `demonstrations/pilote_mr2_v68.py jouer` : **une génération, proposeurs puis gardien**, aucun juge, aucun étage, aucun test de mort ; mondes 1 à 4, proposeurs dans l'ordre ; **un fournisseur en panne est abandonné** (codes 2, 3, 4, 6 de la commande), ses appels restants « échec » sans appel ; aucune reprise ; mode `reel` : configuration sans « à confirmer », texte scellé et son **bloc gelé égal au code**, deux GO, relais branchés à plafond = part ; mode `a_blanc` : relais à amont factice lancés et arrêtés par leur PID | lanceur | `C11C13C14C18EssaiABlanc` ; `test_mode_reel_refuse_sans_go` |
| C-12 | {K1} par monde : la K1 de `preparer_mondes` du **programme de la mesure** (même oracle, donc exactement la loi que la mesure retire du témoin, R-4), arrondie à six décimales (contrôlée), identifiant opaque ; empreinte de l'archive au manifeste | `pole/pilote_mr2_v68.py` | `C12Heritage` |
| C-13 | export `CARTES.json` = `{cartes, appels}` au format du programme v4 (cartes d'un appel en échec jamais exportées) ; `MONDES.json` privé (`ecrire_prive`) | lanceur | mesure v4 rejouée sur l'export (essai et essai à blanc) |
| C-14 | `lire` : champ `regle` de la sortie de la mesure, après contrôle du corps contre `corps_sha256`, du programme (`676d5f37…`) et des modules importés contre les fichiers portés ; rapprochement des coûts | lanceur | `test_lecture`, 3 artefacts |
| C-15 | `generer` : `graine_monde_pilote` **appelée dans le programme v4**, les 8 tirages de `generer_v4` porté, refus si aucun tirage conforme ; `tirer_secret` (32 octets, mode 0600, jamais écrasé, empreinte rendue) ; `ecrire_prive` (liste blanche = dossier du secret, hors dépôt, 0600, sans écrasement) ; impressions : empreintes et contrôles seulement | `pole/pilote_mr2_v68.py` ; lanceur | `C15Generateur` |
| C-16 | `jouer_c16` : `lois_de_reference` du programme v4, chacune passée au **gardien du pilote** ; refus sinon (arrêt avant tout appel) | idem | `C16C17` : sain ; artefact simulé ; **artefact naturel** (section 7, Q-2) |
| C-17 | `jouer_c17` : écart `selection_pari.proba` / `M.probas` ≤ 10⁻⁹ sur un jeu fixe (lois de référence des 4 mondes et 6 cartes écrites : chaque type, `defaut`, 3 conditions sur trait et sous-population, transformée complète), sur le jeu factice et sur 256 épisodes par monde (1 114 instances) | idem | sain (écart maximal 3,9·10⁻¹⁶ à l'essai à blanc) ; artefact (évaluateur biaisé de 10⁻⁷) |
| C-18 | `rapprocher_couts` (commande / journal du relais, par appel) ; `cartes_a_relire` (3 par appel, graine = 16 premiers chiffres de l'empreinte de `CARTES.json`) ; proposeurs factices des quatre relais (appelant `factice:` du relais, 9 scénarios, lisant **le seul texte servi**) ; `rapatrier` (pièces permises seulement, refus de tout fichier qui porte un monde, rien copié alors ; liste des fichiers copiés et de leurs empreintes) | `pole/audit_pilote_v68.py` ; relais | `test_couts_artefact`, `test_cartes_relues`, `test_rapatriement` (un monde déguisé en témoin : refus, rien copié) |

## 3. Fichiers neufs et empreintes (tête de l'organisme)

Bloc gelé que le préenregistrement attend : `EMPREINTES-code-pilote-v68.txt` (sorti par `pilote_mr2_v68.py bloc`, le lanceur en
mode réel exige que le bloc du texte scellé lui soit égal à l'octet) : empreinte du gabarit, bornes, plafonds, parts,
`octets-entree-max`, et l'empreinte de chacun des 31 fichiers gelés (code v68, configuration v9, modules de l'arbre chargés par le
lanceur — fermeture statique essayée —, et les 13 outils portés).

| sha256 | fichier (`orchestrator/`) | gelé |
|---|---|---|
| `8da846fd2311f9064b4c000c07e115068a79308c795ad52c6f4288fe1ba5a1eb` | `pole/pilote_mr2_v68.py` | oui |
| `a9fb2c0f443b5d85fd047ca41288b746f293b150f3d140c674b7c834fabd065e` | `pole/proposeurs_pilote_v68.py` | oui |
| `1bdcd43273e2b2fc43a90a74e94313270451d96b9ac3b256b13a49075fffd877` | `pole/audit_pilote_v68.py` | oui |
| `f6876f13ed8414f7ac116837ce9a4dcdeecea30b086c9402329c7805a685380c` | `demonstrations/pilote_mr2_v68.py` | oui |
| `b61ceaca3887a60307a05b3ba3f4f7993d0cf3f04d974356e3cf4b48b2ded7e9` | `exemples/pilote-mr2-v68/commandes/commande_pilote_v68.py` | oui |
| `0a5f37b03f12e05bcc0cd2ee76ca999aa173397727fb29b43dd90c0ce30c8349` | `exemples/pilote-mr2-v68/commandes/relais_pilote_v68.py` | oui |
| `5d7b667bb3fc284d798adc29e81e5a04bd363b998d13dc80dd0dd457ca3ba62e` | `exemples/pilote-mr2-v68/configuration-pilote-mr2-v9.json` | oui |
| `4ec62e4f68b729c080352b8ce5a860e445a6aeda0a84e3573b2bfb409c5c8b6a` | `essais/test_pilote_mr2_v68.py` | non |
| `b4dc8e3c5fe7168f4aa5f405d038823a79b43bec1ec13f52795f9cbb52354148` | `essais/mutations_pilote_mr2_v68.py` | non |
| (13 fichiers, empreintes au bloc) | `mr2_v68/` : outils v1 à v4 et programme de la mesure, portés octet pour octet avec leurs compagnons | oui |

Pièces versées dans `docs/notes/organisme-multi-generations-v1/pilote-v1/code-v68/` (branche `prep/pilote-mr2-v1`), chacune avec
son compagnon : paquet `organisme-v68-pilote-mr2-v1.bundle` (`43d09adc0253f86180f2da3341ca41c0538692588abeaf9881619b13329d2331`,
prérequis `ab53b7f`, tête `276b6afd…`) ; patch `organisme-v68-contre-ab53b7f.patch`
(`70c68837e303cc6fb15eccee19e2b27c8c34818358bc1334c6c4b4ae806ea5f8`) ; bloc gelé `EMPREINTES-code-pilote-v68.txt`
(`27311ce3d593badf5e7f9492da4c558341a970f494abc6ca53849c5ad68fa709`) ; journal des essais `essais-pilote-v68.txt`
(`f19dee5c…`) ; banc final `mutations-pilote-v68.json` (`f2198fd1…`) et second passage `mutations-pilote-v68-second-passage.json` ;
essais à blanc `essai-a-blanc-v68/A/`, `B/` ; paquet du jalon 1 `organisme-v68-pilote-mr2-jalon1.bundle` (`0c990e83…`, gardé,
remplacé par le paquet v1).

## 4. Essais

`essais/test_pilote_mr2_v68.py` : **51 passés, 42 sous-essais passés, en 102,79 s** (journal `essais-pilote-v68.txt`). Mondes des essais : publics
(`generer_monde_v4(P1.cle("pilote-v68-essai-developpement", r))`), écrits dans un dossier provisoire hors de tout dépôt.

## 5. Banc de mutations

`essais/mutations_pilote_mr2_v68.py` : copie neuve de `orchestrator/` par mutation, remplacement présent une seule fois, empreinte
de la commande ou du relais recopiée dans la configuration de la copie (la mutation est jugée sur son comportement), essais sains
d'abord ; « tuée » seulement si l'essai attendu échoue. Deuxième passage (11:14 à 11:54) : 40 tuées pour la raison attendue,
**3 survivantes**, qui m'ont fait renforcer les essais : M04 (indice 8 admis par la grammaire, refusé seulement par l'évaluation :
motif exigé), M24 (part libre, masquée par le contrôle des parts de GO : artefact rendu cohérent, motif exigé), M43 (contrôle
d'usage inatteignable par les scénarios d'alors : scénario `usage_faux` ajouté) ; rejouées tuées. Passage final sur le code gelé :
**43 mutations, 43 tuées pour la raison attendue** (`mutations-pilote-v68.json`). Une mutation écrite puis retirée parce qu'équivalente : supprimer la branche « refus du
modèle » de la commande (un refus tombe alors dans « raison d'arrêt inconnue », échec aussi).

## 6. Essai à blanc de bout en bout (hors ligne)

Quatre mondes de développement **vérifiés** (`generer_mondes` sur le secret public de 32 octets nuls, phrase « développement
public, jamais pour un vrai monde », empreinte de texte nulle ; `generer_v4` et `verifier_v4` portés ; 882 s ; tirages refusés :
monde 3 un C0, monde 4 un C0 et un C8) : fichier privé `687974573f18d937020350fe9534c529e70cb654e9219d0985b01e46fb05f07c`,
mondes `44106f4b…`, `beebeb25…`, `52861c7a…`, `2c358575…` (empreintes seules versées ; les mondes restent hors dépôt). Textes
servis : 48 562 à 48 613 octets.

- **A, sain** (tous les relais « k1_plus » : copie de K1, K1 et un second trait, trois conditions, quatre conditions, sous-
  populations, clé en trop, septième) : 16 complets ; mesure v4 : 16 répondus, 32 refusées au gardien, 16 au-delà de six, aucune
  non évaluable ; x = 0 ; **issue P-2 avec réserve R-1** (témoin 0 sur 16 : des proposeurs qui ne vont pas au-delà de K1 ne se
  lisent pas comme le meilleur résultat — le témoin fait son office) ; audit R4 « déclenché : x = 0 » ; coûts rapprochés : écart
  nul pour les quatre ; rapatriement : 109 fichiers, **aucun monde** ; code gelé au manifeste = bloc gelé.
- **B, pannes mêlées** (Fable tronqué au monde 3, Opus copies de K1, Argon refus au monde 2 et réponse illisible au monde 4,
  Astra en panne) : Astra **abandonné après le monde 1** (code 3), ses trois autres appels « échec » sans appel ; 10 complets, 1
  tronqué, 5 échecs ; mesure : 9 répondus, 1 sans carte → **issue P-0** (« 9 appels répondus (minimum 12) ; minimum par monde 2 ») ;
  écarts de coût nuls ; rapatriement : 91 fichiers, aucun monde.

Sorties versées (rapatriées, sans monde) : `essai-a-blanc-v68/A/`, `essai-a-blanc-v68/B/`.

## 7. Questions ouvertes (décisions de fond que le texte ne tranche pas ; je ne les tranche pas)

- **Q-1 — Bornes de sortie (marqueur « à figer »).** La commande juge le pire cas sur les **octets** du texte servi (règle des
  commandes v6 : un jeton ≥ un octet), et les textes servis font ≈ 48,6 ko (400 épisodes à 8 traits) ; le texte estimait l'entrée
  à 15 000 jetons. Bornes payables au pire cas pour 52 000 octets : Fable 64 395, Opus 89 395, Argon et Astra 29 395. **Figées :
  64 000 / 89 000 / 29 000 / 29 000** (texte : 70 000 / 95 000 / 36 000 / 36 000, estimées). Le texte disait « six arbres pleins ≈
  30 000 jetons » : chez Argon et Astra, 29 000 rend la troncature plus probable. Options : (a) garder (garantie dure du plafond
  de session ; troncatures possibles, encadrées par le minimum de 12) ; (b) juger l'entrée en jetons estimés (bornes du texte ;
  garantie seulement estimée, le plafond du relais reste dur) ; (c) relever les plafonds de session d'Argon et d'Astra (dépense :
  nœud). Ma recommandation : (a), confiance 0,55.
- **Q-2 — C-16 et la borne ±4.** Le gardien porte les bornes ±4 (texte). Sur 20 mondes publics **non vérifiés** de la famille, 2
  ont une loi de référence « monde sans latente » de coefficient 5,25 et 5,05 (monde 3 et 5 de l'étiquette publique
  `pilote-v2-essai-developpement`) : **C-16 arrête alors le pilote avant tout appel**, et le texte ne prévoit une nouvelle graine
  que sur texte neuf et mot de Lazar. Sur les 4 mondes vérifiés et les 8 de l'étiquette v68, aucune. Si le taux est de cet ordre,
  ≈ 1 chance sur 3 d'un arrêt au pilote. Options : (a) garder (arrêt, texte neuf) ; (b) C-16 sans la borne ±4 pour la seule loi
  « monde sans latente » (elle n'est jamais servie ; mais alors un proposeur ne peut pas l'écrire) ; (c) une règle de tirage écrite
  d'avance (refuser au générateur un monde dont une loi de référence sort des bornes : changerait la famille). Aucune
  recommandation ferme (0,4 pour (c), à voir avec le concepteur).
- **Q-3 — `defaut` et les conditions emboîtées.** La fonction de référence du programme v4 ne parcourt pas `defaut` : une loi qui
  y cache 4 `si_sinon` passe la référence. Le gardien v68 compte le plus grand des deux (identique sur toute loi sans `defaut`).
  À confirmer par le contre-lecteur (le texte dit « comptées comme `conditions_emboitees` du programme v4 »).
- **Q-4 — Effort et réflexion des modèles.** Le texte ne fixe ni l'effort de Fable 5.2 et d'Opus 5.5 (réflexion toujours
  active ; effort par défaut du modèle, Opus 5.5 « medium »), ni la configuration de réflexion d'Argon ni d'Astra. Or « p_c ne
  vaut que pour ce gabarit » : ces réglages en font partie. Le relais v68 n'envoie aucun réglage (défaut du modèle).
- **Q-5 — Voie d'accès aux crédits de Claude** : décrite dans l'en-tête du relais (API Messages, aucun outil, aucun système, en
  flux pour 64 000 à 89 000 jetons, **sans** repli de modèle `fallbacks`, qui changerait le modèle servi) ; à confirmer : quel compte
  porte les crédits, relevé de la consommation par appel. Prix de Claude (8 / 40 et 4 / 20 USD par million) : tarifs de mon
  aide-mémoire au 3 novembre, à confirmer.
- **Q-6 — Astra** : identifiant `gpt-6-astra`, prix 10 / 50, champs ([CHAMPS-ASTRA]) et URL de l'amont à confirmer ; dialecte
  « chat completions » supposé.
- **Q-7 — Argon par le relais v68** (corps entier rendu, témoin de ce qui est reçu et envoyé) au lieu du relais v6 éprouvé (qui ne
  rend ni le corps entier ni le témoin, donc ne satisfait pas C-10) : `generateContent` écrit, jamais appelé.
- **Q-8 — Appels « non conformes »** (refus du modèle, modèle servi différent, usage absent) : lus « échec » **sans abandon** du
  proposeur (seule la panne d'un relais l'abandonne, liste d'arrêt) ; un refus du modèle est un « échec », pas un « complet sans
  carte » (hors du dénominateur dans les deux cas). À confirmer.
- **Q-9 — Taille des lois** : la grammaire de la course (v64) bornait le JSON d'une loi à 2 000 caractères (servi à
  l'expérimentateur) ; à D = 8, un arbre de 24 feuilles en fait ≈ 7 000. Le pilote (sans expérimentateur) ne garde que la
  profondeur ≤ 40. « Le même gabarit au banc et dans la course » : la course devra trancher cette borne.
- **Q-10 — Épisodes de développement** : graine dérivée de l'empreinte du devis seule (le texte ne dit pas la dérivation).
- **Q-11 — Publication** : les outils MR-2 et le programme de la mesure sont portés dans l'arbre de l'organisme, dont le dépôt est
  public ; pousser la v68 publierait le générateur de la famille. Décision de Lazar (rien poussé).
- **Q-12 — Chemin du dépôt de travail dans un outil porté** : `verifier_monde_kimi_v1.controler_grammaire` insère
  `/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/orchestrateur-v52b` en tête de `sys.path` (fichier gelé, non
  modifié) ; le code v68 rend `sys.path` intact après l'appel (`sans_chemin_v52b`, essayé). Sur la machine, ce chemin n'existe pas.

## 8. Marqueurs

- **Levés par le code** : [GABARIT-SHA256] `2b1b33ec0e72ad64cde462487a87108e03b1d63690d81f609a9ad728ef3ce753` ; bloc gelé des
  empreintes du code du pilote et des modules importés (`EMPREINTES-code-pilote-v68.txt`) ; bornes de sortie figées (sous Q-1).
- **Décrits, non levés** : voie d'accès aux crédits de Claude (Q-5) ; [CHAMPS-ASTRA], identifiant et prix d'Astra (Q-6, champs
  supposés) ; lignes de GO (numéro, date, mot de Lazar).

## 9. Ce qui reste avant le premier appel (hors de ce mandat)

Contre-lecture du code par un autre modèle (N-052) ; réponses à Q-1 à Q-12 ; scellement du texte avec le bloc ; GO π1 et π2 ;
secret tiré sur la machine (`pilote_mr2_v68.py secret`), engagé et poussé ; phrase de Lazar ; `generer` (≈ 15 minutes pour 4
mondes) ; `preparer` ; essai à blanc **avec les vraies pièces** sur la machine ; relais lancés avec leurs clés.
