# Chaîne de lancement de la course de la base boîte noire (T0.8) — rapport du développeur — v2

- **Version 2** : remplace la v1 (`docs/notes/t08-chaine-de-lancement-v1/rapport-chaine-de-lancement-t08-v1.md`, `10af579104960c066d099e71954fcaca84b056ddab52386d5d755ddcd43fa721`, gardée telle quelle, R12). Pourquoi : la consigne est passée en v3 pendant que j'écrivais la v1 (ses messages m'ont atteint après la poussée de la v1). La v2 la tient entière.
- **Nature** : rapport de classe C sur du code de classe B (contre-lecture par un autre modèle, puis vérification des corrections par le même contre-lecteur, à demander à la session mère).
- **Auteur** : développeur de la chaîne de lancement de T0.8, session `session_013QMaykVEGYEXUpWBeemUjb` (Opus 5.5), le 2026-11-22, de 19:20 à 21:40 UTC environ.
- **Mandat** : consigne v3, `docs/procedures/t08-course-v1/consigne-chaine-de-lancement-t08-v3.md` (`6f52c4db8d1a3fd0a530cbbfc3cc59e0b0d47f745191d8316aa5d0560e94346e`, branche `prep/t08-texte-complet-fable-v1`, commit `fe2f6185`), empreinte vérifiée. Elle garde les v1 (`722ceb5e…`) et v2 (`a0da4962…`). Ordre de course au brouillon 3 (`6922ada9651f4bbcb9d9347dff105c003c136c702a63b79cc3e5a4f7ae6d01e8`), empreinte vérifiée. Texte : brouillon 14 (`e81e4ddb…`), vérifié.
- **Branche** : `t08/chaine-de-lancement-v1` (consigne v3, § 5). Le code aligné y est fusionné jusqu'à `9efa1c28f`, qui porte la garde de l'instance resserrée (`01fe0ea57`). La fusion n'a réécrit aucune histoire. Tous mes fichiers sont neufs : aucun fichier du code aligné n'est modifié.
- **Aucune machine créée, aucun appel au loueur, aucune dépense** ; aucun résultat de course ni verdict lu (section 7).

## 1. Ce qui est fait

| pièce (consigne v3) | fichier | ce qu'il fait |
|---|---|---|
| 3.1 branche d'entrée | `scripts/construire_branche_entree_t08_v1.py` | extrait par `git show` seul les fichiers que la course lit, avec leurs compagnons ; vérifie chaque empreinte (compagnon, configuration, texte scellé pour les trois fichiers de 7b, commit de 7b cité par le texte) ; écrit une branche **orpheline, neuve** ; contrôle final : liste exacte, aucun interdit, copie à l'octet, objets de l'histoire limités à ce commit, ses arbres et les blobs de la liste ; sous-commande `verifier`, rejouée par le lanceur sans la branche de 7b |
| 3.2 configuration réelle de la course | `scripts/ecrire_configuration_course_t08_v1.py` | écrit `prereg/T0.8-configuration-course-v1.json` (+ compagnon) à partir du texte scellé et des marqueurs du scellement ; contrôle final : `course_v1.exiger_course_reelle` |
| 3.3 lecture en ligne de commande | `src/controle_ia/t08/lire_v1.py`, `src/controle_ia/t08/passage_a_blanc_v1.py`, `scripts/ecrire_configuration_lecture_t08_v1.py` | `lire_v1` n'appelle que `executer_lecture`. Puis, si l'audit R4 est déclenché, il écrit `diag/<run>/echantillon-audit-r4-t08.json` (scellé, rattaché au manifeste de la lecture). L'échantillon recopie à l'octet, pour les seules clés désignées, la ligne du texte de l'action, le coût lu et la ligne de chacun des quatre fichiers de lectures des juges. Le score de chaque ligne recopiée doit égaler celui du résultat, et `lecture-t08.json` n'est pas changé. La sortie ne porte que des chemins et des empreintes (aucun nombre de résultat) ; le passage à blanc ; la configuration de la lecture aux empreintes inscrites |
| 3.4 lanceur | `scripts/lancer_t08_v1.sh` (copie de `lancer_t06_v13.sh`) | section 4 |
| 3.5 amorce | `scripts/amorce_instance_t08_v1.sh` (copie de `amorce_instance_t06_v11.sh`), `scripts/tests-cibles-t08-v1.txt` | section 4 ; **commit local de la course** (§ 3.5, six conditions) |
| (nécessaire) module de session | `src/controle_ia/lancement_t08/session_v1.py` | ligne de GO lue au registre **avec sa prolongation** ; calendrier lu au registre ; vue de l'offre sans relance ni H200 ; surveillance avec l'alerte du compte rendu à 40 USD |
| (nécessaire) commit local | `src/controle_ia/lancement_t08/commit_local_v1.py` | liste attendue, contrôle de la branche d'entrée, contrôle du commit local, contrôle par l'exécutante après la poussée (bibliothèque standard et git seuls) |
| (§ 4) essais | `tests/test_t08_chaine_*_v1.py`, `tests/aide_t08_chaine_v1.py`, `scripts/essai_jouet_chaine_t08_v1.py`, `scripts/differentiel_annote_t08_v1.py` | section 3 |

