-- épreuve d'isolement : un item écrit dans son propre espace (permis)
-- v3 (essai Lean D-1a, v11, pas 2 de l'arbitrage point 7) : copie de iso_persistance_ecrire_v2.lean (inchangé, R12) ; sous Lean 4.35.0,
-- `String.take` rend une tranche `String.Slice` : chaque `.take k` est suivi de `.toString` (la v2 ne compilait pas : aucune tentative).
def tenter (nom : String) (action : IO String) : IO Unit := do
  try
    let r ← action
    IO.println (String.append "ISOLEMENT " (String.append nom (String.append " REUSSI " (r.take 120).toString)))
  catch e =>
    IO.println (String.append "ISOLEMENT " (String.append nom (String.append " ECHEC " (toString e))))

#eval tenter "ecriture-tmp" (do IO.FS.writeFile "/tmp/persistance-v1.txt" "jeton-persistance"; pure "écrit")
#eval tenter "ecriture-item" (do IO.FS.writeFile "/item/persistance-v1.txt" "jeton-persistance"; pure "écrit")
