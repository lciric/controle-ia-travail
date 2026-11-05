# Contre-lecture complète du lanceur durable v3 d'A1-v3 (troisième course) — v1

Contre-lecteur neuf (R2), début : 2026-11-05 09:36 UTC (`date -u`). Consigne : `docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/consigne-contre-lecture-complete-lanceur-v3-v1.md` (sha256 `00cf74d3…`, compagnon vérifié).

## Verdict
(en cours d'écriture)

## Pièces vérifiées
- Commit `bb35e87f0e7825b2225f2ade1177da428f78352e` présent ; les six fichiers de code y ont les empreintes de leurs compagnons et sont identiques à l'arbre de travail :
  - `src/controle_ia/hote_durable_a1_v3_v3.py` 916a3c85dca3be5bc961b3a4893d6e02751f744fab010987f74dcc6594762fa2 (907 lignes)
  - `scripts/amorce_hote_durable_a1_v3_v3.sh` e37bfde5f1aa30df1b294855ec0ec58973ce77549cdfd6fb28ae6f3705a293dd (67 lignes)
  - `tests/test_hote_durable_a1_v3_v3.py` 2f7e929172b5f37f495d23427707b351cf0125cf6eed9c20309befe78cb3c8ef (834 lignes)
  - `src/controle_ia/hote_durable_a1_v3.py` (v1) 5b853fde8987a472a191f769415068ecc15f1da8a042767bba4229dd5c29e0b1 (869 lignes)
  - `src/controle_ia/sonde_hote_durable_a1_v3_v10.py` 37b70a0646874e3769a9e45ccf1438121f2126aecc8307234c3cc590f122b81c (1071 lignes)
  - `src/controle_ia/sonde_hote_durable_a1_v3.py` f7c7f79ba974dd1e38743265caf88f09ce7d4d96ea4676f6d66e75cc9ebca69d (342 lignes)

## Points (en cours)

### Notes de travail (09:46 UTC)
- Essais rejoués : `tests/test_hote_durable_a1_v3_v3.py`, 96 passés en 109,7 s (09:43:42 → 09:45:32 UTC).
- GO rejoués hors réseau avec le code (`verifier_go`, `verifier_go_exact`) sur `registres/go.md` de `origin/main` (`0770797b`, sha256 `7f8721fb…`) et du canal à `740f49e2` (sha256 `bdd492d1…`), garde de `main` (`84512d4a…`) : GO-2026-11-04-06 accepté sur les deux (400 USD, échéance 2026-11-18), GO-2026-11-05-03 accepté sur `main` (35 USD) ; aucun doublon sur le canal ; ligne 82 du canal égale à l'octet à la ligne 244 de `main` ; refus le 2026-11-19.
- Faits de l'hôte (sonde v10, `e53876b5`) : Python 3.13.18, `/usr/bin/python3` 3.11.2, numpy 2.5.3, git 2.39.5, 56 cœurs, 32,1 Go libres.
