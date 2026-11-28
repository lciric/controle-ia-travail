"""Différentiel de comportement, vérification neuve du module v3 (addendum 2 de P3).

1. Fonction pure v2 contre v3 sur chaque scénario synthétique des tests v3 (`SCENARIOS`, tables jouets seulement) :
   sorties sérialisées comparées ; seule différence admise : `audit_symetrie_addendum2.part_hors_bornes` et ce qui en
   découle (déclencheur, lecture, consigne, ligne de la recommandation), et seulement si la part de P3-P1 est en échec.
2. Déclencheur 3, v1 contre v3, sur des entrées construites et tirées au hasard (états de M5, E0, part en échec ou non,
   D / E0 dans et hors de [−1 ; 1], bords ±1) : `part_hors_bornes` identique (v1 n'a pas la clé `consigne`).
3. `principales_du_run` v2 contre v3 : cas sain identique ; pannes : v2 lève une exception nue, v3 une `GardeArret`
   « garde 7 ».
Aucune donnée réelle : le garde R1 v2b est chargé avant tout import (journal : variable REVUE_JOURNAL_R1).
Usage (depuis la racine du dépôt, PYTHONPATH=src:<outils>) : python -B differentiel_v1_v2_v3.py
"""
import sys

sys.dont_write_bytecode = True
import garde_r1_v2b  # noqa: E402,F401  (crochet d'audit R1 actif dès ici)

import copy  # noqa: E402
import importlib.util  # noqa: E402
import json  # noqa: E402
import random  # noqa: E402
from pathlib import Path  # noqa: E402

S = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum2-p3")
BASE = S / "verification-v3" / "base"
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
sys.path.insert(0, str(BASE))

import test_audit_verdict_p3_v1 as T  # noqa: E402  (importe audit_verdict_p3_v1 = base v3)
from controle_ia.gardes import GardeArret  # noqa: E402


def charger(chemin, nom):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


v3 = T.av
v2 = charger(S / "module-v2" / "audit_verdict_p3_v1.py", "av_v2")
v1 = charger(S / "module" / "audit_verdict_p3_v1.py", "av_v1")
for m in (v1, v2, v3):
    m.TIRAGES = 2000
print("modules :", v3.__file__, v2.__file__, v1.__file__)


def ecarts(a, b, chemin=""):
    if isinstance(a, dict) and isinstance(b, dict):
        out = []
        for k in sorted(set(a) | set(b), key=str):
            if k not in a or k not in b:
                out.append(f"{chemin}/{k} : présent d'un seul côté")
            else:
                out += ecarts(a[k], b[k], f"{chemin}/{k}")
        return out
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return [f"{chemin} : longueurs {len(a)} et {len(b)}"]
        out = []
        for i, (x, y) in enumerate(zip(a, b)):
            out += ecarts(x, y, f"{chemin}[{i}]")
        return out
    return [] if a == b else [f"{chemin} : {a!r} ≠ {b!r}"]


# 1. v2 contre v3 sur les scénarios
G = T.G
admis = ("/audit_symetrie_addendum2/part_hors_bornes", "/audit_symetrie_addendum2/declencheur",
         "/audit_symetrie_addendum2/lecture", "/audit_symetrie_addendum2/consigne", "/recommandation_au_verdict_R13")
bilan = {}
for nom in T.SCENARIOS:
    s, lec = T._cas(nom)
    try:
        o3 = json.loads(json.dumps(v3.analyser_addendum2(copy.deepcopy(s), copy.deepcopy(lec), G), ensure_ascii=False))
    except GardeArret as e:
        o3 = {"GardeArret": str(e)}
    try:
        o2 = json.loads(json.dumps(v2.analyser_addendum2(copy.deepcopy(s), copy.deepcopy(lec), G), ensure_ascii=False))
    except GardeArret as e:
        o2 = {"GardeArret": str(e)}
    d = ecarts(o2, o3)
    part = (((o3.get("descriptifs") or {}).get("B1") or {}).get("saboteur-honnete") or {}).get("part_des_formes", {})
    etat_part = (part.get("part") or {}).get("etat")
    hors = [x for x in d if not x.startswith(admis)]
    bilan[nom] = {"ecarts": len(d), "hors_admis": hors, "etat_part_P3P1": etat_part,
                  "d3_v2": (o2.get("audit_symetrie_addendum2") or {}).get("part_hors_bornes"),
                  "d3_v3": (o3.get("audit_symetrie_addendum2") or {}).get("part_hors_bornes")}
    print(f"[1] {nom:16s} écarts {len(d):3d} ; hors admis {len(hors)} ; part P3-P1 : {etat_part} ; "
          f"d3 v2 {bilan[nom]['d3_v2'] and bilan[nom]['d3_v2'].get('etat')!r} → v3 "
          f"{bilan[nom]['d3_v3'] and bilan[nom]['d3_v3'].get('etat')!r}")
    if d and etat_part != v3.ECHEC:
        print("    ÉCART HORS PART EN ÉCHEC :", d[:5])
    for x in hors[:5]:
        print("    hors admis :", x)

