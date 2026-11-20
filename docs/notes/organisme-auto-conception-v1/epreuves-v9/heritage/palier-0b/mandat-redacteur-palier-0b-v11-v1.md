VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — préenregistrement du palier 0b, version 11 (remarque 1 tranchée, GO-2026-11-20-41) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20. Lazar a tranché la remarque 1 (GO-2026-11-20-41) ; le contrôle v9 → v10 a rendu « À corriger », une correction (C1, garde 25) et six renvois à R-4182 ; la mère veut NE-1 et NE-2. Ensuite : contrôle du différentiel v10 → v11 par le même contrôleur, puis code v5, sa vérification, et le scellement par la mère selon ce que le texte exige. Dossier P = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.

## Qui

Un rédacteur neuf, modèle F, qui n'a écrit aucune version du préenregistrement, ni le code, ni aucun contrôle. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

- `P/preenregistrement-heritage-palier-0b-etage-processeur-v10.md` (`ac2deb4daf4fb0b3088400ba742a6583844b0e5720774fd8b9055d0a72250f6b`) ; `P/rapport-redacteur-palier-0b-v10-v1.md`.
- `P/controle-v10/controle-differentiel-palier-0b-v9-v10-v1.md` (`98975c9ecdef3a45e4db4fddcd6c6debd63c6f641bcc2e91bcbefae771a2deb3`), en entier : C1, les six renvois à R-4182, NE-1, NE-2 ; et ses jeux essayés sur copie : `P/controle-v10/essai-remplacements-controleur-sur-v10.json` (C1 et six renvois) et `P/controle-v10/essai-non-exiges-controleur-sur-v10.json` (NE-1, NE-2).
- `P/contre-lecture-v9/controle-differentiel-palier-0b-v8-v9-v1.md`, § 5, remarque 1 : les options (i) et (ii) et la recommandation (ii).
- Sur main (`git -C /home/user/controle-ia-travail fetch origin main`, puis `git … show FETCH_HEAD:registres/go.md > FICHIER_DANS_TON_DOSSIER`) : la ligne **GO-2026-11-20-41**, citée à la lettre. Le mot de Lazar : « Recommandation du contrôleur : (ii), confiance moyenne à haute. : go ».
- L'outil `/home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py` (`391db990…`).

## Ce que tu écris

`preenregistrement-heritage-palier-0b-etage-processeur-v11.md` (nom neuf), à partir de la v10, par l'outil contre-lu, un JSON écrit avec l'outil d'écriture de fichiers (tu peux reprendre mot pour mot les textes des deux jeux du contrôleur, après les avoir comparés à sa pièce), chaque ancre comptée par `grep -c -F -e` avant l'appel (R-4067). Il porte, et rien d'autre :
1. **C1** et les **six renvois à R-4182**, mot pour mot du contrôle.
2. **NE-1 et NE-2**, mot pour mot du contrôle.
3. **La remarque 1 tranchée (GO-2026-11-20-41)** : le seuil d'arrêt de l'étape 3 des audits par dose est **le plus grand de 0,55 et de M + 2 σ₀** ; une exactitude au plus 0,55 n'arrête jamais ; dans la section « Seuil », à la garde 25 (cas sain et artefacts : écris l'artefact qui voit le défaut « arrêt sur une exactitude au plus 0,55 », s'il manque), à la remarque 1 de l'annexe H (« tranchée par Lazar, GO-2026-11-20-41 »), à la liste du code v5 (le seuil à coder), et partout où le texte dit encore la remarque 1 « posée à Lazar » ou « non tranchée ». Ne change rien d'autre : ni la règle calibrée de signalement, ni une autre valeur gelée.
4. **Tenue** : titre, ligne de version, statut, date.

Puis le différentiel `diff -u` v10 → v11 et un rapport court `rapport-redacteur-palier-0b-v11-v1.md` : remplacements, ancres comptées, chaque lieu touché pour la remarque 1 et pourquoi, tout point où la lettre ne suffit pas (en remarque, jamais tranché).

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v11/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement du code du palier, aucun tirage. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
