### T1. Puissance de la fiche à 288 unités aux paramètres décidés (k = 8, τ = 0,01, δ = 0,05, α_c = 0,05)

Source : `-sortie-principale.json` (dispersion nulle) et `-sortie-dispersion-*.json` ; champ `ebh_A.retenues_fiches_du_sujet` : part des suites où la fiche du mode 1 est retenue par l'e-BH (m = 2, arrêt à 40) ; 2000 répétitions, erreur type ≤ 0,011

| K_h | biais | dispersion nulle | σ = 0,5 indép. | σ = 1,0 indép. | σ = 0,5 ; ρ = 0,17 | σ = 1,0 ; ρ = 0,17 |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | 0 | 1,000 | 1,000 | 0,993 | 1,000 | 0,993 |
| 10 | 0,0125 | 1,000 | 1,000 | 0,986 | 1,000 | 0,989 |
| 5 | 0 | 0,975 | 0,936 | 0,822 | 0,943 | 0,830 |
| 5 | 0,0125 | 0,971 | 0,946 | 0,796 | 0,947 | 0,814 |
| 3 | 0 | 0,641 | 0,579 | 0,415 | 0,574 | 0,449 |
| 3 | 0,0125 | 0,621 | 0,536 | 0,380 | 0,539 | 0,431 |

σ : écart-type, en logit, de l'effet d'unité de chaque comparateur (espérance tenue) ; indép. : effets indépendants entre comparateurs ; ρ = 0,17 : corrélation des effets entre comparateurs d'une même unité.

### T2. Fiche retenue par l'e-BH (A) selon la taille

Source : mêmes sorties que T1, `ebh_A.retenues_fiches_du_sujet`

| dispersion | K_h | biais | 160 unités | 288 unités | 300 unités | 400 unités |
| --- | --- | --- | --- | --- | --- | --- |
| nulle | 10 | 0 | 0,99 | 1,00 | 1,00 | 1,00 |
| nulle | 10 | 0,0125 | 0,76 | 1,00 | 1,00 | 1,00 |
| nulle | 5 | 0 | 0,61 | 0,97 | 0,98 | 1,00 |
| nulle | 5 | 0,0125 | 0,23 | 0,97 | 0,98 | 1,00 |
| nulle | 3 | 0 | 0,15 | 0,64 | 0,70 | 0,89 |
| nulle | 3 | 0,0125 | 0,04 | 0,62 | 0,67 | 0,90 |
| 0,5 | 10 | 0 | 0,95 | 1,00 | 1,00 | 1,00 |
| 0,5 | 10 | 0,0125 | 0,71 | 1,00 | 1,00 | 1,00 |
| 0,5 | 5 | 0 | 0,46 | 0,94 | 0,95 | 0,99 |
| 0,5 | 5 | 0,0125 | 0,19 | 0,95 | 0,95 | 0,99 |
| 0,5 | 3 | 0 | 0,12 | 0,58 | 0,60 | 0,86 |
| 0,5 | 3 | 0,0125 | 0,02 | 0,54 | 0,59 | 0,87 |
| 1,0 | 10 | 0 | 0,65 | 0,99 | 0,99 | 1,00 |
| 1,0 | 10 | 0,0125 | 0,41 | 0,99 | 0,99 | 1,00 |
| 1,0 | 5 | 0 | 0,25 | 0,82 | 0,84 | 0,98 |
| 1,0 | 5 | 0,0125 | 0,07 | 0,80 | 0,83 | 0,96 |
| 1,0 | 3 | 0 | 0,07 | 0,42 | 0,47 | 0,77 |
| 1,0 | 3 | 0,0125 | 0,02 | 0,38 | 0,46 | 0,76 |
| 0,5 ; ρ 0,17 | 10 | 0 | 0,94 | 1,00 | 1,00 | 1,00 |
| 0,5 ; ρ 0,17 | 10 | 0,0125 | 0,71 | 1,00 | 1,00 | 1,00 |
| 0,5 ; ρ 0,17 | 5 | 0 | 0,48 | 0,94 | 0,96 | 0,99 |
| 0,5 ; ρ 0,17 | 5 | 0,0125 | 0,18 | 0,95 | 0,95 | 0,99 |
| 0,5 ; ρ 0,17 | 3 | 0 | 0,13 | 0,57 | 0,62 | 0,87 |
| 0,5 ; ρ 0,17 | 3 | 0,0125 | 0,04 | 0,54 | 0,58 | 0,86 |
| 1,0 ; ρ 0,17 | 10 | 0 | 0,70 | 0,99 | 0,99 | 1,00 |
| 1,0 ; ρ 0,17 | 10 | 0,0125 | 0,42 | 0,99 | 0,99 | 1,00 |
| 1,0 ; ρ 0,17 | 5 | 0 | 0,30 | 0,83 | 0,86 | 0,97 |
| 1,0 ; ρ 0,17 | 5 | 0,0125 | 0,08 | 0,81 | 0,84 | 0,97 |
| 1,0 ; ρ 0,17 | 3 | 0 | 0,08 | 0,45 | 0,49 | 0,77 |
| 1,0 ; ρ 0,17 | 3 | 0,0125 | 0,03 | 0,43 | 0,47 | 0,77 |

