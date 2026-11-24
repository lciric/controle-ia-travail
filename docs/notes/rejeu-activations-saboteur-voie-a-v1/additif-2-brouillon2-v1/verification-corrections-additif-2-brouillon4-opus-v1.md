# Vérification des corrections — additif 2 au texte de lecture des sondes sur les épisodes du saboteur à budget (barreau 8), brouillon 4 — v1

## En-tête

- **Relevés de l'heure (`date -u`), tels quels** : au début, `Tue Nov 24 09:50:00 UTC 2026` ; à la fin des vérifications par programme, `Tue Nov 24 09:50:51 UTC 2026` ; l'écriture de ce rapport suit.
- **Pièces vérifiées, empreintes recalculées (`sha256sum`), égales à leur compagnon :**
  - brouillon 4 `docs/notes/rejeu-activations-saboteur-voie-a-v1/additif-2-brouillon2-v1/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1-brouillon4.md` — `0d3f1adc07e09e8cdce838a724569cd3f7db3a5c56008dc7dc1c48b960a5ab7e` ;
  - programme des corrections `…/corrections_brouillon3_vers_brouillon4_v1.py` — `5fb7cbba1196c827e51c27b6d831bd566c7eaaae6c76b38f60fc10f80c0e99da` ;
  - brouillon 3, même dossier — `e3c747f113565588c3a0a655eec673aa040b8d4b75c219b75b2e8f6b8baf594f` ;
  - mon second rapport `…/verification-corrections-additif-2-brouillon3-opus-v1.md` — `05d8850cf7949f20329f09ff271d9d4eab1a10cda60d9db25ee2b5ffa6a9e8f3` (c'est l'empreinte que cite le brouillon 4) ;
  - les autres pièces sont inchangées depuis mes deux premières vérifications.
