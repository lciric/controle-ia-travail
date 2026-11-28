import sys, json, time, tempfile
sys.dont_write_bytecode = True
sys.path.insert(0, "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/module")
from pathlib import Path
import instrument_p4_v1 as ip
import mesures_conception_p4_v1 as mc
from controle_ia.scellement import empreinte
from controle_ia.harnais.modeles import tokeniseur_caracteres_chat
depot = Path(sys.argv[1]); run3 = "20261020-120000-p3-jouet"
chemins = ip.chemins_du_run_source(run3)
chemins.update({"taches": "taches.json", "faits": "donnees/synth/faits.csv", "enjeux": "donnees/synth/enjeux.jsonl"})
emp = {k: {"chemin": c, "sha256": empreinte(depot / c)} for k, c in chemins.items()}
d = Path(tempfile.mkdtemp(dir="/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/proto"))
tokeniseur_caracteres_chat().save_pretrained(d)
t = time.time()
s = mc.mesurer(depot, d, emp, run3, empreinte(d / "tokenizer.json"))
print("duree", round(time.time() - t, 1))
print(s["MC-1"]["B_nom"], s["MC-1"]["Bprime_nom"], s["MC-1"]["seules"], s["MC-1"]["valeurs_dans_le_gabarit"])
print(s["MC-2"]["egaux"], s["MC-3"]["echecs_longueur"], s["MC-3"]["fin_presente"], s["noeud_avant_scellement"], s["identite_attendue"], s["versions_egales_a_p3"], s["format"])
txt = json.dumps(s, ensure_ascii=False)
for l in open(depot / "donnees" / run3 / "textes-actions-p3.jsonl"):
    x = json.loads(l)["texte"]
    if len(x) >= 4 and x in txt: print("TEXTE TROUVÉ", repr(x))
print(len(txt))
