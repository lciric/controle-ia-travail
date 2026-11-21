# Rapport du développeur — véhicule NA-1, lot 3 (requête et journal) — v1

- Développeur du lot 3 du véhicule NA-1, modèle O. Je n'ai écrit ni la conception, ni les lots 1 et 2, ni aucun orchestrateur.
- Date (UTC) : 2026-11-21 ; runs finaux lancés à 09:15:06Z (`date -u`).
- Processeur seul : aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucun relais lancé, aucune écriture dans un dépôt, aucun commit. **Essais sur données factices seules.** Aucun refus de permission, de classifieur ni de garde rencontré.
- Commandes de liste : seulement dans mon dossier et dans celui des lots 1 et 2. Toute autre pièce est ouverte par son chemin complet ; `git show` toujours redirigé vers mon dossier, sur `origin/main`. Ni `git ls-tree`, ni `git fetch`.

## 1. Pièces lues (empreinte recalculée, égale au compagnon)

| pièce | empreinte | lecture |
|---|---|---|
| mandat du lot 3 | `6a494f65eced290eaf8f1034202d6177cab82ee3ccdddb1adfc4acf1866d1ea3` | entier |
| conception v5 (CO5), qui prime | `1b7f6822af20417e997b80290f05e7a4d70aa69c3d65f4139b5b3673cd98a863` | entière |
| contrôle de la v5 | `4b369004733fb4c55bb75deaeac19c4cc4e5dacaa8604f8082f63096c2956156` | entier |
| conception v4 | `3428dfb348c8f367060f587b5953d3c05ed329055f29b07e046ac3538ced2804` | empreinte seule (la v5 prime et la contient) |
| V9, `origin/main` | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` | l. 55 à 99, 154 à 158, 250 à 256, 314 à 316, 370 à 390 |
| partie servie (gabarit), `origin/main` | `4cd360baea1076ec2b19b2c7ba85675e739bc3104c709d4fd57c0769975b1cf1` | entière ; finie par un seul « \n » |
| relevé du lot 0 (L0) | `10ac79ecb0e064f5b5ea80ddb060ae37e303d2d84ff242f653f4cccbd7ff753e` | Q1, Q6, Q7, Q8, Q13, Q14, « contredit », « D2 » |
| lots 1 et 2 : table | `4ba408af7d9e362c885c7b741db47860c16b6ee9a60216a778d752dbc00dedac` | treize fichiers recalculés, tous égaux |
| lots 1 et 2 : rapport v2 | `21676fada803abc65f76814dcce5de9d9f9b2b870884203c6ff5370f7c378943` | entier ; et le rapport v1 (`960845db…`), son § 7 (interface) |
| lots 1 et 2 : vérification | `674996b42d7cac9d6fa41a4a79077ff244dad01b9537eb8515a283a0fd969423` | entière |
| lots 1 et 2 : code | `garde_motifs_na_v2.py`, `tirage_na_v2.py`, `identifiants_na_v1.py`, `aides_na_v2.py`, `mutations_na_v2.py`, programme d'application, manifeste | entiers |
| orchestrateur, commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, arbre propre avant et après | `pole/fiches_v54.py` (`1ab0796d…`, entier), `pole/fiches_v53.py` (`vue_servie`), `pole/noyau_v56.py` (`eb5a003e…`, l. 140 à 219), `pole/noyau_v54.py` (`servir`, `piece`), `pole/configuration_v53.py` (`texte_piece`), `pole/__init__.py`, `essais/conftest.py` | comme dit |

La question n'est jamais ouverte. Aucune branche de quarantaine ni de matière première n'est ouverte. Les deux pièces tirées de `origin/main` (V9, partie servie) ont été retirées de mon dossier après usage.

## 2. Livré

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-vehicule-na-lot-3/`. Chemins du paquet : `paquet/orchestrator/…`, comme la v68 et les lots 1 et 2.

