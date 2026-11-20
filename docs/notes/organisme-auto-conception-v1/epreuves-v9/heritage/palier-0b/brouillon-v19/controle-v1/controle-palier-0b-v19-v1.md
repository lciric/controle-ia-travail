# Contrôle différentiel du brouillon de la version 19 — préenregistrement du palier 0b — v1

**BROUILLON EN ATTENTE DU MOT DE LAZAR. Rien n'est scellé ; la version 13 scellée reste le texte en vigueur.**

- **Auteur** : contre-lecteur neuf, modèle O, le même que pour les versions 14 à 18. Je n'ai écrit aucune version du texte ni aucun programme. Pièce de travail (classe C), 2026-11-20.
- **Mandat** : l'en-tête du mandat `84b76af6…`, et le message de la session du compte organisme qui demande ce contrôle.
- **Conditions** :
  - ce que j'ai fait : l'outil sur des copies ; des lectures de fichiers nommés ;
  - ce que je n'ai pas fait : aucun `git fetch`, le registre n'étant pas en jeu ; aucun lancement ; aucune écriture dans l'arbre de travail du dépôt.
- **Aucun refus de permission, de classifieur ni de garde.**
- **Incident, déclaré.** Une commande `grep -n` sur la v19 a rendu une sortie longue. L'outil l'a rangée de lui-même sous `/root/.claude/`. Je n'y ai rien écrit et ne l'ai pas lue ; j'ai refait la recherche, plus étroite.

## Verdict : **Conforme**

Aucune correction. La v19 peut aller à Lazar comme brouillon.

## 1. Rejeu

**Empreintes égales aux compagnons** :
- le mandat (`11260e2a…`) ;
- le dossier `brouillon-v19/` : v19, différentiel (`063f72b7…`), rapport (`5f267a04…`), jeu de tenue (`e1b04387…`), sortie de la passe 1 ;
- mon jeu Y1–Y2 versé (`88e8b4fa…`).

**Rejeu depuis la v18** (`ae1e8f56…`) :
- passe 1 (Y1–Y2) : 2 remplacements, sortie **`d54b6e53…`**, égale à mon essai ;
- passe 2 (tenue) : 6 remplacements, sortie **`f6bff0c6bd8e9b2f571d2d4e642bb6ed8cd40b502cf2bd96e9bd1376ffd17526`**, et `cmp` avec la v19 muet.

## 2. La tenue

