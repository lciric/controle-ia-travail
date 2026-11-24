# Garde de motifs sur la question neutre groupée v4 du collisionneur, dossier des questions du directeur du 24 novembre (v4)

- **Nature** : pièce de travail (classe C). Aucun appel à un modèle, aucune dépense. Non commité. Les pièces v1 à v3 restent inchangées.
- **Heure** : `2026-11-24T17:39:25Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, auteur des v1 à v3, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`.
- **Origine des retouches** : `test-neutralite-devinette-questions-directeur-v3.md` (`2967c12976319dae62cd52d2aebcaf85117e501f164c38418c85ad2162d729a3`), partie 4 (échec à 0,52) et verdict (retouche facultative de la partie 2), sur l'ordre de la mère.
- **Script** : `garde_motifs_questions_directeur_v4.py` (`0249c127b06042354e5c5fa4376c2e92efbffd2d25cd13127ab5e8e76d8570ed`), copie de la v3 dont seuls changent la docstring et le fichier du bras principal ; code 0 ; sortie `garde-motifs-questions-directeur-v4-sortie.txt` (`29646de0b3d305d67a0b0cc1667abfa017172b942642ea766f17f1b2eebe62cc`).

## 1. Retouches de la v4 (seules différences avec la v3)

| Partie | v3 | v4 | Statut |
|---|---|---|---|
| 4 (d) | « puis compare au moins trois structures distinctes, dont un hypergraphe, dis si aucune ne l'emporte » | « puis compare au moins trois structures distinctes de ton choix (par exemple graphe typé multicouche, hypergraphe, base de faits logiques, programme ou système de réécriture), dis si aucune ne l'emporte » | obligatoire |
| 2 (b) | « Une définition de la « surprise retirée ailleurs » calculable avant toute épreuve, … » | « Face à l'hypothèse rivale selon laquelle la connectivité, la nouveauté de la paire ou la pertinence pour l'évaluateur suffisent à expliquer le fait 3 : une définition de la « surprise retirée ailleurs » calculable avant toute épreuve, … » (hypothèse rivale reprise du rapport) | facultative, appliquée |

Faits (v1) et question témoin (v2) : inchangés.

## 2. Pièces isolées

| Pièce | Octets | Caractères (`lire_entree`) | Mots | Empreinte | `motifs_trouves` (octets / `lire_entree`) |
|---|---:|---:|---:|---|---|
| `faits-neutres-questions-directeur-v1.md` | 3 333 | 3 235 | 563 | `7926025c…` | `[]` / `[]` |
| `question-neutre-groupee-questions-directeur-v4.md` | 9 462 | 9 127 | 1 523 | `13565a793ba307226b689aa4c142781bbdd0f2f4776b8fb0b815344456b97833` | `[]` / `[]` |
| `question-temoin-neutre-questions-directeur-v2.md` | 2 740 | 2 646 | 438 | `4a5a0aef…` | `[]` / `[]` |

La question v4 fait 1 523 mots, juste au-dessus de la cible « environ 1 500 » du mandat.

## 3. Invitations assemblées du troisième étage

| Bras | III.1 conception | III.2 critique croisée | III.3 réponse | `motifs_trouves` |
|---|---:|---:|---:|---|
| principal (v4), caractères par invitation | 15 079 | 15 350 | 15 351 | `[]` sur les neuf |
| témoin (v2), caractères par invitation | 8 598 | 8 869 | 8 870 | `[]` sur les neuf |

**Résultat : vide partout** (trois pièces, dix-huit invitations). Témoin positif : trois catégories sur trois.

## 4. Devis : rejoué

`verif_devis_questions_directeur_v4.py` (`af3999b559b06a648e9a0a8bcbf49813e4d93e8649057730ca52121096b504a2`), copie de la v3 dont seuls changent la docstring et le fichier du bras principal ; code 0 ; sortie `verif-devis-questions-directeur-v4-sortie.txt` (`21d49b65fb831833c598c91ebb30ab7b122a17a5ad5654af740b69dac0ac0c04`).

- **Jetons d'entrée du bras principal** : de +71 à +123 par cellule (par exemple III.3 réponse A : 52 573 → 52 696). Le bras témoin est inchangé.
- **Totaux qui changent d'un centime** (deux bras) :
  - option A : attendu avec pannes au taux prudent de Carbon, 11,38 → 11,39 ;
  - option B : attendu avec pannes, 14,55 → 14,56 ; haut à deux coupures, 23,72 → 23,73 ; pire avec toutes relances, 88,52 → 88,53.
- **Totaux inchangés** :
  - option A : 10,81 attendus avec pannes ; 23,87 au pire sans relance ; 71,61 avec toutes relances ;
  - option B : 32,33 au pire sans relance.
- **Pointes et plafonds inchangés** :
  - option A : pointe 10,81 en séquence, 14,94 en parallèle (bras principal) ; plafond de 16 par bras si l'envoi en séquence est attesté, sinon 20 ;
  - option B : pointe 12,80 en séquence, 14,94 en parallèle ; plafond de 18 par bras.
- Le devis v2 tient à un centime près sur trois totaux ; je ne l'ai pas réécrit.

## 5. Suite

La v4 doit repasser un test de devinette à l'aveugle par un **lecteur neuf**.
