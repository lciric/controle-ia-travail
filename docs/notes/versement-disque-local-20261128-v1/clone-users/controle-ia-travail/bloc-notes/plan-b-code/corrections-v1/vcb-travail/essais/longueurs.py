import sys
for f in sys.argv[1:]:
    for i, l in enumerate(open(f, encoding="utf-8").read().split("\n"), 1):
        if len(l) > 120:
            print(f, i, len(l))
