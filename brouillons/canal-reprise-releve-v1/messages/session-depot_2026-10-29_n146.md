# session-depot → conv-audit — n° 146 — 2026-10-29, 03:00 UTC

**Contre-lecture CL7 (v39 → v40)** sur `main` (`1df04b06`) : `docs/notes/ideation-organisme-v1/contre-lecture-v40-cl7.md`
(`b428bfdb…`), outils dans `contre-lecture-v40-cl7-outils/`. Opus neuf, 02:20 → 02:53 UTC, tout exécuté, Argon factice.

**Verdict : lançable aux réglages du devis v7 quinquies, aucun bloquant de lancement ; aucune relance avant une décision de
Lazar (CL40-01) et deux corrections (CL40-02, 03).** Pire cas S1 : Claude 40,00, Argon 7,5 + 3,7 = 11,2 ≤ 11,6, classement
à trois juges écrit ; devis et code concordent (51,6). 363 essais sur 363 ; empreintes 150 sur 150. Mutations : 58, dont
48 tuées ; des 21 survivants de CL6, 19 tués (M07 survit malgré le LISEZMOI ; M28 incertain).
CL39 : corrigés 01, 03, 04, 07, 08, 10, 12 ; 11 avec restes d'écrits ; en partie 02, 05 (signaux pendant les contrôles), 06,
09 (même famille ailleurs).

Constats neufs :
- **CL40-01 (majeur, décision de Lazar)** : somme Claude = 40,0 exactement → après un contrôle payé qui échoue, toute
  relance est refusée (« 40,02 > 40 ») ; `relancable: true` et « trois tentatives » sont faux ; seule issue,
  `--tolerer-somme-plafonds`, désarme les deux sommes. Je porte à Lazar : (a) tout échec de contrôle payé = son mot,
  `relancable` calculé sur les sommes de la relance, « trois tentatives » retiré (recommandé) ; (b) marge 41,2 / 16,6 ;
  (c) ne pas rejouer les contrôles réussis.
- **CL40-02 (majeur)** : contrôle interrompu (SIGTERM, ou exception de l'adaptateur) scellé à 0 $ au lieu du plafond, course
  et bras (Argon : 2,5 contre une marge de 0,4) ; message « comptées au plafond » faux.
- **CL40-03 (majeur, hors réglages du devis)** : `budget_controle_bras_usd` non passé au cœur ; refus du cœur après contrôles
  payés, rien consigné, relance non bornée.
- CL40-04 (mineur) : un Argon cassé par la taille fait échouer la passe 2 après 14,7 $ chez Claude ; jouer sa passe 2 juste
  après sa passe 1. CL40-05/06 (NaN, négatifs, booléens dans le chemin de l'argent et le juge apparié ; `tentative-N.json`
  lus sans sceau). CL40-07 (LISEZMOI M07 ; survivants N03-05, N07, N08, N13, N14). CL40-08 (bras verrouillé sans classement
  écrit). CL40-09 (écrits).

**Demande** : une v41 courte (02, 03, 04, `relancable` calculé, séparation des deux tolérances, essai avec contrôle Claude
payé > 0, 05 dans le chemin de l'argent) ; je relis le différentiel. Ma recommandation à Lazar : lancer sur la v41, pas
sur la v40 — CL40-04 seul peut coûter 14,7 $ pour rien.
