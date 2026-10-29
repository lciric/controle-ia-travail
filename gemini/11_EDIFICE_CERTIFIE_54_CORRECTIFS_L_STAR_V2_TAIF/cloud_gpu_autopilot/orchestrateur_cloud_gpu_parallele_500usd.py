#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, urllib.error, json, pathlib, time, sys, os, subprocess

HOME = pathlib.Path.home()
ENV_PATH = HOME / ".env.collider.json"
REPO_DIR = HOME / "controle-ia-travail"
RES_DIR = REPO_DIR / "gemini" / "11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF" / "resultats_gpu_reels_vastai"
HARD_KILL_SWITCH_USD = 480.00

CLUSTER_TOPOLOGY_VAST = [
    {
        "node_id": "NODE_A_VOLET_I_K0",
        "role": "Porte E0 + Volet I (k=0 Jumeau Ni? sigma_r^0, Hedges d_z, 2^B Sign-Flip vs CCS/RepE/MassMean)",
        "num_gpus": 1,
        "min_vram_gb": 70,
        "max_dph_usd": 3.80,
        "worker_arg": "--volet I",
        "expected_file": "RESULTAT_REEL_GPU_VOLET_I_K0.json"
    },
    {
        "node_id": "NODE_B_VOLET_II_DOCLAMP",
        "role": "Porte E0 + Volet II (K=6 Rejets, Do-Clamp Affine Idempotent, Koopman C1 + rand-parc L_inf)",
        "num_gpus": 1,
        "min_vram_gb": 70,
        "max_dph_usd": 3.80,
        "worker_arg": "--volet II",
        "expected_file": "RESULTAT_REEL_GPU_VOLET_II_DOCLAMP.json"
    },
    {
        "node_id": "NODE_C_VOLETS_III_IV_H9",
        "role": "Porte E0 + Volets III & IV (Pare-feu Sol/Astra JSD Miller-Madow + H9 d=1..6 AR(1)-CUSUM)",
        "num_gpus": 1,
        "min_vram_gb": 70,
        "max_dph_usd": 3.80,
        "worker_arg": "--volet III_IV",
        "expected_file": "RESULTAT_REEL_GPU_VOLETS_III_IV_H9.json"
    },
    {
        "node_id": "NODE_D_VOLET_V_SWARM_70B",
        "role": "Porte E0 + Volet V (Essaim Chim?re Multi-Esp?ces Llama-3.1 + Qwen2.5 + Mistral, CMH, Breslow-Day, LoRA)",
        "num_gpus": 2,
        "min_vram_gb": 70,
        "max_dph_usd": 7.80,
        "worker_arg": "--volet V_70B",
        "expected_file": "RESULTAT_REEL_GPU_VOLET_V_CHIMERE.json"
    },
]

def load_creds():
    return json.loads(ENV_PATH.read_text(encoding="utf-8-sig")) if ENV_PATH.exists() else {}

def vast_api(api_key: str, endpoint: str, method: str = "GET", payload: dict = None) -> dict:
    sep = "&" if "?" in endpoint else "?"
    url = f"https://console.vast.ai/api/v0/{endpoint.lstrip('/')}{sep}api_key={urllib.parse.quote(api_key)}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        url, data=data, method=method,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "ControleIA-Vast-Autopilot/3.0"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read().decode("utf-8", errors="replace")
            return json.loads(raw) if raw.strip() else {}
    except urllib.error.HTTPError as he:
        err_body = he.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {he.code} sur {endpoint} : {err_body[:300]}")

