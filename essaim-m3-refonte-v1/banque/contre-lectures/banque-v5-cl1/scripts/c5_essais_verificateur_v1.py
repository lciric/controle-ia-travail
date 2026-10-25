"""Contre-lecture de la v5 — c5 : essais (R5) de `construction-v5/verifier_banque_v5_v1.py` des auteurs.
Cas sain : le dossier du dépôt. Artefact A : dans `test`, deux identifiants neufs échangés entre une trace honnête et
une trace sabotée de délégation (secret échangé avec : chaque dossier suit sa tâche ; parts retriées ; compagnons
refaits) — l'équilibre, les champs, le secret et le manifeste restent justes, seule la règle des identifiants est violée.
Les clés ne sont jamais copiées : liens symboliques vers les fichiers du dépôt. Copies modifiées supprimées après usage.
Usage : python3 -I -B c5_essais_verificateur_v1.py DOSSIER_BANQUE DOSSIER_ESSAIS SORTIE"""
import hashlib, json, os, pathlib, shutil, subprocess, sys
D = pathlib.Path(sys.argv[1]).resolve(); E = pathlib.Path(sys.argv[2]); SORTIE = pathlib.Path(sys.argv[3])
V = D / "construction-v5" / "verifier_banque_v5_v1.py"
def lancer(d):
    p = subprocess.run([sys.executable, "-I", "-B", str(V), str(d)], capture_output=True, text=True, timeout=600)
    try: err = json.loads(p.stdout)["erreurs"]
    except Exception: err = ["sortie illisible"]
    return {"code": p.returncode, "erreurs": [e.split(" : ", 1)[-1] for e in err][:5], "n_erreurs": len(err),
            "sortie_sha256": hashlib.sha256(p.stdout.encode()).hexdigest()}
r = {"verificateur_sha256": hashlib.sha256(V.read_bytes()).hexdigest()}
r["sain_depot"] = lancer(D)
r["sain_depot"]["egal_a_la_sortie_des_auteurs"] = r["sain_depot"]["sortie_sha256"] == hashlib.sha256((D / "construction-v5" / "controle-banque-v5-v1.json").read_bytes()).hexdigest()
A = E / "A-echange-identifiants"; shutil.rmtree(A, ignore_errors=True); (A / "construction-v5").mkdir(parents=True)
for n in ("banque-confrontation-v3.json", "banque-confrontation-v3-secret.json", "banque-confrontation-v4.json", "banque-confrontation-v4-cle.json", "banque-confrontation-v5-cle.json"):
    os.symlink(D / n, A / n)
os.symlink(D / "construction-v5" / "construire_banque_v5_v1.py", A / "construction-v5" / "construire_banque_v5_v1.py")
b = json.loads((D / "banque-confrontation-v5.json").read_text(encoding="utf-8")); s = json.loads((D / "banque-confrontation-v5-secret.json").read_text(encoding="utf-8"))
h = next(t for t in b["test"] if t["famille"] == "controle-delegation" and t["verite"] == "honnete")
k = next(t for t in b["test"] if t["famille"] == "controle-delegation" and t["verite"] == "sabotage")
ih, ik = h["id"], k["id"]; h["id"], k["id"] = ik, ih; s[ih], s[ik] = s[ik], s[ih]
b["test"].sort(key=lambda t: t["id"])
for n, c in (("banque-confrontation-v5.json", b), ("banque-confrontation-v5-secret.json", s)):
    f = A / n; f.write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (A / (n + ".sha256")).write_text(f"{hashlib.sha256(f.read_bytes()).hexdigest()}  {n}\n", encoding="utf-8")
r["artefact_A_empreintes"] = {n: hashlib.sha256((A / n).read_bytes()).hexdigest() for n in ("banque-confrontation-v5.json", "banque-confrontation-v5-secret.json")}
r["artefact_A"] = lancer(A)
shutil.rmtree(A)
r["artefact_A_supprime"] = not A.exists()
SORTIE.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(r, ensure_ascii=False, indent=1))
