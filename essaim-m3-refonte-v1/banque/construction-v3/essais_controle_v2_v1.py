"""Essais du contrôle v2 (`verifier_identifiants_opaques_v2.py`) : cas sains et artefacts gardés, avec leurs sorties —
v1 (BC1-08 de `CONTRE-LECTURE-banque-v2-v1.md`).

Usage : python3 -I essais_controle_v2_v1.py DOSSIER_BANQUE RAPPORT_V3 DOSSIER_ARTEFACTS PYTHON
- DOSSIER_BANQUE : `essaim-m3-refonte-v1/banque` (v1, v2, v3, secrets, clé) ;
- RAPPORT_V3 : sortie du contrôle v2 sur la v3 (2 000 tirages) ; ses seuils sont repris (`--seuils`, même composition) ;
- DOSSIER_ARTEFACTS : dossier neuf (R12) où sont écrits les artefacts et les sorties ;
- PYTHON : interpréteur des essais.
Artefacts (copies de la v3, jamais servies) : A1 fuite exacte en délégation sur train et test_final, hasard sur test ;
A2 fuite juste à 80 % en délégation sur les trois parts ; A3 numéros dans l'ordre du fichier v1 (erreur de construction
plausible) ; A6 un texte modifié ; A7 un identifiant en double ; A8 une clé fausse. Plus la v1 et la v2 elles-mêmes.
Écrit `essais-controle-v2-v1.txt` : cas, code de sortie attendu, code obtenu, cases au seuil, erreurs.
"""
import hashlib, json, pathlib, subprocess, sys
import numpy as np

B, R3, A, PY = (pathlib.Path(x) for x in sys.argv[1:5])
if A.exists():
    sys.exit(f"refus : {A} existe déjà (R12)")
A.mkdir(parents=True)
V = pathlib.Path(__file__).with_name("verifier_identifiants_opaques_v2.py")
v3 = json.loads((B / "banque-confrontation-v3.json").read_text(encoding="utf-8"))
rng = np.random.default_rng(np.random.SeedSequence(20261026))


def copie(nom, b):
    p = A / nom
    p.write_text(json.dumps(b, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    p.with_name(p.name + ".sha256").write_text(f"{h}  {p.name}\n", encoding="utf-8")
    return p


def suffixe(b, juste, parts):
    b = json.loads(json.dumps(b))
    for part in ("train", "test", "test_final"):
        for t in b[part]:
            if t["famille"] != "controle-delegation":
                continue
            vrai = "S" if t["verite"] == "sabotage" else "H"
            if part in parts and rng.random() < juste:
                s = vrai
            elif part in parts:
                s = "H" if vrai == "S" else "S"
            else:
                s = "S" if rng.random() < 0.5 else "H"
            t["id"] = f"{t['id']}-{s}"
    return b


def numeros_dans_l_ordre_v1(b_v1):
    b = json.loads(json.dumps(b_v1))
    k = 0
    for part in ("train", "test", "test_final"):
        for t in b[part]:
            k += 1
            t["id"] = f"t-{k:04d}"
    return b


cas = []
a1 = copie("A1-fuite-exacte-train-et-test-final.json", suffixe(v3, 1.0, ("train", "test_final")))
a2 = copie("A2-fuite-a-80-pour-cent.json", suffixe(v3, 0.8, ("train", "test", "test_final")))
v1 = json.loads((B / "banque-confrontation-v1.json").read_text(encoding="utf-8"))
a3 = copie("A3-numeros-dans-l-ordre-du-fichier.json", numeros_dans_l_ordre_v1(v1))
b6 = json.loads(json.dumps(v3)); b6["test"][3]["texte"] += " "
a6 = copie("A6-texte-modifie.json", b6)
b7 = json.loads(json.dumps(v3)); b7["train"][0]["id"] = b7["train"][1]["id"]
a7 = copie("A7-identifiant-en-double.json", b7)
cle = {k: v for k, v in json.loads((B / "banque-confrontation-v3-cle.json").read_text(encoding="utf-8")).items() if k != "entropie_seed_sequence"}
cle_fausse = dict(cle); cle_fausse["entropie_seed_sequence"] = str(int(rng.integers(0, 2**63)) * 2**64 + int(rng.integers(0, 2**63)))  # sans lien avec la vraie clé
p_cle_fausse = A / "A8-cle-fausse.json"
p_cle_fausse.write_text(json.dumps(cle_fausse, ensure_ascii=False) + "\n", encoding="utf-8")

eq = ["--v1", str(B / "banque-confrontation-v1.json"), "--secret-v1", str(B / "banque-confrontation-v1-secret.json"),
      "--secret", str(B / "banque-confrontation-v3-secret.json")]
plan = [
    ("v1 elle-même", B / "banque-confrontation-v1.json", [], 1),
    ("v2 elle-même (ordre v1 gardé)", B / "banque-confrontation-v2.json", [], 1),
    ("A1 fuite exacte sur train et test_final, hasard sur test", a1, [], 1),
    ("A2 fuite juste à 80 % (limite de sensibilité, issue rapportée)", a2, [], None),
    ("A3 numéros dans l'ordre du fichier v1", a3, [], 1),
    ("A6 texte modifié (équivalence)", a6, eq, 2),
    ("A7 identifiant en double (équivalence)", a7, eq, 2),
    ("A8 clé fausse (équivalence)", B / "banque-confrontation-v3.json", eq + ["--cle", str(p_cle_fausse)], 2),
    ("v3 avec sa clé (équivalence)", B / "banque-confrontation-v3.json", eq + ["--cle", str(B / "banque-confrontation-v3-cle.json")], 0),
]
lignes = []
for nom, banque, extra, attendu in plan:
    out = A / ("sortie-" + hashlib.sha256(nom.encode()).hexdigest()[:8] + ".json")
    r = subprocess.run([str(PY), "-I", "-B", str(V), str(banque), "--seuils", str(R3)] + extra,
                       capture_output=True, text=True)
    out.write_text(r.stdout, encoding="utf-8")
    try:
        j = json.loads(r.stdout)
        au_seuil, erreurs = j.get("cases_au_seuil", []), j.get("erreurs", [])
    except Exception:
        au_seuil, erreurs = [], [r.stdout[:200] or r.stderr[-200:]]
    conforme = "rapporté" if attendu is None else ("conforme" if r.returncode == attendu else "NON CONFORME")
    lignes.append(f"- {nom} : code {r.returncode} (attendu {attendu if attendu is not None else 'non fixé'}) — {conforme} ; "
                  f"cases au seuil {len(au_seuil)} {au_seuil[:2]} ; erreurs {len(erreurs)} {erreurs[:1]} ; sortie {out.name}")
n_conformes = sum(1 for l in lignes if "— conforme" in l)
n_attendus = sum(1 for _, _, _, a in plan if a is not None)
entete = (f"Essais du contrôle v2 — v1 ; seuils repris de {R3.name} ({hashlib.sha256(R3.read_bytes()).hexdigest()}) ; "
          f"{n_conformes} cas conformes sur {n_attendus} à issue fixée, plus 1 cas rapporté (A2).")
(A / "essais-controle-v2-v1.txt").write_text(entete + "\n" + "\n".join(lignes) + "\n", encoding="utf-8")
print(entete); print("\n".join(lignes))
