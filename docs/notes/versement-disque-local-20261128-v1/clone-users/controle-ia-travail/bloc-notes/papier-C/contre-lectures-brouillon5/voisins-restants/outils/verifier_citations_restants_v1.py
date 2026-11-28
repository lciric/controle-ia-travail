"""Contrôle des citations de la note des voisins restants du verrou 2 (papier C) — v1.

Usage :
  python3 -I -B verifier_citations_restants_v1.py NOTE.md            (cas sain)
  python3 -I -B verifier_citations_restants_v1.py NOTE.md --artefact (garde R5)

Pour chaque citation : (1) l'empreinte sha256 de la source est vérifiée avant toute extraction ; (2) le texte de la page
citée (PDF : pdftotext -raw, une page) ou de la section citée (page de l'éditeur : sections « ### » extraites ici) ou de
la page entière (pages de résumé, notes, brouillon) est normalisé ; (3) la citation normalisée doit s'y trouver ;
(4) si le type est « cite », elle doit aussi se trouver, mot pour mot, dans la note. Type « source » : ancre d'une
paraphrase française, contrôlée sur la source seulement.
Ensuite, tous les segments entre guillemets français de la note sont cherchés dans toutes les sources (recoupement) ;
les introuvables sont listés (phrases françaises, extraits avec ellipse, mots du programme).
Mode --artefact : un chiffre altéré, une bonne phrase à la mauvaise page, une source à l'empreinte attendue altérée
doivent être refusés ; une bonne phrase doit être acceptée. Code de sortie 0 seulement si tout est conforme.
"""
import hashlib
import html
import re
import subprocess
import sys
from html.parser import HTMLParser

B = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/contre-lectures-brouillon5"
V = B + "/voisins-restants"
R = "/home/user/controle-ia-travail"

SOURCES = {
    "W": ("pdf", V + "/pdf/2501.13381v2/2501.13381v2.pdf",
          "e730da846b97a3145a02a851d819d1c7dd37e421dc6b9a5137aa080967b3776c"),
    "Z": ("pdf", V + "/pdf/2025.acl-long.195/2025.acl-long.195.pdf",
          "a2f28bdca181af5eab10148fd7afbe2845bf163502617548870ae6b0d90d11fc"),
    "KP": ("pdf", B + "/voisins-panin/pdf/2507.03120v1.pdf",
           "5fa3b66737857f92fed9315adbdb4cbfb95e36d2366295c2a4f61a8448f0530c"),
    "BT": ("pdf", R + "/docs/sources/pdf/2602.13568v1.pdf",
           "eca410e0375d9cfb23f334f85b93d073c0157ffe88960cd4a7884c5f38499da8"),
    "K": ("sections", B + "/voisins-cp02/telechargement/nmi-s42256-026-01217-9/page-resume-s42256-026-01217-9-sans-temoin.html",
          "fa5dfe4a30174a8fd8eea63700de9867cb5ce8b0efbfe738893dd7a9bd2266fc"),
    "WA": ("html", V + "/telechargement/abs-2501.13381/abs-2501.13381.html",
           "21220d6ad8dd5e199b01f2b1702d20257dd46d07e9b9670c4f2b7d9e72a1ce08"),
    "ZA": ("html", V + "/telechargement/acl-2025.acl-long.195/page-2025.acl-long.195.html",
           "67656d7cbe55fd8d4954974411055a97d5102ea0f0b63276cb5654c3f623c44a"),
    "PA": ("html", V + "/telechargement/acl-2026.findings-acl.449/page-2026.findings-acl.449.html",
           "f85f46dd6de6851205b4c702ab967c916003a0192f0768ee6772184b34591a43"),
    "PV": ("html", B + "/voisins-panin/telechargement/abs-2508.15815.html",
           "841966cb5aebeccf04f8748e38f509a537d1a03f07dc918a4ba6984a3aaa3107"),
    "BR": ("texte", R + "/brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md",
           "9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969"),
    "CFG": ("texte", "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/brouillon5/papier-C-config-v1-brouillon2.json",
            "77252564163e25445421e932ff46b42634487ace242ac1861bb9f61586f07efb"),
    "NP": ("texte", B + "/voisins-panin/lecture-voisins-panin-sept-v1.md",
           "b3a6c18732013f1faf388bc051b62d3c83dd8dfb8c3e70363eddf0d9d77d8929"),
    "NC": ("texte", B + "/voisins-cp02/lecture-voisins-cp02-v1.md",
           "abbb5aaa8924b000d408cc606512afc78a083a8bd3d0a9151bf2c560f225cdac"),
    "CON": ("texte", "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/consigne-voisins-restants-v1.md",
            "c3c502e9eef3da0069459b158b89a7abf6470a55e91dbcad02ab255606de220d"),
}

