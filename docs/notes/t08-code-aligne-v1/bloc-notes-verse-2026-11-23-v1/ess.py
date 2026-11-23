import sys, json, hashlib, tempfile
from pathlib import Path
from controle_ia.t08 import mots_et_cout_v1 as mc
from controle_ia.gardes import GardeArret
d=Path(tempfile.mkdtemp()); (d/"scripts").mkdir(); (d/"registres").mkdir()
m=d/"scripts/p.py"; m.write_text("PIECE_JOUET = True\n"+"".join(f"def {f}(*a, **k):\n    return None\n" for f in mc.CONTRAT))
sm=hashlib.sha256(m.read_bytes()).hexdigest()
i=d/"registres/i.json"; i.write_text(json.dumps({"commit":"a"*40,"fichiers":{"scripts/p.py":sm}}))
si=hashlib.sha256(i.read_bytes()).hexdigest()
mq={"commit":"a"*40,"fichier_inscription":"registres/i.json","sha256_inscription":si,"module":"scripts/p.py","sha256_module":sm}
try: mc.charger_piece("reel",mq,d,{"chemin":"registres/i.json","sha256":si})
except GardeArret as e: print("refus",str(e)[:60])
print("reste dans sys.modules:", mc.NOM_MODULE_PIECE in sys.modules)
# tuple/ KeyboardInterrupt wrap
m.write_text("raise KeyboardInterrupt\n"); sm=hashlib.sha256(m.read_bytes()).hexdigest()
i.write_text(json.dumps({"commit":"a"*40,"fichiers":{"scripts/p.py":sm}})); si=hashlib.sha256(i.read_bytes()).hexdigest()
mq.update(sha256_inscription=si,sha256_module=sm)
try: mc.charger_piece("reel",mq,d,{"chemin":"registres/i.json","sha256":si})
except BaseException as e: print(type(e).__name__)
