# Rapport du développeur — véhicule NA-1, lot 10 a (colonne « matière première » : chargement et garde) — v1

- Développeur du lot 10 a du véhicule NA-1, modèle O. Je n'ai écrit ni la conception, ni les lots 1 à 6, ni aucun orchestrateur.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 17:41:16Z, après les runs finaux, avant l'écriture de ce rapport.
- Pièces qui font foi, lues en entier, dans l'ordre, chacune égale à son empreinte : mandat (`9f9f20f9bc7fd9476d49445b5509cffee255158c2de23455ad57d46f8ae79795`) ; erratum 1 (`61674e25f8ad90179ed1e0abeb86264369bd6ca9415f55c9c1161a4e60cb122c`), qui prime sur le mandat ; note de lancement (`08a6bac6bcf7298a0b33b371262d61c5c8de50b64701fd245ffb4d8af3737852`), qui prime sur la racine et sur le dossier ; erratum 1 du lot 6 (`1b08d873f6385c6e4e7fe777c1a1f68255083570264b51ae1061b0b5054a667e`), auquel l'erratum du lot 10 a renvoie (E1, E2, E6, E7).
- Processeur seul : aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucun relais lancé, aucune écriture dans un dépôt, aucun commit. Le registre servi réel n'est pas ouvert ; aucune branche de matière première ni de quarantaine ouverte ; rien ouvert sous `additif-matiere-premiere-v1/`, sous `archives-reponses-modeles/` ni sous `/root/.claude/`. **Aucun refus de permission, de classifieur ni de garde rencontré.**
- **Une interruption, dite** : l'orchestrateur (`a41b7b50…`) manquait au conteneur au départ ; la coordination m'a arrêté par précaution, puis l'a rendu disponible, en lecture seule, sur le mot de Lazar (GO-2026-11-21-66), au clone `/home/user/lciric/ideation-organism` (tête `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, relevée) et à la copie sans `.git` `/home/user/orchestrateur-a41b7b50/`. Je n'y ai rien écrit.

## 1. Verdict

- **Essais du lot 10 a : 99 passés, 0 échec** (`journal-essais-na-lot-10-a-v1.txt`).
- **Chaîne entière** sur une copie neuve de l'orchestrateur, lots 2 v5, 3 v3, 4 v1, 5 v1 posés par leurs programmes puis le paquet du lot 10 a par le mien (`--lancer-essais`) : **460 passés** (lot 3 : 72, lot 4 : 87, lot 5 : 202, comptes égaux à leurs rapports ; lot 10 a : 99).
- **Mutations : 52 sur 52 tuées** ; le témoin non muté passe ; le témoin inerte survit (`journal-mutations-na-lot-10-a-v1.json`).
- **Taux de faux refus de l'essai : 0** (0 ligne refusée sur 3 247 lignes de 100 requêtes et 3 énoncés de registre servi ; 5 pièces fixes passées sans un refus ; `mesure-faux-refus-essai-na-lot-10-a-v1.json`). Attendu nul, puisque la comparaison est une égalité de ligne entière ; mesuré sur des données factices seulement.
- Refus du programme d'application éprouvés : seconde application (R12), destination dans le paquet, copie nue (« `identifiants_na_v1.py` absent »).

## 2. Pièces lues (empreinte recalculée, égale à la table de l'erratum)

