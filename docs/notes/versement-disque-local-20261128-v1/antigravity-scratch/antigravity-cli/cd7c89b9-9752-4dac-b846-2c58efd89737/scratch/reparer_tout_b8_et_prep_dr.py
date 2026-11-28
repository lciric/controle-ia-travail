import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(
    r"C:\Users\lciri\.gemini\antigravity-cli\brain"
    r"\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch"
)
VAST_EXE = SCRATCH / "venv-py314" / "Scripts" / "vastai.exe"
WT_B8 = SCRATCH / "wt-b8-puissance"
WT_DR_LECT = SCRATCH / "lecture-dr"

gh_tok = subprocess.check_output(["gh", "auth", "token"], text=True, timeout=20).strip()
vk = Path.home() / ".config" / "vastai" / "vast_api_key"
vast_key = os.environ.get("VAST_API_KEY", "").strip() or vk.read_text("utf-8").strip()

def mask(s: str) -> str:
    for sec in (gh_tok, vast_key):
        if sec and len(sec) >= 8:
            s = s.replace(sec, "***")
    return re.sub(r"(gh[opsu]_|github_pat_|hf_)[A-Za-z0-9_]{8,}", r"\1***", s)

askpass = SCRATCH / "_askpass_gh_tmp.cmd"
askpass.write_text("@echo off\necho %GH_TOK_MEM%\n", encoding="utf-8")
env_git = {
    **os.environ,
    "GIT_ASKPASS": str(askpass),
    "GIT_TERMINAL_PROMPT": "0",
    "GH_TOK_MEM": gh_tok,
    "PYTHONUTF8": "1",
}
remote_url = "https://x-access-token@github.com/lciric/controle-ia-travail.git"

def rm_win(p: Path) -> None:
    if not p.exists():
        return
    def _onexc(func, path, exc):
        os.chmod(path, stat.S_IWRITE)
        func(path)
    shutil.rmtree(p, onexc=_onexc)

def verifier_ou_reparer_lf(cible: Path, sha_attendu: str) -> bool:
    raw = cible.read_bytes()
    if hashlib.sha256(raw).hexdigest() == sha_attendu:
        return False
    raw_lf = raw.replace(b"\r\n", b"\n")
    if hashlib.sha256(raw_lf).hexdigest() == sha_attendu:
        cible.write_bytes(raw_lf)
        return True
    raise RuntimeError(f"Empreinte irréconciliable sur {cible} (attendu {sha_attendu[:12]}…)")

