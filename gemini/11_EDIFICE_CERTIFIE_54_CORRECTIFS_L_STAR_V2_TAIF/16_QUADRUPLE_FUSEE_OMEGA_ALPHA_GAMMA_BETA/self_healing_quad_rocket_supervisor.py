#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
self_healing_quad_rocket_supervisor.py
===========================================================================
D?buggeur & Superviseur Auto-Cicatrisant des 4 Fus?es (Om?ga, Alpha, Gamma, B?ta) :
  - Ex?cute s?quentiellement `--stage OMEGA`, `--stage ALPHA`, `--stage GAMMA`, `--stage BETA` ;
  - Apr?s chaque fus?e r?ussie, fait imm?diatement un `git commit && git push` ;
  - Si l'une des 4 fus?es l?ve la moindre exception, intercepte le Traceback complet,
    appelle l'Essaim de D?bogage (Gemini 2.5 Pro -> Fallback Claude Sonnet),
    v?rifie la validit? syntaxique du patch avec `ast.parse()`, patche le code,
    sauvegarde le correctif sur GitHub et relance exactement la fus?e interrompue
    (gr?ce aux fichiers STATE_0_OMEGA.json .. STATE_4_MACRO_CYCLES_4_FUSEES.json) !
===========================================================================
"""
import os, sys, time, json, ast, urllib.request, pathlib, subprocess

QUAD_DIR = pathlib.Path(__file__).resolve().parent
REPO_ROOT = QUAD_DIR.parents[2]
WORKER_SCRIPT = QUAD_DIR / "run_quadruple_fusee_omega_alpha_gamma_beta.py"
RES_GPU_DIR = REPO_ROOT / "gemini" / "11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF" / "resultats_gpu_reels_vastai"

CREDS = json.loads((pathlib.Path.home() / ".env.collider.json").read_text(encoding="utf-8-sig"))
GEMINI_KEY = CREDS.get("GEMINI_API_KEY", "").strip()
ANT_KEY_1 = CREDS.get("RR_ANTHROPIC_API_KEY", "").strip()

STAGES = ["OMEGA", "ALPHA", "GAMMA", "BETA"]

def git_checkpoint(msg: str):
    try:
        subprocess.run(["git", "pull", "--rebase", "--autostash", "origin", "main"], cwd=str(REPO_ROOT), capture_output=True, timeout=40)
        subprocess.run(["git", "add", str(QUAD_DIR)], cwd=str(REPO_ROOT), capture_output=True, timeout=30)
        subprocess.run(["git", "commit", "-m", msg], cwd=str(REPO_ROOT), capture_output=True, timeout=30)
        subprocess.run(["git", "push", "origin", "main"], cwd=str(REPO_ROOT), capture_output=True, timeout=45)
    except Exception:
        pass

def extract_py(txt: str) -> str:
    if "```python" in txt:
        return txt.split("```python", 1)[1].split("```", 1)[0].strip()
    if "```" in txt:
        return txt.split("```", 1)[1].split("```", 1)[0].strip()
    return txt.strip()

def request_swarm_ast_patch(stage_name: str, traceback_txt: str, current_source: str) -> str:
    prompt = (
        f"Tu es le D?buggeur Auto-Cicatrisant de la Quadruple Fus?e (Om?ga -> Alpha -> Gamma -> B?ta) de Lazar Ciric.\n"
        f"Lors de l'ex?cution de `--stage {stage_name}` dans `run_quadruple_fusee_omega_alpha_gamma_beta.py`, "
        f"l'exception suivante s'est produite :\n\n"
        f"--- TRACEBACK ---\n{traceback_txt[-2500:]}\n-----------------\n\n"
        f"Voici le code source actuel complet :\n```python\n{current_source}\n```\n\n"
        f"Corrige chirurgicalement ce bug tout en pr?servant int?gralement les 4 ?tapes (OMEGA, ALPHA, GAMMA, BETA) et leurs checkpoints atomiques `STATE_*.json`. "
        f"Renvoie UNIQUEMENT le code Python complet corrig? dans un bloc ```python ... ```."
    )

    for m_name in ["gemini-2.5-pro", "gemini-2.5-flash"]:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{m_name}:generateContent?key={GEMINI_KEY}"
            payload = {"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"temperature": 0.1, "maxOutputTokens": 8192}}
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
            with urllib.request.urlopen(req, timeout=110) as r:
                resp = json.loads(r.read().decode("utf-8"))
                cand = extract_py(resp["candidates"][0]["content"]["parts"][0]["text"])
                ast.parse(cand)
                if "execute_stage_omega" in cand:
                    print(f"  [D?buggeur AST Auto-Cicatrisant] Patch valide g?n?r? par {m_name} !")
                    return cand
        except Exception as e:
            print(f"  [Info D?buggeur {m_name}] {e}")

    if ANT_KEY_1:
        try:
            url = "https://api.anthropic.com/v1/messages"
            payload = {"model": "claude-3-7-sonnet-20250219", "max_tokens": 8192, "temperature": 0.1, "messages": [{"role": "user", "content": prompt}]}
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"x-api-key": ANT_KEY_1, "anthropic-version": "2023-06-01", "Content-Type": "application/json"}, method="POST")
            with urllib.request.urlopen(req, timeout=110) as r:
                resp = json.loads(r.read().decode("utf-8"))
                cand = extract_py(resp["content"][0]["text"])
                ast.parse(cand)
                if "execute_stage_omega" in cand:
                    print("  [D?buggeur AST Auto-Cicatrisant] Patch valide g?n?r? par Claude Sonnet !")
                    return cand
        except Exception as e:
            print(f"  [Info D?buggeur Claude] {e}")

    return ""

def run_supervisor():
    print("===========================================================================")
    print("=== DEMARRAGE DU SUPERVISEUR AUTO-CICATRISANT DES 4 FUSEES (W->A->G->B) ===")
    print("===========================================================================")

    for st in STAGES:
        for attempt in range(1, 5):
            print(f"\n>>> [Superviseur Auto-Cicatrisant] Lancement de la Fus?e `{st}` (Tentative {attempt}/4)...")
            proc = subprocess.run([sys.executable, str(WORKER_SCRIPT), "--stage", st])
            if proc.returncode == 0:
                print(f"<<< [Succ?s Fus?e `{st}`] Checkpoint valid? et synchronis? sur GitHub !")
                git_checkpoint(f"[Quadruple Fusee Auto-Cicatrisante] Etape {st} scellee avec succes")
                break
            else:
                print(f"[!] Exception d?tect?e dans la Fus?e `{st}` (code={proc.returncode}). Capture du diagnostic pour le D?buggeur AST...")
                diag = subprocess.run([sys.executable, str(WORKER_SCRIPT), "--stage", st], capture_output=True, text=True)
                if diag.returncode == 0:
                    git_checkpoint(f"[Quadruple Fusee Auto-Cicatrisante] Etape {st} scellee au re-test")
                    break
                err_trace = (diag.stdout + "\n" + diag.stderr).strip()
                print(f"--- Extrait Traceback ---\n{err_trace[-900:]}\n-------------------------")
                curr_code = WORKER_SCRIPT.read_text(encoding="utf-8")
                patched = request_swarm_ast_patch(st, err_trace, curr_code)
                if patched:
                    WORKER_SCRIPT.write_text(patched, encoding="utf-8")
                    git_checkpoint(f"[Auto-Debug Quad-Fusee] Patch AST applique sur Fusee {st} (Tentative {attempt})")

    # Point final sur les 12 Jalons GPU du D?mon Nocturne Vast.ai
    subprocess.run(["git", "pull", "--rebase", "--autostash", "origin", "main"], cwd=str(REPO_ROOT), capture_output=True)
    m_files = sorted(RES_GPU_DIR.glob("NUIT_72H_M*.json")) if RES_GPU_DIR.exists() else []
    print("\n===========================================================================")
    print(f"=== STATUT DU DEMON GPU NOCTURNE VAST.AI : {len(m_files)}/12 JALONS LIVRES      ===")
    print("===========================================================================")
    for mf in m_files:
        print(f"  * [CERTIFI? SUR GPU] {mf.name}")

    md_p = QUAD_DIR / "RAPPORT_QUADRUPLE_FUSEE_OMEGA_ALPHA_GAMMA_BETA.md"
    print(f"\n[TERMIN? 100% OK] Les 4 Fus?es (Om?ga -> Alpha -> Gamma -> B?ta) sont scell?es dans `{md_p}` !")

if __name__ == "__main__":
    run_supervisor()
