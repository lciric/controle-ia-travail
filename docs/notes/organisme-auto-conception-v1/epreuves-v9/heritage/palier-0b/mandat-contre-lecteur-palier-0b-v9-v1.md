VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contre-lecteur — préenregistrement du palier 0b, différentiel v8 → v9 — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20 (règle R2 ; GO-2026-11-20-25). Dossier P = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.

## Qui

Un contre-lecteur neuf, modèle O, qui n'a écrit aucune version du préenregistrement, ni le code, ni sa vérification. Tu signes « contre-lecteur, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- `P/mandat-redacteur-palier-0b-v9-erratum-v1.md` (`6f5e4603…`) : ce que la v9 devait porter, et rien d'autre.
- `P/preenregistrement-heritage-palier-0b-etage-processeur-v8.md` (`fd275af8…`), son contrôle `P/controle-differentiel-palier-0b-v8-v1.md` (T1 à T9).
- `P/preenregistrement-heritage-palier-0b-etage-processeur-v9.md` (`0aacc4ea275e97812647ce0ce4723c9bd01d76f32a8f0c42462d00be2fe7bc2e`), `P/remplacements-preenregistrement-palier-0b-v8-v9.json` (`9351af5e…`), son journal, `P/differentiel-preenregistrement-palier-0b-v8-v9.diff` (`74a81fab…`), `P/rapport-redacteur-palier-0b-v9-v1.md` (`4ddfb220…`).
- `P/code-v4/rapport-developpeur-code-palier-0b-v4.md` (`2947c4f1…`) et `P/verification-code-palier-0b-v4-v1.md` (`183b17d2…`).
- Sur main (`fetch`, puis `git show` redirigé) : `registres/go.md` (GO-2026-11-20-25) et `registres/decisions.md` (R-4123, R-4135, R-4150).

## Ce que tu vérifies

1. **Rejeu de l'outil** (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, `391db990…`) sur la v8 avec le JSON, sortie dans ton dossier : égale à la v9 à l'octet ?
2. **Fidélité** : chacun des sept points du mandat est porté, T1 à T9 à la lettre, et rien d'autre ne change (critères, valeurs gelées, prédictions, issues, audits de lois).
3. **GO-25 point (1)** : le seuil d'arrêt des audits par dose est bien « moyenne permutée + 2σ₀ », M bien défini. **Point (2)** : signalement seulement, jamais un arrêt, pour le contenu et les réunis.
4. **Les quatre remarques non tranchées** du rapport (borne basse quand M + 2σ₀ < 0,55 ; zone médiane du contenu et des réunis ; jeu de la garde 27 ; verrou D6 au-delà de la lettre de R-4123) : pour chacune, dis si la lettre des décisions la tranche déjà ; sinon, si elle relève de Lazar (sens d'un GO) ou de la mère (routine, R-4123 étant d'elle), et recommande, avec confiance.
5. **Les écarts déclarés** (« […] » dans les citations ; § 6 au lieu de « point 5 » ; « R-4123, point 3 » pour le 0,63 ; seuil du signalement écrit à M + 2σ₀ ; mots du rédacteur ; lectures partielles) : acceptés ou non.
6. **La liste pour le code v5** : complète et juste.

Rends `controle-differentiel-palier-0b-v8-v9-v1.md` : « Conforme » ou « À corriger », corrections numérotées avec le texte exact (ancre unique comptée par `grep -c -F -e`). Préfère « non exigé » pour la tenue pure. Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-palier-0b-v9/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement du code du palier, aucun tirage. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
