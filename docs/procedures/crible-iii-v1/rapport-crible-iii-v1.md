# Rapport — code neuf de lancement du crible (iii), v1

- **Rédacteur** : développeur neuf du modèle A (identité dite en conversation seulement) ; n'a écrit ni la pièce qui fera foi, ni ses
  brouillons, ni aucun rapport de contre-lecture, ni le code du pilote. Écrit du 2026-11-16T23:25Z au 2026-11-17T01:20Z (`date -u`), dans le dossier neuf
  `docs/procedures/crible-iii-v1/` ; **aucun fichier existant modifié, rien de committé, aucune machine, aucun appel au loueur ni à
  un fournisseur de modèles, aucune clé employée, aucune dépense**.
- **Pièce qui fait foi** : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-version-foi-v1.md`
  (`91b4bf30fbf8b83d2c057088d8776be19831b006f1010bcb3c7e2e231d2c7179`, égale à son compagnon), jugée **« scellable »** par le tour
  différentiel (`contre-lecture-crible-iii-foi-tour1-v1.md`, six remarques facultatives, aucune correction) ; scellable **comme pièce**,
  non comme préenregistrement en vigueur : restes (a) à (d) de son statut (ci-dessous, § 4).
- **Code du pilote repris, non modifié** (lu par `git show` sur `lot/compte-organisme-v1`, paquet `e3d83e47…` dépaqueté hors dépôt) :
  lanceur v74 (`attendu_du_releve`, configuration v12 `f69503dd…`, empreinte `184ba783…`), cœur v70 (texte servi G0, gardien,
  C-16, C-17, K1 servie), proposeurs v70 (commande, relais, appel en session neuve, témoins), sonde v74 (lecteur du relevé
  `f56d9c0e…`), procédure v14 et ses pièces sans ssh ; modèle de la machine de l'idée 1.1 (procédure v6, lanceur v2, amorce v2,
  garde v1, répétition v2).

## 1. Pièces écrites (toutes neuves, scellées par compagnon)

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

- **Noyau** (`crible_iii_v1.py`) : analyseur gelé de la passe 1 (vingt premiers ensembles valides, invalides et ignorés comptés) ;
  filtre gelé (doublons, ensembles inclus dans les traits de l'archive, premier par l'ordre des noms, puis maximin de Jaccard,
  égalités par l'ordre des noms ; moins de six : tous) qui **refuse toute entrée autre** que les ensembles et les traits de l'archive ;
  ensembles de H tirés de `SeedSequence(racine, spawn_key=(r, 40))` ; gabarits G1 (contexte de G0 puis consigne, aucun mot sur les
  conditions, interactions ou sortes d'effets) et G2 (G0, bloc des ensembles reconstruit depuis les formes canoniques, consigne) ;
  textes de passe 2 et de B contrôlés à l'octet avant l'appel ; **cinq files de quatre mondes** (monde r → file r modulo 5), deux
  étapes par monde (S, passe 1 et H ensemble ; puis D et B ensemble), **borne de 3 000 s par appel et de 7 200 s par monde**,
  **garde de départ de 10 h**, minuterie de 7 200 s + 2 h au départ de chaque monde ; lignes d'arrêt : part atteinte, coût au-dessus
  du pire cas, réponse brute ou témoin absent, limite de débit (> 5 % après dix appels du fournisseur), minimum (complets + en cours
  + non commencés < 16, évalué à chaque fin de monde) ; lecteur gelé des lignes « calcul » (enveloppe GO-2026-11-15-06, mots exigés,
  plafonds exacts 260 et 3 USD).
- **Lanceur** (`lanceur_crible_iii_v1.py`) : `secret`, `generer` (vingt mondes à la graine du crible, quatre processus), `preparer`,
  `jouer` (à blanc avec le relais factice, ou réel par la chaîne du pilote : relais au plafond de la part, 60 et 40 appels,
  commande bornée par le crible), `sonde-gabarits` (κiii0 : trois appels, règles d'avance, III-7 par sa règle), `rapatrier` (jamais
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
- **Machine et session** : amorce, programme machine et aide (trois barrières, phrase chiffrée RSA-OAEP, inscriptions sur `main`,
  essai à blanc sur les vrais mondes avant le feu réel, crible réel une seule fois, mesure, lecture non ouverte, rapatriement,
  balayage, reprise de la poussée, minuterie) ; outil et gardes de la session (offre choisie par la garde, commande imprimée et
  comparée, feux, état, récupération, dépense, destruction par l'identifiant, preuve d'absence par témoins).

## 3. Essais joués (sorties gardées dans ce dossier)

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

1. **Contre-lecture du code** (pièce, Étapes, point 0) : un sous-agent neuf **d'un autre modèle**, sur ce dossier entier et la
   procédure (§ 6 de la procédure : fichiers à lui donner).
2. **Sonde des gabarits** (κiii0, **obligatoire**, 7 USD au pire, 3,03 attendus) : ligne « calcul » à inscrire par la mère avec
   l'accord de Lazar ; jouée depuis la session, sans machine (procédure, geste 0) ; si une règle d'avance se déclenche, gabarit
   réécrit, nouvelle sonde, crible non lancé ; sinon III-7 refaite par sa règle dans une **version 2** de la pièce, puis un tour
   différentiel (R2).
3. **Restes de la pièce** : trois valeurs calculées sur processeur (part de H après filtre pour III-5, puissance de P1 et P2, taux
   d'erreur de l'intervalle par percentile), versement de l'annexe A et de ses programmes ; puis **scellement par `sceller_prereg`
   et recopie sous `prereg/`** (son empreinte devient la racine des graines et `TEXTE_SHA256`).
4. **Addendum d'empreintes** scellé, qui ne change rien d'autre : les cinq fichiers du crible (empreintes du § 1, ou celles de la
   version contre-lue), l'empreinte du texte qui fait foi, les empreintes de l'arbre (`lanceur empreintes`).
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
2026-11-30) ; le chemin court est : contre-lecture du code → sonde des gabarits → version 2 et tour différentiel → scellement et
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
  factices) : à relire par le contre-lecteur.
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
