# Mandat du rédacteur — ligne 3 des épreuves v9, version 6 du préenregistrement — v1

Pièce de travail (classe C), préparée par la session du compte organisme le 2026-11-19 vers 16:47Z. **Ne part qu'au mot de reprise de Lazar** après le second refus d'outil de 16:4xZ.

## Ce que tu fais

Tu écris la version 6 du préenregistrement de la ligne 3 (et le devis v6 seulement si un chiffre ou un renvoi change). La version 5 reste intacte (R12). La version 6 se vérifie sur son différentiel par un agent neuf.

1. **Les quatre corrections** du compte rendu du vérificateur arrêté (`verification-ligne-3-v5-v1-compte-rendu-arrete.md`, même dossier, `9031205f…`), à la lettre quand il donne un texte exact : le repli sur les sept cartes réécrit, avec un seul déclencheur aux trois endroits ; le trou de la condition (3) ; le morceau non déclaré de l'en-tête, rétabli ; la forme des deux bascules.
2. **Les conditions de cloisonnement de la mère** (vers 15:39Z, 16:39Z et 16:44Z), toutes écrites au texte :
   - (1) le fichier des cartes et les 94 cartes sont la seule entrée de la garde ;
   - (2) la lecture se fait par programme seulement, champ `meta` retiré avant tout usage ;
   - (3) la garde ne rend que ce que le texte dit (comptes, empreintes, décision de la garde), jamais le contenu d'une carte à un agent qui conçoit ou juge ;
   - (4) le contrôle dans le code se fait à la contre-lecture du code de la banque, avant la première ouverture du fichier des cartes ; sans ce contrôle passé, la garde ne tourne pas ;
   - (5) au plus cinq rejeux de la garde sans le mot de la mère ; les messages d'erreur et les traces d'exception entrent dans la liste fermée de ce que la garde rend ; rien d'autre ne sort ;
   - le repli sur les sept cartes nommées se déclenche par une règle mécanique écrite, sans rien regarder des cartes ; l'écart au manifeste est déclaré ; il ne vaut que pour ces sept cartes, aux mêmes règles de lecture et sous la condition (5).
3. **L'empreinte du fichier des cartes**, quand le texte en a besoin, se prend par le code de la banque, à sa contre-lecture. Elle ne se prend jamais par une commande d'agent.
4. Garde tout le reste de la version 5. Déclare tout ajout dans le rapport, avec sa raison.

## Ce que tu lis

`CLAUDE.md` ; dans `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/` : la version 5 (`915fbe4b…`), le devis v5 (`43bcb1c8…`), le rapport du rédacteur v5 (`c03a952e…`), le compte rendu du vérificateur arrêté (`9031205f…`), la vérification v4 (`597b97bb…`), les mandats v4 et v5. Vérifie chaque empreinte avant de citer (R6, R11).

## Interdit écrit en tête

**Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Tu n'ouvres aucune carte.

## Ce que tu rends

Dans ton bloc-notes seulement : `preenregistrement-ligne-3-votes-effectifs-juges-v6.md`, le devis v6 s'il y a lieu, et `rapport-redacteur-ligne-3-v6-v1.md`. En-tête : « Auteur : rédacteur neuf, modèle F » ; aucun identifiant de modèle ; heure par `date -u`.

## Autres interdits

Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée, aucune écriture dans le dépôt. Jamais de heredoc. Aucune valeur de clé. Ni « consigne-privee », ni « conception-ii-b », ni `/root/.claude/`. N'écris jamais le nom d'une commande d'arrêt par motif dans une commande. Au premier refus d'un outil : arrête-toi et dis-le.
