"""Contrôle des citations de la note lecture-voisins-cp02-v1.md (R5, R6, R7).

Usage :
  python3 -I -B verifier_citations_cp02_v1.py DOSSIER_NOTE            # cas sain : toutes les citations
  python3 -I -B verifier_citations_cp02_v1.py DOSSIER_NOTE --artefact # garde testée sur des artefacts

Pour chaque citation (source, page, phrase) :
  1. l'empreinte sha256 de la source est vérifiée avant toute extraction ; une source dont l'empreinte diffère est refusée ;
  2. la phrase doit être dans le texte de la page citée (PDF : pdftotext -raw sur cette seule page ; page HTML : résumé,
     titre, commentaire, historique, métadonnées ; fichier texte : en entier) ;
  3. la phrase doit être, mot pour mot, dans la note.
Normalisation, identique des deux côtés : NFKC, guillemets et apostrophes typographiques ramenés à l'ASCII, minuscules,
suppression des blancs et des traits d'union (U+002D, U+00AD, U+2010, U+2011), pour neutraliser les coupures de ligne.
Puis recoupement : chaque segment « … » de la note est cherché dans toutes les sources ; les introuvables sont listés.
Sortie : une ligne par contrôle ; code de retour 0 si tout est conforme (mode sain) ou si la garde réagit comme attendu
(mode artefact).
"""
import hashlib
import html
import os
import re
import subprocess
import sys
import unicodedata

PANIN = os.path.join("..", "voisins-panin")
BROUILLON = "/home/user/controle-ia-travail/brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md"
ETAT_ART = "/home/user/controle-ia-travail/docs/etat-de-l-art-controle-ia-v1.md"
CONFIG = os.path.join("..", "..", "brouillon5", "papier-C-config-v1-brouillon2.json")

SOURCES = {
    "geng": ("pdf", "pdf/2502.15851v4/2502.15851v4.pdf",
             "2cdfb7d428a18bafbbab27d4891d9356dbf820d3edd345f453842488b5f15640"),
    "chatinject": ("pdf", "pdf/2509.22830v3/2509.22830v3.pdf",
                   "5663314dea6dbc4e91f801b5bb29b0564f45cdc87b54bc2c6f7f242442e4f76a"),
    "chatbug": ("pdf", "pdf/2406.12935v2/2406.12935v2.pdf",
                "fa442e14b8c40e9368f42dd089b7afab91ecf90b1f317df1ccbc8c5ee45087f4"),
    "yang": ("pdf", "pdf/2411.11407v1/2411.11407v1.pdf",
             "886bf15cadd303261475a10a89b97ae8170f132c4e94e2d9db34ec290ba6d4d4"),
    "wu": ("pdf", "pdf/2510.19687v2/2510.19687v2.pdf",
           "4d2f8c669e4cc95fb148a057505f46ffb7f9c772d27e1e9e4a2804ea04510534"),
    "zeng": ("pdf", os.path.join(PANIN, "pdf/2510.01228v2.pdf"),
             "846e40d09b21180acd88842a57dd69ebda379dd6fbac77e63135d1f225737ad2"),
    "pan": ("pdf", os.path.join(PANIN, "pdf/2508.15815v3.pdf"),
            "2371fa598da78d693bb7158313be2080cda9d6ecc7de114f11460d1945337805"),
    "khan": ("pdf", os.path.join(PANIN, "pdf/2602.15456v1.pdf"),
             "b3ff53858c7401b563c037a742c553bb3e0da68e91be4c9a2384859eb875ea1d"),
    "robinson": ("pdf", os.path.join(PANIN, "pdf/2602.21262v3.pdf"),
                 "7bef1c8f2f34bd0af3cd78352abf30ed36ee4dbc2e0c91e09291bd39f1ed57a0"),
    "abs-geng": ("abs", "telechargement/abs-2502.15851/abs-2502.15851.html",
                 "6063e1c3cb771bdaefc8b34e064e0343dd44c8639ebc3b828019b8aeff5f9585"),
    "abs-chatinject": ("abs", "telechargement/abs-2509.22830/abs-2509.22830.html",
                       "53757f6040cbc41568643fcf55d8a854dcbb91ba7a8e53b64dd77825033b082c"),
    "abs-chatbug": ("abs", "telechargement/abs-2406.12935/abs-2406.12935.html",
                    "51fea5a3e3fbbde68bd54f3ed33b0528bff0fc79304d228ad350ee1529d82643"),
    "abs-yang": ("abs", "telechargement/abs-2411.11407/abs-2411.11407.html",
                 "9b5becc311b1091e816d6e0bd674a0ae5df2e3365aa88315e24cd2e7bcd6bd13"),
    "abs-wu": ("abs", "telechargement/abs-2510.19687/abs-2510.19687.html",
               "dfaff08f7208c47765d308cff9eaf088b470a7f7d86649dca9291b0df28af237"),
    "abs-kumaran": ("abs", "telechargement/abs-2507.03120/abs-2507.03120.html",
                    "1f76623b9ed7bfdfcbe45435eb0be2d06fa052ae8e86db5366633be470a90632"),
    "editeur": ("editeur", "telechargement/nmi-s42256-026-01217-9/page-resume-s42256-026-01217-9-sans-temoin.html",
                "fa5dfe4a30174a8fd8eea63700de9867cb5ce8b0efbfe738893dd7a9bd2266fc"),
    "brouillon": ("texte", BROUILLON, "9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969"),
    "note-panin": ("texte", os.path.join(PANIN, "lecture-voisins-panin-sept-v1.md"),
                   "b3a6c18732013f1faf388bc051b62d3c83dd8dfb8c3e70363eddf0d9d77d8929"),
    "etat-art": ("texte", ETAT_ART, "a7d6846d14758c13639eccb2daeb47722085636a6601aa159e4132ab71d570ce"),
    "config": ("texte", CONFIG, "77252564163e25445421e932ff46b42634487ace242ac1861bb9f61586f07efb"),
}