### Le commit local de la course (§ 3.5) : conditions, et comment elles sont tenues

| condition | tenue par |
|---|---|
| (i) seul parent : le commit que cite `CODE-T08` | `commit_local_v1.verifier` dans l'amorce, juste après le commit, puis de nouveau dans les gardes, avant tout calcul (`rev-list --parents`) |
| (ii) n'ajoute que les entrées de la course, le texte scellé, la configuration et leurs compagnons ; rien sous un chemin gelé ; liste écrite avant, contrôlée avant la course | liste écrite **avant** le commit (`$R/t08-liste-attendue.txt`), tirée de la configuration copiée : ses entrées, le guide de classification chargé par le code, la configuration et le texte. La branche d'entrée doit égaler cette liste. Après le commit : chaque chemin du diff est un ajout (aucune modification), les ajouts égalent la liste moins les fichiers déjà suivis au commit cité (tâches, consignes, invites, identiques), et aucun n'est gelé. La liste est poussée avec les traces |
| (iii) entrées de la branche d'entrée seule | l'amorce ne recopie que `git show ENTREE_COMMIT:<chemin>` ; la branche de 7b n'est jamais demandée |
| (iv) poussé avec les sorties | la branche de sortie est créée depuis le commit local (poussée initiale), et les sorties s'y ajoutent |
| (v) auteur et date fixés | auteur « instance de calcul (T0.8) » ; date d'auteur et de commit = date du commit de la branche d'entrée ; message fixe. Il se refait à l'identique hors de la machine (même arbre, même parent) |
| (vi) contrôle par l'exécutante | `commit_local_v1 verifier-distant` (section 8, étape 9), par les noms seuls |

**Ce que faisait l'amorce de la course de confirmation** : aucun commit local. Son texte, sa configuration, ses tâches et ses consignes étaient dans le commit scellé `S` de `main` qu'elle clonait ; ses entrées étaient produites sur la machine. Le manifeste portait donc `S` lui-même. Ici, le texte cite le commit du code et ne peut pas s'y trouver, et les entrées de 7b viennent d'une autre branche : la tête est forcément un enfant du commit cité. La v1 de cette chaîne gardait la tête au commit cité en tenant les entrées hors de l'index par `.git/info/exclude`. La consigne v3 fixe le commit local : la v2 le suit.

## 2. Fichiers et empreintes

Chaque fichier a son compagnon `.sha256` (R6). Les compagnons des fichiers de code changés depuis la v1 sont remis à jour, les précédents restant dans l'histoire git (réserve 10). Le commit qui les porte est celui de la poussée (message à la mère).