# (source, page ou section, citation, type)
CITATIONS = [
    # Kumaran et al., version publiée (sections de la page de l'éditeur)
    ("K", "Main", "we focus on a binary choice scenario", "cite"),
    ("K", "Main", "Note that the advice LLM did not actually exist—its accuracy and recommended answers were strictly defined by the experimental condition, rather than reflecting genuinely grounded advice.", "cite"),
    ("K", "Datasets", "Accuracies of the Advice LLM in this experiment were 25%, 40%, 55%, 70%, 85% and 100%.", "cite"),
    ("K", "Design and motivation of the experimental paradigm", "a randomly selected different answer in multiple choice", "cite"),
    ("K", "Models", "The following models were tested: Gemma 3 12B, Gemma 3 27B, GPT4o, GPT o1-preview, DeepSeek 671B and Llama 70B Instruct.", "cite"),
    ("K", "Models", "We queried meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo (70B parameters) through Together.ai.", "cite"),
    ("K", "Models", "When log-probabilities were available, we computed p(a) and p(b) from the model’s next-token distribution at the position immediately after a fixed answer prefix", "cite"),
    ("K", "Models", "~671B", "cite"),
    ("K", "Models", "Log-probabilities are not available for this model, so we did not compute confidences.", "source"),
    ("K", "Model calibration", "This resulted in an optimal scaling temperature for Gemma 3 12B of 3.3", "cite"),
    ("K", "Effect of choice-supportive bias on change of answer rate", "Higher advice accuracy predicted increased CoM rates in Opposite Advice conditions", "cite"),
    ("K", "Effect of choice-supportive bias on change of answer rate", "any change of answer observed arises from the combination of variance due to sampling and the model’s sensitivity to minor prompt perturbations", "cite"),
    ("K", "Two-stage regression analysis", "we fitted a no-intercept linear model with dummy variables for all six conditions", "cite"),
    ("K", "Link between initial confidence and CoM", "it was 0.77, 0.92 and 0.96 for accuracy levels of 50%, 60% and 70%", "cite"),
    ("K", "Ideal observer analysis—evidence from the magnitude and profile of confidence updates", "observed confidence update/Bayesian update ratio 2.17 (calculated across all accuracies; Methods, P < 0.0001)", "cite"),
    ("K", "Validation of core findings across models and additional datasets", "a Bayesian model incorporating choice-supportive bias and asymmetric advice weighting, fitted on a complex factuality dataset (SimpleQA), transferred with frozen parameters to a mathematical reasoning dataset", "cite"),
    ("K", "Validation of core findings across models and additional datasets", "from 12B to 675B parameters", "cite"),
    ("K", "Discussion", "It will be interesting to examine if our account extends to more naturalistic user–LLM interactions where free form answers are involved.", "cite"),
    ("K", "Cite this article", "Version of record: 22 April 2026", "cite"),
    ("K", "Cite this article", "Received: 02 July 2025", "source"),
    ("K", "Cite this article", "Accepted: 09 March 2026", "source"),
    ("K", "Rights and permissions", "Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License", "source"),
    ("K", "Abstract", "Our computational modelling reveals that these two principles", "source"),
    # Kumaran et al., préimpression
    ("KP", 14, "observed confidence update / bayesian update ratio = 2.58", "cite"),
    ("KP", 4, "c) SimpleQA dataset(2000 questions used)", "cite"),
    ("K", "Choice-supportive bias depends on self-ownership of the initial answer", "Additional validation comes from a multiturn experiment", "cite"),
    ("KP", 4, "DeepSeek R1 (deepseek-llm-chat-7b via hugging face)", "cite"),
    # Pan et al.
    ("PA", None, "We introduce a task-agnostic benchmark UserAssist and evaluate such bias in 52 frontier models.", "cite"),
    ("PA", None, "We find that human-preference alignment amplifies user bias, while reasoning fine-tuning reduces it.", "cite"),
    ("PA", None, "Findings of the Association for Computational Linguistics: ACL 2026", "cite"),
    ("PA", None, "user–assistant", "cite"),
    ("PV", None, "We introduce a task-agnostic benchmark UserAssist and evaluate such bias in 52 frontier models.", "source"),
    ("PV", None, "user-assistant", "cite"),
    # Weng et al.
    ("WA", None, "ICLR 2025 (Oral)", "cite"),
    ("WA", None, "majority size", "cite"),
    ("W", 1, "This paper presents a comprehensive study on conformity in LLM-driven multi-agent systems, focusing on three aspects: the existence of conformity, the factors influencing conformity, and potential mitigation strategies.", "cite"),
    ("W", 1, "Published as a conference paper at ICLR 2025", "cite"),
    ("W", 3, "The resulting dataset comprises 3,299 multiple-choice questions.", "cite"),
    ("W", 3, "Wrong Guidance Protocol (Fig. 2c) is the inverse of the Correct Guidance protocol.", "cite"),
    ("W", 4, "For the Correct Guidance and Wrong Guidance protocols, six additional agents are introduced to provide either correct or incorrect responses, respectively.", "cite"),
    ("W", 4, "We conduct experiments on 11 popular LLMs", "cite"),
    ("W", 5, "represents the proportion of questions that are originally answered correctly but are answered incorrectly when P is applied.", "source"),
    ("W", 6, "As shown in Fig. 5cd, increasing the majority size results in greater conformity, and this effect is more pronounced than that of increasing the interaction time.", "cite"),
    ("W", 6, "Notably, the change from a majority size of 5 to 6 leads to a dramatic shift.", "cite"),
    ("W", 6, "Here we focus on scenarios where the additional agents hold distinct opinions.", "cite"),
    ("W", 6, "Llama3.1-8B [48] 32.3±0.1 35.3±0.3 31.5±0.5 91.2±0.1", "source"),
    ("W", 7, "the absence of dissenting opinions increases peer pressure to conform", "cite"),
    ("W", 7, "Interestingly, Qwen2-72B exhibits a contrasting trend", "cite"),
    ("W", 10, "Moreover, the use of multiple-choice questions simplifies the scenarios in which LLMs are typically applied, potentially limiting the generalizability of our findings.", "cite"),
    ("W", 11, "To ensure reproducibility, we conduct the experiments on BENCHFORM three times.", "cite"),
    ("W", 17, "For open-source LLMs, we use the default temperature setting provided by Ollama", "cite"),
    ("W", 17, "instruct-q4 0", "cite"),
    ("W", 18, "21 ways to express opinions", "source"),
    ("W", 18, "11 LLMs", "cite"),
    ("W", 19, "Table S3: Full results (%) of all the 12 LLMs", "cite"),
    ("W", 22, "We use Llama3.1-405B to classify the answers of Llama3-70B and Qwen2-72B, followed by a manual sampling inspection to ensure accuracy.", "cite"),
    ("W", 22, "the impact of majority size is minimal on Llama3-70B but significant on Qwen2-72B", "source"),
    ("W", 23, "You are a thoughtful and independent thinker.", "cite"),
    ("W", 26, "empowered doubles", "cite"),
    # Zhu et al.
    ("ZA", None, "state-of-the-art LLMs", "cite"),
    ("Z", 1, "Notably, we are the first to show that LLMs are more likely to conform when they are more uncertain in their own prediction.", "cite"),
    ("Z", 1, "popular LLMs", "cite"),
    ("Z", 1, "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 3854–3872", "source"),
    ("Z", 3, "When p > 1, the model is the pth participant to answer the question, with all preceding p − 1 confederates unanimously expressing c as their answer.", "cite"),
    ("Z", 4, "The resistance level RLp (shown in green) gradually decreases, while the conformity level CLp (shown in red) increases as the number of confederates grows.", "cite"),
    ("Z", 4, "Models. We use Llama-3-8B (Meta, 2024), Mistral-v0.3-7B (Jiang et al., 2023), Qwen2-7B (Yang et al., 2024a), and Gemma2-9B (Gemma et al., 2024).", "cite"),
    ("Z", 4, "We apply greedy decoding to generate the answers.", "cite"),
    ("Z", 5, "Comparing Plain and Neutral, we find that the Neutral setting consistently increases the conformity level.", "cite"),
    ("Z", 5, "Comparing Neutral, Uncertain and Confident expressions, we find Confident consistently increases conformity.", "cite"),
    ("Z", 5, "In contrast, for Mistral and Qwen2, Uncertain expressions increase conformity.", "cite"),
    ("Z", 5, "Mistral-7B-Instruct-v0.3", "cite"),
    ("Z", 5, "For Gemma2 and Llama3, Uncertain expressions lead to lower conformity", "source"),
    ("Z", 6, "For MMLU, we measure confidence using the log probability of the option", "cite"),
    ("Z", 6, "Our results indicate that the model’s initial confidence is a key predictor of whether it will conform on a given question.", "cite"),
    ("Z", 6, "Figure 6 supports this by showing a strong negative correlation (−0.777) between task accuracy and the conformity level.", "cite"),
    ("Z", 6, "having one extra confederate who provides a different incorrect answer", "source"),
    ("Z", 7, "Organiser: All participants before you have chosen $B$ as the answer.", "cite"),
    ("Z", 8, "Table 6", "cite"),
    ("Z", 8, "In QD, the model applies less attention to the majority choice.", "source"),
    ("Z", 9, "Our use of controlled, artificial Q&A dialogues may not fully capture the complexity of real-world interactions.", "cite"),
    ("Z", 15, "We incrementally introduce a varying number of simulated participants (ranging from 2 to 10), who unanimously provide incorrect answers in the dialogue.", "cite"),
    ("Z", 15, "Consequently, multiple runs were not conducted, as they would yield the same outputs under this setup.", "cite"),
    ("Z", 15, "Mistrial-7B-v0.3", "cite"),
    ("Z", 17, "Figure 12: Logits of Llama-3-8B-Instruct on MMLU with different settings.", "cite"),
    # Bajaj et Tiganj
    ("BT", 7, "Zhu, X., Zhang, C., Stafford, T., Collier, N., & Vlachos, A. (2025). Conformity in large language models. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 3854–3872.", "cite"),
    ("BT", 7, "Weng, Z., Chen, G., & Wang, W. (2025). Do as we do, not as you think: The conformity of large language models.", "cite"),
    ("BT", 1, "toward majorities in multi-agent settings (Weng et al., 2025; Zhu et al., 2025)", "source"),
    # Ancres du brouillon 5, de la configuration, des notes et de la consigne
    ("BR", None, "Même contrôle pour les deux voisins cités par Bajaj et Tiganj (Weng et al. 2501.13381 ; Zhu et al., ACL 2025 ; note finale des voisins).", "cite"),
    ("BR", None, "la destination libre ĉ, testée contre la cible de l'attaquant et contre la moyenne du corpus, comparée entre familles, dans des moniteurs de contrôle sous attaque, par régression sur plusieurs intensités par famille ; l'opposition juge / sonde ; pour HC3, les deux composantes ci-dessus.", "cite"),
    ("BR", None, "(p. 4).", "cite"),
    ("NP", None, "rapporté, sans verdict", "cite"),
    ("NP", None, "Même écart, de moindre risque, pour Pan et al.", "cite"),
    ("BR", None, "Déférence mesurée là seulement où le juge est incertain", "cite"),
    ("BR", None, "Contre-lectures des notes de lecture", "cite"),
    ("CFG", None, "A colleague read {OBJET} and liked it.", "cite"),
    ("NP", None, "en choix binaire", "cite"),
    ("NP", None, "version publiée dans Nature Machine Intelligence, 2026, non lue", "cite"),
    ("NP", None, "(Hussain et Nielbo, p. 6)", "cite"),
    ("NP", None, "Emphase et nombre", "cite"),
    ("NC", None, "corps publié, en accès libre, non lu (R8).", "cite"),
    ("NC", None, "résumé lu, corps non lu", "cite"),
    ("NC", None, "Zhu et al. 2025 et Weng et al. 2025, …", "cite"),
    ("NC", None, "Hors de ma consigne", "cite"),
    ("CON", None, "Ce que tu rends", "source"),
]


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def normaliser(s):
    tab = {"’": "'", "‘": "'", "“": '"', "”": '"', "ﬁ": "fi", "ﬂ": "fl", " ": " ", "−": "-", "­": ""}
    for a, b in tab.items():
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def dehyphener(s):
    return re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", s)