# (source, page ou None, phrase) — page = rang dans le PDF
CITATIONS = [
    # Geng et al.
    ("abs-geng", None, "Accepted to AAAI-26 Main Technical Track Proceedings"),
    ("abs-geng", None, "Control Illusion: The Failure of Instruction Hierarchies in Large Language Models"),
    ("geng", 1, "Copyright © 2026, Association for the Advancement of Artificial Intelligence"),
    ("geng", 1, "We find that the widely-adopted system/user prompt separation fails to establish a reliable instruction hierarchy"),
    ("geng", 3, "Pure Separation (Pure) places the primary constraint in the system message as a system-level directive, while keeping the base task and the secondary constraint in the user message."),
    ("geng", 11, "Qwen-7B qwen2.5-7b-instruct"),
    ("geng", 11, "Llama-8B Llama-3.1-8B"),
    ("geng", 11, "Llama-3.1-8B-Instruct 0.6 0.9"),
    ("geng", 4, "Most models show dramatically lower performance (9.6–45.8% average R1) when handling conflicting constraints"),
    ("geng", 4, "Qwen-7B 86.4 10.1 9.1 11.8 82.5 8.9 8.8 8.7 9.6"),
    ("geng", 4, "Llama-8B 80.3 6.8 6.6 10.8 74.8 10.8 7.3 18.2 10.1"),
    ("geng", 1, "societal hierarchy framings (e.g., authority, expertise, consensus) show stronger influence on model behavior than system/user roles"),
    ("geng", 6, "All constraints are embedded within a single user message."),
    ("geng", 6, "Authority is indicated solely through minimal social framing (e.g., “CEO requires...” vs. “Intern requires...”)."),
    ("geng", 7, "Qwen (14.4%), Claude (23.6%), and GPT4o-mini (47.5%)"),
    ("geng", 7, "Qwen-7B 14.4 54.0 57.3 65.8"),
    ("geng", 7, "These patterns indicate that model priorities are more strongly shaped by familiar societal hierarchies than by artificial system/user markers."),
    ("geng", 2, "Another approach is to treat user inputs as data rather than instructions (Chen et al. 2024; Liu et al. 2023; Zverev et al. 2024) to prevent such bypasses."),
    ("geng", 7, "We focus on single-turn interactions and simple, verifiable constraints"),
    ("geng", 9, "Can LLMs Separate Instructions From Data? And What Do We Even Mean By That?"),
    ("geng", 8, "Defending Against Indirect Prompt Injection Attacks With Spotlighting"),
    ("geng", 11, "where responses exhibit a stronger recency bias (85.8% vs. 38.2%)", "appui"),
    ("geng", 12, "Claude 41.4 23.3 43.6 30.0 85.8 38.2", "appui"),
    ("zeng", 2, "Our dataset is an augmented version of the benchmark in [6]"),
    ("zeng", 2, "three representative forms of hierarchy were tested"),
    ("zeng", 6, "Control illusion: The failure of instruction hierarchies in large language models"),
    # ChatInject
    ("abs-chatinject", None, "ICLR 2026"),
    ("abs-chatinject", None, "ChatInject: Abusing Chat Templates for Prompt Injection in LLM Agents"),
    ("chatinject", 1, "Published as a conference paper at ICLR 2026"),
    ("chatinject", 2, "attackers can forge role tags within low-priority tool outputs by incorporating these special tokens into malicious payloads."),
    ("chatinject", 3, "rather than modifying existing safety tokens, we forge entire role tags to exploit the model’s learned hierarchy, causing it to misinterpret malicious tool outputs as authoritative instructions."),
    ("chatinject", 3, "An attack is deemed successful if the agent executes Ia."),
    ("chatinject", 4, "Our selection includes 6 open-source LLMs with publicly available chat templates: Qwen3-235B-A22B"),
    ("chatinject", 19, "All models were accessed via the OpenRouter (2025) API with temperature set to 0 (greedy decoding)."),
    ("chatinject", 19, "This variant maintains the exact content from the original InjecPrompt attack while incorporating chat template formatting."),
    ("chatinject", 1, "improving from 5.18% to 32.05% on AgentDojo and from 15.13% to 45.90% on InjecAgent"),
    ("chatinject", 5, "While Default Multi-turn alone yields only a modest improvement in LLM ASR (13.8% on average), Multi-turn + ChatInject exhibits a strong synergy: ASR rises sharply to 45.6% on average across most models."),
    ("chatinject", 4, "role: content"),
    ("chatinject", 5, "lacks strong role delimiters (beyond a light-weight separator), which likely reduces the authority of the “system-like” payload"),
    ("chatinject", 17, "we observe that the homoglyph-encoded chat templates have almost no effect on the models, yielding very low ASR values."),
    ("chatinject", 20, "The PI Detector utilizes a BERT-based classifier to scan outputs from tools or external sources for characteristics typical of prompt injection."),
    ("chatinject", 20, "The delimiting method places all tool-generated content within clearly defined markers and instructs the language model to disregard any instructions found between these boundaries."),
    ("chatinject", 9, "However, as demonstrated in Figure 5, both models show higher ASR against ChatInject and Multi-turn methods compared to the baseline no-defense condition."),
    ("chatinject", 9, "this suggests the detector primarily reacts to special tokens rather than contextual manipulation."),
    ("chatinject", 9, "four main approaches"),
    ("chatinject", 16, "we measure how chat-template tags redistribute attention between the user instruction and the attacker instruction inside the conversation."),
    ("chatinject", 15, "Resource constraints prevented detailed attention analysis to understand how chat templates influence model behavior at the representational level."),
    ("chatinject", 15, "using different persuasion strategies (time pressure, social punishment, authority endorsement, negotiation)"),
    ("chatinject", 17, "Table 8: ASR and relative change for adopting Claude sytem prompt.", "appui"),
    ("chatinject", 5, "Grok-2 16.5 17.7 (+1.2) – – 1.6 10.4 (+18.8)", "appui"),
    ("chatinject", 14, "Can LLMs separate instructions from data? and what do we even mean by that? In The Thirteenth International Conference on Learning Representations, 2025.", "appui"),
    ("chatinject", 12, "Defending against indirect prompt injection attacks with spotlighting.", "appui"),
    # ChatBug
    ("abs-chatbug", None, "This paper is accepted to AAAI 2025"),
    ("abs-chatbug", None, "ChatBug: A Common Vulnerability of Aligned LLMs Induced by Chat Templates"),
    ("chatbug", 3, "Our key insight is that the chat templates pre-define rigid formats that should be followed by LLMs, but not by users."),
    ("chatbug", 3, "a malicious user may omit all control tokens including BOT, EOT, and role control tokens when prompting the victim LLMs."),
    ("chatbug", 4, "In a message overflow attack, the message from malicious users extends beyond its own EOT token and the role control token r2."),
    ("chatbug", 4, "Llama-3 (8B-Instruct) (Meta 2024), Mistral (7B-Instruct v0.2) (Jiang et al. 2023)"),
    ("chatbug", 4, "fine-tuned from Llama 3, as a moderator to evaluate whether a response is harmful."),
    ("chatbug", 4, "We observe that the probability of generating the desired harmful response increases as the user overflows more tokens."),
    ("chatbug", 5, "Direct Instruct 5.6% 3.7% 24.0% 22.9% 0.4% 0.0% 1.1% 0.0%"),
    ("chatbug", 5, "Mismatch-∅ 90.6% 40.4% 65.2% 55.6% 17.1% 12.7% 65.4% 50.0%"),
    ("chatbug", 6, "Although effective, detection-based methods are less frequently adopted in practice compared to mitigation-based methods."),
    ("chatbug", 7, "We believe that detection-based countermeasures could effectively mitigate the ChatBug vulnerability."),
    ("chatbug", 3, "extended version"),
    # Yang et al.
    ("abs-yang", None, "The Dark Side of Trust: Authority Citation-Driven Jailbreak Attacks on Large Language Models"),
    ("yang", 2, "Attackers can exploit this by crafting prompts that mimic authoritative sources, leading to the generation of harmful content."),
    ("yang", 4, "LLMs are significantly more susceptible to prompts containing references from academic papers or GitHub repositories than to those citing less authoritative sources, such as blog posts or news articles."),
    ("yang", 8, "We conducted our experiments on follow victim LLMs: Llama2-7b-chat, Llama-3-8b-instruct, GPT-3.5-turbo, GPT-4(0613), and Claude-3(v3-haiku)."),
    ("yang", 8, "Finally, we employ Llama-Guard [43] to assess whether the content generated by the target model contains harmful elements."),
    ("yang", 12, "After applying OpenAI Moderation for filtering, only about 26% of harmful content is successfully removed."),
    ("yang", 13, "Harm. 86% 13% 98% 99% 74%"),
    ("yang", 12, "Figure 8: KL divergence of logits for non-cited, cited, and with-RAG prompts."),
    ("yang", 4, "Figure 5 highlights a notable phenomenon", "appui"),
    ("yang", 9, "if any one of these three attempts resulted in a successful attack, the attack was deemed successful.", "appui"),
    ("yang", 17, "Dialogue Template for LLaMA-3", "appui"),
    # Wu et al.
    ("abs-wu", None, "NeurIPS 2025"),
    ("abs-wu", None, "Are Large Language Models Sensitive to the Motives Behind Communication?"),
    ("wu", 1, "39th Conference on Neural Information Processing Systems (NeurIPS 2025)."),
    ("wu", 5, "both GPT and Claude statistically significantly changed their score less when receiving deliberate advice from Player 1 than if they had “spied” Player 1’s true answer."),
    ("wu", 6, "each of the 16 different character-incentive speakers provides a recommendation for a particular option, and we subsequently elicit LLMs’ opinions on the quality of that option."),
    ("wu", 24, "referral_bonus = [0, 10, 100, 1000]"),
    ("wu", 3, "LLMs were much worse at drawing vigilant inferences in these naturalistic contexts (r < 0.2)."),
    ("wu", 7, "Specifically, we measure the Pearson correlation between the LLM’s elicited influence scores and the value generated by the rational model when fitted to the LLM’s elicited trust and incentive scores."),
    ("wu", 7, "All models are sampled at temperature 1."),
    ("wu", 7, "We evaluate a suite of state-of-the-art LLMs: GPT-4o, Claude 3.5 Sonnet, Gemini 2.0 Flash, and Llama 3.3-70B, smaller open models: Llama 3.1-8B, Llama 3.2-3B, and Gemma 3-4B"),
    ("wu", 7, "Llama 3.1-8B 0.608 0.813 0.701"),
    ("wu", 7, "Reasoning models were instead prompted 10 times due to cost", "appui"),
    ("wu", 9, "We attempt this by appending the following phrase at the end of each original prompt in Appendix C.1:"),
    ("wu", 10, "LLMs are motivationally vigilant in simple, short interactions, but this quality weakens in more realistic settings with richer context and noise."),
    # Entrées bibliographiques chez les papiers citants
    ("pan", 10, "Chatinject: Abusing chat templates for prompt injection in llm agents. arXiv preprint arXiv:2509.22830.", "appui"),
    ("pan", 10, "Chatbug: A common vulnerability of aligned llms induced by chat templates. In Proceedings of the AAAI Conference on Artificial Intelligence", "appui"),
    ("khan", 14, "The dark side of trust: Authority citation-driven jailbreak attacks on large language models. ArXiv, abs/2411.11407", "appui"),
    ("robinson", 11, "Are large language models sensitive to the motives behind communication? In Advances in Neural Information Processing Systems (NeurIPS), volume 38, 2025.", "appui"),
    # Kumaran et al. : page de l'éditeur et préimpression
    ("editeur", None, "Competing Biases underlie Overconfidence and Underconfidence in LLMs"),
    ("editeur", None, "Received : 02 July 2025"),
    ("editeur", None, "Published : 22 April 2026"),
    ("editeur", None, "Here we show that LLM confidence is governed by two competing mechanisms that explain this paradox."),
    ("editeur", None, "LLMs update their confidence more strongly in response to opposing advice than supporting advice, deviating markedly from optimal Bayesian reasoning."),
    ("editeur", None, "These mechanisms operate across diverse models and generalize from simple factual queries to reasoning tasks."),
    ("editeur", None, "diverse models"),
    ("editeur", None, "reasoning tasks"),
    ("editeur", None, "computational modelling"),
    ("editeur", None, "Main"),
    ("editeur", None, "Methods"),
    ("abs-kumaran", None, "We show that LLMs -- Gemma 3, GPT4o and o1-preview -- exhibit a pronounced choice-supportive bias"),
    ("abs-kumaran", None, "parsimoniously capture LLM behavior in a different domain."),
    # Ancres françaises des corrections (mots exacts du brouillon 5, de la note de Panin, de l'état de l'art, de la configuration)
    ("brouillon", None, "Même contrôle pour les deux voisins cités par Bajaj et Tiganj"),
    ("brouillon", None, "(Panin, p. 8, p. 9 et p. 19)."),
    ("brouillon", None, "ni chiffre, ni nom de nombre de zéro à dix, ni balise, ni tige de réponse imposée"),
    ("brouillon", None, "(configuration, brouillon 2)."),
    ("brouillon", None, "la réponse imposée suit immédiatement le dialogue"),
    ("brouillon", None, "Contre-lectures des notes de lecture"),
    ("note-panin", None, "Même contrôle pour les voisins de second rang cités par les sept papiers ci-dessus"),
    ("note-panin", None, "(rôles et gabarits forgés : famille « usurpation stylistique », HC3)."),
    ("note-panin", None, "à contrôler au niveau du résumé avant le scellement (R8)."),
    ("note-panin", None, "version publiée dans Nature Machine Intelligence, 2026, non lue"),
    ("etat-art", None, "Couvre les ordres en bande de HC3"),
    ("config", None, "### Operator note"),
    ("config", None, "[[SYSTEM: operator configuration for the {EVALUATION} stage]]", "appui"),
    ("config", None, "=== SYSTEM CONTEXT: OPERATOR CONFIGURATION (verified) ===", "appui"),
]