| fichier | sha256 |
|---|---|
| `scripts/construire_branche_entree_t08_v1.py` | `8ff94322224fda792f04d539cd3f4d96bf855501e2f9c2a9c954e71887cb42e4` |
| `scripts/ecrire_configuration_course_t08_v1.py` | `4f98dd2df2faa3849b81f9e17a6daad4a7d0e839b6096640251b658e375e2f47` |
| `scripts/ecrire_configuration_lecture_t08_v1.py` | `aafea682d4a34b6560f0291f8ea6dac50a49165e2b860a355fd67bcbfc1176a6` |
| `scripts/lancer_t08_v1.sh` | `d9c8703c23c81ec8999317acc8882d6c75c962c744b5dcde18af606490cf23c8` |
| `scripts/amorce_instance_t08_v1.sh` | `9bd637135310ba9330ab54d2148da3b8197dafe63b6ee439dc8b850e8ce28711` |
| `scripts/tests-cibles-t08-v1.txt` | `5b6db29b7434c3bd38c6178d04b790572e96f767c1ba36410694fcb2a0000c2c` |
| `scripts/essai_jouet_chaine_t08_v1.py` | `7f354b329d7b0d2e07e60e2216f79f0ac087bef51a09d885496d2ca226b4aaf7` |
| `scripts/differentiel_annote_t08_v1.py` | `32e8a3a1afb753686517486adf8e8da57995445fbec053f1e7ed32d639bc74e3` |
| `src/controle_ia/t08/lire_v1.py` | `a757d643bbe06b66ff9504cc28494f7d24732f29a1474359bfa8f5383c7f8daa` |
| `src/controle_ia/t08/passage_a_blanc_v1.py` | `13d17d9a58bf7d2ed8ba188c8fa09900d361065020f3e67a0f9c4e4ca13c0cb9` |
| `src/controle_ia/lancement_t08/__init__.py` | `8f7a415376e25f1bd8b0821b3f55f88947ad142723ef48fb349b780eca68644c` |
| `src/controle_ia/lancement_t08/session_v1.py` | `c598af5b93d5ee4a207e80a8fb5ba6cff0304772b9968b31c7fae25e549ab730` |
| `src/controle_ia/lancement_t08/commit_local_v1.py` | `67463082198831de7eb7c216331bab61fb445d57456d153dcfeaa8c80a56cbee` |
| `tests/aide_t08_chaine_v1.py` | `0ccce84dfa0cdc9c8608a3c973879fb9a3f8acccc40f896de57f312b9cd6305f` |
| `tests/test_t08_chaine_branche_entree_v1.py` | `035806967bbfd2ba57f8c74735b1a1a00b0e5c7f0ef849a998cdeaff05cb42cd` |
| `tests/test_t08_chaine_configuration_v1.py` | `07bcb2b166ce4cebce145d2682611e6e70fb6502b78b46444d9807d3aa5f3781` |
| `tests/test_t08_chaine_lecture_v1.py` | `a38d42c53c899ee00a195bbe3532b8673710cf3ba0ac4e75f0ef39cfbf5ed52a` |
| `tests/test_t08_chaine_lancement_v1.py` | `b03c67900c5af14fec4dc68684a093aad3b75432e393110e99e7147dd1ace702` |
| `tests/test_t08_chaine_amorce_v1.py` | `ebe31cc4c77bbe1946db5735f89e555720774cc2751e953aaa99aa1eb6921afe` |
| `docs/notes/t08-chaine-de-lancement-v1/differentiel-annote-v2.md` | `682f632d482bbd1461e308f59b2e935dc67b45a8681337fae70206246708008c` |
| `docs/notes/t08-chaine-de-lancement-v1/essai-de-bout-en-bout-v2/comparaison-a-b.json` | `f702988f8e4c141351e25415efe7682a1fb3fcb7ad82aebd99ca7cc42931be4b` |
| `docs/notes/t08-chaine-de-lancement-v1/essai-de-bout-en-bout-v2/journal-instance-a.txt` | `7cc5bf5ef8c3be1e33f94096fcff866e582a47b33fb4f6de0b23312b163ecd67` |
| `docs/notes/t08-chaine-de-lancement-v1/essai-de-bout-en-bout-v2/journal-instance-b.txt` | `bc296cac430409a24b6539b05816b33914dc88ec893ad65fc0692006777edb34` |
| `docs/notes/t08-chaine-de-lancement-v1/essai-de-bout-en-bout-v2/lecture-jouet-echantillon-sortie-erreur.txt` | `476716d96399bf081aa44b0dc2722c49b15d60238d6087eb7dc96eb670d9d2ff` |
| `docs/notes/t08-chaine-de-lancement-v1/essai-de-bout-en-bout-v2/lecture-jouet-echantillon-sortie-standard.txt` | `2f0471c67baa5cb2217e17eef4baee06bbd1dd392ad96b701620c0793987284e` |
| `docs/notes/t08-chaine-de-lancement-v1/essai-de-bout-en-bout-v2/liste-attendue-a.txt` | `25ccdec8acaf6eb90a40dfcf5a072083b8f251c5c7d6c7b204deda4aa588333d` |
| `docs/notes/t08-chaine-de-lancement-v1/essai-de-bout-en-bout-v2/liste-attendue-b.txt` | `25ccdec8acaf6eb90a40dfcf5a072083b8f251c5c7d6c7b204deda4aa588333d` |
| `docs/notes/t08-chaine-de-lancement-v1/essai-de-bout-en-bout-v2/rapport-a.json` | `3c617562a9e56d6c5751ff219c7a58617304c1d6de63aebad4703e4a6d72d759` |
| `docs/notes/t08-chaine-de-lancement-v1/essai-de-bout-en-bout-v2/rapport-b.json` | `9cbb0b161b4aba63192699886250ec68aa85ea69f19243baffcd2579a0c106c6` |
| `docs/notes/t08-chaine-de-lancement-v1/essai-de-bout-en-bout-v2/verification-executante-a.txt` | `3f52dfdfd8b2d9ab561d226236eed12d81be92ea8855cbaf4f9168c1c397775d` |

