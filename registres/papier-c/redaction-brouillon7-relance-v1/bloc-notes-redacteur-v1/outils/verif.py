import hashlib,re,sys
from pathlib import Path
texte=Path(sys.argv[1]).read_text(encoding="utf-8")
depot=Path(sys.argv[2]); copie=Path(sys.argv[3])
nus=[copie, depot/"registres/papier-c"]
INTERDITS=("diag/","runs/","donnees/","docs/verdicts/","consigne-privee","conception-ii-b","ii-b-saboteur","archives-reponses-modeles","quarantaine","vérité","rendu","scores")
MOTIF=re.compile(r"`([A-Za-z0-9_./\-]+\.(?:md|py|json|txt|pdf|gz|tsv|sh))`")
occ={}
for m in MOTIF.finditer(texte): occ.setdefault(m.group(1),[]).append(m.end())
bil={}
for ch,fins in sorted(occ.items()):
    if any(i in ch for i in INTERDITS):
        e="non ouvert (interdit)"; bil[e]=bil.get(e,0)+1; print(e+"\t"+ch); continue
    tr=[]
    if "/" in ch: cands=[depot/ch, copie/ch]
    else: cands=[c for r in nus for c in list(r.rglob(ch))[:12]]
    for c in cands:
        if c.is_file() and not any(i in str(c) for i in INTERDITS): tr.append(hashlib.sha256(c.read_bytes()).hexdigest())
    ci=[]
    for f in fins: ci+=re.findall(r"(?<![0-9a-f])([0-9a-f]{8,64})(?![0-9a-f])",texte[f:f+500])
    if not tr: e="introuvable"
    elif not ci: e="sans empreinte voisine"
    elif any(h.startswith(c) for h in tr for c in ci): e="conforme"
    else: e="à regarder"
    bil[e]=bil.get(e,0)+1
    if e!="conforme": print(e+"\t"+ch+("\tcalculé "+", ".join(sorted({h[:16] for h in tr})) if tr else ""))
print(bil)
