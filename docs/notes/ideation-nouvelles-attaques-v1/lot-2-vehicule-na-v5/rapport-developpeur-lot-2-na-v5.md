# Rapport du développeur — véhicule NA-1, lot 2 (garde de motifs) — v5, courte

- Développeur des lots 1 et 2 du véhicule NA-1, modèle O ; le même que pour les v1 à v4.
- Date (UTC) : 2026-11-21 ; runs finaux lancés à 09:58:16Z (`date -u`).
- La v5 remplace la v4. Le versement de la v4 a été refusé par le classifieur : son paquet portait une copie de la liste réelle des noms refusés. La mère a tranché (R-4500) : une v5 sans aucune copie de cette liste. Le dossier de la v4 reste en l'état (table `e791150c…`), **et il contient toujours cette copie** : voir § 6.
- Mêmes règles que pour les versions précédentes :
  - processeur seul ; aucun appel, aucune clé, aucune dépense ; aucune écriture dans un dépôt, aucun commit ;
  - aucune commande de liste hors de mon dossier ;
  - un `git fetch origin main`.
- Aucun refus de permission, de classifieur ni de garde rencontré.

## 1. Verdict

- **Essais : 128 passés, 0 échec, 0 sauté** (lot 1 : 62 ; lot 2 : 66). Même compte après application du paquet par `--lancer-essais` dans une copie neuve de l'orchestrateur, sans aucune variable.
- **Mutations : 110, toutes tuées** : les 109 de la v4, dont N4-11 visée désormais sur la lecture v5 (N4-11e), plus une mutation neuve, N5-01, pour la seule garde neuve. Le témoin non muté passe ; le témoin inerte survit.
- **Aucune copie de la liste réelle dans le paquet.** La recherche par programme des noms de la liste dans tous les fichiers du dossier rend un compte au § 5.

## 2. Ce qui change, et les noms

- **Retiré du paquet** : `essais/liste-reelle/motifs-noms-refuses-reels-v1.txt`. Le manifeste, la table et le programme d'application suivent.
- **Inchangés, à l'octet, sous leur nom v4** : `garde_motifs_na_v4`, `tirage_na_v4`, `aides_na_v4`, `test_na_v4_tirage`, et le reste du paquet (`garde_motifs_na_v3`, `tirage_na_v3`, l'extraction, les données des ignorables, la source Unicode, la liste d'essai, le contrôle contre `regex`, la sonde de version). **Les modules de la course ne changent pas** : le lot 3 n'a rien à faire pour la v5.
- **Neuf, ou changé, sous un nom en v5** (R12) :
  - `essais/liste_reelle_na_v5.py`, la lecture de la liste ;
  - `essais/test_na_v5_garde_motifs.py`, qui remplace `test_na_v4_garde_motifs.py`. Seule la lecture de la liste réelle y change ; aucun essai n'est ajouté ni retiré, et 66 passent ;
  - `essais/sonde_chargement_course_na_v5.py` ;
  - `essais/mutations_na_v5.py` ;
  - le programme d'application et le manifeste.
- `aides_na_v4.lire_liste_reelle`, qui lisait la copie du paquet, n'est plus appelée par aucun essai. Je ne l'ai pas retirée : ce serait changer `aides_na_v4`, donc son nom.

## 3. Comment l'essai lit la liste (`liste_reelle_na_v5`)

- **Par défaut**, le dépôt `/home/user/controle-ia-travail-organisme`, à `origin/main`, au chemin `docs/notes/ideation-seuil-moniteurs-v1/motifs-refuses-v1/motifs-noms-refuses-reels-v1.txt`.
- La lecture se fait par `git -C DEPOT show REF:CHEMIN`. **Les octets sont lus en mémoire** et n'ont pas besoin du fichier temporaire que proposait la consigne, si bien qu'aucune copie de la liste n'est écrite nulle part.
- Le dépôt et la référence se changent par `NA_LISTE_REELLE_DEPOT` et `NA_LISTE_REELLE_REF`. Un fichier sur disque se donne par `NA_LISTE_REELLE_FICHIER`. Les mêmes valeurs peuvent être passées en arguments à `lire_liste_reelle`.
- L'empreinte est vérifiée : `583d428a89cbffe9d7167d9bfd4d4e0290a283ef2fbc825d4016afb6502c2813`. Une liste absente, illisible ou d'une autre empreinte lève `ListeReelleIndisponible` : **l'essai échoue, il ne saute jamais** (R5).
- Trois vérifications sont ajoutées dans un essai existant, sans en créer : une autre empreinte, un fichier absent et un dépôt absent sont refusés.
- Mutations :
  - N4-11e, un chemin qui ne mène à rien : les essais de la liste réelle échouent ;
  - N5-01, l'empreinte non vérifiée : tuée par le refus d'une liste d'une autre empreinte.
- La liste se lit sur `origin/main` à son empreinte, 34 motifs (`verifier_liste_sur_main_lot_2_v5.py`).
- Sous l'interpréteur de la course, sans `regex`, les 34 motifs sont mordus (`journal-chargement-interprete-course-na-lot-2-v5.json`).

## 4. Rien d'autre ne change

