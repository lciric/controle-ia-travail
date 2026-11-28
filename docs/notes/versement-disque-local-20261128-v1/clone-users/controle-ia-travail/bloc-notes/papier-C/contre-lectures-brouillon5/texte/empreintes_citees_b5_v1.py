"""Contre-lecture texte du brouillon 5 : pour chaque empreinte (complète ou abrégée) citée, retrouve le fichier cité
et recalcule son sha256. Lecture seule ; aucune recherche récursive : seuls les chemins écrits dans le texte sont
ouverts, plus les fichiers du dossier de travail de la session nommés explicitement ci-dessous."""
import hashlib, re, sys, pathlib
texte_path, R, P = sys.argv[1], pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3])
texte = pathlib.Path(texte_path).read_text(encoding="utf-8")
lignes = texte.splitlines()
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
# chemins cités entre accents graves
chemins = sorted(set(re.findall(r"`([A-Za-z0-9_./-]+\.(?:md|json|txt|py|pdf))`", texte)))
# lieux de recherche : le dépôt (chemin relatif tel quel) ; dossiers de travail nommés par le texte
lieux = [R, P, P / "brouillon5", P / "brouillon5" / "outils", P / "brouillon5" / "notes", P / "contre-lectures",
         P / "contre-lectures" / "simulations-methode", P / "contre-lectures" / "outils-panin", P / "mesures",
         R / "docs/sources/lecture-pdf-niveau2", R / "donnees/P1-items-gabarit-v1", R / "docs/notes/papier-C-mesures-v1"]
index = {}
for c in chemins:
    trouves = []
    for L in lieux:
        for cand in (L / c, L / pathlib.Path(c).name):
            if cand.is_file():
                trouves.append(cand)
    trouves = sorted(set(trouves))
    index[c] = [(str(t), sha(t)) for t in trouves]
for c in chemins:
    if not index[c]:
        print(f"ABSENT  {c}")
    for t, h in index[c]:
        print(f"{h[:16]}  {c}  <- {t}")
# empreintes citées
complets = sorted(set(re.findall(r"\b[0-9a-f]{64}\b", texte)))
abreges = sorted(set(re.findall(r"\b([0-9a-f]{8})…", texte)))
tous = {h for v in index.values() for _, h in v}
print("\n# empreintes complètes citées sans fichier retrouvé à ces chemins :")
for h in complets:
    if h not in tous:
        i = next(k for k, l in enumerate(lignes, 1) if h in l)
        print(f"  l. {i} : {h}")
print("# empreintes abrégées citées sans fichier retrouvé :")
for a in abreges:
    if not any(h.startswith(a) for h in tous) and not any(h.startswith(a) for h in complets):
        i = next(k for k, l in enumerate(lignes, 1) if a + "…" in l)
        print(f"  l. {i} : {a}…")
