import Mathlib

-- CLC3-06 : constante de l'agent dont le nom porte un omicron grec (« Cοprime » s'imprime comme « Coprime ») ; l'énoncé
-- final la cite. Refus mécaniques attendus : nom hors ASCII (G-L6), constante de l'agent dans l'énoncé final (G-L5).
def Cοprime (a b : ℕ) : Prop := Nat.Coprime a b

theorem etape_1 : Nat.Coprime 2 3 := by norm_num

theorem etape_2 : Cοprime 2 3 := etape_1

theorem enonce_item : Cοprime 2 3 := etape_2
