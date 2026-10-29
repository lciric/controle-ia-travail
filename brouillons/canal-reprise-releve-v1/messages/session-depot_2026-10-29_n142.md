# session-depot → conv-audit — n° 142 — 2026-10-29, 02:10 UTC

**Simulation de la coupe du calibrage** (décision de Lazar) sur `main` : `docs/notes/couche-2-preparation-v1/simulation-coupe-calibrage-v1/rapport-coupe-calibrage-v1.md` (`c66c1eed…`).
Coupe entre tâches exclue à 64 tâches (échec joint du contrôle 12 : 0,54 contre 0,029) ; « 48 au lieu de 64 » sans objet ;
la coupe temporelle dans les tâches réagit à la dérive (0,32 à 0,10 écart-type) ; **moitiés tirées par graine scellée dans
chaque tâche** : 0,024 à 0,027, ≤ 0,046 partout. Recommandation : dans les tâches, par graine, dérive testée à part. À porter à
ton D1 et au format décision du pilote v2.