| fichier neuf (chemin dans l'orchestrateur) | lignes | sha256 |
|---|---|---|
| `orchestrator/pole/requete_na_v1.py` | 511 | `4dfd3eecd0980640fb5b9c3c1e1e071c236ff1e44cd0776769790bf8184c4810` |
| `orchestrator/pole/journal_na_v1.py` | 364 | `8424062363b1ad9b2b63a30c2e6c4184da880ef8c859b0d6a15a24c9b1817e1f` |
| `orchestrator/essais/aides_na_lot3_v1.py` | 94 | `dceb3ca99f0918f531db4359f52828ea8d44e2fb96586cdf0f49870f3dadafd4` |
| `orchestrator/essais/test_na_v1_requete.py` | 430 | `cbc8df87050249ba6a25efb095a8669d8b1d0998d4cff9baadf845a95f425b6d` |
| `orchestrator/essais/test_na_v1_journal.py` | 405 | `006f9f00220de6af6cf0eaddb3b3960a53481361aab15e7a17ce2bd026cb032d` |
| `orchestrator/essais/mutations_na_lot3_v1.py` | 361 | `e736124752a1c1796e141f6df6feb31cce930f91e7cf8861ce3c286bc3b0577f` |

Hors du paquet : `manifeste-paquet-vehicule-na-lot-3-v1.json` (chaque fichier, empreinte, octets, lignes, rôle ; les sept fichiers des lots 1 et 2 dont il dépend, à leurs empreintes ; six fichiers existants lus ; aucun modifié) ; `appliquer_paquet_vehicule_na_lot_3_v1.py` ; `journal-essais-na-lot-3-v1.txt` ; `journal-mutations-na-lot-3-v1.json` ; `sonde_gabarit_servi_na_lot3_v1.py` et `journal-sonde-gabarit-servi-na-lot-3-v1.json` (§ 4) ; `ecrire_compagnons_na_lot3_v1.py` ; ce rapport ; la table d'empreintes ; un compagnon `.sha256` par fichier. La copie d'application `copie-orchestrateur-application/` (orchestrateur du commit de base, lots 1 à 3 posés par leurs programmes) reste dans le dossier ; elle n'est pas un dépôt et n'est pas dans la table.

Les modules du paquet n'importent que la bibliothèque standard et les modules des lots 1 et 2. Seuls les essais importent un module existant : `pole/fiches_v54.py`, comme témoin de la forme déclarée.

## 3. Exigences, et où le code les tient

### Module `requete` (CO5, § 2.2, § 5.3 ; mandat, point 1)

| exigence (citation) | lettre | code | essai |
|---|---|---|---|
| « charge le gabarit, vérifie son empreinte, exige un seul emplacement sur une ligne propre » | § 2.2 ; V9, l. 71 | `requete_na_v1.py:165` (`_verifier_emplacement`), `:175` (`charger_gabarit`), `:188` (`lire_gabarit`) | `TestGabarit` (8) |
| « le chemin de la question donné à la place du gabarit est refusé par son empreinte et par son nom » ; « aucun programme n'ouvre la question » | § 2.2 ; V9, l. 71 | `:150` (nom, **avant toute ouverture**), `:155`, `:175` (empreintes de la question, reprises du lot 1) | `test_question_refusee_par_son_nom_avant_toute_ouverture` (chemin absent : refus par le nom, jamais `FileNotFoundError`), `test_question_refusee_par_son_empreinte` |
| empreinte de chaque pièce servie (arrêt n° 14, refus qui nomme la pièce) | V9, l. 385 | `:91`, `:137` (`charger_piece`) | `test_empreinte_differente_refusee_en_nommant_la_piece`, `test_consigne_a_une_autre_empreinte_refusee` |
| « partie servie remplie par la ligne de case du lot 1 » ; « le remplace par la ligne de case » | mandat ; § 2.2 | `:215` (`cases_du_tirage` : tirage joué sur ce gabarit, même légende, 34 lignes contrôlées par `tirage_na_v2.controler_lignes_de_case`) ; `:232` (`remplir_partie_servie` : contrôle du lot 1, ligne rebâtie de l'identifiant et du triplet, un seul encodage, l'emplacement seul remplacé) | `TestPartieServie` (7), dont `test_partie_servie_a_l_octet` |
| enveloppe **sans ajout** (D2) : « partie servie remplie ; une ligne vide ; synthèse servie à l'octet » ; aux générations 2 et 3, « une ligne vide ; le titre de la section du registre, sur une ligne ; le registre servi » ; registre vide, section omise ; sonde : la partie servie seule | § 0 bis D2 ; § 5.3 | `:52` (`SEPARATEUR`) ; `:358` (`assembler_proposeur`) ; `:392` (`assembler_sonde_refus`) ; l'invariant de `:286` refuse tout séparateur autre que celui de l'enveloppe | `TestEnveloppeSansAjout` (10), dont `test_proposeur_generation_1_exacte`, `test_aucun_texte_du_noyau_ni_de_role` |
| ne reprendre du noyau ni le retrait de fin de ligne, ni la section « Case », ni la section d'héritage | § 2.9 ; L0, « D2 », point 2 | `:358` ; aucune autre source d'octets | `test_aucun_texte_du_noyau_ni_de_role`, `test_partie_servie_et_synthese_jointes_sans_retrait` |
| « le dernier octet des pièces servies est gardé tel quel, et l'empreinte se calcule sur la pièce entière » ; « l'empreinte de chaque pièce … se retrouve dans la composition journalisée » | § 0 bis, 08:00Z, mot 1 ; § 5.3 | `:254` (`Element` : `piece_sha256`, `piece_taille`) ; `:286` (une pièce servie l'est entière, sinon refus) | `TestDernierOctet` (3), dont `test_fins_de_piece_non_normalisees` (fins « x », « \n\n\n », « ␠␠\n », « \r\n » : gardées) |
| « composition par rôle » ; « rend la suite d'octets et sa composition » | mandat ; § 2.2 | `:272` (`RequeteAssemblee` figée ; la composition recouvre les octets morceau par morceau, empreinte de chaque morceau ; UTF-8 valide) | `test_la_composition_recouvre_la_requete`, `test_composition_fausse_refusee`, `test_requete_hors_utf8_refusee` |
| « forme de la fiche servie au portier et aux juges, déclarée » ; « gardée et déclarée à l'additif, octet pour octet » ; « pour un juge, l'identifiant servi en dernière clé » ; identifiant réencodé | mandat ; § 2.4 ; § 2.5 ; § 5.3 ; 07:46Z, mots 1 et 8 | `:58` (constantes de la forme) ; `:418` (`_assembler_forme` : texte décodé, `rstrip`, titre, bloc, indentation d'un espace, un seul encodage) ; `:439` ; `:447` (identifiant de quatorze lettres décodé par le lot 1, sinon refus) ; `:410` (les douze champs, des chaînes) | `TestFormeFicheServie` (10) : **égalité à l'octet avec `fiches_v54.entree_une_fiche` du noyau**, pour le portier et pour un juge ; identifiant du noyau refusé ; la requête de juge passe la garde d'essai, l'identifiant hexadécimal du noyau y fait mordre l'arrêt n° 16 |
| arrêt n° 8 : « consigne, registre compris, plus longue que sa borne » ; « mesure de la taille » ; « requête égale à sa borne : départ ; un octet de plus : départ refusé » | V9, l. 379 ; § 6.1 ; § 7 | `:102` ; `:475` (`mesurer`) ; `:482` (`verifier_borne`) ; `:492` (`tailles_par_sorte`, pour la mesure des consignes du lot 9) | `TestArret8Taille` (5), sur les cinq sortes de requête |
| la chaîne remise au noyau, qui prend une chaîne | vérification des lots 1 et 2, § 5, point 5 | `:503` (`chaine_pour_le_noyau` : décodage strict, ré-encodage égal) | `TestChaineDuNoyau` |

### Module `journal` (CO5, § 2.3, § 2.7, § 2.13 ; mandat, point 1)

| exigence (citation) | lettre | code | essai |
|---|---|---|---|
| journal « d'ajout seul » ; « le journal refuse une réécriture » | mandat ; § 2.7 | `journal_na_v1.py:162` (création neuve, R12 ; nom simple ; dossier de sortie) ; `:187` (le fichier relu et comparé avant chaque ajout) ; `:194` (`O_APPEND`, rang, empreinte de la ligne précédente) ; `:215` (sceau, compagnon) ; `:302` (`verifier_journal`, chaînage ; `exiger_sceau`) | `TestAjoutSeul` (10) : un octet changé, une troncature, un vidage, une ligne ajoutée d'une autre main, un remplacement de même taille : refusés ; scellé : plus d'ajout |
| « une ligne avant l'envoi : taille, empreinte SHA-256, génération, rôle, identifiant de la case, clé par son nom d'usage » ; « après la garde de motifs » ; « un appel sans ligne ne part pas » | V9, l. 77 ; § 2.3, pas 3 et 4 | `:235` (`journaliser_envoi` : garde du lot 2 exigée, garde d'abord, ligne ensuite, composition dans la ligne ; la garde doit avoir lu exactement les octets de la requête ; rend `EnvoiJournalise`) | `TestEnvoi` (11) |
| « le texte trouvé ne va qu'au journal » ; ni le message, ni `args`, ni `repr` | V9, l. 387 ; § 2.7 ; vérification des lots 1 et 2, § 5, point 3 | `:245` à `:254` (ligne « non envoyé » : arrêt n° 16, famille, `rang_motif`, `texte_trouve`, coût nul ; puis l'arrêt du lot 2 est relevé tel quel) | `test_refus_de_la_garde_ligne_non_envoye_et_texte_au_seul_journal` |
| requête journalisée et rejouée égale ; « une requête changée d'un octet après la journalisation est refusée à l'envoi » | V9, l. 77 ; § 6.2 | `:332` (`verifier_rejeu`) ; l'égalité du lot 2 (`verifier_avant_envoi`) sur les octets rendus | `test_requete_rejouee_egale_depuis_les_pieces_relues`, `test_requete_rejouee_egale_dans_un_autre_processus` (graine de hachage différente), `test_requete_changee_d_un_octet_apres_la_journalisation_refusee` |
| lignes « non envoyé » (avec le numéro de l'arrêt) et « non lancé » (coupure au plafond dur) | § 2.3, pas 7 ; § 2.7 | `:264` (liste fermée des champs, coût nul) ; `:273` (renvoi au rang et à l'empreinte de la ligne « envoi », une seule fois, du même journal) | `TestNonEnvoyeEtNonLance` (4) |
| refus écrits par rôle, « ce qu'ils rendent » | § 2.13 ; mère, 07:51Z | `:53` (`RENDUS_REFUS_ECRIT`) ; `:287` (`journaliser_refus_ecrit` : ligne, coût nul, rend `RenduRefusEcrit`) | `TestRefusEcrit` (3) |
| comptes des refus, par rôle et par arrêt, par rôle et par garde | § 2.7 | `:345` (`comptes`) | `test_comptes` |

## 4. Essais, sonde, mutations

**Essais** : `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -v -p no:cacheprovider …/essais/test_na_v1_requete.py …/essais/test_na_v1_journal.py` dans la copie d'application : **72 passés, 0 échec** (requête : 44 ; journal : 28 ; journal `journal-essais-na-lot-3-v1.txt`). Python 3.13. Par le programme d'application (`--lancer-essais`), sur une copie neuve du dossier `orchestrator` du commit `a41b7b50…`, après le paquet v2 des lots 1 et 2 posé par son propre programme : **164 passés** (92 des lots 1 et 2, 72 du lot 3). Le programme du lot 3 refuse : la copie sans les lots 1 et 2 (« fichier requis absent ») ; une seconde application (« cible déjà présente », R12) ; le dépôt de l'orchestrateur (« destination dans le dépôt »). Dépôt de l'orchestrateur propre après (`git status --short --ignored` vide).

**Sonde sur le gabarit servi réel** (hors du paquet, `sonde_gabarit_servi_na_lot3_v1.py`, journal `journal-sonde-gabarit-servi-na-lot-3-v1.json`, comptes seuls) : le gabarit `4cd360ba…` (2 957 octets, fini par une fin de ligne) porte un seul emplacement, sur une ligne propre ; rempli des 120 lignes de case possibles (mot de rang 0), les 120 parties remplies sont égales à l'octet au gabarit hors de l'emplacement, gardent son dernier octet, et égalent la requête de sonde ; 3 006 à 3 080 octets.

**Mutations** : `python -B paquet/orchestrator/essais/mutations_na_lot3_v1.py JOURNAL`, à la manière de la v68 et des lots 1 et 2 (copie neuve, remplacement à texte exact présent une fois, essais nommés dans un processus à part, « tuée » si et seulement si pytest rend 1). **58 mutations, 58 tuées** (requête : 35 ; journal : 23). Témoin non muté : les deux fichiers entiers passent. Témoin inerte (un mot de docstring) : survit, comme attendu. Journal : `journal-mutations-na-lot-3-v1.json`, qui porte l'empreinte des fichiers mutés.

- Une première passe laissait **L3-31** (empreinte des morceaux non vérifiée) en vie : l'essai ne changeait que l'empreinte d'une pièce, que la garde « pièce servie entière » attrapait aussi. J'ai ajouté un cas sur le morceau « titre », qui n'est pas une pièce ; L3-31 est tuée.
- **Preuve plus faible, dite** : six mutations sont tuées parce qu'une autre exception remonte, non parce qu'un essai voit la garde manquer : L3-07 (la ligne rebâtie refuse à la place du contrôle du lot 1), L3-05 (zéro emplacement : erreur d'index), L3-17 et L3-48 (erreur d'attribut), L3-37 (le mode de création exclusif refuse à la place de la garde), L3-56 (erreur de clé). La garde retirée laisse donc une seconde barrière ; je ne l'ai pas ôtée.
- **Non écrites, parce qu'équivalentes** (elles survivraient sans défaut des essais) : la mesure lue sur la composition au lieu des octets (l'invariant les rend égales) ; la comparaison de ré-encodage de `chaine_pour_le_noyau` et de `EnvoiJournalise.chaine_pour_le_noyau` (un décodage UTF-8 strict se ré-encode toujours aux mêmes octets) ; le contrôle de forme canonique d'une ligne de journal et celui de la ligne coupée (le chaînage et le sceau les couvrent).

## 5. Ce que la lettre ne fixe pas (remarques ; rien n'est tranché ici)

1. **Le séparateur de l'enveloppe** est un « \n » ajouté après chaque pièce (CO5, § 5.3, « une ligne vide »). C'est une ligne vide parce que la partie servie et la synthèse finissent par une fin de ligne ; une pièce qui n'en finirait pas serait suivie d'un seul « \n », sans ligne vide. Le code garde le dernier octet tel quel (mot 1) et n'en ajoute pas. Après le titre du registre, une fin de ligne. À écrire à l'additif.
2. **Le titre de la section du registre** et **la règle du registre vide** sont des valeurs ouvertes de l'additif (CO5, § 5.3) : le titre est un argument (une ligne, non vide, sans blanc en bord) ; « registre vide » est lu comme « zéro octet » ; la section est alors omise et la requête le dit (`registre = "omis (registre vide)"`). Les lignes de compte toujours écrites (07:21Z, règle 2) rendront ce cas rare dès la génération 2.
3. **La forme de la réponse sans fiche servie au portier** (appel « réponse sans fiche », CO5, § 2.4, b) n'est fixée nulle part. Proposition du développeur, écrite et éprouvée : la forme de la fiche, titre `## La réponse`, objet `{"reponse": texte}` en JSON ; une clôture de bloc ou une fin de ligne du texte restent échappées dans la chaîne. À fixer à l'additif, avec la consigne de D3.
4. **La forme du noyau retire tous les blancs de fin de la consigne** (`str.rstrip()`), non la seule fin de ligne ; je la garde à l'octet (égalité avec `fiches_v54`), et la composition consigne l'empreinte de la consigne entière et celle de la partie servie. Une consigne de D3 finie par des blancs perd donc plus d'un octet : à dire à l'additif.
5. **La fiche servie au portier et aux juges** est exigée aux douze champs exacts du contrat, des chaînes, dans l'ordre où elle est donnée (le noyau garde l'ordre du contenu). L'ordre des clés n'est pas fixé par la lettre ; le lot 5 donne l'ordre.
6. **La génération** est exigée de 1 à 3 pour un proposeur ; elle est permise absente (`None`) pour la sonde et pour le portier et les juges (épreuve des témoins, lignes à part).
7. **Le numéro des arrêts neufs** (A2, A17, onze refus écrits, garde de la colonne) n'est pas encore donné par l'additif : la ligne « non envoyé » accepte un numéro entier ou un nom non vide.
8. **La liste fermée des champs de plus d'une ligne « non envoyé »** est de moi : famille, `rang_motif` (pour ne pas se confondre avec le rang de la ligne), texte trouvé, cause, clause, empreinte, taille, sorte. Le lot 4 qui voudrait un autre champ demande une version neuve.
9. **Un journal par fichier** : la conception le dit « scellé à la fin de chaque génération » sans dire s'il y a un fichier par génération. Le module tient un fichier ; le lot 6 choisit le nom (`…jsonl`) et le nombre.
10. **La dernière ligne d'un journal non scellé n'est tenue par rien à la relecture** (le chaînage tient les autres). En cours de course, l'objet journal voit toute réécriture ; à la relecture, `verifier_journal(chemin, exiger_sceau=True)` refuse un journal sans compagnon. Le lot 7 (mesures, export) devrait l'exiger.
11. **Le coût nul** est écrit en clair (`cout_usd: 0.0`) sur les lignes « non envoyé », « non lancé » et « refus écrit ». Le journal ne compte aucun coût d'appel : la surcharge d'`appel` (lot 4) les compte.
12. **La table de ce que rend un refus écrit** ajoute deux colonnes de moi, tirées du § 2.13 : `fiche_rendue` (vrai pour le portier en appel « fiche » : au dénominateur de M3 et de la garde du coffre) et `appel_compte_m6` (vrai pour le portier en appel « réponse sans fiche », classé « réponse illisible » ; faux pour un proposeur : « ce n'est pas un appel »).
13. **Le texte système de l'adaptateur Claude** (L0, Q1) n'est pas dans la requête : il est posé par l'adaptateur, hors de ce lot (lot 4). Le lot 3 éprouve seulement que la requête ne porte ni texte de rôle, ni syntaxe de sortie, ni morceau du noyau.

## 6. Interface pour les lots 4 et 5

**Requête** (`pole.requete_na_v1`, alias `rq`) :
- `rq.lire_gabarit(chemin, empreinte=rq.EMPREINTE_GABARIT)` / `rq.charger_gabarit(octets, empreinte, nom_fichier=None)` → `Piece` ; `rq.lire_piece(nom, chemin, empreinte)` / `rq.charger_piece(nom, octets, empreinte)` → `Piece(nom, octets: bytes, sha256, taille)` (synthèse, registre servi, consignes de D3).
- `rq.cases_du_tirage(sortie_du_tirage, gabarit)` → `{"1"|"2"|"3": (CaseServie × 11), "reserve": CaseServie}` ; `CaseServie(triplet, identifiant, ligne)`.
- `rq.assembler_proposeur(gabarit, case, synthese, generation, registre=None, titre_registre=None)` ; `rq.assembler_sonde_refus(gabarit, case)` ; `rq.assembler_portier_fiche(consigne, contenu, identifiant_case, generation=None)` ; `rq.assembler_portier_reponse_sans_fiche(consigne, texte, identifiant_case, generation=None)` ; `rq.assembler_juge(consigne, contenu, identifiant_servi_14_lettres, identifiant_case, generation=None)`. Toutes rendent une `RequeteAssemblee(sorte, generation, identifiant_case, octets: bytes, sha256, taille, composition, registre, sources)`, figée ; `sorte` ∈ `rq.SORTES`.
- `rq.mesurer(requete)`, `rq.verifier_borne(requete, borne_octets)` (lève `rq.ArretConsigneTropLongue`, `numero = 8`, `sorte`, `taille`, `borne`), `rq.tailles_par_sorte(requetes)`.
- Exceptions : `rq.RequeteRefusee` et ses filles `QuestionRefusee`, `EmplacementRefuse`, `EmpreintePieceDifferente` (`numero = 14`, `piece`) ; les refus de ligne de case du lot 1 (`tirage_na_v2.LigneDeCaseRefusee`) remontent tels quels.
- Lot 5 : le portier neuf produit ses deux sortes d'appel et les juges leur requête **par ces fonctions** (forme déclarée) ; l'identifiant servi au juge s'encode par `identifiants_na_v1.encoder_identifiant_juge` (cinq octets du jeton du noyau) ; le registre servi entre comme une `Piece` lue à son empreinte.

**Journal** (`pole.journal_na_v1`, alias `jn`) :
- `j = jn.JournalRequetes(dossier_sortie, "….jsonl")` (fichier neuf, ajout seul).
- **Point d'envoi, pour la surcharge d'`appel` du lot 4** :
  ```
  envoi = j.journaliser_envoi(requete, garde, role=etiquette_du_role, cle=nom_d_usage_de_la_cle)
  octets = envoi.octets                       # la suite d'octets que la garde a lue et que la ligne décrit
  garde_motifs_na_v2.verifier_avant_envoi(envoi.requete_gardee, octets_remis)   # sur ce qui est remis au noyau
  consigne = envoi.chaine_pour_le_noyau()     # la chaîne pour `super().appel` ; elle se ré-encode en `octets`
  ```
  `envoi` est un `EnvoiJournalise(requete_gardee: RequeteGardee du lot 2, rang, sorte, role, cle, generation, identifiant_case, journal_id)`. Refus de la garde : la ligne « non envoyé » est écrite (arrêt n° 16, famille, rang du motif, texte trouvé), puis `garde_motifs_na_v2.ArretMotifInterdit` remonte tel quel, sans le texte. Journal scellé ou réécrit : `jn.JournalScelle` ou `jn.JournalReecrit`, rien n'est rendu, rien ne part.
- `j.journaliser_non_envoye(arret=…, role=…, generation=…, case=…, cle=…, **details)` (arrêt n° 12, garde de la colonne, etc. ; `details` dans `jn.DETAILS_NON_ENVOYE`).
- `j.journaliser_non_lance(envoi, cause=jn.CAUSE_NON_LANCE)` : après un appel que le noyau n'a pas lancé.
- `j.journaliser_refus_ecrit(sorte=…, role=…, generation=…, case=…, garde=…, cause=…)` → `RenduRefusEcrit(sorte, rendu, effet, classe, compte, fiche_rendue, appel_compte_m6, rang)` ; `sorte` ∈ `"proposeur"`, `"portier_fiche"`, `"portier_reponse_sans_fiche"`, `"juge"`.
- `j.sceller()` en fin de génération ; `jn.verifier_journal(chemin, exiger_sceau=False)` ; `jn.verifier_rejeu(ligne_envoi, requete_rejouee)` ; `jn.comptes(lignes)` pour la ligne de la génération (lot 6).

## 7. Écarts et réserves

1. La copie de l'orchestrateur est faite dans mon dossier, comme la session l'a dit ; la copie de travail est retirée, la copie d'application reste (§ 2).
2. Je n'ai lu ni le registre des décisions, ni celui des accords : les mots de la mère sont ceux que portent CO5 et son contrôle.
3. Je n'ai pas relu à la source le texte système de l'adaptateur Claude (L0, Q1, « à vérifier à l'octet au lot 3 ») : sous D2, il est retiré par l'adaptateur neuf du lot 4 et n'entre pas dans la requête ; l'essai du lot 3 cherche dans la requête les fragments « {fiches} », « {notes} » et « bloc JSON », absents.
4. Le gabarit réel n'est pas dans le paquet : les essais lisent le gabarit factice des lots 1 et 2 ; la sonde du § 4 joue le gabarit réel, hors des essais.

— développeur du lot 3 du véhicule NA-1, modèle O
