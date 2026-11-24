# Passation — développeur du code de la dose–réponse — jalon de la course désignée — 2026-11-24 15:45 UTC

Suite de la passation `2026-11-24-1338-developpeur-code-dose-reponse.md`. Session fille de la mère `session_01Qi7Gr3Ggccg85kjmP654WC` ; Opus 5.5, effort élevé ; branche `code/dose-reponse-consigne-cachee-v1`.

## Fait depuis la passation précédente

- Ordres de lancement v3 (`9e065fdf…`) et v4 (`b9450aa1…`), après la contre-lecture neuve de la v2 et sa vérification (corrections B1, B2, M1-M4, m1-m9, N1-N4 ; m8 corrigé autrement : un seul `--dossier`).
- Mot de Lazar GO-2026-11-24-31 : branche (b), option A ; texte de désignation scellé `prereg/G0-critere-3-designation-course-v1.md` (19dbc99e…), ligne DESIGNATION-CRITERE-3 sur main.
- Amorce v3 (commit 685844fb) : `src/controle_ia/dose_reponse/extraction_v1.py` (`7fd66b58…`), `scripts/amorce_instance_dose_reponse_v3.sh` (`722390c3…`), `scripts/lancer_dose_reponse_v3.sh` (`b260f74a…`), liste d'essais de l'instance v3 (58 attendus, `4d99cacc…`), `tests/test_dose_reponse_amorce_v3.py` (13 essais verts, cas sain et artefact de l'extraction du texte de désignation).

## En cours

- Code du lecteur du texte (`CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE`) : sous-agent Opus 5.5 neuf, qui copie `scripts/mots_et_cout_t06_v3.py` sous `scripts/lecteur_texte_dose_reponse_v1.py` et n'en change que ce que le texte de désignation permet ; fichiers neufs, non committés par lui (l'orchestrateur verse).

## Reste

1. Verser le lecteur (commit C2 = code complet), contre-lecture Sonnet 5.5 neuve (amorce v3 + lecteur), vérification par le même.
2. Lignes proposées : CODE-DOSE-REPONSE-CONSIGNE-CACHEE nouvelle (commit C2, chemin portant C2) et CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE.
3. Ordre de lancement v5 : branche (b) jouée ; `--designation` avec `lignes_registre` = DESIGNATION-CRITERE-3, CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE, SONDES-LUES-CRITERE-3, CODE-MOTS-ET-COUT-T06 ; texte de désignation porté sur la branche de lancement ; lanceur et amorce v3 ; `verifier-code` du lecteur avant la création.

## Réserves

- La ligne SONDES-LUES-CRITERE-3 est établie ailleurs (mère) ; sans elle, aucune création.
- Réserves du code v2 inchangées (V2-01 à V2-04).

## Prochaine action

Au retour du sous-agent : relire son rendu, jouer ses essais, committer C2, lancer la contre-lecture.

## Instances actives

Aucune ; aucune dépense.
