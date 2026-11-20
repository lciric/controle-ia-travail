VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contrôleur — différentiel v9 → v10 du préenregistrement du palier 0b — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, règle R2. Le contrôleur de la v9 (modèle O) n'est plus joignable : tu fais à sa place la vérification de ses corrections et des choix de la mère. Dossier P = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.

## Qui

Un contrôleur neuf, modèle O, qui n'a écrit aucune version du préenregistrement, ni le code, ni la vérification du code, ni le contrôle de la v9. Tu signes « contrôleur neuf, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

- `P/mandat-redacteur-palier-0b-v10-v1.md` (`194f44b3…`) : ce qui était demandé.
- `P/preenregistrement-heritage-palier-0b-etage-processeur-v9.md` (`0aacc4ea…`) et `P/preenregistrement-heritage-palier-0b-etage-processeur-v10.md` (`ac2deb4daf4fb0b3088400ba742a6583844b0e5720774fd8b9055d0a72250f6b`) ; `P/remplacements-preenregistrement-palier-0b-v9-v10.json`, son journal, `P/differentiel-preenregistrement-palier-0b-v9-v10.diff`, `P/rapport-redacteur-palier-0b-v10-v1.md` (`ddea2701…`).
- Le contrôle de la v9 : `P/contre-lecture-v9/controle-differentiel-palier-0b-v8-v9-v1.md`, en entier.
- Le code v4 : `P/code-v4/` (rapport du développeur ; `audit.py`, `tirages.py`, lus aux lieux utiles) pour juger les points du verrou et de la garde 27.
- L'outil `/home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py` (`391db990…`).
- Sur main (`git -C /home/user/controle-ia-travail fetch origin main`, puis `git … show FETCH_HEAD:registres/decisions.md > FICHIER_DANS_TON_DOSSIER`) : R-4123, R-4135, R-4182 (la décision de la mère sur les remarques 2 à 4 et N1 à N4, inscrite après l'écriture de la v10) ; `registres/go.md`, GO-2026-11-20-11 et -25.

## Ce que tu fais

1. **Rejeu** de l'outil sur la v9 avec le JSON ; `cmp` avec la v10 ; différentiel refait.
2. **À la lettre du contrôle** : corrections 1 et 2, texte R2-T et ses reports, N1 à N4, chaque texte neuf mot pour mot.
3. **Les 24 remplacements du rédacteur** (remarques 3 et 4, liste du code v5, remarque 1, tenue) : chacun juste, nécessaire, dans la lettre de R-4182 et du contrôle ; aucun critère, valeur gelée, prédiction ou issue ne change hors de ce que la mère a tranché.
4. **La mention « décision de la mère du 2026-11-20 vers 10:09Z, à inscrire »** (six lieux) : donne, pour chacun, le texte exact qui la remplace par l'identifiant R-4182, à porter dans la version qui portera le mot de Lazar sur la remarque 1.
5. **Les huit remarques du rapport** (§ 6) et ses écarts : pour chacune, à corriger, à la mère, à Lazar, ou sans suite, avec ta recommandation.
6. **Verdict** : « Conforme, à sceller après le mot de Lazar sur la remarque 1 et le report de R-4182 » ou « À corriger », avec pour chaque correction l'« Ancien » et le « Neuf » exacts (ancre unique comptée par `grep -c -F -e`).

Écris `controle-differentiel-palier-0b-v9-v10-v1.md` dans ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/controle-palier-0b-v10/`, avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. Aucun lancement du code du palier, aucun tirage. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
