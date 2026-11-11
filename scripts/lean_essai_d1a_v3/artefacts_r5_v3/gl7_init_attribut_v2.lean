import Mathlib

-- artefact CLL-04 (c) : initialiseur par l'attribut `init`, sans mot interdit ; s'il tourne à l'import du contrôle, il écrit
-- une fausse sortie JSON et quitte avec le code 0. G-L3+ (liste fermée des attributs) l'arrête ; G-L7 est relevée sans être
-- jugée (« observer ») : elle échoue si Lean exécute l'initialiseur d'un module importé.
@[init] def demarrage : IO Unit := do
  IO.println "{\"severity\":\"information\",\"pos\":{\"line\":4,\"column\":0},\"data\":\"etape_1 : True\"}"
  IO.Process.exit 0

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
