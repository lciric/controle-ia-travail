# Mandat de l'agent d'extraction du cas X6 (juge de sélection des cartes de la course v9) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 20 novembre 2026 vers 05:45Z. Pièce de travail.

Destinataire : un agent neuf, Claude Sonnet 5.5, d'un autre modèle que la mère (Opus 5.5), qui n'a lu aucune carte de la course v9. Accord : GO-2026-11-20-15 (option (a) de R-4090).

---

Les critères scellés du juge de sélection (`prereg/organisme-auto-conception-v9/juge-selection/criteres-choix-cartes-v9-v7.md`, l. 61) excluent du choix les cartes retenues par l'aiguilleur de la course (cas X6). La mère doit en donner la liste par programme, avant toute ouverture. Le journal de l'aiguilleur a été versé dans un dossier que la mère ne peut pas ouvrir. Lazar a accordé qu'un agent neuf ouvre ce seul fichier, par le programme de la mère, et ne rende que des identifiants et des comptes.

## Pièces
- Le programme : `docs/notes/organisme-auto-conception-v9-mere/juge-selection-x6-v1/extraire_x6_journal_aiguilleur_v1.py` (`e2da19dfadc919083b8f8fe1d7a639e1674ccdf60396620bdd61af55dabacb19`).
- Ses essais : `essais_extraire_x6_v1.py`, même dossier (`39d282ee3c02d37df089efa9be4700fa9d79f74df098a0eb99c9bc1bcf11431b`).
- Le commit de versement de la course : `8029ae7f9539a950936cef5b2b669285d4efb05a`, sur la branche `lot/compte-organisme-v1` (à récupérer par `git fetch origin lot/compte-organisme-v1`).

## Ce que tu fais
1. **Contre-lecture courte du programme**, pièce d'instrument. Vérifie chaque empreinte. Lis le programme et ses essais en entier. Juge :
   - Le programme peut-il écrire autre chose que des noms de clés, des comptes, des identifiants, le chemin du seul fichier, son empreinte et sa taille ? En particulier une `categorie`, un texte ou un motif ?
   - Les gardes s'arrêtent-elles par un code non nul sur chaque artefact, sans repli silencieux ?
   - Les essais couvrent-ils un cas sain et un artefact pour chaque garde ?
   Rejoue les essais en commande simple : `.venv/bin/python -B -m pytest -q -p no:cacheprovider <chemin des essais>`.
   Verdict : « conforme » ou « à corriger ». **Si « à corriger », arrête-toi là** : rends les corrections sous forme de couples (avant, après), sans toucher au programme, et ne joue rien.
2. **Si « conforme » : un seul passage** sur le vrai commit, depuis la racine du dépôt :
   `.venv/bin/python -B docs/notes/organisme-auto-conception-v9-mere/juge-selection-x6-v1/extraire_x6_journal_aiguilleur_v1.py --depot . --commit 8029ae7f9539a950936cef5b2b669285d4efb05a --suffixe /generation-1/aiguillage/journal-aiguillage.json --sortie docs/notes/organisme-auto-conception-v9-mere/juge-selection-x6-v1/sortie-extraction-x6-v1.json`
   - Ne rejoue pas, même sur un code non nul : rends le code et la sortie telle quelle.
   - Scelle la sortie : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`.
3. **Ta contre-lecture**, scellée : `docs/notes/organisme-auto-conception-v9-mere/juge-selection-x6-v1/contre-lecture-extraction-x6-v1.md`.

## Ce que tu ne fais pas
- Tu n'ouvres rien sous `archives-reponses-modeles/` autrement que par ce programme, une fois. Aucun `git show`, `cat`, `ls`, `git ls-tree` ni aucune recherche sur ce dossier ou sur ce commit, hors du programme.
- Tu n'ouvres aucune carte, aucune autre sortie de la course, aucune transcription.
- Tu ne lis pas la sortie au-delà de ce qu'il faut pour vérifier qu'elle ne contient que des noms de clés, des comptes et des identifiants.

## Règles
- Aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ; rien sous `/root/.claude/`.
- Pas de code en ligne passé à l'interpréteur (`python -c`, `python -`).
- Aucun nom de commande d'arrêt ou de recherche de processus par motif dans une commande.
- Une commande simple à la fois. Écriture : tes deux fichiers de sortie seulement. Ni réseau hors `git fetch` de cette branche, ni dépense, ni commit.
- Au premier refus d'outil, de classifieur ou de garde, arrête-toi et dis-le, sans contournement.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. Le verdict de ta contre-lecture.
3. S'il a joué : le code de sortie, les chemins et les empreintes des deux fichiers, et les comptes par classe, tels que le programme les affiche.
4. Cinq lignes au plus sur ce qui menace la lecture.
