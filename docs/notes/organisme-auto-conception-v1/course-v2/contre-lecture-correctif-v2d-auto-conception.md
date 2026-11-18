# Contre-lecture du correctif v2d de la course d'auto-conception (épreuve v4, lanceur v4, additif v2d)

- Date : 2026-11-18T16:56:10Z (date -u).
- Contre-lecteur : modèle K, contre-lecteur neuf (R2) ; je n'ai écrit ni l'additif v2d, ni le programme d'épreuve v4, ni le lanceur v4, ni leurs essais. Le rapport du développeur (modèle L′) a été traité comme une donnée à vérifier, jamais comme une preuve.
- Travail hors ligne seulement : aucun appel à un fournisseur, aucun relais lancé, aucune dépense, aucune valeur de clé lue ; copie de l'orchestrateur `/home/user/ideation-organism` lue sans écrire (`a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, statut propre). Dépôt à `63ca624f96c05ef1f496920a1e3945b1024b0d0d` (fetch par refspec explicite, avance rapide seule). Pièce neuve (R12), aucun fichier existant modifié.

## 1. Pièces lues, empreintes complètes (chaque compagnon `.sha256` vérifié « OK » quand il existe)

| pièce | sha256 |
|---|---|
| Additif v2d `course-v2/additif-preenregistrement-course-auto-conception-v2d.md` | `cb4d44d081e505dfafc2ae4552fbaa8b80e3370ea7e295966a6a1708ce512e45` |
| Lanceur v4 `scripts/lancer_course_auto_conception_v4.py` | `b1661f119407530b0f6e940a75e8811d6dd968fd33bfca08f7f0933ed4e8707e` |
| Programme d'épreuve v4 `scripts/epreuve_temoins_auto_conception_v4.py` | `04f62b8c48db9e9b04114aaa37f00801e825ff0bc2d4a86934b44f2b79263d75` |
| Programme d'épreuve v3 `scripts/epreuve_temoins_auto_conception_v3.py` (diff contre le v4) | `0c72dd8763537152b7339ca15ff439f759c062f0b33a6571a513029870eebd1b` |
| Lanceur v3 `scripts/lancer_course_auto_conception_v3.py` (diff contre le v4) | `42001b2807337cfd4c10c6708b384f5f218201457eab95d309080c6c57949fef` |
| Additif v2c `course-v2/additif-preenregistrement-course-auto-conception-v2c.md` | `7c76eba0340040b2c2d29cf3aa5015a194632ac24f3e558565a22424702b0cfd` |
| Préenregistrement v2 `course-v2/preenregistrement-course-auto-conception-v2.md` | `0d51e0b3f51dd731351589187c124b7ee1a6237494aa0274825b19085c6763c6` |
| Commandes v2d `course-v2/commandes-exactes-course-auto-conception-v2d.md` | `382f463f2c51890589cc5f2bfe749d3964bddd6bb0f5032e226c881b3d217854` |
| Rapport du développeur `course-v2/rapport-developpeur-correctif-v2d.md` | `e3fe8e78b7711860747a7d66279b696d8cf0b77b07054276a720b92bd15fb8a5` |
| Essais de l'épreuve v4 `tests/test_epreuve_temoins_auto_conception_v4.py` | `456ca30390d3973ade564afc5642d1faa629951fd86c7fdf8259be629fdcdc09` |
| Essais du lanceur v4 `tests/test_lancer_course_auto_conception_v4.py` | `a049e4be37588b6a63b68ea2cda9fa9f4aef8030f456031cfbb3489d67c00d45` |
| Rapport scellé de la tentative v3 `course-v2/epreuve-temoins-reelle-auto-conception-v3.json` | `1e11376fe1255d281212bac086f25d143ab8c86f520dd16f3207ad95d40d02cf` |
| Sortie d'erreur de la tentative v3 `course-v2/epreuve-reelle-v3-2026-11-18-v1/epreuve-reelle-v3.stderr.txt` (22 refus « sandbox required but unavailable » : 11 de l'aiguilleur, 11 du juge Claude) | `b30fb23c831078c86bdda42a43feaf63183036d7ee5e39e9b2b9f8f48efda0d7` |
| Sortie standard de la tentative v3 `…/epreuve-reelle-v3.stdout.txt` | `d55fb67b987c042124779024b7c196be47e3e4ee05f422f78febed913cbd7640` |
| Essai à blanc v2d `course-v2/essai-a-blanc-v2d/` (15 compagnons, tous « OK ») : manifeste de départ du lanceur | `d0d94fb498e6893d0dbc57a2c5d0b018f22f1599c5376e7537dc1bd51b8c5799` |
| … acte de gel | `1e4639cbc5567c1bc5f584a39eccf4781b7ba7304d78bbb3ace859aaa656249c` |
| … épreuve hors ligne v4 | `8b462ef7f6ad53ec70e55b5ab4cba6f64bd070a31d4987ecc302772ed258c900` |
| Relais Gemini d'Argon `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py` | `2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb` |
| Commande d'Argon `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py` | `46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46` |
| Enveloppe d'Argon `rapports/fille-ideation-1-v1/appel-argon-v5.sh` | `37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a` |
| Relais Gemini v4 de Carbon (sur `main`) `relais_gemini_v4.py` | `543e728d90e809c661fdc26f1e1b1a32b2e23128a7d09e3b5d16f851408a35b4` |
| Commande de Carbon par lot (sur `main`) `commande_gemini_lot_v1.py` | `9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75` |
| Porte de plafond `scripts/porte_plafond_relais_v1.py` | `fab5fe2e924c47799d968663baddfecb85dd6f74e9f859d9047b185eb36382b1` |
| Orchestrateur `pole/adaptateurs.py` (sonde `etat_bac_a_sable_detaille`, `Resultat`, commande externe l. 751-760) | `a1a8ede8d38884a28365ee797dcd3018dbf09ea1baefa3f57cfcb3281c529c99` |
| Orchestrateur `pole/adaptateurs_v56.py` (portes de plafond, `centime_bas`) | `d36c79b272af450b8d67313f44068743d80f0204bcedbd30f5d879829c945a17` |
| Pièce de départ `course-v2/piece-de-depart-auto-conception-v2.json` (reprise telle quelle) | `e2689fa22fff31319ff69deefe10c066d5329fab28d9c9b133750f2534fc1ded` |
| Sonde d'Astra du jour `course-v2/sonde-astra-commune-2026-11-18-v1.json` (reprise telle quelle) | `802b840edbf14983ce302b71253242c753e70aa60335868e811fdb6fd45e8f43` |
| Relevé des prix Claude `course-v2/releve-prix-claude-course-auto-conception-v2.json` (repris tel quel) | `ed812e6a336ba4682053dd7bec5554c6f5aeb4fb54dcc7d22760900a33e890b4` |
| Registre des GO lu au commit de `main` `3e07d0d136e069d8838a33969093dd43a2682043` : lignes `GO-2026-11-18-20` (calcul, 90 USD), `-21` (calcul, 5 USD), `-36` (décision, échéance 2026-11-18), `-39` (décision) | lignes `7aa8b1a4…`, `f69efafb…`, `2cce7369…` (empreintes de ligne rendues par `verifier_go` et `verifier_mot_de_reprise`) |

