# Vérifications et contre-lecture de la garde de l'instance — alignement de T0.8 (Sonnet, même contre-lecteur) — v1

Quatre rapports du contre-lecteur, recopiés tels quels dans l'ordre (le développeur n'y change rien).

---

## verification-corrections-alignement-t08-v1.md

# Vérification des corrections (202f6379), même contre-lecteur

Lu : diff 04b4edfa..202f6379 (src/controle_ia/t08, tests/test_t08_*), noms des mutations A18-A24 dans mutations-alignement-t08-v2.py. Aucun écart src/tests entre 202f6379 et HEAD. Non ouvert : interdits habituels. Banc v2 : sortie non encore disponible, non vérifiée par moi.
Rejoué : alignement + tokeniseur (T08_EXIGER_TOKENISEUR=1) + mots_et_cout : 32 passés ; test_lecture_reelle_charge_la_piece : 1 passé ; passage à blanc (gardes_corrections) : 2 passés.

- CA-01 vérifié : `charger_piece` restaure `sys.modules` (ancien capturé avant le chargement) si `Piece(...)` refuse ; `test_chargement_contrat_incomplet` passe par `_exiger_arret` (contrôle `sys.modules`). Le test du jouet (`test_t08_mots_et_cout_v1`) ne contrôle toujours pas `sys.modules` : couvert par A18 seulement via le contrat incomplet, suffisant.
- CA-02 vérifié : comparaison des cinq clés inscription/marqueur ; artefact réel (pièce contrôlée sur le marqueur du brouillon 11, configuration factice) refusé.
- CA-03 vérifié : l'espion enregistre les lectures et les appels, exige l'ensemble lu inclus dans CONTRAT plus PIECE_JOUET, l'ordre exact des six appels, les actions/y/centres passés tels quels (identité d'objet). Probant. L'assertion tautologique restée dans l'ancien essai est sans effet : la retirer (remarque, facultatif).
- CA-04 vérifié : test_copie_saine ajouté à A12 (sans fixture), à confirmer dans la sortie du banc.
- CA-05 vérifié : non-Exception relevées telles quelles après restauration ; test SystemExit contrôle `sys.modules`.
- CA-06 vérifié : balayage de `string.printable` sur le tokeniseur réel, constat figé `A_CHEVAL_ASCII`, détection jamais manquée.
- CA-07 vérifié : `piece_points_joues` dans le compte rendu.

**CA-09 — remarque (rapport, à écrire)** : le balayage montre que le constat est plus large que ce que dit le rapport § 3 : 41 lettres sur 52 (par exemple `>Answer`) fusionnent aussi avec `>`, pas seulement saut de ligne et ponctuation. Le rapport final doit le dire (et que la fréquence dans les générations des juges est inconnue) ; la règle de l'état « à cheval » reste un nœud pour la mère.

Reste : sortie du banc v2 (A18-A24 tuées, A12 avec test_copie_saine) à lire dans le rapport final ; marqueurs <<…>> à remplir.

## Verdict : corrections **vérifiées**, sous réserve de la sortie du banc v2 et de CA-09 dans le rapport.

---

## contre-lecture-garde-instance-t08-v1.md

# Contre-lecture : garde de l'instance resserrée (01fe0ea5), classe B

Lu : diff 202f6379..01fe0ea5 (entrees_v1, course_v1, test_t08_entrees_rendu_v1), noms des mutations A25-A28, preuve-inchange-t08-v2.py (sortie rejouée : « tout tient », changements = seulement `_nom_interdit_instance`, `exiger_instance_sans_interdits`, `executer_course`, constante `_RUN_7B`). Rejoué : `-k amorce` 3 passés. Aucun resume.json ouvert, aucun nom listé hors dépôt d'essai. Banc v3 non rejoué.

