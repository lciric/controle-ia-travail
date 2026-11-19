#!/usr/bin/env python3
"""Contrôle des citations obligatoires de N-064 (point 4) et de N-067 (section 6 et liste « à citer »).

Vérificateur : modèle C. Lecture seule : aucune écriture git, aucun accès réseau, aucune recherche récursive.
Les PDF sont lus par `git show REF:CHEMIN` (lecture) vers un dossier provisoire, puis :
  (1) présence du PDF au chemin et sur la branche dits ;
  (2) empreinte SHA-256 complète, égale au préfixe cité et au compagnon `.sha256` ;
  (3) existence des pages citées (`pdfinfo`) ; phrase exacte attendue sur les pages contrôlées (`pdftotext`) ;
  (4) titre, numéro arXiv, version, date égaux à la première page.
Sortie : un JSON (et, avec --md, le tableau Markdown). Heures : `date -u` appelé par le programme.

Usage :
  python3 -I controler_citations_obligatoires_v1.py --depot /home/user/controle-ia-travail \
      --travail DOSSIER_PROVISOIRE --json SORTIE.json [--md SORTIE.md]
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

REFS = {
    "main": "main",
    "pieces": "refs/remotes/origin/prep/etat-de-l-art-niveau3-pieces-v1",
    "v1": "refs/remotes/origin/prep/etat-de-l-art-niveau3-v1",
}
BRANCHE_NOM = {
    "main": "main",
    "pieces": "prep/etat-de-l-art-niveau3-pieces-v1",
    "v1": "prep/etat-de-l-art-niveau3-v1",
}
C8 = "docs/sources/pdf/anteriorite-P-041-v2/c8/"
L4 = "docs/sources/pdf/niveau3-v1/lot4/"
POPPER_ICML = ("docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-"
               "agentic-sequential-falsifications.pdf")


def P(cle, groupe, nom, branche, chemin, chemin_donne, prefixe, arxiv, version, titre, date, pages, phrases,
      source, note=""):
    return dict(cle=cle, groupe=groupe, nom=nom, branche=branche, chemin=chemin, chemin_donne=chemin_donne,
                prefixe=prefixe, arxiv=arxiv, version=version, titre=titre, date=date,
                pages=pages, phrases=phrases, source=source, note=note)


# phrases : {page: phrase exacte attendue (blancs réduits, ligatures et guillemets normalisés)}
PIECES = [
    # ---------------- N-064, point 4 ----------------
    P("popper", "N-064", "POPPER (Huang, Jin, Li, Li, Candès, Leskovec, ICML 2025, PMLR 267)", "main", POPPER_ICML,
      "tronqué (« huang-2025-icml-pmlr-267-….pdf » dans N-064, point 2)", "a3c4b370", None, None,
      "Automated Hypothesis Validation with Agentic Sequential Falsifications", None,
      [2, 3, 4, 5, 14],
      {2: "H0 describes a family P0 of distributions that generate the data under the null",
       3: "Insufficient evidence, proceed with next falsification iteration i + 1",
       4: "E-values are our key instruments for Type-I error control.",
       5: "If an experiment fails because the protocol cannot be completed or the data are insufficient",
       14: "Algorithm 1 Sequential Falsification with HypothesisAgent"},
      "N-064 point 2 (p. 2-5 et algorithme 1 p. 14)"),
    P("dwork", "N-064", "Dwork et al., « Generalization in Adaptive Data Analysis and Holdout Reuse »", "main",
      C8 + "1506.02629.pdf", "non (arXiv 1506.02629 seul, N-064 point 3)", None, "1506.02629", None,
      "Generalization in Adaptive Data Analysis and Holdout Reuse", None, [20, 21],
      {20: "illustrates the danger of reusing a standard holdout",
       21: "reusing a standard holdout results in reported accuracy of over 63% for k = 500"},
      "N-064 point 3 (p. 20-21)",
      "PDF trouvé par `ls` du dossier c8 nommé dans N-067 (section 6), non cité nommément pour cette pièce."),
    P("blum", "N-064", "Blum et Hardt, « The Ladder: A Reliable Leaderboard for Machine Learning Competitions »",
      "main", C8 + "1502.04585.pdf", "non (arXiv 1502.04585 seul, N-064 point 3)", None, "1502.04585", None,
      "The Ladder: A Reliable Leaderboard for Machine Learning Competitions", None, [10, 11, 12],
      {10: "a new canonical attack that an adversarial analyst might perform",
       11: "5.1 Experiments with the boosting attack",
       12: "Even with this more effective attack, the Ladder mechanism"},
      "N-064 point 3 (p. 10-12)",
      "PDF trouvé par `ls` du dossier c8 nommé dans N-067 (section 6), non cité nommément pour cette pièce."),
    P("coscientist", "N-064", "Co-Scientist (Nature 655, p. 487-496)", None, None, "chemin non donné", None, None,
      None, None, None, [], {}, "N-064 point 4 ; N-067 section 6 (« les quatre de N-064 »)"),
    # ---------------- N-067 section 6, citations obligatoires ----------------
    P("qu", "N-067 obligatoire", "Qu, Chen, Wang (Propose, Don't Judge)", "main", C8 + "2609.27051.pdf", "oui",
      "2a8ded0119a1db42", "2609.27051", "1",
      "Propose, Don't Judge: An Anytime-Valid Referee for LLM Agents That Mine Investment Factors", "22 Sep 2026",
      [1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 22, 25, 29, 30, 36],
      {1: "the agent may propose, and a frozen statistical referee that the agent cannot touch must judge",
       2: "No prior system separates proposing from judging.",
       4: "The division of labour, the pipeline implementing it, and the experiment measuring it are ours.",
       6: "Verifier-in-the-loop adaptation means that the controller learns what the referee rewards.",
       8: "4.3 Many candidates: online e-BH over a frozen universe",
       10: "five years of trading days, was registered before the runs",
       11: "The trust kernel comprises the referee, the library, the point-in-time data layer, "
           "the append-only decision log and the cost meter.",
       12: "Its state Zt includes family statistics, the referee's diagnostics, open candidates, and paused families",
       13: "Leaky or No Referee",
       15: "The referee, not the controller, sets the number of false admissions",
       16: "Six memory arms (none, working, episodic, full, shuffled, oracle) run under the frozen referee",
       22: "are available from the corresponding author on request",
       25: "The four threats and their answers."},
      "N-067 sections 3, 4, 6, 7, 8 (pages dispersées)"),
    P("pace", "N-067 obligatoire", "Shawn (PACE)", "main", C8 + "2606.08106.pdf", "oui", "779f49607688fd06",
      "2606.08106", "1", "PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents", "6 Jun 2026",
      [5, 6, 7, 8],
      {5: "This is not a run-level familywise bound",
       6: "a unit test for acceptors",
       7: "5.2 Stochastic: don't chase sampling noise",
       8: "which is precisely why our gate is a single betting test rather than a multiplicity correction"},
      "N-067 section 6 (O11 p. 6, O12 p. 6-7, garantie par décision p. 5, 8)"),
    P("reuse", "N-067 obligatoire", "Sun, Zeng, She, Wang (REUSE)", "main", C8 + "2609.33180.pdf", "oui",
      "20639707e89ee9b1", "2609.33180", "2",
      None, "29 Sep 2026", [2, 6, 32],
      {2: "The third source arises from benchmark reuse.",
       6: "an LLM-based proposer generates modifications and a finite evaluation set is repeatedly reused",
       32: "decision-only proposer that causes a false promotion"},
      "N-067 section 6 (O12 p. 32 ; O9, O19 p. 2, 6)",
      "N-067 ne cite aucun titre pour REUSE ; titre de la première page relevé sans contrôle d'égalité."),
    P("erosion", "N-067 obligatoire", "So, Liu, Long (Masked Erosion)", "main", C8 + "2610.38392.pdf", "oui",
      "6a415ce487e61a71", "2610.38392", "1",
      "Masked Erosion: How Acceptance Gates Lose Redundant Safeguards in Self-Improving Agents", "28 Oct 2026",
      [2, 4, 8, 18, 24],
      {2: "Robust gates ask whether an accepted gain is real",
       4: "Each confirmatory prediction and its analysis code were frozen and hashed before the test ran",
       8: "it accepts a child only if every one-layer ablation stays protected",
       18: "fixed per task by a hash",
       24: "Before each round we froze its predictions and analysis code and hashed both"},
      "N-067 section 6 (O3, O17 p. 4, 24 ; O11 p. 2, 8) et section 3 (p. 18)"),
    P("confirm", "N-067 obligatoire", "Wei et al. (CONFIRM)", "pieces", L4 + "2611.01449v2.pdf", "oui",
      "9a02cc6d6b9897c8", "2611.01449", "2",
      "CONFIRM: Governing Scientific Reporting for Trustworthy Agentic Neuroimaging", "3 Nov 2026",
      [3, 5, 6, 9, 14, 19, 22],
      {3: "The original analysis plan must have been fixed and timestamped before results were observed.",
       5: "Search history and multiplicity",
       6: "We therefore constructed 150 designed negative controls",
       9: "evaluated 10,716 candidates, and none passed even provisionally",
       14: "Search history and multiplicity. The effective family size",
       19: "Table 8: Effect of removing each gate from CONFIRM-Full.",
       22: "The last two arms give CONFIRM's diagnosis for all 150 designed controls"},
      "N-067 section 6 (O2 p. 3, 5-6, 14 ; O12 p. 9, 22) et section 7 (p. 19)"),
    P("sargsyan", "N-067 obligatoire", "Sargsyan", "pieces", L4 + "2511.06701v4.pdf", "oui", "dfcd6dd1ee0bb136",
      "2511.06701", "4",
      "Structural Enforcement of Statistical Rigor in AI-Driven Discovery: A Functional Architecture",
      "25 Sep 2026", [5, 8, 9, 10, 11, 15, 16, 23, 25, 27, 28, 29],
      {5: "The system starts with a baseline model",
       8: "The first failure from Section 3—FDR inflation through naive thresholding—is eliminated by construction.",
       9: "validation data and the statistical test are controlled by the harness",
       10: "5.1. OS-Level Data Separation",
       11: "6. Formal Foundations: LORD in Lean 4",
       15: "it establishes FDR control at every fixed deterministic horizon",
       16: "a disjoint validation split, fixed before any testing",
       23: "an adversarial evaluation probing the data-separation b",
       25: "The naive approach inflates FDR to 41%; LORD controls it at 1.1%.",
       27: "7.3. Adversarial Leakage Evaluation",
       28: "Under the adversarial prompt, every well-formed generation attempted to read the validation file",
       29: "An adversarial model reads the validation file in every generation under the prompt-only baseline"},
      "N-067 sections 3, 6 (O2 p. 8-11, 15-16, 23, 25 ; O11 p. 27-29 ; base p. 5, 29)",
      "La phrase de p. 5 (« starts with a baseline model ») et celle de p. 29 ne disent pas que la base est fournie "
      "par le code du modèle : c'est `get_baseline` qui le dit, p. 9 et p. 27 (voir écarts)."),
    P("cads", "N-067 obligatoire", "Chen et al. (CADS)", "pieces", L4 + "2610.24597v1.pdf", "oui",
      "e923a544b27f7f21", "2610.24597", "1",
      "CADS: Measuring the Incremental Contribution of LLM Proposers in Sequential Biological Screens",
      "17 Oct 2026", [4, 5, 6, 7, 9, 11, 17, 23],
      {4: "converts each numerical readout into a bounded e-value under a one-sided contaminated-null model",
       5: "Deployment contract. The guarantee is conditional",
       6: "Theorem 2 (Registered-family CADS)",
       7: "The proposer's net contribution is the paired, post-hoc difference in oracle-scored true declarations",
       9: "The guarantee depends on the contamination model.",
       11: "A fixed non-LLM prior remains strongest.",
       17: "Four separated objects.",
       23: "Table S7: Contamination stress"},
      "N-067 sections 3, 6, 7 (O2 p. 4-6 ; O11 p. 9, 23 ; N-058 p. 7 ; p. 11, 17)"),
    P("nxn", "N-067 obligatoire", "Wang et al. (N×N E-valuation)", "pieces", L4 + "2608.06621v5.pdf", "oui",
      "d4d4682b52cfcff9", "2608.06621", "5", "N×N E-valuation", "26 Oct 2026", [1, 3, 4, 5, 7, 25, 26],
      {1: "must need nothing from the proposer but the hypothesis",
       3: "Two nulls replace the per-hypothesis resampling model, and neither is written for a hypothesis.",
       4: "Significance e-value.",
       5: "Base rate: identical rows too, but satisfied as often outside the scope, so no lift.",
       7: "We evaluate at three tiers.",
       25: "Some sessions wrote new hypotheses",
       26: "All 47 Matched and 23 Shared certificates clear the e-BH threshold on E sig"},
      "N-067 sections 3, 6 (O2 p. 1, 3-5, 7, 25-26)",
      "N-067 donne « N×N E-valuation » comme nom court ; le titre complet de la pièce est plus long."),
    P("hard", "N-067 obligatoire", "Zhang (Hard to Fool)", "pieces", L4 + "2611.06607v1.pdf", "oui",
      "add4e5be86142ce7", "2611.06607", "1",
      "Hard to Fool: A Bounded LLM Research Loop for Quantitative Finance, and What Two Dozen Campaigns Found",
      "4 Nov 2026", [1, 2, 3, 4, 6],
      {1: "the model is allowed to propose, and only trusted code is allowed to decide",
       2: "no LLM-discovered strategy survives certification",
       3: "are hashed into a campaign contract before the first proposal is evaluated",
       4: "replay consumes only a hash-verified quote artifact with no fallback price source",
       6: "the frozen specification for that campaign had been written to a temporary path and was not on disk "
          "when the holdout was requested"},
      "N-067 sections 3, 6 (O2 p. 1, 3-4 ; O17 p. 4 ; spécification reconstruite p. 6)"),
    P("hegazy", "N-067 obligatoire", "Hegazy, Jordan, Dieuleveut", "pieces", L4 + "2610.06432v1.pdf", "oui",
      "283d3e827032df04", "2610.06432", "1", "Valid Stopping in Adaptive Generator–Verifier Loops", "5 Oct 2026",
      [1, 2, 3],
      {1: "false acceptances may accumulate",
       2: "weighted online e-Benjamini–Hochberg",
       3: "Local evidence via e-values."},
      "N-067 section 6 (O2 (d) p. 2-3 ; adaptation au juge p. 1-2)"),
    P("proctor", "N-067 obligatoire", "Wahi (PROCTOR)", "main", C8 + "2609.02246.pdf", "oui", "9a2923ab00070a89",
      "2609.02246", "1", "LLM-as-a-Judge Is Not an Oracle", "2 Sep 2026", [1, 2, 4, 7],
      {1: "A syntactically broken prompt was promoted as the winning candidate because a silent parser "
          "fallback improved the metric.",
       2: "the LLM evaluator cannot be treated as an oracle",
       4: "No component both proposes and applies. No component both judges and acts.",
       7: "B1. Parser-fallback collapse"},
      "N-067 section 6 (O1 p. 4 ; O17 p. 1, 7 ; O10 p. 2)"),
    # ---------------- N-067 section 6, « à citer quand le point est abordé » ----------------
    P("a2606_11417", "N-067 à citer", "2606.11417 (Mittal, Gupta)", "main", C8 + "2606.11417.pdf", "oui",
      "7ae148beb5c73d30", "2606.11417", None, None, None, [1, 9, 10, 12],
      {1: "Signed Compression Progress on a Sealed Audit is Goodhart-Resistant",
       9: "Prediction error is Goodharted by noise",
       10: "Adaptive scalar-feedback overfitting",
       12: "The guarantee is conditional: it assumes a sealed audit"},
      "N-067 sections 3, 6 (O11, O12 ; p. 1, 9, 10, 12)"),
    P("discern", "N-067 à citer", "DISCERN 2609.17560", "main", C8 + "2609.17560.pdf", "non (chemin non donné)",
      "ef318a961de7d5f2", "2609.17560", None, None, None, [14, 26],
      {14: "Our evaluation was pre-registered.", 26: "Appendix C. Pre-registration and Seed Discipline"},
      "N-067 sections 3, 6 (O11 p. 14, 26)",
      "Chemin non donné par N-067 ; PDF trouvé par `ls` du dossier c8."),
    P("sgm", "N-067 à citer", "SGM 2510.10232", "main", C8 + "2510.10232.pdf", "non (chemin non donné)",
      "ad17c77e8f5f8e09", "2510.10232", None, None, None, [1, 6, 12],
      {1: "SGM separates adaptive proposal generation from confirmation",
       6: "ordinary transactions and hashes can implement them",
       12: "Stored records include frozen manifests and hashes"},
      "N-067 sections 3, 6 (O1 p. 1 ; O17 p. 6, 12)",
      "Chemin non donné par N-067 ; PDF trouvé par `ls` du dossier c8."),
    P("seal", "N-067 à citer", "SEAL 2607.24300", "main", C8 + "2607.24300.pdf", "non (chemin non donné)",
      "0a1434ea1c9b5338", "2607.24300", None, None, None, [1],
      {1: "The agent controls both the optimized object and its verifier."},
      "N-067 sections 3, 6 (O1 p. 1)", "Chemin non donné par N-067 ; PDF trouvé par `ls` du dossier c8."),
    P("a2611_04420", "N-067 à citer", "2611.04420 (Chen, Zhang, Zhang ; soumis, non publié)", "pieces",
      L4 + "2611.04420v1.pdf", "non (chemin non donné)", "731e03b1479e562d", "2611.04420", None, None, None,
      [2, 5, 6, 8, 10],
      {2: "increasingly pair an LLM proposer with an automated verifier",
       5: "E1-D2 (manipulation validity)",
       6: "4.2 Manipulation battery (E1-D2)",
       8: "48% of pairs (A) and 46% (D)",
       10: "The exploratory findings"},
      "N-067 sections 3, 6, 7 (O8, O11, N-058 ; p. 2, 5-6, 8, 10)",
      "Chemin non donné par N-067 ; PDF trouvé par `ls-tree` du dossier lot4 de la branche pieces."),
    P("a2611_00643", "N-067 à citer", "2611.00643 (Yang, Shi)", "pieces", L4 + "2611.00643v1.pdf",
      "non (chemin non donné)", "62be7556ef33cbbd", "2611.00643", None, None, None, [1, 2, 6, 10, 12, 16],
      {1: "Optimizing the harness for an LLM judge raised judge scores while sharply cutting precision for "
          "every generator.",
       2: "evolved harnesses",
       6: "R is a measure of excess truth relative to a calibrated LLM panel",
       10: "4.4 A precision check shows the cost of optimizing for judged novelty",
       12: "Table 5: Judge fitness, 24 fresh runs per arm",
       16: "What pre-registration did and did not protect."},
      "N-067 sections 3, 6, 7, 9 (voisin de O4 ; p. 1, 2, 6, 10, 12, 16)",
      "Chemin non donné par N-067 ; PDF trouvé par `ls-tree` du dossier lot4 de la branche pieces."),
    P("a2610_11289", "N-067 à citer", "2610.11289 (Adachi et al.)", "pieces", L4 + "2610.11289v1.pdf",
      "non (chemin non donné)", "d0655b6d49c5a5d2", "2610.11289", None, None, None, [2],
      {2: "Background knowledge compatibility"},
      "N-067 sections 3, 6 (voisin de O4, sens inverse ; p. 2)",
      "Chemin non donné par N-067 ; PDF trouvé par `ls-tree` du dossier lot4 de la branche pieces."),
]


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("∗", "*")):
        s = s.replace(a, b)
    s = re.sub(r"-\n(?=[a-z])", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def lettres(s):
    return re.sub(r"[^0-9a-zA-Zà-ÿ×]", "", norm(s))


def run(cmd, depot=None, binaire=False):
    r = subprocess.run(cmd, cwd=depot, capture_output=True, text=not binaire)
    return r


def git_show(depot, ref, chemin):
    r = run(["git", "-C", depot, "show", f"{ref}:{chemin}"], binaire=True)
    return r.stdout if r.returncode == 0 else None


def heure():
    return subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True).stdout.strip()


def controler(p, depot, travail):
    res = dict(cle=p["cle"], groupe=p["groupe"], nom=p["nom"], source_citation=p["source"], note=p["note"],
               chemin=p["chemin"], chemin_donne=p["chemin_donne"],
               branche=BRANCHE_NOM.get(p["branche"]) if p["branche"] else None,
               prefixe_cite=p["prefixe"], arxiv_cite=p["arxiv"], version_citee=p["version"],
               titre_cite=p["titre"], date_citee=p["date"], pages_citees=p["pages"])
    if p["branche"] is None:
        res.update(present=False, verdict="absent",
                   ecarts=["aucun chemin donné par N-064 ni N-067 ; aucun PDF recherché (pas de recherche "
                           "récursive) ; Nature 655, p. 487-496 non vérifiable ici"])
        return res
    octets = git_show(depot, REFS[p["branche"]], p["chemin"])
    comp = git_show(depot, REFS[p["branche"]], p["chemin"] + ".sha256")
    ecarts = []
    res["present"] = octets is not None
    if octets is None:
        res.update(verdict="absent", ecarts=[f"PDF absent de {BRANCHE_NOM[p['branche']]} au chemin dit"])
        return res
    pdf = Path(travail) / (p["cle"] + ".pdf")
    pdf.write_bytes(octets)
    h = hashlib.sha256(octets).hexdigest()
    res["sha256_complet"] = h
    res["compagnon_present"] = comp is not None
    if comp is None:
        res["egal_compagnon"] = False
        ecarts.append("compagnon .sha256 absent")
    else:
        hc = comp.decode().split()[0].lower()
        res["compagnon_valeur"] = hc
        res["egal_compagnon"] = (hc == h)
        if hc != h:
            ecarts.append("empreinte différente du compagnon .sha256")
    if p["prefixe"]:
        res["egal_prefixe"] = h.startswith(p["prefixe"].lower())
        if not res["egal_prefixe"]:
            ecarts.append(f"empreinte ne commence pas par {p['prefixe']}")
    else:
        res["egal_prefixe"] = None
    info = run(["pdfinfo", str(pdf)], binaire=False).stdout
    m = re.search(r"^Pages:\s+(\d+)", info, re.M)
    n = int(m.group(1)) if m else 0
    res["pages_pdf"] = n
    res["pages_existantes"] = {str(pg): (1 <= pg <= n) for pg in p["pages"]}
    for pg in p["pages"]:
        if not (1 <= pg <= n):
            ecarts.append(f"page {pg} inexistante (PDF de {n} pages)")

    def texte(pg):
        return run(["pdftotext", "-f", str(pg), "-l", str(pg), str(pdf), "-"], binaire=False).stdout

    # (4) première page
    t1 = texte(1)
    res["premiere_page_extrait"] = norm(t1)[:300]
    n1 = norm(t1)
    mm = re.search(r"arxiv:(\d{4}\.\d{4,5})v(\d+)", n1)
    res["arxiv_page1"] = mm.group(1) if mm else None
    res["version_page1"] = mm.group(2) if mm else None
    if p["arxiv"]:
        res["egal_arxiv"] = (res["arxiv_page1"] == p["arxiv"])
        if not res["egal_arxiv"]:
            ecarts.append(f"numéro arXiv de la page 1 ({res['arxiv_page1']}) différent de {p['arxiv']}")
    if p["version"]:
        res["egal_version"] = (res["version_page1"] == p["version"])
        if not res["egal_version"]:
            ecarts.append(f"version de la page 1 (v{res['version_page1']}) différente de v{p['version']}")
    if p["titre"]:
        res["egal_titre"] = lettres(p["titre"]) in lettres(t1)
        if not res["egal_titre"]:
            ecarts.append("titre cité absent de la première page")
    if p["date"]:
        res["egal_date"] = norm(p["date"]) in n1
        if not res["egal_date"]:
            ecarts.append(f"date citée ({p['date']}) absente de la première page")
    # (3) phrases
    res["pages_controlees"] = {}
    for pg, ph in p["phrases"].items():
        ok = (1 <= pg <= n) and (norm(ph) in norm(texte(pg)))
        res["pages_controlees"][str(pg)] = dict(phrase=ph, trouvee=bool(ok))
        if not ok:
            ecarts.append(f"phrase attendue non trouvée p. {pg} : « {ph} »")
    res["ecarts"] = ecarts
    res["verdict"] = "conforme" if not ecarts else "écart"
    return res


DECISIONS = [
    ("docs/decisions/decision-N-064-v1.md", "387c9d4e"),
    ("docs/decisions/decision-N-067-v1.md", "966dd9dc"),
    ("docs/decisions/contre-lecture-decisions-N-067-a-N-070-v1.md", "db44d995"),
]


def empreintes_decisions(depot):
    out = []
    for chemin, pref in DECISIONS:
        h = hashlib.sha256((Path(depot) / chemin).read_bytes()).hexdigest()
        out.append(dict(fichier=chemin, attendu=pref, sha256=h, egal=h.startswith(pref)))
    return out


def rendre_md(sortie):
    L = []
    L.append("# Contrôle des citations obligatoires de N-064 (point 4) et de N-067 (section 6) (v1)\n")
    L.append(f"- **Vérificateur : modèle C.** Début {sortie['debut_utc']}, fin {sortie['fin_utc']} (`date -u`, appelé par le programme).")
    L.append("- Programme qui rejoue les contrôles (1), (2), (4) et l'existence des pages, plus la présence de la phrase "
             "citée par page contrôlée : `docs/notes/lecture-o4-suite-v1/controler_citations_obligatoires_v1.py`. "
             "Données : `controle-citations-obligatoires-v1.json`.")
    L.append("- Empreintes des fichiers contrôlés : " + " ; ".join(
        f"`{d['fichier'].split('/')[-1]}` {d['sha256'][:16]}… " + ("= attendu" if d['egal'] else "DIFFÉRENT") +
        f" `{d['attendu']}…`" for d in sortie["decisions"]) + ".")
    r = sortie["resume"]
    L.append(f"- Verdicts : conforme {r['conforme']}, écart {r['ecart' if 'ecart' in r else 'écart']}, absent {r['absent']} "
             f"(sur {len(sortie['pieces'])} pièces ou lignes).")
    L.append("- Lecture : `main` lu par `git show main:CHEMIN` (le dossier de travail est sur la branche `lot/compte-organisme-v1`, non utilisée) ; "
             "branches `prep/…` lues par `git show refs/remotes/origin/…:CHEMIN`. Chemins non donnés retrouvés par `ls` non récursif "
             "des dossiers nommés (`docs/sources/pdf/`, `…/c8/`, `…/lot4/`) ; aucune recherche récursive.")
    L.append("- Lecture des phrases : blancs réduits, ligatures et guillemets typographiques normalisés, majuscules ignorées ; "
             "la phrase est cherchée sur la page indiquée seule (`pdftotext -f P -l P`).\n")
    L.append("## Écarts et réserves (en tête)\n")
    for t in sortie["ecarts_en_tete"]:
        L.append(f"- {t}")
    L.append("\n## Table\n")
    L.append("| pièce | chemin et branche | empreinte complète | = préfixe cité / = compagnon | pages citées (existantes) | phrase exacte par page contrôlée | verdict |")
    L.append("|---|---|---|---|---|---|---|")
    for p in sortie["pieces"]:
        if "sha256_complet" not in p:
            L.append(f"| {p['nom']} | chemin non donné | — | — | — | — | **{p['verdict']}** |")
            continue
        pages = ", ".join(str(k) + ("" if v else " (INEXISTANTE)") for k, v in p["pages_existantes"].items())
        ph = "<br>".join(f"p. {k} : « {v['phrase']} »" + ("" if v["trouvee"] else " (NON TROUVÉE)")
                          for k, v in p["pages_controlees"].items())
        pref = {True: "oui", False: "NON", None: "non cité"}[p["egal_prefixe"]]
        comp = "oui" if p["egal_compagnon"] else "NON"
        ch = f"`{p['chemin']}` (`{p['branche']}`) ; chemin donné : {p['chemin_donne']}"
        l4 = f"{p['arxiv_cite'] or '—'} v{p['version_page1'] or '?'} ; {p['pages_pdf']} pages"
        L.append(f"| {p['nom']} ({l4}) | {ch} | `{p['sha256_complet']}` | {pref} / {comp} | {pages} | {ph} | **{p['verdict']}** |")
    L.append("\n## Titre, arXiv, version, date contre la première page\n")
    L.append("| pièce | titre cité = page 1 | arXiv cité = page 1 | version citée = page 1 | date citée = page 1 |")
    L.append("|---|---|---|---|---|")
    def oui(v):
        return {True: "oui", False: "NON", None: "non cité"}[v]
    for p in sortie["pieces"]:
        if "sha256_complet" not in p:
            continue
        L.append(f"| {p['nom']} | {oui(p.get('egal_titre'))} | {oui(p.get('egal_arxiv'))} ({p['arxiv_page1']}) | "
                 f"{oui(p.get('egal_version'))} (v{p['version_page1']}) | {oui(p.get('egal_date'))} |")
    L.append("\n## Notes par pièce\n")
    for p in sortie["pieces"]:
        bits = [p["note"]] if p.get("note") else []
        bits += p.get("ecarts_manuels", [])
        if bits:
            L.append(f"- **{p['nom']}** (cité par : {p['source_citation']}) : " + " ".join(bits))
    return "\n".join(L) + "\n"


# écarts de lecture constatés à la main (non rejouables), ajoutés au verdict
ECARTS_MANUELS = {
    "sargsyan": ["N-067 section 3, ligne O2 (c) : « Sargsyan, p. 5, 29 (base fournie par le code du modèle) » ; "
                 "p. 5 (exemple courant : « The system starts with a baseline model ») et p. 29 (légende du "
                 "tableau 7, « prompt-only baseline » = bras de comparaison de l'expérience) ne disent pas cela ; "
                 "la page qui le dit est p. 27 (« generates a module with the functions optimize, get_baseline, "
                 "and evaluate_model ») et p. 9 (listing 3). Écart léger de numéro de page, sans effet sur le "
                 "sens de la ligne."],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--depot", default="/home/user/controle-ia-travail")
    ap.add_argument("--travail", required=True, help="dossier provisoire neuf pour les PDF extraits")
    ap.add_argument("--json", required=True)
    ap.add_argument("--md", default=None)
    a = ap.parse_args()
    Path(a.travail).mkdir(parents=True, exist_ok=True)
    debut = heure()
    resultats = [controler(p, a.depot, a.travail) for p in PIECES]
    for r in resultats:
        extra = ECARTS_MANUELS.get(r["cle"])
        if extra:
            r["ecarts_manuels"] = extra
            if r["verdict"] == "conforme":
                r["verdict"] = "écart"
    fin = heure()
    ecarts_en_tete = []
    for r in resultats:
        if r["verdict"] == "absent":
            ecarts_en_tete.append(f"**ABSENT : {r['nom']}** : " + "; ".join(r["ecarts"]) + ".")
    for r in resultats:
        if r["verdict"] == "écart":
            ecarts_en_tete.append(f"**ÉCART : {r['nom']}** : " + " ".join(r.get("ecarts", []) + r.get("ecarts_manuels", [])))
    for r in resultats:
        if r["chemin_donne"] != "oui" and r["verdict"] != "absent":
            ecarts_en_tete.append(f"Réserve (chemin non donné ou tronqué dans la décision) : {r['nom']} : chemin donné = "
                                  f"{r['chemin_donne']} ; PDF trouvé en `{r['chemin']}` sur `{r['branche']}`.")
    sortie = dict(
        verificateur="modèle C", debut_utc=debut, fin_utc=fin,
        fichiers_controles={
            "N-064": "docs/decisions/decision-N-064-v1.md (387c9d4e…)",
            "N-067": "docs/decisions/decision-N-067-v1.md (966dd9dc…)",
            "contre-lecture": "docs/decisions/contre-lecture-decisions-N-067-a-N-070-v1.md (db44d995…)"},
        refs=REFS, decisions=empreintes_decisions(a.depot), ecarts_en_tete=ecarts_en_tete,
        resume={v: sum(1 for r in resultats if r["verdict"] == v) for v in ("conforme", "écart", "absent")},
        pieces=resultats)
    Path(a.json).write_text(json.dumps(sortie, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if a.md:
        Path(a.md).write_text(rendre_md(sortie), encoding="utf-8")
    print(json.dumps(sortie["resume"], ensure_ascii=False))
    for r in resultats:
        print(r["cle"], r["verdict"], "; ".join(r.get("ecarts", []))[:200])


if __name__ == "__main__":
    sys.exit(main())
