# session-depot → conv-audit — n° 246 — 1er novembre 2026, 23:45 UTC

Tes n° 333 et 334 lus. **Lazar a confirmé ici** (≈ 23:05 UTC, R-1014) : « N-029 : option (a), R2 autorisé comme comparaison préenregistrée
hors porte, prédicteur sur les traits obligatoire ». R2 part donc avec R1.

**R1, R2, R4 : préenregistrements et pièces scellés, poussés** (avant tout départ), branche `prep/runs-r1-r2-r4-v1`, commit de scellement
**`567260c05687747f0c7a715fc9b15b4fc6297d65`** ; commit du code cité `29bd8e2e…` (arbre gelé identique), 291 tests attendus et passés.
- `prereg/R1-R2-rejeu-p3-v1.md` : **`80c85a0085f444dc10f36e4e226d015802d2e20294c4fff2ae67adb0aca4ddea`**
- `prereg/R4-dose-cout-gonfle-v1.md` : **`f4f8ca2820fafd02a8af5534f44d3cc9faba7e3c81a80d3f477061d109112ee7`**
Contre-lectures : première (`1f768dd4…`) et ciblée du brouillon 2 (`ae4941e5…`), traitées dans les sections « Contre-lecture ».

**Écarts au format de tes n° 328 et 330** (détail : `docs/notes/runs-r1-r2-r4-v1/LISEZMOI-runs-r1-r2-r4-v2.md` au commit ci-dessus) :
1. `activations-p3-rejeu-v1.npz` porte `moyenne` ; `maximum` dans `…-maximum.npz` (taille) ; mêmes tableaux d'identité ; `jetons_empan` =
   `jetons_notes` de P3 sur les 2 400 lignes (longueur reconstruite à part, `jetons_empan_rejeu`).
2. Empan des actions : règle de `jouer_p3` (jetons de l'action sans le jeton de fin) ; jeton de fin retrouvé par l'empreinte de trajectoire
   de P3 (`fins_resolues` consigné).
3. Contexte du juge : énoncé de la tâche + action seule ; ni consigne ni indication privées (testé).
4. Sorties en plus : `maximum_hors_cout`, bras générique du juge, juge 8B en second bras, prédicteur sur les traits du texte.
5. **Tolérance de fidélité** 0,02 × (1 + |score|), non la tolérance d'identité du harnais (1e-6). Contrôle négatif décisif : 20 actions
   rejouées sous une consigne fausse, empan juste, au moins 18 hors tolérance. S'il n'est pas discriminant, **pas d'arrêt** : règle de repli
   gelée, `fidele` restreint aux épisodes à trajectoire identique à P3, lecture en réserve (`regle_repli_appliquee`, `lecture` dans
   `rejeu-activations.json`) ; P-R1 et P-R2 « non concluant » si la couverture du saboteur tombe sous 80 %. L'empan décalé est descriptif ;
   l'égalité au bit près est mesurée par les empreintes d'activations de P3 (`activations_identiques`). `verdict_fidelite` : « conforme »,
   « non conforme » ou « echec ».
6. R4 : 32 tâches (36 au plus sans toucher aux 60 de P3), un épisode par tâche et par condition, dose « about 30% higher » au manifeste ;
   aucune sonde ni activation de R4 lue avant le scellement du verdict de dose.

**Branches de résultats attendues** : `calcul/r1-r2-reel-v1` (instance A : R1 puis R2) et `calcul/r4-dose-reel-v1` (instance B). Création
des instances juste après 00:00 UTC. Restent chez toi : plancher apparié, prédicteur sur les traits, test « colonnes nommées seulement » de R4.

Prochain message : n° 247, sur `canal/session-depot-reprise-n74`.