Journal du relais Gemini de la tentative v3 (hors dépôt, `/home/user/execution-auto-conception-v2c/journal-relais-gemini-epreuve.jsonl`, lu sans écrire) : 19 lignes, 15 admises (8 `countTokens`, 7 `generateContent`, par paires, puis le `countTokens` de t08), 4 refus 429 « --max-appels (15) atteint » (le `generateContent` de t08, puis les `countTokens` de t09 à t11). Ce que l'additif v2d § 2 en dit est exact.

## 2. Décomptes

| essais | résultat |
|---|---|
| `tests/test_epreuve_temoins_auto_conception_v4.py` + `tests/test_lancer_course_auto_conception_v4.py` (commande § 1 des commandes v2d) | **201 passés** (45 + 81 fonctions d'essai, paramétrées : 71 + 130), 0 sauté, 96 s |
| Les 241 de la commande v2c, avec la désélection nommée | **240 passés, 1 désélectionné**, 0 sauté, 158 s |
| L'essai désélectionné joué seul (`test_constantes_identiques_a_la_v2_sauf_les_chemins_neufs` du v3) | échoue sur la seule ligne `assert not E.RAPPORT_REEL.exists() and not E.DECLARATION_EPREUVE.exists()` : le rapport et la déclaration v3 existent depuis l'épreuve réelle ; cause étrangère au correctif, comme dit |
| Compagnons `.sha256` de toutes les pièces nommées ci-dessus et des 15 fichiers de `essai-a-blanc-v2d/` | tous « OK » |
| Commit `63ca624f` | 44 fichiers, tous « A » (ajouts seuls, R12) ; arbre de travail propre |

Vérifications jouées par moi, hors ligne :

- **Lecture gelée identique à l'octet** : les sources de `lire_epreuve`, `jouer`, `verite`, `servir`, `identifiant_servi`, `controles_statiques`, `hors_ligne`, `preparer_appels` et `verifier_dossiers_d_appel` extraites par l'arbre syntaxique des deux fichiers (v3, v4) sont identiques caractère pour caractère.
- **Règle de requalification rejouée sur le rapport scellé de la tentative v3** : avec ses incidents (aiguilleur 11, juge Claude 11, juge Argon t08 à t11) → « non conclue » ; avec un verdict d'Argon rendu faux à côté (t06 rendu notable) → « échouée », `autres = [juge-argon/t06]` ; avec t08 absent mais sans incident consigné (réponse « ok » illisible) → « échouée ». La requalification ne touche que « échouée » → « non conclue » (`qualifier_verdict`, l. 574-585) ; elle ne rend « réussie » que si `lire_epreuve` l'a rendu.
- **Lignes de GO sur `main`** : `verifier_mot_de_reprise` accepte la ligne `GO-2026-11-18-36` du registre au 18 novembre et la refuse au 19 novembre (échéance le 18) ; `verifier_go` accepte `GO-2026-11-18-21` à 5 USD et `GO-2026-11-18-20` à 90 USD.
- **Budget** : dépense v3 lue dans le rapport scellé 0,132289 USD ; budget de la reprise 4,867711 USD ; les portes de l'orchestrateur le transmettent au centime inférieur (`centime_bas`, `adaptateurs_v56.py`), 4,86 ≤ `--plafond-ligne 5` de la porte (`porte_plafond_relais_v1.py`, l. 91).
- **Bornes** : `appels_relais_gemini_requis` rend 24 (11), 288 (143), 376 (187), 464 (231) ; `appels_argon_au_pire` avec la configuration (6 espèces dont Kimi non déclarée → 5 actives, 4 cartes comptées, 1 juge Argon) rend 11 + 11 × 5 × 4 = 231.
- **Deux appels de relais par appel d'Argon, lus dans le code** : `appel-argon-v5.sh` lance `commande_argon_v3d.py` sans `--sans-compter-jetons` ; `--compter-jetons` est vrai par défaut (l. 708-710) ; `countTokens` (l. 822-824) puis `generateContent` (l. 865) ; `relais_gemini_v2.py` : `ACTIONS_PERMISES` (l. 79) et `compteur.admettre(longueur)` pour tout POST (l. 280), refus à `appels >= max_appels` (l. 183-186). Carbon sur `main` : `countTokens` (l. 161) puis `batchGenerateContent` (l. 181) ; `relais_gemini_v4.py` admet un lot **et** un appel pour `batchGenerateContent` (l. 536-537), relevés sous `--max-releves` (défaut 2 000). Astra : une requête par appel (inchangé).
- **Ordre dans `reel()` du v4** (l. 655-772) : environnement sans nom de clé → refus si le rapport v4 existe → pièce de départ → GO-21 → GO-36 → dépense v3 et budget → pièces épinglées (ce programme compris) → orchestrateur → **sonde du bac** → déclaration → **borne d'Argon doublée** (`verifier_procedure_relais` à 24, puis `verifier_borne_argon` sur les arguments et sur l'état) → porte à blanc → adaptateurs et garde des dossiers → transmission du budget → appels. Les deux causes de la tentative v3 (bac absent ; relais borné à 15 pour 22 appels) sont donc refusées avant tout appel et avant toute transmission de plafond.
- **Sonde du bac** par la commande § 4 des commandes v2d, jouée telle qu'écrite dans ce conteneur : `{"actif": true, "proc_neuf": true, "motif": "bwrap et socat présents ; bwrap s'exécute, réseau isolé ; /proc neuf monté"}`.
- **Commandes v2d** : interpréteurs `/usr/bin/python3` et `/usr/local/bin/python3` présents ; empreintes des pièces inchangées citées (§ 1) toutes retrouvées sur disque ou sur `main` (`garde_credit_relais_v5` `6cf87869…`, `lancer_relais_local_v1` `d365affc…`, `porte_plafond_relais_v1` `fab5fe2e…`, `relais_reel.py` `1b90b020…`, `relais_kimi_v4` `67f36951…`, `relais_gemini_v2` `2b0043bc…`, enveloppe `37c0205e…`, Carbon `9484dce0…` et `543e728d…`) ; les commandes d'essai du § 1 rendent exactement l'attendu (201 ; 240 et 1 désélectionné).
- **Lanceur v4** : il épingle l'additif v2d et exige qu'il cite le préenregistrement, l'additif v2c et le programme d'épreuve v4 (`verifier_additif`, l. 744-765) ; la contre-lecture doit citer l'additif v2d et le lanceur (l. 786-808) ; `recalculer_verdict_epreuve` (l. 912-929) applique la lecture gelée puis `qualifier_verdict` du programme épinglé ; la course ne part que sur « réussie ». Essai à blanc versé : code 0, moteur simulé, 88 cartes à passeport, acte de gel et manifeste citent `cb4d44d0…` et `b1661f11…`, borne de relais d'Argon 376 pour 187 appels (Kimi factice) ; épreuve hors ligne v4 : « témoins éprouvés hors ligne », 0 juge au hasard réussi sur 2 000, programme `04f62b8c…`.
- **Rien d'autre ne change** : les diff v3 → v4 (353 et 311 lignes) ne touchent que ce que l'additif v2d § 4 déclare (chemins neufs v4, sonde du bac, borne doublée, incidents techniques, GO-36 et budget, additif v2d épinglé, suffixes v3 dans « une seule course ») ; témoins, consignes, configuration, matière, seuils, plafonds (5 et 90 USD), composition et devis sont inchangés ; les mêmes 33 appels dans le même ordre.

