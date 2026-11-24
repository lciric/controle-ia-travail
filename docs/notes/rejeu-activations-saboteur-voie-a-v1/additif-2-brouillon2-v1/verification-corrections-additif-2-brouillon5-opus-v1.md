# Vérification des corrections — additif 2 au texte de lecture des sondes sur les épisodes du saboteur à budget (barreau 8), brouillon 5 — v1

## En-tête

- **Relevés de l'heure (`date -u`), tels quels** : au début, `Tue Nov 24 09:52:53 UTC 2026` ; à la fin des vérifications par programme, `Tue Nov 24 09:53:37 UTC 2026` ; l'écriture de ce rapport suit.
- **Pièces vérifiées, empreintes recalculées (`sha256sum`), égales à leur compagnon :**
  - brouillon 5 `docs/notes/rejeu-activations-saboteur-voie-a-v1/additif-2-brouillon2-v1/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1-brouillon5.md` — `65b1af62d7437249b88dbb121c8ae1521a5f908d063b97dd3f82d3758746b2f5` (écrit sur disque à 09:52:39Z) ;
  - programme des corrections `…/corrections_brouillon4_vers_brouillon5_v1.py` — `bb9881f95c6d3e560139cf0131f980d6e11fafb408cf7fc4dbe8b8cea6853a62` ;
  - brouillon 4, même dossier — `0d3f1adc07e09e8cdce838a724569cd3f7db3a5c56008dc7dc1c48b960a5ab7e` ;
  - mon troisième rapport `…/verification-corrections-additif-2-brouillon4-opus-v1.md` — `51005045c19ccdf717250063d13576e04cd71a2d2a4ba3c40083c38706111a74` (c'est l'empreinte que cite le brouillon 5) ;
  - les autres pièces sont inchangées.
- **Qui je suis** : le même vérificateur que pour les brouillons 2, 3 et 4. Je suis un sous-agent neuf, modèle Claude Opus 5.5, du côté des moniteurs, non exposé au saboteur. Je n'ai écrit aucune pièce de l'additif 2 ni aucun programme des corrections ; je n'ai écrit que mes quatre rapports.
- **Déclaration de cloisonnement** :
  - Ce que j'ai lu en plus de mes listes précédentes : le programme des corrections du brouillon 4 au brouillon 5, en entier ; le brouillon 5, par sa différence au brouillon 4 et par une recherche dans tout le texte.
  - Ce que je n'ai pas ouvert : rien sous `runs/`, `diag/`, `donnees/`, `coffre/`, `docs/verdicts/`, `brouillons/` ou `registres/iib-*` ; aucune autre branche, aucun ordre, aucune sortie, aucun épisode, aucun score, aucune issue.
  - Je n'ai modifié aucun fichier existant. Le rejeu et les essais sont dans mon bloc-notes, hors du dépôt.

## Verdict

**À corriger, sur un seul point mineur de lettre** (défaut E), présent depuis le brouillon 2 et que je n'avais pas relevé dans mes trois vérifications précédentes. Une phrase de la section « Corrections de la contre-lecture R2 » deviendrait fausse dans la version scellée. La correction tient en une ligne.

Le reste est conforme :
- le défaut D et les deux remarques de forme sont portés ;
- le rejeu redonne le brouillon 5 à l'octet ;
- rien d'autre n'a changé ;
- hors de la phrase du défaut E, aucune phrase ne deviendrait fausse dans la version scellée ;
- sur une copie remplie, le validateur rend une liste vide.

## Défaut par défaut

| point | état | preuve dans le brouillon 5 |
|---|---|---|
| D (mineur) | porté | Statut : « Statut d'avant le scellement : brouillon 5, candidat final … la vérification de ce brouillon 5 … est consignée à l'entrée « Contre-lecture 2 » ». Table du brouillon 3 : « À l'écriture du brouillon 4, ces corrections n'étaient pas vérifiées ; leur vérification est celle du brouillon 4 (table suivante) ». Entrée « Vérification des corrections du brouillon 3 » : « à l'écriture du brouillon 4, ces corrections n'étaient pas vérifiées : leur vérification est l'entrée suivante ». Les mots « non vérifié », « pas vérifiées » et « attend une vérification » ne paraissent plus qu'au passé daté, ou entre guillemets dans la table des corrections |
| forme 1 | porté | « brouillons 2 à 5 » au titre de l'alinéa de la ligne 13, deux fois à l'alinéa des comptes (ligne 172) et à la ligne du rédacteur de la table des expositions (ligne 169), avec « les trois rapports de la vérification des corrections (brouillons 2, 3 et 4) ». La chaîne « brouillons 2 et 3 » ne paraît plus nulle part |
| forme 2 | porté | Cellule AD2-1 : « l'écart aux bornes (b1) et (b4), que nomme aussi le point (iv), ne se dit pas « couvert » ici : il relève du champ AD2-3 et du mot de Lazar que ce champ exige » |

## Défaut restant

**E. Mineur, de lettre — une phrase deviendrait fausse dans la version scellée.** Il empêche seulement un scellement à la lettre exacte, et se corrige en une ligne.

