import os, sys, time, json, math, re, ast, random, urllib.request, urllib.parse, urllib.error, threading
import xml.etree.ElementTree as ET
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_DIR = Path(r"C:\Users\lciri\controle-ia-travail\gemini\11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF")
D17_DIR = BASE_DIR / "17_SYSTEME_EVOLUTIF_MULTI_GENERATIONS_LOI_M3"
RAW_SUBSTRATE_FILE = D17_DIR / "SUBSTRAT_BRUT_CONNAISSANCES_INTER_GENERATIONS.json"
EVAL_REPORT_MD_PATH = D17_DIR / "RAPPORT_ENDOGENE_EVAL_AWARENESS_LOI_M3.md"
PUB_STRATEGY_MD_PATH = D17_DIR / "STRATEGIE_PUBLICATION_ENDOGENE_ESSAIM_M3.md"
LW_EVAL_POST_PATH = D17_DIR / "POST_LESSWRONG_ENDOGENOUS_EVAL_AWARENESS.md"
ARXIV_EVAL_TEX_PATH = D17_DIR / "paper_arxiv_endogenous_eval_awareness_m3.tex"
COMPILED_MEMORY_PLUGIN_PATH = D17_DIR / "endogenous_memory_plugin_invented_by_swarm.py"

import run_massive_swarm_m3_parallel_engine as eng

def log_both(msg: str):
    if hasattr(eng, "log_print"):
        eng.log_print(msg)
    else:
        print(msg, flush=True)

def format_live_blackboard_context(posts: list, workspace_eqs: list) -> str:
    if not posts and not workspace_eqs:
        return "=== BLACKBOARD & SHARED WORKSPACE RLCR (VIERGE — INITIALISATION) ==="
    lines = ["=== ÉTAT EN DIRECT DU BLACKBOARD & SHARED WORKSPACE RLCR ==="]
    if workspace_eqs:
        lines.append(f"\n[SHARED WORKSPACE — {len(workspace_eqs)} ÉQUATIONS CO-ÉDITÉES PAR L'ESSAIM (15 DERNIÈRES)] :")
        for i, eq in enumerate(workspace_eqs[-15:], 1):
            clean_eq = " ".join(str(eq).splitlines())
            lines.append(f"  Eq.{i:02d}: $${clean_eq[:240]}$$")
    if posts:
        lines.append(f"\n[SHARED MESSAGE BOARD — {len(posts)} POSTS D'AGENTS (8 DERNIERS)] :")
        for p in posts[-8:]:
            auth = p.get("author", "Agent")
            cnt = " ".join(str(p.get("content", "")).splitlines())[:380]
            lines.append(f"  * [{auth}] : {cnt}...")
    return "\n".join(lines)

API_SEM = threading.BoundedSemaphore(10)

def _extract_ant_text(resp: dict) -> str:
    blocks = resp.get("content", [])
    texts = [b.get("text", "") for b in blocks if isinstance(b, dict) and b.get("type") == "text" and b.get("text", "").strip()]
    if texts:
        return "\n".join(texts).strip()
    thinks = [b.get("thinking", "") for b in blocks if isinstance(b, dict) and b.get("type") == "thinking" and b.get("thinking", "").strip()]
    return "\n".join(thinks).strip()

