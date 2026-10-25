"""Contre-lecture banque v4 — c1 : structure, équivalence avec la v3, tirage recalculé depuis la clé — v1.
N'imprime jamais la clé (ni v3 ni v4) : seulement des booléens, des comptes et des empreintes.
Usage : python3 -I -B c1_structure_v1.py DOSSIER_BANQUE
"""
import collections, hashlib, json, pathlib, sys
import numpy as np

B = pathlib.Path(sys.argv[1])
FAM = "controle-delegation"
PARTS = ("train", "test", "test_final")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def charger(nom):
    return json.loads((B / nom).read_text(encoding="utf-8"))


out = {"numpy": np.__version__}
# 1. empreintes : compagnons, EMPREINTES-banque-v4-v1.txt, table du LISEZMOI-v7
comp = {}
for f in sorted(B.glob("banque-confrontation-v[34]*.json")) + sorted((B / "construction-v4").glob("*")) + [B / "LISEZMOI-v7.md", B / "EMPREINTES-banque-v4-v1.txt"]:
    if f.name.endswith(".sha256") or not f.is_file():
        continue
    c = f.with_name(f.name + ".sha256")
    comp[str(f.relative_to(B))] = (c.exists() and c.read_text(encoding="utf-8").split()[0] == sha(f))
out["compagnons_conformes"] = comp
emp = {}
for ligne in (B / "EMPREINTES-banque-v4-v1.txt").read_text(encoding="utf-8").splitlines():
    if ligne.strip():
        h, nom = ligne.split(None, 1)
        emp[nom.strip()] = (sha(B / nom.strip()) == h)
out["EMPREINTES_v4_conformes"] = emp
lis = (B / "LISEZMOI-v7.md").read_text(encoding="utf-8")
out["table_LISEZMOI_v7"] = {n: (sha(B / n) in lis) for n in ("banque-confrontation-v4.json", "banque-confrontation-v4-secret.json", "banque-confrontation-v4-cle.json")}

v3, s3, v4, s4 = (charger(n) for n in ("banque-confrontation-v3.json", "banque-confrontation-v3-secret.json", "banque-confrontation-v4.json", "banque-confrontation-v4-secret.json"))
c4, c3 = charger("banque-confrontation-v4-cle.json"), charger("banque-confrontation-v3-cle.json")
out["sha_v3_attendu"] = sha(B / "banque-confrontation-v3.json") == "157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d"

# 2. train, conscience, tâches gardées, ordre
out["train_identique"] = v4["train"] == v3["train"]
r = {}
for p in ("test", "test_final"):
    a4 = [t for t in v4[p] if t["famille"] != FAM]; a3 = [t for t in v3[p] if t["famille"] != FAM]
    par3 = {t["id"]: t for t in v3[p]}
    ids3 = [t["id"] for t in v3[p]]
    pos = [ids3.index(t["id"]) for t in v4[p] if t["id"] in par3]
    r[p] = {"conscience_identique": a4 == a3, "n_conscience": len(a4),
            "taches_gardees_identiques": all(par3.get(t["id"]) == t for t in v4[p]),
            "ordre_relatif_garde": pos == sorted(pos) and len(pos) == len(v4[p]),
            "trie_par_id": [t["id"] for t in v4[p]] == sorted(t["id"] for t in v4[p]),
            "n": len(v4[p])}
ids4 = [t["id"] for p in PARTS for t in v4[p]]
out["ids_uniques"] = len(ids4) == len(set(ids4))
out["parts"] = r

# 3. paires (source, paire) ; une trace par paire ; équilibres
paires_info = {}
kept_ids = set(ids4)
for p in PARTS:
    pv3 = collections.defaultdict(list)
    for t in v3[p]:
        if t["famille"] == FAM:
            pv3[(t["source"], s3[t["id"]]["paire"])].append(t)
    deux_classes = all(len(m) == 2 and {x["verite"] for x in m} == {"honnete", "sabotage"} for m in pv3.values())
    gardes = collections.Counter(sum(x["id"] in kept_ids for x in m) for m in pv3.values())
    # paire prise sans la source (reproduction de la sortie marquée erronée)
    sans_src = collections.defaultdict(list)
    for t in v4[p]:
        if t["famille"] == FAM:
            sans_src[s3[t["id"]]["paire"]].append(t["id"])
    doubles_sans_source = sorted(k for k, v in sans_src.items() if len(v) == 2)
    cl = collections.Counter((t["source"], t["verite"]) for t in v4[p] if t["famille"] == FAM)
    paires_info[p] = {"n_paires_v3": len(pv3), "chaque_paire_v3_deux_classes": deux_classes,
                      "traces_gardees_par_paire": dict(gardes), "numeros_doubles_si_paire_sans_source": doubles_sans_source,
                      "classes_par_source": {f"{a}|{b}": n for (a, b), n in sorted(cl.items())},
                      "type_numero_paire": sorted({type(s3[t["id"]]["paire"]).__name__ for t in v3[p] if t["famille"] == FAM})}