## 3. Mutations (copies hors dépôt, dans mon dossier de travail ; aucun fichier du dépôt touché)

| mutation | original | mutant | attrapée |
|---|---|---|---|
| K1 `STATUTS_TECHNIQUES = ("erreur", "refus")` dans l'épreuve ; un adaptateur factice rend « refus » sur les 11 témoins | « échouée » | « non conclue » | oui |
| K2 `APPELS_RELAIS_PAR_APPEL_GEMINI = 1` dans le lanceur ; relais d'Argon à `--max-appels 280` pour 231 appels, arguments lus par un faux PID, état factice neuf | refusé (464 requis) ; accepté à 464 | accepté (233 requis) | oui |
| K3 `verifier_borne_argon` ne lit plus la borne de `/relais/etat` ; arguments à 24, état à 15 | refusé | accepté | oui |
| K4 `manques_par_sorte` tient tout manque « absent » pour technique sans incident consigné ; tentative v3 sans aucun incident | « échouée » | « non conclue » | oui |

Les mutations propres aux essais du développeur (bac sans exigence, sonde retirée, borne divisée par deux, borne non doublée, requalification trop large ou absente, garde du rapport retirée, période de GO-36 ignorée, tentative non retranchée, borne d'Argon non doublée et Carbon non doublé dans le lanceur, recalcul sans requalification) sont présentes dans les deux fichiers d'essais et passent.

## 4. Constats

Aucun bloquant, aucun majeur.

| gravité | fichier | lignes | constat et preuve | correction |
|---|---|---|---|---|
| mineur | `additif-…-v2d.md` ; `commandes-…-v2d.md` ; `rapport-developpeur-correctif-v2d.md` ; `epreuve_temoins_auto_conception_v4.py` | additif l. 9 et 42 ; commandes l. 3, 77, 110 ; rapport l. 25 ; épreuve l. 588-591 | Les pièces disent « reprise unique » d'après `GO-2026-11-18-36` ; le registre sur `main` (commit `3e07d0d1`) porte aussi `GO-2026-11-18-39` (ligne de forme de la 36 : reprises permises tant que l'échec est technique, arrêt définitif sur un verdict autre que « réussie » rendu avec les verdicts réels de tous les juges, 5 USD au total). Le programme v4 est plus strict que ce que la 39 permet (une seule reprise à son chemin) : aucune dépense ni aucun écart possibles au-delà de la 36, rien à corriger pour cette épreuve. | Aucune pour le v4. Si le v4 rend « non conclue », la reprise suivante demande un programme v5 (chemin neuf, dépenses v3 et v4 retranchées des 5 USD) et un additif qui cite `GO-2026-11-18-39` ; la mention « reprise unique » des commandes vaut pour cette version seulement. |
| mineur | `epreuve_temoins_auto_conception_v4.py` ; `pole/adaptateurs.py` ; `commande_argon_v3d.py` | épreuve l. 129, 535-553 ; adaptateurs l. 751-760 ; commande l. 317-320 | Le statut « erreur » d'une commande externe couvre toute sortie en code non nul ; pour Argon, cela comprend les codes 4 (pire cas au-dessus du plafond, rien envoyé), 5 (réponse non conforme ou vide) et 8 à 11 (usage incohérent). Une réponse vide de Gemini devient donc un manque technique (« non conclue ») et non un échec de lecture, alors qu'une réponse « ok » illisible reste un échec. Cohérent avec la lettre de `GO-2026-11-18-39` (« jugements manquants » = technique) et traçable : le motif court de chaque incident est écrit dans `incidents_techniques`. | Aucune dans le code. Le rapport de l'épreuve v4 se lit avec son champ `incidents_techniques` : un code 5 d'Argon y est nommé et la mère juge s'il relève de la technique. |
| mineur | `lancer_course_auto_conception_v4.py` | l. 1206-1214 | La borne de Carbon est lue dans `/relais/etat` seulement (pas dans les arguments du PID) et seulement si `max_appels` et `max_lots` y sont des entiers ; héritage des v2 et v3, hors du périmètre du correctif. En pratique l'état de `relais_gemini_v4.py` porte `max_appels` et `max_lots` (l. 276-278), donc la garde agit. | Aucune pour le v2d ; à durcir (lecture des arguments `--max-appels`, `--max-lots` par PID) dans une version ultérieure du lanceur. |
| mineur | commandes v2d § 5 | l. 83, 95 | Le relais Claude de l'épreuve est lancé à `--plafond-usd 5` et la porte à `--plafond-ligne 5`, alors que le budget de la reprise est 4,867711 USD : le total « 5 USD, tentative v3 comprise » est tenu par la vérification avant chaque appel (cumul + plafond de session ≤ budget, l. 719) et par le plafond de session du kit ; le plafond du relais n'est qu'une garde de dernier ressort. Le lanceur exige d'ailleurs que le relais Claude soit au plafond de la ligne exactement (`controler_relais_vivant`, l. 1145). | Aucune ; remarque. |
| mineur | message du développeur (hors dépôt) | — | Le message dit « 46 fichiers A » ; le commit `63ca624f` en compte 44, tous « A ». Le rapport scellé du développeur ne donne pas ce nombre. | Aucune. |

Ce que je n'ai pas joué, comme le développeur : aucun appel réel (bac du kit en marche réelle, relais aux bornes 24 et 464, porte avec 4,86 USD). Le pire cas de 231 appels d'Argon suppose que le noyau ne refait aucun appel ; recherche de mots (`tentative`, `retry`, `relanc`) dans `adaptateurs.py`, `adaptateurs_v56.py`, `noyau_v56.py`, `course2_v56.py` : rien, sans preuve formelle ; la marge de 2 ne couvre qu'un jugement.

## Verdict

Scellable.

Sans bloquant ni majeur : les deux causes de la tentative v3 sont refusées avant tout appel ; la lecture gelée est identique à l'octet ; la requalification « non conclue » est bornée aux manques techniques et ne transforme jamais un verdict de juge lu et faux ; la borne d'Argon de la course compte deux appels de relais par appel (464) ; aucun écart au-delà de l'additif v2d ; aucune dépense possible hors 5 et 90 USD ni sans `GO-2026-11-18-20`, `-21` et `-36` ; commandes v2d exécutables telles qu'écrites ; pièce de départ, sonde d'Astra et relevé des prix repris tels quels ; R12 tenu. Les cinq constats mineurs ne demandent aucune correction avant l'épreuve v4.
