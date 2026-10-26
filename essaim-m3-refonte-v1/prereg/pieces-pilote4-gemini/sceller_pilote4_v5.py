"""Graines et empreintes du texte v5 du pilote 4 (la v6.2.1 sur la question M, puis sur la question S ; banque
`confrontation-v3`, conception puis quatre générations, en segments) : tire l'entropie, dérive la graine de la course S
(enfant 0 de SeedSequence(E).spawn(2) ; l'enfant 1 n'est pas écrit), écrit le fichier d'empreintes des pièces et des
contre-lectures, remplit les champs attendus et eux seuls, écrit le compagnon `.sha256` — v5 (pilote de conception : ni
préenregistrement ni scellement au sens de R1 ; le script ne fait que ce que le lanceur v11 exige).

Usage : python -I sceller_pilote4_v5.py PREREG DOSSIER_PIECES DOSSIER_CONTRE_LECTURES CLE_S
v5 (texte v5, R-492 : la v5.3 ne court pas, la seconde course est la v6.2.1 sur la question S) : marqueurs
`<<ENTROPIE>>`, `<<GRAINE_S>>`, `<<EMPREINTE_PIECES>>` ; la ligne « graine de la course v6-2 = 2334107546136117589 »
(graine de la course M, texte v4) doit être présente, une fois, telle quelle (porte « course M précédente » du lanceur
v11) ; écrit `EMPREINTES-pilote4-gemini-v3.txt` (les fichiers v1 et v2 sont ceux des textes v3 et v4 : jamais réécrits).
v3 (contre-lecture 2, P4C2-08) : refuse aussi un texte qui porte **une ligne d'entropie ou de graine de trop** (un texte
inséré au scellement, par exemple le détail d'une contre-lecture, qui en contiendrait une : le lanceur lit la première
ligne d'entropie et recalculerait d'autres graines) — exactement une ligne qui porte « entropie E = », sans nombre avant
le remplissage ; exactement deux lignes « graine de la course … = », celles des deux marqueurs ; après le remplissage,
une seule entropie écrite et les deux graines recalculées depuis elle ; essayé sur un cas sain et sur des artefacts
(`essais_scellement_pilote4_v3.sh`).
v2 (contre-lecture 1, P4C1-14 a) : documentation juste (banque v3) ; **exige au moins une contre-lecture du texte
scellé** (`<nom du texte>-clN.md` dans DOSSIER_CONTRE_LECTURES, avec son compagnon `.sha256` juste) ; refuse une
contre-lecture sans compagnon.
Comme la v1 (dérivée de `sceller_pilote3_v2.py`) : l'enfant 0 de SeedSequence(E).spawn(2) est la graine de la course
**CLE_S** (la course S ; v5 : l'enfant 1 n'est pas écrit) ; fichier d'empreintes
`EMPREINTES-pilote4-gemini-v2.txt` (toutes les pièces sous DOSSIER_PIECES, et les contre-lectures
`pilote4-gemini-organisme-*`).
Refuse : numpy < 1.25 (R9) ; un marqueur de rédaction `[[…]]` restant ; un autre marqueur de scellement que ceux
attendus, ou l'un d'eux absent ou en double ; une ligne de graine ou d'entropie absente, en double ou de trop ; aucune
contre-lecture du texte ; une contre-lecture sans compagnon, ou un compagnon faux ; un fichier d'empreintes existant (R12).
"""
import hashlib, pathlib, re, secrets, sys
import numpy

if tuple(int(x) for x in numpy.__version__.split(".")[:2]) < (1, 25):
    sys.exit(f"refus : numpy {numpy.__version__} < 1.25 (R9)")

prereg, pieces, cl, cle = (pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), sys.argv[4])
if not re.fullmatch(r"v6-[0-9]+-s", cle):
    sys.exit(f"refus : clé de course {cle!r} inattendue")
texte = prereg.read_text(encoding="utf-8")
if re.search(r"\[\[[A-Z0-9_]+\]\]", texte):
    sys.exit("refus : marqueurs de rédaction [[…]] restants : " + ", ".join(sorted(set(re.findall(r"\[\[[A-Z0-9_]+\]\]", texte)))))
attendus = {"<<ENTROPIE>>", "<<GRAINE_S>>", "<<EMPREINTE_PIECES>>"}
trouves = set(re.findall(r"<<[A-Z0-9_]+>>", texte))
if trouves != attendus:
    sys.exit(f"refus : marqueurs {sorted(trouves)} au lieu de {sorted(attendus)}")
for m in attendus:
    if texte.count(m) != 1:
        sys.exit(f"refus : {m} présent {texte.count(m)} fois")
GRAINE_M = "graine de la course v6-2 = 2334107546136117589"   # graine de la course M (texte v4, enfant 1 de son entropie)
for ligne in (f"graine de la course {cle} = <<GRAINE_S>>", GRAINE_M, "entropie E = <<ENTROPIE>>"):
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
graines_attendues = sorted([f"graine de la course {cle} = <<GRAINE_S>>", GRAINE_M])
if lignes_graine != graines_attendues:
    sys.exit(f"refus : lignes de graine {lignes_graine} au lieu de {graines_attendues}")

# contre-lectures : toutes avec un compagnon juste ; au moins une du texte scellé
cls = sorted(p for p in cl.glob("pilote4-gemini-organisme-*") if p.is_file())
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

sortie = pieces / "EMPREINTES-pilote4-gemini-v3.txt"
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
texte = (texte.replace("<<ENTROPIE>>", str(e)).replace("<<GRAINE_S>>", str(g[0]))
              .replace("<<EMPREINTE_PIECES>>", f"`{h_emp}`"))
if re.search(r"<<[A-Z0-9_]+>>", texte):
    sys.exit("refus : marqueur restant après remplissage")
# garde après remplissage : ce que le lanceur lira (première entropie, deux lignes de graine) est ce qui vient d'être tiré
if re.findall(r"entropie E = ([0-9]+)", texte) != [str(e)]:
    sys.exit("refus : après remplissage, l'entropie écrite n'est pas unique ou n'est pas celle tirée")
if re.findall(r"graine de la course " + re.escape(cle) + r" = ([0-9]+)", texte) != [str(g[0])]:
    sys.exit(f"refus : après remplissage, la graine de la course {cle} n'est pas unique ou n'est pas celle dérivée")
if texte.count(GRAINE_M) != 1 or re.findall(r"graine de la course v6-2 = ([0-9]+)", texte) != ["2334107546136117589"]:
    sys.exit("refus : après remplissage, la graine de la course M n'est pas unique ou n'est pas celle du texte v4")
prereg.write_text(texte, encoding="utf-8")
h = hashlib.sha256(prereg.read_bytes()).hexdigest()
pathlib.Path(str(prereg) + ".sha256").write_text(f"{h}  {prereg.name}\n", encoding="utf-8")
print(f"graines écrites : {prereg.name} {h} ; entropie {e} ; graine {cle} {g[0]} (enfant 0 ; enfant 1 non utilisé) ; numpy {numpy.__version__} ; "
      f"empreintes des pièces {h_emp} ({len(fichiers)} fichiers, dont {len(cls)} de contre-lecture ; "
      f"contre-lectures du texte : {', '.join(p.name for p in propres)})")