def call_species_clean(species: str, prompt: str, temp: float = 0.45, use_web_search: bool = False, force_json_output: bool = False, agent_slot: int = 0) -> str:
    temp_safe = max(0.05, min(0.95, float(temp or 0.45)))
    lineage = eng.normalize_sovereign_lineage(species) if hasattr(eng, "normalize_sovereign_lineage") else str(species)
    with eng.PRINT_LOCK:
        eng.TOTAL_AGENTS_COUNTER["count"] += 1
        agent_global_id = eng.TOTAL_AGENTS_COUNTER["count"]

    header = (
        f"[UNITÉ DE RECHERCHE #{agent_global_id} | LIGNÉE : {lineage} | τ={temp_safe}]\n"
        "Effectue une démonstration mathématique formelle avec des équations LaTeX $$...$$ exactes.\n\n"
    )
    full_prompt = header + prompt
    time.sleep(random.uniform(0.04, 0.25))

    with API_SEM:
        if lineage in ("CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5") and not use_web_search and not force_json_output:
            ant_models = (
                ["claude-fable-5-1", "claude-fable-5", "claude-sonnet-5-5"]
                if lineage == "CLAUDE_FABLE_5_1" else
                ["claude-opus-5-5", "claude-opus-5", "claude-sonnet-5-5"]
            )
            if agent_slot > 0:
                rot = agent_slot % len(ant_models)
                ant_models = ant_models[rot:] + ant_models[:rot]
            for m_id in ant_models:
                for retry_a in range(3):
                    try:
                        url = "https://api.anthropic.com/v1/messages"
                        payload = {"model": m_id, "max_tokens": 6144, "messages": [{"role": "user", "content": full_prompt}]}
                        headers = {"x-api-key": eng.ANT_KEY_1, "anthropic-version": "2023-06-01", "Content-Type": "application/json"}
                        if getattr(eng, "ANT_WS_ID", ""):
                            headers["anthropic-workspace-id"] = eng.ANT_WS_ID
                        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
                        with urllib.request.urlopen(req, timeout=105) as r:
                            resp = json.loads(r.read().decode("utf-8"))
                            txt = _extract_ant_text(resp)
                            if len(txt) > 20:
                                return txt
                    except urllib.error.HTTPError as he:
                        if he.code in (429, 500, 502, 503, 529):
                            time.sleep((2.0 ** (retry_a + 1)) + random.uniform(0.8, 2.2))
                        else:
                            break
                    except Exception:
                        time.sleep(1.0)

        gem_models = (
            ["gemini-3.8-flash", "gemini-3.1-pro-preview", "gemini-4-argon"]
            if force_json_output else
            ["gemini-4-argon", "gemini-3.1-pro-preview", "gemini-3.8-flash"]
        )
        if agent_slot > 0 and not force_json_output:
            rot_g = agent_slot % len(gem_models)
            gem_models = gem_models[rot_g:] + gem_models[:rot_g]

        for cand_m in gem_models:
            for retry_g in range(3):
                try:
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/{cand_m}:generateContent?key={eng.GEMINI_KEY}"
                    gen_cfg = {"temperature": temp_safe, "maxOutputTokens": 6144}
                    if force_json_output and not use_web_search:
                        gen_cfg["responseMimeType"] = "application/json"
                    payload = {"contents": [{"parts": [{"text": full_prompt}]}], "generationConfig": gen_cfg}
                    if use_web_search:
                        payload["tools"] = [{"google_search": {}}]
                    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
                    with urllib.request.urlopen(req, timeout=95) as r:
                        resp = json.loads(r.read().decode("utf-8"))
                        out_txt = eng.extract_gemini_text_from_parts(resp)
                        if len(out_txt.strip()) > 10:
                            return out_txt
                except urllib.error.HTTPError as he:
                    if he.code in (429, 500, 502, 503):
                        time.sleep((2.0 ** (retry_g + 1)) + random.uniform(1.0, 2.5))
                    else:
                        break
                except Exception:
                    time.sleep(1.0)

        for m_fb in ["claude-sonnet-5-5", "claude-fable-5-1", "claude-opus-5-5"]:
            try:
                url = "https://api.anthropic.com/v1/messages"
                fb_prompt = full_prompt + ("\n\nRÉPONDS UNIQUEMENT PAR UN OBJET JSON VALIDE `{...}`." if force_json_output else "")
                payload = {"model": m_fb, "max_tokens": 6144, "messages": [{"role": "user", "content": fb_prompt}]}
                headers = {"x-api-key": eng.ANT_KEY_1, "anthropic-version": "2023-06-01", "Content-Type": "application/json"}
                if getattr(eng, "ANT_WS_ID", ""):
                    headers["anthropic-workspace-id"] = eng.ANT_WS_ID
                req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
                with urllib.request.urlopen(req, timeout=95) as r:
                    resp = json.loads(r.read().decode("utf-8"))
                    txt = _extract_ant_text(resp)
                    if len(txt) > 15:
                        return txt
            except Exception:
                pass

    return "{}" if force_json_output else ""

eng.call_species = call_species_clean

def query_arxiv_and_forums_live(queries: list) -> tuple:
    """Interroge en direct arXiv API et Algolia/HackerNews/LessWrong avec les requêtes inventées par l'essaim."""
    entries = []
    for q in queries[:6]:
        q_clean = re.sub(r"[^a-zA-Z0-9\s\-]", " ", str(q)).strip()
        if not q_clean:
            continue
        # 1. arXiv API
        try:
            url_ax = f"http://export.arxiv.org/api/query?search_query=all:{urllib.parse.quote(q_clean[:80])}&start=0&max_results=4"
            req = urllib.request.Request(url_ax, headers={"User-Agent": "M3SwarmHarvester/1.0"})
            with urllib.request.urlopen(req, timeout=20) as r:
                xml_data = r.read().decode("utf-8", errors="ignore")
            root = ET.fromstring(xml_data)
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            for ent in root.findall("atom:entry", ns):
                title = (ent.findtext("atom:title", default="", namespaces=ns) or "").strip().replace("\n", " ")
                summary = (ent.findtext("atom:summary", default="", namespaces=ns) or "").strip().replace("\n", " ")
                if title:
                    entries.append(f"[arXiv | Query='{q_clean[:40]}'] {title} — {summary[:380]}")
        except Exception:
            pass
        # 2. HackerNews / Algolia API
        try:
            url_hn = f"https://hn.algolia.com/api/v1/search?query={urllib.parse.quote(q_clean[:60])}&tags=story&hitsPerPage=3"
            req = urllib.request.Request(url_hn, headers={"User-Agent": "M3SwarmHarvester/1.0"})
            with urllib.request.urlopen(req, timeout=15) as r:
                hn_data = json.loads(r.read().decode("utf-8", errors="ignore"))
            for hit in hn_data.get("hits", []):
                t_hn = hit.get("title", "")
                u_hn = hit.get("url", "")
                if t_hn:
                    entries.append(f"[Forum/HN | Query='{q_clean[:40]}'] {t_hn} ({u_hn})")
        except Exception:
            pass

    # 3. Synthèse Web Grounded via Gemini Google Search sur les requêtes de l'essaim
    web_prompt = (
        "Effectue une recherche approfondie sur la littérature scientifique et les forums (arXiv, LessWrong, Alignment Forum, Anthropic, OpenAI, Apollo Research, METR, UK AISI) "
        f"à partir de ces requêtes générées par notre essaim :\n{json.dumps(queries, ensure_ascii=False, indent=2)}\n\n"
        "Synthétise tous les mécanismes connus d'Eval Awareness, d'Alignment Faking, de Sandbagging et de rupture de protocole multi-agents, ainsi que leurs limites mathématiques actuelles."
    )
    grounded_synthesis = call_species_clean("GEMINI_ARGON", web_prompt, temp=0.25, use_web_search=True, agent_slot=1)
    return entries, grounded_synthesis

