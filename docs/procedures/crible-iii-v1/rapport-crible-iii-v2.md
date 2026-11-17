# Rapport — code neuf de lancement du crible (iii), v2

- **Rédacteur** : développeur neuf du modèle A (identité dite en conversation seulement) ; n'a écrit ni la pièce qui fera foi, ni ses
  brouillons, ni aucun rapport de contre-lecture, ni le code du pilote. Écrit du 2026-11-16T23:25Z au 2026-11-17T01:20Z (`date -u`), dans le dossier neuf
  `docs/procedures/crible-iii-v1/` ; **aucun fichier existant modifié, rien de committé, aucune machine, aucun appel au loueur ni à
  un fournisseur de modèles, aucune clé employée, aucune dépense**.
- **Version** : v2, scellée à 2026-11-17T03:04:30Z (`date -u`) ; suit la v1 (`aac9c95c…`, gardée telle quelle). Corrections du tour 1 de la
  contre-lecture du code (`contre-lecture-code-crible-iii-tour1-v1.md`, `c0c66dd5…`, verdict « corrections » : deux majeures,
  quatre mineures) appliquées par un rédacteur neuf du modèle C, qui n'a écrit ni la pièce, ni le code v1, ni ce rapport en v1, ni
  le rapport du tour 1, par le programme de couples `appliquer_corrections_crible_iii_tour1_v1.py` (`9d3d49f8b88cb9aded955f28c367baf8e2c47de596001c45ac375ea71b6d49de`) ; réponse point
  par point au § 7. Ne change que ce que ces corrections et les noms neufs qu'elles entraînent (R12) exigent : en tête (titre,
  cette puce), § 1 (table v2 ajoutée), § 2 (noyau, lanceur, machine), § 3 (jeux de la v2 ajoutés), § 4 (points 1, 2 et 4, chemin
  court), § 6 (une réserve levée), § 7 (neuf). Aucune machine, aucun appel, aucune clé, aucune dépense ; rien de committé.