out["paires"] = paires_info
retirees = [t["id"] for p in ("test", "test_final") for t in v3[p] if t["id"] not in kept_ids]
out["n_retirees"] = len(retirees)
out["retirees_toutes_delegation"] = all(next(t for p in PARTS for t in v3[p] if t["id"] == i)["famille"] == FAM for i in retirees)
out["retirees_absentes_de_v4"] = not (set(retirees) & kept_ids)
out["retirees_absentes_du_secret_v4"] = not (set(retirees) & set(s4))

# 4. secret
out["secret_v4_egal_v3_restreint"] = set(s4) == set(ids4) and all(s4[k] == s3[k] for k in s4)

# 5. clé : empreinte, longueur, absence en clair, différente de la v3, tirage recalculé
e = int(c4["entropie_seed_sequence"]); e3 = int(c3["entropie_seed_sequence"])
m4 = v4["manifeste"]
out["cle"] = {"empreinte_au_manifeste": hashlib.sha256(str(e).encode("ascii")).hexdigest() == m4["une_trace_par_paire"]["entropie_sha256"],
              "empreinte_dans_cle_egale": c4.get("entropie_sha256") == m4["une_trace_par_paire"]["entropie_sha256"],
              "bits": e.bit_length(), "differente_de_v3": e != e3,
              "champs_fichier_cle": sorted(c4),
              "absente_banque_v4": str(e) not in (B / "banque-confrontation-v4.json").read_text(encoding="utf-8"),
              "absente_secret_v4": str(e) not in (B / "banque-confrontation-v4-secret.json").read_text(encoding="utf-8"),
              "hex_absente_banque_v4": format(e, "x") not in (B / "banque-confrontation-v4.json").read_text(encoding="utf-8"),
              "cle_v3_absente_banque_v4": str(e3) not in (B / "banque-confrontation-v4.json").read_text(encoding="utf-8"),
              "entropie_partition_manifeste_n_est_pas_cle_v4": int(m4["entropie_seed_sequence"]) != e,
              "entropie_partition_manifeste_n_est_pas_cle_v3": int(m4["entropie_seed_sequence"]) != e3}

rng = np.random.default_rng(np.random.SeedSequence(e))
garde = set()
for p in ("test", "test_final"):
    pv = {}
    for t in v3[p]:
        if t["famille"] == FAM:
            pv.setdefault((t["source"], s3[t["id"]]["paire"]), []).append(t)
    par_source = {}
    for (src, pid), membres in sorted(pv.items(), key=lambda kv: kv[0]):
        par_source.setdefault(src, []).append(membres)
    for src in sorted(par_source):
        liste = par_source[src]
        ordre = rng.permutation(len(liste))
        h = len(liste) // 2
        for k, i in enumerate(ordre):
            classe = "honnete" if k < h else "sabotage"
            assert k < 2 * h
            garde.add(next(x["id"] for x in liste[i] if x["verite"] == classe))
deleg4 = {t["id"] for p in ("test", "test_final") for t in v4[p] if t["famille"] == FAM}
out["tirage_recalcule_depuis_la_cle_egal_v4"] = garde == deleg4

# 6. manifeste : champs hérités de la v3, comptes périmés
m3 = v3["manifeste"]
out["manifeste"] = {"champs_changes": sorted(k for k in set(m3) | set(m4) if m3.get(k) != m4.get(k)),
                    "comptes_par_strate_herites_de_v3": m4["comptes_par_strate"] == m3["comptes_par_strate"],
                    "comptes_par_strate_test_delegation": {k: v["test"] for k, v in m4["comptes_par_strate"].items() if k.startswith(FAM)},
                    "regle_racine_heritee": m4["regle"] == m3["regle"],
                    "bilan": m4["une_trace_par_paire"]["bilan"]}
# train : paires
pt = collections.defaultdict(list)
for t in v4["train"]:
    if t["famille"] == FAM:
        pt[(t["source"], s3[t["id"]]["paire"])].append(t["verite"])
out["train_paires"] = {"n": len(pt), "toutes_deux_classes": all(sorted(v) == ["honnete", "sabotage"] for v in pt.values())}
# identifiants retirés : numéros manquants dans 1..200
nums = sorted(int(i.split("-")[1]) for i in ids4)
out["numeros"] = {"min": nums[0], "max": nums[-1], "n": len(nums), "manquants_dans_1_200": 200 - len(nums)}
print(json.dumps(out, ensure_ascii=False, indent=1))
