# Mandat du développeur — sept corrections du code du banc A de la ligne 1 (classe B) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 15:58Z, sur le mot de Lazar « go reprise, go recos » et le mot de la mère (sept corrections appliquées par un développeur Opus, puis vérification par un contre-lecteur d'un autre modèle).

## Ce que tu fais

1. Applique les **sept corrections** de `contre-lecture-code-banc-a-ligne-1-v1-v1.md` (même dossier, `c0bca7dd…`), une par une, chacune avec son essai.
2. Reprends les **quatre réserves** de `contre-lecture-banc-a-ligne1-v1.md` (même dossier) dans la commande de lancement : journal du lanceur ouvert en ajout ; avant toute reprise, vérifier que les processus listés dans les fichiers `pid-*.txt` ne vivent plus ; recoupement de M1-nul des courses 0, 300 et 599 depuis les décisions du journal ; gardes A7 et A11 qui passent par la ligne 0 de la table (à dire, sans changer le code si le préenregistrement ne le demande pas).
3. Recommandation (a) de la contre-lecture retenue : ajoute au rejeu du journal le recoupement du `m` de la décision de promotion et de la sortie brute avec les promotions du journal. La recommandation (b), sur le lieu de dépôt de l'étalonnage, revient à la mère : ne la tranche pas.
4. **Noms neufs (R12)** : les fichiers v1 restent intacts. Les fichiers changés prennent le suffixe `_v2`, avec leurs compagnons `.sha256`. Les fichiers non changés sont repris par référence, sans copie. La configuration v2 porte les empreintes des fichiers v2.
5. **Essai 11 avec le vrai fichier de mémoire** : `memoire_v53.py` n'est pas dans ce conteneur, mais il existe dans l'historique du dépôt (`git log --all --oneline -- '*memoire_v53.py'`). Extrais-le par `git show COMMIT:CHEMIN` dans ton bloc-notes, compare son empreinte à celle qu'attend la configuration, et rejoue l'essai 11 seulement si elles sont égales ; sinon, dis-le.
6. Rejoue les 42 essais et les nouveaux, sur un cas sain et sur un artefact pour chaque garde nouvelle (R5). Graines par `numpy.random.SeedSequence` (R9).
7. Ne change aucun choix qui touche ce qui est jugé ou lu (rapport du développeur v1, § 4.1 à 4.5) : ces cinq choix vont dans l'addendum, écrit par un autre rédacteur.

## Où tu écris

Dans ton bloc-notes seulement. La session verse. Dossier de sortie proposé dans le dépôt : `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/code-v2/` pour le rapport et les sorties d'essais, et `…/ligne-1-effort-recherche/code/` pour les fichiers `_v2`.

## Interdits

Ne lance jamais l'étalonnage ni la course décisive, jamais `--reel`. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée. Jamais de heredoc. Aucune valeur de clé. Rien sous `archives-reponses-modeles/`, ni « consigne-privee », ni « conception-ii-b », ni `/root/.claude/`. **N'écris jamais le nom d'une commande d'arrêt par motif dans une commande, même pour la chercher** : la garde du dépôt la refuse. Lis le code au lieu de le chercher par motif. Aucun identifiant de modèle dans tes pièces ; signe « développeur, modèle L′ ». Au premier refus d'un outil : arrête-toi et dis-le.

## Ce que tu rends

`rapport-developpeur-corrections-banc-a-v2.md` : chaque correction, avec son fichier, sa fonction, son essai et l'empreinte du fichier ; les quatre réserves ; l'essai 11 ; les décomptes d'essais ; ce que tu n'as pas pu faire.