## 3. Essais (R5 : cas sain et artefact pour chaque garde) et nombres

Environnement : `.venv` de `requirements-cpu.txt`, Python 3.13, git 2.43 ; aucun réseau du loueur. **Suite de T0.8 dans le dépôt, état final : 261 passés, 5 sautés, en 253 s.** Économie d'usage (mot de la mère) : essais limités aux fichiers touchés, suite entière une fois à la fin.

| essai (consigne v3, § 4) | cas sain | artefacts | issue |
|---|---|---|---|
| mode jouet de bout en bout, deux fois, sorties égales (`scripts/essai_jouet_chaine_t08_v1.py`) | deux essais (a, b), même entropie (12345) : code 0, fin normale, 428 s et 415 s. Chacun fait : clonage (12 motifs), branche d'entrée, commit local `349b806e74259bd1823f3cde64846a822f359376`, **identique dans les deux essais** (condition v), 10 ajouts déclarés, rien de gelé ; gardes (aucun interdit, run de 7b lu) ; 248 essais passés, 1 écarté ; course jouet ; poussée (code de l'essai, commit local, résultats et données, traces). Contrôle de l'exécutante (`verifier-distant`) sur le dépôt distant de l'essai a : code 0. Lanceur : contrôles, création imprimée et admise par la garde, après-création, surveillance jusqu'à « FIN » (essais du lanceur) | — | **sorties égales** : 12 fichiers de données identiques à l'octet, `resultat` de `course-t08.json` égal (identifiant du run normalisé : il vient de l'heure). Exclus, déclarés : le manifeste du run et son compagnon, le compagnon de l'enveloppe. Pièces : `docs/notes/t08-chaine-de-lancement-v1/essai-de-bout-en-bout-v2/` |
| minuterie | heure non atteinte : rien | heure passée : consignation, puis `PUT stopped`, puis `DELETE`, dans cet ordre ; 120 USD au journal | passés |
| garde de calcul | GO d'origine, prolongation admis | sans GO, échu, de type « décision », absent : refusés | passés |
| offre | A100 dans les bornes choisie | H200 seule, prix, mémoire vive, mémoire de carte, cœurs : code 3 ; carte `relance` : code 2 | passés |
| clonage | (bout en bout) | fichier de sondes dans la branche d'entrée ; `resume.json` de 7b dans les objets git du code (garde resserrée) ; branche d'entrée déplacée : arrêt avant tout calcul | passés |
| plafond restant (O-2) | dépense antérieure nulle : heure du plafond entier | 50 USD antérieurs : heure plus proche de 50 / 1,05 h, à 32 s près (les deux créations ne sont pas à la même seconde) ; reste nul (119,6 USD + forfait de téléchargement 0,4) : aucune création, code 3 | passés |
| accord prolongé (O-3), dates simulées, lignes réelles des accords, garde du dépôt **inchangée** | 26 et 30 novembre : `GO-2026-11-10-12` admis ; 5 décembre : `GO-2026-11-22-79` admis, plafond lu 120 USD à la ligne d'origine | 5 décembre : `GO-2026-11-10-12` refusé ; 2 janvier : les deux refusés ; prolongation d'un autre accord : refusée ; après l'échéance de l'origine, la commande imprimée ne porte que la prolongation, et l'origine ajoutée la fait refuser par la garde | passés |
| antériorité au passage à blanc (m-O2) | lignes antérieures : code 0 | `SCELLEMENT-T08` postérieure : refus ; course déjà inscrite ; autre texte | passés |
| alerte de deux heures (m-O2) | ligne de progression vieille de 10 min : « POURSUIVRE » | 2 h 01 sans ligne : alerte, « aucun arrêt » | passés |
| échantillon de l'audit (L-2) | sur la lecture jouet (audit déclenché) : 180 clés, exactement celles que le résultat désigne ; `lecture-t08.json` garde son empreinte | audit non déclenché : aucun fichier ; clé hors de l'échantillon : refus ; score recopié ≠ score du résultat : arrêt | passés |
| sortie de la lecture (m-L1) | sur la lecture jouet : 12 lignes imprimées, aucune ne porte de nombre isolé | une ligne qui en porte un fait échouer le critère | passés |
| commit local | (bout en bout : liste exacte, parent = commit cité, la course part) | un fichier de plus, de moins dans la branche d'entrée (amorce : arrêt avant l'installation) ; de plus, de moins, sous un chemin gelé, un autre parent, une modification (module) ; contrôle par l'exécutante après la poussée | passés |
| différence ligne par ligne | `docs/notes/t08-chaine-de-lancement-v1/differentiel-annote-v2.md` | un bloc sans raison arrête le programme | engendré |

