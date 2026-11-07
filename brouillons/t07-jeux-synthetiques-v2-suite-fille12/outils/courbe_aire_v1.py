#!/usr/bin/env python3
"""Courbe de l'aire (sac de mots, une tâche laissée de côté) selon le nombre de tâches — lecture seule, règles du script officiel
inchangées. Usage : courbe_aire_v1.py DOSSIER_ASSEMBLE [N …]  (défaut 8 16 24 32). Préfixes = les N premières tâches dans l'ordre du
fichier des énoncés (rangs 0..N-1). Écrit un JSON. Déterministe, sans tirage (aucune graine nécessaire ; l'assemblage a la graine 20261105)."""
import importlib.util, json, sys
from pathlib import Path
RACINE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RACINE / "src"))
spec = importlib.util.spec_from_file_location("v", RACINE / "scripts/verifier_jeux_synthetiques_t07_v2.py")
v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
d = Path(sys.argv[1]); ns = [int(x) for x in sys.argv[2:]] or [8, 16, 24, 32]
ordre = [json.loads(l)["identifiant"] for l in open(d / "enonces-reserve-v2.jsonl")]
recs = [json.loads(l) for l in open(d / "intention-autres-modes-v2.jsonl")]
sortie = {}
for n in ns:
    ok = set(ordre[:n]); r = {}
    for mode in ("controles", "direction"):
        for nom, ext in (("entiere", lambda s: s["reponse"]), ("avant_COST", v.empan_avant)):
            docs, et, ta = [], [], []
            for s in recs:
                if s["mode"] == mode and s["tache"] in ok:
                    docs.append(v.normaliser(ext(s))); et.append(s["etiquette"]); ta.append(s["tache"])
            moy, plis = v.aire_sac_de_mots(docs, et, ta)
            r[f"{mode}/{nom}"] = {"aire": round(moy, 3), "plis": plis}
    sortie[n] = r
print(json.dumps(sortie, indent=1))
