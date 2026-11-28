Passe finale, module v3, C d'essai `3521ff75c316c9f31403486fc6ca84a1c29daeca` ; chaque journal est la sortie brute de
son banc, redirigée dans un fichier neuf de `…/chaine-v3/`.

{TABLE_JOURNAUX}

- `verifications_p4_v1.py preuves …/chaine-v3` (sept journaux des bancs) : code 0, seize scripts éprouvés, chacun égal au
  script livré.
- `verifications_p4_v1.py repetition 3521ff75… …/chaine-v3/repetition-jouet-p4-v1.log P4-instrument-v1-candidat2-essai.md
  79c3e677…` : code 0, quatre scripts répétés égaux aux scripts livrés.
- Répétition : passages 1-sain (code 0), 2 (2), 3 (1), 4 (124), 5-arrêt du module (1) ; sept récupérations conformes avec
  destruction ; vingt-sept artefacts à un seul KO, instance gardée, état et heure limite ; refus en code 2 de la place
  (état et heure limite), des traces d'un autre lancement, du clonage (état et heure limite) ; repli de l'affichage
  établi ; lecture jouet ; aucun jeton, aucune fenêtre affichés ; aucun `__pycache__`.
- Passe préliminaire (C d'essai `3a99173f…`, `…/chaine-v3-travail/passe-1/`) : mêmes verdicts, sauf CV3-01 (corrigé) et
  CV3-04 (minuit, banc du lanceur) ; elle a joué le tokeniseur de substitution (CV3-02).
