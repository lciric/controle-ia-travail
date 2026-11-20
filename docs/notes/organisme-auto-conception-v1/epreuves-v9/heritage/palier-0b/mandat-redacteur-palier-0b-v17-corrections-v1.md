VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION DE PROCESSUS. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. TOUTE REDIRECTION VERS UN CHEMIN COMPLET DE TON DOSSIER.

# Mandat du rédacteur — préenregistrement du palier 0b, brouillon v17 (corrections du contrôle de la v16 et choix de la mère) — BROUILLON, EN ATTENTE DU MOT DE LAZAR — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20. Sa source est la mère, à 22:12Z : « Les trois choix sont faits et inscrits (R-4336) […]. Lance la v17 avec le jeu ajusté, puis son contrôle. » **La v13 scellée (`d9591d5b…`) reste le texte en vigueur. La v16 n'est pas touchée. Rien n'est scellé avant le mot de Lazar.**

## Qui

Tu es le rédacteur de la v15 et de la v16 (modèle F). Tu signes « rédacteur des v15 à v17, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier P = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.
- **Source** : la v16, `P/brouillon-v16/preenregistrement-heritage-palier-0b-etage-processeur-v16.md` (`c37bdb2f301f3bd9efa8767f36158006e7b1f58c4b2ab628d96cfa1eaa3bfa0d`).
- **Le contrôle de la v16** : `P/brouillon-v16/controle-v1/controle-palier-0b-v16-v1.md` (`6e772a5d…`) et son jeu de 11 corrections `P/brouillon-v16/controle-v1/corrections-palier-0b-v16-v1.json` (`7f98449b…`).
- **Le registre sur `origin/main`** (après `git fetch origin main`, puis `git show origin/main:registres/decisions.md` redirigé vers ton dossier) : R-4335 et **R-4336**. Cite R-4336 à la lettre.

## Choix de la mère (R-4336, 22:12Z)

1. **Constat de fin sans arrêt** : la forme du contrôleur, c'est-à-dire les manifestes d'issue « tenue », l'absence des fichiers d'arrêt réels (`arret.txt` pour le programme 3–6, `arret-garde-equivalence-s8.txt` pour le programme 6 bis–7) et les lignes de sortie.
2. **Libellés de la pièce de contrôle** : **avec le nom du programme**, sous la forme du contrôleur (« empreinte du programme lancer_etapes_3_5_6_v2.py : <empreinte> », et de même pour le commit et les deux autres programmes). La forme sans le nom n'entre pas au texte.
3. **Compléments de la pièce de contrôle** : numérotés dans l'ordre où ils s'écrivent, celui de la règle n° 8 en dernier. R-4336 corrige R-4292 sur ce point. L'alinéa « Version 13 » qui réservait `…-v1-complement-1.md` à la règle n° 8 est corrigé ; tu comptes ses lieux.

## Ce que la v17 porte, et rien d'autre

Nom neuf : `preenregistrement-heritage-palier-0b-etage-processeur-v17.md`. Les remplacements passent par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, `391db990…`), en passes nommées. Chaque ancre est comptée par `grep -c -F -e` avant l'appel.

- **Passe 1 — le jeu du contrôleur tel quel** (`7f98449b…`), appliqué à la v16. Tu vérifies que la sortie a la même empreinte que l'essai du contrôleur (`ee5ff013…`). Si l'empreinte diffère, tu t'arrêtes et tu le dis.
- **Passe 2 — l'ajustement aux choix de la mère.** Dans un JSON à toi, tu fais quatre choses :
  - tu cites R-4336 à la lettre ;
  - tu retires du texte toute mention de la forme de libellé sans le nom, et toute alternative restée ouverte aux points 1 et 2 ;
  - tu inscris la numérotation des compléments ;
  - tu corriges l'alinéa « Version 13 ».
- **Passe 3 — tenue** : titre, statut « BROUILLON, non scellé, en attente du mot de Lazar », date par `date -u`, ligne de version, section « Contre-lecture », alinéa « Version 17 » de l'annexe H.

Ensuite :
- le différentiel `diff -u` de v16 à v17 ;
- le compte des lignes qui commencent par « - Commit du code d'analyse : » (1 attendu ; `COMMIT_V6` toujours en blanc ; la table de 64 lignes toujours premier bloc) ;
- le compte des lieux de chacune des trois empreintes entières des programmes ;
- un rapport court, `rapport-redacteur-palier-0b-v17-v1.md`.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v17/`. Chaque fichier a son compagnon. Ne recopie pas le registre dans un fichier à verser : s'il te faut une copie de lecture, nomme-la `lecture-registre-origin-main.md`, elle sera exclue du versement.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement d'un programme ni du code, aucun essai, aucun tirage, aucune pièce d'autorisation ni de contrôle. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus, même sans motif. Aucun appel à un fournisseur de modèles, aucune dépense, aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
