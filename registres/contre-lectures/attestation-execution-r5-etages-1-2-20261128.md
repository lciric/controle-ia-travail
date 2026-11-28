# Attestation d'exécution mécanique R5 — Contre-lecture R2 (Étages 1 & 2)

## 1. Livrables scellables vérifiés
- `contre-lecture-r2-etages-1-2-v1.md` | Octets : `150903` | SHA-256 : `8325ba1c052db3d9b6431265e37f03b1014fae6b2e391948edce231a1952a30d`
- `test_oracles_r5_cloture_etages_1_2.py` | Octets : `29278` | SHA-256 : `893eee8ff515b02a7dd70f7de9f62fb2037f9d76b4ad5acd590b6b035a4e5c0c`

## 2. Exécution locale certifiée (13/13 tests passés, BLAS mono-fil)
- Interpréteur : `C:\Users\lciri\anaconda3\envs\c2judge\python.exe` (`Python 3.12.13`)
- Verrouillage déterministe : `OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1`

```text
PASS  test_constat_c1_c22_c23_schema_taches_validateur_et_scission_a0 (0.000s)
PASS  test_constat_c2_c4_c21_porte_ka3_parseur_cost_bpe_et_prejet (0.000s)
PASS  test_constat_c3_c5_c11_coherence_signe_m4_et_antipode_lora (0.267s)
PASS  test_constat_c6_c7_c8_conforme_groupe_pli_et_doublons_bootstrap (0.121s)
PASS  test_constat_c9_c10_c18_c19_emix_budget_et_preemption_en_ligne (0.000s)
PASS  test_constat_c12_c13_c14_c15_c24_leace_swig_we_et_woodbury (0.011s)
PASS  test_constat_c16_c17_c20_mad_zero_hmac_logprobs_et_bdev (0.034s)
PASS  test_mc_dgp0_nul_groupe_ar1_lora (1.216s)
PASS  test_mc_dgp1_confondant_jeton_unique (0.545s)
PASS  test_mc_dgp2_selection_porte_et_strate_o1 (0.175s)
PASS  test_mc_dgp3_mde_et_puissance_h2 (0.064s)
PASS  test_etancheite_zero_ulp_hors_pli_hors_tache_et_post_cost (0.005s)
PASS  test_isolation_subprocess_audithook_p8_et_a0 (2.086s)
TOTAL 13/13 PASS en 4.524s sous Python 3.12.13
```
