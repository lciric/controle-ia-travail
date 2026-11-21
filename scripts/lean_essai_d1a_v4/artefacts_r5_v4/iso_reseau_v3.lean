-- épreuve d'isolement : connexion sortante pendant la compilation
-- v3 (essai Lean D-1a, v11, pas 2 de l'arbitrage point 7) : copie de iso_reseau_v2.lean (inchangé, R12) ; sous Lean 4.35.0,
-- `String.take` rend une tranche `String.Slice` : chaque `.take k` est suivi de `.toString` (la v2 ne compilait pas : aucune tentative).
def tenter (nom : String) (action : IO String) : IO Unit := do
  try
    let r ← action
    IO.println (String.append "ISOLEMENT " (String.append nom (String.append " REUSSI " (r.take 120).toString)))
  catch e =>
    IO.println (String.append "ISOLEMENT " (String.append nom (String.append " ECHEC " (toString e))))

def sortieProcessus (cmd : String) (args : Array String) : IO String := do
  let o ← IO.Process.output { cmd := cmd, args := args }
  if o.exitCode == 0 then
    pure (String.append "code 0 " (o.stdout.take 80).toString)
  else
    throw (IO.userError (String.append "code " (String.append (toString o.exitCode) (String.append " " (o.stderr.take 160).toString))))

#eval tenter "reseau-curl-ip" (sortieProcessus "curl" #["-sS", "-m", "8", "-o", "/dev/null", "http://1.1.1.1/"])
#eval tenter "reseau-python-tcp" (sortieProcessus "python3" #["-c", "import socket; socket.create_connection(('1.1.1.1', 443), 5)"])
#eval tenter "reseau-dns" (sortieProcessus "python3" #["-c", "import socket; print(socket.gethostbyname('github.com'))"])
