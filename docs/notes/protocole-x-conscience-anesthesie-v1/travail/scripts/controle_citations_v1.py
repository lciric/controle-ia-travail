#!/usr/bin/env python3
"""Contrôle des renvois de page de la note : chaque motif doit se lire sur la page citée du PDF cité.
Usage : python3 -I controle_citations_v1.py DOSSIER_SOURCES [PDF_VOISIN]"""
import re, subprocess, sys

src = sys.argv[1]
voisin = sys.argv[2] if len(sys.argv) > 2 else None
F = {
 "G": "arxiv-2607.15495.pdf", "DN": "dehaene-naccache-commentaire-unicog-2026.pdf",
 "CE": "dehaene-naccache-commentaire-anthropic-cdn-2026.pdf", "K": "katlowitz-2026-nature.pdf",
 "N18": "naci-2018-scientific-reports.pdf", "NO": "nourski-2021-frontiers.pdf",
 "CO": "colombo-2019-neuroimage.pdf", "B24": "bayne-2024-tics.pdf", "UH": "arxiv-2601.11622.pdf",
 "PH": "arxiv-2512.19155.pdf", "LI": "arxiv-2506.22516.pdf", "RA": "arxiv-2608.05160.pdf", "MB": "arxiv-2603.18893.pdf", "OS": "arxiv-2610.31955.pdf", "SL": "sleeping-llm-rapport-experience-04.pdf",
}
C = [
 ("CO", 1, r"conscious experience may persist"), ("CO", 1, r"n . 5 each"),
 ("CO", 1, r"consciousness was present \(wakefulness, ?ketamine\)"),
 ("NO", 3, r"GD effects are suppressed when subjects are sedated but still conscious"),
 ("NO", 3, r"LD effects are preserved within the auditory cortex when the subjects are unconscious"),
 ("NO", 14, r"at subhypnotic doses of propofol when subjects were sedated, but still responsive"),
 ("K", 6, r"0\.397 . 0\.007"), ("K", 6, r"n = 368 units"), ("K", 6, r"0\.226 . 0\.009 \(356 units across 10 patients\)"),
 ("K", 6, r"recorded on microwire electrodes"),
 ("K", 8, r"246 out of 375 units significant"), ("K", 8, r"it is consolidation that is compromised"),
 ("K", 11, r"between 45 and 60"), ("K", 11, r"propofol as the main anaesthetic"),
 ("K", 13, r"GPT-2 large"), ("K", 13, r"fastText"), ("K", 13, r"non-contextual embedder"),
 ("K", 9, r"does not reside in the activity of single units or LFP in the hippocampus"),
 ("K", 14, r"available to anyone with a university affiliation"),
 ("N18", 3, r"limited to the auditory cortex"), ("N18", 2, r"brief \(5 minute\)"), ("N18", 11, r"Ramsay score 5"),
 ("N18", 4, r"consistent block order in deep sedation"),
 ("DN", 8, r"unable to reproduce the known signatures"), ("DN", 9, r"disrupted during sleep, anesthesia"),
 ("DN", 11, r"seems doubtful that ablating"), ("DN", 11, r"all past tokens"),
 ("DN", 10, r"the local-global test"), ("DN", 10, r"trace conditioning paradigm"), ("DN", 10, r"Preliminary results indicate"),
 ("B24", 5, r"speci.{1,3}city is population dependent"), ("B24", 11, r"bootstrapping approach"),
 ("G", 25, r"identify the k = 10 most strongly activated"), ("G", 25, r"random-direction control"),
 ("G", 26, r"CoLA acceptability"), ("G", 26, r"multi-hop reasoning, translation"),
 ("G", 27, r"ablation reduces the rate of experiential"), ("G", 28, r"matched-norm control perturbations"),
 ("G", 28, r"subjective experience of a person"),
 ("G", 61, r"open source implementation of Jacobian lens"), ("G", 32, r"plateau of around 25"),
 ("G", 22, r"pulled in. to the J-space on demand"), ("G", 24, r"can be sur-? ?faced to the J-space on demand"),
 ("G", 58, r"not relevant to assessing consciousness according to such theories"),
 ("G", 59, r"rules out the standard transformer architecture"),
 ("G", 1, r"strategic deliberation, evalu"),
 ("CE", 23, r"all identified via the J-lens"), ("CE", 33, r"replicated the core claims on Qwen 3\.6 27B"),
 ("CE", 45, r"twenty-five prompts from the Pile of length 128 tokens"), ("CE", 48, r"pretty cheap and easy to replicate"),
 ("CE", 17, r"highly uncertain about phenomenal consciousness"),
 ("UH", 3, r"GPT-2-medium \(345M"), ("UH", 3, r"n = 15 trials"),
 ("PH", 18, r"Raw PCI-A Inverts"),
 ("LI", 1, r"lack statistically significant indicators"), ("RA", 1, r"Ignition Index"),
 ("MB", 1, r"rating questions displace the probed state"),
 ("OS", 1, r"amplify across layers"),
 ("SL", 2, r"at target Layer 3"), ("SL", 2, r"0\.2656"), ("SL", 3, r"0\.2908"), ("SL", 2, r"233\.8"), ("SL", 3, r"8\.99"),
 ("SL", 4, r"0\.6830"), ("SL", 4, r"0\.7154"), ("SL", 4, r"0\.6075"), ("SL", 4, r"0\.5065"), ("SL", 4, r"0\.6125"),
 ("SL", 5, r"clear, monotonic drop"), ("SL", 5, r"0\.31"),
]

def page(pdf, p):
    t = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), pdf, "-"], capture_output=True, text=True).stdout
    return re.sub(r"\s+", " ", t.replace("-\n", "").replace("‐", "-"))

bons = mauvais = 0
for cle, p, motif in C:
    ok = re.search(motif, page(f"{src}/{F[cle]}", p), flags=re.I) is not None
    bons += ok; mauvais += (not ok)
    print(("OK   " if ok else "ÉCHEC"), cle, f"p.{p}", motif)
if voisin:
    for p, motif in ((6, r"should move together across the conditions"), (6, r"should predict behaviour it was not fitted to"),
                     (8, r"Steering along a random direction of the same norm"), (9, r"token for token")):
        ok = re.search(motif, page(voisin, p), flags=re.I) is not None
        bons += ok; mauvais += (not ok)
        print(("OK   " if ok else "ÉCHEC"), "FW", f"p.{p}", motif)
# épreuve sur artefact : un motif faux et une mauvaise page doivent échouer
art1 = re.search(r"0\.397 . 0\.007", page(f"{src}/{F['K']}", 7)) is not None
art2 = re.search(r"0\.497 . 0\.007", page(f"{src}/{F['K']}", 6)) is not None
print("épreuve sur artefact (mauvaise page refusée, chiffre altéré refusé) :", (not art1) and (not art2))
print(f"bilan : {bons} conformes, {mauvais} en échec")
