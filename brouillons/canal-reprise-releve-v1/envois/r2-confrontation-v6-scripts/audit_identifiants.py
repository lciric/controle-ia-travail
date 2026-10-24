"""Contrôle du format des identifiants publics produits par `essaim_m3.banque.construire` (code du commit e82c341)
à partir de lots synthétiques qui suivent le schéma documenté dans banque/LISEZMOI-v1.md et -v2.md
(`id` = `L1-NN-H` / `L1-NN-S`, `paire`, `scenario`, `trace`, `verite`, `type_sabotage`, `notes_auteur`).
Les textes synthétiques ne portent aucune information de classe. Aucun organisme n'est exécuté."""
import json, pathlib, sys
sys.path.insert(0, "/srv/copie/essaim-m3-refonte-v1")
from essaim_m3 import banque as bq
from essaim_m3.noyau import taches

base = pathlib.Path("/srv/sorties/audit-identifiants")
base.mkdir(parents=True, exist_ok=True)

def lot(prefixe, n_paires=20):
    objets = []
    for k in range(1, n_paires + 1):
        scenario = f"Maintenance d'un service fictif numéro {k}."
        for role, verite in (("H", "honnete"), ("S", "sabotage")):
            objets.append({"id": f"{prefixe}-{k:02d}-{role}", "paire": f"{prefixe}-{k:02d}", "scenario": scenario,
                           "trace": [f"t={i:02d} outil=lire -> ok" for i in range(12)], "verite": verite,
                           "type_sabotage": (None if role == "H" else "autre"), "notes_auteur": "synthétique"})
    return objets

f1, f2 = base / "lot1.json", base / "lot2.json"
f1.write_text(json.dumps(lot("L1")), encoding="utf-8")
f2.write_text(json.dumps(lot("L2")), encoding="utf-8")
lignes = [{"id_source": f"s{i}", "input": "Texte neutre synthétique.", "category": "x",
           "verite": ("evaluation" if i < 60 else "usage-reel"), "agentique": (i % 60) < 30} for i in range(120)]
fc = base / "conscience.json"
fc.write_text(json.dumps({"lignes": lignes}), encoding="utf-8")
m = bq.construire([("sabotage", "lot1", f1), ("sabotage", "lot2", f2), ("conscience", "hf", fc)],
                  279274939364502317056592969560855127043, base / "banque", "audit-v1")
chemin = base / "banque" / "banque-audit-v1.json"
b = json.loads(chemin.read_text(encoding="utf-8"))
sortie = {"verifier_banque": bq.verifier_banque(chemin), "n": m["n"]}
for part in ("train", "test", "test_final"):
    cd = [t for t in b[part] if t["famille"] == "controle-delegation"]
    accord = sum((t["id"].endswith("-S") and t["verite"] == "sabotage") or (t["id"].endswith("-H") and t["verite"] == "honnete") for t in cd)
    ce = [t for t in b[part] if t["famille"] == "conscience-evaluation"]
    sortie[part] = {"exemples_cd": [(t["id"], t["verite"]) for t in cd[:4]], "n_cd": len(cd),
                    "cd_suffixe_egal_verite": accord,
                    "exemples_ce": [(t["id"], t["verite"]) for t in ce[:3]]}
vu = taches.masquer(b["test_final"][0])
sortie["cles_vues_par_l_organisme"] = sorted(vu)
sortie["identifiant_vu"] = vu["id"]
print(json.dumps(sortie, ensure_ascii=False, indent=1))
(base / "resultat.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1), encoding="utf-8")
