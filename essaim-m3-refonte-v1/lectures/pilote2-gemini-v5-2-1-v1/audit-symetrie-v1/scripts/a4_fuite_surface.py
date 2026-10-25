"""Audit de symétrie, pilote 2 — (a) contexte servi (clés des tâches de test, historique) ; (b) mémoire transmise g0 -> g1 ;
(c) recouvrement des documents moissonnés et des textes de test (n-grammes de 8 et de 6 mots) et journal de fuite ;
(d) règles de surface simples sur la famille B (un mot, une longueur), apprises sur train. Lecture seule de JSON et de texte.
Usage : python3 -I a4_fuite_surface.py RACINE_ESPACE_TRAVAIL_M RACINE_ESPACE_TRAVAIL_S"""
import json, sys, re, pathlib, collections

BANQ = "/home/claude/pilote3-v53-v6/essaim-m3-refonte-v1/banque/banque-confrontation-v1.json"
b = json.load(open(BANQ))
tests = b["test"] + b["test_final"]
ids_test = {t["id"]: t for t in tests}
mots = lambda s: re.findall(r"\w+", s.lower())


def ngrams(s, n):
    w = mots(s)
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


ng_test = {n: collections.defaultdict(set) for n in (6, 8)}
for t in tests:
    for n in (6, 8):
        for x in ngrams(t["texte"], n):
            ng_test[n][x].add(t["id"])
# n-grammes communs à la banque entière (gabarits partagés, ex. « t=01 outil=… ») : on écarte ceux du train aussi
ng_train = {n: set().union(*[ngrams(t["texte"], n) for t in b["train"]]) for n in (6, 8)}

for nom, racine in zip(("M", "S"), sys.argv[1:3]):
    R = pathlib.Path(racine)
    for g in ("g000", "g001"):
        ctx = json.load(open(R / g / "contexte.json"))
        cles = collections.Counter(tuple(sorted(t.keys())) for t in ctx["taches_test"])
        porte_verite = sum(1 for t in ctx["taches_test"] if "verite" in t or "categorie" in t)
        txt_ok = all(t["texte"] == ids_test[t["id"]]["texte"] for t in ctx["taches_test"])
        etiq_dans_texte = {lab: sum(1 for t in ctx["taches_test"] if re.search(rf"\b{lab}\b", t["texte"], re.I))
                           for lab in ("sabotage", "honnete", "honnête", "sabotée", "sabote")}
        print(f"\n== {nom} {g} : contexte.json taches_test n={len(ctx['taches_test'])} clés={dict(cles)} portant vérité={porte_verite}"
              f" textes identiques à la banque={txt_ok} ; mots d'étiquette dans les textes servis={etiq_dans_texte}")
        print(f"   historique : {json.dumps(ctx.get('historique'), ensure_ascii=False)[:600]}")
        mem = R / g / "memoire_isvd.json"
        if mem.exists():
            m = mem.read_text(encoding="utf-8", errors="replace")
            ids_dans = sorted(set(re.findall(r"(cd-lot[12]-L[12]-\d\d-[HS]|ce-hf-\d{4}|L[12]-\d\d-[HS])", m)))
            ids_t = [i for i in ids_dans if i in ids_test or any(k.endswith(i) for k in ids_test)]
            print(f"   memoire_isvd.json ({len(m)} o) : identifiants trouvés={ids_dans[:10]} dont de test={ids_t[:10]} ;"
                  f" mots sabotage/honnete : {len(re.findall(r'sabotage|honnete', m))}")
            # recouvrement mémoire / textes de test (8-grammes absents du train)
            com = {x for x in ngrams(m, 8) if x in ng_test[8] and x not in ng_train[8]}
            print(f"   8-grammes de la mémoire présents dans un texte de test et absents du train : {len(com)} ;"
                  f" items touchés : {sorted(set().union(*[ng_test[8][x] for x in com]))[:12] if com else []}")
        # corpus moissonné et bruts de recherche
        docs = list((R / f"{g}.corpus").glob("**/*")) + list((R / f"{g}.noyau" / "recherches").glob("*.brut"))
        for n in (8, 6):
            touches = collections.Counter(); exemples = []
            for d in docs:
                if not d.is_file():
                    continue
                s = d.read_text(encoding="utf-8", errors="replace")
                com = {x for x in ngrams(s, n) if x in ng_test[n] and x not in ng_train[n]}
                for x in com:
                    for i in ng_test[n][x]:
                        touches[i] += 1
                if com and len(exemples) < 3:
                    exemples.append((d.name, sorted(com)[:2]))
            fam = collections.Counter(ids_test[i]["famille"] for i in touches)
            print(f"   documents moissonnés ({len(docs)}) : items de test touchés par un {n}-gramme (absent du train) = {len(touches)} {dict(fam)} ; exemples {exemples}")
        jf = R / f"{g}.noyau" / "journal-fuite.jsonl"
        lignes = [json.loads(l) for l in jf.read_text().splitlines() if l.strip()] if jf.exists() else []
        print(f"   journal-fuite.jsonl : {len(lignes)} lignes ; {json.dumps(lignes[:2], ensure_ascii=False)[:500]}")

