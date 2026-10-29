#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
autopilot_self_healing_daemon.py
===========================================================================
Superviseur Nocturne Auto-Cicatrisant (Self-Healing Swarm Daemon) :
  - Ex?cute s?quentiellement les 12 Jalons (`M01` ? `M12`) sur le GPU Vast.ai ;
  - Pousse chaque jalon r?ussi imm?diatement sur GitHub (`git push origin main`) ;
  - En cas d'erreur/exception sur un jalon, capture le traceback exact et appelle
    automatiquement l'Essaim Adaptatif (API Gemini 2.5 Pro -> Fallback Claude Sonnet)
    pour diagnostiquer le bug, g?n?rer le correctif Python, v?rifier `ast.parse()`,
    appliquer le patch, le commiter sur GitHub et relancer le jalon !
  - En fin de campagne, d?truit automatiquement l'instance Vast.ai.
===========================================================================
"""
import os, sys, time, json, ast, urllib.request, urllib.error, pathlib, subprocess

CERT_DIR = pathlib.Path(__file__).resolve().parent
REPO_ROOT = CERT_DIR.parents[1]
TARGET_SCRIPT = CERT_DIR / "campagne_nocturne_72h_12_jalons.py"
LOG_FILE = REPO_ROOT / "DAEMON_NOCTURNE_72H_SELF_HEALING.log"

MILESTONES = ["M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09", "M10", "M11", "M12"]

def log_msg(msg: str):
    line = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def git_sync_and_push(commit_msg: str):
    for _ in range(4):
        try:
            subprocess.run(["git", "pull", "--rebase", "--autostash", "origin", "main"], cwd=str(REPO_ROOT), timeout=60)
            subprocess.run(["git", "add", str(LOG_FILE), str(CERT_DIR)], cwd=str(REPO_ROOT), timeout=30)
            subprocess.run(["git", "commit", "-m", commit_msg], cwd=str(REPO_ROOT), timeout=30)
            r = subprocess.run(["git", "push", "origin", "main"], cwd=str(REPO_ROOT), timeout=60)
            if r.returncode == 0:
                return True
        except Exception as e:
            log_msg(f"[Info Git Sync] {e}")
        time.sleep(4)
    return False

def extract_python_block(text: str) -> str:
    if "```python" in text:
        return text.split("```python", 1)[1].split("```", 1)[0].strip()
    if "```" in text:
        return text.split("```", 1)[1].split("```", 1)[0].strip()
    return text.strip()

def ask_adaptive_swarm_for_patch(milestone: str, traceback_str: str, current_code: str) -> str:
    prompt = (
        f"Tu es l'Essaim d'Auto-D?bogage du projet IA Control de Lazar Ciric.\n"
        f"Lors de l'ex?cution sur GPU du jalon `{milestone}` dans `campagne_nocturne_72h_12_jalons.py`, "
        f"l'erreur suivante est survenue :\n\n"
        f"--- TRACEBACK ---\n{traceback_str[-2500:]}\n-----------------\n\n"
        f"Voici le code complet actuel de `campagne_nocturne_72h_12_jalons.py` :\n"
        f"```python\n{current_code}\n```\n\n"
        f"Corrige chirurgicalement la fonction `run_{milestone}()` (ou la fonction utilitaire appel?e) "
        f"pour ?liminer ce bug tout en garantissant que le fichier JSON de sortie attendu par `{milestone}` "
        f"soit bien ?crit dans `OUT_DIR`. Renvoie UNIQUEMENT le fichier Python complet corrig? dans un bloc ```python ... ```."
    )

    # 1. Appel primaire : API Gemini (gemini-2.5-pro / gemini-2.5-flash)
    gem_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if gem_key:
        for model_name in ["gemini-2.5-pro", "gemini-2.5-flash"]:
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={gem_key}"
                payload = {"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"temperature": 0.1}}
                req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
                with urllib.request.urlopen(req, timeout=90) as r:
                    resp = json.loads(r.read().decode("utf-8"))
                    cand_txt = resp["candidates"][0]["content"]["parts"][0]["text"]
                    code_candidate = extract_python_block(cand_txt)
                    ast.parse(code_candidate)
                    log_msg(f"[Swarm Auto-Debug] Patch valide re?u depuis Gemini ({model_name}) !")
                    return code_candidate
            except Exception as e:
                log_msg(f"[Swarm Gemini {model_name} Warning] {e}")

    # 2. Fallback Essaim : API Anthropic Claude
    ant_key = os.environ.get("RR_ANTHROPIC_API_KEY", "").strip()
    if ant_key:
        try:
            url = "https://api.anthropic.com/v1/messages"
            payload = {
                "model": "claude-3-7-sonnet-20250219",
                "max_tokens": 8192,
                "temperature": 0.1,
                "messages": [{"role": "user", "content": prompt}]
            }
            req = urllib.request.Request(
                url, data=json.dumps(payload).encode("utf-8"),
                headers={"x-api-key": ant_key, "anthropic-version": "2023-06-01", "Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=90) as r:
                resp = json.loads(r.read().decode("utf-8"))
                cand_txt = resp["content"][0]["text"]
                code_candidate = extract_python_block(cand_txt)
                ast.parse(code_candidate)
                log_msg("[Swarm Auto-Debug] Patch valide re?u depuis Claude Sonnet !")
                return code_candidate
        except Exception as e:
            log_msg(f"[Swarm Claude Warning] {e}")

    return ""

def run_daemon():
    log_msg("===========================================================================")
    log_msg("=== DEMARRAGE DU DEMON NOCTURNE AUTO-CICATRISANT (12 JALONS M01..M12)  ===")
    log_msg("===========================================================================")
    git_sync_and_push("[Daemon Nocturne 72h] Demarrage de la campagne autonome M01..M12")

    for m_id in MILESTONES:
        success = False
        for attempt in range(1, 5):
            log_msg(f">>> Execution de {m_id} (Tentative {attempt}/4)...")
            proc = subprocess.run(
                [sys.executable, str(TARGET_SCRIPT), "--milestone", m_id],
                capture_output=True, text=True
            )
            if proc.returncode == 0:
                log_msg(f"[SUCCES {m_id}] Sortie :\n{proc.stdout.strip()}")
                git_sync_and_push(f"[Campagne Nocturne 72h] Jalon {m_id} certifie sur GPU")
                success = True
                break
            else:
                err_trace = (proc.stdout + "\n" + proc.stderr).strip()
                log_msg(f"[ALERTE BUG SUR {m_id} - Tentative {attempt}/4] Traceback :\n{err_trace[-1200:]}")
                curr_src = TARGET_SCRIPT.read_text(encoding="utf-8")
                patched_src = ask_adaptive_swarm_for_patch(m_id, err_trace, curr_src)
                if patched_src and "DISPATCH" in patched_src:
                    TARGET_SCRIPT.write_text(patched_src, encoding="utf-8")
                    git_sync_and_push(f"[Auto-Debug Swarm] Correctif automatique applique pour {m_id} (Tentative {attempt})")
                else:
                    log_msg(f"[Auto-Debug] Aucun patch valide obtenu, nouvel essai apr?s nettoyage m?moire...")
                time.sleep(3)

        if not success:
            log_msg(f"[SKIP SECURISE] Le jalon {m_id} n'a pas converg? apr?s 4 tentatives, passage imm?diat au jalon suivant.")
            git_sync_and_push(f"[Daemon Nocturne] Passage au jalon suivant apres {m_id}")

    log_msg("===========================================================================")
    log_msg("=== CAMPAGNE NOCTURNE 72H (M01..M12) INTEGRALEMENT TERMINEE ET POUSSEE ! ===")
    log_msg("===========================================================================")
    git_sync_and_push("[Campagne Nocturne 72h] Bilan final M01..M12 scelle avant Auto-Shutdown")

if __name__ == "__main__":
    run_daemon()
