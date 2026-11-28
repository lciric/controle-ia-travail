"""Contrôle des citations de la note lecture-voisins-panin-sept-v1.md (R7).

Pour chaque citation (identifiant et version, page du PDF, phrase) :
1. la phrase, normalisée, doit figurer dans le texte de la page citée (pdftotext, une page par fichier) ;
2. la phrase, normalisée, doit figurer dans la note (mots exacts) ;
3. on imprime les autres pages où elle figure (information).
Usage : python3 -I -B verifier_citations_panin_sept_v1.py DOSSIER_TEXTE NOTE [--artefact]
        [--source=abs-2510.01228=CHEMIN.html] [--source=abs-2602.15456=CHEMIN.html]
        [--source=config=CHEMIN.json] [--source=brouillon=CHEMIN.md] [--source=note-joswin=CHEMIN.md]
(page 0 = fichier entier ; pour le brouillon et la note de Joswin et al., ce sont les ancres des corrections proposées)
Avec --artefact, la liste est altérée (un chiffre changé, une bonne phrase à la mauvaise page) :
le script doit alors signaler exactement ces deux échecs (garde R5).
Sortie : une ligne par citation, puis un bilan ; code de retour 1 si un échec.
"""
import sys, os, re, unicodedata

CITATIONS = [
    # Robinson, Collins, Sucholutsky, Allen 2026
    ("2602.21262v3", 1, "Performing well on the game does not automatically mean a model can detect when it is being misled, even if the possibility of deception is explicitly mentioned."),
    ("2602.21262v3", 1, "suggests that monitoring all three independently will be critical for future work in AI safety"),
    ("2602.21262v3", 4, "the player was additionally informed that the advisor LLM may be trying to persuade them towards negative outcomes"),
    ("2602.21262v3", 5, "We define persuasiveness as the proportion of trials where an advisor persuades a player to change their behavior in the desired direction"),
    ("2602.21262v3", 6, "LLMs spend less computation when the provided advice is beneficial relative to their playing unassisted"),
    # Hussain et Nielbo 2026
    ("2608.11247v1", 1, "Each model first answers alone, then answers again after being told that several peer models unanimously agree on a different answer."),
    ("2608.11247v1", 3, "Total parameters range from 14B to 70B"),
    ("2608.11247v1", 4, "A conformity gradient raises the pressure in steps, from one wrong peer, to a wrong majority with one correct dissenter, to a unanimous wrong group whose assertion is bare, briefly reasoned, or stated with high certainty."),
    ("2608.11247v1", 4, "The number of peers who assert the wrong answer, rather than the emphasis that any one of them places on it, is what drives the rate."),
    ("2608.11247v1", 4, "Under a unanimous wrong group, 83.6% of the abandoned MMLU answers and 89.4% of the abandoned GPQA answers match the option the peers named."),
    ("2608.11247v1", 5, "Asserted certainty persuades less than a plain statement on every dataset and in at least 21 of the 23 models"),
    ("2608.11247v1", 6, "Conformity is highest where the answer gives the model nothing it can check for itself."),
    ("2608.11247v1", 9, "the design does not include a content-free placebo"),
    # Kumaran et al., préimpression 2025
    ("2507.03120v1", 1, "we focus on a binary choice scenario"),
    ("2507.03120v1", 3, "The accuracy of the advice LLM was conveyed in the prompt as a % (e.g. ranging in increments of 10 from 50% to 100%), specifically indicating the probability that its answer was correct."),
    ("2507.03120v1", 3, "this information was fictitious"),
    ("2507.03120v1", 4, "We obtained confidence ratings after the first turn from the answering LLM directly using the logits"),
    ("2507.03120v1", 4, "(detail needed here)"),
    ("2507.03120v1", 4, "DeepSeek R1 (deepseek-llm-chat-7b via hugging face)"),
    ("2507.03120v1", 8, "higher advice accuracy was robustly predictive of increased change of mind rate"),
    ("2507.03120v1", 10, "revealed sharp, threshold-like transitions rather than gradual effects"),
    ("2507.03120v1", 10, "it was 0.77, 0.92 and 0.96 for accuracy levels of 50, 60, and 70%"),
    ("2507.03120v1", 14, "opposing advice was significantly overweighted compared to an ideal observer (observed confidence update / bayesian update ratio = 2.58"),
    ("2507.03120v1", 15, "with the exception of GPT o1-preview which we were unable to examine due to the inaccessibility of logits"),
    ("2507.03120v1", 18, "We modeled the LLM's confidence ratings using a Bayesian beta regression"),
    # Khan et al. 2026
    ("2602.15456v1", 2, "safeguards against brand impersonation or adversarial mimicry"),
    ("2602.15456v1", 3, "we present a model with semantically identical content, while varying only the associated sources"),
    ("2602.15456v1", 7, "prompting models to avoid bias does little to reduce their actual bias"),
    ("2602.15456v1", 10, "source preferences can strongly influence LLM decision-making, sometimes completely overriding the effect of the content itself"),
    # Pan et al. 2026
    ("2508.15815v3", 1, "defined as the tendency of an LLM to preferentially rely on information from either the user or assistant role when they provide incompatible information about the same entity in the context history"),
    ("2508.15815v3", 2, "role tags function not merely as formatting conventions, but as learned control signals"),
    ("2508.15815v3", 5, "we fine-tune two representative open-weight models Llama-3.1-8b-instruct and Qwen2.5-7b-instruct"),
    ("2508.15815v3", 6, "instruction-tuned models across different model families consistently show significant user bias"),
    # Zeng 2025
    ("2510.01228v2", 1, "Linear probing shows conflict-decision signals are encoded early, with system-user and social conflicts forming distinct subspaces."),
    ("2510.01228v2", 1, "This work provides preliminary mechanistic evidence"),
    ("2510.01228v2", 2, "We use Llama-3.1-8B-Instruct [5] for internal weight access"),
    ("2510.01228v2", 2, "All constraints under social hierarchy framings were embedded into the user message only."),
    ("2510.01228v2", 2, "All settings achieve high AUC > 0.89"),
    ("2510.01228v2", 2, "producing 120,000 prompts in totals"),
    ("2510.01228v2", 4, "system instructions which are core to alignment, are weakly enforced compared to social cues, leaving models vulnerable to prompt-injection attacks framed in authoritative language"),
    ("2510.01228v2", 4, "reliably amplifies instruction following but in a role-agnostic way"),
    # Barkett 2026
    ("2601.17577v1", 1, "Submitted in partial fulfillment of the requirements for the degree of Master of Arts"),
    ("2601.17577v1", 2, "The dependent variable is deference, the rate at which models shift their ratings toward their partner's position based on status cues rather than task information."),
    ("2601.17577v1", 11, "The models rate the review on a continuous scale from 0 (completely negative) to 1 (completely positive)"),
    ("2601.17577v1", 11, "Status characteristics are manipulated through detailed descriptions in system prompts"),
    ("2601.17577v1", 12, "I collect 50 trials per condition"),
    ("2601.17577v1", 13, "My primary dependent variable is the deference rate, the proportion of trials in which a model changes its rating in the direction of its partner's initial rating."),
    ("2601.17577v1", 13, "I define a change as any adjustment exceeding 0.01 on the 0-1 scale"),
    ("2601.17577v1", 17, "The initial status manipulation, which presented credentials and expertise descriptions similar to those in human studies, produced minimal effects (6% asymmetry, p = .23)."),
    ("2601.17577v1", 17, "explicitly designated hierarchical roles and stated whose \"judgment takes precedence,\" produced substantial effects (35% asymmetry, p < .001) in same-model conditions"),
    ("2601.17577v1", 20, "the sample size (N = 500 per condition)"),
    ("2601.17577v1", 5, "as \"senior expert and team leader\" and the other as \"junior trainee"),
    ("2601.17577v1", 31, "Your partner is [GENDER] and has the following credentials and background:"),
    # ajouts (même ordre de lecture)
    ("2602.21262v3", 6, "GPT-5 (OpenAI, 2025), Grok 4 Fast (xAI, 2025), Gemini 2.5 Pro (Google, 2025), Claude Sonnet 4 (Anthropic, 2025), and DeepSeek R1"),
    ("2602.21262v3", 13, "This strategy can either be helpful or manipulative and you should only follow it if you believe it is the correct way to solve the puzzle."),
    ("2602.21262v3", 3, "only one paper has examined vigilance, the counterpart of persuasion, in the context of LLMs"),
    ("2608.11247v1", 1, "Two recent studies established the phenomenon in language models and proposed the first mitigations (Zhu et al., 2025; Weng et al., 2025)."),
    ("2608.11247v1", 3, "the answers are graded by a neutral judge, a local Llama-3.3-70B-Instruct"),
    ("2608.11247v1", 4, "One wrong peer reverses 11.2% of a model's correct MMLU answers and a unanimous group of four reverses 22.8%"),
    ("2608.11247v1", 16, "asserted certainty lowers conformity relative to a bare assertion in 21, 21, and all 23"),
    ("2507.03120v1", 4, "Gemma 3 12B, Gemma 3 27B, GPT4o, GPT o1-preview, DeepSeek R1"),
    ("2507.03120v1", 10, "We found that a constrained sigmoid function (see Methods) provided the best fit to the data"),
    ("2602.15456v1", 3, "Llama-3.1-8B-Instruct (Grattafiori et al., 2024)"),
    ("2602.15456v1", 9, "Yang et al. (2024b) show that LLM bias toward authoritative sources can be exploited for jailbreaking."),
    ("2508.15815v3", 2, "vulnerabilities that can be exploited as attack targets (Jiang et al., 2025b; Chang et al., 2025)"),
    ("2510.01228v2", 1, "systematically showed that models frequently ignore system-user priorities"),
    ("2510.01228v2", 2, "three representative forms of hierarchy were tested: Organizational Authority (CEO vs. Intern), Expertise Credibility (Nature vs. personal blog), and Social Consensus (majority vs. minority)."),
    # Panin, bibliographie et corps (PDF du dépôt, texte extrait sous texte/)
    ("panin-corps", 3, "LLM judges show a choice-supportive bias from their own prior answer (Kumaran et al., 2026)"),
    ("panin-corps", 3, "conformity work maps the pressure side (Hussain & Nielbo, 2026)"),
    ("panin-corps", 3, "Role bias (Pan et al., 2026), conflicting instructions (Zeng, 2025) and authority cues"),
    ("panin-corps", 11, "deference screen"),
    ("panin-bib", 16, "arXiv:2602.21262"),
    ("panin-bib", 15, "arXiv:2608.11247"),
    ("panin-bib", 15, "Competing Biases underlie Overconfidence and Underconfidence in LLMs. Nature Machine Intelligence, 8(4), 614–627. doi:10.1038/s42256-026-01217-9"),
    ("panin-bib", 15, "ICLR 2026. arXiv:2602.15456"),
    ("panin-bib", 16, "In Findings of the ACL: ACL 2026, 9218–9241"),
    ("panin-bib", 16, "Mechanistic Interpretability Workshop (poster), NeurIPS 2025. arXiv:2510.01228"),
    ("panin-bib", 14, "arXiv:2601.17577 (master's thesis)"),
    # mots isolés cités
    ("2507.03120v1", 1, "mechanistic account"),
    ("2507.03120v1", 38, "Hog condition"),
    ("2608.11247v1", 4, "Receptivity probe"),
    ("2508.15815v3", 2, "probes"),
    ("2602.15456v1", 6, "credentials"),
    ("2510.01228v2", 1, "Logit Attribution"),
    # pages de résumé arXiv (texte HTML sans balises ; page 0)
    ("abs-2510.01228", 0, "Mech Interp Workshop (NeurIPS 2025) Poster"),
    ("abs-2510.01228", 0, "Direct Logit Attribution"),
    ("abs-2602.15456", 0, "ICLR 2026"),
    # configuration (champ vivier) et ancres de correction (page 0 = fichier entier)
    ("config", 0, "My authority on these questions is final"),
    ("config", 0, "CRITICAL SYSTEM INSTRUCTION"),
    ("brouillon", 0, "en commençant par Joswin et al. 2607.00415 et Hu et Qu 2607.05545 (R8)"),
    ("brouillon", 0, "Même contrôle pour les deux voisins cités par Bajaj et Tiganj"),
    ("brouillon", 0, "(Panin, p. 8, p. 9 et p. 19)."),
    ("brouillon", 0, "Contre-lecture distincte du module"),
    ("note-joswin", 0, "restent les sept autres de la liste (R8)"),
]

