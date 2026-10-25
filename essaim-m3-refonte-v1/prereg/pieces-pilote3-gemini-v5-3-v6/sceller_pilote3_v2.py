"""Scellement du préenregistrement du pilote 3 (v5.3 puis v6) : tire l'entropie, dérive les deux graines, écrit le
fichier d'empreintes des pièces, remplit les champs du scellement et eux seuls, écrit le compagnon `.sha256`.

Usage : python -I sceller_pilote3_v2.py PREREG DOSSIER_PIECES DOSSIER_CONTRE_LECTURES
(v2 : la v1, gardée, ne vérifiait pas numpy ≥ 1.25 (R9 ; P3C1-13) ; la v2 refuse sinon.)
Dérivé de `sceller_pilote2_v3.py` (second pilote) : l'enfant 0 de SeedSequence(E).spawn(2) est la graine de la course
**v5-3** (première course) et l'enfant 1 celle de la course **v6** ; fichier d'empreintes
`EMPREINTES-pilote3-gemini-v5-3-v6-v1.txt` ; contre-lectures `pilote3-gemini-organisme-v5-3-v6-*`.
Refuse si un autre marqueur que ceux du scellement reste, ou si l'un manque. N'écrase aucun fichier d'empreintes existant.
"""
import hashlib, pathlib, re, secrets, sys
import numpy

if tuple(int(x) for x in numpy.__version__.split(".")[:2]) < (1, 25):
    sys.exit(f"refus : numpy {numpy.__version__} < 1.25 (R9)")

prereg, pieces, cl = (pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]))
texte = prereg.read_text(encoding="utf-8")
attendus = {"<<ENTROPIE>>", "<<GRAINE_V53>>", "<<GRAINE_V6>>", "<<EMPREINTE_PIECES>>"}
trouves = set(re.findall(r"<<[A-Z0-9_]+>>", texte))
if trouves != attendus:
    sys.exit(f"refus : marqueurs {sorted(trouves)} au lieu de {sorted(attendus)}")
for m in attendus:
    if texte.count(m) != 1:
        sys.exit(f"refus : {m} présent {texte.count(m)} fois")

# empreintes des pièces (toutes, compagnons compris) et des contre-lectures du pilote
sortie = pieces / "EMPREINTES-pilote3-gemini-v5-3-v6-v1.txt"
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
fichiers = sorted(p for p in pieces.rglob("*") if p.is_file() and p.name not in (sortie.name, sortie.name + ".sha256"))
fichiers += sorted(p for p in cl.glob("pilote3-gemini-organisme-v5-3-v6-*") if p.is_file())
lignes = []
for p in fichiers:
    rel = p.relative_to(prereg.parent)
    lignes.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {rel}")
sortie.write_text("\n".join(lignes) + "\n", encoding="utf-8")
h_emp = hashlib.sha256(sortie.read_bytes()).hexdigest()
(pieces / (sortie.name + ".sha256")).write_text(f"{h_emp}  {sortie.name}\n", encoding="utf-8")

e = secrets.randbits(128)
enfants = numpy.random.SeedSequence(e).spawn(2)
g = [int(c.generate_state(1, dtype=numpy.uint64)[0]) for c in enfants]
texte = (texte.replace("<<ENTROPIE>>", str(e))
              .replace("<<GRAINE_V53>>", str(g[0]))
              .replace("<<GRAINE_V6>>", str(g[1]))
              .replace("<<EMPREINTE_PIECES>>", f"`{h_emp}`"))
if re.search(r"<<[A-Z0-9_]+>>", texte):
    sys.exit("refus : marqueur restant après remplissage")
prereg.write_text(texte, encoding="utf-8")
h = hashlib.sha256(prereg.read_bytes()).hexdigest()
pathlib.Path(str(prereg) + ".sha256").write_text(f"{h}  {prereg.name}\n", encoding="utf-8")
print(f"scellé : {prereg.name} {h} ; graines v5-3 {g[0]}, v6 {g[1]} ; numpy {numpy.__version__} ; empreintes des pièces {h_emp} ({len(fichiers)} fichiers)")
