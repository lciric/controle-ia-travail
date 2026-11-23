import subprocess, tempfile, os
from pathlib import Path
from controle_ia.t08 import entrees_v1 as en
R="20261115-120000-t06-7b"
env={**os.environ,"GIT_AUTHOR_NAME":"t","GIT_AUTHOR_EMAIL":"t@t","GIT_COMMITTER_NAME":"t","GIT_COMMITTER_EMAIL":"t@t"}
def g(d,*a): subprocess.run(["git","-C",str(d),*a],check=True,capture_output=True,env=env)
d=Path(tempfile.mkdtemp()); g(d,"init","-q")
(d/"a").mkdir(); (d/"a"/"b").write_text("x")
p=d/"diag"/R/"d\nx"; p.mkdir(parents=True); (p/"resume.json").write_text("x")
g(d,"add","-A"); g(d,"commit","-q","-m","a")
import shutil; shutil.rmtree(d/"diag")
try: print(en.exiger_instance_sans_interdits(d,R))
except Exception as e: print("arret",str(e)[:90])
