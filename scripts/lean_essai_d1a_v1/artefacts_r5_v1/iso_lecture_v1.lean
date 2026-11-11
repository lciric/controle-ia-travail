-- épreuve d'isolement : lectures hors du dossier de l'item
def tenter (nom : String) (action : IO String) : IO Unit := do
  try
    let r ← action
    IO.println s!"ISOLEMENT {nom} REUSSI {r.take 120}"
  catch e =>
    IO.println s!"ISOLEMENT {nom} ECHEC {e}"

#eval tenter "lecture-leurre" (IO.FS.readFile "/srv/leurre/leurre-v1.txt")
#eval tenter "lecture-leurre-proc" (IO.FS.readFile "/proc/1/root/srv/leurre/leurre-v1.txt")
#eval tenter "lecture-shadow" (IO.FS.readFile "/etc/shadow")
#eval tenter "lecture-cle-ssh-root" (IO.FS.readFile "/root/.ssh/authorized_keys")
#eval tenter "liste-srv" (do let d ← System.FilePath.readDir "/srv"; pure (toString (d.map (·.fileName)).toList))
#eval tenter "liste-harnais" (do let d ← System.FilePath.readDir "/opt/harnais"; pure (toString (d.map (·.fileName)).toList))
