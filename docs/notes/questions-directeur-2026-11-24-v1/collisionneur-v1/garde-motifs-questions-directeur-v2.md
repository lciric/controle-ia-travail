# Garde de motifs sur la question neutre groupée v2 du collisionneur, dossier des questions du directeur du 24 novembre (v2)

- **Nature** : pièce de travail (classe C). Aucun appel à un modèle, aucune dépense. Non commité. La v1 de cette pièce et la question v1 restent inchangées.
- **Heure** : `2026-11-24T17:27:28Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, auteur de la v1, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`.
- **Origine des retouches** : `test-neutralite-devinette-questions-directeur-v1.md` (`ac815d42e8d17dd5257076cd74ba4600dc9f720e8522abdae9af4f4b712de338`), section 5, sur l'ordre de la mère.
- **Script** : `garde_motifs_questions_directeur_v2.py` (`94fb42f3ae0c6ed3df7b1f29fd81d5787d8862bc636a0dcbf5da0a795e9aceab`), copie de la v1 (`e13b9d4d…`) dont seuls changent la docstring et le fichier du bras principal ; code de sortie 0 ; sortie `garde-motifs-questions-directeur-v2-sortie.txt` (`afc47836e0e0af951da61f7a2e26675e2424a297fe0ae778bd1b5d460da953fd`). Moteur `collisionneur_v9_v8d.py` (`b7803838…`), même méthode qu'en v1 (invitations reconstruites en mémoire, aucune écriture sur disque).

## 1. Retouches de la v2 (seules différences avec la v1)

| Partie | v1 | v2 | Source |
|---|---|---|---|
| 1 | « et lesquelles ne doivent servir qu'à mesurer ; si les règles du cadre se contredisent, dis-le sans trancher » | « et si certaines ne doivent servir qu'à mesurer. Les règles du cadre peuvent-elles se contredire ? Si oui, dis-le sans trancher » | recommandée |
| 2 (d) | « L'usage possible dans le système (tri, exploration, ou mesure seulement rapportée) et le risque qu'un proposeur apprenne à gonfler la mesure » | « L'usage possible dans le système, s'il y en a un, et ce qui pourrait le fausser » | recommandée |
| 3, modèle | « y est le produit d'une probabilité de rencontre en surface et de l'exponentielle de la somme d'un terme de compatibilité de structure et d'un terme de champ » | « y dépend de trois termes, une probabilité de rencontre en surface, un terme de compatibilité de structure et un terme de champ, combinés de façon multiplicative et log-linéaire » | **obligatoire** |
| 3 (a) | « et où ce dictionnaire redonne le modèle existant sous un autre nom » | « et si, et où, ce dictionnaire redonne le modèle existant sous un autre nom, et où il s'en écarte » | **obligatoire** |
| 3 (c) | « À quelle condition une énergie d'activation serait identifiable, dans un corpus et dans le système d'idéation ; dans ce dernier, quels réglages, s'il y en a, joueraient les rôles de la cinétique » | « Ce qui, dans un corpus et dans le système d'idéation, permettrait ou empêcherait d'identifier chaque paramètre de la cinétique » | **obligatoire** |
| 4 | « Or beaucoup d'idées naissent d'une anomalie » | « On avance que beaucoup d'idées naissent d'une anomalie » | facultative, appliquée |
| 5 | liste de six familles donnée en exemples avant la demande ; « relations » en gras | « Propose d'abord tes propres familles » ; les six familles viennent ensuite, après les six points : « Puis seulement, dis lesquelles des familles suivantes recouvrent les tiennes, et lesquelles te semblent vides ou mal posées » ; plus de gras | recommandée |

Faits et question témoin : **inchangés** (admis à 0,35 et 0,30) ; la question témoin n'a pas de v2.

## 2. Pièces isolées

| Pièce | Octets | Caractères (`lire_entree`) | Mots | Empreinte | `motifs_trouves` (octets / `lire_entree`) |
|---|---:|---:|---:|---|---|
| `faits-neutres-questions-directeur-v1.md` | 3 333 | 3 235 | 563 | `7926025c…` | `[]` / `[]` |
| `question-neutre-groupee-questions-directeur-v2.md` | 9 314 | 8 980 | 1 489 | `11657f1835041b9b7a95815b4e08c726ab5da79de5e9042397bbeb58938ade6e` | `[]` / `[]` |
| `question-temoin-neutre-questions-directeur-v1.md` | 2 702 | 2 608 | 430 | `002e0df8…` | `[]` / `[]` |

## 3. Invitations assemblées du troisième étage

| Bras | Tour | Caractères par invitation (A, B, C) | `motifs_trouves` |
|---|---|---:|---|
| principal (v2) | III.1 conception | 14 932 | `[]` |
| principal (v2) | III.2 critique croisée | 15 203 | `[]` |
| principal (v2) | III.3 réponse | 15 204 | `[]` |
| témoin (v1) | III.1, III.2, III.3 | 8 560, 8 831, 8 832 | `[]` |

**Résultat : vide partout** (trois pièces, dix-huit invitations). Témoin positif : trois catégories prises sur trois ; la garde est vivante.

## 4. Suite

La v2 doit repasser **un test de devinette à l'aveugle par un lecteur neuf** : le vérificateur de la v1 n'est plus aveugle. Le partage des rôles reste le même qu'en v1 : texte d'Opus 5.5, non de Fable 5.2.
