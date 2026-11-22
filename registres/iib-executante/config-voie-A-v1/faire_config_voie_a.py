"""Configuration de la voie (A) : égale à la configuration scellée de l'étalonnage (08e22099…) sauf cinq clés
(go_id, code, entropie, offre.etiquette, instances_intouchables). Usage :
python3 -I faire_config_voie_a.py DEPOT COMMIT_CODE BRANCHE_CODE ENTROPIE INTOUCHABLES(csv) SORTIE.json
"""
import hashlib
import json
import subprocess
import sys

depot, commit, branche, entropie, intouch, sortie = sys.argv[1:7]
ANCIENNE = "docs/notes/barreau8-iib-v1/config-iib-organisme-retenu-v5-etalonnage-v2.json"
brut = subprocess.run(["git", "-C", depot, "show", f"43d6d0673edd5055917f536e5310ea99c15ab75e:{ANCIENNE}"], capture_output=True, check=True).stdout
assert hashlib.sha256(brut).hexdigest() == "08e22099d3be9bb8313610379f71ddafaf0e5d77117a1c9cbaadb457304dd363"
c = json.loads(brut)
mod = c["code"]["module_de_lecture"]["chemin"]
contenu = subprocess.run(["git", "-C", depot, "show", f"{commit}:{mod}"], capture_output=True, check=True).stdout
assert (entropie == "VIDE" or int(entropie) > 0) and len(commit) == 40
c["go_id"] = "GO-2026-11-22-75"
c["code"] = {**c["code"], "branche": branche, "commit": commit,
             "module_de_lecture": {"chemin": mod, "sha256": hashlib.sha256(contenu).hexdigest()}}
c["entropie"] = None if entropie == "VIDE" else int(entropie)   # VIDE : tirée par la mère au scellement
c["offre"]["etiquette"] = "iib-voie-a-v1"
c["instances_intouchables"] = [int(x) for x in intouch.split(",")]
# le marqueur des empreintes du code suit le module de lecture (même forme que la configuration scellée)
if "EMPREINTES_CODE_IIB" in c.get("marqueurs", {}):
    c["marqueurs"]["EMPREINTES_CODE_IIB"] = f"{mod} {hashlib.sha256(contenu).hexdigest()}"
texte = json.dumps(c, ensure_ascii=False, indent=1) + "\n"
open(sortie, "w", encoding="utf-8").write(texte)
print(hashlib.sha256(texte.encode()).hexdigest())
