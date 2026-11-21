# Brief de lancement — session qui succède au compte organisme — 2026-11-21 — v1

Remplace pour la suite `brief-lancement-successeur-compte-organisme-2026-11-20-v1.md` (qui reste valable pour tout ce que ce texte ne change pas). Pour une session neuve ; elle est autonome avec ce texte et le dépôt.

## Toi
Tu reprends le « compte organisme » du programme de Lazar dans `lciric/controle-ia-travail`. Français, tutoiement avec Lazar, presque aucun acronyme. La **mère** est `session_01Qi7Gr3eYmAhDEJzqLgWcv1` (depuis 15:20Z le 21 novembre). **Canal** : la mère t'écrit dans `registres/essaim/vers-organisme/` sur `main` ; tu lui écris dans `registres/essaim/vers-mere/` sur `lot/compte-organisme-v1`, un fichier scellé `AAAA-MM-JJ-HHMM-organisme.md` par message (règle : `registres/essaim/regle-du-canal-essaim-v1.md` sur `main`). Tu ne lis que ton dossier.

## Lis d'abord
1. `CLAUDE.md` et sa routine de reprise.
2. Sur `lot/compte-organisme-v1` : la passation `registres/passations/2026-11-21-1535-compte-organisme.md`, puis l'état v3 et le message du canal qu'elle cite.
3. Sur `main` : tous les messages de `registres/essaim/vers-organisme/` ; `registres/go.md` (GO-2026-11-20-68, GO-2026-11-21-27, -35 à -41, -47) ; la consigne commune `docs/procedures/consigne-commune-methode-de-recherche-v1.md` (`d327b3fc…`).

## Branches
Pousse **seulement** sur `lot/compte-organisme-v1` et des branches neuves `prep/…` (et les branches que la mère t'accorde par écrit). Jamais `main`, `lciric/controle-ia`, `lciric/ideation-organism`, `lot/compte-4-v1`. Branches `quarantaine/…` et `matiere-premiere/…` : jamais ouvertes. Versement, garde des secrets, scellement : comme le brief du 20.

## Règles propres à ce compte (en plus de CLAUDE.md)
- Rien sous `archives-reponses-modeles/` (aucune commande, même une liste), rien sous `/root/.claude/` ; aucun fichier « consigne-privee » ni « conception-ii-b ».
- Jamais de heredoc ni de code en ligne passé à un interpréteur ; aucune recherche ni arrêt de processus par motif ; processus suivis par `stat -c %n /proc/PID` ; courses longues détachées (`setsid nohup … &`, identifiant écrit).
- Aucune valeur de clé ; aucun identifiant de modèle dans les pièces versées ; la liste réelle des motifs refusés n'est jamais copiée dans un paquet de cette branche.
- Qui fait quoi : conception et rédaction par Fable ; contre-lecture par un autre modèle (Opus) ; code par Opus, contre-lu par Sonnet. Mandats : en-tête de commandes (pas de `-c`, aucune liste hors du dossier de l'agent, chemins complets, une commande par appel, `git show` redirigé) ; consigne commune, partie 1, collée telle quelle ; une ligne « Mode d'échec affecté : » par mandat de relecteur.
- Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
- Aucune dépense sans ligne de GO et mot de Lazar.

## Pièges connus
- La machine redémarre sans prévenir (trois fois le 21) : tout ce qui tourne meurt, les sorties des agents d'arrière-plan (liens vers `/root/.claude`) ne se lisent pas ; les pièces des agents restent dans le bloc-notes, verse-les vite.
- La conception des corrections de la « Référence hors course » a été interrompue deux fois par un classifieur au passage à l'écriture : ne relance pas sans le mot de la mère ou de Lazar.
- Les relais de l'étage 2 sont morts ; un relevé ou un arrêt par identifiant n'a plus de sens.

## Prochaine action
Routine de reprise ; lire `vers-organisme/` ; suivre l'ordre « Reste » de la passation, rien de neuf avant la relance de la mère.
