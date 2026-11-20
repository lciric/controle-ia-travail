# Vérification du générateur de l'étage 2 à 200 (ligne 3) — v2 — v1

Pièce de travail (classe C), 2026-11-20, par le contre-lecteur neuf, modèle S, sous le mandat `83711f92e5308584c8f8a85d47f52c16ae9ce50250d0000af947aff437db7402` (en-tête compris). Suite de `contre-lecture-generateur-etage-2-v1.md` (`d3b72675…`). Le fichier des cartes n'a été ouvert ni par moi, ni par un programme que j'ai lancé ; rien sous `archives-reponses-modeles/` ; aucun appel à un fournisseur, aucune clé, aucune écriture dans le dépôt ni dans le clone.

## Verdict : Conforme

Les corrections demandées sont portées ; rien d'autre ne change que ce qui est déclaré ; les 89 essais passent ; l'exercice M6 n'a ni réseau ni clé. Quatre remarques non bloquantes (R1 à R4, § 6), dont une pour la mère.

## 1. Table et pièces

`table-empreintes-generateur-v2.txt` (`f763d167f9b6c7fda36d6dca4052c068e3b6e63f078b6b6525638b365ed97228`) : compagnon égal ; les six lignes recalculées égales : programme `a3a4e82f15afbabfb53a954e24ed9db709c5d8f2da5f907978e7612e3fddca65`, essais `1b56764350280efd238b8ad89cb3d16864bce28ef812ab367ee8d40d7c5fbe5a`, fragments `a66cf6d4…` (égal à la v1 : octets identiques), différentiels `87157eef…` et `b03debc3…`, rapport `64254de5…`. Les sept compagnons `.sha256` du dossier v2 sont égaux.

## 2. Essais : lecture d'abord, puis rejeu

Lu avant tout lancement (`essais_generer_temoins_ligne_3_v2.py`) :
- **Fichier des cartes** : le chemin réel n'apparaît que dans une comparaison de chaînes (l. 800-801) ; `EntreeCartes.production()` est construite, jamais lue (l. 804-805). Toutes les garde jouées passent par `EntreeCartes.essai` (fixture, l. 137 ; l. 1095-1098). Les trois appels de `principal(["garde", …])` sans entrée explicite (l. 1070, 1075) ont `jouer_la_garde` remplacée par une fonction qui lève : rien ne s'ouvre. `principal(["creer-journal-rejeux", "--journal", …])` (l. 635) est refusé par `len(argv) != 1` (programme l. 1838) avant toute création : rien n'est écrit sous `DEPOT/runs/`. `LieuDuJournal.production()` est seulement construit (l. 640).
- **Réseau** : le seul essai qui charge du code du clone (M6, l. 1153-1173) retire les variables de mandataire et remplace `socket.socket` et `socket.create_connection` par un refus qui échoue l'essai. Les cinq modules du clone n'importent que la bibliothèque standard (`re`, `json`, `os`, `hashlib`, `datetime`, `math`, `unicodedata`, `itertools`), aucune connexion, aucune variable d'environnement (relu : `caviardage.py:8`, `fiches_v53.py:12-16`, `juges_croises_v53.py:26-30`, `outils.py:6-12`).
- Dossiers temporaires du système (`tempfile.mkdtemp`, l. 52), plus de `tmp-essais/` à côté du code (C2).

Rejeu sur copie (`copie-G2/`), Python 3.13.18 : **89 passed in 7.39s** (`sortie-essais-v2-rejoues-v1.txt`).

## 3. Mes corrections

| point | où en v2 | constat |
|---|---|---|
| T1 | rapport § 3 ; docstring `cartes_du_fichier` (diff l. 164-173) ; essai `test_forme_reelle_du_fichier_des_cartes_admise_avec_repli` (94 cartes `f` + 12 hexadécimaux, `meta` aux deux niveaux, sept noms trouvés par égalité exacte) | porté |
| T2 | docstring de `construire_service_reel` et en-tête | porté ; M6 le confirme en exercice |
| C1 | code l. 632-634, texte d'erreur proche du mien | porté ; essai sain et artefact (l. 1112-1123) |
| C2 | essais l. 52 | porté |
| T3 | sans objet (numérotation) | — |

