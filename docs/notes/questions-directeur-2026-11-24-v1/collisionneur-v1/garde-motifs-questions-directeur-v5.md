# Garde de motifs sur la question neutre groupée v5 du collisionneur, dossier des questions du directeur du 24 novembre (v5)

- **Nature** : pièce de travail (classe C). Aucun appel à un modèle, aucune dépense. Non commité. Les pièces v1 à v4 restent inchangées.
- **Heure** : `2026-11-24T17:44:17Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, auteur des v1 à v4, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`.
- **Origine** : `test-neutralite-devinette-questions-directeur-v4.md` (`072ed3241d73b2aaf54652ad246629b5340be6a37006cfef47b148bbf2a86869`), partie 3 (échec à 0,50), sur l'ordre de la mère.
- **Script** : `garde_motifs_questions_directeur_v5.py` (`bdc76b4d0c641b5277b1fadc38f834111c190c2bfa30dad3b51795ec406d3ac2`), copie de la v4 dont seuls changent la docstring et le fichier du bras principal ; code 0 ; sortie `garde-motifs-questions-directeur-v5-sortie.txt` (`960948117cdafe44e02de6cc3961c340ec26d9d37501d668ab3200036c0e1f69`).

## 1. Retouches de la v5 (partie 3 seulement)

| v4 | v5 |
|---|---|
| « il fait intervenir la structure du graphe, la proximité en surface et un terme de champ » | « il fait intervenir la structure du graphe, la proximité en surface et un terme propre à la paire » |
| « (b) Les prédictions que la cinétique ferait » | « (b) Les prédictions, s'il y en a, que la cinétique ferait » |

Rien d'autre ; faits (v1) et question témoin (v2) inchangés.

## 2. Résultat

- `question-neutre-groupee-questions-directeur-v5.md` : 9 486 octets, 9 150 caractères, 1 529 mots, `6b3f041923e802a9212c0aeb23a6bb89b7d855f1c280fb0faff08db1f3bb4110` ; `motifs_trouves` vide (octets et `lire_entree`).
- Faits v1 et question témoin v2 : vides, comme en v4.
- Invitations du troisième étage : principal 15 102, 15 373 et 15 374 caractères ; témoin 8 598, 8 869 et 8 870 ; **`[]` sur les dix-huit**. Témoin positif : trois catégories sur trois.

## 3. Devis : rejoué

`verif_devis_questions_directeur_v5.py` (`6db299897a3bf37354cfa6441ffef099b0511b397a922c6f2aea1e230a2dbc0e`) ; code 0 ; sortie `verif-devis-questions-directeur-v5-sortie.txt` (`c9cc34a49435ca15eab41507cdb6185bbaf8c647259d2473d2411d83e752e959`).

- **Entrée** : quelques jetons de plus par cellule au bras principal (par exemple III.3 réponse A, 52 696 → 52 707).
- **Totaux des deux bras identiques à la v4, au centime** :
  - option A : 10,81 attendus avec pannes ; 23,87 au pire sans relance ;
  - option B : 14,56 attendus avec pannes ; 32,33 au pire sans relance.
- **Plafonds inchangés** : option A, 16 par bras si l'envoi en séquence est attesté, sinon 20 ; option B, 18 par bras.

La v5 doit repasser un test de devinette par un **lecteur neuf**.
