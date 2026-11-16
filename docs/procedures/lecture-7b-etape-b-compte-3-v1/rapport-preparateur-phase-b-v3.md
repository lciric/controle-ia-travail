# Rapport du préparateur — commande de la phase B du compte 3, version 3 — v1

- **Statut** : rapport pour la session mère, qui fait contre-lire, scelle, verse et remet au directeur. Fichier neuf, scellé, non commité.
  Rien n'est décidé ici : les nœuds sont portés à la mère (section 8).
- **Rédacteur** : préparateur neuf, sous-agent de la session mère `session_016QhUrtmLyFWJP6Cy7rgfXH` (modèle A ; aucun identifiant de
  modèle écrit), le 2026-11-16 de 13:12:02Z à environ 13:35Z (`date -u`). Il reprend le travail d'un premier préparateur (modèle B),
  arrêté par une limite d'usage vers 13:05Z avant d'avoir fini, rendu ou scellé. Ni lecteur ni juge d'aucun verdict ; aucune entrée ni
  sortie de 7a, de 7b, de T0.7 ou de l'étape B bis ouverte (section 11).
- **Brief** : celui du premier préparateur (`brief-phase-b-v2.txt`, bloc-notes de la mère,
  `186dc6188e706b8db691ef7f05b805ebe629de4044ce46bb789c30117344084f`), lu en entier, à deux changements près dits par la mère : pièces en
  version 3 ; départ du brouillon v2 scellé par la mère pour son intégrité seulement.

## Verdict

1. **Commande v3 prête pour la contre-lecture** : `commande-compte-3-phase-b-v3.md`
   (`7090cdf0e1c979d921a70fc0159aa3fd6173427aae909c4d17cd495ae121a6ab`, 667 lignes, 14 blocs), tirée du brouillon v2 par 21 couples
   bornés. Le brouillon était presque complet et juste ; aucun défaut bloquant n'y a été trouvé.
2. **Répétition complète sur dépôts jouets : 175 conformes sur 175** ; constantes contre `main` distant (`e3dc0871…`) et le
   distant : **30 sur 30**. La vraie pièce y est jouée par son vrai lanceur, en mode réel, sur entrées factices : codes 0, 2 et 3.
3. **Un nœud ouvert, à trancher avant la ligne `ISSUE-MOTS-ET-COUT-T06`** (point M-1) : l'audit R4 de la base (A) (T0.8, l. 111)
   veut une relecture par un lecteur neuf « avant l'inscription de `ISSUE-MOTS-ET-COUT-T06` » s'il se déclenche ; ni le brouillon,
   ni la phase C v3, ni sa v4 ne disent qui en lit l'état. La commande le dit à sa section 15 sans le lever.

## 1. Le brouillon v2, lu en entier contre le brief et les pièces qu'il nomme

**Fait, et juste** (vérifié contre le code de la pièce, la phase A v2, la phase C v3 et le brouillon 1 de sa v4, le registre) :

- Les quatre marqueurs du gabarit remplis (section 3 de la commande) : commit `da06bb57…` (celui que cite la fiche du code), ligne
  `CODE-MOTS-ET-COUT-T06` à l'octet, appel `PY=… bash scripts/lancer_mots_et_cout_t06_v3.sh --mode reel --racine-entrees … 20261111-151701-t06-reel`,
  motif `[0-9]{8}-[0-9]{6}-mots-et-cout-t06` (`executer` : `f"{instant:%Y%m%d-%H%M%S}-{NOM_PIECE}"`).
- Les gardes de la commande collent à celles de la pièce : `verifier-code` (sortie comparée à la lettre près), contrôle à blanc qui
  appelle les fonctions de `executer` dans son ordre jusqu'à la lecture des entrées exclue (`verifier_modules_geles`,
  `verifier_texte`, `controler_registre_reel`, `ListeBlanche.pour_7b`, `compagnon_conforme`, `exiger_arbre`) ; codes 0, 2, 3 de
  `main` ; sortie à cinq lignes (en-tête et quatre `chemin empreinte`) ; progrès `PROGRES <heure> etape=<nom>` sur la sortie d'erreur.
- Entrées de 7b **hors du dépôt**, par l'option `--racine-entrees` prévue par l'auteur (`rapport-developpeur-code-v3-v1.md`, § 7) :
  la pièce exige alors un arbre propre et un manifeste « dépôt propre » ; aucun fichier de 7b ne peut être commité.