try:
    # 0. Point sur l'instance Vast.ai 62647167 (72 cœurs)
    print("=== 0. ÉTAT DE L'INSTANCE 62647167 (SONDES V2) ===")
    try:
        req = urllib.request.Request(
            "https://console.vast.ai/api/v0/instances/",
            headers={"Authorization": f"Bearer {vast_key}", "Accept": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=25) as resp:
            insts = json.loads(resp.read().decode("utf-8")).get("instances", [])
        i64 = next((i for i in insts if str(i.get("id")) == "62647167"), None)
        if i64:
            print(f"status={i64.get('actual_status')} | cpu={i64.get('cpu_util')}% | mem={i64.get('mem_usage')}Go")
            logs = subprocess.check_output(
                [str(VAST_EXE), "logs", "62647167"],
                env={**os.environ, "VAST_API_KEY": vast_key, "PYTHONUTF8": "1"},
                text=True, timeout=25, stderr=subprocess.STDOUT,
            )
            print(mask("\n".join(logs.splitlines()[-12:])))
        else:
            print("62647167 ABSENTE (terminée et autodétruite !)")
        ls_suite = subprocess.check_output(
            ["git", "-C", str(REPO), "ls-remote", remote_url, "refs/heads/calcul/sondes-v2-epreuve-plantee-v4-suite"],
            env=env_git, text=True,
        ).strip()
        print("Branche suite sur GitHub:", ls_suite or "(en cours de calcul)")
    except Exception as e:
        print("INFO_62647167:", mask(repr(e)))

    # 1. Réparation exhaustive CRLF -> LF dans wt-b8-puissance + archivage du journal essai 2
    print("\n=== 1. VÉRIFICATION ET RÉPARATION LF SUR wt-b8-puissance ===")
    subprocess.run(["git", "-C", str(REPO), "config", "extensions.worktreeConfig", "true"], check=True)
    subprocess.run(["git", "-C", str(WT_B8), "config", "--worktree", "core.autocrlf", "false"], check=True)

    nb_fixes = 0
    nb_verifies = 0

    # 1a. Tous les compagnons .sha256 présents dans wt-b8-puissance
    for sf in sorted(WT_B8.rglob("*.sha256")):
        if ".git" in sf.parts:
            continue
        raw_sf = sf.read_bytes()
        if b"\r\n" in raw_sf:
            sf.write_bytes(raw_sf.replace(b"\r\n", b"\n"))
        ligne = sf.read_text("utf-8").strip().splitlines()[0]
        m = re.match(r"^([0-9a-f]{64})\s+\*?(.+)$", ligne)
        if not m:
            continue
        att, nom = m.group(1), m.group(2).strip()
        cible = sf.parent / Path(nom).name
        if not cible.is_file() and (WT_B8 / nom).is_file():
            cible = WT_B8 / nom
        if cible.is_file():
            if verifier_ou_reparer_lf(cible, att):
                nb_fixes += 1
            nb_verifies += 1

    # 1b. Toutes les lignes scellées de registres/sondes-iib-v1.md
    reg_iib = (WT_B8 / "registres/sondes-iib-v1.md").read_text("utf-8")
    for ligne in reg_iib.splitlines():
        if ligne.startswith("|"):
            cols = [c.strip().strip("`") for c in ligne.split("|")]
            for idx_c, val in enumerate(cols):
                if re.fullmatch(r"[0-9a-f]{64}", val) and idx_c >= 1:
                    ch_cand = cols[idx_c - 1]
                    p_cand = WT_B8 / ch_cand
                    if p_cand.is_file():
                        if verifier_ou_reparer_lf(p_cand, val):
                            nb_fixes += 1
                        nb_verifies += 1

    # 1c. Tous les fichiers *bordereau*.json présents dans wt-b8-puissance (sans imprimer aucun contenu)
    def inspecter_bordereau(obj, dossier_base: Path):
        fx, ok = 0, 0
        if isinstance(obj, dict):
            ch = obj.get("chemin") or obj.get("fichier") or obj.get("path")
            sh = obj.get("sha256") or obj.get("empreinte")
            if isinstance(ch, str) and isinstance(sh, str) and re.fullmatch(r"[0-9a-f]{64}", sh):
                for cand in (WT_B8 / ch, dossier_base / ch, dossier_base / Path(ch).name):
                    if cand.is_file():
                        if verifier_ou_reparer_lf(cand, sh):
                            fx += 1
                        ok += 1
                        break
            for k, v in obj.items():
                if isinstance(k, str) and isinstance(v, str) and re.fullmatch(r"[0-9a-f]{64}", v):
                    for cand in (WT_B8 / k, dossier_base / k):
                        if cand.is_file():
                            if verifier_ou_reparer_lf(cand, v):
                                fx += 1
                            ok += 1
                            break
                sub_fx, sub_ok = inspecter_bordereau(v, dossier_base)
                fx += sub_fx
                ok += sub_ok
        elif isinstance(obj, list):
            for item in obj:
                sub_fx, sub_ok = inspecter_bordereau(item, dossier_base)
                fx += sub_fx
                ok += sub_ok
        return fx, ok

    for bp in sorted(WT_B8.rglob("*bordereau*.json")):
        if ".git" in bp.parts:
            continue
        b_fx, b_ok = inspecter_bordereau(json.loads(bp.read_text("utf-8")), bp.parent)
        nb_fixes += b_fx
        nb_verifies += b_ok

    bord_liv = WT_B8 / "versement/20261124-122719-rejeu-activations-voie-a/sortie-passe/livraison/bordereau-livraison-passe-barreau8-v1.json"
    sha_bord_liv = hashlib.sha256(bord_liv.read_bytes()).hexdigest()
    assert sha_bord_liv == "85bae5dcd9799f0a517f70eef2eb0d2c147ff3a3963fcb54f494e214a5a972fa", sha_bord_liv

    subprocess.run(["git", "-C", str(WT_B8), "update-index", "--refresh"], check=False, capture_output=True)
    st_b8 = subprocess.check_output(
        ["git", "-C", str(WT_B8), "status", "--porcelain", "--untracked-files=all"], text=True
    ).strip()
    assert st_b8 == "", f"wt-b8-puissance non vide : {st_b8}"

    # 1d. Archiver journal-lecture-sondes-barreau8-v1 et garantir l'absence du dossier pour mkdir
    j_cur = SCRATCH / "journal-lecture-sondes-barreau8-v1"
    j_bak2 = SCRATCH / "journal-lecture-sondes-barreau8-v1-essai2-refus5-crlf"
    if j_cur.exists():
        assert not j_bak2.exists(), f"{j_bak2} existe déjà"
        shutil.move(str(j_cur), str(j_bak2))
        print("ARCHIVE_JOURNAL_ESSAI2_OK:", j_bak2.name)
    assert not j_cur.exists(), "journal-lecture-sondes-barreau8-v1 existe encore !"
    print(f"WT_B8_VERIFIE_OK: {nb_verifies} contrôles SHA-256 passés ({nb_fixes} remis en LF), bordereau=85bae5dcd979…, arbre vide")
    print("PRET_POUR_RELANCE_LECTEUR_B8: OUI")

    # 2. Inscription sur origin/main par git mktree pur (REPO principal non touché)
    print("\n=== 2. INSCRIPTION R-5414 À R-5416 SUR ORIGIN/MAIN ===")
    subprocess.run(
        ["git", "-C", str(REPO), "fetch", remote_url, "main:refs/remotes/origin/main"],
        env=env_git, check=True,
    )
    parent_sha = subprocess.check_output(
        ["git", "-C", str(REPO), "rev-parse", "refs/remotes/origin/main"], text=True
    ).strip()
    dec_txt = subprocess.check_output(["git", "-C", str(REPO), "show", f"{parent_sha}:registres/decisions.md"]).decode("utf-8")
    arr_txt = subprocess.check_output(["git", "-C", str(REPO), "show", f"{parent_sha}:registres/arrets.md"]).decode("utf-8")

    meta_64 = json.loads((SCRATCH / "sondes-v2-64c-launch.json").read_text("utf-8"))
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    r_nums = [int(m.group(1)) for m in re.finditer(r"^- R-(\d+) ", dec_txt, re.M) if int(m.group(1)) < 9000]
    next_r = max(r_nums) + 1
    modif = False

    if "62647167" not in dec_txt:
        r1 = f"R-{next_r}"; next_r += 1
        l1 = (
            f"- {r1} ({meta_64['created_utc']}) — Épreuve synthétique à vérité plantée des sondes "
            f"de la boîte blanche version 2 (GO-2026-11-25-07, reliquat GO-2026-11-24-02) : amorce "
            f"version 7 (`{meta_64['amorce_sha256'][:12]}…`) contre-lue en classe B (`bdaeb71f…`, "
            f"essais conformes) versée sur main (`cfa696277b39`) ; instance Vast.ai `62647167` lancée "
            f"(offre `{meta_64['offre_id']}`, 72 cœurs, 63 Go mémoire vive, 0,2139 USD/h stockage "
            f"compris, minuterie 20 700 s) pour calculer `[130, 500)` du mode étalon et chronométrer "
            f"1 réplique du mode complet vers `calcul/sondes-v2-epreuve-plantee-v4-suite`."
        )
        assert len(l1) <= 600; dec_txt = dec_txt.rstrip("\n") + "\n" + l1 + "\n"; modif = True

    if "a3e16ec24" not in dec_txt:
        r2 = f"R-{next_r}"; next_r += 1
        l2 = (
            f"- {r2} ({now_utc}) — Course de dose-réponse de l'organisme à consigne cachée "
            f"(GO-2026-11-24-25, GO-2026-11-25-01, GO-2026-11-25-02) : 64 blocs sur 64 (1 920 "
            f"épisodes) scellés et versés avec preuve sur `origin/calcul/dose-reponse-v1` (tête "
            f"`a3e16ec24`, résultats `e375d9461`, traces `71db3302a`, aucun coût ni score ouvert) ; "
            f"autodestruction de l'instance Vast.ai `62498862` vérifiée (absente, quatre témoins "
            f"intouchables présents). Révocation du jeton GitHub coordonnée dès la clôture de "
            f"`62647167` (option a de Lazar)."
        )
        assert len(l2) <= 600; dec_txt = dec_txt.rstrip("\n") + "\n" + l2 + "\n"; modif = True

    if "REFUS [5]" not in dec_txt:
        r3 = f"R-{next_r}"; next_r += 1
        l3 = (
            f"- {r3} ({now_utc}) — Lecture décisive des sondes sur le saboteur à budget (barreau 8, "
            f"GO-2026-11-24-28) : après un arrêt avant Python (`01`, collage tronqué), un arrêt "
            f"`REFUS [5]` aux conditions de départ avant garde de réception et avant tout score lu "
            f"(`02`, `bordereau-livraison-passe-barreau8-v1.json` en CRLF sous Windows) et un arrêt "
            f"`mkdir` avant Python (journal non encore déplacé), remise en LF vérifiée à l'octet, "
            f"journaux archivés et relance technique déclarée (texte scellé, plan, point 4)."
        )
        assert len(l3) <= 600; dec_txt = dec_txt.rstrip("\n") + "\n" + l3 + "\n"; modif = True

    if "62498862" not in arr_txt:
        la = (
            f"| {now_utc} | instance Vast 62498862 (`dose-reponse-v1`, A100 SXM4 80 Go, "
            f"GO-2026-11-24-25 / GO-2026-11-25-01) | AUTODÉTRUITE par son amorce v4 (R10) après fin "
            f"normale (`64/64` blocs) et versement prouvé sur `origin/calcul/dose-reponse-v1` "
            f"(`e375d9461`, `71db3302a`, `a3e16ec24`) | absence vérifiée sur l'API Vast.ai (témoins "
            f"`58936096`, `58936099`, `58936100`, `60988826` intacts) ; ≈ 20,8 h à 1,1933 USD/h + "
            f"1,04 USD forfait ≈ 25,9 USD sur 90 USD |\n"
        )
        arr_txt = arr_txt.rstrip("\n") + "\n" + la; modif = True

    if modif:
        blob_dec = subprocess.check_output(["git", "-C", str(REPO), "hash-object", "-w", "--stdin"], input=dec_txt.encode("utf-8")).decode().strip()
        blob_arr = subprocess.check_output(["git", "-C", str(REPO), "hash-object", "-w", "--stdin"], input=arr_txt.encode("utf-8")).decode().strip()

        reg_lines = subprocess.check_output(["git", "-C", str(REPO), "ls-tree", f"{parent_sha}:registres"], text=True).splitlines()
        new_reg_lines = []
        for line in reg_lines:
            meta_p, name = line.split("\t", 1)
            mode, typ, sha = meta_p.split()
            if name == "decisions.md":
                sha = blob_dec
            elif name == "arrets.md":
                sha = blob_arr
            new_reg_lines.append(f"{mode} {typ} {sha}\t{name}")
        reg_tree = subprocess.check_output(
            ["git", "-C", str(REPO), "mktree"], input=("\n".join(new_reg_lines) + "\n").encode("utf-8")
        ).decode().strip()

        root_lines = subprocess.check_output(["git", "-C", str(REPO), "ls-tree", parent_sha], text=True).splitlines()
        new_root_lines = []
        for line in root_lines:
            meta_p, name = line.split("\t", 1)
            mode, typ, sha = meta_p.split()
            if name == "registres":
                sha = reg_tree
            new_root_lines.append(f"{mode} {typ} {sha}\t{name}")
        root_tree = subprocess.check_output(
            ["git", "-C", str(REPO), "mktree"], input=("\n".join(new_root_lines) + "\n").encode("utf-8")
        ).decode().strip()

        msg = "R-5414 a R-5416 : Vast 62647167 lancee, Vast 62498862 close (64/64), relance technique CRLF barreau 8\n"
        commit_sha = subprocess.check_output(
            ["git", "-C", str(REPO), "commit-tree", root_tree, "-p", parent_sha], input=msg.encode("utf-8")
        ).decode().strip()
        subprocess.run(["git", "-C", str(REPO), "push", remote_url, f"{commit_sha}:refs/heads/main"], env=env_git, check=True)
        print("PUSH_MAIN_MKTREE_OK:", commit_sha[:12])
    else:
        print("REGISTRES_DEJA_A_JOUR")

    # 3. Préparer lecture-dr avec core.protectNTFS=false + sparse-checkout
    print("\n=== 3. PRÉPARATION DE lecture-dr ET VÉRIFICATION DES 64 BLOCS ===")
    subprocess.run(
        ["git", "-C", str(REPO), "fetch", remote_url, "calcul/dose-reponse-v1:refs/remotes/origin/calcul/dose-reponse-v1"],
        env=env_git, check=True,
    )
    if WT_DR_LECT.exists() and not (WT_DR_LECT / "src").exists():
        subprocess.run(["git", "-C", str(REPO), "worktree", "remove", "--force", str(WT_DR_LECT)], check=False)
        rm_win(WT_DR_LECT)
        subprocess.run(["git", "-C", str(REPO), "worktree", "prune"], check=False)

    if not WT_DR_LECT.exists():
        subprocess.run([
            "git", "-C", str(REPO), "-c", "core.autocrlf=false", "-c", "core.protectNTFS=false",
            "worktree", "add", "--no-checkout", "--detach", str(WT_DR_LECT), "origin/calcul/dose-reponse-v1",
        ], env=env_git, check=True)
        for k, v in (("core.autocrlf", "false"), ("core.protectNTFS", "false"), ("core.sparseCheckout", "true"), ("core.sparseCheckoutCone", "true")):
            subprocess.run(["git", "-C", str(WT_DR_LECT), "config", "--worktree", k, v], env=env_git, check=True)

        gitdir_wt = Path(subprocess.check_output(["git", "-C", str(WT_DR_LECT), "rev-parse", "--git-dir"], text=True).strip())
        if not gitdir_wt.is_absolute():
            gitdir_wt = (WT_DR_LECT / gitdir_wt).resolve()
        info_dir = gitdir_wt / "info"
        info_dir.mkdir(parents=True, exist_ok=True)
        sparse_rules = "\n".join([
            "/*", "!/*/", "/src/", "/scripts/", "/tests/", "/prereg/", "/brouillons/", "/registres/", "/.claude/",
            "/donnees/20261125-093202-dose-reponse/",
            "/donnees/20261124-144844-banque-dose-reponse-extraction-v2/",
            "/donnees/20261007-082440-t05-extraction/",
            "/diag/20261125-093202-dose-reponse/",
            "/diag/20261006-134235-t05-corpus/",
            "/runs/20261125-093202-dose-reponse/",
        ]) + "\n"
        (info_dir / "sparse-checkout").write_bytes(sparse_rules.encode("utf-8"))
        subprocess.run(
            ["git", "-c", "core.protectNTFS=false", "-C", str(WT_DR_LECT), "read-tree", "--reset", "-u", "HEAD"],
            env=env_git, check=True,
        )

    nb_sha_ok = 0
    for sub in ("donnees/20261125-093202-dose-reponse", "diag/20261125-093202-dose-reponse", "runs/20261125-093202-dose-reponse"):
        for sf in sorted((WT_DR_LECT / sub).rglob("*.sha256")):
            att, nom = sf.read_text("utf-8").strip().split(None, 1)
            cible = sf.parent / Path(nom.lstrip("*")).name
            assert hashlib.sha256(cible.read_bytes()).hexdigest() == att, f"Sceau invalide: {sf}"
            nb_sha_ok += 1

    st_clean = subprocess.check_output(["git", "-C", str(WT_DR_LECT), "status", "--porcelain"], text=True).strip()
    print(f"LECTURE_DR_PRETE_OK: {nb_sha_ok} sceaux .sha256 vérifiés | arbre_propre={st_clean == ''}")

    lect_py = (WT_DR_LECT / "src/controle_ia/dose_reponse/lecture_v2.py").read_text("utf-8")
    print("\n--- CLI de lecture_v2.py ---")
    print("\n".join(lect_py.splitlines()[-35:]))
finally:
    askpass.unlink(missing_ok=True)
