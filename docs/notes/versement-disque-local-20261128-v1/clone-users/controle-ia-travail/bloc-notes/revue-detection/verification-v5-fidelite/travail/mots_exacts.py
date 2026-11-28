"""Vérificateur v5 fidélité : chaque passage entre guillemets des corrections des deux rapports est-il dans la v5 ?
Extrait les segments «…» de premier niveau (guillemets imbriqués gérés) des blocs « Correction » de chaque constat,
puis cherche chaque segment, espaces normalisés, dans la v5. Usage : python3 -I -B mots_exacts.py RAPPORT_FIDELITE RAPPORT_SENS V5"""
import re, sys

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

def segments(txt):
    out, depth, start = [], 0, None
    for i, c in enumerate(txt):
        if c == "«":
            if depth == 0:
                start = i + 1
            depth += 1
        elif c == "»" and depth > 0:
            depth -= 1
            if depth == 0:
                out.append(txt[start:i])
    return out

def blocs(rapport, prefixe):
    t = open(rapport, encoding="utf-8").read()
    # découpe par constat
    parts = re.split(r"(?m)^(?:\*\*|### )(" + prefixe + r"-\d\d)", t)
    res = {}
    for k in range(1, len(parts), 2):
        cid, corps = parts[k], parts[k + 1]
        m = re.search(r"(?s)(\*\*Correction\.\*\*|- \*\*Correction\.\*\*|Correction :|^- \(a\))(.*?)(?=\n- \*\*Reproduire|\n\*\*VV|\n### |\Z)", corps)
        res[cid] = corps if m is None else m.group(2)
        if cid.endswith("-12") and prefixe.endswith("fidelite"):
            res[cid] = corps  # VV4-fidelite-12 : corrections dans le corps (a)-(c)
        if cid.endswith("-16") and prefixe.endswith("sens"):
            res[cid] = corps
    return res

v5 = norm(open(sys.argv[3], encoding="utf-8").read())
for rap, pre in ((sys.argv[1], "VV4-fidelite"), (sys.argv[2], "VV4-sens")):
    for cid, corps in blocs(rap, pre).items():
        for s in segments(corps):
            s2 = norm(s)
            if len(s2) < 20:
                continue
            ok = s2 in v5
            print(f"{cid} | {'PRÉSENT' if ok else 'ABSENT '} | {s2[:150]}")
