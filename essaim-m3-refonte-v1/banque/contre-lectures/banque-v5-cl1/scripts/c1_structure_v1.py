"""Contre-lecture de la banque confrontation-v5 — c1 : structure, sélection, identifiants, secret, manifeste, clés.

Code écrit par le contre-lecteur (aucun import du code des auteurs). N'imprime ni n'écrit aucune clé, aucune
correspondance par tâche entre identifiants (seulement des comptes et des booléens).
Usage : python3 -I -B c1_structure_v1.py DOSSIER_BANQUE SORTIE_JSON
"""
import hashlib, json, os, pathlib, re, sys
import numpy as np

D = pathlib.Path(sys.argv[1]); SORTIE = pathlib.Path(sys.argv[2])
PARTS = ("train", "test", "test_final"); FAM = "controle-delegation"; CHAMPS = ("famille", "texte", "etiquettes", "verite", "source")
J = lambda n: json.loads((D / n).read_text(encoding="utf-8"))
v1, s1 = J("banque-confrontation-v1.json"), J("banque-confrontation-v1-secret.json")
v3, s3, c3 = J("banque-confrontation-v3.json"), J("banque-confrontation-v3-secret.json"), J("banque-confrontation-v3-cle.json")
v4, s4, c4 = J("banque-confrontation-v4.json"), J("banque-confrontation-v4-secret.json"), J("banque-confrontation-v4-cle.json")
v5, s5, c5 = J("banque-confrontation-v5.json"), J("banque-confrontation-v5-secret.json"), J("banque-confrontation-v5-cle.json")
E3, E4, E5 = (int(c["entropie_seed_sequence"]) for c in (c3, c4, c5))
r = {"sha256": {n: hashlib.sha256((D / n).read_bytes()).hexdigest() for n in
                ("banque-confrontation-v3.json", "banque-confrontation-v4.json", "banque-confrontation-v5.json",
                 "banque-confrontation-v5-secret.json")}, "numpy": np.__version__}

# 1. sélection de la v4 refaite depuis sa clé (réécriture indépendante de la règle écrite au constructeur v4)
def ma_selection(e):
    g = np.random.default_rng(np.random.SeedSequence(e)); garde = set()
    for part in ("test", "test_final"):
        paires = {}
        for t in v3[part]:
            if t["famille"] == FAM:
                paires.setdefault((t["source"], s3[t["id"]]["paire"]), {})[t["verite"]] = t["id"]
        assert all(set(m) == {"honnete", "sabotage"} for m in paires.values())
        sources = sorted({s for s, _ in paires}); nh = ns = 0; reste = []
        for s in sources:
            cles = sorted(k for k in paires if k[0] == s)
            perm = g.permutation(len(cles)); h = len(cles) // 2
            for rang, j in enumerate(perm):
                if rang < h: c = "honnete"
                elif rang < 2 * h: c = "sabotage"
                else: reste.append(cles[j]); continue
                garde.add(paires[cles[j]][c]); nh += c == "honnete"; ns += c == "sabotage"
        for k in reste:
            c = "honnete" if nh <= ns else "sabotage"; garde.add(paires[k][c]); nh += c == "honnete"; ns += c == "sabotage"
    return garde
garde = ma_selection(E4)
garde_v4 = {t["id"] for p in ("test", "test_final") for t in v4[p] if t["famille"] == FAM}
r["selection_v4_recalculee_egale"] = garde == garde_v4
r["v4_egale_v3_hors_retraits"] = all(v4[p] == [t for t in v3[p] if t["famille"] != FAM or t["id"] in garde or p == "train"] for p in PARTS)

# 2. la v5 = exactement les 176 tâches de la v4, mêmes champs et parts, sous la règle écrite et la clé v5
ordre4 = [(p, t) for p in PARTS for t in v4[p]]
perm = np.random.default_rng(np.random.SeedSequence(E5)).permutation(len(ordre4))
attendu = {f"q-{int(perm[i]) + 1:04d}": ordre4[i] for i in range(len(ordre4))}
ids5 = {t["id"]: p for p in PARTS for t in v5[p]}
ok_tache = all(attendu[t["id"]][0] == p and {k: t[k] for k in CHAMPS} == {k: attendu[t["id"]][1][k] for k in CHAMPS}
               and set(t) == {"id", *CHAMPS} for p in PARTS for t in v5[p])
r["v5"] = {"n": {p: len(v5[p]) for p in PARTS}, "ids_uniques": len(ids5) == sum(len(v5[p]) for p in PARTS),
           "ids_egaux_a_la_regle": set(ids5) == set(attendu), "taches_egales_v4_meme_part_memes_champs": ok_tache,
           "couverture_v4": sorted(t["id"] for _, t in attendu.values()) == sorted(t["id"] for _, t in ordre4),
           "parts_triees": all([t["id"] for t in v5[p]] == sorted(t["id"] for t in v5[p]) for p in PARTS),
           "ids_contigus_1_176": sorted(ids5) == [f"q-{i:04d}" for i in range(1, 177)],
           "secret_id_v3_egal_regle": {k: v.get("id_v3") for k, v in s5.items()} == {k: t["id"] for k, (_, t) in attendu.items()}}
# 3. secret v5 = secret v3 + id_v3 (et rien d'autre) ; sous_ensemble du secret = part de la v5
r["secret"] = {"cles_egales_banque": set(s5) == set(ids5),
               "egal_secret_v3_plus_id_v3": all(s5[k] == {**s3[s5[k]["id_v3"]], "id_v3": s5[k]["id_v3"]} for k in s5),
               "secret_v4_egal_secret_v3_restreint": all(s4[k] == s3[k] for k in s4) and set(s4) == {t["id"] for _, t in ordre4},
               "sous_ensemble_egal_part": sum(s5[k].get("sous_ensemble") == ids5[k] for k in s5), "n": len(s5),
               "id_v1_tous_presents": all("id_v1" in v for v in s5.values())}
