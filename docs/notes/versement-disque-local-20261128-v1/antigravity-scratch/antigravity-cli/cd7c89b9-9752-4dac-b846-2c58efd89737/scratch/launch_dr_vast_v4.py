import base64
import contextlib
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
WT_LANC = SCRATCH / "wt-lancement-dr-v2"
META_PATH = SCRATCH / "dr-launch-meta.json"
RUN_DIR = SCRATCH / "dr-lancement-v4-reel"

sys.path.insert(0, str(WT_LANC / "src"))
from controle_ia.dose_reponse import controles_v3 as ct
from controle_ia.lancement_t08 import session_v1 as s8
from controle_ia.t06 import session_v2 as s2, session_v3 as s3, session_v12 as s12


def mask(text: str, secrets: list[str]) -> str:
    for s in secrets:
        if s and len(s) >= 8:
            text = text.replace(s, "***")
    return text


def main():
    dry_run = "--execute" not in sys.argv
    meta = json.loads(META_PATH.read_text(encoding="utf-8"))
    c_new = meta["C_NEW"]
    l_new = meta["L_NEW"]
    bl = meta["BRANCHE_LANCEMENT"]
    amorce_sha = meta["AMORCE_V4_SHA256"]
    cfg_rel = meta["CONFIG"]
    prereg_rel = meta["PREREG"]
    branche_sortie = meta["BRANCHE_SORTIE"]
    go_id = meta["GO_ID"]

    # Load tokens strictly in memory, never printed
    hf_token = os.environ.get("HF_TOKEN", "").strip()
    assert len(hf_token) >= 8, "HF_TOKEN manquant"
    gh_token = subprocess.check_output(["gh", "auth", "token"], text=True).strip()
    assert len(gh_token) >= 8, "gh auth token manquant"
    vast_key_path = Path.home() / ".config" / "vastai" / "vast_api_key"
    vast_key = os.environ.get("VAST_API_KEY", "").strip()
    if not vast_key and vast_key_path.is_file():
        vast_key = vast_key_path.read_text(encoding="utf-8").strip()
    assert len(vast_key) >= 8, "VAST_API_KEY manquant"
    secrets = [hf_token, gh_token, vast_key]

    env = os.environ.copy()
    env["VAST_API_KEY"] = vast_key
    env["PYTHONUTF8"] = "1"
    env["PYTHONDONTWRITEBYTECODE"] = "1"

    # Verify préalable 1 bis on launch branch
    scel_txt = (WT_LANC / "registres/scellements-v1.md").read_text(encoding="utf-8")
    assert any(l.startswith("| DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE ") for l in scel_txt.splitlines()), "Préalable 1 bis absent"

    cfg_path = WT_LANC / cfg_rel
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    reg_go = str(WT_LANC / "registres/go.md")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    assert today < "2026-12-13", f"Après dernier jour de création ({today})"

    # GO & calendrier & vue-offre checks
    today_d = date.fromisoformat(today)
    go_res = s8.go_t08(reg_go, cfg, go_id, today_d)
    cal_res = s8.calendrier_t08(reg_go, cfg, go_id, today_d)
    fin_go = int(cal_res["fin_go_utc_s"])
    print("GO_CHECK:", go_res)
    print("CAL_CHECK:", cal_res)

    RUN_DIR.mkdir(parents=True, exist_ok=True)
    vue = s8.vue_offre(cfg)
    vue_path = RUN_DIR / "vue-offre.json"
    vue_path.write_text(json.dumps(vue, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    disque = int(vue["offre"]["disque_min_go"])
    etiq = vue["offre"]["etiquette"]
    assert disque >= 300

    # Check existing instances (never touch untouchables, refuse if label already exists)
    inst_raw = subprocess.check_output(["vastai", "show", "instances", "--raw"], env=env, text=True, timeout=120)
    inst_path = RUN_DIR / "instances.json"
    inst_path.write_text(mask(inst_raw, secrets), encoding="utf-8")
    inst_list = json.loads(inst_raw)
    inv_msg = s2.verifier_instances(inst_list, etiq)
    print("INSTANCES_OK:", inv_msg)

    # Search offers using exact session_v12 filtre + choisir_offre + controles_v3.exiger_offre_lue
    filtre = s12.filtre_recherche(vue, "course")
    print("FILTRE:", filtre)
    offres_raw = subprocess.check_output(
        ["vastai", "search", "offers", filtre, "-o", "dph_total", "--storage", str(disque), "--raw"],
        env=env, text=True, timeout=120,
    )
    offres_path = RUN_DIR / "offres.json"
    offres_path.write_text(mask(offres_raw, secrets), encoding="utf-8")
    offres_list = json.loads(offres_raw)

    # Optional exclude list (if previous attempt refused)
    excl_file = RUN_DIR / "machines_refusees.txt"
    excl = set()
    if excl_file.is_file():
        excl = {x.strip() for x in excl_file.read_text(encoding="utf-8").splitlines() if x.strip()}

    choisie = s12.choisir_offre(offres_list, vue, "course", excl)
    raw_offer = next(o for o in offres_list if int(o["id"]) == int(choisie["id"]))
    ct.exiger_offre_lue(raw_offer, cfg)

    offre_id = int(choisie["id"])
    mach = str(choisie["machine_id"])
    rang = int(choisie["rang"])
    pc = float(choisie["prix_carte"])
    ps = float(choisie["prix_stockage"])
    tel = float(choisie["telechargement_forfait_usd"])
    print(f"OFFRE_CONFORME: id={offre_id} rang={rang} machine={mach} gpu={raw_offer.get('gpu_name')} "
          f"prix_carte={pc:.4f} prix_stockage={ps:.4f} total_h={pc+ps:.4f} tel_forfait={tel:.4f} "
          f"reliab={raw_offer.get('reliability2', 0):.4f} geo={raw_offer.get('geolocation')}")

    now_s = int(time.time())
    dep = s3.depense_cumulee_v3(90, pc, ps, now_s, 0, tel, now_s)
    epuis = int(dep["epuisement_utc_s"])
    ech = min(epuis, fin_go)
    assert now_s < ech <= epuis
    print(f"DEPENSE_GUARD: epuisement_utc_s={epuis} ({datetime.fromtimestamp(epuis, timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}) "
          f"echeance_utc_s={ech} fin_go_utc_s={fin_go} heures_plafond={(epuis-now_s)/3600:.2f}h")

    # Extract amorce v4 directly from L_NEW blob (strictly LF) and verify SHA-256
    amorce_bytes = subprocess.check_output(
        ["git", "-C", str(WT_LANC), "show", f"{l_new}:scripts/amorce_instance_dose_reponse_v4.sh"]
    )
    assert hashlib.sha256(amorce_bytes).hexdigest() == amorce_sha, "Amorce SHA-256 mismatch!"
    b64 = base64.b64encode(amorce_bytes).decode("ascii")
    assert hashlib.sha256(base64.b64decode(b64)).hexdigest() == amorce_sha

    env_str_masked = (
        f"-e LANCEMENT={l_new} -e BRANCHE_LANCEMENT={bl} -e COMMIT_CODE={c_new} "
        f"-e PREREG={prereg_rel} -e CONFIG={cfg_rel} -e BRANCHE={branche_sortie} "
        f"-e GO_ID_DR={go_id} -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git "
        f"-e ECHEANCE_UTC_S={ech} -e FIN_GO_UTC_S={fin_go} -e DEPENSE_EPUISEE_UTC_S={epuis} "
        f"-e ESSAIS=8 -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN"
    )
    cmd_for_guard = (
        f"GO_ID={go_id} vastai create instance {offre_id} --raw --image python:3.11-bookworm "
        f"--disk {disque} --cancel-unavail --label {etiq} --env \"{env_str_masked}\" "
        f"--entrypoint bash --args -c \"echo {b64} | base64 -d > /root/amorce.sh && bash /root/amorce.sh\""
    )
    # Validate with .claude/hooks/garde_calcul.py!
    guard_in = json.dumps({"tool_input": {"command": cmd_for_guard}})
    guard_env = env.copy()
    guard_env["CLAUDE_PROJECT_DIR"] = str(WT_LANC)
    p_guard = subprocess.run(
        [sys.executable, str(WT_LANC / ".claude/hooks/garde_calcul.py")],
        input=guard_in, text=True, capture_output=True, cwd=str(WT_LANC), env=guard_env,
    )
    print("GARDE_CALCUL_RC:", p_guard.returncode, p_guard.stdout.strip(), p_guard.stderr.strip())
    assert p_guard.returncode == 0, f"garde_calcul.py REFUSED: {p_guard.stdout} {p_guard.stderr}"

    if dry_run:
        print("DRY_RUN_OK (pass --execute to actually create the Vast.ai instance)")
        return

    # Real execution — tokens injected directly in argv, NEVER printed!
    env_str_real = (
        f"-e LANCEMENT={l_new} -e BRANCHE_LANCEMENT={bl} -e COMMIT_CODE={c_new} "
        f"-e PREREG={prereg_rel} -e CONFIG={cfg_rel} -e BRANCHE={branche_sortie} "
        f"-e GO_ID_DR={go_id} -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git "
        f"-e ECHEANCE_UTC_S={ech} -e FIN_GO_UTC_S={fin_go} -e DEPENSE_EPUISEE_UTC_S={epuis} "
        f"-e ESSAIS=8 -e HF_TOKEN={hf_token} -e GH_TOKEN={gh_token}"
    )
    args = [
        "vastai", "create", "instance", str(offre_id),
        "--raw", "--image", "python:3.11-bookworm",
        "--disk", str(disque), "--cancel-unavail", "--label", etiq,
        "--env", env_str_real,
        "--entrypoint", "bash",
        "--args", "-c", f"echo {b64} | base64 -d > /root/amorce.sh && bash /root/amorce.sh",
    ]
    # Invoke vastai CLI in-process to avoid Windows CreateProcess 32 KB command-line limit (WinError 206)
    os.environ["VAST_API_KEY"] = vast_key
    os.environ["VASTAI_NO_UPDATE_CHECK"] = "1"
    from vastai.cli import main as vast_cli_main
    buf_out, buf_err = io.StringIO(), io.StringIO()
    old_argv = sys.argv
    rc = 0
    try:
        sys.argv = args
        with contextlib.redirect_stdout(buf_out), contextlib.redirect_stderr(buf_err):
            vast_cli_main.main()
    except SystemExit as exc:
        if exc.code in (None, 0):
            rc = 0
        elif isinstance(exc.code, int):
            rc = exc.code
        else:
            rc = 1
            buf_err.write(f"\n{exc.code}\n")
    finally:
        sys.argv = old_argv

    out_masked = mask(buf_out.getvalue() + "\n" + buf_err.getvalue(), secrets)
    print("CREATE_RC:", rc)
    print("CREATE_OUT:", out_masked.strip()[:1000])

    m_id = re.search(r"new_contract['\"]?\s*:\s*([0-9]+)", out_masked)
    ok = bool(re.search(r"success['\"]?\s*:\s*(True|true)", out_masked))
    if rc == 0 and m_id and ok:
        inst_id = m_id.group(1)
        cr_s = int(time.time())
        lancement_txt = (
            f"controles dose-reponse v4 {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\n"
            f"lancement {l_new}\n"
            f"branche_lancement {bl}\n"
            f"commit {c_new}\n"
            f"prereg {prereg_rel}\n"
            f"config {cfg_rel}\n"
            f"branche {branche_sortie}\n"
            f"amorce {amorce_sha}\n"
            f"go {go_id}\n"
            f"plafond 90\n"
            f"compte_rendu 72\n"
            f"mode reel\n"
            f"offre {offre_id}\n"
            f"carte course\n"
            f"storage {disque}\n"
            f"prix_carte {pc:.6f}\n"
            f"prix_stockage {ps:.6f}\n"
            f"telechargement_forfait {tel:.6f}\n"
            f"anterieure 0\n"
            f"echeance {ech}\n"
            f"epuisement {epuis}\n"
            f"plafond_creation 90\n"
            f"machine_proposee {mach}\n"
            f"rang {rang}\n"
            f"instance {inst_id}\n"
            f"creation {cr_s}\n"
        )
        (RUN_DIR / "lancement.txt").write_text(lancement_txt, encoding="utf-8")
        print(f"INSTANCE_CREATED_OK id={inst_id} creation_utc_s={cr_s} offre={offre_id} machine={mach} prix_total_h={pc+ps:.4f}")
    else:
        print("CREATE_FAILED_OR_UNCERTAIN — check vastai show instances before retrying!")
        if re.search(r"success['\"]?\s*:\s*(False|false)", out_masked) and not m_id:
            with excl_file.open("a", encoding="utf-8") as f:
                f.write(mach + "\n")
        sys.exit(4)


if __name__ == "__main__":
    main()