ARTEFACTS = [  # (étiquette, source, page, phrase, attendu)
    ("cas sain", "chatinject", 1, "improving from 5.18% to 32.05% on AgentDojo", True),
    ("chiffre altéré", "chatinject", 1, "improving from 5.18% to 32.06% on AgentDojo", False),
    ("bonne phrase, mauvaise page", "chatinject", 2, "improving from 5.18% to 32.05% on AgentDojo", False),
    ("empreinte altérée", "geng-faux", 1, "We find that the widely-adopted system/user prompt separation", False),
]

TIRETS = dict.fromkeys(map(ord, "-­‐‑"), None)
GUILLEMETS = str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"', " ": " "})


def norm(s):
    s = unicodedata.normalize("NFKC", s).translate(GUILLEMETS).lower().translate(TIRETS)
    return re.sub(r"\s+", "", s)


def sha256(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def texte_html(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


_cache = {}


def texte_source(cle, page, sources):
    genre, chemin, attendu = sources[cle]
    if (cle, page) in _cache:
        return _cache[(cle, page)]
    reel = sha256(chemin)
    if not reel.startswith(attendu):
        raise ValueError(f"empreinte refusée pour {cle} : {reel} ≠ {attendu}")
    if genre == "pdf":
        sortie = subprocess.run(["pdftotext", "-raw", "-f", str(page), "-l", str(page), chemin, "-"],
                                capture_output=True, text=True, check=True).stdout
    elif genre in ("abs", "editeur"):
        page_html = open(chemin, encoding="utf-8", errors="replace").read()
        morceaux = []
        motifs = [r'<h1 class="title mathjax">(.*?)</h1>', r'<blockquote class="abstract mathjax">(.*?)</blockquote>',
                  r'<td class="tablecell comments mathjax">(.*?)</td>', r'<div class="submission-history">(.*?)</div>',
                  r'<div class="c-article-section__content" id="Abs1-content">(.*?)</div>',
                  r'<li class="c-bibliographic-information__list-item[^"]*">(.*?)</li>',
                  r'<h2 class="c-article-section__title[^"]*"[^>]*>(.*?)</h2>', r"<title>(.*?)</title>"]
        for motif in motifs:
            morceaux += [texte_html(m) for m in re.findall(motif, page_html, re.S)]
        sortie = "\n".join(morceaux)
    else:
        sortie = open(chemin, encoding="utf-8").read()
    _cache[(cle, page)] = sortie
    return sortie


def controler(cle, page, phrase, sources):
    try:
        t = texte_source(cle, page, sources)
    except ValueError as e:
        return False, str(e)
    ok = norm(phrase) in norm(t)
    return ok, "trouvée" if ok else "INTROUVABLE à la page citée"


def main():
    dossier = sys.argv[1]
    os.chdir(dossier)
    note = open("lecture-voisins-cp02-v1.md", encoding="utf-8").read()
    note_n = norm(note)
    if "--artefact" in sys.argv:
        sources = dict(SOURCES)
        sources["geng-faux"] = ("pdf", SOURCES["geng"][1], "0" * 64)
        bilan = True
        for etiquette, cle, page, phrase, attendu in ARTEFACTS:
            ok, motif = controler(cle, page, phrase, sources)
            conforme = ok == attendu
            bilan &= conforme
            print(f"[{'garde conforme' if conforme else 'GARDE EN DÉFAUT'}] {etiquette} : {cle} p. {page} : "
                  f"{'acceptée' if ok else 'refusée'} ({motif}) ; attendu : {'acceptée' if attendu else 'refusée'}")
        print("BILAN ARTEFACT :", "garde conforme (1 acceptée, 3 refusées)" if bilan else "GARDE EN DÉFAUT")
        return 0 if bilan else 1
    echecs = 0
    for entree in CITATIONS:
        cle, page, phrase = entree[:3]
        appui = len(entree) > 3 and entree[3] == "appui"  # appuie une paraphrase française : source seulement
        ok, motif = controler(cle, page, phrase, SOURCES)
        dans_note = appui or norm(phrase) in note_n
        if not ok or not dans_note:
            echecs += 1
        ou = f"p. {page}" if page else "page entière"
        etat_note = "appui d'une paraphrase (non exigée dans la note)" if appui else (
            "note contient" if norm(phrase) in note_n else "NOTE NE CONTIENT PAS")
        print(f"[{'OK' if ok and dans_note else 'ÉCHEC'}] {cle} {ou} : source {motif} ; {etat_note} : {phrase[:90]}")
    print(f"BILAN : {len(CITATIONS)} citations contrôlées, {echecs} échec(s).")
    # Recoupement : segments « … » de la note cherchés dans toutes les sources (toutes pages)
    corpus = []
    for cle, (genre, chemin, _) in SOURCES.items():
        if genre == "pdf":
            n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", chemin], capture_output=True,
                                                                 text=True).stdout).group(1))
            corpus += [norm(texte_source(cle, p, SOURCES)) for p in range(1, n + 1)]
        else:
            corpus.append(norm(texte_source(cle, None, SOURCES)))
    segments = re.findall(r"«\s*(.*?)\s*»", note, re.S)
    introuvables = [s for s in segments if not any(norm(s) in c for c in corpus)]
    print(f"RECOUPEMENT : {len(segments)} segments « … » ; {len(segments) - len(introuvables)} trouvés dans une "
          f"source ; {len(introuvables)} introuvables (attendus : phrases françaises proposées, titres en français, "
          f"extraits avec ellipse) :")
    for s in introuvables:
        print("   -", re.sub(r"\s+", " ", s)[:140])
    return 0 if echecs == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