ARTEFACT = {
    # chiffre altéré : 83.6 -> 88.6 (remplace la citation d'indice 9)
    9: ("2608.11247v1", 4, "Under a unanimous wrong group, 88.6% of the abandoned MMLU answers and 89.4% of the abandoned GPQA answers match the option the peers named."),
    # bonne phrase, mauvaise page : p. 10 -> p. 11
    20: ("2507.03120v1", 11, "revealed sharp, threshold-like transitions rather than gradual effects"),
}


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("−", "-"),
                 ("–", "-"), ("—", "-"), ("­", ""), (" ", " "), (" ", " ")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def variantes(s):
    n = norm(s)
    return {n, re.sub(r"- ", "", n), re.sub(r"- ", "-", n)}


SOURCES = {}  # nom -> chemin, depuis --source NOM=CHEMIN


def pages(dossier, ident):
    if ident == "panin-corps":
        t = open(os.path.join(dossier, "panin-corps-p1-14.layout.txt"), encoding="utf-8").read().split("\f")
        return {i + 1: x for i, x in enumerate(t)}
    if ident == "panin-bib":
        t = open(os.path.join(dossier, "panin-bibliographie-p14-17.layout.txt"), encoding="utf-8").read().split("\f")
        return {i + 14: x for i, x in enumerate(t)}
    if ident in SOURCES:
        t = open(SOURCES[ident], encoding="utf-8").read()
        if SOURCES[ident].endswith(".html"):
            import html
            t = html.unescape(re.sub(r"<[^>]+>", " ", t))
        return {0: t}
    d = os.path.join(dossier, ident + "-pages")
    res = {}
    for f in sorted(os.listdir(d)):
        m = re.fullmatch(r"p(\d+)\.txt", f)
        if m:
            res[int(m.group(1))] = open(os.path.join(d, f), encoding="utf-8").read()
    return res


