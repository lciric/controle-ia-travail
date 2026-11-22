import json, sys, difflib
d = json.load(open(sys.argv[1], encoding="utf-8"))[sys.argv[2]]
lim = int(sys.argv[3]); sel = sys.argv[4:]
for c in d:
    if sel and c["id"] not in sel: continue
    if not sel and c["id"].endswith("01"): continue
    av, ap = c["av"], c["ap"]
    # préfixe et suffixe communs retirés pour ne montrer que ce qui change
    i = 0
    while i < min(len(av), len(ap)) and av[i] == ap[i]: i += 1
    j = 0
    while j < min(len(av), len(ap)) - i and av[-1 - j] == ap[-1 - j]: j += 1
    a2 = av[i:len(av) - j]; b2 = ap[i:len(ap) - j]
    print("#### %s | %s | arrivée %d-%d" % (c["id"], " | ".join(map(str, c["meta"])), c["l_arr"], c["l_arr_fin"]))
    print("  [contexte avant] …" + av[max(0, i - 120):i].replace("\n", " ⏎ "))
    print("  [retiré] " + (a2[:lim] + (" …(%d car.)" % len(a2) if len(a2) > lim else "")).replace("\n", " ⏎ "))
    print("  [mis]    " + (b2[:lim] + (" …(%d car.)" % len(b2) if len(b2) > lim else "")).replace("\n", " ⏎ "))
