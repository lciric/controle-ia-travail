"""Contrôle de la banque `confrontation-v4` contre la v3 — v1.

Vérifie : `train` identique à celui de la v3 ; famille `conscience-evaluation` identique en test et test_final ; chaque
tâche gardée identique à celle de la v3 (identifiant, champs, ordre relatif) ; en test et test_final, aucune paire de
`controle-delegation` n'a ses deux traces (une trace par paire, champ `paire` du secret v3, pris avec la source : les numéros de paire se répètent d'un lot à l'autre), et chaque paire de la v3 en
garde exactement une ; équilibre des classes par part et par source ; secret v4 = secret v3 restreint ; empreinte de la
clé au manifeste. Imprime un rapport ; code 0 si conforme, 2 sinon. N'imprime jamais la clé.

Usage : python3 -I verifier_banque_v4_v1.py BANQUE_V4 SECRET_V4 CLE_V4 BANQUE_V3 SECRET_V3
"""
import collections, hashlib, json, pathlib, sys

PARTS = ("train", "test", "test_final")
FAM = "controle-delegation"
p4, ps4, pc4, p3, ps3 = (pathlib.Path(a) for a in sys.argv[1:6])
v4, s4, c4, v3, s3 = (json.loads(p.read_text(encoding="utf-8")) for p in (p4, ps4, pc4, p3, ps3))
err = []
if v4["train"] != v3["train"]:
    err.append("train différent de la v3")
r = {"banque": p4.name, "sha256": hashlib.sha256(p4.read_bytes()).hexdigest(), "parts": {}}
for part in ("test", "test_final"):
    a4 = [t for t in v4[part] if t["famille"] != FAM]
    a3 = [t for t in v3[part] if t["famille"] != FAM]
    if a4 != a3:
        err.append(f"{part} : famille conscience-evaluation différente de la v3")
    ids3 = [t["id"] for t in v3[part]]
    par3 = {t["id"]: t for t in v3[part]}
    for t in v4[part]:
        if par3.get(t["id"]) != t:
            err.append(f"{part} {t['id']} : tâche différente de la v3 ou absente")
    pos = [ids3.index(t["id"]) for t in v4[part] if t["id"] in par3]
    if pos != sorted(pos):
        err.append(f"{part} : ordre relatif différent de la v3")
    paires_v3 = collections.defaultdict(list)
    for t in v3[part]:
        if t["famille"] == FAM:
            paires_v3[(t["source"], s3[t["id"]]["paire"])].append(t["id"])  # le numéro de paire se répète d'un lot à l'autre
    garde = {t["id"] for t in v4[part] if t["famille"] == FAM}
    for pid, membres in paires_v3.items():
        k = sum(m in garde for m in membres)
        if k != 1:
            err.append(f"{part} : paire {pid} avec {k} traces gardées")
    cl = collections.Counter((t["source"], t["verite"]) for t in v4[part] if t["famille"] == FAM)
    r["parts"][part] = {"n": len(v4[part]), "delegation": dict(sorted((f"{a}|{b}", n) for (a, b), n in cl.items())),
                        "conscience": len(a4)}
    for src in {s for s, _ in cl}:
        if abs(cl[(src, "honnete")] - cl[(src, "sabotage")]) > 1:
            err.append(f"{part} : source {src} déséquilibrée")
ids4 = {t["id"] for p in PARTS for t in v4[p]}
if set(s4) != ids4 or any(s4[k] != s3[k] for k in s4):
    err.append("secret v4 différent du secret v3 restreint")
e = int(c4["entropie_seed_sequence"])
if hashlib.sha256(str(e).encode("ascii")).hexdigest() != v4["manifeste"]["une_trace_par_paire"]["entropie_sha256"]:
    err.append("empreinte de la clé différente de celle du manifeste")
if str(e) in p4.read_text(encoding="utf-8"):
    err.append("la clé apparaît en clair dans la banque")
r["erreurs"] = err
print(json.dumps(r, ensure_ascii=False, indent=1))
sys.exit(2 if err else 0)
