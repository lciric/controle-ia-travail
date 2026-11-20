VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION DE PROCESSUS. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. TOUTE REDIRECTION VERS UN CHEMIN COMPLET DE TON DOSSIER.

# Mandat du rédacteur — préenregistrement du palier 0b, brouillon v18 (compléments de la pièce de contrôle, R-4337 et R-4338) — BROUILLON, EN ATTENTE DU MOT DE LAZAR — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20. Elle part de la mère, à 22:23Z : « Inscrit en R-4338 ; une correction de plus entre dans la v18. Lance la v18 puis son contrôle. » **La v13 scellée (`d9591d5b…`) reste le texte en vigueur. La v17 n'est pas touchée. Rien n'est scellé avant le mot de Lazar.**

## Qui

Le rédacteur des v15 à v17 (modèle F). Tu signes « rédacteur des v15 à v18, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier P = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.
- **Source** : la v17, `P/brouillon-v17/preenregistrement-heritage-palier-0b-etage-processeur-v17.md` (`3ac2bc59dd421375db9ce8ea492998e285f118adacbcfb03109cc14d5339ab4d`).
- **Le contrôle de la v17** : `P/brouillon-v17/controle-v1/controle-palier-0b-v17-v1.md` (`7f42dd73…`) et son jeu de 8 corrections (X1 à X8), `P/brouillon-v17/controle-v1/corrections-palier-0b-v17-v1.json` (`23e4d150…`).
- **Le registre sur `origin/main`** : R-4337 et **R-4338**. Fais `git fetch origin main`, puis `git show origin/main:registres/decisions.md` redirigé vers `lecture-registre-origin-main.md` dans ton dossier ; cette copie est exclue du versement. Cite R-4338 à la lettre.

## Décisions de la mère (22:23Z)

1. La pièce elle-même garde le commit et les trois empreintes des programmes ; les compléments les répètent. C'est une contrainte du code, déjà dite par X1.
2. Complément 3 : « les gelés reçus du lancement précédent » sont les mêmes fichiers venus de 3–6, c'est-à-dire les fréquences et les réglages. X1 le dit ; tu vérifies que c'est sans ambiguïté.
3. **Constat de fin du programme 8–9 (complément 4), R-4338** :
   - manifeste de l'étape 8 présent et vérifié par `verifier_manifeste` ;
   - manifeste de l'étape 9 présent s'il y a des cases à confirmer ;
   - lignes « étape 8 : » et « étape 9 : » à la sortie ;
   - code de sortie nul.

   X1 dit aujourd'hui que ce constat n'est pas fixé ; ce lieu est à corriger.

## Ce que la v18 porte, et rien d'autre

Nom neuf : `preenregistrement-heritage-palier-0b-etage-processeur-v18.md`. Les remplacements passent par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, `391db990…`), en passes nommées, chaque ancre comptée par `grep -c -F -e` avant l'appel (y compris les huit du jeu du contrôleur).

- **Passe 1 — le jeu du contrôleur tel quel** (`23e4d150…`) sur la v17. La sortie doit être égale à son essai (`4dafc835…`) ; sinon, arrêt, et tu le dis.
- **Passe 2 — R-4338**, citée à la lettre :
  - le constat de fin de 8–9 au complément 4, sous la forme ci-dessus ;
  - la phrase qui le disait non fixé, corrigée ;
  - le point 2 ci-dessus, s'il reste une ambiguïté.
- **Passe 3 — tenue** : titre ; statut « BROUILLON, non scellé, en attente du mot de Lazar » ; date par `date -u` ; ligne de version ; section « Contre-lecture » ; alinéa « Version 18 » de l'annexe H.

Rends ensuite :
- le différentiel `diff -u` de v17 à v18 ;
- les comptes : une seule ligne « - Commit du code d'analyse : », `COMMIT_V6` en blanc, table de 64 lignes en premier bloc ;
- les lieux des trois empreintes entières ;
- le compte des noms `…-v1-complement-1` à `-4` et le lieu de chacun ;
- un rapport court, `rapport-redacteur-palier-0b-v18-v1.md`.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v18/`. Chaque fichier a son compagnon.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement d'un programme ni du code, aucun essai, aucun tirage, aucune pièce d'autorisation ni de contrôle. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus, même sans motif. Aucun appel à un fournisseur de modèles, aucune dépense, aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
