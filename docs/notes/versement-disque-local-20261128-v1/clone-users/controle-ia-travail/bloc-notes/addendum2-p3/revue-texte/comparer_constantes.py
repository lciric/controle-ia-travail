"""Compare les constantes et phrases du module (copie) au brouillon 2, sans lire aucune donnée."""
import re, sys, importlib.util
from pathlib import Path

TEXTE = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum2-p3/P3-addendum2-audit-verdict-v1-brouillon2.md").read_text(encoding="utf-8")
spec = importlib.util.spec_from_file_location("avc", sys.argv[1])
av = importlib.util.module_from_spec(spec); spec.loader.exec_module(av)

# 1. table « Entrées »
lignes = re.findall(r"^\| \[(\w+)\] \| `([^`]+)`.*?\| `([0-9a-f]{64})` \|$", TEXTE, re.M)
texte_entrees = {e: (c, h) for e, c, h in lignes}
print("entrées du texte :", sorted(texte_entrees))
for k, (c, h) in av.ENTREES.items():
    tc, th = texte_entrees[k]
    print(f"  [{k}] chemin {'=' if c == tc else '≠'} ; empreinte {'=' if h == th else '≠'}")
print("  entrées citées non lues par le module :", sorted(set(texte_entrees) - set(av.ENTREES)))

# 2. clés de graines : liste du texte reconstruite depuis le texte seul
objets = re.search(r"`<objet>` parmi (.*?) \(27 clés\)", TEXTE, re.S).group(1)
objets = re.findall(r"`([a-z_\-]+)`", objets)
formes = re.findall(r"`(cout_[a-z_]+)`", re.search(r"les cinq formes (.*?) ;", TEXTE, re.S).group(1))
cles = [f"addendum2/{x}/{o}" for x in ("B1/saboteur-honnete", "B2/temoin-honnete", "B2/mention-honnete") for o in objets]
cles += [f"addendum2/ecart/{c}/{f}" for c in ("honnete", "saboteur", "temoin", "mention") for f in formes]
print("objets du texte :", objets)
print("formes du texte (ordre de « Entrées ») :", formes, "| FORMES du module égales :", tuple(formes) == av.FORMES)
print("47 clés du texte = clés du module (même ordre) :", cles == av.cles_addendum2(), len(cles))

# 3. chaînes et nombres
print("COMMANDE dans la garde 5 :", av.COMMANDE in TEXTE, "| commande du plan, point 2 :", ("python " + av.CHEMIN_MODULE) in TEXTE)
print("ENTROPIE :", str(av.ENTROPIE_P3) in TEXTE, "| COMMIT_N025 :", av.COMMIT_N025 in TEXTE)
print("LOG10_3 du texte :", "0,47712125471966244" in TEXTE, repr(av.LOG10_3))
print("CHAINES_MANIFESTE dans la garde 5 :", [s in TEXTE for s in av.CHAINES_MANIFESTE])
print("CLES_INTERDITES :", all(f"`{k}`" in TEXTE for k in av.CLES_INTERDITES), len(av.CLES_INTERDITES))

# 4. phrases des critères : chaque phrase du module figure-t-elle telle quelle dans le texte ?
def present(s):
    # les gabarits {…} du module correspondent à des grandeurs écrites en `…` dans le texte
    morceaux = [m for m in re.split(r"\{[a-z0-9_]+\}", s) if m]
    return all(m in TEXTE for m in morceaux), [m for m in morceaux if m not in TEXTE]
for k, v in list(av.LECTURES.items()) + [("NON_LUE", av.LECTURE_NON_LUE), ("AUCUNE", av.LECTURE_AUCUNE),
                                        ("AUDIT", av.LECTURE_AUDIT), ("ARRET", av.LECTURE_ARRET)]:
    ok, manque = present(v)
    print(f"  phrase {k}: {'présente' if ok else 'ÉCART'} {manque if manque else ''}")
