"""Relevé mécanique des cas sains d'une série d'essais du lanceur du pilote 4 (simulations seulement) — v3 (conv-audit,
26 octobre 2026) : la v1 (7d72a174…, contre-lecture 4, P4C4-05 a) pour la batterie v12 — la v6.2 (v6.2.1, clé de course
`v6-2`) d'abord, puis la v5.3 ; les cas de segments tournent sur la v6.2 ; rien d'autre ne change (la v2, écrite pour
l'ordre ancien, n'a jamais servi).

Usage : python -I releve_appels_simulation_v3.py DOSSIER_DES_CAS_DE_LA_SERIE
Pour la v6.2 et la v5.3 continues, la v6.2 en deux et en trois segments : par journal d'appels recopié (rondes et
générations), le nombre d'appels, les statuts et les appels de rôle `architecte_mutation_endogene` ; dans l'extrait
mécanique, les arrêts et les reprises (segment, appels et dépense relus). Ne lit que des pièces de simulation ; aucun
score.
"""
import collections, json, pathlib, sys

V = pathlib.Path(sys.argv[1])
cas = [("v6.2 continue", V / "cas-sain-v6-2/pilote4-gemini-v6-2-v1"), ("v5.3 continue", V / "cas-sain-v5-3/pilote4-gemini-v5-3-v1"),
       ("v6.2 en deux segments", V / "cas-seg-segment1/pilote4-gemini-v6-2-v1"),
       ("v6.2 en trois segments", V / "cas-seg3-segment1/pilote4-gemini-v6-2-v1")]
for nom, P in cas:
    print(f"== {nom} ({P.relative_to(V)})")
    for j in sorted(P.glob("journal-appels-*.jsonl")):
        lignes = [json.loads(l) for l in j.read_text(encoding="utf-8").splitlines() if l.strip()]
        statuts = dict(collections.Counter(l.get("statut") for l in lignes))
        mut = sum(1 for l in lignes if l.get("role") == "architecte_mutation_endogene")
        print(f"  {j.name} : {len(lignes)} appels ; statuts {statuts} ; appels de mutation {mut}")
    e = json.loads((P / "extrait-mecanique-v1.json").read_text(encoding="utf-8"))
    for ev in e.get("evenements", []):
        if ev.get("etape") == "arret":
            print(f"  arrêt : {ev.get('raison')}")
        elif ev.get("etape") == "reprise":
            print(f"  reprise : segment {ev.get('segment')}, état {ev.get('etat')}, {ev.get('n_appels_relus')} appels et "
                  f"{ev.get('depense_relue_usd')} USD relus")
