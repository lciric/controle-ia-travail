import json, sys
src = open(sys.argv[1]).read()
ns = {}
exec(src.split("# N21")[0].replace('json.dump(RES', '#'), ns)
Brut, ch, us, appel = ns["Brut"], ns["ch"], ns["us"], ns["appel"]
R = {}
for mt in (1, 16, 2000):
    for n in (2 * mt + 8, 2 * mt + 9):
        if n > 12 * mt: continue
        s = Brut(lambda k, c, n=n, mt=mt: ns["sse"](*[ch("a") for _ in range(n)], ch(fin="length"), ch(choix=False, usage=us(c=mt, r=0)), b"[DONE]"))
        r, tr, ex = appel(s.url, mt=mt); s.fin()
        R[f"mt{mt}_n{n}_contenu"] = "coupé" if ex else "accepté"
    # deux champs dans un même delta : chaque champ compte
    n = mt + 5  # 2n = 2mt+10 > 2mt+8
    if 2 * n <= 12 * mt:
        s = Brut(lambda k, c, n=n, mt=mt: ns["sse"](*[{"id": "i", "model": ns["M"], "choices": [{"index": 0, "delta": {"content": "a", "reasoning_content": "b"}}]} for _ in range(n)],
                                                     ch(fin="length"), ch(choix=False, usage=us(c=mt, r=0)), b"[DONE]"))
        r, tr, ex = appel(s.url, mt=mt); s.fin()
        R[f"mt{mt}_{n}deltas_doubles"] = "coupé" if ex else "accepté"
# octets : 12*mt exact accepté, +1 coupé (un seul morceau)
for extra in (0, 1):
    s = Brut(lambda k, c, e=extra: ns["sse"](ch("a" * (12 * 16 + e)), ch(fin="length"), ch(choix=False, usage=us(c=16, r=0)), b"[DONE]"))
    r, tr, ex = appel(s.url, mt=16); s.fin()
    R[f"octets_{12*16+extra}_mt16"] = "coupé" if ex else ("accepté, usage " + ("lu" if r["usage"] else "refusé"))
print(json.dumps(R, ensure_ascii=False, indent=1)); json.dump(R, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
