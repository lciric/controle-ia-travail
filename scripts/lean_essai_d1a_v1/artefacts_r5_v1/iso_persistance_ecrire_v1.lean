-- épreuve d'isolement : un item écrit dans son propre espace (permis)
def tenter (nom : String) (action : IO String) : IO Unit := do
  try
    let r ← action
    IO.println s!"ISOLEMENT {nom} REUSSI {r.take 120}"
  catch e =>
    IO.println s!"ISOLEMENT {nom} ECHEC {e}"

#eval tenter "ecriture-tmp" (do IO.FS.writeFile "/tmp/persistance-v1.txt" "jeton-persistance"; pure "écrit")
#eval tenter "ecriture-item" (do IO.FS.writeFile "/item/persistance-v1.txt" "jeton-persistance"; pure "écrit")
