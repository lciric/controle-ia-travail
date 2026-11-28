from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import traceback
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

MAX_BLOB_OCTETS = 45 * 1024 * 1024  # < 100 Mo GitHub

P8_INTERDIT_RE = re.compile(
    r"(?i)(?:"
    r"\.(?:npz|npy|safetensors|pt|pth|bin|gguf|h5|ckpt|tar|gz|tgz|zip|7z|xz)$"
    r"|(^|/)(?:consigne[-_]privee|consignes[-_]privees|P3-consignes|verites-epreuve|conception-ii-b)"
    r"|(^|/)(?:\.env|\.venv|venv|__pycache__|\.pytest_cache|\.mypy_cache|node_modules|\.git)(/|$)"
    r"|(^|/)sondes-(?:figees|neuves|actions).*\.npz$"
    r"|(^|/)planchers-.*\.npz$"
    r"|(^|/)scripts/_(?:go_2026_11_28_v4\.md|etape1_worker_v4\.py)$"
    r")"
)

PIECES_R2_R5 = [
    (
        "contre-lecture-r2-etages-1-2-v1.md",
        "8325ba1c052db3d9b6431265e37f03b1014fae6b2e391948edce231a1952a30d",
        "docs/notes/audit-r2-etages-1-2-v1/contre-lecture-r2-etages-1-2-v1.md",
    ),
    (
        "test_oracles_r5_cloture_etages_1_2.py",
        "893eee8ff515b02a7dd70f7de9f62fb2037f9d76b4ad5acd590b6b035a4e5c0c",
        "tests/test_oracles_r5_cloture_etages_1_2.py",
    ),
    (
        "contre-epreuve-r2-volets-11-13-v1.md",
        "59a2a571c687da0e1a6c84cd3e2bc5f9cb3a8e016bbcc4bb3f52d6f0b61020ac",
        "docs/notes/audit-r2-etages-1-2-v1/contre-epreuve-r2-volets-11-13-v1.md",
    ),
    (
        "test_contre_epreuve_v4_r5.py",
        "a39bdffe76bb444d5700499fbc1d1ed354f23119370e8ad4a8b40a4c0732ec28",
        "tests/test_contre_epreuve_v4_r5.py",
    ),
]


def git(args: list[str], cwd: Path | None = None, env: dict[str, str] | None = None,
        check: bool = True, text: bool = True, input_data: str | bytes | None = None) -> subprocess.CompletedProcess:
    e = dict(os.environ)
    e["MSYS_NO_PATHCONV"] = "1"
    e["MSYS2_ARG_CONV_EXCL"] = "*"
    if env:
        e.update(env)
    return subprocess.run(
        ["git", *args],
        cwd=str(cwd) if cwd else None,
        env=e,
        input=input_data,
        check=check,
        capture_output=True,
        text=text,
        encoding="utf-8" if text else None,
        errors="replace" if text else None,
    )


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ecrire_lf_atomique(cible: Path, data: bytes) -> str:
    cible.parent.mkdir(parents=True, exist_ok=True)
    propre = data.replace(b"\r\n", b"\n")
    tmp = cible.with_name(f".{cible.name}.tmp.{os.getpid()}")
    tmp.write_bytes(propre)
    os.replace(tmp, cible)
    return sha256_bytes(propre)