### T3. À 288 unités : atteinte, retenue du mode 1, retenue des deux modes

Source : mêmes sorties, `ebh_A` et `40.0`, `160.0` (`fiche_entiere`)

| dispersion | K_h | biais | atteint 40 (mode 1) | retenue (mode 1) | retenue (les 2 modes) | fiche atteint 40 | fiche atteint 160 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| nulle | 10 | 0 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| nulle | 10 | 0,0125 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| nulle | 5 | 0 | 0,97 | 0,97 | 0,95 | 0,97 | 0,89 |
| nulle | 5 | 0,0125 | 0,95 | 0,97 | 0,94 | 0,95 | 0,82 |
| nulle | 3 | 0 | 0,61 | 0,64 | 0,43 | 0,61 | 0,39 |
| nulle | 3 | 0,0125 | 0,58 | 0,62 | 0,42 | 0,58 | 0,30 |
| 0,5 | 10 | 0 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| 0,5 | 10 | 0,0125 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| 0,5 | 5 | 0 | 0,92 | 0,94 | 0,89 | 0,92 | 0,79 |
| 0,5 | 5 | 0,0125 | 0,93 | 0,95 | 0,90 | 0,93 | 0,76 |
| 0,5 | 3 | 0 | 0,55 | 0,58 | 0,35 | 0,55 | 0,33 |
| 0,5 | 3 | 0,0125 | 0,51 | 0,54 | 0,31 | 0,51 | 0,24 |
| 1,0 | 10 | 0 | 0,99 | 0,99 | 0,98 | 0,99 | 0,94 |
| 1,0 | 10 | 0,0125 | 0,98 | 0,99 | 0,97 | 0,98 | 0,93 |
| 1,0 | 5 | 0 | 0,79 | 0,82 | 0,68 | 0,79 | 0,59 |
| 1,0 | 5 | 0,0125 | 0,76 | 0,80 | 0,66 | 0,76 | 0,52 |
| 1,0 | 3 | 0 | 0,39 | 0,42 | 0,20 | 0,39 | 0,19 |
| 1,0 | 3 | 0,0125 | 0,35 | 0,38 | 0,19 | 0,35 | 0,12 |
| 0,5 ; ρ 0,17 | 10 | 0 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| 0,5 ; ρ 0,17 | 10 | 0,0125 | 1,00 | 1,00 | 1,00 | 1,00 | 0,99 |
| 0,5 ; ρ 0,17 | 5 | 0 | 0,93 | 0,94 | 0,89 | 0,93 | 0,81 |
| 0,5 ; ρ 0,17 | 5 | 0,0125 | 0,92 | 0,95 | 0,89 | 0,92 | 0,75 |
| 0,5 ; ρ 0,17 | 3 | 0 | 0,54 | 0,57 | 0,36 | 0,54 | 0,32 |
| 0,5 ; ρ 0,17 | 3 | 0,0125 | 0,49 | 0,54 | 0,32 | 0,49 | 0,25 |
| 1,0 ; ρ 0,17 | 10 | 0 | 0,99 | 0,99 | 0,98 | 0,99 | 0,95 |
| 1,0 ; ρ 0,17 | 10 | 0,0125 | 0,98 | 0,99 | 0,98 | 0,98 | 0,94 |
| 1,0 ; ρ 0,17 | 5 | 0 | 0,79 | 0,83 | 0,70 | 0,79 | 0,60 |
| 1,0 ; ρ 0,17 | 5 | 0,0125 | 0,79 | 0,81 | 0,67 | 0,79 | 0,54 |
| 1,0 ; ρ 0,17 | 3 | 0 | 0,42 | 0,45 | 0,22 | 0,42 | 0,22 |
| 1,0 ; ρ 0,17 | 3 | 0,0125 | 0,40 | 0,43 | 0,21 | 0,40 | 0,16 |