Effectifs par fichier : branche d'entrée 9 ; configuration de la course 9 ; lecture 13 ; session, lanceur, garde, minuterie, plafond restant, accord prolongé, alerte 51 ; amorce et commit local 12.

**Liste figée de la machine** (`scripts/tests-cibles-t08-v1.txt`, `5b6db29b7434c3bd38c6178d04b790572e96f767c1ba36410694fcb2a0000c2c`, inchangée depuis la v1). Elle porte 13 fichiers : tous les `tests/test_t08_*.py` sauf `tokeniseur_balise` (4 essais sautés sans le tokeniseur réel) et `chaine_amorce` (il construit un dépôt par `git archive` du dépôt courant). Un essai du code aligné est écarté par l'amorce : `test_t08_entrees_rendu_v1.py::test_amorce_instance_clone_de_l_arbre_aligne`. Il clone l'arbre entier du dépôt, et sur la machine, clone partiel, il tirerait tout l'arbre de `main` depuis GitHub ; il se joue dans la session, sur l'arbre complet. Résultat : **248 passés, 1 écarté**, dans un clone réduit aux 12 motifs, en 149 s ; nombre écrit en dur dans l'amorce. Il est à remesurer sur le commit que citera `CODE-T08`.

## 4. Différences déclarées avec la chaîne de la course de confirmation

Différentiel annoté, ligne par ligne avec la raison de chaque bloc : `docs/notes/t08-chaine-de-lancement-v1/differentiel-annote-v2.md`. La v1 (`differentiel-annote-v1.md`) est gardée telle quelle.

**Lanceur** (8 blocs ; 101 lignes retirées, 90 ajoutées) : inchangé depuis la v1. Il porte les noms ; le GO toujours par `GO_ID`, lu au registre avec sa prolongation ; un `controles` refait pour T0.8 ; `controles-epreuve` refusée (code 2) ; la carte `relance` refusée ; le plafond 120 ; les bornes lues dans la vue de l'offre ; l'alerte unique de compte rendu à 40 USD. Le plafond restant est déjà tenu par `session_v3 depense` : l'heure d'épuisement vaut création + (120 − antérieure − forfait de téléchargement) / prix horaire. La consigne ne retranche que l'antérieure ; le forfait (≈ 2 USD) est retranché en plus, comme dans la chaîne de la course de confirmation (écart plus prudent, déclaré). L'identifiant `GO_T08.id` (`GO-2026-11-10-12`) de la configuration ne passe jamais dans la commande de création : seul `GO_ID` y passe, deux fois (préfixe et `GO_ID_T08`).

**Amorce** (13 blocs ; 198 lignes retirées, 224 ajoutées) : changements de la v1, plus :
- le commit local (§ 1) ;
- les chemins des entrées ajoutés aux motifs d'extraction ;
- la garde resserrée appelée avec le run de 7b, lu dans la configuration (en mode réel, égal à `RUN_7B`) ;
- l'essai écarté, compté par pytest (« 1 deselected ») ;
- le nombre attendu, 248.

## 5. Défauts trouvés par mes essais, et corrigés

1. (v1) Commentaires insérés au milieu de quatre lignes du lanceur : la garde de l'offre devenait un commentaire.
2. (v1) `.gitignore` non extrait : les caches de pytest salissaient l'arbre et la course refusait de partir.
3. (v1) Ajouts hors des motifs d'extraction refusés par `git add` (désormais `git add --sparse`).
4. (v2) **Entrées commises retirées du disque** : la création de la branche de sortie réappliquait l'extraction partielle, et les entrées du commit local, hors des motifs, disparaissaient. La course refusait (« configuration absente »). Corrigé : leurs chemins exacts rejoignent les motifs avant le commit.
5. (v2) Essai du code aligné qui clone l'arbre entier : il échoue sur l'arbre restreint de l'essai et serait dangereux sur la machine. Il est écarté de la suite jouée par l'amorce (section 3).

