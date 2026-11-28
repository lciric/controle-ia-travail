"""Pour chaque segment absent de mots_exacts_b6_v1 : part des morceaux de 30 caractères retrouvés au brouillon 6,
puis, si la part est ≥ 0,5, les différences mot à mot avec la meilleure fenêtre du brouillon 6."""
import re, sys, difflib, importlib.util
spec = importlib.util.spec_from_file_location("m", sys.argv[2]); m = importlib.util.module_from_spec(spec)
sys.argv = [sys.argv[0], sys.argv[1]]
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
for nom, (f, pl) in m.plages.items():
    L = open(f, encoding="utf-8").read().split("\n")
    for a, b in pl:
        for seg in m.segments("\n".join(L[a-1:b])):
            sn = m.norm(seg)
            if len(sn) < 50 or re.search(m.motif(seg), m.B6n): continue
            sn2 = re.sub(r"<<[A-Z0-9_]+>>", "", sn)
            morceaux = [sn2[i:i+30] for i in range(0, max(1, len(sn2) - 29), 15)]
            part = sum(x in m.B6n for x in morceaux) / len(morceaux)
            print(f"\n## {nom} l.{a}-{b} ({len(sn)} c.) part retrouvée {part:.2f} : {sn[:90]}…")
            if part >= 0.5:
                # meilleure fenêtre : autour du premier morceau retrouvé
                pos = next((m.B6n.find(x) for x in morceaux if x in m.B6n), 0)
                debut = max(0, pos - 200); fen = m.B6n[debut: debut + len(sn2) + 600]
                w1, w2 = sn2.split(" "), fen.split(" ")
                sm = difflib.SequenceMatcher(None, w1, w2, autojunk=False)
                blocs = [bl for bl in sm.get_matching_blocks() if bl.size]
                if not blocs: continue
                j0 = blocs[0].b - blocs[0].a if blocs[0].b >= blocs[0].a else blocs[0].b
                w2 = w2[max(0, blocs[0].b - blocs[0].a): blocs[-1].b + blocs[-1].size + (len(w1) - blocs[-1].a - blocs[-1].size)]
                sm = difflib.SequenceMatcher(None, w1, w2, autojunk=False)
                for op, i1, i2, j1, j2 in sm.get_opcodes():
                    if op != "equal":
                        print(f"   {op}: rapport « {' '.join(w1[i1:i2])[:200]} » / brouillon 6 « {' '.join(w2[j1:j2])[:200]} »")
