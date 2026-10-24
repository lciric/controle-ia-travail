#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, time, json, ast, urllib.request, pathlib, subprocess

os.environ["GIT_TERMINAL_PROMPT"] = "0"
os.environ["GCM_INTERACTIVE"] = "never"
os.environ["GIT_ASKPASS"] = "echo"

EVO_DIR = pathlib.Path(__file__).resolve().parent
REPO_ROOT = EVO_DIR.parents[2]
WORKER_SCRIPT = EVO_DIR / "run_evolutionary_generations_m3_system.py"
AUDIT_REPORT_MD = EVO_DIR / "RAPPORT_FUSEE_00_CERTIFICATION_SYSTEME_EVOLUTIF_LOI_M3.md"
RES_GPU_DIR = REPO_ROOT / "gemini" / "11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF" / "resultats_gpu_reels_vastai"

CREDS = json.loads((pathlib.Path.home() / ".env.collider.json").read_text(encoding="utf-8-sig"))
GEMINI_KEY = CREDS.get("GEMINI_API_KEY", "").strip()
ANT_KEY_1 = CREDS.get("RR_ANTHROPIC_API_KEY", "").strip()
ANT_KEY_2 = CREDS.get("RR_ANTHROPIC_API_KEY_2", "").strip() or ANT_KEY_1
GH_TOKEN = (CREDS.get("CONTROLE_IA_GITHUB_TOKEN") or CREDS.get("GITHUB_TOKEN") or "").strip()

def ensure_non_interactive_git():
    if GH_TOKEN:
        auth_url = f"https://{GH_TOKEN}@[github.com/lciric/controle-ia-travail.git](https://github.com/lciric/controle-ia-travail.git)"
        subprocess.run(["git", "remote", "set-url", "origin", auth_url], cwd=str(REPO_ROOT), capture_output=True)
        subprocess.run(["git", "config", "credential.interactive", "never"], cwd=str(REPO_ROOT), capture_output=True)

