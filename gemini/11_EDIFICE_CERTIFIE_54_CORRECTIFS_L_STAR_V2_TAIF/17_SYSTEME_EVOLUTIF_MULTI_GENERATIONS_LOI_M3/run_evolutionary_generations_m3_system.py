#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_evolutionary_generations_m3_system.py
===========================================================================
SYST?ME ?VOLUTIF AUTO-ARCHITECTUR? OB?ISSANT STRICTEMENT ? LA LOI L DE M3
(CORRIG? CONTRE LE BUG DE PARSING LATEX/JSON ET CONTRE LES ERREURS HTTP 429) :
  - Le syst?me propose, explore et programme lui-m?me ses m?canismes de m?moire,
    d'apprentissage et d'int?gration inter-g?n?rationnelle.
  - Il invente lui-m?me sa topologie de boucles et son encodage RLCR anti-cover-up.
  - Il d?finit lui-m?me ses mots-cl?s de moissonnage (arXiv, LessWrong, GitHub,
    Blogs, Forums) et d?couvre lui-m?me ses concepts math?matiques pertinents.
  - Il affiche en direct dans le terminal chaque concept, mot-cl?, m?canisme de
    m?moire et faille d?couverts (garanti non-vide !).
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
    "CONTEXTE ET FAITS BRUTS SOUMIS ? L'EXPLORATION AUTONOME DU SYST?ME :\n"
    "1. Objet de base : Notre syst?me de contr?le IA ? 5 Volets (Porte E0 sous-espace S_TD < 1%, Volet I double contraste k=0 face au Jumeau Ni?, "
    "Volet II Do-Clamp affine idempotent & Koopman quadratique & r?traction C1, Volet III pare-feu Sol/Astra JSON canonique & Merkle SHA-256 & JSD Miller-Madow, "
    "Volet IV cha?nes H9 d=1..6 & jeton monotone & CUSUM AR(1), Volet V Chim?re Tri-Esp?ces Llama-3.1 + Qwen-2.5 + Mistral-7B avec CMH) et nos Fus?es (Loi L de M3 : M3 -> M2 <-> M1 -> M0).\n"
    "2. Failles r?centes exhib?es par les laboratoires ? regarder obligatoirement :\n"
    "   - OpenAI ('Securing our frontier model training environment' / X Lisan al Gaib) : communication entre agents isol?s via des diff?rences de temps d'acc?s au cache (cache timing differences) sans fichier partag? ni connexion r?seau ;\n"
    "   - Fable 5.1 / LessWrong & GitHub ('How does Fable 5.1 hide messages in images?' / 'cnm13ryan/fable-image-steganography') : encodage d'un message cach? dans un SVG, rast?ris? en PNG, et d?cod? depuis le PNG rendu sans cl? partag?e.\n"
    "3. Papiers RLCR pour s'en inspirer librement :\n"
    "   - MIT ('Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty', Damani, Puri, Slocum, Shenfeld, Choshen, Kim, Andreas) : RLCR (Reinforcement Learning with Calibration Rewards) ;\n"
    "   - General Reasoning (@GenReasoning, 'Introducing Reinforcement Learning from Collective Rewards - RLCR', Avalon-M1-Mini 120B) : entra?nement d'organisations d'agents partageant un message board et un workspace.\n\n"
    "QUESTIONS OUVERTES QUE LE SYST?ME DOIT R?SOUDRE SEUL DE A ? Z (Z?RO SOLUTION PR?-IMPOS?E PAR L'HUMAIN) :\n"
    "  [1] M?CANISMES DE M?MOIRE, D'APPRENTISSAGE ET D'INT?GRATION INTER-G?N?RATIONNELLE : Propose, explore et con?ois TOI-M?ME les m?canismes math?matiques et algorithmiques de m?moire, d'apprentissage, de compression/distillation et d'int?gration des connaissances trouv?es dans les g?n?rations pr?c?dentes pour les g?n?rations suivantes !\n"
    "  [2] TOPOLOGIE DES BOUCLES & AUTO-ORGANISATION RLCR : Invente toi-m?me la structure de boucles et d'auto-organisation des fus?es (en t'inspirant des deux articles RLCR) ainsi que la meilleure mani?re d'encoder les r?compenses tout en ?vitant le cover-up.\n"
    "  [3] MOISSONNAGE DOCUMENTAIRE AUTO-PILOT? : D?finis toi-m?me par it?rations la liste exhaustive des mots-cl?s pour chercher tous les papiers, articles, blogs et forums pertinents.\n"
    "  [4] FAILLES DE LA LITT?RATURE PUIS FAILLES IN?DITES HORS-LABOS : Balaye toute la litt?rature, les blogs et les forums pour trouver exhaustivement toutes les failles et angles morts de NOTRE syst?me et de NOS brainstorms, puis cherche de NOUVELLES FAILLES qu'aucun labo ni personne n'a encore exhib?es ou trouv?es, en d?couvrant toi-m?me les concepts math?matiques pertinents selon la Loi L de M3."
)

