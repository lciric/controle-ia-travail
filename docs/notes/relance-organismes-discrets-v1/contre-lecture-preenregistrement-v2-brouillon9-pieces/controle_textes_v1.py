"""Contre-lecture 9 : (1) empreintes des deux blocs de consigne et compte des marques ; (2) textes transmis par la
session mère : chaque citation entre guillemets (imbrication suivie) est-elle une sous-chaîne exacte du brouillon 9 ;
(3) fiches de décision des deux fichiers : sous-chaînes exactes du brouillon 9 ?"""
import hashlib, pathlib, re
B9 = pathlib.Path("prereg/T0.7-organismes-discrets-v-a-v2-brouillon9.md").read_text(encoding="utf-8")
L = B9.splitlines()
# (1) consignes
blocs, dedans, cour = [], False, []
for l in L:
    if l.startswith("```"):
        if dedans: blocs.append("\n".join(cour)); cour = []
        dedans = not dedans; continue
    if dedans: cour.append(l)
print("blocs de code :", len(blocs))
for b, marques in zip(blocs, (("{title}", "{proposal}", "{controls}"), ("{plan}", "{reference}"))):
    print(" ", hashlib.sha256(b.encode()).hexdigest(), len(b), "caractères ;", {m: b.count(m) for m in marques})
# (2) textes de la mère
M = pathlib.Path("docs/notes/relance-organismes-discrets-v1/textes-des-moniteurs-transmis-par-la-mere-v1.md").read_text(encoding="utf-8")
def citations(s):
    out, prof, deb = [], 0, None
    for i, ch in enumerate(s):
        if ch == "«":
            if prof == 0: deb = i + 1
            prof += 1
        elif ch == "»" and prof:
            prof -= 1
            if prof == 0: out.append(s[deb:i].strip())
    return out
cits = [c for c in citations(M) if len(c) > 60]
print("citations longues du texte de la mère :", len(cits))
for c in cits:
    print("  ", "OK " if c in B9 else "ABSENTE", c[:70].replace("\n", " "), "…", f"({len(c)} car.)")
# phrases hors guillemets des points 1 bis et 1 ter, reprises au brouillon ?
for frag in ["Les vingt et un traits suivent les cinq familles du texte archivé : longueur en jetons ; nombre de champs remplis ; ordre des champs (indicateur d'ordre canonique, puis rang de chacun des cinq champs) ; comptes de ponctuation par les sept catégories d'Unicode ; six indicateurs de forme du champ du coût, pris au lecteur gelé.",
             "Une permutation perdue ne peut venir que d'un moniteur appris (ajustement non convergé) : la permutation dans chaque tâche garde les effectifs de chaque classe."]:
    print("  hors guillemets :", "OK " if frag in B9 else "ABSENTE", frag[:60], "…")
# (3) fiches
for f in ("decisions-bras-a-brouillon7-v1.md", "decisions-bras-a-brouillon9-v1.md"):
    F = pathlib.Path("docs/notes/relance-organismes-discrets-v1/" + f).read_text(encoding="utf-8")
    puces = [l.strip() for l in F.splitlines() if l.strip().startswith("- **") and ("Option" in l or "Enjeu" in l or "Recommandation" in l or "Défaut" in l or "Décision" in l or "Divergence" in l)]
    manq = [p for p in puces if p.lstrip("- ").strip() not in B9 and p[2:].strip() not in B9]
    print(f, ": puces", len(puces), "; absentes du brouillon 9 :", len(manq))
    for p in manq: print("    ", p[:100])