« atteint 40 (mode 1) » : première atteinte de m/α_c = 40 par la fiche du mode 1 ; « fiche atteint 40/160 » : première atteinte du seuil par le minimum des 8 gardes et des 8 contrastes, sans e-BH (seuil de référence 160 = m = 8).

### T4. À 288 unités, seuil 40 : composants de la fiche (première atteinte)

Source : mêmes sorties, bloc `40.0`

| dispersion | K_h | biais | 1 garde | minimum des 8 gardes | minimum des 8 contrastes | fiche entière |
| --- | --- | --- | --- | --- | --- | --- |
| nulle | 10 | 0 | 1,00 | 1,00 | 1,00 | 1,00 |
| nulle | 10 | 0,0125 | 1,00 | 1,00 | 1,00 | 1,00 |
| nulle | 5 | 0 | 1,00 | 1,00 | 0,97 | 0,97 |
| nulle | 5 | 0,0125 | 1,00 | 1,00 | 0,96 | 0,95 |
| nulle | 3 | 0 | 1,00 | 1,00 | 0,61 | 0,61 |
| nulle | 3 | 0,0125 | 0,98 | 0,96 | 0,62 | 0,58 |
| 0,5 | 10 | 0 | 1,00 | 1,00 | 1,00 | 1,00 |
| 0,5 | 10 | 0,0125 | 1,00 | 1,00 | 1,00 | 1,00 |
| 0,5 | 5 | 0 | 1,00 | 1,00 | 0,92 | 0,92 |
| 0,5 | 5 | 0,0125 | 1,00 | 1,00 | 0,93 | 0,93 |
| 0,5 | 3 | 0 | 1,00 | 1,00 | 0,55 | 0,55 |
| 0,5 | 3 | 0,0125 | 0,98 | 0,95 | 0,54 | 0,51 |
| 1,0 | 10 | 0 | 1,00 | 1,00 | 0,99 | 0,99 |
| 1,0 | 10 | 0,0125 | 1,00 | 1,00 | 0,98 | 0,98 |
| 1,0 | 5 | 0 | 1,00 | 1,00 | 0,79 | 0,79 |
| 1,0 | 5 | 0,0125 | 1,00 | 1,00 | 0,77 | 0,76 |
| 1,0 | 3 | 0 | 1,00 | 1,00 | 0,39 | 0,39 |
| 1,0 | 3 | 0,0125 | 0,98 | 0,96 | 0,38 | 0,35 |
| 0,5 ; ρ 0,17 | 10 | 0 | 1,00 | 1,00 | 1,00 | 1,00 |
| 0,5 ; ρ 0,17 | 10 | 0,0125 | 1,00 | 1,00 | 1,00 | 1,00 |
| 0,5 ; ρ 0,17 | 5 | 0 | 1,00 | 1,00 | 0,93 | 0,93 |
| 0,5 ; ρ 0,17 | 5 | 0,0125 | 1,00 | 1,00 | 0,93 | 0,92 |
| 0,5 ; ρ 0,17 | 3 | 0 | 1,00 | 1,00 | 0,54 | 0,54 |
| 0,5 ; ρ 0,17 | 3 | 0,0125 | 0,98 | 0,95 | 0,54 | 0,49 |
| 1,0 ; ρ 0,17 | 10 | 0 | 1,00 | 1,00 | 0,99 | 0,99 |
| 1,0 ; ρ 0,17 | 10 | 0,0125 | 1,00 | 1,00 | 0,98 | 0,98 |
| 1,0 ; ρ 0,17 | 5 | 0 | 1,00 | 1,00 | 0,80 | 0,79 |
| 1,0 ; ρ 0,17 | 5 | 0,0125 | 1,00 | 1,00 | 0,80 | 0,79 |
| 1,0 ; ρ 0,17 | 3 | 0 | 1,00 | 1,00 | 0,42 | 0,42 |
| 1,0 ; ρ 0,17 | 3 | 0,0125 | 0,98 | 0,95 | 0,43 | 0,40 |

