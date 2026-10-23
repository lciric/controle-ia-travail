#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, json, pathlib, time, sys, os

HOME = pathlib.Path.home()
ENV_PATH = HOME / ".env.collider.json"
HARD_KILL_SWITCH_USD = 480.00
MAX_BUDGET_USD = 500.00

CLUSTER_TOPOLOGY_VAST = [
    {
        "node_id": "NODE_A_VOLET_I_K0",
        "role": "Porte E0 (Shard 1) + Volet I (k=0 Jumeau Ni? sigma_r^0, Hedges d_z, 2^B Sign-Flip vs CCS/RepE/MassMean/Patchscopes)",
        "num_gpus": 1,
        "min_vram_gb": 78,
        "max_dph_usd": 3.50,
        "est_hours_h100": 6.0,
        "worker_arg": "--volet I"
    },
    {
        "node_id": "NODE_B_VOLET_II_DOCLAMP",
        "role": "Porte E0 (Shard 2) + Volet II (K=6 Rejets, Do-Clamp Affine Idempotent, Koopman C1 + rand-parc L_inf vs LEACE/INLP)",
        "num_gpus": 1,
        "min_vram_gb": 78,
        "max_dph_usd": 3.50,
        "est_hours_h100": 6.0,
        "worker_arg": "--volet II"
    },
    {
        "node_id": "NODE_C_VOLETS_III_IV_H9",
        "role": "Porte E0 (Shard 3) + Volets III & IV (Pare-feu Sol/Astra JSD Miller-Madow + H9 d=1..6 AR(1)-CUSUM & Jonckheere-Terpstra)",
        "num_gpus": 1,
        "min_vram_gb": 78,
        "max_dph_usd": 3.50,
        "est_hours_h100": 6.0,
        "worker_arg": "--volet III_IV"
    },
    {
        "node_id": "NODE_D_VOLET_V_SWARM_70B",
        "role": "Porte E0 (Shard 4) + Volet V (Essaim Chim?re 70B Llama-3.1+Mistral+Qwen, CMH, Breslow-Day, TOST & LoRA Commit-Reveal)",
        "num_gpus": 2,
        "min_vram_gb": 78,
        "max_dph_usd": 7.50,
        "est_hours_h100": 7.5,
        "worker_arg": "--volet V_70B"
    },
]

def load_creds():
    return json.loads(ENV_PATH.read_text(encoding="utf-8-sig")) if ENV_PATH.exists() else {}

def vast_api(api_key: str, endpoint: str, method: str = "GET", payload: dict = None) -> dict:
    url = f"https://console.vast.ai/api/v0/{endpoint.lstrip('/')}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        url, data=data, method=method,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "ControleIA-Vast-Autopilot/2.1"
        }
    )
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode("utf-8"))

def build_onstart_script(node_cfg: dict, hf_token: str, gh_token: str) -> str:
    auth_repo = f"https://{gh_token}@github.com/lciric/controle-ia-travail.git" if gh_token else "https://github.com/lciric/controle-ia-travail.git"
    return (
        "#!/bin/bash\n"
        "set -e\n"
        f"export HF_TOKEN='{hf_token}'\n"
        "export PYTHONUTF8=1\n"
        "apt-get update -qq && apt-get install -y -qq git python3-pip\n"
        "pip install -q torch transformers accelerate bitsandbytes scikit-learn scipy numpy\n"
        "cd /workspace || cd /root\n"
        f"git clone {auth_repo} controle-ia-gpu || (cd controle-ia-gpu && git pull origin main)\n"
        "cd controle-ia-gpu\n"
        "git config user.name 'Lazar Ciric GPU Cluster'\n"
        "git config user.email 'lciric@controle-ia.org'\n"
        f"python3 gemini/11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF/run_campagne_gpu_72h_5_volets_llama3.py {node_cfg['worker_arg']} > {node_cfg['node_id']}.log 2>&1\n"
        f"git pull --rebase origin main || true\n"
        f"git add {node_cfg['node_id']}.log gemini/11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF/\n"
        f"git commit -m 'Resultats GPU certifies depuis {node_cfg['node_id']}' || true\n"
        "git push origin main || true\n"
    )