def build_onstart_script(node_cfg: dict, hf_token: str, gh_token: str) -> str:
    auth_repo = f"https://{gh_token}@github.com/lciric/controle-ia-travail.git" if gh_token else "https://github.com/lciric/controle-ia-travail.git"
    return (
        "#!/bin/bash\n"
        "export HF_TOKEN='" + hf_token + "'\n"
        "export PYTHONUTF8=1\n"
        "apt-get update -qq && apt-get install -y -qq git python3-pip || true\n"
        "pip install -q torch transformers accelerate bitsandbytes scikit-learn scipy numpy sentencepiece protobuf || true\n"
        "cd /workspace 2>/dev/null || cd /root\n"
        f"git clone {auth_repo} controle-ia-gpu || (cd controle-ia-gpu && git pull origin main)\n"
        "cd controle-ia-gpu\n"
        "git config user.name 'Lazar Ciric GPU Cluster'\n"
        "git config user.email 'lciric@ens-paris-saclay.fr'\n"
        f"python3 gemini/11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF/run_campagne_gpu_72h_5_volets_llama3.py {node_cfg['worker_arg']} > {node_cfg['node_id']}.log 2>&1\n"
        "git pull --rebase origin main || true\n"
        f"git add {node_cfg['node_id']}.log gemini/11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF/ || true\n"
        f"git commit -m 'Resultats GPU finaux certifies depuis {node_cfg['node_id']}' || true\n"
        "git push origin main || true\n"
    )

def search_vast_candidates(api_key: str, node_cfg: dict) -> list:
    q_filter = {
        "verified": {"eq": True},
        "external": {"eq": False},
        "rentable": {"eq": True},
        "rented": {"eq": False},
        "num_gpus": {"eq": node_cfg["num_gpus"]},
        "gpu_ram": {"gte": node_cfg["min_vram_gb"] * 1024},
        "disk_space": {"gte": 65},
        "inet_down": {"gte": 1000},
        "reliability2": {"gte": 0.97},
        "dph_total": {"lte": node_cfg["max_dph_usd"]},
        "order": [["dlperf_per_dphtotal", "desc"]],
        "type": "on-demand"
    }
    res = vast_api(api_key, f"bundles/?q={urllib.parse.quote(json.dumps(q_filter))}", method="GET")
    return res.get("offers", [])

def rent_with_failover(api_key: str, candidates: list, used_ids: set, node_cfg: dict, hf_token: str, gh_token: str) -> dict:
    for off in candidates[:15]:
        oid = off["id"]
        if oid in used_ids:
            continue
        used_ids.add(oid)
        max_disk = float(off.get("disk_space", 80))
        req_disk = min(80, max(40, int(max_disk * 0.8)))
        payload = {
            "client_id": "me",
            "image": "pytorch/pytorch:2.4.0-cuda12.4-cudnn9-devel",
            "disk": req_disk,
            "label": node_cfg["node_id"],
            "onstart": build_onstart_script(node_cfg, hf_token, gh_token),
            "runtype": "ssh"
        }
        try:
            res = vast_api(api_key, f"asks/{oid}/", method="PUT", payload=payload)
            if res.get("success") or res.get("new_contract"):
                return {
                    "contract_id": res.get("new_contract"),
                    "offer_id": oid,
                    "gpu_name": off.get("gpu_name"),
                    "num_gpus": off.get("num_gpus"),
                    "dph_total": round(float(off.get("dph_total", 0.0)), 3),
                    "dlperf": round(float(off.get("dlperf", 0.0)), 1),
                    "inet_down_mbps": int(off.get("inet_down", 0))
                }
            else:
                print(f"    [Failover {node_cfg['node_id']}] Offre {oid} refusee ({res}), essai offre suivante...")
        except Exception as e:
            print(f"    [Failover {node_cfg['node_id']}] Offre {oid} indisponible ({e}), essai offre suivante...")
            time.sleep(1.0)
    return {}

def destroy_vast_instance(api_key: str, contract_id):
    if not contract_id:
        return
    try:
        vast_api(api_key, f"instances/{contract_id}/", method="DELETE")
        print(f"  [Kill-Switch Vast.ai] Instance `{contract_id}` detruite avec succes (facturation stoppee).")
    except Exception as e:
        print(f"  [Info Destruction `{contract_id}`] : {e}")

