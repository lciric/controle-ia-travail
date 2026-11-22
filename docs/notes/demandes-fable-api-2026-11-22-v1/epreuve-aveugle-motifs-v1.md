# Épreuve aveugle de la règle de repérage des duels (correction 43), v1

Trois textes synthétiques écrits par un agent neuf qui n'a lu que les consignes des tours III.1 et III.3 du collisionneur v8d (lignes 528 à 546), sans lire la correction 43 ni les pièces : `textes-aveugles-epreuve-v1.json`. Règle appliquée : fonction `duels` de `epreuve_motifs_correction_28_v2.py` (d1caea7b…), inchangée.

| Texte | Attendu | Obtenu | Verdict |
|---|---|---|---|
| 1 (puces, titres « Duel n », H_A et H_B sur la même puce au duel 3) | 3 | 2 | échec |
| 2 (tableau en H₁/H₂, troisième duel sur une ligne hors tableau) | 3 | 2 | échec |
| 3 (paragraphes, « hypothèse A / B », section (b) en fin de texte) | 2 | 2 | passe |

**Échec : 1 sur 3.** Les pièces de la comparaison essaim (v4) ne sont pas scellables en l'état (règle R5 : garde éprouvée sur cas sains). Retour à Fable.
