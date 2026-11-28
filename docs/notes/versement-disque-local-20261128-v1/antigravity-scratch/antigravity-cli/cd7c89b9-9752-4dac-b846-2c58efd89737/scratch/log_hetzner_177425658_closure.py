import os
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
WT = SCRATCH / "wt-main-push"
env = os.environ.copy()
env["GIT_TERMINAL_PROMPT"] = "0"

def git_run(cwd, *args, check=True, timeout=120):
    p = subprocess.run(
        ["git", "-C", str(cwd), "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential",
         "-c", "core.longpaths=true", "-c", "core.protectNTFS=false", *args],
        env=env, capture_output=True, text=True, timeout=timeout,
    )
    if check and p.returncode != 0:
        raise RuntimeError(f"git {args} failed rc={p.returncode}: {p.stdout} {p.stderr}")
    return p

# 1. List the 27 filenames & sizes (ONLY names/sizes, never content!)
ls_out = git_run(REPO, "ls-tree", "-r", "-l", "origin/calcul/sondes-v2-epreuve-plantee-v4").stdout.splitlines()
print(f"FILES_27 ({len(ls_out)}):")
for ln in ls_out:
    print(" ", ln)

# 2. Refresh fast sparse worktree from origin/main
git_run(REPO, "fetch", "origin", "main")
print("NEW_COMMITS_ON_MAIN:")
print(git_run(REPO, "log", "--oneline", "9c9ab7f5b..origin/main").stdout.strip())
if WT.exists():
    git_run(REPO, "worktree", "remove", "--force", str(WT), check=False)
    if WT.exists():
        shutil.rmtree(WT, ignore_errors=True)
git_run(REPO, "worktree", "add", "--no-checkout", "--detach", str(WT), "origin/main")
git_run(WT, "sparse-checkout", "init", "--cone")
git_run(WT, "sparse-checkout", "set", "registres")
git_run(WT, "checkout")

# 3. Check if 177425658 closure already logged by another session
arr_p = WT / "registres/arrets.md"
arr_txt = arr_p.read_text(encoding="utf-8").rstrip("\n")
if "177425658" in arr_txt:
    print("ALREADY_LOGGED_177425658_IN_ARRETS")
    raise SystemExit(0)

dec_p = WT / "registres/decisions.md"
dec_txt = dec_p.read_text(encoding="utf-8")
nums = [int(m.group(1)) for m in re.finditer(r"^- R-(\d+) ", dec_txt, re.M)]
next_r = max(nums) + 1
now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
arr_line = (
    f"| 2026-11-25T13:16Z | serveur Hetzner 177425658 (`sondes-v2-etalon-v4-20261124-0537`, ccx33 hel1, créé `2026-11-24T05:37:03Z`, GO-2026-11-24-02) "
    f"| AUTODÉTRUIT par sa minuterie interne R10 (`31h30`, `partiel-plafond-r10`) après poussée prouvée à `13:15:30Z` sur la branche orpheline `calcul/sondes-v2-epreuve-plantee-v4` (`38c6f4a7054b14b56be7b357c08db8bf11931ca2`, `27` fichiers versés, non ouverts par la mère) "
    f"| absence prouvée à deux contrôles API Hetzner (`HTTP 404` à `13:18:06Z`, liste `GET /v1/servers` vide `0` serveur à `13:20:23Z`) ; ≈ `31,65 h` (`32 h` entamées à `0,22596 EUR/h` = `7,23 EUR` ≈ `9,04 USD` au taux `1,25`, sous la coupure `15 USD` et le plafond `68 USD`) ; mère Antigravity `cd7c89b9`, R-{next_r} |"
)
arr_p.write_bytes((arr_txt + "\n" + arr_line + "\n").replace("\r\n", "\n").encode("utf-8"))

dep_p = WT / "registres/depenses.md"
dep_txt = dep_p.read_text(encoding="utf-8").rstrip("\n")
dep_line = (
    f"| 2026-11-25T13:16Z | GO-2026-11-24-02 | clôture serveur Hetzner `177425658` (`sondes-v2-etalon-v4-20261124-0537`, ccx33 hel1, `2026-11-24T05:37:03Z` → autodestruction `13:15:30Z`–`13:18:06Z` sur minuterie interne R10 `partiel-plafond-r10`, branche `calcul/sondes-v2-epreuve-plantee-v4` `38c6f4a7`, `27` fichiers versés, absence prouvée `0` serveur) "
    f"| ≈ `9,04 USD` (`7,23 EUR` = `32 h` entamées × `0,22596 EUR/h`, taux `1,25` ; facture Hetzner faisant foi ; sous coupure `15 USD` et plafond `68 USD`) | R-{next_r} |"
)
dep_p.write_bytes((dep_txt + "\n" + dep_line + "\n").replace("\r\n", "\n").encode("utf-8"))

r_line = (
    f"- R-{next_r} ({now_utc}) — Épreuve à vérité plantée des sondes boîte blanche version 2 (`GO-2026-11-24-02`, serveur Hetzner `177425658`, `ccx33` créé `2026-11-24T05:37:03Z`) : "
    f"arrêt propre sur minuterie interne R10 (`partiel-plafond-r10`), versement prouvé à `2026-11-25T13:15:30Z` sur `origin/calcul/sondes-v2-epreuve-plantee-v4` "
    f"(`38c6f4a7054b14b56be7b357c08db8bf11931ca2`, `27` fichiers, aucun score ouvert par la mère) puis autodestruction vérifiée à deux contrôles API Hetzner "
    f"(`HTTP 404` à `13:18:06Z` et `0` serveur actif à `13:20:23Z`). Dépense estimée ≈ `9,04 USD` (`7,23 EUR`, sous la coupure `15 USD` et le plafond `68 USD`), consignée dans `registres/arrets.md` et `registres/depenses.md`. "
    f"En parallèle, contrôle Vast.ai `62498862` (dose-réponse consigne cachée) : `346 / 1 920` épisodes (`bloc 12/64, lot 2/4`, branche `calcul/dose-reponse-v1` `e70a2c7b`), fonctionnement nominal."
)
dec_p.write_bytes((dec_txt.rstrip("\n") + "\n" + r_line + "\n").replace("\r\n", "\n").encode("utf-8"))

git_run(WT, "add", "registres/arrets.md", "registres/depenses.md", "registres/decisions.md")
git_run(WT, "commit", "-m", f"R-{next_r} : cloture verifiee Hetzner 177425658 (partiel-plafond-r10, 38c6f4a7, 0 serveur)")
git_run(WT, "push", "origin", "HEAD:refs/heads/main")
print(f"LOGGED_AND_PUSHED_OK: R-{next_r} head={git_run(WT, 'rev-parse', 'HEAD').stdout.strip()}")
