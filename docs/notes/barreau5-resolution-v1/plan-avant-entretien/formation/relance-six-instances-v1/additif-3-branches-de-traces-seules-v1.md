# Additif 3 au plan « sabotage ou empreinte de l'adaptateur » (barreau 5) : branches de sortie qui ne portent que des traces — v1

Projet d'additif, écrit le 20 novembre 2026. Il complète l'additif 2, version 6, scellé par la session mère (sha256 `3562d5a11bb1967cb9ade2df6c901f78f8f16384efc3393ca9ff3bccd0012626`). **Il attend le mot de Lazar** : c'est un écart à un texte scellé, donc un nœud. Rien n'est supprimé ni recréé avant ce mot, la contre-lecture et le scellement par la session mère.

Un seul mot de Lazar couvre l'additif 2 version 6, cet additif 3, les quatre destructions des premières tentatives des relances 1, 2, 3 et 4, les trois suppressions des branches de sortie des relances 2, 3 et 4, et les quatre recréations hors de la machine 144450, sous la réserve de dépense de l'additif 2. La session mère le lui demande en une seule question, et le consigne en une ligne du registre des accords qui les nomme tous.

- **Textes visés** : le plan scellé (`prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md`, sha256 `bdff244f…d935`), son additif 1 (version 3, sha256 `20e862a3…606a`) et son additif 2 (version 6). Aucun n'est réécrit ; cet additif prime sur les seuls passages nommés à la section 3, pour les seules branches de la section 2.
- **Ce que le rédacteur a lu** : les extraits permis du plan, les additifs 1 et 2, l'amorce au commit de course. Les faits de la section 1 sont ceux qu'atteste la session mère. Aucune branche de données n'a été ouverte par le rédacteur ; aucune sortie, aucun score.
- **Portée** : les branches de sortie des premières tentatives des relances que cite la ligne `GO-RELANCE-FORMATION-B5F`, quand elles ne portent que des traces. Rien d'autre.

## 1. Les faits, sans aucune sortie lue

- Les relances 2, 3 et 4 (machine 144450) sont tombées sur « ARRET : installation des paquets », à 15:45:07Z, 15:46:14Z et 15:45:54Z, sans ligne « marche : début ».
- Le réseau est ensuite revenu. Leur amorce a écrit « versement final prouvé : 4 fichiers », puis « fin, code 2 ; stopped demandé », entre 15:50Z et 15:51Z.
- Leurs branches de sortie `donnees/barreau5-familles-jumelles-v1-formation-instance-<n>-x1` existent donc sur le dépôt distant : instance 2 à la tête `4fef6073…`, instance 3 à `b35dfe17…`, instance 4 à `77fd59da…`.
- Depuis le commit de course `4bdf0d22e4246b4fe431bd8754e26fea4ccd037f`, ces branches ne portent que le dossier `traces-b5f/` : `inventaire-final.json` et son compagnon d'empreinte, `journal/journal-b5f.txt`, `nvidia-smi.txt`, `nvidia-smi-entete.txt`, `pip.txt` (vide). Aucun chemin sous `donnees/`, `runs/` ni `diag/`.
- Elles ont été copiées telles quelles, à 15:57Z, sous `traces/barreau5-relance-<n>-premiere-tentative` ; la poussée est prouvée : la tête distante de chaque copie égale le commit d'origine.
- La condition « branche de sortie absente » de l'additif 2 est donc fausse pour les relances 2, 3 et 4, et l'amorce d'une instance recréée refuserait de partir (ligne 282 : branche de sortie présente sur le dépôt distant).

La relance 1 n'est pas concernée : sa branche de sortie n'existe pas.

## 2. Ce que dit l'additif

**Une branche de sortie qui ne porte que `traces-b5f/`, sans `donnees/`, `runs/` ni `diag/`, copiée et prouvée sous `traces/…`, peut être supprimée du dépôt distant avant la recréation de sa relance.**