## Points
(1) Identification « de 7b » par un dossier du chemin égal à `run_7b` : suffisante pour la lettre du texte si le résumé de 7b vit sous `diag|runs|donnees/<run>/` ; la forme `_RUN_7B` est identique à `cf._RUN` (même regex) ; un identifiant d'une autre forme arrête. Limites (remarques, non bloquantes) : une copie du résumé de 7b sous un chemin sans l'identifiant (note, autre nom de dossier) n'est pas vue — c'est inhérent à une identification par chemin, à déclarer ; la comparaison est sensible à la casse, sans importance sur les identifiants en minuscules. Les fichiers compagnons `resume.json.sha256` ne sont pas visés (empreintes seules), conforme à la lettre.
(2) `git log --all --root --no-renames -m --format= --name-only` : couvre tous les chemins de tous les commits atteignables par une référence (--all : branches, étiquettes, distantes, stash) ; `--root` fait lister l'arbre entier du commit de bord d'un clone peu profond ; `-m` couvre les fusions. Ne couvre pas les commits inatteignables (hors de la portée d'un clone, que rev-list ne voit pas non plus). **Faille trouvée : CA-10.**
(3) Essais : cas sain (clone d'une branche, profondeur 1, arbre courant avec resume.json étrangers), artefacts (resume.json de 7b en fichier, en objet à blob dédoublé, dans un clone), préfixe de l'identifiant admis, identifiants mal formés. Probants ; voir CA-10 pour le cas manquant.
(4) `course_v1.executer_course` passe `marqueurs["RUN_7B"]["run_id"]` (marqueurs déjà validés par `exiger_marqueurs`) ; seul appelant de la fonction dans src ; l'ancienne signature à un argument n'existe plus.

## Constats
**CA-10 — à corriger** — `src/controle_ia/t08/entrees_v1.py`, l. ~434-443 (appel `git log … --name-only`). `git log --name-only` entoure de guillemets et échappe en octal tout chemin contenant un caractère non ASCII (`core.quotePath`). Le chemin `"diag/<run>/\303\251/resume.json"` a alors pour dernier élément `resume.json"` et pour premier `"diag` : `_nom_interdit_instance` ne reconnaît plus ni le fichier ni le dossier de 7b. Vérifié sur un dépôt d'essai : un `resume.json` de 7b sous `diag/<run>/é/`, blob dédoublé (mêmes octets qu'un autre fichier), supprimé du disque, commit gardé : la garde rend `interdits: 0` au lieu d'arrêter (sans dédoublement, `rev-list --objects`, qui ne cite pas les chemins, l'attrape). Correction : ajouter `-z` (et lire `stdout.split("\0")`), ou au minimum `-c core.quotePath=false`, plus un refus de toute ligne qui commence par un guillemet ; ajouter un test (chemin non ASCII + blob dédoublé) et une mutation (retrait de `-z`).
**CA-11 — remarque** — même fichier : `text=True` sans `errors` : un chemin non UTF-8 dans l'objet git lève `UnicodeDecodeError` (arrêt non typé, donc sûr mais non journalisé comme `GardeArret`). Correction : `errors="surrogateescape"` ou lecture en octets avec `-z`.
**CA-12 — remarque (déclaration)** — le texte de la garde dit « de 7b » mais l'essai du cas sain ne couvre que des resume.json d'arbre aligné (aucun de 7b, par hypothèse du rapport). Le rapport doit dire que l'absence de resume.json de 7b dans l'instance réelle repose sur la branche d'entrée de la course (liste blanche), non sur cette garde seule, et que la garde ne voit pas une copie renommée.

## Verdict : **conforme après correction de CA-10** (rapide ; CA-11, CA-12 remarques). Vérification de la correction par le même contre-lecteur.

---

## verification-garde-instance-t08-v1.md

# Vérification de la garde de l'instance (360979d1)

Lu : diff 01fe0ea5..360979d1 (entrees_v1, test_t08_entrees_rendu_v1) ; aucun écart src/tests jusqu'à HEAD. Rejoué : `-k amorce` : 4 passés. Mutation A29 non rejouée. Mêmes interdits respectés.

- CA-10 vérifié : `-z` sur `git log`, `core.quotePath=false` sur `rev-list` ; le test neuf (chemin non ASCII avec espace, blob dédoublé nommé par `a/autre.json`) est probant.
- CA-11 vérifié : sorties lues en octets, décodées en `surrogateescape`, erreurs d'`stderr` en `replace`.

**CA-13 — à corriger (léger)** — `entrees_v1.py`, ligne `set(r.stdout.decode(...).replace("\n", "\0").split("\0"))`. Remplacer les sauts de ligne par NUL coupe un chemin qui contient un saut de ligne. Vérifié sur un dépôt d'essai : `diag/<run>/d\nx/resume.json` (blob dédoublé, retiré du disque) donne `interdits: 0` : la garde ne l'attrape pas. Cas tordu mais de même nature que CA-10. Correction : ne pas remplacer ; découper sur NUL seulement et retirer un éventuel saut de ligne initial de chaque entrée (séparateur de commits), `l.lstrip("\n")` ; ajouter l'essai (dossier avec saut de ligne, blob dédoublé) et une mutation.

## Verdict : CA-10 et CA-11 vérifiés ; **conforme après correction de CA-13** (petite). CA-12 reste au rapport.

---

## verification-ca13-t08-v1.md

# Vérification de CA-13 (d231cc8b)

Lu : diff 360979d1..d231cc8b (entrees_v1, test_t08_entrees_rendu_v1). Rejoué : `-k amorce` : 5 passés. Mêmes interdits.

CA-13 vérifié : découpe sur NUL seule, `lstrip("\n")` par entrée ; l'essai neuf (dossier à saut de ligne, blob dédoublé) est probant (mon cas d'essai précédent est de même forme).

Point à juger : un nom de chemin qui commence par un saut de ligne perd ce caractère. **Acceptable, et dans le sens sûr** : le retrait ne peut que rapprocher le chemin de sa forme normale. Exemple : `\n<run>/resume.json` à la racine, non reconnu tel quel, devient `<run>/resume.json` et est arrêté. Le seul effet possible est un arrêt en plus sur un chemin à la racine dont le dossier est l'identifiant de 7b, ce qui est voulu. Aucun chemin interdit ne peut échapper par ce retrait. À mentionner d'une phrase dans le rapport.

## Verdict : **vérifié** ; plus aucun constat ouvert sur la garde de l'instance (CA-12 reste à inscrire au rapport).
