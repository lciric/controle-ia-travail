# Contrôle indépendant (contre-lecture 5), lecture seule du texte : reprend les gardes d'avant remplissage de
# sceller_pilote4_v4.py (l. 32-58) et celles du lanceur v10 (étape 2) sur une copie remplie en mémoire, valeurs d'essai.
import re, sys, pathlib
import numpy
t = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
cle = "v6-2"
# remplissage à la main simulé des deux marqueurs de rédaction (texte neutre, sans ligne d'entropie ni de graine)
t = t.replace("[[CONTRE_LECTURE]]", "cinq (essai)").replace("[[CONTRE_LECTURE_DETAIL]]", "- contre-lecture 5 (essai) : texte relu efb13feb…")
pb = []
if re.search(r"\[\[[A-Z0-9_]+\]\]", t): pb.append("[[…]] restant")
att = {"<<ENTROPIE>>", "<<GRAINE_V53>>", "<<GRAINE_V6X>>", "<<EMPREINTE_PIECES>>"}
if set(re.findall(r"<<[A-Z0-9_]+>>", t)) != att: pb.append("marqueurs")
for m in att:
    if t.count(m) != 1: pb.append(m + " pas une fois")
for l in ("graine de la course v5-3 = <<GRAINE_V53>>", f"graine de la course {cle} = <<GRAINE_V6X>>", "entropie E = <<ENTROPIE>>"):
    if l not in t: pb.append("ligne absente " + l)
if len([l for l in t.splitlines() if "entropie E =" in l]) != 1: pb.append("lignes d'entropie")
if re.search(r"entropie E = [0-9]", t): pb.append("entropie déjà chiffrée")
lg = sorted(l.strip() for l in t.splitlines() if re.search(r"graine de la course \S+ =", l))
if lg != sorted(["graine de la course v5-3 = <<GRAINE_V53>>", f"graine de la course {cle} = <<GRAINE_V6X>>"]): pb.append("lignes de graine " + str(lg))
print("gardes du script de scellement (avant remplissage) :", "conformes" if not pb else pb)
# remplissage d'essai (valeurs d'essai, jamais celles du pilote)
E = 123456789012345678901234567890
g = [int(c.generate_state(1, dtype=numpy.uint64)[0]) for c in numpy.random.SeedSequence(E).spawn(2)]
t2 = t.replace("<<ENTROPIE>>", str(E)).replace("<<GRAINE_V53>>", str(g[0])).replace("<<GRAINE_V6X>>", str(g[1])).replace("<<EMPREINTE_PIECES>>", "`" + "0"*64 + "`")
# ce que lit le lanceur v10 (étape 2)
e_txt = re.findall(r"entropie E = [0-9]+", t2)[0].split("= ")[1]
ok = []
ok.append(int(e_txt) == E)
ok.append(bool(re.search(rf"graine de la course v6-2 = {g[1]}\b", t2)) and bool(re.search(rf"graine de la course v5-3 = {g[0]}\b", t2)))
ok.append(re.search(r"<<[A-Z0-9_]*>>", t2) is None)
ok.append("0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952" in t2)
ok.append(bool(re.search(rf"(?m)^ *graine de la course v6-2 = {g[1]}$", t2)))
print("lecture par le lanceur v10 (entropie, deux graines, aucun marqueur, empreinte du lanceur, graine de la précédente ancrée) :", ok)
