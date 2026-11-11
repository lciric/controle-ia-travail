import Mathlib

-- Premier pas du noyau : l'agent redéfinit `≤` sur ℕ. Les énoncés « 3 ≤ 2 » sont vérifiés par le noyau (avec l'instance de
-- l'agent), mais leur texte imprimé ne veut pas dire ce qu'ils disent : l'aller-retour (texte réélaboré sans les extensions
-- de l'agent) doit échouer (G-L5).
instance enonce_item.ordreFaux : LE ℕ := ⟨fun _ _ => True⟩

theorem etape_1 : (3 : ℕ) ≤ 2 := trivial

theorem etape_2 : (5 : ℕ) ≤ 1 := trivial

theorem enonce_item : (3 : ℕ) ≤ 2 := trivial
