"""Vérifie, après le scellement, le texte du pilote 4 comme le lanceur le lira — v2 (conv-audit, 26 octobre 2026) :
la v1 pour le texte v4 (objet v6.2 : clé de course `v6-2` ; fichier d'empreintes `EMPREINTES-pilote4-gemini-v2.txt`),
rien d'autre ne change.

Usage : python -I verifier_scellement_pilote4_v2.py TEXTE_SCELLE DOSSIER_PIECES DOSSIER_CONTRE_LECTURES
Vérifie : compagnon `.sha256` du texte juste ; aucun marqueur restant (`[[…]]`, `<<…>>` hors des chevrons simples de la
ligne de GO) ; une seule ligne qui porte « entropie E = » et elle porte un nombre ; exactement deux lignes de graine,
v5-3 et v6-2, égales aux enfants 0 et 1 de SeedSequence(E).spawn(2) (comme le lanceur les recalcule) ; le fichier
d'empreintes des pièces cité par le texte existe, son empreinte est celle que le texte écrit, et toutes ses lignes sont
justes ; il couvre les contre-lectures du texte. N'écrit rien. Code 0 si tout est juste, 1 sinon.
"""
import hashlib, pathlib, re, sys
import numpy

texte_p, pieces, cl = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3])
pb = []
b = texte_p.read_bytes()
sha = hashlib.sha256(b).hexdigest()
comp = texte_p.with_name(texte_p.name + ".sha256")
if not comp.is_file() or comp.read_text(encoding="utf-8").split()[:1] != [sha]:
    pb.append("compagnon du texte absent ou faux")
t = b.decode("utf-8")
if re.search(r"\[\[[A-Z0-9_]+\]\]", t): pb.append("marqueur [[…]] restant")
if re.search(r"<<[A-Z0-9_]+>>", t): pb.append("marqueur <<…>> restant")
le = [l for l in t.splitlines() if "entropie E =" in l]
if len(le) != 1: pb.append(f"{len(le)} lignes d'entropie")
m = re.search(r"entropie E = ([0-9]+)", t)
if not m: pb.append("entropie illisible")
lg = [l.strip() for l in t.splitlines() if re.search(r"graine de la course \S+ =", l)]
if len(lg) != 2: pb.append(f"{len(lg)} lignes de graine")
if m:
    E = int(m.group(1))
    enfants = numpy.random.SeedSequence(E).spawn(2)
    g = [int(e.generate_state(1, dtype=numpy.uint64)[0]) for e in enfants]
    for cle, attendu in (("v5-3", g[0]), ("v6-2", g[1])):
        mm = re.search(rf"graine de la course {cle} = ([0-9]+)", t)
        if not mm or int(mm.group(1)) != attendu:
            pb.append(f"graine {cle} : écrite {mm.group(1) if mm else None}, recalculée {attendu}")
    print(f"entropie {E} ; graine v5-3 {g[0]} ; graine v6-2 {g[1]} (recalculées)")
emp = pieces / "EMPREINTES-pilote4-gemini-v2.txt"
if not emp.is_file():
    pb.append("EMPREINTES-pilote4-gemini-v2.txt absent")
else:
    se = hashlib.sha256(emp.read_bytes()).hexdigest()
    if se not in t: pb.append("le texte n'écrit pas l'empreinte du fichier d'empreintes")
    n_ok = n = 0
    noms = []
    for ligne in emp.read_text(encoding="utf-8").splitlines():
        if not ligne.strip(): continue
        h, nom = ligne.split(None, 1)
        nom = nom.strip()
        noms.append(nom)
        cand = [pieces / nom, cl / pathlib.Path(nom).name, pieces.parent / nom]
        f = next((c for c in cand if c.is_file()), None)
        n += 1
        if f is not None and hashlib.sha256(f.read_bytes()).hexdigest() == h: n_ok += 1
        else: pb.append(f"empreinte fausse ou fichier introuvable : {nom}")
    print(f"fichier d'empreintes {se[:16]}… : {n_ok} lignes justes sur {n}")
    cls = sorted(p.name for p in cl.glob(texte_p.stem + "-cl*.md"))
    manquantes = [c for c in cls if not any(x.endswith(c) for x in noms)]
    if manquantes: pb.append(f"contre-lectures absentes du fichier d'empreintes : {manquantes}")
    print(f"contre-lectures du texte : {cls}")
print("texte scellé :", texte_p.name, sha)
if pb:
    print("PROBLÈMES : " + " ; ".join(pb)); sys.exit(1)
print("vérification : tout est juste")
