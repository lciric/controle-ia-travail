# outil de travail : compile chaque heredoc Python (<<'X' … X, avec un interpréteur Python sur la ligne) des scripts
import ast, re, sys
for p in sys.argv[1:]:
    L = open(p, encoding="utf-8").read().split("\n")
    i = 0
    while i < len(L):
        m = re.search(r"<<-?'([A-Za-z_]+)'", L[i])
        if m and re.search(r"python|\$PY|\$\{PY\}|PY\"", L[i]):
            d = m.group(1); j = i + 1
            while j < len(L) and L[j] != d:
                j += 1
            src = "\n".join(L[i + 1:j])
            try:
                ast.parse(src)
            except SyntaxError as e:
                print(f"{p}:{i+1}: heredoc {d} : {e.msg} (ligne {e.lineno} du bloc)")
            i = j
        i += 1
