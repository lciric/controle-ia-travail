# Mandat du développeur neuf de la seconde passe — code de la lecture des directions des sondes par nos lentilles — v1

Rédigé par la session des lentilles (session_01Qi7Gr3vedYVukbyqBbHd7z) le 2026-11-21, sur les mots de Lazar « on passe au turbo max
pour boucler les billets au plus vite » et « go tu as mon mot pour tout » (GO-2026-11-21-63, tapés dans la session mère, relayés ;
note `docs/notes/neuron-lens-v1/mot-lazar-turbo-seconde-passe-2026-11-21-v1.md`, 591168a5…). Pièce de travail (classe C). Le code
produit est une pièce de **classe B** (instrument) : contre-lecture par un agent neuf d'un autre modèle, puis vérification des
corrections par le même contre-lecteur.

## Ce que ce mandat est
Il reprend **l'étape 2** du mandat du développeur des deux passes
(`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-deux-passes-lentilles-v1.md`,
`0a9517ea4e1d7460b411a0914996503eb3c6a9a680b4d3c88ae9d4f1f67bbdfc`), à partir de la passation de ce développeur
(`docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/passation-developpeur-deux-passes-2026-11-20-etape-1-close-v1.md`,
`708203b1…`). **Toutes les règles de ce mandat-là valent pour toi** (qui tu es, ce que tu lis, ce que tu ne lis jamais, comment tu
travailles, aucune règle nouvelle, refus jamais rejoués, rien ne se lance ni ne se dépense), sauf là où le présent mandat les complète.
**L'étape 1 est close** (code de la première passe fixé, lanceur v7, commit cc7f4576) : tu n'y touches pas. Lis ces deux pièces en entier
d'abord, et vérifie leurs empreintes.

## Mémoire de travail — à dire au départ
Le texte v2 pèse environ 405 Ko ; ton prédécesseur s'est arrêté faute de mémoire avant de le lire. **Dis dans ta première note**
(`developpement/notes-developpement-seconde-passe-v1.md`, scellée) si tu peux tenir le travail ; découpe-le en sous-étapes ; après
chacune, commit, poussée, et une **passation courte** scellée dans `developpement/` (fait, reste, prochaine sous-étape, empreintes).
Si ta mémoire baisse, arrête-toi proprement sur une passation : un remplaçant neuf reprendra. Ne perds rien : brouillons dans le dossier.

## Ordre de lecture
1. `CLAUDE.md` (R1 à R14, interdits).
2. Le mandat 0a9517ea… et la passation 708203b1… ; puis `developpement/notes-developpement-v2.md`,
   `developpement/conformite-code-a-l-addendum-concentration-scelle-v2.md`, et la contre-lecture
   `contre-lectures/contre-lecture-code-premiere-passe-addendum-v1.md` (7954d0fc…).
3. **En entier, sans sa liste « Jamais ouverts »**, le texte de lecture v2 scellé `prereg/lecture-sondes-bbis-par-lentilles-v2.md`
   (`a2bbed7ac34180b69864f143d1a910c8c29687dc73cca359c85256b6d9b78d15`). Il n'est pas sur ta branche : `git fetch origin main`, puis
   `git show origin/main:prereg/lecture-sondes-bbis-par-lentilles-v2.md > prereg/lecture-sondes-bbis-par-lentilles-v2.md` et de même
   son compagnon `.sha256` ; vérifie l'empreinte avant toute lecture ; verse ces deux fichiers tels quels. Sa section « Code neuf » est ta
   liste de travail. Les mots de Lazar qui fixent sa lecture : `docs/notes/neuron-lens-v1/mot-lazar-noeuds-n12-n17-et-brouillon6-2026-11-20-v1.md`,
   `mot-lazar-regle-departage-seconde-passe-2026-11-19-v1.md`, `mot-lazar-declaration-verdict-seconde-passe-2026-11-20-v1.md`,
   `mot-lazar-phase-exploratoire-et-option-c-2026-11-20-v1.md`.