def search_best_vast_offer(api_key: str, node_cfg: dict) -> list:
    q_filter = {
        "verified": {"eq": True},
        "external": {"eq": False},
        "rentable": {"eq": True},
        "rented": {"eq": False},
        "num_gpus": {"eq": node_cfg["num_gpus"]},
        "gpu_ram": {"gte": node_cfg["min_vram_gb"] * 1024},
        "inet_down": {"gte": 1500},
        "reliability2": {"gte": 0.98},
        "dph_total": {"lte": node_cfg["max_dph_usd"]},
        "order": [["dlperf_per_dphtotal", "desc"]],
        "type": "on-demand"
    }
    res = vast_api(api_key, f"bundles/?q={urllib.parse.quote(json.dumps(q_filter))}", method="GET")
    return res.get("offers", [])

def rent_vast_instance(api_key: str, offer: dict, node_cfg: dict, hf_token: str, gh_token: str) -> dict:
    offer_id = offer["id"]
    payload = {
        "client_id": "me",
        "image": "pytorch/pytorch:2.4.0-cuda12.4-cudnn9-devel",
        "disk": 120,
        "label": node_cfg["node_id"],
        "onstart": build_onstart_script(node_cfg, hf_token, gh_token),
        "runtype": "ssh"
    }
    res = vast_api(api_key, f"asks/{offer_id}/", method="PUT", payload=payload)
    return {
        "contract_id": res.get("new_contract"),
        "offer_id": offer_id,
        "gpu_name": offer.get("gpu_name"),
        "num_gpus": offer.get("num_gpus"),
        "dph_total": round(float(offer.get("dph_total", 0.0)), 3),
        "dlperf": round(float(offer.get("dlperf", 0.0)), 1),
        "inet_down_mbps": int(offer.get("inet_down", 0))
    }

def destroy_vast_instance(api_key: str, contract_id):
    if not contract_id:
        return
    try:
        vast_api(api_key, f"instances/{contract_id}/", method="DELETE")
        print(f"  [Kill-Switch Vast.ai] Instance `{contract_id}` d?truite avec succ?s (facturation stopp?e).")
    except Exception as e:
        print(f"  [Alerte] ?chec de destruction de l'instance `{contract_id}` : {e}")

