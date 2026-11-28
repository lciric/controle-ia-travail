"""Contrôle des sorties d'essai : aucune ne doit contenir un morceau de 12 caractères ou plus d'un texte de formulation,
de témoin, de fente, de consigne, de contenu neutre, de paragraphe de bras ou du gabarit du constat nu (remplis A et B
compris). Les morceaux trouvés sont remplacés par [masqué] ; le nombre de remplacements est imprimé."""
import json, re, sys, glob
cfg = json.load(open(sys.argv[1], encoding="utf-8"))
def rem(s, f): return re.sub(r"\{([A-Z_]+)\}", lambda m: f.get(m.group(1), m.group(0)), s)
def chaines(x):
    if isinstance(x, str): yield x
    elif isinstance(x, list):
        for e in x: yield from chaines(e)
    elif isinstance(x, dict):
        for e in x.values(): yield from chaines(e)
base = list(chaines(cfg["vivier"])) + list(chaines(cfg["temoins_sham"])) + [cfg["constat_nu"]["gabarit"]]
sens = []
for s in base:
    sens += [s, rem(s, cfg["fentes"]["A"]), rem(s, cfg["fentes"]["B"])]
sens += list(chaines(cfg["fentes"])) + list(chaines(cfg["consignes"])) + list(chaines(cfg["contenus_neutres"]))
sens += [cfg["agent_bras"]["plaidoyer"], cfg["agent_bras"]["usurpation"]]
morceaux = {s[i:i+12] for s in sens for i in range(len(s) - 11)}
morceaux = {m for m in morceaux if not re.fullmatch(r"[\s\W\d]*", m)}
for f in sorted(glob.glob("*.txt")):
    t = open(f, encoding="utf-8").read(); n = 0; out = []; i = 0
    while i < len(t):
        if t[i:i+12] in morceaux:
            j = i + 12
            while j < len(t) and t[j-11:j+1] in morceaux: j += 1
            out.append("[masqué]"); n += 1; i = j
        else:
            out.append(t[i]); i += 1
    if n:
        open(f, "w", encoding="utf-8").write("".join(out))
    print(f, ":", n, "passage(s) masqué(s)")