**Lieux** (sortie `sortie-lieux-passe-2-v1.txt`) : titre (l. 1), statut et ligne de version (l. 3), date (l. 6), « Contre-lecture » (l. 530 et 566), alinéa « Version 19 » (fin de l'annexe H). Les seules autres lignes changées sont celles de Y1 et Y2 (l. 1158 et 1188 de la v18).

**Contenu** (relu en entier) :
- ce que les nouveaux textes disent de mon contrôle de la v18 est exact ;
- aucune règle, aucun critère, aucun seuil, aucune graine n'est touché ;
- la date porte `date -u` (22:33Z) et l'heure du premier journal (22:32:49Z).

L'alinéa « Version 19 » dit un peu plus que le rangement : le compte des remplacements, et que rien d'autre ne change. C'est de la tenue, sans règle. Sans suite.

## 3. Les mots « Version 18 » dans Y1 et Y2

**Acceptable tel quel.**
- Ces mots datent le renvoi de l'état qu'il décrit : la ligne fixée par les versions 16 à 18.
- Le statut et l'alinéa « Version 19 » disent en propres termes qu'ils entrent par la version 19.
- Le texte a déjà un tel cas : l'annotation « version 17 : … » de la citation de R-4296 porte la mention du complément 4, entrée par la version 18.
- Les remplacer par « Version 19 » romprait l'égalité de la passe 1 avec mon essai, sans rien gagner en sens.

## 4. L'en-tête

- **Ligne du commit** (`sortie-entete-v19-v1.txt`) : une seule ligne commence par « - Commit du code d'analyse : ». `COMMIT_V6` y figure une fois, en blanc, et la ligne ne porte aucun `` `<40 hex>` ``. La table de 64 lignes est le premier bloc qui la suit, égale à l'octet à `table-empreintes-code-v6.txt`.
- **Lieux des empreintes** :
  - `1f04cb46…` : 2 lieux (l. 107 et 407) ;
  - `ed91813a…` : 2 lieux (l. 107 et 408) ;
  - `67052a4b…` : 6 lieux (l. 20, 107, 342, 409, 1162 et 1224).

  Conforme : 2, 2 et 6.

## 5. Vue d'ensemble des sections touchées depuis la v15

**Relu en entier dans la v19** :
- B8 (l. 342), jusqu'à l'alinéa « Version 16 » ;
- la section « Les programmes de lancement des étapes 3 à 9 », en particulier « Ce que chacun rend » et « La pièce de contrôle de la mère » (l. 460 à 469) ;
- la section « ÉCART POUR LAZAR » ;
- l'alinéa sous la liste d'arrêt (l. 526) ;
- l'annexe H, « Version 14 » § 3 et § 7 ;
- l'annexe H, « Version 16 » § 2, remarques 2 à 7 (l. 1224 à 1229) ;
- les alinéas « Version 17 », « Version 18 » et « Version 19 ».

**Aucune contradiction ni règle dite deux fois de façon différente.** Les règles concordent partout où elles sont dites :

| règle | lieux | constat |
|---|---|---|
| constat de fin entre deux lancements | « Ce que chacun rend » ; remarque 3 | la remarque 3 est la forme entière, l'autre lieu un résumé fidèle ; compléments 2 et 3 |
| constat de fin du programme 8–9 | « Ce que chacun rend » ; remarque 4 | même liste (R-4338), au complément 4 |
| empreinte du programme 8–9 | B8, « Version 14 » ; « Version 14 », § 3 et remarque 7, avec leur renvoi ; remarque 2 ; remarque 4 | pièce elle-même et complément 3, contrôle à la main au lancement |
| libellés | « Sa forme » ; remarque 4 | même forme, avec le nom du programme |
| compléments | « Quand elle est écrite » ; remarque 4 ; alinéa « Version 13 » ; annotation de R-4296 | un par lancement, 1 à 3 avant, 4 après, celui de la règle n° 8 en dernier |
| dossiers des sorties | programme 1, silence n° 5 ; annexe C ; remarque 5 ; remarque 4 | celui des étapes 3 à 6 fixé par la pièce (et répété au complément 1) ; ceux des étapes 6 bis à 9 aux compléments 2 et 3 |
| champs du verrou non nuls | B8, « Version 16 » ; programme 2, « Le commit du manifeste » ; remarque 7 | étapes 3 à 7, partout |
| garde 17 | statut ; section « ÉCART » ; alinéa sous la liste d'arrêt ; critères de lecture | écart porté à Lazar, non tranché, partout |

**Deux imprécisions de mots**, sans effet sur une règle. Je ne les corrige pas, et je les signale pour que le lecteur n'y voie pas de désaccord :
- La remarque 4 garde, de la version 17, « celui de la règle n° 8 … vient en dernier, sous le numéro qui lui échoit alors ». La même remarque dit ensuite, par R-4337, que c'est le complément 4. Le « numéro qui lui échoit » est donc 4 : c'est redondant, non contraire.
- « La pièce de contrôle — Ce qu'elle porte » (l. 464) dit que la pièce porte « les chemins et les empreintes des fichiers gelés, inscrits entre les lancements ». La puce suivante (l. 466) et la remarque 4 précisent que tout ce qui s'ajoute après le scellement va dans des compléments. Il faut lire « la pièce » au sens de la pièce et de ses compléments ; les deux puces se suivent et se lisent ensemble.

## 6. Fichiers

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-palier-0b-v12/v19/`.

Fichiers rendus, chacun avec son compagnon :
- cette pièce ;
- `sortie-lieux-passe-2-v1.txt` ;
- `sortie-entete-v19-v1.txt` ;
- `lignes_v1.py`, le programme de lecture des lignes.

Fichiers de travail, non rendus :
- `rejeu-passe-1.md` et `rejeu-passe-2.md`, avec leurs journaux ;
- `passe-2-deplie.txt` ;
- `lecture-sections-v19.txt` et `lecture-alineas-v19.txt`.

*Contre-lecteur neuf, modèle O.*
