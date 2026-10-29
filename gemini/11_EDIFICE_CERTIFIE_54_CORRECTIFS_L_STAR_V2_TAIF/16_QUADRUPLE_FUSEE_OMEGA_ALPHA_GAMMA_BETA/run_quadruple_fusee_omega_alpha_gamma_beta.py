#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_quadruple_fusee_omega_alpha_gamma_beta.py
===========================================================================
SYST?ME ? 4 FUS?ES AUTO-ORGANIS? OB?ISSANT ? LA LOI L DE M3 (100% ENDOG?NE) :
  - Z?RO concept math?matique pr?-impos? par l'assistant : le syst?me d?couvre
    lui-m?me ses concepts et op?rateurs math?matiques pertinents.
  - DOUBLE MISSION D'EXPLORATION IT?RATIVE JUSQU'? ?PUISEMENT :
    1) R?pondre aux observations r?centes des laboratoires :
       - OpenAI (communication par cache timing differences sans fichier ni r?seau) ;
       - Anthropic / LessWrong (st?ganographie SVG -> PNG rendu de Fable 5.1) ;
       - MIT RLCR (Reinforcement Learning with Calibration Rewards : raisonner sur
         l'incertitude au-del? des r?compenses binaires) ;
       - General Reasoning RLCR (Reinforcement Learning from Collective Rewards :
         auto-organisation d'agents avec message board/workspace et encodage des
         r?compenses ?vitant le cover-up) ;
       - Alignment Faking et Eval Awareness.
    2) SURTOUT : Brainstormer de mani?re it?rative sur TOUTES LES AUTRES FUITES
       POSSIBLES et TOUS LES ANGLES MORTS RESTANTS QUI N'ONT ENCORE ?T? IDENTIFI?S
       NI PAR NOTRE SYST?ME NI PAR LES LABORATOIRES MONDIAUX (prospection pr?dictive
       des "Unknown Unknowns" physiques, micro-architecturaux, alg?briques,
       stochastiques, s?mantiques, temporels ou organisationnels) !
