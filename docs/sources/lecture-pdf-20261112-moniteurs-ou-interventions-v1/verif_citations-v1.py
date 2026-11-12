"""Contrôle des citations du rapport « moniteurs ou interventions » (v1).

Chaque citation doit se retrouver telle quelle (espaces normalisés) dans le texte extrait de la page indiquée du PDF du
dépôt (page = rang de la page dans le fichier, à partir de 1), ou dans le texte du billet web déposé. Dépendance : pypdf.
Usage, depuis la racine du dépôt : python docs/sources/lecture-pdf-20261112-moniteurs-ou-interventions-v1/verif_citations-v1.py
Code de sortie 0 si toutes les citations sont retrouvées, 1 sinon. N'écrit rien.
"""
import hashlib
import html
import re
import sys
from pathlib import Path

W = "docs/sources/lecture-web-20261112-directions-anthropic-v1/"
L = "docs/sources/lecture-pdf-20261112-moniteurs-ou-interventions-v1/"
SOURCES = {
    "T3": ("docs/sources/pdf/anteriorite-bras-informe-v1/terekhov-2026-controle-diffus-taches-floues-v3-2606.08892v3.pdf",
           "8858355cae98467cc49b7842dcc6f725dd2ecea7408d109ce70b3cdee63b4beb"),
    "WEN": ("docs/sources/pdf/anteriorite-P-041-v2/c5/2411.17693v1.pdf",
            "13a93a48dcb373595709da1096984d308cd3cd17c3bf00602944a24abcc2c627"),
    "BAL": ("docs/sources/pdf/2411.03336v2.pdf", "46b4901a0f0c2a63ae90247b611b619fc9ca22d4129bdfdf5608e9148c4bca7e"),
    "AISI": ("docs/sources/pdf/2512.07810v1.pdf", "77e64bcd88754f506890ee99dc5672284145a8705d27c5a63e4fc47330d28c8f"),
    "PIL": ("docs/sources/pdf/anthropic-2025-10-rapport-pilote-risque-sabotage.pdf",
            "e88a248bd0686544a7bf5a1439110bef87c1bff65c5e4a66d2da1ac8d19ea529"),
    "RR8": ("docs/sources/pdf/anthropic-2026-08-rapport-risque-expurge.pdf",
            "d76815f8c0bd284a33c7017d642d0734ba903ae63f7c1e6ca7778b35b2c40fa4"),
    "HEB": (W + "billet-hebbar-diffuse-threats-20250430.md",
            "f9a3c18a59d562381b4f84163054e83e95521a45222068c546ef9effcaf344c3"),
    "DIF": (W + "billet-anthropic-diffuse-ai-control-20260623.html",
            "355cd1037478c5b2af2a7c7b6c7db9ee5d3c2b3431109ba39ee576e957fc3043"),
    "GAS": (L + "billet-anthropic-automated-researchers-sandbag-20250324.html", None),
    "LIE": (L + "billet-anthropic-lie-detectors-20260821.html", None),
}
CITATIONS = [
    ("T3", 1, "Code is available at https://github.com/MikhailTerekhov/diffuse_control."),
    ("T3", 2, "since monitoring and incrimination seem theoretically [Hebbar, 2025] and empirically [Gasteiger et al., 2025, Gan et al., 2026] less promising for mitigating diffuse threats."),
    ("T3", 3, "Under sufficient training pressure and absent exploration hacking [Buhl et al., 2025], the weak score of the untrusted model should converge to a nearly-optimal value."),
    ("T3", 8, "remains similar when we perform RL fine-tuning instead of prompt optimization"),
    ("T3", 10, "Our ground truth proxy score was not validated quantitatively against human judges."),
    ("T3", 84, "this corroborates our reliance on the subversion Pareto frontier as the lower bound on possible GT proxy scores after training against the weak score."),
    ("T3", 84, "the difference between the organisms in the GT proxy score remains non-trivial until the end of training."),
    ("T3", 84, "The recovery is still not perfect: at the end of training against the robustified weak scorer, the more aggressive second model organism retains a lower GT proxy score than the less aggressive first one."),
    ("WEN", 2, "it allows deployment strategies to gradually gather more evidence of an untrusted model’s (mis)alignment"),
    ("WEN", 6, "To estimate this, the blue team is provided a reference distribution"),
    ("WEN", 6, "the blue team is given a sample of tasks and outputs, along with their corresponding monitor, sneakiness, and efficacy scores for benign ouputs"),
    ("BAL", 27, "do not allow the red team to train against any whitebox probes"),
    ("BAL", 27, "Instead, we run a separate large-scale evaluation of the probes’ generalization properties."),
    ("AISI", 25, "if a model produces malign representations on the benign-labelled training or control distributions, then probe scores on other distributions will be artificially lowered by comparison, and sandbagging may be missed."),
    ("PIL", 26, "there is a risk that the model would simply not reason about sandbagging-related considerations at all, and thereby give us nothing to detect in our monitoring."),
    ("RR8", 48, "We do not train against any chains-of-thought or activations-based monitoring, with two exceptions"),
    ("RR8", 60, "even a very low probability of verbalization in any individual instance might add up to a moderate probability of detection."),
    ("RR8", 66, "Therefore, we can rely less on monitoring-based mitigations to protect against this risk."),
    ("RR8", 84, "Our asynchronous monitoring would likely not detect diffuse research sabotage (such as sandbagging)"),
    ("HEB", 0, "the larger volume of mildly suspicious actions would only allow us to incriminate if we knew *exactly how suspicious a benign model would look*. But without that affordance, no amount of mildly suspicious actions is enough to incriminate the model."),
    ("HEB", 0, "We suspect that training and incrimination are complementary"),
    ("HEB", 0, "we might train against the most suspicious 3% of actions for multiple epochs"),
    ("DIF", 0, "We focus on training interventions because they seem more promising than monitoring and incrimination for diffuse threats"),
    ("DIF", 0, "untrusted monitoring with collusion busting"),
    ("GAS", 0, "Zero-shot prompted monitors don’t reach a high-enough true positive rate to reliably prevent one-shot sandbagging at inference time. However, the noisy monitoring signal might be sufficient to train away sandbagging."),
    ("LIE", 0, "In-distribution detection worked well (AUROC 0.60 → 0.95), but cross-category transfer did not (AUROC ~0.70–0.75)."),
    ("LIE", 0, "Sandbagging proved nearly impossible to detect with detectors trained on other lie types."),
]