## 4. Rien d'autre ne change que le déclaré

Différentiels refaits par moi (`diff -u` des deux couples de fichiers de G et de G2, `diff-programme-refait-v1.diff`, `diff-essais-refait-v1.diff`) : **corps identiques** à ceux du développeur, hors les deux lignes d'en-tête (518 et 409 lignes ; `comparer_differentiels_v1.py`, sortie `sortie-comparaison-differentiels-v1.json`). Lu en entier, le différentiel du programme ne contient que les treize rubriques du rapport § 2 ; aucune ligne de la garde de recouvrement (comparaison des bardeaux, rapport, repli, rejeux, refus au sixième) n'est modifiée, sauf : le rapport de repli garde `nombre_de_rejeux` (diff l. 364-370) ; `lieu_de` lit la trace sans le source et rend `NOM_DU_PROGRAMME` ; le journal et le manifeste ne sont plus des arguments. Le différentiel des essais ne retire d'assertion que celles de ce qui change de forme (journal par `LieuDuJournal`, pièce du (4) à verdict, `FileExistsError` de l'ancienne recréation remplacée par `ManifesteJournalExisteDeja`).

Ordre dans la garde (programme l. 1290, 1291, 1293, 1334) : manifeste de création, journal, pièce du (4) à verdict, puis seule ouverture. Les trois refus ont lieu avant toute ouverture.

## 5. Les points demandés

- **Verdict exigé dans la pièce du (4)** (`exiger_controle_conforme`, l. 1192 ; `LIGNE_CONFORME` l. 167) : ligne « Conforme » seule (formes `Conforme`, `**Conforme.**`, `Verdict : Conforme`, `**Verdict : Conforme**`), aucune ligne commençant par « Non conforme », empreinte complète du programme dans le texte. Le contrôle v1 « non conforme » ne passerait pas. Remarque R1.
- **`meta` à toute profondeur** (`sans_meta` l. 980, crochet `object_hook` ; garde dure ensuite) : sur la forme réelle, retire `meta` des cartes et du niveau du fichier ; aucune clé `meta` ne peut être légitime ailleurs (`fiches_v53.py:33-35`). Essai dédié.
- **Ligne de commande sous `try`** (l. 1805-1823, `_sortie_de_secours` l. 1790) : arguments lus, empreinte du programme, sortie standard, tout est sous `try` ; la sortie de secours n'écrit que classe et lieu par `os.write`, sans rien recalculer ; essais : message secret dans l'exception, empreinte illisible, sortie standard en panne, `stderr` vide. Les gestes `composer`, `auditer`, `creer-journal-rejeux` gardent leur `try` à `Refus` : une erreur système (par exemple journal déjà posé sans manifeste : `FileExistsError`) sort avec une trace sur la sortie d'erreur, sans rapport avec une carte (R3).
- **M5** : `verifier_contenus_distincts` (l. 823) appelée avant le partage ; refus `ContenusIdentiques` nommant les deux identifiants ; `fragments_communs` (l. 833) au journal de construction et au manifeste ; sur la banque factice maximum 4 sur 5 (mes mesures v1 : 29 paires à quatre), toutes les paires comptées (19 900). Conforme à la décision.
- **M1** : champs du journal hors liste fermée déclarés au rapport § 7 ; à écrire à l'additif de code. Conforme.
- **M6** : `construire_service_reel()` charge le code d'appel v4 par empreinte (cinq modules vérifiés avant tout import) et exerce 800 appels de service sur la banque factice (juge parfait 0 ; trois juges de surface dans la bande ; audit entier « banque passée » avec `nature == "reel"`), socket bloqué et mandataire coupé. Je n'ai relevé aucune écriture dans le clone (compilation depuis les octets, pas de fichier compilé). Conforme.
- **Retrait des deux formes de cartes non réelles en v3 (liste ; `{"fiches": […]}`)** : j'approuve la recommandation. L'empreinte est vérifiée avant l'analyse (l. 1334-1337) : seul le fichier d'empreinte `ba65c411…`, dont la forme est établie, peut passer ; deux branches mortes ne protègent rien et alourdissent la relecture. Coût : `cartes_du_fichier`, l'essai des formes et la fixture `cartes_factices` (liste avec clé `id`) à passer à la forme réelle (l'aide `_forme_reelle` existe). Version neuve (règle R12) ; **non bloquant : v2 peut partir telle quelle.** Une v3 devra garder les constantes du journal inchangées (R2).
- **Emplacement des constantes du journal** : `DEPOT/runs/ligne-3-etage-2-garde-de-recouvrement-v1/` (l. 161-163). Hors de l'archive, hors du dossier du code, hors de la racine interdite `runs/20261119-094145-course-auto-conception-v9` (la garde des chemins ne le refuse pas ; essai l. 637-644). Le répertoire `runs/` existe. L'emplacement convient à la lettre (« journal à ajout seul, créé vide avant le premier passage ») ; deux conséquences pour la mère, R2.

