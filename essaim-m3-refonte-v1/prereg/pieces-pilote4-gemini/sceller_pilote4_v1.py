"""Scellement du préenregistrement du pilote 4 (v5.3 puis v6.x, banque v2, conception puis quatre générations) : tire
l'entropie, dérive les deux graines, écrit le fichier d'empreintes des pièces et des contre-lectures, remplit les champs
du scellement et eux seuls, écrit le compagnon `.sha256` — v1.

Usage : python -I sceller_pilote4_v1.py PREREG DOSSIER_PIECES DOSSIER_CONTRE_LECTURES CLE_V6X
Dérivé de `sceller_pilote3_v2.py` : l'enfant 0 de SeedSequence(E).spawn(2) est la graine de la course **v5-3**
(première course), l'enfant 1 celle de la course **CLE_V6X** (p. ex. `v6-2`) ; fichier d'empreintes
`EMPREINTES-pilote4-gemini-v1.txt` ; contre-lectures `pilote4-gemini-organisme-*`.
Refuse : numpy < 1.25 (R9) ; un marqueur de rédaction `[[…]]` restant ; un autre marqueur de scellement que ceux attendus,
ou l'un d'eux absent ou en double ; une ligne de graine absente ; un fichier d'empreintes existant (R12) ; un compagnon de
contre-lecture faux.
"""
import hashlib, pathlib, re, secrets, sys
import numpy

if tuple(int(x) for x in numpy.__version__.split(".")[:2]) < (1, 25):
    sys.exit(f"refus : numpy {numpy.__version__} < 1.25 (R9)")

prereg, pieces, cl, cle = (pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), sys.argv[4])
if not re.fullmatch(r"v6-[0-9]+", cle):
    sys.exit(f"refus : clé de course {cle!r} inattendue")
texte = prereg.read_text(encoding="utf-8")
if re.search(r"\[\[[A-Z0-9_]+\]\]", texte):
    sys.exit("refus : marqueurs de rédaction [[…]] restants : " + ", ".join(sorted(set(re.findall(r"\[\[[A-Z0-9_]+\]\]", texte)))))
attendus = {"<<ENTROPIE>>", "<<GRAINE_V53>>", "<<GRAINE_V6X>>", "<<EMPREINTE_PIECES>>"}
trouves = set(re.findall(r"<<[A-Z0-9_]+>>", texte))
if trouves != attendus:
    sys.exit(f"refus : marqueurs {sorted(trouves)} au lieu de {sorted(attendus)}")
for m in attendus:
    if texte.count(m) != 1:
        sys.exit(f"refus : {m} présent {texte.count(m)} fois")
for ligne in ("graine de la course v5-3 = <<GRAINE_V53>>", f"graine de la course {cle} = <<GRAINE_V6X>>",
              "entropie E = <<ENTROPIE>>"):
    if ligne not in texte:
        sys.exit(f"refus : ligne absente : {ligne}")

# compagnons des contre-lectures vérifiés avant tout
cls = sorted(p for p in cl.glob("pilote4-gemini-organisme-*") if p.is_file())
for p in cls:
    if p.name.endswith(".sha256"):
        nom = p.read_text(encoding="utf-8").split()
        cible = cl / nom[1]
        if hashlib.sha256(cible.read_bytes()).hexdigest() != nom[0]:
            sys.exit(f"refus : compagnon {p.name} faux")

sortie = pieces / "EMPREINTES-pilote4-gemini-v1.txt"
if sortie.exists() or (pieces / (sortie.name + ".sha256")).exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
fichiers = sorted(p for p in pieces.rglob("*") if p.is_file() and p.name not in (sortie.name, sortie.name + ".sha256"))
fichiers += cls
lignes = [f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(prereg.parent)}" for p in fichiers]
sortie.write_text("\n".join(lignes) + "\n", encoding="utf-8")
h_emp = hashlib.sha256(sortie.read_bytes()).hexdigest()
(pieces / (sortie.name + ".sha256")).write_text(f"{h_emp}  {sortie.name}\n", encoding="utf-8")

e = secrets.randbits(128)
enfants = numpy.random.SeedSequence(e).spawn(2)
g = [int(c.generate_state(1, dtype=numpy.uint64)[0]) for c in enfants]
texte = (texte.replace("<<ENTROPIE>>", str(e)).replace("<<GRAINE_V53>>", str(g[0]))
              .replace("<<GRAINE_V6X>>", str(g[1])).replace("<<EMPREINTE_PIECES>>", f"`{h_emp}`"))
if re.search(r"<<[A-Z0-9_]+>>", texte):
    sys.exit("refus : marqueur restant après remplissage")
prereg.write_text(texte, encoding="utf-8")
h = hashlib.sha256(prereg.read_bytes()).hexdigest()
pathlib.Path(str(prereg) + ".sha256").write_text(f"{h}  {prereg.name}\n", encoding="utf-8")
print(f"scellé : {prereg.name} {h} ; entropie {e} ; graines v5-3 {g[0]}, {cle} {g[1]} ; numpy {numpy.__version__} ; "
      f"empreintes des pièces {h_emp} ({len(fichiers)} fichiers, dont {len(cls)} de contre-lecture)")
