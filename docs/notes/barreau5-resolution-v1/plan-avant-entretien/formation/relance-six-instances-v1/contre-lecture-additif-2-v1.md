# Contre-lecture de l'additif 2 « recréation de la relance de l'instance 1 » — v1

Pièce lue : `additif-2-recreation-relance-1-v1.md`, sha256 d73a322604bc7b7b050fa1bcab23df4561fd6a2cda793bd62efacd5faf987990. Lus aussi, dans le code de lecture figé extrait (`$S/relance/lecture-figee-neuve/`) : `lecture_v1.py` (`instance_de`, `prefixe_de_copie`, `exiger_copie_lue`, `_familles_formees`, `relance_du_registre`) et `relecture_v1.py` (`episodes_propres`). Faits tenus pour vrais : ceux que la mère atteste.

**Verdict : scellable après ces couples.** Aucun n'est bloquant ; deux sont importants.

## Ce que j'ai vérifié dans le code de lecture figé

**« -x2 » est refusé, par quatre voies.**
- `instance_de` ne retire que `-x1` et `-r1`. Le nom « T01-x2 » n'est donc dans aucune instance du plan, et la lecture s'arrête.
- `prefixe_de_copie` ne rend que `<k>` ou `<k>-x1`, et `exiger_copie_lue` n'admet que ce nom ou ce nom suivi de `-r1`.
- `_familles_formees` ne cherche que les marches `…-b5f-formation-<n>` ou `…-<n>-x1`.
- `episodes_propres` refuse toute ligne dont la famille, privée de `-x1` et de `-r1`, n'est pas la famille de base.

La section 4 de l'additif est donc exacte.

**La recréation sous « -x1 » est acceptée, à une condition.** `_familles_formees` exige exactement un dossier `donnees/<AAAAMMJJ-HHMMSS>-b5f-formation-1-x1` dans l'arbre de la branche de la formation. L'horodatage peut être quelconque, donc le nom de marche neuf convient. Les familles « T01-x1 » et « T02-x1 », ou leur retirage, sont la copie lue. Comme la première tentative n'a laissé ni dossier ni branche, il n'y aura qu'une marche. La condition est qu'aucune trace de la première tentative n'entre jamais, sous un tel nom, dans l'arbre de la branche de la formation (couple 1).

## Les deux ajouts du rédacteur

**(1) Traces versées sur une branche d'un autre nom.** La règle est juste et nécessaire : sans elle, `_familles_formees` trouverait deux marches et refuserait. Elle est cependant trop lâche dans sa forme : voir le couple 1.

**(2) Réserve de dépense.** La formule est juste : passé dépensé, plus le maximum restant des relances en cours, plus 26 pour la recréation, plus 21 pour la relecture et 8 pour la répétition générale, au plus 200. Elle est cohérente avec l'additif 1 : la borne de la ligne de relance reste à 147 et la recréation ajoute 26 dollars hors de cette borne. Il manque une précision sur le compteur de l'instance : voir le couple 4.

## Couples

**1. Les traces de la première tentative ne doivent entrer, sous aucun nom de marche, dans la branche de la formation.**
- Constat. L'additif dit « une branche de traces d'un autre nom, choisi par la session mère ». Mais la branche `donnees/barreau5-familles-jumelles-v1-formation` est réunie par la session de formation à partir des branches par instance. Une branche de traces placée sous ce préfixe, ou réunie par erreur, ou un dossier nommé `20261120-144237-b5f-formation-1-x1` sous `donnees/`, donnerait deux marches, et le code figé refuserait la lecture de T01 et de T02.
- Correction. Remplacer « une branche de traces d'un autre nom, choisi par la session mère » par « une branche de traces hors de l'espace `donnees/barreau5-familles-jumelles-v1-formation…` (par exemple `traces/barreau5-relance-1-x1-premiere-tentative`), jamais réunie à la branche de la formation ; aucun chemin de cette branche ne porte un nom de marche de la forme `AAAAMMJJ-HHMMSS-b5f-formation-1-x1` sous `donnees/` ».
- Gravité : important.

**2. L'ordre des gestes, et la seconde condition relevée après l'arrêt.**
- Constat. La première tentative a fini sur « versement final incomplet ou en échec ». Tant qu'elle vit, un versement repris ou une minuterie pourrait encore pousser la branche `…-formation-instance-1-x1` une fois le réseau revenu. Le relevé fait à 15:13Z par `git ls-remote` ne prouve rien pour plus tard. L'additif ne dit pas non plus que la première tentative est détruite.
- Correction. En section 2, écrire l'ordre :
  1. arrêt de `61655405` par son identifiant ;
  2. inventaire de son disque ;
  3. versement prouvé de ses traces (couple 1) ;
  4. destruction par identifiant, consignée dans le registre des arrêts ;
  5. **puis seulement** relevé des deux conditions, dont `git ls-remote` ;
  6. puis recréation.

  Dans la règle mécanique, ajouter à la condition 2 : « relevée après la destruction de la première tentative ».
- Gravité : important.

**3. Un passage remplacé n'est pas nommé.**
- Constat. Le plan dit, pour un versement non prouvé : « l'instance est alors arrêtée sans être détruite, et la mère reprend le versement ». Les « Données gardées » placent, elles, la sortie d'une relance sur `…-instance-<n>-x1`. Pour la première tentative, l'additif envoie ce versement ailleurs, puis détruit l'instance. La table de la section 3 ne le dit pas.
- Correction. Ajouter une ligne à la table :

  | passage | ce qui le remplace |
  |---|---|
  | plan, règle de la relance : versement non prouvé, « la mère reprend le versement » ; « Données gardées » : branche `…-instance-<n>-x1` d'une relance | pour la seule première tentative de la relance 1 : traces versées sur la branche de traces (couple 1), puis destruction |

- Gravité : mineur.

**4. Le compteur de l'instance recréée.**
- Constat. « Coupure : 26 dollars, celle de l'instance 1 » ne dit pas d'où part le cumul de l'instance. Si la session passe au lanceur (`depense … CUMUL_INSTANCE …`) un cumul qui inclut la première tentative, la coupure effective sera plus basse que prévu. Si elle ne l'inclut pas, c'est cohérent avec « une coupure de 26 dollars s'y ajoute ».
- Correction. Ajouter : « le cumul de l'instance recréée compte depuis sa création ; la dépense de la première tentative n'y entre pas, elle reste au compteur commun ».
- Gravité : mineur.

**5. « Sans ouvrir aucune sortie » contre le journal lu.**
- Constat. La condition 1 se relève dans le journal « B5F », que les « Données gardées » rangent parmi les contenus de la branche de la formation. La lecture est mécanique et porte sur des lignes d'état de l'amorce, ce qui est permis par le point 12. La phrase « sans ouvrir aucune sortie » est donc inexacte à la lettre.
- Correction. Écrire « relevées par la session sur les seules lignes d'état de l'amorce (arrêt de préparation, absence de « marche : début ») et sur `git ls-remote`, sans ouvrir aucune sortie de la marche ».
- Gravité : mineur.

**6. La cause invoquée.**
- Constat. Le plan nomme « perte de l'hôte », non « perte du réseau de l'hôte ».
- Correction. Écrire « perte du réseau de l'hôte, assimilée à la perte de l'hôte, cause que le plan range parmi celles qui ne lisent aucune sortie ».
- Gravité : mineur.

## Hors de mes lectures
Je n'ai pas vérifié dans l'amorce que « l'amorce de l'instance recréée s'arrête si cette branche existe » : l'amorce n'était pas dans les fichiers à lire. L'affirmation est à confirmer par qui l'a lue, ou à retirer de la section 2.
