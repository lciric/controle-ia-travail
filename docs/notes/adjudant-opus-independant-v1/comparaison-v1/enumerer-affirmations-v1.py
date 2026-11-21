"""Enumère, dans l'ordre du texte, les affirmations vérifiables d'une réponse.
Unité : une citation de publication avec page, un renvoi de calcul, ou un renvoi
à une décision ou à une note du programme. Sortie : rang, ligne, type, extrait."""
import re, sys
chemin, style = sys.argv[1], sys.argv[2]
lignes = open(chemin, encoding="utf-8").read().splitlines()
motifs = []
if style == "A":
    motifs = [
        ("publication", re.compile(r"\((?:[^()]|\([^()]*\))*?p\. ?\d[^()]*\)")),
        ("calcul", re.compile(r"\[calcul, [A-E](?:, [A-E])*\]")),
    ]
else:
    motifs = [
        ("publication", re.compile(r"\[(?:[^\[\]]*?)p\. ?\d[^\[\]]*\]|\((?:tableau \d, )?p\. ?\d[^()]*\)")),
        ("calcul", re.compile(r"\[calcul[^\]]*\]")),
    ]
programme = re.compile(r"\((?:[^()]*?)(N-0\d\d)(?:[^()]*)\)|note de dissonance, § ?\d|programme, section \d|\(section \d\)|note des expérimentateurs[^.;]*§ ?\d|note de dérive de régime")
rang = 0
for i, l in enumerate(lignes, 1):
    trouves = []
    for typ, m in motifs:
        for x in m.finditer(l):
            if typ == "publication" and style == "B" and x.group(0).startswith("["):
                # une citation par source dans le crochet
                morceaux = [p.strip() for p in x.group(0).strip("[]").split(";") if re.search(r"p\. ?\d", p)]
                for p in morceaux:
                    trouves.append((x.start(), typ, p))
            else:
                trouves.append((x.start(), typ, x.group(0)))
    for x in programme.finditer(l):
        trouves.append((x.start(), "programme", x.group(0)))
    for pos, typ, txt in sorted(trouves):
        rang += 1
        print(f"{rang}\tl.{i}\t{typ}\t{txt[:110]}")
