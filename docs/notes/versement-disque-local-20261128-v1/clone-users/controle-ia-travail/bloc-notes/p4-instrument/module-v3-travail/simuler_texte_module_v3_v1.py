"""Simulation (pas un candidat) : les paires du module v3 appliquées au candidat 1, (a) seules, (b) après les paires fixes
de `ecrire_candidat2_v1.py`, les lignes « Module de P4 » du module v3 et la paire T2 (TESTS_ATTENDUS). Contrôles : chaque
paire trouvée une fois ; table lue par la garde du module v3 ; `prereg.problemes` vide ; lignes « Module de P4 » égales aux
empreintes du module v3 ; « Tests attendus : `N` » lu une fois, comme la chaîne.
Usage : PYTHONPATH=src:<module-v3> python -B simuler_texte_module_v3_v1.py CANDIDAT1 ECRIRE_CANDIDAT2 MODULE_V3 PAIRES SORTIE_MD N"""
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
cand1, script, module, paires_json, sortie, n = sys.argv[1:]
import lecture_p4_v1 as lp  # noqa: E402
import instrument_p4_v1 as ip  # noqa: E402
from controle_ia.prereg import problemes  # noqa: E402

spec = importlib.util.spec_from_file_location("ecrire_candidat2", script)
ec = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ec)
paires = json.loads(Path(paires_json).read_text(encoding="utf-8"))
t0 = Path(cand1).read_text(encoding="utf-8")
rapport = {"candidat1_sha256": hashlib.sha256(t0.encode()).hexdigest(), "paires": len(paires)}

# (a) seules, sur le candidat 1
t = t0
rapport["a_comptes"] = [t0.count(p["ancien"]) for p in paires]
for p in paires:
    t = ec.une(t, p["ancien"], p["nouveau"], p["source"])
rapport["a_table"] = lp.exiger_table_des_criteres(t)

# (b) chaîne complète de l'écrivain du candidat 2 (sans T3, qui exige les scripts de l'instance)
t = t0
for a, b, s in ec.PAIRES_FIXES:
    t = ec.une(t, a, b, s)
sha = {nom: hashlib.sha256((Path(module) / nom).read_bytes()).hexdigest() for nom in ec.NOMS_MODULE}
for nom in ec.NOMS_MODULE:
    t = ec.une(t, f"Module de P4 : `{ec.DOSSIER}/{nom}` : `{ec.ANCIENNES[nom]}`", f"Module de P4 : `{ec.DOSSIER}/{nom}` : `{sha[nom]}`", "module")
t = ec.une(t, "- Tests attendus : 1 102, soit", f"- Tests attendus : `{n}`, soit", "NOTES-CHAINE T2")
rapport["b_comptes"] = [t.count(p["ancien"]) for p in paires]
for p in paires:
    t = ec.une(t, p["ancien"], p["nouveau"], p["source"])
Path(sortie).write_text(t, encoding="utf-8")
rapport["b_table"] = lp.exiger_table_des_criteres(t)
rapport["b_problemes"] = problemes(sortie)
cites = ip.lignes_module(t)
rapport["b_module_egal_v3"] = cites == {f"{ec.DOSSIER}/{nom}": sha[nom] for nom in ec.NOMS_MODULE}
rapport["b_tests_attendus"] = re.findall(r"Tests attendus : `([0-9]+)`", t)
ligne = [x for x in t.split("\n") if x.startswith("- Tests attendus")]
rapport["b_ligne_tests_attendus"] = ligne
rapport["b_sortie_sha256"] = hashlib.sha256(t.encode()).hexdigest()
print(json.dumps(rapport, ensure_ascii=False, indent=1))