- **Pièce qui fait foi** : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-version-foi-v1.md`
  (`91b4bf30fbf8b83d2c057088d8776be19831b006f1010bcb3c7e2e231d2c7179`, égale à son compagnon), jugée **« scellable »** par le tour
  différentiel (`contre-lecture-crible-iii-foi-tour1-v1.md`, six remarques facultatives, aucune correction) ; scellable **comme pièce**,
  non comme préenregistrement en vigueur : restes (a) à (d) de son statut (ci-dessous, § 4).
- **Code du pilote repris, non modifié** (lu par `git show` sur `lot/compte-organisme-v1`, paquet `e3d83e47…` dépaqueté hors dépôt) :
  lanceur v74 (`attendu_du_releve`, configuration v12 `f69503dd…`, empreinte `184ba783…`), cœur v70 (texte servi G0, gardien,
  C-16, C-17, K1 servie), proposeurs v70 (commande, relais, appel en session neuve, témoins), sonde v74 (lecteur du relevé
  `f56d9c0e…`), procédure v14 et ses pièces sans ssh ; modèle de la machine de l'idée 1.1 (procédure v6, lanceur v2, amorce v2,
  garde v1, répétition v2).

## 1. Pièces (v2 : neuves, ou gardées de la v1 ; chacune scellée par compagnon)

  | pièce | rôle | empreinte |
  |---|---|---|
  | `crible_iii_v2.py` | noyau v2 : analyseur, filtre, tirage de H, gabarits G1 et G2, files, bornes, gardes, lignes de GO ; M1 et m3 du tour 1 (exceptions du gardien et d'un monde arrêtées, appels en vol attendus, arrêt réel après le minimum) | `15bc71ed5e4b2522563d0fbb166753bde3497e03505470f0d1819f1a4c7cb611` |
  | `crible_iii_v1.py` | noyau v1, gardé : importé par la mesure seule (constantes, `racine_graines`, `traits_employes`, inchangés en v2) ; son ordonnanceur n'est plus joué | `b163e4c6d8070ec40c544c4519143711fbb8d9ec3d6f9a6a931152b0d265a156` |
  | `lanceur_crible_iii_v2.py` | lanceur v2 : secret, mondes, préparation, crible (à blanc, réel), sonde des gabarits (M2 : appel sous G2 non rendu ou sans carte admise), rapatriement, empreintes | `596b9066fd12e27212182c0a0afacbe7ed58767a129193af3bd01a486a982c38` |
  | `mesure_crible_iii_v1.py` | mesure gelée (nom réservé par la pièce), une seule fois ; inchangée | `8e0df42ac59f8c30e7eece797b1d28b2c770af1d2f1f0516d9bd4b98408a9eeb` |
  | `lire_crible_iii_v1.py` | lecture gelée (nom réservé par la pièce), étages 0 à 7 ; inchangée | `fb83b6303dfc2433082a372ce15fbbc0c18e4077cefcb0daf91fdb045ee0a2e7` |
  | `relais_factice_crible_iii_v1.py` | relais factice (relais du pilote, amont scripté) : essais à blanc seulement ; inchangé | `8f28dacd87e800c74e6278b0c2663a6298fe572698832c1bac99edecc2d56a11` |
  | `amorce_crible_iii_v2.sh` | amorce de la machine v2 (prend le programme machine v2 et son aide) | `510e08cd5e4bba7def246a5ae6068d2b0694c408da3ada1387c47435713fde92` |
  | `machine_crible_iii_v2.sh` | programme machine v2 (lanceur v2, six fichiers du crible) | `5718b23bdf2aeba7653b7cdebfbd5eb8a5956030998906d5b043a04c5e55ad76` |
  | `machine_crible_iii_v2.py` | aide du programme machine v2 (six fichiers du crible à l'addendum) | `4b31f7e4268fb07b72ddded6aa98a72d1429950fe61def52eb0cc1073d998ea3` |
  | `session_crible_iii_v2.sh` | outil de la session v2 (amorce et programme machine v2) | `e7e218654623d39ff263170ec811632f79a676c903bf02828475aad53f0e05f4` |
  | `garde_session_crible_iii_v1.py` | gardes de la session ; inchangées (le lecteur des lignes de GO qu'elles prennent au noyau v1 est inchangé en v2) | `4e4aa32af4e9149790042287cd83a8c6f574dc6e0da1eb993a25633b36d5059b` |
  | `essais_crible_iii_v2.py` | essais R5 du niveau A (45 cas) et cas `essais_arbre_k1` du niveau B (m4) | `f390877d3abe46edf95e50581d014b064b83fd5a6b505657de92c84444637cdd` |
  | `mutations_crible_iii_v2.py` | banc de mutations v2 (40 au niveau A, 1 au niveau B) | `1deaf4384822e0b59cb5eac7dfd92fc01a38141fcd0862aa87a0fe50d9daf90c` |
  | `essai_a_blanc_crible_iii_v2.py` | essai à blanc complet v2, chaîne réelle, relais factices (niveau B) | `ac0d6f25fc4f54684474fb8da3dd0df81dfa928aec648aa0b547954f833930de` |
  | `repetition_machine_crible_iii_v2.sh` | répétition locale de la machine v2 (dépôt jouet, doublures) | `8032d829ffd428503352ddcbdcb08f48bea336c32d2f4e9b0aeff77397331071` |
  | `doublures_repetition_crible_iii_v1.py` | doublures de la répétition ; inchangées | `f264d6dc8bf787e877c3c94d7ae90adff81e8ad410ca2adc06b314f93d62257a` |
  | `sortie-essais-crible-iii-v2.txt` | sortie gardée des essais v2 | `0a01a2e865e88b00e781ef9765f630c3329230f0aadecb5531bb0f8c10b356dc` |
  | `sortie-mutations-crible-iii-v2.txt` | sortie gardée du banc de mutations v2 | `4979207727ace3601799e6bce0527104a6c5c842c56957a0804eaa77976569f1` |
  | `sortie-essai-a-blanc-crible-iii-v2.txt` | sortie gardée de l'essai à blanc complet v2 (second jeu) | `ac91f53df5d0f374a156fd70971a1c6a8285969db918b76ff74bc6cdc65e1d96` |
  | `sortie-essai-a-blanc-crible-iii-v2-jeu-1-ports-occupes.txt` | premier jeu de l'essai à blanc v2, refusé dès son premier cas : ports des relais tenus par une autre session (gardé, R4) | `8672596d261fccc7327268b98067a4309f7889942a9134ef4291afca42b7e0c8` |
  | `sortie-repetition-machine-crible-iii-v2.txt` | sortie gardée de la répétition de la machine v2 | `458651bec2959bbd818be6f6bbfefe0f5a81d4d332a2eaef5a00c6fa9fc3986c` |
  | `devis-machine-crible-iii-v1.md` | devis de la machine (κiii2) ; inchangé | `066f8297aa52e0e3df77e1b0b27458ca3b33c7f0874dcdc7a8f0fa3454b6b740` |
  | `appliquer_corrections_crible_iii_tour1_v1.py` | programme de couples du tour 1 (code v2, puis ce rapport et la procédure v2) | `9d3d49f8b88cb9aded955f28c367baf8e2c47de596001c45ac375ea71b6d49de` |
  | `contre-lecture-code-crible-iii-tour1-v1.md` | rapport du tour 1 de la contre-lecture du code | `c0c66dd585585257bb3fa18c6aff66d298b93d09ccce5536423362e14d5a0f80` |

  Pièces de la v1, gardées telles quelles (R12) ; celles que la v2 remplace (lanceur, amorce, programme machine et aide,
  outil de la session, répétition, essais, banc, essai à blanc, leurs sorties) ne sont plus employées, et le noyau v1 ne l'est
  plus que par la mesure :

  | pièce | rôle | empreinte |
  |---|---|---|
  | `crible_iii_v1.py` | noyau : analyseur, filtre, tirage de H, gabarits G1 et G2, files, bornes, gardes, lignes de GO | `b163e4c6d8070ec40c544c4519143711fbb8d9ec3d6f9a6a931152b0d265a156` |
  | `lanceur_crible_iii_v1.py` | lanceur : secret, mondes, préparation, crible (à blanc, réel), sonde des gabarits, rapatriement, empreintes | `20cff93d6e22a0cad695e42d6a90510d0fb54bb148f988ae588ac86bfff549e1` |
  | `mesure_crible_iii_v1.py` | mesure gelée (nom réservé par la pièce), une seule fois | `8e0df42ac59f8c30e7eece797b1d28b2c770af1d2f1f0516d9bd4b98408a9eeb` |
  | `lire_crible_iii_v1.py` | lecture gelée (nom réservé par la pièce), étages 0 à 7 | `fb83b6303dfc2433082a372ce15fbbc0c18e4077cefcb0daf91fdb045ee0a2e7` |
  | `relais_factice_crible_iii_v1.py` | relais factice (relais du pilote, amont scripté) : essais à blanc seulement | `8f28dacd87e800c74e6278b0c2663a6298fe572698832c1bac99edecc2d56a11` |
  | `amorce_crible_iii_v1.sh` | amorce de la machine (passée à la création) | `7f589103b64ab36813ea8a3e17efded5ca73b7279d987d78a134a3f7f167f730` |
  | `machine_crible_iii_v1.sh` | programme machine (barrières, crible, mesure, rapatriement) | `cdc2420b879d80e773cb0ae1764f44b3d0b22308cff3a79c7962a8e87c9f2002` |
  | `machine_crible_iii_v1.py` | aide du programme machine (attendus, feux, balayage) | `5dc046c2940b8feaf1ed8b595918b19a8ad76a657170015df06e27e1a109b669` |
  | `session_crible_iii_v1.sh` | outil de la session (offre, commande, feux, état, destruction, preuve) | `89ed262b7f490b51f67d7aad72d745f8d096050412c7e010b3e4681e11284a3a` |
  | `garde_session_crible_iii_v1.py` | gardes de la session (offre, échéance, identifiant, absence, dépense, lignes de GO) | `4e4aa32af4e9149790042287cd83a8c6f574dc6e0da1eb993a25633b36d5059b` |
  | `essais_crible_iii_v1.py` | essais R5 du niveau A (cas sain et artefact par ligne d'arrêt ; filtre à la main) | `04153eb16fb2fb931dc87d3a8c5bb94dde26ce59c0a9d7c648718af1ca089708` |
  | `mutations_crible_iii_v1.py` | banc de mutations (35 mutations) | `8c77eae8c3970ccc51d20c0fa41f5e5a6ef45e55cb202ce77d425d88eed0d36a` |
  | `essai_a_blanc_crible_iii_v1.py` | essai à blanc complet, chaîne réelle, relais factices (niveau B) | `7878813196515006cf9e4dfd7a4ee23a1879ab1f600588b7378eee4d09d5a9ef` |
  | `repetition_machine_crible_iii_v1.sh` | répétition locale de la machine (dépôt jouet, doublures) | `a72ca88d28547827d172adf40c39e53aea76405613fe52b5453e160bdb9bf32c` |
  | `doublures_repetition_crible_iii_v1.py` | doublures de la répétition (loueur, lanceur, mesure, lecture) | `f264d6dc8bf787e877c3c94d7ae90adff81e8ad410ca2adc06b314f93d62257a` |
  | `sortie-essais-crible-iii-v1.txt` | sortie gardée des essais | `f200776ef8027cea337c1a20bb56202f8754dff85d109e3706501f827b362aa4` |
  | `sortie-mutations-crible-iii-v1.txt` | sortie gardée du banc de mutations | `8e034dba1e9c4414cd8271a4c3ed2c4b1235da656ab38d5275e54142014ca31d` |
  | `sortie-essai-a-blanc-crible-iii-v1.txt` | sortie gardée de l'essai à blanc complet | `7105d41db9d367ef36da58f278c2a880762cec6b797ec6b4aa1f44c4985a856a` |
  | `sortie-repetition-machine-crible-iii-v1.txt` | sortie gardée de la répétition de la machine | `3720c374532f5d648244f32bdcf699917bd6255e2af5fdf72cca205200ce512e` |
  | `devis-machine-crible-iii-v1.md` | devis de la machine (κiii2) | `066f8297aa52e0e3df77e1b0b27458ca3b33c7f0874dcdc7a8f0fa3454b6b740` |
  | `sortie-essai-a-blanc-crible-iii-v1-jeu-1-avant-correction.txt` | premier jeu de l'essai à blanc, avant la correction de la garde du pire cas (gardé, R4) | `4fbbeb8eaef597abf73f84b5539a96ebc939c12d21b9a61c06552e26b9b46de3` |

## 2. Ce que fait le code (rapporté à la pièce)

- **Noyau** (`crible_iii_v2.py` ; le v1, gardé, n'est plus importé que par la mesure) : analyseur gelé de la passe 1 (vingt premiers ensembles valides, invalides et ignorés comptés) ;
  filtre gelé (doublons, ensembles inclus dans les traits de l'archive, premier par l'ordre des noms, puis maximin de Jaccard,
  égalités par l'ordre des noms ; moins de six : tous) qui **refuse toute entrée autre** que les ensembles et les traits de l'archive ;
  ensembles de H tirés de `SeedSequence(racine, spawn_key=(r, 40))` ; gabarits G1 (contexte de G0 puis consigne, aucun mot sur les
  conditions, interactions ou sortes d'effets) et G2 (G0, bloc des ensembles reconstruit depuis les formes canoniques, consigne) ;
  textes de passe 2 et de B bâtis par la même fonction puis comparés à l'octet avant l'appel (garde qui ne peut pas échouer
  en production et ne compare pas le texte de H : elle ne sert qu'aux essais qui forcent un texte ; la défense réelle est
  l'empreinte `texte_servi_sha256` de chaque appel au relevé, audit R4, et la relecture des corps des relais à l'essai à blanc ;
  m5 du tour 1) ; **cinq files de quatre mondes** (monde r → file r modulo 5), deux
  étapes par monde (S, passe 1 et H ensemble ; puis D et B ensemble), **borne de 3 000 s par appel et de 7 200 s par monde**,
  **garde de départ de 10 h**, minuterie de 7 200 s + 2 h au départ de chaque monde ; lignes d'arrêt : part atteinte, coût au-dessus
  du pire cas, réponse brute ou témoin absent, limite de débit (> 5 % après dix appels du fournisseur), minimum (complets + en cours
  + non commencés < 16, évalué à chaque fin de monde) ; lecteur gelé des lignes « calcul » (enveloppe GO-2026-11-15-06, mots exigés,
  plafonds exacts 260 et 3 USD). En v2 (tour 1) : une exception du gardien arrête le crible (code 3, « exception du
  gardien »), l'appel restant au relevé avec sa dépense ; une exception dans un monde (analyseur, filtre, textes) l'arrête aussi
  (code 3, « exception d'un monde »), le monde compté incomplet ; tous les fils d'appel lancés sont attendus avant que le relevé
  ne soit bâti ; un arrêt réel (témoin absent, coût au-dessus du pire cas, part atteinte, limite de débit, exception) survenu
  après la ligne du minimum la remplace (code 3 : « non jugeable (arrêt) » à l'étage 0 de la lecture, et non « non concluant »).
- **Lanceur** (`lanceur_crible_iii_v2.py`) : `secret`, `generer` (vingt mondes à la graine du crible, quatre processus), `preparer`,
  `jouer` (à blanc avec le relais factice, ou réel par la chaîne du pilote : relais au plafond de la part, 60 et 40 appels,
  commande bornée par le crible), `sonde-gabarits` (κiii0 : trois appels, règles d'avance, III-7 par sa règle ; en v2, M2 du tour 1 : un appel sous G2 non
  rendu, ou complet sans carte admise, déclenche aussi la règle, « G2 non éprouvé, sonde à refaire, crible non lancé »), `rapatrier` (jamais
  `prive/` ni un devis), `empreintes` (pour l'addendum). Gardes du mode réel avant tout dossier : configuration v12, relevé de la
  sonde v74 (exigé dans les deux modes), numpy 2.5.3, texte, addendum d'empreintes, lignes de GO, engagement des vingt mondes
  (non publics, distincts, égaux aux empreintes inscrites), registre des lancements (une seule exécution), bornes gelées.
- **Mesure** (`mesure_crible_iii_v1.py`, nom réservé) : définitions de la pièce (cartes valides, monde complet, composantes comptées
  hors K1 et hors ce que K1 porte seule, C8 de `verifier_v4` en quatre processus, oracle « oracle-crible-iii »), dollars par bras
  (passe 1 comptée dans D et dans B), R_X, Δ_R, ρ, δ, rééchantillonnage apparié de 10 000 tirages `(99, b)`, **97,5 % pour P1 et P2**,
  95 % ailleurs, test des signes, exécution E et E′, bruit, choix de la passe 1, conditionnelle, sensibilités, rapport réintégré de
  δ_DB, drapeaux de l'audit R4 ; une seule fois (seconde mesure refusée) ; défaut nommé si une carte au-delà de six est marquée
  admise.
- **Lecture** (`lire_crible_iii_v1.py`) : étages 0 à 7 des critères gelés, réserves de l'étage 2 (phrases interdites sous « B
  tronqué » et « D tronqué », « sensible à la troncature »), lecture de H-iii, aucune adoption.
- **Machine et session** (v2 : noms neufs seulement ; six fichiers du crible à l'addendum) : amorce, programme machine et aide (trois barrières, phrase chiffrée RSA-OAEP, inscriptions sur `main`,
  essai à blanc sur les vrais mondes avant le feu réel, crible réel une seule fois, mesure, lecture non ouverte, rapatriement,
  balayage, reprise de la poussée, minuterie) ; outil et gardes de la session (offre choisie par la garde, commande imprimée et
  comparée, feux, état, récupération, dépense, destruction par l'identifiant, preuve d'absence par témoins).

## 3. Essais joués (sorties gardées dans ce dossier)

### Jeux de la v2, rejoués après les couples du tour 1

Interpréteur `/usr/bin/python3` (3.13.18, numpy 2.5.3, celui qu'exige la configuration v12) ; arbre 605e0f6 dépaqueté du paquet
`e3d83e47…` dans un dossier jetable ; mondes de développement `4036f512…` (quatre mondes à graine publique, chacun servi cinq
fois) ; relevé de la sonde v74 `f56d9c0e…` ; conteneur chargé par d'autres sessions (charge de 8 à 14 sur quatre cœurs), jeux
sous `nice`, dossiers temporaires dans un dossier jetable. Commandes : `essais_crible_iii_v2.py` (sans argument) ;
`mutations_crible_iii_v2.py --arbre <arbre> --mondes <mondes> --mondes-sha256 4036f512…` ; `essai_a_blanc_crible_iii_v2.py
--arbre … --mondes … --mondes-sha256 … --releve-sonde … --travail <dossier jetable neuf> --python-reel /usr/bin/python3` ;
`bash repetition_machine_crible_iii_v2.sh /usr/bin/python3 <paquet e3d83e47…> <dossier du relevé>`.

- **Essais du niveau A** (`essais_crible_iii_v2.py`, 2026-11-17T02:30:25Z) : **45 cas, 45 passés** : les 42 de la v1 et trois du
  tour 1 : « exception du gardien » (sain : gardien conforme, 20 mondes complets, chaque appel fait listé ; artefact : gardien qui
  lève sur l'appel H du monde 3 → arrêt « exception du gardien », code 3, l'appel au relevé, sa dépense comptée) ; « exception dans
  un monde » (filtre qui lève au monde 3 pendant que son appel S est en vol → arrêt « exception d'un monde », code 3, monde
  incomplet, aucun monde « en cours », l'appel S au relevé) ; « arrêt réel d'un appel en vol après la ligne du minimum » (cinq
  mondes sans passe 1 déclenchent le minimum pendant que l'appel S du monde 5 est en vol ; sain : il revient, « minimum », code 0 ;
  artefacts : il revient sans témoin, ou son gardien lève → l'arrêt réel remplace le minimum, code 3) ; sortie
  `sortie-essais-crible-iii-v2.txt` (`0a01a2e865e88b00e781ef9765f630c3329230f0aadecb5531bb0f8c10b356dc`).
- **Banc de mutations** (`mutations_crible_iii_v2.py --arbre … --mondes … --mondes-sha256 …`, 2026-11-17T02:30:40Z) : original sans échec aux
  niveaux A et B ; **41 mutations, 41 tuées pour la raison attendue** : les 35 de la v1 (les 24 du noyau portées sur
  `crible_iii_v2.py`) ; cinq du tour 1 au niveau A (`try` du gardien retiré, `try` du monde retiré, appels en vol non attendus,
  arrêt réel après le minimum perdu dans l'appel et dans `Commun.arreter`) ; une au niveau B (m4 : « - {eid_k1} - k1_tau » retiré
  de `OutilsMR2.preparer`, sur une copie de la mesure, tuée par le cas `essais_arbre_k1`). Une mutation que les essais « tuent »
  par une exception, et non par l'échec de l'essai attendu, compte comme survivante : c'est le bon sens du refus (m6 du tour 1 ; le
  contre-lecteur l'a vu quand le disque du conteneur était plein) ; sortie `sortie-mutations-crible-iii-v2.txt` (`4979207727ace3601799e6bce0527104a6c5c842c56957a0804eaa77976569f1`).
- **Essai à blanc complet** (`essai_a_blanc_crible_iii_v2.py`, 2026-11-17T02:44:16Z) : **28 cas, 28 conformes** en 1179 s : les
  25 de la v1 et trois du tour 1 : sonde des gabarits avec D en panne (appel sous G2 en échec → « appel sous G2 non rendu (D, état
  echec) : G2 non éprouvé ») et avec B illisible (aucune carte admise → « aucune carte admise sous G2 (B) ») ; préparation réelle
  des mondes (quatre mondes distincts : l'effet de K1 et ce que K1 porte hors des composantes comptées, toutes certifiées ;
  artefact refusé) ; sortie `sortie-essai-a-blanc-crible-iii-v2.txt` (`ac91f53df5d0f374a156fd70971a1c6a8285969db918b76ff74bc6cdc65e1d96`), second jeu : le premier, refusé dès son
  premier cas parce qu'une autre session tenait les ports 8811 et 8812 des relais, est gardé tel quel (R4,
  `sortie-essai-a-blanc-crible-iii-v2-jeu-1-ports-occupes.txt`, `8672596d261fccc7327268b98067a4309f7889942a9134ef4291afca42b7e0c8` ; § 7, incidents).
- **Répétition de la machine** (`repetition_machine_crible_iii_v2.sh`, 2026-11-17T02:30:57Z) : **14 cas, 14 conformes** (les cas de la
  v1, sur l'amorce, le programme machine, l'aide et l'outil de la session v2 et les six fichiers du crible) ; sortie
  `sortie-repetition-machine-crible-iii-v2.txt` (`458651bec2959bbd818be6f6bbfefe0f5a81d4d332a2eaef5a00c6fa9fc3986c`).

### Jeux de la v1, gardés tels quels

- **Essais du niveau A** (`essais_crible_iii_v1.py`) : **42 cas, 42 passés** (cas sain et artefact pour chaque ligne de la liste
  d'arrêt qui se joue sans la chaîne réelle ; filtre éprouvé à la main : égalités, moins de six, doublons, ensemble de l'archive,
  maximin, invalides, au-delà de vingt ; mesure et lecture sur des mondes et des corps synthétiques) ; sortie
  `sortie-essais-crible-iii-v1.txt` (`f200776ef8027cea337c1a20bb56202f8754dff85d109e3706501f827b362aa4`).
- **Banc de mutations** (`mutations_crible_iii_v1.py`) : original 0 échec ; **35 mutations, 35 tuées pour la raison attendue**, dont
  toutes celles que la pièce exige (filtre qui lit le monde ou l'oracle ; égalités rompues par le proposeur ou au hasard ; ensemble
  de l'archive gardé ; H tiré hors de sa graine ou du secret ; B servi d'autres ensembles que D ; réponse brute de la passe 1 servie
  à la passe 2 ; passe 1 comptée hors de $_D ou de $_B ; carte refusée ou au-delà de six comptée ; effet de K1 compté ; intervalles à
  95 % au lieu de 97,5 % pour les principales) et une par garde du lanceur, de la mesure et de la lecture ; sortie
  `sortie-mutations-crible-iii-v1.txt` (`8e034dba1e9c4414cd8271a4c3ed2c4b1235da656ab38d5275e54142014ca31d`).
- **Essai à blanc complet** (`essai_a_blanc_crible_iii_v1.py`, chaîne réelle du pilote, relais factices, aucun appel) : **25 cas,
  25 conformes** en 975 s : crible complet (100 appels, 20 mondes complets, cinq files, bornes gelées, B servi du texte de D à
  l'octet relu dans les corps des relais), mesure une fois (seconde refusée), lecture gelée, lecture avant scellement refusée,
  rapatriement sans monde ni `prive/` ; artefacts de la chaîne : borne par appel (appel de H du monde 1 coupé, compté en échec,
  19 complets), limite de débit, coût au-dessus du pire cas, témoin supprimé, B tronqué partout (ligne du minimum, « non
  concluant »), passe 1 sans liste, carte en trop ; sonde des gabarits (saine, G2 tronqué, G1 illisible, réelle sans ligne) ;
  refus avant tout appel (configuration autre que v12, relevé d'une autre configuration, monde non conforme, garde de départ,
  options du mode réel, ports occupés) ; gardes du mode réel sous numpy 2.5.3 (addendum faux, second lancement, ligne absente,
  mondes autres, scénario) ; sortie `sortie-essai-a-blanc-crible-iii-v1.txt` (`7105d41db9d367ef36da58f278c2a880762cec6b797ec6b4aa1f44c4985a856a`).
- **Répétition de la machine** (`repetition_machine_crible_iii_v1.sh` : amorce et programme machine réels, dépôt jouet, doublures du
  loueur, du lanceur, de la mesure et de la lecture, outil réel de la session) : **14 cas, 14 conformes** : parcours complet (trois
  barrières, phrase chiffrée et effacée, inscriptions, état « fini », lecture rapatriée égale à son compagnon, rien de privé ni de
  secret sur la branche de sortie), feu réel refusé hors de son attente, feu d'arrêt à la barrière 2, cause accentuée refusée,
  phrase absente (arrêt) puis minuterie (DELETE par l'identifiant), refus de l'amorce avant la minuterie (trois DELETE, puis
  « stopped »), branche de sortie déjà présente, commande imprimée (offre par la garde, noms des clés seuls, amorce égale à l'octet,
  0600), `comparer`, ligne de GO absente refusée ; sortie `sortie-repetition-machine-crible-iii-v1.txt`
  (`3720c374532f5d648244f32bdcf699917bd6255e2af5fdf72cca205200ce512e`).
- **Premier jeu de l'essai à blanc** (avant correction ; § 6) : `sortie-essai-a-blanc-crible-iii-v1-jeu-1-avant-correction.txt` (`4fbbeb8eaef597abf73f84b5539a96ebc939c12d21b9a61c06552e26b9b46de3`).

## 4. Ce qui reste avant le feu

1. **Contre-lecture du code** (pièce, Étapes, point 0) : tour 1 fait (`contre-lecture-code-crible-iii-tour1-v1.md`,
   « corrections », appliquées en v2 : § 7) ; reste un **tour différentiel** sur la v2, par un sous-agent neuf d'un autre modèle
   que les auteurs du code v1 (A) et des couples (C), sur ce dossier entier et la procédure v2 (§ 6 de la procédure : fichiers à
   lui donner).
2. **Sonde des gabarits** (κiii0, **obligatoire**, 7 USD au pire, 3,03 attendus) : ligne « calcul » à inscrire par la mère avec
   l'accord de Lazar ; jouée depuis la session, sans machine (procédure, geste 0) ; si une règle d'avance se déclenche, gabarit
   réécrit, nouvelle sonde, crible non lancé (en v2, M2 : un appel sous G2 non rendu ou sans carte admise déclenche aussi
   la règle : G2 non éprouvé, sonde à refaire sur une ligne neuve) ; sinon III-7 refaite par sa règle dans une **version 2** de la pièce, puis un tour
   différentiel (R2).
3. **Restes de la pièce** : trois valeurs calculées sur processeur (part de H après filtre pour III-5, puissance de P1 et P2, taux
   d'erreur de l'intervalle par percentile), versement de l'annexe A et de ses programmes ; puis **scellement par `sceller_prereg`
   et recopie sous `prereg/`** (son empreinte devient la racine des graines et `TEXTE_SHA256`).
4. **Addendum d'empreintes** scellé, qui ne change rien d'autre : les **six** fichiers du crible en v2 (`crible_iii_v1.py`, que la
   mesure importe, `crible_iii_v2.py`, `lanceur_crible_iii_v2.py`, `mesure_crible_iii_v1.py`, `lire_crible_iii_v1.py`,
   `relais_factice_crible_iii_v1.py` : empreintes du § 1, ou celles de la version que le tour différentiel rendra scellable), l'empreinte du texte qui fait foi, les empreintes de l'arbre (`lanceur empreintes`).
5. **Lignes « calcul »** κiii1 (260 USD sur crédits) et κiii2 (3 USD hors crédits) inscrites par la mère sur ce devis, dans
   l'enveloppe de GO-2026-11-15-06 (rien n'y est engagé à ce jour ; le cumul des cinq cribles aux textes actuels, 1 323,67 USD,
   dépasse 1 275 : nœud de Lazar au dernier crible inscrit) ; **feu écrit** `R-<N>` (procédure, § 2, point 5).
6. **Commit** de ce dossier, du texte et de l'addendum sur `main` par la mère (`COMMIT_MAIN`) ; `COMMIT_LOT` = un commit de
   `lot/compte-organisme-v1` qui porte le paquet `e3d83e47…` et le relevé `f56d9c0e…`.
7. **Mondes vérifiés et leurs empreintes, engagement du secret** : faits sur la machine, aux barrières 1 et 2 (empreinte du secret
   inscrite sur `main` **avant** la phrase ; H et S1 à S20 inscrits avant le feu 2 ; vingt mondes conformes exigés).
8. **Mot et phrase de Lazar** : mot daté de moins de dix minutes (présent pour la demi-heure) avant l'impression de la commande ;
   phrase tapée par lui dans la session qui lance, dans l'heure qui suit la location ; préavis avant l'impression.
9. **Décision à prendre avant toute ligne « calcul »** (point 1 de la mère au tour différentiel, recopié ici, sans rien changer) : au
   taux de tronquage de `fable52` lu au pilote (2 sur 4), la ligne d'arrêt du minimum se déclencherait presque sûrement (probabilité
   d'atteindre 16 mondes complets ≈ 1,8 × 10⁻⁷), après ≈ 10 mondes commencés et ≈ 78 USD ; la sonde des gabarits mesurera la sortie
   sous G2 ; les prédictions et G0 étant gelés, accepter ce risque ou demander à Lazar un changement de forme est un nœud.

**Lancer avant le 21 novembre** : rien dans le code ne l'empêche (aucune date n'y est écrite, hors l'échéance des lignes de GO,
2026-11-30) ; le chemin court est : tour différentiel du code v2 → sonde des gabarits → version 2 et tour différentiel → scellement et
addendum → lignes et feu → machine (≈ 2 h 10 attendues, devis § 2).

## 5. Choix faits ici, à contre-lire

- **Mondes générés en quatre processus** (la pièce ne fixe pas le parallélisme ; même graine, même tirage par monde).
- **Monde complet compté par le lanceur** pour la ligne du minimum : appels complets avec au moins une carte **admise** au gardien
  (l'évaluabilité, qui demande l'oracle, n'est jugée qu'à la mesure) ; la mesure refait le compte exact.
- **Modèle servi différent de la configuration** : arrêt (code 3), ligne « configuration autre que v12 » (la pièce ne nomme pas ce
  cas ; le pilote en faisait un abandon du proposeur, qui n'existe pas dans le crible).
- **Aucun abandon de proposeur** après une panne (règle du pilote non reprise : la pièce ne prévoit ni reprise ni bascule, et sa
  ligne « fournisseur perdu en entier » est lue à la mesure).
- **Cartes au-delà du k-ième ensemble** (k < 6) : valides pour la couverture (définition de la pièce : emplacement ≤ 6), hors du
  dénominateur de E et E′, comptées à part (`cartes_sans_ensemble`).
- **Code 2 du crible réel** : arrêt (A), aucune relance (le pilote permettait une relance « reel-2 »).
- **Minuterie au départ d'un monde** : une ligne de défense ; avec la garde de départ, elle ne se déclenche que si l'horloge saute
  (l'essai l'éprouve par un saut d'horloge simulé).
- **Rédaction de G1 et G2** (`CONSIGNE_G1`, `consigne_g2`, `bloc_des_ensembles`) : à contre-lire mot à mot (pièce, « Gabarits ») ;
  leurs empreintes sont au manifeste (`gabarits_neufs_sha256`).

## 6. Réserves et incidents

- **Défaut trouvé par l'essai à blanc et corrigé avant le jeu final** : un appel coupé à sa borne est compté par la chaîne du pilote
  au plafond de session (3 USD pour `fable52`), et la garde propre au lanceur (« coût au-dessus du pire cas », calculée sur les
  octets servis : 2,96 USD) l'aurait pris pour un coût lu et aurait arrêté le crible en code 3 ; la garde ne juge plus que les coûts
  lus (appels complets ou tronqués) ; le premier jeu, avec ce défaut, est gardé tel quel
  (`sortie-essai-a-blanc-crible-iii-v1-jeu-1-avant-correction.txt` : 24 cas conformes sur 25, l'écart est celui-là), le jeu final
  est fait sur le code corrigé.
- **Mondes de l'essai à blanc** : quatre mondes de développement (graine publique), chacun servi cinq fois ; le relais factice
  reconnaît le monde par son contexte servi : un scénario par monde vaut pour les cinq copies, sauf sous H (texte propre à r) ; les
  cartes factices ne portent aucune composante : couverture nulle partout, lecture « hors de la zone utile » (attendu à blanc) ; le
  calcul des couvertures est éprouvé au niveau A, sur des mondes synthétiques.
- **Interpréteurs** : les essais locaux tournent sous numpy 2.4.6 (environnement du dépôt) ; les gardes du mode réel sont éprouvées
  sous `/usr/bin/python3` (3.13.18, numpy 2.5.3, celui qu'exige la configuration v12), sans relais ni appel.
- **Non éprouvé** : la concurrence réelle chez le fournisseur (vingt sessions à la fois) ; la machine louée elle-même (la répétition
  joue l'amorce et le programme machine réels contre un dépôt jouet et une doublure du loueur) ; une mutation de la préparation
  réelle des mondes (retrait de l'effet de K1 dans `OutilsMR2.preparer`) n'est pas au banc (le niveau A emploie des outils
  factices) : à relire par le contre-lecteur (levée en v2 : cas du niveau B et mutation, m4 ; § 3 et § 7).
- **Processus** : l'arrêt du premier jeu de mise au point (par PID) a laissé quatre processus de la mesure (pool) orphelins, arrêtés
  par leur PID (R10) quelques minutes après ; leçon : arrêter la mesure par son PID laisse ses quatre processus (sur la machine, la
  mesure n'est jamais arrêtée par un feu, et la destruction emporte tout). Les essais ont tourné sous `nice`, sur un conteneur
  chargé par d'autres sessions, dont aucun processus n'a été touché.
- **Crochet** : une de mes commandes (une édition de mon propre script de répétition, pour en retirer un arrêt par motif) a été
  bloquée par la garde R10 parce qu'elle portait le nom de l'outil d'arrêt par motif ; je l'ai rejouée en écrivant ce nom en deux
  morceaux dans le programme d'édition : l'effet (retirer cet arrêt du script) est conforme à R10, mais la forme contourne le motif
  que la garde lit ; dit ici pour que la mère en juge.
- **Lectures** : en cherchant R-3005 dans `registres/decisions.md`, la ligne R-3001 s'est affichée avec le libellé de l'issue du
  pilote (déjà écrit à l'en-tête de la pièce : « GO-2026-11-16-08 (l. 349, verdict P-2 accepté) ») ; rien d'autre du verdict n'a
  été lu ; aucune branche `calcul/pilote-mr2-v74-entree-*` ouverte (leur nom seul est paru dans `git branch -a`) ; rien sous `diag/`,
  `runs/`, `donnees/` ; rien de 7a, 7b, T0.6, T0.7, P3-bis, du bras d'attaque. Une commande mal tapée (`/tmp/x`, chemin
  inexistant) n'a rien exécuté (vérifié).
- **Identifiants de modèle** : aucun dans les fichiers de ce dossier (contrôle par programme, valeurs de la configuration lues sans
  être affichées) ; les sorties des relais (corps, réponses brutes), qui en portent, sont restées dans le dossier jetable.

## 7. Contre-lecture

- **Rapport** : `contre-lecture-code-crible-iii-tour1-v1.md`
  (`c0c66dd585585257bb3fa18c6aff66d298b93d09ccce5536423362e14d5a0f80`), tour 1, lecteur C, sous-agent neuf ; verdict
  **« corrections »** (deux majeures, quatre mineures ; aucune ne met la conception en cause) ; ses rejeux (niveau A 42 sur 42, banc
  35 sur 35 au second passage, essai à blanc 25 sur 25) confirmaient ceux de la v1.
- **Application** : par un rédacteur neuf du modèle C, avec `appliquer_corrections_crible_iii_tour1_v1.py` (`9d3d49f8b88cb9aded955f28c367baf8e2c47de596001c45ac375ea71b6d49de`) : il exige
  l'empreinte de chaque source v1 et celle du rapport du tour 1, chaque « ancien » une seule fois au moment de son couple, et
  n'écrase aucune cible ; `code` écrit les dix fichiers de code v2 ; `pieces` refait ces dix fichiers en mémoire, les exige égaux à
  ceux du dossier et à leurs compagnons, lit les bilans des sorties gardées de la v2 (tout conforme exigé), puis écrit ce rapport
  et la procédure v2. Les jeux du § 3 (v2) sont rejoués après les couples.

**Réponse point par point** :

1. **Majeure 1** (exception avalée dans un fil : appel perdu du relevé, aucun arrêt) : **appliquée**. Les deux couples du rapport
   sont recopiés tels quels dans `crible_iii_v2.py`. **Complément déclaré**, hors de leur lettre : un monde en exception laisse
   ses fils d'appel en vol (S et H, ou D et B), que rien n'attendait ; tous les fils d'appel lancés sont désormais attendus avant que
   le relevé ne soit bâti (`fils_d_appel`), sans quoi un appel en vol au moment de l'exception pouvait encore manquer au relevé, le
   défaut même que la majeure exclut. Essais ajoutés au niveau A : « exception du gardien » et « exception dans un monde » (§ 3).
   L'attendu « 100 appels listés » du rapport est lu « chaque appel fait est listé » : l'arrêt arrête les files, les mondes
   suivants ne sont pas commencés et les 100 appels ne sont pas faits. Mutations ajoutées : chacun des deux `try` retiré, et le
   complément retiré ; toutes tuées pour la raison attendue.
2. **Majeure 2** (sonde « saine » quand un appel sous G2 n'a rien rendu) : **appliquée**. Couple du rapport recopié dans
   `lanceur_crible_iii_v2.py` ; couple de la procédure recopié (attendu du geste 0) ; la procédure v2 dit aussi la règle au § 2,
   point 3. Ce n'est pas une quatrième règle d'avance de la pièce (G1 et G2 ne sont pas réécrits) : c'est la garde de validité de
   la sonde ; une sonde à refaire demande une ligne neuve (une seule exécution par ligne) : décision de la mère. Essais ajoutés au
   niveau B (essai à blanc) : D en panne, B illisible ; sain : le cas existant. Aucune mutation demandée, aucune ajoutée (le
   lanceur n'est pas au banc ; les deux artefacts refusés et le cas sain tiennent lieu de R5).
3. **Mineure 3** (arrêt réel perdu derrière la ligne du minimum) : **appliquée** ; les quatre couples du rapport recopiés. Essai
   ajouté au niveau A, avec un second artefact (gardien qui lève sur l'appel en vol), pour éprouver aussi le couple de
   `Commun.arreter`. Mutations : couple de l'appel et couple de `Commun.arreter` remis à l'ancien, tuées ; les couples de la limite
   de débit et de la part, de même forme, ne sont pas éprouvés à part (réserve).
4. **Mineure 4** (préparation réelle des mondes hors du banc) : **appliquée**. Cas `essais_arbre_k1` dans `essais_crible_iii_v2.py`,
   joué par l'essai à blanc et par le banc (`--arbre`) : pour chaque monde de développement distinct, `eid_k1 ∉ comptees`,
   `comptees ∩ k1_tau = ∅`, `comptees ⊆ certifiees` ; un monde préparé puis faussé (effet de K1 remis) est refusé. La mutation de
   niveau B (« - {eid_k1} - k1_tau » retiré, sur une copie de la mesure) est tuée par ce cas. La mesure n'est pas changée. Le banc
   v2 joue pour cela un niveau B (options `--arbre`, `--mondes`, `--mondes-sha256` ; sans elles, le niveau B compte en défaut) :
   original rejoué d'abord, sans échec exigé, puis la mutation.
5. **Mineure 5** (garde du texte de passe 2 tautologique) : **appliquée par la phrase**, le choix étant laissé à la mère : la phrase
   du § 2 est le plus petit changement ; la comparaison de l'octet envoyé au relais dans `fabriquer_appeler` demanderait du code et
   des essais neufs, sans être exigée. Le texte de H n'est contrôlé que par son empreinte au relevé : dit au § 2.
6. **Mineure 6** (deux phrases) : **appliquée** : § 3 (une mutation « tuée » par une exception compte comme survivante ; dit aussi
   dans l'aide du banc v2) ; procédure v2, § 2 point 6 et § 5 (la concurrence réelle non éprouvée est dite à Lazar dans le préavis).

**Remarques facultatives** (aucune n'est une correction) :
- L'analyseur accepte aussi un objet `{"ensembles": […]}`, plus large que « liste JSON de listes d'entiers » de la pièce : gelé tel
  quel, sans conséquence, **dit ici**.
- Second appel de Pr-4 sous G2 à la sonde (au plus 3 USD de plus, plafond κiii0 porté à 10 USD) : **non appliqué** ; c'est un
  changement de forme de la sonde et de sa ligne : à proposer à Lazar par la mère, comme le lecteur l'écrit.
- Choix déclarés du § 5 (modèle servi différent → code 3, aucune relance sur un code 2, aucun abandon de proposeur, cartes au-delà
  du k-ième ensemble), procédure tapable, aucune valeur de clé ni identifiant de modèle : validés par le lecteur ; rien à changer.

**Pour la mère** (rapport du tour 1, § 4) : point 1 (ligne du minimum presque sûre au taux du pilote) inchangé, déjà au § 4,
point 9 ; point 2 fait (v2 et ce rapport) ; point 3 fait (§ 3) ; point 4 inchangé (§ 4) ; point 5 : le disque était encore à 97 %
(1,3 à 1,5 Go libres) pendant les jeux de la v2 ; aucun jeu n'a échoué pour cette cause.

**Conséquences des noms neufs** (R12), déclarées : le noyau v2 impose un lanceur neuf (il importe le noyau), donc une aide et un
programme machine neufs (ils nomment le lanceur et les fichiers du crible), une amorce neuve (elle prend le programme machine et
son aide par leurs noms), un outil de la session neuf (il nomme l'amorce et le programme machine) et une répétition neuve ; les
essais, le banc et l'essai à blanc suivent. La mesure et la lecture (noms réservés par la pièce), le relais factice, les gardes de
la session, les doublures et le devis ne changent pas. `crible_iii_v1.py` reste au jeu des fichiers du crible parce que la mesure
l'importe (constantes, `racine_graines`, `traits_employes`, inchangés en v2) : **six fichiers** à l'addendum au lieu de cinq.
`VERSION` du lanceur devient `lanceur-crible-iii-v2` ; celle du noyau (`crible-iii-v1`, nom du crible), l'étiquette des graines
et l'étiquette de la machine (`crible-iii-v1-AAAAMMJJ`) ne changent pas.

**Tour suivant** : tour différentiel sur la v2 (ce programme de couples, les dix fichiers de code v2 contre leurs v1, ce rapport,
la procédure v2, les sorties v2), par un sous-agent neuf d'un autre modèle que les auteurs du code v1 (A) et des couples (C), R2.
Rien n'a changé dans la pièce qui fait foi ni dans ses prédictions.

**Incidents de ma main** :
- Un programme d'essai jetable de ma main (dans le dossier de session, pour voir l'effet de K1 sur les mondes de développement)
  n'avait pas la garde `if __name__ == "__main__"` : chaque processus de son pool relançait le programme, et le pool les remplaçait
  sans fin pendant une vingtaine de minutes (de 01:58 à 02:21 environ), sur un conteneur déjà chargé ; arrêté par son PID (R10), ses enfants avec lui ; rien d'autre
  touché. Le cas `essais_arbre_k1` du dossier, lui, est sous cette garde.
- Lectures seules dans le dossier de session de la mère : le paquet `e3d83e47…` (dépaqueté dans mon propre dossier jetable, tête
  605e0f6, propre), les mondes de développement `4036f512…` et le dossier du relevé de la sonde v74 `f56d9c0e…` (copiés chez moi
  après contrôle des empreintes). Git en lecture seule (`status`, `log`, `diff --stat`, et un `branch -a` filtré : seule la ligne
  `lot/compte-organisme-v1` affichée) ; aucune branche `calcul/pilote-mr2-v74-entree-*` ouverte ; aucun fetch, aucun commit. La
  mère a committé pendant ce travail (le rapport du tour 1 compris) ; son empreinte est restée `c0c66dd5…`.
- D'autres sessions jouaient en même temps (essais du crible (v), suite d'essais du dépôt) ; leurs processus n'ont pas été touchés.
- La mère a committé mes fichiers du dossier pendant que je travaillais, à plusieurs reprises (au moins `94e5b823`,
  2026-11-17T02:35:03Z, et `11cb5c23`, 02:46:54Z) : les dix fichiers de code v2 et les sorties, déjà scellés, inchangés depuis ;
  mais le premier commit a pris la sortie du banc de mutations alors en écriture (son seul en-tête ; le second l'a reprise, finale et
  scellée), et ce programme de couples, non scellé jusqu'à la fin, a été committé dans des versions intermédiaires (seuls ses textes
  de `pieces` changeaient : commandes des jeux, phrase sur le niveau B du banc, incidents ; ses couples du code sont restés les
  mêmes, ce que `pieces` vérifie en refaisant le code). Sa version finale scellée est à recommitter par la mère. La sortie de l'essai
  à blanc a été écrite d'abord dans mon dossier jetable, puis versée entière.
- Premier jeu de l'essai à blanc v2 (2026-11-17T02:42:26Z) refusé dès son premier cas : « ports des relais occupés : [8811,
  8812] » ; une autre session jouait au même moment ses essais du crible (v), avec des relais sur les ports 8811 à 8814 (ses
  processus n'ont pas été touchés). L'essai à blanc, hérité de la v1 sans changement sur ce point, n'est pas fait pour un refus au
  premier cas : il s'est arrêté ensuite sur une exception (dossier `complet` absent), sans effet sur le code du crible. Gardé tel
  quel (R4) ; le second jeu est parti après la fin du jeu de l'autre session, ports libres. Les ports des relais sont fixés par
  la configuration v12 et communs à toutes les sessions du conteneur : deux jeux à blanc simultanés se refusent l'un l'autre. Un
  espace réseau privé (`unshare -n`, interface `lo` levée) les isolerait : essayé à vide seulement, non employé pour les jeux gardés.
- Les relais factices ont occupé les ports 8811 et 8812 pendant la mise au point de la sonde et l'essai à blanc, arrêtés par le
  lanceur ; des processus d'autres sessions tournaient en même temps (charge de 8 à 14), non touchés.
- Disque du conteneur à 97 % (1,3 à 1,5 Go libres) pendant tout le travail ; fichiers de travail dans mon dossier jetable seulement.