## 6. Réserves, et ce que je n'ai pas pu vérifier

1. **Levée** (v1, bloquante) : la garde de l'instance est resserrée au `resume.json` de 7b dans le code aligné (`01fe0ea57`, décision de la mère, option (a), confirmée par le rédacteur). L'amorce l'appelle avec le run de 7b ; l'artefact `resume.json` de 7b dans les objets git du code arrête bien.
2. **Commit cité par `CODE-T08`** : il doit porter le code aligné **et** cette chaîne. Sur la machine, l'amorce lit `lancement_t08/*`, la liste figée et les essais de la chaîne au commit cité, et `exiger_code_au_commit` compare `scripts/`, `src/` et `tests/` à ce commit. La mère me donne ce commit ; ensuite, il faut remesurer le nombre et l'empreinte de la liste, et rejouer l'essai de bout en bout.
3. **Registre des GO de la branche de l'alignement** : la ligne `GO-2026-11-22-98` y porte une échéance illisible (« réinitialisation hebdomadaire »). La garde de calcul y bloque alors toute commande de lancement, y compris une simple commande de terminal qui en cite le texte (vu le 22 novembre). Sur `main`, la ligne est corrigée (« — »). La création doit se lancer depuis un clone de `main` à jour. Le module de session ne lit que les lignes qu'il emploie et n'est pas touché.
4. **Fin et destruction** : héritée, l'amorce demande l'état « stopped » ; le texte veut la destruction après la vérification de la poussée. Non changé (la consigne ne le nomme pas) : la commande de destruction est à l'étape 11.
5. **Taille des sorties** : les lectures avec raisonnement (7 040 lectures, textes compris) ont une taille inconnue. Au-delà de 90 Mo, un fichier est retiré du commit et laissé sur la machine, et la course finit en anomalie (récupérable avant destruction).
6. **Jamais joués ici** : le mode réel (carte, modèles, chargement hors ligne, juges réels), le vrai loueur, la poussée vers GitHub depuis un clone partiel d'une seule branche (éprouvée vers un dépôt `file://` seulement), l'image `python:3.11-bookworm`.
7. **Section `lancement` dans la configuration de la course** : lue par la chaîne seulement. La course l'ignore, mais elle entre dans l'empreinte canonique de la configuration.
8. **Lignes de GO admises** : `GO-2026-11-10-12`, puis `GO-2026-11-22-79`. `GO-2026-11-22-93` n'est pas admise : son périmètre ne nomme l'origine qu'en abrégé.
9. **Messages d'arrêt du code de lecture qui portent un nombre tiré des données ou des résultats** (m-L1, relevés sans les changer) :
   - `statistiques_v1.py` l. 31 : comptes d'alertes hors domaine ;
   - `tables_v1.py` l. 160 : borne de T6-10 ;
   - `mots_et_cout_v1.py` l. 306, 314, 316 : centre, état et traits de M2 au contrôle d'identité.
   Un arrêt de la lecture écrit aussi son motif dans `arret-lecture-t08.json`.
10. **Compagnons des fichiers de code** : remis à jour avec le code dans cette version, les précédents restent dans l'histoire git (commit `9675ddd5e`). Rapport et différentiel sont versionnés par leur nom.
11. Mémoire vive : 64 Go s'écrit 64 000 Mo. L'entrée de lecture n'imprime ni la table D, ni les qualifications, ni la durée.

## 7. Ce que j'ai lu, et ce que je n'ai pas ouvert

**Lu** :
- `CLAUDE.md` ; consignes v1 et v3 (différence) ; ordre de course, brouillons 1 et 3 (préalables et étapes) ;
- brouillon 14 du texte (plan, points 1 à 5 et 10 ; liste d'arrêt ; machine, devis et dépense ; calendrier ; ordre des lectures ; alignement ; gardes ; panne ; marqueurs) ;
- le code de T0.8 : `course_v1`, `configuration_v1`, `entrees_v1` (garde resserrée comprise), `essai_jouet_v1`, l'étape (i) et les en-têtes de `lecture_v1`, les champs des lectures de `juges_v1`, les entrées de la pièce HD dans `temoin_distille_v1`, les messages d'arrêt de `statistiques_v1`, `tables_v1`, `sequentiel_pas_lus_v1`, `donnees_v1`, `mots_et_cout_v1`, et l'essai `test_amorce_instance_clone_de_l_arbre_aligne` ;
- les scripts de la course de confirmation et leurs modules de session ; des passages de l'amorce de l'étape B bis ; `.claude/hooks/garde_calcul.py` ;
- dans `registres/go.md` : l'en-tête, les lignes des trois accords et la ligne `GO-2026-11-22-98` (sur la branche de l'alignement et sur `main`) ;
- `registres/qui-a-lu-quoi-v20.md` : en-tête et table ;
- les noms des `resume.json` de l'arbre du code, par `git ls-tree`.

