import re, sys, hashlib
err, cible, debut, fin = sys.argv[1:5]
t = open(err, encoding='utf-8').read()
bloc = t.split(debut, 1)[1].split(fin, 1)[0]
txt = open(cible, encoding='utf-8').read()
entrees = re.findall(r'^\*\*(L-\d+)\.\*\* ANCIEN : « (.*?) »\nNOUVEAU : « (.*?) »\nRaison :', bloc, re.M | re.S)
ids = [e[0] for e in entrees]
assert len(ids) == len(set(ids)), ids
for i, a, n in entrees:
    c = txt.count(a)
    assert c == 1, (i, c)
    txt = txt.replace(a, n)
    assert a in n or a not in txt, i
print(len(entrees), 'entrées', ids)
print(hashlib.sha256(txt.encode()).hexdigest())
if len(sys.argv) > 5:
    open(sys.argv[5], 'w', encoding='utf-8').write(txt)
