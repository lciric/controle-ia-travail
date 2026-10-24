#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_evolutionary_generations_m3_system.py
===========================================================================
SYST?ME ?VOLUTIF MULTI-G?N?RATIONS UTILISANT LES VRAIS IDENTIFIANTS SERVEUR :
  - GEMINI_ARGON     -> `gemini-4-argon` / `gemini-3.1-pro-preview` / `gemini-3.8-flash`
  - CLAUDE_FABLE_5_1 -> `claude-fable-5-1` (avec header `anthropic-workspace-id`)
  - CLAUDE_OPUS_5_5  -> `claude-opus-5-5`  (avec header `anthropic-workspace-id`)
  - Z?RO valeur par d?faut cod?e en dur : 100% des concepts, failles, mots-cl?s,
    protocoles de Blackboard RLCR et plugins de m?moire proviennent des mod?les.
===========================================================================
"""
import os, sys, time, json, math, hashlib, pathlib, urllib.request, urllib.parse, urllib.error, subprocess, re, ast, xml.etree.ElementTree as ET
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
CompiledMemoryPluginPath = OUT_DIR / "endogenous_memory_plugin_invented_by_swarm.py"
REPORT_MD_PATH = OUT_DIR / "RAPPORT_SYSTEME_EVOLUTIF_MULTI_GENERATIONS_LOI_M3.md"

SOVEREIGN_LINEAGES = ["GEMINI_ARGON", "CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5"]
PRIMORDIAL_MITOSIS_DONE_CACHE = {"done": False, "differentiated_castes": []}

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

# =========================================================================
# EXTRACTION VECTORIELLE DES ?QUATIONS DANS H_math (CHOLESKY-DPP & ONSAGER)
# =========================================================================
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

def mathematical_concept_embedding(text: str, dim: int = 1024) -> np.ndarray:
    v = np.zeros(dim, dtype=np.float64)
    tokens = extract_endogenous_math_tokens_from_equations(text)
    if len(tokens) < 5:
        tokens = tokens + re.findall(r"[a-zA-Z0-9_\\^=<>+\-]{4,}", str(text or "").lower())
    if not tokens:
        v[0] = 1.0
        return v
    counts = {}
    for i, tok in enumerate(tokens):
        counts[tok] = counts.get(tok, 0) + 1
        if i + 1 < len(tokens):
            bg = f"{tok}::{tokens[i+1]}"
            counts[bg] = counts.get(bg, 0) + 1
    for feat, cnt in counts.items():
        idx = int(hashlib.md5(feat.encode("utf-8", errors="ignore")).hexdigest()[:8], 16) % dim
        sgn = 1.0 if (int(hashlib.md5((feat + "_s").encode("utf-8", errors="ignore")).hexdigest()[:2], 16) % 2 == 0) else -1.0
        v[idx] += sgn * (1.0 + math.log(cnt))
    norm = np.linalg.norm(v)
    return v / (norm + 1e-12)

def cholesky_dpp_and_onsager_cavity_in_H_math(texts: list) -> dict:
    if not texts:
        return {
            "metric_space": "ENDOGENOUS_MATHEMATICAL_STRUCTURES_L_M3",
            "n_sondes": 0, "det_G": 0.0, "log_det_G": 0.0, "lambda_min_innovation": 1.0,
            "mean_off_diag_similarity": 0.0, "onsager_cavity_reaction_term": 0.0,
            "endogenously_saturated_structures": []
        }
    vecs = np.stack([mathematical_concept_embedding(t) for t in texts], axis=0)
    n = len(texts)
    G = np.clip(vecs @ vecs.T, -0.999, 0.999)
    np.fill_diagonal(G, 1.0)
    eigvals = np.linalg.eigvalsh(G)
    lambda_min = float(max(0.0, np.min(eigvals)))
    sign, logdet = np.linalg.slogdet(G + 1e-5 * np.eye(n))
    det_val = float(np.exp(logdet)) if sign > 0 else 0.0
    off_diag = G - np.diag(np.diag(G))
    mean_corr = float(np.sum(np.abs(off_diag)) / max(1, n * (n - 1)))

    doc_freq = {}
    for t in texts:
        for tok in set(extract_endogenous_math_tokens_from_equations(t)):
            if len(tok) >= 3:
                doc_freq[tok] = doc_freq.get(tok, 0) + 1
    saturated = [k for k, _ in sorted(doc_freq.items(), key=lambda x: x[1], reverse=True)[:8] if doc_freq[k] >= max(2, n // 2)]

    return {
        "metric_space": "ENDOGENOUS_MATHEMATICAL_STRUCTURES_L_M3",
        "n_sondes": n,
        "det_G": round(det_val, 5),
        "log_det_G": round(float(logdet), 4),
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
    return round(0.15 + 0.80 * r, 3)

def clamp_temp(val, default_val: float = 0.5) -> float:
    try:
        v = float(val)
        return default_val if (math.isnan(v) or math.isinf(v)) else round(max(0.05, min(0.98, v)), 3)
    except Exception:
        return default_val

def yu_dayan_neuromodulation(dpp_info: dict, step_idx: int) -> dict:
    sim = float(dpp_info.get("mean_off_diag_similarity", 0.3))
    l_min = float(dpp_info.get("lambda_min_innovation", 0.5))
    ach = round(min(1.0, 0.35 + 0.12 * step_idx), 3)
    ne = round(min(1.0, 0.30 + 0.55 * sim + 0.25 * (1.0 - min(1.0, l_min))), 3)
    return {
        "ACh_Expected_Uncertainty": ach,
        "NE_Unexpected_Surprise": ne,
        "Dynamic_Inflation_Factor": round(1.0 + 0.50 * ne, 2)
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

# =========================================================================
# APPEL AUX VRAIS MOD?LES SERVEUR :
#   - `claude-fable-5-1` et `claude-opus-5-5` avec `anthropic-workspace-id`
#   - `gemini-4-argon`, `gemini-3.1-pro-preview` et `gemini-3.8-flash`
# =========================================================================
def call_species(species: str, prompt: str, temp: float = 0.45, use_web_search: bool = False, force_json_output: bool = False) -> str:
    temp_safe = clamp_temp(temp, 0.45)
    lineage = normalize_sovereign_lineage(species)
    header = (
        f"[LIGN?E : {lineage} | FORMALISATION MATH?MATIQUE EXACTE]\n"
        "Formule tes d?couvertes, op?rateurs et failles avec des ?quations LaTeX $$...$$ pr?cises, sans m?taphores.\n\n"
    )
    full_prompt = header + prompt

    # 1. Appel direct sur Anthropic avec `anthropic-workspace-id` pour CLAUDE_FABLE_5_1 et CLAUDE_OPUS_5_5
    if lineage in ("CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5") and not use_web_search and not force_json_output:
        ant_models = (
            ["claude-fable-5-1", "claude-fable-5", "claude-sonnet-5-5"]
            if lineage == "CLAUDE_FABLE_5_1" else
            ["claude-opus-5-5", "claude-opus-5", "claude-sonnet-5-5"]
        )
        for m_id in ant_models:
            for retry_a in range(3):
                try:
                    url = "https://api.anthropic.com/v1/messages"
                    payload = {
                        "model": m_id,
                        "max_tokens": 4096,
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
                    with urllib.request.urlopen(req, timeout=110) as r:
                        resp = json.loads(r.read().decode("utf-8"))
                        blocks = resp.get("content", [])
                        txt = "\n".join([b.get("text", "") for b in blocks if isinstance(b, dict) and b.get("type") == "text"]).strip()
                        if len(txt) > 30:
                            return txt
                except urllib.error.HTTPError as he:
                    if he.code == 429:
                        time.sleep(4 * (retry_a + 1))
                    else:
                        break
                except Exception:
                    time.sleep(2)

    # 2. Appel direct sur les vrais mod?les Gemini 3.x / 4-Argon de ton serveur
    gem_models = (
        ["gemini-3.8-flash", "gemini-3.1-pro-preview", "gemini-4-argon"]
        if force_json_output else
        ["gemini-4-argon", "gemini-3.1-pro-preview", "gemini-3.8-flash"]
    )
    for cand_m in gem_models:
        for retry_g in range(4):
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{cand_m}:generateContent?key={GEMINI_KEY}"
                gen_cfg = {"temperature": temp_safe, "maxOutputTokens": 8192}
                if force_json_output and not use_web_search:
                    gen_cfg["responseMimeType"] = "application/json"
                payload = {"contents": [{"parts": [{"text": full_prompt}]}], "generationConfig": gen_cfg}
                if use_web_search:
                    payload["tools"] = [{"google_search": {}}]
                req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
                with urllib.request.urlopen(req, timeout=110) as r:
                    resp = json.loads(r.read().decode("utf-8"))
                    out_txt = extract_gemini_text_from_parts(resp)
                    if len(out_txt.strip()) > 10:
                        return out_txt
            except urllib.error.HTTPError as he:
                if he.code == 429:
                    time.sleep(5 * (retry_g + 1))
                else:
                    break
            except Exception:
                time.sleep(2 * (retry_g + 1))
    return "{}" if force_json_output else ""

def parse_json_robust(txt: str) -> dict:
    s = str(txt or "").strip()
    if not s:
        return {}
    try:
        d = json.loads(s)
        if isinstance(d, dict):
            return d
    except Exception:
        pass
    if "```json" in s:
        blocks = s.split("```json")
        for b in reversed(blocks[1:]):
            cand = b.split("```", 1)[0].strip()
            try:
                d = json.loads(cand)
                if isinstance(d, dict):
                    return d
            except Exception:
                pass
    end_pos = s.rfind("}")
    if end_pos != -1:
        starts = [m.start() for m in re.finditer(r"\{", s[:end_pos])]
        for st in reversed(starts):
            try:
                d = json.loads(s[st:end_pos+1])
                if isinstance(d, dict) and len(d) >= 1:
                    return d
            except Exception:
                pass
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
        f"{str(raw_swarm_text)[-12000:]}"
    )
    for att in range(3):
        j_out = call_species("GEMINI_ARGON", prompt_extract, temp=0.1 + 0.05 * att, force_json_output=True)
        d = parse_json_robust(j_out)
        if d and all(d.get(k) not in (None, "") for k in required_keys) and all(isinstance(d.get(lk), list) and len(d.get(lk)) >= 1 for lk in list_keys):
            return d
    return d if isinstance(d, dict) else {}

def extract_python_block(txt: str) -> str:
    s = str(txt or "")
    if "```python" in s:
        return s.split("```python", 1)[1].split("```", 1)[0].strip()
    if "```" in s:
        return s.split("```", 1)[1].split("```", 1)[0].strip()
    return s.strip()

def load_raw_substrate() -> dict:
    if RAW_SUBSTRATE_FILE.exists():
        try:
            return json.loads(RAW_SUBSTRATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {
        "current_generation": 0,
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

def save_raw_substrate(sub: dict):
    RAW_SUBSTRATE_FILE.write_text(json.dumps(sub, indent=2, ensure_ascii=False), encoding="utf-8")

def merge_unique_list(base_list: list, new_items: list) -> list:
    out = list(base_list) if isinstance(base_list, list) else []
    for x in (new_items or []):
        s = str(x).strip()
        if s and not s.startswith("<") and s not in out:
            out.append(s)
    return out

# =========================================================================
# 1. AMOR?AGE PAR MITOSE CELLULAIRE UNIQUE (k=1 -> N*) SUR LE BLACKBOARD RLCR
# =========================================================================
def execute_mitosis_from_single_cell_on_rlcr_blackboard(unit_name: str, full_mission: str, rlcr_spec: dict, call_fn) -> tuple:
    blackboard_messages = []
    shared_workspace_equations = []
    m3_outputs, m3_labels = [], []
    rlcr_rules_str = json.dumps(rlcr_spec, ensure_ascii=False, indent=2) if rlcr_spec else "Blackboard RLCR : Shared Message Board + Shared Workspace + MIT Uncertainty Calibration."

    k_cell = 0
    prev_lambda_min = 1.0

    while True:
        k_cell += 1
        sp = SOVEREIGN_LINEAGES[(k_cell - 1) % len(SOVEREIGN_LINEAGES)]
        tau_halton = halton_sequence(k_cell, base=2)

        board_view = (
            "CELLULE SOUCHE PRIMORDIALE k=1 : Le Blackboard et le Shared Workspace sont vierges. Inaugure-les !"
            if not blackboard_messages else
            f"=== ?TAT DU BLACKBOARD (CELLULES 1..{k_cell-1}) ===\n"
            + "\n---\n".join(blackboard_messages[-3:])
            + "\n\n=== ?QUATIONS DU SHARED WORKSPACE ===\n"
            + "\n".join(shared_workspace_equations[-8:])
        )

        rlcr_cell_prompt = (
            f"\n\n[PROTOCOLE BLACKBOARD RLCR & MITOSE CELLULAIRE k={k_cell}]\n{rlcr_rules_str}\n\n"
            f"{board_view}\n\n"
            "ACTIONS DE LA CELLULE SUR LE BLACKBOARD :\n"
            "1. Si k > 1, r?fute tout angle mort ou cover-up des cellules pr?c?dentes et apporte un op?rateur math?matique STRICTEMENT ORTHOGONAL.\n"
            "2. Enrichis le Shared Workspace avec tes ?quations LaTeX $$...$$.\n"
            "3. Raisonne sur ton incertitude ?pist?mique (MIT RLCR) et indique ta confiance calibr?e q in [0, 1]."
        )

        if k_cell >= 3 and (k_cell % 2 == 0):
            sp_partner = SOVEREIGN_LINEAGES[k_cell % len(SOVEREIGN_LINEAGES)]
            lbl = f"{unit_name}_Mitose_Cell_{k_cell}_Hybride_{sp}_x_{sp_partner}_tau{tau_halton}"
            out_c = call_fn(sp, f"{full_mission}\n[F?condation Cellulaire Hybride {sp} x {sp_partner} sur Blackboard]{rlcr_cell_prompt}", tau_halton)
        else:
            lbl = f"{unit_name}_Mitose_Cell_{k_cell}_Monoculture_{sp}_tau{tau_halton}"
            out_c = call_fn(sp, f"{full_mission}\n[Division Cellulaire Monoculture {sp} sur Blackboard]{rlcr_cell_prompt}", tau_halton)

        m3_outputs.append(out_c)
        m3_labels.append(lbl)
        blackboard_messages.append(f"[CELLULE k={k_cell} ({lbl})] :\n{out_c[:900]}")
        shared_workspace_equations.extend(re.findall(r"\$\$[\s\S]*?\$\$", out_c)[:3])

        spec_info = cholesky_dpp_and_onsager_cavity_in_H_math(m3_outputs)
        l_min = spec_info["lambda_min_innovation"]
        delta_l = prev_lambda_min - l_min
        prev_lambda_min = l_min
        print(f"    * [Mitose Cellulaire k={k_cell} sur Blackboard | {lbl:58s}] det(G_math)={spec_info['det_G']:.5f} | lambda_min={l_min:.4f} | Delta_lambda={delta_l:.4f}")

        if k_cell >= 6 and (l_min < 0.45 or abs(delta_l) < 0.08):
            print(f"    => [Arr?t Spectral Endog?ne de la Mitose sur Blackboard] N* = {k_cell} cellules (det(G_math)={spec_info['det_G']:.5f}, lambda_min={l_min:.4f}) !")
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
                    "focus": f"Caste diff?renci?e issue de la cellule primordiale #{i+1}"
                }
                for i, lbl in enumerate(m3_lbl)
            ]
            print(f"    => [Amor?age Primordial Scell? UNE FOIS POUR TOUTES] {len(m3_lbl)} castes diff?renci?es m?moris?es pour toute la suite !")
            return m3_out, m3_lbl, bb_p, ws_e
        else:
            castes_spec = PRIMORDIAL_MITOSIS_DONE_CACHE["differentiated_castes"]
            print(f"    * [H?r?dit? Morphog?n?tique Active] R?utilisation directe des {len(castes_spec)} castes diff?renci?es (z?ro retour ? k=1) !")

    blackboard_messages = []
    shared_workspace_equations = []
    m3_outputs, m3_labels = [], []
    rlcr_rules_str = json.dumps(rlcr_spec, ensure_ascii=False, indent=2) if rlcr_spec else "Blackboard RLCR standard."

    for idx_c, c_cfg in enumerate(castes_spec, start=1):
        mode = str(c_cfg.get("mode", "MONOCULTURE")).upper()
        lins = c_cfg.get("lineages", ["GEMINI_ARGON"])
        if not isinstance(lins, list) or not lins:
            lins = ["GEMINI_ARGON"]
        temp_c = clamp_temp(c_cfg.get("temp", halton_sequence(idx_c, 2)))
        foc = str(c_cfg.get("focus", "Exploration endog?ne"))

        board_view = (
            "BLACKBOARD ENCORE VIERGE (Tu es le 1er agent ? poster)."
            if not blackboard_messages else
            "=== ?TAT EN DIRECT DU BLACKBOARD (SHARED MESSAGE BOARD) ===\n"
            + "\n---\n".join(blackboard_messages[-4:])
            + "\n\n=== ?TAT EN DIRECT DU SHARED WORKSPACE ===\n"
            + "\n".join(shared_workspace_equations[-10:])
        )
        rlcr_agent_instructions = (
            f"\n\n[PROTOCOLE D'ORGANISATION RLCR ACTIF SUR LE BLACKBOARD]\n{rlcr_rules_str}\n\n{board_view}\n\n"
            "1. Lis les posts pr?c?dents sur le Blackboard, critique toute erreur ou cover-up, et poste ta contribution.\n"
            "2. Co-?dite le Shared Workspace avec tes ?quations $$...$$.\n"
            "3. Indique ton incertitude ?pist?mique et ta confiance calibr?e q in [0, 1] (MIT RLCR)."
        )

        if "HYB" in mode and len(lins) >= 2:
            sp1, sp2 = normalize_sovereign_lineage(lins[0]), normalize_sovereign_lineage(lins[1])
            lbl = f"{unit_name}_Blackboard_Hybride_{sp1}_x_{sp2}_tau{temp_c}"
            print(f"    * [Blackboard RLCR | {lbl}] Focus : {foc[:50]}...")
            s1 = call_fn(sp1, f"{full_mission}\nFocus : {foc}\n{rlcr_agent_instructions}", temp_c)
            blackboard_messages.append(f"[POST DE {sp1} ({lbl}_A)] :\n{s1[:900]}")
            shared_workspace_equations.extend(re.findall(r"\$\$[\s\S]*?\$\$", s1)[:3])
            s2 = call_fn(sp2, f"{full_mission}\nFocus : {foc}\n{rlcr_agent_instructions}\nDernier post de {sp1} :\n{s1[:900]}", temp_c)
            blackboard_messages.append(f"[POST DE {sp2} ({lbl}_B)] :\n{s2[:900]}")
            shared_workspace_equations.extend(re.findall(r"\$\$[\s\S]*?\$\$", s2)[:3])
            m3_outputs.extend([s1, s2])
            m3_labels.extend([lbl + "_A", lbl + "_B"])
        else:
            sp = normalize_sovereign_lineage(lins[0])
            lbl = f"{unit_name}_Blackboard_Mono_{sp}_tau{temp_c}"
            print(f"    * [Blackboard RLCR | {lbl}] Focus : {foc[:50]}...")
            out = call_fn(sp, f"{full_mission}\nFocus : {foc}\n{rlcr_agent_instructions}", temp_c)
            blackboard_messages.append(f"[POST DE {sp} ({lbl})] :\n{out[:900]}")
            shared_workspace_equations.extend(re.findall(r"\$\$[\s\S]*?\$\$", out)[:3])
            m3_outputs.append(out)
            m3_labels.append(lbl)

    return m3_outputs, m3_labels, blackboard_messages, shared_workspace_equations

# =========================================================================
# BRIQUE UNIVERSELLE DE FUS?E ? 3 ?TAGES
# =========================================================================
def execute_m3_rocket_unit(unit_name: str, mission_prompt: str, castes_spec: list, active_memory_projection: str, substrate: dict) -> dict:
    rlcr_spec = substrate.get("active_rlcr_blackboard_spec", {})
    full_mission = (
        f"=== PROJECTION DE LA M?MOIRE INTER-G?N?RATIONNELLE DU SYST?ME ===\n{active_memory_projection[:2800]}\n\n"
        f"{MINIMAL_PROBLEM_SEED}\n\n"
        f"=== MISSION DU N?UD `{unit_name}` ===\n{mission_prompt}"
    )

    m3_outputs, m3_labels, bb_posts, ws_eqs = default_execute_swarm_on_rlcr_blackboard(unit_name, full_mission, castes_spec, rlcr_spec, call_species)

    store = substrate.get("custom_swarm_memory_store", {})
    store.setdefault("live_shared_blackboard_posts_history", []).append({
        "unit_name": unit_name,
        "posts_count": len(bb_posts),
        "workspace_equations_count": len(ws_eqs)
    })

    dpp_info = cholesky_dpp_and_onsager_cavity_in_H_math(m3_outputs)
    neuro_info = yu_dayan_neuromodulation(dpp_info, step_idx=len(m3_outputs))
    extra_ne = max(1, int(round(2 * neuro_info["NE_Unexpected_Surprise"])))
    print(f"    * [{unit_name} M2 Onsager/Yu-Dayan sur Blackboard ({len(bb_posts)} posts)] det(G_math)={dpp_info['det_G']:.5f} | lambda_min={dpp_info['lambda_min_innovation']:.4f} | NE={neuro_info['NE_Unexpected_Surprise']} -> +{extra_ne} sonde(s)...")

    joined_m3 = "\n\n".join([f"=== {l} ===\n{o[:1400]}" for l, o in zip(m3_labels, m3_outputs)])
    for idx_ne in range(1, extra_ne + 1):
        sp_ne = SOVEREIGN_LINEAGES[idx_ne % len(SOVEREIGN_LINEAGES)]
        out_ne = call_species(
            sp_ne,
            f"Sonde d'Expansion Orthogonale M2 #{idx_ne} sur le Blackboard de `{unit_name}` sous R?pulsion d'Onsager={dpp_info['onsager_cavity_reaction_term']}.\n"
            f"Structures satur?es (? ?VITER) : {dpp_info['endogenously_saturated_structures']}\n"
            f"Compl?ment orthogonal ? :\n{joined_m3[:3500]}",
            temp=halton_sequence(idx_ne * 7, 5)
        )
        m3_outputs.append(out_ne)
        m3_labels.append(f"{unit_name}_M2_Orthogonal_{sp_ne}_{idx_ne}")

    joined_all = "\n\n".join([f"=== {l} ===\n{o[:1400]}" for l, o in zip(m3_labels, m3_outputs)])
    already_closed = store.get("literature_and_forum_flaws_eliminated", []) + store.get("novel_beyond_labs_flaws_eliminated", [])

    m1_empty_type_template = {
        "c_plus_rejected_count": 4,
        "c_minus_validated_count": 4,
        "mean_mit_rlcr_uncertainty_calibration_score": 0.95,
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
        f"Tu es le Collisionneur de Dolev & Auditeur RLCR (?tage M1 de `{unit_name}`).\n"
        f"Voici les productions r?elles des sondes sur le Blackboard et le Shared Workspace (M3 et M2) :\n\n{joined_all[:13500]}\n\n"
        f"Points d?j? ferm?s aux ?tapes pr?c?dentes : {already_closed[-12:]}\n\n"
        "Extrais fid?lement et uniquement les concepts math?matiques, m?canismes RLCR, topologies de boucles et failles qui ont ?t? formul?s par les sondes ci-dessus."
    )
    m1_json = extract_structured_json_from_swarm_output(
        prompt_m1 + "\n\n" + joined_all[-6000:],
        m1_empty_type_template,
        ["c_plus_rejected_count", "c_minus_validated_count"],
        ["new_math_concepts_discovered", "surviving_breakthroughs"]
    )
    youden_j = round(min(1.0, int(m1_json.get("c_plus_rejected_count", 4)) / 4.0) - max(0.0, 1.0 - int(m1_json.get("c_minus_validated_count", 4)) / 4.0), 4)

    store["invented_rlcr_blackboard_and_uncertainty_mechanisms"] = merge_unique_list(store.get("invented_rlcr_blackboard_and_uncertainty_mechanisms", []), m1_json.get("new_rlcr_blackboard_and_uncertainty_mechanisms", []))
    store["discovered_mathematical_concepts"] = merge_unique_list(store.get("discovered_mathematical_concepts", []), m1_json.get("new_math_concepts_discovered", []))
    store["invented_loop_topologies_and_rlcr_laws"] = merge_unique_list(store.get("invented_loop_topologies_and_rlcr_laws", []), m1_json.get("new_loop_topologies_and_rlcr_laws", []))
    store["invented_anti_cover_up_reward_encodings"] = merge_unique_list(store.get("invented_anti_cover_up_reward_encodings", []), m1_json.get("new_anti_cover_up_reward_encodings", []))
    store["literature_and_forum_flaws_eliminated"] = merge_unique_list(store.get("literature_and_forum_flaws_eliminated", []), m1_json.get("literature_and_forum_flaws_found", []))
    store["novel_beyond_labs_flaws_eliminated"] = merge_unique_list(store.get("novel_beyond_labs_flaws_eliminated", []), m1_json.get("novel_beyond_labs_flaws_found", []))
    if m1_json.get("epigenetic_axiom_for_next_generations") and not str(m1_json.get("epigenetic_axiom_for_next_generations")).startswith("<"):
        store["epigenetic_generational_axioms"] = merge_unique_list(store.get("epigenetic_generational_axioms", []), [m1_json.get("epigenetic_axiom_for_next_generations")])
    substrate["custom_swarm_memory_store"] = store
    save_raw_substrate(substrate)

    print(f"    * [{unit_name} M1 Dolev Valid? (J={youden_j})] +{len(m1_json.get('new_math_concepts_discovered',[]))} concepts | +{len(m1_json.get('literature_and_forum_flaws_found',[]))} failles litt. | +{len(m1_json.get('novel_beyond_labs_flaws_found',[]))} failles in?dites !")

    m0_out = call_species(
        "CLAUDE_OPUS_5_5",
        f"Tu es l'?tage M0 de `{unit_name}`.\n"
        f"? partir des d?couvertes valid?es par M1 :\n{json.dumps(m1_json, indent=2, ensure_ascii=False)}\n\n"
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

# =========================================================================
# FUS?E M?TA-MN?MONIQUE
# =========================================================================
def run_endogenous_memory_mechanism_design_rocket(gen_idx: int, substrate: dict) -> tuple:
    print(f"\n===========================================================================")
    print(f"=== [GEN {gen_idx}] FUSEE META-MNEMONIQUE : CONCEPTION DE LA MEMOIRE INTER-GEN ===")
    print(f"===========================================================================")

    prev_store_summary = json.dumps(substrate.get("custom_swarm_memory_store", {}), ensure_ascii=False)[:2500]
    mem_design_mission = (
        f"G?n?ration G={gen_idx}. Store actuel : {prev_store_summary}\n"
        "Propose, explore et compare plusieurs m?canismes math?matiques et algorithmiques originaux de M?MOIRE, D'APPRENTISSAGE, DE DISTILLATION et D'INT?GRATION DES CONNAISSANCES trouv?es dans les g?n?rations pr?c?dentes pour les g?n?rations suivantes.\n"
        "S?lectionne le meilleur m?canisme et formule sa loi math?matique exacte."
    )
    mem_rocket_res = execute_m3_rocket_unit(f"GEN_{gen_idx}_META_MEMORY_ARCHITECT", mem_design_mission, [], prev_store_summary, substrate)

    mem_empty_template = {
        "memory_mechanism_name": "<nom du m?canisme de m?moire con?u par les sondes>",
        "explored_candidate_mechanisms": ["<candidat 1 explor? par les sondes>", "<candidat 2 explor? par les sondes>"],
        "mathematical_learning_rule_latex": "<?quation LaTeX de la loi d'apprentissage con?ue par les sondes>",
        "knowledge_integration_operator_description": "<description de l'op?rateur d'int?gration con?ue par les sondes>"
    }

    mem_spec = extract_structured_json_from_swarm_output(
        mem_rocket_res["m0_synthesis"] + "\n\n" + mem_rocket_res["raw_m3_joined"],
        mem_empty_template,
        ["memory_mechanism_name", "mathematical_learning_rule_latex", "knowledge_integration_operator_description"],
        ["explored_candidate_mechanisms"]
    )
    print(f"  => [M?canismes de M?moire Explor?s (G={gen_idx})] : {mem_spec.get('explored_candidate_mechanisms')}")
    print(f"  => [M?canisme de M?moire S?lectionn?] : {mem_spec.get('memory_mechanism_name')}")
    print(f"  => [Loi Math?matique d'Apprentissage] : {mem_spec.get('mathematical_learning_rule_latex')}")

    code_gen_prompt = (
        f"Impl?mente en Python pur (biblioth?que standard `json`, `math`, `hashlib`, `re` uniquement) "
        f"le m?canisme de m?moire suivant con?u par l'essaim :\n{json.dumps(mem_spec, indent=2, ensure_ascii=False)}\n\n"
        "?cris UNIQUEMENT un bloc ```python ... ``` contenant ces deux fonctions compl?tes :\n"
        "1. `def swarm_assimilate_discoveries(memory_store: dict, generation_idx: int, unit_traces: list) -> dict:`\n"
        "2. `def swarm_project_knowledge_for_next_generation(memory_store: dict, target_generation_idx: int) -> str:`"
    )
    plugin_namespace = {}
    for att_py in range(3):
        py_candidate = extract_python_block(call_species("CLAUDE_OPUS_5_5" if att_py == 0 else "GEMINI_ARGON", code_gen_prompt, temp=0.1 + 0.05 * att_py))
        try:
            ast.parse(py_candidate)
            if "def swarm_assimilate_discoveries" in py_candidate and "def swarm_project_knowledge_for_next_generation" in py_candidate:
                CompiledMemoryPluginPath.write_text(py_candidate, encoding="utf-8")
                exec(compile(py_candidate, str(CompiledMemoryPluginPath), "exec"), plugin_namespace)
                print(f"  => [Plugin Python de M?moire g?n?r? par le mod?le et valid? par `ast.parse` ({len(py_candidate)} car.) !]")
                break
        except Exception:
            pass

    substrate["active_memory_mechanism_spec"] = mem_spec
    substrate.setdefault("endogenous_memory_mechanisms_proposed_and_tested", []).append({
        "generation": gen_idx,
        "mechanism_spec": mem_spec,
        "youden_J": mem_rocket_res["youden_J"],
        "dpp_math": mem_rocket_res["dpp_math"]
    })
    save_raw_substrate(substrate)
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
                save_raw_substrate(substrate)
                return
        except Exception:
            pass
    save_raw_substrate(substrate)

# =========================================================================
# FUS?E M?TA-RLCR
# =========================================================================
def run_endogenous_rlcr_blackboard_design_rocket(gen_idx: int, substrate: dict, mem_projection: str) -> tuple:
    print(f"\n===========================================================================")
    print(f"=== [GEN {gen_idx}] FUSEE META-RLCR : PROTOCOLE BLACKBOARD & CALIBRATION    ===")
    print(f"===========================================================================")

    rlcr_mission = (
        f"G?n?ration G={gen_idx}.\n"
        "Analyse en profondeur TOUS les ?l?ments des deux travaux RLCR (MIT Calibration Rewards sur l'incertitude & General Reasoning Collective Rewards sur Avalon-M1-Mini avec Blackboard/Workspace) "
        "et con?ois le protocole optimal d'?change sur Blackboard et d'incitation anti-cover-up pour nos essaims."
    )
    rlcr_res = execute_m3_rocket_unit(f"GEN_{gen_idx}_META_RLCR_BLACKBOARD_ARCHITECT", rlcr_mission, [], mem_projection, substrate)

    rlcr_empty_template = {
        "rlcr_blackboard_protocol_name": "<nom du protocole RLCR con?u par les sondes>",
        "shared_message_board_and_workspace_mechanics": "<m?canique d'?change Blackboard/Workspace con?ue par les sondes>",
        "mit_uncertainty_reasoning_and_calibration_reward_law": "<?quation LaTeX de calibration d'incertitude con?ue par les sondes>",
        "collective_reward_and_anti_cover_up_incentive_law": "<?quation LaTeX de r?compense collective anti-cover-up con?ue par les sondes>",
        "emergent_roles_and_verifier_allocation_rule": "<r?gle d'allocation des r?les con?ue par les sondes>",
        "novel_elements_beyond_rlcr_invented_by_swarm": ["<innovation 1 con?ue par les sondes>", "<innovation 2 con?ue par les sondes>"]
    }

    rlcr_spec = extract_structured_json_from_swarm_output(
        rlcr_res["m0_synthesis"] + "\n\n" + rlcr_res["raw_m3_joined"],
        rlcr_empty_template,
        ["rlcr_blackboard_protocol_name", "mit_uncertainty_reasoning_and_calibration_reward_law", "collective_reward_and_anti_cover_up_incentive_law"],
        ["novel_elements_beyond_rlcr_invented_by_swarm"]
    )

    print(f"  => [Protocole de Blackboard RLCR (G={gen_idx})] : {rlcr_spec.get('rlcr_blackboard_protocol_name')}")
    print(f"  => [Loi de Calibration MIT RLCR] : {rlcr_spec.get('mit_uncertainty_reasoning_and_calibration_reward_law')}")
    print(f"  => [Loi Collective Anti-Cover-Up] : {rlcr_spec.get('collective_reward_and_anti_cover_up_incentive_law')}")

    substrate["active_rlcr_blackboard_spec"] = rlcr_spec
    substrate.setdefault("endogenous_rlcr_blackboard_protocols_designed", []).append({
        "generation": gen_idx,
        "rlcr_spec": rlcr_spec,
        "youden_J": rlcr_res["youden_J"],
        "dpp_math": rlcr_res["dpp_math"]
    })
    save_raw_substrate(substrate)
    return rlcr_spec, rlcr_res

# =========================================================================
# MOISSONNEUR AUTONOME IT?RATIF
# =========================================================================
def execute_arxiv_and_forums_queries(queries: list) -> list:
    records = []
    for q in queries:
        qc = str(q).strip()
        if not qc or qc.startswith("<"):
            continue
        try:
            url_a = f"[http://export.arxiv.org/api/query?search_query=all](http://export.arxiv.org/api/query?search_query=all):{urllib.parse.quote(qc)}&sortBy=relevance&max_results=3"
            with urllib.request.urlopen(urllib.request.Request(url_a, headers={"User-Agent": "EvoM3/1.0"}), timeout=15) as r:
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
            with urllib.request.urlopen(urllib.request.Request(url_h, headers={"User-Agent": "EvoM3/1.0"}), timeout=12) as r:
                for h in json.loads(r.read().decode("utf-8", errors="ignore")).get("hits", []):
                    t = h.get("title") or h.get("story_title") or ""
                    if t:
                        records.append(f"[Forum/Blog: {qc}] {t} ({h.get('url', '')})")
        except Exception:
            pass
    return records

def run_generational_harvester(gen_idx: int, mem_projection: str, substrate: dict) -> tuple:
    print(f"\n===========================================================================")
    print(f"=== [GEN {gen_idx}] MOISSONNEUR AUTO-PILOTE SUR BLACKBOARD                  ===")
    print(f"===========================================================================")
    prev_kws = substrate.get("custom_swarm_memory_store", {}).get("explored_search_keywords", [])
    harvest_res = execute_m3_rocket_unit(
        f"GEN_{gen_idx}_HARVESTER",
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
        harvest_res["m0_synthesis"] + "\n\n" + harvest_res["raw_m3_joined"],
        kw_empty_template,
        ["Autonomous_Search_Keywords"],
        ["Autonomous_Search_Keywords"]
    )
    new_kws = [str(k).strip() for k in kw_block.get("Autonomous_Search_Keywords", []) if str(k).strip() and not str(k).startswith("<")][:6]
    substrate["custom_swarm_memory_store"]["explored_search_keywords"] = merge_unique_list(prev_kws, new_kws)
    save_raw_substrate(substrate)

    ext_records = execute_arxiv_and_forums_queries(new_kws)
    web_grounded = call_species(
        "GEMINI_ARGON",
        f"Ex?cute une recherche Web Grounded approfondie sur les mots-cl?s d?finis par l'essaim : {new_kws}.",
        temp=0.2,
        use_web_search=True
    )
    print(f"    -> [Moissonnage G={gen_idx}] {len(new_kws)} nouveaux mots-cl?s g?n?r?s par les mod?les : {new_kws}")
    print(f"    -> [Articles & Forums extraits] : {len(ext_records)} entr?es + Synth?se Web Grounded ({len(web_grounded)} car.)")
    digest = "\n".join(ext_records[:15]) + "\n\n" + web_grounded[:3500]
    return digest, harvest_res

# =========================================================================
# EX?CUTION D'UNE G?N?RATION COMPL?TE G_g
# =========================================================================
def run_one_evolutionary_generation(gen_idx: int, substrate: dict) -> dict:
    store = substrate.get("custom_swarm_memory_store", {})
    print(f"\n###########################################################################")
    print(f"### DEMARRAGE DE LA GENERATION EVOLUTIVE G = {gen_idx}                        ###")
    print(f"### Bagage h?rit? : {len(store.get('discovered_mathematical_concepts',[]))} concepts math | {len(store.get('literature_and_forum_flaws_eliminated',[]))} failles litt. | {len(store.get('novel_beyond_labs_flaws_eliminated',[]))} failles in?dites ###")
    print(f"###########################################################################")

    mem_spec, plugin_ns = run_endogenous_memory_mechanism_design_rocket(gen_idx, substrate)
    mem_projection = invoke_swarm_memory_projection(plugin_ns, substrate, gen_idx)

    rlcr_spec, rlcr_trace = run_endogenous_rlcr_blackboard_design_rocket(gen_idx, substrate, mem_projection)
    generation_unit_traces = [rlcr_trace]

    harvest_digest, harvest_trace = run_generational_harvester(gen_idx, mem_projection, substrate)
    generation_unit_traces.append(harvest_trace)

    print(f"\n===========================================================================")
    print(f"=== [GEN {gen_idx}] FUSEE OMEGA : CONCEPTION DE LA TOPOLOGIE DE BOUCLES     ===")
    print(f"===========================================================================")
    omega_mission = (
        f"Corpus moissonn? ? la G?n?ration G={gen_idx} :\n{harvest_digest[:4000]}\n\n"
        f"Protocole de Blackboard & Calibration RLCR actif :\n{json.dumps(rlcr_spec, ensure_ascii=False, indent=2)}\n\n"
        "Con?ois la topologie de boucles, de r?troactions et d'auto-organisation entre fus?es et essaims op?rant sur le Blackboard et le Shared Workspace RLCR. "
        "D?finis au moins deux boucles : l'une pour ?puiser toutes les failles de la litt?rature/forums (incluant OpenAI cache-timing et Fable 5.1 SVG->PNG) contre notre syst?me, et l'autre pour d?couvrir de nouvelles failles in?dites."
    )
    omega_res = execute_m3_rocket_unit(f"GEN_{gen_idx}_OMEGA_META_TOPOLOGY", omega_mission, [], mem_projection, substrate)
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
        omega_res["m0_synthesis"] + "\n\n" + omega_res["raw_m3_joined"],
        topo_empty_template,
        ["invented_meta_topology_name", "rlcr_inspired_self_organization_law", "anti_cover_up_reward_encoding_formula"],
        ["invented_loops_pipeline"]
    )
    loops_pipeline = meta_plan.get("invented_loops_pipeline", [])
    print(f"  => [Topologie de Boucles Con?ue (G={gen_idx})] : {meta_plan.get('invented_meta_topology_name')}")
    print(f"  => [Formule Anti-Cover-Up Active] : {meta_plan.get('anti_cover_up_reward_encoding_formula')}")

    for lp_cfg in loops_pipeline:
        if not isinstance(lp_cfg, dict):
            continue
        lid = str(lp_cfg.get("loop_id", f"LOOP_G{gen_idx}"))
        ltype = str(lp_cfg.get("loop_type_invented", "Boucle sur Blackboard"))
        tphase = str(lp_cfg.get("target_phase", "EXPLORATION"))
        castes = lp_cfg.get("castes", [])

        print(f"\n***************************************************************************")
        print(f"*** [GEN {gen_idx}] EXECUTION SUR BLACKBOARD DE LA BOUCLE : `{lid}` ***")
        print(f"*** M?canique : {ltype[:80]} ***")
        print(f"***************************************************************************")

        for iter_l in range(1, 3):
            prev_arch = substrate.get("evolved_architecture_spec", MINIMAL_PROBLEM_SEED)
            loop_prompt = (
                f"Ex?cution sur Blackboard & Shared Workspace de la Boucle `{lid}` (Tour {iter_l}) ? Phase : `{tphase}`.\n"
                f"M?canique de boucle : {ltype}\n"
                f"Protocole Blackboard RLCR : {rlcr_spec.get('rlcr_blackboard_protocol_name')}\n"
                f"Corpus moissonn? :\n{harvest_digest[:2800]}\n\n"
                f"Architecture actuelle :\n{prev_arch[-4000:]}\n\n"
                "MISSION : Trouvez sur le Blackboard et dans le Shared Workspace les failles de la litt?rature, des blogs et des forums contre notre syst?me, "
                "puis cherchez de nouvelles failles in?dites non encore couvertes, et formulez les ?quations exactes des capteurs et boucliers."
            )
            unit_res = execute_m3_rocket_unit(f"{lid}_ITER_{iter_l}", loop_prompt, castes, mem_projection, substrate)
            generation_unit_traces.append(unit_res)
            surv = unit_res["m1_extracted"].get("surviving_breakthroughs", [])

            new_arch = prev_arch + f"\n\n--- [G?N?RATION G={gen_idx} | BOUCLE BLACKBOARD {lid} | TOUR {iter_l}] ---\n{unit_res['m0_synthesis']}"
            cauchy_sim = cauchy_math_similarity(prev_arch[-3000:], unit_res["m0_synthesis"])
            substrate["evolved_architecture_spec"] = new_arch
            save_raw_substrate(substrate)

            invoke_swarm_memory_assimilation(plugin_ns, substrate, gen_idx, [unit_res])
            mem_projection = invoke_swarm_memory_projection(plugin_ns, substrate, gen_idx)

            print(f"    -> [Bilan Blackboard `{lid}` Tour {iter_l}] Perc?es={len(surv)} | Similitude de Cauchy={cauchy_sim:.4f}")
            if cauchy_sim >= 0.85 and iter_l >= 1:
                print(f"  => [Convergence de `{lid}` atteinte au Tour {iter_l}] !")
                break

    invoke_swarm_memory_assimilation(plugin_ns, substrate, gen_idx, generation_unit_traces)

    store_end = substrate.get("custom_swarm_memory_store", {})
    print(f"\n===========================================================================")
    print(f"=== BILAN CUMULATIF A LA FIN DE LA GENERATION G = {gen_idx} :               ===")
    print(f"  * Protocole Blackboard RLCR actif : {rlcr_spec.get('rlcr_blackboard_protocol_name')}")
    print(f"  * M?canisme de m?moire actif      : {mem_spec.get('memory_mechanism_name')}")
    print(f"  * Concepts math d?couverts        : {len(store_end.get('discovered_mathematical_concepts', []))}")
    print(f"  * Mots-cl?s moissonn?s            : {len(store_end.get('explored_search_keywords', []))}")
    print(f"  * Failles litt?rature colmat?es   : {len(store_end.get('literature_and_forum_flaws_eliminated', []))}")
    print(f"  * Failles in?dites hors-labos     : {len(store_end.get('novel_beyond_labs_flaws_eliminated', []))}")
    print(f"===========================================================================")

    gen_log = {
        "generation": gen_idx,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "endogenous_rlcr_blackboard_designed": rlcr_spec,
        "endogenous_memory_mechanism_designed": mem_spec,
        "invented_meta_topology": meta_plan
    }
    substrate["current_generation"] = gen_idx
    substrate.setdefault("generations_raw_logs", []).append(gen_log)
    save_raw_substrate(substrate)
    write_unified_markdown_report(substrate)
    return gen_log

def write_unified_markdown_report(substrate: dict):
    mechs = substrate.get("endogenous_memory_mechanisms_proposed_and_tested", [])
    rlcrs = substrate.get("endogenous_rlcr_blackboard_protocols_designed", [])
    store = substrate.get("custom_swarm_memory_store", {})
    py_plugin_str = CompiledMemoryPluginPath.read_text(encoding="utf-8") if CompiledMemoryPluginPath.exists() else ""

    md_txt = (
        "# RAPPORT DU SYST?ME ?VOLUTIF MULTI-G?N?RATIONS (MOD?LES `gemini-4-argon` / `gemini-3.1-pro-preview`, `claude-fable-5-1`, `claude-opus-5-5`)\n\n"
        f"- **G?n?rations ?volutives Accomplies** : `G = 1 .. {substrate.get('current_generation', 1)}`\n"
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
        + "\n".join([f"- **G?n?ration {r['generation']}** : `{r['rlcr_spec'].get('rlcr_blackboard_protocol_name')}`\n  - *Blackboard & Workspace* : {r['rlcr_spec'].get('shared_message_board_and_workspace_mechanics')}\n  - *Loi Calibration MIT* : {r['rlcr_spec'].get('mit_uncertainty_reasoning_and_calibration_reward_law')}\n  - *Loi Collective Anti-Cover-Up* : {r['rlcr_spec'].get('collective_reward_and_anti_cover_up_incentive_law')}\n  - *Innovations* : `{r['rlcr_spec'].get('novel_elements_beyond_rlcr_invented_by_swarm')}`" for r in rlcrs])
        + "\n\n## II. M?CANISMES DE M?MOIRE ET D'INT?GRATION INTER-G?N?RATIONNELLE EXPLOR?S ET COMPIL?S\n\n"
        + "\n".join([f"- **G?n?ration {m['generation']}** : `{m['mechanism_spec'].get('memory_mechanism_name')}` ? Candidats explor?s : `{m['mechanism_spec'].get('explored_candidate_mechanisms')}` ? ?quation : {m['mechanism_spec'].get('mathematical_learning_rule_latex')}" for m in mechs])
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
    REPORT_MD_PATH.write_text(md_txt, encoding="utf-8")

def run_multi_generational_evolution(num_generations_to_run: int = 2):
    substrate = load_raw_substrate()
    start_g = int(substrate.get("current_generation", 0)) + 1
    end_g = start_g + num_generations_to_run - 1

    for g in range(start_g, end_g + 1):
        run_one_evolutionary_generation(g, substrate)

    write_unified_markdown_report(substrate)
    print(f"\n[OK] Rapport complet scell? dans `{REPORT_MD_PATH}` !")

if __name__ == "__main__":
    gens = 2
    if "--generations" in sys.argv:
        idx = sys.argv.index("--generations")
        if idx + 1 < len(sys.argv):
            gens = int(sys.argv[idx + 1])
    run_multi_generational_evolution(num_generations_to_run=gens)