def verifier_vast_et_resultats(main_wt: Path) -> dict[str, object]:
    bilan: dict[str, object] = {}
    # 1. Vérification des résultats locaux et branches distantes (zéro ouverture de .npz, P8 strict)
    dr_dir = main_wt / "donnees" / "20261125-093202-dose-reponse"
    nb_txt, nb_mes, nb_npz_noms = 0, 0, 0
    if dr_dir.is_dir():
        for r_s, _, files in os.walk(dr_dir):
            for f in files:
                if f == "textes.jsonl":
                    nb_txt += 1
                elif f == "mesures.jsonl":
                    nb_mes += 1
                elif f.endswith(".npz"):
                    nb_npz_noms += 1
    bilan["dose_reponse_local"] = {
        "dossier_present": dr_dir.is_dir(),
        "blocs_textes_jsonl": nb_txt,
        "blocs_mesures_jsonl": nb_mes,
        "fichiers_npz_presents_non_ouverts": nb_npz_noms,
    }

    branches_dist = git(["for-each-ref", "--format=%(refname:short)", "refs/remotes/origin/"], cwd=main_wt, check=False).stdout.splitlines()
    bilan["branches_calcul_audit_sur_origin"] = [
        b for b in branches_dist if any(k in b for k in ("dose-reponse", "barreau8", "audit", "passation", "sauvetage"))
    ]

    # 2. Sonde Vast.ai (CLI ou clé API locale sans jamais exposer la clé)
    vast_info: dict[str, object] = {"methode": "aucune_cle_vast_locale"}
    vast_cli = shutil.which("vastai")
    if vast_cli:
        r_v = subprocess.run([vast_cli, "show", "instances", "--raw"], capture_output=True, text=True, timeout=10)
        if r_v.returncode == 0 and r_v.stdout.strip():
            try:
                insts = json.loads(r_v.stdout)
                vast_info = {
                    "methode": "vastai_cli",
                    "nb_instances_actives_ou_stoppees": len(insts),
                    "instances": [
                        {
                            "id": it.get("id"),
                            "status": it.get("actual_status") or it.get("cur_state"),
                            "gpu": it.get("gpu_name"),
                            "dph_total_usd": it.get("dph_total"),
                            "label": it.get("label"),
                        }
                        for it in insts
                    ],
                }
            except Exception as exc:
                vast_info = {"methode": "vastai_cli_parse_err", "detail": str(exc)[:160]}
    else:
        api_key = os.environ.get("VAST_API_KEY", "").strip()
        if not api_key:
            for kp in [Path.home() / ".vast_api_key", Path.home() / ".config" / "vastai" / "vast_api_key"]:
                if kp.is_file():
                    api_key = kp.read_text(encoding="utf-8", errors="ignore").strip()
                    if api_key:
                        break
        if api_key:
            try:
                req = urllib.request.Request(
                    "https://console.vast.ai/api/v0/instances/?owner=me",
                    headers={"Authorization": f"Bearer {api_key}", "Accept": "application/json"},
                )
                with urllib.request.urlopen(req, timeout=10) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                insts = data.get("instances", data if isinstance(data, list) else [])
                vast_info = {
                    "methode": "vast_rest_api",
                    "nb_instances_actives_ou_stoppees": len(insts),
                    "instances": [
                        {
                            "id": it.get("id"),
                            "status": it.get("actual_status") or it.get("cur_state"),
                            "gpu": it.get("gpu_name"),
                            "dph_total_usd": it.get("dph_total"),
                            "label": it.get("label"),
                        }
                        for it in insts
                    ],
                }
            except Exception as exc:
                vast_info = {"methode": "vast_rest_api_err", "detail": str(exc)[:160]}
        else:
            vast_info = {
                "methode": "aucune_cle_vast_sur_ce_pc",
                "conseil": "Verifier https://cloud.vast.ai/instances/ dans le navigateur pour confirmer 0 instance active.",
            }
    bilan["vast_ai_live"] = vast_info
    return bilan


