import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
WT = SCRATCH / "wt-main-push"

env = os.environ.copy()
env["GIT_TERMINAL_PROMPT"] = "0"

def git_run(cwd, *args, check=True, timeout=120):
    r = subprocess.run(
        ["git", "-C", str(cwd), "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential",
         "-c", "core.longpaths=true", "-c", "core.protectNTFS=false", *args],
        env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout
    )
    if check and r.returncode != 0:
        print(f"CMD FAILED: git {args}\nSTDOUT:\n{r.stdout}\nSTDERR:\n{r.stderr}", file=sys.stderr)
        sys.exit(r.returncode)
    return r

git_run(REPO, "fetch", "origin", "main")
if WT.exists():
    git_run(REPO, "worktree", "remove", "--force", str(WT), check=False)
    if WT.exists():
        shutil.rmtree(WT, ignore_errors=True)
git_run(REPO, "worktree", "add", "--no-checkout", "--detach", str(WT), "origin/main")
git_run(WT, "sparse-checkout", "init", "--no-cone")
git_run(WT, "sparse-checkout", "set", "/registres/")
git_run(WT, "checkout")

go_path = WT / "registres" / "go.md"
dec_path = WT / "registres" / "decisions.md"

go_txt = go_path.read_text(encoding="utf-8")
dec_txt = dec_path.read_text(encoding="utf-8")

go_nums = [int(m.group(1)) for m in re.finditer(r"GO-2026-11-25-(\d+)", go_txt)]
next_go_num = (max(go_nums) + 1) if go_nums else 1
go_id = f"GO-2026-11-25-{next_go_num:02d}"

r_nums = [int(m.group(1)) for m in re.finditer(r"^- R-(\d+) ", dec_txt, re.M) if int(m.group(1)) < 9000]
next_r_num = max(r_nums) + 1
r_id = f"R-{next_r_num}"

now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")

go_line = (
    f"| {go_id} | 2026-11-25 | décision | Mot de Lazar tapé le 2026-11-25T16:12:48Z dans la session mère Antigravity "
    f"(Gemini 4 Carbon High, conversation cd7c89b9) : « B go ». Option B retenue pour les diagnostics préalables des sondes "
    f"boîte blanche version 2 (`prereg/diagnostics-prealables-sondes-v1.md` `e8dca00b…` et additif `40a9e45c…`) : "
    f"(1) corriger le défaut `nproc` dans une amorce version 3 contre-lue en classe B (`N_WORKERS=$(nproc --all)` avant `OMP_NUM_THREADS=1`, "
    f"garde multicœur, branche dédiée `calcul/sondes-v2-epreuve-plantee-v4-suite` sans écraser les 13 tranches scellées `[0, 130)`), "
    f"achever `[130, 500)` du mode `etalon` sur les 52 cases + sceller la synthèse fusionnée `[0, 500)` + chronométrer 1 réplique isolée "
    f"du mode `complet`, sous le reliquat de `GO-2026-11-24-02` (attendu ≈ 2 à 3,5 USD sur ≈ 58,96 USD restants) ; "
    f"(2) nœud explicite du directeur (`prereg/diagnostics-prealables-sondes-v1.md` lignes 92 et 108) : dissocier l'ouverture des deux "
    f"questions gouvernées par le mode `etalon` (Q1 identité des poids et Q2 étalon de transport avec contrôle d'intensité) du mode `complet` "
    f"et de la question Q3 (rejeu croisé, dont le contrôle du chemin est prouvé absent par la note des effectifs `7338a3dc…`, ajournée après "
    f"le 1er décembre) ; préparer et contre-lire en parallèle en classe B le court programme aveugle d'étape 4 pour ouvrir Q1 et Q2 dès le "
    f"scellement de la synthèse fusionnée `[0, 500)` du mode `etalon`, puis verdict d'étape 5 par juge neuf (R13). "
    f"| sous GO-2026-11-24-02 (reste ≈ 58,96 USD sur 68 USD) | 2026-12-01 | Lazar | GO-2026-11-24-02 ; GO-2026-11-24-15 ; GO-2026-11-24-49 ; {r_id} |"
)

r_line = (
    f"- {r_id} ({now_iso}) — {go_id} inscrit (« B go », mot de Lazar à 2026-11-25T16:12:48Z après l'audit en 4 points `0a369222` ayant identifié "
    f"le défaut `OMP_NUM_THREADS=1` -> `nproc=1` de l'amorce v2) : (1) reprise multicœur de `[130, 500)` du mode `etalon` + sonde chronométrée "
    f"d'une réplique du mode `complet` sous le reliquat de `GO-2026-11-24-02`, par amorce v3 contre-lue en classe B sans recalcul ni écrasement "
    f"des 13 tranches `[0, 130)` ; (2) nœud de découplage autorisant l'ouverture immédiate de Q1 (identité des poids) et Q2 (étalon de transport) "
    f"dès la synthèse fusionnée `[0, 500)` de `etalon` scellée, par programme aveugle d'étape 4 contre-lu en classe B puis juge neuf R13, "
    f"Q3 (rejeu croisé, contrôle du chemin absent) restant non ouverte et ajournée après le 1er décembre."
)

go_path.write_bytes((go_txt.rstrip("\r\n") + "\n" + go_line + "\n").replace("\r\n", "\n").encode("utf-8"))
dec_path.write_bytes((dec_txt.rstrip("\r\n") + "\n" + r_line + "\n").replace("\r\n", "\n").encode("utf-8"))

git_run(WT, "add", "registres/go.md", "registres/decisions.md")
git_run(WT, "commit", "-m", f"{r_id} : inscrire {go_id} Option B sondes v2 (reprise etalon 130-500 et decouplage Q1-Q2)")
head = git_run(WT, "rev-parse", "HEAD").stdout.strip()
git_run(WT, "push", "origin", "HEAD:refs/heads/main")

print(f"INSCRIBED_OK GO_ID={go_id} R_ID={r_id} HEAD={head}")
