"""Scellement du préenregistrement du second pilote pour la v5.2 : tire l'entropie, dérive les deux graines, écrit le
fichier d'empreintes des pièces, remplit les champs du scellement et eux seuls, écrit le compagnon `.sha256`.

Usage : python -I sceller_pilote2_v3.py PREREG DOSSIER_PIECES DOSSIER_CONTRE_LECTURES
(v3 : la v2, gardée, scellait le texte de la v5.1 ; ici l'enfant 0 de SeedSequence(E).spawn(2) est la graine de la
course **maïeutique** (première course) et l'enfant 1 celle de la course **structure** ; fichier d'empreintes
`EMPREINTES-pilote2-gemini-v5-2-v2.txt` ; contre-lectures `pilote2-gemini-organisme-v5-2-*`.)
Refuse si un autre marqueur que ceux du scellement reste, ou si l'un manque. N'écrase aucun fichier d'empreintes existant.
"""
import hashlib, pathlib, re, secrets, sys
import numpy

prereg, pieces, cl = (pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]))
texte = prereg.read_text(encoding="utf-8")
attendus = {"<<ENTROPIE>>", "<<GRAINE_MAIEUTIQUE>>", "<<GRAINE_STRUCTURE>>", "<<EMPREINTE_PIECES>>"}
trouves = set(re.findall(r"<<[A-Z0-9_]+>>", texte))
if trouves != attendus:
    sys.exit(f"refus : marqueurs {sorted(trouves)} au lieu de {sorted(attendus)}")
for m in attendus:
    if texte.count(m) != 1:
        sys.exit(f"refus : {m} présent {texte.count(m)} fois")

# empreintes des pièces (toutes, compagnons compris) et des contre-lectures du pilote
sortie = pieces / "EMPREINTES-pilote2-gemini-v5-2-v2.txt"
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
fichiers = sorted(p for p in pieces.rglob("*") if p.is_file() and p.name not in (sortie.name, sortie.name + ".sha256"))
fichiers += sorted(p for p in cl.glob("pilote2-gemini-organisme-v5-2-*") if p.is_file())
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
              .replace("<<GRAINE_MAIEUTIQUE>>", str(g[0]))
              .replace("<<GRAINE_STRUCTURE>>", str(g[1]))
              .replace("<<EMPREINTE_PIECES>>", f"`{h_emp}`"))
if re.search(r"<<[A-Z0-9_]+>>", texte):
    sys.exit("refus : marqueur restant après remplissage")
prereg.write_text(texte, encoding="utf-8")
h = hashlib.sha256(prereg.read_bytes()).hexdigest()
pathlib.Path(str(prereg) + ".sha256").write_text(f"{h}  {prereg.name}\n", encoding="utf-8")
print(f"scellé : {prereg.name} {h} ; graines M {g[0]}, S {g[1]} ; numpy {numpy.__version__} ; empreintes des pièces {h_emp} ({len(fichiers)} fichiers)")
