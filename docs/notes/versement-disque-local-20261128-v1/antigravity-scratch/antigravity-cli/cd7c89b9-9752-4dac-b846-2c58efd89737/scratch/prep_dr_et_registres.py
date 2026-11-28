import hashlib
import json
import os
import re
import stat
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(
    r"C:\Users\lciri\.gemini\antigravity-cli\brain"
    r"\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch"
)
VAST_EXE = SCRATCH / "venv-py314" / "Scripts" / "vastai.exe"
WT_MAIN = SCRATCH / "wt-main-push"
WT_DR_LECT = SCRATCH / "lecture-dr"

gh_tok = subprocess.check_output(["gh", "auth", "token"], text=True, timeout=20).strip()
vk = Path.home() / ".config" / "vastai" / "vast_api_key"
vast_key = os.environ.get("VAST_API_KEY", "").strip() or vk.read_text("utf-8").strip()

def mask(s: str) -> str:
    for sec in (gh_tok, vast_key):
        if sec and len(sec) >= 8:
            s = s.replace(sec, "***")
    return re.sub(r"(gh[opsu]_|github_pat_|hf_)[A-Za-z0-9_]{8,}", r"\1***", s)

# 1. Journal en direct de 62647167 (devrait avoir fini le clonage et lancé les 63+1 travailleurs)
print("=== 1. JOURNAL EN DIRECT DE 62647167 ===")
try:
    env_v = {**os.environ, "VAST_API_KEY": vast_key, "PYTHONUTF8": "1"}
    logs = subprocess.check_output(
        [str(VAST_EXE), "logs", "62647167"],
        env=env_v, text=True, timeout=30, stderr=subprocess.STDOUT,
    )
    print(mask("\n".join(logs.splitlines()[-30:])))
except Exception as e:
    print("LOGS_INFO:", mask(repr(e)))

