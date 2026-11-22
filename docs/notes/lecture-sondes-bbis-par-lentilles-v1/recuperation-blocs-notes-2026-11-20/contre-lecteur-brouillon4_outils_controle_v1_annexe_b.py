# Programme de l'annexe B de la contre-lecture 3 (42024aa9…), recopié mot pour mot, plus le classement « égales / prolongées / réécrites ».
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
for i, l in enumerate(a):
    k = j
    while k < len(b) and not (b[k] == l or (l and b[k].startswith(l))): k += 1
    if k == len(b): manque.append(i + 1)
    else:
        if b[k] != l: prolonge.append(i + 1)
        j = k + 1
print(manque, prolonge)
print("lignes de la v1 :", len(a) - 1 if a[-1] == "" else len(a))