4. Le lanceur de la première passe tel qu'il est fixé, et ce qui l'a façonné après l'addendum : `lanceur_v5` à `lanceur_v7`, les notes
   `developpement/notes-lanceur-v5-v1.md`, `notes-lanceur-v6-v1.md`, `notes-lanceur-v7-v1.md`, et les contre-lectures de ces versions
   sous `contre-lectures/`.
5. Le registre propre `registres/lecture-sondes-bbis-par-lentilles-v1.md` (sur main, `git show origin/main:…`), en entier : permis.

## Ce qui est tranché depuis le mandat 0a9517ea… (à suivre, sans le rouvrir)
- **Canal des messages d'arrêt** (nœud 1 de la contre-lecture, laissé à Lazar) : tranché par GO-2026-11-20-56 (messages d'arrêt
  cloisonnés) et GO-2026-11-21-06 (mots fixes gardés, garde du fichier d'arrêt déjà présent). Le lanceur de la seconde passe suit le même
  schéma que `lanceur_v7` : une seule fonction décide ce qui va à la sortie d'erreur (mots fixes) et ce qui va dans `arret.json`
  (message entier) ; garde du fichier d'arrêt déjà présent ; fenêtres d'interruption fermées comme en v6. Réemploie ces fonctions si
  leur interface convient ; sinon version neuve déclarée.
- **Égalité de la relecture de contrôle de l'audit** (nœud 2) : gardée « écrite, sans arrêt » (défaut retenu, relais de la mère du
  2026-11-21 16:00Z).
- **Règle de départage** : identifiant de jeton croissant (GO-2026-11-19-92). **Nœuds N12 et N17** : GO-2026-11-20-18, tels que le
  texte v2 scellé les porte.
- Noms libres : `montage_v2`, `audits_v2`, `phrases_v2`, `nos_lentilles_v1`, `lecture_entree_v1`, `comparaisons_lentilles_v1`,
  `reproduction_v1`, `statistiques_v4`, et le lanceur de la seconde passe sous un nom neuf (par exemple `lanceur_seconde_passe_v1`),
  horloge de 10 heures. Aucun module existant n'est réécrit (R12).

## Le travail
Exactement la section « Code neuf » du texte v2 scellé, entière, avec **tous** ses essais (brouillons 4, 5 et 6 compris), R5 pour chaque
garde (cas sain et artefact), graines par `numpy.random.SeedSequence`. Tout sur jouets : aucun téléchargement de Llama, de la lentille
publique, de nos fichiers d'ajustement ni du corpus ; la clé de la plateforme de modèles n'est ni lue ni testée. Toute ambiguïté qui
oblige à choisir : nœud écrit, daté, et tu continues le reste. Essais : le paquet (`PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m pytest -q tests/test_lentilles_sondes_bbis_*.py`)
et les fichiers voisins touchés ; la suite complète du dépôt n'est pas lancée (plus de deux heures) : dis-le.

## Commits
Branche `claude/brave-galileo-jhp684` seulement ; poussée `git push -u origin claude/brave-galileo-jhp684` (quatre essais au plus sur
erreur réseau ; branche distante avancée : `git fetch origin claude/brave-galileo-jhp684 && git merge --no-edit FETCH_HEAD`, jamais de
poussée forcée). **Aucun identifiant ni nom de modèle dans les messages de commit.** Chaque message finit par les deux lignes
`Co-Authored-By: Claude <noreply@anthropic.com>` et `Claude-Session: https://claude.ai/code/session_01Qi7Gr3vedYVukbyqBbHd7z`.

## Rendu (fin de l'étape 2, ou arrêt propre)
Le rendu de l'étape 1 du mandat 0a9517ea… : verdict en une à trois lignes ; commit ; fichiers neufs et changés avec empreintes ; table
« garde → essai sain → essai artefact » versionnée et scellée ; sortie des essais du paquet ; note de conformité au texte v2 scellé,
point par point, scellée ; nœuds ouverts ; expositions (tout intitulé interdit vu) ; liste des fichiers à donner au contre-lecteur. Puis
tu t'arrêtes : la session des lentilles lance le contre-lecteur neuf. Tu n'inscris aucune ligne de registre.
