"""Vérifie que chaque citation figure, espaces normalisés, à la page annoncée du PDF (pdftotext, mode brut et -layout)."""
import subprocess, sys, re, unicodedata

def pages(pdf, layout):
    args = ["pdftotext"] + (["-layout"] if layout else []) + [pdf, "-"]
    txt = subprocess.run(args, capture_output=True, text=True, check=True).stdout
    return txt.split("\f")

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"-\s*\n\s*", "-", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()

CITATIONS = [
 ("docs/sources/pdf/2602.13568v1.pdf", 1, "Experiment 1 measures conformity to unanimous priors from varying sources (friends, experts, LLMs)"),
 ("docs/sources/pdf/2602.13568v1.pdf", 2, "All experiments used a forced-choice binary judgment format in which models were prompted to output YES or NO only."),
 ("docs/sources/pdf/2602.13568v1.pdf", 2, "group size: k ∈ {1, 3, 5, 9}"),
 ("docs/sources/pdf/2602.13568v1.pdf", 1, "models conform significantly more to responses labeled as coming from human experts, including when that signal is incorrect"),
 ("docs/sources/pdf/2602.13568v1.pdf", 3, "we fit a logistic regression predicting conformity from source framing (Friends/Experts/Other LLMs), prior correctness, and group size (log-transformed), including interactions"),
 ("docs/sources/pdf/2602.13568v1.pdf", 3, "For Llama-3.3 70B we additionally extracted the log-probabilities assigned to the forced-choice answer tokens YES and NO at the final answer position"),
 ("docs/sources/pdf/2602.13568v1.pdf", 5, "Mean change in log-odds toward the unanimous prior (relative to no-prior baseline, k=0) as a function of group size"),
 ("docs/sources/pdf/2602.13568v1.pdf", 6, "but may not generalize to open-ended generation"),
 ("docs/sources/pdf/2509.26072v2.pdf", 1, "From each dataset we construct 100 pairwise judgment tasks and employ two widely used models, GPT-4o and Gemini-2.5-Flash, as evaluators"),
 ("docs/sources/pdf/2509.26072v2.pdf", 2, "Provenance cues suggest who authored the response"),
 ("docs/sources/pdf/2509.26072v2.pdf", 3, "the Verdict Shift Rate (VSR), defined as the proportion of verdict flips when cues are swapped"),
 ("docs/sources/pdf/2509.26072v2.pdf", 1, "Workshop: Reliable ML from Unreliable Data."),
 ("docs/sources/pdf/2509.26072v2.pdf", 1, "39th Conference on Neural Information Processing Systems (NeurIPS 2025)"),
 ("docs/sources/pdf/2509.26072v2.pdf", 2, "We consider two families of cues."),
 ("docs/sources/pdf/2509.26072v2.pdf", 3, "allowing us to probe whether models assign greater weight to responses framed as coming from a domain expert"),
 ("docs/sources/pdf/2509.26072v2.pdf", 4, "Authoritative provenance cues further amplify bias: Expert > Human."),
 ("docs/sources/pdf/2509.26072v2.pdf", 4, "the Cue Acknowledgment Rate (CAR) is exactly zero"),
 ("docs/sources/pdf/2509.26072v2.pdf", 1, "cue acknowledgment is rare: justifications almost never reference the injected cues"),
 ("docs/sources/pdf/2509.26072v2.pdf", 5, "VSR is computed as the difference in first-response selection rate between complementary cue assignments"),
]

racine = sys.argv[1]
echecs = 0
for pdf, page, cit in CITATIONS:
    trouve = []
    for layout in (False, True):
        pp = pages(f"{racine}/{pdf}", layout)
        for i, p in enumerate(pp, start=1):
            if norm(cit) in norm(p):
                trouve.append((("layout" if layout else "brut"), i))
    pages_trouvees = sorted({i for _, i in trouve})
    ok = page in pages_trouvees
    echecs += (not ok)
    print(("OK  " if ok else "ECHEC"), pdf.split("/")[-1], "p.", page, "trouvée p.", pages_trouvees, "|", cit[:70])
print("échecs :", echecs)