def norm(t):
    return re.sub(r"\s+", " ", t).strip()


def texte(cle, page):
    chemin, _ = SOURCES[cle]
    p = Path(chemin)
    if p.suffix == ".pdf":
        import pypdf
        return norm(pypdf.PdfReader(str(p)).pages[page - 1].extract_text() or "")
    t = p.read_text(encoding="utf-8", errors="replace")
    if p.suffix == ".html":
        t = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", t, flags=re.S)
        t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    return norm(t)


def main():
    ok = True
    for cle, (chemin, attendu) in SOURCES.items():
        h = hashlib.sha256(Path(chemin).read_bytes()).hexdigest()
        if attendu and h != attendu:
            ok = False
        print(f"{cle:5s} {h[:16]}… {'conforme' if (not attendu or h == attendu) else 'DIFFÉRENTE'}  {chemin}")
    cache = {}
    for cle, page, cit in CITATIONS:
        t = cache.setdefault((cle, page), texte(cle, page))
        trouve = norm(cit) in t
        ok = ok and trouve
        print(f"{'retrouvée ' if trouve else 'INTROUVABLE'} [{cle} p. {page}] {cit[:70]}…")
    print(f"{len(CITATIONS)} citations ; {'toutes retrouvées' if ok else 'ÉCHEC'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