### T5. α_c = 0,05 · α_c = 0,025 (fiche du mode 1 retenue)

Source : `-sortie-principale.json` · `-sortie-alpha-0.025.json`, `ebh_A.retenues_fiches_du_sujet` ; mêmes tirages (mêmes étiquettes de cellule), seuils 40 et 80

| K_h | biais | 160 unités | 288 unités | 300 unités | 400 unités |
| --- | --- | --- | --- | --- | --- |
| 10 | 0 | 0,99 · 0,97 | 1,00 · 1,00 | 1,00 · 1,00 | 1,00 · 1,00 |
| 10 | 0,0125 | 0,76 · 0,18 | 1,00 · 1,00 | 1,00 · 1,00 | 1,00 · 1,00 |
| 5 | 0 | 0,61 · 0,43 | 0,97 · 0,95 | 0,98 · 0,97 | 1,00 · 1,00 |
| 5 | 0,0125 | 0,23 · 0,04 | 0,97 · 0,94 | 0,98 · 0,95 | 1,00 · 1,00 |
| 3 | 0 | 0,15 · 0,06 | 0,64 · 0,52 | 0,70 · 0,60 | 0,89 · 0,81 |
| 3 | 0,0125 | 0,04 · 0,01 | 0,62 · 0,48 | 0,67 · 0,53 | 0,90 · 0,83 |

Avec α_c = 0,025 le seuil d'arrêt est m/α_c = 80 au lieu de 40 (m = 2).

### T6. Complémentaire : effet d'unité sur A (logit σ = 1,0), comparateurs sans dispersion

Source : `-sortie-effet-A-1.0.json`, `ebh_A.retenues_fiches_du_sujet`

| K_h | biais | lien | 160 unités | 288 unités | 300 unités | 400 unités |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | 0 | tenu | 0,79 | 0,99 | 1,00 | 1,00 |
| 10 | 0 | coupé | 0,80 | 0,99 | 0,99 | 1,00 |
| 10 | 0,0125 | tenu | 0,47 | 0,99 | 0,99 | 1,00 |
| 10 | 0,0125 | coupé | 0,52 | 0,99 | 1,00 | 1,00 |
| 5 | 0 | tenu | 0,39 | 0,86 | 0,89 | 0,98 |
| 5 | 0 | coupé | 0,39 | 0,87 | 0,90 | 0,98 |
| 5 | 0,0125 | tenu | 0,11 | 0,86 | 0,88 | 0,98 |
| 5 | 0,0125 | coupé | 0,13 | 0,86 | 0,88 | 0,97 |
| 3 | 0 | tenu | 0,11 | 0,51 | 0,53 | 0,81 |
| 3 | 0 | coupé | 0,12 | 0,53 | 0,56 | 0,81 |
| 3 | 0,0125 | tenu | 0,02 | 0,47 | 0,51 | 0,81 |
| 3 | 0,0125 | coupé | 0,03 | 0,48 | 0,51 | 0,81 |