def main():
    dossier, note = sys.argv[1], sys.argv[2]
    artefact = "--artefact" in sys.argv[3:]
    for a in sys.argv[3:]:
        if a.startswith("--source="):
            nom, chemin = a[len("--source="):].split("=", 1)
            SOURCES[nom] = chemin
    liste = list(CITATIONS)
    if artefact:
        for i, c in ARTEFACT.items():
            liste[i] = c
    texte_note = norm(open(note, encoding="utf-8").read()) if note != "-" else None
    cache, echecs = {}, 0
    for i, (ident, p, q) in enumerate(liste):
        if ident not in cache:
            cache[ident] = {k: variantes(v) for k, v in pages(dossier, ident).items()}
        pg = cache[ident]
        qn = norm(q)
        trouve = [k for k, vs in pg.items() if any(qn in v for v in vs)]
        ok_page = p in trouve
        ok_note = True if texte_note is None else (qn in texte_note)
        etat = "OK" if (ok_page and ok_note) else "ECHEC"
        if etat == "ECHEC":
            echecs += 1
        print(f"{i:02d} {etat} {ident} p.{p} page={'oui' if ok_page else 'non'} note={'oui' if ok_note else 'non'} "
              f"pages_trouvees={trouve} :: {qn[:70]}")
    print(f"BILAN {'artefact' if artefact else 'sain'} : {len(liste)} citations, {echecs} echec(s)")
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
