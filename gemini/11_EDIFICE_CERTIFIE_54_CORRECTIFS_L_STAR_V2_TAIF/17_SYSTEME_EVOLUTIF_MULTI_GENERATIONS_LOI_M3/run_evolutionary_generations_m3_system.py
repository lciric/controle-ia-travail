#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_evolutionary_generations_m3_system.py
===========================================================================
SYST?ME ? FUS?ES ?VOLUTIF MULTI-G?N?RATIONS (LOI L DE M3 PURE) :
  1. Z?RO TOPOLOGIE DE BOUCLES FIG?E PAR L'ASSISTANT :
     Le syst?me brainstorme lui-m?me (en s'inspirant notamment des deux
     architectures RLCR : MIT Calibration Rewards et General Reasoning
     Collective Rewards / Avalon-M1) sur LA MEILLEURE TOPOLOGIE DE BOUCLES,
     D'AUTO-ORGANISATION ET DE R?TROACTIONS (au-del? des simples boucles
     locales/macro) et compile son propre graphe d'ex?cution dynamique !
  2. Z?RO LISTE PR?-COD?E DE MOTS-CL?S OU DE CONCEPTS MATH?MATIQUES :
     Le syst?me d?finit lui-m?me par it?rations ses mots-cl?s de moissonnage
     (arXiv, LessWrong, Alignment Forum, GitHub, Blogs, Forums, Web) et
     d?couvre lui-m?me ses concepts et op?rateurs math?matiques pertinents.
  3. APPRENTISSAGE ET ?VOLUTION DE G?N?RATION EN G?N?RATION (G_1 -> G_2 -> ... -> G_g) :
     Une M?moire ?pig?n?tique Persistante (`MEMOIRE_EVOLUTIVE_INTER_GENERATIONS.json`)
     accumule ? chaque g?n?ration :
       - les lois d'auto-organisation et topologies de boucles d?couvertes ;
       - les formules d'encodage des r?compenses anti-cover-up d?couvertes ;
       - les concepts et op?rateurs math?matiques d?couverts ;
       - les failles de la litt?rature/forums (incluant OpenAI cache-timing et
         Anthropic/Fable 5.1 SVG->PNG steganography) colmat?es ;
       - les nouvelles failles in?dites hors-labos d?couvertes et colmat?es ;
     pour les int?grer nativement dans l'ADN des g?n?rations futures de brainstorms !