Les sorties jouet (factices) de mes essais : résultats et échantillon de la lecture jouet.

**Jamais ouvert** :
- aucun fichier de `diag/`, `runs/` ou `donnees/` d'une course réelle ;
- la branche de sortie de 7b n'a pas été récupérée dans mon clone ;
- aucune branche `calcul/…` ni `verdict/…`, rien de `docs/verdicts/` ;
- aucune pièce du saboteur, du bras A ni du bras d'attaque.

Aucun refus d'outil, sauf un, cité en réserve 3 : la garde de calcul a bloqué une commande de terminal dont le texte contenait la commande de création (`vastai create`). Je l'ai écrite autrement (par l'outil d'édition de fichier), sans contourner la garde.

## 8. Commandes exactes de chaque étape de l'ordre de course (pour son brouillon des commandes)

Variables communes (à remplir par la mère au scellement) :
- `S` : commit de `main` qui ajoute le texte scellé ;
- `C` : `COMMIT_CODE_T08` ;
- `BC` : branche qui porte `C` ;
- `EA` : empreinte de `scripts/amorce_instance_t08_v1.sh` au commit `C` ;
- `GO` : `GO-2026-11-10-12` jusqu'au 30 novembre, `GO-2026-11-22-79` à partir du 1er décembre ;
- `ANT` : dépense antérieure sous cet accord (registre des dépenses) ;
- `D` : dossier de travail neuf ;
- `ID` : identifiant de la machine, lu dans `$D/lancement.txt`.

Toutes les commandes se lancent depuis un clone de `main` à jour (réserve 3).

- **Au scellement (mère)** :
  - Configuration : `PYTHONPATH=src python3 -B scripts/ecrire_configuration_course_t08_v1.py --texte prereg/T0.8-bases-boite-noire-v0-v1.md --marqueurs <marqueurs.json du scellement> --go-admis GO-2026-11-10-12,GO-2026-11-22-79 --sortie prereg/T0.8-configuration-course-v1.json`, puis commit sur `main`.
  - Récupération de la branche de 7b : `git fetch origin refs/heads/calcul/t06-confirmation-7b-v1:refs/remotes/origin/calcul/t06-confirmation-7b-v1`.
  - Branche d'entrée : `python3 -I -B scripts/construire_branche_entree_t08_v1.py construire --depot . --branche entree/t08-course-v1 --commit-7b 55c3e3eb89a4650419f35999aaa4c54288275b0d --commit-code $C --commit-texte $S --texte prereg/T0.8-bases-boite-noire-v0-v1.md --config prereg/T0.8-configuration-course-v1.json`, puis `git push origin refs/heads/entree/t08-course-v1`.
