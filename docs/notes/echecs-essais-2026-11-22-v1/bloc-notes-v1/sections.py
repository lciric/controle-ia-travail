import re,sys,pathlib
motifs={"echeance":"après l'échéance","validite":"période de validité","creation":"dernier jour de création","expire":"expir"}
for p in sorted(pathlib.Path(sys.argv[1]).glob("test_t06*.log")):
    t=p.read_text(errors="replace")
    if "= FAILURES =" not in t: continue
    t=t.split("= FAILURES =",1)[1].split("short test summary")[0]
    parts=re.split(r"\n_{3,} (.+?) _{3,}\n","\n"+t)
    for nom,corps in zip(parts[1::2],parts[2::2]):
        tags=[k for k,v in motifs.items() if v in corps]
        e=[l for l in corps.splitlines() if l.startswith("E ")][:1]
        print(p.stem, "|", nom, "|", ",".join(tags) or "AUCUN", "|", (e[0][:160] if e else ""))
