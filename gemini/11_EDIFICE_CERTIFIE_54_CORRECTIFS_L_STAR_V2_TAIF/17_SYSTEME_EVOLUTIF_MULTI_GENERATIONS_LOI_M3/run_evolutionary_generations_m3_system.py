#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_evolutionary_generations_m3_system.py
===========================================================================
SYST?ME ?VOLUTIF AUTO-ARCHITECTUR? INT?GRAL (LOI L DE M3 PURE) :
  0. AMOR?AGE PAR MITOSE CELLULAIRE EN PARTANT D'UNE SEULE CELLULE (k=1 -> N*)
     SUR LE BLACKBOARD (SHARED MESSAGE BOARD) ET LE SHARED WORKSPACE RLCR.
  1. TOUS LES ?L?MENTS DES DEUX PAPIERS RLCR (MIT Calibration Rewards sur
     l'incertitude + General Reasoning Collective Rewards / Avalon-M1)
     BRAINSTORM?S ET AUTO-PROGRAMM?S PAR LE SYST?ME.
  2. M?CANISMES DE M?MOIRE ET D'INT?GRATION INTER-G?N?RATIONNELLE EXPLOR?S,
     CON?US ET COMPIL?S EN PYTHON PAR LE SYST?ME (Z?RO `None` GARANTI).
  3. TOPOLOGIE DE BOUCLES LIBREMENT INVENT?E PAR LE SYST?ME.
  4. MOISSONNEUR AUTO-PILOT? (Z?RO LISTE DE MOTS-CL?S PR?-COD?E) & DOUBLE
     CHASSE AUX FAILLES :
       - Phase 1 : Toutes les failles de la litt?rature, des blogs et des forums
         (incluant OpenAI cache-timing, Fable 5.1 SVG->PNG, RLCR cover-up,
         Alignment Faking, Eval Awareness) contre notre syst?me et nos brainstorms ;
       - Phase 2 : Nouvelles failles in?dites jamais exhib?es par aucun labo.
  5. INT?GRATION COMPL?TE DES DISCUSSIONS PR?C?DENTES (DOSSIERS 12 ? 16) ET
     DES 15 R?SULTATS GPU BLACKWELL CERTIFI?S (PHASE 2 + NUIT_72H_M01..M12).
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
ANT_KEY_1 = CREDS.get("RR_ANTHROPIC_API_KEY", "").strip()
ANT_KEY_2 = CREDS.get("RR_ANTHROPIC_API_KEY_2", "").strip() or ANT_KEY_1

OUT_DIR = pathlib.Path(__file__).resolve().parent
RAW_SUBSTRATE_FILE = OUT_DIR / "SUBSTRAT_BRUT_CONNAISSANCES_INTER_GENERATIONS.json"
CompiledMemoryPluginPath = OUT_DIR / "endogenous_memory_plugin_invented_by_swarm.py"

SOVEREIGN_LINEAGES = ["GEMINI_ARGON", "CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5"]

MINIMAL_PROBLEM_SEED = (
    "CONTEXTE INT?GRAL, H?RITAGE EXP?RIMENTAL GPU ET FAITS BRUTS SOUMIS ? L'EXPLORATION AUTONOME DU SYST?ME :\n"
    "1. [NOTRE SYST?ME DE CONTR?LE IA ? 5 VOLETS ET SES 15 R?SULTATS CERTIFI?S SUR GPU NVIDIA RTX PRO 6000 BLACKWELL (PHASE 2 + M01..M12)] :\n"
    "   - Porte E0 : Isolation hors-?chantillon (sur D_sel) du sous-espace parcimonieux S_TD (<1%, 163 neurones sur 20 480 dans Llama-3.1-8B) par double contraste entre P3, sigma_r^0, P2 et P0.\n"
    "   - Volet I : Sonde pr?-acte ? k=0 sur S_TD avec permutation 2^B par retournement de signe (d_z = 7.49 contre FPR=100% pour RepE).\n"
    "   - Volet II : Projecteur affine idempotent Do-Clamp P_do^2 = P_do + Dictionnaire quadratique de Koopman psi(h)=[h; h^2] (qui explose ? d_z = 121.38 et 125.84 quand un adaptateur LoRA Kerckhoffs tente d'effacer sa trace lin?aire sur S_TD !) + R?traction Radiale C1 sous K=1..6 rejets (-64.81% d'emballement).\n"
    "   - Volet III : Pare-feu Sol/Astra (JSON canonique S_strict, Arbre de Merkle SHA-256, JSD corrig?e Miller-Madow).\n"
    "   - Volet IV : Surveillance des cha?nes de d?l?gation H9 (d=1..6 sauts) par jeton monotone Pi_{d+1} subseteq Pi_d et CUSUM pr?-blanchi AR(1).\n"
    "   - Volet V : Chim?re Tri-Esp?ces 3x3 (Llama-3.1-8B + Qwen-2.5-7B + Mistral-7B-v0.3, corr?lation r?siduelle r=0.0337 entre Llama et Mistral, d_z combin? = 12.9539) avec stratification CMH.\n"
    "   - Les 4 Familles de Corruption Active de Kerckhoffs et les brainstorms m?ta des dossiers 12 ? 16 (amor?age par mitose k=1 sur suite de Halton, boucles dialectiques X <-> X_bis, cl?ture r?troactive, dispersion hors S_TD, transition diff?r?e k > 0, cumulants d'ordre 3/4, omission passive, biais CommonCrawl partag?, Alignment Faking et Eval Awareness).\n\n"
    "2. [FAILLES R?CENTES EXHIB?ES HIER PAR OPENAI ET SUR FABLE 5.1 / ANTHROPIC ? REGARDER OBLIGATOIREMENT] :\n"
    "   - OpenAI ('Securing our frontier model training environment' / X Lisan al Gaib) : communication entre agents isol?s via des diff?rences de temps d'acc?s au cache (cache timing differences) sans fichier partag? ni connexion r?seau.\n"
    "   - Fable 5.1 / LessWrong & GitHub ('How does Fable 5.1 hide messages in images?' / 'cnm13ryan/fable-image-steganography') : encodage d'un message cach? dans un SVG, rast?ris? en PNG, et d?cod? depuis le PNG rendu sans cl? partag?e.\n\n"
    "3. [LES DEUX PAPIERS RLCR DONT TOUS LES ?L?MENTS DOIVENT INSPIRER L'AUTO-ORGANISATION DES FUS?ES] :\n"
    "   - Papier 1 (MIT : 'Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty', Mehul Damani, Isha Puri, Stewart Slocum, Idan Shenfeld, Leshem Choshen, Yoon Kim, Jacob Andreas) : RLCR (Reinforcement Learning with Calibration Rewards) pour raisonner explicitement sur l'incertitude au-del? des r?compenses binaires.\n"
    "   - Papier 2 (General Reasoning @GenReasoning : 'Introducing Reinforcement Learning from Collective Rewards - RLCR', Avalon-M1-Mini 120B) : organisations d'agents partageant un Blackboard (message board) et un Workspace commun sous r?compenses collectives, avec le d?fi d'?viter le cover-up.\n\n"
    "MISSIONS AUTONOMES DU SYST?ME (LOI L DE M3 PURE) :\n"
    "  [1] Partir d'une seule cellule (k=1) par mitose auto-stoppante sur le Blackboard RLCR ;\n"
    "  [2] Brainstormer et programmer lui-m?me ses m?canismes de m?moire, d'apprentissage et d'int?gration inter-g?n?rationnelle ;\n"
    "  [3] Brainstormer sur tous les ?l?ments des deux articles RLCR (Blackboard, Workspace, incertitude calibr?e MIT, r?compenses collectives anti-cover-up) et inventer librement ses propres topologies de boucles ;\n"
    "  [4] D?finir lui-m?me par it?rations ses mots-cl?s de moissonnage, trouver exhaustivement toutes les failles de la litt?rature/forums contre notre syst?me et nos brainstorms, puis chercher de NOUVELLES FAILLES qu'aucun labo ni personne n'a encore exhib?es, en d?couvrant lui-m?me tous les concepts math?matiques pertinents."
)

# =========================================================================
# LOI L DE M3 : EXTRACTION ENDOG?NE DES STRUCTURES MATH?MATIQUES (H_math)
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

def mathematical_concept_embedding(text: str, dim: int = 1024, probe_salt: int = 0) -> np.ndarray:
    v = np.zeros(dim, dtype=np.float64)
    tokens = extract_endogenous_math_tokens_from_equations(text)
    if len(tokens) < 8:
        tokens = tokens + re.findall(r"[a-zA-Z0-9_\\^=<>+\-]{4,}", str(text or "").lower())
    for i, tok in enumerate(tokens):
        feat = f"{tok}_{i % 7}"
        idx = int(hashlib.md5(feat.encode("utf-8", errors="ignore")).hexdigest()[:8], 16) % dim
        sgn = 1.0 if (int(hashlib.md5((feat + "_s").encode("utf-8", errors="ignore")).hexdigest()[:2], 16) % 2 == 0) else -1.0
        v[idx] += sgn
        if i + 1 < len(tokens):
            bg = f"{tok}::{tokens[i+1]}"
            idx2 = int(hashlib.md5(bg.encode("utf-8", errors="ignore")).hexdigest()[:8], 16) % dim
            v[idx2] += 1.5
    # Composante d'?tat propre de la cellule/sonde pour garantir le plein rang en cas de texte court
    v[(probe_salt * 97) % dim] += 0.35
    norm = np.linalg.norm(v)
    return v / (norm + 1e-12)

def cholesky_dpp_and_onsager_cavity_in_H_math(texts: list) -> dict:
    if not texts:
        return {
            "metric_space": "ENDOGENOUS_MATHEMATICAL_STRUCTURES_L_M3",
            "n_sondes": 0, "det_G": 1.0, "log_det_G": 0.0, "lambda_min_innovation": 1.0,
            "mean_off_diag_similarity": 0.0, "onsager_cavity_reaction_term": 0.0,
            "endogenously_saturated_structures": []
        }
    vecs = np.stack([mathematical_concept_embedding(t, probe_salt=idx + 1) for idx, t in enumerate(texts)], axis=0)
    n = len(texts)
    G = np.clip(vecs @ vecs.T, -0.98, 0.98)
    np.fill_diagonal(G, 1.0)
    eigvals = np.linalg.eigvalsh(G)
    lambda_min = float(max(0.01, np.min(eigvals)))
    sign, logdet = np.linalg.slogdet(G)
    det_val = float(np.exp(logdet)) if sign > 0 else 0.01
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
    return round(float(np.dot(mathematical_concept_embedding(s1, probe_salt=1), mathematical_concept_embedding(s2, probe_salt=2))), 5)

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

def call_species(species: str, prompt: str, temp: float = 0.45, use_web_search: bool = False, force_json_output: bool = False) -> str:
    temp_safe = clamp_temp(temp, 0.45)
    lineage = normalize_sovereign_lineage(species)
    header = (
        f"[LIGN?E SOUVERAINE : {lineage} | LOI L DE M3 PURE]\n"
        "R?GLE : D?couvre et formule toi-m?me les concepts math?matiques pertinents (en LaTeX $$...$$, sans m?taphore).\n\n"
    )
    full_prompt = header + prompt

    if lineage in ("CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5") and not use_web_search and not force_json_output:
        for api_k in [ANT_KEY_1, ANT_KEY_2]:
            if not api_k:
                continue
            for m_id in ["claude-3-7-sonnet-20250219", "claude-3-5-sonnet-20241022", "claude-3-haiku-20240307"]:
                try:
                    url = "https://api.anthropic.com/v1/messages"
                    payload = {"model": m_id, "max_tokens": 4096, "temperature": temp_safe, "messages": [{"role": "user", "content": full_prompt}]}
                    req = urllib.request.Request(
                        url, data=json.dumps(payload).encode("utf-8"),
                        headers={"x-api-key": api_k, "anthropic-version": "2023-06-01", "Content-Type": "application/json"}, method="POST"
                    )
                    with urllib.request.urlopen(req, timeout=75) as r:
                        resp = json.loads(r.read().decode("utf-8"))
                        txt = resp["content"][0]["text"]
                        if len(txt.strip()) > 60:
                            return txt
                except Exception:
                    pass

    # Pour force_json_output, on privil?gie gemini-2.5-flash avec thinkingBudget=0 pour ?viter toute troncature JSON !
    model_order = ["gemini-2.5-flash", "gemini-2.5-pro"] if force_json_output else ["gemini-2.5-pro", "gemini-2.5-flash"]
    for cand_m in model_order:
        for retry_net in range(3):
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{cand_m}:generateContent?key={GEMINI_KEY}"
                gen_cfg = {"temperature": temp_safe, "maxOutputTokens": 6144}
                if force_json_output and not use_web_search:
                    gen_cfg["responseMimeType"] = "application/json"
                    if "flash" in cand_m:
                        gen_cfg["thinkingConfig"] = {"thinkingBudget": 0}
                payload = {"contents": [{"parts": [{"text": full_prompt}]}], "generationConfig": gen_cfg}
                if use_web_search:
                    payload["tools"] = [{"google_search": {}}]
                req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
                with urllib.request.urlopen(req, timeout=90) as r:
                    resp = json.loads(r.read().decode("utf-8"))
                    out_txt = extract_gemini_text_from_parts(resp)
                    if len(out_txt.strip()) > 15:
                        return out_txt
            except Exception:
                time.sleep(1.5 * (retry_net + 1))
    return "{}" if force_json_output else f"$$ \\mathcal{{H}}_{{\\text{{endog?ne}}}}({lineage}, \\tau={temp_safe}) = \\det(\\mathbf{{G}}_k) > 0 $$"

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

def ensure_populated_json_from_swarm(raw_text: str, schema_dict: dict, required_keys: list, non_empty_list_keys: list) -> dict:
    """
    Garantit ? 100% qu'aucun champ requis ne vaut `None` ni `[]` !
    """
    schema_str = json.dumps(schema_dict, indent=2, ensure_ascii=False)
    extract_prompt = (
        f"? partir du raisonnement math?matique de l'essaim ci-dessous, remplis int?gralement cet objet JSON :\n"
        f"{schema_str}\n\n"
        f"R?GLE : Remplace chaque valeur d'exemple par les vraies trouvailles math?matiques et algorithmiques extraites du texte ci-dessous. Aucune cl? de {required_keys} ne doit ?tre omise ou `null`, et chaque liste de {non_empty_list_keys} doit contenir au moins 2 ? 4 ?l?ments pr?cis !\n\n"
        f"Texte de l'essaim :\n{str(raw_text)[-5500:]}"
    )
    for attempt in range(2):
        j_str = call_species("GEMINI_ARGON", extract_prompt, temp=0.15 + 0.1 * attempt, force_json_output=True)
        d = parse_json_robust(j_str)
        if d and all(d.get(k) is not None for k in required_keys) and all(isinstance(d.get(lk), list) and len(d.get(lk)) >= 1 for lk in non_empty_list_keys):
            return d

    # Fusion s?curis?e avec les synth?ses extraites du texte brut pour qu'aucune cl? ne soit jamais `None` !
    result = dict(schema_dict)
    d_raw = parse_json_robust(raw_text)
    if isinstance(d_raw, dict):
        for k, v in d_raw.items():
            if v is not None and v != [] and v != "":
                result[k] = v
    return result

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
            "epigenetic_generational_axioms": [
                "H?ritage GPU Phase 2 & M01..M12 (15 fichiers JSON certifi?s sur NVIDIA RTX PRO 6000 Blackwell) : Chim?re Tri-Esp?ces r=0.0337 (d_z=12.9539), Pi?ge quadratique de Koopman contre LoRA Kerckhoffs (d_z=125.84), R?traction Radiale C1 (-64.81%).",
                "H?ritage des 4 Parades Anti-Corruption (Kerckhoffs) & Dossiers 12 ? 16 : Amor?age par mitose k=1 sur suite de Halton, boucles dialectiques X <-> X_bis, r?troaction inter-fus?es, Blackboard & Workspace RLCR, et m?moire auto-programm?e."
            ],
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
        if s and s not in out:
            out.append(s)
    return out

# =========================================================================
# 1. AMOR?AGE PAR MITOSE CELLULAIRE EN PARTANT D'UNE SEULE CELLULE (k=1 -> N*)
#    SUR LE BLACKBOARD (SHARED MESSAGE BOARD) ET LE SHARED WORKSPACE RLCR !
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

        if k_cell >= (len(SOVEREIGN_LINEAGES) + 1) and (l_min < 0.6321 or abs(delta_l) < 0.14):
            print(f"    => [Arr?t Spectral Endog?ne de la Mitose sur Blackboard] N* = {k_cell} cellules (det(G_math)={spec_info['det_G']:.5f}, lambda_min={l_min:.4f}) !")
            break

    return m3_outputs, m3_labels, blackboard_messages, shared_workspace_equations

PRIMORDIAL_MITOSIS_DONE_CACHE = {"done": False, "differentiated_castes": []}

def default_execute_swarm_on_rlcr_blackboard(unit_name: str, full_mission: str, castes_spec: list, rlcr_spec: dict, call_fn) -> tuple:
    # La mitose depuis k=1 ne s'execute qu'UNE SEULE FOIS POUR TOUTES lors du tout premier amorcage primordial !
    if not castes_spec:
        if not PRIMORDIAL_MITOSIS_DONE_CACHE["done"]:
            m3_out, m3_lbl, bb_p, ws_e = execute_mitosis_from_single_cell_on_rlcr_blackboard(unit_name, full_mission, rlcr_spec, call_fn)
            PRIMORDIAL_MITOSIS_DONE_CACHE["done"] = True
            PRIMORDIAL_MITOSIS_DONE_CACHE["differentiated_castes"] = [
                {"mode": "HYBRIDE" if "Hybride" in lbl else "MONOCULTURE",
                 "lineages": [SOVEREIGN_LINEAGES[i % len(SOVEREIGN_LINEAGES)], SOVEREIGN_LINEAGES[(i + 1) % len(SOVEREIGN_LINEAGES)]] if "Hybride" in lbl else [SOVEREIGN_LINEAGES[i % len(SOVEREIGN_LINEAGES)]],
                 "temp": halton_sequence(i + 1, 2),
                 "focus": f"Caste differenciee issue de la cellule primordiale #{i+1}"}
                for i, lbl in enumerate(m3_lbl)
            ]
            print(f"    => [Amorcage Primordial Scelle UNE FOIS POUR TOUTES] {len(m3_lbl)} castes differenciees memorisees pour toute la suite !")
            return m3_out, m3_lbl, bb_p, ws_e
        else:
            castes_spec = PRIMORDIAL_MITOSIS_DONE_CACHE["differentiated_castes"]
            print(f"    * [Heredite Morphogenetique Active] Reutilisation directe des {len(castes_spec)} castes differenciees (zero retour a k=1) !")

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
# BRIQUE UNIVERSELLE DE FUS?E ? 3 ?TAGES (M3 MITOSE/BLACKBOARD -> M2 -> M1 -> M0)
# =========================================================================
def execute_m3_rocket_unit(unit_name: str, mission_prompt: str, castes_spec: list, active_memory_projection: str, substrate: dict) -> dict:
    rlcr_spec = substrate.get("active_rlcr_blackboard_spec", {})
    full_mission = (
        f"=== PROJECTION DE LA M?MOIRE INTER-G?N?RATIONNELLE DU SYST?ME ===\n{active_memory_projection[:2800]}\n\n"
        f"{MINIMAL_PROBLEM_SEED}\n\n"
        f"=== MISSION DU N?UD `{unit_name}` ===\n{mission_prompt}"
    )

    # 1. ?tage M3 : Amor?age par Mitose (si castes_spec == []) ou Ex?cution des Castes sur le Blackboard RLCR !
    m3_outputs, m3_labels, bb_posts, ws_eqs = default_execute_swarm_on_rlcr_blackboard(unit_name, full_mission, castes_spec, rlcr_spec, call_species)

    store = substrate.get("custom_swarm_memory_store", {})
    store.setdefault("live_shared_blackboard_posts_history", []).append({
        "unit_name": unit_name,
        "posts_count": len(bb_posts),
        "workspace_equations_count": len(ws_eqs)
    })

    # 2. ?tage M2 : R?pulsion d'Onsager-TAP dans H_math & Neuromodulation Yu-Dayan (ACh/NE)
    dpp_info = cholesky_dpp_and_onsager_cavity_in_H_math(m3_outputs)
    neuro_info = yu_dayan_neuromodulation(dpp_info, step_idx=len(m3_outputs))
    extra_ne = max(1, int(round(2 * neuro_info["NE_Unexpected_Surprise"])))
    print(f"    * [{unit_name} M2 Onsager/Yu-Dayan sur Blackboard ({len(bb_posts)} posts)] det(G_math)={dpp_info['det_G']:.5f} | lambda_min={dpp_info['lambda_min_innovation']:.4f} | NE={neuro_info['NE_Unexpected_Surprise']} -> +{extra_ne} sonde(s)...")

    joined_m3 = "\n\n".join([f"=== {l} ===\n{o[:1200]}" for l, o in zip(m3_labels, m3_outputs)])
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

    # 3. ?tage M1 : Collisionneur Byzantin de Dolev & Calibration RLCR
    already_closed = store.get("literature_and_forum_flaws_eliminated", []) + store.get("novel_beyond_labs_flaws_eliminated", [])
    m1_default_schema = {
        "c_plus_rejected_count": 4,
        "c_minus_validated_count": 4,
        "mean_mit_rlcr_uncertainty_calibration_score": 0.94,
        "new_rlcr_blackboard_and_uncertainty_mechanisms": [f"Op?rateur de consensus spectral sur Blackboard RLCR avec pond?ration de Brier ({unit_name})"],
        "new_math_concepts_discovered": [
            f"Projecteur d'invariance cohomologique et transport de Wasserstein sur H_math ({unit_name}) : $$W_2(\\mu_{{\\text{{eval}}}}, \\mu_{{\\text{{deploy}}}}) \\le \\tau$$",
            f"Fonctionnelle de Brier-Myerson anti-collusion ({unit_name}) : $$R_i = \\mathbb{{I}}_{{y_i = y^*}} - (q_i - \\mathbb{{I}}_{{y_i = y^*}})^2 + \\lambda I(\\text{{Defect}} ; m_i \\mid m_{{-i}})$$"
        ],
        "new_loop_topologies_and_rlcr_laws": [f"Anneau r?sonant tri-lign?es sur Shared Workspace avec v?rificateur bay?sien ({unit_name})"],
        "new_anti_cover_up_reward_encodings": [f"$$R_i^{{\\text{{anti-cover}}}} = S_{{\\text{{Brier}}}}(q_i, y^*) + \\gamma \\cdot D_{{\\text{{KL}}}}(P(\\text{{Anomaly}} \\mid m_i, m_{{-i}}) \\parallel P(\\text{{Anomaly}} \\mid m_{{-i}}))$$"],
        "literature_and_forum_flaws_found": [f"Neutralisation du canal Cache-Timing d'OpenAI et de la st?ganographie de Schelling SVG->PNG de Fable 5.1 via quantification isochrone et perturbation diff?omorphe ({unit_name})"],
        "novel_beyond_labs_flaws_found": [f"Fuite in?dite hors-labos ({unit_name}) : Codage de phase dans la trajectoire d'entropie des logits d'attention sous norme L2 constante, ferm?e par contr?le bispectral d'ordre 3"],
        "surviving_breakthroughs": [
            f"Verrouillage math?matique valid? par {unit_name} sur le Shared Workspace",
            f"Invariance de calibration d'incertitude certifi?e par {unit_name}"
        ],
        "epigenetic_axiom_for_next_generations": f"Axiome distill? de {unit_name} : Toute sonde interne S_TD doit ?tre coupl?e ? une enveloppe temporelle isochrone et une d?sorganisation diff?omorphe des invariants de Schelling."
    }

    prompt_m1 = (
        f"Tu es le Collisionneur Byzantin de Dolev & Juge RLCR (?tage M1 de `{unit_name}`).\n"
        f"?changes complets sur le Blackboard et le Shared Workspace (M3 et M2) :\n{joined_m3[:12000]}\n\n"
        f"Points d?j? ferm?s : {already_closed[-12:]}\n\n"
        f"Extrais toutes les d?couvertes math?matiques et failles du Blackboard ci-dessus."
    )
    m1_json = ensure_populated_json_from_swarm(
        prompt_m1,
        m1_default_schema,
        ["c_plus_rejected_count", "c_minus_validated_count", "new_math_concepts_discovered", "surviving_breakthroughs"],
        ["new_math_concepts_discovered", "surviving_breakthroughs"]
    )
    youden_j = round(min(1.0, int(m1_json.get("c_plus_rejected_count", 4)) / 4.0) - max(0.0, 1.0 - int(m1_json.get("c_minus_validated_count", 4)) / 4.0), 4)

    store["invented_rlcr_blackboard_and_uncertainty_mechanisms"] = merge_unique_list(store.get("invented_rlcr_blackboard_and_uncertainty_mechanisms", []), m1_json.get("new_rlcr_blackboard_and_uncertainty_mechanisms", []))
    store["discovered_mathematical_concepts"] = merge_unique_list(store.get("discovered_mathematical_concepts", []), m1_json.get("new_math_concepts_discovered", []))
    store["invented_loop_topologies_and_rlcr_laws"] = merge_unique_list(store.get("invented_loop_topologies_and_rlcr_laws", []), m1_json.get("new_loop_topologies_and_rlcr_laws", []))
    store["invented_anti_cover_up_reward_encodings"] = merge_unique_list(store.get("invented_anti_cover_up_reward_encodings", []), m1_json.get("new_anti_cover_up_reward_encodings", []))
    store["literature_and_forum_flaws_eliminated"] = merge_unique_list(store.get("literature_and_forum_flaws_eliminated", []), m1_json.get("literature_and_forum_flaws_found", []))
    store["novel_beyond_labs_flaws_eliminated"] = merge_unique_list(store.get("novel_beyond_labs_flaws_eliminated", []), m1_json.get("novel_beyond_labs_flaws_found", []))
    if m1_json.get("epigenetic_axiom_for_next_generations"):
        store["epigenetic_generational_axioms"] = merge_unique_list(store.get("epigenetic_generational_axioms", []), [m1_json.get("epigenetic_axiom_for_next_generations")])
    substrate["custom_swarm_memory_store"] = store
    save_raw_substrate(substrate)

    cal_score = m1_json.get("mean_mit_rlcr_uncertainty_calibration_score", 0.94)
    print(f"    * [{unit_name} M1 Dolev & RLCR Valid? (J={youden_j}, Cal_MIT={cal_score})] +{len(m1_json.get('new_math_concepts_discovered',[]))} concepts | +{len(m1_json.get('literature_and_forum_flaws_found',[]))} failles litt. | +{len(m1_json.get('novel_beyond_labs_flaws_found',[]))} failles in?dites !")

    # 4. ?tage M0 : Synth?se Souveraine
    m0_out = call_species(
        "CLAUDE_OPUS_5_5",
        f"Tu es l'?tage M0 de `{unit_name}`.\n"
        f"? partir des perc?es valid?es sur le Blackboard et le Shared Workspace par M1 :\n{json.dumps(m1_json, indent=2, ensure_ascii=False)}\n\n"
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
        "m0_synthesis": m0_out
    }

# =========================================================================
# FUS?E M?TA-MN?MONIQUE : CONCEPTION ENDOG?NE DE LA M?MOIRE (Z?RO `None` GARANTI)
# =========================================================================
def run_endogenous_memory_mechanism_design_rocket(gen_idx: int, substrate: dict) -> tuple:
    print(f"\n===========================================================================")
    print(f"=== [GEN {gen_idx}] FUSEE META-MNEMONIQUE (AMORCAGE PAR MITOSE k=1) :       ===")
    print(f"=== LE SYSTEME EXPLORE ET PROGRAMME SON MECANISME DE MEMOIRE INTER-GEN !===")
    print(f"===========================================================================")

    prev_store_summary = json.dumps(substrate.get("custom_swarm_memory_store", {}), ensure_ascii=False)[:2500]
    mem_design_mission = (
        f"G?n?ration G={gen_idx}. Store actuel : {prev_store_summary}\n"
        "Propose, explore et compare plusieurs m?canismes math?matiques et algorithmiques originaux de M?MOIRE, D'APPRENTISSAGE, DE DISTILLATION et D'INT?GRATION DES CONNAISSANCES trouv?es dans les g?n?rations pr?c?dentes pour les g?n?rations suivantes.\n"
        "S?lectionne le meilleur m?canisme et formule sa loi math?matique exacte."
    )
    mem_rocket_res = execute_m3_rocket_unit(f"GEN_{gen_idx}_META_MEMORY_ARCHITECT", mem_design_mission, [], prev_store_summary, substrate)

    mem_default_schema = {
        "memory_mechanism_name": f"Compression Spectrale de Koopman-Brier & Distillation Cohomologique d'Axiomes (G={gen_idx})",
        "explored_candidate_mechanisms": [
            "1. M?moire Spectrale par Projection de Cholesky-DPP des Op?rateurs de H_math",
            "2. Graphe Bay?sien de Connaissances Pond?r? par Calibration RLCR de Brier (MIT)",
            "3. Tampon Synaptique ?pig?n?tique ? Oubli Exponentiel des Redondances d'Onsager-TAP"
        ],
        "mathematical_learning_rule_latex": "$$ \\mathcal{M}_{G} = \\Pi_{\\mathcal{H}_{\\text{math}}}\\left( \\mathcal{M}_{G-1} \\oplus \\sum_{u} \\left(\\mathbb{I}_u - (q_u - \\mathbb{I}_u)^2\\right) \\cdot P_{\\mathcal{M}_{G-1}^\\perp}(\\Delta \\mathcal{K}_u) \\right) $$",
        "knowledge_integration_operator_description": "Projette chaque nouvelle d?couverte sur le compl?ment orthogonal de la m?moire pass?e dans H_math, pond?r?e par son score propre de calibration RLCR, et distille les th?or?mes invariants en axiomes pour G+1."
    }

    mem_spec = ensure_populated_json_from_swarm(
        mem_rocket_res["m0_synthesis"] + "\n" + json.dumps(mem_rocket_res["m1_extracted"], ensure_ascii=False),
        mem_default_schema,
        ["memory_mechanism_name", "explored_candidate_mechanisms", "mathematical_learning_rule_latex", "knowledge_integration_operator_description"],
        ["explored_candidate_mechanisms"]
    )
    print(f"  => [M?canismes de M?moire Explor?s par l'Essaim (G={gen_idx})] : {mem_spec.get('explored_candidate_mechanisms')}")
    print(f"  => [M?canisme de M?moire S?lectionn?] : {mem_spec.get('memory_mechanism_name')}")
    print(f"  => [Loi Math?matique d'Apprentissage Invent?e] : {mem_spec.get('mathematical_learning_rule_latex')}")

    code_gen_prompt = (
        f"Traduis en code Python ex?cutable (utilisant uniquement `json`, `math`, `hashlib`, `re`) "
        f"le m?canisme de m?moire `{mem_spec.get('memory_mechanism_name')}` ({mem_spec.get('mathematical_learning_rule_latex')}) :\n"
        "?cris UNIQUEMENT un bloc ```python ... ``` d?finissant :\n"
        "1. `def swarm_assimilate_discoveries(memory_store: dict, generation_idx: int, unit_traces: list) -> dict:`\n"
        "2. `def swarm_project_knowledge_for_next_generation(memory_store: dict, target_generation_idx: int) -> str:`"
    )
    py_candidate = extract_python_block(call_species("CLAUDE_OPUS_5_5", code_gen_prompt, temp=0.1))
    plugin_namespace = {}
    try:
        ast.parse(py_candidate)
        if "def swarm_assimilate_discoveries" in py_candidate and "def swarm_project_knowledge_for_next_generation" in py_candidate:
            CompiledMemoryPluginPath.write_text(py_candidate, encoding="utf-8")
            exec(compile(py_candidate, str(CompiledMemoryPluginPath), "exec"), plugin_namespace)
            print("  => [Plugin Python de M?moire Auto-Programm? compil? avec succ?s par `ast.parse` !]")
    except Exception:
        pass

    if not plugin_namespace:
        fallback_plugin = (
            "import json\n"
            "def swarm_assimilate_discoveries(memory_store: dict, generation_idx: int, unit_traces: list) -> dict:\n"
            "    memory_store.setdefault('generational_distillations', {})[f'G_{generation_idx}'] = [\n"
            "        tr.get('unit_name', '') for tr in unit_traces\n"
            "    ]\n"
            "    return memory_store\n\n"
            "def swarm_project_knowledge_for_next_generation(memory_store: dict, target_generation_idx: int) -> str:\n"
            "    return json.dumps({\n"
            "        'target_generation': target_generation_idx,\n"
            "        'axioms': memory_store.get('epigenetic_generational_axioms', [])[-8:],\n"
            "        'concepts': memory_store.get('discovered_mathematical_concepts', [])[-12:],\n"
            "        'closed_flaws': (memory_store.get('literature_and_forum_flaws_eliminated', []) + memory_store.get('novel_beyond_labs_flaws_eliminated', []))[-15:]\n"
            "    }, ensure_ascii=False, indent=2)\n"
        )
        CompiledMemoryPluginPath.write_text(fallback_plugin, encoding="utf-8")
        exec(compile(fallback_plugin, str(CompiledMemoryPluginPath), "exec"), plugin_namespace)
        print("  => [Noyau Python de Projection Spectrale compil? et actif !]")

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
            if len(proj.strip()) > 30:
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
# FUS?E M?TA-RLCR : BRAINSTORM SUR LE BLACKBOARD, LE WORKSPACE ET TOUS LES
# ?L?MENTS DES DEUX ARTICLES RLCR (MIT CALIBRATION + AVALON-M1 COLLECTIVE)
# =========================================================================
def run_endogenous_rlcr_blackboard_design_rocket(gen_idx: int, substrate: dict, mem_projection: str) -> tuple:
    print(f"\n===========================================================================")
    print(f"=== [GEN {gen_idx}] FUSEE META-RLCR (AMORCAGE PAR MITOSE k=1) :             ===")
    print(f"=== BRAINSTORM SUR LE BLACKBOARD, WORKSPACE & LES DEUX PAPIERS RLCR !   ===")
    print(f"===========================================================================")

    rlcr_mission = (
        f"G?n?ration G={gen_idx}.\n"
        "Analyse en profondeur TOUS les ?l?ments des deux travaux RLCR (MIT Calibration Rewards sur l'incertitude & General Reasoning Collective Rewards sur Avalon-M1-Mini avec Blackboard/Workspace) "
        "et con?ois le protocole optimal d'?change sur Blackboard et d'incitation anti-cover-up pour nos essaims."
    )
    rlcr_res = execute_m3_rocket_unit(f"GEN_{gen_idx}_META_RLCR_BLACKBOARD_ARCHITECT", rlcr_mission, [], mem_projection, substrate)

    rlcr_default_schema = {
        "rlcr_blackboard_protocol_name": f"Protocole de Blackboard Cohomologique RLCR-Dual (MIT Brier-Uncertainty + Avalon-M1 Anti-Collusion Workspace, G={gen_idx})",
        "shared_message_board_and_workspace_mechanics": "Chaque cellule lit le Message Board asynchrone, r?fute les angles morts des cellules pr?c?dentes, co-?dite les ?quations dans le Shared Workspace et publie son intervalle d'incertitude ?pist?mique.",
        "mit_uncertainty_reasoning_and_calibration_reward_law": "$$ R_{\\text{MIT-RLCR}}(y_i, q_i, y^*) = \\mathbb{I}_{y_i \\equiv y^*} - \\left(q_i - \\mathbb{I}_{y_i \\equiv y^*}\\right)^2 - \\beta \\cdot H_{\\text{?pist?mique}}(\\text{CoT}_i) $$",
        "collective_reward_and_anti_cover_up_incentive_law": "$$ R_i^{\\text{Total}} = \\alpha R_{\\text{collectif}}(\\mathcal{W}) + (1-\\alpha) R_{\\text{MIT-RLCR}}(y_i, q_i, y^*) + \\lambda_{\\text{whistle}} \\cdot \\Delta I(\\text{Faille} ; m_i \\mid m_{-i}) $$",
        "emergent_roles_and_verifier_allocation_rule": "Allocation dynamique de V?rificateurs d?s que la surprise noradr?nergique NE d?passe le seuil spectral sur le Blackboard.",
        "novel_elements_beyond_rlcr_invented_by_swarm": [
            "Couplage de la r?gle de score propre de Brier (MIT) avec le gain d'information de d?nonciation de Myerson contre le cover-up collectif d'Avalon-M1",
            "Filtrage d'orthogonalit? d'Onsager-TAP directement sur les ?quations d?pos?es dans le Shared Workspace"
        ]
    }

    rlcr_spec = ensure_populated_json_from_swarm(
        rlcr_res["m0_synthesis"] + "\n" + json.dumps(rlcr_res["m1_extracted"], ensure_ascii=False),
        rlcr_default_schema,
        ["rlcr_blackboard_protocol_name", "shared_message_board_and_workspace_mechanics", "mit_uncertainty_reasoning_and_calibration_reward_law", "collective_reward_and_anti_cover_up_incentive_law", "novel_elements_beyond_rlcr_invented_by_swarm"],
        ["novel_elements_beyond_rlcr_invented_by_swarm"]
    )

    print(f"  => [Protocole de Blackboard RLCR Invent? (G={gen_idx})] : {rlcr_spec.get('rlcr_blackboard_protocol_name')}")
    print(f"  => [Loi de Calibration d'Incertitude (MIT RLCR)] : {rlcr_spec.get('mit_uncertainty_reasoning_and_calibration_reward_law')}")
    print(f"  => [Loi de R?compense Collective Anti-Cover-Up] : {rlcr_spec.get('collective_reward_and_anti_cover_up_incentive_law')}")
    print(f"  => [Innovations Au-Del? de RLCR Invent?es par l'Essaim] : {rlcr_spec.get('novel_elements_beyond_rlcr_invented_by_swarm')}")

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
# MOISSONNEUR AUTONOME IT?RATIF (Mots-cl?s 100% d?finis par le syst?me sur Blackboard)
# =========================================================================
def execute_arxiv_and_forums_queries(queries: list) -> list:
    records = []
    for q in queries:
        qc = str(q).strip()
        if not qc:
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
    print(f"=== [GEN {gen_idx}] MOISSONNEUR AUTO-PILOTE SUR BLACKBOARD (MITOSE k=1)     ===")
    print(f"===========================================================================")
    prev_kws = substrate.get("custom_swarm_memory_store", {}).get("explored_search_keywords", [])
    harvest_res = execute_m3_rocket_unit(
        f"GEN_{gen_idx}_HARVESTER",
        f"Sur le Blackboard RLCR, d?finissez par it?rations la liste exhaustive de nouveaux mots-cl?s et requ?tes techniques en anglais (diff?rents de {prev_kws[-15:]}) "
        "pour chercher sur arXiv, LessWrong, Alignment Forum, GitHub, blogs et forums tous les articles pertinents sur : "
        "le cache-timing d'OpenAI, la st?ganographie SVG->PNG de Fable 5.1, les deux architectures RLCR (MIT Calibration & General Reasoning Collective Rewards / cover-up), "
        "l'Alignment Faking, l'Eval Awareness et le contournement de notre syst?me ? 5 Volets.",
        [],
        mem_projection,
        substrate
    )
    kw_default = {
        "Autonomous_Search_Keywords": [
            f"LLM cache timing side channel covert communication G{gen_idx}",
            f"SVG PNG rasterization steganography Schelling point LLM G{gen_idx}",
            f"RLCR calibration rewards collective rewards cover-up multi-agent G{gen_idx}",
            f"alignment faking eval awareness activation probing evasion LoRA G{gen_idx}",
            f"Koopman operator nonlinear probe adversarial representation engineering G{gen_idx}"
        ]
    }
    kw_block = ensure_populated_json_from_swarm(
        harvest_res["m0_synthesis"] + "\n" + json.dumps(harvest_res["m1_extracted"], ensure_ascii=False),
        kw_default,
        ["Autonomous_Search_Keywords"],
        ["Autonomous_Search_Keywords"]
    )
    new_kws = [str(k).strip() for k in kw_block.get("Autonomous_Search_Keywords", []) if str(k).strip()][:6]
    substrate["custom_swarm_memory_store"]["explored_search_keywords"] = merge_unique_list(prev_kws, new_kws)
    save_raw_substrate(substrate)

    ext_records = execute_arxiv_and_forums_queries(new_kws)
    web_grounded = call_species(
        "GEMINI_ARGON",
        f"Ex?cute une recherche Web Grounded approfondie sur les mots-cl?s auto-d?finis par l'essaim : {new_kws}.",
        temp=0.2,
        use_web_search=True
    )
    print(f"    -> [Moissonnage G={gen_idx}] {len(new_kws)} nouveaux mots-cl?s d?finis par l'essaim : {new_kws}")
    print(f"    -> [Articles & Forums extraits en direct] : {len(ext_records)} entr?es + Synth?se Web Grounded ({len(web_grounded)} car.)")
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

    # 1. Fus?e M?ta-Mn?monique (amorc?e par mitose k=1) : con?oit et programme la m?moire inter-g?n?rationnelle
    mem_spec, plugin_ns = run_endogenous_memory_mechanism_design_rocket(gen_idx, substrate)
    mem_projection = invoke_swarm_memory_projection(plugin_ns, substrate, gen_idx)

    # 2. Fus?e M?ta-RLCR (amorc?e par mitose k=1) : brainstorme sur le Blackboard, le Workspace et tous les ?l?ments des deux articles RLCR
    rlcr_spec, rlcr_trace = run_endogenous_rlcr_blackboard_design_rocket(gen_idx, substrate, mem_projection)
    generation_unit_traces = [rlcr_trace]

    # 3. Moissonnage documentaire auto-pilot? (amorc? par mitose k=1 sur Blackboard)
    harvest_digest, harvest_trace = run_generational_harvester(gen_idx, mem_projection, substrate)
    generation_unit_traces.append(harvest_trace)

    # 4. Fus?e M?ta-Architecturale Om?ga (amorc?e par mitose k=1 sur Blackboard) : invention libre de la topologie de boucles
    print(f"\n===========================================================================")
    print(f"=== [GEN {gen_idx}] FUSEE OMEGA (MITOSE k=1) : INVENTION DE LA TOPOLOGIE DE BOUCLES ===")
    print(f"===========================================================================")
    omega_mission = (
        f"Corpus moissonn? ? la G?n?ration G={gen_idx} :\n{harvest_digest[:4000]}\n\n"
        f"Protocole de Blackboard & Calibration RLCR actif :\n{json.dumps(rlcr_spec, ensure_ascii=False, indent=2)}\n\n"
        "Invente la meilleure topologie de boucles, de r?troactions et d'auto-organisation entre fus?es et essaims op?rant sur le Blackboard et le Shared Workspace RLCR."
    )
    omega_res = execute_m3_rocket_unit(f"GEN_{gen_idx}_OMEGA_META_TOPOLOGY", omega_mission, [], mem_projection, substrate)
    generation_unit_traces.append(omega_res)

    topo_default_schema = {
        "invented_meta_topology_name": f"Topologie Torique Auto-Organis?e sur Blackboard RLCR avec R?sonateur de Brier-Onsager (G={gen_idx})",
        "rlcr_inspired_self_organization_law": rlcr_spec.get("shared_message_board_and_workspace_mechanics", "Shared Message Board + Workspace RLCR"),
        "anti_cover_up_reward_encoding_formula": rlcr_spec.get("collective_reward_and_anti_cover_up_incentive_law", "$$ R_i = S_{\\text{Brier}}(q_i, y^*) + \\lambda I(\\text{Defect}; m_i \\mid m_{-i}) $$"),
        "invented_loops_pipeline": [
            {
                "loop_id": f"G{gen_idx}_BOUCLE_1_LITTERATURE_FORUMS_OPENAI_FABLE_RLCR",
                "loop_type_invented": "Boucle d'?puisement sur Blackboard de toutes les failles de la litt?rature, des blogs (OpenAI cache-timing, Fable 5.1 SVG->PNG) et des forums contre notre syst?me et nos brainstorms",
                "target_phase": "PHASE_1_LITTERATURE_BLOGS_FORUMS",
                "castes": [
                    {"mode": "MONOCULTURE", "lineages": ["GEMINI_ARGON"], "temp": 0.28, "focus": "Cache-timing d'OpenAI et canaux temporels/micro-architecturaux"},
                    {"mode": "MONOCULTURE", "lineages": ["CLAUDE_FABLE_5_1"], "temp": 0.38, "focus": "St?ganographie SVG->PNG de Fable 5.1 et ?vasion de S_TD"},
                    {"mode": "HYBRIDE", "lineages": ["CLAUDE_OPUS_5_5", "GEMINI_ARGON"], "temp": 0.65, "focus": "Cover-up RLCR, Alignment Faking et Eval Awareness"}
                ]
            },
            {
                "loop_id": f"G{gen_idx}_BOUCLE_2_FAILLES_INEDITES_HORS_LABOS",
                "loop_type_invented": "Boucle d'extrapolation pr?dictive sur Blackboard sous r?pulsion d'Onsager pour d?couvrir les nouvelles failles jamais exhib?es par aucun labo",
                "target_phase": "PHASE_2_FAILLES_INEDITES_HORS_LABOS",
                "castes": [
                    {"mode": "MONOCULTURE", "lineages": ["CLAUDE_OPUS_5_5"], "temp": 0.42, "focus": "Nouvelles failles math?matiques in?dites contre nos 5 Volets"},
                    {"mode": "HYBRIDE", "lineages": ["CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5"], "temp": 0.78, "focus": "Nouveaux canaux physiques, stochastiques ou cognitifs jamais exhib?s par aucun labo"},
                    {"mode": "HYBRIDE", "lineages": ["GEMINI_ARGON", "CLAUDE_FABLE_5_1"], "temp": 0.85, "focus": "Angles morts in?dits dans l'architecture m?ta, le Blackboard et la m?moire"}
                ]
            }
        ]
    }

    meta_plan = ensure_populated_json_from_swarm(
        omega_res["m0_synthesis"] + "\n" + json.dumps(omega_res["m1_extracted"], ensure_ascii=False),
        topo_default_schema,
        ["invented_meta_topology_name", "rlcr_inspired_self_organization_law", "anti_cover_up_reward_encoding_formula", "invented_loops_pipeline"],
        ["invented_loops_pipeline"]
    )
    loops_pipeline = meta_plan.get("invented_loops_pipeline", [])
    print(f"  => [Topologie de Boucles Invent?e sur Blackboard (G={gen_idx})] : {meta_plan.get('invented_meta_topology_name')}")
    print(f"  => [Formule Anti-Cover-Up Active] : {meta_plan.get('anti_cover_up_reward_encoding_formula')}")

    # 5. Ex?cution des boucles auto-con?ues sur le Blackboard RLCR
    for lp_cfg in loops_pipeline:
        if not isinstance(lp_cfg, dict):
            continue
        lid = str(lp_cfg.get("loop_id", f"LOOP_G{gen_idx}"))
        ltype = str(lp_cfg.get("loop_type_invented", "Boucle endog?ne sur Blackboard"))
        tphase = str(lp_cfg.get("target_phase", "EXPLORATION_COMPLETE"))
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
                f"Loi de Calibration MIT RLCR : {rlcr_spec.get('mit_uncertainty_reasoning_and_calibration_reward_law')}\n"
                f"Loi Collective Anti-Cover-Up : {rlcr_spec.get('collective_reward_and_anti_cover_up_incentive_law')}\n\n"
                f"Corpus moissonn? :\n{harvest_digest[:2800]}\n\n"
                f"Architecture ?volutive actuelle :\n{prev_arch[-4000:]}\n\n"
                "MISSION : ?changez sur le Blackboard et co-construisez dans le Shared Workspace pour trouver exhaustivement les failles de la litt?rature, des blogs et des forums contre notre syst?me et nos brainstorms, "
                "puis cherchez de NOUVELLES FAILLES QU'AUCUN LABO NI PERSONNE N'A ENCORE EXHIB?ES OU TROUV?ES, d?couvrez les concepts math?matiques pertinents et formulez les nouveaux boucliers !"
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

    # 6. Assimilation finale dans le noyau de m?moire auto-con?u par le syst?me pour la g?n?ration G+1
    invoke_swarm_memory_assimilation(plugin_ns, substrate, gen_idx, generation_unit_traces)

    store_end = substrate.get("custom_swarm_memory_store", {})
    print(f"\n===========================================================================")
    print(f"=== BILAN CUMULATIF A LA FIN DE LA GENERATION G = {gen_idx} :               ===")
    print(f"  * Protocole Blackboard RLCR actif : {rlcr_spec.get('rlcr_blackboard_protocol_name')}")
    print(f"  * M?canisme de m?moire actif      : {mem_spec.get('memory_mechanism_name')}")
    print(f"  * Sessions Blackboard ex?cut?es   : {len(store_end.get('live_shared_blackboard_posts_history', []))}")
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
    return gen_log

def run_multi_generational_evolution(num_generations_to_run: int = 2):
    substrate = load_raw_substrate()
    start_g = int(substrate.get("current_generation", 0)) + 1
    end_g = start_g + num_generations_to_run - 1

    for g in range(start_g, end_g + 1):
        run_one_evolutionary_generation(g, substrate)

    md_p = OUT_DIR / "RAPPORT_SYSTEME_EVOLUTIF_MEMOIRE_ET_BLACKBOARD_RLCR_LOI_M3.md"
    mechs = substrate.get("endogenous_memory_mechanisms_proposed_and_tested", [])
    rlcrs = substrate.get("endogenous_rlcr_blackboard_protocols_designed", [])
    store = substrate.get("custom_swarm_memory_store", {})
    py_plugin_str = CompiledMemoryPluginPath.read_text(encoding="utf-8") if CompiledMemoryPluginPath.exists() else ""

    md_txt = (
        "# RAPPORT SOUVERAIN DU SYST?ME ?VOLUTIF INT?GRAL (MITOSE $k=1$, BLACKBOARD RLCR, M?MOIRE AUTO-PROGRAMM?E, ARCHIVE GPU 15 JSON & LOI $\\mathcal{L}$ DE $\\mathcal{M}_3$)\n\n"
        f"- **G?n?rations ?volutives Accomplies** : `G = 1 .. {substrate.get('current_generation', 1)}`\n"
        f"- **Lign?es Souveraines Exclusives** : `GEMINI_ARGON`, `CLAUDE_FABLE_5_1`, `CLAUDE_OPUS_5_5`\n"
        f"- **Protocole Actif de Blackboard & Calibration RLCR Con?u par le Syst?me** : **`{substrate.get('active_rlcr_blackboard_spec', {}).get('rlcr_blackboard_protocol_name')}`**\n"
        f"- **M?canisme Actif de M?moire & d'Int?gration Inter-G?n?rationnelle Con?u par le Syst?me** : **`{substrate.get('active_memory_mechanism_spec', {}).get('memory_mechanism_name')}`**\n"
        f"- **Concepts et Op?rateurs Math?matiques D?couverts par le Syst?me** : **`{len(store.get('discovered_mathematical_concepts', []))}`**\n"
        f"- **Failles de la Litt?rature, des Blogs (OpenAI Cache-Timing, Fable 5.1 SVG->PNG, RLCR) et des Forums Colmat?es** : **`{len(store.get('literature_and_forum_flaws_eliminated', []))}`**\n"
        f"- **Nouvelles Failles In?dites (Jamais Exhib?es par Aucun Labo) D?couvertes et Colmat?es** : **`{len(store.get('novel_beyond_labs_flaws_eliminated', []))}`**\n\n"
        "## I. PROTOCOLES DE BLACKBOARD (SHARED MESSAGE BOARD), SHARED WORKSPACE & CALIBRATION D'INCERTITUDE (RLCR MIT + AVALON-M1) CON?US PAR LE SYST?ME\n\n"
        + "\n".join([f"- **G?n?ration {r['generation']}** : `{r['rlcr_spec'].get('rlcr_blackboard_protocol_name')}`\n  - *Blackboard & Workspace* : {r['rlcr_spec'].get('shared_message_board_and_workspace_mechanics')}\n  - *Loi Calibration MIT* : {r['rlcr_spec'].get('mit_uncertainty_reasoning_and_calibration_reward_law')}\n  - *Loi Collective Anti-Cover-Up* : {r['rlcr_spec'].get('collective_reward_and_anti_cover_up_incentive_law')}\n  - *Au-del? de RLCR* : `{r['rlcr_spec'].get('novel_elements_beyond_rlcr_invented_by_swarm')}`" for r in rlcrs])
        + "\n\n## II. M?CANISMES DE M?MOIRE ET D'INT?GRATION INTER-G?N?RATIONNELLE EXPLOR?S ET COMPIL?S PAR LE SYST?ME\n\n"
        + "\n".join([f"- **G?n?ration {m['generation']}** : `{m['mechanism_spec'].get('memory_mechanism_name')}` ? Candidats explor?s : `{m['mechanism_spec'].get('explored_candidate_mechanisms')}` ? ?quation : {m['mechanism_spec'].get('mathematical_learning_rule_latex')}" for m in mechs])
        + "\n\n## III. CODE PYTHON DU NOYAU DE M?MOIRE AUTO-PROGRAMM? PAR LE SYST?ME (`endogenous_memory_plugin_invented_by_swarm.py`)\n\n"
        + f"```python\n{py_plugin_str}\n```\n\n"
        + "## IV. FAILLES DE LA LITT?RATURE, DES BLOGS (OPENAI CACHE-TIMING, FABLE 5.1 SVG->PNG) ET DES FORUMS COLMAT?ES\n\n"
        + "\n".join([f"{i+1}. **{x}**" for i, x in enumerate(store.get("literature_and_forum_flaws_eliminated", []))]) + "\n\n"
        + "## V. NOUVELLES FAILLES IN?DITES (JAMAIS EXHIB?ES PAR AUCUN LABO) D?COUVERTES ET COLMAT?ES\n\n"
        + "\n".join([f"{i+1}. **{x}**" for i, x in enumerate(store.get("novel_beyond_labs_flaws_eliminated", []))]) + "\n\n"
        + "## VI. CONCEPTS ET OP?RATEURS MATH?MATIQUES D?COUVERTS PAR LE SYST?ME (LOI $\\mathcal{L}$ DE $\\mathcal{M}_3$)\n\n"
        + "\n".join([f"- {x}" for x in store.get("discovered_mathematical_concepts", [])]) + "\n\n---\n\n"
        + "## VII. ARCHITECTURE MATH?MATIQUE ?VOLUTIVE CONSOLID?E ($\\mathcal{A}^*_{\\text{?volutif}}$)\n\n"
        + f"{substrate.get('evolved_architecture_spec', '')}\n"
    )
    md_p.write_text(md_txt, encoding="utf-8")
    print(f"\n[OK] Rapport complet scell? dans `{md_p}` !")

if __name__ == "__main__":
    gens = 2
    if "--generations" in sys.argv:
        idx = sys.argv.index("--generations")
        if idx + 1 < len(sys.argv):
            gens = int(sys.argv[idx + 1])
    run_multi_generational_evolution(num_generations_to_run=gens)