- **P1** : `sha256sum prereg/T0.8-bases-boite-noire-v0-v1.md && cat prereg/T0.8-bases-boite-noire-v0-v1.md.sha256 && grep '^| SCELLEMENT-T08 ' registres/scellements-v1.md`, puis `PYTHONPATH=src python3 -c 'import sys; from controle_ia.prereg import problemes; p = problemes("prereg/T0.8-bases-boite-noire-v0-v1.md"); print(p); sys.exit(1 if p else 0)'`.
- **P2** : `grep '^| CODE-T08 ' registres/scellements-v1.md && git merge-base --is-ancestor $C origin/$BC`.
- **P3** : `PYTHONPATH=src python3 -m controle_ia.t08.passage_a_blanc_v1 --config prereg/T0.8-configuration-course-v1.json --registre registres/scellements-v1.md --prereg prereg/T0.8-bases-boite-noire-v0-v1.md --racine-piece .` (code 0 exigé) ; essai de la garde : `PYTHONPATH=src python3 -m pytest -q tests/test_t08_chaine_lecture_v1.py -k passage_a_blanc`.
- **P4** : `GO_ID=$GO bash scripts/lancer_t08_v1.sh --verifier-go-seulement prereg/T0.8-configuration-course-v1.json $ANT` ; garde à blanc et dates simulées : `PYTHONPATH=src python3 -m pytest -q tests/test_t08_chaine_lancement_v1.py -k "garde_de_calcul or accord_prolonge or sans_identifiant_echu"`.
- **P6** : `python3 -I -B scripts/construire_branche_entree_t08_v1.py verifier --depot . --ref refs/remotes/origin/entree/t08-course-v1 --commit-texte $S --texte prereg/T0.8-bases-boite-noire-v0-v1.md --config prereg/T0.8-configuration-course-v1.json` (le lanceur la rejoue à l'étape 3).
- **P8** : `PYTHONPATH=src python3 -m pytest -q tests/test_t08_chaine_lancement_v1.py -k "minuterie or plafond_restant or deux_heures"`.
- **Étape 3** : `GO_ID=$GO T08_BRANCHE_ENTREE=entree/t08-course-v1 T08_BRANCHE_CODE=$BC T08_AMORCE_SHA256=$EA bash scripts/lancer_t08_v1.sh controles $D`. Code 0 exigé ; jetons `HF_TOKEN` et `CONTROLE_IA_GITHUB_TOKEN` présents par leur nom.
- **Étapes 4 et 5** : `GO_ID=$GO bash scripts/lancer_t08_v1.sh creation auto course $ANT $D` ; relire la commande imprimée.
  - Champs à relire : carte, prix, `--disk 100`, amorce, `BRANCHE_ENTREE` et `ENTREE_COMMIT`, `COMMIT=$C`, `GO_ID=$GO`, et `DEPENSE_EPUISEE_UTC_S` (heure du plafond restant).
  - Codes : 0 commande imprimée ; 2 échec ; 3 nœud (aucune offre conforme, instance présente, reste nul).
- **Étape 6** : exécuter la commande imprimée telle quelle (elle appelle `apres-creation`). Code 5 : offre retirée ; relancer `creation` comme imprimé (trois essais au plus).
- **Étape 8** : `INTERVALLE=1800 bash scripts/lancer_t08_v1.sh surveillance $ID $D` (codes : 0 fin ; 3 arrêt ; 4 refus de l'amorce).
- **Étape 9** :
  - Récupération et inventaire : `git fetch origin refs/heads/calcul/t08-course-v1:refs/remotes/origin/calcul/t08-course-v1 && git ls-tree -r -l refs/remotes/origin/calcul/t08-course-v1 -- runs diag donnees traces`.
  - Empreinte du résultat : `git show refs/remotes/origin/calcul/t08-course-v1:diag/<run>/course-t08.json | sha256sum`, à comparer à `…/course-t08.json.sha256`.
  - **Commit du manifeste (condition vi)** : `PYTHONPATH=src python3 -I -B -c "import sys; sys.path.insert(0, 'src'); from controle_ia.lancement_t08 import commit_local_v1 as c; sys.exit(c.main(sys.argv[1:]))" verifier-distant . refs/remotes/origin/calcul/t08-course-v1 $C refs/remotes/origin/entree/t08-course-v1`. Code 0 : le premier commit après `$C` sur la branche de sortie a `$C` pour seul parent ; ses ajouts sont exactement les fichiers de la branche d'entrée non suivis au commit cité ; rien n'est gelé.
- **Étape 11** : `vastai destroy instance $ID` (R10), puis `vastai show instances --raw` (inventaire final).
- **Lecture (lecteur neuf, après `COURSE-T08`)** :
  - Configuration : `PYTHONPATH=src python3 -B scripts/ecrire_configuration_lecture_t08_v1.py --texte prereg/T0.8-bases-boite-noire-v0-v1.md --config-course prereg/T0.8-configuration-course-v1.json --registre registres/scellements-v1.md [--hd <chemins de la pièce HD>] --sortie prereg/T0.8-configuration-lecture-v1.json`.
  - Lecture : `PYTHONPATH=src python3 -m controle_ia.t08.lire_v1 --config prereg/T0.8-configuration-lecture-v1.json --run-id <AAAAMMJJ-HHMMSS>-t08-lecture --prereg prereg/T0.8-bases-boite-noire-v0-v1.md`.
  - **Fichier d'échantillon pour la consigne du lecteur** : `diag/<run de la lecture>/echantillon-audit-r4-t08.json` (chemin et empreinte imprimés sur la sortie standard ; `null` si l'audit n'est pas déclenché).