## 6. Remarques non bloquantes

- **R1 — pièce du (4).** Toute ligne commençant par « Non conforme » (insensible à la casse) fait refuser la pièce, même dans un historique ; « Conforme avec réserves » n'est pas accepté ; l'empreinte complète du programme (64 caractères) doit y figurer. À dire au contrôleur avant qu'il écrive (le mandat du contrôleur v1 dit seulement « Conforme » ou « Non conforme »).
- **R2 — durée de vie du journal (pour la mère).** Le compte ne repart pas de zéro tant que journal et manifeste de création existent. Ils vivent dans l'arbre de travail : si la machine est remplacée et le dépôt recloné sans eux, la création est de nouveau permise et le compte repart de zéro, sans signal. Recommandation : verser (commit, push) le manifeste dès sa création et le journal après chaque passage de la garde (la passation le fait déjà pour `runs/`), le dire à l'additif de code, et ne jamais changer ces constantes dans une version suivante. Le code ne détecte pas non plus une troncature ou une édition du journal (aucune chaîne d'empreintes) : hors lettre, même nature que la suppression à la main déjà déclarée.
- **R3 — `creer-journal-rejeux`** quand le journal existe sans manifeste : `FileExistsError` non rattrapée, trace sur la sortie d'erreur. Sans lien avec une carte ; à rattraper à la prochaine version si on la fait.
- **R4 — numérotation et règle R12.** Les noms de sortie de la composition restent « v1 » (banque, journal de construction) et le dossier du journal « …-v1 » : cohérent avec « première banque », à écrire à l'additif.

## 7. Écarts de cette vérification

1. Un `ls` du dossier du générateur v2 (le coordinateur le désigne) et un `ls -ld` sur `/home/user/controle-ia-travail/runs` (existence seulement, sans lister le contenu), ce dernier hors de la permission du mandat.
2. Deux `diff -u` de fichiers du dépôt, redirigés vers mon dossier ; un `grep -n "^-"` sur un différentiel du dépôt (lecture).
3. Copie de G2 dans `copie-G2/` ; les essais ont écrit sous le dossier temporaire du système, comme leur v2 le prévoit.

## 8. Pièces de ce dossier

`verification-generateur-etage-2-v2-v1.md` ; `sortie-essais-v2-rejoues-v1.txt` ; `diff-programme-refait-v1.diff`, `diff-essais-refait-v1.diff` ; `comparer_differentiels_v1.py`, `sortie-comparaison-differentiels-v1.json` ; `copie-G2/` (travail). Chaque pièce a son compagnon `.sha256` ; `table-empreintes-verification-v2-v1.txt` en donne la liste.

Contre-lecteur, modèle S.
