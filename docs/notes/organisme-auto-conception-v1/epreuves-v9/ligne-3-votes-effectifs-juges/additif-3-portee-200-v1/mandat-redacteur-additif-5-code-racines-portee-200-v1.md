VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main` ET NON SUR `FETCH_HEAD`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — additif de code de la mesure « portée à 200 » de la ligne 3 (second additif court, R-4172) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sous GO-2026-11-20-26 et l'additif 3 v3 scellé (`ADDITIF-3-ORGANISME-V9-LIGNE-3`, `71b7a876…`), § 5 point 4 : « La pièce qui autorise est l'additif de code de cette mesure, court, qui ne fait que nommer le code (commit, empreinte de chaque fichier, commandes du point 8 complétées), scellé par la mère après la contre-lecture du code. » Le code est contre-lu « Conforme ». Ensuite : contre-lecture de l'additif par un autre modèle, scellement par la mère ; puis chronométrage, passage unique, verdict.

## Qui

Un rédacteur neuf, modèle F, qui n'a écrit ni le texte de la ligne 3, ni ses additifs, ni le code, ni le verdict de l'étage 1. Tu signes « rédacteur neuf, modèle F ».

## Règle d'aveugle

Tu n'ouvres aucune mesure de l'étage 1 : rien sous `…/execution-etage-1-v1/`, `…/verdict-etage-1-v1/`, ni `prereg/organisme-auto-conception-v9/ligne-3/verdict-etage-1/`.

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

Dossier L3 = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/`.
- L'additif 3 scellé (tiré de `origin/main`, `prereg/organisme-auto-conception-v9/additif-3-preenregistrement-ligne-3-portee-200-v3.md`), en entier ; l'additif 2 scellé (`prereg/organisme-auto-conception-v9/additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v3.md`, `f5562d20…`), § 6, comme modèle de forme.
- Le code : `L3/code-portee-200-v4/`, chaque fichier et son compagnon ; commit de son versement sur la branche `lot/compte-organisme-v1` : `af19ff8dbb0e1c990f7bb97f7e5a77a332dca14c`.
- Le rapport du développeur `L3/additif-3-portee-200-v1/rapport-developpeur-banc-v4-portee-200-v1.md` (`117b7686…`) et la contre-lecture `L3/additif-3-portee-200-v1/contre-lecture-banc-v4-portee-200-v1.md` (`ab19b31a1597f471b1ac057dbe92638bf29dd1a422c83af26ffe3dc6f613d2fd`), en particulier ce qu'elle dit que l'additif de code doit porter.

## Ce que tu écris

`additif-5-code-preenregistrement-ligne-3-portee-200-v1.md` (le nom final et le rang « 5 » sont à confirmer par la mère ; écris-le en remarque), court, qui ne fait que :
1. **Nommer le code** : le dossier, chaque fichier avec son empreinte (table), le commit ; dire que le chemin et le commit de lancement sont ceux du dossier tel que la mère le recopie sur `main` au scellement, à empreintes égales (laisse le commit de `main` « à écrire par la mère au scellement » si tu ne peux le connaître ; c'est le seul blanc permis).
2. **Les racines autorisées** : 2026112031 (chronométrage), 2026112032 et 2026112033 (mesure), clés 2 et 12, `.spawn(210)`, et elles seules ; toutes les autres refusées.
3. **Les deux commandes du gabarit, complétées** : chemin absolu de cet additif et l'empreinte de son compagnon (« à écrire par la mère au scellement » : un fichier ne porte pas sa propre empreinte) ; `DOSSIER` et `DOSSIER_NEUF` hors du dossier du code, absents ; `PYTHONDONTWRITEBYTECODE=1` ; variables `BANC_LIGNE_3_CHEMIN` et `CHRONOMETRAGE_LIGNE_3_CHEMIN` non posées ; le chronométrage d'abord, la mesure ensuite, une fois chacun ; échéance de GO-2026-11-20-26 (2026-11-30).
4. **L'interpréteur et la version de numpy** retenus pour le passage (point de la contre-lecture : essais passés sous l'environnement du dépôt, numpy 2.4.6, et sous `python3`, numpy 2.5.3) : propose lequel, avec sa raison, et que le manifeste consigne `versions.numpy` ; c'est une remarque si la lettre de l'additif 3 ne le tranche pas.
5. **Le dossier du code commité entièrement** avant le lancement (garde « dossier du code propre »), et la réserve de la contre-lecture : un fichier ignoré par `.gitignore` passe la garde.
6. **Rien d'autre** : aucune règle, aucun seuil, aucune prédiction, aucune lecture ne change ; tout le reste est l'additif 3.

Puis un rapport court `rapport-redacteur-additif-5-code-portee-200-v1.md` (ce qui est nommé, les blancs laissés à la mère, remarques).

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-additif-5-code-portee-200/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête et la règle d'aveugle. Aucun lancement du banc ni du chronométrage, aucune dérivation de graine. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense, aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
