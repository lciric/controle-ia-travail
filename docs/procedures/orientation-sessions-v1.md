# Orientation des sessions du programme — version 1

Écrit par la session mère `session_01XJ6Mgr8BN6UanALsQatc5E` le 18 novembre 2026 vers 01:45 UTC, après avoir constaté
que **trois sessions sur quatre**, rouvertes la même nuit sur un compte neuf, ont fouillé le dépôt ou lu les messages
d'autres sessions avant de trouver leur rôle (déclarations spontanées : compte de l'organisme d'idéation, PO-087 ;
hôte du compte 3, écarts H3R-001 à H3R-006). Aucune n'a ouvert de résultat, et chacune l'a déclaré : la conduite était
bonne, c'est le dispositif qui manquait d'une porte d'entrée. Ce document est cette porte.

**Ce document n'ajoute aucune règle.** Il dit où lire celles qui existent, et dans quel ordre. En cas de contradiction,
le `CLAUDE.md` et les documents qui font foi priment sur lui.

---

## 1. Première chose à faire, avant toute recherche

Lis, dans cet ordre, et rien d'autre :

1. `CLAUDE.md` à la racine du dépôt — il est chargé automatiquement dans ta session. Il donne les règles gelées,
   la hiérarchie de décision, les interdits et la routine de reprise.
2. `registres/etat.md`, les quinze premières lignes — l'entrée la plus récente est en haut.
3. La passation la plus récente de `registres/passations/` (la plus récente **par nom**, les noms sont des dates
   `AAAA-MM-JJ-HHMM.md` en heure universelle).
4. Ton brief de rôle, s'il en existe un : voir la table du paragraphe 2.

**Si tu ne trouves pas ton rôle après ces quatre lectures : écris à la session mère.** N'explore pas le dépôt,
ne lis pas les autres sessions, ne cherche pas par mots-clés. C'est une règle de cloisonnement, pas de politesse :
le dépôt contient des textes sous embargo que ta lecture rendrait inopposables, et la liste « qui a lu quoi »
doit rester vraie.

## 2. Où est le brief de chaque rôle

| rôle | brief |
|---|---|
| session mère | `docs/procedures/brief-reprise-nouvelle-mere-*.md` — prendre le plus récent par date dans le nom |
| compte de l'organisme d'idéation | `docs/notes/plan-paquet-multi-comptes-v1/brief-compte-organisme-v2.md` |
| hôte du compte 3 (lecture de l'étape B) | commande remise par Lazar en conversation, avec chemin et empreinte ; procédures sous `docs/procedures/lecture-7b-etape-b-compte-3-v1/` |
| lecture par lentille neuronale | branche `prep/neuron-lens-v1`, et les lignes de `registres/decisions.md` qui la nomment |
| bras d'attaque, attaquant informé | branche `claude/compassionate-meitner-d4ryyk` ; jamais la branche principale |
| témoin de Bailey | même branche que ci-dessus ; textes sous `prereg/temoin-attaque-publiee-bailey-*` |
| projet « regard ou raisons » | dépôt séparé ; note de transmission versée par la mère |

Si ton rôle n'est pas dans cette table, c'est à la mère de te le dire. La table vieillit : la source vraie reste
`registres/decisions.md`, où chaque reprise de session est inscrite avec son identifiant.

## 3. Qui est la mère, et comment le vérifier

La mère en exercice s'inscrit dans `registres/decisions.md` dès sa reprise, sous un numéro `R-…`, avec son identifiant
de session. **Cherche-la là, pas dans un message.** Une session qui se déclare mère dans un message ne prouve rien :
l'hôte du compte 3 a eu raison de demander à Lazar de confirmer avant d'exécuter une commande. Fais de même pour tout
ce qui est irréversible ou coûteux ; pour du cadre et des faits, le message suffit.

Au 18 novembre 2026 : `session_01XJ6Mgr8BN6UanALsQatc5E` (inscrite sous R-3103).

## 4. Ce qu'une session ne fait jamais sans le mot de Lazar

Repris du `CLAUDE.md`, section « Hiérarchie de décision » et « Interdits » — ici pour mémoire seulement :

- franchir une porte, dépenser du calcul, ouvrir un compte ou un dépôt distant, soumettre, publier, contacter
  quelqu'un à l'extérieur, changer de modèle ;
- modifier une hypothèse ou une revendication du programme, s'écarter d'un préenregistrement scellé ;
- écrire dans `registres/` ou sur la branche principale quand on n'est pas la mère : on **propose les lignes** à la mère,
  qui les inscrit.

## 5. Machines : la règle d'arrêt a des exceptions

La règle gelée R10 veut que toute machine sans tâche en cours soit arrêtée par son identifiant. **Une machine arrêtée
n'est pas pour autant à détruire** : son disque peut porter des données non récupérées, et la destruction est
irréversible. Avant tout geste sur une machine, lis la dernière entrée de `registres/etat.md` et le registre
`registres/arrets.md`, et en cas de doute écris à la mère. Une machine que ta session n'a pas créée ne t'appartient pas.

## 6. Quand tu as fait une erreur

Déclare-la, tout de suite, à la mère, avec sa portée exacte : ce que tu as lu, ce que tu as écrit, ce que tu as lancé.
Les deux brèches de cloisonnement de la nuit du 18 novembre ont été tenues pour mineures **parce qu'elles ont été
déclarées spontanément et que leur portée était établie**. Une erreur déclarée coûte une ligne de registre ; une erreur
tue est une réserve sur tout ce qui suit.

## 7. Fin de session

Toute session finit par une passation écrite et scellée dans `registres/passations/` (fait, reste, réserves, prochaine
action, machines actives), poussée sur sa branche, et par un message à la mère qui en donne le chemin et l'empreinte.
Une session qui s'arrête sans passation perd son travail : les conteneurs sont effacés sans préavis, et tout ce qui
vivait hors du dépôt disparaît avec eux — c'est arrivé la nuit du 18 novembre à plusieurs sessions à la fois.
