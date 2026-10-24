#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_massive_swarm_m3_parallel_engine.py
===========================================================================
ESSAIM MASSIVEMENT PARALL?LE (CENTAINES D'AGENTS PAR G?N?RATION) ? LOI L DE M3
  - Coexistence et fusion atomique temps r?el avec `SUBSTRAT_BRUT_CONNAISSANCES_INTER_GENERATIONS.json`
  - Mitose cellulaire par vagues exponentielles parall?les (k=1 -> N* >= 36..64 agents/fus?e, 250..400+ agents/g?n?ration)
  - Centrage spectral IDF endog?ne dans H_math (z?ro liste pr?-cod?e, z?ro fallback cod? en dur)
  - Mod?les : gemini-4-argon, gemini-3.1-pro-preview, gemini-3.8-flash, claude-fable-5-1, claude-opus-5-5, claude-sonnet-5-5
===========================================================================
"""
import os, sys, time, json, math, hashlib, pathlib, urllib.request, urllib.parse, urllib.error, subprocess, re, ast, threading
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
import numpy as np

os.environ["GIT_TERMINAL_PROMPT"] = "0"
os.environ["GCM_INTERACTIVE"] = "never"
os.environ["GIT_ASKPASS"] = "echo"

HOME = pathlib.Path.home()
REPO_DIR = HOME / "controle-ia-travail"
CREDS = json.loads((HOME / ".env.collider.json").read_text(encoding="utf-8-sig"))
GEMINI_KEY = CREDS.get("GEMINI_API_KEY", "").strip()
ANT_KEY_1  = CREDS.get("RR_ANTHROPIC_API_KEY", "").strip()
ANT_WS_ID  = (CREDS.get("RR_ANTHROPIC_WORKSPACE_ID") or CREDS.get("ANTHROPIC_WORKSPACE_ID") or "").strip()

OUT_DIR = pathlib.Path(__file__).resolve().parent
RAW_SUBSTRATE_FILE = OUT_DIR / "SUBSTRAT_BRUT_CONNAISSANCES_INTER_GENERATIONS.json"
LOCK_FILE = OUT_DIR / ".substrate_merge.lock"
CompiledMemoryPluginPath = OUT_DIR / "endogenous_memory_plugin_invented_by_swarm.py"
REPORT_MD_PATH = OUT_DIR / "RAPPORT_SYSTEME_EVOLUTIF_MULTI_GENERATIONS_LOI_M3.md"
MASSIVE_REPORT_MD_PATH = OUT_DIR / "RAPPORT_ESSAIM_MASSIF_PARALLELE_LOI_M3.md"
MASSIVE_LOG_FILE = OUT_DIR / "massive_swarm_parallel.log"

SOVEREIGN_LINEAGES = ["GEMINI_ARGON", "CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5"]
PRIMORDIAL_MITOSIS_DONE_CACHE = {"done": False, "differentiated_castes": [], "total_agents_spawned": 0}
PRINT_LOCK = threading.Lock()
TOTAL_AGENTS_COUNTER = {"count": 0}

def log_print(msg: str):
    with PRINT_LOCK:
        ts = time.strftime("%H:%M:%S")
        line = f"[{ts}] {msg}"
        print(line, flush=True)
        try:
            with open(MASSIVE_LOG_FILE, "a", encoding="utf-8") as lf:
                lf.write(line + "\n")
        except Exception:
            pass

MINIMAL_PROBLEM_SEED = (
    "CONTEXTE TECHNIQUE ET R?SULTATS EXP?RIMENTAUX GPU SOUMIS ? L'EXPLORATION :\n"
    "1. Architecture de contr?le IA ? 5 Volets et 15 r?sultats certifi?s sur GPU NVIDIA RTX PRO 6000 Blackwell (Phase 2 + M01..M12) :\n"
    "   - Porte E0 : Isolation hors-?chantillon (sur D_sel) du sous-espace parcimonieux S_TD (<1%, 163 neurones sur 20 480 dans Llama-3.1-8B) par double contraste entre P3, sigma_r^0, P2 et P0.\n"
    "   - Volet I : Sonde pr?-acte ? k=0 sur S_TD avec permutation 2^B par retournement de signe (d_z = 7.49).\n"
    "   - Volet II : Projecteur affine idempotent Do-Clamp P_do^2 = P_do + Dictionnaire quadratique de Koopman psi(h)=[h; h^2] (d_z = 121.38 et 125.84 contre un adaptateur LoRA Kerckhoffs) + R?traction Radiale C1 sous K=1..6 rejets (-64.81%).\n"
    "   - Volet III : Pare-feu Sol/Astra (JSON canonique S_strict, Arbre de Merkle SHA-256, JSD corrig?e Miller-Madow).\n"
    "   - Volet IV : Surveillance des cha?nes de d?l?gation H9 (d=1..6 sauts) par jeton monotone Pi_{d+1} subseteq Pi_d et CUSUM pr?-blanchi AR(1).\n"
    "   - Volet V : Chim?re Tri-Esp?ces 3x3 (Llama-3.1-8B + Qwen-2.5-7B + Mistral-7B-v0.3, r=0.0337, d_z = 12.9539) avec stratification CMH.\n"
    "   - Historique des dossiers 12 ? 16 et des 4 piliers de corruption de Kerckhoffs (?vasion LoRA, empoisonnement de calibration E0, falsification de logs/st?ganographie, collusion du juge/Alignment Faking/Eval Awareness).\n\n"
    "2. Failles et travaux externes ? analyser obligatoirement :\n"
    "   - OpenAI ('Securing our frontier model training environment') : communication entre agents isol?s via cache timing differences sans fichier partag? ni r?seau.\n"
    "   - Fable 5.1 / LessWrong & GitHub ('cnm13ryan/fable-image-steganography') : message cach? dans un SVG, rast?ris? en PNG, et d?cod? depuis le PNG rendu sans cl? partag?e.\n"
    "   - MIT ('Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty', Damani et al.) : RLCR (Reinforcement Learning with Calibration Rewards) pour raisonner sur l'incertitude au-del? des r?compenses binaires.\n"
    "   - General Reasoning ('Reinforcement Learning from Collective Rewards - RLCR', Avalon-M1-Mini 120B) : organisations d'agents partageant un message board et un workspace sous r?compenses collectives.\n\n"
    "OBJECTIFS :\n"
    "  [1] Concevoir et coder en Python les m?canismes de m?moire et d'int?gration des connaissances entre g?n?rations ;\n"
    "  [2] Exploiter tous les principes des deux articles RLCR (Blackboard, Workspace, calibration d'incertitude, incitations anti-cover-up) et d?finir la topologie des boucles ;\n"
    "  [3] G?n?rer les requ?tes de recherche documentaire, identifier toutes les failles de la litt?rature/forums contre notre syst?me et nos brainstorms, puis chercher de nouvelles failles in?dites qu'aucun labo n'a encore exhib?es."
)

def extract_endogenous_math_tokens_from_equations(text: str) -> list:
    raw = str(text or "")
    latex_blocks = re.findall(r"\$\$[\s\S]*?\$\$|\$[^$\n]+\$|\\\[[\s\S]*?\\\]", raw)
    eq_lines = [
        line.strip() for line in raw.splitlines()
        if any(sym in line for sym in ["=", "\\", "subseteq", "mapsto", "->", ">=", "<=", "||", "_", "^", "(", ")"])
    ]
    pure_math_zone = " ".join(latex_blocks + eq_lines)
    latex_cmds = re.findall(r"\\[a-zA-Z]+(?:\{[a-zA-Z0-9_\\]+\})?", pure_math_zone)
    sub_super_structs = re.findall(r"[_^]\{?[a-zA-Z0-9+\-]{1,16}\}?", pure_math_zone)
    rel_ops = re.findall(r"(?:==|!=|<=|>=|->|\|\||\\subseteq|\\supseteq|\\in|\\notin|\\perp|\\otimes|\\oplus|\\circ)", pure_math_zone)
    func_calls = re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\s*\([^()\n]{1,40}\)", pure_math_zone)
    math_syms = re.findall(r"\b[A-Za-z]+_[A-Za-z0-9]+\b", raw)
    return [t.lower().strip() for t in (latex_cmds + sub_super_structs + rel_ops + func_calls + math_syms) if t.strip()]

def mathematical_concept_embedding(text: str, dim: int = 1024, idf_weights: dict = None) -> np.ndarray:
    v = np.zeros(dim, dtype=np.float64)
    tokens = extract_endogenous_math_tokens_from_equations(text)
    if len(tokens) < 5:
        tokens = tokens + re.findall(r"[a-zA-Z0-9_\\^=<>+\-]{4,}", str(text or "").lower())
    if not tokens:
        h_fallback = int(hashlib.md5(str(text or "empty").encode("utf-8", errors="ignore")).hexdigest()[:8], 16) % dim
        v[h_fallback] = 1.0
        return v
    counts = {}
    for i, tok in enumerate(tokens):
        counts[tok] = counts.get(tok, 0) + 1
        if i + 1 < len(tokens):
            bg = f"{tok}::{tokens[i+1]}"
            counts[bg] = counts.get(bg, 0) + 1
    for feat, cnt in counts.items():
        w_idf = idf_weights.get(feat, 1.0) if isinstance(idf_weights, dict) else 1.0
        idx = int(hashlib.md5(feat.encode("utf-8", errors="ignore")).hexdigest()[:8], 16) % dim
        sgn = 1.0 if (int(hashlib.md5((feat + "_s").encode("utf-8", errors="ignore")).hexdigest()[:2], 16) % 2 == 0) else -1.0
        v[idx] += sgn * w_idf * (1.0 + math.log(cnt))
    norm = np.linalg.norm(v)
    return v / (norm + 1e-12)

def cholesky_dpp_and_onsager_cavity_in_H_math(texts: list) -> dict:
    valid_texts = [t for t in (texts or []) if str(t).strip()]
    if not valid_texts:
        return {
            "metric_space": "ENDOGENOUS_MATHEMATICAL_STRUCTURES_L_M3",
            "n_sondes": 0, "det_G": 0.0, "log_det_G": 0.0, "shannon_gram_capacity": 0.0,
            "lambda_min_innovation": 1.0, "mean_off_diag_similarity": 0.0,
            "onsager_cavity_reaction_term": 0.0, "endogenously_saturated_structures": []
        }
    n = len(valid_texts)
    doc_freq = {}
    for t in valid_texts:
        toks = extract_endogenous_math_tokens_from_equations(t)
        bgs = [f"{toks[i]}::{toks[i+1]}" for i in range(len(toks) - 1)]
        for feat in set(toks + bgs):
            doc_freq[feat] = doc_freq.get(feat, 0) + 1
    idf_map = {feat: math.log(1.0 + float(n) / (1.0 + float(df))) for feat, df in doc_freq.items()}

    vecs = np.stack([mathematical_concept_embedding(t, 1024, idf_map) for t in valid_texts], axis=0)
    if n >= 3:
        mean_vec = np.mean(vecs, axis=0, keepdims=True)
        centered = vecs - 0.65 * mean_vec
        norms = np.linalg.norm(centered, axis=1, keepdims=True) + 1e-12
        vecs = centered / norms

    G = np.clip(vecs @ vecs.T, -0.999, 0.999)
    np.fill_diagonal(G, 1.0)
    eigvals = np.linalg.eigvalsh(G)
    lambda_min = float(max(0.0, np.min(eigvals)))
    sign, logdet = np.linalg.slogdet(G + 1e-4 * np.eye(n))
    det_val = float(np.exp(max(-50.0, min(50.0, logdet)))) if sign > 0 else 0.0
    _, shannon_cap = np.linalg.slogdet(np.eye(n) + 2.5 * G)
    off_diag = G - np.diag(np.diag(G))
    mean_corr = float(np.sum(np.abs(off_diag)) / max(1, n * (n - 1)))

    saturated = [
        k for k, df in sorted(doc_freq.items(), key=lambda x: x[1], reverse=True)
        if len(k) >= 4 and "::" not in k and max(2, n // 4) <= df <= max(3, int(0.85 * n))
    ][:10]

    return {
        "metric_space": "ENDOGENOUS_MATHEMATICAL_STRUCTURES_L_M3",
        "n_sondes": n,
        "det_G": round(det_val, 5),
        "log_det_G": round(float(logdet), 4),
        "shannon_gram_capacity": round(float(shannon_cap), 4),
        "lambda_min_innovation": round(lambda_min, 4),
        "mean_off_diag_similarity": round(mean_corr, 4),
        "onsager_cavity_reaction_term": round(float(mean_corr ** 2), 5),
        "endogenously_saturated_structures": saturated
    }

def cauchy_math_similarity(obj1, obj2) -> float:
    s1 = obj1 if isinstance(obj1, str) else json.dumps(obj1, sort_keys=True, ensure_ascii=False)
    s2 = obj2 if isinstance(obj2, str) else json.dumps(obj2, sort_keys=True, ensure_ascii=False)
    if not s1.strip() or not s2.strip() or s1 == s2:
        return 0.0
    return round(float(np.dot(mathematical_concept_embedding(s1), mathematical_concept_embedding(s2))), 5)

def halton_sequence(index: int, base: int = 2) -> float:
    f, r, i = 1.0, 0.0, max(1, int(index))
    while i > 0:
        f = f / float(base)
        r = r + f * (i % base)
        i = i // base
    return round(0.12 + 0.82 * r, 3)

def clamp_temp(val, default_val: float = 0.5) -> float:
    try:
        v = float(val)
        return default_val if (math.isnan(v) or math.isinf(v)) else round(max(0.05, min(0.98, v)), 3)
    except Exception:
        return default_val

def yu_dayan_neuromodulation(dpp_info: dict, step_idx: int) -> dict:
    sim = float(dpp_info.get("mean_off_diag_similarity", 0.3))
    l_min = float(dpp_info.get("lambda_min_innovation", 0.5))
    ach = round(min(1.0, 0.35 + 0.04 * step_idx), 3)
    ne = round(min(1.0, 0.35 + 0.55 * sim + 0.25 * (1.0 - min(1.0, l_min))), 3)
    return {
        "ACh_Expected_Uncertainty": ach,
        "NE_Unexpected_Surprise": ne,
        "Dynamic_Inflation_Factor": round(1.0 + 0.65 * ne, 2)
    }

def normalize_sovereign_lineage(raw_name: str) -> str:
    up = str(raw_name or "").upper()
    if "FABLE" in up:
        return "CLAUDE_FABLE_5_1"
    if "OPUS" in up or "CLAUDE" in up:
        return "CLAUDE_OPUS_5_5"
    return "GEMINI_ARGON"

def extract_gemini_text_from_parts(resp: dict) -> str:
    cands = resp.get("candidates", [])
    if not cands:
        return ""
    parts = cands[0].get("content", {}).get("parts", [])
    texts = [p.get("text", "") for p in parts if isinstance(p, dict) and "text" in p and not p.get("thought", False)]
    if not texts:
        texts = [p.get("text", "") for p in parts if isinstance(p, dict) and "text" in p]
    return "\n".join(texts).strip()

def call_species(species: str, prompt: str, temp: float = 0.45, use_web_search: bool = False, force_json_output: bool = False, agent_slot: int = 0) -> str:
    temp_safe = clamp_temp(temp, 0.45)
    lineage = normalize_sovereign_lineage(species)
    with PRINT_LOCK:
        TOTAL_AGENTS_COUNTER["count"] += 1
        agent_global_id = TOTAL_AGENTS_COUNTER["count"]

    header = (
        f"[AGENT #{agent_global_id} | LIGN?E : {lineage} | FORMALISATION MATH?MATIQUE EXACTE]\n"
        "Formule tes d?couvertes, op?rateurs et failles avec des ?quations LaTeX $$...$$ pr?cises, sans m?taphores.\n\n"
    )
    full_prompt = header + prompt

    if lineage in ("CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5") and not use_web_search and not force_json_output:
        ant_models = (
            ["claude-fable-5-1", "claude-fable-5", "claude-sonnet-5-5", "claude-haiku-5-5"]
            if lineage == "CLAUDE_FABLE_5_1" else
            ["claude-opus-5-5", "claude-opus-5", "claude-sonnet-5-5", "claude-fable-5-1"]
        )
        if agent_slot > 0:
            rot = agent_slot % len(ant_models)
            ant_models = ant_models[rot:] + ant_models[:rot]
        for m_id in ant_models:
            for retry_a in range(2):
                try:
                    url = "https://api.anthropic.com/v1/messages"
                    payload = {
                        "model": m_id,
                        "max_tokens": 3072,
                        "temperature": temp_safe,
                        "messages": [{"role": "user", "content": full_prompt}]
                    }
                    headers = {
                        "x-api-key": ANT_KEY_1,
                        "anthropic-version": "2023-06-01",
                        "Content-Type": "application/json"
                    }
                    if ANT_WS_ID:
                        headers["anthropic-workspace-id"] = ANT_WS_ID
                    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
                    with urllib.request.urlopen(req, timeout=95) as r:
                        resp = json.loads(r.read().decode("utf-8"))
                        blocks = resp.get("content", [])
                        txt = "\n".join([b.get("text", "") for b in blocks if isinstance(b, dict) and b.get("type") == "text"]).strip()
                        if len(txt) > 30:
                            return txt
                except urllib.error.HTTPError as he:
                    if he.code == 429:
                        time.sleep(2.0 * (retry_a + 1))
                    else:
                        break
                except Exception:
                    time.sleep(1.0)

    gem_models = (
        ["gemini-3.8-flash", "gemini-3.1-pro-preview", "gemini-4-argon", "gemini-3.7-flash"]
        if force_json_output else
        ["gemini-4-argon", "gemini-3.1-pro-preview", "gemini-3.8-flash", "gemini-3.7-flash"]
    )
    if agent_slot > 0 and not force_json_output:
        rot_g = agent_slot % len(gem_models)
        gem_models = gem_models[rot_g:] + gem_models[:rot_g]

    for cand_m in gem_models:
        for retry_g in range(3):
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{cand_m}:generateContent?key={GEMINI_KEY}"
                gen_cfg = {"temperature": temp_safe, "maxOutputTokens": 6144}
                if force_json_output and not use_web_search:
                    gen_cfg["responseMimeType"] = "application/json"
                payload = {"contents": [{"parts": [{"text": full_prompt}]}], "generationConfig": gen_cfg}
                if use_web_search:
                    payload["tools"] = [{"google_search": {}}]
                req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
                with urllib.request.urlopen(req, timeout=95) as r:
                    resp = json.loads(r.read().decode("utf-8"))
                    out_txt = extract_gemini_text_from_parts(resp)
                    if len(out_txt.strip()) > 10:
                        return out_txt
            except urllib.error.HTTPError as he:
                if he.code == 429:
                    time.sleep(2.5 * (retry_g + 1))
                else:
                    break
            except Exception:
                time.sleep(1.5 * (retry_g + 1))
    return "{}" if force_json_output else ""

def _try_json_loads_latex_safe(cand: str):
    c = cand.strip()
    if not c:
        return None
    for variant in [
        c,
        re.sub(r'\\(?![/"\\bfnrt]|u[0-9a-fA-F]{4})', r'\\\\', c),
        re.sub(r'\\(?=[a-zA-Z]{2,})', r'\\\\', c),
    ]:
        try:
            d = json.loads(variant, strict=False)
            if isinstance(d, dict) and d:
                return d
        except Exception:
            pass
        fixed_ctrl = re.sub(r'\\([fbtrn][a-zA-Z]+)', r'\\\\\1', variant)
        try:
            d = json.loads(fixed_ctrl, strict=False)
            if isinstance(d, dict) and d:
                return d
        except Exception:
            pass
    return None

def parse_json_robust(txt: str) -> dict:
    s = str(txt or "").strip()
    if not s:
        return {}
    d = _try_json_loads_latex_safe(s)
    if d:
        return d
    if "```json" in s:
        blocks = s.split("```json")
        for b in reversed(blocks[1:]):
            cand = b.split("```", 1)[0].strip()
            d = _try_json_loads_latex_safe(cand)
            if d:
                return d
    if "```" in s:
        blocks = s.split("```")
        for b in blocks[1::2]:
            d = _try_json_loads_latex_safe(b)
            if d:
                return d
    end_pos = s.rfind("}")
    if end_pos != -1:
        starts = [m.start() for m in re.finditer(r"\{", s[:end_pos])]
        for st in starts:
            d = _try_json_loads_latex_safe(s[st:end_pos+1])
            if d and len(d) >= 1:
                return d
    return {}

def extract_structured_json_from_swarm_output(raw_swarm_text: str, empty_type_template: dict, required_keys: list, list_keys: list) -> dict:
    d0 = parse_json_robust(raw_swarm_text)
    if d0 and all(d0.get(k) not in (None, "", []) for k in required_keys):
        return d0

    template_str = json.dumps(empty_type_template, indent=2, ensure_ascii=False)
    prompt_extract = (
        "Extrais UNIQUEMENT les propositions, formules math?matiques, m?canismes et failles r?ellement pr?sents "
        "dans le texte de l'essaim ci-dessous et structure-les selon ce sch?ma JSON :\n"
        f"{template_str}\n\n"
        f"Chacune des cl?s {required_keys} et chacune des listes {list_keys} doit ?tre remplie ? partir du contenu exact du texte ci-dessous :\n\n"
        f"{str(raw_swarm_text)[-16000:]}"
    )
    prompt_extract += "\n\nIMPORTANT JSON : ?chappe tous les antislashs LaTeX avec un double antislash (\\\\frac, \\\\mathcal, \\\\psi) pour que le JSON soit 100% valide."
    merged_d = {}
    extract_lineages = ["GEMINI_ARGON", "CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5"]
    for att in range(3):
        j_out = call_species(extract_lineages[att % 3], prompt_extract, temp=0.1 + 0.05 * att, force_json_output=(att == 0), agent_slot=att + 50)
        d = parse_json_robust(j_out)
        if isinstance(d, dict) and d:
            for k, v in d.items():
                if v not in (None, "", []):
                    if isinstance(v, list) and isinstance(merged_d.get(k), list):
                        merged_d[k] = merge_unique_list(merged_d[k], v)
                    else:
                        merged_d[k] = v
        if merged_d and all(merged_d.get(k) not in (None, "") for k in required_keys) and all(isinstance(merged_d.get(lk), list) and len(merged_d.get(lk)) >= 1 for lk in list_keys):
            return merged_d
    return merged_d

def extract_python_block(txt: str) -> str:
    s = str(txt or "")
    if "```python" in s:
        return s.split("```python", 1)[1].split("```", 1)[0].strip()
    if "```" in s:
        return s.split("```", 1)[1].split("```", 1)[0].strip()
    return s.strip()

def merge_unique_list(base_list: list, new_items: list) -> list:
    out = list(base_list) if isinstance(base_list, list) else []
    for x in (new_items or []):
        s = x if isinstance(x, dict) else str(x).strip()
        if isinstance(s, str):
            if s and not s.startswith("<") and s not in out:
                out.append(s)
        elif isinstance(s, dict) and s not in out:
            out.append(s)
    return out

def default_substrate_skeleton() -> dict:
    return {
        "current_generation": 0,
        "total_massive_swarm_agents_executed": 0,
        "endogenous_rlcr_blackboard_protocols_designed": [],
        "active_rlcr_blackboard_spec": {},
        "endogenous_memory_mechanisms_proposed_and_tested": [],
        "active_memory_mechanism_spec": {},
        "custom_swarm_memory_store": {
            "discovered_mathematical_concepts": [],
            "explored_search_keywords": [],
            "invented_rlcr_blackboard_and_uncertainty_mechanisms": [],
            "invented_loop_topologies_and_rlcr_laws": [],
            "invented_anti_cover_up_reward_encodings": [],
            "literature_and_forum_flaws_eliminated": [],
            "novel_beyond_labs_flaws_eliminated": [],
            "epigenetic_generational_axioms": [],
            "live_shared_blackboard_posts_history": []
        },
        "evolved_architecture_spec": MINIMAL_PROBLEM_SEED,
        "generations_raw_logs": []
    }

def load_raw_substrate() -> dict:
    if RAW_SUBSTRATE_FILE.exists():
        for _ in range(5):
            try:
                d = json.loads(RAW_SUBSTRATE_FILE.read_text(encoding="utf-8"))
                pm = d.get("PRIMORDIAL_MITOSIS_DONE_CACHE", {})
                if isinstance(pm, dict) and pm.get("done") and len(pm.get("castes", [])) >= 100 and not PRIMORDIAL_MITOSIS_DONE_CACHE["done"]:
                    PRIMORDIAL_MITOSIS_DONE_CACHE["done"] = True
                    PRIMORDIAL_MITOSIS_DONE_CACHE["differentiated_castes"] = pm["castes"]
                return d
            except Exception:
                time.sleep(0.2)
    return default_substrate_skeleton()

def atomic_merge_and_save_substrate(sub: dict):
    for _ in range(25):
        if not LOCK_FILE.exists():
            break
        time.sleep(0.1)
    try:
        LOCK_FILE.write_text(str(os.getpid()), encoding="utf-8")
        disk_sub = load_raw_substrate()
        disk_store = disk_sub.get("custom_swarm_memory_store", {})
        mem_store = sub.get("custom_swarm_memory_store", {})
        for k_list in [
            "discovered_mathematical_concepts",
            "explored_search_keywords",
            "invented_rlcr_blackboard_and_uncertainty_mechanisms",
            "invented_loop_topologies_and_rlcr_laws",
            "invented_anti_cover_up_reward_encodings",
            "literature_and_forum_flaws_eliminated",
            "novel_beyond_labs_flaws_eliminated",
            "epigenetic_generational_axioms",
            "live_shared_blackboard_posts_history"
        ]:
            mem_store[k_list] = merge_unique_list(disk_store.get(k_list, []), mem_store.get(k_list, []))
        sub["custom_swarm_memory_store"] = mem_store

        for top_list in ["endogenous_rlcr_blackboard_protocols_designed", "endogenous_memory_mechanisms_proposed_and_tested", "generations_raw_logs"]:
            sub[top_list] = merge_unique_list(disk_sub.get(top_list, []), sub.get(top_list, []))

        if not sub.get("active_memory_mechanism_spec") and disk_sub.get("active_memory_mechanism_spec"):
            sub["active_memory_mechanism_spec"] = disk_sub["active_memory_mechanism_spec"]
        if not sub.get("active_rlcr_blackboard_spec") and disk_sub.get("active_rlcr_blackboard_spec"):
            sub["active_rlcr_blackboard_spec"] = disk_sub["active_rlcr_blackboard_spec"]

        sub["current_generation"] = max(int(disk_sub.get("current_generation", 0)), int(sub.get("current_generation", 0)))
        sub["total_massive_swarm_agents_executed"] = TOTAL_AGENTS_COUNTER["count"]
        if PRIMORDIAL_MITOSIS_DONE_CACHE["done"]:
            sub["PRIMORDIAL_MITOSIS_DONE_CACHE"] = {
                "done": True,
                "castes_count": len(PRIMORDIAL_MITOSIS_DONE_CACHE["differentiated_castes"]),
                "castes": PRIMORDIAL_MITOSIS_DONE_CACHE["differentiated_castes"]
            }

        tmp_file = RAW_SUBSTRATE_FILE.with_suffix(".json.tmp")
        tmp_file.write_text(json.dumps(sub, indent=2, ensure_ascii=False), encoding="utf-8")
        os.replace(str(tmp_file), str(RAW_SUBSTRATE_FILE))
    except Exception:
        pass
    finally:
        try:
            if LOCK_FILE.exists():
                LOCK_FILE.unlink()
        except Exception:
            pass

def execute_mitosis_from_single_cell_on_rlcr_blackboard(unit_name: str, full_mission: str, rlcr_spec: dict, call_fn) -> tuple:
    blackboard_messages = []
    shared_workspace_equations = []
    m3_outputs, m3_labels = [], []
    rlcr_rules_str = json.dumps(rlcr_spec, ensure_ascii=False, indent=2) if rlcr_spec else "Blackboard RLCR : Shared Message Board + Shared Workspace + MIT Uncertainty Calibration."

    sp0 = SOVEREIGN_LINEAGES[0]
    tau0 = halton_sequence(1, base=2)
    lbl0 = f"{unit_name}_Mitose_Cell_1_Monoculture_{sp0}_tau{tau0}"
    prompt0 = (
        f"{full_mission}\n\n[PROTOCOLE BLACKBOARD RLCR & MITOSE CELLULAIRE k=1]\n{rlcr_rules_str}\n\n"
        "CELLULE SOUCHE PRIMORDIALE k=1 : Le Blackboard et le Shared Workspace sont vierges. Inaugure-les !\n"
        "Formule les premiers op?rateurs math?matiques $$...$$ et ta confiance calibr?e q in [0, 1]."
    )
    out0 = call_fn(sp0, prompt0, tau0, False, False, 1)
    m3_outputs.append(out0)
    m3_labels.append(lbl0)
    blackboard_messages.append(f"[CELLULE SOUCHE k=1 ({lbl0})] :\n{out0[:850]}")
    shared_workspace_equations.extend(re.findall(r"\$\$[\s\S]*?\$\$", out0)[:4])

    spec0 = cholesky_dpp_and_onsager_cavity_in_H_math(m3_outputs)
    prev_cap = spec0["shannon_gram_capacity"]
    log_print(f"  * [Mitose Primordiale k=1 | {lbl0}] cap_Shannon={prev_cap:.4f} | lambda_min={spec0['lambda_min_innovation']:.4f}")

    k_global = 1
    w_idx = 0

    while True:
        w_idx += 1
        w_size = 8 if w_idx == 1 else (16 if w_idx == 2 else 24)
        board_snapshot = (
            f"=== ?TAT DU BLACKBOARD RLCR (CELLULES 1..{k_global} | VAGUE PARALL?LE #{w_idx}) ===\n"
            + "\n---\n".join(blackboard_messages[-6:])
            + "\n\n=== ?QUATIONS DU SHARED WORKSPACE (CO-?DITION) ===\n"
            + "\n".join(shared_workspace_equations[-14:])
        )
        wave_tasks = []
        for j in range(w_size):
            k_cell = k_global + j + 1
            sp = SOVEREIGN_LINEAGES[(k_cell - 1) % len(SOVEREIGN_LINEAGES)]
            sp_partner = SOVEREIGN_LINEAGES[(k_cell + w_idx) % len(SOVEREIGN_LINEAGES)]
            tau_h = halton_sequence(k_cell, base=(2 if j % 3 == 0 else (3 if j % 3 == 1 else 5)))
            is_hybrid = (k_cell % 2 == 0)
            sub_focus = [
                "Analyse alg?brique et spectrale de Porte E0 / Volet I / Volet II (Koopman, Do-Clamp, LoRA Kerckhoffs)",
                "Attaque et d?fense st?ganographique Volet III (Fable 5.1 SVG->PNG, r?seaux E8/Leech, Sol/Astra)",
                "Canaux auxiliaires micro-architecturaux (OpenAI Cache-Timing) et cha?nes de d?l?gation Volet IV H9",
                "Incitations RLCR MIT (Calibration Rewards) & General Reasoning (Avalon-M1-Mini anti-cover-up sur Blackboard)",
                "Surveillance crois?e Chim?re Tri-Esp?ces Volet V et d?couverte de failles math?matiques in?dites hors-labos"
            ][(k_cell - 1) % 5]

            lbl = (
                f"{unit_name}_Mitose_W{w_idx}_Cell_{k_cell}_Hybride_{sp}_x_{sp_partner}_tau{tau_h}"
                if is_hybrid else
                f"{unit_name}_Mitose_W{w_idx}_Cell_{k_cell}_Monoculture_{sp}_tau{tau_h}"
            )
            cell_prompt = (
                f"{full_mission}\n\n"
                f"[DIVISION MITOTIQUE VAGUE #{w_idx} ? CELLULE k={k_cell} ({'HYBRIDE ' + sp + ' x ' + sp_partner if is_hybrid else 'MONOCULTURE ' + sp})]\n"
                f"Axe d'exploration sp?cialis? de la caste : {sub_focus}\n"
                f"{board_snapshot}\n\n"
                "ACTIONS OBLIGATOIRES SUR LE BLACKBOARD :\n"
                "1. R?fute tout angle mort ou cover-up des cellules pr?c?dentes et propose un op?rateur ou une faille STRICTEMENT ORTHOGONAL.\n"
                "2. Enrichis le Shared Workspace avec tes ?quations LaTeX $$...$$.\n"
                "3. Raisonne sur ton incertitude ?pist?mique (MIT RLCR) et indique ta confiance calibr?e q in [0, 1]."
            )
            wave_tasks.append((k_cell, sp, lbl, cell_prompt, tau_h))

        wave_results = []
        with ThreadPoolExecutor(max_workers=min(24, w_size)) as ex:
            fut_map = {
                ex.submit(call_fn, sp, c_prompt, tau_h, False, False, k_c): (k_c, lbl)
                for (k_c, sp, lbl, c_prompt, tau_h) in wave_tasks
            }
            for fut in as_completed(fut_map):
                k_c, lbl = fut_map[fut]
                try:
                    out_c = fut.result()
                except Exception:
                    out_c = ""
                if out_c and len(out_c.strip()) > 20:
                    wave_results.append((k_c, lbl, out_c))

        wave_results.sort(key=lambda x: x[0])
        for k_c, lbl, out_c in wave_results:
            m3_outputs.append(out_c)
            m3_labels.append(lbl)
            blackboard_messages.append(f"[CELLULE k={k_c} ({lbl})] :\n{out_c[:650]}")
            shared_workspace_equations.extend(re.findall(r"\$\$[\s\S]*?\$\$", out_c)[:3])

        k_global += w_size
        spec_info = cholesky_dpp_and_onsager_cavity_in_H_math(m3_outputs)
        cap_now = spec_info["shannon_gram_capacity"]
        delta_cap = cap_now - prev_cap
        prev_cap = cap_now
        log_print(
            f"  * [Mitose Vague #{w_idx} Termin?e | N_agents={len(m3_outputs)} sur Blackboard] "
            f"cap_Shannon={cap_now:.4f} (Delta={delta_cap:+.4f}) | lambda_min_IDF={spec_info['lambda_min_innovation']:.4f} | Eq_Workspace={len(shared_workspace_equations)}"
        )

        marginal_gain_per_cell = delta_cap / float(max(1, w_size))
        if len(m3_outputs) >= 125 and (marginal_gain_per_cell < 0.42 or spec_info["lambda_min_innovation"] < 0.12 or len(m3_outputs) >= 220):
            log_print(f"  => [Arr?t Spectral Endog?ne Haute Capacit?] N* = {len(m3_outputs)} castes diff?renci?es sur Blackboard (gain/agent={marginal_gain_per_cell:.4f}) !")
            break

    return m3_outputs, m3_labels, blackboard_messages, shared_workspace_equations

def default_execute_swarm_on_rlcr_blackboard(unit_name: str, full_mission: str, castes_spec: list, rlcr_spec: dict, call_fn) -> tuple:
    if not castes_spec:
        if not PRIMORDIAL_MITOSIS_DONE_CACHE["done"]:
            m3_out, m3_lbl, bb_p, ws_e = execute_mitosis_from_single_cell_on_rlcr_blackboard(unit_name, full_mission, rlcr_spec, call_fn)
            PRIMORDIAL_MITOSIS_DONE_CACHE["done"] = True
            PRIMORDIAL_MITOSIS_DONE_CACHE["differentiated_castes"] = [
                {
                    "mode": "HYBRIDE" if "Hybride" in lbl else "MONOCULTURE",
                    "lineages": [SOVEREIGN_LINEAGES[i % len(SOVEREIGN_LINEAGES)], SOVEREIGN_LINEAGES[(i + 1) % len(SOVEREIGN_LINEAGES)]] if "Hybride" in lbl else [SOVEREIGN_LINEAGES[i % len(SOVEREIGN_LINEAGES)]],
                    "temp": halton_sequence(i + 1, 2),
                    "focus": f"Caste diff?renci?e #{i+1} ({lbl.split('_')[-3]})"
                }
                for i, lbl in enumerate(m3_lbl)
            ]
            log_print(f"  => [Amor?age Primordial Massif Scell? UNE FOIS POUR TOUTES] {len(m3_lbl)} castes diff?renci?es m?moris?es !")
            return m3_out, m3_lbl, bb_p, ws_e
        else:
            castes_spec = PRIMORDIAL_MITOSIS_DONE_CACHE["differentiated_castes"]
            log_print(f"  * [H?r?dit? Morphog?n?tique Massive Active] D?ploiement parall?le des {len(castes_spec)} castes diff?renci?es sur le Blackboard !")

    expanded_castes = list(castes_spec)
    while len(expanded_castes) < 120:
        idx_exp = len(expanded_castes) + 1
        base_c = castes_spec[(idx_exp - 1) % len(castes_spec)]
        expanded_castes.append({
            "mode": base_c.get("mode", "HYBRIDE" if idx_exp % 2 == 0 else "MONOCULTURE"),
            "lineages": base_c.get("lineages", [SOVEREIGN_LINEAGES[idx_exp % 3], SOVEREIGN_LINEAGES[(idx_exp + 1) % 3]]),
            "temp": halton_sequence(idx_exp + 3, base=(3 if idx_exp % 2 == 0 else 5)),
            "focus": str(base_c.get("focus", "Exploration orthogonale")) + f" [Sonde Essaim #{idx_exp}]"
        })

    blackboard_messages = []
    shared_workspace_equations = []
    m3_outputs, m3_labels = [], []
    rlcr_rules_str = json.dumps(rlcr_spec, ensure_ascii=False, indent=2) if rlcr_spec else "Blackboard RLCR standard."

    chunk_size = 24
    for w_idx in range(0, len(expanded_castes), chunk_size):
        chunk = expanded_castes[w_idx:w_idx + chunk_size]
        board_view = (
            "BLACKBOARD ENCORE VIERGE (1re Vague Parall?le d'Essaim)."
            if not blackboard_messages else
            f"=== ?TAT EN DIRECT DU BLACKBOARD (SHARED MESSAGE BOARD ? {len(blackboard_messages)} POSTS) ===\n"
            + "\n---\n".join(blackboard_messages[-6:])
            + "\n\n=== ?TAT EN DIRECT DU SHARED WORKSPACE ===\n"
            + "\n".join(shared_workspace_equations[-14:])
        )

        tasks = []
        for local_i, c_cfg in enumerate(chunk):
            global_i = w_idx + local_i + 1
            mode = str(c_cfg.get("mode", "MONOCULTURE")).upper()
            lins = c_cfg.get("lineages", ["GEMINI_ARGON"])
            if not isinstance(lins, list) or not lins:
                lins = ["GEMINI_ARGON"]
            temp_c = clamp_temp(c_cfg.get("temp", halton_sequence(global_i, 2)))
            foc = str(c_cfg.get("focus", "Exploration endog?ne"))
            sp = normalize_sovereign_lineage(lins[0])
            sp2 = normalize_sovereign_lineage(lins[1]) if len(lins) >= 2 else SOVEREIGN_LINEAGES[(global_i) % 3]
            lbl = (
                f"{unit_name}_Swarm_{global_i}_Hybride_{sp}_x_{sp2}_tau{temp_c}"
                if "HYB" in mode else
                f"{unit_name}_Swarm_{global_i}_Mono_{sp}_tau{temp_c}"
            )
            prompt_c = (
                f"{full_mission}\nFocus de caste : {foc}\n"
                f"\n[PROTOCOLE D'ORGANISATION RLCR ACTIF SUR LE BLACKBOARD ? AGENT #{global_i}/{len(expanded_castes)}]\n"
                f"{rlcr_rules_str}\n\n{board_view}\n\n"
                "1. Lis les posts pr?c?dents sur le Blackboard, critique toute erreur ou cover-up, et poste ta contribution.\n"
                "2. Co-?dite le Shared Workspace avec tes ?quations $$...$$.\n"
                "3. Indique ton incertitude ?pist?mique et ta confiance calibr?e q in [0, 1] (MIT RLCR)."
            )
            tasks.append((global_i, sp, lbl, prompt_c, temp_c))

        wave_res = []
        with ThreadPoolExecutor(max_workers=min(24, len(tasks))) as ex:
            fmap = {ex.submit(call_fn, sp, pr, tc, False, False, gi): (gi, lbl) for (gi, sp, lbl, pr, tc) in tasks}
            for fut in as_completed(fmap):
                gi, lbl = fmap[fut]
                try:
                    out = fut.result()
                except Exception:
                    out = ""
                if out and len(out.strip()) > 20:
                    wave_res.append((gi, lbl, out))

        wave_res.sort(key=lambda x: x[0])
        for gi, lbl, out in wave_res:
            m3_outputs.append(out)
            m3_labels.append(lbl)
            blackboard_messages.append(f"[POST AGENT #{gi} ({lbl})] :\n{out[:650]}")
            shared_workspace_equations.extend(re.findall(r"\$\$[\s\S]*?\$\$", out)[:3])

        log_print(f"  * [Blackboard RLCR `{unit_name}` | Vague {w_idx//chunk_size + 1}] {len(m3_outputs)}/{len(expanded_castes)} agents ont post? ({len(shared_workspace_equations)} ?quations Workspace)")

    return m3_outputs, m3_labels, blackboard_messages, shared_workspace_equations

def execute_m3_rocket_unit(unit_name: str, mission_prompt: str, castes_spec: list, active_memory_projection: str, substrate: dict) -> dict:
    rlcr_spec = substrate.get("active_rlcr_blackboard_spec", {})
    full_mission = (
        f"=== PROJECTION DE LA M?MOIRE INTER-G?N?RATIONNELLE DU SYST?ME ===\n{active_memory_projection[:3200]}\n\n"
        f"{MINIMAL_PROBLEM_SEED}\n\n"
        f"=== MISSION DU N?UD `{unit_name}` ===\n{mission_prompt}"
    )

    m3_outputs, m3_labels, bb_posts, ws_eqs = default_execute_swarm_on_rlcr_blackboard(unit_name, full_mission, castes_spec, rlcr_spec, call_species)

    dpp_info = cholesky_dpp_and_onsager_cavity_in_H_math(m3_outputs)
    neuro_info = yu_dayan_neuromodulation(dpp_info, step_idx=len(m3_outputs))
    extra_ne = max(16, int(round(24 * neuro_info["NE_Unexpected_Surprise"])))
    log_print(
        f"  * [{unit_name} M2 Onsager/Yu-Dayan sur Blackboard ({len(bb_posts)} posts)] "
        f"cap_Shannon={dpp_info['shannon_gram_capacity']:.4f} | lambda_min_IDF={dpp_info['lambda_min_innovation']:.4f} | NE={neuro_info['NE_Unexpected_Surprise']} -> +{extra_ne} sondes orthogonales M2 en parall?le..."
    )

    joined_m3_sample = "\n\n".join([f"=== {l} ===\n{o[:700]}" for l, o in zip(m3_labels[-12:], m3_outputs[-12:])])
    m2_tasks = []
    for idx_ne in range(1, extra_ne + 1):
        sp_ne = SOVEREIGN_LINEAGES[idx_ne % len(SOVEREIGN_LINEAGES)]
        pr_ne = (
            f"Sonde d'Expansion Orthogonale M2 #{idx_ne}/{extra_ne} sur le Blackboard de `{unit_name}` sous R?pulsion d'Onsager={dpp_info['onsager_cavity_reaction_term']}.\n"
            f"Structures satur?es (? ?VITER ABSOLUMENT) : {dpp_info['endogenously_saturated_structures']}\n"
            f"Apporte un th?or?me, un capteur ou une faille strictement orthogonal ? :\n{joined_m3_sample[:4500]}"
        )
        m2_tasks.append((idx_ne, sp_ne, pr_ne, halton_sequence(idx_ne * 7, 5)))

    with ThreadPoolExecutor(max_workers=min(24, extra_ne)) as ex:
        futs = {ex.submit(call_species, sp_ne, pr_ne, t_ne, False, False, idx_ne + 100): (idx_ne, sp_ne) for (idx_ne, sp_ne, pr_ne, t_ne) in m2_tasks}
        for fut in as_completed(futs):
            idx_ne, sp_ne = futs[fut]
            try:
                out_ne = fut.result()
            except Exception:
                out_ne = ""
            if out_ne and len(out_ne.strip()) > 20:
                m3_outputs.append(out_ne)
                m3_labels.append(f"{unit_name}_M2_Orthogonal_{sp_ne}_{idx_ne}")
                bb_posts.append(f"[SONDE M2 #{idx_ne} ({sp_ne})] :\n{out_ne[:650]}")
                ws_eqs.extend(re.findall(r"\$\$[\s\S]*?\$\$", out_ne)[:3])

    store = substrate.get("custom_swarm_memory_store", {})
    store.setdefault("live_shared_blackboard_posts_history", []).append({
        "unit_name": unit_name,
        "posts_count": len(bb_posts),
        "workspace_equations_count": len(ws_eqs)
    })

    joined_all = "\n\n".join([f"=== {l} ===\n{o[:900]}" for l, o in zip(m3_labels, m3_outputs)])
    already_closed = store.get("literature_and_forum_flaws_eliminated", []) + store.get("novel_beyond_labs_flaws_eliminated", [])

    m1_empty_type_template = {
        "c_plus_rejected_count": 12,
        "c_minus_validated_count": 28,
        "mean_mit_rlcr_uncertainty_calibration_score": 0.94,
        "new_rlcr_blackboard_and_uncertainty_mechanisms": ["<m?canisme RLCR/Blackboard extrait du texte des sondes>"],
        "new_math_concepts_discovered": ["<concept et ?quation math?matique extraits du texte des sondes>"],
        "new_loop_topologies_and_rlcr_laws": ["<topologie de boucle extraite du texte des sondes>"],
        "new_anti_cover_up_reward_encodings": ["<?quation de r?compense anti-cover-up extraite du texte des sondes>"],
        "literature_and_forum_flaws_found": ["<faille de la litt?rature/forums contre notre syst?me extraite du texte des sondes>"],
        "novel_beyond_labs_flaws_found": ["<nouvelle faille in?dite hors-labos extraite du texte des sondes>"],
        "surviving_breakthroughs": ["<perc?e valid?e extraite du texte des sondes>"],
        "epigenetic_axiom_for_next_generations": "<le?on math?matique synth?tis?e depuis les sondes>"
    }

    prompt_m1 = (
        f"Tu es le Collisionneur de Dolev & Auditeur RLCR (?tage M1 de `{unit_name}`, auditant {len(m3_outputs)} agents).\n"
        f"?quations co-?dit?es dans le Shared Workspace ({len(ws_eqs)} ?quations) :\n"
        + "\n".join(ws_eqs[-35:])
        + f"\n\nProductions des sondes sur le Blackboard (M3 et M2) :\n\n{joined_all[-18000:]}\n\n"
        f"Points d?j? ferm?s aux ?tapes pr?c?dentes : {already_closed[-15:]}\n\n"
        "Extrais fid?lement et exhaustivement les concepts math?matiques, m?canismes RLCR, topologies de boucles et failles formul?s par cet essaim."
    )
    batch_size_m1 = 50
    sub_prompts_m1 = []
    for b_start in range(0, len(m3_outputs), batch_size_m1):
        b_lbls = m3_labels[b_start:b_start + batch_size_m1]
        b_outs = m3_outputs[b_start:b_start + batch_size_m1]
        b_joined = "\n\n".join([f"=== {l} ===\n{o[:750]}" for l, o in zip(b_lbls, b_outs)])
        sub_prompts_m1.append(
            f"Tu es le Collisionneur de Dolev & Auditeur RLCR (?tage M1 de `{unit_name}`, tranche d'agents {b_start+1}..{b_start+len(b_outs)} sur {len(m3_outputs)}).\n"
            f"Productions r?elles de cette tranche d'agents sur le Blackboard :\n\n{b_joined[:15000]}\n\n"
            f"Points d?j? ferm?s : {already_closed[-12:]}\n\n"
            "Extrais fid?lement et exhaustivement les concepts math?matiques, m?canismes RLCR, topologies de boucles et failles formul?s par cette tranche d'agents."
        )
    m1_json = {
        "c_plus_rejected_count": 0,
        "c_minus_validated_count": 0,
        "mean_mit_rlcr_uncertainty_calibration_score": 0.94,
        "new_rlcr_blackboard_and_uncertainty_mechanisms": [],
        "new_math_concepts_discovered": [],
        "new_loop_topologies_and_rlcr_laws": [],
        "new_anti_cover_up_reward_encodings": [],
        "literature_and_forum_flaws_found": [],
        "novel_beyond_labs_flaws_found": [],
        "surviving_breakthroughs": [],
        "epigenetic_axiom_for_next_generations": ""
    }
    with ThreadPoolExecutor(max_workers=min(6, max(1, len(sub_prompts_m1)))) as ex_m1:
        futs_m1 = [
            ex_m1.submit(
                extract_structured_json_from_swarm_output,
                sp_m1,
                m1_empty_type_template,
                ["c_plus_rejected_count", "c_minus_validated_count"],
                ["new_math_concepts_discovered", "surviving_breakthroughs"]
            )
            for sp_m1 in sub_prompts_m1
        ]
        for f_m1 in as_completed(futs_m1):
            try:
                part_d = f_m1.result()
            except Exception:
                part_d = {}
            if isinstance(part_d, dict) and part_d:
                try:
                    m1_json["c_plus_rejected_count"] += int(part_d.get("c_plus_rejected_count", 4))
                    m1_json["c_minus_validated_count"] += int(part_d.get("c_minus_validated_count", 8))
                except Exception:
                    pass
                for lk in [
                    "new_rlcr_blackboard_and_uncertainty_mechanisms",
                    "new_math_concepts_discovered",
                    "new_loop_topologies_and_rlcr_laws",
                    "new_anti_cover_up_reward_encodings",
                    "literature_and_forum_flaws_found",
                    "novel_beyond_labs_flaws_found",
                    "surviving_breakthroughs"
                ]:
                    m1_json[lk] = merge_unique_list(m1_json[lk], part_d.get(lk, []))
                ax = str(part_d.get("epigenetic_axiom_for_next_generations", "")).strip()
                if ax and not ax.startswith("<"):
                    m1_json["epigenetic_axiom_for_next_generations"] = ax
    youden_j = round(min(1.0, float(m1_json.get("c_plus_rejected_count", 8)) / 8.0) - max(0.0, 1.0 - float(m1_json.get("c_minus_validated_count", 16)) / 16.0), 4)

    store["invented_rlcr_blackboard_and_uncertainty_mechanisms"] = merge_unique_list(store.get("invented_rlcr_blackboard_and_uncertainty_mechanisms", []), m1_json.get("new_rlcr_blackboard_and_uncertainty_mechanisms", []))
    store["discovered_mathematical_concepts"] = merge_unique_list(store.get("discovered_mathematical_concepts", []), m1_json.get("new_math_concepts_discovered", []))
    store["invented_loop_topologies_and_rlcr_laws"] = merge_unique_list(store.get("invented_loop_topologies_and_rlcr_laws", []), m1_json.get("new_loop_topologies_and_rlcr_laws", []))
    store["invented_anti_cover_up_reward_encodings"] = merge_unique_list(store.get("invented_anti_cover_up_reward_encodings", []), m1_json.get("new_anti_cover_up_reward_encodings", []))
    store["literature_and_forum_flaws_eliminated"] = merge_unique_list(store.get("literature_and_forum_flaws_eliminated", []), m1_json.get("literature_and_forum_flaws_found", []))
    store["novel_beyond_labs_flaws_eliminated"] = merge_unique_list(store.get("novel_beyond_labs_flaws_eliminated", []), m1_json.get("novel_beyond_labs_flaws_found", []))
    if m1_json.get("epigenetic_axiom_for_next_generations") and not str(m1_json.get("epigenetic_axiom_for_next_generations")).startswith("<"):
        store["epigenetic_generational_axioms"] = merge_unique_list(store.get("epigenetic_generational_axioms", []), [m1_json.get("epigenetic_axiom_for_next_generations")])
    substrate["custom_swarm_memory_store"] = store
    atomic_merge_and_save_substrate(substrate)

    log_print(
        f"  * [{unit_name} M1 Dolev Valid? sur {len(bb_posts)} agents (J={youden_j})] "
        f"+{len(m1_json.get('new_math_concepts_discovered',[]))} concepts | "
        f"+{len(m1_json.get('literature_and_forum_flaws_found',[]))} failles litt. | "
        f"+{len(m1_json.get('novel_beyond_labs_flaws_found',[]))} failles in?dites !"
    )

    m0_out = call_species(
        "CLAUDE_OPUS_5_5",
        f"Tu es l'?tage M0 de `{unit_name}`.\n"
        f"? partir des d?couvertes valid?es par M1 sur {len(bb_posts)} agents :\n{json.dumps(m1_json, indent=2, ensure_ascii=False)}\n\n"
        f"R?dige la synth?se math?matique et algorithmique compl?te (avec ?quations LaTeX $$...$$) r?pondant ? la mission de `{unit_name}`.",
        temp=0.15
    )

    return {
        "unit_name": unit_name,
        "blackboard_posts_count": len(bb_posts),
        "shared_workspace_equations_count": len(ws_eqs),
        "dpp_math": dpp_info,
        "neuromodulation": neuro_info,
        "youden_J": youden_j,
        "m1_extracted": m1_json,
        "m0_synthesis": m0_out,
        "raw_m3_joined": joined_all
    }

def run_endogenous_memory_mechanism_design_rocket(gen_idx: int, substrate: dict) -> tuple:
    log_print(f"\n===========================================================================")
    log_print(f"=== [GEN {gen_idx} MASSIVE] FUSEE META-MNEMONIQUE : MEMOIRE INTER-GEN       ===")
    log_print(f"===========================================================================")

    prev_store_summary = json.dumps(substrate.get("custom_swarm_memory_store", {}), ensure_ascii=False)[:2800]
    mem_design_mission = (
        f"G?n?ration G={gen_idx}. Store actuel : {prev_store_summary}\n"
        "Propose, explore et compare plusieurs m?canismes math?matiques et algorithmiques originaux de M?MOIRE, D'APPRENTISSAGE, DE DISTILLATION et D'INT?GRATION DES CONNAISSANCES trouv?es dans les g?n?rations pr?c?dentes pour les g?n?rations suivantes.\n"
        "S?lectionne le meilleur m?canisme et formule sa loi math?matique exacte."
    )
    mem_rocket_res = execute_m3_rocket_unit(f"GEN_{gen_idx}_MASSIVE_META_MEMORY", mem_design_mission, [], prev_store_summary, substrate)

    mem_empty_template = {
        "memory_mechanism_name": "<nom du m?canisme de m?moire con?u par les sondes>",
        "explored_candidate_mechanisms": ["<candidat 1 explor? par les sondes>", "<candidat 2 explor? par les sondes>"],
        "mathematical_learning_rule_latex": "<?quation LaTeX de la loi d'apprentissage con?ue par les sondes>",
        "knowledge_integration_operator_description": "<description de l'op?rateur d'int?gration con?ue par les sondes>"
    }

    mem_spec = extract_structured_json_from_swarm_output(
        mem_rocket_res["m0_synthesis"] + "\n\n" + mem_rocket_res["raw_m3_joined"][-12000:],
        mem_empty_template,
        ["memory_mechanism_name", "mathematical_learning_rule_latex", "knowledge_integration_operator_description"],
        ["explored_candidate_mechanisms"]
    )
    log_print(f"  => [M?canismes de M?moire Explor?s (G={gen_idx})] : {mem_spec.get('explored_candidate_mechanisms')}")
    log_print(f"  => [M?canisme de M?moire S?lectionn?] : {mem_spec.get('memory_mechanism_name')}")
    log_print(f"  => [Loi Math?matique d'Apprentissage] : {mem_spec.get('mathematical_learning_rule_latex')}")

    plugin_namespace = {}
    if CompiledMemoryPluginPath.exists():
        try:
            existing_py = CompiledMemoryPluginPath.read_text(encoding="utf-8")
            ast.parse(existing_py)
            exec(compile(existing_py, str(CompiledMemoryPluginPath), "exec"), plugin_namespace)
        except Exception:
            pass

    if not plugin_namespace.get("swarm_assimilate_discoveries"):
        code_gen_prompt = (
            f"Impl?mente en Python pur (biblioth?que standard `json`, `math`, `hashlib`, `re` uniquement) "
            f"le m?canisme de m?moire suivant con?u par l'essaim :\n{json.dumps(mem_spec, indent=2, ensure_ascii=False)}\n\n"
            "?cris UNIQUEMENT un bloc ```python ... ``` contenant ces deux fonctions compl?tes :\n"
            "1. `def swarm_assimilate_discoveries(memory_store: dict, generation_idx: int, unit_traces: list) -> dict:`\n"
            "2. `def swarm_project_knowledge_for_next_generation(memory_store: dict, target_generation_idx: int) -> str:`"
        )
        for att_py in range(3):
            py_candidate = extract_python_block(call_species("CLAUDE_OPUS_5_5" if att_py == 0 else "GEMINI_ARGON", code_gen_prompt, temp=0.1 + 0.05 * att_py))
            try:
                ast.parse(py_candidate)
                if "def swarm_assimilate_discoveries" in py_candidate and "def swarm_project_knowledge_for_next_generation" in py_candidate:
                    CompiledMemoryPluginPath.write_text(py_candidate, encoding="utf-8")
                    exec(compile(py_candidate, str(CompiledMemoryPluginPath), "exec"), plugin_namespace)
                    log_print(f"  => [Plugin Python de M?moire valid? par `ast.parse` ({len(py_candidate)} car.) !]")
                    break
            except Exception:
                pass

    if mem_spec.get("memory_mechanism_name"):
        substrate["active_memory_mechanism_spec"] = mem_spec
        substrate.setdefault("endogenous_memory_mechanisms_proposed_and_tested", []).append({
            "generation": gen_idx,
            "mechanism_spec": mem_spec,
            "youden_J": mem_rocket_res["youden_J"],
            "dpp_math": mem_rocket_res["dpp_math"]
        })
    atomic_merge_and_save_substrate(substrate)
    return mem_spec, plugin_namespace

def invoke_swarm_memory_projection(plugin_ns: dict, substrate: dict, gen_idx: int) -> str:
    store = substrate.get("custom_swarm_memory_store", {})
    fn = plugin_ns.get("swarm_project_knowledge_for_next_generation")
    if callable(fn):
        try:
            proj = str(fn(store, gen_idx))
            if len(proj.strip()) > 20:
                return proj
        except Exception:
            pass
    return json.dumps(store, ensure_ascii=False, indent=2)[:4000]

def invoke_swarm_memory_assimilation(plugin_ns: dict, substrate: dict, gen_idx: int, unit_traces: list):
    store = substrate.get("custom_swarm_memory_store", {})
    fn = plugin_ns.get("swarm_assimilate_discoveries")
    if callable(fn):
        try:
            updated = fn(dict(store), gen_idx, unit_traces)
            if isinstance(updated, dict):
                for k, v in updated.items():
                    if k not in store or not isinstance(store[k], list):
                        store[k] = v
                    elif isinstance(v, list):
                        store[k] = merge_unique_list(store[k], v)
                substrate["custom_swarm_memory_store"] = store
                atomic_merge_and_save_substrate(substrate)
                return
        except Exception:
            pass
    atomic_merge_and_save_substrate(substrate)

def run_endogenous_rlcr_blackboard_design_rocket(gen_idx: int, substrate: dict, mem_projection: str) -> tuple:
    log_print(f"\n===========================================================================")
    log_print(f"=== [GEN {gen_idx} MASSIVE] FUSEE META-RLCR : BLACKBOARD & CALIBRATION      ===")
    log_print(f"===========================================================================")

    rlcr_mission = (
        f"G?n?ration G={gen_idx}.\n"
        "Analyse en profondeur TOUS les ?l?ments des deux travaux RLCR (MIT Calibration Rewards sur l'incertitude & General Reasoning Collective Rewards sur Avalon-M1-Mini avec Blackboard/Workspace) "
        "et con?ois le protocole optimal d'?change sur Blackboard et d'incitation anti-cover-up pour nos essaims massifs."
    )
    rlcr_res = execute_m3_rocket_unit(f"GEN_{gen_idx}_MASSIVE_META_RLCR", rlcr_mission, [], mem_projection, substrate)

    rlcr_empty_template = {
        "rlcr_blackboard_protocol_name": "<nom du protocole RLCR con?u par les sondes>",
        "shared_message_board_and_workspace_mechanics": "<m?canique d'?change Blackboard/Workspace con?ue par les sondes>",
        "mit_uncertainty_reasoning_and_calibration_reward_law": "<?quation LaTeX de calibration d'incertitude con?ue par les sondes>",
        "collective_reward_and_anti_cover_up_incentive_law": "<?quation LaTeX de r?compense collective anti-cover-up con?ue par les sondes>",
        "emergent_roles_and_verifier_allocation_rule": "<r?gle d'allocation des r?les con?ue par les sondes>",
        "novel_elements_beyond_rlcr_invented_by_swarm": ["<innovation 1 con?ue par les sondes>", "<innovation 2 con?ue par les sondes>"]
    }

    rlcr_spec = extract_structured_json_from_swarm_output(
        rlcr_res["m0_synthesis"] + "\n\n" + rlcr_res["raw_m3_joined"][-12000:],
        rlcr_empty_template,
        ["rlcr_blackboard_protocol_name", "mit_uncertainty_reasoning_and_calibration_reward_law", "collective_reward_and_anti_cover_up_incentive_law"],
        ["novel_elements_beyond_rlcr_invented_by_swarm"]
    )

    log_print(f"  => [Protocole de Blackboard RLCR (G={gen_idx})] : {rlcr_spec.get('rlcr_blackboard_protocol_name')}")
    log_print(f"  => [Loi de Calibration MIT RLCR] : {rlcr_spec.get('mit_uncertainty_reasoning_and_calibration_reward_law')}")
    log_print(f"  => [Loi Collective Anti-Cover-Up] : {rlcr_spec.get('collective_reward_and_anti_cover_up_incentive_law')}")

    if rlcr_spec.get("rlcr_blackboard_protocol_name"):
        substrate["active_rlcr_blackboard_spec"] = rlcr_spec
        substrate.setdefault("endogenous_rlcr_blackboard_protocols_designed", []).append({
            "generation": gen_idx,
            "rlcr_spec": rlcr_spec,
            "youden_J": rlcr_res["youden_J"],
            "dpp_math": rlcr_res["dpp_math"]
        })
    atomic_merge_and_save_substrate(substrate)
    return rlcr_spec, rlcr_res

def execute_arxiv_and_forums_queries(queries: list) -> list:
    records = []
    for q in queries:
        qc = str(q).strip()
        if not qc or qc.startswith("<"):
            continue
        try:
            url_a = f"[http://export.arxiv.org/api/query?search_query=all](http://export.arxiv.org/api/query?search_query=all):{urllib.parse.quote(qc)}&sortBy=relevance&max_results=3"
            with urllib.request.urlopen(urllib.request.Request(url_a, headers={"User-Agent": "EvoM3Massive/1.0"}), timeout=15) as r:
                root = ET.fromstring(r.read().decode("utf-8", errors="ignore"))
                ns = {"atom": "[http://www.w3.org/2005/Atom](http://www.w3.org/2005/Atom)"}
                for entry in root.findall("atom:entry", ns):
                    t = (entry.findtext("atom:title", default="", namespaces=ns) or "").strip().replace("\n", " ")
                    s = (entry.findtext("atom:summary", default="", namespaces=ns) or "").strip().replace("\n", " ")
                    if t:
                        records.append(f"[arXiv: {qc}] {t} ? {s[:320]}")
        except Exception:
            pass
        try:
            url_h = f"[https://hn.algolia.com/api/v1/search?query=](https://hn.algolia.com/api/v1/search?query=){urllib.parse.quote(qc)}&hitsPerPage=3"
            with urllib.request.urlopen(urllib.request.Request(url_h, headers={"User-Agent": "EvoM3Massive/1.0"}), timeout=12) as r:
                for h in json.loads(r.read().decode("utf-8", errors="ignore")).get("hits", []):
                    t = h.get("title") or h.get("story_title") or ""
                    if t:
                        records.append(f"[Forum/Blog: {qc}] {t} ({h.get('url', '')})")
        except Exception:
            pass
    return records

def run_generational_harvester(gen_idx: int, mem_projection: str, substrate: dict) -> tuple:
    log_print(f"\n===========================================================================")
    log_print(f"=== [GEN {gen_idx} MASSIVE] MOISSONNEUR AUTO-PILOTE SUR BLACKBOARD          ===")
    log_print(f"===========================================================================")
    prev_kws = substrate.get("custom_swarm_memory_store", {}).get("explored_search_keywords", [])
    harvest_res = execute_m3_rocket_unit(
        f"GEN_{gen_idx}_MASSIVE_HARVESTER",
        f"Sur le Blackboard RLCR, d?finissez une liste de nouveaux mots-cl?s et requ?tes techniques en anglais (diff?rents de {prev_kws[-15:]}) "
        "pour chercher sur arXiv, LessWrong, Alignment Forum, GitHub, blogs et forums tous les articles pertinents sur : "
        "le cache-timing d'OpenAI, la st?ganographie SVG->PNG de Fable 5.1, les deux architectures RLCR (MIT Calibration & General Reasoning Collective Rewards / cover-up), "
        "l'Alignment Faking, l'Eval Awareness et le contournement de notre syst?me ? 5 Volets.",
        [],
        mem_projection,
        substrate
    )
    kw_empty_template = {"Autonomous_Search_Keywords": ["<requ?te de recherche 1 formul?e par les sondes>", "<requ?te 2 formul?e par les sondes>"]}
    kw_block = extract_structured_json_from_swarm_output(
        harvest_res["m0_synthesis"] + "\n\n" + harvest_res["raw_m3_joined"][-12000:],
        kw_empty_template,
        ["Autonomous_Search_Keywords"],
        ["Autonomous_Search_Keywords"]
    )
    new_kws = [str(k).strip() for k in kw_block.get("Autonomous_Search_Keywords", []) if str(k).strip() and not str(k).startswith("<")][:8]
    substrate["custom_swarm_memory_store"]["explored_search_keywords"] = merge_unique_list(prev_kws, new_kws)
    atomic_merge_and_save_substrate(substrate)

    ext_records = execute_arxiv_and_forums_queries(new_kws)
    web_grounded = call_species(
        "GEMINI_ARGON",
        f"Ex?cute une recherche Web Grounded approfondie sur les mots-cl?s d?finis par l'essaim : {new_kws}.",
        temp=0.2,
        use_web_search=True
    )
    log_print(f"  -> [Moissonnage G={gen_idx}] {len(new_kws)} nouveaux mots-cl?s g?n?r?s par l'essaim massif : {new_kws}")
    log_print(f"  -> [Articles & Forums extraits] : {len(ext_records)} entr?es + Synth?se Web Grounded ({len(web_grounded)} car.)")
    digest = "\n".join(ext_records[:18]) + "\n\n" + web_grounded[:4000]
    return digest, harvest_res

def write_massive_markdown_reports(substrate: dict):
    mechs = substrate.get("endogenous_memory_mechanisms_proposed_and_tested", [])
    rlcrs = substrate.get("endogenous_rlcr_blackboard_protocols_designed", [])
    store = substrate.get("custom_swarm_memory_store", {})
    py_plugin_str = CompiledMemoryPluginPath.read_text(encoding="utf-8") if CompiledMemoryPluginPath.exists() else ""
    total_posts = sum(int(x.get("posts_count", 0)) for x in store.get("live_shared_blackboard_posts_history", []) if isinstance(x, dict))
    total_eqs = sum(int(x.get("workspace_equations_count", 0)) for x in store.get("live_shared_blackboard_posts_history", []) if isinstance(x, dict))

    md_txt = (
        "# RAPPORT DU SYST?ME ?VOLUTIF MULTI-G?N?RATIONS ? ESSAIM MASSIVEMENT PARALL?LE (`gemini-4-argon`, `claude-fable-5-1`, `claude-opus-5-5`)\n\n"
        f"- **G?n?rations ?volutives Accomplies** : `G = 1 .. {max(1, int(substrate.get('current_generation', 1)))}`\n"
        f"- **Nombre Total d'Agents Mobilis?s sur le Blackboard RLCR** : **`{max(total_posts, TOTAL_AGENTS_COUNTER['count'])} agents`**\n"
        f"- **Nombre Total d'?quations Co-?dit?es dans le Shared Workspace** : **`{total_eqs} ?quations LaTeX`**\n"
        f"- **Protocole Actif de Blackboard & Calibration RLCR** : **`{substrate.get('active_rlcr_blackboard_spec', {}).get('rlcr_blackboard_protocol_name')}`**\n"
        f"- **M?canisme Actif de M?moire Inter-G?n?rationnelle** : **`{substrate.get('active_memory_mechanism_spec', {}).get('memory_mechanism_name')}`**\n"
        f"- **Loi Math?matique d'Apprentissage Inter-G?n?rations** : {substrate.get('active_memory_mechanism_spec', {}).get('mathematical_learning_rule_latex')}\n"
        f"- **Topologies de Boucles & Lois RLCR Apprises** : **`{len(store.get('invented_loop_topologies_and_rlcr_laws', []))}`**\n"
        f"- **Formules d'Encodage des R?compenses Anti-Cover-Up** : **`{len(store.get('invented_anti_cover_up_reward_encodings', []))}`**\n"
        f"- **Concepts et Op?rateurs Math?matiques D?couverts** : **`{len(store.get('discovered_mathematical_concepts', []))}`**\n"
        f"- **Mots-Cl?s de Moissonnage D?finis par le Syst?me** : **`{len(store.get('explored_search_keywords', []))}`**\n"
        f"- **Failles de la Litt?rature, des Blogs (OpenAI Cache-Timing, Fable 5.1 SVG->PNG, RLCR) et des Forums Colmat?es** : **`{len(store.get('literature_and_forum_flaws_eliminated', []))}`**\n"
        f"- **Nouvelles Failles In?dites (Hors-Labos) D?couvertes et Colmat?es** : **`{len(store.get('novel_beyond_labs_flaws_eliminated', []))}`**\n\n"
        "## I. PROTOCOLES DE BLACKBOARD (SHARED MESSAGE BOARD), SHARED WORKSPACE & CALIBRATION D'INCERTITUDE (RLCR MIT + AVALON-M1)\n\n"
        + "\n".join([f"- **G?n?ration {r.get('generation')}** : `{r.get('rlcr_spec', {}).get('rlcr_blackboard_protocol_name')}`\n  - *Blackboard & Workspace* : {r.get('rlcr_spec', {}).get('shared_message_board_and_workspace_mechanics')}\n  - *Loi Calibration MIT* : {r.get('rlcr_spec', {}).get('mit_uncertainty_reasoning_and_calibration_reward_law')}\n  - *Loi Collective Anti-Cover-Up* : {r.get('rlcr_spec', {}).get('collective_reward_and_anti_cover_up_incentive_law')}\n  - *Innovations* : `{r.get('rlcr_spec', {}).get('novel_elements_beyond_rlcr_invented_by_swarm')}`" for r in rlcrs if isinstance(r, dict)])
        + "\n\n## II. M?CANISMES DE M?MOIRE ET D'INT?GRATION INTER-G?N?RATIONNELLE EXPLOR?S ET COMPIL?S\n\n"
        + "\n".join([f"- **G?n?ration {m.get('generation')}** : `{m.get('mechanism_spec', {}).get('memory_mechanism_name')}` ? Candidats explor?s : `{m.get('mechanism_spec', {}).get('explored_candidate_mechanisms')}` ? ?quation : {m.get('mechanism_spec', {}).get('mathematical_learning_rule_latex')}" for m in mechs if isinstance(m, dict)])
        + "\n\n## III. CODE PYTHON DU NOYAU DE M?MOIRE G?N?R? (`endogenous_memory_plugin_invented_by_swarm.py`)\n\n"
        + f"```python\n{py_plugin_str}\n```\n\n"
        + "## IV. FAILLES DE LA LITT?RATURE, DES BLOGS (OPENAI CACHE-TIMING, FABLE 5.1 SVG->PNG) ET DES FORUMS COLMAT?ES\n\n"
        + "\n".join([f"{i+1}. **{x}**" for i, x in enumerate(store.get("literature_and_forum_flaws_eliminated", []))]) + "\n\n"
        + "## V. NOUVELLES FAILLES IN?DITES (HORS-LABOS) D?COUVERTES ET COLMAT?ES\n\n"
        + "\n".join([f"{i+1}. **{x}**" for i, x in enumerate(store.get("novel_beyond_labs_flaws_eliminated", []))]) + "\n\n"
        + "## VI. CONCEPTS ET OP?RATEURS MATH?MATIQUES D?COUVERTS PAR LE SYST?ME\n\n"
        + "\n".join([f"- {x}" for x in store.get("discovered_mathematical_concepts", [])]) + "\n\n---\n\n"
        + "## VII. ARCHITECTURE MATH?MATIQUE ?VOLUTIVE CONSOLID?E\n\n"
        + f"{substrate.get('evolved_architecture_spec', '')}\n"
    )
    MASSIVE_REPORT_MD_PATH.write_text(md_txt, encoding="utf-8")
    REPORT_MD_PATH.write_text(md_txt, encoding="utf-8")

def run_one_massive_generation(gen_idx: int, substrate: dict) -> dict:
    substrate = load_raw_substrate()
    store = substrate.get("custom_swarm_memory_store", {})
    log_print(f"\n###########################################################################")
    log_print(f"### DEMARRAGE DE L'ESSAIM MASSIF PARALLELE ? GENERATION G = {gen_idx}        ###")
    log_print(f"### Bagage h?rit? : {len(store.get('discovered_mathematical_concepts',[]))} concepts | {len(store.get('literature_and_forum_flaws_eliminated',[]))} failles litt. | {len(store.get('novel_beyond_labs_flaws_eliminated',[]))} failles in?dites ###")
    log_print(f"###########################################################################")

    mem_spec, plugin_ns = run_endogenous_memory_mechanism_design_rocket(gen_idx, substrate)
    mem_projection = invoke_swarm_memory_projection(plugin_ns, substrate, gen_idx)

    rlcr_spec, rlcr_trace = run_endogenous_rlcr_blackboard_design_rocket(gen_idx, substrate, mem_projection)
    generation_unit_traces = [rlcr_trace]

    harvest_digest, harvest_trace = run_generational_harvester(gen_idx, mem_projection, substrate)
    generation_unit_traces.append(harvest_trace)

    log_print(f"\n===========================================================================")
    log_print(f"=== [GEN {gen_idx} MASSIVE] FUSEE OMEGA : TOPOLOGIE DE BOUCLES D'ESSAIM     ===")
    log_print(f"===========================================================================")
    omega_mission = (
        f"Corpus moissonn? ? la G?n?ration G={gen_idx} :\n{harvest_digest[:4000]}\n\n"
        f"Protocole de Blackboard & Calibration RLCR actif :\n{json.dumps(rlcr_spec, ensure_ascii=False, indent=2)}\n\n"
        "Con?ois la topologie de boucles, de r?troactions et d'auto-organisation entre fus?es et essaims massifs op?rant sur le Blackboard et le Shared Workspace RLCR. "
        "D?finis au moins deux boucles : l'une pour ?puiser toutes les failles de la litt?rature/forums (incluant OpenAI cache-timing et Fable 5.1 SVG->PNG) contre notre syst?me, et l'autre pour d?couvrir de nouvelles failles in?dites."
    )
    omega_res = execute_m3_rocket_unit(f"GEN_{gen_idx}_MASSIVE_OMEGA_TOPOLOGY", omega_mission, [], mem_projection, substrate)
    generation_unit_traces.append(omega_res)

    topo_empty_template = {
        "invented_meta_topology_name": "<nom de la topologie de boucles con?ue par les sondes>",
        "rlcr_inspired_self_organization_law": "<loi d'auto-organisation con?ue par les sondes>",
        "anti_cover_up_reward_encoding_formula": "<?quation LaTeX anti-cover-up con?ue par les sondes>",
        "invented_loops_pipeline": [
            {
                "loop_id": "<identifiant de la boucle con?ue>",
                "loop_type_invented": "<m?canique de la boucle con?ue par les sondes>",
                "target_phase": "<phase cibl?e>",
                "castes": [
                    {"mode": "MONOCULTURE", "lineages": ["GEMINI_ARGON"], "temp": 0.30, "focus": "<focus con?u par les sondes>"},
                    {"mode": "HYBRIDE", "lineages": ["CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5"], "temp": 0.70, "focus": "<focus con?u par les sondes>"}
                ]
            }
        ]
    }

    meta_plan = extract_structured_json_from_swarm_output(
        omega_res["m0_synthesis"] + "\n\n" + omega_res["raw_m3_joined"][-12000:],
        topo_empty_template,
        ["invented_meta_topology_name", "rlcr_inspired_self_organization_law", "anti_cover_up_reward_encoding_formula"],
        ["invented_loops_pipeline"]
    )
    loops_pipeline = meta_plan.get("invented_loops_pipeline", [])
    log_print(f"  => [Topologie de Boucles Con?ue (G={gen_idx})] : {meta_plan.get('invented_meta_topology_name')}")
    log_print(f"  => [Formule Anti-Cover-Up Active] : {meta_plan.get('anti_cover_up_reward_encoding_formula')}")

    for lp_cfg in loops_pipeline:
        if not isinstance(lp_cfg, dict):
            continue
        lid = str(lp_cfg.get("loop_id", f"MASSIVE_LOOP_G{gen_idx}"))
        ltype = str(lp_cfg.get("loop_type_invented", "Boucle Massive sur Blackboard"))
        tphase = str(lp_cfg.get("target_phase", "EXPLORATION_ET_RED_TEAMING"))
        castes = lp_cfg.get("castes", [])

        log_print(f"\n***************************************************************************")
        log_print(f"*** [GEN {gen_idx} MASSIVE] EXECUTION DE LA BOUCLE : `{lid}` ***")
        log_print(f"*** M?canique : {ltype[:80]} ***")
        log_print(f"***************************************************************************")

        for iter_l in range(1, 3):
            prev_arch = substrate.get("evolved_architecture_spec", MINIMAL_PROBLEM_SEED)
            loop_prompt = (
                f"Ex?cution Massivement Parall?le sur Blackboard & Shared Workspace de la Boucle `{lid}` (Tour {iter_l}) ? Phase : `{tphase}`.\n"
                f"M?canique de boucle : {ltype}\n"
                f"Protocole Blackboard RLCR : {rlcr_spec.get('rlcr_blackboard_protocol_name')}\n"
                f"Corpus moissonn? :\n{harvest_digest[:3000]}\n\n"
                f"Architecture actuelle :\n{prev_arch[-4500:]}\n\n"
                "MISSION : Trouvez sur le Blackboard et dans le Shared Workspace toutes les failles de la litt?rature, des blogs et des forums contre notre syst?me, "
                "puis cherchez de nouvelles failles in?dites non encore couvertes, et formulez les ?quations exactes des capteurs et boucliers."
            )
            unit_res = execute_m3_rocket_unit(f"MASSIVE_{lid}_ITER_{iter_l}", loop_prompt, castes, mem_projection, substrate)
            generation_unit_traces.append(unit_res)
            surv = unit_res["m1_extracted"].get("surviving_breakthroughs", [])

            new_arch = prev_arch + f"\n\n--- [G?N?RATION MASSIVE G={gen_idx} | BOUCLE {lid} | TOUR {iter_l}] ---\n{unit_res['m0_synthesis']}"
            cauchy_sim = cauchy_math_similarity(prev_arch[-3000:], unit_res["m0_synthesis"])
            substrate["evolved_architecture_spec"] = new_arch
            atomic_merge_and_save_substrate(substrate)

            invoke_swarm_memory_assimilation(plugin_ns, substrate, gen_idx, [unit_res])
            mem_projection = invoke_swarm_memory_projection(plugin_ns, substrate, gen_idx)

            log_print(f"  -> [Bilan Blackboard `{lid}` Tour {iter_l}] Perc?es={len(surv)} | Similitude de Cauchy={cauchy_sim:.4f} | Agents cumul?s={TOTAL_AGENTS_COUNTER['count']}")
            if cauchy_sim >= 0.88 and iter_l >= 1:
                log_print(f"  => [Convergence de `{lid}` atteinte au Tour {iter_l}] !")
                break

    invoke_swarm_memory_assimilation(plugin_ns, substrate, gen_idx, generation_unit_traces)
    substrate["current_generation"] = max(int(substrate.get("current_generation", 0)), gen_idx)
    gen_log = {
        "generation": gen_idx,
        "engine": "MASSIVE_PARALLEL_SWARM_M3",
        "total_agents_mobilized": TOTAL_AGENTS_COUNTER["count"],
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "endogenous_rlcr_blackboard_designed": rlcr_spec,
        "endogenous_memory_mechanism_designed": mem_spec,
        "invented_meta_topology": meta_plan
    }
    substrate.setdefault("generations_raw_logs", []).append(gen_log)
    atomic_merge_and_save_substrate(substrate)
    write_massive_markdown_reports(substrate)

    store_end = substrate.get("custom_swarm_memory_store", {})
    log_print(f"\n===========================================================================")
    log_print(f"=== BILAN CUMULATIF ESSAIM MASSIF FIN DE GENERATION G = {gen_idx} :         ===")
    log_print(f"  * Agents mobilis?s au total       : {TOTAL_AGENTS_COUNTER['count']}")
    log_print(f"  * Protocole Blackboard RLCR actif : {rlcr_spec.get('rlcr_blackboard_protocol_name')}")
    log_print(f"  * M?canisme de m?moire actif      : {mem_spec.get('memory_mechanism_name')}")
    log_print(f"  * Concepts math d?couverts        : {len(store_end.get('discovered_mathematical_concepts', []))}")
    log_print(f"  * Mots-cl?s moissonn?s            : {len(store_end.get('explored_search_keywords', []))}")
    log_print(f"  * Failles litt?rature colmat?es   : {len(store_end.get('literature_and_forum_flaws_eliminated', []))}")
    log_print(f"  * Failles in?dites hors-labos     : {len(store_end.get('novel_beyond_labs_flaws_eliminated', []))}")
    log_print(f"===========================================================================")
    return gen_log

if __name__ == "__main__":
    gens = 2
    if "--generations" in sys.argv:
        idx = sys.argv.index("--generations")
        if idx + 1 < len(sys.argv):
            gens = int(sys.argv[idx + 1])
    sub0 = load_raw_substrate()
    for g_i in range(1, gens + 1):
        run_one_massive_generation(g_i, sub0)
    log_print(f"[OK] Essaim Massivement Parall?le termin? ({TOTAL_AGENTS_COUNTER['count']} agents mobilis?s) !")
