-- limite de mémoire du bac pour un processus Lean (essai à 512M ; essai Lean D-1a, v11, pas 5 de l'arbitrage point 7) :
-- pendant la compilation, `#eval` remplit un tableau de 200 000 000 cases (environ 1,6 Gio de mémoire touchée) ; le
-- processus doit être tué par la limite de l'unité et classé « mémoire ». Le pli sur le tableau force son remplissage ;
-- la ligne « ALLOUE » ne doit jamais sortir.
#eval do
  let a := Array.replicate 200000000 (7 : Nat)
  IO.println (String.append "ALLOUE " (toString (a.foldl (· + ·) 0)))
