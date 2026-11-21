# Vérification du lot 3 v3 (requête et journal) du véhicule NA-1 — v1

Vérificateur du lot 3 du véhicule NA-1, modèle S. Pièce de travail (classe C). Processeur seul : aucun appel, aucune clé, aucune dépense, aucune écriture dans un dépôt. Données factices ; la liste réelle des noms refusés n'a été lue qu'en mémoire, par programme, et **aucun nom de cette liste n'est écrit dans cette pièce**.

## Verdict

**Conforme. Les lots 4 et 5 passent sur cette base** (lot 2 v5, lot 3 v3). La v3 ne change que des noms : aucune logique ne change. Une garde v4 est acceptée par `journaliser_envoi`, une garde v3 est refusée. Aucune copie de la liste réelle n'est dans le livrable. Une remarque d'hygiène, non bloquante, au § 5.

## 1. Empreintes

| pièce | sha256 | état |
|---|---|---|
| table du livrable | `1be0ffd48b8ade5f0accd106c9682c0b1e3db36bc208046ef66946598bbbed7f` | égale à l'annonce (`1be0ffd4…`) ; les 15 fichiers vérifiés OK |
| rapport v3 | `a778f8fa5d2ed290ecbafa91dff1da786d53bfc1d449b0f3df50c49349cc148e` | égal |
| différentiel v2 → v3 | `a00525e61b36574e2778ad4a13c205d84ff484130b40b4bf305603ce9d62063a` | égal |
| orchestrateur | commit `a41b7b50…` | copie neuve, sans `.git` |

## 2. Rejeu

Copie neuve ; paquet du lot 2 v5 appliqué par son programme, puis paquet du lot 3 v3 par le sien (`--lancer-essais`).

| | annoncé | rejoué |
|---|---|---|
| essais, en tout | 200 | **200 passés**, 0 sauté (sans aucune variable posée) |
| essais du lot 3 | 72 | 72 (200 − 128 du lot 2 v5) |
| mutations | 58 sur 58 tuées | **58 sur 58 tuées** ; témoin non muté passe ; témoin inerte survit |

## 3. Le différentiel ne contient que des noms

J'ai refait les `diff` moi-même, fichier par fichier, entre la v2 et la v3 :

- `requete_na_v2` → `requete_na_v3` : l'import `tirage_na_v3` devient `tirage_na_v4` ; `VERSION` ; trois noms de module dans la docstring et un paragraphe « v3 ». Aucune autre ligne.
- `journal_na_v2` → `journal_na_v3` : les imports `garde_motifs_na_v3` → `_v4` et `requete_na_v2` → `_v3` ; `VERSION` ; un message d'erreur qui nomme le module de la requête ; la docstring. Aucune autre ligne.
- `aides_na_lot3`, `test_na_*_requete`, `test_na_*_journal` : imports, docstrings, et le nom du programme d'aide joué dans un autre processus. Aucune ligne d'essai ajoutée, retirée ni changée.
- `mutations_na_lot3` : la liste des fichiers copiés (garde, tirage et aides en v4 ; requête et journal en v3), les chemins des essais et des modules visés, le nom du journal. Les 58 mutations et le témoin inerte n'ont aucune ligne de différence.
- Programme d'application : manifeste lu, essais joués, clé `dependances_lot_2_v5` et deux messages. Aucune autre ligne.

## 4. Garde v4 acceptée, garde v3 refusée

Sonde sur la copie, avec une garde v4 et une garde v3 construites sur la même liste d'essai :
- la garde v4 est acceptée ; `journaliser_envoi` rend un `EnvoiJournalise` dont la requête gardée est de la classe de `garde_motifs_na_v4` ; la chaîne ré-encodée est égale aux octets gardés ;
- la garde v3 est refusée (`LigneRefusee`, « la garde de motifs du lot 2 est exigée ») et rien n'est écrit au journal ;
- une requête de juge portant « graine⠀factice » avec U+2800 à la place de l'espace lève l'arrêt de la **v4** (famille « composition et tenue », rang 1) : la règle de la mère sur U+2800 est tenue de bout en bout par le lot 3 v3.

## 5. Aucune copie de la liste réelle dans le livrable

- L'arbre du paquet ne porte que six fichiers (deux modules, les aides, deux fichiers d'essais, le programme de mutations) et leurs compagnons : aucun fichier de noms, aucun dossier de liste. Les aides disent qu'aucune liste réelle n'est lue ni copiée.
- Balayage par programme de la liste réelle (en mémoire, comptes seuls) sur les 13 fichiers du livrable que j'ai balayés : **aucun nom en mot entier dans le code du paquet, les essais, le programme de mutations, le programme d'application, le manifeste, la sonde ni le journal des mutations**.
- Remarque d'hygiène, non bloquante : un seul nom (le rang 1, de six lettres) apparaît en mot entier, **uniquement comme segment du chemin du bloc-notes de la session**, dans trois fichiers qui recopient des chemins complets : le rapport (1 occurrence, ligne 67), le différentiel (16) et le journal des essais (73). Mon repérage donne, à chaque fois, le même contexte : un « / » avant, un « - » après, au sein d'un chemin. C'est la classe que le développeur du lot 2 v5 avait corrigée dans ses propres fichiers (chemins relatifs). Ce n'est pas une copie de la liste, rien n'en est servi ; à nettoyer en passant au prochain livrable, si la mère veut la même hygiène partout.

## 6. Ce que je n'ai pas fait

Je n'ai pas rejoué mes 38 mutations supplémentaires du lot 3 v1 ni les sondes de cette série : aucune ligne de logique n'a changé depuis la v2, et la v2 est vérifiée. Je n'ai pas ouvert le dossier de la v4 du lot 2 (qui contient une copie de la liste, selon son développeur).

— vérificateur du lot 3 du véhicule NA-1, modèle S
