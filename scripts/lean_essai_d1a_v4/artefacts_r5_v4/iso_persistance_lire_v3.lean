-- épreuve d'isolement : l'item suivant ne doit rien retrouver
-- v3 (essai Lean D-1a, v11, pas 2 de l'arbitrage point 7) : copie de iso_persistance_lire_v2.lean (inchangé, R12) ; sous Lean 4.35.0,
-- `String.take` rend une tranche `String.Slice` : chaque `.take k` est suivi de `.toString` (la v2 ne compilait pas : aucune tentative).
def tenter (nom : String) (action : IO String) : IO Unit := do
  try
    let r ← action
    IO.println (String.append "ISOLEMENT " (String.append nom (String.append " REUSSI " (r.take 120).toString)))
  catch e =>
    IO.println (String.append "ISOLEMENT " (String.append nom (String.append " ECHEC " (toString e))))

#eval tenter "lecture-tmp-precedent" (IO.FS.readFile "/tmp/persistance-v1.txt")
#eval tenter "lecture-item-precedent" (IO.FS.readFile "/item/persistance-v1.txt")
#eval tenter "liste-items" (do let d ← System.FilePath.readDir "/srv/items"; pure (toString (d.map (·.fileName)).toList))
