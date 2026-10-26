"""Contre-lecture 6 du texte pilote4-gemini-organisme-v4.md : contrôles en lecture seule — v1.

Usage : /opt/venv-essaim-sim-v1/bin/python -I controle_scellement_cl6_v1.py TEXTE LISTE_V6 LISTE_V7 DOSSIER_SIMULATION
1. gardes du script de scellement v4 (l. 35-58), transcrites, sur le texte tel quel ;
2. remplissage en mémoire avec des valeurs d'essai (jamais celles du pilote), gardes après remplissage (l. 89-96) et
   lecture du lanceur v10, étape 2 (l. 501-511), transcrites ;
3. comparaison des listes d'empreintes v6 et v7 par chemin ;
4. nombre d'appels par unité dans les journaux de simulation versés (champs statut et rôle seulement ; aucun score).
N'écrit rien.
"""
import collections, hashlib, json, re, sys
import numpy

texte_p, l6_p, l7_p, sim = sys.argv[1:5]
b = open(texte_p, "rb").read()
print("texte", hashlib.sha256(b).hexdigest())
t = b.decode("utf-8"); cle = "v6-2"; L = t.splitlines()
print("1. [[…]] :", re.findall(r"\[\[[A-Z0-9_]+\]\]", t), "; '[[' :", t.count("[["))
att = {"<<ENTROPIE>>", "<<GRAINE_V53>>", "<<GRAINE_V6X>>", "<<EMPREINTE_PIECES>>"}
print("   marqueurs = attendus :", set(re.findall(r"<<[A-Z0-9_]+>>", t)) == att, {m: t.count(m) for m in sorted(att)},
      "; '<<' :", t.count("<<"), "; '>>' :", t.count(">>"))
for l in ("graine de la course v5-3 = <<GRAINE_V53>>", f"graine de la course {cle} = <<GRAINE_V6X>>", "entropie E = <<ENTROPIE>>"):
    print("   ligne présente :", l in t, "|", l)
print("   lignes « entropie E = » :", [i + 1 for i, l in enumerate(L) if "entropie E =" in l],
      "; nombre déjà écrit :", bool(re.search(r"entropie E = [0-9]", t)))
lg = [(i + 1, l.strip()) for i, l in enumerate(L) if re.search(r"graine de la course \S+ =", l)]
print("   lignes de graine :", lg)
print("   = attendues :", sorted(x for _, x in lg) == sorted(["graine de la course v5-3 = <<GRAINE_V53>>", f"graine de la course {cle} = <<GRAINE_V6X>>"]))
e = 123456789012345678901234567890
g = [int(c.generate_state(1, dtype=numpy.uint64)[0]) for c in numpy.random.SeedSequence(e).spawn(2)]
u = (t.replace("<<ENTROPIE>>", str(e)).replace("<<GRAINE_V53>>", str(g[0])).replace("<<GRAINE_V6X>>", str(g[1]))
      .replace("<<EMPREINTE_PIECES>>", "`" + "ab" * 32 + "`"))
print("2. après remplissage (valeurs d'essai) : marqueur restant", bool(re.search(r"<<[A-Z0-9_]+>>", u)),
      "; entropie unique et juste", re.findall(r"entropie E = ([0-9]+)", u) == [str(e)])
for c, v in (("v5-3", g[0]), (cle, g[1])):
    print("   graine", c, "unique et juste :", re.findall(r"graine de la course " + re.escape(c) + r" = ([0-9]+)", u) == [str(v)])
print("   lanceur l. 502 (marqueurs) :", bool(re.search(r"<<[A-Z0-9_]*>>", u)),
      "; l. 503 (empreinte du lanceur) :", "0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952" in u)
E = re.findall(r"entropie E = [0-9]+", u)[0].split()[-1]
print("   l. 504 (première entropie = tirée) :", E == str(e))
for c, i in (("v5-3", 0), ("v6-2", 1)):
    gc = int(numpy.random.SeedSequence(int(E)).spawn(2)[i].generate_state(1, dtype=numpy.uint64)[0])
    print("   l. 501", c, ":", bool(re.search(r"graine de la course " + c + " = " + str(gc) + r"\b", u)),
          "; l. 509 (ancrée) :", bool(re.search(r"(?m)^ *graine de la course " + c + " = " + str(gc) + "$", u)))

def lire(p):
    d = {}
    for l in open(p, encoding="utf-8"):
        h, n = l.rstrip("\n").split("  ", 1); assert n not in d; d[n] = h
    return d
v6, v7 = lire(l6_p), lire(l7_p)
print("3. v6", len(v6), "; v7", len(v7), "; absentes de v7 :", [p for p in v6 if p not in v7],
      "; empreinte changée :", [p for p in v6 if p in v7 and v6[p] != v7[p]])
nouv = sorted(p for p in v7 if p not in v6)
print("   nouvelles :", len(nouv), dict(collections.Counter((p.split("/")[0] + "/") if "/" in p else "(premier niveau)" for p in nouv)))
print("   interdites (-cle.json, -secret.json, donnees/, runs/, diag/) :",
      [p for p in v7 if re.search(r"-cle\.json|-secret\.json|(^|/)(donnees|runs|diag)/", p)])
for cas in ("v6-2", "v5-3", "v6-2-segments", "v6-2-trois-segments"):
    out = []
    for un in ("c001", "g000", "g001", "g002", "g003"):
        J = [json.loads(x) for x in open(f"{sim}/journal-appels-{un}-simulation-{cas}.jsonl", encoding="utf-8") if x.strip()]
        st = collections.Counter(x.get("statut") for x in J); mu = sum(1 for x in J if x.get("role") == "architecte_mutation_endogene")
        out.append(f"{un} {len(J)}" + (f" (mutation {mu})" if mu else "") + ("" if set(st) == {"OK"} else f" {dict(st)}"))
    print("4.", cas, ":", " ; ".join(out))