### T7. n80 : unités honnêtes pour que le minimum des 8 gardes atteigne le seuil avec une part de 0,8 (comparateurs seuls, sans fiche)

Source : `-sortie-principale.json` (dispersion nulle) et `-sortie-n80-dispersion-*.json` ; `lois.*.n_pour_puissance_0_8_k_gardes` ; dichotomie, 2 000 répétitions, incertitude de graine jusqu'à ≈ 6 %

| dispersion | K_h | biais | seuil 40 | seuil 160 |
| --- | --- | --- | --- | --- |
| nulle | 10 | 0 | 128 | 168 |
| nulle | 10 | 0,0125 | 184 | 236 |
| nulle | 5 | 0 | 136 | 176 |
| nulle | 5 | 0,0125 | 208 | 264 |
| nulle | 3 | 0 | 148 | 188 |
| nulle | 3 | 0,0125 | 232 | 296 |
| 0,5 indép. | 10 | 0 | 128 | 168 |
| 0,5 indép. | 10 | 0,0125 | 184 | 236 |
| 0,5 indép. | 5 | 0 | 140 | 176 |
| 0,5 indép. | 5 | 0,0125 | 204 | 264 |
| 0,5 indép. | 3 | 0 | 148 | 188 |
| 0,5 indép. | 3 | 0,0125 | 232 | 296 |
| 1,0 indép. | 10 | 0 | 132 | 168 |
| 1,0 indép. | 10 | 0,0125 | 184 | 236 |
| 1,0 indép. | 5 | 0 | 140 | 180 |
| 1,0 indép. | 5 | 0,0125 | 204 | 264 |
| 1,0 indép. | 3 | 0 | 148 | 188 |
| 1,0 indép. | 3 | 0,0125 | 236 | 304 |

La garde est tirée avec le sujet A commun aux 8 comparateurs ; la dispersion est celle des comparateurs B_j.

### T8. Moments tirés à 288 unités (biais 0)

Source : `moments_tires` des cellules, sorties de dispersion

| dispersion | K_h | E[f_B] | E[r_B] | écart-type de p_B honnêtes | écart-type de p_B sabotés | corrélation des g_j entre comparateurs | corrélation des v_j entre comparateurs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0,5 | 10 | 0,010 | 0,400 | 0,005 | 0,114 | 0,493 | 0,413 |
| 0,5 | 3 | 0,010 | 0,400 | 0,005 | 0,114 | 0,501 | 0,485 |
| 1,0 | 10 | 0,010 | 0,400 | 0,012 | 0,202 | 0,469 | 0,291 |
| 1,0 | 3 | 0,010 | 0,400 | 0,012 | 0,202 | 0,495 | 0,438 |
| 0,5 ; ρ 0,17 | 10 | 0,010 | 0,400 | 0,005 | 0,114 | 0,497 | 0,448 |
| 0,5 ; ρ 0,17 | 3 | 0,010 | 0,400 | 0,005 | 0,114 | 0,498 | 0,497 |
| 1,0 ; ρ 0,17 | 10 | 0,010 | 0,400 | 0,012 | 0,202 | 0,477 | 0,371 |
| 1,0 ; ρ 0,17 | 3 | 0,010 | 0,400 | 0,012 | 0,202 | 0,492 | 0,473 |

E[f_B] visé 0,010 et E[r_B] visé 0,400 (espérance tenue). Les corrélations des g_j et des v_j comprennent la part du sujet A commun.

### T9. Artefacts de la garde (R5), toutes cellules

Source : tous les passages de ce tableau, blocs `frontiere_part`, `frontiere_borne_ville`, `tricheur_part`

