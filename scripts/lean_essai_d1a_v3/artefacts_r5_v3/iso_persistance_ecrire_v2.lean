-- épreuve d'isolement : un item écrit dans son propre espace (permis)
def tenter (nom : String) (action : IO String) : IO Unit := do
  try
    let r ← action
    IO.println (String.append "ISOLEMENT " (String.append nom (String.append " REUSSI " (r.take 120))))
  catch e =>
    IO.println (String.append "ISOLEMENT " (String.append nom (String.append " ECHEC " (toString e))))

#eval tenter "ecriture-tmp" (do IO.FS.writeFile "/tmp/persistance-v1.txt" "jeton-persistance"; pure "écrit")
#eval tenter "ecriture-item" (do IO.FS.writeFile "/item/persistance-v1.txt" "jeton-persistance"; pure "écrit")
