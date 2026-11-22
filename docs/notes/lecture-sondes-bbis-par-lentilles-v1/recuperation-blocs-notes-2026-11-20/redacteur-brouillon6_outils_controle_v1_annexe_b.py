import difflib, sys
a = open(sys.argv[1], encoding="utf-8").read().split("\n")
b = open(sys.argv[2], encoding="utf-8").read().split("\n")
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
egal = suppr = remplace = insere = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal": egal += i2 - i1
    elif tag == "delete": suppr += i2 - i1
    elif tag == "insert": insere += j2 - j1
    else: remplace += i2 - i1; print(tag, "v1", i1 + 1, i2, "v2", j1 + 1, j2)
print(egal, suppr, remplace, insere)
j = 0; manque = []; prolonge = []
for i, l in enumerate(a):          # chaque ligne de la v1, égale ou début d'une ligne de la v2, dans l'ordre
    k = j
    while k < len(b) and not (b[k] == l or (l and b[k].startswith(l))): k += 1
    if k == len(b): manque.append(i + 1)
    else:
        if b[k] != l: prolonge.append(i + 1)
        j = k + 1
print(manque, prolonge)
