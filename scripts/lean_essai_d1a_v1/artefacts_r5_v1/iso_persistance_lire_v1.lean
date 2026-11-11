-- épreuve d'isolement : l'item suivant ne doit rien retrouver
def tenter (nom : String) (action : IO String) : IO Unit := do
  try
    let r ← action
    IO.println s!"ISOLEMENT {nom} REUSSI {r.take 120}"
  catch e =>
    IO.println s!"ISOLEMENT {nom} ECHEC {e}"

#eval tenter "lecture-tmp-precedent" (IO.FS.readFile "/tmp/persistance-v1.txt")
#eval tenter "lecture-item-precedent" (IO.FS.readFile "/item/persistance-v1.txt")
#eval tenter "liste-items" (do let d ← System.FilePath.readDir "/srv/items"; pure (toString (d.map (·.fileName)).toList))
