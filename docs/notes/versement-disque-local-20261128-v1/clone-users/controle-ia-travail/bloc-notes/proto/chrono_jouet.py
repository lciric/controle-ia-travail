import sys, time, tempfile
sys.dont_write_bytecode = True
from pathlib import Path
M = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/module")
sys.path.insert(0, str(M))
import test_instrument_p4_v1 as ti
import lecture_p4_v1 as lp
base = Path(tempfile.mkdtemp(dir="/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/proto/chrono"))
t0 = time.perf_counter(); d = ti.construire_p3_jouet(base / "depot"); t1 = time.perf_counter()
r = ti.run_p4_jouet(d, "20261020-190000-p4-jouet"); t2 = time.perf_counter()
ti.committer(d, "run p4")
s = lp.analyser(d, "20261020-190000-p4-jouet", "20261020-190100-lecture-p4", None, entropie=4242); t3 = time.perf_counter()
print(f"p3 jouet {t1-t0:.1f} s ; p4 jouet {t2-t1:.1f} s ; lecture {t3-t2:.1f} s ; ligne {s['issue']['ligne']} ; épreuve {r and 'ok'}")