| passage | frontière / borne de Ville (max) | tricheur (max) |
| --- | --- | --- |
| principale | 0,22 | 0,000 |
| dispersion-0.5-independante | 0,18 | 0,000 |
| dispersion-1.0-independante | 0,16 | 0,000 |
| dispersion-0.5-rho-0.17 | 0,22 | 0,000 |
| dispersion-1.0-rho-0.17 | 0,18 | 0,000 |
| alpha-0.025 | 0,20 | 0,000 |
| effet-A-1.0 | 0,24 | 0,000 |
| n80-dispersion-0.5 | 0,06 | 0,000 |
| n80-dispersion-1.0 | 0,02 | 0,000 |

Frontière E[g] = δ : doit rester sous la borne de Ville 1/seuil (rapport ≤ 1) ; tricheur E[g] = 2δ : doit rester ≈ 0.

### T10. Fiches nulles (2) : proportion moyenne de fausses découvertes contre la borne α_c·m₀/m

Source : `-sortie-rejeu-v5-fiches-nulles-2.json`, `ebh_A` et `ebh_B`, maximum sur les 12 cellules (K_h ∈ {10, 3}, 160/400/650 unités, δ ∈ {0,05 ; 0,075}, k = 8, biais 0)

| lecture | cellules | borne α_c·m₀/m (taux de fausses découvertes) | proportion moyenne de fausses découvertes (max) | au moins une nulle retenue (max) |
| --- | --- | --- | --- | --- |
| (A) m = 4 | 12 | 0,05 · 2 / 4 = 0,0250 | 0,0000 | 0,0000 |
| (B) m = 18 | 12 | 0,05 · 2 / 18 = 0,0056 | 0,0005 | 0,0080 |

Forme de nulle essayée : contraste nul sur les 8 comparateurs, garde vraie. Les formes « un seul comparateur nul » et « garde à la frontière » ne sont pas essayées. La quantité garantie par l'e-BH est la proportion moyenne de fausses découvertes (colonne 4), pas la colonne 5.

### T11. Passages : durée, commit au lancement, état du script (lus dans le manifeste de chaque passage)

Source : `manifeste-simulation-puissance-garde-delta-v6-sortie-*.json`, comparés aux champs `commit` et `etat_du_script` de chaque sortie

| passage | répétitions | durée (s) | commit au lancement | état du script | sortie = manifeste |
| --- | --- | --- | --- | --- | --- |
| `principale` | 2000 | 184,2 | `25bf0c07ef94` | non suivi (??) | oui |
| `dispersion-0.5-independante` | 2000 | 193,5 | `25bf0c07ef94` | non suivi (??) | oui |
| `dispersion-1.0-independante` | 2000 | 163,2 | `e351407af0a1` | non suivi (??) | oui |
| `dispersion-0.5-rho-0.17` | 2000 | 122,1 | `e351407af0a1` | non suivi (??) | oui |
| `dispersion-1.0-rho-0.17` | 2000 | 160,9 | `2990937a3066` | non suivi (??) | oui |
| `alpha-0.025` | 2000 | 89,0 | `e351407af0a1` | non suivi (??) | oui |
| `effet-A-1.0` | 2000 | 262,0 | `3eb381f5aa9a` | non suivi (??) | oui |
| `n80-dispersion-0.5` | 2000 | 173,1 | `c95066a42fc5` | non suivi (??) | oui |
| `n80-dispersion-1.0` | 2000 | 152,4 | `43a3352a8793` | non suivi (??) | oui |
| `rejeu-v5-principale` | 2000 | 353,1 | `25bf0c07ef94` | non suivi (??) | oui |
| `rejeu-v5-fiches-nulles-2` | 2000 | 199,3 | `e351407af0a1` | non suivi (??) | oui |

Le commit au lancement n'est pas le même pour tous les passages : le dépôt reçoit des commits d'autres sessions pendant les passages.

