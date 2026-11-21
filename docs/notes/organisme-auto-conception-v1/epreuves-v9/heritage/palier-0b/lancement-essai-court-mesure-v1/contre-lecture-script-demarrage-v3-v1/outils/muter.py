import sys
# change un signe base64 a la position donnee (un seul), garde la longueur
s = open(sys.argv[1]).read()
i = int(sys.argv[3])
c = s[i]
n = "B" if c != "B" else "C"
open(sys.argv[2], "w").write(s[:i] + n + s[i + 1:])
