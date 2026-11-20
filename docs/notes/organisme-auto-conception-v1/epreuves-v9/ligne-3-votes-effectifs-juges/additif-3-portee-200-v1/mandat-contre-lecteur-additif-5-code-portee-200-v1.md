VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main` ET NON SUR `FETCH_HEAD`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contre-lecteur — additif 5 (code de la mesure « portée à 200 » de la ligne 3) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sous GO-2026-11-20-26, l'additif 3 v3 scellé et R-4172 (rang « additif 5 » confirmé par la mère). Contre-lecture par un autre modèle que le rédacteur (modèle F), règle R2 ; puis scellement par la mère, qui recopie le dossier du code sur `main` et écrit les deux blancs permis.

## Qui

Un contre-lecteur neuf, modèle O, qui n'a écrit ni le texte de la ligne 3, ni ses additifs, ni le code, ni sa contre-lecture, ni le verdict de l'étage 1. Tu signes « contre-lecteur neuf, modèle O ».

## Règle d'aveugle

Tu n'ouvres aucune mesure de l'étage 1 : rien sous `…/execution-etage-1-v1/`, `…/verdict-etage-1-v1/`, ni `prereg/organisme-auto-conception-v9/ligne-3/verdict-etage-1/`.

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

Dossier L3 = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/`.
- `L3/additif-3-portee-200-v1/additif-5-code-preenregistrement-ligne-3-portee-200-v1.md` (`d1b237d602d68b488510ff0ba94f9519481984554ae6627807ce43f1a1c4233d`) et le rapport de son rédacteur (`de001c34…`) ; son mandat `L3/additif-3-portee-200-v1/mandat-redacteur-additif-5-code-racines-portee-200-v1.md` (`8a669690…`).
- L'additif 3 scellé et l'additif 2 scellé, tirés de `origin/main` (`prereg/organisme-auto-conception-v9/additif-3-preenregistrement-ligne-3-portee-200-v3.md`, `71b7a876…` ; `prereg/organisme-auto-conception-v9/additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v3.md`, `f5562d20…`).
- Le code `L3/code-portee-200-v4/` (quatorze fichiers et leurs compagnons) ; la contre-lecture du code `L3/additif-3-portee-200-v1/contre-lecture-banc-v4-portee-200-v1.md` (`ab19b31a…`).

## Ce que tu fais

1. **Chaque empreinte** de la table de l'additif recalculée sur disque et égale au compagnon ; le commit `af19ff8d…` porte ces octets (`git -C /home/user/controle-ia-travail show af19ff8d:CHEMIN > FICHIER` puis `sha256sum`, pour le banc et le chronométrage au moins).
2. **Fidélité au § 5 de l'additif 3** : l'additif ne fait que nommer le code, les racines, les commandes ; aucune règle, aucun seuil, aucune prédiction, aucune lecture ne change.
3. **Les commandes** : complètes, exactes, lançables telles quelles une fois les deux blancs écrits ; l'ajout de deux `env -u` (variables de chemin) : garder ou retirer ; les dossiers de sortie choisis (`…/execution-portee-200-v1/chronometrage` et `…/mesure`) : hors du dossier du code, absents, sans `archives-reponses-modeles/` au-dessus ; le chronométrage à `--repliques-echantillon` par défaut.
4. **L'interpréteur proposé** (`python3`, numpy 2.5.3) : juste au regard des additifs 2 et 3 et de la contre-lecture du code ; vérifie toi-même la version par `python3 -m pip show numpy` ou équivalent sans `-c`.
5. **Les deux blancs** (commit de `main` du dossier recopié ; empreinte du compagnon de l'additif) : les seuls ; rien d'autre à écrire par la mère.
6. **Verdict** : « Conforme, à sceller » ou « À corriger », avec « Ancien » et « Neuf » exacts (ancre unique comptée par `grep -c -F -e`).

Écris `contre-lecture-additif-5-code-portee-200-v1.md` dans ton dossier `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-additif-5/`, avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête et la règle d'aveugle. Aucun lancement du banc ni du chronométrage, aucune dérivation de graine. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense, aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