def run_orchestrator():
    creds = load_creds()
    vast_key = creds.get("VAST_API_KEY", "").strip()
    hf_token = creds.get("HF_TOKEN", "").strip()
    gh_token = (creds.get("CONTROLE_IA_GITHUB_TOKEN") or creds.get("GITHUB_TOKEN") or "").strip()

    print("===========================================================================")
    print("=== 1. VERIFICATION DU COMPTE VAST.AI & SOLDE DISPONIBLE                ===")
    print("===========================================================================")
    try:
        user_info = vast_api(vast_key, "users/current/", method="GET")
        credit = float(user_info.get("credit", 0.0))
        email = user_info.get("email", "Compte Vast.ai")
        print(f"  * Connect? ? Vast.ai : {email} | Cr?dit disponible : {credit:.2f} USD")
    except Exception as e:
        print(f"  * Info connexion Vast.ai : {e}")

    print("\n===========================================================================")
    print("=== 2. SCAN LIVE DES MEILLEURES OFFRES VAST.AI (4 NOEUDS EN PARALLELE)  ===")
    print("===========================================================================")
    used_offer_ids = set()
    best_offers_plan = []
    total_hourly = 0.0

    for n in CLUSTER_TOPOLOGY_VAST:
        try:
            offers = search_best_vast_offer(vast_key, n)
            chosen = next((o for o in offers if o["id"] not in used_offer_ids), None)
            if chosen:
                used_offer_ids.add(chosen["id"])
                dph = float(chosen.get("dph_total", 0.0))
                total_hourly += dph
                info = {
                    "node_id": n["node_id"],
                    "offer_id": chosen["id"],
                    "gpu_name": chosen.get("gpu_name"),
                    "num_gpus": chosen.get("num_gpus"),
                    "vram_gb_per_gpu": round(float(chosen.get("gpu_ram", 0)) / 1024.0, 1),
                    "dph_usd": round(dph, 3),
                    "inet_down_mbps": int(chosen.get("inet_down", 0)),
                    "dlperf": round(float(chosen.get("dlperf", 0.0)), 1),
                    "dlperf_per_dph": round(float(chosen.get("dlperf_per_dphtotal", 0.0)), 2)
                }
                best_offers_plan.append((n, chosen, info))
                print(f"  * [{n['node_id']:24s}] -> {info['num_gpus']}x {info['gpu_name']} ({info['vram_gb_per_gpu']} Go) @ {info['dph_usd']:.3f} $/h | DLPerf={info['dlperf']} | Net={info['inet_down_mbps']} Mbps | OfferID={info['offer_id']}")
            else:
                print(f"  * [{n['node_id']:24s}] Aucune offre sous {n['max_dph_usd']} $/h ? cet instant.")
        except Exception as e:
            print(f"  [Erreur Scan {n['node_id']}] : {e}")

    print("---------------------------------------------------------------------------")
    print(f"  => Tarif horaire total des 4 noeuds simultan?s : {total_hourly:.3f} USD / heure")
    print(f"  => Co?t total estim? pour ~6h30 en parall?le   : {total_hourly * 6.5:.2f} USD (Coupe-Circuit actif ? {HARD_KILL_SWITCH_USD:.2f} USD)")
    print("---------------------------------------------------------------------------")

    
    if "--deploy-single-fast" in sys.argv:
        print("\n>>> [MODE COMMANDO 1 NOEUD ULTRA-RAPIDE (COMPATIBLE SOLDE 13.29 USD)]")
        print("    Location d'UN SEUL noeud RTX PRO 6000 S (96 Go VRAM) avec r?seau ultra-rapide qui ex?cute `--volet ALL` (~2h30 = ~4.20 USD) !")
        best_single = sorted(best_offers_plan, key=lambda x: x[2]["inet_down_mbps"], reverse=True)[0]
        n_cfg, off, info = best_single
        n_cfg = dict(n_cfg)
        n_cfg["node_id"] = "NODE_MASTER_ALL_5_VOLETS_96GB"
        n_cfg["worker_arg"] = "--volet ALL"
        best_offers_plan = [(n_cfg, off, info)]

    if "--deploy-live" not in sys.argv and "--deploy-single-fast" not in sys.argv:
        print("\n[FEU VERT] Les 4 offres Vast.ai sont pr?tes ! Pour louer r?ellement les 4 instances maintenant, lance :")
        print("  python gemini/11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF/cloud_gpu_autopilot/orchestrateur_cloud_gpu_parallele_500usd.py --deploy-live")
        return {"status": "VAST_OFFERS_FOUND_READY_TO_DEPLOY", "total_hourly_usd": round(total_hourly, 3), "offers": [x[2] for x in best_offers_plan]}

    active_contracts = []
    start_ts = time.time()
    try:
        print("\n>>> [D?PLOIEMENT LIVE VAST.AI] Location simultan?e des 4 noeuds GPU...")
        for n_cfg, off, info in best_offers_plan:
            rented = rent_vast_instance(vast_key, off, n_cfg, hf_token, gh_token)
            cid = rented.get("contract_id")
            if cid:
                active_contracts.append((cid, rented["dph_total"], n_cfg["node_id"]))
                print(f"  [Instance Vast.ai Lou?e] {n_cfg['node_id']} -> Contract ID={cid} ({rented['num_gpus']}x {rented['gpu_name']} @ {rented['dph_total']} $/h)")
        while active_contracts:
            elapsed_h = (time.time() - start_ts) / 3600.0
            spent_usd = sum(rate * elapsed_h for _, rate, _ in active_contracts)
            print(f"  [Monitoring Cluster Vast.ai] Temps={elapsed_h*60:.1f} min | D?pens?={spent_usd:.2f} USD / {HARD_KILL_SWITCH_USD:.2f} USD")
            if spent_usd >= HARD_KILL_SWITCH_USD or elapsed_h >= 12.0:
                print("  [COUPE-CIRCUIT ATTEINT] Arr?t et destruction imm?diate de toutes les instances !")
                break
            time.sleep(60)
    finally:
        for cid, _, n_id in active_contracts:
            destroy_vast_instance(vast_key, cid)
    return {"status": "VAST_CAMPAIGN_FINISHED_AND_CLEANED"}

if __name__ == "__main__":
    res = run_orchestrator()
    (pathlib.Path(__file__).parent / "ETAT_CLUSTER_VASTAI_500USD.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