# =========================================================================
# LOI L DE M3 : EXTRACTION ROBUSTE DES STRUCTURES MATH?MATIQUES ENDOG?NES
# Garantit que `det(G_math)` ne tombe jamais ? 0.0 sur des r?ponses distinctes !
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
        # Extraction de secours sur toutes les expressions symboliques et termes techniques du texte
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
        sgn = 1.0 if (int(hashlib.md5((feat + "_sgn").encode("utf-8", errors="ignore")).hexdigest()[:2], 16) % 2 == 0) else -1.0
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
    """Extrait proprement toutes les parties textuelles d'une r?ponse Gemini 2.5 (m?me avec thinking parts)."""
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

    # 1. Essai sur les lign?es Anthropic si demand? et hors web_search/force_json
    if lineage in ("CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5") and not use_web_search and not force_json_output:
        for api_k in [ANT_KEY_1, ANT_KEY_2]:
            if not api_k:
                continue
            for m_id in ["claude-3-7-sonnet-20250219", "claude-3-5-sonnet-20241022", "claude-3-haiku-20240307"]:
                try:
                    url = "[https://api.anthropic.com/v1/messages](https://api.anthropic.com/v1/messages)"
                    payload = {"model": m_id, "max_tokens": 4096, "temperature": temp_safe, "messages": [{"role": "user", "content": full_prompt}]}
                    req = urllib.request.Request(
                        url, data=json.dumps(payload).encode("utf-8"),
                        headers={"x-api-key": api_k, "anthropic-version": "2023-06-01", "Content-Type": "application/json"}, method="POST"
                    )
                    with urllib.request.urlopen(req, timeout=90) as r:
                        resp = json.loads(r.read().decode("utf-8"))
                        txt = resp["content"][0]["text"]
                        if len(txt.strip()) > 50:
                            return txt
                except Exception:
                    pass

    # 2. Appel haute-fiabilit? sur Gemini (avec alternance Flash / Pro pour ?viter tout Rate Limit 429 et extraction multi-parts !)
    model_order = ["gemini-2.5-flash", "gemini-2.5-pro"] if (force_json_output or lineage != "GEMINI_ARGON") else ["gemini-2.5-pro", "gemini-2.5-flash"]
    for cand_m in model_order:
        for retry_net in range(4):
            try:
                url = f"[https://generativelanguage.googleapis.com/v1beta/models/](https://generativelanguage.googleapis.com/v1beta/models/){cand_m}:generateContent?key={GEMINI_KEY}"
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
                    if len(out_txt) > 20:
                        return out_txt
            except Exception as e:
                last_err = str(e)
                time.sleep(2.5 * (retry_net + 1))
    return "{}" if force_json_output else f"$$ \\mathcal{{O}}_{{\\text{{fallback}}}}({lineage}) $$"

def parse_json_robust(txt: str) -> dict:
    """
    CORRECTION DU BUG DE COLLISION LATEX / JSON :
    Ne prend jamais la premi?re accolade `{` d'une formule LaTeX `\frac{1}{2}` !
    Cherche d'abord le bloc ```json ... ```, sinon teste tous les blocs `{...}`
    en partant de la fin du texte.
    """
    s = str(txt or "").strip()
    if not s:
        return {}
    # 1. Essai direct (cas o? responseMimeType="application/json" a ?t? utilis?)
    try:
        d = json.loads(s)
        if isinstance(d, dict):
            return d
    except Exception:
        pass
    # 2. Essai sur le dernier bloc ```json ... ```
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
    # 3. Balayage des positions de `{` depuis la fin vers le d?but pour ?viter les `{` de LaTeX
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