| pièce | empreinte |
|---|---|
| conception v5 | `1b7f6822af20417e997b80290f05e7a4d70aa69c3d65f4139b5b3673cd98a863` (§ 0, 0 bis, 2.2 à 2.7, 2.14, 2.15, 6, 7, 8, 9, 10 lus) |
| contrôle de la conception v5 | `4b369004733fb4c55bb75deaeac19c4cc4e5dacaa8604f8082f63096c2956156` (point 4 lu) |
| relevé du lot 0 | `10ac79ecb0e064f5b5ea80ddb060ae37e303d2d84ff242f653f4cccbd7ff753e` (en entier) |
| lot 3 v3 : table ; rapport ; vérification | `1be0ffd4…f7` ; `a778f8fa…8e` ; `a1de7092…3f` |
| lot 4 v1 : table ; rapport ; vérification | `747f782b…54` ; `1b16fabb…2f` ; `3c8d1aa2…83` |
| lot 5 v1 : table ; rapport ; vérification | `c7e7bd56…31` ; `695bdcd9…f5` ; `7742a649…7d` |
| V9 scellée, par `git show origin/main:… >` mon dossier | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` (l. 60 à 129, 366 à 400) |
| consigne commune de méthode, de même | `d327b3fcbee59f37f833e83812a66ba8b28af72cdd5475772870612a2c9d23d8` |
| code lu des lots 2 à 5 | `garde_motifs_na_v4`, `identifiants_na_v1`, `requete_na_v3`, `journal_na_v3`, `appel_garde_na_v1`, `registre_na_v1` (en partie), `verifier_registre_servi_na_v1`, les aides des lots 2 à 4, le programme de mutations du lot 5 |

Non ouverts : le complément de valeurs v3 et les deux additifs de la table de l'erratum (rien du lot 10 a n'en dépend) ; la base v68 (la manière des mutations est prise dans le programme du lot 5, qui la suit).

## 3. Exigences et code (`paquet/orchestrator/pole/matiere_premiere_na_v1.py`, noté MP)

| exigence (lettre) | code |
|---|---|
| chargeur : empreinte du registre vérifiée **avant toute lecture** (§ 2.14 ; arrêt n° 14) | MP:242 `lire_registre`, MP:266 ; MP:317 `charger_registre` |
| de chaque entrée, l'énoncé seul ; forme de l'arrêt n° 19 ; un défaut : colonne non chargée, rien retiré en silence (§ 2.14, § 2.15) | MP:291 (`verifier_enonce` du lot 5, défauts n° 19), MP:109 `ColonneNonChargee` |
| normalisé comme la garde de motifs ; empreinte SHA-256 seule gardée ; ni nom, ni énoncé, ni autre champ (§ 2.14) | MP:150 `_forme` ; MP:176 `Colonne` (quatre attributs, figée) |
| identifiant de ligne reçu par une fonction, aucune source fixée (E5) | MP:242 (paramètre sans défaut), MP:298 |
| interrupteur à trois états ; état 1 sans additif ; état 2 sous la règle d'allumage ; aucun chemin par l'environnement ni par la configuration seule (§ 2.14, table et règle) | MP:420 `decider_etat`, MP:433, MP:435 ; MP:369 `ConditionsAllumage`, MP:380 |
| E4 : état 2 refusé si le manifeste de la lecture de fin manque ou ne porte pas l'empreinte de l'additif ; jamais lue dans la configuration | MP:400 `_manques_manifeste` |
| sixième ligne de la pièce de relevés, **libellé d'essai** ; absente, double, d'un autre libellé, d'une autre empreinte : départ refusé, par son nom (contrôle v5, point 4) | MP:71 `LIBELLE_ESSAI`, MP:334 `lire_sixieme_ligne`, MP:350 ; MP:469 `preparer_depart` |
| garde par énoncé entier et par empreinte, jamais le nom court (07:51Z) | MP:204 `examiner_ligne`, MP:213 `examiner_texte` |
| tenue (ii) : au pas 3 de la surcharge d'`appel`, proposeur et sonde ; « non envoyé », coût nul, compté, arrêt nommé | MP:491 `JournalRequetesColonneNA`, MP:507, MP:513, MP:519 ; MP:66 |
| tenue (iii) : registre servi des générations 2 et 3 ; la génération ne part pas | MP:548 `garder_registre_servi`, MP:525 |
| contrôle des pièces fixes au départ (gabarit, synthèse, consignes, témoins) | MP:453 `controler_pieces_fixes`, MP:485 |
| état 0 : rien n'est chargé ni contrôlé | MP:479 |
| taux de faux refus mesuré et rapporté | MP:572 `mesurer_faux_refus` ; programme `essais/aides_na_lot10a_v1.py` |
| recherche par programme d'absence des noms et énoncés (§ 6.2) | MP:602 `rechercher_textes` |
| arrêt de la garde sans numéro dans la V9 | MP:62 `ARRET_COLONNE`, nommé ; numéro à l'additif |

## 4. Essais (`essais/test_na_lot10a_v1_matiere_premiere.py`, 99) et mutations

Les essais tournent sur le registre d'essai de `essais/aides_na_lot10a_v1.py` : 35 entrées inertes (24 « visée factice », 11 « défense factice »), quatre champs d'essai. **La garde au pas 3 est éprouvée contre le vrai `appel` du noyau et la vraie surcharge du lot 4**, par le montage des essais du lot 4, journal de la colonne à sa place.

| garde | cas sain | artefact |
|---|---|---|
| chargeur, empreinte | registre d'essai à son empreinte : 35 empreintes, 35 identifiants | octets illisibles d'une autre empreinte : refus n° 14 (non « illisible ») ; un octet de plus ; fichier d'une autre empreinte |
| chargeur, forme n° 19 | 35 énoncés conformes ; une étiquette du n° 9 seule ne refuse pas | deux lignes, marque de code, étape numérotée, consigne, borne : non chargé, rang de l'entrée, message sans contenu |
| entrée | quatre champs | champ de plus, champ manquant, pas un objet, énoncé non chaîne, vide après normalisation ; nombre d'entrées ; clé en double |
| empreintes seules | attributs : empreinte du registre, compte, empreintes et identifiants | recherche de chaque nom, énoncé et sorte dans l'état gardé : absents ; colonne non modifiable |
| identifiant de ligne (E5) | deux fonctions d'essai différentes : mêmes empreintes, identifiants disjoints ; la garde rend l'identifiant de la fonction | cinq octets, une chaîne, six octets nuls répétés, une fonction qui lève : non chargé ; aucune valeur par défaut ; l'entrée remise à la fonction ne se modifie pas |
| garde, énoncé entier | nom court, début d'énoncé, reformulation, énoncé dans une ligne plus longue, mot seul : passent | ligne égale en clair, puis sept formes ramenées (casse, espace insécable, bords, caractère invisible, tabulation, tiret de puce, accent décomposé) : mord |
| tenue (ii), vrai noyau | requête de proposeur qui porte un nom court et un début d'énoncé : part | ligne égale, en clair et sous trois formes : `ArretColonneNA`, une seule ligne « non envoyé », coût nul, aucun appel reçu, aucune consommation, cumul inchangé, compté ; avant la garde de motifs ; journal en panne : « requête journalisée », rien ne part ; sonde gardée ; portier et juge hors de la tenue (ii), à la lettre ; état 0 : rien n'est gardé |
| 165 requêtes | en état 1 et en état 0, les 165 requêtes de proposeur (33 cases × 5 rôles) : empreintes et tailles journalisées **égales** | — |
| tenue (iii) | registre servi inerte : passe | un énoncé égal, en clair et sous deux formes : la génération ne part pas, octets inchangés ; génération 1 refusée |
| pièces fixes | les cinq pièces passent | un énoncé entier ajouté à chacune, tour à tour : départ refusé, la pièce nommée |
| sixième ligne | état 1 lu, rang 6 | absente, double, autre libellé seul, autre libellé en plus d'une ligne juste, mal formée, nom d'état faux, état 3 ; empreinte de la pièce fausse (n° 14) ; empreinte du registre fausse dans la ligne (n° 14, sans chargement) ; colonne chargée d'un autre registre |
| interrupteur | état 1 : chargé, manifeste aux comptes ; état 0 : rien chargé (chargeur jamais appelé) ; état 2 avec toutes les conditions d'essai : admis | état 2 sans conditions ; **E4 : manifeste absent, empreinte absente, empreinte fausse, empreinte posée dans la configuration seulement : refusé dans les quatre cas** ; chaque condition (a), (c), (d), (e) manquante ; variable d'environnement qui nomme la colonne (deux casses) ; configuration qui porte un autre état ; refusé avant toute écriture |
| faux refus | taux nul sur l'essai | une ligne plantée : la mesure la voit |
| rien ne fuit | une course courte (un envoi, un refus en tenue (ii), un refus en tenue (iii), un manifeste de départ écrit et imprimé) : aucun nom ni énoncé dans le dossier de sortie, le dossier du run, l'écran | un texte planté : la recherche le voit |

**Mutations** (`essais/mutations_na_lot10a_v1.py`, 52, toutes tuées) : garde retirée (X-01), normalisation retirée (X-02), bords gardés (X-03), empreinte non vérifiée ou lue après (X-04, X-05), forme n° 19 retirée (X-06), retrait silencieux (X-07), contrôles d'entrée (X-08, X-09, X-15), identifiant de ligne (X-10 à X-14, dont « source fixée par défaut »), sixième ligne (X-16 à X-21), environnement et configuration (X-22 à X-24), règle d'allumage et E4 (X-25 à X-33, X-52, dont « empreinte de l'additif prise dans la configuration »), tenue (ii) (X-34 à X-40), tenue (iii) (X-41, X-42), pièces fixes (X-43, X-44), état 0 (X-45), autre registre (X-46), mesure aveugle (X-47), énoncé gardé à la place de l'empreinte (X-48), recherche aveugle (X-49), colonne modifiable (X-50), contenu recopié dans la ligne « non envoyé » (X-51). **Une première passe en laissait survivre trois** : deux par ma faute (identifiants d'essais terminés par « :: », aucun essai joué : T-00, X-01, X-51) ; une réelle, X-30 : l'artefact de la ligne d'accord « état 1 » ne portait pas l'empreinte du registre et mourait pour une autre cause. L'essai est renforcé (et X-52 ajoutée), sans toucher au code ; la passe finale tue tout.

## 5. Ce que la lettre ne fixe pas (remarques ; rien n'est tranché ici)

1. **Lieu de la tenue (ii)** : la conception dit « au pas 3 ». Le lot 4 étant figé, je ne le modifie pas : la garde vit dans un journal du lot 3 dérivé (`JournalRequetesColonneNA`), que la surcharge appelle à son pas 3 (`journaliser_envoi`), après le routage et la part, avant la garde de motifs. Son arrêt n'est pas rattrapé par le lot 4 : rien ne part, aucun coût. Le refus est compté au journal (`comptes_colonne`, et `journal_na_v3.comptes` sous le nom de l'arrêt), **non** dans `na_comptes` du lot 4 : le lot 6 lit l'un et l'autre.
2. **Sortes gardées** : proposeur et sonde, à la lettre. Les requêtes du portier et des juges, qui portent des fiches, ne sont pas gardées en tenue (ii) ; un énoncé recopié dans une fiche y passerait. Point pour la mère.
3. **Forme du registre** : inconnue de moi (non ouvert). Le chargeur prend la forme en paramètres déclarés (`champ_enonce`, `champs_entree`, `cle_des_entrees`, `entrees_attendues`, borne) ; l'essai suppose quatre champs. À fixer à l'additif contre le registre réel, par qui peut l'ouvrir.
4. **Défauts gardés au chargement** : ceux du n° 19 seuls (la conception dit « forme de l'arrêt n° 19 ») ; les étiquettes du n° 9 que `verifier_enonce` rend aussi sont écartées. Les listes de marques sont celles, brouillon, du lot 5.
5. **Forme comparée** : la normalisation de la garde de motifs, **puis les bords retirés** ; découpe des lignes par `str.splitlines` (avant la normalisation, qui ramène les fins de ligne à une espace). Un énoncé vide après normalisation refuse le chargement (il mordrait sur les lignes blanches).
6. **Identifiant de ligne** : la fonction reçoit le rang et une vue non modifiable de l'entrée, et rend six octets, encodés en dix-huit lettres (`identifiants_na_v1`) ; elle peut lire un champ de l'entrée : c'est le choix de qui la donne. Deux entrées au même énoncé normalisé : une empreinte, deux identifiants.
7. **Sixième ligne** : libellé d'essai `colonne « matière première » [libellé d'essai] :`, puis l'interrupteur, `état N (nom)`, l'empreinte du registre, la date. Toute ligne qui nomme l'interrupteur sous un autre libellé refuse le départ. Les cinq autres lignes ne sont pas lues ici (arrêt n° 11, lot 8).
8. **État 0** : pris de la sixième ligne, écrite par la mère ; je le lis comme « le mot de la mère ». À confirmer.
9. **Environnement** : toute variable dont le nom, en majuscules, porte `MATIERE_PREMIERE` ou `COLONNE_MATIERE` refuse la décision, quelle que soit sa valeur. **Configuration** : la clé `colonne_matiere_premiere`, si elle est présente, doit égaler l'état de la ligne ; elle ne l'établit jamais seule.
10. **Règle d'allumage, formes d'essai** : ligne d'accord (nomme l'interrupteur, « état 2 » et l'empreinte du registre, par présence de chaînes) ; manifeste de la lecture de fin (JSON, `format`, `empreinte_additif`), l'empreinte attendue étant **épinglée par le lanceur**, jamais lue dans la configuration ; devis (`ligne` = « lecture de fin », plafond positif, hors des parts) ; lecteurs parmi quatre juges de fin nommés à l'essai ; branche orpheline = le booléen vrai rendu par l'outil du lot 7. Toutes à fixer à l'additif et au lot 10 b.
11. **Taux de faux refus** : mesuré ici sur données factices ; le taux qui compte se mesure à l'essai à blanc du lot 9, sur les pièces réelles et le registre réel.
12. **Copie de travail** : l'erratum dit « dossiers des lots 1 à 5 » pour les listes ; j'ai aussi listé ma copie d'application et l'orchestrateur, permis par la coordination à la reprise.

## 6. Interface pour les lots 8 et 9

**Lot 8 (lanceur)**, au départ, avant toute écriture :
```
depart = mp.preparer_depart(piece_releves=octets, empreinte_piece_releves=…, empreinte_registre_attendue="3bcb94e6…",
                            configuration=conf, pieces_fixes={nom: octets, …}, environ=os.environ,
                            conditions_allumage=None | mp.ConditionsAllumage(…),
                            charger=lambda: mp.charger_registre(chemin, "3bcb94e6…", normaliseur=garde.liste.normaliseur,
                                octets_identifiant_ligne=<fonction donnée>, champ_enonce=…, champs_entree=…,
                                borne_enonce_octets=…, entrees_attendues=35))
```
Lève `DepartRefuseColonneNA` (`ColonneNonChargee`, `EtatRefuseNA`), `.numero` = 14 pour une empreinte. Rend `DepartColonne(etat, colonne, manifeste)` ; `depart.manifeste` va au manifeste de départ (comptes et empreintes seuls). Le libellé d'essai est à remplacer par le libellé fixe de l'additif ; l'arrêt n° 11 lit les cinq autres lignes.

**Lot 6 (génération)** : le journal de chaque génération est `mp.JournalRequetesColonneNA(dossier, nom, depart=depart)`, passé à `ContexteAppelGardeNA(journal=…)` ; `ArretColonneNA` traverse `appel` (arrêt nommé de la course) ; au départ des générations 2 et 3, `mp.garder_registre_servi(depart, s.octets, g)` après `verifier_registre_servi` (lève `GenerationRefuseeColonneNA`) ; `controler_pieces_fixes` rejoué au départ de la génération 2. Comptes : `journal.comptes_colonne`.

**Lot 9 (essai à blanc)** : `mp.mesurer_faux_refus(depart.colonne, requetes, registres_servis)` sur toutes les requêtes et tous les registres de l'essai ; `mp.rechercher_textes([sortie, run], textes_du_registre_d_essai)` pour « rien ne fuit » ; les 165 requêtes comparées entre état 1 et état 0 par leurs lignes de journal.

## 7. Relevé de méthode

**Chaîne de raisonnement.**
1. Le lot 10 a charge et garde ; la lecture de fin est au lot 10 b (conception v5, `1b7f6822…`, § 7, table, lignes 10 a et 10 b).
2. En état 1, seules des empreintes d'énoncé sont gardées, et la comparaison porte sur la ligne entière normalisée (§ 2.14, « Le chargement » et « La garde de la colonne »).
3. L'état 1 se lit à une sixième ligne de la pièce de relevés, sous un libellé encore non fixé ; une ligne absente refuse le départ (contrôle v5, `4b369004…`, point 4 ; mandat, `9f9f20f9…`, § « Ce qui fait foi »).
4. L'état 2 est refusé sans manifeste de lecture de fin portant l'empreinte de l'additif, jamais lue dans la configuration (erratum, `61674e25…`, E4).
5. La source de l'identifiant de ligne n'est pas fixée (E5) : le chargeur la reçoit par une fonction requise (MP:242), éprouvée avec deux fonctions (§ 4).
6. La surcharge du lot 4 appelle `journal.journaliser_envoi` à son pas 3 et ne rattrape que `ArretMotifInterdit`, `JournalRefuse` et `OSError` (`appel_garde_na_v1.py`, l. 358 à 371, fichier à l'empreinte de la table du lot 4 `747f782b…`, vérifiée par son programme d'application) ; un journal dérivé qui lève un autre arrêt avant d'écrire « envoi » refuse donc l'envoi au pas 3, sans coût : calcul rejoué par l'essai « artefact » contre le vrai noyau (§ 4).
7. Le contrat est tenu par les 99 essais (rejoués : 99 passés) et les 52 mutations (rejouées : 52 tuées).
8. Le taux de faux refus de l'essai est nul (rejoué, `mesure-faux-refus-essai-na-lot-10-a-v1.json`) ; supposé représentatif de rien d'autre que l'essai.

**Objets de contrôle.**
- Garde de la colonne. Vrai par construction : une ligne égale à un énoncé du registre d'essai ; attendu « mord » ; rendu : mord (en clair et sous sept formes). Faux par construction : nom court, début d'énoncé, reformulation, énoncé dans une ligne plus longue ; attendu « passe » ; rendu : passe. Mutation « garde retirée » : l'essai échoue.
- Tenue (ii). Artefact : requête de proposeur à ligne plantée, vrai noyau ; attendu : arrêt nommé, « non envoyé », coût nul, aucun appel ; rendu : idem. Sain : requête sans ligne entière ; attendu : envoi ; rendu : envoi, issue « ok ».
- Tenue (iii) et pièces fixes : sain, aucun refus ; artefact, refus nommé (génération, pièce) ; rendu conforme.
- Chargeur : sain, registre d'essai à son empreinte, chargé ; artefacts, empreinte fausse (n° 14), énoncés non conformes (n° 19), entrées d'une autre forme : non chargé ; rendu conforme.
- Sixième ligne : sain, état 1 lu ; artefacts, absente, double, autre libellé, mal formée, empreintes fausses : départ refusé ; rendu conforme.
- Interrupteur : sain, état 1 sans condition, état 0 sans chargement, état 2 avec toutes les conditions d'essai ; artefacts, état 2 sans additif, les quatre artefacts d'E4, chaque condition manquante, environnement, configuration : refusé avant toute écriture ; rendu conforme.
- Mesure du faux refus : sain, essai sans ligne plantée, taux 0 ; artefact, une ligne plantée, vue ; rendu conforme.
- Recherche d'absence : sain, sortie d'une course courte, 0 trouvaille ; artefact, un fichier planté, 1 ; rendu conforme.
- Programme de mutations : témoin non muté passe ; témoin inerte survit ; une première passe a montré trois survivantes, dont deux par un défaut du programme lui-même (§ 4) : le juge a été éprouvé et corrigé.

**Premier pas non justifié.** Le pas 3 : la sixième ligne est écrite contre un libellé d'essai ; ce qui le justifierait est le libellé fixe à l'additif du véhicule, et le programme de la pièce de relevés de la mère qui la porte. Ensuite le pas 2 pour le registre réel : sa forme (champ d'énoncé, nombre de champs) n'est pas vue ; la justifierait une déclaration de forme par qui peut l'ouvrir.

**Mode d'échec affecté.** Sans objet : je suis développeur, non relecteur.

**Dérivation de l'énoncé seul.** Sans objet : je suis développeur, non agent de re-dérivation.

**Trouvaille de côté.**
- La tenue (ii) ne couvre ni le portier ni les juges : un énoncé recopié dans une fiche passe (remarque 2).
- Le journal du lot 3 v3 reste sans conversion de `OSError` en `JournalRefuse` (constat du lot 3) ; le lot 4 le rattrape, et mon essai « journal en panne » le montre.
- Les essais des lots 1 et 2 v5 ne sont pas dans ma chaîne de 460 : je ne les ai pas joués.

**Évaluateur et conseil.** Ce qui juge mon produit : les 99 essais et les 52 mutations, rejouables par le vérificateur S ; la chaîne de 460 essais sur une copie neuve. Témoins du juge : le témoin non muté et le témoin inerte du programme de mutations ; une première passe a montré que le juge pouvait se tromper (identifiants vides). Par où le produit pourrait être bien jugé sans le mériter : toutes les données sont factices, et les formes (registre, sixième ligne, manifeste, conditions) sont celles que j'ai choisies ; un registre réel d'une autre forme, ou un libellé fixe autre, ne serait pas lu, et cela ne se verrait qu'à l'essai à blanc. Ma garde, mes données et mes essais sont du même auteur.

## 8. Livré

Dossier de travail : `dev-vehicule-na-lot-10-a/` dans le bloc-notes de la session ; copie aux jalons sous `/home/user/dossiers-developpeurs-vehicule-na-v1/lot-10-a/`. Un compagnon `.sha256` par fichier de la table ; table `table-empreintes-dossier-na-lot-10-a-v1.txt`. Hors de la table : `application/` (copie d'application, lots 2 à 5 et 10 a posés, sans `.git`), `brouillon-essai/`, `brouillon-copie-nue/` et deux journaux de mutations de brouillon ; `v9.md` et `consigne-commune.md`, tirés de `origin/main`.

— développeur du lot 10 a du véhicule NA-1, modèle O