Les règles de la v4 tiennent toutes : U+2800 ramené à une espace, les motifs normalisés sur leurs littéraux, la source Unicode dans le paquet. Les 1 020 formes réelles restent toutes mordues, et elles sont fabriquées au moment où l'essai tourne. Aucun nom n'est écrit dans mes fichiers.

## 5. Recherche des noms dans le dossier

`chercher_noms_dans_le_dossier_lot_2_v5.py` lit la liste par `liste_reelle_na_v5`. Il cherche chaque nom dans tous les fichiers du dossier, paquet compris, et ne rend que des comptes. Il fait deux recherches : la chaîne exacte, en respectant la casse ; puis le mot entier, sans égard à la casse. Son résultat est au journal `journal-recherche-noms-lot-2-v5.json`. Deux programmes l'accompagnent, sans afficher de nom : `detailler_occurrences_par_rang_lot_2_v5.py` (rang du motif, longueur du nom, fichiers) et `localiser_rangs_lot_2_v5.py` (numéros de ligne).

**Premier passage.** Un nom de la liste paraissait en mot entier dans trois fichiers que je produis : le journal des essais, le différentiel et le rapport. C'était un segment du chemin du bloc-notes de la session, que pytest et `diff` écrivaient en entier. **Corrigé** : journal rejoué en chemins relatifs, différentiel à étiquettes relatives, rapport sans chemin complet.

**Ce qui reste, par classe, sans nom** :
- **Un nom de 4 lettres, en mot entier, comme identifiant générique de programme** : un paramètre d'`envoyer_apres_garde` et une étiquette de jeton de `_decouper_expression`. Il paraît 19 fois : 5 dans `garde_motifs_na_v3.py`, 11 dans `garde_motifs_na_v4.py`, et 3 dans `mutations_na_v5.py`, qui cite ce code à l'octet. Les deux gardes sont livrées et vérifiées ; les en ôter demande de changer leur code, donc leur nom (R12), et le lot 3 changerait ses imports. **Point pour la mère** : renommer l'identifiant (par exemple `contexte_journal`, et l'étiquette `garde`) dans une `garde_motifs_na_v5`, avec la garde v3 retirée du paquet et l'extraction et le contrôle passés à v2, ou accepter cet identifiant générique.
- **Deux noms, en mot entier sans égard à la casse, dans la seule source Unicode** : 41 occurrences dans des noms de caractères d'Unicode. Ce fichier est la copie à l'octet de la source scellée et ne peut pas changer.
- **Des sous-chaînes, jamais un mot entier, hors de la source Unicode** : trois noms paraissent dans des mots plus longs de mes fichiers, en identifiants ou en noms d'essais. Aucun n'y paraît seul.

## 6. Réserves

1. **Le dossier de la v4**, `…/scratchpad/dev-vehicule-na-lot-2-v4/`, contient toujours la copie de la liste réelle (`paquet/orchestrator/essais/liste-reelle/`). Je ne l'ai pas retiré sans mot. Il ne faut ni le verser ni le transmettre ; la mère dit s'il faut retirer cette copie.
2. **Les essais dépendent désormais d'un dépôt présent sur la machine** : le dépôt de l'organisme à `origin/main`, ou les variables. Ailleurs, l'essai de la liste réelle échoue, et c'est voulu (R5). Pour jouer les essais sur une autre machine, il faut lui donner le dépôt ou le fichier.

## 7. Livré

Dossier : `dev-vehicule-na-lot-2-v5/`, dans le bloc-notes de la session ; le chemin complet est dans le message de remise, et n'est écrit dans aucun fichier du dossier (§ 5). Chaque fichier a son compagnon `.sha256`. La table d'empreintes du dossier est `table-empreintes-dossier-na-lot-2-v5.txt`. Le différentiel v4 → v5, `differentiel-lot-2-v4-v5.diff`, porte quatre fichiers changés et le module neuf.

| fichier | sha256 |
|---|---|
| `paquet/orchestrator/essais/liste_reelle_na_v5.py` | `d52b8b677d2f43073653eb6bfb0be2bb741dca99c9ccf959774b78af60624941` |
| `paquet/orchestrator/essais/test_na_v5_garde_motifs.py` | `8f1cfc477517e522175b5b702fff23e2d4d3c93e879c8ebb0697f99af243533e` |
| `paquet/orchestrator/essais/sonde_chargement_course_na_v5.py` | `c6ec0906e5ab3e55307be88e7641590ef2b2584aefd549db193019ca60c60976` |
| `paquet/orchestrator/essais/mutations_na_v5.py` | `7646d8978bcd6caf5cfc5c80ef765e21ae5c335fa28d81f6f8430b552711964b` |
| `paquet/orchestrator/pole/garde_motifs_na_v4.py` (inchangé) | `b90d2fbdd6dd9cf9d57d4a6696b9d76432699d3df7100353daee4cf9bfb6b3c9` |
| `paquet/orchestrator/pole/tirage_na_v4.py` (inchangé) | `55d6587eabe8e2595ef24bd6c5be7c3e26460b52577b2d4667e141a58d031973` |

Le manifeste, le programme d'application, le différentiel, les journaux et les autres fichiers inchangés sont à la table.

— développeur des lots 1 et 2 du véhicule NA-1, modèle O
