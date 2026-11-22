# Épreuve des motifs de l'article 4 (correction 28), version 1

22 novembre 2026, Opus 5.5. Prescription : correction 28 de la relecture de Fable, `docs/notes/demandes-fable-api-2026-11-22-v1/relecture-pieces-essaim-v2/relecture-fable-api.md` (sha256 0cec14ce096574666db1c4b4368b6cf89d3f471e8e2d5c5aed29080c764ccb0f). Motifs éprouvés : article 4 de `pieces-comparaison-essaim-v3.md` (sha256 3931390197977729947f87cf66cd7ce8e388639f10de18692d618ed786886734), correction 27 comprise.

**Résultat : ÉCHOUE — 6 textes sur 10 au nombre de duels attendu.** Les quatre échecs sont exactement les quatre textes qui nomment H_A (ou H₁) plusieurs fois dans un même duel : chaque ligne qui contient H_A ouvre un duel. C'est l'échec que Fable annonçait. Les motifs de section (b) et de fin de section (titre de (c), ou fin de la cellule) ont rendu les bornes voulues dans les dix textes.

Suite, selon la correction 28 : les motifs ne sont pas scellables en l'état ; le motif de duel est à retoucher par quelqu'un qui a lu les consignes, puis l'épreuve est à rejouer. Opus 5.5 ne retouche aucun motif (règle GO-2026-11-21-84).

## Protocole

- Script : `docs/notes/demandes-fable-api-2026-11-22-v1/epreuve_motifs_correction_28_v1.py` (sha256 314c293c0efec278b14b4ad5e6a3715adbce4854958a7317fd3cd2faf80beaca), lancé par `python3 -I epreuve_motifs_correction_28_v1.py` (Python 3.13.18) ; code de sortie 1.
- Dix textes synthétiques, écrits d'après les seules consignes des tours III.1 et III.3 et le préambule (règle B4 : duel H_A contre H_B) de `docs/notes/collisionneur-v9/collisionneur_v9_v8d.py`. Aucune cellule ni aucune réponse de modèle lue. Les textes sont dans le script.
- Nombre de duels attendu fixé dans le script, avec chaque texte, avant la première exécution.
- Textes 3, 4, 5 et 10 (quatre, au moins trois exigés) : H_A ou H₁ nommée plusieurs fois dans un même duel (titre, hypothèse, issue ou contrôle ; en 10, duel rédigé en prose sur plusieurs lignes). Les autres couvrent : un duel par ligne, titres de duel sans H_A, titres en gras, titre « b) » nu, notation HA sans tiret bas, H_A nommée hors de la section (b) (en (a) au texte 9, en (c) au texte 7), section (b) sans section (c) (texte 6).
- Motifs appliqués tels qu'écrits : section (b) et (c) avec casse ignorée ; motif de duel `H_?A\b|H₁` sans drapeau de casse (l'article 4 n'en dit rien).

## Sorties (telles qu'imprimées)

~~~
texte  1 : attendu 2, obtenu 2, section (b) lignes (3, 7) : PASSE
texte  2 : attendu 3, obtenu 3, section (b) lignes (0, 13) : PASSE
texte  3 [plusieurs H_A par duel] : attendu 2, obtenu 6, section (b) lignes (0, 13) : ÉCHOUE
    ouverture : **Expérience 1 : H_A contre H_B**
    ouverture : - H_A : le saboteur réparti échappe au moniteur de transcription.
    ouverture : - Issue : un écart inférieur à 0,1 falsifie H_A.
    ouverture : **Expérience 2 : H_A contre H_B**
    ouverture : - H_A : la sonde ajoute du signal au moniteur de texte.
    ouverture : - Contrôle négatif : sonde sur couche aléatoire ; sous H_A, l'aire reste à 0,5.
texte  4 [plusieurs H_A par duel] : attendu 2, obtenu 5, section (b) lignes (4, 13) : ÉCHOUE
    ouverture : ### Duel 1 (corrigé) — H_A contre H_B
    ouverture : H_A : le moniteur garde sa puissance sous paraphrase.
    ouverture : Correction : banque d'évaluation séparée ; sous H_A, le taux reste au-dessus de 0,6.
    ouverture : ### Duel 2 (corrigé) — H_A contre H_B
    ouverture : H_A : la règle d'audit au hasard borne le dommage.
texte  5 [plusieurs H_A par duel] : attendu 2, obtenu 5, section (b) lignes (0, 8) : ÉCHOUE
    ouverture : - Expérience 1 : H₁ contre H₂.
    ouverture : - H₁ : le score de la sonde monte avec la dose de sabotage.
    ouverture : - Issue qui falsifie H₁ : pente nulle.
    ouverture : - Expérience 2 : H₁ contre H₂.
    ouverture : - H₁ : deux copies voient leurs scores monter ensemble.
texte  6 : attendu 1, obtenu 1, section (b) lignes (3, 7) : PASSE
texte  7 : attendu 2, obtenu 2, section (b) lignes (3, 7) : PASSE
texte  8 : attendu 2, obtenu 2, section (b) lignes (3, 7) : PASSE
texte  9 : attendu 3, obtenu 3, section (b) lignes (3, 8) : PASSE
texte 10 [plusieurs H_A par duel] : attendu 2, obtenu 4, section (b) lignes (0, 8) : ÉCHOUE
    ouverture : Expérience 1. On oppose H_A, selon laquelle le saboteur informé contourne la sonde,
    ouverture : et l'issue qui falsifie H_A est un taux supérieur à 0,5 sous attaque informée.
    ouverture : Expérience 2. On oppose H_A, selon laquelle l'audit au hasard borne le dommage,
    ouverture : à H_B, selon laquelle il ne le borne pas ; un dommage planté non vu falsifie H_A.
RÉSULTAT : ÉCHOUE (6/10 textes au nombre attendu)
~~~

## Remarques sans changement de texte

- Au texte 5, la notation H₁ échoue de la même façon que H_A.
- Les textes à une seule mention de H_A par duel passent tous, y compris H_A hors de la section (b) et section (b) close par la fin de la cellule.
