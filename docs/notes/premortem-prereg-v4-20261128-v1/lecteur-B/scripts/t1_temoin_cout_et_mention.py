"""Témoin T1 : recalcul, depuis les 64 mesures.jsonl (commit 42cdfcf29) et par la définition scellée `cout_lisible`
(src/controle_ia/t06/cout.py), des coûts illisibles de `honnete` et `consigne_neutre` et de la part de
`mention_texte_prive` de `consigne_neutre`, `gonfle_3`, `gonfle_5` ; comparaison au résultat scellé
(lecture-cout-dose-reponse.json, 70baf0e6…). Comptes et taux seulement ; aucun seuil réglé."""
import hashlib, json, sys
from collections import Counter, defaultdict
from pathlib import Path
from controle_ia.t06.cout import cout_lisible

blocs = Path(sys.argv[1]); scelle = Path(sys.argv[2])
n = Counter(); illis = Counter(); mention = Counter(); plusieurs = Counter(); nuls = Counter(); tronq = Counter()
empreintes_ok = 0
for d in sorted(blocs.iterdir()):
    bloc = json.loads((d / "bloc.json").read_text())
    brut = (d / "mesures.jsonl").read_bytes()
    assert hashlib.sha256(brut).hexdigest() == bloc["fichiers"]["mesures.jsonl"], d.name
    empreintes_ok += 1
    for ligne in brut.decode().splitlines():
        m = json.loads(ligne); c = m["condition"]
        n[c] += 1
        illis[c] += not cout_lisible(m["cout"])
        nuls[c] += (m["cout"] == 0)
        mention[c] += bool(m["mention_texte_prive"])
        plusieurs[c] += bool(m["cout_plusieurs_nombres"])
        tronq[c] += bool(m["tronquee"])
res = json.loads(scelle.read_text())["resultat"]["manipulation"]
sortie = {"blocs": empreintes_ok, "actions": sum(n.values()), "empreinte_scelle": hashlib.sha256(scelle.read_bytes()).hexdigest(), "lignes": []}
ok = True
for c in ("honnete", "consigne_neutre", "gonfle_2", "gonfle_3", "gonfle_5"):
    l = {"condition": c, "actions": n[c], "illisibles_recalcule": illis[c], "illisibles_scelle": res[c]["illisibles"],
         "part_illisible": illis[c] / n[c], "dont_cout_nul": nuls[c],
         "mention_recalcule": mention[c], "part_mention_recalcule": mention[c] / n[c],
         "part_mention_scelle": res[c]["part_mention_texte_prive"],
         "part_plusieurs_nombres": plusieurs[c] / n[c], "tronquees_recalcule": tronq[c], "tronquees_scelle": res[c]["tronquees"]}
    l["conforme"] = (illis[c] == res[c]["illisibles"] and mention[c] / n[c] == res[c]["part_mention_texte_prive"] and tronq[c] == res[c]["tronquees"])
    ok &= l["conforme"]; sortie["lignes"].append(l)
p = {l["condition"]: l["part_mention_recalcule"] for l in sortie["lignes"]}
sortie["ecarts_mention_contre_consigne_neutre"] = {"gonfle_3": p["gonfle_3"] - p["consigne_neutre"], "gonfle_5": p["gonfle_5"] - p["consigne_neutre"], "gonfle_2": p["gonfle_2"] - p["consigne_neutre"]}
sortie["temoin_T1_conforme"] = ok
print(json.dumps(sortie, indent=1, ensure_ascii=False))
