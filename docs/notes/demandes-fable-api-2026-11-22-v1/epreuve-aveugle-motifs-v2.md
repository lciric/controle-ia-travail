# Épreuve aveugle de la règle de repérage des duels (correction 43), v2 — erratum de la v1

La v1 (`epreuve-aveugle-motifs-v1.md`) comptait la longueur du couple rendu par `duels` (toujours 2) au lieu du nombre de duels : erreur de la mère dans le harnais, relevée par Fable (relecture c1cebee3…). Rejeu correct, même règle (`epreuve_motifs_correction_28_v2.py`, d1caea7b…), mêmes textes (`textes-aveugles-epreuve-v1.json`) :

| Texte | Attendu | Obtenu | Bornes de la section (b) | Verdict |
|---|---|---|---|---|
| 1 | 3 | 5 | lignes 6 à 26 | échec |
| 2 | 3 | 4 | lignes 8 à 17 | échec |
| 3 | 2 | 0 | lignes 6 à 9 | échec |

**Échec : 0 sur 3.** Conclusion inchangée et renforcée : voie (b) de Fable (balises aux tours III.1 et III.3 pour l'avenir, description seule pour les dossiers déjà joués).
