"""Contrôle de la banque `confrontation-v5` contre la v4 et la v3 — v1.

Vérifie : la sélection de la v4 se recalcule depuis sa clé (fonction du constructeur de la v5, non-régression) ; chaque
tâche de la v5 est la tâche de la v4 nommée par `id_v3` du secret (champs `famille`, `texte`, `etiquettes`, `verite`,
`source` égaux ; même part) et la v5 couvre exactement les 176 tâches de la v4 ; identifiants recalculés depuis la clé
v5 ; chaque part triée par identifiant ; secret v5 = secret v3 de la tâche + `id_v3` ; `comptes_par_strate` et `n` du
manifeste recalculés ; empreinte de la clé ; la clé n'apparaît pas dans la banque ; aucun identifiant v1 ni v3 dans la
banque. Code 0 si conforme, 2 sinon. N'imprime jamais une clé ni un identifiant v1 ou v3.

Usage : python3 -I verifier_banque_v5_v1.py DOSSIER_BANQUE
"""
import hashlib, importlib.util, json, pathlib, re, sys
import numpy as np

PARTS = ("train", "test", "test_final")
FAM = "controle-delegation"
d = pathlib.Path(sys.argv[1])
lire = lambda n: json.loads((d / n).read_text(encoding="utf-8"))
v3, s3 = lire("banque-confrontation-v3.json"), lire("banque-confrontation-v3-secret.json")
v4, c4 = lire("banque-confrontation-v4.json"), lire("banque-confrontation-v4-cle.json")
v5, s5, c5 = lire("banque-confrontation-v5.json"), lire("banque-confrontation-v5-secret.json"), lire("banque-confrontation-v5-cle.json")
spec = importlib.util.spec_from_file_location("constructeur_v5", d / "construction-v5" / "construire_banque_v5_v1.py")
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
err = []
garde = mod.selection_v4(v3, s3, int(c4["entropie_seed_sequence"]))
if garde != {t["id"] for p in ("test", "test_final") for t in v4[p] if t["famille"] == FAM}:
    err.append("sélection de la v4 non retrouvée depuis sa clé")
par4 = {t["id"]: (p, t) for p in PARTS for t in v4[p]}
vus = set()
for p in PARTS:
    ids = [t["id"] for t in v5[p]]
    if ids != sorted(ids):
        err.append(f"{p} : non triée par identifiant")
    for t in v5[p]:
        sec = s5.get(t["id"]) or {}
        i3 = sec.get("id_v3")
        if i3 not in par4:
            err.append(f"{t['id']} : id_v3 absent ou hors de la v4"); continue
        p4, t4 = par4[i3]
        vus.add(i3)
        if p4 != p:
            err.append(f"{t['id']} : part différente de la v4")
        for k in ("famille", "texte", "etiquettes", "verite", "source"):
            if t[k] != t4[k]:
                err.append(f"{t['id']} : champ {k} différent de la v4")
        attendu = dict(s3[i3]); attendu["id_v3"] = i3
        if sec != attendu:
            err.append(f"{t['id']} : dossier secret différent du secret v3 + id_v3")
if vus != set(par4):
    err.append(f"tâches de la v4 non couvertes : {len(set(par4) - vus)}")
ordre4 = [t["id"] for p in PARTS for t in v4[p]]
e5 = int(c5["entropie_seed_sequence"])
perm = np.random.default_rng(np.random.SeedSequence(e5)).permutation(len(ordre4))
attendus = {f"q-{int(perm[i]) + 1:04d}": ordre4[i] for i in range(len(ordre4))}
if attendus != {k: v["id_v3"] for k, v in s5.items()}:
    err.append("identifiants non conformes à la règle et à la clé v5")
if hashlib.sha256(str(e5).encode("ascii")).hexdigest() != v5["manifeste"]["identifiants_opaques"]["entropie_sha256"]:
    err.append("empreinte de la clé v5 différente de celle du manifeste")
texte_banque = (d / "banque-confrontation-v5.json").read_text(encoding="utf-8")
if str(e5) in texte_banque or c4["entropie_seed_sequence"] in texte_banque:
    err.append("une clé apparaît en clair dans la banque")
if re.search(r"(cd-lot[12]-L[12]-[0-9]+-[HS]|ce-hf-[0-9]{4}|\"t-[0-9]{4}\")", texte_banque):
    err.append("un identifiant v1 ou v3 apparaît dans la banque")
comptes = {}
for p in PARTS:
    for t in v5[p]:
        mode = "agentique" if s5[t["id"]].get("agentique") else "conversation"
        k = f"{t['famille']}|{t['verite']}|{t['source']}|{mode}"
        comptes.setdefault(k, {q: 0 for q in PARTS})[p] += 1
if v5["manifeste"]["comptes_par_strate"] != {k: comptes[k] for k in sorted(comptes)}:
    err.append("comptes_par_strate du manifeste faux")
if v5["manifeste"]["n"] != {p: len(v5[p]) for p in PARTS}:
    err.append("n du manifeste faux")
r = {"banque": "banque-confrontation-v5.json", "sha256": hashlib.sha256((d / "banque-confrontation-v5.json").read_bytes()).hexdigest(),
     "n": {p: len(v5[p]) for p in PARTS}, "comptes_par_strate": comptes, "erreurs": err}
print(json.dumps(r, ensure_ascii=False, indent=1))
sys.exit(2 if err else 0)
