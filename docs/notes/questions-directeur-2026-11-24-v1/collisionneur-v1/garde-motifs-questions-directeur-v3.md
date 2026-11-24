# Garde de motifs sur la question neutre groupée v3 et la question témoin v2 du collisionneur, dossier des questions du directeur du 24 novembre (v3)

- **Nature** : pièce de travail (classe C). Aucun appel à un modèle, aucune dépense. Non commité. Les pièces v1 et v2 restent inchangées.
- **Heure** : `2026-11-24T17:34:26Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, auteur des v1 et v2, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`.
- **Origine des retouches** : `test-neutralite-devinette-questions-directeur-v2.md` (`c58a7e75f9dd9eeb92e8671402a60158df9c55c347fd3e50705723679969cc01`), section « Fuite de conclusion constatée », sur l'ordre de la mère.
- **Script** : `garde_motifs_questions_directeur_v3.py` (`7bba6af0220342c95d8b783a5a1d08b06a7788677cc32a354f224f674db4e5c7`), copie de la v2 (`94fb42f3…`) dont seuls changent la docstring et les deux fichiers de question ; code 0 ; sortie `garde-motifs-questions-directeur-v3-sortie.txt` (`e7ec6b96ff2dff3dc6717861fb271e52ca54c30fc8b2fc31c14e20c1c02ec241`). Moteur `collisionneur_v9_v8d.py` (`b7803838…`), même méthode (invitations reconstruites en mémoire, aucune écriture sur disque).

## 1. Retouches de la v3 (seules différences avec la v2 de la question groupée)

| Partie | v2 | v3 | Statut au rapport |
|---|---|---|---|
| 1 | « Dis lesquelles de leurs sorties pourraient légitimement servir à choisir une configuration du système, et si certaines ne doivent servir qu'à mesurer. Les règles du cadre peuvent-elles se contredire ? Si oui, dis-le sans trancher. » | dans la liste « Pour chacune » : « et si sa sortie peut servir à choisir une configuration du système, seulement à mesurer, ou à rien. Dis si les règles du cadre se contredisent ou non, et où. » | obligatoire |
| 2 | « …qu'elle leur apporte, pondérée par leur centralité » ; « et le rôle de la pondération » | « …qu'elle leur apporte » ; « et le rôle d'une pondération éventuelle » | facultative, appliquée |
| 3, modèle | « y dépend de trois termes, une probabilité de rencontre en surface, un terme de compatibilité de structure et un terme de champ, combinés de façon multiplicative et log-linéaire » | « Un modèle formel du taux de naissance d'un lien entre deux concepts existe déjà ; il fait intervenir la structure du graphe, la proximité en surface et un terme de champ » (ni ordre de la cinétique, ni forme de combinaison) | obligatoire |
| 3 (a) | « et si, et où, ce dictionnaire redonne le modèle existant sous un autre nom, et où il s'en écarte » | « puis ce que ce dictionnaire partage avec le modèle existant et ce qu'il y ajoute, terme par terme » | obligatoire |
| 3 (d) | « garder, garder en partie ou écarter » | « écarter, garder en partie ou garder » | obligatoire |
| 4 | « et de représenter l'ensemble par un hypergraphe » | « et de choisir une structure de représentation pour l'ensemble » | obligatoire |
| 4 (c) | « Comment la couche entre dans le taux… et quelle prédiction elle ajoute » | « Si et comment la couche entre dans le taux… et quelle prédiction elle ajouterait au modèle des mariages, s'il y en a » | obligatoire |
| 4 (d) | « compare au moins deux structures distinctes, l'hypergraphe compris » | « compare au moins trois structures distinctes, dont un hypergraphe, dis si aucune ne l'emporte » | obligatoire |

**Question témoin v2** (`question-temoin-neutre-questions-directeur-v2.md`), facultative, appliquée : piste 3, « Qu'est-ce que cela ajouterait de mesurable, s'il y a quelque chose ? » ; piste 4, « On avance que beaucoup d'idées naissent d'une anomalie… ». Faits : inchangés (v1).

## 2. Pièces isolées

| Pièce | Octets | Caractères (`lire_entree`) | Mots | Empreinte | `motifs_trouves` (octets / `lire_entree`) |
|---|---:|---:|---:|---|---|
| `faits-neutres-questions-directeur-v1.md` | 3 333 | 3 235 | 563 | `7926025c…` | `[]` / `[]` |
| `question-neutre-groupee-questions-directeur-v3.md` | 9 197 | 8 872 | 1 483 | `0234875fe2df92cd42f11cecaa4ee3528ef707ab63d9fea7c220092c6910ef89` | `[]` / `[]` |
| `question-temoin-neutre-questions-directeur-v2.md` | 2 740 | 2 646 | 438 | `4a5a0aef549169a05d8086ed9863a2e3314486b3d5a97afbccc7fd339af4616d` | `[]` / `[]` |

## 3. Invitations assemblées du troisième étage

| Bras | III.1 conception | III.2 critique croisée | III.3 réponse | `motifs_trouves` |
|---|---:|---:|---:|---|
| principal (v3), caractères par invitation | 14 824 | 15 095 | 15 096 | `[]` sur les neuf |
| témoin (v2), caractères par invitation | 8 598 | 8 869 | 8 870 | `[]` sur les neuf |

**Résultat : vide partout** (trois pièces, dix-huit invitations). Témoin positif : trois catégories sur trois ; la garde est vivante.

## 4. Devis : rejoué, non réécrit

`verif_devis_questions_directeur_v3.py` (`aa2cf1030fa4d7442a492c71140a227cb0262e2be653050484a968721582d4f2`), copie de la v2 dont seuls changent la docstring et les deux fichiers de question ; code 0 ; sortie `verif-devis-questions-directeur-v3-sortie.txt` (`3c1de7d9340cfb03a1b06833a621bd9cf56abbe0b446e09ca06a99fd3e37f607`).

- **Les jetons d'entrée changent un peu** : de −30 à −52 par cellule au bras principal (par exemple III.3 réponse A : 52 625 → 52 573), de +10 à +18 au bras témoin.
- **Les totaux ne changent pas au centime**, sauf le pire avec toutes relances de l'option B : 88,53 → 88,52. Option A : 10,81 attendus avec pannes, 23,87 au pire sans relance, 71,61 avec relances. Option B : 14,55, 32,33 et 88,52. Information : 11,38 et 15,13 au taux de panne prudent de Carbon ; 8,37 et 12,12 au barème de Carbon facturé jusqu'au 30 novembre.
- **Pointes et plafonds inchangés** : en séquence, 10,81 et 10,75 (A), 12,80 et 12,70 (B) ; en parallèle, 14,93 et 14,86 (A), 14,94 et 14,85 (B). D'où les plafonds : A, 16 par bras si l'envoi en séquence est attesté, sinon 20 ; B, 18.
- **Le devis v2 tient** (`devis-collisionneur-questions-directeur-v2.md`) ; je ne l'ai pas réécrit. Seuls les noms des fichiers d'entrée et les comptes de jetons du § 4 sont à lire dans la sortie v3. Si la mère veut une pièce de classe A qui porte la v3, un devis v3 se tire de cette sortie sans autre calcul.

## 5. Suite

La v3 et la question témoin v2 doivent repasser un test de devinette à l'aveugle par un **lecteur neuf**, puis la vérification du devis (rejeu du script v3).
