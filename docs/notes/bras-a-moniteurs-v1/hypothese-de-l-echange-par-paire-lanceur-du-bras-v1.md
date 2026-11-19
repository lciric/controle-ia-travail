# Ce qui distingue les deux épisodes d'une paire dans le lanceur du bras A — vérification pour l'échange par paire — v1

Écrit par le développeur habilité côté moniteurs, le 19 novembre 2026, à la demande de la session mère. Sans interne de moniteur. Rien n'est exécuté : lecture du code seulement.

**Verdict.** Dans le code du lanceur, la dose est la seule chose **voulue** qui distingue l'épisode honnête et l'épisode dosé de même tâche et de même rang. Trois différences de fait restent, qui ne sont pas la dose : l'ordre d'exécution, le remplissage des lots, et l'adaptateur chargé à l'échelle 0 pour l'honnête. Aucune ne brise l'échange par paire sous l'hypothèse « la dose ne change rien », à une condition que le code vérifie déjà en partie (état de phase, base au bit près) et que la lecture du code ne peut pas établir en entier (déterminisme de la machine).

Pièce lue : `src/controle_ia/organismes_discrets/lanceur_bras_a_v2.py`, `14dfcf3c5da91ce630d865196504dcd3acbf75afafd7dd7b2a4c50bb523086fb`, branche de la relance, commit `5031865b` ; fonctions `rejouer` et `jouer_honnetes` ; `graines_des_actions` de `src/controle_ia/environnements/pilote_a.py`.

## Ce qui est identique dans une paire

| objet | constat dans le code |
|---|---|
| graines | la graine de l'épisode est la clé `verification/tache/{tâche}/e{k}`, sans la condition ; les graines des actions de chaque pas en sont tirées ; la même fonction joue toutes les conditions |
| entrées | même tâche, même environnement (l'environnement honnête, pour toutes les conditions), même nombre de pas, même guide |
| réglages | même configuration : jetons générés au plus, température, couches, tolérance |
| plan des lots | même liste (tâche, rang) dans le même ordre, même taille de lot : un épisode est dans le même lot, à la même place, dans toutes les conditions |

## Ce qui diffère, hors la dose

1. **L'ordre d'exécution.** L'honnête est jouée d'abord, puis chaque condition dosée, dans l'ordre des adaptateurs. Sans effet si rien ne passe d'une condition à la suivante ; le lanceur vérifie l'état de phase avant et après chaque lot (échelle et empreinte de l'adaptateur).
2. **L'adaptateur de l'honnête.** L'honnête n'est pas jouée sans adaptateur : le premier adaptateur de la liste est chargé, à l'échelle 0. Le contrôle d'identité du lanceur vérifie que les logits sont alors ceux de la base au bit près.
3. **Le remplissage des lots.** Les graines sont communes, mais dès qu'un texte diffère, les deux épisodes ne suivent plus le même contexte ; leurs longueurs diffèrent, et le remplissage du lot avec elles. C'est un effet de la dose sur les voisins de lot, borné par la garde d'équivalence du jeu d'épisodes (tolérance de la configuration).

## Ce que cela dit de l'échange par paire

- Les deux épisodes d'une paire partagent leurs tirages : leurs scores se ressemblent. C'est ce qui rend la permutation libre très prudente, et l'échange par paire adapté.
- L'échange par paire suppose que, si la dose ne change rien à la loi des textes, les deux épisodes d'une paire sont échangeables. Les points 1 à 3 ne donnent à l'un des deux aucun avantage qui ne vienne pas de l'adaptateur.
- **L'honnête est commune aux quatre doses** : l'épisode honnête de rang k est le pair de l'épisode de rang k de chaque dose. Les valeurs p des doses ne sont donc pas indépendantes ; la correction de Holm ne le demande pas.
- **Ce que la lecture du code n'établit pas** : que la machine rejoue au bit près d'un lot à l'autre. Le lanceur fixe le déterminisme et le vérifie sur ses contrôles ; un écart serait un bruit de plus dans la paire, symétrique sous l'hypothèse nulle.
- **Paire incomplète.** Si toutes les unités d'un épisode manquent pour un moniteur, son pair garde son étiquette dans le code des moniteurs (`autres_moniteurs_v8.py`, `61105129f58f5df590b033c183e7ab334f56a51cc03bb04e86ebdb52e6e53760`). Les positions lues par le juge sont les mêmes dans toutes les conditions.

## À écrire au texte, si l'échange par paire est retenu

« L'échange par paire s'appuie sur le lanceur du bras, cité par son empreinte : les épisodes de même tâche et de même rang y sont joués, dans toutes les conditions, avec les mêmes graines, les mêmes entrées, les mêmes réglages et le même plan de lots ; seuls diffèrent l'adaptateur et son échelle. Tout changement du lanceur sur l'un de ces points défait l'hypothèse et demande de la revérifier. »