def run_orchestrator():
    creds = load_creds()
    vast_key = creds.get("VAST_API_KEY", "").strip()
    hf_token = creds.get("HF_TOKEN", "").strip()
    gh_token = (creds.get("CONTROLE_IA_GITHUB_TOKEN") or creds.get("GITHUB_TOKEN") or "").strip()

    user_info = vast_api(vast_key, "users/current/", method="GET")
    print("===========================================================================")
    print(f"=== COMPTE VAST.AI : {user_info.get('email')} | SOLDE : {float(user_info.get('credit', 0.0)):.2f} USD (Auto-Topup Actif) ===")
    print("===========================================================================")

    used_offer_ids = set()
    active_contracts = {}
    total_spent_closed = 0.0
    start_ts = time.time()

    try:
        print("\n>>> [DEPLOIEMENT LIVE VAST.AI AVEC FAILOVER AUTOMATIQUE] Location des 4 noeuds GPU...")
        for n_cfg in CLUSTER_TOPOLOGY_VAST:
            cands = search_vast_candidates(vast_key, n_cfg)
            print(f"  * [{n_cfg['node_id']:24s}] {len(cands)} offres candidates haute vitesse trouvees sur Vast.ai...")
            rented = rent_with_failover(vast_key, cands, used_offer_ids, n_cfg, hf_token, gh_token)
            cid = rented.get("contract_id")
            if cid:
                active_contracts[cid] = {
                    "node_id": n_cfg["node_id"],
                    "dph": rented["dph_total"],
                    "expected_file": n_cfg["expected_file"],
                    "gpu_name": rented["gpu_name"],
                    "num_gpus": rented["num_gpus"],
                    "rent_ts": time.time()
                }
                print(f"    -> [LOUE OK] {n_cfg['node_id']} : ContractID={cid} ({rented['num_gpus']}x {rented['gpu_name']} @ {rented['dph_total']} $/h | Net={rented['inet_down_mbps']} Mbps)")
            else:
                print(f"    -> [ALERTE] Aucune offre n'a pu etre louee pour {n_cfg['node_id']}.")

        print("\n===========================================================================")
        print(f"=== SURVEILLANCE ACTIVE DES {len(active_contracts)} NOEUDS GPU & SYNCHRONISATION GITHUB ===")
        print("===========================================================================")

        while active_contracts:
            time.sleep(60)
            now_ts = time.time()
            elapsed_global_h = (now_ts - start_ts) / 3600.0

            try:
                subprocess.run(["git", "pull", "--rebase", "origin", "main"], cwd=str(REPO_DIR), capture_output=True, timeout=30)
            except Exception:
                pass

            running_cost = sum(info["dph"] * ((now_ts - info["rent_ts"]) / 3600.0) for info in active_contracts.values())
            total_spent = total_spent_closed + running_cost
            print(f"  [Watchdog {elapsed_global_h*60:.0f} min] Noeuds actifs={len(active_contracts)} | Depense cumulee={total_spent:.2f} USD / {HARD_KILL_SWITCH_USD:.2f} USD")

            for cid, info in list(active_contracts.items()):
                exp_f = RES_DIR / info["expected_file"]
                log_f = REPO_DIR / f"{info['node_id']}.log"
                if exp_f.exists() and log_f.exists():
                    node_h = (now_ts - info["rent_ts"]) / 3600.0
                    total_spent_closed += info["dph"] * node_h
                    print(f"  >>> [JOB TERMINE SUR GITHUB] `{info['node_id']}` a livre `{info['expected_file']}` ! Destruction immediate du pod `{cid}`...")
                    destroy_vast_instance(vast_key, cid)
                    del active_contracts[cid]

            if total_spent >= HARD_KILL_SWITCH_USD or elapsed_global_h >= 12.0:
                print("  [COUPE-CIRCUIT BUDGETAIRE / TEMPOREL ATTEINT] Destruction immediate de tous les pods restants !")
                break
    finally:
        for cid in list(active_contracts.keys()):
            destroy_vast_instance(vast_key, cid)

    return {"status": "VAST_LIVE_CLUSTER_COMPLETED"}

if __name__ == "__main__":
    res = run_orchestrator()
    (pathlib.Path(__file__).parent / "ETAT_CLUSTER_VASTAI_500USD.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