- **Qui je suis** : le même vérificateur que pour les brouillons 2 et 3 — sous-agent neuf, modèle Claude Opus 5.5, du côté des moniteurs, non exposé au saboteur. Je n'ai écrit aucune pièce de l'additif 2 ni aucun programme des corrections, hors de mes trois rapports.
- **Déclaration de cloisonnement** : lus en plus de mes deux premières listes : le programme des corrections du brouillon 3 au brouillon 4, en entier ; le brouillon 4, par sa différence au brouillon 3 et par les lignes changées. Rien n'a été ouvert sous `runs/`, `diag/`, `donnees/`, `coffre/`, `docs/verdicts/`, `brouillons/`, `registres/iib-*`. Je n'ai ouvert aucune autre branche, aucun ordre, aucune sortie, aucun épisode, aucun score et aucune issue. Je n'ai modifié aucun fichier existant. Le rejeu et les essais sont dans mon bloc-notes, hors du dépôt.
- **Correction de mon second rapport (déclarée ici ; ce rapport n'est pas touché)** : il dit la vérification faite « entre 09:44Z et 09:55Z ». L'heure de fin, 09:55Z, était fausse : j'avais écrit une heure anticipée. Le fichier a été écrit à 09:46:42Z. Le brouillon 4 écrit « vers 09:45Z », ce qui est juste.

## Verdict

**À corriger, sur un seul point mineur, de lettre** : quatre phrases du brouillon 4 deviendraient fausses dans la version scellée (défaut D). La règle du scellement ne permet de les changer qu'avant le scellement. Elles disent le brouillon « non vérifié », en attente d'une vérification, et ses corrections « pas vérifiées ».

Ce défaut levé, et les deux remarques de forme, au choix du rédacteur, le texte peut aller au scellement après remplissage des champs ouverts :
- les défauts A, B et C et mes deux remarques de forme sont portés ;
- le rejeu redonne le brouillon 4 à l'octet ;
- rien d'autre n'a changé ;
- il ne reste aucune voie par laquelle l'écart aux bornes (b1) et (b4) se dirait couvert sans un mot de Lazar qui le nomme ;
- le validateur rend une liste vide sur une copie remplie.

## Défaut par défaut

| défaut | état | preuve dans le brouillon 4 |
|---|---|---|
| A (moyen) | porté | Les cinq lieux sont corrigés. (1) En-tête, point (iv) : le point 10 de la fiche est cité, et « pour l'écart aux bornes (b1) et (b4), son mot est exigé (champ AD2-3) ». (2) « Borne du scellement » : « L'écart à leur lettre ne vaut que couvert par un mot de Lazar qui le nomme … il ne couvre donc pas cet écart ». (3) Cellule AD2-3 : « <mot de Lazar qui nomme cet écart : identifiant … et ses mots> ». (4) Alinéa des comptes : « il ne vaut que couvert par un mot de Lazar qui le nomme, cité au champ AD2-3 ». (5) Ligne 30 (a) : « écart … sans un mot de Lazar qui le nomme » interdit le scellement. Une recherche de « couvert », « accord nommé », « (b1) » et « (b4) » dans tout le texte ne trouve plus aucune autre voie. Le champ AD2-1, qui laisse la session mère dire « couverts » les quatre points de l'en-tête, ne l'ouvre pas : la cellule AD2-3 et la ligne 30 (a) exigent le mot de Lazar quoi que dise AD2-1 (remarque de forme 2) |
| B (mineur) | porté | « Borne du scellement » : « rédacteur non exposé au saboteur, qui a lu les comptes déclarés » ; « hors de la forme du fichier des identifiants et des valeurs de l'extrait du côté exposé (D-13 : chemins, empreintes, versions) » |
| C (mineur) | porté | Cellule AD2-3 : « « attesté » … seulement si les quatre exigences de l'additif 1 tiennent toutes — écrit par le développeur du côté des moniteurs, à partir de l'additif 1 seul, contre-lu par un autre modèle, corrections vérifiées par le même contre-lecteur ; sinon « non attesté » ». M-4 : « Si elle n'atteste pas ces quatre exigences, toutes (« non attesté ») ». Toute réponse partielle tombe dans la réécriture sous nom nouveau |
| forme, table des expositions | porté | ligne « rédacteur des brouillons 2, 3 et 4 … les deux rapports de la vérification des corrections (brouillons 2 et 3) » |
| forme, heures | porté | « brouillon 3 … vers 09:43Z ; brouillon 4 … vers 09:50Z ». Le fichier a été écrit à 09:48:08Z, ce que « vers » couvre |

## Défauts restants ou introduits

### À corriger avant le scellement (mineur, de lettre)

**D. Mineur — quatre phrases deviendraient fausses dans la version scellée.**

- **Lieux** :
  - ligne 3, « Statut : brouillon 4, non vérifié » et « ce brouillon 4 attend une vérification que la session mère décide, avant tout scellement » ;
  - table « Corrections de la vérification du brouillon 3 », « **Ces corrections ne sont pas vérifiées.** » ;
  - section « Contre-lecture », entrée « Vérification des corrections du brouillon 3 », « ces corrections ne sont pas vérifiées ».
- **Constat** :
  - Aucune de ces phrases n'est dans les quatre lieux que la session mère remplit.
  - La règle du scellement interdit de les changer ensuite (ligne 18 de l'additif 1, étendue).
  - Une fois l'entrée « Contre-lecture 2 » remplie par une vérification conforme, le texte scellé dirait à la fois que ses corrections sont vérifiées et qu'elles ne le sont pas.
- **Correction la plus petite**, à faire par un programme rejouable comme les précédents : écrire ces phrases au passé daté.
  - Statut : « brouillon 4 ; à son écriture, non vérifié : sa vérification est l'entrée « Contre-lecture 2 » ».
  - Dans les deux autres lieux : « à l'écriture du brouillon 4, ces corrections n'étaient pas vérifiées ; leur vérification est l'entrée « Contre-lecture 2 » ».
- **Autre voie** : ajouter ces trois lieux à la règle du scellement. Elle est plus lourde, puisqu'elle change la règle.

### Remarques de forme (n'empêchent pas le scellement)

1. **Deux mentions des brouillons 2 et 3, à compléter du brouillon 4.**
   - Ligne 13 : le titre de l'alinéa dit « Ce que les brouillons 2 et 3 changent après le mot de Lazar », alors que le point (iv) porte aussi l'ajout du brouillon 4 (point 10 de la fiche).
   - Alinéa des comptes, ligne 162, deux fois : « le rédacteur des brouillons 2 et 3 » ; la table des expositions dit, elle, « des brouillons 2, 3 et 4 ».
   - Correction : écrire « 2 à 4 ».
2. **Champ AD2-1 et écart aux bornes.** Le champ AD2-1 laisse la session mère dire « couverts » les quatre points de l'en-tête, dont le point (iv), qui comprend maintenant l'écart aux bornes. C'est sans effet, puisque la cellule AD2-3 et la ligne 30 (a) exigent le mot de Lazar. Pour la clarté, ajouter dans la cellule AD2-1 : « l'écart aux bornes (b1) et (b4) relève du champ AD2-3 ».

## Vérifications demandées

- **(a) Rejeu et différence**
  - Le programme, rejoué sur le brouillon 3 vers une cible de mon bloc-notes, rend `0d3f1adc…`, égal à l'octet au brouillon 4 (`cmp`).
  - La différence ligne à ligne compte douze blocs. Chacun vient d'une instruction du programme, que j'ai lu en entier : titre, statut, rédacteurs, date, point (iv) de l'en-tête, table des corrections neuve, « Borne du scellement », cellule AD2-3, ligne du rédacteur dans la table des expositions, alinéa des comptes, alinéa « Provenance » de M-4, ligne 30 (a), entrée de vérification et entrée « Contre-lecture 2 ».
  - Rien d'autre n'a changé.
- **(b)** Voir la table ci-dessus.
- **(c) Marqueur et validateur**
  - Le marqueur d'attente paraît aux seules lignes 132, 133 et 134 (cellules AD2-1, AD2-2 et AD2-3) et 331 (entrée « Contre-lecture 2 »).
  - Sur une copie hors du dépôt, une fois ces quatre lieux remplis et l'entrée finale à deux empreintes, `problemes` rend `[]`. Avec une seule empreinte, il rend « contre-lecture 2 sans ses deux empreintes ».
  - La nouvelle entrée « Vérification des corrections du brouillon 3 » ne gêne pas le validateur.
  - Les 59 fragments cités de la liste fermée se retrouvent toujours à l'identique dans le texte scellé ou dans l'additif 1.
- **(d) Ce qui ne bouge pas**
  - Aucune instruction ne touche une sonde, un seuil, une métrique, un état, la table des issues, l'audit ni les graines.
  - Une recherche par programme ne trouve dans le brouillon 4 aucun nom du code de la course, aucun compte de la note version 7 ni de la fiche, aucun montant et aucun chiffre de résultat.
- **(e) Cohérence interne**
  - Les quatre pièces de la condition D-14, la ligne 21, la ligne 30 (a), M-4 et la cellule AD2-3 sont cohérents entre eux.
  - La table des corrections de tête est fidèle au corps.
  - Seules les phrases du défaut D et les deux remarques de forme ne tiennent pas.
- **Non vérifié** : tout ce que mes deux premiers rapports déclaraient non vérifié (dont la ligne GO-2026-11-24-07 et l'auteur du programme de comparaison de version 1).