# 2. Inscription par différentiel git dans wt-main-push (lignes <= 600 signes)
print("\n=== 2. MISE À JOUR DES REGISTRES SUR MAIN ===")
askpass = SCRATCH / "_askpass_gh_tmp.cmd"
askpass.write_text("@echo off\necho %GH_TOK_MEM%\n", encoding="utf-8")
env_git = {
    **os.environ,
    "GIT_ASKPASS": str(askpass),
    "GIT_TERMINAL_PROMPT": "0",
    "GH_TOK_MEM": gh_tok,
    "PYTHONUTF8": "1",
}
try:
    subprocess.run(["git", "-C", str(WT_MAIN), "fetch", "origin", "main"], env=env_git, check=True)
    subprocess.run(["git", "-C", str(WT_MAIN), "checkout", "-B", "main", "origin/main"], env=env_git, check=True)
    subprocess.run(["git", "-C", str(WT_MAIN), "sparse-checkout", "add", "registres"], env=env_git, check=False)

    dec_p = WT_MAIN / "registres" / "decisions.md"
    arr_p = WT_MAIN / "registres" / "arrets.md"
    dec_txt = dec_p.read_text("utf-8")
    arr_txt = arr_p.read_text("utf-8")

    meta_64 = json.loads((SCRATCH / "sondes-v2-64c-launch.json").read_text("utf-8"))
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    r_nums = [int(m.group(1)) for m in re.finditer(r"^- R-(\d+) ", dec_txt, re.M) if int(m.group(1)) < 9000]
    next_r = max(r_nums) + 1
    modif = False

    if "62647167" not in dec_txt:
        r1 = f"R-{next_r}"
        next_r += 1
        l1 = (
            f"- {r1} ({meta_64['created_utc']}) — Épreuve synthétique à vérité plantée des sondes de la boîte blanche version 2 "
            f"(GO-2026-11-25-07, reliquat GO-2026-11-24-02) : amorce version 7 (`{meta_64['amorce_sha256'][:12]}…`) contre-lue en classe B "
            f"(`bdaeb71f…`, essais conformes) versée sur main (`cfa696277b39`) ; instance Vast.ai `62647167` lancée "
            f"(offre `{meta_64['offre_id']}`, 72 cœurs, 63 Go mémoire vive, 0,2139 USD/h stockage compris, minuterie 20 700 s) "
            f"pour calculer `[130, 500)` du mode étalon et chronométrer 1 réplique du mode complet vers `calcul/sondes-v2-epreuve-plantee-v4-suite`."
        )
        assert len(l1) <= 600, len(l1)
        dec_txt = dec_txt.rstrip("\n") + "\n" + l1 + "\n"
        modif = True

    if "a3e16ec24" not in dec_txt:
        r2 = f"R-{next_r}"
        next_r += 1
        l2 = (
            f"- {r2} ({now_utc}) — Course de dose-réponse de l'organisme à consigne cachée (GO-2026-11-24-25, GO-2026-11-25-01, GO-2026-11-25-02) : "
            f"64 blocs sur 64 (1 920 épisodes) scellés et versés avec preuve sur `origin/calcul/dose-reponse-v1` "
            f"(tête `a3e16ec24`, résultats `e375d9461`, traces `71db3302a`, aucun coût ni score ouvert) ; "
            f"autodestruction de l'instance Vast.ai `62498862` vérifiée (absente de l'inventaire, quatre témoins intouchables présents). "
            f"Révocation du jeton GitHub coordonnée dès la clôture de l'instance `62647167` (option a de Lazar)."
        )
        assert len(l2) <= 600, len(l2)
        dec_txt = dec_txt.rstrip("\n") + "\n" + l2 + "\n"
        modif = True

    if "62498862" not in arr_txt:
        la = (
            f"| {now_utc} | instance Vast 62498862 (`dose-reponse-v1`, A100 SXM4 80 Go, GO-2026-11-24-25 / GO-2026-11-25-01) | "
            f"AUTODÉTRUITE par son amorce v4 (R10) après fin normale (`64/64` blocs) et versement prouvé sur `origin/calcul/dose-reponse-v1` (`e375d9461`, `71db3302a`, `a3e16ec24`) | "
            f"absence vérifiée sur l'API Vast.ai (témoins `58936096`, `58936099`, `58936100`, `60988826` intacts) ; ≈ 20,8 h à 1,1933 USD/h + 1,04 USD forfait ≈ 25,9 USD sur 90 USD |\n"
        )
        arr_txt = arr_txt.rstrip("\n") + "\n" + la
        modif = True

    if modif:
        dec_p.write_bytes(dec_txt.encode("utf-8"))
        arr_p.write_bytes(arr_txt.encode("utf-8"))
        subprocess.run(["git", "-C", str(WT_MAIN), "add", "registres/decisions.md", "registres/arrets.md"], env=env_git, check=True)
        subprocess.run([
            "git", "-C", str(WT_MAIN), "-c", "commit.gpgsign=false", "commit",
            "-m", "R-5414 et R-5415 : instance Vast 62647167 (sondes v2 72c) lancee et cloture Vast 62498862 (dose-reponse 64/64)",
        ], env=env_git, check=True)
        subprocess.run(["git", "-C", str(WT_MAIN), "push", "https://x-access-token@github.com/lciric/controle-ia-travail.git", "HEAD:refs/heads/main"], env=env_git, check=True)
        print("PUSH_MAIN_OK:", subprocess.check_output(["git", "-C", str(WT_MAIN), "rev-parse", "--short", "HEAD"], text=True).strip())
    else:
        print("REGISTRES_DEJA_INSCRITS")

    # 3. Préparer l'arbre détaché lecture-dr sur origin/calcul/dose-reponse-v1 et contrôler tous les sceaux
    print("\n=== 3. PRÉPARATION DE lecture-dr ET CONTRÔLE DES SCEAUX ===")
    subprocess.run(["git", "-C", str(REPO), "fetch", "https://x-access-token@github.com/lciric/controle-ia-travail.git", "calcul/dose-reponse-v1:refs/remotes/origin/calcul/dose-reponse-v1"], env=env_git, check=True)
    if not WT_DR_LECT.exists():
        subprocess.run([
            "git", "-C", str(REPO), "-c", "core.autocrlf=false",
            "worktree", "add", "--detach", str(WT_DR_LECT), "origin/calcul/dose-reponse-v1",
        ], env=env_git, check=True)

    subprocess.run([
        "git", "-C", str(WT_DR_LECT), "sparse-checkout", "add",
        "src", "scripts", "tests", "prereg", "brouillons", "registres", ".claude",
        "donnees/20261125-093202-dose-reponse",
        "donnees/20261124-144844-banque-dose-reponse-extraction-v2",
        "donnees/20261007-082440-t05-extraction",
        "diag/20261125-093202-dose-reponse",
        "diag/20261006-134235-t05-corpus",
        "runs/20261125-093202-dose-reponse",
    ], env=env_git, check=True)

    nb_sha_ok = 0
    for sub in ("donnees/20261125-093202-dose-reponse", "diag/20261125-093202-dose-reponse", "runs/20261125-093202-dose-reponse"):
        for sf in sorted((WT_DR_LECT / sub).rglob("*.sha256")):
            att, nom = sf.read_text("utf-8").strip().split(None, 1)
            nom = nom.lstrip("*")
            cible = sf.parent / Path(nom).name
            got = hashlib.sha256(cible.read_bytes()).hexdigest()
            assert got == att, f"Sceau invalide: {sf} ({got} != {att})"
            nb_sha_ok += 1

    st_clean = subprocess.check_output(["git", "-C", str(WT_DR_LECT), "status", "--porcelain"], text=True).strip()
    print(f"SCEAUX_RUN_VERIFIES_OK: {nb_sha_ok} fichiers .sha256 | arbre_propre={st_clean == ''}")

    # 4. Vérifier les dépendances et arguments de lecture_v2.py et lancer_lecteur_texte_dose_reponse_v2.sh
    for vname in ("venv-py314", "venv-cpu"):
        py_cand = SCRATCH / vname / "Scripts" / "python.exe"
        if py_cand.is_file():
            r_imp = subprocess.run(
                [str(py_cand), "-c", "import controle_ia.dose_reponse.lecture_v2 as m; print('IMPORT_OK')"],
                cwd=str(WT_DR_LECT),
                env={**os.environ, "PYTHONPATH": str(WT_DR_LECT / "src"), "PYTHONUTF8": "1"},
                capture_output=True, text=True,
            )
            print(f"ENV {vname}: rc={r_imp.returncode} out={r_imp.stdout.strip()!r} err={r_imp.stderr.strip()[:200]!r}")

    lect_py = (WT_DR_LECT / "src/controle_ia/dose_reponse/lecture_v2.py").read_text("utf-8")
    print("\n--- Fin de lecture_v2.py (CLI) ---")
    print("\n".join(lect_py.splitlines()[-55:]))
finally:
    askpass.unlink(missing_ok=True)
