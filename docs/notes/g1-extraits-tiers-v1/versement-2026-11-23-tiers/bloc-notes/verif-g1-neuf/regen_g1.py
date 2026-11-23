import importlib.util, json, sys, hashlib
from pathlib import Path
D = Path("/home/user/controle-ia-travail")
spec = importlib.util.spec_from_file_location("ex", D/"docs/notes/g1-extraits-tiers-v1/outils/extraire_v4.py")
ex = importlib.util.module_from_spec(spec); spec.loader.exec_module(ex)
for nom in sys.argv[1:]:
    chemin = "docs/notes/g1-extraits-tiers-v1/fiches/"+nom
    fiche = json.loads((D/chemin).read_text(encoding="utf-8"))
    texte = ex.fabriquer(fiche, chemin)
    actuel = (D/fiche["sortie"]).read_bytes()
    side = (D/(fiche["sortie"]+".sha256")).read_text().split()[0]
    print(nom, "identique" if texte.encode()==actuel else "DIFFERENT", hashlib.sha256(actuel).hexdigest()[:16], "compagnon", hashlib.sha256(actuel).hexdigest()==side)
