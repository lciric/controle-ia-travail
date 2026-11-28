import sys
ident, k, valeur = sys.argv[1], int(sys.argv[2]), sys.argv[3]
L = sys.stdin.read().split("\n")
print("\n".join(("|".join(c if i != k else f" {valeur} " for i, c in enumerate(l.split("|"))) if l.startswith(f"| {ident} |") else l)
                for l in L), end="")