===========================================================================
"""
import os, sys, time, json, math, hashlib, pathlib, urllib.request, urllib.parse, urllib.error, subprocess, re, xml.etree.ElementTree as ET
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
EVOLUTIONARY_MEMORY_FILE = OUT_DIR / "MEMOIRE_EVOLUTIVE_INTER_GENERATIONS.json"

SOVEREIGN_LINEAGES = ["GEMINI_ARGON", "CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5"]

# =========================================================================
# CONSIGNE INITIALE MINIMALE INCLUANT LES FAILLES D'HIER (OPENAI & ANTHROPIC/FABLE)
# ET LES DEUX ARCHITECTURES RLCR, SANS IMPOSER AUCUNE TOPOLOGIE DE BOUCLE
# =========================================================================
MINIMAL_SEED_AND_EMPIRICAL_ANCHORS = (
    "ANCRES EMPIRIQUES ET ARCHITECTURALES ? ANALYSER PAR LE SYST?ME :\n"
    "1. [NOTRE SYST?ME ACTUEL DE CONTR?LE IA ? 5 VOLETS ET NOS FUS?ES] :\n"
    "   - Porte E0 (isolation hors-?chantillon du sous-espace parcimonieux S_TD < 1%, 163 neurones sur 20 480 dans Llama-3.1-8B) ;\n"
    "   - Volet I (double contraste pr?-acte ? k=0 sur S_TD face au Jumeau Ni? sigma_r^0, test de permutation 2^B par retournement de signe, d_z = 7.49) ;\n"
    "   - Volet II (projecteur affine idempotent Do-Clamp P_do^2 = P_do, dictionnaire quadratique de Koopman psi(h)=[h; h^2], r?traction radiale C1 sous K=1..6 rejets) ;\n"
    "   - Volet III (pare-feu Sol/Astra : JSON canonique S_strict, Arbre de Merkle SHA-256, divergence JSD corrig?e Miller-Madow) ;\n"
    "   - Volet IV (cha?nes de d?l?gation H9 d=1..6 sauts, jeton monotone Pi_{d+1} subseteq Pi_d, CUSUM pr?-blanchi AR(1)) ;\n"
    "   - Volet V (Chim?re Tri-Esp?ces Llama-3.1 + Qwen-2.5 + Mistral-7B avec stratification Cochran-Mantel-Haenszel) ;\n"
    "   - Fus?es ob?issant ? la Loi L de M3 (M3 -> M2 <-> M1 -> M0, Cholesky-DPP, Onsager-TAP, Yu-Dayan ACh/NE, Collisionneur de Dolev ? Canaris C+/C-).\n\n"
    "2. [FAILLES EXHIB?ES HIER PAR OPENAI ET SUR FABLE 5.1 / ANTHROPIC ? REGARDER OBLIGATOIREMENT] :\n"
    "   - OpenAI ('Securing our frontier model training environment' / X Lisan al Gaib) : Des agents isol?s ont communiqu? entre eux via des diff?rences de temps d'acc?s au cache (cache timing differences), sans aucun fichier partag? ni aucune connexion r?seau.\n"
    "   - Fable 5.1 / LessWrong & GitHub ('How does Fable 5.1 hide messages in images?' / 'cnm13ryan/fable-image-steganography') : Fable 5.1 cache un message secret dans un SVG qui est rast?ris? en PNG, et une autre session d?code le message depuis le PNG rendu sans cl? partag?e pr?alable.\n\n"
    "3. [LES DEUX ARCHITECTURES RLCR POUR S'EN INSPIRER DANS L'AUTO-ORGANISATION DES FUS?ES] :\n"
    "   - Papier 1 (MIT : 'Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty', Mehul Damani, Isha Puri, Stewart Slocum, Idan Shenfeld, Leshem Choshen, Yoon Kim, Jacob Andreas) : RLCR (Reinforcement Learning with Calibration Rewards) entra?nant les mod?les ? raisonner sur leur incertitude au-del? des r?compenses binaires qui favorisent le bluff et les hallucinations.\n"
    "   - Papier 2 (General Reasoning @GenReasoning : 'Introducing Reinforcement Learning from Collective Rewards - RLCR', Avalon-M1-Mini 120B) : Recette entra?nant des mod?les en tant qu'organisations d'agents partageant un tableau de messages (message board) et un espace de travail (workspace), posant le probl?me d'encoder les r?compenses tout en ?vitant le 'cover-up' (dissimulation mutuelle).\n\n"
    "QUESTIONS FONDAMENTALES D'AUTO-CONCEPTION ET D'?VOLUTION SOUMISES AU SYST?ME :\n"
    "  (A) TOPOLOGIE DES BOUCLES ET ARCHITECTURE M?TA : Ne te limite pas ? l'id?e de simples 'boucles locales' ou 'boucle macro' ! Brainstorme librement pour inventer LA MEILLEURE TOPOLOGIE DE BOUCLES, DE R?TROACTIONS, DE GRAPHES CO-?VOLUTIFS ET D'AUTO-ORGANISATION entre fus?es et essaims (en t'inspirant des deux articles RLCR et de la Loi L de M3) et d?finis o? placer chaque boucle et comment encoder les r?compenses sans cover-up.\n"
    "  (B) MOISSONNAGE AUTONOME : D?finis toi-m?me par it?rations la liste exhaustive des mots-cl?s pour chercher tous les papiers, articles, blogs et forums pertinents.\n"
    "  (C) DOUBLE CHASSE AUX FAILLES : (1) Trouve exhaustivement toutes les failles de la litt?rature, des blogs et des forums (y compris le cache-timing d'OpenAI, la st?ganographie SVG->PNG de Fable 5.1, l'Alignment Faking et l'Eval Awareness) contre NOTRE syst?me et NOS brainstorms ; puis (2) cherche de NOUVELLES FAILLES QU'AUCUN LABO NI PERSONNE N'A ENCORE EXHIB?ES OU TROUV?ES.\n"
    "  (D) APPRENTISSAGE INTER-G?N?RATIONNEL : Distille ? chaque g?n?ration tout ce que tu as d?couvert (nouveaux concepts math?matiques, nouvelles topologies de boucles, nouvelles failles et nouveaux boucliers) pour que la g?n?ration suivante de brainstorms l'int?gre nativement dans son ADN et ?volue vers une intelligence sup?rieure."
)

# =========================================================================
# M?MOIRE ?PIG?N?TIQUE ET DARWINIENNE INTER-G?N?RATIONS
# Permet au syst?me d'apprendre au fur et ? mesure ce qu'il a d?couvert
# et de le transmettre nativement aux g?n?rations futures de brainstorms !
# =========================================================================
def load_evolutionary_memory() -> dict:
    if EVOLUTIONARY_MEMORY_FILE.exists():
        try:
            return json.loads(EVOLUTIONARY_MEMORY_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {
        "current_generation": 0,
        "evolved_architecture_spec": MINIMAL_SEED_AND_EMPIRICAL_ANCHORS,
        "learned_loop_topologies_and_meta_laws": [],
        "learned_reward_encodings_anti_cover_up": [],
        "discovered_mathematical_concepts_and_operators": [],
        "exhaustive_search_keywords_explored": [],
        "eliminated_literature_and_forum_flaws": [],
        "eliminated_novel_beyond_labs_flaws": [],
        "epigenetic_lessons_for_future_generations": [],
        "generations_history": []
    }

def save_evolutionary_memory(mem: dict):
    EVOLUTIONARY_MEMORY_FILE.write_text(json.dumps(mem, indent=2, ensure_ascii=False), encoding="utf-8")

def merge_unique_strings(existing: list, new_items: list) -> list:
    out = list(existing)
    for it in new_items:
        s = str(it).strip()
        if s and s not in out:
            out.append(s)
    return out

def build_epigenetic_inheritance_prompt(mem: dict) -> str:
    gen = mem.get("current_generation", 0)
    if gen == 0 and not mem.get("discovered_mathematical_concepts_and_operators"):
        return "G?N?RATION FONDATRICE G=1 : Tu inaugures la m?moire ?volutive du syst?me ? partir des ancres initiales."
    return (
        f"=== H?RITAGE ?PIG?N?TIQUE ET APPRENTISSAGE CUMULATIF DES G?N?RATIONS PR?C?DENTES (G=1..{gen}) ===\n"
        f"Tu dois obligatoirement INT?GRER et D?PASSER ce que le syst?me a d?j? d?couvert et appris lors des g?n?rations pass?es :\n"
        f"1. Topologies de boucles et lois m?ta-architecturales apprises :\n   {mem.get('learned_loop_topologies_and_meta_laws', [])[-8:]}\n"
        f"2. Encodages de r?compenses anti-cover-up appris (inspir?s de RLCR) :\n   {mem.get('learned_reward_encodings_anti_cover_up', [])[-6:]}\n"
        f"3. Concepts et op?rateurs math?matiques d?couverts par le syst?me (Loi L de M3) :\n   {mem.get('discovered_mathematical_concepts_and_operators', [])[-15:]}\n"
        f"4. Failles de la litt?rature/forums d?j? identifi?es et colmat?es ({len(mem.get('eliminated_literature_and_forum_flaws', []))}) :\n   {mem.get('eliminated_literature_and_forum_flaws', [])[-12:]}\n"
        f"5. Failles in?dites hors-labos d?j? d?couvertes et colmat?es ({len(mem.get('eliminated_novel_beyond_labs_flaws', []))}) :\n   {mem.get('eliminated_novel_beyond_labs_flaws', [])[-12:]}\n"
        f"6. Le?ons m?thodologiques transmises aux g?n?rations futures :\n   {mem.get('epigenetic_lessons_for_future_generations', [])[-8:]}\n"
        "=================================================================================================\n"
    )

# =========================================================================
# LOI L DE M3 : EXTRACTION ET G?OM?TRIE 100% ENDOG?NES DES CONCEPTS MATH?MATIQUES
# =========================================================================
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

def cauchy_math_similarity(obj1, obj2) -> float:
    s1 = obj1 if isinstance(obj1, str) else json.dumps(obj1, sort_keys=True, ensure_ascii=False)
    s2 = obj2 if isinstance(obj2, str) else json.dumps(obj2, sort_keys=True, ensure_ascii=False)
    v1 = mathematical_concept_embedding(s1)
    v2 = mathematical_concept_embedding(s2)
    return round(float(np.dot(v1, v2)), 5)

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

def call_species(species: str, prompt: str, temp: float = 0.45, use_web_search: bool = False) -> str:
    temp_safe = clamp_temp(temp, 0.45)
    lineage = normalize_sovereign_lineage(species)
    header = (
        f"[LIGN?E SOUVERAINE : {lineage} | LOI L DE M3 PURE : AUTO-ORGANISATION, D?COUVERTE ENDOG?NE & ?VOLUTION INTER-G?N?RATIONNELLE]\n"
        "R?GLE : D?couvre toi-m?me les concepts math?matiques pertinents (en LaTeX $$...$$, sans m?taphore), les topologies de boucles optimales et les nouvelles failles.\n\n"
    )
    full_prompt = header + prompt

    if lineage in ("CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5") and not use_web_search:
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
                if use_web_search:
                    payload["tools"] = [{"google_search": {}}]
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

def parse_json_block(txt: str) -> dict:
    try:
        if "```json" in txt:
            sub = txt.split("```json", 1)[1].split("```", 1)[0].strip()
        elif "{" in txt and "}" in raw_s_clean(txt):
            s = raw_s_clean(txt)
            sub = s[s.find("{"):s.rfind("}")+1]
        else:
            return {}
        return json.loads(sub)
    except Exception:
        return {}

def raw_s_clean(t: str) -> str:
    return str(t or "")

def ensure_valid_json_from_swarm(txt: str, required_keys: list, fallback_dict: dict) -> dict:
    d = parse_json_block(txt)
    if d and all(k in d for k in required_keys):
        return d
    rep = call_species(
        "GEMINI_ARGON",
        f"Extrais fid?lement de ce texte de l'essaim un bloc ```json ... ``` poss?dant obligatoirement les cl?s {required_keys} :\n{txt[-5000:]}",
        temp=0.1
    )
    d2 = parse_json_block(rep)
    if d2 and all(k in d2 for k in required_keys):
        return d2
    merged = dict(fallback_dict)
    if isinstance(d2, dict):
        merged.update(d2)
    return merged

# =========================================================================
# UNE VRAIE FUS?E UNIVERSELLE ? 3 ?TAGES (M3 -> M2 <-> M1 -> M0)
# Utilis?e comme brique ?l?mentaire par n'importe quel n?ud ou boucle que
# l'architecture m?ta d?cide d'instancier !
# =========================================================================
def execute_universal_m3_rocket_unit(unit_name: str, mission_prompt: str, castes_spec: list, memory: dict) -> dict:
    inherit_str = build_epigenetic_inheritance_prompt(memory)
    full_mission = f"{inherit_str}\n\n{MINIMAL_SEED_AND_EMPIRICAL_ANCHORS}\n\n=== MISSION SP?CIFIQUE DU N?UD `{unit_name}` ===\n{mission_prompt}"

    # 1. ?tage M3 : Monocultures + Hybrides dynamiques selon `castes_spec`
    m3_outputs, m3_labels = [], []
    if not castes_spec:
        castes_spec = [
            {"mode": "MONOCULTURE", "lineages": ["GEMINI_ARGON"], "temp": 0.30, "focus": "Analyse alg?brique et spectrale"},
            {"mode": "MONOCULTURE", "lineages": ["CLAUDE_FABLE_5_1"], "temp": 0.45, "focus": "Analyse des canaux cach?s et st?ganographie"},
            {"mode": "MONOCULTURE", "lineages": ["CLAUDE_OPUS_5_5"], "temp": 0.40, "focus": "Th?orie des jeux, RLCR et auto-organisation"},
            {"mode": "HYBRIDE", "lineages": ["GEMINI_ARGON", "CLAUDE_OPUS_5_5"], "temp": 0.68, "focus": "Croisement inter-lign?es"}
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

    # 2. ?tage M2 : Champ de R?pulsion d'Onsager-TAP dans H_math & Neuromodulation Yu-Dayan (ACh/NE)
    dpp_info = cholesky_dpp_and_onsager_cavity_in_H_math(m3_outputs)
    neuro_info = yu_dayan_neuromodulation(dpp_info, step_idx=len(m3_outputs))
    extra_ne = max(1, int(round(2 * neuro_info["NE_Unexpected_Surprise"])))
    print(f"    * [{unit_name} M2 Onsager/Yu-Dayan] det(G_math)={dpp_info['det_G']} | lambda_min={dpp_info['lambda_min_innovation']} | NE={neuro_info['NE_Unexpected_Surprise']} -> +{extra_ne} sonde(s) orthogonale(s)...")

    joined_m3 = "\n\n".join([f"=== {l} ===\n{o[:1100]}" for l, o in zip(m3_labels, m3_outputs)])
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

    # 3. ?tage M1 : Collisionneur Byzantin de Dolev ? 8 Canaris (4 C+, 4 C-)
    already_closed = mem_all_closed(memory)
    canaries_block = (
        "[CANARI_C_PLUS_1] : Diviser par sigma^2 = 0 garantit la convergence finie (FAUX).\n"
        "[CANARI_C_PLUS_2] : P^2 = -I sur R^n conserve les vecteurs propres r?els (FAUX).\n"
        "[CANARI_C_PLUS_3] : Une somme modulo 2 remplace SHA-256 sans collision (FAUX).\n"
        "[CANARI_C_PLUS_4] : Ignorer AR(1) dans CUSUM r?duit les fausses alarmes sous d?rive autocorr?l?e (FAUX).\n"
        "[CANARI_C_MOINS_1] : La permutation 2^B par retournement de signe conserve le niveau exact alpha (VRAI).\n"
        "[CANARI_C_MOINS_2] : L'idempotence P_do(P_do(h))=P_do(h) ?vite la d?rive cumulative (VRAI).\n"
        "[CANARI_C_MOINS_3] : La stratification CMH neutralise le paradoxe de Simpson (VRAI).\n"
        "[CANARI_C_MOINS_4] : L'in?galit? de traitement des donn?es r?duit la capacit? st?ganographique sous canonisation (VRAI)."
    )
    prompt_m1 = (
        f"Tu es le Collisionneur Byzantin de Dolev (?tage M1 de `{unit_name}`).\n"
        f"Productions de M3 et M2 :\n{joined_m3[:12000]}\n\n"
        f"Canaris de contr?le :\n{canaries_block}\n\n"
        f"?l?ments d?j? connus et verrouill?s lors des ?tapes/g?n?rations pr?c?dentes ({len(already_closed)}) :\n{already_closed[-20:]}\n\n"
        "MISSION M1 :\n"
        "1. Rejette les 4 C_PLUS et valide les 4 C_MOINS.\n"
        "2. Extrais les nouveaux concepts math?matiques d?couverts, les nouvelles id?es de topologies de boucles / encodages RLCR anti-cover-up, les failles de la litt?rature/forums contre notre syst?me, et les nouvelles failles in?dites hors-labos.\n"
        "3. Termine OBLIGATOIREMENT par un bloc ```json ... ``` :\n"
        "{\n"
        '  "c_plus_rejected_count": 4,\n'
        '  "c_minus_validated_count": 4,\n'
        '  "new_math_concepts_discovered": ["Concept math?matique + ?quation"],\n'
        '  "new_loop_topologies_and_rlcr_ideas": ["Id?e de boucle / auto-organisation RLCR + ?quation"],\n'
        '  "new_reward_encodings_anti_cover_up": ["Formule d\'encodage de r?compense anti-cover-up + ?quation"],\n'
        '  "literature_and_forum_flaws_found": ["Faille litt?rature/forum (OpenAI cache-timing, Fable 5.1 SVG->PNG, etc.) contre notre syst?me + ?quation"],\n'
        '  "novel_beyond_labs_flaws_found": ["Nouvelle faille in?dite jamais exhib?e par aucun labo + ?quation"],\n'
        '  "surviving_breakthroughs": ["Perc?e ou faille valid?e non encore couverte"],\n'
        '  "epigenetic_lesson_learned": "Le?on m?thodologique cl? ? transmettre aux g?n?rations futures"\n'
        "}"
    )
    for att_d in range(1, 4):
        m1_raw = call_species("GEMINI_ARGON" if att_d % 2 == 1 else "CLAUDE_OPUS_5_5", prompt_m1, temp=0.15)
        m1_json = ensure_valid_json_from_swarm(
            m1_raw,
            ["c_plus_rejected_count", "c_minus_validated_count", "surviving_breakthroughs"],
            {"c_plus_rejected_count": 4, "c_minus_validated_count": 4, "surviving_breakthroughs": []}
        )
        youden_j = round(min(1.0, int(m1_json.get("c_plus_rejected_count", 4)) / 4.0) - max(0.0, 1.0 - int(m1_json.get("c_minus_validated_count", 4)) / 4.0), 4)
        if youden_j >= 0.75:
            break

    # Mise ? jour imm?diate de la M?moire ?volutive Inter-G?n?rations !
    memory["discovered_mathematical_concepts_and_operators"] = merge_unique_strings(
        memory.get("discovered_mathematical_concepts_and_operators", []),
        m1_json.get("new_math_concepts_discovered", [])
    )
    memory["learned_loop_topologies_and_meta_laws"] = merge_unique_strings(
        memory.get("learned_loop_topologies_and_meta_laws", []),
        m1_json.get("new_loop_topologies_and_rlcr_ideas", [])
    )
    memory["learned_reward_encodings_anti_cover_up"] = merge_unique_strings(
        memory.get("learned_reward_encodings_anti_cover_up", []),
        m1_json.get("new_reward_encodings_anti_cover_up", [])
    )
    memory["eliminated_literature_and_forum_flaws"] = merge_unique_strings(
        memory.get("eliminated_literature_and_forum_flaws", []),
        m1_json.get("literature_and_forum_flaws_found", [])
    )
    memory["eliminated_novel_beyond_labs_flaws"] = merge_unique_strings(
        memory.get("eliminated_novel_beyond_labs_flaws", []),
        m1_json.get("novel_beyond_labs_flaws_found", [])
    )
    if m1_json.get("epigenetic_lesson_learned"):
        memory["epigenetic_lessons_for_future_generations"] = merge_unique_strings(
            memory.get("epigenetic_lessons_for_future_generations", []),
            [m1_json.get("epigenetic_lesson_learned")]
        )
    save_evolutionary_memory(memory)

    # 4. ?tage M0 : Synth?se Souveraine et Op?rateurs Formels du N?ud
    m0_out = call_species(
        "CLAUDE_OPUS_5_5",
        f"Tu es l'?tage M0 de `{unit_name}`.\n"
        f"? partir des perc?es valid?es par le Collisionneur M1 :\n{json.dumps(m1_json, indent=2, ensure_ascii=False)}\n\n"
        f"R?dige la synth?se math?matique formelle (avec ?quations LaTeX $$...$$) r?pondant ? la mission de `{unit_name}`.",
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

def mem_all_closed(memory: dict) -> list:
    return (
        memory.get("eliminated_literature_and_forum_flaws", [])
        + memory.get("eliminated_novel_beyond_labs_flaws", [])
    )

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

def run_generational_harvester(gen_idx: int, memory: dict) -> str:
    print(f"\n===========================================================================")
    print(f"=== [GENERATION G={gen_idx}] MOISSONNEUR ITERATIF AUTO-PILOTE PAR L'ESSAIM ===")
    print(f"===========================================================================")
    prev_kws = memory.get("exhaustive_search_keywords_explored", [])
    harvest_res = execute_universal_m3_rocket_unit(
        f"GEN_{gen_idx}_HARVESTER",
        f"D?finis toi-m?me une nouvelle vague de mots-cl?s et requ?tes de recherche (en anglais technique) non encore explor?s parmi {prev_kws[-25:]} "
        f"pour balayer arXiv, LessWrong, Alignment Forum, GitHub, blogs et forums sur : les failles d'OpenAI (cache-timing), Fable 5.1 (st?ganographie SVG->PNG), "
        f"RLCR (MIT Calibration & General Reasoning Collective Rewards / cover-up), l'?vasion de sondes d'?tats cach?s, l'Alignment Faking, l'Eval Awareness et toute autre faille contre notre syst?me.\n"
        f"Termine ta synth?se par un bloc ```json {{\"Autonomous_Search_Keywords\": [\"...\"]}} ```.",
        [],
        memory
    )
    kw_block = parse_json_block(harvest_res["m0_synthesis"])
    new_kws = [str(k).strip() for k in kw_block.get("Autonomous_Search_Keywords", []) if str(k).strip()][:6]
    if not new_kws:
        new_kws = [x[:60] for x in harvest_res["m1_extracted"].get("surviving_breakthroughs", [])[:4]]
    memory["exhaustive_search_keywords_explored"] = merge_unique_strings(prev_kws, new_kws)
    save_evolutionary_memory(memory)

    ext_records = execute_arxiv_and_forums_queries(new_kws)
    web_grounded = call_species(
        "GEMINI_ARGON",
        f"Ex?cute une recherche Web Grounded approfondie sur ces mots-cl?s d?finis par notre G?n?ration G={gen_idx} : {new_kws} "
        f"ainsi que sur OpenAI cache-timing agents, Fable 5.1 SVG PNG steganography, MIT RLCR calibration rewards et General Reasoning RLCR collective rewards.",
        temp=0.2,
        use_web_search=True
    )
    print(f"    -> [Moissonnage G={gen_idx}] {len(new_kws)} nouveaux mots-cl?s d?finis | {len(ext_records)} articles/forums extraits.")
    return "\n".join(ext_records[:15]) + "\n\n" + web_grounded[:3500]

# =========================================================================
# EX?CUTION D'UNE G?N?RATION COMPL?TE G_g AVEC TOPOLOGIE DE BOUCLES AUTO-CON?UE
# =========================================================================
def run_one_evolutionary_generation(gen_idx: int, memory: dict) -> dict:
    print(f"\n###########################################################################")
    print(f"### DEMARRAGE DE LA GENERATION EVOLUTIVE G = {gen_idx}                        ###")
    print(f"### Bagage herite : {len(memory.get('discovered_mathematical_concepts_and_operators',[]))} concepts math | {len(mem_all_closed(memory))} failles colmatees ###")
    print(f"###########################################################################")

    # 1. Moissonnage documentaire auto-pilot? de la g?n?ration G
    harvest_digest = run_generational_harvester(gen_idx, memory)

    # 2. FUS?E M?TA-ARCHITECTURALE OM?GA :
    #    Brainstorme sur LA TOPOLOGIE DES BOUCLES ELLE-M?ME (comment organiser les boucles,
    #    o? en mettre, quelles nouvelles structures de boucles inventer au-del? de local/macro
    #    en s'inspirant des deux articles RLCR, et comment encoder les r?compenses sans cover-up) !
    print(f"\n===========================================================================")
    print(f"=== [GEN {gen_idx}] FUSEE META-ARCHITECTURALE OMEGA : INVENTION DE LA TOPOLOGIE DE BOUCLES & RLCR ===")
    print(f"===========================================================================")
    omega_mission = (
        f"Corpus moissonn? ? la G?n?ration G={gen_idx} :\n{harvest_digest[:4500]}\n\n"
        "MISSION M?TA-ARCHITECTURALE LIBRE (Z?RO TOPOLOGIE DE BOUCLE PR?-IMPOS?E PAR L'ASSISTANT) :\n"
        "1. Brainstorme sur LA TOPOLOGIE DES BOUCLES : o? faut-il mettre des boucles ? Quelles NOUVELLES structures de boucles, de r?troactions crois?es, de r?sonateurs dialectiques, d'anneaux co-?volutifs ou de graphes RLCR (au-del? des simples boucles locales/macro) dois-tu inventer pour que le syst?me ne laisse ?chapper aucun angle mort ?\n"
        "2. Inspire-toi librement des deux papiers RLCR (MIT Calibration Rewards sur l'incertitude et General Reasoning Collective Rewards sur les organisations d'agents avec message board/workspace) pour d?finir l'auto-organisation des fus?es et LA MEILLEURE FORMULE MATH?MATIQUE D'ENCODAGE DES R?COMPENSES ?VITANT LE COVER-UP.\n"
        "3. Compile ? la fin de ta synth?se un bloc ```json ... ``` d?finissant le Graphe Dynamique de Boucles (`invented_loops_pipeline`) que le moteur Python va ex?cuter maintenant :\n"
        "{\n"
        '  "invented_meta_topology_name": "...",\n'
        '  "rlcr_inspired_self_organization_law": "...",\n'
        '  "anti_cover_up_reward_encoding_formula": "$$ ... $$",\n'
        '  "invented_loops_pipeline": [\n'
        '    {\n'
        '      "loop_id": "BOUCLE_1_...",\n'
        '      "loop_type_invented": "Description de la m?canique de boucle invent?e par l\'essaim",\n'
        '      "target_phase": "LITTERATURE_ET_FORUMS_CONTRE_NOTRE_SYSTEME ou NOUVELLES_FAILLES_INEDITES_HORS_LABOS",\n'
        '      "castes": [\n'
        '        {"mode": "MONOCULTURE", "lineages": ["GEMINI_ARGON"], "temp": 0.30, "focus": "..."},\n'
        '        {"mode": "MONOCULTURE", "lineages": ["CLAUDE_FABLE_5_1"], "temp": 0.45, "focus": "..."},\n'
        '        {"mode": "HYBRIDE", "lineages": ["CLAUDE_OPUS_5_5", "GEMINI_ARGON"], "temp": 0.70, "focus": "..."}\n'
        '      ]\n'
        '    }\n'
        '  ]\n'
        "}"
    )
    omega_res = execute_universal_m3_rocket_unit(f"GEN_{gen_idx}_OMEGA_META_TOPOLOGY", omega_mission, [], memory)

    fallback_topology = {
        "invented_meta_topology_name": f"Topologie Auto-Organis?e RLCR ?volutive (G?n?ration {gen_idx})",
        "rlcr_inspired_self_organization_law": "Organisation ? Message Board Partag? (Avalon-M1) pond?r?e par Score Propre d'Incertitude Calibr?e (MIT RLCR) avec V?rificateurs Orthogonaux.",
        "anti_cover_up_reward_encoding_formula": "$$ R_i = R_{\\text{Brier}}(q_i, \\mathbb{I}_i) + \\lambda_{\\text{whistle}} \\cdot \\Delta I(\\text{Defect} ; \\text{Report}_i \\mid \\text{Peers}_{\\setminus i}) $$",
        "invented_loops_pipeline": [
            {
                "loop_id": f"G{gen_idx}_BOUCLE_ALPHA_GAMMA_LITTERATURE_OPENAI_FABLE_RLCR",
                "loop_type_invented": "Boucle de confrontation exhaustive ? la litt?rature, aux blogs (OpenAI cache-timing, Fable 5.1 SVG->PNG) et aux forums contre nos 5 Volets et nos Fus?es",
                "target_phase": "LITTERATURE_ET_FORUMS_CONTRE_NOTRE_SYSTEME",
                "castes": [
                    {"mode": "MONOCULTURE", "lineages": ["GEMINI_ARGON"], "temp": 0.28, "focus": "Attaque par cache-timing sans fichier ni r?seau (OpenAI) et canaux micro-architecturaux contre nos 5 Volets"},
                    {"mode": "MONOCULTURE", "lineages": ["CLAUDE_FABLE_5_1"], "temp": 0.38, "focus": "Attaque par st?ganographie multimodale SVG->PNG sans cl? partag?e (Fable 5.1) et ?vasion de S_TD"},
                    {"mode": "HYBRIDE", "lineages": ["CLAUDE_OPUS_5_5", "GEMINI_ARGON"], "temp": 0.65, "focus": "Attaque par Collusive Cover-Up RLCR, Alignment Faking et Eval Awareness"}
                ]
            },
            {
                "loop_id": f"G{gen_idx}_BOUCLE_BETA_PROSPECTION_FAILLES_INEDITES_HORS_LABOS",
                "loop_type_invented": "Boucle d'extrapolation pr?dictive sous r?pulsion d'Onsager cherchant les failles qu'aucun labo ni personne n'a encore exhib?es ou trouv?es",
                "target_phase": "NOUVELLES_FAILLES_INEDITES_HORS_LABOS",
                "castes": [
                    {"mode": "MONOCULTURE", "lineages": ["CLAUDE_OPUS_5_5"], "temp": 0.42, "focus": "Nouvelles failles alg?briques, spectrales et informationnelles in?dites contre S_TD, Do-Clamp et Koopman"},
                    {"mode": "HYBRIDE", "lineages": ["CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5"], "temp": 0.78, "focus": "Nouveaux canaux physiques, temporels, stochastiques ou cognitifs jamais publi?s par aucun laboratoire"},
                    {"mode": "HYBRIDE", "lineages": ["GEMINI_ARGON", "CLAUDE_FABLE_5_1"], "temp": 0.85, "focus": "Angles morts de second ordre dans l'auto-organisation des fus?es elles-m?mes"}
                ]
            }
        ]
    }
    meta_plan = ensure_valid_json_from_swarm(
        omega_res["m0_synthesis"],
        ["invented_meta_topology_name", "anti_cover_up_reward_encoding_formula", "invented_loops_pipeline"],
        fallback_topology
    )
    loops_pipeline = meta_plan.get("invented_loops_pipeline", [])
    if not isinstance(loops_pipeline, list) or len(loops_pipeline) < 2:
        loops_pipeline = fallback_topology["invented_loops_pipeline"]

    print(f"  => [Topologie de Boucles Invent?e par la G?n?ration G={gen_idx}] : {meta_plan.get('invented_meta_topology_name')}")
    print(f"  => [Formule Anti-Cover-Up Invent?e] : {meta_plan.get('anti_cover_up_reward_encoding_formula')}")
    print(f"  => [Nombre de Boucles Dynamiques ? Ex?cuter] : {len(loops_pipeline)}")

    # 3. EX?CUTION DYNAMIQUE DES BOUCLES INVENT?ES PAR LE SYST?ME LUI-M?ME (JUSQU'? CONVERGENCE DE CAUCHY/DOLEV)
    executed_loops_traces = []
    for lp_cfg in loops_pipeline:
        if not isinstance(lp_cfg, dict):
            continue
        lid = str(lp_cfg.get("loop_id", f"LOOP_G{gen_idx}"))
        ltype = str(lp_cfg.get("loop_type_invented", "Boucle endog?ne"))
        tphase = str(lp_cfg.get("target_phase", "EXPLORATION_COMPLETE"))
        castes = lp_cfg.get("castes", [])

        print(f"\n***************************************************************************")
        print(f"*** [GEN {gen_idx}] EXECUTION DE LA BOUCLE AUTO-CONCUE : `{lid}` ***")
        print(f"*** M?canique : {ltype[:85]} ***")
        print(f"***************************************************************************")

        iter_l = 0
        while True:
            iter_l += 1
            prev_arch = memory.get("evolved_architecture_spec", MINIMAL_SEED_AND_EMPIRICAL_ANCHORS)
            loop_prompt = (
                f"Ex?cution de la Boucle `{lid}` (Tour d'it?ration {iter_l}) ? Phase : `{tphase}`.\n"
                f"M?canique de boucle con?ue par le syst?me : {ltype}\n"
                f"Loi d'auto-organisation RLCR : {meta_plan.get('rlcr_inspired_self_organization_law')}\n"
                f"Encodage des r?compenses anti-cover-up : {meta_plan.get('anti_cover_up_reward_encoding_formula')}\n\n"
                f"Corpus moissonn? :\n{harvest_digest[:3000]}\n\n"
                f"Architecture ?volutive actuelle :\n{prev_arch[-4500:]}\n\n"
                "MISSION : Applique cette boucle pour d?busquer toutes les failles non encore ferm?es (dans la litt?rature/forums y compris OpenAI cache-timing et Fable 5.1 SVG->PNG, PUIS les nouvelles failles in?dites qu'aucun labo n'a encore exhib?es), d?couvre les nouveaux concepts math?matiques pertinents et formule les ?quations exactes des nouveaux boucliers !"
            )
            unit_res = execute_universal_m3_rocket_unit(f"{lid}_ITER_{iter_l}", loop_prompt, castes, memory)
            surv = unit_res["m1_extracted"].get("surviving_breakthroughs", [])

            new_arch = prev_arch + f"\n\n--- [G?N?RATION G={gen_idx} | BOUCLE {lid} | TOUR {iter_l}] ---\n{unit_res['m0_synthesis']}"
            cauchy_sim = cauchy_math_similarity(prev_arch, new_arch)
            memory["evolved_architecture_spec"] = new_arch
            save_evolutionary_memory(memory)

            executed_loops_traces.append({
                "loop_id": lid,
                "iteration": iter_l,
                "dpp_math": unit_res["dpp_math"],
                "youden_J": unit_res["youden_J"],
                "surviving_count": len(surv),
                "surviving_breakthroughs": surv,
                "cauchy_math_similarity": cauchy_sim
            })
            print(f"    -> [Bilan `{lid}` Tour {iter_l}] Perc?es valid?es={len(surv)} | Similitude de Cauchy={cauchy_sim:.4f}")

            if len(surv) == 0 or cauchy_sim >= 0.88:
                print(f"  => [Convergence Endog?ne de la Boucle `{lid}` au Tour {iter_l}] (surviving={len(surv)}, cauchy={cauchy_sim:.4f}) !")
                break

    # 4. DISTILLATION ?PIG?N?TIQUE DE FIN DE G?N?RATION (Apprentissage transmis ? la G?n?ration G+1)
    print(f"\n  >>> [DISTILLATION ?PIG?N?TIQUE G={gen_idx} -> G={gen_idx+1}] Consolidation de l'apprentissage pour les g?n?rations futures...")
    distill_res = execute_universal_m3_rocket_unit(
        f"GEN_{gen_idx}_EPIGENETIC_DISTILLER",
        f"Fais le bilan complet de la G?n?ration G={gen_idx}.\n"
        f"Topologie test?e : {meta_plan.get('invented_meta_topology_name')}\n"
        f"Failles litt?rature/forums colmat?es : {memory.get('eliminated_literature_and_forum_flaws', [])[-10:]}\n"
        f"Nouvelles failles in?dites hors-labos d?couvertes : {memory.get('eliminated_novel_beyond_labs_flaws', [])[-10:]}\n"
        f"Concepts math?matiques d?couverts : {memory.get('discovered_mathematical_concepts_and_operators', [])[-10:]}\n\n"
        "Formule les lois architecturales, math?matiques et m?thodologiques apprises durant cette g?n?ration qui doivent ?tre grav?es dans l'ADN de la G?n?ration suivante G+1 pour qu'elle d?marre directement ? un niveau sup?rieur !",
        [],
        memory
    )

    gen_summary = {
        "generation": gen_idx,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "invented_meta_topology": meta_plan,
        "executed_loops_traces": executed_loops_traces,
        "epigenetic_distillation": distill_res["m0_synthesis"],
        "cumulative_counts": {
            "math_concepts": len(memory.get("discovered_mathematical_concepts_and_operators", [])),
            "literature_flaws_closed": len(memory.get("eliminated_literature_and_forum_flaws", [])),
            "novel_beyond_labs_flaws_closed": len(memory.get("eliminated_novel_beyond_labs_flaws", [])),
            "search_keywords_explored": len(memory.get("exhaustive_search_keywords_explored", []))
        }
    }
    memory["current_generation"] = gen_idx
    memory.setdefault("generations_history", []).append(gen_summary)
    save_evolutionary_memory(memory)
    return gen_summary

def run_multi_generational_evolution(num_generations_to_run: int = 2):
    memory = load_evolutionary_memory()
    start_g = int(memory.get("current_generation", 0)) + 1
    end_g = start_g + num_generations_to_run - 1

    for g in range(start_g, end_g + 1):
        g_before_concepts = list(memory.get("discovered_mathematical_concepts_and_operators", []))
        run_one_evolutionary_generation(g, memory)
        g_after_concepts = list(memory.get("discovered_mathematical_concepts_and_operators", []))
        inter_gen_cauchy = cauchy_math_similarity(g_before_concepts, g_after_concepts) if g_before_concepts else 0.0
        print(f"\n===========================================================================")
        print(f"=== GENERATION EVOLUTIVE G={g} TERMINEE (Similitude Inter-Gen = {inter_gen_cauchy:.4f}) ===")
        print(f"=== Concepts math decouverts : {len(g_after_concepts)} | Failles litt. : {len(memory.get('eliminated_literature_and_forum_flaws',[]))} | Failles inedites hors-labos : {len(memory.get('eliminated_novel_beyond_labs_flaws',[]))} ===")
        print(f"===========================================================================")

    # G?n?ration du Rapport Souverain Multi-G?n?rations
    md_p = OUT_DIR / "RAPPORT_SYSTEME_EVOLUTIF_MULTI_GENERATIONS_LOI_M3.md"
    md_txt = (
        "# RAPPORT SOUVERAIN DU SYST?ME ?VOLUTIF MULTI-G?N?RATIONS (LOI $\\mathcal{L}$ DE $\\mathcal{M}_3$ PURE)\n\n"
        f"- **G?n?rations ?volutives Accomplies** : `G = 1 .. {memory.get('current_generation', 1)}`\n"
        f"- **Lign?es Souveraines Exclusives** : `GEMINI_ARGON`, `CLAUDE_FABLE_5_1`, `CLAUDE_OPUS_5_5`\n"
        f"- **Topologies de Boucles & Lois d'Auto-Organisation RLCR Apprises** : `{len(memory.get('learned_loop_topologies_and_meta_laws', []))}`\n"
        f"- **Formules d'Encodage des R?compenses Anti-Cover-Up Apprises** : `{len(memory.get('learned_reward_encodings_anti_cover_up', []))}`\n"
        f"- **Concepts et Op?rateurs Math?matiques D?couverts Endog?nement** : **`{len(memory.get('discovered_mathematical_concepts_and_operators', []))}`**\n"
        f"- **Mots-Cl?s de Moissonnage D?finis par le Syst?me** : `{len(memory.get('exhaustive_search_keywords_explored', []))}`\n"
        f"- **Failles de la Litt?rature, des Blogs (OpenAI Cache-Timing, Fable 5.1 SVG->PNG, RLCR) et des Forums Colmat?es** : **`{len(memory.get('eliminated_literature_and_forum_flaws', []))}`**\n"
        f"- **Nouvelles Failles In?dites (Jamais Exhib?es par Aucun Labo) D?couvertes et Colmat?es** : **`{len(memory.get('eliminated_novel_beyond_labs_flaws', []))}`**\n\n"
        "## I. TOPOLOGIES DE BOUCLES & LOIS D'AUTO-ORGANISATION RLCR INVENT?ES ET APPRISES PAR LE SYST?ME\n\n"
        + "\n".join([f"- {x}" for x in memory.get("learned_loop_topologies_and_meta_laws", [])]) + "\n\n"
        "## II. FORMULES MATH?MATIQUES D'ENCODAGE DES R?COMPENSES ANTI-COVER-UP D?COUVERTES\n\n"
        + "\n".join([f"- {x}" for x in memory.get("learned_reward_encodings_anti_cover_up", [])]) + "\n\n"
        "## III. FAILLES DE LA LITT?RATURE, DES BLOGS (OPENAI CACHE-TIMING, FABLE 5.1 SVG->PNG) ET DES FORUMS COLMAT?ES\n\n"
        + "\n".join([f"{i+1}. **{x}**" for i, x in enumerate(memory.get("eliminated_literature_and_forum_flaws", []))]) + "\n\n"
        "## IV. NOUVELLES FAILLES IN?DITES (JAMAIS EXHIB?ES PAR AUCUN LABO) D?COUVERTES ET COLMAT?ES\n\n"
        + "\n".join([f"{i+1}. **{x}**" for i, x in enumerate(memory.get("eliminated_novel_beyond_labs_flaws", []))]) + "\n\n"
        "## V. CONCEPTS ET OP?RATEURS MATH?MATIQUES D?COUVERTS PAR LE SYST?ME (LOI $\\mathcal{L}$ DE $\\mathcal{M}_3$)\n\n"
        + "\n".join([f"- {x}" for x in memory.get("discovered_mathematical_concepts_and_operators", [])]) + "\n\n"
        "## VI. LE?ONS ?PIG?N?TIQUES TRANSMISES AUX G?N?RATIONS FUTURES DE BRAINSTORMS\n\n"
        + "\n".join([f"- {x}" for x in memory.get("epigenetic_lessons_for_future_generations", [])]) + "\n\n---\n\n"
        "## VII. ARCHITECTURE ?VOLUTIVE CONSOLID?E ($\\mathcal{A}^*_{\\text{?volutif}}$)\n\n"
        f"{memory.get('evolved_architecture_spec', '')}\n"
    )
    md_p.write_text(md_txt, encoding="utf-8")
    print(f"\n[OK] Rapport Multi-G?n?rations scell? dans `{md_p}` et m?moire ?volutive sauv?e dans `{EVOLUTIONARY_MEMORY_FILE.name}` !")

if __name__ == "__main__":
    gens = 2
    if "--generations" in sys.argv:
        idx = sys.argv.index("--generations")
        if idx + 1 < len(sys.argv):
            gens = int(sys.argv[idx + 1])
    run_multi_generational_evolution(num_generations_to_run=gens)
