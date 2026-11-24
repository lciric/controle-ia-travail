# Engagement de dépense, inscrit avant tout appel

- Dossier : collisionneur sur la dynamique de l'évasion sous filtrage pendant l'entraînement (protocole X).
- Accord : GO-2026-11-24-29 (main, R-5304), 20 USD, échéance 30 novembre 2026.
- Devis : docs/notes/collisionneur-v9/devis-collisionneur-dynamique-evasion-filtrage-v1.md (pire cas sans relance 17,99 USD comptés ; attendu environ 8 ; réel environ 3,5).
- Programme : collisionneur_v9_v8o.py (f63c513c…), étage III, --opus --astra --carbon --neon --google-arriere-plan, sans --sortie-max, sans bras témoin ; --plafond-usd 20 --ligne-usd 20.
- Clés : RR_ANTHROPIC_API_KEY (Anthropic), OPENAI_API_KEY_2 (Astra), GEMINI_API_KEY_FREE (Google, gratuite).
- Règle : un 429 ou un 503 de Google donne une reprise unique par cellule après une pause, puis arrêt sur les cellules Google et un mot à la mère.
- Inscrit le 2026-11-24T14:41:08Z par la session fille session_01Qi7Gr4L1p9Jdu9GbxtU362.
