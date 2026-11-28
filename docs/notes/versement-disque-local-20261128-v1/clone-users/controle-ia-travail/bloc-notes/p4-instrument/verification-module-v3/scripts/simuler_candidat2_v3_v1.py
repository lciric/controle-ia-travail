"""Simulation independante (pas un candidat) : le candidat 1, puis les paires fixes de `ecrire_candidat2_v1.py` (lues
par l'arbre syntaxique, sans executer l'ecrivain), les six lignes « Module de P4 » aux empreintes du module v3, la paire
T2 avec TESTS_ATTENDUS, la paire T3 (empreintes des scripts de la chaine v2), puis les paires JSON dans deux ordres :
(1) chaine v2 puis module v3 ; (2) module v3 puis chaine v2. Chaque ancre doit etre trouvee une seule fois au moment
ou elle s'applique. Controles sur le texte obtenu : validateur gele, garde de table du module v3, lignes « Module de
P4 » relues par `lignes_module`, « Tests attendus : `N` » lu comme la chaine (une seule fois).

Usage : python -B simuler_candidat2_v3_v1.py COPIE_V3 CANDIDAT1 ECRIVAIN MODULE_V3 CHAINE_V2 PAIRES_CHAINE PAIRES_V3
        TESTS_ATTENDUS SORTIE_MD SORTIE_JSON
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import ast  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
from pathlib import Path  # noqa: E402

(COPIE, CAND, ECRIVAIN, MODULE, CHAINE, PCH, PV3, TESTS, SMD, SJS) = sys.argv[1:11]
sys.path.insert(0, COPIE)
import instrument_p4_v1 as ip  # noqa: E402
import lecture_p4_v1 as lp  # noqa: E402
from controle_ia.prereg import problemes  # noqa: E402

arbre = ast.parse(Path(ECRIVAIN).read_text(encoding="utf-8"))
val = {}
for n in arbre.body:
    if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
        if n.targets[0].id in ("PAIRES_FIXES", "ANCIENNES", "NOMS_MODULE", "DOSSIER"):
            val[n.targets[0].id] = ast.literal_eval(n.value)


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def appliquer(t: str, paires, journal: list) -> str:
    for a, b, s in paires:
        n = t.count(a)
        journal.append({"source": s, "compte": n})
        if n != 1:
            raise SystemExit(f"{s} : ancre trouvée {n} fois")
        t = t.replace(a, b)
    return t


def simuler(ordre: str):
    j = []
    t = Path(CAND).read_text(encoding="utf-8")
    t = appliquer(t, val["PAIRES_FIXES"], j)
    t = appliquer(t, [(f"Module de P4 : `{val['DOSSIER']}/{n}` : `{val['ANCIENNES'][n]}`",
                       f"Module de P4 : `{val['DOSSIER']}/{n}` : `{sha(Path(MODULE) / n)}`", f"module {n}")
                      for n in val["NOMS_MODULE"]], j)
    t = appliquer(t, [("- Tests attendus : 1 102, soit", f"- Tests attendus : `{TESTS}`, soit", "T2")], j)
    amorce, instance = Path(CHAINE) / "amorce_instance_p4_v1.sh", Path(CHAINE) / "p4_instance_v1.sh"
    t = appliquer(t, [("- Run source (P3) : ",
                       f"- Scripts de l'instance, gelés par le scellement : `{val['DOSSIER']}/amorce_instance_p4_v1.sh` "
                       f"(`{sha(amorce)}`, sha256) ; `{val['DOSSIER']}/p4_instance_v1.sh` (`{sha(instance)}`, sha256).\n"
                       "- Lancement : `PREREG=prereg/P4-instrument-v1.md`, `BRANCHE=calcul/p4-reel-v1`.\n- Run source (P3) : ",
                       "T3")], j)
    pch = [(p["ancien"], p["nouveau"], p.get("source", "chaîne")) for p in json.loads(Path(PCH).read_text(encoding="utf-8"))]
    pv3 = [(p["ancien"], p["nouveau"], p.get("source", "module v3")) for p in json.loads(Path(PV3).read_text(encoding="utf-8"))]
    t = appliquer(t, pch + pv3 if ordre == "chaîne puis module" else pv3 + pch, j)
    return t, j


res = {}
for ordre in ("chaîne puis module", "module puis chaîne"):
    t, j = simuler(ordre)
    res[ordre] = {"comptes": [x["compte"] for x in j], "n_paires": len(j), "sha256": hashlib.sha256(t.encode()).hexdigest()}
    if ordre == "chaîne puis module":
        texte = t
        journal = j
assert res["chaîne puis module"]["sha256"] == res["module puis chaîne"]["sha256"], "l'ordre change le texte"
Path(SMD).write_text(texte, encoding="utf-8")
lm = ip.lignes_module(texte)
attendus = re.findall(r"Tests attendus : `([0-9]+)`", texte)
sortie = {
    "candidat1_sha256": sha(CAND), "ecrivain_sha256": sha(ECRIVAIN), "paires_chaine_sha256": sha(PCH),
    "paires_v3_sha256": sha(PV3), "ordres": res, "meme_texte_dans_les_deux_ordres": True,
    "journal": journal,
    "table": lp.exiger_table_des_criteres(texte),
    "validateur": problemes(SMD),
    "lignes_module_egales_v3": {c: (s == sha(Path(MODULE) / Path(c).name)) for c, s in lm.items()},
    "tests_attendus": attendus, "lignes_tests_attendus": texte.count("Tests attendus : `"),
    "ligne_tests_attendus": [x for x in texte.split("\n") if "Tests attendus : `" in x],
    "simulation_sha256": sha(SMD),
}
Path(SJS).write_text(json.dumps(sortie, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in sortie.items() if k != "journal"}, ensure_ascii=False, indent=1))
