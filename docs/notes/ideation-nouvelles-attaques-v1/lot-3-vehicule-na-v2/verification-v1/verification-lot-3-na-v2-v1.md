# Vérification du lot 3 v2 (requête et journal) du véhicule NA-1 — v1

Vérificateur du lot 3 du véhicule NA-1, modèle S. Pièce de travail (classe C). Processeur seul : aucun appel, aucune clé, aucune dépense, aucune écriture dans un dépôt. Données factices seules.

## Verdict

**Conforme. Les lots 4 et 5 peuvent partir**, sur les lots 1 et 2 v3 (garde v3) et ce lot 3 v2. La v2 ne change que des noms, des docstrings, la liste des fichiers copiés et la clé de dépendance : aucune logique ne change. Une v3 du journal n'est pas à faire avant le lot 4 : le mandat du lot 4 peut attraper `OSError` (§ 4).

## 1. Empreintes

| pièce | sha256 | état |
|---|---|---|
| table du livrable | `672f76acf3e633495b39f40ecfa8e1adb8a1cadc3e893e5b0fedfdc2cfd9c38d` | égale à l'annonce ; les 15 fichiers vérifiés OK |
| rapport v2 | `f9e72b34a0cc8e192ba2c7c906f6821bda4651b4f1543c8400b4d374c90fe266` | égal |
| différentiel v1 → v2 | `bb6c8fbc57c8482cd1966fa873f6e7260be828d2899cdf51ea9364a9a6ed0c06` | égal |
| orchestrateur | commit `a41b7b50…` | copie neuve, sans `.git` |

## 2. Rejeu

Copie neuve ; paquet v3 du lot 2 appliqué par son programme, puis paquet v2 du lot 3 par le sien (`--lancer-essais`).

| | annoncé | rejoué |
|---|---|---|
| essais, en tout | 189 passés, 1 sauté | **189 passés, 1 sauté** |
| essais du lot 3 seuls | 72 (requête 44, journal 28) | **72 passés** |
| mutations | 58 sur 58 tuées | **58 sur 58 tuées** ; témoin non muté passe ; témoin inerte survit |

L'essai sauté est `test_extraction_reelle_rejouee_egale_a_l_octet` du lot 2 v3 : le défaut relevé dans ma vérification du lot 2 v3 (essai sauté sans la variable `NA_SOURCE_UNICODE_15_1_0`), que la v4 corrige. Il ne touche pas le lot 3.

## 3. Le différentiel ne touche-t-il que des noms ? Oui

J'ai refait les différences moi-même, fichier par fichier, sans m'appuyer sur le fichier de différentiel du développeur.

- `requete_na_v1` → `requete_na_v2` : l'import `tirage_na_v2` devient `tirage_na_v3` ; `VERSION` ; deux noms de module dans la docstring ; un paragraphe « v2 ». Aucune autre ligne ne change.
- `journal_na_v1` → `journal_na_v2` : les imports `garde_motifs_na_v2` → `…_v3` et `requete_na_v1` → `requete_na_v2` ; `VERSION` ; un message d'erreur qui nomme le module de la requête ; la docstring. Aucune autre ligne ne change.
- `aides_na_lot3`, `test_na_*_requete`, `test_na_*_journal` : imports et docstrings ; le nom du programme d'aide joué dans un autre processus. Aucun essai ajouté, retiré ni changé (le `diff` ne montre aucune ligne d'essai).
- `mutations_na_lot3` : liste des fichiers copiés (noms v3 du lot 2 et v2 du lot 3, plus les données des ignorables et leur programme d'extraction), chemins des essais et des modules visés, nom du journal. Les 58 mutations et le témoin inerte n'ont aucune ligne de différence.
- Programme d'application : manifeste lu, essais joués, clé `dependances_lots_1_et_2` devenue `dependances_lot_2_v3`, deux messages. Aucune autre ligne.

Sonde sur la garde : une garde v3 est acceptée par `journaliser_envoi` et passe l'égalité ; une garde v2 est refusée (`LigneRefusee`). Le développeur le dit et note qu'aucun essai ne le tient à part ; c'est la mutation L3-46 et `test_garde_du_lot_2_exigee` qui tiennent le contrôle de type. Non bloquant.

## 4. Constat mineur du journal : une v3 avant le lot 4 ou non ?

**Non : pas de v3 du journal avant le lot 4. Le mandat du lot 4 attrape `OSError` à côté de `JournalRefuse`.**

Sondes sur la v2 :
- fichier de journal supprimé : `FileNotFoundError` (`OSError`, pas `JournalRefuse`) ;
- fichier remplacé par un dossier : `IsADirectoryError` (`OSError`) ;
- écriture qui échoue (disque plein simulé) : `OSError`. Aucun octet n'est écrit, l'état du journal reste cohérent, et l'ajout suivant réussit.

Dans tous les cas, l'exception remonte avant que rien ne parte : la garantie « un appel sans ligne ne part pas » tient. Seule la classe de l'exception diffère.

Raisons de ne pas bloquer :
- Toutes les pannes de fichier sont des `OSError` ; une clause `except (JournalRefuse, OSError)` les rattrape toutes, sans trou.
- Une v3 du journal ne change pas ce que le lot 4 doit faire d'une panne : l'arrêter.
- Une version de plus du journal est mieux employée si elle rassemble ce qui manque (§ 5). Reporter ce constat, avec les lignes d'arrêt et de génération, à une v3 groupée avant les lots 6 et 7.

À écrire au mandat du lot 4 (erratum 2) : toute `JournalRefuse` ou `OSError` levée par le journal à l'envoi est un refus « rien ne part », sans coût ; et, comme l'état du journal reste utilisable après une panne d'écriture, c'est le lot 4 qui décide d'arrêter la course (on ne continue pas sans journal). À dire : l'arrêt qui la porte.

## 5. Ce qui reste pour une v3 groupée du journal (avant le lot 6)

Mes deux ajouts du § 4 de ma vérification du lot 3 v1 tiennent :
- l'égalité refusée après la ligne « envoi » ;
- l'absence de ligne d'arrêt générale et de « ligne de la génération » (`EVENEMENTS` est fermé à quatre événements).

S'y ajoute le constat ci-dessus (conversion des `OSError`).

## 6. Note : la v4 du lot 2

La v4 ramène U+2800 à une espace et normalise les motifs, sans changer les noms de modules. Le lot 3 v2 n'importe que des noms (`garde_motifs_na_v3` : `GardeMotifs`, `RequeteGardee`, `ArretMotifInterdit`, `NUMERO_ARRET`, `verifier_avant_envoi`) : il devrait passer tel quel. À confirmer sur la v4 livrée.

Un point de la v2 à porter à l'additif : la garde v3 lit les clés de la fiche servie comme des mots séparés d'espaces (le rapport le dit, § 6). Un motif littéral fait de mots pourrait mordre sur un nom de champ ; la liste réelle doit être jouée sur les requêtes du portier et des juges avant le départ.

## 7. Ce que je n'ai pas fait

Je n'ai pas rejoué mes 38 mutations supplémentaires du lot 3 v1 : aucune ligne de logique n'a changé. Je n'ai pas relu la v4 du lot 2, pas encore livrée.

— vérificateur du lot 3 du véhicule NA-1, modèle S