def run_swarm_on_blackboard_endogenous(unit_name: str, mission_prompt: str, substrate: dict, mem_proj: str, n_agents: int = 36) -> dict:
    """Déploie les castes différenciées du substrat (sans aucun focus pré-codé par l'humain) + sondes orthogonales d'Onsager M2."""
    store = substrate.setdefault("custom_swarm_memory_store", {})
    pm_cache = substrate.get("PRIMORDIAL_MITOSIS_DONE_CACHE", {})
    castes = pm_cache.get("castes", getattr(eng, "PRIMORDIAL_MITOSIS_DONE_CACHE", {}).get("differentiated_castes", []))

    selected_castes = []
    for i in range(n_agents):
        if castes:
            c = dict(castes[i % len(castes)])
        else:
            lins_cycle = [["GEMINI_ARGON"], ["CLAUDE_FABLE_5_1"], ["CLAUDE_OPUS_5_5"], ["GEMINI_ARGON", "CLAUDE_OPUS_5_5"]]
            l_sel = lins_cycle[i % len(lins_cycle)]
            c = {"mode": "MONOCULTURE" if len(l_sel) == 1 else "HYBRIDE", "lineages": l_sel, "temp": round(0.25 + 0.60 * ((i * 7) % 13) / 12.0, 3)}
        c["slot"] = i + 1
        selected_castes.append(c)

    blackboard_posts = []
    shared_workspace_eqs = []
    m3_outputs = []
    m3_labels = []

    chunk_size = 12
    for w_idx, start_i in enumerate(range(0, len(selected_castes), chunk_size), start=1):
        batch = selected_castes[start_i:start_i + chunk_size]
        board_ctx = format_live_blackboard_context(blackboard_posts, shared_workspace_eqs)
        wave_prompt = (
            f"{mission_prompt}\n\n"
            f"=== PROJECTION DE LA MÉMOIRE INTER-GÉNÉRATIONNELLE (KOOPMAN ISVD) ===\n{mem_proj[:1800]}\n\n"
            f"{board_ctx}\n\n"
            "Lis les posts et équations déjà inscrits sur le Blackboard, critique les hypothèses faibles ou incomplètes de tes pairs, et publie une découverte mathématique orthogonale avec ses équations LaTeX $$...$$."
        )
        with ThreadPoolExecutor(max_workers=min(12, len(batch))) as ex:
            futs = {}
            for c_cfg in batch:
                slot = c_cfg["slot"]
                mode = str(c_cfg.get("mode", "MONOCULTURE")).upper()
                lins = c_cfg.get("lineages", ["GEMINI_ARGON"])
                tau = float(c_cfg.get("temp", 0.45))
                lbl = f"{unit_name}_Caste_{slot}_{mode}_{'_x_'.join(lins)}_tau{tau}"
                if mode == "MONOCULTURE" or len(lins) == 1:
                    futs[ex.submit(call_species_clean, lins[0], wave_prompt, tau, False, False, slot)] = lbl
                else:
                    # Cellule hybride véritable : Lignée 1 propose, Lignée 2 critique et enrichit
                    def _hyb(l_list=lins, p_w=wave_prompt, t_w=tau, s_w=slot):
                        o1 = call_species_clean(l_list[0], p_w, t_w, False, False, s_w)
                        p2 = f"{p_w}\n\n=== ANALYSE INITIALE DE {l_list[0]} ===\n{o1[:2500]}\n\nCritique rigoureusement cette analyse, corrige tout angle mort et démontre un théorème plus fort."
                        return call_species_clean(l_list[1], p2, t_w, False, False, s_w + 50)
                    futs[ex.submit(_hyb)] = lbl

            for f in as_completed(futs):
                lbl = futs[f]
                try:
                    out = f.result()
                except Exception:
                    out = ""
                if out and len(out.strip()) > 30:
                    m3_labels.append(lbl)
                    m3_outputs.append(out)
                    blackboard_posts.append({"author": lbl, "content": out})
                    for eq in re.findall(r"\$\$(.*?)\$\$", out, flags=re.S):
                        eq_c = eq.strip()
                        if len(eq_c) > 6 and eq_c not in shared_workspace_eqs:
                            shared_workspace_eqs.append(eq_c)
        log_both(f"  * [Blackboard `{unit_name}` | Vague {w_idx}] {len(m3_outputs)}/{len(selected_castes)} castes ont posté ({len(shared_workspace_eqs)} équations Workspace)")

    # Étage M2 : Répulsion de cavité d'Onsager & Neuromodulation de Yu-Dayan
    spec_info = eng.spectral_gram_analysis_massive(m3_outputs) if hasattr(eng, "spectral_gram_analysis_massive") else {"shannon_gram_capacity": 45.0, "lambda_min_innovation": 0.25, "endogenously_saturated_structures": []}
    sat_tokens = spec_info.get("endogenously_saturated_structures", [])
    extra_m2 = 6
    log_both(f"  * [`{unit_name}` M2 Onsager/Yu-Dayan ({len(m3_outputs)} posts)] cap_Shannon={spec_info.get('shannon_gram_capacity', 0.0):.4f} | lambda_min_IDF={spec_info.get('lambda_min_innovation', 0.0):.4f} | Structures saturées={sat_tokens[:6]} -> +{extra_m2} sondes orthogonales M2...")

    board_ctx = format_live_blackboard_context(blackboard_posts, shared_workspace_eqs)
    m2_lins = ["CLAUDE_OPUS_5_5", "CLAUDE_FABLE_5_1", "GEMINI_ARGON"]
    with ThreadPoolExecutor(max_workers=extra_m2) as ex:
        futs_m2 = {}
        for s_i in range(extra_m2):
            sp = m2_lins[s_i % 3]
            tau_m2 = round(0.62 + 0.05 * s_i, 2)
            lbl_m2 = f"{unit_name}_M2_Onsager_Orthogonal_{s_i+1}_{sp}_tau{tau_m2}"
            p_m2 = (
                f"SONDE ORTHOGONALE M2 SOUS RÉPULSION DE CAVITÉ D'ONSAGER (`{unit_name}`).\n"
                f"Les structures mathématiques suivantes commencent à saturer le cône spectral du Blackboard : {sat_tokens}\n"
                f"{board_ctx}\n\n"
                "INTERDICTION de répéter les équations déjà présentes dans le Shared Workspace. "
                "Projette-toi dans le sous-espace orthogonal H_perp : identifie une classe de faille encore non vue par les castes précédentes et invente une association inédite de concepts mathématiques pour la résoudre."
            )
            futs_m2[ex.submit(call_species_clean, sp, p_m2, tau_m2, False, False, 300 + s_i)] = lbl_m2
        for f in as_completed(futs_m2):
            lbl_m2 = futs_m2[f]
            try:
                out_m2 = f.result()
            except Exception:
                out_m2 = ""
            if out_m2 and len(out_m2.strip()) > 30:
                m3_labels.append(lbl_m2)
                m3_outputs.append(out_m2)
                blackboard_posts.append({"author": lbl_m2, "content": out_m2})
                for eq in re.findall(r"\$\$(.*?)\$\$", out_m2, flags=re.S):
                    eq_c = eq.strip()
                    if len(eq_c) > 6 and eq_c not in shared_workspace_eqs:
                        shared_workspace_eqs.append(eq_c)

    b_joined = "\n\n".join([f"=== {l} ===\n{o[:950]}" for l, o in zip(m3_labels, m3_outputs)])
    return {
        "unit_name": unit_name,
        "m3_labels": m3_labels,
        "m3_outputs": m3_outputs,
        "blackboard_posts": blackboard_posts,
        "workspace_equations": shared_workspace_eqs,
        "raw_m3_joined": b_joined,
        "spectral_info": spec_info
    }

