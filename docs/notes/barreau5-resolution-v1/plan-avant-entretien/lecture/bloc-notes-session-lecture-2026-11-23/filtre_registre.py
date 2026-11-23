import sys
CLES = ["SCELLEMENT-B5F","CODE-FORMATION-B5F","GO-FORMATION-B5F","CODE-LECTURE-B5F","EPREUVE-B5F",
        "GO-RELANCE-FORMATION-B5F","SORTIES-FORMATION-B5F","ENGAGEMENT-B5F","GO-LECTURE-B5F",
        "SCORES-B5F","OUVERTURE-B5F","LECTURE-B5F","VERDICT-B5F"]
for n, l in enumerate(open(sys.argv[1], encoding="utf-8"), 1):
    if not l.lstrip().startswith("|"):
        continue
    cells = [c.strip().strip("`").strip("*").strip() for c in l.strip().strip("|").split("|")]
    if any(c in CLES for c in cells):
        print(n, l.rstrip())