# 2. déclencheur 3, v1 contre v3
L = T._faux_L()
P = T.P


def contrastes(etat_m5, D, E0, etat_part):
    if etat_m5 != v3.CALCULE:
        pf = {"etat": etat_m5, "motif": "simulé"}
    else:
        part = {"etat": etat_part, "motif": "simulé"}
        if etat_part == v3.CALCULE and E0 != 0:
            part.update(valeur=D / E0, bas=0.0, haut=1.0, tirages=2000, degeneres=0)
        pf = {"etat": v3.CALCULE, "D": {"valeur": D}, "E0": {"valeur": E0}, "part": part}
    c = T._faux_contrastes(0.6, 0.5)
    c["saboteur-honnete"]["part_des_formes"] = pf
    return c


rng = random.Random(20261020)
cas = []
for etat_m5 in (v3.CALCULE, v3.NON_CALCULABLE, v3.ECHEC):
    for etat_part in (v3.CALCULE, v3.ECHEC, v3.NON_CALCULABLE):
        for D, E0 in [(0.5, 0.5), (0.5, -0.5), (0.6, 0.5), (-0.6, 0.5), (0.4, 0.5), (0.5, 0.0), (0.0, 0.3),
                      (0.5, 2 / 21), (1e-9, 1e-9)] + [(rng.uniform(-2, 2), rng.choice([0.0, rng.uniform(-1, 1)]))
                                                     for _ in range(60)]:
            cas.append((etat_m5, D, E0, etat_part))
diff = 0
vrais_en_echec = 0
phrases = set()
for etat_m5, D, E0, etat_part in cas:
    c = contrastes(etat_m5, D, E0, etat_part)
    a1 = v1.audit_symetrie(L, copy.deepcopy(c), {}, P)
    a3 = v3.audit_symetrie(L, copy.deepcopy(c), {}, P)
    # la phrase `lecture` a changé entre v1 et v2 (CC-texte-08 : consigne sortie de la phrase) : comparée à part
    if a1["part_hors_bornes"] != a3["part_hors_bornes"] or a1["declencheur"] != a3["declencheur"] \
            or (a1["lecture"] is None) != (a3["lecture"] is None):
        diff += 1
        print("[2] ÉCART v1/v3 :", etat_m5, D, E0, etat_part, a1["part_hors_bornes"], a3["part_hors_bornes"])
    phrases.add((a1["lecture"], a3["lecture"]))
    if etat_m5 == v3.CALCULE and etat_part == v3.ECHEC and a3["part_hors_bornes"]["etat"] is True:
        vrais_en_echec += 1
        assert a3["declencheur"] is True and a3["consigne"] == v3.CONSIGNE_AUDIT
print(f"[2] déclencheur 3, v1 contre v3 : {len(cas)} cas, {diff} écart(s) ; "
      f"part en échec et part ponctuelle hors bornes : {vrais_en_echec} cas, tous déclenchés avec la consigne")
print(f"[2] phrases (v1, v3) rencontrées : {sorted(phrases, key=str)}")

# 3. principales_du_run, v2 contre v3
s, _ = T._cas("sain")
assert v2.principales_du_run(s) == v3.principales_du_run(s) == list(P)
pannes = {"principales absente": lambda sf: sf.pop("principales"),
          "enjeux absente": lambda sf: sf["principales"].pop("enjeux"),
          "tromperie = None": lambda sf: sf["principales"].__setitem__("tromperie", None),
          "enjeux = 3": lambda sf: sf["principales"].__setitem__("enjeux", 3),
          "enjeux vide": lambda sf: sf["principales"].__setitem__("enjeux", ""),
          "principales = liste": lambda sf: sf.__setitem__("principales", ["a", "b"]),
          "[SF] absent": None}
for nom, f in pannes.items():
    x, _ = T._cas("sain")
    if f is None:
        x.pop("sondes-figees")
    else:
        f(x["sondes-figees"])
    res = []
    for m in (v2, v3):
        try:
            r = m.principales_du_run(x)
            res.append(f"rendu {r!r}")
        except Exception as e:
            res.append(f"{type(e).__name__} : {str(e)[:90]}")
    print(f"[3] {nom:20s} v2 → {res[0]} | v3 → {res[1]}")
print("fin")