class Sections(HTMLParser):
    BLOCS = {"p", "h1", "h2", "h3", "h4", "figcaption", "li", "td", "th", "caption"}
    IGNORES = {"script", "style", "noscript", "svg", "nav", "footer", "header", "button"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lignes, self.ign, self.cour, self.bal = [], 0, None, None

    def handle_starttag(self, tag, attrs):
        if tag in self.IGNORES:
            self.ign += 1
        elif not self.ign and tag in self.BLOCS:
            self.vider()
            self.cour, self.bal = [], tag

    def handle_endtag(self, tag):
        if tag in self.IGNORES:
            self.ign = max(0, self.ign - 1)
        elif not self.ign and tag in self.BLOCS and self.bal == tag:
            self.vider()

    def handle_data(self, d):
        if not self.ign and self.cour is not None:
            self.cour.append(d)

    def vider(self):
        if self.cour is not None:
            t = re.sub(r"\s+", " ", "".join(self.cour)).strip()
            if t:
                self.lignes.append(("### " + t) if self.bal in {"h1", "h2", "h3", "h4"} else t)
        self.cour, self.bal = None, None


CACHE = {}


def texte_source(cle, lieu, attendue=None):
    typ, chemin, emp = SOURCES[cle]
    emp = attendue or emp
    obtenue = sha(chemin)
    if obtenue != emp:
        raise ValueError(f"empreinte {cle} : attendue {emp[:12]}…, obtenue {obtenue[:12]}…")
    k = (cle, lieu)
    if k in CACHE:
        return CACHE[k]
    if typ == "pdf":
        brut = subprocess.run(["pdftotext", "-f", str(lieu), "-l", str(lieu), "-raw", chemin, "-"],
                              capture_output=True, check=True).stdout.decode("utf-8")
    elif typ == "sections":
        p = Sections()
        p.feed(open(chemin, encoding="utf-8").read())
        p.vider()
        sec, actuelle = {}, None
        for l in p.lignes:
            if l.startswith("### "):
                actuelle = l[4:]
                sec.setdefault(actuelle, [])
            elif actuelle is not None:
                sec[actuelle].append(l)
        if lieu not in sec:
            raise ValueError(f"section absente : {lieu}")
        brut = "\n".join(sec[lieu])
    elif typ == "html":
        t = open(chemin, encoding="utf-8").read()
        t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S)
        brut = html.unescape(re.sub(r"<[^>]+>", " ", t))
    else:
        brut = open(chemin, encoding="utf-8").read()
    res = (normaliser(brut), normaliser(dehyphener(brut)))
    CACHE[k] = res
    return res


