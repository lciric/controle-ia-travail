"""python executer_vast.py ID 'COMMANDE' SORTIE : `vastai execute` (commandes bornées du loueur : ls, du) par le client
1.11.2 lui-même ; sa réponse texte (que le client, qui attend un objet JSON, ne sait pas lire) est écrite telle quelle."""
import sys
ident, cmd, sortie = sys.argv[1], sys.argv[2], sys.argv[3]
assert cmd.split()[0] in ("ls", "du"), "seules ls et du"
from vastai.api import instances as ia
from vastai.cli.commands import misc
orig, rendu = ia.execute, []
def tap(client, **kw):
    r = orig(client, **kw); rendu.append(r)
    raise SystemExit(0)
ia.execute = misc.instances_api.execute = tap
sys.argv = ["vastai", "execute", ident, cmd]
from vastai.cli.main import main
try:
    main()
except SystemExit:
    pass
r = rendu[0] if rendu else None
assert isinstance(r, str), f"réponse inattendue : {type(r).__name__}"
open(sortie, "x", encoding="utf-8").write(r)
print(f"{sortie} : {len(r)} signes, {r.count(chr(10))} lignes")
