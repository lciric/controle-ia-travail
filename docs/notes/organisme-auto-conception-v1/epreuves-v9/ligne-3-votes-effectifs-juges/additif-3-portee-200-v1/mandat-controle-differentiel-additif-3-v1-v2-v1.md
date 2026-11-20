VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contrôleur — différentiel v1 → v2 de l'additif 3 de la ligne 3 (portée à 200 témoins) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sous GO-2026-11-20-26 et GO-2026-11-20-36 (point 2), règle R2. Le contre-lecteur de la v1 (modèle O) n'est plus joignable (session close) : tu fais à sa place la vérification de ses corrections. Si tu la juges conforme, la mère scelle la v2.

## Qui

Un contrôleur neuf, modèle O, qui n'a écrit ni le préenregistrement de la ligne 3, ni ses additifs, ni le code, ni le verdict de l'étage 1. Tu signes « contrôleur neuf, modèle O ».

## Règle d'aveugle

Tu n'ouvres aucune mesure de l'étage 1 : rien sous `…/ligne-3-votes-effectifs-juges/execution-etage-1-v1/`, `…/verdict-etage-1-v1/`, ni `prereg/organisme-auto-conception-v9/ligne-3/verdict-etage-1/`. Ce que tu en sais, c'est ce que la contre-lecture en dit.

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

Dossier D = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/additif-3-portee-200-v1/`.
- `D/additif-3-preenregistrement-ligne-3-portee-200-v1.md` (`9e189f1a…`) et `D/additif-3-preenregistrement-ligne-3-portee-200-v2.md` (`bea75ff2b970f9cb344c241bccc63335289b27a97868b7543f5a6dd69a896b94`).
- `D/contre-lecture-additif-3-portee-200-v1.md` (`f264cf9e8c8fca02a308e6831963ab55672f77017e522c653fa2ac2c08b57082`), en entier : verdict, corrections 1 à 3, nœuds 1 à 4, point de procédure.
- `D/remplacements-additif-3-v1-v2.json`, son journal, `D/differentiel-additif-3-portee-200-v1-v2.diff`, `D/rapport-redacteur-additif-3-portee-200-v2.md`.
- L'outil `/home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py` (`391db990…`).
- Sur main (`git -C /home/user/controle-ia-travail fetch origin main`, puis `git … show FETCH_HEAD:CHEMIN > FICHIER_DANS_TON_DOSSIER`) : `registres/go.md`, lignes GO-2026-11-20-26 et GO-2026-11-20-36 ; `registres/decisions.md`, R-4172 et R-4174.

## Ce que tu fais

1. **Rejeu** : l'outil sur la v1 avec le JSON, sortie dans ton dossier ; `cmp` avec la v2.
2. **Fidélité** : chaque correction 1 à 3 portée mot pour mot ; rien d'autre ne change que la tenue (titre, statut, phrase de version) ; la phrase de version et le statut, de la main du rédacteur, jugés.
3. **Les quatre nœuds et le point de procédure devant GO-2026-11-20-36 (2) et R-4172** : pour chacun, dis si la v2, telle qu'elle est, est compatible avec la lettre de la décision, ou si une phrase doit changer avant le scellement. Si oui, donne le texte exact (« Ancien : » / « Neuf : », ancre unique comptée par `grep -c -F -e`). Ce qui relève du second additif (code, racines, calcul versionné du nœud 3) n'est pas à porter ici : dis-le seulement.
4. **Verdict** : « Conforme, à sceller » ou « À corriger », avec les textes exacts.

Écris `controle-differentiel-additif-3-v1-v2-v1.md` dans ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/controle-additif-3-v2/`, avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête et la règle d'aveugle. Aucun lancement du banc. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