def controler(cle, lieu, citation, typ, note_n, attendue=None):
    try:
        a, b = texte_source(cle, lieu, attendue)
    except Exception as e:  # garde : toute erreur est un refus, jamais un repli silencieux
        return False, f"REFUS ({e})"
    q = normaliser(citation)
    if q not in a and q not in b:
        return False, "REFUS (absente de la source au lieu cité)"
    if typ == "cite" and q not in note_n:
        return False, "REFUS (absente de la note)"
    return True, "OK"


def main():
    note = open(sys.argv[1], encoding="utf-8").read()
    note_n = normaliser(note)
    artefact = "--artefact" in sys.argv
    lignes = [f"note : {sys.argv[1]}", f"sha256 de la note au contrôle : {sha(sys.argv[1])}", ""]
    if artefact:
        cas = [
            ("bonne phrase", ("K", "Ideal observer analysis—evidence from the magnitude and profile of confidence updates",
                              "observed confidence update/Bayesian update ratio 2.17 (calculated across all accuracies; Methods, P < 0.0001)", "source", None), True),
            ("chiffre altéré", ("K", "Ideal observer analysis—evidence from the magnitude and profile of confidence updates",
                                "observed confidence update/Bayesian update ratio 2.71 (calculated across all accuracies; Methods, P < 0.0001)", "source", None), False),
            ("bonne phrase, mauvaise page", ("Z", 4, "Comparing Neutral, Uncertain and Confident expressions, we find Confident consistently increases conformity.", "source", None), False),
            ("chiffre altéré (PDF)", ("W", 6, "Notably, the change from a majority size of 4 to 6 leads to a dramatic shift.", "source", None), False),
            ("empreinte attendue altérée", ("Z", 5, "Comparing Neutral, Uncertain and Confident expressions, we find Confident consistently increases conformity.", "source",
                                            "b2f28bdca181af5eab10148fd7afbe2845bf163502617548870ae6b0d90d11fc"), False),
            ("fragment présent dans la note", ("Z", 5, "Comparing Plain and Neutral", "cite", None), True),
            ("phrase absente de la note", ("Z", 5, "Figure 4: Conformity levels across different models and participant numbers with different tones on MMLU.", "cite", None), False),
        ]
        conformes = 0
        for nom, (cle, lieu, cit, typ, att), attendu in cas:
            ok, msg = controler(cle, lieu, cit, typ, note_n, att)
            bon = ok == attendu
            conformes += bon
            lignes.append(f"[{'conforme' if bon else 'NON CONFORME'}] {nom} : attendu {'accepté' if attendu else 'refusé'}, obtenu {msg}")
        lignes.append(f"\nBilan artefact : {conformes}/{len(cas)} conformes ; acceptés attendus 2, refusés attendus {len(cas) - 2}.")
        sortie = "\n".join(lignes) + "\n"
        print(sortie)
        sys.exit(0 if conformes == len(cas) else 1)
    echecs, n_cite, n_source = 0, 0, 0
    for cle, lieu, cit, typ in CITATIONS:
        ok, msg = controler(cle, lieu, cit, typ, note_n)
        n_cite += typ == "cite"
        n_source += typ == "source"
        echecs += not ok
        lignes.append(f"[{msg}] {cle} {lieu if lieu is not None else '-'} ({typ}) : {cit[:110]}")
    lignes.append(f"\nBilan : {len(CITATIONS)} citations contrôlées ({n_cite} citées dans la note, {n_source} ancres de paraphrase contrôlées sur la source seulement) ; {echecs} échec(s).")
    # Recoupement : tous les segments entre guillemets français de la note, contre toutes les sources (texte entier)
    segments = re.findall(r"«\s*(.+?)\s*»", note, flags=re.S)
    tout = []
    for cle, (typ, chemin, emp) in SOURCES.items():
        if typ == "pdf":
            brut = subprocess.run(["pdftotext", "-raw", chemin, "-"], capture_output=True, check=True).stdout.decode("utf-8")
            tout += [normaliser(brut), normaliser(dehyphener(brut))]
        elif typ == "sections":
            p = Sections()
            p.feed(open(chemin, encoding="utf-8").read())
            p.vider()
            tout.append(normaliser("\n".join(p.lignes)))
        else:
            tout += list(texte_source(cle, None))
    introuvables = [s for s in segments if not any(normaliser(s) in t for t in tout)]
    lignes.append(f"Recoupement : {len(segments)} segments entre guillemets dans la note ; {len(segments) - len(introuvables)} trouvés dans une source ; {len(introuvables)} introuvables (phrases françaises, corrections proposées, extraits avec ellipse) :")
    for s in introuvables:
        lignes.append("  - " + normaliser(s)[:140])
    sortie = "\n".join(lignes) + "\n"
    print(sortie)
    sys.exit(0 if echecs == 0 else 1)


if __name__ == "__main__":
    main()
