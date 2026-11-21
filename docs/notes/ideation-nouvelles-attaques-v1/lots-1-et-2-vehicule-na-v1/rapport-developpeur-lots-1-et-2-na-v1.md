# Rapport du développeur — véhicule NA-1, lots 1 (tirage) et 2 (garde de motifs) — v1

- Développeur des lots 1 et 2 du véhicule NA-1, modèle O. Je n'ai écrit ni la conception, ni le relevé du lot 0, ni aucun orchestrateur.
- Date (UTC) : 2026-11-21 ; essais finaux lancés à 08:23:08Z (`date -u`).
- Processeur seul : aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucun relais lancé, aucune écriture dans un dépôt, aucun commit. **Essais sur données factices seules** : gabarit factice, racine factice, liste de motifs d'essai. Le tirage réel n'a pas été joué.
- Aucun refus de permission, de classifieur ni de garde rencontré.
- Mandat : `docs/notes/ideation-nouvelles-attaques-v1/mandat-developpeur-vehicule-na-lots-1-et-2-v1.md`, `67e7d456752203c415612840ef81ae39c6adeb3336c6a85628cdce6e9211707a`, égal à son compagnon, lu en entier ; départ sur le mot de la mère (08:04Z) transmis par la coordination.

## 1. Pièces lues (empreinte égale au compagnon, recalculée)

| pièce | empreinte |
|---|---|
| conception v4 (CO4), lue en entier | `3428dfb348c8f367060f587b5953d3c05ed329055f29b07e046ac3538ced2804` |
| contrôle de la conception v4, lu en entier : « les lots 1 à 5 ne touchent ni A3 ni les points de 08:00Z » | `3fda0db5e37f1bb97c94f93fdd6ec61576dbfb8b2b35171ad093d2b7c803c381` |
| V9, `origin/main` (l. 1 à 396 lues) | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` |
| additif 1 v5 (A1), l. 1 à 189 | `9f731795cd8b9166ad8b78346e3d37c7352010ea0edd1f34ac86cfb0ac689200` |
| complément de valeurs v3 (CV) : recherche « clé », « tirage », « identifiant » ; il n'ajoute aucune valeur au tirage (l. 185) | `b4ef87dc6d5cce138f76457771c4cff18b84dfde662916841fc6386d77e202b2` |
| additif au complément v2 (AC) : même recherche, rien sur le tirage | `ce76e0d6a0a6e65ffb99f68d9efced8d26e205ed0e2cf11c0e2469b69f672388` |
| partie servie (gabarit), lue en entier, jamais passée au programme | `4cd360baea1076ec2b19b2c7ba85675e739bc3104c709d4fd57c0769975b1cf1` |
| relevé du lot 0 (L0) : recherche « Q6 », « identifiant », « hexad » | `10ac79ecb0e064f5b5ea80ddb060ae37e303d2d84ff242f653f4cccbd7ff753e` |
| rapport du développeur de la v68 (R68), son manifeste, l'arbre du paquet, la classe des mutations de ses essais | tirés de `origin/main` par `git show` redirigé |
| orchestrateur, commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` : `orchestrator/pole/__init__.py` (`f7341b96…`), `orchestrator/essais/conftest.py` (`c60e041d…`) | lus ; arbre propre après (`git status --porcelain --ignored` vide) |

La question n'est jamais ouverte. Aucune branche de quarantaine ni de matière première n'est ouverte.