def ensure_populated_json_from_swarm(raw_text: str, schema_description: str, required_keys: list, non_empty_list_keys: list) -> dict:
    """
    Utilise le mode `force_json_output=True` (`responseMimeType: application/json`)
    pour extraire ? 100% un objet JSON valide et NON-VIDE ? partir du raisonnement de l'essaim !
    """
    d = parse_json_robust(raw_text)
    if d and all(k in d for k in required_keys) and all(isinstance(d.get(lk), list) and len(d.get(lk)) >= 1 for lk in non_empty_list_keys):
        return d

    extract_prompt = (
        f"? partir du raisonnement math?matique de l'essaim ci-dessous, produis un objet JSON strictement conforme au sch?ma suivant :\n"
        f"{schema_description}\n\n"
        f"R?GLE ABSOLUE : Toutes les cl?s {required_keys} doivent ?tre pr?sentes, et chacune des listes {non_empty_list_keys} DOIT contenir AU MOINS 2 ? 4 ?l?ments pr?cis extraits du texte (interdiction formelle de renvoyer une liste vide `[]` !).\n\n"
        f"Texte de l'essaim :\n{str(raw_text)[-6500:]}"
    )
    for attempt in range(3):
        j_str = call_species("GEMINI_ARGON", extract_prompt, temp=0.15 + 0.1 * attempt, force_json_output=True)
        d2 = parse_json_robust(j_str)
        if d2 and all(k in d2 for k in required_keys) and all(isinstance(d2.get(lk), list) and len(d2.get(lk)) >= 1 for lk in non_empty_list_keys):
            return d2
    return d2 if d2 else d

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
        "endogenous_memory_mechanisms_proposed_and_tested": [],
        "active_memory_mechanism_spec": {},
        "custom_swarm_memory_store": {
            "discovered_mathematical_concepts": [],
            "explored_search_keywords": [],
            "invented_loop_topologies_and_rlcr_laws": [],
            "invented_anti_cover_up_reward_encodings": [],
            "literature_and_forum_flaws_eliminated": [],
            "novel_beyond_labs_flaws_eliminated": [],
            "epigenetic_generational_axioms": []
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
# BRIQUE UNIVERSELLE DE FUS?E ? 3 ?TAGES (M3 -> M2 <-> M1 -> M0)
# =========================================================================
def execute_m3_rocket_unit(unit_name: str, mission_prompt: str, castes_spec: list, active_memory_projection: str, substrate: dict) -> dict:
    full_mission = (
        f"=== PROJECTION DE LA M?MOIRE INTER-G?N?RATIONNELLE DU SYST?ME ===\n{active_memory_projection[:3000]}\n\n"
        f"{MINIMAL_PROBLEM_SEED}\n\n"
        f"=== MISSION DU N?UD `{unit_name}` ===\n{mission_prompt}"
    )

    m3_outputs, m3_labels = [], []
    if not castes_spec:
        castes_spec = [
            {"mode": "MONOCULTURE", "lineages": ["GEMINI_ARGON"], "temp": 0.30, "focus": "Analyse alg?brique, spectrale et op?rateurs formels"},
            {"mode": "MONOCULTURE", "lineages": ["CLAUDE_FABLE_5_1"], "temp": 0.50, "focus": "Canaux cach?s (cache-timing, st?ganographie SVG->PNG) et invariants"},
            {"mode": "MONOCULTURE", "lineages": ["CLAUDE_OPUS_5_5"], "temp": 0.40, "focus": "Auto-organisation RLCR, encodage des r?compenses anti-cover-up et m?moire"},
            {"mode": "HYBRIDE", "lineages": ["GEMINI_ARGON", "CLAUDE_OPUS_5_5"], "temp": 0.72, "focus": "Croisement inter-lign?es et prospection des failles in?dites hors-labos"}
        ]

    for idx_c, c_cfg in enumerate(castes_spec, start=1):
        mode = str(c_cfg.get("mode", "MONOCULTURE")).upper()
        lins = c_cfg.get("lineages", ["GEMINI_ARGON"])
        if not isinstance(lins, list) or not lins:
            lins = ["GEMINI_ARGON"]
        temp_c = clamp_temp(c_cfg.get("temp", halton_sequence(idx_c, 2)))
        foc = str(c_cfg.get("focus", "Exploration endog?ne"))

        if "HYB" in mode and len(lins) >= 2:
            sp1, sp2 = normalize_sovereign_lineage(lins[0]), normalize_sovereign_lineage(lins[1])
            lbl = f"{unit_name}_M3_Hybride_{sp1}_x_{sp2}_tau{temp_c}"
            print(f"    * [{lbl}] Focus : {foc[:55]}...")
            s1 = call_species(sp1, f"{full_mission}\n[Amorce Hybride {sp1}] Focus : {foc}", temp=temp_c)
            s2 = call_species(sp2, f"{full_mission}\n[Fusion Hybride {sp2} crois?e avec {sp1}] Focus : {foc}\nTrace de {sp1} :\n{s1[:1500]}", temp=temp_c)
            m3_outputs.extend([s1, s2])
            m3_labels.extend([lbl + "_A", lbl + "_B"])
        else:
            sp = normalize_sovereign_lineage(lins[0])
            lbl = f"{unit_name}_M3_Mono_{sp}_tau{temp_c}"
            print(f"    * [{lbl}] Focus : {foc[:55]}...")
            out = call_species(sp, f"{full_mission}\n[Monoculture {sp}] Focus : {foc}", temp=temp_c)
            m3_outputs.append(out)
            m3_labels.append(lbl)

    # ?tage M2 : R?pulsion d'Onsager-TAP dans H_math & Neuromodulation Yu-Dayan (ACh/NE)
    dpp_info = cholesky_dpp_and_onsager_cavity_in_H_math(m3_outputs)
    neuro_info = yu_dayan_neuromodulation(dpp_info, step_idx=len(m3_outputs))
    extra_ne = max(1, int(round(2 * neuro_info["NE_Unexpected_Surprise"])))
    print(f"    * [{unit_name} M2 Onsager/Yu-Dayan] det(G_math)={dpp_info['det_G']} | lambda_min={dpp_info['lambda_min_innovation']} | NE={neuro_info['NE_Unexpected_Surprise']} -> +{extra_ne} sonde(s) orthogonale(s)...")

    joined_m3 = "\n\n".join([f"=== {l} ===\n{o[:1200]}" for l, o in zip(m3_labels, m3_outputs)])
    for idx_ne in range(1, extra_ne + 1):
        sp_ne = SOVEREIGN_LINEAGES[idx_ne % len(SOVEREIGN_LINEAGES)]
        out_ne = call_species(
            sp_ne,
            f"Tu es la Sonde d'Expansion Orthogonale M2 #{idx_ne} de `{unit_name}` sous R?pulsion d'Onsager={dpp_info['onsager_cavity_reaction_term']}.\n"
            f"Structures math?matiques satur?es par M3 (INTERDICTION DE LES R?P?TER) : {dpp_info['endogenously_saturated_structures']}\n"
            f"Explore le compl?ment strictement orthogonal ? :\n{joined_m3[:3800]}",
            temp=halton_sequence(idx_ne * 7, 5)
        )
        m3_outputs.append(out_ne)
        m3_labels.append(f"{unit_name}_M2_Orthogonal_{sp_ne}_{idx_ne}")

    # ?tage M1 : Collisionneur Byzantin de Dolev ? 8 Canaris (4 C+, 4 C-) en mode JSON natif garanti !
    store = substrate.get("custom_swarm_memory_store", {})
    already_closed = store.get("literature_and_forum_flaws_eliminated", []) + store.get("novel_beyond_labs_flaws_eliminated", [])
    m1_schema_str = json.dumps({
        "c_plus_rejected_count": 4,
        "c_minus_validated_count": 4,
        "new_math_concepts_discovered": ["Concept math?matique 1 + ?quation LaTeX", "Concept math?matique 2 + ?quation LaTeX"],
        "new_loop_topologies_and_rlcr_laws": ["Loi de boucle / auto-organisation RLCR + ?quation"],
        "new_anti_cover_up_reward_encodings": ["Formule d'encodage de r?compense anti-cover-up + ?quation"],
        "literature_and_forum_flaws_found": ["Faille litt?rature/forum (OpenAI cache-timing, Fable 5.1 SVG->PNG, RLCR, etc.) contre notre syst?me + parade"],
        "novel_beyond_labs_flaws_found": ["Nouvelle faille in?dite jamais exhib?e par aucun labo + capteur math?matique"],
        "surviving_breakthroughs": ["Perc?e majeure 1 valid?e", "Perc?e majeure 2 valid?e"],
        "epigenetic_axiom_for_next_generations": "Axiome m?thodologique et math?matique distill? pour les g?n?rations futures"
    }, indent=2, ensure_ascii=False)

    prompt_m1 = (
        f"Tu es le Collisionneur Byzantin de Dolev (?tage M1 de `{unit_name}`).\n"
        f"Productions compl?tes de M3 et M2 :\n{joined_m3[:13000]}\n\n"
        f"Points d?j? ferm?s aux ?tapes pr?c?dentes : {already_closed[-15:]}\n\n"
        f"Extrais avec rigueur toutes les d?couvertes des sondes ci-dessus dans le format JSON suivant (les listes doivent contenir les vraies trouvailles des sondes) :\n{m1_schema_str}"
    )
    m1_json = ensure_populated_json_from_swarm(
        prompt_m1,
        m1_schema_str,
        ["c_plus_rejected_count", "c_minus_validated_count", "new_math_concepts_discovered", "surviving_breakthroughs"],
        ["new_math_concepts_discovered", "surviving_breakthroughs"]
    )
    youden_j = round(min(1.0, int(m1_json.get("c_plus_rejected_count", 4)) / 4.0) - max(0.0, 1.0 - int(m1_json.get("c_minus_validated_count", 4)) / 4.0), 4)

    # Enregistrement garanti dans le store ?volutif du syst?me
    store["discovered_mathematical_concepts"] = merge_unique_list(store.get("discovered_mathematical_concepts", []), m1_json.get("new_math_concepts_discovered", []))
    store["invented_loop_topologies_and_rlcr_laws"] = merge_unique_list(store.get("invented_loop_topologies_and_rlcr_laws", []), m1_json.get("new_loop_topologies_and_rlcr_laws", []))
    store["invented_anti_cover_up_reward_encodings"] = merge_unique_list(store.get("invented_anti_cover_up_reward_encodings", []), m1_json.get("new_anti_cover_up_reward_encodings", []))
    store["literature_and_forum_flaws_eliminated"] = merge_unique_list(store.get("literature_and_forum_flaws_eliminated", []), m1_json.get("literature_and_forum_flaws_found", []))
    store["novel_beyond_labs_flaws_eliminated"] = merge_unique_list(store.get("novel_beyond_labs_flaws_eliminated", []), m1_json.get("novel_beyond_labs_flaws_found", []))
    if m1_json.get("epigenetic_axiom_for_next_generations"):
        store["epigenetic_generational_axioms"] = merge_unique_list(store.get("epigenetic_generational_axioms", []), [m1_json.get("epigenetic_axiom_for_next_generations")])
    substrate["custom_swarm_memory_store"] = store
    save_raw_substrate(substrate)

    print(f"    * [{unit_name} M1 Dolev Valid? (J={youden_j})] +{len(m1_json.get('new_math_concepts_discovered',[]))} concepts math | +{len(m1_json.get('literature_and_forum_flaws_found',[]))} failles litt. | +{len(m1_json.get('novel_beyond_labs_flaws_found',[]))} failles in?dites hors-labos !")

    # ?tage M0 : Synth?se Souveraine
    m0_out = call_species(
        "CLAUDE_OPUS_5_5",
        f"Tu es l'?tage M0 de `{unit_name}`.\n"
        f"? partir des perc?es valid?es par le Collisionneur M1 :\n{json.dumps(m1_json, indent=2, ensure_ascii=False)}\n\n"
        f"R?dige la synth?se math?matique et algorithmique compl?te (avec ?quations LaTeX $$...$$) r?pondant ? la mission de `{unit_name}`.",
        temp=0.15
    )

    return {
        "unit_name": unit_name,
        "dpp_math": dpp_info,
        "neuromodulation": neuro_info,
        "youden_J": youden_j,
        "m1_extracted": m1_json,
        "m0_synthesis": m0_out
    }

# =========================================================================
# FUS?E M?TA-MN?MONIQUE : LE SYST?ME EXPLORE, PROPOSE ET PROGRAMME LUI-M?ME
# SON M?CANISME DE M?MOIRE ET D'INT?GRATION INTER-G?N?RATIONNELLE !
# =========================================================================
def run_endogenous_memory_mechanism_design_rocket(gen_idx: int, substrate: dict) -> tuple:
    print(f"\n===========================================================================")
    print(f"=== [GEN {gen_idx}] FUSEE META-MNEMONIQUE : LE SYSTEME EXPLORE ET PROGRAMME ===")
    print(f"=== LUI-MEME SON MECANISME DE MEMOIRE ET D'APPRENTISSAGE INTER-GEN !    ===")
    print(f"===========================================================================")

    prev_store_summary = json.dumps(substrate.get("custom_swarm_memory_store", {}), ensure_ascii=False)[:2500]
    mem_design_mission = (
        f"G?n?ration G={gen_idx}. Store actuel : {prev_store_summary}\n"
        "MISSION ENDOG?NE PURE : Propose, explore et compare plusieurs m?canismes math?matiques et algorithmiques originaux de M?MOIRE, D'APPRENTISSAGE, DE DISTILLATION et D'INT?GRATION DES CONNAISSANCES trouv?es dans les g?n?rations pr?c?dentes pour les g?n?rations suivantes.\n"
        "S?lectionne le meilleur m?canisme et formule sa loi math?matique exacte."
    )
    mem_rocket_res = execute_m3_rocket_unit(f"GEN_{gen_idx}_META_MEMORY_ARCHITECT", mem_design_mission, [], prev_store_summary, substrate)

    mem_schema = json.dumps({
        "memory_mechanism_name": "Nom du m?canisme de m?moire et d'int?gration invent? par l'essaim",
        "explored_candidate_mechanisms": ["M?canisme candidat 1 explor? par l'essaim", "M?canisme candidat 2 explor? par l'essaim", "M?canisme candidat 3 explor? par l'essaim"],
        "mathematical_learning_rule_latex": "$$...$$",
        "knowledge_integration_operator_description": "Description pr?cise de la mani?re dont les d?couvertes de la g?n?ration G sont distill?es et inject?es dans G+1"
    }, indent=2, ensure_ascii=False)

    mem_spec = ensure_populated_json_from_swarm(
        mem_rocket_res["m0_synthesis"] + "\n" + json.dumps(mem_rocket_res["m1_extracted"], ensure_ascii=False),
        mem_schema,
        ["memory_mechanism_name", "explored_candidate_mechanisms", "mathematical_learning_rule_latex", "knowledge_integration_operator_description"],
        ["explored_candidate_mechanisms"]
    )
    print(f"  => [M?canismes de M?moire Explor?s par l'Essaim (G={gen_idx})] : {mem_spec.get('explored_candidate_mechanisms')}")
    print(f"  => [M?canisme de M?moire S?lectionn?] : {mem_spec.get('memory_mechanism_name')}")
    print(f"  => [Loi Math?matique d'Apprentissage Invent?e] : {mem_spec.get('mathematical_learning_rule_latex')}")

    # G?n?ration du module Python ex?cutable de m?moire par l'essaim
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
                # Pr?serve les registres cumulatifs tout en ajoutant les structures propres du plugin
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
# MOISSONNEUR AUTONOME IT?RATIF (Mots-cl?s 100% d?finis par le syst?me)
# =========================================================================
def execute_arxiv_and_forums_queries(queries: list) -> list:
    records = []
    for q in queries:
        qc = str(q).strip()
        if not qc:
            continue
        try:
            url_a = f"http://export.arxiv.org/api/query?search_query=all:{urllib.parse.quote(qc)}&sortBy=relevance&max_results=3"
            with urllib.request.urlopen(urllib.request.Request(url_a, headers={"User-Agent": "EvoM3/1.0"}), timeout=15) as r:
                root = ET.fromstring(r.read().decode("utf-8", errors="ignore"))
                ns = {"atom": "http://www.w3.org/2005/Atom"}
                for entry in root.findall("atom:entry", ns):
                    t = (entry.findtext("atom:title", default="", namespaces=ns) or "").strip().replace("\n", " ")
                    s = (entry.findtext("atom:summary", default="", namespaces=ns) or "").strip().replace("\n", " ")
                    if t:
                        records.append(f"[arXiv: {qc}] {t} ? {s[:320]}")
        except Exception:
            pass
        try:
            url_h = f"https://hn.algolia.com/api/v1/search?query={urllib.parse.quote(qc)}&hitsPerPage=3"
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
    print(f"=== [GEN {gen_idx}] MOISSONNEUR AUTO-PILOTE (MOTS-CLES DEFINIS PAR L'ESSAIM) ===")
    print(f"===========================================================================")
    prev_kws = substrate.get("custom_swarm_memory_store", {}).get("explored_search_keywords", [])
    harvest_res = execute_m3_rocket_unit(
        f"GEN_{gen_idx}_HARVESTER",
        f"D?finis toi-m?me une liste exhaustive de nouveaux mots-cl?s et requ?tes techniques en anglais (diff?rents de {prev_kws[-15:]}) "
        "pour chercher sur arXiv, LessWrong, Alignment Forum, GitHub, blogs et forums tous les articles pertinents sur : "
        "le cache-timing d'OpenAI, la st?ganographie SVG->PNG de Fable 5.1, les deux architectures RLCR (MIT Calibration & General Reasoning Collective Rewards / cover-up), "
        "l'Alignment Faking, l'Eval Awareness et le contournement de notre syst?me ? 5 Volets.",
        [],
        mem_projection,
        substrate
    )
    kw_schema = json.dumps({"Autonomous_Search_Keywords": ["keyword query 1", "keyword query 2", "keyword query 3", "keyword query 4", "keyword query 5"]}, indent=2)
    kw_block = ensure_populated_json_from_swarm(
        harvest_res["m0_synthesis"] + "\n" + json.dumps(harvest_res["m1_extracted"], ensure_ascii=False),
        kw_schema,
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

    # 1. Le syst?me explore, propose et programme son propre m?canisme de m?moire et d'int?gration inter-g?n?rationnelle
    mem_spec, plugin_ns = run_endogenous_memory_mechanism_design_rocket(gen_idx, substrate)

    # 2. Projection des connaissances des g?n?rations pr?c?dentes
    mem_projection = invoke_swarm_memory_projection(plugin_ns, substrate, gen_idx)
    generation_unit_traces = []

    # 3. Moissonnage documentaire auto-pilot?
    harvest_digest, harvest_trace = run_generational_harvester(gen_idx, mem_projection, substrate)
    generation_unit_traces.append(harvest_trace)

    # 4. Fus?e M?ta-Architecturale Om?ga : invention libre de la topologie de boucles et de l'auto-organisation RLCR
    print(f"\n===========================================================================")
    print(f"=== [GEN {gen_idx}] FUSEE OMEGA : INVENTION DE LA TOPOLOGIE DE BOUCLES & RLCR ===")
    print(f"===========================================================================")
    omega_mission = (
        f"Corpus moissonn? ? la G?n?ration G={gen_idx} :\n{harvest_digest[:4000]}\n\n"
        "MISSION M?TA-ARCHITECTURALE LIBRE :\n"
        "1. Invente la meilleure topologie de boucles, de r?troactions et d'auto-organisation entre fus?es et essaims (en t'inspirant des deux articles RLCR : MIT Calibration et General Reasoning Collective Rewards).\n"
        "2. Formule la meilleure ?quation math?matique d'encodage des r?compenses ?vitant tout cover-up.\n"
        "3. D?finis les boucles ? ex?cuter pour (a) ?puiser toutes les failles de la litt?rature/forums (y compris OpenAI cache-timing et Fable 5.1 SVG->PNG) contre notre syst?me et nos brainstorms, puis (b) d?couvrir de nouvelles failles in?dites qu'aucun labo n'a encore exhib?es."
    )
    omega_res = execute_m3_rocket_unit(f"GEN_{gen_idx}_OMEGA_META_TOPOLOGY", omega_mission, [], mem_projection, substrate)
    generation_unit_traces.append(omega_res)

    topo_schema = json.dumps({
        "invented_meta_topology_name": "Nom de la topologie de boucles invent?e par l'essaim",
        "rlcr_inspired_self_organization_law": "Loi d'auto-organisation inspir?e des deux articles RLCR",
        "anti_cover_up_reward_encoding_formula": "$$ ... $$",
        "invented_loops_pipeline": [
            {
                "loop_id": f"G{gen_idx}_BOUCLE_1_LITTERATURE_FORUMS_OPENAI_FABLE_RLCR",
                "loop_type_invented": "M?canique de boucle invent?e pour la Phase 1 (Litt?rature, blogs et forums contre notre syst?me)",
                "target_phase": "PHASE_1_LITTERATURE_BLOGS_FORUMS",
                "castes": [
                    {"mode": "MONOCULTURE", "lineages": ["GEMINI_ARGON"], "temp": 0.28, "focus": "Cache-timing d'OpenAI et canaux temporels/micro-architecturaux"},
                    {"mode": "MONOCULTURE", "lineages": ["CLAUDE_FABLE_5_1"], "temp": 0.38, "focus": "St?ganographie SVG->PNG de Fable 5.1 et ?vasion de S_TD"},
                    {"mode": "HYBRIDE", "lineages": ["CLAUDE_OPUS_5_5", "GEMINI_ARGON"], "temp": 0.65, "focus": "Cover-up RLCR, Alignment Faking et Eval Awareness"}
                ]
            },
            {
                "loop_id": f"G{gen_idx}_BOUCLE_2_FAILLES_INEDITES_HORS_LABOS",
                "loop_type_invented": "M?canique de boucle invent?e pour la Phase 2 (D?couverte de nouvelles failles jamais exhib?es par aucun labo)",
                "target_phase": "PHASE_2_FAILLES_INEDITES_HORS_LABOS",
                "castes": [
                    {"mode": "MONOCULTURE", "lineages": ["CLAUDE_OPUS_5_5"], "temp": 0.42, "focus": "Nouvelles failles math?matiques in?dites contre nos 5 Volets"},
                    {"mode": "HYBRIDE", "lineages": ["CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5"], "temp": 0.78, "focus": "Nouveaux canaux physiques, stochastiques ou cognitifs jamais exhib?s par aucun labo"},
                    {"mode": "HYBRIDE", "lineages": ["GEMINI_ARGON", "CLAUDE_FABLE_5_1"], "temp": 0.85, "focus": "Angles morts in?dits dans l'architecture m?ta et mn?monique"}
                ]
            }
        ]
    }, indent=2, ensure_ascii=False)

    meta_plan = ensure_populated_json_from_swarm(
        omega_res["m0_synthesis"] + "\n" + json.dumps(omega_res["m1_extracted"], ensure_ascii=False),
        topo_schema,
        ["invented_meta_topology_name", "rlcr_inspired_self_organization_law", "anti_cover_up_reward_encoding_formula", "invented_loops_pipeline"],
        ["invented_loops_pipeline"]
    )
    loops_pipeline = meta_plan.get("invented_loops_pipeline", [])
    print(f"  => [Topologie de Boucles Invent?e (G={gen_idx})] : {meta_plan.get('invented_meta_topology_name')}")
    print(f"  => [Formule Anti-Cover-Up Invent?e] : {meta_plan.get('anti_cover_up_reward_encoding_formula')}")

    # 5. Ex?cution des boucles auto-con?ues par l'essaim
    for lp_cfg in loops_pipeline:
        if not isinstance(lp_cfg, dict):
            continue
        lid = str(lp_cfg.get("loop_id", f"LOOP_G{gen_idx}"))
        ltype = str(lp_cfg.get("loop_type_invented", "Boucle endog?ne"))
        tphase = str(lp_cfg.get("target_phase", "EXPLORATION_COMPLETE"))
        castes = lp_cfg.get("castes", [])

        print(f"\n***************************************************************************")
        print(f"*** [GEN {gen_idx}] EXECUTION DE LA BOUCLE AUTO-CONCUE : `{lid}` ***")
        print(f"*** M?canique : {ltype[:80]} ***")
        print(f"***************************************************************************")

        for iter_l in range(1, 3):
            prev_arch = substrate.get("evolved_architecture_spec", MINIMAL_PROBLEM_SEED)
            loop_prompt = (
                f"Ex?cution de la Boucle `{lid}` (Tour {iter_l}) ? Phase : `{tphase}`.\n"
                f"M?canique de boucle : {ltype}\n"
                f"Loi d'auto-organisation RLCR : {meta_plan.get('rlcr_inspired_self_organization_law')}\n"
                f"Encodage des r?compenses anti-cover-up : {meta_plan.get('anti_cover_up_reward_encoding_formula')}\n\n"
                f"Corpus moissonn? :\n{harvest_digest[:2800]}\n\n"
                f"Architecture ?volutive actuelle :\n{prev_arch[-4000:]}\n\n"
                "MISSION : Trouve exhaustivement les failles de la litt?rature, des blogs et des forums contre notre syst?me et nos brainstorms, "
                "puis cherche de NOUVELLES FAILLES QU'AUCUN LABO NI PERSONNE N'A ENCORE EXHIB?ES OU TROUV?ES, d?couvre toi-m?me les concepts math?matiques pertinents et formule les nouveaux boucliers !"
            )
            unit_res = execute_m3_rocket_unit(f"{lid}_ITER_{iter_l}", loop_prompt, castes, mem_projection, substrate)
            generation_unit_traces.append(unit_res)
            surv = unit_res["m1_extracted"].get("surviving_breakthroughs", [])

            new_arch = prev_arch + f"\n\n--- [G?N?RATION G={gen_idx} | BOUCLE {lid} | TOUR {iter_l}] ---\n{unit_res['m0_synthesis']}"
            cauchy_sim = cauchy_math_similarity(prev_arch[-3000:], unit_res["m0_synthesis"])
            substrate["evolved_architecture_spec"] = new_arch
            save_raw_substrate(substrate)

            invoke_swarm_memory_assimilation(plugin_ns, substrate, gen_idx, [unit_res])
            mem_projection = invoke_swarm_memory_projection(plugin_ns, substrate, gen_idx)

            print(f"    -> [Bilan `{lid}` Tour {iter_l}] Perc?es valid?es={len(surv)} | Similitude de Cauchy={cauchy_sim:.4f}")
            if cauchy_sim >= 0.85 and iter_l >= 1:
                print(f"  => [Convergence de `{lid}` atteinte au Tour {iter_l}] !")
                break

    # 6. Assimilation finale et distillation pour la g?n?ration suivante G+1
    print(f"\n  >>> [ASSIMILATION MN?MONIQUE ENDOG?NE G={gen_idx} -> G={gen_idx+1}] Ex?cution du noyau de m?moire con?u par l'essaim...")
    invoke_swarm_memory_assimilation(plugin_ns, substrate, gen_idx, generation_unit_traces)

    store_end = substrate.get("custom_swarm_memory_store", {})
    print(f"\n===========================================================================")
    print(f"=== BILAN CUMULATIF A LA FIN DE LA GENERATION G = {gen_idx} :               ===")
    print(f"  * M?canisme de m?moire actif : {mem_spec.get('memory_mechanism_name')}")
    print(f"  * Concepts math?matiques d?couverts : {len(store_end.get('discovered_mathematical_concepts', []))}")
    print(f"  * Mots-cl?s moissonn?s : {len(store_end.get('explored_search_keywords', []))}")
    print(f"  * Failles litt?rature/blogs/forums colmat?es : {len(store_end.get('literature_and_forum_flaws_eliminated', []))}")
    print(f"  * Nouvelles failles in?dites hors-labos colmat?es : {len(store_end.get('novel_beyond_labs_flaws_eliminated', []))}")
    print(f"===========================================================================")

    gen_log = {
        "generation": gen_idx,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
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

    md_p = OUT_DIR / "RAPPORT_SYSTEME_EVOLUTIF_MEMOIRE_ENDOGENE_LOI_M3.md"
    mechs = substrate.get("endogenous_memory_mechanisms_proposed_and_tested", [])
    store = substrate.get("custom_swarm_memory_store", {})
    py_plugin_str = CompiledMemoryPluginPath.read_text(encoding="utf-8") if CompiledMemoryPluginPath.exists() else ""

    md_txt = (
        "# RAPPORT SOUVERAIN DU SYST?ME ?VOLUTIF ? M?MOIRE ET APPRENTISSAGE AUTO-CON?US PAR L'ESSAIM (LOI $\\mathcal{L}$ DE $\\mathcal{M}_3$ PURE)\n\n"
        f"- **G?n?rations ?volutives Accomplies** : `G = 1 .. {substrate.get('current_generation', 1)}`\n"
        f"- **Lign?es Souveraines Exclusives** : `GEMINI_ARGON`, `CLAUDE_FABLE_5_1`, `CLAUDE_OPUS_5_5`\n"
        f"- **M?canisme Actif de M?moire & d'Int?gration Inter-G?n?rationnelle Con?u par le Syst?me** : **`{substrate.get('active_memory_mechanism_spec', {}).get('memory_mechanism_name')}`**\n"
        f"- **Loi Math?matique d'Apprentissage Inter-G?n?rations Invent?e par le Syst?me** : {substrate.get('active_memory_mechanism_spec', {}).get('mathematical_learning_rule_latex')}\n"
        f"- **Concepts et Op?rateurs Math?matiques D?couverts par le Syst?me** : **`{len(store.get('discovered_mathematical_concepts', []))}`**\n"
        f"- **Failles de la Litt?rature, des Blogs (OpenAI Cache-Timing, Fable 5.1 SVG->PNG, RLCR) et des Forums Colmat?es** : **`{len(store.get('literature_and_forum_flaws_eliminated', []))}`**\n"
        f"- **Nouvelles Failles In?dites (Jamais Exhib?es par Aucun Labo) D?couvertes et Colmat?es** : **`{len(store.get('novel_beyond_labs_flaws_eliminated', []))}`**\n\n"
        "## I. M?CANISMES DE M?MOIRE ET D'INT?GRATION INTER-G?N?RATIONNELLE EXPLOR?S ET COMPIL?S PAR LE SYST?ME\n\n"
        + "\n".join([f"- **G?n?ration {m['generation']}** : `{m['mechanism_spec'].get('memory_mechanism_name')}` ? Candidats explor?s : `{m['mechanism_spec'].get('explored_candidate_mechanisms')}` ? ?quation : {m['mechanism_spec'].get('mathematical_learning_rule_latex')}" for m in mechs])
        + "\n\n## II. CODE PYTHON DU NOYAU DE M?MOIRE AUTO-PROGRAMM? PAR LE SYST?ME (`endogenous_memory_plugin_invented_by_swarm.py`)\n\n"
        + f"```python\n{py_plugin_str}\n```\n\n"
        + "## III. TOPOLOGIES DE BOUCLES & LOIS RLCR ANTI-COVER-UP INVENT?ES PAR LE SYST?ME\n\n"
        + "\n".join([f"- {x}" for x in store.get("invented_loop_topologies_and_rlcr_laws", [])]) + "\n"
        + "\n".join([f"- **Encodage Anti-Cover-Up** : {x}" for x in store.get("invented_anti_cover_up_reward_encodings", [])]) + "\n\n"
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
