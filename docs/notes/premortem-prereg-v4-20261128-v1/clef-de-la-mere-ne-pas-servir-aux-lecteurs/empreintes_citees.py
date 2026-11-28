"""Clef de la mère : empreintes citées par les trois pièces de Gemini — longueur, et présence ailleurs dans le dépôt
(chaînes cherchées par `git grep` dans les fichiers texte suivis ; aucun fichier interdit n'est ouvert par ce programme :
`git grep -I` ignore les binaires, et la recherche ne rend que la chaîne trouvée)."""
import re, subprocess, sys, collections
DEPOT = "/home/user/controle-ia-travail"
D = "brouillons/prereg-v4-c-furtif-g1"
MOTIFS = __file__.replace("empreintes_citees.py", "motifs-empreintes.txt")
PIECES = ["G0-critere-3-additif-c-furtif-v1-brouillon-gemini-1.md", "G1-architecture-h1-h2-v1-brouillon-gemini-1.md",
          "arbitrages-GO-2026-11-28-01-a-03-texte-gemini-v1.md"]
ou = collections.defaultdict(set)
for p in PIECES:
    t = open(f"{DEPOT}/{D}/{p}", encoding="utf-8").read()
    for m in re.finditer(r"(?<![0-9a-f])[0-9a-f]{32,}(?![0-9a-f])", t):
        ou[m.group(0)].add(p.split("-")[0])
anormales = sorted(h for h in ou if len(h) not in (40, 64))
h64 = sorted(h for h in ou if len(h) == 64)
print("chaînes hexadécimales distinctes :", len(ou), "; de 64 signes :", len(h64), "; de 40 :", sum(len(h) == 40 for h in ou))
print("longueur anormale :", [(h[:12] + "…", len(h), sorted(ou[h])) for h in anormales])
open(MOTIFS, "w").write("\n".join(h64) + "\n")
r = subprocess.run(["git", "-C", DEPOT, "grep", "-I", "-o", "-h", "-F", "-f", MOTIFS, "--", ".", f":!{D}"],
                   capture_output=True, text=True)
trouvees = set(r.stdout.split())
absentes = [h for h in h64 if h not in trouvees]
print("de 64 signes, retrouvées ailleurs dans le dépôt :", len(h64) - len(absentes), "; absentes :", len(absentes))
for h in absentes:
    print("  absente :", h, sorted(ou[h]))