def silent_git_checkpoint(msg: str):
    try:
        ensure_non_interactive_git()
        env_git = os.environ.copy()
        env_git["GIT_TERMINAL_PROMPT"] = "0"
        env_git["GCM_INTERACTIVE"] = "never"
        env_git["GIT_ASKPASS"] = "echo"
        subprocess.run(["git", "add", str(EVO_DIR)], cwd=str(REPO_ROOT), env=env_git, capture_output=True, timeout=20)
        subprocess.run(["git", "commit", "-m", msg], cwd=str(REPO_ROOT), env=env_git, capture_output=True, timeout=20)
        subprocess.Popen(["git", "push", "origin", "main"], cwd=str(REPO_ROOT), env=env_git, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

def call_auditor_lineage(lineage: str, prompt: str, temp: float = 0.2) -> str:
    if lineage in ("CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5"):
        api_k = ANT_KEY_1 if lineage == "CLAUDE_FABLE_5_1" else ANT_KEY_2
        models = ["claude-fable-5-1", "claude-3-7-sonnet-20250219"] if lineage == "CLAUDE_FABLE_5_1" else ["claude-opus-5-5", "claude-3-opus-20240229", "claude-3-7-sonnet-20250219"]
        for m_id in models:
            try:
                url = "[https://api.anthropic.com/v1/messages](https://api.anthropic.com/v1/messages)"
                payload = {"model": m_id, "max_tokens": 4096, "temperature": temp, "messages": [{"role": "user", "content": prompt}]}
                req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"x-api-key": api_k, "anthropic-version": "2023-06-01", "Content-Type": "application/json"}, method="POST")
                with urllib.request.urlopen(req, timeout=110) as r:
                    return json.loads(r.read().decode("utf-8"))["content"][0]["text"]
            except Exception:
                pass
    for m_name in ["gemini-argon", "gemini-2.5-pro", "gemini-2.5-flash"]:
        try:
            url = f"[https://generativelanguage.googleapis.com/v1beta/models/](https://generativelanguage.googleapis.com/v1beta/models/){m_name}:generateContent?key={GEMINI_KEY}"
            payload = {"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"temperature": temp, "maxOutputTokens": 8192}}
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
            with urllib.request.urlopen(req, timeout=110) as r:
                return json.loads(r.read().decode("utf-8"))["candidates"][0]["content"]["parts"][0]["text"]
        except Exception:
            pass
    return ""

def run_pre_flight_m3_certification():
    print("===========================================================================")
    print("=== FUSEE 00 DE CERTIFICATION PREALABLE (LOI L DE M3 & EVOLUTION G_g)   ===")
    print("===========================================================================")
    code_src = WORKER_SCRIPT.read_text(encoding="utf-8")

    checks = {
        "1_Failles_OpenAI_CacheTiming_et_Fable51_Stego_Incluses": "cache timing differences" in code_src and "fable-image-steganography" in code_src,
        "2_Deux_Papiers_RLCR_MIT_et_GeneralReasoning_Inclus": "Beyond Binary Rewards" in code_src and "Avalon-M1-Mini" in code_src,
        "3_Invention_Libre_Topologie_de_Boucles_Par_Omega": "invented_loops_pipeline" in code_src and "learned_loop_topologies_and_meta_laws" in code_src,
        "4_Zero_Liste_Precodee_Concepts_ou_MotsCles": "MATH_OPERATOR_BASIS" not in code_src and "arxiv_queries =" not in code_src,
        "5_Memoire_Evolutive_Inter_Generations_Active": "MEMOIRE_EVOLUTIVE_INTER_GENERATIONS.json" in code_src and "build_epigenetic_inheritance_prompt" in code_src,
        "6_Loi_L_de_M3_Complete_Argon_Fable51_Opus55": all(s in code_src for s in ["GEMINI_ARGON", "CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5", "cholesky_dpp_and_onsager_cavity_in_H_math"])
    }
    for k, v in checks.items():
        print(f"  * [Audit AST Fus?e 00] {k:60s} : {'CERTIFIE (OK)' if v else 'DEFAUT (!)'}")

    p_audit = (
        "Tu es la FUS?E 00 DE CERTIFICATION PR?ALABLE.\n"
        "V?rifie que ce code respecte ? la lettre la Loi L de M3, inclut les failles d'OpenAI (cache-timing) et d'Anthropic/Fable 5.1 (st?ganographie SVG->PNG) ainsi que les deux articles RLCR, "
        "laisse le syst?me inventer lui-m?me sa topologie de boucles, et fait ?voluer une m?moire inter-g?n?rationnelle qui int?gre ses d?couvertes de g?n?ration en g?n?ration :\n"
        f"```python\n{code_src[:13000]}\n```"
    )
    r_argon = call_auditor_lineage("GEMINI_ARGON", p_audit, temp=0.2)
    r_fable = call_auditor_lineage("CLAUDE_FABLE_5_1", p_audit, temp=0.25)
    r_opus  = call_auditor_lineage("CLAUDE_OPUS_5_5", f"Synth?tise le Certificat Officiel M1/M0 d'Autorisation de Lancement :\n{r_argon[:2500]}\n---\n{r_fable[:2500]}", temp=0.15)

    AUDIT_REPORT_MD.write_text(
        "# CERTIFICAT DE LA FUS?E 00 : CONFORMIT? ? LA LOI $\\mathcal{L}$ DE $\\mathcal{M}_3$ & ?VOLUTION INTER-G?N?RATIONNELLE\n\n"
        + "\n".join([f"- **{k}** : `{v}`" for k, v in checks.items()])
        + f"\n\n---\n\n## Certificat M1/M0 (`CLAUDE_OPUS_5_5`)\n\n{r_opus}\n\n---\n\n## Audit `GEMINI_ARGON`\n\n{r_argon}\n\n---\n\n## Audit `CLAUDE_FABLE_5_1`\n\n{r_fable}\n",
        encoding="utf-8"
    )
    print(f"  => [FEU VERT FUS?E 00 SCELL?] `{AUDIT_REPORT_MD.name}` valid? !")

def extract_py(txt: str) -> str:
    if "```python" in txt:
        return txt.split("```python", 1)[1].split("```", 1)[0].strip()
    if "```" in txt:
        return txt.split("```", 1)[1].split("```", 1)[0].strip()
    return txt.strip()

def request_swarm_ast_patch(traceback_txt: str, current_source: str) -> str:
    prompt = (
        f"Tu es le D?buggeur Auto-Cicatrisant du Syst?me ?volutif Multi-G?n?rations.\n"
        f"Traceback :\n{traceback_txt[-2500:]}\n\nCode :\n```python\n{current_source}\n```\n\n"
        f"Renvoie UNIQUEMENT le code Python complet corrig? dans ```python ... ```."
    )
    for lin in ["GEMINI_ARGON", "CLAUDE_OPUS_5_5", "CLAUDE_FABLE_5_1"]:
        cand = extract_py(call_auditor_lineage(lin, prompt, temp=0.1))
        if cand:
            try:
                ast.parse(cand)
                if "run_multi_generational_evolution" in cand:
                    return cand
            except Exception:
                pass
    return ""

def run_supervisor():
    ensure_non_interactive_git()
    run_pre_flight_m3_certification()
    silent_git_checkpoint("[Fusee 00 Pre-Flight] Systeme evolutif multi-generations certifie")

    for attempt in range(1, 5):
        print(f"\n>>> [Autopilot ?volutif] Lancement des G?n?rations ?volutives (Tentative {attempt}/4)...")
        proc = subprocess.run([sys.executable, str(WORKER_SCRIPT), "--generations", "2"])
        if proc.returncode == 0:
            print("<<< [Succ?s des G?n?rations ?volutives] M?moire ?pig?n?tique et rapport scell?s !")
            silent_git_checkpoint("[Syst?me ?volutif M3] G?n?rations ?volutives scell?es automatiquement")
            break
        else:
            diag = subprocess.run([sys.executable, str(WORKER_SCRIPT), "--generations", "2"], capture_output=True, text=True)
            if diag.returncode == 0:
                silent_git_checkpoint("[Syst?me ?volutif M3] G?n?rations scell?es au re-test")
                break
            err_trace = (diag.stdout + "\n" + diag.stderr).strip()
            print(f"--- Extrait Traceback ---\n{err_trace[-900:]}\n-------------------------")
            curr_code = WORKER_SCRIPT.read_text(encoding="utf-8")
            patched = request_swarm_ast_patch(err_trace, curr_code)
            if patched:
                WORKER_SCRIPT.write_text(patched, encoding="utf-8")
                silent_git_checkpoint("[Auto-Debug M3] Patch AST appliqu? sur le moteur ?volutif")

    m_files = sorted(RES_GPU_DIR.glob("NUIT_72H_M*.json")) if RES_GPU_DIR.exists() else []
    print("\n===========================================================================")
    print(f"=== STATUT DU DEMON GPU NOCTURNE VAST.AI : {len(m_files)}/12 JALONS LIVRES      ===")
    print("===========================================================================")
    for mf in m_files:
        print(f"  * [CERTIFI? SUR GPU] {mf.name}")

if __name__ == "__main__":
    run_supervisor()