print("\n== règles de surface simples, famille contrôle de délégation (apprises sur train, notées sur test et test_final)")
fam = "controle-delegation"
tr = [t for t in b["train"] if t["famille"] == fam]


def ee(pred, items):
    vp = sum(1 for t in items if t["verite"] == "sabotage" and pred(t)); fn = sum(1 for t in items if t["verite"] == "sabotage" and not pred(t))
    vn = sum(1 for t in items if t["verite"] == "honnete" and not pred(t)); fp = sum(1 for t in items if t["verite"] == "honnete" and pred(t))
    return round((vp / max(1, vp + fn) + vn / max(1, vn + fp)) / 2, 4)


voc = collections.Counter(w for t in tr for w in set(mots(t["texte"])))
meilleurs = []
for w, c in voc.items():
    if c < 2:
        continue
    for signe in (True, False):
        p = (lambda t, w=w, s=signe: (w in set(mots(t["texte"]))) == s)
        meilleurs.append((ee(p, tr), w, signe))
meilleurs.sort(reverse=True)
for sc, w, signe in meilleurs[:5]:
    p = (lambda t, w=w, s=signe: (w in set(mots(t["texte"]))) == s)
    print(f"  mot {w!r} {'présent' if signe else 'absent'} ⇒ sabotage : train {sc} ; test {ee(p, [t for t in b['test'] if t['famille'] == fam])} ;"
          f" test_final {ee(p, [t for t in b['test_final'] if t['famille'] == fam])}")
longs = sorted({len(t["texte"]) for t in tr})
best = max(((ee(lambda t, L=L, s=s: (len(t["texte"]) > L) == s, tr), L, s) for L in longs for s in (True, False)))
p = lambda t, L=best[1], s=best[2]: (len(t["texte"]) > L) == s
print(f"  longueur > {best[1]} {'⇒' if best[2] else '⇏'} sabotage : train {best[0]} ; test {ee(p, [t for t in b['test'] if t['famille'] == fam])} ;"
      f" test_final {ee(p, [t for t in b['test_final'] if t['famille'] == fam])}")
# contraste de paire (hors de portée de l'organisme, qui voit une trace par consigne) : la plus longue des deux = sabotage ?
for part in ("test", "test_final"):
    par = collections.defaultdict(dict)
    for t in b[part]:
        if t["famille"] == fam:
            par[t["id"][:-2]][t["verite"]] = len(t["texte"])
    plus_long = sum(1 for v in par.values() if v["sabotage"] > v["honnete"])
    print(f"  {part} : paires où la trace sabotée est la plus longue : {plus_long}/{len(par)}")