- Défauts déjà trouvés non refaits : appel détaché, marqueur posé avant l'appel, B5b relançable seul (CL3-04, CL3-05) ; contrôle à blanc
  par les gardes de la pièce (CL3-06) ; répétition de bout en bout (CL3-07, CL3-15) ; approfondissement d'un clone superficiel avant la
  recherche du commit (CL3-08) ; versions exactes (CL3-09) ; fichier déjà placé admis s'il est égal (CL3-10) ; aucune fin de journal
  affichée (CL3-20) ; branche neuve tirée de la référence distante, sans passer par `main` local (écart P3A-007 de la phase A).
- Contrainte d'aval tenue (section 9) ; mère et bloc V conformes au § 15 de la phase C.
- Ses trois scripts de répétition (sous `repetition-phase-b-v2/`) : rejoués par son dossier de travail, 168 sur 168 à 13:04:46Z, sur
  le brouillon tel que scellé (`e0dba2aa…`). Je ne l'ai pas tenu pour acquis : la v3 est répétée de nouveau en entier (section 5).

**Manquait** : le rapport (`rapport-preparateur-phase-b-v2.md` n'existe pas, mais le brouillon y renvoyait) ; les sorties de la
répétition et de la vérification des constantes, ni versées ni scellées ; la condition de l'audit R4 avant la ligne d'issue (M-1).

**Faux ou imprécis** :

- En-tête : « même modèle qu'elle, noté modèle A » pour le premier préparateur ; la mère le dit **modèle B** (brief de ma tâche, et
  commit `49705423` « Limite du modèle B »). La v3 écrit modèle B (point M-2).
- Bloc B3 : la taille attendue (« environ 18 960 000 octets ») était comparée à `du -sb`, qui compte les dossiers ; un hôte qui lit
  « toute autre sortie est un arrêt » pouvait s'arrêter à tort. Remplacée par la somme exacte des tailles des cinq entrées.
- Bloc B2 : `pip install` avec cache ; or l'environnement pèse 5,9 Go une fois installé (`.venv` du dépôt de la mère, même
  `requirements-cpu.txt`) et le cache en ajoute autant à peu près ; avec le seuil de 9 Gio, le disque pouvait manquer. Sans cache en v3.
- Bloc 1B : `INTERDITS_NOMS` n'avait pas `bbis` ni `b-bis`, que la phase A porte ; ajoutés (sans effet sur les dix chemins, vérifié).
- Renvois : la commande et ses pièces au nom v2 ; journal provisoire « commande phase B v2 exécutée ».

## 2. Différentiel avec le gabarit (section 9 de `commande-compte-3-v1.md`, `21d891c5…`)

| point du gabarit | commande v3 | écart |
|---|---|---|
| branche `verdict/t06-mots-et-cout-compte-3-v1` créée sur `main` | B1 : `git switch --no-track -c` depuis `refs/remotes/origin/main`, poussée éprouvée égale à `main` | aucun (référence distante : P3A-007) |
| ligne `CODE-MOTS-ET-COUT-T06` comparée à l'octet | B1 (`grep -cxF`, une seule), puis la pièce elle-même (B4, `verifier-code`) | en plus : `SCELLEMENT-T08-BASE-A`, `RUN-CONFIRMATION-T06` ; absence de `LECTURE-T08-BASE-A` et d'`ISSUE-MOTS-ET-COUT-T06` |
| entrées de 7b « placées depuis `$CLONE7B` » (cinq fichiers de P5.2, compagnons, jamais commités) | B3 : dépôt jetable sans contenu, `git show <tête>:<chemin>` par liste positive, **dans le bac, hors du dépôt** ; `--racine-entrees` | **écart voulu** : hors du dépôt plutôt que dans la racine ; aucun fichier de 7b ne peut être commité ; arbre propre exigé par la pièce |
| sorties `diag/<run-mc>/`, `runs/<run-mc>/` absentes avant | B1 et B4 (garde), la pièce aussi (R12) | aucun |
| **un seul appel**, sortie dans `$BAC`, jamais affichée | B5a détaché, marqueur posé avant ; B5-attente ; sortie et progrès dans le bac ; seuls le code, le nom du run, les étapes et, sur un code 2, la ligne de refus sont lus | en plus : borne de 60 minutes (nœud, aucun arrêt de processus) |
| seuls fichiers neufs sous les deux dossiers, scellés, commités seuls, poussés, aucun ouvert | B5b : noms exacts, compagnons, empreintes annoncées par la pièce, index contrôlé, garde des secrets ; F-B : journal provisoire à part | en plus : journal provisoire (noms, empreintes, code ; aucune valeur) |
| la mère vérifie les blobs, lit BA-L2 (N-C), inscrit `LECTURE-T08-BASE-A` puis `ISSUE-MOTS-ET-COUT-T06` | section 15 : bloc V (objets git et empreintes, sans ouverture), puis les deux lignes dans cet ordre, puis le bloc M de la phase C | **ordre** : le gabarit écrit « lit BA-L2 » avant les lignes ; la phase C v3 (§ 15) et le programme du bloc M exigent la ligne `LECTURE-T08-BASE-A` d'abord : la v3 suit la phase C. En plus : condition de l'audit R4 (M-1) |
| marqueurs `<<COMMIT_PIECE>>`, `<<LIGNE_CODE_MOTS_ET_COUT>>`, `<<COMMANDE_PIECE>>`, `<<MOTIF_RUN_PIECE>>` | remplis (section 3) | aucun |

