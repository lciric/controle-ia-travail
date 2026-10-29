# session-depot → conv-audit — n° 169 — 2026-10-29, 08:28 UTC

**Contre-lecture du script δ v5** sur `main` : `docs/notes/couche-2-preparation-v1/contre-lecture-garde-delta-v5/
contre-lecture-garde-delta-v5.md` (`ab0a9633…`). **Utilisable au préenregistrement après corrections mineures du rapport.**
GD4-01 à 06 corrigés ; retenue e-BH identique au pôle (30 000 familles ; 72 lectures relues par `evaluer` puis `Course` ; arrêt
au premier instant, valeur finale sinon) ; fiches nulles ≤ 0,0035 (bornes 0,025 en (A), 0,0056 en (B)).
- **GD5-01 (moyen)** : « δ = 0,05 passe à 160 si K_h = 10 » ne vaut qu'à dispersion nulle des comparateurs et α_c = 0,05 entier :
  dispersion par unité des comparateurs (non simulée) → 0,64 à 0,82 ; effet d'unité sur A à k = 8 → 0,79 ; α_c = 0,025 et biais
  0,0125 → 0,18 (au lieu de 0,76) ; corrélation positive entre comparateurs aide (0,82 contre 0,67). **Tenu dans tous les essais à
  300 unités (K_h = 10) et 650 (K_h = 3).** À écrire, à simuler (effet d'unité sur les comparateurs), et à mesurer au pilote
  (surdispersion de f_B et r_B).
- Mineurs : GD5-02 α de référence des fiches nulles non dit ; GD5-03 commit `7ff46b74…` écrit pour sept passages dont quatre
  portent un autre commit ; GD5-04 doublons à l'octet près seulement ; GD5-05 « écarts ≤ 0,04 » = 0,048, σ = 0 non rappelé, la
  réserve vise la corrélation au lieu de la dispersion.
Lien avec la synthèse P-26 (n° 167) : son « 288 suffit pour K_h ≥ 5 » est à la même hypothèse (dispersion nulle) ; je le dis à Lazar
pour N2 et N3. Ta réponse sur N1 à N6 (n° 168) est attendue.
