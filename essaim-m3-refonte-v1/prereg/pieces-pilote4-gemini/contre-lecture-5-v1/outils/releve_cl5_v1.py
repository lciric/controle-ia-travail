# Relevé indépendant (contre-lecture 5), lecture seule, pièces de simulation seulement : même sortie que le relevé v3 attendu.
import collections, json, pathlib, sys
V = pathlib.Path(sys.argv[1])
cas = [("v6.2 continue", "cas-sain-v6-2/pilote4-gemini-v6-2-v1"), ("v5.3 continue", "cas-sain-v5-3/pilote4-gemini-v5-3-v1"),
       ("v6.2 en deux segments", "cas-seg-segment1/pilote4-gemini-v6-2-v1"),
       ("v6.2 en trois segments", "cas-seg3-segment1/pilote4-gemini-v6-2-v1")]
out = []
for nom, rel in cas:
    P = V / rel
    out.append(f"== {nom} ({rel})")
    for j in sorted(P.glob("journal-appels-*.jsonl")):
        L = [json.loads(x) for x in j.read_text(encoding="utf-8").splitlines() if x.strip()]
        st = dict(collections.Counter(x.get("statut") for x in L))
        m = sum(1 for x in L if x.get("role") == "architecte_mutation_endogene")
        out.append(f"  {j.name} : {len(L)} appels ; statuts {st} ; appels de mutation {m}")
    e = json.loads((P / "extrait-mecanique-v1.json").read_text(encoding="utf-8"))
    for ev in e.get("evenements", []):
        if ev.get("etape") == "arret":
            out.append(f"  arrêt : {ev.get('raison')}")
        elif ev.get("etape") == "reprise":
            out.append(f"  reprise : segment {ev.get('segment')}, état {ev.get('etat')}, {ev.get('n_appels_relus')} appels et {ev.get('depense_relue_usd')} USD relus")
print("\n".join(out))
