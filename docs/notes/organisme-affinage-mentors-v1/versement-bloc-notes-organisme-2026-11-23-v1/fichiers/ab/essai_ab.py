import importlib.util, sys, shutil, subprocess, hashlib, json
from pathlib import Path
RACINE = Path("/home/user/wt-organisme"); T = Path(sys.argv[1]); ORCH = Path(sys.argv[2])
s = importlib.util.spec_from_file_location("l", RACINE / "scripts/lancer_course_affinage_mentors_v11d.py")
L = importlib.util.module_from_spec(s); sys.modules["l"] = L; s.loader.exec_module(L)
depot = T / "depot"
for rel, _ in L.PIECES.values():
    (depot / rel).parent.mkdir(parents=True, exist_ok=True)
    src = RACINE / rel
    if src.is_file(): shutil.copyfile(src, depot / rel)
(depot / L.PIECES["garde_google"][0]).write_bytes(subprocess.run(["git", "-C", str(RACINE), "show", "refs/remotes/origin/main:" + L.PIECES["garde_google"][0]], capture_output=True).stdout)
pre = depot / L.PREREG; pre.parent.mkdir(parents=True, exist_ok=True); pre.write_text("# préenregistrement d'essai\n")
Path(str(pre) + ".sha256").write_text(hashlib.sha256(pre.read_bytes()).hexdigest() + "  " + pre.name + "\n")
L.DEPOT = depot
L.ORCHESTRATEURS_CANDIDATS = (ORCH,)
orig = L.extraire_de_main
L.extraire_de_main = lambda d, c, a, dest: orig(RACINE, c, a, dest)
print("code", L.principal(["--a-blanc", str(T / "a-blanc")]))
