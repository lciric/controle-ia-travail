# Brief de lancement — session qui succède au compte organisme — 2026-11-20 — v1

Pour une session neuve, sur un autre compte. Elle est autonome avec ce texte et le dépôt.

## Toi

Tu reprends le « compte organisme » du programme de Lazar (organisme d'idéation, épreuves de la course v9) dans `lciric/controle-ia-travail`. Langue : français, tutoiement avec Lazar, presque aucun acronyme. Lazar est le directeur ; la **session mère** (`session_01XJ6Mgr8BN6UanALsQatc5E`) scelle sur `main`, inscrit les GO dans `registres/go.md` et les décisions dans `registres/decisions.md`. Tu lui écris par `send_message` (outils `claude-code-remote`).

## Lis d'abord, dans cet ordre

1. `CLAUDE.md` (racine) et la routine de reprise qu'il décrit (empreintes, `verifier-arbre`, état, tests).
2. La passation `registres/passations/2026-11-20-0831-compte-organisme.md` (sur la branche `lot/compte-organisme-v1`) : fait, reste, agents en vol et leurs mandats.
3. Sur `main` : `registres/go.md` (GO-2026-11-20-10, -11, -20 à -30), `registres/decisions.md` (R-4067, R-4083, R-4117, R-4123, R-4128 à R-4165), `registres/scellements-v1.md`.

## Branche et dépôt

- Travaille et pousse **seulement** sur `lot/compte-organisme-v1` (et des branches neuves `prep/…`). **Jamais** sur `main`, `lciric/controle-ia` ni `lciric/ideation-organism`. Jamais la branche `lot/compte-4-v1`.
- Versement : `cp --update=none` du bloc-notes vers le dépôt, `sha256sum -c`, garde des secrets à 0 sur le différentiel indexé (`sk-ant|api[_-]?key *[:=]|hcloud_token *=|ghp_|BEGIN (RSA|OPENSSH) PRIVATE`), commit, puis `git fetch origin lot/compte-organisme-v1`, `git merge --no-edit FETCH_HEAD`, `git push origin lot/compte-organisme-v1`.
- Sceller : `PYTHONPATH=src python3 -m controle_ia.scellement sceller FICHIER`. Règle R12 : une version neuve a un nom neuf, on n'écrase jamais.

## Cloisonnement (règles propres à ce compte, en plus de CLAUDE.md)

- **Aucune commande** (même une empreinte, une liste ou une taille) sur un chemin sous `archives-reponses-modeles/`, sauf les seuls gestes qu'un GO permet, faits par un agent neuf (GO-23, GO-24, GO-28 : le seul `fiches.json` de la course v9, `test -f` et les programmes contre-lus).
- Rien sous `/root/.claude/`. Aucun fichier « consigne-privee » ni « conception-ii-b », rien sous `brouillons/ii-b-saboteur-budget-v1/`, jamais la ligne R-2059.
- Jamais de heredoc ni de code en ligne passé à un interpréteur ; jamais le nom d'une commande d'arrêt ou de recherche de processus par motif (une tâche de fond s'arrête par l'outil de tâches).
- Aucune valeur de clé ; vérification de présence par le nom seulement. Aucun identifiant de modèle dans les pièces versées. « Aucune recette » dans les sorties de la course « nouvelles attaques ».
- **Qui fait quoi** : rédaction et conception par Fable (« non je veux fable » : aucune recopie d'une pièce de conception par un autre modèle) ; contre-lecture par Opus (ou un autre modèle que l'auteur) ; code par Opus, contre-lu par Sonnet.
- **Au premier refus** de permission, de classifieur ou de garde : arrête-toi et dis-le (R-4067 : le rejet d'une entrée fautive par notre propre outil est un essai raté, à corriger et déclarer).
- Chaque mandat d'agent porte l'en-tête : version de Python sans `-c` ; aucune commande de liste ; une commande simple par appel ; `git show` redirigé par `>`.
- **Aucune dépense** sans une ligne de GO et le mot de Lazar.

## Accords en cours

- GO-2026-11-20-24 (masque et lecteur par programme sur `fiches.json`), -28 (noms de clés, fait), -25 (palier 0b, seuil et calibrage), -26 (ligne 3 : portée à 200, puis étage 2 ≤ 88,36 USD, échéance 2026-11-30 ; aucune dépense avant le verdict scellé de la portée à 200), -30 (alarme : règle de mot sur graines neuves, sans dépense).

## En attente

- Contre-lecture : additif 3 (ligne 3, portée à 200) ; préenregistrement v9 du palier 0b ; puis additif 4 (alarme) et configuration A v2 quand ils rendent.
- Scellement par la mère : additif 3, v9 du palier 0b, additif 4, configuration A v2 — chacun après sa contre-lecture conforme.
- Décisions de Lazar à poser par la mère : remarque 1 de la v9 (borne basse du seuil), quatre points de l'additif 3, éventuel nœud de la configuration A v2, réflexion sur P3, proposition « tentative refusée » avec le devis du palier 1.

## Prochaine action exacte

1. Fais la routine de reprise. 2. Pour chacun des cinq travaux de la table « Agents encore en cours » de la passation : si la sortie n'est pas versée sur la branche, relance un agent neuf du modèle indiqué sur le mandat scellé (vérifie son empreinte d'abord), verse sa sortie, envoie-la à la mère. 3. Suis l'ordre « Reste » de la passation.
