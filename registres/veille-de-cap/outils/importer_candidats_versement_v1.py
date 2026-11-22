"""Import des 79 candidats du versement du 22 novembre au journal des idées, après la garde des noms exclus (v1).
Garde : MOTS_INTERDITS de partition_journal_v3 sur nom, mots, sert, repere, note, extrait, chemin ; niveau « plein » du
bras boucle (listes_lecture_v3) pour le chemin source. Écarté = non importé, compté, listé par numéro de ligne."""
import hashlib, importlib.util, json, re, sys
F = "docs/notes/memoire-conception-v1/fusion-outils-v1/"
def charger(n, f):
    s = importlib.util.spec_from_file_location(n, F + f); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
pj = charger("pj", "partition_journal_v3.py"); ll = pj.ll2
cand, journal_base, sortie, quand_import = sys.argv[1:5]
brut = open(cand, "rb").read()
assert hashlib.sha256(brut).hexdigest().startswith("7942a069"), "empreinte des candidats"
L = [json.loads(l) for l in brut.decode().split("\n") if l.strip()]
assert len(L) == 79
maxi = {"G": 0, "I": 0, "P": 0}
for p in [journal_base, journal_base[:-6] + "-partie-0002.jsonl"]:
    for l in open(p):
        m = re.fullmatch(r"([GIP])-(\d{4})", json.loads(l).get("fiche", ""))
        if m: maxi[m.group(1)] = max(maxi[m.group(1)], int(m.group(2)))
print("plus hauts numéros avant import :", maxi)
gardes, ecartes = [], []
for i, e in enumerate(L, 1):
    src = e["source"]
    libres = [e.get("nom") or "", *(e.get("mots") or []), e.get("sert") or "", src.get("repere") or "",
              e.get("note") or "", src.get("extrait") or "", src.get("chemin") or ""]
    bas = ll.sans_accents(" ".join(libres)).lower()
    touches = [m for m in pj.MOTS_INTERDITS if m in bas]
    niv = ll.niveau_boucle(ll.normaliser_chemin(src["chemin"]))[0]
    if touches or niv != "plein":
        ecartes.append((i, touches, niv)); continue
    gardes.append(e)
lignes = []
for e in gardes:
    p = e["fiche"][0]; maxi[p] += 1
    lot = e.pop("lot", None)
    note = f"importé le {quand_import} du versement du 22 novembre (candidats-v2.jsonl, 7942a069…)"
    if lot: note += f" ; lot du versement : {lot}"
    if e.get("note"): note += f" ; note du versement : {e['note']}"
    e["fiche"] = f"{p}-{maxi[p]:04d}"; e["note"] = note
    e["origine"] = e["quand"][:10]; e["derniere_trace"] = e["quand"][:10]
    lignes.append(json.dumps(e, ensure_ascii=False))
with open(sortie, "x", encoding="utf-8") as f:
    f.write("\n".join(lignes) + "\n")
print(f"importés {len(lignes)}, écartés {len(ecartes)} : {ecartes}")
print("plus hauts numéros après import :", maxi)