## 2. Livré

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-vehicule-na-lots-1-2/`. Chemins du paquet : `paquet/orchestrator/…`, comme la v68.

| fichier neuf (chemin dans l'orchestrateur) | lot | lignes | sha256 |
|---|---|---|---|
| `orchestrator/pole/identifiants_na_v1.py` | 1 | 147 | `38d9860b7535e24b5ba707560f9dd5c4a27acc6e5632e453308a3fd2b93909dd` |
| `orchestrator/pole/tirage_na_v1.py` | 1 | 462 | `94c5cb9de5c6cdd95130e5c634678fb84e5088c280b63bcc803a5471ef40aa11` |
| `orchestrator/pole/garde_motifs_na_v1.py` | 2 | 304 | `7c9127eea021d8c38574d5429f9a956fa0805271cf0e22db6e97b5e22a190614` |
| `orchestrator/essais/aides_na_v1.py` | 1, 2 | 94 | `db5377b218d2d63c0325c658afba339f6a9e249d25505e1e5256e7777dc5e3a2` |
| `orchestrator/essais/liste-motifs-essai-na-v1.json` (liste d'essai, factice) | 2 | 20 | `41a50329f67c41d073115a75ae64981fd59a46b4663c269f42a32b4055c0508b` |
| `orchestrator/essais/test_na_v1_tirage.py` | 1 | 538 | `0ff0cc61e92b460cd8b323aa50f9666b2d0f66289e48b74fb089d4d4a49460f5` |
| `orchestrator/essais/test_na_v1_garde_motifs.py` | 2 | 256 | `909ff36586ff07074a748b13b22bef90fe25613669edfd60ceb2296dff441e2e` |
| `orchestrator/essais/mutations_na_v1.py` | 1, 2 | 279 | `5599668f8a5b6757737cf1ac3d954e1b1ec4d388eeb9c7bf44f0b1a3489acdc9` |

Hors du paquet : `manifeste-paquet-vehicule-na-lots-1-2-v1.json` (chemin, empreinte, octets, lignes, rôle de chaque fichier ; commit de base ; fichiers existants lus ; aucun modifié) ; `appliquer_paquet_vehicule_na_lots_1_2_v1.py` (vérifie les empreintes du paquet, refuse le dépôt de l'orchestrateur comme destination, refuse une cible présente, copie, relit chaque copie, `--lancer-essais`) ; `journal-essais-na-lots-1-2-v1.txt` ; `journal-mutations-na-lots-1-2-v1.json` ; ce rapport ; la table d'empreintes du dossier ; un compagnon `.sha256` par fichier.

Aucun fichier du paquet n'importe un module existant de l'orchestrateur ; `tirage_na_v1` importe `numpy` (R9), les deux autres modules la bibliothèque standard seule.

## 3. Ce que la conception exige, et où le code le fait

### Lot 1 — `tirage` (CO4, § 2.1, § 5.2, § 6.1, § 6.2, § 7)

| exigence (citation) | lieu | code | essai |
|---|---|---|---|
| « lit la légende des trois axes dans le gabarit de la partie servie, à l'octet (jamais dans la question) » ; « le gabarit à son empreinte » | § 2.1 | `pole/tirage_na_v1.py:139` (`lire_legende` : empreinte, nom et empreintes de la question refusés, table unique, 6/5/4 valeurs, « autre, à nommer » au rang 5) | `TestLegende` (7) |
| « la racine écrite, jamais recalculée » ; « racine recalculée sur une autre empreinte : refus » | § 2.1 ; § 6.2 | `tirage_na_v1.py:42`, `:128` | `TestRacineEtNumpy` |
| « la version de `numpy`, refusée sous 1.25 » | § 2.1 ; § 6.2 | `tirage_na_v1.py:117` | `test_numpy_sous_1_25_refuse` |
| « forme les 120 triplets dans l'ordre canonique ; tire la clé 0, puis les clés 1, 2, 3 » (V9, l. 300 à 307) | § 2.1 | `tirage_na_v1.py:177`, `:214`, `:218` | `test_tirages_recalcules_a_part`, `test_comptes_et_partition` |
| « tire la clé 30 parmi les seules cases servies dont la menace du programme est le sabotage, ou ne tire rien s'il n'y en a aucune » ; « une demande de second tirage : refusée » | § 2.1 ; § 6.2 ; A1, l. 79 à 82 | `tirage_na_v1.py:234` (`tirer_cle_30`), `:208` (`_rng`, une fois par clé) | `test_cle_30_cas_sain`, `test_cle_30_aucune_case_de_sabotage_rien_n_est_tire`, `test_cle_30_second_tirage_refuse` |
| « la clé n° 40 … tirée au même geste que les autres, par le même programme, et consignée » ; `rng.choice(216000, size=120, replace=False)` | § 5.2 ; § 0 bis, 07:21Z, règle 3 | `tirage_na_v1.py:251`, `:265` (`jouer` : 0, 1, 2, 3, 30, 40 dans un seul appel), sortie `cles` et `cle_30` | `test_cles_30_et_40_au_meme_geste_et_consignees`, `test_cle_40_mots_de_case` |
| « chaque mot passe la garde de motifs avant le scellement ; un mot qui la ferait refuser arrête le tirage par un refus nommé, sans second tirage en silence » | § 5.2 ; § 6.2 | `tirage_na_v1.py:251` à `:260` | `test_cle_40_mot_refuse_arrete_le_tirage_sans_second_tirage`, `test_garde_exigee` |
| « désigne la première case de la réserve » | § 2.1 ; V9, l. 313 | sortie `reserve` (`tirage_na_v1.py:276`) | `test_comptes_et_partition` |
| « expose, pour la course, les tirages des clés 12, 13 et 20 » | § 2.1 | `tirage_na_v1.py:393`, `:401` | `TestClesDeLaCourse` |
| « un seul fichier, octets déterministes (clés triées, fins de ligne fixes, aucune heure) … L'heure et le commit vont au manifeste, à part » | § 2.1 | `tirage_na_v1.py:300` (`serialiser`), `:416` (`main` : sortie et manifeste, jamais par-dessus) | `test_rejoue_deux_fois_egal_a_l_octet`, `test_rejoue_dans_deux_processus_egal_a_l_octet`, `test_sortie_deterministe_sans_heure`, `TestProgramme` |
| C1 : « aucune case servie deux fois ; trente-trois cases servies ; aucune case de la famille tenue à l'écart servie » | V9, l. 158 | `tirage_na_v1.py:305` | `TestC1` (4) |
| ligne de case : « trois valeurs égales à l'octet à la légende, identifiants distincts, aucune suite de huit caractères hexadécimaux, aucun chiffre, borne de 256 octets » ; artefacts : « une valeur qui diffère d'un octet ; un identifiant numéroté sur un total ; huit caractères hexadécimaux de suite » | § 2.2 ; § 5.2 ; § 6.2 ; V9, l. 75 | `tirage_na_v1.py:182`, `:187`, `:327`, `:355` | `TestLigneDeCase` (7) |
| arrêt n° 10 (premier temps) : « une case de cette famille, puis une case déjà servie, plantées dans une copie du tirage : départ refusé » | § 6.1 ; V9, l. 381 | `tirage_na_v1.py:366` (`garde_disjonction`) | `TestArretDisjonction` (5) |
| réencodage (« alphabet, ordre des octets, base 60 à longueur fixe, 18 et 14 lettres, décodage qui refuse ») ; « éprouvée dans les deux sens » ; « mutation ordre des octets inversé » | § 5.2 ; § 6.2 ; mot 1 de 07:46Z | `pole/identifiants_na_v1.py:25` à `:143` | `TestIdentifiants` (12) |

### Lot 2 — `garde_motifs` (V9, arrêt n° 16 ; CO4, § 2.3, pas 3 ; § 6.1 ; § 7)

| exigence (citation) | code | essai |
|---|---|---|
| « lit la requête assemblée au dernier point avant l'envoi : après elle, plus aucun octet ne change, et l'empreinte journalisée est celle de ce qu'elle a lu » | `pole/garde_motifs_na_v1.py:264` (copie, lecture de la copie, `RequeteGardee` figée), `:277`, `:285` | `TestDernierPointAvantEnvoi` (5) |
| « Deux familles de motifs, gelées par l'empreinte de leur liste et de leur programme » | `garde_motifs_na_v1.py:48`, `:157` (empreinte, format strict), `:301` | `TestFormatDeLaListe` (12) |
| « normalisé avant la comparaison (forme Unicode de compatibilité, casse repliée, espaces et tirets ramenés à une seule forme, caractères invisibles retirés) » | `garde_motifs_na_v1.py:92` | `TestNormalisation` (2) |
| « Chaque motif a un témoin positif … rejoué à chaque départ » ; « un motif qui ne mord pas sur son témoin positif refuse le départ » | `garde_motifs_na_v1.py:233`, `:243` | `TestTemoinsPositifs` (3) |
| « l'envoi est refusé, et l'arrêt est nommé : il dit la famille et le rang du motif ; le texte trouvé n'est écrit qu'au journal ; aucun retrait silencieux » | `garde_motifs_na_v1.py:71`, `:258`, `:293` | `TestArret16ParFamille` (6), `test_une_requete_qui_porte_un_motif_refusee_avant_l_envoi` |
| épreuve par famille : cas sain, puis un motif planté « en clair puis sous une forme que la normalisation doit ramener » | — | `TestArret16ParFamille` : deux familles × (clair, forme ramenée) |
| « un appel sans ligne ne part pas » (CO4, § 2.3, pas 4) | `garde_motifs_na_v1.py:296` | `test_ligne_de_journal_qui_ne_s_ecrit_pas_rien_ne_part` |

Le format de la liste (`liste-motifs-na-v1`) est écrit dans l'en-tête du module (`garde_motifs_na_v1.py:21` à `:38`) : JSON, deux familles nommées à la lettre de V9, l. 387, dans cet ordre ; par motif `rang` (1, 2, 3… sans trou), `type` (« litteral » ou « expression_reguliere »), `motif`, `temoin_positif` ; aucune clé en plus, aucune en double, aucune famille vide. Le premier constat rendu suit l'ordre des familles puis des rangs.

## 4. Essais

`/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -v -p no:cacheprovider …/paquet/orchestrator/essais` (Python 3.13, numpy 2.4.6, pytest 9.1.1) : **83 passés, 0 échec** — lot 1 : **55** ; lot 2 : **28** (journal `journal-essais-na-lots-1-2-v1.txt`). Rejoués après application du paquet par son programme dans une copie neuve du dossier `orchestrator` du commit `a41b7b50…` (hors de mon dossier, sous le `conftest.py` de l'orchestrateur, `pole` paquet régulier) : **83 passés**. Le programme d'application, rejoué sur la même copie : refus « cible déjà présente (R12) » ; sur le dépôt de l'orchestrateur : refus « destination dans le dépôt » ; dépôt propre après.

Ce que le mandat demandait, un par un : arrêt n° 10 (premier temps) : 5 ; ligne de case : 7 ; tirage rejoué deux fois égal à l'octet : en processus et dans deux processus à graine de hachage différente ; clé n° 30 sans case de sabotage (rien n'est tiré : la clé 30 n'est jamais passée à `SeedSequence`) ; clé n° 40, mot refusé (la clé 40 tirée une fois) ; encodage aller et retour sur 3 000 valeurs tirées par longueur (`SeedSequence`, entropie d'essai, non la racine de la course), plus 2 000 en sens inverse ; refus d'une chaîne hors alphabet (lettre hexadécimale, majuscule, chiffre) ; aucune suite de huit chiffres hexadécimaux dans un mot encodé (sur l'échantillon, et pour tout couple de syllabes : la plus longue suite possible fait un caractère) ; arrêt n° 16 par famille, cas sain et artefact ; une requête assemblée qui passe ; une qui porte un motif, refusée au dernier point ; aucun octet changé après la garde.

## 5. Mutations

`python -B paquet/orchestrator/essais/mutations_na_v1.py JOURNAL` : chaque mutation copie les seuls fichiers des lots 1 et 2, retire une garde par remplacement à texte exact (texte présent une fois exactement, sinon « invalide »), joue les essais de cette garde dans un processus à part ; « tuée » si et seulement si pytest rend le code 1. **42 mutations, 42 tuées** (lot 1 : 25 ; lot 2 : 17) ; témoin non muté : les 41 essais visés (distincts) passent ; **témoin inerte** (un mot de docstring changé) : survit, comme attendu — le programme sait dire « non tuée » (R4). Journal : `journal-mutations-na-lots-1-2-v1.json`, qui porte l'empreinte des fichiers mutés.

Gardes retirées, lot 1 : racine ; numpy ; empreinte du gabarit ; nom et empreinte de la question ; arrêt n° 10 (famille, déjà servie, écart au tirage scellé) ; clé 30 (filtre sabotage, « aucune ») ; second tirage ; clé 40 (mot refusé, garde exigée) ; ligne de case (valeurs, hexadécimal, chiffre, identifiant décodé, doublon, borne) ; C1 ; ordre des octets inversé ; borne, alphabet et longueur du décodage ; forme du jeton du noyau. Lot 2 : normalisation entière ; invisibles ; forme de compatibilité ; casse ; tirets ; espaces ; chaque famille ; témoins positifs ; copie défensive ; empreinte de la liste ; accord vide ; famille vide ; texte trouvé dans le message ; envoi avant journal ; ligne « non envoyé » ; requête non examinée.

## 6. Ce que la lettre ne fixe pas (remarques ; rien n'est tranché ici)

1. **Lot du réencodage.** Le mandat met l'encodage au lot 1 ; CO4 le range au lot 5 (§ 5.1, ligne `identifiants` ; § 7). Il est écrit en module à part, `identifiants_na_v1` ; le lot 5 l'importe.
2. **Du rang au mot de case.** CO4, § 5.2, fixe le tirage (`choice(216000, …)`) et l'alphabet, non l'écriture d'un rang en trois syllabes. J'applique les points 1 et 3 de la règle (base 60, chiffre fort d'abord) : à écrire à l'additif.
3. **Ordre des onze cases d'une génération** : celui que rend `choice` (ordre du tirage). Ni V9 ni CO4 ne le disent ; il compte pour la copie de configuration par génération (lot 6).
4. **Clé 30.** « Cases servies » lu comme les trente-trois des trois générations, rangées ensemble en ordre canonique (A1, l. 79). La menace « sabotage » est reconnue par sa place (valeur 0 de l'axe « menace du programme ») et vérifiée par le préfixe « sabotage » de la légende : valeur du développeur.
5. **Ligne de case** : la forme `case : <identifiant> ; <v1> ; <v2> ; <v3>` est la proposition du concepteur (§ 5.2), non encore fixée par l'additif (constantes `PREFIXE_LIGNE`, `SEPARATEUR_LIGNE`). « Aucun chiffre » vient de CO4, § 2.2, non de V9.
6. **Normalisation**, « espaces et tirets ramenés à une seule forme » : lu comme deux formes (une espace ; « - »), non une forme commune aux deux ; l'autre lecture rendrait « a-b » égal à « a b » et ôterait à la liste le moyen de les distinguer, alors qu'une expression régulière peut toujours les unir. Les fins de ligne sont des espaces. L'ordre des opérations est de moi (§ 3).
7. **Format de la liste** (deux types de motif, ordre du premier constat, refus des expressions à accord vide, clés strictes) : valeur du développeur, à contre-lire avec le véhicule et à suivre par la rédaction de la liste réelle.
8. **Texte trouvé** : celui du texte normalisé, non les octets d'origine.
9. **Le mot de case passe la garde seul** (§ 5.2) ; la ligne entière passe avec la requête (lots 3 et 4).
10. **Clé 20** : pour n ≤ 60, tous les rangs, sans tirage ; au-delà, l'ordre rendu est celui du tirage.
11. **Le gabarit réel n'est pas passé au programme** dans mes essais : la lecture de la légende est éprouvée sur un gabarit factice de même forme (mêmes noms d'axes, même séparateur, une valeur à virgule, une à parenthèses). Le premier jeu de la session la vérifie ; une forme différente y est un refus nommé. `plus_longue_ligne_possible` donne la mesure que CO4, § 5.2, demande pour la borne de 256 octets.
12. **Le programme du tirage exige la liste des motifs**, sans défaut : le jeu scellé attend la liste réelle (CO4, § 7, lot 1, « pour le jeu scellé : la liste des motifs scellée »).
13. **Programme d'application** : il ne clone pas la source (la v68 le faisait) ; la copie est donnée par l'opérateur.

## 7. Interface que recevront les lots 3 et 5

**Sortie du tirage** (`serialiser(sortie)`, JSON trié) : `generations["1"|"2"|"3"]` = onze `{"triplet": [i, j, k], "identifiant": mot, "ligne": ligne de case}` ; `reserve` = `{"compte", "premiere": {…}, "cases"}` ; `famille_tenue_a_l_ecart` ; `cle_30` = `{"n", "rang", "case"}` (« aucune » si n = 0) ; `identifiants` (120) ; `legende` ; `controles_C1` ; `gabarit_sha256`, `liste_motifs_sha256`, `racine`, `numpy`, `cles`.

**Lot 3 (`requete`, `journal`)**
- `tirage_na_v1.lignes_du_tirage(sortie)`, `ligne_de_case(identifiant, triplet, legende)`, `controler_ligne_de_case(i, triplet, ligne, legende)` (lève `LigneDeCaseRefusee(indice, cause)`), `controler_lignes_de_case(lignes, legende)`, `plus_longue_ligne_possible(legende)`.
- `garde_motifs_na_v1.charger_liste_motifs(chemin, empreinte)` → `GardeMotifs(liste)` (témoins rejoués ; `TemoinPositifManque(famille, rang)`) ; `.garder_requete(octets)` → `RequeteGardee(octets: bytes, sha256, taille)`, seuls octets à envoyer ; `.garder_texte(str)` ; `.examiner(str)` → `Constat(famille, rang, texte_trouve)` ou `None` ; `verifier_avant_envoi(requete_gardee, octets)` (`EcartApresGarde`) ; `envoyer_apres_garde(garde, requete, envoyer, journal, meta)` : `journal(dict)` reçoit `{"evenement": "envoi", "taille", "sha256", **meta}` avant l'envoi, ou `{"evenement": "non envoyé", "arret": 16, "famille", "rang", "texte_trouve", **meta}` puis `ArretMotifInterdit(famille, rang, texte_trouve)` (message sans le texte) ; `RequeteIllisible` ; `empreinte_programme()`.
- Pour le lot 6 : `garde_disjonction(tirage, generation, cases_a_servir=None)` (`ArretDisjonction`, numéro 10, `cause`).

**Lot 5 (`identifiants`, `registre`, `portier`, `verifier_registre_servi`)**
- `identifiants_na_v1.encoder_identifiant_fiche(6 octets)` (18 lettres), `encoder_identifiant_juge(5 octets)` (14 lettres), `reencoder_jeton_noyau(jeton, prefixe, n_octets)` (jeton du noyau : préfixe puis 2n caractères hexadécimaux minuscules ; L0, l. 24 et 232), `decoder_octets(mot, n_octets)` (`MotRefuse.cause` ∈ « pas une chaîne », « longueur », « hors alphabet », « entier au-delà de la borne »), `porte_suite_hexadecimale(texte)`.
- `tirage_na_v1.permutation_registre(generation, n)` (clés 12 et 13) pour l'ordre du registre servi ; `part_anteriorite(n)` (clé 20, lot 7).
- La garde de motifs sur le registre servi : `GardeMotifs.garder_texte` ou `garder_requete`.

## 8. Écarts et réserves

1. **Commandes de liste hors de mon dossier**, contraires à l'en-tête du mandat : un `git ls-tree --name-only origin/main prereg/ideation-nouvelles-attaques-v1/` (sortie à l'écran) ; deux `git show origin/main:<dossier>/` qui rendent un arbre (redirigés vers mon dossier). Rien d'autre n'a été listé ; les sorties nomment des fichiers du dépôt, sans contenu.
2. `git fetch` a rapatrié des références de branches, dont celle de la matière première : elle n'est pas ouverte.
3. La copie du dossier `orchestrator` (`cp -a`, sans `.git`) vit dans le bloc-notes, hors de mon dossier : `…/scratchpad/copie-orchestrateur-na-lots-1-2/`. Elle n'est pas un dépôt.
4. Le dossier `sources/` (pièces tirées de `origin/main` pour lecture, empreintes au § 1) est retiré avant la table d'empreintes : il ne fait pas partie du livrable.
5. Je n'ai pas lu le registre des décisions ni celui des accords ; les mots de la mère sont ceux que portent CO4 et son contrôle.

— développeur des lots 1 et 2 du véhicule NA-1, modèle O
