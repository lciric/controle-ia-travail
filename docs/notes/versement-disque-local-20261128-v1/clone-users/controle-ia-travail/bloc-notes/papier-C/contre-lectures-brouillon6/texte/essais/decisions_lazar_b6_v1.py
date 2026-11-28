"""Textes de la section 2 du projet de traitement (R-307 ajouts 2 et 3, R-309) : présents mot pour mot au brouillon 6 ?"""
import re, sys, importlib.util
P = sys.argv[1]
spec = importlib.util.spec_from_file_location("m", sys.argv[2]); m = importlib.util.module_from_spec(spec)
import io, contextlib
argv = sys.argv; sys.argv = [argv[0], P]
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
projet = open(f"{P}/traitement-brouillon5/traitement-contre-lectures-brouillon5-papier-C-projet-v1.md", encoding="utf-8").read()
a = projet.index("## 2. Décisions de Lazar déjà prises"); b = projet.index("## 3. P-019 corrigée")
sec = projet[a:b]
# blocs cités en « > » et segments « … » de 2.3
blocs = re.findall(r"((?:^> .*\n?)+)", sec, flags=re.M)
for bl in blocs:
    t = m.norm(re.sub(r"^> ?", "", bl, flags=re.M))
    print("bloc >", len(t), "car. :", "PRÉSENT" if t in m.B6n else "ABSENT", "|", t[:80])
for seg in m.segments(sec[sec.index("### 2.3"):]):
    s = m.norm(seg)
    if len(s) >= 40: print("seg 2.3", len(s), "car. :", "PRÉSENT" if s in m.B6n else "ABSENT", "|", s[:90])