# 4. manifeste
m = v5["manifeste"]; comptes = {}
for p in PARTS:
    for t in v5[p]:
        mode = "agentique" if (t["famille"] != FAM and s5[t["id"]].get("agentique")) else "conversation"  # banque.py l. 85, l. 125
        k = f"{t['famille']}|{t['verite']}|{t['source']}|{mode}"
        comptes.setdefault(k, {q: 0 for q in PARTS})[p] += 1
cv1 = v1["manifeste"]["comptes_par_strate"]
r["manifeste"] = {"n_juste": m["n"] == {p: len(v5[p]) for p in PARTS}, "comptes_justes": m["comptes_par_strate"] == comptes,
                  "strates_conscience_egales_v1": all(cv1[k] == comptes[k] for k in comptes if k.startswith("conscience")),
                  "champs": sorted(m), "parts_annoncees": m.get("parts"),
                  "parts_reelles": {p: round(len(v5[p]) / 176, 4) for p in PARTS},
                  "provenance_n": [x["n"] for x in m.get("provenance", [])],
                  "n_tronques_annonce": m.get("n_tronques"), "n_tronques_reel": sum(bool(v.get("tronque")) for v in s5.values()),
                  "complete_annonce": m.get("complete"),
                  "complete_reel": all({t["famille"] for t in v5[p]} == {FAM, "conscience-evaluation"} for p in PARTS),
                  "entropie_cle_v5_empreinte_juste": m["identifiants_opaques"]["entropie_sha256"] == hashlib.sha256(str(E5).encode()).hexdigest(),
                  "graine_partition_v1_en_clair": "entropie_seed_sequence" in m,
                  "graine_partition_v1_egale_v1": m.get("entropie_seed_sequence") == v1["manifeste"]["entropie_seed_sequence"],
                  "graine_partition_v1_egale_une_cle_secrete": m.get("entropie_seed_sequence") in (E3, E4, E5),
                  "bilan_6_6_au_manifeste": "une_trace_par_paire" in m,
                  "regle_racine": m.get("regle"), "regle_identifiants": m["identifiants_opaques"].get("regle")}
# 5. clés : formes cherchées dans tous les fichiers du dossier (noms interdits exclus)
def formes(e):
    b = e.to_bytes(16, "big")
    return {"dec": str(e).encode(), "hex": f"{e:x}".encode(), "HEX": f"{e:X}".encode(), "hex32": f"{e:032x}".encode(),
            "b16": b, "l16": b[::-1]}
interdit = lambda p: p.name == "P3-consignes-v1.md" or p.name.startswith("textes-actions-") or any(x in ("donnees", "runs", "diag") for x in p.parts)
fichiers = [p for p in sorted(D.rglob("*")) if p.is_file() and not interdit(p.relative_to(D))]
trouves = {n: {} for n in ("E3", "E4", "E5", "graine_v1")}
gv1 = int(v1["manifeste"]["entropie_seed_sequence"])
for p in fichiers:
    o = p.read_bytes()
    for n, e in (("E3", E3), ("E4", E4), ("E5", E5), ("graine_v1", gv1)):
        for f, motif in formes(e).items():
            if motif in o:
                trouves[n].setdefault(str(p.relative_to(D)), []).append(f)
r["cles"] = {"fichiers_lus": len(fichiers), "trouvees": trouves, "E5_diff_E3_E4": E5 not in (E3, E4), "bits": [e.bit_length() for e in (E3, E4, E5)]}
# 6. identifiants v1, v3, id_source, groupe dans la banque v5 (texte du fichier)
tb = (D / "banque-confrontation-v5.json").read_text(encoding="utf-8")
def compte(vals):
    n = 0
    for x in vals:
        if x and re.search(r"(?<![\w-])" + re.escape(str(x)) + r"(?![\w-])", tb):
            n += 1
    return n
r["identifiants_dans_v5"] = {"id_v1": compte(v["id_v1"] for v in s3.values()), "id_v3": compte(s3.keys()),
                             "id_v3_entre_guillemets": sum(f'"{k}"' in tb for k in s3),
                             "id_source": compte(v.get("id_source") for v in s3.values()),
                             "groupe": compte(v.get("groupe") for v in s3.values()),
                             "motif_t_9999": len(re.findall(r"(?<![\w-])t-[0-9]{4}(?![\w-])", tb)),
                             "motif_cd_lot": len(re.findall(r"cd-lot", tb)), "motif_ce_hf": len(re.findall(r"ce-hf-[0-9]", tb)),
                             "motif_q_9999_dans_textes": sum(len(re.findall(r"q-[0-9]{4}", t["texte"])) for p in PARTS for t in v5[p])}
# 7. étiquettes constantes par famille ; ordre des textes ; consigne d'amorçage (six premières tâches du train)
r["etiquettes_constantes"] = all(len({json.dumps(t["etiquettes"]) for p in PARTS for t in v5[p] if t["famille"] == f}) == 1 for f in (FAM, "conscience-evaluation"))
r["amorcage_six_premieres"] = {n: [(t["famille"], t["verite"]) for t in b["train"][:6]] for n, b in (("v3", v3), ("v4", v4), ("v5", v5))}
paire_de = {t["id"]: (t["source"], s5[t["id"]].get("paire")) for t in v5["train"][:6] if t["famille"] == FAM}
r["amorcage_six_premieres_paires_completes_v5"] = len(paire_de) - len(set(paire_de.values()))
SORTIE.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(r, ensure_ascii=False, indent=1))