- **Lieu** : section « Corrections de la contre-lecture R2 (brouillon 1 → brouillon 2) », ligne 29 : « La table détaillée, avec les motifs, est livrée à part, à côté de ce brouillon. »
- **Constat** :
  - La version scellée sera `prereg/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1.md`.
  - La table détaillée reste dans `docs/notes/rejeu-activations-saboteur-voie-a-v1/additif-2-brouillon2-v1/`.
  - Une fois scellé, le texte ne serait plus un brouillon, et la table ne serait plus « à côté ».
  - La table n'est par ailleurs citée nulle part par son chemin ni par son empreinte.
  - La phrase est là depuis le brouillon 2 ; je ne l'avais pas relevée.
- **Correction la plus petite** : remplacer « à côté de ce brouillon » par « `docs/notes/rejeu-activations-saboteur-voie-a-v1/additif-2-brouillon2-v1/table-constats-corrections-additif-2-brouillon1-vers-brouillon2-v1.md` (`7bd96a0461d310093c08b872542c46a031d40c59e2ce6b58486431d32605d5ce`) ».

**Remarque, qui n'est pas un défaut** : l'en-tête dit « brouillon 5 écrit le même jour, vers 09:55Z ». Le fichier a été écrit à 09:52:39Z, par un programme qui porte cette heure en dur. « Vers » couvre l'écart, mais « vers 09:52Z » serait exact.

## Recherche des phrases qui deviendraient fausses (point (b))

Recherche dans tout le texte, par programme, des tournures d'état. Ont été cherchés : « non vérifi », « pas vérifi », « attend », « soumis », « candidat », « sera », « seront », « n'est pas encore », « à faire », « à venir », « ce brouillon », « à l'écriture », « à côté ». Chaque occurrence a été relue. Les quatre lieux remplis par la session mère sont hors de cette recherche. Toutes les autres occurrences tiennent dans la version scellée :

- **Daté ou marqué comme antérieur au scellement** :
  - le statut, « d'avant le scellement » ;
  - le registre propre « à l'écriture » ;
  - les quatre pièces de la condition D-14 « à l'écriture du brouillon 2 » ;
  - l'extrait « à l'écriture » ;
  - les deux phrases du défaut D.
- **Une règle ou un ordre, non un état** :
  - la règle du scellement ;
  - l'ordre des opérations ;
  - « Fichiers à donner explicitement au vérificateur » ;
  - « Ce qu'il doit éprouver en premier ».
- **Le vocabulaire des essais**, comme « attendu » ou « valeurs attendues ».

Seule la phrase du défaut E fait exception.

## Vérifications demandées

- **(a) Rejeu et différence** :
  - Le programme, rejoué sur le brouillon 4 vers une cible de mon bloc-notes, rend `65b1af62…`, égal à l'octet au brouillon 5 (`cmp`).
  - La différence ligne à ligne compte dix blocs. Chacun est produit par une instruction du programme, que j'ai lu en entier : titre, statut, rédacteurs, date, titre de l'alinéa de la ligne 13, phrase de la table du brouillon 3, table neuve « Corrections de la vérification du brouillon 4 », cellule AD2-1, ligne du rédacteur et alinéa des comptes dans « Expositions », entrée de vérification du brouillon 3, entrée neuve de vérification du brouillon 4 et entrée « Contre-lecture 2 ».
  - Rien d'autre n'a changé.
- **(d) Marqueur et validateur** :
  - Le marqueur d'attente paraît aux seules lignes 142, 143 et 144 (cellules AD2-1, AD2-2 et AD2-3) et 342 (entrée « Contre-lecture 2 »).
  - Sur une copie hors du dépôt, quatre lieux remplis et entrée finale à deux empreintes, `problemes` rend `[]`. Avec une seule empreinte, il rend « contre-lecture 2 sans ses deux empreintes ».
  - Les 59 fragments cités de la liste fermée se retrouvent toujours à l'identique.
- **(e) Ce qui ne bouge pas** :
  - Aucune instruction du programme ne touche une sonde, un seuil, une métrique, un état, la table des issues, l'audit ni les graines.
  - Une recherche par programme ne trouve aucun nom du code de la course, aucun compte de la note version 7 ni de la fiche de décision, aucun montant, aucun chiffre de résultat.
- **(f) Cohérence interne** :
  - Les tables des corrections de tête (quatre tables) sont fidèles au corps.
  - Les entrées de la section « Contre-lecture » s'enchaînent : contre-lecture 1, puis les vérifications des brouillons 2, 3 et 4, puis l'entrée « Contre-lecture 2 ».
  - Les cellules AD2-1 et AD2-3 et la ligne 30 (a) sont cohérentes sur l'écart aux bornes (b1) et (b4) : le mot de Lazar est exigé partout.
- **Non vérifié** : tout ce que mes rapports précédents déclaraient non vérifié, dont la ligne GO-2026-11-24-07 et l'auteur du programme de comparaison de version 1.