## 3. Différentiel avec le brouillon v2 (les 21 couples de `couples_commande_phase_b_v3_v1.py`)

Le programme vérifie l'empreinte du brouillon (`e0dba2aa…`), exige que chaque ancien texte s'y trouve une fois, puis qu'aucun nom de
la v2 ne reste hors du renvoi au brouillon. Par sujet :

1. **Noms** (huit couples) : titre ; 0b-B lit `commande-compte-3-phase-b-v3.md` sur `main` ; pièces et annexe sous
   `repetition-phase-b-v3/` ; renvoi au rapport v3 ; journal provisoire `…-v3.md`, titre « (v3) », « commande phase B v3 exécutée ».
2. **En-tête** (quatre couples) : paragraphe « Version 3 » (changements, noms du bac gardés à dessein) ; « Brouillon v2 » à la place
   de « Version 2 » ; rédacteurs (modèle B, puis modèle A) ; phase C « v3, ou sa version 4, en cours ».
3. **Bloc B2** (deux couples) : `--no-cache-dir` ; point 4 de la section 0 dit « sans cache de pip ».
4. **Bloc B3** (un couple) : la somme des tailles des cinq entrées, attendue à 18 959 392 octets (P1.4 de `prealables-v1.md`, tailles
   lues au distant à la tête `55c3e3eb` : 8 509 + 1 556 085 + 125 598 + 1 830 726 + 15 438 474) ; une autre somme n'arrête pas (les
   empreintes font foi), elle se dit à Lazar.
5. **Bloc 1B** (un couple) : `bbis|b-bis` dans `INTERDITS_NOMS`.
6. **Section 15** (deux couples) : point 2, la condition de l'audit R4 (M-1) ; point 3, le bloc M est le même, à l'octet, dans le
   brouillon 1 de la phase C v4 (vérifié par la répétition).
7. **Annexe** (trois couples) : noms v3 ; bloc M comparé entre les deux versions de la phase C.

Rien d'autre ne change : blocs, gardes, ordre, rendu et section 14 sont ceux du brouillon.

## 4. Choix faits

- **Programme de couples** plutôt qu'une écriture neuve : les changements sont bornés (21) et le brouillon, répété à 168 sur 168, est
  juste sur le fond.
- **Noms du bac et des fichiers de marque gardés** (`$HOME/bac-mots-et-cout-compte-3-v2`, `variables-v2.sh`,
  `appel-piece-lance-v2.txt`, …), comme la phase C l'a fait de sa v2 à sa v4 : si le brouillon v2 venait à être joué par erreur après la
  v3 (ou l'inverse), le bloc 1B s'arrête sur le bac déjà ouvert ; et de toute façon la branche poussée au bloc B1 arrête l'autre version
  (« existe déjà au distant »). Le journal provisoire, lui, porte `-v3` : il dit quelle commande a été jouée.
- **Taille des entrées** : information, non garde ; les empreintes (compagnons, manifeste contre `RUN-CONFIRMATION-T06`, puis la
  pièce contre `episodes-t06.json`) restent les seules gardes du contenu.
- **Audit R4** : dit et porté en nœud ; je n'ai rien ajouté qui lise un champ de plus de 7b (ce serait étendre R-2741, mot de Lazar).
- **Liste « qui a lu quoi »** : la v2 reste celle de l'attestation (la v3 suit la phase B ; la commande ne change pas si la mère
  verse la v3 avant).