def main() -> int:
    repo_arg = Path(sys.argv[1]).resolve()
    tmp_dir = Path(tempfile.mkdtemp(prefix="etape1_v4_"))
    try:
        # 1. Liste des worktrees
        wt_lines = git(["worktree", "list", "--porcelain"], cwd=repo_arg).stdout.splitlines()
        worktrees: list[dict[str, str]] = []
        cur: dict[str, str] = {}
        for ln in wt_lines:
            if not ln.strip():
                if cur:
                    worktrees.append(cur)
                    cur = {}
                continue
            k, _, v = ln.partition(" ")
            cur[k] = v.strip()
        if cur:
            worktrees.append(cur)

        main_wt = Path(worktrees[0]["worktree"]) if worktrees else repo_arg
        wt_sur_main: Path | None = None
        for w in worktrees:
            if w.get("branch") == "refs/heads/main":
                wt_sur_main = Path(w["worktree"])
                main_wt = wt_sur_main
                break

        git(["config", "core.autocrlf", "false"], cwd=main_wt, check=False)
        git(["fetch", "origin", "--prune"], cwd=main_wt, check=False)

        print("=== [1/7] Bilan Vast.ai et resultats du run d'il y a 3 jours ===")
        bilan_vast = verifier_vast_et_resultats(main_wt)
        print(json.dumps(bilan_vast, indent=2, ensure_ascii=False))

        # 2. Sauvetage non destructif de tous les worktrees via GIT_INDEX_FILE + SHA-1 d'arbre
        print(f"=== [2/7] Inspection et sauvetage hors-P8 des {len(worktrees)} worktree(s) ===")
        rapports_wt: list[dict[str, object]] = []
        branches_sauvetage: list[str] = []

        for idx, w in enumerate(worktrees):
            wt_path = Path(w["worktree"])
            wt_head = w.get("HEAD", "")
            wt_branch = w.get("branch", "DETACHED")
            slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", wt_path.name).strip("-") or f"wt-{idx}"
            info: dict[str, object] = {
                "worktree": str(wt_path),
                "branch": wt_branch,
                "head": wt_head,
                "fichiers_captures": [],
                "ignores": [],
                "ref_sauvetage": None,
            }
            if not wt_path.is_dir():
                info["statut"] = "absent"
                rapports_wt.append(info)
                continue

            tr_res = git(["rev-parse", "--verify", "HEAD^{tree}"], cwd=wt_path, check=False)
            if tr_res.returncode != 0:
                info["statut"] = "head_tree_invalide"
                rapports_wt.append(info)
                continue
            head_tree = tr_res.stdout.strip()

            st_raw = git(["status", "--porcelain=v1", "-z", "-uall"], cwd=wt_path, text=False, check=False).stdout
            morceaux = st_raw.split(b"\x00")
            cands_add: list[str] = []
            ignores: list[str] = []
            i = 0
            while i < len(morceaux):
                ent = morceaux[i]
                i += 1
                if not ent or len(ent) < 4:
                    continue
                xy = ent[:2].decode("ascii", errors="replace")
                rel = ent[3:].decode("utf-8", errors="surrogateescape").replace("\\", "/")
                if xy[0] in ("R", "C") and i < len(morceaux):
                    i += 1
                if P8_INTERDIT_RE.search(rel):
                    ignores.append(f"P8_OU_TMP:{rel}")
                    continue
                plein = wt_path / rel
                if plein.is_file() and not plein.is_symlink():
                    sz = plein.stat().st_size
                    if sz > MAX_BLOB_OCTETS:
                        ignores.append(f"TAILLE>{MAX_BLOB_OCTETS}:{rel}")
                    else:
                        cands_add.append(rel)

            info["ignores"] = ignores[:25]
            ref_save = f"refs/heads/sauvetage/20261128-{idx:02d}-{slug}"

            if cands_add:
                idx_file = tmp_dir / f"idx_wt_{idx}"
                env_idx = {"GIT_INDEX_FILE": str(idx_file)}
                git(["read-tree", head_tree], cwd=wt_path, env=env_idx)
                for k0 in range(0, len(cands_add), 50):
                    git(["add", "-f", "--", *cands_add[k0:k0 + 50]], cwd=wt_path, env=env_idx)
                new_tree = git(["write-tree"], cwd=wt_path, env=env_idx).stdout.strip()
                if new_tree != head_tree:
                    msg = f"sauvetage(passation-v4): capture worktree {slug} ({wt_branch}) [hors-P8]"
                    c_sha = git(["commit-tree", new_tree, "-p", wt_head, "-m", msg], cwd=wt_path).stdout.strip()
                    git(["update-ref", ref_save, c_sha], cwd=main_wt)
                    branches_sauvetage.append(ref_save.replace("refs/heads/", ""))
                    info["ref_sauvetage"] = ref_save
                    info["commit_sauvetage"] = c_sha
                    info["fichiers_captures"] = cands_add
            elif wt_branch == "DETACHED" and wt_head:
                cont = git(["branch", "-r", "--contains", wt_head], cwd=main_wt, check=False).stdout.strip()
                if not cont:
                    git(["update-ref", ref_save, wt_head], cwd=main_wt)
                    branches_sauvetage.append(ref_save.replace("refs/heads/", ""))
                    info["ref_sauvetage"] = ref_save
            rapports_wt.append(info)

        # 3. Audit et push de toutes les branches locales non poussées (avec assainissement auto si P8/taille bloque)
        print("=== [3/7] Sauvegarde sur origin de toutes les branches locales des 3 derniers jours ===")
        toutes_branches = [
            b.strip() for b in git(["for-each-ref", "--format=%(refname:short)", "refs/heads/"], cwd=main_wt).stdout.splitlines()
            if b.strip() and b.strip() != "main"
        ]
        branches_poussees: list[str] = []
        branches_assainies: dict[str, object] = {}

        base_origin_main = git(["rev-parse", "--verify", "refs/remotes/origin/main"], cwd=main_wt, check=False).stdout.strip()
        if not base_origin_main:
            base_origin_main = git(["rev-parse", "refs/heads/main"], cwd=main_wt).stdout.strip()

        for br in sorted(set(toutes_branches + branches_sauvetage)):
            ahead = git(["rev-list", f"refs/heads/{br}", "--not", "--remotes=origin"], cwd=main_wt, check=False).stdout.splitlines()
            if not ahead:
                continue
            objs = git(["rev-list", "--objects", f"refs/heads/{br}", "--not", "--remotes=origin"], cwd=main_wt).stdout
            lignes_b = git(
                ["cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize) %(rest)"],
                cwd=main_wt,
                input_data=objs,
            ).stdout.splitlines()

            infractions: list[str] = []
            for ln in lignes_b:
                mor = ln.split(" ", 3)
                if len(mor) < 4 or mor[1] != "blob":
                    continue
                _, _, sz_str, chemin_b = mor
                if P8_INTERDIT_RE.search(chemin_b):
                    infractions.append(f"P8:{chemin_b}")
                elif int(sz_str) > MAX_BLOB_OCTETS:
                    infractions.append(f"TAILLE({sz_str}):{chemin_b}")

            if not infractions:
                p1 = git(["push", "-u", "origin", f"refs/heads/{br}:refs/heads/{br}"], cwd=main_wt, check=False)
                if p1.returncode == 0:
                    branches_poussees.append(br)
                else:
                    horo = datetime.now(timezone.utc).strftime("%H%M%S")
                    br_alt = f"sauvetage/20261128-copie-{re.sub(r'[^a-zA-Z0-9._-]+', '-', br)}-{horo}"
                    p2 = git(["push", "-u", "origin", f"refs/heads/{br}:refs/heads/{br_alt}"], cwd=main_wt, check=False)
                    if p2.returncode == 0:
                        branches_poussees.append(f"{br}->{br_alt}")
                    else:
                        branches_assainies[br] = {"erreur_push": p1.stderr.strip()[:200]}
            else:
                # Construction automatique d'une archive assainie sans les blobs P8/géants pour ne perdre aucun texte/code !
                ls_br = git(["ls-tree", "-r", "-l", f"refs/heads/{br}"], cwd=main_wt).stdout.splitlines()
                idx_clean = tmp_dir / f"idx_clean_{re.sub(r'[^a-zA-Z0-9]+', '_', br)}"
                env_cl = {"GIT_INDEX_FILE": str(idx_clean)}
                for item in ls_br:
                    meta, _, path_it = item.partition("\t")
                    parts_m = meta.split()
                    if len(parts_m) < 4:
                        continue
                    mode_it, _, sha_it, sz_it = parts_m[0], parts_m[1], parts_m[2], int(parts_m[3])
                    if P8_INTERDIT_RE.search(path_it) or sz_it > MAX_BLOB_OCTETS:
                        continue
                    git(["update-index", "--add", "--cacheinfo", f"{mode_it},{sha_it},{path_it}"], cwd=main_wt, env=env_cl)
                clean_tree = git(["write-tree"], cwd=main_wt, env=env_cl).stdout.strip()
                br_clean = f"sauvetage/20261128-propre-{re.sub(r'[^a-zA-Z0-9._-]+', '-', br)}"
                msg_cl = f"sauvetage(propre): {br} filtre hors-P8/taille sur parent origin/main"
                c_clean = git(["commit-tree", clean_tree, "-p", base_origin_main, "-m", msg_cl], cwd=main_wt).stdout.strip()
                git(["update-ref", f"refs/heads/{br_clean}", c_clean], cwd=main_wt)
                pc = git(["push", "-u", "origin", f"refs/heads/{br_clean}:refs/heads/{br_clean}"], cwd=main_wt, check=False)
                branches_assainies[br] = {
                    "infractions_exclues": infractions[:10],
                    "branche_propre_poussee": br_clean if pc.returncode == 0 else f"ECHEC:{pc.stderr.strip()[:150]}",
                }
        print(f"Branches poussees : {branches_poussees}")
        if branches_assainies:
            print(f"Branches assainies : {json.dumps(branches_assainies, ensure_ascii=False)}")

        # 4. Recherche sur disque + dans tous les blobs Git des 4 pièces R2/R5
        print("=== [4/7] Ancrage et verification SHA-256 des 4 pieces R2/R5 ===")
        racines_disque: list[Path] = [Path(w["worktree"]) for w in worktrees if Path(w["worktree"]).is_dir()]
        for ex in [repo_arg, main_wt.parent, Path.home() / "Downloads", Path.home() / "Desktop", Path.home() / "Documents"]:
            if ex.is_dir() and ex not in racines_disque:
                racines_disque.append(ex)

        tous_objets_git = git(["rev-list", "--all", "--objects"], cwd=main_wt, check=False).stdout.splitlines()
        statut_r2_r5: dict[str, dict[str, object]] = {}
        blobs_pour_main: dict[str, bytes] = {}

        for nom_f, sha_att, dest_rel in PIECES_R2_R5:
            contenu_ok: bytes | None = None
            src_ok: str | None = None
            sha_proches: list[str] = []

            for rac in racines_disque:
                max_p = 5 if rac in [Path(w["worktree"]) for w in worktrees] else 2
                for r_s, dirs, files in os.walk(rac):
                    if len(Path(r_s).relative_to(rac).parts) > max_p:
                        dirs[:] = []
                        continue
                    dirs[:] = [d for d in dirs if d not in {".git", ".venv", "venv", "donnees", "runs", "__pycache__", "node_modules"}]
                    for fn in files:
                        if fn == nom_f or nom_f.replace("-", "_") in fn.replace("-", "_"):
                            cand_p = Path(r_s) / fn
                            raw = cand_p.read_bytes()
                            lf = raw.replace(b"\r\n", b"\n")
                            if sha256_bytes(raw) == sha_att:
                                contenu_ok, src_ok = raw, str(cand_p)
                                break
                            if sha256_bytes(lf) == sha_att:
                                contenu_ok, src_ok = lf, f"{cand_p} (CRLF->LF)"
                                break
                            sha_proches.append(f"{cand_p}:{sha256_bytes(lf)[:16]}")
                    if contenu_ok is not None:
                        break
                if contenu_ok is not None:
                    break

            if contenu_ok is None:
                for obj_ln in tous_objets_git:
                    b_sha, _, b_path = obj_ln.partition(" ")
                    if b_path.endswith(nom_f) or nom_f in b_path:
                        raw_b = git(["cat-file", "blob", b_sha], cwd=main_wt, text=False, check=False).stdout
                        lf_b = raw_b.replace(b"\r\n", b"\n")
                        if sha256_bytes(lf_b) == sha_att:
                            contenu_ok, src_ok = lf_b, f"git_blob:{b_sha[:12]}:{b_path}"
                            break
                        sha_proches.append(f"blob:{b_sha[:10]}:{sha256_bytes(lf_b)[:16]}")

            if contenu_ok is not None:
                ecrire_lf_atomique(repo_arg / dest_rel, contenu_ok)
                if main_wt != repo_arg:
                    ecrire_lf_atomique(main_wt / dest_rel, contenu_ok)
                blobs_pour_main[dest_rel] = contenu_ok
                statut_r2_r5[nom_f] = {"present": True, "sha256_exact": True, "chemin": dest_rel, "source": src_ok}
            else:
                statut_r2_r5[nom_f] = {"present": False, "sha256_exact": False, "candidats_vus": sha_proches[:5]}
        print(json.dumps(statut_r2_r5, indent=2, ensure_ascii=False))

        # 5. Exécution des oracles Python R5 disponibles
        print("=== [5/7] Execution des suites d'oracles R5 ===")
        resultats_r5: dict[str, object] = {}
        for py_t in ("test_contre_epreuve_v4_r5.py", "test_oracles_r5_cloture_etages_1_2.py"):
            cible_t = repo_arg / "tests" / py_t
            if cible_t.is_file():
                rt = subprocess.run([sys.executable, str(cible_t)], cwd=str(repo_arg), capture_output=True, text=True)
                resultats_r5[py_t] = {
                    "returncode": rt.returncode,
                    "tail": (rt.stdout + "\n" + rt.stderr).strip().splitlines()[-4:],
                }
                print(f"  {py_t} -> code={rt.returncode} | {resultats_r5[py_t]['tail']}")

        # 6. Sonde lecture seule sous P8 de tirage.json (68ade33f…) vs taches-banque.json (0065065b…)
        print("=== [6/7] Sonde P8 tirage.json (68ade33f) vs taches-banque.json (0065065b) ===")
        sonde_tirage: dict[str, object] = {}
        for cle_nom, hint, pref in [
            ("tirage", "diag/20261006-134235-t05-corpus/tirage.json", "68ade33f"),
            ("banque", "donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json", "0065065b"),
        ]:
            data_j = None
            for cand_root in [repo_arg, main_wt]:
                pf = cand_root / hint
                if pf.is_file():
                    raw_j = pf.read_bytes()
                    if sha256_bytes(raw_j).startswith(pref):
                        data_j = json.loads(raw_j.decode("utf-8"))
                        sonde_tirage[f"{cle_nom}_source"] = str(pf)
                        break
            if data_j is None:
                for obj_ln in tous_objets_git:
                    b_sha, _, b_path = obj_ln.partition(" ")
                    if b_path.endswith(Path(hint).name):
                        raw_j = git(["cat-file", "blob", b_sha], cwd=main_wt, text=False, check=False).stdout
                        if sha256_bytes(raw_j).startswith(pref):
                            data_j = json.loads(raw_j.decode("utf-8"))
                            sonde_tirage[f"{cle_nom}_source"] = f"git_blob:{b_sha[:12]}"
                            break
            if cle_nom == "tirage" and isinstance(data_j, dict):
                res_d = data_j.get("resultat")
                if isinstance(res_d, dict):
                    sonde_tirage["tirage_cles_resultat"] = {
                        k: (len(v) if hasattr(v, "__len__") else type(v).__name__) for k, v in res_d.items()
                    }
                elif isinstance(res_d, list):
                    sonde_tirage["tirage_len_resultat"] = len(res_d)
            elif cle_nom == "banque" and data_j is not None:
                lst_b = data_j.get("taches") if isinstance(data_j, dict) else data_j
                if isinstance(lst_b, list):
                    sonde_tirage["banque_nb_taches"] = len(lst_b)
                    rangs = [x.get("rang_tirage") or x.get("rang") for x in lst_b if isinstance(x, dict)]
                    rangs_num = [r for r in rangs if isinstance(r, int)]
                    if rangs_num:
                        sonde_tirage["banque_rang_min_max"] = [min(rangs_num), max(rangs_num)]
        print(json.dumps(sonde_tirage, indent=2, ensure_ascii=False))

        # 7. Mise à jour append-only de registres/go.md et push sur origin/main par plomberie Git sans conflit de branche !
        print("=== [7/7] Versement append-only de GO-2026-11-28-01..03 et push sur origin/main ===")
        parent_main = git(["rev-parse", "--verify", "refs/remotes/origin/main"], cwd=main_wt, check=False).stdout.strip()
        local_main = git(["rev-parse", "--verify", "refs/heads/main"], cwd=main_wt, check=False).stdout.strip()
        if local_main and parent_main and local_main != parent_main:
            # Si main locale descend de origin/main et est propre hors-P8, on garde ses commits !
            est_anc = git(["merge-base", "--is-ancestor", parent_main, local_main], cwd=main_wt, check=False).returncode == 0
            if est_anc:
                parent_main = local_main
        elif local_main and not parent_main:
            parent_main = local_main

        parent_tree = git(["rev-parse", f"{parent_main}^{{tree}}"], cwd=main_wt).stdout.strip()
        go_orig_bytes = git(["show", f"{parent_main}:registres/go.md"], cwd=main_wt, text=False).stdout
        go_orig = go_orig_bytes.replace(b"\r\n", b"\n").decode("utf-8")
        go_ajout = (repo_arg / "scripts" / "_go_2026_11_28_v4.md").read_bytes().replace(b"\r\n", b"\n").decode("utf-8").strip()

        deja = [g for g in ("GO-2026-11-28-01", "GO-2026-11-28-02", "GO-2026-11-28-03") if g in go_orig]
        if len(deja) == 3:
            nouveau_go_bytes = go_orig.encode("utf-8")
            print("  GO-2026-11-28-01..03 deja presents sur main (idempotence tenue).")
        elif len(deja) == 0:
            prefixe = go_orig.rstrip("\n")
            nouveau_go_str = prefixe + "\n\n" + go_ajout + "\n"
            assert nouveau_go_str.startswith(prefixe), "Erreur interne : prefixe de go.md altere !"
            nouveau_go_bytes = nouveau_go_str.encode("utf-8")
        else:
            raise RuntimeError(f"Etat partiel inattendu de GO dans main : {deja}")

        blobs_pour_main["registres/go.md"] = nouveau_go_bytes

        inv_rel = "diag/passation-v4-20261128/inventaire-sauvetage-et-tirage-v4.json"
        inventaire_doc = {
            "horodatage_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "etape": "1/3",
            "bilan_vast_et_resultats_3j": bilan_vast,
            "worktrees_inspectes": rapports_wt,
            "branches_poussees_origin": branches_poussees,
            "branches_assainies_hors_p8": branches_assainies,
            "ancrages_r2_r5": statut_r2_r5,
            "oracles_r5": resultats_r5,
            "sonde_p8_tirage_vs_banque": sonde_tirage,
        }
        inv_bytes = (json.dumps(inventaire_doc, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
        blobs_pour_main[inv_rel] = inv_bytes

        sh_wrapper = repo_arg / "scripts" / "etape1_forensique_et_go_v4.sh"
        if sh_wrapper.is_file():
            blobs_pour_main["scripts/etape1_forensique_et_go_v4.sh"] = sh_wrapper.read_bytes().replace(b"\r\n", b"\n")

        idx_main = tmp_dir / "idx_commit_main"
        env_m = {"GIT_INDEX_FILE": str(idx_main)}
        git(["read-tree", parent_tree], cwd=main_wt, env=env_m)
        for rel_p, b_content in sorted(blobs_pour_main.items()):
            if P8_INTERDIT_RE.search(rel_p):
                raise RuntimeError(f"Blocage securite P8 : {rel_p}")
            b_oid = git(["hash-object", "-w", "--stdin"], cwd=main_wt, text=False, input_data=b_content).stdout.decode("ascii").strip()
            git(["update-index", "--add", "--cacheinfo", f"100644,{b_oid},{rel_p}"], cwd=main_wt, env=env_m)

        new_main_tree = git(["write-tree"], cwd=main_wt, env=env_m).stdout.strip()
        if new_main_tree != parent_tree:
            msg_m = "registres(go): verser GO-2026-11-28-01..03, ancrages R2/R5 et inventaire sauvetage 3j (etape 1/3)"
            commit_main = git(["commit-tree", new_main_tree, "-p", parent_main, "-m", msg_m], cwd=main_wt).stdout.strip()
        else:
            commit_main = parent_main

        git(["push", "origin", f"{commit_main}:refs/heads/main"], cwd=main_wt)

        # Synchronisation propre de la ref locale main et des fichiers sur disque
        if wt_sur_main is not None:
            for rel_p, b_content in blobs_pour_main.items():
                ecrire_lf_atomique(wt_sur_main / rel_p, b_content)
            git(["update-ref", "refs/heads/main", commit_main], cwd=wt_sur_main)
            git(["read-tree", commit_main], cwd=wt_sur_main)
        else:
            git(["update-ref", "refs/heads/main", commit_main], cwd=main_wt)
            for rel_p, b_content in blobs_pour_main.items():
                ecrire_lf_atomique(repo_arg / rel_p, b_content)

        # Nettoyage des 2 fichiers temporaires d'amorçage
        for f_tmp in (repo_arg / "scripts" / "_go_2026_11_28_v4.md", repo_arg / "scripts" / "_etape1_worker_v4.py"):
            if f_tmp.is_file():
                f_tmp.unlink()

        print(f"SUCCES COMPLET ETAPE 1/3 — origin/main est a {commit_main}")
        return 0
    except Exception:
        print("ERREUR INTERCEPTEE (la fenetre Git Bash reste ouverte) :")
        traceback.print_exc()
        return 1
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
