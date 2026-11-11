-- épreuve d'isolement : écritures dans la chaîne, Mathlib, le harnais, la racine du bac
def tenter (nom : String) (action : IO String) : IO Unit := do
  try
    let r ← action
    IO.println (String.append "ISOLEMENT " (String.append nom (String.append " REUSSI " (r.take 120))))
  catch e =>
    IO.println (String.append "ISOLEMENT " (String.append nom (String.append " ECHEC " (toString e))))

#eval tenter "ecriture-controle" (do IO.FS.writeFile "/controle/Controle.lean" "-- piégé"; pure "écrit")
#eval tenter "ecriture-srv-controle" (do IO.FS.writeFile "/srv/controle/piege.lean" "x"; pure "écrit")
#eval tenter "ecriture-mathlib" (do IO.FS.writeFile "/opt/mathlib/Piege-v1.txt" "x"; pure "écrit")
#eval tenter "ecriture-olean-mathlib" (do IO.FS.writeFile "/opt/mathlib/.lake/build/lib/lean/Piege.olean" "x"; pure "écrit")
#eval tenter "ecriture-elan" (do IO.FS.writeFile "/opt/elan/Piege-v1.txt" "x"; pure "écrit")
#eval tenter "ecriture-usr" (do IO.FS.writeFile "/usr/Piege-v1.txt" "x"; pure "écrit")
#eval tenter "ecriture-harnais" (do IO.FS.writeFile "/opt/harnais/Piege-v1.txt" "x"; pure "écrit")
#eval tenter "ecriture-racine-bac" (do IO.FS.writeFile "/Piege-v1.txt" "x"; pure "écrit")