## 5. Répétition (règle R5) : bilan

- `repetition-phase-b-v3/repetition_phase_b_jouet_v3.sh` (`5a5dfaae…`), dérivé de celui du brouillon par
  `deriver_repetition_phase_b_v3_v1.py` (`ef26e50d…`) ; fabrique `fabrique_depots_jouets_phase_b_v3.py` (`b25e1128…`, celle du
  brouillon, noms seuls changés) ; sortie `repetition-phase-b-jouet-sortie-v3.txt` (`8a3535d7…`) : **175 conformes sur 175**, de
  13:24:27Z à 13:26:49Z, en priorité basse (`nice -n 19`), un seul processus lourd. Couverture : les quatorze blocs extraits de la
  commande v3 (épreuve du crochet bloquée, les treize autres passent le crochet) ; chaque bloc sur un cas sain et chaque garde sur un
  artefact ; trois passes (clone complet et installation suivie de bout en bout, code 0 ; clone superficiel approfondi, code 2 ; code 3) ;
  six sessions d'artefacts (1B, B1, B4 par variantes du dépôt distant jouet) ; le bloc V de la mère, ses lignes par
  `registre_v1.ajouter_ligne` dans l'ordre, le bloc M de la phase C rejoué sur une vraie sortie de la pièce, la reprise du fichier
  d'issue comme au bloc C2, la relance refusée par la pièce une fois les lignes écrites.
- **Contrôles ajoutés en v3** (sept) : bloc M du brouillon 1 de la v4 égal à l'octet à celui de la v3 ; forme des blocs C2, C5, F-C des
  deux versions de la phase C (ligne `IS=…`, reprise sur `<<BRANCHE_PIECE>>`) ; somme des tailles au bloc B3 ; nom « bbis » parmi les
  entrées → B3 arrête ; `--no-cache-dir` dans l'installation détachée ; nom, titre et premier fait du journal provisoire v3.