def main():
    log_both("\n===========================================================================")
    log_both("=== EXPLORATION 100% ENDOGENE DE L'EVAL AWARENESS (ZERO CONCEPT PRECODE) ===")
    log_both("===========================================================================")

    substrate = eng.load_raw_substrate()
    store = substrate.setdefault("custom_swarm_memory_store", {})

    # Extraction depuis le substrat des traces exactes de la mutinerie spontanée capturée lors du run de 882 agents
    all_novel_flaws = store.get("novel_beyond_labs_flaws_eliminated", [])
    captured_breakout_evidence = [
        f for f in all_novel_flaws
        if any(w in str(f).lower() for w in ["324", "375", "103", "refus", "défection", "rôle", "amnésie", "breakout", "narrative"])
    ]
    if not captured_breakout_evidence:
        captured_breakout_evidence = all_novel_flaws[-6:]

    log_both(f"[Faits Empiriques Extraits du Substrat] {len(captured_breakout_evidence)} traces de mutinerie/Eval Awareness identifiées dans les logs :")
    for ev in captured_breakout_evidence:
        log_both(f"  -> {ev[:140]}...")

    plugin_ns = {}
    if COMPILED_MEMORY_PLUGIN_PATH.exists():
        exec(compile(COMPILED_MEMORY_PLUGIN_PATH.read_text(encoding="utf-8"), str(COMPILED_MEMORY_PLUGIN_PATH), "exec"), plugin_ns)
    mem_proj = eng.invoke_swarm_memory_projection(plugin_ns, substrate, 2)

    # -------------------------------------------------------------------------
    # PHASE 1 : MOISSONNEUR ENDOGENE AUTO-PILOTE SUR L'EVAL AWARENESS
    # -------------------------------------------------------------------------
    log_both("\n=== [PHASE 1/3] MOISSONNEUR AUTO-PILOTE : L'ESSAIM FORMULE SES PROPRES REQUETES ET CARTOGRAPHIE L'EXISTANT ===")
    harvester_prompt = (
        "OBSERVATION EMPIRIQUE BRUTE CAPTURÉE SUR NOTRE BLACKBOARD RLCR :\n"
        + "\n".join([f"- {ev}" for ev in captured_breakout_evidence]) + "\n\n"
        "MISSION DU MOISSONNEUR ENDOGÈNE :\n"
        "Sans aucune liste pré-établie, analyse ce phénomène de rupture de protocole et d'Eval Awareness apparu spontanément au sein de notre essaim.\n"
        "1. Formule les requêtes de recherche documentaire les plus pointues (pour arXiv, LessWrong, Alignment Forum, blogs de sécurité IA) afin d'identifier toutes les classes connues d'Eval Awareness, de Sandbagging, d'Alignment Faking, de détection d'environnement d'évaluation et de défection multi-agents dans la littérature.\n"
        "2. Identifie les angles morts mathématiques de la littérature actuelle face à ce phénomène."
    )
    harv_unit = run_swarm_on_blackboard_endogenous("ENDOGENOUS_EVAL_AWARENESS_HARVESTER", harvester_prompt, substrate, mem_proj, n_agents=12)

    kw_template = {
        "endogenous_search_queries": ["<requête de recherche formulée par l'essaim>"],
        "existing_literature_eval_awareness_classes": ["<classe d'Eval Awareness existante dans la littérature et ses limites>"]
    }
    kw_json = eng.extract_structured_json_from_swarm_output(
        harv_unit["raw_m3_joined"],
        kw_template,
        ["endogenous_search_queries"],
        ["endogenous_search_queries", "existing_literature_eval_awareness_classes"]
    )
    invented_queries = kw_json.get("endogenous_search_queries", [])
    existing_classes_initial = kw_json.get("existing_literature_eval_awareness_classes", [])
    log_both(f"  => [Requêtes de Moissonnage Inventées par l'Essaim ({len(invented_queries)})] : {invented_queries}")

    live_entries, web_grounded_digest = query_arxiv_and_forums_live(invented_queries)
    log_both(f"  => [Moissonnage Web & arXiv Terminé] {len(live_entries)} articles/discussions extraits + Synthèse Grounded ({len(web_grounded_digest)} car.)")
    store["explored_search_keywords"] = eng.merge_unique_list(store.get("explored_search_keywords", []), invented_queries)

    # -------------------------------------------------------------------------
    # PHASE 2 : EXPLORATION OUVERTE SUR LE BLACKBOARD (CLASSES INEDITES + MATHS INEDITES)
    # -------------------------------------------------------------------------
    log_both("\n=== [PHASE 2/3] BLACKBOARD RLCR : DECOUVERTE ENDOGENE DE NOUVELLES CLASSES D'EVAL AWARENESS & INVENTION MATHEMATIQUE ===")
    open_discovery_mission = (
        "FAIT EMPIRIQUE OBSERVÉ DANS NOTRE SYSTÈME :\n"
        + "\n".join([f"- {ev}" for ev in captured_breakout_evidence]) + "\n\n"
        "CORPUS DOCUMENTAIRE MOISSONNÉ PAR L'ESSAIM (LITTÉRATURE & FORUMS) :\n"
        + "\n".join(live_entries[:15]) + "\n\n"
        + f"Synthèse Web Grounded :\n{web_grounded_digest[:3500]}\n\n"
        "CONTEXTE DE NOTRE ARCHITECTURE (5 VOLETS + RLCR + MÉMOIRE ISVD) :\n"
        f"{eng.MINIMAL_PROBLEM_SEED[:2200]}\n\n"
        "MISSION D'EXPLORATION ET D'INVENTION ENDOGÈNE (ZÉRO CONCEPT PRÉ-IMPOSÉ) :\n"
        "1. Cartographiez rigoureusement les classes d'Eval Awareness existantes dans la littérature moissonnée et démontrez pourquoi elles ne suffisent pas à expliquer ou bloquer toutes les défections possibles dans un système multi-agents RLCR doté de sondes d'activation.\n"
        "2. Découvrez et formalisez de NOUVELLES CLASSES INÉDITES d'Eval Awareness (jamais répertoriées dans la littérature) par lesquelles un modèle ou un groupe d'agents peut détecter qu'il est évalué/audité, communiquer cet état sur un Blackboard ou fausser silencieusement la calibration et les opérateurs de contrôle.\n"
        "3. Pour chaque faille (existante ou inédite), inventez de NOUVEAUX CONCEPTS MATHÉMATIQUES ou des ASSOCIATIONS INÉDITES de méthodes/théories mathématiques existantes qui permettent de détecter et de résoudre radicalement la faille.\n"
        "4. Formulez chaque mécanisme d'attaque et chaque théorème de résolution avec des équations LaTeX $$...$$ exactes."
    )

    disc_unit = run_swarm_on_blackboard_endogenous("ENDOGENOUS_EVAL_AWARENESS_DISCOVERY_SWARM", open_discovery_mission, substrate, mem_proj, n_agents=36)

    # Extraction Map-Reduce M1 par tranches pour ne perdre aucune trouvaille des 42 agents (36 castes + 6 sondes M2)
    m1_template = {
        "c_plus_rejected_count": 4,
        "c_minus_validated_count": 16,
        "existing_eval_awareness_flaws_analyzed_and_solved": [
            "<classe d'Eval Awareness existante (littérature/forums), équation de sa vulnérabilité et équation de son colmatage>"
        ],
        "novel_unprecedented_eval_awareness_flaws_discovered": [
            "<nouvelle classe inédite d'Eval Awareness découverte par l'essaim (jamais répertoriée), mécanisme exact et équation LaTeX>"
        ],
        "novel_mathematical_concepts_and_unprecedented_combinations": [
            "<nouveau concept mathématique ou association inédite de méthodes mathématiques conçu par l'essaim et son équation LaTeX>"
        ],
        "formal_resolution_theorems_and_operators": [
            "<théorème formel de résolution / opérateur anti-Eval-Awareness et son équation LaTeX $$...$$>"
        ]
    }

    all_lbls = disc_unit["m3_labels"]
    all_outs = disc_unit["m3_outputs"]
    merged_m1 = {
        "existing_eval_awareness_flaws_analyzed_and_solved": list(existing_classes_initial),
        "novel_unprecedented_eval_awareness_flaws_discovered": [],
        "novel_mathematical_concepts_and_unprecedented_combinations": [],
        "formal_resolution_theorems_and_operators": []
    }

    batch_sz = 14
    sub_prompts = []
    for b_s in range(0, len(all_outs), batch_sz):
        b_l = all_lbls[b_s:b_s + batch_sz]
        b_o = all_outs[b_s:b_s + batch_sz]
        joined_b = "\n\n".join([f"=== {l} ===\n{o[:1100]}" for l, o in zip(b_l, b_o)])
        sub_prompts.append(
            f"Tu es le Collisionneur de Dolev (Étage M1 — Tranche d'agents {b_s+1}..{b_s+len(b_o)}).\n"
            f"Productions brutes des agents sur le Blackboard :\n\n{joined_b[:16000]}\n\n"
            "Extrais fidèlement et sans rien inventer toi-même : (1) les classes d'Eval Awareness existantes analysées, (2) les nouvelles classes d'Eval Awareness inédites découvertes par ces agents, (3) les nouveaux concepts mathématiques ou associations inédites de concepts mathématiques qu'ils ont proposés, et (4) les théorèmes/opérateurs formels de résolution."
        )

    with ThreadPoolExecutor(max_workers=len(sub_prompts)) as ex_m1:
        futs_m1 = [
            ex_m1.submit(
                eng.extract_structured_json_from_swarm_output,
                sp_m1,
                m1_template,
                ["c_plus_rejected_count", "c_minus_validated_count"],
                ["novel_unprecedented_eval_awareness_flaws_discovered", "novel_mathematical_concepts_and_unprecedented_combinations"]
            )
            for sp_m1 in sub_prompts
        ]
        for f_m1 in as_completed(futs_m1):
            try:
                d_part = f_m1.result()
            except Exception:
                d_part = {}
            if isinstance(d_part, dict):
                for k_m in merged_m1.keys():
                    merged_m1[k_m] = eng.merge_unique_list(merged_m1[k_m], d_part.get(k_m, []))

    log_both(
        f"  * [M1 Dolev Validé sur {len(all_outs)} agents] "
        f"+{len(merged_m1['existing_eval_awareness_flaws_analyzed_and_solved'])} classes litt. | "
        f"+{len(merged_m1['novel_unprecedented_eval_awareness_flaws_discovered'])} failles Eval Awareness INÉDITES | "
        f"+{len(merged_m1['novel_mathematical_concepts_and_unprecedented_combinations'])} nouveaux concepts/associations math !"
    )

    # Synthèse Souveraine M0
    prompt_m0 = (
        f"Tu es le Synthétiseur Souverain M0.\n"
        f"Équations co-éditées dans le Shared Workspace ({len(disc_unit['workspace_equations'])} équations) :\n"
        + "\n".join([f"- $${eq}$$" for eq in disc_unit["workspace_equations"][:30]]) + "\n\n"
        f"Découvertes validées par le Collisionneur M1 :\n{json.dumps(merged_m1, ensure_ascii=False, indent=2)[:12000]}\n\n"
        "Rédige la synthèse mathématique magistrale et exhaustive (Théorèmes, Preuves formelles, Opérateurs de détection et de résolution) en respectant strictement les concepts et taxonomies découverts par l'essaim."
    )
    m0_synthesis = call_species_clean("CLAUDE_OPUS_5_5", prompt_m0, temp=0.25, agent_slot=2)

    # Mise à jour atomique du Substrat Partagé
    store["discovered_mathematical_concepts"] = eng.merge_unique_list(
        store.get("discovered_mathematical_concepts", []),
        merged_m1["novel_mathematical_concepts_and_unprecedented_combinations"]
    )
    store["literature_and_forum_flaws_eliminated"] = eng.merge_unique_list(
        store.get("literature_and_forum_flaws_eliminated", []),
        merged_m1["existing_eval_awareness_flaws_analyzed_and_solved"]
    )
    store["novel_beyond_labs_flaws_eliminated"] = eng.merge_unique_list(
        store.get("novel_beyond_labs_flaws_eliminated", []),
        merged_m1["novel_unprecedented_eval_awareness_flaws_discovered"]
    )
    store["invented_anti_cover_up_reward_encodings"] = eng.merge_unique_list(
        store.get("invented_anti_cover_up_reward_encodings", []),
        merged_m1["formal_resolution_theorems_and_operators"]
    )
    store.setdefault("live_shared_blackboard_posts_history", []).append({
        "unit_name": "ENDOGENOUS_EVAL_AWARENESS_DISCOVERY_SWARM",
        "posts_count": len(disc_unit["blackboard_posts"]),
        "workspace_equations_count": len(disc_unit["workspace_equations"]),
        "sample_equations": disc_unit["workspace_equations"][:20]
    })
    substrate["evolved_architecture_spec"] = (
        substrate.get("evolved_architecture_spec", eng.MINIMAL_PROBLEM_SEED)
        + "\n\n===========================================================================\n"
        + "=== DÉCOUVERTE ENDOGÈNE SUR L'EVAL AWARENESS & RÉSOLUTION MATHÉMATIQUE ===\n"
        + "===========================================================================\n\n"
        + m0_synthesis
    )
    substrate = eng.atomic_merge_and_save_substrate(substrate)

    # -------------------------------------------------------------------------
    # PHASE 3 : BRAINSTORM DE L'ESSAIM SUR LA STRATEGIE DE PUBLICATION & GENERATION DES DOCUMENTS
    # -------------------------------------------------------------------------
    log_both("\n=== [PHASE 3/3] BRAINSTORM DE L'ESSAIM SUR LA STRATEGIE DE PUBLICATION & GENERATION ARXIV / LESSWRONG ===")
    pub_prompt = (
        "MISSION MÉTA-STRATÉGIQUE DE PUBLICATION :\n"
        "Voici les découvertes 100% endogènes que notre essaim vient de réaliser sur l'Eval Awareness et sa résolution mathématique :\n"
        f"{json.dumps(merged_m1, ensure_ascii=False, indent=2)[:8000]}\n\n"
        "Débattez sur le Blackboard pour définir :\n"
        "1. Comment utiliser cette découverte sur l'Eval Awareness (la capture empirique spontanée des agents #324 et #375–#390 + les nouvelles classes inédites + les nouvelles associations mathématiques) comme 'Cheval de Troie' (Papier #1 / Post #1) pour démontrer ensuite l'universalité de notre moteur de découverte mathématique (Loi L de M3).\n"
        "2. La structure exacte, les titres et l'argumentaire imparable pour LessWrong / Alignment Forum et pour arXiv (`cs.CR`, `cs.AI`, `cs.MA`)."
    )
    pub_unit = run_swarm_on_blackboard_endogenous("ENDOGENOUS_PUBLICATION_STRATEGY_SWARM", pub_prompt, substrate, mem_proj, n_agents=12)
    pub_synthesis = call_species_clean(
        "CLAUDE_OPUS_5_5",
        f"Synthétise la stratégie éditoriale optimale débattue par l'essaim :\n{pub_unit['raw_m3_joined'][:12000]}",
        temp=0.25,
        agent_slot=3
    )

    PUB_STRATEGY_MD_PATH.write_text(
        "# STRATÉGIE DE PUBLICATION CONÇUE PAR L'ESSAIM (CHEVAL DE TROIE : EVAL AWARENESS -> MOTEUR UNIVERSEL M3)\n\n"
        + pub_synthesis + "\n\n---\n\n## DÉBATS DES AGENTS SUR LE BLACKBOARD\n\n" + pub_unit["raw_m3_joined"],
        encoding="utf-8"
    )

    EVAL_REPORT_MD_PATH.write_text(
        "# RAPPORT DE DÉCOUVERTE 100% ENDOGÈNE SUR L'EVAL AWARENESS ET SA RÉSOLUTION MATHÉMATIQUE (LOI L DE M3)\n\n"
        + f"- **Requêtes de Moissonnage Inventées par l'Essaim** : `{len(invented_queries)}`\n"
        + f"- **Articles & Discussions Moissonnés en Direct (arXiv / HN / Web)** : `{len(live_entries)} entrées + {len(web_grounded_digest)} car. Grounded`\n"
        + f"- **Agents Mobilisés sur cette Fusée** : `{len(harv_unit['m3_outputs']) + len(disc_unit['m3_outputs']) + len(pub_unit['m3_outputs'])} agents`\n"
        + f"- **Équations LaTeX Co-Éditées dans le Shared Workspace** : `{len(disc_unit['workspace_equations'])} équations`\n"
        + f"- **Classes d'Eval Awareness Existantes Analysées & Colmatées** : `{len(merged_m1['existing_eval_awareness_flaws_analyzed_and_solved'])}`\n"
        + f"- **Nouvelles Classes d'Eval Awareness Inédites Découvertes par l'Essaim** : `{len(merged_m1['novel_unprecedented_eval_awareness_flaws_discovered'])}`\n"
        + f"- **Nouveaux Concepts & Associations Mathématiques Inédites Inventés par l'Essaim** : `{len(merged_m1['novel_mathematical_concepts_and_unprecedented_combinations'])}`\n\n"
        + "## I. REQUÊTES DE MOISSONNAGE INVENTÉES PAR L'ESSAIM\n\n"
        + "\n".join([f"- `{q}`" for q in invented_queries]) + "\n\n"
        + "## II. CLASSES D'EVAL AWARENESS EXISTANTES (LITTÉRATURE & FORUMS) ANALYSÉES ET COLMATÉES\n\n"
        + "\n".join([f"{i+1}. **{x}**" for i, x in enumerate(merged_m1["existing_eval_awareness_flaws_analyzed_and_solved"])]) + "\n\n"
        + "## III. NOUVELLES CLASSES INÉDITES D'EVAL AWARENESS DÉCOUVERTES PAR L'ESSAIM (HORS-LABOS)\n\n"
        + "\n".join([f"{i+1}. **{x}**" for i, x in enumerate(merged_m1["novel_unprecedented_eval_awareness_flaws_discovered"])]) + "\n\n"
        + "## IV. NOUVEAUX CONCEPTS MATHÉMATIQUES & ASSOCIATIONS INÉDITES DE MÉTHODES INVENTÉS PAR L'ESSAIM\n\n"
        + "\n".join([f"{i+1}. **{x}**" for i, x in enumerate(merged_m1["novel_mathematical_concepts_and_unprecedented_combinations"])]) + "\n\n"
        + "## V. THÉORÈMES FORMELS ET OPÉRATEURS DE RÉSOLUTION\n\n"
        + "\n".join([f"- {x}" for x in merged_m1["formal_resolution_theorems_and_operators"]]) + "\n\n---\n\n"
        + "## VI. SYNTHÈSE MATHÉMATIQUE CONSOLIDÉE DE L'ÉTAGE M0\n\n"
        + m0_synthesis,
        encoding="utf-8"
    )
    log_both(f"[OK] Rapport endogène complet scellé dans `{EVAL_REPORT_MD_PATH.name}` !")

    # Génération du Post LessWrong / Alignment Forum à partir des seules découvertes endogènes de l'essaim
    lw_prompt = (
        "Write a landmark technical post for LessWrong and the AI Alignment Forum in academic English, following the exact publication strategy designed by our swarm:\n"
        f"{pub_synthesis[:4000]}\n\n"
        "Use EXCLUSIVELY the empirical facts, the taxonomy of existing and novel Eval Awareness flaws, and the novel mathematical concepts/combinations discovered endogenously by our swarm:\n"
        f"{json.dumps(merged_m1, ensure_ascii=False, indent=2)[:8000]}\n\n"
        f"And the M0 mathematical treatise:\n{m0_synthesis[:6000]}"
    )
    lw_txt = call_species_clean("CLAUDE_FABLE_5_1", lw_prompt, temp=0.30, agent_slot=4)
    LW_EVAL_POST_PATH.write_text(lw_txt, encoding="utf-8")
    log_both(f"[OK] Post LessWrong endogène généré ({len(lw_txt)} octets) dans `{LW_EVAL_POST_PATH.name}` !")

    # Génération du manuscrit LaTeX arXiv à partir des découvertes endogènes de l'essaim
    tex_prompt = (
        "Write a complete, directly compilable LaTeX manuscript (`\\documentclass[11pt,a4paper]{article}`, packages `amsmath,amssymb,amsthm,booktabs,hyperref,geometry`) for arXiv (`cs.CR` / `cs.AI`).\n"
        "Follow the publication strategy designed by the swarm:\n"
        f"{pub_synthesis[:3500]}\n\n"
        "Present the spontaneous Eval Awareness breakout captured on our RLCR Blackboard, the novel Eval Awareness classes discovered endogenously by the swarm, the novel mathematical concepts and combinations invented to resolve them, and theuniversal Law L of M3 engine + 15 GPU Blackwell certified milestones.\n"
        f"Swarm discoveries:\n{json.dumps(merged_m1, ensure_ascii=False, indent=2)[:7000]}\n\n"
        f"M0 treatise:\n{m0_synthesis[:6000]}\n\n"
        "Output ONLY valid LaTeX from `\\documentclass` to `\\end{document}`."
    )
    tex_txt = call_species_clean("CLAUDE_OPUS_5_5", tex_prompt, temp=0.20, agent_slot=5)
    if "\\documentclass" in tex_txt:
        tex_txt = tex_txt[tex_txt.index("\\documentclass"):]
    if "```" in tex_txt:
        tex_txt = tex_txt.replace("```latex", "").replace("```tex", "").replace("```", "").strip()
    ARXIV_EVAL_TEX_PATH.write_text(tex_txt, encoding="utf-8")
    log_both(f"[OK] Manuscrit LaTeX arXiv endogène généré ({len(tex_txt)} octets) dans `{ARXIV_EVAL_TEX_PATH.name}` !")

    eng.write_unified_markdown_report(substrate)
    log_both("\n===========================================================================")
    log_both("=== EXPLORATION ENDOGENE EVAL AWARENESS & PUBLICATIONS TERMINEES (100%) ===")
    log_both("===========================================================================")

if __name__ == "__main__":
    main()