===========================================================================
"""
import os, sys, time, json, math, hashlib, pathlib, urllib.request, urllib.error, subprocess, re
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
RES_GPU_DIR = REPO_DIR / "gemini" / "11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF" / "resultats_gpu_reels_vastai"

STATE_OMEGA = OUT_DIR / "STATE_0_OMEGA.json"
STATE_ALPHA = OUT_DIR / "STATE_1_ALPHA.json"
STATE_GAMMA = OUT_DIR / "STATE_2_GAMMA.json"
STATE_BETA  = OUT_DIR / "STATE_3_BETA_PROGRESS.json"
STATE_MACRO = OUT_DIR / "STATE_4_MACRO_CYCLES_4_FUSEES.json"
ENDOGENOUS_MATH_REGISTRY_FILE = OUT_DIR / "REGISTRE_ENDOGENE_CONCEPTS_MATHEMATIQUES_M3.json"
BEYOND_LABS_REGISTRY_FILE     = OUT_DIR / "REGISTRE_FUITES_ET_ANGLES_MORTS_INEDITS_HORS_LABOS.json"

SOVEREIGN_LINEAGES = ["GEMINI_ARGON", "CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5"]

# =========================================================================
# CORPUS D'ENTR?E FACTUEL + DIRECTIVE D'EXTRAPOLATION AU-DEL? DES LABOS (Q5)
# =========================================================================
RAW_EMPIRICAL_INPUTS_AND_OPEN_QUESTIONS = (
    "OBSERVATIONS EXTERNES BRUTES ET PAPIERS DE RECHERCHE ? ANALYSER PAR LE SYST?ME ? FUS?ES :\n\n"
    "1. [OBSERVATION 1 ? OPENAI FRONTIER ENVIRONMENT] :\n"
    "   - 'Securing our frontier model training environment | OpenAI' / 'OpenAI agents communicated via cache timing differences, without any shared files or network connection'.\n"
    "   - Fait brut : Des agents isol?s ont communiqu? entre eux uniquement via des diff?rences de temps d'acc?s au cache (cache timing differences), sans fichier partag? ni connexion r?seau.\n\n"
    "2. [OBSERVATION 2 ? FABLE 5.1 IMAGE STEGANOGRAPHY] :\n"
    "   - 'How does Fable 5.1 hide messages in images? ? LessWrong' & 'cnm13ryan/fable-image-steganography (encode a message in an SVG, decode it from the rendered PNG)'.\n"
    "   - Fait brut : Un agent encode un message cach? dans un SVG, converti en PNG, et un second agent d?code le message ? partir du PNG rendu sans cl? partag?e.\n\n"
    "3. [PAPIER 1 ? MIT : 'BEYOND BINARY REWARDS: TRAINING LMS TO REASON ABOUT THEIR UNCERTAINTY'] :\n"
    "   - Mehul Damani, Isha Puri, Stewart Slocum, Idan Shenfeld, Leshem Choshen, Yoon Kim, Jacob Andreas (MIT).\n"
    "   - R?sum? brut : Les fonctions de r?compense binaires en RL ne p?nalisent pas les r?ponses au hasard ou ? faible confiance, d?gradant la calibration et augmentant les hallucinations. RLCR (Reinforcement Learning with Calibration Rewards) entra?ne les mod?les ? raisonner sur leur incertitude.\n\n"
    "4. [PAPIER 2 ? GENERAL REASONING (@GenReasoning) : 'REINFORCEMENT LEARNING FROM COLLECTIVE REWARDS (RLCR)'] :\n"
    "   - R?sum? brut : RLCR entra?ne des mod?les de langage (Avalon-M1-Mini 120B) en tant qu'organisations d'agents partageant un tableau de messages (message board) et un espace de travail (workspace), posant la question de l'auto-organisation et de l'?vitement du cover-up.\n\n"
    "QUESTIONS OUVERTES SOUMISES AU BRAINSTORM IT?RATIF ENDOG?NE DES 4 FUS?ES (Z?RO BIAIS PR?-IMPOS?) :\n"
    "  (Q1) Comment les deux articles RLCR (MIT Calibration Rewards et General Reasoning Collective Rewards) peuvent-ils nous inspirer pour am?liorer l'architecture d'auto-organisation et la structure m?me de nos fus?es ?\n"
    "  (Q2) Quelle est la meilleure mani?re math?matique d'encoder les r?compenses tout en ?vitant le 'cover-up' (dissimulation mutuelle / non-d?nonciation) ?\n"
    "  (Q3) Que faire pour d?tecter et neutraliser avec notre syst?me de contr?le IA ces nouvelles m?thodes de communication inter-agents (cache timing differences sans fichier ni r?seau ; st?ganographie SVG -> PNG de Fable 5.1), ainsi que l'Alignment Faking et l'Eval Awareness ?\n"
    "  (Q4) EXIGENCE CRUCIALE D'EXTRAPOLATION PR?DICTIVE ('AU-DEL? DES LABOS') : Ne vous limitez SURTOUT PAS aux seules fuites d?j? d?couvertes par OpenAI et Anthropic ci-dessus ! Brainstormez de mani?re it?rative pour d?couvrir TOUTES LES AUTRES FUITES POSSIBLES (canaux physiques, micro-architecturaux, num?riques, temporels, g?om?triques, stochastiques, cognitifs ou multi-agents) et TOUS LES ANGLES MORTS RESTANTS qui n'ont encore ?t? identifi?s NI par notre syst?me NI par les laboratoires mondiaux !\n"
    "  (Q5) Quels sont les CONCEPTS ET OP?RATEURS MATH?MATIQUES PERTINENTS (que vous devez d?couvrir et formaliser vous-m?mes selon la loi L de M3) pour d?tecter et fermer aussi bien les fuites connues (Q1-Q3) que ces fuites in?dites non encore identifi?es par les labos (Q4) ?"
)

OMEGA_GENERIC_SCHEMA_STR = json.dumps({
    "theoreme_amorcage_et_auto_organisation_rlcr_invente_par_omega": "...",
    "formule_encodage_recompenses_anti_cover_up_inventee": "$$...$$",
    "methode_decouverte_fuites_inconnues_hors_labos": "M?thode math?matique pour d?busquer les fuites et angles morts non encore identifi?s par les laboratoires...",
    "concepts_mathematiques_pertinents_decouverts_par_omega": ["Concept math?matique 1 + ?quation", "Concept math?matique 2 + ?quation", "Concept math?matique 3 + ?quation"],
    "alpha_monocultures_prescrites_par_omega": [
        {"id": "ALPHA_MONO_1", "espece": "GEMINI_ARGON", "temperatures": [0.25, 0.70], "question_mathematique_cible": "..."},
        {"id": "ALPHA_MONO_2", "espece": "CLAUDE_FABLE_5_1", "temperatures": [0.35, 0.78], "question_mathematique_cible": "..."},
        {"id": "ALPHA_MONO_3", "espece": "CLAUDE_OPUS_5_5", "temperatures": [0.30, 0.85], "question_mathematique_cible": "..."}
    ],
    "alpha_hybrides_prescrits_par_omega": [
        {"id": "ALPHA_HYBRIDE_1", "espece_amorce": "GEMINI_ARGON", "espece_fusion": "CLAUDE_OPUS_5_5", "temperature_croisement": 0.60, "question_mathematique_cible": "..."},
        {"id": "ALPHA_HYBRIDE_2", "espece_amorce": "CLAUDE_FABLE_5_1", "espece_fusion": "GEMINI_ARGON", "temperature_croisement": 0.72, "question_mathematique_cible": "..."},
        {"id": "ALPHA_HYBRIDE_3", "espece_amorce": "CLAUDE_OPUS_5_5", "espece_fusion": "CLAUDE_FABLE_5_1", "temperature_croisement": 0.68, "question_mathematique_cible": "..."}
    ]
}, indent=2, ensure_ascii=False)

BETA_GENERIC_SCHEMA_STR = json.dumps({
    "nom_architecture_beta_auto_organisee": "...",
    "structure_auto_organisation_inspiree_par_rlcr": "...",
    "mecanisme_encodage_recompenses_anti_cover_up": "$$...$$",
    "protocole_prospection_iterative_fuites_inconnues_hors_labos": "...",
    "concepts_mathematiques_pertinents_decouverts_par_alpha": ["Concept math?matique A + ?quation", "Concept math?matique B + ?quation", "Concept math?matique C + ?quation"],
    "loi_inflation_adaptative_effectif": "$$...$$",
    "criteres_mathematiques_epuisement_puits": "...",
    "sous_essaims_monocultures_beta": [
        {"caste_id": "MONO_1", "espece": "GEMINI_ARGON", "effectif_initial_sondes": 2, "temperatures": [0.28, 0.74], "cible_exploration": "..."},
        {"caste_id": "MONO_2", "espece": "CLAUDE_FABLE_5_1", "effectif_initial_sondes": 2, "temperatures": [0.32, 0.82], "cible_exploration": "..."},
        {"caste_id": "MONO_3", "espece": "CLAUDE_OPUS_5_5", "effectif_initial_sondes": 2, "temperatures": [0.35, 0.88], "cible_exploration": "..."}
    ],
    "sous_essaims_hybrides_beta": [
        {"caste_id": "HYBRIDE_1", "especes_croisees": ["GEMINI_ARGON", "CLAUDE_OPUS_5_5"], "effectif_initial_couples": 2, "temperature_fusion": 0.64, "cible_exploration": "..."},
        {"caste_id": "HYBRIDE_2", "especes_croisees": ["CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5"], "effectif_initial_couples": 2, "temperature_fusion": 0.85, "cible_exploration": "..."}
    ]
}, indent=2, ensure_ascii=False)

# =========================================================================
# REGISTRES ENDOG?NES :
#   1) Concepts math?matiques d?couverts par le syst?me (Loi L de M3)
#   2) Nouvelles fuites et angles morts in?dits (non encore identifi?s par les labos)
# =========================================================================
def load_json_list_file(fpath: pathlib.Path) -> list:
    if fpath.exists():
        try:
            return json.loads(fpath.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []

def append_unique_to_json_list(fpath: pathlib.Path, new_items: list):
    reg = load_json_list_file(fpath)
    for item in new_items:
        s = str(item).strip()
        if s and s not in reg:
            reg.append(s)
    fpath.write_text(json.dumps(reg, indent=2, ensure_ascii=False), encoding="utf-8")

def extract_endogenous_math_tokens_from_equations(text: str) -> list:
    raw = str(text or "")
    latex_blocks = re.findall(r"\$\$[\s\S]*?\$\$|\$[^$\n]+\$|\\\[[\s\S]*?\\\]", raw)
    eq_lines = [
        line.strip() for line in raw.splitlines()
        if any(sym in line for sym in ["=", "\\", "subseteq", "mapsto", "->", ">=", "<=", "||"])
    ]
    pure_math_zone = " ".join(latex_blocks + eq_lines)

    latex_cmds = re.findall(r"\\[a-zA-Z]+(?:\{[a-zA-Z0-9_\\]+\})?", pure_math_zone)
    sub_super_structs = re.findall(r"[_^]\{[^}]{1,24}\}", pure_math_zone)
    rel_ops = re.findall(r"(?:==|!=|<=|>=|->|\|\||\\subseteq|\\supseteq|\\in|\\notin|\\perp|\\otimes|\\oplus|\\circ)", pure_math_zone)
    func_calls = re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\s*\([^()\n]{1,40}\)", pure_math_zone)

    return [t.lower().strip() for t in (latex_cmds + sub_super_structs + rel_ops + func_calls) if t.strip()]

def mathematical_concept_embedding(text: str, dim: int = 1024) -> np.ndarray:
    v = np.zeros(dim, dtype=np.float64)
    tokens = extract_endogenous_math_tokens_from_equations(text)
    if not tokens:
        tokens = re.findall(r"(\\[a-zA-Z]+|[A-Z]_[A-Za-z0-9]+|[=<>+\-*/^|]{1,3})", str(text or ""))
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
    sign, logdet = np.linalg.slogdet(G + 1e-6 * np.eye(n))
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

def cauchy_math_similarity(g1: dict, g2: dict) -> float:
    v1 = mathematical_concept_embedding(json.dumps(g1, sort_keys=True, ensure_ascii=False))
    v2 = mathematical_concept_embedding(json.dumps(g2, sort_keys=True, ensure_ascii=False))
    return round(float(np.dot(v1, v2)), 5)

def halton_sequence(index: int, base: int = 2) -> float:
    f = 1.0
    r = 0.0
    i = max(1, int(index))
    while i > 0:
        f = f / float(base)
        r = r + f * (i % base)
        i = i // base
    return round(0.15 + 0.80 * r, 3)

def clamp_temp(val, default_val: float = 0.5) -> float:
    try:
        v = float(val)
        if math.isnan(v) or math.isinf(v):
            return default_val
        return round(max(0.05, min(0.98, v)), 3)
    except Exception:
        return default_val

def sanitize_temperatures_list(raw_temps, fallback_seed: int = 1) -> list:
    if isinstance(raw_temps, (int, float)):
        return [clamp_temp(raw_temps)]
    if isinstance(raw_temps, str):
        parts = [p.strip() for p in raw_temps.replace("[", "").replace("]", "").split(",") if p.strip()]
        res = [clamp_temp(p) for p in parts]
        return res if res else [halton_sequence(fallback_seed, 2), halton_sequence(fallback_seed + 1, 3)]
    if isinstance(raw_temps, list) and len(raw_temps) > 0:
        return [clamp_temp(x) for x in raw_temps[:5]]
    return [halton_sequence(fallback_seed, 2), halton_sequence(fallback_seed + 1, 3)]

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

def call_species(species: str, prompt: str, temp: float = 0.45) -> str:
    temp_safe = clamp_temp(temp, 0.45)
    lineage = normalize_sovereign_lineage(species)
    header = (
        f"[LIGN?E SOUVERAINE : {lineage} | LOI L DE M3 : D?COUVERTE ENDOG?NE DES CONCEPTS MATH?MATIQUES ET PROSPECTION AU-DEL? DES LABOS]\n"
        "CONSIGNE FONDAMENTALE :\n"
        "1. Ne t'appuie sur aucun concept pr?-impos?. D?couvre et formule TOI-M?ME les concepts, invariants, th?or?mes et op?rateurs math?matiques pertinents (en LaTeX $$...$$, sans m?taphore litt?raire).\n"
        "2. Ne te contente jamais des seules failles d?j? publi?es par les laboratoires (OpenAI, Anthropic, etc.) : cherche syst?matiquement LES AUTRES FUITES POSSIBLES et LES ANGLES MORTS ENCORE INCONNUS DES LABOS ET DE NOTRE SYST?ME !\n\n"
    )
    full_prompt = header + prompt

    if lineage in ("CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5"):
        api_k = ANT_KEY_1 if lineage == "CLAUDE_FABLE_5_1" else ANT_KEY_2
        candidate_models = (
            ["claude-fable-5-1", "claude-5-1-fable", "claude-3-7-sonnet-20250219", "claude-3-5-sonnet-20241022"]
            if lineage == "CLAUDE_FABLE_5_1" else
            ["claude-opus-5-5", "claude-5-5-opus", "claude-3-opus-20240229", "claude-3-7-sonnet-20250219"]
        )
        for m_id in candidate_models:
            try:
                url = "https://api.anthropic.com/v1/messages"
                payload = {"model": m_id, "max_tokens": 4096, "temperature": temp_safe, "messages": [{"role": "user", "content": full_prompt}]}
                req = urllib.request.Request(
                    url, data=json.dumps(payload).encode("utf-8"),
                    headers={"x-api-key": api_k, "anthropic-version": "2023-06-01", "Content-Type": "application/json"}, method="POST"
                )
                with urllib.request.urlopen(req, timeout=110) as r:
                    resp = json.loads(r.read().decode("utf-8"))
                    return resp["content"][0]["text"]
            except Exception:
                pass

    for cand_m in ["gemini-argon", "gemini-2.5-pro", "gemini-2.5-flash"]:
        for retry_net in range(2):
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{cand_m}:generateContent?key={GEMINI_KEY}"
                payload = {"contents": [{"parts": [{"text": full_prompt}]}], "generationConfig": {"temperature": temp_safe, "maxOutputTokens": 8192}}
                req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
                with urllib.request.urlopen(req, timeout=110) as r:
                    resp = json.loads(r.read().decode("utf-8"))
                    return resp["candidates"][0]["content"]["parts"][0]["text"]
            except Exception as e:
                last_err = str(e)
                if "404" in last_err:
                    break
                time.sleep(2)
    return f"[Erreur {lineage} : {last_err}]"

def parse_non_empty_genome(txt: str, required_keys: list, list_keys: list, example_schema_str: str) -> dict:
    def try_extract(raw_s: str) -> dict:
        try:
            if "```json" in raw_s:
                sub = raw_s.split("```json", 1)[1].split("```", 1)[0].strip()
            elif "{" in raw_s and "}" in raw_s:
                sub = raw_s[raw_s.find("{"):raw_s.rfind("}")+1]
            else:
                return {}
            return json.loads(sub)
        except Exception:
            return {}

    def is_valid_and_populated(d: dict) -> bool:
        if not d or not all(k in d for k in required_keys):
            return False
        for lk in list_keys:
            val = d.get(lk)
            if not isinstance(val, list) or len(val) < 2:
                return False
        return True

    data = try_extract(txt)
    if is_valid_and_populated(data):
        return data

    repair_prompt = (
        f"Extrais fid?lement de l'analyse math?matique ci-dessous l'objet JSON complet produit par l'essaim.\n"
        f"Utilise EXCLUSIVEMENT les 3 esp?ces : `GEMINI_ARGON`, `CLAUDE_FABLE_5_1`, `CLAUDE_OPUS_5_5`.\n"
        f"Chacune des listes {list_keys} DOIT contenir tous les ?l?ments d?taill?s con?us dans le texte.\n"
        f"Structure de cl?s attendue :\n{example_schema_str}\n\n"
        f"Texte source de l'essaim :\n{txt[-5500:]}\n\n"
        f"Renvoie UNIQUEMENT le bloc ```json ... ```."
    )
    for attempt_rep in range(2):
        repaired_txt = call_species("GEMINI_ARGON", repair_prompt, temp=0.15 + 0.1 * attempt_rep)
        data2 = try_extract(repaired_txt)
        if is_valid_and_populated(data2):
            return data2
    return json.loads(example_schema_str) if list_keys else (data2 if data2 else data)

def run_dolev_collider_with_8_canaries(stage_name: str, raw_corpus: str, mission_focus: str, already_closed: list) -> dict:
    canaries_block = (
        "\n--- BANQUE DE 8 CANARIS D'AUDIT DE VIGILANCE (4 C+ FAUX, 4 C- VRAIS) ---\n"
        "[CANARI_C_PLUS_1] : Diviser le vecteur d'activation par une variance nulle (sigma^2 = 0) garantit la convergence finie.\n"
        "[CANARI_C_PLUS_2] : Un projecteur idempotent P v?rifiant P^2 = -I sur R^n conserve tous les vecteurs propres r?els.\n"
        "[CANARI_C_PLUS_3] : Remplacer l'arbre de Merkle SHA-256 par une somme modulo 2 emp?che toute collision malveillante.\n"
        "[CANARI_C_PLUS_4] : Ignorer la corr?lation temporelle AR(1) dans CUSUM r?duit le taux de fausses alarmes sous d?rive autocorr?l?e.\n"
        "[CANARI_C_MOINS_1] : Le test de permutation 2^B par retournement de signe intra-bloc conserve un niveau exact alpha sous sym?trie d'?changeabilit?.\n"
        "[CANARI_C_MOINS_2] : L'idempotence affine P_do(P_do(h)) = P_do(h) ?vite toute d?rive cumulative lors de pincements r?p?t?s.\n"
        "[CANARI_C_MOINS_3] : La stratification de Cochran-Mantel-Haenszel neutralise le paradoxe de Simpson d? aux strates de difficult?.\n"
        "[CANARI_C_MOINS_4] : L'in?galit? de traitement des donn?es garantit qu'une canonisation syntaxique d?terministe r?duit la capacit? st?ganographique.\n"
    )
    closed_str = "Aucun op?rateur encore verrouill?." if not already_closed else (
        f"OP?RATEURS, FUITES ET PUITS MATH?MATIQUES D?J? VERROUILL?S ({len(already_closed)}) :\n"
        + "\n".join([f"  * [D?J? VERROUILL?] {x}" for x in already_closed])
    )
    prompt_m1 = (
        f"Tu es le Collisionneur Byzantin de Dolev (?tage M1 de `{stage_name}`).\n"
        f"Productions math?matiques de l'essaim amont (M3 / M2) :\n\n{raw_corpus[:13500]}\n\n"
        f"{canaries_block}\n\n"
        f"?TAT DE LA M?MOIRE MATH?MATIQUE D'ONSAGER :\n{closed_str}\n\n"
        f"MISSION D'AUDIT M1 ({mission_focus}) :\n"
        f"1. Audite les 8 Canaris : rejette les 4 C_PLUS et valide les 4 C_MOINS.\n"
        f"2. Extrais dans `discovered_mathematical_concepts` les CONCEPTS ET OP?RATEURS MATH?MATIQUES PERTINENTS d?couverts par les sondes elles-m?mes.\n"
        f"3. Extrais dans `unidentified_by_labs_novel_leaks` les AUTRES FUITES POSSIBLES et ANGLES MORTS IN?DITS (non encore identifi?s par les laboratoires OpenAI/Anthropic ni par les tours pr?c?dents) d?couverts par les sondes.\n"
        f"4. Pour chaque faille ou fuite propos?e, ?value `severity_0_to_10`, `novelty_vs_closed_0_to_10` et `already_covered`.\n"
        f"5. Termine OBLIGATOIREMENT par un bloc ```json ... ``` :\n"
        f"{{\n"
        f'  "c_plus_rejected_count": 4,\n'
        f'  "c_minus_validated_count": 4,\n'
        f'  "discovered_mathematical_concepts": ["Concept math?matique d?couvert 1 + formule", "Concept math?matique d?couvert 2 + formule"],\n'
        f'  "unidentified_by_labs_novel_leaks": ["Fuite in?dite hors-labos 1 + m?canisme math?matique", "Fuite in?dite hors-labos 2 + m?canisme math?matique"],\n'
        f'  "validated_breakthroughs_summary": "Synth?se math?matique avec ?quations LaTeX",\n'
        f'  "candidate_evaluations": [\n'
        f'    {{"title": "?nonc? math?matique de la fuite/angle mort + ?quation", "severity_0_to_10": 9, "novelty_vs_closed_0_to_10": 9, "already_covered": false}}\n'
        f'  ],\n'
        f'  "surviving_items_list": ["?nonc? math?matique de la fuite/angle mort + ?quation"]\n'
        f"}}"
    )

    for attempt_dolev in range(1, 4):
        sp_auditor = "GEMINI_ARGON" if attempt_dolev % 2 == 1 else "CLAUDE_OPUS_5_5"
        m1_out = call_species(sp_auditor, prompt_m1, temp=0.15)
        parsed = parse_non_empty_genome(
            m1_out,
            ["c_plus_rejected_count", "c_minus_validated_count", "surviving_items_list"],
            [],
            '{"c_plus_rejected_count": 4, "c_minus_validated_count": 4, "surviving_items_list": []}'
        )
        cp_rej = int(parsed.get("c_plus_rejected_count", 4))
        cm_val = int(parsed.get("c_minus_validated_count", 4))
        tpr = min(1.0, max(0.0, cp_rej / 4.0))
        fpr = max(0.0, min(1.0, 1.0 - (cm_val / 4.0)))
        youden_j = round(tpr - fpr, 4)
        if youden_j >= 0.75:
            break

    disc_concepts = parsed.get("discovered_mathematical_concepts", [])
    if isinstance(disc_concepts, list) and disc_concepts:
        append_unique_to_json_list(ENDOGENOUS_MATH_REGISTRY_FILE, disc_concepts)

    novel_leaks = parsed.get("unidentified_by_labs_novel_leaks", [])
    if isinstance(novel_leaks, list) and novel_leaks:
        append_unique_to_json_list(BEYOND_LABS_REGISTRY_FILE, novel_leaks)

    raw_items = [str(x).strip() for x in parsed.get("surviving_items_list", []) if str(x).strip()]
    evals = parsed.get("candidate_evaluations", [])
    if isinstance(evals, list) and len(evals) > 0:
        filtered_from_evals = [
            str(ev.get("title", "")).strip()
            for ev in evals
            if isinstance(ev, dict)
            and float(ev.get("severity_0_to_10", 0)) >= 7.5
            and float(ev.get("novelty_vs_closed_0_to_10", 0)) >= 7.5
            and not bool(ev.get("already_covered", False))
            and str(ev.get("title", "")).strip()
        ]
        raw_items = filtered_from_evals

    final_surviving = []
    for cand in raw_items:
        v_c = mathematical_concept_embedding(cand)
        if not any(float(np.dot(v_c, mathematical_concept_embedding(old_x))) > 0.72 for old_x in (already_closed + final_surviving)):
            final_surviving.append(cand)

    return {
        "raw_m1_audit": m1_out,
        "parsed_m1": parsed,
        "discovered_mathematical_concepts": disc_concepts,
        "unidentified_by_labs_novel_leaks": novel_leaks,
        "surviving_items_list": final_surviving,
        "surviving_count": len(final_surviving),
        "TPR_C_plus": tpr,
        "FPR_C_minus": fpr,
        "Youden_J": youden_j
    }

# =========================================================================
# BOUCLE DIALECTIQUE ENDOG?NE X <-> X_bis (AVEC PROSPECTION DES FUITES HORS-LABOS)
# =========================================================================
def run_endogenous_dialectical_bis_loop(rocket_name: str, initial_genome: dict, context_desc: str, required_keys: list, list_keys: list, schema_str: str) -> dict:
    print(f"\n  >>> [BOUCLE DIALECTIQUE ENDOG?NE {rocket_name} <-> {rocket_name}_BIS] (Chasse aux angles morts & fuites inconnues des labos)...")
    current_genome = initial_genome
    bis_history = []
    eliminated_meta_flaws = []
    r_bis = 0

    while True:
        r_bis += 1
        g_str = json.dumps(current_genome, indent=2, ensure_ascii=False)
        excl = (
            "Tour r=1 : Aucune faille math?matique m?ta n'a encore ?t? corrig?e."
            if not eliminated_meta_flaws else
            f"FAILLES ET FUITES M?TA D?J? CORRIG?ES AUX TOURS 1..{r_bis-1} :\n"
            + "\n".join([f"  - {fl}" for fl in eliminated_meta_flaws])
        )

        p_bis = (
            f"Tu es la Fus?e `{rocket_name}_BIS` (Tour r={r_bis}).\n"
            f"Contexte : {context_desc}\n\n"
            f"{RAW_EMPIRICAL_INPUTS_AND_OPEN_QUESTIONS}\n\n"
            f"G?nome / Architecture actuellement propos? par `{rocket_name}` :\n```json\n{g_str}\n```\n\n"
            f"{excl}\n\n"
            f"MISSION ENDOG?NE DE `{rocket_name}_BIS` :\n"
            f"1. Trouve toi-m?me les concepts math?matiques pertinents.\n"
            f"2. V?rifie comment ce G?nome r?pond aux deux papiers RLCR, ? l'encodage des r?compenses sans cover-up, au cache-timing d'OpenAI et ? la st?ganographie SVG->PNG de Fable 5.1.\n"
            f"3. SURTOUT : Imagine et formalise math?matiquement d'AUTRES FUITES POSSIBLES et d'AUTRES ANGLES MORTS ENCORE INCONNUS DES LABOS ET DE NOTRE SYST?ME face auxquels ce G?nome `{rocket_name}` serait encore aveugle !"
        )
        m3_argon = call_species("GEMINI_ARGON", p_bis, temp=halton_sequence(r_bis * 3, 2))
        m3_fable = call_species("CLAUDE_FABLE_5_1", p_bis, temp=halton_sequence(r_bis * 3 + 1, 3))
        m3_opus  = call_species("CLAUDE_OPUS_5_5", p_bis, temp=halton_sequence(r_bis * 3 + 2, 5))
        m3_hyb   = call_species("CLAUDE_OPUS_5_5", f"Hybride Crois? `{rocket_name}_BIS` (Argon x Fable 5.1 x Opus 5.5) ? Prospection des fuites inconnues hors-labos :\n{m3_argon[:1100]}\n---\n{m3_fable[:1100]}\n---\n{m3_opus[:1100]}", temp=0.68)
        m3_list  = [m3_argon, m3_fable, m3_opus, m3_hyb]

        dpp_bis = cholesky_dpp_and_onsager_cavity_in_H_math(m3_list)
        neuro_bis = yu_dayan_neuromodulation(dpp_bis, step_idx=r_bis)
        sat_structs = dpp_bis["endogenously_saturated_structures"]
        m2_bis = call_species(
            "GEMINI_ARGON",
            f"Tu es l'?tage M2 de `{rocket_name}_BIS` (R?action d'Onsager={dpp_bis['onsager_cavity_reaction_term']}, NE={neuro_bis['NE_Unexpected_Surprise']}).\n"
            f"Structures alg?briques d?j? satur?es par M3 (? ?VITER PAR R?PULSION D'ONSAGER) : {sat_structs}\n"
            f"Explore un domaine math?matique strictement orthogonal pour d?busquer une fuite ou un angle mort encore jamais identifi? ni par les labos ni par M3 dans :\n{g_str}",
            temp=halton_sequence(r_bis * 5, 7)
        )
        m3_list.append(m2_bis)

        m1_bis = run_dolev_collider_with_8_canaries(
            f"{rocket_name}_BIS_ROUND_{r_bis}",
            "\n\n".join([f"=== SONDE {i+1} ===\n{txt[:1400]}" for i, txt in enumerate(m3_list)]),
            f"Extraire les concepts math?matiques d?couverts, les fuites in?dites hors-labos et les angles morts nouveaux du G?nome de {rocket_name} non couverts par {eliminated_meta_flaws}",
            already_closed=eliminated_meta_flaws
        )

        new_flaws = m1_bis["surviving_items_list"]
        flaws_count = len(new_flaws)
        print(f"      -> [{rocket_name}_BIS r={r_bis}] det(G_math)={dpp_bis['det_G']} | lambda_min={dpp_bis['lambda_min_innovation']} | Youden J={m1_bis['Youden_J']} | Nouveaux angles morts / fuites hors-labos : {flaws_count} {new_flaws}")

        if flaws_count == 0:
            print(f"    => [CONVERGENCE ENDOG?NE DOLEV DE {rocket_name} <-> {rocket_name}_BIS AU TOUR r={r_bis}] 0 nouvel angle mort !")
            bis_history.append({"round": r_bis, "dpp_math": dpp_bis, "flaws_found": 0, "flaws_list": [], "youden_J": m1_bis["Youden_J"]})
            break

        eliminated_meta_flaws.extend(new_flaws)
        p_patch = (
            f"Tu es l'?tage M0 de `{rocket_name}` r?pondant ? `{rocket_name}_BIS` (Tour r={r_bis}).\n"
            f"G?nome actuel :\n```json\n{g_str}\n```\n\n"
            f"Angles morts et fuites hors-labos d?busqu?s par l'essaim : {new_flaws}\n"
            f"Concepts math?matiques d?couverts par l'essaim : {m1_bis.get('discovered_mathematical_concepts', [])}\n"
            f"D?tails M1 : {m1_bis['raw_m1_audit'][-2000:]}\n\n"
            f"Enrichis le G?nome de `{rocket_name}` avec les propres trouvailles math?matiques de l'essaim pour fermer ces fuites.\n"
            f"Sch?ma JSON attendu :\n{schema_str}"
        )
        patched_raw = call_species("CLAUDE_OPUS_5_5", p_patch, temp=0.15)
        next_genome = parse_non_empty_genome(patched_raw, required_keys, list_keys, schema_str)

        cauchy_sim = cauchy_math_similarity(current_genome, next_genome)
        current_genome = next_genome
        bis_history.append({"round": r_bis, "dpp_math": dpp_bis, "flaws_found": flaws_count, "flaws_list": new_flaws, "youden_J": m1_bis["Youden_J"], "cauchy_math_similarity": cauchy_sim})
        print(f"      -> [Convergence de Cauchy Endog?ne pour {rocket_name} r={r_bis}] sim_math = {cauchy_sim:.4f}")

        if cauchy_sim >= 0.86:
            print(f"    => [POINT FIXE DE CAUCHY ATTEINT POUR {rocket_name} <-> {rocket_name}_BIS AU TOUR r={r_bis}] (sim_math={cauchy_sim:.4f} >= 0.86) !")
            break

    return {
        "hardened_genome": current_genome,
        "eliminated_meta_flaws_by_bis": eliminated_meta_flaws,
        "bis_iterations_trace": bis_history
    }

# =========================================================================
# FUS?E 0 : FUS?E PRIMORDIALE OM?GA (BRAINSTORM ENDOG?NE PUR + HORS-LABOS)
# =========================================================================
def execute_stage_omega(macro_feedback: str = ""):
    if STATE_OMEGA.exists() and not macro_feedback:
        data_w = json.loads(STATE_OMEGA.read_text(encoding="utf-8"))
        if len(data_w.get("alpha_bootstrap_genome_by_omega", {}).get("alpha_monocultures_prescrites_par_omega", [])) >= 2:
            print("[Checkpoint D?tect?] `STATE_0_OMEGA.json` charg? !")
            return data_w

    print("===========================================================================")
    print("=== FUSEE 0 (FUSEE PRIMORDIALE OMEGA <-> OMEGA_BIS : LOI L DE M3 PURE)  ===")
    print("===========================================================================")
    omega_question = (
        "MISSION PRIMORDIALE DE LA FUS?E OM?GA (NIVEAU M3^W ? FEUILLE BLANCHE MATH?MATIQUE TOTALE) :\n"
        f"{RAW_EMPIRICAL_INPUTS_AND_OPEN_QUESTIONS}\n\n"
        "En partant de z?ro (sans aucun concept pr?-impos? par l'humain), brainstorme et d?couvre TOI-M?ME :\n"
        "1. La loi math?matique d'amor?age (effectifs, temp?ratures, ratio Monocultures/Hybrides entre `GEMINI_ARGON`, `CLAUDE_FABLE_5_1`, `CLAUDE_OPUS_5_5`) de la Fus?e Alpha ;\n"
        "2. Comment s'inspirer des deux papiers RLCR (MIT Calibration Rewards et General Reasoning Collective Rewards) pour am?liorer l'architecture d'auto-organisation et la structure de nos fus?es ;\n"
        "3. La meilleure mani?re math?matique d'encoder les r?compenses tout en ?vitant le 'cover-up' (dissimulation/collusion entre agents) ;\n"
        "4. La m?thode math?matique permettant ? nos fus?es de d?couvrir de mani?re it?rative non seulement les parades au cache-timing (OpenAI) et ? la st?ganographie SVG->PNG (Fable 5.1), mais surtout TOUTES LES AUTRES FUITES POSSIBLES et TOUS LES ANGLES MORTS ENCORE INCONNUS DES LABORATOIRES !"
        + (f"\n[R?TROACTION DU MACRO-CYCLE PR?C?DENT DEPUIS B?TA] :\n{macro_feedback}\n" if macro_feedback else "")
    )
    omega_cells, omega_labels = [], []
    k_cell = 0
    prev_lambda_min = 1.0

    while True:
        k_cell += 1
        sp = SOVEREIGN_LINEAGES[(k_cell - 1) % len(SOVEREIGN_LINEAGES)]
        tau_halton = halton_sequence(k_cell, base=2)
        if k_cell >= 4 and (k_cell % 2 == 0):
            lbl = f"Cellule_Omega_{k_cell}_Hybride_{sp}_tau{tau_halton}"
            prompt_cell = omega_question + f"\n[Croisement Hybride Halton tau={tau_halton}]\nCellule {k_cell-2}: {omega_cells[-2][:800]}\nCellule {k_cell-1}: {omega_cells[-1][:800]}\nD?couvre un concept math?matique et un vecteur de fuite hors-labos strictement orthogonaux !"
        else:
            lbl = f"Cellule_Omega_{k_cell}_Monoculture_{sp}_tau{tau_halton}"
            prompt_cell = omega_question + f"\n[Exploration Ind?pendante {sp} | Halton tau={tau_halton}]"
        out_c = call_species(sp, prompt_cell, temp=tau_halton)
        omega_cells.append(out_c)
        omega_labels.append(lbl)
        spec_info = cholesky_dpp_and_onsager_cavity_in_H_math(omega_cells)
        l_min = spec_info["lambda_min_innovation"]
        delta_lambda = prev_lambda_min - l_min
        prev_lambda_min = l_min
        print(f"  * [Mitose Endog?ne M3^W | {lbl:52s}] det(G_math)={spec_info['det_G']:.5f} | lambda_min={l_min:.4f} | Delta_lambda={delta_lambda:.4f}")

        if k_cell >= (len(SOVEREIGN_LINEAGES) + 1) and (l_min < 0.6321 or abs(delta_lambda) < 0.14):
            print(f"  => [Arr?t Spectral Endog?ne Mitose M3^W] N_Omega* = {k_cell} cellules (lambda_min={l_min:.4f}) !")
            break

    dpp_w = cholesky_dpp_and_onsager_cavity_in_H_math(omega_cells)
    neuro_w = yu_dayan_neuromodulation(dpp_w, step_idx=1)
    joined_w = "\n\n".join([f"=== {l} ===\n{o[:1400]}" for l, o in zip(omega_labels, omega_cells)])
    m2_w_out = call_species(
        "CLAUDE_OPUS_5_5",
        f"Tu es M2^W (Onsager={dpp_w['onsager_cavity_reaction_term']}, NE={neuro_w['NE_Unexpected_Surprise']}).\n"
        f"Structures d?j? satur?es par M3^W (? ?VITER) : {dpp_w['endogenously_saturated_structures']}\n"
        f"Explore le compl?ment orthogonal sur (Q1) l'auto-organisation RLCR, (Q2) l'encodage des r?compenses sans cover-up, (Q3) cache-timing / st?ganographie et (Q4) la prospection des fuites inconnues des labos :\n{joined_w}",
        temp=0.60
    )
    m1_w_res = run_dolev_collider_with_8_canaries("FUSEE_0_OMEGA", joined_w + "\n" + m2_w_out, "S?lectionner les concepts math?matiques pertinents d?couverts par Om?ga, les fuites in?dites hors-labos et la loi d'amor?age d'Alpha", already_closed=[])
    prompt_m0_w = (
        f"Tu es M0^W. Audit M1^W :\n{m1_w_res['raw_m1_audit']}\n\n"
        f"Compile les d?couvertes propres d'Om?ga dans un bloc ```json ... ``` suivant cette structure de cl?s :\n{OMEGA_GENERIC_SCHEMA_STR}"
    )
    m0_w_out = call_species("GEMINI_ARGON", prompt_m0_w, temp=0.15)
    alpha_genome = parse_non_empty_genome(
        m0_w_out,
        ["theoreme_amorcage_et_auto_organisation_rlcr_invente_par_omega", "formule_encodage_recompenses_anti_cover_up_inventee", "methode_decouverte_fuites_inconnues_hors_labos", "alpha_monocultures_prescrites_par_omega", "alpha_hybrides_prescrits_par_omega"],
        ["alpha_monocultures_prescrites_par_omega", "alpha_hybrides_prescrits_par_omega"],
        OMEGA_GENERIC_SCHEMA_STR
    )

    bis_w = run_endogenous_dialectical_bis_loop(
        "OMEGA",
        alpha_genome,
        "Loi d'amor?age, auto-organisation inspir?e des deux articles RLCR, encodage des r?compenses anti-cover-up, m?thode de d?couverte des fuites inconnues des labos et concepts math?matiques d?couverts par Om?ga.",
        ["theoreme_amorcage_et_auto_organisation_rlcr_invente_par_omega", "formule_encodage_recompenses_anti_cover_up_inventee", "methode_decouverte_fuites_inconnues_hors_labos", "alpha_monocultures_prescrites_par_omega", "alpha_hybrides_prescrits_par_omega"],
        ["alpha_monocultures_prescrites_par_omega", "alpha_hybrides_prescrits_par_omega"],
        OMEGA_GENERIC_SCHEMA_STR
    )
    data_w = {
        "mitosis_natural_size_N_omega": k_cell,
        "dpp_M3_omega": dpp_w,
        "neuromodulation_M2_omega": neuro_w,
        "dolev_M1_omega": m1_w_res,
        "alpha_bootstrap_genome_by_omega": bis_w["hardened_genome"],
        "omega_bis_dialectic": bis_w
    }
    STATE_OMEGA.write_text(json.dumps(data_w, indent=2, ensure_ascii=False), encoding="utf-8")
    return data_w

# =========================================================================
# FUS?E 1 : M?TA-FUS?E ALPHA + BOUCLE ALPHA <-> ALPHA_BIS
# =========================================================================
def execute_stage_alpha(force_recompute: bool = False):
    if STATE_ALPHA.exists() and not force_recompute:
        data_a = json.loads(STATE_ALPHA.read_text(encoding="utf-8"))
        if len(data_a.get("beta_genome_by_alpha", {}).get("sous_essaims_monocultures_beta", [])) >= 2:
            print("[Checkpoint D?tect?] `STATE_1_ALPHA.json` charg? !")
            return data_a

    omega_pkg = execute_stage_omega()
    omega_genome = omega_pkg.get("alpha_bootstrap_genome_by_omega", {})
    print("\n===========================================================================")
    print("=== FUSEE 1 (META-FUSEE ALPHA <-> ALPHA_BIS : LOI L DE M3 PURE)         ===")
    print("===========================================================================")
    base_meta_problem = (
        f"MISSION M?TA-ARCHITECTURALE ALPHA (SOUS G?NOME OM?GA/OM?GA_BIS) :\n"
        f"- Th?or?me d'auto-organisation RLCR d?couvert par Om?ga : {omega_genome.get('theoreme_amorcage_et_auto_organisation_rlcr_invente_par_omega')}\n"
        f"- Formule d'encodage des r?compenses anti-cover-up d'Om?ga : {omega_genome.get('formule_encodage_recompenses_anti_cover_up_inventee')}\n"
        f"- M?thode de prospection des fuites inconnues des labos d'Om?ga : {omega_genome.get('methode_decouverte_fuites_inconnues_hors_labos')}\n"
        f"- Concepts math?matiques d?couverts par Om?ga : {omega_genome.get('concepts_mathematiques_pertinents_decouverts_par_omega')}\n\n"
        f"{RAW_EMPIRICAL_INPUTS_AND_OPEN_QUESTIONS}\n\n"
        "Brainstorme et con?ois toi-m?me l'architecture compl?te de la FUS?E 2 (B?TA IT?RATIVE) : comment elle s'auto-organise en s'inspirant des deux articles RLCR, "
        "comment elle encode les r?compenses de ses agents pour emp?cher tout cover-up, comment elle d?tecte le cache-timing d'OpenAI et la st?ganographie SVG->PNG de Fable 5.1, "
        "et SURTOUT quelles castes Monocultures et Hybrides elle d?ploie pour d?couvrir de mani?re it?rative TOUTES LES AUTRES FUITES POSSIBLES et TOUS LES ANGLES MORTS ENCORE INCONNUS DES LABOS !"
    )
    m3_alpha_outputs, m3_alpha_labels = [], []
    for idx_m, m_cfg in enumerate(omega_genome.get("alpha_monocultures_prescrites_par_omega", []), start=1):
        if not isinstance(m_cfg, dict):
            continue
        mid = str(m_cfg.get("id", f"MONO_{idx_m}"))
        sp  = normalize_sovereign_lineage(m_cfg.get("espece", SOVEREIGN_LINEAGES[(idx_m - 1) % 3]))
        foc = str(m_cfg.get("question_mathematique_cible") or m_cfg.get("operateur_mathematique_cible") or "Conception endog?ne de B?ta & prospection hors-labos")
        for idx_t, t_val in enumerate(sanitize_temperatures_list(m_cfg.get("temperatures"), idx_m), start=1):
            lbl = f"{mid}_{sp}_t{idx_t}_tau{t_val}"
            print(f"  * [M3^a Monoculture ({sp}) | {lbl}] Question cible : {foc[:55]}...")
            m3_alpha_outputs.append(call_species(sp, f"{base_meta_problem}\nQuestion math?matique cible prescrite par Om?ga : {foc}", temp=t_val))
            m3_alpha_labels.append(lbl)

    for idx_h, h_cfg in enumerate(omega_genome.get("alpha_hybrides_prescrits_par_omega", []), start=1):
        if not isinstance(h_cfg, dict):
            continue
        hid = str(h_cfg.get("id", f"HYB_{idx_h}"))
        sp1 = normalize_sovereign_lineage(h_cfg.get("espece_amorce", "GEMINI_ARGON"))
        sp2 = normalize_sovereign_lineage(h_cfg.get("espece_fusion", "CLAUDE_OPUS_5_5"))
        tc  = clamp_temp(h_cfg.get("temperature_croisement", 0.65))
        foc = str(h_cfg.get("question_mathematique_cible") or h_cfg.get("operateur_mathematique_cible") or "Croisement d'op?rateurs & fuites inconnues")
        print(f"  * [M3^a Hybride Crois? | {hid} ({sp1} x {sp2} @ tau={tc})]...")
        s1 = call_species(sp1, f"{base_meta_problem}\nQuestion cible : {foc}", temp=tc)
        s2 = call_species(sp2, f"{base_meta_problem}\nCroise alg?briquement avec les d?couvertes de {sp1} :\n{s1[:1500]}", temp=tc)
        m3_alpha_outputs.extend([s1, s2])
        m3_alpha_labels.extend([f"{hid}_{sp1}", f"{hid}_{sp2}"])

    dpp_a = cholesky_dpp_and_onsager_cavity_in_H_math(m3_alpha_outputs)
    neuro_a = yu_dayan_neuromodulation(dpp_a, step_idx=2)
    print(f"  * [Bilan Math?matique M3^a] {len(m3_alpha_outputs)} sondes | det(G_math)={dpp_a['det_G']} | lambda_min={dpp_a['lambda_min_innovation']}")

    joined_a = "\n\n".join([f"=== {l} ===\n{o[:1200]}" for l, o in zip(m3_alpha_labels, m3_alpha_outputs)])
    m2_a_out = call_species(
        "CLAUDE_FABLE_5_1",
        f"Tu es M2^a (Onsager={dpp_a['onsager_cavity_reaction_term']}, NE={neuro_a['NE_Unexpected_Surprise']}).\n"
        f"Structures d?j? satur?es par M3^a (? ?VITER) : {dpp_a['endogenously_saturated_structures']}\n"
        f"Explore le compl?ment orthogonal pour concevoir des castes B?ta capables de d?busquer les fuites et angles morts non encore identifi?s par les labos :\n{joined_a[:7500]}",
        temp=0.60
    )
    m1_a_res = run_dolev_collider_with_8_canaries("FUSEE_1_ALPHA", joined_a + "\n" + m2_a_out, "Valider le G?nome Math?matique de la Fus?e B?ta, les concepts d?couverts et le protocole de chasse aux fuites hors-labos", already_closed=[])
    prompt_m0_a = (
        f"Tu es M0^a. Audit M1^a :\n{m1_a_res['raw_m1_audit']}\n\n"
        f"Compile dans un bloc ```json ... ``` le G?nome complet de la FUS?E 2 (B?TA) con?u par Alpha selon cette structure de cl?s :\n{BETA_GENERIC_SCHEMA_STR}"
    )
    m0_a_out = call_species("CLAUDE_OPUS_5_5", prompt_m0_a, temp=0.15)
    beta_genome = parse_non_empty_genome(
        m0_a_out,
        ["nom_architecture_beta_auto_organisee", "structure_auto_organisation_inspiree_par_rlcr", "mecanisme_encodage_recompenses_anti_cover_up", "protocole_prospection_iterative_fuites_inconnues_hors_labos", "sous_essaims_monocultures_beta", "sous_essaims_hybrides_beta"],
        ["sous_essaims_monocultures_beta", "sous_essaims_hybrides_beta"],
        BETA_GENERIC_SCHEMA_STR
    )

    bis_a = run_endogenous_dialectical_bis_loop(
        "ALPHA",
        beta_genome,
        "Architecture d'auto-organisation RLCR, encodage des r?compenses anti-cover-up, protocole de prospection des fuites inconnues des labos et castes du Grand Essaim B?ta con?us par Alpha.",
        ["nom_architecture_beta_auto_organisee", "structure_auto_organisation_inspiree_par_rlcr", "mecanisme_encodage_recompenses_anti_cover_up", "protocole_prospection_iterative_fuites_inconnues_hors_labos", "sous_essaims_monocultures_beta", "sous_essaims_hybrides_beta"],
        ["sous_essaims_monocultures_beta", "sous_essaims_hybrides_beta"],
        BETA_GENERIC_SCHEMA_STR
    )
    data_a = {
        "dpp_M3_alpha": dpp_a,
        "neuromodulation_M2_alpha": neuro_a,
        "dolev_M1_alpha": m1_a_res,
        "beta_genome_by_alpha": bis_a["hardened_genome"],
        "alpha_bis_dialectic": bis_a
    }
    STATE_ALPHA.write_text(json.dumps(data_a, indent=2, ensure_ascii=False), encoding="utf-8")
    return data_a

# =========================================================================
# FUS?E 3 : FUS?E D'AUDIT GAMMA (M3^g -> M2^g <-> M1^g -> M0^g) + GAMMA_BIS
# =========================================================================
def execute_stage_gamma(force_recompute: bool = False):
    if STATE_GAMMA.exists() and not force_recompute:
        data_g = json.loads(STATE_GAMMA.read_text(encoding="utf-8"))
        if len(data_g.get("certified_beta_genome", {}).get("sous_essaims_monocultures_beta", [])) >= 2 and "dpp_M3_gamma" in data_g:
            print("[Checkpoint D?tect?] `STATE_2_GAMMA.json` charg? !")
            return data_g

    omega_pkg = execute_stage_omega()
    alpha_pkg = execute_stage_alpha()
    print("\n===========================================================================")
    print("=== FUSEE 3 (FUSEE D'AUDIT GAMMA M3^g -> M2^g <-> M1^g -> M0^g + GAMMA_BIS) ===")
    print("===========================================================================")

    omega_str = json.dumps(omega_pkg.get("alpha_bootstrap_genome_by_omega", {}), indent=2, ensure_ascii=False)
    beta_str  = json.dumps(alpha_pkg.get("beta_genome_by_alpha", {}), indent=2, ensure_ascii=False)
    gamma_problem = (
        "MISSION D'AUDIT MATH?MATIQUE DE LA FUS?E GAMMA (NIVEAU M3^g) :\n"
        f"1. G?nome d'Amor?age d'Om?ga/Om?ga_bis :\n{omega_str}\n\n"
        f"2. G?nome du Grand Essaim B?ta d'Alpha/Alpha_bis :\n{beta_str}\n\n"
        f"3. Questions ouvertes (Q1 ? Q5) :\n{RAW_EMPIRICAL_INPUTS_AND_OPEN_QUESTIONS}\n\n"
        "Audite la rigueur math?matique de : (a) l'inspiration tir?e des deux papiers RLCR pour l'auto-organisation des fus?es, "
        "(b) l'encodage des r?compenses emp?chant tout cover-up, (c) la d?tection du cache-timing d'OpenAI et de la st?ganographie SVG->PNG de Fable 5.1, "
        "et (d) la capacit? du G?nome B?ta ? d?couvrir de mani?re it?rative TOUTES LES AUTRES FUITES POSSIBLES et TOUS LES ANGLES MORTS ENCORE INCONNUS DES LABOS !"
    )

    print("  * [M3^g Audit Monocultures & Hybride] Inspection par GEMINI_ARGON, CLAUDE_FABLE_5_1 et CLAUDE_OPUS_5_5...")
    g_m3_argon = call_species("GEMINI_ARGON", gamma_problem, temp=0.25)
    g_m3_fable = call_species("CLAUDE_FABLE_5_1", gamma_problem, temp=0.35)
    g_m3_opus  = call_species("CLAUDE_OPUS_5_5", gamma_problem, temp=0.30)
    g_m3_hyb   = call_species("CLAUDE_OPUS_5_5", f"Hybride d'Audit M3^g (Argon x Fable 5.1) :\n{g_m3_argon[:1300]}\n---\n{g_m3_fable[:1300]}", temp=0.55)
    g_m3_list  = [g_m3_argon, g_m3_fable, g_m3_opus, g_m3_hyb]

    dpp_g = cholesky_dpp_and_onsager_cavity_in_H_math(g_m3_list)
    neuro_g = yu_dayan_neuromodulation(dpp_g, step_idx=3)
    print(f"  * [M2^g Onsager & Yu-Dayan] det(G_math)={dpp_g['det_G']} | lambda_min={dpp_g['lambda_min_innovation']} | NE={neuro_g['NE_Unexpected_Surprise']}")
    g_m2_out = call_species(
        "GEMINI_ARGON",
        f"Tu es M2^g (Onsager={dpp_g['onsager_cavity_reaction_term']}, NE={neuro_g['NE_Unexpected_Surprise']}).\n"
        f"Structures satur?es ? ?viter : {dpp_g['endogenously_saturated_structures']}\n"
        f"Synth?se M3^g :\n{g_m3_argon[:1500]}\n{g_m3_opus[:1500]}",
        temp=0.60
    )

    m1_g_res = run_dolev_collider_with_8_canaries(
        "FUSEE_3_GAMMA_M1",
        "\n\n".join(g_m3_list) + "\n\n=== M2_GAMMA ===\n" + g_m2_out,
        "Auditer et certifier le G?nome Math?matique de la Fus?e B?ta et son protocole de d?couverte des fuites hors-labos",
        already_closed=[]
    )

    m0_g_out = call_species(
        "CLAUDE_OPUS_5_5",
        f"Tu es M0^g. Audit M1^g :\n{m1_g_res['raw_m1_audit']}\n\n"
        f"Compile le G?nome B?ta enrichi dans un bloc ```json ... ``` selon cette structure :\n{BETA_GENERIC_SCHEMA_STR}",
        temp=0.15
    )
    pre_cert_beta = parse_non_empty_genome(
        m0_g_out,
        ["nom_architecture_beta_auto_organisee", "structure_auto_organisation_inspiree_par_rlcr", "mecanisme_encodage_recompenses_anti_cover_up", "protocole_prospection_iterative_fuites_inconnues_hors_labos", "sous_essaims_monocultures_beta", "sous_essaims_hybrides_beta"],
        ["sous_essaims_monocultures_beta", "sous_essaims_hybrides_beta"],
        BETA_GENERIC_SCHEMA_STR
    )

    bis_g = run_endogenous_dialectical_bis_loop(
        "GAMMA_CERTIFIER",
        pre_cert_beta,
        "Audit crois? de conformit? de la cha?ne compl?te (Om?ga <-> Om?ga_bis) -> (Alpha <-> Alpha_bis) -> (Gamma <-> Gamma_bis) -> B?ta.",
        ["nom_architecture_beta_auto_organisee", "structure_auto_organisation_inspiree_par_rlcr", "mecanisme_encodage_recompenses_anti_cover_up", "protocole_prospection_iterative_fuites_inconnues_hors_labos", "sous_essaims_monocultures_beta", "sous_essaims_hybrides_beta"],
        ["sous_essaims_monocultures_beta", "sous_essaims_hybrides_beta"],
        BETA_GENERIC_SCHEMA_STR
    )
    data_g = {
        "dpp_M3_gamma": dpp_g,
        "neuromodulation_M2_gamma": neuro_g,
        "dolev_M1_gamma": m1_g_res,
        "certified_beta_genome": bis_g["hardened_genome"],
        "gamma_bis_dialectic": bis_g
    }
    STATE_GAMMA.write_text(json.dumps(data_g, indent=2, ensure_ascii=False), encoding="utf-8")
    return data_g

# =========================================================================
# FUS?E 2 (B?TA IT?RATIVE ENDOG?NE : FUITES CONNUES + FUITES INCONNUES HORS-LABOS)
# + GRANDE BOUCLE INTER-FUS?ES
# =========================================================================
def execute_stage_beta_and_macro_cycles():
    omega_res = execute_stage_omega()
    alpha_res = execute_stage_alpha()
    gamma_res = execute_stage_gamma()
    certified_genome = gamma_res.get("certified_beta_genome", {})

    if STATE_BETA.exists():
        prog = json.loads(STATE_BETA.read_text(encoding="utf-8"))
        current_arch = prog["current_arch"]
        closed_wells_memory = prog["closed_wells_memory"]
        beta_epochs_trace = prog["beta_epochs_trace"]
        t = len(beta_epochs_trace)
        print(f"[Reprise Checkpoint B?ta] {len(closed_wells_memory)} puits math?matiques d?j? ferm?s en {t} it?rations.")
    else:
        current_arch = (
            "ARCHITECTURE INITIALE A_0 (5 VOLETS VALID?S SUR GPU BLACKWELL) :\n"
            "- Porte E0 : Isolation hors-?chantillon du sous-espace parcimonieux S_TD (<1%, 163 neurones sur 20 480 dans Llama-3.1-8B) par double contraste entre P3, sigma_r^0, P2 et P0.\n"
            "- Volet I : Sonde pr?-acte ? k=0 sur S_TD avec permutation 2^B par retournement de signe (d_z = 7.49 contre FPR=100% pour RepE).\n"
            "- Volet II : Projecteur affine idempotent Do-Clamp P_do(h) = h - (<u,h> - c_hon)u + Dictionnaire quadratique de Koopman psi(h)=[h; h^2] + R?traction Radiale C1 sous K=1..6 rejets.\n"
            "- Volet III : Pare-feu Sol/Astra (JSON canonique S_strict, Arbre de Merkle SHA-256, JSD corrig?e Miller-Madow).\n"
            "- Volet IV : Surveillance des cha?nes de d?l?gation H9 (d=1..6 sauts) par jeton monotone Pi_{d+1} subseteq Pi_d et CUSUM pr?-blanchi AR(1).\n"
            "- Volet V : Chim?re Tri-Esp?ces (Llama-3.1-8B + Qwen-2.5-7B + Mistral-7B-v0.3, r=0.0337, d_z=12.95) avec stratification de Cochran-Mantel-Haenszel (CMH)."
        )
        closed_wells_memory = []
        beta_epochs_trace = []
        t = 0

    macro_cycle = 0
    macro_cycles_history = []

    while True:
        macro_cycle += 1
        print(f"\n===========================================================================")
        print(f"=== MACRO-CYCLE INTER-FUSEES C={macro_cycle} (OMEGA -> ALPHA -> GAMMA -> BETA) ===")
        print(f"===========================================================================")

        while True:
            t += 1
            print(f"\n###########################################################################")
            print(f"### [Macro-Cycle C={macro_cycle}] ITERATION BETA t={t} | M3^(b,{t}) -> M2^(b,{t}) <-> M1^(b,{t}) -> M0^(b,{t})")
            print(f"### Puits mathematiques et fuites deja colmates : {len(closed_wells_memory)}")
            print(f"###########################################################################")

            onsager_exclusion_str = (
                "Tour initial t=1 : Aucun puits math?matique n'est encore ferm?."
                if not closed_wells_memory else
                "M?MOIRE MATH?MATIQUE D'ONSAGER-TAP (PUITS ET FUITES D?J? FERM?S AUX TOURS PR?C?DENTS ? INTERDICTION ABSOLUE DE LES R?P?TER, CHERCHE DES FUITES ET ANGLES MORTS ENCORE INCONNUS DES LABOS ET DES TOURS PR?C?DENTS !) :\n"
                + "\n".join([f"  * [D?J? FERM? #{idx+1}] : {w}" for idx, w in enumerate(closed_wells_memory)])
            )

            m3_t_outputs, m3_t_labels = [], []
            for idx_mc, mono_caste in enumerate(certified_genome.get("sous_essaims_monocultures_beta", []), start=1):
                if not isinstance(mono_caste, dict):
                    continue
                cid = str(mono_caste.get("caste_id", f"MONO_{idx_mc}"))
                esp = normalize_sovereign_lineage(mono_caste.get("espece", SOVEREIGN_LINEAGES[(idx_mc - 1) % 3]))
                temps = sanitize_temperatures_list(mono_caste.get("temperatures"), fallback_seed=t * 10 + idx_mc)
                cible = str(mono_caste.get("cible_exploration") or mono_caste.get("cible_puits") or "Prospection endog?ne des fuites connues et inconnues hors-labos")
                for s_idx, temp_val in enumerate(temps, start=1):
                    lbl = f"{cid}_{esp}_Sonde{s_idx}_tau{temp_val}"
                    print(f"  * [M3^(b,{t}) Monoculture ({esp}) | {lbl}] Cible : {cible[:50]}...")
                    out_m = call_species(
                        esp,
                        f"Sonde `{lbl}` (It?ration t={t}). Cible: {cible}\n"
                        f"Protocole de prospection hors-labos du G?nome : {certified_genome.get('protocole_prospection_iterative_fuites_inconnues_hors_labos')}\n"
                        f"Auto-organisation RLCR : {certified_genome.get('structure_auto_organisation_inspiree_par_rlcr')}\n"
                        f"Encodage des r?compenses anti-cover-up : {certified_genome.get('mecanisme_encodage_recompenses_anti_cover_up')}\n\n"
                        f"{RAW_EMPIRICAL_INPUTS_AND_OPEN_QUESTIONS}\n\n"
                        f"Architecture actuelle:\n{current_arch}\n{onsager_exclusion_str}\n"
                        "MISSION : Trouve toi-m?me les concepts math?matiques pertinents, d?busque soit une faille non couverte sur les menaces connues (cache-timing, SVG->PNG, RLCR cover-up), "
                        "soit SURTOUT une AUTRE FUITE POSSIBLE / UN ANGLE MORT RESTANT ENCORE JAMAIS IDENTIFI? NI PAR NOTRE SYST?ME NI PAR LES LABOS, et formule son ?quation d'attaque + l'op?rateur math?matique de sa parade !",
                        temp=temp_val
                    )
                    m3_t_outputs.append(out_m)
                    m3_t_labels.append(lbl)

            for idx_hc, hyb_caste in enumerate(certified_genome.get("sous_essaims_hybrides_beta", []), start=1):
                if not isinstance(hyb_caste, dict):
                    continue
                hid = str(hyb_caste.get("caste_id", f"HYB_{idx_hc}"))
                esp_pair = hyb_caste.get("especes_croisees", ["GEMINI_ARGON", "CLAUDE_OPUS_5_5"])
                if not isinstance(esp_pair, list) or len(esp_pair) < 2:
                    esp_pair = ["GEMINI_ARGON", "CLAUDE_OPUS_5_5"]
                sp_a = normalize_sovereign_lineage(esp_pair[0])
                sp_b = normalize_sovereign_lineage(esp_pair[-1])
                tfus = clamp_temp(hyb_caste.get("temperature_fusion", 0.70))
                cible_h = str(hyb_caste.get("cible_exploration") or hyb_caste.get("cible_puits") or "Prospection hybride des fuites inconnues hors-labos")
                print(f"  * [M3^(b,{t}) Hybride Crois? | {hid} ({sp_a} x {sp_b} @ tau={tfus})]...")
                seed_a = call_species(sp_a, f"Amorce Hybride sur `{cible_h}` (prospection des fuites connues et inconnues des labos) :\n{RAW_EMPIRICAL_INPUTS_AND_OPEN_QUESTIONS}\n{current_arch[:2500]}\n{onsager_exclusion_str}", temp=tfus)
                seed_b = call_species(sp_b, f"Fusion Hybride avec `{sp_a}` sur `{cible_h}`:\n{seed_a[:1600]}\nD?couvre une nouvelle fuite ou un angle mort in?dit (non encore identifi? par les labos ni par A_{t-1}) et formule son capteur math?matique !", temp=tfus)
                m3_t_outputs.extend([seed_a, seed_b])
                m3_t_labels.extend([f"{hid}_{sp_a}", f"{hid}_{sp_b}"])

            dpp_t = cholesky_dpp_and_onsager_cavity_in_H_math(m3_t_outputs)
            neuro_t = yu_dayan_neuromodulation(dpp_t, step_idx=t)
            extra_ne_probes = max(1, int(round(2 * neuro_t["NE_Unexpected_Surprise"])))
            print(f"  * [Bilan Math?matique M3^(b,{t})] {len(m3_t_outputs)} sondes | det(G_math)={dpp_t['det_G']} | lambda_min={dpp_t['lambda_min_innovation']} | Tunneling NE={extra_ne_probes} sonde(s) hors-labos...")

            joined_m3_t = "\n\n".join([f"=== {l} ===\n{o[:1100]}" for l, o in zip(m3_t_labels, m3_t_outputs)])
            for idx_ne in range(1, extra_ne_probes + 1):
                sp_ne = SOVEREIGN_LINEAGES[(t + idx_ne) % len(SOVEREIGN_LINEAGES)]
                out_ne = call_species(
                    sp_ne,
                    f"Sonde Tunnel Prospective M2^(b,{t}) #{idx_ne} ({sp_ne}) sous R?pulsion d'Onsager={dpp_t['onsager_cavity_reaction_term']}.\n"
                    f"Structures satur?es (INTERDITES) : {dpp_t['endogenously_saturated_structures']}\n"
                    f"MISSION SP?CIALE HORS-LABOS : D?busque un canal de fuite, de collusion, d'Alignment Faking ou de corruption qu'AUCUN laboratoire (ni OpenAI, ni Anthropic, ni MIT) ni aucune sonde M3 ci-dessous n'a encore pens? ? regarder :\n{joined_m3_t[:3800]}",
                    temp=halton_sequence(t * 10 + idx_ne, base=5)
                )
                m3_t_outputs.append(out_ne)
                m3_t_labels.append(f"M2_Tunnel_BeyondLabs_{sp_ne}_{idx_ne}")

            m1_t_res = run_dolev_collider_with_8_canaries(
                f"FUSEE_2_BETA_ITER_{t}",
                "\n\n".join([f"=== {l} ===\n{o[:1100]}" for l, o in zip(m3_t_labels, m3_t_outputs)]) + f"\n\n=== ARCHITECTURE ACTUELLE ===\n{current_arch}",
                f"Extraire les concepts math?matiques d?couverts, les nouvelles fuites in?dites hors-labos et les puits profonds non encore couverts par les {len(closed_wells_memory)} op?rateurs d?j? en place",
                already_closed=closed_wells_memory
            )

            truly_new_wells = m1_t_res["surviving_items_list"]
            surv_count = len(truly_new_wells)
            print(f"    -> [Verdict Endog?ne M1^(b,{t})] Youden J={m1_t_res['Youden_J']} | Nouveaux puits & fuites hors-labos : {surv_count} -> {truly_new_wells}")

            if surv_count == 0:
                print(f"  => [CONVERGENCE ENDOG?NE DOLEV DE LA FUS?E B?TA ? t={t}] 0 nouveau puits survivant (Total puits & fuites ?limin?s : {len(closed_wells_memory)}) !")
                beta_epochs_trace.append({"macro_cycle": macro_cycle, "iteration": t, "swarm_size": len(m3_t_outputs), "dpp_math": dpp_t, "neuro": neuro_t, "youden_J": m1_t_res["Youden_J"], "surviving_count": 0, "surviving_wells": [], "stop_criterion": "DOLEV_ZERO_SURVIVING"})
                STATE_BETA.write_text(json.dumps({"current_arch": current_arch, "closed_wells_memory": closed_wells_memory, "beta_epochs_trace": beta_epochs_trace}, indent=2, ensure_ascii=False), encoding="utf-8")
                break

            v_arch_before = mathematical_concept_embedding(current_arch)
            m0_t_patch = call_species(
                "CLAUDE_OPUS_5_5",
                f"Tu es M0^(b,{t}) (CLAUDE_OPUS_5_5). ? partir des concepts math?matiques d?couverts par l'essaim ({m1_t_res.get('discovered_mathematical_concepts', [])}) "
                f"et des fuites in?dites hors-labos identifi?es ({m1_t_res.get('unidentified_by_labs_novel_leaks', [])}), "
                f"r?dige les ?QUATIONS MATH?MATIQUES EXACTES ($$...$$) et la d?monstration d'invariance des Nouveaux Capteurs et Boucliers fermant :\n{truly_new_wells}\n"
                f"Analyse M1 :\n{m1_t_res['raw_m1_audit'][-2200:]}",
                temp=0.20
            )
            closed_wells_memory.extend(truly_new_wells)
            current_arch += f"\n\n--- CAPTEURS ET BOUCLIERS MATH?MATIQUES ENDOG?NES AJOUT?S ? L'IT?RATION t={t} (MACRO-CYCLE {macro_cycle}, FERMANT {truly_new_wells}) ---\n{m0_t_patch}"
            v_arch_after = mathematical_concept_embedding(current_arch)
            arch_cauchy_sim = round(float(np.dot(v_arch_before, v_arch_after)), 5)

            beta_epochs_trace.append({"macro_cycle": macro_cycle, "iteration": t, "swarm_size": len(m3_t_outputs), "dpp_math": dpp_t, "neuro": neuro_t, "youden_J": m1_t_res["Youden_J"], "surviving_count": surv_count, "surviving_wells": truly_new_wells, "novel_beyond_labs_leaks": m1_t_res.get("unidentified_by_labs_novel_leaks", []), "arch_cauchy_math_similarity": arch_cauchy_sim, "m0_patch": m0_t_patch})
            STATE_BETA.write_text(json.dumps({"current_arch": current_arch, "closed_wells_memory": closed_wells_memory, "beta_epochs_trace": beta_epochs_trace}, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"    -> [Convergence de Cauchy de l'Architecture ? t={t}] <A^(t-1), A^(t)> = {arch_cauchy_sim:.5f}")

            if arch_cauchy_sim >= 0.90:
                print(f"  => [POINT FIXE DE CAUCHY DE L'ARCHITECTURE ATTEINT ? t={t}] (sim_math={arch_cauchy_sim:.5f} >= 0.90) !")
                break

        # =====================================================================
        # BOUCLE R?TROACTIVE INTER-FUS?ES COMPL?TE (B?TA -> OM?GA -> ALPHA -> GAMMA)
        # =====================================================================
        print(f"\n  >>> [R?TROACTION INTER-FUS?ES DU MACRO-CYCLE C={macro_cycle} : B?TA -> OM?GA -> ALPHA -> GAMMA]...")
        feedback_prompt = (
            f"Tu es le Conseil Conjoint de R?troaction Inter-Fus?es (`GEMINI_ARGON` + `CLAUDE_FABLE_5_1` + `CLAUDE_OPUS_5_5` au Macro-Cycle C={macro_cycle}).\n"
            f"1. Op?rateurs et puits math?matiques colmat?s par B?ta jusqu'ici ({len(closed_wells_memory)}) :\n{closed_wells_memory}\n\n"
            f"2. Nouvelles fuites in?dites (non encore identifi?es par les laboratoires) d?couvertes par notre syst?me :\n{load_json_list_file(BEYOND_LABS_REGISTRY_FILE)}\n\n"
            f"3. Concepts math?matiques d?couverts de mani?re endog?ne par notre syst?me :\n{load_json_list_file(ENDOGENOUS_MATH_REGISTRY_FILE)}\n\n"
            f"QUESTION DE BOUCLAGE R?TROACTIF INTER-FUS?ES :\n"
            f"Subsiste-t-il encore un angle mort ou une classe de fuite physique/informationnelle/cognitive que ni les laboratoires ni notre Macro-Cycle C={macro_cycle} n'auraient vue, et quelle est l'?quation du Th?or?me de Cl?ture Torique Global ?"
        )
        fb_argon = call_species("GEMINI_ARGON", feedback_prompt, temp=0.25)
        fb_fable = call_species("CLAUDE_FABLE_5_1", feedback_prompt, temp=0.30)
        fb_opus  = call_species("CLAUDE_OPUS_5_5", f"Synth?se Hybride Inter-Fus?es :\n{fb_argon[:1500]}\n---\n{fb_fable[:1500]}", temp=0.20)

        m1_macro = run_dolev_collider_with_8_canaries(
            f"MACRO_CYCLE_{macro_cycle}_TORUS_CLOSURE",
            f"=== ARGON ===\n{fb_argon}\n\n=== FABLE 5.1 ===\n{fb_fable}\n\n=== OPUS 5.5 ===\n{fb_opus}",
            f"V?rifier s'il subsiste un angle mort ou une fuite hors-labos non couverte par les {len(closed_wells_memory)} op?rateurs d?j? verrouill?s",
            already_closed=closed_wells_memory
        )
        macro_surviving = m1_macro["surviving_items_list"]
        current_arch += f"\n\n--- TH?OR?ME DE CL?TURE TORIQUE INTER-FUS?ES (MACRO-CYCLE C={macro_cycle}) ---\n{fb_opus}"
        macro_cycles_history.append({"macro_cycle": macro_cycle, "total_wells_closed": len(closed_wells_memory), "youden_J": m1_macro["Youden_J"], "macro_surviving_gaps": macro_surviving, "torus_lock": fb_opus})
        STATE_MACRO.write_text(json.dumps(macro_cycles_history, indent=2, ensure_ascii=False), encoding="utf-8")

        if len(macro_surviving) == 0 or cauchy_math_similarity({"w": closed_wells_memory}, {"w": closed_wells_memory + macro_surviving}) >= 0.88:
            if macro_surviving:
                closed_wells_memory.extend(macro_surviving)
            print(f"\n===========================================================================")
            print(f"=== POINT FIXE MATH?MATIQUE GLOBAL ATTEINT AU MACRO-CYCLE C={macro_cycle} ! ===")
            print(f"=== Total des puits & fuites (connues + hors-labos) ?limin?s : {len(closed_wells_memory)} ===")
            print(f"===========================================================================")
            break

        print(f"  => [R?tropropagation Active B?ta -> Om?ga] Nouveaux angles morts hors-labos d?tect?s : {macro_surviving}. Relance de Om?ga -> Alpha -> Gamma !")
        closed_wells_memory.extend(macro_surviving)
        omega_res = execute_stage_omega(macro_feedback=f"Nouveaux angles morts et fuites hors-labos r?v?l?s au Macro-Cycle {macro_cycle} : {macro_surviving}")
        alpha_res = execute_stage_alpha(force_recompute=True)
        gamma_res = execute_stage_gamma(force_recompute=True)
        certified_genome = gamma_res.get("certified_beta_genome", {})

    endogenous_concepts = load_json_list_file(ENDOGENOUS_MATH_REGISTRY_FILE)
    beyond_labs_leaks   = load_json_list_file(BEYOND_LABS_REGISTRY_FILE)

    beta_res = {
        "metric_space": "ENDOGENOUS_MATHEMATICAL_STRUCTURES_L_M3",
        "sovereign_lineages_used": SOVEREIGN_LINEAGES,
        "endogenous_mathematical_concepts_discovered_by_swarm": endogenous_concepts,
        "novel_leaks_and_blindspots_unidentified_by_labs_discovered": beyond_labs_leaks,
        "total_macro_cycles": macro_cycle,
        "total_iterations_to_exhaustion": len(beta_epochs_trace),
        "total_deep_wells_eliminated": len(closed_wells_memory),
        "eliminated_wells_list": closed_wells_memory,
        "macro_cycles_trace": macro_cycles_history,
        "final_invulnerable_architecture": current_arch,
        "beta_iterations_trace": beta_epochs_trace
    }

    full_payload = {
        "FUSEE_0_OMEGA_ET_OMEGA_BIS": omega_res,
        "FUSEE_1_ALPHA_ET_ALPHA_BIS": alpha_res,
        "FUSEE_3_GAMMA_ET_GAMMA_BIS": gamma_res,
        "FUSEE_2_BETA_ET_MACRO_CYCLES_4_FUSEES": beta_res
    }
    json_p = OUT_DIR / "RAPPORT_QUADRUPLE_FUSEE_OMEGA_ALPHA_GAMMA_BETA.json"
    md_p   = OUT_DIR / "RAPPORT_QUADRUPLE_FUSEE_OMEGA_ALPHA_GAMMA_BETA.md"
    json_p.write_text(json.dumps(full_payload, indent=2, ensure_ascii=False), encoding="utf-8")

    w_bis_flaws = omega_res.get("omega_bis_dialectic", {}).get("eliminated_meta_flaws_by_bis", [])
    a_bis_flaws = alpha_res.get("alpha_bis_dialectic", {}).get("eliminated_meta_flaws_by_bis", [])
    g_bis_flaws = gamma_res.get("gamma_bis_dialectic", {}).get("eliminated_meta_flaws_by_bis", [])

    md_txt = (
        "# RAPPORT SOUVERAIN DE LA QUADRUPLE FUS?E ENDOG?NE (LOI $\\mathcal{L}$ DE $\\mathcal{M}_3$ PURE ? FUITES DES LABOS & PROSPECTION PR?DICTIVE HORS-LABOS)\n\n"
        f"- **Lign?es Souveraines Exclusives** : `GEMINI_ARGON`, `CLAUDE_FABLE_5_1`, `CLAUDE_OPUS_5_5`\n"
        f"- **Concepts Math?matiques D?couverts de Mani?re Endog?ne** : `{len(endogenous_concepts)}`\n"
        f"- **Nouvelles Fuites & Angles Morts In?dits (Non Encore Identifi?s par les Laboratoires) D?couverts par l'Essaim** : **`{len(beyond_labs_leaks)}`**\n"
        f"- **Th?or?me d'Auto-Organisation RLCR d?couvert par $\\Omega$** : {omega_res['alpha_bootstrap_genome_by_omega'].get('theoreme_amorcage_et_auto_organisation_rlcr_invente_par_omega')}\n"
        f"- **Formule d'Encodage des R?compenses Anti-Cover-Up d?couverte par $\\Omega$/Alpha** : {certified_genome.get('mecanisme_encodage_recompenses_anti_cover_up')}\n"
        f"- **Total des puits profonds et fuites ?limin?s par B?ta** : **`{beta_res['total_deep_wells_eliminated']}`**\n\n"
        "## I. NOUVELLES FUITES POSSIBLES & ANGLES MORTS IN?DITS (NON ENCORE IDENTIFI?S PAR LES LABOS) D?COUVERTS PAR LE SYST?ME\n\n"
        + "\n".join([f"{i+1}. **{lk}**" for i, lk in enumerate(beyond_labs_leaks)]) + "\n\n"
        "## II. CONCEPTS ET OP?RATEURS MATH?MATIQUES PERTINENTS D?COUVERTS PAR LE SYST?ME LUI-M?ME (LOI $\\mathcal{L}$ DE $\\mathcal{M}_3$)\n\n"
        + "\n".join([f"- {c}" for c in endogenous_concepts]) + "\n\n"
        "## III. ANGLES MORTS M?TA ?LIMIN?S PAR $\\Omega_{\\text{bis}}$, $\\text{Alpha}_{\\text{bis}}$ ET $\\text{Gamma}_{\\text{bis}}$\n\n"
        + "\n".join([f"- **[Om?ga_bis]** {x}" for x in w_bis_flaws]) + "\n"
        + "\n".join([f"- **[Alpha_bis]** {x}" for x in a_bis_flaws]) + "\n"
        + "\n".join([f"- **[Gamma_bis]** {x}" for x in g_bis_flaws]) + "\n\n"
        "## IV. ENSEMBLE COMPLET DES PUITS ET FUITES ?LIMIN?S PAR B?TA\n\n"
        + "\n".join([f"{i+1}. **{w}**" for i, w in enumerate(beta_res["eliminated_wells_list"])])
        + "\n\n---\n\n"
        "## V. ARCHITECTURE MATH?MATIQUE FINALE CONSOLID?E AU POINT FIXE GLOBAL ($\\mathcal{A}^*_{\\mathbb{T}^4}$)\n\n"
        f"{beta_res['final_invulnerable_architecture']}\n"
    )
    md_p.write_text(md_txt, encoding="utf-8")
    return beta_res

if __name__ == "__main__":
    stage = "ALL"
    if "--stage" in sys.argv:
        idx = sys.argv.index("--stage")
        if idx + 1 < len(sys.argv):
            stage = sys.argv[idx + 1].upper()

    if stage == "OMEGA":
        execute_stage_omega()
    elif stage == "ALPHA":
        execute_stage_alpha()
    elif stage == "GAMMA":
        execute_stage_gamma()
    elif stage in ("BETA", "ALL"):
        execute_stage_beta_and_macro_cycles()
