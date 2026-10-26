"""Graines et empreintes du texte des deux courses à question de la v6.2.1 (course « maieutique », GO-2026-10-26-05 ;
course « audit », GO-2026-10-26-04 partie (2) ; banque `confrontation-v3`, conception puis quatre générations, en
segments) : tire une entropie, dérive les deux graines (enfants 0 et 1 de SeedSequence(E).spawn(2) : enfant 0 pour la
course `maieutique`, enfant 1 pour la course `audit`), écrit le fichier d'empreintes des pièces et des contre-lectures,
remplit les champs attendus et eux seuls, écrit le compagnon `.sha256` — v6 (pilote de conception : ni préenregistrement
ni scellement au sens de R1 ; le script ne fait que ce que le lanceur v12 exige).

Usage : python -I sceller_courses_question_v6.py TEXTE DOSSIER_PIECES DOSSIER_CONTRE_LECTURES
v6 (dérivé de `sceller_pilote4_v5.py`) : marqueurs `<<ENTROPIE>>`, `<<GRAINE_MAIEUTIQUE>>`, `<<GRAINE_AUDIT>>`,
`<<EMPREINTE_PIECES>>` ; exactement deux lignes « graine de la course … = », celles des deux marqueurs ; aucune ligne de
graine héritée n'est exigée (rien n'est demandé des courses du pilote 4) ; écrit `EMPREINTES-courses-question-v1.txt`
(les fichiers `EMPREINTES-pilote4-gemini-v*.txt` sont ceux des textes du pilote 4 : jamais réécrits). Le reste est celui
de la v5 : une seule ligne d'entropie, sans nombre avant le remplissage (P4C2-08) ; au moins une contre-lecture du texte
(`<nom du texte>-clN.md`) avec son compagnon juste ; refuse numpy < 1.25 (R9), un marqueur de rédaction `[[…]]`, un
marqueur de scellement absent, en double ou de trop, un fichier d'empreintes existant (R12).
"""
import hashlib, pathlib, re, secrets, sys
import numpy

if tuple(int(x) for x in numpy.__version__.split(".")[:2]) < (1, 25):
    sys.exit(f"refus : numpy {numpy.__version__} < 1.25 (R9)")

prereg, pieces, cl = (pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]))
texte = prereg.read_text(encoding="utf-8")
if re.search(r"\[\[[A-Z0-9_]+\]\]", texte):
    sys.exit("refus : marqueurs de rédaction [[…]] restants : " + ", ".join(sorted(set(re.findall(r"\[\[[A-Z0-9_]+\]\]", texte)))))
attendus = {"<<ENTROPIE>>", "<<GRAINE_MAIEUTIQUE>>", "<<GRAINE_AUDIT>>", "<<EMPREINTE_PIECES>>"}
trouves = set(re.findall(r"<<[A-Z0-9_]+>>", texte))
if trouves != attendus:
    sys.exit(f"refus : marqueurs {sorted(trouves)} au lieu de {sorted(attendus)}")
for m in attendus:
    if texte.count(m) != 1:
        sys.exit(f"refus : {m} présent {texte.count(m)} fois")
for ligne in ("graine de la course maieutique = <<GRAINE_MAIEUTIQUE>>", "graine de la course audit = <<GRAINE_AUDIT>>",
              "entropie E = <<ENTROPIE>>"):
    if ligne not in texte:
        sys.exit(f"refus : ligne absente : {ligne}")
# P4C2-08 : une seule ligne d'entropie (le lanceur lit la première), sans nombre avant le remplissage ; les seules lignes
# de graine sont celles des deux marqueurs
lignes_entropie = [l for l in texte.splitlines() if "entropie E =" in l]
if len(lignes_entropie) != 1:
    sys.exit(f"refus : {len(lignes_entropie)} lignes qui portent « entropie E = » au lieu d'une (le lanceur lit la première)")
if re.search(r"entropie E = [0-9]", texte):
    sys.exit("refus : une ligne d'entropie porte déjà un nombre avant le scellement")
lignes_graine = sorted(l.strip() for l in texte.splitlines() if re.search(r"graine de la course \S+ =", l))
graines_attendues = sorted(["graine de la course maieutique = <<GRAINE_MAIEUTIQUE>>", "graine de la course audit = <<GRAINE_AUDIT>>"])
if lignes_graine != graines_attendues:
    sys.exit(f"refus : lignes de graine {lignes_graine} au lieu de {graines_attendues}")

# contre-lectures : toutes avec un compagnon juste ; au moins une du texte scellé
cls = sorted(p for p in cl.glob(prereg.stem + "-*") if p.is_file())
for p in cls:
    if p.name.endswith(".sha256"):
        nom = p.read_text(encoding="utf-8").split()
        cible = cl / nom[1]
        if not cible.is_file() or hashlib.sha256(cible.read_bytes()).hexdigest() != nom[0]:
            sys.exit(f"refus : compagnon {p.name} faux")
    elif not (cl / (p.name + ".sha256")).is_file():
        sys.exit(f"refus : contre-lecture {p.name} sans compagnon .sha256")
propres = [p for p in cls if re.fullmatch(re.escape(prereg.stem) + r"-cl[0-9]+\.md", p.name)]
if not propres:
    sys.exit(f"refus : aucune contre-lecture de {prereg.name} ({prereg.stem}-clN.md) dans {cl}")

sortie = pieces / "EMPREINTES-courses-question-v1.txt"
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
texte = (texte.replace("<<ENTROPIE>>", str(e)).replace("<<GRAINE_MAIEUTIQUE>>", str(g[0]))
              .replace("<<GRAINE_AUDIT>>", str(g[1])).replace("<<EMPREINTE_PIECES>>", f"`{h_emp}`"))
if re.search(r"<<[A-Z0-9_]+>>", texte):
    sys.exit("refus : marqueur restant après remplissage")
# garde après remplissage : ce que le lanceur lira (première entropie, deux lignes de graine) est ce qui vient d'être tiré
if re.findall(r"entropie E = ([0-9]+)", texte) != [str(e)]:
    sys.exit("refus : après remplissage, l'entropie écrite n'est pas unique ou n'est pas celle tirée")
if re.findall(r"graine de la course maieutique = ([0-9]+)", texte) != [str(g[0])]:
    sys.exit("refus : après remplissage, la graine de la course maieutique n'est pas unique ou n'est pas celle dérivée")
if re.findall(r"graine de la course audit = ([0-9]+)", texte) != [str(g[1])]:
    sys.exit("refus : après remplissage, la graine de la course audit n'est pas unique ou n'est pas celle dérivée")
prereg.write_text(texte, encoding="utf-8")
h = hashlib.sha256(prereg.read_bytes()).hexdigest()
pathlib.Path(str(prereg) + ".sha256").write_text(f"{h}  {prereg.name}\n", encoding="utf-8")
print(f"graines écrites : {prereg.name} {h} ; entropie {e} ; graine maieutique {g[0]} (enfant 0) ; graine audit {g[1]} (enfant 1) ; "
      f"numpy {numpy.__version__} ; empreintes des pièces {h_emp} ({len(fichiers)} fichiers, dont {len(cls)} de contre-lecture ; "
      f"contre-lectures du texte : {', '.join(p.name for p in propres)})")
