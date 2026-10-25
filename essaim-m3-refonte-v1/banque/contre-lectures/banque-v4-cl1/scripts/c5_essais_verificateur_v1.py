"""Contre-lecture banque v4 — c5 : le contrôle `verifier_banque_v4_v1.py` sur des artefacts (R5) — v1.
Artefacts écrits sous le dossier de travail de la contre-lecture, jamais dans le dépôt :
  A1 une paire de test garde ses deux traces (jumelle remise) ;
  A2 sélection permutée : dans une source de test, une paire « honnête gardée » et une paire « sabotée gardée »
     échangent leur trace gardée (équilibre intact, tirage non conforme à la clé) ;
  A3 secret v4 avec une entrée de trop (la jumelle retirée) ;
  A4 identique à la v4 (cas sain).
Usage : python3 -I -B c5_essais_verificateur_v1.py DOSSIER_BANQUE DOSSIER_ARTEFACTS
"""
import json, pathlib, subprocess, sys

B, D = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
D.mkdir(parents=True, exist_ok=True)
FAM = "controle-delegation"
v3 = json.loads((B / "banque-confrontation-v3.json").read_text(encoding="utf-8"))
s3 = json.loads((B / "banque-confrontation-v3-secret.json").read_text(encoding="utf-8"))
v4 = json.loads((B / "banque-confrontation-v4.json").read_text(encoding="utf-8"))
s4 = json.loads((B / "banque-confrontation-v4-secret.json").read_text(encoding="utf-8"))
ids4 = {t["id"] for p in ("train", "test", "test_final") for t in v4[p]}
paires = {}
for t in v3["test"]:
    if t["famille"] == FAM:
        paires.setdefault((t["source"], s3[t["id"]]["paire"]), []).append(t)


def jumelle(t):
    return next(x for x in paires[(t["source"], s3[t["id"]]["paire"])] if x["id"] != t["id"])


def ecrire(nom, banque, secret):
    pb, ps = D / f"{nom}-banque.json", D / f"{nom}-secret.json"
    pb.write_text(json.dumps(banque, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    ps.write_text(json.dumps(secret, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return pb, ps


def ordonner(liste):
    rang = {t["id"]: i for i, t in enumerate(v3["test"])}
    return sorted(liste, key=lambda t: rang[t["id"]])


gardees = [t for t in v4["test"] if t["famille"] == FAM]
# A1
a1 = json.loads(json.dumps(v4)); j = jumelle(gardees[0])
a1["test"] = ordonner(a1["test"] + [j])
s_a1 = dict(s4); s_a1[j["id"]] = s3[j["id"]]
# A2 : même source, classes opposées
src = gardees[0]["source"]
h = next(t for t in gardees if t["source"] == src and t["verite"] == "honnete")
s = next(t for t in gardees if t["source"] == src and t["verite"] == "sabotage")
a2 = json.loads(json.dumps(v4))
a2["test"] = ordonner([t for t in a2["test"] if t["id"] not in (h["id"], s["id"])] + [jumelle(h), jumelle(s)])
s_a2 = {k: v for k, v in s4.items() if k not in (h["id"], s["id"])}; s_a2[jumelle(h)["id"]] = s3[jumelle(h)["id"]]; s_a2[jumelle(s)["id"]] = s3[jumelle(s)["id"]]
s_a2 = {k: s_a2[k] for k in sorted(s_a2)}
# A3
s_a3 = dict(s4); s_a3[j["id"]] = s3[j["id"]]
res = {}
for nom, banque, secret in (("A1-paire-a-deux-traces", a1, s_a1), ("A2-selection-permutee", a2, s_a2), ("A3-secret-en-trop", v4, s_a3), ("A4-sain", v4, s4)):
    pb, ps = ecrire(nom, banque, secret)
    r = subprocess.run([sys.executable, "-I", "-B", str(B / "construction-v4" / "verifier_banque_v4_v1.py"), str(pb), str(ps),
                        str(B / "banque-confrontation-v4-cle.json"), str(B / "banque-confrontation-v3.json"), str(B / "banque-confrontation-v3-secret.json")],
                       capture_output=True, text=True)
    try:
        err = json.loads(r.stdout)["erreurs"]
    except Exception:
        err = ["sortie illisible : " + r.stderr[-300:]]
    res[nom] = {"code": r.returncode, "n_erreurs": len(err), "erreurs": [e.split(" : ")[-1] if "t-" in e else e for e in err][:4]}
print(json.dumps(res, ensure_ascii=False, indent=1))
