# Épreuve des motifs de l'article 4, version 2 (règle de duel de la correction 43)

22 novembre 2026, Opus 5.5. Prescription : correction 43 de la relecture de Fable, `docs/notes/demandes-fable-api-2026-11-22-v1/relecture-pieces-essaim-v3/relecture-fable-api.md` (sha256 44b7d86efd2f55f32e77b3da0137525a133ab034306e60197ac809c4349dc201), point « Suite » 2 : mêmes dix textes, mêmes nombres attendus, 10 sur 10 exigé. Motifs éprouvés : article 4 de `pieces-comparaison-essaim-v4.md` (sha256 48caa135c62e82b50f27fd698a37f5d2554163e6af9a3a97d887f2a1dc510ab3).

**Résultat : PASSE — 10 textes sur 10 au nombre de duels attendu.** Les quatre textes qui échouaient en version 1 (3, 4, 5 et 10, plusieurs H_A ou H₁ par duel) passent ; les six autres passent toujours, avec les mêmes bornes de section (b).

## Protocole

- Script : `docs/notes/demandes-fable-api-2026-11-22-v1/epreuve_motifs_correction_28_v2.py` (sha256 d1caea7bdaa66ef2b18fdcf1b23b8d84a8c1d5b872fc52d4de637949e0d5d1ac), lancé par `python3 -I epreuve_motifs_correction_28_v2.py` (Python 3.13.18) ; code de sortie 0.
- Copie de la version 1 (`epreuve_motifs_correction_28_v1.py`, sha256 314c293c0efec278b14b4ad5e6a3715adbce4854958a7317fd3cd2faf80beaca). Seuls changements : `MOTIF_DUEL` remplacé par le bloc de code de la correction 43 (`HA`, `HB`, `MOTIF_A`, `MOTIF_A_OU_B`, `MOTIF_OPPOSITION`, `ouvertures_duels`), copié tel quel, casse respectée pour A et B ; la ligne `ouvertures = …` de `duels()` devient `ouvertures = ouvertures_duels(section)` ; la docstring dit la version et la source. Motifs de section (b) et (c) inchangés, casse ignorée.
- Dix textes et nombres attendus inchangés : la partie du script de `TEXTES = [` à la fin a la même empreinte dans les deux versions (sha256 7d8c0d8f2b9aeb53fa92466006930c5ca38e930a99cbd95a2228d9d95b5b8191).

## Sorties (telles qu'imprimées)

~~~
texte  1 : attendu 2, obtenu 2, section (b) lignes (3, 7) : PASSE
texte  2 : attendu 3, obtenu 3, section (b) lignes (0, 13) : PASSE
texte  3 [plusieurs H_A par duel] : attendu 2, obtenu 2, section (b) lignes (0, 13) : PASSE
texte  4 [plusieurs H_A par duel] : attendu 2, obtenu 2, section (b) lignes (4, 13) : PASSE
texte  5 [plusieurs H_A par duel] : attendu 2, obtenu 2, section (b) lignes (0, 8) : PASSE
texte  6 : attendu 1, obtenu 1, section (b) lignes (3, 7) : PASSE
texte  7 : attendu 2, obtenu 2, section (b) lignes (3, 7) : PASSE
texte  8 : attendu 2, obtenu 2, section (b) lignes (3, 7) : PASSE
texte  9 : attendu 3, obtenu 3, section (b) lignes (3, 8) : PASSE
texte 10 [plusieurs H_A par duel] : attendu 2, obtenu 2, section (b) lignes (0, 8) : PASSE
RÉSULTAT : PASSE (10/10 textes au nombre attendu)
~~~

## Réserves de Fable, rappelées sans changement de texte

- L'épreuve n'est plus aveugle : la règle a été écrite après lecture des dix textes ; la réussite montre qu'elle les couvre, pas qu'elle couvre les cellules.
- Limites connues non éprouvées ici : rappel sur une ligne (A puis B à l'intérieur d'un duel ouvre un duel en trop) ; section mixte (duel sans ligne d'opposition placé après un duel qui en a une, non compté).
- Recommandation de Fable, non faite ici et laissée au directeur : deux ou trois textes de plus écrits par une session qui n'a pas lu la correction 43, dont un rappel sur une ligne, joués à titre indicatif.