**Règle mécanique de vérification.** Elle porte sur des noms de chemins et des identifiants de commits seulement ; aucun fichier n'est ouvert. Pour la relance de l'instance `<n>`, avec `B` = `donnees/barreau5-familles-jumelles-v1-formation-instance-<n>-x1` et `T` = `traces/barreau5-relance-<n>-premiere-tentative`, les quatre conditions suivantes sont vraies :
1. la relance est tombée et sa marche n'a jamais commencé, au sens des conditions 1 et 2 de l'additif 2, version 6 ;
2. la tête de `B` descend du commit de course (`git merge-base --is-ancestor 4bdf0d22… <tête>`), et `git diff --name-only 4bdf0d22… <tête>` ne rend que des chemins sous `traces-b5f/` : aucun sous `donnees/`, `runs/` ni `diag/`, aucun ailleurs ;
3. la copie existe à la même tête : `git ls-remote` rend, pour `refs/heads/T`, le même identifiant de commit que pour `refs/heads/B` ;
4. la première tentative est détruite (pas 4 des six gestes de l'additif 2) : arrêtée seulement, elle pourrait pousser de nouveau sa branche.

Si l'une des quatre est fausse, rien n'est supprimé : c'est un nœud.

**La suppression.**
- Par le seul nom exact de la branche `B`, écrit en entier ; jamais par un motif ni par une liste calculée.
- Consignée par la session mère : nom de la branche, tête supprimée, nom et tête de la copie, heure.
- Vérifiée absente ensuite : `git ls-remote --exit-code` ne rend rien pour `refs/heads/B`.
- La copie `T` n'est jamais supprimée ni réunie à la branche de la formation.

**Puis la condition « branche de sortie absente » de l'additif 2 est relue.** C'est sa condition 3 dans la version 6 (sa « condition 2 » dans les versions 1 à 3). Elle est relevée après la suppression, et la recréation suit les règles de l'additif 2, inchangées : une recréation au plus par relance, même nom, mêmes familles, mêmes graines, même commande, même commit de course, offre hors de la machine d'une relance tombée, réserve de dépense relevée avant chaque recréation.

**Ordre, pour une relance dont la branche de sortie ne porte que des traces.** Arrêt par l'identifiant ; inventaire du disque ; copie prouvée de la branche de sortie sous `T` (elle tient lieu du versement des traces du pas 3) ; destruction sur le mot de Lazar ; vérification des quatre conditions ; suppression de `B`, consignée et vérifiée ; relevé des conditions de l'additif 2 ; recréation.

## 3. Ce que l'additif remplace, pour ces seules branches

| passage | ce qui le remplace |
|---|---|
| plan, « Données gardées » : sorties gardées « sur des branches du dépôt », dont `…-instance-<n>-x1` pour une relance ; « Aucune sortie n'est supprimée avant son versement » | les traces d'une première tentative restent gardées, à l'identique, sous `traces/barreau5-relance-<n>-premiere-tentative` ; la branche `…-instance-<n>-x1` qui ne porte qu'elles est supprimée après cette copie prouvée, et son nom est rendu à la recréation |
| règle des noms versionnés (R12) : on n'écrase jamais | exception déclarée : le nom de la branche de sortie est repris par la recréation ; rien n'est perdu, la copie garde le contenu et la tête d'origine |
| additif 2, version 6, section 2, pas 3 : traces versées sur une branche de traces | la copie de la branche de sortie sous `T` tient lieu de ce versement |
| additif 2, version 6, section 6 : nœud « une première tentative […] dont la branche de sortie existe » | n'est plus un nœud quand les quatre conditions de la section 2 sont vraies ; le reste dans tout autre cas |

Tout le reste du plan et des additifs 1 et 2 est inchangé.

## 4. Pourquoi cela ne coûte rien à la lecture

- Le code de lecture figé ne lit que les dossiers de marche `donnees/<marche>` de la branche réunie de la formation. Les branches supprimées n'en portent aucun, et leurs copies sous `traces/…` ne sont jamais réunies à cette branche.
- Aucune sortie d'une marche n'existe pour ces relances : rien n'est écarté ni choisi. Les familles recréées portent les noms et les graines que le plan fixait.
- Sans la suppression, la recréation est impossible : l'amorce s'arrête si la branche de sortie existe (ligne 282), et le code figé ne connaît pas d'autre nom de copie que `-x1` (additif 2, section 4).

## 5. Qui tient quoi

- **Le code, sans changement** : l'amorce refuse une branche de sortie présente.
- **La session mère** : les quatre conditions, relevées et écrites pour chaque branche ; la suppression par le nom exact, consignée et vérifiée ; la garde des copies sous `traces/…`.

## 6. Nœuds

Remontent à Lazar, sans rien supprimer : une branche de sortie qui porte un chemin hors de `traces-b5f/` ; une tête qui ne descend pas du commit de course ; une copie absente ou d'une autre tête ; une première tentative non détruite ; la suppression de toute autre branche, ou d'une branche de traces.
