# Rapport du développeur : collisionneur v9-v8m (v1)

Pièce de classe B. Développeur : Claude Opus 5.5, 22 novembre 2026. Copie de la v8l (`da282cf7…`, inchangée), sur une
règle neuve de l'arbitre.

## 1. Fichiers

Tous dans `docs/notes/collisionneur-v9/`. Rien n'est scellé ni commité ; aucun processus n'a été touché ; aucun
fournisseur n'a été appelé.

| Fichier | sha256 | Rôle |
| --- | --- | --- |
| `collisionneur_v9_v8m.py` | `420394f9d803bc4eb41f0e469a30e0be647e11a2c91ac9f42e70c90fdb31c377` | script neuf |
| `fabriquer_v8m_depuis_v8l_v1.py` | `5f09270f…` | remplacements exacts, empreinte de la v8l contrôlée |
| `test_collisionneur_v9_v8m.py` | `75ed33da…` | copie des essais de la v8l (`7a4a0f38…`), trois accords marqués « v9-v8m », section v9-v8m en fin de fichier |

## 2. Niveau du rejeu

Le niveau est vérifié sur la page https://platform.claude.com/docs/en/build-with-claude/effort, lue le 22 novembre 2026.
« xhigh » y est documenté pour Fable 5.2, Fable 5.1 et Opus 5.5.

Opus 4.6 n'a pas « xhigh » : la page dit « Not every model that supports `max` supports `xhigh` ». Pour lui, le plus haut
niveau documenté sous « max » est **« high »**.

La table est `REJEU_EFFORT`.

## 3. Ordre exact des essais d'une cellule d'Anthropic sous `--effort-max`

1. **Essai 1** : effort `max`, premier plafond.
   - S'il finit en `max_tokens` sans texte, l'essai 2 est **le rejeu**.
   - Le rejeu prend la place de la relance de la v8l : il ne s'y ajoute pas.
   - Il part au plafond de relance, à l'effort `xhigh` (`high` pour Opus 4.6).
   - S'il finit coupé avec du texte, l'essai 2 est la relance de la v8l : effort `max`, plafond de relance.
2. **Essai 2, si c'est la relance** : s'il finit en `max_tokens` sans texte, **le rejeu vient en essai 3**, au plafond de
   relance.
3. **Le rejeu** :
   - il est déclaré au journal (`rejeu_effort_xhigh_declare`) et à l'écran, après les gardes de dépense et avant l'envoi ;
   - il n'a lieu qu'une fois ;
   - s'il finit encore en `max_tokens` sans texte, l'arrêt prend le statut `MAX_TOKENS_SANS_TEXTE`, au **code 9**, qui
     est celui de la v8d : rien n'est écrit, et la commande suivante ne renvoie pas la cellule ;
   - s'il finit coupé avec du texte, c'est la fin : statut `TRONQUE`, aucun autre envoi.

Au pire, une cellule fait donc trois essais. Pour le devis et la garde :
- `nombre_relances` vaut 2 pour une espèce d'Anthropic sous `--effort-max`. Le pire « avec relances » du devis de
  reprise grimpe d'une relance.
- Chaque envoi, rejeu compris, est vérifié contre le plafond et contre la ligne avant de partir. Un rejeu refusé à ce
  stade n'est pas déclaré.
- Sans `--effort-max`, rien ne change par rapport à la v8l.

## 4. Opus 4.6

La réflexion adaptative est toujours envoyée. L'effort est `high` par défaut, comme pour les autres espèces, et `max`
seulement avec `--effort-max`.

## 5. Essais et mutations

Lancés sous `env -u` de toutes les clés : **518 passés, 11 sautés**. Il y a 11 essais neufs, sains et artefacts.

Sur 13 mutants, 12 sont pris. Un seul survit, et il est équivalent : retirer la condition « pas déjà un rejeu » ne
change rien. Un rejeu sans texte prend en effet le statut `MAX_TOKENS_SANS_TEXTE` avant ce test. La condition est
gardée en défense.

Programme : `/tmp/claude-0/-home-user-controle-ia-travail/cf01708e-9b7d-5868-b0e7-26f697d45137/scratchpad/mutations_v8m.py`.
