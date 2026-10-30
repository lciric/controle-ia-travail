# Complément 2 au LISEZMOI v3 — addendum v6, mutation m6 — v2

conv-audit (Fable 5.1), 30 octobre 2026, 23:45 UTC. Suit `complement-lisezmoi-v3-addendum-v5-v1.md` (gardé). Vérification des corrections : `contre-lecture-code/verification-corrections-cla-et-addendum-v5-v1.md` (Sonnet neuf) : « scellable après corrections mineures », VC-01 à VC-08.

- **Addendum v6** (`prereg/addendum-ecarts-bisociation-deux-espaces-v2-v6.md`, empreinte `37f6df2e0f3653088643b4eb1883c2a5b083111227edd3c53a0e411cd187774f`, non scellée) = v5 + VC-01 (point (vi-b) à l'état réel du code : `identites_paires`), VC-05 (renvoi S11 dans « Effet attendu »), VC-04 et VC-08 (point (ix) : limite du balayage, CLA-12 déclaré). Aucune décision ni seuil touché.
- Code : `invocation_unique_v2.py` lignes 43-44 (`ADDENDUM`, `EMPREINTE_ADDENDUM` à la v6) ; `essais/essais_cla_v2.py` ligne 43 (nom attendu) ; **VC-03** : `plomberie-corrections-v2/mutations_corrections_v1.py`, mutation m6, lambda à la signature `surcharge=None` — m6 échoue désormais par `AssertionError` (vérifié avec `--runxfail -k m6`), non par `TypeError`.
- Rejeu : **118 essais réussis** (30,12 s) ; **8 mutations xfail strictes** (7,37 s). Compagnons des trois fichiers régénérés.
- VC-07 (essai de filtre sur listes issues de JSON) : facultatif, non fait, déclaré.
- Suite : contrôle rapide de ces corrections par un sous-agent neuf → scellement de l'addendum v6 → reproduction des témoins régénérée → validation → invocation.