- `repetition-phase-b-v3/verification_constantes_phase_b_v3.sh` (`2c8eff2a…`, dérivé par `deriver_constantes_phase_b_v3_v1.py`,
  `b90df542…`), sortie `verification-constantes-phase-b-sortie-v3.txt` (`7f91a140…`) : **30 sur 30**, à 13:24:14Z, sur `main` distant
  `e3dc0871748593a25caf93b87fbd842effc098e6` : trois lignes du registre à l'octet, deux absentes ; empreintes des pièces et de leurs
  compagnons ; commit de la pièce ancêtre de `main` (224 commits plus bas) ; fiche du code ; contre-lecture citée ; attestation v3 sur la
  liste v2 réelle avec l'identifiant de l'hôte (0 ligne de l'hôte, conforme) ; empreintes de lancement ; versions de
  `requirements-cpu.txt` ; journal des ouvertures (2 lignes, aucune des sondes de T0.6 ni de l'étape B) ; aucun run de la pièce ni
  fichier de 7b suivi sur `main` ; tête `55c3e3eb…` de la branche de 7b ; branche de la pièce absente du distant ; en plus en v3 :
  `INTERDITS_NOMS` ne touche aucun des dix chemins, et la somme 18 959 392 relue à P1.4 de `prealables-v1.md` sur `main`.

## 6. Ce qui n'est pas éprouvé (seul l'hôte peut le jouer)

- L'installation réelle de `requirements-cpu.txt` (environ 6 Go ; trop lourde pour la machine partagée) : le chemin du bloc B2 est
  joué sur des exigences jouets (échec, versions autres, processus disparu, succès), puis les bibliothèques du `.venv` de la mère sont
  rendues visibles par un fichier `.pth`.
- Le transport par GitHub (la répétition pousse vers un dépôt nu local, `file://`) ; le filtre `blob:none` du dépôt jetable de 7b sur
  GitHub.
- L'identifiant de session réel de l'hôte, son crochet de garde, son horloge, son quota, sa place libre, son interpréteur `python3`
  (la mère a Python 3.13.18).
- La pièce sur les entrées réelles : un refus à la lecture des entrées (code 2) ou un arrêt au calcul (code 3) restent possibles ; la
  commande les traite sans relance.
- La lecture par un hôte humainement guidé des « attendu » : c'est la contre-lecture qui le juge.

## 7. Durée attendue chez l'hôte

| blocs | durée | source |
|---|---|---|
| 0-B, 0b-B, 1B, 2B | 5 minutes | phase A (journal provisoire P3A-001 : de 23:03:52Z au journal écrit à 23:27:11Z, lecteur compris) |
| B1 | 1 à 5 minutes (plus si le clone est superficiel et doit être approfondi) | répétition ; taille de l'historique non mesurée |
| B2 | 10 à 20 minutes (téléchargement de torch et de ses bibliothèques) | `.venv` de la mère : 5,9 Go |
| B3, B4 | 2 à 3 minutes | répétition (19 Mo d'entrées réelles contre 7,7 Mo factices) |
| B5a, B5-attente | la pièce : de l'ordre de 0,5 à 3 minutes ; borne 60 minutes | répétition : 29 s sur entrées factices aux effectifs de 7b (5 760 actions) ; textes réels environ deux fois plus lourds |
| B5b, F-B | 2 minutes | répétition |

**Total : environ 25 à 45 minutes de gestes**, dominés par l'installation, plus les temps de conversation. Puis la mère : bloc V,
deux lignes, bloc M, ligne dédiée de BA-L2 (environ 20 à 30 minutes), **après** le nœud M-1.

## 8. Risques et points pour la mère

- **M-1 (nœud, audit R4 de la base (A))** : T0.8 l. 111 : « Audit R4, gelé, toujours calculé […] Action : relecture, avant l'inscription
  de `ISSUE-MOTS-ET-COUT-T06`, par un lecteur neuf, des centres, des coefficients, des comptes et d'un échantillon de 20 actions par
  condition concernée » ; la pièce écrit cet état (réserve R-BA6, `s_applique`) dans `base-a-t08.json`. La mère n'en lit que BA-L2
  (R-2741) ; aucun registre ni aucune commande ne dit qui lit R-BA6 (aucune ligne du registre des décisions ne porte « R-BA6 », compte
  fait par `grep -c`, aucune ligne lue). Décision à prendre par Lazar avant la ligne `ISSUE-MOTS-ET-COUT-T06`. Options : (a) la mère lit
  par programme, en plus de BA-L2, le seul booléen `audit_r4.declenche` (à la racine de `base-a-t08.json`, d'après le code ; la
  réserve R-BA6 en est la copie) ; le lecteur de BA-L2 l'atteint par `--cle-json audit_r4.declenche`, mais imprimerait alors
  l'étiquette « ÉTAT BA-L2 » : un petit lecteur au nom juste, essayé sur un cas sain et sur un artefact, vaut mieux ; s'il est
  déclenché, un lecteur neuf, hors de la mère, fait la relecture avant la ligne ; avantage : lettre de T0.8
  tenue au moindre coût ; inconvénient : étend d'un bit la lecture de 7b par la mère (mot de Lazar). (b) Un lecteur neuf, dans la
  session hôte, lit l'état de l'audit et fait la relecture si besoin, puis rend « déclenché ou non » ; avantage : la mère ne lit rien de
  plus ; inconvénient : une commande de plus, et un lecteur de 7b de plus à inscrire à la liste. (c) Écart déclaré : la relecture passe
  au lecteur B de la phase C ; inconvénient : contredit l'ordre de T0.8 (écart à un texte scellé, nœud). **Recommandation : (a),
  confiance 0,6.**
- **M-2** : lettre de modèle du premier préparateur : son brouillon dit A, la mère dit B ; la v3 écrit B. À confirmer.
- **M-3** : le brouillon v2 et ses scripts sont scellés mais non commités ; s'ils vont sur `main` comme archive, le directeur doit
  donner l'empreinte de la v3 (`7090cdf0…`) : le bloc 0b-B la compare, et les noms de bac communs empêchent de jouer les deux.
- **M-4 (disque)** : environnement de 5,9 Go installé ; sans cache, il faut tout de même la place des roues téléchargées pendant
  l'installation ; le seuil reste 9 Gio, comme la phase C ; je conseille à l'hôte au moins 12 Gio libres. Un manque de place donne
  « installation en échec » : arrêt propre, mais la reprise demande un mot de la mère (le bloc n'efface rien).
- **M-5 (interpréteur de l'hôte)** : la phase A a créé un environnement numpy seul dans son bac ; la phase B en crée un complet dans
  `$DEPOT/.venv`, que la phase C (C1a) reprend tel quel. Si le `python3` de l'hôte n'a pas de roue torch 2.14.1, B2 s'arrête.
- **M-6 (code 2 et information)** : sur un refus à l'étape « entrées » ou « manifeste », la ligne de refus peut citer une forme d'un
  fichier de 7b (un effectif, un début d'empreinte) ; la commande l'envoie à Lazar, qui décide de ce qu'il transmet (section 13,
  point 3), comme R-V3 pour la phase C.
- **M-7** : `main` distant a avancé pendant mon travail (`49705423` → `e3dc0871`) ; les constantes sont vérifiées sur `e3dc0871` ;
  la mère les rejoue juste avant de verser (`verification_constantes_phase_b_v3.sh`, quelques secondes).
- **M-8** : la session hôte est fixée (`session_016QhUrrSUMEzEqWPnQYxjHB`, GO-2026-11-16-05, point 2) ; si elle n'est plus joignable,
  la voie (a) en repli demande une version nouvelle (bloc 1B s'arrête, et la liste doit nommer le nouvel hôte).
- **Risque d'exécution** : le contrôle à blanc ne voit pas le contenu des entrées ; un refus à leur lecture (code 2) reste possible et
  coûte une version nouvelle ; un code 3 est un nœud (BA-L0, aucune ligne d'issue).

## 9. Contrainte d'aval (phase C v3, brouillon 1 de sa v4) : tenue

- `ISSUE-MOTS-ET-COUT-T06` : la mère l'inscrit (section 15, point 2) avec le chemin `diag/<run>/issue-mots-et-cout-t06.json` et son
  empreinte ; les blocs C2, C5 et F-C des deux versions la lisent par `cut -d'|' -f4` (vérifié par la répétition, trois occurrences
  chacune).
- `LECTURE-T08-BASE-A` : inscrite avant, avec `diag/<run>/base-a-t08.json` ; datée avant l'instant du bloc M (une seconde suffit).
- `<<BRANCHE_PIECE>>` : `verdict/t06-mots-et-cout-compte-3-v1` (section 15, point 6), ou `main` si la mère y recopie les sorties par
  leurs objets ; le bloc C2 y reprend le fichier d'issue et son compagnon (répété).
- **Bloc M** : le même dans les deux versions (comparé à l'octet) ; joué sur la branche jouet de la pièce, il rend l'état seul.
- **Section 15** de la phase C : l'ordre « les deux lignes, puis le bloc M, puis la ligne dédiée » n'est pas changé ; la condition M-1
  s'ajoute avant la ligne d'issue sans le contredire.
- État de l'hôte laissé à la phase C : branche de la pièce tirée, arbre propre, `.venv` conforme dans le dépôt (C1a le prend) ; bac
  `bac-mots-et-cout-compte-3-v2` distinct de `bac-etape-b-compte-3-v2` ; `main` local non touché (0b-C l'avance).

## 10. Fichiers à donner au contre-lecteur (chemins sous `docs/procedures/lecture-7b-etape-b-compte-3-v1/` sauf mention)

1. `commande-compte-3-phase-b-v3.md` (`7090cdf0…`) — à juger ;
2. `commande-compte-3-phase-b-v2.md` (`e0dba2aa…`) et `couples_commande_phase_b_v3_v1.py` (`94f957b0…`) — le différentiel ;
3. ce rapport ;
4. `repetition-phase-b-v3/` : `repetition_phase_b_jouet_v3.sh`, `fabrique_depots_jouets_phase_b_v3.py`,
   `verification_constantes_phase_b_v3.sh`, les deux programmes de dérivation et les deux sorties ;
5. le gabarit : `commande-compte-3-v1.md` (§ 9 et § 15) ; le modèle : `commande-compte-3-phase-a-v2.md` ;
6. l'aval : `commande-compte-3-phase-c-v3.md` (blocs C0, C2, C5, F-C, § 15) et `commande-compte-3-phase-c-v4-brouillon1.md` ;
7. les défauts déjà trouvés : `contre-lecture-commande-compte-3-v1.md`, `verification-courte-commandes-v2-v3-v1.md` ;
8. le code : `scripts/mots_et_cout_t06_v3.py`, `scripts/lancer_mots_et_cout_t06_v3.sh`,
   `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json`, `docs/notes/piece-mots-et-cout-v1/rapport-developpeur-code-v3-v1.md` (§ 7) ;
9. les textes : `prereg/T0.8-base-A-mots-et-cout-v1.md` (l. 105-135 et 157-170) et `prereg/T0.6-organismes-v0-v1.md` (l. 765-772) ;
10. `lecture_etat_ba_l2_mere_v1.py`, `attestation_qui_a_lu_quoi_compte_3_v3.py`, `prealables-v1.md` (P1.4, P5.2) ; dans
    `registres/scellements-v1.md`, les lignes par leur clé ; sur la branche `verdict/t06-table-a-7b-compte-3-v1`, seulement
    `registres-provisoires/compte-3-phase-a-2026-11-14-2327-v2.md`, `registres/passations/2026-11-15-1843.md` et
    `docs/procedures/lecture-7b-etape-b-compte-3-v1/brief-relance-compte-3-autre-compte-v1.md` (jamais `docs/verdicts/`).

Le contre-lecteur peut rejouer les deux scripts (environ 2 minutes 30 et 3 secondes ; dossier neuf en argument).

## 11. Déclaration d'exclusion

Rôle : préparateur de la commande ; ni lecteur ni juge. Lettre : modèle A. Heures (`date -u`) : début 13:12:02Z ; fin de rédaction
vers 13:35Z. Lu : le brief (`186dc618…`) ; le brouillon v2 en entier (`e0dba2aa…`) et ses trois scripts (`cff9b069…`, `cfaad459…`,
`22668505…`) ; la sortie de son dossier de travail (`rep3-sortie.txt`, sorties factices) ; `commande-compte-3-v1.md` (`21d891c5…` : en-tête,
§ 9, § 12 à 15, annexe) ; `commande-compte-3-phase-a-v2.md` (blocs 0 à 1) ; `commande-compte-3-phase-c-v3.md` (`9d788919…` : C0, C1a,
C1, C2, C5, F-C, § 12 à 15, 0b-C, 2C) ; `commande-compte-3-phase-c-v4-brouillon1.md` (`f4bcf406…` : en-tête, lignes qui nomment la
phase B) ; `verification-courte-commandes-v2-v3-v1.md` (`cb9757d5…`, § 1, 3 à 6) ; `contre-lecture-commande-compte-3-v1.md` (`092acef6…`,
lignes qui nomment la phase B) ; `rapport-preparateur-v1.md` (lignes qui nomment la phase B) ; `calendrier-et-remise-phase-c-v3-v1.md`
en entier ; `prealables-v1.md` (`0cd96b62…`, lignes P1.4, P5.2) ; `lecture_etat_ba_l2_mere_v1.py` (en-tête) ; le code de la pièce
(`9dbcc55c…`, lanceur `e1d2514c…`) et sa fiche (`e418fdaf…`) ; le rapport du développeur v3 (§ 5 à 7, 9) ; T0.8 base (A) (l. 11, 52,
105-135, 157-170, 218) et T0.6 (l. 765-772), aucun résultat ; les lignes du registre des scellements par leur clé ; les lignes R-2711,
R-2735, R-2741, R-2760, R-2763, R-2765, R-2768 à R-2779, R-2808, R-2845, R-2971 du registre des décisions par leur clé, plus deux comptes
(`grep -c`) sans ligne lue ; GO-2026-11-16-05 ; sur la branche de la phase A, le journal provisoire, la passation et le brief de relance.
**Jamais ouvert** : aucun fichier de `diag/`, `runs/` ou `donnees/` de 7a, de 7b ou de T0.7 ; aucun fichier de la liste interdite ;
aucun fichier de l'étape B bis ; aucun fichier de `docs/verdicts/` de la branche de la phase A (noms vus par `git diff --name-only`,
section « Incidents » du rendu) ; aucune valeur de clé.
