# Registre des Preuves de Validation et d'?limination (`controle-ia`)

Chaque r?sultat ci-dessous renvoie directement ? son fichier primaire brut dans `01_DONNEES_PRIMAIRES_BRUTES/` et `03_PREUVES_DE_VALIDATION_ET_AUDITS/`.

1. **Preuve 1 ? Qualification exp?rimentale de `rigor` et `falsifiable_duels` et Disqualification de `negative_controls` (`preuve_1_calibration_e0_meta_jev.json`)** :
   - Sur 12 paires appari?es par rejet ($u_3 - u_2 > 0,10$), `composite` ($\Delta_C = +0,275$), `falsifiable_duels` ($\Delta_C = +0,093$) et `rigor` ($\Delta_C = +0,078, |\Delta_R| = 0,028$) discriminent la disjonction r?elle des intervalles, tandis que `negative_controls` ($\Delta_C = +0,017, |\Delta_R| = 0,040$, t?moin vide $= 0,67$) est bannie.
2. **Preuve 2 ? Convergence monotone `[9 -> 6 -> 3 -> 0]` au Tour 4 et Matrice de Pr?dation Apprise (`preuve_3_matrice_predation_et_budget_tour4.json` & `preuve_4_etat_final_collisionneur_adaptatif_tour4.md`)** :
   - `claude-opus-5-5` atteint un poids de pr?dation de `5.933` contre `claude-fable-5-1` et de `7.162` contre `gemini-4-argon`.
   - Au Tour 4, `claude-fable-5-1` identifie et corrige 2 failles fatales qui avaient ?t? cr??es par ses propres corrections du Tour 3 (prouvant l'insuffisance d'un collisionneur fig? ? $T=3$ tours).
3. **Preuve 3 ? Les 30 Champions $\mathcal{M}_3$ int?graux sans troncature (`preuve_5_les_30_champions_m3_integraux_64k.json`)** :
   - 10 `claude-fable-5-1` + 10 `claude-opus-5-5` + 10 `gemini-4-argon` couvrant les 10 C?nes Math?matiques ? 64k jetons.
4. **Preuve 4 ? Les 4 Ponts $\mathcal{M}_2 \to \mathcal{M}_1$ consolid?s apr?s audit d'Opus 5.5 (`preuve_2_bilan_4_ponts_m2_consolides.json`)** :
   - `Silo-M2-1` (GLRT de Kelly sur fouillis, 16 failles corrig?es, `rigor = 3.57`), `Silo-M2-2` (R?traction radiale $C^1$ de Koopman, 13 failles corrig?es, `rigor = 3.73`), `Silo-M2-3` (Capacit? z?ro-erreur de Shannon $\alpha(G_n)$ vs $\alpha(G_1)$, 8 failles corrig?es, `rigor = 3.66`), `Silo-M2-4` (Divergence KL interventionnelle bidirectionnelle, 11 failles corrig?es, `duels = 0.48`).
5. **Preuve 5 ? Ex?cution $\mathcal{M}_0$ des 4 op?rateurs (`preuve_6_resultats_execution_m0_validation.json`)** :
   - Validation num?rique exacte des 4 fonctions `compute_O` et de leurs contr?les n?gatifs (`H_perp`, invariance en zone s?re, nul conditionnel sans m?moire, et sous-espaces al?atoires de Haar appari?s en norme).
